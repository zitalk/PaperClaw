from pathlib import Path
from dataclasses import replace
import sys
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from clients import github_ops, multisource_client
import check_source_api_keys
import paper_processor
from services import issue_index


class MultiSourceDiscoveryTest(unittest.TestCase):
    def test_dedup_merges_sources_and_prefers_real_arxiv_id(self):
        scopus = multisource_client._candidate(
            source="Elsevier Scopus",
            source_id="SCOPUS_ID:1",
            title="Training-Free Open-Set Segmentation",
            abstract="Short abstract.",
            published="2026-09-01",
            doi="10.1000/example",
            authors=["Alice Example"],
            venue="IEEE Transactions on Multimedia",
            url="https://example.org/scopus/1",
        )
        arxiv = multisource_client._candidate(
            source="arXiv",
            source_id="2609.00001",
            title="Training-Free Open-Set Segmentation",
            abstract="A longer abstract with more method and experiment details.",
            published="2026-09-01",
            doi="10.1000/example",
            arxiv_id="2609.00001",
            authors=["Alice Example", "Bob Example"],
            url="https://arxiv.org/abs/2609.00001",
        )

        merged = multisource_client._merge_items([scopus, arxiv])

        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]["paper_id"], "2609.00001")
        self.assertEqual(merged[0]["arxiv_id"], "2609.00001")
        self.assertEqual(merged[0]["sources"], ["Elsevier Scopus", "arXiv"])
        self.assertEqual(merged[0]["venue"], "IEEE Transactions on Multimedia")
        self.assertIn("longer abstract", merged[0]["abstract"])

    def test_semantic_scholar_slot_enforces_cumulative_one_rps(self):
        with (
            patch.object(multisource_client, "_semantic_last_request", 100.0),
            patch.object(multisource_client.time, "monotonic", side_effect=[100.25, 101.10]),
            patch.object(multisource_client.time, "sleep") as sleep,
        ):
            multisource_client._semantic_slot()

        sleep.assert_called_once()
        self.assertAlmostEqual(sleep.call_args.args[0], 0.85, places=6)

    def test_elsevier_uses_api_key_and_default_scopus_endpoint_only(self):
        with (
            patch.object(
                multisource_client,
                "CONFIG",
                replace(multisource_client.CONFIG, elsevier_api_key="test-key"),
            ),
            patch.object(multisource_client, "_json_request", return_value={}) as request,
        ):
            self.assertEqual(multisource_client.fetch_elsevier_scopus("2026-09-01"), [])

        self.assertEqual(request.call_count, len(multisource_client.QUERY_BUNDLES))
        for call in request.call_args_list:
            source, url = call.args[:2]
            query = parse_qs(urlparse(url).query)
            self.assertEqual(source, "Elsevier Scopus")
            self.assertEqual(urlparse(url).path, "/content/search/scopus")
            self.assertEqual(query["view"], ["STANDARD"])
            self.assertNotIn("insttoken", query)
            self.assertEqual(call.kwargs["headers"], {"X-ELS-APIKey": "test-key"})

    def test_generic_paperclaw_id_is_recovered_from_issue_body(self):
        body = "| **PaperClaw ID** | `doi:10.1000/example` |"
        self.assertEqual(github_ops.extract_arxiv_id_from_text(body), "doi:10.1000/example")
        self.assertEqual(issue_index._extract_arxiv_id(body), "doi:10.1000/example")

    def test_issue_index_keeps_publication_source_metadata(self):
        body = (
            "| **来源** | IEEE Xplore |\n"
            "| **出版物** | IEEE Transactions on Multimedia |\n"
            "| **链接** | [来源页面](https://ieeexplore.ieee.org/document/123) |"
        )
        self.assertEqual(
            issue_index._source_metadata(body, "doi:10.1000/example"),
            {
                "source": "IEEE Xplore",
                "venue": "IEEE Transactions on Multimedia",
                "url": "https://ieeexplore.ieee.org/document/123",
            },
        )

    def test_issue_index_recognizes_arxiv_source(self):
        self.assertEqual(
            issue_index._source_metadata("", "2609.00001v1"),
            {
                "source": "arXiv",
                "venue": "arXiv",
                "url": "https://arxiv.org/abs/2609.00001v1",
            },
        )

    def test_issue_index_keeps_real_code_repository_url(self):
        body = (
            "| **代码** | [开源仓库](https://github.com/example/vision-model) |\n"
            "### Q8: 代码开源？\n已开源。"
        )
        self.assertEqual(
            issue_index._source_metadata(body, "doi:10.1000/example")["code_url"],
            "https://github.com/example/vision-model",
        )

    def test_issue_index_does_not_infer_code_without_repository_url(self):
        body = "### Q8: 代码开源？\n作者表示代码之后会公开。"
        self.assertNotIn("code_url", issue_index._source_metadata(body, "doi:10.1000/example"))

    def test_arxiv_processing_keeps_merged_publication_metadata(self):
        sources, venue = paper_processor._publication_metadata(
            {
                "sources": ["arXiv", "OpenAlex"],
                "venue": "IEEE Transactions on Multimedia",
            }
        )
        self.assertEqual(sources, "arXiv, OpenAlex")
        self.assertEqual(venue, "IEEE Transactions on Multimedia")

    def test_healthcheck_does_not_require_insttoken_or_sciencedirect(self):
        with patch.dict(
            check_source_api_keys.os.environ,
            {"ELSEVIER_API_KEY": "test-key", "ELSEVIER_INSTTOKEN": "ignored"},
            clear=False,
        ):
            checks = check_source_api_keys.build_checks()

        elsevier_checks = [check for check in checks if check.name.startswith("Elsevier")]
        self.assertEqual([check.name for check in elsevier_checks], ["Elsevier Scopus"])
        self.assertNotIn("X-ELS-Insttoken", elsevier_checks[0].headers)
        self.assertEqual(
            check_source_api_keys._safe_http_detail(400, "Elsevier Scopus"),
            "authentication_or_api_key_configuration_rejected",
        )


if __name__ == "__main__":
    unittest.main()
