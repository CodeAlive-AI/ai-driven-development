# Evidence, review and closeout

Read when deciding whether to stop, when handling review findings, when a failure looks
pre-existing, or when writing the final report.

## Contents

- [Order of gates](#order-of-gates)
- [Enough confidence](#enough-confidence)
- [The purpose after release](#the-purpose-after-release)
- [Whether another test is needed](#whether-another-test-is-needed)
- [Statuses](#statuses)
- [Independent review](#independent-review)
- [Triage of findings](#triage-of-findings)
- [Convergence](#convergence)
- [A failure that looks pre-existing](#a-failure-that-looks-pre-existing)
- [Templates](#templates)

## Order of gates

Run gates in the order in which one can invalidate the next:

```text
implementation and focused tests
  → the project's required gates
  → independent review, when warranted
  → repair and re-run
  → acceptance against the claims
  → pass through the real product, for user-facing work
  → evidence audit
```

- Any change to code, schema, prompt or UI invalidates later evidence gathered on the earlier
  revision. Re-run what the change touches.
- Do not give a verdict while a required test or review is still running.
- Tell apart a result checked locally, a build and a deployment. When the risk concerns the
  shipped application, check the built or deployed artefact.

## Enough confidence

1. The material acceptance claims are mapped to specific observations.
2. The changed logic and the material boundaries are checked at a fitting level.
3. For the important tests, the source of the expected result and the defect they detect are
   clear.
4. The project's required checks ran on the final revision.
5. There is no unexplained failure or skip that could change acceptance.
6. Where a user path changed, the matching scenario was exercised in the running product.
7. Limits of the environment, substitutions and residual risks are named and assessed.

A residual limitation is acceptable when it does not break the agreed result. An unknown about
data safety or working authorization cannot be declared acceptable because the budget ran out.
Report that result as partially verified or blocked, with the specific reason.

## The purpose after release

Some changes exist to move an outcome that only real use shows: more questions answered, fewer
abandoned forms, fewer support requests. Checks before release prove that the mechanism works,
not that it achieves the purpose.

- Name the signal, where it is recorded, the baseline it is compared with and when it will be
  read. Prefer data the system already records.
- If nothing records it, say so and propose the smallest record. Adding one joins the scope only
  when agreed.
- If the expected volume is too small to tell the effect from noise, say so instead of reading
  noise as success.
- Report the purpose as not verified until the signal is read. That does not hold back the
  closeout of the mechanism.

## Whether another test is needed

Add a test when it closes a material unverified risk, reproduces a new defect, protects an
important contract, or replaces an expensive check with a more reliable one. Do not add one for
the number of assertions, line coverage, the share of unit tests or a mutation score.

The economic question: how much does the new test reduce risk compared with the evidence already
held, and what do its run, its diagnosis and its upkeep cost? A critical requirement is not waived
on cost. Improve the design of the check, or declare a blocker.

## Statuses

| Status | Meaning |
|---|---|
| Verified | The claim is confirmed under the named conditions |
| Partially verified | Part is confirmed, and a material boundary remains outside the check |
| Not verified | The needed run or observation did not happen |
| Blocked | The required check or behaviour could not be obtained |

Plan state and execution state are different things. "Designed", "automated", "executed",
"passed", "blocked" and "not applicable" are not interchangeable. "Not applicable" is confirmed
again against the final scope.

## Independent review

- **When:** material uncertainty remains: permissions, data loss, a complex rule, concurrency, a
  disputed oracle. Not for every cosmetic diff.
- **Input:** the original task, the acceptance claims, the diff and the actual results. The first
  pass works without the author's explanation of why the solution is right.
- **Output:** concrete findings with a location, a trigger and a consequence. Status reports,
  general approval and unsupported severity are rejected.
- **Limits:** another agent's opinion is not an independent oracle, because agents can share one
  wrong assumption. The verdict rests on the requirement, an executable check and an observed
  result. The number of agreeing models adds nothing.
- **Severity:** before assigning it, read enough surrounding code, call sites, guards and tests to
  establish that the condition is reachable. A diff hunk alone does not establish impact.
- **Safety:** a read-only reviewer does not modify the shared working tree.

## Triage of findings

Deduplicate, then put each finding into exactly one category, and process them in causal order.

| Category | Meaning | Action |
|---|---|---|
| Missing intent | The requirement gives no basis for choosing the correct behaviour | Stop the affected work and ask the owner; do not infer intent |
| Wrong plan or criterion | Intent is known, the plan or the acceptance claim was incomplete or wrong | Amend it, then re-derive the affected work |
| Defect | The contract is adequate and the fix is unambiguous | Reproduce, add the earliest reliable red test, fix, re-run the affected gates |
| Plausible risk | Not yet shown either way | Run a targeted check, then re-classify |
| Pre-existing | A real problem outside this change | Record the five fields below and the owner |
| Noise | False positive, unreachable condition, behaviour already handled | Drop it and create no backlog entry |

A gap in intent or in the plan invalidates the lower-level reasoning about patches for the
affected behaviour. For a defect that reached production, also apply the `bug-fix-protocol` skill
when it is installed: it adds an audit of why the existing checks let the defect through.

## Convergence

A new round is justified by changed code, confirmation of a fix or a remaining material risk.
Repeating disputed remarks call for a revision of the task statement or the tool. They do not
call for more tests, another redesign or one more agent. After several unsuccessful loops, stop
and report the exact repeated blocking condition.

## A failure that looks pre-existing

It may be set aside as pre-existing only with all five:

1. The exact failing command or reproduction.
2. The baseline revision from before the change.
3. The current revision.
4. Proof that the failure exists at the baseline and is not made worse.
5. An explicit owner and a destination for the follow-up.

Without all five it is treated as a regression from this change. A known failure is never silently
declared unrelated.

## Templates

Shrink them for a small task to goal, risk, check and result.

**Verification plan**

```text
User goal:
Acceptance claims:
Invariants and forbidden effects:
Risks of the change:
Existing checks:
Missing checks and the chosen level:
Substituted dependencies and what stays unconfirmed:
QA charter and required platforms:
Required project gates:
Condition for completion:
Signal of the purpose after release, if any:
```

**Evidence table**, only when there are several distinct claims:

| Claim | Source of expected | Check | Fact and status |
|---|---|---|---|
| Rule or effect | Requirement or example | Test name or QA action | Revision, observation, limitation |

**Final report**

```text
Result and revision:
Claims confirmed:
Sources of the significant expected results:
Checks actually run, and what was observed:
Tests or checking tools changed, and why:
Substitutions used, and what they leave unconfirmed:
Flaky, skipped or impossible checks:
Residual risk and its effect on acceptance:
Purpose signal to read after release, and when:
Outcome: verified / partially verified / blocked
```

An artefact may be a run report, a trace, a small screenshot, an API response or the identifier of
a test object. Keep what is needed to check the conclusion and to diagnose. Do not collect large
logs just in case, and include no secrets or personal data.
