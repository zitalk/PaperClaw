from pathlib import Path
import sys
import unittest
from unittest.mock import patch
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from services.venue_policy import filter_venues, load_policy, venue_decision
from services.digest_builder import build_digest_with_llm
from clients.multisource_client import _merge_items
import paper_processor
import daily_arxiv_cross_filter


class VenuePolicyTest(unittest.TestCase):
    def test_entire_explicit_allowlist(self):
        for entry in load_policy()["allow"]:
            for name in [entry["name"], entry["abbr"], *entry.get("aliases", [])]:
                with self.subTest(name=name):
                    self.assertTrue(venue_decision({"venue": name})[0])

    def test_no_blacklist_and_arxiv_always_bypasses_venue_gate(self):
        self.assertNotIn("deny", load_policy())
        for name in ["Scientific Reports", "Engineering Research Express", "IEEE Access", "Sensors", "Applied Sciences", "Unknown Venue"]:
            with self.subTest(name=name):
                self.assertEqual(venue_decision({"venue": name, "arxiv_id": "2609.01234"}), (True, "arxiv_exempt"))
                self.assertEqual(venue_decision({"venue": name}), (False, "venue_not_allowlisted"))

    def test_unlisted_doi_does_not_override_arxiv(self):
        for doi in ["10.1038/s41598-026-69495-2", "10.1088/2631-8695/aea1db",
                    "10.1109/ACCESS.2026.123456", "10.3390/s26010123", "10.3390/app16010123"]:
            for field, value in [("doi", doi), ("paper_id", "doi:" + doi), ("url", "https://doi.org/" + doi)]:
                with self.subTest(field=field, doi=doi):
                    self.assertFalse(venue_decision({field: value})[0])
                    self.assertTrue(venue_decision({field: value, "arxiv_id": "2609.01234"})[0])

    def test_does_not_confuse_similar_journal_names(self):
        for venue in ["Internet of Things", "IEEE Transactions on Human-Machine Systems", "Expert Systems", "Pattern Recognition Letters", "IEEE Transactions on Unknown"]:
            self.assertFalse(venue_decision({"venue": venue})[0])

    def test_content_and_database_names_cannot_admit_a_paper(self):
        self.assertFalse(venue_decision({"title": "CVPR arXiv sensors", "sources": ["arXiv"]})[0])
        self.assertEqual(venue_decision({"paper_id": "doi:10.1/test"})[1], "venue_unknown")

    def test_arxiv_remains_exempt_without_formal_venue(self):
        for candidate in [{"arxiv_id": "2609.12345v1"}, {"paper_id": "cs/9901001"},
                          {"url": "https://arxiv.org/abs/2609.12345"}]:
            self.assertEqual(venue_decision(candidate), (True, "arxiv_exempt"))

    def test_conference_metadata_and_workshops(self):
        self.assertTrue(venue_decision({"venue": "2026 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)"})[0])
        self.assertTrue(venue_decision({"venue": "Proceedings of the 40th AAAI Conference on Artificial Intelligence"})[0])
        for venue in ["CVPR Workshops", "ICCV Companion", "CVPR Demo", "ECCV Extended Abstracts"]:
            self.assertFalse(venue_decision({"venue": venue})[0])

    def test_doi_aliases_for_new_journals(self):
        for journal in ["knosys", "eswa", "patcog", "inffus"]:
            self.assertTrue(venue_decision({"doi": f"10.1016/j.{journal}.2026.12345"})[0])

    def test_merge_keeps_arxiv_exemption_despite_unlisted_venues(self):
        items = _merge_items([
            {"title": "same", "venue": "IEEE Access", "arxiv_id": "2609.01234", "sources": ["arXiv"]},
            {"title": "same", "venue": "A much longer unknown venue", "sources": ["Crossref"]},
        ])
        self.assertEqual(venue_decision(items[0]), (True, "arxiv_exempt"))

    def test_filter_preserves_reason_and_inputs(self):
        candidates = [{"paper_id": "2609.12345"}, {"venue": "IEEE Access"}, {"venue": "KBS"}]
        admitted, excluded = filter_venues(candidates)
        self.assertEqual(len(admitted), 2)
        self.assertEqual(excluded[0]["venue_policy_reason"], "venue_not_allowlisted")
        self.assertNotIn("venue_policy_reason", candidates[1])

    def test_direct_processing_stops_before_llm(self):
        with patch.object(paper_processor, "_process_metadata_candidate") as process:
            result, error = paper_processor.process_candidate({"venue": "Sensors"})
        self.assertIsNone(result)
        self.assertIn("venue_not_allowlisted", error)
        process.assert_not_called()

    def test_zero_candidates_report_shows_venue_gate_counts(self):
        body = build_digest_with_llm("20260904", [], stats={
            "candidate_count": 5, "venue_admitted_count": 0,
            "venue_excluded_count": 5, "llm_selected_count": 0,
        })
        self.assertIn("刊会准入通过 0 篇（排除 5 篇）", body)

    def test_scheduled_entry_filters_before_llm(self):
        items = [{"paper_id": "doi:10.1/excluded", "venue": "Scientific Reports"},
                 {"paper_id": "doi:10.1/admitted", "venue": "KBS"}]
        with (
            patch.object(daily_arxiv_cross_filter, "CONFIG", SimpleNamespace(github_token="test", llm_api_key="test")),
            patch.object(daily_arxiv_cross_filter, "get_repo"),
            patch.object(daily_arxiv_cross_filter, "ensure_index", return_value={}),
            patch.object(daily_arxiv_cross_filter, "fetch_recent_candidates", return_value=items),
            patch.object(daily_arxiv_cross_filter, "llm_cross_filter", return_value=[]) as llm,
            patch.object(daily_arxiv_cross_filter, "compact_item", side_effect=lambda x: x),
        ):
            daily_arxiv_cross_filter.main(dry_run=True, target_date="20260904")
        llm.assert_called_once_with([items[1]])

    def test_empty_admission_does_not_call_llm_api(self):
        with patch.object(daily_arxiv_cross_filter, "call_llm") as api:
            self.assertEqual(daily_arxiv_cross_filter.llm_cross_filter([]), [])
        api.assert_not_called()


if __name__ == "__main__":
    unittest.main()
