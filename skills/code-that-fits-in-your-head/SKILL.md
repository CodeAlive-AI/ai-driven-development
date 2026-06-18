---
name: code-that-fits-in-your-head
description: Software engineering heuristics from Mark Seemann's book Code That Fits in Your Head (2021). Use when writing new code, reviewing code, refactoring, designing APIs, handling validation and invariants, writing unit tests, debugging defects, performing security review (STRIDE), or setting up a new code base. Covers decomposition (cyclomatic complexity, 80/24 rule, cohesion, fractal architecture), encapsulation (invariants, parse-don't-validate, Postel's law), outside-in TDD (walking skeleton, AAA, triangulation, devil's advocate), API design (affordance, poka-yoke, CQS), git/PR hygiene (50/72 commits, small commits, code review), feature flags, Strangler pattern, bisection debugging, logging with decorators, and STRIDE threat modelling. Not for language-specific syntax, framework tutorials, production incident response, or performance profiling.
---

# Code That Fits in Your Head

Engineering heuristics for sustainable software, based on Mark Seemann's 2021 book.

## Philosophy (Why This Skill Exists)

Software development is principally a **design activity**, not construction. Code is written by people, read by people, and endures far longer than any "project". These heuristics are rules of thumb (not scientific laws) that make software sustainable — that is, cheap to change and resilient to the next 10,000 small decisions.

Core mental model from Chapter 1:

| Metaphor | What it gets right | What it misses |
|----------|-------------------|-----------------|
| **Building a house** | Plans, structure | Software endures; there's no construction phase (compiling is free); dependencies can start anywhere |
| **Growing a garden** | Pruning, refactoring, tending | Code doesn't grow by itself — someone writes it |
| **Art / craft** | Skill, mastery, situational knowledge | Doesn't scale; leaves newcomers without guidance |
| **Engineering** (the target) | Heuristics, review, sign-off, checklists | We're not there yet — physical-construction calculations don't apply |

> "The act of describing a program in unambiguous detail and the act of programming are one and the same." — Kevlin Henney

**Practical implications for a code agent:**

1. **Successful software endures.** Prefer changes that don't lock the future; avoid "finish-and-forget" thinking.
2. **Heuristics, not laws.** Every rule in this skill has context. Understand *why* before deviating. When the user asks to break a rule, check if their reason addresses the rule's rationale.
3. **Design = typing code.** Code review, naming, function size, and API shape are the primary design surfaces.
4. **The future is unevenly distributed.** Techniques described here (CI, tests, checklists, STRIDE) exist today — adopt them per-context rather than arguing for greenfield-only use.

See `references/foundations/` for more on sustainability, readability, and brain-limited design.

## How to Use This Skill

1. Identify the user's task (writing, reviewing, debugging, security review, setting up, etc.)
2. Read `guidelines.md` — it maps tasks and symptoms to specific reference files
3. Load only the reference files relevant to the current task (progressive disclosure)
4. Apply the rules; when in doubt, consult `references/practices-glossary/` for cross-references

## Chapter Index

| Topic | Use when... |
|-------|-------------|
| `references/foundations/` | Understanding why code should fit in head; sustainability, readability, humane code |
| `references/codebase-setup/` | Starting or inheriting a code base — git, build automation, warnings-as-errors |
| `references/outside-in-tdd/` | Writing new features test-first; walking skeleton, AAA, triangulation, devil's advocate, editing tests |
| `references/encapsulation/` | Designing types with invariants; DTO vs Domain Model, always-valid, Postel's law, parse-don't-validate |
| `references/decomposition/` | Splitting a function/class; cyclomatic complexity, 80/24 rule, cohesion, feature envy, fractal architecture, composition |
| `references/api-design/` | Designing a public API; affordance, poka-yoke, CQS, hierarchy of communication, naming over comments |
| `references/separation-of-concerns/` | Adding cross-cutting concerns; Decorator pattern, logging, what to log, performance vs legibility |
| `references/teamwork-git/` | Writing commits, reviewing PRs; 50/72 rule, small commits, continuous integration, pair/mob, code review |
| `references/evolution/` | Changing running systems; feature flags, Strangler pattern, versioning, regular dependency updates, Conway's law |
| `references/troubleshooting/` | Debugging a defect; scientific method, rubber ducking, reproduce-as-test, bisection, non-deterministic defects |
| `references/security/` | Threat modelling; STRIDE (spoofing, tampering, repudiation, info disclosure, DoS, elevation) |
| `references/code-navigation/` | Onboarding to a code base; big picture, file organisation, cycles, property-based testing, behavioural code analysis |
| `references/practices-glossary/` | Looking up a named practice by name (28 entries: 50/72, 80/24, AAA, Bisection, CQS, Strangler, etc.) |

### ⚠️ Editorial amendments (NOT from the book)

The folder below is NOT content from Seemann's book. It contains our own additions covering agent-specific concerns the 2021 book does not address. Do not attribute these files to Seemann. See `references/agent-native/knowledge.md`.

| Topic | Use when... |
|-------|-------------|
| `references/agent-native/` | The question is specifically about how a code agent should do something differently from Seemann's 2021 guidance — tight verification loops, hallucination debugging, strict types as primary guardrails, reviewable vs readable code |

## Workflows

Composite step-by-step processes live in `workflows/`:

| Task | Workflow |
|------|----------|
| Review a pull request / piece of code | `workflows/review-code.md` |
| Add a new feature from scratch | `workflows/add-feature-outside-in.md` |
| Investigate and fix a defect | `workflows/debug-defect.md` |
| Threat-model a new endpoint | `workflows/threat-model.md` |

See `guidelines.md` for the full routing layer (task → file, symptom → file, decision tree).
