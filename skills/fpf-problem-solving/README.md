# fpf-problem-solving-skill

[Русская версия (README-RU.md)](README-RU.md)

AI coding agent skill for the [First Principles Framework (FPF)](https://github.com/ailev/FPF) by [Anatoly Levenchuk](https://github.com/ailev).

FPF is a transdisciplinary reasoning architecture for systems engineering, knowledge coordination, and mixed human/AI teams.

FPF is a **thinking amplifier** — it helps you plan deeper and make better decisions by systematically exploring relevant alternatives instead of anchoring on the first idea.

## How it works

This skill functions as **agentic RAG** — retrieval-augmented generation driven by the agent itself, with no external vector database or embedding pipeline. The 97,000-line upstream FPF specification is split into a two-level hierarchy (15 directories, 324 files). SKILL.md provides a thinking-verb router that maps the user's intent to the right section, including applying a selected pattern to its first useful result, distinguishing relations from their occurrences, decision, causality, temporal reasoning, architecture description and synthesis, constraint-governed unfolding, narrative rendering, ontic governance, publication stability, SoTA-pack refresh, and provenance needs. The agent then navigates `_index.md` files to pick the narrowest sub-section and loads only that into context. The agent is the retriever, the router, and the reasoner — all in one loop.

## Install

```bash
npx skills add CodeAlive-AI/fpf-problem-solving-skill -g
```

## Structure

```
sections/
  05-part-a---kernel-architecture-cluster/
    _index.md                          # TOC with descriptions of all sub-sections
    01-a-0---onboarding-glossary.md    # 248 lines
    02-a-1---holonic-foundation.md     # 185 lines
    ...                                # 21 sub-sections total
  09-part-c-kernel-extension-specifications/
    _index.md
    ...                                # 73 sub-sections
  ...                                  # 15 directories total
```

The agent reads `_index.md` first, picks the right sub-section file, and loads only that.

## Sections

| # | Section | Sub-sections |
|---|---------|:---:|
| 01 | Title page | 0 |
| 02 | Table of Content | 0 |
| 03 | FPF Readme | 7 |
| 04 | Preface | 21 |
| 05 | Part A — Kernel Architecture | 21 |
| 06 | A.IV.A — Signature Stack & Boundary | 26 |
| 07 | A.V — Constitutional Principles | 37 |
| 08 | Part B — Trans-disciplinary Reasoning | 25 |
| 09 | Part C — Kernel Extensions | 73 |
| 10 | Part D — Ethics & Conflict | 5 |
| 11 | Part E — Constitution & Authoring | 57 |
| 12 | Part F — Unification Suite | 21 |
| 13 | Part G — SoTA Patterns Kit | 15 |
| 14 | Part H — Reserved | 0 |
| 15 | Part I — Annexes | 1 |

## Updating after FPF spec changes

When the upstream FPF specification changes, two things need updating:

### 1. Regenerate section files

Clone the official upstream `ailev/FPF` into a temporary skill layout outside this repository, then run the splitter there and replace the tracked `sections/` tree with the generated result:

```bash
tmpdir="$(mktemp -d)"
mkdir -p "$tmpdir/skill/scripts"
git clone https://github.com/ailev/FPF.git "$tmpdir/skill/FPF"
cp scripts/split_spec.py "$tmpdir/skill/scripts/split_spec.py"
python3 "$tmpdir/skill/scripts/split_spec.py"
rsync -a --delete "$tmpdir/skill/sections/" sections/
rm -rf "$tmpdir"
```

### 2. Update SKILL.md navigation

The section files are raw content — `SKILL.md` is the navigation layer on top.
After regenerating, review whether the thinking-verb router, use cases, or Section INDEX
in `SKILL.md` need updating to reflect new, changed, or removed content.

See **[FPF-SKILL-UPDATE-GUIDE.md](FPF-SKILL-UPDATE-GUIDE.md)** for the full
methodology: what to check, how to validate router entries, and how to run an FPF self-audit
on the skill file itself.

## Credits

- **FPF specification**: [Anatoly Levenchuk](https://github.com/ailev) — [github.com/ailev/FPF](https://github.com/ailev/FPF)
- **Skill packaging**: [CodeAlive-AI](https://github.com/CodeAlive-AI)

## License

MIT
