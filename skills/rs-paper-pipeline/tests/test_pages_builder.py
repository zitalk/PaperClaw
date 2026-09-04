import json
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from build_pages_site import (
    _classify_paper,
    _ccf_grade,
    _display_authors,
    _display_institutions,
    _source_label,
    build_site,
    collect_site_data,
    parse_report,
)
from services.research_taxonomy import classify_research, public_directions
from services.report_status import REPORT_MARKER


class PagesBuilderTest(unittest.TestCase):
    def test_page_categories_match_research_directions(self):
        examples = {
            "RGB-T Salient Object Detection with Cross-Modal Guidance": "多模态视觉学习",
            "Robust Multimodal Visual Fusion under Missing Modalities": "多模态视觉学习",
            "Cross-Camera Multi-Object Tracking and Re-Identification": "多视角与多目标感知",
            "Small Object Detection in UAV Aerial Imagery": "无人机视觉",
            "Training-Free Open-Vocabulary Semantic Segmentation": "免训练开放集分割",
        }
        for title, expected in examples.items():
            with self.subTest(title=title):
                self.assertEqual(_classify_paper(title, ""), expected)

    def test_training_free_aerial_segmentation_uses_specific_direction(self):
        self.assertIn(
            "免训练开放集分割",
            classify_research(
                "Restrict, Don't Retrain: Inference-Time VLM Guidance for Zero-Shot Aerial Segmentation",
                "无需重训练即可提升航拍图像零样本分割精度。",
            )["categories"],
        )

    def test_four_public_directions_and_cod_topic(self):
        directions = public_directions()
        self.assertEqual(len(directions), 4)
        self.assertNotIn("多模态显著目标检测", [d["name"] for d in directions])
        self.assertIn("mm-cod", [t["id"] for t in directions[0]["topics"]])

    def test_cross_direction_labels_are_not_exclusive(self):
        result = classify_research("Training-Free Open-Vocabulary Aerial Segmentation with Vision-Language Models")
        self.assertEqual(set(result["categories"]), {"免训练开放集分割", "多模态视觉学习", "无人机视觉"})
        result = classify_research("UAV Cross-Camera Multi-Object Tracking")
        self.assertEqual(set(result["categories"]), {"无人机视觉", "多视角与多目标感知"})

    def test_cod_is_a_multimodal_group_subtopic(self):
        for title in ["RGB-D Camouflaged Object Detection", "Concealed Object Detection in Images", "伪装目标检测与分割"]:
            result = classify_research(title)
            self.assertEqual(result["categories"], ["多模态视觉学习"])
            self.assertIn("mm-cod", [t["id"] for t in result["topics"]])

    def test_zero_shot_and_annotation_free_are_not_training_free_proof(self):
        for title in ["Zero-Shot Open-Vocabulary Segmentation with CLIP", "Annotation-Free Open-Set Segmentation", "SAM for Open-World Segmentation"]:
            self.assertNotIn("免训练开放集分割", classify_research(title)["categories"])
        self.assertNotIn("免训练开放集分割", classify_research("Open-Set Segmentation", "Our method is not training-free.")["categories"])

    def test_no_forced_multimodal_or_aerial_category(self):
        for title in ["COD removal in wastewater", "Satellite Image Classification", "Single Object Tracking", "Medical Image Segmentation", "Infrared Image Classification"]:
            result = classify_research(title)
            self.assertEqual(result["categories"], [])
            self.assertEqual(result["classification_status"], "pending")

    def test_abstract_is_used_as_classification_evidence(self):
        result = classify_research("New Visual Model", abstract="We propose camera-LiDAR fusion for UAV detection.")
        self.assertEqual(set(result["categories"]), {"多模态视觉学习", "无人机视觉"})

    def test_stereo_and_multi_fisheye_are_multiview(self):
        self.assertIn("多视角与多目标感知", classify_research("Stereo 4D Radar for 3D Object Detection")["categories"])
        self.assertEqual(set(classify_research("Multi-Fisheye Perception for UAVs")["categories"]), {"多视角与多目标感知", "无人机视觉"})

    def test_single_modality_cod_does_not_claim_multimodal_input(self):
        topic_ids = [t["id"] for t in classify_research("Camouflaged Object Detection")["topics"]]
        self.assertIn("mm-cod", topic_ids)
        self.assertNotIn("mm-perception", topic_ids)

    def test_camouflaged_vehicle_cod_synonym(self):
        result = classify_research("Domain shift-robust object detection with GenAI image editing", abstract="我们以伪装军用车辆检测作为具有挑战性的域偏移场景进行研究。")
        self.assertEqual(result["categories"], ["多模态视觉学习"])
        self.assertIn("mm-cod", [t["id"] for t in result["topics"]])
        self.assertNotIn("mm-perception", [t["id"] for t in result["topics"]])

    def test_zero_reports_visible_only_with_own_provenance(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            month = root / "202609"
            month.mkdir()
            (month / "20260904.md").write_text("# 日报 20260904\n" + REPORT_MARKER + "\n## 📌 今日概况\n\n检索完成，0 篇。", encoding="utf-8")
            (month / "20260903.md").write_text("# 日报 20260903\n旧项目的空日报", encoding="utf-8")
            with patch("build_pages_site.REPORTS_DIR", root):
                reports, papers = collect_site_data()
        self.assertEqual([r["date"] for r in reports], ["20260904"])
        self.assertEqual(reports[0]["paper_count"], 0)
        self.assertEqual(papers, [])

    def test_readme_lists_all_subtopics_and_has_no_workflow_diagram(self):
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        for direction in public_directions():
            self.assertIn(direction["name"], readme)
            for topic in direction["topics"]:
                self.assertIn(topic["name"], readme)
        self.assertNotIn("```mermaid", readme)
        self.assertNotIn("## 工作流", readme)

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

    def test_card_without_institution_uses_compact_placeholder(self):
        self.assertEqual(_display_institutions(""), "暂无")
        self.assertEqual(_display_institutions("暂无"), "暂无")

    def test_source_label_uses_common_venue_abbreviations(self):
        self.assertEqual(
            _source_label("IEEE Transactions on Multimedia", "IEEE Xplore", "doi:10.1/example"),
            "TMM",
        )
        self.assertEqual(
            _source_label(
                "Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition",
                "OpenAlex",
                "doi:10.1/example",
            ),
            "CVPR",
        )
        self.assertEqual(_source_label("arXiv", "arXiv", "2609.00001v1"), "arXiv")
        self.assertEqual(
            _source_label("", "", "doi:10.1038/s41598-026-69495-2"),
            "Sci Rep",
        )
        self.assertEqual(
            _source_label("", "", "doi:10.1088/2631-8695/aea1db"),
            "Eng Res Express",
        )

    def test_ccf_badge_uses_exact_venue_abbreviation(self):
        self.assertEqual(_ccf_grade("CVPR"), "A")
        self.assertEqual(_ccf_grade("TMM"), "A")
        self.assertEqual(_ccf_grade("IJCAI"), "B")
        self.assertEqual(_ccf_grade("ICLR"), "A")
        self.assertEqual(_ccf_grade("KBS"), "C")
        self.assertEqual(_ccf_grade("ESWA"), "C")
        self.assertEqual(_ccf_grade("PR"), "B")
        self.assertEqual(_ccf_grade("IROS"), "C")
        self.assertEqual(_ccf_grade("arXiv"), "")
        self.assertEqual(_ccf_grade("Scientific Reports"), "")

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
            self.assertEqual(len(data["directions"]), 4)
            self.assertTrue(all("categories" in p and "topics" in p for p in data["papers"]))
            self.assertGreaterEqual(len(data["papers"]), 17)
            self.assertNotIn("GITHUB_TOKEN", payload)
            self.assertNotIn("LLM_API_KEY", payload)


if __name__ == "__main__":
    unittest.main()
