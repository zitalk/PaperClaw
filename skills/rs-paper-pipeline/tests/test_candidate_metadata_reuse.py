from __future__ import annotations

import sys
import unittest
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import paper_processor


class CandidateMetadataReuseTests(unittest.TestCase):
    def test_builds_abs_info_from_discovery_candidate(self):
        info = paper_processor._candidate_abs_info(
            {
                "title": "Cached paper",
                "authors": ["Author One", "Author Two"],
                "institutions": "Example University",
                "abstract": "Cached abstract.",
                "published": "2026-09-01",
            }
        )

        self.assertEqual(info["title"], "Cached paper")
        self.assertEqual(info["authors"], "Author One, Author Two")
        self.assertEqual(info["abstract_en"], "Cached abstract.")
        self.assertEqual(info["date"], "2026-09-01")

    def test_missing_title_falls_back_to_arxiv_lookup(self):
        self.assertIsNone(paper_processor._candidate_abs_info({"abstract": "Only an abstract"}))


if __name__ == "__main__":
    unittest.main()
