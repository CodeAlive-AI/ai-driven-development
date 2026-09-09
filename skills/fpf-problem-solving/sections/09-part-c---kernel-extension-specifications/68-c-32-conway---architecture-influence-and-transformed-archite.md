## C.32.CONWAY - Architecture-Influence and Transformed-Architecture Correspondence

> **Type:** Architectural subpattern under C.32
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Tech-name:** `Architecture-Influence and Transformed-Architecture Correspondence`
> **Plain cue:** compare an architecture that influences the change with the architecture being changed
> **Lineage and search cue only:** Transformer and Transformed Architecture Correspondence

### C.32.CONWAY:1 - Problem frame

Use this pattern when one architecture-side source — recovered as an exact described holon, selected `U.Structure`, and either an obtaining C.30 `ArchitectureRelation` or truthful modal `ArchitectureClaim` — or another independently typed Work arrangement, communication structure, constraint, or candidate-synthesis result influences the candidate architecture of a changed referent, and the practitioner must decide what to change on either side without mistaking influence for action.

Plain cue: **compare an architecture that influences the change with the architecture being changed**.

Primary working reader: an architect or architecture-responsible practitioner who must compare one independently typed influence source with the current or modal architecture content of the changed referent and prepare candidate changes without turning an `ArchitectureRelation`, selected structure, claim, or architecture-bearing holon into an actor.

Typical entry situations include:

- a desired product architecture cannot be produced and verified by the current manufacturing and certification arrangements;
- chosen service boundaries still force every delivery team to coordinate every release;
- a method family is proposed for changing documents, but the assigned review roles and evidence structure do not fit what the project must produce;
- an AI-agent toolchain is intended for Work on project products, but its control and evidence boundaries do not fit the changed product architecture; or
- the project needs a source-side, transformed-side, joint, or bounded-mismatch inverse-Conway candidate rather than another diagram of the desired target.

A clean-looking target architecture can still be unbuildable or unproducible, untestable, hard to maintain or evolve, or hard to certify. Existing production, communication, approval, control, evidence, and operating arrangements can constrain the candidate and shift coordination into shared releases, approvals, evidence reconciliation, or exception handling. Treat each such arrangement as an independently typed influence source and recover its direct influence relation when that relation is asserted; the source architecture does not act, and mirroring alone does not establish architecture adequacy.


Start with the domain action: a manufacturing system builds a product, a compiler compiles a program, a service team changes a service, a clinical team treats a patient, or an instructional system teaches a learner. Identify the changed referent first. Only then name an acting system, exact system-role assignment, and dated Work when those facts are current. Separately name the architecture or other source that influences the candidate and the exact relation by which it does so.

**First-minute use slice.** A product-family team wants independently replaceable field modules. It identifies the changed referent as `ProductFamilyFieldModuleBoundary@2026Q3`. The influence side is the obtaining C.30 `ArchitectureRelation(ManufacturingCertificationSystem@Plant-A, BatchLineSharedEvidenceStructure@Current)`; the transformed side is the obtaining C.30 `ArchitectureRelation(ProductFamily@Current, FieldModuleBoundaryStructure@Current)`. The exact holons and selected `U.Structure` participants remain visible, and any desired replacement structure stays only in a separate `ArchitectureClaim`. No direct architecture-influence kind or predicate has yet been recovered, so the team keeps the pairing as a provisional independent-change pressure with `missing-governor`. It prepares source-side, transformed-side, joint, and bounded-mismatch candidates without naming an acting system, system-role assignment, Work occurrence, or actual transformation. Those facts are added separately only if a later claim needs them.

The primary working object is a local candidate-synthesis frame. It can pair actual architecture sides through exact obtaining C.30 `ArchitectureRelation` refs or carry candidate, required, desired, or expected structure only through separately identified `ArchitectureClaim` refs. When one exact architecture-influence or correspondence relation already obtains between two actual architecture sides, C.32.CONWAY is also the pattern for one reusable `ArchitectureInfluenceTransformedArchitectureCorrespondenceRow@Context` episteme about that exact occurrence. The frame, row, architecture relations, claims, selected structures, changing system, Work, actual transformation, changed referent, candidate palette, and any network that later cites the row remain different objects.

What goes wrong if this pattern is missed: an architecture, organization chart, method family, toolchain, communication structure, or network record is called the transformer and silently receives agency, a system-role kind or assignment, Work, or participation in the change. Or the reverse happens: real performer and Work facts disappear behind a vague claim that one architecture shaped another.

What this buys in practice: the practitioner can prepare architecture candidates while preserving four independent questions—what changed, who acted or performed Work, which sources influenced the candidate, and which exact architecture pair the current correspondence row concerns.

Ordinary working move:

1. name the changed referent and, only when actual change is claimed, the independently admitted `U.Transformation`; keep every actor-side or Work-to-change relation separate;
2. name exact acting and performance facts only when current;
3. name each influence source with its kind and direct influence relation;
4. for an exact reusable row, select one pair of obtaining C.30 `ArchitectureRelation` occurrences and keep each holon and selected-structure participant visible; when either side is only candidate, required, desired, or expected, keep the pair in the frame with its exact `ArchitectureClaim` instead;
5. prepare source-side change, transformed-side change, joint change, or bounded mismatch candidates.

Adoption test: a reader can tell which exact case passes, which does not, what the practitioner changes next, and whether the result is only local synthesis material or a reusable exact pair row.

Not this pattern when the current work is only bounded-change identification, system-role assignment or Work attribution, module-interface repair, mathematical structural similarity, local choice, or an architecture decision. Use the subject pattern and return here only when one pair of an influence-source architecture and a transformed architecture changes candidate synthesis.

Common exits by claim kind:

- `A.3.4` or `A.3.4.P` for the bounded change and changed referent.
- `A.12` for acting-side externalization, `A.13` for exact actual-performer recovery, `A.15.1` for independent dated-Work admission and distributed-performer forms, `A.2.1` for an exact assignment occurrence when separately claimed, `F.6` for a later `performedUnderAssignment(W, RA)` relation only when precise assignment-bound attribution is expressly consumed, and the pattern that defines any direct actor-side or Work-to-change relation needed by the current use. F.6's holder projection only supports equality comparison with the already recovered performer; it identifies neither assignment nor performer.
- `A.6.M` for module-interface repair.
- `C.32.ACS` for current architecture-characteristic criteria rows and `C.25` for any composite Q-Bundle and exact slot used by the trade-off.
- `C.29` and the project-selected structural-equivalence pattern for structural similarity.
- `A.19.CPM` for explicit comparison and `A.19.SelectorMechanism` for set-returning selection.
- `G.5` for selected-set result declaration; `E.17` for a source-backed publication face and source return; `E.24.PUB` for the publication occurrence and audience availability; `C.18` and `C.19` for archive, front, or pool-treatment policy.
- `C.11` for fixed local choice and `C.32.PAD` for a project architecture decision.

The first useful output is `ArchitectureInfluenceTransformedArchitectureCorrespondenceFrame@Project`. It is a working record for candidate synthesis, not an acting entity, exact relation occurrence, architecture decision, or structural-equivalence claim.

For a first pass, fill only the synthesis question, intended correspondence use, ClaimScope when it changes the claim, independently identified changed referent, source-side and transformed-side exact holon and selected-structure refs, and either an obtaining C.30 `ArchitectureRelation` ref or a truthful modal `ArchitectureClaim` ref for each side. Add architecture-characteristic criteria refs or plain provisional heads, applicable candidate-form heads, evidence and the evolution window, and the next pattern. Assert an influence row only when its direct relation is current and both architecture sides are obtaining C.30 occurrences; otherwise keep one explicit provisional pressure in `provisionalArchitectureCharacteristicHeads[]` and its exact return. The first-minute case above can be filled as follows:

```text
ArchitectureInfluenceTransformedArchitectureCorrespondenceFrame@Project:
  intendedCorrespondenceUse: prepare architecture candidates for independent field-module replacement
  claimScopeRef?: product-family module-change architecture claims
  synthesisQuestion: which source-side, product-side, joint, or bounded-mismatch change can support independently replaceable field modules?
  changedReferentRef: ProductFamilyFieldModuleBoundary@2026Q3
  influenceSourceSelectedStructureMap[]:
    - influenceSourceHolonRef: ManufacturingCertificationSystem@Plant-A
      influenceSourceArchitectureRelationRef: C.30 ArchitectureRelation(ManufacturingCertificationSystem@Plant-A, BatchLineSharedEvidenceStructure@Current)
      influenceSourceArchitectureClaimRef?: omitted — the obtaining relation and current structure are enough for this use
      structureKindRef: BatchAndEvidenceResponsibilityStructure
      selectedStructureRef: BatchLineSharedEvidenceStructure@Current
      contributionToCandidatePressure: may prevent independent field-module replacement
      architectureCharacteristicPressure: provisional independent-change pressure
      relationFunctionClaimRef: C.30 plus A.22
      sourceReturnCondition: missing-governor — recover the direct architecture-influence kind and predicate
  transformedHolonRef: ProductFamily@Current
  transformedArchitectureRelationRef: C.30 ArchitectureRelation(ProductFamily@Current, FieldModuleBoundaryStructure@Current)
  transformedArchitectureClaimRef?: omitted — the obtaining relation and current structure are enough for this use
  transformedSelectedStructureMap[]:
    - structureKindRef: ModuleBoundaryStructure
      selectedStructureRef: FieldModuleBoundaryStructure@Current
      requiredStructureContribution: permit independent field-module replacement
      architectureCharacteristicPressure: provisional independent-change pressure
      relationFunctionClaimRef: C.30 plus A.22
  correspondenceClaims[]:
    - correspondenceId: BatchEvidence-to-FieldModulePressure
      influenceSourceArchitectureRelationRef: C.30 ArchitectureRelation(ManufacturingCertificationSystem@Plant-A, BatchLineSharedEvidenceStructure@Current)
      transformedArchitectureRelationRef: C.30 ArchitectureRelation(ProductFamily@Current, FieldModuleBoundaryStructure@Current)
      influenceSourceSelectedStructureRef: BatchLineSharedEvidenceStructure@Current
      transformedSelectedStructureRef: FieldModuleBoundaryStructure@Current
      correspondenceUse: prepare candidates; no exact pair row asserted
      pressureDirection: batch and evidence arrangements may constrain module independence
      provisionalArchitectureCharacteristicHeads[]: independent change for field modules
      receivingUsePatternLocator: C.32.ACS
      sourceReturnCondition: missing-governor — recover the direct influence kind and predicate
  candidateArchitectureConfigurations[]:
    - candidateRef: SourceSideChange@CellAndEvidenceStructures
    - candidateRef: TransformedSideChange@FieldModuleBoundary
    - candidateRef: JointChange@CellEvidenceAndModuleBoundary
    - candidateRef: BoundedMismatch@ExplicitExceptionCost
  evolutionWindowRef: ProductFamilyModuleChange@2026Q3
  evidenceRefs?: current batch-line evidence-structure and field-module boundary records
  nextQuestionPatternLocator: C.32.ACS
```

This sparse frame asserts no influence occurrence and no exact pair row. The four candidate refs are first-pass heads, not comparison-ready configurations. Add acting-system, exact system-role-assignment, dated-Work, exact-pair-row, C.29, network, publication, comparison-ready gain, loss, and preservation, and any additional source-return fields only when the corresponding claim becomes current; adding them refines this frame without changing its changed referent, architecture pair, or provisional pressure. The complete extension schema is:

```text
ArchitectureInfluenceTransformedArchitectureCorrespondenceFrame@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureCorrespondenceFrameProjectUseRelationRef?: U.RelationRef defined by the exact synthesis-use or work-use pattern
  synthesisQuestion:
  intendedCorrespondenceUse:
  claimScopeRef?: U.ClaimScope
  changedReferentRef:
  actualTransformationRef?: U.EntityRef constrained to U.Transformation, only when A.3.4 independently admits the bounded change of changedReferentRef
  performerRows[]?:
    actingSystemRef: U.EntityRef constrained to U.System; for performance, this is the exact actual performer recovered through performerA13CoreBasisRef
    performerA13CoreBasisRef?: required with workOccurrenceRef; cites the exact local kind and criterion, classification, same obtaining assignment, scope, working situation, window, and adequate core evidence
    workOccurrenceRef?: U.EntityRef constrained to U.Work, independently admitted by A.15.1 when performance is claimed
    actingSystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment, include when an obtaining assignment is separately represented and require the same A.13 assignment when attribution is represented
    performedUnderAssignmentRelationRef?: U.RelationRef governed by F.6, include only when this row expressly represents precise assignment-bound attribution; omit otherwise; missing or failed F.6 leaves workOccurrenceRef intact
    actorSideOrWorkToChangeRelationRefs[]: exact U.RelationRef values required by the current claim
  influenceSourceRows[]?: asserted influence facts only
    influenceSourceRef:
    influenceSourceKindRef:
    exactInfluenceRelationRef: U.RelationRef
    influencePatternLocator:
  influenceSourceSelectedStructureMap[]?:
    influenceSourceHolonRef:
    influenceSourceArchitectureRelationRef?: exact obtaining C.30 ArchitectureRelation ref
    influenceSourceArchitectureClaimRef?: exact C.30 ArchitectureClaimRef for actual, candidate, required, desired, or expected content not carried by an obtaining relation
    structureKindRef:
    selectedStructureRef:
    contributionToCandidatePressure:
    architectureCharacteristicPressure:
    relationFunctionClaimRef:
    sourceReturnCondition?:
  transformedHolonRef:
  transformedArchitectureRelationRef?: exact obtaining C.30 ArchitectureRelation ref
  transformedArchitectureClaimRef?: exact C.30 ArchitectureClaimRef for actual, candidate, required, desired, or expected content not carried by an obtaining relation
  transformedSelectedStructureMap[]:
    structureKindRef:
    selectedStructureRef?:
    requiredStructureContribution:
    architectureCharacteristicPressure:
    relationFunctionClaimRef:
    sourceReturnCondition?:
  evolutionWindowRef:
  evidenceRefs?:
  architecturePairRowRefs[]?: ArchitectureInfluenceTransformedArchitectureCorrespondenceRow@Context refs
  correspondenceClaims[]?: synthesis-local compound claims that have not yet met the exact-row assertion threshold
    correspondenceId:
    influenceSourceArchitectureRelationRef?:
    influenceSourceArchitectureClaimRef?:
    transformedArchitectureRelationRef?:
    transformedArchitectureClaimRef?:
    influenceSourceSelectedStructureRef?:
    transformedSelectedStructureRef:
    correspondenceUse:
    pressureDirection:
    affectedArchitectureCharacteristicRefs[]?: current C.32.ACS criteria-row refs; exact C.25 Q-Bundle slot refs when composite
    provisionalArchitectureCharacteristicHeads[]?: plain discovery cues pending C.32.ACS/C.25; never criteria refs
    expectedArchitectureGain?:
    knownArchitectureLoss?:
    preservedStructure?:
    lostOrHiddenStructure?:
    receivingUsePatternLocator:
    sourceReturnCondition:
  candidateArchitectureConfigurations[]:
    candidateRef:
    influenceSourceSideChange?:
    transformedArchitectureChange?:
    coordinationChange?:
    expectedArchitectureGain?:
    knownArchitectureLoss?:
    evolutionWindowRef?:
    receivingUsePatternLocator?:
    sourceReturnCondition?:
    stopOrEscalationCondition?:
  c29LensOrStructuralEquivalenceRef?:
  nextQuestionPatternLocator:
```

Project-local use keeps two separate fields. `@Project` remains a compatibility and retrieval cue only. If the frame is used in one actual project, `projectWorkOccurrenceRef` names the exact composite `U.Work` and `architectureCorrespondenceFrameProjectUseRelationRef` names the direct relation by which that Work uses the frame. The frame, synthesis Work, candidates, architecture relations, claims, selected structures, and project Work remain distinct. An `ArchitectureRelation` ref is affirmative only for an independently obtaining C.30 occurrence; candidate, required, desired, or expected architecture content stays in an `ArchitectureClaim` and cannot enter an exact pair row as though it already obtained.

`TransformerTransformedArchitectureCorrespondenceFrame@Project` and the former title “Transformer and Transformed Architecture Correspondence” are lineage and search cues only. They do not name the current Tech object, make any named value an actor, or establish an acting-system, system-role-kind, assignment, Work, or participation fact.

### C.32.CONWAY:2 - Problem

Architecture influence and action often occur in the same story but are not the same fact. A manufacturing architecture can constrain a product candidate while a manufacturing system performs production Work. A communication structure can influence service boundaries while people or teams perform change Work only through their admitted exact `U.System` identities. A method description can influence a work-product architecture without being a worker. A toolchain architecture can constrain project-task candidates while an admitted execution system acts.

Transformer and transformed wording can hide these differences. It can leave the changed referent implicit, treat an architecture bearer as the performer, omit the exact system-role assignment and dated Work, or call a source influential without a direct relation. It can also stretch one local architecture pair into a whole recursive transformation-flow network.

C.32.CONWAY repairs the problem by keeping the changed referent, actor and performance facts, influence-source facts, and one exact architecture pair separately recoverable. Conway and inverse-Conway practice then supplies candidate pressure, not a universal relation and not evidence that any source acted.

### C.32.CONWAY:3 - Forces

| Force | Tension |
|---|---|
| Domain action vs architecture influence | A system can act while its architecture or another selected structure influences the candidate; neither fact entails the other. |
| Performance detail vs candidate synthesis | Exact system-role assignment and dated Work matter when performance is claimed, but candidate architecture work must not invent them from an influence diagram. |
| Exact influence vs useful local frame | A local compound correspondence can guide candidate synthesis before a reusable episteme about an obtaining exact relation can be asserted. |
| One pair vs recursive network | One architecture pair can qualify a network reading, but the pair is neither the network nor a cross-flow relation by citation. |
| Desired transformed architecture vs source-side constraint | The transformed architecture may need a structure the current influence-side arrangement cannot sustain. |
| Evolution window | A correspondence that works now can fail when either selected architecture, the direct relation, or the changed referent changes. |

### C.32.CONWAY:4 - Solution

Build the local synthesis frame first. Admit a relation kind only through the applicable E.24-family admission pattern and direct settlement. Use that pattern's predicate and applicability to test the current pair. If current facts or constituting history satisfy the predicate affirmatively, one world-side occurrence obtains and the row may cite its exact identity. If the predicate is false, no exact pair row is asserted. If the current facts do not decide it, keep the correspondence synthesis-local and name the missing grounding or information-sufficiency boundary. Use `missing-governor` only when no direct relation kind and predicate govern the intended pair and use.

#### C.32.CONWAY:4.1 - Keep acting, influence, and correspondence facts separate

1. **Name the domain action and changed referent.** Identify `changedReferentRef` independently. Add `actualTransformationRef` only when A.3.4 independently admits one bounded change of that same continuing referent; keep actor-side and Work-to-change relations under their subject patterns. Architecture influence identifies none of those facts.
2. **Add acting and performance facts only when claimed.** Every precise actual performer is one exact `U.System` recovered through A.13. Claimed performance requires one exact dated `U.Work` independently admitted through A.15.1 and the exact actor-side or Work-to-change relation needed by the claim. Add an obtaining occurrence of a directly admitted `U.SystemRoleAssignment` species under A.2.1 and F.6 `performedUnderAssignment(W, RA)` only when this frame or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; then compare `S` with `RA.HolderSystemSlot`. F.6 identifies neither assignment nor performer, and missing or failed F.6 leaves the Work intact. Use A.15.1 `CC-A15.1-17` when several systems jointly perform the top-level Work or when the use instead needs a parent Work with separately performed child occurrences.
3. **Name every influence source by kind.** Architecture, selected structure, Work, communication, constraint, and candidate-synthesis results retain their kinds and direct influence relations. Influence alone supplies no system identity, system-role kind or assignment, Work, performer status, changed-referent identity, or transformation participation.
4. **Select one architecture pair.** For an exact row, name one obtaining influence-source C.30 `ArchitectureRelation` and one obtaining transformed-side C.30 `ArchitectureRelation`, with each exact holon and selected-`U.Structure` participant. Their architecture-bearing holons may differ from every acting system. Record equality only when independent actor and architecture-bearer facts establish it. If either side is only candidate, required, desired, or expected, keep its exact `ArchitectureClaim` and the pair in the synthesis frame; do not assert an exact pair row.
5. **Map only structures and characteristics that change the candidate.** Name the source-side selected structure, transformed-side selected structure, expected gain, known loss, evolution window, pattern for the next question, and source-return condition. For each affected characteristic, reference only the few current `C.32.ACS` criteria rows and any declared `C.25` Q-Bundle slots that make this trade-off real.
6. **Prepare four candidate forms.** Change the influence-source side, change the transformed architecture, change both, or keep a bounded mismatch with an explicit cost and reopen trigger.
7. **Use C.29 only for structural-similarity claims.** A correspondence row does not establish homomorphism, equivalence, or architecture adequacy.
8. **Stop at the next governed claim.** Send comparison, selection, publication, choice, decision, evidence, assurance, gate, Work, or organization-governance claims to their direct patterns.

#### C.32.CONWAY:4.2 - Exact reusable architecture-pair row

```text
ArchitectureInfluenceTransformedArchitectureCorrespondenceRow@Context <: U.Episteme:
  entityOfConcernRef: exactArchitectureInfluenceOrCorrespondenceRelationOccurrenceRef
  entityOfConcernKindRef: exactArchitectureInfluenceOrCorrespondenceRelationKindRef
  relationFunctionClaimRef: subject pattern of that exact relation kind and occurrence
  influenceSourceArchitectureRelationRef: one exact obtaining C.30 ArchitectureRelation
  influenceSourceHolonRef: the exact architectureBearingHolonRef participant of influenceSourceArchitectureRelationRef
  influenceSourceSelectedStructureRef: the exact selectedArchitectureStructureRef participant of influenceSourceArchitectureRelationRef
  influenceSourceArchitectureClaimRef?: exact C.30 ArchitectureClaimRef when the current use also needs claim content about that same holon, relation, or structure
  transformedArchitectureRelationRef: one exact obtaining C.30 ArchitectureRelation
  transformedHolonRef: the exact architectureBearingHolonRef participant of transformedArchitectureRelationRef
  transformedSelectedStructureRef: the exact selectedArchitectureStructureRef participant of transformedArchitectureRelationRef
  transformedArchitectureClaimRef?: exact C.30 ArchitectureClaimRef when the current use also needs claim content about that same holon, relation, or structure
  changedReferentRef: exact independently identified referent of the current change
  actualTransformationRef?: U.EntityRef constrained to U.Transformation, only when A.3.4 independently admits the bounded change of changedReferentRef
  performerRows[]?:
    actingSystemRef: U.EntityRef constrained to U.System; for performance, this is the exact actual performer recovered through performerA13CoreBasisRef
    performerA13CoreBasisRef?: required with workOccurrenceRef; cites the exact local kind and criterion, classification, same obtaining assignment, scope, working situation, window, and adequate core evidence
    workOccurrenceRef?: U.EntityRef constrained to U.Work, independently admitted by A.15.1 when performance is claimed
    actingSystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment, include when an obtaining assignment is separately represented and require the same A.13 assignment when attribution is represented
    performedUnderAssignmentRelationRef?: U.RelationRef governed by F.6, include only when this row expressly represents precise assignment-bound attribution; omit otherwise; missing or failed F.6 leaves workOccurrenceRef intact
    actorSideOrWorkToChangeRelationRefs[]: U.RelationRef
  additionalInfluenceSourceRows[]?:
    influenceSourceRef:
    influenceSourceKindRef:
    exactInfluenceRelationRef: U.RelationRef
    influencePatternLocator:
  affectedArchitectureCharacteristicRefs[]: current C.32.ACS criteria-row refs; exact C.25 Q-Bundle slot refs when composite
  evolutionWindowRef:
  correspondenceUse:
  expectedArchitectureGain:
  knownArchitectureLoss:
  receivingUsePatternLocator:
  sourceReturnCondition:
  networkCrossFlowRelationRowRef?: E.18.NET NetworkCrossFlowRelationRowRef
```

The row is a `U.Episteme` about one already obtaining direct influence or correspondence relation whose exact participants include the two obtaining C.30 architecture-relation occurrences required by this use. Because those occurrences fill participant positions of another relation, each is explicitly individuated under A.6.REL for this receiving use. The row neither creates the influence occurrence nor mints a universal Conway relation. Each C.30 occurrence keeps its exact holon and selected-`U.Structure` participants; the influence occurrence keeps its identity under its direct relation pattern and A.6.REL. This row only describes them for the current correspondence use. `entityOfConcernRef`, its kind, its governor, both C.30 occurrences and their participant pairs, and the changed referent are required. If the practitioner has only a useful local compound correspondence claim, or either architecture side is modal rather than obtaining, keep it in the frame for candidate synthesis. Assert the row only after the admitted influence relation kind's direct predicate is applicable and current facts satisfy it affirmatively. If the predicate is false, assert no row; if facts are unresolved, keep the frame and name that boundary; if the kind or predicate is absent, return `missing-governor`. None of these branches permits inferring a relation from two architecture claims, structures, diagrams, or names.

#### C.32.CONWAY:4.3 - Qualified network reading

The same exact pair row may appear in `architectureCorrespondenceRowRefs[]` of several `TransformationFlowStructureNetworkRecord@Context` values while its pair, relation occurrence, evolution window, correspondence use, and claim scope remain current. Each citation contributes only one qualified architecture reading. The row's optional singular `networkCrossFlowRelationRowRef`, when present, qualifies only the exact current record edition named by that locator; it does not qualify the row's citations from other records. No citation makes the pair row the network, adds a member, or satisfies the network's exact cross-flow-relation discriminator.

Set `networkCrossFlowRelationRowRef` only when the pair row's exact influence occurrence and architecture-relation participants are independently grounded in member-flow positions and the locator's `transformationFlowStructureNetworkRecordRef` names the same exact current record whose `architectureCorrespondenceRowRefs[]` citation this mapping is intended to qualify. Resolve that record first, then require exactly one `crossFlowRelationRow` to match the occurrence and complete ordered endpoint-binding identity. That row must preserve the same kind, governor, participant order, endpoints, and bindings as this correspondence row. Zero or several matches, a different record, or a stale record edition leaves the locator unresolved. Do not reuse one locator to qualify another record's citation. A record citation alone infers none of those facts.

Acting-system identity, system-role assignment, F.6 attribution, Work, actual transformation, actor-side or Work-to-change relation, influence relation, and network cross-flow relation remain separately governed even when one case cites all of them.


#### C.32.CONWAY:4.4 - Candidate moves and repair rows

Plain text begins with the domain action—builds, assembles, repairs, configures, treats, teaches, compiles, or evaluates. It then names the acting system and Work only when those facts are current. In a separate sentence it says which architecture or other source influences which candidate through which exact relation. `Creator`, `creation`, `producer`, `transformer architecture`, and `uses` remain ordinary cues, not universal technical labels.

Choose only pressures that change the candidate or protect against a concrete loss. Every `affectedArchitectureCharacteristicRefs[]` value in an exact pair row or comparison-ready candidate must resolve to a current `C.32.ACS` criteria row; when the pressure is one slot of a composite quality family, also resolve the declared `C.25` Q-Bundle and that exact slot. If those governed objects do not yet exist, put plain heads such as independent change, substitutability, evidence reuse, latency, coupling or cohesion, coordination load, and source-return cost only in the local frame's `provisionalArchitectureCharacteristicHeads[]`; never place them in `affectedArchitectureCharacteristicRefs[]`. These heads are discovery cues, not a universal catalogue and not criteria refs. Use `C.32.ACS` or `C.25` before making a stronger comparison, selection, or decision claim.

| Correspondence repair row | Use | Minimum repair against overread |
|---|---|---|
| `changedReferentRecovery` | The story names a team, line, tool, method, or organization but not what changes. | Identify the exact continuing changed referent; when actual change is asserted, identify its A.3.4 `U.Transformation`; keep actor-side and Work-to-change relations separately governed. |
| `performerRecovery` | A source is said to build, design, repair, or operate. | Recover each exact actual performer through A.13 and let A.15.1 independently admit the dated `U.Work`; add the exact A.2.1 assignment, F.6 `performedUnderAssignment` occurrence, and holder-equality check only when this frame or receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment. Add direct actor-side or Work-to-change relations separately; use A.15.1 `CC-A15.1-17` when several systems perform. |
| `influenceSourceRecovery` | An architecture or structure is said to shape a candidate. | Name its exact kind and direct influence relation; otherwise keep it as a candidate cue. |
| `architecturePairRecovery` | Two architectures are compared or linked. | Apply the direct relation pattern. With no kind/predicate, return `missing-governor`; with unresolved facts, keep the pair synthesis-local and name the missing grounding; with a false predicate, assert no occurrence; with a satisfied predicate, name the exact obtaining occurrence and pair. |
| `inverseConwayRetargeting` | The desired transformed architecture is sound, but the current source-side arrangement cannot sustain it. | Change selected influence-source structures and record migration cost, new burden, and stop condition. |
| `transformedArchitectureRetargeting` | The source-side arrangement is fixed or too expensive to change in the current window. | Change the transformed architecture candidate and record the lost desired property or exception. |
| `jointCorrespondenceSynthesis` | Neither side alone can carry the architecture characteristic. | Change both sides and record preserved structure, lost structure, and coordination burden. |
| `boundedCorrespondenceMismatch` | A mismatch is tolerable for now. | State exception cost, bounded-use limit, source-return condition, and reopen trigger. |

**Stop condition.** A first-pass frame may stop when it names the changed referent, separately typed source and transformed architectures, one selected structure on each side, either governed affected-characteristic refs or visibly provisional heads with their exact return, the applicable candidate-form heads, and the next subject pattern. Every acting, performance, or influence fact that is asserted must already have its direct basis. Before a candidate enters comparison or reliance, complete its source-side change, transformed-side change, expected gain, known loss, evolution window, pattern for the next question, source-return condition, and stop. An exact pair row additionally requires its direct relation predicate to be satisfied and its obtaining occurrence to be identified. A provisional pressure stays in `correspondenceClaims[]` with the exact reason visible: missing governor, unresolved grounding or information sufficiency, or a false predicate.

**Lowering condition.** Lower an exact row to synthesis-local correspondence material when its influence occurrence, either C.30 architecture-relation occurrence or participant pair, changed referent, evolution window, or receiving use is missing or stale. Retire a candidate when its source-side change, transformed-side change, bounded mismatch, or known loss no longer belongs to the declared evolution window. Use A.3.4 or E.18 when the actual transformation, changed referent, or flow relation is not recovered; A.12, A.2.1, A.15.1, and F.6 when the issue is acting side, assignment, Work, or attribution; and C.29 when the current claim is structural similarity or preservation.

### C.32.CONWAY:5 - Worked Correspondence Cases

| Grounded working case | Acting and performance facts | Influence-source and architecture-pair facts | Candidate work | Stop or return |
|---|---|---|---|---|
| Product family and manufacturing system | The product referent and bounded A.3.4 transformation are identified independently when actual change is claimed. The admitted manufacturing and certification Systems jointly perform dated architecturing Work, each through its basis: A.13 first, independent A.15.1 Work admission second, and F.6 afterward only for precise assignment-bound attribution; the direct Work-to-change relation remains separate. | One obtaining C.30 `ArchitectureRelation` connects the manufacturing-and-certification holon to its shared batch-line evidence structure; another connects the product-family holon to its current field-module structure. A Plant-A domain declaration defines the influence predicate between those exact occurrences, and current case facts satisfy it. Neither architecture-bearing holon nor architecture relation is inferred to be a performer. | Prepare manufacturing-cell change, product-module split, joint change, and bounded batch exception. | Stop at candidate preparation. Handle product choice or architecture decision under `C.11` or `C.32.PAD`; factory Work authorization through its direct authority or permission relation or an `A.21` gate; and certification evidence or assurance through `A.10` or `B.3`. |
| Organization designing and operating a service platform | Each acting team or organization is used through its admitted `U.System` identity; any actual design or operations Work points to its basis: A.13 first, independent A.15.1 Work admission second, and F.6 afterward only for precise assignment-bound attribution. | Communication, deployment, test, and approval structures influence one service-platform architecture pair through their direct relations. | Prepare a service-boundary, platform-mediation, or bounded-coordination-cost change. If responsibility retargeting is proposed, name the exact responsibility predicate and old and proposed participants; otherwise mark that branch `missing-governor` instead of calling it a team or test role change. | Stop before an organization-redesign decision or authority claim and apply the exact predicate and test for that claim. Use `G.5` for selected-set result declaration and `C.32.PAD` for an architecture decision. When publication is current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. |
| Review method influencing authored work products | The method description does not act. When review is performed, recover every precise performer's A.13 core and independently admit the review Work under A.15.1; add F.6 only when precise assignment-bound attribution is current, and state any Work-to-change relation separately. | The review-method or evidence structure influences the authored-section architecture through its exact method-use, evidence-scope, or project influence relation. | Add a prospective exception-assignment requirement and evidence scope, change the Method step, change the work-product structure, or reject the automation candidate. | Stop before method-governance or publication claims. For method use, apply the direct predicate and the pattern that defines and tests it. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability. Use `G.5` only when selected-set result declaration is current. |
| Instructional system changing learner capability | Each instructor or instructional organization is used through its admitted `U.System` identity; any actual teaching Work points to its basis: A.13 first, independent A.15.1 Work admission second, and F.6 afterward only for precise assignment-bound attribution. | Curriculum, feedback, and evidence structures influence the architecture claim about the changed learner-capability referent. | Prepare curriculum, a prospective feedback-assignment requirement, evidence scope, or bounded-cohort candidates. | Stop before educational policy, evidence-sufficiency, or ethical-mediation claims; state them under the exact policy predicate, `A.10`, or `D.4` respectively. |
| AI-agent toolchain changing project work products | An admitted execution System performs any actual tool-call or authoring Work through its basis: A.13 first, independent A.15.1 Work admission second, and F.6 afterward only for precise assignment-bound attribution. | Toolchain control and evidence-refresh structures influence the transformed work-product architecture through exact relations; the toolchain architecture itself does not act. | Add supervision and refresh, change task decomposition, or keep bounded autonomy with source return. | Stop before safety, gate, release, or assurance claims; use the exact safety predicate, `A.21` for a gate decision, the applicable authority or permission relation for release, and `B.3` for assurance. |

**Exact positive, distributed-performer, and network-local slice.** In one Plant-A domain framework, `PlantArchitectureInfluenceRelations-v3` defines `BatchEvidenceArchitectureConstrainsModuleArchitecture(sourceArchitectureRelation, transformedArchitectureRelation, evolutionWindow)`. Its first participant is the obtaining C.30 `ArchitectureRelation(ManufacturingCertificationSystem@Plant-A, BatchLineSharedEvidenceStructure@Current)`; its second is the obtaining C.30 `ArchitectureRelation(ProductFamily@Current, FieldModuleBoundaryStructure@Current)`. Both occurrences are explicitly individuated under A.6.REL because this domain predicate uses them as participants. Plant-A facts satisfy that predicate over `ProductFamilyModuleChange@2026Q3`, so `BatchEvidenceConstrainsFieldModules-17` is the exact obtaining influence occurrence and the EntityOfConcern of `BatchEvidence-to-FieldModules-Row-17`. This case-local predicate and occurrence do not mint a universal Conway relation.

The changed referent is independently identified as `ProductFamilyFieldModuleBoundary@2026Q3`. If the case also claims actual change, A.3.4 independently identifies `FieldModuleBoundaryTransformation-17 : U.Transformation`.

Before the candidate occurrence is called Work, A.13 recovers both collective performers for one shared scope, working situation, and window. The scope is `ProductFamilyModuleChange@2026Q3`; the situation is `PlantAModuleTransitionArchitecturingSituation-17`; and the window is `2026-07-14T09:00:00+03:00` through `2026-07-16T18:00:00+03:00`. `ManufacturingArchitectureTeam-A : U.System` has boundary `ManufacturingArchitectureTeamBoundary-A`, comprising the rostered team members, their manufacturing-constraint decision channel, and the coordination interactions governed by `ManufacturingArchitectureCoordinationMethod-v2`. Its exact case-local action is `ManufacturingBoundaryConstraintAction-17`: select, revise, pause, or escalate manufacturing-feasibility constraints on the field-module boundary. It acts toward `BatchFeasibleModuleBoundaryObjective-17` under the current batch-line capability, shared-evidence, and batch-exception conditions. `CertificationArchitectureTeam-A : U.System` has the distinct boundary `CertificationArchitectureTeamBoundary-A`, comprising its rostered members, certification-evidence decision channel, and the coordination interactions governed by `CertificationArchitectureCoordinationMethod-v2`. Its exact action is `CertificationEvidenceConstraintAction-17`: select, revise, pause, or escalate the certification-evidence obligations attached to the same boundary. It acts under `CertificationEvidenceContinuityNorm-17`, which requires every recommended boundary continuation to retain traceable applicable evidence and requires a hold when a material evidence gap remains. Its relevant conditions are the applicable certification obligations, current evidence links, and open evidence gaps. Neither System boundary includes the product family, either C.30 architecture-relation occurrence, the role-kind descriptions, or the assignment occurrences; neither action is yet called Work.

`PlantArchitecturingSystemRoleKindDomain` contains two exact local agential system-role kinds with independent membership criteria. `ManufacturingArchitectureSystemRole` requires the stable work-facing contribution of manufacturing-feasibility constraint judgment and goal-directed, condition-sensitive regulation toward `BatchFeasibleModuleBoundaryObjective-17`: the holder must select among admissible boundary continuations and revise, pause, or escalate its judgment when batch-line capability or exception evidence changes. `CertificationArchitectureSystemRole` requires the stable work-facing contribution of certification-evidence constraint judgment and corresponding regulation under `CertificationEvidenceContinuityNorm-17`: the holder must select among admissible evidence continuations and revise, pause, or escalate when an obligation or evidence gap changes. `ManufacturingConstraintDecisionTrace-17` shows the manufacturing team comparing two admissible continuations, revising one constraint after new batch-exception evidence, and pausing the unsupported continuation. `CertificationEvidenceDecisionTrace-17` shows the certification team revising the evidence obligation after an applicability change and holding the unsupported continuation pending a missing trace. A.10 evidence-use claims connect those traces and the respective boundary and coordination records to the two criteria. On that basis Plant-A separately classifies `ManufacturingArchitectureTeam-A` under `ManufacturingArchitectureSystemRole` and `CertificationArchitectureTeam-A` under `CertificationArchitectureSystemRole`. The evidence and classifications are independent of the candidate Work and of either assignment. No Grade, autonomy result, characteristic profile, or stronger assurance claim is consumed here.

The two-participant assignment kind `PlantArchitecturingWorkAssignment` is declared under `U.SystemRoleAssignment`. Its `HolderSystemSlot` admits a `U.System`; its local `AssignedSystemRoleKindSlot` uses `PlantArchitecturingSystemRoleKindDomain`; and its predicate says that, for the declared scope, situation, and interval, the holder is selected to supply the contribution defined by the assigned kind to the Plant-A transition-architecturing action. `ManufacturingArchitectureAssignment-17` assigns `ManufacturingArchitectureSystemRole` to `ManufacturingArchitectureTeam-A`; `CertificationArchitectureAssignment-17` assigns `CertificationArchitectureSystemRole` to `CertificationArchitectureTeam-A`. Both occurrences obtain with their declared holder and assigned-kind values, all species-specific predicates satisfied, and maximal uninterrupted predicate-true intervals covering the full stated window. These are the same obtaining assignments later consumed by F.6.

Only after both A.13 cores are established does A.15.1 independently admit `ModuleTransitionArchitecturingWork-17 : U.Work`. The independently grounded joint performance history records the two actions above as one top-level occurrence; the Work runs from `2026-07-14T09:00:00+03:00` to `2026-07-16T18:00:00+03:00` and enacts `ModuleTransitionArchitecturingMethod-v3`. A locally declared relation places that Work within `ProductFamilyEngineeringSystem-A` for the stated engineering-system boundary and Work interval. The independently admitted `ProductFamilyEngineeringSystem-A : U.System` is the second participant of that relation. Neither assignment nor an F.6 conclusion is an A.15.1 admission premise.

F.6 then records that `ModuleTransitionArchitecturingWork-17` was performed under each of the same obtaining assignments established in the A.13 cores. The direct case facts link the exact Work to both assignment occurrences; holder equality holds for `ManufacturingArchitectureTeam-A` and `CertificationArchitectureTeam-A`, and both assignment intervals cover the Work. The Plant-A relation `ArchitecturingWorkChangesModuleBoundary` separately states that this Work brings about `FieldModuleBoundaryTransformation-17`.

This is the A.15.1 `CC-A15.1-17` joint-performer form. Neither a lead assignment nor the architecture pair substitutes for either performer. Taxonomy and scheme epistemes may help interpret an assertion, but they are not assignment participants.

`ProductDevelopmentNetworkRecord-2026Q3` may cite `BatchEvidence-to-FieldModules-Row-17` once in `architectureCorrespondenceRowRefs[]`. That citation contributes one reading of the exact two C.30 architecture-relation occurrences. The pair row remains an episteme, not the `TransformationFlowStructureNetwork`, not one of its members, and not a cross-flow relation. Its optional `networkCrossFlowRelationRowRef` stays absent unless this same influence occurrence is independently grounded at exact member-flow positions and the composite E.18.NET locator resolves exactly one matching row in that same current record edition.

**Network-qualified reading.**
A product-development TFS and a production-system-change TFS participate in one selected E.18.NET-conforming network. A current architecture pair row about manufacturing-architecture influence may be cited by the network record alongside a separately grounded obtaining production or project occurrence. If the pair row also carries `networkCrossFlowRelationRowRef`, that locator names this same exact current record edition and resolves exactly one matching row; it qualifies no citation from another record. The pair row remains one reading of one exact architecture pair. It is neither the network nor proof that the architecture-influence occurrence is the cross-flow occurrence.

**Near miss.** A diagram places a factory architecture beside a product architecture and labels the arrow “shapes”. No direct relation kind and predicate govern that pair and use. The frame may retain the pair as synthesis-local pressure, but the exact row and network cross-flow mapping remain absent with `missing-governor`; the diagram does not create an occurrence.

### C.32.CONWAY:6 - Correspondence Failure Modes

| Failure mode | C.32.CONWAY repair action |
|---|---|
| **Architecture-as-actor** | Replace the acting architecture with the exact `U.System`. When performance is claimed, recover every precise performer's A.13 core and independently admit the Work under A.15.1; add F.6 only when precise assignment-bound attribution is current, and state any actor-side or Work-to-change relation separately. Keep architecture relation, claim, holon, and selected structure as separately related influence-side objects. |
| **Influence-as-performance** | Remove system-role-kind, assignment, Work, performer, or transformation-participation inferences that came only from influence. Establish those facts independently or leave them absent. |
| **Changed referent or transformation omitted** | Identify the exact continuing referent; when actual change is claimed, identify its A.3.4 `U.Transformation`; keep actor-side and Work-to-change relations under their subject patterns before deciding which architecture content is transformed. |
| **Performer without Work basis** | When performance is claimed, recover every precise performer's A.13 core and independently admit the Work under A.15.1; add F.6 only when precise assignment-bound attribution is current, and add only the other direct relations used by the claim. Use A.15.1 multiple-performer forms when needed. |
| **Influence source without governor** | Apply the direct relation pattern. With no kind/predicate, keep the correspondence synthesis-local and return `missing-governor`; with unresolved facts, name the grounding boundary; with a false predicate, remove the influence-occurrence claim. |
| **Architecture-bearer equality with an actor inferred** | Keep the influence-source holon and acting-system refs separate; assert equality only when independent actor and architecture-bearer facts establish it. |
| **Transformed-side-only inverse Conway** | If the text says inverse Conway but changes only the transformed architecture, name the exact influence-source selected structure that must change or stop using the inverse-Conway claim. |
| **Source-side change without transformed pressure** | If an organization, method, line, or toolchain is reorganized without one transformed architecture and characteristic under pressure, return to the direct Work or organization-design use. |
| **One-sided optimization** | Prepare source-side change, transformed-side change, joint change, and bounded mismatch candidates before claiming the correspondence has been constructively handled. |
| **Pair treated as network** | Keep the exact pair row as one qualified reading; use E.18.NET for network identity, members, and exact cross-flow relations. |
| **Network citation treated as relation admission** | Ground the exact relation participants in member-flow positions and make the E.18.NET composite locator name that same citing current record and exactly one cross-flow row; otherwise remove `networkCrossFlowRelationRowRef`. A locator for one record does not qualify another record's citation. |
| **Mirroring treated as adequacy** | Keep the statement as candidate pressure or use C.29 when structural similarity or preservation is claimed. |
| **Software-practice overfit** | When the changed referent is a product family, manufacturing system, school, hospital, or another admitted non-software holon, transfer only the selected-structure correspondence and affected characteristics; do not import software-service or team ontology. A method-family or method-description label alone does not make the named object a `U.Holon`; if the case uses a method-related holon, identify that exact holon and admit it independently under its direct kind-admission pattern. |
| **Static correspondence** | Reopen when either architecture, selected structure, relation occurrence, changed referent, or evolution window changes. |

### C.32.CONWAY:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
|---|---|---|
| `CC-C32.CONWAY-1` | `changedReferentRef` is independently identified; any claimed actual bounded change has one A.3.4 `actualTransformationRef`, while actor-side and Work-to-change relations retain their direct governors. | Recover those exact objects and relations or keep the change description provisional. |
| `CC-C32.CONWAY-2` | Every claimed actor is an admitted `U.System`; every claimed work-facing assignment names an occurrence and its declared A.2.1 species. The occurrence's holder matches the separately named acting System; the species defines the local assigned-kind domain, predicate, applicability, participant meanings, and occurrence identity. | Add the System, species, and assignment occurrence or remove the acting or assignment claim. |
| `CC-C32.CONWAY-3` | Claimed performance has every exact actual performer recovered through A.13 and exact dated Work independently admitted through A.15.1. An exact A.2.1 assignment, F.6 `performedUnderAssignment(W, RA)` occurrence, and `S = RA.HolderSystemSlot` appear only when precise assignment-bound attribution is expressly represented; missing or failed F.6 leaves Work intact. Direct actor-side or Work-to-change relations remain separate, and several performers use A.15.1 `CC-A15.1-17` forms. | Restore the independent performer and Work basis; add attribution only for a consuming claim, or remove the unsupported performance or attribution claim. |
| `CC-C32.CONWAY-4` | Every influence source retains its exact kind and direct obtaining occurrence; influence entails no actor, system-role kind or assignment, Work, changed-referent, or transformation-participation fact. | Apply the direct predicate: a missing kind or predicate returns `missing-governor`, unresolved facts stay provisional, and a false predicate excludes the occurrence claim; delete inferred acting facts. |
| `CC-C32.CONWAY-5` | One exact pair row names two obtaining C.30 `ArchitectureRelation` occurrences, each exact holon and selected-`U.Structure` participant, the changed referent, exact obtaining influence or correspondence occurrence, admitted relation kind, direct predicate and governor, and a satisfied affirmative case. Modal architecture content remains an `ArchitectureClaim` in the frame. | Complete the satisfied actual pair; otherwise keep only the synthesis-local frame and state modal status, `missing-governor`, unresolved grounding, or false predicate exactly. |
| `CC-C32.CONWAY-6` | Equality between an architecture bearer and an actor is recorded only from independent facts. | Separate the refs and remove equality inference. |
| `CC-C32.CONWAY-7` | The two project-use fields retain their exact Work identity and direct use-relation meaning. | Add both facts when project use is claimed or keep `@Project` retrieval-only. |
| `CC-C32.CONWAY-8` | Each comparison-ready candidate states source-side change, transformed-side change, expected gain, known loss, evolution window, pattern for the next question, source-return condition, and stop; a first-pass candidate head is visibly outside comparison. | Complete the candidate before comparison or keep only its `candidateRef` as a first-pass head. |
| `CC-C32.CONWAY-8a` | Every `affectedArchitectureCharacteristicRefs[]` value resolves to a current C.32.ACS criteria row and, when composite, the exact C.25 Q-Bundle slot; a local discovery cue appears only in `provisionalArchitectureCharacteristicHeads[]` and supports no comparison, selection, or decision. | Resolve the governed ref, move the cue to the provisional-head field and use C.32.ACS/C.25, or remove the stronger claim. |
| `CC-C32.CONWAY-9` | Structural-similarity claims use C.29 or the selected structural-equivalence pattern. | Remove similarity entailment or apply the direct pattern. |
| `CC-C32.CONWAY-10` | A network record cites the pair only as a qualified reading; any `networkCrossFlowRelationRowRef` names that same exact current citing record, resolves exactly one row there, and its independently grounded occurrence and endpoint bindings agree with this pair. The singular locator qualifies no other record citation. | Remove the network link or repair the citing record, occurrence, and ordered endpoint-binding locator. |
| `CC-C32.CONWAY-11` | Source-return and evolution-window conditions are present. | Add the changed values and reopen trigger. |

### C.32.CONWAY:8 - Common Repair Cues

| Repair cue | Symptom | First repair |
|---|---|---|
| `ArchitectureActs` | An architecture, method, toolchain, organization chart, or episteme builds, decides, repairs, or performs. | Start with the domain action; name the exact system and Work when current, then state architecture influence separately. |
| `InfluenceSourceUntyped` | A source “shapes” the candidate without kind or relation. | Apply the subject pattern: recover kind/predicate or return `missing-governor`; if facts are unresolved, keep a candidate cue; if false, remove the occurrence claim; if satisfied, name the obtaining occurrence. |
| `ChangedReferentHidden` | The pair is named but the object or claimed actual transformation is not. | Identify the continuing changed referent and, when current, the A.3.4 `U.Transformation`; keep direct participation and Work-to-change relations separate. |
| `PerformerBasisMissing` | A performer is named without its A.13 core, independently admitted dated Work, or the F.6 relation required by a precise assignment-bound attribution. | Apply A.12 to separate acting and changed sides; recover every precise performer's A.13 core; independently admit the Work under A.15.1; add F.6 only when the receiving claim needs precise assignment-bound attribution; and use the `CC-A15.1-17` form when several systems perform. |
| `TransformedArchitectureNoSourceFit` | The desired architecture cannot be sustained by the current influence-side structures. | Open source-side retargeting, transformed-architecture retargeting, joint change, and bounded mismatch as alternatives. |
| `InverseConwayNoSourceChange` | The text says inverse Conway but names no selected influence-source structure change. | Name that exact structure, affected characteristic, migration burden, loss, and pattern for the next question or drop the inverse-Conway claim. |
| `SourceChangeNoTransformedPressure` | A source-side organization, method, line, or toolchain change has no transformed architecture characteristic under pressure. | State the change under its direct Work or organization-governance predicate until the architecture pair is current. |
| `CoordinationCostHidden` | Visible coupling falls while Work, evidence, approval, manufacturing, or operational coordination rises elsewhere. | Name the exact influence source and relation carrying that pressure; add candidates that expose the shifted cost. |
| `MirroringNoExceptionTest` | Mirroring is used without preserved or lost structure, an exception, or an evolution window. | Keep it as diagnostic pressure or use C.29 for the declared lens. |
| `PairFlattenedIntoNetwork` | One architecture pair is called the entire transformation-flow network. | Restore E.18.NET identity and keep the pair as one optional qualified reading. |
| `BoundedMismatchHidden` | A known mismatch is kept without cost or trigger. | Record bounded use, exception cost, source return, and reopen trigger. |

### C.32.CONWAY:9 - Consequences

| Positive consequence | Cost or trade-off |
|---|---|
| Architecture influence can guide synthesis without granting agency. | Actor, Work, changing, and influence relations must be grounded separately. |
| Exact pair rows can be reused across current network records. | Each reuse must preserve pair, relation occurrence, qualification window, and claim scope. |
| Inverse-Conway work produces explicit candidate changes and bounded mismatches. | Some familiar “transformer architecture” shorthand must be expanded into several facts. |
| Changed referent and transformed architecture stay recoverable. | A useful local frame may remain below exact-row assertion when the governor is missing or case facts remain unresolved. |
| Network recursion remains with E.18.NET. | One pair row cannot stand in for the whole network or its cross-flow relations. |
| Candidate architectures are checked against source-side production, testing, maintenance, evidence, and evolution arrangements. | Changing the influence-source side can be expensive; an attractive transformed-side candidate may therefore be rejected for the current evolution window. |
| Organization, Work, method, tool, and module claims are routed to their subject patterns instead of being hidden in an architecture-pair result. | This separation may require the practitioner to follow several separately governed exits before comparison. Mirroring supplies candidate pressure, not architecture adequacy; use C.29 when the claim is structural similarity or preservation. |

### C.32.CONWAY:10 - Rationale

Architectures do not act. Systems perform dated Work under exact system-role assignments when performance is claimed. Architectures, selected structures, Work arrangements, communication structures, constraints, and candidate-synthesis results can nevertheless influence which transformed architecture is feasible. C.32.CONWAY is useful precisely because it relates those facts without merging them.

The exact pair row gives one obtaining architecture-influence or correspondence occurrence a reusable episteme. The larger frame remains useful when a project has enough information to prepare candidates but not enough to assert that exact row. This preserves practical forward motion while keeping the exact relation status visible: missing governor, unresolved grounding, false predicate, or satisfied affirmative case.

The four candidate forms remain: change the influence-source side, change the transformed architecture, change both, or keep a bounded mismatch. The split between actor facts and influence facts changes their grounding, not their constructive purpose.

### C.32.CONWAY:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.CONWAY. Each row names the field, repair row, or boundary that uses the source's contribution. The source family supports architecture practice; it does not decide actor identity or make a relation obtain.

| Source to inspect | Why this source is load-bearing here | Transfer into C.32.CONWAY | Concrete C.32.CONWAY mutation | Blocked overread |
|---|---|---|---|---|
| Melvin Conway, `How Do Committees Invent?` (`https://www.melconway.com/Home/Committees_Paper.html`) | Original source for pressure between communication arrangements and the structure of designed systems. | Treat communication and organization architecture as influence on candidates. | `influenceSourceRows[]` and the exact pair row name the source architecture, transformed architecture, selected structures, relation occurrence, and changed referent. | The organization or its architecture is not inferred to be the acting system; candidate pressure is not a universal Conway relation. |
| MacCormack, Rusnak, and Baldwin 2012 mirroring hypothesis (`https://doi.org/10.1016/j.respol.2012.04.011`) and Colfer and Baldwin 2016 exceptions survey (`https://www.hbs.edu/ris/Publication%20Files/16-124_7ae90679-0ce6-4d72-9e9d-828872c7af49.pdf`) | Empirical and theory line for product-architecture and organization-architecture mirroring and exceptions. | Use mirroring as a correspondence hypothesis over selected structures and an evolution window. | Failure and conformance rows require affected characteristics, exceptions, source return, and C.29 for structural-similarity claims. | Mirroring does not establish adequacy, actor equality, relation occurrence, or an entire network. |
| DORA loosely coupled teams, last updated 2025-10-20 (`https://dora.dev/capabilities/loosely-coupled-teams/`) | Practitioner line tying architecture, team independence, testing, deployment, and coordination load. | Treat those arrangements as typed influence sources when they constrain a service architecture candidate. | Candidate forms expose source-side retargeting, transformed-side retargeting, joint change, and bounded mismatch. | Team autonomy or work-transfer counts do not identify actors, Work, or an architecture-influence occurrence without their direct facts. |
| Team Topologies key concepts (`https://teamtopologies.com/key-concepts`) | Organization-design family for fast flow, interaction modes, cognitive load, platform teams, and evolving boundaries. | Use team types and interaction modes as candidate influence sources, not acting kinds. | Influence-source rows retain exact source kind and relation; candidate rows retain migration cost, burden, and evolution window. | Team-topology vocabulary creates neither a system-role kind or assignment nor Work, module relation, authority, or decision claims. |
| Current FPF `A.12`, `A.2.1`, `A.15.1`, `F.6`, `A.3.4`, `A.3.4.P`, `E.18`, `E.18.NET`, `A.6.M`, `C.29`, `C.30`, `C.32`, `C.32.MLAO`, and `C.32.FAIL` | Current ontology for acting Systems, declared system-role-assignment species and their obtaining occurrences, Work, performed-under-assignment attribution, bounded transformation, flow structures and networks, module repair, lens use, architecture relations and claims, candidate synthesis, residual reduction, and failure repair. | Recover participants and relations before using Conway wording. | Performer rows, influence rows, the C.30 pair assertion, network-qualified reading, and receiving-pattern exits are separately checkable. | No root Conway kind, universal correspondence relation, acting architecture, modal architecture promoted to actuality, or bypass around decision, Work, evidence, or network selection. |

**Source-currentness boundary.** Recheck a row when the changed referent, acting and performance facts, influence source or relation, architecture pair, selected structures, evolution window, source practice, or pattern for the next question changes. If the source no longer supports the selected local pressure, lower it to background lineage; do not preserve a technical claim by name alone.

### C.32.CONWAY:12 - Relations

- **Builds on:** `C.32` for candidate architecture synthesis; `C.30` for exact described holons, obtaining `ArchitectureRelation` occurrences, selected `U.Structure` participants, and modal `ArchitectureClaim` content; `A.3.4` and `A.3.4.P` for the continuing changed referent and actual bounded transformation; `A.12` for acting-side externalization; `A.13` for exact actual-performer recovery; `A.15.1` for independent dated-Work admission and distributed-performer forms; `A.2.1` for assignment occurrence identity when separately represented; `F.6` for a later `performedUnderAssignment(W, RA)` relation only when precise assignment-bound attribution is consumed; direct subject relation patterns for actor-side, Work-to-change, and influence occurrences; `A.6.REL` when this episteme consumes occurrence identity; `E.18` for one TFS; and `E.18.NET` for network identity and exact cross-member relations. F.6's holder projection only compares equality with the already recovered performer.
- **Uses:** `C.32.ACS` for current architecture-characteristic criteria rows; `C.25` for composite Q-Bundles and their declared slots; `C.32.MLAO` for a cross-scope residual; `C.32.FAIL` for a correspondence repair failure; `C.29` when structural similarity, preservation, mapping, or equivalence is claimed; and `A.6.P.WMR` and `A.6.RCD` when a required direct relation cannot be recovered.
- **Patterns for the next questions:** `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `G.5` for selected-set result declaration, `E.17` for a source-backed publication face and source return, `E.24.PUB` for the publication occurrence and audience availability, `C.18` and `C.19` for archive, front, or pool treatment, `C.11` for fixed local choice, `C.32.PAD` for architecture decisions, `A.10` for evidence, `B.3` for assurance, `A.21` for gate decisions, the applicable authority or permission relation for release, and the direct method, Work, or organization-governance patterns when those claims are current.
- **Network boundary:** an `ArchitectureInfluenceTransformedArchitectureCorrespondenceRow@Context` may be cited as one qualified reading in `architectureCorrespondenceRowRefs[]`; it is not the network and does not satisfy an E.18.NET cross-flow relation without the separately grounded obtaining occurrence and endpoint bindings. Its optional singular row locator qualifies only the exact current citing record it names.
- **P2S docking:** `C.32.P2S` may use C.32.CONWAY when a problem-to-structure flow needs one exact architecture-influence/transformed-architecture pair. It does not infer performer or influence facts from the flow card.
- **Boundary:** C.32.CONWAY governs correspondence framing and one exact reusable architecture-pair episteme inside candidate synthesis. It does not govern actor identity, Work occurrence, organization redesign, authority, evidence sufficiency, assurance, gate passage, release, structural-equivalence theory, final architecture decision, or transformation-flow-network identity.

### C.32.CONWAY:13 - Footer marker

`C.32.CONWAY` governs candidate synthesis where one exact architecture or other typed source influences a transformed-architecture candidate through a governed relation. It keeps the changed referent, acting and performance facts, influence-source facts, one architecture pair, and any larger network separately recoverable.

### C.32.CONWAY:End

