## C.30.LCA - Control Structure View Adequacy (LCA)

> **Type:** Architectural subpattern under `C.30`
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.30.LCA:1 - Problem frame

Use this pattern when a selected control structure or control-structure relation changes the next architecture move: a controller regulates a plant, an observer or estimator changes what can be known, a planner provides references to lower-rate control, a supervisor constrains a subsystem, a policy loop changes allowed behavior, or an LCA cue makes roles, rates, observation boundaries, actuation boundaries, feedback, or externalities architecture-relevant.

The first-minute working situation is ordinary engineering talk: a diagram says the supervisor watches a subsystem, a controller regulates a plant, an observer estimates state, a planner gives references to a lower-rate controller, or a policy or control relation changes allowed controller behavior. The useful first move is to recover a `ControlStructureViewNote`: which exact holon, actual architecture relation or bounded architecture claim is current; which exact selected control structure, control roles, and independently obtaining relations are present; which rate bands or recovered control-layer relations are claimed; which feedback or externality boundaries are named; and which governing pattern carries each additional claim. If the source only says `layer`, `level`, `tier`, or `stack` without a control-specific relation, use `C.30.STRAT` first.

What goes wrong if C.30.LCA is missed: a control diagram becomes the control structure, `U.View`, or proof; stratification labels bypass `C.30.STRAT` and carry undeclared scope; and `B.2.5`, E.18 transformation-flow prose, or Layered Control Architecture prose is overread as control adequacy.

What C.30.LCA buys in practice: the practitioner can keep useful controller, plant, observer, regulator, supervisor, feedback, rate, and control-layer language while recovering an exact selected control structure, one description episteme, its possible E.17.0 view conformance, and the governing pattern that carries any proof or claim named by value.

Not this pattern when the issue under repair is generic stratification or source-label repair, only an E.18 transformation-flow path slice, function description, module boundary, measurement head, causal intervention, or safety case. Use `C.30.STRAT`, `C.30.TFS-REL`, `A.6.F`, `A.6.M`, `C.16`, `C.28`, or the assurance/evidence pattern governing the claim as appropriate.

The primary EntityOfConcern for a full C.30.LCA description or view is one exact selected control `U.Structure`. The description, selected structure, controlled holon, actual architecture relation, bounded architecture claim, exact viewpoint, conformance occurrence, control-role assignments, direct control relations, diagram, representation, proof claims, and publication remain separate. Ordinary use may stop with a typed note:

```text
ControlStructureViewNote ordinary minimum:
  architectureRelationOccurrenceRef?: ArchitectureRelationRef
  architectureClaimRef?: U.EpistemeRef constrained to ArchitectureClaim
  describedHolonRef?: U.HolonRef
  selectedControlStructureRef?:
  controlledHolonRef:
  candidateViewEpistemeRef?: U.EpistemeRef
  exactViewpointRef?: U.ViewpointRef
  viewpointConformanceRelationRef?: EpistemeViewpointConformanceRelationRef
  controllerRoleAssignmentRef?:
  selectedControlRelationRef:
  feedbackClosureState: closed | oneWay | unclear
  controlLayerRelationRef?:
  rateBandRef?:
  stratificationRepairRef?:
  nextGoverningPatternApplicationRef?:
  stopCondition:
```

The ordinary note requires an exact described or controlled holon plus one selected control structure or honest structure gap and at least one direct control relation when a positive relation claim is made. `architectureRelationOccurrenceRef` is filled only when that direct C.30 occurrence obtains; `architectureClaimRef` remains optional claim content or trace. The note does not become a C.2.1 episteme or `U.View` by its field names.

Use full `ControlStructureView` only when an independently identified architecture-description episteme about the exact selected control structure satisfies the fixed E.17.0 predicate for one exact viewpoint. Full use is justified when roles, relations, rates, recovered control-layer labels, boundary refs, source return, representation/publication, or explicit governing-pattern applications matter beyond the note.

### C.30.LCA:2 - Problem

Control diagrams are persuasive because they look operational: arrows imply feedback, boxes imply responsibility, and recovered control-layer labels imply separation. In practice that is often enough for orientation, but not enough to identify selected structure, make direct relations obtain, admit the description as `U.View`, or establish architecture adequacy. A control-stack description can quietly overclaim stability, safety, evidence sufficiency, gate validity, assurance, or causality; a non-control `layer`, `level`, `tier`, or `stack` label belongs first to `C.30.STRAT`.

FPF needs a pattern that preserves useful recognition without letting the cue become structure, relation, or proof. Control roles, feedback relations, externality boundaries, and rate separations can enter an architecture structural description. The same episteme is a view only through exact viewpoint conformance. Dynamics, temporal aspects, authored temporal-claim adequacy, causal use, evidence, assurance, gates, and mathematical-lens transfer stay with their direct owners.

### C.30.LCA:3 - Forces

* Control talk is useful and current engineering practice uses it, so deleting it would make architecture prose less usable.
* The same source labels can name different things. C.30.LCA applies only after an actual control-role assignment, direct control relation, rate-band relation, control-layer relation, or `B.2.5` supervisor-subholon relation is recovered. A model-use structure is cited only when that independently selected structure changes interpretation.
* Layered and multi-rate control descriptions often need timing and dynamics claims before they can carry stability or safety claims.
* `B.2.5` already gives FPF a supervisor-subholon feedback relation, but it does not turn every feedback or loop diagram into that occurrence, selected structure, or proof.
* E.18 `TransformationFlowStructure` values and their mathematical graph descriptions can describe flow, path, crossing, or transformation-flow relations that participate in control, but the selected flow structure, graph expression, and control structure remain distinct.
* Practitioners need one small first output; exact viewpoint conformance, dynamics, C.29, evidence, assurance, and gate records are used only when the question calls for them.

### C.30.LCA:4 - Solution

Treat LCA-like source descriptions as possible inputs to a control-structure description under C.30. Recover one exact described holon, any actual architecture relation, one selected control structure, the exact controlled holon, actual control-role assignments, independently obtaining observation, actuation, reference, supervision, and feedback relations, and any rate or control-layer relation that changes the next architecture move. A.22 identifies the selected structure from exact constituents, selected obtaining relation occurrences, applied constraint claims, and the receiving-use frame; a note, diagram, list, or description creates none of them. If a source label is not yet control-specific, apply `C.30.STRAT` first. Then state admissible use and the next governing-pattern application.

The ordinary minimum may stop with a compact `ControlStructureViewNote`:

```text
ControlStructureViewNote:
  architectureRelationOccurrenceRef?: ArchitectureRelationRef
  architectureClaimRef?: U.EpistemeRef constrained to ArchitectureClaim
  describedHolonRef?: U.HolonRef
  selectedControlStructureRef?:
  controlledHolonRef:
  selectedControlRelationRef:
  feedbackClosureState: closed | oneWay | unclear
  controlLayerRelationRef?:
  rateBandRef?:
  observationBoundaryRef?:
  actuationBoundaryRef?:
  feedbackBoundaryRef?:
  externalityBoundaryRef?:
  stratificationRepairRef?:
  nextGoverningPatternApplicationRef?:
  admissibleUse:
  nonAdmissibleUse:
  stopCondition:
```

Use `rateBandRef?`, `controlLayerRelationRef?`, and `externalityBoundaryRef?` only when that object or relation changes the control-structure use. Otherwise the note may stop after one actual control relation, feedback-closure state, and next governing-pattern application. Generic stratification labels stay with `C.30.STRAT` until a control-specific relation is recovered.

When a recovered control-layer relation is used to justify decomposition, substitution, or design reliance, recover the inter-layer assumption-guarantee relation or mark the control-layer relation as orientation only. `interLayerControlRelationRefs?` is used only when the relation is already control-specific and is used for decomposition, substitution, design reliance, safety, or stability claims.

```text
InterLayerControlRelationNote:
  upperLayerAssumptionRefs:
  lowerLayerGuaranteeRefs:
  observationConditionRefs:
  actuationAuthorityRefs:
  latencyBoundRefs?:
  rateEnvelopeRefs?:
  violationFallbackRefs:
  admissibleUse:
  nonAdmissibleUse:
```

Use this note only when a recovered control-layer relation is used for decomposition, substitution, safety or stability claim, or architecture decision claim. It is not proof and does not make the relation obtain. Otherwise keep C.30.LCA at the small note or ordinary description form, or return the source label to `C.30.STRAT`.

```text
ControlStructureView ::= ArchitectureDescription & U.View & {
  viewEpistemeRef: U.EpistemeRef,
  claimGraph: exactly one C.2.1 ClaimGraph,
  entityOfConcernRef: selectedControlStructureRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue,
  selectedControlStructureRef: U.StructureRef,
  structureKindRef = ControlStructure,

  viewpointRef: U.ViewpointRef,
  viewpointConformanceRelationRef: EpistemeViewpointConformanceRelationRef,
  concernRefs?: FinSet(U.EntityRef),

  describedHolonRef?: U.HolonRef,
  architectureRelationOccurrenceRefs?: FinSet(ArchitectureRelationRef),
  architectureClaimRefs?: FinSet(U.EpistemeRef constrained to ArchitectureClaim),
  claimScope?: U.ClaimScope, byValue,
  modelUseStructureRef?: U.StructureRef,
  empiricalGroundingRelationRefs?: FinSet(EpistemeEmpiricalGroundingRelationRef),
  controlledHolonRef: U.HolonRef,

  plannerRoleAssignmentRefs?: FinSet(U.RoleAssignmentRef),
  controllerRoleAssignmentRefs?: FinSet(U.RoleAssignmentRef),
  observerRoleAssignmentRefs?: FinSet(U.RoleAssignmentRef),
  supervisorRoleAssignmentRefs?: FinSet(U.RoleAssignmentRef),
  controlMethodRefs?: FinSet(U.MethodRef),

  selectedControlRelationRefs: FinSet(U.RelationRef),
  observationRelationRefs?: FinSet(U.RelationRef),
  actuationRelationRefs?: FinSet(U.RelationRef),
  referenceProvisionRelationRefs?: FinSet(U.RelationRef),
  feedbackRelationRefs?: FinSet(U.RelationRef),
  controlLayerRelationRefs?: FinSet(U.RelationRef),
  rateBandRefs?: FinSet(RateBandRef),
  interLayerControlRelationRefs?: FinSet(U.RelationRef),
  supervisorSubholonRelationRefs?: FinSet(U.RelationRef),

  observationBoundaryRefs?: FinSet(BoundaryRef),
  actuationBoundaryRefs?: FinSet(BoundaryRef),
  feedbackBoundaryRefs?: FinSet(BoundaryRef),
  externalityBoundaryRefs?: FinSet(BoundaryRef),
  transformationFlowPathSliceRefs?: FinSet(PathSliceId),

  stratificationRepairRefs?: FinSet(C30STRATRepairRef),
  sourceToUsePathRefs?: FinSet(U.RelationRef),
  downstreamGoverningPatternApplicationRefs?,
  representationRefs?: FinSet(U.EntityRef),
  publicationOccurrenceRefs?: FinSet(EpistemePublicationRelationRef),
  publicationFormRefs?: FinSet(U.EntityRef),
  carrierRefs?: FinSet(U.EntityRef constrained to U.PresentationCarrier),
  admissibleUse,
  nonAdmissibleUse,
  sourceReturnCondition?
}
```

The full view is the same C.2.1 episteme identified by its exact claim graph, selected-control-structure EntityOfConcern, and effective scheme. Its direct E.17.0 conformance occurrence has exactly that candidate episteme and one exact viewpoint episteme as participants; the fixed five-part predicate and participant-determined identity govern it. Authoring, A.6.3 construction, a `viewpointRef`, query, selection, bundle membership, diagramming, rendering, publication, or current use does not make it obtain.

`controlledHolonRef` names the holon whose state is observed or changed by independently obtaining control relations and may be the described holon or one of its exact parts. Architecture claims, `ClaimScope`, model-use structure, concern, and empirical grounding remain optional neighboring objects or relations. `modelUseStructureRef` appears only when an independently selected DDD-style bounded-model-use structure changes interpretation or selection.

Every positive control-role assignment and control-relation reference identifies an actual occurrence admitted by its direct pattern. The description, control note, view record, or diagram neither creates those occurrences nor acts. Representation, publication occurrence, form, and carrier likewise remain separate from the selected structure and view episteme.

#### C.30.LCA:4.0a - Safety-loss control-structure note

Use a `SafetyLossControlStructureNote` only when safety wording is being used for a loss-control claim and the practitioner first needs the architecture-side loss-control structure, not a safety-case verdict:

```text
SafetyLossControlStructureNote:
  lossOrHarm:
  hazardOrUnsafeState:
  unsafeControlActionOrMissingControl:
  controlledProcessOrPlantRef:
  controlConstraintRef:
  feedbackOrObservabilityBoundary:
  timingOrRateBoundary:
  operationalDesignScopeOrMisuseScope:
  foreseeableMisuseRefs?:
  architectureStructureKindRefs:
    ControlStructure | ConstraintRequirementStructure |
    SecurityTrustBoundaryStructure | InformationDataStructure |
    EvidenceAssuranceStructure
  governingPatternApplicationRefs:
    A.3.3 dynamics, C.27.TA temporal aspect or rate, and C.27 authored temporal-claim adequacy,
    C.28 causal-use, A.10 or G.6 evidence,
    B.3 assurance, A.20 or A.21 gate
  nonAdmissibleUse:
    not safety proof, not safety-case verdict, not regulatory acceptance
```

The note gives a positive safety-triggered architecture move: find the loss-control structure, controlled process or plant, constraint, foreseeable misuse, operational design scope, and action-relevant boundary. It does not replace the generic control-structure view and does not replace evidence, assurance, gate, causal, dynamics, or temporal claims.

**Role interpretation.**

| Source label | FPF recovery |
|---|---|
| Plant or controlled holon | `U.Holon` whose state evolves; reusable state-evolution claims use `A.3.3`. |
| Regulator or controller | System in a control role enacting a method over observations and actuations. |
| Planner | Acting system in a planner role; the enacted method may structure setpoint, plan, reference, or allowed-region production. |
| Observer or estimator | Acting system in an observer or estimator role; the enacted method may structure state estimates, observations, or evidence-facing readouts. |
| Supervisor | Acting system in a supervisor role; the enacted method or policy may structure work that constrains subordinate holons, gates, policy changes, or control-mode changes. |

**Control-specific stratification gate.** `Layer`, `level`, `tier`, and `stack` enter C.30.LCA only after `C.30.STRAT` or the local sentence recovers a control-role assignment, direct control relation, inter-layer control relation, rate band, or `B.2.5` supervisor-subholon relation. A label by itself does not establish control structure or separation.

**B.2.5 boundary.** `B.2.5` governs the supervisor-subholon feedback relation. `C.30.LCA` may cite such a relation as part of the selected control structure, but stability, safety, causality, evidence, gate, and assurance claims still use their direct governing patterns. If an episteme appears in a control example, name the acting system, its role assignment, enacted method when current, and any publication, source-to-use, or work-reliance relation. An episteme does not sense, decide, plan, adapt, or act as an agent.

**Transformation-flow boundary.** An `E.18` transformation-flow path slice may supply flow-structure, path, crossing, or transformation-flow-structure input to the control view when that relation is being used. The transformation-flow graph expression remains a mathematical description or view of transformation-flow structure. It does not become the functional architecture, the control structure, or proof of control adequacy.

**C.29 boundary.** An LCA can be a model used for one selected control structure, or it can be used as a transferable mathematical lens. Open `C.29` only when transfer, prediction, reusable cross-domain explanation, or mathematical-lens use is being claimed. Dynamics, rate bands, authored temporal-claim adequacy, and causal claims remain with `A.3.3`, `C.27.TA`, `C.27`, and `C.28`.

**Nesting and scale rule.** If a control-structure view nests without a local depth limit, the record uses `scaleAuditRef?` when the nesting affects latency, stability, observability, accountability, or assurance.

**Worked slice A - LCA diagram used as proof.** A safety note says: `The Layered Control Architecture proves the plant is safe because the supervisor monitors the lower controller.` A conforming repair keeps the control-structure view and names planner, controller, plant, and supervisor relations, observation and actuation boundaries, and any rate bands. Safety and assurance claims use `B.3`, evidence to `A.10` or `G.6`, temporal-aspect and rate-band claims to `C.27.TA`, authored temporal-claim adequacy to `C.27`, and dynamics or stability claims use `A.3.3` or the appropriate dynamics claim.

**Worked slice B - multi-rate controller.** A source says a control stack has a slow planner, a faster regulator, and an observer with a different update period. Apply `C.30.LCA` to the case only after the stack label has been recovered as control roles, relations, and rate bands; otherwise the label is recovered first by `C.30.STRAT`. C.30.LCA does not claim rate adequacy. If the rate relation matters for oscillation, latency, stability, or safety, the next admissible use is `C.27.TA` for temporal aspect or rate-band structure, plus `C.27` only when an authored temporal-claim adequacy question is under repair, and the dynamics or assurance pattern named by value when that claim kind is being made.

**Worked slice C - supervisor-subholon loop.** A subsystem is supervised by an external controller that changes allowed modes. `C.30.LCA` records the supervisor-subholon relation and may reference `B.2.5`. If the text claims that this loop authorizes work, passes a gate, or proves a policy constraint, the claim uses `A.15`, `A.20`, or `A.21`.

**Currentness and smallest reopen.** When a decisive input changes, reopen only the control-structure locus and use conclusion that depend on it. A changed selected control structure or controlled holon reopens the affected `ControlStructureViewNote` or full description/view; a changed role assignment or direct relation reopens that exact assignment or occurrence and its dependent structure selection; changed feedback, rate, or control-layer relations reopen only their matching relation or boundary fields; changed view conformance reopens only the E.17.0 admission; and a changed source edition reopens its source-to-use and source-return locus. A changed safety or proof claim, or a changed direct governor, reopens only that neighboring claim or governor-owned relation unless a control-structure input also changed. Update the affected locus, demote full view use to a note or orientation, narrow use, or reopen the control-structure question; unrelated structures and claims stay closed.

### C.30.LCA:5 - Archetypal Grounding

| Archetype | Without C.30.LCA | With C.30.LCA |
|---|---|---|
| System | A plant, controller, or supervisor diagram is treated as if the drawing itself established the controlled system's behavior. | The controlled system, controller, observer, planner, supervisor, boundaries, rate bands, actual control relations, and selected control structure remain separately recoverable. |
| Episteme | A control-description publication is read as structure, `U.View`, or proof because it uses familiar control labels. | The exact description episteme has one selected-structure EntityOfConcern; it is a view only through exact E.17.0 conformance. Representation, publication, and proof-like claims stay separate. |

### C.30.LCA:6 - Bias-Annotation

* **Diagram authority bias.** A neat feedback diagram can look more persuasive than the exact structure, source-to-use path, work-reliance relation, or claim it actually supports. Repair by naming each direct object/relation and governing pattern.
* **Stratification-label bias.** A `layer`, `level`, `tier`, or `stack` label can hide whether it names a control relation, rate band, aggregation, scale, organization, Work scope, evidence scope, deployment, or publication section. Repair with `C.30.STRAT`; C.30.LCA applies only to the recovered control-specific case.
* **Supervisor anthropomorphism.** A supervisor label can make an episteme, policy, or dashboard sound agentive. Repair by naming the acting system in role, the method it enacts when current, and the Work or review practice when current.
* **Transformation-flow and LCA conflation.** A transformation-flow graph expression and a control description/view can inform each other, but neither replaces the other. Repair by naming the exact EntityOfConcern, structure kind, and direct relations for each.

This checklist verifies the preceding guidance after the practitioner has chosen the selected repair action; it is not a required project control form and not a substitute for the note, description episteme, conformance occurrence, direct control relation, or repair guidance above.

### C.30.LCA:7 - Conformance Checklist

| ID | Check | Why it matters |
|---|---|---|
| CC-LCA-1 | A conforming full description/view has one exact C.2.1 identity whose EntityOfConcern is one exact selected control structure; the described and controlled holons and any actual `ArchitectureRelation` remain separately recoverable. | Prevents a free-floating diagram, claim, or unspecified relation set from becoming structure or episteme identity. |
| CC-LCA-2 | A conforming use records the actual control-role assignments and direct relations present: planner, regulator/controller, observer/estimator, plant/controlled system, supervisor, or the local subset. | Keeps the view action-guiding without making the description act. |
| CC-LCA-3 | `Layer`, `level`, `tier`, or `stack` wording enters only with a recovered control-role assignment, direct control relation, inter-layer relation, rate band, or `B.2.5` supervisor-subholon relation. | Prevents generic stratification wording from standing in for control structure. |
| CC-LCA-4 | A claimed `U.View` names the exact viewpoint episteme and independently obtaining `EpistemeViewpointConformanceRelation`; bundle membership, viewpoint label, authoring, query, diagram, and publication are insufficient. | Keeps structural description and view membership distinct. |
| CC-LCA-5 | Stability, safety, dynamics, temporal-aspect or rate-band structure, authored temporal-claim adequacy, causal use, empirical grounding, evidence, gate, and assurance claims are assigned to their governing patterns. | Prevents LCA-as-proof. |
| CC-LCA-6 | `B.2.5` is used only for the supervisor-subholon feedback relation it governs. | Keeps a cited feedback relation distinct from stability, safety, evidence, gate, and assurance claims. |
| CC-LCA-7 | An E.18 transformation-flow path slice used by the control view remains an exact selected transformation-flow object governed by E.18, not the control structure or actual transformation itself. | Keeps transformation-flow and LCA relations distinct. |
| CC-LCA-8 | C.29 or mathematical-lens use is opened when LCA is transferred across domains or used for prediction, reusable explanation, or assurance input. | Preserves mathematical-lens use and representation boundaries. |
| CC-LCA-9 | The record states admissible use, non-admissible use, and source-return condition; representation and E.24.PUB occurrence/form/carrier remain separate. | Prevents narrowed recognition or publication from becoming unchecked reliance. |

### C.30.LCA:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| LCA-as-proof | The text says the control stack proves safety, stability, or gate readiness. | Keep the control view and assign proof or claim named by value to dynamics, evidence, assurance, gate, or safety patterns. |
| Control-layer-as-generic-level | `Layer`, `level`, `tier`, or `stack` is used without a control-role assignment, direct control relation, inter-layer relation, rate band, or `B.2.5` supervisor-subholon relation. | Apply `C.30.STRAT`; return to C.30.LCA only after a control-specific relation is recovered. |
| Agentive episteme | A policy, model, dashboard, or architecture note is said to watch, decide, plan, or adapt. | Name the acting system, actual role assignment, enacted method when current, Work occurrence when current, and any publication, source-to-use, or work-reliance relation. |
| Transformation-flow and LCA substitution | A transformation-flow graph expression is treated as control architecture, or an LCA diagram is treated as the transformation-flow graph expression. | Recover both exact selected structures and description epistemes separately; use E.17.0 only for actual viewpoint conformance. |
| Hidden rate claim | Multi-rate control is named, but rate adequacy is not checked. | Add `rateSeparationClaimRefs?`; assign temporal-aspect or rate-band claims to `C.27.TA` and authored temporal-claim adequacy to `C.27`. |

### C.30.LCA:9 - Consequences

The gain is a small, usable control-structure output that preserves common architecture language while blocking structure, view, and proof overread. Practitioners can still say `controller`, `plant`, `supervisor`, `feedback`, and `control layer`, but the record shows the exact selected structure, description/view boundary, and direct relations those words carry; generic stratification labels use `C.30.STRAT` first.

The cost is an extra relation or conformance note before downstream reliance. When the claim is only recognition, that cost is small. When it is view membership, safety, stability, evidence, assurance, or gate passage, the cost is appropriate because none was carried by the diagram alone.

### C.30.LCA:10 - Rationale

Control architecture is too important to leave to diagram authority and too useful to remove from architecture language. The FPF move is to keep the practice cue and recover control-structure content first: exact selected structure, controlled holon, actual architecture relation when current, control roles, direct control relations, recovered rate/control-layer labels, observation and actuation boundaries, externality boundaries, and next admissible move. The full record is one description episteme and, only through exact E.17.0 conformance, the same episteme as `U.View`. It can cite `C.30.STRAT`, `B.2.5`, E.18 transformation-flow structure, dynamics, `C.27.TA`, `C.27`, `C.28`, evidence, assurance, gates, and C.29, but does not absorb their claim kinds.

This protects subject, structure, episteme, View, representation, and publication boundaries. Several descriptions may have the same selected control structure as EntityOfConcern, and one description may be published repeatedly without changing identity, creating the structure, granting view membership, or making direct relations obtain.

### C.30.LCA:11 - SoTA-Echoing

| SoTA and practice source | What it contributes | FPF adoption stance | Practitioner implication |
| --- | --- | --- | --- |
| Anderson, Doyle, Low, and Matni, "System Level Synthesis" (Annual Reviews in Control, 2019). | Structured controller-synthesis practice treats closed-loop responses, constraints, locality, and distributed implementation as explicit synthesis variables and implementation relations rather than as a box-and-arrow guarantee. | Adopt and adapt: use SLS as current control-structure pressure for explicit role, relation, locality, rate, and implementation-boundary fields; do not import SLS proof claims into C.30.LCA. | A distributed-control diagram can start a control-structure description; stability or robust-performance claims are governed by dynamics or control-proof patterns. |
| Ames, Coogan, Egerstedt, Notomista, Sreenath, and Tabuada, "Control Barrier Functions: Theory and Applications" (ECC, 2019). | Safety-critical control separates a controller structure from a safety property and the mathematical certificate or enforcement method used for that property. | Adopt and adapt: keep safety wording visible as a neighboring safety or proof claim, not as control-view adequacy. | When a sentence says the supervisor/controller makes the plant safe, keep the control description and assign safety to the direct safety, dynamics, evidence, or assurance pattern. |
| Rawlings, Mayne, and Diehl, *Model Predictive Control: Theory, Computation, and Design*, 2nd ed. (2017). | Planner/regulator, receding horizon, constraint, update period, and model-boundary distinctions are current MPC structure cues. | Adopt as control vocabulary: recover roles, rates, model boundaries, and constraints; route temporal/rate claims to `C.27.TA`, authored temporal adequacy to `C.27`, and dynamics to `A.3.3`. | A multi-rate or MPC-style note names rate bands and model boundaries before claiming adequacy. |
| Leveson and Thomas, *STPA Handbook* (2018), as systems-theoretic safety-control practice. | Safety analysis treats unsafe control actions, feedback, process models, constraints, and losses as control-structure-relevant distinctions. | Adopt and adapt: allow safety-loss control-structure notes, while keeping safety-case verdicts and evidence sufficiency outside C.30.LCA. | A loss-control diagram can organize the description; it does not close the safety case. |
| FPF `C.2.1`, `A.22`, `C.30`, `C.30.AD`, `E.17.0`, and `C.30.ASV`. | These patterns separate exact selected control structure, architecture relation/claim, description episteme, viewpoint episteme, conformance occurrence, and described/controlled holon. | Bind `ControlStructureView` to one selected `U.Structure` and exact viewpoint conformance; recover every control relation through its direct pattern. | A control view can coordinate several relations without becoming the architecture, relation occurrence, or proof. |

### C.30.LCA:12 - Relations

* Builds on `C.30` for direct architecture relation and selected-structure adequacy, `C.30.AD` for description identity/use, `E.17.0` for direct viewpoint conformance, and `C.30.ASV` for structural-view adequacy.
* Uses `A.22` for exact structure identity and structure-kind discipline.
* Coordinates with `C.30.STRAT` when layer, level, tier, stack, ladder, rung, block, expert, cache, router, gate, or similar source labels must be recovered before control-specific use.
* Coordinates with `B.2.5` for supervisor-subholon feedback relation recognition.
* Coordinates with E.18 and C.30.TFS-REL when transformation-flow path slices supply structure input to the control view.
* Applies `A.3.3` for dynamics/stability, `C.27.TA` for temporal-aspect/rate-band structure, `C.27` for authored temporal-claim adequacy, `C.28` for causal use, A.10/G.6 for evidence, B.3 for assurance, A.20/A.21 for constraint validity/gates, A.15 for Work/project use, E.24.PUB for publication, and C.29 for representation or transferable mathematical-lens use.

Neighboring claims stay with their governing patterns: C.30.STRAT for stratification/source-label repair; C.30 for actual architecture relations and selected structures; C.30.AD for description; E.17.0/C.30.ASV for view conformance and adequacy; B.2.5 for supervisor-subholon feedback; E.18 for graph/path/crossing structure; A.3.3 for dynamics; C.27.TA/C.27 for temporal claims; C.28 for causal use; A.10/G.6 for evidence; B.3 for assurance; A.20/A.21 for gate and constraint-validity records; A.15 for Work; E.24.PUB for publication; and C.29 for representation/lens use. C.30.LCA governs only the exact control-structure description/view adequacy at issue.

### C.30.LCA:End

