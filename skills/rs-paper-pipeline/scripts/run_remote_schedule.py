#!/usr/bin/env python3
"""Run the scheduled pipeline remotely without duplicate discovery requests."""

from __future__ import annotations

import run_rs_daily_workday


def main() -> int:
    target_dates = run_rs_daily_workday.resolve_target_dates()
    processed = 0

    for date_str in target_dates:
        already_done, reason = run_rs_daily_workday._date_already_completed(date_str)
        if already_done:
            print(f"REMOTE_SKIP date={date_str} reason=already_completed detail={reason}")
            continue

        # Discovery happens exactly once inside the workday pipeline.  The
        # filter writes counts to its stats JSON, and the pipeline stops before
        # digest/sync/notify when no candidate (or no LLM-selected paper) exists.
        # This is especially important for Semantic Scholar's cumulative 1 RPS
        # quota: a separate preflight would immediately repeat every request.
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
