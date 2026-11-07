## CMP.14 - Compose Interacting Computations through Their Required Observations

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.14:1 - Problem frame

**Use this when** computations that work separately must run together, but shared state, communication or scheduling can change their results. You need to construct their interaction, repair a failing interleaving, or replace a component while retaining the behavior on which the rest relies.

The reader can describe each component's operations and the results expected from their combination. This method adds the shared state, communication and ordering rules needed to reason about the whole. It applies to concurrent algorithms and protocols, including computations performed by cooperating software agents. The implementation language and physical machine supply particular operations and failure conditions.

The first useful result is a composed procedure with a trace or invariant explaining how it obtains the required observation, or a counterexample that identifies the interaction to change. A small shared-state example needs only a few explicit steps. A general guarantee over an implementation needs the corresponding memory, scheduling and failure assumptions.

Use ordinary sequential composition or dependency scheduling when completed outputs suffice and no relevant interference remains. If the algorithms are already adequate and only their physical communication or timing is unresolved, take those requirements to the realization method. An organizational division of work needs its own account of actual roles, capabilities and authority; a computational model can help compare it once that correspondence is established.

### CMP.14:2 - Problem

How can separately useful computations be connected so that their possible interactions produce the required behavior, and what must change when one component's assumptions fail?

Two correct increments can lose an update. Retrying a request can repeat its effect. Individually finite operations can wait forever for one another. A replacement that returns the same final value can expose a different intermediate state to its neighbors. These failures concern the composition, so executing each component alone does not expose them.

### CMP.14:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Local reasoning and interference | A component's facts must survive the environment steps allowed between its own steps. |
| Independence and coordination cost | Isolation can simplify reasoning while synchronization, copying or serialization adds work. |
| Final result and observed history | Calls, replies and intermediate effects can distinguish executions with equal final values. |
| Excluding failure and ensuring progress | An execution can avoid every prohibited state yet never return a required answer. |
| Abstract operation and available primitive | A convenient atomic step requires an implementation or a justified coarser observation. |

### CMP.14:4 - Solution

**Local mantra:** choose the observations; expose the interactions; construct compatible steps; find the failing order or invariant; repair the protocol; establish progress under its actual assumptions.

#### CMP.14:4.1 - Specify what the combined computation must make observable

State the allowed inputs and required results. Include the observations a receiving component can make while work is in progress: returned values, shared-state reads, messages, failures or completed operations. Distinguish a request from each attempt to transmit or execute it when retries are possible.

Choose the required ordering. For a concurrent object, **linearizability** compares a history of calls and responses with legal sequential behavior. A finite history can contain pending calls. Append responses to any selected pending calls, then omit those still pending. Keep every originally completed operation, including its arguments and returned value. Seek a legal sequential order of the retained operations that respects every case where one operation returned before another was called. Each retained operation appears to take effect between its call and response in this extended history.

The appended responses belong to this comparison; they do not establish that the pending operations will actually return. Section :5.4 shows a pending call whose effect another operation has already observed. Other applications may accept weaker order, duplicate-tolerant combination or eventual agreement; use the property the receiving computation needs.

Also state required eventual events, such as a pending operation returning. An acceptable state or finite history does not alone settle that question. In concurrency theory, a **safety property** excludes a violation detectable in a finite execution prefix; a **liveness property** requires progress that no finite delay alone disproves. These meanings describe execution properties here.

#### CMP.14:4.2 - Expose steps, shared state and the environment

Give each component its local state and point of execution. Identify shared variables, owned data, channels and the operations that connect them. For each elementary action, specify when it is enabled, what it reads and changes, and which other values remain unchanged.

Choose the granularity supported by the computational model. A source statement that reads and then writes a value may allow another component's step in between. If a compare-and-swap or transaction is assumed atomic, its availability and scope are part of the construction.

Under an interleaving shared-memory model, form the combined state from the components and shared store, and let an enabled component take one step at a time. Message passing adds channel states and send/receive transitions; rendezvous requires the participating steps together. Include the admitted environment transitions, such as message loss, duplication, restart or input arrival, where the required claim depends on them.

A real language or memory model may permit observations absent from simple interleaving. Recover its ordering and visibility rules before transferring the argument. The method can then change the synchronization or the model instead of concealing the missing premise.

#### CMP.14:4.3 - Derive a compatible invariant or interaction rule

Construct the relation that must survive composition. For example, the shared counter must equal the number of committed increments, a request identifier must have at most one committed effect, or a waiting computation must request only a resource later in an acquisition order.

Establish that relation initially and inspect each allowed transition that can affect it. Local predicates must survive permitted environment steps. **Rely/guarantee reasoning** makes this explicit: a component assumes a stated interference relation from its environment and establishes a stated relation for its own steps. Its neighbors' possible steps must fit that assumption. Check the step-level conditions and their initial basis; mutually assuming that the other component eventually succeeds supplies no initial progress.

For a finite construction, explore enabled interleavings until a failure or the relevant closed state set is obtained. CMP.4 supplies search and CMP.13 supplies a qualified abstraction when the state space is too large. A counterexample should retain enough state and ordering to reproduce the offending interaction.

When operations commute under the observations of interest, exploit that property: some orders can be combined or avoided in exploration. Include intermediate observations in the comparison. Equality of the final store is insufficient if a neighboring read distinguishes the swapped operations.

#### CMP.14:4.4 - Change the interaction that causes the failure

Construct a repair from the failed premise. Common choices have different costs:

| Exposed difficulty | Constructive choice | Cost or condition to retain |
| --- | --- | --- |
| An intervening write invalidates a read | Use an atomic update, or validate the observed version and retry. | The primitive must cover the relevant state; retries have a progress cost. |
| Intermediate state is observed inconsistently | Serialize the affected operation, protect its critical region or publish an immutable result. | Waiting, ownership or retained copies replace the former interference. |
| A repeated message repeats an effect | Identify the logical request and combine effect application with remembering its result. | Identifier lifetime and failure recovery must preserve the relation. |
| Components wait in a resource cycle | Impose a shared acquisition order or another cycle-breaking protocol. | All participating acquisitions must follow the rule; starvation remains a separate question. |
| Coordination costs more than the required consistency is worth | Change the result specification to a weaker observation the receiver can use. | Revalidate the receiving algorithm under that weaker result. |

Execute the original failing trace against the repair, then inspect the transition family that caused it. This both explains the changed behavior and identifies what a more general argument must cover.

#### CMP.14:4.5 - Establish the progress actually promised

Identify what can enable and execute each required next step. A component may wait for another component, a message or a resource. A finite dependency with an available first move differs from a cycle in which every participant waits.

Choose only scheduling and delivery assumptions the intended use can support. **Weak fairness** excludes postponing an action forever once it remains continuously enabled. **Strong fairness** also excludes postponing an action forever when it becomes enabled infinitely often. Name the action or action family: fairness for an entire process does not make every branch of its code fair.

Use those assumptions with a progress measure or a dependency argument. Show why a required response eventually becomes possible and occurs. A bound on elapsed time additionally needs timing and resource bounds. A retry limit provides a finite failure return, not a guarantee that the requested effect happened or that it did not happen.

Test the relevant lost-progress case: an unavailable participant, an indefinitely lost reply, a stopped lock holder or an unfair scheduler. Return the supported result or the unresolved execution status. Do not preserve an eventual-response claim after removing its delivery or scheduling premise.

#### CMP.14:4.6 - Compare replacements through the composed observation

Relate the detailed execution to the promised higher-level operation. Some implementation steps may leave the chosen observation unchanged. That permits a coarser description, but hiding indefinitely many such steps can conceal lost progress; qualify the correspondence accordingly.

For replacement, ask whether the new component introduces an observation the allowed context could not obtain before. Include context interactions, failure and progress when they are part of the required behavior. A final-value comparison is sufficient only for a receiving use governed by that value.

Return the constructed coordination procedure, the result it supports and the assumptions the next user must retain. If a supplier changes its operation, memory rule, failure behavior or response promise, reopen the dependent composition. Use the common result-cost comparison and C.11.DUA when deciding whether another experiment, formal argument or alternative implementation would change the next move.

### CMP.14:5 - Archetypal Grounding

#### CMP.14:5.1 - Two increments need an operation that survives interference

Initially `x=0`. Two components each perform `r=x; x=r+1` once. Reads and writes are atomic, arithmetic uses unbounded integers, but the pair is not atomic. The required final result after both operations is 2.

One admitted execution is:

```text
A reads 0
B reads 0
A writes 1
B writes 1
```

The final value 1 violates the required result. Replace each increment by:

```text
repeat:
    v = read(x)
    if compare_and_swap(x, v, v+1) succeeds:
        return
```

Compare-and-swap tests the current value and, only if it equals `v`, changes it to `v+1` in one atomic action. A failed attempt leaves `x` unchanged.

The invariant is `x = number of successful compare-and-swap actions`. It holds initially; each success increases both sides by one, while reads and failed attempts change neither. Each component returns after its first success. Thus, when both return, `x=2`. A successful action supplies the point at which its increment takes effect in the sequential account.

If A and B both read 0, A can succeed first; B's stale attempt fails. B then reads 1 and succeeds with 2. For these two one-shot callers, each failed attempt is attributable to the other caller's success, so there can be at most one failed attempt before that caller completes. With both callers continuing to receive steps, both finish. A system with an unlimited stream of competing callers needs a different per-caller progress argument.

**Changed condition:** the environment supplies only a separate comparison and write. The old failing order is possible again. Use a primitive that really combines them or protect the read-modify-write region.

#### CMP.14:5.2 - A retry must refer to the same logical operation

A sender requests that a receiver add 5 to a stored counter. Initially the counter is 0. Messages may be lost or duplicated; the receiver continues running and retains its state. The receiver performs the addition, but the reply is lost. Blindly repeating the addition can leave 10 even though the sender requested one increment.

Give the logical request an identifier `k` that is not reused while an old request or reply with that identifier can still arrive. The sender retries the same pair `(k, add 5)`. At the receiver, process the following as one atomic state transition:

```text
if k is already in completed:
    result = completed[k]
else:
    counter = counter + 5
    result = counter
    completed[k] = result
send reply(k, result)
```

Only the state-changing conditional must be atomic; sending the reply can occur afterward. The first request changes the counter to 5 and stores `completed[k]=5`. Every duplicate returns 5 without another addition. The invariant relates a remembered identifier to its one committed effect. It depends on the same identifier denoting the same request payload.

At-most-once effect needs no promise that a message is eventually delivered. To promise a returned answer as well, suppose the sender keeps retrying, delivered requests are eventually processed, and each direction is a fair-loss channel: a message sent infinitely often is delivered infinitely often. The receiver answers each delivered request. These conditions ensure a reply eventually arrives. The result is a delivery-and-processing argument, not a deadline.

**Changed condition:** after applying the effect, the receiver can restart with the counter retained but `completed` lost. A later retry can again produce 10. Preserve the effect and its identifying result together across the admitted failure, for example through a durable atomic state update, or use an operation whose repetition is acceptable. An effect performed by another service needs that service's corresponding guarantee; persisting only the local identifier leaves the effect/record crash gap unresolved.

#### CMP.14:5.3 - An acquisition order removes a waiting cycle

Two computations need exclusive resources `L` and `R`. A obtains L and waits for R; B obtains R and waits for L. Both acquisitions were locally valid, but neither computation can proceed to release its first resource.

Choose one strict total order, `L<R`, and require both computations to acquire L before R. More generally, each computation acquires resources in strictly increasing order and releases them after its finite protected work. It waits only for these resource acquisitions.

A resource-wait cycle would require a strictly increasing sequence of resource positions to return to its starting position, which is impossible. The construction therefore excludes deadlock of this acquisition form. A waiting computation can still be postponed indefinitely by unfair grants. A starvation-freedom claim additionally needs a suitable grant policy and progress by holders; a bounded waiting time needs further bounds on their work and scheduling.

**Changed condition:** introduce a callback while holding R that tries to acquire L. This violates the shared order and can restore a cycle. Move the callback outside the protected region or redesign the acquisition protocol and its argument.

#### CMP.14:5.4 - Include an observed effect of a pending call

An initially empty FIFO queue has this history: A calls `enqueue(7)` at t=1; B calls `dequeue()` at t=2 and receives 7 at t=3; A has not returned by t=4. Comparing only completed operations would leave a dequeue from an empty queue.

For the comparison, append A's response at t=5. The sequential order `enqueue(7); dequeue() returns 7` is legal. For example, their effects can be placed at t=1.5 and t=2.5, within their call/response intervals. This is a witness for the finite history; it supplies no promise that A will eventually respond in the actual execution.

If there is no enqueue call at all, appending responses cannot invent one: a dequeue returning 7 from the empty queue remains invalid. If A instead returned at t=2 before B called at t=3, the sequential order must keep A before B. Pending-call completion thus preserves both the observed values and the order already imposed by completed calls.

### CMP.14:6 - Bias-Annotation

Sequential intuition can hide an interleaving between a read and its use. An atomic-looking API can hide a smaller implementation primitive. A successful retry demonstration can hide the uncertainty introduced by a lost reply or restart. Recover the actual transitions and observations before assigning the result of a simpler model to them.

### CMP.14:7 - Conformance Checklist

- The combined result includes the intermediate observations and eventual responses its user needs.
- The model states atomicity, visibility, communication and admitted environment changes where they affect the argument.
- Initial conditions and each relevant component or environment step support the shared invariant or protocol relation.
- A proposed repair changes the offending interaction and its general transition family.
- Progress uses named scheduling, delivery and failure assumptions; a finite timeout has its own qualified outcome.
- A replacement preserves the observations and progress required by its receiving context, with physical realization checked where that correspondence matters.

### CMP.14:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Failure | Useful repair |
| --- | --- | --- |
| Compose isolated correctness results | Another component invalidates a locally established fact. | Test the permitted interference against that fact. |
| Treat a read-modify-write statement as indivisible | Interleaving can lose an update. | Construct or justify the required atomic operation. |
| Infer failure of the effect from a missing reply | The effect may have happened before the reply was lost. | Identify the logical request and recover its result. |
| Infer eventual response from absence of a bad state | All participants may keep waiting. | Establish an enabled progression and its fairness conditions. |
| Assume each component progresses because the other does | The circular assumptions may admit no first move. | Derive progress from initial enabling and justified dependencies. |
| Hide a changed memory or crash model in an implementation detail | The former permitted executions no longer cover the implementation. | Reconstruct the affected interaction and preservation argument. |

### CMP.14:9 - Consequences

The reader can construct an interaction protocol, locate a failed order, and explain which whole-computation property follows. An invariant, counterexample or progress argument supports division of algorithmic work while exposing the assumptions shared across components.

Coordination can add waiting, retries, retained state or stronger primitives. Sometimes changing the required observation admits a cheaper useful composition. The improvement is conditional on the receiving computation accepting that changed result.

### CMP.14:10 - Architectural Rationale

Mathematical composition supplies an operation for combining descriptions. Computational composition must also establish how the resulting process runs and what other processes can observe. Interference makes a component's admissible context part of its meaning.

The counter, retry and resource-order cases construct three different repairs: conditional atomic change, identity across repeated communication, and removal of cyclic acquisition. Their shared method is to expose the missing interaction, construct the coordinating steps and retain separate arguments for allowed histories and progress. Modeling a working Method with these operations can sharpen a methodological comparison, but the modeled operations still need a justified correspondence to the actual work.

### CMP.14:11 - SoTA-Echoing

How should local computations be combined without losing the required whole behavior? **Adopt** the separation of state/action description, refinement, progress and environment-dependent composition in Lamport's [*A Science of Concurrent Programs*](https://lamport.azurewebsites.net/tla/science-book.html), chapters 3, 4, 6 and section 8.2. It supports :4.2–4.6. Its composition discussion exposes the circularity of proving each component's eventual success by assuming the other's. A direct global invariant remains a serious simpler choice for small interacting systems; a component proof becomes useful when its explicit environment assumptions reduce repeated reasoning. The accepted cost is recovering those assumptions. Changes in observed behavior or progress premises reopen the choice.

When reasoning about a concurrent implementation by using an abstract atomic specification, **adapt** the composition-sensitive account in [Oliveira Vale, Shao and Chen](https://flint.cs.yale.edu/flint/publications/ctlinear-jacm.html). It relates linearizability, locality and observational refinement through explicit composition operations. For the observation and replacement questions in :4.1 and :4.6, identify the client context and establish that its observations with the implementation are permitted by the abstract specification. The specification may permit additional behavior. A short history/linearization-point argument is sufficient for :5.1; the richer algebra is useful when it reduces actual composition-proof work. It does not automatically preserve progress or supply an implementation. A new interaction context can reverse the choice.

Which interference may a component assume? **Adopt** the memory-model parameterization demonstrated by [Lahav and colleagues' rely/guarantee treatment of causally consistent shared memory](https://arxiv.org/abs/2305.08486) as a boundary on :4.2–4.3. Sequential interleaving is a convenient comparator, while weaker visibility needs a compatible semantics and reasoning rules. Retaining the simpler model is justified when the implementation supplies its conditions. Otherwise synchronization, the algorithm or the claimed observation must change.

When restart is admitted, **adapt** the explicit crash-aware observation in [*Linearizability with Crashes*](https://flint.cs.yale.edu/flint/publications/crashlin.html) for :4.2 and :5.2. A no-crash history can omit the retained-state distinction that recovery needs. A durable coordination protocol accepts persistence and recovery costs; accepting an uncertain result or an idempotent effect may be a cheaper suitable rival. The framework distinguishes forms of crash-aware correctness. Change the failure model or the effect's location and reconsider the corresponding claim.

### CMP.14:12 - Relations

- **MATH.17 and MATH.18:** supply composition of operations and interpretation between accounts; this method constructs their interacting computational execution.
- **CMP.3 and CMP.10:** supply dependency scheduling and data representations; interference can change the operations those representations must support.
- **CMP.4 and CMP.13:** supply exploration and qualified abstraction for the composed state or trace system.
- **CMP.12:** supplies interpretation and behavior-preserving translation when the component's executable description changes.
- **C.29.2 and C.29.3:** supply computational formulation and realization, including whether the modeled primitives and resource conditions are available.
- **C.11.DUA:** governs the worth of stronger analysis or testing for the proposed use.

### CMP.14:End
