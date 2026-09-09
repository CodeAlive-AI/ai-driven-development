## C.26.3 - Viability-Envelope Boundary Regulation

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.26.3:1 - Problem frame

Use this pattern when architecture work is maintaining, recovering, or changing viable operating ranges across boundaries. The working problem is not "optimize one metric"; it is "keep a bundle of characteristics inside a viable region while disturbances, probes, candidate interventions, boundary conditions, and operating regimes change."

**What goes wrong if missed.** The team treats one dashboard value, stability slogan, or local metric as viability, while another envelope variable, intervention cost, boundary condition, or failure mode is already breaking the protected promise or function.

**What this buys.** The viability claim becomes inspectable for an envelope-regulation decision: the exact object filling the local viability-bearer position and the pattern used to identify it, protected promise or function, variables, disturbances, sensors or probes, candidate interventions, boundary condition, adaptation cost, and failure mode are all named before acting.

Use C.26.3 for the general envelope-regulation claim when several characteristics must remain inside a viable region under a disturbance and a candidate intervention, boundary condition, adaptation cost, or failure mode matters. Continue to use the direct control, quality, SRE, causal, measurement, boundary, and work patterns for the exact objects and claims they define; using them does not make the envelope result leave C.26.3.

QL is an optional coordination branch. Use `C.26` and its QL vocabulary only when a probe, frame, export, coarsening, order, incompatible representation, or measurement-changing-state issue remains after the ordinary patterns have carried their part and leaves a specific contextual-model obstruction that changes what may be inferred or done. FEP, allostasis, and active inference remain source analogies rather than a second entry condition.

| Working card | Value |
| --- | --- |
| Primary reader | Architect, platform lead, reliability lead, product manager, or operations lead preserving viability under changing conditions. |
| Primary EntityOfConcern | The exact viability bearer: either one System with its A.1 identity, one A.22 `U.Structure` identified by its four discriminators, or another subject identified under its direct identity rule. The primary result is a `C.2.1` episteme about that bearer, not a plan or the writing card. |
| Admissible move | Point the local viability-bearer position to that exact object and record the pattern used to identify it; then name envelope variables, disturbance, sensors/probes, candidate interventions, boundary condition, adaptation cost, and failure mode. |
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

Start with this recognition note:

| Mini-entry | Question |
| --- | --- |
| Viability bearer | Is it one System with its A.1 identity, one A.22 `U.Structure` with exact constituents, selected obtaining relations, applied constraints, and a named selection-use frame, or a population/market slice with its own declared basis? A list of system-role kinds and assignment occurrences is not a bearer. |
| Protected promise / function | Which `U.PromiseContent`, stakeholder value, function, operating regime, commitment payload, or delivery promise is protected? |
| Envelope variables | Which two to five variables matter, rather than one comfort scalar? |
| Disturbance | What pushes the exact object in the local viability-bearer position outside the declared envelope? |
| Sensor / probe / candidate intervention | What reads the situation? What change is proposed, which exact object carries that proposal, and what actual Work, transformation, relation, or resulting state exists, if any? |
| Trade-off / failure | What gets worse, what cost is paid, and what failure would show the envelope move did not work? |

Use the fuller envelope-regulation record below when the viability reading will change a metric, candidate-intervention choice, boundary, staffing, routing, promise, or evidence decision.

Full envelope-regulation record:

| Field | Question |
| --- | --- |
| Viability bearer | Is it one System with its A.1 identity, one A.22 `U.Structure` with exact constituents, selected obtaining relations, applied constraints, and a named selection-use frame, or a population/market slice with its own declared basis? A list of system-role kinds and assignment occurrences is not a bearer. |
| Protected promise / function | Which `U.PromiseContent`, stakeholder value, function, operating regime, commitment payload, or delivery promise is protected? |
| Current service/access claims, if any | Which independently governed service/access claims are current, and what exact subjects, relations, and subject patterns do they name? |
| Envelope variables | Which characteristics or quality-bundle dimensions define viability? |
| Viable region / bounds | What counts as inside, near edge, degraded, or outside the envelope for this use? |
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

Do not say that all architecture is homeostasis. Say that some architecture decisions are viability-envelope decisions.

#### C.26.3:4.2 - Finish conditions

Finish with one of these results:

| Result | Meaning |
| --- | --- |
| Envelope-regulation claim | Write one `C.2.1` episteme whose EntityOfConcern is the exact viability bearer and whose ClaimGraph states the protected promise/function, envelope variables, viable region/bounds, disturbance, sensors/probes, candidate interventions, boundary condition, trade-off condition, adaptation cost, and failure mode. Its effective ReferenceScheme supplies the reading context. |
| Candidate-intervention recovery or redesign | Recover the direct object first. Revise only the current proposal—its Method or description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description—and identify any dated Work, actual change, obtaining relation occurrence, and resulting state separately. A fixed F.9 Bridge is not an intervention object: after an endpoint sense or profile changes, test another F.9 candidate and identify it only if the predicate obtains. |
| Measurement/probe redesign | Redesign a dashboard, alert, health check, readiness score, or review process because it distorts the envelope it reports. |
| Neighbor coordination without QL | Keep the C.26.3 envelope-regulation claim and use `C.25`, `C.16`, `A.6`, `A.15`, `U.Dynamics`, `C.18`, `C.19`, or `A.19` for the exact neighboring objects and claims. Omit `C.26` / QL when no contextual-model obstruction remains. |
| No envelope claim | Drop the viability-envelope wording when the exact object for the local viability-bearer position and the pattern used to identify it, protected promise/function, viable region/bounds, disturbance, candidate interventions, adaptation cost, and failure mode cannot be stated. |

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

The primary result is one `C.2.1` episteme. Its EntityOfConcern is the exact viability bearer, its effective ReferenceScheme fixes how references are read, and its ClaimGraph states the envelope-regulation claim. The writing card below is only a local shape for that ClaimGraph; it is not the episteme's subject and does not create another object.

Keep a `U.WorkPlan` and each other proposal under its direct kind. A setting proposal, policy proposal, Bridge description, or other proposal is a separate claim-bearing episteme unless its direct pattern identifies that object as another kind. Identify the episteme's EntityOfConcern under that pattern. A modal F.9 proposal concerns the admitted direct Bridge relation kind and designates its proposed endpoints and profile in the ClaimGraph. None of them becomes the envelope episteme merely by appearing in its ClaimGraph.

The first useful move is to replace a one-scalar stability story with an inspectable envelope-regulation claim for the decision.

Envelope-regulation sequence:

1. Point the local viability-bearer position to one exact object. For a System, cite its A.1 identity. For selected organization, cite one A.22 `U.Structure` through exact independently identified constituents, exact selected obtaining relation occurrences, exact constraints as applied, and one named selection-use frame; a role-kind/assignment list is insufficient. For a population or market slice, state its declared domain and effective reference scheme, membership or scope, and identity basis. Then name the separately defined promise or function being preserved. If no branch identifies the bearer, stop.
2. Name the envelope variables and the viable range or qualitative boundary for each.
3. Name the disturbance or regime change.
4. Name sensors/probes and say whether they only report, also frame, or also change behavior.
5. Name each candidate intervention and recover the exact object of the proposal: Method or description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description. Separately identify any dated Work, actual change, obtaining relation occurrence, or resulting state. Work may change an access, permission, assignment, local-sense claim, reference scheme, Bridge description, bounded-use claim, or other world-side object only as its direct pattern permits. If an F.9 endpoint or profile changes, test the resulting Bridge candidate anew; a fixed Bridge occurrence cannot be revised or ended by authority.
6. State the boundary condition being preserved or changed.
7. State the trade-off condition and adaptation cost.
8. State the failure mode and re-probe/destabilization condition.
9. Add dynamics detail only if rate, inertia, damping, latency, resistance, or acceleration changes the decision.

Ordinary output: produce a viability-envelope record with envelope variables and viable region, a disturbance/sensor/probe map, a candidate-intervention-to-direct-object recovery, and a trade-off, adaptation, and failure condition that tells the practitioner what changes in the work.

The output should give one direct next move: revise a MethodDescription or policy episteme; amend a WorkPlan; recover each actual performer's A.13 core and independently admit the Work under A.15.1; if that Work account must also identify the assignment under which it was performed, check the relation separately through F.6; change a setting through a separately grounded transformation; change an access or permission relation when its direct pattern permits; revise a local-sense claim, reference scheme, Bridge description, or bounded-use claim; test a new F.9 candidate after an endpoint/profile change; record the resulting state; or drop the envelope claim.

#### C.26.3:4.6 - Viability envelope record

A usable envelope record is a C.26.3-local normal form for the ClaimGraph content of one `C.2.1` episteme about the exact viability bearer. The enclosing episteme supplies the EntityOfConcern and effective ReferenceScheme. The card is not a constructor and is used only when envelope regulation is load-bearing.

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

The record is not a new U-kind or a universal architecture constructor. Changing its ClaimGraph content changes the claim and therefore identifies another episteme under `C.2.1`. A new layout, publication occurrence, form, or carrier can leave the episteme unchanged. New evidence can change the support for the claim without changing that claim; if the asserted ClaimGraph changes, the result is another episteme.

Well-formedness constraints:

- the local viability-bearer position points to one exact object and introduces no kind or relation: a System has its A.1 identity; an A.22 `U.Structure` has exact independently identified constituents, exact selected obtaining relation occurrences, exact constraints as applied, and one named selection-use frame; a population or market slice has its declared domain and effective reference scheme, membership or scope, and identity basis; a list of system-role kinds and assignments satisfies none of these branches;
- service or access wording names each current object and relation separately—the exact object in the local viability-bearer position, promise content, system, system-role assignment, commitment, Work occurrence, evidence, or another direct relation—through the pattern that defines that object or relation; the wording creates neither a root bearer nor a bundle;
- at least two envelope dimensions are visible when the claim says "viability" rather than one ordinary metric;
- at least one candidate intervention is named when the text proposes regulation rather than only diagnosis, and its proposal-side Method, description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description is recovered under the subject pattern; any dated Work, actual transformation, obtaining relation occurrence, or resulting state is identified separately;
- authority and latency are stated only for an object to which they apply; a description, Method, plan, setting label, Bridge description, or resulting state is not made an actor or Work by this card;
- the adaptation cost is named, because allostasis hides cost when phrased as "stability through change";
- the failure mode is named, because viability is otherwise indistinguishable from optimism.

#### C.26.3:4.7 - Sensor, probe, candidate-intervention, and metric split

Do not let one dashboard value stand for the whole envelope.

| Item | Viability-facing question |
| --- | --- |
| Envelope variable | Which quality, resource, promise, risk, or operating dimension is inside/outside viable range? |
| Sensor | Which metric, alert, trace, health check, survey, review, or observation reports part of the envelope? |
| Probe | Which measurement setup, dashboard, readiness check, review, experiment, or incident query may change behavior or expose hidden dimensions? |
| Candidate intervention | What change is proposed? Recover whether cache, throttle, routing, staffing, protocol, escalation, access, bridge, or context-split wording denotes a Method or description, setting proposal, plan, access or permission claim, or Bridge proposal or description. Separately identify any dated Work, actual transformation or other change, obtaining relation occurrence, or resulting state claimed to exist. |
| Boundary condition | Which access, ownership, context, interface, promise, environment, or information constraint shapes the envelope? |
| Adaptation cost | Which latency, risk, support load, or compliance exposure is incurred, and which effort, attention, energy, trust, or future flexibility is spent, reduced, or put at risk? |

A metric value or dashboard carrier is neither Work nor an actual change. Its use, publication, or a surrounding governance routine may participate in a separately grounded behavior-changing claim. When Work is asserted, recover each actual performer's A.13 core and independently admit the dated occurrence under A.15.1. If the claim must also identify the assignment under which the Work was performed, name that assignment and check the relation separately through F.6. Name any changed setting, actual transformation, access or permission relation, or boundary relation separately. Repairing one envelope variable may still damage another.

#### C.26.3:4.8 - Homeostasis, allostasis, and architecture work

Homeostatic wording is useful when the claim concerns keeping a variable or bundle inside a stable range. Allostatic wording is useful when preserving the named function requires one or more separately governed setting, boundary, environment, access, staffing, routing, protocol, cache-policy, or operating-regime changes. The wording does not decide whether each item is a Method, description, plan, Work, transformation, relation, or resulting state.

Use the minimal reading that carries the case:

| Reading | Use when | Practical output |
| --- | --- | --- |
| Scalar quality repair | One characteristic or Q-bundle dimension is enough. | Apply `C.25`, measurement patterns, or evidence patterns as appropriate. |
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

This translation keeps the pattern practical for architects. The reader should be able to move from a source line to one concrete action: change a metric or probe; recover the candidate proposal as its exact Method or description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description; separately identify any dated Work, actual transformation or other change, obtaining relation occurrence, or resulting state; where a direct relation pattern permits Work or a transformation to establish, change, or end its occurrence, state that occurrence under its predicate; for F.9, revise only the relevant claim, scheme, endpoint sense, profile, or description and test any new Bridge candidate independently; change a boundary condition; state a trade-off; or reroute.

### C.26.3:5 - Archetypal Grounding

Tell: A platform team tries to preserve checkout latency during a traffic spike. The first move is to increase cache aggressiveness. Latency improves, but support load rises because stale payment-failure status causes confused customer contacts.

Show, System side: take `CheckoutSystem-1` as a case premise: it has already been independently recognized under A.1 as the deployed `U.System` whose viability envelope the team regulates. If that recognition is unavailable, stop; *checkout*, *payment*, and *service* wording do not establish the bearer. Keep the protected promise separate: `CheckoutPromiseContent-1` is the `U.PromiseContent` stating the checkout outcome and reliability on which the customer may rely. For this envelope decision, latency and payment-correctness measurements support claims about selected behaviour and results of `CheckoutSystem-1`; support-load measurement concerns the team's dated support Work; operator-attention measurement concerns the people doing that Work; and customer-promise reliability is tested by a separate evaluation of whether `CheckoutPromiseContent-1` is fulfilled. The decision uses these claims as distinct constraints; it does not turn them into facets of one bearer. Candidate interventions are proposed cache-policy, retry-policy, or routing changes. If the team plans one as intended Work, place that intention in a `U.WorkPlan`; the proposal is not `U.Work`. Assert `U.Work` only after each actual performer's A.13 core is established and A.15.1 independently admits the dated occurrence from its history, enacted Method, temporal extent, and containing-System relation. If the case must also identify the assignment under which that Work was performed, check the relation separately through F.6. For the cache intervention, this case asserts only the observed cache-setting change, not a Work individual. A dashboard query remains a probe unless the case separately names a behaviour-changing occurrence. Changing escalation terms, a local-sense claim, a reference scheme, an F.9 endpoint/profile component, or a Bridge description keeps the resulting promise content, commitment, claim, description, and dated Work separate. After an endpoint/profile change, test the new F.9 candidate independently; do not say that Work revised the fixed Bridge occurrence. Here the observed cache-setting change improves latency while stale payment-failure status increases support load, so optimizing one declared dimension damages another.

Show, Episteme side: the supported claim is not "latency is the viability state." It is an envelope-regulation claim: the observed cache-setting change preserved latency while damaging another envelope dimension. The text records that actual change separately from the proposed cache-policy intervention. The repair is to state the trade-off, adaptation cost, applicable authority and latency, and failure mode.

### C.26.3:6 - Bias-Annotation

This pattern biases authors against scalar comfort. That bias prevents "green dashboard" from replacing viability.

It also biases authors toward actionable architecture work. The pattern asks which direct object a boundary, access, protocol, staffing, cache, throttle, bridge, or measurement proposal denotes and how quickly its separately governed effects can matter. For any precise Work claim, establish each actual performer's A.13 core and independently admit the dated occurrence under A.15.1. Add F.6 attribution only if the account must also identify the assignment under which that Work was performed. Any actual transformation is grounded separately.

Use `C.25` alone when one quality bundle or metric can be handled without envelope, disturbance, boundary condition, recovered candidate intervention, adaptation cost, or viability failure mode.

### C.26.3:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-C26.3.1 | The viability bearer is one exact System under A.1, one exact A.22 `U.Structure` under all four identity discriminators, or another exact subject under its direct identity rule; the local position introduces no kind, relation, or configuration object. |
| CC-C26.3.2 | The protected promise or function is named. |
| CC-C26.3.3 | Envelope variables or quality-bundle dimensions and the viable region / bounds are named. |
| CC-C26.3.4 | Disturbance class and scenario/window are named. |
| CC-C26.3.5 | Sensors/probes and their possible behavior-changing or dimension-hiding effects are named when measurement carries the envelope claim. |
| CC-C26.3.6 | Each candidate intervention is recovered as a proposal about an exact Method, description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description; dated Work, actual change, obtaining relation occurrence, and resulting state remain separate. A fixed F.9 Bridge is never the object revised or ended by Work; an endpoint/profile change opens a new candidate that must pass F.9 independently. |
| CC-C26.3.7 | Boundary condition, trade-off condition, and adaptation cost are stated. |
| CC-C26.3.8 | Failure mode and re-probe/destabilization condition are stated. |
| CC-C26.3.9 | Metrics or dashboards are not treated as the envelope itself. |
| CC-C26.3.10 | The QL cue / formal cue is named if QL wording is retained. |
| CC-C26.3.11 | QL wording appears only when probe, order, export, coarsening, or incompatible frame interaction remains load-bearing and satisfies C.26's contextual-model obstruction condition. |
| CC-C26.3.12 | Rate/inertia/damping/effort and second-order dynamics variables appear only when load-bearing. |
| CC-C26.3.13 | Homeostasis, allostasis, active inference, and Markov-boundary wording are restored into FPF subject patterns before they carry the claim; Markov-blanket wording does not by itself create boundary, interface, component, agency, or viability authority. |
| CC-C26.3.14 | The pattern adds no new control ontology. |

### C.26.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| One metric as viability | Availability, latency, or score stands for the whole envelope. | Add the exact object filling the local viability-bearer position and the pattern used to identify it, protected promise, other dimensions, and failure mode. |
| Fixed setpoint thinking | Stability means one variable must never move. | Ask whether allostasis preserves function by changing settings, environment, boundary, or regime. |
| Passive sensor assumption | A dashboard is treated as neutral even after it changes behavior. | Use `C.26.1` when the false passive reading changes the architecture decision; use evidence patterns for its support. |
| Candidate intervention without a recovered object, predicate, or applicable authority | The text recommends a change without recovering its proposal-side Method, description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description; fails to identify separately any dated Work, actual transformation, obtaining relation occurrence, or resulting state on which it relies; or claims Work no system can perform in time. | Recover the proposal-side object first; identify every actuality separately under its subject pattern; state authority and latency only for the applicable Work, change, or relation. |
| Biological proof jump | Homeostasis or FEP language is used as proof for software or organizations. | Treat it as modeling discipline and apply existing FPF patterns to claims. |
| Markov-blanket collapse | A statistical separation, physical interface, interface module, functional element, component, boundary description, and agency threshold are all called the Markov blanket. | Split the source phrase through `A.6.RSIR`: use `C.29` or `C.26` for lens use; use `A.1` plus the direct relation pattern for holon delimitation or boundary crossing; use `A.6.P`, `A.6.0`, and `A.6.5` for relation, signature, or slot claims; use `A.6.M` for module-interface claims; use `A.6.F` for functional claims; use `A.14`, `C.13`, or `B.3.5` for component claims; use `C.2.1` for description content, `C.30.AD` for architecture descriptions, and `E.17` for reader-facing publication of an accepted account; use `A.13` for agency criteria, `C.16` for measurement construction, and `A.19` for a `CharacteristicSpace` or reusable `CharacteristicSpacePredicate` over it. |

### C.26.3:9 - Consequences

This pattern helps architects see stability-through-change. It supports decisions about candidate interventions only after each throttling, staffing, routing, protocol, context-boundary, cache, measurement, or escalation proposal is recovered as its exact Method, description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description, while any dated Work, actual transformation or other change, obtaining relation occurrence, and resulting state remain separately grounded.

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
- translate source terms into selected structures, `ArchitectureOf@Context` relations, architecture descriptions, structural views, or named C.30 subcases;
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

