#!/usr/bin/env python3
"""Validate PaperClaw academic-source API keys without exposing secrets.

The script performs one minimal metadata request per configured source.  It only
prints a normalized status, HTTP code, and a safe diagnostic category; response
bodies and request URLs (which may contain credentials) are never logged.
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable


USER_AGENT = "PaperClaw/1.0 (+https://github.com/zitalk/PaperClaw)"
TIMEOUT_SECONDS = 30
MAX_ATTEMPTS = 2


@dataclass(frozen=True)
class Check:
    name: str
    secret_names: tuple[str, ...]
    url: str
    headers: dict[str, str]
    validator: Callable[[Any], bool]


@dataclass(frozen=True)
class Result:
    name: str
    status: str
    http_status: int | None
    detail: str


def _env(name: str) -> str:
    return os.environ.get(name, "").strip()


def _url(base: str, **params: str | int) -> str:
    return f"{base}?{urllib.parse.urlencode(params)}"


def _is_mapping_with(payload: Any, key: str) -> bool:
    return isinstance(payload, dict) and key in payload


def build_checks() -> list[Check]:
    openalex_key = _env("OPENALEX_API_KEY")
    semantic_key = _env("SEMANTIC_SCHOLAR_API_KEY")
    ieee_key = _env("IEEE_API_KEY")
    elsevier_key = _env("ELSEVIER_API_KEY")
    elsevier_insttoken = _env("ELSEVIER_INSTTOKEN")
    springer_key = _env("SPRINGER_NATURE_API_KEY")

    elsevier_headers = {
        "Accept": "application/json",
        "X-ELS-APIKey": elsevier_key,
    }
    if elsevier_insttoken:
        elsevier_headers["X-ELS-Insttoken"] = elsevier_insttoken

    return [
        Check(
            name="OpenAlex",
            secret_names=("OPENALEX_API_KEY",),
            url=_url(
                "https://api.openalex.org/works",
                search="multimodal vision",
                per_page=1,
                api_key=openalex_key,
            ),
            headers={},
            validator=lambda value: _is_mapping_with(value, "results"),
        ),
        Check(
            name="Semantic Scholar",
            secret_names=("SEMANTIC_SCHOLAR_API_KEY",),
            url=_url(
                "https://api.semanticscholar.org/graph/v1/paper/search",
                query="multimodal vision",
                limit=1,
                fields="paperId,title",
            ),
            headers={"x-api-key": semantic_key},
            validator=lambda value: _is_mapping_with(value, "data"),
        ),
        Check(
            name="IEEE Xplore",
            secret_names=("IEEE_API_KEY",),
            url=_url(
                "https://ieeexploreapi.ieee.org/api/v1/search/articles",
                apikey=ieee_key,
                querytext="multimodal vision",
                max_records=1,
                start_record=1,
                format="json",
            ),
            headers={},
            validator=lambda value: isinstance(value, dict)
            and ("articles" in value or "total_records" in value),
        ),
        Check(
            name="Elsevier Scopus",
            secret_names=("ELSEVIER_API_KEY",),
            url=_url(
                "https://api.elsevier.com/content/search/scopus",
                query="ALL(multimodal)",
                count=1,
            ),
            headers=elsevier_headers,
            validator=lambda value: _is_mapping_with(value, "search-results"),
        ),
        Check(
            name="Elsevier ScienceDirect",
            secret_names=("ELSEVIER_API_KEY",),
            url=_url(
                "https://api.elsevier.com/content/search/sciencedirect",
                query='"multimodal vision"',
                count=1,
            ),
            headers=elsevier_headers,
            validator=lambda value: _is_mapping_with(value, "search-results"),
        ),
        Check(
            name="Springer Nature",
            secret_names=("SPRINGER_NATURE_API_KEY",),
            url=_url(
                "https://api.springernature.com/meta/v2/json",
                api_key=springer_key,
                q="keyword: multimodal vision",
                s=1,
                p=1,
            ),
            headers={},
            validator=lambda value: isinstance(value, dict)
            and "result" in value
            and "records" in value,
        ),
    ]


def _safe_http_detail(status: int) -> str:
    if status in (401, 403):
        return "authentication_or_entitlement_rejected"
    if status == 429:
        return "rate_limited"
    if status == 400:
        return "request_rejected"
    if 500 <= status <= 599:
        return "provider_server_error"
    return "unexpected_http_response"


def run_check(check: Check) -> Result:
    missing = [name for name in check.secret_names if not _env(name)]
    if missing:
        return Result(check.name, "FAIL", None, f"missing_secret:{','.join(missing)}")

    request_headers = {"User-Agent": USER_AGENT, **check.headers}
    for attempt in range(1, MAX_ATTEMPTS + 1):
        request = urllib.request.Request(check.url, headers=request_headers)
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
                status = int(response.status)
                payload = json.loads(response.read().decode("utf-8"))
            if check.validator(payload):
                return Result(check.name, "PASS", status, "authenticated_metadata_query")
            return Result(check.name, "FAIL", status, "unexpected_response_schema")
        except urllib.error.HTTPError as exc:
            status = int(exc.code)
            retryable = status == 429 or 500 <= status <= 599
            if retryable and attempt < MAX_ATTEMPTS:
                time.sleep(2 * attempt)
                continue
            return Result(check.name, "FAIL", status, _safe_http_detail(status))
        except (urllib.error.URLError, TimeoutError):
            if attempt < MAX_ATTEMPTS:
                time.sleep(2 * attempt)
                continue
            return Result(check.name, "FAIL", None, "network_or_timeout")
        except (json.JSONDecodeError, UnicodeDecodeError):
            return Result(check.name, "FAIL", None, "non_json_response")
        except Exception:
            # Deliberately avoid logging exception text: urllib exceptions may
            # contain a credential-bearing request URL.
            return Result(check.name, "FAIL", None, "unexpected_client_error")

    return Result(check.name, "FAIL", None, "retry_exhausted")


def write_github_summary(results: list[Result]) -> None:
    summary_path = _env("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    lines = [
        "## Academic source API health check",
        "",
        "| Source | Result | HTTP | Detail |",
        "|---|---:|---:|---|",
    ]
    for result in results:
        icon = "✅ PASS" if result.status == "PASS" else "❌ FAIL"
        http_status = str(result.http_status) if result.http_status is not None else "—"
        lines.append(f"| {result.name} | {icon} | {http_status} | `{result.detail}` |")
    lines.extend(
        [
            "",
            "> This check never prints API keys, request URLs, or response bodies.",
        ]
    )
    Path(summary_path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    results = [run_check(check) for check in build_checks()]
    print("Academic source API health check")
    for result in results:
        http_status = result.http_status if result.http_status is not None else "-"
        print(f"{result.status:4} | {result.name:24} | HTTP {http_status} | {result.detail}")
    write_github_summary(results)
    return 1 if any(result.status != "PASS" for result in results) else 0


if __name__ == "__main__":
    sys.exit(main())
