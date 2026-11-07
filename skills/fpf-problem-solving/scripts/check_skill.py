#!/usr/bin/env python3
"""Check that SKILL.md and the READMEs agree with the generated FPF Library.

  python3 scripts/check_skill.py

Run after scripts/split_spec.py. It changes nothing; it lists each problem with its place and the fix.
Checks:
  - SKILL.md frontmatter: only name and description; description at most 1024 characters, no < or >
  - one upstream commit in SKILL.md, README.md, README-RU.md and PATTERN-INDEX.md
  - every Core or DPF ID mentioned in SKILL.md and references/core-router.md (Map A) resolves
  - every domain framework (DPF) appears in SKILL.md Map B
  - every Map A group and row need in references/core-router.md is named in the SKILL.md Map A overview
  - SKILL.md body stays within BUDGET_TOKENS (characters / 4, the skills-management estimate) and
    "When to use" within USE_BULLETS bullets
  - Core section counts in README.md and README-RU.md match sections/
  - "N domain frameworks" in SKILL.md and README.md, "N доменных" in README-RU.md match dpfs/
  - every local link and path in SKILL.md and the router exists; every file in PATTERN-INDEX.md exists
Standard library only.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
INDEX = SKILL_DIR / "PATTERN-INDEX.md"
ROW_RE = re.compile(r"^\| ([^|]+?) \| ([^|]*?) \| ([^|]+?) \| ([^|]+?) \|$")
TOKEN_RE = re.compile(r"(?<![\w./-])([A-Z][A-Za-z]*(?:\.[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)+(?::[A-Za-z0-9.]+)?)")
SHA_RE = re.compile(r"\b[0-9a-f]{40}\b")
ROUTER = SKILL_DIR / "references" / "core-router.md"
# SKILL.md is loaded whole on every use, so its body is held near 4,000 tokens (skills-management
# estimates characters / 4 and penalises above 4,000); Map A lives in references/core-router.md and is
# read only for a general thinking need. Growth came from one use-case bullet or one row per new pattern,
# so the budget makes the sync condense instead of append.
BUDGET_TOKENS = 4_800
USE_BULLETS = 10

problems: list[str] = []


def problem(where: str, what: str, fix: str) -> None:
    problems.append(f"  {where}: {what}\n      fix: {fix}")


def load_index() -> tuple[dict[str, tuple[str, str, str]], dict[str, tuple[str, str, str]], str]:
    if not INDEX.is_file():
        sys.exit("check_skill: PATTERN-INDEX.md is missing; nothing was checked.\n"
                 f"  next: python3 {SKILL_DIR / 'scripts/split_spec.py'} --source <ailev/FPF checkout>")
    text = INDEX.read_text(encoding="utf-8")
    pubs: dict[str, tuple[str, str, str]] = {}
    pats: dict[str, tuple[str, str, str]] = {}
    section = None
    for line in text.splitlines():
        if line.startswith("## Publications"):
            section = pubs
        elif line.startswith("## Patterns"):
            section = pats
        m = ROW_RE.match(line)
        if section is not None and m and not m.group(1).startswith(("DocID", "ID", "---")):
            section[m.group(1)] = (m.group(2), m.group(3), m.group(4))
    sha = SHA_RE.search(text)
    return pubs, pats, sha.group(0) if sha else ""


def core_clusters() -> set[str]:
    """Cluster labels such as A.IV.A and A.V, taken from the Core section headings."""
    found = set()
    for idx in (SKILL_DIR / "sections").glob("*/_index.md"):
        first = idx.read_text(encoding="utf-8").split("\n", 1)[0]
        m = re.search(r"\bCluster ([A-K](?:\.[IVX]+)+(?:\.[A-Z])?)\b", first)
        if m:
            found.add(m.group(1))
    return found


CLUSTERS: set[str] = set()


def resolves(token: str, pats: dict, pubs: dict) -> bool:
    if token in pats or token in pubs or token in CLUSTERS or token.endswith(":End"):
        return True
    base, colon, section = token.partition(":")
    if colon:
        parts = section.split(".")
        while parts:
            if f"{base}:{'.'.join(parts)}" in pats:
                return True
            parts.pop()
        return base in pats or base in pubs
    return False


def check_frontmatter(text: str) -> None:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        problem("SKILL.md:1", "no YAML frontmatter", "start the file with ---, name, description, ---")
        return
    keys = re.findall(r"^([A-Za-z_-]+):", m.group(1), re.M)
    if keys != ["name", "description"]:
        problem("SKILL.md:1", f"frontmatter keys are {keys}", "keep exactly name and description")
    d = re.search(r'^description:\s*"(.*)"\s*$', m.group(1), re.M)
    if not d:
        problem("SKILL.md:3", "description is not one double-quoted line", "write description as one quoted line")
    else:
        if len(d.group(1)) > 1024:
            problem("SKILL.md:3", f"description has {len(d.group(1))} characters", "shorten it to 1024 or fewer")
        if re.search(r"[<>]", d.group(1)):
            problem("SKILL.md:3", "description contains < or >", "remove angle brackets")


def check_ids(name: str, lines: list[str], pats: dict, pubs: dict) -> int:
    known = {"FPF", "Library"} | {d for d in pubs} | set("ABCDEFGHIJK")
    seen = 0
    for n, line in enumerate(lines, 1):
        for token in TOKEN_RE.findall(line):
            token = token.rstrip(".")
            prefix = token.split(".")[0]
            if prefix not in known:
                continue
            seen += 1
            if resolves(token, pats, pubs):
                continue
            pieces = [p for p in token.split("-") if TOKEN_RE.fullmatch(p)]
            if len(pieces) > 1 and all(resolves(p, pats, pubs) for p in pieces):
                continue  # a range such as A.17-A.19
            problem(f"{name}:{n}", f"ID {token} does not resolve in PATTERN-INDEX.md",
                    f"run `python3 scripts/find_pattern.py {token}` for nearby IDs (upstream may have renamed it), then fix or remove it")
    return seen


def check_map_b(text: str, pubs: dict) -> int:
    start = text.find("### Map B")
    end = text.find("### Map C")
    if start < 0 or end < 0:
        problem("SKILL.md", "Map B or Map C heading is missing", "keep '### Map B' and '### Map C' headings")
        return 0
    block = text[start:end]
    frameworks = [d for d, (_, path, home) in pubs.items()
                  if path.startswith("dpfs/") and not path.endswith("suite-reference/_index.md")]
    for docid in frameworks:
        if not re.search(rf"(?<![\w.]){re.escape(docid)}(?![\w])", block):
            title, path, home = pubs[docid]
            problem("SKILL.md Map B", f"{docid} ({title}, {home}) is not mapped",
                    f"add '{docid} — <what it works on>' to the matching row; read {path} for its subject")
    return len(frameworks)


def section_counts() -> dict[str, int]:
    counts = {}
    for d in sorted((SKILL_DIR / "sections").iterdir()):
        if d.is_dir():
            counts[d.name[:2]] = len([f for f in d.iterdir() if f.suffix == ".md" and f.name != "_index.md"])
    return counts


def check_core_table(name: str, lines: list[str], counts: dict[str, int]) -> None:
    found = set()
    for n, line in enumerate(lines, 1):
        m = re.match(r"^\| (\d\d) \| (.+?) \| (\d+) \|", line)
        if not m:
            continue
        num, count = m.group(1), int(m.group(3))
        found.add(num)
        if num not in counts:
            problem(f"{name}:{n}", f"section {num} is not in sections/", "remove the row or regenerate sections/")
            continue
        if count != counts[num]:
            problem(f"{name}:{n}", f"section {num} says {count} files, sections/ has {counts[num]}",
                    f"set the count to {counts[num]}")
    for num in counts:
        if num not in found:
            problem(name, f"Core section {num} has no row", f"add a row for sections/{num}-…")


def body_tokens(text: str) -> int:
    m = re.match(r"^---\n.*?\n---\n", text, re.S)
    return len(text[m.end():] if m else text) // 4


def check_budget(text: str) -> None:
    tokens = body_tokens(text)
    if tokens > BUDGET_TOKENS:
        problem("SKILL.md", f"body is about {tokens} tokens, budget {BUDGET_TOKENS}",
                "condense instead of appending: put Core routing in references/core-router.md, name a pattern family "
                "(find_pattern.py lists its members) rather than each member, merge rows that serve one need")
    m = re.search(r"^## When to use\n(.*?)(?=^## )", text, re.S | re.M)
    if not m:
        problem("SKILL.md", "no '## When to use' section", "keep a short '## When to use' list of broad situations")
    else:
        bullets = len(re.findall(r"^- ", m.group(1), re.M))
        if bullets > USE_BULLETS:
            problem("SKILL.md When to use", f"{bullets} bullets, at most {USE_BULLETS}",
                    "extend an existing bullet with the new kind of use; a new pattern goes into its map row, not here")


def check_router(skill_text: str) -> int:
    """Map A rows live in the router; the SKILL.md overview must name each group and each row's need."""
    if not ROUTER.is_file():
        problem("references/core-router.md", "file is missing", "restore Map A from git; SKILL.md Step 0 sends general needs there")
        return 0
    start, end = skill_text.find("### Map A"), skill_text.find("### Map B")
    overview = skill_text[start:end].lower() if 0 <= start < end else ""
    if not overview:
        problem("SKILL.md", "Map A overview is missing", "keep a '### Map A' section before '### Map B' listing the router's groups and needs")
        return 0
    if "references/core-router.md" not in overview:
        problem("SKILL.md Map A", "overview does not link the router", "link [references/core-router.md](references/core-router.md)")
    rows = 0
    for n, line in enumerate(ROUTER.read_text(encoding="utf-8").splitlines(), 1):
        g = re.match(r"^## (A\d+)\. (.+?) —", line)
        if g and f"{g.group(1).lower()}. {g.group(2).lower()}" not in overview:
            problem(f"core-router.md:{n}", f"group {g.group(1)} is not in the SKILL.md overview",
                    f"add '**{g.group(1)}. {g.group(2)}** — <its needs>' to the SKILL.md Map A overview")
        r = re.match(r"^\| \*\*(.+?)\*\*", line)
        if r:
            rows += 1
            need = re.sub(r"\s+", " ", r.group(1)).strip(" /").lower()
            if need not in overview:
                problem(f"core-router.md:{n}", f"row need '{r.group(1)}' is not named in the SKILL.md Map A overview",
                        "add it, in a few words, to its group's line in the overview")
    return rows


def check_framework_count(name: str, text: str, actual: int, pattern: str) -> None:
    for m in re.finditer(pattern, text):
        if int(m.group(1)) != actual:
            line = text[:m.start()].count("\n") + 1
            problem(f"{name}:{line}", f"says {m.group(1)} domain frameworks, dpfs/ has {actual}",
                    f"change the number to {actual}")


def check_links(name: str, lines: list[str], base: Path) -> None:
    for n, line in enumerate(lines, 1):
        for target in re.findall(r"\]\(([^)\s]+)\)", line):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            if not (base / target.split("#")[0]).exists():
                problem(f"{name}:{n}", f"link {target} does not exist", "fix the path (links are relative to the file)")
        for path in re.findall(r"`((?:sections|dpfs|library|scripts|references)/[^`\s]+|PATTERN-INDEX\.md)`", line):
            if "<" in path or "…" in path:
                continue
            if not (SKILL_DIR / path).exists():
                problem(f"{name}:{n}", f"path {path} does not exist", "fix the path (relative to the skill directory) or regenerate the library")


def main() -> int:
    pubs, pats, sha = load_index()
    CLUSTERS.update(core_clusters())
    skill_text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    skill_lines = skill_text.splitlines()
    check_frontmatter(skill_text)

    for name in ("SKILL.md", "README.md", "README-RU.md"):
        path = SKILL_DIR / name
        if not path.is_file():
            problem(name, "file is missing", "restore it from git")
            continue
        shas = set(SHA_RE.findall(path.read_text(encoding="utf-8")))
        if shas != {sha}:
            problem(name, f"upstream commit {sorted(shas) or 'none'} differs from PATTERN-INDEX.md {sha}",
                    f"write the upstream commit as `{sha}`")

    ids = check_ids("SKILL.md", skill_lines, pats, pubs)
    router_lines = ROUTER.read_text(encoding="utf-8").splitlines() if ROUTER.is_file() else []
    ids += check_ids("core-router.md", router_lines, pats, pubs)
    rows = check_router(skill_text)
    mapped = check_map_b(skill_text, pubs)
    counts = section_counts()
    check_budget(skill_text)
    for name in ("README.md", "README-RU.md"):
        if (SKILL_DIR / name).is_file():
            check_core_table(name, (SKILL_DIR / name).read_text(encoding="utf-8").splitlines(), counts)
    check_framework_count("SKILL.md", skill_text, mapped, r"(\d+) domain frameworks")
    if (SKILL_DIR / "README.md").is_file():
        check_framework_count("README.md", (SKILL_DIR / "README.md").read_text(encoding="utf-8"), mapped, r"(\d+) domain frameworks")
    if (SKILL_DIR / "README-RU.md").is_file():
        check_framework_count("README-RU.md", (SKILL_DIR / "README-RU.md").read_text(encoding="utf-8"), mapped, r"(\d+) доменн")
    check_links("SKILL.md", skill_lines, SKILL_DIR)
    check_links("core-router.md", router_lines, ROUTER.parent)
    missing = [p for _, p, _ in pats.values() if not (SKILL_DIR / p).is_file()]
    missing += [p for _, p, _ in pubs.values() if not (SKILL_DIR / p).is_file()]
    if missing:
        problem("PATTERN-INDEX.md", f"{len(missing)} listed files are missing, e.g. {missing[0]}",
                "regenerate with scripts/split_spec.py; do not edit generated trees by hand")

    if problems:
        print(f"check_skill: {len(problems)} problem(s); nothing was changed.")
        print("\n".join(problems))
        return 1
    print(f"check_skill: OK — {ids} ID mentions resolve, {mapped} domain frameworks mapped, {rows} Map A rows "
          f"in the overview, {len(counts)} Core sections counted, {len(pats)} patterns indexed, SKILL.md body "
          f"~{body_tokens(skill_text)}/{BUDGET_TOKENS} tokens, upstream {sha[:12]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
