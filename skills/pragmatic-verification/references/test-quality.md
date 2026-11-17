# Test quality: tests that can fail for the right reason

Read when writing or reviewing test code, when a test looks weak or self-confirming, when a test
contradicts the task, or when a runner, fixture, skip or snapshot is being changed.

## Contents

- [Eight questions before adding a test](#eight-questions-before-adding-a-test)
- [Where expected comes from](#where-expected-comes-from)
- [Writing the test](#writing-the-test)
- [Weak shapes that pass while the code is wrong](#weak-shapes-that-pass-while-the-code-is-wrong)
- [Show that the test can fail](#show-that-the-test-can-fail)
- [Integrity of the check itself](#integrity-of-the-check-itself)
- [When a test contradicts the task](#when-a-test-contradicts-the-task)
- [Lifecycle: add, strengthen, merge, delete](#lifecycle-add-strengthen-merge-delete)
- [TDD and metrics in their place](#tdd-and-metrics-in-their-place)

## Eight questions before adding a test

1. Which promise of the system does the test protect?
2. Which realistic defect must turn it red?
3. Where is the correct value or invariant known from?
4. Why this level?
5. Which dependencies and failure mechanisms are excluded from its environment?
6. How does it differ from the checks that already exist?
7. Will it survive a change of implementation that keeps the behaviour?
8. Will the cause of a failure be clear from the name, the setup and the assertions?

If answers are missing, refine the test or drop it. "Few tests were written" is not a defect. "A
material requirement has no check" is a reason to continue.

## Where expected comes from

**Acceptable sources:** an agreed requirement, a small example computed by hand, a standard or an
external format, a confirmed fixture, a domain invariant, an independent reference implementation
whose reliability was assessed. A second model paraphrasing the implementation is not independent.

**Two passes:**

- **Intent first.** From requirements, contracts, public interfaces and domain examples, write the
  main scenarios, the forbidden effects and the real ambiguities before reading the new patch or
  its author's explanation.
- **Implementation second.** Read the diff and its dependencies to add specific boundaries,
  concurrency and error paths. A reviewer who never sees the code misses internal risks.

When an expected value was obtained only by reading the current code, say so. That test
characterizes existing behaviour. It does not show the behaviour is correct.

## Writing the test

- **One coherent scenario per test.** That is not "exactly one assert": creating an entity may
  need the identifier, the stored state and the absence of a duplicate. Do not join independent
  scenarios so that the first failure hides the rest.
- **Name and shape.** The name states the outcome. Arrange holds the conditions that matter, act
  is the client's action, assert checks the material consequences.
- **Visible data.** Helpers cut noise and keep data and expectations in sight. A shared fixture
  with implicit defaults makes a test hard to verify. Clarity beats removing repetition.
- **Exact where exactness is the contract:** amount, status, permissions, number of effects. Use
  semantic assertions for the rest. Comparing a whole HTML string or a large JSON pins details
  nobody promised.
- **Snapshots:** a small one is fine for a stable format when its changes are reviewed with
  attention.
- **Public boundary.** Test observable behaviour. Do not test private methods or internal state.

## Weak shapes that pass while the code is wrong

| Weak shape | Strengthen by |
|---|---|
| Only the happy branches of a guard are entered | One case per branch the guard can take, including loading, error and unknown values |
| The boundary is stepped over: 0 and 5 around `> 0` | Using the first value that crosses the line |
| The fixture uses an identity value: factor 1, empty list, one currency | Varying inputs so that different operators and branches give different results |
| An optional input is never absent | Supplying the missing value and asserting the safe outcome |
| The invariant and the implementation share one mistake | Asserting the predicate directly against the specification |
| Required fields are removed never, or all at once | Removing one required field at a time |
| "Nothing happened" is asserted before the state is reached | Waiting for the observable next state, then asserting the absence |
| A rejected promise or a thrown handler is hidden by polling or a retry | Awaiting settlement, capturing unhandled errors and asserting there are none |
| The assertion is truthiness, a length or "a call was made" | Asserting the value, the stored state or the user-visible outcome |
| A loop or `all()` runs over a collection that may be empty | Asserting first that the collection is not empty |
| Canary data does not resemble the real thing, as in redaction checks | Using data shaped like real identifiers and free text |
| The mock agrees with the code and both disagree with production | Cross-checking against a specification, a recorded real payload or the production validator |

- A line is covered and its value unchecked: strengthen the existing assertion, do not add a test.
- A line is uncovered: ask whether a test there would catch a real bug. If not, do not write a
  hollow test for it.

## Show that the test can fail

- **Bug fix:** see the regression test fail on the old defect, for the reason of the defect. An
  import error or an unavailable database demonstrates nothing about the assertion.
- **New material rule:** try one plausible break: `>=` to `>`, remove the ownership check, skip
  the write, repeat the external effect. The test must fail for that reason.
- **Scope:** a temporary experiment or a targeted mutation of the changed code. Not a mutation
  run over the whole repository for a percentage, and not after every cosmetic edit.
- **Survivors:** ask whether the survivor reveals wrong production code or only correct behaviour
  nobody checks. It may be equivalent. Do not invent a contract to kill it, and do not assert on
  log strings to kill it. Unreachable code is deleted, not tested.
- **Afterwards:** restore the code and re-run on the real state. Leave no temporary defect, no
  disabled assertion and no skipped test behind.

## Integrity of the check itself

For a significant change, look at three kinds of diff:

| Artefact | What to check when it changes |
|---|---|
| Accepted expectations | The reason an expected value, scenario, significant snapshot or invariant changed |
| Test code and data | Whether an important case disappeared, or a result was bent to fit the current implementation |
| The checking mechanism | Discovery, filters, skips, matchers, normalization, fixtures, real dependencies, the run command, the final exit status |

Expected values can stay the same while the test stops running or stops noticing the error. A
check that silently verifies nothing has this shape:

1. Its success path can be reached without doing the work: a skip branch, an early return, a zero
   denominator, an empty scope.
2. Absence is reported as health: "0 found, pass", "24 skipped" under a green total.
3. The change that disabled it looked unrelated.
4. Nothing tests the check itself.

- **A check must be able to say it is off.** An empty scope may pass. An unexecuted scope may not.
- **Read the summary line:** how many ran, how many were skipped, and whether the result was
  produced by this run or carried over from a cache.
- **New or changed runner, gate or selector:** show once that a known wrong result is reported as
  a failure.
- **Workarounds are reported.** A workaround that disables anything is named in the report and in
  a comment at the disabling line, saying what it disables.

## When a test contradicts the task

Neither edit the test until it is green nor treat every old assertion as truth.

1. Reproduce the discrepancy.
2. Name the requirement it conflicts with.
3. Establish what has to change: the implementation, the specification or an outdated check.
4. Change that artefact and state the reason.

An unresolvable domain ambiguity goes to the owner of the requirement, not to a vote of models. A
test that starts failing after a confirmed bug fix may be guarding the old bug: check it against
the domain basis before rolling back a correct fix.

## Lifecycle: add, strengthen, merge, delete

When working in an area, the four actions are equal and each needs a reason, not a quota.

- **Delete** a test for an obsolete contract, a full duplicate or a broken setup, once the
  protection that matters is kept elsewhere.
- **Keep long-term** only a test whose protected behaviour, source of expectation and added
  protection are clear.
- **Duplicates:** when a cheaper, more stable test catches the same significant defect, the
  duplicate needs its own justification.

## TDD and metrics in their place

- TDD is a working technique for a clear rule or a reproducible bug. It is not a certificate of
  quality: a test written first can still encode an invented expectation.
- A red run is valuable when it shows the intended failure.
- For an exploratory integration, experiment with the real system first, then pin the confirmed
  behaviour.
- Coverage points to code nothing visits. A targeted mutation checks sensitivity. Neither replaces
  a correct expected value or a met user goal.
