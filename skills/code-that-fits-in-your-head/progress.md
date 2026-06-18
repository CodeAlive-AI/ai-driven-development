# code-that-fits-in-your-head — Creation Log

Skill built from Mark Seemann's *Code That Fits in Your Head: Heuristics for Software Engineering* (Addison-Wesley, 2021, 408 pp).

## Final Stats

| Piece | Count |
|-------|-------|
| SKILL.md | 1 (70 lines, YAML frontmatter + philosophy + chapter index) |
| guidelines.md | 1 (330 lines, task/symptom/practice routing + decision tree + file index) |
| Workflows | 4 (review-code, add-feature-outside-in, debug-defect, threat-model) |
| Reference themes | 13 folders |
| Reference files | 39 |
| **Total markdown files** | **47** |
| **Longest reference file** | 248 lines (`evolution/examples.md`) |

All reference files are within the 50-250 line budget.

## Theme breakdown

| Theme | Files | Source chapters |
|-------|-------|-----------------|
| foundations/ | 2 | Ch 3 + §14.1 |
| codebase-setup/ | 3 | Ch 2 |
| outside-in-tdd/ | 4 | Ch 4 + Ch 6 + Ch 11 |
| encapsulation/ | 3 | Ch 5 + §7.2.5 |
| decomposition/ | 5 | Ch 7 (− §7.2.5) + §13.1 |
| api-design/ | 3 | Ch 8 |
| separation-of-concerns/ | 3 | §13.2 + §15.1 |
| teamwork-git/ | 3 | Ch 9 + §2.2.1 |
| evolution/ | 4 | Ch 10 + §14.2 |
| troubleshooting/ | 3 | Ch 12 |
| security/ | 3 | §15.2 |
| code-navigation/ | 2 | Ch 16 + §15.3 |
| practices-glossary/ | 1 | Appendix A |

## Conversion notes

- PDF converted via Document AI (quality) *and* `pdftotext -layout` (reading order). The layout version (`book.clean.txt`) was used for extraction because Document AI scrambled page order inside large chunks.
- Page headers ("Chapter N Title") repeating every page and letter-spaced section titles ("3.1 P u r p o s e") were stripped by each subagent during extraction.
- C# code examples preserved verbatim with ```csharp fencing.
- Practice A.1 (The 50/72 Rule) was missing from the PDF's Appendix A due to a page-break artefact; filled with standard Git convention.

## Ownership / Follow-ups

- If the book is re-sourced cleanly, re-run extraction just for `practices-glossary/` to confirm A.1 content.
- No workflows have been battle-tested against real PRs yet — refinement should come from actual usage.

## Post-creation amendments

Added `references/agent-native/` folder with 5 files (`knowledge.md` + 4 topic files). This content is **NOT from the book** — it is our own editorial additions for agent-specific concerns (verification loops, hallucination debugging, types-as-guardrails, reviewability) that the 2021 source does not address. Every file in that folder starts with an explicit "Not from the book" warning. `SKILL.md` and `guidelines.md` both flag this folder separately in their chapter indexes.
