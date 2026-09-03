import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from build_pages_site import (
    _classify_paper,
    _display_authors,
    _display_institutions,
    build_site,
    parse_report,
)


class PagesBuilderTest(unittest.TestCase):
    def test_page_categories_match_research_directions(self):
        examples = {
            "RGB-T Salient Object Detection with Cross-Modal Guidance": "多模态显著目标检测",
            "Robust Multimodal Fusion under Missing Modalities": "多模态视觉学习",
            "Cross-Camera Multi-Object Tracking and Re-Identification": "多视角与多目标感知",
            "Small Object Detection in UAV Aerial Imagery": "无人机视觉",
            "Training-Free Open-Vocabulary Semantic Segmentation": "免训练开放集分割",
        }
        for title, expected in examples.items():
            with self.subTest(title=title):
                self.assertEqual(_classify_paper(title, ""), expected)

    def test_training_free_aerial_segmentation_uses_specific_direction(self):
        self.assertEqual(
            _classify_paper(
                "Restrict, Don't Retrain: Inference-Time VLM Guidance for Zero-Shot Aerial Segmentation",
                "无需重训练即可提升航拍图像零样本分割精度。",
            ),
            "免训练开放集分割",
        )

    def test_card_authors_are_limited_to_three(self):
        self.assertEqual(
            _display_authors("Alice A, Bob B, Carol C, David D"),
            "Alice A, Bob B, Carol C, et al.",
        )

    def test_card_institutions_keep_top_level_organizations(self):
        raw = (
            "School of Automation, Southeast University, Nanjing, China；"
            "Chair of Robotics, Technical University of Munich, Munich, Germany"
        )
        self.assertEqual(
            _display_institutions(raw),
            "Southeast University, Technical University of Munich",
        )

    def test_card_institutions_are_limited_to_three(self):
        raw = "A University；B University；C University；D University"
        self.assertEqual(
            _display_institutions(raw),
            "A University, B University, C University, et al.",
        )

    def test_card_institutions_rejoin_broken_affiliation_fragments(self):
        raw = (
            "School of Computer Science and Technology, Wuhan University of Science and；"
            "Hubei Province Key Laboratory of Intelligent Information Processing and；"
            "Real-Time Industrial System, Wuhan University of Science and Technology, Wuhan；"
            "State Key Laboratory of Robotics and Intelligent Systems, Shenyang Institute of；"
            "Automation, Chinese Academy of Sciences, Shenyang 110016, China；"
            "China University of Chinese Academy of Sciences, Beijing 100049, China"
        )
        self.assertEqual(
            _display_institutions(raw),
            "Wuhan University of Science and Technology, Chinese Academy of Sciences, "
            "University of Chinese Academy of Sciences",
        )
        self.assertNotIn("Science and,", _display_institutions(raw))

    def test_card_institution_removes_city_and_country_suffix(self):
        self.assertEqual(
            _display_institutions("Shandong University Jinan China"),
            "Shandong University",
        )

    def test_card_institutions_drop_secondary_units_when_parent_exists(self):
        self.assertEqual(
            _display_institutions(
                "School of Computing；State University of New York at Binghamton"
            ),
            "State University of New York at Binghamton",
        )

    def test_card_institution_removes_author_prose_prefix(self):
        self.assertEqual(
            _display_institutions(
                "Centre for Robotics (CAOR)；The authors are with Paris-Saclay University"
            ),
            "Paris-Saclay University",
        )

    def test_card_institution_extracts_university_from_embedded_school(self):
        self.assertEqual(
            _display_institutions(
                "School of Automation Engineering of the University of Electronic Science "
                "and Technology of China (UESTC)"
            ),
            "University of Electronic Science and Technology of China (UESTC)",
        )

    def test_card_institutions_ignore_non_affiliation_prose(self):
        raw = (
            "Swedish Defence Research Agency (FOI), Linköping, Sweden；"
            "Kalman filter over a full center-size box state as a strong physical baseline"
        )
        self.assertEqual(
            _display_institutions(raw),
            "Swedish Defence Research Agency (FOI)",
        )

    def test_parse_current_report(self):
        report = parse_report(REPO_ROOT / "daily_reports" / "202609" / "20260901.md")
        self.assertEqual(report["date"], "20260901")
        self.assertEqual(report["paper_count"], 17)
        self.assertEqual(report["papers"][0]["issue_number"], 1)
        self.assertIn("UAV", report["papers"][0]["title"])

    def test_build_site_outputs_public_json_without_secrets(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "site"
            report_count, paper_count = build_site(output)
            self.assertGreaterEqual(report_count, 1)
            self.assertGreaterEqual(paper_count, 17)
            self.assertTrue((output / "index.html").exists())
            payload = (output / "data" / "papers.json").read_text(encoding="utf-8")
            data = json.loads(payload)
            self.assertGreaterEqual(len(data["papers"]), 17)
            self.assertNotIn("GITHUB_TOKEN", payload)
            self.assertNotIn("LLM_API_KEY", payload)


if __name__ == "__main__":
    unittest.main()
