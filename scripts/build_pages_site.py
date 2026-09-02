#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "daily_reports"
ISSUE_INDEX_PATH = ROOT / "papers" / "issue_index.json"
SITE_SOURCE_DIR = ROOT / "site"
REPO_URL = "https://github.com/zitalk/PaperClaw"
ISSUE_URL_PREFIX = f"{REPO_URL}/issues/"


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


def _load_arxiv_by_issue() -> dict[int, str]:
    if not ISSUE_INDEX_PATH.exists():
        return {}
    payload = json.loads(ISSUE_INDEX_PATH.read_text(encoding="utf-8"))
    result: dict[int, str] = {}
    for arxiv_id, metadata in payload.items():
        if isinstance(metadata, dict) and isinstance(metadata.get("number"), int):
            result[metadata["number"]] = arxiv_id
    return result


def _classify_paper(title: str, summary: str) -> str:
    text = f"{title} {summary}".lower()
    if re.search(r"salien(?:cy|t)", text):
        return "显著目标"
    if re.search(r"\b(?:uav|drone|aerial|low-altitude)\b", text):
        return "无人机视觉"
    if re.search(r"\b(?:tracking|multi-view|multiview|multi-camera|re-identification)\b", text):
        return "跟踪与多视角"
    if re.search(r"\b(?:multimodal|multi-modal|fusion|rgb-|infrared|thermal|hyperspectral|cross-modal)\b", text):
        return "多模态融合"
    return "综合视觉"


def parse_report(path: Path, arxiv_by_issue: dict[int, str] | None = None) -> dict:
    arxiv_by_issue = arxiv_by_issue or {}
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
        arxiv_id = arxiv_by_issue.get(issue_number, "")
        papers.append(
            {
                "date": date,
                "title": title,
                "authors": cells[1],
                "institution": cells[2],
                "summary": cells[3],
                "issue_number": issue_number,
                "issue_url": issue_url,
                "arxiv_id": arxiv_id,
                "arxiv_url": f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else "",
                "category": _classify_paper(title, cells[3]),
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
    arxiv_by_issue = _load_arxiv_by_issue()
    report_paths = [
        path
        for path in REPORTS_DIR.rglob("*.md")
        if re.fullmatch(r"\d{8}", path.stem)
        and re.fullmatch(r"\d{6}", path.parent.name)
    ]
    reports = [
        parse_report(path, arxiv_by_issue)
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
        json.dumps({"generated_at": generated_at, "papers": papers}, ensure_ascii=False, indent=2),
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
