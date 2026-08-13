# Decomposition Knowledge

> **Source note:** This book-derived theme includes 2026 editorial reframing for agent-scale changes and system-level complexity. Those additions are not from Seemann.

How to divide software so changes remain local without fragmenting cohesive logic into needless indirection.

## Code Rot

Code rot is the gradual increase in change cost as branches, state, dependencies, duplication, and temporary paths accumulate. It happens locally inside methods and globally when module boundaries stop constraining change.

Metrics help expose drift, but no single metric proves maintainability. A low-complexity method can participate in a cyclic, duplicated, tightly coupled architecture.

## Cyclomatic Complexity

Cyclomatic complexity counts independent paths through a piece of code. Straight-line code starts at 1; branches and loops add paths.

Use complexity to focus review and testing, not to drive blind extraction. This skill uses **above 15** as a generic review trigger—roughly twice the book's original threshold of 7. A project may choose a stricter value. Cohesive parsers, decision tables, and generated code can justify higher values when their structure remains explicit and well verified.

## Responsibility and Cohesion

Cohesion asks whether the members of a unit belong together and change for the same reasons. Decomposition improves design only when the new boundary represents a meaningful concept.

Extracting every few lines creates navigation overhead and hides the real algorithm. Leaving validation, persistence, policy, and formatting intertwined creates a different failure. Prefer boundaries that separate reasons to change, effects, trust levels, or domain concepts.

## Interacting State

Complexity rises with the number of values and effects that interact simultaneously. Count variables, parameters, fields, mutable state, and external dependencies as diagnostic clues, but group them by concept rather than enforcing a universal item limit.

A domain type can turn several related primitives into one meaningful concept. A generic parameter bag that merely hides unrelated values does not reduce complexity.

## Pure Core, Explicit Effects

Pure functions are deterministic and have no observable side effects. They compose and test well because the same input produces the same output. Functional-core/imperative-shell design keeps decisions pure where useful and performs I/O, time, randomness, and mutation at explicit boundaries.

Purity is a means, not a mandate. The important property is that effects and their ordering are visible, constrained, and testable.

## Fractal Coherence

At every zoom level—system, service, module, type, method—the visible parts should form a comprehensible model. A reader should be able to name the main concepts and predict where a change belongs.

This requires progressive disclosure: higher levels expose stable responsibilities and lower levels contain the detail without leaking it everywhere.

## System-Level Complexity

Big Ball of Mud architecture typically appears through:

- dependency cycles and bidirectional knowledge;
- shared mutable state and implicit runtime coupling;
- duplicated domain rules;
- broad changes spanning unrelated modules;
- unstable hotspots with repeated corrective edits;
- stale feature flags, adapters, and parallel implementations;
- abstractions that have multiple incompatible meanings.

Architecture tests, dependency analysis, duplication detection, and change-history analysis can make these signals visible. They inform judgment; they do not replace it.

## Large Changes

Large changes are not necessarily complex. A systematic migration can touch thousands of files while preserving a simple transformation and clear target architecture. Conversely, a ten-line patch can add a damaging dependency cycle.

Judge large work by architecture, invariants, verification, reversibility, and whether each affected area has a clear reason to change.

## Common Misconceptions

- **"Smaller is always better."** Smaller units help only when boundaries carry meaning.
- **"A metric below threshold means good design."** Metrics miss coupling, duplication, hidden effects, and domain confusion.
- **"A large diff is automatically unreviewable."** Systematic, well-specified changes can be reviewed through their transformation, architecture, and verification evidence.
- **"More abstraction reduces complexity."** Abstraction helps only when it eliminates irrelevant detail without hiding essential behavior.
