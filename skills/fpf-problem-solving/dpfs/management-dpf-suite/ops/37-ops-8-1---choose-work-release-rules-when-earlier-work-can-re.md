## OPS.8.1 - Choose Work-Release Rules When Earlier Work Can Return

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative

### OPS.8.1:1 - Problem frame

**Use this when** finishing one operation can trigger new work even though the previous result may still need correction, another visit or downstream acceptance. A specialist finishes an analysis and begins a long client session; the analysis then returns for urgent revision. A part leaves a machine but may return after inspection. An admission limit frees a place at local completion while later work still needs the same resources.

Choose what event should permit another start, what remaining and possible work that start must accommodate, and how the decision changes when feedback arrives. The result is a release rule that can be operated: a signal, eligible next work, a load or time condition, treatment of returns and a response when the conditions no longer fit.

Start with the result and resource that the rule must protect. If the existing rule already handles these returns adequately, use it through OPS.5 rather than reconstruct it for every admission. Identifying the resource that limits throughput, when that is uncertain, is a separate contribution from OPS.9.

### OPS.8.1:2 - Problem

A completion signal establishes that something finished within its stated boundary. The next start can nevertheless displace work still needed for the previous customer's result. A rule that waits for all possible later claims can create the opposite loss: useful resources remain idle while a completed item awaits a response that uses none of them.

The operator needs to compare these consequences before selecting a signal. The signal, the population limited by a card or count, the resource load and the customer's completion event may have different boundaries.

### OPS.8.1:3 - Forces

| Force | Practical tension |
| --- | --- |
| Earlier release and correction capacity | Starting sooner can advance new work but occupy the resource needed when an earlier result returns. |
| Simple counts and unequal demands | One freed place is easy to recognize; the returning and incoming jobs may require very different resources and times. |
| Protection and useful idle time | Holding capacity can preserve a deadline; excessive protection postpones work without improving the required service. |
| Feedback timing and decisions | Waiting can reveal whether a return is needed, but that information may arrive too late to protect the result. |
| Local pace and the receiving result | A constraint's completion can regulate replenishment while another resource or downstream join determines customer delivery. |

### OPS.8.1:4 - Solution

**Working sequence:** choose the receiving result → locate the proposed release signal → recover work that remains or can return → compare the next admission with the capacity it would leave → choose the rule and its response to feedback → operate it and reconsider the changed conditions.

The capacity comparison can return to the proposed signal, job selection, resource arrangement or commitment. A signal that works for one product mix may fail for another.

#### OPS.8.1:4.1 - Choose the completion and release events separately

Name the service to be protected, its receiving result and relevant horizon or deadline. Retain the event from which the customer has been waiting. Then identify the event currently proposed to permit another start: an operation completes, the selected constraint consumes its next ready job, a job leaves a controlled loop, acceptance arrives, or the remaining workload falls below a limit.

For a count limit, identify what enters and leaves its population. For a replenishment signal, identify the activity and ready supply it serves. Define readiness for the next operation using OPS.8; future outputs need not already exist.

Ask what obligation or operating work survives the signal. Trace it to the resource that would perform it. A card may be returned when a job leaves one loop even though that job still contributes load to another resource or a later visit. Preserve those contributions in the comparison.

#### OPS.8.1:4.2 - Recover known work and possible returns

For each resource that can change the release decision, establish the unfinished operations already assigned to it, their remaining occupancy, calendars and required times. Include known later visits by the same job. Count the resource use of each visit, while retaining one customer's result and waiting history.

For work that may return, identify the event that reveals the need, when the resource could be needed and the possible amount and kind of work. A supported bound, a small set of scenarios or a joint probability model can be enough, depending on the receiving question. Preserve shared causes: the same defect may return several jobs together.

Separate work already known to remain from allowance for work that is still contingent. If a return becomes known, replace its contingent allowance with the actual remaining work; do not add both for the same visit. When acceptance or another suitable event excludes that return within the selected horizon, release the corresponding allowance. An acceptance event does not remove separately retained warranty or other later service obligations.

When the possible return cannot yet be quantified, keep the supported comparison and identify which promised service remains unsupported. Further observation is useful when it can change the release choice. Release despite that uncertainty is a separate decision for a participant with the relevant authority, under commitments and protected conditions that permit the choice. It does not establish that the earlier service is protected.

#### OPS.8.1:4.3 - Test what capacity the next start leaves

Begin with the simplest consequence that can decide the question. In a fixed horizon, the known remaining occupancy, the proposed job's occupancy and a chosen allowance for returns can be compared with usable resource time.

For example, a resource with five usable hours cannot complete two hours of existing work, two hours of a protected return and two hours of new work within that horizon. Passing the total-hours comparison is only a necessary condition: readiness, precedence, joint resources and uninterrupted windows may still prevent placement. OPS.10.2 constructs that schedule or obstruction.

Match the comparison to the promised protection:

- For a stated return scenario, place that return and the new work with their readiness, access and deadlines.
- For protection over a bounded family, show that the selected response can handle every member of that family.
- For a probability requirement, use the joint model and the operating policy through OPS.10.1; a mean return load alone does not determine a service probability.

A policy that reacts to feedback must use information available at the time of its choice. If release is allowed before inspection, the policy needs an executable response when inspection later requires a return. It cannot choose an early start only in retrospect for the outcomes in which no correction was needed.

A workload-control norm can instead be a calibrated congestion-control quantity. Retain its definition and units: a route-position-weighted load is not the same quantity as occupied hours available before a deadline. Use its operating comparison for its intended purpose, and a finite schedule when the deadline question requires one.

#### OPS.8.1:4.4 - Compare signals and their return treatment

Compare the existing rule with a material alternative on the same arrivals, resources, receiving result and waiting origin. Keep the rule's actual mechanism visible.

| Candidate rule | What permits new work | What to resolve about returns |
| --- | --- | --- |
| Completion at a selected constrained activity triggers replenishment | That activity consumes the next ready supply and calls for its replacement. | Which later work can revisit this resource or occupy another resource needed for delivery? What ready supply and remaining capacity protect those visits? |
| A job's departure frees a place in a limited loop | The controlled population falls below its limit. | Is a return inside that loop, or admitted through another rule after departure? Retain its load wherever it will be served. |
| Remaining workload fits the selected norms | The candidate's contributions fit the resource-specific load rule. | Include repeated visits under that rule, distinguish known work from uncertain returns, and define what happens when feedback changes the load. |
| Acceptance permits the next start | The selected receiving event closes the exposure being protected. | Does waiting for this event preserve useful capacity, or unnecessarily hold a place while acceptance uses another resource? |

The names Drum-Buffer-Rope, CONWIP and workload control locate families of these methods; they do not settle the particular boundaries or exception rules. A rule can combine a replenishment signal with a return allowance or use a separate return queue. Evaluate that combination rather than assuming that choosing a name determines its behavior.

Compare the delay imposed on new work with the protected earlier result. If holding one job would starve an important resource, consider another ready job with compatible resource use, a smaller independently useful unit, another capable resource or a different start window. Any exception that spends protected capacity changes what the rule can support. OPS.7 and OPS.13 supply priority and commitment decisions when the two services cannot both be retained.

#### OPS.8.1:4.5 - Define the actions at release and feedback

Choose the next eligible work and the condition under which it can start. Make the condition usable in the operation's existing account: for example a freed loop place together with a reserved correction window, or a remaining-load calculation updated at inspection.

At a return, restore the work's readiness and resource demand, replace the corresponding allowance, and apply the selected priority and placement rule. Keep the original customer clock. A repeated service visit may restart a station's own interval without restarting the customer's wait.

At no-return confirmation, remove only the allowance that the event actually resolves, then reconsider held work. At late or ambiguous feedback, update the possible demand and the time left; absence of a message alone does not establish acceptance.

Observe whether the rule changes completion, total waiting, resource starvation, actual correction burden and displaced work. Reopen it when the return route, feedback time, service duration, resource access, product mix or receiving requirement changes. Stop redesigning once the existing inputs support a usable rule or a specific choice requiring changed conditions.

### OPS.8.1:5 - Archetypal Grounding

#### OPS.8.1:5.1 - An analysis returns during the next client session

A specialist finishes report X at hour zero. A review at hour one will either accept it or identify a correction requiring two uninterrupted specialist-hours. If a correction is needed, the corrected report is required by hour three. These are the two stated possibilities; the correction input becomes usable at hour one.

New job Y is a four-hour live session using the same specialist throughout. It is ready at zero, can start at any suitable time, must finish by hour seven and cannot be paused to perform X. Other resources do not change these conditions.

Releasing Y to run at 0–4 on X's first completion gives X no correction window before three. In the return case, the earliest correction is 4–6. The completion signal did not remove X's possible resource need.

A rule that preserves X's 1–3 correction window works as follows:

| Feedback at hour one | Specialist's next work | Completion of Y |
| --- | --- | ---: |
| X accepted | Start Y at 1 and finish at 5. | 5 |
| X needs correction | Correct X at 1–3; run Y at 3–7. | 7 |

The same observable rule handles both possibilities. It costs one hour of delayed Y completion in the no-return case relative to starting at zero. Holding a loop place until review and returning the place earlier while separately preserving the correction window can implement the same resource decision.

If Y instead needs one uninterrupted hour, with the other conditions unchanged, it can run at 0–1 and leave the same 1–3 correction window. Waiting for review before starting that Y would add delay without improving the stated protection of X.

Change the review time to hour two while retaining X's deadline three and its two-hour correction. Even an idle specialist can now finish that correction only at four. Keeping Y outside the system does not repair this obstruction. The operation needs earlier usable feedback, a genuinely shorter correction or a changed commitment.

#### OPS.8.1:5.2 - A free place and a full receiving resource

A manufacturing resource S is available continuously from 0 to 5. Job A is already running there from 0 to 2. A part X undergoing inspection elsewhere may need one additional two-hour visit to S; the answer becomes available at hour one, and any such visit must be complete by five.

A new job Y would require two uninterrupted hours at S and is also wanted by five. Its upstream activity has space and emits a release signal. There are no other operations needed for these completions.

Protecting the stated return and promising Y requires 2 + 2 + 2 = 6 hours in a five-hour window. The free upstream place does not remove this obstruction.

At hour one, one hour of A remains. If X is accepted, the remaining requirement is one hour of A plus two of Y; A finishes at two and Y runs 2–4. If X returns, its visit can run 2–4, but Y cannot also finish by five. Replacing the two-hour return allowance with X's known visit preserves this result; adding both would falsely claim eight original hours of demand.

This example uses full occupied hours and a finite deadline. A workload norm based on a different weighted quantity would need its own interpretation. If Y instead used an independent resource, holding it because of S's protected hours would require another reason.

#### OPS.8.1:5.3 - Waiting for an event that cannot consume the resource

An operation completes a job inside a machining loop. The remaining customer acknowledgment will use a separate administrative service, and the operating arrangement excludes any further use of the machining loop for this job in the horizon under consideration. The next eligible part has the required resources and fits the loop's release rule.

Keeping the machining-loop card until that acknowledgment would postpone the part without protecting any machining work in the stated horizon. Return the card at the loop's completion and retain the customer's outstanding acknowledgment in its own account. If inspection can instead return the part to that machine, this premise is lost and the release decision reopens.

### OPS.8.1:6 - Bias-Annotation

A board or card encourages attention to visible membership. Keep the resource work that survives a boundary crossing. Conversely, a policy designed around a painful return can retain every item until remote final acceptance; test whether that event can still change the protected resource use.

Expected load can make correlated returns appear manageable. Use the return pattern needed for the actual consequence. The cases above establish conditional consequences under stated inputs.

### OPS.8.1:7 - Conformance Checklist

- The receiving result, its time requirement and the proposed release event are distinguishable.
- Known remaining operations and possible returns retain their resource use, readiness and customer waiting origin.
- Any claimed protection states its scenario, bounded family or probability interpretation; an unresolved risk remains visible in the release choice.
- A total-load screen is followed by placement when calendars, precedence or uninterrupted work can change feasibility.
- Feedback replaces or releases the relevant allowance; it does not count the same return twice.
- The selected rule states what happens to both returning work and the next candidate, including conflicts that need a changed priority or commitment.
- A changed feedback time or return route can reopen the decision.

### OPS.8.1:8 - Common Anti-Patterns and How to Avoid Them

| Mistake | Consequence | Repair |
| --- | --- | --- |
| Treating a local completion as the end of resource responsibility | A new long job displaces an earlier correction. | Retain the remaining and contingent resource demands after that event. |
| Holding every place until remote final acceptance | Unrelated acknowledgment delays useful service. | Choose the controlled loop and retain obligations outside it in their own account. |
| Reserving for a return and then adding the same work again | Artificial overload blocks usable capacity. | Replace the matching allowance when the return becomes known. |
| Calling a mean return load protective | A burst or correlated return defeats the promised deadline. | Test the scenario, bounded family or joint probability required by that promise. |
| Resetting the customer's clock when work returns | A policy appears faster by losing earlier waiting. | Separate visit intervals from the original receiving interval. |

### OPS.8.1:9 - Consequences

The release rule can exploit available capacity while retaining the demand that may return. Its price is the information and coordination needed to distinguish the relevant events and resource contributions. A small deterministic comparison may suffice; larger operations can need the capacity and scheduling constructions.

Some conflicts remain real. Protecting an earlier correction can delay new work, and waiting for information can itself make the earlier result unattainable. The method exposes those choices for the responsible operating decision.

### OPS.8.1:10 - Architectural Rationale

A release rule can permit new work at local completion while the customer's result still requires another resource or a later visit. The method therefore couples that event with the work still needed and with the consequence of the next start.

The comparison works in both directions. Requirements of the receiving result constrain local starts; actual readiness and resource windows constrain the delivery that can be supported. A specialist's service, a loop's population and the customer's result can retain different boundaries without becoming inconsistent.

The rule need not model every future complaint. Its horizon and service question determine which returns matter. Distinguishing a known visit, a contingent allowance and new work makes updates local and keeps counts from replacing the work they are intended to regulate.

### OPS.8.1:11 - SoTA-Echoing

For the question “may this new job start while earlier work can return?”, the selected line combines a defined release signal with the remaining resource demand and the required service. Two simpler alternatives are one-in/one-out counting and waiting for final acceptance. The first can omit consequential load; the second can delay work without protecting that service. Sections 4.1–4.5 add the event, load, timing and feedback operations needed to decide between them. Cases 5.1–5.3 demonstrate different outcomes, including a condition under which holding capacity cannot help.

Hopp and Spearman, *Factory Physics*, third edition, §10.4 and §§14.3.1–14.3.2, supply CONWIP's controlled-loop construction and the distinction between counting jobs and accounting for unequal resource demands. Adopt the loop boundary and adapt the treatment of work diverted for rework: freeing a card requires retaining whichever other admission and load rules govern that work. No universal final-customer-acceptance boundary is inferred.

Steve Tendon, *The Book of TameFlow* (2022), printed pp. 117 and 138, supplies a concrete contrast: a constrained team's completion triggers replenishment, while the teaching exercise also permits a customer return for reprocessing and retains elapsed project time. Adopt the separate signal and customer-clock operations. Adapt the release choice to the actual return resource and timing through sections 4.2–4.5; the exercise does not establish that every operation can absorb any later correction.

[Thürer and Stevenson, *Workload Control in Job Shops with Re-entrant Flows: An Assessment by Simulation*](https://eprints.lancs.ac.uk/id/eprint/78334/1/Thurer_and_Stevenson_IJPR_Manuscript_Text_Figures_and_Tables.pdf), §§3.2 and 4.3–4.4, compare load accounting and release behavior for known repeated visits. Their corrected load weights route positions, and a starvation-triggered exception can exceed a norm. Adopt explicit repeated-visit accounting; distinguish that congestion policy from the finite occupied-hours test in 4.3. The study does not supply the timing or distribution of an as-yet-undiscovered correction.

[Prabhu and colleagues (2024)](https://doi.org/10.2478/mspe-2024-0014), the REM subsection on printed p. 149 and comparison on pp. 152–153, combine regular and re-entrant workload in a release rule. Adapt that combined-load comparison in 4.2–4.3: possible corrections still awaiting discovery need an allowance or scenario in addition to known visits, and resource-specific time limits remain. The study's rankings differ for flow time, throughput and modeled profit, supporting the receiving-question comparison in 4.4. Its rotor-blade simulation does not select a universally best rule. The occupied-hours screen here is an accounting bound followed by placement, rather than a protection claim inferred from an average population-time relation.

Reopen the selection when another signal or accounting method supports the same receiving result with less delay, information or coordination, or when returns, resource sharing, interruption, feedback timing or service requirements change. Compare outcomes at the original customer boundary; changing that boundary is not evidence that the rule improved service.

### OPS.8.1:12 - Relations

OPS.8 supplies the queue, readiness and protective-policy context. OPS.5 applies the resulting rule to a particular admission; OPS.6 continues an admitted case; OPS.7 and OPS.13 handle priority and commitment changes.

OPS.11.1 supplies the operating arrangement and resource relationships. OPS.15.1 constructs the visit, occupancy and customer-time quantities. OPS.10.1 compares capacity and uncertain service; OPS.10.2 constructs the finite schedule and revises it after feedback. These contributions let the release rule remain about when to start work rather than redefining the underlying quantities or scheduling method.

MMP.8 and MMP.8.SD supply sequential information and consequence reasoning when the choice depends on what can be learned before acting. C.11 supports choice under the actual alternatives and resources; C.29 retains correspondence between the modeled load and the operating work.

### OPS.8.1:End
