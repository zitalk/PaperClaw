from pathlib import Path
from types import SimpleNamespace
import sys
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import daily_digest_llm_upgrade


class DailyDigestSelectionTest(unittest.TestCase):
    def test_stats_exclude_stale_date_labeled_issues(self):
        papers = [
            {"number": 10, "title": "Current selected paper"},
            {"number": 11, "title": "Stale paper from an earlier replay"},
        ]
        selected_issue = SimpleNamespace(
            _rawData={"number": 10, "title": "Current selected paper"}
        )
        stats = {"successful_selected_arxiv_ids": ["2609.00010v1"]}

        with (
            patch.object(daily_digest_llm_upgrade, "ensure_index", return_value={}),
            patch.object(
                daily_digest_llm_upgrade,
                "lookup_issue",
                return_value=selected_issue,
            ),
        ):
            result = daily_digest_llm_upgrade._augment_papers_from_stats(
                object(), papers, stats
            )

        self.assertEqual([paper["number"] for paper in result], [10])

    def test_without_stats_keeps_date_labeled_issues(self):
        papers = [{"number": 10}, {"number": 11}]
        self.assertIs(
            daily_digest_llm_upgrade._augment_papers_from_stats(
                object(), papers, None
            ),
            papers,
        )


if __name__ == "__main__":
    unittest.main()
