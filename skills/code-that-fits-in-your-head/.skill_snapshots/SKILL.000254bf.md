---
name: code-that-fits-in-your-head
description: Software-engineering heuristics based on Mark Seemann's Code That Fits in Your Head (2021), updated for agent-driven development. Use when writing or reviewing code, refactoring accidental complexity or a Big Ball of Mud, controlling technical or architectural debt in generated code, designing APIs and invariants, adding a feature through a walking skeleton and acceptance tests, debugging a defect with reproducible tests or bisection, threat-modelling endpoints and trust boundaries with STRIDE, planning a legacy or Strangler migration with rollback, or setting up a maintainable codebase. Covers decomposition and cyclomatic complexity, cohesion, encapsulation, outside-in TDD, separation of concerns, Git/review discipline, safe evolution, and troubleshooting. Not for language syntax, framework tutorials, production incident response, or performance profiling.
---

# Code That Fits in Your Head

Engineering heuristics for sustainable software, based on Mark Seemann's 2021 book and clearly labelled agent-era amendments.

## Philosophy (Why This Skill Exists)

Software development is principally a **design activity**, not construction. An agent may produce most of the text, but people still review, operate, extend, and own the resulting system. These heuristics make software sustainable: understandable, resistant to architectural erosion, and cheap to change after thousands of decisions.

Core mental model from Chapter 1:

| Metaphor | What it gets right | What it misses |
|----------|-------------------|-----------------|
| **Building a house** | Plans, structure | Software endures; there's no construction phase (compiling is free); dependencies can start anywhere |
| **Growing a garden** | Pruning, refactoring, tending | Code does not improve by itself; generated code still needs stewardship |
| **Art / craft** | Skill, mastery, situational knowledge | Doesn't scale; leaves newcomers without guidance |
| **Engineering** (the target) | Heuristics, review, sign-off, checklists | We're not there yet — physical-construction calculations don't apply |

> "The act of describing a program in unambiguous detail and the act of programming are one and the same." — Kevlin Henney

**Practical implications for a code agent:**

1. **Successful software endures.** Prefer changes that preserve clear boundaries and keep future change affordable.
2. **Complexity is the enemy, not task size.** Agents can complete changes spanning tens of thousands of lines when architecture, plan, and acceptance criteria are sound. Reject needless coupling, duplication, hidden effects, and unverifiable bulk—not large scope by itself.
3. **Heuristics, not laws.** Understand the purpose of a rule before applying or relaxing it. Project policy overrides generic formatting and workflow conventions.
4. **Verification is part of design.** Types, tests, schemas, architecture checks, observability, and explicit acceptance criteria constrain both human- and agent-written code.
5. **Code is a liability.** Generated volume is not progress. Prefer the smallest coherent design that solves the problem without accumulating debt.

See `references/foundations/` for more on sustainability, readability, and brain-limited design.

## How to Use This Skill

1. Identify the user's task (writing, reviewing, debugging, security review, setting up, etc.)
2. Read `guidelines.md` — it maps tasks and symptoms to specific reference files
3. Load only the reference files relevant to the current task (progressive disclosure)
4. Apply the rules; when in doubt, consult `references/practices-glossary/` for cross-references

## Chapter Index

| Topic | Use when... |
|-------|-------------|
| `references/foundations/` | Sustainability, readability, complexity control, and code as liability |
| `references/codebase-setup/` | Starting or inheriting a code base — git, build automation, warnings-as-errors |
| `references/outside-in-tdd/` | Writing new features test-first; walking skeleton, AAA, triangulation, devil's advocate, editing tests |
| `references/encapsulation/` | Designing types with invariants; DTO vs Domain Model, always-valid, Postel's law, parse-don't-validate |
| `references/decomposition/` | Controlling method and system complexity; cyclomatic complexity, cohesion, coupling, feature envy, fractal architecture |
| `references/api-design/` | Designing a public API; affordance, poka-yoke, CQS, hierarchy of communication, naming over comments |
| `references/separation-of-concerns/` | Adding cross-cutting concerns; Decorator pattern, logging, what to log, performance vs legibility |
| `references/teamwork-git/` | Writing commits, reviewing changes, continuous integration, collective ownership |
| `references/evolution/` | Changing running systems; feature flags, Strangler pattern, versioning, regular dependency updates, Conway's law |
| `references/troubleshooting/` | Debugging a defect; scientific method, rubber ducking, reproduce-as-test, bisection, non-deterministic defects |
| `references/security/` | Threat modelling; STRIDE (spoofing, tampering, repudiation, info disclosure, DoS, elevation) |
| `references/code-navigation/` | Onboarding to a code base; big picture, file organisation, cycles, property-based testing, behavioural code analysis |
| `references/practices-glossary/` | Looking up a named book practice and its current status |

### ⚠️ Editorial amendments (NOT from the book)

The folder below is NOT content from Seemann's book. It contains our own additions covering agent-specific concerns the 2021 book does not address. Do not attribute these files to Seemann. See `references/agent-native/knowledge.md`.

| Topic | Use when... |
|-------|-------------|
| `references/agent-native/` | Agent-specific verification integrity, hallucination and dependency grounding, executable guardrails, and accountable review |

## Workflows

Composite step-by-step processes live in `workflows/`:

| Task | Workflow |
|------|----------|
| Review a pull request / piece of code | `workflows/review-code.md` |
| Add a new feature from scratch | `workflows/add-feature-outside-in.md` |
| Investigate and fix a defect | `workflows/debug-defect.md` |
| Threat-model a new endpoint | `workflows/threat-model.md` |

See `guidelines.md` for the full routing layer (task → file, symptom → file, decision tree).
