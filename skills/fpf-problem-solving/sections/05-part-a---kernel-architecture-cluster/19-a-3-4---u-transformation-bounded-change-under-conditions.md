## A.3.4 - U.Transformation: Bounded Change Under Conditions

> **Type:** Definitional pattern
> **Status:** Stable
> **Normativity:** Normative except where a section is explicitly informative

### A.3.4:0 - Use This When

Use this pattern when a project needs to identify a bounded transformation itself: what governed object changes, from what condition to what condition or delta, under which boundary conditions, and which typed values must be considered around that transformation before a stronger claim is made.

Use it when the working question is:

- what is transformed;
- what relation, task, transition, operation family, or predicate states the change;
- what conditions make the transformation possible, admissible, planned, enacted, observed, modeled, claimed, or published;
- which temporal aspect matters: time window, duration, cadence, rhythm, synchronization, currentness, or ordering relation;
- which transformation-ontic slots are claim-relevant in this use: acting system and `TransformerRole` relation when actual work is claimed, method, method description, mechanism, work plan, work occurrence, transformation-flow structure, transformation-flow mathematical description or lens, dynamics episteme, temporal aspect, temporal-claim adequacy, evidence relation, result record, source relation, publication, gate, decision, assurance, or refresh or reopen claim.

**Primary EntityOfConcern.** The `EntityOfConcern` is `U.Transformation`: the durable ontic for bounded change under declared conditions over an entity, structure, state, characteristic, episteme, work product, architecture, formal object, or other governed object. Its type-level typed n-ary `SlotRelation` with `SlotSpec` signature states both the identity slots by which one transformation is recovered and the participation and check slots by which claims about acting side, method, work, mechanism, transformation-flow structure, mathematical description, evidence, publication, and other transformation-relevant values stay attached to the same ontic. The `transformationRelation` is one slot inside that typed relation, not the whole `U.Transformation`.

**First useful move.** Identify the `U.Transformation` value first by filling the identity slots: transformed object, bounded context, initial condition, post-state condition or delta, transformation relation, admissibility or boundary condition, and temporal or ordering reference when relevant. Then run the participation and check slot relation in `A.3.4:4.4`: for each slot, record a filled value, unknown or not recovered, not asserted, not current for this claim, or claim lowering or blocking when a stronger claim depends on the missing value. If a claim-bearing record is also needed, treat it as a `C.2.1` episteme whose claim graph may make claims about the transformation, one of its slots, a slot filler, or relations among those values. Do not treat the episteme as the transformation itself.

**Open-world guard.** An unfilled method, work, description, evidence, result, gate, or publication slot does not mean that no such value exists in the world. It means only that this use has not recovered or asserted that value, or that the value is not current for the claim being made. Do not infer a methodless transformation merely because no `U.Method` has been described yet.

**What goes wrong if missed.** Method names become change proof, work traces become laws, process diagrams become execution, dynamics models become permission, temporal trends become intervention claims, mathematical constructions become project-world work, and publications about a change are treated as the change itself.

**What this buys.** A practitioner can keep the transformation under concern distinct from, but slot-connected to, the system bearing TransformerRole and dated work when actual project-world change is claimed, the method that can specify it, the mechanism that can law-govern it, the transformation-flow structure that can compose or locate it, the mathematical description or lens that can express selected structure, the dynamics episteme that can model it, the temporal aspect that can time it, the temporal-claim adequacy pattern that can judge a temporal claim, and the evidence or result relation that can justify a use.

**Not this pattern when.**

- If the issue is only a semantic way of doing, use `A.3.1`.
- If the issue is a description of that way, use `A.3.2`.
- If the issue is a state-space and transition-law episteme, use `A.3.3`.
- If the issue is a law-governed operation algebra with admissibility predicates, use `A.6.1` and `E.20`.
- If the issue is planned or dated work, use `A.15.2` or `A.15.1`.
- If the issue is the selected compound transformation-flow structure, its locus, path, path slice, crossing, or flow valuation, use `E.18`.
- If the issue is a graph, algebra, category, tuple, morphism, quotient, fold, refinement, factorization, or wiring expression used to describe that structure mathematically, use `E.18.2` and `C.29`.
- If the issue is a positive temporal aspect of an object or claim, use `C.27.TA`.
- If the issue is adequacy or admissible use of a temporal claim, use `C.27`.

### A.3.4:1 - Problem Frame

FPF often needs to talk about change in physical systems, engineered artifacts, organizations, epistemes, documents, architectures, programs, regulatory situations, and research objects. The same source phrase may say "algorithm", "process", "workflow", "procedure", "mechanism", "run", "trajectory", "transition", "stabilization", "editing", "migration", "optimization", "morphism", "construction", or another field-specific name for a change, transformer, or change structure.

Those phrases are not enough to recover the object under concern. A CRISPR editing protocol, a nuclear-plant operating change, a platform refactoring, a model update, a document repair, an architecture move, a proof construction, and a method-result carry-through can all involve transformation, but the FPF values under use differ.

FPF already has strong neighboring patterns:

- `A.3` for transformer constitution: acting system bearing `TransformerRole`, method description, method, and actual work;
- `A.3.1` for `U.Method`;

- `A.3.2` for `U.MethodDescription`;
- `A.3.3` for `U.Dynamics`;
- `A.6.0` and `A.6.5` for signatures and slot discipline;
- `A.6.1` and `E.20` for mechanisms;
- `A.15.2` and `A.15.1` for work plans and dated work;
- `E.18` for transformation-flow structures;
- `E.18.2` for mathematical descriptions of transformation-flow structures;
- `E.18.1` for problem-to-principle-to-work carry-through;
- `C.27.TA` for positive temporal aspects;
- `C.27` for temporal-claim adequacy;
- `C.29` for mathematical-lens use;
- evidence, gate, assurance, source, result, decision, and publication patterns for their own claims.

What is missing is the compact ontic that says how these values fit around one bounded transformation without turning any one of them into the whole change.

### A.3.4:2 - Problem

Without `U.Transformation`, projects repeatedly make category errors:

1. **Method as transformation.** A way of doing is treated as if the change already happened or must happen.
2. **Mechanism as transformation.** A law-governed operation algebra is treated as the actual or intended change, rather than as one governing value for a transformation.
3. **Work as transformation law.** A dated work occurrence or trace is treated as if it defined the reusable transformation.
4. **Dynamics as permission.** A state-space or transition-law episteme is used as if it authorized action, gate passage, or result acceptance.
5. **Temporal claim as transformation.** A claim about rate, rhythm, recovery, delay, effort, inertia, freshness, or validity window is used as if it specified the whole change and its conditions.
6. **Formal construction as project-world work.** A morphism, proof construction, or formal transformation inside a mathematical substrate is treated as a physical or organizational change without a realization or work relation.
7. **Publication as transformation.** A report, dashboard, diagram, source span, or published specification is treated as if it were the changed object or the change event.

These errors are expensive because the wrong neighboring pattern then receives the claim. The project may seek evidence for a method when it needs a work trace, compare dynamics models when it needs a transformation boundary, or invoke temporal-claim adequacy when the real problem is the missing transformation relation.

### A.3.4:3 - Forces

| Force | Tension |
| --- | --- |
| Generality and specificity | The pattern must cover physical, biological, software, organizational, documentary, architectural, formal, and epistemic changes without reducing them to software algorithms. |
| Possible, planned, actual, modeled, and claimed transformation | A transformation may be physically possible, planned, enacted, observed, modeled, claimed, or published. Those use relations must stay distinct. |
| Neighboring value competition | Methods, mechanisms, dynamics, work, temporal aspects, evidence, and results all look like "the thing that changes things". Each must keep its own kind. |
| Time and order | Many transformations need a time window, cadence, duration, ordering relation, or refresh condition, but time wording alone does not define the transformation. |
| Mathematical strength and practical use | Formal task, morphism, state-space, constructor-theory, or dynamics language can make transformations precise, while practical permission, evidence, work, and responsibility stay with their governing patterns. |

### A.3.4:4 - Solution

#### A.3.4:4.1 - Definition

`U.Transformation` is a durable FPF ontic for bounded change under conditions.

A `U.Transformation` is identified by:

- the transformed entity, structure, state, characteristic, episteme, work product, architecture, formal object, or other governed object;
- the bounded context;
- an initial condition and post-state condition, final condition, or delta predicate;
- a transformation relation, task, transition, operation family, morphism, construction, or declared transformation predicate;
- admissibility or boundary conditions;
- a temporal or ordering reference when timing or ordering matters for the claim.

The transformation may be possible, planned, enacted, observed, modeled, described, evidenced, or published. Those are linked-use relations around the transformation. They do not change the basic kind.

#### A.3.4:4.2 - Transformation Core

Use this compact filled core before examples or neighboring-pattern references. It identifies one `U.Transformation` value under concern by filling the core slots from the type-level schema in `A.3.4:4.4`. It is not a second ontology, not an episteme slot relation, not a record kind, and not a substitute for neighboring patterns.

```text
TransformationCore:
  transformedEntityOrStructure: governed object or structure whose change is under concern; type it through A.3.4:4.3.
  boundedContext: bounded context-of-meaning where the transformation has meaning; type it as `U.BoundedContext` or through the direct context-governing pattern when current.
  initialCondition: starting state, structure, characteristic value, formal object, or condition set.
  postStateConditionOrDelta: intended, observed, possible, modeled, or claimed post-state, result condition, or delta predicate.
  transformationRelation: the relation, task, transition, operation family, morphism, construction, or predicate that makes the change one transformation rather than an unrelated before-and-after pair.
  admissibilityOrBoundaryCondition: condition that makes the transformation possible, admissible, meaningful, blocked, or lowered.
  temporalOrOrderingReference?: time window, duration, cadence, ordering relation, or C.27.TA temporal aspect when timing or order changes the transformation claim.
```

Filled first-use slice:

```text
TransformationCore:
  transformedEntityOrStructure: reactor cooling loop operating state, governed as a plant subsystem state.
  boundedContext: emergency thermal-power-change operating review.
  initialCondition: temperature profile oscillates after a thermal-power step.
  postStateConditionOrDelta: oscillation is damped within the declared safety window.
  transformationRelation: operating-state stabilization relation under the revised control setting.
  admissibilityOrBoundaryCondition: safety-case review and measurement evidence must hold before the setting is used.
  temporalOrOrderingReference: settling-time window and observation cadence governed through C.27.TA.

Immediate linked values:
  MethodRef?: revised operating method, governed by A.3.1.
  DynamicsEpistemeRef?: state-space and transition-law model, governed by A.3.3.
  WorkOccurrenceRef?: not asserted until dated plant work is recorded through A.15.1.
  EvidenceOrSourceRef?: temperature measurement evidence, not permission by itself.
```

`TransformationCore` is the ordinary filled-core instruction for one concrete use. It does not add `U.TransformationKind`, `U.TransformationTuple`, or `U.TransformationCard`. Use those names only after a separate E.24 decision shows that dependent patterns need those levels.

After the core is identified, run the participation and check slot signature in `A.3.4:4.4`. Method, method description, mechanism, work plan, work occurrence, acting system and `TransformerRole` chain when actual work is claimed, transformation-flow structure, transformation-flow mathematical description, dynamics episteme, temporal aspect, temporal-claim adequacy, mathematical lens, evidence, source, gate, decision, assurance, result, publication, and refresh or reopen slots are not all identity slots, but they are not arbitrary neighbors either. They belong to the `U.Transformation` ontic because claims about a transformation change admissible use, evidence relation, responsibility, repeatability, enactment, observation, modeling, permission, or refresh when those slot fillers change.

The modularity rule is: the slot belongs to the transformation ontic, while the filler keeps its governing kind and pattern. A `MethodRef?` slot may be filled by `U.Method` under `A.3.1`; a `WorkOccurrenceRef?` slot may be filled by `U.Work` under `A.15.1`; a `MechanismRef?` slot may be filled by `U.Mechanism` under `A.6.1` and `E.20`. This prevents two bad moves at once: it does not collapse method, mechanism, and work into transformation identity, and it also does not pretend that a transformation claim can ignore the way, enactment, evidence, or description that the claim relies on.

When an authored text, dashboard, proof, publication, model, or project record makes claims about the transformation, model that claim-bearing value through `C.2.1` rather than duplicating the episteme ontic here:

```text
TransformationDescriptionEpisteme (C.2.1 shorthand, only when a claim-bearing value is current):
  EntityOfConcernSlot: the U.Transformation, one transformation slot, one slot filler, or a relation among those values, as selected by the current claim.
  ClaimGraphSlot: claims about possibility, planning, enactment, observation, modeling, evidence, publication, acceptance, or admissible use.
  ReferenceSchemeSlot: how the claim graph is read or tested as claims about the selected transformation value or slot relation while preserving the enclosing U.Transformation context.
```

This shorthand is only a C.2.1 application. It does not add a second slot relation to `A.3.4`, and it must not make the description, publication, proof, dashboard, source span, or record into the transformation itself.

#### A.3.4:4.3 - Transformed Object Discipline

Do not identify transformations over untyped "things". The transformed-object slot is one slot inside the `U.Transformation` ontic. Its filler is an `EntityOfConcern` value under its governing pattern, not a string, record, dashboard, workflow label, or publication title.

Minimum transformed-object record:

```text
transformedEntityOrStructure:
  value: the named object, structure, state, characteristic, episteme, work product, formal object, or architecture-selected structure under concern.
  governingPattern: the FPF pattern that governs that object kind or relation.
  objectKind: Entity | Holon | System | Episteme | ArchitectureSelectedStructure | WorkProduct | FormalOrIdealObject | OtherGovernedObject
  boundaryOrReferenceScheme: boundary, reference scheme, identity condition, or formal substrate that keeps this object recoverable.
  levelOrScopeWhenRelevant: holon level, system scope, architecture level, formal level, publication scope, or local context when it changes the claim.
  descriptionOrPublicationWhenRelevant: description, diagram, report, dashboard, source span, or publication only when it is being used as a description or publication of the transformed object.
  notSelfEvidencingSource: source, publication, dashboard, or card that must not be treated as evidence merely because it names the object.
```

Use current `A.1` for the holon, entity, or system source line and the governing subject pattern for the filled object. A `U.System`, `U.Episteme`, architecture-selected structure, work product, organization, physical object, document or specification episteme, formal object, or project-world object can fill the slot. The slot does not make the filler a new kind, and the filler does not become `U.Transformation` merely by occupying the slot.

#### A.3.4:4.4 - Ontic Slot Relation, Identity Slots, and Participation Checklist

`U.Transformation` uses `A.6.0` and `A.6.5` slot discipline. This section is the type-level `onticSlotRelation` schema expressed through `SlotSpec` rows for `U.Transformation`. It has two slot statuses:

- **identity slots** that make one bounded transformation recoverable;
- **participation and check slots** that must be considered when claims about the transformation use method, mechanism, work, dynamics, temporal, graph, formal, evidence, result, source, publication, gate, decision, assurance, or refresh material.

This is not an editor's distinction between "important" and "optional" prose. It is the ontological modularity decision for `U.Transformation`. A participation and check slot is included in this ontic when all five conditions hold:

1. Claims about the transformation regularly change their admissible use, evidence relation, repeatability, responsibility, enactment, observation, modeling, permission, acceptance, or refresh when this slot's filler changes.
2. The filler has a stable relation to the transformation: it specifies, constrains, enables, enacts, observes, models, times, evidences, publishes, authorizes, accepts, refreshes, or otherwise participates in the ontic through a stable relation.
3. Omitting the slot would force dependent patterns to copy local negative catalogues or grow a shadow ontology around "process", "algorithm", "workflow", "mechanism", "evidence", "record", or similar source labels.
4. Including the slot does not fuse kinds: the slot belongs to `U.Transformation`, while the filler remains governed by its own pattern.
5. The first-use burden stays bounded: a user records a disposition for the slot, not a full neighboring pattern unless the current claim depends on that value.

The `?` marker on a slot means optional in a filled use, not optional in the type-level checklist. Each use considers the slot and records one disposition: filled, unknown or not recovered, not asserted, not current for this claim, or claim lowering or blocking when a stronger claim depends on the missing value. Under open-world discipline, an unfilled slot does not assert that the value does not exist.

Claims may be made about any part of this ontic: the whole transformation, an identity slot, a participation and check slot, a slot filler, or a relation among fillers. A `C.2.1` episteme carries those claims; A.3.4 supplies the transformation ontology that keeps the claims from drifting into separate ontologies.

The broad recognition area is change under concern. FPF does not add a separate `U.Change` head here. `U.Transformation` is the durable ontic for an atomic bounded change under conditions; `change` remains the plain recognition gloss. `E.18` supplies `TransformationFlowStructure`: selected compound structure over transformations and adjacent governed loci. Source phrases do not create a second ontology competing with `U.Transformation`: recover bounded transformation, selected transformation-flow structure, or mathematical-description slot by the current EntityOfConcern and claim. When a transformation-flow locus, path, path slice, substructure, crossing, or flow valuation composes, decomposes, constrains, or locates the bounded change, it fills the structural slot. When a graph, algebra, category, tuple, morphism, quotient, fold, refinement, factorization, or wiring expression is used to express that selected structure, it fills the mathematical-description slot instead.

The A.3 transformer line is the actual-work docking for this ontic. A.3 already governs the acting side: a `U.System` bearing `TransformerRole`, a `U.MethodDescription`, a `U.Method`, and a dated `U.Work` occurrence. A.3.4 supplies the missing filled change-under-concern core and surrounding participation slots that those values can participate in. When a transformation is claimed as actual project-world change, recover the `A.3` and `A.15` chain through `WorkOccurrenceRef?`: `performedBy -> U.RoleAssignment(holder: U.System, role: TransformerRole, context, window)` and `enactsMethod -> U.Method`, with the method-description source when current. Do not introduce a separate transformer and transformation ontology for the acting side, and do not treat actual work as the whole transformation when the changed object, delta, boundary condition, or graph expression is also claim-relevant.

`A.3.4` therefore needs two different linked slots, not one vague graph reference. `TransformationFlowStructureRef?` is current when an `E.18` selected compound structure, transformation locus, selected path, path slice, substructure, crossing, or flow valuation composes, decomposes, constrains, or locates the atomic bounded change. `TransformationFlowMathematicalDescriptionRef?` is current when a graph, algebra, category, tuple, morphism, quotient, fold, refinement, factorization, or wiring expression is used as a mathematical description or lens for that selected structure. The first keeps the transformation in-life or in-subject structure under concern; the second keeps the mathematical description from becoming the transformation, method, mechanism, work occurrence, publication, or evidence relation.

`TransformationCore` in `A.3.4:4.2` is one filled use of the identity slots, not a second ontology. The participation and check slots are fixed typed positions around the transformation, not extra identity conditions and not fused neighboring kinds.

Identity slots:

| Identity slot | Value kind or governing pattern | Meaning |
| --- | --- | --- |
| `transformedEntityOrStructure` | `EntityOfConcern` value under its governing pattern | What changes or is to be changed. |
| `boundedContext` | `U.BoundedContext` or direct context-governing pattern when current | The context-of-meaning in which this is one transformation; if the context name becomes durable, public, Core-facing, or cross-context, use `F.18` and `F.17 UTS`. |
| `initialCondition` | state, characteristic value, structure, formal object, or condition set | The condition before the transformation or the lower boundary of the claim. |
| `postStateConditionOrDelta` | state, characteristic value, structure, result condition, or delta predicate | The intended, observed, possible, or claimed post-state or delta. |
| `transformationRelation` | relation, task, transition, operation family, morphism, construction, transformation-flow structural relation via E.18 when current, or declared transformation predicate | What makes this one bounded change a transformation rather than an unrelated before-and-after pair. |
| `admissibilityOrBoundaryCondition` | condition set or governing-pattern boundary | What makes the transformation possible, admissible, meaningful, blocked, or lowered. |
| `temporalOrOrderingReference?` | `C.27.TA` temporal aspect, time window, order relation, cadence, duration, or not-triggered | The timing or ordering reference when it changes the transformation claim. |

Participation and check slots:

| Participation and check slot | Filler kind or governing pattern | Consideration rule |
| --- | --- | --- |
| `TransformerRef?` | `U.System`, candidate system, or system-in-role locus bearing `TransformerRole@Context`; use A.7 and the role/work family when role assignment, responsibility, capability, work, or enactment is current | Consider who or what produces, enacts, carries, realizes, or sustains the transformation. A `FunctionalElement@Context` may recover this transformer locus in a functional structure view, but reactors, enzymes, control systems, service organizations, scripts, instruments, manufacturing cells, and document-editing systems can also fill it. If a source cue names the device or system side that performs input-output conversion, map it here plus any current signature, mechanism, capability, method, work, port, interface, or module-allocation claim; do not mint a second transformer kind from the source cue. |
| `InputConditionOrPortRefs?` | input state, material, energy, signal, information, work product, formal object, condition, or functional-port signature; use `A.6.0`, `A.6.5`, `A.6.F`, `A.6.M`, `E.18`, `C.30.ASV`, and the domain pattern when current | Consider inputs when boundary, transfer, conservation, loss, acceptance, port, or functioning claims depend on what enters or is accepted by the transformation. Inputs may constrain identity only when the input boundary distinguishes this transformation; otherwise they are participation/check slots. |
| `OutputConditionOrPortRefs?` | output state, produced flow, result condition, work product, formal object, or functional-port signature; use `A.6.0`, `A.6.5`, `A.6.F`, `A.6.M`, `E.18`, `C.30.ASV`, and result/evidence patterns when current | Consider outputs when the claim depends on produced state, flow, work product, condition, port, transfer, conservation, loss, acceptance, or flow boundary. Keep output distinct from result evidence and publication: an output may identify or constrain the transformation, while evidence/result patterns govern proof, observation, or acceptance claims. |
| `FunctioningRef?` | governed relation/use value linking `FunctionalElement@Context` to `U.Transformation` or `TransformationFlowStructure`; use `A.6.F`, `C.30.ASV`, `E.17.2`, and `A.6.M` for the functional-view, viewpoint, and allocation sides | Consider when this transformation is functioning of a functional element: the bearer-system's functional behavior in a bounded functional structure view, often located inside a transformation-flow structure. The slot may name functional element, bearer, `TransformerRole`, capability, functional port signatures, flow location, module allocation, and status such as required, possible, intended, observed, degraded, or blocked when those claims are current. It is not a new `U.Functioning` root. |
| `MethodRef?` | `U.Method` via `A.3.1` | Consider the way by which the transformation is specified, selected, guided, repeated, or compared. An algorithm may fill this slot only when the current claim is the semantic way of doing under conditions; otherwise recover method description, formal substrate, mechanism, work, or evidence through its governing slot. If no method is recovered, do not infer method absence; mark unknown or not recovered, or lower a method-dependent claim. |
| `MethodDescriptionRef?` | `U.MethodDescription` via `A.3.2`; `C.2.1` when the description is claim-bearing | Consider an authored procedure, protocol, solver formulation, proof script, algorithm text, or other description when it is used around the transformation. This is a description episteme or source value, not the transformation and not necessarily the method itself. |
| `MechanismRef?` | `U.Mechanism` via `A.6.1` and `E.20` | Consider a law-governed operation algebra, realization structure, admissibility predicate, or mechanism-method stabilization claim when it governs how the transformation can occur. |
| `WorkPlanRef?` | `U.WorkPlan` via `A.15.2` | Consider planned dated work when the transformation is planned, proposed, coordinated, or carries a planned-responsibility claim. Recover role requirements or proposed `U.RoleAssignment`s when planning responsibility, performer eligibility, or cross-role coordination is current. |
| `WorkOccurrenceRef?` | `U.Work` via `A.15.1` | Consider performed dated work when the transformation is claimed as enacted, observed through work, traced, result-producing, or responsibility-bearing. Recover `performedBy -> U.RoleAssignment`, `enactsMethod -> U.Method`, method-description source when current, affected referent, result, and evidence relation when current. |
| `TransformationFlowStructureRef?` | `E.18` selected compound transformation-flow structure, transformation locus, path, path slice, substructure, crossing, or flow valuation | Consider when an E.18 structure composes, decomposes, constrains, orders, couples, or locates the atomic bounded change itself. Use it to fill or constrain `transformationRelation` or structural context; do not infer method, mechanism, work, publication, gate, or evidence from structural position unless the corresponding slot filler is recovered through its governing pattern. |
| `TransformationFlowMathematicalDescriptionRef?` | `E.18.2` graph, algebra, category, tuple, morphism, path, slice, quotient, fold, refinement, factorization, or wiring expression, coordinated with `C.29` when lens choice matters | Consider when a mathematical description or lens expresses, compares, folds, decomposes, or computes over the selected transformation-flow structure. This slot is about the description/lens; it does not by itself define the in-life transformation relation or enactment. |
| `DynamicsEpistemeRef?` | `U.Dynamics` via `A.3.3` | Consider state-space, transition-law, or control-model claims when they model, predict, or bound the transformation. |
| `TemporalAspectRef?` | `C.27.TA` | Consider time window, rhythm, cadence, duration, synchronization, currentness, recovery, stabilization, effort, inertia, or validity window when it matters to the transformation claim. |
| `TemporalClaimAdequacyRef?` | `C.27` | Consider temporal-claim adequacy when an authored temporal claim about the transformation is being used for action, comparison, promise, assurance, or source-currentness. |
| `FormalOrMathLensRef?` | `A.6.0`, `C.29`, or direct formal or mathematical pattern | Consider formal substrate, invariant, morphism, construction, state-space, task, or mathematical lens when it states, constrains, or compares the transformation relation. |
| `EvidenceOrSourceRef?` | `A.10`, `G.6`, `B.3`, `C.16`, source/currentness patterns, or the direct domain evidence pattern when current | Consider evidence, source use, provenance, measurement, model assumption, or source-currentness. Recover the exact typed value under the governing evidence, source, measurement, provenance, or currentness pattern; these are not one kind. |
| `ResultRef?` | direct result, acceptance, or result-publication pattern when current | Consider produced result, accepted result, stop condition, lowered result, or reopened result when the claim depends on result status. |
| `GateDecisionAssuranceRef?` | `A.20`, `A.21`, `B.3`, `G.6`, `C.11`, or the direct gate, decision, assurance, permission, or release-authority pattern when current | Consider permission, release, gate passage, assurance, responsibility, or decision. Recover the exact gate, decision, assurance, permission, responsibility, or release-authority value under its governing pattern; these are not one kind. |
| `PublicationOrDescriptionRef?` | `C.2.1`, `E.17`, `E.17.0`, `E.17.1`, `E.17.2`, or the direct publication, view, carrier, source, or specification-use pattern when current | Consider description, dashboard, diagram, source span, proof, publication, or view when it is used around the transformation. Use `C.2.1` for a claim-bearing transformation description episteme and `E.17` family or the direct publication/source/specification-use pattern for publication, view, source-use, or publication-use claims. |
| `RefreshOrReopenRef?` | direct refresh, currentness, or reopen pattern | Consider source refresh, validity-window change, new evidence, changed result, or reopening condition when it changes use of the transformation claim. |

The functional-transformation slots form one reciprocal group, not five loose fields. `TransformerRef?`, `InputConditionOrPortRefs?`, `OutputConditionOrPortRefs?`, `FunctioningRef?`, and `TransformationFlowStructureRef?` are active when the transformation is a functional behavior, is located in a flow, crosses a port or boundary, or depends on a bearer/capability/allocation claim. They are not identity slots by default; they become identity-making only when the current transformation claim explicitly distinguishes this transformation by the bearer, input/output boundary, functioning relation, or flow position.

A.3.4 does not duplicate A.15 role slots and does not add `RoleAssignmentRef?` as an identity slot. If a transformation claim depends on planned or performed work, recover the role-method-work chain through `A.15`, `A.15.1`, and `A.15.2`. If the required `U.RoleAssignment`, holder, role, context, method, work plan, or work occurrence cannot be recovered, lower or block the work-dependent transformation claim.

E.18 locus labels do not automatically fill A.3.4 slots. A transformation-flow locus labelled as mechanism points to mechanism-governing content under `A.6.1` and `E.20`; it fills `MechanismRef?` only when that mechanism value is recovered. A locus labelled as work or work enactment fills `WorkOccurrenceRef?` only when a dated performed-work occurrence is current under `A.15.1`. A signature locus points to `A.6.0`; a check locus points to gate or constraint-validity claims under `A.20` or `A.21`. Method and method-description slots still use `A.3.1` and `A.3.2`; a readable structure order does not create a method.

This is a weak dependency on `E.18`, not an identity dependency. Every `U.Transformation` may receive a one-locus, path-slice, substructure, or containing-flow-structure expression, but A.3.4 does not require such a structure to identify the transformation. When the structure is current, it helps recover method, work, mechanism, publication, evidence, gate, result, or refresh slots by pointing to structure-local loci; the filled values still remain governed by their own patterns.

Kinds do not collapse when associated with a transformation. `U.Method`, `U.Mechanism`, `U.WorkPlan`, and `U.Work` are not descriptions merely because they are named here. `U.MethodDescription`, `U.Dynamics`, and a transformation-description value are epistemes under their own governing patterns. Evidence, source, gate, decision, assurance, result, and publication values may bear on or govern claims about the transformation; they do not become identity slots unless a governing pattern explicitly makes them identity conditions.

When the current object is a claim-bearing description of the transformation, use `C.2.1` explicitly:

```text
TransformationDescriptionEpisteme:
  EntityOfConcernSlot: the U.Transformation, one transformation slot, one slot filler, or a relation among those values
  ClaimGraphSlot: claims about possibility, planning, enactment, observation, modeling, evidence, publication, acceptance, or admissible use
  ReferenceSchemeSlot: how those claims are read or tested as claims about the selected value or slot relation while preserving the enclosing U.Transformation context
```

A dependent pattern may cite `U.Transformation`, a filled `TransformationCore`, or a specific participation and check slot without copying this slot relation.

#### A.3.4:4.5 - Neighboring Distinction Table

| Current claim | Governing pattern |
| --- | --- |
| bounded transformation under conditions | `A.3.4 U.Transformation` |
| transformation-flow structure, path, path slice, substructure, crossing, or flow valuation as compound structure, locus, or context | `E.18`; `A.3.4` only for the atomic bounded transformation claim |
| graph, algebra, category, tuple, morphism, path, slice, quotient, fold, refinement, factorization, or wiring expression used as mathematical description or lens | `E.18.2`, coordinated with `C.29` when lens adequacy matters |
| semantic way of doing | `A.3.1 U.Method` |
| description of a way of doing | `A.3.2 U.MethodDescription` |
| state-space and transition-law episteme | `A.3.3 U.Dynamics` |
| law-governed operation algebra with admissibility predicates | `A.6.1 U.Mechanism` and `E.20` |
| formal declaration, substrate, invariant, morphism, construction, or postulate set | `A.6.0`, `C.29`, or the direct mathematical pattern |
| planned dated work | `A.15.2 U.WorkPlan` |
| dated work occurrence | `A.15.1 U.Work` |
| positive temporal aspect | `C.27.TA` |
| temporal claim adequacy | `C.27` |
| problem-to-principle-to-work carry-through | `E.18.1` |
| evidence, assurance, gate, decision, source, result, or publication use | the direct governing pattern for that claim |

#### A.3.4:4.6 - Description And Publication Boundary

A method description, dynamics model, transformation diagram, transformation-flow structure description, dashboard, result record, source span, publication, or proof may describe a transformation or provide evidence for a use. It is not the transformation.

If the description itself is under concern, use `C.2.1`, `A.3.2`, `A.3.3`, `E.17`, `E.18`, or the direct publication or source pattern. If the transformation is under concern, keep the description as a neighboring episteme or publication value.

#### A.3.4:4.7 - Formal Transformation And Project-World Realization

A morphism, constructive proof, formal construction, task, or state transition can be a transformation inside a formal or mathematical object of concern. That does not make it project-world work.

Use this distinction:

- If the object under concern is formal or ideal, the transformation relation may be a morphism, construction, task, or transition inside the formal substrate.
- If the object under concern is physical, organizational, architectural, documentary, or epistemic, the formal relation may specify, model, constrain, or compare the transformation, while work, realization, evidence, and result relations stay with their governing patterns.
- If a project wants to move from formal construction to project-world change, name the realization relation, work plan, work occurrence, evidence relation, and result relation separately.

#### A.3.4:4.8 - Typed Bundle Recovery Slice

Use this slice when one source phrase appears to name method, mechanism, formal construction, work, evidence, and transformation at once.

Source phrase:

> "The workflow algorithm transforms the emergency-stop specification, and the proof shows the new plant boundary is safe."

Recover the project concern first: the project is asking whether a specification episteme and an architecture-selected boundary have been changed so that an emergency-stop claim can be used safely. Then recover typed values:

```text
TransformationCore:
  transformedEntityOrStructure:
    value: emergency-stop specification episteme section
    governingPattern: C.2.1 plus the specification or publication pattern that governs the section
    objectKind: Episteme
    boundaryOrReferenceScheme: named section and declared emergency-stop boundary
    descriptionOrPublicationWhenRelevant: published specification revision
    notSelfEvidencingSource: the proof and publication do not prove their own project-world use
  boundedContext: plant-control safety specification review
  initialCondition: ambiguous stop boundary admits two incompatible readings
  postStateConditionOrDelta: revised boundary admits one declared interpretation under named conditions
  transformationRelation: specification-repair relation over the episteme section
  admissibilityOrBoundaryCondition: review condition and safety-case relation required before use
  temporalOrOrderingReference: C.27.TA validity window for the revision and review cycle

TransformationDescriptionEpisteme (C.2.1 shorthand):
  EntityOfConcernSlot: the U.Transformation identified above
  ClaimGraphSlot: claims that the specification section changed, that the proof relation bears on one formal boundary reading, and that safety use still needs assurance or gate admission
  ReferenceSchemeSlot: specification section reference plus formal-substrate interpretation and safety-case review scheme
```

Current neighboring relation references: method description for the repair procedure; formal substrate or mathematical lens for the proof; evidence or assurance relation for safety use. These references stay outside `TransformationCore`.

This slice shows the slot-bundle rule without making the claim-bearing episteme the object. The workflow label may point to a method description, a work plan, or an E.18 transformation-flow structure. The algorithm or proof may point to a formal substrate or mathematical lens. The published revised specification is an episteme or publication value. The project-world plant change, if any, needs separate work, evidence, gate, and result relations. Do not assign one typed value as method, mechanism, transformation, work, and evidence merely because the source phrase uses one convenient label.

### A.3.4:5 - Archetypal Grounding

#### A.3.4:5.1 - Physical System Change

A nuclear-plant team claims a revised operating method stabilizes a temperature profile after a thermal-power change.

`U.Transformation` names the bounded change: reactor subsystem under context, initial operating condition, post-change stability condition, transformation relation, admissibility and safety boundary, and time window. The operating method is `U.Method`; the operation algebra or control law may be `U.Mechanism`; the state-space model is `U.Dynamics`; the work trace is `U.Work`; the safety evidence and gate use remain with evidence and gate patterns.

#### A.3.4:5.2 - Biological Editing

A CRISPR project claims an editing protocol changes a DNA target while keeping off-target risk under a bound.

`U.Transformation` names the changed biological target, initial condition, post-state or delta, editing transformation relation, admissibility or boundary condition, and any temporal or ordering reference that changes the claim. The editing protocol fills `MethodDescriptionRef` or `MethodRef` when it is a selected way of doing; the biochemical mechanism fills `MechanismRef`; off-target measurements fill `EvidenceOrSourceRef`; the observed edited sequence or accepted lab output fills `ResultRef`. The protocol description is not the transformation; the biochemical mechanism is not the dated lab work; the off-target evidence is not permission to use the result.

#### A.3.4:5.3 - Specification Repair

A safety specification is revised so that an emergency-stop boundary no longer permits two incompatible readings.

`U.Transformation` can name the bounded change to the specification episteme: the affected episteme or section, the initial ambiguous condition, the clarified post-state condition, the transformation relation, and the review or acceptance condition. The edit work is `U.Work`; the repair method is `U.Method`; the revised specification remains an episteme or publication under its own governing pattern.

#### A.3.4:5.4 - Formal Construction

A mathematical proof constructs an object and shows that a morphism preserves a chosen invariant.

`U.Transformation` may govern the formal transformation when the formal object is the `EntityOfConcern`: initial formal object, constructed object or delta, morphism or construction relation, and admissibility or invariant condition. Formal substrate or mathematical lens fills `FormalOrMathLensRef` unless it is already the context-of-meaning for the formal object; the proof relation fills an evidence relation, a source relation, or a `C.2.1` claim-bearing episteme, not core transformation identity. It does not describe project-world work until a separate realization, method, work, or evidence relation is named.

#### A.3.4:5.5 - Architecture Move

An architecture team changes a selected structure so that an interlevel conflict is reduced while a key architecture characteristic stays within bounds.

`U.Transformation` names the structure change and delta condition. The architecture pattern governs the selected structure and characteristic; `C.29` may supply a mathematical lens for preserved and lost structure; `C.27.TA` may govern trajectory, cadence, recovery, inertia, or validity window; work planning and dated work stay with `A.15.2` and `A.15.1`.

#### A.3.4:5.6 - Functional Transformer In A Flow

Use this slice when the same sentence says that a system "performs a function", "transforms input to output", or "implements an algorithm". The first question is not whether a function word is present. The first question is which transformation, bearer, input/output boundary, method or algorithm, and flow position are current.

```text
Functional transformation slice:
  TransformationCore:
    transformedEntityOrStructure:
    boundedContext:
    initialCondition:
    postStateConditionOrDelta:
    transformationRelation:
    admissibilityOrBoundaryCondition:
  TransformerRef?: U.System bearing TransformerRole@Context, candidate system, or not recovered
  InputConditionOrPortRefs?: accepted input state, flow, material, energy, signal, information, work product, formal object, condition, or functional port signature
  OutputConditionOrPortRefs?: produced state, flow, material, energy, signal, information, work product, formal object, condition, or functional port signature
  FunctioningRef?: FunctionalElement@Context relation when this transformation is used as the element's functioning
  MethodRef? or MethodDescriptionRef?: algorithm, protocol, recipe, controller, or generalized method only when that claim is current
  MechanismRef?: law-governed realization or operation structure when current
  TransformationFlowStructureRef?: containing flow, path, path slice, composition, coupling, or constraint when current
```

Examples:

- A pump in a hydraulic network is a `U.System` filling `TransformerRef?` when it raises pressure or moves fluid under the current claim. Its required behavior grounds a `U.Transformation`; inlet/outlet hydraulic conditions or port signatures fill input/output slots; the pump curve may fill mechanism or dynamics slots; the network path fills `TransformationFlowStructureRef?`.
- A resistor in an electrical circuit is a system or component locus bearing transformer role when the claim is voltage-current relation, heat dissipation, or signal conditioning. Its terminals are not module interfaces by default; they are input/output or port-signature slots for the electrical transformation unless a module-interface claim is current.
- A warehouse in a logistics network performs receiving, storing, picking, or shipping transformations. The warehouse or candidate subsystem fills `TransformerRef?`; pallets, orders, inventory states, or documents fill input/output slots; a routing algorithm may be `U.Method` or `U.MethodDescription`; dated picking work remains `U.Work`.
- A refrigerator thermal cycle has compressor, condenser, expansion, and evaporator transformations inside one `TransformationFlowStructure`. The refrigerator or subsystem can fill `TransformerRef?`; heat-flow and refrigerant-state boundaries fill input/output slots; the thermodynamic mechanism and control method stay with their governing slots.
- A neural-network block transforms activations inside an architecture flow. The block can be a candidate system or module locus depending on the claim; tensor shape signatures may fill input/output slots; an attention algorithm may be method or method description; benchmarks, ablations, or pruning masks are evidence/result or architecture claims only when their governing patterns are current.

These cases permit the sentence "the system performs a functional transformation at this point in the flow" when the system/candidate system, `TransformerRole@Context`, bounded transformation, input/output boundary, and flow location are named or explicitly marked unknown/not-current. They also prevent the overread that a named algorithm, module, port, or evidence record by itself proves the transformation, functioning, compatibility, or result.

### A.3.4:6 - Bias-Annotation

Lenses tested: **Onto**, **Arch**, **Prag**, **Epist**, **Gov**.

This pattern intentionally biases toward object separation: transformation, method, mechanism, work, dynamics episteme, temporal aspect, temporal-claim adequacy, evidence, result, and publication are kept as linked values, not synonyms.

Resisted distortions:

- **software narrowing:** algorithm or process wording is treated as code-only when the project concern is a physical, formal, architectural, or project-world transformation;
- **method-as-effect:** a way of doing is treated as if it had already produced the change;
- **model-as-authority:** a dynamics episteme is treated as permission, evidence, or gate passage;
- **trace-as-law:** one work occurrence becomes a reusable law;
- **formal-as-work:** a proof construction, morphism, or formal transition is treated as project-world work;
- **temporal-overread:** rate or rhythm wording is treated as a transformation without transformation relation and boundary conditions.

### A.3.4:7 - Conformance Checklist

| Check | Conformance statement |
| --- | --- |
| `CC-A34-1` | The `TransformationCore` identifies the transformed object, bounded context, initial condition, post-state condition or delta, transformation relation, and boundary condition. |
| `CC-A34-2` | Participation and check slots are considered and each receives an open-world disposition: filled, unknown or not recovered, not asserted, not current for this claim, or used to lower or block a claim that depends on the missing value. |
| `CC-A34-3` | The transformed object is typed through its governing pattern, with A.1 used for entity, holon, or system source discipline where relevant. |
| `CC-A34-4` | Method, method description, mechanism, work plan, work occurrence, dynamics episteme, temporal aspect, temporal-claim adequacy, evidence, result, source, gate, decision, assurance, publication, and refresh or reopen values keep their own governing patterns while filling participation and check slots in the transformation ontic. |
| `CC-A34-5` | A `C.2.1` episteme may carry claims about the transformation, one transformation slot, one slot filler, or a relation among those values, but descriptions and publications of a transformation are not treated as the transformation itself. |
| `CC-A34-6` | Time, rate, rhythm, cadence, effort, inertia, freshness, validity-window, or ordering wording uses `C.27.TA` for positive temporal aspects and `C.27` for temporal-claim adequacy. |
| `CC-A34-7` | Formal or mathematical structure uses `A.6.0`, `A.6.1`, `C.29`, or the direct mathematical pattern before it is used as a transformation law, formal relation, or evidence relation. |
| `CC-A34-8` | Evidence, assurance, gate, result acceptance, and decision authority are not inferred from `TransformationCore` or from a `C.2.1` episteme about the transformation. |
| `CC-A34-9` | The identity-plus-participation slot relation follows `A.6.5` SlotKind/ValueKind/RefKind discipline; dependent patterns may cite `U.Transformation`, filled identity slots, or specific participation and check slots without copying the full slot relation or turning their own values into identity slots. |
| `CC-A34-10` | Functional-transformation uses recover `TransformerRef?`, `InputConditionOrPortRefs?`, `OutputConditionOrPortRefs?`, `FunctioningRef?`, and `TransformationFlowStructureRef?` when those claims are current; none is silently left to A.6.F, C.30.ASV, or E.18 as an outside reference. |
| `CC-A34-11` | A system/candidate system may be said to perform a functional transformation at a flow point only when the system or candidate system, `TransformerRole@Context`, bounded transformation, input/output or port boundary, and flow location are named or explicitly marked unknown/not-current. |
| `CC-A34-12` | Algorithm wording is recovered as `U.Method`, `U.MethodDescription`, formal substrate, mechanism, work, or evidence according to the current claim; it is not treated as software-only and not used as proof that transformation occurred. |

### A.3.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Method name as change | "This method transforms X" with no transformed object, condition, or delta. | Identify `TransformationCore`; keep the method in the method slot. |
| Process diagram as work | A workflow diagram is treated as enacted work. | Use `E.18` or `A.3.2` for the diagram; use `A.15.1` for dated work. |
| Dynamics model as permission | A transition law is used to approve action. | Keep `A.3.3` for the model; use evidence, gate, decision, and assurance patterns for use authority. |
| Temporal trend as intervention | A rate or rhythm trend is treated as proof of changed behavior under an intervention. | Use `C.27.TA` for the temporal aspect, `C.27` for temporal-claim adequacy, and name the transformation relation separately. |
| Formal construction as work | A morphism or proof construction is treated as work performed in a project-world object. | Use `C.29` or the direct formal pattern for the mathematical relation; name realization and work separately. |
| Publication as transformation | A dashboard or report is treated as the changed state. | Use publication or source patterns for the publication; keep the transformation as the governed object. |

### A.3.4:11 - Consequences

- FPF gains one place to identify bounded transformations without turning method, mechanism, work, dynamics, temporal aspect, temporal-claim adequacy, evidence, or publication into each other.
- `C.27.TA` can carry positive temporal aspects while `C.27` stays focused on temporal-claim adequacy and admissible use.
- `A.3.3` can stay an episteme pattern for state-space and transition-law claims.
- Users pay the cost of identifying a small `TransformationCore` when transformation is material to the project concern.
- Neighboring patterns need thin relation updates so they can cite `U.Transformation` without copying its slot relation.

### A.3.4:9 - Rationale

`U.Transformation` gives FPF one durable ontic for bounded change under conditions. Without it, method, mechanism, dynamics, work, evidence, publication, and mathematical description repeatedly compete to be "the change" and grow local shadow ontologies.

The slot-relation design keeps the ontic compact. Identity slots recover one bounded transformation; participation and check slots keep method, method description, mechanism, work plan, work occurrence, acting system, transformation-flow structure, mathematical description, dynamics episteme, temporal aspect, evidence, result, source, gate, decision, assurance, and publication connected without fusing their kinds.

### A.3.4:10 - SoTA-Echoing

| Source family | Current lesson for A.3.4 | FPF decision |
| --- | --- | --- |
| Constructor theory, including Marletto, Deutsch, and Vedral 2026 ["Tests of constructor theory"](https://arxiv.org/abs/2606.07352v1). | Constructor-theory work frames principles through possible or impossible tasks and constructors beyond ordinary computation and software programs. | Use `U.Transformation` as a substrate-neutral transformation or task ontic. Do not treat algorithm or process wording as IT-only. |
| Deutsch and Marletto 2025 ["Constructor theory of time"](https://arxiv.org/abs/2505.08692v3), arXiv version `2505.08692v3`. | Duration and dynamics need separate interpretation from the task or transformation. The source is used for the constructor-theory time/dynamics distinction, not as an imported FPF temporal ontology. | Keep temporal aspect and dynamics episteme separate from `U.Transformation`; use `C.27.TA`, `C.27`, and `A.3.3` for those claims. |
| Background engineering and modeling practice on process ontologies, flow representations, and graph descriptions. Informative only; this row does not add slots or mutate the `U.Transformation` boundary. | Compound structures can be described through flow or graph-shaped expressions, but that ordinary practice is not enough to decide whether the EoC is a selected structure, mathematical description, or publication. | Use the FPF decision already made by `E.18`, `E.18.2`, and `C.29`: keep structure claims, mathematical-description claims, and atomic transformation claims separate. |
| FPF `C.2.1 U.EpistemeSlotRelation` precedent | A compact slot relation can make a complex subject easier to use when identity and dependent slots are explicit. | Give `U.Transformation` a small slot relation and let neighboring patterns govern their own values. |

### A.3.4:12 - Relations

- **Builds on:** `E.24`, `A.1`, `A.6.0`, `A.6.5`, `C.2.1`, `A.3`, `A.7`.
- **Coordinates with:** `A.3.1`, `A.3.2`, `A.3.3`, `A.6.1`, `E.20`, `A.15.1`, `A.15.2`, `E.18`, `E.18.1`, `C.32.P2S`, `C.27.TA`, `C.27`, `C.29`, evidence, gate, decision, source, result, assurance, and publication patterns.
- **Specializes:** the A.3 transformer-constitution family for bounded transformations under declared conditions.

### A.3.4:End

