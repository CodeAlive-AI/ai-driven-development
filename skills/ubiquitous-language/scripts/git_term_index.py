#!/usr/bin/env python3
"""Build a throwaway SQLite index of git history and query it for domain-term evidence.

Purpose: resolve naming ambiguities collected in the `## Unresolved` section of a
THESAURUS.md by mining what actually happened in the repository — when a name was
born, when it stopped being touched, which names travelled together in the same
commits, and what the commit messages said about them.

Dependency-free (Python 3.9+ stdlib, git). The index is a single SQLite file in a
temp directory OUTSIDE the working tree, safe to delete at any time (`clean`).

Why SQLite: the whole diff history is indexed, not a recent window, so "born" means
born. Commit messages go into an FTS5 table, so message search is ranked by BM25
relevance instead of recency.

Schema:
  commits(id, sha, date, author, subject, body)   + commits_fts (FTS5/BM25)
  files(commit_id, status, path, oldpath)         changed paths
  renames(commit_id, oldpath, newpath, sim)       detected renames (-M)
  tokens(id, tok, norm)                           identifiers + casing-independent norm
  token_sub(sub, token_id)                        camelCase/snake_case subwords
  paths(id, path)                                 files touched
  tc(token_id, commit_id, path_id, adds, dels)    identifier x commit x FILE occurrences

Commands:
  build    build or refresh the index
  status   show what is indexed
  query    per-term evidence report (life, trajectory, renames, paths, messages)
  contexts where one name lives — directory split, the polysemy check
  pair     compare competing names (birth order, displacement, shared commits)
  search   BM25 full-text search over commit messages
  clean    delete the index

Examples:
  python3 git_term_index.py build --repo-dir .
  python3 git_term_index.py build --repo-dir . --content          # + full diff history
  python3 git_term_index.py query Account Customer
  python3 git_term_index.py pair Minion Node
  python3 git_term_index.py contexts Account
  python3 git_term_index.py search 'rename minion node'
  python3 git_term_index.py clean
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time
from collections import Counter
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Sequence, Tuple

REC = "\x01"  # record separator inside git log output
FLD = "\x02"  # field separator inside git log output

TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]{2,}")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
SUBWORD_RE = re.compile(r"[A-Z]+(?![a-z])|[A-Z][a-z0-9]+|[a-z0-9]+")
RENAME_WORD_RE = re.compile(
    r"\b(renam|rename[ds]?|replac|migrat|deprecat|s/\w+/\w+|instead of|switch to|"
    r"convert.{0,12}to|drop\b)", re.I)

# High-precision issue/PR references only. A bare `#12` is deliberately NOT matched:
# real histories are full of `(2026/08 #09)` release-note numbering and `#1` stack-trace
# frames, and that noise is worse than a missed reference.
ISSUE_RE = re.compile(
    r"""(?:
          \(\#(?P<squash>[1-9]\d{0,5})\)                  # GitHub squash-merge subject
        | \bGH-(?P<gh>[1-9]\d{0,5})\b                     # GH-123
        | \b(?:fix(?:e[sd])?|close[sd]?|resolve[sd]?|
               refs?|see|PR|pull\srequest|issue)
          \s*:?\s*\#(?P<kw>[1-9]\d{0,5})\b                # fixes #123, PR #123
        | github\.com/[^\s]+?/(?:pull|issues)/(?P<url>[1-9]\d{0,5})
        )""",
    re.I | re.X,
)

# Vendored, generated and minified paths dominate token counts in large repos and
# carry no domain vocabulary. Excluded from the diff pass unless --no-default-excludes.
DEFAULT_EXCLUDES = [
    ":(exclude)vendor/**", ":(exclude)third_party/**", ":(exclude)node_modules/**",
    ":(exclude)**/testdata/**", ":(exclude)**/*.min.js", ":(exclude)**/*.min.css",
    ":(exclude)**/*.lock", ":(exclude)**/package-lock.json", ":(exclude)**/yarn.lock",
    ":(exclude)**/go.sum", ":(exclude)**/Cargo.lock", ":(exclude)**/*.snap",
    ":(exclude)**/*generated*.go", ":(exclude)**/*.pb.go", ":(exclude)**/zz_generated*",
    ":(exclude)**/*.svg", ":(exclude)**/*.map",
    ":(exclude)**/*.po", ":(exclude)**/*.pot", ":(exclude)**/locale/**", ":(exclude)po/**",
    ":(exclude)**/CHANGELOG*", ":(exclude)**/*.golden",
]

READ_CHUNK = 1 << 20
BATCH = 20000
MIN_NET_SWAP = 3  # net occurrences; below this a 'swap' is line noise
NOISE_FLOOR = 0.05  # exchanges must be this share of shared commits to count

# Tokens that carry no domain signal. Kept deliberately small: this is a naming
# tool, and over-filtering hides real evidence.
STOPWORDS = {
    "the", "and", "for", "not", "with", "this", "that", "from", "into", "out",
    "var", "let", "const", "def", "func", "function", "class", "struct", "enum",
    "interface", "type", "typedef", "public", "private", "protected", "internal",
    "static", "return", "import", "export", "require", "package", "namespace",
    "using", "include", "true", "false", "null", "none", "nil", "void", "int",
    "str", "string", "bool", "float", "double", "list", "dict", "map", "set",
    "new", "self", "async", "await", "try", "catch", "except", "finally",
    "if", "else", "elif", "while", "break", "continue", "pass", "yield",
}


def eprint(*args: object) -> None:
    print(*args, file=sys.stderr)


# --------------------------------------------------------------------------- git


def run(cmd: Sequence[str], cwd: Path, timeout: int = 900) -> str:
    """Run git and return stdout. Only for commands with bounded output."""
    proc = subprocess.run(
        list(cmd), cwd=str(cwd), text=True, errors="replace",
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"git failed ({proc.returncode}): {' '.join(cmd)}\n{proc.stderr.strip()}")
    return proc.stdout


def stream_records(cmd: Sequence[str], cwd: Path, timeout: int = 3600) -> Iterator[str]:
    """Stream `git log` output record by record so memory stays flat on huge histories."""
    proc = subprocess.Popen(
        list(cmd), cwd=str(cwd), text=True, errors="replace",
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    # A git that wedges emits nothing, so a deadline checked after read() returns would
    # never fire. Kill it from a watchdog thread instead.
    timed_out = threading.Event()

    def watchdog() -> None:
        if proc.wait_event.wait(timeout):  # type: ignore[attr-defined]
            return
        timed_out.set()
        proc.kill()

    proc.wait_event = threading.Event()  # type: ignore[attr-defined]
    threading.Thread(target=watchdog, daemon=True).start()
    deadline = time.monotonic() + timeout
    buf = ""
    try:
        assert proc.stdout is not None
        while True:
            data = proc.stdout.read(READ_CHUNK)
            if not data:
                break
            if time.monotonic() > deadline:
                proc.kill()
                raise subprocess.TimeoutExpired(list(cmd), timeout)
            buf += data
            if REC in buf:
                parts = buf.split(REC)
                buf = parts.pop()
                for part in parts:
                    if part.strip():
                        yield part
        if buf.strip():
            yield buf
    finally:
        if proc.stdout:
            proc.stdout.close()
        err = proc.stderr.read() if proc.stderr else ""
        if proc.stderr:
            proc.stderr.close()
        rc = proc.wait()
        proc.wait_event.set()  # type: ignore[attr-defined]
        if timed_out.is_set():
            raise subprocess.TimeoutExpired(list(cmd), timeout)
        if rc not in (0, -9):
            raise RuntimeError(f"git failed ({rc}): {' '.join(cmd)}\n{err.strip()}")


def repo_root(repo_dir: Path) -> Path:
    try:
        return Path(run(["git", "rev-parse", "--show-toplevel"], repo_dir, timeout=60).strip())
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(f"not a git repository: {repo_dir} ({exc})")


def head_commit_date(root: Path) -> str:
    try:
        return run(["git", "log", "-1", "--date=short", "--format=%ad"], root, timeout=60).strip()
    except Exception:  # noqa: BLE001
        return ""


# --------------------------------------------------------------------------- helpers


def index_path_for(root: Path, override: Optional[str]) -> Path:
    if override:
        return Path(override).expanduser().resolve()
    digest = hashlib.sha1(str(root).encode()).hexdigest()[:10]
    base = Path(os.environ.get("TMPDIR", tempfile.gettempdir()))
    return base / "ubiquitous-language-git-index" / f"{root.name}-{digest}.sqlite3"


def flatten(text: str) -> str:
    return " ".join(text.split())


def subwords(token: str) -> List[str]:
    """camelCase / snake_case / PascalCase -> lowercase word list.

    Must be called on the ORIGINAL token: lowercasing first destroys the camelCase
    boundaries, which is why `OrderLineItem` and `order_line_item` used to index as two
    unrelated identifiers and a PascalCase thesaurus Identifier found nothing in a
    snake_case codebase.
    """
    out = []
    for part in token.split("_"):
        out.extend(w.lower() for w in SUBWORD_RE.findall(part))
    return [w for w in out if w]


def normal_form(token: str) -> str:
    """Casing-independent identity of an identifier: its subwords, underscore-joined.

    `OrderLineItem`, `order_line_item`, `ORDER_LINE_ITEM` and `orderLineItem` all share
    the norm `order_line_item`; `BillingAccount` is `billing_account`, distinct from
    `account`, so the two never contaminate each other's counts.
    """
    return "_".join(subwords(token))


def content_subwords(token: str) -> List[str]:
    """Subwords worth indexing for family lookups (drops noise words)."""
    return [w for w in subwords(token) if len(w) >= 3 and w not in STOPWORDS]


def word_re(term: str) -> re.Pattern:
    """Match the term as a whole identifier, in any casing style."""
    parts = [p for p in SUBWORD_RE.findall(term) if p]
    joined = r"[\s_\-]*".join(re.escape(p) for p in parts) if parts else re.escape(term)
    return re.compile(rf"(?<![A-Za-z0-9]){joined}(?![A-Za-z0-9])", re.I)


def issue_refs(text: str) -> List[str]:
    out = []
    for m in ISSUE_RE.finditer(text):
        num = next((g for g in m.groups() if g), None)
        if num:
            out.append(num)
    return out


def fts_query(text: str) -> str:
    """Turn free user input into a safe FTS5 MATCH expression.

    FTS5 has its own operator grammar (`-`, `:`, `NEAR`, `*`), so raw input like
    `grep-first` is parsed as syntax and fails. Every word becomes a quoted phrase;
    implicit AND still applies between them.
    """
    words = re.findall(r"[0-9A-Za-z_]+", text)
    return " ".join(f'"{w}"' for w in words)


def plural(n: int, noun: str) -> str:
    return f"{n} {noun}" if n == 1 else f"{n} {noun}s"


def dormant_years(last_date: str, head_date: str) -> float:
    try:
        return (int(head_date[:4]) - int(last_date[:4])) + (int(head_date[5:7]) - int(last_date[5:7])) / 12
    except Exception:  # noqa: BLE001
        return 0.0


def connect(path: Path, write: bool = False) -> sqlite3.Connection:
    con = sqlite3.connect(str(path))
    con.row_factory = sqlite3.Row
    if write:
        con.executescript("PRAGMA journal_mode=OFF; PRAGMA synchronous=OFF; "
                          "PRAGMA temp_store=MEMORY; PRAGMA cache_size=-200000;")
    return con


SCHEMA = """
CREATE TABLE meta(k TEXT PRIMARY KEY, v TEXT);
CREATE TABLE commits(id INTEGER PRIMARY KEY, sha TEXT, date TEXT, author TEXT,
                     subject TEXT, body TEXT);
CREATE TABLE files(commit_id INTEGER, status TEXT, path TEXT, oldpath TEXT);
CREATE TABLE renames(commit_id INTEGER, oldpath TEXT, newpath TEXT, sim TEXT);
CREATE TABLE tokens(id INTEGER PRIMARY KEY, tok TEXT, norm TEXT);
CREATE TABLE token_sub(sub TEXT, token_id INTEGER);
CREATE TABLE paths(id INTEGER PRIMARY KEY, path TEXT);
CREATE TABLE tc(token_id INTEGER, commit_id INTEGER, path_id INTEGER,
                adds INTEGER, dels INTEGER);
"""

INDEXES = """
CREATE UNIQUE INDEX commits_sha ON commits(sha);
CREATE INDEX files_path ON files(path);
CREATE INDEX files_commit ON files(commit_id);
CREATE INDEX renames_commit ON renames(commit_id);
CREATE UNIQUE INDEX tokens_tok ON tokens(tok);
CREATE INDEX tokens_norm ON tokens(norm);
CREATE INDEX token_sub_i ON token_sub(sub);
CREATE UNIQUE INDEX paths_path ON paths(path);
CREATE INDEX tc_token ON tc(token_id);
CREATE INDEX tc_commit ON tc(commit_id);
CREATE INDEX tc_path ON tc(path_id);
"""


def has_fts5(con: sqlite3.Connection) -> bool:
    try:
        con.execute("CREATE VIRTUAL TABLE _fts_probe USING fts5(x)")
        con.execute("DROP TABLE _fts_probe")
        return True
    except sqlite3.OperationalError:
        return False


# --------------------------------------------------------------------------- build


def build(args: argparse.Namespace) -> int:
    root = repo_root(Path(args.repo_dir).resolve())
    db_path = index_path_for(root, args.index_file)
    try:
        head = run(["git", "rev-parse", "HEAD"], root, timeout=60).strip()
    except RuntimeError:
        raise SystemExit(f"{root} has no commits yet — nothing to mine")

    if db_path.exists() and not args.refresh:
        meta = read_meta_safe(db_path)
        scope_now = build_scope(args)
        if (meta and meta.get("head") == head
                and (meta.get("content") == "1" or not args.content)
                and meta.get("scope") == scope_now):
            print(f"index up to date: {db_path}\n  {meta.get('commits')} commits, content={meta.get('content')}")
            return 0
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()

    if (args.max_commits and args.content_max_commits
            and args.content_max_commits > args.max_commits):
        raise SystemExit(
            f"--content-max-commits ({args.content_max_commits}) exceeds --max-commits "
            f"({args.max_commits}); the diff pass would walk commits the message pass never "
            f"indexed and silently drop them. Lower it or raise --max-commits.")
    started = time.monotonic()
    con = connect(db_path, write=True)
    con.executescript(SCHEMA)
    fts = has_fts5(con)
    if fts:
        con.executescript(
            "CREATE VIRTUAL TABLE commits_fts USING fts5(subject, body, "
            "content='commits', content_rowid='id');")

    shallow = run(["git", "rev-parse", "--is-shallow-repository"], root, timeout=60).strip() == "true"
    n_commits, n_files, n_renames, oldest, newest = pass_commits(con, root, args)
    con.commit()

    n_tokens = n_tc = 0
    diff_stats: Dict[str, object] = {}
    if args.content:
        n_tokens, n_tc, diff_stats = pass_diffs(con, root, args)
        con.commit()

    print("  building indexes …", flush=True)
    con.executescript(INDEXES)
    if fts:
        con.execute("INSERT INTO commits_fts(rowid, subject, body) SELECT id, subject, body FROM commits")
    con.commit()

    meta = {
        "root": str(root), "head": head, "commits": n_commits, "file_changes": n_files,
        "renames": n_renames, "tokens": n_tokens, "token_commits": n_tc,
        "content": "1" if args.content else "0", "fts5": "1" if fts else "0",
        "oldest": oldest, "newest": newest, "shallow": "1" if shallow else "0",
        "since": args.since or "", "max_commits": str(args.max_commits or ""),
        "pathspec": " ".join(args.pathspec or []),
        "scope": build_scope(args),
        "refs": "all" if args.all_refs else "HEAD",
        "excludes": "default" if not args.no_default_excludes else "none",
        "built_seconds": str(round(time.monotonic() - started, 1)),
        **{f"diff_{k}": str(v) for k, v in diff_stats.items()},
    }
    con.executemany("INSERT INTO meta(k, v) VALUES(?, ?)", list(meta.items()))
    con.commit()
    con.execute("PRAGMA optimize")
    con.close()

    size = db_path.stat().st_size / 1024 / 1024
    print(f"index built: {db_path}")
    print(f"  commits {n_commits} ({oldest} … {newest})  file-changes {n_files}  renames {n_renames}")
    if args.content:
        print(f"  identifiers {n_tokens}  identifier×commit rows {n_tc}"
              + (f"  diff window: {diff_stats.get('commits')} commits, "
                 f"{diff_stats.get('oldest')} … {diff_stats.get('newest')}"
                 if diff_stats.get("truncated") else "  (full history)"))
    else:
        print("  (messages + paths only — add --content to index identifiers from diffs)")
    if not fts:
        print("  ** this Python's sqlite3 has no FTS5 — `search` unavailable, messages fall back to LIKE **")
    if shallow:
        print("  ** shallow clone — early history is missing; treat every date as a lower bound **")
    print(f"  {size:.0f} MB, {meta['built_seconds']}s")
    return 0


def build_scope(args: argparse.Namespace) -> str:
    """Everything that changes what the index covers. Part of the up-to-date check: a
    `--pathspec src/` index must not be silently reused for a whole-repo question."""
    return json.dumps({
        "pathspec": args.pathspec or [], "since": args.since or "",
        "max_commits": args.max_commits, "content_max_commits": args.content_max_commits,
        "all_refs": bool(args.all_refs), "excludes": not args.no_default_excludes,
    }, sort_keys=True)


def pass_commits(con: sqlite3.Connection, root: Path,
                 args: argparse.Namespace) -> Tuple[int, int, int, str, str]:
    """Pass A: commit messages, changed paths, renames. Cheap."""
    cmd = ["git", "log", "--no-merges", "-M", "--date=short", "--name-status",
           f"--pretty=format:{REC}%H{FLD}%ad{FLD}%an{FLD}%B{FLD}"]
    if args.all_refs:
        cmd.insert(2, "--all")
    if args.since:
        cmd.append(f"--since={args.since}")
    if args.max_commits:
        cmd.append(f"-n{args.max_commits}")
    if args.pathspec:
        cmd += ["--"] + args.pathspec

    print("  pass 1/2: commit messages, paths, renames …", flush=True)
    cbuf: List[tuple] = []
    fbuf: List[tuple] = []
    rbuf: List[tuple] = []
    n = nf = nr = dropped = 0
    oldest = newest = ""
    for chunk in stream_records(cmd, root, timeout=args.timeout):
        parts = chunk.split(FLD)
        if len(parts) < 4 or not SHA_RE.match(parts[0]):
            dropped += 1
            continue
        sha, date, author, body = parts[0], parts[1], parts[2], parts[3]
        tail = parts[4] if len(parts) > 4 else ""
        lines = body.splitlines()
        subject = lines[0].strip() if lines else ""
        rest = flatten(" ".join(lines[1:]))
        n += 1
        cid = n
        if not newest:
            newest = date
        oldest = date
        cbuf.append((cid, sha, date, flatten(author), flatten(subject), rest))
        for line in tail.splitlines():
            cols = line.rstrip("\n").split("\t")
            if len(cols) < 2 or not cols[0]:
                continue
            status = cols[0]
            if status[0] in ("R", "C") and len(cols) >= 3:
                fbuf.append((cid, status, cols[2], cols[1]))
                rbuf.append((cid, cols[1], cols[2], status))
                nr += 1
            else:
                fbuf.append((cid, status, cols[1], None))
            nf += 1
        if len(cbuf) >= BATCH:
            flush_pass_a(con, cbuf, fbuf, rbuf)
    flush_pass_a(con, cbuf, fbuf, rbuf)
    if dropped:
        print(f"    ** {dropped} commit record(s) unparseable (control bytes in a message?) "
              f"— skipped **", flush=True)
    return n, nf, nr, oldest, newest


def flush_pass_a(con: sqlite3.Connection, cbuf: List[tuple], fbuf: List[tuple], rbuf: List[tuple]) -> None:
    if cbuf:
        con.executemany("INSERT INTO commits(id, sha, date, author, subject, body) "
                        "VALUES(?,?,?,?,?,?)", cbuf)
        cbuf.clear()
    if fbuf:
        con.executemany("INSERT INTO files(commit_id, status, path, oldpath) VALUES(?,?,?,?)", fbuf)
        fbuf.clear()
    if rbuf:
        con.executemany("INSERT INTO renames(commit_id, oldpath, newpath, sim) VALUES(?,?,?,?)", rbuf)
        rbuf.clear()


def pass_diffs(con: sqlite3.Connection, root: Path,
               args: argparse.Namespace) -> Tuple[int, int, Dict[str, object]]:
    """Pass B: identifiers on added/removed diff lines, per FILE, over the FULL history."""
    sha_to_id = {r["sha"]: r["id"] for r in con.execute("SELECT id, sha FROM commits")}

    cmd = ["git", "log", "--no-merges", "-M", "--date=short", "-U0", "--no-color", "-p",
           f"--pretty=format:{REC}%H{FLD}%ad{FLD}"]
    if args.all_refs:
        cmd.insert(2, "--all")
    if args.since:
        cmd.append(f"--since={args.since}")
    if args.content_max_commits:
        cmd.append(f"-n{args.content_max_commits}")
    pathspec = list(args.pathspec or [])
    if not args.no_default_excludes:
        pathspec += DEFAULT_EXCLUDES
    if pathspec:
        cmd += ["--"] + pathspec

    print("  pass 2/2: identifiers from diffs, per file (full history) …", flush=True)
    tok_ids: Dict[str, int] = {}
    path_ids: Dict[str, int] = {}
    sub_rows: List[tuple] = []
    tok_rows: List[tuple] = []
    tc_buf: List[tuple] = []
    n_tc = 0
    seen = 0
    skipped = 0
    oldest = newest = ""
    last_report = time.monotonic()

    def token_id(raw: str) -> int:
        """Intern by lowercase literal, but derive the norm from the ORIGINAL casing."""
        key = raw.lower()
        tid = tok_ids.get(key)
        if tid is None:
            tid = len(tok_ids) + 1
            tok_ids[key] = tid
            tok_rows.append((tid, key, normal_form(raw)))
            for sub in set(content_subwords(raw)):
                if sub != key:
                    sub_rows.append((sub, tid))
        return tid

    def path_id(path: str) -> int:
        pid = path_ids.get(path)
        if pid is None:
            pid = len(path_ids) + 1
            path_ids[path] = pid
        return pid

    for chunk in stream_records(cmd, root, timeout=args.timeout):
        parts = chunk.split(FLD, 2)
        if len(parts) < 3 or not SHA_RE.match(parts[0]):
            skipped += 1
            continue
        sha, date, diff = parts[0], parts[1], parts[2]
        cid = sha_to_id.get(sha)
        if cid is None:
            skipped += 1
            continue
        seen += 1
        if not newest:
            newest = date
        oldest = date

        # (path, token) -> [adds, dels] for this commit
        per_file: Dict[Tuple[str, str], List[int]] = {}
        cur = ""
        for line in diff.splitlines():
            if line.startswith("+++ "):
                p = line[4:].strip()
                cur = p[2:] if p.startswith("b/") else ("" if p == "/dev/null" else p)
                continue
            if line.startswith("--- ") or line.startswith("diff --git ") or len(line) < 2:
                continue
            if line[0] not in "+-":
                continue
            slot = 0 if line[0] == "+" else 1
            for m in TOKEN_RE.finditer(line, 1):
                raw = m.group(0)
                if len(raw) < 3:
                    continue
                rec = per_file.get((cur, raw))
                if rec is None:
                    per_file[(cur, raw)] = rec = [0, 0]
                rec[slot] += 1

        for (path, raw), (a, d) in per_file.items():
            low = raw.lower()
            if low in STOPWORDS:
                continue
            tc_buf.append((token_id(raw), cid, path_id(path), a, d))
        if len(tc_buf) >= BATCH:
            n_tc += len(tc_buf)
            con.executemany(
                "INSERT INTO tc(token_id, commit_id, path_id, adds, dels) VALUES(?,?,?,?,?)", tc_buf)
            tc_buf.clear()
        if time.monotonic() - last_report > 20:
            print(f"    … {seen} commits, {len(tok_ids)} identifiers, {len(path_ids)} files",
                  flush=True)
            last_report = time.monotonic()

    if tc_buf:
        n_tc += len(tc_buf)
        con.executemany(
            "INSERT INTO tc(token_id, commit_id, path_id, adds, dels) VALUES(?,?,?,?,?)", tc_buf)
    con.executemany("INSERT INTO tokens(id, tok, norm) VALUES(?,?,?)", tok_rows)
    con.executemany("INSERT INTO paths(id, path) VALUES(?,?)",
                    ((v, k) for k, v in path_ids.items()))
    con.executemany("INSERT INTO token_sub(sub, token_id) VALUES(?,?)", sub_rows)

    stats = {"commits": seen, "oldest": oldest, "newest": newest,
             "files": len(path_ids), "skipped": skipped,
             "truncated": bool(args.content_max_commits)}
    return len(tok_ids), n_tc, stats


def read_meta_safe(db_path: Path) -> Optional[Dict[str, str]]:
    try:
        con = connect(db_path)
        meta = {r["k"]: r["v"] for r in con.execute("SELECT k, v FROM meta")}
        con.close()
        return meta
    except Exception:  # noqa: BLE001
        return None


# --------------------------------------------------------------------------- query


def require_index(args: argparse.Namespace) -> Tuple[Path, sqlite3.Connection, Dict[str, str]]:
    root = repo_root(Path(args.repo_dir).resolve())
    db_path = index_path_for(root, args.index_file)
    if not db_path.exists():
        raise SystemExit(f"no index at {db_path} — run: {Path(__file__).name} build --repo-dir {root}")
    con = connect(db_path)
    meta = {r["k"]: r["v"] for r in con.execute("SELECT k, v FROM meta")}
    return root, con, meta


def token_ids(con: sqlite3.Connection, term: str, family: bool = False) -> List[int]:
    """Identifiers denoting `term`.

    Default is the *concept*: every spelling whose normal form equals the term's
    (`OrderLineItem` == `order_line_item` == `ORDER_LINE_ITEM`). `family=True` widens to
    identifiers merely containing the term as a subword (`OrderLineItem` for `Order`) —
    useful for exploration, wrong for comparing two names, because the set for `Account`
    would then swallow `BillingAccount` and mask the very exchange being measured.
    """
    norm = normal_form(term)
    ids = {r["id"] for r in con.execute(
        "SELECT id FROM tokens WHERE norm = ? OR tok = ?", (norm, term.lower()))}
    if family:
        for sub in set(content_subwords(term)) or {term.lower()}:
            ids |= {r["token_id"] for r in con.execute(
                "SELECT token_id FROM token_sub WHERE sub = ?", (sub,))}
    return sorted(ids)


def term_life(con: sqlite3.Connection, term: str, family: bool = False) -> Optional[Dict[str, object]]:
    """Birth, last change, last growth and volume of an identifier — one indexed query."""
    ids = token_ids(con, term, family)
    if not ids:
        return None
    ph = ",".join("?" * len(ids))
    row = con.execute(
        f"SELECT COUNT(DISTINCT tc.commit_id) n, SUM(tc.adds) a, SUM(tc.dels) d, "
        f"MIN(c.date) first, MAX(c.date) last "
        f"FROM tc JOIN commits c ON c.id = tc.commit_id WHERE tc.token_id IN ({ph})", ids
    ).fetchone()
    if not row or not row["n"]:
        return None

    def commit_at(date: str, order: str) -> Dict[str, str]:
        r = con.execute(
            f"SELECT c.sha, c.date, c.author, c.subject FROM tc JOIN commits c ON c.id = tc.commit_id "
            f"WHERE tc.token_id IN ({ph}) AND c.date = ? ORDER BY c.id {order} LIMIT 1",
            ids + [date]).fetchone()
        return dict(r) if r else {}

    # A retired name keeps getting deleted (stale comments, leftover tests) for years
    # after nobody adds it any more, so "last touched" overstates how alive it is.
    # Measured: git.git's `get_sha1` was last *touched* in 2026 by a commit that deleted a
    # comment mentioning it — it was last *grown* in 2017.
    grown = con.execute(
        f"SELECT MAX(c.date) d FROM tc JOIN commits c ON c.id = tc.commit_id "
        f"WHERE tc.token_id IN ({ph}) AND tc.adds > tc.dels", ids).fetchone()
    last_grown = grown["d"] if grown and grown["d"] else ""
    spellings = [r["tok"] for r in con.execute(
        f"SELECT tok FROM tokens WHERE id IN ({ph}) ORDER BY tok", ids)]
    return {"birth": commit_at(row["first"], "DESC"), "last": commit_at(row["last"], "ASC"),
            "grown": commit_at(last_grown, "ASC") if last_grown else {},
            "commits": row["n"], "adds": row["a"] or 0, "dels": row["d"] or 0,
            "ids": ids, "spellings": spellings}


def term_paths(con: sqlite3.Connection, ids: Sequence[int], limit: int = 8) -> List[sqlite3.Row]:
    """Where the identifier actually occurs — files, not commits."""
    ph = ",".join("?" * len(ids))
    return list(con.execute(
        f"SELECT p.path, SUM(tc.adds) a, SUM(tc.dels) d, COUNT(DISTINCT tc.commit_id) n "
        f"FROM tc JOIN paths p ON p.id = tc.path_id WHERE tc.token_id IN ({ph}) "
        f"GROUP BY p.id ORDER BY a DESC LIMIT ?", list(ids) + [limit]))


def dir_spread(con: sqlite3.Connection, ids: Sequence[int], depth: int = 2) -> List[Tuple[str, int]]:
    """Directory distribution of an identifier's occurrences, weighted by additions."""
    ph = ",".join("?" * len(ids))
    agg: Counter = Counter()
    for r in con.execute(
            f"SELECT p.path path, SUM(tc.adds) a FROM tc JOIN paths p ON p.id = tc.path_id "
            f"WHERE tc.token_id IN ({ph}) GROUP BY p.id", list(ids)):
        parts = (r["path"] or "").split("/")
        key = "/".join(parts[:depth]) if len(parts) > depth else (
            "/".join(parts[:-1]) or "(root)")
        agg[key] += r["a"] or 0
    return agg.most_common()


def print_life(life: Optional[Dict[str, object]], head_date: str, indent: str = "",
               first_date: str = "") -> None:
    if life is None:
        print(f"{indent}- **history**: this identifier never appears in any indexed diff")
        return
    b, l = life["birth"], life["last"]  # type: ignore[index]
    print(f"{indent}- **born**: {b.get('date')} `{str(b.get('sha'))[:9]}` by {b.get('author')} — "
          f"{str(b.get('subject'))[:100]}")
    print(f"{indent}- **last changed**: {l.get('date')} `{str(l.get('sha'))[:9]}` — "
          f"{str(l.get('subject'))[:100]}")
    g = life.get("grown") or {}
    if g and g.get("date") != l.get("date"):
        print(f"{indent}- **last grown**: {g.get('date')} `{str(g.get('sha'))[:9]}` — "
              f"{str(g.get('subject'))[:100]}")
    print(f"{indent}- **volume**: {life['commits']} commits, +{life['adds']} / -{life['dels']} occurrences")
    if first_date and str(b.get("date")) == first_date:
        print(f"{indent}  - **caveat**: present in the repository's oldest indexed commit — "
              f"this is an import/squash artefact or a common English word, not a naming event")
    basis = (g.get("date") if g else None) or l.get("date")
    gap = dormant_years(str(basis), head_date)
    if gap >= 1.5:
        print(f"{indent}  - **signal**: dormant ~{gap:.1f} years — nothing has *added* it since "
              f"{basis}; reads as retired, not current vocabulary")
    elif int(life["dels"]) > int(life["adds"]) * 2 and int(life["commits"]) > 2:  # type: ignore[arg-type]
        print(f"{indent}  - **signal**: removals far outweigh additions — being phased out")


def meta_notes(meta: Dict[str, str]) -> List[str]:
    out = []
    if meta.get("content") == "1" and meta.get("diff_truncated") == "True":
        out.append(f"**Diff index is truncated** to {meta.get('diff_commits')} commits "
                   f"({meta.get('diff_oldest')} … {meta.get('diff_newest')}) — dates below are "
                   f"first-seen-in-window, not birth dates. Rebuild without --content-max-commits.")
    if meta.get("content") != "1":
        out.append("No diff index — `born`/`volume` unavailable. Rebuild with `--content`.")
    if meta.get("shallow") == "1":
        out.append("**Shallow clone** — early history is absent; every date is a lower bound.")
    scope = meta.get("scope")
    if scope:
        sc = json.loads(scope)
        bits = []
        if sc.get("pathspec"):
            bits.append("paths " + " ".join(sc["pathspec"]))
        if sc.get("since"):
            bits.append("since " + sc["since"])
        bits.append("all refs" if sc.get("all_refs") else "HEAD only")
        out.append("Indexed scope: " + ", ".join(bits))
    if meta.get("excludes") == "default":
        out.append("Vendored/generated paths were excluded from the diff pass "
                   "(vendor/, third_party/, testdata/, *.pb.go, lockfiles, …).")
    return out


def query(args: argparse.Namespace) -> int:
    root, con, meta = require_index(args)
    head_date = meta.get("newest") or head_commit_date(root)
    first_date = meta.get("oldest") or ""
    for note in meta_notes(meta):
        print(f"> {note}")

    for term in args.terms:
        print(f"\n## `{term}`\n")
        pat = word_re(term)

        life = term_life(con, term, args.family) if meta.get("content") == "1" else None
        if meta.get("content") == "1":
            print_life(life, head_date, first_date=first_date)
            if life and len(life.get("spellings") or []) > 1:
                print("- **spellings**: " + ", ".join(f"`{x}`" for x in life["spellings"][:8]))

        msg = message_hits(con, meta, term, pat, args.limit)
        print(f"- **commit messages**: {msg['total']} mention(s)"
              + (" (ranked by BM25)" if msg["ranked"] else ""))
        for r in msg["rows"]:
            print(f"  - {r['date']} `{r['sha'][:9]}` {r['subject'][:120]}")
        if msg["total"] > len(msg["rows"]):
            print(f"  - … {msg['total'] - len(msg['rows'])} more")

        issues = Counter()
        for r in msg["all_text"]:
            for num in issue_refs(r):
                issues[num] += 1
        if issues:
            print("- **referenced issues/PRs**: " + ", ".join(f"#{n}" for n, _ in issues.most_common(8)))

        rn = [r for r in con.execute(
            "SELECT c.sha, c.date, r.oldpath, r.newpath FROM renames r "
            "JOIN commits c ON c.id = r.commit_id ORDER BY c.date DESC")
            if pat.search(r["oldpath"]) or pat.search(r["newpath"])]
        if rn:
            print(f"- **file renames**: {len(rn)}")
            for r in rn[: args.limit]:
                print(f"  - {r['date']} `{r['sha'][:9]}` {r['oldpath']} → {r['newpath']}")

        if life:
            spread = dir_spread(con, life["ids"])
            tot = sum(n for _, n in spread) or 1
            if spread:
                print("- **where it occurs** (by directory): "
                      + ", ".join(f"{d} {n / tot:.0%}" for d, n in spread[:4]))
                if len(spread) >= 2 and spread[0][1] / tot < 0.8:
                    print(f"  - split across {len(spread)} directories — run "
                          f"`contexts {term}` before assuming one meaning")
            files = term_paths(con, life["ids"], args.limit)
            if files:
                print("- **busiest files**:")
                for r in files:
                    print(f"  - {r['path']} (+{r['a']} / -{r['d']}, {r['n']} commits)")
        named_paths = Counter()
        for r in con.execute("SELECT path, COUNT(*) n FROM files GROUP BY path"):
            if pat.search(r["path"]):
                named_paths[r["path"]] = r["n"]
        if named_paths:
            print(f"- **paths whose name carries the term**: {len(named_paths)}")
            for path, n in named_paths.most_common(args.limit):
                print(f"  - {path} ({n} changes)")

        if msg["years"] and len(msg["years"]) > 1:
            print("- **mentions by year**: " + " ".join(f"{y}:{n}" for y, n in sorted(msg["years"].items())))

    con.close()
    print()
    return 0


def message_hits(con: sqlite3.Connection, meta: Dict[str, str], term: str,
                 pat: re.Pattern, limit: int) -> Dict[str, object]:
    """BM25-ranked message hits when FTS5 exists, else a LIKE scan; both verified by regex."""
    rows: List[sqlite3.Row] = []
    ranked = False
    if meta.get("fts5") == "1":
        try:
            # Query the subwords, not the literal: FTS5 tokenises `order_line_item` into
            # three words, so a PascalCase `OrderLineItem` would match nothing. word_re
            # below still filters, and it accepts the spaced form.
            words = subwords(term) or [term]
            rows = list(con.execute(
                "SELECT c.sha, c.date, c.subject, c.body FROM commits_fts f "
                "JOIN commits c ON c.id = f.rowid WHERE commits_fts MATCH ? "
                "ORDER BY bm25(commits_fts, 4.0, 1.0)", (fts_query(" ".join(words)),)))
            ranked = True
        except sqlite3.OperationalError:
            rows = []
    if not rows:
        like = f"%{term}%"
        rows = list(con.execute(
            "SELECT sha, date, subject, body FROM commits "
            "WHERE subject LIKE ? OR body LIKE ? ORDER BY date DESC", (like, like)))
    hits = [r for r in rows if pat.search(r["subject"] or "") or pat.search(r["body"] or "")]
    return {
        "total": len(hits), "ranked": ranked, "rows": hits[:limit],
        "all_text": [f"{r['subject']} {r['body']}" for r in hits],
        "years": Counter(r["date"][:4] for r in hits),
    }


def shared_commits(con: sqlite3.Connection, ia: List[int], ib: List[int]) -> List[sqlite3.Row]:
    """Commits touching both identifier sets, with per-side totals and same-file totals.

    `same_file_*` restricts the exchange to paths where BOTH names occur in that commit —
    a rename edits one file to swap one name for the other, whereas ordinary churn merely
    happens to touch both names somewhere in a large commit.
    """
    pa, pb = ",".join("?" * len(ia)), ",".join("?" * len(ib))
    return list(con.execute(
        f"""
        WITH t AS (
          SELECT tc.commit_id cid, tc.path_id pid,
                 SUM(CASE WHEN tc.token_id IN ({pa}) THEN tc.adds ELSE 0 END) aa,
                 SUM(CASE WHEN tc.token_id IN ({pa}) THEN tc.dels ELSE 0 END) ad,
                 SUM(CASE WHEN tc.token_id IN ({pb}) THEN tc.adds ELSE 0 END) ba,
                 SUM(CASE WHEN tc.token_id IN ({pb}) THEN tc.dels ELSE 0 END) bd
          FROM tc WHERE tc.token_id IN ({pa}) OR tc.token_id IN ({pb})
          GROUP BY tc.commit_id, tc.path_id
        )
        SELECT c.sha, c.date, c.subject,
               SUM(t.aa) a_add, SUM(t.ad) a_del, SUM(t.ba) b_add, SUM(t.bd) b_del,
               SUM(CASE WHEN t.ad > t.aa AND t.ba > t.bd THEN t.ad - t.aa ELSE 0 END) sf_shrink,
               SUM(CASE WHEN t.ad > t.aa AND t.ba > t.bd THEN t.ba - t.bd ELSE 0 END) sf_grow,
               SUM(CASE WHEN t.ad > t.aa AND t.ba > t.bd THEN 1 ELSE 0 END) sf_files,
               SUM(CASE WHEN t.bd > t.ba AND t.aa > t.ad THEN 1 ELSE 0 END) sf_files_rev
        FROM t JOIN commits c ON c.id = t.cid
        GROUP BY t.cid
        HAVING SUM(t.aa + t.ad) > 0 AND SUM(t.ba + t.bd) > 0
        ORDER BY c.date""",
        ia + ia + ib + ib + ia + ib))


def score_direction(rows: Sequence[sqlite3.Row], forward: bool,
                    shrink_re: re.Pattern, grow_re: re.Pattern) -> Dict[str, object]:
    """Commits where one name net-shrinks while the other net-grows.

    A swap is a NET exchange. Testing "any deletion of A and any addition of B" fires on
    ordinary churn: measured on a real repo it labelled 105 of 174 commits touching two
    unrelated integrations as rename candidates — including commits where BOTH names were
    net-removed and commits where A actually grew.
    """
    scored = []
    for r in rows:
        if forward:
            net_shrink, net_grow = r["a_del"] - r["a_add"], r["b_add"] - r["b_del"]
            files = r["sf_files"]
        else:
            net_shrink, net_grow = r["b_del"] - r["b_add"], r["a_add"] - r["a_del"]
            files = r["sf_files_rev"]
        if net_shrink >= MIN_NET_SWAP and net_grow >= MIN_NET_SWAP:
            # same-file exchanges outrank whole-commit ones
            scored.append((files * 1000 + min(net_shrink, net_grow), net_shrink, net_grow,
                           files, r))
    scored.sort(key=lambda x: -x[0])
    # A subject announces a rename only if it carries a rename word AND names BOTH sides —
    # "Rename sha1_array to oid_array", "Change minion to node". Accepting one side lets an
    # unrelated "Rename Telegram meeting wrapper" certify `club` -> `meeting`.
    named, hinted = [], []
    for x in scored:
        subj = x[4]["subject"] or ""
        if not RENAME_WORD_RE.search(subj):
            continue
        hits = bool(shrink_re.search(subj)) + bool(grow_re.search(subj))
        (named if hits == 2 else hinted).append(x)
    same_file = [x for x in scored if x[3]]
    return {"scored": scored, "named": named, "hinted": hinted, "same_file": same_file}


def pair(args: argparse.Namespace) -> int:
    root, con, meta = require_index(args)
    head_date = meta.get("newest") or head_commit_date(root)
    first_date = meta.get("oldest") or ""
    for note in meta_notes(meta):
        print(f"> {note}")
    terms = args.terms

    if meta.get("content") != "1":
        print("\n> No diff index — rebuild with `--content` to compare names.")
        con.close()
        return 0

    lives: Dict[str, Optional[Dict[str, object]]] = {}
    print("\n## Life of each name\n")
    for term in terms:
        lives[term] = term_life(con, term, args.family)
        print(f"### `{term}`")
        print_life(lives[term], head_date, first_date=first_date)
        print()

    good = {t: v for t, v in lives.items() if v}
    if len(good) > 1:
        by_birth = sorted(good.items(), key=lambda kv: str(kv[1]["birth"].get("date")))  # type: ignore[index]
        print("> **Birth order**: " + " → ".join(
            f"`{t}` ({v['birth'].get('date')})" for t, v in by_birth))  # type: ignore[index]

    print("\n## Exchange evidence and verdict\n")
    for i, a in enumerate(terms):
        for b in terms[i + 1:]:
            verdict_for(con, a, b, lives, head_date, args.limit, args.family)

    con.close()
    print()
    return 0


def verdict_for(con: sqlite3.Connection, a: str, b: str,
                lives: Dict[str, Optional[Dict[str, object]]], head_date: str,
                limit: int, family: bool) -> None:
    ia, ib = token_ids(con, a, family), token_ids(con, b, family)
    if not ia or not ib:
        missing = a if not ia else b
        print(f"### `{a}` vs `{b}`\n\n- `{missing}` never appears in any indexed diff — "
              f"nothing to compare. Check the spelling, or the name may live only in docs "
              f"or in paths (see `query {missing}`).\n")
        return
    overlap = set(ia) & set(ib)
    if overlap:
        # One name contains the other (`Account` vs `BillingAccount` under --family):
        # keeping the shared identifiers in both sets makes B's additions cancel A's
        # deletions and hides the exchange entirely.
        ia = [i for i in ia if i not in overlap]
        ib = [i for i in ib if i not in overlap]
        if not ia or not ib:
            print(f"### `{a}` vs `{b}`\n\n- these two names resolve to the same identifiers — "
                  f"they are spellings of one concept, not competing names.\n")
            return

    rows = shared_commits(con, ia, ib)
    ra, rb = word_re(a), word_re(b)
    fwd = score_direction(rows, True, ra, rb)
    rev = score_direction(rows, False, rb, ra)

    # Direction is inferred, not taken from argument order — an agent asking about two
    # names rarely knows which way a rename went.
    def strength(d):
        return (len(d["named"]), len(d["same_file"]), len(d["scored"]))

    if strength(rev) > strength(fwd):
        old, new, best, other = b, a, rev, fwd
    else:
        old, new, best, other = a, b, fwd, rev

    def grown(t: str) -> str:
        v = lives.get(t) or {}
        g = v.get("grown") or {}
        return str(g.get("date") or (v.get("last") or {}).get("date") or "")

    scored, named, same_file = best["scored"], best["named"], best["same_file"]
    share = len(scored) / max(1, len(rows))
    # Noise floor: in a busy codebase a couple of incidental exchanges out of hundreds of
    # shared commits means nothing. Measured on git.git, `bisect`/`rebase` — two unrelated
    # concepts — produced 2 exchanges out of 145 shared commits.
    # Same-file exchanges are stronger evidence than whole-commit ones, so they clear a
    # lower bar — but not no bar: measured on git.git, `bisect`/`rebase` (unrelated) produced
    # 2 same-file exchanges in 111 shared commits, which is still churn.
    sf_share = len(same_file) / max(1, len(rows))
    sf_signal = len(same_file) >= 2 and sf_share >= NOISE_FLOOR / 2
    signal = bool(named) or sf_signal or (len(scored) >= 2 and share >= NOISE_FLOOR)

    if not signal:
        # With no exchange evidence the labels must not depend on which name was typed
        # first: orient by dormancy instead.
        if dormant_years(grown(b), head_date) > dormant_years(grown(a), head_date):
            old, new = b, a
        else:
            old, new = a, b
    stale = dormant_years(grown(old), head_date) - dormant_years(grown(new), head_date)
    gap = abs(stale)

    print(f"### `{a}` vs `{b}`\n")
    print(f"- shared commits: {len(rows)} · net exchanges `{old}`→`{new}`: {len(scored)} "
          f"(reverse direction: {len(other['scored'])}) · same-file exchanges: {len(same_file)} "
          f"· subjects naming a rename: {len(named)}")
    print(f"- last grown: `{old}` {grown(old) or '—'} · `{new}` {grown(new) or '—'}")

    if named and scored:
        line = (f"**RENAME — strong.** `{old}` → `{new}` — net exchange in "
                f"{plural(len(scored), 'commit')}, announced in "
                f"{plural(len(named), 'subject')}.")
    elif sf_signal and stale >= 2:
        line = (f"**RENAME — probable.** `{old}` → `{new}` — {plural(len(same_file), 'commit')} "
                f"swap them inside the same files, and `{old}` stopped growing {gap:.1f} years "
                f"earlier. No subject says so — read the top commits before deciding.")
    elif sf_signal:
        line = (f"**RENAME — probable.** `{old}` → `{new}` — {plural(len(same_file), 'commit')} "
                f"swap them inside the same files. Both names are still being added, so the "
                f"migration may be unfinished.")
    elif signal and stale >= 2:
        line = (f"**RENAME — possible.** `{old}` → `{new}` — net exchange in "
                f"{plural(len(scored), 'commit')} and `{old}` stopped growing {gap:.1f} years "
                f"earlier, but never in the same file. Weak: verify with `git show`.")
    elif signal:
        line = (f"**DRIFT or PARTIAL MIGRATION — weak.** {plural(len(scored), 'commit')} shift "
                f"`{old}` → `{new}`, but never within one file and both names are still being "
                f"added. Check whether they occupy the same paths.")
    elif stale >= 2:
        line = (f"**NOT A RENAME.** No meaningful exchange between them. `{old}` merely stopped "
                f"growing {gap:.1f} years before `{new}` — an abandoned concept, not a replaced "
                f"name.")
    else:
        line = ("**COEXISTENCE.** No exchange, both still growing — two live concepts, or synonym "
                "drift. The path split below is the evidence that separates those two cases.")
    print(f"- verdict: {line}")

    if scored:
        if not signal:
            print(f"- below the noise floor: {len(scored)} exchange(s) in {len(rows)} shared "
                  f"commits ({share:.0%}), none inside one file and no subject names a rename — "
                  f"listed for completeness, not as evidence:")
        else:
            print("- strongest exchanges (same-file ones first):")
        for _s, net_old, net_new, files, r in scored[:limit]:
            mark = f", {plural(files, 'file')} swapped in place" if files else ""
            print(f"  - {r['date']} `{r['sha'][:9]}` (net -{net_old} `{old}` / +{net_new} "
                  f"`{new}`{mark}) {r['subject'][:80]}")
        if named:
            print("- subjects that announce it (both names present):")
            for _s, _no, _nn, _f, r in named[:limit]:
                print(f"  - {r['date']} `{r['sha'][:9]}` {r['subject'][:100]}")
        elif best.get("hinted"):
            print("- subjects with rename wording but only one of the two names "
                  "(weaker — may be about something else):")
            for _s, _no, _nn, _f, r in best["hinted"][:limit]:
                print(f"  - {r['date']} `{r['sha'][:9]}` {r['subject'][:100]}")
        if signal and share > 0.4 and not named and not sf_signal:
            print(f"- **caution**: {share:.0%} of shared commits look like exchanges, none inside "
                  f"one file and none names a rename — in a busy codebase that is ordinary churn.")
        print("- confirm before acting: `git show <sha> -- <path>`")

    print_split(con, a, b, ia, ib, limit)
    print()


def print_split(con: sqlite3.Connection, a: str, b: str,
                ia: List[int], ib: List[int], limit: int) -> None:
    """Do the two names live in the same code, or in disjoint parts of the tree?

    This is the polysemy test: one word meaning two things in two modules shows up as two
    directory clusters with no shared files. It needs identifier x FILE granularity —
    commit-level co-occurrence cannot see it, because one commit touches many files.
    """
    pa, pb = ",".join("?" * len(ia)), ",".join("?" * len(ib))
    both = con.execute(
        f"SELECT COUNT(*) n FROM (SELECT tc.path_id FROM tc WHERE tc.token_id IN ({pa}) "
        f"INTERSECT SELECT tc.path_id FROM tc WHERE tc.token_id IN ({pb}))", ia + ib).fetchone()["n"]
    only_a = con.execute(
        f"SELECT COUNT(DISTINCT path_id) n FROM tc WHERE token_id IN ({pa})", ia).fetchone()["n"]
    only_b = con.execute(
        f"SELECT COUNT(DISTINCT path_id) n FROM tc WHERE token_id IN ({pb})", ib).fetchone()["n"]
    print(f"- files: `{a}` in {only_a}, `{b}` in {only_b}, **both in {both}**")
    if both == 0:
        print(f"  - **disjoint** — no file has ever contained both. Two concepts that share a "
              f"vocabulary, not two names for one thing. Candidate bounded-context split.")
    else:
        overlap_share = both / max(1, min(only_a, only_b))
        if overlap_share >= 0.5:
            print(f"  - heavily shared ({overlap_share:.0%} of the smaller set) — they live in the "
                  f"same code, so a rename or synonym drift is plausible.")
    for label, ids in ((a, ia), (b, ib)):
        spread = dir_spread(con, ids)[:4]
        if spread:
            tot = sum(n for _, n in spread) or 1
            print(f"  - `{label}` by directory: "
                  + ", ".join(f"{d} {n / tot:.0%}" for d, n in spread))


def contexts(args: argparse.Namespace) -> int:
    """Where one identifier lives — the polysemy check for a single name."""
    root, con, meta = require_index(args)
    for note in meta_notes(meta):
        print(f"> {note}")
    if meta.get("content") != "1":
        print("\n> No diff index — rebuild with `--content`.")
        con.close()
        return 0
    for term in args.terms:
        ids = token_ids(con, term, args.family)
        print(f"\n## `{term}`\n")
        if not ids:
            print("- never appears in any indexed diff")
            continue
        spellings = [r["tok"] for r in con.execute(
            f"SELECT tok FROM tokens WHERE id IN ({','.join('?' * len(ids))}) ORDER BY tok", ids)]
        print(f"- spellings indexed as this concept: " + ", ".join(f"`{s}`" for s in spellings[:8]))
        spread = dir_spread(con, ids)
        tot = sum(n for _, n in spread) or 1
        print(f"- directories ({len(spread)} total):")
        for d, n in spread[: args.limit]:
            print(f"  - {d:<40} {n / tot:5.0%}  ({n} additions)")
        if len(spread) >= 2 and spread[0][1] / tot < 0.8:
            top = spread[:2]
            print(f"- **possible polysemy**: the name is split across `{top[0][0]}` "
                  f"({top[0][1] / tot:.0%}) and `{top[1][0]}` ({top[1][1] / tot:.0%}). "
                  f"Read one file from each before assuming they mean the same thing.")
        print("- busiest files:")
        for r in term_paths(con, ids, args.limit):
            print(f"  - {r['path']} (+{r['a']} / -{r['d']}, {r['n']} commits)")
    con.close()
    print()
    return 0


def search(args: argparse.Namespace) -> int:
    """BM25-ranked full-text search over commit messages."""
    root, con, meta = require_index(args)
    if meta.get("fts5") != "1":
        raise SystemExit("this Python's sqlite3 was built without FTS5 — `search` unavailable")
    q = fts_query(" ".join(args.terms))
    if not q:
        raise SystemExit("empty search query")
    rows = con.execute(
        "SELECT c.sha, c.date, c.author, c.subject, bm25(commits_fts, 4.0, 1.0) score "
        "FROM commits_fts f JOIN commits c ON c.id = f.rowid "
        "WHERE commits_fts MATCH ? ORDER BY score LIMIT ?", (q, args.limit)).fetchall()
    if not rows:
        print("no matches")
    for r in rows:
        print(f"{r['date']} `{r['sha'][:9]}` {r['subject'][:110]}")
    con.close()
    return 0


def status(args: argparse.Namespace) -> int:
    root, con, meta = require_index(args)
    db_path = index_path_for(root, args.index_file)
    print(f"index: {db_path}  ({db_path.stat().st_size / 1024 / 1024:.0f} MB)")
    print(json.dumps(meta, indent=2))
    con.close()
    return 0


def clean(args: argparse.Namespace) -> int:
    root = repo_root(Path(args.repo_dir).resolve())
    db_path = index_path_for(root, args.index_file)
    removed = False
    if db_path.exists():
        db_path.unlink()
        print(f"removed {db_path}")
        removed = True
    legacy = db_path.with_suffix("")  # TSV directory written by earlier versions
    if legacy.is_dir():
        shutil.rmtree(legacy)
        print(f"removed {legacy}")
        removed = True
    if not removed:
        print(f"nothing to remove at {db_path}")
    parent = db_path.parent
    if parent.exists() and parent.name == "ubiquitous-language-git-index" and not any(parent.iterdir()):
        shutil.rmtree(parent)
    return 0


# --------------------------------------------------------------------------- cli


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    def common(p: argparse.ArgumentParser) -> None:
        p.add_argument("--repo-dir", default=".", help="path inside the git repository (default: .)")
        p.add_argument("--index-file", default=None, help="override the temp index location")

    b = sub.add_parser("build", help="build or refresh the index")
    common(b)
    b.add_argument("--content", action="store_true",
                   help="also index identifiers from diffs over the FULL history (the useful mode)")
    b.add_argument("--since", default=None, help="limit history, e.g. '3 years ago'")
    b.add_argument("--max-commits", type=int, default=None, help="cap commits for the message pass")
    b.add_argument("--content-max-commits", type=int, default=None,
                   help="cap commits for the diff pass (default: no cap — index everything)")
    b.add_argument("--pathspec", nargs="*", default=None, help="limit to these paths")
    b.add_argument("--all-refs", action="store_true",
                   help="walk every ref, not just HEAD — picks up side branches (and their noise)")
    b.add_argument("--no-default-excludes", action="store_true",
                   help="do not exclude vendor/, third_party/, testdata/, generated and lock files")
    b.add_argument("--timeout", type=int, default=3600)
    b.add_argument("--refresh", action="store_true", help="rebuild even if the index looks current")
    b.set_defaults(func=build)

    q = sub.add_parser("query", help="evidence report for one or more terms")
    common(q)
    q.add_argument("terms", nargs="+")
    q.add_argument("--limit", type=int, default=10)
    q.add_argument("--family", action="store_true",
                   help="also match identifiers merely containing the term as a subword")
    q.set_defaults(func=query)

    p = sub.add_parser("pair", help="compare competing names for the same concept")
    common(p)
    p.add_argument("terms", nargs="+")
    p.add_argument("--limit", type=int, default=10)
    p.add_argument("--family", action="store_true",
                   help="widen each name to identifiers containing it (shared ones are dropped)")
    p.set_defaults(func=pair)

    cx = sub.add_parser("contexts", help="where one identifier lives — the polysemy check")
    common(cx)
    cx.add_argument("terms", nargs="+")
    cx.add_argument("--limit", type=int, default=8)
    cx.add_argument("--family", action="store_true")
    cx.set_defaults(func=contexts)

    s = sub.add_parser("search", help="BM25 full-text search over commit messages")
    common(s)
    s.add_argument("terms", nargs="+")
    s.add_argument("--limit", type=int, default=15)
    s.set_defaults(func=search)

    st = sub.add_parser("status", help="show index metadata")
    common(st)
    st.set_defaults(func=status)

    c = sub.add_parser("clean", help="delete the index")
    common(c)
    c.set_defaults(func=clean)

    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except KeyboardInterrupt:
        return 130
    except subprocess.TimeoutExpired:
        eprint("git timed out — narrow the scope with --since / --pathspec / --content-max-commits")
        return 2
    except BrokenPipeError:
        return 0
    except RuntimeError as exc:
        eprint(str(exc))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
