# Brittle, flaky and heavy tests

Read when a test fails intermittently, breaks on refactoring, or the suite is too slow.

## Contents

- [Tell the problems apart](#tell-the-problems-apart)
- [Brittle: narrow the contract](#brittle-narrow-the-contract)
- [Flaky: remove the source of variation](#flaky-remove-the-source-of-variation)
- [Order of investigation](#order-of-investigation)
- [Retries and quarantine](#retries-and-quarantine)
- [Heavy suites](#heavy-suites)
- [Signals worth tracking](#signals-worth-tracking)

## Tell the problems apart

- **Brittle:** fails after an allowed change of implementation while the behaviour is preserved.
- **Flaky:** can pass and fail for the same version of test and product under the same stated
  preconditions.
- **Changed conditions:** a change of flags, schema, data or a dependency version is investigated
  as a change of conditions first.

The cause of non-repeatability may sit in the test, the environment or the product. One test can
have both problems.

## Brittle: narrow the contract

Remove assertions on immaterial calls, private state, incidental order and decorative markup. If
the behaviour really changed, the failure is correct, and the expectation changes because of the
new requirement, not because the test is in the way.

## Flaky: remove the source of variation

| Source | Usual measure |
|---|---|
| Shared data and run order | Separate namespaces or accounts, independent setup and cleanup |
| Global state and caches | Reset of state, process isolation when needed |
| Process environment: variables, working directory, locale, time zone, ambient config files | Explicit setup per test; pin a non-default time zone so the assertion stays meaningful |
| Time and randomness | An injected clock and random source, a fixed seed, recorded inputs |
| Asynchrony | Waiting for a condition or event with a timeout, proper shutdown of background tasks |
| Wall-clock expectations ("two ticks within 35 ms") | Waiting on an event so that the order is causal |
| Network and provider | A controlled response in the main suite, a separate live check |
| Ports, files, processes | Unique resources and guaranteed release |
| Visual comparison | Stable sizes, fonts, data, animations and baseline |
| A race in the product | A real fix of synchronization or atomicity |

- A seed makes inputs reproducible. It does not control threads, the network or OS scheduling.
- Raise a timeout only after establishing the real budget of the operation: its stated limit, or
  its observed duration on the target environment plus a margin. It must not hide that the needed
  state never arrives. Fail at once on a terminal error state instead of waiting it out, and on
  timeout report the last observed state.
- Parallel runners can hide leakage between tests. Run the suspects serially, in shuffled order
  and from a clean checkout to expose it.

## Order of investigation

1. Keep the first failure: version, conditions, inputs, assertion, trace, logs, identifiers.
2. Form a hypothesis and repeat the run to test it.
3. Tell apart a product defect, a test defect, polluted state, an external failure and an
   infrastructure problem.
4. Fix the cause, reproduce the significant condition and confirm the fix.
5. Keep the original instability in the report, even when the next run passed.

## Retries and quarantine

- A pass after a failure is not a clean pass. Report it as flaky.
- Do not adopt "retry until green". Retries and quarantine can hide real defects.
- A retry does not fix a deterministic error. Simulate the real error and assert the reaction.
- **Quarantine** is a temporary exclusion from the blocking set with an owner, a task, a review
  date, a description of the risk, substitute evidence and a condition for return. For a material
  requirement, the missing reliable check stays an acceptance gap.
- A blocking gate that rejects good changes intermittently is a defect of the test system and is
  fixed as one.

## Heavy suites

**Typical sources of weight:**

- A unit table replayed through e2e.
- A container or a full application start per test.
- The whole stack started to check one piece of logic.
- A real provider inside the inner loop.
- Deep fixture graphs that set up far more than the scenario needs.

**What to do:**

- For each heavy check choose one action: keep, simplify, move to a fitting level, replace, or
  delete after checking the remaining risk. Do not delete a heavy test only for its duration, and
  do not rewrite the whole suite for a new classification.
- Separate the fast local loop, the required checks of a change and the rarer checks of a real
  environment. This is no licence to push critical checks to a nightly run: when a change touches
  that risk, they run before acceptance.
- Run the relevant set first, not the whole repository by reflex. Widen the run according to the
  possible regressions.
- **Automatic test selection:** account for new and changed tests, freshness of dependency data
  and known gaps. With insufficient data, run wider. For critical changes across components,
  selection by file paths may not be enough.
- **Skips in CI:** know whether a skipped job counts as passed in the pipeline.

## Signals worth tracking

- Which material defects pass through the suite, and why.
- How many failures need investigation without a contract violation behind them.
- Time to feedback and time to find the cause of a failure.
- How many tests have to be edited during a safe refactoring.
- Age of quarantined tests and presence of substitute checks.

Test count and coverage can appear in a report. They are not a measure of quality by themselves.
