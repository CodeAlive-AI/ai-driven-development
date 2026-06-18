# code-that-fits-in-your-head

Codex skill for designing, reviewing, refactoring, and evolving complex code so it stays small enough to understand, change, and verify.

The skill is based on Mark Seemann's *Code That Fits in Your Head: Heuristics for Software Engineering* (2021). It turns the book's engineering heuristics into agent-readable routing, workflows, and focused reference files for everyday software design work.

Use it when a task is about:

- designing complex code, APIs, domain types, validation boundaries, and invariants
- decomposing large functions, classes, workflows, or subsystems
- reviewing code for readability, cohesion, coupling, encapsulation, and testability
- adding features outside-in with tests and a walking skeleton
- debugging defects with reproducible tests, bisection, and tighter verification loops
- evolving legacy systems with feature flags, Strangler-style migration, and small safe changes
- threat-modelling endpoints or services with STRIDE

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

Core themes include decomposition, encapsulation, API design, outside-in TDD, separation of concerns, teamwork and git hygiene, software evolution, troubleshooting, security, and codebase navigation.

## Source Boundaries

Most reference folders summarize or operationalize ideas from Seemann's book. The `references/agent-native/` folder is different: it contains local editorial additions for AI coding agents, such as verification loops, hallucination debugging, stricter type guardrails, and reviewable agent-generated changes. Do not attribute those files to the book.

