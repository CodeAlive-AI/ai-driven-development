## A.22.CGUS - Constraint-Governed Unfolding Structure

> **Type:** A.22 specialization of `U.Structure`
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### A.22.CGUS:0 - Use This When

Use this pattern when a diagram or explanation shows several possible next actions, but readers may mistake one displayed path for the required work sequence. Start with one ordinary question:

> Which alternatives are available now, and what condition blocks each one?

Name the decision, the visible alternatives, the condition for each alternative, and the facts available now. If a needed fact or rule is missing, mark that alternative `unknown` and stop when this answers the practical question. A useful explanation need not first become a formal record or an admitted structure.

Open the formal branch only when the team must qualify, persist, compare, publish, or rely more strongly on the structure. A `ConstraintGovernedUnfoldingStructure` (CGUS) is one A.22 `U.Structure` whose locally named loci, constituents, obtaining relations, and constraints define at least two potential continuations across the cases allowed by those constraints. A separate result says which alternatives are enabled, disabled, or unknown for one case and time window.

Do not use CGUS merely because a card, graph, table, narrative, prompt path, or README line looks route-shaped. A single recommendation or displayed sequence is not enough. The structure may branch, join, cycle through subject relations, remain partially ordered, or leave several alternatives live at once. A result with zero or one enabled alternative can still concern that same branching structure.

**What changes in practice.** Practitioners correct the visible alternatives and their conditions before completing formal fields. They keep potential structure separate from the result for the present case, and they stop at the first unresolved fact instead of inventing a continuation. Display order alone neither prescribes nor performs Work.

### A.22.CGUS:1 - Problem Frame

FPF often needs to explain how several identified things and relations constrain what may follow without turning that explanation into a workflow. The shared object is one A.22 structure. CGUS adds local loci and a membership test for potential branching; a continuation judgement then evaluates one case.

Descriptions, publication forms, evidence, assurance, authorization, work plans, performed Work, architecture claims, and mathematical models can be used alongside that structure. They remain separate objects and claims under the patterns that define or test them.

### A.22.CGUS:2 - Problem

A route-shaped explanation can hide the relations and constraints that make an alternative available. Readers then follow the displayed order as if it were a required procedure, or they treat a condition label as proof that the condition is true now.

The opposite repair is also harmful: authors replace the simple decision question with a large admission, replay, publication, and assurance package. The formal package becomes harder to use than the misleading card it was meant to correct.

### A.22.CGUS:3 - Forces

| Force | Tension |
| --- | --- |
| Useful explanation vs workflow overread | A visible path helps a reader, but actual Work may be nonlinear, interrupted, iterative, or arranged by another Method or plan. |
| Potential structure vs present result | The structure can retain several possible branches while the present case enables none, one, or several. |
| Plain entry vs formal replay | An ordinary correction should be cheap; qualification and replay still need enough identity and relation detail to be checked later. |
| Description vs described structure | A card, graph, table, or narrative can describe a structure without creating it. |
| Reuse vs copied mini-patterns | CGUS needs direct exits to relation, transformation-flow, work, publication, and assurance patterns without copying their architectures. |

### A.22.CGUS:4 - Solution

#### A.22.CGUS:4.1 - Ordinary branch

Write the smallest useful answer in domain language:

1. name the decision or question;
2. list the real alternatives;
3. state the condition for each alternative;
4. state the facts known for this case;
5. mark each alternative `available`, `blocked`, or `unknown`, and name the first missing fact or rule.

For example, a design review has two alternatives: accept the design or repair it. Acceptance needs both checks to pass. Repair needs at least one failed check and a repair proposal that concerns this design.

| Alternative | Present facts | Result shown on the card |
| --- | --- | --- |
| Accept the design | Thermal check failed; service check passed. | `blocked — both checks have not passed` |
| Repair the design | A check failed and a repair proposal exists, but the proposal-to-design relation has not been established. | `unknown — proposal target not established` |

That corrected card is already useful. It keeps both potential alternatives visible and refuses to invent the missing relation. Continue only if a named later use needs formal structure identity or replayable results.

#### A.22.CGUS:4.2 - Formal qualification branch

Use the four A.22 discriminators to identify one `U.Structure`:

- its constituent references;
- the obtaining relation occurrences it selects;
- the applied constraint claims;
- the named selection-use frame: the question or action and the overread it forbids.

CGUS membership adds locally declared loci and bindings that expose how those constituents matter to the unfolding question. The selected relations and constraints must define at least two potential continuation candidates across allowed cases. The current continuation result, a description, or a publication field adds no structure-identity discriminator.

```text
selectedCGUSRef: one A.22 U.Structure
A22IdentityBasis:
  selectedConstituentRefs[]
  selectedObtainingRelationOccurrenceRefs[]
  appliedConstraintClaimRefs[]
  namedSelectionUseFrame:
    questionOrAction
    forbiddenOverread
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

A CGUS locus belongs to this structure, not to a reusable relation declaration:

```text
CGUSLocusRef := <selectedCGUSRef, locusId>
CGUSLocusBinding := <selectedCGUSRef, locusId, locusMeaning, selectedConstituentRef>
```

The constituent must already belong to the A.22 identity basis. A locus binding neither changes that constituent's kind nor creates a relation. Do not use an A.6.5 `SlotSpec` as a free-standing structure position.

When replay must identify one participant in a relation occurrence, retain the direct relation definition, the occurrence, the participant order, and the participant binding:

```text
RelationParticipantLocator := <relationDefinitionRef, relationOccurrenceRef, participantOrder, participantRef, relationSignatureRef?, slotSpecRef?>
```

Add a `RelationSignature` and its declaration-local `SlotSpec` together only when an existing reusable declaration is itself needed for replay. Neither declaration value substitutes for the obtaining occurrence. The CGUS has no ambient context field.

Judge each continuation separately. An immediate local use may keep the following values in the explanation; persistence or replay may place them in an ordinary C.2.1 result episteme.
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
  stopOrNextAction
  recheckConditions[]
```

A claim reference identifies the claim being applied; it does not show that the test applies or that its condition is satisfied. An obtaining relation is not a condition claim. Keep these two basis branches distinct and derive the case result only from completed judgements.

The membership test concerns potential topology. Changed facts, evidence, test outcomes, or time windows normally change a judgement and the current set, not the structure. Reidentify the A.22 structure when a constituent, selected obtaining relation occurrence, applied constraint, or named use frame changes. Reapply CGUS membership when a locus binding or potential-continuation row changes.

#### A.22.CGUS:4.3 - Four separate decisions

Do not turn qualification, case evaluation, description adequacy, and downstream reliance into one score.

| Decision | Passing basis | Honest lower result |
| --- | --- | --- |
| A.22 identity and CGUS membership | The four A.22 discriminators identify one structure; its local loci, relations, and constraints define at least two potential continuations across allowed cases. | Name the missing discriminator, binding, relation, constraint, or candidate. Keep the artifact as an explanation. |
| Continuation result for this case | Each candidate has an applicable test or obtaining-relation basis, case inputs, facts, required polarity, time window, and an `enabled`, `disabled`, `unknown`, or `error` result. | Mark the affected candidate unknown or stop on the missing value. Do not revoke an independently established structure. |
| Description or demonstrative-slice adequacy | The description says what it shows and omits for its declared use. C.33 is used only when a carrier's loss affects that use. | Narrow or correct the description. Missing publication or loss material does not deny the structure. |
| A stronger neighboring claim | The method, Work, evidence, assurance, gate, architecture, publication, currentness, or mathematical claim passes its own definition or test. | Stop only that stronger use and name its missing rule or basis. |

Potential branches and joins remain part of the structure even when the present case enables one or none. A linear teaching slice neither removes the other topology nor fixes the order of performed Work.

#### A.22.CGUS:4.4 - Explanations, descriptions, and the non-workflow boundary

Before qualification, an ordinary explanation is about the domain question or proposed alternatives. If persistence is needed, its C.2.1 `EntityOfConcern` remains that question or proposed set, not a CGUS that has not yet qualified.

After qualification, a whole-structure description may describe loci, bindings, relations, constraints, potential branches, case results, and relevant omissions. A separate demonstrative slice may show one traversal for a declared teaching or comparison use. That slice is a C.2.1 episteme: its exact claim content, the qualified CGUS as `EntityOfConcern`, and its effective `U.ReferenceScheme` jointly recover its identity. `DemonstrativeUnfoldingSlice@Context` is readable lineage for this possibility, not a `U.Kind` or an exact slice by itself. The slice neither creates nor reidentifies the structure. Use C.33 only when hidden or lost structure in its carrier matters to the declared use.

Displayed words such as *move*, *next*, and *path* remain ordinary language unless a stronger claim requires another kind. A proposed action, a plan item, a `U.WorkPlan`, dated `U.Work`, and an actual `U.Transformation` are different values. Use `E.10.MOVE`, A.15, and A.3 only when that distinction changes the claim; a display performs and authorizes nothing.

For a transformation-flow use, apply `E.18.3`. It owns the choice among one TFS, one parent-relative `SubflowRef`, or an E.18.NET network and the corresponding position and demonstration locators. CGUS keeps only its local locus bindings and potential topology; it does not copy the network's members, positions, valuations, Work, transformations, or tags.

Cite another pattern only when its content supplies a needed definition, constraint, test, method, evidence rule, or assurance rule. For example, use C.32 for an architecture claim, E.23 for improvement, G.11 for source currentness, C.29 for a mathematical-lens claim, and A.10 or B.3 for evidence or assurance. The cited pattern is not an actor or a field of the CGUS.

If a durable name or a relation between local senses is the question, use F.17, F.18, or F.9 after the value has been recovered. Do not copy their naming or Bridge procedures into this pattern. Entry cards and publication faces remain under E.11 and E.17.

#### A.22.CGUS:4.5 - Replay and change localization

Replay structure identity from the four A.22 discriminators. Replay CGUS membership from the local locus bindings and potential topology. Replay the case result from each candidate's basis, inputs, facts, polarity, dependent occurrences, time window, outcome, and reason.

Localize change before reopening wider work. A changed constituent, selected occurrence, constraint, or use frame can reidentify the A.22 structure. A changed locus binding or potential-continuation row reopens CGUS membership. A changed fact, evidence item, test result, or time window normally reopens only the affected judgement and current set. A changed omission reopens the affected description use. A changed neighboring claim stays with the pattern that defines or tests it.

### A.22.CGUS:5 - Complete Worked Case

Return to the design review from `4.1`. The ordinary card becomes formal only because the team now needs to retain and compare the review basis across editions.

```text
selectedCGUSRef: DesignReviewAlternatives@DR-27
A22IdentityBasis:
  selectedConstituentRefs[]:
    DesignCandidate-A
    ThermalCheckResult-A
    ServiceCheckResult-A
    RepairProposal-A
    AcceptCandidate-Continuation
    RepairCandidate-Continuation
  selectedObtainingRelationOccurrenceRefs[]:
    ThermalCheckAboutCandidate@DR-27
    ServiceCheckAboutCandidate@DR-27
    RepairProposalTargetsCandidate@DR-27
  relationOccurrenceRecoveryRows[]:
    - relationOccurrenceRef: ThermalCheckAboutCandidate@DR-27
      predicateDefinitionRef: CheckResultAboutDesignCandidatePredicate
      participantRefsInPredicateOrder[]: [ThermalCheckResult-A, DesignCandidate-A]
    - relationOccurrenceRef: ServiceCheckAboutCandidate@DR-27
      predicateDefinitionRef: CheckResultAboutDesignCandidatePredicate
      participantRefsInPredicateOrder[]: [ServiceCheckResult-A, DesignCandidate-A]
    - relationOccurrenceRef: RepairProposalTargetsCandidate@DR-27
      predicateDefinitionRef: RepairProposalTargetsDesignCandidatePredicate
      participantRefsInPredicateOrder[]: [RepairProposal-A, DesignCandidate-A]
  appliedConstraintClaimRefs[]:
    AcceptIfBothChecksSatisfied
    RepairIfAnyCheckViolatedAndProposalTargetsCandidate
  namedSelectionUseFrame:
    questionOrAction: which review continuation is available now?
    forbiddenOverread: the display is not performed Work or authorization
constraintGovernedProfileBasis:
  locusBindingRows[]:
    - <DesignReviewAlternatives@DR-27, candidate, design under review, DesignCandidate-A>
    - <DesignReviewAlternatives@DR-27, thermal-result, thermal finding, ThermalCheckResult-A>
    - <DesignReviewAlternatives@DR-27, service-result, service finding, ServiceCheckResult-A>
    - <DesignReviewAlternatives@DR-27, repair-proposal, proposed repair, RepairProposal-A>
    - <DesignReviewAlternatives@DR-27, accept, accept continuation, AcceptCandidate-Continuation>
    - <DesignReviewAlternatives@DR-27, repair, repair continuation, RepairCandidate-Continuation>
  potentialContinuationRows[]:
    - AcceptCandidate-Continuation, constrained by AcceptIfBothChecksSatisfied
    - RepairCandidate-Continuation, constrained by RepairIfAnyCheckViolatedAndProposalTargetsCandidate
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
currentContinuationSet: enabled [RepairCandidate-Continuation]; disabled [AcceptCandidate-Continuation]; unknown []
stopOrNextAction: show repair as available; recheck when either result, the proposal relation, or the window changes
```

The structure has two potential continuations although this case enables only repair. The relation rows state their predicates and ordered participants; the judgement rows state the tests, applicability, inputs, facts, polarity, dependent occurrences, window, outcomes, and reasons.

If `RepairProposalTargetsCandidate@DR-27` or its participant binding is missing, the repair result becomes `unknown — proposal target not established`. If the structure's identity was established on another sufficient basis, only this case result is incomplete. If that occurrence belongs to the claimed identity basis, this structure claim also remains provisional.

If a later thermal check passes while the service check still passes, acceptance becomes enabled and repair becomes disabled. The constituents, selected occurrences, constraints, use frame, locus bindings, and potential topology have not changed, so the CGUS keeps its identity and membership.

### A.22.CGUS:6 - Bias-Annotation

| Bias risk | Mitigation |
| --- | --- |
| Workflow bias | Ask about alternatives and conditions; use work and method patterns only for actual work-order or way-of-doing claims. |
| Display bias | Treat cards, graphs, tables, narratives, and entry lines as explanations or descriptions, not as the structure. |
| Formality bias | Start with the ordinary decision answer and open formal qualification only for a named later use. |
| Consumer bias | Keep transformation-flow, architecture, improvement, currentness, evidence, and publication details in their direct patterns. |
| Lexical bias | Words such as *route*, *path*, *loop*, *workflow*, *graph*, or *sequence* establish no CGUS by themselves. |

### A.22.CGUS:7 - Conformance Checklist

| ID | Passing condition | Failed-check repair |
| --- | --- | --- |
| **CC-CGUS-1 Identity and profile.** | The four A.22 discriminators identify one `U.Structure`; local locus bindings, relations, and constraints define at least two potential continuations across allowed cases. | Recover the missing value or keep the artifact as an explanation. |
| **CC-CGUS-2 Local loci and relation participants.** | Every `CGUSLocusBinding` uses a locus declared inside this CGUS and binds one constituent for a stated meaning. A needed relation participant retains its definition, occurrence, order, and binding; `RelationSignature` and `SlotSpec` appear together only for declaration-level replay. | Restore the locus or complete relation-participant basis. Never use a free-standing `SlotSpec` as a structure position. |
| **CC-CGUS-3 Explanation and description separation.** | An ordinary or persisted provisional explanation concerns the domain question or proposed alternatives. Post-qualification descriptions and slices concern the CGUS. None is the structure or a membership condition. | Restore the right `EntityOfConcern` or keep the explanation ordinary. |
| **CC-CGUS-4 Current continuation result.** | Each judgement retains its test or obtaining-relation basis, applicability, inputs, facts, polarity, dependent occurrences, window, outcome, and reason. The enabled set may contain zero, one, or several alternatives. | Mark the affected candidate unknown or stop on the missing value. |
| **CC-CGUS-5 Separate decisions.** | Identity and membership, case result, description adequacy, and each neighboring claim are judged separately. | Reopen only the affected decision. |
| **CC-CGUS-6 Non-workflow boundary.** | The structure and display do not prescribe or perform Work by themselves. | Move a justified work-order claim to the Method or work-plan pattern. |
| **CC-CGUS-7 Graph-shaped coverage.** | Branches, joins, cycles, partial order, and live alternatives are preserved or explicitly omitted for the declared use. | Keep a chain provisional or state what its demonstrative slice omits. |

### A.22.CGUS:8 - Common Anti-Patterns And Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Pretty route as ontology** | A card or graph is treated as the structure. | Keep it as an explanation; qualify the structure independently. |
| **Condition label as result** | A label or claim reference is treated as proof that a continuation is enabled. | Apply the test or recover the obtaining relation and facts; otherwise return `unknown`. |
| **One enabled branch as one-branch structure** | The present result erases other potential continuations. | Keep potential topology and the case result separate. |
| **Formal package or field count first** | A simple correction requires replay fields, or authors add references merely to raise schema completion. | Use the ordinary branch and stop when it answers the question. In formal use, retain only fields consumed by qualification or replay and test whether readers recover the right alternatives and smallest repair. |
| **Displayed order as Work** | A teaching slice becomes a project procedure or authorization. | Use the applicable Method, work-plan, Work, or gate pattern only when that claim is actually made. |
| **Consumer architecture copied inward** | CGUS repeats transformation-flow locators, naming procedures, or catalogs of neighboring claims. | Keep the local structural rule and exit directly to the pattern that defines or tests the other claim. |

### A.22.CGUS:9 - Consequences

CGUS preserves the usefulness of a route-shaped explanation without making it a workflow. Ordinary use is cheap: decision, alternatives, conditions, facts, honest result, and stop. Formal use costs more because structure identity, CGUS membership, the case result, and any description or neighboring claim must remain separately checkable.

This separation prevents a changed fact from reidentifying a stable structure and prevents a missing publication, evidence, or assurance value from erasing a useful ordinary answer.

### A.22.CGUS:10 - Rationale

The recurring object is a thin specialization of A.22 `U.Structure`, not a new root kind. Constraint-based process modeling, object-centric querying, artifact-centric modeling, acausal modeling, and FPF pattern use all distinguish a constraint-bearing structure from a performed trace, work order, view, publication, solver run, or example path.

The same distinction appears in acausal engineering models: component relations and constraints can be stated before an analysis chooses a calculation direction. FPF adopts only that general separation. Mathematical models, analyses, executions, results, and publications keep their own kinds and rules.

### A.22.CGUS:11 - SoTA-Echoing

| Source or practice anchor | FPF adoption | Boundary |
| --- | --- | --- |
| Esser and Fahland, “OCPQ: Object-Centric Process Querying & Constraints”, 2025 | Current research comparator for typed objects, joins, many-to-many dependencies, and relation-preserving constraint queries. | A query or result is not the CGUS. |
| JuliaHub, Dyad 3.2 component and analysis documentation, 2026 | Current engineering comparator for reusable relation-first components separated from analyses and their solution objects. | FPF imports neither Dyad ontology nor its tools. Modelica 3.7 is retained only as historical acausal-modeling lineage. |
| Declare/MP-Declare, DCR, artifact-centric/GSM, and CMMN work | Lineage for declarative constraints, live alternatives, stages, guards, and weakly structured case work. | These are not current authority for a universal FPF process calculus; their notation and workflow ontology are not imported. |
| FPF pattern-language practice | Ordinary explanations may precede qualification; descriptions and demonstrative slices may follow it. | An entry card, example, or publication is neither admission evidence nor the specification. |

As of 2026-08-04, OCPQ and Dyad are the current comparators used here. Modelica, Declare, DCR, artifact-centric/GSM, and CMMN remain lineage where their distinctions are useful. Reopen this choice when a newer object-centric constraint method or relation-first engineering language changes the treatment of objects, relations, analyses, or live alternatives.

### A.22.CGUS:12 - Relations

Specializes: one A.22 `U.Structure` whose local locus bindings, obtaining relations, and constraints define at least two potential continuations across allowed cases. Continuation judgements, descriptions, slices, loss notes, and neighboring claims are separate results or uses.

Specialized by: `E.18.3` when the same structure also satisfies its transformation-flow condition. Local applications include architecture, abduction, improvement, narrative, grounding, currentness, and first-entry uses only when their own constituents, relations, constraints, and use frames are recoverable.

Coordinates with: `A.6.P` and A.6.5 for relation occurrence and reusable declaration precision; `E.18`, `E.18.NET`, and `E.18.3` for transformation-flow substrates; `A.3` and `A.15` for Method, plan, Work, and Transformation claims; `A.10`, `B.3`, `A.20`, and `A.21` for evidence, assurance, constraint decisions, and gates; `C.30` and C.32 for architecture; `E.23` for improvement; `G.11` for currentness; `C.29` for mathematical-lens use; `C.33` for material description loss; `E.11` and `E.17` for entry and publication; and `F.17`, `F.18`, and `F.9` for source-local sense, durable naming, and Bridge claims.

Does not replace any pattern that supplies the definition, constraint, test, method, evidence rule, or assurance rule for a neighboring claim.

### A.22.CGUS:End

