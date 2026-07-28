# code-that-fits-in-your-head

Cross-agent skill for keeping software understandable and inexpensive to change. It helps prevent accidental complexity, architectural erosion into a Big Ball of Mud, and silent technical-debt accumulation—especially when coding agents can generate code faster than people can review and own it.

The skill is based on Mark Seemann's *Code That Fits in Your Head: Heuristics for Software Engineering* (2021), with clearly labelled editorial amendments for agent-driven development.

Use it when a task is about:

- designing complex code, APIs, domain types, validation boundaries, and invariants
- decomposing tangled functions, classes, workflows, or subsystems
- reviewing code for readability, cohesion, coupling, encapsulation, and testability
- adding features outside-in with tests and a walking skeleton
- debugging defects with reproducible tests, bisection, and tighter verification loops
- evolving legacy systems with feature flags, Strangler-style migration, reversible stages, and explicit verification
- threat-modelling endpoints or services with STRIDE
- reviewing agent-generated changes for architectural fit, verification integrity, dependency provenance, and new debt

Large tasks are not rejected because they are large. Agents can successfully implement changes spanning tens of thousands of lines when the work has coherent architecture, a clear plan, trustworthy acceptance criteria, and verifiable checkpoints. The skill targets unstructured complexity and unverifiable change—not scope by itself.

## How It Works

`SKILL.md` contains the trigger description and top-level index. `guidelines.md` is the routing layer: it maps tasks, symptoms, code elements, and named practices to the smallest useful reference files.

The skill uses progressive disclosure. Load one primary file and at most one or two secondary files for the current task instead of reading the whole skill.

## Structure

```text
SKILL.md                 # Trigger, philosophy, chapter index
guidelines.md            # Task/symptom/practice routing
workflows/               # Step-by-step workflows for common engineering tasks
references/              # Focused reference packs by theme
```

Core themes include decomposition, encapsulation, API design, outside-in TDD, separation of concerns, teamwork and Git discipline, software evolution, troubleshooting, and security.

## Source Boundaries

Most reference folders summarize or operationalize ideas from Seemann's book. The `references/agent-native/` folder is different: it contains local editorial additions for coding agents—verification integrity, hallucination and dependency grounding, executable guardrails, and accountable review. Editorial amendments placed in book-derived themes are explicitly marked. Do not attribute them to Seemann.

## Governing Principles

- Prefer simple, cohesive designs over clever or speculative abstractions.
- Keep dependencies, side effects, and ownership boundaries explicit.
- Judge complexity across the system, not only inside individual methods.
- Require verification proportional to risk and independent of the implementation where it matters.
- Never weaken tests, types, CI, or security controls merely to make generated code pass.
- Treat generated code volume, merge rate, and approval speed as poor proxies for maintainability.
