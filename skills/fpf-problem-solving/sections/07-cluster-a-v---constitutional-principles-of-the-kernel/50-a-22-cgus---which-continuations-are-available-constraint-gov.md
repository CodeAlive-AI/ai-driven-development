## A.22.CGUS - Which Continuations Are Available? — Constraint-Governed Unfolding Structure (CGUS)

> **Type:** A.22 specialization of `U.Structure`
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.22.CGUS:0 - Use This When

Use this pattern to work out which continuations the conditions of a case allow, including when a diagram shows only one path or no candidates have yet been named. Start with the recipient's question:

> Must I establish that this particular continuation is available, that some continuation exists, or which continuations make up the full set? If I must choose a way to proceed, what will let me identify and use it in time?

Use the required result, the choices open to the actors and the governing constraints to find potential continuations. A named way needs its own conditions. An existence claim can also follow from a rule covering the possible cases. A claim to give all the available ways, or to exclude them all, needs grounds covering the allowed range. Mark a candidate `unknown` when a missing fact or rule prevents deciding it. One established blocking condition can already exclude it. Stop when the answer supplies the requested use.

Open the formal branch when a named use needs the identity and qualification of the unfolding organization as a CGUS. A `ConstraintGovernedUnfoldingStructure` (CGUS) is one A.22 `U.Structure` whose locally named loci, constituents, obtaining relations, and constraints define at least two potential continuations across the cases allowed by those constraints. A separate result says which alternatives are enabled, disabled, unknown, or error for one case and time window.

Do not use CGUS merely because a card, graph, table, narrative, prompt path, or README line looks route-shaped. A single recommendation or displayed sequence is not enough. The structure may branch, join, cycle through subject relations, remain partially ordered, or leave several alternatives live at once. A result with zero or one enabled alternative can still concern that same branching structure.

**What changes in practice.** Practitioners can develop alternatives from the work required or assess alternatives already proposed. Their answer supplies the continuation, existence finding or complete range the recipient needs. They keep potential structure separate from the result for the present case, and they mark an alternative `unknown` when an unresolved fact or rule prevents deciding it. Display order alone neither prescribes nor performs Work.

### A.22.CGUS:1 - Problem Frame

FPF often needs to explain how several identified things and relations constrain what may follow without turning that explanation into a workflow. The shared object is one A.22 structure. CGUS adds local loci and a membership test for potential branching; a continuation judgement then evaluates one case.

Descriptions, publication forms, evidence, assurance, authorization, work plans, performed Work, architecture claims, and mathematical models can be used alongside that structure. They remain separate objects and claims under the patterns that define or test them.

### A.22.CGUS:2 - Problem

A route-shaped explanation can hide the relations and constraints that make an alternative available. Readers then follow the displayed order as if it were a required procedure, or they treat a condition label as proof that the condition is true now.

The opposite repair is also harmful: authors replace the simple decision question with a large admission, replay, publication, and assurance package. The formal package becomes harder to use than the misleading card it was meant to correct.

### A.22.CGUS:3 - Forces

| Force | Tension |
| --- | --- |
| Useful explanation vs workflow overread | A visible path helps a reader, but Work may be nonlinear, interrupted, iterative, or arranged by another Method or plan. |
| Potential structure vs present result | The structure can retain several possible branches while the present case enables none, one, or several. |
| Plain entry vs formal replay | An ordinary correction should be cheap; qualification and replay still need enough identity and relation detail to be checked later. |
| Description vs described structure | A card, graph, table, or narrative can describe a structure without creating it. |
| Reuse vs copied mini-patterns | CGUS needs exits to relation, transformation-flow, work, publication, and assurance patterns without copying their architectures. |

### A.22.CGUS:4 - Solution

#### A.22.CGUS:4.1 - Ordinary branch

Decide what would let this recipient act or answer. For example, a venue confirms that a room has been booked for the company’s rehearsal tomorrow and omits the room name. This establishes an existing booking. If the musicians must choose a building before boarding and cannot change it later, the organizer needs the building by departure. If the order asks for the booked room by name, the organizer also needs its identity by the agreed time. Confirmation for the East Room supplies that answer while leaving open whether the company also booked the West Room. For a complete list of its rooms, the organizer needs a booking record or rule that covers all of them. Confirmation naming East as the company’s sole room establishes the booking, identifies a booked room and completes the list. Giving directions to the right building also requires knowing where East is.

1. State the question, the relevant case and time, and the range of results and circumstances it covers. For a decision someone must make, establish who can decide and by when. A question about whether a continuation exists can already have an answer even if no chooser has been designated.
2. For a specified move, take it as the candidate. When finding a way forward is your task, work back from the result each move must make possible. Which change of arrangement, source, timing or actor would provide a genuinely different way under the constraints? Build or reuse candidate continuations on that basis. Where the route leaves a choice, establish who can choose and which information will be available in time. A continuation can also be fixed by its conditions or a schedule.
3. State what must hold for each continuation on which the answer relies. Retain the distinctions that change availability or the grounds the recipient must explain, including dependencies between constituent actions under §4.1.1.
4. Apply those conditions to the facts for this case and window. When the choice may wait for more information, establish what the chooser will know in time and which response will then be possible.
5. Return the conclusion requested. For an identified candidate, give `available`, `blocked` or `unknown` with its grounds. One enabled candidate suffices to establish existence. A rule may also establish existence without identifying the same available action in every case. For a complete set, justify that the candidates or the generating rule cover every admissible continuation and determine which satisfy the conditions. Report a partial set or the outstanding distinction where the grounds fall short. An evaluation error retains its own status.

For example, suppose the rules of a design review permit exactly two review outcomes, acceptance and repair. The team wants the current status of both. Acceptance needs both checks to pass. Repair needs at least one failed check and a repair proposal that concerns this design.

| Alternative | Present facts | Result shown on the card |
| --- | --- | --- |
| Accept the design | Thermal check failed; service check passed. | `blocked — thermal check failed` |
| Repair the design | A check failed and a repair proposal exists, but the proposal-to-design relation has not been established. | `unknown — proposal target not established` |

That corrected card is already useful. It keeps both potential alternatives visible and refuses to invent the missing relation. Retain the rules, facts, and result when the ordinary answer must be reconsidered or compared later. Continue into formal qualification only when a named use depends on the organization's CGUS identity or membership.

When retaining or handing over this card separately, include the two rules above or a usable return to them so the recipient can reconsider availability after the facts change.

##### A.22.CGUS:4.1.1 - Conditions through constituent and encompassing work

When a continuation is a way of performing work, recover the constituent–whole relations in the relevant Method and Work structures that can change availability. For a design, work back from what the encompassing undertaking must supply to the constituent actions and their conditions. For an occurrence, recover what encompassing work was actually performed through those actions. B.1.5.EW supplies that recovery; knowing a Method's description does not supply the capability or resources to perform it.

Distinguish conditions needed at entry, conditions that must remain satisfied during combined performance, and the result required by the encompassing use. In particular:

- a constituent may be individually performable but fail in the needed coordination;
- adequate local resources may be insufficient when constituents share them;
- a constituent result may satisfy its own postcondition while leaving the whole's result unresolved.

For each relevant condition, state what it concerns and how it affects this continuation. Reuse an understood connection or adequate existing basis. Failure of a necessary condition blocks the dependent continuation. A missing fact leaves it unknown when the outstanding fact could change the result. An independent way to learn, obtain support or change the arrangement can remain available. Capability belongs to its performer and conditions under A.2.2; prospective resources and support remain prospective until available.

In the formal branch, express these dependencies with the existing constituents, selected relations, applied constraints and continuation judgements. A temporal edge alone cannot express that one action constitutes part of another ongoing work. Nor does a nested flow position establish Method or Work parthood. A diagram may show the relations together when their meanings remain recoverable.

A constituent's postcondition supports the encompassing conclusion only through the relevant composition and result-use conditions. An expected postcondition is not an observed result. If the displayed account omits conditions needed to perform the whole, state the narrower question it answers. A constituent hierarchy without potential alternatives does not require CGUS qualification.

#### A.22.CGUS:4.2 - Formal qualification branch

Use the four A.22 discriminators to identify one `U.Structure`:

- its constituent references;
- the obtaining relation occurrences it selects;
- the applied constraint claims;
- the named selection-use frame: the question, admissible action, and stop or return condition. Any optional explanatory overread follows F.19:4 and remains outside the identity basis.

CGUS membership adds locally declared loci and bindings that expose how those constituents matter to the unfolding question. The selected relations and constraints must define at least two potential continuation candidates across allowed cases. The current continuation result, a description, or a publication field adds no structure-identity discriminator.

```text
selectedCGUSRef: one A.22 U.Structure
A22IdentityBasis:
  selectedConstituentRefs[]
  selectedObtainingRelationOccurrenceRefs[]
  appliedConstraintClaimRefs[]
  namedSelectionUseFrame:
    questionOrAction: selection question
    admissibleAction
    stopOrReturnCondition
forbiddenOverread?: optional explanation outside A22IdentityBasis
constraintGovernedProfileBasis:
  locusBindingRows[]:
    locusRef: <selectedCGUSRef, locusId>
    locusMeaning: why this constituent matters to this question
    selectedConstituentRef
  potentialContinuationRows[2..*]:
    continuationCandidateRef
    constrainingRelationOccurrenceRefs[]
    appliedConstraintClaimRefs[]
```

`forbiddenOverread?` and `groundedForbiddenOverread?` name the same optional explanation. Use F.19:4's plausible-reader test to decide whether it is useful here.

A CGUS locus belongs to this structure, not to a reusable relation declaration:

```text
CGUSLocusRef := <selectedCGUSRef, locusId>
CGUSLocusBinding := <selectedCGUSRef, locusId, locusMeaning, selectedConstituentRef>
```

The constituent must already belong to the A.22 identity basis. A locus binding neither changes that constituent's kind nor creates a relation. Do not use an A.6.5 `SlotSpec` as a free-standing structure position.

When replay must identify one participant in a relation occurrence, retain the relation definition, the occurrence, the participant order, and the participant binding:

```text
RelationParticipantLocator := <relationDefinitionRef, relationOccurrenceRef, participantOrder, participantRef, relationSignatureRef?, slotSpecRef?>
```

Add a `RelationSignature` and its declaration-local `SlotSpec` together only when an existing reusable declaration is needed for replay. Neither declaration value substitutes for the obtaining occurrence. The CGUS has no ambient context field.

For a finding about one candidate, evaluate its condition. For a current-set result, establish the range of candidate continuations and which of them satisfy their conditions in this case. An immediate local use may keep the following values in the explanation; persistence or replay may place them in an ordinary C.2.1 result episteme.
```text
ContinuationJudgementResult:
  selectedCGUSRef
  continuationCandidateRef
  basisRows[]:
    basisKind: conditionEvaluation | obtainingRelation
    conditionEvaluation?:
      conditionPredicateOrTestRef
      applicabilityResult
      caseInputRefs[]
      currentFactOrEvidenceRefs[]
      requiredPolarity
      observedOutcome: satisfied | notSatisfied | unknown | error
    obtainingRelation?:
      relationDefinitionRef
      relationOccurrenceRef
      participantRefsInPredicateOrder[]
      currentFactOrEvidenceRefs[]
    dependentSelectedRelationOccurrenceRefs[]
  qualificationWindow
  result: enabled | disabled | unknown | error
  reason

CurrentContinuationSetResult:
  selectedCGUSRef
  caseInputRefs[]
  qualificationWindow
  judgementResultRefs[]
  enabledContinuationCandidateRefs[]
  disabledContinuationCandidateRefs[]
  unknownContinuationCandidateRefs[]
  errorContinuationCandidateRefs[]
  stopOrNextAction
  recheckConditions[]
```

A claim reference identifies the claim being applied; it does not show that the test applies or that its condition is satisfied. An obtaining relation is not a condition claim. Keep these two basis branches distinct and derive the case result only from completed judgements. Apply the candidate’s condition logic: for example, one false required conjunct can establish `disabled` despite another unknown conjunct. Retain that unknown basis value; it is not thereby satisfied. An evaluation failure yields `error` under the applicable test, not an invented fact about the candidate.

The membership test concerns potential topology. Changed facts, evidence, test outcomes, or time windows normally change a judgement and the current set, not the structure. Reidentify the A.22 structure when a constituent, selected obtaining relation occurrence, applied constraint, or named use frame changes. Reapply CGUS membership when a locus binding or potential-continuation row changes.

#### A.22.CGUS:4.3 - Four separate decisions

| Decision | Passing basis | Lower result |
| --- | --- | --- |
| A.22 identity and CGUS membership | The four A.22 discriminators identify one structure; its local loci, relations, and constraints define at least two potential continuations across allowed cases. | Name the missing discriminator, binding, relation, constraint, or candidate. Keep the artifact as an explanation. |
| Continuation result for this case | Each candidate retains its condition-evaluation and obtaining-relation basis rows as applicable. A condition-evaluation row keeps the test, applicability, inputs, required polarity, and observed outcome; an obtaining-relation row keeps the definition, occurrence, and ordered participants. Keep the relevant facts or evidence, time window, and an `enabled`, `disabled`, `unknown`, or `error` result. | Mark the affected candidate unknown when the gap prevents deciding its condition; retain an independently established disabled result. Do not revoke an independently established structure. |
| Description or demonstrative-slice adequacy | The description says what it shows and omits for its declared use. Use C.33 only when a carrier's loss affects a declared architecture use within C.33's scope. | Narrow or correct the description. Missing publication or loss material does not deny the structure. |
| A stronger neighboring claim | The method, Work, evidence, assurance, gate, architecture, publication, currentness, or mathematical claim passes its own definition or test. | Stop only that stronger use and name its missing rule or basis. |

Potential branches and joins remain part of the structure even when the present case enables one or none. A linear teaching slice neither removes the other topology nor fixes the order of performed Work.

#### A.22.CGUS:4.4 - Explanations, descriptions, and the non-workflow boundary

An ordinary explanation keeps the subject designated by its claims. When its episteme identity matters, recover that independently identified `EntityOfConcern` under C.2.1. It may already be an A.22 structure whose CGUS membership is unresolved. An assertion of CGUS membership still requires its qualification basis.

After qualification, a whole-structure description may describe loci, bindings, relations, constraints, potential branches, case results, and relevant omissions. A separate demonstrative slice may show one traversal for a declared teaching or comparison use. That slice is a C.2.1 episteme: its claim content, the qualified CGUS as `EntityOfConcern`, and its effective reference scheme jointly recover its identity. `DemonstrativeUnfoldingSlice@Context` is readable lineage for this possibility, not a `U.Kind` or a slice by itself. The slice neither creates nor reidentifies the structure. Use C.33 only when hidden or lost structure in its carrier matters to a declared architecture use within C.33's scope.

Where a slice shows one selected pattern use, it may recall the difficulty through the pattern's `Problem frame` or `Problem`, or recall the way of addressing it through the `Solution`. To show that same use in either form, preserve the selected pattern, working subject and question or proposed use, current conditions, expected result, stop or continuation, and relevant locus bindings. Changing between those formulations changes only the description when the selected pattern use and the qualified structure remain the same. A.22 structure identity still depends on its constituents, selected obtaining relations, applied constraints and named selection-use frame; CGUS membership additionally depends on its locus bindings and at least two potential continuations. Question or action labels establish neither.

Displayed words such as *move*, *next*, and *path* remain ordinary language unless a stronger claim requires another kind. A proposed action, a plan item, a `U.WorkPlan`, dated `U.Work`, and an actual `U.Transformation` are different values. Use `E.10.MOVE`, A.15, and A.3 only when that distinction changes the claim; a display performs and authorizes nothing.

For a transformation-flow use, apply `E.18.3`. It owns the choice among one TFS, one parent-relative `SubflowRef`, or an E.18.NET network and the corresponding position and demonstration locators. CGUS keeps only its local locus bindings and potential topology; it does not copy the network's members, positions, valuations, Work, transformations, or tags.

Cite another pattern only when its content supplies a needed definition, constraint, test, method, evidence rule, or assurance rule. For example, use C.30 for an architecture claim and C.32 for architecture-candidate synthesis, E.23 for repeated quality improvement under a declared evaluation, G.11 for source currentness, C.29 for a mathematical-lens claim, A.10 when the source-to-use account is implicit or must remain replayable, or B.3 for a named assurance claim.

If a durable name or a relation between local senses is the question, use F.17, F.18, or F.9 after the value has been recovered. Do not copy their naming or Bridge procedures into this pattern. Entry cards and publication faces remain under E.11 and E.17.

#### A.22.CGUS:4.5 - Replay and change localization

Replay structure identity from the four A.22 discriminators. Replay CGUS membership from the local locus bindings and potential topology. Replay the case result from each candidate's basis rows, retaining the values required by each applicable condition-evaluation or obtaining-relation branch in `4.2`, the relevant case inputs and facts or evidence, dependent occurrences, time window, continuation result, and reason.

Localize change before reopening wider work. A changed constituent, selected occurrence, constraint, or use frame can reidentify the A.22 structure. A changed locus binding or potential-continuation row reopens CGUS membership. A changed fact, evidence item, test result, or time window normally reopens only the affected judgement and current set. A changed omission reopens the affected description use. A changed neighboring claim stays with the pattern that defines or tests it.

### A.22.CGUS:5 - Complete Worked Case

Return to the design review from `4.1`. The team now needs to determine whether reviews across editions use the same qualified unfolding structure or a different one. Recover the formal basis below for that comparison.

```text
selectedCGUSRef: DesignReviewAlternatives@DR-27
A22IdentityBasis:
  selectedConstituentRefs[]:
    DesignCandidate-A
    RepairProposal-A
    AcceptCandidate-Continuation
    RepairCandidate-Continuation
  selectedObtainingRelationOccurrenceRefs[]:
    RepairProposalTargetsCandidate@DR-27
  relationOccurrenceRecoveryRows[]:
    - relationOccurrenceRef: RepairProposalTargetsCandidate@DR-27
      predicateDefinitionRef: RepairProposalTargetsDesignCandidatePredicate
      participantRefsInPredicateOrder[]: [RepairProposal-A, DesignCandidate-A]
  appliedConstraintClaimRefs[]:
    AcceptIfBothChecksSatisfied
    RepairIfAnyCheckViolatedAndProposalTargetsCandidate
  namedSelectionUseFrame:
    questionOrAction: which review continuations satisfy the two-check rule for DesignCandidate-A?
    admissibleAction: show enabled, disabled, unknown or error results for the current case
    stopOrReturnCondition: recheck a case when its result inputs or window change; reidentify the structure when its selected basis changes
forbiddenOverread?: displayed order as performed Work, or an available branch as authorization
constraintGovernedProfileBasis:
  locusBindingRows[]:
    - <DesignReviewAlternatives@DR-27, candidate, design under review, DesignCandidate-A>
    - <DesignReviewAlternatives@DR-27, repair-proposal, proposed repair, RepairProposal-A>
    - <DesignReviewAlternatives@DR-27, accept, accept continuation, AcceptCandidate-Continuation>
    - <DesignReviewAlternatives@DR-27, repair, repair continuation, RepairCandidate-Continuation>
  potentialContinuationRows[]:
    - AcceptCandidate-Continuation, constrained by AcceptIfBothChecksSatisfied
    - RepairCandidate-Continuation, constrained by RepairIfAnyCheckViolatedAndProposalTargetsCandidate
caseBasis:
  checkResultRefs: [ThermalCheckResult-A, ServiceCheckResult-A]
  resultAboutCandidateOccurrences:
    - <ThermalCheckAboutCandidate@DR-27, CheckResultAboutDesignCandidatePredicate, [ThermalCheckResult-A, DesignCandidate-A]>
    - <ServiceCheckAboutCandidate@DR-27, CheckResultAboutDesignCandidatePredicate, [ServiceCheckResult-A, DesignCandidate-A]>
continuationJudgements[]:
  - candidate: AcceptCandidate-Continuation
    basisKind: conditionEvaluation
    predicateOrTest: AcceptIfBothChecksSatisfied
    applicability: both named results concern DesignCandidate-A
    caseInputs: [ThermalCheckResult-A, ServiceCheckResult-A]
    currentFacts: [thermal violated, service satisfied]
    requiredPolarity: both satisfied
    observedOutcome: notSatisfied
    dependentOccurrences: [ThermalCheckAboutCandidate@DR-27, ServiceCheckAboutCandidate@DR-27]
    window: ReviewWindow-DR-27
    result: disabled
    reason: thermal check is violated
  - candidate: RepairCandidate-Continuation
    basisKind: conditionEvaluation
    predicateOrTest: RepairIfAnyCheckViolatedAndProposalTargetsCandidate
    applicability: the proposal concerns DesignCandidate-A
    caseInputs: [ThermalCheckResult-A, ServiceCheckResult-A, RepairProposal-A]
    currentFacts: [thermal violated, service satisfied, RepairProposalTargetsCandidate@DR-27 obtains]
    requiredPolarity: at least one violation and the targeting relation obtains
    observedOutcome: satisfied
    dependentOccurrences: [ThermalCheckAboutCandidate@DR-27, ServiceCheckAboutCandidate@DR-27, RepairProposalTargetsCandidate@DR-27]
    window: ReviewWindow-DR-27
    result: enabled
    reason: one check is violated and the repair proposal concerns this design
currentContinuationSet: enabled [RepairCandidate-Continuation]; disabled [AcceptCandidate-Continuation]; unknown []; error []
stopOrNextAction: show repair as available; recheck when the case results or window change
```

The structure has two potential continuations although this case enables only repair. The selected proposal-to-design relation belongs to its identity basis. Thermal and service result epistemes, and their about-candidate relations, belong to the current case basis; they are not constituents or selected relation occurrences of this structure.

If the proposal-to-design relation cannot be established, this formal structure claim remains provisional. The ordinary explanation can still report repair as unknown. Do not treat an unknown identity-bearing relation as an established constituent of a qualified CGUS.

A later passing thermal check is a different result episteme and supplies a new case input. With service still satisfied, acceptance becomes enabled and repair becomes disabled. The selected design, proposal, continuation candidates, proposal-to-design relation, constraints, use frame, loci and potential topology are unchanged, so the same CGUS remains available for that new case.

Now hold the original facts fixed and change the review rule. In the second edition acceptance still requires both checks to pass. Under its remit the repair branch can take a targeted proposal only when the service check is violated. In DR-27 the thermal check failed and the service check passed. The first edition therefore makes repair available. The second makes neither acceptance nor repair available for this case. The applied repair constraint has changed. The second structure binds its four loci to the same design, proposal, acceptance continuation and repair continuation respectively. It keeps the proposal-to-design relation and the selection use. Its potential repair continuation now takes the service-violation constraint. The unavailable repair in this case remains a potential branch for a case with a service violation and a targeted proposal. A new printed edition that merely rephrased the original rule while preserving the selected constituents, relations, applied constraints, use frame, bindings and potential branches could still describe the same structure.

#### A.22.CGUS:5.1 - A missing intermediate capability changes the continuation

In this constructed learning case, a dancer has the strength and static axis control needed by a figure and can recall its sequence. The known limitation is maintaining balance during its required rotation. The figure's continuation depends on that coordinated performance, not just on adequate strength and memory.

| Alternative | Relevant conditions in this case | Present result |
| --- | --- | --- |
| Perform the complete figure under its intended conditions. | The required balance during rotation cannot yet be sustained. | Unavailable for the intended performance; naming the figure or its steps does not remove the gap. |
| Practise the rotational coordination under a suitable reduced demand. | A domain-appropriate exercise, suitable space and the needed support are available in the stipulated case. | Available as practice of the intermediate performance. It does not establish ability to perform the full figure. |

During the rotation, balance coordination would constitute part of turning; that turn would constitute part of the figure. These are connections through performance, not three successive tasks. The practice alternative can exercise the first connection without already performing the intended figure.

When the coordination can be sustained, return to what the dancer is asked to perform. If the required turn and the other constituents can be performed together under the conditions of that figure, the capability claim can extend to it. If a partner steadies the turn, establish which balance the dancer maintained and what the partner supplied. That performance can demonstrate the supported figure. For an unaided figure, use grounds for that dancer sustaining the required balance without the partner’s support. Use adequate prior performances, a domain rule or a suitable trial when a wider capability is at issue. The case condition and its continuation judgement can change without changing the potential alternatives. The subject's training Method supplies the exercise and assessment; CGUS makes their effect on the available continuation explicit.

### A.22.CGUS:6 - Bias-Annotation

| Bias risk | Mitigation |
| --- | --- |
| Workflow bias | Ask about alternatives and conditions; use work and method patterns only for work-order or way-of-doing claims. |
| Display bias | Treat cards, graphs, tables, narratives, and entry lines as explanations or descriptions, not as the structure. |
| Formality bias | Start with the ordinary decision answer and open formal qualification only for a named later use. |
| Consumer bias | Keep transformation-flow, architecture, improvement, currentness, evidence, and publication details in their patterns. |
| Lexical bias | Words such as *route*, *path*, *loop*, *workflow*, *graph*, or *sequence* establish no CGUS by themselves. |

### A.22.CGUS:7 - Conformance Checklist

| ID | Passing condition | Failed-check repair |
| --- | --- | --- |
| **CC-CGUS-1 Identity and profile.** | The four A.22 discriminators identify one `U.Structure`; local locus bindings, relations, and constraints define at least two potential continuations across allowed cases. | Recover the missing value or keep the artifact as an explanation. |
| **CC-CGUS-2 Local loci and relation participants.** | Every `CGUSLocusBinding` uses a locus declared inside this CGUS and binds one constituent for a stated meaning. A needed relation participant retains its definition, occurrence, order, and binding; `RelationSignature` and `SlotSpec` appear together only for declaration-level replay. | Restore the locus or complete relation-participant basis. Never use a free-standing `SlotSpec` as a structure position. |
| **CC-CGUS-3 Explanation and description separation.** | An ordinary or persisted provisional explanation concerns the subject of its claims; this may be an already identified A.22 structure whose CGUS membership remains unresolved. Post-qualification descriptions and slices concern the CGUS. None is the structure or a membership condition. | Restore the right `EntityOfConcern` or keep the explanation ordinary. |
| **CC-CGUS-4 Current continuation result.** | Each judgement retains its basis rows with the values required by each applicable condition-evaluation or obtaining-relation branch in `4.2`, the relevant case inputs and facts or evidence, dependent occurrences, window, continuation result, and reason. A result for a named candidate or for existence can suffice on its own. Reporting the complete enabled set, including an empty set, requires covering the candidate domain as well as establishing availability. | Apply the candidate’s condition logic; mark it unknown only when the missing value prevents deciding the result, and retain evaluation errors separately. |
| **CC-CGUS-5 Separate decisions.** | Identity and membership, case result, description adequacy, and each neighboring claim are judged separately. | Reopen only the affected decision. |
| **CC-CGUS-6 Work-order boundary.** | The selected structure and display expose branches and conditions. | Put any prescribed or performed Work order under the Method, work-plan, or Work pattern that establishes it. |
| **CC-CGUS-7 Graph-shaped coverage.** | Branches, joins, cycles, partial order, and live alternatives are preserved or explicitly omitted for the declared use. | Keep a chain provisional or state what its demonstrative slice omits. |

### A.22.CGUS:8 - Common Anti-Patterns And Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Pretty route as ontology** | A card or graph is treated as the structure. | Keep it as an explanation; qualify the structure independently. |
| **Condition label as result** | A label or claim reference is treated as proof that a continuation is enabled. | Apply the test or recover the obtaining relation and facts. Mark the continuation `unknown` when the missing basis prevents deciding it. |
| **One enabled branch as one-branch structure** | The present result erases other potential continuations. | Keep potential topology and the case result separate. |
| **Formal package or field count first** | A simple correction requires replay fields, or authors add references merely to raise schema completion. | Use the ordinary branch and stop when it answers the question. In formal use, retain only fields consumed by qualification or replay and test whether readers recover the right alternatives and smallest repair. |
| **Displayed order as Work** | A teaching slice becomes a project procedure or authorization. | Use the applicable Method, work-plan, or Work pattern for work order, A.21 for a gate decision, and the permission or authority rule for authorization, only when that claim is made. |
| **Consumer architecture copied inward** | CGUS repeats transformation-flow locators, naming procedures, or catalogs of neighboring claims. | Keep the local structural rule and exit to the pattern that defines or tests the other claim. |

### A.22.CGUS:9 - Consequences

CGUS preserves the usefulness of a route-shaped explanation without making it a workflow. Ordinary use is cheap: decision, alternatives, conditions, facts, result, and stop. Formal use costs more because structure identity, CGUS membership, the case result, and any description or neighboring claim must remain separately checkable.

This separation prevents a changed fact from reidentifying a stable structure and prevents a missing publication, evidence, or assurance value from erasing a useful ordinary answer.

### A.22.CGUS:10 - Rationale

The recurring object is a thin specialization of A.22 `U.Structure`, not a new root kind. The cited constraint-based, object-centric, artifact-centric and acausal approaches provide different ways to express relations and constraints beyond one displayed execution path. CGUS uses this design question while retaining its own A.22 identity and continuation tests.

The same distinction appears in acausal engineering models: component relations and constraints can be stated before an analysis chooses a calculation direction. FPF adopts only that general separation. Mathematical models, analyses, executions, results, and publications keep their own kinds and rules.

### A.22.CGUS:11 - SoTA-Echoing

| Source or practice anchor | FPF adoption | Boundary |
| --- | --- | --- |
| Aaron Küsters and Wil M.P. van der Aalst, [“OCPQ: Object-Centric Process Querying & Constraints”](https://arxiv.org/html/2506.11541v1), 2025 | Comparison for queries and constraint checks over typed objects and events, including linked instances and their qualified relationships in the cited 2025 work. | A query or result is not the CGUS. |
| JuliaHub, Dyad [Components and Reuse](https://help.juliahub.com/dyad/stable/manual/components.html) and [Analyses](https://help.juliahub.com/dyad/stable/manual/analyses.html) documentation | Engineering comparison for reusable equation-based component models and connections, separately defined analyses, and their solution objects. | FPF imports neither Dyad ontology nor its tools. Modelica 3.7 is retained only as historical acausal-modeling lineage. |
| Declare/MP-Declare, DCR, artifact-centric/GSM, and CMMN work | Lineage for declarative constraints, live alternatives, stages, guards, and weakly structured case work. | These are not current authority for a universal FPF process calculus; their notation and workflow ontology are not imported. |
| FPF pattern-language practice | Ordinary explanations may precede qualification; descriptions and demonstrative slices may follow it. | Publication form alone supplies neither CGUS qualification grounds nor specification force. |


### A.22.CGUS:12 - Relations

Specializes: one A.22 `U.Structure` whose local locus bindings, obtaining relations, and constraints define at least two potential continuations across allowed cases. Continuation judgements, descriptions, slices, loss notes, and neighboring claims are separate results or uses.

Specialized by: `E.18.3` when the same structure also satisfies its transformation-flow condition. Local applications include architecture, abduction, improvement, narrative, grounding, currentness, and first-entry uses only when their own constituents, relations, constraints, and use frames are recoverable.

Coordinates with: `A.6.P` and A.6.5 for relation occurrence and reusable declaration precision; `E.18`, `E.18.NET`, and `E.18.3` for transformation-flow substrates; `A.3` and `A.15` for Method, plan, Work, and Transformation claims; `A.10` for claim-bound evidence reliance, `B.3` for a named assurance claim, `A.20` for internal-constraint validity, and `A.21` for gate decisions; `C.30` for architecture claims and C.32 for architecture-candidate synthesis; `E.23` for repeated quality improvement under a declared evaluation; `G.11` for currentness; `C.29` for mathematical-lens use; `C.33` for description loss that affects a declared architecture use; `E.11` for entry, `E.17` for a source-backed reader face, and `E.24.PUB` for publication occurrence, form, carrier, audience, bounded use, and availability; and `F.17`, `F.18`, and `F.9` for source-local sense, durable naming, and Bridge claims.

Does not replace any pattern that supplies the definition, constraint, test, method, evidence rule, or assurance rule for a neighboring claim.

Use `F.19` for ordinary precise-plain-language repair and the plausible-reader test for an optional explanatory overread.

### A.22.CGUS:End
