# Practices Glossary

Fast-lookup reference for currently retained named practices from the book. Project-specific formatting and screen-size conventions are intentionally omitted.

## Quick Lookup Table

| Practice | One-line summary | Deep dive |
|----------|------------------|-----------|
| Bisection | Halve the code repeatedly to isolate a defect | `troubleshooting/rules.md` |
| Checklist for a New Code Base | Short startup checklist (Git, build automation, all warnings on) | `codebase-setup/rules.md` |
| Command Query Separation | A method is either a Command (side effects) or a Query (returns data), never both | `api-design/rules.md` |
| Count the Variables | Count locals, parameters, and fields in a method; keep the total low | `decomposition/rules.md` |
| Cyclomatic Complexity | Path-count metric; values above 15 trigger review by default | `decomposition/rules.md` |
| Explicit Seams for Cross-Cutting Concerns | Keep logging, caching, and resilience outside domain logic using a scope-appropriate seam | `separation-of-concerns/rules.md` |
| Functional Core, Imperative Shell | Push pure functions to the core, keep side effects at the edge | `decomposition/rules.md` |
| Complementary Communication | Put enforceable contracts in executable artifacts and rationale in prose/history | `api-design/rules.md` |
| Justify Exceptions from the Rule | Deviating from a rule is OK — if documented and justified | `teamwork-git/rules.md` |
| Parse, Don't Validate | Convert unstructured data to structured types as early as possible | `encapsulation/rules.md` |
| Explicit Boundary Parsing | Accept deliberate compatibility and reject malformed input | `encapsulation/rules.md` |
| Regularly Update Dependencies | Schedule dependency updates; never fall far behind | `evolution/rules.md` |
| Reproduce Defects as Tests | Turn every reproducible bug into an automated test | `troubleshooting/rules.md` |
| Review Code | Have another person review every change; rejection must be a real option | `teamwork-git/rules.md` |
| Semantic Versioning | Version releases by compatibility (MAJOR.MINOR.PATCH) | `evolution/rules.md` |
| Slice | Ship small vertical slices that each improve a working system | `../../workflows/add-feature.md` |
| Strangler | Add the new implementation alongside the old, migrate gradually | `evolution/rules.md` |
| X Out Names | Mentally replace method names with Xs to test signature clarity | `api-design/rules.md` |

## Practices

### Bisection
**Definition**: When struggling to understand a bug, remove half of your code and check if the problem persists. Keep halving until you have a minimal working example — at that point the cause is usually obvious.
**Use when**: A defect's cause is not clear from reading the code.
**Deep dive**: `troubleshooting/rules.md`

### Checklist for a New Code Base
**Definition**: When creating a new code base, follow a short checklist. A suggested starter: use Git, automate the build, turn on all error messages. Modify to fit your context, but keep it short.
**Use when**: Starting a new repository or project within a solution.
**Deep dive**: `codebase-setup/rules.md`

### Command Query Separation
**Definition**: Separate Commands from Queries. Commands are procedures that have side effects. Queries are functions that return data. Every method should be either a Command or a Query, but not both.
**Use when**: Designing any method or API surface.
**Deep dive**: `api-design/rules.md`

### Count the Variables
**Definition**: Count all the variables involved in a method implementation — local variables, method parameters, and class fields. Keep the total number low.
**Use when**: A method feels hard to reason about.
**Deep dive**: `decomposition/rules.md`

### Cyclomatic Complexity
**Definition**: Cyclomatic complexity measures the number of pathways through a piece of code. This skill uses above 15 as a review trigger, not an automatic rejection or proof of bad design. It also helps identify path-coverage needs.
**Use when**: Deciding whether a method needs to be broken up.
**Deep dive**: `decomposition/rules.md`

### Explicit Seams for Cross-Cutting Concerns
**Definition**: Keep logging, caching, telemetry, and resilience outside domain logic. Choose a Decorator, middleware, filter, interceptor, or pipeline according to scope and keep wiring visible.
**Use when**: You need logging, caching, retries, or auditing around core logic.
**Deep dive**: `separation-of-concerns/rules.md`

### Functional Core, Imperative Shell
**Definition**: Favour pure functions. Referential transparency means you can replace a function call with its result without changing behaviour — the ultimate abstraction. Pure functions compose well and are easy to unit test. Push them to the core; keep side effects in an outer shell.
**Use when**: Structuring a new module or refactoring existing logic.
**Deep dive**: `decomposition/rules.md`

### Complementary Communication
**Definition**: Use types, schemas, and tests for enforceable contracts; names for readable intent; comments and commit history for non-obvious rationale; documentation for system mission and usage.
**Use when**: Deciding where to put an explanation.
**Deep dive**: `api-design/rules.md`

### Justify Exceptions from the Rule
**Definition**: Good rules work most of the time, but sometimes a rule is in the way. It's OK to deviate — but justify and document the reason. Get a second opinion first; a co-worker may see a way to follow the rule that you missed.
**Use when**: You're tempted to break a team rule.
**Deep dive**: `teamwork-git/rules.md`

### Parse, Don't Validate
**Definition**: Your code receives data as JSON, XML, CSV, or other formats with few integrity guarantees. Convert less-structured data to more-structured data as soon as possible. Think of this as parsing, even if you don't parse plain text.
**Use when**: Data enters your system from the outside.
**Deep dive**: `encapsulation/rules.md`

### Explicit Boundary Parsing
**Definition**: Parse untrusted data into explicit supported forms. Accept compatibility only when deliberate and tested; reject malformed or invented shapes instead of silently coercing them.
**Use when**: Designing trust-boundary inputs and compatibility behavior.
**Deep dive**: `encapsulation/rules.md`

### Regularly Update Dependencies
**Definition**: Don't let your code base fall behind its dependencies. Check for updates on a regular schedule — if you fall too far behind, catching up becomes difficult.
**Use when**: Maintaining a long-lived project.
**Deep dive**: `evolution/rules.md`

### Reproduce Defects as Tests
**Definition**: If at all possible, reproduce bugs as one or more automated tests before fixing them.
**Use when**: A bug has been reported and can be triggered reliably.
**Deep dive**: `troubleshooting/rules.md`

### Review Code
**Definition**: Apply independent review proportional to risk. Material architecture, security, data, and contract changes require accountable human approval; automated review is screening rather than ownership.
**Use when**: Reviewing production changes under repository risk policy.
**Deep dive**: `teamwork-git/rules.md`

### Semantic Versioning
**Definition**: Consider using Semantic Versioning — MAJOR.MINOR.PATCH — to signal compatibility of a release.
**Use when**: Publishing a library or shared API.
**Deep dive**: `evolution/rules.md`

### Slice
**Definition**: Build through coherent vertical behavior and verifiable checkpoints. Large systematic work is acceptable when architecture and acceptance criteria remain clear.
**Use when**: Planning how to deliver a feature.
**Deep dive**: `../../workflows/add-feature.md`

### Strangler
**Definition**: Establish the new implementation beside the old, migrate callers, and remove the old path when side-by-side change reduces blast radius or improves verification and rollback.
**Use when**: In-place replacement would create excessive compatibility, deployment, or recovery risk.
**Deep dive**: `evolution/rules.md`

### X Out Names
**Definition**: Replace method names with Xs (in your head — you don't have to edit the code) to examine how much information the signature alone communicates. In a statically typed language, types can carry much of the meaning if you let them.
**Use when**: Reviewing an API for clarity.
**Deep dive**: `api-design/rules.md`
