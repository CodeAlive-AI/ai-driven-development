#!/usr/bin/env python3
"""Unit tests for coding-agents-management scripts (Claude Code & Antigravity)."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from init_marketplace import init_marketplace  # noqa: E402
from init_plugin import init_plugin  # noqa: E402
from validate_hooks import validate_file as validate_hooks_file  # noqa: E402
from validate_plugin import validate_plugin  # noqa: E402


class TestInitAndValidatePlugin(unittest.TestCase):
    def test_claude_plugin_scaffold_defaults_to_skills_and_validates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            pdir = init_plugin("sample-cc", tmp, agent="claude-code", with_hooks=True, with_mcp=True)
            self.assertTrue((pdir / "skills" / "example-skill" / "SKILL.md").exists())
            self.assertFalse((pdir / "commands").exists())
            res = validate_plugin(str(pdir), agent="auto")
            self.assertEqual(res.agent, "claude-code")
            self.assertTrue(res.is_valid, res.errors)

    def test_claude_plugin_supports_http_remote_mcp_and_new_events(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            pdir = init_plugin("http-cc", tmp, agent="claude-code")
            (pdir / ".mcp.json").write_text(
                json.dumps({"mcpServers": {"linear": {"type": "http", "url": "https://mcp.linear.app/mcp"}}}),
                encoding="utf-8",
            )
            (pdir / "hooks").mkdir()
            (pdir / "hooks" / "hooks.json").write_text(
                json.dumps(
                    {
                        "hooks": {
                            "PostToolUseFailure": [
                                {"matcher": "Bash", "hooks": [{"type": "http", "url": "https://hooks.local/fail"}]}
                            ],
                            "PreToolUse": [
                                {"matcher": "Edit", "hooks": [{"type": "agent", "prompt": "Verify edit safety"}]}
                            ],
                        }
                    }
                ),
                encoding="utf-8",
            )
            res = validate_plugin(str(pdir), agent="claude-code")
            self.assertTrue(res.is_valid, res.errors)

    def test_antigravity_plugin_scaffold_and_jsonc_validation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            pdir = init_plugin("sample-agy", tmp, agent="antigravity", with_hooks=True, with_mcp=True)
            self.assertTrue((pdir / "plugin.json").exists())
            self.assertTrue((pdir / "hooks.json").exists())
            self.assertTrue((pdir / "mcp_config.json").exists())
            self.assertTrue((pdir / "rules" / "AGENTS.md").exists())

            # Replace plugin.json with JSONC comments and trailing comma + unknown field warning
            (pdir / "plugin.json").write_text(
                """// JSONC plugin manifest
{
  "name": "sample-agy",
  "description": "Valid Antigravity plugin for testing.",
  "version": "1.2.0",
  "suggestedPrompts": ["One", "Two"],
  "skills": "skills/",
  "customUnknown": true,
}
""",
                encoding="utf-8",
            )
            res = validate_plugin(str(pdir), agent="auto")
            self.assertEqual(res.agent, "antigravity")
            self.assertTrue(res.is_valid, res.errors)
            self.assertTrue(any("customUnknown" in w for w in res.warnings))

    def test_antigravity_rejects_nested_hooks_dir_in_plugin(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            pdir = init_plugin("bad-agy", tmp, agent="antigravity")
            (pdir / "hooks").mkdir()
            (pdir / "hooks" / "hooks.json").write_text("{}", encoding="utf-8")
            res = validate_plugin(str(pdir), agent="antigravity")
            self.assertFalse(res.is_valid)
            self.assertTrue(any("hooks/hooks.json" in e for e in res.errors))

    def test_marketplace_scaffold(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            mdir = init_marketplace("team-mkt", tmp, initial_plugins=["alpha"])
            self.assertTrue((mdir / ".claude-plugin" / "marketplace.json").exists())
            self.assertTrue((mdir / "plugins" / "alpha" / ".claude-plugin" / "plugin.json").exists())


class TestValidateHooks(unittest.TestCase):
    def test_claude_command_only_event_rejects_prompt_hook(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cfg = Path(tmp) / "settings.json"
            cfg.write_text(
                json.dumps(
                    {
                        "hooks": {
                            "SessionStart": [
                                {"hooks": [{"type": "prompt", "prompt": "Should fail"}]}
                            ]
                        }
                    }
                ),
                encoding="utf-8",
            )
            res = validate_hooks_file(str(cfg), agent="claude-code")
            self.assertFalse(res["valid"])
            self.assertTrue(any("only supports 'command'" in e for e in res["errors"]))

    def test_antigravity_named_hooks_validates_flat_and_matcher_events(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            hfile = Path(tmp) / "hooks.json"
            hfile.write_text(
                json.dumps(
                    {
                        "audit": {
                            "enabled": True,
                            "SessionStart": [{"command": "./scripts/start.sh"}],
                            "PreToolUse": [
                                {
                                    "matcher": "run_command",
                                    "hooks": [{"type": "command", "command": "./scripts/guard.sh", "timeout": 5}],
                                }
                            ],
                        }
                    }
                ),
                encoding="utf-8",
            )
            res = validate_hooks_file(str(hfile), agent="auto")
            self.assertEqual(res["agent"], "antigravity")
            self.assertTrue(res["valid"], res["errors"])

    def test_antigravity_rejects_top_level_hooks_wrapper_and_settings_hooks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            hfile = Path(tmp) / "hooks.json"
            hfile.write_text(json.dumps({"hooks": {"PreToolUse": []}}), encoding="utf-8")
            res = validate_hooks_file(str(hfile), agent="antigravity")
            self.assertFalse(res["valid"])

            sfile = Path(tmp) / ".antigravity" / "settings.json"
            sfile.parent.mkdir()
            sfile.write_text(json.dumps({"hooks": {}}), encoding="utf-8")
            sres = validate_hooks_file(str(sfile), agent="auto")
            self.assertFalse(sres["valid"])


if __name__ == "__main__":
    unittest.main()
