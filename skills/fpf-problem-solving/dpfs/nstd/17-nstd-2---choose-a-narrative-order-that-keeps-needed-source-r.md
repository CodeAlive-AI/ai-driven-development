## NSTD.2 - Choose a Narrative Order That Keeps Needed Source Relations Recoverable

> **Status:** Stable

> **Type:** DPF pattern body

> **Purpose:** choose or assess a sequence that makes the source relations needed for the reader’s use recoverable.

### NSTD.2:1 - Problem frame

Use this method when the order of a narrative affects which relations a reader can recover from it. A graph, mechanism, body of evidence, plot, decision history or mathematical argument may support several orders. The question may be how to arrange new material or what an existing order makes available.

Locate the point where the reader has to interpret something or act. Read far enough on either side to see what is available then and what arrives later. A short passage may settle a local choice of order. If the conclusion depends on a reveal in a later episode, follow the account through that reveal. Clarify the relation or change the order when the task calls for revision.

A fluent sequence can invite an unsupported inference. The first event mentioned may look earliest, most important or causally decisive. A student may mistake the order of exposition for the order of proof, or a project team may mistake it for the order in which work was authorized.

A suitable order lets the intended reader follow the account and recover the dependencies the use requires.

### NSTD.2:2 - Problem

To present a tree, graph, mechanism, set of alternatives or architecture view in sequence, choose where to enter and which relations to show at each step. A sequence can expose one dependency while leaving another implicit. Check how the reader could recover each relation that matters for the purpose.

### NSTD.2:3 - Forces

| Force | Tension |
| --- | --- |
| Ease of following the account and fidelity to the source | A sequence can introduce a difficult relation gradually. It can also hide a branch or return that matters to the reader. |
| Teaching and formal dependency | A useful lesson can begin with an example whose full proof appears later. Make its status clear where the difference matters. |
| Suspense and prerequisites | An author can postpone the disclosure of a cause or a character’s means. Establish the prerequisites the events themselves require. |
| Compactness and access to detail | A short sequence can serve the immediate task. A consequential distinction it leaves out must be available by the time the reader relies on it. |

### NSTD.2:4 - Solution

Choose an order for the reader’s task or examine the existing one. At a consequential point, identify what the text has stated, which clues it has supplied and what can be inferred with the reader’s relevant prior knowledge. Compare the sequence with the source. If it obscures a needed relation, a short revision or usable source return may suffice. Use the note below when another worker or a later comparison needs the choices.

```text
NarrativeOrderingRule@Context:
  narrativeRenderingRef:
  sourceStructureRefs:
  unfoldingStructureRef?:
  demonstrativeSliceRef?:
  orderingRuleKind:
  orderRationale:
  preservedSourceRelations:
  foregroundedSourceRelations:
  coarsenedOrLostSourceRelations:
  sourceReturnCondition:
  additionalClaimReferences?:
```

A sequence can follow chronology, causal or logical dependency, discovery, teaching prerequisites, tension, viewpoint or the grounds for a decision. Choose the relation the account needs to foreground. Explain a departure when an otherwise plausible reading would confuse that order with another.

If the choice is unclear, compare the passage using the questions below.

| Test | Ask | If unclear |
| --- | --- | --- |
| Source relations | Which dependencies, cycles, alternatives or times does the intended use require? | Use a sufficient source directly. If the relevant selection is still unclear, use `NSTD.1` or try a provisional order to locate the missing relation. |
| First encounter | What should this passage show first, and what can a reader with the assumed preparation infer at that point? | Compare two short orders if the difference matters. Include expressive aims such as suspense when they are part of the use. |
| Hidden relations | Does the reader need a connection before it is disclosed? | Put it where the reader needs it or give a usable route to it in time. Keep a delayed disclosure if the earlier task can already be completed on its grounds. |
| Misreading | Which feature of this sequence could support a mistaken inference? | Where a correction is warranted, choose a sentence, marker or change of order that identifies the needed relation. |

Follow the inferences at the points where someone must use them. If a second reader has to act partway through the account, establish what is already available to that reader. A disclosure at the end may explain in retrospect an action that could not have been chosen on those grounds earlier. For an interpretation requested after the whole reading, use what is then available. A later disclosure can give grounds to revise an earlier interpretation. A whole story can also support several readings. Use NSTD.9 if those interpretations need developing or comparison. For a claim about what a particular reader understood, or when they understood it, use NSTD.6 with evidence from the relevant reading and point in time. An anticipated response is sufficient for planning its examination.

A lesson can introduce an example, recount the discovery that made a distinction interesting and then supply its proof. A live account can follow observed events in time, while a later recap examines causes. A story can show effects before revealing their cause. Make the transition recognizable when the reader’s task depends on which relation the order expresses. For a decision made before a later update, reconstruct when the fact was observed, when the decision holder could have received it and when the choice was made. A dated observation can establish what happened. A receipt or another warranted account of access can establish what was knowable to that actor. What reached the reader in the opening scene may have reached the actor only after the choice.

For a constraint-governed unfolding structure (CGUS), identify the path the account presents and preserve its applicable constraints. Show a branch, return, exit or stop when the reader needs it to explain what happened or determine what could happen. A demonstration of one path need not prescribe that sequence for future work.

The following difficulties can arise in a passage or appear in a reader’s response. Check the proposed explanation against the passage and the circumstances of the reading.

| Difficulty | Possible explanation | What to examine or change |
| --- | --- | --- |
| A reader takes the first-mentioned cause to be strongest. | Placement makes one cause salient. | Check the evidence for relative causal strength. If presentation invites the overreading, explain what the order shows or revise it. |
| Learners can retell the lesson but miss a formal exercise. | A story may have omitted a prerequisite or blurred example order and proof dependency. | Examine the task, the attempted reasoning and the available support. Restore the mathematical relation or the return to the proof when that is the missing contribution. |
| Stakeholders interpret the explanation as a sequence of decisions or work. | The passage may make an explanatory order look historical or prescriptive. | Identify the order the account intends. For an actual decision or implementation sequence, use the record of what happened. Use the plan for what was intended. |
| A reveal is well received, but a character lacked the means for an earlier action. | Delayed disclosure may conceal a gap in the events. | Check the selected canon or premises for the means at the time of the action. Revise the events if they lack it, or decide when to disclose existing support. |
| A generated story has plausible steps but drops a required source relation. | Generated sequence obscures its source constraint. | Compare the candidate with that relation; repair its plan or realization through `NSTD.7`. The defect can be evaluated before either is repaired. |

Use `NSTD.6` when the question calls for a qualified assessment of this sequence. A draft can already show that a dependency is missing or inaccessible. Report that limit, or repair the passage before using it for a purpose that needs the dependency.

### NSTD.2:5 - Archetypal Grounding



#### NSTD.2:5.1 - Worked example: choosing a path through a graph


A knowledge graph can connect concepts, dependencies, counterexamples, evidence and practices. Choose an order that makes the necessary relations available to the intended reader. The following example records such a choice for a homotopy introduction.

```text
NarrativeOrderingRule@HomotopyIntro:
  narrativeRenderingRef: HomotopyIntroNarrative@v1
  sourceStructureRefs:
    - topological space
    - path
    - deformation under constraints
    - invariant
    - example and counterexample
    - proof-status boundary
  orderingRuleKind: didactic prerequisite plus analogy-first cue
  orderRationale: an initial image can introduce the deformation question; the formal dependency must remain recoverable
  preservedSourceRelations: prerequisite relation; analogy-to-definition return; example-to-counterexample contrast
  foregroundedSourceRelations: deformation intuition and invariant question
  coarsenedOrLostSourceRelations: full proof order; advanced generality; categorical reformulation
  sourceReturnCondition: use the formal statement and proof when deciding a theorem, equivalence or proof claim
  additionalClaimReferences: `A.6.3.CSC`, `E.17.EFP`, `A.10`, `NSTD.6` when the corresponding claim is made
```

The introduction can begin with a picture of paths being deformed, then return to the definition. For example, “Picture one path being deformed into another while their endpoints stay fixed. The definition specifies which deformations are allowed.” The image gives the reader a candidate example. The definition supplies the conditions for a homotopy of paths relative to their endpoints.



#### NSTD.2:5.2 - Before and after repair: architecture order


Before:

> We tried several designs and eventually found the architecture that solved the coordination problem.

“Eventually” puts the attempts in time. “Solved” asserts a successful result. The sentence gives no basis for identifying the coordination problem, the accepted trade-off or the result after implementation.

After:

> Two services could each apply the eligibility rule locally, but would then have to keep their copies in step. We chose one eligibility service and accepted an extra call. Clients still need to handle an unavailable service and mismatched rule versions.

The revised account lets a reader compare rule maintenance with the cost and failure modes of a service call. A decision record can establish the grounds for the choice. Whether the deployed arrangement reduced coordination work depends on evidence from its use.



#### NSTD.2:5.3 - Before and after repair: live commentary


Before:

> The midfield is late, so the press has failed, and that is why the match is turning.

The timing of movement and loss of possession may be observable live. The cause of the loss and the projected direction of the match require further support.

After:

> The midfield line arrived after the forwards began pressing, leaving space between them. Did the opponent receive the ball in that space, or gain it in an individual challenge? A replay showing the passes, the challenge and the timing of possession might establish either contribution, show how both mattered or leave the cause open.

The account identifies the observed sequence and a specific remaining question about its cause.



#### NSTD.2:5.4 - Comparing candidate orders


| Observation | Next useful move |
| --- | --- |
| The sequence is readable but a necessary relation disappears. | Restore that relation or change the order. |
| The order has a name, but a reader reports a different dependency. | Check the passage and what informed the response. If the passage obscures the intended dependency, revise the wording or order. |
| The reader recovers the relations needed for this use. | The result supports the sequence for that reader under the observed conditions. Retain it where adequate. Consider a change if its expected contribution warrants the effort. |
| The route will be reused with changed material or audience preparation. | Check the condition that matters to transfer. Where sufficient evidence is already available, apply it. Where the changed use leaves a consequential question open, compare a representative case. |

Use `NSTD.6` when the task requires an evaluation of the order for a particular reader and use.



#### NSTD.2:5.5 - SoTA-to-action translation


Narratology distinguishes the selected material and story, discourse and presentation. Natural language generation distinguishes content selection, text planning and wording. In this task the distinctions help a writer compare what each version includes with where and how it presents that material. Smooth wording can still place a dependency where its use is unclear.

One teaching order for homotopy moves from spaces and paths to homotopy, the fundamental group, examples and questions about proof. An analogy can introduce a relation before its formal treatment. Identify where to find the definition or proof when the claim requires it. The order chosen for teaching by itself establishes neither historical discovery nor formal logical dependence.

In this constructed case two teams maintain the same validation rule in separate modules. They compare a library with a shared service and choose the service so that a rule change can be deployed once. They accept an extra service call and client handling of version mismatches. These are the decision and its anticipated consequences. The example supplies no runtime measurement.

Two short orders preserve the same source:

- **Cost first:** “The chosen service adds a call and requires version-mismatch handling. The teams accepted these costs to deploy a shared validation rule once, after comparing a library with a service. The runtime effect is not yet measured.”
- **Decision first:** “To deploy a shared validation rule once, the teams chose a service over a shared library. They accepted the extra call and version-mismatch handling; the runtime effect is not yet measured.”

For a new maintainer asking why the teams selected the service, the second version foregrounds the reason. For an investigation of the extra call, the first foregrounds the cost. A decision record can supply more detail about the alternatives. To report a realized improvement, use relevant measurements or observations.

A continuation can present scenes for suspense. Establish what the chosen events require in the story, including any necessary means, motive or prior event. The author can disclose those conditions later. If a twist contradicts a fixed premise, revise the event or change a premise the task permits changing. If the basis is uncertain, return to the selected canon.

A scientific account can build tension around a failed attempt, a surprising measurement and a revised hypothesis. If the explanation remains uncertain, keep the unresolved alternative in view. Identify the calculations, proposed mechanisms and experimental observations needed to check the resulting claims.

An architecture explanation can be repaired as follows.

1. Initial symptom: "The team first tried A, then B, and finally discovered the right architecture."
2. Identify the inference the sentence invites. It treats the last design in time as the right one.
3. Recover the relevant candidates, criteria, rejected alternatives and the decision basis or operating observations that actually exist.
4. Present the problem, alternatives and trade-off. Use a separate sequence if the implementation order matters.
5. Identify consequential omissions, such as a lower-level exception or an alternative outside the chosen scope.
6. Refer to the architecture description, candidate comparison or decision record for the particular structure, trade-off or authorized decision the reader needs.

For a mathematics lesson, the corresponding revision might run as follows.

1. Initial symptom: "We introduce homotopy with loops, then groups, then examples, because that is the natural story."
2. Identify what “natural” leaves unexplained. The intended order is for teaching. A reader might mistake it for the logical order of proof.
3. Identify the definitions, examples and theorem prerequisites on which the lesson relies. Establish where each proof claim can be checked.
4. Choose the teaching order. Make a divergence from formal dependency explicit when the reader needs to know it.
5. Say which formal details are deferred and where they can be recovered.
6. Use `NSTD.6` to assess whether the lesson makes the dependency and proof boundary recoverable or examine a learner’s response for what they actually recovered. Evaluate enjoyment separately when that too is an aim.

Case matrix for ordering work:

| Case | Candidate order | Preserves | Hides or weakens | Required source return |
| --- | --- | --- | --- | --- |
| FPF learning route | Entry difficulty, useful distinction, attempted application, result and continuation. | Pattern-use relationships and learner build-up. | Monolith order, advanced variants and source history. | Source pattern body; supporting definitions when needed. |
| Homotopy explanation | Teaching order, with an analogy before the formal proof. | An entry for learners and the relevant dependencies. | Full proof order, lemmas and advanced generality. | Formal statements and proofs, with the analogy’s limit. |
| Franchise continuation | Causal plot order plus reveal order. | Continuity, motivation, event consequence and return to the chosen canon. | Canon details outside this continuation's scope. | The selected canon and continuity constraints; a separate permission question only when the proposed use raises one. |
| Live commentary | Live chronological order plus provisional interpretation markers. | Event stream, uncertainty, listener orientation. | Later tactical recap, off-camera sources, official correction. | Official event record, telemetry, recording. |
| Architecture explanation | Decision-memory order or trade-off route. | Problem, candidate, selected trade-off, residual exception. | Implementation order, full structure, rejected-candidate detail. | Architecture description, candidate set, decision record, telemetry. |

Use the matrix to compare available orders, draft a passage or assess an existing sequence. A historical question about why the author chose one order needs evidence of that choice. A textual assessment can establish the structure of the published passage directly.

When two orders matter, preserve their distinct relations. A lesson can introduce prerequisites before recounting historical discovery. A mystery can present effects before their causes. A commentator can follow events in time and later explain a tactical sequence. Use a transition or source return where the intended reader needs to recognize the change of order.

### NSTD.2:6 - Bias-Annotation

A chronological, dramatic or slide order that feels natural to its author can hide a different relation in the source. Compare the chosen sequence with what it preserves, emphasizes or omits. Repair the account or provide a source return when the distinction matters. Formal serialization and the publication order of a corpus have their own purposes.

### NSTD.2:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD2-1` | The chosen sequence serves the reader's task; an explanation of its rule is available where the choice matters. |
| `CC-NSTD2-2` | The relations needed for the reader’s task are recoverable by the time they must be used. A later disclosure can complete a retrospective interpretation. |
| `CC-NSTD2-3` | Narrative order is not treated as physical time, proof order, work order, or decision authority without source support. |
| `CC-NSTD2-4` | If reliance calls for a return to the source, the reader can recognize the occasion and reach the pertinent material in time. |
| `CC-NSTD2-5` | Use `C.34` for architecture-specific preservation claims and `A.6.3.CSC` for a claimed coarsening. Use `C.2.8` through `NSTD.6` for reader-relative structural amount, and `C.33` for architecture-description adequacy. Ordinary source comparison needs no such additional claim. |

### NSTD.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Natural-order assumption | An obvious order for the author hides a dependency from the reader. | Recover the missing relation and change or explain the sequence. |
| Confusing tension with a prerequisite | A disclosure order is taken to determine what the events require. | Identify the prerequisite and choose where to reveal it. Provide a source return when the relation needs one. |
| Using slide order as evidence of source architecture | A teaching sequence is taken to establish how the source is organized. | Use the source to establish its structure and `NSTD.8` when a teaching route or its support needs attention. |

### NSTD.2:9 - Consequences

A well-chosen sequence can make a difficult subject easier to follow while preserving the relations needed for the reader’s purpose. Compare it with the source closely enough to identify consequential losses.

### NSTD.2:10 - Rationale

Both serialization and narrativization can choose an order for material whose relations have another structure. A narrative can additionally use a point of view, a revelation or an expressive pause. Locate any relation the chosen order obscures and preserve a route back to it when its loss could change the intended reading.

### NSTD.2:11 - SoTA-Echoing

Schmid's [Narratology: An Introduction](https://doi.org/10.1515/9783110226324) distinguishes happenings, story, narrative and presentation. Chihaia's [survey of narratology introductions](https://www.diegesis.uni-wuppertal.de/index.php/diegesis/article/view/71) shows differences of tradition and audience. These are historical conceptual anchors. Gatt and Krahmer's [NLG survey](https://arxiv.org/abs/1703.09902) distinguishes content selection from text structuring and realization. Cardona Rivera, Jhala, Porteous and Young's [The Story So Far on Narrative Planning](https://ojs.aaai.org/index.php/ICAPS/article/view/31509) examines plan-based construction and communication of stories. This pattern synthesizes those distinctions into an ordering method; it does not require a formal plan for every account.

These sources contribute distinct operations to the comparison.

- From Schmid, distinguish selection, composition and linearization. Well-chosen material may still be ordered badly, so compare `NSTD.2` ordering separately from `NSTD.1` selection.
- From Chihaia, interpret terms such as plot, discourse or fabula within the tradition using them. Explain the ordering consequence when different traditions use a term differently.
- From natural language generation, distinguish content choice, ordering and expression. If a reader misses a needed relation, inspect the supplied content as well as its order and wording.
- From narrative planning, distinguish the order of events from their presentation. Mark a divergence when it could mislead the reader about causality or dependency.
- For an architecture explanation, compare the account with the relevant structures and views. Use `C.30.ASV`, `C.33` or `C.34` only for the architecture question each defines.

For a short account of the incident in the Readme, try two versions. One can report the change at 14:00, failures at 14:02, rollback at 14:05 and recovery at 14:07. The other can use the same chronology and add that the log leaves open what caused the failures and whether the rollback produced the recovery. Choose the detail the reader needs to reconstruct the sequence or assess a causal claim.

Section 4 adapts the distinctions between content, structure and wording in natural language generation, and between events and their presentation in narrative planning. For an ordinary passage, a direct comparison of the relevant relations may suffice. For suspense or aesthetic rhythm, consider an order that serves that aim while preserving the relations the work needs. Reconsider the choice when the task changes, an observed difficulty concerns the order, or another equally economical arrangement would make the needed relations clearer.

### NSTD.2:12 - Relations

Use `A.6.3.NAR` for the source-to-narrative construction, `A.6.3.CSC` for a consequential simplification, and `NSTD.6` with `C.2.8` for correct recovery of selected structure from architecture or other sources. Use `C.33` for architecture-description adequacy and `C.34` for architectural preservation. `E.17` and `E.17.EFP` concern publication and explaining a source. If a proposed account overcommits, use `A.16.2` to reopen it, and `A.6.P` for an ambiguous relation. Use `G.11` when changed source, use or evidence puts an earlier assessment in question. The Architecture and Narrative Work Bridge covers ordering of views, candidates, decisions and evidence from realized structures. The Semiotic And Language-Precision Bridge and NSTD.Reference:11 help resolve consequential ambiguity in wording about simplification, relations and quality.

### NSTD.2:End
