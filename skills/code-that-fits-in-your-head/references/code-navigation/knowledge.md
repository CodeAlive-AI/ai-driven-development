# Code Navigation Knowledge

Core concepts for onboarding to an unfamiliar code base: seeing the big picture, finding details, reading architecture, and using tests as documentation.

## Overview

When you land on a new code base, your goal is to build a mental model without drowning in detail. Start at the entry point, zoom out to see the shape of the system, then zoom in only where the question demands it. The file tree is a poor map; the tests are a good one. Two complementary techniques, property-based testing and behavioural code analysis, help you probe invariants and find hotspots that static reading misses.

## Key Concepts

### Seeing the Big Picture

**Definition**: Starting at the framework's entry point (e.g. `Main`, `Startup`) and reading the top-level configuration as a table of contents for the code base.

The `Startup.ConfigureServices` method is typically a laundry list of service registrations: authorisation, repository, clock, post office. Each call points at a detail you can zoom into later. At each level the code should fit in your head (low cyclomatic complexity, few activated objects, a handful of lines).

**Key points**:
- Entry points and `Configure*` methods act as tables of contents
- High abstraction level is a feature here — you learn what exists, not how it works
- Fractal architecture: each zoom level stands on its own, surrounding context becomes irrelevant

### File Organisation

**Definition**: A flat layout where most files live in a single directory; subdirectories only where a group of files serves one narrow purpose.

File systems are trees — one parent per file — so any hierarchy excludes other valid groupings. Picking "Controllers vs Models" locks out "Reservations vs Calendar". Use the IDE's Go To Definition, Go To Implementation, Find All References, and tab switching instead of folders.

**Key points**:
- 65 files in one directory is acceptable if the IDE is your navigator
- Subdirectories are defensible only for tightly-scoped adapters (e.g. an `Options` folder of ASP.NET config DTOs)
- "How will we find files?" — you don't; the IDE does

### Monolith (as default)

**Definition**: A single deployable package containing domain, data access, HTTP, auth, and logging. Internally structured (e.g. functional core / imperative shell, ports and adapters) but shipped as one unit.

A monolith is the simplest shape. It's not automatically wrong. The sample restaurant reservation code base ships as three packages (production + two test projects) and is internally well-decoupled.

### Cycles

**Definition**: Dependency loops where A uses B uses C uses A. A classic case: a repository interface in the Domain Model whose method signatures reference ORM row types from the data access layer.

Cycles violate the Dependency Inversion Principle and the Acyclic Dependency Principle. Mainstream languages permit cycles between classes but forbid them between packages — so splitting a monolith into packages is a poka-yoke that makes architectural violations a compile error.

**Key points**:
- F# forbids cycles at the language level; Haskell's side-effect types push you toward ports-and-adapters
- Without that discipline, split into packages: domain model, data access, HTTP model, app host (composition root), plus matching test packages
- Cycles are a red flag: they collapse zoom levels so nothing fits in your head

### Tests as Living Documentation

**Definition**: Reading the test suite to learn intended usage. A good test has low cyclomatic complexity, few activated objects, and a high abstraction level that communicates intent.

Tests show how to make a reservation, how to authenticate, what a valid request looks like. Test Utility Methods (helpers like `PostReservation`, `GetRestaurant`) are reusable entry points — often generic enough to promote to a production SDK.

### Listening to Tests

**Definition**: Treating test pain as design feedback. If a test is hard to write, set up, or read, the System Under Test is badly designed, not the test.

From Growing Object-Oriented Software, Guided by Tests: "listen to your tests." Test code is code; refactor it, and when you do, watch for utilities that deserve to graduate into production code.

### Property-Based Testing

**Definition**: A testing style where the framework generates arbitrary inputs (usually 100 per run, skewed toward boundary values like 0, 1, -1) and you assert a property that must hold for all of them.

FsCheck (C#/.NET), QuickCheck (Haskell, the original, 1999), and ports in most languages. Replaces hand-picked `[InlineData]` values with wrapper types like `NonNegativeInt`, `PositiveInt`, `NegativeInt`. Good for invariants you can state generally ("quantity must be positive") but struggle to enumerate case by case.

**Key points**:
- Complements example-based tests; does not replace them
- Useful when you can describe a property more easily than you can enumerate cases
- Scales from simple wrappers up to custom generators via APIs like `Prop.ForAll`

### Behavioural Code Analysis

**Definition**: Mining Git history to surface patterns invisible in static code: which files change most often, which change together, who owns what.

Popularised by Adam Tornhill (CodeScene). Produces hotspot enclosure diagrams (circle size = complexity, colour intensity = change frequency) and change coupling maps (files that co-change above a threshold).

**Key points**:
- Hotspot = high complexity × high change frequency → prime refactoring target
- Change coupling catches copy-paste coupling that dependency analysis misses
- Also useful for bus-factor analysis via knowledge maps (main author per file)
- Can run in a Continuous Delivery pipeline; watch trends, not just absolute numbers

## Terminology

| Term | Definition |
|------|------------|
| Fractal architecture | Every zoom level is self-contained; outer context becomes irrelevant when you drill in |
| Hex flower diagram | A visual check that a method's activated objects or branches fit in roughly seven cells |
| Composition Root | The single place where the object graph is wired up |
| Test Utility Method | A helper inside the test project, often promotable to a production client SDK |
| Hotspot | File with both high complexity and high change frequency |
| Change coupling | Files that commit together more often than a threshold, even without a code-level dependency |
| Bus factor | How many team members can leave before knowledge of a file is lost |

## How It Relates To

- **Fractal architecture (ch. 7)**: Navigation exploits it; each `Configure*` method is one fractal level
- **Monolith vs packages**: Choose packages when you want the compiler to enforce acyclic dependencies
- **Test-driven development**: Listening to tests only works if tests exist and are maintained

## Common Misconceptions

- **Myth**: A large flat directory means the code is disorganised.
  **Reality**: Hierarchy forces one axis of grouping and hides others. Flat + IDE navigation is often clearer.

- **Myth**: A monolith is an anti-pattern.
  **Reality**: It's the simplest shape. The anti-pattern is internal spaghetti, which you can have in microservices too.

- **Myth**: Property-based testing replaces example-based tests.
  **Reality**: They complement each other. Examples pin concrete behaviour; properties probe invariants and boundaries.

- **Myth**: Behavioural code analysis is for managers' dashboards.
  **Reality**: It's actionable engineering data — hotspots point at the files most worth refactoring.

## Quick Reference

| Concept | One-Line Summary |
|---------|-----------------|
| Big picture | Start at the entry point; read `Configure*` as a table of contents |
| File organisation | Flat by default; IDE navigates, not folders |
| Monolith | Simplest shape; fine if internally decoupled |
| Cycles | Red flag; packages make them a compile error |
| Learning from tests | Tests encode intent — read them first |
| Listen to tests | Hard-to-write test = design smell |
| Property-based testing | Framework generates inputs; you assert invariants |
| Behavioural code analysis | Git-history mining for hotspots and change coupling |
