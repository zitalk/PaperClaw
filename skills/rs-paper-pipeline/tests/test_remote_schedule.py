import sys
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import run_remote_schedule


class RemoteScheduleTest(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()

