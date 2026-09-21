#!/usr/bin/env python3
"""Run the scheduled pipeline remotely without duplicate discovery requests."""

from __future__ import annotations

import json
import os
import time
import urllib.error
from pathlib import Path

import run_rs_daily_workday
from clients import arxiv_client
from clients.multisource_client import ARXIV_SCHEDULE_CACHE_ENV


SCHEDULE_MODES = ("workday_daily", "weekend_backfill")


def _safe_source_error(exc: Exception) -> str:
    if isinstance(exc, urllib.error.HTTPError):
        return f"HTTP {exc.code}"
    return type(exc).__name__


def _prepare_weekend_arxiv_cache(
    target_dates: list[str],
    memory_dir: Path | None = None,
) -> Path:
    """Query arXiv once for the weekly window and share it with every date run."""
    memory_dir = memory_dir or Path("memory")
    memory_dir.mkdir(parents=True, exist_ok=True)
    cache_path = memory_dir / "arxiv_weekend_schedule_cache.json"
    try:
        items = arxiv_client.fetch_recent_candidates(
            max_results=1200,
            days_back=max(len(target_dates) + 1, 8),
            target_date=None,
        )
        payload = {"status": "ok", "items": items}
        print(f"ARXIV_WEEKEND_CACHE_READY candidates={len(items)} dates={len(target_dates)}")
    except Exception as exc:
        reason = _safe_source_error(exc)
        payload = {"status": "unavailable", "items": [], "reason": reason,
                   "retry_after": time.time() + 600}
        print(f"::warning title=arXiv 周末批量检索不可用::{reason}")
    cache_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    os.environ[ARXIV_SCHEDULE_CACHE_ENV] = str(cache_path.resolve())
    return cache_path


def _weekend_backfill_notice(
    target_dates: list[str],
    memory_dir: Path | None = None,
) -> dict[str, int]:
    memory_dir = memory_dir or Path("memory")
    found = 0
    recovered = 0
    failed = 0
    affected_dates: list[str] = []

    for date_str in target_dates:
        stats_path = memory_dir / f"rs_daily_stats_{date_str}.json"
        if not stats_path.exists():
            continue
        stats = json.loads(stats_path.read_text(encoding="utf-8"))
        date_found = int(stats.get("todo_count") or 0)
        date_failed = len(stats.get("failed_items") or [])
        if date_found:
            affected_dates.append(date_str)
        found += date_found
        failed += date_failed
        recovered += max(0, date_found - date_failed)

    result = {"found": found, "recovered": recovered, "failed": failed}
    if found:
        dates = ", ".join(affected_dates)
        message = f"发现 {found} 篇历史遗漏，成功补录 {recovered} 篇，失败 {failed} 篇；涉及日期：{dates}"
        print(f"::warning title=PaperClaw 周末补漏::{message}")
    else:
        message = "最近 7 天未发现历史遗漏。"
        print("WEEKEND_BACKFILL_CLEAR found=0")

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write("## PaperClaw 周末补漏\n\n")
            summary.write(message + "\n")
    return result


def main(mode: str | None = None) -> int:
    mode = mode or os.environ.get("RS_SCHEDULE_MODE") or "workday_daily"
    if mode not in SCHEDULE_MODES:
        raise ValueError(f"unsupported schedule mode: {mode}")
    weekend_backfill = mode == "weekend_backfill"
    target_dates = run_rs_daily_workday.resolve_target_dates(
        weekend_backfill=weekend_backfill,
    )
    processed = 0

    if weekend_backfill:
        _prepare_weekend_arxiv_cache(target_dates)

    try:
        for date_str in target_dates:
            # Discovery happens exactly once inside each date pipeline. arXiv
            # additionally reuses the schedule-level cache on Sunday, while
            # per-date providers retain their own exact-date API constraints.
            run_rs_daily_workday.main(
                target_date=date_str,
                notify=False,
                force=False,
                incremental=True,
            )
            processed += 1
    finally:
        os.environ.pop(ARXIV_SCHEDULE_CACHE_ENV, None)

    if weekend_backfill:
        notice = _weekend_backfill_notice(target_dates)
        print(
            "WEEKEND_BACKFILL_DONE "
            f"found={notice['found']} recovered={notice['recovered']} failed={notice['failed']}"
        )

    print(f"REMOTE_SCHEDULE_DONE mode={mode} dates={len(target_dates)} processed={processed}")
    return 0


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=SCHEDULE_MODES, default=None)
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.mode))
