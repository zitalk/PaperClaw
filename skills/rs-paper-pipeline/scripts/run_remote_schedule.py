#!/usr/bin/env python3
"""Run the scheduled pipeline remotely without duplicate discovery requests."""

from __future__ import annotations

import json
import os
from pathlib import Path

import run_rs_daily_workday


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


def main() -> int:
    target_dates = run_rs_daily_workday.resolve_target_dates()
    weekend_backfill = run_rs_daily_workday.is_weekend_schedule()
    processed = 0

    for date_str in target_dates:
        # Discovery happens exactly once inside the workday pipeline.  The
        # filter writes counts to its stats JSON, including zero-result runs.
        # The same date's digest is updated on retries, never duplicated.
        # This is especially important for Semantic Scholar's cumulative 1 RPS
        # quota: a separate preflight would immediately repeat every request.
        run_rs_daily_workday.main(
            target_date=date_str,
            notify=False,
            force=False,
            incremental=True,
        )
        processed += 1

    if weekend_backfill:
        notice = _weekend_backfill_notice(target_dates)
        print(
            "WEEKEND_BACKFILL_DONE "
            f"found={notice['found']} recovered={notice['recovered']} failed={notice['failed']}"
        )

    mode = "weekend_backfill" if weekend_backfill else "workday_daily"
    print(f"REMOTE_SCHEDULE_DONE mode={mode} dates={len(target_dates)} processed={processed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
