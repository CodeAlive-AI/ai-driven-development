import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from audit_skill_duplicates import (  # noqa: E402
    active_claude_plugin_skill_roots,
    audit_candidate,
    duplicate_groups,
    scan_roots,
)


class DuplicateAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def make_skill(self, parent: Path, directory: str, name: str, body: str = "body") -> Path:
        skill = parent / directory
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: test\n---\n\n{body}\n",
            encoding="utf-8",
        )
        return skill

    def classify(self, roots):
        groups = duplicate_groups(scan_roots(roots))
        self.assertEqual(len(groups), 1)
        return groups[0]["status"]

    def test_symlinks_to_one_real_skill_are_aliases(self):
        root = self.base / "skills"
        source = self.make_skill(root, "demo", "demo")
        (root / "demo-link").symlink_to(source, target_is_directory=True)
        self.assertEqual(self.classify([(root, "canonical-user")]), "alias")

    def test_identical_copies_are_replicas(self):
        first = self.base / "first"
        second = self.base / "second"
        self.make_skill(first, "demo", "demo")
        self.make_skill(second, "demo", "demo")
        self.assertEqual(
            self.classify([(first, "agent-user"), (second, "agent-user")]),
            "replica",
        )

    def test_different_content_is_divergent(self):
        first = self.base / "first"
        second = self.base / "second"
        self.make_skill(first, "demo", "demo", "old")
        self.make_skill(second, "demo", "demo", "new")
        self.assertEqual(
            self.classify([(first, "agent-user"), (second, "agent-user")]),
            "divergent",
        )

    def test_backup_directory_is_stale_backup(self):
        root = self.base / "skills"
        self.make_skill(root, "demo", "demo", "new")
        self.make_skill(root, "demo.backup-20260101", "demo", "old")
        self.assertEqual(self.classify([(root, "canonical-user")]), "stale-backup")

    def test_plugin_and_global_divergence_is_namespaced(self):
        global_root = self.base / "global"
        plugin_root = self.base / "plugin"
        self.make_skill(global_root, "demo", "demo", "new")
        self.make_skill(plugin_root, "demo", "demo", "old")
        self.assertEqual(
            self.classify([(global_root, "canonical-user"), (plugin_root, "plugin-cache")]),
            "namespaced-divergent",
        )

    def test_plugin_cache_versions_are_managed_not_user_conflicts(self):
        first = self.base / "plugin-v1"
        second = self.base / "plugin-v2"
        self.make_skill(first, "demo", "demo", "old")
        self.make_skill(second, "demo", "demo", "new")
        groups = duplicate_groups(scan_roots([
            (first, "plugin-cache"),
            (second, "plugin-cache"),
        ]))
        self.assertEqual(groups[0]["status"], "managed-plugin-divergent")
        self.assertFalse(groups[0]["requires_decision"])

    @patch("audit_skill_duplicates.subprocess.run")
    def test_only_enabled_claude_plugin_roots_are_active(self, run):
        run.return_value.stdout = (
            '[{"enabled": true, "installPath": "/plugins/current"}, '
            '{"enabled": false, "installPath": "/plugins/old"}]'
        )
        self.assertEqual(
            active_claude_plugin_skill_roots(),
            [Path("/plugins/current/skills")],
        )

    def test_candidate_preflight_blocks_identical_existing_copy(self):
        installed_root = self.base / "installed"
        candidate_root = self.base / "candidate"
        self.make_skill(installed_root, "demo", "demo")
        candidate = self.make_skill(candidate_root, "demo", "demo")
        result = audit_candidate(candidate, roots=[(installed_root, "canonical-user")])
        self.assertTrue(result["blocked"])
        self.assertEqual(result["matches"][0]["relation"], "identical")


if __name__ == "__main__":
    unittest.main()
