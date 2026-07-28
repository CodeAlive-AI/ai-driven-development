# Guidelines — Task Routing for `code-that-fits-in-your-head`

This is the routing layer for the skill. Find the user's task or symptom below, then load **only** the specific files listed.

**Rule of thumb**: one primary file + at most 1-2 secondary files per task. If you find yourself wanting to load four or more, re-read the task — you may be combining two tasks.

**Note on editorial content**: `agent-native/` contains four canonical amendments for code agents. Specialized agent-era additions in book-derived themes are explicitly marked and are not attributable to Seemann. See `references/agent-native/knowledge.md`.

---

## Table of Contents

- [By Task](#by-task)
- [By Code Element](#by-code-element)
- [By Symptom / Smell](#by-symptom--smell)
- [By Named Practice](#by-named-practice)
- [Agent-Native Amendments](#agent-native-amendments-not-from-the-book)
- [Decision Tree](#decision-tree)
- [File Index](#file-index)
- [Common Combinations](#common-combinations)

---

## By Task

### Code Review

| What you're reviewing | Load these files |
|-----------------------|-------------------|
| A pull request (general) | `workflows/review-code.md`, `teamwork-git/checklist.md` |
| A large agent-authored migration/change | `agent-native/reviewability.md`, `agent-native/verification-loops.md` |
| Function/method complexity | `decomposition/rules.md`, `decomposition/smells.md` |
| API surface (public interface) | `api-design/rules.md`, `api-design/examples.md` |
| Naming quality | `api-design/rules.md` (X-Out Names section) |
| Type/class encapsulation | `encapsulation/rules.md`, `encapsulation/examples.md` |
| Tests | `outside-in-tdd/rules.md`, `teamwork-git/checklist.md` |
| Commit messages | `teamwork-git/rules.md` (accuracy, rationale, repository policy) |
| Security posture of an endpoint | `workflows/threat-model.md`, `security/checklist.md` |
| Logging / cross-cutting | `separation-of-concerns/rules.md`, `separation-of-concerns/patterns.md` |

### Writing New Code

| What you're writing | Load these files |
|---------------------|-------------------|
| A brand-new feature | `workflows/add-feature-outside-in.md`, `outside-in-tdd/knowledge.md` |
| A new domain type with invariants | `encapsulation/rules.md`, `encapsulation/examples.md` |
| A new public API | `api-design/knowledge.md`, `api-design/rules.md` |
| A unit test (first for this SUT) | `outside-in-tdd/rules.md`, `outside-in-tdd/examples.md` |
| Additional test cases | `outside-in-tdd/rules.md` (Devil's Advocate section) |
| Cross-cutting concern (logging, caching, auth) | `separation-of-concerns/patterns.md` |
| A commit message | `teamwork-git/rules.md` |

### Refactoring

| What you're changing | Load these files |
|----------------------|-------------------|
| A long/complex function | `decomposition/rules.md`, `decomposition/patterns.md` |
| A class that has feature envy | `decomposition/smells.md`, `decomposition/examples.md` |
| Splitting monolithic logic | `decomposition/patterns.md`, `separation-of-concerns/patterns.md` |
| Replacing a legacy subsystem | `evolution/patterns.md` (Strangler), `evolution/examples.md` |
| Tests without touching prod code | `outside-in-tdd/rules.md` (separate-refactor section) |
| Hardening validation | `encapsulation/rules.md` (parse-don't-validate) |

### Debugging & Troubleshooting

| What you're investigating | Load these files |
|---------------------------|-------------------|
| A reproducible defect | `workflows/debug-defect.md`, `troubleshooting/patterns.md` |
| A flaky/non-deterministic test | `troubleshooting/rules.md`, `troubleshooting/patterns.md` |
| A regression (when did it break?) | `troubleshooting/patterns.md` (bisection section) |
| Slow test suite | `troubleshooting/rules.md` (slow tests section) |

### Security Review

| What you're threat-modelling | Load these files |
|------------------------------|-------------------|
| A new endpoint/service | `workflows/threat-model.md`, `security/checklist.md` |
| A STRIDE-specific concern | `security/rules.md` |

### Setting Up / Onboarding

| Situation | Load these files |
|-----------|-------------------|
| Starting a new code base | `codebase-setup/checklist.md`, `codebase-setup/rules.md` |
| Retrofitting discipline into a legacy base | `codebase-setup/rules.md` (gradual improvement section) |
| Onboarding to an unfamiliar code base | `code-navigation/knowledge.md`, `code-navigation/rules.md` |

### Evolution & Release

| Situation | Load these files |
|-----------|-------------------|
| Deploying a risky change | `evolution/rules.md` (feature flag section), `evolution/patterns.md` |
| Versioning a library / breaking change | `evolution/rules.md` (semver section) |
| Updating dependencies | `evolution/rules.md` (regular updates section) |

---

## By Code Element

| Element type | Primary | Secondary |
|--------------|---------|-----------|
| Function / method | `decomposition/rules.md` | `decomposition/smells.md` |
| Class / domain type | `encapsulation/rules.md` | `encapsulation/examples.md` |
| Public API surface | `api-design/rules.md` | `api-design/examples.md` |
| Unit test | `outside-in-tdd/rules.md` | `outside-in-tdd/examples.md` |
| Commit / PR | `teamwork-git/rules.md` | `teamwork-git/checklist.md` |
| Cross-cutting wrapper | `separation-of-concerns/patterns.md` | `separation-of-concerns/rules.md` |
| Validation layer | `encapsulation/rules.md` (parse-don't-validate) | — |
| Feature flag | `evolution/patterns.md` | `evolution/examples.md` |

---

## By Symptom / Smell

| If you notice... | Load these files |
|------------------|-------------------|
| Cyclomatic complexity > 15 or opaque branching | `decomposition/rules.md`, `decomposition/smells.md` (D1) |
| Small methods but architecture remains tangled | `decomposition/smells.md` (D8 system-wide sprawl) |
| Method envies another object's data | `decomposition/smells.md` (D4 feature envy) |
| Vocabulary drift between layers | `decomposition/smells.md` (D5 lost in translation) |
| Boolean `IsValid()` scattered everywhere | `encapsulation/rules.md` (parse-don't-validate) |
| Invariants checked in many places | `encapsulation/rules.md`, `encapsulation/examples.md` |
| `null!` or `?` sprinkled to silence compiler | `encapsulation/rules.md` |
| A method both returns and mutates | `api-design/rules.md` (CQS section) |
| Names don't carry meaning | `api-design/rules.md` (X-Out Names) |
| Comments explaining what code does | `api-design/rules.md` (naming-over-comments) |
| Logging duplicated across layers | `separation-of-concerns/rules.md` |
| Inheritance for cross-cutting | `separation-of-concerns/patterns.md` (Decorator) |
| Big-bang replacement plan | `evolution/patterns.md` (Strangler) |
| Tests are flaky | `troubleshooting/rules.md`, `troubleshooting/patterns.md` |
| Can't reproduce a bug | `troubleshooting/patterns.md` (reproduce-as-test) |
| Dependency cycles between namespaces | `code-navigation/rules.md` |
| Input validation after construction | `encapsulation/rules.md` |
| Commit history lacks rationale or useful checkpoints | `teamwork-git/rules.md` |
| PR sits unreviewed for days | `teamwork-git/rules.md` (review latency) |

---

## By Named Practice

For any retained practice referenced by name (for example Strangler or CQS), first check `practices-glossary/knowledge.md` for a short definition and deep-dive pointer, then load the referenced theme file.

Common named practices and their deep-dive location:

| Practice | Deep dive |
|----------|-----------|
| Arrange-Act-Assert (AAA) | `outside-in-tdd/rules.md` |
| Bisection | `troubleshooting/patterns.md` |
| Command Query Separation (CQS) | `api-design/rules.md` |
| Cyclomatic Complexity | `decomposition/rules.md` |
| Decorator (cross-cutting) | `separation-of-concerns/patterns.md` |
| Devil's Advocate | `outside-in-tdd/rules.md`, `outside-in-tdd/patterns.md` |
| Feature Flag | `evolution/rules.md`, `evolution/patterns.md` |
| Functional Core, Imperative Shell | `decomposition/patterns.md` |
| Complementary Communication | `api-design/rules.md` |
| Parse, Don't Validate | `encapsulation/rules.md` |
| Explicit Boundary Parsing | `encapsulation/rules.md` |
| Red Green Refactor | `outside-in-tdd/rules.md` |
| Reproduce Defects as Tests | `troubleshooting/patterns.md` |
| Semantic Versioning | `evolution/rules.md` |
| Strangler | `evolution/patterns.md` |
| STRIDE / Threat Model | `security/knowledge.md`, `security/checklist.md` |
| Transformation Priority Premise | `encapsulation/rules.md` |
| X Out Names | `api-design/rules.md` |

Full retained list in `practices-glossary/knowledge.md`.

---

## Agent-Native Amendments (NOT from the book)

Load one of these when the user's concern is specifically how an agent should do something differently from Seemann's 2021 guidance. These files are editorial additions, not summaries of the book.

| Concern | File |
|---------|------|
| Verification checkpoints, independent oracles, and protection against weakened gates | `agent-native/verification-loops.md` |
| Invented API, version drift, package hallucination, or dependency provenance | `agent-native/hallucination-debugging.md` |
| Choosing practical types, schemas, tests, and executable constraints | `agent-native/types-as-guardrails.md` |
| Reviewing agent-authored work, including very large systematic changes | `agent-native/reviewability.md` |
| Overview / disclaimer that these files are not book content | `agent-native/knowledge.md` |

When to prefer an `agent-native/` file over a book theme:

| User's question | Book theme | Agent-native | Choose |
|-----------------|-----------|---------------|--------|
| "Why is this test flaky?" | `troubleshooting/` | — | Book |
| "This test has been failing since I changed library version" | `troubleshooting/` | `agent-native/hallucination-debugging.md` | Agent-native (version drift) |
| "How should this long-running change be verified?" | `outside-in-tdd/rules.md` | `agent-native/verification-loops.md` | Agent-native (checkpoint and oracle integrity) |
| "Should I enable strict mode?" | `codebase-setup/rules.md` | `agent-native/types-as-guardrails.md` | Both — strongest practical policy with a brownfield ratchet |
| "How do I write a good commit message?" | `teamwork-git/rules.md` | — | Book |
| "How do I keep this PR reviewable?" | `teamwork-git/checklist.md` | `agent-native/reviewability.md` | Both — book for mechanics, ours for agent-specific framing |

---

## Decision Tree

```
START: What's the user asking?
│
├─► Review code / PR
│   ├─► Function-level issue → decomposition/rules.md (+ smells.md)
│   ├─► API quality → api-design/rules.md
│   ├─► Type/invariant → encapsulation/rules.md
│   ├─► Commit message → teamwork-git/rules.md
│   └─► Overall PR hygiene → workflows/review-code.md
│
├─► Write new code
│   ├─► New feature from scratch → workflows/add-feature-outside-in.md
│   ├─► New type with invariants → encapsulation/rules.md
│   ├─► New API → api-design/rules.md
│   └─► New test → outside-in-tdd/rules.md
│
├─► Refactor
│   ├─► Complexity too high → decomposition/rules.md + patterns.md
│   ├─► Feature envy → decomposition/smells.md (D4)
│   ├─► Replace legacy → evolution/patterns.md (Strangler)
│   └─► Cross-cutting bloat → separation-of-concerns/patterns.md
│
├─► Debug
│   ├─► New defect → workflows/debug-defect.md
│   ├─► Regression → troubleshooting/patterns.md (bisection)
│   └─► Flaky test → troubleshooting/rules.md + patterns.md
│
├─► Security review
│   └─► workflows/threat-model.md + security/checklist.md
│
├─► Set up / onboard
│   ├─► New repo → codebase-setup/checklist.md
│   ├─► Legacy retrofit → codebase-setup/rules.md
│   └─► Unfamiliar code base → code-navigation/rules.md
│
├─► Evolve / release
│   ├─► Risky change → evolution/patterns.md (feature flag)
│   ├─► Breaking change → evolution/rules.md (semver)
│   └─► Deps → evolution/rules.md (regular updates)
│
└─► Philosophical / why questions
    └─► foundations/knowledge.md
```

---

## File Index

### Theme: foundations/
| File | Purpose |
|------|---------|
| `foundations/knowledge.md` | Sustainability, readability, conceptual cohesion, and code as liability |
| `foundations/rules.md` | Durable heuristics for understandable, changeable software |

### Theme: codebase-setup/
| File | Purpose |
|------|---------|
| `codebase-setup/knowledge.md` | Why checklists and reproducible setup matter |
| `codebase-setup/rules.md` | Canonical verification, reproducibility, warnings, and ratchets |
| `codebase-setup/checklist.md` | Actionable checklist for a new or legacy code base |

### Theme: outside-in-tdd/
| File | Purpose |
|------|---------|
| `outside-in-tdd/knowledge.md` | Walking skeleton, vertical slice, AAA, and triangulation |
| `outside-in-tdd/rules.md` | Test-first rules with acceptance-oracle integrity |
| `outside-in-tdd/patterns.md` | Walking Skeleton, Characterisation Test, Devil's Advocate, and Fake Object |
| `outside-in-tdd/examples.md` | Curated C# test examples |

### Theme: encapsulation/
| File | Purpose |
|------|---------|
| `encapsulation/knowledge.md` | Invariants, DTO versus domain, and always-valid models |
| `encapsulation/rules.md` | Parse-don't-validate, explicit boundary parsing, and error semantics |
| `encapsulation/examples.md` | C# examples and a controller-refactoring walkthrough |

### Theme: decomposition/
| File | Purpose |
|------|---------|
| `decomposition/knowledge.md` | Code rot, cohesion, structural complexity, and fractal architecture |
| `decomposition/rules.md` | Responsibility-first decomposition; complexity above 15 triggers review |
| `decomposition/smells.md` | Function- and system-level smells with detection and fixes |
| `decomposition/patterns.md` | Sequential, nested, and functional-core/imperative-shell composition |
| `decomposition/examples.md` | C# before/after refactorings |

### Theme: api-design/
| File | Purpose |
|------|---------|
| `api-design/knowledge.md` | Affordance, poka-yoke, CQS, and X-Out Names |
| `api-design/rules.md` | Actionable API-design rules and complementary communication channels |
| `api-design/examples.md` | Maître D' examples, CQS fixes, and poka-yoke |

### Theme: separation-of-concerns/
| File | Purpose |
|------|---------|
| `separation-of-concerns/knowledge.md` | Cross-cutting concerns, logging, and legibility over performance |
| `separation-of-concerns/rules.md` | Choosing an explicit cross-cutting seam and when to optimise |
| `separation-of-concerns/patterns.md` | Decorator walkthrough in C# |

### Theme: teamwork-git/
| File | Purpose |
|------|---------|
| `teamwork-git/knowledge.md` | Git, CI, coherent checkpoints, ownership, and collaboration |
| `teamwork-git/rules.md` | Accurate history, risk-based integration, and review ownership |
| `teamwork-git/checklist.md` | PR reviewer checklist for architecture, debt, and evidence |

### Theme: evolution/
| File | Purpose |
|------|---------|
| `evolution/knowledge.md` | Feature flags, Strangler, semver, and Conway's Law |
| `evolution/rules.md` | Risk-, verification-, and rollback-based rules for safe change |
| `evolution/patterns.md` | Feature Flag, Method-Level Strangler, and Class-Level Strangler |
| `evolution/examples.md` | C# walkthroughs |

### Theme: troubleshooting/
| File | Purpose |
|------|---------|
| `troubleshooting/knowledge.md` | Scientific method, externalised evidence, reproduction, and bisection |
| `troubleshooting/rules.md` | Evidence-driven debugging, slow tests, and nondeterminism |
| `troubleshooting/patterns.md` | Reproduce-as-Test, Git Bisection, and Isolate-Then-Fix |

### Theme: security/
| File | Purpose |
|------|---------|
| `security/knowledge.md` | STRIDE with one section per threat |
| `security/rules.md` | Per-category mitigations plus coding-agent runtime threats |
| `security/checklist.md` | STRIDE walkthrough for a new endpoint |

### Theme: code-navigation/
| File | Purpose |
|------|---------|
| `code-navigation/knowledge.md` | Onboarding, monoliths, cycles, PBT, and behavioural analysis |
| `code-navigation/rules.md` | Compact rules for understanding unfamiliar code |

### Theme: practices-glossary/
| File | Purpose |
|------|---------|
| `practices-glossary/knowledge.md` | Retained-practice lookup table and definitions |

### Theme: agent-native/ (NOT from the book — editorial amendments)
| File | Purpose |
|------|---------|
| `agent-native/knowledge.md` | Disclaimer + overview of why these amendments exist |
| `agent-native/verification-loops.md` | Verification checkpoints, independent oracles, no gate weakening |
| `agent-native/hallucination-debugging.md` | Agent-specific defects and dependency provenance |
| `agent-native/types-as-guardrails.md` | Practical complementary executable constraints |
| `agent-native/reviewability.md` | Evidence, risk lanes, large changes, and accountable ownership |

### Workflows
| File | Purpose |
|------|---------|
| `workflows/review-code.md` | End-to-end code review process |
| `workflows/add-feature-outside-in.md` | Adding a new feature test-first |
| `workflows/debug-defect.md` | Investigating and fixing a defect |
| `workflows/threat-model.md` | Applying STRIDE to a new endpoint |

---

## Common Combinations

| Scenario | Files to load together |
|----------|------------------------|
| "Review this PR" | `workflows/review-code.md` + `teamwork-git/checklist.md` |
| "Start a new feature" | `workflows/add-feature-outside-in.md` + `outside-in-tdd/rules.md` + `encapsulation/rules.md` |
| "This bug's been around — when did it start?" | `workflows/debug-defect.md` + `troubleshooting/patterns.md` |
| "New public endpoint" | `api-design/rules.md` + `workflows/threat-model.md` + `security/checklist.md` |
| "Replace this legacy module" | `evolution/patterns.md` + `evolution/examples.md` + `decomposition/patterns.md` |
| "This function mixes too many responsibilities" | `decomposition/rules.md` + `decomposition/patterns.md` + `decomposition/examples.md` |
| "Help me write a commit message" | `teamwork-git/rules.md` (accuracy, rationale, repository policy) |
| "Is this code sustainable?" | `foundations/knowledge.md` + `foundations/rules.md` |
