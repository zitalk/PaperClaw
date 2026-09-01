from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from clients.arxiv_client import has_remote_sensing_signal
from daily_arxiv_cross_filter import has_ai_signal
from services.filter_assets import load_filter_keywords, load_filter_prompt_template


class ResearchProfileFilterTest(unittest.TestCase):
    def test_filter_assets_are_valid(self):
        config = load_filter_keywords()
        self.assertGreaterEqual(len(config["rs_query_terms"]), 20)
        self.assertIn("salient object detection", config["rs_query_terms"])
        self.assertIn("UAV vision", config["rs_query_terms"])
        self.assertIn("{{candidate_lines}}", load_filter_prompt_template())

    def test_research_direction_examples_pass_domain_filter(self):
        examples = [
            "Uncertainty-Aware Modality Fusion for Unaligned RGB-T Salient Object Detection",
            "Prompted RGB-D Saliency Detection with Missing Depth",
            "Event-RGB Fusion for Robust Visual Saliency",
            "Multi-Camera Multi-Object Tracking with Cross-View Association",
            "UAV-Based Vision for Small Object Detection in Aerial Video",
        ]
        for text in examples:
            with self.subTest(text=text):
                self.assertTrue(has_remote_sensing_signal(text))
                self.assertTrue(has_ai_signal(text))

    def test_unrelated_examples_do_not_pass_domain_filter(self):
        examples = [
            "Multimodal Sentiment Analysis for Social Media Conversations",
            "Energy-Efficient Routing for UAV Communication Networks",
            "Land Cover Classification from Satellite Images",
            "Large Language Model Agents for Recommendation Systems",
        ]
        for text in examples:
            with self.subTest(text=text):
                self.assertFalse(has_remote_sensing_signal(text))


if __name__ == "__main__":
    unittest.main()
