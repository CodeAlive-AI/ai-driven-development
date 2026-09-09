## C.22.PFR - Problematic-For Relation

> **Type:** Conceptual (C)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain name.** Actual problem.

### C.22.PFR:1 - Problem frame

**Use this when.** Use this pattern when an actual condition may be adverse for one exact entity and use, and a receiving claim needs to distinguish the actual Problem from a signal, criterion description, evaluation, assessment claim, ProblemCard, or claim that no suitable method is currently known.

**First useful move.** Name the actual-condition relation. Then name the exact predicate, entity, scope, and interval for which that predicate applies. If the condition falls on the adverse side of that applicable predicate, say plainly: "This condition is a problem for this entity in this scope." Expose a PFR occurrence only when another claim needs that Problem identity.

**What goes wrong if missed.** A card or evaluation result is allowed to create a Problem; the same criterion is applied to the wrong entity or scope; a new description edition creates a false new Problem; or one continuously adverse episode is split every time evidence is sampled. Conversely, two adverse episodes separated by actual non-adverse behavior collapse into one occurrence.

**What this buys.** Actual Problems can exist before discovery, can be referenced while still ongoing, and can be distinguished across repeated adverse episodes. One exact applicability relation supplies the predicate, problem-for entity, claim scope, and declared criterion-applicability window used by PFR; its actual occurrence extent is separately derived from uninterrupted obtaining. Measurements, evaluations, evidence, claims, cards, and method search remain available without becoming Problem identity.

**Early battery stop.** A low terminal-voltage reading can be a useful signal and can justify a `ProblemCard`, but it is not itself the actual-condition participant. Until a direct voltage-state pattern supplies the exact relation kind, participant meanings, obtaining rule, temporal extent, recurrence, and occurrence identity, the battery case remains explicitly non-conforming: the reading, alarm, report, assertion, and card establish none of that world-side relation. Once such a governor exists, the applicability relation can connect its selected voltage predicate to the exact vehicle, intended-start `U.ClaimScope`, and declared criterion-applicability window; discovering a method still changes solvability rather than PFR actuality.

**Not this pattern when.** Use `C.22.2` when the current object is a problem-side card, signal, hypothesis, forecast, scenario, anticipated-condition claim, or reviewable formulation rather than an actual PFR. Use `C.27` when a rate, rhythm, recovery, or regime claim is being used to change action, `C.28` when causal support is at issue, or the exact direct forecast, scenario, counterfactual, or anticipated-condition governor when that claim is current. Use the selected A.19 comparison, `G.4` acceptance, state, gate, or measurement pattern when the current question is how to evaluate or support the adverse predicate. Use `E.18.1`, `E.23`, and the direct NQD or OEE patterns for repeated problematization, search, work, evaluation, and continuation.

### C.22.PFR:2 - Problem

An actual Problem is neither a record nor a free-standing quality label. It depends on an actual condition and on a criterion that applies to one exact entity, scope, and interval. The relation obtains when the condition is on the adverse side of that applicable predicate.

FPF needs one identity for this dependent evaluative relation without copying values defined by `ProblemCriterionApplicabilityRelation` into additional writable PFR slots. It also needs to distinguish continuous adverse episodes from repeated episodes while refusing to infer a recovery from missing observations or evidence.

### C.22.PFR:3 - Forces

| Force | Tension |
|---|---|
| Actuality vs discoverability | A Problem can obtain before anyone evaluates, notices, describes, or publishes it. |
| Readable problem talk vs typed dependence | Practitioners need a direct sentence, while load-bearing use needs exact condition and applicability occurrences. |
| One applicability relation vs duplicated participants | Predicate, problem-for entity, claim scope, and declared criterion-applicability window are useful independently of PFR but must not be writable both as applicability-relation participants and as PFR participants; the applicability occurrence extent remains derived. |
| Continuous identity vs repeated episodes | One adverse episode may receive many assessments; the same participants may also stand in later adverse episodes after a real recovery. |
| Open episode use vs final interval | Current work needs to reference a Problem before the adverse episode has ended. |
| Predicate truth vs epistemic support | Evaluation and evidence support claims about adverse truth but do not make the world-side dependent relation obtain. |
| Solvability vs Problem actuality | Finding a method changes what can be done, not whether the current condition remains adverse. |
| Anticipated-condition claim vs actual occurrence | A useful forecast, scenario, or hazard card can describe a possible condition before any actual-condition relation obtains. |

### C.22.PFR:4 - Solution

Model an actual Problem as one obtaining `ProblematicForRelation`, a dependent evaluative `U.Relation` between exactly two relation occurrences: the actual condition and the applicability of a characteristic-space predicate.

#### C.22.PFR:4.1 - Use one exact criterion-applicability relation

`CharacteristicSpacePredicate` is a by-value predicate used by an A.19 comparison, acceptance, state, gate, or other direct consumer. It is not a new U-kind, publication record, description edition, or comparison result. Its meaning is recoverable from the declared characteristic-space coordinates, scales, normalization or bridge values, operator, cut or band, polarity, and the selected direct consumer's governed comparator, admissibility, and predicate-use semantics. A separately performed evaluation remains `U.Work`; its result episteme and evidential-support relations remain separately governed, and none of these constitutes predicate meaning.

Before testing adversity, answer three plain questions: **what exact point or value does this condition supply, how is that point obtained, and why is it the input for this problem-for entity and use?** The by-value predicate therefore carries one `ConditionToPredicateInputRule` as part of its own semantics, not as another PFR participant:

- **Direct input:** the actual-condition participant is already a governed characteristic-assignment or state relation whose subject pattern exposes the exact characteristic-space coordinate, scale, and value used by the predicate.
- **Projected input:** when that relation does not itself expose the needed point, the rule cites one exact governed projection or bridge, its source relation kind and participant positions, target characteristic space, coordinate and scale, and the direct relation or predicate connecting that input to the problem-for entity and receiving use.

A relation reference alone is not a coordinate. If neither path yields the exact point and the problem-for link, adverse truth and PFR remain unestablished. When two projections are plausible, the rule names the selected one; identify the nearest inadmissible alternative only when one fails the declared input or problem-for-link conditions. `ConditionToPredicateInputRule` is a pattern-local by-value rule inside `CharacteristicSpacePredicate`; it is not a U-kind, relation occurrence, evaluation result, or copied PFR field.

**Public name settlement.** The following F.18 NameCard names the applicability relation kind.

```text
NameCard:
  NameCardId: NC-PROBLEM-CRITERION-APPLICABILITY-RELATION
  GovernedValueRef: ProblemCriterionApplicabilityRelation under C.22.PFR
  SubjectPatternLocator: C.22.PFR
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: obtaining relation saying that one characteristic-space predicate currently governs one exact problem-for entity and claim scope under one declared criterion-applicability window, independently of whether an actual condition presently satisfies the adverse predicate; repeated occurrences with the same four participants are distinguished by maximal continuous actual applicability
  TechLabel: ProblemCriterionApplicabilityRelation
  PlainLabel: problem-criterion applicability
  CandidateSet: ProblemCriterionApplicabilityRelation; CriterionApplicabilityRelation; ProblemCriterionUseRelation; ApplicableProblemCriterion
  RejectedCandidates: CriterionApplicabilityRelation overclaims a universal criterion ontology; ProblemCriterionUseRelation hides obtaining applicability behind use wording; ApplicableProblemCriterion turns a relation into an adjective-headed value
  SelectionRationale: preserve distinct applicability occurrences for different exact entities, scopes, or declared windows and after actual loss and restoration of applicability, without making a predicate-description edition identity-bearing
  PublicRowStatus: pending
  LineageEntries: replaces description-edition and generic criterion-use identity proposals
  RefreshCondition: reopen if the four fixed participants plus maximal continuous actual applicability cannot distinguish applicability occurrences, or if the direct rule no longer separates criterion governance from adverse-condition satisfaction
```

Use one individuable dependent `U.Relation` for applicability:

```text
ProblemCriterionApplicabilityRelation:
  ProblemCriterionPredicateSlot: CharacteristicSpacePredicate, byValue
  ProblemForEntitySlot: U.Entity, byRef with an exact local ValueKind
  PredicateClaimScopeSlot: U.ClaimScope, byValue
  DeclaredCriterionApplicabilityWindowSlot: DeclaredCriterionApplicabilityWindow, byValue; use an explicit unbounded value when no finite bound is intended
```

This relation states that one exact predicate currently governs one exact entity and claim scope under one declared criterion-applicability window. Its direct applicability predicate is satisfied while that criterion remains selected and governing for that entity, scope, and window; it does not ask whether any actual condition is presently on the adverse side. The applicability occurrence can therefore continue across adverse, non-adverse, and later adverse condition intervals. It ceases when the criterion is withdrawn or replaced for that use, the entity or claim scope changes, the declared window no longer covers the use, or another direct applicability condition fails. One occurrence is identified by the four fixed participants plus the maximal continuous period of actual applicability. Changing a participant yields another occurrence; actual loss and later restoration of applicability yields distinct occurrences even when all four participants stay fixed. A coextensional description edition or carrier change does not change either the predicate participant or the occurrence. Assessment windows, evidence-relevance intervals, description editions, claim-currentness windows, and adverse-truth intervals remain with their own claims and relations.

A semantic predicate change selects a different predicate participant; it is not an edition-only repair. If the new predicate replaces the old predicate for the same use and the old applicability therefore ceases, the old applicability occurrence ends and a new occurrence begins only if the new predicate actually applies. The PFR dependent on the old occurrence can then end, and another PFR can begin under the new occurrence when adverse truth obtains. If both predicates remain applicable, two applicability occurrences may coexist; a new criterion description alone does not prove replacement or cessation.

#### C.22.PFR:4.2 - Keep the PFR signature reduced to two participants

**Public name settlement.** The following F.18 NameCard names the actual dependent evaluative relation kind.

```text
NameCard:
  NameCardId: NC-PROBLEMATIC-FOR-RELATION
  GovernedValueRef: ProblematicForRelation under C.22.PFR
  SubjectPatternLocator: C.22.PFR
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: actual dependent evaluative relation with one actual-condition relation occurrence and one problem-criterion-applicability relation occurrence as its only non-derived participants, individuated by those participants plus the actual inception of each maximal continuous adverse episode
  TechLabel: ProblematicForRelation
  PlainLabel: actual problem
  CandidateSet: ProblematicForRelation; AdverseCriterionAssessmentRelation; ProblemUseRelation; ProblemRelation; ProblemSituationRelation
  RejectedCandidates: AdverseCriterionAssessmentRelation omits the problem-for relation; ProblemUseRelation hides the actual adverse condition; ProblemRelation hides criterion applicability; ProblemSituationRelation falsely requires situation
  SelectionRationale: make ordinary Problem recoverable without copying applicability participants and distinguish repeated adverse episodes without requiring a universal adverse-evaluation relation occurrence
  PublicRowStatus: pending
  LineageEntries: situation-first, card-as-world, bearer-duplicating, and description-edition identity proposals retired
  RefreshCondition: reopen if participant references plus actual adverse inception cannot keep one stable occurrence reference through closure or distinguish later adverse episodes, or if the predicate's condition-to-input rule no longer yields one unambiguous characteristic point and problem-for link
```

**No-mint disposition for root `U.Problem`.** Do not introduce a second problem entity beside the obtaining `ProblematicForRelation` occurrence. That occurrence is the actual Problem; a `ProblemCard`, criterion description, assessment claim, or local Plain label may describe or designate it but does not supply another world-side identity.

The complete non-derived participant set is:

```text
ProblematicForRelation:
  ActualConditionRelationSlot: U.Relation, byRef
  ProblemCriterionApplicabilityRelationSlot: U.Relation, byRef
```

The first reference resolves to the exact obtaining relation that constitutes the actual condition under its direct pattern. The second resolves to the exact obtaining applicability relation from C.22.PFR:4.1.

PFR has no separately writable condition-bearer, predicate, problem-for-entity, claim-scope, applicability-window, assessment-window, or description-edition slot. The actual-condition relation fixes its condition participants, and the applicability relation fixes the predicate, problem-for entity, claim scope, and declared applicability window. Assessment windows and description editions remain with their own claims. A readable claim projects the applicability values from that participant:

```text
PFR.problemCriterionPredicate
  := PFR.problemCriterionApplicabilityRelation.problemCriterionPredicate
PFR.problemForEntity
  := PFR.problemCriterionApplicabilityRelation.problemForEntity
PFR.predicateClaimScope
  := PFR.problemCriterionApplicabilityRelation.predicateClaimScope
PFR.declaredCriterionApplicabilityWindow
  := PFR.problemCriterionApplicabilityRelation.declaredCriterionApplicabilityWindow
PFR.problemCriterionApplicabilityExtent
  := maximal continuous obtaining extent of PFR.problemCriterionApplicabilityRelation
```

This is a derivation from one participant, not a consistency check between copies.

#### C.22.PFR:4.3 - Use predicate truth as the obtaining condition

`ProblematicForRelation` obtains exactly when all three conditions hold:

1. The exact `ActualConditionRelation` obtains under its direct pattern.
2. The exact `ProblemCriterionApplicabilityRelation` obtains because its criterion remains governing for the exact entity and claim scope under the declared criterion-applicability window, independently of whether the actual condition is adverse.
3. For the actual-condition participant, the predicate's exact `ConditionToPredicateInputRule` must yield the declared characteristic-space point or value and the direct link to the problem-for entity and use; that point falls on the adverse side under the selected scale, comparator, cut or band, polarity, and admissibility semantics.

The selected direct consumer supplies the governed input projection or consumes the direct characteristic assignment, then governs the comparator and admissibility semantics. An evaluation may calculate or support a claim that the resulting point is adverse. Comparison outcomes, acceptance outcomes, state or gate results, measurements, evidence, and assessment claims are not automatically PFR participants, and producing them does not make PFR obtain.

A Problem can therefore obtain unnoticed. Later detection can involve work, evidence, and claims about the already obtaining relation; it does not create retroactive actuality.

When evaluation is actually performed, recover every exact actual performer `U.System` through A.13, independently admit the dated evaluation `U.Work` under A.15.1, and name the `U.Method` actually followed. Name any declared A.6.1 operation application separately when its returned-value binding is claimed. Add F.6 only when the evaluation account or a receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; missing or failed F.6 leaves the evaluation Work intact. A short PFR explanation may omit an assignment identifier that no later claim uses. That Work may return the separate evaluation result `true`, `false`, or `unknown` defined by the selected evaluation pattern; a C.2.1 assertion may state the result. A.10 governs evidence use for reliance on that assertion, B.3 governs any named assurance claim, and G.11 may qualify the assertion's current edition. The practitioner may rely on the assertion for the receiving Work, decline or defer that reliance, or reopen its basis. `unknown` is an evaluation result, never a world-side PFR value; test PFR obtaining through the three conditions in §4.3.


#### C.22.PFR:4.4 - Identify repeated adverse episodes from world-side continuity

The direct occurrence rule is ontic. With the two participant occurrences fixed, one PFR occurrence is the maximal continuous episode during which both participants obtain and the selected condition point is actually on the adverse side. Actual cessation of either participant or actual movement to the non-adverse side ends that occurrence. Later renewed adverse truth starts a later PFR occurrence. Measurement, evaluation, demonstration, assessment, and evidence availability neither start nor end either occurrence.

Use this world-side identity basis:

```text
<actualConditionRelationRef,
 problemCriterionApplicabilityRelationRef,
 adverseEpisodeStart>
```

`adverseEpisodeStart` is the episode's actual inception under the declared temporal reference, not the first observation or report time. When admitted time grain cannot distinguish co-inceptions, or when a receiving history must keep one reference while a claim about inception remains revisable, explicitly individuate the occurrence under A.6.REL and assign a stable `pfrOccurrenceId` that designates it. The resolution record may carry the current boundary claim, but neither its asserted start nor its asserted end becomes a mutable identifier field. The PFR's `actualAdverseExtent` is derived from the world-side episode: its end becomes fixed when the episode actually ceases, and a later claim may recover or correct that boundary. The recovered end and completed extent describe the occurrence; they do not replace it or change its assigned reference. This applies A.6.REL's participant-plus-episode rule without making a currently known boundary constitutive.

Participant references alone remain insufficient because the same participants can enter adverse, non-adverse, and later adverse episodes. A universal evaluation reference is also insufficient because an unnoticed PFR can obtain and several assessments can support one occurrence.

#### C.22.PFR:4.5 - Keep world-side occurrence and current boundary claim separate

Use `[adverseEpisodeStart, open]` only in a current claim whose evidence supports that this same PFR occurrence still obtains at the claim's stated reference time. `open` is a claim-side endpoint sentinel, not the clock time, an identity field, or a substitute for missing evidence. The stable occurrence reference remains unchanged when a later claim records the recovered actual end.

A current assertion or description distinguishes three cases in ordinary words:

- **supported current:** the evidence supports continuous adverse obtaining from the episode's actual inception through the stated reference time; publish `[adverseEpisodeStart, open]`;
- **supported closed:** the evidence supports actual cessation at an exact boundary; publish `[adverseEpisodeStart, adverseEpisodeEnd]` for the same occurrence reference;
- **continuity unresolved:** the available evidence does not decide whether an unobserved cessation or restart occurred; retain the recoverable earlier occurrence reference and the supported segments, but assert neither one continuous occurrence nor two occurrences across the gap.

Later evidence may revise the assertion, including its claimed start, end, or continuity, without creating or changing the world-side episode. If it supports an earlier actual cessation, complete the extent of the earlier occurrence at that boundary. If it also supports later renewed adverse truth, identify the later occurrence from its own actual inception. Until that distinction is supported, do not attach the later adverse segment to either the old or a new occurrence by default.

Use the A-B-C regression while holding one continuously obtaining applicability occurrence fixed. The criterion remains governing for the same entity, scope, and declared window through A, B, and C; only world-side adverse truth changes:

- During A, the condition is actually adverse, so the first PFR obtains from `A.start` until its actual cessation at `A.end`.
- During B, the condition is actually non-adverse, so the first PFR does not obtain.
- During C, the condition is actually adverse again, so a later PFR begins at `C.start` with the same two participant references and a different stable occurrence reference.

Evidence that supports A, B, and C warrants the corresponding two-occurrence assertion. A missing assessment, unavailable measurement, stale evidence item, or support gap warrants `continuity unresolved`; it neither proves recovery nor licenses continuity. Adjacent or overlapping assessment windows likewise do not split or join world-side episodes by themselves.

#### C.22.PFR:4.6 - Keep assertions, reliance, anticipated conditions, solvability, and cards separate

An assertion about the exact PFR obtaining predicate has affirmative or negative claim polarity. An affirmative assertion may designate an independently established occurrence; a negative assertion denies predicate satisfaction for the named participants and qualification but does not erase or reidentify an earlier occurrence. A.10 governs the evidence-use account for treating that assertion as supported, refuted, or unresolved in one receiving use; B.3 applies only when a named assurance claim is current. Assertion polarity, support, and reliance therefore answer different questions.

A possible or anticipated problem remains an exact forecast, scenario, counterfactual, or anticipated-condition claim in `ProblemCard` or another episteme until an actual-condition relation, an applicability relation, and adverse predicate truth all obtain. `C.2.1` governs its assertion identity and polarity. Use `C.27` when a rate, rhythm, recovery, or regime claim is being used to change action and `C.28` when causal support is at issue. The exact direct claim pattern defines or constrains assumptions, horizon, and non-actual semantics. None of those claim-side facts establishes a current PFR.

A `ProblemCard` is one C.2.1 episteme with one exact ClaimGraph, one independently identified `EntityOfConcern`, and one effective `U.ReferenceScheme`. It may carry claims designating several PFR occurrences only when those claims are jointly about that one EntityOfConcern under the direct pattern that identifies it. When two PFR references lack such a joint concern, split the ClaimGraph and card. Conversely, several cards may designate the same PFR through different ClaimGraphs, schemes, viewpoints, or receiving uses. Card count, merge or split, currentness, assessment window, publication, carrier, and edition change neither PFR actuality nor identity. C.22.2:20.1b replays all three branches with exact objects: two Robot-7 PFR episodes share one A.1-identified `Robot-7` and one card; Robot-7 and Robot-8 PFRs have no direct joint EntityOfConcern and force two ClaimGraphs and cards; and two differently qualified cards retain the unchanged `PFR-InspectionAssignment-17` reference.

A claim that no supported method is currently available concerns the admitted method set, evidence, constraints, and intended use. Selecting or discovering a method changes current solvability; it does not end PFR while the actual condition remains adverse. Performed repair work can end PFR only when an independently recovered actual change makes a participant cease or moves the selected condition point to the non-adverse side.

Repeated problematization, method search, work, evaluation, and continuation occur in work and transformation flows governed by `E.18.1` and `E.23`. A claim or plan may carry a reference to the same PFR while work and transformation occurrences participate in a selected transformation-flow structure. Neither that reference use nor any flow-structure relation enters PFR identity. A later PFR is a later occurrence because a participant changes or because actual adverse truth begins again after actual cessation, not because another card, assessment, or flow visit exists.

#### C.22.PFR:4.7 - Preserve the lightweight path

For a first use, name only what decides the case:

1. the exact obtaining condition and the value or point it supplies;
2. the criterion that makes that point adverse, including the selected input path and cut or band;
3. the entity for which it is a Problem, the use or claim scope, and the applicability window.

Then write one ordinary sentence:

> `<condition and value>` misses `<criterion>` for `<entity and use>` during `<applicability window>`; therefore it is an actual Problem for that entity and use.

Stop there when the next work only needs to recognize the Problem. Cite the direct condition and criterion patterns, but do not fill a PFR record, repeat either relation signature, or assign a PFR identifier. The NameCards and signatures above define reusable semantics; they are not a mandatory user form.

Add explicit identity only when another claim must compare, qualify, change, nest, plan from, or refer back to this particular Problem occurrence. That receiving claim then names the exact actual-condition occurrence, exact applicability occurrence, actual adverse inception or stable PFR identifier when needed, claimed extent, and any evidence or assessment claim on which its reliance depends. The evidence remains separate from the world-side Problem.

### C.22.PFR:5 - Archetypal Grounding

**Executable first use — an assignment that violates a release criterion.** `InspectionReleaseAssignment` is a declared `U.SystemRoleAssignment` species defined under A.2.1. It defines the holder and assigned-kind participant meanings, assignment predicate, applicability, and occurrence identity. Occurrence `InspectionAssignment-17` has admitted System `Robot-7` as holder and local kind `InspectorSystemRole` as assigned-kind value. It obtains without interruption during `[2026-07-13T09:00, 2026-07-13T17:00]`. `MaintenanceRoles-2026`, `Maintenance-Scheme-A`, and the interval description may interpret or describe the assertion; they are not extra world-side participants. A roster row and `InspectionAssignmentAssertion-17` may describe the assignment and interval; neither makes the relation obtain.

A.2.1 identifies `InspectionAssignment-17` through the complete real participant set and the maximal uninterrupted period in which the direct species predicate obtains. Demonstrated non-assignment after the stated 17:00 boundary ends it. If the same participant set again satisfies the predicate on the next day after that actual gap, `InspectionAssignment-18` is a later occurrence; an evidence gap by itself neither ends nor splits the first occurrence. The subject pattern therefore supplies the participant meanings, obtaining rule, temporal extent, recurrence, and same-versus-new-occurrence rule required of `ActualConditionRelationSlot`.

The by-value predicate `NoInspectorSystemRoleBeforeValidation-v2` uses one direct `ConditionToPredicateInputRule`: from `InspectionAssignment-17` it reads the assigned-kind participant as coordinate `assignedSystemRoleKind = InspectorSystemRole` on a nominal system-role-kind scale and the holder participant as the direct link to problem-for entity `Robot-7`. Its adverse region is the declared set of system-role kinds prohibited for that System's autonomous-inspection release before validation, which contains `InspectorSystemRole`. The same kind assigned to another System is the nearest inadmissible input because its holder participant does not link the condition to `Robot-7`; a roster row is inadmissible because it is not the obtaining assignment occurrence.

`Robot7ReleaseCriterionApplicability-4` is the separate applicability occurrence. Its four participants are that predicate, `Robot-7`, `autonomous inspection release before validation` as the exact `U.ClaimScope`, and declared window `[2026-07-13T08:30, 2026-07-15T18:00]`. Because both participant relations obtain and the selected point is adverse, `PFR-InspectionAssignment-17` obtains on `[2026-07-13T09:00, 2026-07-13T17:00]`. The ordinary first-use sentence is:

> Robot-7 is assigned as inspector through `InspectionAssignment-17`, while `InspectorSystemRole` is prohibited for this System's autonomous-inspection release before validation during the declared 13–15 July window. This assignment is an actual Problem for Robot-7's release during its 13 July 09:00–17:00 assignment episode.

**Evaluation and reliance remain separate.** Admitted `SafetyReviewSystem-2 : U.System` performs dated `InspectionReleaseCheckWork-21` under independently obtaining `SafetyReviewAssignment-9 : SafetyReviewWorkAssignment <: U.SystemRoleAssignment`; F.6 uses the assignment's holder projection, and the Work enacts `InspectionReleaseCheckMethod-3`. The operation application returns `true` for the adverse predicate. `InspectionReleaseCheckAssertion-21` states that result; its evidence path and assurance tuple can warrant one release decision, G.11 can qualify the assertion edition, and the release decision-maker can rely on the assertion or decline that reliance. None is a third PFR participant. A `ProblemCard` may later designate `PFR-InspectionAssignment-17`; creating, revising, splitting, or publishing that card changes neither PFR participant nor actuality. If evaluation never occurs, the PFR still obtains. If the assertion is stale, the basis for that reliance may become unresolved, but the world-side relation is not thereby created, ended, or split.

**Actuality and recurrence.** Selecting another staffing Method and writing a Work order do not end the PFR. Only actual cessation of the A.2.1 assignment predicate at the stated 17:00 boundary ends it. When the same direct species predicate resumes on the next day as `InspectionAssignment-18` while the applicability occurrence still obtains, A.2.1 identifies that later system-role-assignment occurrence and its later adverse inception grounds `PFR-InspectionAssignment-18`. An evidence gap alone establishes neither continuous assignment nor withdrawal and reassignment.

**Blocked stress fixture — installed component.** `Fuse-R17 : U.System` and `Panel-7 : U.System` may be named in a parts claim, but current A.14 supplies no installed-part relation kind, installed-part participant meanings, obtaining predicate, temporal extent, recurrence, or same-versus-new-occurrence rule. Under A.6.REL:5.2, `ComponentOf-FuseR17-Panel7` is therefore not minted as an individuated installed-part occurrence here. A parts list, inspection note, removal report, or reinstallation wording cannot fill `ActualConditionRelationSlot`; the fuse case remains non-conforming until an accepted direct installed-part pattern supplies the complete settlement.

**Blocked stress fixture — battery voltage.** Current A.18 and C.16 can govern the voltage characteristic, scale, measurement work, result, uncertainty, and assertion. They do not supply a direct voltage-state relation with participant meanings, obtaining, temporal extent, recurrence, and occurrence identity. Therefore `TerminalVoltageState-12` is not minted here, and the low-voltage case remains non-conforming until an A.6.RCD decision selects or assigns that direct governor. `MeterReport-88`, an alarm, or a maintenance card may support a claim but cannot fill `ActualConditionRelationSlot` or backdate PFR.

**Blocked stress fixture — proof gap.** Current proof and assurance patterns define or constrain proof epistemes, obligations, evidence, and relying decisions, but this case lacks direct patterns supplying both (a) an individuable unresolved-consequence relation with its obtaining and episode law and (b) the exact proof-use or acceptance object and applicability relation needed by the case. Keep the condition gate and problem-for/applicability gate separate. `UnresolvedConsequence-17`, `ProofUseEntity`, and an omnibus proof-gap object are not admitted by this wording; the case remains non-conforming until both direct governors close.

**Blocked stress fixture — clinical condition.** A diagnosis, assessment, measurement report, and patient label are epistemes or context-dependent cues, not the clinical-condition occurrence or patient identity. This case lacks a clinical-condition pattern supplying the needed participants, obtaining, recurrence, identity, and temporal extent. Until one does, keep the case non-conforming. If *patient* also names a work-facing classification, recover the classified System and local system-role kind. If an assignment is claimed, recover its holder System, assigned kind, occurrence, and declared `U.SystemRoleAssignment` species; none supplies the missing clinical-condition relation.

**Blocked stress fixture — missed transfer.** First distinguish transfer Work, a world-side transfer or delivery relation, a commitment or acceptance relation, and a package or record episteme. E.18's structural `U.Transfer` cannot be reused merely by the phrase *hand-off failure*. This case lacks a direct pattern supplying the exact missed-transfer condition relation, and the phrase *receiving work* does not decide whether the problem-for entity is intended `U.WorkPlan`, dated `U.Work`, or another governed entity. The case therefore remains non-conforming until separate direct governors settle both questions.

**Blocked stress fixture — one hot surface, two uses.** This case lacks a direct pattern supplying an individuated hot-surface condition relation; a temperature reading cannot substitute for it. If such a governor later exists, hold its one occurrence fixed and use two distinct applicability occurrences when an exact receiving `U.Work` and an exact `U.System` have different problem-for fillers, scopes, declared windows, or applicability continuity. Adverse truth would then yield two PFR occurrences sharing only the condition reference. Until the condition gate closes, this remains a multiplicity test, not an asserted example.

**Repair branch replay.** Keep four outcomes distinct: a repair method is selected; repair work is planned; dated repair work occurs without a demonstrated condition change; or dated repair work is connected through its direct change/result governors to actual cessation or non-adversity of the condition. Only the fourth outcome can end PFR while applicability continues. A work record, result claim, acceptance verdict, or method label is insufficient.

### C.22.PFR:6 - Bias-Annotation

This pattern has an actuality bias: Plain **problem** names an obtaining dependent relation. The anticipated-condition guard preserves forecasts, scenarios, counterfactuals, hazards, and problem formulations as useful epistemes under their exact claim governors without backdating actuality.

It has a predicate-centered bias because adverse truth is load-bearing. The applicability relation prevents a criterion from becoming globally adverse by label; exact entity, scope, and interval stay explicit.

It also has a continuous-time bias for occurrence identity. Discrete-state and event-based domains can supply equivalent actual episode boundaries under their temporal reference. Evidence gaps leave the continuity assertion unresolved in either representation; they do not decide the world-side boundary.

### C.22.PFR:7 - Conformance Checklist

1. The actual condition is an explicitly individuated obtaining `U.Relation` under its direct pattern.
2. `CharacteristicSpacePredicate` is given by value and includes one exact `ConditionToPredicateInputRule`: either a direct governed characteristic assignment/state relation or a named governed projection/bridge to the exact coordinate, scale, and problem-for link. A criterion-description identifier, arbitrary relation reference, or plausible alternative projection is insufficient.
3. `ProblemCriterionApplicabilityRelation` has the predicate, exact problem-for entity, claim scope, and declared criterion-applicability window as its four participants. It obtains while that criterion governs those participants, independently of adverse-condition satisfaction; its occurrence extent is the maximal continuous period of actual applicability.
4. PFR has exactly two non-derived participant slots: actual condition and criterion applicability.
5. Predicate, entity, scope, declared criterion-applicability window, and actual applicability-occurrence extent are projected from applicability rather than copied into PFR.
6. The selected direct consumer obtains the exact point through the declared direct assignment or projection and governs comparator, cuts or bands, polarity, admissibility, evaluation, and support; the condition relation is never treated as a coordinate by itself.
7. Evaluation work, outcomes, measurements, evidence, assessment claims, descriptions, and cards do not create or identify PFR by default.
8. Repeated PFR occurrences use the two participant references plus actual adverse inception. Add a stable occurrence identifier only for co-inceptions or a receiving history that must survive revision of the claimed inception boundary; the currently asserted start, derived end, and completed extent are not mutable key fields.
9. `[adverseEpisodeStart, open]` is used only by a claim that supports current continuous obtaining; a later supported end completes the claimed extent on the same stable occurrence reference.
10. Actual non-adverse B between actual adverse A and C yields two world-side PFR occurrences. Evidence can support, refute, or leave that boundary unresolved; a gap alone proves neither one occurrence nor two.
11. Method availability and solvability claims remain separate from PFR actuality and identity.
12. Possible conditions remain exact forecast, scenario, counterfactual, or anticipated-condition claims under their direct governors until both participant relations and adverse predicate truth obtain; assertion polarity and reliance posture do not substitute for those obtaining conditions.
13. Ordinary readable use can stop before explicit PFR materialization when no receiving claim needs Problem identity.
14. Battery-voltage, proof-gap, clinical-condition, missed-transfer, and hot-surface cases remain explicitly non-conforming until their named direct condition and, where applicable, problem-for/applicability governors exist; a phrase, measurement, diagnosis, record, card, or structural transfer does not mint them.

### C.22.PFR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
|---|---|---|
| Card-created Problem | Creating or accepting a ProblemCard is treated as Problem actuality. | Test actual-condition obtaining, applicability obtaining, and adverse predicate truth; keep the card as an episteme about zero or more occurrences. |
| Duplicated applicability | Predicate, entity, scope, or interval is writable in both applicability and PFR. | Keep those values only in `ProblemCriterionApplicabilityRelation` and derive PFR projections. |
| Applicability conditioned on adversity | Criterion applicability is ended whenever the actual condition becomes non-adverse, so PFR tests the same predicate twice and cannot replay A-B-C with one applicability occurrence. | Let applicability state which criterion governs the entity and scope under the declared window; test adverse-condition satisfaction only in PFR §4.3. |
| Relation-as-coordinate | An arbitrary condition relation is said to be adverse without naming the characteristic point, projection, or link to the problem-for entity. | Use the predicate's exact direct-input or governed-projection rule; reject the nearest plausible projection that does not meet that rule. |
| Assessment-constituted PFR | Evaluation work or an assessment result becomes a universal PFR participant or is treated as starting or ending the world-side episode. | Let evaluation and evidence support a boundary claim; keep PFR participants, actual inception, and actual cessation world-side. |
| Evidence-window splitting | Each measurement or assessment window creates a new Problem occurrence. | Use actual adverse inception and cessation for occurrence identity; keep support windows with the claims they warrant. |
| Unknown-as-recovery or continuity | Missing evidence is treated as proof of recovery or as permission to bridge the gap. | Record `continuity unresolved`; later evidence may revise the boundary assertion but does not create the world-side episode. |
| Open-interval churn | Every observation changes the identity key, or `open` is used for an unsupported evidence gap. | Keep participants plus actual adverse inception as the stable reference; use `open` only for supported current obtaining and add the recovered end to the claimed extent on closure. |
| Method-selected resolution | Finding a repair method is treated as ending the Problem. | Update the solvability claim; end PFR only when the adverse condition or another obtaining condition ceases. |
| Criterion-edition identity | Rewording or republishing a coextensional criterion creates a new Problem. | Recover the by-value predicate; create another applicability occurrence only when a fixed participant changes or when actual applicability ceases and later obtains again. |

### C.22.PFR:9 - Consequences

**Benefits.** PFR gives actual Problems stable identity without turning cards or evaluations into world-side constituents. Two entities or scopes can use one predicate without collision, repeated adverse episodes remain distinguishable, and ongoing episodes can be referenced before closure. Unknown evidence remains epistemically honest.

**Costs.** A load-bearing use must recover a by-value predicate, its exact condition-to-input rule and problem-for link, and one exact applicability relation. Direct consumer patterns must state how the selected point is obtained and how adverse truth is evaluated, including comparator and polarity semantics. Temporal identity requires a real recovery boundary rather than assessment timestamps.

**Limits.** C.22.PFR does not define domain criteria, measurement methods, comparator semantics, acceptance policy, evidence sufficiency, method search, repair work, or problem-card publication. It governs only actual Problem obtaining, dependence, projection, and occurrence identity.

### C.22.PFR:10 - Rationale

Applicability is independently useful: it states which predicate applies to which entity and use under which declared criterion-applicability window even when no adverse condition currently exists. Keeping those four participants canonical there prevents disagreements between duplicated fields, while maximal continuous actual obtaining distinguishes repeated applicability occurrences without adding a fifth participant. PFR adds the exact missing fact: the named actual condition is adverse for that applicability occurrence.

The maximal continuous adverse episode resolves a genuine identity collision, but its completed interval value is not a stable reference key. Participant references plus actual adverse inception retain one occurrence reference before and after closure; the derived end completes its extent. Actual non-adverse behavior ends the occurrence and later renewed adverse truth starts another. Assessments can support, refute, or leave those boundary claims unresolved, but they neither supply the world-side boundary nor create the occurrence.

### C.22.PFR:11 - SoTA-Echoing

| Current line | What it contributes | FPF adoption |
|---|---|---|
| FPF `A.19`, `A.19.CPM`, `G.4`, and direct state and gate patterns | Current FPF already separates characteristic-space predicate, comparison semantics, typed acceptance use, and supported outcome. | **Adopt directly.** Put the by-value predicate in applicability and leave comparison, acceptance, evaluation, and support with the selected consumer rather than duplicating them in PFR. |
| FPF `A.6.REL` relation-occurrence discipline | Relation occurrences can be explicit participants, and separate episodes with the same participants need a subject pattern-supplied boundary discriminator. | **Adapt.** Use the two relation participants plus actual adverse inception as the stable reference for one maximal continuous adverse episode; keep its recovered end as derived extent rather than a changing key field. |
| FPF `A.15.1` and `C.27.TA` temporal conventions | Temporal statements name bearer, reference, and interval, while later evidence can revise a claim about an occurrence without changing what occurred. | **Adapt.** Use `[adverseEpisodeStart, open]` only for supported current obtaining, publish a recovered end on the same stable occurrence reference, and keep unresolved continuity explicit rather than inferring a world-side boundary from evidence availability. |
| Operator seminar practice on development work, selected slides (2026) | Practical explanation separates problematization, characteristics and criteria, method search, performed work, working results, and repeated improvement while keeping them in one understandable progression. | **Adapt as a use-pressure test.** Keep actual PFR identity with the adverse condition and criterion applicability; keep method search, Work, results, and repetition as separate exact assertions under their own predicates, using `E.18.1`/`E.23` only for the applicable carry-through or improvement questions instead of making them PFR participants. |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint | Current relation and situation comparisons provide stress pressure for dependent relations, reification, and occurrence identity. | **Use as a comparator.** Retain a dependent relation with explicit participants and identity while avoiding a universal situation object or imported category hierarchy. |
| [TypeDB relation instances](https://typedb.com/docs/core-concepts/typeql/entities-relations-attributes/) | Relation instances can participate in other relation instances in an implementable model. | **Adapt as implementation evidence.** Permit actual-condition and applicability occurrences as PFR participants without treating the database model as the source of PFR truth. |

**External-source qualification and reopen.** The three non-FPF rows are qualified to the cited 2026 material and the current FPF direct relation and temporal interfaces used here. The selected seminar material is only a practice-pressure comparator for separating problematization, criteria, method search, performed work, and results; it supplies no ontology or occurrence law. The cited 2026 gUFO preprint is only a current research comparator for dependent relations, reification, and occurrence identity; its category hierarchy is not imported. The TypeDB Core Concepts documentation is only implementation evidence that relation instances can participate in relations; database semantics do not establish FPF truth or identity. Reopen only the affected row if later seminar material changes the separation being tested, a later gUFO edition changes the relevant relation or occurrence treatment, TypeDB changes the cited relation-participation semantics, or a current FPF subject pattern changes so that the comparison no longer tests this Solution. A carrier, hyperlink, or layout change with unchanged source content does not reopen the decision.

These lines change the Solution by keeping evaluation outside PFR, admitting relation occurrences as participants, identifying repeated episodes from actual adverse inception and cessation, and separating a stable world-side occurrence reference from revisable boundary claims.

### C.22.PFR:12 - Relations

- `A.6.REL` governs explicit individuation of both PFR participants and PFR itself when a receiving use needs identity.
- `A.6.RCD` governs each missing direct-condition or applicability relation decision; C.22.PFR keeps the affected case non-conforming until an existing direct predicate closes it or a separately admitted direct subject pattern supplies obtaining, recurrence, and occurrence identity.
- `A.6.5` governs the two PFR participant SlotSpecs and the four applicability SlotSpecs.
- `A.19` governs the characteristic space used by `CharacteristicSpacePredicate`; the selected direct consumer governs its condition-to-input rule and comparator semantics, `A.19.CPM` governs comparison when that is the consumer, and `G.4` governs typed acceptance clauses when acceptance is the consumer.
- `C.16`, `A.18`, and direct condition or measurement patterns define or constrain characteristics, scales, actual characteristic assignments or state relations, and measurements. F.9 governs any semantic Bridge named by the input rule; none of these adds a PFR participant.
- `C.22` governs selector-facing task typing and TaskSignature assignment after a problem-side episteme is usable.
- `C.22.2` governs ProblemCard claims, signals, forecasts, scenarios, anticipated-condition cues, descriptions, next use, and publication without creating PFR; the exact direct claim pattern defines or constrains each claim carried there.
- `A.15.1` and `A.3.4` govern repair work and changes to the actual-condition relation.
- `E.18.1`, `E.23`, and direct NQD and OEE patterns define or constrain repeated problematization, method search, work, evaluation, and continuation; relations locating or ordering those occurrences in a transformation-flow structure do not enter PFR identity.
- `C.27.TA` governs temporal aspect statements when interval publication or temporal adequacy is current.
- `A.10`, `B.3`, and `G.11` govern evidence use, assurance, and source or claim currentness.

### C.22.PFR:End

