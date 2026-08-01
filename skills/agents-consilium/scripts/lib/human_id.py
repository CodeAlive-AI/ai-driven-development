#!/usr/bin/env python3
"""Human-readable run identifiers.

Agents (and humans) handle `run_amber-otter-4f21` far better than
`run_9f3c1d0a5b7e4c2f8a6d3b1e0c7f5a29`: word pairs survive being read aloud,
retyped from a transcript, and referenced three messages later without a
copy-paste. The short hex tail keeps ids unique when the same word pair is
drawn twice.

Used by:
  - steer/registry.py   → default steerable delegate run ids
  - artifacts.sh        → per-run artifact directory names

CLI:
  python3 human_id.py [prefix]   # prints one id and exits

Word lists are deliberately neutral and unambiguous when spoken: no homophones,
no words that read as status ("failed", "stale"), nothing longer than 8 chars.
"""
from __future__ import annotations

import secrets
import sys

ADJECTIVES = (
    "amber", "arctic", "azure", "brave", "brisk", "bronze", "calm", "citrus",
    "clear", "coral", "cosmic", "crisp", "dawn", "deep", "dusty", "eager",
    "early", "fair", "fleet", "fresh", "gentle", "glad", "golden", "grand",
    "green", "hidden", "ivory", "jade", "keen", "lively", "lucid", "lunar",
    "mellow", "merry", "misty", "noble", "nordic", "olive", "opal", "plain",
    "polar", "proud", "quiet", "rapid", "royal", "ruby", "rustic", "sage",
    "scarlet", "silent", "silver", "slate", "smooth", "solar", "spry", "steady",
    "stony", "sunny", "swift", "teal", "tidy", "vivid", "warm", "wild",
)

NOUNS = (
    "acorn", "anchor", "arrow", "aspen", "basalt", "beacon", "birch", "bison",
    "bridge", "canyon", "cedar", "cobalt", "comet", "coral", "crane", "delta",
    "ember", "falcon", "fern", "fjord", "flint", "forge", "garnet", "glacier",
    "harbor", "hazel", "heron", "ibis", "indigo", "island", "juniper", "kestrel",
    "lantern", "ledger", "lichen", "lynx", "maple", "marble", "meadow", "mesa",
    "nebula", "oak", "onyx", "orchid", "otter", "pebble", "pine", "prairie",
    "quartz", "quill", "raven", "reef", "ridge", "river", "sable", "sequoia",
    "shale", "sparrow", "spruce", "summit", "thicket", "tundra", "willow", "zephyr",
)


def human_id(prefix: str = "", words: int = 2, suffix_bytes: int = 2) -> str:
    """Return `<prefix><word>-<word>-<hex>`.

    `words` >= 2 alternates adjective / noun. `suffix_bytes` = 0 drops the hex
    tail entirely — only safe where the caller detects and retries collisions.
    """
    if words < 1:
        raise ValueError("words must be >= 1")
    parts = []
    for i in range(words):
        pool = ADJECTIVES if i % 2 == 0 else NOUNS
        parts.append(secrets.choice(pool))
    if suffix_bytes > 0:
        parts.append(secrets.token_hex(suffix_bytes))
    return prefix + "-".join(parts)


if __name__ == "__main__":
    sys.stdout.write(human_id(sys.argv[1] if len(sys.argv) > 1 else "") + "\n")
