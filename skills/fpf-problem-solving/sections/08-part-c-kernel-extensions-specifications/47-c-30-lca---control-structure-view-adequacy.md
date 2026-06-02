## C.30.LCA - Control Structure View Adequacy (LCA)

> **Type:** Architectural subpattern under `C.30`
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.30.LCA:1 - Problem frame

Use this pattern when an architecture description uses a control-stack, supervisor-loop, controller/plant, planner/regulator, observer/estimator, feedback-loop, multi-rate control, or Layered Control Architecture cue to explain how a grounded holon is controlled, observed, regulated, supervised, or protected.

The first-minute working situation is ordinary engineering talk: a diagram says the supervisor watches a subsystem, a controller regulates a plant, an observer estimates state, a planner gives references to a lower-rate controller, or a policy/control relation changes allowed controller behavior. The useful first move is not to accept the diagram as proof. The useful first move is to recover a `ControlStructureView@Context`: which architecture claim is being described, which control roles and relations are present, which rates or declared control layers are live, which feedback or externality boundaries are named, and which exact governing FPF pattern carries any stability, safety, evidence, gate, causal, or assurance claim kind.

What goes wrong if C.30.LCA is missed: a control diagram becomes proof of stability, safety, causality, evidence sufficiency, gate validity, or assurance; layer and level labels start carrying undeclared scope; and `B.2.5`, Transduction Graph Architecture (TGA), or Layered Control Architecture (LCA) prose is overread as control adequacy.

What C.30.LCA buys in practice: the practitioner can keep useful controller, plant, observer, regulator, supervisor, feedback, rate, and control-layer language while recovering the control-structure view and the exact governing pattern that carries any proof or exact claim.

Not this pattern when the live issue is only a general TGA path slice, a function description, a module boundary, a measurement head, a causal intervention, or a safety case. Use `C.30.TGA-FLOW-REL` for flow/transduction structure relation, `A.6.F` for function wording repair, the exact module/interface repair pattern for module-interface structure, `C.16` or an admitted characteristic/measurement receiving pattern for measured characteristics, `C.28` for causal-use claims, and `B.3`/`A.10`/`G.6` for assurance or evidence claim.

The governed object is one control-structure view of `ArchitectureOf@Context`, not the controlled holon itself, not a proof, and not the architecture as a whole. Ordinary use may stop with a typed control-structure view note:

```text
ControlStructureViewNote ordinary minimum:
  architecture claim or described holon plus context:
  one control relation:
  loop posture: closed | one-way | unclear:
  layer or rate label live?: yes | no:
  proof, evidence, causal, gate, or assurance governing pattern if live:
  stop condition:
```

The full `ControlStructureView@Context` opens when the live control claim needs declared roles, relations, rates, control-layer labels, boundary refs, or explicit exact governing pattern applications beyond that note.

Use a `SafetyLossControlStructureNote` when safety wording is live but the practitioner first needs the architecture-side loss-control structure, not a safety-case verdict:

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
    A.3.3 dynamics, C.27 temporal or rate,
    C.28 causal-use, A.10/G.6 evidence,
    B.3 assurance, A.20/A.21 gate
  nonAdmissibleUse:
    not safety proof, not safety-case verdict, not regulatory acceptance
```

The note gives a positive first architecture move: find the loss-control structure, controlled process or plant, constraint, foreseeable misuse, operational design scope, and action-relevant boundary. It does not replace evidence, assurance, gate, causal, dynamics, or temporal support.



### C.30.LCA:2 - Problem

Control diagrams are persuasive because they look operational: arrows imply feedback, boxes imply responsibility, and layer labels imply separation. In practice that is often enough for orientation, but not enough to make the architecture claim admissible. A control-stack description can quietly overclaim that stability, safety, evidence sufficiency, gate validity, assurance, or causality has already been established.

FPF needs a pattern that preserves the useful recognition of control architecture without letting the recognition cue become a proof. The control roles, feedback relations, externality boundaries, and rate separations belong in an architecture structural view. Claims about dynamics, temporal adequacy, causal use, evidence, assurance, gates, or mathematical lens transfer belong in the exact governing pattern that governs that claim kind.

### C.30.LCA:3 - Forces

* Control talk is useful and current engineering practice uses it, so deleting it would make architecture prose less usable.
* The same labels can name different things: a control layer, a declared system level, a scale window, an organizational level, a work/evidence scope, or a publication grouping.
* Layered and multi-rate control descriptions often need timing and dynamics claim before they can carry stability or safety claims.
* `B.2.5` already gives FPF a supervisor-subholon feedback-loop pattern, but it does not turn every loop diagram into proof.
* TGA graphs can describe flow and transduction relations that participate in control, but the TGA graph is still a description or view, not the control structure itself.
* Practitioners need one small first output; dynamics, C.29, evidence, assurance, and gate records open only when the live question calls for that exact governing pattern use.

### C.30.LCA:4 - Solution

Treat LCA-like material as a control-structure view under `C.30`. Recover the described architecture claim, the control roles, the control relations, the relevant rate bands or declared control-layer labels, and the boundary refs that make the view checkable. Then state the admissible use and the non-admissible overread.

Use `rateBandRefs?`, `controlLayerRefs?`, and `externalityBoundaryRefs?` only when rate, control-layer, or externality wording carries a live claim. Otherwise the ordinary note may stop after one control relation, loop posture, any live layer or rate label, and the exact proof-governing pattern application if that claim is live.

When a layer relation is used to justify decomposition, substitution, or design reliance, recover the inter-layer assumption-guarantee relation or mark the layer relation as orientation only. `interLayerControlRelationRefs?` opens only when the layer relation is used for decomposition, substitution, design reliance, safety, or stability claim kinds.

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

Open this note only when a layer relation is used for decomposition, substitution, safety or stability claim, or architecture decision claim. It is not proof. Otherwise keep C.30.LCA at the small note or ordinary view form.



```text
ControlStructureView@Context ::= {
  architectureClaimRef : ArchitectureOf@ContextRef,
  descriptionContext   : DescriptionContext(
    DescribedEntityRef = architectureClaimRef,
    BoundedContextRef = ArchitectureOf@Context.boundedContextRef,
    ViewpointRef = viewpointRef
  ),
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
  declaredSystemLevelRefs?  : FinSet(SystemLevelRef),
  aggregationScopeRefs?     : FinSet(AggregationScopeRef),
  organizationLevelRefs?    : FinSet(OrganizationLevelRef),
  workEvidenceScopeRefs?    : FinSet(ScopeRef),
  scaleWindowRefs?          : FinSet(ScaleWindowRef),
  feedbackRelationRefs      : FinSet(QualifiedRelationRecordRef),
  observationBoundaryRefs?  : FinSet(BoundaryRef),
  actuationBoundaryRefs?    : FinSet(BoundaryRef),
  externalityBoundaryRefs?  : FinSet(BoundaryRef),
  controlledSystemRefs?     : FinSet(U.HolonRef),

  rateSeparationClaimRefs? : FinSet(C27TemporalClaimRef | TemporalAdequacyClaimRef),
  dynamicsClaimRefs?       : FinSet(A3_3DynamicsRef),
  gateDecisionRefs?          : FinSet(A20ConstraintValidityRef | A21GateDecisionRef),
  TGAPathSliceRefs?        : FinSet(PathSliceId),
  stabilityClaimRefs?    : FinSet(DynamicsRef | StabilityEvidenceRef),
  evidenceClaimRefs?     : FinSet(A10EvidenceGraphRef | G6EvidenceRef),
  assuranceClaimRefs?    : FinSet(B3AssuranceRef),
  causalUseClaimRefs?    : FinSet(C28ApplicationRef),
  scaleAuditRef?           : ArchitectureScaleAuditRecordRef,
  MLAOutputRefs?           : FinSet(MLAOutputRef),

  admissibleUse,
  nonAdmissibleUse,
  sourceReturnCondition
}
```

**Role reading.**

| Source label | FPF reading |
|---|---|
| Plant or controlled system | `U.System` whose state evolves; reusable state-evolution claims use `A.3.3`. |
| Regulator or controller | System in a control role enacting a method over observations and actuations. |
| Planner | Upstream role or method producing targets, plans, references, or allowed regions for regulators. |
| Observer or estimator | Role or method producing state estimates, observations, or evidence-facing readouts. |
| Supervisor | Role or method governing subordinate holons, gates, policy changes, or control-mode changes. |

**Layer, level, tier, stack, and rate rule.** `Control layer` may remain as an LCA source label only when the record names the control role, relation, rate band, and bounded context. When the source says layer, level, tier, or stack, recover exactly one or more of: `controlLayerRef`, `declaredSystemLevelRef`, `aggregationScopeRef`, `rateBandRef`, `organizationLevelRef`, `workEvidenceScopeRef`, `scaleWindowRef`, or `publicationSectionRef` when the wording only names a document layer. `System level` is not a synonym for control layer. Use it only for a declared system level or aggregation scope, with the relevant `B.2.5` supervisor-subholon relation or comparable declared relation recovered. A layer label is not a structure kind, not a system level, not a rate band, and not evidence of separation by itself. In renormalization, coarse-graining, or mathematical-lens use, prefer `scale`, `scale window`, `coarse-graining scale`, `coarse-graining step`, or `resolution` for the lens itself.

**B.2.5 boundary.** `B.2.5` remains the supervisor-subholon feedback-loop check pattern. `C.30.LCA` can cite a `B.2.5` relation when a supervisor-subholon loop is part of the control view. It does not use `B.2.5` prose as proof of stability, safety, causality, evidence sufficiency, gate validity, or assurance. If an episteme appears in a control example, the acting `Transformer`, publication or review practice, and publication or source/reliance relation are named; an episteme does not sense, judge, plan, adapt, or act as an agent.

**TGA boundary.** A TGA path slice may support the control view when flow or transduction relation is live. The TGA graph remains a description or view of flow/transduction structure. It does not become the functional architecture, the control structure, or proof of control adequacy.

**C.29 boundary.** LCA may be an accepted local control-theory description in one context and a transferable mathematical lens in another. When transfer, prediction, assurance input, or reusable cross-domain explanation is live, use `MLA.FullCard` or at least `MLA.MiniCard`. Dynamics, temporal adequacy, and causal claims are still assigned to `A.3.3`, `C.27`, and `C.28`.

**Nesting and scale rule.** If a control-structure view nests without a local depth limit, the record uses `scaleAuditRef?` when the nesting affects latency, stability, observability, accountability, or assurance.

**Worked slice A - LCA diagram used as proof.** A safety note says: `The Layered Control Architecture proves the plant is safe because the supervisor monitors the lower controller.` A conforming repair keeps the control-structure view and names planner/controller/plant/supervisor relations, observation and actuation boundaries, and any rate bands. Safety and assurance claims use `B.3`, evidence to `A.10` or `G.6`, temporal adequacy to `C.27`, and dynamics/stability claims use `A.3.3` or the appropriate dynamics claim.

**Worked slice B - multi-rate controller.** A control stack has a slow planner, a faster regulator, and an observer with a different update period. `C.30.LCA` records the roles, relations, and rate bands. It does not claim rate adequacy. If the rate relation matters for oscillation, latency, stability, or safety, the next admissible move is `C.27` plus dynamics or assurance claim as live.

**Worked slice C - supervisor-subholon loop.** A subsystem is supervised by an external controller that changes allowed modes. `C.30.LCA` records the supervisor-subholon relation and may reference `B.2.5`. If the text claims that this loop authorizes work, passes a gate, or proves a policy constraint, the claim uses `A.15`, `A.20`, or `A.21`.

### C.30.LCA:5 - Archetypal Grounding

| Archetype | Without C.30.LCA | With C.30.LCA |
|---|---|---|
| System | A plant/controller/supervisor diagram is treated as if the drawing itself established the controlled system's behavior. | The controlled system, controller, observer, planner, supervisor, boundaries, and rate bands are recorded as a view of control structure. |
| Episteme | A control-description publication is read as proof because it uses familiar control labels. | The publication is treated as a description or view; proof-like claim kinds move to the pattern that governs that claim kind. |

### C.30.LCA:6 - Bias-Annotation

* **Diagram authority bias.** A neat feedback diagram can look more persuasive than the source/reliance relation or claim pattern it actually uses. Repair by naming the source/reliance relation and the exact governing pattern that carries the live claim kind.
* **Layer label bias.** A layer label can hide whether it names a control role, aggregation scope, rate band, organization level, publication section, or scale window. Repair by recovering the declared field.
* **Supervisor anthropomorphism.** A supervisor label can make an episteme, policy, or dashboard sound agentive. Repair by naming the acting transformer, method, or work practice.
* **TGA/LCA conflation.** A flow graph and a control view can inform each other, but neither replaces the other. Repair by naming the description context and structure kind for each view.

This checklist verifies the preceding guidance after the practitioner has chosen the live move; it is not a required project control form and not a substitute for the card, note, view, relation, or repair move above.

### C.30.LCA:7 - Conformance Checklist


| ID | Check | Why it matters |
|---|---|---|
| CC-LCA-1 | A conforming use names the `ArchitectureOf@Context` or recoverable described holon and bounded context whose control structure is being viewed. | Prevents free-floating control diagrams. |
| CC-LCA-2 | A conforming use records control roles and relations: planner, regulator/controller, observer/estimator, plant or controlled system, supervisor, or the local subset actually present. | Keeps the view action-guiding. |
| CC-LCA-3 | A conforming use distinguishes control layer, declared system level, aggregation scope, rate band, organization level, work/evidence scope, and scale window when any of those labels carry a live claim. | Prevents pseudo-level or pseudo-layer overread. |
| CC-LCA-4 | A conforming use records observation, actuation, feedback, and externality boundaries when they are live in the view. | Makes the control relation inspectable. |
| CC-LCA-5 | Stability, safety, dynamics, temporal adequacy, causal use, evidence, gate, and assurance claims are assigned to their governing exact governing patterns. | Prevents LCA-as-proof. |
| CC-LCA-6 | `B.2.5` is used only as a supervisor-subholon feedback-loop relation or check pattern, not as proof of stability, safety, evidence, gate validity, or assurance. | Keeps existing FPF control relation bounded. |
| CC-LCA-7 | A TGA path slice used by the control view remains a flow/transduction description or relation to E.18, not the control structure itself. | Keeps TGA and LCA relations distinct. |
| CC-LCA-8 | A C.29 or mathematical-lens use is opened when LCA is transferred across domains or used for prediction, reusable explanation, or assurance input. | Preserves mathematical-lens adequacy. |
| CC-LCA-9 | The record states admissible use, non-admissible use, and source-return condition. | Prevents narrowed recognition from becoming unchecked reliance. |

### C.30.LCA:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| LCA-as-proof | The text says the control stack proves safety, stability, or gate readiness. | Keep the control view and assign proof or exact claims to dynamics, evidence, assurance, gate, or safety patterns. |
| Control-layer-as-system-level | `Layer`, `level`, `tier`, or `stack` is used without a declared role, relation, rate band, or scope. | Recover the exact field: control layer, declared system level, aggregation scope, rate band, organization level, work/evidence scope, or scale window. |
| Agentive episteme | A policy, model, dashboard, or architecture note is said to watch, decide, plan, or adapt. | Name the acting transformer, method, work practice, or publication or source/reliance relation. |
| TGA/LCA substitution | A TGA graph is treated as the control architecture, or an LCA diagram is treated as the flow graph. | Use `DescriptionContext` and structure kind fields to keep views distinct. |
| Hidden rate claim | Multi-rate control is named, but rate adequacy is not checked. | Add `rateSeparationClaimRefs?` and assign timing claims to `C.27`. |

### C.30.LCA:9 - Consequences

The gain is a small, usable control-structure output that preserves common architecture language while blocking proof overread. Practitioners can still say `controller`, `plant`, `supervisor`, `feedback`, and `control layer`, but the record shows what those words carry.

The cost is an extra relation note before downstream reliance. When the live claim is only recognition, that cost is small. When the live claim is safety, stability, evidence, assurance, or gate passage, the cost is appropriate because those claims were never carried by the diagram alone.

### C.30.LCA:10 - Rationale

Control architecture is too important to leave to diagram authority and too useful to remove from architecture language. The FPF move is to keep the practice cue and recover its kind: a control-structure view is a D/S record over selected architecture-relevant control structure. It can cite `B.2.5`, TGA, dynamics, C.27, C.28, evidence, assurance, gates, and C.29, but it does not absorb their claim kinds.

This also protects the architecture ontology's I/D/S distinction. The architecture is the selected structure under `ArchitectureOf@Context`; the LCA diagram or control note is an architecture description/view. Several descriptions may describe the same control structure, and one description may be published without becoming the structure it describes.

### C.30.LCA:11 - SoTA-Echoing

| SoTA/practice anchor | What it supports | FPF adoption stance | Practitioner implication |
|---|---|---|---|
| Layered and multi-rate control architecture practice, with Matni/Ames/Doyle used here as lineage and practice basis for quantitative layered multi-rate control rather than as current proof by itself. | Planner, controller/regulator, observer, plant, supervisor, rate separation, and feedback relations are recognizable control-structure-view content. | Adopt and adapt: use the practice vocabulary to start or check a control-structure view, then assign stability, safety, timing, evidence, assurance, and gate claims to their governing FPF patterns. | A control-stack diagram can start a view record; it cannot close stability, safety, or evidence review. |
| Feedback-control and cyber-physical systems practice. | Observation, actuation, plant dynamics, disturbances, and externality boundaries matter for control adequacy. | Adopt: keep boundary fields visible in the control view and assign dynamics/timing claims out. | If timing or plant behavior matters, open `C.27` or `A.3.3` instead of adding more claim force to the LCA sentence. |
| ISO/IEC/IEEE 42010 architecture-description practice. | Architecture descriptions use viewpoints and views over concerns, and several views may describe one architecture. | Adopt and adapt: bind `ControlStructureView@Context` to `DescriptionContext` and `ArchitectureOf@Context`. | A control view is a view under a declared concern, not the architecture itself. |
| FPF `B.2.5` supervisor-subholon feedback-loop material. | Supervisor-subholon relations are already useful FPF pattern material for feedback-loop recognition. | Reuse with boundary: cite `B.2.5` for the relation, not for proof. | A supervisor loop becomes inspectable without becoming evidence, assurance, or gate authority. |

### C.30.LCA:12 - Relations

* Builds on `C.30` for architecture-description adequacy and `C.30.ASV` for structural-view adequacy.
* Uses `A.22` for structure and structural-view kind discipline.
* Coordinates with `B.2.5` for supervisor-subholon feedback-loop recognition.
* Coordinates with `E.18` and `C.30.TGA-FLOW-REL` when flow/transduction path slices supply structure input to the control view.
* Applies `A.3.3` for dynamics and stability claims, `C.27` for temporal/rate adequacy, `C.28` for causal-use claims, `A.10`/`G.6` for evidence claim, `B.3` for assurance, `A.20`/`A.21` for constraint validity and gate decisions, `A.15` for work authority, and `C.29` when LCA is used as a transferable mathematical lens.

Does not replace: `C.30` architecture-description adequacy, `C.30.ASV` architecture structural-view adequacy, `B.2.5` supervisor-subholon feedback-loop discipline, `E.18` graph/path/crossing discipline, `A.3.3` dynamics claim, `C.27` temporal/rate adequacy, `C.28` causal-use claim, `A.10`/`G.6` evidence claim, `B.3` assurance, `A.20`/`A.21` gate and constraint-validity records, `A.15` work, or `C.29` mathematical-lens adequacy.

### C.30.LCA:End

