import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import run_rs_daily_workday
from pipeline_config import load_config


class CrossPlatformRuntimeTest(unittest.TestCase):
    def test_subprocesses_reuse_current_python(self):
        self.assertEqual(run_rs_daily_workday.PYTHON_BIN, sys.executable)

    def test_relative_runtime_paths_are_resolved_from_pipeline_root(self):
        config = load_config()
        self.assertEqual(config.temp_dir, ROOT / "tmp")
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


if __name__ == "__main__":
    unittest.main()
