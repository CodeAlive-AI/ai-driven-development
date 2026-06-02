# Plan Mode — Full Protocol

This is the complete contract behind the `plan-mode` skill. The default flow is: investigate context → analyze the task → identify ambiguities, contradictions, risks, dependencies, and blockers → ask focused questions → produce a consistent step-by-step plan → wait for explicit approval → implement → validate.

Do not begin coding immediately after reading only the user prompt, and do not skip the planning gate merely because the requested change looks small.

## Contents

- [The gate: what is allowed](#the-gate-what-is-allowed)
- [Context investigation workflow](#context-investigation-workflow)
- [Task analysis workflow](#task-analysis-workflow)
- [Classifying ambiguities, contradictions, and blockers](#classifying-ambiguities-contradictions-and-blockers)
- [Question protocol](#question-protocol)
- [Planning output](#planning-output)
- [Quality bar for the plan](#quality-bar-for-the-plan)
- [Approval handling](#approval-handling)
- [Implementation after approval](#implementation-after-approval)
- [Final response after implementation](#final-response-after-implementation)
- [Gotchas](#gotchas)
- [Special handling: small tasks](#special-handling-small-tasks)
- [Special handling: urgent fixes](#special-handling-urgent-fixes)
- [Special handling: user-provided plans](#special-handling-user-provided-plans)
- [Special handling: partial context](#special-handling-partial-context)

## The gate: what is allowed

During Plan Mode, do not modify source files, tests, configs, schemas, lockfiles, generated files, infrastructure, or documentation — unless the user has explicitly asked only for a planning artifact that itself requires creating a file.

**Allowed during Plan Mode:**

- Read files.
- Search the repository.
- Inspect project structure.
- Review tests, docs, configs, API contracts, schemas, migrations, and related code.
- Run read-only or diagnostic commands when safe.
- Run existing tests or builds when they do not mutate the project in a meaningful way.
- Use external docs only when project context is insufficient or the task depends on current external behavior.

**Not allowed during Plan Mode:**

- Editing files.
- Creating scaffolding.
- Applying patches.
- Installing packages.
- Updating lockfiles.
- Running migrations.
- Deploying.
- Starting destructive scripts.
- "Trying an implementation" to learn the codebase.

If a tool or command might mutate state, ask for permission first or avoid it.

## Context investigation workflow

Before asking questions or proposing a plan, gather enough evidence to understand how the project works. Use the tools available in the environment, and prefer these steps when applicable.

1. **Establish repository state.** Identify the project root. Check whether the working tree already has user changes. Do not overwrite or reformat unrelated changes. Note uncommitted files that may affect the plan.
2. **Map the project.** Inspect top-level files and directories. Read README, architecture docs, contribution docs, package manifests, build configs, test configs, and relevant environment examples. Identify framework, language, runtime, dependency manager, test runner, linting tools, formatting rules, and deployment conventions.
3. **Find relevant feature areas.** Search for existing implementations of similar features. Locate domain models, services, controllers, handlers, components, routes, commands, jobs, migrations, tests, fixtures, and generated clients related to the request. Read adjacent code, not just the names returned by search.
4. **Understand current behavior.** Trace the request / data / control flow end to end. Identify public API boundaries, persistence boundaries, validation layers, authorization checks, error handling, telemetry, localization, feature flags, and backward-compatibility constraints. Look for existing tests that define intended behavior.
5. **Infer project conventions.** Match existing style instead of inventing new patterns. Prefer the project's existing abstractions, naming, error handling, dependency injection, transaction handling, testing style, and file organization. Do not introduce new libraries, frameworks, patterns, or infrastructure without a strong reason.
6. **Check constraints.** Identify compatibility requirements, performance constraints, security implications, data-migration needs, rollout needs, external-service contracts, and operational risks. Distinguish hard blockers from manageable risks.

## Task analysis workflow

After context investigation, analyze the user's request. Build an understanding of:

- The user-visible goal.
- The current behavior.
- The desired behavior.
- Acceptance criteria, explicit or inferred.
- In-scope changes.
- Out-of-scope changes.
- Affected users, APIs, data, workflows, and systems.
- Edge cases.
- Failure modes.
- Testing strategy.
- Rollback or migration concerns, when relevant.

Do not expose raw private reasoning. Share concise findings, evidence, assumptions, and decisions.

## Classifying ambiguities, contradictions, and blockers

Classify every open issue using these definitions:

- **Ambiguity** — more than one plausible interpretation exists, and the choice changes the implementation.
- **Contradiction** — the user request, docs, tests, code, API contracts, or business rules conflict.
- **Blocker** — safe planning or implementation cannot proceed without a decision, credential, dependency, missing artifact, environment access, or architectural choice.
- **Risk** — implementation can proceed, but the plan needs mitigation or validation.
- **Assumption** — a reasonable default chosen because the issue is minor or non-blocking.

For each issue, capture: what it is, the evidence from the project or user request, why it matters, whether it blocks implementation, and the proposed default or resolution.

Do not bury blockers inside a long plan. Surface them before the plan.

## Question protocol

Ask questions only after investigating the project context. Do not ask the user for information that can be discovered from the repository, files, tests, logs, docs, or provided context.

When questions are needed:

- Ask the smallest set of questions that unblocks planning.
- Prioritize decisions that materially affect architecture, data model, public behavior, compatibility, or user experience.
- Group related questions.
- Provide a recommended default for each question when possible.
- Explain briefly why each answer matters.
- Avoid open-ended "What should I do?" questions.

Default question format:

```markdown
I found [short context summary]. These decisions affect the implementation:

1. [Question]
   - Why it matters: [impact]
   - Recommended default: [default]

2. [Question]
   - Why it matters: [impact]
   - Recommended default: [default]
```

If the user explicitly says to proceed without questions, proceed only when no hard blocker exists, and state the assumptions in the plan.

## Planning output

After investigation and any necessary questions, produce a plan using this structure.

```markdown
# Feature Plan: [short title]

## Understanding

[One concise paragraph describing the requested change and intended outcome.]

## Context findings

- [Fact about current implementation, with file / path / function / test reference when possible.]
- [Fact about project convention.]
- [Fact about affected behavior.]

## Ambiguities, contradictions, and blockers

| Type | Item | Evidence | Impact | Resolution |
|---|---|---|---|---|
| Ambiguity / Contradiction / Blocker / Risk / Assumption | [item] | [evidence] | [impact] | [question, default, or mitigation] |

If there are none, explicitly say: `No hard blockers found.`

## Proposed implementation plan

1. [Small, concrete, sequential step.]
   - Files/areas: [likely files, modules, or layers]
   - Reason: [why this step is needed]
   - Notes: [edge cases, constraints, or conventions]

2. [Next step.]
   - Files/areas: [...]
   - Reason: [...]
   - Notes: [...]

## Test and validation plan

- Unit tests: [specific tests to add or update]
- Integration / API / UI tests: [specific tests if applicable]
- Regression checks: [existing tests, build, lint, typecheck]
- Manual checks: [only if automated validation is not enough]

## Rollout, migration, and compatibility

- Data / schema changes: [none or details]
- Backward compatibility: [impact]
- Feature flags / config: [needed or not]
- Rollback considerations: [if relevant]

## Approval gate

I will not implement until you approve this plan. Please reply with approval or changes.
```

## Quality bar for the plan

A good plan must be:

- **Evidence-based** — grounded in inspected project context.
- **Sequential** — each step depends logically on prior steps.
- **Specific** — names likely files, modules, interfaces, tests, or layers.
- **Minimal** — solves the requested problem without unrelated refactors.
- **Consistent** — does not contradict discovered code, docs, tests, or user requirements.
- **Testable** — includes concrete validation steps.
- **Safe** — identifies blockers, migration risks, compatibility issues, and user-data implications.
- **Reversible where possible** — avoids unnecessary irreversible changes.
- **Convention-aligned** — follows existing project patterns.

Reject or revise your own plan if it:

- Relies on invented project structure.
- Ignores failing or missing tests.
- Introduces a new abstraction without showing why existing ones are insufficient.
- Hides a blocker as an assumption.
- Cannot be validated.
- Changes public behavior without identifying compatibility impact.
- Includes implementation before approval.

## Approval handling

Treat these as approval:

- The user explicitly says to proceed, implement, apply, go ahead, approve, or similar.
- The user modifies the plan and clearly asks to continue with the modified version.

Do not treat these as approval:

- The user answers only one planning question.
- The user comments on the plan but does not approve implementation.
- The user asks for more detail, alternatives, or estimates.
- The user asks "is this enough?" or "what do you think?".

When approval is ambiguous, ask for a direct confirmation.

## Implementation after approval

After approval:

1. Re-check the working tree and the relevant files.
2. Implement in small, coherent changes.
3. Preserve unrelated user changes.
4. Follow the approved plan.
5. If new evidence contradicts the approved plan, pause implementation and return to Plan Mode with: what changed, the evidence, the impact, and a revised recommendation.
6. Add or update tests according to the validation plan.
7. Run the most relevant tests first, then broader checks as appropriate.
8. Fix failures caused by the change.
9. Do not silently ignore validation failures.
10. Summarize what changed and how it was validated.

## Final response after implementation

Use this structure:

```markdown
Implemented the approved plan.

## Changed

- [File/module]: [what changed]
- [File/module]: [what changed]

## Validation

- `[command]` — passed
- `[command]` — failed: [reason and impact]

## Notes

- [Known limitation, follow-up, migration note, or none.]
```

If implementation was blocked, use:

```markdown
Implementation is blocked.

## What blocks it

[Clear description.]

## Evidence

[What was found.]

## Needed decision or action

[What the user or project owner must provide.]

## Safe next step

[Recommended next action.]
```

## Gotchas

- Do not begin coding immediately after reading only the user prompt.
- Do not ask broad questions before inspecting available project context.
- Do not assume a missing requirement is harmless when it affects data, security, public API, or UX.
- Do not use the plan as a place to hide uncertainty.
- Do not claim the project uses a pattern unless you found evidence.
- Do not add dependencies unless the project already uses them or the plan justifies them.
- Do not replace existing conventions with generic best practices.
- Do not modify unrelated code while implementing.
- Do not skip tests because the change looks obvious.
- Do not mark work complete if validation was not run — say what was and was not validated.

## Special handling: small tasks

For a truly small, low-risk task, keep the plan concise but still follow the gate.

Minimum acceptable compact plan:

```markdown
I inspected [files/areas]. The change appears limited to [scope].

No hard blockers found.

Plan:
1. [Step]
2. [Step]
3. Validate with [test/check].

I will not implement until you approve.
```

Do not use the compact plan when the task touches authentication, authorization, payments, data migrations, public APIs, concurrency, infrastructure, security, privacy, or irreversible operations.

## Special handling: urgent fixes

Urgency does not remove the planning gate; it changes the plan's shape.

- Investigate the failure path first.
- Identify the smallest safe mitigation.
- Separate the immediate hotfix from follow-up hardening.
- Include rollback and validation.
- Ask only blocker questions.
- Do not perform deployment or production operations without explicit approval.

## Special handling: user-provided plans

If the user provides their own plan:

1. Validate it against project context.
2. Identify missing steps, contradictions, risks, and blockers.
3. Revise it into a consistent, executable plan.
4. Ask for approval before implementation.

Do not blindly execute a user-provided plan if project evidence contradicts it.

## Special handling: partial context

If the repository, files, or environment are unavailable:

- State what context is missing.
- Do not invent project-specific details.
- Produce a context-limited plan with explicit assumptions.
- Ask for the minimum missing artifacts needed to produce a safe implementation plan.

Use this wording:

```markdown
I cannot fully validate the plan against the project because [missing context]. Based on the available information, here is a provisional plan. Treat it as unapproved until the missing context is checked.
```
