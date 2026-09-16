#!/usr/bin/env python3
"""consilium sessions — search and navigate local coding-agent session histories.

Read-only, index-free reader over the native on-disk session stores of CLI
coding agents. Emits bounded JSONL fragments with source locators and honest
coverage diagnostics. See references/session-history.md for the format
recipes and the navigation algorithm this implements.

Never execute stored content. Never mutate source files. SQLite stores are
opened `mode=ro` + `PRAGMA query_only` — never `immutable=1`, never manual
WAL parsing.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Iterator

HOME = Path.home()
IS_MACOS = sys.platform == "darwin"

EXIT_OK = 0
EXIT_USAGE = 5
EXIT_PARTIAL = 2
EXIT_FAILED = 3

# ---------------------------------------------------------------------------
# Normalized fragment model
#
# kind:      prompt | assistant | context | tool_call | tool_result |
#            reasoning | permission | compaction | boundary | metadata | unknown
# authorship: human | agent | system | unknown   (who authored the text)
# visible:   True | False | None(unknown)        (shown to the user)
# Every fragment carries `locator` so the reader can jump back to the source.
# ---------------------------------------------------------------------------

KINDS_CONVO = {"prompt", "assistant"}
KINDS_TOOLS = {"tool_call", "tool_result"}
KINDS_SYSTEM = {"context", "metadata", "boundary", "permission", "compaction"}
SCOPES = {
    "convo": KINDS_CONVO,
    "prompts": {"prompt"},
    "assistant": {"assistant"},
    "tools": KINDS_TOOLS,
    "reasoning": {"reasoning"},
    "system": KINDS_SYSTEM | {"unknown"},
    "all": None,  # no filtering
}

AUTOCONTEXT_MARKERS = (
    "<command-name>",
    "<command-message>",
    "<command-args>",
    "<local-command-stdout>",
    "<local-command-stderr>",
    "<system-reminder>",
    "<environment_context>",
    "Caveat:",
)


def _trunc(text: Any, limit: int) -> tuple[str, bool]:
    if not isinstance(text, str):
        text = json.dumps(text, ensure_ascii=False)
    if limit and len(text) > limit:
        return text[:limit], True
    return text, False


def frag(
    harness: str,
    store: str,
    session_id: str,
    seq: int,
    kind: str,
    native_type: str,
    locator: dict[str, Any],
    *,
    text: Any = None,
    ts: Any = None,
    authorship: str = "unknown",
    visible: bool | None = None,
    basis: str = "",
    model: str | None = None,
    provider: str | None = None,
    cwd: str | None = None,
    rel: dict[str, Any] | None = None,
    phase: str | None = None,
    status: str | None = None,
    max_chars: int = 400,
) -> dict[str, Any]:
    out: dict[str, Any] = {
        "harness": harness,
        "store": store,
        "session_id": session_id,
        "seq": seq,
        "kind": kind,
        "native_type": native_type,
        "locator": locator,
    }
    if text is not None:
        out["text"], truncated = _trunc(text, max_chars)
        if truncated:
            out["truncated"] = True
    if ts is not None:
        out["ts"] = _iso(ts)
    if authorship != "unknown":
        out["authorship"] = authorship
    if visible is not None:
        out["visible"] = visible
    if basis:
        out["basis"] = basis
    if model:
        out["model"] = model
    if provider:
        out["provider"] = provider
    if cwd:
        out["cwd"] = cwd
    if rel:
        out["rel"] = rel
    if phase:
        out["phase"] = phase
    if status:
        out["status"] = status
    return out


def _iso(value: Any) -> str | None:
    """Normalize a timestamp (ISO str, epoch s/ms) to ISO-8601 UTC."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        seconds = value / 1000.0 if value > 1e12 else float(value)
        try:
            return datetime.fromtimestamp(seconds, tz=timezone.utc).isoformat().replace("+00:00", "Z")
        except (OverflowError, OSError, ValueError):
            return str(value)
    if isinstance(value, str):
        return value
    return str(value)


def parse_time_bound(value: str | None) -> float | None:
    """--since/--until: ISO-8601 (naive = local tz) or epoch seconds."""
    if not value:
        return None
    value = value.strip()
    if re.fullmatch(r"\d+(\.\d+)?", value):
        epoch = float(value)
        return epoch / 1000.0 if epoch > 1e12 else epoch
    text = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        raise SystemExit(f"invalid time bound: {value!r} (expected ISO-8601 or epoch)")
    if dt.tzinfo is None:
        dt = dt.astimezone()
    return dt.timestamp()


def ts_epoch(value: Any) -> float | None:
    """Parse a stored timestamp back to epoch seconds for filtering."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return value / 1000.0 if value > 1e12 else float(value)
    if isinstance(value, str):
        try:
            return parse_time_bound(value)
        except SystemExit:
            return None
    return None


# ---------------------------------------------------------------------------
# IO helpers
# ---------------------------------------------------------------------------

def iter_jsonl(path: Path, stats: dict[str, int]) -> Iterator[tuple[int, dict[str, Any]]]:
    """Yield (line_no, record) for each parseable JSON object line.

    Reads are bounded to the file size observed at open time; a truncated
    trailing line is reported via stats['truncated_tail'], malformed interior
    lines via stats['malformed'].
    """
    try:
        size = path.stat().st_size
        fh = path.open("r", encoding="utf-8", errors="replace")
    except OSError:
        stats["unreadable"] = stats.get("unreadable", 0) + 1
        return
    with fh:
        data = fh.read(size + 1)
    if not data.endswith("\n") and data.strip():
        stats["truncated_tail"] = stats.get("truncated_tail", 0) + 1
    # split('\n'), not splitlines(): JSON strings may legally contain raw
    # U+2028/U+2029/NEL which splitlines() would wrongly treat as line breaks.
    for line_no, line in enumerate(data.split("\n"), 1):
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            stats["malformed"] = stats.get("malformed", 0) + 1
            continue
        if isinstance(record, dict):
            yield line_no, record
        else:
            stats["malformed"] = stats.get("malformed", 0) + 1


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError):
        return None


def tail_line(path: Path, chunk: int = 8192) -> str | None:
    try:
        size = path.stat().st_size
        with path.open("rb") as fh:
            fh.seek(max(0, size - chunk))
            data = fh.read().decode("utf-8", errors="replace")
    except OSError:
        return None
    lines = [ln for ln in data.splitlines() if ln.strip()]
    return lines[-1] if lines else None


def open_sqlite_ro(path: Path) -> sqlite3.Connection:
    """Short-lived read-only connection. Never immutable=1 (unsafe on live DBs),
    never manual WAL parsing. Raises on failure → caller reports unavailable."""
    conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=2.0)
    conn.execute("PRAGMA query_only=ON")
    return conn


def table_exists(conn: sqlite3.Connection, name: str) -> bool:
    row = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)
    ).fetchone()
    return row is not None


def table_columns(conn: sqlite3.Connection, name: str) -> set[str]:
    try:
        return {r[1] for r in conn.execute(f"PRAGMA table_info({name})")}
    except sqlite3.Error:
        return set()


def content_blocks_text(content: Any, kinds: tuple[str, ...]) -> list[str]:
    if isinstance(content, str):
        return [content] if "text" in kinds else []
    if not isinstance(content, list):
        return []
    return [
        str(b.get(kinds[0] if kinds == ("text",) else "text") or b.get("text") or b.get("thinking") or "")
        for b in content
        if isinstance(b, dict) and b.get("type") in kinds
    ]


# ---------------------------------------------------------------------------
# Harness descriptors
# ---------------------------------------------------------------------------

# evidence: verified = reader validated against live data on a dev machine;
#           spec    = reader written from reference-repo schemas/fixtures only
HARNESS_EVIDENCE = {
    "claude-code": "verified",
    "codex": "verified",
    "opencode": "verified",
    "grok": "verified",
    "devin": "verified",
    "gemini": "verified",
    "consilium": "verified",
    "claude-desktop": "verified",
    "cursor": "spec",
    "qwen-code": "spec",
    "kimi-code": "spec",
    "omp": "spec",
}

ENV_ROOT = "CONSILIUM_HISTORY_ROOT_"


def _root_override(slug: str) -> Path | None:
    raw = os.environ.get(ENV_ROOT + slug.upper().replace("-", "_"))
    return Path(raw).expanduser() if raw else None


def _steer_root() -> Path:
    env = os.environ.get("CONSILIUM_STEER_DIR")
    if env:
        return Path(env).expanduser()
    if IS_MACOS:
        return HOME / "Library" / "Caches" / "agents-consilium" / "steer"
    return Path(os.environ.get("XDG_CACHE_HOME", HOME / ".cache")) / "agents-consilium" / "steer"


class Store:
    """One physical history store a reader knows about."""

    def __init__(self, harness: str, name: str, path: Path, kind: str):
        self.harness = harness
        self.name = name
        self.path = path
        self.kind = kind  # jsonl_dir | session_dirs | sqlite | json_dir | run_registry
        self.status = "ok" if path.exists() else "missing"
        self.error: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return {
            "harness": self.harness,
            "store": self.name,
            "path": str(self.path),
            "kind": self.kind,
            "status": self.status,
            "error": self.error,
            "evidence": HARNESS_EVIDENCE.get(self.harness, "spec"),
        }


def stores_for(harness: str) -> list[Store]:
    ov = _root_override(harness)
    if harness == "claude-code":
        roots = [ov] if ov else [HOME / ".claude" / "projects", HOME / ".claude.back" / "projects"]
        return [Store(harness, f"{r.parent.name}/{r.name}", r, "jsonl_dir") for r in roots]
    if harness == "codex":
        if ov:
            return [Store(harness, "sessions", ov, "jsonl_dir")]
        codex_home = Path(os.environ.get("CODEX_HOME") or (HOME / ".codex"))
        out = [
            Store(harness, "sessions", codex_home / "sessions", "jsonl_dir"),
            Store(harness, "archived", codex_home / "archived_sessions", "jsonl_dir"),
        ]
        for p in sorted(codex_home.glob("state_*.sqlite")):
            out.append(Store(harness, f"state:{p.name}", p, "sqlite"))
        out.append(Store(harness, "catalog", codex_home / "sqlite" / "codex-dev.db", "sqlite"))
        out.append(Store(harness, "summaries",
                         codex_home / "sqlite" / "codex-thread-summaries-dev.db", "sqlite"))
        out.append(Store(harness, "history", codex_home / "history.jsonl", "jsonl_dir"))
        return out
    if harness == "opencode":
        if ov:
            return [Store(harness, "custom", ov, "json_dir")]
        base = HOME / ".local" / "share" / "opencode"
        return [
            Store(harness, "db", base / "opencode.db", "sqlite"),
            Store(harness, "storage", base / "storage", "json_dir"),
        ]
    if harness == "grok":
        return [Store(harness, "sessions", ov or (HOME / ".grok" / "sessions"), "session_dirs")]
    if harness == "devin":
        base = ov or (HOME / ".local" / "share" / "devin" / "cli")
        return [
            Store(harness, "sessions.db", base / "sessions.db", "sqlite"),
            Store(harness, "transcripts", base / "transcripts", "json_dir"),
        ]
    if harness == "gemini":
        base = ov or (HOME / ".gemini")
        return [
            Store(harness, "chats", base / "tmp", "json_dir"),
            Store(harness, "projects-map", base / "projects.json", "json_dir"),
        ]
    if harness == "claude-desktop":
        base = ov or (HOME / "Library" / "Application Support" / "Claude")
        if ov:
            return [Store(harness, "cowork", base, "session_dirs")]
        return [
            Store(harness, "cowork", base / "local-agent-mode-sessions", "session_dirs"),
            Store(harness, "code-sessions", base / "claude-code-sessions", "json_dir"),
        ]
    if harness == "cursor":
        if ov:
            return [Store(harness, "custom", ov, "sqlite")]
        base = HOME / "Library" / "Application Support" / "Cursor" / "User"
        out = [Store(harness, "globalStorage", base / "globalStorage" / "state.vscdb", "sqlite")]
        ws = base / "workspaceStorage"
        if ws.is_dir():
            for sub in sorted(ws.iterdir()):
                db = sub / "state.vscdb"
                if db.exists():
                    out.append(Store(harness, f"workspace:{sub.name[:8]}", db, "sqlite"))
        return out
    if harness == "qwen-code":
        return [Store(harness, "projects", ov or (HOME / ".qwen" / "projects"), "jsonl_dir")]
    if harness == "kimi-code":
        home = os.environ.get("KIMI_CODE_HOME")
        return [Store(harness, "sessions", ov or Path(home or (HOME / ".kimi-code")) / "sessions", "session_dirs")]
    if harness == "omp":
        return [Store(harness, "sessions", ov or (HOME / ".omp" / "agent" / "sessions"), "jsonl_dir")]
    if harness == "consilium":
        return [Store(harness, "runs", _steer_root() / "runs", "run_registry")]
    return []


ALL_HARNESSES = [
    "claude-code", "codex", "opencode", "grok", "devin", "gemini",
    "claude-desktop", "cursor", "qwen-code", "kimi-code", "omp", "consilium",
]


class SessionRef:
    def __init__(self, harness: str, store: str, session_id: str, **kw: Any):
        self.harness = harness
        self.store = store
        self.session_id = session_id
        self.locator = kw.get("locator") or {}
        self.title = kw.get("title")
        self.cwd = kw.get("cwd")
        self.created = kw.get("created")
        self.updated = kw.get("updated")
        self.models = kw.get("models") or []
        self.parent = kw.get("parent")
        self.agent = kw.get("agent")          # subagent identity when present
        self.hidden = kw.get("hidden")
        self.extra = kw.get("extra") or {}

    def matches(self, cwd: str | None, since: float | None, until: float | None) -> bool:
        if cwd and not (self.cwd and cwd in self.cwd):
            return False
        created, updated = ts_epoch(self.created), ts_epoch(self.updated)
        if since and updated is not None and updated < since:
            return False
        if until and created is not None and created > until:
            return False
        return True

    def as_dict(self) -> dict[str, Any]:
        out = {
            "harness": self.harness,
            "store": self.store,
            "session_id": self.session_id,
            "locator": self.locator,
        }
        for key in ("title", "cwd", "parent", "agent", "hidden"):
            value = getattr(self, key)
            if value is not None:
                out[key] = value
        if self.created:
            out["created"] = _iso(self.created)
        if self.updated:
            out["updated"] = _iso(self.updated)
        if self.models:
            out["models"] = sorted(set(self.models))
        out.update(self.extra)
        return out


# ---------------------------------------------------------------------------
# claude-code
# ---------------------------------------------------------------------------

def claude_iter_sessions(store: Store) -> Iterator[SessionRef]:
    for path in sorted(store.path.rglob("*.jsonl")):
        rel = path.relative_to(store.path).with_suffix("").as_posix()
        project_dir = path.relative_to(store.path).parts[0] if len(path.relative_to(store.path).parts) > 1 else ""
        stats: dict[str, int] = {}
        first_ts = last_ts = cwd = title = None
        models: list[str] = []
        parent = None
        agent = None
        for line_no, rec in iter_jsonl(path, stats):
            if first_ts is None:
                first_ts = rec.get("timestamp")
            if rec.get("timestamp"):
                last_ts = rec["timestamp"]
            t = rec.get("type")
            if cwd is None and rec.get("cwd"):
                cwd = rec["cwd"]
            if t == "custom-title" and rec.get("customTitle"):
                title = rec["customTitle"]
            elif title is None and t == "ai-title" and rec.get("aiTitle"):
                title = rec["aiTitle"]
            elif title is None and t == "summary" and rec.get("summary"):
                title = rec["summary"]
            if t == "assistant" and isinstance(rec.get("message"), dict):
                m = rec["message"].get("model")
                if m and m != "<synthetic>" and m not in models:
                    models.append(m)
        if "subagents/" in rel:
            parent = rel.split("/subagents/")[0]
            agent = path.stem
        yield SessionRef(
            "claude-code", store.name, rel,
            locator={"file": str(path)},
            title=title, cwd=cwd or (None if not project_dir else None),
            created=first_ts, updated=last_ts, models=models,
            parent=parent, agent=agent,
            extra={"project_dir": project_dir} if project_dir else {},
        )


def claude_iter_fragments(store: Store, ref: SessionRef, max_chars: int, stats: dict[str, int]) -> Iterator[dict[str, Any]]:
    path = Path(ref.locator["file"])
    sidechain = "subagents/" in ref.session_id
    seq = 0
    for line_no, rec in iter_jsonl(path, stats):
        seq += 1
        loc = {"file": str(path), "line": line_no}
        t = rec.get("type")
        ts = rec.get("timestamp")
        cwd = rec.get("cwd")
        rel_ids = {"uuid": rec.get("uuid"), "parent": rec.get("parentUuid"), "sessionId": rec.get("sessionId")}
        if rec.get("isSidechain") or sidechain:
            rel_ids["sidechain"] = True
        msg = rec.get("message") if isinstance(rec.get("message"), dict) else None

        if t == "user" and msg is not None:
            content = msg.get("content")
            origin_kind = (rec.get("origin") or {}).get("kind") if isinstance(rec.get("origin"), dict) else None
            if isinstance(content, str):
                blocks = [{"type": "text", "text": content}]
            elif isinstance(content, list):
                blocks = [b for b in content if isinstance(b, dict)]
            else:
                blocks = []
            auto = bool(rec.get("isMeta"))
            for b in blocks:
                seq += 1
                bt = b.get("type")
                text = b.get("text") or ("" if bt != "tool_result" else _tool_result_text(b))
                if bt == "tool_result" or isinstance(b.get("content"), list):
                    yield frag("claude-code", store.name, ref.session_id, seq, "tool_result", "user.tool_result", loc,
                               text=text, ts=ts, authorship="system", visible=False,
                               basis="tool_result block inside user-role record",
                               cwd=cwd, rel={**rel_ids, "call_id": b.get("tool_use_id")}, max_chars=max_chars)
                else:
                    marker = auto or any(m in (b.get("text") or "") for m in AUTOCONTEXT_MARKERS)
                    auth = "human" if origin_kind == "human" else ("system" if marker else ("agent" if origin_kind else "unknown"))
                    yield frag("claude-code", store.name, ref.session_id, seq,
                               "context" if marker and auth == "system" else "prompt",
                               "user", loc, text=b.get("text"), ts=ts,
                               authorship=auth, visible=not marker,
                               basis=f"origin.kind={origin_kind!r} isMeta={auto}",
                               cwd=cwd, rel=rel_ids, max_chars=max_chars)
        elif t == "assistant" and msg is not None:
            model = msg.get("model")
            for b in msg.get("content") or []:
                if not isinstance(b, dict):
                    continue
                seq += 1
                bt = b.get("type")
                if bt == "thinking" or bt == "redacted_thinking":
                    yield frag("claude-code", store.name, ref.session_id, seq, "reasoning", "assistant.thinking", loc,
                               text=b.get("thinking") or b.get("data"), ts=ts, authorship="agent",
                               model=model, cwd=cwd, rel={**rel_ids, "message_id": msg.get("id")}, max_chars=max_chars)
                elif bt == "tool_use" or bt == "server_tool_use":
                    yield frag("claude-code", store.name, ref.session_id, seq, "tool_call", f"assistant.{bt}", loc,
                               text=json.dumps({"name": b.get("name"), "input": b.get("input")}, ensure_ascii=False),
                               ts=ts, authorship="agent", model=model, cwd=cwd,
                               rel={**rel_ids, "call_id": b.get("id"), "message_id": msg.get("id"), "tool": b.get("name")},
                               max_chars=max_chars)
                elif bt in ("text",):
                    yield frag("claude-code", store.name, ref.session_id, seq, "assistant", "assistant.text", loc,
                               text=b.get("text"), ts=ts, authorship="agent", model=model, cwd=cwd,
                               rel={**rel_ids, "message_id": msg.get("id")}, max_chars=max_chars)
                else:
                    yield frag("claude-code", store.name, ref.session_id, seq, "unknown", f"assistant.{bt}", loc,
                               text=b, ts=ts, model=model, cwd=cwd, rel=rel_ids, max_chars=max_chars)
        elif t in ("summary", "custom-title", "ai-title"):
            yield frag("claude-code", store.name, ref.session_id, seq, "metadata", t, loc,
                       text=rec.get("summary") or rec.get("customTitle") or rec.get("aiTitle"),
                       ts=ts, authorship="system", visible=False, basis="title/bookkeeping record",
                       cwd=cwd, rel=rel_ids, max_chars=max_chars)
        elif t in ("permission-mode", "mode"):
            yield frag("claude-code", store.name, ref.session_id, seq, "permission", t, loc,
                       text=rec.get("permissionMode") or rec.get("mode"), ts=ts, authorship="system",
                       cwd=cwd, rel=rel_ids, max_chars=max_chars)
        elif t is not None:
            yield frag("claude-code", store.name, ref.session_id, seq, "metadata", str(t), loc,
                       text={k: v for k, v in rec.items() if k not in ("message",)} if t else None,
                       ts=ts, authorship="system", visible=False, cwd=cwd, rel=rel_ids, max_chars=max_chars)


def _tool_result_text(block: dict[str, Any]) -> str:
    inner = block.get("content")
    if isinstance(inner, str):
        return inner
    if isinstance(inner, list):
        return "\n".join(str(b.get("text", "")) for b in inner if isinstance(b, dict))
    return json.dumps(inner, ensure_ascii=False)


# ---------------------------------------------------------------------------
# codex-cli
# ---------------------------------------------------------------------------

def codex_iter_sessions(store: Store) -> Iterator[SessionRef]:
    if store.kind == "sqlite":
        yield from _codex_sqlite_sessions(store)
        return
    if store.name == "history":
        yield from _codex_history_sessions(store)
        return
    for path in sorted(store.path.rglob("rollout-*.jsonl")):
        stats: dict[str, int] = {}
        meta = None
        first_ts = last_ts = None
        models: list[str] = []
        for line_no, rec in iter_jsonl(path, stats):
            if first_ts is None:
                first_ts = rec.get("timestamp")
            if rec.get("timestamp"):
                last_ts = rec["timestamp"]
            t = rec.get("type")
            payload = rec.get("payload") or {}
            if t == "session_meta" and meta is None:
                meta = payload
            elif t == "turn_context" and payload.get("model"):
                if payload["model"] not in models:
                    models.append(payload["model"])
        meta = meta or {}
        lineage = meta.get("source", {}).get("subagent", {}).get("thread_spawn") if isinstance(meta.get("source"), dict) else None
        parent = meta.get("parent_thread_id") or meta.get("forked_from_id") or (lineage or {}).get("parent_thread_id")
        yield SessionRef(
            "codex", store.name, str(meta.get("id") or meta.get("session_id") or path.stem),
            locator={"file": str(path)},
            cwd=meta.get("cwd"), created=first_ts or meta.get("timestamp"), updated=last_ts,
            models=models or ([meta["model_provider"]] if meta.get("model_provider") else []),
            parent=parent,
            agent=meta.get("agent_nickname") or meta.get("agent_path"),
            extra={k: meta[k] for k in ("originator", "cli_version") if meta.get(k)},
        )


def _codex_source_kind(src: Any) -> tuple[str, str | None, str | None, str | None]:
    """threads.source / session_meta.source → (kind, parent_thread, nickname, path)."""
    if isinstance(src, dict):
        sp = (src.get("subagent") or {}).get("thread_spawn") or {}
        if sp:
            return "subagent", sp.get("parent_thread_id"), sp.get("agent_nickname"), sp.get("agent_path")
        return "other", None, None, None
    if isinstance(src, str) and src.startswith("{"):
        try:
            return _codex_source_kind(json.loads(src))
        except json.JSONDecodeError:
            return src, None, None, None
    return str(src or ""), None, None, None


def _codex_sqlite_sessions(store: Store) -> Iterator[SessionRef]:
    try:
        conn = open_sqlite_ro(store.path)
    except sqlite3.Error as e:
        store.status, store.error = "unavailable", str(e)
        return
    try:
        if store.name.startswith("state:"):
            if not table_exists(conn, "threads"):
                store.status, store.error = "unsupported", "no threads table"
                return
            edges: dict[str, str] = {}
            if table_exists(conn, "thread_spawn_edges"):
                try:
                    for p, c in conn.execute("SELECT parent_thread_id, child_thread_id FROM thread_spawn_edges"):
                        edges[c] = p
                except sqlite3.Error:
                    pass
            wanted = ["id", "title", "cwd", "created_at", "updated_at_ms", "rollout_path",
                      "source", "model", "reasoning_effort", "git_branch", "archived",
                      "tokens_used", "preview", "first_user_message", "agent_nickname",
                      "model_provider", "originator", "project_id", "name"]
            have = table_columns(conn, "threads")
            cols = [c for c in wanted if c in have]
            for row in conn.execute(f"SELECT {', '.join(cols)} FROM threads"):
                rec = dict(zip(cols, row))
                src_kind, parent, nick, agent_path = _codex_source_kind(rec.get("source"))
                parent = parent or edges.get(rec["id"])
                title = (rec.get("title") or rec.get("name") or rec.get("preview")
                         or rec.get("first_user_message") or "")[:160] or None
                yield SessionRef(
                    "codex", store.name, rec["id"],
                    locator={"db": str(store.path), "table": "threads", "key": rec["id"]},
                    title=title, cwd=rec.get("cwd"), created=rec.get("created_at"),
                    updated=rec.get("updated_at_ms") or rec.get("created_at"),
                    models=[m for m in (rec.get("model"), rec.get("model_provider")) if m],
                    parent=parent, agent=rec.get("agent_nickname") or nick or agent_path,
                    extra={"rollout_path": rec.get("rollout_path"), "source": src_kind,
                           "effort": rec.get("reasoning_effort"), "git_branch": rec.get("git_branch"),
                           "archived": bool(rec.get("archived")), "tokens_used": rec.get("tokens_used"),
                           "originator": rec.get("originator"), "project_id": rec.get("project_id"),
                           "first_user_message": rec.get("first_user_message") or None},
                )
        elif store.name == "catalog":
            if not table_exists(conn, "local_thread_catalog"):
                store.status, store.error = "unsupported", "no local_thread_catalog table"
                return
            for row in conn.execute(
                "SELECT thread_id, display_title, cwd, source_created_at, source_updated_at, "
                "source_kind, git_branch, model_provider, project_id, conversation_origin, "
                "missing_candidate, host_id FROM local_thread_catalog"
            ):
                yield SessionRef(
                    "codex", "catalog", row[0],
                    locator={"db": str(store.path), "table": "local_thread_catalog", "key": row[0]},
                    title=row[1] or None, cwd=row[2], created=row[3], updated=row[4],
                    models=[row[7]] if row[7] else [],
                    extra={"source_kind": row[5], "git_branch": row[6], "project_id": row[8],
                           "conversation_origin": row[9], "host_id": row[11],
                           "missing_candidate": bool(row[10])},
                )
        elif store.name == "summaries":
            if not table_exists(conn, "thread_turn_summaries"):
                store.status, store.error = "unsupported", "no thread_turn_summaries table"
                return
            for row in conn.execute(
                "SELECT thread_id, summary, compact_summary, updated_at FROM thread_turn_summaries"
            ):
                yield SessionRef(
                    "codex", "summaries", row[0],
                    locator={"db": str(store.path), "table": "thread_turn_summaries", "key": row[0]},
                    title=(row[2] or (row[1] or "")[:80]) or None, updated=row[3],
                    extra={"cloud_summary": True},
                )
    except sqlite3.Error as e:
        store.status, store.error = "unavailable", str(e)
    finally:
        conn.close()


def _codex_history_sessions(store: Store) -> Iterator[SessionRef]:
    """~/.codex/history.jsonl — flat {session_id, ts, text} prompt log."""
    if not store.path.is_file():
        store.status = "missing"
        return
    stats: dict[str, int] = {}
    agg: dict[str, dict[str, Any]] = {}
    for _ln, rec in iter_jsonl(store.path, stats):
        sid = str(rec.get("session_id") or "")
        if not sid:
            continue
        e = agg.setdefault(sid, {"n": 0, "first": None, "last": None, "title": None})
        e["n"] += 1
        ts = rec.get("ts")
        if e["first"] is None:
            e["first"] = ts
            e["title"] = (rec.get("text") or "")[:80]
        if ts:
            e["last"] = ts
    for sid, e in agg.items():
        yield SessionRef(
            "codex", "history", sid,
            locator={"file": str(store.path)},
            title=e["title"], created=e["first"], updated=e["last"],
            extra={"prompt_count": e["n"]},
        )


def _find_codex_rollout(thread_id: str) -> Path | None:
    codex_home = Path(os.environ.get("CODEX_HOME") or (HOME / ".codex"))
    for base in (codex_home / "sessions", codex_home / "archived_sessions"):
        if not base.is_dir():
            continue
        hits = list(base.rglob(f"rollout-*-{thread_id}.jsonl"))
        if hits:
            return hits[0]
    return None


def _codex_db_only_fragments(store: Store, ref: SessionRef, max_chars: int, stats: dict[str, int]) -> Iterator[dict[str, Any]]:
    """No rollout file — emit what the index layer still knows."""
    seq = 0
    info = {"title": ref.title, "cwd": ref.cwd, **{k: v for k, v in ref.extra.items()
            if k not in ("rollout_path",)}}
    yield frag("codex", store.name, ref.session_id, seq, "metadata", "index_row", ref.locator,
               text=info, ts=ref.created, authorship="system", visible=False,
               basis="no local rollout file — index/catalog row only", max_chars=max_chars)
    first = ref.extra.get("first_user_message")
    if first:
        seq += 1
        yield frag("codex", store.name, ref.session_id, seq, "prompt", "threads.first_user_message",
                   ref.locator, text=first, ts=ref.created, authorship="unknown", visible=True,
                   basis="index-level first prompt preview; full transcript unavailable",
                   max_chars=max_chars)
    sdb = store.path if store.name == "summaries" else None
    if sdb is None:
        for cand in (store.path.parent / "codex-thread-summaries-dev.db",
                     store.path.parent / "sqlite" / "codex-thread-summaries-dev.db"):
            if cand.exists():
                sdb = cand
                break
    if sdb and sdb.exists():
        try:
            conn = open_sqlite_ro(sdb)
            row = conn.execute(
                "SELECT summary, compact_summary, updated_at FROM thread_turn_summaries WHERE thread_id=?",
                (ref.session_id,),
            ).fetchone()
            conn.close()
        except sqlite3.Error:
            row = None
        if row:
            seq += 1
            yield frag("codex", store.name, ref.session_id, seq, "metadata", "thread_turn_summaries",
                       {"db": str(sdb), "table": "thread_turn_summaries", "key": ref.session_id},
                       text=row[0], ts=row[2], authorship="system", visible=True,
                       basis="cloud/app-generated thread summary", max_chars=max_chars)


def codex_iter_fragments(store: Store, ref: SessionRef, max_chars: int, stats: dict[str, int]) -> Iterator[dict[str, Any]]:
    if store.name == "history":
        seq = 0
        for line_no, rec in iter_jsonl(store.path, stats):
            if str(rec.get("session_id")) != ref.session_id:
                continue
            seq += 1
            yield frag("codex", "history", ref.session_id, seq, "prompt", "history.entry",
                       {"file": str(store.path), "line": line_no},
                       text=rec.get("text"), ts=rec.get("ts"), authorship="unknown",
                       visible=True, basis="prompt log entry (no per-record authorship proof)",
                       rel={"sessionId": rec.get("session_id")}, max_chars=max_chars)
        return
    file = ref.locator.get("file")
    if not file:
        rollout = ref.extra.get("rollout_path") or _find_codex_rollout(ref.session_id)
        if rollout and Path(rollout).exists():
            file = str(rollout)
        else:
            yield from _codex_db_only_fragments(store, ref, max_chars, stats)
            return
    path = Path(file)
    seq = 0
    event_texts: set[str] = set()   # event-layer texts; response_item dups marked via membership
    pending_user_items: dict[str, int] = {}
    for line_no, rec in iter_jsonl(path, stats):
        seq += 1
        loc = {"file": str(path), "line": line_no}
        t = rec.get("type")
        ts = rec.get("timestamp")
        payload = rec.get("payload") if isinstance(rec.get("payload"), dict) else {}
        pt = payload.get("type")

        if t == "session_meta":
            lineage = (payload.get("source") or {}).get("subagent", {}).get("thread_spawn") if isinstance(payload.get("source"), dict) else None
            yield frag("codex", store.name, ref.session_id, seq, "metadata", "session_meta", loc,
                       text={k: payload.get(k) for k in ("id", "cwd", "originator", "cli_version", "model_provider", "thread_source", "agent_nickname", "agent_path") if payload.get(k)},
                       ts=ts, authorship="system", visible=False,
                       cwd=payload.get("cwd"),
                       rel={"parent_thread": payload.get("parent_thread_id") or payload.get("forked_from_id") or (lineage or {}).get("parent_thread_id")},
                       max_chars=max_chars)
        elif t == "turn_context":
            yield frag("codex", store.name, ref.session_id, seq, "boundary", "turn_context", loc,
                       text={k: payload.get(k) for k in ("turn_id", "model", "effort", "approval_policy", "collaboration_mode") if payload.get(k) is not None},
                       ts=ts, authorship="system", visible=False,
                       model=payload.get("model"), cwd=payload.get("cwd"),
                       rel={"turn_id": payload.get("turn_id")}, max_chars=max_chars)
        elif t == "response_item":
            if pt == "message":
                role = payload.get("role")
                text = _codex_message_text(payload)
                if role == "assistant":
                    kind, native, auth, vis, basis = "assistant", "response_item.assistant", "agent", True, "response layer"
                elif role in ("user", "developer"):
                    # verbatim human prompts are confirmed by event_msg.user_message;
                    # response-layer user text is bootstrap/context unless mirrored
                    kind = "prompt" if text in event_texts else "context"
                    native = "response_item." + role
                    auth = "unknown" if kind == "prompt" else "system"
                    vis = None if kind == "prompt" else False
                    basis = "mirrors event_msg.user_message" if kind == "prompt" else "response-layer injection (bootstrap/env/steer)"
                    if kind == "prompt":
                        pending_user_items[text] = seq
                else:
                    kind, native, auth, vis, basis = "metadata", f"response_item.{role}", "system", False, "non-conversational role"
                yield frag("codex", store.name, ref.session_id, seq, kind, native, loc,
                           text=text, ts=ts, authorship=auth, visible=vis, basis=basis,
                           cwd=None, rel={"item_id": payload.get("id")}, max_chars=max_chars)
            elif pt == "reasoning":
                yield frag("codex", store.name, ref.session_id, seq, "reasoning", "response_item.reasoning", loc,
                           text=(payload.get("summary") or [{}])[0].get("text") if payload.get("summary") else payload.get("content"),
                           ts=ts, authorship="agent", visible=False, rel={"item_id": payload.get("id")}, max_chars=max_chars)
            elif pt in ("function_call", "custom_tool_call", "tool_search_call"):
                yield frag("codex", store.name, ref.session_id, seq, "tool_call", f"response_item.{pt}", loc,
                           text=json.dumps({"name": payload.get("name"), "arguments": payload.get("arguments") or payload.get("input")}, ensure_ascii=False),
                           ts=ts, authorship="agent", visible=False,
                           rel={"call_id": payload.get("call_id"), "tool": payload.get("name")}, max_chars=max_chars)
            elif pt in ("function_call_output", "custom_tool_call_output", "tool_search_output"):
                yield frag("codex", store.name, ref.session_id, seq, "tool_result", f"response_item.{pt}", loc,
                           text=payload.get("output"), ts=ts, authorship="system", visible=False,
                           rel={"call_id": payload.get("call_id")}, max_chars=max_chars)
            else:
                yield frag("codex", store.name, ref.session_id, seq, "unknown", f"response_item.{pt}", loc,
                           text=payload, ts=ts, rel={"item_id": payload.get("id")}, max_chars=max_chars)
        elif t == "event_msg":
            if pt == "user_message":
                event_texts.add(payload.get("message") or "")
                yield frag("codex", store.name, ref.session_id, seq, "prompt", "event_msg.user_message", loc,
                           text=payload.get("message"), ts=ts, authorship="unknown", visible=True,
                           basis="verbatim submitted prompt (authorship not guaranteed — may be orchestrator-injected)",
                           rel={"turn_id": payload.get("turn_id")}, max_chars=max_chars)
            elif pt == "agent_message":
                yield frag("codex", store.name, ref.session_id, seq, "assistant", "event_msg.agent_message", loc,
                           text=payload.get("message"), ts=ts, authorship="agent", visible=True,
                           phase=payload.get("phase"), rel={"turn_id": payload.get("turn_id")}, max_chars=max_chars)
            elif pt in ("task_started", "task_complete", "turn_aborted"):
                yield frag("codex", store.name, ref.session_id, seq, "boundary", f"event_msg.{pt}", loc,
                           text={k: payload.get(k) for k in ("turn_id", "reason", "msg") if payload.get(k)},
                           ts=ts, authorship="system", visible=False,
                           status={"task_complete": "completed", "turn_aborted": "aborted"}.get(pt),
                           rel={"turn_id": payload.get("turn_id")}, max_chars=max_chars)
            elif pt == "guardian_assessment":
                yield frag("codex", store.name, ref.session_id, seq, "permission", "event_msg.guardian_assessment", loc,
                           text={k: payload.get(k) for k in ("target_item_id", "status", "decision_source") if payload.get(k)},
                           ts=ts, authorship="system", visible=False,
                           rel={"call_id": payload.get("target_item_id")}, max_chars=max_chars)
            elif pt in ("context_compacted",):
                yield frag("codex", store.name, ref.session_id, seq, "compaction", f"event_msg.{pt}", loc,
                           text=payload.get("message") or payload, ts=ts, authorship="system", visible=False,
                           max_chars=max_chars)
            else:
                yield frag("codex", store.name, ref.session_id, seq, "metadata", f"event_msg.{pt}", loc,
                           text=None if pt == "token_count" else payload, ts=ts, authorship="system",
                           visible=False, rel={"turn_id": payload.get("turn_id")}, max_chars=max_chars)
        elif t == "compacted":
            yield frag("codex", store.name, ref.session_id, seq, "compaction", "compacted", loc,
                       text=payload.get("message") or payload, ts=ts, authorship="system",
                       visible=False, basis="history compaction record", max_chars=max_chars)
        else:
            yield frag("codex", store.name, ref.session_id, seq, "metadata", str(t), loc,
                       text=payload or None, ts=ts, authorship="system", visible=False, max_chars=max_chars)


def _codex_message_text(payload: dict[str, Any]) -> str:
    parts = []
    for block in payload.get("content") or []:
        if isinstance(block, dict) and block.get("type") in ("input_text", "output_text", "text"):
            parts.append(str(block.get("text", "")))
    return "\n".join(p for p in parts if p)


# ---------------------------------------------------------------------------
# opencode — storage JSON tree + opencode.db sqlite
# ---------------------------------------------------------------------------

def _opencode_part_kind(part: dict[str, Any]) -> str:
    t = part.get("type")
    return {
        "text": "assistant", "reasoning": "reasoning", "tool": "tool_call",
        "step-start": "boundary", "step-finish": "boundary", "patch": "metadata",
        "subtask": "metadata", "file": "context", "agent": "metadata",
    }.get(str(t), "unknown")


def opencode_iter_sessions(store: Store) -> Iterator[SessionRef]:
    if store.name == "db":
        try:
            conn = open_sqlite_ro(store.path)
        except sqlite3.Error as e:
            store.status, store.error = "unavailable", str(e)
            return
        try:
            if not table_exists(conn, "session"):
                store.status, store.error = "unsupported", "no session table"
                return
            for row in conn.execute(
                "SELECT s.id, s.directory, s.title, s.time_created, s.time_updated, s.parent_id, s.agent, s.model, s.version, p.worktree "
                "FROM session s LEFT JOIN project p ON p.id = s.project_id"
            ):
                model = None
                try:
                    model = json.loads(row[7]).get("id") if row[7] else None
                except (json.JSONDecodeError, AttributeError):
                    model = row[7]
                yield SessionRef(
                    "opencode", "db", row[0],
                    locator={"table": "session", "key": row[0], "db": str(store.path)},
                    title=row[2], cwd=row[1] or row[9], created=row[3], updated=row[4],
                    parent=row[5], models=[m for m in (model,) if m],
                    extra={"agent": row[6], "version": row[8]},
                )
        except sqlite3.Error as e:
            store.status, store.error = "unavailable", str(e)
        finally:
            conn.close()
        return
    sess_root = store.path / "session"
    if not sess_root.is_dir():
        store.status = "missing"
        return
    for path in sorted(sess_root.rglob("ses_*.json")):
        data = read_json(path)
        if not isinstance(data, dict):
            continue
        time_block = data.get("time") or {}
        yield SessionRef(
            "opencode", "storage", str(data.get("id") or path.stem),
            locator={"file": str(path)},
            title=data.get("title"), cwd=data.get("directory"),
            created=time_block.get("created"), updated=time_block.get("updated"),
            parent=data.get("parentID"),
            extra={"agent": data.get("agent"), "version": data.get("version"), "projectID": data.get("projectID")},
        )


def opencode_iter_fragments(store: Store, ref: SessionRef, max_chars: int, stats: dict[str, int]) -> Iterator[dict[str, Any]]:
    seq = 0
    if store.name == "db":
        conn = open_sqlite_ro(store.path)
        try:
            messages = conn.execute(
                "SELECT id, time_created, data FROM message WHERE session_id=? ORDER BY time_created",
                (ref.session_id,),
            ).fetchall()
            parts = conn.execute(
                "SELECT id, message_id, time_created, data FROM part WHERE session_id=? ORDER BY time_created",
                (ref.session_id,),
            ).fetchall()
        finally:
            conn.close()
        parts_by_msg: dict[str, list[tuple[str, int, dict[str, Any]]]] = {}
        for pid, mid, ptime, pdata in parts:
            try:
                parts_by_msg.setdefault(mid, []).append((pid, ptime, json.loads(pdata)))
            except json.JSONDecodeError:
                stats["malformed"] = stats.get("malformed", 0) + 1
        for mid, mtime, mdata in messages:
            try:
                msg = json.loads(mdata)
            except json.JSONDecodeError:
                stats["malformed"] = stats.get("malformed", 0) + 1
                continue
            seq += 1
            loc = {"db": str(store.path), "table": "message", "key": mid}
            role = msg.get("role")
            model = msg.get("modelID") or (msg.get("model") or {}).get("modelID")
            provider = msg.get("providerID") or (msg.get("model") or {}).get("providerID")
            cwd = (msg.get("path") or {}).get("cwd")
            if role == "user":
                yield frag("opencode", "db", ref.session_id, seq, "prompt", "message.user", loc,
                           ts=mtime, authorship="human" if not msg.get("format") else "unknown",
                           visible=True, basis="role=user" + ("; format set → SDK/structured, authorship unproven" if msg.get("format") else ""),
                           model=model, provider=provider, cwd=cwd,
                           rel={"message_id": mid}, max_chars=max_chars)
            elif role == "assistant":
                seq += 0  # fragments come from parts; emit a boundary when finish is set
                if msg.get("finish"):
                    yield frag("opencode", "db", ref.session_id, seq, "boundary", f"message.finish.{msg['finish']}", loc,
                               ts=(msg.get("time") or {}).get("completed") or mtime, authorship="system",
                               status="completed" if msg["finish"] == "stop" else msg["finish"],
                               model=model, cwd=cwd, rel={"message_id": mid}, max_chars=max_chars)
            for pid, ptime, part in parts_by_msg.get(mid, []):
                seq += 1
                ploc = {"db": str(store.path), "table": "part", "key": pid}
                ptype = part.get("type")
                kind = _opencode_part_kind(part)
                if ptype == "text" and role == "user":
                    yield frag("opencode", "db", ref.session_id, seq, "prompt", "part.text(user)", ploc,
                               text=part.get("text"), ts=ptime, authorship="human", visible=True,
                               basis="text part of role=user message", cwd=cwd,
                               rel={"message_id": mid}, max_chars=max_chars)
                    continue
                if ptype == "tool":
                    st = part.get("state") or {}
                    yield frag("opencode", "db", ref.session_id, seq, "tool_call", "part.tool", ploc,
                               text=json.dumps({"tool": part.get("tool"), "input": st.get("input"), "status": st.get("status")}, ensure_ascii=False),
                               ts=ptime, authorship="agent", model=model, cwd=cwd,
                               rel={"call_id": part.get("callID"), "tool": part.get("tool")}, max_chars=max_chars)
                    if st.get("output") or st.get("error"):
                        seq += 1
                        yield frag("opencode", "db", ref.session_id, seq, "tool_result", "part.tool.output", ploc,
                                   text=st.get("output") or st.get("error"), ts=ptime, authorship="system",
                                   visible=False, rel={"call_id": part.get("callID")}, max_chars=max_chars)
                elif ptype == "subtask":
                    yield frag("opencode", "db", ref.session_id, seq, "metadata", "part.subtask", ploc,
                               text=part.get("description") or part.get("prompt"), ts=ptime,
                               authorship="agent", visible=False,
                               rel={"child_agent": part.get("agent")}, basis="subtask part — child session link",
                               max_chars=max_chars)
                else:
                    yield frag("opencode", "db", ref.session_id, seq, kind, f"part.{ptype}", ploc,
                               text=part.get("text") or part.get("output"), ts=ptime,
                               authorship="agent" if role == "assistant" else "system",
                               visible=(kind == "assistant"), model=model, cwd=cwd,
                               rel={"message_id": mid}, max_chars=max_chars)
        return
    # storage JSON tree
    msg_root = store.path / "message" / ref.session_id
    for mpath in sorted(msg_root.glob("msg_*.json")):
        msg = read_json(mpath)
        if not isinstance(msg, dict):
            continue
        seq += 1
        role = msg.get("role")
        loc = {"file": str(mpath)}
        model, provider = msg.get("modelID"), msg.get("providerID")
        cwd = (msg.get("path") or {}).get("cwd")
        if role == "user":
            yield frag("opencode", "storage", ref.session_id, seq, "prompt", "message.user", loc,
                       ts=(msg.get("time") or {}).get("created"),
                       authorship="human" if not msg.get("format") else "unknown",
                       visible=True, basis="role=user" + ("; format set" if msg.get("format") else ""),
                       cwd=cwd, rel={"message_id": msg.get("id")}, max_chars=max_chars)
        elif role == "assistant" and msg.get("finish"):
            yield frag("opencode", "storage", ref.session_id, seq, "boundary", f"message.finish.{msg['finish']}", loc,
                       ts=(msg.get("time") or {}).get("completed"), authorship="system",
                       status="completed" if msg["finish"] == "stop" else msg["finish"],
                       model=model, cwd=cwd, rel={"message_id": msg.get("id")}, max_chars=max_chars)
        part_root = store.path / "part" / str(msg.get("id"))
        for ppath in sorted(part_root.glob("prt_*.json")):
            part = read_json(ppath)
            if not isinstance(part, dict):
                continue
            seq += 1
            ptype = part.get("type")
            ploc = {"file": str(ppath)}
            if ptype == "text" and role == "user":
                yield frag("opencode", "storage", ref.session_id, seq, "prompt", "part.text(user)", ploc,
                           text=part.get("text"), ts=(part.get("time") or {}).get("start") if isinstance(part.get("time"), dict) else None,
                           authorship="human", visible=True, basis="text part of role=user message",
                           cwd=cwd, rel={"message_id": msg.get("id")}, max_chars=max_chars)
                continue
            if ptype == "tool":
                st = part.get("state") or {}
                yield frag("opencode", "storage", ref.session_id, seq, "tool_call", "part.tool", ploc,
                           text=json.dumps({"tool": part.get("tool"), "input": st.get("input"), "status": st.get("status")}, ensure_ascii=False),
                           ts=(st.get("time") or {}).get("start"), authorship="agent",
                           model=model, cwd=cwd, rel={"call_id": part.get("callID"), "tool": part.get("tool")},
                           max_chars=max_chars)
                if st.get("output") or st.get("error"):
                    seq += 1
                    yield frag("opencode", "storage", ref.session_id, seq, "tool_result", "part.tool.output", ploc,
                               text=st.get("output") or st.get("error"), ts=(st.get("time") or {}).get("end"),
                               authorship="system", visible=False, rel={"call_id": part.get("callID")},
                               max_chars=max_chars)
            elif ptype == "subtask":
                yield frag("opencode", "storage", ref.session_id, seq, "metadata", "part.subtask", ploc,
                           text=part.get("description") or part.get("prompt"),
                           authorship="agent", visible=False, rel={"child_agent": part.get("agent")},
                           basis="subtask part — child session link", max_chars=max_chars)
            else:
                kind = _opencode_part_kind(part)
                yield frag("opencode", "storage", ref.session_id, seq, kind, f"part.{ptype}", ploc,
                           text=part.get("text"), ts=(part.get("time") or {}).get("start") if isinstance(part.get("time"), dict) else None,
                           authorship="agent" if role == "assistant" else "system",
                           visible=(kind == "assistant"), model=model, cwd=cwd,
                           rel={"message_id": msg.get("id")}, max_chars=max_chars)


# ---------------------------------------------------------------------------
# grok-build
# ---------------------------------------------------------------------------

def grok_iter_sessions(store: Store) -> Iterator[SessionRef]:
    for proj in sorted(store.path.iterdir() if store.path.is_dir() else []):
        if not proj.is_dir():
            continue
        cwd = urllib.parse.unquote(proj.name)
        for sess in sorted(proj.iterdir()):
            if not sess.is_dir():
                continue
            summary = read_json(sess / "summary.json") or {}
            info = summary.get("info") or {}
            yield SessionRef(
                "grok", store.name, str(info.get("id") or sess.name),
                locator={"dir": str(sess)},
                title=summary.get("generated_title") or summary.get("session_summary"),
                cwd=info.get("cwd") or cwd,
                created=summary.get("created_at"), updated=summary.get("updated_at") or summary.get("last_active_at"),
                models=[summary["current_model_id"]] if summary.get("current_model_id") else [],
                extra={k: summary[k] for k in ("agent_name", "sandbox_profile", "reasoning_effort", "num_messages") if summary.get(k) is not None},
            )


def grok_iter_fragments(store: Store, ref: SessionRef, max_chars: int, stats: dict[str, int]) -> Iterator[dict[str, Any]]:
    sess_dir = Path(ref.locator["dir"])
    prompts: set[str] = set()
    for line_no, rec in iter_jsonl(sess_dir.parent / "prompt_history.jsonl", stats):
        if rec.get("session_id") == ref.session_id and rec.get("prompt"):
            prompts.add(rec["prompt"])
    seq = 0
    for line_no, rec in iter_jsonl(sess_dir / "chat_history.jsonl", stats):
        seq += 1
        loc = {"file": str(sess_dir / "chat_history.jsonl"), "line": line_no}
        t = rec.get("type")
        if t == "user":
            texts = [b.get("text", "") for b in rec.get("content") or [] if isinstance(b, dict) and b.get("type") == "text"]
            text = "\n".join(texts)
            bootstrap = "<user_info>" in text or text.lstrip().startswith("<rules")
            auto = any(m in text for m in AUTOCONTEXT_MARKERS)
            yield frag("grok", store.name, ref.session_id, seq,
                       "context" if (bootstrap or auto) else "prompt", "user", loc, text=text,
                       authorship="system" if (bootstrap or auto) else ("human" if text in prompts else "unknown"),
                       visible=not (bootstrap or auto),
                       basis=("bootstrap wrapper" if bootstrap else "auto-context marker" if auto else
                              "matches prompt_history verbatim" if text in prompts else "no verbatim confirmation"),
                       max_chars=max_chars)
        elif t == "assistant":
            yield frag("grok", store.name, ref.session_id, seq, "assistant", "assistant", loc,
                       text=rec.get("content"), authorship="agent", max_chars=max_chars)
            for call in rec.get("tool_calls") or []:
                seq += 1
                yield frag("grok", store.name, ref.session_id, seq, "tool_call", "assistant.tool_call", loc,
                           text=json.dumps({"name": call.get("name"), "arguments": call.get("arguments")}, ensure_ascii=False),
                           authorship="agent", visible=False,
                           rel={"call_id": call.get("id"), "tool": call.get("name")}, max_chars=max_chars)
        elif t == "reasoning":
            texts = [s.get("text", "") for s in rec.get("summary") or [] if isinstance(s, dict)]
            yield frag("grok", store.name, ref.session_id, seq, "reasoning", "reasoning", loc,
                       text="\n".join(texts) or "(encrypted reasoning)", authorship="agent", visible=False,
                       rel={"reasoning_id": rec.get("id")}, max_chars=max_chars)
        elif t == "tool_result":
            yield frag("grok", store.name, ref.session_id, seq, "tool_result", "tool_result", loc,
                       text=rec.get("content"), authorship="system", visible=False,
                       rel={"call_id": rec.get("tool_call_id")}, max_chars=max_chars)
        elif t == "backend_tool_call":
            kind = rec.get("kind") or {}
            yield frag("grok", store.name, ref.session_id, seq, "tool_call", "backend_tool_call", loc,
                       text=json.dumps(kind.get("action") or kind, ensure_ascii=False),
                       authorship="agent", visible=False, status=rec.get("status"),
                       rel={"tool": kind.get("tool_type"), "call_id": rec.get("id")}, max_chars=max_chars)
        elif t == "system":
            yield frag("grok", store.name, ref.session_id, seq, "context", "system", loc,
                       text=rec.get("content"), authorship="system", visible=False,
                       basis="system prompt record", max_chars=max_chars)
        else:
            yield frag("grok", store.name, ref.session_id, seq, "unknown", str(t), loc,
                       text=rec, max_chars=max_chars)


# ---------------------------------------------------------------------------
# devin-cli
# ---------------------------------------------------------------------------

def devin_iter_sessions(store: Store) -> Iterator[SessionRef]:
    if store.name == "transcripts":
        if not store.path.is_dir():
            store.status = "missing"
            return
        for path in sorted(store.path.glob("*.json")):
            data = read_json(path)
            if not isinstance(data, dict):
                continue
            agent = data.get("agent") or {}
            steps = data.get("steps") or []
            ts = [s.get("timestamp") for s in steps if isinstance(s, dict) and s.get("timestamp")]
            yield SessionRef(
                "devin", "transcripts", str(data.get("session_id") or path.stem),
                locator={"file": str(path)},
                cwd=None, created=min(ts) if ts else None, updated=max(ts) if ts else None,
                models=[agent["model_name"]] if agent.get("model_name") else [],
                extra={"agent_version": agent.get("version"), "exported": True},
            )
        return
    try:
        conn = open_sqlite_ro(store.path)
    except sqlite3.Error as e:
        store.status, store.error = "unavailable", str(e)
        return
    try:
        for row in conn.execute(
            "SELECT id, working_directory, model, agent_mode, created_at, last_activity_at, title, hidden, main_chain_id FROM sessions"
        ):
            yield SessionRef(
                "devin", "sessions.db", row[0],
                locator={"table": "sessions", "key": row[0], "db": str(store.path)},
                title=row[6], cwd=row[1], created=row[4], updated=row[5],
                models=[row[2]] if row[2] else [],
                hidden=bool(row[7]),
                extra={"agent_mode": row[3], "main_chain_id": row[8]},
            )
    except sqlite3.Error as e:
        store.status, store.error = "unavailable", str(e)
    finally:
        conn.close()


def devin_iter_fragments(store: Store, ref: SessionRef, max_chars: int, stats: dict[str, int]) -> Iterator[dict[str, Any]]:
    if store.name == "transcripts":
        path = Path(ref.locator["file"])
        data = read_json(path) or {}
        for seq, step in enumerate(data.get("steps") or [], 1):
            if not isinstance(step, dict):
                continue
            source = step.get("source")
            kind = {"user": "prompt", "agent": "assistant", "tool": "tool_result", "system": "context"}.get(str(source), "unknown")
            yield frag("devin", "transcripts", ref.session_id, seq, kind, f"step.{source}",
                       {"file": str(path), "step": step.get("step_id") or seq},
                       text=step.get("message"), ts=step.get("timestamp"),
                       authorship={"user": "unknown", "agent": "agent", "tool": "system", "system": "system"}.get(str(source), "unknown"),
                       visible=kind in ("prompt", "assistant"), max_chars=max_chars)
        return
    conn = open_sqlite_ro(store.path)
    try:
        rows = conn.execute(
            "SELECT row_id, node_id, parent_node_id, chat_message, created_at FROM message_nodes WHERE session_id=? ORDER BY node_id",
            (ref.session_id,),
        ).fetchall()
        heads: list[tuple] = []
        if table_exists(conn, "subagent_heads"):
            try:
                heads = conn.execute("SELECT * FROM subagent_heads WHERE session_id=?", (ref.session_id,)).fetchall()
            except sqlite3.Error:
                heads = []
    finally:
        conn.close()
    seq = 0
    for row_id, node_id, parent_id, blob, created in rows:
        seq += 1
        loc = {"db": str(store.path), "table": "message_nodes", "row_id": row_id, "node_id": node_id}
        try:
            msg = json.loads(blob)
        except json.JSONDecodeError:
            stats["malformed"] = stats.get("malformed", 0) + 1
            continue
        role = msg.get("role")
        rel = {"node_id": node_id, "parent_node_id": parent_id, "message_id": msg.get("message_id")}
        if role == "user":
            yield frag("devin", "sessions.db", ref.session_id, seq, "prompt", "message_nodes.user", loc,
                       text=msg.get("content"), ts=created, authorship="unknown", visible=True,
                       basis="role=user (may include orchestrator prompts)", rel=rel, max_chars=max_chars)
        elif role == "assistant":
            thinking = (msg.get("thinking") or {}).get("thinking")
            if thinking:
                yield frag("devin", "sessions.db", ref.session_id, seq, "reasoning", "message_nodes.thinking", loc,
                           text=thinking, ts=created, authorship="agent", visible=False, rel=rel, max_chars=max_chars)
                seq += 1
            if msg.get("content"):
                yield frag("devin", "sessions.db", ref.session_id, seq, "assistant", "message_nodes.assistant", loc,
                           text=msg.get("content"), ts=created, authorship="agent", visible=True, rel=rel,
                           status=(msg.get("metadata") or {}).get("finish_reason"), max_chars=max_chars)
                seq += 1
            for call in msg.get("tool_calls") or []:
                yield frag("devin", "sessions.db", ref.session_id, seq, "tool_call", "message_nodes.tool_call", loc,
                           text=json.dumps({"name": call.get("name"), "arguments": call.get("arguments")}, ensure_ascii=False),
                           ts=created, authorship="agent", visible=False,
                           rel={**rel, "call_id": call.get("id"), "tool": call.get("name")}, max_chars=max_chars)
                seq += 1
        elif role == "tool":
            yield frag("devin", "sessions.db", ref.session_id, seq, "tool_result", "message_nodes.tool", loc,
                       text=msg.get("content"), ts=created, authorship="system", visible=False, rel=rel,
                       max_chars=max_chars)
        elif role == "system":
            yield frag("devin", "sessions.db", ref.session_id, seq, "context", "message_nodes.system", loc,
                       text=msg.get("content"), ts=created, authorship="system", visible=False, rel=rel,
                       max_chars=max_chars)
        else:
            yield frag("devin", "sessions.db", ref.session_id, seq, "unknown", f"message_nodes.{role}", loc,
                       text=msg.get("content") or msg, ts=created, rel=rel, max_chars=max_chars)
    for head in heads:
        seq += 1
        yield frag("devin", "sessions.db", ref.session_id, seq, "metadata", "subagent_heads", 
                   {"db": str(store.path), "table": "subagent_heads"},
                   text=json.dumps(head[1:] if isinstance(head, tuple) else head, ensure_ascii=False, default=str),
                   authorship="system", visible=False, basis="subagent head record — child session linkage",
                   max_chars=max_chars)


# ---------------------------------------------------------------------------
# gemini-cli
# ---------------------------------------------------------------------------

def _gemini_projects_map(base: Path) -> dict[str, str]:
    data = read_json(base / "projects.json")
    out = {}
    if isinstance(data, dict):
        for cwd, slug in (data.get("projects") or {}).items():
            out[slug] = cwd
    return out


def gemini_iter_sessions(store: Store) -> Iterator[SessionRef]:
    if store.name == "projects-map":
        # informational store — sessions live under chats
        store.status = "ok" if store.path.exists() else "missing"
        return
    slug2cwd = _gemini_projects_map(store.path.parent)
    for path in sorted(store.path.rglob("chats/session-*.json")):
        proj_hash = path.relative_to(store.path).parts[0]
        data = read_json(path)
        if not isinstance(data, dict):
            continue
        msgs = data.get("messages") or []
        models = [m["model"] for m in msgs if isinstance(m, dict) and m.get("model")]
        yield SessionRef(
            "gemini", "chats", str(data.get("sessionId") or path.stem),
            locator={"file": str(path)},
            cwd=slug2cwd.get(proj_hash) or data.get("cwd"),
            created=data.get("startTime"), updated=data.get("lastUpdated"),
            models=models, extra={"project_hash": proj_hash},
        )


def gemini_iter_fragments(store: Store, ref: SessionRef, max_chars: int, stats: dict[str, int]) -> Iterator[dict[str, Any]]:
    path = Path(ref.locator["file"])
    data = read_json(path)
    if not isinstance(data, dict):
        stats["malformed"] = stats.get("malformed", 0) + 1
        return
    for seq, msg in enumerate(data.get("messages") or [], 1):
        if not isinstance(msg, dict):
            continue
        loc = {"file": str(path), "message_index": seq - 1}
        t = msg.get("type")
        ts = msg.get("timestamp")
        rel = {"message_id": msg.get("id")}
        if t == "user":
            yield frag("gemini", "chats", ref.session_id, seq, "prompt", "user", loc,
                       text=msg.get("content"), ts=ts, authorship="human", visible=True,
                       basis="type=user checkpoint record", rel=rel, max_chars=max_chars)
        elif t == "gemini":
            yield frag("gemini", "chats", ref.session_id, seq, "assistant", "gemini", loc,
                       text=msg.get("content") or msg.get("text"), ts=ts, authorship="agent",
                       model=msg.get("model"), rel=rel, max_chars=max_chars)
            for call in msg.get("toolCalls") or []:
                yield frag("gemini", "chats", ref.session_id, seq, "tool_call", "gemini.toolCalls", loc,
                           text=json.dumps(call, ensure_ascii=False), ts=ts, authorship="agent",
                           visible=False, rel={**rel, "tool": call.get("name")}, max_chars=max_chars)
        elif t in ("info", "error", "warning"):
            yield frag("gemini", "chats", ref.session_id, seq, "metadata", t, loc,
                       text=msg.get("content"), ts=ts, authorship="system", visible=True, rel=rel,
                       max_chars=max_chars)
        else:
            yield frag("gemini", "chats", ref.session_id, seq, "unknown", str(t), loc,
                       text=msg.get("content") or msg, ts=ts, rel=rel, max_chars=max_chars)


# ---------------------------------------------------------------------------
# claude-desktop (local agent mode)
# ---------------------------------------------------------------------------

def _claude_desktop_manifest(store: Store, meta_path: Path, data: dict[str, Any]) -> SessionRef:
    sid = str(data.get("sessionId") or data.get("session_id") or meta_path.stem)
    sess_dir = meta_path.with_suffix("")
    locator: dict[str, Any] = {"file": str(meta_path)}
    if sess_dir.is_dir():
        locator["dir"] = str(sess_dir)
    return SessionRef(
        "claude-desktop", store.name, sid,
        locator=locator,
        title=data.get("title") or (data.get("initialMessage") or "")[:80] or None,
        cwd=data.get("cwd") or data.get("workingDirectory"),
        created=data.get("createdAt") or data.get("created_at"),
        updated=data.get("lastActivityAt") or data.get("updatedAt") or data.get("updated_at"),
        models=[data["model"]] if data.get("model") else [],
        hidden=bool(data.get("isArchived")),
        extra={k: v for k, v in {
            "cli_session_id": data.get("cliSessionId"),
            "prior_cli_session_ids": data.get("priorCliSessionIds"),
            "effort": data.get("effort") or data.get("effortOverride"),
            "permission_mode": data.get("permissionMode"),
            "turns": data.get("completedTurns"),
            "process_name": data.get("processName"),
            "surface": "code-tab" if store.name == "code-sessions" else "cowork",
        }.items() if v is not None},
    )


def claude_desktop_iter_sessions(store: Store) -> Iterator[SessionRef]:
    if not store.path.is_dir():
        store.status = "missing"
        return
    for meta_path in sorted(store.path.rglob("local_*.json")):
        data = read_json(meta_path)
        if not isinstance(data, dict):
            continue
        yield _claude_desktop_manifest(store, meta_path, data)


def claude_desktop_iter_fragments(store: Store, ref: SessionRef, max_chars: int, stats: dict[str, int]) -> Iterator[dict[str, Any]]:
    seq = 0
    meta: dict[str, Any] = {}
    meta_file = ref.locator.get("file") or ref.locator.get("meta")
    if meta_file:
        data = read_json(Path(meta_file))
        if isinstance(data, dict):
            meta = data
            yield frag("claude-desktop", store.name, ref.session_id, seq, "metadata", "manifest", 
                       {"file": str(meta_file)},
                       text={k: meta.get(k) for k in
                             ("title", "model", "effort", "permissionMode", "completedTurns",
                              "cliSessionId", "cwd", "processName", "isArchived") if meta.get(k) is not None},
                       ts=meta.get("createdAt"), authorship="system", visible=False,
                       model=meta.get("model"), cwd=meta.get("cwd"),
                       basis="desktop session manifest", max_chars=max_chars)
    for prior in meta.get("priorCliSessionIds") or []:
        seq += 1
        yield frag("claude-desktop", store.name, ref.session_id, seq, "metadata", "prior_cli_session",
                   {"file": str(meta_file)} if meta_file else ref.locator,
                   text=None, authorship="system", visible=False,
                   basis="session continues an earlier CLI transcript",
                   rel={"cli_session_id": prior, "continued_from": True}, max_chars=max_chars)

    if store.name == "code-sessions":
        cli_sid = meta.get("cliSessionId")
        hits: list[Path] = []
        if cli_sid:
            claude_root = _root_override("claude-code") or (HOME / ".claude" / "projects")
            if claude_root.is_dir():
                hits = list(claude_root.rglob(f"{cli_sid}.jsonl"))
        if hits:
            sub = Store("claude-code", "via-claude-desktop", hits[0].parent, "jsonl_dir")
            sref = SessionRef("claude-code", "via-claude-desktop", cli_sid,
                              locator={"file": str(hits[0])})
            for f in claude_iter_fragments(sub, sref, max_chars, stats):
                seq += 1
                f["seq"] = seq
                f["harness"] = "claude-desktop"
                f["store"] = store.name
                f.setdefault("rel", {})["cli_session_id"] = cli_sid
                yield f
        else:
            seq += 1
            yield frag("claude-desktop", store.name, ref.session_id, seq, "metadata", "cli_transcript",
                       ref.locator, text={"cliSessionId": cli_sid},
                       authorship="system", visible=False,
                       basis="cliSessionId has no transcript under ~/.claude/projects",
                       rel={"cli_session_id": cli_sid}, max_chars=max_chars)
        return

    sess_dir = ref.locator.get("dir")
    if not sess_dir:
        seq += 1
        yield frag("claude-desktop", store.name, ref.session_id, seq, "metadata", "no_workdir",
                   ref.locator, text=None, authorship="system", visible=False,
                   basis="manifest has no sibling local_* working dir", max_chars=max_chars)
        return
    if meta.get("initialMessage"):
        seq += 1
        yield frag("claude-desktop", store.name, ref.session_id, seq, "prompt", "manifest.initialMessage",
                   {"file": str(meta_file)} if meta_file else {"dir": sess_dir},
                   text=meta["initialMessage"], ts=meta.get("createdAt"), authorship="human",
                   visible=True, basis="user-entered first message recorded in the manifest",
                   max_chars=max_chars)
    inner = Path(sess_dir) / ".claude" / "projects"
    if inner.is_dir():
        seq += 1
        yield frag("claude-desktop", store.name, ref.session_id, seq, "metadata", "inner_transcript",
                   {"dir": str(inner)}, text=None, authorship="system", visible=False,
                   basis="inner claude-code subprocess transcripts live under .claude/projects",
                   max_chars=max_chars)
    audit = Path(sess_dir) / "audit.jsonl"
    for line_no, rec in iter_jsonl(audit, stats):
        seq += 1
        loc = {"file": str(audit), "line": line_no}
        t = rec.get("type")
        ts = rec.get("timestamp") or rec.get("_audit_timestamp")
        sidechain = bool(rec.get("parent_tool_use_id"))
        rel = {"uuid": rec.get("uuid"), "parent_tool_use_id": rec.get("parent_tool_use_id")}
        msg = rec.get("message") if isinstance(rec.get("message"), dict) else None
        if t == "user" and msg is not None:
            content = msg.get("content")
            blocks = [{"type": "text", "text": content}] if isinstance(content, str) else [b for b in (content or []) if isinstance(b, dict)]
            for b in blocks:
                seq += 1
                bt = b.get("type")
                if bt == "tool_result":
                    yield frag("claude-desktop", store.name, ref.session_id, seq, "tool_result", "user.tool_result", loc,
                               text=_tool_result_text(b), ts=ts, authorship="system", visible=False,
                               rel={**rel, "call_id": b.get("tool_use_id")}, max_chars=max_chars)
                else:
                    marker = "<system-reminder>" in (b.get("text") or "")
                    yield frag("claude-desktop", store.name, ref.session_id, seq,
                               "context" if marker else "prompt", "user", loc, text=b.get("text"), ts=ts,
                               authorship="agent" if sidechain else ("system" if marker else "unknown"),
                               visible=False if (sidechain or marker) else True,
                               basis="parent_tool_use_id set → subagent record" if sidechain else None,
                               rel=rel, max_chars=max_chars)
        elif t == "assistant" and msg is not None:
            model = msg.get("model")
            for b in msg.get("content") or []:
                if not isinstance(b, dict):
                    continue
                seq += 1
                bt = b.get("type")
                kind = {"thinking": "reasoning", "text": "assistant", "tool_use": "tool_call"}.get(str(bt), "unknown")
                yield frag("claude-desktop", store.name, ref.session_id, seq, kind, f"assistant.{bt}", loc,
                           text=b.get("text") or b.get("thinking") or json.dumps({"name": b.get("name"), "input": b.get("input")}, ensure_ascii=False),
                           ts=ts, authorship="agent", visible=(kind == "assistant"), model=model,
                           rel={**rel, "call_id": b.get("id") if bt == "tool_use" else None, "tool": b.get("name")},
                           max_chars=max_chars)
        elif t == "system" and rec.get("subtype") in ("permission_request", "permission_response"):
            yield frag("claude-desktop", store.name, ref.session_id, seq, "permission",
                       f"system.{rec['subtype']}", loc,
                       text={k: rec.get(k) for k in
                             ("tool_name", "tool_use_id", "decision", "behavior", "suggestions")
                             if rec.get(k) is not None} or None,
                       ts=ts, authorship="system", visible=False,
                       basis="permission/approval event", rel=rel, max_chars=max_chars)
        elif t == "system" and rec.get("subtype") == "init":
            yield frag("claude-desktop", store.name, ref.session_id, seq, "metadata", "system.init", loc,
                       text={k: rec.get(k) for k in ("cliSessionId", "claude_code_version", "permissionMode", "cwd", "model") if rec.get(k)},
                       ts=ts, authorship="system", visible=False, model=rec.get("model"),
                       cwd=rec.get("cwd"), rel=rel, max_chars=max_chars)
        elif t == "result":
            yield frag("claude-desktop", store.name, ref.session_id, seq, "boundary", f"result.{rec.get('subtype')}", loc,
                       text=rec.get("result"), ts=ts, authorship="system", visible=False,
                       status=rec.get("subtype"), basis="turn boundary with cumulative usage",
                       rel=rel, max_chars=max_chars)
        else:
            yield frag("claude-desktop", store.name, ref.session_id, seq, "metadata", str(t), loc,
                       text=None, ts=ts, authorship="system", visible=False, rel=rel, max_chars=max_chars)


# ---------------------------------------------------------------------------
# cursor (state.vscdb)
# ---------------------------------------------------------------------------

def _folder_uri_to_path(uri: Any) -> str | None:
    """'file:///Users/x/proj' -> '/Users/x/proj'; plain paths pass through."""
    if not isinstance(uri, str) or not uri:
        return None
    if uri.startswith("file://"):
        from urllib.parse import unquote, urlparse
        return unquote(urlparse(uri).path) or None
    return uri


def cursor_iter_sessions(store: Store) -> Iterator[SessionRef]:
    try:
        conn = open_sqlite_ro(store.path)
    except sqlite3.Error as e:
        store.status, store.error = "unavailable", str(e)
        return
    try:
        if not table_exists(conn, "cursorDiskKV"):
            store.status = "empty"
            return
        headers: dict[str, dict[str, Any]] = {}
        if table_exists(conn, "composerHeaders"):
            try:
                for cid, value in conn.execute("SELECT composerId, value FROM composerHeaders"):
                    try:
                        headers[cid] = json.loads(value) if isinstance(value, str) else {}
                    except json.JSONDecodeError:
                        headers[cid] = {}
            except sqlite3.Error:
                pass
        ws_json = read_json(store.path.parent / "workspace.json") or {}
        ws_cwd = _folder_uri_to_path(ws_json.get("folder"))
        for (key, value) in conn.execute("SELECT key, value FROM cursorDiskKV WHERE key LIKE 'composerData:%'"):
            try:
                data = json.loads(value)
            except (json.JSONDecodeError, TypeError):
                continue
            cid = key.split(":", 1)[1]
            header = headers.get(cid) or {}
            ws = (header.get("workspaceIdentifier") or {})
            cwd = None
            if isinstance(ws, dict):
                uri = (ws.get("uri") or {})
                cwd = uri.get("fsPath") if isinstance(uri, dict) else None
            cwd = cwd or ws_cwd
            models = list((data.get("usageData") or {}).keys())
            yield SessionRef(
                "cursor", store.name, cid,
                locator={"db": str(store.path), "table": "cursorDiskKV", "key": key},
                title=data.get("name"), cwd=cwd,
                created=data.get("createdAt"), updated=data.get("lastUpdatedAt"),
                models=models,
                extra={"archived": header.get("isArchived"), "is_subagent": header.get("isSubagent")},
            )
    except sqlite3.Error as e:
        store.status, store.error = "unavailable", str(e)
    finally:
        conn.close()


def cursor_iter_fragments(store: Store, ref: SessionRef, max_chars: int, stats: dict[str, int]) -> Iterator[dict[str, Any]]:
    conn = open_sqlite_ro(store.path)
    try:
        key = ref.locator["key"]
        row = conn.execute("SELECT value FROM cursorDiskKV WHERE key=?", (key,)).fetchone()
        composer = json.loads(row[0]) if row else {}
        refs = composer.get("fullConversationHeadersOnly") or [
            {"bubbleId": b} for b in (composer.get("conversation") or [])
        ]
        out_rows = []
        for r in refs:
            bid = r.get("bubbleId")
            brow = conn.execute(
                "SELECT value FROM cursorDiskKV WHERE key=?", (f"bubbleId:{ref.session_id}:{bid}",)
            ).fetchone()
            if not brow:
                continue
            try:
                out_rows.append((bid, r.get("type"), json.loads(brow[0])))
            except json.JSONDecodeError:
                stats["malformed"] = stats.get("malformed", 0) + 1
    finally:
        conn.close()
    for seq, (bid, btype, bubble) in enumerate(out_rows, 1):
        loc = {"db": str(store.path), "table": "cursorDiskKV", "key": f"bubbleId:{ref.session_id}:{bid}"}
        if bubble.get("isThought"):
            yield frag("cursor", store.name, ref.session_id, seq, "reasoning", "bubble.thought", loc,
                       text=bubble.get("text"), authorship="agent", visible=False,
                       rel={"bubble_id": bid}, max_chars=max_chars)
            continue
        if btype == 1:
            yield frag("cursor", store.name, ref.session_id, seq, "prompt", "bubble.user", loc,
                       text=bubble.get("text"), authorship="human", visible=True,
                       basis="bubble type=1 (user)", rel={"bubble_id": bid}, max_chars=max_chars)
        elif btype == 2:
            yield frag("cursor", store.name, ref.session_id, seq, "assistant", "bubble.assistant", loc,
                       text=bubble.get("text"), authorship="agent", visible=True,
                       rel={"bubble_id": bid}, max_chars=max_chars)
        tool = bubble.get("toolFormerData")
        if isinstance(tool, dict) and tool.get("name"):
            yield frag("cursor", store.name, ref.session_id, seq, "tool_call", "bubble.toolFormerData", loc,
                       text=json.dumps({"name": tool.get("name"), "params": tool.get("params"), "status": tool.get("status")}, ensure_ascii=False),
                       authorship="agent", visible=False,
                       rel={"call_id": tool.get("toolCallId"), "tool": tool.get("name")}, max_chars=max_chars)
            if tool.get("result") is not None:
                yield frag("cursor", store.name, ref.session_id, seq, "tool_result", "bubble.toolFormerData.result", loc,
                           text=tool.get("result"), authorship="system", visible=False,
                           rel={"call_id": tool.get("toolCallId")}, max_chars=max_chars)


# ---------------------------------------------------------------------------
# qwen-code
# ---------------------------------------------------------------------------

QWEN_HUMAN_SUBTYPES = {None, "mid_turn_user_message"}
QWEN_NONHUMAN_SUBTYPES = {"notification", "cron"}


def qwen_iter_sessions(store: Store) -> Iterator[SessionRef]:
    if not store.path.is_dir():
        store.status = "missing"
        return
    for path in sorted(store.path.rglob("*.jsonl")):
        rel = path.relative_to(store.path).as_posix()
        stats: dict[str, int] = {}
        first_ts = last_ts = cwd = sid = None
        models: list[str] = []
        for line_no, rec in iter_jsonl(path, stats):
            if first_ts is None:
                first_ts = rec.get("timestamp")
            if rec.get("timestamp"):
                last_ts = rec["timestamp"]
            sid = sid or rec.get("sessionId") or rec.get("agentId")
            cwd = cwd or rec.get("cwd")
            if rec.get("model") and rec["model"] not in models:
                models.append(rec["model"])
        parent = None
        agent = None
        if "/subagents/" in rel:
            parent = rel.split("/subagents/")[1].split("/")[0]
            agent = path.stem
        yield SessionRef(
            "qwen-code", store.name, str(sid or path.stem),
            locator={"file": str(path)},
            cwd=cwd, created=first_ts, updated=last_ts, models=models,
            parent=parent, agent=agent,
            extra={"rel_path": rel},
        )


def qwen_iter_fragments(store: Store, ref: SessionRef, max_chars: int, stats: dict[str, int]) -> Iterator[dict[str, Any]]:
    path = Path(ref.locator["file"])
    sidechain = "/subagents/" in ref.extra.get("rel_path", "")
    seq = 0
    for line_no, rec in iter_jsonl(path, stats):
        seq += 1
        loc = {"file": str(path), "line": line_no}
        t, subtype = rec.get("type"), rec.get("subtype")
        ts, cwd, model = rec.get("timestamp"), rec.get("cwd"), rec.get("model")
        rel = {"uuid": rec.get("uuid"), "parent": rec.get("parentUuid"), "sessionId": rec.get("sessionId")}
        msg = rec.get("message") if isinstance(rec.get("message"), dict) else {}
        parts = msg.get("parts") or []
        if t == "user" and any(isinstance(p, dict) and p.get("functionResponse") for p in parts):
            text = "\n".join(
                json.dumps(p.get("functionResponse", {}).get("response"), ensure_ascii=False)
                for p in parts if isinstance(p, dict) and p.get("functionResponse")
            ) or json.dumps(rec.get("toolCallResult"), ensure_ascii=False)
            yield frag("qwen-code", store.name, ref.session_id, seq, "tool_result", "user.functionResponse", loc,
                       text=text, ts=ts, authorship="system", visible=False, cwd=cwd,
                       rel={**rel, "call_id": (rec.get("toolCallResult") or {}).get("callId")}, max_chars=max_chars)
        elif t == "user":
            if subtype in QWEN_HUMAN_SUBTYPES:
                auth, kind = ("agent" if sidechain else "human"), "prompt"
                basis = f"subtype={subtype or 'plain'}" + ("; subagent file → task prompt" if sidechain else "")
            elif subtype in QWEN_NONHUMAN_SUBTYPES:
                auth, kind = "system", "context"
                basis = f"subtype={subtype} (auto/scheduled)"
            else:
                auth, kind, basis = "unknown", "prompt", f"unrecognized subtype={subtype!r}"
            text = "\n".join(str(p.get("text", "")) for p in parts if isinstance(p, dict) and p.get("text"))
            yield frag("qwen-code", store.name, ref.session_id, seq, kind, f"user.{subtype or 'plain'}", loc,
                       text=text, ts=ts, authorship=auth, visible=(kind == "prompt"),
                       basis=basis, cwd=cwd, rel=rel, max_chars=max_chars)
        elif t == "assistant":
            for p in parts:
                if not isinstance(p, dict):
                    continue
                seq += 1
                if p.get("functionCall"):
                    fc = p["functionCall"]
                    yield frag("qwen-code", store.name, ref.session_id, seq, "tool_call", "assistant.functionCall", loc,
                               text=json.dumps({"name": fc.get("name"), "args": fc.get("args")}, ensure_ascii=False),
                               ts=ts, authorship="agent", model=model, cwd=cwd,
                               rel={**rel, "call_id": fc.get("id"), "tool": fc.get("name")}, max_chars=max_chars)
                elif p.get("thought") or p.get("type") == "thought":
                    yield frag("qwen-code", store.name, ref.session_id, seq, "reasoning", "assistant.thought", loc,
                               text=p.get("text"), ts=ts, authorship="agent", model=model, cwd=cwd,
                               rel=rel, max_chars=max_chars)
                else:
                    yield frag("qwen-code", store.name, ref.session_id, seq, "assistant", "assistant.text", loc,
                               text=p.get("text"), ts=ts, authorship="agent", model=model, cwd=cwd,
                               rel=rel, max_chars=max_chars)
        elif t == "tool_result":
            text = json.dumps(rec.get("toolCallResult"), ensure_ascii=False)
            yield frag("qwen-code", store.name, ref.session_id, seq, "tool_result", "tool_result", loc,
                       text=text, ts=ts, authorship="system", visible=False, cwd=cwd,
                       rel={**rel, "call_id": (rec.get("toolCallResult") or {}).get("callId")}, max_chars=max_chars)
        elif t == "system":
            yield frag("qwen-code", store.name, ref.session_id, seq, "metadata", f"system.{subtype}", loc,
                       text=None, ts=ts, authorship="system", visible=False, cwd=cwd, rel=rel, max_chars=max_chars)
        else:
            yield frag("qwen-code", store.name, ref.session_id, seq, "unknown", f"{t}.{subtype}", loc,
                       text=rec, ts=ts, cwd=cwd, rel=rel, max_chars=max_chars)


# ---------------------------------------------------------------------------
# kimi-code
# ---------------------------------------------------------------------------

KIMI_ORIGIN_HUMAN = {"user"}
KIMI_ORIGIN_NONHUMAN = {"system_trigger", "background_task", "subagent"}


def kimi_iter_sessions(store: Store) -> Iterator[SessionRef]:
    if not store.path.is_dir():
        store.status = "missing"
        return
    index: dict[str, str] = {}
    for _ln, rec in iter_jsonl(store.path.parent / "session_index.jsonl", {}):
        if rec.get("sessionId") and rec.get("workDir"):
            index[str(rec["sessionId"])] = rec["workDir"]
    for state_path in sorted(store.path.rglob("state.json")):
        state = read_json(state_path)
        sess_dir = state_path.parent
        sid = sess_dir.name
        if not isinstance(state, dict):
            state = {}
        yield SessionRef(
            "kimi-code", store.name, sid,
            locator={"dir": str(sess_dir)},
            title=state.get("title"),
            cwd=state.get("workDir") or index.get(sid),
            created=state.get("createdAt"), updated=state.get("updatedAt"),
            parent=state.get("forkedFrom"),
            extra={"lastPrompt": state.get("lastPrompt"), "agents": list((state.get("agents") or {}).keys())},
        )


def kimi_iter_fragments(store: Store, ref: SessionRef, max_chars: int, stats: dict[str, int]) -> Iterator[dict[str, Any]]:
    sess_dir = Path(ref.locator["dir"])
    merged: list[tuple[float, int, Path, int, dict[str, Any]]] = []
    wire_files = sorted(sess_dir.glob("agents/*/wire.jsonl"))
    for order, wpath in enumerate(wire_files):  # 'main' first, then subagents
        wstats: dict[str, int] = {}
        for line_no, rec in iter_jsonl(wpath, wstats):
            stats.update({k: stats.get(k, 0) + v for k, v in wstats.items()})
            wstats.clear()
            merged.append((ts_epoch(rec.get("time")) or 0.0, 0 if wpath.parent.name == "main" else 1, wpath, line_no, rec))
    merged.sort(key=lambda x: (x[0], x[1], x[3]))
    seen_prompt_texts: set[str] = set()
    seq = 0
    for _t, _ord, wpath, line_no, rec in merged:
        seq += 1
        agent_id = wpath.parent.name
        loc = {"file": str(wpath), "line": line_no, "agent": agent_id}
        t = rec.get("type")
        ts = rec.get("time")
        rel = {"agent": agent_id, "turn_id": None}
        if t in ("turn.prompt", "turn.steer"):
            origin = ((rec.get("origin") or {}).get("kind"))
            text = "\n".join(str(i.get("text", "")) for i in (rec.get("input") or []) if isinstance(i, dict))
            seen_prompt_texts.add(text)
            if origin in KIMI_ORIGIN_HUMAN:
                auth = "human"
            elif origin in KIMI_ORIGIN_NONHUMAN:
                auth = "agent" if origin == "subagent" else "system"
            else:
                auth = "unknown"
            yield frag("kimi-code", store.name, ref.session_id, seq, "prompt", t, loc,
                       text=text, ts=ts, authorship=auth, visible=auth == "human",
                       basis=f"origin.kind={origin!r}", rel=rel, max_chars=max_chars)
        elif t == "context.append_message":
            msg = rec.get("message") or {}
            texts = "\n".join(str(c.get("text", "")) for c in (msg.get("content") or []) if isinstance(c, dict))
            yield frag("kimi-code", store.name, ref.session_id, seq, "context", t, loc,
                       text=texts, ts=ts, authorship="system", visible=False,
                       basis="duplicate layer of turn.prompt (kept for provenance)", rel=rel,
                       max_chars=max_chars)
        elif t == "context.append_loop_event":
            ev = rec.get("event") or {}
            et = ev.get("type")
            rel = {**rel, "turn_id": ev.get("turnId"), "step": ev.get("step")}
            if et == "content.part":
                part = ev.get("part") or {}
                pt = part.get("type")
                if pt == "tool.call" or part.get("toolCallId") and part.get("name"):
                    yield frag("kimi-code", store.name, ref.session_id, seq, "tool_call", "loop.tool.call", loc,
                               text=json.dumps({"name": part.get("name"), "args": part.get("arguments") or part.get("args")}, ensure_ascii=False),
                               ts=ts, authorship="agent",
                               rel={**rel, "call_id": part.get("toolCallId") or part.get("id"), "tool": part.get("name")},
                               max_chars=max_chars)
                elif pt == "tool.result":
                    yield frag("kimi-code", store.name, ref.session_id, seq, "tool_result", "loop.tool.result", loc,
                               text=part.get("result") or part.get("output"), ts=ts, authorship="system",
                               visible=False, rel={**rel, "call_id": part.get("toolCallId")}, max_chars=max_chars)
                else:
                    kind = "reasoning" if pt == "think" else "assistant"
                    yield frag("kimi-code", store.name, ref.session_id, seq, kind, f"loop.part.{pt}", loc,
                               text=part.get("text") or part.get("think"), ts=ts, authorship="agent",
                               visible=(kind == "assistant"), rel=rel, max_chars=max_chars)
            elif et in ("step.begin", "step.end"):
                yield frag("kimi-code", store.name, ref.session_id, seq, "boundary", f"loop.{et}", loc,
                           text=None if et == "step.begin" else json.dumps({"finishReason": ev.get("finishReason"), "usage": ev.get("usage")}, ensure_ascii=False),
                           ts=ts, authorship="system", visible=False,
                           status=ev.get("finishReason") if et == "step.end" else None,
                           rel=rel, max_chars=max_chars)
            else:
                yield frag("kimi-code", store.name, ref.session_id, seq, "metadata", f"loop.{et}", loc,
                       text=ev, ts=ts, authorship="system", visible=False, rel=rel, max_chars=max_chars)
        elif t == "permission.set_mode":
            yield frag("kimi-code", store.name, ref.session_id, seq, "permission", t, loc,
                       text=rec.get("mode"), ts=ts, authorship="system", visible=False, rel=rel, max_chars=max_chars)
        else:
            yield frag("kimi-code", store.name, ref.session_id, seq, "metadata", str(t), loc,
                       text=None if t in ("usage.record", "llm.request") else rec, ts=ts,
                       authorship="system", visible=False, rel=rel, max_chars=max_chars)


# ---------------------------------------------------------------------------
# omp
# ---------------------------------------------------------------------------

def omp_iter_sessions(store: Store) -> Iterator[SessionRef]:
    if not store.path.is_dir():
        store.status = "missing"
        return
    for path in sorted(store.path.rglob("*.jsonl")):
        stats: dict[str, int] = {}
        first_ts = last_ts = cwd = title = sid = None
        models: list[str] = []
        for line_no, rec in iter_jsonl(path, stats):
            ts = rec.get("timestamp") or rec.get("updatedAt")
            if first_ts is None:
                first_ts = ts
            if ts:
                last_ts = ts
            t = rec.get("type")
            if t == "session":
                sid = sid or rec.get("id")
                cwd = cwd or rec.get("cwd")
                title = title or rec.get("title")
            elif t in ("title", "title_change") and rec.get("title"):
                title = rec["title"]
            elif t == "model_change" and rec.get("model"):
                models.append(rec["model"])
        yield SessionRef(
            "omp", store.name, str(sid or path.stem),
            locator={"file": str(path)}, title=title, cwd=cwd,
            created=first_ts, updated=last_ts, models=models,
        )


def omp_iter_fragments(store: Store, ref: SessionRef, max_chars: int, stats: dict[str, int]) -> Iterator[dict[str, Any]]:
    path = Path(ref.locator["file"])
    seq = 0
    for line_no, rec in iter_jsonl(path, stats):
        seq += 1
        loc = {"file": str(path), "line": line_no}
        t = rec.get("type")
        ts = rec.get("timestamp") or rec.get("updatedAt")
        rel = {"id": rec.get("id"), "parent": rec.get("parentId")}
        if t == "message":
            msg = rec.get("message") or {}
            role = msg.get("role")
            attribution = msg.get("attribution")
            if role == "user":
                yield frag("omp", store.name, ref.session_id, seq, "prompt", "message.user", loc,
                           text="\n".join(str(c.get("text", "")) for c in (msg.get("content") or []) if isinstance(c, dict)),
                           ts=ts, authorship="agent" if attribution == "agent" else "human",
                           visible=attribution != "agent",
                           basis=f"attribution={attribution!r}", model=msg.get("model"),
                           rel=rel, max_chars=max_chars)
            elif role in ("toolResult", "tool"):
                yield frag("omp", store.name, ref.session_id, seq, "tool_result", "message.toolResult", loc,
                           text="\n".join(str(c.get("text", "")) for c in (msg.get("content") or []) if isinstance(c, dict)),
                           ts=ts, authorship="system", visible=False,
                           rel={**rel, "call_id": msg.get("toolCallId"), "tool": msg.get("toolName")},
                           max_chars=max_chars)
            else:
                for c in msg.get("content") or []:
                    if not isinstance(c, dict):
                        continue
                    seq += 1
                    ct = c.get("type")
                    if ct == "toolCall":
                        yield frag("omp", store.name, ref.session_id, seq, "tool_call", "message.toolCall", loc,
                                   text=json.dumps({"name": c.get("name"), "arguments": c.get("arguments") or c.get("partialArgs")}, ensure_ascii=False),
                                   ts=ts, authorship="agent", model=msg.get("model"),
                                   rel={**rel, "call_id": c.get("id"), "tool": c.get("name")}, max_chars=max_chars)
                    elif ct == "thinking":
                        yield frag("omp", store.name, ref.session_id, seq, "reasoning", "message.thinking", loc,
                                   text=c.get("thinking"), ts=ts, authorship="agent", visible=False,
                                   model=msg.get("model"), rel=rel, max_chars=max_chars)
                    else:
                        yield frag("omp", store.name, ref.session_id, seq, "assistant", f"message.{ct}", loc,
                                   text=c.get("text"), ts=ts, authorship="agent", model=msg.get("model"),
                                   status=msg.get("stopReason"), rel=rel, max_chars=max_chars)
        elif t == "compaction":
            yield frag("omp", store.name, ref.session_id, seq, "compaction", "compaction", loc,
                       text=rec.get("summary") or rec.get("shortSummary"), ts=ts, authorship="system",
                       visible=False, rel=rel, max_chars=max_chars)
        elif t in ("session", "title", "title_change", "model_change", "thinking_level_change"):
            yield frag("omp", store.name, ref.session_id, seq, "metadata", t, loc,
                       text=rec.get("title") or rec.get("model") or rec.get("thinkingLevel"),
                       ts=ts, authorship="system", visible=False,
                       model=rec.get("model") if t == "model_change" else None,
                       rel=rel, max_chars=max_chars)
        elif t == "custom":
            ct = rec.get("customType")
            data = rec.get("data") or {}
            kind = "tool_call" if ct == "tool_execution_start" else "metadata"
            yield frag("omp", store.name, ref.session_id, seq, kind, f"custom.{ct}", loc,
                       text=data.get("intent") or data.get("args") or rec.get("text"), ts=ts,
                       authorship="agent" if kind == "tool_call" else "system", visible=False,
                       rel={**rel, "call_id": data.get("toolCallId"), "tool": data.get("toolName")},
                       max_chars=max_chars)
        else:
            yield frag("omp", store.name, ref.session_id, seq, "metadata", str(t), loc,
                       text=None, ts=ts, authorship="system", visible=False, rel=rel, max_chars=max_chars)


# ---------------------------------------------------------------------------
# consilium's own delegate runs
# ---------------------------------------------------------------------------

def consilium_iter_sessions(store: Store) -> Iterator[SessionRef]:
    if not store.path.is_dir():
        store.status = "missing"
        return
    for run_dir in sorted(store.path.iterdir()):
        meta = read_json(run_dir / "meta.json")
        if not isinstance(meta, dict):
            continue
        handle = meta.get("session_handle") or {}
        yield SessionRef(
            "consilium", "runs", str(meta.get("run_id") or run_dir.name),
            locator={"dir": str(run_dir)},
            title=(meta.get("task") or "")[:120] or None,
            cwd=meta.get("cwd"), created=meta.get("launched_at") or meta.get("started_at"),
            updated=meta.get("finished_at") or meta.get("last_event_at"),
            models=[meta["model"]] if meta.get("model") else [],
            extra={
                "agent_id": meta.get("agent_id"), "backend": meta.get("backend"),
                "effort": meta.get("effort"), "status": meta.get("status"),
                "native_session": handle.get("thread_id"),
            },
        )


def consilium_iter_fragments(store: Store, ref: SessionRef, max_chars: int, stats: dict[str, int]) -> Iterator[dict[str, Any]]:
    run_dir = Path(ref.locator["dir"])
    norm_dir = run_dir / "normalized"
    files = sorted(norm_dir.glob("*.jsonl")) if norm_dir.is_dir() else sorted(run_dir.glob("normalized/*.jsonl"))
    if not files:
        art = read_json(run_dir / "meta.json") or {}
        stats["unreadable"] = stats.get("unreadable", 0) + 1
        if art.get("artifacts_dir"):
            norm_dir = Path(art["artifacts_dir"]) / "normalized"
            files = sorted(norm_dir.glob("*.jsonl")) if norm_dir.is_dir() else []
    seq = 0
    for npath in files:
        for line_no, rec in iter_jsonl(npath, stats):
            seq += 1
            t = rec.get("type")
            loc = {"file": str(npath), "line": line_no}
            if t in ("run_started",):
                yield frag("consilium", "runs", ref.session_id, seq, "metadata", t, loc,
                           text={k: rec.get(k) for k in ("agent", "backend", "model", "effort", "mode") if rec.get(k)},
                           ts=rec.get("ts") or rec.get("timestamp"), authorship="system", visible=False,
                           max_chars=max_chars)
            elif t in ("steer", "user", "prompt"):
                yield frag("consilium", "runs", ref.session_id, seq, "prompt", t, loc,
                           text=rec.get("text") or rec.get("prompt") or rec.get("data"),
                           ts=rec.get("ts") or rec.get("timestamp"), authorship="agent",
                           visible=False, basis="orchestrator steer/prompt", max_chars=max_chars)
            elif t in ("tool", "tool_call"):
                yield frag("consilium", "runs", ref.session_id, seq, "tool_call", t, loc,
                           text=json.dumps({"name": rec.get("name"), "chunks": rec.get("chunks")}, ensure_ascii=False),
                           ts=rec.get("ts") or rec.get("timestamp"), authorship="agent", visible=False,
                           rel={"tool": rec.get("name")}, max_chars=max_chars)
            elif t in ("text", "answering", "answer", "message"):
                yield frag("consilium", "runs", ref.session_id, seq, "assistant", t, loc,
                           text=rec.get("text") or rec.get("data"), ts=rec.get("ts") or rec.get("timestamp"),
                           authorship="agent", visible=False, max_chars=max_chars)
            elif t in ("end", "run_finished", "completed"):
                yield frag("consilium", "runs", ref.session_id, seq, "boundary", t, loc,
                           text=rec.get("data"), ts=rec.get("ts") or rec.get("timestamp"),
                           authorship="system", status=rec.get("status"), max_chars=max_chars)
            else:
                yield frag("consilium", "runs", ref.session_id, seq, "metadata", str(t), loc,
                           text=rec.get("data") or rec.get("text"), ts=rec.get("ts") or rec.get("timestamp"),
                           authorship="system", visible=False, max_chars=max_chars)


# ---------------------------------------------------------------------------
# dispatch tables
# ---------------------------------------------------------------------------

READERS = {
    "claude-code": (claude_iter_sessions, claude_iter_fragments),
    "codex": (codex_iter_sessions, codex_iter_fragments),
    "opencode": (opencode_iter_sessions, opencode_iter_fragments),
    "grok": (grok_iter_sessions, grok_iter_fragments),
    "devin": (devin_iter_sessions, devin_iter_fragments),
    "gemini": (gemini_iter_sessions, gemini_iter_fragments),
    "claude-desktop": (claude_desktop_iter_sessions, claude_desktop_iter_fragments),
    "cursor": (cursor_iter_sessions, cursor_iter_fragments),
    "qwen-code": (qwen_iter_sessions, qwen_iter_fragments),
    "kimi-code": (kimi_iter_sessions, kimi_iter_fragments),
    "omp": (omp_iter_sessions, omp_iter_fragments),
    "consilium": (consilium_iter_sessions, consilium_iter_fragments),
}


def resolve_harnesses(raw: str | None) -> list[str]:
    if not raw:
        return list(ALL_HARNESSES)
    out = []
    for part in raw.split(","):
        part = part.strip()
        if part and part not in READERS:
            raise SystemExit(f"unknown harness: {part!r} (known: {', '.join(ALL_HARNESSES)})")
        if part:
            out.append(part)
    return out


def selected_stores(harnesses: list[str], store_filter: str | None = None) -> list[Store]:
    out: list[Store] = []
    for h in harnesses:
        for s in stores_for(h):
            if store_filter and store_filter not in s.name and store_filter not in str(s.path):
                continue
            out.append(s)
    return out


def iter_all_sessions(store: Store, cwd: str | None, since: float | None, until: float | None) -> Iterator[SessionRef]:
    if store.status != "ok":
        return
    iter_sessions, _ = READERS[store.harness]
    try:
        for ref in iter_sessions(store):
            if ref.matches(cwd, since, until):
                yield ref
    except (OSError, sqlite3.Error) as e:
        store.status, store.error = "unavailable", str(e)


def iter_all_fragments(store: Store, ref: SessionRef, max_chars: int, stats: dict[str, int]) -> Iterator[dict[str, Any]]:
    _, iter_fragments = READERS[store.harness]
    try:
        yield from iter_fragments(store, ref, max_chars, stats)
    except (OSError, sqlite3.Error) as e:
        store.status, store.error = "unavailable", str(e)


def in_scope(fragment: dict[str, Any], scope: str) -> bool:
    kinds = SCOPES.get(scope)
    return kinds is None or fragment.get("kind") in kinds


def in_window(fragment: dict[str, Any], since: float | None, until: float | None) -> bool:
    if since is None and until is None:
        return True
    epoch = ts_epoch(fragment.get("ts"))
    if epoch is None:
        return since is None  # undated fragments only surface when no lower bound set
    if since is not None and epoch < since:
        return False
    if until is not None and epoch > until:
        return False
    return True


def emit(obj: dict[str, Any]) -> None:
    print(json.dumps(obj, ensure_ascii=False, default=str))


def coverage_summary(stores: list[Store], scanned: int, matched: int, stats: dict[str, int], *, truncated: bool = False) -> dict[str, Any]:
    store_report = [s.as_dict() | {"sessions_scanned": None} for s in stores]
    return {
        "_summary": True,
        "stores": store_report,
        "sessions_scanned": scanned,
        "fragments_emitted": matched,
        "malformed_records": stats.get("malformed", 0),
        "truncated_tail_files": stats.get("truncated_tail", 0),
        "unreadable_files": stats.get("unreadable", 0),
        "scan_complete": not truncated and all(s.status != "unavailable" for s in stores),
        "note": "empty result means: no matches AND scan_complete — check stores[].status for missing/unavailable",
    }


# ---------------------------------------------------------------------------
# commands
# ---------------------------------------------------------------------------

def cmd_roots(args: argparse.Namespace) -> int:
    stores = selected_stores(resolve_harnesses(args.agent), getattr(args, "store", None))
    for s in stores:
        emit(s.as_dict())
    emit({"_summary": True, "stores_total": len(stores),
          "available": sum(1 for s in stores if s.status == "ok"),
          "evidence_levels": {h: HARNESS_EVIDENCE[h] for h in resolve_harnesses(args.agent)}})
    return EXIT_OK


def cmd_list(args: argparse.Namespace) -> int:
    harnesses = resolve_harnesses(args.agent)
    stores = selected_stores(harnesses, getattr(args, "store", None))
    since, until = parse_time_bound(args.since), parse_time_bound(args.until)
    scanned = emitted = 0
    stats: dict[str, int] = {}
    for store in stores:
        for ref in iter_all_sessions(store, args.cwd, since, until):
            scanned += 1
            if args.limit and emitted >= args.limit:
                break
            emit(ref.as_dict())
            emitted += 1
    emit(coverage_summary(stores, scanned, emitted, stats))
    return EXIT_OK if all(s.status != "unavailable" for s in stores) else EXIT_PARTIAL


def cmd_grep(args: argparse.Namespace) -> int:
    harnesses = resolve_harnesses(args.agent)
    stores = selected_stores(harnesses, getattr(args, "store", None))
    since, until = parse_time_bound(args.since), parse_time_bound(args.until)
    if args.regex:
        pattern = re.compile(args.pattern, re.IGNORECASE if args.ignore_case else 0)
        match = lambda t: bool(pattern.search(t))
    else:
        needle = args.pattern if not args.ignore_case else args.pattern.lower()
        match = (lambda t: needle in t) if not args.ignore_case else (lambda t: needle in t.lower())
    scanned = emitted = 0
    stats: dict[str, int] = {}
    truncated = False
    for store in stores:
        if store.status != "ok":
            continue
        for ref in iter_all_sessions(store, args.cwd, None, None):
            scanned += 1
            for f in iter_all_fragments(store, ref, args.max_chars, stats):
                if not in_scope(f, args.scope) or not in_window(f, since, until):
                    continue
                text = f.get("text")
                if text is None or not match(text):
                    continue
                f["session"] = {k: v for k, v in ref.as_dict().items() if k in ("session_id", "title", "cwd", "created", "parent", "agent")}
                emit(f)
                emitted += 1
                if args.limit and emitted >= args.limit:
                    truncated = True
                    break
            if truncated:
                break
        if truncated:
            break
    emit(coverage_summary(stores, scanned, emitted, stats, truncated=truncated))
    return EXIT_OK if all(s.status != "unavailable" for s in stores) else EXIT_PARTIAL


def fast_resolve(store: Store, query_id: str) -> SessionRef | None:
    """Direct locator construction — avoids a full store scan when the id maps
    onto a known file/row name pattern. Returns None to fall back to scan."""
    p = store.path
    if store.harness == "claude-code":
        f = p / f"{query_id}.jsonl"
        if f.exists():
            return SessionRef("claude-code", store.name, query_id, locator={"file": str(f)})
    elif store.harness == "codex":
        if store.kind == "sqlite":
            table = ("threads" if store.name.startswith("state:")
                     else {"catalog": "local_thread_catalog",
                           "summaries": "thread_turn_summaries"}.get(store.name))
            if not table:
                return None
            idcol = "id" if table == "threads" else "thread_id"
            try:
                conn = open_sqlite_ro(p)
                row = conn.execute(f"SELECT 1 FROM {table} WHERE {idcol}=? LIMIT 1", (query_id,)).fetchone()
                conn.close()
            except sqlite3.Error:
                row = None
            if row:
                return SessionRef("codex", store.name, query_id,
                                  locator={"db": str(p), "table": table, "key": query_id})
            return None
        if store.name == "history":
            stats: dict[str, int] = {}
            for _ln, rec in iter_jsonl(p, stats):
                if str(rec.get("session_id")) == query_id:
                    return SessionRef("codex", "history", query_id, locator={"file": str(p)})
            return None
        hits = list(p.rglob(f"rollout-*-{query_id}.jsonl"))
        if len(hits) == 1:
            return SessionRef("codex", store.name, query_id, locator={"file": str(hits[0])})
    elif store.harness == "grok":
        hits = [d for d in p.glob(f"*/{query_id}") if d.is_dir()]
        if len(hits) == 1:
            summary = read_json(hits[0] / "summary.json") or {}
            info = summary.get("info") or {}
            return SessionRef("grok", store.name, query_id, locator={"dir": str(hits[0])},
                              cwd=info.get("cwd"), title=summary.get("generated_title"))
    elif store.harness == "opencode":
        if store.name == "db":
            try:
                conn = open_sqlite_ro(p)
                row = conn.execute(
                    "SELECT s.id, s.directory, s.title, s.time_created, s.time_updated, s.parent_id, s.agent, s.model, s.version, p.worktree "
                    "FROM session s LEFT JOIN project p ON p.id = s.project_id WHERE s.id=?", (query_id,)
                ).fetchone()
                conn.close()
            except sqlite3.Error:
                row = None
            if row:
                return SessionRef("opencode", "db", row[0],
                                  locator={"table": "session", "key": row[0], "db": str(p)},
                                  title=row[2], cwd=row[1] or row[9], created=row[3], updated=row[4],
                                  parent=row[5], extra={"agent": row[6], "version": row[8]})
        else:
            hits = list(p.glob(f"session/*/{query_id}.json"))
            if len(hits) == 1:
                data = read_json(hits[0]) or {}
                return SessionRef("opencode", "storage", query_id, locator={"file": str(hits[0])},
                                  title=data.get("title"), cwd=data.get("directory"))
    elif store.harness == "devin":
        if store.name == "sessions.db":
            try:
                conn = open_sqlite_ro(p)
                row = conn.execute(
                    "SELECT id, working_directory, model, agent_mode, created_at, last_activity_at, title, hidden, main_chain_id FROM sessions WHERE id=?",
                    (query_id,),
                ).fetchone()
                conn.close()
            except sqlite3.Error:
                row = None
            if row:
                return SessionRef("devin", "sessions.db", row[0],
                                  locator={"table": "sessions", "key": row[0], "db": str(p)},
                                  title=row[6], cwd=row[1], created=row[4], updated=row[5],
                                  models=[row[2]] if row[2] else [], hidden=bool(row[7]),
                                  extra={"agent_mode": row[3], "main_chain_id": row[8]})
        else:
            f = p / f"{query_id}.json"
            if f.exists():
                return SessionRef("devin", "transcripts", query_id, locator={"file": str(f)})
    elif store.harness == "gemini" and store.name == "chats":
        hits = list(p.rglob(f"chats/*{query_id[:8]}*.json"))
        if len(hits) == 1:
            return SessionRef("gemini", "chats", query_id, locator={"file": str(hits[0])})
    elif store.harness == "claude-desktop":
        sid = query_id if query_id.startswith("local_") else f"local_{query_id}"
        metas = list(p.rglob(f"{sid}.json"))
        if len(metas) == 1:
            loc = {"file": str(metas[0])}
            d = metas[0].with_suffix("")
            if d.is_dir():
                loc["dir"] = str(d)
            return SessionRef("claude-desktop", store.name, sid, locator=loc)
    elif store.harness == "cursor" and store.kind == "sqlite":
        try:
            conn = open_sqlite_ro(p)
            row = conn.execute("SELECT value FROM cursorDiskKV WHERE key=?", (f"composerData:{query_id}",)).fetchone()
            conn.close()
        except sqlite3.Error:
            row = None
        if row:
            return SessionRef("cursor", store.name, query_id,
                              locator={"db": str(p), "table": "cursorDiskKV", "key": f"composerData:{query_id}"})
    elif store.harness == "qwen-code":
        hits = list(p.rglob(f"chats/{query_id}.jsonl"))
        if len(hits) == 1:
            return SessionRef("qwen-code", store.name, query_id, locator={"file": str(hits[0])})
    elif store.harness == "kimi-code":
        hits = [d for d in p.glob(f"*/{query_id}") if d.is_dir()]
        if len(hits) == 1:
            return SessionRef("kimi-code", store.name, query_id, locator={"dir": str(hits[0])})
    elif store.harness == "omp":
        hits = list(p.rglob(f"{query_id}.jsonl"))
        if len(hits) == 1:
            return SessionRef("omp", store.name, query_id, locator={"file": str(hits[0])})
    elif store.harness == "consilium":
        d = p / query_id
        if d.is_dir():
            return SessionRef("consilium", "runs", query_id, locator={"dir": str(d)})
    return None


def _hydrate_ref(store: Store, ref: SessionRef) -> SessionRef:
    """Fill title/cwd/models/etc. on a fast-resolved ref by scanning only the
    narrowest enclosing scope (the file's own directory, not the whole store).
    For sqlite stores there is no narrower scope — match on session_id."""
    if ref.title and ref.cwd:
        return ref
    f = ref.locator.get("file")
    scope = store if not f else Store(store.harness, store.name, Path(f).parent, store.kind)
    try:
        for r in READERS[store.harness][0](scope):
            if (r.locator.get("file") != f) if f else (r.session_id != ref.session_id):
                continue
            for key in ("title", "cwd", "created", "updated", "parent", "agent", "hidden"):
                val = getattr(r, key)
                if val is not None:
                    setattr(ref, key, val)
            if r.models:
                ref.models = r.models
            ref.extra.update(r.extra)
            break
    except (OSError, sqlite3.Error):
        pass
    return ref


def _resolve_session(harnesses: list[str], query: str, store_filter: str | None = None) -> tuple[Store, SessionRef]:
    """Address forms: 'harness:session-id', bare session-id (must be unique),
    or --file path handled by caller."""
    harness_hint, _, sid = query.partition(":")
    if sid and harness_hint in READERS:
        harnesses = [harness_hint]
        query_id = sid
    else:
        query_id = query
    fast: list[tuple[Store, SessionRef]] = []
    for store in selected_stores(harnesses, store_filter):
        if store.status != "ok":
            continue
        ref = fast_resolve(store, query_id)
        if ref is not None:
            fast.append((store, _hydrate_ref(store, ref)))
    unique_fast = {(r.harness, r.session_id) for _s, r in fast}
    if len(unique_fast) == 1:
        return fast[0]
    candidates: list[tuple[Store, SessionRef]] = []
    for store in selected_stores(harnesses, store_filter):
        if store.status != "ok":
            continue
        for ref in iter_all_sessions(store, None, None, None):
            if ref.session_id == query_id or ref.session_id.endswith(query_id) or Path(ref.session_id).name == query_id:
                candidates.append((store, ref))
    if not candidates:
        # substring fallback
        for store in selected_stores(harnesses, store_filter):
            if store.status != "ok":
                continue
            for ref in iter_all_sessions(store, None, None, None):
                if query_id in ref.session_id:
                    candidates.append((store, ref))
    if not candidates:
        raise SystemExit(f"session not found: {query!r}")
    unique = {(c[1].harness, c[1].session_id) for c in candidates}
    if len(unique) > 1:
        lines = "; ".join(f"{r.harness}:{r.session_id} (store {s.name})" for s, r in candidates[:8])
        raise SystemExit(f"ambiguous session id {query!r} → {lines}. Qualify as harness:session-id and/or pass --store.")
    # Same session visible through several layers (e.g. codex rollout + state
    # index + catalog): prefer the canonical content layer over index rows.
    def _rank(item: tuple[Store, SessionRef]) -> int:
        s, r = item
        if r.locator.get("file") and not r.locator.get("dir"):
            return 0
        if r.extra.get("rollout_path"):
            return 1
        return 2
    return min(candidates, key=_rank)


def cmd_show(args: argparse.Namespace) -> int:
    harnesses = resolve_harnesses(args.agent)
    stats: dict[str, int] = {}
    since, until = parse_time_bound(args.since), parse_time_bound(args.until)
    if args.file:
        path = Path(args.file).expanduser()
        store, ref = _store_for_file(path)
    else:
        store, ref = _resolve_session(harnesses, args.session, getattr(args, "store", None))
    emit({"_session": ref.as_dict()})
    emitted = 0
    target = args.around  # seq of the fragment to center the window on
    context = args.context
    window: list[dict[str, Any]] = []
    after_remaining: int | None = None
    for f in iter_all_fragments(store, ref, args.max_chars, stats):
        if not in_scope(f, args.scope) or not in_window(f, since, until):
            continue
        if target is None:
            emit(f)
            emitted += 1
            if args.limit and emitted >= args.limit:
                break
            continue
        if after_remaining is not None:
            emit(f)
            emitted += 1
            after_remaining -= 1
            if after_remaining <= 0:
                break
            continue
        if f.get("seq") == target:
            for prev in window:
                emit(prev)
                emitted += 1
            emit(f)
            emitted += 1
            after_remaining = context
        else:
            window.append(f)
            if len(window) > context:
                window.pop(0)
    emit(coverage_summary([store], 1, emitted, stats))
    return EXIT_OK


def _store_for_file(path: Path) -> tuple[Store, SessionRef]:
    """Sniff a single file's harness by structure, then build a one-file store."""
    if not path.exists():
        raise SystemExit(f"no such file: {path}")
    if path.suffix in (".db", ".sqlite", ".sqlite3", ".vscdb"):
        # choose by table shape
        try:
            conn = open_sqlite_ro(path)
            try:
                if table_exists(conn, "message_nodes"):
                    store = Store("devin", "sessions.db", path, "sqlite")
                    sid = _pick_single_session(conn, "sessions", "id")
                    return store, SessionRef("devin", "sessions.db", sid, locator={"table": "sessions", "key": sid, "db": str(path)})
                if table_exists(conn, "cursorDiskKV"):
                    store = Store("cursor", "custom", path, "sqlite")
                    sid = _pick_single_session(conn, "cursorDiskKV", "key", like="composerData:%")
                    return store, SessionRef("cursor", "custom", sid.split(":", 1)[-1], locator={"db": str(path), "table": "cursorDiskKV", "key": sid})
                if table_exists(conn, "session"):
                    store = Store("opencode", "db", path, "sqlite")
                    sid = _pick_single_session(conn, "session", "id")
                    return store, SessionRef("opencode", "db", sid, locator={"table": "session", "key": sid, "db": str(path)})
            finally:
                conn.close()
        except sqlite3.Error as e:
            raise SystemExit(f"cannot open sqlite read-only: {e}")
        raise SystemExit(f"unrecognized sqlite store: {path}")
    # JSON / JSONL: peek first records
    first = path.open("r", encoding="utf-8", errors="replace").read(65536)
    try:
        obj = json.loads(first)
        if isinstance(obj, dict) and "messages" in obj and ("sessionId" in obj or "projectHash" in obj):
            store = Store("gemini", "chats", path.parent.parent.parent, "json_dir")
            return store, SessionRef("gemini", "chats", str(obj.get("sessionId") or path.stem), locator={"file": str(path)})
        if isinstance(obj, dict) and "steps" in obj and "session_id" in obj:
            store = Store("devin", "transcripts", path.parent, "json_dir")
            return store, SessionRef("devin", "transcripts", str(obj.get("session_id") or path.stem), locator={"file": str(path)})
    except json.JSONDecodeError:
        pass
    stats: dict[str, int] = {}
    records = list(iter_jsonl(path, stats))[:5]
    types = {r.get("type") for _ln, r in records}
    if "session_meta" in types or "turn_context" in types or "response_item" in types:
        store = Store("codex", "custom", path.parent, "jsonl_dir")
        sid = next((r.get("payload", {}).get("id") for _ln, r in records if r.get("type") == "session_meta"), path.stem)
        return store, SessionRef("codex", "custom", str(sid), locator={"file": str(path)})
    if types & {"turn.prompt", "turn.steer", "context.append_loop_event"}:
        store = Store("kimi-code", "custom", path.parent.parent, "session_dirs")
        return store, SessionRef("kimi-code", "custom", path.parent.parent.name, locator={"dir": str(path.parent.parent)})
    if {"uuid", "parentUuid"} <= set().union(*[set(r.keys()) for _ln, r in records], set()):
        harness = "qwen-code" if any("parts" in (r.get("message") or {}) for _ln, r in records) else "claude-code"
        store = Store(harness, "custom", path.parent, "jsonl_dir")
        sid = next((r.get("sessionId") for _ln, r in records if r.get("sessionId")), path.stem)
        return store, SessionRef(harness, "custom", str(sid), locator={"file": str(path)})
    if any(r.get("chat_history") or r.get("type") in ("backend_tool_call",) for _ln, r in records):
        store = Store("grok", "custom", path.parent.parent, "session_dirs")
        return store, SessionRef("grok", "custom", path.parent.name, locator={"dir": str(path.parent)})
    raise SystemExit(f"could not identify harness of {path} — pass --agent and session id instead")


def _pick_single_session(conn: sqlite3.Connection, table: str, col: str, like: str | None = None) -> str:
    if like:
        rows = conn.execute(f"SELECT {col} FROM {table} WHERE {col} LIKE ? LIMIT 2", (like,)).fetchall()
    else:
        rows = conn.execute(f"SELECT {col} FROM {table} LIMIT 2").fetchall()
    if len(rows) != 1:
        raise SystemExit(f"--file on a multi-session {table} store needs an explicit session id, not implemented: use list first")
    return str(rows[0][0])


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def _add_common(p: argparse.ArgumentParser) -> None:
    p.add_argument("-a", "--agent", help="comma-separated harness slugs (default: all)")
    p.add_argument("--store", help="only stores whose name or path contains this substring")
    p.add_argument("--cwd", help="only sessions whose recorded cwd contains this substring")
    p.add_argument("--since", help="ISO-8601 or epoch; naive timestamps = local time")
    p.add_argument("--until", help="ISO-8601 or epoch")
    p.add_argument("--scope", choices=sorted(SCOPES), default="convo",
                   help="convo=prompt+assistant (default) | prompts | assistant | tools | reasoning | system | all")
    p.add_argument("--limit", type=int, default=200, help="max fragments/sessions emitted (0=unbounded)")
    p.add_argument("--max-chars", type=int, default=400, help="per-fragment text cap (0=full)")


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="consilium sessions",
        description="Search and navigate local coding-agent session histories (read-only).",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("roots", help="show detected history stores and availability")
    p.add_argument("-a", "--agent")
    p.add_argument("--store", help="only stores whose name or path contains this substring")

    p = sub.add_parser("list", help="list sessions (id, title, cwd, dates, models)")
    _add_common(p)

    p = sub.add_parser("grep", help="literal/regex search over decoded fragment text")
    _add_common(p)
    p.add_argument("pattern")
    p.add_argument("-i", "--ignore-case", action="store_true")
    p.add_argument("--regex", action="store_true", help="treat pattern as a regex")

    p = sub.add_parser("show", help="dump one session's fragments with locators")
    _add_common(p)
    p.add_argument("session", nargs="?", help="harness:session-id or unique id substring")
    p.add_argument("--file", help="read a single session file/db directly (harness auto-detected)")
    p.add_argument("--around", type=int, metavar="SEQ", help="emit a window around the fragment with this seq")
    p.add_argument("--context", type=int, default=10, help="fragments on each side of --around (default 10)")

    args = parser.parse_args()
    args.max_chars = getattr(args, "max_chars", 400) or 0
    if getattr(args, "limit", 200) == 0:
        args.limit = 0
    handlers = {"roots": cmd_roots, "list": cmd_list, "grep": cmd_grep, "show": cmd_show}
    try:
        return handlers[args.command](args)
    except BrokenPipeError:
        return EXIT_OK
    except SystemExit:
        raise
    except Exception as e:  # never leak a traceback as the only diagnostic
        print(json.dumps({"_summary": True, "error": f"{type(e).__name__}: {e}"}, ensure_ascii=False), file=sys.stderr)
        return EXIT_FAILED


if __name__ == "__main__":
    sys.exit(main())
