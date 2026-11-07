# FPF Skill Update Guide

Methodology for keeping this skill in step with upstream [ailev/FPF](https://github.com/ailev/FPF)
— the FPF Library: Core (`FPF-Spec.md`), the domain frameworks (`DPFs/`), and the Library documents.
Discovered by applying FPF to its own skill file — dog-fooding the framework.

The skill exists for agent experience: an agent should learn from `SKILL.md` **when** to use FPF,
**where** to go for its case, and **how** to read and apply one pattern. Every update preserves that.

## When to update

- Upstream changed (the regular sync): new, renamed or removed patterns, frameworks or sections
- A map row is found to misroute (validated against real usage)
- Description trigger phrases no longer match how users actually invoke FPF

Per B.3.4 (Evidence Decay), the skill carries epistemic debt whenever upstream evolves and the skill
does not. The generated trees are always regenerated whole; only the navigation layer is edited by hand.

## 0. Regenerate the library (generated — never edit by hand)

```bash
git clone --depth 1 https://github.com/ailev/FPF.git /tmp/fpf-upstream
python3 skills/fpf-problem-solving/scripts/split_spec.py --source /tmp/fpf-upstream
python3 skills/fpf-problem-solving/scripts/check_skill.py
rm -rf /tmp/fpf-upstream
```

Use the default branch of official upstream `ailev/FPF`; never a fork. The splitter writes
`sections/` (Core), `dpfs/` (DPFs and Suite references), `library/` (Library readme, `USING-FPF.md`,
`LICENSING.md`, Library Architectural Reference) and `PATTERN-INDEX.md`, rewriting links to the local
files. It validates everything first and replaces nothing if a check fails; read its message, which
names the place to change in `scripts/split_spec.py`. Typical refusals:

- an unknown root publication upstream → add it to `ROOT_FILES` (or `ROOT_IGNORED`) deliberately;
- a DPF without a DocID row in `Library.Reference:11.1`, or a DocID mismatch → inspect upstream;
- a framework that does not follow Title → Table of Contents → Readme → … → adapt `plan_framework()`.

The splitter prints `NOTE` lines when a framework's pattern count differs from the upstream catalogue
and lists any local links it could not resolve; look at them, they usually mean an upstream layout change.
Headings inside fenced code blocks are never split points. Links pinned to an older upstream commit are
left as they are: they cite that edition.

Do not invent missing Part headings in the skill layer; if upstream omits a Part-level H1, reflect that
in the Library INDEX and README tables. Review upstream licensing notices when they change; keep the
attribution in SKILL.md and both READMEs accurate.

## 1. Run the checker and fix what it lists

`scripts/check_skill.py` changes nothing; each problem names the file, line and fix. It checks:

- frontmatter: only `name` and `description`; description at most 1024 characters, no angle brackets;
- one upstream commit in SKILL.md, README.md, README-RU.md and PATTERN-INDEX.md;
- every Core or DPF ID mentioned in SKILL.md resolves (a renamed pattern shows up here — use
  `python3 scripts/find_pattern.py <old ID>` for nearby IDs);
- every domain framework appears in Map B;
- Core counts in the Library INDEX and both README tables match `sections/`;
- "N domain frameworks" (and "N доменных" in README-RU) match `dpfs/`;
- local links and paths in SKILL.md exist; every file listed in PATTERN-INDEX.md exists.

The checker passing is necessary, not sufficient: it proves the navigation points at real files, not
that it points at the right ones. Then review the navigation layer below.

## 2. Update the navigation layer

### Description (frontmatter)

Decides WHETHER the skill triggers. It names what the Library does, trigger phrases (FPF, DPF, pattern
IDs), and negative triggers. Add a phrase only for a new kind of use, not for each new pattern.

### Use cases

Broad situations a person recognizes without FPF vocabulary. Ask: "Would a user who has never heard of
FPF describe their problem this way?" Prefer extending an existing bullet over adding one.

### Step 0 and the maps

| Map | What it routes | How to maintain |
|---|---|---|
| **Step 0** | how FPF came up → which map | Stable; change only when a new way of entering FPF appears. |
| **Map A — Core router** | thinking need → Core section and patterns, in five groups (model the subject; reason, evaluate, decide; obtain results and improve work; architecture and structure; express, publish, sources) | Route a new Core pattern through the existing row of its thinking need; add a row only for a distinct need, in the group it belongs to. |
| **Map B — Domain frameworks** | field question → DPF DocID | Every DPF must be listed (the checker enforces it). Add a new DPF to its Suite row or to the standalone row that fits, with a few words on what it works on, taken from `dpfs/_index.md` or the Suite `_index.md`. |
| **Map C — Common troubles** | a trouble as people notice it → one pattern | Curated, not generated: it paraphrases Anatoly Levenchuk's cheatsheet of frequently used patterns. Fix an ID when upstream renames it; add or remove rows only on the owner's request or a new edition of the cheatsheet. |

Each map row must serve a distinct need (A.7 Strict Distinction). If two rows feel interchangeable,
merge them. Within a group, keep rows scannable: an agent pattern-matches the left column.

To add a row:
1. Identify the need the new content serves (what does it help the user DO?).
2. Name it with a bold verb (Map A) or the field (Map B) or the trouble in plain words (Map C).
3. Point to IDs, not to numbered file paths: file names carry ordinal prefixes that shift upstream.
4. Check for overlap with existing rows — merge if the need is the same.

To validate a row: simulate a user query that should trigger it, resolve the IDs with
`find_pattern.py`, and check that the file's Problem frame matches the query.

### Library INDEX

The Core table must stay in sync with `sections/` (the checker compares counts). Each "When to use" cell
leads with a **bold thinking verb**: `**Verb**: what's inside`. The second table lists the DPF and Library
entry points; change it only when the generated layout changes.

### Composition guidance (Steps 1–4)

Update when new patterns create novel cross-section or Core–DPF composition needs, or new category-error
patterns are discovered. The natural synthesis order (decompose → evaluate → resolve) stays stable unless
FPF's reasoning architecture fundamentally changes.

## 3. Update the READMEs

README.md and README-RU.md are for humans on GitHub and must say the same thing:

- the Core sections table (counts are checked) and the domain frameworks table;
- the upstream commit in the License section (checked);
- "How it works" and "Structure" only when the navigation approach or layout changes.

Do not append a paragraph per new pattern ("Navigation also covers …"): the maps and PATTERN-INDEX.md
carry that, and the READMEs stay readable.

## How to validate (FPF self-audit)

After the checker passes, run these checks against the FPF patterns that matter most for a navigation artifact:

| FPF Pattern | Check |
|---|---|
| **Bounded Context (A.1.1)** | Does SKILL.md have clear entry/exit semantics? Do the maps bridge user-intent context to FPF context without collapsing them? |
| **Strict Distinction (A.7)** | Are use cases (admission) and maps (navigation) still separate? Does any row conflate two different needs? Is Core kept distinct from a DPF? |
| **Trust & Assurance (B.3)** | Can each row be grounded in actual pattern content? Would following the path produce a useful result? |
| **Multi-View (E.17)** | Do the maps serve different roles (engineer, manager, researcher) without being locked to one view? |
| **Epistemic Debt (B.3.4)** | Are there sections or frameworks reachable from no map? Intentional, or an omission? |
| **Composition (B.1)** | Does Step 4 still give adequate synthesis guidance across sections and across Core and DPFs? |
| **Cognitive Elegance (P-1)** | Is SKILL.md still compact? Growth should be justified by navigation value, not completeness for its own sake. |

## Process summary

```
1. Regenerate the library from upstream ailev/FPF (split_spec.py --source …)
2. Run check_skill.py; fix every listed problem
3. For each upstream change, ask: "What need does this serve?" and update the matching map row
4. Update description / use cases only for a new kind of use
5. Run the FPF self-audit and a few simulated queries through find_pattern.py
6. Sync README.md and README-RU.md (tables, commit); rerun check_skill.py
```
