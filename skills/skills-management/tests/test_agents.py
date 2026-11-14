import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import agents  # noqa: E402
import audit_skill_duplicates  # noqa: E402


class RegistryShapeTests(unittest.TestCase):
    def test_every_entry_is_complete_and_keyed_by_name(self):
        for agent_id, config in agents.AGENTS.items():
            with self.subTest(agent_id):
                self.assertEqual(agent_id, config["name"])
                for key in ("display_name", "project_dir", "global_dir", "source"):
                    self.assertTrue(config[key], key)
                self.assertFalse(os.path.isabs(config["project_dir"]))
                self.assertTrue(config["detect_paths"] or config.get("detect_project_markers"))

    def test_shared_dir_agents_install_globally_into_shared_dir(self):
        for agent_id in ("codex", "cursor", "gemini-cli", "opencode", "amp", "kimi-code-cli", "pi"):
            with self.subTest(agent_id):
                self.assertEqual(agents.get_global_skills_dir(agent_id), Path.home() / ".agents" / "skills")

    def test_antigravity_installs_outside_shared_dir(self):
        self.assertEqual(
            agents.get_global_skills_dir("antigravity"), Path.home() / ".gemini" / "config" / "skills"
        )


class PathExpansionTests(unittest.TestCase):
    def test_home_env_relocates_global_and_detect_paths(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"GROK_HOME": tmp}):
            self.assertEqual(agents.get_global_skills_dir("grok"), Path(tmp) / "skills")
            self.assertIn("grok", agents.detect_installed_agents(cwd=Path(tmp)))

    def test_xdg_config_home_replaces_dot_config(self):
        with patch.dict(os.environ, {"XDG_CONFIG_HOME": "/xdg"}):
            self.assertEqual(agents.get_global_skills_dir("crush"), Path("/xdg/crush/skills"))
            self.assertIn(Path("/xdg/agents/skills"), agents.get_all_global_skills_dirs("amp"))

    def test_prefix_match_is_by_path_component(self):
        config = {"home_env": ("VIBE_HOME", "~/.vibe")}
        with patch.dict(os.environ, {"VIBE_HOME": "/v"}):
            self.assertEqual(agents.expand_path("~/.viberant/skills", config), Path.home() / ".viberant/skills")

    def test_project_marker_detects_agent(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / ".replit").write_text("", encoding="utf-8")
            self.assertIn("replit", agents.detect_installed_agents(cwd=Path(tmp)))


class ExtraDirsTests(unittest.TestCase):
    def test_extra_global_dirs_follow_primary_without_duplicates(self):
        dirs = agents.get_all_global_skills_dirs("cursor")
        self.assertEqual(dirs[0], Path.home() / ".agents" / "skills")
        self.assertIn(Path.home() / ".cursor" / "skills", dirs)
        self.assertEqual(len(dirs), len(set(dirs)))

    def test_sharing_includes_agents_reading_dir_as_extra(self):
        sharing = agents.agents_sharing_dir(Path.home() / ".config" / "agents" / "skills")
        self.assertIn("amp", sharing)
        self.assertIn("kimi-code-cli", sharing)

    def test_audit_scans_extra_global_dirs(self):
        with tempfile.TemporaryDirectory() as tmp:
            legacy = Path(tmp) / "legacy"
            legacy.mkdir()
            with patch.object(audit_skill_duplicates, "get_all_global_skills_dirs", return_value=[legacy]), \
                 patch.object(audit_skill_duplicates, "active_claude_plugin_skill_roots", return_value=[]):
                roots = audit_skill_duplicates.default_roots(Path(tmp))
            self.assertIn(legacy, [root for root, _ in roots])

    def test_symlinked_root_to_known_root_is_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            real = Path(tmp) / "config" / "skills"
            real.mkdir(parents=True)
            legacy = Path(tmp) / "legacy-skills"
            legacy.symlink_to(real, target_is_directory=True)
            roots = {}
            audit_skill_duplicates.add_root(roots, real, "agent-user")
            audit_skill_duplicates.add_root(roots, legacy, "agent-user")
            self.assertEqual([path for path, _ in roots.values()], [real])


if __name__ == "__main__":
    unittest.main()
