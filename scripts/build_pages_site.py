#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills" / "rs-paper-pipeline" / "scripts"))
from services.venue_policy import NON_MAIN, allowed_venue, load_policy
from services.research_taxonomy import classify_research, public_directions
REPORTS_DIR = ROOT / "daily_reports"
ISSUE_INDEX_PATH = ROOT / "papers" / "issue_index.json"
SITE_SOURCE_DIR = ROOT / "site"
REPO_URL = "https://github.com/zitalk/PaperClaw"
ISSUE_URL_PREFIX = f"{REPO_URL}/issues/"

_ORGANIZATION_SCORES = (
    (re.compile(r"\b(?:university|institute of technology)\b", re.IGNORECASE), 100),
    (re.compile(r"\b(?:agency|academy|corporation|company|limited|ltd|cloud|INP)\b", re.IGNORECASE), 90),
    (re.compile(r"\binstitute\b", re.IGNORECASE), 80),
    (re.compile(r"\bcollege\b", re.IGNORECASE), 60),
    (re.compile(r"\b(?:school|faculty)\b|\b(?:centre|center) for\b|\bresearch (?:centre|center)\b", re.IGNORECASE), 40),
    (re.compile(r"\b(?:laboratory|lab)\b", re.IGNORECASE), 20),
)
_COUNTRIES = (
    "China|India|Australia|Canada|France|Germany|Italy|Japan|Malaysia|Portugal|"
    "Singapore|Spain|Sweden|Switzerland|UK|USA|U\\.K\\.|U\\.S\\.A\\."
)
_ARXIV_ID_RE = re.compile(r"\d{4}\.\d{4,5}(?:v\d+)?")
_VENUE_ABBREVIATIONS = (
    (re.compile(r"IEEE Transactions on Multimedia", re.IGNORECASE), "TMM"),
    (re.compile(r"IEEE Transactions on Pattern Analysis and Machine Intelligence", re.IGNORECASE), "TPAMI"),
    (re.compile(r"IEEE Transactions on Image Processing", re.IGNORECASE), "TIP"),
    (re.compile(r"IEEE Transactions on Circuits and Systems for Video Technology", re.IGNORECASE), "TCSVT"),
    (re.compile(r"IEEE Transactions on Geoscience and Remote Sensing", re.IGNORECASE), "TGRS"),
    (re.compile(r"IEEE Transactions on Neural Networks and Learning Systems", re.IGNORECASE), "TNNLS"),
    (re.compile(r"^International Journal of Computer Vision$", re.IGNORECASE), "IJCV"),
    (re.compile(r"^Computer Vision and Image Understanding$", re.IGNORECASE), "CVIU"),
    (re.compile(r"^Pattern Recognition$", re.IGNORECASE), "PR"),
    (re.compile(r"Computer Vision and Pattern Recognition", re.IGNORECASE), "CVPR"),
    (re.compile(r"International Conference on Computer Vision", re.IGNORECASE), "ICCV"),
    (re.compile(r"European Conference on Computer Vision", re.IGNORECASE), "ECCV"),
    (re.compile(r"Winter Conference on Applications of Computer Vision", re.IGNORECASE), "WACV"),
    (re.compile(r"International Conference on Robotics and Automation", re.IGNORECASE), "ICRA"),
    (re.compile(r"Intelligent Robots and Systems", re.IGNORECASE), "IROS"),
    (re.compile(r"ACM International Conference on Multimedia", re.IGNORECASE), "ACM MM"),
    (re.compile(r"Neural Information Processing Systems", re.IGNORECASE), "NeurIPS"),
    (re.compile(r"International Conference on Machine Learning", re.IGNORECASE), "ICML"),
    (re.compile(r"International Conference on Learning Representations", re.IGNORECASE), "ICLR"),
    (re.compile(r"AAAI Conference on Artificial Intelligence", re.IGNORECASE), "AAAI"),
    (re.compile(r"International Joint Conference on Artificial Intelligence", re.IGNORECASE), "IJCAI"),
    (re.compile(r"Scientific Reports", re.IGNORECASE), "Sci Rep"),
    (re.compile(r"Engineering Research Express", re.IGNORECASE), "Eng Res Express"),
)
_DOI_VENUE_PREFIXES = (
    ("doi:10.1038/s41598-", "Sci Rep"),
    ("doi:10.1088/2631-8695/", "Eng Res Express"),
)
_CCF_GRADES = {entry["abbr"].upper(): entry.get("ccf", "") for entry in load_policy()["allow"]}


def _extract_section(markdown: str, heading: str) -> str:
    match = re.search(
        rf"^##\s+[^\n]*{re.escape(heading)}[^\n]*\n(.*?)(?=^##\s|\Z)",
        markdown,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def _extract_overview(markdown: str) -> str:
    section = _extract_section(markdown, "今日概况")
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", section) if part.strip()]
    return "\n\n".join(paragraphs[:2])


def _extract_highlights(markdown: str) -> list[str]:
    section = _extract_section(markdown, "今日亮点")
    return [line[2:].strip() for line in section.splitlines() if line.startswith("- ")]


def _display_authors(value: str, limit: int = 3) -> str:
    authors = [author.strip() for author in value.split(",") if author.strip()]
    if not authors:
        return "未公开"
    shown = authors[:limit]
    return ", ".join(shown) + (", et al." if len(authors) > limit else "")


def _organization_score(value: str) -> int:
    return max((score for pattern, score in _ORGANIZATION_SCORES if pattern.search(value)), default=-1)


def _join_broken_institution_chunks(value: str) -> list[str]:
    """Rejoin affiliation fragments split after connectors such as 'and' or 'of'."""
    chunks: list[str] = []
    pending = ""
    for raw_chunk in re.split(r"[；;]", value):
        chunk = re.sub(r"\s+", " ", raw_chunk).strip(" ,")
        if not chunk:
            continue
        pending = f"{pending} {chunk}".strip() if pending else chunk
        if re.search(r"\b(?:and|of|for|the)\s*$", pending, re.IGNORECASE):
            continue
        chunks.append(pending)
        pending = ""
    if pending:
        chunks.append(pending)
    return chunks


def _normalize_institution_name(value: str) -> str:
    institution = re.sub(r"\s+", " ", value).strip(" ,;；")
    institution = re.sub(
        r"^(?:the\s+)?authors?\s+(?:are|is)\s+with\s+",
        "",
        institution,
        flags=re.IGNORECASE,
    )
    if re.match(r"^(?:the\s+)?(?:school|department|faculty|college)\b", institution, re.IGNORECASE):
        embedded_university = re.search(
            r"\b(?:the\s+)?((?:[A-Z][\w&.'()/-]*\s+)*University\b.*)$",
            institution,
        )
        if embedded_university:
            institution = embedded_university.group(1)
    institution = re.sub(
        r"^China University of Chinese Academy of Sciences\b",
        "University of Chinese Academy of Sciences",
        institution,
        flags=re.IGNORECASE,
    )
    if re.search(r"\b(?:and|of|for|the)\s*$", institution, re.IGNORECASE):
        return ""
    return institution


def _is_secondary_unit(value: str) -> bool:
    return bool(
        re.match(
            r"^(?:the\s+)?(?:school|department|faculty|college|chair|"
            r"(?:state|national|provincial|province)?\s*key laboratory|"
            r"(?:centre|center) for)\b",
            value,
            re.IGNORECASE,
        )
    )


def _top_level_institution(value: str) -> str:
    cleaned = re.sub(r"^[\s*∗†‡\d.(]+", "", value).strip(" ,;；")
    if not cleaned or len(cleaned) > 240:
        return ""
    parts = [part.strip().lstrip("(").strip() for part in cleaned.split(",") if part.strip(" ()")]
    ranked = [(_organization_score(part), index, part) for index, part in enumerate(parts)]
    ranked = [item for item in ranked if item[0] >= 0]
    if not ranked:
        return ""
    _, _, institution = max(ranked, key=lambda item: (item[0], item[1]))
    institution = _normalize_institution_name(institution)
    if not institution:
        return ""
    institution = re.sub(
        rf"^(.+?\bUniversity)\s+(?:[A-Z][\w.'-]*\s+){{0,3}}(?:{_COUNTRIES})$",
        r"\1",
        institution,
        flags=re.IGNORECASE,
    )
    return institution


def _display_institutions(value: str, limit: int = 3) -> str:
    institutions: list[str] = []
    seen: set[str] = set()
    for chunk in _join_broken_institution_chunks(value):
        institution = _top_level_institution(chunk)
        key = institution.casefold()
        if not institution or key in seen:
            continue
        institutions.append(institution)
        seen.add(key)
    if not institutions:
        return "暂无"
    top_level = [institution for institution in institutions if not _is_secondary_unit(institution)]
    if top_level:
        institutions = top_level
    shown = institutions[:limit]
    return ", ".join(shown) + (", et al." if len(institutions) > limit else "")


def _source_label(venue: str, source: str, paper_id: str) -> str:
    venue = re.sub(r"\s+", " ", venue or "").strip()
    source = re.sub(r"\s+", " ", source or "").strip()
    if NON_MAIN.search(venue):
        return venue if len(venue) <= 26 else f"{venue[:25].rstrip()}…"
    entry = allowed_venue(venue)
    if entry:
        return entry["abbr"]
    if _ARXIV_ID_RE.fullmatch(paper_id or "") and venue.casefold() in {"", "arxiv", "arxiv preprint"}:
        return "arXiv"
    for prefix, abbreviation in _DOI_VENUE_PREFIXES:
        if paper_id.casefold().startswith(prefix):
            return abbreviation
    for pattern, abbreviation in _VENUE_ABBREVIATIONS:
        if pattern.search(venue):
            return abbreviation
    acronym = re.search(r"\(([A-Z][A-Z0-9&-]{1,11})\)", venue)
    if acronym:
        return acronym.group(1)
    if venue and venue.casefold() not in {"暂无", "unknown", "n/a"}:
        return venue if len(venue) <= 26 else f"{venue[:25].rstrip()}…"
    source_aliases = {
        "ieee xplore": "IEEE",
        "elsevier scopus": "Elsevier",
        "springer nature": "Springer",
    }
    if source.casefold() in source_aliases:
        return source_aliases[source.casefold()]
    if paper_id.startswith("doi:"):
        return "DOI"
    return source or "来源"


def _ccf_grade(source_label: str) -> str:
    return _CCF_GRADES.get(re.sub(r"\s+", " ", source_label or "").strip().upper(), "")


def _load_paper_metadata_by_issue() -> dict[int, dict[str, str]]:
    if not ISSUE_INDEX_PATH.exists():
        return {}
    payload = json.loads(ISSUE_INDEX_PATH.read_text(encoding="utf-8"))
    result: dict[int, dict[str, str]] = {}
    for paper_id, metadata in payload.items():
        if isinstance(metadata, dict) and isinstance(metadata.get("number"), int):
            source = str(metadata.get("source") or "")
            venue = str(metadata.get("venue") or "")
            url = str(metadata.get("url") or "")
            code_url = str(metadata.get("code_url") or "")
            arxiv_id = paper_id if _ARXIV_ID_RE.fullmatch(paper_id) else ""
            if not url and arxiv_id:
                url = f"https://arxiv.org/abs/{arxiv_id}"
            elif not url and paper_id.startswith("doi:"):
                url = f"https://doi.org/{paper_id[4:]}"
            source_label = _source_label(venue, source, paper_id)
            result[metadata["number"]] = {
                "paper_id": paper_id,
                "arxiv_id": arxiv_id,
                "source_label": source_label,
                "source_url": url,
                "ccf_grade": _ccf_grade(source_label),
                "code_url": code_url,
                "abstract": metadata.get("abstract", ""),
            }
    return result


def _classify_paper(title: str, summary: str) -> str:
    """Compatibility field only; category filtering uses the complete categories list."""
    categories = classify_research(title, summary)["categories"]
    return categories[0] if categories else "待归类"


def parse_report(path: Path, metadata_by_issue: dict[int, dict[str, str]] | None = None) -> dict:
    metadata_by_issue = metadata_by_issue or {}
    markdown = path.read_text(encoding="utf-8")
    date = path.stem
    papers: list[dict[str, str | int]] = []

    table_started = False
    for line in markdown.splitlines():
        if line.startswith("| 标题 |"):
            table_started = True
            continue
        if not table_started:
            continue
        if line.startswith("|---"):
            continue
        if not line.startswith("|"):
            if papers:
                break
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        issue_match = re.search(r"\[#(\d+)\]\((https://github\.com/[^)]+)\)", cells[4])
        if not issue_match:
            continue
        issue_number = int(issue_match.group(1))
        issue_url = issue_match.group(2)
        if not issue_url.startswith(ISSUE_URL_PREFIX):
            continue
        title = re.sub(r"^\[\d{8}\]\s*", "", cells[0]).strip()
        source_metadata = metadata_by_issue.get(issue_number, {})
        arxiv_id = source_metadata.get("arxiv_id", "")
        classification = classify_research(title, cells[3], source_metadata.get("abstract", ""))
        papers.append(
            {
                "date": date,
                "title": title,
                "authors": cells[1],
                "display_authors": _display_authors(cells[1]),
                "institution": cells[2],
                "display_institution": _display_institutions(cells[2]),
                "summary": cells[3],
                "issue_number": issue_number,
                "issue_url": issue_url,
                "arxiv_id": arxiv_id,
                "arxiv_url": f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else "",
                "source_label": source_metadata.get("source_label", "arXiv" if arxiv_id else "DOI"),
                "source_url": source_metadata.get("source_url", ""),
                "ccf_grade": source_metadata.get("ccf_grade", ""),
                "code_url": source_metadata.get("code_url", ""),
                "category": classification["categories"][0] if classification["categories"] else "待归类",
                **classification,
            }
        )

    return {
        "date": date,
        "overview": _extract_overview(markdown),
        "highlights": _extract_highlights(markdown),
        "paper_count": len(papers),
        "github_url": f"{REPO_URL}/blob/main/daily_reports/{date[:6]}/{date}.md",
        "papers": papers,
    }


def collect_site_data() -> tuple[list[dict], list[dict]]:
    metadata_by_issue = _load_paper_metadata_by_issue()
    report_paths = [
        path
        for path in REPORTS_DIR.rglob("*.md")
        if re.fullmatch(r"\d{8}", path.stem)
        and re.fullmatch(r"\d{6}", path.parent.name)
    ]
    reports = [
        parse_report(path, metadata_by_issue)
        for path in sorted(report_paths, reverse=True)
    ]
    reports = [report for report in reports if report["papers"]]
    papers = [paper for report in reports for paper in report["papers"]]
    papers.sort(key=lambda item: (item["date"], item["issue_number"]), reverse=True)
    return reports, papers


def build_site(output_dir: Path) -> tuple[int, int]:
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SITE_SOURCE_DIR, output_dir, dirs_exist_ok=True)
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    reports, papers = collect_site_data()
    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    (data_dir / "papers.json").write_text(
        json.dumps({"generated_at": generated_at, "directions": public_directions(), "papers": papers}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (data_dir / "reports.json").write_text(
        json.dumps({"generated_at": generated_at, "reports": reports}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return len(reports), len(papers)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the PaperClaw GitHub Pages site")
    parser.add_argument("--output", default="_site", help="Output directory")
    args = parser.parse_args()
    report_count, paper_count = build_site((ROOT / args.output).resolve())
    print(f"Built PaperClaw Pages: reports={report_count}, papers={paper_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
