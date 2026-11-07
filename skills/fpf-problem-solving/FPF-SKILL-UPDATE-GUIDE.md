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
- SKILL.md stays within its reading budget (36,000 characters) and "When to use" within ten bullets —
  when either is exceeded, condense instead of appending (see section 2);
- Core counts in both README tables match `sections/`;
- "N domain frameworks" (and "N доменных" in README-RU) match `dpfs/`;
- local links and paths in SKILL.md exist; every file listed in PATTERN-INDEX.md exists.

The checker passing is necessary, not sufficient: it proves the navigation points at real files, not
that it points at the right ones. Then review the navigation layer below.

## 2. Update the navigation layer

### Description (frontmatter)

Decides WHETHER the skill triggers. It names what the Library does, trigger phrases (FPF, DPF, pattern
IDs), and negative triggers. Add a phrase only for a new kind of use, not for each new pattern.

### When to use

At most ten bullets of broad situations a person recognizes without FPF vocabulary. Ask: "Would a user
who has never heard of FPF describe their problem this way?" A new pattern goes into its map row, never
into this list; extend an existing bullet only for a new kind of use. (A bullet per pattern grew this list
to sixty entries before; the checker now caps it.)

### Step 0 and the maps

| Map | What it routes | How to maintain |
|---|---|---|
| **Step 0** | how FPF came up → which map | Stable; change only when a new way of entering FPF appears. |
| **Map A — Core router** | thinking need → Core section and patterns, in five groups (model the subject; reason, evaluate, decide; obtain results and improve work; architecture and structure; express, publish, sources) | Route a new Core pattern through the existing row of its thinking need; add a row only for a distinct need, in the group it belongs to. Put the usual starting pattern first in the cell. When a family grows, name the family (`find_pattern.py <ID>` lists its members with titles) instead of every member. |
| **Map B — Domain frameworks** | field question → DPF DocID | Every DPF must be listed (the checker enforces it). Add a new DPF to its Suite row or to the standalone row that fits, with a few words on what it works on, taken from `dpfs/_index.md` or the Suite `_index.md`. |
| **Map C — Common troubles** | a trouble as people notice it → the pattern to start with | Curated, not generated: it paraphrases Anatoly Levenchuk's cheatsheet of frequently used patterns. The first ID is the start; after `·` a cell may name a neighbouring case and its pattern. Name a pattern, not a bare DocID, when the framework's entries do not cover the trouble. Fix an ID when upstream renames it; add or remove rows only on the owner's request or a new edition of the cheatsheet. |

Each map row must serve a distinct need (A.7 Strict Distinction). If two rows feel interchangeable,
merge them. Within a group, keep rows scannable: an agent pattern-matches the left column.

To add a row:
1. Identify the need the new content serves (what does it help the user DO?).
2. Name it with a bold verb (Map A) or the field (Map B) or the trouble in plain words (Map C).
3. Point to IDs, not to numbered file paths: file names carry ordinal prefixes that shift upstream.
4. Check for overlap with existing rows — merge if the need is the same.

To validate a row: simulate a user query that should trigger it, pass the row's IDs to `find_pattern.py`
(one card per ID with *use when* and *not when*), and check that the card matches the query. When two
rows compete for one query, say in the cell which case each takes.

### Library layout

A short table of entry points (PATTERN-INDEX, Core folders, DPF catalogue, Suite and framework indexes,
Library documents). Change it only when the generated layout changes. The Core sections table with
counts lives in the READMEs; SKILL.md routes through Map A instead.

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
| **Cognitive Elegance (P-1)** | Is SKILL.md still compact (the checker enforces the budget)? Growth should be justified by navigation value, not completeness for its own sake. |

## Process summary

```
1. Regenerate the library from upstream ailev/FPF (split_spec.py --source …)
2. Run check_skill.py; fix every listed problem
3. For each upstream change, ask: "What need does this serve?" and update the matching map row
4. Update the description / "When to use" only for a new kind of use
5. Run the FPF self-audit and a few simulated queries through find_pattern.py (cards, DocIDs, --search)
6. Sync README.md and README-RU.md (tables, commit); rerun check_skill.py
```
