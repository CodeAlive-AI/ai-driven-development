# Models, boundaries and interfaces

How to choose the representation of a problem, where to put knowledge, state and effects, and
how to decide when two good principles disagree.

## Contents

- [Representation first](#representation-first)
- [Illegal states](#illegal-states)
- [Algorithms and data are design](#algorithms-and-data-are-design)
- [Where things live](#where-things-live)
- [Boundaries](#boundaries)
- [Interfaces and client obligations](#interfaces-and-client-obligations)
- [Comparing alternatives](#comparing-alternatives)
- [When principles disagree](#when-principles-disagree)
- [A shared agreement for parallel work](#a-shared-agreement-for-parallel-work)

## Representation first

Most heavy designs are the right logic on the wrong representation. Before adding a mechanism,
look for the shape of data or model in which the problem becomes plain.

| Symptom | Try |
|---|---|
| Special cases keep arriving | A model in which they are ordinary cases: an empty list instead of null, a zero-amount line instead of an "if no discount" branch |
| Flags whose combinations are partly illegal | One explicit state with the data each state needs |
| The same check in many places | Convert once at the edge into a value that is valid by construction |
| Branching on a type or kind in many places | A table of data, or one operation per kind |
| Order-dependent steps a caller must remember | One operation that owns the sequence |
| Derived values drift from their source | Compute them, or name one owner that updates both atomically |
| A name needs "and", "or" or "manager" | Two concepts are sharing one name; split the concept before the code |

A good representation makes the next change local: adding a case adds one row or one type, not
an edit in five functions. Test a candidate by walking the task's real scenarios through it,
including the awkward ones. Then combine two cases: if the combination needs a branch of its
own, the model is missing a concept.

## Illegal states

Make states that must not exist impossible to write down:

- an explicit state type instead of independent booleans (`Draft | Submitted(at) |
  Paid(receipt)` instead of `isSubmitted`, `isPaid`, `receipt?`);
- unvalidated outside data and validated domain values as different types, converted in one
  place;
- transitions as named operations that take one state and return another.

Limits: types exclude combinations inside one process. They do not prove that transitions are
right, that two requests cannot interleave, that the disk kept the write, or that outside data
is true. An invariant that spans requests needs a mechanism at the shared state (see
`failure-and-recovery.md`).

## Algorithms and data are design

Design is not only the arrangement of modules. The distribution of inputs, the complexity of
the algorithm, memory, I/O and contention decide whether a structure can work at all. A simple
structure with the right data layout often removes a whole caching or batching layer. Check a
performance assumption that decides the design by measurement or analysis, at the scale named in
the context, before building on it.

## Where things live

Place four things on purpose:

| What | Rule | Sign it is misplaced |
|---|---|---|
| **Knowledge** (a rule, a format, an algorithm) | One authoritative place per decision | A change of one rule needs edits in several modules |
| **State** | One owner per mutable fact; others ask or receive | Two writers; a copy that must be "kept in sync" |
| **Effects** (I/O, messages, time, randomness) | At the edge: decide with plain computation, then act | A calculation cannot be checked without a network or a clock |
| **Responsibility** | The party that has the knowledge to do it right | Every caller repeats the same precaution |

Separating computation from effects is a technique, not an architecture to impose: use it where
it makes checking and changing easier. A forty-line script does not need ports and adapters.

## Boundaries

Draw a boundary around a decision that is likely to change or a difference worth protecting, so
that the rest of the system does not know it: a storage format, a provider, a pricing rule, a
recovery algorithm. Splitting by steps of execution ("read, process, write") usually spreads one
decision over all the parts.

Several kinds of boundary exist and they need not coincide. Name which one is being drawn:

| Boundary | Separates | Typical price |
|---|---|---|
| Module | Who knows a decision | An interface to keep stable |
| Transaction | What changes atomically | Contention; anything outside it can be seen half-done |
| Process or failure | What stops together | Partial failure, timeouts, unknown outcomes |
| Data ownership | Who may write a fact | Others must ask or hold a possibly stale copy |
| Team ownership | Who decides and who is on call | Coordination for every cross-boundary change |
| Deployment | What is released together | Versions that coexist |

A boundary pays only when the difference it protects is real. A module does not have to become
a service: a process boundary buys independent failure and deployment and costs every difficulty
of distribution. A good first question for any critical change: can it stay inside one
transactional boundary that already exists?

**Deletion test.** Ask what it would take to delete or replace the part: its data, its outside
contracts, the migration, the operations around it. If that is cheap, the boundary is real. Easy
deletion of a file does not prove it.

**Locality.** A reader should understand a behaviour from the place where they look. Many tiny
functions or layers that each do nothing can cost more than one longer function that tells the
whole story.

## Interfaces and client obligations

An interface is everything a caller must know to use the thing correctly: signatures, order of
calls, errors, side effects, limits, timing. A module is deep when a small interface hides much
that the caller would otherwise have to know.

**Client-obligations inventory.** For an interface that matters, list what each caller has to
know or do:

- the order of calls, and what must be closed or released;
- which errors can arrive and what each obliges the caller to do;
- whether a call may be repeated, and under which identity;
- formats, units, limits, and what happens beyond a limit;
- what must be true before the call and what is guaranteed after.

Every item is a cost paid at each call site and a place to get it wrong. Remove items by moving
the knowledge inside, by changing the contract so the case cannot arise, or by making the wrong
use impossible to write.

**Hide the mechanism, not the consequences.** A caller does not need to know how a result is
obtained. It does need to know what its correct use depends on: that the call can take seconds,
can fail half-way, costs money, or may be repeated only with the same identity.

**Design the usage first.** Write the three most common call sites before the implementation.
If they are awkward, no implementation will fix it.

**Accidental contracts.** With enough callers, every observable behaviour gets depended on:
ordering, timing, the text of an error. Before changing one, check who relies on it. Where it is
cheap, keep unpromised behaviour from looking like a promise. This is not permission to break
compatibility that has already formed.

## Comparing alternatives

Compare when a real choice exists, before a commitment that is costly to reverse:

1. Make the alternatives materially different constructions, not variations of one. Include the
   direct change and keeping the current design when they are admissible.
2. Check each against the musts. An alternative that breaks one is out, and its other merits do
   not matter.
3. Walk the same scenarios through the rest: the main use, the next plausible change, and each
   failure scenario that matters.
4. Write the trade-off, not a score: what each gains, what each gives up, who pays.
5. Ask of the leader "why not substantially simpler?" and "what does this make harder?".

No fixed number of alternatives is required. Inventing a second design to satisfy a procedure is
waste; a design nobody tried to beat is a risk. When the interface is what matters, sketch it
twice in different styles and compare the call sites.

## When principles disagree

Each pair below is two good rules with different conditions. Find the condition that applies.

| Tension | Decide by |
|---|---|
| One source of a rule / independence of parts | Do the copies express one decision that must change together, or do they only look alike? Merge the first, keep the second apart. While unsure, wait: a wrong abstraction costs more than duplication. |
| No speculative generality / prepare for change | Is the change confirmed or already repeating? Prepare for that one. Otherwise keep the code easy to change in general and build nothing for the guess. |
| Small functions / local understanding | Can a reader follow the behaviour without jumping? Split where a piece has its own name and meaning, not by length. |
| General / concrete | A somewhat general interface is often simpler than a special one. A framework for cases that do not exist is not. |
| Independent modules / a simple system | Complicating one module is right when it removes more from all its callers and operators than it adds, and the larger blast radius is accepted. |
| Hide complexity / show consequences | Hide how. Show what correct use depends on. |
| No derived state / recovery and idempotency | State that can be recomputed from current inputs is derived. A fact about what happened (a request identity, a past price, an audit entry) is not, and cannot go. |
| Decide up front / learn by building | Decide early what is costly to reverse and what blocks the next safe step. Let reversible things be settled by implementation. A prototype is a legitimate way to answer a design question. |
| Test behaviour / test internals | Do not pin incidental structure. Do check an essential algorithm, an access rule, the absence of a repeated effect and the order of a protocol at the level where they live. |
| Less process / independent check | Add a check where the risk is real and the checker can find what the author cannot. Not by quota. |

## A shared agreement for parallel work

When several people or agents build parts that must fit, they will make incompatible choices
unless the few shared decisions are fixed first. Write only those:

```text
Decision    what is fixed
Scope       where it applies
Prevents    the incompatible behaviour it rules out
Check       how a violation would be noticed
Local       what each part stays free to decide
```

Keep three things apart, in whatever place the project already has for them: the meaning of a
term (glossary), a constraint in force (this agreement), the reasoning behind a choice (decision
record). Do not multiply documents nobody will read; a record of a decision does not show that
the code follows it.
