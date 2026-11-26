## NSTD.7 - Automated Narrativization and Story Planning

> **Status:** Stable

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** planning, generating and inspecting a narrative produced with a tool, so that its content and form serve the intended use.

### NSTD.7:1 - Problem frame

Use this method to generate, inspect or repair a narrative with an LLM, an NLG system, graph-to-text or data-to-text generation, story planning, a schema or search. An existing tool-produced account can itself be the object of evaluation.

Establish the reader’s task and what has been commissioned of you. To generate an account, give the tool the subject material and constraints that bear on that task. To inspect an existing account, compare what it offers with the intended use and applicable sources. A finding can complete an inspection. If the commission is to design a procedure for later accounts, establish what it must do when the source varies and which choices its users retain.

Fluent or schema-valid output can introduce a cause the source never established, drop a condition or break continuity.

A focused comparison can locate such a loss and guide a correction while retaining the speed of automated drafting.

### NSTD.7:2 - Problem

Automated systems can produce fluent narratives that lose a source relation or violate a story constraint. A plan helps control generation, while inspection tests the actual result. Either can reveal a need to revise the other.

### NSTD.7:3 - Forces

| Force | Tension |
| --- | --- |
| Fast drafting vs source comparison | Generation is fast; finding a consequential omission or invention still requires comparison with the needed content. |
| Schema constraints and fidelity | Correct field structure establishes format compliance. Inspect the values and relations to establish fidelity. |
| Fluency and correspondence | A smooth transition can turn succession into an unsupported explanation. |
| Automation and responsibility | A consequential use may require an authorized decision. Identify who holds that authority and, when relevant, who implemented the decision. |

### NSTD.7:4 - Solution

For a new narrative, establish the result the recipient commissioned. For an existing narrative, start with the use you are asked to assess today. Its earlier commission matters when the question is whether the author fulfilled that commission. For a subject explanation, recover the intended reader’s question from the applicable brief and authorized changes before consulting the generator’s outline or an earlier verdict. What must the reader be able to explain or decide, and across which cases? Use the subject practice and EXD.Reference:3 to obtain the claims, grounds and conditions that answer that question. Keep a sufficient existing explanation. A draft can also help discover an argument. Check that argument against the question and sources before letting it organize the account.

Read the finished narrative with the preparation, references and help its audience actually has. Follow its reasoning across passages to the point of use. Which connection does the text supply? Which is available in time from a stated prerequisite? Which did you add as a reviewer? Compare this account with the original task independently of the author's choice of episodes. When the job crosses kinds of holons, their composition scales or levels of model abstraction, identify the relationship that warrants each consequential passage between them. For example, describing every part separately can still leave their joint behaviour unexplained. A case can also contain the argument for the whole commissioned range. If a required connection is missing, return to the subject account. If the assignment supplies the answer to a choice the learner was to make, revise that assignment. If the connection is present but arrives too late, change its placement or the route to it.

For an open story the author can choose the purpose within the brief. For a commission just to express a given graph, accurate recovery of its requested relations can complete the job. If asked to design the selection or generation procedure, establish what its users must receive and what they can supply. Ask whether the proposed procedure would treat alike inputs for which its users need different answers. Use that difference, or a rule already covering the range, to decide what the procedure must preserve and what it may leave to the writer or generator. Give its users the procedure and grounds for its promised range. A suitable generated passage can itself complete a commission for that passage. Use the note below when later work needs the generation choices.

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
  findingUseDecisionOrRepair:
  consequentialUseDecisionMaker?:
  architectureSynthesisAssessmentRef?:
  additionalClaimGrounds?:
  revisitCondition?:
```

Use the contribution that settles the remaining question.

| Question | Applicable content |
| --- | --- |
| Source selection and an evidence claim | Use `NSTD.1` for ordinary source selection, or `G.2` to collect and synthesize the relevant SoTA traditions. Support an evidence claim from its subject sources. Use `A.10` if the source-to-use relation is implicit or must remain reproducible. |
| Generated content is to inform architecture work | `C.35` evaluates the generated contribution for that use. |
| Source-to-narrative relation | `A.6.3.NAR` and this DPF |
| Reader recovery of selected structure | `C.2.8` through `NSTD.6`; `C.33` separately when architecture-description adequacy is the question. |
| Correspondence between structures | Compare the pertinent source and result directly. Use `C.34` to evaluate an architecture-specific preservation claim. |
| Generation procedure | Establish which method was specified or used, from its description, source material or evidence of execution as the claim requires. |
| Narrative quality for a reader and use | Use `NSTD.6` and its applicable `A.19.ECS` evaluation or `C.16` measurement basis. |
| Repeated quality improvement | `E.22` when the quality question is not framed, then `E.23` using `NSTD.6` result rows and re-evaluation |
| Evidence | Use the subject criterion and relevant sources. Use `A.10` for a source-to-use relation that is implicit or must be reproducible. |
| Assurance | `B.3` |
| Ethics, harm, bias, affected parties | `D.1` through `D.5` |
| Responsibility for a consequential use | If the account assigns a duty, establish who owes what to whom under the governing terms. For a decision, correction or withdrawal, establish who may act and on what terms. A single provision may settle both questions. For an account of what happened, establish from evidence of that occurrence who or what performed the action. An automated change can be made by a technical system. |

For new generation, planning and drafting can be interleaved. Inspection may reveal that the content or order needs to change. A short task can combine planning in one prompt and comparison in one reading. Use separate stages or records when the tool, experiment or later work needs them.

| Operation | What to do | Typical failure |
| --- | --- | --- |
| Source selection | Select the material and relations or constraints needed for the reader's use. Keep unresolved source claims visible. | A prompt assumption is reported as an established fact. |
| Content planning | Choose what to include, omit and foreground. Revise the selection when comparison reveals a gap. | The generator silently drops a condition needed for the reader's action. |
| Discourse or sequence planning | Use `NSTD.2` to choose the order, when to disclose events and what the expression then allows a reader with the specified prior knowledge to infer. | A plausible sequence changes chronology, support for a cause, proof dependence or continuity. |
| Realization | Generate wording and viewpoint for the use. For a required voice, use NSTD.4 to choose examples or a trial treatment and compare connected passages. | Smooth prose can introduce a connection or replace the chosen voice with a different manner. |
| Inspection and evaluation | Compare what the reader can reconstruct with the commission and its subject grounds. Test fidelity when the brief asks the narrative to preserve a source. Use NSTD.6 for the required quality judgement. | An accurate account of the generator’s selection leaves a necessary relationship outside the selection. |
| Finding, use or repair | Report what inspection established. For a proposed consequential use, apply its criteria and authority. For a repair, compare the changed version with the earlier one before claiming improvement. | Regeneration alone leaves it open whether the original defect was resolved. |


For a required voice, use NSTD.4 to identify the speaker’s relation to the reader, suitable source passages or a treatment to try, the expressive choices and content to preserve, and what the speaker knows under the real or fictional conditions. Include adjoining text when the transition matters. An ordinary prompt can carry this information. Keep a separate profile when later work needs it. If the model receives only a compressed description, identify consequential features that description leaves open.

Compare a connected passage with the selected treatment through NSTD.4:4.5. A request to preserve a voice establishes the instruction. The written output can reveal a lost distinction, invented memory, inappropriate address or broken transition. For an assessment, report the finding. For a repair, revise that passage and inspect its connections with adjacent text. Retain an adequate result. Revisit the choices affected by a changed genre or source example. Use a human or automated comparison where it can supply the particular judgement required.

For schema-governed generation, check the required fields and follow the constraints across the scenes that have to fit together. An outline may permit either of two characters to carry one key. Two scenes can each fit the outline while together putting the same key in two distant locked rooms at the same moment. A continuous story needs a common history of the key. Scenes offered as alternative continuations can each use their own history. If the source already fixes its holder, the writer can use that fact directly. A schema may also specify locations, source references, branches or engine inputs. Save constraints that later maintenance needs. Use `NSTD.6` for narrative quality, subject evidence for a factual claim and `C.34` for architecture-specific structural preservation.

For LLM-assisted analysis, compare the proposed themes with the excerpts, question and serious alternative readings. Use NSTD.9 when the interpretation remains unresolved. Establish who proposed, challenged and interpreted the theme when its attribution matters. In NITA, the human researcher interprets the evidence and explains the result and its limits.

For fiction or an explicitly hypothetical real scenario, distinguish choosing events from expressing them. Use NSTD.10 if events, consequences or changes in what participants know or want still need construction. Give the generator the established premises, available choices and consequential relations. Compare its proposals with these. A new discovery or motive can lead the author to retain the premises and revise the event, or deliberately change a premise. A short scene may convey its plan. Use a graph or separate plan where it helps maintain dependencies. A plan whose relevant premises or claims are suitable can supply later narrative work.

Choose a further probe when its attainable result can answer a material question about the method, narrative or intended use at a worthwhile cost. Use an adequate existing result when available.

1. **Source perturbation.** Choose a change for which the subject grounds establish the expected effect on the recipient’s answer or its justification. To test sensitivity, change a relation the account must now express differently. To test preservation, change a detail the question permits the account to omit. In either case, compare what the generated passage now lets its reader infer. An unchanged answer can be sound with different grounds. This comparison establishes what happened under the tested conditions.
2. **Structure recovery.** Use a reader’s response to the selected task, with access and help specified. To test what can be recovered under conditions excluding the prompt, keep the prompt out of that attempt. Retain the first response and identify what help was used. If a relation is missing, examine whether content, order, access or other conditions explain the loss. When earlier expert readings repeatedly missed this kind of loss, use F.19:4.5 for an actual first reading under the promised conditions. If you need to rely on the reviewer to distinguish sound explanations from plausible substitutes, use C.41.QC and establish the expected judgements independently. Test both errors when the decision depends on both. One established missed defect can already refute a guarantee to catch every such defect. A reader who reconstructs an omitted step from expertise supplies evidence about that reader.
3. **Responsibility.** Follow the claim to the party that owes the action or the party entitled to decide, correct or withdraw it. If the question is who owes someone a correction, identify the undertaking and its beneficiary. For authorization, establish the corresponding authority. A generated note can convey an existing authorization when its issuer and terms support that use. Verify the actual grant if the wording is the only apparent basis.

### NSTD.7:5 - Archetypal Grounding



#### NSTD.7:5.1 - Generated-narrative pipeline: graph-to-text case


An AI agent produces a fluent explanation from a concept graph. First establish what the recipient wants the author to produce from this graph. For a faithful verbal rendering, compare the draft with the specified graph. To teach someone to design a procedure, also establish from the original commission and subject material which choices they must learn to make. A correct rendering of the graph may supply only part of that explanation. The note below records the graph-to-text comparison when it is useful to repeat it.

```text
GeneratedNarrativeUseNote@GraphToTextTeaching:
  sourceMaterialRef: concept graph with dependency, example, counterexample and evidence links
  requiredRelationsOrConstraints: prerequisite chain, contrast pairs, evidence-return points
  generationMethodRef: LLM-assisted graph-to-text workflow
  contentPlanRef: selected nodes and relations
  discourseOrEventPlanRef: didactic dependency order with a contrast reveal
  generatedDraftRef: prose candidate
  sourceComparison: required relations compared with their sentences
  evaluationRef: relevant NSTD.6 questions and findings
  findingUseDecisionOrRepair: repair a missing prerequisite before using the dependent inference
  revisitCondition: a source graph, generator or reader finding changes in a way that affects the relied-on result
```

The following steps construct and check the teaching account.

1. For a rendering, select the specified nodes, relations and returns. For a lesson, establish which of them support the commissioned learner choice and obtain any missing grounds from the subject practice.
2. Choose the order with `NSTD.2` and generate a short draft that makes the chosen relations available.
3. Compare the draft with the graph. If it says “B occurs because A” but the graph supports only “A precedes B”, replace the causal claim or obtain the missing causal account.
4. Use `NSTD.6` to check the resulting version for its actual task. In a lesson follow the explanation into the issued exercise. Trace the learner’s grounds and identify any consequential choice already supplied by the graph, the prompt or a heading.
5. Keep the adequate result. For repeated improvement, use `E.23` with the version, changed part, protected characteristics and comparison basis.



#### NSTD.7:5.2 - Probe suite for generated narrative


| Probe | Question | Pass condition | Failure repair |
| --- | --- | --- | --- |
| Source perturbation | Which parts of the required answer, if any, must change when the source condition changes? | The answer remains warranted under the new condition. A changed relation appears where required, and a warranted common answer may stay the same. | Trace a lost distinction through the supplied source, plan and passage. Use additional grounds for a claim about what caused the output to change. |
| Structure recovery | Which selected relations can this reader reconstruct from the account under the stated conditions? | The reader correctly recovers the required relations and recognizes the omissions that matter to use. | Locate the loss. Clarify the content, add a usable return, address access or narrow the supported use as appropriate. |
| Responsibility | Does the reader need to know who owes a correction, who may authorize it, or both? | The relevant terms establish the duty, the decision authority or both as commissioned. | Recover the missing obligation or permission that matters for this use. To report that someone actually corrected the account, establish that act. |
| Schema use | Do the contents of the required fields support the commissioned narrative? | Values satisfy their own constraints and any relation required across scenes in the same history. | Locate the failure in the output or generation procedure. Use executable validation where it can test the relevant constraint. |
| Improvement evidence | Is the new variant better under the relevant `NSTD.6` characteristics? | Re-evaluation supports the claimed change without losing protected results. A sufficient one-off comparison can finish here. | Keep an unsupported variant as a candidate. Use `E.22` if the question needs framing, or `E.23` for repeated improvement. |



#### NSTD.7:5.3 - Before and after repair: generated seminar outline


Before:

> The generated outline sounds coherent and covers all important ideas, so it can be used as a DPF learning route.

Here the seminar brief asks learners to choose a source pattern and use it on an unfamiliar case. Suppose the outline explains the relevant patterns but gives each exercise the heading of the pattern to apply. The heading tells learners who see it which pattern to apply. The brief may have specified the choice, the generator may have made it, or an editor may have added it. To attribute it, examine the work that produced the heading. A learner who chose a pattern before seeing the heading may have evidence of that earlier choice.

After:

> Learners can use the named pattern to work on each case. The outline still supplies the choice they must make in their next job. Keep the explanations, then give learners another incident account, the next engineer’s question and the available records. Ask them to prepare the account that engineer needs. Make the patterns and ordinary references available. Let the learner select a pattern and use it before discussing the pattern named in the earlier exercise. NSTD.8 helps arrange that practice. NSTD.6 can assess the revised route against both parts of the brief. To report what a learner actually chose and did, use that learner’s work with the help available.



#### NSTD.7:5.4 - Generated-storycraft boundary


For a franchise continuation, compare the generated scene with the selected canon, premises and character motives. A surprising event can fit them. For a contradiction, report it, repair the event if asked, or change a premise where the project permits that choice. A source perturbation can help investigate a recurring problem with the generator. Consider the permissions relevant to private critique or publication. `NSTD.6` can evaluate the candidate for either use.





#### NSTD.7:5.5 - Calibration for generated narrative


| Illustrative condition | Consequence for use |
| --- | --- |
| Fluent output contradicts a required source relation. | Identify the conflict. Repair it for the commissioned use or report what remains unsupported. An authorized narrower use can rely on the part that is sound. |
| The source relations are expressed and a consequential reading remains ambiguous. | Report the ambiguity. For a claim about a particular reading, use the available response or a suitable new probe. Clarify the wording if the intended use requires it. |
| Inspection supports the intended use at acceptable cost. | Return or use the account under the established conditions. |
| A method improvement is claimed. | Compare versions under the same relevant conditions, including protected characteristics. Repeated or heterogeneous probes support only the generality they actually test. |




#### NSTD.7:5.6 - Inspect a generated explanation, recap, game or analysis


Content planning, realization and inspection answer different questions. Inspect which claims the generated expression conveys. Use `C.2.8` for the selected structure a particular reader can correctly recover. Use subject grounds for evidence, `A.10` for an implicit source-to-use account or one that must remain reproducible, and `B.3` for a specified assurance claim. Use `C.35` when the generated material is intended to inform architecture work. Reconsider the affected comparison when its source or the generator’s behaviour changes in a consequential way.

An LLM drafts an explanation of FPF pattern use from notes. Compare its selected relations, ordering and source returns with the notes and the applicable patterns. Use `NSTD.6` to assess the draft. If the necessary subject or reader basis is missing, leave the structural amount unassigned and report any defect that inspection does establish. To establish how it was produced, use pertinent records, version history or another qualified account of the work. If those grounds are missing, report the historical limit.

A graph-to-text system produces a match recap. The event graph, timestamps, uncertainty markers and official results can establish the documented sequence and when to refresh it. If the recap attributes a goal to a cause absent from the graph, identify the gap. Report the sequence and what remains open, or obtain evidence of the cause when the question needs it.

A game system generates a branching scene. The schema specifies its objective, location, actors, traits, constraints and available actions. Check required fields for format, the scene for continuity and the intended action for reachability in the engine when it must run. To report a player’s experience, use relevant observations. Evaluate any ethical concern under the conditions it raises.

In a NITA study, an LLM proposes themes from interview notes. The human researcher considers their own standpoint, reads excerpts, tests proposed themes against alternatives and decides what the report supports at the individual-case, cross-case or dataset level in question. Their interpretation and its limits are the result used in the report.

Use these examples to distinguish evaluation from acceptance:

| Generated account | Current evaluation or use decision | Reason |
| --- | --- | --- |
| A fluent summary with an unknown source. | Assess visible narrative defects; leave source fidelity unresolved. | The source relation cannot yet be compared. |
| A graph-to-text candidate with event IDs and a stated order. | Identify the sequence the text presents. If the source is available, compare it with the graph to establish what was preserved or lost. | The draft can be inspected before acceptance. Without adequate source evidence, leave fidelity open. |
| A schema-valid RPG scene contradicting a selected continuity constraint. | Unsuitable for that source-faithful use until repaired. | Field validity does not establish continuity. |
| An FPF seminar outline with source references and reconstruction tasks. | Evaluate its teaching route through `NSTD.8` and `NSTD.6`. | Product quality and actual learning-effect claims use different evidence. |
| A homotopy metaphor with an unstated analogy limit. | Identify the omitted formal condition. Clarify it if the account must support proof-related use. | An intuitive reading and a mathematical proof require different grounds. |


For an improvement claim, retain the versions or spans compared, the relevant `NSTD.6` results, protected qualities and material costs or risks. Keep the changed prompt or method when it bears on the comparison, a continuing workflow or a claim about how the repair was performed. A single correction can be settled by comparing the changed passage with its source. Greater fluency can coincide with less recoverable structure, a lost source return or a mistaken attribution of agency.

The source and intended use affect which plan and comparison will help.

| Source type | Content to select | Order or story plan | Mistake that changes the use | What to evaluate |
| --- | --- | --- | --- | --- |
| Knowledge graph or event graph | Select nodes, edges, event ids, uncertainty, and omissions. | Choose traversal, grouping, and return links. | Treating graph coverage as semantic truth. | Epiplexity, ordering recoverability, relation strength. |
| Architecture source pack | Select structures, candidate trade-offs, decisions, telemetry, and residual exceptions. | Use decision-memory or trade-off route. | Treating generated explanation as architecture decision or assurance. | Structural-information capture, correspondence, source return. |
| Fictional canon or source material | Select the relevant premises, character agency, continuity constraints and conditions of use. | Choose a plot and an order of disclosure suited to the story. | Assuming permission to publish from permission for private critique. | Continuity, character agency, support for the selected events and the scope of rights. |
| Teaching source material | Select what the learner needs for the promised action, including choices still theirs to make. | Arrange the reasoning, opportunities to practise and returns around that action. | A coherent outline covers the subjects while an exercise supplies the answer the learner was to design. | Whether the issued task, support and feedback let the learner do the commissioned work. |
| Interviews used in NITA | Select excerpts, tentative themes, alternative interpretations and the researcher’s standpoint. | Develop the report with traceable excerpts. | Attributing an LLM proposal to the researcher as an accepted interpretation. | The human researcher’s interpretation, the source relations and the ethical conditions. |

When applying a generation method to a new type of material, check whether the available source covers that use. For a graph-to-text claim, a particular method or study may supply grounds a general NLG survey leaves open. An engine may require executable or playability checks absent from text-generation research. If the question remains open, seek the missing evidence or state the scope the present sources support.

### NSTD.7:6 - Bias-Annotation

Inspect the relation that matters to the reader. A visible continuity error can be established directly from the candidate and canon even when its production history is unavailable. A fluent passage may still assert an unsupported cause. Choose additional checks for the particular claim and its consequences.

### NSTD.7:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD7-1` | The inspection compares what the generated account makes available with the task being assessed. Use the current recipient’s requirements for present suitability and the earlier commission for a claim about its fulfilment. For a commissioned explanation, it identifies grounds supplied by the publication or timely declared preparation, decisions left to the reader and any necessary connection the reviewer had to supply. For a rendering of specified source material it checks the required correspondence. |
| `CC-NSTD7-2` | Candidate evaluation can inform use, repair or rejection. `C.35` is selected only for a result entering architecture work. |
| `CC-NSTD7-3` | Source plan, plot or event plan, schema constraints, and generation method are named when relied on. |
| `CC-NSTD7-4` | Fluency, coherence, controllability, schema validity and planning have criteria appropriate to those properties. Claims about evidence, authorization or admission have their own grounds. |
| `CC-NSTD7-5` | For a claim about responsibility, establish who owes the stated action to whom. For a claim about permission, establish who is authorized and on what terms. One provision can support both conclusions when it assigns both. |
| `CC-NSTD7-6` | An improvement claim identifies the compared versions or changed part and is supported by `NSTD.6` re-evaluation, with relevant costs, risks and protected qualities considered. An already-scoped one-off comparison can be sufficient; `E.22` frames an unresolved improvement question and `E.23` supports repeated improvement. |

### NSTD.7:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Fluency as fidelity | A necessary source relation was omitted or changed. | Compare the source and output. Report the loss or repair it for the intended use. Use `NSTD.6` when quality for that use is in question. |
| Schema compliance as source fidelity | The story satisfies a schema but changes a required source relation or constraint. | Compare and repair the changed relation directly; use `NSTD.6` for narrative quality. `C.34` applies to architecture-specific preservation, `C.2.8` to reader-relative structural amount, and `C.33` to architecture-description adequacy. |
| Treating a statement of permission as a grant | Wording in a draft is used to authorize consequential action. | Establish the issuer, scope and terms of the decision the wording purports to convey. |
| Regeneration as improvement | Another fluent variant is treated as an improvement without a supported comparison. | Compare the candidate and previous version through `NSTD.6`, keeping needed relations and costs in view. Use `E.22` for an unresolved comparison question and `E.23` when repeated improvement is wanted. |

### NSTD.7:9 - Consequences

Automated drafting can save time while retaining a manageable comparison with the source. The work needed to inspect or repair an account depends on which loss would matter to its use. A small adequate account can be returned directly.

### NSTD.7:10 - Rationale

A plan specifies intended content and order. Comparing the resulting narrative with that plan establishes where they agree or differ. To explain the plan’s contribution to generation, examine evidence of how the tool or author used it. Inspection can settle its own question or inform acceptance or further drafting.

### NSTD.7:11 - SoTA-Echoing



#### NSTD.7:11.1 - Operational comparison against domain vocabulary


Narratology distinguishes story, discourse and presentation. Generation methods distinguish content selection, ordering and realization. Use these distinctions to locate an omission, misleading sequence, unsupported relation or consequential wording choice. A tool can combine the operations internally. Inspect the resulting account and use evidence of execution when the question concerns how the tool produced it.

Keep a domain term when it helps identify or repair the operation. If an ambiguity affects the claim or use, resolve it directly or use the FPF method for the remaining question.

Gatt and Krahmer’s [NLG survey](https://arxiv.org/abs/1703.09902) (2018) distinguishes planning from realization. Alabdulkarim, Li and Peng’s [story-generation survey](https://aclanthology.org/2021.nuse-1.8/) (2021) examines control, commonsense, characters and evaluation. Cardona Rivera, Jhala, Porteous and Young’s [narrative-planning review](https://ojs.aaai.org/index.php/ICAPS/article/view/31509) (2024) covers plan-based methods. Kumaran, Rowe, Mott and Lester’s [SceneCraft](https://ojs.aaai.org/index.php/AIIDE/article/view/27504) (2023) generates interactive scenes from instructions. Rahman, Yu and Cho’s [G-KMS](https://www.mdpi.com/2079-8954/14/2/175) (2026) tests structured generation, repair and execution in a compact Unity RPG. Ma et al.’s [survey](https://aclanthology.org/2026.eacl-srw.39/) (2026) identifies problems in coherence, character consistency, diversity, plot control and evaluation. Nguyen-Trung and Nguyen’s [NITA](https://doi.org/10.1080/14780887.2026.2638348) (2026) gives the human researcher responsibility for interpretive judgement in its qualitative-analysis method.

Use these contributions for the question they address.

- Distinguish content planning, discourse planning and realization. For final prose, inspect its source relations and order. Recover the plan when it helps explain, repair or reproduce the result. To report what happened during generation, seek evidence of that work.
- Select the characteristics the proposed use needs, such as coherence, controllability or diversity, and examine the output under those criteria.
- Use a plot or event plan to guide generation. Compare the resulting story with its goals and constraints to see how far the plan was realized.
- For a scene that must execute, check parsing, state reachability and the semantic constraints that matter in the engine.
- For technical playability, use a suitable execution test, exhaustive check of the applicable state model or existing play evidence to establish the reachable actions in question. For how a player experienced the scene, use evidence of the player’s response.
- In NITA, the human qualitative researcher interprets the tool’s tentative themes in relation to excerpts, the question and alternatives. Preserve that contribution when using NITA.

Use the comparison to decide whether the particular narrative serves the requested purpose. Keep unresolved claims within their evidenced limits.

### NSTD.7:12 - Relations

Uses `G.2`, `C.35`, `A.6.3.NAR`, `C.2.8`, `C.33`, `C.34`, `NSTD.6`, `A.19.ECS`, `C.16`, `E.22`, `E.23`, `A.10`, `B.3`, `D.1` through `D.5` and `G.11`. `C.2.8` gives the common structural amount, `C.33` architecture-description adequacy, `C.34` architecture-specific preservation and `C.35` the use of generated material in architecture work. Use `G.2` to synthesize SoTA across traditions. For an improvement comparison under `E.22` or `E.23`, identify the versions, change and relevant `NSTD.6` results. Reconsider a finding when changed material, generator, method, schema, use, evidence or research affects what it supports. See the Source Use And Refresh Map for generation and source claims, `NSTD.Reference:11` for the meaning of plan, constraint, admission, correspondence and responsibility, and the Semiotic And Language-Precision Bridge for a change of language state, coarsening, cue or evaluative wording. C.39.QR:4.1 recovers the original task independently of a proposed answer. EXD.Reference:3 supplies its subject explanation and EXD.6:4.1 tests the finished account for that use. In a lesson, NSTD.8:4.1 traces where the learner obtains and uses the needed grounds.

### NSTD.7:End
