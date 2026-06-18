# Evolution Knowledge

Core concepts for changing running software safely — augmenting code without breaking it.

## Overview

Existing code bases need three kinds of change: adding new behaviour, modifying existing behaviour, and fixing bugs. Evolution focuses on the first two. The goal is to take small steps that always leave the system in a consistent, deployable state — even when the work spans weeks.

## Key Concepts

### Augmenting vs. Modifying In-Place

**Definition**: Augmenting means appending new code beside existing code. Modifying in-place means editing a live method or class while callers depend on it.

Adding a new feature is usually low-risk because most of the code is new. Changing existing behaviour is risky because callers may break while you work. Prefer side-by-side additions whenever a change will take more than a few hours.

**Rule of thumb**: *For any significant change, don't make it in-place; make it side-by-side.*

### Feature Flags

**Definition**: A boolean (or similar) configuration value that hides incomplete or not-yet-released behaviour from production users, while the code that implements it ships alongside everything else.

Feature flags decouple **deploy** (shipping code to production) from **release** (exposing behaviour to users). They let you practice Continuous Integration — merging to master multiple times per day — even on features that take weeks to finish.

**Key points**:
- Default the flag to `false` so production stays unaffected.
- Override the flag to `true` in integration tests so the new behaviour is still driven by automated tests.
- Delete the flag (and lean on the compiler to remove dead branches) once the feature is live.

### Calendar Flag

A feature flag specifically used to gate a calendar/browsing capability. In the book's REST API example, the `HomeController` conditionally adds calendar links to its response when `EnableCalendar` is configured `true`.

### Strangler Pattern

**Definition**: A side-by-side replacement technique. Add the new implementation next to the old one, migrate callers one at a time, then delete the old implementation when no callers remain. Named after the strangler fig vine that gradually overtakes a host tree.

Originally described by Martin Fowler for replacing legacy systems at architectural scale, but applies equally at method and class level.

**Three stages**:
1. Add the new method/class beside the old.
2. Migrate callers one by one, committing after each.
3. Delete the old method/class once nothing calls it.

### Method-Level Strangler

Applying the Strangler pattern to a single method (often on an interface). Add a new overload, migrate each call site, delete the original.

### Class-Level Strangler

Applying the Strangler pattern to a class. Add the new class, optionally add a temporary conversion helper, migrate callers gradually, then delete the old class and the helper.

### Semantic Versioning

**Definition**: A `major.minor.patch` version scheme. Major bumps signal breaking changes; minor bumps add features; patch bumps are bug fixes.

Even if you don't formally adopt SemVer, thinking in these terms sharpens reasoning about what changes break callers. Stable libraries stay on the same major version for years — one of the author's libraries reached `3.51.0` before a major bump.

### Advance Warning (Deprecation)

Before removing a public API, mark it deprecated (e.g. `[Obsolete]` in .NET, `@Deprecated` in Java) so callers get a compiler warning and time to migrate. Only delete deprecated APIs when releasing a new major version.

### Dependency-Update Rhythm

Package dependencies (NuGet, NPM, etc.) drift constantly. Updating rarely is painful: breaking changes pile up and the team becomes afraid to upgrade. Updating on a regular schedule keeps each step small. Same reasoning applies to language/platform versions, TLS certificates, domain names, and backup-restore drills — they expire or degrade silently, so schedule them.

### Conway's Law

> "Any organization that designs a system [...] will inevitably produce a design whose structure is a copy of the organization's communication structure."

How the team is organised shapes the code. Open offices with ad-hoc chatter tend to produce spaghetti code. Rigid hierarchies produce rigid systems. Organising work like open-source (pull requests, written reviews, asynchronous communication) tends to produce clearer architecture and preserved knowledge.

## Terminology

| Term | Definition |
|------|------------|
| Feature flag | Config boolean that hides incomplete behaviour in production |
| Strangler pattern | Side-by-side replacement: add new, migrate, delete old |
| Semantic versioning | `major.minor.patch` where major = breaking |
| Deprecation | Marking an API obsolete to warn callers before removal |
| Conway's Law | Systems mirror the communication structure of the org that builds them |

## How It Relates To

- **Continuous Integration**: Feature flags make CI possible for multi-week work — you keep merging without exposing half-finished behaviour.
- **Refactoring**: The Strangler pattern is the large-scale analog of a safe refactor. Make the change easy (side-by-side), then make the easy change.
- **API Design**: Versioning discipline matters only once other code depends on yours. Inside a monolith with no public API, breakage is cheaper.

## Common Misconceptions

- **Myth**: Long-lived feature branches are fine if you rebase frequently.
  **Reality**: They lead to merge hell. Hide the feature behind a flag and merge to master instead.

- **Myth**: Strangler is only for replacing whole legacy systems.
  **Reality**: It works at method and class level too — any time an in-place change would take longer than a few hours.

- **Myth**: If the compiler doesn't complain, you can skip deprecation.
  **Reality**: External callers get no compile errors from your changes until they upgrade. Deprecate first, delete later.

## Quick Reference

| Concept | One-Line Summary |
|---------|-----------------|
| Feature flag | Ship code dark; release later by flipping config |
| Strangler | Add new, migrate callers, delete old |
| SemVer | Major = breaking, minor = feature, patch = fix |
| Advance warning | Deprecate before delete; give callers time |
| Update rhythm | Schedule dependency updates; don't wait for pain |
| Conway's Law | Org structure leaks into the architecture |
