## NSTD.3 - Repair Missing or Unsupported Narrative Connections (Coherence and Event Models)

> **Status:** Stable

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** repairing the connections through which a reader reconstructs a narrative's events, mechanisms or dependencies.

### NSTD.3:1 - Problem frame

Use this pattern when locally fluent narrative passages fail because readers cannot build a coherent model of source mechanism, event flow, dependency structure, architecture relation, state change, or proof dependency.

First useful move: take one passage the reader cannot explain, state the connection it suggests and compare it with the source or fictional premises. Add the missing connection, qualify an unsupported one or keep the unresolved question visible.

What goes wrong if missed: fluency is mistaken for source coherence. Readers remember the story but cannot say what changed, why it changed, which relation mattered, or where the claim stops.

What this buys: coherence is tied to recoverable source structure, not to smooth prose alone.

### NSTD.3:2 - Problem

Narratives often use events and agents because they are easy to follow. But many source structures are not event sequences. Architecture structures, mathematical definitions, evidence graphs, mechanism diagrams, and source packs can be misread when forced into a fiction-like event model.

### NSTD.3:3 - Forces

| Force | Tension |
| --- | --- |
| Event readability vs non-event structures | Readers follow events easily, but not every source relation is an event. |
| Causal wording vs causal support | A causal explanation needs grounds for the particular cause; “because” can also introduce a reason, proof step or fictional motive. |
| Mechanism clarity vs uncertainty | A good mechanism story can hide unknown or contested source relations. |
| Reconstruction vs entertainment | The declared use may require reconstruction, not only engagement. |

### NSTD.3:4 - Solution

Work on the connection the reader needs: what changed, what depends on what, why an action follows or which condition limits the conclusion. The optional note below is useful when several passages, collaborators or later comparisons need to retain that analysis. A single passage can be repaired directly.

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

Compare the intended reconstruction with the passage and its source. An unknown source relation and a relation merely omitted from the explanation call for different repairs. An ambiguity can also be supported by the account: the text may leave several motives possible while clearly showing the action. Preserve those alternatives when that is the intended use; NSTD.9 helps distinguish a warranted reading from an invented resolution. If the story requires an event or relationship that has not been constructed, use NSTD.10. Adding a connective phrase cannot perform that construction.

Use the following questions to repair a passage; retain answers only where the working use needs them.

1. State the connection on which the passage depends, its source or premise, and what remains unknown.
2. Identify the relation and its grounds. For example, a time sequence, mathematical dependency, physical cause and fictional motivation answer different questions; they are not successive strengths on one scale.
3. State what the reader needs to reconstruct: for example a state change, explanation, prediction or limit of an analogy.
4. Find wording or omissions that invite a different reconstruction from the one supported.
5. Repair the connection: supply a missing step, correct its kind or strength, add a relevant uncertainty, or return to the source question. Keep a strong claim when its grounds support it; weakening every claim can also mislead.

Connectors are cues to inspect the complete claim, not automatic triggers for another procedure.

| Wording | Question about this passage | Repair when needed |
| --- | --- | --- |
| "then" or "after" | Does the source establish this sequence, or is this only the chosen presentation order? | State the supported sequence or explain the ordering choice. |
| "because" | Does it introduce a cause, a reason, a proof dependency or a fictional motive? | Supply or qualify that relation. Use `C.28` only when its causal-use question is at issue. |
| "therefore" | Which premises and inference make the conclusion follow? | Restore the missing premise or step, or state the remaining uncertainty. |
| "had to" | Which condition makes the action necessary, and under which alternatives? | Name that condition or replace necessity with the supported choice. |
| "wanted" or "decided" | Whose motive or decision is asserted, and is it factual, fictional or interpretive? | Clarify the participant and grounds. Use `NSTD.4` when viewpoint or attribution causes the ambiguity. |
| "shows that" | What does the observation, argument or example actually establish? | Match the conclusion to those grounds; an evidence claim may require `A.10`. |
A proof can be narrated through questions and inferences, and an architecture explanation through a trade-off. Describe those relations as such. Inventing an event or intention to connect them may change the subject. An imagined discovery scene can still illustrate a proof when its imagined events remain distinguishable from the mathematical argument.

Reader reconstruction tasks should be concrete:

- "Name the mechanism and the unresolved relation" is better than "understand the mechanism."
- "Distinguish observed event, inference, and prediction" is better than "follow the live story."
- "Point to the formal statement where the analogy stops" is better than "get the math intuition."
- "Recover which architecture trade-off was accepted and which exception remains" is better than "remember the project story."

If the required reconstruction cannot yet be stated, clarify what the reader needs to do with the passage. Entertainment or initial orientation can be sufficient aims. A use that depends on a mechanism or inference needs a recoverable account of that relation.

### NSTD.3:5 - Archetypal Grounding



#### NSTD.3:5.1 - Worked example: event support


A science narrative says: "The failed experiment forced the theory to change." Compare the observed result with the prediction and alternatives: was a consequence refuted, an auxiliary assumption questioned, or a replacement supported? The repair should say which of those happened.

```text
NarrativeEventSupportRecord@ExperimentTension:
  narrativeRenderingRef: ScienceStory@v1
  eventOrMechanismClaim: failed measurement challenged the prior mechanism hypothesis
  sourceStructureRef: measurement record, model expectation, uncertainty interval, alternative explanations
  relationStrength: observed mismatch plus mechanism hypothesis, not proof of forced theory change
  reconstructionTarget: reader can distinguish observed result, hypothesis pressure, and later evidence
  overclaimRisk: "forced", "proved", "settled", and "therefore" make the relation too strong
  sourceReturnCondition: return to the measurement and model assumptions when a stronger conclusion is needed
```

Before:

> The experiment failed, so the old theory collapsed.

After:

> The measured value lay outside the range predicted under these assumptions. The discrepancy calls for examining the mechanism model and the measurement assumptions; this experiment does not yet distinguish the proposed replacements.

The repaired passage retains the surprising result and the next research question, while distinguishing the mismatch from the still-undecided explanation.



#### NSTD.3:5.2 - Worked example: franchise plot support


In a continuation-style storycraft probe, a scene says that a character betrays an ally "because the plot needs a darker turn." That is a narrative-function explanation, not source support. Repair it as source structure:

```text
NarrativeEventSupportRecord@CharacterTurn:
  eventOrMechanismClaim: character changes allegiance under named pressure
  sourceStructureRef: selected canon constraint, prior motivation, current dilemma, consequence chain
  relationStrength: a proposed motive consistent with the selected fictional premises
  reconstructionTarget: reader can state motive, pressure, action, consequence, and canon-return condition
  overclaimRisk: author need or theme is treated as character cause
  sourceReturnCondition: return to source pack and agency constraints
```

For a story whose events should follow intelligible motives, the author's desire for a twist does not supply the character's reason. Add a pressure, choice or event that makes the turn intelligible, or revise the turn. A deliberately unexplained or absurd turn has a different artistic aim and should be judged for that aim.



#### NSTD.3:5.3 - Comparing relation support


| Observation | Next useful move |
| --- | --- |
| Events are easy to retell but the needed relation is supplied only by a suggestive connector. | Find and express the missing basis or change the claim. |
| The relation is named but its conditions remain unclear. | State the condition that changes the reader's inference. |
| The reader reconstructs the relation and its relevant limits. | Keep it for that use; investigate a remaining uncertainty only when its answer can change the next move. |
| A change of viewpoint or order may conceal the relation. | Compare the changed passage and repair the particular loss. |

These are diagnostic situations. Use `NSTD.6` for a qualified evaluation rather than deriving a score from the presence of a support record.



#### NSTD.3:5.4 - Connecting to the relevant subject method


A connector does not settle the relation it expresses. “Because” can introduce a physical cause, a reason for acting or a mathematical dependence. Identify that relation first; open the corresponding FPF or subject method when the relation itself needs further work.

Suppose a design comparison says a proposed modular split removes one required hand-off between teams, but sends exceptional requests through a shared interface. The narrative can explain that change in dependency. Less routine coordination work is a prediction from the design; its realized cost remains unknown until observed. If observations are available, report the supported result rather than automatically weakening it to a prediction.

A science story can say that an experimental result "forced" a revised hypothesis only if the source line supports that constraint. Often the honest relation is weaker: the result made one hypothesis less useful, exposed a tension, or suggested a new mechanism to test. `NSTD.3` keeps the tension narratable while preventing the narrative from closing evidence that the source left open.

A live match commentary may connect a late midfield movement with lost possession. State the observed sequence separately from that provisional tactical explanation, and identify what the replay could resolve.

In a homotopy explanation, a deformation story may help learners track invariance, but it is not a proof by itself. The support record says which formal relation the story illustrates, what the learner should reconstruct, and where analogy must return to definitions or proof-status boundaries.

Use rewrite diagnostics when a sentence sounds good but may overclaim.

| Initial sentence | Source-support question | Replacement selected by the answer |
| --- | --- | --- |
| “The failed experiment revealed the true mechanism.” | Does the source identify the mechanism, rule out a prediction, or merely report a discrepancy? | If it reports only a discrepancy, state the measurement and prediction that disagree and leave the mechanism unresolved. If it establishes the mechanism, retain that conclusion and its supporting scope. |
| “The module split solved coordination.” | Does the source show a changed dependency, predict a cost effect or observe one? | For the proposed design above: “The split removes one required hand-off and routes exceptional requests through a shared interface. Its effect on coordination time has not yet been measured.” A measured reduction would warrant the corresponding observed claim. |
| “The character had no choice.” | Which alternatives do the fictional premises actually exclude? | If the scene establishes that both exits are locked and no other escape is available, say “With both exits locked, the character remained in the room.” If an alternative remains possible, describe the choice or pressure rather than inventing necessity. |
| “The proof idea is that loops remember holes.” | Which formal restriction or invariant does the image represent? | If the supplied definition requires a loop to remain in the punctured plane, explain that a deformation cannot pass through the missing point. Return to the argument for any claimed invariant; the image alone establishes no theorem. |
| “The team was outplayed because the press failed.” | Is this an observed cause, a provisional interpretation or a later supported analysis? | If the live source records late midfield movement followed by lost possession but no established cause, retain those observations and present the tactical connection as a hypothesis. Later analysis can justify a stronger claim; tentative wording is not compulsory once that support exists. |

These are conditional repairs, not substitutes to copy without their premises. For a supported strong case, suppose the mathematical source defines f(x) = 2x and the task supplies x = 3. “Under this definition, f(3) = 6” follows directly; weakening it to “perhaps 6” would lose the supported result. If the source instead contains only an input-output observation of 3 and 6, keep that observed pair and leave the general doubling rule unresolved. The words become no weaker or stronger than the supplied relation warrants.

If the repair makes the narrative less exciting, that is not automatically a defect. The repair preserves the source relation. Engagement can be rebuilt later through `NSTD.5` around the safer relation instead of by restoring the overclaim.

Optional notes for more involved comparisons:

```text
NarrativeEventMechanismSupport@ArchitectureTradeoff:
  sourceStructureKind: architecture-like and mechanism-like trade-off
  requiredReaderReconstruction: which required hand-off the proposed design removes, where exceptional requests go, and why an observed time saving remains unknown
  eventOrMechanismModel: ordinary requests no longer cross the removed hand-off; exceptional requests still require shared-interface coordination
  dependencyOrConstraintRefs: before-and-after dependency diagram; rule selecting exceptional requests; shared-interface responsibility
  supportingBasis: the stated design supports the dependency change and a conditional cost prediction; observed cost would need observations
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
  causalUseOwnerRef: none unless a causal learning claim is made
  uncertaintyOrUnknownRefs: analogy may fail outside named examples
  reconstructionTaskRefs: learner states where analogy stops and where proof returns
  sourceReturnCondition: formal source statement for proof or exercise use
```

```text
NarrativeEventMechanismSupport@LiveCommentary:
  sourceStructureKind: live event stream with provisional interpretations
  requiredReaderReconstruction: observed event vs inference vs prediction vs official correction
  eventOrMechanismModel: state updates and tactical hypothesis under uncertainty
  participatingHolonOrRoleRefs: teams, players, officials, broadcast or event source roles when needed
  uncertaintyOrUnknownRefs: off-camera events; later telemetry; official review
  reconstructionTaskRefs: listener can say what was observed and what was inferred
  sourceReturnCondition: official record, recording, statistics, or telemetry
```

These sketches illustrate information that can matter in different cases. Use only the fields needed to repair or compare the passage. A missing field does not by itself make a coherent account inadequate.

### NSTD.3:6 - Bias-Annotation

This pattern blocks fluent-coherence drift: smooth event language is mistaken for a mechanism, dependency, architecture, proof, or causal model. The bias appears when readers can retell the story but cannot reconstruct the selected source relation. Repair by naming the source-structure kind, the reconstruction target, the owner for causal or dependency claims, and the source-return condition. Scope: DPF-local for narrative coherence over selected source structure; it does not certify mechanism truth or causal evidence.

### NSTD.3:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD3-1` | The passage represents the relevant source relations without silently turning a dependency, constraint or proof step into a physical event. |
| `CC-NSTD3-2` | The intended reader can identify the connection needed for the stated use, or the remaining uncertainty is explicit. |
| `CC-NSTD3-3` | Claims of cause, dependency, necessity or motive have grounds suited to that claim; extra subject work is selected only where it can resolve a consequential question. |
| `CC-NSTD3-4` | An unknown, disputed or deferred relation remains visible when it affects the reader's conclusion or action. |
| `CC-NSTD3-5` | Learning or consequential use has a suitable way to check or recover the needed connection. A separate test or source note is selected for its value to that use. |

### NSTD.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Fluent but unsupported explanation | A passage invites an explanation that its source does not support. | Supply the missing connection, qualify it or return to the unresolved source question. |
| Causal overstatement | The narrative claims more about the cause than the grounds support. | State the supported causal strength; use `C.28` when its causal-use question needs work. Chronology is not a substitute causal explanation. |
| Event forcing | A graph, proof dependency, or architecture view is converted into fake events. | Name source structure kind and choose a better ordering rule through `NSTD.2`. |

### NSTD.3:9 - Consequences

The benefit is that narrative coherence becomes testable. The cost is that some dramatic simplifications must be weakened or paired with source return.

### NSTD.3:10 - Rationale

Narrative comprehension often depends on event models and causal schemas. FPF uses that strength but keeps event support distinct from causal evidence, mechanism truth, architecture evaluation, and proof status.

### NSTD.3:11 - SoTA-Echoing

Nguyen's [A Review of Mechanistic Models of Event Comprehension](https://arxiv.org/abs/2409.18992) (2024) compares accounts of prediction, hierarchy, updating and causal representation in comprehension. Hoffmann's [The Tensions of Scientific Storytelling](https://roaldhoffmann.com/sites/default/files/fromd6/Tensions%20ofScientific%20Storytelling%20as%20published.pdf) (2014) illustrates how scientific accounts organize mechanisms and unresolved tensions. Gatt and Krahmer's [NLG survey](https://arxiv.org/abs/1703.09902) (2018) distinguishes content selection and realization. This pattern's synthesis is to compare the connection the passage suggests with the relation its source or premises support.

Operational payload:

- Event-comprehension models motivate checking the reader's event boundaries, dependencies and predictions when those matter to the use. They do not establish that every reader builds the same model from every narrative.
- From scientific storytelling, unresolved tension is narratively useful. It must stay unresolved when the source is unresolved. A good story may preserve tension rather than close it.
- From NLG, inspect content as well as realization: a fluent connector cannot supply an omitted premise.
- For evidence, inference and causal claims, inspect the complete claim before selecting additional work. The occurrence of “shows”, “proves” or “because” alone does not require an assurance procedure.
- From architecture work, a mechanism-like story about structure must keep trade-offs, residual exceptions, and telemetry distinct. A before-and-after story is not by itself an architecture evaluation.

For a passage that implies an unsupported connection, the selected line is to inspect the event or dependency relation before polishing its connector. A serious alternative is local wording repair: replace “proved” by “suggested” or “caused” by “preceded”. At comparable effort on the one disputed sentence, that can be sufficient when it states what the source establishes; it fails when the weaker replacement also invents a fact. The incident case shows the decisive difference: retain the logged sequence and leave the cause unresolved instead of supplying a plausible mechanism.

**Adapt** event-model and content-planning distinctions in :4's source comparison and :5's diagnostics. **Adopt** scientific storytelling's use of unresolved tension: the next investigation can remain part of the account. The accepted cost is consulting the relevant source relation rather than guessing a safer-sounding sentence. Keep a strong conclusion when that source supports it. Reopen if a new observation or argument establishes the connection, if the intended use needs a different relation, or if the reader still infers more than the repaired passage supports.

### NSTD.3:12 - Relations

Uses `A.6.3.NAR`, `NSTD.2`, `C.28`, `A.10`, `B.3`, `C.2.8` for structural amount, `C.33` for architecture-description adequacy, `C.34`, `NSTD.6`, and `G.11`. Mechanism-support recovery can supply a `C.2.8` structural result through `NSTD.6`; the event-mechanism quality judgement retains its own meaning and evidence. Reopen when the source mechanism, causal support, reconstruction target, or evaluation result changes. Support-map entry: open `Architecture and Narrative Work Bridge` when event, mechanism, dependency, or coherence support is architecture-relevant; open `Source Use And Refresh Map` when a source or cognition claim supports reconstructability; open `NSTD.Reference:11 — Working meanings and direct source returns` when event, mechanism, coherence, support, or cause language starts doing evidence or quality work.

### NSTD.3:End
