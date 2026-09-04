import json
import sys
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from clients import multisource_client as sources
from services.digest_builder import build_digest_with_llm
from services.report_status import REPORT_MARKER, daily_encouragement, read_run_status
import daily_digest_llm_upgrade as digest
import run_rs_daily_workday as workday
import daily_arxiv_cross_filter as filtering


class EmptyDailyReportTest(unittest.TestCase):
    def stats(self, **updates):
        return {"date": "20260904", "candidate_count": 0, "llm_selected_count": 0,
                "source_status": [{"name": "arXiv", "status": "ok"}],
                "successful_selected_arxiv_ids": [], **updates}

    def test_healthy_zero_uses_no_llm_and_has_status_time_and_encouragement(self):
        for count in (0, 12):
            with patch("services.digest_builder.call_llm") as llm:
                body = build_digest_with_llm("20260904", [], self.stats(candidate_count=count))
            llm.assert_not_called()
            self.assertEqual(read_run_status(body)["status"], "ok")
            self.assertIn("北京时间", body)
            self.assertIn(daily_encouragement("20260904"), body)
            self.assertIn(REPORT_MARKER, body)
            self.assertIn("最终纳入日报 0 篇", body)

    def test_unavailable_sources_are_not_healthy_zero_results(self):
        body = build_digest_with_llm("20260904", [], self.stats(source_status=[
            {"name": "arXiv", "status": "ok"},
            {"name": "IEEE Xplore", "status": "unavailable"},
        ]))
        self.assertEqual(read_run_status(body)["status"], "degraded")
        self.assertIn("IEEE Xplore", body)
        self.assertNotIn(daily_encouragement("20260904"), body)

    def test_processing_failure_or_missing_archival_record_is_degraded(self):
        for failures in ([], [{"title": "Example", "error": "metadata_error"}]):
            body = build_digest_with_llm("20260904", [], self.stats(llm_selected_count=1, failed_items=failures))
            self.assertEqual(read_run_status(body)["status"], "degraded")
            self.assertIn("存在异常", body)

    def test_legacy_stats_do_not_invent_source_health(self):
        body = build_digest_with_llm("20260904", [], {"candidate_count": 0})
        self.assertEqual(read_run_status(body)["status"], "unknown")
        self.assertIn("来源状态未记录", body)

    def test_empty_retry_updates_existing_issue_without_duplicate(self):
        repo = MagicMock()
        existing = SimpleNamespace(title="日报 20260904", number=99,
                                   _rawData={"title": "日报 20260904"}, edit=MagicMock())
        with tempfile.TemporaryDirectory() as temp:
            stats_path = Path(temp) / "stats.json"
            stats_path.write_text(json.dumps(self.stats()), encoding="utf-8")
            with (
                patch.object(digest, "CONFIG", SimpleNamespace(github_token="test", llm_api_key="test", temp_dir=Path(temp))),
                patch.object(digest, "get_repo", return_value=repo),
                patch.object(digest, "load_open_issues", return_value=[existing]),
                patch.object(digest, "ensure_index", return_value={}),
                patch("services.digest_builder.call_llm") as llm,
            ):
                digest.main("20260904", str(stats_path))
                digest.main("20260904", str(stats_path))
        self.assertEqual(existing.edit.call_count, 2)
        repo.create_issue.assert_not_called()
        llm.assert_not_called()

    def test_optional_source_failure_does_not_repeat_completed_paper_processing(self):
        body = '<!-- paperclaw-run: {"status":"degraded"} -->\nhttps://github.com/zitalk/PaperClaw/issues/1'
        with (
            patch.object(workday, "_get_repo"),
            patch.object(workday, "get_today_digest_issue", return_value=SimpleNamespace(body=body, number=99)),
            patch.object(workday, "daily_report_file_exists", return_value=True),
        ):
            self.assertTrue(workday._date_already_completed("20260904")[0])

    def test_source_health_distinguishes_unconfigured_from_unavailable(self):
        config = SimpleNamespace(multisource_enabled=True, openalex_api_key="",
                                 semantic_scholar_api_key="test", springer_nature_api_key="",
                                 ieee_api_key="test", elsevier_api_key="")
        with ExitStack() as stack:
            stack.enter_context(patch.object(sources, "CONFIG", config))
            for fn in ("fetch_arxiv_candidates", "fetch_crossref", "fetch_semantic_scholar"):
                stack.enter_context(patch.object(sources, fn, return_value=[]))
            stack.enter_context(patch.object(sources, "fetch_ieee", side_effect=sources.ProviderUnavailable("HTTP 403")))
            health = []
            self.assertEqual(sources.fetch_recent_candidates(target_date="20260904", source_status=health), [])
        by_name = {s["name"]: s["status"] for s in health}
        self.assertEqual(by_name["arXiv"], "ok")
        self.assertEqual(by_name["Semantic Scholar"], "ok")
        self.assertEqual(by_name["OpenAlex"], "not_configured")
        self.assertEqual(by_name["IEEE Xplore"], "unavailable")

    def test_filter_fallback_is_exposed_as_degraded(self):
        warnings = []
        candidate = {"arxiv_id": "2609.1", "title": "UAV object detection", "abstract": "Deep learning"}
        with patch.object(filtering, "call_llm", return_value="invalid"):
            filtering.llm_cross_filter([candidate], warnings=warnings)
        self.assertEqual(warnings, ["llm_parse_fallback"])
        body = build_digest_with_llm("20260904", [], self.stats(filter_warnings=warnings))
        self.assertEqual(read_run_status(body)["status"], "degraded")


if __name__ == "__main__":
    unittest.main()
