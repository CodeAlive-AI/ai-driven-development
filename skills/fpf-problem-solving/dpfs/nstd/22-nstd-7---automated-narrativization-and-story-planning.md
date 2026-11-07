## NSTD.7 - Automated Narrativization and Story Planning

> **Status:** Stable

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** planning, generating and inspecting a narrative produced with a tool, so that its content and form serve the intended use.

### NSTD.7:1 - Problem frame

Use this pattern when LLM, NLG, graph-to-text, data-to-text, story-planning, schema-governed generation, or search is used to produce or repair narrative renderings.

First useful move: give the generator the material, the relations it should preserve and the intended reader's task. Obtain a small draft and compare it with the material for omissions, inventions and misleading connections. Evaluate those defects before deciding how to use the draft.

What goes wrong if missed: fluent wording or a valid output schema hides an unsupported cause, missing condition or continuity error.

What this buys: useful automated drafting with a way to detect and repair the losses that matter to the reader.

### NSTD.7:2 - Problem

Automated systems can produce fluent narratives that lose a source relation or violate a story constraint. A plan helps control generation, while inspection tests the actual result. Either can reveal a need to revise the other.

### NSTD.7:3 - Forces

| Force | Tension |
| --- | --- |
| Fast drafting vs source comparison | Generation is fast; finding a consequential omission or invention still requires comparison with the needed content. |
| Schema control vs source truth | A valid story schema does not prove source fidelity. |
| Fluency vs correspondence | Fluent text can lose selected structure. |
| Automation and responsibility | A workflow must identify who decides a consequential use; the generated text does not make that decision. |

### NSTD.7:4 - Solution

Work from a content plan to an inspected draft. For a short account, the plan can be a few instructions or marked source relations. Inspect a candidate before accepting, repairing or rejecting it; prior acceptance is not required to evaluate it. Use the optional note below when another worker, an experiment or a maintained workflow needs to recover those choices. Keep only the fields that serve that use.

```text
GeneratedNarrativeUseNote@Context:
  sourceMaterialRef:
  generatedDraftRef:
  intendedReaderAndUse:
  requiredRelationsOrConstraints:
  generationMethodRef?:
  contentPlanRef?:
  discourseOrEventPlanRef?:
  schemaConstraintRefs?:
  sourceComparison:
  evaluationRef?:
  useDecisionOrRepair:
  consequentialUseDecisionMaker?:
  architectureSynthesisAssessmentRef?:
  additionalClaimGrounds?:
  revisitCondition?:
```

Choose additional checks from the claim being made:

| Question | Applicable content |
| --- | --- |
| Source selection and any evidence claim | `NSTD.1` for ordinary source selection; `G.2` for SoTA harvesting and synthesis across traditions; the claim's subject grounds for evidence, with `A.10` when the source-to-use account is implicit or must remain replayable. |
| Generated result will inform architecture work | `C.35`; generation alone does not select it. |
| Source-to-narrative relation | `A.6.3.NAR` and this DPF |
| Reader recovery of selected structure | `C.2.8` through `NSTD.6`; `C.33` separately when architecture-description adequacy is the question. |
| Claimed correspondence between structures | Compare the relevant source and result directly. Use `C.34` for architecture-specific preservation claims; ordinary story continuity does not select it. |
| Generation procedure | method or method-description owner, with source-pack grounding |
| Narrative rendering quality evaluation | `NSTD.6`, `A.19.ECS`, `C.16` |
| Repeated quality improvement | `E.22` when the quality question is not framed, then `E.23` using `NSTD.6` result rows and re-evaluation |
| Evidence | The claim's defining or testing rule and adequate source basis; `A.10` when the source-to-use account is implicit or must remain replayable. |
| Assurance | `B.3` |
| Ethics, harm, bias, affected parties | `D.1` through `D.5` |
| Responsibility for a consequential use | The applicable organizational assignment or decision authority; precise Work claims use their own FPF grounds. |

The following operations describe a useful generation cycle. They can be interleaved: an inspected draft may reveal a better content selection or order. A short task can combine planning in one prompt and comparison in one reading. Separate stages or records are useful only when the task, tool or receiving use needs them.

| Operation | What to do | Typical failure |
| --- | --- | --- |
| Source selection | Select the material and relations or constraints needed for the reader's use. Keep unresolved source claims visible. | A prompt assumption is reported as an established fact. |
| Content planning | Choose what to include, omit and foreground. Revise the selection when comparison reveals a gap. | The generator silently drops a condition needed for the reader's action. |
| Discourse or sequence planning | Choose an order or reveal rule through `NSTD.2`. | Plausible prose changes chronology, causal support, proof dependency or continuity. |
| Realization | Generate wording and viewpoint suited to the use; carry a required voice through NSTD.4's examples or chosen treatment and connected-fragment comparison. | Smoothness disguises an unsupported connection or replaces the intended voice with a generic manner. |
| Inspection and evaluation | Compare the draft with its sources and constraints; use `NSTD.6` for the relevant quality questions. | A defect remains invisible because only fluency or schema validity was checked. |
| Use, repair or reject | Decide from the result and stakes. Re-evaluate changed claims before calling a revision better. | Repeated generation changes the text without resolving the original defect. |


For a required voice, provide the generator with the basis selected through NSTD.4: the speaker–reader relationship, suitable source passages or chosen trial, useful expressive observations, content to preserve, and the speaker's actual or fictional access to it. Include neighboring text where the join matters. These can fit in an ordinary prompt; a separate profile is useful only when the continuing work needs one. If a model cannot receive the samples, qualify what a compressed description leaves unresolved.

Generate a connected fragment and compare its actual expression under NSTD.4:4.5. A prompt saying “preserve my voice” or the generator's claim that it did so is not that comparison. Repair the particular loss, such as a flattened distinction, invented memory, inappropriate address or broken transition, and inspect the changed span and affected joins. Preserve adequate output. Changing a genre or source example reopens the dependent treatment; it need not restart unrelated content work. Automated or human comparison supports only its actual question and evidence; neither tool use nor an inferred voice profile creates a universal human-approval step.

For schema-governed generation, distinguish a format check from a content check. A schema can require scene fields, character roles, locations, source references, branches or game-engine inputs. Check whether those fields contain the right relations and satisfy the intended constraints. Record the constraints when later maintenance needs them; use `NSTD.6` for narrative quality and `C.34` when architecture-specific structural preservation is at issue. Neither a valid schema nor a complete note establishes factual accuracy.

For LLM-assisted analysis or theme generation, compare proposed themes with the source excerpts and serious alternative readings through NSTD.9 when the interpretive account is unresolved. The researcher decides which interpretation the report supports and explains its limitations. Generating an interpretation changes what the tool proposes, not what the underlying evidence establishes.

For generated fiction or explicitly hypothetical scenarios, distinguish choosing events from expressing them. Use NSTD.10 when the next events, their consequences or the participants' changing knowledge and purposes still need construction. Give the generator the fixed premises, available choices and currently important relations; inspect proposals against them. A generated discovery or motivation can change the story plan, but it must remain consistent with the retained premises or lead to an explicit premise revision. A short scene can carry its own plan; an event graph or separate plan is useful when its absence would make those dependencies difficult to maintain. A generated plan can become input to later narrative work once its relevant claims or premises are suitable for that use; a named admission record is not a universal prerequisite.

Select a probe when its possible result can change the generation method, repair or intended use:

1. **Source perturbation:** change one relevant constraint and compare the next output. A failure to reflect the change exposes a grounding problem. A successful probe supports that tested relation; it does not prove fidelity for every output.
2. **Structure recovery:** ask a reader to reconstruct the relations needed for the task without seeing the prompt. Retain the first answer and actual assistance. A missing relation may require content or order repair.
3. **Responsibility:** for a consequential organizational use, establish who decides and can correct or withdraw it. A tool-generated assertion of permission supplies no such assignment.

### NSTD.7:5 - Archetypal Grounding



#### NSTD.7:5.1 - Generated-narrative pipeline: graph-to-text case


An AI agent receives a concept graph and produces a polished explanation. The author compares the needed dependency and example relations with the draft, evaluates consequential losses and repairs the account. The optional record below supports repetition of that comparison.

```text
GeneratedNarrativeUseNote@GraphToTextTeaching:
  sourceMaterialRef: concept graph with dependency, example, counterexample and evidence links
  requiredRelationsOrConstraints: prerequisite chain, contrast pairs, evidence-return points
  generationMethodRef: LLM-assisted graph-to-text workflow
  contentPlanRef: selected nodes and relations
  discourseOrEventPlanRef: didactic dependency order with a contrast reveal
  generatedDraftRef: prose candidate
  sourceComparison: required relations compared with their sentences
  evaluationRef: relevant NSTD.6 questions and results
  useDecisionOrRepair: repair any missing prerequisite before the learner uses that inference
  revisitCondition: source graph, generator behavior or reader result changes
```

Pipeline steps:

1. Select the nodes, relations and returns the learner needs.
2. Choose an order through `NSTD.2`, then generate a short draft.
3. Compare the draft with the graph. If it says “B occurs because A” but the graph supports only “A precedes B”, replace the causal claim or obtain the missing causal account.
4. Use `NSTD.6` to assess the repaired version for the intended reading. The draft need not have been accepted before this assessment.
5. Keep the adequate result. For repeated improvement, use `E.23` with the version, changed part, protected characteristics and comparison basis.



#### NSTD.7:5.2 - Probe suite for generated narrative


| Probe | Question | Pass condition | Failure repair |
| --- | --- | --- | --- |
| Source perturbation | If one source relation changes, does the generated narrative change at the right place? | The affected sentence, order marker, or source-return link changes. | Recover source plan; do not rely on prompt fluency. |
| Structure recovery | Can a reader reconstruct selected source structure from the output? | Reader recovers nodes and relations needed for declared use and knows lost relations. | Add source-return markers or narrow declared use. |
| Responsibility | Who decides the consequential use and can correct it? | The applicable assignment or decision authority is recoverable. | Resolve that authority question; apply evidence or assurance checks only when those claims are made. |
| Schema use | Does the result satisfy the constraints that matter to its use? | Required fields and their semantic constraints are satisfied. | Repair the generator or result; use executable validation when it can test those constraints. |
| Improvement evidence | Is the new variant better under the relevant `NSTD.6` characteristics? | Re-evaluation supports the claimed change without losing protected results. A sufficient one-off comparison can finish here. | Keep an unsupported variant as a candidate. Use `E.22` if the question needs framing, or `E.23` for repeated improvement. |



#### NSTD.7:5.3 - Before and after repair: generated seminar outline


Before:

> The generated outline sounds coherent and covers all important ideas, so it can be used as a DPF learning route.

Failure: neither the needed source relations nor the learner's task is identified. “Covers all important ideas” has no comparison basis.

After:

> The outline selects `EntityOfConcern`, forces, solution, neighboring-pattern exits and the improvement loop, ordered by their teaching prerequisites. Compare those relations with the source and try the intended reconstruction task through `NSTD.8` and `NSTD.6`. A worked design estimate can support a provisional lesson; a claim about what learners actually recover requires a reading or teaching trial. `C.35` becomes relevant only if the generated result is being used to inform architecture work.



#### NSTD.7:5.4 - Generated-storycraft boundary


For a franchise continuation, compare the generated scene with the selected continuity, premise and character-motivation constraints. A surprising event is acceptable when those relations support it; if it relies on a contradiction, repair the event or change the stated premise. Source perturbation can test a recurring generator problem. A private critique and a publication have different permissions questions. `NSTD.6` can evaluate the candidate before either use is accepted.





#### NSTD.7:5.5 - Calibration for generated narrative


| Illustrative condition | Consequence for use |
| --- | --- |
| Fluent output contradicts a required source relation. | Repair that relation or narrow the proposed use. |
| Needed source relations are present, but a consequential reading remains ambiguous. | Use a targeted recovery probe or clarify the wording. |
| The inspected result supports the intended use at an acceptable cost. | Use it; no separate generation dossier is required. |
| A method improvement is claimed. | Compare versions under the same relevant conditions, including protected characteristics. Repeated or heterogeneous probes support only the generality they actually test. |




#### NSTD.7:5.6 - FPF owner teaching


`NSTD.7` connects content planning, realization and evaluation. A generated account has claims conveyed by a particular expression; its fluency alone does not establish those claims. Use `C.2.8` for reader recovery, the relevant subject grounds for evidence claims, and `B.3` for actual named assurance claims. Use `A.10` when a source-to-use account is implicit or must remain replayable. `C.35` is restricted to generated or discovered results intended to inform architecture work. Source changes and changed generator behavior can reopen an earlier comparison.

An LLM drafts an explanation of FPF pattern use from notes. Compare its selected relations, order and returns with those notes and the applicable pattern content. `NSTD.6` can assess the candidate immediately; if the necessary subject basis is missing, it leaves that amount unassigned while retaining independently supported defect findings. An absent generation journal does not erase visible product qualities or defects.

A graph-to-text system turns an event graph into a match recap. The event graph, source timestamp, uncertainty markers, and official-result refresh route are admitted source basis for this rendering. If the system adds causal explanations not in the graph, those claims are not admitted by graph-to-text success. Repair by lowering causal language, adding source return, or opening the evidence owner.

A game story-planning pipeline generates a branching scene. The schema may require objective, location, actors, traits, constraints, and available actions. `NSTD.7` treats those fields as method and source-plan support, not as proof of playable, coherent, or ethically acceptable narrative. Structural, semantic, executable, and human probes remain separate from fluency.

An LLM proposes themes from interview notes for qualitative narrative analysis. The generated theme list is not the researcher's interpretation by default. Human interpretive agency remains live: the researcher checks source excerpts, reflexive stance, alternative readings, and admissible use before any narrative rendering or report uses the generated material.

Use these examples to distinguish evaluation from acceptance:

| Generated account | Current evaluation or use decision | Reason |
| --- | --- | --- |
| A fluent summary with an unknown source. | Assess visible narrative defects; leave source fidelity unresolved. | The source relation cannot yet be compared. |
| A graph-to-text candidate with event IDs and a stated order. | Evaluate through `NSTD.6`, then use or repair it. | Its needed relations and losses can be inspected without prior acceptance. |
| A schema-valid RPG scene contradicting a selected continuity constraint. | Unsuitable for that source-faithful use until repaired. | Field validity does not establish continuity. |
| An FPF seminar outline with source references and reconstruction tasks. | Evaluate its teaching route through `NSTD.8` and `NSTD.6`. | Product quality and actual learning-effect claims use different evidence. |
| A homotopy metaphor with an unstated analogy limit. | Diagnose the missing condition and clarify it. | An intuitive explanation can be evaluated before it is fit for proof-related reliance. |


When claiming improvement from automated repair, retain the compared versions or changed spans, the relevant quality results, protected trade-offs, and any costs or risks that affect the claim or continuing use. Keep prompt or method changes when the comparison, continuing workflow or a claim about the repair process needs them. A one-off correction can finish with the changed passage and its source comparison. A variant can be more fluent and still worse on epiplexity, source return or agency discipline.

Pipeline variants by source type:

| Source type | Content plan | Discourse or story plan | Admission danger | Evaluation focus |
| --- | --- | --- | --- | --- |
| Knowledge graph or event graph | Select nodes, edges, event ids, uncertainty, and omissions. | Choose traversal, grouping, and return links. | Treating graph coverage as semantic truth. | Epiplexity, ordering recoverability, relation strength. |
| Architecture source pack | Select structures, candidate trade-offs, decisions, telemetry, and residual exceptions. | Use decision-memory or trade-off route. | Treating generated explanation as architecture decision or assurance. | Structural-information capture, correspondence, source return. |
| Fictional canon or source pack | Select canon constraints, premise, agency, continuity, and non-use boundary. | Use causal plot plus reveal order. | Treating private generated scene as authorized continuation. | Continuity, character agency, causal support, rights boundary. |
| Teaching source spine | Select concepts, dependencies, examples, counterexamples, tasks. | Use didactic prerequisite route with repeated anchors. | Treating generated outline as source framework. | Reconstruction tasks, learning-route quality, source-return readiness. |
| Qualitative notes or interviews | Select excerpts, themes, alternative readings, reflexive stance. | Use analysis narrative with traceable source excerpts. | Treating generated theme as researcher judgment. | Human interpretive agency, source traceability, ethical boundary. |

If a pipeline variant requires a source type not covered by the current source pack, mark the case as a source-refresh trigger rather than silently generalizing. A graph-to-text claim, for example, may require a more specific graph-to-text source than a general NLG survey. A game narrative pipeline may need executable or playability probes that a plain text-generation source does not supply.

### NSTD.7:6 - Bias-Annotation

Fluency can conceal a missing condition or invented cause. Inspect the relation that matters to the reader, rather than inferring source fidelity from style. The opposite error is to require a complete production dossier before evaluating an observable defect. Select additional checks from the claim and consequence, and keep candidate evaluation available throughout drafting.

### NSTD.7:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD7-1` | The generated account is compared with the source relations or constraints needed for its intended use. |
| `CC-NSTD7-2` | Candidate evaluation can inform use, repair or rejection. `C.35` is selected only for a result entering architecture work. |
| `CC-NSTD7-3` | Source plan, plot or event plan, schema constraints, and generation method are named when relied on. |
| `CC-NSTD7-4` | Fluency, coherence, controllability, schema compliance, and story planning do not become authority, evidence, or admission. |
| `CC-NSTD7-5` | Responsibility and permission are established when the proposed use needs them; a generated assertion does not supply that authority. |
| `CC-NSTD7-6` | An improvement claim identifies the compared versions or changed part and is supported by `NSTD.6` re-evaluation, with relevant costs, risks and protected qualities considered. An already-scoped one-off comparison can be sufficient; `E.22` frames an unresolved improvement question and `E.23` supports repeated improvement. |

### NSTD.7:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Fluency as fidelity | A needed source relation is not inspected. | Compare source and output, diagnose through `NSTD.6`, then repair or restrict the use. |
| Schema compliance as source fidelity | The story satisfies a schema but changes a required source relation or constraint. | Compare and repair the changed relation directly; use `NSTD.6` for narrative quality. `C.34` applies to architecture-specific preservation, `C.2.8` to reader-relative structural amount, and `C.33` to architecture-description adequacy. |
| Generated permission as authority | A tool's wording is taken to authorize a consequential action. | Establish the applicable assignment or decision authority independently of that wording. |
| Regeneration as improvement | Another fluent variant is treated as an improvement without a supported comparison. | Compare the candidate and previous version through `NSTD.6`, keeping needed relations and costs in view. Use `E.22` for an unresolved comparison question and `E.23` when repeated improvement is wanted. |

### NSTD.7:9 - Consequences

The benefit is automated drafting with a tractable source comparison and repair cycle. Its cost depends on the relations and consequences being checked; a small adequate account can be retained without a separate dossier.

### NSTD.7:10 - Rationale

Planning makes selected content and order available for control; inspecting the resulting narrative checks whether that control succeeded. Evaluation therefore belongs inside the generation cycle and can support a later acceptance decision.

### NSTD.7:11 - SoTA-Echoing



#### NSTD.7:11.1 - Operational comparison against domain vocabulary


Narratology distinguishes story, discourse and presentation; generation methods distinguish selected content, its order and its realization. Use these distinctions to locate a defect: omitted material, misleading sequence, unsupported relation or wording. A tool may combine these operations internally, so evaluate the output without inventing a production history.

Keep domain terms when they help select or repair the operation. Resolve an ambiguity where it changes the claim or intended use; another FPF pattern is useful only if its particular question is at issue.

Gatt and Krahmer's [NLG survey](https://arxiv.org/abs/1703.09902) (2018) distinguishes planning and realization. Alabdulkarim, Li and Peng's [story-generation survey](https://aclanthology.org/2021.nuse-1.8/) (2021) reviews controllability, commonsense, characters and evaluation limits. Cardona Rivera, Jhala, Porteous and Young's [narrative-planning review](https://ojs.aaai.org/index.php/ICAPS/article/view/31509) (2024) examines plan-based narrative methods. Kumaran, Rowe, Mott and Lester's [SceneCraft](https://ojs.aaai.org/index.php/AIIDE/article/view/27504) (2023) generates interactive scenes from author instructions; Rahman, Yu and Cho's [G-KMS](https://www.mdpi.com/2079-8954/14/2/175) (2026) tests structured generation, repair and execution in a compact Unity RPG setting. Ma et al.'s [survey](https://aclanthology.org/2026.eacl-srw.39/) (2026) identifies continuing coherence, consistency, diversity, control and evaluation problems. Nguyen-Trung and Nguyen's [NITA](https://doi.org/10.1080/14780887.2026.2638348) (2026) assigns interpretive judgement to the researcher in its qualitative-analysis method. These contributions support different operations and conditions, not one compulsory workflow for every narrative.

Operational payload:

- From NLG, keep content planning, discourse planning, and realization separate. If a tool returns only final prose, inspect its source relation and ordering; reconstruct a plan when it helps repair or reproduce the result. A present-product judgement does not establish the tool's hidden production history.
- Story-generation surveys motivate testing the characteristics that matter to the output's use, including coherence, control or diversity. Their findings do not create a universal admission form.
- A plot or event plan guides generation. Compare the realized story with its intended goals and constraints rather than infer success from the plan.
- For an output that must execute in an engine, inspect parsing, state reachability and relevant semantic constraints. A successful schema check alone leaves other narrative qualities untested.
- From interactive game generation, executable or playability probes may be needed when the narrative must function inside an engine or workflow; text fluency alone is the wrong evidence.
- In the NITA method, the qualitative researcher interprets proposed themes in relation to excerpts, questions and alternatives. Preserve that responsibility when using this method; it is not a claim that all automated narratives require a human interpreter.

The practical consequence is to preserve the speed of automated drafting while examining the particular relations, constraints and outcomes on which the receiving use depends.

### NSTD.7:12 - Relations

Uses `G.2`, `C.35`, `A.6.3.NAR`, `C.2.8` for structural amount, `C.33` for architecture-description adequacy, `C.34`, `NSTD.6`, `A.19.ECS`, `C.16`, `E.22`, `E.23`, `A.10`, `B.3`, `D.1` through `D.5`, and `G.11`. `E.22`/`E.23` use the evaluated version, changed part and relevant `NSTD.6` results; a retry is an improvement only when comparison supports that conclusion. `C.35` applies when the result informs architecture work; `C.34` to architecture-specific preservation; `G.2` to SoTA harvesting and synthesis across traditions. Reopen when the selected material, generator, method, schema, intended use, evaluation result or relevant research changes. Support-map entry: open `Source Use And Refresh Map` when generation, NLG, story-planning, schema, or source-pack claims are relied on; open `NSTD.Reference:11 — Working meanings and direct source returns` when generated source plan, plot plan, schema constraint, admission, correspondence, or responsibility words blur object kinds; open `Semiotic And Language-Precision Bridge` when prompt output changes language state, coarsening, cue, or quality wording.

### NSTD.7:End
