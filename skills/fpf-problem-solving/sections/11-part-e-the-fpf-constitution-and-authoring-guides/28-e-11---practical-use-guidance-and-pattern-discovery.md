## E.11 - Practical-Use Guidance and Pattern Discovery

> **Type:** Pattern-language governance pattern (E)
> **Status:** Stable
> **Normativity:** Normative for public FPF practical-use guidance, bounded card comparison, and reliance-conditioned comparison records.

### E.11:1 - Problem frame

#### E.11:1.1 - Use this when

Use `E.11` when an FPF author or maintainer publishes or refreshes the public practical-use cards that help a practitioner, manager, or assisting agent find which direct pattern to inspect first.

The practitioner, manager, or assisting agent is the reader of that publication, not the performer of E.11's publication method. Their first move is to compare the current README cards by working situation and first result or blocker, then open the direct pattern from the card that best fits the work.

Public guidance answers three questions quickly: "Is this my situation? What useful result could I obtain first? Which direct pattern should I open?" A public example remains a template; it is not a project instance, applicability finding, recommendation, plan, decision, or work occurrence.

**Primary EntityOfConcern.** One context-free public practical-use guidance episteme and its expansion, published through an E.17-conforming public card unit.

**Conditional support object.** A `PracticalUseCardShortlist@Context` is current only when a named receiving use relies on addressable comparison history. It records that bounded comparison; it is not a second public guidance form or the primary `EntityOfConcern`.

**What this buys.** A cold reader can move from an ordinary project question to one or a few inspectable direct patterns. A wrong first choice remains recoverable, while ordinary comparison stays conversational.

**Not this pattern when.** After one direct pattern has been selected, use `E.11.PUA` to follow its conditional `Solution`: identify the first independently governed result and the direct basis for calling it this use's result, or stop when that basis is missing. Use `E.11.PUR` when local applicability, recommendation, coordination, or ordering among candidate pattern uses is current. Use the direct subject pattern for the actual result, plan, work, evidence, decision, or publication claim.

### E.11:2 - Problem

Pattern libraries are difficult to enter from a working situation. A reader may see a long table of contents, search by a familiar word, or choose the first appealing pattern title. That choice can be premature because nearby cards may lead to different first results and different stop conditions.

Attempts to help can create a second problem. Public guidance becomes a numbered method, a shadow pattern body, or a form that asks the reader to fabricate project-local values before the direct pattern has been inspected. The discovery aid then competes with the patterns it should expose.

### E.11:3 - Forces

| Force | Pressure on the solution |
| --- | --- |
| Recognition | Public wording starts from situations engineers recognize, not internal pattern topology. |
| Exactness | Every candidate names the admitted kind of a potential result, the local identification question, its direct owner and identity-or-obtaining basis template, the kind of governed object relative to which the result phrase would be true, and one category-correct relative-basis template. |
| No fictitious context | Public guidance has no reader-project identity and cannot contain `@Context` instances. |
| Bounded search | Several cards can remain plausible, so comparison needs stop and return conditions rather than one perfect first guess. |
| Light ordinary use | Card comparison should normally remain in conversation. |
| Durable reliance | A named later review, replay, audit, or automation use can rely on addressable comparison history. |
| Didactic continuity | Every card needs a readable walkthrough, not only a list of PatternIDs. |
| One source of guidance | README carries the public card set; Preface, ToC, retrieval, and pattern bodies answer different questions. |

### E.11:4 - Solution

An FPF author or maintainer publishes or refreshes sixteen semantic practical-use cards. Each card starts from a recognizable situation and question, states a readable first result or exact public blocker, points to direct candidate-use templates, and links to an expansion with boundaries and one walkthrough.

A practitioner, manager, or assisting agent uses the already published set: compare the cards that fit the working situation, inspect their different first results or blockers, and open the direct pattern from the card that best fits the work. Ordinary card use does not make that reader a framework publisher.

The keys identify situations; they do not order them. A user may compare any finite set that remains plausible.

#### E.11:4.1 - Public card and expansion

```text
PracticalUseGuidance@FPFReadme <: U.Episteme:
  practicalUseKey: PracticalUseKeyValue
  publicSituationDescriptionRef: U.Episteme
  publicPracticalQuestionRef: PublicPracticalUseQuestion@FPFReadme
  publicObstacleDescriptionRef?: PublicPatternUseObstacleDescription@FPFReadme
  publicFirstResultSummaryRef: U.Episteme
  cardExpansionRef: PracticalUseCardExpansion@FPFReadme

PracticalUseCardExpansion@FPFReadme <: U.Episteme:
  guidanceRef: PracticalUseGuidance@FPFReadme
  candidateUseTemplateRefs[1..*]: PublicCandidatePatternUseTemplate@FPFReadme
  publicStopBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicReturnBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicWrongTurnRecoveryBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicStrongerNeighborBoundaryRefs[]: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicCoarseningRows[]: PublicResultCoarseningRow@FPFReadme
  demonstrativeSliceRef?: DemonstrativeUnfoldingSlice@Context
  ordinaryWalkthroughRef?: PublicOrdinaryWalkthrough@FPFReadme

PracticalUseCardPublicationUnit@FPFReadme:
  conformsTo: E.17.AUD
  publishes: PracticalUseGuidance@FPFReadme
  linksTo: PracticalUseCardExpansion@FPFReadme
```

Exactly one walkthrough ref is present. Use `demonstrativeSliceRef` when the example passes A.22.CGUS admission in its own declared illustrative bounded context. It does not fill a reader-project position. Otherwise use an ordinary walkthrough with an explicit reason why the example is not a CGUS slice.

#### E.11:4.1.1 - Cold-reader recognition and grounded public value

Test every public card and expansion against a first-time engineer, engineer-manager, or assisting agent who has not studied FPF. The heading and first sentence name a recognizable working situation before PatternIDs, FPF kind names, or internal quality, projection, and conformance vocabulary. They then name a first useful result or exact blocker that the reader can imagine identifying, grounding, or requesting in the project—for example, identifying a current plan, grounding a claim about a pre-existing pump, or requesting an evaluation—without implying that the public template performs any of those acts. The expansion names the admitted kind of the potential result, the local identification question, direct owner and identity-or-obtaining basis, the kind of method, plan, dated Work, transformation, evaluation, decision, or receiving-use object relative to which the phrase would be true, the category-correct relative basis, the minimum usable result, and any actually current conditional receiver. It introduces no project instance.

A public benefit claim is grounded only when the card makes recoverable a concrete project need, one admitted kind of potential first result or exact blocker, the local identification and category-correct basis questions, one specific direct-pattern distinction that changes the next project action, and the direct pattern whose `Solution` governs the result kind. Otherwise the claim is marketing copy, even if it sounds plausible. These values may remain readable prose; this rule does not require the reader to fill a card or project record before opening the direct pattern.

Keep the public set representative of FPF's practical range. Wording and description repair remain visible, but they do not dominate architecture, problem shaping, work, comparison, evidence, timing, causal use, mathematical modeling, quality, improvement, and framework authoring.

#### E.11:4.2 - Public helper epistemes

```text
PublicPracticalUseQuestion@FPFReadme <: U.Episteme:
  situationRef: U.Episteme
  questionDescriptionRef: U.Episteme
  likelyDirectResultDescriptionRef?: U.Episteme

PublicPatternUseObstacleDescription@FPFReadme <: U.Episteme:
  situationRef: U.Episteme
  obstacleDescriptionRef: U.Episteme
  obstacleEffectOnUseRef: U.Episteme

PublicPatternUseResultTemplate@FPFReadme <: U.Episteme:
  readableResultDescriptionRef: U.Episteme
  exactResultKindRef: U.Kind
  resultIdentificationQuestionRef: U.Episteme
  resultDirectOwnerPatternRef: U.MethodDescription
  resultIdentityOrObtainingBasisTemplateRef: U.Episteme
  resultRelativeGovernedObjectKindRef: U.Kind
  resultRelativeDirectBasisKind: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  resultRelativeDirectBasisTemplateRef: U.Episteme
  minimumUsableResultDescriptionRef: U.Episteme
  conditionalReceivingPatternRef?: U.MethodDescription

PublicPatternUseBoundaryConditionTemplate@FPFReadme <: U.Episteme:
  boundaryConditionKind: recognizableCondition | stop | return | wrongTurnRecovery | strongerNeighbor | missingGovernor | missingInformation
  conditionDescriptionRef: U.Episteme
  governingPatternRef: U.MethodDescription
  conditionalReceivingPatternRef?: U.MethodDescription
  conditionalReceivingPatternPositionDescriptionRef?: U.Episteme

PublicResultCoarseningRow@FPFReadme:
  readableResultPhraseRef: U.Episteme
  exactResultKindRef: U.Kind
  resultIdentificationQuestionRef: U.Episteme
  resultDirectOwnerPatternRef: U.MethodDescription
  resultIdentityOrObtainingBasisTemplateRef: U.Episteme
  resultRelativeGovernedObjectKindRef: U.Kind
  resultRelativeDirectBasisKind: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  resultRelativeDirectBasisTemplateRef: U.Episteme
```

A public template asserts no project result and contains no project value. It names the admitted kind of a potential later result, the local question by which a practitioner would identify such an entity or occurrence, its direct owner, and what would make that candidate entity exist or that relation occurrence obtain. It separately names the kind of exact method, plan, dated Work, transformation, evaluation, decision, or separately governed receiving-use object relative to which a real PUA closure would call it a result.

The result-relative basis template has exactly one category. A direct-relation template asks for predicate, participants, applicability, obtaining, occurrence identity, and direct governor. An A.6.1 template asks for operation, application, argument or result binding, and direct governor. An A.6.RCD local-claim template asks for one C.2.1 claim episteme with polarity, substrate or constructor, base predicates and their direct owners, participants, case facts, and any support or warrant required by the later receiving use. The claim does not obtain, and A.6.RCD does not replace the base owners. Result identity or currentness and result-relative basis are different public questions; they coincide only when the potential result is the same direct relation occurrence used to close the later application.

`conditionalReceivingPatternRef` is present only when the public branch itself promises a continuation or names a downstream reliance. A result template without such a continuation leaves it absent. A public `stop`, `missingGovernor`, or `missingInformation` boundary has no receiver. `return`, `wrongTurnRecovery`, and `strongerNeighbor` name a receiver only when that route is part of the branch. The optional obstacle names a recognizable obstacle only when one matters. Practical use may begin from an object to inspect, a result to evaluate, or an existing method to improve without first inventing a problem.

#### E.11:4.3 - Candidate-use templates and basis completeness

```text
PublicCandidatePatternUseTemplate@FPFReadme <: U.Episteme:
  templateKey: PublicCandidateUseTemplateKeyValue
  recognizableConditionRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  directPatternRef: U.MethodDescription
  directSolutionSectionRef: PatternSolutionSectionRef
  expectedResultTemplateRef?: PublicPatternUseResultTemplate@FPFReadme
  resultPromiseBlockerRef?: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  candidateBasisCompletenessConditionRefs[1..*]: CandidatePatternUseBasisCompletenessCondition@FPFReadme

CandidatePatternUseBasisCompletenessCondition@FPFReadme <: U.Episteme:
  candidateBasisPosition: entityOfConcernKind | practicalQuestion | optionalProblemCard | resultIdentificationQuestion | resultRelativeGovernedObjectKind | candidateSpecificBasis
  admittedBasisValueKindRef: U.Kind
  completenessConditionDescriptionRef: U.Episteme
```

`PatternSolutionSectionRef` is an edition-pinned reference to the cited pattern's `Solution`. A broad result family or pattern title is insufficient.

Exactly one of `expectedResultTemplateRef` and `resultPromiseBlockerRef` is present. The result-promise branch is admissible only when the exact potential-result kind, its identification question, direct owner, identity-or-obtaining basis template, result-relative governed-object kind, category-correct relative-basis template, minimum usable result, and any actually current conditional receiver are all stateable. The blocker branch uses `missingGovernor` or `missingInformation`, states the exact absent governor or information, and carries no fulfilled result template. Optional omissions cannot masquerade as a weak passing promise.

The completeness condition inherits C.2.1 constitution. Its EntityOfConcern is the reusable candidate-basis position declared by the template; its ClaimGraph states the admitted filler kind and positive completeness condition; its ReferenceScheme explains how later current project fillers satisfy that position. It contains no project value and orders nobody to fill a form.

#### E.11:4.4 - Ordinary walkthrough

```text
PublicOrdinaryWalkthrough@FPFReadme <: U.Episteme:
  guidanceRef: PracticalUseGuidance@FPFReadme
  situationDescriptionRef: U.Episteme
  firstResultTemplateRef?: PublicPatternUseResultTemplate@FPFReadme
  resultPromiseBlockerRef?: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  walkthroughRowRefs[2..*]: PublicOrdinaryWalkthroughRow@FPFReadme
  fullPatternTransitionBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  cgusNonAdmissionRationaleRef: U.Episteme

PublicOrdinaryWalkthroughRow@FPFReadme <: U.Episteme:
  actionOrProposedUseDescriptionRef: U.Episteme
  expectedResultTemplateRef?: PublicPatternUseResultTemplate@FPFReadme
  resultPromiseBlockerRef?: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  directPatternRef: U.MethodDescription
  directSolutionSectionRef: PatternSolutionSectionRef
  continuationConditionRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
```

The walkthrough and each row carry exactly one result template or exact public blocker. An ordinary walkthrough is still an explanation, not a project method, work order, or recommendation. It may contain a local pattern mantra: a short repeatable formulation that keeps that pattern's Solution in attention. It may be presented as a CGUS-demonstrative mantra only when A.22.CGUS admits the represented conditional continuations as a `DemonstrativeUnfoldingSlice@Context`.

#### E.11:4.4.1 - Practical-use carry-through check

Check every published card over its public values. This check asks whether the card can lead a reader to one direct pattern and either a truthful context-free result promise or an exact public missing-governor or missing-information blocker. It creates no project instance, applicability verdict, result entity, relation occurrence, or receiving use.

```text
PracticalUseCarryThroughCheck:
  practicalUseKey: PracticalUseKeyValue
  practicalUseGuidanceRef: PracticalUseGuidance@FPFReadme
  publicSituationDescriptionRef: U.Episteme
  publicPracticalQuestionRef: PublicPracticalUseQuestion@FPFReadme
  publicObstacleDescriptionRef?: PublicPatternUseObstacleDescription@FPFReadme
  candidateUseTemplateRefs[]: PublicCandidatePatternUseTemplate@FPFReadme
  publicStopBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicReturnBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicWrongTurnRecoveryBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicStrongerNeighborBoundaryRefs[]: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicCoarseningRows[]: PublicResultCoarseningRow@FPFReadme
  demonstrativeSliceRef?: DemonstrativeUnfoldingSlice@Context
  ordinaryWalkthroughRef?: PublicOrdinaryWalkthrough@FPFReadme
  walkthroughSelectionRationaleRef: U.Episteme
  principalBlockedOverreadRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
```

Exactly one walkthrough reference is present. A demonstrative slice passes A.22.CGUS admission and identifies the included positions, C.33 structure-loss notes, alternatives or returns, direct patterns, and transition to the full pattern. An ordinary walkthrough carries its CGUS non-admission rationale. A local mantra inside it remains a compact reminder of the direct pattern's Solution; it does not acquire the Tech kind `DemonstrativeUnfoldingSlice@Context` merely because it is memorable or repeated.

Each candidate-use template passes one of two disjoint branches. A result-promise branch names one direct pattern and Solution, the admitted kind of a potential result, the local identification question, direct owner and identity-or-obtaining basis, full governed relative-object kind, category-correct relative-basis template, minimum usable result, every candidate-basis completeness condition, and a conditional receiver only when one is actually current. A blocker branch names the exact missing governor or missing information and carries no expected-result template. Reject omitted values presented as a weak promise, a public project instance, a broad family in place of the result kind, a generic result relation, or a PatternID list without selection conditions. The principal blocked overread states the most consequential false project claim that a reader could otherwise infer from the card.

#### E.11:4.5 - Sixteen stable practical-use keys


| Key | Public situation heading |
| --- | --- |
| `ARCHITECTURE` | Shape an architecture from a problem and competing characteristics |
| `WORKING-DOCUMENTS` | Create a working document that another participant can use |
| `OPTION-COMPARISON` | Compare options without hiding trade-offs |
| `PROBLEM-SHAPING` | Turn a vague concern into an accepted problem-side record |
| `IMPROVEMENT` | Improve a named object under an explicit evaluation |
| `COSTLY-ACTION` | Prepare a costly or hard-to-reverse action |
| `TIME` | Make a time-dependent claim usable |
| `CAUSAL-USE` | Decide what a causal claim may support |
| `DESCRIPTION-USE` | Use a description or view without confusing it with its subject |
| `NAMING` | Name a governed value so people can recover its meaning |
| `WORDING` | Repair wording that hides the object, relation, or claim kind |
| `MATHEMATICAL-MODELING` | Choose and bound a mathematical lens |
| `SOTA-PORTFOLIO` | Build a current state-of-the-art synthesis pack |
| `DPF-AUTHORING` | Build a domain or local FPF-grounded framework |
| `SYSTEM-RECOGNITION` | Decide whether the exact entity in the claim is a system |
| `SYSTEM-DELIMITATION` | Decide which entities are parts of the system and which relations only cross its boundary |

E.11 records one F.13-form historical read path: `splits(SYSTEM-IN-CONTEXT -> {SYSTEM-RECOGNITION, SYSTEM-DELIMITATION, WORDING, ARCHITECTURE})`. The unchanged F.13 body does not contain this row. The old card had no single surviving public-guidance identity: system recognition, system delimitation, lexical recovery, and architecture have different referents, relations or evaluations, receiving uses, first results, and direct governors. Older writing remains readable through this one read path; current card use names only the four successor keys. A.1.STM is a conditional continuation with a dedicated readable README guide, not a fifth successor key. The split creates no U-kind, relation kind, record kind, result kind, or generic `Context` claim.

README owns the current public cards and their expansions. Preface explains why FPF's distinctions work together. ToC locates pattern families. Full patterns carry methods, conditions, costs, consequences, and exact result semantics. None is a second card store.

#### E.11:4.6 - Bounded comparison

When more than one card remains plausible, compare four things: recognizable-situation fit, difference among first results or exact public blockers, direct pattern, and stop or return condition. Keep the comparison in conversation for ordinary bounded use. Open the most promising direct pattern before constructing a project candidate.

The comparison rationale has one public guidance subject and exists before a project candidate is constructed. When materialized, it follows full C.2.1 identity:

```text
PracticalUseCardComparisonRationale@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one PracticalUseGuidance@FPFReadme
  claimGraph: U.ClaimGraph by value
  effectiveReferenceSchemeRef: U.ReferenceSchemeRef
  editionId
  recognitionReasonDescriptionRef: U.Episteme
  firstResultDifferenceDescriptionRef: U.Episteme
  comparisonRationaleDescriptionRef: U.Episteme
```

Stop inspection when one card has enough recognition and first-result advantage to justify direct pattern inspection, when no remaining card can change the starting choice, or when the inspection budget opens an explicit return. No fixed maximum of three is inferred.

Materialize comparison history only when a named receiving use relies on it:

```text
PracticalUseCardShortlist@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact PracticalUseQuestion@Context being compared
  claimGraph: U.ClaimGraph by value
  effectiveReferenceSchemeRef: U.ReferenceSchemeRef
  editionId
  claimScopeRef?: U.EntityRef, referencing one U.ClaimScope
  modelUseStructureRef?: U.EntityRef, referencing one BoundedModelUseStructure
  namedRelianceConditionRef: U.Episteme
  receivingUseDescriptionRef: U.Episteme
  receivingUseGoverningPatternRef: U.MethodDescription
  comparisonRefs[1..*]: PracticalUseCardComparison@Context
  selectedStartingGuidanceRef?: PracticalUseGuidance@FPFReadme
  inspectionStopBoundaryRef: PatternUseBoundaryCondition@Context
  returnBoundaryRef: PatternUseBoundaryCondition@Context

PracticalUseCardComparison@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one PracticalUseGuidance@FPFReadme
  claimGraph: U.ClaimGraph by value
  effectiveReferenceSchemeRef: U.ReferenceSchemeRef
  editionId
  shortlistRef: PracticalUseCardShortlist@Context
  recognizableSituationFitRationaleRef: PracticalUseCardComparisonRationale@Context
  firstResultTemplateRefs[]: PublicPatternUseResultTemplate@FPFReadme
  resultPromiseBlockerRefs[]: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  firstResultDifferenceRationaleRef: PracticalUseCardComparisonRationale@Context
  inspectionDisposition: keep | defer | discard | startHere
```

Guidance, practical question, compared result templates or blockers, first-result differences, named reliance, stop, and return remain ClaimGraph content or separately governed references; none replaces the C.2.1 identity. Each comparison cites at least one result template or exact blocker from the guidance it evaluates. `claimScopeRef` or `modelUseStructureRef` is present only when its exact direct relation changes the named reliance. Several plausible cards alone do not make this record current. The named reliance may be a later review, replay, audit, automation, or another use that needs addressable comparison history. Retain only the rows that use needs.

#### E.11:4.7 - Replay and currentness

Replay one public guidance claim from the current card and expansion, the edition-pinned direct `Solution`, and its exact branch. For a result promise, recover the potential-result kind, identification question, direct owner and identity-or-obtaining basis, governed relative-object kind, category-correct relative-basis template, minimum usable result, readable coarsening row, boundary, any conditional receiver, and selected walkthrough. For a blocker, recover the exact missing governor or information and confirm that no fulfilled result template was published. The guidance remains current only while the card's recognizable situation and practical question still point to that same use.

Recheck the smallest affected card slice when its recognizable situation, practical question, or resulting recognition condition changes; when the direct `Solution`, potential-result kind, identification question, direct owner, identity-or-obtaining basis, governed relative-object kind, relative-basis category, first-result difference, promise blocker, receiver, or boundary changes; or when use evidence shows a recurrent wrong turn. `G.11` governs edition, telemetry, currentness-window, and decay orchestration; E.11 supplies the card-specific values and change conditions that orchestration inspects.

### E.11:5 - Archetypal Grounding

#### E.11:5.1 - Architecture or description?

A team says, "Our diagram no longer explains the system." `ARCHITECTURE` and `DESCRIPTION-USE` both look plausible. The first card offers an architecture question and selected-structure result; the second offers a description-use or representation-transition result.

The team compares the first-result difference, opens `C.30` and `E.17.0`, and discovers that the selected structure is unsettled. It starts with `ARCHITECTURE`. No shortlist record is needed because the comparison is local and reversible.

#### E.11:5.2 - A later safety review needs comparison history

The receiving safety review relies on an addressable rationale for why two teams considered `TIME`, `COSTLY-ACTION`, `CAUSAL-USE`, and `SYSTEM-DELIMITATION` before a hazardous test, because it will replay the selection after new measurements arrive. The fourth card remains plausible while exact parthood, the direct choice or architecture-decision result that makes one inclusion/exclusion claim current for the test object, or a crossing participation relation is unsettled.

In a separate systemhood fixture, “Could this stateful session or natural body be a system for this decision?” selects `SYSTEM-RECOGNITION`, because the exact entity and the A.1 evaluation can change what the decision may rely on. It does not select delimitation merely because an environment is mentioned.

That named reliance admits a `PracticalUseCardShortlist@Context` with four comparison rows, the stop boundary, and the return condition. The shortlist does not authorize the test or replace evidence, assurance, gate, choice, or WorkPlan relations.

#### E.11:5.3 - A card leads to a physical result without promising it

`WORKING-DOCUMENTS` can lead to a usable machining work instruction. Its public template first names the admitted `U.MethodDescription` or `U.WorkPlan` kind and asks how a later project use would identify the episteme under A.3.2 or A.15.2. It then asks separately which exact relation occurrence, A.6.1 binding, or category-correct local claim would make that episteme the result relative to the later document-use or machining-planning object. Any conditional receiving pattern appears only when that continuation is part of the branch. The card does not promise a machined component.

The reader can therefore imagine useful progress without inferring that publication or planning performed the machining. When actual machining or other dated work later becomes current, use A.15.1 to identify the exact performed Work occurrence; use A.15 as well only when role–method–work alignment is itself current. The instruction or plan is neither that dated `U.Work` nor proof that it occurred.

#### E.11:5.4 - Repair the smallest card slice after a direct result changes

Suppose a new `A.6.3.RT` edition makes one exact `RepresentationSchemeTransitionRelation@Context` kind the potential first-result kind for one `DESCRIPTION-USE` condition. Repair that candidate-use template so it names the relation kind, its source and target participant kinds, A.6.3.RT predicate and obtaining test, occurrence-identification question, the governed-object kind relative to which a later PUA use would call it a result, its readable coarsening row, and any boundary whose condition changed. Recheck the linked walkthrough against that context-free basis template; only PUA later names a project occurrence.

The public card heading and question remain unchanged when readers still recognize the same situation. Preface and ToC remain unchanged when framework rationale and retrieval location did not move. The `A.6.3.RT` pattern body remains the authority for the relation; E.11 repairs only the public guidance that points to it.

#### E.11:5.5 - A better first-click rate can make discovery worse

Suppose retrieval ranks the most familiar title first and the first-click rate rises. Follow-up comparison shows that more readers now open `DESCRIPTION-USE` when the selected structure is still unsettled, so first-result mismatch and wrong-turn returns also rise.

The visible navigation measure improved while the intended value worsened: readers reached a less suitable direct pattern more often. Keep first-click rate as telemetry, apply `E.13` to the substitution, and judge the guidance by recoverable situation fit, first-result fit, and wrong-turn cost rather than by the click measure alone.

### E.11:6 - Bias-Annotation

- **Title-match bias.** A familiar word selects a pattern before its Problem and first result are inspected. Compare situations and result differences, then open the direct pattern.
- **Public-instance bias.** A README example is filled with project values. Keep public templates context-free; project candidates belong to `E.11.PUA`.
- **Numbered-route bias.** Card order is read as method order. Use semantic keys and condition-specific continuations.
- **Record-first bias.** Comparison emits a shortlist by default. Materialize one only for a named receiving reliance.
- **Card-as-authority bias.** A public card is treated as applicability verdict, recommendation, decision, or authorization. Return to `E.11.PUR` or the direct subject pattern.

### E.11:7 - Conformance Checklist

| ID | Check | Passing condition |
| --- | --- | --- |
| `E11-1` | Situation first | Card wording begins with a recognizable working situation before PatternIDs or internal topology. |
| `E11-2` | Exact first result | Every promise branch names the admitted potential-result kind, identification question, direct owner and identity-or-obtaining basis, full governed relative-object kind, category-correct relative-basis template, and only an actually current conditional receiver. Every blocker branch names exact missing governance or information and carries no result template. |
| `E11-3` | No fictitious context | Public card, expansion, templates, and walkthrough contain no reader-project `@Context` values. |
| `E11-4` | Complete public explanation | The carry-through check names exactly one admitted demonstrative slice or justified ordinary walkthrough, its selection rationale, and the principal blocked overread. |
| `E11-5` | Template completeness | Exactly one result promise or public blocker is present. A promise carries the direct Solution and every required result-template position; a blocker carries `missingGovernor` or `missingInformation`. Optional omissions, project occurrences, generic result relations, and fabricated receivers do not pass. |
| `E11-6` | Bounded comparison | Comparison exposes first-result differences and a stop or return condition. |
| `E11-7` | Conditional shortlist | Every materialized shortlist names the receiving reliance that uses its history. |
| `E11-8` | Publication responsibility and reader separation | An FPF author or maintainer publishes or refreshes the README cards; a practitioner, manager, or assisting agent compares the published cards and opens a direct pattern. Preface, ToC, retrieval, and full patterns do not maintain duplicate card bodies. |
| `E11-9` | Cold-reader recognition | A reader unfamiliar with FPF encounters the working situation and imaginable first result or blocker before internal vocabulary, while the expansion preserves the potential-result kind, identification question, direct owner, governed relative-object kind, category-correct basis, minimum usable result, and boundary. |
| `E11-10` | Grounded public value | Every benefit claim exposes the concrete need, potential first-result kind or exact blocker, local identification and basis questions, specific direct-pattern distinction that changes the next project action, and direct pattern; the public set does not present FPF mainly as wording or description policing. |

### E.11:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Why it fails | Repair |
| --- | --- | --- |
| Pattern list as guidance | IDs do not show recognition conditions, potential-result differences, local identification questions, category-correct basis templates, or exact blockers. | Publish situation, result promise or blocker, direct Solution, and boundaries. |
| Internal vocabulary as the front door | The card starts with PatternIDs, FPF kinds, or quality and conformance terms before the reader can recognize the work. | Put the ordinary working situation and first useful result first, then restore precision in the expansion and direct pattern. |
| Ungrounded public value | The card promises broad help but shows no concrete potential-result kind or blocker, identification question, basis template, or direct-pattern distinction that changes the next project action. | Name the need, result kind or exact blocker, local identification and basis questions, the distinction that changes the next action, and the direct pattern. |
| Card as a form | Readers fabricate project facts before inspecting the pattern. | Keep the card context-free and defer local records to PUA under reliance. |
| Fixed three-card shortlist | Interface convenience becomes ontology. | Use any finite inspected set bounded by the current question and stop condition. |
| Walkthrough as workflow | Presentation order becomes a fixed work sequence. | State continuation conditions and use CGUS only when its structure is actually admitted. |
| README as pattern body | Public copy accumulates methods and conformance doctrine. | Link to the expansion and direct pattern; keep method authority there. |

### E.11:9 - Consequences

**Benefits.** FPF gains human-readable public practical-use guidance without losing the potential-result kind, direct owner, two distinct basis questions, or subject-pattern authority. Readers can explore and recover from wrong turns. Ordinary use stays light, while a named later review or replay can preserve comparisons.

**Costs.** Public guidance remains trustworthy only while the sixteen cards and their expansions stay synchronized with the direct patterns. Every readable result phrase needs a context-free potential-result kind, identification question, direct owner and identity-or-obtaining basis, governed relative-object kind, category-correct relative basis, and boundary behind it. Honest blocker branches add exact missing-governor or missing-information distinctions. When a named later review, replay, audit, or automation must rely on a comparison, the team must materialize addressable comparison records and maintain their stop and return conditions.

### E.11:10 - Rationale

Discovery is a bounded decision under limited attention, not a one-time lookup. A semantic card makes the practical question and first-result difference visible before the reader commits to a pattern. A recoverable return is more useful than pretending the first cue is always right.

Public guidance remains trustworthy only when it is weaker than the direct pattern. It helps a reader decide what to inspect; it does not decide applicability, authorize Work, identify a project result, or make a relation obtain. This division also keeps public explanation teachable: simple phrases can remain visible because expansions restore the admitted potential-result kind, local identification question, direct owner, governed relative-object kind, category-correct basis template, minimum usable result, and exact blocker when the promise cannot be made.

### E.11:11 - SoTA-Echoing

| Source or practice line | Problem-solving move taken here | Adoption and boundary |
| --- | --- | --- |
| Information-foraging and information-scent practice | Put recognizable situation and expected information gain before internal navigation structure. | Adopt through situation-first cards and first-result differences. Do not infer ontology or a fixed shortlist size. |
| Jin, Bai, and Oulasvirta, *Modeling Trial-and-Error Navigation With a Sequential Decision Model of Information Scent*, arXiv:2603.11759 (2026) | Treat inspection, premature selection, wrong turns, and backtracking as a bounded sequence under memory and time constraints. | Adapt through explicit stop, wrong-turn, and return boundaries. Materialize history only for named reliance; the preprint does not establish a universal discovery record. |
| Zhu, Reinecke, and Mitra, *Language Scent: Exploring Cross-Language Information Navigation*, arXiv:2604.03604 (2026) | Keep contextual cues near the governed value while preserving the exact target behind a reader-facing expression. | Adapt to public cue and expansion design. The small study does not establish universal label equivalence or decide FPF ontology. |
| Current FPF E.8, E.17, F.17, F.18, and E.11.PUA | Separate public recognition, publication, naming, and project pattern use. | Adopt as the governing patterns for their stated relations. E.11 defines only the public guidance and reliance-conditioned comparison layer. |

The practitioner implication is concrete: inspect a small plausible set, compare the potential-result kind or exact blocker each direct pattern can truthfully expose and the local identification and basis questions each requires, then keep durable history only when someone will use it later.

Information-foraging is the lineage anchor, not by itself the current competitive claim. Familiar-title lookup and popularity ranking are the common comparator: they are cheap cues, but E.11 rejects either as the sole selection basis because neither exposes first-result differences or a recoverable return.

The two 2026 studies are current preprint anchors rather than settled consensus. Reopen the bounded-navigation adaptation when peer review, replication, or use evidence changes the observed role of inspection, memory, backtracking, or wrong-turn cost. Reopen the language-scent adaptation when broader studies show that in-situ cues obscure the governed target more often than they help readers recover it. `G.11` orchestrates those currentness and telemetry checks; E.11 changes the affected card cues, comparison, or boundaries.

### E.11:12 - Relations

- **Builds on:** `E.8` for pattern recognition text, `E.17.AUD` for publication-unit discipline, `F.17` and `F.18` for published terms and naming, and `C.2.1` for public helper epistemes.
- **Leads to:** `E.11.PUA` for applying one selected pattern and `E.11.PUR` for local applicability, recommendation, and coordination.
- **Coordinates with:** `A.22.CGUS` for demonstrative slices, `E.18` for flow-local results, `G.11` for currentness orchestration, and each direct pattern cited by a public template.

### E.11:End

