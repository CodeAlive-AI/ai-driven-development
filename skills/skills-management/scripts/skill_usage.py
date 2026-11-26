#!/usr/bin/env python3
"""Incremental, resource-bounded skill usage telemetry across porch harnesses.

Supports two read-only modes:
- ``fast`` (<300 ms): flat prompt history logs + porch's existing SQLite index
  (opened ``mode=ro`` with NO sync lock).
- ``deep`` (windowed by ``--since``, default 30d): mtime/SQL-pruned scan of native
  transcripts with incremental caching in ``~/.cache/skills-management/usage-v1.json``.

Counts distinct canonical sessions (splitting explicit human triggers from agent/tool
activations) and excludes bulk-audit sessions reading >8 distinct ``SKILL.md`` files.
Stdlib-only Python 3.11+.
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
import sys
import time
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import quote

try:
    from compression import zstd as _stdlib_zstd  # Python 3.14+
except ImportError:
    _stdlib_zstd = None


SKILL_MD_PATH_RE = re.compile(r"(?:^|[/\\])([a-z0-9][a-z0-9._-]*)[/\\]SKILL\.md\b", re.IGNORECASE)
SLASH_TRIGGER_RE = re.compile(r"(?:^|[\s(\"'`])/(?P<name>[a-z0-9][a-z0-9_-]{1,63})(?=$|[\s.,:;!?)\"'`])")
DOLLAR_TRIGGER_RE = re.compile(r"(?:^|[\s(\"'`])\$(?P<name>[a-z0-9][a-z0-9_-]{1,63})(?=$|[\s.,:;!?)\"'`])")
AT_TRIGGER_RE = re.compile(r"(?:^|[\s(\"'`])@(?P<name>[a-z0-9][a-z0-9_-]{1,63})(?=$|[\s.,:;!?)\"'`])")
USER_REQ_RE = re.compile(r"<USER_REQUEST>\s*(.*?)\s*</USER_REQUEST>", re.DOTALL)
BULK_AUDIT_SKILL_THRESHOLD = 8


@dataclass
class SkillUsageStat:
    name: str
    total_sessions: int = 0
    explicit_sessions: int = 0
    agent_sessions: int = 0
    last_used_ts: float | None = None
    last_used_iso: str | None = None
    harnesses: dict[str, int] = field(default_factory=dict)


def parse_since(since: str | None, *, default_days: int | None = None) -> float | None:
    """Parse ``30d``, ``24h``, ``YYYY-MM-DD``, or ``all`` into a UTC epoch timestamp."""
    if not since:
        if default_days is None:
            return None
        return time.time() - default_days * 86400.0
    text = since.strip().lower()
    if text in ("all", "none", "*"):
        return None
    m = re.fullmatch(r"(\d+)([dhw])", text)
    if m:
        num = int(m.group(1))
        unit = {"h": 3600, "d": 86400, "w": 7 * 86400}[m.group(2)]
        return time.time() - num * unit
    try:
        dt = datetime.fromisoformat(since.strip().replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.timestamp()
    except ValueError:
        if default_days is not None:
            return time.time() - default_days * 86400.0
        return None


def _parse_ts(raw) -> float | None:
    """Normalize epoch seconds/ms or ISO timestamp strings to UTC epoch seconds."""
    if raw is None or raw == "":
        return None
    if isinstance(raw, (int, float)):
        val = float(raw)
        if val > 1e12:
            val /= 1000.0
        return val if val > 0 else None
    if isinstance(raw, str):
        s = raw.strip()
        if not s:
            return None
        if s.isdigit():
            return _parse_ts(int(s))
        try:
            dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.timestamp()
        except ValueError:
            return None
    return None


def _iso_utc(ts: float | None) -> str | None:
    if ts is None:
        return None
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")


def default_cache_path(home: Path | None = None) -> Path:
    """Return private disposable cache path ``~/.cache/skills-management/usage-v1.json``."""
    base = home or Path.home()
    xdg = os.environ.get("XDG_CACHE_HOME", "").strip()
    cache_root = Path(xdg).expanduser() if (xdg and home is None) else (base / ".cache")
    return cache_root / "skills-management" / "usage-v1.json"


def resolve_porch_index_db(home: Path | None = None) -> Path | None:
    """Locate porch's ``index-v1.sqlite`` without importing or locking porch."""
    candidates: list[Path] = []
    if env_dir := os.environ.get("PORCH_SESSIONS_INDEX_DIR", "").strip():
        candidates.append(Path(env_dir).expanduser() / "index-v1.sqlite")
    if steer_dir := os.environ.get("PORCH_STEER_DIR", "").strip():
        candidates.append(Path(steer_dir).expanduser().parent / "sessions-index" / "index-v1.sqlite")
    base = home or Path.home()
    if sys.platform == "darwin":
        candidates.append(base / "Library" / "Caches" / "pragmatic-orchestration" / "sessions-index" / "index-v1.sqlite")
    xdg = os.environ.get("XDG_CACHE_HOME", "").strip()
    if xdg and home is None:
        candidates.append(Path(xdg).expanduser() / "pragmatic-orchestration" / "sessions-index" / "index-v1.sqlite")
    candidates.append(base / ".cache" / "pragmatic-orchestration" / "sessions-index" / "index-v1.sqlite")
    if os.name == "nt":
        if local := os.environ.get("LOCALAPPDATA", "").strip():
            candidates.append(Path(local) / "pragmatic-orchestration" / "sessions-index" / "index-v1.sqlite")
    for cand in candidates:
        if cand.is_file():
            return cand
    return None


def _open_ro_sqlite(db_path: Path) -> sqlite3.Connection | None:
    """Open SQLite strictly read-only with tight page-cache & mmap caps."""
    if not db_path.is_file():
        return None
    try:
        conn = sqlite3.connect(f"file:{quote(str(db_path))}?mode=ro", uri=True, timeout=2.0)
        conn.execute("PRAGMA query_only=ON")
        conn.execute("PRAGMA cache_size=-4000")
        conn.execute("PRAGMA mmap_size=0")
        return conn
    except sqlite3.Error:
        return None


def _extract_prompt_triggers(text: str, known: set[str]) -> set[str]:
    """Extract explicit ``/skill``, ``$skill``, and ``@skill`` triggers present in ``known``."""
    if not text:
        return set()
    hits: set[str] = set()
    for regex in (SLASH_TRIGGER_RE, DOLLAR_TRIGGER_RE, AT_TRIGGER_RE):
        for m in regex.finditer(text):
            name = m.group("name")
            if name in known:
                hits.add(name)
    return hits


def _extract_skill_md_reads(text: str, known: set[str]) -> set[str]:
    if not text or "SKILL.md" not in text:
        return set()
    hits: set[str] = set()
    for m in SKILL_MD_PATH_RE.finditer(text):
        name = m.group(1)
        if name in known:
            hits.add(name)
    return hits


def _record_hit(
    sessions: dict[str, dict],
    canonical_sid: str,
    harness: str,
    ts: float | None,
    *,
    explicit: Iterable[str] = (),
    agent: Iterable[str] = (),
    md_reads: Iterable[str] = (),
) -> None:
    rec = sessions.setdefault(
        canonical_sid,
        {"harness": harness, "ts": ts, "explicit": set(), "agent": set(), "md_reads": set()},
    )
    if ts is not None and (rec["ts"] is None or ts > rec["ts"]):
        rec["ts"] = ts
    rec["explicit"].update(explicit)
    rec["agent"].update(agent)
    rec["md_reads"].update(md_reads)


def _finalize_usage_stats(
    skill_names: set[str],
    sessions: dict[str, dict],
    *,
    mode: str,
    since_ts: float | None,
    coverage: dict,
) -> dict:
    """Aggregate deduplicated session hits into per-skill usage stats."""
    stats_map: dict[str, SkillUsageStat] = {name: SkillUsageStat(name=name) for name in sorted(skill_names)}
    filtered_audit_sessions = 0

    for sid, rec in sessions.items():
        ts = rec.get("ts")
        if since_ts is not None and ts is not None and ts < since_ts:
            continue
        explicit = set(rec.get("explicit", ())) & skill_names
        agent = set(rec.get("agent", ())) & skill_names
        md_reads = set(rec.get("md_reads", ())) & skill_names

        # Filter bulk audit / inspection sessions that read >8 distinct SKILL.md files
        if len(md_reads) > BULK_AUDIT_SKILL_THRESHOLD:
            filtered_audit_sessions += 1
            md_reads = set()

        agent_all = agent | md_reads
        all_for_session = explicit | agent_all
        harness = rec.get("harness", "unknown")
        for sname in all_for_session:
            st = stats_map[sname]
            st.total_sessions += 1
            if sname in explicit:
                st.explicit_sessions += 1
            if sname in agent_all and sname not in explicit:
                st.agent_sessions += 1
            elif sname in agent_all and sname in explicit:
                # Session both explicitly triggered and ran agent tool; count total=1, record both channels
                st.agent_sessions += 1
            if ts is not None and (st.last_used_ts is None or ts > st.last_used_ts):
                st.last_used_ts = ts
                st.last_used_iso = _iso_utc(ts)
            st.harnesses[harness] = st.harnesses.get(harness, 0) + 1

    coverage["filtered_audit_sessions"] = filtered_audit_sessions
    return {
        "mode": mode,
        "since": _iso_utc(since_ts) if since_ts is not None else "all",
        "coverage": coverage,
        "skills": {k: asdict(v) for k, v in stats_map.items()},
    }


def collect_usage_fast(
    skill_names: set[str],
    *,
    since_ts: float | None = None,
    home: Path | None = None,
    harnesses_filter: set[str] | None = None,
) -> dict:
    """Fast usage scan (<300 ms): flat prompt logs + read-only porch SQLite index."""
    home = home or Path.home()
    sessions: dict[str, dict] = {}
    sources_read: list[str] = []
    porch_indexed_sessions = 0
    porch_index_total_hint = None

    def _want(h: str) -> bool:
        return not harnesses_filter or h in harnesses_filter

    # 1. ~/.claude/history.jsonl
    claude_hist = home / ".claude" / "history.jsonl"
    if _want("claude-code") and claude_hist.is_file():
        sources_read.append("claude-history")
        try:
            with claude_hist.open("r", encoding="utf-8", errors="replace") as fh:
                for idx, line in enumerate(fh):
                    if not line.strip():
                        continue
                    try:
                        row = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    ts = _parse_ts(row.get("timestamp"))
                    if since_ts is not None and ts is not None and ts < since_ts:
                        continue
                    text = str(row.get("display", ""))
                    hits = _extract_prompt_triggers(text, skill_names)
                    if hits:
                        sid = str(row.get("sessionId") or f"claude-hist-{idx}")
                        _record_hit(sessions, f"claude:{sid}", "claude-code", ts, explicit=hits)
        except OSError:
            pass

    # 2. ~/.codex/history.jsonl
    codex_hist = home / ".codex" / "history.jsonl"
    if _want("codex") and codex_hist.is_file():
        sources_read.append("codex-history")
        try:
            with codex_hist.open("r", encoding="utf-8", errors="replace") as fh:
                for idx, line in enumerate(fh):
                    if not line.strip():
                        continue
                    try:
                        row = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    ts = _parse_ts(row.get("ts"))
                    if since_ts is not None and ts is not None and ts < since_ts:
                        continue
                    text = str(row.get("text", ""))
                    hits = _extract_prompt_triggers(text, skill_names)
                    if hits:
                        sid = str(row.get("session_id") or f"codex-hist-{idx}")
                        _record_hit(sessions, f"codex:{sid}", "codex", ts, explicit=hits)
        except OSError:
            pass

    # 3. ~/.grok/sessions/*/*/prompt_history.jsonl
    grok_dir = home / ".grok" / "sessions"
    if _want("grok") and grok_dir.is_dir():
        grok_hits_scanned = 0
        for pfile in grok_dir.glob("*/*/prompt_history.jsonl"):
            try:
                if since_ts is not None and pfile.stat().st_mtime < since_ts:
                    continue
                grok_hits_scanned += 1
                with pfile.open("r", encoding="utf-8", errors="replace") as fh:
                    for line in fh:
                        if not line.strip():
                            continue
                        try:
                            row = json.loads(line)
                        except json.JSONDecodeError:
                            continue
                        ts = _parse_ts(row.get("timestamp") or row.get("ts"))
                        text = str(row.get("text") or row.get("prompt") or row.get("content") or "")
                        hits = _extract_prompt_triggers(text, skill_names)
                        if hits:
                            _record_hit(sessions, f"grok:{pfile.parent.name}", "grok", ts, explicit=hits)
            except OSError:
                continue
        if grok_hits_scanned:
            sources_read.append("grok-prompt-history")

    # 4. Porch read-only SQLite index (no sync())
    idx_db = resolve_porch_index_db(home)
    if idx_db and (conn := _open_ro_sqlite(idx_db)):
        try:
            sources_read.append("porch-index-ro")
            row_cnt = conn.execute("SELECT COUNT(*) FROM sessions").fetchone()
            porch_indexed_sessions = int(row_cnt[0]) if row_cnt else 0
            meta_cov = conn.execute("SELECT value FROM meta WHERE key='last_sync_coverage'").fetchone()
            if meta_cov and meta_cov[0]:
                try:
                    cov_data = json.loads(meta_cov[0])
                    if not cov_data.get("complete", True):
                        porch_index_total_hint = "partial index (run 'porch sessions index build' for full coverage)"
                except json.JSONDecodeError:
                    pass
            # Read prompt docs only (fast single scan of indexed prompt rows)
            for session_key, ts_raw, text in conn.execute(
                "SELECT s.harness || ':' || COALESCE(s.native_id, d.session_key), d.ts, d.text "
                "FROM docs d JOIN sessions s ON s.session_key = d.session_key "
                "WHERE d.kind = 'prompt'"
            ):
                harness = session_key.split(":", 1)[0]
                if not _want(harness):
                    continue
                ts = _parse_ts(ts_raw)
                if since_ts is not None and ts is not None and ts < since_ts:
                    continue
                hits = _extract_prompt_triggers(text or "", skill_names)
                if hits:
                    # Normalize claude-code / claude-desktop key shape to match history.jsonl
                    norm_key = session_key
                    if harness in ("claude-code", "claude-desktop"):
                        sid_part = session_key.split(":", 1)[1]
                        norm_key = f"claude:{sid_part.rsplit('/', 1)[-1]}"
                    elif harness == "codex":
                        norm_key = f"codex:{session_key.split(':', 1)[1]}"
                    _record_hit(sessions, norm_key, harness, ts, explicit=hits)
        except sqlite3.Error:
            pass
        finally:
            conn.close()

    coverage = {
        "mode": "fast",
        "sources": sources_read,
        "porch_indexed_sessions": porch_indexed_sessions,
        "note": porch_index_total_hint or "fast mode captures explicit /skill and $skill triggers from prompt logs & index",
        "complete": False if porch_index_total_hint else True,
    }
    return _finalize_usage_stats(skill_names, sessions, mode="fast", since_ts=since_ts, coverage=coverage)


def _load_cache(cache_path: Path) -> dict:
    if not cache_path.is_file():
        return {"version": 1, "files": {}, "db_sessions": {}}
    try:
        data = json.loads(cache_path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and data.get("version") == 1 and isinstance(data.get("files"), dict):
            data.setdefault("db_sessions", {})
            return data
    except (OSError, json.JSONDecodeError):
        pass
    return {"version": 1, "files": {}, "db_sessions": {}}


def _save_cache(cache_path: Path, cache: dict) -> None:
    try:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            os.chmod(cache_path.parent, 0o700)
        except OSError:
            pass
        tmp = cache_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(cache), encoding="utf-8")
        try:
            os.chmod(tmp, 0o600)
        except OSError:
            pass
        tmp.replace(cache_path)
    except OSError:
        pass


def _iter_jsonl_lines(path: Path) -> Iterable[str]:
    """Stream lines from plain ``.jsonl`` or ``.jsonl.zst`` (when stdlib zstd exists)."""
    if path.suffix == ".zst":
        if _stdlib_zstd is None:
            return
        try:
            with path.open("rb") as raw_fh:
                data = _stdlib_zstd.decompress(raw_fh.read())
            for line in data.decode("utf-8", errors="replace").splitlines():
                yield line
        except Exception:
            return
    else:
        try:
            with path.open("r", encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    yield line
        except OSError:
            return


def _scan_claude_file(path: Path, skill_names: set[str], sid_hint: str) -> dict[str, dict]:
    """Parse one Claude Code / Cowork JSONL file for explicit, Skill tool, and SKILL.md reads."""
    out: dict[str, dict] = {}
    for line in _iter_jsonl_lines(path):
        if not line.strip():
            continue
        # Quick byte guard: skip lines that cannot mention a skill or prompt trigger
        if "Skill" not in line and "SKILL.md" not in line and '"type":"user"' not in line and '"type": "user"' not in line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        ts = _parse_ts(row.get("timestamp"))
        sid = str(row.get("sessionId") or sid_hint)
        rtype = row.get("type")
        msg = row.get("message") if isinstance(row.get("message"), dict) else {}
        content = msg.get("content")

        if rtype == "user" and not row.get("isMeta"):
            if isinstance(content, str) and not content.lstrip().startswith("<system-reminder>"):
                hits = _extract_prompt_triggers(content, skill_names)
                if hits:
                    _record_hit(out, f"claude:{sid}", "claude-code", ts, explicit=hits)
            elif isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "text":
                        txt = str(block.get("text", ""))
                        if not txt.lstrip().startswith("<system-reminder>"):
                            hits = _extract_prompt_triggers(txt, skill_names)
                            if hits:
                                _record_hit(out, f"claude:{sid}", "claude-code", ts, explicit=hits)
        elif rtype == "assistant" and isinstance(content, list):
            for block in content:
                if not isinstance(block, dict) or block.get("type") != "tool_use":
                    continue
                tname = block.get("name", "")
                tinp = block.get("input") if isinstance(block.get("input"), dict) else {}
                if tname == "Skill":
                    raw_skill = str(tinp.get("skill", "")).strip()
                    sname = raw_skill.split(":")[-1]
                    if sname in skill_names:
                        _record_hit(out, f"claude:{sid}", "claude-code", ts, agent=[sname])
                elif tname in ("Read", "read_file", "Bash"):
                    txt = json.dumps(tinp)
                    reads = _extract_skill_md_reads(txt, skill_names)
                    if reads:
                        _record_hit(out, f"claude:{sid}", "claude-code", ts, md_reads=reads)
    return out


def _scan_codex_file(path: Path, skill_names: set[str], sid_hint: str) -> dict[str, dict]:
    out: dict[str, dict] = {}
    sid = sid_hint
    for line in _iter_jsonl_lines(path):
        if not line.strip():
            continue
        if "session_meta" not in line and "user_message" not in line and "SKILL.md" not in line and "$" not in line and "/" not in line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        ts = _parse_ts(row.get("timestamp"))
        rtype = row.get("type")
        payload = row.get("payload") if isinstance(row.get("payload"), dict) else {}
        if rtype == "session_meta" and payload.get("id"):
            sid = str(payload["id"])
        elif rtype == "event_msg" and payload.get("type") == "user_message":
            txt = str(payload.get("message", ""))
            hits = _extract_prompt_triggers(txt, skill_names)
            if hits:
                _record_hit(out, f"codex:{sid}", "codex", ts, explicit=hits)
        elif rtype == "response_item":
            ptype = payload.get("type")
            if ptype in ("function_call", "custom_tool_call"):
                reads = _extract_skill_md_reads(str(payload.get("arguments", "")) + str(payload.get("input", "")), skill_names)
                if reads:
                    _record_hit(out, f"codex:{sid}", "codex", ts, md_reads=reads)
    return out


def _scan_agy_file(path: Path, skill_names: set[str], cid: str) -> dict[str, dict]:
    """Scan ``brain/<cid>/.system_generated/logs/transcript*.jsonl`` (never SQLite)."""
    out: dict[str, dict] = {}
    for line in _iter_jsonl_lines(path):
        if not line.strip():
            continue
        if "USER_REQUEST" not in line and "SKILL.md" not in line and "<SKILL>" not in line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        ts = _parse_ts(row.get("created_at"))
        rtype = row.get("type", "")
        content = str(row.get("content", ""))
        if "USER_INPUT" in rtype or "USER_EXPLICIT" in rtype:
            req = USER_REQ_RE.search(content)
            prompt_txt = req.group(1) if req else content
            hits = _extract_prompt_triggers(prompt_txt, skill_names)
            # Antigravity attaches loaded skill path inside <SKILL> block
            if "<SKILL>" in content:
                hits |= _extract_skill_md_reads(content, skill_names)
            if hits:
                _record_hit(out, f"agy:{cid}", "agy", ts, explicit=hits)
        if tool_calls := row.get("tool_calls"):
            reads = _extract_skill_md_reads(json.dumps(tool_calls), skill_names)
            if reads:
                _record_hit(out, f"agy:{cid}", "agy", ts, md_reads=reads)
    return out


def _scan_generic_jsonl(path: Path, harness: str, skill_names: set[str], sid: str) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for line in _iter_jsonl_lines(path):
        if not line.strip():
            continue
        if "SKILL.md" not in line and "/" not in line and "$" not in line:
            continue
        ts = None
        try:
            row = json.loads(line)
            ts = _parse_ts(row.get("timestamp") or row.get("ts") or row.get("created_at"))
        except json.JSONDecodeError:
            pass
        reads = _extract_skill_md_reads(line, skill_names)
        hits = _extract_prompt_triggers(line, skill_names)
        if hits or reads:
            _record_hit(out, f"{harness}:{sid}", harness, ts, explicit=hits, md_reads=reads)
    return out


def _merge_cached_sessions(target: dict[str, dict], cached: dict[str, dict]) -> None:
    for sid, rec in cached.items():
        _record_hit(
            target,
            sid,
            rec["harness"],
            rec.get("ts"),
            explicit=rec.get("explicit", ()),
            agent=rec.get("agent", ()),
            md_reads=rec.get("md_reads", ()),
        )


def _serialize_session_hits(hits: dict[str, dict]) -> dict[str, dict]:
    return {
        sid: {
            "harness": rec["harness"],
            "ts": rec["ts"],
            "explicit": sorted(rec["explicit"]),
            "agent": sorted(rec["agent"]),
            "md_reads": sorted(rec["md_reads"]),
        }
        for sid, rec in hits.items()
    }


def collect_usage_deep(
    skill_names: set[str],
    *,
    since_ts: float | None = None,
    home: Path | None = None,
    harnesses_filter: set[str] | None = None,
    cache_path: Path | None = None,
    no_cache: bool = False,
    max_files: int = 4000,
    deadline_s: float = 25.0,
) -> dict:
    """Single-pass, mtime/SQL-pruned, deduplicated, incrementally cached usage scan."""
    home = home or Path.home()
    since_ts = parse_since("30d") if since_ts is None else since_ts
    cache_file = cache_path or default_cache_path(home)
    cache = {"version": 1, "files": {}} if no_cache else _load_cache(cache_file)
    files_cache: dict = cache["files"]

    start_time = time.monotonic()
    deadline_hit = False
    files_scanned = 0
    cache_hits = 0
    skipped_old = 0
    stores_checked: dict[str, str] = {}
    sessions: dict[str, dict] = {}
    db_sessions_cache: dict = cache.setdefault("db_sessions", {})

    def _want(h: str) -> bool:
        return not harnesses_filter or h in harnesses_filter

    def _scan_cached_file(fpath: Path, harness: str, scanner, *args) -> None:
        nonlocal files_scanned, cache_hits, skipped_old, deadline_hit
        if deadline_hit or files_scanned >= max_files or (time.monotonic() - start_time) > deadline_s:
            deadline_hit = True
            return
        try:
            st = fpath.stat()
        except OSError:
            return
        if since_ts is not None and st.st_mtime < since_ts:
            skipped_old += 1
            return
        fkey = str(fpath)
        cached = files_cache.get(fkey)
        if cached and cached.get("mtime_ns") == st.st_mtime_ns and cached.get("size") == st.st_size:
            cache_hits += 1
            _merge_cached_sessions(sessions, cached.get("sessions", {}))
            return
        files_scanned += 1
        found = scanner(fpath, skill_names, *args)
        serialized = _serialize_session_hits(found)
        files_cache[fkey] = {"mtime_ns": st.st_mtime_ns, "size": st.st_size, "sessions": serialized}
        _merge_cached_sessions(sessions, serialized)

    # 1. Claude Code (~/.claude/projects/**/*.jsonl)
    claude_dir = home / ".claude" / "projects"
    if _want("claude-code") and claude_dir.is_dir():
        stores_checked["claude-code"] = "ok"
        for fpath in claude_dir.rglob("*.jsonl"):
            if deadline_hit:
                break
            _scan_cached_file(fpath, "claude-code", _scan_claude_file, fpath.stem)

    # 2. Codex CLI/App (~/.codex/{sessions,archived_sessions}/**/*.jsonl*)
    if _want("codex"):
        codex_dirs = [home / ".codex" / "sessions", home / ".codex" / "archived_sessions"]
        any_codex = any(d.is_dir() for d in codex_dirs)
        if any_codex:
            stores_checked["codex"] = "ok"
            for cdir in codex_dirs:
                if not cdir.is_dir():
                    continue
                for ext in ("*.jsonl", "*.jsonl.zst"):
                    if ext == "*.jsonl.zst" and _stdlib_zstd is None:
                        continue
                    for fpath in cdir.rglob(ext):
                        if deadline_hit:
                            break
                        _scan_cached_file(fpath, "codex", _scan_codex_file, fpath.stem)

    # 3. Antigravity CLI (~/.gemini/antigravity-cli/brain/*/...) - NEVER open .db
    agy_brain = home / ".gemini" / "antigravity-cli" / "brain"
    if _want("agy") and agy_brain.is_dir():
        stores_checked["agy"] = "ok"
        for cid_dir in agy_brain.iterdir():
            if deadline_hit:
                break
            if not cid_dir.is_dir():
                continue
            logs_dir = cid_dir / ".system_generated" / "logs"
            tfile = logs_dir / "transcript_full.jsonl"
            if not tfile.is_file():
                tfile = logs_dir / "transcript.jsonl"
            if tfile.is_file():
                _scan_cached_file(tfile, "agy", _scan_agy_file, cid_dir.name)

    # 4. OpenCode SQLite (~/.local/share/opencode/opencode.db) with SQL time predicate + session cache
    oc_db = home / ".local" / "share" / "opencode" / "opencode.db"
    if not deadline_hit and _want("opencode") and (conn := _open_ro_sqlite(oc_db)):
        try:
            stores_checked["opencode"] = "ok"
            since_ms = int((since_ts or 0) * 1000)
            srows = conn.execute(
                "SELECT id, time_updated FROM session_v2 WHERE time_updated >= ?",
                (since_ms,),
            ).fetchall()
            recent_sids = {r[0]: _parse_ts(r[1]) for r in srows}
            rev_map = {r[0]: r[1] for r in srows}
            uncached_sids: list[str] = []
            for sid, tu in srows:
                c_entry = db_sessions_cache.get(f"opencode:{sid}")
                if c_entry and c_entry.get("rev") == tu:
                    cache_hits += 1
                    _merge_cached_sessions(sessions, c_entry.get("sessions", {}))
                else:
                    uncached_sids.append(sid)

            for offset in range(0, len(uncached_sids), 200):
                if (time.monotonic() - start_time) > deadline_s:
                    deadline_hit = True
                    break
                chunk = uncached_sids[offset:offset + 200]
                chunk_hits: dict[str, dict[str, dict]] = {s: {} for s in chunk}
                placeholders = ",".join("?" for _ in chunk)
                rows = conn.execute(
                    f"SELECT session_id, type, time_created, data FROM session_message "
                    f"WHERE session_id IN ({placeholders}) "
                    f"AND (type = 'skill' OR (type IN ('user', 'assistant') AND length(data) <= 65536 AND (data LIKE '%SKILL.md%' OR data LIKE '%\"skill\"%')))",
                    chunk,
                ).fetchall()
                for sid, mtype, tc, data in rows:
                    ts = _parse_ts(tc) or recent_sids.get(sid)
                    text = str(data or "")
                    if mtype == "skill":
                        try:
                            parsed = json.loads(text)
                            sname = str(parsed.get("name") or parsed.get("skill") or "")
                            if sname in skill_names:
                                _record_hit(chunk_hits[sid], f"opencode:{sid}", "opencode", ts, agent=[sname])
                        except json.JSONDecodeError:
                            pass
                    elif mtype == "user":
                        hits = _extract_prompt_triggers(text, skill_names)
                        if hits:
                            _record_hit(chunk_hits[sid], f"opencode:{sid}", "opencode", ts, explicit=hits)
                    reads = _extract_skill_md_reads(text, skill_names)
                    if reads:
                        _record_hit(chunk_hits[sid], f"opencode:{sid}", "opencode", ts, md_reads=reads)
                for sid in chunk:
                    ser = _serialize_session_hits(chunk_hits[sid])
                    db_sessions_cache[f"opencode:{sid}"] = {"rev": rev_map.get(sid), "sessions": ser}
                    _merge_cached_sessions(sessions, ser)
        except sqlite3.Error:
            stores_checked["opencode"] = "error"
        finally:
            conn.close()

    # 5. Devin SQLite (~/.local/share/devin/cli/sessions.db) - indexed activity + prompt_history + compact tool_call_state
    devin_db = home / ".local" / "share" / "devin" / "cli" / "sessions.db"
    if not deadline_hit and _want("devin") and (conn := _open_ro_sqlite(devin_db)):
        try:
            stores_checked["devin"] = "ok"
            sample = conn.execute("SELECT last_activity_at FROM sessions WHERE last_activity_at IS NOT NULL LIMIT 1").fetchone()
            recent_rows: list[tuple] = []
            if sample is not None:
                val = sample[0]
                if isinstance(val, (int, float)):
                    cutoff = int((since_ts or 0) * (1000 if val > 1e12 else 1))
                else:
                    cutoff = datetime.fromtimestamp(since_ts or 0, tz=timezone.utc).isoformat()
                recent_rows = conn.execute(
                    "SELECT id, last_activity_at FROM sessions WHERE last_activity_at >= ? ORDER BY last_activity_at DESC LIMIT 300",
                    (cutoff,),
                ).fetchall()

            # Check prompt_history table when present (tiny indexed table)
            tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()}
            if "prompt_history" in tables:
                try:
                    for psid, pcontent, pts in conn.execute(
                        "SELECT session_id, content, timestamp FROM prompt_history WHERE timestamp >= ?",
                        (int(since_ts or 0),),
                    ).fetchall():
                        hits = _extract_prompt_triggers(str(pcontent or ""), skill_names)
                        if hits:
                            _record_hit(sessions, f"devin:{psid}", "devin", _parse_ts(pts), explicit=hits)
                except sqlite3.Error:
                    pass

            uncached_devin: list[tuple[str, object, float | None]] = []
            for raw_sid, la in recent_rows:
                sid = str(raw_sid)
                c_entry = db_sessions_cache.get(f"devin:{sid}")
                if c_entry and c_entry.get("rev") == la:
                    cache_hits += 1
                    _merge_cached_sessions(sessions, c_entry.get("sessions", {}))
                else:
                    uncached_devin.append((sid, la, _parse_ts(la)))

            has_tool_call_state = "tool_call_state" in tables
            for offset in range(0, len(uncached_devin), 50):
                if (time.monotonic() - start_time) > deadline_s:
                    deadline_hit = True
                    break
                chunk = uncached_devin[offset:offset + 50]
                chunk_sids = [c[0] for c in chunk]
                chunk_rev = {c[0]: c[1] for c in chunk}
                chunk_ts = {c[0]: c[2] for c in chunk}
                chunk_hits: dict[str, dict[str, dict]] = {s: {} for s in chunk_sids}
                placeholders = ",".join("?" for _ in chunk_sids)
                if has_tool_call_state:
                    rows = conn.execute(
                        f"SELECT session_id, tool_call_json FROM tool_call_state "
                        f"WHERE session_id IN ({placeholders}) AND tool_call_json LIKE '%SKILL.md%'",
                        chunk_sids,
                    ).fetchall()
                    for sid, tjson in rows:
                        reads = _extract_skill_md_reads(str(tjson or ""), skill_names)
                        if reads:
                            _record_hit(chunk_hits[sid], f"devin:{sid}", "devin", chunk_ts.get(sid), md_reads=reads)
                elif "message_nodes" in tables:
                    # Fallback for fixture DBs without tool_call_state: strict SKILL.md + length cap
                    rows = conn.execute(
                        f"SELECT session_id, chat_message, created_at FROM message_nodes "
                        f"WHERE session_id IN ({placeholders}) AND length(chat_message) <= 65536 AND chat_message LIKE '%SKILL.md%'",
                        chunk_sids,
                    ).fetchall()
                    for sid, msg, ca in rows:
                        ts = _parse_ts(ca) or chunk_ts.get(sid)
                        txt = str(msg or "")
                        hits = _extract_prompt_triggers(txt, skill_names)
                        reads = _extract_skill_md_reads(txt, skill_names)
                        if hits or reads:
                            _record_hit(chunk_hits[sid], f"devin:{sid}", "devin", ts, explicit=hits, md_reads=reads)
                for sid in chunk_sids:
                    ser = _serialize_session_hits(chunk_hits[sid])
                    db_sessions_cache[f"devin:{sid}"] = {"rev": chunk_rev[sid], "sessions": ser}
                    _merge_cached_sessions(sessions, ser)
        except sqlite3.Error:
            stores_checked["devin"] = "error"
        finally:
            conn.close()

    # 6. Hermes SQLite (~/.hermes/state.db) with session cache
    hermes_db = home / ".hermes" / "state.db"
    if not deadline_hit and _want("hermes") and (conn := _open_ro_sqlite(hermes_db)):
        try:
            stores_checked["hermes"] = "ok"
            sample = conn.execute("SELECT started_at FROM sessions WHERE started_at IS NOT NULL LIMIT 1").fetchone()
            recent_hermes_rows: list[tuple] = []
            if sample is not None:
                val = sample[0]
                if isinstance(val, (int, float)):
                    cutoff = int((since_ts or 0) * (1000 if val > 1e12 else 1))
                else:
                    cutoff = datetime.fromtimestamp(since_ts or 0, tz=timezone.utc).isoformat()
                recent_hermes_rows = conn.execute(
                    "SELECT id, started_at FROM sessions WHERE started_at >= ?",
                    (cutoff,),
                ).fetchall()

            uncached_hermes: list[tuple[str, object, float | None]] = []
            for raw_sid, sa in recent_hermes_rows:
                sid = str(raw_sid)
                c_entry = db_sessions_cache.get(f"hermes:{sid}")
                if c_entry and c_entry.get("rev") == sa:
                    cache_hits += 1
                    _merge_cached_sessions(sessions, c_entry.get("sessions", {}))
                else:
                    uncached_hermes.append((sid, sa, _parse_ts(sa)))

            for offset in range(0, len(uncached_hermes), 100):
                if (time.monotonic() - start_time) > deadline_s:
                    deadline_hit = True
                    break
                chunk = uncached_hermes[offset:offset + 100]
                chunk_sids = [c[0] for c in chunk]
                chunk_rev = {c[0]: c[1] for c in chunk}
                chunk_ts = {c[0]: c[2] for c in chunk}
                chunk_hits: dict[str, dict[str, dict]] = {s: {} for s in chunk_sids}
                placeholders = ",".join("?" for _ in chunk_sids)
                rows = conn.execute(
                    f"SELECT session_id, role, content, tool_calls, timestamp FROM messages "
                    f"WHERE session_id IN ({placeholders})",
                    chunk_sids,
                ).fetchall()
                for sid, role, content, tcalls, ts_raw in rows:
                    ts = _parse_ts(ts_raw) or chunk_ts.get(sid)
                    txt = str(content or "")
                    if role == "user":
                        hits = _extract_prompt_triggers(txt, skill_names)
                        if hits:
                            _record_hit(chunk_hits[sid], f"hermes:{sid}", "hermes", ts, explicit=hits)
                    reads = _extract_skill_md_reads(txt + str(tcalls or ""), skill_names)
                    if reads:
                        _record_hit(chunk_hits[sid], f"hermes:{sid}", "hermes", ts, md_reads=reads)
                for sid in chunk_sids:
                    ser = _serialize_session_hits(chunk_hits[sid])
                    db_sessions_cache[f"hermes:{sid}"] = {"rev": chunk_rev[sid], "sessions": ser}
                    _merge_cached_sessions(sessions, ser)
        except sqlite3.Error:
            stores_checked["hermes"] = "error"
        finally:
            conn.close()

    # 7. Claude Desktop Cowork audit logs + Gemini CLI chat JSON
    cowork_root = home / "Library" / "Application Support" / "Claude" / "local-agent-mode-sessions"
    if not deadline_hit and _want("claude-desktop") and cowork_root.is_dir():
        stores_checked["claude-desktop"] = "ok"
        for fpath in cowork_root.glob("*/*/local_*/audit.jsonl"):
            if deadline_hit:
                break
            _scan_cached_file(fpath, "claude-desktop", _scan_claude_file, fpath.parent.name)

    gemini_tmp = home / ".gemini" / "tmp"
    if not deadline_hit and _want("gemini") and gemini_tmp.is_dir():
        stores_checked["gemini"] = "ok"
        for fpath in gemini_tmp.glob("*/chats/session-*.json"):
            if deadline_hit:
                break
            _scan_cached_file(fpath, "gemini", _scan_generic_jsonl, "gemini", fpath.stem)

    # 8. Peer JSONL harnesses (grok, qwen-code, kimi-code, omp)
    peer_globs = [
        ("grok", home / ".grok" / "sessions", "chat_history.jsonl"),
        ("qwen-code", home / ".qwen" / "projects", "*.jsonl"),
        ("kimi-code", home / ".kimi-code" / "sessions", "*.jsonl"),
        ("omp", home / ".omp" / "agent" / "sessions", "*.jsonl"),
    ]
    for harness, root_dir, pattern in peer_globs:
        if not _want(harness) or not root_dir.is_dir() or deadline_hit:
            continue
        stores_checked[harness] = "ok"
        for fpath in root_dir.rglob(pattern):
            if deadline_hit:
                break
            _scan_cached_file(fpath, harness, _scan_generic_jsonl, harness, fpath.stem)

    if not no_cache:
        _save_cache(cache_file, cache)

    elapsed = round(time.monotonic() - start_time, 2)
    coverage = {
        "mode": "deep",
        "elapsed_s": elapsed,
        "files_parsed": files_scanned,
        "cache_hits": cache_hits,
        "skipped_before_since": skipped_old,
        "stores": stores_checked,
        "complete": not deadline_hit,
        "reason": "deadline or max_files reached" if deadline_hit else None,
        "note": "Counts deduplicated sessions; sessions reading >8 SKILL.md files are excluded as bulk audits",
    }
    return _finalize_usage_stats(skill_names, sessions, mode="deep", since_ts=since_ts, coverage=coverage)
