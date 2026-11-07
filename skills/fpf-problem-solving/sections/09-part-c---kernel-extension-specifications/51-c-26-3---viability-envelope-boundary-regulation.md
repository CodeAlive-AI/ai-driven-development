## C.26.3 - Viability-Envelope Boundary Regulation

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.26.3:1 - Problem frame

Use this pattern when architecture work is maintaining, recovering, or changing viable operating ranges across boundaries. The working problem is not "optimize one metric"; it is "keep a bundle of characteristics inside a viable region while disturbances, probes, candidate interventions, boundary conditions, and operating regimes change."

**What goes wrong if missed.** The team treats one dashboard value, stability slogan, or local metric as viability, while another envelope variable, intervention cost, boundary condition, or failure mode is already breaking the protected promise or function.

**What this buys.** The practitioner can derive the envelope from the work or promise being protected, locate the basis of its limits, and judge a disturbance or proposed change against all relevant constraints. A supported diagnosis can finish without a remedy; missing limits or effect grounds leave a bounded open question.

Use C.26.3 for the general envelope-regulation claim when several characteristics must remain inside a viable region under a disturbance and a candidate intervention, boundary condition, adaptation cost, or failure mode matters. Continue to use the direct control, quality, SRE, causal, measurement, boundary, and work patterns for the exact objects and claims they define; using them does not make the envelope result leave C.26.3.

QL is an optional coordination branch. Use `C.26` and its QL vocabulary only when a probe, frame, export, coarsening, order, incompatible representation, or measurement-changing-state issue remains after the ordinary patterns have carried their part and leaves a specific contextual-model obstruction that changes what may be inferred or done. FEP, allostasis, and active inference remain source analogies rather than a second entry condition.

| Working card | Value |
| --- | --- |
| Primary reader | Architect, platform lead, reliability lead, product manager, or operations lead preserving viability under changing conditions. |
| Primary EntityOfConcern | The exact viability bearer: either one System with its A.1 identity, one A.22 `U.Structure` identified by its four discriminators, or another subject identified under its direct identity rule. The primary result is a `C.2.1` episteme about that bearer, not a plan or the writing card. |
| Admissible move | Identify the bearer and protected result; obtain the relevant variables and limits from that result's requirements and available support; compare observed or expected effects, including costs and changed conditions. |
| Outside work | One-metric quality tuning, generic control theory, biological proof, full FEP doctrine, and ordinary feedback without an envelope/boundary claim. |
| What changes in practice | The team stops treating one dashboard value as viability and designs the actual envelope-regulation move. |

Plain glosses:
- `viability bearer`: a local lens position, not a kind or relation. If the bearer is a System, cite that System's A.1 identity. If it is a selected organization of systems, system-role kinds, and assignment occurrences, identify one A.22 `U.Structure` from exact independently identified constituents, exact selected obtaining relation occurrences, exact constraints as applied, and one named selection-use frame. Kind declarations or assignment occurrences listed together do not identify a Structure. A population or market slice instead needs a declared domain and effective reference scheme, membership or scope, and identity basis. If no branch supplies one exact object, stop.
- `protected promise / function`: the separately governed `U.PromiseContent`, stakeholder-value claim, function claim, operating-regime claim, commitment payload, or delivery promise whose continued satisfaction or realization the regulation decision is meant to protect. It is not a slot or part of the object in the local viability-bearer position.
- `service` or market wording: the wording does not itself identify the viability bearer. Apply the A.1 System branch, the four-discriminator A.22 Structure branch above, or the population/market-slice branch, as applicable. Keep claims about promise content, access points, assignments, commitments, Work occurrences, evidence, and direct relations separate. If no branch identifies one exact object, stop; do not turn the phrase or a list of role kinds and assignments into a bearer kind, situation kind, or bundle.
- `viability envelope`: the region of declared characteristic values within which the exact object remains inside the viability bounds stated for the current protected claim or use.
- `envelope variable`: one characteristic that must stay within bounds, such as latency, reliability, support load, compliance exposure, safety margin, energy, or operator attention.
- `actuator` / `candidate intervention`: *actuator* is a control-theory or source label, not an FPF kind and not a synonym for Work. Use *candidate intervention* only as a local prompt until its proposal-side object is recovered: a Method; a `U.MethodDescription` or policy episteme; a proposed setting change; a `U.WorkPlan`; an access or permission claim; or a Bridge proposal or description. Separately identify any dated `U.Work`, independently grounded `U.Transformation`, obtaining relation occurrence, or resulting state claimed to exist. Keep these objects distinct.
- `allostasis`: preserving function through separately governed changes to settings, environment relations, boundary conditions, or operating regime when circumstances change.

### C.26.3:2 - Problem

Teams often collapse viability into one dashboard value or fixed target. They optimize latency and increase operator load. They improve availability and increase compliance exposure. They preserve one metric while exhausting the team, hiding risk, or making recovery slower.

A second failure is passive sensing. A metric, probe, dashboard, alert, or health check is treated as a neutral window into viability, even when its use or publication changes behavior through separately grounded Work, interaction, or governance, or hides unmeasured dimensions.

A third failure is static stability. Teams say "keep the system stable" as if stability always means holding one internal variable fixed. In real architecture work, preserving viability may require a candidate intervention. Recover whether the proposal concerns a Method or description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description. Separately identify any dated Work, actual change, obtaining relation occurrence, or resulting state claimed to exist; words such as caching, staffing, routing, protocol, and measurement design do not choose among them.

### C.26.3:3 - Forces

| Force | Tension |
| --- | --- |
| Bundle vs scalar | Viability usually concerns a bundle, but dashboards often expose one or two proxies. |
| Stability vs change | The system may preserve function by changing internal settings, external environment, boundary conditions, or operating regime. |
| Sensing vs intervention | A measurement value is not a change or Work. Its use may report, probe, or participate in a separately grounded behavior-changing Work, interaction, or governance claim. |
| General envelope regulation vs optional QL coordination | Use C.26.3 for the envelope-regulation claim and `C.25`, `U.Dynamics`, `A.6`, `A.15`, and `C.16` for its exact constituent claims and objects. Add `C.26` / QL only under the residual-obstruction condition in §1. |
| Light use vs dynamics detail | Rate, inertia, damping, latency, and effort of the recovered intervention object or resulting change matter only when load-bearing. |

### C.26.3:4 - Solution

Use C.26.3 when the work must regulate a multi-characteristic viability envelope under disturbance. Use `C.25`, `U.Dynamics`, measurement, boundary, causal, and work patterns to state the exact qualities, changes, observations, relations, and Work on which the envelope claim relies. Add `C.26` / QL only under the residual-obstruction condition in §1. If no such obstruction remains, omit the QL fields and checks; do not discard an otherwise useful envelope-regulation result.

Start with these recognition questions; ordinary prose can supply the answers.

| Mini-entry | Question |
| --- | --- |
| Viability bearer | Is it one System with its A.1 identity, one A.22 `U.Structure` with exact constituents, selected obtaining relations, applied constraints, and a named selection-use frame, or a population/market slice with its own declared basis? A list of system-role kinds and assignment occurrences is not a bearer. |
| Protected promise / function | Which `U.PromiseContent`, stakeholder value, function, operating regime, commitment payload, or delivery promise is protected? |
| Envelope variables | What would prevent the protected work or result, which quantities or conditions reveal that failure, and what requirement or resource limit sets their admissible bounds? |
| Disturbance | What pushes the exact object in the local viability-bearer position outside the declared envelope? |
| Sensor / probe / candidate intervention | What reads the situation? What change is proposed, which exact object carries that proposal, and what actual Work, transformation, relation, or resulting state exists, if any? |
| Trade-off / failure | What gets worse, what cost is paid, and what failure would show the envelope move did not work? |

Use the fuller account below when the receiving viability decision needs distinctions missing from the recognition note. Reuse adequate existing content. A supported diagnosis can finish without an intervention proposal.

Full envelope-regulation record:

| Field | Question |
| --- | --- |
| Viability bearer | Is it one System with its A.1 identity, one A.22 `U.Structure` with exact constituents, selected obtaining relations, applied constraints, and a named selection-use frame, or a population/market slice with its own declared basis? A list of system-role kinds and assignment occurrences is not a bearer. |
| Protected promise / function | Which `U.PromiseContent`, stakeholder value, function, operating regime, commitment payload, or delivery promise is protected? |
| Current service/access claims, if any | Which independently governed service/access claims are current, and what exact subjects, relations, and subject patterns do they name? |
| Envelope variables | Which characteristics or quality-bundle dimensions define viability? |
| Viable region / bounds | Which requirements, safety or operating limits, commitments or available resources determine acceptability for this use? Distinguish those criteria from observed values and provisional targets. |
| QL cue or formal cue if retained | Which probe, order, export, coarsening, incompatible-frame, open-information-system update law, probe-frame relation, export admissibility, or measurement-changing-state cue remains after ordinary viability patterns are active, and what specific contextual-model obstruction does it leave for inference or use? |
| Disturbance | What pushes the exact object in the local viability-bearer position outside the declared envelope? |
| Sensors / probes | Which metric, dashboard, alert, health check, review, trace query, observation setup, or probe reads the envelope, and can it change behavior or hide unmeasured dimensions? |
| Candidate intervention and recovered direct object | What change is proposed? Recover whether the proposal concerns a Method or description, setting proposal, `U.WorkPlan`, access or permission claim, or Bridge proposal or description. Separately identify any dated `U.Work`, independently grounded `U.Transformation` or other actual change, obtaining relation occurrence, or resulting state already claimed to exist. Which exact objects are current, and under which subject patterns? |
| Boundary condition preserved / changed | Which access, ownership, context, interface, promise, or environment condition matters? |
| Trade-off condition | Which envelope dimension is protected, relaxed, delayed, made more expensive, or deliberately held constant? |
| Adaptation cost | What is spent, delayed, damaged, risked, or made harder by the adaptation? |
| Failure mode | What breakdown, drift, unsafe persistence, or loss of viability shows that the move failed? |

#### C.26.3:4.1 - Homeostasis and allostasis reading

`Homeostasis` means keeping a parameter or bundle inside viable bounds. `Allostasis` means preserving functioning through separately governed changes to internal settings, external relations, boundary conditions, or operating regime when circumstances change.

Use these terms when their distinction changes the interpretation of the viability decision.

#### C.26.3:4.2 - Finish conditions

Finish with one of these results:

| Result | Meaning |
| --- | --- |
| Envelope claim | State the exact bearer, protected result, variables and justified bounds, disturbance, observations and failure condition. Include sensors/probes and boundary conditions where they affect the conclusion; a proposed regulation also needs its candidate change, trade-off and adaptation cost. Ordinary prose may carry these claims. |
| Candidate-intervention recovery or redesign | Recover the direct object first. Revise only the current proposal—its Method or description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description—and identify any dated Work, actual change, obtaining relation occurrence, and resulting state separately. A fixed F.9 Bridge is not an intervention object: after an endpoint sense or profile changes, test another F.9 candidate and identify it only if the predicate obtains. |
| Measurement/probe redesign | Redesign a dashboard, alert, health check, readiness score, or review process because it distorts the envelope it reports. |
| Neighbor coordination without QL | Keep the C.26.3 envelope-regulation claim and use `C.25`, `C.16`, `A.6`, `A.15`, `U.Dynamics`, `C.18`, `C.19`, or `A.19` for the exact neighboring objects and claims. Omit `C.26` / QL when no contextual-model obstruction remains. |
| No envelope claim | Drop the viability-envelope wording when the exact bearer and its identity basis, protected promise/function, viable region/bounds, disturbance, or failure mode cannot be stated. A proposed regulation also needs at least one candidate intervention recovered under its direct pattern and its adaptation cost. An envelope diagnosis with no intervention yet may retain only the supported diagnostic claim. |

#### C.26.3:4.3 - Metric-induced distortion

Name sensors, probes, dashboards, alerts, metrics, disturbances, and candidate interventions in the envelope claim when they matter. They participate only in world-side relations defined by their direct patterns; C.26.3 does not infer a generic viability relation from their appearance in the same card. A probe or dashboard may still affect behavior, but that effect needs its own grounded claim.

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Metric-as-envelope | A proxy is treated as the whole envelope. | Recover the exact object filling the local viability-bearer position and the pattern used to identify it, protected promise, full envelope, unmeasured dimensions, and admissible use. |
| Goodharted viability | Actors optimize measured slots while damaging unmeasured survivor relations or future adaptability. | Use `C.26.1` when the probe changes represented state but its output is used as a passive read for the decision; add evidence for unmeasured envelope dimensions. |
| Intervention overfit | A proposed or enacted move preserves one parameter while pushing another cost, latency, boundary relation, or promise outside bounds. | Add the trade-off condition, authority, latency, adaptation cost, and failure mode; recover any Method, description, plan, Work, change, setting, or relation under its subject pattern. |

#### C.26.3:4.4 - Conditional dynamics detail

When rate, acceleration, second-order change, inertia, damping, resistance, effort, or the strength and latency of a recovered intervention or resulting actual change is load-bearing, state:

- what rate or acceleration matters;
- what slows or speeds the change;
- whether the rate of change itself is changing, rebounding, overshooting, or damping out;
- which inertia is useful and which is harmful;
- which recovered intervention object is proposed, what Work, relation, or setting change can lawfully realize it, and which independently grounded actual change affects the envelope fast enough;
- which evidence shows the dynamic state.

If those variables are not load-bearing, do not force dynamics machinery into the case. The short recognition note or the full envelope-regulation record is enough.

#### C.26.3:4.5 - Claim identity and operational sequence

Identify an envelope account under `C.2.1` when its exact claim-bearing identity is used: its EntityOfConcern is the viability bearer, its claim content states the envelope, and its effective ReferenceScheme determines how that content is read. A record is one possible presentation.

Keep the actual object of a proposal clear. A setting or policy proposal may be part of that account's claims; mentioning it does not require another episteme. A separately identified proposal, `U.WorkPlan`, Method, description or relation retains the identity supplied by its direct pattern. In particular, a modal F.9 proposal designates possible endpoints and a profile; it does not establish an obtaining Bridge.

The first useful move is to replace a one-scalar stability story with an inspectable envelope-regulation claim for the decision.

Envelope-regulation sequence:

1. Point the local viability-bearer position to one exact object. For a System, cite its A.1 identity. For selected organization, cite one A.22 `U.Structure` through exact independently identified constituents, exact selected obtaining relation occurrences, exact constraints as applied, and one named selection-use frame; a role-kind/assignment list is insufficient. For a population or market slice, state its declared domain and effective reference scheme, membership or scope, and identity basis. Then name the separately defined promise or function being preserved. If no branch identifies the bearer, stop.
2. Recover the protected work or result from the receiving requirement, promise, operating procedure or current failure. Follow what must remain possible: successful outputs, necessary inputs, supporting work, resources and timing. For each relevant way it can fail, identify the quantity or condition that distinguishes continued operation from that failure. Keep the subject of each constraint explicit; support-team load is not automatically a characteristic of the service System.
3. Obtain each bound from its governing basis. Reuse an applicable customer requirement, commitment, safety or operating limit, or an established resource constraint. Where the constraint is capacity, relate the demand in the stated window to the people, equipment, time or other provision actually available under that same workload and service condition. A historical average describes performance; it does not set acceptable performance. If a needed limit is absent, recover it with the party entitled to set the requirement or make the trade-off. Until then, a proposed threshold remains a scenario assumption: return the effects or feasible range and identify the unresolved acceptability question.
4. Identify the disturbance or regime change and the observations needed to locate the current state against those bounds. Use existing observations where adequate. Recover what each sensor or probe measures, including timing, coverage and a supported behavior-changing effect; use `C.26.1` for a material unresolved interpretation.
5. If regulation is needed, trace the failure to an available change in the mechanism, resource, operating rule or boundary condition. Reuse a suitable domain Method. When the dependency is unresolved, `C.28.CM` develops the causal account; `C.28.MR` derives consequences of a specified mechanism change, and `C.29` contributes when formulation or transfer needs mathematical work. Recover the proposal's object and distinguish it from any performed Work, actual transformation or obtaining relation. An F.9 endpoint/profile change requires testing the resulting Bridge candidate; Work does not revise a fixed Bridge occurrence.
6. Follow each proposed change to every affected constraint, including displaced work, transition time and adaptation cost. Use a calculation, simulation, case evidence or other justified account appropriate to the decision. Keep its assumptions and uncertainty visible. Improving one variable is sufficient only if the remaining required conditions also hold.
7. Return the supported diagnosis or conditional proposal. A known violation can rule out restoration of the envelope even while another effect remains unknown. A positive viability claim needs all its required conditions supported; an unresolved limit or effect may instead warrant a restricted action, further inquiry or no change. New inquiry is conditional on its attainable contribution to the receiving decision, not a required extra step.
8. Add rate, inertia, damping, latency, resistance, acceleration or a reprobe condition only when it changes that result.

Ordinary output: explain the viability bearer, variables and bounds, disturbance, observations and failure condition. When regulation is proposed, add the identified proposal, trade-off and adaptation cost. A record is useful when its layout helps recover those distinctions; ordinary prose can preserve them.

Finish with the supported diagnosis or the proposal it warrants. Use the proposal's direct pattern for its development and any later execution or change; keep the supported envelope claim separate from those results. If its necessary grounds are missing, retain only the narrower supported claim or return the missing basis.

#### C.26.3:4.6 - Viability envelope record

When a record is useful, it can present the envelope claim and its grounds. Retain only the fields consumed by that claim or receiving action, while keeping its subject and any needed episteme identity recoverable.

```text
exact object in the local viability-bearer position and pattern used to identify it: ...
protected promise or function: ...
envelope variables: ...
viable region: ...
disturbance: ...
sensors or probes: ...
candidate intervention and recovered direct object: ...
authority and latency for the applicable Work, setting change, or relation: ...
boundary condition: ...
trade-off condition: ...
adaptation cost: ...
failure mode: ...
re-probe or destabilization condition: ...
```

Changing the ClaimGraph content changes the claim and therefore identifies another episteme under `C.2.1`. A new layout, publication occurrence, form, or carrier can leave the episteme unchanged. New evidence can change the support for the claim without changing that claim; if the asserted ClaimGraph changes, the result is another episteme.

Well-formedness constraints:

- the local viability-bearer position points to one exact object and introduces no kind or relation: a System has its A.1 identity; an A.22 `U.Structure` has exact independently identified constituents, exact selected obtaining relation occurrences, exact constraints as applied, and one named selection-use frame; a population or market slice has its declared domain and effective reference scheme, membership or scope, and identity basis; a list of system-role kinds and assignments satisfies none of these branches;
- service or access wording names each current object and relation separately—the exact object in the local viability-bearer position, promise content, system, system-role assignment, commitment, Work occurrence, evidence, or another direct relation—through the pattern that defines that object or relation; the wording creates neither a root bearer nor a bundle;
- this pattern's multi-characteristic branch keeps every dimension needed by the protected result; if one characteristic already answers the question, use the adequate single-characteristic account;
- at least one candidate intervention is named when the text proposes regulation rather than only diagnosis, and its proposal-side Method, description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description is recovered under the subject pattern; any dated Work, actual transformation, obtaining relation occurrence, or resulting state is identified separately;
- authority and latency are stated only for an object to which they apply; a description, Method, plan, setting label, Bridge description, or resulting state is not made an actor or Work by this card;
- when regulation or adaptation is proposed, its adaptation cost is named, because allostasis hides cost when phrased as "stability through change";
- the failure mode is named, because viability is otherwise indistinguishable from optimism.

#### C.26.3:4.7 - Sensor, probe, candidate-intervention, and metric split

Do not let one dashboard value stand for the whole envelope.

| Item | Viability-facing question |
| --- | --- |
| Envelope variable | Which quality, resource, promise, risk, or operating dimension is inside/outside viable range? |
| Sensor / observation source | Which instrument, observation procedure, trace or report supplies a reading, and what quantity or condition does that output represent? |
| Probe | Which deliberate query, measurement, review or experiment supplies information, and does its interaction with the subject affect the needed interpretation? |
| Candidate intervention | What change is proposed? Recover whether cache, throttle, routing, staffing, protocol, escalation, access, bridge, or context-split wording denotes a Method or description, setting proposal, plan, access or permission claim, or Bridge proposal or description. Separately identify any dated Work, actual transformation or other change, obtaining relation occurrence, or resulting state claimed to exist. |
| Boundary condition | Which access, ownership, context, interface, promise, environment, or information constraint shapes the envelope? |
| Adaptation cost | Which latency, risk, support load, or compliance exposure is incurred, and which effort, attention, energy, trust, or future flexibility is spent, reduced, or put at risk? |

A metric value or dashboard carrier is neither Work nor an actual change. Its use, publication, or a surrounding governance routine may participate in a separately grounded behavior-changing claim. When Work is asserted, recover each actual performer's A.13 core and independently admit the dated occurrence under A.15.1. If the claim must also identify the assignment under which the Work was performed, name that assignment and check the relation separately through F.6. Name any changed setting, actual transformation, access or permission relation, or boundary relation separately. Repairing one envelope variable may still damage another.

#### C.26.3:4.8 - Homeostasis, allostasis, and architecture work

Homeostatic wording is useful when the claim concerns keeping a variable or bundle inside a stable range. Allostatic wording is useful when preserving the named function requires one or more separately governed setting, boundary, environment, access, staffing, routing, protocol, cache-policy, or operating-regime changes. The wording does not decide whether each item is a Method, description, plan, Work, transformation, relation, or resulting state.

Use the minimal reading that carries the case:

| Reading | Use when | Practical output |
| --- | --- | --- |
| Scalar quality repair | One characteristic or Q-bundle dimension is enough. | Use `C.16` for the Characteristic/measurement claim, `C.25` for an engineering-quality bundle when needed, and evidence patterns for the actual reliance. |
| Homeostatic envelope | The target is to keep a bundle inside a stable range under disturbance. | State variables, range, disturbance, sensor, candidate intervention with its recovered direct object, and failure mode. |
| Allostatic envelope | Function is preserved through one or more separately governed changes. | State the proposal's exact Method or description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description; separately state any dated Work, actual transformation or other change, obtaining relation occurrence, resulting state, and moved cost. |
| Probe-coupled viability | The measurement, dashboard, review, or readiness check changes the envelope it reports, but its output is used as a passive read for the decision. | Coordinate with `C.26.1`. |
| Enacted viability state | Coordinated work, behavior, or traces support a collective-state reading relevant to the envelope that no single report or export faithfully carries. | Coordinate with `C.26.2`. |

Do not call every adaptation allostasis. The term earns its place only when stability-through-change is the useful architecture reading.

#### C.26.3:4.9 - Case bank and near misses

| Case | Supported C.26.3 reading | Near miss / reroute |
| --- | --- | --- |
| Checkout cache under spike | Cache aggressiveness preserves latency but increases stale payment-failure status and support load. | If only cache latency is at issue, use ordinary performance and quality-bundle patterns. |
| Smart-building energy control | Energy, comfort, privacy, occupancy, and abrupt weather changes form one envelope with sensors and candidate interventions recovered under their subject patterns. | If the case only tunes one thermostat setting, use ordinary control/measurement language and state any actual setting change separately. |
| Incident staffing | A proposed staffing intervention may preserve recovery time while increasing coordination overhead and error risk; recover whether the proposal concerns a Method or description, staffing or assignment-setting proposal, or WorkPlan. Separately identify any dated staffing Work, changed assignment relation, other actual change, or resulting state claimed to exist. | If staffing is merely a work-allocation issue, use `A.15` and planning patterns. |
| Compliance exposure | A fast remediation path lowers outage time but increases evidence gaps and audit risk. | If audit evidence is primary, use `A.10` for evidence reliance and `B.3` only for an actual named assurance claim; keep C.26.3 only for envelope trade-off. |
| Service boundary split | Splitting a service may reduce deployment coupling while changing endpoint senses and increasing operational support-transfer cost. | If only cross-local semantic correspondence is at issue, resolve the exact senses and test the resulting F.9 candidate; if the split changes the viability envelope, use C.26.3. |
| Body-temperature analogy | Function may be preserved by clothing, room air, activity, or exposure, not only internal heat production. | Use only as explanatory analogy; do not make biology the proof for software. |

#### C.26.3:4.10 - Source-to-pattern translation

Allostasis, active inference, FEP, Markov blankets, and computational-boundary sources are useful here only after translation into FPF architecture terms:

| Source-side term | FPF-facing translation |
| --- | --- |
| Homeostasis | Keep one parameter or bundle inside viable bounds. |
| Allostasis | Preserve function through one or more separately governed changes to settings, environment, boundary condition, or operating regime; the source term does not determine Method, description, plan, Work, transformation, relation, or resulting state. |
| Active inference / perception as action | Measurement, sensor placement, and action have cost and can change later state estimates. |
| Markov blanket or computational boundary | Statistical or probabilistic boundary-lens cue only after recovery. Accepted local Markov dynamics stay with `A.3.3`; lens use stays with `C.29`. Use C.26 when quantum-like, probe, frame, or measure-model-act wording exposes the required contextual-model obstruction; use C.26.3 when the envelope-regulation question in §1 remains. Physical boundary, interface module, component, functional element, boundary description or publication, and agency threshold require their subject patterns; Markov wording does not admit them by itself. |
| Criticality / metastability | Stability may be regime-bounded and fluctuation-bearing, not one final fixed point. |
| Expected free energy / precision control | Information gathering, action, and confidence have cost; use only when those costs change the architecture decision. |

Use the translated source contribution to explain an envelope constraint or choose the next needed operation—for example, compare a probe redesign or a proposed setting change. The operational sequence and direct subject patterns govern the resulting proposal, observation or actual change; a source analogy supplies none of their missing grounds.

### C.26.3:5 - Archetypal Grounding

In this constructed case, a platform team must preserve checkout service during a traffic spike. The receiving service requirement specifies both timely responses and sufficiently current payment-failure status. The team traces a proposed increase in cache duration: serving more requests from cache may reduce delay, while retaining old status longer can mislead customers and increase support contacts.

`CheckoutSystem-1` is independently recognized under A.1 as the deployed System. `CheckoutPromiseContent-1` separately states the checkout outcome and reliability on which customers may rely. For this example, the receiving requirement sets the latency limit at 250 ms for the highest five-minute p95 in the incident hour and the stale-status limit at 1% of statuses in that hour. The support limit is derived from the provision reserved for this incident: four available specialists can each handle up to five comparable contacts within the hour under the stipulated workload, giving reserved capacity for 20. These are constructed requirement and capacity premises, not limits inferred from the observed averages.

Compare two matched one-hour windows under the stipulated spike condition, before and after the cache-setting change:

| Constraint and subject | Required bound | Before cache-setting change | After cache-setting change |
| --- | --- | ---: | ---: |
| CheckoutSystem-1 request latency, highest five-minute p95 within each hour | <=250 ms | 350 ms | 180 ms |
| CheckoutSystem-1 stale payment-failure statuses over the incident hour | <=1% | 0.2% | 3% |
| Incident support demand: customer contacts requiring handling during that hour | <=20 | 10 | 45 |

The observed values are constructed case premises. Latency improves, but in the changed setting the status constraint is violated and support demand exceeds the stipulated handling capacity, so the declared envelope is not restored. The decision combines properties of CheckoutSystem-1 with demand on the incident-support team. The support figure counts contacts requiring handling; a count of completed handling would concern actual support Work. Operator attention, if added, would concern the people handling those contacts. Fulfillment of CheckoutPromiseContent-1 still needs its own evaluation.

If the acceptable stale-status bound has not been established, retain the observed 3% and the finding that support demand of 45 contacts exceeds capacity for 20. This does not settle whether 3% is acceptable. Recover the correctness requirement from the receiving use and its requirement setter; until then, the positive envelope verdict remains open. If the receiving task asks only whether the proposed cache setting restores all already declared constraints, the excess demand is enough to answer no.

A dashboard query is an observation operation unless a behavior-changing effect is separately established.

Retain the diagnosis that the changed setting improves latency while violating other envelope constraints. The dependency through cached status suggests comparing a shorter cache duration or bypassing the cache for payment-failure updates; either could increase upstream work and latency. Recover the relevant update and read paths before predicting that trade-off. A valid existing account can settle it; otherwise the missing effect remains a question rather than an observed remedy. Recover the proposal's object, adaptation cost, applicable authority and realization latency before choosing it; a planned enactment belongs in a WorkPlan. Missing intervention evidence leaves the diagnosis useful. If support capacity is independently revised to 50 comparable contacts per hour under the same conditions, the same demand of 45 contacts satisfies that revised constraint, but the 3% stale-status result still exceeds the retained 1% requirement.



### C.26.3:6 - Bias-Annotation

This pattern emphasizes constraints that a favorable scalar can hide, including damage to another envelope dimension.

It also biases authors toward actionable architecture work. The pattern asks which direct object a boundary, access, protocol, staffing, cache, throttle, bridge, or measurement proposal denotes and how quickly its separately governed effects can matter. For a particular dated Work claim, establish each actual performer's A.13 core and independently admit the dated occurrence under A.15.1. Add F.6 attribution only if the account must also identify the assignment under which that Work was performed. Any actual transformation is grounded separately.

Use `C.25` alone when one quality bundle or metric can be handled without envelope, disturbance, boundary condition, recovered candidate intervention, adaptation cost, or viability failure mode.

### C.26.3:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-C26.3.1 | The viability bearer is one exact System under A.1, one exact A.22 `U.Structure` under all four identity discriminators, or another exact subject under its direct identity rule; the local position introduces no kind, relation, or configuration object. |
| CC-C26.3.2 | The protected promise or function is named. |
| CC-C26.3.3 | Variables and bounds follow from the protected result's requirements or available provision. Observations, proposed targets and justified acceptability criteria remain distinct; an unknown required bound limits the viability conclusion. |
| CC-C26.3.4 | Disturbance class and scenario/window are named. |
| CC-C26.3.5 | Sensors/probes and their possible behavior-changing or dimension-hiding effects are named when measurement carries the envelope claim. |
| CC-C26.3.6 | Each candidate intervention is recovered as a proposal about an exact Method, description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description; dated Work, actual change, obtaining relation occurrence, and resulting state remain separate. A fixed F.9 Bridge is never the object revised or ended by Work; an endpoint/profile change opens a new candidate that must pass F.9 independently. |
| CC-C26.3.7 | The boundary condition is stated. When regulation is proposed, the trade-off condition and adaptation cost are stated. |
| CC-C26.3.8 | The failure condition is stated; a reprobe or destabilization condition is included when the receiving use depends on it. |
| CC-C26.3.9 | Metrics or dashboards are not treated as the envelope itself. |
| CC-C26.3.10 | The QL cue / formal cue is named if QL wording is retained. |
| CC-C26.3.11 | QL wording appears only when probe, order, export, coarsening, or incompatible frame interaction remains load-bearing and satisfies C.26's contextual-model obstruction condition. |
| CC-C26.3.12 | Rate/inertia/damping/effort and second-order dynamics variables appear only when load-bearing. |
| CC-C26.3.13 | Homeostasis, allostasis, active inference, and Markov-boundary wording are restored into FPF subject patterns before they carry the claim; Markov-blanket wording does not by itself create boundary, interface, component, agency, or viability authority. |
| CC-C26.3.14 | The result retains the supported diagnosis or proposal and identifies any missing bound or effect that prevents the required viability conclusion. |

### C.26.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| One metric as viability | Availability, latency, or score stands for the whole envelope. | Add the exact object filling the local viability-bearer position and the pattern used to identify it, protected promise, other dimensions, and failure mode. |
| Fixed setpoint thinking | Stability means one variable must never move. | Ask whether allostasis preserves function by changing settings, environment, boundary, or regime. |
| Passive sensor assumption | A dashboard is treated as neutral even after it changes behavior. | Use `C.26.1` when the false passive reading changes the architecture decision; use evidence patterns for its support. |
| Candidate intervention without a recovered object, predicate, or applicable authority | The text recommends a change without recovering its proposal-side Method, description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description; fails to identify separately any dated Work, actual transformation, obtaining relation occurrence, or resulting state on which it relies; or claims Work no system can perform in time. | Recover the proposal-side object first; identify every actuality separately under its subject pattern; state authority and latency only for the applicable Work, change, or relation. |
| Biological proof jump | Homeostasis or FEP language is used as proof for software or organizations. | Treat it as modeling discipline and apply existing FPF patterns to claims. |
| Markov-blanket collapse | A statistical separation, physical interface, interface module, functional element, component, boundary description, and agency threshold are all called the Markov blanket. | Split the source phrase through `A.6.RSIR`: use `C.29` or `C.26` for lens use; use `A.1` plus the direct relation pattern for holon delimitation or boundary crossing; use `A.6.P`, `A.6.0`, and `A.6.5` for relation, signature, or slot claims; use `A.6.M` for module-interface claims; use `A.6.F` for functional claims; use `A.14`, `C.13`, or `B.3.5` for component claims; use `C.2.1` for description content, `C.30.AD` for architecture descriptions, `E.24.PUB` for a publication occurrence or form, and `E.17` when multi-view publication is current; use `A.13` for agency criteria, `C.16` for measurement construction, and `A.19` for a `CharacteristicSpace` or reusable `CharacteristicSpacePredicate` over it. |

### C.26.3:9 - Consequences

The envelope account makes trade-offs visible: preserving one characteristic can violate a constraint supplied by another claim. It supports a diagnosis, or comparison of independently identified proposals, while the direct subject patterns continue to govern the proposed objects and any actual changes.

The cost is that simple metric stories become less simple. That is acceptable when the metric story hides another envelope dimension, an intervention cost, a boundary condition, or a failure mode.

### C.26.3:10 - Rationale

Ordinary quality-bundle work does not always show boundary conditions, candidate interventions and their recovered direct objects, disturbances, adaptation cost, and failure modes together. C.26.3 coordinates those elements while preserving ordinary FPF patterns.

The QL lens is secondary. It matters when the way viability is probed, exported, or coarsened leaves a contextual-model obstruction that changes the state reading or admissible use of the representation.

### C.26.3:11 - SoTA-Echoing

| Pattern claim | Practice source | Pattern implication | Adoption stance |
| --- | --- | --- | --- |
| Viability maintenance is not fixed-value homeostasis only; stability can be relational, variational, dynamic, allostatic, metastable, and resilient. | [Conceptual foundations of physiological regulation incorporating the free energy principle and self-organized criticality](https://www.sciencedirect.com/science/article/pii/S0149763423004281). | Use viability envelopes and stability-through-change; reject one-scalar optimization and "all architecture is homeostasis." | Adapt as architecture-facing envelope discipline. |
| Action and perception are coupled under partial observability and cost. | [Active inference as a theory of sentient behavior](https://www.sciencedirect.com/science/article/pii/S0301051123002612). | Treat sensors, probes, dashboards, and source-labelled actuators as relevant to the envelope claim when they change behavior or viability; recover each candidate intervention as its exact FPF object before relying on it. | Adapt for measurement-as-action and planning cost. |
| Active-inference engineering already appears in energy/building control under privacy, partial observability, evolving conditions, and abrupt changes. | [Active Inference for Energy Control and Planning in Smart Buildings and Communities](https://arxiv.org/abs/2503.18161). | Use engineering examples cautiously: they show the kind of control problem, not settled FPF doctrine. | Use as emerging engineering anchor. |
| Boundaries can be statistical or computational descriptions of what a system can measure, model, and affect. | [The Computational Boundary of a Self](https://philpapers.org/rec/LEVTCB-3) and [The Markov blankets of life](https://philarchive.org/rec/KIRTMB). | Name boundary conditions and information constraints without reifying a boundary substance. | Adapt with map-territory caution. |
| Excess Bayesian / active-embodied inference shows the cost of moving sensor, body, instrument, or access point to obtain a discriminating observation. | [Connecting the free energy principle with quantum cognition](https://www.frontiersin.org/articles/10.3389/fnbot.2022.910161/full). | Treat probe placement, access placement, and observation cost as part of viability-envelope work when they change the decision. | Adapt for probe/action cost, not as a replacement for ordinary Bayesian or active-inference routes. |
| Platform and software engineering already treats many quality concerns as trade-off bundles. | Reliability, incident, platform, compliance, energy, support, operator-load practice, and [Google SRE SLO / error-budget practice](https://sre.google/workbook/implementing-slos/), coordinated with `C.25`. | Make the quality bundle explicit, recover each candidate intervention as its direct object, and state applicable authority, latency, adaptation cost, and failure mode. | Adopt through FPF quality-bundle routes. |

Worked-slice discipline from these rows:

- state the envelope before importing source terminology;
- use a source analogy only through the subject claim and relations it actually supports;
- keep sensors, probes, metrics, candidate interventions, and every recovered direct object distinct;
- state adaptation cost and failure mode;
- apply ordinary quality and measurement patterns to one-scalar quality concerns.

### C.26.3:12 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: braking, throttling, cadence, recovery, or stabilization moves in claims such as slow rollout protecting support capacity, request throttling preventing collapse, or cadence change preserving attention/team health.
- This pattern keeps: viability bearer, protected promise/function, viable region, disturbance, sensor/probe/candidate-intervention/direct-object split, adaptation cost, and failure mode.
- Non-admissible use: stabilization wording is not a viability envelope, and C.27 is not the pattern for all stability-through-change claims.
- Exit: if the claim being made is only better quality, healthier team, or more resilient service without a declared viability envelope, use C.25, E.13, or the relevant quality/proxy/value pattern rather than C.26.3 or a C.27 profile.

- Builds on: `C.26`, `C.25`, `U.Dynamics`, `A.6`, `A.15`, `C.16`, `A.10`, `B.3`, `A.3`, `A.19`, `C.18`, `C.19`.
- Coordinates with: `C.26.1` when a state-changing probe's output is used as a passive read for the decision; `C.26.2` when coordinated work, behavior, or traces support a collective-state reading that no single report or export faithfully carries.
- Does not replace: ordinary quality-bundle patterns, generic control theory, full FEP doctrine, or biological homeostasis claims outside FPF bridge and loss discipline.
- Name: `Viability-Envelope Boundary Regulation` names architecture work over a viability envelope and boundary/action conditions.

### C.26.3:End
