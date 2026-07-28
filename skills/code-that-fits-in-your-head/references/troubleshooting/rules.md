# Troubleshooting Rules

> **Source note:** This book-derived theme includes 2026 editorial reframing for durable agent debugging state. Agent-specific additions are not from Seemann.

Rules for diagnosing defects without accumulating speculative fixes and technical debt.

## Core Rules

### 1. Understand Before You Fix

Do not make random edits until the symptom disappears. Establish what is happening, why the current behavior follows from the system, and which evidence would disprove the explanation.

- The first useful outcome may be knowledge rather than a green build.
- Separate diagnosis from implementation when premature editing would destroy evidence.
- Escalate when required context or authority is missing; do not guess across an unknown boundary.

### 2. Record a Falsifiable Hypothesis

Write the prediction before the experiment. Include:

- suspected cause;
- expected observation if it is true;
- observation that would falsify it;
- smallest relevant experiment;
- result and next conclusion.

Keep this as durable state during long agent runs so failed approaches are not repeated after context changes.

### 3. Reproduce the Defect With an Executable Check

Prefer an automated regression test, contract check, or deterministic script that fails for the defect and passes after the fix.

- If the check passes before the fix, revise the hypothesis.
- If deterministic reproduction is impossible, preserve the strongest observable signal and document its limitations.
- For material defects, prefer an oracle independent of the proposed implementation.

### 4. Externalize Reasoning Before Escalation

Summarize the problem, evidence, attempted explanations, and open question before asking a human or another agent. This often exposes a missing assumption and makes escalation useful. Rubber-ducking is one human technique, not a required mechanism.

### 5. Try Removing Complexity Before Adding a Special Case

Ask whether deletion, consolidation, or restoring an invariant removes the defect. A new branch for every symptom often converts a local bug into permanent debt.

- Look for duplicated rules, stale compatibility paths, and abstractions that obscure the real behavior.
- Do not delete necessary behavior merely to make a test pass.

### 6. Keep Feedback Fast Enough to Use Reliably

There is no universal ten-second limit. Separate focused and comprehensive checks so developers and agents can run the relevant feedback often without discarding slower high-value tests.

- Maintain a focused inner loop for the touched behavior.
- Run complete required gates before acceptance.
- Optimize slow verification when its delay causes systematic skipping, not merely because it exceeds a stopwatch target.
- Keep the command suitable for bisection or classification as cheap and deterministic as practical.

### 7. Isolate Non-Determinism Before Fixing It

Control threading, clock, randomness, locale, external state, and environment before changing production logic.

- Inject clocks and random sources.
- Record seeds and relevant environment.
- Use disposable fixtures for external state.
- Stress concurrency with bounded, observable experiments.
- Treat flaky false positives as corrosive; repair or quarantine them with an owner.

### 8. Use History When the Behavior Changed

Use `git bisect`, blame, logs, and prior incidents when a known-good and known-bad state exist. Small coherent commits improve diagnosis, but a systematic large commit can also be useful when its transformation is explicit.

### 9. Stop Repeating Experiments Without New Evidence

After several attempts that do not change the evidence, stop editing and revise the hypothesis, instrumentation, or system model. Repeated mutation without new information is agentic thrashing, not debugging.

## Guidelines

- Prefer observable experiments over debugger-only conclusions that leave no regression guard.
- Preserve logs, failing inputs, versions, and environment needed to reproduce the issue.
- Use stronger domain types to prevent silent argument swaps and invalid states.
- When bisection identifies the cause, still add the appropriate regression guard.
- State explicitly when the correct action is no code change.

## Exceptions

- **Exploration without a harness** may begin with REPL commands or ad-hoc scripts; turn a stable reproduction into a durable check before accepting the fix.
- **Rare races** may require architectural containment or production instrumentation rather than a deterministic local test.
- **Emergency mitigation** may precede full diagnosis when harm is ongoing; preserve evidence and perform root-cause analysis afterwards.

## Quick Reference

| Rule | Summary |
|---|---|
| Understand first | Do not mutate the system without a causal model |
| Falsifiable hypothesis | Predict before experimenting and record the result |
| Executable reproduction | Preserve a failing signal and regression guard |
| Externalize reasoning | Make evidence and unknowns durable before escalation |
| Remove complexity first | Avoid special-case debt when deletion restores the invariant |
| Usable feedback | Separate focused and complete gates; no universal stopwatch |
| Isolate nondeterminism | Control clocks, randomness, concurrency, and state |
| Use history | Bisect changed behavior with a reliable classifier |
| No evidence-free loops | Revise the model instead of repeating edits |
