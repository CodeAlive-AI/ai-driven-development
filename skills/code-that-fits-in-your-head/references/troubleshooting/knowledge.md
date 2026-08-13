# Troubleshooting Knowledge

> **Source note:** This book-derived theme includes 2026 editorial reframing for durable agent debugging state. Agent-specific additions are not from Seemann.

Core concepts for debugging defects methodically.

## Overview

Troubleshooting is the disciplined activity of *understanding* why code misbehaves, as opposed to "programming by coincidence" where changes continue until the symptom disappears. Scientific hypotheses, simplification, executable reproduction, and bisection prevent speculative fixes from becoming debt.

## Key Concepts

### Scientific Method Applied to Debugging

A loop of falsifiable hypothesis, experiment, and comparison. First priority is understanding, not symptom removal. A typical experiment is a unit test with the prediction "when I run it, it will fail." Compare outcome to prediction; repeat until you understand what is going on.

### Simplification

Remove code until only the defect remains, rather than adding special cases. Ask: "Can I solve this by deleting code?" More often the problem is an underlying implementation error, not an aberration of a "working" system.

### Externalizing the Problem

Record the problem, evidence, attempted explanations, and open questions clearly enough for another person or agent to evaluate. For an agent, durable notes prevent repeated failed attempts and make escalation useful after a long run or context change. Stop repeating experiments that produce no new evidence.

### Reproduce Defects as Tests

Before fixing, encode the hypothesis as an automated test expected to fail. A failing test validates the hypothesis; a passing one refutes it. Once fixed, the test is a permanent regression guard. Understanding and reproducing is usually the hard part; making the test pass is typically the easy part.

### Slow Tests

Tests (commonly integration tests touching a database or external service) that are too slow for the inner loop. Keep a fast inner loop for the touched behaviour (default target: seconds, project-configurable); keep comprehensive gates separate and run them at the appropriate checkpoint. There is no universal stopwatch — separate focused checks from high-value slow ones rather than discarding either.

### Non-deterministic Defects

Defects that depend on uncontrolled inputs (scheduling, clock, random, external state). Preferred fallback: a non-deterministic test that loops the scenario under a fixed timeout. Accept false negatives; reject false positives (noise that destroys suite trust). These tests belong in the slow, second-stage tier.

### Bisection

Binary search over code or history to localise a cause. Applied to git history: `git bisect` given a known-good and known-bad commit halves the range each iteration.

## Common Misconceptions

- **Myth**: The first step in troubleshooting is firing up the debugger.
  **Reality**: The scientific method, automated tests, and bisection solve more problems, work where debuggers cannot, and leave regression coverage behind.

- **Myth**: Flaky tests are better than no tests only if they are deterministic.
  **Reality**: A non-deterministic test that occasionally misses a race is still better than no coverage. What you must avoid are *false positives* that destroy trust.

- **Myth**: Bisection only works if you have tests.
  **Reality**: `git bisect` works in interactive mode where you manually mark each checkout good or bad.
