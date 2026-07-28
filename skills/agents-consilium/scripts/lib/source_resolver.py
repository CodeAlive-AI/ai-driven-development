#!/usr/bin/env python3
"""Resolve an exploration source into a concrete, trustworthy working tree.

Used by `consilium explore`. Responsibilities, in order:

  1. classify the source spec  — local path | GitHub shorthand | remote URL
  2. reject unsafe git transports before any subprocess touches them
  3. materialize remote sources into an isolated workspace
  4. collect git provenance the model cannot obtain itself (no shell in explore)
  5. build a bounded file inventory the model would otherwise pay many
     list_dir turns to reconstruct — without .gitignore awareness

Prints one JSON object on stdout. Progress/diagnostics go to stderr only.

Isolation layout for remote sources:

    <workspace>/            <- neutral; becomes the agent CWD
      source/               <- the clone; agent explores this subtree

The agent's CWD is deliberately the *parent* of the clone so that repo-local
agent configuration (.grok/config.toml, AGENTS.md, CLAUDE.md) inside `source/`
is not discovered as active project configuration. Verified against Grok Build
0.2.112 via `grok inspect`: CWD=<workspace> loads only user-level instructions,
CWD=<workspace>/source additionally loads the repository's own AGENTS.md and
CLAUDE.md. This is a real boundary, but only for *project* config — user-level
configuration (~/.grok, ~/.claude) still loads and is treated as trusted.

Exit codes:
  0 — resolved
  6 — source error (bad spec, blocked transport, clone/ref failure)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlsplit, urlunsplit

EXIT_OK = 0
EXIT_SOURCE_ERROR = 6

# Inventory bounds. A repository larger than this gets a directory-level summary
# instead of a file list — a truncated file list reads as complete and would
# silently steer the model away from whole subtrees.
MAX_INVENTORY_FILES = 2000
MAX_INVENTORY_CHARS = 60000

SHORTHAND_RE = re.compile(r"^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+$")
SCP_LIKE_RE = re.compile(r"^[A-Za-z0-9._-]+@[A-Za-z0-9._-]+:[^/].*$")
SHA_RE = re.compile(r"^[0-9a-fA-F]{7,40}$")

ALLOWED_SCHEMES = {"https", "ssh", "git+ssh"}
# git remote helpers that can execute arbitrary local programs or read local
# paths. `file` is separately gated because the offline test suite needs it.
BLOCKED_SCHEME_PREFIXES = ("ext", "transport", "fd", "gcrypt")

WALK_SKIP_DIRS = {
    ".git", ".hg", ".svn", "node_modules", "bower_components", "vendor",
    "dist", "build", "out", "target", "bin", "obj", ".next", ".nuxt",
    "__pycache__", ".venv", "venv", ".tox", ".mypy_cache", ".pytest_cache",
    ".gradle", ".idea", ".vscode", "Pods", "DerivedData", ".terraform",
}


def die(msg: str) -> "NoReturn":  # type: ignore[valid-type]
    print(f"Error: {msg}", file=sys.stderr)
    sys.exit(EXIT_SOURCE_ERROR)


def note(msg: str) -> None:
    sys.stderr.write(f"[consilium] explore {msg}\n")
    sys.stderr.flush()


# --------------------------------------------------------------------------
# source classification
# --------------------------------------------------------------------------

def redact_url(url: str) -> str:
    """Strip userinfo (user:token@) from a URL before it reaches logs or meta."""
    if SCP_LIKE_RE.match(url):
        # git@host:path — the "user" here is the ssh account, not a secret.
        return url
    try:
        parts = urlsplit(url)
    except ValueError:
        return "<unparsable-url>"
    if not parts.netloc or "@" not in parts.netloc:
        return url
    host = parts.netloc.rsplit("@", 1)[1]
    return urlunsplit((parts.scheme, host, parts.path, "", ""))


def classify(spec: str, allow_local_remote: bool, allow_insecure: bool) -> Tuple[str, str]:
    """Return (kind, value). kind is 'local' or 'remote'.

    An existing local path always wins over GitHub shorthand: a directory named
    `owner/repo` under the cwd is a real thing a user can be sitting next to,
    and silently cloning from the network instead would be surprising.
    """
    if not spec:
        die("empty --repo value")
    if spec.startswith("-"):
        die(f"refusing source that looks like a flag: {spec}")

    expanded = os.path.expanduser(spec)
    if os.path.isdir(expanded):
        return "local", os.path.realpath(expanded)

    if SHORTHAND_RE.match(spec):
        return "remote", f"https://github.com/{spec}"

    if SCP_LIKE_RE.match(spec):
        return "remote", spec

    if "://" in spec:
        scheme = spec.split("://", 1)[0].lower()
        base = scheme.split("+", 1)[0]
        if base in BLOCKED_SCHEME_PREFIXES or "::" in scheme:
            die(f"blocked git transport: {scheme}:// (arbitrary helper execution)")
        if base == "file":
            if not allow_local_remote:
                die(
                    "file:// sources are blocked. Pass the path directly as "
                    "--repo <path> to explore a local tree."
                )
            return "remote", spec
        if base == "http":
            if not allow_insecure:
                die(
                    "plain http:// is blocked (clone content is unauthenticated). "
                    "Use https://, or set CONSILIUM_EXPLORE_ALLOW_INSECURE=1."
                )
            return "remote", spec
        if base not in ALLOWED_SCHEMES:
            die(f"unsupported git transport: {scheme}://")
        return "remote", spec

    if "::" in spec:
        die(f"blocked git remote helper syntax: {spec}")

    die(
        f"cannot resolve source: {spec} (not an existing directory, not owner/repo, "
        "not a supported git URL)"
    )


# --------------------------------------------------------------------------
# git helpers
# --------------------------------------------------------------------------

def git_env() -> Dict[str, str]:
    env = dict(os.environ)
    # Never block on an interactive credential or host-key prompt: explore runs
    # unattended inside another agent's tool call.
    env["GIT_TERMINAL_PROMPT"] = "0"
    env.setdefault("GIT_SSH_COMMAND", "ssh -oBatchMode=yes")
    # Submodules and LFS payloads are out of scope for v1 exploration.
    env["GIT_LFS_SKIP_SMUDGE"] = "1"
    return env


def run_git(args: List[str], cwd: Optional[str] = None, check: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(
        ["git"] + args,
        cwd=cwd,
        env=git_env(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if check and proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip().splitlines()
        tail = detail[-1] if detail else f"exit {proc.returncode}"
        raise RuntimeError(tail)
    return proc


def git_out(args: List[str], cwd: str) -> str:
    proc = run_git(args, cwd=cwd, check=False)
    return proc.stdout.strip() if proc.returncode == 0 else ""


def clone(url: str, dest: str, ref: Optional[str], depth: str) -> Dict[str, Any]:
    """Materialize `url` at `ref` into `dest`. Returns clone strategy info.

    `git clone --branch` resolves branches and tags only. A raw commit SHA needs
    the init+fetch path, and a server that refuses SHA-in-want needs a full
    clone. Silently ignoring --ref would be worse than any of these fallbacks.
    """
    depth_args = [] if depth == "full" else ["--depth", depth]
    common = ["--no-recurse-submodules", "--no-tags"]
    redacted = redact_url(url)

    if ref is None:
        note(f"clone {redacted} (depth={depth})")
        run_git(["clone", "--quiet"] + depth_args + common + [url, dest])
        return {"strategy": "clone", "shallow": depth != "full"}

    # 1. branch or tag
    note(f"clone {redacted} at ref={ref} (depth={depth})")
    proc = run_git(
        ["clone", "--quiet", "--branch", ref] + depth_args + common + [url, dest],
        check=False,
    )
    if proc.returncode == 0:
        return {"strategy": "clone-branch", "shallow": depth != "full"}

    if os.path.isdir(dest):
        shutil.rmtree(dest, ignore_errors=True)
    os.makedirs(dest, exist_ok=True)

    # 2. explicit commit fetch (works on GitHub for reachable SHAs)
    if SHA_RE.match(ref):
        note(f"ref {ref} is not a branch/tag — fetching commit directly")
        try:
            run_git(["init", "--quiet"], cwd=dest)
            run_git(["remote", "add", "origin", url], cwd=dest)
            run_git(["fetch", "--quiet"] + depth_args + ["origin", ref], cwd=dest)
            run_git(["checkout", "--quiet", "FETCH_HEAD"], cwd=dest)
            return {"strategy": "fetch-commit", "shallow": depth != "full"}
        except RuntimeError as exc:
            note(f"commit fetch failed ({exc}); falling back to a full clone")

    # 3. full clone, then check the ref out locally
    shutil.rmtree(dest, ignore_errors=True)
    try:
        run_git(["clone", "--quiet"] + common + [url, dest])
        run_git(["checkout", "--quiet", ref], cwd=dest)
    except RuntimeError as exc:
        die(f"cannot resolve ref '{ref}' in {redacted}: {exc}")
    return {"strategy": "full-clone-checkout", "shallow": False}


def collect_git_facts(root: str) -> Dict[str, Any]:
    """Git provenance. The explore agent has no shell, so this is the only path."""
    facts: Dict[str, Any] = {
        "is_git": False,
        "resolved_commit": None,
        "branch": None,
        "dirty": None,
        "shallow": None,
        "commit_subject": None,
        "commit_date": None,
    }
    inside = git_out(["rev-parse", "--is-inside-work-tree"], root)
    if inside != "true":
        return facts
    facts["is_git"] = True
    facts["resolved_commit"] = git_out(["rev-parse", "HEAD"], root) or None
    branch = git_out(["rev-parse", "--abbrev-ref", "HEAD"], root)
    facts["branch"] = None if branch in ("", "HEAD") else branch
    facts["shallow"] = git_out(["rev-parse", "--is-shallow-repository"], root) == "true"
    status = run_git(["status", "--porcelain"], cwd=root, check=False)
    facts["dirty"] = bool(status.stdout.strip()) if status.returncode == 0 else None
    facts["commit_subject"] = git_out(["log", "-1", "--format=%s"], root) or None
    facts["commit_date"] = git_out(["log", "-1", "--format=%cI"], root) or None
    return facts


# --------------------------------------------------------------------------
# file inventory
# --------------------------------------------------------------------------

def list_tracked(root: str) -> Optional[List[str]]:
    proc = run_git(["ls-files", "-z"], cwd=root, check=False)
    if proc.returncode != 0:
        return None
    return [p for p in proc.stdout.split("\0") if p]


def walk_files(root: str) -> List[str]:
    found: List[str] = []
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        dirnames[:] = [
            d for d in dirnames
            if d not in WALK_SKIP_DIRS and not (d.startswith(".") and d != ".github")
        ]
        for name in filenames:
            rel = os.path.relpath(os.path.join(dirpath, name), root)
            found.append(rel)
            if len(found) > MAX_INVENTORY_FILES * 4:
                return found
    return found


def summarize_dirs(paths: List[str]) -> List[str]:
    """Directory-level rollup for repositories too large to list file by file."""
    counts: Dict[str, int] = {}
    for p in paths:
        parts = p.split("/")
        key = "/".join(parts[:2]) + "/" if len(parts) > 2 else (
            parts[0] + "/" if len(parts) == 2 else "(root)"
        )
        counts[key] = counts.get(key, 0) + 1
    return [f"{k}  ({v} files)" for k, v in sorted(counts.items(), key=lambda kv: -kv[1])]


def build_inventory(root: str, is_git: bool) -> Dict[str, Any]:
    paths = list_tracked(root) if is_git else None
    source = "git ls-files"
    if paths is None:
        paths = walk_files(root)
        source = "directory walk (build artifacts and dot-directories excluded)"

    paths.sort()
    total = len(paths)
    if total <= MAX_INVENTORY_FILES:
        body = "\n".join(paths)
        truncated = False
        if len(body) > MAX_INVENTORY_CHARS:
            body = "\n".join(summarize_dirs(paths))
            truncated = True
            source += "; too large to list individually — directory rollup"
    else:
        body = "\n".join(summarize_dirs(paths))
        truncated = True
        source += f"; {total} files exceed the {MAX_INVENTORY_FILES} listing cap — directory rollup"

    return {"source": source, "total_files": total, "truncated": truncated, "body": body}


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Resolve a consilium explore source")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--ref", default=None)
    ap.add_argument("--depth", default="1")
    ap.add_argument("--resolve-only", action="store_true",
                    help="Classify and validate the source, then exit without "
                         "cloning or reading anything. Used by tests and by "
                         "callers that only need the redacted identity.")
    ap.add_argument("--isolate", action="store_true",
                    help="Remote sources always isolate; this forces the neutral "
                         "workspace layout for local sources too (not used in v1).")
    args = ap.parse_args()

    if args.depth != "full":
        if not args.depth.isdigit() or int(args.depth) < 1:
            die(f"--depth must be a positive integer or 'full' (got: {args.depth})")

    if shutil.which("git") is None:
        die("git not found in PATH")

    allow_local_remote = os.environ.get("CONSILIUM_EXPLORE_ALLOW_LOCAL_REMOTE") == "1"
    allow_insecure = os.environ.get("CONSILIUM_EXPLORE_ALLOW_INSECURE") == "1"
    kind, value = classify(args.repo, allow_local_remote, allow_insecure)

    # Never carry the raw spec forward: when it is a URL with embedded
    # credentials, `source_input` would persist that token into meta.json and
    # into every progress line derived from it.
    safe_input = redact_url(args.repo) if "://" in args.repo else args.repo

    result: Dict[str, Any] = {
        "source_kind": kind,
        "source_input": safe_input,
        "requested_ref": args.ref,
        "clone_depth": None,
        "workspace": None,
        "exploration_root": None,
        "agent_cwd": None,
        "source_rel": ".",
        "clone_strategy": None,
    }

    if args.resolve_only:
        # Classification and transport validation only: no clone, no filesystem
        # read, no network. Everything a caller needs to decide whether this
        # source is acceptable before paying for it.
        result["source_url_redacted"] = None if kind == "local" else redact_url(value)
        if kind == "local":
            result["exploration_root"] = value
            result["agent_cwd"] = value
        json.dump(result, sys.stdout)
        sys.stdout.write("\n")
        return EXIT_OK

    if kind == "local":
        if args.ref:
            die("--ref applies to remote sources only; check out the ref locally instead")
        root = value
        result["source_url_redacted"] = None
        result["exploration_root"] = root
        result["agent_cwd"] = root
        result["isolation"] = "trusted-local"
    else:
        result["source_url_redacted"] = redact_url(value)
        workspace = tempfile.mkdtemp(prefix="consilium-explore.")
        os.chmod(workspace, 0o700)
        dest = os.path.join(workspace, "source")
        try:
            info = clone(value, dest, args.ref, args.depth)
        except RuntimeError as exc:
            shutil.rmtree(workspace, ignore_errors=True)
            die(f"clone failed for {result['source_url_redacted']}: {exc}")
        result["clone_depth"] = args.depth
        result["clone_strategy"] = info["strategy"]
        result["workspace"] = workspace
        result["exploration_root"] = dest
        # Neutral parent as CWD: keeps the clone's own agent configuration from
        # being discovered as active project configuration.
        result["agent_cwd"] = workspace
        result["source_rel"] = "source"
        result["isolation"] = "isolated-workspace"

    root = result["exploration_root"]
    facts = collect_git_facts(root)
    if kind == "local" and not facts["is_git"]:
        result["source_kind"] = "local-nongit"
    result["git"] = facts
    result["inventory"] = build_inventory(root, facts["is_git"])

    json.dump(result, sys.stdout)
    sys.stdout.write("\n")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
