# Moves: less obvious constructions

A repertoire of moves that can dissolve a problem the obvious design only manages. Each is
conditional: it helps in its situation and harms outside it. "Can help" never means "always
do". Before using a move, state the situation, what it should remove, what must keep holding,
its price, and how to check that it worked.

## Contents

- [Index by symptom](#index-by-symptom)
- [Understanding and structure](#understanding-and-structure)
- [Contracts and interfaces](#contracts-and-interfaces)
- [State and data](#state-and-data)
- [Concurrency and coordination](#concurrency-and-coordination)
- [Failure and load](#failure-and-load)

## Index by symptom

| Symptom | Move |
|---|---|
| Behaviour is scattered and cannot be followed | [One pile](#one-pile) |
| Unsure whether two similar pieces are one rule | [Duplicate to learn](#duplicate-to-learn) |
| Every caller repeats the same precautions | [Complicate one module](#complicate-one-module-to-simplify-the-system) |
| Unsure whether a module boundary is real | [Deletion test](#deletion-test) |
| The right design depends on things not yet known | [Design with a time limit](#design-with-a-time-limit) |
| A flexible tool makes checking or safety hard | [Less expressive tool](#less-expressive-tool) |
| An abstraction surprises callers with latency, cost or failure | [Show the consequences](#show-the-consequences) |
| Callers depend on behaviour nobody promised | [No accidental contract](#no-accidental-contract) |
| Callers are full of error handling for one case | [Define the error out of existence](#define-the-error-out-of-existence) |
| Tests break on every refactoring | [Test behaviour](#test-behaviour-not-incidental-structure) |
| A stored copy drifts from its source | [Recompute](#recompute-instead-of-storing) |
| A cache or index must be exact and costs coordination | [Verifiable hint](#verifiable-hint) |
| An optimised implementation is hard to trust | [Slow implementation as oracle](#slow-implementation-as-oracle) |
| Locks and races around one piece of state | [Single writer](#single-writer) |
| Coordination between replicas or services is the bottleneck | [Order-insensitive operations](#order-insensitive-operations) |
| Everyone contends for one counter or limit | [Escrow](#escrow) |
| Background tasks leak, outlive their purpose or lose errors | [Structured concurrency](#structured-concurrency) |
| A lower layer "guarantees" delivery, yet results are wrong | [End-to-end check](#end-to-end-check) |
| A fallback makes outages worse or is never exercised | [Remove the dangerous fallback](#remove-the-dangerous-fallback) |
| Recovery needs the very thing that is failing | [Static stability](#static-stability) |
| Overload turns into collapse | [Shed load early](#shed-load-early) |
| Failures depend on rare timing and cannot be reproduced | [Deterministic simulation](#deterministic-simulation) |

## Understanding and structure

### One pile

- **Signal:** behaviour is spread over small functions and files, and nobody can say what
  happens.
- **Move:** inline the pieces into one place, read the whole, then split along the lines that
  are really there.
- **Must hold:** behaviour is unchanged; it is an exploration step, not the target shape.
- **Trap:** leaving the pile as the final design.
- **Check:** after the new split, a reader follows the behaviour from one place.

### Duplicate to learn

- **Signal:** two pieces look alike and it is unclear whether they express one decision.
- **Move:** keep, or make, the copies and let them evolve until the real common part shows.
- **Must hold:** an established single rule (a tax rate, an access check) is not copied without
  control over drift.
- **Trap:** a temporary experiment that turns into supported code by neglect.
- **Check:** after a few changes, did the copies change together or apart?

### Complicate one module to simplify the system

- **Signal:** each caller repeats ordering, retries, validation or cleanup.
- **Move:** move that work inside one module, even if it becomes harder to write.
- **Must hold:** the sum of obligations falls for callers, the module owner and operators
  together.
- **Trap:** the complexity is only hidden from the estimate; the module becomes a single point
  whose failure or change hits everyone.
- **Check:** the client-obligations list is shorter, and the wider blast radius is accepted.

### Deletion test

- **Signal:** a boundary exists on paper and nobody knows whether it isolates anything.
- **Move:** ask what deleting or replacing the part would take.
- **Must hold:** the count includes data, outside contracts, migration and operations.
- **Trap:** easy deletion of a file read as proof of independence.
- **Check:** a diagnostic only. It informs a decision and makes none.

### Design with a time limit

- **Signal:** the problem is not yet understood, or the scale will change by orders of
  magnitude.
- **Move:** build deliberately for a limited horizon and plan the replacement.
- **Must hold:** the horizon, the signal for replacement and the way out are written down; the
  musts hold from day one.
- **Trap:** "temporary" as an excuse to skip a guarantee; a rewrite assumed to be free.
- **Check:** the data and contracts that must survive replacement are named.

## Contracts and interfaces

### Less expressive tool

- **Signal:** a general mechanism (arbitrary code, free-form queries, an open plugin interface)
  makes behaviour hard to check, bound or secure.
- **Move:** offer a narrower form: a table, a declarative rule, a fixed set of operations.
- **Must hold:** every scenario that is needed is still expressible.
- **Trap:** inventing a private language; cutting needed behaviour for the sake of rigour.
- **Check:** walk the real use cases through the narrow form; name what became checkable.

### Show the consequences

- **Signal:** a call looks local and cheap but can be slow, partial, costly or unsafe to
  repeat.
- **Move:** put deadlines, error kinds, repeat rules and cost into the contract, while keeping
  the mechanism hidden.
- **Must hold:** only what correct use depends on is shown.
- **Trap:** leaking every technical detail and calling it honesty.
- **Check:** can a caller use it correctly from the contract alone?

### No accidental contract

- **Signal:** many consumers; an observable detail (order, timing, error text) is stable by
  chance.
- **Move:** keep the unpromised detail from looking like a promise (vary it where cheap,
  document it as unspecified), and check who relies on it before changing it.
- **Must hold:** existing production compatibility is not broken on the strength of "it was
  never documented".
- **Trap:** using the idea as licence to change behaviour arbitrarily.
- **Check:** consumers pass under each allowed variant of the behaviour.

### Define the error out of existence

- **Signal:** callers carry handling for a case that could simply be valid.
- **Move:** change the contract so that the case is ordinary: deleting what is absent succeeds,
  an empty range yields an empty result.
- **Must hold:** the new meaning matches the original intent, or the change of requirement is
  agreed.
- **Trap:** renaming data loss, a denied access or a broken process as success.
- **Check:** no caller needed the error to make a decision.

### Test behaviour, not incidental structure

- **Signal:** tests fail on refactoring while behaviour is unchanged.
- **Move:** check the promised behaviour through the interface that carries the promise.
- **Must hold:** essential internals are still checked where they live: an algorithm, an access
  rule, the absence of a repeated effect, the order of a protocol.
- **Trap:** assuming a test through the public interface is always stronger or cheaper.
- **Check:** a refactoring leaves tests green; breaking the promise turns one red.

## State and data

### Recompute instead of storing

- **Signal:** a derived value is stored and must be kept in step with its source.
- **Move:** compute it on demand from primary data.
- **Must hold:** the inputs are reproducible, the cost is acceptable, and the meaning of "as
  of when" is right.
- **Trap:** deleting a fact that looks derived but records what happened: a request identity, a
  price at the time of sale, an audit entry, anything needed for replay or recovery.
- **Check:** can the value be rebuilt today, exactly, from what is kept?

### Verifiable hint

- **Signal:** keeping a cache, index or routing entry exact needs expensive coordination.
- **Move:** let it be possibly wrong, and verify against the authoritative state before acting.
- **Must hold:** the verification is sufficient, and a miss has a correct path.
- **Trap:** treating the hint as permission to act; a race between the check and the effect.
- **Check:** feed it a wrong hint. The result is slower, not incorrect.

### Slow implementation as oracle

- **Signal:** an optimised or complex implementation is hard to verify.
- **Move:** keep a simple, obviously correct version and compare the two on many inputs.
- **Must hold:** the area of comparison is clear and the two obtain the answer in sufficiently
  independent ways.
- **Trap:** agreement read as correctness when both share a misunderstanding of the
  requirement.
- **Check:** seed a defect into the fast version and see the comparison catch it.

## Concurrency and coordination

### Single writer

- **Signal:** locks, lost updates and races around one piece of state.
- **Move:** give the state one owner that applies all changes in order; others send requests.
- **Must hold:** the owner's throughput, queue limits, handover of ownership and recovery are
  designed.
- **Trap:** claiming a speed-up without measurement; believing one writer removes every race
  (two owners after a failed handover; readers of stale state).
- **Check:** what happens when the owner stops mid-operation, and when two believe they own it?

### Order-insensitive operations

- **Signal:** replicas or services coordinate only to agree on an order.
- **Move:** shape the operations so that the result does not depend on order: growing sets,
  maxima, merges that commute.
- **Must hold:** the property is shown for the concrete operations and the business result.
- **Trap:** an append-only log does not make the outcome monotonic; limits on a resource and
  "nothing exists yet" claims still need coordination.
- **Check:** apply the operations in two different orders, with duplicates. Same result?

### Escrow

- **Signal:** all participants contend for one global counter, stock or quota.
- **Move:** hand out shares in advance; each participant spends its own share locally.
- **Must hold:** the global invariant survives transfer, failure and return of shares.
- **Trap:** capacity stranded in an unreachable share; the cost of rebalancing. Coordination is
  moved, not removed.
- **Check:** a holder of a share fails. Is the invariant intact, and is the share recoverable?

### Structured concurrency

- **Signal:** background tasks outlive their purpose, lose errors or cannot be cancelled.
- **Move:** tie each task to an owner and a scope; the scope ends when its tasks have ended.
- **Must hold:** long-lived work has an owner of matching lifetime.
- **Trap:** expecting the construction to preserve work when the process itself dies.
- **Check:** on error or cancellation in the scope, is anything still running?

## Failure and load

### End-to-end check

- **Signal:** a transport or storage layer acknowledges, and the application result is still
  wrong or duplicated.
- **Move:** check the guarantee at the level that knows its meaning: the business operation,
  not the packet.
- **Must hold:** lower-level guarantees stay in use as optimisations.
- **Trap:** duplicating every check at every level.
- **Check:** for each acknowledgement, say exactly what it confirms and where the user's
  promise becomes true.

### Remove the dangerous fallback

- **Signal:** a fallback path is rarely run, behaves differently, or adds load during an
  outage.
- **Move:** remove it, or make the main path strong enough and exercise the fallback
  constantly.
- **Must hold:** the agreed behaviour under degradation and required availability remain.
- **Trap:** treating every fallback as harmful.
- **Check:** compare whole behaviour with and without it during the failure it was built for.

### Static stability

- **Signal:** recovery needs scaling, configuration, discovery or credentials from a control
  plane that may itself be down.
- **Move:** provision in advance, so that the working part keeps working with no control
  operations.
- **Must hold:** the range of failures covered is stated; working on old state is allowed by
  the contract.
- **Trap:** relying on expired permissions or stale configuration; ignoring the cost of the
  reserve.
- **Check:** draw the dependencies of recovery separately from those of normal work.

### Shed load early

- **Signal:** under overload every request gets slower until none completes.
- **Move:** reject excess work at the door, cheaply, before it takes resources.
- **Must hold:** refusal is admissible; priorities, fairness, limits and client retry behaviour
  are defined.
- **Trap:** counting rejected requests as success; rejections that trigger a retry storm.
- **Check:** remove the overload. Does useful throughput return by itself?

### Deterministic simulation

- **Signal:** defects depend on rare orderings and cannot be reproduced.
- **Move:** design the system so that time, scheduling, network and failures can be driven by a
  seeded test harness.
- **Must hold:** the cost is proportionate to the risk of the failures studied.
- **Trap:** a result that holds for the simulated model taken as true of the real environment.
- **Check:** a known ordering defect is found and replayed from its seed.
