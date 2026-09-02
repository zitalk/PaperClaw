import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import run_rs_daily_workday
from paper_processor import cleanup_downloads
from pipeline_config import load_config


class CrossPlatformRuntimeTest(unittest.TestCase):
    def test_subprocesses_reuse_current_python(self):
        self.assertEqual(run_rs_daily_workday.PYTHON_BIN, sys.executable)

    def test_relative_runtime_paths_are_resolved_from_pipeline_root(self):
        config = load_config()
        self.assertEqual(config.temp_dir, ROOT / "tmp")
        self.assertFalse(config.keep_downloads)
        self.assertEqual(
            config.filter_keywords_path,
            ROOT / "scripts" / "config" / "filter_keywords.json",
        )

    def test_pipeline_lock_rejects_a_second_holder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            lock_path = Path(temp_dir) / "pipeline.lock"
            with run_rs_daily_workday._exclusive_lock(lock_path):
                with self.assertRaises(RuntimeError):
                    with run_rs_daily_workday._exclusive_lock(lock_path):
                        self.fail("A second lock holder should not be admitted")

    def test_transient_pdf_and_source_are_cleaned(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            pdf = temp_path / "2609.12345v1.pdf"
            source = temp_path / "2609.12345v1.src"
            report = temp_path / "keep.md"
            pdf.write_bytes(b"pdf")
            source.write_bytes(b"source")
            report.write_text("keep", encoding="utf-8")

            removed = cleanup_downloads("2609.12345v1", temp_path, keep_downloads=False)

            self.assertCountEqual(removed, [pdf.name, source.name])
            self.assertFalse(pdf.exists())
            self.assertFalse(source.exists())
            self.assertTrue(report.exists())

    def test_download_cleanup_can_be_disabled(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            pdf = Path(temp_dir) / "2609.12345v1.pdf"
            pdf.write_bytes(b"pdf")

            removed = cleanup_downloads("2609.12345v1", Path(temp_dir), keep_downloads=True)

            self.assertEqual(removed, [])
            self.assertTrue(pdf.exists())


if __name__ == "__main__":
    unittest.main()
