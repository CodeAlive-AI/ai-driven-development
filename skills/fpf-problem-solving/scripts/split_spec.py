#!/usr/bin/env python3
"""Split the FPF Library into agent-sized local files.

Usage (from anywhere):
  git clone --depth 1 https://github.com/ailev/FPF.git /tmp/fpf-upstream
  python3 skills/fpf-problem-solving/scripts/split_spec.py --source /tmp/fpf-upstream

--source  an official ailev/FPF checkout (default: <skill>/FPF, the legacy layout)
--out     the skill directory to write into (default: this script's skill)

Writes into --out:
  sections/         FPF Core (FPF-Spec.md): one folder per H1, one file per H2
  dpfs/             Domain Principle Frameworks: one folder per framework (by DocID), one file per H2
  library/          Library Readme, USING-FPF.md, LICENSING.md and the Library Architectural Reference
  PATTERN-INDEX.md  every DocID and PatternID mapped to its local file

Links between publications (in-document anchors, relative paths, GitHub blob links and
fpf.tools/<ID> links) are rewritten to the local files, so an agent can follow them offline.

Nothing is replaced until every publication has been split and validated.
Standard library only.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

SKILL_DIR = Path(__file__).resolve().parent.parent
SCRIPT_REL = "scripts/split_spec.py"
GENERATED = ["sections", "dpfs", "library", "PATTERN-INDEX.md"]
UPSTREAM_URL = "https://github.com/ailev/FPF.git"

# Root files of the upstream checkout and where they go. Any other root Markdown file is an
# error, so that a new upstream publication is noticed instead of silently dropped.
ROOT_FILES = {
    "FPF-Spec.md": ("core", "sections"),
    "FPF-LIBRARY-REFERENCE.md": ("framework", "library/reference"),
    "Readme.md": ("verbatim", "library/_index.md"),
    "USING-FPF.md": ("verbatim", "library/USING-FPF.md"),
    "LICENSING.md": ("verbatim", "library/LICENSING.md"),
}
ROOT_IGNORED = {"LICENSE"}  # plain license text; SKILL.md links the upstream licensing scope

FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
# A heading that starts with an identifier: A.1, C.11.DUA, GOALS.7, KCAE.USE,
# GOALS.Reference:2, HCD.12:4.1, FPF.Reference:16
ID_HEADING_RE = re.compile(
    r"^(?P<id>[A-Za-z][A-Za-z0-9]*(?:\.[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)+(?::[A-Za-z0-9.]+)?)"
    r"(?:\s+[-—–]+\s+|\s*$)(?P<title>.*)$"
)
INLINE_LINK_RE = re.compile(r"(\]\()(<[^>\n]*>|[^)\s]+)((?:\s+\"[^\"\n]*\")?\))")
REF_DEF_RE = re.compile(r"^(\s{0,3}\[[^\]\n]+\]:\s*)(<[^>\n]*>|\S+)(.*)$")
FPF_TOOLS_RE = re.compile(r"^https?://fpf\.tools/([^?#]+)(?:\?[^#]*)?(?:#(.*))?$")
# Only links to the default branch are rewritten; links pinned to a commit cite that exact edition.
GITHUB_BLOB_RE = re.compile(r"^https?://github\.com/ailev/FPF/(?:blob|tree)/main/([^?#]*)(?:\?[^#]*)?(?:#(.*))?$")


class SplitError(Exception):
    """A problem that must stop the split before anything is replaced."""


# --------------------------------------------------------------------------- helpers


def to_slug(text: str, max_len: int = 70) -> str:
    """Convert heading text to a kebab-case ASCII slug for file and folder names."""
    clean = re.sub(r"[*`]", "", text)
    clean = re.sub(r"\(.*?\)", "", clean)
    clean = re.sub(r"[^a-zA-Z0-9\s-]", " ", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean.lower().replace(" ", "-")[:max_len].rstrip("-")


def heading_text(line: str) -> str:
    return line.lstrip("#").strip()


def gh_slug_base(text: str) -> str:
    """GitHub-style anchor slug of a heading (what `#anchor` links in upstream point to)."""
    t = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = t.replace("`", "").replace("*", "")
    t = t.lower()
    t = re.sub(r"[^\w\- ]", "", t)
    return t.replace(" ", "-")


class Slugger:
    def __init__(self) -> None:
        self.seen: dict[str, int] = {}

    def slug(self, text: str) -> str:
        base = gh_slug_base(text)
        if base not in self.seen:
            self.seen[base] = 0
            return base
        while True:
            self.seen[base] += 1
            cand = f"{base}-{self.seen[base]}"
            if cand not in self.seen:
                self.seen[cand] = 0
                return cand


def first_sentence(lines_block: list[str], max_chars: int = 200) -> str:
    """Extract the first non-empty, non-heading text line as a brief description."""
    for line in lines_block:
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", "|", "---")):
            continue
        desc = re.sub(r"[*`>]", "", stripped).strip()
        if len(desc) > 20:
            if len(desc) > max_chars:
                desc = desc[:max_chars].rsplit(" ", 1)[0] + "..."
            return desc
    return ""


def heading_id(text: str) -> tuple[str, str] | None:
    m = ID_HEADING_RE.match(text)
    if not m:
        return None
    return m.group("id"), m.group("title").strip()


# --------------------------------------------------------------------------- model


@dataclass
class Heading:
    line: int
    level: int
    text: str


@dataclass
class Doc:
    src: str                    # posix path relative to the source root
    kind: str                   # core | framework | verbatim
    out: str                    # output folder (core/framework) or file (verbatim)
    lines: list[str]
    docid: str | None = None
    title: str = ""
    suite: str | None = None
    headings: list[Heading] = field(default_factory=list)
    fenced: list[bool] = field(default_factory=list)
    index_file: str = ""        # the file an agent opens first for this publication


@dataclass
class OutFile:
    path: str                   # posix path relative to the skill dir
    doc: Doc
    ranges: list[tuple[int, int]]
    generated: str = ""         # appended after the rewritten source text (already local links)
    headings: list[Heading] = field(default_factory=list)
    virtual: list[Heading] = field(default_factory=list)  # H1s listed (not copied) in this file


def scan(doc: Doc) -> None:
    fence: str | None = None
    fenced: list[bool] = []
    for i, raw in enumerate(doc.lines):
        line = raw.rstrip("\n")
        m = FENCE_RE.match(line)
        if m:
            marker = m.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            fenced.append(True)
            continue
        fenced.append(fence is not None)
        if fence is None:
            h = HEADING_RE.match(line)
            if h:
                doc.headings.append(Heading(i, len(h.group(1)), h.group(2)))
    doc.fenced = fenced


# --------------------------------------------------------------------------- discovery


def git_edition(source: Path) -> tuple[str, str]:
    try:
        sha = subprocess.run(["git", "-C", str(source), "rev-parse", "HEAD"], check=True,
                             capture_output=True, text=True).stdout.strip()
        date = subprocess.run(["git", "-C", str(source), "log", "-1", "--format=%cI"], check=True,
                              capture_output=True, text=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        raise SplitError(
            f"{source} is not a git checkout, so the upstream edition cannot be recorded ({exc}).\n"
            f"Next: git clone --depth 1 {UPSTREAM_URL} /tmp/fpf-upstream && "
            f"python3 {SKILL_DIR / SCRIPT_REL} --source /tmp/fpf-upstream"
        ) from exc
    return sha, date


def load_catalogue(source: Path) -> dict[str, tuple[str, str]]:
    """DocID -> (full title, carrier path) from Library.Reference:11.1."""
    ref = (source / "FPF-LIBRARY-REFERENCE.md").read_text(encoding="utf-8").splitlines()
    start = next((i for i, l in enumerate(ref) if re.match(r"^#{2,4} Library\.Reference:11\.1\b", l)), None)
    if start is None:
        raise SplitError(
            "FPF-LIBRARY-REFERENCE.md has no 'Library.Reference:11.1' heading, which holds the DocID "
            "catalogue. Upstream changed its structure: find the new DocID catalogue and update "
            f"load_catalogue() in {SCRIPT_REL}. Nothing was changed."
        )
    cat: dict[str, tuple[str, str]] = {}
    for line in ref[start + 1:]:
        if line.startswith("#"):
            break
        m = re.match(r"^\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|\s*\[[^\]]*\]\(([^)]+)\)\s*\|", line)
        if m:
            cat[m.group(1)] = (m.group(2), unquote(m.group(3)))
    if len(cat) < 10:
        raise SplitError(
            f"Parsed only {len(cat)} DocID rows from Library.Reference:11.1; the table format changed. "
            f"Update load_catalogue() in {SCRIPT_REL}. Nothing was changed."
        )
    return cat


def discover(source: Path) -> list[Doc]:
    problems: list[str] = []
    for name in ROOT_FILES:
        if not (source / name).is_file():
            problems.append(f"missing {name}")
    if problems:
        raise SplitError(
            f"{source} is not a complete ailev/FPF checkout ({', '.join(problems)}). Nothing was changed.\n"
            f"Next: git clone --depth 1 {UPSTREAM_URL} /tmp/fpf-upstream && "
            f"python3 {SKILL_DIR / SCRIPT_REL} --source /tmp/fpf-upstream"
        )
    unknown_root = sorted(
        p.name for p in source.iterdir()
        if p.is_file() and p.suffix.lower() == ".md" and p.name not in ROOT_FILES
    )
    unknown_root += sorted(
        p.name for p in source.iterdir()
        if p.is_dir() and not p.name.startswith(".") and p.name != "DPFs"
    )
    if unknown_root:
        raise SplitError(
            "Upstream has root publications this splitter does not place: "
            + ", ".join(unknown_root)
            + f".\nAdd them to ROOT_FILES (or ROOT_IGNORED) in {SCRIPT_REL}, then rerun. Nothing was changed."
        )

    catalogue = load_catalogue(source)
    carrier_to_docid = {path: docid for docid, (_, path) in catalogue.items()}
    docs: list[Doc] = []

    def read(rel: str) -> list[str]:
        return (source / rel).read_text(encoding="utf-8").splitlines(keepends=True)

    for name, (kind, out) in ROOT_FILES.items():
        doc = Doc(name, kind, out, read(name))
        doc.docid = carrier_to_docid.get(name)
        docs.append(doc)

    dpf_root = source / "DPFs"
    if not dpf_root.is_dir():
        raise SplitError(f"{source} has no DPFs/ folder. Check that --source is an ailev/FPF checkout. Nothing was changed.")
    seen_docids: set[str] = set()
    for path in sorted(dpf_root.rglob("*.md")):
        rel = path.relative_to(source).as_posix()
        parts = PurePosixPath(rel).parts  # ('DPFs', [suite], file)
        suite = parts[1] if len(parts) == 3 else None
        if len(parts) > 3:
            raise SplitError(f"{rel} is nested deeper than DPFs/<Suite>/; update discover() in {SCRIPT_REL}. Nothing was changed.")
        suite_dir = f"dpfs/{to_slug(suite)}" if suite else "dpfs"
        if path.name == "README.md":
            docs.append(Doc(rel, "verbatim", f"{suite_dir}/_index.md", read(rel), suite=suite))
            continue
        docid = carrier_to_docid.get(rel)
        if docid is None:
            raise SplitError(
                f"{rel} has no DocID row in Library.Reference:11.1 (FPF-LIBRARY-REFERENCE.md).\n"
                "Either upstream added a framework before cataloguing it, or the catalogue moved. "
                f"Inspect the catalogue and update load_catalogue()/discover() in {SCRIPT_REL}. Nothing was changed."
            )
        seen_docids.add(docid)
        folder = "suite-reference" if path.name.endswith("-SUITE-REFERENCE.md") else docid.lower()
        doc = Doc(rel, "framework", f"{suite_dir}/{folder}", read(rel), docid=docid, suite=suite)
        declared = re.search(r"^\*\*DocID:\*\*\s*`?([A-Za-z]+)`?", "".join(doc.lines[:40]), re.M)
        if declared and declared.group(1) != docid:
            raise SplitError(
                f"{rel} declares DocID {declared.group(1)} but Library.Reference:11.1 says {docid}. "
                "Report the inconsistency upstream; decide which one to follow in discover(). Nothing was changed."
            )
        docs.append(doc)

    missing = sorted(
        d for d, (_, p) in catalogue.items()
        if p.startswith("DPFs/") and d not in seen_docids
    )
    if missing:
        raise SplitError(
            "Library.Reference:11.1 lists DPFs whose files are absent: " + ", ".join(missing)
            + ". Check the upstream checkout is complete. Nothing was changed."
        )
    for doc in docs:
        if doc.docid:
            doc.title = catalogue[doc.docid][0]
        scan(doc)
    return docs


# --------------------------------------------------------------------------- planning


def validate_part_structure(h1_titles: list[str]) -> None:
    """Fail if Part A-K H1 headings of FPF-Spec.md are duplicated or out of order."""
    letters = list("ABCDEFGHIJK")
    positions: dict[str, list[int]] = {}
    for idx, title in enumerate(h1_titles):
        for letter in letters:
            if re.search(rf"\bPart {letter}\b", title):
                positions.setdefault(letter, []).append(idx)
    problems = [f"  - Part {l}: found {len(v)} H1 headings (expected 1)" for l, v in positions.items() if len(v) > 1]
    firsts = [positions[l][0] for l in letters if positions.get(l)]
    if firsts != sorted(firsts):
        problems.append("  - Part A-K headings are out of document order")
    if problems:
        raise SplitError("FPF-Spec.md Part A-K heading structure is invalid:\n" + "\n".join(problems)
                         + "\nFix duplicate or out-of-order Part headings before splitting. Nothing was changed.")


def h1_groups(doc: Doc) -> list[tuple[Heading | None, list[Heading]]]:
    """[(h1, [h2...])], with a leading (None, h2s) group if H2s precede the first H1."""
    groups: list[tuple[Heading | None, list[Heading]]] = []
    for h in doc.headings:
        if h.level == 1:
            groups.append((h, []))
        elif h.level == 2:
            if not groups:
                groups.append((None, []))
            groups[-1][1].append(h)
    return groups


def block_end(doc: Doc, heading: Heading) -> int:
    """Line index after the block opened by heading (next heading of the same or higher level)."""
    for h in doc.headings:
        if h.line > heading.line and h.level <= heading.level:
            return h.line
    return len(doc.lines)


def plan_core(doc: Doc) -> list[OutFile]:
    groups = h1_groups(doc)
    if groups and groups[0][0] is None:
        raise SplitError("FPF-Spec.md has H2 headings before its first H1; update plan_core(). Nothing was changed.")
    validate_part_structure([heading_text(h1.text) for h1, _ in groups])
    outs: list[OutFile] = []
    for i, (h1, h2s) in enumerate(groups, 1):
        dirname = f"{doc.out}/{i:02d}-{to_slug(h1.text)}"
        end = block_end(doc, h1)
        if not h2s:
            outs.append(OutFile(f"{dirname}/_index.md", doc, [(h1.line, end)]))
            continue
        entries = []
        for j, h2 in enumerate(h2s, 1):
            fname = f"{j:02d}-{to_slug(h2.text, 60)}.md"
            h2_end = block_end(doc, h2)
            outs.append(OutFile(f"{dirname}/{fname}", doc, [(h2.line, h2_end)]))
            block = doc.lines[h2.line:h2_end]
            entries.append((fname, h2.text, len(block), first_sentence(block[1:])))
        toc = ["", "## Contents", ""]
        for fname, title, count, desc in entries:
            clean = re.sub(r"[*`]", "", title)
            toc.append(f"- [{clean}]({fname}) ({count} lines)" + (f" — {desc}" if desc else ""))
        outs.append(OutFile(f"{dirname}/_index.md", doc, [(h1.line, h2s[0].line)], "\n".join(toc) + "\n"))
        if i == 3 or "readme" in h1.text.lower():
            doc.index_file = doc.index_file or f"{dirname}/_index.md"
    doc.index_file = doc.index_file or outs[0].path
    return outs


def plan_framework(doc: Doc) -> list[OutFile]:
    """One folder per publication: _index.md = title + contents + readme; one file per H2."""
    groups = h1_groups(doc)
    if not groups:
        raise SplitError(f"{doc.src} has no headings; update plan_framework(). Nothing was changed.")
    h1s = [h1 for h1, _ in groups if h1 is not None]
    front_end_group = 0
    if len(h1s) > 1:
        readme = next((k for k, (h1, _) in enumerate(groups[:4]) if h1 and "readme" in h1.text.lower()), None)
        toc = next((k for k, (h1, _) in enumerate(groups[:3]) if h1 and h1.text.strip().lower() == "table of contents"), None)
        if readme is None or toc is None:
            raise SplitError(
                f"{doc.src} does not follow the framework layout (Title, Table of Contents, Readme, ...): "
                f"found H1s {[heading_text(h.text)[:50] for h in h1s[:4]]}.\n"
                f"Update plan_framework() in {SCRIPT_REL} for this layout. Nothing was changed."
            )
        front_end_group = readme
    # Front matter: everything up to the end of front_end_group (multi-H1) or up to the first H2 (single H1).
    if len(h1s) > 1:
        nxt = groups[front_end_group + 1][0] if front_end_group + 1 < len(groups) else None
        front_end = nxt.line if nxt else len(doc.lines)
        rest = groups[front_end_group + 1:]
    else:
        _, h2s = groups[0]
        front_end = h2s[0].line if h2s else len(doc.lines)
        rest = [(None, h2s)] if h2s else []

    planned: list[tuple[str, int, int, str]] = []  # (group label, start, end, heading text)
    listed_only: list[Heading] = []                # H1s without own text: anchors go to the listing
    for h1, h2s in rest:
        label = heading_text(h1.text) if h1 else ""
        if h1 is not None:
            pre_end = h2s[0].line if h2s else block_end(doc, h1)
            body = [l for l in doc.lines[h1.line + 1:pre_end] if l.strip()]
            if body or not h2s:
                planned.append((label, h1.line, pre_end, h1.text))
            else:
                listed_only.append(h1)
        for h2 in h2s:
            planned.append((label, h2.line, block_end(doc, h2), h2.text))

    width = max(2, len(str(len(planned))))
    outs: list[OutFile] = []
    listing: list[str] = ["", "---", "", "## Files of this publication", "",
                          "Generated by the skill's splitter: one file per section, in reading order.", ""]
    current_label = None
    for n, (label, start, end, text) in enumerate(planned, 1):
        fname = f"{n:0{width}d}-{to_slug(text, 60)}.md"
        outs.append(OutFile(f"{doc.out}/{fname}", doc, [(start, end)]))
        if label != current_label and label:
            listing += ["", f"### {label}", ""]
            current_label = label
        clean = re.sub(r"[*`]", "", heading_text(text))
        listing.append(f"- [{clean}]({fname}) ({end - start} lines)")
    index = OutFile(f"{doc.out}/_index.md", doc, [(0, front_end)], "\n".join(listing) + "\n",
                    virtual=listed_only)
    outs.insert(0, index)
    doc.index_file = index.path
    if not doc.title and h1s:
        doc.title = heading_text(h1s[0].text)
    return outs


def plan_verbatim(doc: Doc) -> list[OutFile]:
    doc.index_file = doc.out
    if not doc.title:
        first = next((h for h in doc.headings if h.level == 1), None)
        doc.title = heading_text(first.text) if first else doc.src
    return [OutFile(doc.out, doc, [(0, len(doc.lines))])]


# --------------------------------------------------------------------------- links


@dataclass
class Target:
    path: str
    slug: str
    top: bool


class LinkMap:
    def __init__(self, docs: list[Doc], outs: list[OutFile], sha: str) -> None:
        self.by_doc_slug: dict[tuple[str, str], Target] = {}
        self.by_id: dict[str, Target] = {}
        self.docs = {d.src: d for d in docs}
        self.docid_index = {d.docid: d.index_file for d in docs if d.docid}
        self.sha = sha
        self.unresolved: list[str] = []
        self.rewritten = 0
        for doc in docs:
            doc_slugger = Slugger()
            owner: dict[int, OutFile] = {}
            for out in (o for o in outs if o.doc is doc):
                for start, end in out.ranges:
                    for h in doc.headings:
                        if start <= h.line < end:
                            owner[h.line] = out
                for h in out.virtual:
                    owner[h.line] = out
            file_sluggers: dict[str, Slugger] = {}
            for h in doc.headings:
                dslug = doc_slugger.slug(h.text)
                out = owner.get(h.line)
                if out is None:
                    continue
                fs = file_sluggers.setdefault(out.path, Slugger())
                if h in out.virtual:
                    # listed as "### <title>" after the "## Files of this publication" heading
                    fs.seen.setdefault(gh_slug_base("Files of this publication"), 0)
                fslug = fs.slug(h.text)
                top = out.ranges[0][0] == h.line and not out.path.endswith("_index.md")
                tgt = Target(out.path, fslug, top)
                self.by_doc_slug.setdefault((doc.src, dslug), tgt)
                if h not in out.virtual:
                    out.headings.append(h)
                hid = heading_id(heading_text(h.text))
                if hid:
                    self.by_id.setdefault(hid[0], tgt)

    def _link(self, tgt: Target, from_path: str) -> str:
        rel = os.path.relpath(tgt.path, start=os.path.dirname(from_path) or ".")
        rel = PurePosixPath(*Path(rel).parts).as_posix()
        return rel if tgt.top or not tgt.slug else f"{rel}#{tgt.slug}"

    def _doc_index(self, src: str, from_path: str) -> str | None:
        doc = self.docs.get(src)
        if doc is None:
            return None
        return self._link(Target(doc.index_file, "", True), from_path)

    def _resolve_path(self, src_path: str, frag: str, from_path: str) -> str | None:
        src_path = src_path.strip("/")
        if src_path in ROOT_IGNORED:
            return f"https://github.com/ailev/FPF/blob/{self.sha}/{src_path}"
        if src_path in ("", "."):
            src_path = "Readme.md"
        elif src_path not in self.docs and f"{src_path}/README.md" in self.docs:
            src_path = f"{src_path}/README.md"
        if src_path not in self.docs:
            return None
        if frag:
            tgt = self.by_doc_slug.get((src_path, unquote(frag).lower()))
            if tgt:
                return self._link(tgt, from_path)
            return None
        return self._doc_index(src_path, from_path)

    def resolve(self, target: str, doc: Doc, from_path: str) -> str | None:
        t = target[1:-1] if target.startswith("<") and target.endswith(">") else target
        if t.startswith("#"):
            return self._resolve_path(doc.src, t[1:], from_path)
        m = FPF_TOOLS_RE.match(t)
        if m:
            ident = unquote(m.group(1)).strip("/")
            frag = unquote(m.group(2) or "")
            for key in (frag, ident):
                if key and key in self.by_id:
                    return self._link(self.by_id[key], from_path)
                if key and key in self.docid_index:
                    return self._link(Target(self.docid_index[key], "", True), from_path)
            return None
        m = GITHUB_BLOB_RE.match(t)
        if m:
            return self._resolve_path(unquote(m.group(1)), m.group(2) or "", from_path)
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", t):
            return None  # other absolute URLs and mailto: stay as they are
        path, _, frag = t.partition("#")
        joined = os.path.normpath(os.path.join(os.path.dirname(doc.src), unquote(path))) if path else doc.src
        joined = PurePosixPath(*Path(joined).parts).as_posix() if joined != "." else ""
        return self._resolve_path(joined, frag, from_path)

    def rewrite(self, out: OutFile) -> str:
        doc = out.doc
        chunks: list[str] = []
        for start, end in out.ranges:
            for i in range(start, end):
                line = doc.lines[i]
                if doc.fenced[i]:
                    chunks.append(line)
                    continue
                chunks.append(self._rewrite_line(line, doc, out.path))
        return "".join(chunks)

    def _rewrite_line(self, line: str, doc: Doc, from_path: str) -> str:
        def sub_inline(m: re.Match) -> str:
            new = self._try(m.group(2), doc, from_path)
            return f"{m.group(1)}{new}{m.group(3)}" if new else m.group(0)

        m = REF_DEF_RE.match(line)
        if m:
            new = self._try(m.group(2), doc, from_path)
            return f"{m.group(1)}{new}{m.group(3)}\n" if new else line
        if "](" not in line:
            return line
        return INLINE_LINK_RE.sub(sub_inline, line)

    def _try(self, target: str, doc: Doc, from_path: str) -> str | None:
        new = self.resolve(target, doc, from_path)
        if new:
            self.rewritten += 1
            return new
        bare = target.strip("<>")
        looks_local = bare.startswith("#") or ".md" in bare or bare.endswith("/")
        if (looks_local and not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", bare)) or GITHUB_BLOB_RE.match(bare):
            self.unresolved.append(f"{doc.src}: {target[:120]}")
        return None


# --------------------------------------------------------------------------- outputs


def pattern_index(docs: list[Doc], outs: list[OutFile], links: LinkMap, sha: str, date: str,
                  line_counts: dict[str, int]) -> str:
    rows: list[str] = []
    seen: dict[str, str] = {}
    duplicates: list[str] = []
    order = sorted(docs, key=lambda d: (d.kind != "core", d.src != "FPF-LIBRARY-REFERENCE.md", d.docid or "~", d.src))
    for doc in order:
        if doc.kind == "verbatim":
            continue
        for out in (o for o in outs if o.doc is doc):
            for h in out.headings:
                if h.level != 2:
                    continue
                hid = heading_id(heading_text(h.text))
                if not hid or hid[0].endswith(":End"):
                    continue
                ident, title = hid
                prefix = ident.split(".")[0]
                if doc.kind == "core" and not (re.fullmatch(r"[A-K]", prefix) or prefix == "FPF"):
                    continue
                if doc.kind == "framework" and prefix != (doc.docid or ""):
                    continue
                if ident in seen:
                    duplicates.append(f"{ident} in {seen[ident]} and {out.path}")
                    continue
                seen[ident] = out.path
                clean = re.sub(r"[*`|]", "", title)
                rows.append(f"| {ident} | {clean} | {out.path} | {line_counts[out.path]} |")
    if duplicates:
        raise SplitError("Duplicate PatternIDs across the Library:\n  " + "\n  ".join(duplicates[:20])
                         + f"\nInspect these headings upstream and update pattern_index() in {SCRIPT_REL}. Nothing was changed.")
    pubs = ["| DocID | Title | Open first | Home |", "| --- | --- | --- | --- |"]
    for doc in sorted((d for d in docs if d.docid), key=lambda d: (d.docid != "FPF", d.docid != "Library", d.docid.lower())):
        home = doc.suite or ("Library" if doc.kind != "framework" or doc.src.startswith("FPF") else "standalone DPF")
        pubs.append(f"| {doc.docid} | {doc.title} | {doc.index_file} | {home} |")
    header = f"""# FPF Library pattern index

Generated by `{SCRIPT_REL}` from [ailev/FPF](https://github.com/ailev/FPF) commit `{sha}` ({date}).
Do not edit by hand; rerun the splitter.

- **Resolve an ID:** `python3 scripts/find_pattern.py GOALS.7` prints the file, its section map and
  the publication; it also takes section references (`HCD.12:4.1`), DocIDs (`GOALS`) and `--search <words>`.
- **Without Python:** `grep -F "| <ID> |" PATTERN-INDEX.md`, then open the file in the third column.
- A DocID alone (GOALS, EXD, FPF) means the whole publication: open its `Open first` file.

## Publications

{chr(10).join(pubs)}

## Patterns and reference sections ({len(rows)})

| ID | Title | File | Lines |
| --- | --- | --- | --- |
"""
    return header + "\n".join(rows) + "\n"


def count_check(docs: list[Doc], outs: list[OutFile]) -> list[str]:
    """Compare pattern counts with the 'Patterns' column of upstream DPF catalogues."""
    declared: dict[str, int] = {}
    for doc in docs:
        if not doc.src.startswith("DPFs/") or not doc.src.endswith("README.md"):
            continue
        for line in doc.lines:
            m = re.match(r"^\|\s*\[([^\]]+)\]\(([^)]+)\)[^|]*\|[^|]*\|\s*(\d+)\s*\|", line)
            if not m:
                continue
            for d in docs:
                if d.docid and (f"({d.docid})" in m.group(1) or d.title == m.group(1)):
                    declared[d.docid] = int(m.group(3))
    notes = []
    for doc in docs:
        if doc.docid not in declared:
            continue
        actual = 0
        for out in (o for o in outs if o.doc is doc):
            for h in out.headings:
                hid = heading_id(heading_text(h.text)) if h.level == 2 else None
                if hid and hid[0].split(".")[0] == doc.docid and "Reference" not in hid[0] and ":" not in hid[0]:
                    actual += 1
        if actual != declared[doc.docid]:
            notes.append(f"{doc.docid}: catalogue says {declared[doc.docid]} patterns, split found {actual}")
    return notes


def split(source: Path, out_dir: Path) -> None:
    sha, date = git_edition(source)
    docs = discover(source)
    outs: list[OutFile] = []
    for doc in docs:
        planner = {"core": plan_core, "framework": plan_framework, "verbatim": plan_verbatim}[doc.kind]
        outs.extend(planner(doc))
    paths = [o.path for o in outs]
    dup = {p for p in paths if paths.count(p) > 1}
    if dup:
        raise SplitError(f"Two sections map to the same output file: {sorted(dup)[:5]}. Update the planners. Nothing was changed.")

    links = LinkMap(docs, outs, sha)
    tmp = out_dir / ".fpf-split-tmp"
    if tmp.exists():
        shutil.rmtree(tmp)
    line_counts: dict[str, int] = {}
    try:
        for out in outs:
            text = links.rewrite(out).rstrip() + "\n"
            if out.generated:
                text = text.rstrip() + "\n" + out.generated
            target = tmp / out.path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
            line_counts[out.path] = text.count("\n")
        (tmp / "PATTERN-INDEX.md").write_text(
            pattern_index(docs, outs, links, sha, date, line_counts), encoding="utf-8")
    except BaseException:
        shutil.rmtree(tmp, ignore_errors=True)
        raise

    old = out_dir / ".fpf-split-old"
    if old.exists():
        shutil.rmtree(old)
    old.mkdir()
    for name in GENERATED:
        if (out_dir / name).exists():
            shutil.move(str(out_dir / name), str(old / name))
        shutil.move(str(tmp / name), str(out_dir / name))
    shutil.rmtree(old)
    shutil.rmtree(tmp)

    core = [o for o in outs if o.doc.kind == "core"]
    dpf = [o for o in outs if o.path.startswith("dpfs/")]
    frameworks = [d for d in docs if d.kind == "framework" and d.src.startswith("DPFs/")]
    print(f"Upstream ailev/FPF {sha} ({date})")
    print(f"  sections/: {len(core)} files from FPF-Spec.md")
    print(f"  dpfs/:     {len(dpf)} files from {len(frameworks)} publications (DPFs and Suite references)")
    print(f"  library/:  {len([o for o in outs if o.path.startswith('library/')])} files")
    print(f"  links rewritten to local files: {links.rewritten}")
    if links.unresolved:
        print(f"  local links left as in upstream (target not found): {len(links.unresolved)}")
        for item in links.unresolved[:15]:
            print(f"    {item}")
    for note in count_check(docs, outs):
        print(f"  NOTE {note}")
    print(f"Wrote {', '.join(GENERATED)} into {out_dir}")
    print(f"Next: python3 {out_dir / 'scripts/check_skill.py'}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--source", type=Path, default=SKILL_DIR / "FPF",
                        help="ailev/FPF checkout (default: <skill>/FPF)")
    parser.add_argument("--out", type=Path, default=SKILL_DIR, help="skill directory to write into")
    args = parser.parse_args()
    try:
        split(args.source.resolve(), args.out.resolve())
    except SplitError as exc:
        print(f"split_spec: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
