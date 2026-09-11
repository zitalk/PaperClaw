from pathlib import Path
from dataclasses import replace
import sys
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from clients import arxiv_client, github_ops, multisource_client
import check_source_api_keys
import paper_processor
from services import issue_index


class MultiSourceDiscoveryTest(unittest.TestCase):
    def test_arxiv_discovery_keeps_authors_and_affiliations(self):
        xml = """<?xml version="1.0" encoding="UTF-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
          <entry>
            <id>https://arxiv.org/abs/2609.00001v1</id>
            <title>RGB-D Salient Object Detection with Multimodal Fusion</title>
            <summary>We study visual salient object detection with RGB and depth inputs.</summary>
            <published>2026-09-01T12:00:00Z</published>
            <author><name>Alice Example</name><arxiv:affiliation>Example University</arxiv:affiliation></author>
            <author><name>Bob Example</name></author>
          </entry>
        </feed>"""
        with (
            patch.object(arxiv_client, "fetch_url_with_retry", return_value=xml),
            patch.object(arxiv_client.time, "sleep"),
        ):
            candidates = arxiv_client.fetch_recent_candidates(max_results=1, target_date="20260901")

        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["authors"], "Example Alice, Example Bob")
        self.assertEqual(candidates[0]["institutions"], "Example University")

    def test_arxiv_rate_limit_wait_is_capped_for_rolling_discovery(self):
        error = HTTPError("https://export.arxiv.org/api/query", 429, "rate limited", {"Retry-After": "600"}, None)
        with (
            patch.object(arxiv_client.urllib.request, "urlopen", side_effect=error),
            patch.object(arxiv_client.time, "sleep") as sleep,
            self.assertRaises(HTTPError),
        ):
            arxiv_client.fetch_url_with_retry(
                "https://export.arxiv.org/api/query",
                retries=2,
                rate_limit_backoff=[15, 30],
                max_rate_limit_wait=30,
            )

        sleep.assert_called_once_with(30)

    def test_arxiv_failure_does_not_abort_other_source_pipeline(self):
        health = []
        with (
            patch.object(
                multisource_client,
                "CONFIG",
                replace(multisource_client.CONFIG, multisource_enabled=False),
            ),
            patch.object(multisource_client, "fetch_arxiv_candidates", side_effect=HTTPError("url", 429, "rate limited", {}, None)),
        ):
            candidates = multisource_client.fetch_recent_candidates(target_date="20260901", source_status=health)

        self.assertEqual(candidates, [])
        self.assertEqual(health, [{"name": "arXiv", "status": "unavailable"}])

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

    def test_ieee_slot_serializes_requests(self):
        with (
            patch.object(multisource_client, "_ieee_last_request", 100.0),
            patch.object(multisource_client.time, "monotonic", side_effect=[100.25, 101.10]),
            patch.object(multisource_client.time, "sleep") as sleep,
        ):
            multisource_client._ieee_slot()

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

    def test_springer_uses_compatible_meta_endpoint_and_local_date_filter(self):
        payload = {
            "result": [{"total": "1"}],
            "records": [{
                "identifier": "doi:10.1007/example",
                "doi": "10.1007/example",
                "title": "Multimodal Industrial Anomaly Detection",
                "abstract": "A visual inspection method.",
                "publicationDate": "2026-09-01",
                "journalTitle": "Machine Vision and Applications",
                "creators": [{"creator": "Alice Example"}, "Bob Example"],
            }],
        }
        with (
            patch.object(
                multisource_client,
                "CONFIG",
                replace(multisource_client.CONFIG, springer_nature_api_key="test-key"),
            ),
            patch.object(multisource_client, "_json_request", return_value=payload) as request,
        ):
            papers = multisource_client.fetch_springer("2026-09-01")

        self.assertEqual(request.call_count, len(multisource_client.QUERY_BUNDLES))
        source, url = request.call_args_list[0].args[:2]
        query = parse_qs(urlparse(url).query)
        self.assertEqual(source, "Springer Nature")
        self.assertEqual(urlparse(url).path, "/meta/v2/json")
        self.assertEqual(query["api_key"], ["test-key"])
        self.assertEqual(query["q"], [f"keyword: {multisource_client.QUERY_BUNDLES[0]}"])
        self.assertEqual(query["p"], [str(multisource_client.SPRINGER_PAGE_SIZE)])
        self.assertNotIn("onlinedate", query["q"][0])
        self.assertEqual(papers[0]["venue"], "Machine Vision and Applications")
        self.assertEqual(papers[0]["authors"], "Example Alice, Example Bob")
        self.assertEqual(papers[0]["url"], "https://doi.org/10.1007/example")

    def test_healthcheck_uses_compatible_springer_meta_endpoint(self):
        with patch.dict(
            check_source_api_keys.os.environ,
            {"SPRINGER_NATURE_API_KEY": "test-key"},
            clear=False,
        ):
            springer = next(check for check in check_source_api_keys.build_checks() if check.name == "Springer Nature")

        self.assertEqual(urlparse(springer.url).path, "/meta/v2/json")
        health_query = parse_qs(urlparse(springer.url).query)
        self.assertEqual(health_query["api_key"], ["test-key"])
        self.assertEqual(health_query["q"], [f"keyword: {multisource_client.QUERY_BUNDLES[0]}"])
        self.assertEqual(health_query["p"], [str(multisource_client.SPRINGER_PAGE_SIZE)])
        self.assertEqual(springer.fallback_url, "")

    def test_healthcheck_maps_ieee_418_to_temporary_provider_block(self):
        self.assertEqual(
            check_source_api_keys._safe_http_detail(418, "IEEE Xplore"),
            "provider_anti_bot_or_temporary_block",
        )


if __name__ == "__main__":
    unittest.main()
