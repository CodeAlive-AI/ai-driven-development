## NSTD.6 - Declared-Use Narrative Rendering Quality Evaluation

> **Status:** Stable

> **Type:** DPF evaluation pattern body

> **Primary EntityOfConcern:** `NarrativeRenderingQualityEvaluationCharacteristicSpace@Context`, an evaluation `CharacteristicSpace` for one evaluated narrative rendering kind and declared use.

### NSTD.6:1 - Problem frame

Use this pattern when a team must decide whether one narrative rendering version, including an unaccepted candidate, is good enough for one declared reader or listener use. An editor may evaluate a directly authored or already existing product without knowing how its author produced it. State whether the present question concerns that product's current quality, a promised source-to-result relation, or assurance about actual construction work; these questions need different evidence.

Evaluated object kind: `NarrativeRenderingVersion@Context`, an identifiable version of a narrative account in a form a reader can use. A seminar script, slide sequence or generated draft can express such an account. Select the narrative and its intended use within a larger source collection or teaching programme; evaluating that collection's authority, the generation method or the whole programme is a different question. Missing source relations or poor quality are possible findings, not reasons to exclude a narrative candidate before evaluating it.

First useful move: identify the narrative version, reader and intended use, then select the relations and characteristics on which that use depends. Compare an adequate account with a deficient one. Distinguish those from a question about a different object, such as the generation method rather than its resulting narrative.

What goes wrong if missed: readability, elegance, engagement, expert approval, or generated fluency substitutes for epiplexity, source-return discipline, and bounded use.

What this buys: a repeatable evaluation that can feed `E.23` improvement without confusing characteristics, measurements, eval programs, evidence, assurance, or gates.

Quality target: this pattern evaluates quality for one declared use under source-structure selection fit, `NarrativeRenderingEpiplexity`, ordering recoverability, temporal-posture and role fit, source-return readiness, bounded engagement, and owner-routed evidence, assurance, ethics, publication, and work claims.

### NSTD.6:2 - Problem

Narrative rendering quality for declared use is not one property. A narrative can be fluent but structurally false, engaging but ethically unsafe, technically accurate but unusable for learners, or source-faithful but impossible to follow. A useful evaluation needs object-kind fit, characteristic slots, value meanings, evidence basis, missingness rules, floor, exceptional meaning, result-row shape, and repair actions.

### NSTD.6:3 - Forces

| Force | Tension |
| --- | --- |
| Fluency vs epiplexity | A readable narrative may pull too little selected source structure into the rendering for the declared use. |
| Engagement vs bounded use | A motivating narrative may overpersuade. |
| Local usability vs reusable scale | A project can use a small rubric, but DPF needs reusable value meanings. |
| Measurement vs evaluation | Some values may be measured through `C.16`; many are ordinal content evaluations. |
| Improvement vs Goodhart pressure | Indicatorized characteristics help loops, but unmeasured tracked concerns must prevent proxy capture. |

### NSTD.6:4 - Solution

Construct and use one narrative rendering quality evaluation characteristic space for one declared use. Reuse a sufficient current specification and result when their object, question and conditions still match.

For explanatory technical prose, apply `F.19` in the same connected reading, with its declared-use and genre conditions. Recover the governing message, compare it with the selected source and test what each optional contrast, caveat or extra proposition contributes to this reader. Use `F.19:4.4` for a proposed warning and `F.19:4.5` for the reading basis needed by the conclusion. This supplies the semantic and pragmatic wording judgement within `LanguageStatePrecisionAndCoarseningFit`.

Establish what counts as a supported answer for this use. For a factual account, its working interpretation must remain answerable to the evidence. For a literary interpretation, compare the reading with the relevant text and serious alternatives. For an intentionally open narrative, correct recovery may include recognising why several interpretations remain possible. For a new fictional construction or hypothetical scenario, inspect the chosen premises and consequences as well as the resulting experience. NSTD.9 and NSTD.10 supply the corresponding interpretive or constructive work when it is missing. Fidelity to one earlier representation alone cannot establish that the representation was adequate, that a new story is worthwhile, or that its audience responded as intended.

For the structural-amount question, `NarrativeRenderingEpiplexity` specializes [FPF `C.2.8 ExtractableStructuralInformation`](../../sections/09-part-c---kernel-extension-specifications/12-c-2-8---extractablestructuralinformation-structure-this-read.md): the structure this reader or observer can extract. Its three bearers are the receiving narrative episteme, the particular expression conveying it, and the specified reader or observer. The selected source structure, correctness criterion, usable prior knowledge, operations, help, access and budget qualify this tuple. An unambiguous rendering reference can identify the account and expression. Use the existing epiplexity basis, scale and evidence fields below to retain the qualifications needed for the comparison; they do not create another bearer or record kind.

Begin with named additional and missing relations when a qualitative comparison answers the question. If a number is useful, count correctly recovered selected semantic relations at a declared grain, optionally as `n/N` for a fixed nonempty selected set. Each unit preserves participants, predicate, polarity, modality and action-changing conditions. Repeated words, headings or arrows do not add units. Retain which relations were recovered: equal counts can differ in suitability for the next use. A different ordinal or nonnegative structural weighting needs its own explicit structural meaning; a utility weighting is another score. A formal bit estimate needs the mapping in `C.2.8`, not merely the name epiplexity.

State whether the basis is a conditional design walkthrough, an actual reading or a mapped formal estimate. One response establishes the recovery observed in that trial and can ground an extractability estimate; it does not establish a maximum, impossibility after failure, or reliability across a reader class. An exact computational amount requires the corresponding method and model. Keep the first response, actual help and source returns. Familiar structure can be recovered from an expression; an expert's independent correction of false or absent instruction earns that expression no credit. Recovery of what a source asserts and recovery of warranted subject structure use different correctness questions.

For a comparison intended to isolate a change of expression, hold the expressed claims and other relevant conditions constant. Added or changed substantive claims can identify another episteme through `C.2.1`; changed access, preparation or help qualifies another comparison. A transfer or perturbation result belongs to its tested condition or robustness question and adds nothing to the original amount by itself. Compare effort and usefulness separately through `C.11.CRC` and `C.11`; keeping the sufficient rendering is an available result.

```text
NarrativeRenderingQualityEvaluationCharacteristicSpace@Context:
  evaluatedObjectKindRef: NarrativeRenderingVersion@Context
  declaredUseScope:
  objectKindFitRule:
  discriminatingCaseSet:
  characteristicSlotSet:
  epiplexityBasisRule:
  scaleBindingSet:
  valueMeaningSet:
  evidenceBasisRule:
  missingnessAndLoweringRule:
  resultRowShape:
  floorAndExceptionalMeaning:
  protectedTradeoffSet:
  stopOrReopenCondition:
  neighboringGoverningPatternRefs:
```

Object-kind fit:

| Object-kind case | Handling |
| --- | --- |
| Narrative account, whether candidate or accepted | Evaluate every characteristic whose failure would defeat the intended use. |
| Below-floor narrative rendering | Evaluate and return low-value repair actions. |
| A different object is being evaluated | Select an evaluation for that object; for example, a generator's reliability or a source archive's authenticity is not the quality of one resulting narrative. |
| Wrong-kind object after invocation | Record explicit object-kind-fit defect and stop; do not silently assign values to unrelated coordinates. |

Default value meanings for the other ordinal content-quality characteristics follow. `NarrativeRenderingEpiplexity` uses its own structural scale above; the following 0–5 labels do not assign its amount, missingness or use threshold:

| Value | Meaning |
| --- | --- |
| `0` | The characteristic has no usable basis or the evaluation stops before a quality value can be used. Record the cause; this code is not a structural amount. |
| `1` | Object is a narrative rendering but unusable for the declared use. |
| `2` | Orientation only; source return is needed before reliance. |
| `3` | Locally usable with named limitations and repair obligations. |
| `4` | Good for declared use with bounded losses and source return. |
| `5` | Strong for declared use; the current source relation, response to a meaningful change, and consequential boundary cases are replayable. Actual construction or repair history is additionally replayable when a historical claim is part of the declared use. |

For reliance-bearing or teaching use, the default for structural recovery is that every relation declared necessary for that use must be recoverable under the specified support and evidence conditions. State those necessary relations at the grain the decision needs; a short account of the required distinction and stop can suffice. There is no generic structural-amount floor of `4`. Keep the amount and satisfaction of the use condition separate: unrelated extra relations cannot compensate for a missing necessary relation.

The other load-bearing quality characteristics retain default floor `4` on their own scales, including `OrderingRecoverability` and `SourceReturnReadiness`. When the selected source structure is a constraint-governed unfolding structure, `DemonstrativeSliceRecoverability` is load-bearing and may not be below `4`. A local low-risk orientation use may set those quality floors to `3` only if non-admissible downstream use is explicit. Neither numeral translates into a structural amount. A narrower use fixes its structure selection before evaluation; removing a difficult relation after observing the answer changes the basis rather than improving the original amount.

Result-row shape:

```text
NarrativeRenderingQualityResultRow@Context:
  narrativeRenderingVersionRef:
  declaredUseScopeRef:
  characteristicId:
  characteristicName:
  scaleRef:
  value:
  evidenceBasisRefs:
  missingnessClass:
  loweringReason:
  repairAction:
  directOwnerRefs:
  reopenCondition:
```

Package the rows before feeding an improvement loop:

```text
NarrativeRenderingQualityEvaluationResult@Context:
  evaluatedNarrativeRenderingVersionRef:
  declaredUseScopeRef:
  evaluationCharacteristicSpaceRef: NarrativeRenderingQualityEvaluationCharacteristicSpace@Context
  evaluationPurpose:
  evidenceBasisRefs:
  resultRows:
  protectedTradeoffSet:
  belowFloorRows:
  candidateImprovementProposalRows?:
  nonUseBoundary?:
  stopOrReopenCondition:
```

When repeated improvement is wanted, open `E.22` first if the quality question is not already framed. Then use `E.23` with `NSTD.6` as the object-under-improvement evaluation.

```text
NarrativeRenderingImprovementLoopInput@Context:
  e22QuestionFrameRef?:
  objectUnderImprovementRef: NarrativeRenderingVersion@Context
  objectVersionBeforeRef:
  objectUnderImprovementEvaluationRef: NSTD.6
  improvementAim:
  protectedTradeoffSet:
  costAndRiskAccount:
  allowedChangeSlice:
    narrativeRenderingVersion | NSTD.1-intake | NSTD.2-ordering |
    NSTD.3-event-model | NSTD.4-viewpoint | NSTD.5-engagement |
    NSTD.7-generation-and-inspection | NSTD.8-learning-route |
    NSTD.9-interpretation | NSTD.10-story-construction |
    evaluationCharacteristicSpace
  returnedFindingOrProposalRows:
  expectedReEvaluationResultForm: NarrativeRenderingQualityEvaluationResult@Context
  neighboringGoverningPatternRefs:
  stopContinueSwitchOrHoldCondition:
```

`E.23` may claim improvement only after the changed object version is re-evaluated through `NSTD.6` or through a declared stronger evaluation. If the loop changes the source pack, source-currentness, generated-carrier admission, learning publication carrier, publication face, ethics claim, evidence claim, assurance claim, or evaluation characteristic space, the loop must name the neighboring governing pattern and either keep it as the allowed change slice or open separate work. Style edits, prompt retries, or additional drama are admissible loop operations only when their expected movement under `NSTD.6` is stated and protected trade-offs are checked. `B.4` is relevant only when the narrative episteme or learning route is claimed to evolve across use and renewed operation; `G.11` handles a change in source currentness, reader telemetry, teaching-test evidence, generated-narrative practice or FPF edition when it could alter support for the receiving use; retain sufficient unaffected results.

Before assigning values, recover the source and use basis for the question being answered.

For current-product evaluation, name the selected subject structures, intended reader work and necessary prerequisites, then trace what the present rendering preserves, hides or loses. Use the task and qualified subject sources to establish the needed structure; the rendering can help refine that basis but cannot excuse its own omissions. Recover its ordering rationale, source-return condition, and the event or mechanism, viewpoint, agency, engagement and learning-route relations that matter to this use through `NSTD.1` through `NSTD.5` and `NSTD.8`. Point to actual source and rendering passages. If this account is reconstructed now, identify it as an evaluation of the current product, with its uncertainties, not a record of what the author did. Missing manufacturing notes do not by themselves lower current-product values; missing subject basis, inaccessible return or unsupported relation still does.

For a promised transformation, compare the named source and result versions against the promised preservation or change. This can establish their present fidelity relation without establishing the actual sequence of manufacturing actions. For a claim about actual construction or repair, obtain records or other admissible evidence of those actions and distinguish them from a plausible reconstruction. Trace the applicable `NSTD.1` selection, `NSTD.2` ordering, `NSTD.3` mechanism, `NSTD.4` viewpoint, `NSTD.5` engagement and `NSTD.8` learning-route decisions. If their history cannot be established, leave that historical or assurance claim unsupported and return it to its owner. A good product does not supply the missing history.

A candidate can be evaluated before acceptance; the result can inform acceptance, repair or rejection. Additional requirements follow from the proposed use and claims. When generated or discovered content is intended to inform architecture work, `C.35` supplies that assessment. Reuse as evidence requires the relevant subject grounds; `A.10` recovers the source-to-use account when it is implicit or must remain replayable. Assurance, publication authority and actual human learning-effect claims require their own grounds. None of those conclusions follows merely from a favourable narrative-quality result.

Use this evaluation sequence:

1. Object-kind fit: which narrative account and version is being assessed? Identify it in its text, slide sequence or other form. A question about the source collection, generator or whole teaching programme returns to the evaluation for that different object.
2. Evidence fit for the question: for current-product quality, recover selected source structures, ordering, source return and relevant relations from the subject/use basis and present rendering; for promised fidelity, compare the named source and result; for actual construction or repair, recover evidence of the claimed actions. Keep these conclusions distinct.
3. Declared-use fit: which reader or listener work is this result to inform, and under what conditions? State a limitation when it changes the use of that result.
4. Load-bearing characteristics: assign values only to the characteristics needed for the declared use, but include every characteristic whose failure would make the use unsafe or useless.
5. Low-value repair: for every value below floor, name the smallest repair route before proposing style, drama, or generation retries.
6. Re-evaluation route: if any repair changes the object version or selected source basis, plan a new `NSTD.6` evaluation before claiming improvement.

Missingness and lowering rules:

| Missing or defect condition | Lowering rule |
| --- | --- |
| Selected source structures cannot be identified from the subject/use basis | Leave the structural amount unassigned. Use `NSTD.1` for a selection gap, `NSTD.9` for a missing or disputed working interpretation, or `NSTD.10` for proposed events that still need construction. A missing basis is not a small amount; apply any actual object-kind defect separately. |
| Reader, correctness criterion or other action-changing structural-comparison condition cannot be recovered | Leave the amount unassigned at that scope; retain any narrower supported result and continue independently answerable diagnosis. An absent observation is not a zero. |
| Ordering rule absent | `OrderingRecoverability` no higher than `2`. |
| A missing time, viewpoint, participant or mediation distinction changes the reader's interpretation | `TemporalPostureAndRoleFit` no higher than `2` for that use; return the specific ambiguity to `NSTD.1` or `NSTD.4`. A missing optional record field alone is not a defect. |
| A relevant source-selection rationale or reader-use hypothesis cannot be recovered | `SourceStructureSelectionFit` no higher than `2` for that use; return the selection question to `NSTD.1`. Lower `TemporalPostureAndRoleFit` only if its time or participant distinctions are also missing. Leave structural amount unassigned only when its own selection, correctness or observer basis is unavailable; a missing optional field alone does not erase a recoverable basis. |
| Source-return condition absent | `SourceReturnReadiness` no higher than `2`. |
| Constraint-governed unfolding structure is selected but the rendering declares only a sequence, route card, story line, or lesson chain | `DemonstrativeSliceRecoverability` no higher than `2`; return to `NSTD.1`, `NSTD.2`, and `A.22.CGUS` or the local governing pattern before treating the narrative as a rendering of the wider structure. |
| Literary, simplified or dramatic wording hides or distorts a source relation, precision distinction or coarsening limit needed for the declared use | `LanguageStatePrecisionAndCoarseningFit` no higher than `2` for that use. Identify the missing relation or limit and repair it directly when its meaning is determined. Use `C.2.LS`, `A.6.3.CSC`, `E.17.EFP`, `E.10`, `A.6.P` or `C.16.Q` for the particular unresolved language-state, coarsening, explanation or precision question; then re-evaluate the present rendering. |
| Only an intended effect or seed is available, without an identifiable narrative account | No narrative version is yet available for this evaluation. Develop the cue through `A.16.1`, `NSTD.1` or `NSTD.2`, or evaluate the cue for its own use. |
| An intended persuasive use conceals a material uncertainty, risk or alternative needed for the reader's choice | `EngagementBoundedness` no higher than `3`; restore that condition or alternative through `NSTD.5`. If a consequential value or harm question remains, identify the affected party and question and use the applicable `D.1`–`D.5` contribution. An ordinary curiosity device alone requires no additional ethics work. |
| Generated account has not yet been accepted for use | Evaluate the available candidate and retain the grounds and limits of each result. Use `NSTD.7` for generation repair; use `C.35` only when the result is intended to inform architecture work. |
| Unsupported evidence or assurance claim | Qualify the unsupported claim and recover its defining or testing rule. Use `A.10` for an implicit or needed replayable source-to-use account, and `B.3` for an actual named assurance claim. Lower a relevant quality value only under its own meaning. An unsupported structural amount is unassigned rather than numerically penalized. |
| Manufacturing or repair history absent while the current-product basis is available | Do not lower a product characteristic for this absence alone. Leave any historical claim unsupported and return the evidence or assurance question to its owner; apply every relevant source, use, admission and missingness rule independently. |

A defined trial that recovers none of the selected relations supports observed recovery `0` on that scale, not impossible extraction. An empty denominator supports no fraction. Wrong-kind handling precedes amount assignment. A qualified design estimate can remain available without an actual trial; obtain a trial when its possible outcomes can change the receiving decision.

Default narrative rendering quality characteristics:

| Characteristic | Evaluation question | Low-value repair action |
| --- | --- | --- |
| `SourceStructureSelectionFit` | Are the selected source structures and reader-interest or use hypothesis explicit, non-magical, and well matched to the declared use? | Reopen `NSTD.1`; reconstruct or revise the source-structure selection rationale before changing style, drama, or prompt wording. |
| `NarrativeRenderingEpiplexity` | What selected structure can this observer correctly extract from the narrative episteme through this expression under the declared conditions, and how does that compare with the alternative? | Use `C.2.8` for the common characteristic. Return a selection gap to `NSTD.1`; repair the missing or false relation, its expression or its usable source return through the relevant NSTD method. A better basis declaration alone does not increase amount. `C.33` separately governs architecture-description adequacy when that question is live. |
| `OrderingRecoverability` | Can the reader say why this sequence was chosen and what it hides? | Reopen `NSTD.2`; state ordering rule, preserved relations, and lost relations. |
| `DemonstrativeSliceRecoverability` | When a constraint-governed unfolding structure is selected, can the reader recover the wider structure, the demonstrative slice, and the hidden branches, loops, alternatives, direct exits, or stop conditions? | Reopen `NSTD.1` and `NSTD.2`; name the selected CGUS or local block, the demonstrative slice, preserved constraints, lost structure, and return to `A.22.CGUS` or the local governing pattern. |
| `TemporalPostureAndRoleFit` | Are time stance, mediation and the relevant participant or viewpoint distinctions clear enough for the declared use? Work-role, performer/assignment or architecture-admission information is needed only for the corresponding claim. | Reopen `NSTD.1` or `NSTD.4`; clarify observed, live, proposed or fictional material and distinguish the narrative voice from any actual participant. Examine a further Work or admission basis when that claim is made. |
| `EventMechanismSupport` | Can the reader reconstruct events, mechanisms, dependencies, or state changes when required? | Reopen `NSTD.3`; add mechanism support or lower causal language. |
| `ViewpointAgencyDiscipline` | Does viewpoint reveal source structure without false agency, capability, responsibility, or permission? | Reopen `NSTD.4`; split protagonist, actant, role, agency, and ethics owners. |
| `EngagementBoundedness` | Does engagement serve the intended effect while preserving source relations and the conditions needed for the reader's choice? | Reopen `NSTD.5`; restore the missing condition, revise the device or keep a sufficient simpler account. |
| `LanguageStatePrecisionAndCoarseningFit` | Does the chosen language state make the needed relations, precision and coarsening limits recoverable for this use? In explanatory technical prose, what does each optional rhetorical branch contribute to the intended reader? | Apply the connected `F.19` reading to explanatory technical prose, retaining the distinctions that change its use. For a remaining question, use `C.2.LS` for a threshold-bearing language-state profile, `A.6.3.CSC` for narrowed-use coarsening, `E.17.EFP` for explanation-facing retelling, `A.16.1`/`A.16.2` for cue or backoff, and `E.10`, `A.6.P` or `C.16.Q` for precision restoration. |
| `EthicsEvidenceAssuranceRouting` | When a consequential value, harm, evidence, assurance or policy claim is made, are its grounds and limits available for the intended use? | Identify the unresolved question, then use the corresponding `D.1`–`D.5`, `A.10`, `B.3` or professional contribution. A generic owner name does not answer the question. |
| `MediumAndPublicationFit` | Does the carrier fit the reader and use without changing the claim? | Route publication or audience-unit questions to `E.17`, `E.17.AUD`, or `NSTD.8`. |
| `SourceReturnReadiness` | Does the narrative tell readers when and where to return to the source basis or relevant method? | Add the missing return condition or destination, or narrow the supported use. |
| `LearningRouteReconstructionFit` | For a learning route, do the responses meet the declared reconstruction task and source-return condition under the specified support? | Use `NSTD.8` to repair the source contribution, support or next task. Distinguish a supplied design response from an actual learner response. |

`LearningRouteReconstructionFit` is an additional characteristic for teaching uses. It uses the ordinal quality meanings above and the adjacent calibration below; it is not a structural-amount scale.

### NSTD.6:5 - Archetypal Grounding



#### NSTD.6:5.1 - Value bank: full result rows


Use this bank when a narrative rendering "sounds good" and therefore tempts the worker to skip evaluation. Each row illustrates evaluation of a narrative version for one declared use; prior acceptance is unnecessary. The same text may receive different values for a different use.

| Case | Characteristic | Value | Evidence basis | Low-value repair |
| --- | --- | --- | --- | --- |
| FPF seminar handout | `NarrativeRenderingEpiplexity` | Qualitative illustration; no numerical amount established | The case assumes learners can recover `EntityOfConcern`, forces, solution and neighboring exits. These aspect names do not define equal semantic units, a denominator or an observed reading protocol. | Retain the stated recovery. If transfer matters, try choosing a governing pattern in a new situation and qualify that separate result; it does not increase the original amount. |
| FPF seminar handout | `SourceReturnReadiness` | `4` | In this constructed handout, each slogan links to its pattern; the exercise sends the reader to that pattern's conditions before applying the slogan in a new situation. This supplies a when-and-where return, but no changed-condition response or boundary replay for `5`. | Reopen if the task, reader preparation or source access changes, or if the reader cannot locate or use the return. Repair that failure even when the source text is unchanged. |
| FPF seminar handout | `EngagementBoundedness` | `4` | The constructed failure story invites readers to compare workload conditions and makes the relevant conditions available for that comparison. Its fictional status is clear. The value expresses a design judgement; an attention-gain claim would need an observed comparison. | Reopen a changed reader effect or stronger benefit claim; restore a condition the persuasive use needs or obtain grounds for that particular claim. |
| Homotopy explanation | `LanguageStatePrecisionAndCoarseningFit` | `3` | Analogy is vivid but learners may not know where formal conditions return. | Add an analogy-stop line and a formal boundary task. |
| Homotopy explanation | `OrderingRecoverability` | `4` | Didactic order is named and proof order is deferred by value. | To reach `5`, add a second problem where learner maps story order to formal dependency order. |
| Franchise continuation probe | `SourceReturnReadiness` | `4` | An illustrative repair of the Readme's key case puts this return in the draft: “If a scene assumes access before Wednesday, consult the supplied premise that the character first obtains the key on Wednesday.” The condition and destination are explicit. | If the premise or proposed access changes, reopen that continuity comparison. Check a changed case when robustness matters; private or public use alone does not change this value. |
| Live commentary | `EventMechanismSupport` | `3` | Observation and provisional interpretation are separated, but later telemetry return is only generic. | Add specific official record, replay, or statistics return condition. |
| Generated graph-to-text narrative | `EventMechanismSupport` | `2` | The draft states “A caused B”, while the source graph establishes only that A preceded B. | Return to `NSTD.3` or `NSTD.7`: remove the unsupported cause or obtain the needed causal account. |



#### NSTD.6:5.2 - An existing product and an unknown manufacturing history


An editor receives a handout narrative with a declared onboarding use, qualified subject basis and source-return links, but no manufacturing or repair journal. The editor reconstructs the needed source relations from the intended work and subject sources, follows their use through the present explanation and exercises, and tests a meaningful changed case. A missing return or a false relation is a current-product defect. No journal is needed to identify or repair it, and a strong present boundary test can support a high product value without inventing an earlier repair.

If the same editor is instead asked whether the handout faithfully transforms a named seminar, the seminar and handout must be compared. If asked whether the author performed a prescribed review or made a particular correction, evidence of that action is also needed. Current fidelity or a successful reader attempt cannot answer that historical question. A generated candidate receives the same current-product evaluation; its acceptance or production-history claims remain separate questions.



#### NSTD.6:5.3 - Before and after evaluation repair


Before evaluation statement:

> The narrative is strong because readers liked it and remembered the main point.

Failure: engagement and memory are treated as total quality. Source recovery, relation strength, owner routing, and use boundary are absent.

After evaluation statement:

> For the declared onboarding use, the illustrative recovery result is that learners can reconstruct the pattern-use route; a numerical amount needs a specified relation set, conditions and evidence. Source-return readiness receives value `3` because two slogans lack pattern-body refs, and engagement boundary receives value `4` because the constructed failure story gives learners a reason to compare load conditions and preserves the conditions needed for that comparison. The first repair is to add source-return refs for the slogans before changing style.

Now `E.23` has a concrete changed slice: add two source-return refs and re-evaluate source-return readiness. Revisit the amount only if the changed access or explanation can change structural recovery. An earlier amount label is reusable only through its recoverable selection, scale, conditions and evidence; an unsupported `4` does not become `4/5`.



#### NSTD.6:5.4 - Adjacent-value calibration


For structural-amount calibration, fix five relations in a narrative about reusing a review after a display change: reuse requires the same claims, the same question, and the same qualification window; an unavailable required argument stops the new check and returns it to the source; that stop preserves unrelated review results. This adapts C.37.CF's content example. The condition, stop and source return form one compound unit at this declared grain. Hold the reader, case facts, material, operations, help and budget constant. The counts below illustrate nested constructed recovery sets, not three observed trials or a universal five-point rubric. Another selected set uses its own count or denominator without conversion to five labels.

| Correctly recovered units | Selected set size | Meaning at the fixed conditions |
| --- | --- | --- |
| `3` | `5` | `3/5`: the three reuse conditions are correctly recovered. |
| `4` | `5` | `4/5`: those same conditions plus the required-argument stop and return are correctly recovered. |
| `5` | `5` | `5/5`: those four units plus preservation of unrelated results are correctly recovered. |

The other characteristics use their own ordinal quality meanings:

| Characteristic | `3` means | `4` means | `5` means |
| --- | --- | --- | --- |
| `OrderingRecoverability` | Order is named, but wrong reconstruction remains likely. | The intended order and relations needed for use are recoverable; consequential losses are clear. | Conflicting order layers are handled and tested. |
| `EventMechanismSupport` | Events are coherent, but support strength is partly inferred from wording. | Relation strength and reconstruction target are explicit. | A wording or viewpoint change does not change recovered support strength. |
| `ViewpointAgencyDiscipline` | Viewpoint is useful, but agency or responsibility repair is incomplete. | Viewpoint function and the source of a consequential attribution are recoverable. | Reader can remove or swap viewpoint without losing source structure. |
| `EngagementBoundedness` | Interest exists, but a needed source relation or condition for informed choice is missing. | Interest supports the declared use while preserving the needed relations and conditions. | A more engaging variant improves attention without lowering source recovery, with the comparison supported under the stated conditions. |
| `SourceStructureSelectionFit` | Selected content partly serves the purpose, but a needed relation is omitted. | Selected relations support the intended use and meaningful omissions are recoverable. | A relevant changed case confirms the selection's stated reach and limits. |
| `LearningRouteReconstructionFit` | Learners can retell the route but not reliably reconstruct source relations. | Learners reconstruct source spine and source-return boundaries. | Learners transfer the route to a new case and identify the correct neighboring owner. |



#### NSTD.6:5.5 - Evaluation-to-improvement repair input without process theatre


`NSTD.6` returns an evaluation of the narrative. For repeated improvement, the following compact input can make the object, intended change and comparison recoverable:

```text
NarrativeRenderingImprovementLoopInput@Context:
  objectVersionRef: narrative rendering version, including a candidate
  evaluationResultRefs: selected `NSTD.6` rows
  improvementAim: raise one declared value without lowering protected trade-offs
  allowedChangedSlice: wording, source-return link, ordering marker, viewpoint repair, engagement device, generated source plan, or learning task
  protectedTradeoffSet: source fidelity, owner routing, engagement, cost, reader burden
  expectedReEvaluationForm: rerun the affected `NSTD.6` rows and any neighbor owner checks
```

Regeneration can supply a candidate change when the compared versions, relevant changes, protected qualities and re-evaluation remain recoverable. Adding a source-return link and an analogy-stop task is another possible repair. `E.23` compares the changed result under the selected evaluation; a more engaging draft alone does not establish improvement.



#### NSTD.6:5.6 - FPF owner teaching


`C.2.8` governs structural amount for architecture and non-architecture narratives alike. `NSTD.6` applies it to the narrative and the selected observer/use conditions. `C.33` retains the separate architecture-description adequacy question. Source-selection fit, source-return readiness, effort and usefulness remain separately judged; a story need not be an architecture description for its structural amount to be compared.

Pass case: an FPF seminar handout narrates how a practitioner moves from problem frame to forces to solution and checks. It names FPF pattern source sections, ordering rule, learner reconstruction task, and source-return points. Its necessary source relations are recoverable under the declared support; the other selected quality characteristics can reach `4` or `5` on their own scales. Those quality labels do not assign its structural amount.

Fail despite fluency: a polished architecture story says one chosen architecture "won" because it felt coherent, hides rejected candidates, omits architectural characteristics, and gives no source-return path. The needed architecture relations are missing, so the structural-use condition fails; assign an amount only when its selection and conditions are established. `OrderingRecoverability` and `SourceReturnReadiness` can fall below their own floors even if engagement is high.

Different object: an evaluator is asked whether a text generator is reliable across unseen topics. One narrative's `NSTD.6` result does not answer that question; the generator and its proposed operating range need their own evaluation. By contrast, a fluent generated story with an unknown source is still a narrative candidate: visible defects can be diagnosed, while source fidelity and structural amount remain unassigned where their required basis is unavailable.

### NSTD.6:6 - Bias-Annotation

This pattern blocks proxy-as-quality drift: readability, fluency, liking, engagement, expert approval, or generated-text benchmark value replaces object-kind fit and declared-use rendering quality. It also blocks the opposite drift where a test program is treated as the characteristic itself. Repair by selecting the evaluated object kind, scales, value meanings, evidence basis, missingness and lowering rules, floor, result rows, and repair actions. Scope: DPF-local for evaluating narrative rendering versions; it does not govern evidence, assurance, gate, decision, or publication authority.

### NSTD.6:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD6-1` | Evaluated object kind, declared use, and object-kind fit rule are explicit. |
| `CC-NSTD6-2` | At least three discriminating cases are present: pass, below-floor, and wrong-kind. |
| `CC-NSTD6-3` | Each characteristic has a declared qualitative comparison or a bound scale. Structural-amount values preserve their tuple, selection, conditions, granularity and evidence kind; generic quality labels do not substitute. |
| `CC-NSTD6-4` | Value meanings, evidence basis, missingness rules, floor, exceptional meaning, and stop or reopen condition are declared. |
| `CC-NSTD6-5` | Result rows include value, evidence basis, lowering reason, repair action, owner, and reopen condition. |
| `CC-NSTD6-6` | Measurement, eval program, evidence, assurance, gate, decision, publication, and pattern-quality claims route to owners. |
| `CC-NSTD6-7` | If repeated improvement is claimed, the `E.22` or `E.23` input names object version, `NSTD.6` as evaluation, improvement aim, protected trade-offs, allowed change slice, cost and risk account, and expected re-evaluation form. |
| `CC-NSTD6-8` | No quality movement is claimed until the changed narrative rendering version or declared changed slice is re-evaluated by `NSTD.6` or a declared stronger evaluation. |
| `CC-NSTD6-9` | Current-product reconstruction, source-to-result fidelity and evidence of actual construction or repair remain distinct; absence of manufacturing history neither defeats a supported product judgement nor licenses an unsupported historical or admission claim. |

### NSTD.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Fluency benchmark value as quality | Smoothness replaces structure recovery. | Inspect the selected relations and evidence. Return a missing basis or repair a demonstrated loss through `NSTD.1` through `NSTD.3`; fluency alone establishes neither a high nor a low amount. |
| Style repair as precision repair | A nicer wording pass is treated as sufficient while relation kind, quality sense, language-state threshold, or coarsening loss remains hidden. | Lower `LanguageStatePrecisionAndCoarseningFit` for the unresolved defect. Clarify it directly when its meaning is determined, or use the relevant precision, coarsening, explanation or language-state pattern for the remaining question. Re-evaluate the repaired rendering before claiming improvement. |
| Prompt loop as improvement | The worker keeps regenerating more engaging drafts without a named object version, allowed change slice, protected trade-offs, or re-evaluation. | Open `E.22` when needed, route the repair to `E.23`, and re-evaluate the changed version through `NSTD.6`; otherwise retain it as a candidate without claiming improvement. |
| Overextending a quality result | A narrative-quality result is taken to establish a wider evidence, assurance or gate claim without that claim's grounds. | Keep the narrative-quality result at its supported scope and obtain the grounds required by the wider use. Use `A.10` for an implicit or needed replayable source-to-use account, `B.3` for an actual named assurance claim, and the gate's governing pattern for its decision. |
| Evaluating a different object | A judgement about one narrative is used to rate its generator, source archive or whole course. | Select the evaluation for that object. A script or generated draft can still be assessed as a narrative when it expresses one. |
| Reconstructed history as evidence | A plausible route inferred from a good product is reported as the author's actual construction or repair. | Retain the current-product result and mark the historical claim unestablished until its own evidence is obtained. |
| Characteristics as eval programs | Test scripts or automated checks are treated as characteristics. | Keep characteristics in `A.19.ECS`; automated evals are measurement or eval-program carriers under direct owners. |

### NSTD.6:9 - Consequences

The benefit is a usable improvement target: `E.23` can improve narrative versions because values, floors, evidence, and repairs are declared. The cost is heavier evaluation before reliance-bearing use.

### NSTD.6:10 - Rationale

`A.19.ECS` says improvement cannot be better than its evaluation. `NSTD.6` specializes that lesson for narrative renderings: first recover object kind and use, then choose characteristics that discriminate narrative rendering quality for that declared use.

### NSTD.6:11 - SoTA-Echoing

FPF `A.19.ECS` and `C.16` supply the evaluation and measurement distinctions. `C.2.8` supplies reader-relative structural amount and its qualified formal epiplexity specialization; `C.33` concerns architecture-description adequacy. Amount, extraction effort, learning and task usefulness can change independently. Language-state, coarsening and explanation patterns support the particular repairs named in the scale; they are not extra tests triggered by every stylistic change.

Castricato et al.'s [model-theoretic account](https://aclanthology.org/2021.nuse-1.10/) distinguishes narrator-to-reader information and evolving story models. Mengelkamp et al.'s [reading-goal experiments](https://doi.org/10.1002/acp.70036) found condition-dependent comprehension effects and persistent overestimation. Georgiou et al.'s [narrative-memory study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11852912/) separates recall, recognition and reconstruction of order. These results support asking what a reader actually recovered, separately from fluency, confidence or enjoyment; they do not validate the DPF's ordinal scale.

The competing shortcut is to rate a narrative by fluency or engagement alone. A fluent account that turns temporal precedence into cause demonstrates why that shortcut fails for a causal explanation. This pattern therefore evaluates the selected relations and the intended use separately from engagement, accepting the cost of a focused source comparison or reader task when it can change the judgement. For an expressive use without that causal claim, do not invent the same obligation.

Ma et al.'s [story-generation survey](https://aclanthology.org/2026.eacl-srw.39/) identifies continuing coherence, consistency, diversity, control and evaluation problems. Rahman et al.'s [G-KMS](https://www.mdpi.com/2079-8954/14/2/175) adds structured, semantic and engine-execution checks for its RPG setting. Select these checks for the claim being assessed: an observable continuity defect can be judged from the product, while a claim about reader experience needs an appropriate reader basis. Neither source makes a human study a prerequisite for inspecting an ordinary draft.

### NSTD.6:12 - Relations

Uses `A.19.ECS`, `A.17`, `A.18`, `C.2.8`, `C.16`, `C.16.Q`, `C.2.LS`, `A.16.1`, `A.16.2`, `A.6.3.CSC`, `E.17.EFP`, `E.10`, `A.6.P`, `C.33`, `E.22`, `E.23`, `B.4`, `A.10`, `B.3`, `E.17`, `C.35`, and `G.11`. `C.2.8` defines structural amount for all admitted source domains; `C.33` is used when architecture-description adequacy is current. `E.23` consumes `NSTD.6` result rows only after object version, allowed change slice, protected trade-offs, cost and risk, and re-evaluation form are explicit. `B.4` is used only for an evolution claim over a narrative episteme, learning route, or other holon under repeated use; `G.11` handles currentness and refresh. Reopen when evaluated object kind, declared use, source pack, characteristic set, language-state profile, cue or backoff status, coarsening or explanation relation, precision-restoration result, epiplexity basis, value meanings, floor, evidence basis, allowed improvement slice, or low-value repair route changes. Support-map entry: open `Architecture and Narrative Work Bridge` when `NarrativeRenderingEpiplexity` is architecture-relevant or tied to `C.33`; open `Semiotic And Language-Precision Bridge` for language-state, coarsening, explanation, relation, or quality-word repairs; open `Source Use And Refresh Map` when evidence basis or source-currentness supports a value; open `NSTD.Reference:11 — Working meanings and direct source returns` when a characteristic name risks becoming a new ontology.

### NSTD.6:End
