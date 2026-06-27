#!/usr/bin/env python3
"""Split FPF-Spec.md into a hierarchical structure by # and ## headings.

Output:
  sections/
    01-title-page/
      _index.md          — H1 heading + list of H2 children with descriptions
      (no H2 files if section has no ## headings — content lives in _index.md)
    04-part-a-kernel-architecture-cluster/
      _index.md          — H1 heading + H2 listing
      01-a-2-1-u-roleassignment.md
      02-a-2-2-u-capability.md
      ...
"""

import re
import shutil
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SPEC_FILE = PROJECT_ROOT / "FPF" / "FPF-Spec.md"
OUTPUT_DIR = PROJECT_ROOT / "sections"


def to_slug(text: str, max_len: int = 70) -> str:
    """Convert heading text to a kebab-case slug."""
    clean = re.sub(r"[*`]", "", text)
    clean = re.sub(r"\(.*?\)", "", clean)
    clean = re.sub(r"[^a-zA-Z0-9\s-]", " ", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean.lower().replace(" ", "-")[:max_len].rstrip("-")


def heading_to_dirname(index: int, heading: str) -> str:
    heading = heading.lstrip("# ").strip()
    return f"{index:02d}-{to_slug(heading)}"


def heading_to_filename(index: int, heading: str) -> str:
    heading = heading.lstrip("# ").strip()
    return f"{index:02d}-{to_slug(heading, 60)}.md"


def first_sentence(lines_block: list[str], max_chars: int = 200) -> str:
    """Extract first non-empty, non-heading text line as a brief description."""
    for line in lines_block:
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("|") or stripped.startswith("---"):
            continue
        # Clean markdown formatting
        desc = re.sub(r"[*`>]", "", stripped).strip()
        if len(desc) > 20:
            if len(desc) > max_chars:
                desc = desc[:max_chars].rsplit(" ", 1)[0] + "..."
            return desc
    return ""


def build_toc(h2_entries: list[tuple[str, str, int, str]]) -> str:
    """Build a markdown TOC for _index.md from H2 entries."""
    toc_lines = ["", "## Contents", ""]
    for filename, title, line_count, desc in h2_entries:
        clean_title = re.sub(r"[*`]", "", title.lstrip("# ").strip())
        summary = f" — {desc}" if desc else ""
        toc_lines.append(f"- [{clean_title}]({filename}) ({line_count} lines){summary}")
    toc_lines.append("")
    return "\n".join(toc_lines)


# Top-level Parts are emitted as H1 headings when they exist in the upstream spec.
# Validate ordering and duplicates without assuming the spec currently contains
# every possible Part A-K heading.
EXPECTED_PART_LETTERS = list("ABCDEFGHIJK")


def validate_part_structure(h1_titles: list[str]) -> None:
    """Fail loudly if an expected Part A-K H1 heading is missing, duplicated, or
    out of order, so a bad spec never silently produces a wrong sections/ tree."""
    positions: dict[str, list[int]] = {}
    for idx, title in enumerate(h1_titles):
        for letter in EXPECTED_PART_LETTERS:
            if re.search(rf"\bPart {letter}\b", title):
                positions.setdefault(letter, []).append(idx)

    problems: list[str] = []
    for letter in EXPECTED_PART_LETTERS:
        hits = positions.get(letter, [])
        if len(hits) > 1:
            problems.append(
                f"  - Part {letter}: found {len(hits)} H1 headings (expected 1)"
            )

    firsts = [positions[l][0] for l in EXPECTED_PART_LETTERS if positions.get(l)]
    if firsts != sorted(firsts):
        problems.append("  - Part A-K headings are out of document order")

    if problems:
        print(
            "ERROR: FPF-Spec.md Part A-K heading structure is invalid:\n"
            + "\n".join(problems)
            + "\n\nFix duplicate or out-of-order Part headings before splitting.",
            file=sys.stderr,
        )
        sys.exit(1)


def split_spec():
    if not SPEC_FILE.exists():
        print(f"Error: {SPEC_FILE} not found. Clone upstream ailev/FPF into FPF/ first.", file=sys.stderr)
        sys.exit(1)

    lines = SPEC_FILE.read_text(encoding="utf-8").splitlines(keepends=True)

    # Collect all # and ## heading positions
    headings = []
    for i, line in enumerate(lines):
        m = re.match(r"^(#{1,2})\s", line)
        if m:
            headings.append((i, len(m.group(1)), line.rstrip("\n")))

    # Group into H1 sections, each with its H2 children
    h1_sections = []
    current_h1 = None
    current_h2s = []

    for idx, (line_num, level, title) in enumerate(headings):
        next_line = headings[idx + 1][0] if idx + 1 < len(headings) else len(lines)
        block = lines[line_num:next_line]

        if level == 1:
            if current_h1 is not None:
                h1_sections.append((current_h1, current_h2s))
            current_h1 = (line_num, title, block)
            current_h2s = []
        else:
            current_h2s.append((line_num, title, block))

    if current_h1 is not None:
        h1_sections.append((current_h1, current_h2s))

    # Validate Part A-K structure before destroying the existing output tree,
    # so an upstream heading regression aborts the run instead of silently
    # producing a wrong tree.
    validate_part_structure([h1[1] for h1, _ in h1_sections])

    # Clean output dir
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    total_dirs = 0
    total_files = 0

    for h1_idx, (h1, h2s) in enumerate(h1_sections, 1):
        h1_line, h1_title, h1_block = h1
        dirname = heading_to_dirname(h1_idx, h1_title)
        dir_path = OUTPUT_DIR / dirname
        dir_path.mkdir(parents=True, exist_ok=True)
        total_dirs += 1

        if not h2s:
            # No H2 children — put all content in _index.md
            content = "".join(h1_block)
            (dir_path / "_index.md").write_text(content, encoding="utf-8")
            total_files += 1
            print(f"  {dirname}/ ({len(h1_block)} lines, no sub-sections)")
        else:
            # Has H2 children — write each H2 as a separate file
            # The H1 "preamble" is lines between H1 heading and first H2
            first_h2_line = h2s[0][0]
            preamble = lines[h1_line:first_h2_line]

            h2_entries = []
            for h2_idx, (h2_line, h2_title, h2_block) in enumerate(h2s, 1):
                filename = heading_to_filename(h2_idx, h2_title)
                (dir_path / filename).write_text("".join(h2_block), encoding="utf-8")
                total_files += 1
                desc = first_sentence(h2_block[1:])
                h2_entries.append((filename, h2_title, len(h2_block), desc))

            # Write _index.md with preamble + TOC
            index_content = "".join(preamble) + build_toc(h2_entries)
            (dir_path / "_index.md").write_text(index_content, encoding="utf-8")
            total_files += 1

            print(f"  {dirname}/ ({len(h2s)} sub-sections)")

    print(f"\nWrote {total_dirs} directories, {total_files} files to {OUTPUT_DIR}/")


if __name__ == "__main__":
    split_spec()
