---
name: pragmatic-architecture
description: "Design method for simple solutions that are not fragile, from the choice of model, state ownership and boundaries down to the order of implementation steps, built on Kent Beck's 'make the change easy, then make the easy change'. Use when a change has more than one reasonable design, when deciding where state, an invariant or a side effect should live, when shaping a module boundary, contract or data model, when preparing code so that a hard change becomes easy, when a design must survive retries, concurrency, partial failure or migration, or when comparing alternatives and trade-offs. Not for code-level style and refactoring mechanics (code-that-fits-in-your-head), choosing tests (pragmatic-verification), visual or UX design, or a clear local fix."
---

# Pragmatic Architecture

**Core rule:** "For each desired change, make the change easy (warning: this may be hard), then
make the easy change" (Kent Beck). Designing is finding the structure in which the change at hand
is easy and every promise the system must keep still holds.

Judge a design by two tests, in this order:

1. **Admissible.** A design that breaks a required promise under a realistic sequence of events
   is out, however short it is.
2. **Easy to change.** Among admissible designs, prefer the one in which this change and the next
   plausible ones cost least, counting callers, migration, operation and recovery, not only the
   code written today.

**Simple** means few things to hold in mind at once and few conditions that must hold together,
not few lines or files. **Elegant** means a small consistent set of concepts covers the cases
without exceptions. **Fitting** means the cost matches the stakes, scale, deadline, team and
lifetime of this task. Remove accidental states, dependencies, variants and duties. Never remove
state a guarantee needs: the identity of an operation, an outcome not yet known, compatibility
between versions.

## Size the design first

| The change | What to do |
|---|---|
| One obvious design, no signal below | Make it directly. No record. |
| Several reasonable constructions, an awkward direct change, or cases that multiply | Follow the route briefly. Record the decision in one sentence. |
| A signal below is touched | Follow the route in full, with a property card for each promise the signal puts at risk. With several signals, or across a service or team boundary, have someone who did not write the design check it. |

Signals:

- an effect that cannot be taken back or that leaves the local transaction: money, a message,
  deletion, access rights, an external call;
- state reachable by more than one writer, request or process: concurrency, retries, timeouts,
  background work;
- a contract, schema or stored format with live clients or existing records;
- a shared limited resource (pool, queue, quota), or recovery that is manual or slow.

Judge by what the change touches, not by the size of the diff.

## The route

Each step ends in an output. Reuse an output that is already known; go back only when a deciding
fact changes.

1. **Name the change and what must survive it.** Separate the result the user needs from the
   solution they suggested. List the promises that must still hold, forbidden outcomes included.
   Check whether a smaller scope, an existing component or no change gives the result, and
   propose that openly. *Output: the change in one sentence and the promises.*
2. **Find the facts that can change the choice.** Walk the context groups: result and scope,
   meaning and invariants, data and load, quality and risk, variability, environment, people and
   ownership, economics and reversibility. Keep a factor only if another plausible value of it
   would change what is admissible, chosen, built, verified or recovered. Mark each as fact,
   requirement, assumption or unknown. Turn adjectives into scenarios with a measurable bound.
   Never invent a number. *Output: the deciding factors and open unknowns.* See `context.md`.
3. **Try the direct change against the code as it is.** Find where it gets hard: a rule known in
   several places, state with two owners, an effect buried mid-way, a caller that must know the
   order of steps. That spot, not general untidiness, is what preparation must remove. *Output:
   the direct change and what makes it hard. "Nothing" means no preparation is needed, not that
   the design is done.*
4. **Choose the representation.** Look for the model and data shape in which special cases
   disappear and illegal states cannot be written down. Start from the concepts the code already
   has: each new entity, state, table or service names the scenario the existing ones fail. Give
   each mutable fact one owner. Compute from primary data unless a stored copy is needed for
   history, replay or recovery. *Output: the concepts, and where each piece of knowledge, state
   and effect lives.* See `models-and-boundaries.md`.
5. **Put each guarantee where its violation is controlled.** For every promise a signal touches:
   the outcome that must not happen, the shortest sequence of events that would produce it (a
   second writer, a lost response, a crash between two steps, an old version still running), the
   mechanism that forbids that sequence and who owns it, the assumptions it rests on. An
   operation with an outside effect has four outcomes: done, failed without effect, partly done,
   unknown to the caller. A timeout is the fourth, not the second. *Output: property cards.* See
   `failure-and-recovery.md`.
6. **Compare with the simplest admissible alternative** on the same scenarios, the direct change
   and the current design included. Ask "why not substantially simpler?" and "what does this make
   harder?". No quota of alternatives and no scores. A trade-off gives up a preference, never a
   must: relaxing a must, even for the minutes of a rollout, is the user's decision. *Output:
   chose A over B because Y, accepting Z.*
7. **Prepare, then change.** Pick the smallest preparation that makes the change easy; it may be
   none. Keep structure changes and behaviour changes in separate steps, each leaving the system
   working. Design the path as well as the end state: versions that coexist, half-migrated data,
   work in flight, and what a rollback really restores. *Output: ordered steps, each safe to stop
   after.* See `change-path.md`.
8. **Rehearse and stop.** Walk the next plausible change through the new structure: if it is
   still hard, the preparation missed. Name the evidence each critical property needs
   (`pragmatic-verification`). Stop when more analysis no longer changes the choice or the
   accepted risk. *Output: the design record.*

## Design record

A direct change needs none. A real choice needs one sentence: "Need X under C. Must keep I. Chose
A over B because Y, accepting Z. Verify by P. Revisit when R." Anchor it in the code at hand:
where the change lands, what a caller no longer has to know after the preparation, and the
scenario that shows the must still holds. A promise at risk needs a card:

```text
Property        the observable promise and the outcome that must not happen
Mechanism       who controls the state and which transitions are allowed
Assumptions     dependency contracts; the failure, time and concurrency model
Counterexample  the 3-4 events that would break it, and what stops them
Limits          the nearest realistic failure the mechanism does not stop, and who accepted it
Evidence        what is checked, on which code or model, and what that leaves uncovered
Recovery        what is true after partial execution, a crash, a version change
```

"None" is not a counterexample. Give the strongest sequence found and the exact point where the
mechanism stops it; if nothing stops it, the design is not admissible yet. A counterexample the
mechanism was built for proves little: `Limits` names the one it was not built for.

## Never

- Merge look-alike code that changes for different reasons, or copy one authoritative rule
  without a way to keep the copies in step.
- Hide a remote or partial effect behind a call that looks local.
- Guard a concurrent invariant with read-then-write alone. Name the place that serialises the
  writes or refuses the conflict.
- Retry an operation that is not shown safe to repeat, or retry without a budget.
- Call a revert or a feature flag a rollback once data or an outside effect has changed.
- Replace or relax a requirement yourself because it is awkward to build. Propose it; the user
  decides.
- Add a layer, option, extension point or mechanism that cannot name the outcome it prevents or
  the confirmed change it makes cheaper.

## Example

Add JSON to an import that reads CSV, validates rows and writes them in one function. Clients
repeat a request after a timeout, and rows must not be imported twice.

- **Direct:** `if format == "json"` inside that function. Every later format touches validation
  and commit again.
- **Prepared:** first split decoding (bytes to rows) from validate-and-commit with behaviour
  unchanged, then add JSON as one decoder.
- **Not enough:** in both versions a repeat after a lost response lands the rows twice. That
  promise needs state: an import identity stored in the same transaction as the rows, under a
  unique constraint. Deleting that state for brevity breaks the promise.
- **Not needed:** a plugin registry, a queue, format negotiation. No confirmed change asks for
  them.

## What to read when

Read a reference only when its trigger applies.

| Read | When |
|---|---|
| [context.md](references/context.md) | The task is underspecified; which facts matter and when to stop asking; quality words without numbers; cost over the lifetime |
| [models-and-boundaries.md](references/models-and-boundaries.md) | Choosing a model, data shape, boundary or interface; special cases keep growing; two principles in conflict |
| [failure-and-recovery.md](references/failure-and-recovery.md) | A sizing signal is touched; writing a property card or a counterexample; retries, timeouts, overload, recovery |
| [change-path.md](references/change-path.md) | The change is hard in the current structure; code without tests; a schema, contract or data migration; whether to tidy first |
| [moves.md](references/moves.md) | The obvious design is stuck or heavy |
| [sources.md](references/sources.md) | The authority behind a rule is needed |
