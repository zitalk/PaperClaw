#!/usr/bin/env python3
"""Persistent issue index for fast paper_id → issue_number lookup.

Index file lives at ``papers/issue_index.json`` in the repo (committed).
Avoids full ``repo.get_issues()`` scans on every pipeline run.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone

from clients.github_ops import upsert_repo_file

INDEX_PATH = "papers/issue_index.json"
_CODE_REPOSITORY_RE = re.compile(
    r"https?://(?:www\.)?(?:github\.com|gitlab\.com|codeberg\.org)/"
    r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+",
    re.IGNORECASE,
)


def _extract_arxiv_id(body: str) -> str | None:
    generic = re.search(r"\| \*\*PaperClaw ID\*\* \|\s*`([^`]+)`\s*\|", body or "")
    if generic:
        return generic.group(1).strip()
    match = re.search(r"arxiv\.org/abs/([^\)\s]+)", body or "")
    return match.group(1).strip() if match else None


def _extract_table_value(body: str, label: str) -> str:
    match = re.search(rf"\| \*\*{re.escape(label)}\*\* \|\s*(.*?)\s*\|", body or "")
    return match.group(1).strip() if match else ""


def _extract_code_url(body: str) -> str:
    code_row = _extract_table_value(body, "代码")
    match = _CODE_REPOSITORY_RE.search(code_row or body or "")
    return match.group(0).rstrip(".,;:)]}") if match else ""


def _source_metadata(body: str, paper_id: str) -> dict[str, str]:
    source = _extract_table_value(body, "来源")
    venue = _extract_table_value(body, "出版物")
    link_text = _extract_table_value(body, "链接") or _extract_table_value(body, "arXiv")
    link_match = re.search(r"\[[^\]]+\]\((https?://[^)]+)\)", link_text)
    url = link_match.group(1) if link_match else ""
    code_url = _extract_code_url(body)

    if re.fullmatch(r"\d{4}\.\d{4,5}(?:v\d+)?", paper_id or ""):
        source = source or "arXiv"
        venue = venue or "arXiv"
        url = url or f"https://arxiv.org/abs/{paper_id}"

    metadata = {"source": source, "venue": venue, "url": url, "code_url": code_url,
                "abstract": _extract_table_value(body, "摘要")}
    return {key: value for key, value in metadata.items() if value and value not in {"暂无", "未提供"}}


def _index_entry(paper_id: str, issue) -> dict:
    body = issue.body or ""
    return {
        "number": issue.number,
        "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        **_source_metadata(body, paper_id),
    }


def load_index(repo) -> dict[str, dict]:
    """Load the index from the repo file. Returns {} if not found."""
    try:
        content = repo.get_contents(INDEX_PATH)
        data = json.loads(content.decoded_content.decode("utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def save_index(repo, index: dict[str, dict]) -> None:
    """Persist the index to the repo."""
    body = json.dumps(index, ensure_ascii=False, indent=2) + "\n"
    upsert_repo_file(repo, INDEX_PATH, body, "update issue index")


def rebuild_index(repo) -> dict[str, dict]:
    """Full scan: build index from all issues in the repo."""
    index: dict[str, dict] = {}
    for issue in repo.get_issues(state="all"):
        body = issue.body or ""
        paper_id = _extract_arxiv_id(body)
        if not paper_id:
            continue
        index[paper_id] = _index_entry(paper_id, issue)
    return index


def ensure_index(repo) -> dict[str, dict]:
    """Load index; auto-rebuild if empty."""
    index = load_index(repo)
    if not index:
        print("[issue_index] index empty, rebuilding...")
        index = rebuild_index(repo)
        save_index(repo, index)
        print(f"[issue_index] rebuilt with {len(index)} entries")
    return index


def lookup_issue(repo, index: dict[str, dict], arxiv_id: str):
    """Fetch a single issue by number from the index. Returns None if not found."""
    entry = index.get(arxiv_id)
    if not entry:
        return None
    try:
        return repo.get_issue(entry["number"])
    except Exception:
        return None


def update_index_from_issue(index: dict[str, dict], arxiv_id: str, issue) -> bool:
    """Update index entry for a source-agnostic paper ID."""
    if not arxiv_id:
        return False
    index[arxiv_id] = _index_entry(arxiv_id, issue)
    return True


def commit_index_if_dirty(repo, index: dict[str, dict]) -> bool:
    """Save index to repo if it has been modified. Returns True if saved."""
    if not index:
        return False
    save_index(repo, index)
    return True
