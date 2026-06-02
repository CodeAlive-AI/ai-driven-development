---
name: plan-mode
description: Use this skill when the user asks to plan, design, scope, estimate, or implement a feature, bug fix, refactor, migration, integration, API change, UI change, or other project modification. Enforces a planning gate before editing code — investigate project context, analyze the task, surface ambiguities, contradictions, risks, dependencies, and blockers, ask focused questions, produce an evidence-based step-by-step plan, and implement only after explicit user approval. Not for trivial one-line edits, pure questions about the codebase, or changes the user has already reviewed and approved for direct implementation.
---

# Plan Mode

Prevent premature implementation. **Understand → plan → get approval → implement → validate.** Do not skip the gate just because a change looks small.

The full protocol — investigation steps, issue classification, the question and plan templates, validation, and special cases — lives in [`PROTOCOL.md`](PROTOCOL.md). **Read it before planning or implementing.**

## Default behavior

1. Investigate project context (read-only).
2. Analyze the task: goal, current vs desired behavior, acceptance criteria, scope, edge cases.
3. Classify open issues as **ambiguity / contradiction / blocker / risk / assumption**.
4. Ask the smallest set of focused questions that unblocks planning.
5. Produce a consistent, evidence-based, step-by-step plan.
6. Wait for explicit approval.
7. Implement only the approved plan.
8. Validate, then report what was and was not checked.

## The gate (core rule)

During Plan Mode, **do not mutate the project**: no editing files, scaffolding, patches, package installs, lockfile updates, migrations, deploys, destructive scripts, or "trying an implementation" to learn the code.

**Allowed:** read files, search the repo, inspect structure, review tests / docs / configs / API contracts / schemas / migrations, run read-only or non-mutating diagnostic commands, and consult external docs when project context is insufficient.

If a tool or command might mutate state, ask first or avoid it.

## Surfacing blockers

Surface ambiguities, contradictions, and blockers **before** the plan — never bury them inside it. For each, capture: what it is, the evidence, why it matters, whether it blocks implementation, and a proposed default or resolution. If none exist, state `No hard blockers found.`

## Asking questions

Ask only **after** investigating context, and never for what the repo, tests, docs, or provided context already answer. Group related questions, give each a recommended default, and explain briefly why each answer matters. Avoid open-ended "What should I do?" questions.

## Approval

**Counts as approval:** an explicit "proceed / implement / apply / go ahead / approve", or an edited plan with a clear instruction to continue.
**Does not count:** answering one question, commenting on the plan, asking for more detail or alternatives, or "is this enough?". When approval is ambiguous, ask for a direct confirmation.

If new evidence contradicts the approved plan mid-implementation, **pause** and return to planning with what changed, the evidence, the impact, and a revised recommendation.

## Reference

Full protocol, output templates, and special handling (small tasks, urgent fixes, user-provided plans, partial context): [`PROTOCOL.md`](PROTOCOL.md).
