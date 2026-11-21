# Failure, recovery and guarantees

How to keep a design from being fragile: which promises it makes, which mechanism keeps each,
under which assumptions, and what happens when a step fails half-way.

## Contents

- [What "not fragile" means](#what-not-fragile-means)
- [The assumptions that break](#the-assumptions-that-break)
- [Eight questions](#eight-questions)
- [The four outcomes of an operation](#the-four-outcomes-of-an-operation)
- [Building a counterexample](#building-a-counterexample)
- [Worked example](#worked-example)
- [Evidence fitted to the property](#evidence-fitted-to-the-property)
- [Keeping it proportionate](#keeping-it-proportionate)

## What "not fragile" means

A solution is not fragile when it keeps the required behaviour for allowed inputs and
interactions, withstands the deviations it was designed for, limits the consequences of the
rest, and can be recovered and changed under control. The goal is not a system that gains from
failure. It is one that does not break in the ordinary ways.

"Reliable" decides nothing. Name the observable promise: what result the user gets, when it
counts as complete, what survives a failure, which degradation is allowed, and under which
conditions recovery must finish.

Keep the goals apart, because one does not stand in for another: **correctness** (matches the
specification), **availability** (can serve), **safety of consequences** (no unacceptable
harm), **recoverability** (can return to an acceptable state), **changeability** (can be
altered safely). Refusing a new operation can be the right way to keep accepted data intact.

Tests give evidence about a construction. A green run does not define its properties.

## The assumptions that break

A fragile design works only while assumptions nobody wrote down stay true. Check a design for
each of these:

| Unwritten assumption | What really happens |
|---|---|
| The operation runs once | Clients, queues and people repeat it |
| A timeout means it did not happen | The work may have finished; the answer was lost |
| Nobody else changes this state meanwhile | A second request, a background job, an operator |
| A dependency is either up or clearly down | It is slow, or answers health checks while failing requests |
| A restart begins from a clean state | Half-finished work is on disk and in other systems |
| Old and new versions never meet | They overlap during every deploy, and old data lives on |
| Recovery can use the services it recovers | Recovery depends on what is broken |
| Cancelling the wait cancels the work | The remote side keeps going |

## Eight questions

Apply the ones the task touches. An inapplicable question is skipped, not answered with a
ritual paragraph.

**1. Which outcomes are unacceptable, and what is observable success?**
Start from the losses that must not happen: a repeated irreversible effect, loss of
acknowledged data, a breach of access, a wrong total, a resource held forever. State a few
critical invariants, and separately the conditions of completion. "No duplicate effect" forbids
a bad state. "Every accepted operation reaches a definite outcome" needs progress, and cannot be
promised if a dependency may stay down forever; say which conditions it relies on. If the
executor of the effect cannot support the promise, agree a weaker one and a way to resolve
doubt. A useful invariant names the transition that could break it, who controls that
transition, and where evidence of compliance would be found.

**2. Can independent state and spread of knowledge be reduced?**
Compute from primary data instead of keeping another mutable copy. Name one authoritative
writer. Separate computing a result from committing an irreversible effect. Prefer explicit
allowed states to combinations of flags. Deliberate duplication between independent contexts
can reduce coupling; duplicating an authoritative mutable fact without a reconciliation
protocol is a separate decision with its own price. Fewer lines and fewer conditions of
correctness are different things.

**3. Is each guarantee placed where its violation is controlled?**
If two concurrent writes can break the invariant, "read, then write" must be judged together
with the concurrency mechanism: a uniqueness constraint, the needed isolation level, a version
check, an atomic compare-and-set, a single writer. The name of a mechanism is not an argument.
Say which conflicting history it forbids, where the decision becomes fixed, what other
participants then see, and what happens after the executor stops. An invariant that spans
independent services is not secured by one local lock. First question: can the critical change
stay within one existing transactional boundary? A new distributed protocol must be earned by
the task.

**4. What are the partial and unknown outcomes?**
See [the four outcomes](#the-four-outcomes-of-an-operation).

**5. How far can a failure and accumulated work spread?**
Find the shared pools: connections, threads, memory, locks, queues, quotas, outbound channels.
Give each a limit and a priority rule. Bound repeated work by one budget across the layers; count
time already spent queueing; stop work nobody is waiting for. Look for positive feedback: what
adds load exactly when capacity drops (retries, reconnect storms, cache refill)? Design the exit
from overload, not only the steady state: a limit on accumulated work and a reachable recovery
mode. Removing the trigger may not end the degradation. Redundancy helps only when the copies
are independent with respect to the failure in question: two handlers in separate processes
still share a database, a configuration and a bad rollout.

**6. Is recovery a protocol?**
Recovery has start conditions, steps, required authority, dependencies and a verifiable end
state. Can it be interrupted and safely resumed? Walk a stop after every significant effect:
what is saved, what is lost, what counts as true after start, how finished work is recognised.
Say how discrepancies are reconciled and when reconciliation is complete. A backup is worth
exactly as much as the restore that has been performed within the allowed time. A rollback
command does not explain how changed data or an outside effect is undone.

**7. Is the path of change part of the design?**
See `change-path.md`: versions that coexist, half-migrated data, work in flight, lifecycle
changes that remove hidden cleanup.

**8. Does the evidence fit the property?**
See [evidence](#evidence-fitted-to-the-property).

## The four outcomes of an operation

Every operation with an effect outside the caller's transaction ends in one of four ways:

| Outcome | The caller knows | Design decision needed |
|---|---|---|
| **Done** | The effect happened | None |
| **Failed without effect** | Nothing happened | May be retried or reported |
| **Partly done** | Some effects happened | Continue, compensate, or accept the partial result as valid |
| **Unknown** | Nothing: a timeout, a lost response, a crash | How the real result is found, and whether a repeat is safe |

Rules that follow:

- A timeout is "unknown". Treating it as "failed" is how duplicates and lost work appear.
- A repeat must be shown safe, counting every observable effect. Some operations are safe by
  nature: setting a value, deleting by key. The rest need an **operation identity**: who
  issues it, where it is stored, for how long, in which scope it is unique, and what happens
  when the same identity arrives with different content.
- The identity and the effect must be fixed together: in one transaction, or under a contract
  of the executor that honours the identity. A check before the call plus a write after it is a
  race.
- Provide a way to look up the actual result and to reconcile state. If the outside system
  offers neither identity nor lookup, state the limit of the promise and the manual procedure.
- Acknowledged delivery of a message and a single business effect are different properties. An
  extra queue does not close the gap. An outbox ties a local change to an obligation to send;
  single effect at the receiver still needs the receiver's contract.
- An error handler is part of the state protocol. Decide what remains done and who may continue
  or repeat.

## Building a counterexample

A counterexample is a short concrete sequence of events that would break a property. Building
one is the cheapest test of a design, and it works on paper.

1. Write the success path as steps, marking each effect that outlives the step.
2. Between every two steps, and during each outside call, insert one event at a time:
   - a **crash** and restart;
   - a **duplicate** of the request or message;
   - a **second actor** doing the same or a conflicting operation;
   - a **delay** long enough for a timeout, with the work finishing afterwards;
   - an **old version** of the code or data taking part;
   - a **dependency** that is slow rather than down.
3. For each, say what every observer sees and whether the property still holds.
4. Keep the shortest sequence that breaks it, three or four events, and name the mechanism that
   forbids it. If there is none, the design is not admissible yet.

Classic sequences worth trying first:

| Sequence | Breaks |
|---|---|
| Request → effect done → response lost → retry | Single effect |
| A reads → B reads → A writes → B writes | An invariant guarded by read-then-write |
| Local commit → crash → message never sent | "Saved implies notified" |
| Message sent → crash → local commit lost | "Notified implies saved" |
| New code writes new format → old worker reads it | Compatibility during rollout |
| Dependency slows → callers retry → queue grows → dependency slows further | Exit from overload |
| Job takes lease → pauses → lease expires → second job starts → first resumes | Single owner |
| Cancel requested → remote work continues → result arrives after cleanup | "Cancelled means stopped" |

A counterexample that depends on a disputed assumption turns into a question about that
assumption. Check the assumption, not the opinion.

## Worked example

A service accepts an order and triggers an outside effect. The naive sequence "save the order,
call the dependency, mark success; on error retry" leaves four things undescribed: a lost
response, a crash between steps, a concurrent repeat, and recovery after a new version ships.

| Situation | Decision in the construction | What must be confirmed |
|---|---|---|
| Two identical requests at once | One operation identity; its result, or the right to execute, is established atomically | Concurrent execution against the real storage |
| The dependency acted, the response was lost | An explicit "unknown" state; result lookup, or a repeat under the agreed contract | No second effect under the stated conditions |
| The process stopped after the local write | The local change and a durable obligation to continue are committed together | Resumption after a stop at each intermediate point |
| The dependency slowed down | Bounded accumulated work and a budget of attempts | Useful throughput, and a reachable exit from overload |
| The format of a long operation changes | Explicit compatibility or a controlled version transition | Reading old records, continuing unfinished work, a way to repair |

The local right to execute prevents some concurrent repeats. Protection of the outside effect
has to act where the effect is made, within the executor's contract.

If the whole change fits one database, a transaction with the right constraints may be the
complete answer. The design chooses the smallest set of mechanisms that closes the concrete
properties. Its strength does not come from the number of exception handlers. It comes from
this: for every significant intermediate state, the allowed actions and the end result of
recovery are known.

## Evidence fitted to the property

| Property | Evidence that can confirm it |
|---|---|
| A computation | An independent example or reference result |
| A domain model | A check of allowed and forbidden transitions |
| Concurrency | Controlled interleavings against real storage, or a small model |
| Recovery | Interruptions at intermediate points and a return to a working state |
| Overload | Recovery of useful throughput after the trigger is removed |
| Migration | Mixed states: old and new code, old and new data |
| An outside contract | A small experiment against the real dependency, in the version used |

The model, the code, the runtime and the deployment process are different objects of a check.
Tie each result to an exact revision and to its assumptions, and say what it does not cover. An
independent review of the expected behaviour is worth more than a second set of tests that
repeats the same wrong assumption. For choosing and writing the checks, use
`pragmatic-verification`.

For a risky protocol, build a small model of the critical interaction; for a risky technical
assumption, run the smallest experiment against the real dependency. Choose the tool whose
result could change the decision. A checked model is not a checked implementation.

## Keeping it proportionate

- Pick protections by the failure mechanism they answer. Adding every pattern at once
  (breaker, retry, queue, fallback) creates new modes of failure; a breaker can make recovery
  harder, and a fallback that is rarely exercised fails when it is needed.
- The depth of analysis follows the consequences of the error, not the size of the repository.
- Research the code and its history for writers, transactional boundaries, background jobs,
  retries, shared resources and lifecycles only as far as they bear on the decision.
- Ready to implement means: each critical property has a concrete mechanism, its conditions and
  enough evidence for the next step; high-impact unknowns are closed or explicitly limit the
  design; recovery and version transition are feasible. It does not mean the unwritten code has
  been verified.
- In production, watch the promised results and meaningful discrepancies, not only whether
  processes are alive. A health signal must reflect the service actually promised: a heartbeat
  can survive while requests hang.
