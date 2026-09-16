"""Offline tests for lib/sessions.py — synthetic fixtures only, no real user data."""
from __future__ import annotations

import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

LIB = Path(__file__).resolve().parents[1] / "lib"
sys.path.insert(0, str(LIB))
import sessions  # noqa: E402


def write_jsonl(path: Path, records: list) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for rec in records:
            if isinstance(rec, str):  # raw line, e.g. malformed
                fh.write(rec + "\n")
            else:
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return path


def write_json(path: Path, obj) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")
    return path


class FixtureMixin:
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="consilium sessions ")
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)


class ClaudeCodeTests(FixtureMixin, unittest.TestCase):
    def make(self):
        proj = self.root / "claude" / "-Users-x-proj"
        sid = "11111111-2222-3333-4444-555555555555"
        write_jsonl(proj / f"{sid}.jsonl", [
            {"type": "summary", "summary": "Fix the flaky test", "timestamp": "2026-01-01T10:00:00Z"},
            {"type": "user", "timestamp": "2026-01-01T10:00:01Z", "cwd": "/Users/x/proj",
             "sessionId": sid, "uuid": "u1", "origin": {"kind": "human"},
             "message": {"role": "user", "content": "why is the test flaky?"}},
            {"type": "assistant", "timestamp": "2026-01-01T10:00:02Z", "sessionId": sid, "uuid": "a1",
             "message": {"role": "assistant", "model": "claude-opus-5", "id": "msg_1",
                         "content": [{"type": "thinking", "thinking": "hmm"},
                                     {"type": "text", "text": "Race in the fixture."},
                                     {"type": "tool_use", "id": "tu1", "name": "Read", "input": {"f": "t.py"}}]}},
            {"type": "user", "timestamp": "2026-01-01T10:00:03Z", "sessionId": sid, "uuid": "u2",
             "message": {"role": "user", "content": [
                 {"type": "tool_result", "tool_use_id": "tu1", "content": "file body"}]}},
            {"type": "user", "timestamp": "2026-01-01T10:00:04Z", "sessionId": sid, "uuid": "u3",
             "isMeta": True,
             "message": {"role": "user", "content": "<command-name>/clear</command-name>"}},
        ])
        write_jsonl(proj / "subagents" / "agent-abc.jsonl", [
            {"type": "user", "timestamp": "2026-01-01T10:01:00Z", "sessionId": "sub-1",
             "isSidechain": True, "agentId": "abc", "promptId": "p1",
             "message": {"role": "user", "content": "subagent task"}},
        ])
        return self.root / "claude"

    def test_sessions_and_fragments(self):
        root = self.make()
        store = sessions.Store("claude-code", ".claude/projects", root, "jsonl_dir")
        refs = list(sessions.claude_iter_sessions(store))
        self.assertEqual(len(refs), 2)
        main = next(r for r in refs if "subagents" not in r.session_id)
        sub = next(r for r in refs if "subagents" in r.session_id)
        self.assertEqual(main.title, "Fix the flaky test")
        self.assertEqual(main.cwd, "/Users/x/proj")
        self.assertEqual(main.models, ["claude-opus-5"])
        self.assertTrue(sub.parent)
        self.assertEqual(sub.agent, "agent-abc")

        stats: dict[str, int] = {}
        out = list(sessions.claude_iter_fragments(store, main, 400, stats))
        by_kind = {}
        for f in out:
            by_kind.setdefault(f["kind"], []).append(f)
        prompts = by_kind["prompt"]
        self.assertEqual(len(prompts), 1)
        self.assertEqual(prompts[0]["authorship"], "human")
        self.assertEqual(prompts[0]["text"], "why is the test flaky?")
        self.assertEqual(by_kind["tool_result"][0]["authorship"], "system")
        self.assertEqual(by_kind["reasoning"][0]["text"], "hmm")
        self.assertEqual(by_kind["tool_call"][0]["rel"]["tool"], "Read")
        # isMeta command record → context, not prompt
        self.assertTrue(any(f["kind"] == "context" for f in out))
        self.assertTrue(all("line" in f["locator"] for f in out))


class CodexTests(FixtureMixin, unittest.TestCase):
    def make(self):
        sid = "99999999-8888-7777-6666-555555555555"
        path = self.root / "codex" / "2026" / "01" / "02" / f"rollout-2026-01-02T00-00-00-{sid}.jsonl"
        write_jsonl(path, [
            {"timestamp": "2026-01-02T00:00:00Z", "type": "session_meta",
             "payload": {"id": sid, "cwd": "/work/repo", "originator": "Codex Desktop",
                         "cli_version": "0.1", "model_provider": "openai"}},
            {"timestamp": "2026-01-02T00:00:01Z", "type": "turn_context",
             "payload": {"turn_id": "t1", "model": "gpt-6-astra", "effort": "high"}},
            {"timestamp": "2026-01-02T00:00:02Z", "type": "response_item",
             "payload": {"type": "message", "role": "user", "id": "i1",
                         "content": [{"type": "input_text", "text": "<environment_context>cwd=/work/repo</environment_context>"}]}},
            {"timestamp": "2026-01-02T00:00:03Z", "type": "event_msg",
             "payload": {"type": "user_message", "turn_id": "t1", "message": "add a retry loop"}},
            {"timestamp": "2026-01-02T00:00:04Z", "type": "response_item",
             "payload": {"type": "message", "role": "user", "id": "i2",
                         "content": [{"type": "input_text", "text": "add a retry loop"}]}},
            {"timestamp": "2026-01-02T00:00:05Z", "type": "response_item",
             "payload": {"type": "reasoning", "id": "r1", "summary": [{"text": "planning"}]}},
            {"timestamp": "2026-01-02T00:00:06Z", "type": "response_item",
             "payload": {"type": "function_call", "name": "shell", "call_id": "c1", "arguments": "{}"}},
            {"timestamp": "2026-01-02T00:00:07Z", "type": "response_item",
             "payload": {"type": "function_call_output", "call_id": "c1", "output": "ok"}},
            {"timestamp": "2026-01-02T00:00:08Z", "type": "event_msg",
             "payload": {"type": "agent_message", "turn_id": "t1", "message": "Done.", "phase": "final"}},
            '{"timestamp": "2026-01-02T00:00:09Z", "type": "response_item", GARBAGE-BINARY-\x00\x01',
            {"timestamp": "2026-01-02T00:00:10Z", "type": "event_msg",
             "payload": {"type": "token_count", "info": {"total": 5}}},
        ])
        return self.root / "codex", sid

    def test_classification(self):
        root, sid = self.make()
        store = sessions.Store("codex", "sessions", root, "jsonl_dir")
        refs = list(sessions.codex_iter_sessions(store))
        self.assertEqual(len(refs), 1)
        ref = refs[0]
        self.assertEqual(ref.session_id, sid)
        self.assertEqual(ref.cwd, "/work/repo")
        self.assertIn("gpt-6-astra", ref.models)

        stats: dict[str, int] = {}
        out = list(sessions.codex_iter_fragments(store, ref, 400, stats))
        prompts = [f for f in out if f["kind"] == "prompt"]
        ctx = [f for f in out if f["kind"] == "context"]
        # event_msg.user_message is the authoritative prompt
        self.assertTrue(any(f["native_type"] == "event_msg.user_message" and f["text"] == "add a retry loop"
                            for f in prompts))
        # mirrored response_item user record upgrades to prompt
        self.assertTrue(any(f["native_type"] == "response_item.user" for f in prompts))
        # bootstrap environment context must NOT be a prompt
        self.assertTrue(any("environment_context" in (f.get("text") or "") for f in ctx))
        self.assertTrue(any(f["kind"] == "tool_call" for f in out))
        self.assertTrue(any(f["kind"] == "tool_result" for f in out))
        self.assertTrue(any(f["kind"] == "reasoning" for f in out))
        # malformed interior line counted, not dropped silently
        self.assertEqual(stats.get("malformed"), 1)


class OpenCodeDbTests(FixtureMixin, unittest.TestCase):
    def make(self):
        db = self.root / "opencode.db"
        conn = sqlite3.connect(db)
        conn.executescript("""
            CREATE TABLE project (id TEXT PRIMARY KEY, worktree TEXT);
            CREATE TABLE session (id TEXT PRIMARY KEY, project_id TEXT, parent_id TEXT,
                directory TEXT, title TEXT, agent TEXT, model TEXT, version TEXT,
                time_created REAL, time_updated REAL);
            CREATE TABLE message (id TEXT PRIMARY KEY, session_id TEXT, time_created REAL, data TEXT);
            CREATE TABLE part (id TEXT PRIMARY KEY, session_id TEXT, message_id TEXT,
                time_created REAL, data TEXT);
        """)
        conn.execute("INSERT INTO project VALUES ('p1', '/work/repo')")
        conn.execute("INSERT INTO session VALUES ('ses_1', 'p1', NULL, '/work/repo', 'Fix bug', 'build', '{\"id\":\"kimi-k3\"}', '1.0', 1000, 2000)")
        conn.execute("INSERT INTO message VALUES ('msg_u1', 'ses_1', 1100, ?)",
                     (json.dumps({"id": "msg_u1", "role": "user", "path": {"cwd": "/work/repo"}}),))
        conn.execute("INSERT INTO message VALUES ('msg_a1', 'ses_1', 1200, ?)",
                     (json.dumps({"id": "msg_a1", "role": "assistant", "finish": "stop",
                                  "modelID": "kimi-k3", "providerID": "opencode"}),))
        conn.execute("INSERT INTO part VALUES ('prt_u1', 'ses_1', 'msg_u1', 1101, ?)",
                     (json.dumps({"type": "text", "text": "please fix the bug"}),))
        conn.execute("INSERT INTO part VALUES ('prt_a1', 'ses_1', 'msg_a1', 1201, ?)",
                     (json.dumps({"type": "text", "text": "Fixed it."}),))
        conn.execute("INSERT INTO part VALUES ('prt_a2', 'ses_1', 'msg_a1', 1202, ?)",
                     (json.dumps({"type": "tool", "tool": "bash", "callID": "c1",
                                  "state": {"status": "completed", "input": {"cmd": "ls"}, "output": "ok"}}),))
        conn.commit()
        conn.close()
        return db

    def test_db_reader(self):
        db = self.make()
        store = sessions.Store("opencode", "db", db, "sqlite")
        refs = list(sessions.opencode_iter_sessions(store))
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0].title, "Fix bug")
        self.assertEqual(refs[0].cwd, "/work/repo")
        self.assertEqual(refs[0].models, ["kimi-k3"])

        stats: dict[str, int] = {}
        out = list(sessions.opencode_iter_fragments(store, refs[0], 400, stats))
        prompts = [f for f in out if f["kind"] == "prompt"]
        # text part inside role=user message → prompt, human
        self.assertTrue(any(f.get("text") == "please fix the bug" and f["authorship"] == "human" for f in prompts))
        self.assertTrue(any(f["kind"] == "assistant" and f["text"] == "Fixed it." for f in out))
        self.assertTrue(any(f["kind"] == "tool_call" for f in out))
        self.assertTrue(any(f["kind"] == "tool_result" for f in out))

    def test_storage_tree(self):
        base = self.root / "storage"
        write_json(base / "session" / "p1" / "ses_9.json",
                   {"id": "ses_9", "title": "T", "directory": "/w",
                    "time": {"created": 1, "updated": 2}})
        write_json(base / "message" / "ses_9" / "msg_1.json",
                   {"id": "msg_1", "role": "user", "time": {"created": 1}})
        write_json(base / "part" / "msg_1" / "prt_1.json",
                   {"type": "text", "text": "hello from storage"})
        store = sessions.Store("opencode", "storage", base, "json_dir")
        refs = list(sessions.opencode_iter_sessions(store))
        self.assertEqual(len(refs), 1)
        stats: dict[str, int] = {}
        out = list(sessions.opencode_iter_fragments(store, refs[0], 400, stats))
        self.assertTrue(any(f["kind"] == "prompt" and f.get("text") == "hello from storage" for f in out))


class GrokTests(FixtureMixin, unittest.TestCase):
    def make(self):
        sess = self.root / "grok" / "%2Fwork%2Frepo" / "sess-1"
        sess.mkdir(parents=True)
        write_json(sess / "summary.json",
                   {"info": {"id": "sess-1", "cwd": "/work/repo"},
                    "generated_title": "Investigate cache", "current_model_id": "grok-4.6",
                    "created_at": "2026-01-03T00:00:00Z", "updated_at": "2026-01-03T01:00:00Z",
                    "reasoning_effort": "high", "num_messages": 4})
        write_jsonl(sess / "chat_history.jsonl", [
            {"type": "system", "content": "you are grok"},
            {"type": "user", "content": [{"type": "text", "text": "<system-reminder>rules…</system-reminder>"}]},
            {"type": "user", "content": [{"type": "text", "text": "find the cache bug"}]},
            {"type": "reasoning", "summary": [{"text": "thinking…"}], "id": "r1"},
            {"type": "assistant", "content": "The bug is in invalidation.",
             "tool_calls": [{"id": "c1", "name": "view", "arguments": "{}"}]},
            {"type": "tool_result", "tool_call_id": "c1", "content": "file…"},
        ])
        write_jsonl(self.root / "grok" / "%2Fwork%2Frepo" / "prompt_history.jsonl", [
            {"session_id": "sess-1", "prompt": "find the cache bug"},
        ])
        return self.root / "grok"

    def test_grok(self):
        root = self.make()
        store = sessions.Store("grok", "sessions", root, "session_dirs")
        refs = list(sessions.grok_iter_sessions(store))
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0].title, "Investigate cache")
        self.assertEqual(refs[0].models, ["grok-4.6"])

        stats: dict[str, int] = {}
        out = list(sessions.grok_iter_fragments(store, refs[0], 400, stats))
        prompts = [f for f in out if f["kind"] == "prompt"]
        ctx = [f for f in out if f["kind"] == "context"]
        self.assertEqual(len(prompts), 1)
        self.assertEqual(prompts[0]["authorship"], "human")  # prompt_history match
        self.assertTrue(any("system-reminder" in (f.get("text") or "") for f in ctx))
        self.assertTrue(any(f["kind"] == "reasoning" for f in out))
        self.assertTrue(any(f["kind"] == "tool_call" for f in out))
        self.assertTrue(any(f["kind"] == "tool_result" for f in out))


class DevinTests(FixtureMixin, unittest.TestCase):
    def make(self):
        base = self.root / "devin"
        base.mkdir()
        db = base / "sessions.db"
        conn = sqlite3.connect(db)
        conn.executescript("""
            CREATE TABLE sessions (id TEXT PRIMARY KEY, working_directory TEXT, model TEXT,
                agent_mode TEXT, created_at TEXT, last_activity_at TEXT, title TEXT,
                hidden INTEGER, main_chain_id INTEGER);
            CREATE TABLE message_nodes (row_id INTEGER PRIMARY KEY, session_id TEXT,
                node_id INTEGER, parent_node_id INTEGER, chat_message TEXT, created_at TEXT);
            CREATE TABLE subagent_heads (session_id TEXT, head TEXT);
        """)
        conn.execute("INSERT INTO sessions VALUES ('test-sess', '/work/repo', 'swe-2-high', "
                     "'bypass', '2026-01-04T00:00:00Z', '2026-01-04T01:00:00Z', 'Test title', 0, 7)")
        for row_id, node, parent, msg, ts in [
            (1, 1, None, {"role": "system", "content": "sys"}, "2026-01-04T00:00:01Z"),
            (2, 2, 1, {"role": "user", "content": "do the thing", "message_id": "m1"}, "2026-01-04T00:00:02Z"),
            (3, 3, 2, {"role": "assistant", "content": "Done", "message_id": "m2",
                       "thinking": {"thinking": "hmm"},
                       "tool_calls": [{"id": "c1", "name": "run", "arguments": "{}"}],
                       "metadata": {"finish_reason": "stop"}}, "2026-01-04T00:00:03Z"),
            (4, 4, 3, {"role": "tool", "content": "output", "message_id": "m3"}, "2026-01-04T00:00:04Z"),
        ]:
            conn.execute("INSERT INTO message_nodes VALUES (?, 'test-sess', ?, ?, ?, ?)",
                         (row_id, node, parent, json.dumps(msg), ts))
        conn.execute("INSERT INTO subagent_heads VALUES ('test-sess', 'head-1')")
        conn.commit()
        conn.close()
        write_json(base / "transcripts" / "test-sess.json",
                   {"session_id": "test-sess", "agent": {"model_name": "swe-2-high"},
                    "steps": [{"step_id": "s1", "source": "user", "message": "hi",
                               "timestamp": "2026-01-04T00:00:02Z"},
                              {"step_id": "s2", "source": "agent", "message": "hello",
                               "timestamp": "2026-01-04T00:00:03Z"}]})
        return base

    def test_db_and_transcripts(self):
        base = self.make()
        store = sessions.Store("devin", "sessions.db", base / "sessions.db", "sqlite")
        refs = list(sessions.devin_iter_sessions(store))
        self.assertEqual(refs[0].title, "Test title")
        self.assertEqual(refs[0].extra["agent_mode"], "bypass")

        stats: dict[str, int] = {}
        out = list(sessions.devin_iter_fragments(store, refs[0], 400, stats))
        kinds = {f["kind"] for f in out}
        self.assertIn("prompt", kinds)
        self.assertIn("assistant", kinds)
        self.assertIn("reasoning", kinds)
        self.assertIn("tool_call", kinds)
        self.assertIn("tool_result", kinds)
        self.assertIn("context", kinds)
        self.assertTrue(any(f["native_type"] == "subagent_heads" for f in out))
        node_rel = next(f for f in out if f["kind"] == "prompt")["rel"]
        self.assertEqual(node_rel["node_id"], 2)
        self.assertEqual(node_rel["parent_node_id"], 1)

        tstore = sessions.Store("devin", "transcripts", base / "transcripts", "json_dir")
        trefs = list(sessions.devin_iter_sessions(tstore))
        self.assertEqual(trefs[0].models, ["swe-2-high"])
        tout = list(sessions.devin_iter_fragments(tstore, trefs[0], 400, {}))
        self.assertEqual([f["kind"] for f in tout], ["prompt", "assistant"])


class GeminiTests(FixtureMixin, unittest.TestCase):
    def test_chat(self):
        base = self.root / "gemini"
        write_json(base / "projects.json", {"projects": {"/work/repo": "abc123"}})
        write_json(base / "tmp" / "abc123" / "chats" / "session-2026-01-05T00-00-deadbeef.json", {
            "sessionId": "deadbeef-1234", "startTime": "2026-01-05T00:00:00Z",
            "lastUpdated": "2026-01-05T00:10:00Z",
            "messages": [
                {"type": "user", "id": "m1", "content": "explain auth", "timestamp": "2026-01-05T00:00:01Z"},
                {"type": "gemini", "id": "m2", "content": "Auth works via…", "model": "gemini-3",
                 "timestamp": "2026-01-05T00:00:02Z",
                 "toolCalls": [{"name": "read", "args": {}}]},
                {"type": "info", "id": "m3", "content": "checkpoint", "timestamp": "2026-01-05T00:00:03Z"},
            ]})
        store = sessions.Store("gemini", "chats", base / "tmp", "json_dir")
        refs = list(sessions.gemini_iter_sessions(store))
        self.assertEqual(refs[0].cwd, "/work/repo")  # resolved via projects.json
        stats: dict[str, int] = {}
        out = list(sessions.gemini_iter_fragments(store, refs[0], 400, stats))
        kinds = [f["kind"] for f in out]
        self.assertEqual(kinds, ["prompt", "assistant", "tool_call", "metadata"])


class CursorTests(FixtureMixin, unittest.TestCase):
    def test_vscdb(self):
        wsdir = self.root / "ws" / "deadbeef"
        wsdir.mkdir(parents=True)
        write_json(wsdir / "workspace.json", {"folder": "file:///work/repo"})
        db = wsdir / "state.vscdb"
        conn = sqlite3.connect(db)
        conn.execute("CREATE TABLE cursorDiskKV (key TEXT PRIMARY KEY, value TEXT)")
        conn.execute("INSERT INTO cursorDiskKV VALUES ('composerData:cid1', ?)",
                     (json.dumps({"name": "Cursor chat", "createdAt": "2026-01-06T00:00:00Z",
                                  "lastUpdatedAt": "2026-01-06T01:00:00Z",
                                  "fullConversationHeadersOnly": [{"bubbleId": "b1", "type": 1},
                                                                  {"bubbleId": "b2", "type": 2}]}),))
        conn.execute("INSERT INTO cursorDiskKV VALUES ('bubbleId:cid1:b1', ?)",
                     (json.dumps({"text": "cursor question"}),))
        conn.execute("INSERT INTO cursorDiskKV VALUES ('bubbleId:cid1:b2', ?)",
                     (json.dumps({"text": "cursor answer"}),))
        conn.commit()
        conn.close()
        store = sessions.Store("cursor", "workspace:deadbeef", db, "sqlite")
        refs = list(sessions.cursor_iter_sessions(store))
        self.assertEqual(refs[0].title, "Cursor chat")
        self.assertEqual(refs[0].cwd, "/work/repo")  # workspace.json fallback
        stats: dict[str, int] = {}
        out = list(sessions.cursor_iter_fragments(store, refs[0], 400, stats))
        self.assertEqual(out[0]["kind"], "prompt")
        self.assertEqual(out[0]["authorship"], "human")
        self.assertEqual(out[1]["kind"], "assistant")


class CodexIndexTests(FixtureMixin, unittest.TestCase):
    """Codex App/Desktop layers: state index, UI catalog, summaries, history."""

    def make(self):
        home = self.root / "codex_home"
        sid = "aaaaaaaa-1111-2222-3333-444444444444"
        child = "bbbbbbbb-1111-2222-3333-444444444444"
        # canonical rollout for the parent thread
        write_jsonl(home / "sessions" / "2026" / "01" / "02"
                    / f"rollout-2026-01-02T00-00-00-{sid}.jsonl", [
            {"timestamp": "2026-01-02T00:00:00Z", "type": "session_meta",
             "payload": {"id": sid, "cwd": "/work/repo"}},
            {"timestamp": "2026-01-02T00:00:01Z", "type": "event_msg",
             "payload": {"type": "user_message", "turn_id": "t1", "message": "real prompt"}},
        ])
        db = home / "state_5.sqlite"
        conn = sqlite3.connect(db)
        conn.executescript("""
            CREATE TABLE threads (id TEXT PRIMARY KEY, rollout_path TEXT, created_at TEXT,
                updated_at_ms TEXT, source TEXT, model_provider TEXT, cwd TEXT, title TEXT,
                sandbox_policy TEXT, approval_mode TEXT, tokens_used INTEGER,
                has_user_event INTEGER, archived INTEGER, git_sha TEXT, git_branch TEXT,
                git_origin_url TEXT, first_user_message TEXT, agent_nickname TEXT,
                agent_role TEXT, reasoning_effort TEXT, agent_path TEXT, thread_source TEXT,
                preview TEXT, history_mode TEXT, name TEXT, project_id TEXT, originator TEXT,
                model TEXT);
            CREATE TABLE thread_spawn_edges (parent_thread_id TEXT, child_thread_id TEXT PRIMARY KEY,
                status TEXT);
        """)
        conn.execute(
            "INSERT INTO threads (id, rollout_path, created_at, updated_at_ms, source, "
            "model_provider, cwd, title, tokens_used, archived, git_branch, first_user_message, "
            "reasoning_effort, model) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (sid, str(home / "sessions" / "2026" / "01" / "02"
                      / f"rollout-2026-01-02T00-00-00-{sid}.jsonl"),
             "2026-01-02T00:00:00Z", "2026-01-02T01:00:00Z", "vscode", "openai",
             "/work/repo", "Parent thread", 1234, 0, "main", "real prompt", "high", "gpt-6"))
        conn.execute(
            "INSERT INTO threads (id, rollout_path, created_at, source, model_provider, cwd, "
            "title, agent_nickname, agent_path) VALUES (?,?,?,?,?,?,?,?,?)",
            (child, "/nonexistent/rollout.jsonl", "2026-01-02T00:10:00Z",
             json.dumps({"subagent": {"thread_spawn": {"parent_thread_id": sid, "depth": 1,
                                                     "agent_nickname": "Hegel",
                                                     "agent_path": "/root/audit"}}}),
             "openai", "/work/repo", "Child thread", "Hegel", "/root/audit"))
        conn.execute("INSERT INTO thread_spawn_edges VALUES (?, ?, 'done')", (sid, child))
        conn.commit()
        conn.close()
        cat = home / "sqlite" / "codex-dev.db"
        cat.parent.mkdir(parents=True)
        conn = sqlite3.connect(cat)
        conn.execute("CREATE TABLE local_thread_catalog (host_id TEXT, thread_id TEXT, "
                     "display_title TEXT, source_created_at TEXT, source_updated_at TEXT, "
                     "cwd TEXT, source_kind TEXT, source_detail TEXT, model_provider TEXT, "
                     "git_branch TEXT, project_id TEXT, conversation_origin TEXT, "
                     "missing_candidate INTEGER)")
        conn.execute("INSERT INTO local_thread_catalog VALUES ('local', ?, 'Local chat', "
                     "'2026-01-02T00:00:00Z', '2026-01-02T01:00:00Z', '/work/repo', 'vscode', "
                     "NULL, 'openai', 'main', NULL, NULL, 0)", (sid,))
        conn.execute("INSERT INTO local_thread_catalog VALUES ('chatgpt:h1', 'cloud-1', "
                     "'Cloud chat', '2026-01-02T00:00:00Z', NULL, NULL, 'chatgpt', NULL, "
                     "'openai', NULL, NULL, NULL, 0)")
        conn.commit()
        conn.close()
        write_jsonl(home / "history.jsonl", [
            {"session_id": sid, "ts": 1767225600, "text": "logged prompt"},
            {"session_id": "other", "ts": 1767225660, "text": "second prompt"},
        ])
        return home, sid, child

    def test_state_index(self):
        home, sid, child = self.make()
        store = sessions.Store("codex", "state:state_5.sqlite", home / "state_5.sqlite", "sqlite")
        refs = {r.session_id: r for r in sessions.codex_iter_sessions(store)}
        self.assertEqual(set(refs), {sid, child})
        parent = refs[sid]
        self.assertEqual(parent.title, "Parent thread")
        self.assertEqual(parent.cwd, "/work/repo")
        self.assertIn("gpt-6", parent.models)
        self.assertIn("openai", parent.models)
        self.assertEqual(parent.extra["rollout_path"].split("/")[-1][:7], "rollout")
        self.assertEqual(parent.extra["git_branch"], "main")
        # child: subagent lineage via source JSON and thread_spawn_edges
        self.assertEqual(refs[child].parent, sid)
        self.assertEqual(refs[child].extra["source"], "subagent")
        self.assertEqual(refs[child].agent, "Hegel")

    def test_state_fragments_delegate_to_rollout(self):
        home, sid, child = self.make()
        store = sessions.Store("codex", "state:state_5.sqlite", home / "state_5.sqlite", "sqlite")
        refs = {r.session_id: r for r in sessions.codex_iter_sessions(store)}
        stats: dict[str, int] = {}
        out = list(sessions.codex_iter_fragments(store, refs[sid], 400, stats))
        self.assertTrue(any(f["kind"] == "prompt" and f["text"] == "real prompt" for f in out))
        self.assertTrue(all("rollout-" in str(f["locator"].get("file")) for f in out))
        # child has no rollout file → honest index-only fragments
        out = list(sessions.codex_iter_fragments(store, refs[child], 400, stats))
        self.assertTrue(out and all(f["kind"] == "metadata" or f["kind"] == "prompt" for f in out))
        self.assertIn("no local rollout", out[0]["basis"])

    def test_catalog_and_history(self):
        home, sid, child = self.make()
        cat = sessions.Store("codex", "catalog", home / "sqlite" / "codex-dev.db", "sqlite")
        refs = {r.session_id: r for r in sessions.codex_iter_sessions(cat)}
        self.assertEqual(refs[sid].extra["source_kind"], "vscode")
        self.assertEqual(refs["cloud-1"].extra["source_kind"], "chatgpt")
        self.assertEqual(refs["cloud-1"].extra["host_id"], "chatgpt:h1")
        # cloud-only row: no rollout → index_row fragment, never fake conversation
        stats: dict[str, int] = {}
        out = list(sessions.codex_iter_fragments(cat, refs["cloud-1"], 400, stats))
        self.assertEqual(len([f for f in out if f["kind"] in ("prompt", "assistant")]), 0)
        self.assertTrue(any(f["native_type"] == "index_row" for f in out))

        hist = sessions.Store("codex", "history", home / "history.jsonl", "jsonl_dir")
        refs = {r.session_id: r for r in sessions.codex_iter_sessions(hist)}
        self.assertEqual(len(refs), 2)
        stats = {}
        out = list(sessions.codex_iter_fragments(hist, refs[sid], 400, stats))
        self.assertEqual([f["text"] for f in out], ["logged prompt"])
        self.assertEqual(out[0]["kind"], "prompt")
        self.assertEqual(out[0]["ts"], "2026-01-01T00:00:00Z")  # epoch → ISO


class ClaudeDesktopTests(FixtureMixin, unittest.TestCase):
    def test_cowork(self):
        root = self.root / "lam"
        sess = root / "proj" / "local_abc"
        write_json(root / "proj" / "local_abc.json",
                   {"sessionId": "local_abc", "title": "Desktop chat", "cwd": "/work/repo",
                    "model": "claude-opus-5", "effort": "medium",
                    "initialMessage": "first user message",
                    "createdAt": "2026-01-07T00:00:00Z",
                    "lastActivityAt": "2026-01-07T01:00:00Z"})
        write_jsonl(sess / "audit.jsonl", [
            {"type": "system", "subtype": "init", "cwd": "/work/repo", "model": "claude-4",
             "timestamp": "2026-01-07T00:00:00Z"},
            {"type": "user", "timestamp": "2026-01-07T00:00:01Z", "uuid": "u1",
             "message": {"role": "user", "content": "desktop prompt"}},
            {"type": "user", "timestamp": "2026-01-07T00:00:02Z", "uuid": "u2",
             "parent_tool_use_id": "tu9",
             "message": {"role": "user", "content": "subagent user msg"}},
            {"type": "assistant", "timestamp": "2026-01-07T00:00:03Z", "uuid": "a1",
             "message": {"role": "assistant", "model": "claude-4",
                         "content": [{"type": "text", "text": "answer"}]}},
            {"type": "system", "subtype": "permission_request",
             "timestamp": "2026-01-07T00:00:04Z"},
            {"type": "result", "subtype": "success", "result": "ok",
             "timestamp": "2026-01-07T00:00:05Z"},
        ])
        # sensitive HMAC key + nested inner claude transcripts — must be left alone
        (sess / ".audit-key").parent.mkdir(parents=True, exist_ok=True)
        (sess / ".audit-key").write_text("SECRET-KEY", encoding="utf-8")
        inner = sess / ".claude" / "projects" / "-work-repo"
        write_jsonl(inner / "inner.jsonl", [
            {"type": "user", "timestamp": "t", "sessionId": "inner",
             "message": {"role": "user", "content": "inner transcript"}},
        ])
        store = sessions.Store("claude-desktop", "cowork", root, "session_dirs")
        refs = list(sessions.claude_desktop_iter_sessions(store))
        self.assertEqual(len(refs), 1)  # inner .claude tree not double-counted
        self.assertEqual(refs[0].title, "Desktop chat")
        self.assertEqual(refs[0].models, ["claude-opus-5"])
        self.assertEqual(refs[0].extra["effort"], "medium")

        stats: dict[str, int] = {}
        out = list(sessions.claude_desktop_iter_fragments(store, refs[0], 400, stats))
        prompts = [f for f in out if f["kind"] == "prompt"]
        # initialMessage is proven human input
        first = next(f for f in prompts if f["native_type"] == "manifest.initialMessage")
        self.assertEqual(first["authorship"], "human")
        self.assertEqual(first["text"], "first user message")
        side = [f for f in prompts if (f.get("rel") or {}).get("parent_tool_use_id")]
        self.assertTrue(side and side[0]["authorship"] == "agent")
        self.assertTrue(any(f["kind"] == "boundary" for f in out))
        self.assertTrue(any(f["kind"] == "permission" for f in out))
        self.assertTrue(any(f["native_type"] == "inner_transcript" for f in out))
        # .audit-key never read or referenced
        self.assertFalse(any(".audit-key" in json.dumps(f["locator"]) for f in out))
        self.assertEqual((sess / ".audit-key").read_text(), "SECRET-KEY")

    def test_code_sessions_linkage(self):
        root = self.root / "ccs"
        cli_sid = "cccccccc-1111-2222-3333-444444444444"
        write_json(root / "grp" / "local_x1.json",
                   {"sessionId": "local_x1", "cliSessionId": cli_sid, "cwd": "/work/repo",
                    "title": "Linked chat", "model": "claude-opus-5", "effort": "medium",
                    "permissionMode": "acceptEdits", "completedTurns": 3,
                    "priorCliSessionIds": ["older-1"],
                    "createdAt": "2026-01-07T00:00:00Z",
                    "lastActivityAt": "2026-01-07T01:00:00Z"})
        write_json(root / "grp" / "local_x2.json",
                   {"sessionId": "local_x2", "cliSessionId": "gone-1", "cwd": "/work/repo",
                    "title": "Orphaned chat", "createdAt": "2026-01-07T00:00:00Z"})
        claude_root = self.root / "claude"
        write_jsonl(claude_root / "-work-repo" / f"{cli_sid}.jsonl", [
            {"type": "user", "timestamp": "2026-01-07T00:00:01Z", "sessionId": cli_sid,
             "origin": {"kind": "human"},
             "message": {"role": "user", "content": "linked prompt"}},
            {"type": "assistant", "timestamp": "2026-01-07T00:00:02Z", "sessionId": cli_sid,
             "message": {"role": "assistant", "model": "claude-opus-5",
                         "content": [{"type": "text", "text": "linked answer"}]}},
        ])
        store = sessions.Store("claude-desktop", "code-sessions", root, "json_dir")
        refs = {r.session_id: r for r in sessions.claude_desktop_iter_sessions(store)}
        self.assertEqual(refs["local_x1"].extra["cli_session_id"], cli_sid)
        self.assertEqual(refs["local_x1"].extra["surface"], "code-tab")

        env = {"CONSILIUM_HISTORY_ROOT_CLAUDE_CODE": str(claude_root)}
        with patch.dict(os.environ, env):
            stats: dict[str, int] = {}
            out = list(sessions.claude_desktop_iter_fragments(store, refs["local_x1"], 400, stats))
        convo = [f for f in out if f["kind"] in ("prompt", "assistant")]
        self.assertTrue(any(f["text"] == "linked prompt" and f["authorship"] == "human"
                            for f in convo))
        self.assertTrue(all(f["harness"] == "claude-desktop" for f in out))
        self.assertTrue(any(f["native_type"] == "prior_cli_session" for f in out))
        # missing transcript → explicit metadata, no fabricated messages
        with patch.dict(os.environ, env):
            out = list(sessions.claude_desktop_iter_fragments(store, refs["local_x2"], 400, stats))
        self.assertFalse(any(f["kind"] in ("prompt", "assistant") for f in out))
        self.assertTrue(any(f["native_type"] == "cli_transcript" and "no transcript" in f["basis"]
                            for f in out))


class QwenTests(FixtureMixin, unittest.TestCase):
    def test_qwen(self):
        root = self.root / "qwen"
        write_jsonl(root / "-work-repo" / "chats" / "s1.jsonl", [
            {"type": "user", "timestamp": "t1", "sessionId": "s1", "cwd": "/work/repo",
             "message": {"parts": [{"text": "qwen human prompt"}]}},
            {"type": "assistant", "timestamp": "t2", "sessionId": "s1", "model": "qwen3",
             "message": {"parts": [{"functionCall": {"name": "f", "id": "c1", "args": {}}},
                                    {"text": "answer text"}]}},
            {"type": "user", "timestamp": "t3", "sessionId": "s1",
             "message": {"parts": [{"functionResponse": {"response": {"out": 1}}}]}},
            {"type": "user", "subtype": "notification", "timestamp": "t4", "sessionId": "s1",
             "message": {"parts": [{"text": "cron tick"}]}},
        ])
        store = sessions.Store("qwen-code", "projects", root, "jsonl_dir")
        refs = list(sessions.qwen_iter_sessions(store))
        self.assertEqual(refs[0].session_id, "s1")
        stats: dict[str, int] = {}
        out = list(sessions.qwen_iter_fragments(store, refs[0], 400, stats))
        prompts = [f for f in out if f["kind"] == "prompt"]
        self.assertEqual([f["text"] for f in prompts], ["qwen human prompt"])
        self.assertTrue(any(f["kind"] == "tool_result" and f["native_type"] == "user.functionResponse"
                            for f in out))
        self.assertTrue(any(f["kind"] == "context" for f in out))  # notification
        self.assertTrue(any(f["kind"] == "tool_call" for f in out))


class KimiTests(FixtureMixin, unittest.TestCase):
    def test_kimi(self):
        root = self.root / "kimi" / "sessions"
        sess = root / "%2Fwork%2Frepo" / "ks1"
        write_json(sess / "state.json",
                   {"title": "Kimi task", "workDir": "/work/repo",
                    "createdAt": "2026-01-08T00:00:00Z"})
        write_jsonl(sess / "agents" / "main" / "wire.jsonl", [
            {"type": "turn.prompt", "time": "2026-01-08T00:00:01Z", "origin": {"kind": "user"},
             "input": [{"text": "kimi human prompt"}]},
            {"type": "context.append_loop_event", "time": "2026-01-08T00:00:02Z",
             "event": {"type": "content.part", "turnId": "t1",
                       "part": {"type": "think", "think": "hmm"}}},
            {"type": "context.append_loop_event", "time": "2026-01-08T00:00:03Z",
             "event": {"type": "content.part", "turnId": "t1",
                       "part": {"type": "tool.call", "name": "run", "toolCallId": "c1", "arguments": "{}"}}},
            {"type": "context.append_loop_event", "time": "2026-01-08T00:00:04Z",
             "event": {"type": "step.end", "turnId": "t1", "finishReason": "stop"}},
            {"type": "permission.set_mode", "time": "2026-01-08T00:00:05Z", "mode": "auto"},
        ])
        write_jsonl(sess / "agents" / "worker" / "wire.jsonl", [
            {"type": "turn.prompt", "time": "2026-01-08T00:00:06Z", "origin": {"kind": "subagent"},
             "input": [{"text": "sub task"}]},
        ])
        store = sessions.Store("kimi-code", "sessions", root, "session_dirs")
        refs = list(sessions.kimi_iter_sessions(store))
        self.assertEqual(refs[0].session_id, "ks1")
        self.assertEqual(refs[0].cwd, "/work/repo")
        stats: dict[str, int] = {}
        out = list(sessions.kimi_iter_fragments(store, refs[0], 400, stats))
        prompts = [f for f in out if f["kind"] == "prompt"]
        human = [f for f in prompts if f.get("authorship") == "human"]
        sub = [f for f in prompts if f.get("authorship") == "agent"]
        self.assertEqual(len(human), 1)
        self.assertEqual(len(sub), 1)
        self.assertTrue(any(f["kind"] == "reasoning" for f in out))
        self.assertTrue(any(f["kind"] == "tool_call" for f in out))
        self.assertTrue(any(f["kind"] == "permission" for f in out))
        self.assertTrue(any(f["kind"] == "boundary" for f in out))


class OmpTests(FixtureMixin, unittest.TestCase):
    def test_omp(self):
        root = self.root / "omp"
        write_jsonl(root / "2026" / "s1.jsonl", [
            {"type": "session", "id": "s1", "cwd": "/work/repo", "title": "OMP run",
             "timestamp": "2026-01-09T00:00:00Z"},
            {"type": "message", "timestamp": "2026-01-09T00:00:01Z", "id": "m1",
             "message": {"role": "user", "content": [{"text": "omp prompt"}]}},
            {"type": "message", "timestamp": "2026-01-09T00:00:02Z", "id": "m2",
             "message": {"role": "user", "attribution": "agent",
                         "content": [{"text": "injected by orchestrator"}]}},
            {"type": "message", "timestamp": "2026-01-09T00:00:03Z", "id": "m3",
             "message": {"role": "assistant", "model": "m",
                         "content": [{"type": "thinking", "thinking": "t"},
                                     {"type": "toolCall", "id": "c1", "name": "x", "arguments": "{}"},
                                     {"type": "text", "text": "omp answer"}],
                         "stopReason": "stop"}},
            {"type": "compaction", "timestamp": "2026-01-09T00:00:04Z", "summary": "…"},
        ])
        store = sessions.Store("omp", "sessions", root, "jsonl_dir")
        refs = list(sessions.omp_iter_sessions(store))
        self.assertEqual(refs[0].title, "OMP run")
        stats: dict[str, int] = {}
        out = list(sessions.omp_iter_fragments(store, refs[0], 400, stats))
        prompts = [f for f in out if f["kind"] == "prompt"]
        self.assertEqual(len(prompts), 2)
        human = [f for f in prompts if f.get("authorship") == "human"]
        agent = [f for f in prompts if f.get("authorship") == "agent"]
        self.assertEqual(len(human), 1)
        self.assertEqual(len(agent), 1)
        self.assertTrue(any(f["kind"] == "compaction" for f in out))
        self.assertTrue(any(f["kind"] == "reasoning" for f in out))
        self.assertTrue(any(f["kind"] == "tool_call" for f in out))


class ConsiliumRunTests(FixtureMixin, unittest.TestCase):
    def test_runs(self):
        run = self.root / "runs" / "run_test-1"
        write_json(run / "meta.json",
                   {"run_id": "run_test-1", "agent_id": "grok", "backend": "grok-build",
                    "model": "grok-4.6", "effort": "high", "cwd": "/work/repo",
                    "status": "completed", "task": "do stuff",
                    "launched_at": "2026-01-10T00:00:00Z",
                    "session_handle": {"thread_id": "native-1"}})
        write_jsonl(run / "normalized" / "events.jsonl", [
            {"type": "run_started", "ts": "2026-01-10T00:00:01Z", "agent": "grok", "model": "grok-4.6"},
            {"type": "steer", "ts": "2026-01-10T00:00:02Z", "text": "keep going"},
            {"type": "text", "ts": "2026-01-10T00:00:03Z", "text": "working…"},
            {"type": "end", "ts": "2026-01-10T00:00:04Z", "status": "completed"},
        ])
        store = sessions.Store("consilium", "runs", self.root / "runs", "run_registry")
        refs = list(sessions.consilium_iter_sessions(store))
        self.assertEqual(refs[0].extra["native_session"], "native-1")
        stats: dict[str, int] = {}
        out = list(sessions.consilium_iter_fragments(store, refs[0], 400, stats))
        self.assertTrue(any(f["kind"] == "prompt" and f["authorship"] == "agent" for f in out))
        self.assertTrue(any(f["kind"] == "boundary" and f["status"] == "completed" for f in out))


class EnrichmentTests(FixtureMixin, unittest.TestCase):
    """error / usage / interrupted fields propagated from native records."""

    def test_codex_error_interrupted_usage(self):
        sid = "88887777-6666-5555-4444-333322221111"
        path = self.root / "codex" / "2026" / "02" / "01" / f"rollout-2026-02-01T00-00-00-{sid}.jsonl"
        write_jsonl(path, [
            {"timestamp": "2026-02-01T00:00:00Z", "type": "session_meta",
             "payload": {"id": sid, "cwd": "/w", "model_provider": "openai"}},
            {"timestamp": "2026-02-01T00:00:01Z", "type": "event_msg",
             "payload": {"type": "user_message", "turn_id": "t1", "message": "run it"}},
            {"timestamp": "2026-02-01T00:00:02Z", "type": "response_item",
             "payload": {"type": "function_call", "name": "shell", "call_id": "c1", "arguments": "{}"}},
            {"timestamp": "2026-02-01T00:00:03Z", "type": "response_item",
             "payload": {"type": "function_call_output", "call_id": "c1",
                         "output": json.dumps({"output": "boom", "metadata": {"exit_code": 1}})}},
            {"timestamp": "2026-02-01T00:00:04Z", "type": "event_msg",
             "payload": {"type": "turn_aborted", "turn_id": "t1"}},
            {"timestamp": "2026-02-01T00:00:05Z", "type": "event_msg",
             "payload": {"type": "token_count", "info": {"total_token_usage": {"input": 10}}}},
        ])
        store = sessions.Store("codex", "sessions", self.root / "codex", "jsonl_dir")
        ref = list(sessions.codex_iter_sessions(store))[0]
        out = list(sessions.codex_iter_fragments(store, ref, 400, {}))
        err = [f for f in out if f.get("error")]
        self.assertTrue(any(f["kind"] == "tool_result" for f in err))
        self.assertTrue(any(f.get("interrupted") for f in out))
        self.assertTrue(any(f.get("usage") for f in out))

    def test_claude_is_error_and_usage(self):
        proj = self.root / "claude" / "-p"
        sid = "12345678-1234-1234-1234-1234567890ab"
        write_jsonl(proj / f"{sid}.jsonl", [
            {"type": "user", "timestamp": "2026-02-01T00:00:00Z", "sessionId": sid,
             "origin": {"kind": "human"}, "message": {"role": "user", "content": "go"}},
            {"type": "assistant", "timestamp": "2026-02-01T00:00:01Z", "sessionId": sid,
             "message": {"role": "assistant", "model": "claude-opus-5",
                         "usage": {"input_tokens": 5, "output_tokens": 9},
                         "content": [{"type": "tool_use", "id": "t1", "name": "Bash",
                                      "input": {"command": "false"}}]}},
            {"type": "user", "timestamp": "2026-02-01T00:00:02Z", "sessionId": sid,
             "message": {"role": "user", "content": [
                 {"type": "tool_result", "tool_use_id": "t1", "is_error": True,
                  "content": "exit 1"}]}},
        ])
        store = sessions.Store("claude-code", "projects", self.root / "claude", "jsonl_dir")
        ref = list(sessions.claude_iter_sessions(store))[0]
        out = list(sessions.claude_iter_fragments(store, ref, 400, {}))
        self.assertTrue(any(f.get("error") and f["kind"] == "tool_result" for f in out))
        self.assertTrue(any((f.get("usage") or {}).get("output") == 9 for f in out))


def afrag(kind, authorship=None, text=None, tool=None, inp=None, error=False,
          ts=None, seq=0, usage=None, interrupted=False, status=None):
    f = {"kind": kind, "seq": seq, "native_type": "test",
         "locator": {"file": "fx", "line": seq}}
    if text is not None:
        f["text"] = text
    if authorship:
        f["authorship"] = authorship
    if tool:
        f["rel"] = {"tool": tool}
        f["text"] = json.dumps({"name": tool, "input": inp or {}})
    if error:
        f["error"] = True
    if ts:
        f["ts"] = ts
    if usage:
        f["usage"] = usage
    if interrupted:
        f["interrupted"] = True
    if status:
        f["status"] = status
    return f


class AnalyzeTests(FixtureMixin, unittest.TestCase):
    """Turn/flags/stats projections over synthetic fragment streams."""

    def run_session(self, frags, store_name="s"):
        import analyze
        store = sessions.Store("h", store_name, self.root, "jsonl_dir")
        ref = sessions.SessionRef(harness="h", store=store_name, session_id="sess-1",
                                  locator={}, title="t", cwd="/w")
        return analyze.analyze_session(store, ref, frags)

    def test_turn_boundaries_and_prompt_merge(self):
        frags = [
            afrag("prompt", "human", "first", seq=1),
            afrag("prompt", "human", "second same request", seq=2),  # merged
            afrag("assistant", "agent", "reply", seq=3, ts="2026-01-01T00:00:10Z"),
            afrag("prompt", "human", "next task", seq=4, ts="2026-01-01T00:00:20Z"),
            afrag("assistant", "agent", "reply2", seq=5, ts="2026-01-01T00:00:30Z"),
        ]
        rows, flags = self.run_session(frags)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["turn"], 1)
        self.assertEqual(rows[0]["user_msgs"], 2)
        self.assertTrue(rows[0]["has_final"])
        self.assertEqual(rows[1]["turn"], 2)

    def test_technical_prompts_do_not_trigger(self):
        frags = [
            afrag("context", "system", "sys", seq=1),
            afrag("prompt", "system", "auto-injection", seq=2),
            afrag("prompt", "agent", "subagent task", seq=3),
            afrag("prompt", "human", "real prompt", seq=4),
            afrag("assistant", "agent", "ok", seq=5),
        ]
        rows, _ = self.run_session(frags)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["user_msgs"], 1)

    def test_flags_full_session(self):
        frags = [
            afrag("prompt", "human", "do it", seq=1, ts="2026-01-01T00:00:00Z"),
            afrag("tool_call", tool="Read", inp={"file_path": "/a.py"}, seq=2),
            afrag("tool_result", seq=3),
        ]
        # 5 consecutive search calls: search_loop; 3 identical Greps: retry_loop
        frags += [afrag("tool_call", tool="Grep", inp={"pattern": "x"}, seq=4 + i) for i in range(3)]
        frags += [afrag("tool_result", error=True, seq=7),
                  afrag("tool_call", tool="Read", inp={"file_path": "/b.py"}, seq=8),
                  afrag("tool_call", tool="Read", inp={"file_path": "/c.py"}, seq=9)]
        # mutation on a path never read
        frags += [afrag("tool_call", tool="Write", inp={"file_path": "/new.py"}, seq=10),
                  afrag("tool_result", seq=11),
                  afrag("assistant", "agent", "done", seq=12)]
        # permission friction + compaction + interrupt
        frags += [afrag("permission", "system", seq=13 + i) for i in range(3)]
        frags += [afrag("compaction", "system", seq=16),
                  afrag("metadata", "system", seq=17, interrupted=True)]
        # correction prompt → turn 2; then unanswered prompt → abandoned
        frags += [afrag("prompt", "human", "that's not what I asked, revert it", seq=18),
                  afrag("assistant", "agent", "ok reverted", seq=19),
                  afrag("prompt", "human", "and also …", seq=20)]
        rows, flags = self.run_session(frags)
        pats = {f["pattern"] for f in flags}
        self.assertIn("retry_loop", pats)
        self.assertIn("search_loop", pats)
        self.assertIn("edit_without_read", pats)
        self.assertIn("correction", pats)
        self.assertIn("permission_friction", pats)
        self.assertIn("context_pressure", pats)
        self.assertIn("interrupted", pats)
        self.assertIn("abandoned", pats)
        self.assertEqual(len(rows), 3)
        self.assertFalse(rows[-1]["has_final"])
        # evidence locators always present for evidence-bearing flags
        ev = [f for f in flags if f["pattern"] == "retry_loop"][0]
        self.assertTrue(ev["evidence"])
        self.assertIn("file", ev["evidence"][0]["locator"])
        self.assertIn("seq", ev["evidence"][0])

    def test_retry_loop_step_collapsing(self):
        # calls fanned out from one raw record (same locator) = one parallel
        # step — must NOT count as a retry run (grok batch-edit false positive)
        one_loc = {"file": "fx", "line": 7}
        frags = [afrag("prompt", "human", "go", seq=1)]
        for i, p in enumerate(("/a.py", "/b.py", "/c.py")):
            f = afrag("tool_call", tool="Write", inp={"file_path": p}, seq=2 + i)
            f["locator"] = one_loc
            frags.append(f)
        frags.append(afrag("assistant", "agent", "done", seq=6))
        _, flags = self.run_session(frags)
        self.assertNotIn("retry_loop", {f["pattern"] for f in flags})
        # same call across three DISTINCT steps IS a retry loop
        frags = [afrag("prompt", "human", "go", seq=1)]
        for i in range(3):
            frags.append(afrag("tool_call", tool="Bash", inp={"command": "ls"},
                               seq=2 + i * 2))
            frags.append(afrag("tool_result", seq=3 + i * 2))
        _, flags = self.run_session(frags)
        self.assertIn("retry_loop", {f["pattern"] for f in flags})

    def test_retry_loop_unparseable_input(self):
        # truncated/unparseable args must not collapse all calls into sig="{}"
        frags = [afrag("prompt", "human", "go", seq=1)]
        for i, name in enumerate(("/x.py", "/y.py", "/z.py")):
            f = afrag("tool_call", tool="Write", seq=2 + i)
            f["text"] = '{"name":"Write","arguments":"{\\"file_path\\": \\"' + name  # truncated JSON
            frags.append(f)
        _, flags = self.run_session(frags)
        self.assertNotIn("retry_loop", {f["pattern"] for f in flags})

    def test_error_burst(self):
        frags = [afrag("prompt", "human", "go", seq=1)]
        frags += [afrag("tool_result", error=True, seq=2 + i) for i in range(3)]
        frags += [afrag("assistant", "agent", "x", seq=6)]
        _, flags = self.run_session(frags)
        self.assertIn("error_burst", {f["pattern"] for f in flags})

    def test_stats_grouping_and_dedup(self):
        import analyze
        root = self.root / "claude"
        sid = "ded00000-0000-0000-0000-00000000000a"
        proj = root / "-p"
        write_jsonl(proj / f"{sid}.jsonl", [
            {"type": "user", "timestamp": "2026-03-01T00:00:00Z", "sessionId": sid,
             "origin": {"kind": "human"}, "message": {"role": "user", "content": "hi"}},
            {"type": "assistant", "timestamp": "2026-03-01T00:00:05Z", "sessionId": sid,
             "message": {"role": "assistant", "model": "claude-x",
                         "content": [{"type": "text", "text": "hey"}]}},
        ])
        # two stores over the same tree → session counted once
        stores = [sessions.Store("claude-code", "projects", root, "jsonl_dir"),
                  sessions.Store("claude-code", "dup", root, "jsonl_dir")]
        for s in stores:
            s.status = "ok"
        args = type("A", (), {"cwd": None, "since": None, "until": None, "max_chars": 400})
        stats: dict[str, int] = {}
        seen = [(st.name, r.session_id) for st, r, f in analyze.iter_dedup_sessions(stores, args, stats)]
        self.assertEqual(len(seen), 1)
        self.assertEqual(seen[0][0], "projects")
        self.assertEqual(stats.get("deduped"), 1)

        # cmd_stats aggregates over the deduped stream
        import contextlib
        import io
        import unittest.mock as m
        ns = type("N", (), {})()
        ns.agent = "claude-code"; ns.store = None; ns.cwd = None
        ns.since = None; ns.until = None; ns.max_chars = 400; ns.limit = 0; ns.by = "model"
        with m.patch.object(analyze.S, "selected_stores", return_value=stores):
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                analyze.cmd_stats(ns)
        rows = [json.loads(l) for l in buf.getvalue().splitlines()]
        grp = next(r for r in rows if r.get("group") == "claude-x")
        self.assertEqual(grp["sessions"], 1)  # dedup applied
        self.assertEqual(grp["turns"], 1)
        self.assertEqual(grp["sessions_no_model"], 0)
        self.assertTrue(rows[-1]["_summary"])
        self.assertIn("dedup_rule", rows[-1])


class CliAnalyticsTests(FixtureMixin, unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")

    def run_cli(self, *args, env_extra=None):
        env = dict(self.env)
        env.update(env_extra or {})
        return subprocess.run(
            [sys.executable, str(LIB / "sessions.py"), *args],
            capture_output=True, text=True, encoding="utf-8", timeout=30, env=env)

    def lines(self, proc):
        return [json.loads(l) for l in proc.stdout.splitlines() if l.strip()]

    def test_turns_flags_stats_cli(self):
        proj = self.root / "claude" / "-p"
        sid = "aaaabbbb-0000-1111-2222-333344445555"
        write_jsonl(proj / f"{sid}.jsonl", [
            {"type": "user", "timestamp": "2026-03-02T00:00:00Z", "sessionId": sid,
             "origin": {"kind": "human"}, "message": {"role": "user", "content": "build it"}},
            {"type": "assistant", "timestamp": "2026-03-02T00:00:05Z", "sessionId": sid,
             "message": {"role": "assistant", "model": "claude-opus-5",
                         "content": [{"type": "tool_use", "id": "t1", "name": "Read",
                                      "input": {"file_path": "/x.py"}}]}},
            {"type": "user", "timestamp": "2026-03-02T00:00:06Z", "sessionId": sid,
             "message": {"role": "user", "content": [
                 {"type": "tool_result", "tool_use_id": "t1", "is_error": True,
                  "content": "no such file"}]}},
            {"type": "user", "timestamp": "2026-03-02T00:00:30Z", "sessionId": sid,
             "origin": {"kind": "human"},
             "message": {"role": "user", "content": "that's not right, undo it"}},
        ])
        env = {"CONSILIUM_HISTORY_ROOT_CLAUDE_CODE": str(self.root / "claude")}

        proc = self.run_cli("turns", "-a", "claude-code", env_extra=env)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        rows = [r for r in self.lines(proc) if not r.get("_summary")]
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["turn"], 1)
        self.assertEqual(rows[0]["tool_errors"], 1)
        self.assertEqual(rows[0]["duration_s"], 6.0)
        self.assertFalse(rows[1]["has_final"])

        proc = self.run_cli("flags", "-a", "claude-code", env_extra=env)
        pats = {r["pattern"] for r in self.lines(proc) if not r.get("_summary")}
        self.assertIn("correction", pats)
        self.assertIn("abandoned", pats)

        proc = self.run_cli("stats", "-a", "claude-code", "--by", "model", env_extra=env)
        rows = self.lines(proc)
        grp = next(r for r in rows if r.get("group") == "claude-opus-5")
        self.assertEqual(grp["turns"], 2)
        self.assertEqual(grp["tool_errors"], 1)


class WindowsPathTests(FixtureMixin, unittest.TestCase):
    """Store paths resolve to %APPDATA%/%LOCALAPPDATA% under Windows."""

    def _stores(self, harness, env):
        env = dict(env)
        env.pop("CONSILIUM_STEER_DIR", None)  # keep the host env out of steer-root resolution
        with patch.object(sessions, "IS_WINDOWS", True), \
             patch.object(sessions, "IS_MACOS", False), \
             patch.object(sessions, "HOME", self.root), \
             patch.dict(os.environ, env, clear=False):
            return sessions.stores_for(harness)

    def test_windows_bases(self):
        appdata = str(self.root / "AppData" / "Roaming")
        localapp = str(self.root / "AppData" / "Local")
        env = {"APPDATA": appdata, "LOCALAPPDATA": localapp}
        cur = self._stores("cursor", env)
        self.assertEqual(cur[0].path,
                         self.root / "AppData" / "Roaming" / "Cursor" / "User" / "globalStorage" / "state.vscdb")
        cd = self._stores("claude-desktop", env)
        self.assertTrue(str(cd[0].path).startswith(appdata))
        dev = self._stores("devin", env)
        # Both Roaming and LocalAppData candidates are offered (order: roaming first)
        self.assertEqual(len(dev), 4)
        self.assertTrue(str(dev[0].path).startswith(appdata))
        self.assertTrue(str(dev[2].path).startswith(localapp))
        oc = self._stores("opencode", env)
        self.assertTrue(str(oc[0].path).startswith(localapp))
        with patch.object(sessions, "IS_WINDOWS", True), \
             patch.object(sessions, "IS_MACOS", False), \
             patch.object(sessions, "HOME", self.root), \
             patch.dict(os.environ, {**env, "CONSILIUM_STEER_DIR": ""}, clear=False):
            self.assertTrue(str(sessions._steer_root()).startswith(localapp))

    def test_sqlite_uri_windows_path(self):
        # file: URI must use forward slashes even for drive-letter paths
        db = self.root / "sub dir" / "x.db"
        db.parent.mkdir(parents=True)
        conn = sqlite3.connect(db)
        conn.execute("CREATE TABLE t (a)")
        conn.close()
        c = sessions.open_sqlite_ro(db)
        self.assertIsNotNone(c)
        c.close()


class CliTests(FixtureMixin, unittest.TestCase):
    """End-to-end through argv parsing using CONSILIUM_HISTORY_ROOT_* overrides."""

    def setUp(self):
        super().setUp()
        self.env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")

    def run_cli(self, *args, env_extra=None):
        env = dict(self.env)
        env.update(env_extra or {})
        proc = subprocess.run(
            [sys.executable, str(LIB / "sessions.py"), *args],
            capture_output=True, text=True, encoding="utf-8", timeout=30, env=env)
        return proc

    def make_claude(self):
        proj = self.root / "claude" / "-work-repo"
        sid = "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
        write_jsonl(proj / f"{sid}.jsonl", [
            {"type": "summary", "summary": "CLI test", "timestamp": "2026-01-11T00:00:00Z"},
            {"type": "user", "timestamp": "2026-01-11T00:00:01Z", "cwd": "/work/repo",
             "sessionId": sid, "uuid": "u1", "origin": {"kind": "human"},
             "message": {"role": "user", "content": "needle in the haystack"}},
            {"type": "assistant", "timestamp": "2026-01-11T00:00:02Z", "sessionId": sid, "uuid": "a1",
             "message": {"role": "assistant", "model": "claude-opus-5",
                         "content": [{"type": "text", "text": "found it"}]}},
        ])
        return self.root / "claude", sid

    def lines(self, proc):
        return [json.loads(l) for l in proc.stdout.splitlines() if l.strip()]

    def test_list_grep_show_around(self):
        root, sid = self.make_claude()
        env = {"CONSILIUM_HISTORY_ROOT_CLAUDE_CODE": str(root)}

        proc = self.run_cli("list", "-a", "claude-code", env_extra=env)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        rows = self.lines(proc)
        self.assertEqual(rows[0]["session_id"], f"-work-repo/{sid}")
        self.assertTrue(rows[-1]["_summary"])
        self.assertTrue(rows[-1]["scan_complete"])

        proc = self.run_cli("grep", "-a", "claude-code", "needle", env_extra=env)
        hits = [r for r in self.lines(proc) if not r.get("_summary")]
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["kind"], "prompt")
        self.assertEqual(hits[0]["authorship"], "human")
        self.assertIn("line", hits[0]["locator"])

        proc = self.run_cli("show", f"claude-code:-work-repo/{sid}", env_extra=env)
        rows = self.lines(proc)
        self.assertEqual(rows[0]["_session"]["title"], "CLI test")
        seqs = [r["seq"] for r in rows if "seq" in r]
        target = seqs[0]
        proc = self.run_cli("show", f"claude-code:-work-repo/{sid}",
                            "--around", str(target), "--context", "1", env_extra=env)
        rows = self.lines(proc)
        seqs2 = [r["seq"] for r in rows if "seq" in r]
        self.assertIn(target, seqs2)

    def test_missing_store_reports_not_crash(self):
        proc = self.run_cli("list", "-a", "qwen-code",
                            env_extra={"CONSILIUM_HISTORY_ROOT_QWEN_CODE": str(self.root / "nope")})
        self.assertEqual(proc.returncode, 0, proc.stderr)
        summary = self.lines(proc)[-1]
        self.assertEqual(summary["stores"][0]["status"], "missing")
        self.assertTrue(summary["scan_complete"])

    def test_no_db_or_index_created(self):
        root, sid = self.make_claude()
        env = {"CONSILIUM_HISTORY_ROOT_CLAUDE_CODE": str(root)}
        before = {str(p) for p in self.root.rglob("*")}
        proc = self.run_cli("grep", "-a", "claude-code", "needle", env_extra=env)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        after = {str(p) for p in self.root.rglob("*")}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main(verbosity=2)
