import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from audit_skill_duplicates import (  # noqa: E402
    active_antigravity_plugin_skill_roots,
    active_claude_plugin_skill_roots,
    antigravity_manifest_skill_roots,
    audit_candidate,
    default_roots,
    duplicate_groups,
    format_text,
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

    def test_antigravity_plugin_roots_respect_config_bom_skills_field_and_escape(self):
        home = self.base / "home"
        plugins = home / ".gemini" / "config" / "plugins"

        p_enabled = plugins / "p-enabled"
        self.make_skill(p_enabled / "skills", "s1", "s1")
        (p_enabled / "plugin.json").write_text('{"name": "p-enabled"}', encoding="utf-8")

        p_disabled_manifest = plugins / "p-disabled"
        self.make_skill(p_disabled_manifest / "skills", "s2", "s2")
        (p_disabled_manifest / "plugin.json").write_text(
            '{"name": "p-disabled", "disabled": true}', encoding="utf-8"
        )

        p_overridden = plugins / "p-overridden"
        self.make_skill(p_overridden / "skills", "s3", "s3")
        (p_overridden / "plugin.json").write_text('{"name": "p-overridden"}', encoding="utf-8")

        p_string_skills = plugins / "p-str"
        self.make_skill(p_string_skills / "custom-skills", "s4", "s4")
        (p_string_skills / "plugin.json").write_text(
            '{"name": "p-str", "skills": "./custom-skills"}', encoding="utf-8"
        )

        p_list_escape = plugins / "p-esc"
        outside = self.base / "outside-skills"
        self.make_skill(outside, "evil", "evil")
        self.make_skill(p_list_escape / "extra", "s5", "s5")
        (p_list_escape / "plugin.json").write_text(
            '{"name": "p-esc", "skills": ["./extra", "../../../outside-skills"]}',
            encoding="utf-8",
        )

        # UTF-8 BOM + JSONC in config.json overrides plugin enabled state
        (home / ".gemini" / "config" / "config.json").write_text(
            '\ufeff{\n  // override\n  "plugins": {\n    "p-overridden": {"enabled": false,},\n    "p-disabled": {"enabled": true},\n  }\n}\n',
            encoding="utf-8",
        )

        roots = active_antigravity_plugin_skill_roots(home=home, query_cli=False)
        resolved = {r.resolve() for r in roots}
        self.assertIn((p_enabled / "skills").resolve(), resolved)
        self.assertIn((p_disabled_manifest / "skills").resolve(), resolved)
        self.assertNotIn((p_overridden / "skills").resolve(), resolved)
        self.assertIn((p_string_skills / "custom-skills").resolve(), resolved)
        self.assertIn((p_list_escape / "extra").resolve(), resolved)
        self.assertNotIn(outside.resolve(), resolved)

    @patch("audit_skill_duplicates.subprocess.run")
    def test_antigravity_cli_plugin_list_merged_and_fallback_safe(self, run):
        home = self.base / "home"
        cli_plugin = self.base / "cli-plugin"
        self.make_skill(cli_plugin / "skills", "cli-skill", "cli-skill")
        run.return_value.stdout = (
            f'[{{"name": "cli-p", "enabled": true, "path": "{cli_plugin}"}}, '
            f'{{"name": "off-p", "enabled": false, "path": "{self.base / "off"}"}}]'
        )
        roots = active_antigravity_plugin_skill_roots(home=home, query_cli=True)
        self.assertEqual([r.resolve() for r in roots], [(cli_plugin / "skills").resolve()])

        run.side_effect = FileNotFoundError("no agy")
        self.assertEqual(active_antigravity_plugin_skill_roots(home=home, query_cli=True), [])

    def test_antigravity_manifests_jsonc_cycles_and_workspace_confinement(self):
        home = self.base / "home"
        g_cfg = home / ".gemini" / "config"
        g_cfg.mkdir(parents=True)
        g_extra = self.base / "global-extra"
        self.make_skill(g_extra, "g1", "g1")
        (g_cfg / "shared.json").write_text(
            f'{{"inherits": [{{"path": "skills.json"}}], "entries": [{{"path": "{g_extra}"}}]}}',
            encoding="utf-8",
        )
        (g_cfg / "skills.json").write_text(
            '{\n  // global manifest\n  "inherits": [{"path": "shared.json"}],\n  "entries": [],\n}\n',
            encoding="utf-8",
        )

        repo = self.base / "repo"
        (repo / ".git").mkdir(parents=True)
        (repo / ".agents").mkdir()
        in_repo = repo / "team-skills"
        self.make_skill(in_repo, "r1", "r1")
        outside = self.base / "outside"
        self.make_skill(outside, "out", "out")
        (repo / ".agents" / "out-link").symlink_to(outside, target_is_directory=True)
        (repo / ".agents" / "skills.json").write_text(
            f'{{"entries": [{{"path": "team-skills"}}, {{"path": "../outside"}}, {{"path": "{outside}"}}, {{"path": ".agents/out-link"}}]}}',
            encoding="utf-8",
        )

        found = antigravity_manifest_skill_roots(home, [repo])
        resolved_kinds = {(p.resolve(), kind) for p, kind in found}
        self.assertIn((g_extra.resolve(), "manifest-global"), resolved_kinds)
        self.assertIn((in_repo.resolve(), "manifest-workspace"), resolved_kinds)
        self.assertNotIn((outside.resolve(), "manifest-workspace"), resolved_kinds)

    def test_default_roots_finds_agy_plugin_repo_and_legacy_workspace_dirs(self):
        repo = self.base / "agy-plugin-repo"
        (repo / ".git").mkdir(parents=True)
        (repo / "plugin.json").write_text('{"name": "demo-plugin"}', encoding="utf-8")
        self.make_skill(repo / "skills", "plug-s", "plug-s")
        self.make_skill(repo / ".agent" / "skills", "legacy-ws", "legacy-ws")
        self.make_skill(repo / ".agents" / "plugins" / "local-p" / "skills", "ws-plug", "ws-plug")

        with patch("audit_skill_duplicates.active_claude_plugin_skill_roots", return_value=[]), \
             patch("audit_skill_duplicates.active_antigravity_plugin_skill_roots", return_value=[]):
            roots = default_roots(repo)
        kinds = {(r.resolve(), k) for r, k in roots}
        self.assertIn(((repo / "skills").resolve(), "plugin-source"), kinds)
        self.assertIn(((repo / ".agent" / "skills").resolve(), "repo"), kinds)
        self.assertIn(((repo / ".agents" / "plugins" / "local-p" / "skills").resolve(), "plugin-workspace"), kinds)

    def test_duplicate_audit_tracks_invocation_mode_and_mode_mismatch(self):
        first = self.base / "first"
        second = self.base / "second"
        s1 = self.make_skill(first, "demo", "demo")
        (s1 / "SKILL.md").write_text(
            "---\nname: demo\ndescription: test\ndisable-model-invocation: true\n---\n\nbody\n",
            encoding="utf-8",
        )
        (s1 / "agents").mkdir()
        (s1 / "agents" / "openai.yaml").write_text(
            "policy:\n  allow_implicit_invocation: false\n",
            encoding="utf-8",
        )

        s2 = self.make_skill(second, "demo", "demo")
        (s2 / "SKILL.md").write_text(
            "---\nname: demo\ndescription: test\ndisable-model-invocation: true\n---\n\nbody\n",
            encoding="utf-8",
        )

        groups = duplicate_groups(scan_roots([(first, "canonical-user"), (second, "agent-user")]))
        self.assertEqual(len(groups), 1)
        grp = groups[0]
        self.assertEqual(grp["status"], "divergent")
        self.assertTrue(grp["invocation_mode_mismatch"])
        modes = {r["invocation_mode"] for r in grp["records"]}
        self.assertEqual(modes, {"manual", "manual-frontmatter-only"})

        rendered = format_text(groups)
        self.assertIn("[mode mismatch]", rendered)
        self.assertIn("[manual]", rendered)
        self.assertIn("[manual-frontmatter-only]", rendered)


if __name__ == "__main__":
    unittest.main()
