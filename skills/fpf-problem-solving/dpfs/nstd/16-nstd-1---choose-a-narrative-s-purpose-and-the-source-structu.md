## NSTD.1 - Choose a Narrative's Purpose and the Source Structures It Must Preserve

> **Status:** Stable

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** selecting source structures and a narrative purpose that serve the intended reader. The optional intake below records one application of this method.

### NSTD.1:1 - Problem frame

Use this pattern when a writer, narrator, teacher, architect, researcher, commentator, story designer, or tool starts with a message, lesson, theme, persuasive effect, desired memory, live commentary line, or future scenario before naming the source structures that must survive the narrative rendering.

First useful move: name the reader's question, point to the available material and choose the relations or events the reader needs. Draft a short account, then compare it with that material. Refine the purpose or selection when the comparison exposes a gap. A few sentences can carry these choices; a completed intake form is not required.

What goes wrong if missed: the desired effect determines what the source is said to contain. Readers may remember the account but miss a relevant relation, mistake uncertainty for fact or be unable to find the material needed to check it.

What this buys: a useful account whose selected content supports its purpose and whose unresolved claims remain visible.

Use `NSTD.4` when viewpoint or voice is the difficulty, and `NSTD.7` when generation needs planning or inspection. Use `C.35` only when the generated result is intended to inform architecture work. A separate evidence, ethics or publication question needs its own applicable method; merely drafting an explanation does not open all of those questions.

### NSTD.1:2 - Problem

Narrative purpose is useful because a narrative rendering is made for someone and for some use. But ordinary purpose language is often too broad: "make it inspiring", "tell the story", "explain the architecture", "make learners care". Those phrases do not say which structures must be preserved, which distinctions may be coarsened, and which downstream use is blocked.

### NSTD.1:3 - Forces

| Force | Tension |
| --- | --- |
| Reader usefulness vs source discipline | A narrative needs a purpose, but the purpose cannot replace selected source structures. |
| Motivation vs authority | Motivation helps attention, but it does not create evidence, assurance, ethics clearance, or work permission. |
| Domain vocabulary and distinct claims | Narrative terms help design; claims about evidence, ethics or authority still need their own grounds. |
| Drafting and source comparison | A quick draft can clarify the purpose; comparing it with the source reveals omissions and unsupported connections. |

### NSTD.1:4 - Solution

Start with a useful reader question and the available material. Select what the account must preserve, choose a provisional order and try a short narrative. Compare it with the source for omitted relations, unsupported additions and misleading connections. Stop when that account serves the intended use, or name the missing source relation that prevents it.

For example, a paragraph states that a valve opens when pressure exceeds a threshold. An operator asks why the valve opened. The first useful account names that condition and the observed pressure, if available. If only the opening was observed, say that the threshold crossing is still unestablished.

When selecting the relations presupposes an account that is not yet available, use NSTD.9 to construct and compare it from the material. Its result can change which events, participants or meanings belong in the selection. A supplied diagram, chronology or interpretation is a usable input when its grounds fit; it need not be reconstructed. For a story or hypothetical scenario whose events are still open, NSTD.10 supplies their construction under the selected premises. Return to the reader's purpose after either result: a discovered ambiguity or a new possibility may change what the narrative should make available.

Use the following optional intake when another worker must continue the task, several alternatives must be compared or a maintained collection needs the same fields. Include only fields that change that use. The filled records later in this section illustrate richer cases; they are not the minimum entry cost.

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

Use `unfoldingStructureRefs?` only when one selected source structure is governed as a constraint-governed unfolding structure by `A.22.CGUS`, `E.18.3`, or a local FPF block. Use `demonstrativeSliceRefs?` only for the slice the narrative renders for the reader; the slice is not the whole selected structure.

The intake supports these decisions when they matter:

1. Identify the material and selected relations or events, explaining their relevance to the reader's purpose. State whether they concern past, live, proposed or fictional events when that changes the account.
2. If the account depends on an architecture description, decision or observation record, keep the needed return to that material. A direct explanation of source claims needs no architecture account.
3. Name the writer's contribution and intended reader in ordinary project terms. Use `NSTD.4` when voice or viewpoint changes what the reader can recover; use `NSTD.7` for a generated draft. A precise system-role classification or assignment uses `A.2` or `A.2.1`. A claimed dated production Work additionally needs the A.13 and A.15.1 grounds for that claim. None of those precise claims is required merely to ask a teacher or agent for an explanation.
4. Relate the purpose to the selected structure and reader use. Revise the purpose or the selection together when either proves unsuitable.
5. Inspect what the draft leads this reader to infer from the selected material. When a particular inference would change the intended understanding or action, locate its basis in the wording, representation, source or an observed reader response. Apply `F.19:4.4` to choose the smallest useful correction. The optional `likelyMisreading?` field records that inference with its ground when another worker needs it.
6. Give the source or further question to return to when an omitted relation or stronger claim becomes necessary.

For a difficult intake, these four questions can expose the unresolved choice. Stop once the useful choice is clear; they are not four required documents.

| Pass | Question | Output |
| --- | --- | --- |
| Source pass | What selected source material or source pack is being rendered, and which selected source structures must remain recoverable for the declared use? | Source-basis refs or source-pack refs, selected source structure refs, and source-return condition. |
| Use pass | Who will use the narrative, for what work or understanding, and which distinctions must they recover? | Reader or listener, reader-interest hypothesis, intended use and the distinctions it requires. |
| Mediation pass | Is the work direct source-structure rendering, architecture-mediated rendering, or mixed? What temporal posture changes source obligations? | Rendering mediation mode, temporal posture, architecture mediation refs, and live telemetry or source-return refs. |
| Reliance question | Which claim or feature of this account creates a consequential reliance question for its intended reader? | Apply `F.19:4.4` to a grounded difficulty; repair the claim or expression and supply any condition, source or decision the use needs. |

A draft can help discover the needed selection. Before relying on it, explain which relations or events matter without using their accidental prominence in that draft as the reason. If the reader's purpose is still unclear, ask a question or offer a small orientation account that helps settle it. Broader claims about completeness or fidelity remain open.

Use these contrasts when the purpose remains unclear:

- Admissible: "This route helps new FPF readers reconstruct why `EntityOfConcern`, forces, and neighboring-pattern exits matter during pattern use." The selected structures are named and the use is reconstructive.
- Below floor for the declared reconstruction lesson: "Make the seminar inspiring so people like FPF." Motivation can help learners continue, but this purpose does not yet identify the source relations they must reconstruct or use. An expressive-only event can have a different sufficient aim.
- Argument explanation: "Help reviewers understand the argument for this proposal." Select its premises, inferences and grounds as the material to explain, together with the consequential uncertainty or competing position.

For prospective or fictional material, select the relevant canon, premises, design constraints or future-state hypotheses. The narrative may add proposed events within those constraints. If a turn conflicts with them, change the turn or explicitly change the premise; excitement alone does not resolve the conflict. A formal source pack is useful when maintaining canon or comparing alternatives requires it.

When the narrative selects part of a constraint-governed unfolding structure, identify that wider structure and the chosen part. The selected structure may be `ConstraintGovernedUnfoldingStructure@Context`, an `E.18.3` transformation-flow unfolding structure, a P2S local block, an improvement-loop block, or a narrative-ordering block under `A.6.3.NAR`. The writer may choose one `DemonstrativeUnfoldingSlice@Context` for the reader's use. Identify omitted branches, alternatives, loops, constraints or exits when losing them would change the reader's understanding or next action. The slice is not the whole selected structure and not a work order.

Use role-specific intake prompts when the worker is stuck.

| Worker situation | Prompt | Expected answer |
| --- | --- | --- |
| Teacher or trainer | "After the narrative, what should learners reconstruct from source without relying on my story?" | Source spine, reconstruction task, and source-return condition. |
| Architect or analyst | "Which structure, trade-off, candidate, telemetry, or decision memory must survive the narrative?" | Architecture or source-structure refs plus rendering mediation mode. |
| Scientist or researcher | "Which mechanism, calculation, failed attempt, source uncertainty, or unresolved tension is being rendered?" | Mechanism or event support, uncertainty, evidence owner, and source return. |
| Story designer | "Which canon, premise, agency, continuity, or causal plot constraint governs this route?" | Bounded source pack and non-publication boundary when needed. |
| Live commentator | "Which observation, inference, prediction, and later official source must stay distinguishable?" | Temporal posture, uncertainty markers, and refresh condition. |
| Tool builder | "What material and relations must the output preserve, and how will a reader or operator detect a consequential omission or invention?" | A generation plan and source-comparison question under `NSTD.7`; add production-history or responsibility details when the intended use requires them. |

Mood, audience reaction, style or genre can be part of a legitimate purpose. When source fidelity or learning is also intended, those aims leave the needed source selection unanswered. Resolve that question before claiming fidelity or learning; `NSTD.4` and `NSTD.5` can help realize the expressive aim.

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
  readerInterestOrUseHypothesis: learner needs usable entry, not complete monolith memory
  intendedReaderOrListenerUse: reconstruct one pattern-use route and apply it to a new case
  narrativePurpose: orient attention and sequence learning tasks around source-returnable pattern use
  sourceReturn: FPF source patterns and teaching publication-carrier relation
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
  sourceReturn: mathematical source or proof owner
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
  sourceReturn: event source owner, official record, recording, telemetry
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


Use the precise construction in `A.6.3.NAR:4.0.1` when the receiving use needs identifiable source and narrative claims for citation, dispute, consequential cross-scheme use or another stated reliance requirement. Recover source episteme X, narrative episteme Y and the construction between them; preserve the same EntityOfConcern and test any correspondence on which it depends. Public distribution by itself does not require this fuller account. A permission, evidence or assurance claim still needs its own grounds.

### NSTD.1:5 - Archetypal Grounding



#### NSTD.1:5.1 - Worked slice: FPF seminar from source spine to narrative route


A seminar author receives the request: "Tell a motivating story about FPF so people want to use it." To turn that aim into a lesson, the author chooses what learners should be able to do: recognize a situation, select a suitable pattern and apply its conditions. The following record shares those choices with another teacher; a sole author could develop them in the draft itself.

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
  intendedReaderOrListenerUse: reconstruct one pattern-use route and choose the next governing pattern
  narrativePurpose: orient attention and motivation toward source-returnable pattern use
  sourceReturn: selected FPF pattern body and relation record
  additionalClaimQuestion: none unless the seminar makes assurance, policy, or affected-party claims
  refreshCondition: FPF edition or selected-source pattern changes; learner reconstruction test fails
```

The record above makes the choices available to another teacher; the writer can develop them while composing. A short opening can ask learners to choose a pattern for a difficulty they recognize. The next passage explains how its conditions, forces and neighboring exits affect that choice, then the exercise returns to the selected pattern. The account connects a memorable question with the source contribution needed to answer it.

Evaluation through `NSTD.6` later asks whether learners can choose a pattern for another case, explain the conditions affecting that choice and return to its body for the needed method. A response that repeats the opening question without using those conditions identifies a missing contribution to the lesson; the teacher returns to source selection, explanation or practice as appropriate.

If an LLM produces a seminar draft, the intake keeps three positions separate:

```text
renderingContribution: course-author or generator-operator role; recover the actual system, role assignment, and Work separately when those claims are made
narrativeVoiceOrViewpoint: teacher-facing explanatory voice under NSTD.4
generatedDraftInspectionRef: the NSTD.7 case that identifies the generated draft, source comparison and acceptance for its intended use; C.35 applies only when the result informs architecture work
```

One person may operate the tool, choose the voice and decide how to use the result. The output still needs comparison with the selected material.



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

The team uses this account to recover the selected structure and the reasons for preserving or varying its parts. Return a missing design choice to the architecture work. Use `NSTD.6`, applying `C.2.8`, when the question is what structure the reader can recover; use `C.33` for the adequacy of the architecture description and `C.34` for correspondence with realized structure. `E.17` governs publication when it is needed. `NSTD.1` connects the narrative purpose with those selected structures and the team's use.



#### NSTD.1:5.3 - Worked slice: franchise continuation probe


For a continuation-style storycraft probe using a well-known space-opera franchise such as `Star Wars`, select the canon, premise and continuity constraints relevant to the proposed scene. A draft can help reveal which of those choices remain unclear. In this example the use is a private critique; a later publication would raise separate rights questions.

The request "Write a surprising sequel that feels epic" leaves those choices open. For the private critique, the writer chooses a continuation premise that preserves a character's established motivation and the consequences of earlier events. A new event may extend the story; if it conflicts with the chosen continuity, revise the event or explain the changed premise. Ordering and suspense alone cannot repair that conflict.



#### NSTD.1:5.4 - Role-specific first moves


| Worker | First source-selection move | Common hidden overread | Repair when that difficulty occurs |
| --- | --- | --- | --- |
| Teacher | Name the source spine and reconstruction task. | Learner interest means learning occurred. | Add source-return question and later `NSTD.6` row. |
| Architect | Name selected structures, candidates, residuals, and actual-structure feedback. | Explanatory story is the architecture decision. | Route decision authority to architecture decision owners. |
| Scientist | Name mechanism, calculation, uncertainty, and proof or evidence boundary. | Story coherence is evidence closure. | Add evidence owner and source-return condition. |
| Story designer | Name source pack, continuity, agency, and non-use boundary. | Dramatic surprise authorizes source violation. | Reopen source-pack selection before ordering. |
| Live commentator | Name event stream, provisional interpretation, and later official return. | Live causal claim is settled fact. | Mark uncertainty and telemetry return. |
| AI-agent operator | Name material, required relations and the proposed use. | Fluent prose silently adds a cause or drops a constraint. | Inspect and repair through `NSTD.7` and `NSTD.6`; apply `C.35` only for an architecture use. |



#### NSTD.1:5.5 - Match the source return to the intended use

Across these cases, the source return follows what the reader needs to recover. The seminar returns to a pattern's working conditions; the mathematical explanation to definitions, constraints and proof; live commentary to observations and subsequent official corrections; fictional continuation to its selected premises. A desired effect cannot establish the support that the intended use needs. When that use changes, revisit the source selection: an orientation may become a claim needing investigation, or a private story critique may become a publication needing separate consideration of rights.


### NSTD.1:6 - Bias-Annotation

A writer can select only the material that supports a desired conclusion. Compare the proposed account with relevant omitted relations and alternatives, then repair its selection or qualify its use. The converse mistake is to demand a completed source-and-role dossier before a simple explanation. Start with the useful account and add documentation only when another use consumes it.

### NSTD.1:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD1-1` | The reader purpose and selected material are connected; the draft is compared with the source before the intended reliance. |
| `CC-NSTD1-2` | Source-structure selection rationale explains why these structures are needed for the reader or listener use. |
| `CC-NSTD1-3` | Past, live, proposed or fictional status and any intervening description are clear wherever they change interpretation. |
| `CC-NSTD1-4` | Writing contribution, narrative viewpoint and intended reader are distinguishable when needed. Precise system-role, assignment or dated Work claims receive their own grounds only when asserted. |
| `CC-NSTD1-5` | The intended use supplies enough direction to choose or improve the account, including an expressive aim when that is the task. |
| `CC-NSTD1-6` | A correction of a misleading inference has the independent ground, plausible reader and useful contribution required by `F.19:4.4`; any recorded difficulty keeps that ground. |
| `CC-NSTD1-7` | Additional evidence, ethics, authority or production-history claims have the grounds their actual use requires. |
| `CC-NSTD1-8` | The reader can find the relevant source and knows when to revisit it if currentness or hidden distinctions affect the use. |

### NSTD.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Desired conclusion selects its own evidence | The account suppresses a relevant conflicting relation. | Compare the draft with the needed source relations and alternatives; change its selection or qualify the conclusion. |
| Unexplained selection | Neither the writer nor reader can say why a relation was included or omitted. | Recover that choice from the intended use and source; revise the selection where it fails. |
| Motivation as truth support | A moving narrative is treated as stronger evidence. | Use the claim's subject grounds and keep motivation as reader-use support. Use `A.10` when the source-to-use account is implicit or must remain replayable. |
| Unstated limit that changes reliance | A reader uses an incident chronology as its causal explanation. | State which causal claim is unresolved and where to obtain the needed account. |

### NSTD.1:9 - Consequences

The reader's purpose and the source relations guide drafting together. The cost is selecting and comparing the needed content; a maintained intake adds documentation only when later coordination or comparison uses it.

### NSTD.1:10 - Rationale

Narrative design begins from audience, communicative aim and available material. Relating those choices prevents the desired effect from silently determining what the source is said to contain. A narrative is the resulting account; the structure-to-narrative construction explains how it draws on the selected source.

### NSTD.1:11 - SoTA-Echoing



#### NSTD.1:11.1 - Operational comparison against domain vocabulary


Narratology distinguishes story, discourse and presentation; cognitive accounts examine event models, perspective and memory; NLG separates content planning, discourse planning and realization. Use these distinctions to ask different practical questions: what material to select, what order to present, what the reader is likely to infer, and what wording to produce. Their terms retain their disciplinary meanings; FPF supplies additional distinctions only where a claim needs them.

For an incident explanation, selecting only events that support the desired conclusion can produce a fluent but misleading story. Selecting the reader's question together with the relevant events, including an unresolved alternative, yields a draft that can be compared with its source. This DPF combines the source-selection and communication distinctions above for that use. The extra comparison costs effort, so keep it to relations that could change the account or its use. A free fictional invention has a different source obligation: preserve its chosen premises rather than pretend to report an actual event.

Hoffmann's "The Tensions of Scientific Storytelling" shows that scientific story construction can organize attempts, mechanisms, and unresolved tensions for readers; Schmid's `Narratology: An Introduction` and Chihaia's `Introductions to Narratology: Theory, Practice and the Afterlife of Structuralism` show that presentation and audience-facing narrative traditions differ by source tradition; Castricato et al.'s "Towards a Formal Model of Narratives" supports explicit narrator-to-reader information flow, reader story-model evolution, and uncertainty; Dahlstrom and Ho's "Ethical Considerations of Using Narrative to Communicate Science" warns that communicative purpose can become persuasion risk. The DPF uses audience and purpose to guide source selection, and makes temporal posture, mediation and participant distinctions explicit when they affect the narrative's use. When a purpose, reader-use, science-storytelling, teaching, future-scenario, or persuasion-risk claim depends on a cited source basis, name that source basis and keep the claim within its boundary.

### NSTD.1:12 - Relations

Uses `A.6.3.NAR` to define the Core narrative relation, `A.16.1` when the first honest material is only a pre-articulation narrative cue, `C.2.LS` when language-state facets or thresholds shape the intake, `G.2` for SoTA harvesting and synthesis across traditions, `C.2.8` for reader-relative structural amount and `C.33` for architecture-description adequacy, `NSTD.4` for load-bearing voice or viewpoint, `NSTD.7` for automated narrative construction and inspection, with `C.35` only for a result entering architecture work, `NSTD.6` for declared-use narrative evaluation, `D.1` through `D.5` when affected parties or persuasion are live, `A.10` for evidence, `B.3` for assurance, `E.10` and `F.18` for durable wording or naming repairs, and `G.11` for source and telemetry refresh. Support-map entry: open `Architecture and Narrative Work Bridge` when `renderingMediationMode` is `architecture-mediated` or `mixed`; open `Source Use And Refresh Map` when a cited source basis is relied on or stale; open `NSTD.Reference:11 — Working meanings and direct source returns` when a local narrative term threatens to become ontology; open `Name And Edition Route` only for DPF-prefix or edition questions.

### NSTD.1:End
