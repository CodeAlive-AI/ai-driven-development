# Case design: from a requirement to a justified set of cases

Read when turning a requirement into concrete cases, or when a case matrix keeps growing.

## Contents

- [Procedure](#procedure)
- [Pick the technique by the shape of the behaviour](#pick-the-technique-by-the-shape-of-the-behaviour)
- [Risk menu](#risk-menu)
- [Sequences and failure points](#sequences-and-failure-points)
- [Two matrices, never multiplied](#two-matrices-never-multiplied)
- [Properties and metamorphic relations](#properties-and-metamorphic-relations)
- [Justify inclusion and omission](#justify-inclusion-and-omission)
- [Worked example: a shipping threshold](#worked-example-a-shipping-threshold)

## Procedure

1. **Promise.** Write the result the user gets, the rules that must keep holding, the consequences
   that are not allowed, and where each expected result is known from.
2. **Unknowns.** "Add autosave" does not define behaviour on a lost network, on conflicting edits
   or on closing the page. Separate what the requirement says from what was assumed. Resolve an
   unknown from context when the product leaves one reasonable reading. Ask when the choice is a
   product decision: data loss, conflict policy, access.
3. **Failure mechanisms.** Replace "check errors" with a sentence: "the permission check exists in
   the interface and is missing in the server handler". The mechanism selects both the case and
   the level.
4. **Model and cases.** For each rule decide what matters: classes of data, boundaries,
   combinations of conditions, transitions, order of events, concurrent actions. Derive the cases
   from that model with the table below.
5. **Oracle and observation.** Decide what counts as correct and which observation establishes it.
   A "Saved" message, an API response and a fresh read of stored data confirm three different
   claims.
6. **Level and environments.** Use `levels-and-doubles.md`, then the environment matrix below.
7. **Run and revise.** An observation may show that the model was incomplete. Add the missing
   class, state, combination or question, and continue.

## Pick the technique by the shape of the behaviour

| Behaviour shape | Technique | What it yields | Limit |
|---|---|---|---|
| Distinct categories of input | Equivalence classes | One representative per class that really behaves differently, valid and invalid | A class is a hypothesis: a hidden branch splits it |
| Limits, ranges, thresholds | Boundary analysis | Values just below, on and just above each point where the result changes | Only boundaries that exist in the contract or the code |
| Several conditions decide the outcome | Decision table | Each feasible combination with its outcome; infeasible ones marked with the reason | Grows fast; collapse conditions that do not matter in a row |
| Outcome depends on earlier actions | State transition model | Each allowed transition, each forbidden transition rejected, the important sequences | Visiting every state does not cover every transition |
| Many independent configuration factors | Combinatorial selection, pairwise or higher | A set with a stated coverage strength | Pairwise misses defects that need three factors |
| Behaviour not yet understood | Exploratory session | Observations, new hypotheses, a corrected model | Not a regression asset by itself |

Naming a technique in a plan adds nothing. The reason it fits the behaviour does.

**State models:** look for dead-end states, unreachable states, missing transitions such as
cancellation from any active state, forbidden transitions, and two triggers firing at once. For
every "in progress" status, include a case showing that an error cannot leave it in progress
forever.

**Time bounds:** a delay, timeout, retry window, expiry or upper cap is a boundary like any other.
Check just before it, where nothing happens yet, and just after it, where the effect happens
exactly once. Use a controlled clock, not real waiting. A cap that ends waiting is its own case:
a reminder held while the user is active must still go out at the maximum delay. When the wait
can outlive the process, check that a restart neither loses nor repeats it.

**Combinatorial sets:** choose the factors, define which combinations are impossible, and check
that the generated set really has the claimed coverage. The word "pairwise" above a table proves
nothing. Add every known dangerous combination by hand, whatever the method covers. Use it only
when there are three or more independent factors whose interactions matter.

## Risk menu

Pick what applies to the contract or the architecture. It is a menu, not a checklist.

- Empty result, partial success, absent optional input.
- The first value that crosses a boundary.
- One required field missing at a time.
- Repeat, cancellation, timeout, restart.
- Concurrency, another role, another owner.

Do not permute equivalent examples. Do not invent states that the types forbid and no real input
can reach. At an input boundary, do test the invalid data a real client can send.

## Sequences and failure points

Configuration tables do not express order. For retry, cancellation, lost responses, recovery,
concurrency and lifecycle, describe the scenario as: initial state, events, the order that
matters, the point of failure, the observable consequences.

These two cases look the same in the interface and differ in system state and in the recovery
they require:

- The save request never reached the server.
- The save happened and the response never reached the client.

A sequential double call and two concurrent calls also probe different risks.

## Two matrices, never multiplied

**Behaviour and risk matrix** answers what must be confirmed and by which evidence:

> rule or risk → chosen case → expected result and its source → observation → main check →
> what was actually executed

**Environment matrix** answers where the chosen checks must run. Possible axes: browser engine,
OS and significant version, device class, input method, accessibility settings, debug or release
build, fresh install or upgrade, network and real dependencies.

Four roles, five states, six data classes, four network modes and three platforms give 1,440
combinations. That number says nothing about the useful amount of checking. Reduce in this order:

1. Remove impossible combinations and keep the valid negative ones.
2. Send different mechanisms to the levels that fit them.
3. Choose representatives and say why the rest are equivalent.
4. Include the known dangerous combinations explicitly.
5. Apply combinatorial selection to the factors that remain, if needed.
6. Design the order-dependent sequences separately.

State what the chosen representative covers and what it does not. Server-side combinations of
roles and data are not repeated in every browser without a specific reason.

## Properties and metamorphic relations

Use a property-based test when inputs are many and a property is clear. The property states the
meaning of the task: sorting keeps the same multiset of elements and orders them.

- **Weak property:** ask whether a function returning a constant or an empty value would pass.
  "The fee is 0 or 500" is satisfied by a function that always returns 0.
- **Restated code:** a property that re-implements the algorithm is the same self-confirming test
  in another form.
- **Generator:** it must reach the important parts of the domain. Many random trivial inputs prove
  little. Prefer constrained generators to filtering.
- **Round trip:** encode then decode is useful, and a symmetric mistake in both passes it. When
  the format is itself a contract, add independent examples of the format.
- **No basis, no property:** permuting cart items may legitimately change the result when a
  discount depends on order.

A cluster of example tests around one predicate is often one property. One rule may have
examples, a property and an integration scenario when each targets a different failure mechanism.

## Justify inclusion and omission

Be able to finish both sentences for every material decision:

> This case is included because it checks the rule, boundary, transition or failure mechanism ___.

> These three values belong to one class, and no separate mechanism of difference was found.

"To increase coverage" does not finish the first sentence.

## Worked example: a shipping threshold

Illustrative contract: delivery is free when the subtotal after discounts is at least 10,000
minor units, otherwise it costs 500.

| Subtotal after discounts | Fee | Why the case exists |
|---|---|---|
| 9,999 | 500 | Just below the threshold |
| 10,000 | 0 | The included boundary |
| 10,001 | 0 | Just above the threshold |

The expected values are written down from the agreed rule. These two forms are not tests:

```text
expected = shipping_fee(10000)                # compares the function with itself
expected = 0 if subtotal >= 10000 else 500    # copies the production rule
```

- **Sensitivity:** change `>=` to `>` and confirm that the 10,000 case fails.
- **A different risk at the next level:** orchestration may pass the subtotal before the discount.
  One integration case is enough: 10,500 before the discount and 9,500 after it must cost 500. The
  unit table is not replayed there.
- **UI:** check only that the fee is visible and consistent with the order total, and only when
  the UI or its data path changed.
