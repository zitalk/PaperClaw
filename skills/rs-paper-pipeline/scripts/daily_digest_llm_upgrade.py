#!/usr/bin/env python3
from __future__ import annotations

import re
import json
from collections import defaultdict
from pathlib import Path

from pipeline_config import get_repo, load_config
from services.digest_builder import build_digest_with_llm, extract_paper_date, validate_papers_for_digest, refresh_digest_status
from services.issue_index import ensure_index, lookup_issue, _extract_arxiv_id, _source_metadata
from services.venue_policy import venue_decision

CONFIG = load_config()


def issue_data(issue) -> dict:
    return getattr(issue, "_rawData", None) or {}


def load_open_issues(repo):
    issues = []
    for issue in repo.get_issues(state="open"):
        raw_data = getattr(issue, "_rawData", None) or {}
        if "pull_request" in raw_data:
            continue
        issues.append(issue)
    return issues


def collect_papers_by_date(issues):
    paper_by_date = defaultdict(list)
    digest_issue_by_date = {}

    for it in issues:
        raw = issue_data(it)
        t = raw.get("title") or it.title
        if "日报" not in t:
            paper_date = extract_paper_date(raw)
            if paper_date:
                paper_by_date[paper_date].append(raw)
        dm = re.search(r"日报\s*(\d{8})", t)
        if dm:
            digest_issue_by_date[dm.group(1)] = it

    return paper_by_date, digest_issue_by_date


def _paper_key(paper: dict) -> int | None:
    number = paper.get("number")
    return number if isinstance(number, int) else None


def _merge_paper(papers: list[dict], paper: dict) -> None:
    number = _paper_key(paper)
    if number is not None and any(_paper_key(item) == number for item in papers):
        return
    papers.append(paper)


def _load_stats_map(stats_json: str | None) -> dict[str, dict]:
    stats_map: dict[str, dict] = {}
    if not stats_json:
        return stats_map
    try:
        obj = json.loads(Path(stats_json).read_text(encoding="utf-8"))
        if isinstance(obj, dict) and obj.get("date"):
            stats_map[obj["date"]] = obj
    except Exception:
        pass
    return stats_map


def _augment_papers_from_stats(repo, papers: list[dict], stats: dict | None) -> list[dict]:
    if not stats:
        return papers

    selected_ids = stats.get("successful_selected_arxiv_ids")
    if selected_ids is None:
        return papers

    index = ensure_index(repo)
    by_issue_number = {
        _paper_key(paper): paper
        for paper in papers
        if _paper_key(paper) is not None
    }
    selected_papers: list[dict] = []

    for arxiv_id in selected_ids:
        issue = lookup_issue(repo, index, arxiv_id)
        if issue is None:
            continue

        raw = issue_data(issue)
        number = _paper_key(raw)
        if number is not None and number in by_issue_number:
            raw = by_issue_number[number]
        _merge_paper(selected_papers, raw)

    return selected_papers


def published_paper_numbers(body: str, repo_name: str) -> set[int]:
    """Only the approved paper table counts, never arbitrary links or failures."""
    section = re.search(r"^##[^\n]*今日文章列表[^\n]*\n(.*?)(?=^## |\Z)", body or "", re.M | re.S)
    if not section:
        return set()
    numbers = set()
    for line in section.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not line.startswith("|") or len(cells) < 5:
            continue
        match = re.fullmatch(r"\[#(\d+)\]\(https://github\.com/" + re.escape(repo_name) + r"/issues/(\d+)\)", cells[4])
        if match and match[1] == match[2]:
            numbers.add(int(match[1]))
    return numbers


def retain_previous_papers(repo, issues, body: str, date: str, repo_name: str) -> list[dict]:
    available = {_paper_key(issue_data(i)): issue_data(i) for i in issues}
    retained = []
    for number in sorted(published_paper_numbers(body, repo_name)):
        raw = available.get(number)
        if raw is None:
            try:
                raw = issue_data(repo.get_issue(number))
            except Exception as exc:
                if getattr(exc, "status", None) in (404, 410):
                    continue  # Deleted cards must never be resurrected.
                raise  # A transient API failure must not silently shrink the digest.
        if raw.get("state", "open") != "open" or "pull_request" in raw:
            continue
        if extract_paper_date(raw) != date:
            continue
        paper_id = _extract_arxiv_id(raw.get("body") or "") or ""
        metadata = {**_source_metadata(raw.get("body") or "", paper_id), "paper_id": paper_id}
        if venue_decision(metadata)[0]:
            _merge_paper(retained, raw)
    return retained


def main(target_date: str | None = None, stats_json: str | None = None, incremental: bool = False):
    if not CONFIG.github_token:
        raise RuntimeError("Missing required environment variable: GITHUB_TOKEN")
    if not CONFIG.llm_api_key:
        raise RuntimeError("Missing required environment variable: LLM_API_KEY")

    repo = get_repo(CONFIG)

    stats_map = _load_stats_map(stats_json)

    issues = load_open_issues(repo)
    paper_by_date, digest_issue_by_date = collect_papers_by_date(issues)

    out_dir = CONFIG.temp_dir / "RS-PaperClaw" / "daily_reports"
    out_dir.mkdir(parents=True, exist_ok=True)

    dates = sorted(set(paper_by_date.keys()) | set(stats_map.keys()))
    if target_date:
        dates = [d for d in dates if d == target_date]

    if not dates:
        print(f"NO_DIGEST_DATE target={target_date or 'ALL'}")
        return

    for date in dates:
        # Open issue list is eventually consistent right after paper creation.
        # Current successes plus previously published, still-admitted cards.
        # Date labels alone must not reintroduce old, removed or unrelated cards.
        stats = stats_map.get(date)
        papers = _augment_papers_from_stats(repo, paper_by_date.get(date, []), stats)
        previous_issue = digest_issue_by_date.get(date)
        previous_body = (getattr(previous_issue, "body", None) or issue_data(previous_issue).get("body", "")) if previous_issue else ""
        repo_name = getattr(CONFIG, "github_repo", "zitalk/PaperClaw")
        previous = retain_previous_papers(repo, issues, previous_body, date, repo_name) if incremental else []
        previous_ids = {_paper_key(p) for p in previous}
        new_count = len({_paper_key(p) for p in papers} - previous_ids)
        for paper in previous:
            _merge_paper(papers, paper)
        if incremental and stats is not None:
            stats = {**stats, "incremental": True, "new_included_count": new_count,
                     "cumulative_included_count": len(papers)}
        papers = sorted(papers, key=lambda x: x["number"])
        if not papers and date not in stats_map:
            print(f"NO_PAPERS date={date}")
            continue
        validation_errors = validate_papers_for_digest(papers)
        if validation_errors:
            raise RuntimeError(
                f"digest paper validation failed for {date}: " + " | ".join(validation_errors[:8])
            )
        md = None
        # Nothing new: retain paper summaries, update counts and health without LLM.
        if (incremental and stats and papers and not new_count
                and not stats.get("refresh_count")
                and {_paper_key(p) for p in papers} == published_paper_numbers(previous_body, repo_name)):
            md = refresh_digest_status(previous_body, stats, len(papers))
        if md is None:
            md = build_digest_with_llm(date, papers, stats=stats,
                                      failed_items=(stats or {}).get("failed_items"))
        (out_dir / f"{date}.md").write_text(md, encoding="utf-8")

        title = f"日报 {date}"
        labels = [date, "日报"]
        if date in digest_issue_by_date:
            digest_issue_by_date[date].edit(body=md, title=title, labels=labels)
            print(f"UPDATED digest issue {date} -> #{digest_issue_by_date[date].number}")
        else:
            ni = repo.create_issue(title=title, body=md, labels=labels)
            print(f"CREATED digest issue {date} -> #{ni.number}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--date", dest="date", help="仅生成指定日期日报，格式 YYYYMMDD")
    parser.add_argument("--stats-json", dest="stats_json", help="筛选统计 JSON 文件路径")
    parser.add_argument("--incremental", action="store_true", help="保留已纳入日报的论文并追加新论文")
    args = parser.parse_args()

    main(target_date=args.date, stats_json=args.stats_json, incremental=args.incremental)
