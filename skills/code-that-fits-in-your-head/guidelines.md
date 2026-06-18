# Guidelines — Task Routing for `code-that-fits-in-your-head`

This is the routing layer for the skill. Find the user's task or symptom below, then load **only** the specific files listed.

**Rule of thumb**: one primary file + at most 1-2 secondary files per task. If you find yourself wanting to load four or more, re-read the task — you may be combining two tasks.

**Note on `agent-native/`**: twelve of the thirteen theme folders are extracted from Seemann's book. The `agent-native/` folder contains four files that are our own editorial amendments — concerns specific to code agents that the 2021 book does not address. See `references/agent-native/knowledge.md`.

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
| Function/method complexity | `decomposition/rules.md`, `decomposition/smells.md` |
| API surface (public interface) | `api-design/rules.md`, `api-design/examples.md` |
| Naming quality | `api-design/rules.md` (X-Out Names section) |
| Type/class encapsulation | `encapsulation/rules.md`, `encapsulation/examples.md` |
| Tests | `outside-in-tdd/rules.md`, `teamwork-git/checklist.md` |
| Commit messages | `teamwork-git/rules.md` (50/72 rule) |
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
| Function exceeds 80×24 | `decomposition/rules.md` |
| Cyclomatic complexity > 7 | `decomposition/rules.md`, `decomposition/smells.md` (D1) |
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
| Commits have subjects > 50 chars | `teamwork-git/rules.md` |
| PR sits unreviewed for days | `teamwork-git/rules.md` (review latency) |

---

## By Named Practice

For any practice referenced by name in the user's request (e.g. "use Strangler", "apply 80/24"), first check `practices-glossary/knowledge.md` for a 1-sentence definition + deep-dive pointer, then load the referenced theme file.

Common named practices and their deep-dive location:

| Practice | Deep dive |
|----------|-----------|
| 50/72 Rule | `teamwork-git/rules.md` |
| 80/24 Rule | `decomposition/rules.md` |
| Arrange-Act-Assert (AAA) | `outside-in-tdd/rules.md` |
| Bisection | `troubleshooting/patterns.md` |
| Command Query Separation (CQS) | `api-design/rules.md` |
| Cyclomatic Complexity | `decomposition/rules.md` |
| Decorator (cross-cutting) | `separation-of-concerns/patterns.md` |
| Devil's Advocate | `outside-in-tdd/rules.md`, `outside-in-tdd/patterns.md` |
| Feature Flag | `evolution/rules.md`, `evolution/patterns.md` |
| Functional Core, Imperative Shell | `decomposition/patterns.md` |
| Hierarchy of Communication | `api-design/rules.md` |
| Parse, Don't Validate | `encapsulation/rules.md` |
| Postel's Law | `encapsulation/rules.md` |
| Red Green Refactor | `outside-in-tdd/rules.md` |
| Reproduce Defects as Tests | `troubleshooting/patterns.md` |
| Semantic Versioning | `evolution/rules.md` |
| Strangler | `evolution/patterns.md` |
| STRIDE / Threat Model | `security/knowledge.md`, `security/checklist.md` |
| Transformation Priority Premise | `encapsulation/rules.md` |
| X Out Names | `api-design/rules.md` |

Full list (28 practices) in `practices-glossary/knowledge.md`.

---

## Agent-Native Amendments (NOT from the book)

Load one of these when the user's concern is specifically how an agent should do something differently from Seemann's 2021 guidance. These files are editorial additions, not summaries of the book.

| Concern | File |
|---------|------|
| Agent cycle is much tighter than human TDD — how to structure edit/verify | `agent-native/verification-loops.md` |
| Agent produced confident-wrong code (invented API, outdated syntax, version drift) | `agent-native/hallucination-debugging.md` |
| How strict to make types/tests/specs; why they are primary defense for agent-written code | `agent-native/types-as-guardrails.md` |
| Making an agent-generated PR fast for a human to approve | `agent-native/reviewability.md` |
| Overview / disclaimer that these files are not book content | `agent-native/knowledge.md` |

When to prefer an `agent-native/` file over a book theme:

| User's question | Book theme | Agent-native | Choose |
|-----------------|-----------|---------------|--------|
| "Why is this test flaky?" | `troubleshooting/` | — | Book |
| "This test has been failing since I changed library version" | `troubleshooting/` | `agent-native/hallucination-debugging.md` | Agent-native (version drift) |
| "When do I run the tests?" | `outside-in-tdd/rules.md` | `agent-native/verification-loops.md` | Agent-native (tighter cadence) |
| "Should I enable strict mode?" | `encapsulation/rules.md` | `agent-native/types-as-guardrails.md` | Agent-native (book recommends moderation; we argue strict-from-line-1) |
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
| File | Purpose | Lines |
|------|---------|-------|
| `foundations/knowledge.md` | Sustainability, readability, 7±2 memory, humane code, rhythm | 130 |
| `foundations/rules.md` | Ten actionable heuristics for code-that-fits-in-head | 128 |

### Theme: codebase-setup/
| File | Purpose | Lines |
|------|---------|-------|
| `codebase-setup/knowledge.md` | Why checklists; aid-to-memory principle | 101 |
| `codebase-setup/rules.md` | Day-1 rules (Git, automated build, warnings-as-errors, ratchet) | 101 |
| `codebase-setup/checklist.md` | Actionable checklist for new or legacy code base | 123 |

### Theme: outside-in-tdd/
| File | Purpose | Lines |
|------|---------|-------|
| `outside-in-tdd/knowledge.md` | Walking skeleton, vertical slice, AAA, triangulation | 109 |
| `outside-in-tdd/rules.md` | Test-first rules (AAA, see fail first, etc.) | 135 |
| `outside-in-tdd/patterns.md` | Walking Skeleton, Characterisation Test, Devil's Advocate, Fake Object | 200 |
| `outside-in-tdd/examples.md` | 6 curated C# test examples | 225 |

### Theme: encapsulation/
| File | Purpose | Lines |
|------|---------|-------|
| `encapsulation/knowledge.md` | Invariants, DTO vs Domain, always-valid, natural numbers | 95 |
| `encapsulation/rules.md` | 9 rules: parse-don't-validate, Postel's Law, 400 vs 500 | 156 |
| `encapsulation/examples.md` | 5 C# examples + controller refactoring walkthrough | 227 |

### Theme: decomposition/
| File | Purpose | Lines |
|------|---------|-------|
| `decomposition/knowledge.md` | Code rot, cyclomatic complexity, 80/24, cohesion, fractal architecture | 144 |
| `decomposition/rules.md` | 10 hard rules with thresholds (≤7 complexity, 80×24) | 100 |
| `decomposition/smells.md` | 7 named smells (D1-D7) with detection + fix | 197 |
| `decomposition/patterns.md` | Sequential, nested, functional-core/imperative-shell | 192 |
| `decomposition/examples.md` | 5 C# before/after refactorings | 211 |

### Theme: api-design/
| File | Purpose | Lines |
|------|---------|-------|
| `api-design/knowledge.md` | Affordance, poka-yoke, CQS, hierarchy of communication, X-Out Names | 113 |
| `api-design/rules.md` | 9 actionable rules | 116 |
| `api-design/examples.md` | Maître D' examples, CQS fix, poka-yoke | 205 |

### Theme: separation-of-concerns/
| File | Purpose | Lines |
|------|---------|-------|
| `separation-of-concerns/knowledge.md` | Cross-cutting concerns, Decorator, logging, legibility-over-perf | 115 |
| `separation-of-concerns/rules.md` | Rules for logging, decorators, when to optimise | 134 |
| `separation-of-concerns/patterns.md` | Decorator walkthrough in C# | 195 |

### Theme: teamwork-git/
| File | Purpose | Lines |
|------|---------|-------|
| `teamwork-git/knowledge.md` | Git, CI, small commits, ownership, pair/mob | 147 |
| `teamwork-git/rules.md` | 11 rules (50/72, imperative mood, etc.) | 165 |
| `teamwork-git/checklist.md` | PR reviewer checklist | 108 |

### Theme: evolution/
| File | Purpose | Lines |
|------|---------|-------|
| `evolution/knowledge.md` | Feature flags, Strangler, semver, Conway's Law | 109 |
| `evolution/rules.md` | Actionable rules for safe change | 106 |
| `evolution/patterns.md` | Feature Flag, Method-Level Strangler, Class-Level Strangler | 195 |
| `evolution/examples.md` | 3 C# walkthroughs | 248 |

### Theme: troubleshooting/
| File | Purpose | Lines |
|------|---------|-------|
| `troubleshooting/knowledge.md` | Scientific method, rubber-duck, reproduce, bisect | 115 |
| `troubleshooting/rules.md` | Rules for debugging, slow tests, non-determinism | 155 |
| `troubleshooting/patterns.md` | Reproduce-as-Test, Git Bisection, Isolate-Then-Fix | 200 |

### Theme: security/
| File | Purpose | Lines |
|------|---------|-------|
| `security/knowledge.md` | STRIDE with one paragraph per threat | 92 |
| `security/rules.md` | Actionable per-category mitigations | 164 |
| `security/checklist.md` | STRIDE walkthrough for a new endpoint | 112 |

### Theme: code-navigation/
| File | Purpose | Lines |
|------|---------|-------|
| `code-navigation/knowledge.md` | Onboarding method, monolith, cycles, PBT, behavioural analysis | 128 |
| `code-navigation/rules.md` | Actionable onboarding rules | 153 |

### Theme: practices-glossary/
| File | Purpose | Lines |
|------|---------|-------|
| `practices-glossary/knowledge.md` | 28-practice lookup table + definitions | 178 |

### Theme: agent-native/ (NOT from the book — editorial amendments)
| File | Purpose |
|------|---------|
| `agent-native/knowledge.md` | Disclaimer + overview of why these amendments exist |
| `agent-native/verification-loops.md` | Tiered feedback pyramid; cycle tighter than human TDD |
| `agent-native/hallucination-debugging.md` | Classes of agent-specific defects; grep/read-before-edit |
| `agent-native/types-as-guardrails.md` | Strict types + tests + specs as primary defense; agent-friendliness of stacks |
| `agent-native/reviewability.md` | Fast-approve PR design; reviewability vs readability |

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
| "This function is 300 lines" | `decomposition/rules.md` + `decomposition/patterns.md` + `decomposition/examples.md` |
| "Help me write a commit message" | `teamwork-git/rules.md` (50/72 section only) |
| "Is this code sustainable?" | `foundations/knowledge.md` + `foundations/rules.md` |
