#!/usr/bin/env python3
"""Filesystem operations shared by the skill install, copy, move and delete scripts.

Skill directories are often symlinks to one canonical real directory, and agents
share directories such as ``~/.agents/skills``. These helpers treat a symlink as
an entry of its own (never deleting through it) and never remove an existing
target before its replacement is fully in place.
"""

from __future__ import annotations

import shutil
from collections.abc import Callable
from pathlib import Path


def path_present(path: Path) -> bool:
    """True if anything occupies ``path``, including a broken symlink."""
    return path.is_symlink() or path.exists()


def remove_path(path: Path) -> None:
    """Remove a symlink itself (never its target) or a real directory tree."""
    if path.is_symlink() or path.is_file():
        path.unlink()
    else:
        shutil.rmtree(path)


def same_location(a: Path, b: Path) -> bool:
    """True if both paths resolve to the same real directory."""
    return a.resolve() == b.resolve()


def stage_and_swap(target: Path, build: Callable[[Path], None]) -> None:
    """Build the new entry next to ``target`` and swap it in only once it is complete."""
    target.parent.mkdir(parents=True, exist_ok=True)
    staging = target.with_name(f".{target.name}.incoming")
    if path_present(staging):
        remove_path(staging)
    try:
        build(staging)
    except BaseException:
        if path_present(staging):
            remove_path(staging)
        raise
    if path_present(target):
        remove_path(target)
    staging.rename(target)


def copy_into_place(source: Path, target: Path) -> None:
    """Copy ``source`` to ``target``; an existing target is replaced only after the copy succeeded."""
    stage_and_swap(target, lambda staging: shutil.copytree(source, staging))


def link_into_place(real_dir: Path, target: Path) -> None:
    """Make ``target`` a symlink to ``real_dir``; an existing target is replaced afterwards."""
    stage_and_swap(
        target, lambda staging: staging.symlink_to(real_dir.resolve(), target_is_directory=True)
    )


def move_into_place(source: Path, target: Path) -> None:
    """Move a skill entry: a symlink stays a symlink to the same real directory, a directory is copied."""
    if source.is_symlink():
        link_into_place(source, target)
    else:
        copy_into_place(source, target)
    remove_path(source)
