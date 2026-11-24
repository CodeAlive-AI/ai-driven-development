# Evolution Knowledge

Core concepts for changing code that other code depends on: augmenting it without breaking its callers.

## Overview

Existing code bases need new behaviour, modified behaviour, and bug fixes. Evolution focuses on the first two: take small steps that always leave the system in a consistent, deployable state — even when the work spans weeks.

## Key Concepts

### Augmenting vs. Modifying In-Place

Augmenting appends new code beside existing code; modifying in-place edits a live method while callers depend on it. Prefer side-by-side replacement when it reduces blast radius, preserves rollback, or makes verification clearer. Rule of thumb: *for any significant change, don't make it in-place; make it side-by-side.*

### Strangler Pattern

Add the new implementation next to the old, migrate callers one at a time, delete the old when nothing calls it. This theme covers method and class scale; see `patterns.md`. Replacing a subsystem with its own data or outside clients needs a designed migration path first (`pragmatic-architecture`).

### Scaffolding

A flag, a bridge method, a temporary rename or a second implementation exists only to carry a change through. Each adds a branch the reader must keep in mind, so it is introduced with an owner and a removal step, and deleted when the change lands. Details in `rules.md`.

### Semantic Versioning and Deprecation

`major.minor.patch`: major = breaking, minor = feature, patch = fix. Before removing a public API, mark it deprecated so callers get a compiler warning; delete only at the next major version. Details in `rules.md`.

### Dependency-Update Rhythm

Update packages and platform versions on a regular schedule so each step stays small. Same reasoning applies to TLS certificates, domain names, and backup-restore drills.

## Common Misconceptions

- **Myth**: Long-lived feature branches are fine if you rebase frequently.
  **Reality**: They lead to merge hell. Put the new code beside the old, unused or switched off, and merge to mainline instead.

- **Myth**: Strangler is only for replacing whole legacy systems.
  **Reality**: It works at method and class level too — whenever side-by-side migration improves verification, rollback, or blast-radius control.

- **Myth**: If the compiler doesn't complain, you can skip deprecation.
  **Reality**: External callers get no compile errors until they upgrade. Deprecate first, delete later.
