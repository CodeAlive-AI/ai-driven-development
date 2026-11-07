# fpf-problem-solving-skill

[Русская версия (README-RU.md)](README-RU.md)

AI coding agent skill for the FPF Library by [Anatoly Levenchuk](https://github.com/ailev):
[First Principles Framework (FPF)](https://github.com/ailev/FPF) Core plus 36 domain frameworks (DPFs),
all stored locally.

FPF is a transdisciplinary reasoning architecture for systems engineering, knowledge coordination, and
mixed human/AI teams. It is a **thinking amplifier**: it helps plan deeper and decide better by
systematically exploring relevant alternatives instead of anchoring on the first idea. The domain
frameworks apply it to particular fields — strategy, goals and OKR, operations, research, decision
design, systems engineering, explanation, mathematics, human capability development and others.

## How it works

The skill is **agentic RAG** without a vector database: the agent is the retriever, the router and the
reasoner.

1. **Entry.** `SKILL.md` Step 0 asks how FPF came up: a named pattern (`F.19`, `C.11.DUA`, `GOALS.7`),
   a familiar trouble, a question inside a field, or a general thinking need.
2. **Three maps.** Map A routes a thinking need to Core patterns, in five groups. Map B routes a field
   question to its domain framework. Map C maps frequent troubles in work with an agent — hedging
   instead of judgment, a lost original question, resuming after a handoff, look-alike options — to the
   pattern that addresses them, following Anatoly Levenchuk's cheatsheet of frequently used patterns.
3. **Resolution.** `scripts/find_pattern.py <ID>` resolves a PatternID or a section reference
   (`HCD.12:4.1`) to a card — when to use the pattern and when not to, its family, its file and section
   map; several IDs give one card each, to choose between them. A DocID lists the framework's entries
   (situation → start with) and patterns; `--search <words>` ranks entries, titles and keywords.
4. **Reading.** The agent opens the narrowest file: Problem frame and Solution first, then the
   Conformance Checklist to check its own result, and stops at the first useful result.

The upstream publications are split into one file per section, and every link between them —
in-document anchors, relative paths, GitHub and fpf.tools links — is rewritten to the local file, so
references can be followed offline.

## Install

```bash
npx skills add CodeAlive-AI/fpf-problem-solving-skill -g
```

## Example prompt

> Use the FPF skill. Help me structure my project / problem / programme.
> Use plain language for an engineer-manager.
> Propose: (1) bounded contexts / specialisations, (2) decision criteria, (3) key alternatives,
> (4) hand-offs, and (5) missing evidence or tests before commitment.
> Introduce internal FPF names only when they add precision.

## Structure

```text
SKILL.md            entry, maps A–C, reading rules
PATTERN-INDEX.md    every DocID and PatternID → local file (generated)
sections/           FPF Core: one folder per part, one file per pattern; _index.md lists the files
dpfs/               domain frameworks: dpfs/<suite>/<docid>/ or dpfs/<docid>/
  management-dpf-suite/goals/_index.md   practical entries, contents with keywords, file list
library/            Library readme, USING-FPF.md, LICENSING.md, Library Architectural Reference
scripts/            split_spec.py (regenerate), find_pattern.py (resolve), check_skill.py (validate)
```

## Core sections

| # | Section | Sub-sections |
|---|---------|:---:|
| 01 | Title page | 0 |
| 02 | Table of Contents | 0 |
| 03 | FPF Readme | 12 |
| 04 | Architectural Reference | 22 |
| 05 | Part A — Kernel Architecture | 38 |
| 06 | A.IV.A — Signature Stack & Boundary | 29 |
| 07 | A.V — Constitutional Principles | 50 |
| 08 | Part B — Trans-disciplinary Reasoning | 43 |
| 09 | Part C — Kernel Extensions | 130 |
| 10 | Part D — Ethics & Conflict | 5 |
| 11 | Part E — Constitution & Authoring | 69 |
| 12 | Part F — Unification Suite | 24 |
| 13 | Part G — SoTA Patterns Kit | 15 |
| 14 | Part H — Reserved | 0 |

Counts follow upstream H2 headings. The Architectural Reference has 21 content sections plus the
content-free `FPF.Reference:End` boundary marker.

## Domain frameworks

| Suite or group | Frameworks (DocID) |
|---|---|
| Management | STR, GOALS, OPS, ADM, CGOV, MA, FIN, MKT, CUST, EAM, LDR, CB, OCE, HRM |
| Engineering | SYSE, KCAE, SIE, CAD, MNT |
| Foundational Thinking | MATH, MMP, PHY, CMP, NOT |
| Human Capability Engineering | HCD, SOM |
| Standalone | PSDA, RMP, EXD, NSTD, IS, ECO, FDM, DTM, RHY, MDPE |

`dpfs/_index.md` is the upstream catalogue with what each framework works on.

## Updating after upstream changes

```bash
git clone --depth 1 https://github.com/ailev/FPF.git /tmp/fpf-upstream
python3 scripts/split_spec.py --source /tmp/fpf-upstream
python3 scripts/check_skill.py
```

The splitter replaces `sections/`, `dpfs/`, `library/` and `PATTERN-INDEX.md` only after every
publication has been split and validated. The checker lists what `SKILL.md` and these READMEs must
change: unresolved IDs, unmapped frameworks, counts, the upstream commit. See
**[FPF-SKILL-UPDATE-GUIDE.md](FPF-SKILL-UPDATE-GUIDE.md)** for the full method.

## Credits

- **FPF Library**: [Anatoly Levenchuk](https://github.com/ailev) — [github.com/ailev/FPF](https://github.com/ailev/FPF)
- **Skill packaging**: [CodeAlive-AI](https://github.com/CodeAlive-AI)

## License

Skill packaging and scripts: MIT. Adapted from the *FPF Library* by Anatoly Levenchuk — *First
Principles Framework (FPF)* Core, its domain frameworks and Library documents —
[ailev/FPF](https://github.com/ailev/FPF), upstream commit `e317958532699b762dd9e7baf460f97bad7a4c9c`.
The Library text is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); see the
[upstream licensing scope](https://github.com/ailev/FPF/blob/main/LICENSING.md). Changes: the
publications were split into section files with generated navigation indexes, their links were rewritten
to the local files, and `SKILL.md` adds an agent-oriented router and usage instructions. This adaptation
is not endorsed by the FPF author.
