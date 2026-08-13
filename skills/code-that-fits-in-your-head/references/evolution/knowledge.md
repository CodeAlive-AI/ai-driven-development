# Evolution Knowledge

Core concepts for changing running software safely — augmenting code without breaking it.

## Overview

Existing code bases need new behaviour, modified behaviour, and bug fixes. Evolution focuses on the first two: take small steps that always leave the system in a consistent, deployable state — even when the work spans weeks.

## Key Concepts

### Augmenting vs. Modifying In-Place

Augmenting appends new code beside existing code; modifying in-place edits a live method while callers depend on it. Prefer side-by-side replacement when it reduces blast radius, preserves rollback, or makes verification clearer. Rule of thumb: *for any significant change, don't make it in-place; make it side-by-side.*

### Feature Flags

A configuration value that hides incomplete behaviour from production users while the code ships. Decouples **deploy** from **release**. Default off in production; override on in integration tests; delete the flag once live. Details in `rules.md` and `patterns.md`.

### Strangler Pattern

Add the new implementation next to the old, migrate callers one at a time, delete the old when nothing calls it. Applies at method, class, and architectural scale. See `patterns.md`.

### Semantic Versioning and Deprecation

`major.minor.patch`: major = breaking, minor = feature, patch = fix. Before removing a public API, mark it deprecated so callers get a compiler warning; delete only at the next major version. Details in `rules.md`.

### Dependency-Update Rhythm

Update packages and platform versions on a regular schedule so each step stays small. Same reasoning applies to TLS certificates, domain names, and backup-restore drills.

### Conway's Law (as design advice)

Expect an interface to form at every team boundary; design deliberately there. The communication structure of the organisation will leak into the architecture whether or not you plan for it — so make those boundaries explicit rather than accidental. This is design advice an agent can act on (name and own the boundary), not org-restructuring advice.

## Common Misconceptions

- **Myth**: Long-lived feature branches are fine if you rebase frequently.
  **Reality**: They lead to merge hell. Hide the feature behind a flag and merge to mainline instead.

- **Myth**: Strangler is only for replacing whole legacy systems.
  **Reality**: It works at method and class level too — whenever side-by-side migration improves verification, rollback, or blast-radius control.

- **Myth**: If the compiler doesn't complain, you can skip deprecation.
  **Reality**: External callers get no compile errors until they upgrade. Deprecate first, delete later.
