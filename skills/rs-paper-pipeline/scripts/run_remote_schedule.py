#!/usr/bin/env python3
"""Run the scheduled pipeline remotely without creating empty daily reports."""

from __future__ import annotations

from clients.arxiv_client import fetch_recent_candidates
import run_rs_daily_workday


def main() -> int:
    target_dates = run_rs_daily_workday.resolve_target_dates()
    processed = 0

    for date_str in target_dates:
        already_done, reason = run_rs_daily_workday._date_already_completed(date_str)
        if already_done:
            print(f"REMOTE_SKIP date={date_str} reason=already_completed detail={reason}")
            continue

        candidates = fetch_recent_candidates(
            max_results=1200,
            days_back=2,
            target_date=date_str,
        )
        print(f"REMOTE_PREFLIGHT date={date_str} candidates={len(candidates)}")
        if not candidates:
            print(f"REMOTE_SKIP date={date_str} reason=no_arxiv_candidates")
            continue

        run_rs_daily_workday.main(
            target_date=date_str,
            notify=False,
            force=False,
        )
        processed += 1

    print(f"REMOTE_SCHEDULE_DONE dates={len(target_dates)} processed={processed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
