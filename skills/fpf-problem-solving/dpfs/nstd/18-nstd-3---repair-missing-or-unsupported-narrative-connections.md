## NSTD.3 - Repair Missing or Unsupported Narrative Connections (Coherence and Event Models)

> **Status:** Stable

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** the connections a reader needs to reconstruct events, mechanisms or dependencies from a narrative.

### NSTD.3:1 - Problem frame

Use this method when you need to assess or explain a connection in a narrative. A reader may be able to retell the events yet leave open what changed, how a mechanism worked, why a design choice mattered or how a proof step followed.

State what the reader must be able to connect. Find the words, scenes or source records that carry each end of that connection and read them together. One sentence may suffice for a local question. If revising, supply a missing step from its grounds, correct an unsupported claim or make the unresolved question clear.

To explain a past reading, examine what the reader said or did with the passage and what other information or help they used. An analysis of the text can establish what it made possible to infer under stated assumptions.

The comparison shows which connections the passage supports and which still depend on an unstated premise, a different source or a further observation.

### NSTD.3:2 - Problem

An event sequence can make a narrative easy to follow. A design dependency, mathematical definition or relation between a finding and its evidence can matter even when nothing happens in sequence. Turning such a relation into an episode can obscure what follows from it.

### NSTD.3:3 - Forces

| Force | Tension |
| --- | --- |
| Events and other structures | A reader may follow the episodes and still miss the dependency on which the explanation turns. |
| Causal wording and its grounds | A physical cause, a reason for acting, a proof step and a fictional motive require different grounds. “Because” can introduce any of them. |
| Mechanism and uncertainty | A clear account of the proposed mechanism can still give the impression that an untested or disputed step is settled. |
| Reconstruction and engagement | Ask what the reader should be able to reconstruct when that ability matters to the intended use. |

### NSTD.3:4 - Solution

Identify what changed, what depends on what, what explains an action or which condition limits a conclusion. For a single passage, compare it directly with the source or premises. A note like this can preserve grounds that several passages or collaborators will need.

```text
NarrativeEventMechanismSupport@Context:
  narrativeRenderingRef:
  sourceStructureKind:
  requiredReaderReconstruction:
  eventOrMechanismModel:
  participants?:
  dependencyOrConstraintRefs?:
  causalClaimBasis?:
  uncertaintyOrUnknownRefs?:
  reconstructionTaskRefs?:
  sourceReturnCondition:
```

Compare the intended connection with what the passage expresses or permits a reader to infer. Supply an omitted step if the source establishes it. When the source leaves the relation open, state what cannot be determined and identify any alternatives the material supports. An action may be clear while two motives remain possible or its motive is wholly unknown. Use NSTD.9 to examine a disputed reading. If a fictional scene or an explicitly hypothetical real-world scenario needs a new event or constraint, use NSTD.10 to construct it under the chosen premises.

When a passage joins several well-supported statements, ask what the reader is meant to infer from them together. A report may establish that an operator rolled back a setting, and a log that service returned. To say that this operator restored this service by that action, connect the records to the same incident and establish the effect of the rollback. Even records from the same incident can leave the cause open. For a question about whether service was available at a stated time, a sufficient observation of service at that time can settle the matter directly.

The following questions support an assessment or revision. Keep the answers that another part of the work needs.

1. State the connection at issue and the source or premise on which it depends. Identify any uncertainty that bears on it.
2. Identify the kind of connection. An event order, mathematical dependency, physical cause and fictional motivation answer different questions. Establish the grounds appropriate to the one claimed.
3. Identify what a reader needs here, such as a state change, an explanation, a prediction or the point where an analogy stops.
4. Compare the passage with that task. What supports the intended reading? Does a word or omission suggest a different relation?
5. When a change is needed, supply a missing step, correct the kind or strength of the claim or identify the relevant uncertainty. State an established conclusion at the strength its grounds support. Return to the subject source when a stronger answer is needed.

Examine how a connector works in its sentence before choosing a repair.

| Wording | Question about this passage | Repair when needed |
| --- | --- | --- |
| "then" or "after" | Does the source establish this sequence, or is this only the chosen presentation order? | State the supported sequence or explain the ordering choice. |
| "because" | Does it introduce a cause, a reason, a proof dependency or a fictional motive? | Supply or qualify that relation. Use `C.28` only when its causal-use question is at issue. |
| "therefore" | Which premises and inference make the conclusion follow? | Restore the missing premise or step, or state the remaining uncertainty. |
| "had to" | Which condition makes the action necessary, and under which alternatives? | Name that condition or replace necessity with the supported choice. |
| "wanted" or "decided" | Whose motive or decision is asserted, and is it factual, fictional or interpretive? | Clarify the participant and grounds. Use `NSTD.4` when viewpoint or attribution causes the ambiguity. |
| "shows that" | What does the observation, argument or example establish? | Match the conclusion to its grounds. Use `A.10` when the connection to the evidence needs recovery or must be reproducible. |
A proof may be presented as a sequence of questions and inferences, and an architecture choice as a comparison of trade-offs. If you invent a scene of discovery to illustrate a proof, distinguish the imagined events from the premises and inferences that establish the result.

Derive the reconstruction from the reader’s job. The task may supply a kind of connection and still leave the reader to identify which events it connects or what supports it. Leave open whichever of these choices the reader is to make. Name the connection itself when the job is to explain one already identified. Each question below leaves some work to the reader. Choose its wording according to which connection the reader is to identify or explain.

- Name the proposed mechanism and the relation still unresolved.
- In a live account, identify an observation, an inference and a prediction.
- Point to the formal statement where the mathematical analogy stops.
- Explain the trade-off accepted in a design choice and the exception it left open.

If the required reconstruction cannot yet be stated, clarify what the reader needs to do with the passage. Entertainment or initial orientation can be sufficient aims. A use that depends on a mechanism or inference needs a recoverable account of that relation.

### NSTD.3:5 - Archetypal Grounding



#### NSTD.3:5.1 - Worked example: event support


A science narrative says that a failed experiment forced a theory to change. First find out what failed. Did the instrument give an unusable reading, or did a qualified measurement disagree with a prediction? In the second case, determine which assumptions the discrepancy puts in question and whether the evidence distinguishes any replacements.

```text
NarrativeEventSupportRecord@ExperimentTension:
  narrativeRenderingRef: ScienceStory@v1
  eventOrMechanismClaim: a qualified measurement disagreed with the range predicted from the proposed mechanism and its auxiliary assumptions
  sourceStructureRef: measurement record, model expectation, uncertainty interval, alternative explanations
  relationStrength: observed discrepancy under the stated assumptions, with its explanation unresolved
  reconstructionTarget: distinguish the discrepancy, its possible explanations and the contribution of any later evidence
  overclaimRisk: stating that the discrepancy forced one particular theoretical change
  sourceReturnCondition: return to the measurement and model assumptions when a stronger conclusion is needed
```

Before:

> The experiment failed, so the old theory collapsed.

After:

> The measured value lay outside the predicted range under the stated assumptions. The discrepancy bears on the mechanism model and the assumptions used in measurement. The observed difference alone leaves the proposed replacements unresolved.

The passage makes the discrepancy and unresolved alternatives available to the reader. To distinguish the explanations, look for an existing result that would differ under them. A further experiment is one option when it could obtain such a result and the question warrants it.



#### NSTD.3:5.2 - Worked example: franchise plot support


In a proposed continuation, a character betrays an ally “because the plot needs a darker turn”. This gives the author’s purpose. To explain the character’s choice, look for a motive supported by the selected canon and the circumstances of the scene.

```text
NarrativeEventSupportRecord@CharacterTurn:
  eventOrMechanismClaim: character changes allegiance under named pressure
  sourceStructureRef: selected canon constraint, prior motivation, current dilemma, consequence chain
  relationStrength: a proposed motive consistent with the selected fictional premises
  reconstructionTarget: reader can state motive, pressure, action, consequence, and canon-return condition
  overclaimRisk: author need or theme is treated as character cause
  sourceReturnCondition: consult the selected canon and the character’s available choices when a claim about the motive depends on them
```

If the story needs an intelligible motive, supply the pressure, choice or event that makes the betrayal intelligible, or revise the turn. An existing passage can support two plausible motives. Deliberate absurdity or an unexplained turn may also serve the intended work.



#### NSTD.3:5.3 - Comparing relation support


| Observation | Next useful move |
| --- | --- |
| Events are easy to retell but the needed relation is supplied only by a suggestive connector. | Find and express the missing basis or change the claim. |
| The relation is named but its conditions remain unclear. | State the condition that changes the reader's inference. |
| The reader reconstructs the relation and its relevant limits. | Use that finding for the observed conditions. Pursue a further uncertainty if the question requires it. |
| A change of viewpoint or order may conceal the relation. | Compare the passages and report any loss that matters to the intended reading. If a revision is requested, restore the connection or use a version that preserves it. |

Use `NSTD.6` when the work needs a qualified assessment of reception or quality. The comparison can also answer a narrower question about the passage itself.



#### NSTD.3:5.4 - Connecting to the relevant subject method


“Because” may introduce a physical cause, a reason for acting or a mathematical dependence. Identify the particular relation. Consult its FPF or subject method when the source leaves a material question about that relation open.

Suppose a proposed module split removes one hand-off between teams for routine requests and routes exceptions through a shared interface. The design establishes this change of dependency. A prediction of lower coordination cost also depends on the frequency and cost of exceptions. Suitable experience with the implemented design can establish the time actually spent and, with an appropriate comparison, whether the change reduced it.

To write that a result forced a theoretical revision, establish which alternatives the measurement and other evidence excluded under the assumptions in use. The result may instead expose a discrepancy, reduce support for a hypothesis or suggest a mechanism to examine. Any of these can be the conclusion of the account.

In live commentary, identify the late midfield movement and the loss of possession. A replay of how the opposing side gained possession might distinguish a tactical gap, a missed challenge or a contribution from both. Report the limit when the evidence leaves the explanation open.

For a homotopy explanation, connect the image of deforming a loop to its permitted deformations. Identify the formal definition or argument that supports any claimed invariant, and what the learner should be able to recover from the image.

Use the source to decide how to revise a disputed sentence.

| Initial sentence | Source-support question | Replacement selected by the answer |
| --- | --- | --- |
| “The failed experiment revealed the true mechanism.” | Does the source identify the mechanism, rule out a prediction, or merely report a discrepancy? | If it reports only a discrepancy, state the measurement and prediction that disagree and leave the mechanism unresolved. If it establishes the mechanism, retain that conclusion and its supporting scope. |
| “The module split solved coordination.” | Does the source show a changed dependency, predict a cost effect or observe one? | For the proposed design above: “The split removes one required hand-off and routes exceptional requests through a shared interface. Its effect on coordination time has not yet been measured.” A measured reduction would warrant the corresponding observed claim. |
| “The character had no choice.” | Which alternatives do the fictional premises actually exclude? | If the scene establishes that both exits are locked and no other escape is available, say “With both exits locked, the character remained in the room.” If an alternative remains possible, describe the choice or pressure rather than inventing necessity. |
| “The proof idea is that loops remember holes.” | Which formal restriction or invariant does the image represent? | If the supplied definition requires a loop to remain in the punctured plane, explain that a deformation cannot pass through the missing point. Return to the argument for any claimed invariant; the image alone establishes no theorem. |
| “The team was outplayed because the press failed.” | What sequence is observed and what supports the tactical explanation? | With only the late midfield movement and subsequent loss of possession established, report both events and identify the tentative explanation. Use a stronger conclusion if later analysis distinguishes its contribution. |

Suppose the source defines f(x) = 2x and the task gives x = 3. Then f(3) = 6 follows by substitution. If the source records only the pair (3, 6), that observation establishes the pair and leaves the rule open. The same numbers support a deductive conclusion in the first case and a limited observation in the second.

If the factual repair has reduced engagement that matters to the task, use `NSTD.5` to develop the presentation around the supported relation.

These notes illustrate three different uses.

```text
NarrativeEventMechanismSupport@ArchitectureTradeoff:
  sourceStructureKind: dependency and trade-off in a proposed software architecture
  requiredReaderReconstruction: which required hand-off the proposed design removes, where exceptional requests go, and why an observed time saving remains unknown
  eventOrMechanismModel: ordinary requests no longer cross the removed hand-off; exceptional requests still require shared-interface coordination
  dependencyOrConstraintRefs: before-and-after dependency diagram; rule selecting exceptional requests; shared-interface responsibility
  supportingBasis: the design shows the removed hand-off and the exception route. Their frequency and cost matter to the prediction of time saved
  uncertaintyOrUnknownRefs: realized coordination time unmeasured; other candidate designs outside this sketch
  reconstructionTaskRefs: reader distinguishes the design change, remaining exception work and unmeasured cost effect
  sourceReturnCondition: consult the dependency comparison for the design claim and observations for an actual cost claim
```

```text
NarrativeEventMechanismSupport@HomotopyAnalogy:
  sourceStructureKind: proof-like and definition-like dependency
  requiredReaderReconstruction: distinguish intuitive deformation image from formal equivalence relation
  eventOrMechanismModel: path deformation story used as analogy for invariant tracking
  dependencyOrConstraintRefs: formal definitions; examples; counterexamples; theorem prerequisites
  basisForLearningEffect: a claim that the analogy helped learners would need evidence that distinguishes its contribution
  uncertaintyOrUnknownRefs: analogy may fail outside named examples
  reconstructionTaskRefs: identify where the image stops and which formal premise or argument is needed
  sourceReturnCondition: formal source statement for proof or exercise use
```

```text
NarrativeEventMechanismSupport@LiveCommentary:
  sourceStructureKind: live event stream with provisional interpretations
  requiredReaderReconstruction: observed event vs inference vs prediction vs official correction
  eventOrMechanismModel: state updates and tactical hypothesis under uncertainty
  participatingHolonOrRoleRefs: teams, players, officials, broadcast or event source roles when needed
  uncertaintyOrUnknownRefs: events outside the camera view and decisions still under official review
  reconstructionTaskRefs: listener can say what was observed and what was inferred
  sourceReturnCondition: official record, recording, statistics, or telemetry
```

For each use, retain the information needed to explain, compare or repair the connection.

### NSTD.3:6 - Bias-Annotation

A vivid episode can make a suggested cause or motive feel established. Compare the relation implied by the passage with the observation, argument or fictional premise that could support it. Separate what the text permits from what a particular reader actually reconstructed. Return to the subject source where the relation itself remains in question.

### NSTD.3:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD3-1` | The passage represents the relevant source relations without silently turning a dependency, constraint or proof step into a physical event. |
| `CC-NSTD3-2` | The assessment identifies what the passage makes recoverable under the assumed knowledge, or what remains uncertain. To report what a particular reader understood, use a response or action that reveals their interpretation of the connection at issue. |
| `CC-NSTD3-3` | The evidence supports the connection the reader needs, including any link between the events or contributions combined in the account. Cause, dependency, necessity and motive each have grounds appropriate to the claim. |
| `CC-NSTD3-4` | An unknown, disputed or deferred relation remains visible when it affects the reader's conclusion or action. |
| `CC-NSTD3-5` | Learning or consequential use has a suitable way to check or recover the needed connection. A separate test or source note is selected for its value to that use. |

### NSTD.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Fluent but unsupported explanation | A passage invites an explanation that its source does not support. | Supply the missing connection, qualify it or return to the unresolved source question. |
| Causal overstatement | An account attributes an effect on the strength of event order alone. | State the observed order and the support for any further causal inference. Use `C.28` if the particular causal claim needs examination. |
| Event forcing | A graph, proof dependency or architecture view is retold as an invented sequence of events. | Identify the source relation. If its presentation order needs changing, use `NSTD.2` to compare alternatives. |

### NSTD.3:9 - Consequences

The comparison can show why a reader would infer too much from a fluent passage and what its source actually supports. Correcting the passage may require recovering the source relation or changing a dramatic simplification.

### NSTD.3:10 - Rationale

Readers often use event models and causal expectations to follow a narrative. What a passage invites them to infer and what the subject evidence establishes can differ, including in an account of a mechanism, an architecture or a proof.

### NSTD.3:11 - SoTA-Echoing

Nguyen's [A Review of Mechanistic Models of Event Comprehension](https://arxiv.org/abs/2409.18992) (2024) compares accounts of prediction, hierarchy, updating and causal representation in comprehension. Hoffmann's [The Tensions of Scientific Storytelling](https://roaldhoffmann.com/sites/default/files/fromd6/Tensions%20ofScientific%20Storytelling%20as%20published.pdf) (2014) illustrates how scientific accounts organize mechanisms and unresolved tensions. Gatt and Krahmer's [NLG survey](https://arxiv.org/abs/1703.09902) (2018) distinguishes content selection and realization. This pattern's synthesis is to compare the connection the passage suggests with the relation its source or premises support.

The sources contribute different operations.

- Use event-comprehension models to identify event boundaries, dependencies or predictions that matter to a reading task. Evidence about the particular reading can then establish what a reader recovered.
- Scientific storytelling can make an unresolved tension intelligible. Distinguish the established observation from the explanations still possible.
- In natural language generation, compare the selected content as well as its expression. A smoother connective will leave an omitted premise missing.
- For evidence, inference or cause, inspect the complete claim before choosing how to substantiate it.
- In an architecture account, distinguish an accepted trade-off, residual exception handling and what operation measurements establish about the realized design.

A local wording change such as “preceded” in place of “caused” can be sufficient when the source establishes that order. If a source identifies the cause, the change would discard information. In the incident log the dates support the chronology, while the cause remains open. Checking the source decides whether the small edit preserves the claim.

The source comparison in §4 and the examples in §5 adapt distinctions from event modeling and content planning. Scientific storytelling also shows how to make an open research question part of an account. Return to the passage if new evidence changes the source relation, the intended task changes or an observed reading reveals a different interpretation that matters to that use.

### NSTD.3:12 - Relations

Use `A.6.3.NAR` and `NSTD.2` for narrative form and order. Use `C.28` for a causal claim needing examination, `A.10` when the route from a source to a claim is unclear or must be reproducible, and `B.3` when reliance on the resulting claim needs qualification. `NSTD.6` can use `C.2.8` for structural recoverability and `C.33` for the adequacy of an architecture description. Use `C.34` when a claim concerns preservation or correspondence of an architectural structure, and `G.11` when a changed source or result may affect the maintained account. Use the Architecture and Narrative Work Bridge for an architectural dependency, the Source Use and Refresh Map for a source claim, and NSTD.Reference:11 for a technical term’s meaning and direct source. Qualify the proposed mechanism on its own grounds.

### NSTD.3:End
