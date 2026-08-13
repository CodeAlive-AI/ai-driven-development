# Outside-In TDD Knowledge

Core concepts for test-first development: walking skeleton, vertical slice, characterisation tests, and the safety net of a test suite.

## Overview

Outside-in TDD starts tests at the system boundary (HTTP, CLI, message queue) and works inward. The first goal is a Walking Skeleton: a thin vertical slice from data ingress to data persistence that ships working software early. Tests act as a driver of change — they force the production code to justify itself.

## Key Concepts

### Walking Skeleton

A minimal, automatically deployable slice that exercises every part of the architecture without doing anything useful yet. It gives you a test suite, a build script, a deployment pipeline, and running software — all at once, and all minimal.

### Vertical Slice

A feature implemented end-to-end — from the outer boundary all the way to data persistence — using the simplest possible code at each layer. Pick the simplest feature, prefer data input so later tests have data to read, aim for the happy path first, and avoid Speculative Generality.

### Outside-In Test-Driven Development

First tests exercise the high-level boundary of the System Under Test; later tests work inward to finer-grained units as needed. Boundary tests catch combinatorial explosion at the outer shell; unit tests handle edge cases.

### Characterisation Test

A test written after the fact that describes the behaviour of existing software, usually to protect against regressions. Not true TDD (no red phase for new behaviour), but the right starting point for wizard-generated or legacy code. Assert only superficial, stable properties when behaviour is expected to change soon.

### Arrange Act Assert (AAA)

Three-phase structure: arrange preconditions, act on the SUT, assert the outcome. The blank line between phases is a heuristic. The act phase is usually the smallest.

### Triangulation

Adding more specific test cases to force the production code to become more generic. "As the tests get more specific, the code gets more generic." (Robert C. Martin).

### Safety-Net Asymmetry

The test suite lets you refactor production code with confidence. Production code has a safety net (the tests); test code does *not*. Test code can only be checked by seeing it fail against broken production code. Edit tests carefully and commit independently.

## Common Misconceptions

- **Myth**: The first vertical slice is pointless because it just saves a hard-coded value.
  **Reality**: It establishes running software, a deployment pipeline, and a test suite. Everything else is additive from there.

- **Myth**: A unit test should have exactly one assertion ("Assertion Roulette").
  **Reality**: Assertion Roulette is interleaving assert/act sections or unlabelled assertions. Multiple assertions that strengthen postconditions are fine.

- **Myth**: You must strictly TDD every class.
  **Reality**: Humble Objects (DB access, UI glue) and tool-generated code may skip TDD.

- **Myth**: You can refactor unit tests the same way as production code.
  **Reality**: Refactoring's precondition is "solid tests" — test code doesn't have that safety net.
