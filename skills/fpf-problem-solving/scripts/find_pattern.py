#!/usr/bin/env python3
"""Resolve FPF Library references to local files and find where to start.

  python3 scripts/find_pattern.py F.19               a PatternID: when to use it, its family, its section map
  python3 scripts/find_pattern.py C.38 C.40 SYSE.24  several IDs: a short card each, to choose the one that fits
  python3 scripts/find_pattern.py HCD.12:4.1         a section reference: the line of that section
  python3 scripts/find_pattern.py GOALS              a DocID: its entries (situation -> start with) and patterns
  python3 scripts/find_pattern.py FPF                the Core: practical entries and parts
  python3 scripts/find_pattern.py --search shared specialists okr
                                                     English words: ranked entries, titles, keywords and
                                                     "use this when" text; partial matches are labelled

Paths are relative to the skill directory printed on the first line.
Standard library only; reads PATTERN-INDEX.md written by scripts/split_spec.py.
"""

from __future__ import annotations

import difflib
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
INDEX = SKILL_DIR / "PATTERN-INDEX.md"
CORE_ENTRIES = "sections/03-first-principles-framework-readme/02-practical-entries.md"
ROW_RE = re.compile(r"^\| ([^|]+?) \| ([^|]*?) \| ([^|]+?) \| ([^|]+?) \|$")
ID_PAT = r"[A-Za-z][A-Za-z0-9]*(?:\.[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)+(?::[A-Za-z0-9.]+)?"
ID_RE = re.compile(rf"\b({ID_PAT})")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]*)\)")
TOKEN_RE = re.compile(rf"\[([^\]]*)\]\(([^)\s]*)\)|\b({ID_PAT})")
USE_RE = re.compile(r"use this (?:pattern )?when", re.I)
NOT_RE = re.compile(r"not this pattern when|cheap non-use", re.I)
SCRIPT = "python3 scripts/find_pattern.py"
STOP = set("a an and are as at be by can could do does for from how i in into is it its my no not of on or our "
           "should so that the their them they this to us we what when where which who why will with without "
           "would you your".split())


def plain(text: str) -> str:
    text = LINK_RE.sub(lambda m: m.group(1), text)
    text = re.sub(r"[*`]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def short(text: str, n: int) -> str:
    return text if len(text) <= n else text[: n].rsplit(" ", 1)[0] + " …"


def file_lines(rel: str) -> list[str]:
    path = SKILL_DIR / rel
    return path.read_text(encoding="utf-8").splitlines() if path.is_file() else []


def headings(rel: str) -> list[tuple[int, int, str]]:
    out, fence = [], None
    for n, line in enumerate(file_lines(rel), 1):
        f = re.match(r"^\s*(`{3,}|~{3,})", line)
        if f:
            fence = None if fence and f.group(1)[0] == fence[0] else (fence or f.group(1))
            continue
        h = re.match(r"^(#{1,4})\s+(.*)$", line)
        if h and fence is None:
            out.append((n, len(h.group(1)), h.group(2).strip()))
    return out


@dataclass
class Entry:
    path: str
    line: int
    name: str
    text: str
    starts: list[str] = field(default_factory=list)


class Library:
    def __init__(self) -> None:
        if not INDEX.is_file():
            sys.exit(f"find_pattern: {INDEX} is missing. Regenerate it:\n"
                     f"  python3 {SKILL_DIR / 'scripts/split_spec.py'} --source <ailev/FPF checkout>")
        self.pubs: dict[str, tuple[str, str, str]] = {}
        self.pats: dict[str, tuple[str, str, str]] = {}
        section = None
        for line in INDEX.read_text(encoding="utf-8").splitlines():
            if line.startswith("## Publications"):
                section = self.pubs
            elif line.startswith("## Patterns"):
                section = self.pats
            m = ROW_RE.match(line)
            if section is not None and m and not m.group(1).startswith(("DocID", "ID", "---")):
                section[m.group(1)] = (m.group(2), m.group(3), m.group(4))
        self.by_path: dict[str, str] = {}
        for ident, (_, rel, _) in self.pats.items():
            self.by_path.setdefault(rel, ident)
        for docid, (_, rel, _) in self.pubs.items():
            self.by_path.setdefault(rel, docid)

    # ------------------------------------------------------------------ IDs and entries

    def known(self, token: str) -> bool:
        return token in self.pats or token in self.pubs or token.partition(":")[0] in self.pats

    def ids_in(self, text: str, base: Path) -> list[str]:
        """IDs in order of appearance, from ID text and from links to local pattern or framework files."""
        found: list[str] = []
        for m in TOKEN_RE.finditer(text):
            if m.group(3):
                token = m.group(3).rstrip(".")
                if self.known(token):
                    found.append(token)
                continue
            inner = [t.rstrip(".") for t in ID_RE.findall(m.group(1)) if self.known(t.rstrip("."))]
            if inner:
                found.extend(inner)
                continue
            target = m.group(2).split("#")[0]
            if target and not re.match(r"^[a-z]+:", target):
                try:
                    rel = (base / target).resolve().relative_to(SKILL_DIR).as_posix()
                except ValueError:
                    continue
                if rel in self.by_path:
                    found.append(self.by_path[rel])
        return list(dict.fromkeys(found))

    def starts(self, text: str, base: Path) -> list[str]:
        m = re.search(r"start with", text, re.I)
        if m:
            segment = text[m.end():].split("\n\n", 1)[0].split("\n- ", 1)[0]
            ids = self.ids_in(segment, base)
            if ids:
                return ids
        return self.ids_in(text, base)[:6]

    def entries_in(self, rel: str) -> list[Entry]:
        """Practical entries, cards and question tables of a readme: situation -> where to start."""
        lines = file_lines(rel)
        base = (SKILL_DIR / rel).parent
        start = next((i for i, l in enumerate(lines)
                      if re.match(r"^# .*readme", l, re.I) or re.match(r"^## (choose an entry|practical entries)", l, re.I)),
                     None)
        if start is None:
            return []
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## Files of this publication")),
                   len(lines))
        entries: list[Entry] = []
        block: list = []  # [line, level, name, buffer]
        fence = False

        def flush() -> None:
            if block and block[1] >= 3:
                text = "\n".join(block[3])
                if re.search(r"start with", text, re.I):
                    entries.append(Entry(rel, block[0], plain(block[2]), plain(text), self.starts(text, base)))

        for i in range(start, end):
            line = lines[i]
            if re.match(r"^\s*(```|~~~)", line):
                fence = not fence
                continue
            if fence:
                continue
            h = re.match(r"^(#{2,4})\s+(.*)$", line)
            if h:
                flush()
                block = [i + 1, len(h.group(1)), h.group(2), []]
                continue
            if line.startswith("|"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                nxt = lines[i + 1] if i + 1 < len(lines) else ""
                is_sep = all(re.fullmatch(r":?-{3,}:?", c) for c in cells)
                is_head = bool(re.match(r"^\|\s*:?-{3,}", nxt))
                if len(cells) >= 2 and not is_sep and not is_head:
                    ids = self.ids_in(cells[-1], base)
                    if ids:
                        entries.append(Entry(rel, i + 1, plain(cells[0]), plain(" ".join(cells)), ids))
                continue
            bold = re.match(r"^\*\*([^*]+)\*\*", line)
            if bold and re.search(r"start with", line, re.I):
                entries.append(Entry(rel, i + 1, plain(bold.group(1)), plain(line), self.starts(line, base)))
                continue
            if block:
                block[3].append(line)
        flush()
        return entries

    def entry_files(self) -> list[str]:
        files = [CORE_ENTRIES] if (SKILL_DIR / CORE_ENTRIES).is_file() else []
        files += sorted(p.relative_to(SKILL_DIR).as_posix() for p in (SKILL_DIR / "dpfs").rglob("_index.md"))
        return files

    # ------------------------------------------------------------------ pattern cards

    def fit_lines(self, rel: str) -> tuple[str, str]:
        """The 'use this when' and 'not this pattern when' text from the pattern's opening."""
        lines = file_lines(rel)
        stop = next((i for i, l in enumerate(lines) if re.match(r"^#{2,4} \S+:2\b", l)), min(len(lines), 120))
        head = lines[:stop]

        def para_after(i: int) -> str:
            out = []
            for l in head[i + 1:]:
                if l.startswith("#"):
                    break
                if not l.strip():
                    if out:
                        break
                    continue
                out.append(l.strip().lstrip("-> ").strip())
                if sum(map(len, out)) > 450:
                    break
            return " ".join(out)

        use = ""
        for i, l in enumerate(head):
            if USE_RE.search(l):
                use = para_after(i) if l.startswith("#") else l
                use = plain(use)
                while USE_RE.match(use.lstrip("*_ ")):
                    use = re.sub(r"^\W*use this (?:pattern )?when\W*", "", use, flags=re.I)
                break
        if not use:
            frame = next((i for i, l in enumerate(head) if re.match(r"^#{2,4} \S+:1\b", l)), None)
            if frame is not None:
                use = plain(para_after(frame))
        notwhen = ""
        for i, l in enumerate(head):
            if NOT_RE.search(l) and not l.startswith("#"):
                text = re.sub(r"^\W*(not this pattern when|cheap non-use)\W*", "", plain(l), flags=re.I)
                notwhen = text if len(text) > 60 else (text + " " + plain(para_after(i))).strip()
                break
        return use, notwhen

    def family(self, ident: str) -> list[str]:
        return [k for k in self.pats if k.startswith(ident + ".") and ":" not in k]

    def card(self, ident: str, titles: bool = False) -> None:
        title, rel, n = self.pats[ident]
        print(f"{ident} — {title}")
        print(f"  file: {rel} ({n} lines)")
        use, notwhen = self.fit_lines(rel)
        if use:
            print(f"  use when: {short(use, 420)}")
        if notwhen:
            print(f"  not when: {short(notwhen, 320)}")
        fam = self.family(ident)
        if fam and titles:
            print(f"  family ({len(fam)}):")
            for k in fam[:40]:
                print(f"    {k:<16} {short(self.pats[k][0], 92)}")
            if len(fam) > 40:
                print(f"    … {len(fam) - 40} more")
        elif fam:
            print(f"  family ({len(fam)}): " + ", ".join(fam[:24]) + (", …" if len(fam) > 24 else ""))

    def show_pattern(self, ident: str, section: str | None) -> None:
        self.card(ident, titles=True)
        title, rel, _ = self.pats[ident]
        docid = ident.split(".")[0]
        if docid in self.pubs and docid != ident:
            print(f"  publication: {docid} — {self.pubs[docid][0]} → {self.pubs[docid][1]}")
        elif re.fullmatch(r"[A-K]", docid):
            print(f"  publication: FPF Core — {self.pubs.get('FPF', ('', 'sections/'))[1]}")
        hs = headings(rel)
        if section:
            ref = f"{ident}:{section}"
            hit = [h for h in hs if h[2].startswith(ref + " ") or h[2] == ref]
            print(f"  section {ref}: " + (f"line {hit[0][0]} — {hit[0][2]}" if hit else "heading not found; see the section map"))
        print("  sections:")
        for n, level, text in hs[1:]:
            if level <= 3:
                print(f"    L{n:<5} {text}")
        print("  read: Problem frame and Solution first; check your result against the Conformance Checklist;\n"
              "        Relations names neighbouring patterns. Stop at the first useful result.")

    # ------------------------------------------------------------------ publications

    def show_publication(self, docid: str) -> None:
        title, rel, home = self.pubs[docid]
        print(f"{docid} — {title} ({home})")
        print(f"  open first: {rel}")
        files = [CORE_ENTRIES] if docid == "FPF" else [rel]
        if rel.endswith("suite-reference/_index.md"):
            files.append(str(Path(rel).parent.parent / "_index.md"))
        for f in files:
            entries = self.entries_in(f)
            if entries:
                print("  entries (situation → start with)" + ("" if f == rel else f" in {f}") + ":")
                for e in entries:
                    print(f"    L{e.line:<5} {short(e.name, 92)} → {', '.join(e.starts[:5])}")
        if docid == "FPF":
            print("  Core parts (read a folder's _index.md, or route by SKILL.md Map A):")
            for d in sorted(p for p in (SKILL_DIR / "sections").iterdir() if p.is_dir()):
                count = len([f for f in d.iterdir() if f.suffix == ".md" and f.name != "_index.md"])
                print(f"    sections/{d.name}/  ({count} files)")
        else:
            methods = [k for k in self.pats if k.startswith(docid + ".") and ":" not in k]
            if methods:
                print(f"  patterns ({len(methods)}):")
                for k in methods:
                    print(f"    {k:<16} {short(self.pats[k][0], 92)}")
            groups: dict[str, list[str]] = {}
            for k in self.pats:
                if k.startswith(docid + ".") and ":" in k:
                    g, _, num = k.partition(":")
                    groups.setdefault(g.split(".", 1)[1], []).append(num)
            if groups:
                print("  also: " + ", ".join(f"{g}:{v[0]}" + (f"–{v[-1]}" if len(v) > 1 else "") for g, v in groups.items()))
        toc = next((h for h in headings(rel) if h[2].lower() == "table of contents"), None)
        if toc:
            print(f"  contents with keywords and dependencies: {rel} line {toc[0]}")
        print(f"  next: {SCRIPT} <ID> [<ID> …] — a card for each, to choose where to read")

    # ------------------------------------------------------------------ resolution and search

    def lookup(self, arg: str) -> tuple[str, str, str | None] | None:
        """(kind, id, section) for a PatternID, DocID or section reference, case-insensitively."""
        lower = {k.lower(): k for k in list(self.pats) + list(self.pubs)}
        for c in (arg, lower.get(arg.lower(), "")):
            if c in self.pats:
                return "pattern", c, None
            if c in self.pubs:
                return "publication", c, None
        if ":" in arg:
            base, _, sec = arg.partition(":")
            c = base if base in self.pats else lower.get(base.lower(), "")
            if c in self.pats:
                return "pattern", c, sec
        return None

    def not_found(self, arg: str) -> None:
        close = difflib.get_close_matches(arg, list(self.pats) + list(self.pubs), n=8, cutoff=0.6)
        prefix = [k for k in self.pats if k.lower().startswith(arg.lower().rstrip(".") + ".")][:8]
        print(f"{arg}: not in PATTERN-INDEX.md.", file=sys.stderr)
        if prefix or close:
            print("  nearby IDs: " + ", ".join(dict.fromkeys(prefix + close)), file=sys.stderr)
        print(f"  next: {SCRIPT} --search <English words from the pattern's subject>", file=sys.stderr)

    def search(self, words: list[str]) -> bool:
        if any(re.search(r"[А-Яа-яЁё]", w) for w in words):
            print("note: the Library is written in English; search with English words.")
        terms = [w.lower() for w in re.findall(r"[\w.:-]+", " ".join(words)) if w.lower() not in STOP]
        if not terms:
            print(f"No search words left after dropping common words. Try: {SCRIPT} --search <subject words>", file=sys.stderr)
            return False

        def forms(word: str) -> set[str]:
            out = {word}
            for suf, rep in (("ies", "y"), ("es", ""), ("s", ""), ("ing", ""), ("ed", ""), ("y", "")):
                if word.endswith(suf) and len(word) - len(suf) >= 3:
                    out.add(word[: -len(suf)] + rep)
            return out

        term_forms = [re.compile(r"(?<![\w])(?:" + "|".join(map(re.escape, sorted(forms(t)))) + ")") for t in terms]
        items: list[tuple[str, str, str, str]] = []  # (kind, label, name, body)
        entry_by_label: dict[str, Entry] = {}
        keywords: dict[str, list[str]] = {}
        tocs = ["sections/02-table-of-contents/_index.md", *self.entry_files()]
        for toc in tocs:
            for line in file_lines(toc):
                if line.startswith("|"):
                    m = ID_RE.search(line)
                    if m and m.group(1) in self.pats:
                        keywords.setdefault(m.group(1), []).append(plain(line))
        for ident, (title, rel, _) in self.pats.items():
            use = self.fit_lines(rel)[0] if ":" not in ident else ""
            items.append(("pattern", ident, f"{ident} {title}", " ".join(keywords.get(ident, [])) + " " + use))
        for rel in self.entry_files():
            for e in self.entries_in(rel):
                entry_by_label[f"{e.path}:{e.line}"] = e
                items.append(("entry", f"{e.path}:{e.line}", e.name, e.text + " " + " ".join(e.starts)))
        for docid, (title, rel, _) in self.pubs.items():
            items.append(("publication", docid, f"{docid} {title}", ""))

        phrase = " ".join(terms) if len(terms) > 1 else ""
        scored = []
        for order, (kind, label, name, body) in enumerate(items):
            lname, lbody = name.lower(), body.lower()
            score = matched = 0
            for rx in term_forms:
                if rx.search(lname):
                    score, matched = score + 3, matched + 1
                elif rx.search(lbody):
                    score, matched = score + 1, matched + 1
            if phrase and phrase in lname:
                score += 6
            elif phrase and phrase in lbody:
                score += 4
            if matched:
                rank = {"entry": 0, "pattern": 1, "publication": 2}[kind]
                scored.append((-matched, -score, rank, order, kind, label, name, body))
        if not scored:
            print(f"Nothing matched any of: {' '.join(terms)}.", file=sys.stderr)
            print(f"  next: other English words, or route by SKILL.md Step 0 and Maps A–C; {SCRIPT} FPF lists the Core entries.",
                  file=sys.stderr)
            return False
        scored.sort()
        best = -scored[0][0]
        floor = best if best == 1 else best - 1
        scored = [s for s in scored if -s[0] >= floor]
        if best < len(terms):
            print(f"No item matched all {len(terms)} words; best partial matches ({best} of {len(terms)}) are weak "
                  "evidence — prefer SKILL.md Step 0 and its maps, or try other English words:")
        for neg_matched, _, _, _, kind, label, name, _ in scored[:15]:
            if -neg_matched < best:
                print(f"  ({-neg_matched} of {len(terms)} words)")
                best = -neg_matched
            if kind == "entry":
                entry = entry_by_label[label]
                print(f"[entry]   {short(name, 80)} → {', '.join(entry.starts[:5])}   ({label})")
            elif kind == "pattern":
                print(f"[pattern] {label:<16} {short(self.pats[label][0], 84)}")
            else:
                print(f"[framework] {label:<14} {short(self.pubs[label][0], 70)} → {self.pubs[label][1]}")
        if len(scored) > 15:
            print(f"... {len(scored) - 15} more; add a word to narrow the search.")
        print(f"next: {SCRIPT} <ID> [<ID> …] — a card for each, to choose where to read")
        return True


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if argv else 1
    lib = Library()
    print(f"skill: {SKILL_DIR}")
    if argv[0] == "--search":
        return 0 if lib.search(argv[1:]) else 1
    args = [a.strip().rstrip(",;") for a in argv if a.strip().rstrip(",;")]
    found = [(a, lib.lookup(a)) for a in args]
    ok = all(hit for _, hit in found)
    if len(found) == 1:
        arg, hit = found[0]
        if not hit:
            lib.not_found(arg)
        elif hit[0] == "pattern":
            lib.show_pattern(hit[1], hit[2])
        else:
            lib.show_publication(hit[1])
        return 0 if ok else 1
    for i, (arg, hit) in enumerate(found):
        if i:
            print()
        if not hit:
            lib.not_found(arg)
        elif hit[0] == "publication":
            title, rel, home = lib.pubs[hit[1]]
            print(f"{hit[1]} — {title} ({home})\n  open first: {rel}  (run it alone for its entries and patterns)")
        else:
            lib.card(hit[1])
            if hit[2]:
                ref = f"{hit[1]}:{hit[2]}"
                line = next((h[0] for h in headings(lib.pats[hit[1]][1]) if h[2].startswith(ref + " ") or h[2] == ref), None)
                print(f"  section {ref}: " + (f"line {line}" if line else "heading not found"))
    print(f"\nnext: {SCRIPT} <one ID> — its section map with line numbers")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
