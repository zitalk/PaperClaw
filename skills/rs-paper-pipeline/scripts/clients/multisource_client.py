#!/usr/bin/env python3
"""Multi-source discovery with source isolation, rate limiting and deduplication."""

from __future__ import annotations

import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from typing import Any, Callable

from clients.arxiv_client import (
    fetch_recent_candidates as fetch_arxiv_candidates,
    format_affiliations,
    format_authors,
    has_remote_sensing_signal,
)
from pipeline_config import install_urllib_proxy, load_config


CONFIG = load_config()
install_urllib_proxy()

QUERY_BUNDLES = (
    "salient object detection multimodal saliency",
    "multimodal vision sensor fusion missing modality",
    "multi-view multi-camera multi-object tracking",
    "UAV drone aerial visual perception",
    "training-free open-vocabulary open-set segmentation",
)
USER_AGENT = CONFIG.arxiv_user_agent
SEMANTIC_MIN_INTERVAL_SECONDS = 1.1
_semantic_last_request = 0.0


class ProviderUnavailable(RuntimeError):
    pass


def _date_window(target_date: str | None, days_back: int) -> set[str]:
    if target_date:
        day = datetime.strptime(target_date, "%Y%m%d").date()
        return {day.isoformat()}
    today = datetime.now().date()
    return {(today - timedelta(days=i)).isoformat() for i in range(max(days_back, 1))}


def _url(base: str, **params: Any) -> str:
    return f"{base}?{urllib.parse.urlencode(params)}"


def _retry_after(headers: Any, fallback: int) -> int:
    raw = headers.get("Retry-After") if headers else None
    try:
        return max(int(raw), fallback)
    except (TypeError, ValueError):
        return fallback


def _json_request(
    source: str,
    url: str,
    headers: dict[str, str] | None = None,
    before_request: Callable[[], None] | None = None,
    attempts: int = 3,
) -> dict[str, Any]:
    request_headers = {"User-Agent": USER_AGENT, "Accept": "application/json", **(headers or {})}
    for attempt in range(1, attempts + 1):
        if before_request:
            before_request()
        try:
            request = urllib.request.Request(url, headers=request_headers)
            with urllib.request.urlopen(request, timeout=45) as response:
                value = json.loads(response.read().decode("utf-8"))
            if not isinstance(value, dict):
                raise ProviderUnavailable("unexpected_response_schema")
            return value
        except urllib.error.HTTPError as exc:
            if exc.code in (401, 403):
                raise ProviderUnavailable(f"HTTP {exc.code} authentication_or_entitlement") from None
            if exc.code == 429 or 500 <= exc.code <= 599:
                if attempt < attempts:
                    wait_seconds = min(_retry_after(exc.headers, 2**attempt), 30)
                    print(f"  [{source}] HTTP {exc.code}，{wait_seconds}s 后重试 {attempt}/{attempts}")
                    time.sleep(wait_seconds)
                    continue
            raise ProviderUnavailable(f"HTTP {exc.code} request_failed") from None
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            if attempt < attempts:
                time.sleep(2**attempt)
                continue
            raise ProviderUnavailable(type(exc).__name__) from None
    raise ProviderUnavailable("retry_exhausted")


def _semantic_slot() -> None:
    global _semantic_last_request
    elapsed = time.monotonic() - _semantic_last_request
    if elapsed < SEMANTIC_MIN_INTERVAL_SECONDS:
        time.sleep(SEMANTIC_MIN_INTERVAL_SECONDS - elapsed)
    _semantic_last_request = time.monotonic()


def _clean_text(value: Any) -> str:
    text = re.sub(r"<[^>]+>", " ", html.unescape(str(value or "")))
    return re.sub(r"\s+", " ", text).strip()


def _normalize_doi(value: Any) -> str:
    text = str(value or "").strip()
    text = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", text, flags=re.IGNORECASE)
    return text.lower()


def _extract_arxiv_id(value: Any) -> str:
    text = str(value or "").strip()
    direct = re.fullmatch(r"(\d{4}\.\d{4,5}(?:v\d+)?)", text, re.I)
    if direct:
        return direct.group(1)
    match = re.search(
        r"(?:arxiv\.org/(?:abs|pdf)/|arXiv[.:/])(\d{4}\.\d{4,5}(?:v\d+)?)",
        text,
        re.I,
    )
    return match.group(1) if match else ""


def _paper_id(item: dict[str, Any]) -> str:
    if item.get("arxiv_id"):
        return str(item["arxiv_id"])
    if item.get("doi"):
        return f"doi:{_normalize_doi(item['doi'])}"
    source = re.sub(r"[^a-z0-9]+", "-", str(item.get("primary_source") or "source").lower()).strip("-")
    return f"{source}:{item.get('source_id') or _title_key(item.get('title', ''))[:48]}"


def _title_key(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(value or "").casefold())


def _candidate(
    *,
    source: str,
    source_id: str,
    title: Any,
    abstract: Any,
    published: Any,
    doi: Any = "",
    arxiv_id: Any = "",
    authors: list[str] | None = None,
    institutions: list[str] | None = None,
    venue: Any = "",
    url: Any = "",
) -> dict[str, Any] | None:
    date_value = str(published or "")[:10]
    title_value = _clean_text(title)
    if not title_value or not date_value:
        return None
    item: dict[str, Any] = {
        "paper_id": "",
        "arxiv_id": _extract_arxiv_id(arxiv_id),
        "doi": _normalize_doi(doi),
        "source_id": str(source_id or ""),
        "primary_source": source,
        "sources": [source],
        "title": title_value,
        "abstract": _clean_text(abstract),
        "published": date_value,
        "authors": format_authors(authors or []),
        "institutions": format_affiliations(institutions or []),
        "venue": _clean_text(venue),
        "url": str(url or "").strip(),
    }
    item["paper_id"] = _paper_id(item)
    # Keep the legacy key for downstream compatibility while the pipeline index
    # is migrated to source-agnostic paper IDs.
    item["arxiv_id"] = item["arxiv_id"] or item["paper_id"]
    return item


def _reconstruct_openalex_abstract(index: Any) -> str:
    if not isinstance(index, dict):
        return ""
    positions: list[tuple[int, str]] = []
    for word, offsets in index.items():
        if isinstance(offsets, list):
            positions.extend((int(offset), str(word)) for offset in offsets if isinstance(offset, int))
    return " ".join(word for _, word in sorted(positions))


def fetch_openalex(target_date: str) -> list[dict[str, Any]]:
    if not CONFIG.openalex_api_key:
        return []
    output: list[dict[str, Any]] = []
    for query in QUERY_BUNDLES:
        payload = _json_request(
            "OpenAlex",
            _url(
                "https://api.openalex.org/works",
                search=query,
                filter=f"from_publication_date:{target_date},to_publication_date:{target_date}",
                per_page=100,
                api_key=CONFIG.openalex_api_key,
            ),
        )
        for work in payload.get("results", []):
            if not isinstance(work, dict):
                continue
            authors: list[str] = []
            institutions: list[str] = []
            for authorship in work.get("authorships") or []:
                if not isinstance(authorship, dict):
                    continue
                author = authorship.get("author") or {}
                if isinstance(author, dict) and author.get("display_name"):
                    authors.append(str(author["display_name"]))
                for institution in authorship.get("institutions") or []:
                    if isinstance(institution, dict) and institution.get("display_name"):
                        institutions.append(str(institution["display_name"]))
            ids = work.get("ids") or {}
            primary_location = work.get("primary_location") or {}
            location_source = primary_location.get("source") or {} if isinstance(primary_location, dict) else {}
            item = _candidate(
                source="OpenAlex",
                source_id=work.get("id", ""),
                title=work.get("display_name") or work.get("title"),
                abstract=_reconstruct_openalex_abstract(work.get("abstract_inverted_index")),
                published=work.get("publication_date"),
                doi=work.get("doi"),
                arxiv_id=(ids.get("arxiv") if isinstance(ids, dict) else ""),
                authors=authors,
                institutions=institutions,
                venue=(location_source.get("display_name") if isinstance(location_source, dict) else ""),
                url=(primary_location.get("landing_page_url") if isinstance(primary_location, dict) else "")
                or work.get("doi")
                or work.get("id"),
            )
            if item:
                output.append(item)
    return output


def fetch_semantic_scholar(target_date: str) -> list[dict[str, Any]]:
    if not CONFIG.semantic_scholar_api_key:
        return []
    output: list[dict[str, Any]] = []
    fields = "paperId,title,abstract,publicationDate,authors,externalIds,url,openAccessPdf,venue,publicationVenue"
    for query in QUERY_BUNDLES:
        payload = _json_request(
            "Semantic Scholar",
            _url(
                "https://api.semanticscholar.org/graph/v1/paper/search",
                query=query,
                publicationDateOrYear=f"{target_date}:{target_date}",
                limit=100,
                fields=fields,
            ),
            headers={"x-api-key": CONFIG.semantic_scholar_api_key},
            before_request=_semantic_slot,
        )
        for work in payload.get("data", []):
            if not isinstance(work, dict):
                continue
            external_ids = work.get("externalIds") or {}
            authors = [str(author.get("name")) for author in (work.get("authors") or []) if author.get("name")]
            publication_venue = work.get("publicationVenue") or {}
            item = _candidate(
                source="Semantic Scholar",
                source_id=work.get("paperId", ""),
                title=work.get("title"),
                abstract=work.get("abstract"),
                published=work.get("publicationDate"),
                doi=external_ids.get("DOI") if isinstance(external_ids, dict) else "",
                arxiv_id=external_ids.get("ArXiv") if isinstance(external_ids, dict) else "",
                authors=authors,
                venue=work.get("venue") or (
                    publication_venue.get("name") if isinstance(publication_venue, dict) else ""
                ),
                url=work.get("url"),
            )
            if item:
                output.append(item)
    return output


def fetch_crossref(target_date: str) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for query in QUERY_BUNDLES:
        payload = _json_request(
            "Crossref",
            _url(
                "https://api.crossref.org/works",
                **{
                    "query.bibliographic": query,
                    "filter": f"from-online-pub-date:{target_date},until-online-pub-date:{target_date}",
                    "rows": 100,
                },
            ),
        )
        message = payload.get("message") or {}
        for work in message.get("items", []) if isinstance(message, dict) else []:
            authors = []
            for author in work.get("author") or []:
                name = " ".join(str(author.get(key, "")).strip() for key in ("given", "family")).strip()
                if name:
                    authors.append(name)
            titles = work.get("title") or []
            container_titles = work.get("container-title") or []
            item = _candidate(
                source="Crossref",
                source_id=work.get("DOI", ""),
                title=titles[0] if titles else "",
                abstract=work.get("abstract"),
                published=target_date,
                doi=work.get("DOI"),
                authors=authors,
                venue=container_titles[0] if container_titles else "",
                url=work.get("URL"),
            )
            if item:
                output.append(item)
    return output


def fetch_springer(target_date: str) -> list[dict[str, Any]]:
    if not CONFIG.springer_nature_api_key:
        return []
    output: list[dict[str, Any]] = []
    for query in QUERY_BUNDLES:
        payload = _json_request(
            "Springer Nature",
            _url(
                "https://api.springernature.com/meta/v2/json",
                api_key=CONFIG.springer_nature_api_key,
                q=f'keyword: "{query}" onlinedate:{target_date}',
                s=1,
                p=100,
            ),
        )
        for work in payload.get("records", []):
            if not isinstance(work, dict):
                continue
            urls = work.get("url") or []
            landing_url = ""
            for link in urls:
                if isinstance(link, dict) and link.get("value"):
                    landing_url = str(link["value"])
                    break
            item = _candidate(
                source="Springer Nature",
                source_id=work.get("identifier", ""),
                title=work.get("title"),
                abstract=work.get("abstract"),
                published=work.get("onlineDate") or work.get("publicationDate"),
                doi=work.get("doi"),
                authors=[str(value) for value in (work.get("creators") or [])],
                venue=work.get("publicationName"),
                url=landing_url,
            )
            if item:
                output.append(item)
    return output


def fetch_ieee(target_date: str) -> list[dict[str, Any]]:
    if not CONFIG.ieee_api_key:
        return []
    output: list[dict[str, Any]] = []
    compact_date = target_date.replace("-", "")
    for query in QUERY_BUNDLES:
        payload = _json_request(
            "IEEE Xplore",
            _url(
                "https://ieeexploreapi.ieee.org/api/v1/search/articles",
                apikey=CONFIG.ieee_api_key,
                querytext=query,
                start_date=compact_date,
                end_date=compact_date,
                max_records=200,
                start_record=1,
                format="json",
            ),
        )
        for work in payload.get("articles", []):
            if not isinstance(work, dict):
                continue
            authors: list[str] = []
            institutions: list[str] = []
            author_block = work.get("authors") or {}
            for author in author_block.get("authors", []) if isinstance(author_block, dict) else []:
                if author.get("full_name"):
                    authors.append(str(author["full_name"]))
                affiliation = author.get("affiliation")
                if isinstance(affiliation, list):
                    institutions.extend(str(value) for value in affiliation)
                elif affiliation:
                    institutions.append(str(affiliation))
            item = _candidate(
                source="IEEE Xplore",
                source_id=work.get("article_number", ""),
                title=work.get("title"),
                abstract=work.get("abstract"),
                published=work.get("insert_date") or work.get("publication_date"),
                doi=work.get("doi"),
                authors=authors,
                institutions=institutions,
                venue=work.get("publication_title"),
                url=work.get("html_url") or work.get("abstract_url"),
            )
            if item:
                output.append(item)
    return output


def fetch_elsevier_scopus(target_date: str) -> list[dict[str, Any]]:
    if not CONFIG.elsevier_api_key:
        return []
    output: list[dict[str, Any]] = []
    for query in QUERY_BUNDLES:
        payload = _json_request(
            "Elsevier Scopus",
            _url(
                "https://api.elsevier.com/content/search/scopus",
                query=query,
                date=target_date[:4],
                sort="-coverDate",
                count=25,
                view="STANDARD",
            ),
            headers={"X-ELS-APIKey": CONFIG.elsevier_api_key},
        )
        results = payload.get("search-results") or {}
        for work in results.get("entry", []) if isinstance(results, dict) else []:
            if not isinstance(work, dict):
                continue
            affiliations = []
            for affiliation in work.get("affiliation") or []:
                if isinstance(affiliation, dict) and affiliation.get("affilname"):
                    affiliations.append(str(affiliation["affilname"]))
            item = _candidate(
                source="Elsevier Scopus",
                source_id=work.get("dc:identifier", ""),
                title=work.get("dc:title"),
                abstract=work.get("dc:description"),
                published=work.get("prism:coverDate"),
                doi=work.get("prism:doi"),
                authors=[str(work.get("dc:creator"))] if work.get("dc:creator") else [],
                institutions=affiliations,
                venue=work.get("prism:publicationName"),
                url=work.get("prism:url"),
            )
            if item:
                output.append(item)
    return output


def _merge_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = []
    by_key: dict[str, dict[str, Any]] = {}
    for item in items:
        arxiv = _extract_arxiv_id(item.get("arxiv_id"))
        doi = _normalize_doi(item.get("doi"))
        title = _title_key(item.get("title"))
        keys = [key for key in (f"arxiv:{arxiv}" if arxiv else "", f"doi:{doi}" if doi else "", f"title:{title}" if title else "") if key]
        current = next((by_key[key] for key in keys if key in by_key), None)
        if current is None:
            current = dict(item)
            merged.append(current)
        else:
            current["sources"] = list(dict.fromkeys([*(current.get("sources") or []), *(item.get("sources") or [])]))
            for field in ("abstract", "authors", "institutions", "venue", "url", "doi"):
                old_value = str(current.get(field) or "")
                new_value = str(item.get(field) or "")
                if len(new_value) > len(old_value):
                    current[field] = item.get(field)
            new_arxiv = _extract_arxiv_id(item.get("arxiv_id"))
            if new_arxiv:
                current["arxiv_id"] = new_arxiv
        current["paper_id"] = _paper_id(current)
        current["arxiv_id"] = _extract_arxiv_id(current.get("arxiv_id")) or current["paper_id"]
        for key in keys:
            by_key[key] = current
        by_key[f"title:{_title_key(current.get('title'))}"] = current
        if current.get("doi"):
            by_key[f"doi:{_normalize_doi(current['doi'])}"] = current
        real_arxiv = _extract_arxiv_id(current.get("arxiv_id"))
        if real_arxiv:
            by_key[f"arxiv:{real_arxiv}"] = current
    return merged


def fetch_recent_candidates(
    max_results: int = 1200,
    days_back: int = 2,
    target_date: str | None = None,
) -> list[dict[str, Any]]:
    valid_days = _date_window(target_date, days_back)
    arxiv_items = fetch_arxiv_candidates(max_results=max_results, days_back=days_back, target_date=target_date)
    normalized: list[dict[str, Any]] = []
    for item in arxiv_items:
        normalized_item = _candidate(
            source="arXiv",
            source_id=item["arxiv_id"],
            title=item["title"],
            abstract=item["abstract"],
            published=item["published"],
            arxiv_id=item["arxiv_id"],
            venue="arXiv",
            url=f"https://arxiv.org/abs/{item['arxiv_id']}",
        )
        if normalized_item:
            normalized.append(normalized_item)

    if not CONFIG.multisource_enabled:
        return normalized

    providers: tuple[tuple[str, Callable[[str], list[dict[str, Any]]]], ...] = (
        ("OpenAlex", fetch_openalex),
        ("Crossref", fetch_crossref),
        ("Semantic Scholar", fetch_semantic_scholar),
        ("Springer Nature", fetch_springer),
        ("IEEE Xplore", fetch_ieee),
        ("Elsevier Scopus", fetch_elsevier_scopus),
    )
    for name, provider in providers:
        try:
            found: list[dict[str, Any]] = []
            for day in sorted(valid_days):
                found.extend(provider(day))
            found = [item for item in found if item.get("published") in valid_days]
            found = [item for item in found if has_remote_sensing_signal(f"{item.get('title', '')}\n{item.get('abstract', '')}")]
            normalized.extend(found)
            print(f"  [{name}] 日期内研究方向候选 {len(found)}")
        except ProviderUnavailable as exc:
            print(f"  [{name}] 跳过：{exc}")
        except Exception as exc:
            print(f"  [{name}] 跳过：{type(exc).__name__}")

    merged = _merge_items(normalized)
    merged.sort(key=lambda item: (str(item.get("published", "")), str(item.get("paper_id", ""))), reverse=True)
    print(f"  [多源去重] 原始 {len(normalized)}，合并后 {len(merged)}")
    return merged
