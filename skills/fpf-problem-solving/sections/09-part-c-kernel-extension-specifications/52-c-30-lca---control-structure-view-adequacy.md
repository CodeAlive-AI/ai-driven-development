## C.30.LCA - Control Structure View Adequacy (LCA)

> **Type:** Architectural subpattern under `C.30`
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.30.LCA:1 - Problem frame

Use this pattern when a selected control structure or control-structure relation changes the next architecture move: a controller regulates a plant, an observer or estimator changes what can be known, a planner provides references to lower-rate control, a supervisor constrains a subsystem, a policy loop changes allowed behavior, or an LCA cue makes roles, rates, observation boundaries, actuation boundaries, feedback, or externalities architecture-relevant.

The first-minute working situation is ordinary engineering talk: a diagram says the supervisor watches a subsystem, a controller regulates a plant, an observer estimates state, a planner gives references to a lower-rate controller, or a policy relation or control relation changes allowed controller behavior. The useful first move is to recover a `ControlStructureView@Context`: which architecture claim is being described, which control roles and relations are present, which rate bands or recovered control-layer relations are being claimed, which feedback or externality boundaries are named, and which governing pattern carries any additional claim being made. If the source only says `layer`, `level`, `tier`, or `stack` without a control-specific relation, use `C.30.STRAT` first.

What goes wrong if C.30.LCA is missed: a control diagram becomes proof; stratification labels bypass `C.30.STRAT` and start carrying undeclared scope; and `B.2.5`, `E.18` transformation-flow-structure prose, or Layered Control Architecture (LCA) prose is overread as control adequacy.

What C.30.LCA buys in practice: the practitioner can keep useful controller, plant, observer, regulator, supervisor, feedback, rate, and control-layer language while recovering the control-structure view and the governing pattern that carries any proof or claim named by value.

Not this pattern when the issue under repair is generic stratification or source-label repair, only an `E.18` transformation-flow path slice, function description, module boundary, measurement head, causal intervention, or safety case. Use `C.30.STRAT`, `C.30.TFS-REL`, `A.6.F`, `A.6.M`, `C.16`, `C.28`, or the assurance or evidence pattern governing the claim as appropriate.

The primary `EntityOfConcern` for this pattern use is the selected control structure or control-structure relation set under an `ArchitectureOf@Context`. The `ControlStructureView@Context` is a describing episteme for that selected structure; proof, safety, evidence, gate, and architecture-as-whole claims remain claim named by value refs governed by their governing patterns. Ordinary use may stop with a typed control-structure view note:

```text
ControlStructureViewNote ordinary minimum:
  architecture claim or described holon plus context:
  one control relation:
  loop state: closed | one-way | unclear:
  control-layer or rate label recovered?: yes | no | C.30.STRAT needed:
  governing pattern for proof, evidence, causal, gate, or assurance claim, if that claim is being made:
  stop condition:
```

The full `ControlStructureView@Context` is used when the control claim being made needs declared roles, relations, rates, recovered control-layer labels, boundary refs, or explicit governing-pattern applications beyond that note.

### C.30.LCA:2 - Problem

Control diagrams are persuasive because they look operational: arrows imply feedback, boxes imply responsibility, and recovered control-layer labels imply separation. In practice that is often enough for orientation, but not enough to make the architecture claim admissible. A control-stack description can quietly overclaim that stability, safety, evidence sufficiency, gate validity, assurance, or causality has already been established; a non-control `layer`, `level`, `tier`, or `stack` label belongs first to `C.30.STRAT`, not to C.30.LCA.

FPF needs a pattern that preserves the useful recognition of control architecture without letting the recognition cue become a proof. The control roles, feedback relations, externality boundaries, and rate separations belong in an architecture structural view. Claims about dynamics, temporal aspects, authored temporal-claim adequacy, causal use, evidence, assurance, gates, or mathematical lens transfer belong in the governing pattern that governs that claim kind.

### C.30.LCA:3 - Forces

* Control talk is useful and current engineering practice uses it, so deleting it would make architecture prose less usable.
* The same source labels can name different things. C.30.LCA applies only to recovered control-layer, rate-band, control-relation, bounded-context, and `B.2.5` supervisor-subholon uses; other `layer`, `level`, `tier`, or `stack` uses are recovered with `C.30.STRAT` and then governed by their governing patterns when those claims are being made.
* Layered and multi-rate control descriptions often need timing and dynamics claim before they can carry stability or safety claims.
* `B.2.5` already gives FPF a supervisor-subholon feedback relation, but it does not turn every feedback or loop diagram into proof.
* `E.18` `TransformationFlowStructure` values and their mathematical graph descriptions can describe flow, path, crossing, or transformation-flow relations that participate in control, but the transformation-flow description or graph expression is still a description or view, not the control structure itself.
* Practitioners need one small first output; dynamics, C.29, evidence, assurance, and gate records are used only when the question under repair calls for that governing pattern use.

### C.30.LCA:4 - Solution

Treat LCA-like material as a control-structure view under `C.30`. Recover the described architecture claim, the selected control structure or control-structure relation set, the control roles, the control relations, the relevant rate bands or recovered control-layer labels, and the boundary refs that make the view checkable. If the source label is not yet control-specific, apply `C.30.STRAT` before applying C.30.LCA to the case. Then state the admissible use and the non-admissible overread.

The ordinary minimum may stop with a compact `ControlStructureViewNote`:

```text
ControlStructureViewNote:
  architecture claim or described holon plus context:
  selected control structure or relation:
  one control relation:
  loop state: closed | one-way | unclear:
  control-layer or rate label recovered?: yes | no | C.30.STRAT needed:
  boundary refs used?: observation | actuation | feedback | externality | not used:
  governing pattern for proof, evidence, causal, gate, or assurance claim, if that claim is being made:
  admissibleUse:
  nonAdmissibleUse:
  stop condition:
```

Use `rateBandRefs?`, `controlLayerRefs?`, and `externalityBoundaryRefs?` only when rate, recovered control-layer, or externality wording carries a control-structure claim being made. Otherwise the ordinary note may stop after one control relation, loop state, and the proof-governing pattern application named by value if that claim is being made. Generic stratification labels stay with `C.30.STRAT` until recovered.

When a recovered control-layer relation is used to justify decomposition, substitution, or design reliance, recover the inter-layer assumption-guarantee relation or mark the control-layer relation as orientation only. `interLayerControlRelationRefs?` is used only when the relation is already control-specific and is used for decomposition, substitution, design reliance, safety, or stability claim kinds.

```text
InterLayerControlRelationNote:
  upperLayerAssumptionRefs:
  lowerLayerGuaranteeRefs:
  observationRequirementRefs:
  actuationAuthorityRefs:
  latencyOrRateEnvelopeRefs:
  violationFallbackRefs:
  admissibleUse:
  nonAdmissibleUse:
```

Use this note only when a recovered control-layer relation is used for decomposition, substitution, safety or stability claim, or architecture decision claim. It is not proof. Otherwise keep C.30.LCA at the small note or ordinary view form, or return the source label to `C.30.STRAT`.

```text
ControlStructureView@Context ::= {
  architectureClaimRef : ArchitectureOf@ContextRef,
  descriptionContext   : DescriptionContext(
    EntityOfConcernRef = selectedControlStructureEntityOfConcernRef,
    BoundedContextRef = ArchitectureOf@Context.boundedContextRef,
    ViewpointRef = viewpointRef
  ),
  selectedControlStructureEntityOfConcernRef :
    U.StructureRef | FinSet(QualifiedRelationRecordRef),
  viewpointRef (= descriptionContext.ViewpointRef),
  structureKindRef = ControlStructure,

  controlRoleRefs : FinSet(PlannerRef | RegulatorRef | ControllerRef |
                           ObserverEstimatorRef | PlantProcessRef | SupervisorRef),
  controlRelationRefs       : FinSet(QualifiedRelationRecordRef),
  controlLayerRefs?         : FinSet(ControlLayerRef),
  rateBandRefs?             : FinSet(RateBandRef),
  interLayerControlRelationRefs? : FinSet(InterLayerControlRelationRef(
    assumptionRefs,
    guaranteeRefs,
    allowedControlActionRefs,
    observationRequirementRefs,
    actuationAuthorityRefs,
    latencyOrRateEnvelopeRefs,
    violationFallbackRefs
  )),
  stratificationRepairRefs? : FinSet(C30STRATRepairRef),
  supervisorSubholonRelationRefs? : FinSet(B25SupervisorSubholonRelationRef),
  feedbackRelationRefs      : FinSet(QualifiedRelationRecordRef),
  observationBoundaryRefs?  : FinSet(BoundaryRef),
  actuationBoundaryRefs?    : FinSet(BoundaryRef),
  externalityBoundaryRefs?  : FinSet(BoundaryRef),
  controlledHolonRefs?     : FinSet(U.HolonRef),

  rateSeparationClaimRefs? : FinSet(C27TemporalClaimRef | TemporalAdequacyClaimRef),
  dynamicsClaimRefs?       : FinSet(A3_3DynamicsRef),
  gateDecisionRefs?          : FinSet(A20ConstraintValidityRef | A21GateDecisionRef),
  transformationFlowPathSliceRefs? : FinSet(PathSliceId),
  stabilityClaimRefs?    : FinSet(DynamicsRef | StabilityEvidenceRef),
  evidenceClaimRefs?     : FinSet(A10EvidenceGraphRef | G6EvidenceRef),
  assuranceClaimRefs?    : FinSet(B3AssuranceRef),
  causalUseClaimRefs?    : FinSet(C28ApplicationRef),
  scaleAuditRef?           : ArchitectureScaleAuditRecordRef,
  MathLensUseOutputRefs?           : FinSet(MathLensUseOutputRef),

  admissibleUse,
  nonAdmissibleUse,
  sourceReturnCondition
}
```

`DescriptionContext.EntityOfConcernRef` names the selected control structure or control-structure relation set represented by `selectedControlStructureEntityOfConcernRef`. `architectureClaimRef` names the enclosing architecture claim and supplies the bounded context and described holon; it is not the EntityOfConcern of the control-structure view itself.

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

**Control-specific stratification gate.** `Layer`, `level`, `tier`, and `stack` enter C.30.LCA only after `C.30.STRAT` or the local sentence recovers a control-specific item: `controlLayerRef`, `controlRoleRef`, `controlRelationRef`, `interLayerControlRelationRef`, `rateBandRef`, bounded context, and, where the supervisor-subholon relation is being claimed, `B.2.5` supervisor-subholon relation. Generic system level, aggregation scope, organization level, work or evidence scope, scale window, coarse-graining, deployment tier, and publication section do not stay in C.30.LCA. A layer label is not a control structure, not a system level, not a rate band, and not evidence of separation by itself.

**B.2.5 boundary.** `B.2.5` remains the owner for the supervisor-subholon feedback relation. `C.30.LCA` can cite a `B.2.5` relation when a supervisor-subholon relation is part of the control view. Loop wording stays in C.30.LCA only when the current control view explicitly recovers a control-loop or dynamics claim under its direct owner. `C.30.LCA` does not use `B.2.5` prose as proof of stability, safety, causality, evidence sufficiency, gate validity, or assurance. If an episteme appears in a control example, name the acting system in the relevant role, the A.3.4 transformer-position only when a transformation claim is current, and any publication, review record, publication relation, source relation, or reliance relation. An episteme does not sense, judge, plan, adapt, or act as an agent.

**Transformation-flow boundary.** An `E.18` transformation-flow path slice may supply flow-structure, path, crossing, or transformation-flow-structure input to the control view when that relation is being used. The transformation-flow graph expression remains a mathematical description or view of transformation-flow structure. It does not become the functional architecture, the control structure, or proof of control adequacy.

**C.29 boundary.** LCA may be an accepted local control-theory description in one context and a transferable mathematical lens in another. When transfer, prediction, assurance input, or reusable cross-domain explanation is being claimed, use `MathLensUse.FullCard` or at least `MathLensUse.MiniCard`. Dynamics, temporal aspects or rate bands, authored temporal-claim adequacy, and causal claims are still assigned to `A.3.3`, `C.27.TA`, `C.27`, and `C.28`.

**Nesting and scale rule.** If a control-structure view nests without a local depth limit, the record uses `scaleAuditRef?` when the nesting affects latency, stability, observability, accountability, or assurance.

**Worked slice A - LCA diagram used as proof.** A safety note says: `The Layered Control Architecture proves the plant is safe because the supervisor monitors the lower controller.` A conforming repair keeps the control-structure view and names planner, controller, plant, and supervisor relations, observation and actuation boundaries, and any rate bands. Safety and assurance claims use `B.3`, evidence to `A.10` or `G.6`, temporal-aspect and rate-band claims to `C.27.TA`, authored temporal-claim adequacy to `C.27`, and dynamics or stability claims use `A.3.3` or the appropriate dynamics claim.

**Worked slice B - multi-rate controller.** A source says a control stack has a slow planner, a faster regulator, and an observer with a different update period. Apply `C.30.LCA` to the case only after the stack label has been recovered as control roles, relations, and rate bands; otherwise the label is recovered first by `C.30.STRAT`. C.30.LCA does not claim rate adequacy. If the rate relation matters for oscillation, latency, stability, or safety, the next admissible use is `C.27.TA` for temporal aspect or rate-band structure, plus `C.27` only when an authored temporal-claim adequacy question is under repair, and the dynamics or assurance pattern named by value when that claim kind is being made.

**Worked slice C - supervisor-subholon loop.** A subsystem is supervised by an external controller that changes allowed modes. `C.30.LCA` records the supervisor-subholon relation and may reference `B.2.5`. If the text claims that this loop authorizes work, passes a gate, or proves a policy constraint, the claim uses `A.15`, `A.20`, or `A.21`.

### C.30.LCA:5 - Archetypal Grounding

| Archetype | Without C.30.LCA | With C.30.LCA |
|---|---|---|
| System | A plant, controller, or supervisor diagram is treated as if the drawing itself established the controlled system's behavior. | The controlled system, controller, observer, planner, supervisor, boundaries, and rate bands are recorded as a view of control structure. |
| Episteme | A control-description publication is read as proof because it uses familiar control labels. | The publication is treated as a description or view; proof-like claim kinds are governed by the pattern for that claim kind. |

### C.30.LCA:6 - Bias-Annotation

* **Diagram authority bias.** A neat feedback diagram can look more persuasive than the source relation, reliance relation, or claim pattern it actually uses. Repair by naming that relation named by value and the governing pattern that carries the claim kind being made.
* **Stratification-label bias.** A `layer`, `level`, `tier`, or `stack` label can hide whether it names a control relation, rate band, aggregation, scale, organization, work scope or evidence scope, deployment, or publication section. Repair with `C.30.STRAT`; C.30.LCA applies only to the recovered control-specific case.
* **Supervisor anthropomorphism.** A supervisor label can make an episteme, policy, or dashboard sound agentive. Repair by naming the acting system in role, the method it enacts when current, and the work or review practice when current.
* **Transformation-flow and LCA conflation.** A transformation-flow graph expression and a control view can inform each other, but neither replaces the other. Repair by naming the description context and structure kind for each view.

This checklist verifies the preceding guidance after the practitioner has chosen the selected repair action; it is not a required project control form and not a substitute for the card, note, view, relation, or repair guidance above.

### C.30.LCA:7 - Conformance Checklist

| ID | Check | Why it matters |
|---|---|---|
| CC-LCA-1 | A conforming use names the `ArchitectureOf@Context` or recoverable described holon and bounded context whose control structure is being viewed. | Prevents free-floating control diagrams. |
| CC-LCA-2 | A conforming use records control roles and relations: planner, regulator or controller, observer or estimator, plant or controlled system, supervisor, or the local subset actually present. | Keeps the view action-guiding. |
| CC-LCA-3 | A conforming use recovers `layer`, `level`, `tier`, or `stack` wording with `C.30.STRAT` unless the text already recovers a control-specific `controlLayerRef`, `controlRelationRef`, `interLayerControlRelationRef`, `rateBandRef`, bounded context, or `B.2.5` supervisor-subholon relation. | Prevents pseudo-level or pseudo-layer overread inside C.30.LCA. |
| CC-LCA-4 | A conforming use records observation, actuation, feedback, and externality boundaries when they are used in the view. | Makes the control relation inspectable. |
| CC-LCA-5 | Stability, safety, dynamics, temporal-aspect or rate-band structure, authored temporal-claim adequacy, causal use, evidence, gate, and assurance claims are assigned to their governing patterns. | Prevents LCA-as-proof. |
| CC-LCA-6 | `B.2.5` is used only as a supervisor-subholon feedback relation, not as proof of stability, safety, evidence, gate validity, or assurance. Loop claims use the control or dynamics owner named by value. | Keeps existing FPF control relation bounded. |
| CC-LCA-7 | An `E.18` transformation-flow path slice used by the control view remains a transformation-flow description or relation governed by E.18, not the control structure itself. | Keeps transformation-flow and LCA relations distinct. |
| CC-LCA-8 | A C.29 or mathematical-lens use is opened when LCA is transferred across domains or used for prediction, reusable explanation, or assurance input. | Preserves mathematical-lens use. |
| CC-LCA-9 | The record states admissible use, non-admissible use, and source-return condition. | Prevents narrowed recognition from becoming unchecked reliance. |

### C.30.LCA:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| LCA-as-proof | The text says the control stack proves safety, stability, or gate readiness. | Keep the control view and assign proof or claim named by values to dynamics, evidence, assurance, gate, or safety patterns. |
| Control-layer-as-generic-level | `Layer`, `level`, `tier`, or `stack` is used without a recovered control role, relation, rate band, bounded context, or `B.2.5` supervisor-subholon relation. | Apply `C.30.STRAT`; return to C.30.LCA only for a recovered control-layer or control-relation case. |
| Agentive episteme | A policy, model, dashboard, or architecture note is said to watch, decide, plan, or adapt. | Name the acting system in role, the method it enacts when current, the work or review practice when current, and any publication relation, source relation, or reliance relation. |
| Transformation-flow and LCA substitution | A transformation-flow graph expression is treated as the control architecture, or an LCA diagram is treated as the transformation-flow graph expression. | Use `DescriptionContext` and structure kind fields to keep views distinct. |
| Hidden rate claim | Multi-rate control is named, but rate adequacy is not checked. | Add `rateSeparationClaimRefs?`; assign temporal-aspect or rate-band claims to `C.27.TA` and authored temporal-claim adequacy to `C.27`. |

### C.30.LCA:9 - Consequences

The gain is a small, usable control-structure output that preserves common architecture language while blocking proof overread. Practitioners can still say `controller`, `plant`, `supervisor`, `feedback`, and `control layer`, but the record shows what those words carry; generic stratification labels use `C.30.STRAT` before they are allowed to enter this pattern.

The cost is an extra relation note before downstream reliance. When the claim being made is only recognition, that cost is small. When the claim being made is safety, stability, evidence, assurance, or gate passage, the cost is appropriate because those claims were never carried by the diagram alone.

### C.30.LCA:10 - Rationale

Control architecture is too important to leave to diagram authority and too useful to remove from architecture language. The FPF move is to keep the practice cue and recover the control-structure content first: controlled holon or architecture claim, control roles, control relations, recovered rate or control-layer labels, observation and actuation boundaries, externality boundaries, and the next admissible control-architecture move. The record may be a Description episteme or episteme-lane view, possibly admitted for specification use, but that is the record lane for the control-structure move, not the center of the pattern. It can cite `C.30.STRAT`, `B.2.5`, `E.18` transformation-flow structure, dynamics, `C.27.TA`, `C.27`, `C.28`, evidence, assurance, gates, and `C.29`, but it does not absorb their claim kinds.

This also protects the architecture ontology's EntityOfConcern and Description-episteme boundary plus specification-use discipline. The architecture-relevant EntityOfConcern is the selected control structure under `ArchitectureOf@Context`; the LCA diagram or control note is an architecture description or view when description or view use is being made. Several descriptions may describe the same control structure, and one description may be published without becoming the structure it describes.

### C.30.LCA:11 - SoTA-Echoing

| SoTA and practice source | What it contributes | FPF adoption stance | Practitioner implication |
| --- | --- | --- | --- |
| Anderson, Doyle, Low, and Matni, "System Level Synthesis" (Annual Reviews in Control, 2019). | Structured controller-synthesis practice treats closed-loop responses, constraints, locality, and distributed implementation as explicit synthesis variables and implementation relations rather than as a box-and-arrow guarantee. | Adopt and adapt: use SLS as current control-structure pressure for explicit role, relation, locality, rate, and implementation-boundary fields; do not import SLS proof claims into C.30.LCA. | A distributed-control diagram can start a control-structure view; stability or robust-performance claims are governed by dynamics or control proof patterns. |
| Ames, Coogan, Egerstedt, Notomista, Sreenath, and Tabuada, "Control Barrier Functions: Theory and Applications" (ECC, 2019). | Safety-critical control separates a controller structure from a safety property and the mathematical certificate or enforcement method used for that property. | Adopt and adapt: keep safety wording visible as a neighboring safety or proof claim, not as control-view adequacy. | When the sentence says the supervisor or controller makes the plant safe, keep the control view and assign the safety claim to the safety named by value, dynamics, evidence, or assurance pattern. |
| Rawlings, Mayne, and Diehl, *Model Predictive Control: Theory, Computation, and Design*, 2nd ed. (2017). | Planner or regulator, receding-horizon, constraint, update-period, and model-boundary distinctions are common current MPC structure cues. | Adopt as control vocabulary: recover roles, rates, model boundaries, and constraints; assign temporal-aspect or rate-band claims to `C.27.TA`, authored temporal-claim adequacy to `C.27`, and dynamics claims to `A.3.3` when those claims are being made. | A multi-rate or MPC-style note should name rate bands and model boundaries before it claims adequacy. |
| Leveson and Thomas, *STPA Handbook* (2018), as systems-theoretic safety-control practice. | Safety analysis treats unsafe control actions, feedback, process models, constraints, and losses as control-structure-relevant distinctions. | Adopt and adapt: allow safety-loss control-structure notes, while keeping safety-case verdicts and evidence sufficiency outside C.30.LCA. | A loss-control diagram can organize the view; it does not close the safety case. |
| ISO/IEC/IEEE 42010:2022 architecture-description practice. | Architecture descriptions use concerns, viewpoints, views, and correspondences, and several views may describe one architecture. | Adopt and adapt: bind `ControlStructureView@Context` to `DescriptionContext` and `ArchitectureOf@Context`. | A control view is a view under a declared concern, not the architecture itself. |

### C.30.LCA:12 - Relations

* Builds on `C.30` for grounded architecture and selected-structure adequacy and `C.30.ASV` for structural-view adequacy.
* Uses `A.22` for structure and structural-view kind discipline.
* Coordinates with `C.30.STRAT` when layer, level, tier, stack, ladder, rung, block, expert, cache, router, gate, or similar source labels must be recovered before any control-specific use enters C.30.LCA.
* Coordinates with `B.2.5` for supervisor-subholon feedback relation recognition.
* Coordinates with `E.18` and `C.30.TFS-REL` when transformation-flow path slices supply structure input to the control view.
* Applies `A.3.3` for dynamics and stability claims, `C.27.TA` for temporal-aspect or rate-band structure, `C.27` for authored temporal-claim adequacy, `C.28` for causal-use claims, `A.10` or `G.6` for evidence claim, `B.3` for assurance, `A.20` or `A.21` for constraint validity and gate decisions, `A.15` for work authority, and `C.29` when LCA is used as a transferable mathematical lens.

Neighboring claims stay with their governing patterns: `C.30.STRAT` for stratification and source-label precision restoration, `C.30` for grounded architecture and selected-structure adequacy, `C.30.ASV` for architecture structural-view adequacy, `B.2.5` for supervisor-subholon feedback relation, `E.18` for graph, path, and crossing discipline, `A.3.3` for dynamics claims, `C.27.TA` for temporal-aspect or rate-band structure, `C.27` for authored temporal-claim adequacy, `C.28` for causal use, `A.10` or `G.6` for evidence, `B.3` for assurance, `A.20` or `A.21` for gate and constraint-validity records, `A.15` for work, and `C.29` for mathematical-lens use. `C.30.LCA` governs only the control-structure view relation being claimed.

### C.30.LCA:End

