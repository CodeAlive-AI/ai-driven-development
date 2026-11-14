"""Regression tests for symlink- and shared-directory-safe skill file operations."""

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import delete_skill  # noqa: E402
import fs_ops  # noqa: E402
import move_skill  # noqa: E402
import move_skill_agent  # noqa: E402


def make_skill(path: Path, body: str = "v1") -> Path:
    path.mkdir(parents=True)
    (path / "SKILL.md").write_text(f"---\nname: {path.name}\ndescription: test\n---\n{body}\n", encoding="utf-8")
    return path


class Sandbox(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.base = Path(self._tmp.name).resolve()
        self.agent_dirs = {agent: self.base / agent / "skills" for agent in ("alpha", "beta", "gamma")}
        for directory in self.agent_dirs.values():
            directory.mkdir(parents=True)
        self.claude_user = self.base / "claude-user" / "skills"
        self.claude_project = self.base / "claude-project" / "skills"
        self.claude_user.mkdir(parents=True)
        self.claude_project.mkdir(parents=True)

        patches = [
            patch.object(delete_skill, "detect_installed_agents", return_value=list(self.agent_dirs)),
            patch.object(delete_skill, "get_agent_config", side_effect=lambda a: {"display_name": a.title()}),
            patch.object(
                delete_skill,
                "get_skills_dir",
                side_effect=lambda a, scope, cwd=None: self.agent_dirs[a] if scope == "global" else None,
            ),
            patch.object(delete_skill, "get_user_skills_dir", return_value=self.claude_user),
            patch.object(delete_skill, "get_project_skills_dir", return_value=self.claude_project),
            patch.object(move_skill, "get_user_skills_dir", return_value=self.claude_user),
            patch.object(move_skill, "get_project_skills_dir", return_value=self.claude_project),
        ]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)
        self.addCleanup(self._tmp.cleanup)

    def run_quietly(self, func, *args, **kwargs):
        with redirect_stdout(io.StringIO()) as out:
            result = func(*args, **kwargs)
        return result, out.getvalue()


class MoveSkillTests(Sandbox):
    def test_force_move_onto_own_symlink_target_keeps_content(self):
        real = make_skill(self.claude_project / "demo")
        (self.claude_user / "demo").symlink_to(real, target_is_directory=True)

        ok, output = self.run_quietly(move_skill.move_skill, "demo", "project", force=True)

        self.assertFalse(ok)
        self.assertIn("same directory", output)
        self.assertTrue((real / "SKILL.md").is_file())
        self.assertFalse(real.is_symlink())

    def test_already_in_scope_is_a_successful_no_op(self):
        make_skill(self.claude_user / "demo")
        ok, _ = self.run_quietly(move_skill.move_skill, "demo", "user")
        self.assertTrue(ok)


class DeleteSkillTests(Sandbox):
    def _canonical_with_links(self) -> Path:
        real = make_skill(self.agent_dirs["alpha"] / "demo")
        for agent in ("beta", "gamma"):
            (self.agent_dirs[agent] / "demo").symlink_to(real, target_is_directory=True)
        return real

    def test_all_agents_removes_canonical_and_every_link(self):
        self._canonical_with_links()

        ok, _ = self.run_quietly(delete_skill.delete_skill_agents, "demo", all_agents=True, force=True)

        self.assertTrue(ok)
        for directory in self.agent_dirs.values():
            self.assertFalse(fs_ops.path_present(directory / "demo"))

    def test_deleting_canonical_that_others_link_to_is_refused(self):
        real = self._canonical_with_links()

        ok, output = self.run_quietly(delete_skill.delete_skill_agents, "demo", agents=["alpha"], force=True)

        self.assertFalse(ok)
        self.assertIn("--all-agents --force", output)
        self.assertTrue((real / "SKILL.md").is_file())

    def test_deleting_only_a_link_keeps_canonical(self):
        real = self._canonical_with_links()

        ok, _ = self.run_quietly(delete_skill.delete_skill_agents, "demo", agents=["beta"], force=True)

        self.assertTrue(ok)
        self.assertFalse(fs_ops.path_present(self.agent_dirs["beta"] / "demo"))
        self.assertTrue((real / "SKILL.md").is_file())

    def test_broken_symlink_can_be_deleted(self):
        (self.agent_dirs["beta"] / "demo").symlink_to(self.base / "gone", target_is_directory=True)

        ok, _ = self.run_quietly(delete_skill.delete_skill_agents, "demo", agents=["beta"], force=True)

        self.assertTrue(ok)
        self.assertFalse(fs_ops.path_present(self.agent_dirs["beta"] / "demo"))

    def test_without_terminal_and_force_nothing_is_deleted(self):
        real = make_skill(self.claude_user / "demo")

        with patch.object(sys, "stdin", io.StringIO("")):
            ok, output = self.run_quietly(delete_skill.delete_skill_default, "demo")

        self.assertFalse(ok)
        self.assertIn("--force", output)
        self.assertTrue((real / "SKILL.md").is_file())


class FsOpsTests(Sandbox):
    def test_failed_copy_keeps_existing_target(self):
        source = make_skill(self.base / "src" / "demo", "new")
        target = make_skill(self.agent_dirs["alpha"] / "demo", "old")

        with patch.object(fs_ops.shutil, "copytree", side_effect=OSError("disk full")):
            with self.assertRaises(OSError):
                fs_ops.copy_into_place(source, target)

        self.assertIn("old", (target / "SKILL.md").read_text(encoding="utf-8"))
        self.assertEqual(sorted(p.name for p in target.parent.iterdir()), ["demo"])

    def test_copy_replaces_broken_symlink_target(self):
        source = make_skill(self.base / "src" / "demo")
        target = self.agent_dirs["alpha"] / "demo"
        target.symlink_to(self.base / "gone", target_is_directory=True)

        fs_ops.copy_into_place(source, target)

        self.assertFalse(target.is_symlink())
        self.assertTrue((target / "SKILL.md").is_file())

    def test_moving_a_symlink_keeps_it_a_symlink(self):
        real = make_skill(self.base / "canonical" / "demo")
        link = self.agent_dirs["alpha"] / "demo"
        link.symlink_to(real, target_is_directory=True)
        target = self.agent_dirs["beta"] / "demo"

        with patch.object(move_skill_agent, "get_skills_dir", side_effect=lambda a, s, cwd=None: self.agent_dirs[a]), \
             patch.object(move_skill_agent, "find_skill_in_agent", return_value=(link, "global")), \
             patch.object(move_skill_agent, "agents_sharing_dir", return_value=[]), \
             patch.object(move_skill_agent, "get_agent_config", side_effect=lambda a: {"display_name": a}):
            ok, _ = move_skill_agent.move_skill("demo", "alpha", "beta", to_scope="global")

        self.assertTrue(ok)
        self.assertTrue(target.is_symlink())
        self.assertEqual(target.resolve(), real)
        self.assertFalse(fs_ops.path_present(link))


if __name__ == "__main__":
    unittest.main()
