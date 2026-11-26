"""Comprehensive unit tests for skill revision, topology reconciliation, usage telemetry, and porch parity."""

from __future__ import annotations

import json
import os
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import agents  # noqa: E402
import install_skill  # noqa: E402
import revise_skills  # noqa: E402
import skill_topology  # noqa: E402
import skill_usage  # noqa: E402
import sync_skills  # noqa: E402


def _make_skill(parent: Path, folder: str, name: str | None = None, desc: str = "Use when testing.", extra_body: str = "") -> Path:
    sdir = parent / folder
    sdir.mkdir(parents=True, exist_ok=True)
    fm = ["---"]
    if name is not None:
        fm.append(f"name: {name}")
    if desc is not None:
        fm.append(f"description: {desc}")
    fm.append("---")
    (sdir / "SKILL.md").write_text("\n".join(fm) + "\n\n# Heading\n\nStep 1.\n" + extra_body, encoding="utf-8")
    return sdir


class TopologyAndHygieneTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.base = Path(self._tmp.name)
        self.home = self.base / "home"
        self.home.mkdir()

    def test_porch_rejected_in_install_skill(self):
        src = _make_skill(self.base / "src", "demo", "demo")
        ok, msg = install_skill.install_skill(src, "porch", scope="global", allow_duplicate_name=True)
        self.assertFalse(ok)
        self.assertIn("orchestrator", msg)

    def test_hermes_nested_categories_and_bundled_manifest(self):
        hermes_skills = self.home / ".hermes" / "skills"
        _make_skill(hermes_skills / "apple", "apple-notes", "apple-notes")
        _make_skill(hermes_skills, "dogfood", "dogfood")
        empty_cat = hermes_skills / "stale-empty"
        (empty_cat / "__pycache__").mkdir(parents=True)
        (hermes_skills / ".bundled_manifest").write_text("apple/apple-notes: deadbeef\n", encoding="utf-8")

        roots = skill_topology.discover_roots(scope="global", cwd=self.base, home=self.home, agents_filter=["hermes"])
        entries, _ = skill_topology.scan_topology(roots, home=self.home, cwd=self.base)

        by_name = {e.name: e for e in entries}
        self.assertIn("apple-notes", by_name)
        self.assertEqual(by_name["apple-notes"].category, "apple")
        self.assertTrue(by_name["apple-notes"].is_bundled)
        self.assertIn("dogfood", by_name)
        self.assertFalse(by_name["dogfood"].is_ghost)
        self.assertIn("stale-empty", by_name)
        self.assertTrue(by_name["stale-empty"].is_ghost)

    def test_broken_links_ghost_dirs_lockfile_and_trojan_unicode(self):
        shared = self.home / ".agents" / "skills"
        agy = self.home / ".gemini" / "config" / "skills"
        claude = self.home / ".claude" / "skills"
        shared.mkdir(parents=True)
        agy.mkdir(parents=True)
        claude.mkdir(parents=True)

        # Ghost dir
        (shared / "ghost-one" / "scripts" / "__pycache__").mkdir(parents=True)
        # Trojan unicode in valid skill
        _make_skill(shared, "sneaky", "sneaky", extra_body="Hidden\u202ebidi payload\n")
        # Broken relative link
        (agy / "orphan-rel").symlink_to("../../../.agents/skills/orphan-rel", target_is_directory=True)
        # Symlink loop
        (claude / "loop-a").symlink_to(claude / "loop-b", target_is_directory=True)
        (claude / "loop-b").symlink_to(claude / "loop-a", target_is_directory=True)
        # Lockfile with 1 valid + 1 orphan
        (self.home / ".agents" / ".skill-lock.json").write_text(
            json.dumps({
                "version": 3,
                "skills": {
                    "sneaky": {"source": "a/b", "sourceUrl": "https://example.com"},
                    "orphan-rel": {"source": "x/y", "sourceUrl": "https://example.com"},
                },
            }),
            encoding="utf-8",
        )

        report = revise_skills.run_revision(scope="global", cwd=self.base, home=self.home, usage_mode="off")
        self.assertEqual(report["summary"]["broken_symlinks"], 3)
        self.assertEqual(report["summary"]["ghost_dirs"], 1)
        self.assertEqual(report["summary"]["orphaned_lock_entries"], 1)
        trojan_rules = [i["rule"] for e in report["triage"]["integrity_errors"] for i in e["issues"]]
        self.assertIn("trojan-unicode", trojan_rules)

    def test_monorepo_ancestor_walk_and_four_axis_duplicates(self):
        repo = self.base / "mono"
        (repo / ".git").mkdir(parents=True)
        nested_cwd = repo / "packages" / "web"
        nested_cwd.mkdir(parents=True)
        shared_global = self.home / ".agents" / "skills"

        _make_skill(shared_global, "deploy-app", "deploy-app", extra_body="global\n")
        _make_skill(repo / ".agents" / "skills", "deploy-app", "deploy-app", extra_body="local\n")
        # Root-level single-skill repo inside warehouse
        warehouse = self.base / "warehouse"
        _make_skill(warehouse / "solo-repo", "solo-repo", "solo-skill", extra_body="same\n")
        _make_skill(shared_global, "solo-skill", "solo-skill", extra_body="same\n")
        # Identical clone under different name
        _make_skill(shared_global, "clone-a", "clone-a", extra_body="identical-payload\n")
        _make_skill(shared_global, "clone-b", "clone-b", extra_body="identical-payload\n")

        # Update clone-b's SKILL.md? No, for hash match they must have identical files, so put same name mismatch?
        # Wait: SKILL.md contains `name: clone-a` vs `name: clone-b`, so those differ.
        # Test exact identical hash by writing folder name clone-copy with `name: clone-copy` vs no-frontmatter?
        # Wait: folder mismatch gives two entries with same dir_name across roots:
        _make_skill(self.home / ".claude" / "skills", "solo-skill", "solo-renamed", extra_body="other\n")

        report = revise_skills.run_revision(
            scope="all",
            cwd=nested_cwd,
            home=self.home,
            source_roots=[warehouse],
            usage_mode="off",
        )
        statuses = {g["name"]: g["status"] for g in report["triage"]["duplicates"]["by_name"]}
        self.assertEqual(statuses["deploy-app"], "local-shadows-global-divergent")
        dir_mismatches = {m["dir_name"] for m in report["triage"]["duplicates"]["by_dir_mismatch"]}
        self.assertIn("solo-skill", dir_mismatches)

    def test_startup_context_budget_flags_truncation_and_totals(self):
        claude = self.home / ".claude" / "skills"
        _make_skill(claude, "long-desc", "long-desc", desc="Use when " + ("x" * 1600))
        report = revise_skills.run_revision(
            scope="global",
            cwd=self.base,
            home=self.home,
            agents_filter=["claude-code"],
            usage_mode="off",
        )
        cb = report["context_budgets"]["claude-code"]
        self.assertEqual(cb["skill_count"], 1)
        self.assertGreater(cb["total_chars"], 1600)
        self.assertTrue(any("1536" in w for w in cb["warnings"]))


class SyncAndUndoTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.base = Path(self._tmp.name)
        self.home = self.base / "home"
        self.home.mkdir()

    def test_dry_run_apply_and_undo_roundtrip(self):
        warehouse = self.base / "warehouse"
        canon = _make_skill(warehouse / "my-repo" / "skills", "good-skill", "good-skill", extra_body="same\n")

        shared = self.home / ".agents" / "skills"
        agy = self.home / ".gemini" / "config" / "skills"
        claude = self.home / ".claude" / "skills"
        shared.mkdir(parents=True)
        agy.mkdir(parents=True)
        claude.mkdir(parents=True)

        # Good skill in shared + 2-hop chained link in agy + byte-identical copy in claude
        (shared / "good-skill").symlink_to(canon, target_is_directory=True)
        (agy / "good-skill").symlink_to("../../../.agents/skills/good-skill", target_is_directory=True)
        _make_skill(claude, "good-skill", "good-skill", extra_body="same\n")

        # Broken link + ghost dir + lockfile orphan
        (agy / "dead-skill").symlink_to("/nonexistent/dead-skill", target_is_directory=True)
        (shared / "zombie-dir" / "scripts").mkdir(parents=True)
        lockfile = self.home / ".agents" / ".skill-lock.json"
        lockfile.write_text(
            json.dumps({"version": 3, "skills": {"good-skill": {"source": "a/b"}, "dead-skill": {"source": "x/y"}}}),
            encoding="utf-8",
        )

        # 1. Dry-run staged plan mutates nothing
        plan = sync_skills.build_plan(
            home=self.home,
            cwd=self.base,
            prune_broken=True,
            collapse_hops=True,
            converge_replicas=True,
            sync_agents=["qwen-code"],
            source_roots=[warehouse],
        )
        self.assertEqual(plan["state"], "staged")
        self.assertTrue((agy / "dead-skill").is_symlink())
        self.assertTrue((shared / "zombie-dir").is_dir())
        self.assertFalse((claude / "good-skill").is_symlink())

        # 2. Apply with quarantine
        trash = self.base / "trash"
        res = sync_skills.apply_plan(plan, home=self.home, trash_root=trash)
        self.assertEqual(res["state"], "done")
        self.assertFalse((agy / "dead-skill").is_symlink())
        self.assertFalse((shared / "zombie-dir").exists())
        # 2-hop relative link collapsed to direct 1-hop canonical target
        self.assertEqual(Path(os.readlink(agy / "good-skill")), canon.resolve())
        # Identical replica converted to 1-hop symlink
        self.assertTrue((claude / "good-skill").is_symlink())
        self.assertEqual((claude / "good-skill").resolve(), canon.resolve())
        # Synced to qwen-code
        self.assertEqual((self.home / ".qwen" / "skills" / "good-skill").resolve(), canon.resolve())
        # Lockfile cleaned cleanly
        cleaned_lock = json.loads(lockfile.read_text(encoding="utf-8"))
        self.assertEqual(list(cleaned_lock["skills"].keys()), ["good-skill"])

        # 3. Full --undo restores exact prior state!
        undo_res = sync_skills.undo_transaction(res["tx_id"], home=self.home, trash_root=trash)
        self.assertEqual(undo_res["state"], "done")
        self.assertTrue((agy / "dead-skill").is_symlink())
        self.assertEqual(os.readlink(agy / "dead-skill"), "/nonexistent/dead-skill")
        self.assertEqual(os.readlink(agy / "good-skill"), "../../../.agents/skills/good-skill")
        self.assertTrue((shared / "zombie-dir" / "scripts").is_dir())
        self.assertTrue((claude / "good-skill").is_dir() and not (claude / "good-skill").is_symlink())
        self.assertFalse((self.home / ".qwen" / "skills" / "good-skill").is_symlink())
        restored_lock = json.loads(lockfile.read_text(encoding="utf-8"))
        self.assertIn("dead-skill", restored_lock["skills"])

    def test_divergent_copies_are_never_overwritten(self):
        shared = self.home / ".agents" / "skills"
        claude = self.home / ".claude" / "skills"
        _make_skill(shared, "diff-skill", "diff-skill", extra_body="version A\n")
        _make_skill(claude, "diff-skill", "diff-skill", extra_body="version B\n")

        plan = sync_skills.build_plan(home=self.home, cwd=self.base, converge_replicas=True)
        self.assertEqual(plan["op_count"], 0)
        self.assertTrue(any("divergent" in sk["reason"].lower() for sk in plan["skipped"]))


class UsageTelemetryTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.base = Path(self._tmp.name)
        self.home = self.base / "home"
        self.home.mkdir()

    def test_fast_usage_reads_history_and_porch_index_ro(self):
        claude_dir = self.home / ".claude"
        claude_dir.mkdir(parents=True)
        (claude_dir / "history.jsonl").write_text(
            json.dumps({"display": "/alpha-skill please run", "timestamp": 1795000000000, "sessionId": "s1"}) + "\n",
            encoding="utf-8",
        )
        codex_dir = self.home / ".codex"
        codex_dir.mkdir(parents=True)
        (codex_dir / "history.jsonl").write_text(
            json.dumps({"session_id": "c1", "ts": 1795000100, "text": "Use $beta-skill now"}) + "\n",
            encoding="utf-8",
        )
        idx_dir = self.home / ".cache" / "pragmatic-orchestration" / "sessions-index"
        idx_dir.mkdir(parents=True)
        idx_db = idx_dir / "index-v1.sqlite"
        conn = sqlite3.connect(idx_db)
        conn.execute("CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT)")
        conn.execute("CREATE TABLE sessions (session_key TEXT PRIMARY KEY, harness TEXT, native_id TEXT)")
        conn.execute("CREATE TABLE docs (doc_id INTEGER PRIMARY KEY, session_key TEXT, kind TEXT, ts TEXT, text TEXT)")
        conn.execute("INSERT INTO meta VALUES ('last_sync_coverage', '{\"complete\": false}')")
        conn.execute("INSERT INTO sessions VALUES ('claude-code:s1', 'claude-code', 's1')")
        conn.execute("INSERT INTO docs VALUES (1, 'claude-code:s1', 'prompt', '1795000000000', '/alpha-skill please run')")
        conn.execute("INSERT INTO sessions VALUES ('agy:a1', 'agy', 'a1')")
        conn.execute("INSERT INTO docs VALUES (2, 'agy:a1', 'prompt', '1795000200', '/gamma-skill check')")
        conn.commit()
        conn.close()

        with patch.object(skill_usage, "resolve_porch_index_db", return_value=idx_db):
            res = skill_usage.collect_usage_fast({"alpha-skill", "beta-skill", "gamma-skill"}, home=self.home)

        # Deduplicated s1 across claude history.jsonl and index-v1.sqlite -> 1 session!
        self.assertEqual(res["skills"]["alpha-skill"]["total_sessions"], 1)
        self.assertEqual(res["skills"]["beta-skill"]["total_sessions"], 1)
        self.assertEqual(res["skills"]["gamma-skill"]["total_sessions"], 1)
        self.assertFalse(res["coverage"]["complete"])

    def test_deep_usage_filters_bulk_audit_sessions_and_caches(self):
        proj = self.home / ".claude" / "projects" / "repo1"
        proj.mkdir(parents=True)
        # Session s-normal invokes Skill alpha twice and reads SKILL.md twice -> counts as 1 session!
        (proj / "normal.jsonl").write_text(
            "\n".join([
                json.dumps({"type": "user", "sessionId": "s-normal", "timestamp": "2026-11-25T10:00:00Z", "message": {"content": "/alpha-skill go"}}),
                json.dumps({"type": "assistant", "sessionId": "s-normal", "timestamp": "2026-11-25T10:00:05Z", "message": {"content": [{"type": "tool_use", "name": "Skill", "input": {"skill": "alpha-skill"}}]}}),
                json.dumps({"type": "assistant", "sessionId": "s-normal", "timestamp": "2026-11-25T10:00:10Z", "message": {"content": [{"type": "tool_use", "name": "Read", "input": {"file_path": "/skills/alpha-skill/SKILL.md"}}]}}),
            ]) + "\n",
            encoding="utf-8",
        )
        # Session s-audit reads 10 distinct SKILL.md files -> excluded by bulk-audit filter!
        skill_names = {f"s{i}" for i in range(10)} | {"alpha-skill"}
        audit_lines = [
            json.dumps({
                "type": "assistant",
                "sessionId": "s-audit",
                "timestamp": "2026-11-25T11:00:00Z",
                "message": {"content": [{"type": "tool_use", "name": "Read", "input": {"file_path": f"/skills/s{i}/SKILL.md"}}]},
            })
            for i in range(10)
        ]
        (proj / "audit.jsonl").write_text("\n".join(audit_lines) + "\n", encoding="utf-8")

        cache_file = self.base / "usage-cache.json"
        since_ts = skill_usage.parse_since("2026-11-20")
        res1 = skill_usage.collect_usage_deep(skill_names, since_ts=since_ts, home=self.home, cache_path=cache_file)
        self.assertEqual(res1["skills"]["alpha-skill"]["total_sessions"], 1)
        self.assertEqual(res1["skills"]["s0"]["total_sessions"], 0)
        self.assertEqual(res1["coverage"]["filtered_audit_sessions"], 1)
        self.assertEqual(res1["coverage"]["files_parsed"], 2)

        # Second run hits cache cleanly
        res2 = skill_usage.collect_usage_deep(skill_names, since_ts=since_ts, home=self.home, cache_path=cache_file)
        self.assertEqual(res2["coverage"]["files_parsed"], 0)
        self.assertEqual(res2["coverage"]["cache_hits"], 2)

    def test_matrix_pool_renders_shrd_for_shared_readers_and_omits_uninstalled_omp(self):
        shared = self.home / ".agents" / "skills"
        _make_skill(shared, "shared-only", "shared-only")
        (self.home / ".codex").mkdir(parents=True)
        (self.home / ".grok").mkdir(parents=True)
        (self.home / ".config" / "devin").mkdir(parents=True)
        report = revise_skills.run_revision(scope="global", cwd=self.base, home=self.home, usage_mode="off")
        col_ids = [c["id"] for c in report["matrix"]["columns"]]
        self.assertIn("shared", col_ids)
        self.assertIn("grok", col_ids)
        self.assertIn("devin", col_ids)
        self.assertNotIn("omp", col_ids)
        row = next(r for r in report["matrix"]["rows"] if r["name"] == "shared-only")
        self.assertEqual(row["cells"]["shared"], "copy")
        self.assertEqual(row["cells"]["grok"], "shrd")
        self.assertEqual(row["cells"]["devin"], "shrd")

    def test_deep_usage_caches_devin_tool_call_state_and_opencode_sessions(self):
        devin_dir = self.home / ".local" / "share" / "devin" / "cli"
        devin_dir.mkdir(parents=True)
        dconn = sqlite3.connect(devin_dir / "sessions.db")
        dconn.execute("CREATE TABLE sessions (id TEXT PRIMARY KEY, last_activity_at INTEGER)")
        dconn.execute("CREATE TABLE prompt_history (id INTEGER PRIMARY KEY, content TEXT, timestamp INTEGER, session_id TEXT)")
        dconn.execute("CREATE TABLE tool_call_state (session_id TEXT, tool_call_id TEXT, tool_call_json TEXT)")
        now = int(__import__("time").time())
        dconn.execute("INSERT INTO sessions VALUES ('d1', ?)", (now,))
        dconn.execute("INSERT INTO tool_call_state VALUES ('d1', 'tc1', '{\"path\": \"/x/skills/alpha-skill/SKILL.md\"}')")
        dconn.commit()
        dconn.close()

        oc_dir = self.home / ".local" / "share" / "opencode"
        oc_dir.mkdir(parents=True)
        oconn = sqlite3.connect(oc_dir / "opencode.db")
        oconn.execute("CREATE TABLE session_v2 (id TEXT PRIMARY KEY, time_updated INTEGER)")
        oconn.execute("CREATE TABLE session_message (id TEXT PRIMARY KEY, session_id TEXT, type TEXT, time_created INTEGER, data TEXT)")
        now_ms = now * 1000
        oconn.execute("INSERT INTO session_v2 VALUES ('o1', ?)", (now_ms,))
        oconn.execute("INSERT INTO session_message VALUES ('m1', 'o1', 'skill', ?, '{\"name\": \"beta-skill\"}')", (now_ms,))
        oconn.commit()
        oconn.close()

        cache_file = self.base / "db-cache.json"
        since_ts = now - 3600
        res1 = skill_usage.collect_usage_deep({"alpha-skill", "beta-skill"}, since_ts=since_ts, home=self.home, cache_path=cache_file)
        self.assertEqual(res1["skills"]["alpha-skill"]["total_sessions"], 1)
        self.assertEqual(res1["skills"]["beta-skill"]["total_sessions"], 1)
        self.assertEqual(res1["coverage"]["cache_hits"], 0)

        res2 = skill_usage.collect_usage_deep({"alpha-skill", "beta-skill"}, since_ts=since_ts, home=self.home, cache_path=cache_file)
        self.assertEqual(res2["skills"]["alpha-skill"]["total_sessions"], 1)
        self.assertEqual(res2["skills"]["beta-skill"]["total_sessions"], 1)
        self.assertEqual(res2["coverage"]["cache_hits"], 2)


class ClaudeSyncedAndStaleAgentTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.base = Path(self._tmp.name)
        self.home = self.base / "home"
        self.home.mkdir()
        self.apps = self.base / "Apps"
        self.apps.mkdir()
        self.exts = self.base / "Exts"
        self.exts.mkdir()

    def test_claude_synced_dir_is_not_flagged_as_ghost_or_pruned(self):
        claude = self.home / ".claude" / "skills"
        synced = claude / "synced"
        (synced / ".bucket-org_user").mkdir(parents=True)
        _make_skill(synced / "org_user", "pdf", "pdf")
        (synced / "org_user" / "manifest.json").write_text("{}", encoding="utf-8")

        report = revise_skills.run_revision(
            scope="global",
            cwd=self.base,
            home=self.home,
            usage_mode="off",
            which_fn=lambda b: "/usr/local/bin/claude" if b == "claude" else None,
            app_dirs=[self.apps],
            extension_dirs=[self.exts],
        )
        self.assertEqual(report["summary"]["ghost_dirs"], 0)

        plan = sync_skills.build_plan(home=self.home, cwd=self.base, prune_broken=True)
        self.assertEqual(plan["op_count"], 0)
        self.assertTrue((synced / "org_user" / "manifest.json").is_file())

        # An actual skill named `synced` (with SKILL.md directly inside) IS scanned normally.
        _make_skill(claude, "synced", "synced")
        report2 = revise_skills.run_revision(
            scope="global",
            cwd=self.base,
            home=self.home,
            usage_mode="off",
            which_fn=lambda b: "/usr/local/bin/claude" if b == "claude" else None,
            app_dirs=[self.apps],
            extension_dirs=[self.exts],
        )
        names = {r["name"] for r in report2["matrix"]["rows"]}
        self.assertIn("synced", names)

    def test_stale_agent_detection_classifies_active_stub_orphan_and_antigravity_only_gemini(self):
        # Active claude-code (bin: claude)
        _make_skill(self.home / ".claude" / "skills", "s1", "s1")
        # Cursor with NO binary, only bare "agent" in PATH (must NOT mark cursor active!)
        (self.home / ".cursor").mkdir(parents=True)
        # Windsurf alive via Devin.app + ~/.codeium/windsurf
        (self.home / ".codeium" / "windsurf" / "skills").mkdir(parents=True)
        (self.apps / "Devin.app").mkdir()
        # Antigravity active via Antigravity.app + ~/.gemini/antigravity & config
        (self.apps / "Antigravity.app").mkdir()
        (self.home / ".gemini" / "antigravity").mkdir(parents=True)
        (self.home / ".gemini" / "config").mkdir(parents=True)
        # Mux skills-only stub
        (self.home / ".mux" / "skills").mkdir(parents=True)
        # Augment orphaned-agent (extra residual file + skills/)
        (self.home / ".augment" / "skills").mkdir(parents=True)
        (self.home / ".augment" / "auggie-path").write_text("/opt/homebrew/bin/auggie", encoding="utf-8")

        def fake_which_no_cursor(bin_name: str) -> str | None:
            if bin_name == "claude":
                return "/usr/local/bin/claude"
            if bin_name == "agent":  # Grok collision binary; cursor must ignore it!
                return "/usr/local/bin/agent"
            return None

        health = agents.inspect_agent_installations(
            ["claude-code", "cursor", "windsurf", "antigravity", "gemini-cli", "mux", "augment", "omp"],
            cwd=self.base,
            home=self.home,
            which_fn=fake_which_no_cursor,
            app_dirs=[self.apps],
            extension_dirs=[self.exts],
        )
        self.assertEqual(health["claude-code"]["status"], "active")
        self.assertEqual(health["cursor"]["status"], "orphaned-agent")
        self.assertEqual(health["windsurf"]["status"], "active")
        self.assertEqual(health["antigravity"]["status"], "active")
        self.assertEqual(health["gemini-cli"]["status"], "shared-parent-only")
        self.assertEqual(health["mux"]["status"], "skills-only-stub")
        self.assertEqual(health["augment"]["status"], "orphaned-agent")
        self.assertEqual(health["omp"]["status"], "not-installed")

        # Now add cursor-agent -> cursor becomes active
        health_cur = agents.inspect_agent_installations(
            ["cursor"],
            cwd=self.base,
            home=self.home,
            which_fn=lambda b: "/usr/local/bin/cursor-agent" if b == "cursor-agent" else None,
            app_dirs=[self.apps],
            extension_dirs=[self.exts],
        )
        self.assertEqual(health_cur["cursor"]["status"], "active")

        # Add ~/.gemini/skills -> gemini-cli becomes orphaned-agent, but ~/.gemini/skills is protected by antigravity!
        (self.home / ".gemini" / "skills").mkdir(parents=True)
        (self.home / ".zencoder" / "skills").mkdir(parents=True)
        report = revise_skills.run_revision(
            scope="global",
            cwd=self.base,
            home=self.home,
            usage_mode="off",
            which_fn=fake_which_no_cursor,
            app_dirs=[self.apps],
            extension_dirs=[self.exts],
        )
        stale_by_id = {s["agent_id"]: s for s in report["triage"]["stale_agents"]}
        self.assertIn("gemini-cli", stale_by_id)
        self.assertEqual(stale_by_id["gemini-cli"]["prunable_paths"], [])
        self.assertTrue(
            any(pp["path"].endswith("/.gemini/skills") and "antigravity" in pp["active_readers"]
                for pp in stale_by_id["gemini-cli"]["protected_paths"])
        )
        self.assertIn("zencoder", stale_by_id)
        self.assertIn("zenflow", stale_by_id)

    def test_prune_stale_agents_quarantine_dedup_no_overlap_and_undo_roundtrip(self):
        shared = self.home / ".agents" / "skills"
        _make_skill(shared, "live-shared", "live-shared")

        # Active antigravity + ~/.gemini/skills shared with gemini-cli
        (self.apps / "Antigravity.app").mkdir()
        (self.home / ".gemini" / "antigravity").mkdir(parents=True)
        (self.home / ".gemini" / "config" / "skills").mkdir(parents=True)
        _make_skill(self.home / ".gemini" / "skills", "gem-skill", "gem-skill")

        # Mux stub with broken symlink inside
        (self.home / ".mux" / "skills").mkdir(parents=True)
        (self.home / ".mux" / "skills" / "dead-mux").symlink_to("/nonexistent/dead-mux", target_is_directory=True)

        # Augment orphan with non-skill file + broken symlink inside skills/
        (self.home / ".augment" / "skills").mkdir(parents=True)
        (self.home / ".augment" / "auggie-path").write_text("/opt/homebrew/bin/auggie", encoding="utf-8")
        (self.home / ".augment" / "skills" / "dead-aug").symlink_to("/nonexistent/dead-aug", target_is_directory=True)

        # Zencoder + Zenflow sharing ~/.zencoder/skills
        (self.home / ".zencoder" / "cache").mkdir(parents=True)
        (self.home / ".zencoder" / "skills").mkdir(parents=True)
        (self.home / ".zencoder" / "skills" / "dead-zen").symlink_to("/nonexistent/dead-zen", target_is_directory=True)

        # Standalone broken link in shared ~/.agents/skills (should still be pruned cleanly)
        (shared / "dead-shared").symlink_to("/nonexistent/dead-shared", target_is_directory=True)

        plan = sync_skills.build_plan(
            home=self.home,
            cwd=self.base,
            prune_stale_agents=True,
            prune_broken=True,
            which_fn=lambda b: None,
            app_dirs=[self.apps],
            extension_dirs=[self.exts],
        )

        op_paths = [op.get("path") for op in plan["ops"]]
        self.assertIn(str((self.home / ".mux").absolute()), op_paths)
        self.assertIn(str((self.home / ".augment" / "skills").absolute()), op_paths)
        self.assertEqual(op_paths.count(str((self.home / ".zencoder" / "skills").absolute())), 1)
        # Broken links inside quarantined roots MUST NOT have separate remove_symlink ops
        self.assertNotIn(str((self.home / ".mux" / "skills" / "dead-mux").absolute()), op_paths)
        self.assertNotIn(str((self.home / ".augment" / "skills" / "dead-aug").absolute()), op_paths)
        self.assertNotIn(str((self.home / ".zencoder" / "skills" / "dead-zen").absolute()), op_paths)
        # Broken link in active shared dir IS still pruned
        self.assertIn(str((shared / "dead-shared").absolute()), op_paths)
        # ~/.gemini/skills & ~/.agents/skills NEVER pruned
        self.assertNotIn(str((self.home / ".gemini" / "skills").absolute()), op_paths)
        self.assertNotIn(str(shared.absolute()), op_paths)
        self.assertTrue(any("antigravity" in sk["reason"] for sk in plan["skipped"]))

        trash = self.base / "trash"
        res = sync_skills.apply_plan(plan, home=self.home, trash_root=trash)
        self.assertEqual(res["state"], "done")
        self.assertFalse((self.home / ".mux").exists())
        self.assertFalse((self.home / ".augment" / "skills").exists())
        self.assertTrue((self.home / ".augment" / "auggie-path").is_file())
        self.assertFalse((self.home / ".zencoder" / "skills").exists())
        self.assertTrue((self.home / ".zencoder" / "cache").is_dir())
        self.assertTrue((self.home / ".gemini" / "skills" / "gem-skill" / "SKILL.md").is_file())
        self.assertFalse((shared / "dead-shared").is_symlink())

        undo_res = sync_skills.undo_transaction(res["tx_id"], home=self.home, trash_root=trash)
        self.assertEqual(undo_res["state"], "done")
        self.assertTrue((self.home / ".mux" / "skills" / "dead-mux").is_symlink())
        self.assertTrue((self.home / ".augment" / "skills" / "dead-aug").is_symlink())
        self.assertTrue((self.home / ".zencoder" / "skills" / "dead-zen").is_symlink())
        self.assertTrue((shared / "dead-shared").is_symlink())

    def test_sync_agents_excludes_bundled_honors_from_agents_and_avoids_dir_name_dups(self):
        shared = self.home / ".agents" / "skills"
        agy = self.home / ".gemini" / "config" / "skills"
        claude = self.home / ".claude" / "skills"
        hermes = self.home / ".hermes" / "skills"
        goose = self.home / ".config" / "goose" / "skills"
        shared.mkdir(parents=True)
        agy.mkdir(parents=True)
        claude.mkdir(parents=True)

        # Hermes bundled skill (must NEVER leak into antigravity)
        _make_skill(hermes / "apple", "apple-notes", "apple-notes")
        (hermes / ".bundled_manifest").write_text("apple/apple-notes: deadbeef\n", encoding="utf-8")
        # Legacy goose-only skill (must NOT sync when from_agents ignores goose)
        _make_skill(goose, "legacy-goose", "legacy-goose")
        # Shared skill whose frontmatter `name` has spaces/caps different from folder `dir_name`
        _make_skill(shared, "semantic-scholar-lookup", "Semantic Scholar Lookup")
        # Claude-only and Antigravity-only skills
        _make_skill(claude, "claude-only", "claude-only")
        _make_skill(agy, "agy-only", "agy-only")

        plan = sync_skills.build_plan(
            home=self.home,
            cwd=self.base,
            sync_agents=["antigravity", "agy"],
            from_agents=["codex", "claude-code", "antigravity"],
        )
        op_paths = [op["path"] for op in plan["ops"]]
        self.assertNotIn(str((agy / "apple-notes").absolute()), op_paths)
        self.assertNotIn(str((agy / "legacy-goose").absolute()), op_paths)
        self.assertNotIn(str((shared / "Semantic Scholar Lookup").absolute()), op_paths)
        self.assertIn(str((agy / "semantic-scholar-lookup").absolute()), op_paths)
        self.assertIn(str((agy / "claude-only").absolute()), op_paths)
        self.assertIn(str((shared / "claude-only").absolute()), op_paths)
        self.assertIn(str((shared / "agy-only").absolute()), op_paths)


if __name__ == "__main__":
    unittest.main()
