# Code Navigation Knowledge

Core concepts for onboarding to an unfamiliar code base when the reader is an agent: progressive maps, tests as documentation, cycles, and history-based hotspot detection.

## Overview

When you land on a new code base, build a mental model without drowning in detail. Start at the entry point / composition root, zoom out to see the shape of the system, then zoom in only where the task demands it. The file tree is a poor map; the tests and the composition root are good ones. Navigate with search, imports, tests, and git history — not by reading whole directories.

## Key Concepts

### Start at the Entry Point

The framework entry point (`Main`, `Startup`, `program.ts`, composition root) is the table of contents. Top-level service registrations and route wiring list major subsystems by name. At each level the code should fit in your head: low complexity, few activated objects, a handful of lines. Learn what exists first; open implementations only when the task needs them.

### Agent Navigation Strategy

An agent navigates without IDE tabs:

- **Symbol lookup**: `rg 'SymbolName'` or LSP go-to-definition when available.
- **Find usages**: `rg -w 'SymbolName'` across the repo.
- **Follow imports**: read the import graph from the file the task touches outward.
- **Read the test named after the behaviour before the implementation** — tests encode intended usage.
- **History for "why"**: `git log --follow -- <file>` and blame when the design choice is opaque.

Prefer progressive reading over speculative directory walks. See `rules.md` (Context budget).

### File Organisation

Follow the repository's existing convention. Flat vs deep is a project choice, not a design rule. File systems force one parent per file, so any hierarchy excludes other valid groupings — that is a trade-off the project has already made. Do not reorganise layout to match a preferred IDE navigation style.

### Monolith (as default)

A single deployable package containing domain, data access, HTTP, auth, and logging is the simplest shape. Internally structured (functional core / imperative shell, ports and adapters) but shipped as one unit is fine. The anti-pattern is internal spaghetti, not the monolith itself.

### Cycles

Dependency loops (A uses B uses C uses A) collapse zoom levels so nothing fits in your head. Mainstream languages often permit cycles between classes but forbid them between packages — splitting into packages/projects turns cycle prevention into a compile error. Detect cycles with the commands in `../tooling/commands.md`.

### Tests as Living Documentation

Read the test suite to learn intended usage. A good test has low complexity and a high abstraction level that communicates intent. Test helpers (`PostReservation`, `GetRestaurant`) are reusable entry points — sometimes generic enough to promote to a production client SDK. "Listen to your tests": if a test is hard to write or set up, the System Under Test is badly designed, not the test.

### Property-Based Testing

A framework generates arbitrary inputs (skewed toward boundaries) and you assert a property that must hold for all of them. Complements example-based tests; does not replace them. Useful when you can state an invariant ("quantity must be positive") more easily than enumerate cases.

### Behavioural Code Analysis

Mine Git history for patterns invisible in static code: which files change most often, which change together. Hotspot = high complexity × high change frequency → prime refactoring target. Change coupling catches copy-paste coupling that dependency analysis misses. Detection commands (churn, hotspots, coupling) live in `../tooling/commands.md`. Watch trends, not absolute numbers.

## Common Misconceptions

- **Myth**: A large flat directory means the code is disorganised.
  **Reality**: Hierarchy forces one axis of grouping. Follow the project's convention; navigation tools find files either way.

- **Myth**: A monolith is an anti-pattern.
  **Reality**: It's the simplest shape. The anti-pattern is internal spaghetti, which you can have in microservices too.

- **Myth**: Property-based testing replaces example-based tests.
  **Reality**: They complement each other. Examples pin concrete behaviour; properties probe invariants.

- **Myth**: Behavioural code analysis is for managers' dashboards.
  **Reality**: It's actionable engineering data — hotspots point at the files most worth refactoring.
