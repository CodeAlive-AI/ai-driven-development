## B.4.1 - Publish Candidate Routes for a Stabilized Cue (RoutedCueSet)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Candidate routes from an observed cue.

### B.4.1:1 - Problem frame
**Use this when.** A recipient needs a publication of possible continuations from a stabilized cue, or needs to receive a route choice with its grounds. Start with the action or question the cue bears on. An operator who only needs to choose a next action can use the reasoning in §4 and act within their authority. A promise to publish the recommendation also requires making it available as agreed.

The publication in `B.4.1` starts from a stabilized cue preserved in `PreArticulationCuePack` or an equivalent early form under `A.16`. Its grounds may suffice for action while the cause of the cue remains open. Keep an established anomaly, action claim or hypothesis under its own subject pattern.

### B.4.1:2 - Problem
A cue publication can lose its useful continuations when it is forced prematurely into a late form such as `AnomalyStatement`, `Characteristic`, or `ActionOption`. A route choice can also remain hidden in cue-pack prose, leaving the reader without its grounds or the subject pattern.

### B.4.1:3 - Forces
| Force | Tension |
|---|---|
| **Early capture vs endpoint discipline** | Preserve low-articulation cues without collapsing route discipline. |
| **Plural route set vs recorded selection** | Permit multiple candidate routes while requiring a selection record when selection occurs. |
| **Useful publication vs extra kinds** | Make routes inspectable without introducing a new publication kind for every case. |
| **Route content vs reader presentation** | Preserve the route-form requirements when selecting an MVPK face for the reader. |

### B.4.1:4 - Solution
Begin with the decision the recipient can make and the time they have to make it. What was actually noticed, about which part, use or occasion? What further result would let this recipient act or answer the question? Work backwards from that result to a possible next action, its actor and its entry conditions. A standing instruction or a reliable result already available may settle which action to take. If you have been asked to devise the continuations, make that choice from the work before consulting the route names in §4.2. Applying a supplied route exercises a different decision.

Choose how far to follow the cue. Hold the local observation fixed and vary its use elsewhere. Then hold an overall reading fixed and vary the affected parts or occasions. Which variation changes someone’s next decision or invalidates its grounds? Retain that distinction and the link to the recipient’s use. A common instruction applicable to all remaining cases can settle the action while their identities or causes remain open. Where the answer differs, look for a timely way to distinguish the cases, state the condition to the recipient, or identify what remains undecidable on the available evidence.

Some continuations are alternatives. Others supply different results the recipient needs together. In that case establish how those results could be combined, by whom and by when. A feasible choice for each person in isolation may depend on the same unavailable hour or on information they cannot share in time. If asked for one justified continuation, give it with its grounds. If asked to identify every admissible continuation, establish why the set covers them. The publication sequence for a stabilized cue is:

`Observe -> Notice -> Stabilize -> Route`

For the requested or needed route publication, use the `RoutedCueSet` form, normally downstream of `PreArticulationCuePack`. `RoutedCueSet` names the reusable publication rules defined below. The filled account states candidate routes and selection claims; C.2.1 governs its episteme identity. Its expression follows the route-form rules and, when selected, the presentation rules of an MVPK face under E.17.

The route publication should identify:

- the **originating cue pack**, if any, or the equivalent early form preserving the stabilized cue,
- the **candidate route set**,
- the **route decision state**,
- the **selected route**, if any,
- the **grounds for each live route**,
- any **conditions that would change the candidate set or its selection**,
- and any published **typed downstream publication**.

An existing publication can serve the receiving question when its content, form and availability meet the publication requirements. A reasoned choice by the authorized operator or body, a recommendation delivered to its intended recipient, a publication available to its recipients, and an intervention that actually took place each have their own grounds.

For specialization-sensitive routes, state the declared task family or utility target, any budget condition that qualifies the proposed continuation, any unresolved fact needed for its use or selection, and the downstream subject pattern with its entry conditions.

#### B.4.1:4.1 - `RoutedCueSet` shape
A conforming route account may include these fields:

- `sourceCuePackRef`
- `candidateRouteSet`
- `routeDecision?`
- `selectedRoute?`
- `routeRationale?`
- `routeSelectionStatus?`
- `multiRoutePolicy?`
- `publicationFaceRefs?`
- `articulationThresholdStatus?`
- `closureStatus?`
- `scope?`
- `GammaTime?`

`RoutedCueSet` is not the late endpoint. `articulationThresholdStatus` and `closureStatus` report guard state only; their governance remains with `C.2.4` and `C.2.5`, and route discrimination may cite `C.2.6` or `C.2.7` when source or use conditions or representation-factor differences affect the route choice.

`candidateRouteSet` is the core here. When reporting a selection, use `routeDecision`, `selectedRoute`, `routeRationale` and `routeSelectionStatus` to distinguish the decision, its status and what is known about its grounds. A record can identify a past choice while leaving the chooser's reasons unknown. They do **not** belong in `PreArticulationCuePack`.

The status reports which candidate routes remain live and any selection made; endpoint admission, publication availability, current use or retirement, and any authority relation remain separate claims under A.16 and their patterns.

Use `sourceCuePackRef` when the originating early form is a cue pack; otherwise identify the equivalent early form and the stabilized cue it preserves.

Use `publicationFaceRefs` when publication or review needs to identify the selected MVPK face forms. An expression of the route account or a later typed account follows its content form's rules and the presentation rules of any selected MVPK face. Selecting a face alone does not establish that the content rules are satisfied.

One `RoutedCueSet` can describe several candidate routes. A lineage fork requires distinct successor epistemes or project records under their identity and lineage rules. Use `C.2.1` for episteme identity; publication availability remains separate under `E.24.PUB`.

#### B.4.1:4.2 - Starter route family and conditional extension species
The candidate route set may contain, among others:

- starter routes:
  - `EvaluativeRoute`
  - `ActionInvitationRoute`
  - `ProblemAbductionRoute`
  - `MethodWorkRoute`
  - `RequirementCommitmentRoute`
- conditional extension routes for bounded specialization or corridor discovery:
  - `TaskFamilySpecializationRoute`
  - `AdaptationProbeRoute`
  - `NonHumanUtilityRoute`
  - `SubstrateDiversificationRoute`

##### B.4.1:4.2.1 - Specialization-sensitive extension route family
These four routes are not part of the starter core. Use them only when the cue carries explicit bounded-specialization pressure, corridor-entry pressure, or substrate-fit doubt that subject patterns must be able to recover by value.

Use `TaskFamilySpecializationRoute` when the cue points toward acquiring one narrower higher-fit specialist lane for one declared task family under budget, where that lane may later resolve into one specialist method, portfolio, or competence bundle.

Use `AdaptationProbeRoute` when the next question is whether threshold-reaching specialization is attainable under the current budget.

Use `NonHumanUtilityRoute` when the cue suggests a promising utility target outside the current human-default solution corridor but tied to one declared task family or utility target.

Use `SubstrateDiversificationRoute` when the cue raises a question about whether the current method substrate, or a broader or different one, can meet the declared task or utility target.

Contexts may refine the route family locally, but they shall keep the distinction between early route publication and endpoint governance.

#### B.4.1:4.3 - Projection discipline
Here `projection` names route-bounded partialization. For a downstream projection under this section, publish the result in a **typed publication form**. The expression may also follow an existing MVPK face’s presentation rules. A recipient may carry out a selected action directly when authorized and its conditions hold. The subject pattern governs the downstream claim.

A routed cue set may support these continuations:

- publish `U.AbductivePrompt` under `B.5.2.0`,
- apply `A.6.P`, `A.6.A`, or `C.16.Q` under its entry conditions and produce the sentence, record, or other result that the selected pattern calls for,
- or publish another explicitly typed upstream projection.

For a proposed downstream projection, if no applicable typed publication form can be identified, keep the content in `RoutedCueSet`; an MVPK face supplies no such form.

### B.4.1:5 - Archetypal Grounding
**Tell.** Route publication requires a stabilized cue and a stated candidate route set.

**Show (System).** An operator alarm may support routes toward intervention, rollback, or anomaly investigation.

**Show (Episteme).** An inquiry cue about a model-vs-observation discrepancy may route toward anomaly framing, opportunity framing, or probe design before a hypothesis exists.

### B.4.1:6 - Bias-Annotation
The pattern favors preserving low-articulation cues and exposing real alternatives. In a route publication, state the grounds for each live route and for any asserted selection. A single decisive ground can warrant the requested continuation across the whole relevant range.

### B.4.1:7 - Conformance Checklist
- `CC-B.4.1-1` Observe output **SHALL NOT** be forced into `AnomalyStatement` when articulation threshold is not met.
- `CC-B.4.1-2` A routed cue set **SHALL** name its `candidateRouteSet` and explain how the stated continuations serve the receiving question in the applicable conditions. Support any claim of completeness. One justified route may suffice for a request for one continuation.
- `CC-B.4.1-3` A published selection **SHALL** identify the selected route and whose decision it was. For a past selection, state the grounds for attributing it to that person or system. Report their rationale when the evidence establishes it, and identify any rationale still unknown. A recommendation supplied by the author gives the author’s grounds. When publication is part of the assignment, establish availability to its intended recipients.
- `CC-B.4.1-4` `publicationFaceRefs` **MAY** be named. The expression **SHALL** satisfy the route-form requirements as well as the presentation rules of any selected MVPK face.
- `CC-B.4.1-5` `RoutedCueSet` **SHALL NOT** be treated as establishing a late endpoint result.
- `CC-B.4.1-6` When a specialization-sensitive route is kept live, the route package **SHALL** name the declared task family or utility target, any budget condition that qualifies the proposed continuation, any unresolved fact needed for its use or selection, and the downstream subject pattern with its entry conditions.

### B.4.1:8 - Common Anti-Patterns and How to Avoid Them
- **Anomaly inflation.** Treat every early cue as an anomaly statement.
- **Cue-pack route smuggling.** Hide route decision or route rationale upstream in `PreArticulationCuePack`.
- **False single-route certainty.** Pretend one route is obvious when multiple candidate routes are live.
- **Projection capture.** Treat a typed downstream projection publication or its MVPK face as if it governed the endpoint family.

### B.4.1:9 - Consequences
Recipients can inspect candidate continuations, their grounds, and any selection before a downstream result is established. The cost is an additional route publication and its maintenance.

### B.4.1:10 - Rationale
Cue preservation and route choice answer different questions. A separate route publication makes the proposed continuations inspectable while retaining the cue pack as the account of the stabilized cue.

### B.4.1:11 - SoTA-Echoing
For the operator question in §13.1, the response-time clause and the latency rise support different possible continuations. Calling the alert an established duty would settle clause applicability without grounds; retaining only the cue would leave the proposed continuations implicit.

Adapting A.16's distinction between preservation and routing, §4 publishes those continuations and the grounds needed for any choice, while §13.1 retains intervention and inquiry alongside the duty question. This comparison supports that bounded gain at the cost of publishing and maintaining the route account.

Existing content can serve as that publication when it exposes the needed distinctions. Reconsider the route set when its grounds or the receiving question change.

### B.4.1:12 - Relations
- Builds on: `B.4`, `C.2.2a`, `A.16`, `A.16.1`, `C.2.LS`.
- Coordinates with: `A.16.0`, `C.2.4`, `C.2.5`, `C.2.6`, `C.2.7`, `B.5.2.0`, `B.5.2`, `A.6.P`, `A.6.A`, `C.16.Q`, `A.15`.
- Constrains: pre-abductive route publication.

### B.4.1:13 - Worked Route Sets

#### B.4.1:13.1 - Multi-route operator case
An operator is asked what a service-latency alert warrants. The note records a rise after a configuration change. The response-time clause may apply to a particular service and incident window. To compare possible continuations for the recipients, the operator may publish a route set containing:

- `ActionInvitationRoute`,
- `ProblemAbductionRoute`,
- and `RequirementCommitmentRoute`.

The investigator would need grounds for explaining the delay. The duty manager would need to know whether the clause applies and whether its trigger was reached within the window. An increase alone can occur entirely below a trigger. Use `A.2.8` for the resulting duty question. An authorized intervention can be appropriate before either the cause or the contractual duty is established.

Suppose the only question now is whom to notify. The record establishes that the trigger was reached at one of two service desks during the covered window, but leaves the desk unidentified. If the current rule sends alerts from both desks to the same manager, the operator can notify that manager now. If the rules require different recipients and restrict disclosure to the responsible one, the same record leaves the choice open until the desk can be identified or an authorized disposition valid in both cases is found. A commission to publish the continuations for later shifts still requires an available publication. Neither a route choice nor its publication establishes that the notification was sent.

#### B.4.1:13.2 - Inquiry case
A conceptual mismatch may route simultaneously toward:

- explanatory inquiry,
- probe design,
- and later lexical repair.

A published account that retains these routes explains what each could contribute and which question, if any, requires their results together.

#### B.4.1:13.3 - Invalid jump
It is invalid to treat a routed cue set as if it were a hypothesis, a gate, or a work plan. The route account records candidate continuations; the subject pattern governs the downstream result.

#### B.4.1:13.4 - Specialization-route and nonhuman-utility split
A routed cue set for a new task family may keep `ProblemAbductionRoute`, `TaskFamilySpecializationRoute`, and `NonHumanUtilityRoute` live together. The point is to preserve the declared task family, utility target, any qualifying budget conditions, any unresolved facts needed for use or selection, and any relevant corridor-entry conditions without presenting those candidates as a justified prompt, selector, or policy choice.

### B.4.1:14 - Keeping route plurality useful

State the grounds for the live route or routes, the selection status, and the basis for any current-use or retirement claim. Preserve the alternatives that still matter to the recipient.

#### B.4.1:14.1 - Minimal route package
Use the minimal route package in §4 (Solution).

#### B.4.1:14.2 - Selected route is not endpoint governance
When one route is selected, the routed cue set states the route choice. If the receiving work calls for a further claim or result, apply its subject pattern under that pattern's entry conditions. Publishing the routes and selection can be the sufficient result.

#### B.4.1:14.3 - Review prompt and threshold reminder
Review what the cue supports and the grounds for any recommendation or reported choice. Explain an exclusion when claiming that another route ceased to be suitable. Selecting a suitable route can leave other routes suitable. If the articulation threshold required for a proposed late prompt, requirement, or work claim is not met, keep the publication early.

#### B.4.1:14.4 - Deferred selection and route splitting
In a route publication, describe deferred selection through the live candidates, their grounds and any unresolved condition that matters to the recipient. Attribute an actual selection when one has been made.

One cue cluster may also split into several routed cue sets if different sub-cues support different destinations. Explain a split to later readers when their decision depends on how the sub-cues and destinations relate.

### B.4.1:15 - Migration and worked continuation boundaries

`B.4.1` governs route publication. Use the subject pattern under its entry conditions when the receiving work needs further abductive reasoning, lexical repair, a requirement or commitment claim, or work execution.

#### B.4.1:15.1 - Migration from anomaly-first prose
If a publication labels a cue as an anomaly before the anomaly's entry conditions hold, recover the stabilized cue. Publish its candidate routes when the receiving question needs them.

#### B.4.1:15.2 - Intervention vs inquiry split
An operator-facing disturbance may support both:

- an immediate intervention-oriented route,
- and a slower explanatory route.

A publication for both needs preserves the two continuations with their grounds and selection conditions. For an immediate response alone, act on the grounds for that response when authorized. The explanatory question can remain open.

#### B.4.1:15.3 - Requirement-route overreach
A route set that includes `RequirementCommitmentRoute` should not be read as if the requirement exists. The route is one admissible continuation; the requirement or commitment claim is decided under its subject pattern.

#### B.4.1:15.4 - Continue under the subject pattern
For a selected further question or task, continue under the subject pattern when its entry conditions are met. Typical questions and entry requirements are:

- relation-bearing wording whose relation, participants, direction, or required detail remain unresolved: `A.6.P`;
- evaluative wording whose sense, bearer, comparison, or consequence remains unclear: `C.16.Q`; use its ordinary repair sequence first, and meet C.16.Q:4.1's articulation and interpretation requirements when a transitional `qualityTermAscription(...)` is needed;
- affordance-like or action-first wording with enough context to compare its consequential meanings: `A.6.A`; recover the supported claim or question, or the fact that would distinguish the alternatives, then apply its subject rule;
- a declared prompt species, stable open question, scope, and provenance, with the articulation and closure conditions for rival answers to remain live: `B.5.2.0`;
- a stated requirement or commitment claim over its subject: its requirement-facing pattern; use `A.2.8` for a question about an individual duty;
- or an alignment question involving Method, WorkPlan, or Work: `A.15`; use `A.3.1`, `A.15.2`, or `A.15.1` when only the Method, WorkPlan, or dated Work is in question.

`ActionInvitationRoute` names the route to this wording-recovery use; it does not require an invitation occurrence. A.6.A can return an open question without settling its answer. If the selected next-use entry conditions cannot be established, keep that proposed use unresolved and retain the supported route account.

### B.4.1:20 - Route Evidence and Discrimination Package

#### B.4.1:20.1 - Evidence-per-route rule
Each live route in a routed cue set should cite the cue grounds that support it and any further grounds used to keep it live. Where those grounds are not published, complete the route account so readers can assess the support.

#### B.4.1:20.2 - Discriminator publication
When further information is needed to decide a route's use or selection, name the missing fact or condition and which question it would resolve. Several routes may remain live because they support different needed contributions.

#### B.4.1:20.3 - Multi-route state is not yet a lineage fork
One routed cue set may keep several candidate routes live without forking lineage. A fork claim requires distinct successor epistemes or project records and the lineage relation under their identity and lineage rules. State the preserved and lost content needed for that claim. Publication availability and any responsibility or authority handoff remain separate claims.

#### B.4.1:20.4 - Projection restraint
A typed downstream projection publication or prompt may be shown as one admissible continuation; the other live routes, their grounds and any unresolved conditions relevant to their use or selection shall remain readable.

#### B.4.1:20.5 - Review test for false single-route certainty
Consider the alternatives permitted by the original question. Would the same cue, in a different covered use, require a different recipient, continuation or reason? If so, preserve the distinction or state which needed fact is missing. If one ground establishes the requested continuation in all those cases, a single route suffices. For an account of an actual choice or publication, what establishes who chose or what was made available to whom?
### B.4.1:End
