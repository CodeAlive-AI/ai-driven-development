## SYSE.40 - Protect Software Platform Capacity and Isolate Failure

> **Status:** Stable

> **Normativity:** Guidance within the stated software capacity-protection use; examples are illustrative.

### SYSE.40:1 - Problem frame

Use this pattern when bursts, expensive work or a failing dependency prevent other users from obtaining supported platform results. Start with the constrained resource and the workload classes consuming it, including the control and recovery work needed to keep the service operable.

The first result is a tested capacity-protection arrangement for a stated operating envelope, or the proposed envelope and the conditions whose qualification is missing. The arrangement includes admission, bounded waiting, separation, deadline/retry limits and useful rejected or degraded outcomes.

If ordinary demand already fits a qualified envelope and no consequential coupling exists, use that arrangement. If an active failure needs immediate mitigation, use SYSE.38. Continuing allocation of operating work remains an operating responsibility; this pattern engineers the means and limits.

### SYSE.40:2 - Problem

Requests with the same name or arrival rate can consume very different CPU, memory, storage, connection or worker resources. A long queue can hide overload until every accepted task misses its useful deadline. Retries can multiply demand while the original work is still running.

Adding capacity may not repair a serial bottleneck, a downstream limit or a failure that affects every new instance. Likewise, protecting a front-end proxy does not automatically protect its upstream service or preserve the user's task.

### SYSE.40:3 - Forces

| Force | Practical tension |
| --- | --- |
| Utilization and isolation | Sharing resources is efficient until one class prevents another from completing. |
| Admission and user outcome | Rejecting early can preserve useful work while still being a failed attempt for the rejected user. |
| Waiting and usefulness | A queue smooths short bursts but can retain work that is no longer worth completing. |
| Recovery and amplification | Retry can recover a transient failure or intensify pressure and duplicate effects. |

### SYSE.40:4 - Solution

#### SYSE.40:4.1 - Recover demand, resource limits and failure coupling

Identify supported task classes, their demand patterns and the resources they consume through the path. Include costly variants, concurrency, fan-out, dependencies and resource use during failure, not only average successful requests.

Measure the relevant resource constraints directly where possible. A requests-per-second figure can be useful for a stable workload but cannot stand in for changing request cost. Distinguish available capacity from a configured limit and from a provider's promised future supply.

Locate shared failure effects. Heavy tests may occupy the workers needed for release control; retrying clients may overload a recovering dependency; the monitoring or cancellation path may depend on the same exhausted pool. Determine which useful work must remain available under the selected failure.

#### SYSE.40:4.2 - Choose the protected envelope and alternatives

Compare additional capacity, reduced offered work, a cheaper qualified result, per-user or workload isolation, and redesigning the execution path to remove an identified serialization point. Autoscaling is one possible mechanism; its start delay, quotas, dependency capacity and failure behavior remain conditions.

Choose a bounded demand/resource envelope and the supported degradation outside it. Obtain the actual authority for priority and resource trade-offs. A technical queue cannot decide by itself which users may be delayed or refused.

Define the useful outcome for rejected, delayed or degraded work. Preserve the distinction between an accepted task, a refusal before effects, an unfinished task and a partial result. Do not count overload rejection as user success merely because it protects the service.

#### SYSE.40:4.3 - Construct admission and bounded waiting

Admit work only under the selected resource and concurrency limits. Bound queues or waiting by the conditions that preserve task usefulness, including deadlines and cancellation behavior. Account for the resources consumed merely by holding or rejecting a request.

Separate workload or user classes where their coupling would violate the protected use. Reserve or independently provide control, health observation and recovery capacity when that is necessary. Verify that a shared downstream resource does not invalidate the apparent isolation.

Expose a useful response when work cannot be admitted. Give the user enough information to distinguish a refused attempt from one that may already have effects. A retry indication must reflect the qualified path, not encourage an immediate synchronized retry storm.

#### SYSE.40:4.4 - Bound retry and dependency failure

For each retrying layer, know the operation's replay behavior, deadline and attempt identity. Reconcile uncertain effects before repeating a state-changing operation. SYSE.34 and SYSE.41 supply the relevant data and runtime boundaries.

Bound the aggregate retry amplification across layers, not only each local loop. Delays and jitter can spread attempts but do not make an unbounded retry policy finite. Stop work that can no longer produce its permitted result rather than spending resources until an outer timeout hides it.

Protect both the component receiving pressure and the dependency receiving calls. A local resource monitor, a dependency concurrency limit and a fallback can address different failure mechanisms. Do not treat one control's existence as proof that the whole path is protected.

#### SYSE.40:4.5 - Exercise overload, isolation and recovery

Test representative ordinary demand and the bursts, expensive variants or dependency slowdowns/failures that can defeat the claimed operating envelope, within a safe permitted environment. Observe accepted, rejected, delayed and partial task outcomes as well as resources.

Verify that the protected class still obtains its qualified result, queues stay bounded, and other tenants or downstream Systems are not made worse in an unaccepted way. Check the control/observation path under pressure; repair the arrangement if its state cannot be observed or admission cannot resume under the selected recovery conditions.

Then reduce pressure and verify recovery. Ensure queues drain usefully, admission resumes appropriately and clients do not overwhelm the recovering service. A lower resource chart alone does not show that users can work again.

Return the exercised envelope, chosen limits, response behavior and remaining blind spots. Use SYSE.36 to retain user-visible failure and delay in measurement, and SYSE.38 for unresolved active failures.

#### SYSE.40:4.6 - Derive limits from useful work and check the recovering system

Develop a capacity model at the bottleneck that the task can actually reach. For a reasonably stable task class, measure resource demand per completed task and its variation, then combine it with the anticipated arrival and concurrency pattern. Distinguish sustained demand from a burst and include service time while a dependency is slow. A mean CPU cost can help estimate a baseline; it does not bound a costly tail or a separate memory, connection or storage constraint. Establish which resource becomes limiting under each relevant workload mix.

Use those observations to choose headroom and an admission rule. Headroom covers selected variation and failure conditions, such as one worker unavailable or a dependency taking longer to respond. It is not a universal percentage. A limit based on active concurrency can protect a connection pool better than a request-rate cap when calls become slow. A rate cap can protect a service from excessive arrivals even when each finishes quickly. Some paths need both, together with a bounded waiting population. Follow the request into shared dependencies before concluding that either local limit is sufficient.

Relate waiting to the task's remaining useful time. In a simple single-class example, two dedicated workers complete each job within a qualified two-second bound and have no hidden downstream wait. Four queued jobs behind two just-started jobs can complete in three waves, by six seconds. If the task must finish within five seconds from admission, accepting all six cannot guarantee that bound: when each job uses the permitted two seconds, the last pair is late. Reduce accepted work, shorten qualified service time, add usable capacity or change the promise with its holder. If service time is only an average, this deterministic bound is unavailable; qualify a probabilistic or observed service objective instead.

Compare strict reservation with borrowing deliberately. Strictly separate pools make a protected class easier to reason about but can leave capacity idle. Borrowing can improve utilization if the protected class can reclaim sufficient capacity within its response bound. Non-preemptible long jobs can make that reclaim promise false. Separate execution pools also do not separate a shared database lock, network limit or provider quota. Choose the mechanism at the actual point of interference, including priority propagation where the downstream system supports it.

Design admission and recovery as one feedback arrangement. When measured pressure rises, reduce offered work soon enough to preserve the selected useful tasks. When it falls, resume in a way that does not immediately recreate the overload. Hysteresis, a gradual increase or a limited trial population can prevent rapid oscillation, but each needs a trigger and observation appropriate to the mechanism. Autoscaling can provide later capacity without protecting the interval before new workers are ready; a scaling request is not available capacity.

Extend the two-worker example with a constructed recovery trace. Each job can still complete within two seconds, including dependencies and result delivery; scheduling is FIFO, and the admission gate's acceptance and completion records are current. At second 0, four jobs are accepted and admission pauses: two start immediately and two queue. An empty-system observation sampled at second −1 arrives at second 1 because resource reporting takes two seconds. At second 1, six clients whose earlier requests were refused before effects return with original task deadlines at second 6. The gate admits or refuses this burst by second 1.1 using separately qualified control capacity. If the controller reopens admission for all six from the stale observation, jobs taking the permitted two seconds finish in pairs at seconds 2, 4, 6, 8 and 10. The last four newly accepted jobs miss both their original deadline and the five-second bound from admission.

Instead, use the current accepted work and its remaining service bound to admit at most two of the six in this recovery trial. The gate enforces that total across the simultaneous arrivals and closes the trial after those acceptances; the other four receive refusal before execution effects. The earlier jobs finish by seconds 2 and 4; the admitted new pair finishes by second 6, within five seconds of admission and its original deadline. In that same two-second history, at second 4 even the next pair queued behind the still-accepted pair has a completion bound of second 8. The four refused tasks with original deadline 6 therefore cannot be readmitted on that basis. A later trial can serve other offered work only if its remaining useful time fits.

If one worker becomes unavailable during the trial, the two-worker calculation no longer supplies the promised bound. Stop further admission and identify the affected accepted tasks for recovery through SYSE.38; preserving their deadlines now requires another feasible arrangement.

Keep the service accountable for the resulting user outcomes. A cheaper response counts as a good degraded result only if that meaning was agreed for the task; stale data can be acceptable for one display and unacceptable for another. Expiring a queued task does not cancel an effect that has already begun. A recovery exercise must show both restored new-task admission and resolution or explicit limitation of earlier accepted work. Track retries and resumed demand during that exercise: a healthy idle service can fail as soon as all waiting clients return together.

When ParcelWorks adds a test class with much larger memory demand, the six-heavy-slot arrangement may cease to be safe even though the job count is unchanged. Introduce the relevant memory bound or a distinct class, qualify its effect on the shared dependency, and reconsider the accepted waiting population. Preserve the control reservation only if it still protects the actual end-to-end control task. This gives a concrete change rule for the capacity model rather than a permanent significance to the example's six-and-two split.

### SYSE.40:5 - Archetypal Grounding

A constructed ParcelWorks platform has eight execution slots. Long test jobs can occupy all eight, preventing short delivery-control tasks from running. The current question is how to preserve a bounded control path under a test burst, not how to maximize average worker occupancy.

The team first qualifies the resource demand of the supported test and control classes. It finds that the relevant slot isolation can be implemented, while database and artifact-store limits still require separate observation. The following numbers illustrate the chosen admission construction.

The candidate reserves six execution slots for heavy tests and two for control work. Waiting is bounded at twelve heavy tasks and four control tasks, subject to the task's remaining useful deadline. A class does not silently borrow the other's reserved execution capacity in this construction. For the following admission-count illustration, all requests meet the class, access and remaining-deadline conditions; timing qualification is a separate question below.

| Simultaneous burst into an initially empty arrangement | Running | Waiting | Refused before execution |
| --- | --- | --- | --- |
| 20 heavy test requests | 6 | 12 | 2 |
| 8 control requests | 2 | 4 | 2 |

The counts close the admission example: eighteen heavy and six control requests are accepted, while four requests receive explicit refusal without execution effects. The total of eight running tasks respects the slot limit. A refusal is not counted as a successful developer task.

The control queue is not a guarantee that all six accepted control requests will finish in time. Their task-duration/dependency envelope and remaining deadlines must be exercised. If that qualification fails, reduce admission, provide capacity or change the service promise; a short queue alone does not establish responsiveness.

For ordinary load, representative tasks complete and their results are observed. Under the burst, control work still has its reserved slots while the heavy class reaches its own limit. If all control tasks nevertheless block on an exhausted shared database connection pool, the apparent isolation fails at that downstream resource and the arrangement must be revised.

In a second adverse history, a client times out while a deployment may already have changed its target. The retry policy first queries the existing attempt. It does not treat every timeout as a refusal with no effects. Only a qualified repeat is allowed, with a bounded total attempt budget across client and service layers.

To make the cross-layer bound concrete, suppose one user attempt permits at most three service invocations and each invocation at most two downstream calls, counting initial calls in both limits. Independent local caps can therefore produce 3 × 2 = 6 calls to the constrained dependency. In the alternative construction, every invocation for that same attempt identity shares four downstream-call units and a ten-second deadline measured from the original entry; neither allowance resets on an outer retry. Each call must obtain one unit from the common allowance before it is sent. If otherwise qualified repeats use two calls in the first invocation and two in the second, no unit remains for a third invocation's downstream call. Waiting and backoff also spend the common time; do not start a call that cannot fit the qualified remaining-time rule, and do not mistake the deadline for proof that earlier work has stopped. If the second state-changing call has an unknown effect, stop replay with two units still available and recover its state. These counts and times are illustrative bounds, not universal settings or evidence of response-time qualification.

After pressure falls, the test verifies that waiting useful work completes, expired work is resolved according to its rule, and admission resumes without a synchronized flood. Observation and recovery operations must themselves remain available.

An implementation comparison is Envoy's [overload-manager architecture](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/operations/overload_manager.html): it connects resource-pressure observations to configured actions protecting the proxy. Its own-resource protection is distinct from upstream circuit breaking. The linked latest/development documentation is not a pinned production configuration; the deployed edition and actual monitors/actions need separate qualification.

What changes in practice is that accepted work and overload responses have explicit bounds, and one workload cannot be assumed isolated merely because it has a different queue name.

### SYSE.40:6 - Bias-Annotation

Average throughput can conceal expensive requests and a small class losing all service. A provider can also report a healthy system after rejecting most users. Inspect task outcomes by relevant class, including recovery/control work, and retain the cost of reserved or unused capacity.

### SYSE.40:7 - Conformance Checklist

- The constrained resources and workload/failure conditions are identified.
- The protected envelope and priority trade-offs have an actual basis and holder.
- Admission and waiting are bounded by capacity and task usefulness.
- Isolation includes consequential downstream and control-path dependencies.
- Any retry mechanism has a qualified effect model and aggregate amplification limit.
- Rejected, delayed and degraded work remains visible as its actual user outcome.
- Ordinary use, overload and recovery are exercised before relying on the envelope.

### SYSE.40:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| Size everything by average requests per second. | Inspect actual resource cost and supported expensive variants. |
| Add an unbounded queue to avoid rejections. | Bound waiting and expose work that cannot finish usefully. |
| Assume autoscaling solves a shared dependency limit. | Qualify the bottleneck and the time/capacity available to scale. |
| Retry at every layer until the task succeeds. | Reconcile effects and bound total retries, deadlines and offered load. |

### SYSE.40:9 - Consequences

Capacity protection can preserve useful service during pressure and make refusals more intelligible. It can reduce peak utilization, require reserved resources and expose an inadequate service promise. Isolation has a maintenance and cost burden; additional capacity or reduced demand may be the better choice for a particular envelope.

### SYSE.40:10 - Rationale

Overload is a relation between offered work, its resource cost and the available means of completion. An arrival-rate or component-health limit protects the task only when it controls the relevant resource demand and preserves the required completion. Bounded admission, separation and replay behavior preserve a meaningful task result or an explicit refusal when unlimited service is impossible.

### SYSE.40:11 - SoTA-Echoing

For resource pressure, **adopt and adapt** the developed 2016 [SRE Handling Overload](https://sre.google/sre-book/handling-overload/) treatment. Resource-sensitive demand, quotas, client throttling and differentiated criticality are already professional capabilities. Sections 4.1–4.6 connect those choices to useful task deadlines, retained effects and recovery of accepted work; they do not replace the service's workload model with universal limits.

**Compare** the chosen controls with Envoy's [overload-manager architecture](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/operations/overload_manager.html) and [configuration](https://www.envoyproxy.io/docs/envoy/latest/configuration/operations/overload_manager/overload_manager) when that mechanism is used. Local proxy protection differs from upstream protection. Strict reservation, reclaimable borrowing, extra capacity and reduced demand have different utilization and response consequences.

Reopen the envelope when request cost, workload mix, shared dependencies, retry layers or deployed mechanisms change. Latest documentation is not qualification of an installed version; a burst count alone is not a task-deadline guarantee.

### SYSE.40:12 - Relations

SYSE.26 defines the supported task result, SYSE.33 supplies controlled exercise conditions, and SYSE.36 measures rejected/delayed work. SYSE.38 handles active failure. SYSE.34 and SYSE.41 qualify state-changing recovery. SYSE.24 compares whole obtaining alternatives when capacity changes that larger choice; operating allocation remains with the relevant OPS work.

### SYSE.40:End
