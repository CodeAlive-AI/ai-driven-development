# fpf-problem-solving-skill

[Русская версия (README-RU.md)](README-RU.md)

AI coding agent skill for the [First Principles Framework (FPF)](https://github.com/ailev/FPF) by [Anatoly Levenchuk](https://github.com/ailev).

FPF is a transdisciplinary reasoning architecture for systems engineering, knowledge coordination, and mixed human/AI teams.

FPF is a **thinking amplifier** — it helps you plan deeper and make better decisions by systematically exploring relevant alternatives instead of anchoring on the first idea.

## How it works

This skill functions as **agentic RAG** — retrieval-augmented generation driven by the agent itself, with no external vector database or embedding pipeline. The 82,000-line FPF specification is split into a two-level hierarchy (20 directories, 269 files). SKILL.md provides a thinking-verb router that maps the user's intent to the right section, including decision, causality, temporal reasoning, architecture description, publication stability, SoTA-pack refresh, and provenance needs. The agent then navigates `_index.md` files to pick the narrowest sub-section (~300 lines) and loads only that into context. The agent is the retriever, the router, and the reasoner — all in one loop.

## Install

```bash
npx skills add CodeAlive-AI/fpf-problem-solving-skill -g
```

## Structure

```
sections/
  04-part-a-kernel-architecture-cluster/
    _index.md                          # TOC with descriptions of all sub-sections
    01-a-0---onboarding-glossary.md    # 137 lines
    02-a-1---holonic-foundation.md     # 185 lines
    ...                                # 19 sub-sections total
  08-part-c-kernel-extensions-specifications/
    _index.md
    ...                                # 49 sub-sections
  ...                                  # 20 directories total
```

The agent reads `_index.md` first, picks the right sub-section file, and loads only that.

## Sections

| # | Section | Sub-sections |
|---|---------|:---:|
| 01 | Title page | 0 |
| 02 | Table of Content | 1 |
| 03 | Preface | 17 |
| 04 | Part A — Kernel Architecture | 19 |
| 05 | A.IV.A — Signature Stack & Boundary | 22 |
| 06 | A.V — Constitutional Principles | 33 |
| 07 | Part B — Trans-disciplinary Reasoning | 25 |
| 08 | Part C — Kernel Extensions | 49 |
| 09 | Part D — Ethics & Conflict | 1 |
| 10 | Part E — Constitution & Authoring | 0 |
| 11 | E-I — FPF Constitution | 42 |
| 12 | Part F — Unification Suite | 0 |
| 13 | F.I — Context of Meaning and Lexical Inputs | 19 |
| 14 | UTS Layout A | 0 |
| 15 | UTS Layout B | 1 |
| 16 | Part G — SoTA Patterns Kit | 15 |
| 17 | Part H — Glossary | 0 |
| 18 | Part I — Annexes | 1 |
| 19 | Part J — Indexes | 1 |
| 20 | Part K — Lexical Debt | 3 |

## Updating after FPF spec changes

When the upstream FPF specification changes, two things need updating:

### 1. Regenerate section files

Pull the submodule and re-run the splitter to rebuild the `sections/` hierarchy:

```bash
git submodule update --remote
python3 scripts/split_spec.py
```

### 2. Update SKILL.md navigation

The section files are raw content — `SKILL.md` is the navigation layer on top.
After regenerating, review whether the thinking-verb router, use cases, or Section INDEX
in `SKILL.md` need updating to reflect new, changed, or removed content.

See **[FPF-SKILL-UPDATE-GUIDE.md](FPF-SKILL-UPDATE-GUIDE.md)** for the full
methodology: what to check, how to validate router entries, and how to run an FPF self-audit
on the skill file itself.

> **Note:** the `FPF` submodule temporarily tracks a fork ([rodion-m/FPF](https://github.com/rodion-m/FPF), branch `fix/restore-orphaned-part-headings`) that restores the Part D/E/F/G section headings accidentally deleted upstream — see [ailev/FPF#42](https://github.com/ailev/FPF/issues/42) and [PR #43](https://github.com/ailev/FPF/pull/43). It will be re-pinned to upstream `ailev/FPF` once the PR is merged.

## Credits

- **FPF specification**: [Anatoly Levenchuk](https://github.com/ailev) — [github.com/ailev/FPF](https://github.com/ailev/FPF)
- **Skill packaging**: [CodeAlive-AI](https://github.com/CodeAlive-AI)

## License

MIT
