import sys
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import run_remote_schedule


class RemoteScheduleTest(unittest.TestCase):
    def test_workday_schedule_targets_previous_day_only(self):
        beijing = timezone(timedelta(hours=8))
        now = datetime(2026, 9, 9, 9, 30, tzinfo=beijing)
        self.assertEqual(
            run_remote_schedule.run_rs_daily_workday.resolve_target_dates(now),
            ["20260908"],
        )

    def test_monday_schedule_targets_sunday_only(self):
        beijing = timezone(timedelta(hours=8))
        now = datetime(2026, 9, 7, 3, 0, tzinfo=beijing)
        self.assertEqual(
            run_remote_schedule.run_rs_daily_workday.resolve_target_dates(now),
            ["20260906"],
        )

    def test_weekend_schedule_reconciles_previous_seven_days(self):
        beijing = timezone(timedelta(hours=8))
        now = datetime(2026, 9, 6, 12, 0, tzinfo=beijing)
        self.assertEqual(
            run_remote_schedule.run_rs_daily_workday.resolve_target_dates(now),
            [
                "20260830",
                "20260831",
                "20260901",
                "20260902",
                "20260903",
                "20260904",
                "20260905",
            ],
        )

    def test_weekend_backfill_notice_counts_recovered_and_failed_papers(self):
        with tempfile.TemporaryDirectory() as tmp:
            memory_dir = Path(tmp)
            (memory_dir / "rs_daily_stats_20260904.json").write_text(
                json.dumps({"todo_count": 3, "failed_items": [{"paper_id": "failed"}]}),
                encoding="utf-8",
            )
            (memory_dir / "rs_daily_stats_20260905.json").write_text(
                json.dumps({"todo_count": 2, "failed_items": []}),
                encoding="utf-8",
            )

            with patch("builtins.print") as output:
                result = run_remote_schedule._weekend_backfill_notice(
                    ["20260904", "20260905"],
                    memory_dir=memory_dir,
                )

        self.assertEqual(result, {"found": 5, "recovered": 4, "failed": 1})
        self.assertTrue(any("::warning title=PaperClaw 周末补漏::" in str(call) for call in output.call_args_list))

    def test_schedule_rejects_empty_lookback_window(self):
        with self.assertRaises(ValueError):
            run_remote_schedule.run_rs_daily_workday.resolve_target_dates(lookback_days=0)

    def test_each_incomplete_date_runs_discovery_exactly_once_in_pipeline(self):
        with (
            patch.object(
                run_remote_schedule.run_rs_daily_workday,
                "resolve_target_dates",
                return_value=["20260901", "20260902"],
            ),
            patch.object(run_remote_schedule.run_rs_daily_workday, "is_weekend_schedule", return_value=False),
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
        pipeline_main.assert_any_call(target_date="20260901", notify=False, force=False, incremental=True)
        pipeline_main.assert_any_call(target_date="20260902", notify=False, force=False, incremental=True)

    def test_completed_date_still_runs_incremental_discovery(self):
        with (
            patch.object(
                run_remote_schedule.run_rs_daily_workday,
                "resolve_target_dates",
                return_value=["20260901"],
            ),
            patch.object(run_remote_schedule.run_rs_daily_workday, "is_weekend_schedule", return_value=False),
            patch.object(
                run_remote_schedule.run_rs_daily_workday,
                "_date_already_completed",
                return_value=(True, "digest=#18 papers=17"),
            ),
            patch.object(run_remote_schedule.run_rs_daily_workday, "main") as pipeline_main,
        ):
            self.assertEqual(run_remote_schedule.main(), 0)

        pipeline_main.assert_called_once_with(target_date="20260901", notify=False, force=False, incremental=True)

    def test_incremental_mode_bypasses_completion_guard_and_reaches_both_steps(self):
        workday = run_remote_schedule.run_rs_daily_workday
        with (
            patch.object(workday, "_date_already_completed", return_value=(True, "done")) as completion,
            patch.object(workday, "_run_step") as step,
            patch.object(workday, "_load_stats", return_value={"date": "20260903"}),
            patch.object(workday, "_write_state"), patch.object(workday, "run"),
            patch.object(workday, "_get_repo"),
            patch.object(workday, "daily_report_file_exists", return_value=True),
        ):
            workday._process_date("20260903", notify=False, incremental=True)
        completion.assert_not_called()
        self.assertEqual(step.call_count, 2)
        self.assertTrue(all("--incremental" in call.args[2] for call in step.call_args_list))

    def test_empty_filter_still_publishes_and_syncs_digest(self):
        workday = run_remote_schedule.run_rs_daily_workday
        with (
            patch.object(workday, "_run_step") as run_step,
            patch.object(
                workday,
                "_load_stats",
                return_value={"date": "20260901", "candidate_count": 0, "llm_selected_count": 0},
            ),
            patch.object(workday, "_write_state") as write_state,
            patch.object(workday, "run") as run,
            patch.object(workday, "_get_repo"),
            patch.object(workday, "daily_report_file_exists", return_value=True),
        ):
            workday._process_date("20260901", notify=False, force=True)

        self.assertEqual(run_step.call_count, 2)
        self.assertEqual(run_step.call_args.args[1], "digest")
        self.assertEqual(write_state.call_args.args[1:3], ("done", "ok"))
        self.assertIn("scripts/sync_daily_reports_to_repo.py", run.call_args.args[0])

    def test_missing_stats_never_publishes_healthy_empty_report(self):
        workday = run_remote_schedule.run_rs_daily_workday
        with (
            patch.object(workday, "_run_step") as run_step,
            patch.object(workday, "_load_stats", return_value={}),
            patch.object(workday, "_write_state"),
        ):
            with self.assertRaises(RuntimeError):
                workday._process_date("20260901", notify=False, force=True)
        self.assertEqual(run_step.call_count, 1)

    def test_empty_report_remains_eligible_for_later_retries(self):
        from types import SimpleNamespace
        workday = run_remote_schedule.run_rs_daily_workday
        with (
            patch.object(workday, "_get_repo"),
            patch.object(workday, "get_today_digest_issue", return_value=SimpleNamespace(number=99, body="日报：0 篇")),
            patch.object(workday, "daily_report_file_exists", return_value=True),
        ):
            self.assertFalse(workday._date_already_completed("20260901")[0])


if __name__ == "__main__":
    unittest.main()
