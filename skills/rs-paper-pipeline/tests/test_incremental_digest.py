import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import daily_digest_llm_upgrade as digest
import daily_arxiv_cross_filter as filtering
from services.digest_builder import refresh_digest_status
from services.report_status import read_run_status

DATE = "20260903"
REPO = "zitalk/PaperClaw"


def paper(number, state="open", date=DATE):
    return {"number": number, "state": state, "title": "UAV object detection",
            "labels": [{"name": date}], "html_url": f"https://github.com/{REPO}/issues/{number}",
            "body": f"| **arXiv** | [paper](https://arxiv.org/abs/2609.{number:05d}) |\n| **作者** | Alice, Bob |"}


def report(*numbers):
    rows = [f"| UAV object detection | Alice, Bob | 暂无 | Old summary {n} | [#{n}](https://github.com/{REPO}/issues/{n}) |" for n in numbers]
    return f"# 日报 {DATE}\n\n## 📌 今日概况\n\n旧概况\n\n## 🗂 今日文章列表\n\n| 标题 | 作者 | 单位 | 一句话概括 | Issue |\n|---|---|---|---|---|\n" + "\n".join(rows) + "\n\n## 🔎 观察\n\n旧观察"


class IncrementalDigestTest(unittest.TestCase):
    def test_only_own_approved_table_links_are_retained(self):
        body = report(1) + "\nhttps://github.com/zitalk/PaperClaw/issues/2"
        body += "\n| Wrong repo | A | B | C | [#3](https://github.com/other/repo/issues/3) |"
        self.assertEqual(digest.published_paper_numbers(body, REPO), {1})

    def test_retention_ignores_stale_date_labels_closed_and_wrong_dates(self):
        issues = [SimpleNamespace(_rawData=p) for p in [paper(1), paper(2, "closed"), paper(3, date="20260902"), paper(4)]]
        result = digest.retain_previous_papers(MagicMock(), issues, report(1, 2, 3), DATE, REPO)
        self.assertEqual([p["number"] for p in result], [1])

    def test_retention_rechecks_venue_gate(self):
        p = paper(1)
        p["body"] = "| **出版物** | Scientific Reports |\n| **PaperClaw ID** | `doi:10.1038/s41598-example` |"
        self.assertEqual(digest.retain_previous_papers(MagicMock(), [SimpleNamespace(_rawData=p)], report(1), DATE, REPO), [])

    def test_missing_card_404_skipped_but_transient_failure_does_not_erase_it(self):
        repo = MagicMock()
        error = RuntimeError("gone")
        error.status = 404
        repo.get_issue.side_effect = error
        self.assertEqual(digest.retain_previous_papers(repo, [], report(1), DATE, REPO), [])
        repo.get_issue.side_effect = RuntimeError("network")
        with self.assertRaises(RuntimeError):
            digest.retain_previous_papers(repo, [], report(1), DATE, REPO)

    def run_round(self, current):
        repo = MagicMock()
        old = SimpleNamespace(title=f"日报 {DATE}", number=99, body=report(1),
                              _rawData={"title": f"日报 {DATE}"}, edit=MagicMock())
        issues = [old, SimpleNamespace(title="Paper", _rawData=paper(1)),
                  SimpleNamespace(title="Paper", _rawData=paper(2)),
                  SimpleNamespace(title="Stale paper", _rawData=paper(3))]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "stats.json"
            path.write_text(json.dumps({"date": DATE, "candidate_count": len(current),
                "new_llm_selected_count": len(current), "source_status": [{"name": "arXiv", "status": "ok"}]}), encoding="utf-8")
            with (
                patch.object(digest, "CONFIG", SimpleNamespace(github_token="test", llm_api_key="test", temp_dir=Path(folder), github_repo=REPO)),
                patch.object(digest, "get_repo", return_value=repo),
                patch.object(digest, "load_open_issues", return_value=issues),
                patch.object(digest, "_augment_papers_from_stats", return_value=current),
                patch("services.digest_builder.call_llm", return_value='{"overview":"Summary","one_liners":[]}') as llm,
            ):
                digest.main(DATE, str(path), incremental=True)
        repo.create_issue.assert_not_called()
        return old.edit.call_args.kwargs["body"], llm.call_count

    def test_late_paper_is_appended_without_stale_date_labeled_card(self):
        body, calls = self.run_round([paper(2)])
        self.assertEqual(digest.published_paper_numbers(body, REPO), {1, 2})
        self.assertIn("本轮新增入报 1 篇；目标日累计收录 2 篇", body)
        self.assertEqual(calls, 1)

    def test_empty_or_same_round_preserves_old_paper_and_avoids_llm(self):
        for current in ([], [paper(1)]):
            body, calls = self.run_round(current)
            self.assertEqual(digest.published_paper_numbers(body, REPO), {1})
            self.assertIn("Old summary 1", body)
            self.assertIn("本轮新增入报 0 篇；目标日累计收录 1 篇", body)
            self.assertEqual(calls, 0)

    def test_no_addition_round_still_reports_source_failure(self):
        stats = {"source_status": [{"name": "IEEE Xplore", "status": "unavailable"}], "new_included_count": 0}
        body = refresh_digest_status(report(1), stats, 1)
        self.assertEqual(read_run_status(body)["status"], "degraded")
        self.assertIn("IEEE Xplore", body)
        self.assertIn("Old summary 1", body)

    def test_reused_candidate_is_not_llm_filtered_or_processed_again(self):
        candidate = {"paper_id": "2609.00001", "arxiv_id": "2609.00001", "title": "UAV object detection", "abstract": "Test", "published": "2026-09-03"}
        old = SimpleNamespace(number=1, state="open", body=paper(1)["body"])
        with (
            patch.object(filtering, "CONFIG", SimpleNamespace(github_token="test", llm_api_key="test")),
            patch.object(filtering, "get_repo"), patch.object(filtering, "ensure_index", return_value={}),
            patch.object(filtering, "fetch_recent_candidates", return_value=[candidate]),
            patch.object(filtering, "load_existing_issue_map", return_value={"2609.00001": old}),
            patch.object(filtering, "call_llm") as llm,
            patch.object(filtering, "process_candidate") as process,
            patch.object(filtering, "save_index"),
        ):
            filtering.main(target_date=DATE, incremental=True)
        llm.assert_not_called()
        process.assert_not_called()


if __name__ == "__main__":
    unittest.main()
