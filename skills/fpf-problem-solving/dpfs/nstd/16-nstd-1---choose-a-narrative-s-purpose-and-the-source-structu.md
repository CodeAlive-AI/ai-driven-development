## NSTD.1 - Choose a Narrative's Purpose and the Source Structures It Must Preserve

> **Status:** Stable

> **Type:** DPF pattern body

> **Purpose:** select from the source the events, relations and distinctions the intended reader needs.

### NSTD.1:1 - Problem frame

Use this method when you need to choose which source relations a narrative must preserve for its intended use, or to assess those choices in an existing account. A lesson, an argument, a live commentary, a fictional scene and a future scenario can require different selections.

Identify the reader’s question, locate the available material and select the relations or events it requires. Compare an existing draft with that material, or try a short account if the selection is unclear. Revise the purpose or selection where the comparison exposes a gap. A few sentences can suffice.

If the desired effect determines what the source is said to contain, a reader may remember the story but lose an important relation, mistake uncertainty for fact or lack the material needed to check a claim.

The result identifies the material that supports the account’s purpose and any claim the available material leaves open.

Use `NSTD.4` for a question about viewpoint or voice and `NSTD.7` for planning or assessing generated text. Use `C.35` when a generated result will inform architecture work. If the intended use raises a question about evidence, ethics or publication, obtain the relevant result for that question.

### NSTD.1:2 - Problem

“Make it inspiring” can be enough direction for an expressive sketch. It leaves open which relations an explanation of an architecture must preserve, which details can be simplified for a lesson, or what a reviewer must be able to check. Clarify the purpose to the degree the reader’s intended use requires.

### NSTD.1:3 - Forces

| Force | Tension |
| --- | --- |
| The reader’s use and the available material | The purpose guides selection. The material determines which subject claims the account can support. |
| Attention and authority | A motivating account may keep readers interested. A claim about evidence, assurance, ethical clearance or permission to act needs its own grounds. |
| Domain vocabulary and distinct claims | Narrative terms help design; claims about evidence, ethics or authority still need their own grounds. |
| Drafting and source comparison | A quick draft can clarify the purpose; comparing it with the source reveals omissions and unsupported connections. |

### NSTD.1:4 - Solution

Start with the reader’s question and the available material. Select what the account must preserve and examine how an existing or proposed sequence presents it. Use a short draft when it helps expose an omission or an unsupported connection. The answer can be a suitable selection, a finished account for the intended use, or a precise limit on what the material establishes.

Suppose an automatic valve is designed to open when pressure exceeds a threshold. An operator asks why it opened on one occasion. The rule explains one possible mechanism. A time-matched pressure reading and evidence that the automatic mechanism triggered the opening can establish that explanation for this event. If the only observation is an open valve, report its state and leave the cause open. Manual opening can produce the same observation.

When the reader needs an interpretation the material does not yet supply, use NSTD.9 to construct or compare accounts of the events, participants and meanings. Use an adequate diagram, chronology or interpretation directly. For fiction or a hypothetical scenario with undecided events, use NSTD.10 to develop what could happen under the selected premises. A discovered ambiguity or new possibility can change what the account needs to make available to this reader.

The optional intake below can preserve the choices needed by a collaborator, a comparison of alternatives or a maintained collection. Include the details that change that use. The examples show how the same fields can serve different tasks.

```text
NarrativePurposeIntake@Context:
  sourceBasisRefs:
  selectedSourceStructureRefs:
  unfoldingStructureRefs?:
  demonstrativeSliceRefs?:
  sourceStructureSelectionRationale:
  sourceTemporalPosture:
  renderingMediationMode: direct-source-structure | architecture-mediated | mixed
  architectureMediationRef?:
  sourceDefinitionOrConstraintRef?:
  renderingContribution?:
  narrativeVoiceOrViewpoint?:
  generatedDraftInspectionRef?:
  intendedReaderOrListener:
  readerInterestOrUseHypothesis:
  intendedReaderOrListenerUse:
  narrativePurpose:
  likelyMisreading?:
  sourceReturn:
  additionalClaimQuestion?:
  refreshCondition?:
```

Use `unfoldingStructureRefs?` when `A.22.CGUS`, `E.18.3` or a local FPF block defines a constraint-governed structure selected for this account. Use `demonstrativeSliceRefs?` for the particular path the narrative presents. The wider structure can also contain alternatives, returns and stops.

Use the following prompts where a choice remains open.

1. Identify the material and selected relations or events, explaining their relevance to the reader's purpose. State whether they concern past, live, proposed or fictional events when that changes the account.
2. If the narrative uses an architecture description, decision or observation, let the reader find the source whose structure or claim matters to that use. A direct explanation can refer straight to the subject material.
3. Identify who is writing or supplying the account and who will use it. Use `NSTD.4` for a consequential choice of voice or viewpoint and `NSTD.7` for planning or inspecting generated text. Use `A.2` or `A.2.1` for a precise system-role or assignment claim. Use A.13 and A.15.1 when the claim needs precise attribution of a dated Work occurrence.
4. Relate the purpose to the selected structure and the reader’s use. If one changes, check whether the other still fits.
5. Examine which inferences the draft invites given the reader’s likely preparation. Locate a consequential difficulty in the wording, presentation, source or evidence from a reading. A response can show which interpretation a particular reader gave. To attribute it to this passage or report independent understanding, establish what else the reader knew or used. Apply `F.19:4.4` when choosing a correction. The optional `likelyMisreading?` field can preserve the inference and its grounds for a collaborator.
6. Identify where to find an omitted relation or what still needs investigation if the reader requires a stronger conclusion.

For a difficult selection, use whichever of these questions could settle it.

| Pass | Question | Output |
| --- | --- | --- |
| Source | Which material is the account drawing on, and which relations does the reader need to recover? | Identify the material, the selected relations and when a reader will need to return to the source. |
| Use | Who will use the narrative, for what work or understanding, and which distinctions does that use require? | Name the intended reader or listener, the expected interest or purpose and the needed distinctions. |
| Mediation | Does the writer use subject material directly, an architecture description or both? Does the account concern past, live, planned or hypothetical events? | Identify the source used, its relation to the account, and the observations or later corrections needed for its claims. |
| Reliance | Which claim or feature could change what the intended reader can infer or do? | Use `F.19:4.4` for a grounded difficulty. Identify the relevant condition, source or decision and revise the wording when that is the needed remedy. |

A draft can reveal a useful selection. Check its relations against the reader’s purpose and the available sources before relying on them. If the purpose is unclear, ask what the reader needs or offer a short account that helps identify it. Qualify any broader claim about completeness or fidelity on its own grounds.

Use these contrasts when the purpose remains unclear:

- **Reconstructing a procedure.** “Help new FPF readers recognize why the EntityOfConcern, forces and neighboring-pattern exits matter in use.” This purpose identifies relations the learner should be able to reconstruct.
- **Motivating a class.** “Make the seminar inspiring so people want to use FPF” gives an expressive aim. For a reconstruction lesson, also identify what learners need to reconstruct and do with the result.
- **Explaining an argument.** To help reviewers understand a proposal, select its premises, inferences and grounds. Include an uncertainty or rival position when it affects the argument.

For fiction or a proposed real scenario, select the relevant canon, premises, design constraints or hypotheses. The narrative can develop events under those conditions. If a proposed event conflicts with a fixed condition, change the event. Change an author-controlled premise explicitly if the task permits. For a real scenario, establish the grounds for any claim that the proposed events could occur. A maintained source collection can help compare alternatives or preserve canon.

When the narrative follows one path through a constraint-governed unfolding structure, identify the wider structure and the path shown. Possible sources include `A.22.CGUS`, an `E.18.3` transformation flow, a P2S or improvement-loop block, and an ordering block under `A.6.3.NAR`. A writer can select one `DemonstrativeUnfoldingSlice@Context` of a `ConstraintGovernedUnfoldingStructure@Context`. Show omitted branches, returns, constraints or exits when the reader needs them to interpret this path or act. Identify whether the path shows an actual occurrence, an admissible possibility or a prescribed way to proceed.

These questions address common difficulties in selecting sources.

| Worker situation | Prompt | Expected answer |
| --- | --- | --- |
| Teacher or trainer | “What should learners be able to reconstruct or do, and what help may they use?” | Identify the source relations, a task that uses them and when to return to the source. |
| Architect or analyst | “Which structure, trade-off, candidate, observation or earlier decision does the account need to convey?” | Identify the subject or architecture source, what it establishes and how the narrative draws on it. |
| Scientist or researcher | “Which mechanism, calculation, attempt, source uncertainty or unresolved tension does the account concern?” | Identify the relevant calculation, proof or evidence, what remains uncertain and where a stronger claim could be checked. |
| Story designer | “Which events, character choices and constraints must hold under the selected canon or premises?” | Identify the relevant premises and any limit on publishing or reusing the result for the intended purpose. |
| Live commentator | “What was observed, what is being inferred or predicted and what can the official account later settle?” | Locate the observations in time and identify any uncertainty and subsequent correction. |
| Tool builder | "What material and relations must the output preserve, and how will a reader or operator detect a consequential omission or invention?" | A generation plan and source-comparison question under `NSTD.7`; add production-history or responsibility details when the intended use requires them. |

Mood, genre, style or an audience reaction can be a narrative aim. If fidelity or learning also matters, select the source relations the audience needs. Use `NSTD.4` or `NSTD.5` to develop the expression. An actual claim about learning needs evidence of the learner’s performance.

Examples of the optional intake for different uses:

```text
NarrativePurposeIntake@FPFLearningRoute:
  sourceBasisRefs: selected FPF pattern bodies and relation records
  selectedSourceStructureRefs: EntityOfConcern discipline; problem frame; forces; solution; neighboring exits; quality and improvement loop
  unfoldingStructureRefs: A.22.CGUS only when the lesson explicitly teaches source-to-next-use unfolding
  demonstrativeSliceRefs: first seminar route through selected pattern-use positions
  sourceStructureSelectionRationale: learners must reconstruct how a practitioner chooses and uses a pattern
  sourceTemporalPosture: prospective planned learning route over current source corpus
  renderingMediationMode: direct-source-structure unless architecture-of-FPF explanation is opened
  renderingContribution: teacher or course designer
  intendedReaderOrListener: new FPF author or reviewer
  readerInterestOrUseHypothesis: the learner wants to use an appropriate pattern for a case
  intendedReaderOrListenerUse: reconstruct one pattern-use route and apply it to a new case
  narrativePurpose: help learners locate the applicable conditions and use the source method in a case
  sourceReturn: the applicable FPF patterns and, for this teaching publication, its relation to those sources
  refreshCondition: FPF edition, learner telemetry, or route evaluation changes
```

```text
NarrativePurposeIntake@HomotopyExplanation:
  sourceBasisRefs: formal definitions, examples, diagrams, proof-status notes, and selected textbook or lecture source basis
  selectedSourceStructureRefs: definition dependency; example and counterexample relation; theorem prerequisite; formal-source return
  sourceStructureSelectionRationale: learner needs an intuitive route that preserves formal boundaries
  sourceTemporalPosture: retrospective or atemporal explanation over existing mathematical material
  renderingMediationMode: direct-source-structure unless a teaching architecture is explicitly used
  renderingContribution: teacher, explainer, or tool-assisted author
  intendedReaderOrListener: learner who must later distinguish intuition from proof
  readerInterestOrUseHypothesis: learner needs recoverable dependency order and analogy boundary
  intendedReaderOrListenerUse: use examples and return to formal statements without treating metaphor as theorem
  narrativePurpose: make abstractions followable while preserving proof-status boundary
  sourceReturn: the relevant mathematical definition, argument or qualified source for the proof
  refreshCondition: source correction, learner failure, or changed learning objective
```

```text
NarrativePurposeIntake@LiveCommentary:
  sourceBasisRefs: live observations, official event feed, telemetry, recording, later official result
  selectedSourceStructureRefs: event order; score state; possession or control changes; actor roles; uncertainty markers
  sourceStructureSelectionRationale: listener needs orientation during an unfolding event stream
  sourceTemporalPosture: live unfolding source with later refresh
  renderingMediationMode: direct-source-structure
  renderingContribution: commentator or live analyst
  narrativeVoiceOrViewpoint: live commentator voice following the unfolding event under `NSTD.4`
  intendedReaderOrListener: listener following the event and later checking the official event record
  readerInterestOrUseHypothesis: listener needs distinction between observation, inference, prediction, and official correction
  intendedReaderOrListenerUse: follow the event without treating provisional interpretation as fact
  narrativePurpose: maintain orientation and attention under uncertainty
  sourceReturn: the event observations, relevant recording or telemetry, and official source for the result
  refreshCondition: official correction, telemetry, or post-event evidence changes
```

```text
NarrativePurposeIntake@FictionalContinuationProbe:
  sourceBasisRefs: selected canon or local source pack for private storycraft test
  selectedSourceStructureRefs: canon constraints; continuity; premise and theme; character agency; causal plot support
  sourceStructureSelectionRationale: the chosen action must remain intelligible under the characters' established commitments and the consequences of earlier events
  sourceTemporalPosture: prospective fictional source structure
  renderingMediationMode: direct-source-structure unless fictional organization or technology architecture is live
  renderingContribution: story designer or tool-assisted writer
  intendedReaderOrListener: private reviewer of storycraft plan
  readerInterestOrUseHypothesis: reviewer needs to see whether continuity and agency survive the route
  intendedReaderOrListenerUse: private design critique, not publication
  narrativePurpose: develop a continuation whose choices can be compared with the selected premises
  sourceReturn: selected canon and explicit premises of the continuation
  refreshCondition: corrected source material, changed canon selection or revised premise
```



#### NSTD.1:4.1 - When claim identity matters


Use `A.6.3.NAR:4.0.1` when citation, dispute or another consequential use needs identifiable source and narrative claims. Identify source episteme X, narrative episteme Y and the construction that relates them. Preserve their common EntityOfConcern and check the correspondence on which the claimed use depends. When the two expressions use different representation languages, show how each is read and which source claims the narrative preserves under those readings. Establish publication permission, evidence or assurance when the intended claim or action requires it.

### NSTD.1:5 - Archetypal Grounding



#### NSTD.1:5.1 - Worked slice: FPF seminar from source spine to narrative route


A seminar author is asked to tell a motivating story about FPF. To develop a lesson, the author chooses what learners should be able to do: recognize a situation, select a suitable pattern and apply its conditions. The following example records the choices so a colleague can use them in teaching.

```text
NarrativePurposeIntake@FPFSeminarOrientation:
  sourceBasisRefs: selected FPF pattern bodies and relation records
  selectedSourceStructureRefs:
    - EntityOfConcern discipline
    - Problem frame and forces
    - Solution as admissible move under conditions
    - neighboring-pattern exits
    - quality and improvement loop entry
  sourceStructureSelectionRationale: the learner needs to recognize the method's applicable conditions, first operation, result and next useful move
  sourceTemporalPosture: prospective planned learning route over current FPF source corpus
  renderingMediationMode: direct-source-structure
  renderingContribution: seminar author
  intendedReaderOrListener: new FPF practitioner; team lead evaluating local adoption
  readerInterestOrUseHypothesis: reader wants a first usable route through FPF without learning every pattern first
  intendedReaderOrListenerUse: recover an appropriate pattern-use route and identify any further pattern the case needs
  narrativePurpose: connect the opening question to a use of the pattern in which the source conditions matter
  sourceReturn: selected FPF pattern body and relation record
  additionalClaimQuestion: none unless the seminar makes assurance, policy, or affected-party claims
  refreshCondition: FPF edition or selected-source pattern changes; learner reconstruction test fails
```

The opening asks learners to choose a pattern for a difficulty they recognize. The next passage explains how the pattern’s conditions, forces and neighboring exits affect that choice. The exercise returns to the selected pattern so the learner can use those conditions in a case.

To examine the lesson with `NSTD.6`, use a learner’s response to another case. Did the learner choose a pattern, explain the relevant conditions and use its body for the needed method? A response that repeats the opening question establishes which words the learner supplied. To count that as recall, check whether the words remained on display or were prompted. Applying the pattern to the new case requires the relevant conditions. If the teacher needs to explain the difficulty, examine the supplied material, the task, the learner’s preparation and the help used. Change the selection, explanation or practice when the diagnosis supports that change.

For a seminar draft produced with an LLM, specify the relevant contributions separately.

```text
renderingContribution: course-author or generator-operator role; recover the actual system, role assignment, and Work separately when those claims are made
narrativeVoiceOrViewpoint: teacher-facing explanatory voice under NSTD.4
generatedDraftInspectionRef: the NSTD.7 case that identifies the generated draft, source comparison and acceptance for its intended use; C.35 applies only when the result informs architecture work
```

The same participant may operate the tool, choose the voice and be authorized to select the result. To judge fidelity, compare the draft with the selected material or use an adequate comparison already made.



#### NSTD.1:5.2 - Worked slice: architecture-mediated narrative


An architect wants to explain a selected system structure to the team that will implement it. The architecture description and decision supply the structure, alternatives and trade-offs; the account must make the implementation-relevant choices recoverable. This is an architecture-mediated narrative.

```text
NarrativePurposeIntake@ArchitectureDecisionStory:
  sourceBasisRefs: architecture candidate set, selected architecture description, decision record, expected characteristics, known residuals
  selectedSourceStructureRefs:
    - problem situation and forces
    - candidate structures considered
    - selected structure and rejected alternatives
    - expected architecture characteristics
    - residual exceptions and developer continuation boundary
    - telemetry or later actual-structure feedback condition
  sourceTemporalPosture: prospective future holon structure before implementation
  renderingMediationMode: architecture-mediated
  architectureMediationRef: architecture description and candidate synthesis records
  intendedReaderOrListener: developer team; product steward; later evaluator
  intendedReaderOrListenerUse: understand what structure to preserve while implementing and what may be locally detailed
  narrativePurpose: carry structural intent and trade-off rationale into development work
  sourceReturn: architecture description, architecture decision record, and future telemetry route
  refreshCondition: candidate set, selected architecture, decision, or actual-structure feedback changes
```

The account is intended to let the implementers recover the selected structure and reasons for preserving or varying its parts. For an unresolved design choice, use the available architecture result or obtain the missing decision from the responsible work. Use `NSTD.6` with `C.2.8` to assess what the team could recover, or examine an observed reading for what it did recover. Use `C.33` for architecture-description adequacy, `C.34` for correspondence with the realized structure and `E.17` if the account is to be published.



#### NSTD.1:5.3 - Worked slice: franchise continuation probe


For a private critique of a continuation in a familiar space-opera setting such as `Star Wars`, select the canon, premises and continuity constraints relevant to the proposed scene. A draft can show which choices remain unsettled. A proposal to publish raises its own rights question.

The request "Write a surprising sequel that feels epic" leaves those choices open. For the private critique, the writer chooses a continuation premise that preserves a character's established motivation and the consequences of earlier events. A new event may extend the story; if it conflicts with the chosen continuity, revise the event or explain the changed premise. Ordering and suspense alone cannot repair that conflict.



#### NSTD.1:5.4 - Role-specific first moves


| Worker | First source-selection move | Common hidden overread | Repair when that difficulty occurs |
| --- | --- | --- | --- |
| Teacher | Identify the source relations and the task that calls for them. | A report of interest is treated as demonstrated learning. | Use a question or a performance that calls for the relation, with suitable existing evidence or a new observation where needed. Use `NSTD.6` for the assessment. |
| Architect | Identify the selected structure, candidates, exceptions and evidence about the actual organization. | An explanatory story is treated as an authorized architecture decision. | Check the earlier decision and its authority, or refer a new decision to its authorized owner if one is needed. |
| Scientist | Identify the mechanism, calculation or event at issue and the available evidence or proof. | A coherent story is treated as settling a scientific question. | Use the relevant source result and identify where the evidence leaves the claim open. |
| Story designer | Identify the premises, continuity and character agency that matter to this scene. | A surprise conflicts with a fixed premise. | Revise the event or explicitly change a premise the author is free to change. |
| Live commentator | Identify the observed events, provisional interpretation and available official return. | A live inference is presented as an established cause. | Name its grounds and uncertainty. Use the later official or observational source for the issue it can settle. |
| AI-agent operator | Name material, required relations and the proposed use. | Fluent prose silently adds a cause or drops a constraint. | Inspect and repair through `NSTD.7` and `NSTD.6`; apply `C.35` only for an architecture use. |



#### NSTD.1:5.5 - Match the source return to the intended use

The relevant source depends on the question. A seminar can return to the pattern’s working conditions, a mathematics lesson to definitions and proof, a match report to dated observations and later official corrections, and a fictional continuation to its premises. Reconsider the selection when the use changes. A brief orientation may become a request to investigate a cause, or a private critique may become a publication requiring permission.


### NSTD.1:6 - Bias-Annotation

Check whether the proposed account omits a material counterexample or a serious alternative. If so, revise the selection or qualify the conclusion. Document sources and roles to the degree the receiving work needs. A short explanation can use an adequate source directly.

### NSTD.1:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD1-1` | The selection serves the reader’s purpose. Where reliance on the account requires fidelity, an adequate comparison identifies what it preserves from the source. |
| `CC-NSTD1-2` | The reason for including a relation is recoverable from the reader’s intended use and the source. |
| `CC-NSTD1-3` | Past, live, proposed or fictional status and any intervening description are clear wherever they change interpretation. |
| `CC-NSTD1-4` | Writing contribution, narrative viewpoint and intended reader are distinguishable when needed. Precise system-role, assignment or dated Work claims receive their own grounds only when asserted. |
| `CC-NSTD1-5` | The intended use supplies enough direction to choose or improve the account, including an expressive aim when that is the task. |
| `CC-NSTD1-6` | A correction aimed at a plausible misleading inference has grounds and a useful consequence under `F.19:4.4`. Preserve those grounds when another use relies on them. |
| `CC-NSTD1-7` | Additional evidence, ethics, authority or production-history claims have the grounds their actual use requires. |
| `CC-NSTD1-8` | The intended reader can locate the relevant source or its qualified result when omitted distinctions or changed conditions matter. |

### NSTD.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Desired conclusion selects its own evidence | The account suppresses a relevant conflicting relation. | Compare the draft with the needed source relations and alternatives; change its selection or qualify the conclusion. |
| Unexplained selection | Neither the writer nor reader can say why a relation was included or omitted. | Recover that choice from the intended use and source; revise the selection where it fails. |
| Treating motivation as evidence | A moving narrative is taken to establish a subject claim. | Use the evidence for that claim and assess the motivational effect on its own grounds. Use `A.10` when the source-to-use connection is unclear or must remain reproducible. |
| An unstated limit changes reliance | A reader uses a chronology as a causal explanation. | State which facts establish the sequence, which causal claim remains open, and any relevant source for the stronger conclusion. |

### NSTD.1:9 - Consequences

The reader’s purpose and the source relations guide selection together. The cost lies in identifying and comparing the material that could change the account. Record further details when a collaborator or later comparison needs them.

### NSTD.1:10 - Rationale

Audience, purpose and source material jointly shape a narrative. The author can choose what to foreground and still answer to the source for factual claims. Examining the construction from source to narrative shows what was selected, related, omitted or given a new order.

### NSTD.1:11 - SoTA-Echoing



#### NSTD.1:11.1 - Operational comparison against domain vocabulary


Narratology distinguishes the story’s selected and organized events, the discourse through which it is told and its presentation. Cognitive studies examine event models, perspective and memory. Natural language generation distinguishes content planning, discourse planning and realization. These traditions help pose different questions about selecting material, ordering it, anticipating a possible reading or producing wording. Use their terms in their own domains and FPF distinctions where the claim needs them.

For an incident explanation, selecting only events that support the desired conclusion can produce a fluent but misleading story. Selecting the reader's question together with the relevant events, including an unresolved alternative, yields a draft that can be compared with its source. This DPF combines the source-selection and communication distinctions above for that use. The extra comparison costs effort, so keep it to relations that could change the account or its use. A free fictional invention has a different source obligation: preserve its chosen premises rather than pretend to report an actual event.

Hoffmann’s “The Tensions of Scientific Storytelling” examines how a scientific account can organize attempts, mechanisms and unresolved questions. Schmid’s *Narratology: An Introduction* and Chihaia’s *Introductions to Narratology: Theory, Practice and the Afterlife of Structuralism* offer source-specific accounts of presentation and narratological traditions. Castricato et al.’s “Towards a Model-Theoretic View of Narratives” models a narrator’s information, changes in a reader’s story model and uncertainty. Dahlstrom and Ho’s “Ethical Considerations of Using Narrative to Communicate Science” examines the ethical issues of persuasion. Use these works for their respective claims about scientific communication, interpretation, modeling and influence. Where timing, intervening sources or participant roles change the narrative’s use, make those conditions explicit.

### NSTD.1:12 - Relations

Use `A.6.3.NAR` for the source-to-narrative relation. `A.16.1` can preserve an early cue, `C.2.LS` can clarify an action-changing language distinction, and `G.2` can support synthesis across research traditions. For recoverable source structure see `C.2.8`, and for architecture-description adequacy see `C.33`. Use `NSTD.4` for voice or viewpoint, `NSTD.7` for generated narratives and `NSTD.6` for evaluation. `C.35` applies to a generated result used in architecture work. Use `D.1`–`D.5` for a consequential affected-party or persuasion question, `A.10` for a source connection that is unclear or must remain reproducible, `B.3` for assurance, `E.10` or `F.18` for wording or naming, and `G.11` for currentness. The Architecture and Narrative Work Bridge explains architecture mediation. The Source Use And Refresh Map identifies research grounds. NSTD.Reference:11 distinguishes working terms, and the Name And Edition Route locates the document or edition.

### NSTD.1:End
