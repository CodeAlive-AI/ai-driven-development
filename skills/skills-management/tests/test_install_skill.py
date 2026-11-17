import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from install_skill import global_scope_command, install_skill  # noqa: E402


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

    def _alias_audit(self, source: Path) -> dict:
        """An audit whose only match is another link to the candidate itself."""
        return {
            "matches": [{
                "relation": "already-discoverable",
                "record": {"path": str(source), "root_kind": "plugin-source"},
            }],
            "blocked": True,
        }

    def _make_skill(self, base: Path) -> Path:
        source = base / "source" / "demo"
        source.mkdir(parents=True)
        (source / "SKILL.md").write_text(
            "---\nname: demo\ndescription: test\n---\n", encoding="utf-8"
        )
        return source

    def test_link_is_not_blocked_by_its_own_real_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            source = self._make_skill(base)
            target_root = base / "agent-skills"
            with patch("install_skill.audit_candidate", return_value=self._alias_audit(source)), \
                    patch("install_skill.get_skills_dir", return_value=target_root):
                success, message = install_skill(source, "codex", scope="global", link=True)

            self.assertTrue(success, message)
            self.assertEqual((target_root / "demo").resolve(), source.resolve())

    def test_copy_is_still_blocked_by_the_same_real_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            source = self._make_skill(base)
            target_root = base / "agent-skills"
            with patch("install_skill.audit_candidate", return_value=self._alias_audit(source)), \
                    patch("install_skill.get_skills_dir", return_value=target_root):
                success, message = install_skill(source, "codex", scope="global", link=False)

            self.assertFalse(success)
            self.assertIn("already discoverable", message)
            self.assertFalse((target_root / "demo").exists())

    def test_project_scope_inside_a_skill_directory_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            source = self._make_skill(base)
            manager = base / "manager"
            (manager / "scripts").mkdir(parents=True)
            (manager / "SKILL.md").write_text(
                "---\nname: manager\ndescription: test\n---\n", encoding="utf-8"
            )
            success, message = install_skill(
                source, "codex", scope="project", cwd=manager / "scripts",
                allow_duplicate_name=True,
            )

            self.assertFalse(success)
            self.assertIn("--scope global", message)
            self.assertFalse((manager / ".agents").exists())

    def test_global_scope_command_replaces_the_scope(self):
        command = global_scope_command(
            ["scripts/install_skill.py", "/src/demo", "--agent", "codex", "-s", "project", "--link"]
        )
        self.assertEqual(
            command,
            "uv run scripts/install_skill.py /src/demo --agent codex --link --scope global",
        )


if __name__ == "__main__":
    unittest.main()
