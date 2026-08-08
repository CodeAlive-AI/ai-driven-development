#!/usr/bin/env python3
"""Explicit mode → capability policy matrix for Consilium.

Source of truth for filesystem / shell / web / memory / subagents / steer /
interrupt decisions. Backend-specific safety flags still live with each
backend argv builder, but they must consult this matrix rather than a coarse
readonly/yolo boolean alone.

Fail-closed: unknown modes and unknown capability keys raise.
A new mode cannot inherit YOLO behavior unless it is declared with
access_class=yolo (or explicit write/shell grants).
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Dict, FrozenSet, Mapping, Optional


# Capability keys the matrix may declare. Unknown keys are rejected.
KNOWN_CAPABILITIES = frozenset(
    {
        "filesystem",  # none | read | write
        "shell",  # bool
        "web",  # bool
        "memory",  # bool
        "subagents",  # bool
        "steer",  # bool
        "interrupt",  # bool
        "access_class",  # readonly | yolo  (coarse class for argv builders)
    }
)

ACCESS_CLASSES = frozenset({"readonly", "yolo"})
FILESYSTEM_VALUES = frozenset({"none", "read", "write"})


@dataclass(frozen=True)
class ModeCapabilities:
    mode: str
    filesystem: str  # none | read | write
    shell: bool
    web: bool
    memory: bool
    subagents: bool
    steer: bool
    interrupt: bool
    access_class: str  # readonly | yolo

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @property
    def is_readonly(self) -> bool:
        return self.access_class == "readonly"

    @property
    def is_yolo(self) -> bool:
        return self.access_class == "yolo"

    def allows_writes(self) -> bool:
        return self.filesystem == "write"

    def validate(self) -> None:
        if self.filesystem not in FILESYSTEM_VALUES:
            raise ValueError(
                f"mode {self.mode!r}: invalid filesystem={self.filesystem!r}"
            )
        if self.access_class not in ACCESS_CLASSES:
            raise ValueError(
                f"mode {self.mode!r}: invalid access_class={self.access_class!r}"
            )
        # Safety invariant: yolo requires write; readonly forbids filesystem
        # write capability. Review may still use a shell for git/rg/tests;
        # backend sandboxing and the trusted prompt define its write posture.
        if self.access_class == "readonly":
            if self.filesystem == "write":
                raise ValueError(
                    f"mode {self.mode!r}: readonly cannot grant filesystem=write"
                )
        if self.access_class == "yolo" and self.filesystem != "write":
            raise ValueError(
                f"mode {self.mode!r}: yolo requires filesystem=write"
            )


# Public mode ids accepted by backend_run / workflows.
# Sub-modes (review-ask, review-code-basic, …) map to the same matrix row as
# their public mode family unless overridden.
_MODE_MATRIX: Dict[str, ModeCapabilities] = {
    "review": ModeCapabilities(
        mode="review",
        filesystem="read",
        shell=True,
        web=True,
        memory=False,
        subagents=False,
        steer=False,
        interrupt=False,
        access_class="readonly",
    ),
    "explore": ModeCapabilities(
        mode="explore",
        filesystem="read",
        shell=False,
        web=True,  # docs/RFCs; prompt forbids acting on in-repo URLs
        memory=False,
        subagents=False,
        steer=False,
        interrupt=False,
        access_class="readonly",
    ),
    "delegate": ModeCapabilities(
        mode="delegate",
        filesystem="write",
        shell=True,
        web=True,
        memory=True,
        subagents=True,
        steer=False,
        interrupt=False,
        access_class="yolo",
    ),
    "delegate-steerable": ModeCapabilities(
        mode="delegate-steerable",
        filesystem="write",
        shell=True,
        web=True,
        memory=True,
        subagents=True,
        steer=True,
        interrupt=True,  # mode exists; backend may still reject interrupt
        access_class="yolo",
    ),
}

# Aliases → canonical matrix keys.
_MODE_ALIASES: Dict[str, str] = {
    "review-ask": "review",
    "review-code": "review",
    "review-code-basic": "review",
    "review-code-specialists": "review",
    "review-code-super": "review",
    "review-code-ultra": "review",
    "ask": "review",
    "code": "review",
    "super": "review",
    "ultra": "review",
    "basic": "review",
    "specialists": "review",
    "steerable": "delegate-steerable",
    "delegate_steerable": "delegate-steerable",
}


class UnknownModeError(KeyError):
    pass


class UnknownCapabilityError(KeyError):
    pass


def canonical_mode(mode: str) -> str:
    if not mode:
        raise UnknownModeError("empty mode")
    if mode in _MODE_MATRIX:
        return mode
    if mode in _MODE_ALIASES:
        return _MODE_ALIASES[mode]
    # review-code-* family
    if mode.startswith("review-"):
        return "review"
    raise UnknownModeError(f"unknown mode: {mode!r}")


def get_mode_capabilities(mode: str) -> ModeCapabilities:
    key = canonical_mode(mode)
    caps = _MODE_MATRIX[key]
    caps.validate()
    return caps


def access_policy_for(mode: str) -> str:
    """Coarse readonly|yolo string for argv builders (compat with shell)."""
    return get_mode_capabilities(mode).access_class


def capability(mode: str, name: str) -> Any:
    if name not in KNOWN_CAPABILITIES:
        raise UnknownCapabilityError(f"unknown capability: {name!r}")
    caps = get_mode_capabilities(mode)
    return getattr(caps, name)


def assert_no_yolo_leak(mode: str) -> None:
    """Fail closed: a readonly mode must never look like YOLO."""
    caps = get_mode_capabilities(mode)
    if caps.access_class == "readonly":
        if caps.allows_writes():
            raise AssertionError(
                f"readonly mode {mode!r} leaked write grants: {caps.to_dict()}"
            )
        if caps.steer or caps.interrupt:
            raise AssertionError(
                f"readonly mode {mode!r} must not enable steer/interrupt"
            )


def list_modes() -> FrozenSet[str]:
    return frozenset(_MODE_MATRIX.keys())


def matrix_as_dict() -> Dict[str, Dict[str, Any]]:
    return {k: v.to_dict() for k, v in _MODE_MATRIX.items()}


def validate_matrix() -> None:
    for caps in _MODE_MATRIX.values():
        caps.validate()
        assert_no_yolo_leak(caps.mode)


# Ensure matrix is consistent at import time.
validate_matrix()


def _main() -> int:
    import argparse
    import json
    import sys

    ap = argparse.ArgumentParser(description="Consilium mode capability policy")
    ap.add_argument("mode", nargs="?", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--access-class", action="store_true",
                    help="Print only readonly|yolo for shell consumers")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--check", action="store_true", help="Validate matrix and exit")
    args = ap.parse_args()

    if args.check:
        validate_matrix()
        # Explicit regression: inventing a readonly mode must not get yolo.
        for m in ("review", "explore"):
            assert_no_yolo_leak(m)
            assert access_policy_for(m) == "readonly"
        assert access_policy_for("delegate") == "yolo"
        print("ok")
        return 0
    if args.list:
        if args.json:
            print(json.dumps(matrix_as_dict(), indent=2))
        else:
            for m in sorted(list_modes()):
                print(m)
        return 0
    if not args.mode:
        print("Error: mode required", file=sys.stderr)
        return 2
    try:
        caps = get_mode_capabilities(args.mode)
    except UnknownModeError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 4
    if args.access_class:
        print(caps.access_class)
        return 0
    if args.json:
        print(json.dumps(caps.to_dict(), indent=2))
    else:
        for k, v in caps.to_dict().items():
            print(f"{k}={v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
