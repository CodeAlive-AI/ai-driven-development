# Troubleshooting Knowledge

> **Source note:** This book-derived theme includes 2026 editorial reframing for durable agent debugging state. Agent-specific additions are not from Seemann.

Core concepts and foundational understanding for debugging defects methodically.

## Overview

Troubleshooting is the disciplined activity of *understanding* why code misbehaves, as opposed to "programming by coincidence" where changes continue until the symptom disappears. Scientific hypotheses, simplification, executable reproduction, and bisection prevent speculative fixes from becoming debt.

## Key Concepts

### Scientific Method Applied to Debugging

**Definition**: A disciplined loop of hypothesis, experiment, and comparison applied to a defect.

When a problem manifests, most people jump straight into "fix it" mode. Instead, your first priority should be to understand the problem. Adopt a lightweight version of the scientific method:

- Make a prediction (the hypothesis), such as "if I call this function, the return value will be 42."
- Perform the experiment.
- Compare the outcome to the prediction. Repeat until you understand what is going on.

The hypothesis must be falsifiable. The distinction from "programming by coincidence" is that the goal of the cycle is understanding, not mere symptom removal. A typical experiment is a unit test with the prediction "when I run it, it will fail."

### Simplification

**Definition**: Removing code until only the defect remains, rather than adding more code to paper over it.

The instinctive reaction to a problem is to add code to special-case it. The unspoken assumption is that the system "works" and the problem is just an aberration. More often, the problem is a manifestation of an underlying implementation error, and simplifying (or deleting) code resolves it. Ask: "Can I solve this by deleting code?"

### Externalizing the Problem

**Definition**: Recording the problem, evidence, attempted explanations, and open question clearly enough for another person or agent to evaluate.

Rubber ducking is one human form of this technique. For an agent, durable notes prevent repeated failed attempts and make escalation useful after a long run or context change.

Stop repeating experiments when they produce no new evidence. Revise the hypothesis, instrumentation, or system model instead.

### Reproduce Defects as Tests

**Definition**: Before fixing a bug, encode the hypothesis as an automated test that is expected to fail.

If your hypothesis about a defect is correct, you can design an experiment: a test that should fail given the current code. Running it either validates the hypothesis (test fails as predicted) or refutes it (test passes, so revise the hypothesis). When the failing test exists, fixing the code turns it green and leaves a permanent regression guard. The hard part of addressing a defect is usually *understanding and reproducing* it; making the test pass is typically the easy part.

### Slow Tests

**Definition**: Tests (commonly integration tests touching a database or external service) that are too slow to run in the inner TDD loop.

Feedback must be fast enough that it is used reliably, but no universal duration applies. Separate focused checks from comprehensive database, HTTP, filesystem, migration, or system verification. Keep slower high-value tests and run them at the appropriate checkpoint or gate.

### Non-deterministic Defects

**Definition**: Defects whose manifestation depends on uncontrolled inputs: thread scheduling, system clock, random values, external state, locale, etc.

Some defects resist deterministic reproduction — race conditions are the canonical example. The preferred fallback is a non-deterministic test that runs the suspect scenario on a loop for a fixed timeout (e.g. 30 seconds) and asserts on the result. Such a test can produce a false negative, but is strictly better than no coverage. These tests also belong in the slow, second-stage tier.

**Test failure modes to weigh**:
- **False positive** — test reports a failure when there is none. Introduces noise; people stop trusting the suite.
- **False negative** — test fails to catch a real bug. Reduces trust, but at least a failing suite still signals a real problem.

### Bisection

**Definition**: Binary search over a search space (code, history) to localize the cause of a defect.

The general procedure:
1. Find a way to detect or reproduce the problem.
2. Remove half the code (or history).
3. If the problem is still present, recurse on the remaining half. If it vanishes, recurse on the other half.
4. Continue until the offending piece is small enough to understand.

Applied to git history, this is `git bisect`: given a known-good commit and a known-bad commit, git checks out the midpoint and asks whether the defect is present. The answer halves the range each iteration (log2 N steps).

## Terminology

| Term | Definition |
|------|------------|
| Programming by coincidence | Trying random fixes until the symptom disappears, without understanding why. |
| Hypothesis | A falsifiable prediction about what the code does. |
| Rubber ducking | Explaining a problem out loud to force comprehension. |
| Regression test | A test that reproduces a fixed defect to prevent it from returning. |
| Humble Object | An object so simple (cyclomatic complexity 1) it is considered not worth unit-testing. |
| False positive | A passing test erroneously reported as failing. |
| False negative | A failing test erroneously reported as passing (bug not caught). |
| Minimal working example | The smallest piece of code that still reproduces the problem. |

## How It Relates To

- **Test-driven development**: Reproducing defects as tests extends the Red-Green-Refactor loop to bug fixing.
- **Git discipline**: Small, well-named commits make `git bisect` effective. Large messy commits make bisection painful.
- **Simple design**: Simpler code has fewer defects and is easier to reason about when one appears.
- **Dependency injection**: Injecting clocks, random sources, and other non-determinism is what makes isolate-then-fix possible for flaky behavior.

## Common Misconceptions

- **Myth**: The first step in troubleshooting is firing up the debugger.
  **Reality**: The debugger is a specialized tool. The scientific method, automated tests, and bisection solve more problems, work in production where debuggers cannot, and leave regression coverage behind.

- **Myth**: Flaky tests are better than no tests only if they are deterministic.
  **Reality**: A non-deterministic test that occasionally misses a race condition is still better than no coverage. What you must avoid are *false positives* — tests that fail for no real reason — because they destroy trust in the suite.

- **Myth**: Bisection only works if you have tests.
  **Reality**: `git bisect` can run automatically if you have a test, but works just as well in interactive mode where you manually mark each checkout as good or bad.

## Quick Reference

| Concept | One-Line Summary |
|---------|-----------------|
| Scientific method | Hypothesize, experiment, compare — repeat until you understand. |
| Simplify | Try deleting code before adding more. |
| Rubber ducking | Explaining the problem often reveals it. |
| Reproduce-as-test | A failing test is the best specification of a bug. |
| Ten-second budget | Inner-loop test suites must stay fast; slow tests go to stage two. |
| Non-determinism | Loop the test under a timeout; accept false negatives, reject false positives. |
| git bisect | Binary search over commit history to pinpoint the breaking change. |
