## C.30.LCA - Control Structure View Adequacy (LCA)

> **Type:** Architectural subpattern under `C.30`
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.30.LCA:1 - Problem frame

Use this pattern when a control diagram, control-language source, or selected control structure changes the next architecture move. Start with an ordinary question: what actually controls what, through which observation, command, reference, supervision, or feedback relation? A label such as controller, plant, observer, planner, supervisor, or policy loop is only a cue; identify the relation and what each participant does in it before relying on the diagram.

A participating System, local system-role kind, System-classification judgment, assignment, Method, or Work is a separate fact. Add it only when it independently obtains and changes the use of the control-structure result.

The first useful result can be one sentence: “Supervisor S sends allowed-mode commands to controller C and receives status feedback; this diagram does not yet establish stability or safety.” The small note below retains that result and the next action. If the source says only `layer`, `level`, `tier`, or `stack` without a control-specific relation, use `C.30.STRAT` first.

What goes wrong if C.30.LCA is missed: a control diagram becomes the control structure, `U.View`, or proof; stratification labels bypass `C.30.STRAT` and carry undeclared scope; and `B.2.5`, E.18 transformation-flow prose, or Layered Control Architecture prose is overread as control adequacy.

What C.30.LCA buys in practice: the practitioner can keep useful controller, plant, observer, regulator, supervisor, feedback, rate, and control-layer language while recovering a selected control structure, one description episteme, its possible E.17.0 view conformance, and the pattern used to state or test each proof or claim.

Not this pattern when the issue under repair is generic stratification or source-label repair, only an E.18 transformation-flow path slice, function description, module boundary, measurement head, causal intervention, or safety case. Use `C.30.STRAT`, `C.30.TFS-REL`, `A.6.F`, `A.6.M`, `C.16`, `C.28`, or the applicable assurance or evidence pattern to state or test the current claim.

The primary EntityOfConcern for a full C.30.LCA description or view is one exact selected control `U.Structure`. The description, selected structure, controlled holon, architecture relation, architecture claim, viewpoint, conformance occurrence, control relations and their participants, any participating Systems, classifications, assignments, Methods or Work, diagram, representation, proof claims, and publication remain separate. Start with the smallest useful note:

```text
ControlStructureViewNote ordinary minimum:
  controlledHolonRef:
  selectedControlStructureRef?:
  structureGap?:
  selectedControlRelationRef:
  controlRelationParticipantRefs:
  feedbackClosureState: closed | oneWay | unclear
  nextPatternUseRef?:
  stopCondition:
```

Use either `selectedControlStructureRef` or an honest `structureGap`. A positive control claim also names at least one obtaining control relation and its participants. This note is enough when those values make the next action clear; its fields do not turn it into a C.2.1 episteme or `U.View`.

Add a described holon, an architecture-relation occurrence or claim, rate bands, control-layer relations, boundaries, view and viewpoint-conformance facts, source return, representation, or publication only when they change the intended use. Add participating Systems, local classifications, assignments, Methods, Work, and F.6 attribution only when those neighboring facts are independently current.

When either form includes actual control Work, each Work ref names an occurrence independently admitted under A.15.1 after every exact actual performer is recovered through A.13. `assignmentRows` and `actualControlWorkAttributionRefs` remain optional: include them only when the note, view, or receiving use expressly represents precise assignment-bound attribution. Any present attribution ref resolves through F.6 to the same obtaining A.13 assignment; absence or failure of that relation leaves the Work ref intact. The note or view creates none of these facts.

Use full `ControlStructureView` only when an independently identified architecture-description episteme about the selected control structure satisfies the fixed E.17.0 predicate for one viewpoint. Full use is justified when control-participant meanings, direct relations, rates, recovered control-layer labels, boundary refs, source return, representation or publication, or the patterns used for particular claims matter beyond the note.

### C.30.LCA:2 - Problem

Control diagrams are persuasive because they look operational: arrows imply feedback, boxes imply responsibility, and recovered control-layer labels imply separation. In practice that is often enough for orientation, but not enough to identify selected structure, make direct relations obtain, admit the description as `U.View`, or establish architecture adequacy. A control-stack description can quietly overclaim stability, safety, evidence sufficiency, gate validity, assurance, or causality; a non-control `layer`, `level`, `tier`, or `stack` label belongs first to `C.30.STRAT`.

FPF needs a pattern that preserves useful recognition without letting the cue become structure, relation, or proof. Direct control relations, their participant meanings, feedback relations, externality boundaries, and rate separations can enter an architecture structural description. The same episteme is a view only through viewpoint conformance. Systems, local kinds, separate System-classification judgments, assignments, Methods, and Work are optional neighboring facts; use the relevant patterns to state or test authority, responsibility, safety, stability, gates, evidence, assurance, and causal effects.

### C.30.LCA:3 - Forces

* Control talk is useful and current engineering practice uses it, so deleting it would make architecture prose less usable.
* The same source labels can name different things. C.30.LCA applies after an exact direct control relation, rate-band relation, control-layer relation, or `B.2.5` supervisor-subholon relation is recovered. An assignment is neither required nor sufficient for control; include it only when it independently obtains. A model-use structure is cited only when that independently selected structure changes interpretation.
* Layered and multi-rate control descriptions often need timing and dynamics claims before they can carry stability or safety claims.
* `B.2.5` already gives FPF a supervisor-subholon feedback relation, but it does not turn every feedback or loop diagram into that occurrence, selected structure, or proof.
* Mathematical graph descriptions of E.18 `TransformationFlowStructure` values can describe flow, path, crossing, or transformation-flow relations relevant to control, but the selected flow structure, graph expression, and control structure remain distinct.
* Practitioners need one small first output; exact viewpoint conformance, dynamics, C.29, evidence, assurance, and gate records are used only when the question calls for them.

### C.30.LCA:4 - Solution

Treat LCA-like source descriptions as possible inputs to a control-structure description under C.30. Recover one described holon, any actual architecture relation, one selected control structure, the controlled holon, independently obtaining observation, actuation, reference, supervision, and feedback relations, and the participant meaning in each relation.

Add participating Systems, local kinds, separate System-classification judgments, assignment species and obtaining occurrences, Methods, and actual Work only when the corresponding fact is independently established. Use A.22 to identify the selected structure from its constituents, selected obtaining relation occurrences, applied constraint claims, and receiving-use frame; a note, diagram, list, description, kind, or assignment creates none of them. If a source label is not yet control-specific, apply `C.30.STRAT` first. Then state admissible use and the next pattern to use.

When the result must retain boundary, admissible-use, or handoff detail, expand the same `ControlStructureViewNote`:

```text
ControlStructureViewNote:
  architectureRelationOccurrenceRef?: ArchitectureRelationRef
  architectureClaimRef?: U.EpistemeRef constrained to ArchitectureClaim
  describedHolonRef?: U.HolonRef
  selectedControlStructureRef?:
  structureGap?:
  controlledHolonRef:
  selectedControlRelationRef:
  controlRelationParticipantRefs:
  feedbackClosureState: closed | oneWay | unclear
  controlLayerRelationRef?:
  rateBandRef?:
  observationBoundaryRef?:
  actuationBoundaryRef?:
  feedbackBoundaryRef?:
  externalityBoundaryRef?:
  stratificationRepairRef?:
  nextPatternUseRef?:
  admissibleUse:
  nonAdmissibleUse:
  stopCondition:
```

Use `rateBandRef?`, `controlLayerRelationRef?`, and `externalityBoundaryRef?` only when that object or relation changes the control-structure use. Otherwise the note may stop after one actual control relation, feedback-closure state, and the next pattern to use. Generic stratification labels stay with `C.30.STRAT` until a control-specific relation is recovered.

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

Use this note only when a recovered control-layer relation is used for decomposition, substitution, a safety or stability claim, or an architecture decision. It is not proof and does not make the relation obtain. Otherwise keep C.30.LCA at the small note or ordinary description form, or use `C.30.STRAT` to recover the source label.

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

  selectedControlRelationRefs: FinSet(U.RelationRef),
  controlRelationParticipantRefs: FinSet(U.EntityRef),
  observationRelationRefs?: FinSet(U.RelationRef),
  actuationRelationRefs?: FinSet(U.RelationRef),
  referenceProvisionRelationRefs?: FinSet(U.RelationRef),
  feedbackRelationRefs?: FinSet(U.RelationRef),
  controlLayerRelationRefs?: FinSet(U.RelationRef),
  rateBandRefs?: FinSet(RateBandRef),
  interLayerControlRelationRefs?: FinSet(U.RelationRef),
  supervisorSubholonRelationRefs?: FinSet(U.RelationRef),

  participatingSystemRefs?: FinSet(U.EntityRef constrained to U.System),
  localSystemRoleKindRefs?: FinSet(U.KindRef),
  systemRoleClassificationJudgmentRefs?: FinSet(U.RelationRef),
  assignmentRows?: FinSet({
    assignmentSpeciesRef: U.RelationKindRef constrained under U.SystemRoleAssignment,
    assignmentOccurrenceRef: U.RelationRef constrained to an obtaining occurrence of assignmentSpeciesRef
  }),
  actualControlWorkRefs?: FinSet(U.EntityRef constrained to U.Work),
  actualControlWorkAttributionRefs?: FinSet(U.RelationRef constrained to obtaining performedUnderAssignment relations),

  observationBoundaryRefs?: FinSet(BoundaryRef),
  actuationBoundaryRefs?: FinSet(BoundaryRef),
  feedbackBoundaryRefs?: FinSet(BoundaryRef),
  externalityBoundaryRefs?: FinSet(BoundaryRef),
  transformationFlowPathSliceRefs?: FinSet(PathSliceId),

  stratificationRepairRefs?: FinSet(C30STRATRepairRef),
  sourceToUsePathRefs?: FinSet(U.RelationRef),
  downstreamPatternUseRefs?,
  representationRefs?: FinSet(U.EntityRef),
  publicationOccurrenceRefs?: FinSet(EpistemePublicationRelationRef),
  publicationFormRefs?: FinSet(U.EntityRef),
  carrierRefs?: FinSet(U.EntityRef constrained to U.PresentationCarrier),
  admissibleUse,
  nonAdmissibleUse,
  sourceReturnCondition?
}
```

The full view is the same C.2.1 episteme identified by its exact claim graph, selected-control-structure EntityOfConcern, and effective scheme. Its direct E.17.0 conformance occurrence has exactly that candidate episteme and one exact viewpoint episteme as participants. It obtains only when the fixed five-part predicate is true, and those participants determine its identity. Authoring, A.6.3 construction, a `viewpointRef`, query, selection, bundle membership, diagramming, rendering, publication, or current use does not make it obtain.

`controlledHolonRef` names the holon whose state is observed or changed by independently obtaining control relations and may be the described holon or one of its exact parts. Architecture claims, `ClaimScope`, model-use structure, concern, and empirical grounding remain optional neighboring objects or relations. `modelUseStructureRef` appears only when an independently selected DDD-style bounded-model-use structure changes interpretation or selection.

For every positive control-relation reference, identify the actual occurrence and use the relevant pattern to recover what its participants mean. Identify any participating System, local classification, assignment, Method, Work, or F.6 attribution independently on its own admitted basis. A classification or assignment establishes neither control nor action.

The description, control note, view record, and diagram create none of these occurrences. Representation, publication occurrence, form, and carrier likewise remain separate from the selected structure and view episteme.

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
  claimPatternUseRefs:
    A.3.3 dynamics, C.27.TA temporal aspect or rate, and C.27 authored temporal-claim adequacy,
    C.28 causal-use, A.10 bounded source-to-use reliance, G.6 citable provenance paths,
    B.3 named assurance, A.20 internal-constraint validity, A.21 gate decisions
  nonAdmissibleUse:
    not safety proof, not safety-case verdict, not regulatory acceptance
```

The note gives a positive safety-triggered architecture move: find the loss-control structure, controlled process or plant, constraint, foreseeable misuse, operational design scope, and action-relevant boundary. It does not replace the generic control-structure view and does not replace evidence, assurance, gate, causal, dynamics, or temporal claims.

**Control-participant interpretation.**

| Source label | FPF recovery |
|---|---|
| Plant or controlled holon | `U.Holon` whose state evolves; reusable state-evolution claims use `A.3.3`. |
| Regulator or controller | Recover the regulation or control relation and its participant meaning. If control Work is claimed, recover the exact performer System through A.13 and admit the Work independently through A.15.1 with its enacted Method. Add an assignment occurrence and F.6 only when the control account expressly consumes precise assignment-bound attribution. Add local classification only when relied on; assignment supplies none. |
| Planner | Recover the exact reference-provision, planning, or other direct relation. A planning System and planning Work are separate; for a plan, authority, or allowed-region result, use its own pattern. |
| Observer or estimator | Recover the observation or estimation relation and participant meaning. If observation or estimation Work occurred, recover the exact performer System through A.13 and admit the dated Work and enacted Method independently through A.15.1. Add assignment and F.6 only when precise assignment-bound attribution is expressly consumed; a reading or evidence result remains separate. |
| Supervisor | Recover the exact supervision or `B.2.5` supervisor-subholon relation. Use separate patterns for any constraining Work, policy change, authority, responsibility, gate, or control-mode change. |

**Control-specific stratification gate.** `Layer`, `level`, `tier`, and `stack` enter C.30.LCA only after `C.30.STRAT` or the local sentence recovers a direct control relation, inter-layer control relation, rate band, or `B.2.5` supervisor-subholon relation. An assignment alone is insufficient, and the label by itself establishes neither control structure nor separation.

**B.2.5 boundary.** Use `B.2.5` for the supervisor-subholon feedback relation. A `C.30.LCA` use may cite that relation as part of the selected control structure, but use the relevant patterns for stability, safety, causality, evidence, gate, and assurance claims. If action involving an episteme is claimed, recover the exact performing System through A.13 and admit the dated Work and enacted Method independently through A.15.1. Add an assignment occurrence and F.6 only when the account expressly consumes precise assignment-bound attribution; keep publication, source-to-use, and work-reliance relations separate.

**Transformation-flow boundary.** An `E.18` transformation-flow path slice may supply flow-structure, path, crossing, or transformation-flow-structure input to the control view when that relation is being used. The transformation-flow description may use a mathematical graph expression under `E.18.2`; the description is a `U.View` only when E.17.0 conformance obtains. Neither the expression nor the description becomes the functional architecture, the control structure, or proof of control adequacy.

**C.29 boundary.** An LCA can be a model used for one selected control structure, or it can be used as a transferable mathematical lens. Use `C.29` when a mathematical lens makes transfer, prediction, reusable cross-domain explanation, or another control-structure use more inspectable. Dynamics, rate bands, authored temporal-claim adequacy, and causal claims remain with `A.3.3`, `C.27.TA`, `C.27`, and `C.28`.

**Nesting and scale rule.** If a control-structure view nests without a local depth limit, the record uses `scaleAuditRef?` when the nesting affects latency, stability, observability, accountability, or assurance.

**Worked slice A - LCA diagram used as proof.** A safety note says: `The Layered Control Architecture proves the plant is safe because the supervisor monitors the lower controller.` A conforming repair keeps the control-structure view and names planner, controller, plant, and supervisor relations, observation and actuation boundaries, and any rate bands. Use the applicable safety pattern for the safety claim, `B.3` only for a named assurance claim, `A.10` for bounded source-to-use reliance, `G.6` for citable provenance paths, `C.27.TA` for temporal aspects and rate bands, `C.27` for authored temporal-claim adequacy, and `A.3.3` or the applicable dynamics pattern for dynamics or stability.

**Worked slice B - multi-rate controller.** A source says a control stack has a slow planner, a faster regulator, and an observer with a different update period. Apply `C.30.LCA` only after the stack label has been recovered as exact reference-provision, regulation, observation, or other control relations with their participant meanings and rate bands; otherwise use `C.30.STRAT` first. Systems, classifications, assignments, Methods, and Work are added only where independently current. A C.30.LCA description establishes no rate adequacy. If the rate relation matters for oscillation, latency, stability, or safety, next use `C.27.TA` for temporal aspect or rate-band structure, `C.27` when an authored temporal-claim adequacy question is under repair, and the dynamics or assurance pattern named by value when that claim kind is being made.

**Worked slice C - supervisor-subholon loop.** A subsystem is supervised by an external controller System. The C.30.LCA note records the supervisor-subholon relation and may reference `B.2.5`. If that System performs mode-change Work, recover it through A.13 and admit the Work and enacted Method independently through A.15.1. Add an assignment occurrence and F.6 only when this slice also expressly represents precise assignment-bound attribution; missing or failed F.6 leaves the mode-change Work intact. Authority, responsibility, gate passage, safety, stability, and policy-constraint results remain separate claims under their own patterns; the supervisor relation establishes none of them.

**Currentness and smallest reopen.** When a decisive input changes, reopen only the control-structure locus and the use conclusions that depend on it. A changed selected control structure or controlled holon reopens the affected `ControlStructureViewNote` or full description and view; a changed direct control relation or participant meaning reopens that occurrence and its dependent structure selection; a changed classification, assignment, Method, Work, or F.6 attribution reopens only that neighboring fact and any view use that relied on it. Changed feedback, rate, or control-layer relations reopen only their matching relation or boundary fields; changed view conformance reopens only the E.17.0 admission; and a changed source edition reopens its source-to-use and source-return locus. A changed authority, responsibility, safety, proof, evidence, assurance, or gate claim reopens only that neighboring claim unless a control-structure input also changed. Update the affected locus, demote full view use to a note or orientation, narrow use, or reopen the control-structure question; unrelated structures and claims stay closed.

### C.30.LCA:5 - Archetypal Grounding

| Archetype | Without C.30.LCA | With C.30.LCA |
|---|---|---|
| System | A plant, controller, or supervisor diagram is treated as if the drawing itself established the controlled system's behavior. | The controlled system, controller, observer, planner, supervisor, boundaries, rate bands, actual control relations, and selected control structure remain separately recoverable. |
| Episteme | A control-description publication is read as structure, `U.View`, or proof because it uses familiar control labels. | The exact description episteme has one selected-structure EntityOfConcern; it is a view only through exact E.17.0 conformance. Representation, publication, and proof-like claims stay separate. |

### C.30.LCA:6 - Bias-Annotation

* **Diagram authority bias.** A neat feedback diagram can look more persuasive than the structure, source-to-use path, work-reliance relation, or claim it actually supports. Repair by naming each object or relation and the pattern used to state or test the claim.
* **Stratification-label bias.** A `layer`, `level`, `tier`, or `stack` label can hide whether it names a control relation, rate band, aggregation, scale, organization, Work scope, evidence scope, deployment, or publication section. Repair with `C.30.STRAT`; C.30.LCA applies only to the recovered control-specific case.
* **Supervisor anthropomorphism.** A supervisor label can make an episteme, policy, assignment, or dashboard sound agentive. Repair by recovering the supervision relation first. If action is claimed, recover the exact performer System through A.13 and admit the dated Work and enacted Method independently through A.15.1. Add assignment and F.6 only for an expressly consumed precise assignment-bound attribution; recover authority, responsibility, gate, safety, and evidence separately.
* **Transformation-flow and LCA conflation.** A transformation-flow graph expression and a control description or view can inform each other, but neither replaces the other. Repair by naming the EntityOfConcern, structure kind, and direct relations for each.

This checklist verifies the preceding guidance after the practitioner has chosen the selected repair action; it is not a required project control form and not a substitute for the note, description episteme, conformance occurrence, direct control relation, or repair guidance above.

### C.30.LCA:7 - Conformance Checklist

| ID | Check | Why it matters |
|---|---|---|
| CC-LCA-1 | A conforming full description or view has one C.2.1 identity whose EntityOfConcern is one exact selected control structure; the described and controlled holons and any actual `ArchitectureRelation` remain separately recoverable. | Prevents a free-floating diagram, claim, or unspecified relation set from becoming structure or episteme identity. |
| CC-LCA-2 | A conforming use records the direct control relations and participant meanings present: for example, reference provision, regulation or control, observation or estimation, plant or controlled-holon participation, or supervision. Systems, classifications, assignments, Methods, Work, and F.6 attribution are separate optional facts. | Keeps the view tied to actual control relations and their participants. |
| CC-LCA-3 | `Layer`, `level`, `tier`, or `stack` wording enters only with a recovered direct control relation, inter-layer relation, rate band, or `B.2.5` supervisor-subholon relation. An assignment alone is insufficient. | Prevents generic stratification wording from standing in for control structure. |
| CC-LCA-4 | A claimed `U.View` names the exact viewpoint episteme and independently obtaining `EpistemeViewpointConformanceRelation`; bundle membership, viewpoint label, authoring, query, diagram, and publication are insufficient. | Keeps structural description and view membership distinct. |
| CC-LCA-5 | Use the relevant patterns to state or test stability, safety, dynamics, temporal-aspect or rate-band structure, authored temporal-claim adequacy, causal use, empirical grounding, evidence, gate, and assurance claims. | Prevents LCA-as-proof. |
| CC-LCA-6 | Use `B.2.5` only to state or test the supervisor-subholon feedback relation it defines. | Keeps a cited feedback relation distinct from stability, safety, evidence, gate, and assurance claims. |
| CC-LCA-7 | Use E.18 to identify and test any transformation-flow path slice used by the control view. The slice is not the control structure or actual transformation itself. | Keeps transformation-flow and LCA relations distinct. |
| CC-LCA-8 | Use C.29 for the mathematical-lens portion of cross-domain transfer, prediction, reusable explanation, or assurance input when that lens changes the use. | Preserves mathematical-lens use and representation boundaries. |
| CC-LCA-9 | The record states admissible use, non-admissible use, and a source-return condition when the intended use relies on hidden source-side distinctions; representation, E.24.PUB publication occurrence, publication form, and carrier remain separate. | Prevents narrowed recognition or publication from becoming unchecked reliance. |

### C.30.LCA:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| LCA-as-proof | The text says the control stack proves safety, stability, or gate readiness. | Keep the control view and use the relevant dynamics, evidence, assurance, gate, or safety pattern for each proof or claim named by value. |
| Control-layer-as-generic-level | `Layer`, `level`, `tier`, or `stack` is used without a direct control relation, inter-layer relation, rate band, or `B.2.5` supervisor-subholon relation. | Apply `C.30.STRAT`; use C.30.LCA only after a control-specific relation is recovered. |
| Agentive episteme, kind, or assignment | A policy, model, dashboard, local system-role kind, assignment, or architecture note is said to watch, decide, plan, or adapt. | Recover the direct control relation and participant meanings. For actual action, recover the exact performer through A.13 and admit the `U.Work` occurrence independently through A.15.1. Add assignment and F.6 only when precise assignment-bound attribution is expressly consumed; keep publication, source-to-use, work-reliance, authority, responsibility, gate, safety, and evidence relations separate. |
| Transformation-flow and LCA substitution | A transformation-flow graph expression is treated as control architecture, or an LCA diagram is treated as the transformation-flow graph expression. | Recover both exact selected structures and description epistemes separately; use E.17.0 only for actual viewpoint conformance. |
| Hidden rate claim | Multi-rate control is named, but rate adequacy is not checked. | Add `rateSeparationClaimRefs?`; use `C.27.TA` for temporal-aspect or rate-band claims and `C.27` for authored temporal-claim adequacy. |

### C.30.LCA:9 - Consequences

The gain is a small, usable control-structure output that preserves common architecture language while blocking structure, view, and proof overread. Practitioners can still say `controller`, `plant`, `supervisor`, `feedback`, and `control layer`, but the record shows the selected structure, the boundary between description and view, and the direct relations those words carry; generic stratification labels use `C.30.STRAT` first.

The cost is an extra relation or conformance note before downstream reliance. When the claim is only recognition, that cost is small. When it is view membership, safety, stability, evidence, assurance, or gate passage, the cost is appropriate because none was carried by the diagram alone.

### C.30.LCA:10 - Rationale

Control architecture is too important to leave to diagram authority and too useful to remove from architecture language. The FPF move is to keep the practice cue and recover control-structure content first: selected structure, controlled holon, actual architecture relation when current, direct control relations and participant meanings, recovered rate or control-layer labels, observation and actuation boundaries, externality boundaries, and next admissible move. Systems, classifications, assignments, Methods, Work, and F.6 attribution are added independently; use their own patterns for authority, responsibility, gate, safety, stability, and evidence. The full record is one description episteme and, only through E.17.0 conformance, the same episteme as `U.View`. It can cite `C.30.STRAT`, `B.2.5`, E.18 transformation-flow structure, dynamics, `C.27.TA`, `C.27`, `C.28`, evidence, assurance, gates, and C.29, but does not absorb their claim kinds.

This protects subject, structure, episteme, View, representation, and publication boundaries. Several descriptions may have the same selected control structure as EntityOfConcern, and one description may be published repeatedly without changing identity, creating the structure, granting view membership, or making direct relations obtain.

### C.30.LCA:11 - SoTA-Echoing

| SoTA and practice source | What it contributes | FPF adoption stance | Practitioner implication |
| --- | --- | --- | --- |
| Anderson, Doyle, Low, and Matni, "System Level Synthesis" (Annual Reviews in Control, 2019). | Structured controller-synthesis practice treats closed-loop responses, constraints, locality, and distributed implementation as explicit synthesis variables and implementation relations rather than as a box-and-arrow guarantee. | Adopt and adapt: use SLS as current control-structure pressure for explicit control-participant meanings, direct relations, locality, rate, and implementation boundaries; do not import SLS proof claims into C.30.LCA. | A distributed-control diagram can start a control-structure description; for stability or robust-performance claims, use the relevant dynamics or control-proof pattern. |
| Ames, Coogan, Egerstedt, Notomista, Sreenath, and Tabuada, "Control Barrier Functions: Theory and Applications" (ECC, 2019). | Safety-critical control separates a controller structure from a safety property and the mathematical certificate or enforcement method used for that property. | Adopt and adapt: keep safety wording visible as a neighboring safety or proof claim, not as control-view adequacy. | When a sentence says the supervisor or controller makes the plant safe, keep the control description and use the relevant safety, dynamics, evidence, or assurance pattern to state and test that claim. |
| Rawlings, Mayne, and Diehl, *Model Predictive Control: Theory, Computation, and Design*, 2nd ed. (2017). | Planner and regulator distinctions, receding horizon, constraint, update period, and model-boundary distinctions are current MPC structure cues. | Adopt as control vocabulary: recover direct control relations and participant meanings, rates, model boundaries, and constraints; add Systems, classifications, assignments, Methods, and Work only when independently current. Handle temporal or rate claims under `C.27.TA`, authored temporal adequacy under `C.27`, and dynamics under `A.3.3`. | A multi-rate or MPC-style note names relation participants, rate bands, and model boundaries before claiming adequacy. |
| Leveson and Thomas, *STPA Handbook* (2018), as systems-theoretic safety-control practice. | Safety analysis treats unsafe control actions, feedback, process models, constraints, and losses as control-structure-relevant distinctions. | Adopt and adapt: allow safety-loss control-structure notes, while keeping safety-case verdicts and evidence sufficiency outside C.30.LCA. | A loss-control diagram can organize the description; it does not close the safety case. |
| FPF `C.2.1`, `A.22`, `C.30`, `C.30.AD`, `E.17.0`, and `C.30.ASV`. | These patterns separate selected control structure, architecture relation, architecture claim, description episteme, viewpoint episteme, conformance occurrence, described holon, and controlled holon. | Bind `ControlStructureView` to one selected `U.Structure` and viewpoint conformance; recover every control relation through the pattern that defines it. | A control view can coordinate several relations without becoming the architecture, relation occurrence, or proof. |

### C.30.LCA:12 - Relations

* Builds on `C.30` for direct architecture relations and selected-structure adequacy, `C.30.AD` for description identity and use, `E.17.0` for direct viewpoint conformance, and `C.30.ASV` for structural-view adequacy.
* Uses `A.22` for exact structure identity and structure-kind discipline.
* Coordinates with `C.30.STRAT` when layer, level, tier, stack, ladder, rung, block, expert, cache, router, gate, or similar source labels must be recovered before control-specific use.
* Coordinates with `B.2.5` for supervisor-subholon feedback relation recognition.
* Coordinates with E.18 and C.30.TFS-REL when transformation-flow path slices supply structure input to the control view; use E.18.2 for a mathematical description when that description is current.
* For neighboring claims, use `A.3.3` for dynamics or stability, `C.27.TA` for temporal-aspect or rate-band structure, `C.27` for authored temporal-claim adequacy, `C.28` for causal use, A.10 for bounded source-to-use reliance, G.6 for citable provenance paths, B.3 only for a named assurance claim, A.20 for internal-constraint validity, A.21 for gate decisions, A.15 for Work alignment, A.15.6 for project-Work recovery, E.24.PUB for publication, and C.29 for representation or transferable mathematical-lens use.

Use C.30.LCA only for the control-structure description or view-adequacy question at issue.

### C.30.LCA:End

