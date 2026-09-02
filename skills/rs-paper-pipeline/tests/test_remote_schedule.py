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
    def test_schedule_targets_previous_weekday(self):
        beijing = timezone(timedelta(hours=8))
        expected_by_day = {
            1: "20260831",
            2: "20260901",
            3: "20260902",
            4: "20260903",
            5: "20260904",
            6: "20260904",
            7: "20260904",
        }
        for day, expected in expected_by_day.items():
            now = datetime(2026, 9, day, 3, 0, tzinfo=beijing)
            with self.subTest(day=day):
                self.assertEqual(
                    run_remote_schedule.run_rs_daily_workday.resolve_target_dates(now),
                    [expected],
                )

    def test_only_runs_dates_with_candidates(self):
        candidate_sets = {
            "20260901": [],
            "20260902": [{"id": "2609.00001"}],
        }

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
                run_remote_schedule,
                "fetch_recent_candidates",
                side_effect=lambda **kwargs: candidate_sets[kwargs["target_date"]],
            ),
            patch.object(
                run_remote_schedule.run_rs_daily_workday,
                "main",
            ) as pipeline_main,
        ):
            self.assertEqual(run_remote_schedule.main(), 0)

        pipeline_main.assert_called_once_with(
            target_date="20260902",
            notify=False,
            force=False,
        )

    def test_completed_date_skips_arxiv_preflight(self):
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
            patch.object(run_remote_schedule, "fetch_recent_candidates") as fetch,
            patch.object(run_remote_schedule.run_rs_daily_workday, "main") as pipeline_main,
        ):
            self.assertEqual(run_remote_schedule.main(), 0)

        fetch.assert_not_called()
        pipeline_main.assert_not_called()


if __name__ == "__main__":
    unittest.main()
