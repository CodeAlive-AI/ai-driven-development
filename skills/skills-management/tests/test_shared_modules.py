"""Tests for the modules that replaced per-script copies: claude_scopes, run_io, llm_cli."""

import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import claude_scopes  # noqa: E402
import llm_cli  # noqa: E402
import run_io  # noqa: E402
import skill_md  # noqa: E402


class ClaudeScopesTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.base = Path(self._tmp.name)
        self.user = self.base / "config" / "skills"
        self.project = self.base / "repo" / ".claude" / "skills"
        for directory in (self.user, self.project):
            directory.mkdir(parents=True)

    def scoped(self):
        env = patch.dict(os.environ, {"CLAUDE_CONFIG_DIR": str(self.base / "config")})
        cwd = patch.object(Path, "cwd", return_value=self.base / "repo")
        return env, cwd

    def make_skill(self, root: Path, name: str) -> Path:
        (root / name).mkdir()
        (root / name / "SKILL.md").write_text(f"---\nname: {name}\n---\n", encoding="utf-8")
        return root / name

    def test_user_scope_follows_claude_config_dir(self):
        # Before: ten scripts hard-coded ~/.claude/skills while install_skill.py
        # wrote to $CLAUDE_CONFIG_DIR/skills.
        env, cwd = self.scoped()
        with env, cwd:
            self.assertEqual(claude_scopes.get_user_skills_dir(), self.user)
            self.assertEqual(claude_scopes.get_project_skills_dir(), self.project)
            self.assertEqual(claude_scopes.scope_dirs(), [("user", self.user), ("project", self.project)])
            self.assertEqual(claude_scopes.scope_dirs("project"), [("project", self.project)])

    def test_find_skill_prefers_user_scope_and_needs_skill_md(self):
        env, cwd = self.scoped()
        for root in (self.user, self.project):
            self.make_skill(root, "demo")
        (self.user / "no-skill-md").mkdir()
        with env, cwd:
            self.assertEqual(claude_scopes.find_skill("demo"), (self.user / "demo", "user"))
            self.assertEqual(claude_scopes.find_skill("demo", "project"), (self.project / "demo", "project"))
            self.assertEqual(claude_scopes.find_skill("no-skill-md"), (None, None))
            self.assertEqual(claude_scopes.find_skill("missing"), (None, None))

    def test_broken_links_match_only_with_include_links(self):
        env, cwd = self.scoped()
        (self.project / "gone").symlink_to(self.base / "nowhere", target_is_directory=True)
        with env, cwd:
            self.assertEqual(claude_scopes.find_skill("gone"), (None, None))
            self.assertEqual(claude_scopes.find_skill("gone", include_links=True),
                             (self.project / "gone", "project"))


class RunIoTests(unittest.TestCase):
    def test_jsonl_strict_and_tolerant_readers(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "rows.jsonl"
            path.write_text('{"a": 1}\n\nnot json\n{"b": 2}\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "line 3"):
                run_io.load_jsonl(path)
            stderr = io.StringIO()
            with redirect_stderr(stderr):
                self.assertEqual(run_io.read_jsonl(path), [{"a": 1}, {"b": 2}])
            self.assertIn("line 3", stderr.getvalue())

    def test_json_round_trip_and_missing_text(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nested" / "out.json"
            run_io.write_json(path, {"name": "é"})
            self.assertEqual(run_io.read_json(path), {"name": "é"})
            self.assertIsNone(run_io.safe_read_text(Path(directory) / "absent.md"))


class LlmCliTests(unittest.TestCase):
    def test_safe_json_loads(self):
        self.assertEqual(llm_cli.safe_json_loads('```json\n{"ok": true}\n```'), {"ok": True})
        self.assertEqual(llm_cli.safe_json_loads('Sure: {"ok": 1} done'), {"ok": 1})
        self.assertIsNone(llm_cli.safe_json_loads("no json"))

    def test_call_llm_json_retries_once(self):
        answers = iter(["garbage", '{"ok": 2}'])
        with patch.object(llm_cli, "run_cli", side_effect=lambda *a, **k: next(answers)), \
             redirect_stderr(io.StringIO()):
            self.assertEqual(llm_cli.call_llm_json("model --flag", "prompt"), {"ok": 2})

    def test_run_cli_reports_missing_command(self):
        with self.assertRaisesRegex(RuntimeError, "CLI not found"):
            llm_cli.run_cli(["definitely-not-a-real-cli-xyz"], stdin="")


class SplitProtectedTests(unittest.TestCase):
    def test_split(self):
        block = f"{skill_md.SLOW_UPDATE_START}\nkeep\n{skill_md.SLOW_UPDATE_END}"
        self.assertEqual(skill_md.split_protected(f"a\n{block}\nb"), ("a\n", block, "\nb"))
        self.assertEqual(skill_md.split_protected("plain"), ("plain", None, ""))


if __name__ == "__main__":
    unittest.main()
