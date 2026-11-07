## OPS.10.1 - Construct and Compare Operating Capacity Models

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative

### OPS.10.1:1 - Problem frame

**Use this when** a capacity decision has a service question and an operating arrangement, but the calculation needed to compare its alternatives is missing or misleading. A faster machine produces longer queues. Two staffing plans have the same average hours but different completion risks. A workload controller changes an aggregate smoothly while the customer is waiting for one complete order.

Model how the available resources produce the required result, then calculate the consequence of each proposed change. Keep the arrival, service, resource and completion meanings attached to the quantities. The result can be a finite schedule, an obstruction, a mean estimate, a conditional probability or a useful bound.

**First useful move.** Select one result and its time criterion. Recover who or what must serve it, what is already waiting and what prevents the next service from starting. A resource-time shortfall may settle the question immediately.

The reader needs to interpret rates, durations and elementary probability for the branches used. A practitioner can obtain a specialist calculation while retaining the operating assumptions and result interpretation. Use an adequate existing model directly; reconstruct it when a changed resource, arrival process or question invalidates a needed relation. OPS.10 selects the wider capacity/service decision. This method develops the model used in that decision.

### OPS.10.1:2 - Problem

Dividing mean demand by nominal capacity suppresses the arrangement that makes service possible. It can hide shared attention, interrupted availability, burst arrivals and visits that fail to produce a final result. A mean waiting-time formula can then be used to promise a deadline it never calculated.

At the other extreme, a full simulation can consume effort while leaving a simpler decisive bound unused. The difficulty is to model enough of the service process to answer the question and identify which assumption or relation needs revision when the model is insufficient.

### OPS.10.1:3 - Forces

| Force | Practical tension |
| --- | --- |
| Amount and timing | Enough total resource time may exist, yet be unavailable when a job needs it. |
| Detail and useful consequence | A richer model can retain a lost dependency, but also cost more to build and maintain. |
| Average performance and individual service | A mean can compare recurring load without determining a completion probability or hard deadline. |
| Local change and shared work | Speeding one activity can move waiting or consume a resource needed elsewhere. |

### OPS.10.1:4 - Solution

Model how work arrives, uses resources and reaches completion. Calculate each alternative against the same service question. If an assumption fails, revise it and the results that depend on it. Enter at a later step when its inputs are already adequate.

#### OPS.10.1:4.1 - Define the completion question and its clock

Choose the operating population, arrival event, completion event and horizon. Keep an order, its visits and its accepted result distinct. For each alternative, measure customer waiting from the same event unless the question concerns that starting event.

State the output needed: all listed jobs finished by a date; a mean residence time in a continuing regime; a fraction completed within a duration; a probability under a specified model; or protection against a stated disturbance. Recover the initial unfinished work and its remaining requirements. A system started empty is a different input from a busy operation observed halfway through a shift.

For example, “the two jobs need four hours on average” does not yet answer “with what probability will both be complete by hour four?” Section 5.2 constructs both answers from the same service assumptions.

#### OPS.10.1:4.2 - Construct usable service and a first load bound

Use the operating model to identify the resources needed by each activity, including simultaneous needs. Recover usable calendars, capabilities, access, setup, interruption, restart and return rules. An unattended machine interval may occupy the machine while releasing its operator.

For a finite horizon, sum the required remaining occupancy separately for each resource. Compare it with the time in which that resource can perform this work. If the requirement exceeds that time, the proposed completion is impossible under those inputs. If it fits, timing, precedence or resource compatibility may still prevent a schedule.

For recurring demand, a useful first load expression is:

```text
resource demand per unit time =
    sum over arriving classes of
    (class arrival rate * expected resource time used by one arrival)
```

Expected resource time includes the modeled visits, setups and recovery attributable to that arrival. A return may require another visit without producing another delivered order. If return behavior depends on congestion or policy, recover that dependence before reusing the old expectation.

Divide this demand by the usable resource time supplied per unit time to obtain an offered-load ratio. It can exceed one: the work offered exceeds that capacity. The observed fraction of time busy remains at most one. Both measures can be useful, but they answer different questions.

Define service time for the chosen server. Include an interruption in effective service when the model treats it as extending that server's service; otherwise represent the unavailable interval separately. Count its loss once. Waiting for another team or for permission is not automatically occupancy of this server. A batch's shared machine time is also different from the sum of its parts' elapsed times. OPS.11.1 and OPS.15.1 supply these resource and event constructions.

#### OPS.10.1:4.3 - Build the finite or changing-regime account

For a continuously available single server, first-come service, known arrivals and service durations, construct each start and finish in arrival order:

```text
start[i]  = max(arrival[i], finish[i-1])
finish[i] = start[i] + service[i]
wait[i]   = start[i] - arrival[i]
```

The initial finish represents the server's remaining occupied time; it is zero for an empty system available at zero. This recurrence obtains the earliest schedule under that fixed policy. It does not choose a better job order.

When a job needs an uninterrupted usable interval, replace the proposed start by the first interval that fits its duration and required resources. If work can pause, account for the work completed before each interruption and the permitted restart, including lost setup or recovery. Construct precedence and resource choices explicitly when several activities interact. OPS.10.2 develops this finite schedule, including calendar windows and conditional time reserve. A feasible candidate demonstrates its own schedule; a failed search does not demonstrate that all schedules fail.

For a changing regime, begin with the actual initial state and advance arrivals, completions, failures, returns and control actions using their event rules. A model of continuous aggregate quantities can use fewer variables when amounts and rates are the required outputs: write its accumulation balance and the rule that determines outflow. Retain any capacity, nonnegativity and delay constraints of that rule. Section 5.3 shows why a proportional outflow and a constant service rate give different completion accounts.

A feedback policy can be part of either an event or continuous model. Its requested capacity change must correspond to an obtainable operating change, such as an available shift, machine setting or additional resource.

#### OPS.10.1:4.4 - Construct a continuing-regime mean when that is the question

First establish the modeled regime: arrival process, service order, number of servers, availability, initial transients, return behavior and relevant dependence. Long-run parameters do not describe an arbitrary finite overload merely because their units fit.

For one continuously available first-come server, consider independent, identically distributed interarrival intervals and independent, identically distributed service times, with the two sequences independent. Let `lambda` be the arrival rate, `E[S]` the mean service duration and `rho = lambda * E[S]`. With finite second moments and `rho < 1`, a useful two-moment approximation is:

```text
mean queue wait ≈ ((ca² + cs²) / 2) * rho / (1-rho) * E[S]
mean residence  ≈ mean queue wait + E[S]
```

Here `ca²` is interarrival variance divided by squared mean interarrival time; `cs²` is service-time variance divided by squared mean service time. The factor `rho/(1-rho)` retains the sharp rise near saturation. Both arrival and service variation matter.

Use this as a qualified mean calculation under those premises. In the Poisson-arrival case, the displayed mean wait equals the established single-server result for a general independent service distribution with finite second moment. Section 5.1 uses that special case. Neither use supplies a wait percentile.

Temporal dependence can defeat a description consisting of two moments. Count arrivals in windows at time scales relevant to the queue; examine whether their variance relative to mean changes with window length. Retain that dependence in a richer queue model or in simulated arrival paths when it can change the choice. Dispersion-based queueing analysis supplies one such mean-performance alternative; it retains its own stationarity and service assumptions.

Do not substitute the one-server formula after pooling servers, adding priorities, introducing blocking or changing the dependence. Reconstruct the model of service. A deterministic arrival every hour and a one-hour uninterrupted service can operate continuously without a queue; its feasible timing is not invalidated by a stochastic formula singular at `rho = 1`.

#### OPS.10.1:4.5 - Obtain the needed probability or protective bound

For a finite probability question, specify the joint uncertain inputs, initial state and operating policy. When a policy adapts during execution, base each choice on information available at that time. Separate schedules chosen after each complete outcome is known do not establish one policy that can be executed. When there are few combinations of uncertain inputs, enumerate them; otherwise generate paths from that joint model and apply the event rules to each path. For each path, test the stated service predicate, such as both named orders complete by hour four. Aggregate by the paths' probabilities, or estimate the probability with the sampling uncertainty needed by the decision. MMP.7, MMP.13 and CMP.9 supply observation, inference and sampling methods when those contributions are needed.

Preserve dependence between arrivals, service durations, outages and returns. Equal marginal means or distributions do not make different joint models equivalent. Section 5.2 changes only service dependence and changes the probability while preserving the mean completion time.

A scenario without probabilities supports a conditional consequence. A family of bounded disturbances can support a protective bound if the response is shown to work for every disturbance in that family. One successful replay supplies only its case. A mean replenishment time multiplied by a consumption rate gives no such worst-case or probability statement by itself.

Include the starting backlog and horizon for a transient service question. Use a continuing-regime mean only for the mean question it answers. For an empirical claim, interpret source coverage and input/model uncertainty as well as calculation or sampling error. Obtain another observation only if the unresolved difference can alter the receiving decision.

#### OPS.10.1:4.6 - Compare operating changes and return their consequences

Change the modeled mechanism of each alternative: service requirement, resource access, setup, interruption, release, route or policy. Recalculate the affected consequence while preserving unaffected inputs and the common service question.

Compare the relevant results separately: completion, waiting, resource demand, cost, burden and recovery. Use the existing finite-comparison or portfolio methods when these consequences compete. A faster nominal operation can lose to a more predictable one on mean residence, yet remain preferable at another arrival rate or cost.

Distinguish waiting moved before admission from service made faster by reduced interference. The first can improve an internal measure without earlier delivery; the second needs the changed service mechanism in the model. Return the result to admission, release/protection or commitments together with the conditions that can change it. A modeled resource does not establish that it has been provided or authorized.

Stop with the answer the decision needs: a usable alternative, demonstrated shortfall, sufficient bound or an identified unresolved relation. Reopen the affected calculation when arrivals, mix, service, access, dependence or the requested service criterion changes.

### OPS.10.1:5 - Archetypal Grounding

#### OPS.10.1:5.1 - A slower machine gives a better mean, within its capacity

Jobs arrive as a Poisson process at one job per three hours. A continuously available first-come machine serves one job at a time; its service durations are independent across jobs and of arrivals. Service includes all job-specific recovery. There is no other setup, loss, resource or return. These are constructed alternatives.

Machine A takes one hour with probability 0.9 and eleven hours with probability 0.1. Its mean service is two hours, its variance is nine squared hours and `cs² = 2.25`. Machine B always takes 2.2 hours, so its service variance is zero. Poisson arrivals give `ca² = 1`.

| Result | A | B |
| --- | ---: | ---: |
| Mean service, hours | 2 | 2.2 |
| Offered-load ratio | 2/3 | 11/15 |
| Mean queue wait, hours | 6.5 | 3.025 |
| Mean arrival-to-completion time, hours | 8.5 | 5.225 |

For example, A's mean wait is `((1+2.25)/2) * ((2/3)/(1/3)) * 2 = 6.5`. The special-case mean relation applies to these stated service laws. B has the larger mean service duration and higher load ratio, yet the smaller mean residence. Its absence of service variation changes the queue consequence.

If the decision needs a mean residence below six hours, B meets that modeled criterion and A does not. Cost and actual availability still affect the operating choice.

Change the arrival rate to 0.48 jobs per hour. A's mean service rate is 0.5 and B's is about 0.455. A has load ratio 0.96, while B has 1.056. The former comparison cannot justify B for that continuing arrival regime. Return the increased demand to capacity or admission instead of inserting a ratio above one into the steady-mean formula.

#### OPS.10.1:5.2 - Four hours on average, with a missed-deadline risk

Two independent jobs are ready at time zero. One server processes them in fixed order without interruption. Each service takes one or three hours with probability one half, independently of the other service. Both jobs must be complete by hour four.

| Service durations, hours | Last completion, hour | Probability | Both complete by four? |
| --- | ---: | ---: | --- |
| 1, 1 | 2 | 1/4 | Yes |
| 1, 3 | 4 | 1/4 | Yes |
| 3, 1 | 4 | 1/4 | Yes |
| 3, 3 | 6 | 1/4 | No |

Mean last completion is four hours; the probability of meeting the deadline is three quarters. Replacing both durations by their mean of two hours would produce a single on-time schedule and discard that risk.

An additional independent server capable of the same work would allow both to start at zero and finish by three in every listed case. That is a conditional alternative; obtaining it is another operating action. Without it, a deadline of six covers all cases in this bounded model.

Now keep both marginal service distributions but make their durations equal, perhaps because a shared job condition affects both. The only outcomes are (1,1) and (3,3), each with probability one half. Mean last completion remains four; deadline probability falls to one half. The changed dependence reopens the probability result without changing the two means.

#### OPS.10.1:5.3 - An aggregate curve and a completed job

A controller represents remaining workload `q` in job-equivalents, starting at one with no new arrivals. Its assumed output rate is `k*q`, with `k = 1 per hour`. The balance gives `q(t) = exp(-t)`: after one hour, about 0.368 job-equivalents remain. This model can support an aggregate regulation question where that outflow law fits.

A different operating account says one indivisible job takes exactly one uninterrupted hour on the available resource. Its completion event occurs at hour one. A constant-rate fluid balance, stopped at zero, also gives `q(t) = max(1-t,0)` in job-equivalents, but its intermediate fractions do not make the actual job partially delivered.

Even the exponential curve permits another interpretation under different premises. For one exponentially distributed service duration with mean one hour, it is the expected number of unfinished jobs; completion by one hour then has probability about 0.632. It is not a deterministic promise.

The practitioner chooses the account by the receiving question and the operating service law, not by whether the display uses a curve or discrete events. For the fixed one-hour deadline, use the completion event. For aggregate feedback, establish the outflow relation and how a commanded rate change can be realized. A new capacity setting without a corresponding operating mechanism leaves the proposed intervention unsupported.

### OPS.10.1:6 - Bias-Annotation

Nominal speed attracts attention because it is easy to compare. Section 5.1 keeps recovery variation and queue consequences visible. A smooth trajectory can be equally persuasive: section 5.3 recovers what the curve represents before interpreting it as a completed result.

A familiar formula can survive after its regime disappears. Reconstruct the changed arrival, service or dependence relation rather than preserving the number merely because the formula still accepts the inputs.

### OPS.10.1:7 - Conformance Checklist

1. Are the completion event, clock and service criterion clear before the calculation?
2. Are usable resources and each job's demands represented, with shared occupancy and losses counted once?
3. Does a finite schedule preserve the initial backlog, policy, calendars and precedence it uses?
4. Does a continuing-regime calculation retain its arrival, service, dependence and stability premises?
5. Is a probability derived from the joint uncertain model, and a protective bound from its stated disturbance family?
6. Does the comparison distinguish a changed service mechanism from a changed measurement boundary?
7. Can admission, protection or commitment use the result and identify what would reopen it?

**Recognition and assurance.** A reproducible conditional calculation is a model result. For reliance on actual service, establish the resource availability and input assumptions that can change the decision, at the assurance level the work requires. Missing information may leave a probability unknown while a resource bound still settles the decision.

### OPS.10.1:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Consequence | Repair |
| --- | --- | --- |
| Replace the utilization factor by the busy fraction alone. | The rise in waiting near saturation disappears from the mean calculation. | Retain `rho/(1-rho)` with the selected model's premises. |
| Put mean durations into one schedule and report its deadline as assured. | Different uncertain paths collapse into an unrepresentative outcome. | Calculate the required predicate over the joint paths or derive an applicable bound. |
| Deduct interruption time after already including it in effective service. | The same capacity loss is counted twice. | Choose a consistent service/availability representation. |
| Apply the old one-server model after pooling resources or changing service dependence. | The mathematical account no longer describes the proposal. | Reconstruct the affected service mechanism before comparing its result. |

### OPS.10.1:9 - Consequences

The practitioner can obtain a capacity comparison from the smallest sufficient construction and see which operating change would alter its conclusion. Mean, scenario, deadline and probability questions remain connected without substituting one answer for another.

The cost grows when dependence, calendars or uncertain service matter. A bounded decision may finish with an elementary obstruction; a probability-sensitive decision may need richer modeling and input support. The method makes that additional work conditional on the receiving question.

### OPS.10.1:10 - Architectural Rationale

To compare capacity choices, explain how available resources perform activities under a policy and produce the required results. Observations, estimates or stipulated case inputs supply the quantities; mathematics relates them and calculation obtains the consequences. Their correspondence to the operating work determines what a calculation answers.

The construction therefore separates what the resources must do, how their service evolves and which result is requested. The same arrangement can need a finite deadline model today and a continuing mean model for another decision. Cases 5.1–5.3 show changes of variation, dependence and interpretation that a single scalar capacity value cannot retain.

Common model construction, inference and comparison remain in their supplying Methods. This pattern supplies the service laws and operating assumptions needed to use those Methods for a capacity decision.

### OPS.10.1:11 - SoTA-Echoing

For a quick mean comparison of one continuing first-come server, **adopt** the service-process and two-moment construction in [Hopp and Spearman, Factory Physics, third edition](https://www.waveland.com/browse.php?t=587), §8.6.5, equations 8.25–8.26. A utilization-only calculation is cheaper but loses the action-changing service variation in section 5.1. Sections 4.2 and 4.4 retain both variance contributions, the saturation factor and their premises. The formula is a mature approximation with a useful exact Poisson-arrival special case, not a universal service law. Its low calculation cost is accepted for the mean question; a changed operating regime or a required deadline probability reopens the choice.

For dependent traffic, **adapt** the richer description developed by [Whitt and You (2022)](https://www.columbia.edu/~ww2040/RQNA_pub.pdf), §§2.1–2.2: count dispersion over time retains variability a fixed two-moment description can lose. This costs additional traffic characterization. Section 4.4 selects that effort when the lost dependence matters. Their robust-queueing construction approximates mean performance in a steady regime under its stationarity and independent-service assumptions. Although the derivation uses a worst-case construction, the returned result estimates a mean; it does not guarantee an upper bound on individual waits. Changed dependence, routing or the requested result reopens that use.

For changing aggregate workload, [Oliveira, Sagawa and Mušič (2025)](https://apem-journal.org/Archives/2025/APEM20-1_029-042.pdf), §§3–4, supplies a current continuous feedback-control alternative. **Adapt** its explicit accumulation and capacity-response account for a suitable aggregate question; **reject** treating continuous versus discrete representation as the test for whether feedback is possible. Sections 4.3 and 5.3 retain the outflow law, completion interpretation and obtainable capacity change. An event model requires individual timing detail and is preferable when that detail decides the deadline. The paper's simulated control response does not establish physical access or every individual completion. Reopen when a changed service law or required completion event invalidates the chosen correspondence.

The finite probability and changed-dependence case is a direct construction from its stated premises. It avoids a simulation project for four enumerable outcomes. Use a larger probabilistic construction when the joint inputs or the risk question being answered require it.

### OPS.10.1:12 - Relations

OPS.10 selects the capacity/service decision. OPS.10.2 constructs the detailed deadline schedule and its conditional reserve. OPS.11.1 supplies the shared-resource and completion model; OPS.15.1 constructs the operating quantities. OPS.9 diagnoses an unresolved limiting mechanism. OPS.5, OPS.8 and OPS.13 use capacity results in admission, protection and commitments; OPS.19 reconciles simultaneous operating work.

MMP.10 supplies constraint construction, MMP.11 the response formulation and MMP.7 and MMP.13 the observation and inference contributions. CMP.9 supplies a randomized estimator when enumeration is insufficient. C.29 qualifies returning a mathematical result to its operating subject; C.16 preserves quantity meaning, and C.11/C.11.CRC supply common comparison and decision-use discipline.

### OPS.10.1:End
