## C.30 - Grounded Architecture and Selected-Structure Adequacy

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.30:1 - Problem frame

Use this pattern when the current question concerns the architecture of one exact `U.Holon`: which actual subject relations obtain, which exact `U.Structure` is selected from them, whether the direct `ArchitectureRelation` obtains, what one C.2.1 claim says about that holon, relation, or structure, under which concern and admissible-use frame, and what next architecture move follows.

The first useful architecture move is small:

```text
ArchitectureQuestionCard@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureQuestionProjectUseRelationRef?: U.RelationRef
  architectureClaimRef?: ArchitectureClaimRef
  describedHolonRef:
  architectureRelationDisposition:
    actualRelationNamed | actualRelationStillToRecover |
    candidateOrExpectedOnly | nonArchitectureQuestion
  architectureRelationRefs?: FinSet(U.RelationRef)
  claimScope?:
  effectiveReferenceScheme?:
  modelUseStructureRef?: only when one selected bounded model-use structure changes this architecture use
  architectureConcernCue:
  architectureConcernClaimRefs?: FinSet(U.EpistemeRef)
  sourcePhrase?, if useful:
  questionDisposition:
    concernCueOnly | problemCardReady | architectureClaimReady | nonArchitectureClaimReady
  selectedStructureRefs?: FinSet(U.StructureRef)
  candidateOrExpectedStructureRefs?: FinSet(U.StructureRef)
  selectedStructureKindRefs or candidateStructureKindRefs:
  inspectedMaterialUse, if current: claim content | description | view | representation | publication form | source | decision | mathematical lens | other exact use
  inspectedMaterialUseRelationRefs?: exact direct relation refs that obtain
  firstArchitectureMove:
  architectureDescriptionBridge, if durable description use is current:
  governingPatternApplicationRefs, if another claim is being made:
  non-admissible overread:
```

The card can stop before a durable claim. An `actualRelationNamed` result requires exact obtaining `ArchitectureRelation` occurrences and their A.22 structure participants. A candidate, planned, required, desired, expected, modeled, or diagrammed structure remains in `candidateOrExpectedStructureRefs` and makes no subject relation obtain.
`architectureConcernCue` is recognition wording only until it helps choose one selected structure kind and one architecture move. When a controlled cue is useful, use `changeLocalization`, `substitutionOrReplacement`, `flowBottleneck`, `controlOrRateMismatch`, `dataCustodyOrStateResidence`, `physicalSeparationOrPlacement`, `evidenceReuseOrAssuranceReuse`, `scaleWindowOrCoarseningLoss`, `runtimeFailureMode`, `crossScopeResidual`, `descriptionViewLoss`, or `otherDeclared`. Local phrases such as change localization failure, hidden crossing, source return, generated-view loss, or state-residence uncertainty may remain in `sourcePhrase?` or Plain prose. If the described holon, actual/candidate structure distinction, architecture concern, and first move cannot yet be named, set `questionDisposition` to `concernCueOnly` or `problemCardReady`; wording alone promotes neither a claim nor an obtaining relation.

`ArchitectureQuestionCard@Project` is a triage aid for choosing one architecture move. `questionDisposition` records whether to keep a concern cue, prepare a separately governed ProblemCard, constitute an `ArchitectureClaim`, or name a non-architecture pattern. `architectureRelationDisposition` separately records whether an actual direct relation has been recovered or the content is candidate/expected only. The card is not an evidence record, gate, decision, release record, quality score, risk rating, or publication-use authority claim.

Across C.30, `@Project` in a record name is a compatibility and retrieval cue only. It identifies neither a project entity nor a composite project `U.Work`, and it establishes no context, authority, viewpoint, or parthood. When the card is genuinely local to one actual project, `projectWorkOccurrenceRef` identifies the exact composite `U.Work` recovered under A.15.6 and `architectureQuestionProjectUseRelationRef` identifies the exact obtaining relation by which this card use concerns that Work. Description publication and other project-local uses likewise name their own exact Work and project-use relation. A described holon, architecture claim, or architecture relation does not become project Work by retrieval suffix.

Use a conditional `ArchitectureDescription` bridge only when durable architecture-description use is current: cross-team reuse, regulated or safety use, reusable design, comparison, source or lens reuse, or another named full-mode description use. Ordinary use stops at `ArchitectureQuestionCard@Project` when it makes one next architecture move clear. If the architecture description itself becomes the EntityOfConcern under repair, use `C.30.AD`.

What goes wrong if C.30 is missed: the practitioner reasons from a document, module diagram, transformation-flow graph description, mathematical lens, benchmark, maturity score, or decision record instead of recovering the described holon, selected structures, first architecture move, and non-architecture claim kind.

What C.30 buys in practice: a practitioner can separate actual subject relations, selected structure, direct architecture relation, claim episteme, description, view, representation, publication occurrence/form/carrier, source relation, and non-architecture claim kind, then choose one small next architecture move.

Not this pattern when the `EntityOfConcern` under repair is not an architecture claim, selected architecture-relevant structure, source relation, description relation, view relation, publication-use recovery for an architecture claim, or the thin architecture-description bridge needed for one architecture move. Use the subject pattern named by the recovered relation, and keep C.30 only for the architecture-claim portion if that portion is being claimed. Common non-architecture claim boundaries are summarized in `C.30:12`.

Thin precision-restoration pointer: if the issue under repair is still whether *architecture*, *architecture description*, *structural view*, *module diagram*, *model*, *source material*, *functional architecture*, or a source label such as *layer*, *level*, *tier*, *stack*, *block*, *expert*, *cache*, *router*, or *gate* names an architecture claim, description, view, representation, publication form, source relation, structure, or non-architecture subject-pattern application, use `C.30.P` or `C.30.STRAT` as triggered before applying C.30 to the recovered architecture portion. If the recovered issue is mathematical-lens use, apply `C.29`; when no mathematical-lens use changes the architecture work, keep ordinary prose or use `NoMathLensUseNeededNote` under C.29 rather than creating a C.30-local lens result. Keep trigger tables in those patterns; C.30 is applied only after `ArchitectureClaim`, exact selected architecture-relevant structure, conditional `ArchitectureDescription` bridge use, `C.30.AD` application, or the non-architecture application named by value is recoverable.

### C.30:2 - Problem

Engineering teams use "architecture" for several different things:

- the selected structure of a holon;
- a diagram, model, table, dashboard, generated relation graph, or document;
- a module layout;
- a selected transformation-flow structure, flow description, or mathematical graph description;
- a functional, control, information, deployment, logical, or physical structure view;
- an ADR-like publication;
- a project-side claim carried by another governing FPF pattern.

These uses are all useful in ordinary engineering speech, but they cannot carry the same FPF claim. The core distinction is the one already used across FPF: actual subject-relation occurrences; the exact A.22 structure selected from them; the direct `ArchitectureRelation` that may obtain between that structure and one holon; a C.2.1 claim about the holon, relation, or structure; the Description episteme or view; the representation and publication objects; and any project decision about changing architecture are different objects.

The first-minute practitioner can ask: Are we recovering an actual architecture relation, considering a candidate structure, or only reading a representation? Which subject relations actually obtain, and which exact A.22 structure is selected from them? Which structure kind is in view: function, flow, control, module structure, interface relation, Work, system-role-kind or assignment structure, enactor structure, evidence relation, assurance relation, information structure, data structure, placement structure, deployment structure, scale structure, or declared logical structure? What is the inspected material being used as: claim content, description, view, representation, publication form, decision, source relation, or mathematical lens?

How can FPF describe architecture without:

- creating `U.Architecture` as a new root kind;
- treating a description, view, diagram, graph, ADR, dashboard, or generated relation graph as the architecture;
- reducing architecture to module structure or interface relation;
- letting E.18 transformation-flow structures, LCA structures, control structures, C.29 lenses, quality language, evidence, assurance, gates, work, or decisions silently become architecture ontology;
- making architecture descriptions so heavy that ordinary practitioners cannot get a first useful architecture move.

### C.30:3 - Forces

| Force | Tension |
| --- | --- |
| Everyday architecture speech vs FPF kind precision | Engineers need familiar phrases such as functional architecture, physical architecture, and control architecture; FPF-governed use recovers described holon, selected structure, structure kind, architecture concern, admissible-use frame, and the exact use of inspected material as source, description, view, or publication form. |
| Direct architecture relation vs claim vs description | An obtaining `ArchitectureRelation`, a C.2.1 claim about it or about candidate/expected structure, and a useful architecture description are easy to collapse into one word even though only the direct relation is subject-side architecture. |
| Multi-view adequacy vs module reduction | Architecture includes functional, flow, control, module structure, interface relation, Work, system-role-kind or assignment structure, evidence relation, information structure, placement structure, scale, and declared logical structures; module diagrams are only one structure kind. |
| Small first architecture move vs full record | The practitioner often needs one architecture question card, not a complete architecture description record set. |
| Multi-view architecture discipline vs tool lock-in | Current FPF separates holons, selected structures, descriptions, viewpoints, views, correspondences, publications, source return, and subject-pattern applications without importing a tool-specific lifecycle. |
| Structure source relation vs overread | A structure, graph, lens, measurement, or model can supply a source relation for an architecture description without proving evidence, assurance, causality, gate passage, or release. |

### C.30:4 - Solution

C.30 starts from one architecture move over one exact `U.Holon`. Recover separately: any actual subject-relation occurrences; the exact A.22 structures selected from them; any obtaining `ArchitectureRelation`; the claim episteme that states an affirmative, negative, unresolved, candidate, or expected architecture claim; the concern and admissible-use frame; and the exact use of inspected material as source, description, view, representation, publication form, decision input, or another directly governed use. Use a conditional architecture-description bridge when durable, reusable, multi-view, regulated, comparison, or reliance-bearing description is being made. If `ArchitectureQuestionCard@Project` gives one usable next architecture candidate use, stop there.

In C.30, the EntityOfConcern is one exact described holon, one exact `ArchitectureRelation` occurrence, one exact selected structure, or another exact subject object selected by the current claim. A claim episteme, description, diagram, or publication is not a proxy EntityOfConcern for a world-side relation or structure. Description hygiene supports this boundary but is not the center of C.30.

Architecture-description material in C.30 is deliberately minimal. C.30 itself is not the full architecture-description mechanism. It gives a thin bridge from the exact holon, architecture relation, or selected structure to a separately constituted architecture-description episteme only when durable description use changes the architecture move. `C.30.AD` carries the full general architecture-description EntityOfConcern: multi-view description sets, viewpoint-based views, correspondences, source return, freshness, specification use, and publication boundary. `C.30.AD.BA` carries built-asset architecture-description, asset-information, digital-twin, and reference-designation specialization. Generic episteme, view, viewpoint, publication, form, representation, and carrier machinery remains with C.2.1, E.17.0, E.17.1, E.17.2, E.17, E.24.PUB, and C.29. C.30.ASV carries the selected-structure-to-view branch; C.30.TFS-REL, C.30.LCA, and other named subpatterns carry their direct structure relations and claims.

C.30 does not mint `U.Architecture` and does not redefine `U.Viewpoint`. It directly governs `ArchitectureRelation`, the architecture claim form, `ArchitectureQuestionCard@Project`, selected architecture-relevant structures, structure-kind recovery, architecture concern and admissible-use framing, exact inspected-material-use recovery, first architecture-question assignment, characteristic-claim assignment, small boundary notes, and the thin description bridge. It does not make descriptions or views conform merely by form and does not govern all architecture structure-kind views. Generic guards about publication, deontic permission, promise, evidence sufficiency, assurance, decision, gate passage, Work authorization, or release authorization stay in their direct patterns.

#### C.30:4.1 - Direct architecture relation and architecture claim

C.30 keeps one subject-side relation and one claim-bearing episteme distinct.

**Direct relation kind.** `ArchitectureRelation` is a C.30-governed direct dependent `U.Relation` between exactly two actual participants:

1. `architectureBearingHolonRef` — the exact `U.Holon` whose realized organization is at issue; and
2. `selectedArchitectureStructureRef` — one exact `U.Structure` selected under A.22 from declared constituents, obtaining subject-relation occurrences, applied constraints and invariants, and an admissible-use frame.

The relation is applicable only when the structure's exact constituents and selected subject-relation occurrences are recoverable for that holon or its admitted constituents and the structure is being used as architecture-relevant organization of that holon. Its obtaining predicate is satisfied only when the selected structure is actually constituted under A.22, every selected subject relation required by that structure obtains under its subject pattern, and those constituents and relations organize the exact holon in the declared way. A planned, required, desired, expected, modeled, diagrammed, listed, or merely published structure does not satisfy this predicate.

Occurrence identity is the exact participant pair over one maximal continuous interval during which that predicate remains satisfied. A different holon, a differently identified A.22 structure, or cessation followed by later renewed obtaining yields another occurrence. A changed concern, claim scope, effective reference scheme, description, viewpoint, view, representation, publication, or carrier does not by itself reidentify or create the relation. Ordinary prose may state the readable relation and stop; use A.6.REL only when a later receiver must distinguish this occurrence from another one.

**Architecture claim episteme.** `ArchitectureClaim` is an ordinary C.2.1 `U.Episteme`, not the direct relation and not a new architecture kind:

```text
ArchitectureClaim ::= {
  claimEpistemeRef: U.EpistemeRef,
  entityOfConcernRef:
    describedHolonRef | architectureRelationRef | selectedStructureRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue,
  claimScope?: U.ClaimScope, byValue,
  content: {
    describedHolonRef: U.HolonRef,
    architectureRelationAssertion:
      obtains | doesNotObtain | unresolved | candidateOrExpectedOnly,
    architectureRelationRefs?: FinSet(U.RelationRef),
    selectedStructureRefs?: FinSet(U.StructureRef),
    candidateOrExpectedStructureRefs?: FinSet(U.StructureRef),
    structureKindRefs: FinSet(ArchitectureStructureKindRef),
    architectureConcernClaimRefs?: FinSet(U.EpistemeRef),
    architectureConcernCue?: Plain recognition wording,
    admissibleUse,
    nonAdmissibleUse
  },
  modelUseStructureRef?: U.StructureRef,
  empiricalGroundingRelationRef?: U.RelationRef
}
```

The C.2.1 identity basis is the exact content, one exact `entityOfConcernRef`, and effective `U.ReferenceScheme`. `claimScope` qualifies what the claim covers. `modelUseStructureRef` appears only when one independently selected bounded-model-use structure changes structure interpretation or selection for this receiving use. `empiricalGroundingRelationRef` names a separately obtaining grounding relation; neither grounding nor the optional model-use structure is an `ArchitectureRelation` participant.

For an affirmative actual claim, every `architectureRelationRef` resolves to an obtaining occurrence governed by the direct settlement above and every `selectedStructureRef` is the exact structure participant of one of those occurrences. A negative, unresolved, candidate, required, desired, or expected claim can remain truthful claim content without an obtaining occurrence; it uses no invented positive reference. A description, diagram, graph, file, list, architecture decision, authoring act, or publication may state or carry the claim, but creates neither its truth nor the subject-side relation or structure.

Earlier consumers may still say “open the `ArchitectureOf@Context` form in the current C.30 edition.” In this edition that legacy retrieval instruction resolves to the `ArchitectureClaim` form plus the separate `ArchitectureRelation` settlement above. The suffix supplies no field, participant, scope, scheme, grounding, project identity, or relation fact, and new records use the current names.

**EntityOfConcern bridge.** C.30 may make the described holon, one exact `ArchitectureRelation` occurrence, or one exact selected structure the EntityOfConcern of a claim. A later architecture description independently chooses the exact holon, relation occurrence, or structure it describes under C.2.1; it does not use a claim record as a world-side proxy. Publication occurrences, forms, representations, and carriers remain separate.

#### C.30:4.1a - Holonic architecture modes

Recover which holonic architecture mode is current before applying MHT, structure, description, or mathematical-lens language:

| Mode | Current EntityOfConcern | Admissible C.30 use | Boundary |
| --- | --- | --- | --- |
| Direct holonic architecture mode | One exact `ArchitectureRelation` between a described holon and an actual selected structure, plus any C.2.1 claim about it. | Recover the actual subject relations, selected structure, architecture relation, structure kind, concern, admissible-use frame, and first move. | Do not apply MHT merely because the architecture has levels, scopes, parts, modules, or views. |
| Architecture-bound holon mode | An architecture residual raises a whole-reidentification question for a candidate result holon. | Use C.30 only for the actual-relation or modal-claim architecture residual; use `B.2` or `B.2.P` when whole reidentification is current. | `MHTTriggerProfile` is not a general architecture heuristic. |
| Non-holonic description, record, or mathematical mode | A description, view, diagram, dashboard, model, source relation, publication form, or mathematical-lens result is under repair. | Assign the claim to `C.30.AD`, `C.30.AD.BA`, `C.30.ASV`, `E.17`, `A.10`, `C.29`, or another subject pattern. | Do not treat the representation as the architecture or as MHT evidence by label. |

#### C.30:4.1b - Evolutionary-engineering architecture candidate bridge

Use this bridge when an open-ended search, quality-diversity archive, current pool, front, or selected set contains possible architecture moves. The archive or front is not yet an actual architecture relation. It becomes C.30 material only when the current claim names the described holon, the existing or candidate structure and structure kind, the affected architecture characteristic, and the next architecture move.

```text
ArchitectureCandidateMove:
  candidateMoveClaimEpistemeRef: U.EpistemeRef
  architectureClaimRef?: ArchitectureClaimRef
  describedHolonRef:
  currentArchitectureRelationRefs?: FinSet(U.RelationRef)
  currentSelectedStructureRefs?: FinSet(U.StructureRef)
  candidateStructureRefs: FinSet(U.StructureRef)
  candidateStructureKindRefs:
  affectedArchitectureCharacteristicRef:
  candidateMoveClaim:
  candidateSetOrArchiveRef:
  selectedSetResultRef?:
  localChoiceRef?:
  patternUseRecommendationRef?:
  workPlanRef?:
  workEntryReadinessRef?:
  gateDecisionRef?:
  performedWorkRef?:
  stopCondition:
```

`ArchitectureCandidateMove` is a thin claim note about a possible structural change. It records why a generated, retained, front-member, or selected-set variant can be considered as architecture material; it is not an obtaining `ArchitectureRelation`, work plan, local choice result, declared selected-set result, publication occurrence, decision, performed Work, or new kind. Candidate structure content remains modal until the exact structure is constituted and the direct architecture predicate obtains.

For common exits from this architecture question, use `C.18` for archive generation or front maintenance, `C.19` for current-pool treatment, `G.5` for selected-set result declaration, and `C.11` for local choice. If that result is made available to an audience, use `E.17` for a source-backed publication face and return to source, and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. Cite `E.11.PUR` for a recommended FPF pattern use. Use `A.15.2`, `A.15.5`, `A.21`, or `A.15.1` when the move enters planning, work-entry readiness, a gate decision, or performed Work. Keep only the architecture claim here: which holon and current relation are at issue, which candidate structure matters, which characteristic may change, and which next use is admissible.

Architecture-move wording creates no root `U.Move`, structure, relation, WorkPlan, readiness relation, gate decision, performed work, decision, or source-use claim by itself. When source wording uses “move” outside this architecture-candidate use, restore the concern through `E.10.MOVE` and name the subject pattern.

When the useful next work is synthesizing candidate architecture variants rather than judging or repairing one grounded actual relation, stop the C.30 question card after naming the described holon, the distinction between current and candidate structure, the structure kind, the concern, the admissible-use frame, and the next admissible use. Use `C.32` only to build the candidate architecture palette. When another claim becomes current, use the pattern that defines and tests it. For example, use `A.19.CPM` for comparison, `A.19.SelectorMechanism` for selector-policy use, `G.5` for selected-set result declaration, `C.11` for final local choice, `C.32.PAD` for a project architecture decision, `A.10` for evidence, `B.3` for assurance, `A.20` or `A.21` for a gate or release, and `A.15` for Work. For audience publication, use `E.17` for the source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability.

#### C.30:4.2 - Conditional architecture-description bridge

C.30 does not define a second local `ArchitectureDescription` record shape. The canonical C.2.1 episteme and its architecture-use specialization are governed by `C.30.AD:4.1`. C.30 admits only a thin bridge when durable description use changes the first architecture move.

The minimum bridge recoverable in C.30 is:

```text
C30ArchitectureDescriptionBridge minimum:
  architectureDescriptionRef: exact U.EpistemeRef
  entityOfConcernRef: exactly one described holon,
    obtaining ArchitectureRelation occurrence, or selected U.Structure
  effectiveReferenceScheme: U.ReferenceScheme, byValue
  architectureClaimRefs?: bounded claim content or trace
  selectedStructureRefs or structureKindRefs:
  architectureStructuralViewRefs?: only for exact description epistemes
    with independently obtaining E.17.0 viewpoint conformance
  viewpointConformanceRelationRefs?:
  admissibleUse:
  nonAdmissibleUse:
  correspondenceClaimOrRelationRefs or sourceReturnCondition?:
    only when reuse, cross-view use, or source return is needed
  freshnessClaimRefs?: only when currentness bounds admissible use
```

This bridge does not mint another description definition, local view-membership relation, subject-side architecture relation, selected structure, or truth fact. It lets the C.30 reader say why an exact description episteme matters for the next architecture move, then applies `C.30.AD` whenever the description itself becomes the EntityOfConcern under repair or the full mechanism is needed: multi-view description-set use, exact viewpoint conformance, correspondence, source return, freshness, specification-use boundary, representation/publication boundary, or reusable architecture-description use.

An architecture-description freshness claim is canonical in `C.30.AD:4.4`. C.30 may point to it only to bound admissible use of the first architecture move; it is not empirical grounding, publication currentness, evidence sufficiency, or assurance.

#### C.30:4.3 - Publication-use boundary

This subsection is the C.30 publication-use boundary. It says what an architecture description or its publication does not carry by itself, while the subject Solution stays about architecture claim, described holon, selected structures, structural views, and the next architecture move. If a guard concerns deontic permission, promise, prescription, evidence sufficiency, assurance, decision, gate passage, work authorization, release authorization, source authority, or publication-use authority, keep it here, in `C.30.AD`, or in the description or publication pattern governing that claim rather than expanding C.30's thin bridge.

```text
ArchitectureDescriptionPublication@Project ::= {
  sourceEpistemeRef | sourceViewRef,
  publicationViewpointRef?,
  publicationScopeId,
  claimScope?,
  effectiveReferenceScheme?,
  modelUseStructureRef?,
  mvpkFaceRef,
  publicationFormRef,
  sourcePinSetRef,
  audience,
  admissiblePublicationUse,
  nonAdmissiblePublicationUse
}
```

`ArchitectureDescriptionPublication@Project` is subordinate to E.17 and MVPK machinery. It publishes one source episteme or episteme-lane view reference. `publicationViewpointRef?` names the publication-side viewpoint only when MVPK needs one; it is not an architecture viewpoint and not a TEVB viewpoint. `mvpkFaceRef` is a publication-lane face reference, not an alternative source episteme, source view, or source relation. Publication does not establish non-publication claims; apply `C.30:4.3` and the subject pattern when evidence, gate, work, assurance, decision, or release claims are current.

Model cards, system cards, and evaluation harness reports enter C.30 through the same publication boundary or source-relation boundary. They may describe a model, deployed AI system, architecture claim, evaluation harness, or policy, but the architecture move still needs the actual/candidate structure distinction, an obtaining `ArchitectureRelation` only when its predicate is satisfied, a bounded `ArchitectureClaim` when claim content is needed, and any proof, release, or gate claim assigned to its subject pattern.

```text
ModelCardOrSystemCardBoundaryNote@Project ::= {
  sourcePublicationRef,
  entityOfConcernRef,
  entityOfConcernKind:
    model | deployedAISystem | architectureClaim |
    evaluationHarness | policy | otherDeclared,
  architectureStructureKindRefs?,
  intendedUseScope,
  evaluationScopeAndKnownLoss?,
  deploymentInterpretationOrUseMismatch?,
  evidenceOrAssurancePatternLocator?,
  nonAdmissibleUse:
    notArchitectureAdequacy | notSafetyProof |
    notReleaseAuthorityByPublicationAlone
}
```

If the card or harness is used beyond transparency, recover the architecture structure kind being used first and then apply `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `C.16`, `C.28`, or `C.11` for the non-architecture claim kind.

#### C.30:4.4 - Architecture name formation

The word `architecture` is shorthand only after the described holon, selected structures, structure kind, architecture concern and admissible-use frame, and exact use of inspected material as source, description, view, representation, or publication form are recoverable. Without those qualifiers, it is a recovery trigger, not a stable FPF term.

```text
ArchitectureNameFormationRule:

If a text says "<X> architecture", then the FPF-governed use is conforming only with:
  describedHolonRef,
  actual subject relation occurrences or an explicit candidate/expected stop,
  architectureRelationRefs only when those exact relations obtain,
  claimScope? when claim coverage changes use,
  effectiveReferenceScheme for any claim episteme,
  modelUseStructureRef? only when that structure changes interpretation or selection,
  structureKindRef = <X>StructureKind or a declared local classifier,
  actual selectedStructureRefs or separately named candidateOrExpectedStructureRefs,
  architectureStructuralViewRefs only when a conforming view episteme is being used,
  admissibleUse,
  nonAdmissibleUse.
If <X> is not a declared structure kind, the phrase is plain recognition wording only.
```

| Phrase | Required recovery |
| --- | --- |
| functional architecture | `structureKindRef = FunctionalStructure`; functions, effects, capabilities, and functional dependencies named as structure content; transformation-flow structures, paths, and flow valuations are assigned to `TransformationFlowStructure` or `C.30.TFS-REL`. |
| modular architecture | `structureKindRef = ModuleInterfaceStructure`; module claim content, selected dependency structure, interface specifications, substitutability rule, and change policy. Cite a direct module relation only after its exact predicate is defined and current facts make it obtain; current A.6.M `moduleIn(...)` syntax is claim content. |
| logical architecture | `structureKindRef = DeclaredLogicalStructure`; local definition says whether `logical` means information relation, functional relation, runtime relation, responsibility relation, allocation relation, or another relation class. |
| physical architecture | `structureKindRef` in `{MaterialSpatialStructure, PlacementDeploymentStructure}` or a locally declared physical structure kind. |
| control architecture | `structureKindRef = ControlStructure`; an LCA record may describe the control structure, but proof claims are assigned to dynamics, temporal, causal, evidence, safety, or assurance patterns as triggered. |
| information architecture | `structureKindRef = InformationDataStructure`; state bearer and residence, schema refs, semantic refs, persistence locus, provenance relation, custody relation, and source-return conditions. |
| security architecture | `structureKindRef = SecurityTrustBoundaryStructure`; recover protected asset or effect, trust boundary, adversarial path, authority or privilege relation, secure-default or hardening boundary, and evidence, assurance, or gate subject patterns when those claim kinds are being made. |

#### C.30:4.5 - Architecture characteristic assignment

C.30 recovers the exact bearer before any `quality`, `fitness`, `measure`, `metric`, `score`, `modularity`, or `ility` wording carries an architecture-adequacy claim. Those words are triggers, not stable architecture adequacy by themselves.

```text
ArchitectureCharacteristicAssignment:

A. SystemQualityAffectedByArchitecture
   Bearer: exact described U.Holon, named product holon, or named system holon
   Subject pattern: C.25 Q-Bundle or C.16
   Examples: maintainability, evolvability, resilience, availability, safety, observability

B. ArchitectureStructuralCharacteristic
   Bearer: one exact selected U.Structure, obtaining ArchitectureRelation,
           actual subject relation or constraint, or separately admitted
           module/interface relation
   Subject pattern: C.16, A.17-A.19, C.25, or the direct
                      characteristic-space or Q-bundle pattern
   Examples: coupling, cohesion, interface alphabet, substitutability,
             hidden coupling, reusable-structure share

C. ArchitectureDescriptionOrViewAdequacy
   Bearer: one exact architecture-description episteme, one exact view episteme,
           one exact correspondence model, or one exact publication-use object
   Subject pattern: C.30.AD, C.30.ASV, E.17.0, E.17, C.16.Q, or C.16
   Examples: viewpoint coverage, correspondence adequacy,
             source-return adequacy, description modularity
```

An `ArchitectureClaim` may state a characteristic claim, but the claim episteme is not automatically the characteristic bearer when its content names the holon, direct architecture relation, or selected structure. Select the exact bearer under the characteristic's subject pattern. Likewise, a diagram or publication cannot inherit the subject's quality by describing it.

C.30 keeps only a thin bridge from structural characteristics to Q-Bundle relevance. If the claim says architecture causes an outcome improvement, assign causal use to `C.28`. If a structural characteristic is used as a mechanism, constraint, predictor, proxy, evidence relation, or causal hypothesis for a Q-Bundle slot, start with `ArchitectureStructuralCharacteristicQBundleClaimLine` rather than a formula such as `low coupling = maintainability`.

`ArchitectureStructuralCharacteristicQBundleClaimLine` is claim content for first contact, not a `U.Relation` occurrence or reusable relation declaration:

```text
ArchitectureStructuralCharacteristicQBundleClaimLine ::= {
  architectureClaimRef?: ArchitectureClaimRef,
  entityOfConcernRef:
    architectureBearingHolonRef | architectureRelationRef |
    selectedStructureRef | directStructuralRelationRef |
    structuralCharacteristicRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue,
  claimScope?: U.ClaimScope, byValue,
  structuralCharacteristicCueOrRef,
  affectedQBundleSlotRef,
  relationClaimKind:
    structuralCharacteristicRelevantToQBundleSlot |
    structuralCharacteristicConstrainsQBundleSlot |
    structuralCharacteristicPredictsQBundleSlot |
    structuralCharacteristicProxiesQBundleSlot |
    structuralCharacteristicCausalHypothesisForQBundleSlot |
    structuralCharacteristicEvidenceRelationForQBundleSlot,
  relationGroundingKind:
    modelBased | empirical | causalModelBased | expertJudgement |
    sourceLineageOnly | SoTAActionLineage | reportOnly,
  directRelationDisposition:
    noDirectRelationClaimed | exactDirectOwnerAndOccurrenceRefs |
    directOwnerStillNeeded,
  directRelationOccurrenceRefs?: FinSet(U.RelationRef),
  evidenceOrCausalPatternLocator?,
  nonAdmissibleUse
}
```

The line supports an inspectable next question without claiming measurement, modularity score, evidence sufficiency, assurance, gate passage, or causal proof. `exactDirectOwnerAndOccurrenceRefs` is available only when the direct characteristic, evidence, or causal pattern supplies its participant meanings, obtaining predicate, applicability, and occurrence identity and the referenced occurrences actually obtain. If no subject pattern exists for a needed reusable relation, use A.6.RCD; neither a local token nor this line admits one.

Minimal structural-characteristic claim-line examples:

| Structure kind | Structural characteristic cue or relation | Affected Q-Bundle slot | Relation grounding note | Non-admissible use |
| --- | --- | --- | --- | --- |
| `ModuleInterfaceStructure` | Stable interface specification plus substitution policy. | Evolvability or replaceability. | Replacement without global retesting. | Open label as substitutability proof. |
| `PlacementDeploymentStructure` | Controller placed near plant or edge-node locality. | Latency, resilience, or jurisdictional compliance. | Reduced communication delay and bounded data custody. | Placement diagram as performance or regulatory acceptance proof. |
| `InformationDataStructure` | State bearer, residence, provenance, and custody boundary. | Observability, privacy, or auditability. | Recoverable state lineage and bounded custody. | Data schema as evidence sufficiency. |
| `MaterialSpatialStructure` | Physical separation, adjacency, or energy path. | Safety, maintainability, or energy efficiency. | Isolation, accessibility, or loss reduction. | Geometry as safety proof. |
| `ControlStructure` | Observer-controller-plant loop with rate envelope. | Stability, controllability, or safety. | Feedback and bounded actuation relation. | Control diagram as proof. |
| `TransformationFlowStructure` | Path crossing, bottleneck, buffer boundary, or waiting-line boundary. | Latency, throughput, or resilience. | Recoverable path, crossing, capacity, and valuation relation. | Flow diagram or mathematical graph description as performance or causal proof. |
| `SecurityTrustBoundaryStructure` | Trust boundary, privilege path, or untrusted-input crossing. | Security, abuse resistance, or privacy. | Reduced exposed authority and bounded trust crossing. | Risk color or compliance label as security proof. |
| `EvidenceAssuranceStructure` | Evidence package reused across variants. | Assurance maintainability or release readiness. | Explicit affected-structure and source-return boundary. | Evidence-structure view as assurance verdict. |
| `WorkMethodStructure` | Method description, work plan, or work enactment relation with explicit exception path. | Operability, auditability, or maintainability. | Bounded repeatability and recoverable exception handling. | Work-method diagram as work authorization or evidence sufficiency. |

`ArchitectureCharacteristicQBundleClaim` is the triggered full claim episteme. Use it only when publication, comparison, causal use, evidence reliance, assurance, gate, decision, or reusable cross-case reliance needs a durable bounded claim and the thin line cannot keep the content inspectable.

```text
ArchitectureCharacteristicQBundleClaim ::= {
  claimEpistemeRef: U.EpistemeRef,
  entityOfConcernRef:
    architectureBearingHolonRef | architectureRelationRef |
    selectedStructureRef | directStructuralRelationRef |
    structuralCharacteristicRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue,
  claimScope?: U.ClaimScope, byValue,
  architectureClaimRef?: ArchitectureClaimRef,
  architectureStructuralViewRef?,
  architectureDescriptionRef?,
  structuralCHRRefs,
  affectedQBundleRefs,
  assertedParticipantRefs: {
    structuralCharacteristicRef,
    qBundleSlotRef
  },
  relationClaimPolarity:
    positive | negative | unresolved | candidateOnly,
  relationClaimKind:
    structuralCharacteristicRelevantToQBundleSlot |
    structuralCharacteristicConstrainsQBundleSlot |
    structuralCharacteristicPredictsQBundleSlot |
    structuralCharacteristicProxiesQBundleSlot |
    structuralCharacteristicCausalHypothesisForQBundleSlot |
    structuralCharacteristicEvidenceRelationForQBundleSlot,
  relationGroundingKind:
    modelBased | empirical | expertJudgement |
    sourceLineageOnly | SoTAActionLineage | causalModelBased | reportOnly,
  directRelationDisposition,
  directRelationOccurrenceRefs?: FinSet(U.RelationRef),
  scopeOrScaleWindow?,
  viewpointRef?,
  qualifiers?,
  witnessExpectations?,
  admissibleSemanticChangeClasses?,
  bridgeOrLossBoundary?,
  admissibleUse,
  nonAdmissibleUse,
  evidenceOrCausalPatternLocator?
}
```

The full claim preserves the older branch's inspectable proposal detail: assertion polarity, the exact structural-characteristic and Q-Bundle-slot referents, scope or scale window, viewpoint when it changes interpretation, qualifiers, witness expectations, admissible semantic change classes, and bridge or loss boundary. These are claim-content fields. They neither declare a reusable relation kind nor make an occurrence obtain; a direct relation still needs an admitted kind, exact participants, a defining predicate and applicability rule, and occurrence identity.

Reusable product-quality vocabularies may supply candidate characteristic names, but they do not become architecture theory. The claim content may connect exact bearers and Q-Bundle slots; only the subject pattern makes a relation obtain. Measurement, modularity scoring, reusable-structure accounting, bespoke-residue accounting, evidence, assurance, gate, causal, and scale-audit claims stay with their subject patterns.

#### C.30:4.6 - Relation to structural views

`C.30.ASV` governs structural-view adequacy for an exact architecture-description episteme about one selected structure; E.17.0 alone admits that same episteme as `U.View` through independently obtaining conformance to an exact viewpoint. C.30 governs direct `ArchitectureRelation` occurrences and bounded `ArchitectureClaim` content and, only when durable description use is being made, how its thin `ArchitectureDescription` bridge cites exact structural views. Hidden/lost structure, correspondence, source or reliance relations, and source-return boundaries stay explicit when they affect action. `C.30.AD` governs the full description mechanism.

A diagram, model, table, selected transformation-flow diagram, mathematical graph description, LCA diagram, C.29 lens output, ADR, dashboard, generated explanation, or other publication face may carry an architecture description or an architecture structural view. It does not become the architecture, and it does not become a conforming view only because it looks like a view.

Use `AffectedArchitectureStructureNote` when the next architecture move needs to name affected structures or view losses without using an architecture decision, ADR, gate, evidence, assurance, or release record:

```text
AffectedArchitectureStructureNote:
  architectureClaimRef:
  affectedStructureKindRefs:
  affectedStructureRefs?:
  affectedArchitectureStructuralViewRefs?:
  acceptedOrSuspectedViewLoss?:
  sourceReturnCondition?:
  nextAdmissibleUse:
```

This note only names affected architecture structure for the next architecture use. Decision, ADR, gate-passage, evidence-sufficiency, and release-authorization claims apply the patterns define or constraining those claims.

#### C.30:4.7 - Minimal boundary notes

Use these notes when a common architecture phrase is close to a subject pattern but the full subject-pattern application is not yet needed for an asserted claim.

Use the thinnest claim or boundary form that preserves the next architecture move. Use a fuller governing claim or relation record only when the content or independently admitted relation being used cannot be inspected, compared, refreshed, or bounded without it. Typical thin forms are `ArchitectureMathLensUseBoundary` before C.29 Mini or Full, `AffectedArchitectureStructureNote` before an architecture decision record, and `ArchitectureStructuralCharacteristicQBundleClaimLine` before full measurement, causal, evidence, or reusable direct-relation records.

```text
InterfaceSignatureBoundaryNote ::= {
  phraseOrArtifactRef,
  apparentClaim:
    interface | signature | port | endpoint | connector | link |
    API | protocol | E.18 transformation-flow relation | E.18 transformation-flow path | mechanism reference,
  recoveredKind,
  governingPatternApplicationRefs,
  admissibleUse,
  nonAdmissibleUse
}

ModuleRelationBoundaryNote ::= {
  phraseOrArtifactRef,
  apparentClaim:
    module | component | package | platform | open architecture |
    recoveredModuleInterfaceSourceLabel |
    typed control-structure relation,
  moduleInterfaceRepairClaimCurrent?: yes | no,
  openOrPlatformClaimCurrent?: yes | no,
  selectedModuleInterfaceRelationRefs?,
  variationPointRef?,
  substitutabilityPolicyRef?,
  interfaceConformanceEvidencePatternRef?,
  changePolicyOrRelationRef?,
  consumerMigrationBoundary?,
  versionOrUpdateChannelRef?,
  secureDefaultOrHardeningBoundary?,
  governingPatternApplicationRefs,
  admissibleUse,
  nonAdmissibleUse
}
```

These notes are not substitutes for the module-and-interface repair pattern named by value, interface specifications, signature records, conformance evidence, or module-and-interface repair. An open or platform label is not substitutability proof, security proof, scale proof, assurance, or universal maturity evidence. A source label such as `layer`, `stack`, `block`, `expert`, `cache`, `router`, or `gate` enters this note only after `C.30.STRAT` recovers a module-interface or adjacent architecture-relevant item. It becomes architecture-relevant only through local structure, interface, variation, substitution, migration, update, and hardening boundaries. Relation-heavy wording inside these notes remains a Plain cue until a module relation reference named by value, interface relation ref, relation governing the asserted use record, or governing FPF pattern application is named. The note keeps first use honest until the non-architecture claim kind named by value is being made.

#### C.30:4.8 - Architecture mathematical-lens boundary

Architecture descriptions may use C.29 lenses, but the lens does not become architecture ontology.

```text
ArchitectureMathLensUseBoundary:
  noMLUNeeded?: yes | no
  lensOneLine?:
    lensRef,
    structureClaimRef,
    preservedStructure,
    lostStructure,
    lensRelationKind,
    stopCondition,
    governingPatternApplicationRefs?
```

Use the one-line boundary only when it is enough to keep the lens from being overread. Use a C.29 Mini or Full card when the lens choice, preserved structure, lost structure, relation class or admissible-use value, or stop condition changes the architecture move.

Lens use by architecture problem:

| Architecture problem | Candidate mathematical lens | Preserved structure | Typical loss or stop |
| --- | --- | --- | --- |
| Hidden dependency or modularity. | Typed graph, DSM, or hypergraph. | Dependency, coupling, or clustering. | Semantics, interface law, evidence, and work remain outside unless bridged. |
| Flow bottleneck. | Transformation-flow structure, network flow, or queueing. | Path, crossing, valuation, and capacity. | Purpose, proof, causality, and safety remain non-architecture claims. |
| Control-rate mismatch. | LCA, hybrid systems, assumption-guarantee relations, or control relations. | Feedback participant meanings and scale or rate relations. | Stability proof and safety proof remain outside the lens. |
| Cross-scope residual. | Coarse-graining or renormalization-group-style lens. | Preserved and lost structure across scale. | Utility, causal-use claims, and selector authority remain outside unless separately grounded. |
| Extracted structure from traces. | Epiplexity or MDL-style bounded-observer lens. | Learnable structural regularity. | Task relevance, assurance, and causal proof remain non-architecture claims. |
| Physical separation or spatial arrangement. | Topology, geometry, or spatial graph lens. | Adjacency, containment, separation, reachability, energy-transfer relation, or material-transfer relation. | Safety proof, accessibility, regulatory acceptance, and causal-use claims remain outside unless separately grounded. |
| Composition relation. | Category, open-systems, or compositional lens. | Interface, composition, and coherence. | Domain semantics remain outside unless bridged. |

This table is not a C.29 replacement and does not make mathematics mandatory. It helps the practitioner see when a lens may add a useful architecture move; C.29 still carries lens-use result, preserved structure, lost structure, relation class or admissible-use value, and stop condition when those description or view uses are being made.

Epiplexity-like use remains a C.29 bounded-observer structural-information lens. It may help recover learnable structure from traces, but it is not an architecture quality, task relevance proof, causal proof, assurance, or selector authority.

#### C.30:4.9 - Boundary and repair table

| Tempting collapse | C.30 repair |
| --- | --- |
| Bare architecture as free-floating selected claim | Recover the actual subject-relation occurrences and exact A.22 structure, then either identify the obtaining `ArchitectureRelation` or keep candidate, expected, negative, or unresolved content in `ArchitectureClaim`. Also recover the exact described holon, structure kind, concern and admissible-use frame, effective reference scheme and ClaimScope when applicable, and the exact source, description, view, representation, publication-form, or other direct use of inspected material. |
| Architecture description as architecture | Keep `ArchitectureDescription` as a C.2.1 episteme about one exact holon, obtaining `ArchitectureRelation`, or selected structure; keep specification use, representation, and publication separate. |
| Diagram, model, table, dashboard, or generated relation graph as architecture | Treat it as publication form, description, view, source relation, or source-finding aid only when that relation is explicit. |
| Module diagram as all architecture | Use `C.30.ASV` to recover structure kind; module structure and interface relation are only one structure family. |
| Transformation-flow structure or graph description as architecture | Use E.18 for selected transformation-flow structure, path, and crossing records; use E.18.2 and C.29 for mathematical graph descriptions; use C.30.TFS-REL for the architecture-to-transformation-flow relation. |
| LCA diagram or control diagram as proof | Use `C.30.LCA` for control-structure view; assign dynamics, temporal, causal, evidence, gate, safety, and assurance claims to their subject patterns. |
| Mathematical lens as architecture ontology | Use `C.29`; cite `MathLensUseOutputRef` only through an `ArchitectureMathLensUseBoundary` or C.29 lens record and state stop condition. |
| ADR as architecture decision | Use the project-side architecture decision pattern when a decision claim is being made; ADR is a publication form, not the decision. |
| Quality, score, or measurement term as architecture adequacy | Recover the bearer through ArchitectureCharacteristicAssignment; assign the claim being made to C.25, C.16, A.17-A.19, the characteristic-space or Q-bundle pattern governing the characteristic claim, or C.30 grounded architecture, selected-structure, or conditional description-use scope. |
| Architecture record as evidence, assurance, gate, work, or release | Assign evidence, assurance, gate, work, or release claims to A.10, G.6, B.3, A.20, A.21, A.15, or the release locus named by value when a release claim is being made. |
| Architecture as agent, worker, controller, gate, or proof | Split the claim. If action or Work is meant, identify the performer System, dated Work, enacted Method, assignment occurrence and its declared species, and F.6 attribution. Recover mechanism or control relations, permission, authority, responsibility, gate results, evidence, assurance, proof, and guarantees only through their own predicates or results. A local system-role kind or assignment may be a neighboring fact but neither acts nor establishes any of those stronger claims. Neither an `ArchitectureRelation`, its selected structure, nor `ArchitectureClaim` is an acting entity by wording alone. |

**Currentness and smallest reopen.** When a decisive input changes, reopen only the C.30 object and use conclusion that depend on it. A changed holon or obtaining subject relation reopens the affected selected structure and, if asserted, the direct `ArchitectureRelation` predicate; a changed selected structure or predicate result reopens that relation occurrence and any affirmative `ArchitectureClaim` reference; a changed claim scheme or `ClaimScope` reopens only that claim; and a changed description, view, or source edition, admissible-use boundary, or direct governor reopens its exact reference and dependent `ArchitectureQuestionCard@Project` disposition. Admissible results are to update the affected reference or claim mode, narrow use, re-run the direct predicate, or reopen the card when its next architecture move is no longer supported; unrelated structures, descriptions, and claims stay closed.

#### C.30:4.10 - Worked slices

**"We have the architecture in this diagram."** The diagram is a representation or publication form. It creates neither architecture nor `U.View`; recover an exact `ArchitectureDescription` episteme and, when view use is claimed, its independently obtaining E.17.0 conformance relation.

```text
ArchitectureQuestionCard@Project:
  describedHolonRef: payment system
  claimScope: checkout-platform architecture use
  effectiveReferenceScheme: checkout-platform architecture terms
  architectureConcernCue: descriptionViewLoss or flowBottleneck
  sourcePhrase?: "architecture in this diagram"; unclear dependency between payment orchestration and fraud scoring
  questionDisposition: architectureClaimReady
  architectureRelationDisposition: actualRelationStillToRecover
  inspectedMaterialUse: publication form carrying possible architecture structural-view material
  inspectedMaterialUseRelationRefs: exact publication occurrence or representation relation when independently current
  selectedStructureKindRefs: FunctionalStructure, ModuleInterfaceStructure, TransformationFlowStructure
  firstArchitectureMove: recover the diagram as a publication face and create a minimal architecture structural-view note
  governingPatternApplicationRefs: C.30.ASV
  non-admissible overread: treating the diagram as architecture itself, evidence, assurance, gate passage, or decision
```

**"Low coupling gives maintainability."** C.30 does not allow that formula to carry the claim by itself. The ordinary repair starts with the thin claim line:

```text
ArchitectureStructuralCharacteristicQBundleClaimLine:
  architectureClaimRef: ArchitectureClaimRef
  entityOfConcernRef: selected module-interface structure or its exact structural-characteristic referent
  effectiveReferenceScheme: module-interface and maintainability terms used by this claim
  structuralCharacteristicCueOrRef: coupling under module claim, admitted direct module relation, or interface relation as actually grounded
  affectedQBundleSlotRef: maintainability Q-Bundle slot
  relationClaimKind: structuralCharacteristicRelevantToQBundleSlot
  relationGroundingKind: sourceLineageOnly | SoTAActionLineage | modelBased, as actually grounded
  directRelationDisposition: noDirectRelationClaimed | exactDirectOwnerAndOccurrenceRefs | directOwnerStillNeeded
  evidenceOrCausalPatternLocator?: one selected subject pattern reference: C.28, B.3, A.10, or G.6 when evidence sufficiency, causal-use, assurance, or safety-case claim is being made
  nonAdmissibleUse: causal proof, assurance, or direct relation by slogan
```
Use `ArchitectureCharacteristicQBundleClaim` only when publication, comparison, causal use, evidence reliance, assurance, gate, decision, or reusable cross-case claim reliance needs the fuller bounded claim. If repeated use needs an independently admitted direct characteristic, evidence, or causal relation, its subject pattern must first supply the participants, obtaining predicate, applicability, and occurrence identity; the useful move is not to accept the slogan as architecture truth.

**"The backup-pump architecture is safe because the loop is redundant."** C.30 starts with the plant holon, operating claim scope, effective reference scheme when local terms need it, and selected structures: control loop, material-flow structure, placement structure, module-interface relation, and maintenance-work relation. The redundancy phrase may motivate an architecture move, but safety proof, causal proof, evidence sufficiency, gate passage, and work authorization go to their subject patterns. The C.30 output is the selected structure and next architecture move, not a safety case by slogan.

**"We replaced the neural-network block, so the architecture improved."** Treat `block` first as a source label and apply `C.30.STRAT` unless the changed value is already recovered. The phrase is admissible architecture recognition only after the changed structure kind, transformation-flow relation, module or interface claim kind, preserved and lost structure, changed characteristic, source relation, and decision or evidence subject patterns are named. A block label, benchmark result, ablation, pruning mask, or distillation result is not an architecture decision, evidence sufficiency, gate passage, assurance, or architecture adequacy by itself.

### C.30:5 - Archetypal Grounding

| Tell-Show-Show row | Grounding |
| --- | --- |
| Tell | A project team says "architecture" while looking at a diagram, model, generated relation graph, ADR, or module list. C.30 asks which subject relations actually obtain, which A.22 structure is selected, whether the direct architecture relation obtains or the content is candidate or expected only, how the inspected material is being used, and what architecture move remains admissible. |
| Show: `U.System` | A payment system, plant, vehicle, product platform, AI-agent system, or neural-network model has actual subject relations from which functional, flow, control, module-interface, information, placement, scale, work, evidence, or declared logical structures can be selected. When the C.30 predicate is satisfied, the exact selected structure stands in an `ArchitectureRelation` to that holon; a claim or publication about it is not the relation. |
| Show: `U.Episteme` | An `ArchitectureClaim`, architecture description, model, view, generated relation graph, ADR-like note, safety-case view, or dashboard is an episteme or publication-side object. It can state or describe actual, negative, unresolved, candidate, or expected content and can participate in source or grounding relations, but it does not create the selected structure, `ArchitectureRelation`, evidence sufficiency, gate result, assurance case, or project decision. |

### C.30:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto**, **Epist**, **Prag**, **Did**, **Gov**. Scope: FPF architecture-description use over holons.

| Bias risk | Mitigation |
| --- | --- |
| Module-diagram bias | Keep module structure and interface relation as one structure family among several; use `C.30.ASV` and the module-and-interface repair pattern when a module or interface claim is being made. |
| Tool-model bias | Treat notation, tool model, generated relation graph, diagram, and dashboard as description, specification-use, or publication forms unless an exact direct relation gives the source material a more specific use. |
| Check-only bias | The first output is an architecture question card plus action palette, not a checklist that only detects mistakes. |
| Assurance or gate bias | Architecture descriptions do not certify safety, evidence sufficiency, release, or gate passage; assign those claims to the subject patterns. |
| Didactic-thinning risk | Semantic repair preserves why the distinction matters: the pattern begins with the practitioner situation, payoff, stop condition, and first architecture move. |

This checklist verifies the preceding guidance after the practitioner has chosen the selected architecture candidate use; it is not a required project control form and not a substitute for the card, note, view, relation, or repair use above.

### C.30:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-C30-1 Grounded architecture name.** | An FPF-governed use distinguishes actual subject relations and selected A.22 structure from candidate or expected content, identifies an obtaining `ArchitectureRelation` only when its predicate is satisfied, and gives every `ArchitectureClaim` one exact EntityOfConcern and effective reference scheme. It also names concern, admissible-use frame, and the exact source, description, view, representation, publication-form, or other direct use of inspected material. | Rewrite through `ArchitectureQuestionCard@Project`; recover the direct relation, retain modal content only in the claim, or demote the phrase to Plain recognition wording. |
| **CC-C30-2 No `U.Architecture`.** | The pattern use does not mint or rely on a root `U.Architecture`. | Recover exact A.22 structure and the direct `ArchitectureRelation`, or keep candidate/expected content in a claim and handle any other claim under its subject pattern. |
| **CC-C30-3 EntityOfConcern and Description-episteme boundary plus specification-use separation.** | Actual subject relation, selected structure, `ArchitectureRelation`, claim, description, view, representation, publication occurrence/form/carrier, decision, evidence, and Work stay distinct. | Recover the exact object doing each job; a description, specification use, diagram, list, file, or publication creates no subject-side architecture fact. |
| **CC-C30-4 Exact description subject.** | Every architecture description has one exact C.2.1 EntityOfConcern—holon, obtaining `ArchitectureRelation`, or selected structure—and effective `U.ReferenceScheme`; architecture-claim refs remain optional content or trace. | Recover the exact subject and scheme, or split the description from the bounded architecture claim. |
| **CC-C30-5 View and publication boundary.** | The same description episteme is `U.View` only through an independently obtaining E.17.0 conformance relation to one exact viewpoint; representation, publication occurrence, form, carrier, and publication currentness remain separate. | Apply `C.30.AD`, `E.17.0`, C.29, and E.24.PUB to the exact objects; remove any view membership inferred from authoring, query, bundle, diagram, file, rendering, or publication. |
| **CC-C30-6 Small output before heavy record.** | Ordinary use may stop at `ArchitectureQuestionCard@Project` when one next architecture move and subject-pattern application is clear. | Remove needless full-record expansion or explain which full-mode trigger is present. |
| **CC-C30-7 Structure-kind boundary.** | Structural-view claims apply `C.30.ASV`; module, function, flow, control, work, evidence, scale, and decision claims do not collapse into C.30. | Name the structure kind, state the structural view if needed, or assign the claim to the subject pattern. |
| **CC-C30-8 Characteristic assignment.** | Quality, measure, score, metric, modularity, and `ility` wording recovers its bearer and subject pattern before use. | Add `ArchitectureCharacteristicAssignment`, or narrow the sentence to ordinary non-FPF-governed recognition. |
| **CC-C30-9 Non-architecture claim kind.** | Evidence, assurance, causal, gate, work, decision, publication-use authority, mathematical-lens, measurement, and release claims are assigned to their subject patterns. | The check passes when the governing FPF pattern and the claim kind being made are named, while the C.30 record remains limited to architecture and selected-structure adequacy. |
| **CC-C30-10 Useful action.** | The repaired wording leaves a surviving admissible action: name the architecture claim, recover the exact use of inspected material, state an architecture structural view, add a source or reliance relation, add a `SourceReturnCondition`, or apply the FPF pattern that defines or constrains the claim kind being made. | Restore that action, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

### C.30:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Architecture-as-document** | A document, diagram, table, generated relation graph, or dashboard is treated as the architecture or as what makes `ArchitectureRelation` obtain. | Recover the representation/publication objects, exact claim episteme, selected structure, and actual direct relation separately; a carrier creates none of their subject-side facts. |
| **Publication-unit architecture drift** | One publication unit mixes architecture description, evidence claim, gate decision state, decision note, and work authorization under one architecture heading. | Name the exact `ArchitectureRelation` or modal `ArchitectureClaim` content, keep description/view and publication objects separate, and assign evidence, gate, decision, and work claims to their direct patterns. The publication heading creates no selected structure or subject-side relation. |
| **Module-diagram takeover** | Architecture is reduced to module structure or interface relation. | Recover structure kind and use `C.30.ASV`; assign full module repair to the module-and-interface repair pattern when that claim kind is being made. |
| **Tool-model lock-in** | A notation or tool model becomes the source of architecture truth. | Recover FPF architecture claim, structures, views, correspondence, and source-return condition. |
| **Evidence laundering** | A published architecture description is used as evidence sufficiency. | Assign the evidence relation or evidence claim to `A.10` or `G.6`; C.30 keeps only the architecture claim, selected-structure, and conditional architecture-description-use boundary; the evidence relation stays with the evidence pattern. |
| **Assurance or safety overread** | Architecture description or LCA diagram is used as assurance or safety case. | Assign the claim being made to `B.3`, `A.10`, `G.6`, `C.30.LCA`, or the safety-case or gate pattern governing the claim when that claim kind is being made. |
| **Risk color as architecture decision** | A red, yellow, or green risk cell, risk matrix, or maturity score decides the architecture move or resource-allocation priority. | Recover the structure kind under consideration, affected scope, loss, hazard, or threat path, source relation or grounding relation, characteristic scale, comparator, and gate pattern; architecture adequacy, evidence sufficiency, causal proof, assurance proof, resource-allocation reason, and gate-passage claims stay with their subject patterns. |
| **Causal slogan** | Architecture property is said to cause a quality without a bounded claim or independently admitted relation grounding. | Start with `ArchitectureStructuralCharacteristicQBundleClaimLine`; apply C.28, evidence, causal-use, or assurance pattern, or use `ArchitectureCharacteristicQBundleClaim` when a durable bounded claim is needed. A direct relation appears only under its subject pattern and only when it actually obtains. |
| **Architecture-operation overread** | Replacing a block, module, layer, protocol, cache, memory path, or flow relation is treated as improvement by label alone. | Apply `C.30.STRAT` to source labels, then recover changed structure kind, preserved structure, lost structure, source relation, affected characteristic, and decision or evidence subject pattern. |
| **Sterile compliance rewrite** | The text becomes well typed but no longer helps the practitioner act. | Restore `ArchitectureQuestionCard@Project`, a concrete next architecture move, or a named subject-pattern application. |

### C.30:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| Actual architecture relations and modal architecture claims become separable from diagrams, publications, generated relation graphs, ADRs, module lists, and decisions. | A conforming use recovers actual subject relations, selected A.22 structure, direct-relation disposition, exact claim EntityOfConcern and effective reference scheme, and the exact inspected-material use when relevant. |
| The pattern enables first-principles architecture reasoning without forcing full measurement, synthesis, assurance, or decision machinery. | Some familiar architecture phrases become triggers for quick recovery rather than accepted claims. |
| Functional, flow, control, module structure, interface relation, information structure, placement structure, scale structure, work structure, evidence relation, and declared logical structures can coexist without one structure kind swallowing the rest. | Structural-view adequacy is governed by `C.30.ASV`, so practitioners can require an explicit view application. |
| C.29, E.18, LCA, module-and-interface repair, evidence, assurance, and gate patterns can supply source or reliance relations for architecture work without becoming architecture ontology. | Subject pattern applications are named by value whenever a source or reliance relation is used beyond C.30 architecture claim, selected-structure, or conditional description-use scope. |

### C.30:10 - Rationale

Architecture is most useful in FPF when it stays close to actual selected structure over a holon and far away from document-as-architecture, graph-as-architecture, model-as-architecture, and decision-as-architecture collapses. The direct `ArchitectureRelation` keeps the exact holon and actual selected structure together without minting `U.Architecture`; an `ArchitectureClaim` gives practitioners a claim-bearing handle for affirmative, negative, unresolved, candidate, or expected content without substituting that episteme for the relation.

C.30 and C.30.ASV establish an FPF architecture kernel: actual subject relations first; exact selected A.22 structure; direct `ArchitectureRelation` to the described holon; separately constituted claim, description, viewpoint, and view epistemes; structure-kind discipline; correspondence and source-return boundaries; and characteristic-claim applications. They do not by themselves provide full measurement, synthesis, decision, causal proof, safety proof, or assurance.

The small first card is deliberate. Architecture discussions often need one immediate architecture move: name the holon, choose the structure kind under consideration, recover the exact use of inspected material, assign an evidence or assurance claim to its subject pattern, or stop. A full architecture description is useful only when durable publication, cross-team use, comparison, regulated use, source reuse, or reliance-relation reuse is being made.

Exact episteme identity and direct view conformance also preserve plurality. The same holon, architecture-relation occurrence, or selected structure may be described by several independently identified epistemes; one episteme may conform to several exact viewpoints through distinct occurrences; several publications may render one description. C.30 keeps those variants usable without turning any publication form into architecture or any bundle/list into view membership.

### C.30:11 - SoTA-Echoing

| Practice or source line | C.30 adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| FPF `C.2.1`, `A.22`, `C.30.AD`, and `C.30.ASV` multi-view architecture discipline | Current FPF separates actual subject relations, exact selected A.22 structure, direct `ArchitectureRelation`, bounded claim content, Description episteme, viewpoint, structural view, representation, publication, correspondence, grounding, and source return. | Ask whether the actual relation obtains or the content is modal, then choose the next architecture move before opening heavier description and view records. When architecture-description or traceability use is current, recover correspondence, source pins, description-reliance relations, and source-return conditions. | A tool, notation, model-use structure, view, description, file, list, or publication creates none of the subject-side relation, structure, or truth facts by form. |
| SEI views-and-beyond lineage plus current multi-view practice | Keep module, component-and-connector, runtime interaction, allocation, and placement as separate view pressures. | Do not reduce architecture to module structure or interface relation; assign structural-view claims to `C.30.ASV`. | View taxonomies are lineage and comparison support, not a second FPF ontology. |
| arXiv:2603.00601 code-space architecture relation-graph work and related code-agent architecture probing benchmarks | Adapt partial-observability probing, typed edge rules, component-boundary rules, invariant-field semantics, uncertainty or unexplored-region reporting, and probe-as-intervention warning. | A generated code relation graph can supply a source relation for an architecture description or structural view only with claim, source, uncertainty, relation semantics, and source return. | Do not mint `U.CodeSpace`; do not treat probe or benchmark output as architecture adequacy, evidence sufficiency, assurance, or release. |
| Holon-architecture law-like constraint set from the architecture source | Adopt Conway and mirroring as transformer-transformed correspondence pressure through `C.32.CONWAY`; use other law-like architecture lines only as recognition pressure for selected structures and architecture characteristics. | For Conway or mirroring, recover transformer holon, transformed holon, changing relation, selected structures, affected characteristics, candidate gain, and candidate loss. For other law-like pressure, identify the selected structure and characteristic, then apply the governing architecture, relation, measurement, selected-set, or decision pattern. | No law-like slogan is architecture adequacy, decision, evidence sufficiency, assurance, gate passage, or universal architecture ontology by itself. |
| GonzoML neural-network architecture corpus as source example for general architecture-operation language | Adopt practitioner architecture-operation language as general architecture material: structural substitution, relation retargeting, dataflow change, path-selection and gating, memory and cache placement, block and layer substitutions, MoE expert-selection, pruning, distillation, NAS, ablation, and compute, memory, and latency tradeoffs. | Keep source labels as source labels through `C.30.STRAT`; after recovery, use the language for architecture-description and architecture-view recognition, transformation-flow-structure source relation, module-and-interface repair, scale characterization, candidate move guidance, and decision-context fields. | Neural-network labels, benchmarks, ablations, pruning masks, search outputs, or distillation success do not become FPF ontology, architecture decision, evidence sufficiency, gate passage, assurance, or architecture adequacy by themselves. |
| Platform-engineering, MOSA, and open-systems practice | Adapt open-interface, platform extension-rule, substitution-policy, and conformance-expectation pressure as local architecture boundary discipline. | For an open-interface claim or platform claim, name the local structure, interface, variation point, substitution policy, conformance-evidence subject pattern, migration boundary, update channel, and hardening boundary that change action. | Platform design depends on project, organization, time, and place; there is no universal platform maturity scale or open-label proof. |
| ADR and architecture-knowledge-management practice | Adopt decision-memory pressure only as a project-side decision concern governed outside C.30. | Treat ADR-like material as publication or decision-description source relation until the architecture decision claim is being made. | ADR is not the project decision itself and not a source of release authorization. |

### C.30:12 - Relations

Builds on: `A.1`, `A.22`, `E.24.PUB`, `C.30.P`, `C.2.1`, `A.6.3`, `A.7`, `E.10.D2`, `E.17.0`, `E.17.1`, `E.17`, `E.17.2`, `A.6.P`, `F.18`, `E.10`, and `C.2.P`.

Coordinates with: `C.30.STRAT`, `C.30.ASV`, `A.6.F`, `C.30.TFS-REL`, `C.30.LCA`, `C.30.ILC`, `E.18`, `C.29`, `C.16`, `C.25`, `C.28`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, `G.5`, `E.17`, `C.32.P2S`, `C.32`, `C.32.PAD`, `C.32.ADR`, `C.32.ADA`, `C.33`, `C.34`, and `C.35` when problem-to-structure carry-through, candidate-set, architecture-decision, ADR-projection, decision-adequacy, structure-capture, preservation, or discovery-adequacy claim kinds are being made.

For neighboring claims, use `A.1` for the described holon, `A.22` for a selected-structure EntityOfConcern, `C.30.STRAT` for stratification-wording and source-label repair, `C.30.ASV` for structural-view adequacy, `C.33` for captured and lost selected-structure adequacy plus source return, `C.34` for preservation or correspondence adequacy, `C.35` for generated or discovered carrier adequacy before C.32 admission, `E.18` for selected transformation-flow structure, path, and crossing discipline, `E.18.2` and `C.29` for mathematical graph descriptions and mathematical-lens use, `C.16` for characterization, `C.25` for Q-Bundles, `C.28` for causal use, `A.10` and `G.6` for evidence, `B.3` for assurance, `A.20` and `A.21` for gate or release records, `A.15.2` for a WorkPlan, `A.15.5` for work-entry readiness, `A.15.1` for performed Work, `C.11` for decisions, `E.11.PUR` for pattern-use recommendation, `E.10.MOVE` for move-like wording outside C.30 architecture-candidate use, and `C.32.P2S` for the connected problem-to-structure architecturing flow. For publication, use `E.17` for a source-backed face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. Use `C.30` to state and test actual `ArchitectureRelation` occurrences, bounded `ArchitectureClaim` content, selected structures, and the next admissible architecture candidate use.

### C.30:End

