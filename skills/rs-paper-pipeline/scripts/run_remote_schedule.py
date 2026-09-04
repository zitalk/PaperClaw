#!/usr/bin/env python3
"""Run the scheduled pipeline remotely without duplicate discovery requests."""

from __future__ import annotations

import run_rs_daily_workday


def main() -> int:
    target_dates = run_rs_daily_workday.resolve_target_dates()
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

    print(f"REMOTE_SCHEDULE_DONE dates={len(target_dates)} processed={processed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
