## C.32.P2S - Problem-to-Structure Architecturing Unfolding

> **Type:** Architectural process pattern under C.32
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.32.P2S:1 - Problem frame

Use this pattern when an architect or architecture-responsible practitioner has a stated external-use hypothesis for one project system-of-interest and must carry the resulting architecture pressure through selected structures, candidate synthesis, project architecture decision, realization Work, actual-structure feedback, and the next action selected for the current question. If the expected change outside the system, beneficiary or relying use, project designation, boundary hypothesis, or required functioning is not yet intelligible, stop before internal architecture and use the pattern for that missing claim.

The common first moment is practical: a required function has no recoverable bearer; an architecture characteristic is failing; a cross-scope residual survives local repair; a modularity, reuse, interface, scale, or description-loss problem blocks action; one typed Work, communication, tool, method, deployment, evidence, selected-structure, or architecture-side source cannot yet sustain the transformed-side architecture content needed for the changed referent; or operation shows that expected structures and actual structures diverge.

The first useful output is `ProblemToStructureArchitecturingFlowCard@Project`. The card is a working `U.Episteme` about one project-local P2S architecturing transformation flow, not the flow itself, the P2S method, a `U.MethodDescription`, or any planned or performed `U.Work`. It is not a new `U` kind, not an architecture claim, not an architecture decision, not a work plan, not an eval result, and not a publication format. It keeps the connected flow reviewable while each local object remains distinct and the practitioner uses the pattern for each current claim.

For the first pass, fill only the fields that prevent the next wrong move: exact problem claim or pressure, described holon, architecture question and intended use, ClaimScope or qualification window when material, first pattern to use, one unknown or selected structure slot, selected transformation-flow structure when one is actually relied on, and pattern for the next claim. Add decision, work, eval, publication, and feedback refs only when the corresponding question becomes current.

```text
ProblemToStructureArchitecturingFlowCard@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to an individual admitted under U.Work
  architecturingFlowCardProjectUseRelationRef?: U.RelationRef whose predicate is stated in the cited architecturing-use or work-use pattern
  flowId:
  describedHolonRef:
  architectureQuestion:
  intendedArchitectureUse:
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?:
  transformationFlowStructureRef?: exact independently selected E.18 structure used by this flow
  architectingSystemRef?: U.EntityRef constrained to U.System
  architectingAssignmentSpeciesRef?: U.RelationKindRef constrained under U.SystemRoleAssignment
  architectingSystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment, naming the obtaining occurrence when an assignment claim is current

  firstPatternLocator:
  problemPressure:
    acceptedProblemCardRef?: U.EpistemeRef resolving to one exact C.22.2 ProblemCard
    actualProblematicForRelationRef?: U.RelationRef resolving to one exact C.22.PFR occurrence, only when an actual Problem is independently current

    pressureKind:
    problemPressureSignalRefs?:
    sourceUseRecordRefs?:
    architectureConcernRefs?:
    currentStopOrReturnReason?:
  architectureContent:
    architectureQuestionCardRef?: U.EpistemeRef resolving to one exact C.30 ArchitectureQuestionCard@Project
    architectureClaimRefs[]?: exact C.30 ArchitectureClaimRefs
    currentArchitectureRelationRefs[]?: exact obtaining C.30 ArchitectureRelation refs

    candidateStructureKindRefs:
    selectedStructureRefs?:
    expectedStructureRefs?:
    actualStructureRefs?:
    architectureCharacteristicRefs:
    architectureCharacteristicCriteriaSetRef?:
    qBundleRefs?:
    candidateSynthesisRef?:
  structuralInformation:
    unknownStructure:
    selectedStructure:
    expectedStructure:
    actualStructure:
    capturedInDescriptionsOrDecisions:
    handedToMethodsOrWork:
    latentOrHiddenStructure:
    lostStructure:
    strongerStructureInspectionReturnCondition:
  decisionAndWorkDocking:
    candidateSetOrPaletteRef?:
    selectedSetRef?:
    architectureDecisionRef?:
    adrProjectionRef?:
    methodDescriptionRefs?:
    workPlanRefs?:
    readinessRefs?:
    performedWorkRefs?: refs to independently identified U.Work occurrences when performance is current
    performedWorkAttributionRefs?: refs to obtaining F.6 performedUnderAssignment relations only when the flow or receiving use expressly represents attribution

    actualTransformationRefs?:
    workToChangeRelationRefs?: Work-to-change relations that actually obtain
    workToChangeRuleRefs?: refs to applicable rules in the cited patterns, or to local claims selected under A.6.RCD disposition 2
    productionWorkClaimRefs?:
    entityIdentityInceptionClaimRefs?:
    productionCompletionClaimRefs?:
  architectureInfluenceCorrespondence?:
    changedReferentRef:
    actualTransformationRef?: U.EntityRef constrained to U.Transformation, only when independently grounded under A.3.4
    influenceSourceRows[]?: asserted influence facts only
      influenceSourceRef:
      influenceSourceKindRef:
      exactInfluenceRelationRef: U.RelationRef to a relation that actually obtains and has a declared predicate
      influencePatternLocator:
    influenceSourceArchitectureMaps[]?:
      influenceSourceHolonRef:
      influenceSourceArchitectureRelationRef?: exact obtaining C.30 ArchitectureRelation ref
      influenceSourceArchitectureClaimRef?: exact C.30 ArchitectureClaimRef for modal content
      influenceSourceSelectedStructureRefs:
    transformedHolonRef:
    transformedArchitectureRelationRef?: exact obtaining C.30 ArchitectureRelation ref
    transformedArchitectureClaimRef?: exact C.30 ArchitectureClaimRef for modal content
    transformedSelectedStructureRefs:
    correspondenceFrameOrPairRowRef: C.32.CONWAY synthesis-local frame or exact pair-row ref
  feedback:
    evalProgramRefs?:
    evalResultRefs?:
    actualStructureDescriptionRefs?:
    measurementRefs?:
    operationOrUseObservationRefs?:
    functionalCharacteristicImplications?:
    freshnessOrDecaySignalRefs?:
    returnOrRepairForNextQuestion:
      c32NextSynthesisExit?
      c32PadOrAdaDecisionRepairOrSupersessionExit?
      e23ImprovementCycleRef?
      g11CurrentnessRefreshRef?
      e18TransformationFlowRefreshRef?
      c18C19ArchiveFrontPoolUpdateRef?
      c30DescriptionOrViewLossRepairRef?
  patternForNextClaim:
```

For `ProblemToStructureArchitecturingFlowCard@Project`, `flowId` designates the exact project-local P2S architecturing transformation flow that is the card's C.2.1 EntityOfConcern. The claims carried by the filled card and the effective `U.ReferenceScheme` for its designations remain recoverable; changed claim content, changed flow EntityOfConcern, or changed effective reference scheme identifies another card episteme. `@Project` is a compatibility and retrieval cue only. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. When the card is genuinely used in one actual project, `projectWorkOccurrenceRef` identifies the exact composite Work occurrence admitted under `U.Work` and `architecturingFlowCardProjectUseRelationRef` identifies the direct relation by which architecturing work uses the card. The card, the architecturing work it helps coordinate, and the larger project work remain distinct.

The problem, architecting-side, realization, and architecture refs point to independently established objects; they are not P2S relation kinds. `acceptedProblemCardRef` resolves to one C.22.2 C.2.1 episteme; the nested signal and pressure fields neither constitute that card nor make an actual Problem obtain. An assignment claim uses `architectingAssignmentSpeciesRef` and `architectingSystemRoleAssignmentRef` for its separately declared species and obtaining occurrence; it supplies neither classification nor performance. When performance is current, each exact performer first has its A.13 core and each `performedWorkRef` names Work independently admitted through A.15.1. `performedWorkAttributionRefs` are optional and appear only when the flow or receiving use expressly represents precise assignment-bound attribution through the same obtaining A.13 assignment; missing or failed F.6 leaves the Work refs intact. Authority, responsibility, capability, Work, assignment, attribution, and result remain separate.

`actualTransformationRefs` name independently identified actual changes under `A.3.4`. The Work-to-change fields pair each relation that actually obtains with the cited pattern or local claim used to check it. The three production refs resolve to separate local `A.15.PROD` claims and remain absent when their particular question is not current.

`actualStructureRefs` name subject-side `U.Structure` values whose declared substrate and selected relation organization are recovered under `A.22` from direct facts that actually obtain; they introduce neither an `ActualStructure` kind nor an actualization relation. Use C.30 to keep the described holon, obtaining `ArchitectureRelation` occurrences, selected structures, and any affirmative, negative, unresolved, candidate, required, desired, or expected `ArchitectureClaim` content separate. `actualStructureDescriptionRefs` name later descriptions of those structures and do not make them actual.

Not this pattern when the current work is only a problem card, only a grounded architecture claim, only a structural view, only a candidate palette, only a project architecture decision, only an ADR-like publication, only work planning, only performed work, only measurement, only a mathematical lens, or only `G.11` currentness, freshness, telemetry, edition, or decay orchestration. Use the pattern named in `Relations` for that narrower claim.

### C.32.P2S:2 - Problem

FPF has patterns for problem records, grounded architecture, structural views, candidate palettes, architecture characteristics, eval programs, decisions, ADR-like projections, methods, Work occurrences, separate method descriptions and work-record epistemes, measurements, mathematical lenses, improvement loops, and currentness or decay orchestration. A practitioner still needs one readable pattern for the architecture work that connects them.

Architecture work can fail in two opposite ways.

First, the flow collapses into a description or decision artifact: a diagram, view set, ADR, memo, dashboard, score, or publication record is treated as if it carried the architecture, the decision, and the realized structure. The project then loses the distinction between selected structure, description, decision, method expectation, performed work, and actual structure.

Second, the flow starts inside the boundary or disappears into relation rows. An architect selects modules, interfaces, or an attractive configuration before stating the external change, relying use, project system-of-interest, and functioning hypothesis that would justify them; or every local pattern is correct but no readable flow carries the pressure through Work and feedback. In either branch, the user can name patterns but cannot explain why this internal structure serves the outside use.

### C.32.P2S:3 - Forces

| Force | Tension |
|---|---|
| Structure-first architecture | Architecture uses obtaining relations between an exact described holon and selected structures for a named architecture question and use; the flow is not reducible to documents, labels, stages, tools, or a generic context participant. |
| Structural uncertainty | Architecturing often starts before structure kinds, bearers, interfaces, allocations, or variation points are known. |
| Characteristic trade-off | Architecture characteristics compete; optimizing one can damage another or hide Goodhart pressure behind a metric. |
| Candidate plurality | Useful architecture work keeps structurally different alternatives alive until comparison, selected-set, local choice, or architecture decision becomes the current question. |
| Realization gap | Selected and expected structures do not become actual structures by decision, model, description, or matching labels. When claiming that work realized a structure, establish the domain work, actual changes, work-to-change facts, and the facts that make the subject-side structure obtain. |
| Architecture-influence constraint | One typed Work, communication, tool, method, deployment, evidence, selected-structure, or architecture-side source can enable or block the transformed-side architecture content needed for the changed referent without thereby becoming an actor or transformation participant. |
| Description loss | Views, descriptions, decision records, method descriptions, and eval reports capture only part of the structural content needed for later use. |
| Evolution and feedback | Operation, use, telemetry, inspection, evaluation, decay, and new sources can reveal the next question. The practitioner then uses the matching pattern: `C.32` for synthesis, `C.32.PAD` or `C.32.ADA` for repair or supersession, `E.23` for improvement, `G.11` for currentness refresh, `E.18` for transformation-flow slice-local refresh, `C.18` or `C.19` for archive, front, and pool update, or `C.30.AD` or `C.30.ASV` for architecture-description or structural-view loss. |

### C.32.P2S:4 - Solution

Create or update one `ProblemToStructureArchitecturingFlowCard@Project` and apply the P2S method through only the smallest useful part of the Plain action sequence below. The numbered presentation guides attention; it is not by itself a claim about the order, identity, or occurrence of project Work or actual transformations. When the applicable rule in another pattern fully answers the current question, use that pattern and stop there. Continue the P2S card only while the connected project-local P2S architecturing transformation flow remains the object being reviewed.

Before selecting internal structure, state four things in ordinary language: the expected change outside the system, the beneficiary or relying use, the actual or intended project system-of-interest and its boundary, and the functioning hypothesis by which that system could support the use. A merely intended system stays in plan or description content. A.1/A.1.SCR is the pattern for actual-system recognition; A.15.6 is the pattern for project designation; A.1.STM can locate the first unsupported long-map answer. If one of the four statements is missing or contested, return there and do not justify architecture from the inside alone.

Use the analogy with `E.18.1` P2W narrowly. A P2W use carries an accepted problem-side record or exact accepted C.22.2 `ProblemCard` episteme plus the carried distinction into the next FPF use. A C.32.P2S use carries architecture-relevant pressure and structural uncertainty into candidate structures, selected structures, project architecture decision, realization work, and actual-structure feedback. The practitioner then uses the pattern for the next question. The analogy ends when that question is method, work, telemetry, publication, or improvement-loop use; use its pattern rather than stretching P2S into generic process management.

1. Recover the problem pressure or architecture concern together with its outside-use basis. Name the expected environmental or relying-use change, beneficiary or user, project system-of-interest designation and boundary hypothesis, required functioning, pressure signals, source-use records, affected holon, and first pattern to use. If the pressure is still only a cue, use C.22.2 and cite the resulting `ProblemCard` episteme when it becomes the accepted input. If an actual Problem is claimed, cite an independently obtaining C.22.PFR `ProblematicForRelation`; the card and its fields create no such occurrence. If the outside-use or system basis is absent, recover it under the applicable recognition or problem pattern before continuing with P2S.
2. Recover the described holon after the outside-use and boundary hypotheses are visible. State the architecture question and intended use, plus ClaimScope or qualification window when either changes the answer. Then recover candidate or selected structure kinds, selected structures when available, and architecture characteristics. Use C.30 for the grounded architecture claim, C.32.HCS for starter characteristic heads, C.32.ACS for project criteria rows, and C.25 when a composite quality family is current.
3. Represent future-structure uncertainty. State unknown structure kinds, unknown internal composition, candidate bearers, interfaces, allocations, variation points, constraints, expected structures, and the condition that returns the work to stronger inspection of the selected or expected structure. Record what is captured, handed off, latent, hidden, or lost.
4. Generate architecture ideas, principles, constraints, and candidate structure changes. Use an admitted problem-side record, source-pack cue, architecture pressure note, or candidate-generation input only after the affected selected structure, architecture characteristic, expected gain, accepted loss, and pattern for the receiving claim are recoverable.
5. Synthesize candidate architecture configurations and candidate sets through `C.32`. Keep function-bearing feasibility, ordinary work organization or actual Work, and candidate-relevant selected structures visible when they change the candidate. Such structures include constructive-module, placement, control, transformation-flow, information, evidence, and scale structures. Route every unresolved claim-bearing *role* cue through `E.10.ROLE`; carry the recovered local system-role kind, separate System-classification judgment, assignment, direct-relation position, function claim, organization or representation position, or ordinary wording rather than a generic role structure.
6. Compare, retain, declare a selected-set result, publish it, or return alternatives only under the exact predicate that defines or constrains that relation. Use `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.18` and `C.19` for archive, front, and pool policy, `G.5` for selected-set result declaration, and `C.11` for a fixed local choice. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability.
7. Make a project architecture decision through `C.32.PAD` when implementation commitment is current. The decision relation names the selected architecture option, affected structures, trade-off, accepted losses, method and work consequences, accepted lost-structure return, and decision repair or supersession condition.
8. Publish descriptions, views, ADR-like records, narrative renderings, or other records only as descriptions, structure-to-narrative renderings, or publication forms of claims about structures, decision relations, method expectations, description or view loss repair, and reader use. Use `C.30.AD`, `C.30.ASV`, `C.32.ADR`, `A.6.3.NAR`, `E.17`, and `E.24.PUB` as applicable.
9. Name the intended architecting or realizing Systems first, then make the needed Method descriptions, constraints, readiness expectations, work expectations, and structure-use return conditions available to them under their own access or use relations. Do not call a System a holder unless a separately obtaining assignment is present; assignment does not establish classification. Keep availability or access, local kind, separate classification, assignment, readiness, permission, authority, responsibility, and plan or commitment independent. When performance is claimed, recover each exact actual performer through A.13 and let A.15.1 independently admit the `U.Work`. Add `performedWorkAttributionRefs` only when the flow or receiving use expressly represents precise assignment-bound attribution. Add a Work-to-change relation only when that direct predicate obtains. Return the exact missing governor for an unsupported direct claim.
10. Realize selected structures in the transformed holon through domain work without treating the selected or expected structure, decision, method, `MethodDescription`, `WorkPlan`, model, description, evaluation result, publication, or transfer as the actual structure or as an actual transformation. Use `A.15.1` for each dated work occurrence and `A.3.4` for each independently identified actual bounded change. If work is said to cause or realize a change, name the Work-to-change relation and use the cited pattern to check the applicable rule. If no reusable relation is available, cite a local claim selected under `A.6.RCD` disposition 2. Use separate local `A.15.PROD` claims only when production-work participation, entity-identity inception, or historically indexed production completion is current. The P2S card records refs to the independently established Work occurrences, transformations, Work-to-change relations, and local production claims.
11. Observe, inspect, measure, and evaluate subject-side `U.Structure` values whose declared substrate and selected relation organization are recovered under `A.22` from relation occurrences, applied constraints, invariants, or other facts that actually obtain. Include architecture-characteristic results and functional-characteristic or capability implications in operation or use. Ask whether those actual structures enable or block the functions and effects they were meant to bear, and ask what selected structure, accepted loss, counter-characteristic, or functional implication got worse when a visible metric improved. A description, measurement, evaluation result, publication, or resemblance to the selected structure does not itself make a structure actual or establish conformance. Use `C.30` to name an obtaining `ArchitectureRelation` only when its exact holon, selected-structure participant, and predicate are satisfied; keep candidate, required, desired, expected, negative, or unresolved architecture content in an exact `ArchitectureClaim`. Use `C.30.AD` or `C.30.ASV` for actual-structure descriptions or views, `C.32.ACE` for eval programs and eval results, `C.16` for measurement, and `C.25` for Q-bundles. Use `E.23` when repeated improvement method is current, `G.11` when currentness, telemetry, edition, freshness, or decay orchestration is current, `E.18` for transformation-flow slice-local refresh, `C.18` or `C.19` for archive, front, and pool updates, `C.32.PAD` or `C.32.ADA` for decision repair or supersession, `C.32` for new synthesis, and `C.30.AD` or `C.30.ASV` for architecture-description or structural-view loss repair. Use the pattern for the next question to select the return or repair action from actual-structure divergence, eval results, functional implications, freshness loss, description or view loss, and new constraints.

At the realization boundary, keep selected structure, expected structure, actual subject-side structure, exact dated work, independently identified actual transformations, local production claims, actual-structure description, and evaluation result as different objects. Shared assembly work, temporal adjacency, common affected referents, one flow, or one selected configuration establishes neither one composite transformation nor absence of finer transformation parts. If a receiving claim requires transformation composition, return the exact missing-governor blocker; do not use that blocker to stop independent work, inception, completion, actual-structure, description, evaluation, or return claims.

When architecture-influence correspondence constrains the candidate set, add the C.32.CONWAY branch before synthesis becomes narrow. Name the changed referent and any independently grounded A.3.4 transformation separately. Name every influence source by exact kind. Put only asserted influence facts with an exact obtaining direct relation in `influenceSourceRows[]`; otherwise keep the pressure synthesis-local in the C.32.CONWAY frame with its `missing-governor`, unresolved-grounding, or false-predicate disposition. For each actual architecture side, name the exact C.30 holon, obtaining `ArchitectureRelation`, and selected `U.Structure`; keep modal content in an exact `ArchitectureClaim`. Then frame candidate families that change the influence-source side, the transformed side, both, or declare a bounded mismatch with the named correspondence or decision-repair return condition.

#### C.32.P2S:4.1 - P2S Unfolding Structure Block

When the P2S card must remain reusable across patterns for decision, description, work, and feedback claims, add this local block. `P2SUnfoldingStructureBlock` is an architecture-facing local `A.22.CGUS` `U.Structure` specialization block defined here for problem-to-structure architecturing use. That `U.Structure`, the project-local P2S architecturing transformation flow, the P2S method, and the flow-card episteme remain distinct. A pre-admission `ProvisionalUnfoldingDemonstrationDescription` or post-admission `DemonstrativeUnfoldingSlice` is a separate episteme whose displayed order is not the CGUS, flow, method, or Work. The block is not a root U-kind, not an architecture decision, not an ADR, not an architecture description, and not a work plan by itself.

```text
P2SUnfoldingStructureBlock:
  unfoldingStructureRef: U.StructureRef resolving to the selected CGUS or local architecture-facing structure block
  problemPressureRef: U.EpistemeRef resolving to a C.22.2 ProblemCard or another architecture-pressure episteme whose claim has been checked with the cited pattern
  selectedOrUnknownStructureRefs[]:
  architectureContentLoci[]:
  structuralUncertaintyLoci[]:
  candidateSynthesisLoci[]:
  decisionLinkageRef?:
  realizationWorkLinkageRef?:
  actualTransformationRefs[]?:
  workToChangeRelationRefs[]?: Work-to-change relations that actually obtain
  workToChangeRuleRefs[]?: refs to applicable rules in the cited patterns, or to local claims selected under A.6.RCD disposition 2
  productionWorkClaimRefs[]?:
  entityIdentityInceptionClaimRefs[]?:
  productionCompletionClaimRefs[]?:
  actualStructureFeedbackRef?:
  e18TransformationFlowUnfoldingRefs[]?:
  descriptionRefs[]?:
  nextReceivingAction: next action supported by the problem-to-structure result; apply a decision, description, Work, transformation, production, or feedback pattern when its claim is current
  stopOrReturnCondition: reopen when the problem, constraints, candidate structure, or actual feedback changes
  blockedOverread?: include only when F.19's plausible-reader test justifies this exact blocked reading
```

The block is useful when the architecture work has to show how problem pressure constrains candidate, selected, expected, or actual structures without hiding the rule for the next claim or the pattern that contains it. `unfoldingStructureRef` names the selected CGUS or local architecture-facing `U.Structure` block. When a narrower-specialization relation is needed, name and test it under the pattern that defines its predicate; use A.6.RCD if that predicate is missing. `decisionLinkageRef` names the project architecture decision relation defined in `C.32.PAD` only when that decision is current. For the claims associated with `descriptionRefs[]`, use `C.30.AD`, `C.30.ASV`, `C.32.ADR`, `A.6.3.NAR`, or publication patterns only when a description, view, ADR projection, narrative rendering, or publication claim is current. `realizationWorkLinkageRef` points to the A.15-family work relation; use `A.3.4` for actual transformations. The Work-to-change fields keep the obtaining relation separate from the cited pattern or local claim used to check it. The three production-ref groups point only to separate local `A.15.PROD` claims. Establish any Work-authorization, performed-Work, or selected/expected-to-actual claim through its direct pattern. Otherwise stop with the problem-to-structure result, next receiving action, and stop or return condition.

`groundedArtifactConfusion?` is an alias for the same optional `blockedOverread?` value.

Use `e18TransformationFlowUnfoldingRefs[]` only for slices whose substrate is transformation-flow structure. P2S itself is broader: it can carry, for example, module, functional, placement, control, method, evidence, scale, and information structures through architecture synthesis and feedback. Any role-like source wording first resolves to the independently relevant local kind, classification judgment, assignment occurrence, direct-relation or representation position, function claim, organization position, responsibility or authority relation, or ordinary label; P2S has no generic role-structure carrier.

#### C.32.P2S:4.2 - Architecture Unfolding Structure Use

Use `ArchitectureUnfoldingStructureUse@Project` when a named constraint-governed unfolding structure is being used as architecture-relevant structure inside problem-to-structure architecturing. This dependent architecture-use relation record is defined here; use it with the relevant C.30 or C.32 pattern. Record any architecture decision, description, ADR projection, or realization Work through its direct pattern when that claim is current.

```text
ArchitectureUnfoldingStructureUse@Project:
  kind: dependent architecture-use relation record under C.32.P2S, C.30, and adjacent architecture patterns
  projectWorkOccurrenceRef: U.EntityRef constrained to the exact composite U.Work that is an explicit participant in this use relation
  architectureQuestionCardRef?: U.EpistemeRef resolving to one exact C.30 ArchitectureQuestionCard@Project
  architectureBearingHolonRef: U.EntityRef resolving to the exact described holon
  architectureRelationRefs[]?: exact obtaining C.30 ArchitectureRelation refs
  architectureClaimRefs[]?: exact C.30 ArchitectureClaimRefs for affirmative, negative, unresolved, candidate, required, desired, or expected content
  unfoldingStructureRef:
  architectureStructureUseKind:
    transformationFlow |
    methodWork |
    control |
    narrativePublication |
    evidenceAssurance |
    referenceCurrentnessRefresh |
    otherDeclared
  architectureViewpointRef?:
  affectedSelectedStructures[]:
  architectureCharacteristicRefs[]:
  acceptedLosses[]:
  methodOrWorkLinkageRefs[]?:
  architectureDecisionRef?:
  architectureDescriptionRefs[]?:
  architectureUseReturnCondition:
  repairOrSupersessionCondition:
```

For `ArchitectureUnfoldingStructureUse@Project`, the suffix remains a compatibility and retrieval cue until an exact use is asserted. Every asserted occurrence includes `projectWorkOccurrenceRef` as the exact composite `U.Work` participant; without that Work, keep only the retrieval cue and do not assert the use relation. `architectureQuestionCardRef` may cite the exact C.30 triage episteme, while `architectureBearingHolonRef` names its independently identified subject. `architectureRelationRefs[]` contain only independently obtaining C.30 occurrences; modal architecture content stays in `architectureClaimRefs[]`. `unfoldingStructureRef` names the admitted CGUS or local block being used. `affectedSelectedStructures[]`, `architectureCharacteristicRefs[]`, and `acceptedLosses[]` state why the unfolding structure matters for architecture rather than for a generic route. Method and work refs point to the A.15 family only as realization or feedback linkage. For decisions, descriptions, ADR-like projections, measurements, evals, evidence, gates, publication, and performed work, use the exact subject predicates and treat their patterns only as locators.

Stop conditions:

- stop at `C.22.2` when the signal is not yet a reviewable problem-side record;
- stop at `C.30` or `C.30.ASV` when the current need is only architecture claim or structural-view adequacy;
- stop at `C.32` when the next useful artifact is a candidate palette rather than a whole P2S carry-through record;
- stop at `C.32.PAD` when the project architecture decision is current;
- stop at `A.3.1` for Method identity or `A.3.2` for `MethodDescription` membership, or at the A.15 family when the current question is method-work alignment, work planning, readiness, or performed work;
- stop at `C.16`, `C.25`, `C.29`, `C.32.ACE`, `E.23`, or `G.11` when the current claim is measurement, quality-bundle, mathematical-lens, eval, improvement, or `G.11` currentness refresh;
- reconsider P2S only when a later subject assertion establishes architecture pressure that changes candidate structures, expected structures, actual structures, selected structures, or the stronger-structure inspection condition.

### C.32.P2S:5 - Archetypal Grounding

**Tell.** The architect carries pressure into structure: first by finding which selected structures are missing or inadequate, then by constructing alternatives, deciding what will be pursued, enabling exact domain work, and watching which subject-side structures actually obtain under operation. An actual transformation is introduced only when its own `A.3.4` basis is grounded.

**First-minute use slice.** A plant architect sees that expected throughput and actual throughput diverge after a layout change. The first P2S card pass names the production cell as described holon, the throughput-after-layout-change architecture question, operating-shift qualification window, pressure kind `actualStructureDivergesFromExpectedStructure`, first pattern to use `C.30`, unknown structure `material-flow bottleneck bearer`, selected structure candidate `buffer placement`, and pattern for the next claim `C.32`. The card does not yet add a PAD decision, work plan, or eval result; those refs appear only when their questions become current.

**Lens-use slice.** If the plant team builds a DSM or epiplexity-style lens over stations, buffers, and routing events, P2S records only the architecture use: which dependency or learnable structural content was preserved, which flow distinction was compressed away, which selected structures the lens can inform, and which lens-use return condition sends the claim back to `C.29`. The lens result is not architecture adequacy, an eval result, or a decision.

**Show A - built asset and technical system.** A clinic has rising instrument-turnaround delays and infection-control pressure. The first P2S move does not ask for a better diagram. It names the clinic service system as described holon, the turnaround-and-contamination architecture question, intended operating use, applicable scope and window, candidate structure kinds, architecture characteristics, and uncertainty: room layout, sterile and contaminated flows, equipment modules, tray interface, maintenance work, throughput, contamination isolation, maintainability, and surge adaptability. Candidate synthesis develops these alternatives: a centralized autoclave bay, distributed sterilization modules, and a reusable tray-interface change. Use `C.32.PAD` for the decision selecting one configuration, `C.30.AD` and `C.32.ADR` for its descriptions and publication, and A.15-family patterns for construction and operating work. During operation, measure actual turnaround, contamination events, maintenance burden, and actual-structure feedback triggers.

**Show B - organization and Method structures.** Inspection work catches ontological errors late. The source may call the object a review practice and speak of checker roles, but P2S first restores the claim: the described holon is the review organization-as-system; if review Work is the subject instead, recover each exact performer through A.13 and identify the `U.Work` occurrence independently through A.15.1. Use `E.10.ROLE` to separate any local checker kind, classification, current assignment, direct review-relation position, function claim, organization position, and ordinary audience label. Candidate synthesis develops modal alternatives. Establish any claimed actual subject relations independently. For later actual inspection Work, add F.6 only when the flow or receiving use expressly represents precise assignment-bound attribution. Telemetry separately shows whether errors are caught earlier.

**Show C - architecture-influence and transformed-side co-synthesis.** A team wants a modular product architecture but its toolchain, team communication, release method, and evidence workflow only support one tightly coupled build. The team uses `C.32.CONWAY` within the P2S flow: those typed influence sources and their direct relations remain separate from both exact C.30 architecture sides, the changed referent, any actual transformation, acting Systems, assignments, and Work. Candidate families include changing the product modules only, changing the influence-source structures only, changing both, or accepting a bounded mismatch while retaining a named correspondence-frame return condition. The decision states which side changes now, what architecture characteristics are protected, what Work and exact work-to-change relations realize the change, and what operation or delivery feedback can return to the `C.32.CONWAY` correspondence frame or to decision repair.

**Show D - PumpSkid 7 realization and return.** Architecture pressure calls for a modular pump-skid with selected module and placement structures; use `C.32.PAD` for the project architecture decision. Assembly work `W-PS7-ASSEMBLY` and later commissioning work `W-PS7-COMMISSION` are separate Work occurrences admitted under `U.Work` by `A.15.1`. Mounting change `T-PS7-MOUNT`, wiring change `T-PS7-WIRE`, fluid-connection change `T-PS7-CONNECT`, and commissioning-related change `T-PS7-COMMISSION` are each independently identified under `A.3.4`. Where the assembly or commissioning work is asserted to cause a change, cite the work-to-change relation and its declared predicate. Shared work, temporal adjacency, and one selected pump-skid configuration do not establish one composite transformation. The local `A.15.PROD` entity-identity-inception claim uses the applicable PumpSkid 7 identity-specification edition, its applicability basis, work-to-change and change-to-identity facts, and `inceptionBoundary`; it need not assert a composite transformation. Later commissioning can remain production work until subject-state facts at `completionBoundary` satisfy the applicable production-completion-criterion edition; only then can a separate historically indexed completion claim be written. A later `C.30.AD` or `C.30.ASV` record describes the actual structure; use `C.32.ACE` to evaluate service-access coupling. When coupling is worse than the selected expectation, the eval result returns to decision repair or new synthesis. Neither the description, evaluation, identity-inception claim, completion claim, nor shared assembly work proves conformance to the selected architecture or transformation composition.

### C.32.P2S:6 - Bias-Annotation

Use these rows as repair cues for problem pressure, source-practice transfer, or observed signals, not as a catalogue of mistakes.

| Pressure cue or source-practice row | Risk in P2S use | Repair |
|---|---|---|
| Description-first pressure cue | A view, model, diagram, ADR-like record, dashboard, or memo starts to carry architecture, decision, and work authority at once. | Recover selected structures and current use. Use `C.30.AD` or `C.30.ASV` for description adequacy, `C.32.PAD` for decisions, `C.32.ADR` for projections, and A.15-family patterns for work claims. |
| Single-winner pressure cue | A score, workshop favorite, generated candidate, or apparent best alternative hides structurally different candidates. | Restore candidate plurality through `C.32`; keep archive, front, pool, selected-set, comparison, local-choice, or decision use with its applicable pattern. |
| Eval-shaped practice row or signal | A metric, benchmark, source-practice fitness-function term, eval result, or telemetry event is treated as the characteristic or the decision. | Recover characteristic, bearer, scale, eval program, measurement, and receiving use. Use `C.32.ACE`, `C.16`, `C.25`, and then the applicable comparison, selected-set, local-choice, or decision pattern. |
| Architecture-influence basis hidden | Desired transformed-side architecture content is stated without asking which typed Work, communication, tool, method, deployment, evidence, selected-structure, or architecture-side source constrains it. | Open `C.32.CONWAY`; keep the changed referent and any actual transformation separate, recover both exact C.30 architecture sides or their modal claims, name every influence source by kind and either its exact obtaining direct relation or precise provisional disposition, and prepare influence-source-side, transformed-side, joint, and bounded-mismatch candidates. |
| Work-shaped pressure cue | A schedule, task list, method recipe, performed-work record, shared assembly occurrence, or completion label is treated as the architecturing flow, an actual transformation, a composite transformation, or proof that selected structure is actual. | Keep the A.15-family distinctions intact. The P2S card may cite Work occurrences, independently grounded changes, Work-to-change relations and their rules, separate local `A.15.PROD` claims, and actual-structure facts only when they obtain; common work or chronology supplies none of the stronger claims. |

### C.32.P2S:7 - Conformance Checklist

| Check | Pass condition |
|---|---|
| `CC-C32P2S-1` | The card names the exact problem claim or pressure, described holon, architecture question and intended use, first pattern to use, and at least one architecture-relevant structure or unknown-structure slot; scope, window, and selected transformation-flow structure are named only when material. |
| `CC-C32P2S-2` | Each architecture use keeps the exact described holon, obtaining C.30 `ArchitectureRelation` occurrences and their selected-structure participants, and any affirmative, negative, unresolved, candidate, required, desired, or expected `ArchitectureClaim` content separate; no description or publication record carries the architecture by itself. |
| `CC-C32P2S-3` | Architecture characteristics are separate from functional demands, measurements, eval programs, eval results, Q-bundles, comparison rules, and decisions. |
| `CC-C32P2S-4` | The structural-information slots in the P2S card record unknown, selected, expected, actual, captured, handed-off, latent or hidden, lost, and returned structure when those slots are live. |
| `CC-C32P2S-5` | Use `C.32` for candidate synthesis and the applicable patterns for comparison and selection. A score or prose preference alone does not establish a selection result. |
| `CC-C32P2S-6` | When a project architecture decision is current, use `C.32.PAD`; for an ADR-like publication, use `C.32.ADR` and the applicable publication patterns. |
| `CC-C32P2S-7` | Use `A.3.1` for Method identity, `A.3.2` for `MethodDescription` membership, and A.15-family patterns for alignment, work-plan, readiness, and performed-work claims. Identify every actual transformation under `A.3.4`. For every claimed Work-to-change link, cite the relation and the pattern or local `A.6.RCD` claim used to check it. Keep production-work, entity-identity-inception, and production-completion as separate local `A.15.PROD` claims. The P2S card carries refs and expected structure effects only. |
| `CC-C32P2S-8` | For measurement, Q-bundle, mathematical-lens, eval, improvement, `G.11` currentness refresh, and `E.18` transformation-flow slice-local refresh claims, use `C.16`, `C.25`, `C.29`, `C.32.ACE`, `E.23`, `G.11`, or `E.18` as applicable. |
| `CC-C32P2S-9` | Architecture-influence cases keep the changed referent, any actual A.3.4 transformation, both exact C.30 architecture sides or modal claims, every influence source's exact kind and obtaining direct relation or precise provisional disposition, and the `C.32.CONWAY` synthesis-local frame or exact pair row separately recoverable. |
| `CC-C32P2S-10` | The pattern use covers at least one actual-structure feedback route that checks subject-side `U.Structure` values recovered under `A.22` from obtaining relation occurrences, applied constraints, invariants, or other selected-organization facts. It also checks architecture-characteristic results and relevant functional-characteristic or capability implications through operation, use, inspection, measurement, eval result, telemetry, decay, stronger-structure inspection return, or decision-repair trigger. |
| `CC-C32P2S-11` | Selected and expected structures, methods, plans, models, decisions, descriptions, evaluation results, publications, and transfers remain distinct from actual structures and actual transformations. Resemblance does not establish conformance. Shared work, adjacency, common referents, or one flow establishes neither transformation composition nor partlessness. |
| `CC-C32P2S-12` | The PumpSkid 7 replay independently identifies mounting, wiring, connection, and commissioning-related changes; cites exact assembly and commissioning work plus the work-to-change relations and their declared predicates; separates entity-identity inception from later historically indexed production completion; and routes actual-structure description, architecture-characteristic evaluation, and return without fabricating conformance or one composite transformation. |

### C.32.P2S:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Description stop | The project stops after producing a view set, diagram, ADR-like record, or architecture description even though no candidate structure, decision, realization, or feedback path is recoverable. | Return to step 2 or 5. Name selected or unknown structures, architecture characteristics, and the next pattern to use: `C.30`, `C.30.ASV`, `C.32`, or `C.32.PAD`. |
| Relation index P2S | The P2S artifact lists neighboring patterns but does not tell the architect what to do from pressure to subject-side actual structures recovered from facts that actually obtain. | Use the P2S method's Plain action sequence to record only the currently relevant links in the card: pressure, structural uncertainty, candidates, retention or selection, decision, descriptions, method and work handoff, Work, actual changes, subject-side actual structures, feedback, and a return selected for the next question. |
| Eval-as-decision | An eval result, score, metric, telemetry event, or dashboard value selects the architecture. | Use `C.32.ACE` for the eval, `C.16` for measurement, and `C.25` for composite quality; ask what selected structure, accepted loss, counter-characteristic, or functional implication worsened; then use comparison, selected-set, local-choice, or `C.32.PAD` if selection or decision is current. |
| Hidden architecture-influence basis | The transformed-side candidate is designed as if no typed Work, communication, tool, method, deployment, evidence, selected-structure, or architecture-side source constrains it. | Open the architecture-influence branch and `C.32.CONWAY`; recover every source's exact kind and obtaining direct relation or precise provisional disposition, then add candidate families that change the influence-source side, transformed side, both, or a bounded mismatch while keeping actor, Work, changed-referent, and transformation facts separate. |
| Lost structure left silent | The description, decision, method handoff, or eval report compresses away distinctions needed for later work. | Fill the P2S structural-information slots: what is captured, handed off, latent or hidden, lost, and what stronger-structure inspection return condition restores the selected or expected structure needed by the next claim. |
| Work-pattern takeover | P2S prose starts authorizing Work occurrences or replacing method, readiness, WorkPlan, or separate assertion or record epistemes about performed work. | Keep P2S as architecture carry-through. Use `A.3.1` for Method identity, `A.3.2` for `MethodDescription` membership, and A.15-family patterns for method-work alignment and work claims. Keep in the P2S card only references plus expected selected-structure effects. |
| Selected structure treated as actual | A decision, model, description, view, evaluation result, or matching label is used as proof that the selected structure obtains. | Recover the subject-side `U.Structure` under `A.22` from its declared substrate and obtaining relation occurrences, applied constraints, invariants, or other selected-organization facts. Use C.30 `ArchitectureRelation` only when its holon and selected-structure participants satisfy the obtaining predicate; keep modal content in `ArchitectureClaim`. Keep descriptions and evaluations separate, and use the relevant patterns to test conformance. |
| Common work treated as one composite transformation | Mounting, wiring, connection, or commissioning changes are merged because one assembly work occurrence, selected configuration, or time interval contains them. | Identify every actual transformation independently under `A.3.4`; cite direct work-to-change facts; return the exact missing-governor blocker if the receiving claim needs transformation composition. |

### C.32.P2S:9 - Consequences

The project gains one replayable architecturing flow from pressure to actual-structure feedback. Practitioners can see where the Work currently stands and which assertion is next, with the relevant pattern as a locator, without treating descriptions, decisions, eval results, Work occurrences, or separate records about them as interchangeable.

The cost is disciplined record work: the card preserves structural uncertainty, candidate plurality, accepted losses, handoffs, and stronger-structure inspection return. If one narrower pattern already answers the question, use it directly and do not open P2S.

The pattern improves cross-holon and adjacent-structure reuse. Practitioners may apply the same P2S method and Plain action sequence to different project-local flows in system, built-asset, product-family, organization-as-system, episteme, AI-agent-setup, discipline, and C.36-recovered cultural-evolution cases, after identifying the described holon in each case. Sharing that guidance does not give the flows one cross-holon identity or turn the examples into performed-work order. When architecture pressure concerns source wording such as roles, methods, practices, cultures, traditions, or styles, name the described holon and locality separately. Keep each recovered local kind, classification judgment, assignment, direct-relation or representation position, Method, Method relation structure, MethodDescription, Work claim, canon or memory episteme, recognition or selection regime, and mediation-system claim with the pattern for that claim.

The pattern does not guarantee adequacy. It makes the architecturing flow inspectable. For candidate quality, decision adequacy, evidence, assurance, gate passage, release, measurement validity, and `G.11` currentness refresh, use the relevant patterns.

### C.32.P2S:10 - Rationale

C.32.P2S belongs under C.32 because its central architecturing concern is architecture synthesis: recovering problem pressure and structural uncertainty, generating candidate selected-structure changes, preserving alternatives, making decision-ready content, and returning actual-structure feedback to the next synthesis question. During realization, identify and test every actual bounded change under `A.3.4`.

It cannot be only a C.22 pattern because a problem card does not carry architecture synthesis, decision, realization, and feedback. It cannot be only a C.30 pattern because grounded architecture and structural-view adequacy do not supply candidate construction or downstream-work instructions. It cannot be only a C.32 pattern because the palette is only one stage of the larger architecturing flow. It cannot be only C.32.PAD or C.32.ADR because decisions and records do not create the candidate space and do not realize structures. It cannot be only A.15 or E.18.1 because method and work carry-through and P2W do not supply architecture candidate synthesis or selected-structure decision content.

The P2S structural-information slots are necessary because otherwise P2S cannot explain what changes. Architecturing refines uncertainty about future structures into candidate, selected, expected, and actual structures. Descriptions and records capture only part of that content. The practitioner records which structural content is captured by descriptions, decisions, method handoffs, references to Work occurrences, separate work-record epistemes, evals, and measurements; which structure remains latent, hidden, or lost; and which stronger-structure inspection return condition returns the work to stronger structure inspection, description or view loss repair, decision repair, or a `C.29` lens use such as epiplexity, DSM, graph, coarse-graining, equivalence, or morphism.

### C.32.P2S:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.P2S. Software-system sources are used as source families and examples only; they do not narrow P2S to IT architecture.

| SoTA source to inspect | Why this source is load-bearing here | Adopt, adapt, or reject disposition | Transfer into C.32.P2S | Blocked overread |
|---|---|---|---|---|
| ISO/IEC/IEEE 42010:2022 architecture-description standard (`https://www.iso.org/standard/74393.html`) | Current architecture-description practice separates architecture, description, concern, viewpoint, view, model kind, and correspondence. | Adopt the separation of architecture and description; adapt it through the exact description, view, ADR, and publication predicates located in `C.30.AD`, `C.30.ASV`, `C.32.ADR`, `E.17`, and `E.24.PUB`; reject any takeover of FPF holon and selected-structure ontology. | P2S step 8 and `CC-C32P2S-2` keep descriptions, views, and ADR-like records as captured structural content or publication forms with exact neighboring subject assertions. | A description, view, diagram, or publication carrier is not the architecture, the project architecture decision, or performed work. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`) | Best current practitioner line for guided incremental change over declared architecture characteristics with feedback from eval practice. | Adopt guided evolutionary change and feedback; adapt source-practice fitness-function practice into `C.32.ACE` eval programs and `C.16` measurement over `C.32.ACS` rows; reject treating eval success as a decision. | P2S step 11, the eval-shaped practice row, and `CC-C32P2S-8` require architecture characteristics, eval exits, feedback, stronger-structure inspection return, and next-action triggers selected for the current question rather than one-time design settlement. | A source-practice fitness-function name, metric, or passing eval result is not the architecture characteristic, decision, or proof of realized structure. |
| Richards and Ford, `Fundamentals of Software Architecture`, 2nd ed. (`https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/`) and Ford et al., `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Current practitioner sources for architecture characteristics, trade-offs, risk, coupling, cohesion, and difficult architecture decisions. | Adopt characteristic and trade-off discipline; adapt software-system examples to holons and selected structures; reject software-only module reduction. | P2S steps 2, 7, and 11 plus `CC-C32P2S-3` separate functional demand from architecture characteristics, require accepted-loss visibility, and feed realized functional implications back without confusing kinds. | A list of qualities, trade-off discussion, or rationale text is not candidate synthesis or decision adequacy by itself. |
| Architecture synthesis and multi-objective quality-attribute optimization, including Di Pompeo and Tucci 2023 (`https://arxiv.org/abs/2301.07516`) and ATRAF 2025 (`https://arxiv.org/abs/2505.00688`) | Current research line for competing quality attributes, multi-objective trade-offs, and architecture candidate evaluation. | Adopt candidate plurality and trade-off front inspection. Use the FPF patterns that define comparison, selected-set result declaration, local choice, and decision; reject a scalar score or generated winner as sufficient grounds for selection. | P2S steps 5 and 6, the single-winner pressure-cue row, and `CC-C32P2S-5` keep candidate plurality and require the explicit comparison, selection, selected-set result declaration, local choice, or decision predicate applicable to the current use after C.32 candidate synthesis; publication remains a separate sequence. | A Pareto front, scalar score, optimization run, or generated winner does not select the architecture. |
| DSM, multiple-domain matrix, modularization, and dependency-structure practice; inherited C.32 source-anchor row for Jiang and Luo 2026 (`https://arxiv.org/abs/2604.28018`), epiplexity structural-information line (`https://arxiv.org/abs/2601.03220`), and `C.31.RSA` structure-accounting rows | Strong engineering-design line for inspecting dependency, coupling, modularity, learnable structural content, and structural loss; the inherited C.32 row also warns that functional priors and structural modularization objectives can diverge. | Adopt DSM, MDM, and epiplexity as structure-inspection lenses; adapt them through `C.29` lens refs and structural-information slots; reject matrix, cluster, compression, or epiplexity result as architecture adequacy. | P2S steps 3 and 5 and `CC-C32P2S-4` let the card cite DSM, MDM, graph, epiplexity, coarse-graining, equivalence, or morphism claims while recording preserved and lost structure. | A cluster, matrix, graph, compression, or epiplexity result is not architecture adequacy or a decision without recovered selected structures and a route to the next applicable pattern. |
| Conway correspondence, mirroring, DORA loosely coupled teams (`https://dora.dev/capabilities/loosely-coupled-teams/`), and Team Topologies (`https://teamtopologies.com/key-concepts`) | Current socio-technical architecture practice shows that typed Work, communication, tool, method, deployment, evidence, selected-structure, or architecture-side sources can enable or block transformed-side architecture content and independent change. | Adopt co-synthesis of the influence-source and transformed sides; adapt through `C.32.CONWAY`; reject organization labels, communication diagrams, architecture relations, claims, or structures as acting Systems or direct transformation participants. | The P2S architecture-influence branch, Show C, and `CC-C32P2S-9` require exact C.30 architecture sides or modal claims, an independently typed influence source and direct relation, the changed referent, and any actual A.3.4 transformation as separate objects. | Organization labels, team diagrams, or communication patterns do not settle transformed-side architecture content, acting identity, Work attribution, or transformation participation; they enter only through their exact kinds and direct relations. |
| NASA Systems Engineering Handbook decision and trade-study practice (`https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf`), Michael Nygard's ADR practice (`https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions`), MADR 4.x (`https://adr.github.io/madr/`), and `C.32.ADR` source-anchor rows | Non-software domains often publish architecture choices as trade studies, engineering memos, review records, or certification rationale rather than Markdown ADR files; ADR practice supplies compact status, context, decision, options, consequences, links, and update conditions. | Adopt record-function discipline; adapt carrier form to project domain through the predicates and publication forms defined in `C.32.ADR`, `E.17`, and `E.24.PUB`; reject ADR file form as mandatory or authoritative by itself. | P2S step 8 and the Relations boundary treat decision records by section function and reader use: project architecture decisions require an exact `C.32.PAD` assertion, while record projection uses the `C.32.ADR` description. | ADR file form is not mandatory and does not create a second decision authority. |
| FPF `C.18`, `C.19`, `E.23`, and `G.11` with NQD, OEE, improvement, telemetry, freshness, and decay practice | Modern architecturing happens under evolution; retained alternatives, stepping stones, feedback, and decay affect the next synthesis question. | Adopt archive, front, pool, improvement, telemetry, freshness, and decay distinctions; adapt them as exits to the next applicable pattern; reject `G.11` refresh state or archive state as architecture choice. | P2S steps 6 and 11 record archive, front, and pool refs, improvement-loop refs, telemetry, actual-structure observations, decay, stronger-structure inspection return, and return or repair refs selected for the next question without merging the meanings defined by their patterns. | Archive membership, improvement-loop status, telemetry, or freshness signal does not decide architecture by itself. |

**SoTA-anchor currentness boundary.** Use each SoTA source-anchor row only for the P2S card field, P2S method or architecturing-transformation-flow step, boundary, or repair named in the row. Recheck the row when the source-practice anchor, applicable FPF pattern, described holon, structure kinds, architecture characteristics, architecture-influence relation, eval mode, or project use changes.

### C.32.P2S:12 - Relations

- **Builds on:** `A.1` and `A.1.SCR` for an existing system boundary, `A.15.6` for project system-of-interest designation and intended-system separation, `A.1.STM` when the missing outside-to-inside dependency must be located, `C.22.2` for problem-side recovery, `C.30`, `C.30.AD`, and `C.30.ASV` for grounded architecture, architecture-description adequacy, and structural-view adequacy, `C.33` and `C.34` for structural-information capture and preservation, `C.35` to recover the kind of a generated or discovered result and assess its adequacy for the next architecture use inside the flow, `C.32` for candidate architecture synthesis, `C.32.HCS`, `C.32.ACS`, and `C.32.ACE` for characteristic starter heads, project criteria rows, and eval programs, `C.25` for Q-bundles, `C.31` family patterns for modularity, reusable structure, and scale preference, `C.29` for mathematical-lens use when claimed, `E.17` for a source-backed publication face and source return, and `E.24.PUB` for the publication occurrence and audience availability.
- **Uses:** `A.22.CGUS` for the P2S unfolding-structure block when problem pressure, structure uncertainty, candidate synthesis, decision linkage, work linkage, and actual-structure feedback must remain inspectable as one constraint-governed unfolding structure; `E.18.3`, `C.30.TFS-REL`, `E.18`, and `A.3.4` when architecture pressure concerns transformation-flow or bounded change; `C.30.ILC`, `C.32.MLAO`, and `B.2` family patterns when cross-scope, interlevel, interlayer, meta-holon, emergence, or reidentification pressure changes the candidate frame; `C.32.CONWAY` when co-synthesis of exact influence-source and transformed-side architecture content is current; `C.32.FAIL` when a recognizable architecture-synthesis failure becomes a repair action.
- **Patterns for the next questions:** `A.19.CPM`, `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, and `C.11` for comparison, selection, archive, front, pool policy, selected-set result declaration, and local choice; `C.32.PAD`, `C.32.ADR`, and `C.32.ADA` for project architecture decision, ADR-like projection, and decision adequacy; `C.30.AD` for architecture descriptions; `A.6.3.NAR` for architecture-mediated narrative renderings; `E.17` for source-backed publication faces and source return; `E.24.PUB` for publication occurrences and audience availability; `A.3.1` for Method identity and `A.3.2` for `MethodDescription` membership; `A.15`, `A.15.1`, `A.15.2`, and `A.15.5` for method-work alignment, performed work, work plan, and readiness; `A.3.4` for each actual bounded change; the pattern for the predicate, or `A.6.RCD`, for Work-to-change claims and blockers; `A.15.PROD` for separate local production-work, entity-identity-inception, and production-completion claims; `C.16`, `C.25`, `C.29`, `C.32.ACE`, `E.23`, `G.11`, and `E.18` for measurement, Q-bundle, mathematical lens, eval, improvement, currentness refresh, and transformation-flow slice-local refresh.
- **Boundary:** Use C.32.P2S for the connected project-local architecturing transformation flow from architecture-relevant pressure to subject-side actual structures recovered under `A.22` from obtaining facts, and then to feedback. `C.33`, `C.34`, and `C.35` deepen the structural-information slot group already present in P2S; they do not move the whole connected flow out of P2S. C.32.P2S does not define or test architecture claims, architecture descriptions, structural views, candidate palettes, comparison, selected-set result declarations, decisions, ADR-like publications, publication forms, publication-use claims, methods, Work, measurement, eval, evidence, assurance, gate, release, improvement, currentness refresh, or formal structural-information theory.

### C.32.P2S:13 - Footer marker

Use `C.32.P2S` for one reader-facing problem-to-structure architecturing flow: pressure and structural uncertainty are carried into candidate, selected, and expected structures, then through domain work to independently grounded actual changes and subject-side actual structures, with descriptions, evaluations, and return or repair exits selected for the next question.

### C.32.P2S:End

