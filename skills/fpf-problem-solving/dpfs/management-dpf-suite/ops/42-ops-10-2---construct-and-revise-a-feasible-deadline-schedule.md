## OPS.10.2 - Construct and Revise a Feasible Deadline Schedule

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative

### OPS.10.2:1 - Problem frame

**Use this when** a team must deliver particular results by particular times, but a list of tasks and estimated durations does not establish whether the work fits. Two ready tasks compete for one specialist. A test needs an uninterrupted window. A delayed input changes which remaining operation can now postpone delivery.

Construct a finite schedule: assign the required operations to times and resources under their actual conditions. Use it to identify a feasible way to meet the deadline, an obstruction that excludes the deadline, or the choice still unresolved. Then determine which delays the plan can absorb and revise it when a consequential condition changes.

**First useful move.** Name the recipient's completion event and deadline. Trace the remaining operations to that event, including required handovers and acceptance. Mark the people, equipment and calendar windows they share. OPS.11.1 supplies that operating account; OPS.15.1 supplies event and clock interpretation.

**Practical gain.** The planner can state what should start when, which reservations matter, how much postponement is still possible under the chosen arrangement, and what change could recover a threatened commitment.

This method addresses finite delivery timing within the broader capacity and service question of OPS.10. Its subject is the proposed schedule, not the performed work or a new customer promise. Use an adequate existing schedule directly when its conditions still answer the question. Use OPS.10's demand and capacity analysis when the question instead concerns sustained throughput or a distribution of future delays.

The elementary cases need time intervals, arithmetic and a dependency diagram or equivalent list. A large search may need a scheduling specialist. Known jobs with known durations do not require a probability model.

### OPS.10.2:2 - Problem

A dependency diagram can allow work to proceed in parallel while the same person must perform both branches. A resource total can fit a day while a continuous operation fits none of its open windows. A priority rule can produce a late plan even though another order meets the deadline.

A second error arises after a plan has been obtained. Its apparent spare time is spent independently by several participants, or a once-critical sequence continues to determine priorities after resource access has changed. The practitioner needs a construction that connects the proposed times, their feasibility, the reserve being used and the conditions requiring revision.

### OPS.10.2:3 - Forces

| Force | Tension |
| --- | --- |
| Early results and shared resources | Advancing one result can postpone another. |
| Compact model and consequential detail | Whole-operation durations are convenient, but attendance phases or calendar gaps can decide feasibility. |
| Fast plan and strong conclusion | A useful candidate may be easy to obtain; optimality or impossibility needs an additional argument. |
| Deferred starts and protection | Waiting can reduce aging or premature work while consuming opportunities to recover delay. |
| Stable coordination and changed facts | Keeping appointments has value, but preserving an invalid order can lose the delivery. |

### OPS.10.2:4 - Solution

**Working mantra.** Recover the recipient's result and deadline; pass them to a description of the remaining operations and the events that enable each one. Carry that description into shared resource occupations and usable calendar windows. Use those conditions to choose a sequence and place operations, returning a complete feasible plan or the reason a proposed placement fails. Compare the plan with a necessary bound before claiming that earlier completion is impossible. Pass the feasible plan to a calculation of conditional start windows and delivery reserve. Use those windows to compare early work, postponement and deliberate protection. When a condition changes, retain completed facts, reopen the affected dependencies and resource competition, obtain the revised plan, and return its delivery consequences to the people choosing priorities and release.

#### OPS.10.2:4.1 - Recover the delivery question and remaining work

State the result that must be available, its deadline and its waiting origin. An internal completion can precede transport, approval or receiving acceptance. Include those operations when the promise needs them.

Separate hard requirements from preferences. "Meet all three dates" asks for feasibility. "Finish the last order as early as possible" minimizes the last completion. "Obtain the first result sooner" can prefer a different order. If competing recipients cannot all receive their earliest possible result, OPS.7 supplies the priority and commitment choice.

For each remaining operation, recover its readiness event, required predecessors, duration or bounded scenario, eligible resources, and whether it can be interrupted. Include setups, transfers and known return work when they consume relevant time. Retain completed operations and work already under way as facts; estimate only their remaining requirements.

Qualify the duration before calculating a schedule. Recover the execution conditions and whether the quoted time includes waiting or deliberate protection against overruns. A protected task commitment is not, by itself, a measure of the time the work takes. Keep work and required waiting in the timing model, and identify protection already included before reserving more time for the same delays. If that split is unknown, obtain a supported estimate or compare explicit duration scenarios; cutting every quotation by the same percentage does not recover the missing basis.

Keep the finite work list at the detail the decision needs. If a task requires an operator only during loading, recover that phase without decomposing every machine movement. If an unknown duration could reverse the decision, compare supported bounds or obtain that particular input. A full event history is unnecessary when the supplied conditions already settle the schedule.

#### OPS.10.2:4.2 - Construct precedence, occupation and calendar conditions

A precedence relation states which event must occur before another operation may begin. For a continuous operation i of duration p_i, finish f_i equals start s_i plus p_i. A finish-to-start relation from i to j with required delay l requires s_j >= f_i + l. At a join, every required predecessor must satisfy its relation. An actual partial handover can use an earlier event, provided the downstream work can use that partial result.

Resource sharing adds a different condition. Two operations requiring the same exclusive resource cannot occupy it at the same time. Their order is a choice unless the operation already fixes it. For a pool, check how many eligible members are needed simultaneously; one free but unqualified person does not supply the required capability.

Recover each occupation separately. A machine may hold an order for three hours while its operator is needed only in the first hour. Represent the machine interval and that operator interval with their common start. Apply each resource's capacity and calendar to its own intervals. Use half-open intervals, including the start and excluding the finish, when a resource can pass immediately to the next operation.

Distinguish three calendar conditions that require different placements:

- A continuous occupation must fit wholly inside an available window.
- Work that may pause can accumulate processing across open windows, with any restart cost included.
- A machine may continue through an operator's absence when that phase needs no attendance.

A rule allowing an operation to start during working hours does not establish that its later occupied hours are available. Where several resources are needed together, find a window in which their required occupations are jointly possible.

Check that the precedence relations can be satisfied. A finish-to-start cycle with positive total required duration and delay is an obstruction. When the work actually revisits a station, represent the later visit as a later operation rather than requiring one operation to precede itself.

MMP.10 supplies the joint formulation. Keep the operational reason for a condition recoverable: actual precedence, chosen resource order, calendar closure, admission policy or deadline. A chosen order can be reconsidered without pretending the technological route changed.

#### OPS.10.2:4.3 - Place the work and distinguish the resulting conclusions

For a small case, start with operations whose required predecessors have been placed. Choose an eligible operation, find its earliest jointly available placement after readiness, reserve the required intervals, and continue. Several reservations may be made within one long machine operation when its attendance phases allow other work.

At a resource conflict, compare the competing orders. A near deadline or a long downstream continuation can guide the first attempt; neither is a universal priority theorem. Preserve alternatives when that first attempt fails or gives an inadequate result. Inserting work into a gap, leaving a resource temporarily idle, or changing an uncommitted order can permit a schedule that a simple dispatch rule misses.

Once the relevant orders are fixed, calculate the earliest times consistent with them. With continuous availability and finish-to-start relations, each start is the maximum of its readiness and predecessor finishes plus their required intervening delays. Chosen resource-order relations also contribute predecessors. For partial attendance, connect the occupied phases, not the finish of an unrelated unattended phase. With calendars, move each proposed occupation to the next jointly permitted window and propagate the resulting finish.

Check the complete candidate against every required operation, precedence, occupation, calendar and completion event. A feasible assignment is a witness that the modeled work fits; the participants must still have the stated access and capability.

Use cheap necessary bounds before a larger search. A required dependency chain cannot finish faster than its ordered work permits. A resource cannot supply more mandatory occupation than its available capacity in the required window. A continuous operation cannot use several disjoint short windows as one long window. Passing these bounds does not construct a schedule.

Return the actual strength of the result:

| Obtained result | Supported conclusion |
| --- | --- |
| Complete feasible schedule meeting the dates | Those dates are attainable under the stated conditions. |
| Feasible completion C and lower bound L on the earliest possible completion | The optimum lies between L and C. Equality establishes an earliest completion. |
| Necessary condition incompatible with the deadline, or a complete valid search excluding every permitted schedule | The deadline is impossible within that modeled arrangement. |
| A failed priority rule, restricted sequence or interrupted search | That attempt found no satisfactory plan; other permitted schedules remain unresolved. |

CMP.4 supplies justified search when the operational choices remain numerous. CMP.5 supplies relaxations and bounds. Give the specialist the actual resource and calendar conditions and the conclusion needed.

Stop when a suitable plan or sufficient obstruction answers the decision. Further optimization is useful only when its possible improvement matters.

#### OPS.10.2:4.4 - Derive time reserve and conditional criticality

First state the event against which reserve is measured. If the proposed final completion is C and its deadline is D, D-C is the plan's final margin. A negative value shows that this plan misses the deadline; it does not by itself exclude another plan.

For a precedence network with fixed durations, continuous calendars and no binding resource contention, calculate early starts forward and latest starts backward. Start the backward pass from the selected final time T, retaining any earlier hard intermediate deadlines. For each successor, subtract the required intervening delay from that successor's latest start. The earliest of those bounds and any deadline on the operation gives its latest finish; subtract its duration to obtain its latest start. Latest start minus early start is its total float relative to those targets. Free float is the delay that leaves the successors' early starts unchanged, including their required intervening delays.

When only the final event governs this calculation, setting T to the earliest final completion identifies zero-float paths controlling that completion. An earlier intermediate deadline can instead give zero float to work protecting that intermediate event; identify which event the result concerns. Using a later final deadline adds delivery margin where other commitments permit it, so an operation on the longest precedence path can have positive deadline float. Several longest paths can exist. Serial operations may draw on the same margin, so their individual floats are not independent allowances to add together.

With shared resources, retain the selected allocations and orders when making the timing calculation. For whole-operation exclusive occupations, add the chosen resource-order relations to the precedence network; its timing is conditional on those orders. For partial occupations or calendars, use the corresponding phase and window constraints. A different allowed order or calendar can change the controlling sequence.

To assess a proposed postponement, hold the stated commitments fixed, delay that start, and refit the affected work. Identify the latest feasible placement or the set of feasible start windows that still meets the protected event. Calendar gaps can make intermediate start times infeasible even when a later window exists. A backward arithmetic pass that ignores those gaps supplies no usable postponement permission.

Call a sequence critical only with its plan, resource choices and target event recoverable. Test a claimed critical operation by changing its duration or availability and recalculating the consequence at that scope. An operating bottleneck concerns the mechanism limiting sustained flow under a workload; it need not be an operation controlling this finite deadline. OPS.9 supplies that diagnosis.

#### OPS.10.2:4.5 - Choose early work, deferred starts and protection

Compare start policies inside the feasible windows. Starting earlier can reveal problems and retain recovery time. Deferring can avoid aging, premature expenditure or work invalidated by a later input. Retain the recipient's original waiting boundary in either comparison.

When protection is needed, name the event and disturbance to be absorbed. Choose an internal target earlier than the commitment, or reserve time before a consequential join. Determine its amount from the delay scenario, supported bound or risk model that matters to the decision. A final margin is available time; calling it a buffer adds a policy for preserving and using it.

When several operations protect the same delivery, compare keeping their individual protection with placing protection before the common delivery or a feeding join. Revise the operation estimates and protection together, preserving the required work, intermediate obligations and execution conditions. Size the shared protection for the joint delays it must absorb: delays that can occur together cannot be treated as mutually exclusive. Check the new plan and the participants' release and handover rules; moving reserve into one place does not make it available before every earlier commitment. Keep or restore local protection where the joint arrangement cannot protect that earlier result.

For known deterministic conditions, the feasible schedule can be enough. To protect against a stated extra hour of review, add that hour to the appropriate operation and recompute the plan. This answers the scenario without inventing its probability. A service-probability claim needs the corresponding duration and dependence model; OPS.10.1 supplies that construction.

After inserting protection, recheck resource and calendar feasibility. Moving a feeding operation earlier can take another task's reservation. Keeping two hours before final delivery does not make those hours usable before an earlier calendar closure. Do not allocate the same margin to several independent promises without checking their combined delay.

Return the selected target times, reserved intervals and response to reserve consumption to OPS.8 for release and protection. OPS.7 uses the delivery consequences for priorities; OPS.14 supplies financial comparison when it can change the start policy.

#### OPS.10.2:4.6 - Reconstruct the affected remainder after a change

At the current time, retain actual starts, completions and ongoing occupations. Replace the changed duration, readiness, access window, required operation or commitment. Do not restart completed work or shorten an uninterrupted operation merely to recover the former finish date.

Follow the changed operation through both its successors and the resources it shares. A task outside its precedence descendants can still lose a resource window. Include resulting admission changes and downstream joins; widen the affected set until its remaining boundary conditions are unchanged.

Try retaining unaffected reservations and the useful parts of the former plan. Refit the affected work under those commitments. If that restricted repair fails, identify which still-changeable reservation or resource order could matter and compare a broader rearrangement with its coordination cost. Failure while preserving the old order excludes only that restricted repair.

Recompute completion times, feasible postponement windows and protected reserve. Compare them with the same recipient events and deadlines. Return the actionable difference: a changed start or allocation, reserve consumed, an obtainable operating remedy, a commitment needing reconsideration, or an unresolved scheduling choice. Retain unaffected model and calculation results whose premises still hold.

### OPS.10.2:5 - Archetypal Grounding

#### OPS.10.2:5.1 - A deliverable with a join and shared deadline margin

A report needs preparation P, taking four hours, and evidence extraction E, taking two. Different people can perform them concurrently from time zero. Review V takes three hours after both finish; release R takes one hour after review. These resources are independently available, durations are known, and release completes delivery. The deadline is hour ten.

| Operation | Predecessors | Earliest interval | Latest start for delivery at 10 | Total float |
| --- | --- | --- | ---: | ---: |
| P | None | 0-4 | 2 | 2 |
| E | None | 0-2 | 4 | 4 |
| V | P and E | 4-7 | 6 | 2 |
| R | V | 7-8 | 9 | 2 |

The precedence path P-V-R takes eight hours and controls earliest delivery. E has two hours of free float before its delay moves V's early start. Starting E at hour two preserves delivery at eight and may avoid producing an input earlier than useful. Starting it at four instead gives V at 6-9 and R at 9-10, consuming all final margin.

P, V and R each have two hours of total float against ten, but they share those hours. Delaying P by two moves V to six and R to nine; another two-hour delay of V would miss the deadline.

To preserve one hour before the external deadline, use an internal delivery target of nine. The latest starts become P at one, E at three, V at five and R at eight. They jointly give one feasible deferred plan with the intended final reserve.

Return to execution of the earliest-start plan. At hour two, preparation is found to need three further hours instead of two. E is already complete. Continue P to five, then V at 5-8 and R at 8-9. The new final margin is one hour. The changed input reopens preparation and its successors; E's completed result remains available.

#### OPS.10.2:5.2 - A failed short-task priority is not an impossible deadline

Two jobs are ready at zero. U needs three hours of one specialist followed by seven hours of unattended equipment work. V needs two hours of that specialist followed by one unattended hour. The equipment is different for the two jobs, all resources are continuously available, and both results are required by hour ten.

Doing the shorter specialist task first gives V at 0-2, its equipment at 2-3, U at 2-5 and its equipment at 5-12. That plan misses the deadline.

Doing U first gives specialist intervals U at 0-3 and V at 3-5. U's equipment runs at 3-10 and V's at 5-6. Both dates are met. U's own required chain takes ten hours, so the plan also attains the lower bound for the last completion.

In the first plan, the chosen resource relation V-before-U makes V part of the sequence controlling the final finish. In the second plan, V can finish well before U. That criticality was a consequence of the selected order. Five hours of specialist demand alone revealed neither the successful order nor the ten-hour completion.

#### OPS.10.2:5.3 - Shared attendance still permits machine overlap

Five orders arrive at zero. Each needs A for two hours and then B for three, with order 1-5 on each station. Each station has one continuously available machine; there are no setups, returns or other work. B completion makes an order ready for its customer. No operation is interrupted. Admit the first two at zero and the next order immediately when a B completion frees one of the two places.

With independent station resources, earliest A intervals are 0-2, 2-4, 5-7, 8-10 and 11-13. B finishes at 5, 8, 11, 14 and 17.

Now both stations use one operator. A requires continuous attendance; B requires attendance only in its first hour and holds its machine for all three hours. The old A intervals conflict with B attendance. Recovering the phases yields this revised plan:

| Order | Admission | A with operator | B with operator | B unattended | Completion |
| --- | ---: | --- | --- | --- | ---: |
| 1 | 0 | 0-2 | 2-3 | 3-5 | 5 |
| 2 | 0 | 3-5 | 5-6 | 6-8 | 8 |
| 3 | 5 | 6-8 | 8-9 | 9-11 | 11 |
| 4 | 8 | 9-11 | 11-12 | 12-14 | 14 |
| 5 | 11 | 12-14 | 14-15 | 15-17 | 17 |

At hour two, start B1 before A2; then place A2 inside B1's unattended phase. Repeating that choice keeps B working continuously. The operator's intervals do not overlap, and no more than two orders are admitted and unfinished.

B cannot begin before hour two and must process five orders sequentially for three hours each. Every completion therefore satisfies f_Bi >= 2+3i; the plan attains all five bounds. The shared operator changes starts at A without delaying any recipient result.

Customer times average eleven hours. Internal times are 5, 8, 6, 6 and 6 hours, averaging 6.2; the remaining average 4.8 hours occurs before admission. These quantities retain their different event boundaries.

#### OPS.10.2:5.4 - A calendar gap makes final margin unusable for a test

A maintenance test becomes ready at hour two. It needs a rig and an engineer together for three uninterrupted hours. A separate analyst then needs one hour to issue the acceptance result and is available throughout. The rig is available from two to ten; the engineer from zero to five and from six to ten. Acceptance is due at eight.

The test fits at 2-5 and acceptance work at 5-6. The final margin is two hours, but the test cannot be postponed by one hour: 3-6 crosses the engineer's absence. The next complete test window starts at six, giving acceptance at ten. Within the original deadline, the margin can postpone the analyst's work, not the test.

Before execution, the engineer's first window is shortened to end at four. Common availability before the latest possible test finish at seven is 2-4 and 6-7: three hours in total, but no continuous three-hour interval. This excludes acceptance by eight. The earliest remaining test is 6-9 followed by acceptance at 9-10.

The obstruction identifies a useful remedy to investigate: restore attendance through five or obtain another qualified continuous window ending by seven. Merely reporting three available engineer-hours, or silently allowing the test to pause, does not answer the stated operation.

These examples are constructed scheduling cases. Their conclusions follow from the stated intervals and bounds.

### OPS.10.2:6 - Bias-Annotation

Finite deterministic schedules favor work whose remaining operations and durations can be specified. Discovery work or frequent unplanned returns can require scenarios, rolling revision or a different service model. Keep that uncertainty visible without withholding a useful known-date bound.

The examples assume that named people and machines are interchangeable only where stated. Human fatigue, location, recovery and skill conditions can change available occupation. Recover them when they alter the proposed plan rather than treating a calendar reservation as supplied capability.

### OPS.10.2:7 - Conformance Checklist

- The completion event, waiting origin, deadlines and any optimization preference are explicit.
- Required operations, precedence and partial resource occupations describe the work being planned.
- Resource sharing, capability, calendars and interruption conditions are jointly respected.
- A claimed feasible result includes an executable assignment of the required work.
- An impossibility or optimality conclusion has the necessary bound or complete-search basis.
- Float, feasible postponement windows and final margin retain their target and resource-order conditions.
- Protection has a named event, burden and delay basis, and the protected plan remains feasible.
- Revision follows shared-resource competition as well as precedence and preserves completed facts.

### OPS.10.2:8 - Common Anti-Patterns and How to Avoid Them

| Mistake | Consequence | Repair |
| --- | --- | --- |
| Schedule each department's copy of one person independently | The plan double-books the actual person. | Constrain that person's combined occupied intervals. |
| Keep the first priority rule after it misses a date | A poor sequence is presented as an impossible commitment. | Reconsider permitted orders or obtain an impossibility argument. |
| Spend each task's float independently | Several tasks consume the same delivery margin. | Recompute their joint postponement. |
| Treat the original critical sequence as permanent | New resource competition or delay is missed. | Recalculate conditional criticality from the changed arrangement. |
| Deduct closed hours while allowing a continuous task to span them | A nominal working-time calculation produces an impossible operation. | Place the complete required occupation in a permitted window. |
| Add a buffer without rescheduling its feeders | Earlier work competes with existing reservations. | Check the full protected assignment. |

### OPS.10.2:9 - Consequences

The method produces a usable temporal arrangement or a specific obstacle instead of an unsupported date. Conditional reserve also gives release and priority decisions something concrete to use.

Detailed scheduling costs inquiry and maintenance, and optimization may consume more effort than its possible benefit. A feasible plan remains dependent on the supplied work and access conditions. Reusing unaffected assignments and reopening consequential changes limits that burden without treating the first plan as permanent.

### OPS.10.2:10 - Architectural Rationale

Precedence, resource competition and calendars enter together because each can exclude a superficially plausible plan. The precedence-only calculation remains a useful reduced case and lower bound when resources are relaxed. It becomes the full answer only when the omitted conditions do not invalidate its assignment.

Feasibility precedes reserve use: a gap in an impossible plan is no protection. Reserve is then interpreted against a specific event and selected choices, allowing early and deferred policies to be compared.

The operating construction supplies phase occupations, appointments, available windows, receiving deadlines and the changed remainder. MMP.10 and CMP provide general formulation and search. Keeping criticality conditional also lets a planner revise a local sequence without mistaking it for the sustained-flow constraint of the whole service.

### OPS.10.2:11 - SoTA-Echoing

For the question "Can this finite work meet its dates with shared resources?", adopt explicit interval feasibility and sequence choices. The [OR-Tools Job Shop account, variables and constraints](https://developers.google.com/optimization/scheduling/job_shop) supplies precedence and exclusive-resource alternatives; its [CP-SAT result definitions](https://developers.google.com/optimization/cp/cp_solver#cp-sat_return_values) distinguish a feasible answer, a proven optimum, proven infeasibility and an unresolved stop. Adapt these constructions in :4.2-4.3 to operating attendance phases and recipient deadlines. A precedence-only forward pass is cheaper and sufficient when resources do not bind. In :5.2 it cannot choose the specialist order, so explicit resource choices earn their added effort. Reconsider the formulation or search method when problem size or new operating constraints make its cost or representation inadequate.

For calendar feasibility, adopt the explicit distinction between elapsed interval and working duration in [IBM's Scheduling Tutorial, chapter 4](https://ibmdecisionoptimization.github.io/tutorials/html/Scheduling_Tutorial.html#Chapter-4.-Adding-calendars-to-the-house-building-problem). Its example permits suspension during days off and explains separate restrictions on starts, ends and occupied extent. Adapt :4.2 and :4.4 to choose the rule from the operation: :5.4 requires a whole uninterrupted occupation. Combining open hours would answer a different permitted-work question. The extra interval check is small and decides the example; the tutorial does not establish whether a real test may pause. Reopen when interruption, attendance or calendar rules change.

[Goldratt, Critical Chain (1997)](https://www.toc-goldratt.com/en/product/Critical-Chain), chapters 16–17, is a historical construction of moving protection from individual task estimates to project and feeding buffers, together with changed execution rules. Adopt the distinction between work estimates and deliberately placed protection in :4.1 and :4.5. Its halving example assumes already protected estimates; it does not establish a universal conversion of a task quotation into a duration or a completion probability.

For a known schedule or a named delay scenario, compare an explicit feasible plan with tested reserve against fixed critical-chain and percentage-buffer prescriptions. [Herroelen and Leus, On the Merits and Pitfalls of Critical Chain Scheduling, PMI conference paper (2000)](https://www.pmi.org/learning/library/merits-pitfalls-critical-chain-scheduling-1102), sections on critical sequences, buffers and computational experiments, supplies historical counterexample and experimental evidence. Adapt its attention to resource-dependent sequences and schedule revision; reject treating an initially selected chain or a fixed percentage as sufficient protection. This changes :4.4-4.6: preserve useful reservations, compare the delay actually being protected, and recheck resource feasibility after buffer placement. The cost is a more explicit comparison and possible coordination changes. The paper's old software comparisons and experimental percentages are not present-day performance claims. Reopen when an applicable protection policy meets the same delivery and coordination requirements with better supported burden or outcomes; probabilistic protection requires its own uncertainty basis.

### OPS.10.2:12 - Relations

OPS.10 selects the deadline or service question. OPS.10.1 constructs the capacity, mean or probability account when that question requires it. OPS.11.1 supplies the operating arrangement and resource identities; OPS.15.1 supplies event-defined time and occupancy quantities.

OPS.7 uses changed delivery consequences for priorities and commitments. OPS.8 uses feasible release times and protection; OPS.9 diagnoses throughput-limiting mechanisms. OPS.14 contributes financial consequences when early or deferred work changes the decision.

MMP.10 supplies the constraint formulation and its interpretation. CMP.4 supplies search with justified exclusions and CMP.5 supplies relaxation and bound reasoning when needed. C.29 returns the calculated schedule to its operating meaning; B.5.MPC coordinates changed subject premises, mathematics and computation. A.22.CGUS helps recover enabled alternatives before a sequence is fixed.

### OPS.10.2:End
