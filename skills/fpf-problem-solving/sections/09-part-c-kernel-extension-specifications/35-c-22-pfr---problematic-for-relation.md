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

**Early battery contrast.** A battery-voltage condition below the applicable vehicle-start bound can already participate in an actual PFR before anyone notices it. A later maintenance card is an episteme describing that condition and Problem; writing or accepting the card creates neither. Discovering a supported charging or replacement method changes present solvability, not the still-adverse condition. Only actual change of the condition, loss of criterion applicability, or cessation of adverse predicate truth ends that PFR.

**Not this pattern when.** Use `C.22.2` when the current object is a problem-side card, signal, hypothesis, forecast, scenario, anticipated-condition claim, or reviewable formulation rather than an actual PFR. Use `C.27`, `C.28`, or the exact direct forecast, scenario, counterfactual, or anticipated-condition governor when that claim is current. Use the selected A.19 comparison, `G.4` acceptance, state, gate, or measurement pattern when the current question is how to evaluate or support the adverse predicate. Use `E.18.1`, `E.23`, and the direct NQD or OEE patterns for repeated problematization, search, work, evaluation, and continuation.

### C.22.PFR:2 - Problem

An actual Problem is neither a record nor a free-standing quality label. It depends on an actual condition and on a criterion that applies to one exact entity, scope, and interval. The relation obtains when the condition is on the adverse side of that applicable predicate.

FPF needs one identity for this dependent evaluative relation without copying values owned by `ProblemCriterionApplicabilityRelation` into additional writable PFR slots. It also needs to distinguish continuous adverse episodes from repeated episodes while refusing to infer a recovery from missing observations or evidence.

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

- **Direct input:** the actual-condition participant is already a governed characteristic-assignment or state relation whose direct owner exposes the exact characteristic-space coordinate, scale, and value used by the predicate.
- **Projected input:** when that relation does not itself expose the needed point, the rule cites one exact governed projection or bridge, its source relation kind and participant positions, target characteristic space, coordinate and scale, and the direct relation or predicate connecting that input to the problem-for entity and receiving use.

A relation reference alone is not a coordinate. If neither path yields the exact point and the problem-for link, adverse truth and PFR remain unestablished. When two projections are plausible, the rule names the selected one and the nearest inadmissible projection. `ConditionToPredicateInputRule` is a pattern-local by-value rule inside `CharacteristicSpacePredicate`; it is not a U-kind, relation occurrence, evaluation result, or copied PFR field.

**Public name settlement.** The following F.18 NameCard names the applicability relation kind. It does not make one applicability occurrence obtain and does not replace the relation signature below.

```text
NameCard:
  NameCardId: NC-PROBLEM-CRITERION-APPLICABILITY-RELATION
  GovernedValueRef: ProblemCriterionApplicabilityRelation under C.22.PFR
  GoverningPatternRef: C.22.PFR
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

**Public name settlement.** The following F.18 NameCard names the actual dependent evaluative relation. It does not create the Problem, add a third participant, or replace the occurrence-identity rule.

```text
NameCard:
  NameCardId: NC-PROBLEMATIC-FOR-RELATION
  GovernedValueRef: ProblematicForRelation under C.22.PFR
  GoverningPatternRef: C.22.PFR
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

PFR has no separately writable condition-bearer, predicate, problem-for-entity, claim-scope, applicability-window, assessment-window, or description-edition slot. Those values already have canonical owners. A readable claim projects them from the two participants:

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
3. Apply the predicate's exact `ConditionToPredicateInputRule` to the actual-condition participant. It must yield the declared characteristic-space point or value and the direct link to the problem-for entity and use; that point then falls on the adverse side under the selected scale, comparator, cut or band, polarity, and admissibility semantics.

The selected direct consumer supplies the governed input projection or consumes the direct characteristic assignment, then governs the comparator and admissibility semantics. An evaluation may calculate or support a claim that the resulting point is adverse. Comparison outcomes, acceptance outcomes, state or gate results, measurements, evidence, and assessment claims are not automatically PFR participants, and producing them does not make PFR obtain.

A Problem can therefore obtain unnoticed. Later detection produces work, evidence, and claims about the already obtaining relation; it does not create retroactive actuality.

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

#### C.22.PFR:4.6 - Keep anticipated-condition claims, solvability, and cards separate

A possible or anticipated problem remains an exact forecast, scenario, counterfactual, or anticipated-condition claim in `ProblemCard@Context` or another episteme until an actual-condition relation, an applicability relation, and adverse predicate truth all obtain. `C.2.1` governs its assertion identity and polarity; `C.27`, `C.28`, or the exact direct claim pattern governs assumptions, horizon, and non-actual semantics; `A.10` or the receiving evaluation separately governs supported, refuted, or unresolved reliance. None of those claim-side facts establishes a current PFR. A card may describe zero, one, or several independently obtaining PFR occurrences; several cards may describe one PFR under different viewpoints.

A claim that no supported method is currently available concerns the admitted method set, evidence, constraints, and acceptance use. Selecting or discovering a method changes current solvability. It does not end PFR while the actual condition remains adverse. Performed repair work can end or change the actual-condition occurrence and thereby end PFR.

Repeated problematization, method search, work, evaluation, and continuation occur in work and transformation flows governed by `E.18.1` and `E.23`. A claim or plan may carry a reference to the same PFR while work and transformation occurrences participate in a selected transformation-flow structure. Neither that PFR reference use nor any flow-structure relation enters PFR identity. A later PFR is a later occurrence because a participant changes or because actual adverse truth begins again after an actual cessation; the stable reference therefore carries a different participant reference or actual adverse inception, not a different assessment or flow visit.

#### C.22.PFR:4.7 - Preserve the lightweight path

For a first use, name only what decides the case:

1. the exact obtaining condition and the value or point it supplies;
2. the criterion that makes that point adverse, including the selected input path and cut or band;
3. the entity for which it is a Problem, the use or claim scope, and the applicability window.

Then write one ordinary sentence:

> `<condition and value>` misses `<criterion>` for `<entity and use>` during `<applicability window>`; therefore it is an actual Problem for that entity and use.

Stop there when the next work only needs to recognize the Problem. Cite the direct condition and criterion owners, but do not fill a PFR record, repeat either relation signature, or assign a PFR identifier. The NameCards and signatures above define reusable semantics; they are not a mandatory user form.

Add explicit identity only when another claim must compare, qualify, change, nest, plan from, or refer back to this particular Problem occurrence. That receiving claim then names the exact actual-condition occurrence, exact applicability occurrence, actual adverse inception or stable PFR identifier when needed, claimed extent, and any evidence or assessment claim on which its reliance depends. The evidence remains separate from the world-side Problem.

### C.22.PFR:5 - Archetypal Grounding

**Executable first use — `Battery-12` cannot support `Van-7`'s intended start.** At 10:02 the starter of `Van-7` is engaged. The project electrical owner identifies one obtaining `TerminalVoltageState-12` relation with bearer `Battery-12`, load condition `Van7StarterLoad-1`, and characteristic assignment `terminalVoltageUnderStarterLoad = 10.8 V` on the volt scale. That state relation actually obtains from 10:02 until `Battery-12` is removed from `Van-7` at 10:06.

The same case has one `Van7StartCriterionApplicability-12` occurrence. Its by-value predicate `Van7StartVoltageAtLeast11_8` selects the direct `terminalVoltageUnderStarterLoad` input, cut `11.8 V`, and lower-is-adverse polarity. It governs problem-for entity `Van-7`, claim scope `intended engine start at Depot-A`, and declared applicability window `[09:55, 10:15]`. The exact C.13 Working-Model occurrence `ut:ComponentOf(Battery-12, Van-7)` connects the condition bearer to that vehicle. Because the selected point is `10.8 V`, the PFR actually obtains on `[10:02, 10:06]`.

`MeterReport-88` is a separate assessment claim: it says that the terminal voltage under starter load was `10.8 V` at 10:03 and supports the claim that the PFR obtained then. The report did not make the voltage state, applicability, or PFR obtain.

The resulting ordinary sentence is:

> Battery-12 supplies 10.8 V under Van-7's starter load, below the 11.8 V start cut during the 09:55–10:15 intended-start window; this low loaded voltage is an actual Problem for Van-7's intended start from 10:02 until Battery-12 is removed at 10:06.

**Cheapest valid stop.** A mechanic who only needs to recognize this Problem records that sentence, cites the two world-side relation-occurrence references `TerminalVoltageState-12` and `Van7StartCriterionApplicability-12`, and keeps `MeterReport-88` as the separate supporting claim; no explicit PFR record or identifier is required.

**One receiving-use expansion.** A recurrence comparison that must distinguish this episode from a later low-voltage episode additionally records the two participant-occurrence references, actual inception `10:02`, stable `pfrOccurrenceId=PFR-VAN7-START-20260723-1002`, the claimed closed extent `[10:02, 10:06]`, and the separate supporting claim `MeterReport-88`. Those references let the comparison point back to this occurrence; none is an extra PFR participant.

**Near miss — same number, wrong input.** `OpenCircuitVoltageMeasurement-89` also reports `10.8 V`, but it was taken after `Battery-12` was removed from `Van-7` and supplies the coordinate `openCircuitTerminalVoltage`, not `terminalVoltageUnderStarterLoad`. The start predicate's input rule rejects that measurement, and the condition-to-vehicle/use link is absent. The same numeric value may matter under another criterion, but it does not establish a Problem for `Van-7`'s intended start.

**Distinct projected-input branch — proof gap.** `UnresolvedConsequence-17` is the exact obtaining relation inside `SafetyProof-v5`; the proof-acceptance consumer's named `RequiredObligationGapCountProjection-v1` maps only unresolved required obligations of that proof to coordinate `unresolvedRequiredObligationCount = 1` in `ProofAcceptanceSpace`, on the natural-count scale with cut `0` and greater-than-zero-is-adverse polarity. `ReleaseAssuranceClaim-3` is the problem-for entity. The exact A.10 evidence-provenance graph occurrence `SafetyProofEvidencePath-3` names `SafetyProof-v5` as its evidence episteme, `ReleaseAssuranceClaim-3` as its target claim, and the release-assurance use stated by that claim's B.3 tuple as its bounded relying use. Counting every TODO in the repository is inadmissible because those items are neither required proof obligations nor evidence for that release-assurance claim.

**Distinct claim/actuality branch — clinical diagnosis.** A patient-specific clinical-condition relation, an obtaining applicability relation, and actual adverse predicate truth can make PFR obtain before any diagnosis is authored. A later diagnosis episteme may support a claim about that PFR but does not become its condition participant, problem-for entity, or inception boundary.

**Distinct problem-for branch — missed transfer.** A missed-transfer relation can be the condition while one exact receiving Work occurrence is the problem-for entity. The coordination participants stay in the missed-transfer relation; the applicability relation names the affected Work as its problem-for entity rather than copying it into PFR.

**Distinct multiplicity branch — one condition, two uses.** One hot-surface condition paired with two applicability occurrences for different exact receiving work or systems yields two PFR occurrences when the condition satisfies both adverse predicates. The applicability references distinguish them; PFR copies neither receiving participant nor scope.

**Distinct actuality/repair branch — unnoticed and repaired.** A condition and applicability can make PFR obtain before monitoring exists. Selecting a repair method changes only the solvability claim. Performed repair work ends PFR only when its world-side result actually ends or changes an obtaining condition; work records and result claims remain separately governed.

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
| FPF `A.6.REL` relation-occurrence discipline | Relation occurrences can be explicit participants, and separate episodes with the same participants need a direct owner-supplied boundary discriminator. | **Adapt.** Use the two relation participants plus actual adverse inception as the stable reference for one maximal continuous adverse episode; keep its recovered end as derived extent rather than a changing key field. |
| FPF `A.15.1` and `C.27.TA` temporal conventions | Temporal statements name bearer, reference, and interval, while later evidence can revise a claim about an occurrence without changing what occurred. | **Adapt.** Use `[adverseEpisodeStart, open]` only for supported current obtaining, publish a recovered end on the same stable occurrence reference, and keep unresolved continuity explicit rather than inferring a world-side boundary from evidence availability. |
| Operator seminar practice on development work, selected slides (2026) | Practical explanation separates problematization, characteristics and criteria, method search, performed work, working results, and repeated improvement while keeping them in one understandable progression. | **Adapt as a use-pressure test.** Keep actual PFR identity with the adverse condition and criterion applicability; route method search, work, results, and repetition through their direct patterns and `E.18.1`/`E.23` instead of making them PFR participants. |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint | Current relation and situation comparisons provide stress pressure for dependent relations, reification, and occurrence identity. | **Use as a comparator.** Retain a dependent relation with explicit participants and identity while avoiding a universal situation object or imported category hierarchy. |
| [TypeDB relation instances](https://typedb.com/docs/core-concepts/typeql/entities-relations-attributes/) | Relation instances can participate in other relation instances in an implementable model. | **Adapt as implementation evidence.** Permit actual-condition and applicability occurrences as PFR participants without treating the database model as the source of PFR truth. |

These lines change the Solution by keeping evaluation outside PFR, admitting relation occurrences as participants, identifying repeated episodes from actual adverse inception and cessation, and separating a stable world-side occurrence reference from revisable boundary claims.

### C.22.PFR:12 - Relations

- `A.6.REL` governs explicit individuation of both PFR participants and PFR itself when a receiving use needs identity.
- `A.6.5` governs the two PFR participant SlotSpecs and the four applicability SlotSpecs.
- `A.19` governs the characteristic space used by `CharacteristicSpacePredicate`; the selected direct consumer governs its condition-to-input rule and comparator semantics, `A.19.CPM` governs comparison when that is the consumer, and `G.4` governs typed acceptance clauses when acceptance is the consumer.
- `C.16`, `A.18`, and direct condition or measurement patterns govern characteristics, scales, actual characteristic assignments or state relations, and measurements. F.9 governs any cross-reference-scheme bridge named by the input rule; none of these adds a PFR participant.
- `C.22` governs selector-facing task typing and TaskSignature assignment after a problem-side episteme is usable.
- `C.22.2` governs ProblemCard claims, signals, forecasts, scenarios, anticipated-condition cues, descriptions, next use, and publication without creating PFR; the exact direct claim pattern governs each claim carried there.
- `A.15.1` and `A.3.4` govern repair work and changes to the actual-condition relation.
- `E.18.1`, `E.23`, and direct NQD and OEE patterns govern repeated problematization, method search, work, evaluation, and continuation; relations locating or ordering those occurrences in a transformation-flow structure do not enter PFR identity.
- `C.27.TA` governs temporal aspect statements when interval publication or temporal adequacy is current.
- `A.10`, `B.3`, and `G.11` govern evidence use, assurance, and source or claim currentness.

### C.22.PFR:End

