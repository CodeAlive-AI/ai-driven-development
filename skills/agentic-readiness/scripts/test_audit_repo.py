#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from audit_repo import audit


class AgenticReadinessAuditTests(unittest.TestCase):
    def make_repo(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "AGENTS.md").write_text(
            "# Project\n\nBefore editing a target path, read every applicable `AGENTS.md`.\n",
            encoding="utf-8",
        )
        (root / "CLAUDE.md").write_text("@AGENTS.md\n", encoding="utf-8")
        return temp, root

    def test_canonical_agents_with_claude_import_has_no_discovery_issue(self) -> None:
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)

        report = audit(root)

        self.assertTrue(report["instruction_topology"]["canonical_agents_md"])
        self.assertTrue(report["instruction_topology"]["claude_compatibility_file"])
        messages = [issue["message"] for issue in report["issues"]]
        self.assertFalse(any("does not import" in message for message in messages))
        self.assertFalse(any("duplicate copies" in message for message in messages))

    def test_duplicate_claude_file_is_flagged(self) -> None:
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        text = (root / "AGENTS.md").read_text(encoding="utf-8")
        (root / "CLAUDE.md").write_text(text, encoding="utf-8")

        report = audit(root)

        self.assertTrue(
            any("duplicate copies" in issue["message"] for issue in report["issues"])
        )

    def test_tracked_override_is_flagged(self) -> None:
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        (root / "AGENTS.override.md").write_text(
            "# Temporary override\n", encoding="utf-8"
        )
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(
            ["git", "add", "AGENTS.md", "CLAUDE.md", "AGENTS.override.md"],
            cwd=root,
            check=True,
        )

        report = audit(root)

        self.assertTrue(
            any("masks AGENTS.md" in issue["message"] for issue in report["issues"])
        )

    def test_codex_default_budget_overflow_is_flagged(self) -> None:
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        (root / "AGENTS.md").write_text(
            "# Project\n" + ("x" * 33_000), encoding="utf-8"
        )

        report = audit(root)

        self.assertGreater(
            report["instruction_topology"]["codex_project_chains"]["worst_known_chain"][
                "combined_bytes"
            ],
            32_768,
        )
        self.assertTrue(
            any(issue["category"] == "context-budget" for issue in report["issues"])
        )

    def test_configuration_values_are_not_reported(self) -> None:
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        (root / ".codex").mkdir()
        secret_value = "must-not-appear-in-report"
        (root / ".codex" / "config.toml").write_text(
            f'api_key = "{secret_value}"\n[mcp_servers.demo]\ncommand = "demo"\n',
            encoding="utf-8",
        )

        report = audit(root)
        serialized = json.dumps(report)

        self.assertNotIn(secret_value, serialized)
        config = report["agent_configuration"][0]
        self.assertIn("api_key", config["possible_secret_keys"])
        self.assertEqual(config["mcp_server_count"], 1)

    def test_child_git_repository_requires_explicit_route_and_is_not_traversed(
        self,
    ) -> None:
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        child = root / "backend"
        child.mkdir()
        (child / ".git").mkdir()
        (child / "AGENTS.md").write_text("# Backend\n", encoding="utf-8")

        report = audit(root)

        self.assertEqual(report["repository"]["child_git_repositories"], ["backend"])
        self.assertEqual(
            report["instruction_topology"]["unrouted_child_git_repositories"],
            ["backend"],
        )
        instruction_paths = [
            item["path"] for item in report["instruction_topology"]["files"]
        ]
        self.assertNotIn("backend/AGENTS.md", instruction_paths)


if __name__ == "__main__":
    unittest.main()
