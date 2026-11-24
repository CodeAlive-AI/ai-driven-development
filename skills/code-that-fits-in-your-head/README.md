# code-that-fits-in-your-head

Cross-agent skill for the shape of code inside one code base: keeping each unit small enough to hold in mind and inexpensive to change. It helps prevent accidental complexity, architectural erosion into a Big Ball of Mud, and silent technical-debt accumulation—especially when coding agents can generate code faster than people can review and own it.

The skill is based on Mark Seemann's *Code That Fits in Your Head: Heuristics for Software Engineering* (2021), with clearly labelled editorial amendments for agent-driven development.

Use it when a task is about:

- designing complex code, APIs, domain types, validation boundaries, and invariants
- decomposing tangled functions, classes, workflows, or subsystems
- reviewing code for readability, cohesion, coupling, encapsulation, and testability
- building a feature as a thin slice from the boundary inward
- debugging defects by hypothesis, reproduction, and bisection
- replacing a method or class side by side (Strangler) and removing the scaffolding afterwards
- reviewing agent-generated changes for architectural fit, dependency provenance, and new debt
- measuring complexity, cycles, duplication and hotspots, and turning a recurring finding into a lint or CI gate

Large tasks are not rejected because they are large. Agents can successfully implement changes spanning tens of thousands of lines when the work has coherent architecture, a clear plan, trustworthy acceptance criteria, and verifiable checkpoints. The skill targets unstructured complexity and unverifiable change—not scope by itself.

## What It Leaves to Other Skills

A question belongs here when it is answered by reading the code. The rest is handed on:

| Question | Skill |
|---|---|
| Which tests to write and at which level, TDD, a flaky or slow test, whether a task is done | `pragmatic-verification` |
| Which design to choose, where state lives, retries and partial failure, schema and contract migration, rollout and rollback, threat modelling | `pragmatic-architecture` |
| Which problem to solve, build or buy, causes outside the code, delivery and operations | `fpf-problem-solving` |

Test-driven development is a large part of Seemann's book. This skill does not prescribe it: the order of tests and code is left to `pragmatic-verification`. What stays from it is about code, not tests: build from the boundary inward in thin slices, and treat code that is hard to check as a design smell.

## How It Works

`SKILL.md` contains the trigger description and top-level index. `guidelines.md` is the routing layer: it maps tasks, symptoms, and named practices to the smallest useful reference files.

Code examples are C#-first; every rule and the tooling tables are language-neutral.

The skill uses progressive disclosure. Load one primary file and at most one or two secondary files for the current task instead of reading the whole skill. When a rule proves repeatedly useful in a repository, operationalize it (`workflows/operationalize-finding.md`) so it persists as a gate and in project agent instructions.

## Structure

```text
SKILL.md                 # Trigger, philosophy, chapter index
guidelines.md            # Task/symptom/practice routing
workflows/               # Step-by-step workflows for common engineering tasks
references/              # Focused reference packs by theme
references/tooling/      # Executable measurement commands (complexity, cycles, dead code, …)
```

Core themes include decomposition, encapsulation, API design, separation of concerns, teamwork and Git discipline, code evolution, troubleshooting, code navigation, and measurement tooling. Workflows cover review, adding a feature, debugging, and operationalizing findings into gates.

## Source Boundaries

Most reference folders summarize or operationalize ideas from Seemann's book. The `references/agent-native/` folder is different: it contains local editorial additions for coding agents—hallucination and dependency grounding, executable guardrails, and accountable review. Editorial amendments placed in book-derived themes are explicitly marked. Do not attribute them to Seemann.

## Governing Principles

- Prefer simple, cohesive designs over clever or speculative abstractions.
- Keep dependencies, side effects, and ownership boundaries explicit.
- Judge complexity across the system, not only inside individual methods.
- Never weaken tests, types, CI, or security controls merely to make generated code pass.
- Treat generated code volume, merge rate, and approval speed as poor proxies for maintainability.
