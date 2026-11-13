## B.4.1 - Publish Candidate Routes for a Stabilized Cue (RoutedCueSet)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Candidate routes from an observed cue.

### B.4.1:1 - Problem frame
**Use this when.** A stabilized cue has possible continuations that a recipient needs to compare, or a route choice needs to be published. State the candidate routes and any justified selection without presenting the cue as an established anomaly, action claim, or hypothesis.

Routing begins **after cue stabilization**, with `PreArticulationCuePack` or an equivalent early form under `A.16`. Cue preservation may exist before routing. `B.4.1` begins only when publishing the routes becomes worthwhile.

### B.4.1:2 - Problem
A cue publication can lose its useful continuations when it is forced prematurely into a late form such as `AnomalyStatement`, `Characteristic`, or `ActionOption`. A route choice can also remain hidden in cue-pack prose, leaving the reader without its grounds or the subject pattern.

### B.4.1:3 - Forces
| Force | Tension |
|---|---|
| **Early capture vs endpoint discipline** | Preserve low-articulation cues without collapsing route discipline. |
| **Plural route set vs recorded selection** | Permit multiple candidate routes while requiring a selection record when selection occurs. |
| **Useful publication vs extra kinds** | Make routes inspectable without introducing a new publication kind for every case. |
| **Form vs face precision** | Keep route-bearing publication form distinct from the MVPK face on which it is rendered. |

### B.4.1:4 - Solution
After cue stabilization, state the candidate continuations and any selected route. Keep downstream claims under their subject patterns. The optional route follows this sequence:

`Observe -> Notice -> Stabilize -> Route`

Publish the route package as a `RoutedCueSet`, normally downstream of `PreArticulationCuePack`.

The route publication should identify:

- the **originating cue pack**, if any, or the equivalent early form preserving the stabilized cue,
- the **candidate route set**,
- the **route decision state**,
- the **selected route**, if any,
- the **grounds for each live route**,
- any **conditions that would change the candidate set or its selection**,
- and any published **typed downstream publication**.

This keeps later handoff reviewable while leaving downstream claims and results under their subject patterns.

For specialization-sensitive routes, state the declared task family or utility target, any budget condition that qualifies the proposed continuation, any unresolved fact needed for its use or selection, and the downstream subject pattern with its entry conditions.

#### B.4.1:4.1 - `RoutedCueSet` shape
A conforming routed cue set may publish:

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

`candidateRouteSet` is the core here. `routeDecision`, `selectedRoute`, `routeRationale`, and `routeSelectionStatus` belong here when route selection is stated. They do **not** belong in `PreArticulationCuePack`.

The status reports which candidate routes remain live and any selection made; endpoint admission, publication availability, current use or retirement, and any authority relation remain separate claims under A.16 and their patterns.

Use `sourceCuePackRef` when the originating early form is a cue pack; otherwise identify the equivalent early form and the stabilized cue it preserves.

`publicationFaceRefs` names MVPK faces only when face typing matters for publication or review. Faces are renderings of the routed cue set or of later typed projection publications; they are not the route-bearing form.

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
Here `projection` names route-bounded partialization. The resulting content must be published in a **typed publication form**, rendered, when needed, on an existing MVPK face. The subject pattern governs the downstream claim.

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
The pattern favors preserving low-articulation cues and publishing route plurality. Routing must state why one route is live and why one route was selected if selection occurred.

### B.4.1:7 - Conformance Checklist
- `CC-B.4.1-1` Observe output **SHALL NOT** be forced into `AnomalyStatement` when articulation threshold is not met.
- `CC-B.4.1-2` A routed cue set **SHALL** name its `candidateRouteSet`.
- `CC-B.4.1-3` When route selection occurs, `routeDecision`, `selectedRoute`, and `routeRationale` **SHALL** be explicit.
- `CC-B.4.1-4` `publicationFaceRefs` **MAY** be named, but route-bearing form and publication face **SHALL NOT** be collapsed.
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
An operator alert note records a service-latency rise after a configuration change and a response-time clause whose applicability to this service is unresolved. The operator may publish a route set containing:

- `ActionInvitationRoute`,
- `ProblemAbductionRoute`,
- and `RequirementCommitmentRoute`.

Keep the live routes explicit and state any selection with its grounds. The missing discriminator for `RequirementCommitmentRoute` is whether the clause covers this service and incident window. If it does, use `A.2.8` for the question of a duty; the latency cue can support intervention and explanatory inquiry.

#### B.4.1:13.2 - Inquiry case
A conceptual mismatch may route simultaneously toward:

- explanatory inquiry,
- probe design,
- and later lexical repair.

This is admissible only if the route rationale states the plurality.

#### B.4.1:13.3 - Invalid jump
It is invalid to treat a routed cue set as if it were a hypothesis, a gate, or a work plan. The route-bearing publication form records candidate continuations; the subject pattern governs the downstream result.

#### B.4.1:13.4 - Specialization-route and nonhuman-utility split
A routed cue set for a new task family may keep `ProblemAbductionRoute`, `TaskFamilySpecializationRoute`, and `NonHumanUtilityRoute` live together. The point is to preserve the declared task family, utility target, any qualifying budget conditions, any unresolved facts needed for use or selection, and any relevant corridor-entry conditions without presenting those candidates as a justified prompt, selector, or policy choice.

### B.4.1:14 - Keeping route plurality useful

A routed cue set stays useful only when route plurality, route grounds, selection status, and any current-use or retirement claim remain explicit.

#### B.4.1:14.1 - Minimal route package
Use the minimal route package in §4 (Solution).

#### B.4.1:14.2 - Selected route is not endpoint governance
When one route is selected, the routed cue set states the route choice. If the receiving work calls for a further claim or result, apply its subject pattern under that pattern's entry conditions. Publishing the routes and selection can be the sufficient result.

#### B.4.1:14.3 - Review prompt and threshold reminder
Review the cue grounds and any further grounds used to justify the selection, including the reasons for excluding previously live alternatives. If the articulation threshold required for a proposed late prompt, requirement, or work claim is not met, keep the publication early.

#### B.4.1:14.4 - Deferred selection and route splitting
When selection is deferred, publish the live candidates, their grounds and any unresolved conditions. When a selection is made, state it.

One cue cluster may also split into several routed cue sets if different sub-cues support different destinations. The split should be published so that later readers do not assume that one route exhausted the original cue complex.

### B.4.1:15 - Migration and worked continuation boundaries

`B.4.1` governs route publication. Use the subject pattern under its entry conditions when the receiving work needs further abductive reasoning, lexical repair, a requirement or commitment claim, or work execution.

#### B.4.1:15.1 - Migration from anomaly-first prose
If a publication labels a cue as an anomaly before the anomaly's entry conditions hold, recover the stabilized cue. Publish its candidate routes when the receiving question needs them.

#### B.4.1:15.2 - Intervention vs inquiry split
An operator-facing disturbance may support both:

- an immediate intervention-oriented route,
- and a slower explanatory route.

`B.4.1` preserves both continuations with their grounds and selection conditions.

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
Ask: if a selected route were excluded, would the publication explain the other live routes and any unresolved conditions relevant to their use or selection? If that information is missing, restore it before relying on the route set.
### B.4.1:End
