"""Typed file candidates and an exact-file adapter to audited Mole modules.

No shell command is accepted from an agent or browser. A file is moved onto the
same filesystem into a private holding directory, checked again, and only then
passed to Mole. A failed/mismatched move is retained for manual recovery, never
recursively deleted. Source directories and their open descriptors are retained.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import tempfile
import time
import uuid

ASSETS = Path(__file__).resolve().parent
GIB = 1024 ** 3
PROFILE = {"revision": 1, "age_days": 7, "max_bytes": 5 * GIB,
           "max_seconds": 120,
           "roots": ["Library/Caches/Homebrew/downloads", ".npm/_cacache/content-v2"]}
PROFILE_HASH = hashlib.sha256(json.dumps(PROFILE, sort_keys=True).encode()).hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def no_links(path):
    path = Path(path)
    if not path.is_absolute() or ".." in path.parts or any(ord(c) < 32 for c in str(path)):
        raise ValueError("invalid absolute path")
    for parent in [*reversed(path.parents), path]:
        if parent.is_symlink():
            raise ValueError(f"symlink refused: {parent}")
    return path


def private_dir(path):
    path = no_links(path)
    path.mkdir(mode=0o700, parents=True, exist_ok=True)
    info = path.stat()
    if info.st_uid != os.getuid() or info.st_mode & 0o077:
        raise ValueError(f"directory must be owned by you and mode 700: {path}")
    return path


def read_json(path):
    path = no_links(path)
    info = path.stat()
    if (not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid()
            or info.st_mode & 0o077 or info.st_nlink != 1):
        raise ValueError(f"unsafe state file: {path}")
    if info.st_size > 8 * 1024 * 1024:
        raise ValueError("state file too large")
    return json.loads(path.read_text())


def write_json(path, value):
    path = no_links(path)
    private_dir(path.parent)
    fd, temp = tempfile.mkstemp(dir=path.parent, prefix=".write-")
    try:
        with os.fdopen(fd, "w") as output:
            json.dump(value, output, ensure_ascii=False, indent=2)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temp, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def measure(volume="/System/Volumes/Data"):
    result = subprocess.run(["/bin/df", "-Pk", volume], check=True,
                            capture_output=True, text=True, timeout=10)
    row = result.stdout.splitlines()[-1].split()
    total, free = int(row[1]) * 1024, int(row[3]) * 1024
    if total <= 0 or free < 0 or free > total:
        raise ValueError("invalid disk measurement")
    return free, total


def identity(info):
    return [info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns,
            info.st_uid, info.st_nlink, stat.S_IFMT(info.st_mode)]


def candidate(home, path, now=None, allow_downloads=False):
    home, path = no_links(home), no_links(path)
    relative = path.relative_to(home).as_posix()
    root = next((r for r in PROFILE["roots"] if relative.startswith(r + "/")), None)
    if root == PROFILE["roots"][0]:
        if path.parent != home / root or not re.fullmatch(
                r"[0-9a-f]{64}--[^/]+\.(?:tar\.(?:gz|xz|zst|bz2)|zip|dmg|pkg|gz)", path.name):
            raise ValueError("not a Homebrew package download")
    elif root == PROFILE["roots"][1]:
        if not re.fullmatch(r"[0-9a-f]{2}/[0-9a-f]{2}/[0-9a-f]{124}",
                            path.relative_to(home / root).as_posix()):
            raise ValueError("not npm content-addressed package data")
    elif allow_downloads and path.parent == home / "Downloads" and path.suffix.lower() in {
            ".dmg", ".pkg", ".zip", ".gz", ".xz", ".7z", ".tar"}:
        root = "Downloads"
    else:
        raise ValueError("outside the reviewed file profile")
    info = path.lstat()
    if (not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid()
            or info.st_nlink != 1 or info.st_dev != home.stat().st_dev):
        raise ValueError("not an owned, single-link regular file on the home filesystem")
    age = ((time.time() if now is None else now) - info.st_mtime) / 86400
    if age < PROFILE["age_days"]:
        raise ValueError("file is too recent")
    return {"id": digest([str(path), identity(info)])[:24], "path": str(path),
            "identity": identity(info), "size_bytes": info.st_size,
            "age_days": int(age), "root": root, "label": path.name,
            "operation": "mole-remove-file", "protected": False,
            "description": ("Downloaded installer/archive. It may be your only copy; confirm its purpose before deleting."
                            if root == "Downloads" else
                            "Downloaded package cache. The package manager may download this file again."),
            "warning": "Permanent deletion" if root == "Downloads" else "May require downloading again",
            "default_selected": False}


def inventory(home, allow_downloads=False, limit=2000, seconds=30):
    home, rows = Path(home), []
    deadline = time.monotonic() + seconds
    roots = PROFILE["roots"] + (["Downloads"] if allow_downloads else [])
    truncated = False
    for root in roots:
        directory = no_links(home / root)
        if not directory.exists():
            continue
        for parent, dirs, files in os.walk(directory, followlinks=False):
            dirs[:] = [d for d in dirs if not (Path(parent) / d).is_symlink()]
            if root != PROFILE["roots"][1]:
                dirs[:] = []
            for name in files:
                if time.monotonic() > deadline or len(rows) >= limit:
                    truncated = True
                    return rows, truncated
                try:
                    rows.append(candidate(home, Path(parent) / name,
                                          allow_downloads=allow_downloads))
                except (ValueError, OSError):
                    continue
    return rows, truncated


def package_tools_idle():
    # No arguments/environment are collected. Ruby is included because brew is
    # a Ruby process; node covers npm. Unknown/failed sampling fails closed.
    result = subprocess.run(["/bin/ps", "-axo", "comm="], check=True,
                            capture_output=True, text=True, timeout=10)
    return not any(Path(line.strip()).name.lower() in {
        "brew", "ruby", "npm", "node", "pnpm", "yarn", "curl", "wget"}
        for line in result.stdout.splitlines())


class Mole:
    """Compatibility-pinned adapter; never invokes broad `mo clean`."""
    def __init__(self, core):
        self.core = no_links(Path(core).absolute())
        expected = json.loads((ASSETS / "mole-core-1.39.0.json").read_text())
        for name, checksum in expected.items():
            path = no_links(self.core / name)
            if hashlib.sha256(path.read_bytes()).hexdigest() != checksum:
                raise ValueError("Mole modules changed; this version needs a compatibility review")

    def run(self, original, target, dry_run=True):
        # Recheck modules immediately before every use. The adapter's logging
        # facade replaces Mole's log destination, not any protection function.
        self.__init__(self.core)
        no_links(Path.home() / ".config/mole/whitelist")
        env = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "HOME": str(Path.home()),
               "LC_ALL": "C", "MOLE_DRY_RUN": "1" if dry_run else "0"}
        result = subprocess.run(["/bin/bash", str(ASSETS / "mole-exact-file.sh"),
                                 str(self.core), str(original), str(target)],
                                env=env, stdin=subprocess.DEVNULL,
                                capture_output=True, text=True, timeout=15)
        if result.returncode:
            raise RuntimeError("Mole refused exact-file operation: " + result.stderr[-400:])
        return result.stdout[-2000:]


def remove_files(home, items, incident, backend, authorized, emergency=False,
                 disk_measure=measure, idle=package_tools_idle):
    """Stop on any mismatch/error; retain a moved file instead of guessing recovery."""
    incident = private_dir(incident)
    holding = private_dir(incident / "holding")
    if holding.stat().st_dev != Path(home).stat().st_dev:
        raise ValueError("holding directory is on another filesystem")
    if any(holding.iterdir()):
        raise ValueError("previous held file requires manual recovery")
    started, consumed, removed = time.monotonic(), 0, []
    if emergency:
        selected, budget = [], 0
        for item in items:
            if budget + item["size_bytes"] <= PROFILE["max_bytes"]:
                selected.append(item)
                budget += item["size_bytes"]
        items = selected
    # Preview every exact candidate before the first mutation. The time bound
    # includes this phase, not just deletion.
    for item in items:
        if time.monotonic() - started >= PROFILE["max_seconds"] or not authorized():
            raise ValueError("preview deadline exceeded or consent revoked")
        fresh = candidate(home, Path(item["path"]), allow_downloads=not emergency)
        if fresh["identity"] != item["identity"] or fresh["id"] != item["id"]:
            raise ValueError("stale selection; rescan required")
        backend.run(item["path"], item["path"], dry_run=True)
    before = disk_measure()
    write_json(incident / "apply-audit.json", {"status": "previewed", "items": items,
               "before": before, "profile": PROFILE_HASH, "removed": []})
    if emergency and before[0] * 100 >= before[1] * 2:
        result = {"status": "recovered", "before": before, "after": before, "removed": []}
        write_json(incident / "apply-audit.json", result)
        return result
    for item in items:
        if not authorized():
            raise ValueError("consent revoked or responses paused")
        if time.monotonic() - started >= PROFILE["max_seconds"]:
            break
        if emergency:
            free, total = disk_measure()
            if free * 100 >= total * 3:
                break
            if consumed + item["size_bytes"] > PROFILE["max_bytes"]:
                continue
        if item["root"] != "Downloads" and not idle():
            raise ValueError("package manager/download process active; refusing cache cleanup")
        path = Path(item["path"])
        fresh = candidate(home, path, allow_downloads=not emergency)
        if fresh["identity"] != item["identity"]:
            raise ValueError("candidate changed since preview")
        # Source directory is pinned by descriptor. The holding area prevents
        # pathname replacement between our identity check and Mole's rm call.
        parent_fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        destination = holding / str(uuid.uuid4())
        try:
            if identity(os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)) != item["identity"]:
                raise ValueError("source changed before move")
            write_json(incident / "move.json", {"source": str(path), "holding": str(destination),
                       "identity": item["identity"], "status": "moving"})
            os.rename(path.name, destination, src_dir_fd=parent_fd)
            if identity(destination.lstat()) != item["identity"]:
                raise ValueError(f"source raced; object retained, not deleted: {destination}")
            if not authorized():
                raise ValueError(f"consent revoked; original retained at {destination}")
            backend.run(path, destination, dry_run=False)
            if destination.exists():
                raise RuntimeError("Mole did not remove the held file")
            removed.append(item["id"])
            consumed += item["size_bytes"]
            write_json(incident / "move.json", {"source": str(path), "status": "removed"})
            write_json(incident / "apply-audit.json", {"status": "partial", "items": items,
                       "before": before, "removed": removed, "profile": PROFILE_HASH})
        finally:
            os.close(parent_fd)
    result = {"status": "completed" if emergency or len(removed) == len(items) else "partial",
              "items": items, "before": before,
              "after": disk_measure(), "removed": removed, "profile": PROFILE_HASH}
    write_json(incident / "apply-audit.json", result)
    return result
