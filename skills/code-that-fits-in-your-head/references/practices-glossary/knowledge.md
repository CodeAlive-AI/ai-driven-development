# Practices Glossary

Fast-lookup reference for 28 named practices from the book. Each entry: short definition + the theme folder where it's covered in depth.

## Quick Lookup Table

| Practice | One-line summary | Deep dive |
|----------|------------------|-----------|
| 50/72 Rule | Git commit subject ≤50 chars, body wrapped at 72 | `teamwork-git/rules.md` |
| 80/24 Rule | Keep code blocks within an 80-col × 24-row box | `decomposition/rules.md` |
| Arrange Act Assert | Structure tests in three clearly separated sections | `outside-in-tdd/rules.md` |
| Bisection | Halve the code repeatedly to isolate a defect | `troubleshooting/rules.md` |
| Checklist for a New Code Base | Short startup checklist (Git, build automation, all warnings on) | `codebase-setup/rules.md` |
| Command Query Separation | A method is either a Command (side effects) or a Query (returns data), never both | `api-design/rules.md` |
| Count the Variables | Count locals, parameters, and fields in a method; keep the total low | `decomposition/rules.md` |
| Cyclomatic Complexity | Useful code metric; keep under a threshold (7 works well) | `decomposition/rules.md` |
| Decorators for Cross-Cutting Concerns | Wrap business logic with decorators for logging, caching, fault tolerance | `separation-of-concerns/rules.md` |
| Devil's Advocate | Deliberately mis-implement the SUT to expose missing tests | `outside-in-tdd/rules.md` |
| Feature Flag | Hide incomplete features so you can keep integrating | `evolution/rules.md` |
| Functional Core, Imperative Shell | Push pure functions to the core, keep side effects at the edge | `decomposition/rules.md` |
| Hierarchy of Communication | Prefer types > names > comments > tests > commit msgs > docs | `api-design/rules.md` |
| Justify Exceptions from the Rule | Deviating from a rule is OK — if documented and justified | `teamwork-git/rules.md` |
| Parse, Don't Validate | Convert unstructured data to structured types as early as possible | `encapsulation/rules.md` |
| Postel's Law | Be conservative in what you send, liberal in what you accept | `encapsulation/rules.md` |
| Red Green Refactor | TDD loop: failing test → simplest pass → refactor → repeat | `outside-in-tdd/rules.md` |
| Regularly Update Dependencies | Schedule dependency updates; never fall far behind | `evolution/rules.md` |
| Reproduce Defects as Tests | Turn every reproducible bug into an automated test | `troubleshooting/rules.md` |
| Review Code | Have another person review every change; rejection must be a real option | `teamwork-git/rules.md` |
| Semantic Versioning | Version releases by compatibility (MAJOR.MINOR.PATCH) | `evolution/rules.md` |
| Separate Refactoring of Test and Production Code | Never refactor test and production code simultaneously | `outside-in-tdd/rules.md` |
| Slice | Ship small vertical slices that each improve a working system | `outside-in-tdd/rules.md` |
| Strangler | Add the new implementation alongside the old, migrate gradually | `evolution/rules.md` |
| Threat-Model | Make deliberate security decisions using STRIDE | `security/rules.md` |
| Transformation Priority Premise | Prefer small transformations that keep code in valid states | `outside-in-tdd/rules.md` |
| X-driven Development | Always drive your code with something (a test, analyzer, refactor tool) | `outside-in-tdd/rules.md` |
| X Out Names | Mentally replace method names with Xs to test signature clarity | `api-design/rules.md` |

## Practices

### 50/72 Rule
**Definition**: Write Git commit messages with a subject line of no more than 50 characters, followed by a blank line, then a body wrapped at 72 characters.
**Use when**: Writing any Git commit message.
**Deep dive**: `teamwork-git/rules.md`

### 80/24 Rule
**Definition**: Keep blocks of code small. In C-based languages, try to stay within an 80 × 24 character box — the size of an old terminal window. The exact thresholds are a mnemonic (nod to the Pareto 80/20 rule); pick a limit and stay within it consistently.
**Use when**: A method is growing long or wide.
**Deep dive**: `decomposition/rules.md`

### Arrange Act Assert
**Definition**: Structure automated tests according to the Arrange Act Assert pattern. Make it clear to readers where one section ends and the next begins.
**Use when**: Writing or reviewing any unit test.
**Deep dive**: `outside-in-tdd/rules.md`

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
**Definition**: Cyclomatic complexity measures the number of pathways through a piece of code. A threshold of 7 works well in practice — big enough to be useful, small enough to fit in your head. It also gives the minimum number of tests needed to fully cover the method.
**Use when**: Deciding whether a method needs to be broken up.
**Deep dive**: `decomposition/rules.md`

### Decorators for Cross-Cutting Concerns
**Definition**: Don't inject logging, caching, or fault-tolerance dependencies into your business logic — that jumbles concerns together. Instead, use the Decorator design pattern to wrap business logic with these concerns.
**Use when**: You need logging, caching, retries, or auditing around core logic.
**Deep dive**: `separation-of-concerns/rules.md`

### Devil's Advocate
**Definition**: Deliberately implement the System Under Test incorrectly. The more incorrect you can make it while still passing the tests, the more test cases you should consider adding. A heuristic for evaluating whether more tests would improve confidence.
**Use when**: Reviewing an existing test suite for gaps.
**Deep dive**: `outside-in-tdd/rules.md`

### Feature Flag
**Definition**: If you can't complete a coherent set of changes in half a day's work, hide the feature behind a feature flag and continue to integrate your changes with other peoples' work.
**Use when**: A change is too big to finish in a single short-lived branch.
**Deep dive**: `evolution/rules.md`

### Functional Core, Imperative Shell
**Definition**: Favour pure functions. Referential transparency means you can replace a function call with its result without changing behaviour — the ultimate abstraction. Pure functions compose well and are easy to unit test. Push them to the core; keep side effects in an outer shell.
**Use when**: Structuring a new module or refactoring existing logic.
**Deep dive**: `decomposition/rules.md`

### Hierarchy of Communication
**Definition**: Write code for future readers. Favour communicating behaviour and intent in this prioritised order: (1) distinct types, (2) helpful method names, (3) good comments, (4) illustrative tests, (5) helpful commit messages, (6) external documentation.
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

### Postel's Law
**Definition**: Be conservative in what you send, be liberal in what you accept. Methods should accept input as long as they can make sense of it, but no further. Return values should be as trustworthy as possible.
**Use when**: Designing pre- and postconditions for a method.
**Deep dive**: `encapsulation/rules.md`

### Red Green Refactor
**Definition**: The TDD loop as a checklist: (1) write a failing test — did it run, did it fail, did it fail on an assertion, on the last assertion? (2) make all tests pass with the simplest thing that could possibly work, (3) refactor while tests stay green, (4) repeat.
**Use when**: Practising test-driven development.
**Deep dive**: `outside-in-tdd/rules.md`

### Regularly Update Dependencies
**Definition**: Don't let your code base fall behind its dependencies. Check for updates on a regular schedule — if you fall too far behind, catching up becomes difficult.
**Use when**: Maintaining a long-lived project.
**Deep dive**: `evolution/rules.md`

### Reproduce Defects as Tests
**Definition**: If at all possible, reproduce bugs as one or more automated tests before fixing them.
**Use when**: A bug has been reported and can be triggered reliably.
**Deep dive**: `troubleshooting/rules.md`

### Review Code
**Definition**: Have another person review every change — one of the most effective QA techniques we know. Reviews can be continuous (pair/mob programming) or asynchronous (pull requests). Reviews must be constructive, but rejection has to be a real option — otherwise a review is worth little.
**Use when**: Any production change.
**Deep dive**: `teamwork-git/rules.md`

### Semantic Versioning
**Definition**: Consider using Semantic Versioning — MAJOR.MINOR.PATCH — to signal compatibility of a release.
**Use when**: Publishing a library or shared API.
**Deep dive**: `evolution/rules.md`

### Separate Refactoring of Test and Production Code
**Definition**: Automated tests give you confidence when refactoring production code — but refactoring test code is more dangerous because you have no tests of the tests. You may refactor test code, but not at the same time as production code. When you refactor production code, leave test code alone, and vice versa.
**Use when**: Any refactoring session.
**Deep dive**: `outside-in-tdd/rules.md`

### Slice
**Definition**: Work in small increments. Each increment should improve a running, working system. Start with a vertical slice, then add functionality to it.
**Use when**: Planning how to deliver a feature.
**Deep dive**: `outside-in-tdd/rules.md`

### Strangler
**Definition**: When a refactoring is too large to finish in half a day of consistent state, use the Strangler process: establish the new way of doing things side-by-side with the old way, gradually migrate callers from the old API to the new, and delete the old API when nothing uses it anymore.
**Use when**: A refactoring would otherwise take days or weeks in one shot.
**Deep dive**: `evolution/rules.md`

### Threat-Model
**Definition**: Take deliberate security decisions. For non-experts, the STRIDE model is manageable: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege. Involve IT and stakeholders — mitigation weighs business concerns against security risks.
**Use when**: Designing a feature that handles auth, user data, or trust boundaries.
**Deep dive**: `security/rules.md`

### Transformation Priority Premise
**Definition**: Try to work so your code is in a valid state most of the time. Transforming one valid state into another typically involves an invalid phase (won't compile). The Transformation Priority Premise suggests a series of small transformations that minimise these invalid phases.
**Use when**: Planning a non-trivial edit.
**Deep dive**: `outside-in-tdd/rules.md`

### X-driven Development
**Definition**: Use a driver for the code you write — static analysis, a unit test, a built-in refactoring tool, and so on. It's OK to deviate, but the closer you adhere, the less you tend to go astray.
**Use when**: Starting any piece of code.
**Deep dive**: `outside-in-tdd/rules.md`

### X Out Names
**Definition**: Replace method names with Xs (in your head — you don't have to edit the code) to examine how much information the signature alone communicates. In a statically typed language, types can carry much of the meaning if you let them.
**Use when**: Reviewing an API for clarity.
**Deep dive**: `api-design/rules.md`
