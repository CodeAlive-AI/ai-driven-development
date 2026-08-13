# Codebase Setup Knowledge

Why the setup rules exist. The actionable material is in `rules.md` and `checklist.md`; read this only for rationale.

## Why Checklists

A checklist is a short aid to memory covered in minutes at pause points — not a compliance flowchart. The problem it solves is not lack of skill but *forgetting*: on a complex task, skipping one trivial-but-important step is almost inevitable. Externalising those steps frees working memory (human or context window) for the hard parts.

Two run modes: **read-do** (read an item, do it, move on — fits imperative lists like `checklist.md`) and **do-confirm** (do the work, then verify against the list — for auditing an existing code base, verify with evidence rather than recall).

## Why Day 1

Retrofitting discipline onto a large code base is a formidable task; on an empty one it costs almost nothing. Zero code means zero warnings to triage and no pipeline to untangle, and each new warning is fixed the moment it appears. The cost of postponing rises non-linearly — which is why the only viable path for legacy code is the gradual ratchet (`rules.md`, rule 5).

## Automated Checks as Automated Checklists

Compilers, linters, analysers, and warnings-as-errors are machine-enforced checklists that run on every build, controlling for thousands of issues no human would check line by line. Suppressing an occasional false positive is cheap; walking away from the tools is expensive. A machine-enforced rule also survives delivery pressure better than a human-held convention — see `workflows/operationalize-finding.md` for converting conventions into gates.

## Common Misconceptions

- **Myth**: Checklists are for the unskilled.
  **Reality**: Surgeons and pilots use them *because* they are experts. Skill and memory are different things.

- **Myth**: Turning on all warnings slows the team down.
  **Reality**: Seven warnings today are easier than hundreds in six months. What gets upset is the illusion that the code was maintainable without discipline.

- **Myth**: Strict checks cannot be added to a legacy code base.
  **Reality**: They can — one library, one rule, one warning category at a time (the ratchet).
