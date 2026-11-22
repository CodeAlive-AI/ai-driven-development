## NSTD.6 - Declared-Use Narrative Rendering Quality Evaluation

> **Status:** Stable

> **Type:** DPF evaluation pattern body

> **Primary EntityOfConcern:** `NarrativeRenderingQualityEvaluationCharacteristicSpace@Context`, the characteristics, scales and evidence used to evaluate a narrative rendering for a specified use.

### NSTD.6:1 - Problem frame

Use this pattern to assess a version of a narrative for a particular reader or listener and use. An editor can inspect an existing handout or an unaccepted draft. Decide whether the question concerns the present product, its fidelity to a specified source, or what the author did to produce or repair it.

The evaluated object, `NarrativeRenderingVersion@Context`, is an identifiable version of a narrative account as expressed for a reader. A script, a slide sequence or a generated draft may contain one. Identify the account within a collection or teaching programme. An unknown source or a defect can itself be an evaluation finding. Assess the authority of the collection, the reliability of its generator or the quality of the entire programme under the criteria for that object.

Identify the version, its reader and the work the account should support. Select the relations and characteristics needed for that work. Check that the criteria distinguish an adequate account from a deficient one and refer a question about another object to the appropriate evaluation.

A technical narrative can be easy to read and still turn precedence into cause or omit the condition under which a reader must consult the source.

A repeatable evaluation identifies the grounds for each judgement. Use it in `E.23` when the task includes improving the narrative.

Select the characteristics below for the use in question. They cover source selection, structural recovery, order, time and roles, source return and engagement. Examine evidence, assurance, ethics, publication authority or historical work when the corresponding claim is at stake.

### NSTD.6:2 - Problem

A fluent narrative can misstate a relation. An accurate one can leave learners unable to follow it. To judge a version for its use, specify the object, characteristics, scales, evidence, treatment of missing information and thresholds. Show what supports each value, what an exceptional result would establish and what could repair a consequential deficiency.

### NSTD.6:3 - Forces

| Force | Tension |
| --- | --- |
| Fluency and structural recovery | A reader can follow the prose while missing a relation needed for the task. |
| Engagement and informed use | A compelling story can conceal an uncertainty that changes the reader’s choice. |
| Local use and a reusable scale | A short rubric may serve one project. To compare judgements across cases, evaluators need common value meanings and stated conditions. |
| Measurement vs evaluation | Some values may be measured through `C.16`; many are ordinal content evaluations. |
| Improvement and proxy measures | Improving a measured indicator can damage a quality the indicator omits. Track the consequential effects on those qualities as well. |

### NSTD.6:4 - Solution

Use an existing evaluation result if it answers the question for this narrative version, reader and use. If a suitable evaluation specification is available, apply it to the version. Develop or adapt a specification for any remaining question about which characteristics to judge and what evidence counts.

For explanatory technical prose, apply `F.19` to the connected text. Recover its governing message, compare it with the selected source and test the contribution of each optional contrast, caveat or extra proposition for this reader and genre. Use `F.19:4.4` for a proposed warning and `F.19:4.5` for the reading evidence the conclusion needs. This wording judgement contributes to `LanguageStatePrecisionAndCoarseningFit`.

Decide what counts as a supported answer. Compare a factual account with evidence and a literary reading with the text and serious alternatives. For a deliberately open story, the reader may need to explain why several interpretations fit. For a fictional construction or a hypothetical real scenario, inspect the premises and their consequences. If the question concerns audience experience, examine evidence of that response. Use NSTD.9 for an interpretation still needed and NSTD.10 to construct missing events. Comparing two expressions can establish fidelity. Whether the source was adequate, the new account was worth producing or the audience responded as intended requires grounds for that claim.

A faithful story can show every step of a particular run. If the author was asked to explain how to design a procedure for a range of situations, use EXD.Reference:3 and EXD.6:4.1 to see whether the finished story lets the reader produce and justify a suitable design. Several designs may be admissible. Give the story credit for the decisions and grounds its reader can recover. If a reviewer can perform the missing step, establish where the intended reader could get it in time. A relation stated in a later lesson can support a later use. An earlier task that needs it calls for an accessible source, prior preparation or an earlier explanation.

Use `NarrativeRenderingEpiplexity` to assess how much selected structure a reader can correctly extract. It specializes [FPF `C.2.8 ExtractableStructuralInformation`](../../sections/09-part-c---kernel-extension-specifications/12-c-2-8---extractablestructuralinformation-structure-this-read.md). Identify the receiving narrative episteme (the account conveyed), the particular expression conveying it and the reader or observer. Specify the source structure, correctness criterion, usable prior knowledge, operations, help, access and budget. A rendering reference can identify both account and expression when it is unambiguous. Record the conditions under the basis, scale and evidence fields below.

If naming the additional and missing relations answers the question, report them. For a count, define the units, then count the correctly recovered selected semantic relations. A fraction `n/N` needs a fixed nonempty selected set. For each unit preserve the participants, predicate, polarity, modality and conditions that change use. Count a relation once however often it is repeated or depicted. Keep its identity with the count. Two readers may each recover four of five relations while only one recovers the condition for stopping. Give any ordinal or nonnegative weight its structural meaning. Score utility separately. Use the formal mapping in `C.2.8` for a bit estimate.

State whether the basis is a conditional walkthrough, an observed reading or a formal estimate with a specified mapping. A first response under known conditions shows the recovery observed in that trial and can inform an estimate of extractability. Establish a maximum, impossibility or reliability across a class only with evidence covering that claim. For a computational amount, specify the method and model. Retain the first response, help used and source returns. A familiar relation can still be recoverable from the expression. If an expert supplies a correction from prior knowledge, attribute that correction to its source. Decide whether correctness means recovering the source’s claim or recovering a warranted relation in the subject.

To isolate the effect of expression, hold the expressed claims and the other relevant conditions constant. A substantive change can identify another episteme under `C.2.1`. Report any changed access, preparation or help with the comparison it qualifies. Report performance after a perturbation or transfer under the new conditions. Use `C.11.CRC` and `C.11` to compare effort and usefulness when relevant. A sufficient existing rendering can stay in use.

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

Identify the object before assigning a value.

| Object-kind case | Handling |
| --- | --- |
| Narrative account, whether candidate or accepted | Evaluate every characteristic whose failure would defeat the intended use. |
| Narrative rendering below a required floor | Report the supported value, the loss for this use and the smallest repair that could address it, if one is available. |
| The question concerns another object | Evaluate that object under its own criteria, such as reliability across a generator’s operating range or authenticity of a source archive. |
| The object proves to be another kind after the evaluation has begun | State the mismatch and stop assigning values to this object under the narrative criteria. |

Use these default meanings for the ordinal content-quality characteristics. Assign `NarrativeRenderingEpiplexity` its own structural amount and use condition as specified above.

| Value | Meaning |
| --- | --- |
| `0` | No usable basis for this quality judgement, or evaluation stopped before a quality value could be used. Give the cause. |
| `1` | Object is a narrative rendering but unusable for the declared use. |
| `2` | Suitable for orientation. Consult the source before relying on this account. |
| `3` | Locally usable with named limitations and repair obligations. |
| `4` | Good for the declared use. Consequential omissions are understood, with a usable return to the source where needed. |
| `5` | Strong for the declared use. The reader can trace the grounds for the conclusion throughout its stated range and recognize any limit that matters there. A single record can settle a narrowly posed question. When the claim extends to changed conditions or concerns how an account was constructed or repaired, the grounds also cover that extension or history. |

For teaching or other reliance-bearing use, the default is that every selected relation necessary for that use must be recoverable with the stated support and evidence. Specify those relations at the grain the task needs. A required distinction and its stop condition may suffice. Judge the amount recovered and the use condition separately. Unrelated relations cannot make up for a missing necessary one.

The other characteristics essential to the use have a default floor of `4` on their own scales, including `OrderingRecoverability` and `SourceReturnReadiness` when essential. When the account demonstrates a route through a constraint-governed unfolding structure, the default floor of `4` applies to recovering the route and the source constraints the declared use needs. A local, low-risk orientation use may set these quality floors to `3` if it explicitly excludes the downstream uses the result cannot support. Select the structure before evaluating a narrower use. Removing a difficult relation after seeing the answer defines a different comparison.

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
  professionalOrAuthorityRefs?:
  reopenCondition:
```

For repeated improvement, collect the relevant judgements in a result for the version and use being compared.

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

When repeated improvement is wanted, use `E.23` with `NSTD.6` as the evaluation of the narrative. Use `E.22` first if the quality question still needs framing.

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

To judge improvement, evaluate the changed version through `NSTD.6` or a declared stronger evaluation. Compare it with an applicable baseline. Claim the gain that comparison establishes under the protected conditions. Specify what the change should improve and which qualities it must protect, including for a style edit, another generation attempt or added drama. If the change affects the source set or its currency, admission of generated material, the teaching or publication medium, an ethics, evidence or assurance claim, or the evaluation criteria, identify the applicable method. Include that work in the change being assessed or commission it separately. Use `B.4` for a claim about evolution under repeated use. Under `G.11`, reconsider affected results when the source, reader observations, teaching evidence, generation practice or FPF edition changes enough to alter reliance. Reuse sufficient unaffected results.

Before assigning values, recover the source and use basis for the question being answered.

For current-product quality, derive the necessary structure from the work readers need to do, their prerequisites and qualified subject sources. Use the account to refine that selection and inspect what it conveys, hides or loses. Point to the relevant source and rendering passages. Recover the ordering rationale, conditions for source return and any consequential event, mechanism, viewpoint, agency, engagement or learning-route relations, using `NSTD.1` through `NSTD.5` and `NSTD.8` as needed. Report this reconstruction as a present assessment with its uncertainties. Missing subject grounds, inaccessible returns and unsupported relations affect that assessment under their own criteria.

For a promised transformation, compare the named source and result against the preservation or change promised. For a claim about how the work was performed, use records or other evidence of the relevant actions. Trace the actual selection, order, mechanism, viewpoint, engagement and learning-route choices that the claim needs under `NSTD.1` through `NSTD.5` and `NSTD.8`. State which actions the evidence establishes. If the history remains unknown, give that limit to the work relying on it.

Evaluate a candidate before acceptance when its quality is in question. The result may support acceptance, repair or rejection. Use `C.35` for generated or discovered content intended to inform architecture work. Before reusing a narrative as evidence, establish the relevant subject grounds. Use `A.10` when the source-to-use account is implicit or must remain reproducible. For assurance, authority to publish or an effect on human learning, obtain evidence or authorization appropriate to that claim.

Carry out the parts of the evaluation that answer the question.

1. Identify the version and the particular account in its text, slides or other expression. Follow the narrative across as many lessons or documents as its intended use requires. Evaluate the course, source collection or generator in its own right when the question concerns such matters as learning, provenance or the reliability of subsequent outputs.
2. Select evidence for the claim. Inspect the subject and rendering for present quality, compare the named source and result for promised fidelity, or establish the claimed work from evidence of its performance. A single admissible route can show that an outcome is possible. One admissible route that misses a deadline refutes a claim that every admissible route meets it. A reader who must choose a route as conditions change needs the rule for that choice and a way to recognize when it applies. Assess that content even when the illustrated route is correct.
3. Identify the work this reader or listener needs the account for and the conditions under which the judgement holds. State limits that affect reliance on the result.
4. Evaluate every characteristic whose failure would defeat the declared use or make it unsafe. Select additional characteristics only when their result matters to the question.
5. When a value falls below its floor, identify the loss. Give the smallest repair that would address it, or specify what is still needed to find one.
6. Before claiming an improvement, re-evaluate the affected characteristics if the version or selected source basis changes.

Missingness and lowering rules:

| Missing or defect condition | Lowering rule |
| --- | --- |
| Selected structures cannot be identified from the task and subject sources | Leave the structural amount unassigned. Use `NSTD.1` to complete source selection, `NSTD.9` if the needed interpretation is missing or disputed, or `NSTD.10` if the proposed events still need construction. State any separate mismatch in the evaluated object. |
| The reader, correctness criterion or another consequential condition of comparison is unknown | Leave the amount unassigned for that scope. Return any narrower finding that the available evidence supports and examine independently answerable questions. |
| The reader needs to recover an order but the account and permitted sources leave that order ambiguous | Set `OrderingRecoverability` no higher than `2` for that use. An evident chronology can supply the order directly. |
| A missing distinction of time, viewpoint, participant or mediation changes the reading for this use | Set `TemporalPostureAndRoleFit` no higher than `2`. Use `NSTD.1` or `NSTD.4` to resolve that ambiguity. Apply the limit when the distinction matters to the interpretation. |
| A source-selection rationale or reader-use hypothesis needed for the evaluation cannot be recovered | Set `SourceStructureSelectionFit` no higher than `2` for that use and return the selection question to `NSTD.1`. Lower `TemporalPostureAndRoleFit` if its time or participant distinctions are also missing. Leave structural amount unassigned if its own selection, correctness or observer basis is unavailable. Check what can be recovered from all the pertinent material. |
| Reliance requires a return to the source and the reader lacks a way to recognize or complete it in time | Set `SourceReturnReadiness` no higher than `2` for that use. A self-contained answer can settle a question that requires no return. |
| The account presents one route as obligatory although the governing conditions allow other routes, or omits a branch, return or exit that would change the reader’s conclusion or action | Set `DemonstrativeSliceRecoverability` no higher than `2` for that use. Restore the missing choice and governing condition through `NSTD.1`, `NSTD.2` or `A.22.CGUS`. Accept an admissible route as a sufficient demonstration when the claim only requires one such route. |
| Simplification, literary wording or drama obscures a source relation, distinction of precision or limit of a coarser account needed for this use | Set `LanguageStatePrecisionAndCoarseningFit` no higher than `2`. Repair the specific loss when its meaning is known. Use `C.2.LS`, `A.6.3.CSC`, `E.17.EFP`, `E.10`, `A.6.P` or `C.16.Q` for a remaining question of language state, coarsening, explanation or precision, then reassess the affected characteristic. |
| Only an intended effect or seed is available, without an identifiable narrative account | No narrative version is yet available for this evaluation. Develop the cue through `A.16.1`, `NSTD.1` or `NSTD.2`, or evaluate the cue for its own use. |
| Persuasion conceals an uncertainty, risk or alternative material to the reader’s choice | Set `EngagementBoundedness` no higher than `3`. Restore the relevant condition or alternative through `NSTD.5`. Use the applicable `D.1`–`D.5` contribution if a consequential value or harm question remains for an affected party. |
| A generated narrative is still a candidate | Evaluate it for the stated use. Record the basis and limits. Use `NSTD.7` when the generation method needs repair and `C.35` when the content is meant to inform architecture work. |
| A claim about evidence or assurance lacks grounds | State which claim is unsupported and recover its criterion. Use `A.10` for a source-to-use account that is implicit or must be reproducible and `B.3` for a specified assurance claim. Judge each quality under its own criterion. Leave an unsupported structural amount unassigned. |
| The present product can be assessed, but its construction or repair history is unknown | Use the available product evidence for current quality. Report the historical limit to whoever relies on that claim and apply the relevant source, use and admission criteria to their own questions. |

A defined trial in which the reader recovers none of the selected relations supports observed recovery `0` for that trial. An empty selected set has no recovery fraction. Identify the object before assigning an amount. A walkthrough can support a conditional estimate. Use an existing reading when it answers an empirical question, or consider a new trial when the obtainable evidence would justify its cost for the task.

Default narrative rendering quality characteristics:

| Characteristic | Evaluation question | Low-value repair action |
| --- | --- | --- |
| `SourceStructureSelectionFit` | Do the chosen relations support the reader’s question about the whole or parts at issue, including any interaction on which its conclusion depends? What grounds support the selection and any assumption about reader interest? | Use `NSTD.1` to recover a missing distinction or connection before changing the style, drama or generation instruction. |
| `NarrativeRenderingEpiplexity` | Which selected relations can this observer correctly extract from the account through this expression under the specified conditions? When comparing alternatives, which relations differ? | Use `C.2.8` for structural amount. Return a selection gap to `NSTD.1`. Repair a missing or false relation, its expression or a needed source return through the method for that problem. Reassess recovery if the repair changes what can be extracted. Use `C.33` for an additional question about architecture-description adequacy. |
| `OrderingRecoverability` | Can the reader recover the order the task requires and recognize any consequential change of order? | Use `NSTD.2` to clarify the relationship that was lost. Explain the author’s ordering choice when the reader needs its rationale. |
| `DemonstrativeSliceRecoverability` | Can the reader identify which route the account shows, why the source permits it, and which other possibilities matter for the intended inference or decision? | Use `NSTD.1`, `NSTD.2` or the source method to recover a constraint, alternative, loop or exit whose omission changes that use. |
| `TemporalPostureAndRoleFit` | Can the reader distinguish the relevant time, mediation, participants and viewpoints? | Use `NSTD.1` or `NSTD.4` to clarify observation, live reporting, proposal or fiction and who is speaking or acting. Obtain work-role, performer/assignment or architecture-admission evidence when the corresponding claim needs it. |
| `EventMechanismSupport` | Can the reader reconstruct events, mechanisms, dependencies, or state changes when required? | Reopen `NSTD.3`; add mechanism support or lower causal language. |
| `ViewpointAgencyDiscipline` | Does the viewpoint convey the source relation and accurately attribute action, capability, responsibility and permission? | Use `NSTD.4` to distinguish the protagonist or actant from whoever acted, held a role or a permission, or bore the relevant responsibility. Examine the ethical question when it arises. |
| `EngagementBoundedness` | Does engagement serve the intended effect while preserving source relations and the conditions needed for the reader's choice? | Reopen `NSTD.5`; restore the missing condition, revise the device or keep a sufficient simpler account. |
| `LanguageStatePrecisionAndCoarseningFit` | Does the chosen language state make the needed relations, precision and coarsening limits recoverable for this use? In explanatory technical prose, what does each optional rhetorical branch contribute to the intended reader? | Apply the connected `F.19` reading to explanatory technical prose, retaining the distinctions that change its use. For a remaining question, use `C.2.LS` for a threshold-bearing language-state profile, `A.6.3.CSC` for narrowed-use coarsening, `E.17.EFP` for explanation-facing retelling, `A.16.1`/`A.16.2` for cue or backoff, and `E.10`, `A.6.P` or `C.16.Q` for precision restoration. |
| `EthicsEvidenceAssuranceRouting` | For a consequential claim about value, harm, evidence, assurance or policy, are the grounds and limits available for this use? | Identify the unresolved issue and use the pertinent `D.1`–`D.5`, `A.10`, `B.3` or professional contribution. |
| `MediumAndPublicationFit` | Does the carrier fit the reader and use without changing the claim? | Route publication or audience-unit questions to `E.17`, `E.17.AUD`, or `NSTD.8`. |
| `SourceReturnReadiness` | Does the narrative tell readers when and where to return to the source basis or relevant method? | Add the missing return condition or destination, or narrow the supported use. |
| `LearningRouteReconstructionFit` | Can the learner reconstruct the needed relations and perform the action assigned to them, including a choice of their own when the task calls for one? | Use `NSTD.8` to repair a missing relation, a premature solution or a task that omits the learner’s decision. Inspect the materials for a design judgement and the learner’s response for a performance judgement. |

Use `LearningRouteReconstructionFit` for the learner action the narrative promises. For reconstruction, establish whether the account supports the required links and any necessary return to source. For a decision using that route, include the differences the learner must recognize and the choice they must make. If independent design is promised, identify the organizing relation, criterion or check the learner must choose. If the commission also asks for the grounds, give the learner a way to develop and express them. Inspect the material, including its prompts, for a judgement about the design. Credit a learner with a choice from their own work under the help available to them. The separate count of correctly recovered relations retains its stated denominator.

### NSTD.6:5 - Archetypal Grounding



#### NSTD.6:5.1 - Value bank: full result rows


Each row evaluates an identifiable account for a particular use. Earlier acceptance is unnecessary, and a change in use can change the judgement.

| Case | Characteristic | Value | Evidence basis | Low-value repair |
| --- | --- | --- | --- | --- |
| FPF seminar handout | `NarrativeRenderingEpiplexity` | Qualitative illustration. The numerical amount is unknown. | The case assumes that learners can recover the EntityOfConcern, forces, solution and relevant exits. Their names alone specify neither equal units nor a denominator or an observed trial. | Retain this limited finding. If transfer matters, use evidence of a learner choosing an appropriate pattern in a different situation and report it under those conditions. |
| FPF seminar handout | `SourceReturnReadiness` | `4` | Each slogan in the constructed handout links to the relevant pattern. Before applying one in a new situation the exercise directs the reader to that pattern’s conditions. This shows when and where to return. For `5`, establish that the handout and the available sources let readers recover the conditions throughout the range claimed. A changed case can answer a remaining question about that range. | Reconsider this value if a change in task, preparation or access affects the return, or if a reader cannot find or use it. Repair a confirmed failure even if the source text is unchanged. |
| FPF seminar handout | `EngagementBoundedness` | `4` | This clearly fictional failure story invites readers to compare workloads and gives them the relevant conditions. The value is a judgement about the design. | If increased attention is claimed, use an appropriate observed comparison. Restore any condition the persuasive use conceals. |
| Incomplete version of a homotopy lesson | `LanguageStatePrecisionAndCoarseningFit` | `3` | The vivid analogy leaves readers to infer which continuous deformations are allowed and when to consult the formal account. | Name the restriction on crossing the missing point and ask when it matters to contraction. |
| Homotopy explanation | `OrderingRecoverability` | `4` | The explanation names its teaching order and tells readers where to recover the dependencies of the proof. | For `5` on this explanation, trace how each dependency needed for the proof becomes available when the reader must use it. If the lesson promises transfer to other problems, establish the grounds for that wider claim. |
| Franchise continuation probe | `SourceReturnReadiness` | `4` | An illustrative repair of the Readme's key case puts this return in the draft: “If a scene assumes access before Wednesday, consult the supplied premise that the character first obtains the key on Wednesday.” The condition and destination are explicit. | If the premise or proposed access changes, reopen that continuity comparison. Check an appropriate changed case when robustness across cases matters. Reconsider new use conditions if they affect the return. |
| Live commentary | `EventMechanismSupport` | `3` | The live brief calls for the confirmed change of lead and a provisional explanation. The commentator reports the order correctly and identifies loss of pace as a possibility. The listener can use the race update, while the account leaves open what supports that explanation over its rivals. | In the live account, describe the change of lead and qualify the proposed cause. Identify which later observations could distinguish that explanation from the rivals. |
| Generated graph-to-text narrative | `EventMechanismSupport` | `2` | The brief calls for a factual explanation of why B occurred. The draft presents A as its cause. The source graph establishes only that A preceded B, so the requested causal explanation is unavailable. | Return to `NSTD.3` or `NSTD.7`: remove the unsupported cause or obtain the needed causal account. |



#### NSTD.6:5.2 - An existing product and an unknown manufacturing history


An editor receives an onboarding handout with a qualified subject basis and source links. The record of its creation is missing. The editor identifies the relations needed for onboarding from the task and the subject sources, follows them through the present explanation and exercises, and tests a meaningful changed case. Inspection can establish a missing return or false relation. A strong boundary test can support a high present-product value. What the author did remains a historical question.

To assess fidelity to a particular seminar, the editor compares that seminar with the handout. To establish that the author reviewed or corrected it, the editor needs evidence of the action. A successful reader response bears on the reader’s performance. A generated draft can likewise receive a current-product evaluation before an acceptance decision or any historical investigation.



#### NSTD.6:5.3 - Before and after evaluation repair


Before evaluation statement:

> The narrative is strong because readers liked it and remembered the main point.

The judgement asserts liking and recall of the main point. It leaves open the evidence for those claims, which source relations the readers recovered, what the relations support and which uses the result permits.

After evaluation statement:

> For onboarding, assume learners can reconstruct the ordinary route for using the pattern. A numerical amount still needs a defined set of relations, conditions and evidence. Readers can use the handout for the familiar case. For the assigned new case, two slogans give no usable route to conditions that readers must consult. Source-return readiness is at most `2` for that use. Engagement boundedness is `4` because the constructed story invites comparison of workloads and preserves the conditions needed for that choice. If the task includes repair, add usable directions to those two sources first.

For an improvement under `E.23`, add those two references and compare whether readers can now locate the applicable conditions under the intended support. Revisit structural recovery if changed access or wording can affect it. Reuse a previous amount only with its selection, scale, conditions and evidence. A quality label of `4` provides no numerator or denominator.



#### NSTD.6:5.4 - Adjacent-value calibration


Fix five relations in an account of reusing a review after a change in display. The claims, the question and the qualification window must each be the same. If a required argument is unavailable, stop the new check and return to the source. This stop preserves unrelated review results. The example adapts C.37.CF. Count the condition, stop and return as one compound unit at this grain. Hold the reader, case facts, material, operations, help and budget constant. The three rows illustrate progressively larger constructed sets within this selection. For another selection, keep its own denominator and the identities of the relations.

| Correctly recovered units | Selected set size | Meaning at the fixed conditions |
| --- | --- | --- |
| `3` | `5` | `3/5`: the three reuse conditions are correctly recovered. |
| `4` | `5` | `4/5`: those same conditions plus the required-argument stop and return are correctly recovered. |
| `5` | `5` | `5/5`: those four units plus preservation of unrelated results are correctly recovered. |

The other characteristics use their own ordinal quality meanings:

| Characteristic | `3` means | `4` means | `5` means |
| --- | --- | --- | --- |
| `OrderingRecoverability` | Order is named, but wrong reconstruction remains likely. | The required order is recoverable and consequential losses are clear. | The reader can reconstruct the order and its grounds throughout the declared use, including any conflicts among event, disclosure and decision times that bear on it. |
| `EventMechanismSupport` | A consequential event connection still rests on wording alone. | The reader can recover which connections the source supports and with what strength. | The grounds for the requested connection are traceable even where the same sequence permits competing explanations. For a claim across viewpoints, the account also preserves what each can disclose. |
| `ViewpointAgencyDiscipline` | The viewpoint is useful but a consequential attribution still lacks grounds. | The viewpoint’s function and the source of the attribution are recoverable. | Across the claimed range, the reader can trace each attribution to what the participant could know, do or decide, including a change of viewpoint where one is part of the use. |
| `EngagementBoundedness` | Interest exists, but a needed source relation or condition for informed choice is missing. | Interest supports the declared use while preserving the needed relations and conditions. | The grounds show how the device sustains the intended experience while leaving the reader able to recover each consequential qualification and choice. Ground a claim about audience response in reception, and a claim of improvement in a comparison with the earlier treatment. |
| `SourceStructureSelectionFit` | Selected content partly serves the purpose, but a needed relation is omitted. | Selected relations support the intended use and meaningful omissions are recoverable. | The grounds cover the claimed range of use. A changed case can establish a use within that range, reveal a limit or refute a broader claim. Coverage of several conditions requires grounds that address those conditions. |
| `LearningRouteReconstructionFit` | The learner can retrace part of the account. A required relation, return or independently assigned choice still lacks grounds or the opportunity to use them. | The route supports the commissioned action across its required conditions, including any change or exceptional case in the brief. Reconstruction can suffice for a retelling. When the learner must choose or design, the route supplies grounds and leaves that choice for the learner. Evidence about a learner comes from their response. | The route is strong for the declared use. Its readers can trace the grounds for the assigned action and recognize where those grounds end, including under a consequential change in the presentation or conditions when that belongs to the use. Show what supports this judgement for the specified reader and task. |



#### NSTD.6:5.5 - Use an evaluation to improve a narrative


When repeated improvement is needed, use the narrative evaluation to identify the version, the intended change and the basis for comparing results. The following fields illustrate the input.

```text
NarrativeRenderingImprovementLoopInput@Context:
  objectVersionRef: narrative rendering version, including a candidate
  evaluationResultRefs: selected `NSTD.6` rows
  improvementAim: raise one declared value without lowering protected trade-offs
  allowedChangedSlice: wording, source-return link, ordering marker, viewpoint repair, engagement device, generated source plan, or learning task
  protectedTradeoffSet: source fidelity, grounds for consequential claims, engagement, cost and reader burden
  expectedReEvaluationForm: reassess the affected NSTD.6 characteristics and any changed claim governed elsewhere
```

Regeneration can produce a candidate improvement when the versions, change, protected qualities and basis for reassessment remain identifiable. Another repair might add a source link and a task about the limit of an analogy. Compare the changed result under the selected evaluation in `E.23`. Increased engagement by itself establishes only the change in engagement, when that effect has been observed.



#### NSTD.6:5.6 - Evaluate a seminar handout or an architecture story


Use `C.2.8` for structural amount in any narrative within its scope. `NSTD.6` specifies the narrative, expression, observer and use conditions. Use `C.33` when the question concerns the adequacy of an architecture description. Also assess source selection, access to the source, effort or usefulness if these affect the question.

In the seminar handout, a practitioner moves from the problem frame through forces and solution to checks. It names the source sections, explains the order, gives the learner a reconstruction task and specifies when to return to the source. Suppose the necessary relations are recoverable with the stated support. The other selected quality values may reach `4` or `5` under their own criteria. To quantify structural amount, use the structural scale.

A fluent architecture story explains that the chosen architecture felt coherent. It omits the rejected candidates, architectural characteristics and a route back to the sources. That defeats the use requiring those comparisons. Assign a structural amount only when the selection and conditions are established. High engagement can coexist with below-floor `OrderingRecoverability` or `SourceReturnReadiness`.

Reliability of a generator on unseen topics requires evidence about the generator across its stated range. A single generated narrative can still be inspected for a visible continuity error. If its source is unknown, leave fidelity and structural amount unassigned where their required basis is missing.

### NSTD.6:6 - Bias-Annotation

A reader’s enjoyment, an expert’s approval, a fluency benchmark and performance on a test each establish different things. For this narrative, state the characteristics the use requires, their scales, thresholds, evidence, treatment of missing information and implications of a deficiency. Distinguish the characteristic being judged from the procedure used to evaluate it. Evidence, assurance and authority to admit, act or publish have their own criteria.

### NSTD.6:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD6-1` | Evaluated object kind, declared use, and object-kind fit rule are explicit. |
| `CC-NSTD6-2` | When developing or qualifying a specification, demonstrate that its criteria discriminate at least three cases: adequate use, a below-floor narrative and an object of another kind. Apply a qualified specification directly when it covers the present use. |
| `CC-NSTD6-3` | Each characteristic has a declared qualitative comparison or a bound scale. Structural-amount values preserve their tuple, selection, conditions, granularity and evidence kind; generic quality labels do not substitute. |
| `CC-NSTD6-4` | Value meanings, evidence basis, missingness rules, floor, exceptional meaning, and stop or reopen condition are declared. |
| `CC-NSTD6-5` | Each row states the value or why it is unassigned and its evidence. For a deficiency, name the reason, any proposed repair and the conditions for reconsideration. Identify a responsible professional or decision holder when their contribution or authority matters. |
| `CC-NSTD6-6` | Claims about measurement, evaluation, evidence, assurance, admission, decisions, publication or pattern quality have the grounds and, where applicable, the authority their use requires. |
| `CC-NSTD6-7` | If repeated improvement is claimed, the `E.22` or `E.23` input names object version, `NSTD.6` as evaluation, improvement aim, protected trade-offs, allowed change slice, cost and risk account, and expected re-evaluation form. |
| `CC-NSTD6-8` | An improvement claim identifies a gain over an applicable baseline under the protected conditions. Evaluate the changed version or affected part through `NSTD.6` or a specified stronger evaluation on a comparable basis. |
| `CC-NSTD6-9` | Assess current quality from the product and its subject/use basis, fidelity from the source and resulting versions, and historical construction or repair from evidence of those actions. Address any admission claim under its own conditions. |

### NSTD.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Fluency benchmark value as quality | Smoothness replaces structure recovery. | Inspect the selected relations and evidence. Return a missing basis or repair a demonstrated loss through `NSTD.1` through `NSTD.3`; fluency alone establishes neither a high nor a low amount. |
| Style repair as precision repair | A nicer wording pass is treated as sufficient while relation kind, quality sense, language-state threshold, or coarsening loss remains hidden. | Lower `LanguageStatePrecisionAndCoarseningFit` for the unresolved defect. Clarify it directly when its meaning is determined, or use the relevant precision, coarsening, explanation or language-state pattern for the remaining question. Re-evaluate the repaired rendering before claiming improvement. |
| Prompt loop as improvement | The worker keeps regenerating more engaging drafts without a named object version, allowed change slice, protected trade-offs, or re-evaluation. | Open `E.22` when needed, route the repair to `E.23`, and re-evaluate the changed version through `NSTD.6`; otherwise retain it as a candidate without claiming improvement. |
| Overextending a quality result | A wider evidence, assurance or admission claim lacks its own grounds. | Use the quality result within its established scope. Use `A.10` when a source-to-use account is implicit or must be reproducible, `B.3` for a specified assurance claim and the applicable admission rule for a decision. |
| Evaluating a different object | A judgement about one narrative is used to rate its generator, source archive or whole course. | Select the evaluation for that object. A script or generated draft can still be assessed as a narrative when it expresses one. |
| Reconstructed history as evidence | A plausible route inferred from a good product is reported as the author's actual construction or repair. | Retain the current-product result and mark the historical claim unestablished until its own evidence is obtained. |
| Treating an evaluation procedure as a characteristic | A script used to obtain a value is put in the place of the property being judged. | Specify the characteristic through `A.19.ECS`. Identify the automated measurement or evaluation procedure, the conditions in which it operates and the result it supplies. |

### NSTD.6:9 - Consequences

A reader can use the result to judge the version for the declared task. When improvement is wanted, the values, floors and observed losses identify changes that `E.23` can compare. Establishing the grounds for reliance can require more time or access than a preliminary reading.

### NSTD.6:10 - Rationale

Following `A.19.ECS`, identify the object and use, then select characteristics whose values distinguish adequate from deficient use. An improvement claim can be only as informative as the evaluation on which it depends.

### NSTD.6:11 - SoTA-Echoing

FPF `A.19.ECS` and `C.16` distinguish evaluation and measurement. `C.2.8` supplies reader-relative structural amount and defines the conditions for its formal epiplexity estimate. `C.33` addresses architecture-description adequacy. Effort, learning and usefulness can vary independently of amount. Use the language-state, coarsening or explanation method for the particular repair needed.

Castricato et al.’s [model-theoretic account](https://aclanthology.org/2021.nuse-1.10/) relates the information a narrator makes available to an evolving reader model. In Mengelkamp et al.’s [reading-goal experiments](https://doi.org/10.1002/acp.70036), comprehension effects differed by condition and readers overestimated their performance. In Georgiou et al.’s [narrative-memory study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11852912/), recall after scrambled presentation could follow the original story order. Recall, recognition and reconstruction therefore warrant distinct questions. Use evidence of a reader’s task to assess what they recovered. The ordinal meanings above are this framework’s criteria.

Consider a reader judging a causal explanation. A fluent account can turn precedence into cause, so compare its causal relation with the source. If the question concerns what a reader understood, use their answer or an appropriate task when the available evidence warrants that work. For an expressive account, select the characteristics its purpose actually requires.

Ma et al.’s [story-generation survey](https://aclanthology.org/2026.eacl-srw.39/) identifies continuing challenges in coherence, consistency, diversity, control and evaluation. Rahman et al.’s [G-KMS](https://www.mdpi.com/2079-8954/14/2/175) uses structural, semantic and engine-execution checks for its RPG. Choose a check for the claim at issue. Inspect the draft for a visible continuity defect. Use appropriate evidence from a reader when the claim concerns their experience.

### NSTD.6:12 - Relations

Uses `A.19.ECS`, `A.17`, `A.18`, `C.2.8`, `C.16`, `C.16.Q`, `C.2.LS`, `A.16.1`, `A.16.2`, `A.6.3.CSC`, `E.17.EFP`, `E.10`, `A.6.P`, `C.33`, `E.22`, `E.23`, `B.4`, `A.10`, `B.3`, `E.17`, `C.35` and `G.11`. For an improvement comparison under `E.23`, identify the version, change, protected qualities, cost, risk and reassessment. Use `B.4` for evolution under repeated use and `G.11` when changed grounds affect reliance. Reconsider the affected judgement when its object, use, source, characteristics, language or precision conditions, cue, backoff, coarsening, explanation, structural basis, scale, threshold, evidence or proposed repair changes materially. The Architecture and Narrative Work Bridge relates structural recovery under `C.2.8` to the separate architecture-adequacy question under `C.33`. The Semiotic and Language-Precision Bridge covers language, expression and precision, and the Source Use and Refresh Map covers support and currency. Consult `NSTD.Reference:11` for the meanings and sources of the characteristic names. For a commissioned explanation, EXD.Reference:3 recovers the necessary subject grounds and EXD.6:4.1 compares them with the reasoning available to the reader.

### NSTD.6:End
