# Decomposition Rules

> **Source note:** This book-derived theme includes 2026 editorial reframing for agent-scale changes and system-level complexity. Those additions are not from Seemann.

Heuristics for keeping logic cohesive and preventing local complexity from growing into system-wide mud.

## Core Rules

### 1. Review Cyclomatic Complexity Above 15

Count independent paths through a method. When cyclomatic complexity exceeds 15, refactor unless the branching is cohesive, explicit, and better represented in its current form.

- Treat 15 as a review trigger, not a scientific law or automatic rejection.
- Prefer reducing nested decisions, duplicated conditions, and mixed responsibilities.
- Do not replace one understandable decision table or parser with a maze of tiny indirections merely to lower the number.
- Projects may choose a stricter threshold based on language, domain risk, and tooling.

### 2. Split by Responsibility, Not Display Geometry

Line width, screen height, and editor layout are project concerns, not universal design rules.

- Split when a method mixes responsibilities, effects, abstraction levels, or reasons to change.
- Keep cohesive transformations together even when they are long.
- Extract only when the new name and boundary reduce what a reader must understand.

### 3. Watch Interacting State

Count variables, parameters, fields, mutable state, and external dependencies when logic feels hard to follow. The smell is not a fixed count; it is interaction that cannot be explained as a few coherent concepts.

- Group values that form one domain concept into a type.
- Reduce live mutable state and push intermediate results forward.
- Do not hide unrelated values inside a parameter object solely to game a count.

### 4. Prefer Sequential Composition to Hidden Nesting

Chain transformations so the output of one becomes the input of the next. Avoid object graphs and callbacks that conceal ordering or side effects.

### 5. Favour a Pure Core and Explicit Effects

- Keep complex decisions deterministic where practical.
- Concentrate time, randomness, I/O, and mutation at explicit boundaries.
- Make effect ordering observable and testable.

### 6. Move Behaviour to the Data It Understands

If a method mainly reads another type's state and ignores its own class, consider moving it to that type or a cohesive domain service. Avoid static helper dumping grounds.

### 7. Extract Low-Coupling Sections First

Blocks that use no instance state or external effects are low-risk extraction candidates. Preserve a clear abstraction level in the caller.

### 8. Parse Into Stronger Types

Do not return a Boolean when validation also discovers structured information. Return the parsed domain value or a typed failure so callers do not repeat work.

### 9. Preserve Coherence at Every Zoom Level

Entry points, modules, types, and methods should each expose a small number of meaningful concepts. The exact number is contextual; the requirement is that a reader can name the parts and predict where a change belongs.

### 10. Check System Complexity, Not Only Methods

Tiny functions can still form a Big Ball of Mud. Review:

- dependency cycles and violated layer direction;
- fan-in/fan-out and cross-module coupling;
- duplicated business rules and competing abstractions;
- changes that spread across unrelated areas;
- churn concentrated in unstable hotspots;
- temporary flags, adapters, and migration paths that never disappear.

Use available architecture tests or static analysis where they provide reliable signals. Do not mandate a particular product or reduce architectural judgment to one score.

## Guidelines

- Prefer deletion and reuse over adding another helper or abstraction.
- Constructors should not perform hidden I/O or irreversible effects.
- Treat `static` helpers and utility modules as smells when they collect unrelated behavior.
- Use blank-line groupings as clues to responsibility boundaries, not as proof that extraction is needed.
- Refactor when a metric and the code's semantics both indicate rising change cost.

## Exceptions

- **Cohesive algorithms and generated code** may be long or branch-heavy while still being the clearest representation.
- **System edges** coordinate effects; keep the sequence explicit rather than forcing artificial purity.
- **Production emergencies** may accept temporary complexity with a recorded owner and removal condition.
- **Project policy** may set different metric thresholds; preserve the underlying goal of comprehensibility and local change.

## Quick Reference

| Rule | Summary |
|---|---|
| CC > 15 triggers review | Investigate complexity; do not refactor mechanically |
| Split by responsibility | Ignore universal screen and line limits |
| Watch interacting state | Reduce unrelated live concepts and mutation |
| Sequential composition | Keep ordering and effects explicit |
| Pure core, explicit effects | Make decisions deterministic and boundaries visible |
| Move feature-envious behavior | Put logic with the data it understands |
| Stronger parse results | Return information, not a lossy Boolean |
| Every zoom level coherent | Make parts nameable and change locations predictable |
| Check system structure | Prevent cycles, duplication, sprawl, and permanent migration debt |
