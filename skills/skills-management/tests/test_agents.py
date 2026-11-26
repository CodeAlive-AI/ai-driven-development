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

    def test_antigravity_topology_and_shared_global_safety(self):
        shared = Path.home() / ".agents" / "skills"
        app_cfg = agents.AGENTS["antigravity"]
        self.assertEqual(app_cfg["extra_project_dirs"], [".agent/skills", "_agents/skills", "_agent/skills"])
        self.assertFalse(app_cfg.get("reads_shared_global", False))
        self.assertNotIn(shared, agents.get_readable_global_skills_dirs("antigravity"))
        self.assertNotIn("antigravity", agents.agents_sharing_dir(shared))

        cli_cfg = agents.AGENTS["antigravity-cli"]
        self.assertEqual(cli_cfg["extra_project_dirs"], [".agent/skills", "_agents/skills", "_agent/skills"])
        self.assertTrue(cli_cfg.get("reads_shared_global"))
        self.assertNotIn(shared, agents.get_all_global_skills_dirs("antigravity-cli"))
        self.assertIn(shared, agents.get_readable_global_skills_dirs("antigravity-cli"))
        self.assertIn("antigravity-cli", agents.agents_sharing_dir(shared))

    def test_porch_aliases_omp_and_env_overrides(self):
        self.assertEqual(agents.canonical_agent_id("agy"), "antigravity-cli")
        self.assertEqual(agents.canonical_agent_id("gemini"), "gemini-cli")
        self.assertEqual(agents.canonical_agent_id("hermes"), "hermes-agent")
        self.assertEqual(agents.canonical_agent_id("kimi-code"), "kimi-code-cli")
        self.assertEqual(agents.canonical_agent_id("grok-build"), "grok")
        self.assertEqual(agents.canonical_agent_id("claude-desktop"), "claude-code")
        self.assertTrue(agents.validate_agent("agy"))
        self.assertIn("omp", agents.AGENTS)
        self.assertTrue(agents.AGENTS["omp"].get("reads_shared_global"))
        self.assertTrue(agents.AGENTS["hermes-agent"].get("supports_nested_categories"))
        with tempfile.TemporaryDirectory() as tmp:
            fake_home = Path(tmp)
            with patch.dict(os.environ, {"KIMI_CODE_HOME": str(fake_home / "kimi"), "CURSOR_CONFIG_DIR": str(fake_home / "cur")}):
                self.assertIn(fake_home / "kimi", [agents.expand_path(p, agents.AGENTS["kimi-code-cli"]) for p in agents.AGENTS["kimi-code-cli"]["detect_paths"]])
                self.assertIn(fake_home / "cur" / "skills", agents.get_all_global_skills_dirs("cursor"))
            hermes_dir = fake_home / ".hermes"
            hermes_dir.mkdir(parents=True)
            self.assertFalse(agents.hermes_reads_shared_global(home=fake_home))
            (hermes_dir / "config.yaml").write_text("skills:\n  external_dirs:\n    - ~/.agents/skills\n", encoding="utf-8")
            self.assertTrue(agents.hermes_reads_shared_global(home=fake_home))

    def test_antigravity_detected_from_config_json_or_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            fake_home = Path(tmp)
            config_dir = fake_home / ".gemini" / "config"
            config_dir.mkdir(parents=True)
            (config_dir / "config.json").write_text("{}", encoding="utf-8")
            with patch("pathlib.Path.home", return_value=fake_home), \
                 patch.object(agents, "expand_path", side_effect=lambda p, c=None: Path(p.replace("~", str(fake_home)))):
                self.assertIn("antigravity", agents.detect_installed_agents(cwd=fake_home))

            (config_dir / "config.json").unlink()
            (config_dir / "skills").mkdir()
            with patch("pathlib.Path.home", return_value=fake_home), \
                 patch.object(agents, "expand_path", side_effect=lambda p, c=None: Path(p.replace("~", str(fake_home)))):
                self.assertIn("antigravity", agents.detect_installed_agents(cwd=fake_home))


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
