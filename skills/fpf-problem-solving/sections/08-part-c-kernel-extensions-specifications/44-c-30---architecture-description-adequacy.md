## C.30 - Architecture Description Adequacy (ADA)

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.30:1 - Problem frame

Use this pattern when architecture talk is doing more than naming modules, diagrams, documents, tool outputs, or a general engineering topic. Open C.30 when the live question is what architecture claim is being described, what selected structures carry it, what artifact role the current text or model has, and what the next admissible architecture move is.

The ordinary first output is intentionally small:

```text
ArchitectureQuestionCard@Project:
  describedHolonRef:
  boundedContextRef:
  liveArchitectureConcernCue:
  claimPosture:
    preClaimCue | problemCardReady | architectureClaimReady | nonArchitectureClaimReady
  plainPromptLabel?:
  activeStructureKindRefs: FinSet(ArchitectureStructureKindRef)
  currentCollapseCue:
  firstArchitectureMove:
  ordinaryNotThisPatternBoundary:
  governingPatternApplicationRefs:
```

Use `ArchitectureConcernCue` only to recognize the architecture problem family that chooses the first structure kind and architecture move:

```text
ArchitectureConcernCue:
  changeLocalization | substitutionOrReplacement | flowBottleneck |
  controlOrRateMismatch | dataCustodyOrStateResidence |
  physicalSeparationOrPlacement | evidenceReuseOrAssuranceReuse |
  scaleWindowOrCoarseningLoss | runtimeFailureMode |
  crossScopeResidual | descriptionViewLoss | otherDeclared
```

Typical architecture problem cues:

```text
changeLocalizationFailure
substitutionFailure
crossViewMismatch
flowBottleneckOrHiddenCrossing
controlRateOrLayerMismatch
dataCustodyOrStateResidenceUnclear
placementOrJurisdictionMismatch
evidenceReuseFailure
sourceReturnNeeded
crossScopeResidual
generatedViewLoss
```

Use the cue only to choose the first architecture move. The cue is not a quality score, failure proof, risk rating, gate result, or decision.

Do not treat the cue as a quality, measure, risk score, decision, or free `ArchitectureConcern` ontology. If the concern cannot yet name described holon, bounded context, one candidate structure kind, and one admissible next architecture move, keep it as a concern cue or `ProblemCard@Context`-style issue; do not promote it to `ArchitectureOf@Context` by wording alone. ISO 42010-style concern language may remain as lineage or project wording, but C.30 recovers the FPF carrier as `liveArchitectureConcernCue`, `governingArchitectureConcernRefs?`, or `architectureConcernNotes?`.

This is a project-side triage aid, not `U.Architecture`, not evidence, not a decision, and not a mandatory publication.
The action palette for `firstArchitectureMove` is deliberately short:

- name or narrow the described holon and bounded context;
- choose the live structure kind;
- downgrade an artifact to publication, diagram, carrier, source-relation object, or generated relation graph when it is not a D/S view;
- repair a collapsed function, module, flow, control, interface, or signature claim;
- open a minimal architecture structural view only when it changes the next move;
- assign C.29, A.10, B.3, A.20, A.21, C.28, A.15, C.11, C.16, or another exact governing pattern only when its claim kind is live;
- state `NoMLANeeded` when no mathematical lens changes the next architecture move;

- stop with one admissible next architecture move.

The full `ArchitectureDescription@Context` opens only for durable publication, cross-team use, regulated or safety use, reusable design, FPF pattern example, comparison, reuse of a source, evidence, lens, or assurance relation, or a comparable full-mode claim kind. Ordinary use stops at `ArchitectureQuestionCard@Project` when it makes one next architecture move clear.

What goes wrong if C.30 is missed: a module diagram, Transduction Graph Architecture (TGA) graph, Layered Control Architecture (LCA)/control sketch, mathematical-lens output, generated relation graph, ADR, dashboard, or benchmark result is treated as the architecture; architecture then starts carrying evidence, assurance, gate, work, release, causal, or decision claim kinds it cannot carry.

What C.30 buys in practice: a practitioner can separate architecture claim, selected structure, architecture description, view, publication, source relation, and non-architecture claim kind, then choose one small next architecture move instead of opening a full measurement, synthesis, assurance, or decision apparatus by default.

Not this pattern when the live question is only structure as such. Use A.22. If it is an architecture structural view, use `C.30.ASV`. If it is a TGA graph, path, or crossing relation, use `E.18` and `C.30.TGA-FLOW-REL` when architecture-flow description is live. If it is evidence, assurance, causal use, gate, work, decision, publication authority, mathematical-lens adequacy, measurement, structural information, structural equivalence, morphism, or discovery aid, use the exact governing pattern or an admitted receiving pattern and keep C.30 only to the architecture-description portion.

Thin precision-restoration pointer: if the live issue is still whether *architecture*, *architecture description*, *structural view*, *module diagram*, *model*, *artifact*, *layer*, or *functional architecture* names an architecture claim, description, view, carrier, source, structure, or non-architecture receiving object, use `C.30.P` first. Do not copy the `C.30.P` trigger table into C.30; C.30 resumes after the architecture-description claim or exact non-architecture exit is recoverable.
### C.30:2 - Problem

Engineering teams use "architecture" for several different things:

- the selected structure of a holon;
- a diagram, model, table, dashboard, generated relation graph, or document;
- a module layout;
- a TGA graph or flow description;
- a functional, control, information, deployment, logical, or physical structure view;
- an ADR-like publication;
- a decision, gate, evidence path, assurance case, or release claim.

These uses are all useful in ordinary engineering speech, but they cannot carry the same FPF claim. The core distinction is the one already used across FPF: the architecture-relevant selected structure, the architecture claim over that structure, the D/S description or view of that claim, the publication of that description or view, and the project decision about changing architecture are different records.

The first-minute practitioner can ask: Are we choosing an architecture, or just naming a module layout? Which structure is being described: function, flow, control, module/interface, work, role/enactor, evidence/assurance, information/data, placement/deployment, scale, or declared logical structure? What artifact are we looking at: architecture claim, description, view, carrier, publication, decision, source-relation object, or mathematical lens?

How can FPF describe architecture without:

- creating `U.Architecture` as a new root kind;
- treating a description, view, diagram, graph, ADR, dashboard, or generated relation graph as the architecture;
- reducing architecture to module/interface structure;
- letting TGA, LCA, C.29 lenses, quality language, evidence, assurance, gates, work, or decisions silently become architecture ontology;
- making architecture descriptions so heavy that ordinary practitioners cannot get a first useful move.

### C.30:3 - Forces

| Force | Tension |
| --- | --- |
| Everyday architecture speech vs FPF kind precision | Engineers need familiar phrases such as functional architecture, physical architecture, and control architecture; FPF-force-bearing use recovers described holon, bounded context, selected structure, structure kind, artifact role, and admissible use. |
| Architecture claim vs architecture description | A useful architecture description can be mistaken for the architecture claim or for the selected structure. |
| Multi-view adequacy vs module reduction | Architecture includes functional, flow, control, module/interface, work, role, evidence, information, placement, scale, and declared logical structures; module diagrams are only one structure kind. |
| Small first move vs full record | The practitioner often needs one architecture question card, not a complete architecture description record set. |
| SoTA architecture-description discipline vs tool lock-in | ISO 42010-style view, viewpoint, and correspondence discipline is useful, and FPF adapts it to holons, epistemes, views, publications, source return, and exact governing pattern applications. |
| Structure source relation vs overread | A structure, graph, lens, measurement, or model can supply a source relation for an architecture description without proving evidence, assurance, causality, gate passage, or release. |

### C.30:4 - Solution

Introduce architecture-description adequacy as governance for describing an `ArchitectureOf@Context` claim record that selects intensional structure for one holon in one bounded context. The description is governed; it is not the architecture itself.

C.30 does not mint `U.Architecture` and does not redefine `U.Viewpoint`. It specializes A.22 structure records and `U.MultiViewDescribing` for architecture descriptions whose described entity is the `ArchitectureOf@Context` claim record for a holon, while preserving the I/D/S distinction between architecture and its descriptions.

C.30 governs architecture-description adequacy for one `ArchitectureOf@Context` claim record over selected `candidate:U.Structure` references for one described holon in one bounded context. It governs `ArchitectureOf@Context`, `ArchitectureQuestionCard@Project`, `ArchitectureDescription@Context`, architecture-description publication boundaries, architecture name formation, characteristic assignment, first architecture-question assignment, and small boundary notes. It does not mint `U.Architecture` and does not govern all architecture structure-kind views; `C.30.ASV` governs architecture structural views.

#### C.30:4.1 - Architecture claim record

```text
ArchitectureOf@Context ::= {
  describedHolonRef: U.HolonRef,
  boundedContextRef: U.BoundedContextRef,
  structureRefs: FinSet(candidate:U.StructureRef),
  structureKindRefs: FinSet(ArchitectureStructureKindRef),
  liveArchitectureConcernCue?,
  governingArchitectureConcernRefs?,
  architectureConcernNotes?,
  structuralRelationRecordRefs?,
  admissibleUse,
  nonAdmissibleUse
}
```

`ArchitectureOf@Context` is a project-side architecture claim record over selected structures. It is not the selected structure itself, not a D/S description, not a view, not a diagram, not a publication face, not a decision, and not a new root `U.*` kind.

`ArchitectureOf@ContextRef` is admissible as a `DescriptionContext.DescribedEntityRef` for architecture D/S descriptions and views. The holon whose architecture is claimed remains `ArchitectureOf@Context.describedHolonRef`; it is not the D/S `DescribedEntityRef` for those architecture descriptions unless a separate direct holon description is opened.

#### C.30:4.2 - Architecture description record

`ArchitectureDescription@Context` is a governed multi-view D/S description record set over one `ArchitectureOf@Context` claim record and selected `StructuralDescription@Context` or `StructuralView@Context` records. It is used for engineering reasoning about the described holon's design, operation, evolution, interfaces, work, evidence, adequacy, and scale behavior through typed relations to exact non-architecture records; it does not collect those non-architecture claim kinds as architecture-description ontology.

```text
ArchitectureDescription@Context ::= {
  architectureDescriptionId: ArchitectureDescriptionId,
  architectureClaimRef: ArchitectureOf@ContextRef,
  descriptionContext: DescriptionContext(
    DescribedEntityRef = architectureClaimRef,
    BoundedContextRef = ArchitectureOf@Context.boundedContextRef,
    ViewpointRef = viewpointRef
  ),
  selectedStructureRefs: FinSet(candidate:U.StructureRef),
  structureKindRefs: FinSet(ArchitectureStructureKindRef),
  architectureStructuralViewRefs: FinSet(ArchitectureStructuralViewRef),
  structuralAspectDescriptionRefs: FinSet(StructuralAspectDescriptionRef),
  correspondenceModelRefs: FinSet(CorrespondenceModelRef),
  structuralRelationRecordRefs: FinSet(QualifiedRelationRecordRef),
  descriptionRelianceRelationRefs?: FinSet(
    CharacteristicRelationRef | EvidencePathRef | AssuranceCaseRef |
    TGASourceRelationRef | MLALensBoundaryRef | SourceReturnRef
  ),
  freshnessCueRefs?: FinSet(ArchitectureDescriptionFreshnessCueRef),
  sourceReturnCondition?,
  admissibleUse,
  nonAdmissibleUse
}
```

`ArchitectureDescription@Context` is not the holon itself, not the selected structure, not identical to the `ArchitectureOf@Context` claim record, and not the publication face, carrier, or rendering. It is a D/S episteme record whose `DescriptionContext.DescribedEntityRef` points to the `ArchitectureOf@Context` claim record.

Use an `ArchitectureDescriptionFreshnessCue` when the admissible use of an architecture description depends on source edition or structure edition:

```text
ArchitectureDescriptionFreshnessCue:
  sourceEditionRefs:
  structureEditionRefs?:
  knownRefreshTrigger:
    sourceChange | deploymentChange | interfaceChange | controlRateChange |
    modelEditionChange | evidenceDecay | toolApiChange |
    legalRegulatoryChange | incidentFinding | unknown
  admissibleUseUntil:
  sourceReturnCondition:
```

The freshness cue is not evidence sufficiency and not assurance. It only bounds the architecture description's admissible use.

#### C.30:4.3 - Publication boundary

```text
ArchitectureDescriptionPublication@Project ::= {
  sourceEpistemeRef | sourceViewRef,
  publicationVPId,
  publicationScopeId,
  boundedContextRef,
  mvpkFaceRef,
  carrierRef,
  sourcePinSetRef,
  audience,
  admissiblePublicationUse,
  nonAdmissiblePublicationUse
}
```

`ArchitectureDescriptionPublication@Project` is E.17/MVPK-subordinate. It publishes one source episteme or episteme-lane view reference. `mvpkFaceRef` is a publication-lane face reference, not an alternative source object. Publication does not add architecture claims, evidence sufficiency, gate status, work authority, assurance, decision authority, or release permission.

Model cards, system cards, and evaluation harness reports enter C.30 through the same publication/source-relation boundary. They may describe a model, deployed AI system, architecture claim, evaluation harness, or policy, but they do not by themselves establish architecture adequacy, safety proof, release authority, or gate passage.

```text
ModelCardOrSystemCardBoundaryNote@Project ::= {
  sourcePublicationRef,
  describedEntityRef,
  describedEntityKind:
    model | deployedAISystem | architectureClaim |
    evaluationHarness | policy | otherDeclared,
  architectureStructureKindRefs?,
  intendedUseScope,
  evaluationScopeAndKnownLoss?,
  deploymentContextMismatch?,
  evidenceOrAssuranceGoverningPatternRef?,
  nonAdmissibleUse:
    notArchitectureAdequacy | notSafetyProof |
    notReleaseAuthorityByPublicationAlone
}
```

If the card or harness is used beyond transparency, recover the live architecture structure kind first and then apply `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `C.16`, `C.28`, or `C.11` for the non-architecture claim kind.

#### C.30:4.4 - Architecture name formation

The word `architecture` is shorthand only after the described holon, bounded context, selected structures, structure kind, and artifact role are recoverable. Without those qualifiers, it is a recovery trigger, not a stable FPF term.

```text
ArchitectureNameFormationRule:

If a text says "<X> architecture", then the FPF-force-bearing use is conforming only with:
  describedHolonRef,
  boundedContextRef,
  structureKindRef = <X>StructureKind or declared local relation,
  structureRefs,
  ArchitectureStructuralViewRefs if this is a description/view claim,
  admissibleUse,
  nonAdmissibleUse.

If <X> is not a declared structure kind, the phrase is plain recognition wording only.
```

| Phrase | Required recovery |
| --- | --- |
| functional architecture | `structureKindRef = FunctionalStructure`; functions, effects, capabilities, and functional dependencies named as structure content; transductions and flow paths are assigned to `FlowTransductionStructure` or `C.30.TGA-FLOW-REL`. |
| modular architecture | `structureKindRef = ModuleInterfaceStructure`; module relation records, interface specifications, substitutability rule, and change policy. Full module/interface repair applies the exact module/interface repair pattern when that claim kind is live. |
| logical architecture | `structureKindRef = DeclaredLogicalStructure`; local definition says whether `logical` means information, functional, runtime, responsibility/allocation, or another relation class. |
| physical architecture | `structureKindRef` in `{MaterialSpatialStructure, PlacementDeploymentStructure}` or a locally declared physical structure kind. |
| control architecture | `structureKindRef = ControlStructure`; an LCA record may describe the control structure, but proof claims are assigned to dynamics, temporal, causal, evidence, safety, or assurance patterns as triggered. |
| information architecture | `structureKindRef = InformationDataStructure`; state bearer and residence, schema refs, semantic refs, persistence locus, provenance relation, custody relation, and source-return conditions. |
| security architecture | `structureKindRef = SecurityTrustBoundaryStructure`; recover protected asset or effect, trust boundary, adversarial path, authority or privilege relation, secure-default or hardening boundary, and evidence, assurance, or gate governing patterns when those claim kinds are live. |


#### C.30:4.5 - Architecture characteristic assignment

C.30 uses three bearers before any `quality`, `fitness`, `measure`, `metric`, `score`, `modularity`, or `ility` wording carries architecture-adequacy force. Those words are triggers for bearer recovery, not stable architecture adequacy by themselves.

```text
ArchitectureCharacteristicAssignment:

A. SystemQualityAffectedByArchitecture
   Bearer: described U.Holon or named product/system entity
   Governing pattern: C.25 Q-Bundle or C.16
   Examples: maintainability, evolvability, resilience, availability, safety, observability

B. ArchitectureStructuralCharacteristic
   Bearer: `ArchitectureOf@Context` claim, architecture structural view, declared structural relation or constraint, module/interface relation
      Governing pattern: C.16 / A.17-A.19 / admitted architecture-characterization receiving pattern
   Examples: coupling, cohesion, interface alphabet, substitutability, hidden coupling, reusable-structure share

C. ArchitectureDescriptionAdequacy
   Bearer: ArchitectureDescription@Context / architecture structural view / correspondence model
   Governing pattern: C.30 / E.17 / C.16.Q / C.16
   Examples: viewpoint coverage, correspondence adequacy, source-return adequacy, description modularity
```

C.30 keeps only a thin bridge from structural characteristics to Q-Bundle relevance. If the claim says architecture causes an outcome improvement, assign causal-use governance to `C.28` before causal use. If a structural characteristic is used as a mechanism, constraint, predictor, proxy, evidence relation, or causal hypothesis for a Q-Bundle slot, start with `ArchitectureStructuralCharacteristicQBundleRelationLine` rather than a formula such as `low coupling = maintainability`; send measurement, modularity scoring, reusable-structure share or accounting, bespoke-residue accounting, evidence sufficiency, assurance, gate, causal proof, and scale audit to their exact governing patterns.

`ArchitectureStructuralCharacteristicQBundleRelationLine` is the only ordinary first-contact relation shape C.30 introduces for this case. Do not add a second generic characteristic relation record in C.30. Use the line when the useful move is to show why one structural characteristic may matter without opening the full relation record. Do not use this line as a measurement record, modularity score, evidence sufficiency statement, assurance verdict, or causal proof:

```text
ArchitectureStructuralCharacteristicQBundleRelationLine ::= {
  architectureClaimRef: ArchitectureOf@ContextRef,
  architectureStructuralViewRef?: ArchitectureStructuralView@ContextRef,
  structuralCharacteristicCueOrRef,
  affectedQBundleSlotRef,
  qBundleRelationKind:
    structuralCharacteristicRelevantToQBundleSlot |
    structuralCharacteristicConstrainsQBundleSlot |
    structuralCharacteristicPredictsQBundleSlot |
    structuralCharacteristicProxiesQBundleSlot |
    structuralCharacteristicCausalHypothesisForQBundleSlot |
    structuralCharacteristicEvidencePathForQBundleSlot,
  relationBasisKind:
    modelBased | empirical | causalModelBased | expertJudgement |
    sourceLineageOnly | SoTAActionLineage | reportOnly,
  evidenceOrCausalGoverningPatternRefIfLive?,
  nonAdmissibleUse
}
```

Minimal structural-characteristic relation-line examples:

| Structure kind | Structural characteristic cue or relation | Affected Q-Bundle slot | Relation-basis note | Non-admissible use |
| --- | --- | --- | --- | --- |
| `ModuleInterfaceStructure` | Stable interface specification plus substitution policy. | Evolvability or replaceability. | Replacement without global retesting. | Open label as substitutability proof. |
| `PlacementDeploymentStructure` | Controller placed near plant or edge-node locality. | Latency, resilience, or jurisdictional compliance. | Reduced communication delay and bounded data custody. | Placement diagram as performance or legal proof. |
| `InformationDataStructure` | State bearer, residence, provenance, and custody boundary. | Observability, privacy, or auditability. | Recoverable state lineage and bounded custody. | Data schema as evidence sufficiency. |
| `MaterialSpatialStructure` | Physical separation, adjacency, or energy path. | Safety, maintainability, or energy efficiency. | Isolation, accessibility, or loss reduction. | Geometry as safety proof. |
| `ControlStructure` | Observer-controller-plant loop with rate envelope. | Stability, controllability, or safety. | Feedback and bounded actuation relation. | Control diagram as proof. |
| `FlowTransductionStructure` | Path crossing, bottleneck, or buffer/waiting-line boundary. | Latency, throughput, or resilience. | Recoverable path, crossing, capacity, and valuation relation. | Flow graph as performance or causal proof. |
| `SecurityTrustBoundaryStructure` | Trust boundary, privilege path, or untrusted-input crossing. | Security, abuse resistance, or privacy. | Reduced exposed authority and bounded trust crossing. | Risk color or compliance label as security proof. |
| `EvidenceAssuranceStructure` | Evidence package reused across variants. | Assurance maintainability or release readiness. | Explicit affected-structure and source-return boundary. | Evidence-structure view as assurance verdict. |
| `WorkMethodStructure` | Method description, work plan, or work enactment relation with explicit exception path. | Operability, auditability, or maintainability. | Bounded repeatability and recoverable exception handling. | Work-method diagram as work authority or evidence sufficiency. |

`ArchitectureCharacteristicQBundleRelationRecord` is a triggered/full-mode record, not the ordinary first-contact shape. Open the full record only when publication, comparison, causal use, evidence reliance, assurance, gate, decision, or reusable cross-case relation reliance is live and the thin line cannot keep the relation inspectable, reusable, or bounded. This preserves the protection against causal or quality overread without turning C.30 into a measurement-first pattern.

Relation kinds in this record are C.30-local relation tokens. They must remain recoverable as A.6.P-style relation specifications: polarity, participant slots, qualifiers, witness expectations, admissible semantic change classes, and bridge or loss boundary where those are live.
ISO/IEC 25010-like quality models may be used as quality vocabulary or comparison lineage for product qualities such as reliability, security, maintainability, usability, efficiency, compatibility, or portability. C.30 does not inherit them as architecture theory. Architecture relates to qualities through Q-Bundle slots, mechanism slots, relation posture, evidence or causal governing patterns, or report-only posture.

```text
ArchitectureCharacteristicQBundleRelationRecord ::= {
  architectureClaimRef: ArchitectureOf@Context,
  architectureStructuralViewRef?,
  architectureDescriptionRef?,
  structuralCHRRefs,
  affectedQBundleRefs,
  relationKind:
    structuralCharacteristicRelevantToQBundleSlot |
    structuralCharacteristicConstrainsQBundleSlot |
    structuralCharacteristicPredictsQBundleSlot |
    structuralCharacteristicProxiesQBundleSlot |
    structuralCharacteristicCausalHypothesisForQBundleSlot |
    structuralCharacteristicEvidencePathForQBundleSlot,
  participantSlots:
    structuralCharacteristicRef,
    qBundleSlotRef,
    architectureClaimRef,
    scopeOrScaleWindow?,
    viewpointRef?,
  qualifiers?,
  witnessExpectations?,
  relationBasisKind:
    modelBased | empirical | expertJudgement |
    sourceLineageOnly | SoTAActionLineage | causalModelBased | reportOnly,
  bridgeOrLossBoundary?,
  admissibleUse,
  nonAdmissibleUse,
  evidenceOrCausalGoverningPatternRefIfLive?
}
```
#### C.30:4.6 - Relation to structural views

`C.30.ASV` governs `ArchitectureStructuralView@Context`. C.30 only governs the architecture-description relation to the structural views it uses, with hidden/lost structure, correspondence, source or reliance relation, and source-return boundaries recoverable when those boundaries affect action.

A diagram, model, table, TGA graph, LCA diagram, C.29 lens output, ADR, dashboard, generated explanation, or other publication face may carry an architecture description or an architecture structural view. It does not become the architecture, and it does not become a conforming view only because it looks like a view.

Use `AffectedArchitectureStructureNote` when the next architecture move needs to name affected structures or view losses without opening an architecture decision, ADR, gate, evidence, assurance, or release record:

```text
AffectedArchitectureStructureNote:
  architectureClaimRef:
  affectedStructureKindRefs:
  affectedStructureRefs?:
  affectedArchitectureStructuralViewRefs?:
  acceptedOrSuspectedViewLoss?:
  sourceReturnCondition?:
  nextAdmissibleMove:
```

This note only names affected architecture structure for the next move. It is not an architecture decision, not an ADR, not gate passage, not evidence sufficiency, and not release authority.

#### C.30:4.7 - Minimal boundary notes

Use these notes when a common architecture phrase is close to a exact governing pattern but the full governing pattern is not yet live.

Use the thinnest relation form that preserves the next architecture move. Open fuller exact governing relation records only when the current relation cannot be inspected, used, compared, refreshed, or bounded without it. Typical thin forms are `ArchitectureMLABoundary` before C.29 Mini or Full, `AffectedArchitectureStructureNote` before an architecture decision record, and `ArchitectureStructuralCharacteristicQBundleRelationLine` before full measurement or causal/evidence records.

```text
InterfaceSignatureBoundaryNote ::= {
  phraseOrArtifactRef,
  apparentClaim:
    interface | signature | port | endpoint | connector | link |
    API | protocol | TGA transfer | TGA path | mechanism reference,
  recoveredKind,
  governingPatternApplicationRefs,
  admissibleUse,
  nonAdmissibleUse
}

ModuleRelationBoundaryNote ::= {
  phraseOrArtifactRef,
  apparentClaim:
    module | component | package | platform | stack | open architecture |
    typed control-structure relation,
  moduleInterfaceRepairClaimLive?: yes | no,
  openOrPlatformClaimLive?: yes | no,
  exactModuleInterfaceRelationRefs?,
  variationPointRef?,
  substitutabilityPolicyRef?,
  interfaceConformanceEvidencePatternRef?,
  changePathRef?,
  consumerMigrationBoundary?,
  versionOrUpdateChannelRef?,
  secureDefaultOrHardeningBoundary?,
  governingPatternApplicationRefs,
  admissibleUse,
  nonAdmissibleUse
}
```

These notes are not substitutes for the exact module/interface repair pattern, interface specifications, signature records, conformance evidence, or module/interface repair. An open or platform label is not substitutability proof, security proof, scale proof, assurance, or universal maturity evidence. It becomes architecture-relevant only through local structure, interface, variation, substitution, migration, update, and hardening boundaries. Relation-heavy wording inside these notes remains a Plain cue until an exact module/interface relation ref, exact governing relation record, or governing FPF pattern carrier is named. The note keeps first use honest until the exact non-architecture claim kind opens.

#### C.30:4.8 - Architecture mathematical-lens boundary

Architecture descriptions may use C.29 lenses, but the lens does not become architecture ontology.

```text
ArchitectureMLABoundary:
  noMLANeeded?: yes | no
  lensOneLine?:
    lensRef,
    structureClaimRef,
    preservedStructure,
    lostStructure,
    lensRelationBasisKind,
    stopCondition,
    governingPatternApplicationRefs?
```

Use the one-line boundary only when it is enough to keep the lens from being overread. Open C.29 Mini or Full cards when the lens choice, preserved/lost structure, relation posture, or stop condition changes the architecture move.

Lens use by architecture problem:

| Architecture problem | Candidate mathematical lens | Preserved structure | Typical loss or stop |
| --- | --- | --- | --- |
| Hidden dependency or modularity. | Typed graph, DSM, or hypergraph. | Dependency, coupling, or clustering. | Semantics, interface law, evidence, and work remain outside unless bridged. |
| Flow bottleneck. | TGA, network flow, or queueing. | Path, crossing, valuation, and capacity. | Purpose, proof, causality, and safety remain non-architecture claims. |
| Control-rate mismatch. | LCA, hybrid systems, assumption-guarantee relations, or control relations. | Feedback roles and scale or rate relations. | Stability proof and safety proof remain outside the lens. |
| Cross-scope residual. | Coarse-graining or renormalization-group-style lens. | Preserved and lost structure across scale. | Utility, causal-use claims, and selector authority remain outside unless separately grounded. |
| Extracted structure from traces. | Epiplexity or MDL-style bounded-observer lens. | Learnable structural regularity. | Task relevance, assurance, and causal proof remain non-architecture claims. |
| Physical separation or spatial arrangement. | Topology, geometry, or spatial graph lens. | Adjacency, containment, separation, reachability, or energy/material path. | Safety proof, accessibility, legal acceptance, and causal-use claims remain outside unless separately grounded. |
| Composition relation. | Category, open-systems, or compositional lens. | Interface, composition, and coherence. | Domain semantics remain outside unless bridged. |

This table is not a C.29 replacement and does not make mathematics mandatory. It helps the practitioner see when a lens may add a useful architecture move; C.29 still carries lens adequacy, preserved/lost structure, relation posture, and stop condition when those are live.

Epiplexity-like use remains a C.29 bounded-observer structural-information lens. It may help recover learnable structure from traces, but it is not an architecture quality, task relevance proof, causal proof, assurance, or selector authority.

#### C.30:4.9 - Boundary and repair table

| Tempting collapse | C.30 repair |
| --- | --- |
| Bare architecture as governed object | Recover `describedHolonRef`, `boundedContextRef`, selected `structureRefs`, active `structureKindRef`, artifact role, `admissibleUse`, and `nonAdmissibleUse`. |
| Architecture description as architecture | Keep `ArchitectureDescription@Context` as D/S episteme over `ArchitectureOf@Context`. |
| Diagram, model, table, dashboard, or generated relation graph as architecture | Treat it as carrier, publication, description, view, source relation, or source-finding aid only when that relation is explicit. |
| Module diagram as all architecture | Use `C.30.ASV` to recover structure kind; module/interface is only one structure kind. |
| TGA graph as architecture | Use `E.18` for graph/path/crossing and `C.30.TGA-FLOW-REL` for architecture-flow description. |
| LCA/control diagram as proof | Use `C.30.LCA` for control-structure view; assign dynamics, temporal, causal, evidence, gate, safety, and assurance claims to their governing patterns. |
| Mathematical lens as architecture ontology | Use `C.29`; cite `MLAOutputRef` only through an `ArchitectureMLABoundary` or C.29 lens record and state stop condition. |
| ADR as architecture decision | Use the exact project-side architecture decision pattern when a decision claim is live; ADR is a publication form, not the decision. |
| Quality, score, or measurement term as architecture adequacy | Recover the bearer through `ArchitectureCharacteristicAssignment`; assign the live claim to `C.25`, `C.16`, an admitted architecture-characterization receiving pattern, or C.30 description adequacy. |
| Architecture record as evidence, assurance, gate, work, or release | Assign evidence, assurance, gate, work, or release claims to `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, or release loci as live. |
| Architecture as agent, worker, controller, gate, or proof | Recover the mechanism, control relation, role/enactor, gate, work, evidence, or assurance carrier that actually bears enforce, decide, optimize, adapt, prove, or guarantee wording; keep `ArchitectureOf@Context` as a selected-structure claim, not an acting entity. |

#### C.30:4.10 - Worked slices

**"We have the architecture in this diagram."** The diagram is a carrier or publication face unless it explicitly carries an `ArchitectureDescription@Context` or `ArchitectureStructuralView@Context`.

```text
ArchitectureQuestionCard@Project:
describedHolonRef: payment system
boundedContextRef: checkout platform context
liveArchitectureConcernCue: unclear dependency between payment orchestration and fraud scoring
plainPromptLabel: "architecture in this diagram"
activeStructureKindRefs: FunctionalStructure, ModuleInterfaceStructure, FlowTransductionStructure
currentCollapseCue: diagram is being treated as architecture itself
firstArchitectureMove: downgrade the diagram to a publication face and create a minimal architecture structural-view note
ordinaryNotThisPatternBoundary: no evidence, assurance, gate, or decision claim yet
governingPatternApplicationRefs: C.30.ASV
```

**"Low coupling gives maintainability."** C.30 does not allow that formula to carry the claim by itself. The ordinary repair starts with the thin relation line:

```text
ArchitectureStructuralCharacteristicQBundleRelationLine:
  architectureClaimRef: ArchitectureOf@ContextRef
  structuralCharacteristicCueOrRef: coupling under module/interface relation
  affectedQBundleSlotRef: maintainability Q-Bundle slot
  qBundleRelationKind: structuralCharacteristicRelevantToQBundleSlot
  relationBasisKind: sourceLineageOnly | SoTAActionLineage | modelBased, as actually grounded
  evidenceOrCausalGoverningPatternRefIfLive?: C.28 / B.3 / A.10 / G.6 when the stronger claim is live
  nonAdmissibleUse: causal proof or assurance by slogan
```

Open `ArchitectureCharacteristicQBundleRelationRecord` only when publication, comparison, causal use, evidence reliance, assurance, gate, decision, or reusable cross-case relation reliance needs the fuller record. The useful move is to decide whether a structural characteristic has a bounded relation to a maintainability slot, not to accept the slogan as architecture truth.

**"We replaced the neural-network block, so the architecture improved."** The phrase is admissible architecture recognition only after the changed structure kind, flow or transduction relation, module or interface claim kind, preserved and lost structure, changed characteristic, source-relation object, and decision or evidence governing patterns are named. A block label, benchmark result, ablation, pruning mask, or distillation result is not an architecture decision, evidence sufficiency, gate passage, assurance, or architecture adequacy by itself.

### C.30:5 - Archetypal Grounding

| Tell-Show-Show row | Grounding |
| --- | --- |
| Tell | A project team says "architecture" while looking at a diagram, model, generated relation graph, ADR, or module list. C.30 asks what holon is being described, what structure is selected, what artifact role the current material has, and what architecture move remains admissible. |
| Show: `U.System` | A payment system, plant, vehicle, product platform, AI-agent system, or neural-network model has selected structures: function, flow, control, module/interface, information, placement, scale, work/evidence, or declared logical structure. The architecture claim is over selected structures of that holon; the publication is not the holon and not the architecture claim. |
| Show: `U.Episteme` | An architecture description, model, view, generated relation graph, ADR-like note, safety-case view, or dashboard is an episteme or view publication. It can describe an architecture claim or serve as a source relation for it, but it does not become the architecture, evidence sufficiency, gate result, assurance case, or project decision. |

### C.30:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto/Epist**, **Prag**, **Did**, **Gov**. Scope: FPF architecture-description use over holons.

| Bias risk | Mitigation |
| --- | --- |
| Module-diagram bias | Keep module/interface as one structure kind among several; use `C.30.ASV` and the exact module/interface repair pattern when live. |
| Tool-model bias | Treat notation, tool model, generated relation graph, diagram, and dashboard as D/S or publication artifacts unless a declared governing relation gives the artifact a more specific role. |
| Check-only bias | The first output is an architecture question card plus action palette, not a checklist that only detects mistakes. |
| Assurance/gate bias | Architecture descriptions do not certify safety, evidence sufficiency, release, or gate passage; assign those claims to the governing patterns. |
| Didactic-thinning risk | Semantic repair preserves why the distinction matters: the pattern opens with the practitioner situation, payoff, stop condition, and first move. |

This checklist verifies the preceding guidance after the practitioner has chosen the live move; it is not a required project control form and not a substitute for the card, note, view, relation, or repair move above.

### C.30:7 - Conformance Checklist


| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-C30-1 Grounded architecture name.** | An FPF-force-bearing architecture claim names the described holon, bounded context, selected structures, structure kinds, artifact role, admissible use, and non-admissible use. | Rewrite the phrase through `ArchitectureQuestionCard@Project` or demote it to Plain recognition wording. |
| **CC-C30-2 No `U.Architecture`.** | The pattern use does not mint or rely on a root `U.Architecture`. | Use `ArchitectureOf@Context` over selected A.22 structures, or assign the claim to another existing kind. |
| **CC-C30-3 I/D/S separation.** | Architecture claim, structure, description, view, publication face, carrier, decision, evidence, and work stay distinct. | Downgrade the artifact or carrier to its D/S or publication role and name the claim or non-architecture claim kind separately. |
| **CC-C30-4 ArchitectureOf record.** | Architecture descriptions and views point through `ArchitectureOf@Context`; the described holon is recovered through `architectureClaimRef.describedHolonRef`. | Add `ArchitectureOf@Context` or split direct holon description from architecture-claim description. |
| **CC-C30-5 DescriptionContext reuse.** | `ArchitectureDescription@Context` reuses `DescriptionContext` and existing D/S machinery; it does not redefine viewpoint or publication ontology. | Replace local fields with imported D/S fields or assign the publication/view claim to E.17/A.6.3/E.17.0. |
| **CC-C30-6 Small output before heavy record.** | Ordinary use may stop at `ArchitectureQuestionCard@Project` when one next architecture move and exact governing pattern application is clear. | Remove needless full-record expansion or explain which full-mode trigger is live. |
| **CC-C30-7 Structure-kind boundary.** | Structural-view claims apply `C.30.ASV`; module, function, flow, control, work, evidence, scale, and decision claims do not collapse into C.30. | Name the structure kind, open the structural view if needed, or assign the claim to the exact governing pattern. |
| **CC-C30-8 Characteristic assignment.** | Quality, measure, score, metric, modularity, and `ility` wording recovers its bearer and governing pattern before use. | Add `ArchitectureCharacteristicAssignment`, or narrow the sentence to ordinary non-FPF-force-bearing recognition. |
| **CC-C30-9 Non-architecture claim kind.** | Evidence, assurance, causal, gate, work, decision, publication-authority, mathematical-lens, measurement, and release claims are assigned to their governing patterns. | Name the exact governing FPF pattern and the live claim kind; do not add fields to C.30 to absorb it. |
| **CC-C30-10 Useful action.** | The repaired wording leaves a surviving admissible action: name the architecture claim, downgrade an artifact, open an architecture structural view, add a source or reliance relation, return to source, or apply the exact governing pattern that carries the live claim kind. | Restore that action, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

### C.30:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Architecture-as-document** | The document, diagram, table, generated relation graph, or dashboard is called the architecture. | Recover carrier/publication/description/view relation and name `ArchitectureOf@Context` only when selected structure is live. |
| **Publication-unit architecture drift** | One publication unit mixes architecture description, evidence status, gate status, decision note, and work authority under one architecture heading. | Name the source architecture description or view, split evidence/gate/decision/work authority to exact governing patterns, and keep the publication face as E.17/MVPK-subordinate. A publication heading is not an architecture claim, and a section title is not evidence, gate, decision, or work authority. |
| **Module-diagram takeover** | Architecture is reduced to module/interface structure. | Recover structure kind and use `C.30.ASV`; assign full module repair to the exact module/interface repair pattern when that claim kind is live. |
| **Tool-model lock-in** | A notation or tool model becomes the source of architecture truth. | Recover FPF architecture claim, structures, views, correspondence, and source-return condition. |
| **Evidence laundering** | A published architecture description is used as evidence sufficiency. | Assign evidence-path governance to `A.10` or `G.6`; C.30 keeps only description adequacy. |
| **Assurance or safety overread** | Architecture description or LCA diagram is used as assurance or safety case. | Assign the live claim to `B.3`, `A.10`, `G.6`, `C.30.LCA`, and safety/gate patterns as live. |
| **Risk color as architecture decision** | A red, yellow, or green risk cell, risk matrix, or maturity score decides the architecture move or resource-allocation priority. | Recover the live structure kind, affected scope, loss, hazard, or threat path, source or relation basis, characteristic scale, comparator, and gate pattern; do not treat ordinal risk color as architecture adequacy, evidence sufficiency, causal proof, assurance proof, resource-allocation basis, or gate passage. |
| **Causal slogan** | Architecture property is said to cause a quality without a declared relation basis. | Start with `ArchitectureStructuralCharacteristicQBundleRelationLine`; open `C.28`, evidence-path, causal-use, or assurance claim, or `ArchitectureCharacteristicQBundleRelationRecord` only when that stronger evidence, causal-use, assurance, or full relation claim is live. |
| **Architecture-operation overread** | Replacing a block, module, layer, protocol, cache, memory path, or flow relation is treated as improvement by label alone. | Recover changed structure kind, preserved/lost structure, source-relation object, affected characteristic, and decision or evidence governing pattern. |
| **Sterile compliance rewrite** | The text becomes well typed but no longer helps the practitioner act. | Restore `ArchitectureQuestionCard@Project`, a concrete next architecture move, or a named exact governing pattern application. |

### C.30:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| Architecture claims become separable from diagrams, publications, generated relation graphs, ADRs, module lists, and decisions. | A conforming use names described holon, context, selected structure, and artifact role when the use carries FPF force. |
| The pattern enables first-principles architecture reasoning without forcing full measurement, synthesis, assurance, or decision machinery. | Some familiar architecture phrases become triggers for quick recovery rather than accepted claims. |
| Functional, flow, control, module/interface, information, placement, scale, work/evidence, and declared logical structures can coexist without one structure kind swallowing the rest. | Structural-view adequacy moves to `C.30.ASV`, so practitioners may need an explicit view application. |
| C.29, E.18, LCA, module/interface, evidence, assurance, and gate patterns can supply source or reliance relations for architecture work without becoming architecture ontology. | Exact governing pattern applications are named whenever a source or reliance relation is used beyond description adequacy. |

### C.30:10 - Rationale

Architecture is most useful in FPF when it stays close to selected structure over a holon and far away from document-as-architecture, graph-as-architecture, model-as-architecture, and decision-as-architecture collapses. The `ArchitectureOf@Context` record gives the selected structure a project-side claim handle without minting `U.Architecture`.

C.30 and C.30.ASV establish an FPF architecture kernel: architecture as selected intensional structure for a described holon, with D/S descriptions and structural views, structure-kind discipline, correspondence and source-return boundaries, and characteristic-relation applications. They do not by themselves provide full measurement, synthesis, decision, causal proof, safety proof, or assurance.

The small first card is deliberate. Architecture discussions often need one immediate move: name the holon, choose the live structure kind, downgrade an artifact, assign an evidence or assurance claim to its governing pattern, or stop. A full architecture description is useful only when durable publication, cross-team use, comparison, regulated use, or source/reliance reuse is live.

The D/S split also preserves plurality. The same architecture claim may have several descriptions and views; several publications may render one description; several source records may be source relations for a view with different validation boundaries. C.30 keeps those variants usable without turning any one carrier into the architecture.

### C.30:11 - SoTA-Echoing

| Practice or source line | C.30 adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022 view, viewpoint, concern, and correspondence discipline | Adopt view/viewpoint/correspondence discipline for architecture descriptions. | Ask for architecture claim, `DescriptionContext`, viewpoint/correspondence posture, and next architecture move before notation-specific records. | Reject tool, notation, or method-description lock-in; FPF holon, episteme, view, and publication split stays governing. |
| OMG SysML v2 and current MBSE traceability/model-consistency practice | Adapt model-view consistency and traceability as source-return and relation pressure when architecture description or traceability wording carries FPF force. | Use correspondence, source pins, description-reliance relations, and source-return conditions. | Reject model-as-architecture overread and tool dependence. |
| SEI views-and-beyond lineage plus current multi-view practice | Keep module, component/connector, runtime interaction, allocation, and placement as separate view pressures. | Do not reduce architecture to module/interface structure; assign structural-view claims to `C.30.ASV`. | Older view taxonomies are lineage and comparison basis, not a second FPF ontology. |
| arXiv:2603.00601 code-space architecture relation-graph work and related code-agent architecture probing benchmarks | Adapt partial-observability probing, typed edge rules, component-boundary rules, invariant-field semantics, uncertainty or unexplored-region reporting, and probe-as-intervention warning. | A generated code relation graph can supply a source relation for an architecture description or structural view only with claim, source, uncertainty, relation semantics, and source return. | Do not mint `U.CodeSpace`; do not treat probe or benchmark output as architecture adequacy, evidence sufficiency, assurance, or release. |
| GonzoML neural-network architecture corpus as practitioner operation-language intake | Adopt practitioner architecture-operation language as general architecture material: structural substitution, relation retargeting, dataflow change, path-selection and gating, memory and cache placement, block and layer substitutions, MoE expert-selection, pruning, distillation, NAS, ablation, and compute/memory/latency tradeoffs. | Use the language for architecture-description and architecture-view recognition, TGA flow-structure source relation, module/interface repair, scale characterization, candidate move guidance, and decision-context fields. | Neural-network labels, benchmarks, ablations, pruning masks, search outputs, or distillation success do not become FPF ontology, architecture decision, evidence sufficiency, gate passage, assurance, or architecture adequacy by themselves. |
| Platform-engineering and MOSA/open-systems practice | Adapt open-interface and platform-readiness pressure as local architecture boundary discipline. | For an open/platform claim, name the local structure, interface, variation point, substitution policy, conformance-evidence governing pattern, migration boundary, update channel, and hardening boundary that change action. | Platform design depends on project, organization, time, and place; there is no universal platform maturity scale or open-label proof. |
| ADR and architecture-knowledge-management practice | Adopt decision-memory pressure only as a project-side decision concern governed outside C.30. | Treat ADR-like material as publication or decision-description source relation until the architecture decision pattern is live. | ADR is not the project decision itself and not a source of release authority. |

### C.30:12 - Relations

Builds on: `A.22`, `C.30.P`, `C.2.1`, `A.6.3`, `A.7`, `E.10.D2`, `E.17.0`, `E.17.1`, `E.17`, `E.17.2`, `A.6.P`, `F.18`, `E.10`, and `C.2.P`.

Coordinates with: `C.30.ASV`, `A.6.F`, `C.30.TGA-FLOW-REL`, `C.30.LCA`, `C.30.ILC`, `E.18`, `C.29`, `C.16`, `C.25`, `C.28`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, `E.17`, and named receiving patterns for architecture decision and candidate-set claims when those claim kinds are live.

Does not replace: A.22 structure carrier, C.30.ASV structural-view adequacy, E.TGA graph/path/crossing discipline, C.29 mathematical-lens adequacy, C.16 characterization, C.25 Q-Bundles, C.28 causal-use support, A.10/G.6 evidence, B.3 assurance, A.20/A.21 gate/release records, A.15 work, C.11 decisions, or E.17 publication.

### C.30:End

