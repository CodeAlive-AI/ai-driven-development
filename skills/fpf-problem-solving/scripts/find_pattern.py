#!/usr/bin/env python3
"""Resolve FPF Library references to local files.

  python3 scripts/find_pattern.py F.19              a PatternID: file, section map, publication
  python3 scripts/find_pattern.py HCD.12:4.1        a section reference: the line of that section
  python3 scripts/find_pattern.py GOALS             a DocID: the publication's entry file and practical entries
  python3 scripts/find_pattern.py --search okr goal  words (all must match) in titles, keywords and queries

Paths are relative to the skill directory printed on the first line.
Standard library only; reads PATTERN-INDEX.md written by scripts/split_spec.py.
"""

from __future__ import annotations

import difflib
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
INDEX = SKILL_DIR / "PATTERN-INDEX.md"
ROW_RE = re.compile(r"^\| ([^|]+?) \| ([^|]*?) \| ([^|]+?) \| ([^|]+?) \|$")
ID_RE = re.compile(r"\b([A-Za-z][A-Za-z0-9]*(?:\.[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)+(?::[A-Za-z0-9.]+)?)")
SCRIPT = "python3 scripts/find_pattern.py"


def load() -> tuple[dict[str, tuple[str, str, str]], dict[str, tuple[str, str, str]]]:
    if not INDEX.is_file():
        sys.exit(f"find_pattern: {INDEX} is missing. Regenerate it:\n"
                 f"  python3 {SKILL_DIR / 'scripts/split_spec.py'} --source <ailev/FPF checkout>")
    pubs: dict[str, tuple[str, str, str]] = {}
    pats: dict[str, tuple[str, str, str]] = {}
    section = None
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Publications"):
            section = pubs
        elif line.startswith("## Patterns"):
            section = pats
        m = ROW_RE.match(line)
        if section is not None and m and not m.group(1).startswith(("DocID", "ID", "---")):
            section[m.group(1)] = (m.group(2), m.group(3), m.group(4))
    return pubs, pats


def headings(path: Path) -> list[tuple[int, int, str]]:
    out, fence = [], None
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        f = re.match(r"^\s*(`{3,}|~{3,})", line)
        if f:
            fence = None if fence and f.group(1)[0] == fence[0] else (fence or f.group(1))
            continue
        h = re.match(r"^(#{1,4})\s+(.*)$", line)
        if h and fence is None:
            out.append((n, len(h.group(1)), h.group(2).strip()))
    return out


def show_pattern(ident: str, pats, pubs, section: str | None) -> None:
    title, rel, lines = pats[ident]
    print(f"{ident} — {title}")
    print(f"  file: {rel} ({lines} lines)")
    docid = ident.split(".")[0]
    if docid in pubs:
        print(f"  publication: {docid} — {pubs[docid][0]} → {pubs[docid][1]}")
    elif re.fullmatch(r"[A-K]", docid):
        print(f"  publication: FPF Core — {pubs.get('FPF', ('', 'sections/'))[1]}")
    hs = headings(SKILL_DIR / rel)
    if section:
        ref = f"{ident}:{section}"
        hit = [h for h in hs if h[2].startswith(ref + " ") or h[2] == ref]
        print(f"  section {ref}: " + (f"line {hit[0][0]} — {hit[0][2]}" if hit else "heading not found; read the section map below"))
    print("  sections:")
    for n, level, text in hs[1:]:
        if level <= 3:
            print(f"    L{n:<5} {text}")
    print("  read: Problem frame and Solution first; check your result against the Conformance Checklist;\n"
          "        Relations names neighbouring patterns. Stop at the first useful result.")


def show_publication(docid: str, pubs) -> None:
    title, rel, home = pubs[docid]
    print(f"{docid} — {title} ({home})")
    print(f"  open first: {rel}")
    path = SKILL_DIR / rel
    if path.is_file():
        hs = headings(path)
        entries = [h for h in hs if h[1] == 3 and re.match(r"^[A-Z][A-Z0-9-]+\s+[-—–]", h[2])]
        if entries:
            print("  practical entries (situation → where to start):")
            for n, _, text in entries:
                print(f"    L{n:<5} {text}")
        toc = next((h for h in hs if h[2].lower() == "table of contents"), None)
        if toc:
            print(f"  table of contents with keywords: line {toc[0]}")


def resolve(arg: str, pubs, pats) -> bool:
    cands = [arg, arg.upper()] + [k for k in list(pats) + list(pubs) if k.lower() == arg.lower()]
    for c in cands:
        if c in pats:
            show_pattern(c, pats, pubs, None)
            return True
        if c in pubs:
            show_publication(c, pubs)
            return True
    if ":" in arg:
        base, _, sec = arg.partition(":")
        for c in (base, base.upper()):
            if c in pats:
                show_pattern(c, pats, pubs, sec)
                return True
    close = difflib.get_close_matches(arg, list(pats) + list(pubs), n=8, cutoff=0.6)
    prefix = [k for k in pats if k.lower().startswith(arg.lower().rstrip(".") + ".")][:8]
    print(f"{arg}: not in PATTERN-INDEX.md.", file=sys.stderr)
    if prefix or close:
        print("  nearby IDs: " + ", ".join(dict.fromkeys(prefix + close)), file=sys.stderr)
    print(f"  next: {SCRIPT} --search <words from the pattern's subject>", file=sys.stderr)
    return False


def search(words: list[str], pubs, pats) -> bool:
    terms = [w.lower() for w in words]
    hits: dict[str, tuple[int, str]] = {}

    def consider(ident: str, text: str, weight: int) -> None:
        low = text.lower()
        if all(t in low for t in terms) and ident in pats:
            if ident not in hits or hits[ident][0] < weight:
                hits[ident] = (weight, text)

    for ident, (title, _, _) in pats.items():
        consider(ident, f"{ident} {title}", 2)
    tocs = [SKILL_DIR / "sections/02-table-of-contents/_index.md", *sorted((SKILL_DIR / "dpfs").rglob("_index.md"))]
    for toc in tocs:
        if not toc.is_file():
            continue
        for line in toc.read_text(encoding="utf-8").splitlines():
            if line.startswith("|"):
                m = ID_RE.search(line)
                if m:
                    consider(m.group(1), re.sub(r"\]\([^)]*\)", "]", line), 1)
    pub_hits = [(d, p) for d, p in pubs.items() if all(t in f"{d} {p[0]}".lower() for t in terms)]
    for docid, (title, rel, home) in pub_hits:
        print(f"{docid:<22} {title[:70]:<70}  [publication] {rel}")
    if not hits:
        if not pub_hits:
            print(f"No title, keyword or query matched all of: {' '.join(words)}. Try fewer or broader words.", file=sys.stderr)
        return bool(pub_hits)
    ranked = sorted(hits.items(), key=lambda kv: (-kv[1][0], kv[0]))
    for ident, (weight, _) in ranked[:25]:
        title, rel, lines = pats[ident]
        where = "title" if weight == 2 else "keywords"
        print(f"{ident:<22} {title[:70]:<70}  [{where}] {rel}")
    if len(ranked) > 25:
        print(f"... {len(ranked) - 25} more; add a word to narrow the search.")
    return True


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if argv else 1
    pubs, pats = load()
    print(f"skill: {SKILL_DIR}")
    if argv[0] == "--search":
        return 0 if search(argv[1:], pubs, pats) else 1
    ok = True
    for i, arg in enumerate(argv):
        if i:
            print()
        ok = resolve(arg.strip().rstrip(",;"), pubs, pats) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
