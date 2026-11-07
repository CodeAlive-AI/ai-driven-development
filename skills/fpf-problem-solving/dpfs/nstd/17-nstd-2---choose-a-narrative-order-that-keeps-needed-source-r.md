## NSTD.2 - Choose a Narrative Order That Keeps Needed Source Relations Recoverable

> **Status:** Stable

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** choosing and repairing a narrative sequence so that the reader can follow the relations needed for the intended use.

### NSTD.2:1 - Problem frame

Use this pattern when a graph, mechanism, evidence set, architecture structure, candidate set, mathematical dependency structure, canon structure, or source tradition must be put into a sequence and the sequence changes what readers can recover.

First useful move: put a few connected items in a candidate order and compare the sequence with their source relations. If a reader could mistake presentation order for chronology, cause or prerequisite, mark the difference or change the order.

What goes wrong if missed: the order feels natural, but readers silently infer a different order kind: chronology, proof, causality, importance, decision order, work order, or moral priority.

What this buys: a readable path through the material that keeps important dependencies recoverable.

### NSTD.2:2 - Problem

Narrative is sequential. Many source structures are not. Trees, graphs, mechanism diagrams, dependency sets, option sets, proof dependencies, and architecture views must be traversed. A chosen order preserves some relations and hides others. If the ordering rule is implicit, a fluent sequence can misrepresent the selected source structure.

### NSTD.2:3 - Forces

| Force | Tension |
| --- | --- |
| Legibility vs structural fidelity | Linear order helps reading but cannot preserve every relation. |
| Teaching order vs source order | A good learning route may violate publication order or proof order. |
| Dramatic tension vs dependency truth | Suspense and reveal can hide prerequisites. |
| Compactness vs source return | The sequence needs to move, but hidden relations need return points. |

### NSTD.2:4 - Solution

Choose an order that serves the reader's task, try a short passage and check what it makes the reader infer. Revise the order or add a return to the source when an important relation is hidden. Use the following optional note when a maintained route, handover or comparison needs to retain the choices; an ordinary draft can express them directly.

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

Useful choices include chronology, causal or logical dependency, discovery, teaching prerequisites, tension, viewpoint and decision explanation. These are examples, not an exhaustive classification. A label helps only if the actual sequence shows the needed relation; explain a departure when the reader could otherwise infer the wrong one.

Choose the rule through a four-question ordering test.

| Test | Ask | If unclear |
| --- | --- | --- |
| Source structure | Which relations matter to this reader: for example dependencies, cycles, alternatives or chronology? | Inspect the needed source portion with `NSTD.1`; a provisional sequence may help expose the missing relation. |
| Reader traversal | What should the reader encounter first to do the intended work? | Try two short orders and compare what each makes easier to recover. Authorial and expressive aims can be part of that use. |
| Hidden relations | Which necessary relation becomes hidden or weaker in this order? | Restore it in the passage or provide a usable return to the source. |
| Misreading | Does a visible feature of this sequence invite a wrong inference? | Correct that inference with the smallest useful sentence, marker or change of order. |

Ordering can change interpretation even when it changes no event. Compare what the reader can infer at the relevant point and after the whole account. A later disclosure may legitimately revise an earlier reading; a final account may also sustain more than one supported reading. Use NSTD.9 when the alternatives themselves need to be constructed or compared. Do not call unresolved meaning an ordering failure merely because the reader cannot recover one predetermined answer.

An account can combine orders. A lesson may introduce prerequisites, use a discovery story to motivate a distinction, then return to a proof. A live account may follow observations chronologically and a later recap explain causes. A continuation may reveal effects before causes. Make the transition clear wherever the intended reader needs to distinguish those orders.

When the source describes a constraint-governed unfolding structure (CGUS), the narrative follows one traversal or demonstration. Preserve the constraints needed to interpret it. Show omitted alternatives, loops, exits or stop conditions when their omission would change the reader's choice or action; an illustrative path must not be mistaken for the only possible path or an instruction to execute every step.

Use this repair table when the narrative feels coherent but readers reconstruct the wrong structure.

| Symptom | Likely hidden order | Repair |
| --- | --- | --- |
| Readers think the first-mentioned cause is the strongest cause. | Salience order mistaken for causal order. | Mark salience as viewpoint or teaching order; return causal-strength claims to the evidence or source governing pattern. |
| Learners can retell the lesson but fail formal exercises. | Didactic story order mistaken for proof order. | Add proof-return checkpoints and separate example order from theorem dependency. |
| Stakeholders read the explanation order as the project decision sequence. | Explanation order mistaken for decision or work order. | State the order actually used; refer to the decision record or work plan when the reader needs that different sequence. |
| Fans like a reveal but continuity breaks. | Reveal order hides source canon constraints. | Add source-pack return and causal and continuity support before dramatic reveal. |
| A generated story has plausible steps but drops a required source relation. | Generated sequence obscures its source constraint. | Compare the candidate with that relation; repair its plan or realization through `NSTD.7`. The defect can be evaluated before either is repaired. |

Evaluate the sequence for its intended use through `NSTD.6`, including a draft whose order or source relationship is defective. If it conceals a critical dependency, repair that dependency before relying on the passage. A completed ordering note is not required to see the defect.

### NSTD.2:5 - Archetypal Grounding



#### NSTD.2:5.1 - Worked example: choosing a path through a graph


A knowledge graph can connect concepts, dependencies, counterexamples, evidence and practice routes. To introduce part of it, choose a traversal that helps the reader encounter the necessary dependencies. The optional example note below retains those choices for a homotopy introduction.

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
  orderRationale: learner needs visual intuition before formal return, but formal dependency must remain recoverable
  preservedSourceRelations: prerequisite relation; analogy-to-definition return; example-to-counterexample contrast
  foregroundedSourceRelations: deformation intuition and invariant question
  coarsenedOrLostSourceRelations: full proof order; advanced generality; categorical reformulation
  sourceReturnCondition: use the formal statement and proof when deciding a theorem, equivalence or proof claim
  additionalClaimReferences: `A.6.3.CSC`, `E.17.EFP`, `A.10`, `NSTD.6` when the corresponding claim is made
```

The introduction can begin with a picture of paths being deformed, then return to the formal definition. For example: "First picture a loop being deformed while its endpoints stay fixed. The next definition specifies which deformations are allowed." This connects the intuitive sequence to its missing mathematical condition.



#### NSTD.2:5.2 - Before and after repair: architecture order


Before:

> We tried several designs and eventually found the architecture that solved the coordination problem.

Failure: “eventually” supplies a chronology, while “solved” asserts a successful result. The account does not say which coordination problem was addressed, what trade-off was accepted or what observation supports success.

After:

> Begin with the coordination problem, compare the candidate module splits, then explain the chosen trade-off and remaining interface exceptions. Consult the decision record for why that split was selected and observations of the implemented system for whether it reduced coordination work.

What changed: the explanation connects the choice to its problem, alternatives and remaining cost. A reader seeking the implementation sequence or an observed outcome has a different source to consult.



#### NSTD.2:5.3 - Before and after repair: live commentary


Before:

> The midfield is late, so the press has failed, and that is why the match is turning.

Failure: live chronological observation is mixed with causal explanation and outcome projection. The source at that moment may support late movement and lost possession, but not a settled causal account.

After:

> The midfield line arrived after the forwards began pressing, leaving space between them. That gap may explain the lost possession; the replay can help distinguish this explanation from a missed individual challenge.

What changed: the observed sequence remains distinct from the provisional explanation, with a specific question for later review.



#### NSTD.2:5.4 - Comparing candidate orders


| Observation | Next useful move |
| --- | --- |
| The sequence is readable but a necessary relation disappears. | Restore that relation or change the order. |
| The order has a name but readers infer the wrong dependency. | Repair the passage itself; the label has not solved the problem. |
| The reader recovers the relations needed for this use. | Keep the sequence unless a worthwhile improvement is available. |
| The route will be reused with different material or readers. | Compare relevant changed cases; retain the conditions under which the order works. |

Use `NSTD.6` when a qualified quality result is needed.



#### NSTD.2:5.5 - SoTA-to-action translation


Narratology distinguishes selected material, story, discourse and presentation. Here those distinctions help the author separate what is included from the order in which it is encountered. NLG likewise distinguishes content selection, document planning and wording. A smooth sentence can still present a dependency in a misleading place.

A homotopy-theory explanation orders material by learner dependency: spaces, paths, homotopy, fundamental group, examples, proof-status boundaries. This is not the historical discovery order and not the formal proof order of a research monograph. The narrative must state that definitions and proof obligations remain in source-return formal statements.

Consider this constructed decision source: two teams maintain the same validation rule in separate modules. They compare a shared library with a shared service, then choose the service so that a rule change can be deployed once. They accept an extra service call and client handling of version mismatches. These are design expectations; runtime effects have not been measured.

Two short orders preserve the same source:

- **Cost first:** “The chosen service adds a call and requires version-mismatch handling. The teams accepted these costs to deploy a shared validation rule once, after comparing a library with a service. The runtime effect is not yet measured.”
- **Decision first:** “To deploy a shared validation rule once, the teams chose a service over a shared library. They accepted the extra call and version-mismatch handling; the runtime effect is not yet measured.”

For a new maintainer asking why the service was selected, the second order foregrounds the reason. For a reader investigating the added call, the first order foregrounds the relevant cost. Neither order supplies an observed improvement. Use the decision source for further alternative detail and measurements for a claim about the realized effect.

A franchise-continuation outline may order scenes by reveal and tension. That does not mean reveal order is causal order. The underlying causal and continuity order must still name premise constraint, character motivation, event cause, consequence, and canon-return point. If a later twist works only because a source constraint was hidden from the writer as well as from the reader, the order is not a legitimate reveal; it is a source-selection failure.

A scientific storytelling case may order experiments by tension: failed attempt, surprising measurement, revised hypothesis, unresolved conflict. That order can be useful because it mirrors inquiry, but it cannot make unresolved tension into evidence closure. The sequence must name which calculations, mechanisms, and experimental facts remain source-return points.

Worked repair sequence:

1. Initial symptom: "The team first tried A, then B, and finally discovered the right architecture."
2. Hidden-order diagnosis: chronology is being read as decision quality and finality.
3. Source topology repair: name candidate structures, quality characteristics, rejected alternatives, and telemetry or decision basis.
4. Ordering repair: present the problem, alternatives and trade-off; distinguish that explanation from the implementation sequence.
5. Loss repair: state what the narrative omits, such as lower-level exceptions or candidates excluded for scope.
6. Source-return repair: link to architecture description, decision record, or candidate comparison when a reader needs authority.

Second worked repair sequence:

1. Initial symptom: "We introduce homotopy with loops, then groups, then examples, because that is the natural story."
2. Hidden-order diagnosis: "natural story" hides the didactic prerequisite order and may be mistaken for formal proof order.
3. Source topology repair: list definitions, examples, theorem prerequisites, proof-status boundaries, and formal-source returns.
4. Ordering rule repair: choose didactic dependency order and explicitly state where it diverges from formal order.
5. Loss repair: record which formal details are deferred and where they return.
6. Evaluation repair: `NSTD.6` checks whether learners can reconstruct dependency and proof boundaries, not whether they enjoyed the story.

Case matrix for ordering work:

| Case | Candidate order | Preserves | Hides or weakens | Required source return |
| --- | --- | --- | --- | --- |
| FPF learning route | Entry difficulty, useful distinction, attempted application, result and continuation. | Pattern-use relationships and learner build-up. | Monolith order, advanced variants and source history. | Source pattern body; supporting definitions when needed. |
| Homotopy explanation | Didactic dependency order with analogy before formal proof. | Learner accessibility and dependency sequence. | Full proof order, all lemmas and advanced generalization. | Formal statements and proofs, with the analogy's boundary. |
| Franchise continuation | Causal plot order plus reveal order. | Continuity, motivation, event consequence and return to the chosen canon. | Canon details outside this continuation's scope. | The selected canon and continuity constraints; a separate permission question only when the proposed use raises one. |
| Live commentary | Live chronological order plus provisional interpretation markers. | Event stream, uncertainty, listener orientation. | Later tactical recap, off-camera sources, official correction. | Official event record, telemetry, recording. |
| Architecture explanation | Decision-memory order or trade-off route. | Problem, candidate, selected trade-off, residual exception. | Implementation order, full structure, rejected-candidate detail. | Architecture description, candidate set, decision record, telemetry. |

Use the matrix when comparing possible orders. It can guide a first draft or diagnose an existing passage. Reconstructing an earlier author's choices is useful for repair; judging the current sequence does not require establishing how it was originally written.

When two orders conflict, preserve both as named layers. A learning route may teach prerequisites first and later show historical discovery. A mystery-like story may reveal effects before causes while keeping an internal causal order. A live recap may reorder events by causal explanation after first recording live chronology. The reader must be told which layer they are following.

### NSTD.2:6 - Bias-Annotation

This pattern blocks natural-sequence drift: a chronological, didactic, dramatic, traversal, or slide order is treated as if it were the source structure itself. The bias is especially likely when the order feels intuitive to the author. Repair by naming the ordering rule, preserved relations, foregrounded relations, lost relations, and source-return condition. Scope: DPF-local for source-structure-to-sequence rendering; it does not govern general serialization formats or publication order.

### NSTD.2:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD2-1` | The chosen sequence serves the reader's task; an explanation of its rule is available where the choice matters. |
| `CC-NSTD2-2` | The relations needed for that use remain recoverable; consequential omissions are shown or have a source return. |
| `CC-NSTD2-3` | Narrative order is not treated as physical time, proof order, work order, or decision authority without source support. |
| `CC-NSTD2-4` | Source-return condition is present when lost relations affect action or reliance. |
| `CC-NSTD2-5` | Use `C.34` for architecture-specific preservation claims and `A.6.3.CSC` for a claimed coarsening. Use `C.2.8` through `NSTD.6` for reader-relative structural amount, and `C.33` for architecture-description adequacy. Ordinary source comparison needs no such additional claim. |

### NSTD.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Natural-order assumption | An obvious order for the author hides a dependency from the reader. | Recover the missing relation and change or explain the sequence. |
| Tension as dependency | Reveal order is read as prerequisite order. | Split dramatic order from dependency order and add source return. |
| Slide order as source structure | A teaching sequence is treated as the corpus architecture. | Route the teaching publication carrier through `NSTD.8` and keep source structure separate. |

### NSTD.2:9 - Consequences

The reader can follow a manageable path without losing a necessary relation. The author must spend enough attention comparing the sequence with the source to detect omissions that matter.

### NSTD.2:10 - Rationale

Narrative sequence is a transformation over structure. Making the ordering rule explicit preserves the useful similarity between serialization and narrativization: both choose an order for a structure, both preserve and lose relations, and both need a return path when the order is relied on.

### NSTD.2:11 - SoTA-Echoing

Schmid's [Narratology: An Introduction](https://doi.org/10.1515/9783110226324) distinguishes happenings, story, narrative and presentation. Chihaia's [survey of narratology introductions](https://www.diegesis.uni-wuppertal.de/index.php/diegesis/article/view/71) shows differences of tradition and audience. These are historical conceptual anchors. Gatt and Krahmer's [NLG survey](https://arxiv.org/abs/1703.09902) distinguishes content selection from text structuring and realization. Cardona Rivera, Jhala, Porteous and Young's [The Story So Far on Narrative Planning](https://ojs.aaai.org/index.php/ICAPS/article/view/31509) examines plan-based construction and communication of stories. This pattern synthesizes those distinctions into an ordering method; it does not require a formal plan for every account.

Operational payload:

- From Schmid, distinguish selection, composition and linearization. Well-chosen material may still be ordered badly, so compare `NSTD.2` ordering separately from `NSTD.1` selection.
- From Chihaia, interpret terms such as plot, discourse or fabula within the tradition using them. Explain the ordering consequence when different traditions use a term differently.
- From NLG, distinguish what to say from how to order and express it. Inspect the needed content when fluent realization leaves the reader's reconstruction incomplete.
- From narrative planning, distinguish the order of events from their presentation. Mark a divergence when it could mislead the reader about causality or dependency.
- For an architecture explanation, compare the account with the relevant structures and views. Use `C.30.ASV`, `C.33` or `C.34` only for the architecture question each defines.

For a short explanation whose reader must distinguish event order from cause or prerequisite, the best-supported line here is to keep those relations available while choosing the presentation order. The serious default is to preserve source order and improve only the prose. Compare two equally short accounts of the incident in the Readme: both retain the logged times, but the relation-aware account leaves the causal investigation open. Source order alone cannot expose that difference; the added comparison is justified by the reader's remedy decision, not by a preference for more elaborate planning.

**Adapt** the distinction between content, structure and realization from NLG, and between events and their communication from narrative planning, in :4's short-sequence comparison. **Reject** a required formal plan for an ordinary account: its cost is unnecessary when a few relations can be compared directly. For suspense or aesthetic rhythm, accept a different order when its effect matters and the needed relation remains available. Reopen this choice if a changed reader task requires another relation, if a reader repeatedly reconstructs the wrong order, or if an equally economical alternative preserves those relations more clearly.

### NSTD.2:12 - Relations

Uses `A.6.3.NAR`, `A.6.3.CSC`, `C.2.8` for structural amount, `C.33` for architecture-description adequacy, `C.34`, `E.17`, `E.17.EFP`, `A.16.2` when a route must back off or respecify after overcommitment, `A.6.P` when ordering rationale hides relation-kind claims, `NSTD.6`, and `G.11`. `NSTD.6` applies the same C.2.8 characteristic to narrative recovery from architecture and non-architecture source domains. Reopen when source structure, reader use, ordering rule, source-return condition, route authority, relation precision, or low `NSTD.6` ordering value changes. Support-map entry: open `Architecture and Narrative Work Bridge` when sequence is over architecture views, candidate structures, descriptions, correspondence, or actual-structure feedback; open `Semiotic And Language-Precision Bridge` or `NSTD.Reference:11 — Working meanings and direct source returns` when ordering terms hide coarsening, relation-kind, or quality claims.

### NSTD.2:End
