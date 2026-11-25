import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync_references.py"
SPEC = importlib.util.spec_from_file_location("sync_references", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ReferenceSyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "references" / "disciplines" / "example.md"
        self.source.parent.mkdir(parents=True)
        self.source.write_text("example\n", encoding="utf-8")
        self.skill = self.root / "skills" / "example"
        self.skill.mkdir(parents=True)
        (self.skill / "SKILL.md").write_text("example", encoding="utf-8")
        self.copy = self.skill / "references" / "disciplines" / "example.md"

    def run_sync(self, check=True):
        with contextlib.redirect_stdout(io.StringIO()):
            return MODULE.synchronize(self.root, check)

    def test_missing_copy_fails_without_writing(self):
        self.assertEqual(self.run_sync(), 1)
        self.assertFalse(self.copy.exists())

    def test_nested_file_copied_and_matches(self):
        self.assertEqual(self.run_sync(check=False), 0)
        self.assertEqual(self.copy.read_bytes(), self.source.read_bytes())
        self.assertEqual(self.run_sync(), 0)

    def test_different_copy_fails(self):
        self.run_sync(check=False)
        self.copy.write_text("changed", encoding="utf-8")
        self.assertEqual(self.run_sync(), 1)

    def test_extra_copy_fails_without_deletion(self):
        self.run_sync(check=False)
        extra = self.copy.with_name("obsolete.md")
        extra.write_text("old", encoding="utf-8")
        self.assertEqual(self.run_sync(), 1)
        self.assertTrue(extra.exists())

    def test_empty_source_fails(self):
        self.source.unlink()
        self.assertEqual(self.run_sync(check=False), 1)

    def test_missing_skills_fails(self):
        (self.skill / "SKILL.md").unlink()
        self.assertEqual(self.run_sync(), 1)


if __name__ == "__main__":
    unittest.main()
