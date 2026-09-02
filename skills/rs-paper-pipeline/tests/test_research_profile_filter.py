from pathlib import Path
import sys
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from clients.arxiv_client import has_remote_sensing_signal
import daily_arxiv_cross_filter
from daily_arxiv_cross_filter import has_ai_signal
from services.filter_assets import load_filter_keywords, load_filter_prompt_template


class ResearchProfileFilterTest(unittest.TestCase):
    def test_filter_assets_are_valid(self):
        config = load_filter_keywords()
        self.assertGreaterEqual(len(config["rs_query_terms"]), 60)
        self.assertEqual(config["arxiv_categories"], ["cs.CV", "eess.IV", "cs.RO", "cs.MM", "eess.SP"])
        self.assertIn("salient object detection", config["rs_query_terms"])
        self.assertIn("UAV vision", config["rs_query_terms"])
        self.assertIn("camera LiDAR fusion", config["rs_query_terms"])
        self.assertIn("vision language perception", config["rs_query_terms"])
        self.assertIn("training-free open-vocabulary segmentation", config["rs_query_terms"])
        self.assertIn("{{candidate_lines}}", load_filter_prompt_template())

    def test_research_direction_examples_pass_domain_filter(self):
        examples = [
            "Uncertainty-Aware Modality Fusion for Unaligned RGB-T Salient Object Detection",
            "Prompted RGB-D Saliency Detection with Missing Depth",
            "Event-RGB Fusion for Robust Visual Saliency",
            "Multi-Camera Multi-Object Tracking with Cross-View Association",
            "UAV-Based Vision for Small Object Detection in Aerial Video",
            "Camera-LiDAR Fusion for Robust 3D Object Detection",
            "Cross-Spectral Person Re-Identification in Visible and Infrared Cameras",
            "Missing-Modality Robust Multimodal Segmentation with Modality Dropout",
            "Vision-Language Perception for Open-Vocabulary UAV Object Detection",
            "Multispectral Tiny Object Detection in Low-Altitude Imagery",
            "Training-Free Open-Vocabulary Semantic Segmentation with Frozen CLIP",
            "Annotation-Free Open-Set Segmentation for Remote Sensing Images",
            "Zero-Shot Open-World Segmentation in UAV Aerial Imagery",
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

    def test_llm_filter_batches_broad_search_candidates(self):
        candidates = [
            {
                "arxiv_id": f"2609.{index:05d}v1",
                "title": f"Multimodal vision paper {index}",
                "abstract": "Camera and LiDAR fusion for object detection.",
            }
            for index in range(71)
        ]
        batch_sizes = []

        def fake_batch(batch, batch_number, batch_total):
            batch_sizes.append((len(batch), batch_number, batch_total))
            return batch[:1]

        with patch.object(daily_arxiv_cross_filter, "_llm_cross_filter_batch", side_effect=fake_batch):
            selected = daily_arxiv_cross_filter.llm_cross_filter(candidates)

        self.assertEqual(batch_sizes, [(35, 1, 3), (35, 2, 3), (1, 3, 3)])
        self.assertEqual(len(selected), 3)


if __name__ == "__main__":
    unittest.main()
