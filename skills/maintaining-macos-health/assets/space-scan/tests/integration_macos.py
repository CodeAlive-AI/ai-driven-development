#!/usr/bin/env python3
"""macOS-only smoke tests; only creates/deletes its own temporary fixture.

Run after `make`: python3 tests/integration_macos.py
This script was supplied for execution on macOS, not executed on Linux.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile


def fixture(root: Path) -> None:
    for name in ("a", "b", "a/nested", "empty"):
        (root / name).mkdir(parents=True, exist_ok=True)
    (root / "a/plain.bin").write_bytes(b"x" * 10003)
    (root / "a/nested/another.bin").write_bytes(b"q" * 65539)
    (root / "b/zero.bin").touch()
    (root / "b/строка\nс пробелом.txt").write_bytes("Привет".encode())
    with (root / "b/sparse.bin").open("wb") as file:
        file.write(b"z")
        file.truncate(64 * 1024 * 1024)
    os.link(root / "a/plain.bin", root / "b/hardlink.bin")
    os.symlink("../a", root / "b/symlink-dir")
    os.symlink("plain.bin", root / "a/symlink-file")
    os.symlink("missing", root / "a/broken-symlink")


def expected(root: Path, once: bool) -> tuple[dict[str, tuple[int, int]], dict[str, tuple[int, int]]]:
    records = []
    dirs = {str(root): [0, 0]}
    for folder, names, files in os.walk(root, followlinks=False):
        dirs[str(Path(folder))] = [0, 0]
        for name in files:
            path = Path(folder) / name
            st = path.lstat()
            if stat.S_ISREG(st.st_mode):
                records.append((str(path), st.st_dev, st.st_ino, st.st_size, st.st_blocks * 512))
    seen = set()
    selected = {}
    for path, dev, inode, logical, allocated in sorted(records):
        if once and (dev, inode) in seen:
            continue
        seen.add((dev, inode))
        selected[path] = (logical, allocated)
        parent = Path(path).parent
        while True:
            dirs[str(parent)][0] += logical
            dirs[str(parent)][1] += allocated
            if parent == root:
                break
            parent = parent.parent
    return selected, {key: tuple(value) for key, value in dirs.items()}


def run(binary: Path, root: Path, workers: int, once: bool, metric: str, backend: str = "bulk") -> None:
    proc = subprocess.run(
        [str(binary), "--backend", backend, "--json", "--top", "100", "--workers", str(workers),
         "--metric", metric, "--hardlinks", "once" if once else "paths", str(root)],
        text=True, encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        timeout=120, check=False,
    )
    if proc.returncode:
        raise AssertionError(f"scanner exited {proc.returncode}\n{proc.stderr}\n{proc.stdout}")
    result = json.loads(proc.stdout)
    expected_files, expected_dirs = expected(root, once)
    observed_files = {row["path"]: (row["logical_bytes"], row["allocated_bytes"]) for row in result["files"]}
    observed_dirs = {row["path"]: (row["logical_bytes"], row["allocated_bytes"]) for row in result["folders"]}
    root_totals = expected_dirs.pop(str(root))
    assert observed_files == expected_files, (observed_files, expected_files)
    assert observed_dirs == expected_dirs, (observed_dirs, expected_dirs)
    assert (result["logical_bytes"], result["allocated_bytes"]) == root_totals
    assert result["counted_regular_files"] == len(expected_files)
    assert result["errors"] == 0
    assert result["skipped_nonregular"] == 3
    assert result["reclaimable_bytes"] is None
    assert result["snapshot_consistent"] is False
    sizes = [row[f"{metric}_bytes"] for row in result["files"]]
    assert sizes == sorted(sizes, reverse=True)
    print(f"PASS backend={backend} workers={workers} hardlinks={'once' if once else 'paths'} metric={metric}")


def main() -> int:
    if sys.platform != "darwin":
        print("SKIP: requires macOS and a locally built space_scan.")
        return 0
    binary = Path(__file__).resolve().parents[1] / "space_scan"
    if not binary.is_file():
        raise SystemExit("Build first: make space_scan")
    # A user can point TMPDIR to an APFS test volume; no system volume is modified.
    with tempfile.TemporaryDirectory(prefix="space-scan-test-") as temporary:
        root = Path(temporary).resolve()
        fixture(root)
        for workers in (1, 4):
            for once in (True, False):
                for metric in ("allocated", "logical"):
                    for backend in ("bulk", "stat"):
                        run(binary, root, workers, once, metric, backend)
    print("All macOS fixture tests passed. This is not a full-volume performance benchmark.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
