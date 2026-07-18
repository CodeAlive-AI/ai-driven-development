import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from install_skill import install_skill  # noqa: E402


class InstallSkillTests(unittest.TestCase):
    def test_link_uses_one_canonical_real_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            source = base / "source" / "demo"
            target_root = base / "agent-skills"
            source.mkdir(parents=True)
            (source / "SKILL.md").write_text(
                "---\nname: demo\ndescription: test\n---\n",
                encoding="utf-8",
            )

            with patch("install_skill.get_skills_dir", return_value=target_root):
                success, _ = install_skill(
                    source,
                    "codex",
                    scope="global",
                    allow_duplicate_name=True,
                    link=True,
                )

            installed = target_root / "demo"
            self.assertTrue(success)
            self.assertTrue(installed.is_symlink())
            self.assertEqual(installed.resolve(), source.resolve())


if __name__ == "__main__":
    unittest.main()
