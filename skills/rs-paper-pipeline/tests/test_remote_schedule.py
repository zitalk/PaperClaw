import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import run_remote_schedule


class RemoteScheduleTest(unittest.TestCase):
    def test_schedule_targets_previous_day_and_monday_weekend_backfill(self):
        beijing = timezone(timedelta(hours=8))
        expected_by_day = {
            1: ["20260831"],
            2: ["20260901"],
            3: ["20260902"],
            4: ["20260903"],
            5: ["20260904"],
            6: ["20260904"],
            7: ["20260904", "20260905", "20260906"],
        }
        for day, expected in expected_by_day.items():
            now = datetime(2026, 9, day, 3, 0, tzinfo=beijing)
            with self.subTest(day=day):
                self.assertEqual(
                    run_remote_schedule.run_rs_daily_workday.resolve_target_dates(now),
                    expected,
                )

    def test_each_incomplete_date_runs_discovery_exactly_once_in_pipeline(self):
        with (
            patch.object(
                run_remote_schedule.run_rs_daily_workday,
                "resolve_target_dates",
                return_value=["20260901", "20260902"],
            ),
            patch.object(
                run_remote_schedule.run_rs_daily_workday,
                "_date_already_completed",
                return_value=(False, "not completed"),
            ),
            patch.object(
                run_remote_schedule.run_rs_daily_workday,
                "main",
            ) as pipeline_main,
        ):
            self.assertEqual(run_remote_schedule.main(), 0)

        self.assertEqual(pipeline_main.call_count, 2)
        pipeline_main.assert_any_call(target_date="20260901", notify=False, force=False)
        pipeline_main.assert_any_call(target_date="20260902", notify=False, force=False)

    def test_completed_date_skips_pipeline(self):
        with (
            patch.object(
                run_remote_schedule.run_rs_daily_workday,
                "resolve_target_dates",
                return_value=["20260901"],
            ),
            patch.object(
                run_remote_schedule.run_rs_daily_workday,
                "_date_already_completed",
                return_value=(True, "digest=#18 papers=17"),
            ),
            patch.object(run_remote_schedule.run_rs_daily_workday, "main") as pipeline_main,
        ):
            self.assertEqual(run_remote_schedule.main(), 0)

        pipeline_main.assert_not_called()

    def test_empty_filter_stops_before_digest(self):
        workday = run_remote_schedule.run_rs_daily_workday
        with (
            patch.object(workday, "_run_step") as run_step,
            patch.object(
                workday,
                "_load_stats",
                return_value={"candidate_count": 0, "llm_selected_count": 0},
            ),
            patch.object(workday, "_write_state") as write_state,
        ):
            workday._process_date("20260901", notify=False, force=True)

        self.assertEqual(run_step.call_count, 1)
        self.assertEqual(run_step.call_args.args[1], "filter")
        self.assertEqual(write_state.call_args.args[1:3], ("done", "skipped"))


if __name__ == "__main__":
    unittest.main()
