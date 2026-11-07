## OPS.8 - Coordinate Queues and Buffers

> **Status:** Stable


### OPS.8:0 - Use This When

Use this Method when items wait across service or resource boundaries, a downstream activity is starved despite full boards, or release and buffer rules need to change for the continuing result of an operation. It is especially useful when teams optimize their own columns while unfinished inputs accumulate elsewhere.

Start by asking: **what is ready for which service, what is waiting for something else, and what loss should a buffer prevent?** The first useful result is a bounded queue-and-buffer policy: eligible population, ordering and release rules, protective purpose and amount where justified, replenishment action, exception authority, and a condition for reconsideration. A useful result can establish eligibility and release rules while returning an unresolved sizing question.

Use OPS.5 for one admission decision, OPS.6 for the next permissible Work in an admitted case, and OPS.7 for a local priority or existing-commitment decision when the shared policy remains adequate. Recover confused subjects through OPS.3. A numerical service or protection claim whose uncertainty matters also needs OPS.10.

### OPS.8:1 - Problem frame

An operation may contain several queues and joins. A release needs a tested configuration, a safety result and an authorized decision; a shipment needs product and documents; a case may need more than one specialist contribution. Completing one contribution does not make the whole result ready.

A queue is a selected waiting population eligible for a named service, ordered under a stated policy. A buffer protects or decouples something against a specified disturbance. A board column can describe either, both under separate rules, or neither. The policy question concerns the actual waiting and protection arrangements, not the appearance of that column.

### OPS.8:2 - Problem

Local limits can hide unfinished Work beyond a board boundary. Conversely, removing every visible queue can eliminate the ready supply that protects a costly or time-critical activity. Starting more items may increase incomplete kits while the activity needed for completion still lacks usable inputs.

The operation therefore needs to coordinate release, readiness, ordering and protection together, while preserving the distinction between a customer's waiting time and the waiting visible at one service station.

### OPS.8:3 - Forces

| Force | Practical tension |
| --- | --- |
| less started Work and reliable replenishment | A small started population can reduce congestion, but too little eligible supply can leave an important resource idle. |
| local autonomy and joins | A team can finish its own contribution while the receiving activity still waits for the rest of its kit. |
| small batches and setup burden | Smaller transfers can expose problems sooner; frequent setups or transactions can consume scarce time. |
| pooling and differentiated service | Sharing eligible demand can reduce idle capacity while changing failure exposure, priority, tail delay or fairness. |
| simple rules and protected conditions | A common dispatch rule is easy to use, but clinical, safety, compatibility and contractual conditions may require distinct treatment. |

### OPS.8:4 - Solution

#### OPS.8:4.1 - Fix the result, service boundary and population

Name the continuing result and its acceptance conditions, the service or resource in question, and the horizon. Reuse the operating focus and current subject account when they fit. Distinguish demand, an admitted matter, a work item, a service visit, a batch and an accepted result. One matter can require several visits; failed or repeated visits are not additional accepted matters.

State the event from which end-to-end waiting is counted. Define ready-queue membership by the inputs, permission, capability and access required for the next service. Keep upstream waiting, blocked matters and work already in progress visible under their own rules; excluding an item from the ready queue does not erase it from the operation's load or commitments.

#### OPS.8:4.2 - Recover incomplete joins and ready supply

At each consequential handoff, ask what the receiver can actually use now. Match the required inputs to the same configuration, case or result. Record the missing input and its supplier when the kit is incomplete. Inspect arrivals and eligibility changes over time, not just one queue snapshot.

A complete kit is relative to the next action. A test can be ready because its configuration, equipment, procedure and permission are available even though its test result does not yet exist. That result may be a prerequisite for later release. Requiring the future output as an input would prevent the action that produces it.

Where several actual structures interact, use OPS.11 to recover the relevant coupling. A local “Done” label is insufficient evidence that a receiving service has its inputs.

#### OPS.8:4.3 - State what each buffer protects

Select only the protection needed for the operating question.

| Arrangement | What its policy controls or protects | Useful quantity |
| --- | --- | --- |
| ready-work buffer before a selected service | service continuity during replenishment delay | eligible service load, related to the resource's operating calendar |
| inventory reserve | availability of specified material under replenishment and consumption uncertainty | usable quantity by material, location and condition |
| capacity reserve | response or recovery when load or availability changes | usable resource time with the necessary capability and access |
| limit on started items | congestion and exposure from concurrent unfinished matters | items under an explicit start/finish boundary, with load differences retained |

For the selected arrangement, state the shortage or disturbance, the consequence of failure, who replenishes it, what consumes it, and what signal changes action. A customer's commitment has its own parties and conditions; it does not automatically put the item in a protective buffer.

Work backward from the next shortage: when must replenishment become eligible, how long do recognition, request, authorization, supply and receiving checks take, and what other work uses the same people or resources? Choose a trigger that leaves that whole response available. For continuing service, also recover the quantity supplied per request, the earliest permitted next request, any overlap limit and the supplier’s capacity. Follow successive consumption and replenishment events: the available eligible load must cover consumption until each next receipt, and replenishment must sustain the required pace. More initial stock can cover a finite gap but cannot correct a continuing supply deficit. Distinguish material ordered, delivered and actually ready. A late-response signal needs a permitted alternative, such as different supply, protected capacity or an explicit service revision.

#### OPS.8:4.4 - Compare policies by their operating mechanism

Compare the current policy with one material alternative before adding a more elaborate policy family.

- If incomplete kits create downstream starvation, coordinate the missing inputs and release into the receiving service only when its kit is ready.
- If excess starts congest the relevant operation, compare a whole-boundary release limit with the existing local limits. Count unfinished matters that crossed local board boundaries.
- If a supported constraint needs protection, relate release and replenishment to its usable pace. Use OPS.9 when the constraint itself is uncertain.
- If pooling is proposed, test service compatibility, routing, resource failures, priority and the service criterion that matters. Also ask whether ownership, visibility of waiting work or interruption changes the performer's processing and checking behavior. Hold service quality and protected classes fixed when comparing those observations. Fixed service-time analysis remains useful when that premise is supported; otherwise price a bounded behavior-sensitive comparison before rollout.
- If batch size is the lever, compare setup or transaction burden with waiting, holding, feedback and rework consequences. Transfer batch and processing batch may differ.

Keep the end-to-end result and waiting origin fixed in the comparison. Reducing a downstream queue by holding demand just outside its measured boundary is not an end-to-end improvement.

When earlier work can revisit a resource after the release signal, [OPS.8.1 - Choose Work-Release Rules When Earlier Work Can Return](37-ops-8-1---choose-work-release-rules-when-earlier-work-can-re.md) constructs the release decision with that remaining or contingent demand. When auxiliary work could occupy an idle reserve, [OPS.8.2 - Use Protective Capacity While Keeping It Available](38-ops-8-2---use-protective-capacity-while-keeping-it-available.md) constructs its interruption or completion and the return to protected service. Reuse an adequate existing arrangement when the proposed use changes none of its relevant conditions.

#### OPS.8:4.5 - Size protection only to the supported use

Translate the supported replenishment delay into the amount consumed during it, using the protected activity’s calendar and rate. For example, a rig consuming one rig-hour of eligible load per open hour needs two ready rig-hours to cover one stated two-open-hour interruption. For a repeating policy, apply the quantity and cadence check in :4.3 as well. These are scenario-qualified conclusions; a probability guarantee needs the corresponding distributional basis.

Compare the carrying, delay and attention costs of more protection with the consequences of shortage. Include unusable or expired stock, changing case mix, correlated demand, failures, recovery and competing service classes where they change the choice. Use OPS.10 for a capacity/service comparison or a model-qualified distributional claim.

A relation among average population, arrival rate and time can check consistent units and accounting. It cannot determine a protective percentile or establish that a buffer never empties. If replenishment behavior or shortage consequences are unknown, keep the part of the policy that is supported and return the exact missing sizing input.

#### OPS.8:4.6 - Return and operate the bounded policy

State the eligible population, ordering rule, release condition, selected protective amount or unresolved amount, replenishment signal and action, exception authority, affected commitments, and review condition. Use the operation's existing account when it can carry that information.

For a trial, state its horizon, monitored consequences and withdrawal condition. Observe whether the policy changes accepted results, total waiting, starvation, rework, burden and protected service classes—not just the number of cards in one column. A demand, eligibility, replenishment, access or acceptance change can reopen the policy before the scheduled review.

### OPS.8:5 - Archetypal Grounding

#### OPS.8:5.1 - PumpWorks: twelve matters, four ready test packages

In this constructed case, PumpWorks coordinates weekly evidenced controller releases and incident response. Across five eight-hour rig-access windows, its history shows 20 hours of test execution, 4 of setup, 4 of unavailability and 12 with no eligible job. The final board snapshot contains twelve matters. Four test packages are ready and require eight rig-hours under their current estimates.

The practitioner obtains two different results from these inputs. The snapshot supports a ready queue of four packages with eight rig-hours of estimated load. The history shows lost open time with no eligible job. Neither establishes that twelve matters form one service queue or that rig capacity limits accepted releases.

The immediate policy is to book and dispatch only packages whose next-test inputs, permission and access are current; track the remaining matters by their missing inputs; and retain their waiting in the end-to-end account. The existing authorized priority rule orders the eligible packages. No new buffer quantity is claimed until replenishment and shortage consequences are known.

ReleaseCandidate-R42 lacks test evidence T9. If the inputs and lab-test permission for T9 are current, that missing output is not a reason to mark the test itself ineligible. SafetyQuestion-S19 and release authority remain separate conditions for the later release decision.

The return to OPS.9 is precise: distinguish late readiness from insufficient usable rig time as explanations for lost accepted releases. The return to OPS.10 is the eligible-load and access-window comparison, including recovery and rework. OPS.11 handles ProviderChange-P8 when its access decision changes those windows. The first policy can be used while those wider questions remain bounded and explicit.

#### OPS.8:5.2 - A small protection calculation

A service has one qualified resource, consuming one unit of ready service load per open hour. Its coordinator has a supported planning scenario in which replenishment can be interrupted for two open hours, and no other resource can serve that class. A two-unit ready buffer covers that interruption if service demand and eligibility remain as stated.

Keeping only one unit leaves one open hour exposed in that scenario. Keeping four units adds no coverage needed for the specified two-hour interruption, although another supported disturbance might justify it. If that interruption can instead last four hours, the two-unit conclusion reopens. Continuing protection also depends on the replenishment policy below.

Make the continuing response concrete. In a two-hour planning scenario, each ready unit is a one-hour job. At hour 0, A and B are eligible; replenishment is authorized and requested before A starts. The rule requests the next two jobs when two unstarted jobs remain immediately before dispatch and no earlier request is outstanding. For each such request, the supplier can make the next pair eligible within two open hours. Setup, receiving checks and access are included in that bound; they use separately available support, not the protected resource. This repeatable response supplies two jobs for each two-hour consumption cycle.

The supplied trace is: A runs 0–1, B runs 1–2; C and D arrive and pass their receiving checks at 1.5. Although no unstarted job remains from 1 to 1.5, B is still running: there is no service starvation. At 2, C and D are ready, the earlier request is closed, and the next pair is requested before C starts. It becomes ready at 3.5; C and D run 2–3 and 3–4. This return demonstrates two cycles under the supplied trace. The observation burden is one request/acknowledgement and one eligibility confirmation per pair; an existing dispatch record can carry both.

Now, at 1.25 the supplier reports that C and D cannot be ready before 2.5. The coordinator has no approved substitute. A and B still finish by 2; service then waits half an hour, and C cannot finish before 3.5. A promise of three completions by 3 cannot be met under these conditions and needs the OPS.13 service decision.

For later operation, three initial one-hour jobs would cover one 2.5-hour response, but adding that stock alone does not repair the continuing two-job policy. Even if the first pair is requested at 0, successive 2.5-hour responses can leave five jobs consumed by hour 5 and the next pair unavailable until 5.5. Compare a change to quantity or request cadence with the supplier. One conditional alternative is three eligible jobs per request, requested before dispatch when three unstarted jobs remain and no earlier request is outstanding, with a supported whole-response bound of 2.5 hours for every request. Starting with three jobs, their three-hour coverage then contains each response; the next request is made before the next three-job group begins. The former two-job promise does not establish this larger response. Ask the supplier whether it can provide those three eligible jobs under the same receiving checks and support capacity, or what quantity and cadence it can support. Until that answer is obtained, retain the supported finite coverage and return the unsupported continuing-service promise for revision. Include the added stock and coordination burden in the choice.

#### OPS.8:5.3 - Patient waiting is not one interchangeable queue

A hospital coordinator receives qualified clinical eligibility and priority for a particular resource class. The operating queue includes only cases that can use that service under those conditions. Patients awaiting a different clinical decision or capability remain visible in the wider waiting account.

OPS.8 can coordinate the resource queue and readiness information. It does not supply the clinical eligibility, triage rule, consent or treatment decision. Pooling unlike service classes is not justified merely because the combined list is shorter.

#### OPS.8:5.4 - Pooling can change how people serve the queue

Consider two qualified diagnostic practitioners serving interchangeable routine requests for two hours. A separate protected urgent-service arrangement and the same diagnostic acceptance criteria remain unchanged. With two assigned requests each, the supplied dedicated-queue trace takes 60 minutes per request and completes four accepted results by hour 2. A fixed-rate pooling calculation predicts the same four, with potential benefit when the assignment becomes unbalanced.

The proposed common queue removes each practitioner's visible pending count and makes assignment negotiation part of every pickup. In a constructed matched replay, each request now consumes 60 minutes of diagnosis plus 12 minutes of that coordination; checking is unchanged. Only two results finish by hour 2; all four finish by 2.4. The change has not provided four timely accepted results, even though the jobs remain compatible and total demand is unchanged. Do not roll out that policy for the four-result commitment. Retain the current arrangement, or test a pooled policy with explicit pickup ownership and visible pending load before claiming that it preserves the earlier rate.

The comparison itself needs time: here 30 minutes to agree the comparable requests and quality check, and 10 minutes of independent observation per arrangement, in addition to the observed service work. Those supplied costs belong to the choice, as do transition and training if a revised pool is tried. In live use, preserve mix, staffing and quality, account for learning/carryover, and inspect whether the observed change supports the claimed cause. This constructed trace proves no general causal effect. When automated service has a stable rate and dispatch changes none of these behaviors, the fixed-rate model can be sufficient; do not impose an extra behavioral experiment without an action-changing premise.

### OPS.8:6 - Bias-Annotation

| Bias | Consequence | Countermeasure |
| --- | --- | --- |
| board-boundary bias | Waiting disappears when an item leaves a local column. | Retain the operation's population and waiting origin. |
| zero-buffer ideal | Protection is removed together with avoidable congestion. | State the disturbance and shortage consequence before changing the amount. |
| complete-kit absolutism | Every future result is demanded before any useful action can start. | Define readiness for the next service, not for the whole case's eventual completion. |
| local-utilization pressure | More starts create incomplete kits and downstream waiting. | Inspect the accepted result and receiver-ready inputs. |
| pooling optimism | Mean efficiency hides class-specific or failure-related loss. | Compare the actual service criterion and resource assumptions. |

### OPS.8:7 - Conformance Checklist

1. Can the reader identify the operating result, service boundary, eligible queue members and wider unfinished population?
2. Does readiness describe inputs for the next service without requiring that service's future output?
3. Does every selected buffer have a protective purpose, units, replenishment action and shortage consequence?
4. Is the chosen policy compared with the current arrangement using total waiting and accepted results?
5. Is its amount justified for the stated scenario or distributional claim, or returned as an exact unresolved question?
6. Are exception authority, affected commitments, monitored consequences and reopening conditions usable by the participants?

These questions recognize a constructible policy. Assurance additionally requires the case evidence, capability, permission, load and uncertainty basis needed for the particular protection or service claim.

### OPS.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Count every board item as ready supply. | Some items lack prerequisites or use another service. | Recover membership and missing-input populations. |
| Treat commitment as buffer membership. | A promise does not establish eligibility or physical protection. | State the two relations separately. |
| Size a “never empty” buffer from averages. | A mean relation does not establish the shortage tail. | Qualify replenishment scenarios and consequences through OPS.10. |
| Improve the metric by moving its start boundary. | The customer can wait just as long outside the reported queue. | Preserve the end-to-end origin and show local waiting separately. |
| Use one pooling or batch rule everywhere. | Compatibility, failure, setup and service objectives differ. | Compare the concrete alternative under the receiving operation's conditions. |

### OPS.8:9 - Consequences

The operation can reduce avoidable congestion while retaining justified protection. Participants can see whether the next useful action is to replenish a kit, dispatch eligible work, restrict starts, obtain capacity evidence or coordinate another structure.

The cost is maintaining consequential eligibility and replenishment information. A more precise ready queue can initially look smaller without any improvement in the wider operation. The practical benefit is a better policy decision; realized improvement still requires the operating evidence.

### OPS.8:10 - Rationale

Queue coordination works at the receiver's service boundary and at the wider result boundary together. The first prevents dispatch of unusable inputs; the second prevents hidden waiting and local improvement from replacing the actual purpose.

Protection and concurrency control are therefore selected by their effects, not by a shared label or a management school. A cheap eligibility rule can be useful before a numerical buffer study, while a numerical guarantee cannot borrow that rule's adequacy.

### OPS.8:11 - SoTA-Echoing

| Practice question and selected line | Serious alternative, trade-off and pattern change | Source roles, limits and reopen condition |
| --- | --- | --- |
| How should local completion and downstream readiness be coordinated? **Adapt** whole-operation ready-supply and complete-kit reasoning. | Local column limits are cheaper but can miss joins; a complete-kit rule applied to the whole case can block useful investigation. Sections 4.1–4.4 and 5.1 instead bind readiness to the next service while retaining total waiting. The added input matching is justified when it changes dispatch or starvation. | Tendon, *The Book of TameFlow* (2022), complete-kit example and time-buffer discussion, printed pp. 135–137 and 141–143, is a mechanism candidate. [The Kanban Guide 2025.5](https://kanbanguides.org/the-kanban-guide/2025.5/) is the serious workflow-policy comparator. Neither establishes one policy for every operation. Reopen when the join, eligibility or receiving result changes. |
| How much protection or batching is useful? **Adapt** disturbance-specific protection and the setup-versus-delay comparison. | Minimizing every queue or batch ignores the cost of shortage or repeated setup. Sections 4.3–4.5 and 5.2 require a purpose and supported scenario instead of a universal optimum. This costs an explicit consumption/replenishment account, not necessarily a full optimizer. | Tendon's time-buffer account and Reinertsen, *The Principles of Product Development Flow* (2009), E6–E9 and Figure 5-4, supply competing mechanism candidates. Their models do not establish a protection tail or transferable batch optimum. Reopen when setup, replenishment, feedback or shortage consequences change. |
| Should eligible demand be pooled? **Adapt** model- and service-criterion-specific comparison. | Pooling can improve one mean measure while worsening a protected tail or class. Section 4.4 keeps the service criterion and failure assumptions explicit; no pool-all default is selected. | [Andradóttir, Ayhan and Down (2017)](https://doi.org/10.1016/j.ejor.2016.05.009) and [Cao et al. (2021)](https://doi.org/10.1287/opre.2019.1976) supply counterexamples under different modeled conditions. Their results do not prescribe a rig or clinical queue. Reopen for the actual routing, failure, abandonment or service-class change. |

[Song, Armony and Roels (2024)](https://doi.org/10.1287/msom.2023.0202) report two online experiments in a healthcare-delivery context in which queue configuration, ownership and awareness of queue length interact with processing behavior. Their abstract supports questioning a fixed-service-time premise, not importing an effect size, clinical conclusion or dedicated-queue rule. Sections 4.4 and 5.4 adapt that question to a same-result comparison and include observation cost. Keep a capable pooling model when its behavioral assumptions fit; reopen when the arrangement changes attention, quality, ownership or the protected population.

### OPS.8:12 - Relations

OPS.3 and OPS.4 supply matching subject and current-state accounts. OPS.5 consumes the applicable admission or release limit; OPS.6 uses the policy for permissible case continuation; OPS.7 supplies local priority under its authority without redesigning the queue.

OPS.9 supplies a supported constraint account when protection depends on that diagnosis. OPS.10 qualifies load, capacity and protection/service uncertainty. OPS.11 coordinates couplings that a local queue rule cannot resolve.

Current FPF C.16 and C.27.TA govern measurement and time use. A.22 and E.18 govern relevant structures; E.18.NET applies only to independently identified flow structures with obtaining cross-flow relations. Clinical, safety, legal and other specialist permission remains with the practice that supplies it.

### OPS.8:End
