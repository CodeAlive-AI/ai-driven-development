# ⚠️ Agent-Native Amendments — NOT from the book

> **This folder is not Seemann's.** The four files here are additions we wrote to cover agent-specific concerns that the 2021 book does not address. Treat them as editorial commentary, not source material.

The book *Code That Fits in Your Head* was written by Mark Seemann in 2021 for humans. It pre-dates the widespread use of code agents. Four gaps matter enough for agent-driven workflows that we added our own chapters:

| File | Agent-specific concern | Why not in the book |
|------|------------------------|---------------------|
| `verification-loops.md` | Edit → verify cycle ~100× tighter than human TDD | Book assumes human cycle times |
| `hallucination-debugging.md` | LLMs invent symbols / APIs / imports | Unknown defect class in 2021 |
| `types-as-guardrails.md` | Types + tests + specs as primary defense (not one tool among many) | Book treats these as normal heuristics |
| `reviewability.md` | Code optimised for fast human approval of agent-generated PRs | Review target has shifted |

## Authorship & status

- **Not book content.** No text here paraphrases or summarises Seemann. Where a file connects to the book, there is an explicit "Relation to the Book" section at the bottom.
- **Opinionated.** These are our working hypotheses for 2026-era agent work, not peer-reviewed practice. Treat as starting defaults, not scripture.
- **Subject to change.** The book's ideas are stable; these amendments should evolve as agent tooling evolves.

## How to use this folder

- If the user asks about a topic the book covers, reach for the book's theme folders first (`foundations/`, `decomposition/`, `encapsulation/`, etc.).
- Load files from `agent-native/` when the question is specifically about **how an agent should do something differently from what the book prescribes**.
- When quoting or citing this skill externally, do NOT attribute these four files to Seemann.

## The files at a glance

1. **verification-loops.md** — tiered feedback pyramid (types → lint → unit → integration → e2e), "verify after each edit, not at the end", antipatterns for agent work
2. **hallucination-debugging.md** — classes of agent-specific defects (invented APIs, outdated syntax, version drift), grep-before-use / read-before-edit rules
3. **types-as-guardrails.md** — the triad of types + tests + specs, agent-friendliness ranking of languages, strict-from-line-1 rule, fallback order when you can't have all three
4. **reviewability.md** — distinction from "readable code", small-diffs rule, PR description template for agents, red flags when reviewing agent PRs
