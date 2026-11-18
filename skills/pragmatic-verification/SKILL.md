---
name: pragmatic-verification
description: "Language-agnostic playbook for thoughtful tests and checks: which cases deserve unit, integration, contract or e2e tests, when to mock, how to avoid redundant, self-confirming, brittle or flaky tests, and which QA scenarios to run through browser, computer or phone use. Use when writing, reviewing or pruning tests, auditing an existing project's test suite, planning verification of a change, or deciding whether the evidence is enough to call a task done. Not for tool syntax tutorials, load testing, security audits or evals of LLM output quality."
---

# Pragmatic Verification

**Core rule:** for each risk that matters, choose the cheapest check that still contains the
mechanism of the possible defect and lets the correct result be observed. A new check must add a
reason for confidence that existing checks do not give. Test count, coverage and mutation score
are never the goal.

A green check is evidence only when three things hold:

1. **The product is right.** Observed behaviour, including side effects, matches the requirement.
2. **The expectation is right.** The expected result comes from a source independent of the code
   under test.
3. **The check really ran.** It ran on the final revision, in a suitable environment, and its
   failure would have changed the reported status.

The work has two outputs: evidence that this task is solved, and permanent regression tests worth
their upkeep. A one-off browser pass is valid evidence and need not become a permanent test.

## Size the effort first

| Change | What to do |
|---|---|
| Cosmetic or local: copy, spacing, rename, pure refactoring | Run existing checks and look at the affected spot once. No new permanent test unless a gap is found. |
| Functional: a rule, state, API, persistence, UI flow | Follow the route. A few lines of plan are enough. |
| Costly to get wrong: access, money, deletion, user data, migrations, concurrency | Follow the route, plus negative cases at the server boundary, real storage, an independent review and explicit residual risk. |

Judge risk by damage, plausibility and recovery cost, not by diff size: a one-line change can
expose another user's data.

## The route

1. **State the contract.** List what the user can do after the change as separate observable
   claims, including forbidden effects: no false success, no access for others, no duplicate.
   Resolve unknowns from context or ask. Never turn a guess into an `expected`.
2. **Name the oracle.** Say where each correct result comes from: a requirement, an agreed
   example, a standard, an invariant, a hand-computed small case. "What the code returns now"
   is a characterization test and is labelled as one. Derive cases from the requirement first and
   read the implementation second.
3. **Check what exists.** Adding, strengthening, merging and deleting are equal options. Extend an
   existing case table before writing a new test. A new test names the promise it protects, the
   realistic defect that turns it red, and what existing checks miss.
4. **Derive cases from failure mechanisms.** Name the concrete way a claim can break ("a stale
   response overwrites newer state", not "handle errors") and pick the cases that expose it;
   time limits are boundaries too. See `case-design.md`.
5. **Choose level and reality.** Put each check at the smallest boundary that reproduces the
   mechanism and exposes the result. Say what is real, what is substituted, which platform rules
   the substitute skips, and what that leaves unproven. See `levels-and-doubles.md`.
6. **Show that the test can fail.** For a bug fix, watch the regression test fail on the old
   defect for the right reason. For an important rule, break it once (`>=` to `>`, drop the
   ownership check), see red, restore. See `test-quality.md`.
7. **Use the product.** When a user-facing path changed, drive the running build through its real
   interface and observe the end effect, not the click or the toast. See `exploratory-qa.md`.
8. **Close out on evidence.** Map what was actually run to each claim on the final revision, and
   say plainly what was not verified, including a purpose only real use can show. See
   `evidence-and-closeout.md`.

## Where each defect is caught

| Possible defect | Check | What must be real |
|---|---|---|
| Formula, rule, state transition | Unit, or property-based for many inputs and a clear property | The logic itself |
| SQL, constraints, transactions, migrations | Integration | A production-compatible engine and the real schema |
| HTTP contract, routing, validation, serialization | Integration through the public boundary | Router, validator, serializer |
| Access to another user's data | Integration through the server with two users | Authorization and ownership |
| Reaction to a failing dependency | Injected failure at the adapter | The reaction code; the adapter is verified separately |
| Race, retry, duplicate delivery | Integration with controlled overlap | Storage uniqueness and atomicity |
| Form logic, handlers, error display | Component test driven by user events | The UI tree; the network may be stubbed |
| Layout, focus, navigation, cookies, files | Real browser | The browser mechanism in question |
| Wiring of the whole chain | A few e2e routes ending in a meaningful observation | Everything on the route |
| Camera, push, background, device speed | Platform test on a suitable device | The OS or hardware feature |

Each business branch has one home. A higher level adds only a new boundary or failure mechanism
and never replays the unit table through the browser. The pyramid is a cost guide, not a quota.

## Never do this

- Compute `expected` with the code under test, a copy of its algorithm, or an unchecked snapshot.
- Test trivial accessors, the framework or standard library, the existence of a function, or a
  string in the source.
- Write a test in which only mocks execute, or assert internal calls and call counts that are not
  a promised external effect.
- Add a case with the same outcome and failure mechanism as an existing one.
- Mock a chain of internal collaborators to test a thin orchestrator. Test it integrated.
- Assert in a loop or `all(…)` over a collection that may be empty without first asserting it is
  not empty.
- Use fixed sleeps, retry until green, force-click, or bypass a broken UI step and report the path
  as passed.
- Weaken an expectation, skip, matcher, fixture, test discovery or the run command to get green.
  A red check means the code, the test or the specification is wrong. Find out which.

## What to read when

Read a reference only when its trigger applies.

| Read | When |
|---|---|
| [case-design.md](references/case-design.md) | Turning a requirement into cases: boundaries, states, sequences, combinations; pruning a matrix |
| [levels-and-doubles.md](references/levels-and-doubles.md) | Choosing a level, mock or real; databases, concurrency, migrations, external services |
| [test-quality.md](references/test-quality.md) | Writing or reviewing test code; a weak or self-confirming test; a test at odds with the task; a changed runner, fixture, skip or snapshot |
| [ui-automation.md](references/ui-automation.md) | Writing a permanent component, browser or e2e test |
| [exploratory-qa.md](references/exploratory-qa.md) | Planning or doing a pass through the running product by browser, computer or phone use |
| [flaky-and-brittle.md](references/flaky-and-brittle.md) | A test is intermittent or breaks on refactoring; a slow suite |
| [evidence-and-closeout.md](references/evidence-and-closeout.md) | Deciding whether to stop; review findings; a failure that looks pre-existing; the final report |
| [suite-audit.md](references/suite-audit.md), [suite-audit-worker.md](references/suite-audit-worker.md) | Auditing an existing project's tests and gates, not one change |
| [llm-features.md](references/llm-features.md) | The product itself calls an LLM at runtime |
| [sources.md](references/sources.md) | The authority behind a rule is needed |

**Stack tooling:** read only the file for the stack at hand; map its roles to any other.

[Python](references/stack-python.md) ·
[TypeScript/JS](references/stack-typescript.md) ·
[JVM](references/stack-jvm.md) ·
[.NET](references/stack-dotnet.md) ·
[Go](references/stack-go.md) ·
[Mobile](references/stack-mobile.md)

## Report

Give each claim one status: **verified**, **partially verified**, **not verified** or **blocked**,
with what ran, on which revision, and what substitutes leave unproven. Writing a test, running
it and showing it can fail are three different facts. Never invent a confidence percentage.
