## E.10.MOVE - Move and Readiness Wording Precision Restoration

> **Type:** Part E precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative for move-like, movement-like, readiness-like, route-like, path-like, and trajectory-like wording-use restoration.

**At a glance.** `E.10.MOVE` restores the exact FPF value or relation hidden by move-like, movement-like, readiness-like, route-like, path-like, or trajectory-like wording. It preserves the demonstrated-continuation and readiness branches, distinguishes actual, modelled, proposed, planned, population, archive or search, mathematical-lens, and specialized-account uses where needed, and routes each additional claim to its direct owner; it admits no generic Move or Trajectory head.

**Use this when.** After the normal `F.19` reading and compact `E.10` routing, use this pattern only while move-like, movement-like, readiness-like, route-like, path-like, or trajectory-like wording still hides which demonstrated continuation, recommendation, prediction, transformation, ordered history, modelled path, plan, readiness claim or result, gate decision, publication relation, representation, or performed Work is current.

**Primary EntityOfConcern.** One wording-use restoration over a bounded text span whose move-like, movement-like, readiness-like, route-like, path-like, or trajectory-like wording has an FPF-governed use.

**First output.** Repaired wording, a truthful split, or a blocker. When later replay relies on the repair, use a temporary `MoveAndReadinessWordingRepairNote` that names the governed span, claim, object under repair, wording-use disposition, subject pattern, exact governed value and kind, relation signature when applicable, repaired wording or blocker, and reader use. A grounded non-use boundary is optional under `F.19`; it is not a required repair field.

**Not this pattern when.** Use `A.3.4.P` first when the wording is primarily about a transformation or change situation. Use `E.10.DEV` first when *development* or *evolution* still hides the changed subject, continuity or membership, or direction or value claim; continue here only if an independent trajectory, route, ordering, posture, or representation ambiguity remains. Use `F.19` and the direct subject pattern immediately when the current object is already known. Generic *process*, *workflow*, *loop*, or *flow* wording stays outside unless it independently carries one of the governed move, readiness, route, path, or trajectory claims.

### E.10.MOVE:1 - Problem Frame

"Move" is useful in project conversation. It can mean a chess-like next choice, a first FPF use, a TameFlow `MOVE`, an architecture candidate, a language-state transition, a call-planning next action, a work-preparation item, or an ordinary action. "Ready", "full kit", and "work entry" can likewise mean source currentness, work planning, preparation work, gate passage, or performed work.

The defect is not the word. The defect is letting that word choose the ontology. `E.10.MOVE` restores the object under wording repair and the direct FPF relation before any rewrite is accepted.

### E.10.MOVE:2 - Problem

Without this restoration:

1. FPF mints a false root `U.Move`.
2. Pattern-use recommendations become performed work or work authorization.
3. TameFlow `MOVE` is imported as if it were an FPF kind.
4. Readiness labels become gate passage or work occurrence by appearance.
5. Route, workflow, process, and path wording is repaired through taste rather than through the governed object.

### E.10.MOVE:3 - Forces

| Force | Pressure |
| --- | --- |
| Plain engineering language | Teams naturally ask for a next useful move or readiness result. |
| Kind safety | The same word may point to several different FPF values. |
| Practical payoff | A repair that removes "move" but hides what the user can do next has failed. |
| Neighboring-pattern discipline | Change-situation wording belongs to `A.3.4.P`; work, gates, publications, sources, architecture, and call planning have their own patterns. |
| Short cue set | The trigger list should be memorable and should not become an alias catalog. |

### E.10.MOVE:4 - Solution

**Cheap ordinary use.** When the governed value and its direct pattern are already evident, apply `F.19`, name the value, rewrite the phrase without changing the claim, confirm the reader use, and stop. Do not materialize the repair note or traverse the disposition table. Open the fuller procedure only when the wording remains ambiguous, carries several governed values, imports a source term, or must be replayed later.

Restore the governed target before choosing replacement wording:

1. Name the exact `GovernedTextSpan`, the `ClaimBeingMade`, and the `ObjectUnderWordingRepair`.
2. Decide whether the wording is ordinary prose, a quotation, or wording relied on for an FPF-governed claim. Ordinary and quotation uses can close without inventing a technical target.
3. When the phrase is `mantra move`, first ask which use is present. In a post-qualification A.22.CGUS demonstrative slice that shows pattern use, recover the exact E.11.PUA `PatternUsePracticeContinuationDescription@Context`: its proposed use, expected result and kind, PatternID and name, current condition, and continuation disposition. Keep `mantra move` only as bounded Plain wording for that shown continuation. A.22.CGUS supplies the structure and slice boundary; it does not create a universal displayed-row kind. For a Plain local mantra, name the bounded result and restore the move-like wording through that result's exact predicate or constraint. For a Plain long mantra, name the intended final result and the particular map location whose answer or stop is current, then state the exact answer or blocker and use the subject pattern only as a locator. Do not invent a demonstrated row, collapse the long map into one pattern's Solution, or treat any branch as Work order.
4. When `move`, `movement`, `direction`, or similar wording predicts a later evaluation result, recover `ExpectedEvaluationResultChange@Context` under `E.23`. That value is a coordinate-and-scale-qualified prediction episteme, not an operation, transition, movement, work occurrence, or proof of improvement.
5. For every other governed use, name the exact recovered value or relation, its kind, and its subject pattern. For a relation claim, name the admitted direct predicate and actual participants. Add a `RelationSignature` reference only when an admitted reusable typed declaration is current and the receiving use needs that declaration. If the governed value is already clear, use its pattern directly.
6. Split the text when one phrase carries more than one governed value. A recommendation, method, transformation, readiness claim or result, gate decision, publication relation, and performed Work do not become one value because the same word was used for them.
7. Preserve `RemainingReaderUse`: the repair is complete only when a practitioner can still tell what can be inspected, selected, evaluated, planned, performed, or returned to next.

#### E.10.MOVE:4.1 - MoveAndReadinessWordingRepairNote

```text
MoveAndReadinessWordingRepairNote:
  EncounteredWording:
  GovernedTextSpan:
  ClaimBeingMade:
  ObjectUnderWordingRepair:
  WordingUseDispositionValue: boundedDemonstratedContinuation | evaluationResultChangePrediction | directGovernedUse | importedSourceWording | ordinaryProse | quoteOnly
  SubjectPatternLocator?: PatternID, locating the pattern whose content defines, constrains, or tests the recovered value
  RecoveredGovernedValueRef?: U.EntityRef
  RecoveredGovernedValueKindRef?: U.KindRef
  RecoveredRelationSignatureRef?: U.EntityRef, referencing one RelationSignature
  RetainedPlainWording?:
  GroundedNonUseBoundary?:
  SplitDisposition?:
  RepairedWordingOrBlocker:
  RemainingReaderUse:
  QualificationWindow:
  CurrentnessBasis:
  ReopenCondition:
```

The governed-value ref and kind ref are both present or both absent. `GroundedNonUseBoundary?` appears only when independent local evidence makes the exact rival reading plausible to the intended reader and deleting the boundary would change understanding, selection, safety, reliance, stop, or action. The relation-signature ref is present only when an admitted reusable typed declaration is current and the receiving use needs that declaration. Otherwise a relation claim names the admitted direct predicate and actual participants without a signature ref. A governed use has a non-semantic `SubjectPatternLocator`: an ordinary PatternID that identifies the pattern whose content defines, constrains, or tests the recovered value. The locator creates no `U.Method`, `U.MethodDescription`, or Method-use relation. Ordinary prose and quote-only uses may leave those positions absent and record why no FPF object is being claimed. The `...Ref` fields carry references of the declared RefKinds; they do not carry the referenced values or kinds. A materialized note also states the edition, source, context, or time window in which the repair is relied on, the current pattern or source basis for that interpretation, and the smallest change that reopens it. Use `G.11` only when actual refresh orchestration is current; the note merely records its own currentness boundary. The note is a temporary wording-restoration aid, not a project result, method, plan, gate decision, or work occurrence. Ordinary immediate repair need not materialize the note.

#### E.10.MOVE:4.2 - Trigger groups

Run this restoration when one of these wording groups carries an FPF-governed use:

- `move`, `step`, `action`, `application`, `solution`, and `next action`;
- `readiness`, `ready`, `full kit`, `work entry`, and `launch-ready`;
- `movement`, `direction`, or `shift` used for an expected evaluation-result change;
- `route`, `workflow`, `process`, `path`, `trajectory`, `loop`, or `flow` used for an ordered history, prediction, proposed continuation, selected structure, transformation, Method, Work, gate, publication, decision, currentness, population or lineage, archive or front, or representation claim;
- imported source wording such as TameFlow `MOVE`.

The trigger group only opens the repair. It does not supply a replacement vocabulary or choose the governed-value kind.

##### E.10.MOVE:4.2.1 - Readiness exits

Stay in E.10.MOVE only while `readiness`, `ready`, `full kit`, `work entry`, or a similar cue still hides which governed value is meant. Once that value is recovered, use the direct pattern:

| Recovered claim | Direct pattern |
| --- | --- |
| A patient, system, or other subject has a value in a still-hidden state frame | `A.19.SPR`, then the subject pattern that defines or tests the recovered value. |
| An exact system-role assignment satisfies a by-value assignment-state condition | `A.2.5`; keep its predicate, world-side relation occurrence, and assertion episteme distinct. |
| One intended performance satisfies a work-entry criterion | `A.15.5`; its local readiness result is not a gate decision or performed target Work. |
| A distinct `OperationalGate(profile)` consumes declared checks and publishes a decision | `A.21`; a ready label or readiness result alone is not gate passage. |
| A publication use, permission claim, preparation Work, or target Work is meant | `E.17`, the direct permission pattern, or `A.15.1` as applicable. Keep each claim separate. |

If the direct pattern and value were already clear, bypass this table and use that pattern immediately.

#### E.10.MOVE:4.2a - No synonym closure

Replacing `move` with `step`, `action`, `use`, or `application` does not close the repair. Close only after recovering the governed value and its subject pattern. When responsibility is claimed, name the admitted System, direct domain predicate, actual participants, and applicability, or return the exact A.6.RCD missing governor; an assignment is not a responsibility result. Individuate the responsibility-relation occurrence separately only when a named receiving use needs to distinguish that occurrence. Ordinary-prose or quote-only use closes only when no FPF-governed value is claimed.

#### E.10.MOVE:4.2b - Trajectory wording recovery

Use this branch when *trajectory* or close path wording remains claim-bearing after any primary transformation wording has been recovered. The first result is an ordinary repaired claim or exact gap, not a trajectory record.

Ask only the questions the receiving use needs:

1. What exact bearer or represented subject is positioned or ordered?
2. What identity, continuity, membership, lineage, or edition rule matters?
3. Which declared position space, state space, configuration space, or possibility space and edition is relied on, if any?
4. What is the ordering or reference domain—time, event, generation, plan order, graph order, or another index?
5. What counts as a position, segment, branch, interval, generation, or edge for this use?
6. Is the posture actual, observed, reconstructed, predicted, simulated, proposed, recommended, or planned?
7. Which direct pattern owns the resulting claim, what receiving use is allowed, and is any grounded non-use boundary needed under the `F.19` plausible-intended-reader test?

These are recovery questions, not fields of a new `Trajectory`, `TrajectoryAccount`, relation head, Method, or mandatory card.

| Recovered trajectory use | Direct exit and boundary |
| --- | --- |
| Actual or reconstructed history of one identified subject | `A.3.4`, `A.3.4.P`, `B.4`, `C.27.TA`, and A.10 as applicable. A plotted sequence or intervention does not establish actual change or continuity. |
| Predicted or simulated state history | `A.3.3`, `A.19`, `C.27`, and `C.29`; name model edition, state space or position space, transition law, validity boundary, and posture. Model output is not actual history. |
| Proposed, recommended, or planned route | `C.22.2`, `C.11.CRC`, `C.11`, A.15.2, and the domain Method. Recommendation, choice, WorkPlan, performed Work, and effect remain separate. |
| Population or lineage history | `C.36` only for the cultural case; otherwise use an admitted domain owner or return the named non-cultural population or lineage architecture gap. Do not model membership turnover as one-holder continuity. |
| NQD/OEE search history, archive or front succession, or possibility-space projection | `C.17`–`C.19`, `G.5`, `G.11`, and `C.29` as applicable. An archive is not automatically a population. |
| Language-state move responsibility | `A.16.0` for its exact language-state bearer, position space, move lineage, branching, merging, or loss, and responsibility use. The specialized account is not a general template. |
| Mathematical trajectory lens | `C.29` for the selected representation and explicit correspondence, with declared losses; keep the represented subject under its direct owner. |
| Ordinary or quote-only wording | Preserve it and stop unless a later FPF use relies on a stronger claim. |

For *development trajectory*, open `E.10.DEV` first when the action-changing doubt is what develops, what remains identifiable, or whether improvement is asserted. Continue here only if trajectory still carries an independent claim about position, ordering, posture, or representation. If the bearer and development claim are already clear and only path posture is unresolved, start here and open `E.10.DEV` afterward only for a remaining separate ambiguity. Do not require two notes or two full passes by spelling alone.

#### E.10.MOVE:4.3 - Wording-use dispositions

`WordingUseDispositionValue` is a local finite enumeration for choosing a repair branch. It is not a U-kind, relation kind, state frame, or claim about the project value being repaired.

| `WordingUseDispositionValue` | Selected recovery |
| --- | --- |
| `boundedDemonstratedContinuation` | One E.11.PUA `PatternUsePracticeContinuationDescription@Context` shown inside a post-qualification demonstrative slice. A.22.CGUS supplies the structure and slice boundary, not a wrapper-row kind. Retain the complete bounded use and route any other current claim to its direct pattern. |
| `evaluationResultChangePrediction` | One E.23 `ExpectedEvaluationResultChange@Context` with evaluation pattern, coordinate, scale, current result, one expected value, range, or closed direction, proposal basis, and protected tradeoffs. |
| `directGovernedUse` | The exact governed value or relation, its kind, and its subject pattern. For a relation claim, name the admitted direct predicate and actual participants; include a `RelationSignature` reference only when an admitted reusable typed declaration is current and the receiving use needs it. The wording disposition itself contributes no project ontology. |
| `importedSourceWording` | Preserve the source expression only as source wording; recover every FPF use under its direct pattern. |
| `ordinaryProse` | Keep or lightly rewrite after recording that no FPF-governed value is being asserted. |
| `quoteOnly` | Preserve the quotation and its source-licensed use. State a grounded project-side non-use boundary only when that boundary changes the receiving use. |

#### E.10.MOVE:4.4 - Relation to A.3.4.P

Use `A.3.4.P` first when the claim is about a change situation or transformation-flow structure. Use `E.10.MOVE` only for the remaining wording-use question. If the same sentence also recommends a pattern use, claims readiness, or names a demonstrated continuation, split those claims and use its direct pattern for each.

#### E.10.MOVE:4.5 - Durable name repair

A durable name states the recovered subject value or relation; it does not retain an implementation head merely because the fields are typed.

| Misleading durable name | Repair |
| --- | --- |
| `localMoveLocus` | Name the exact local value or relation and its subject pattern. Do not preserve `locus` as a cross-pattern grouping head. |
| `ExpectedEvaluationMovement` | Use `ExpectedEvaluationResultChange@Context` only when the E.23 prediction positions are recoverable. |
| `FirstMoveRecord@Context` | Name the actual first result or relation governed by the direct pattern. |
| `Pattern-Use Sequence` | Use `PatternUseCoordination@Context` for the coordination judgement, `PatternUseOrderingRelation@Context` for one justified pairwise precedence relation inside it, and `PatternUseSequence@Context` only for the bounded total-order specialization under a named receiving use. Keep conversational coordination or ordering unmaterialized when no later reliance needs an addressable object. |

These are repair demonstrations, not a global replacement table.

### E.10.MOVE:5 - Archetypal Grounding - Worked Slices

#### E.10.MOVE:5.1 - Bounded `mantra move`

Source sentence: "The next mantra move is to compare the two patterns."

Keep `mantra move` only when the sentence presents one E.11.PUA practice-continuation description inside a named post-qualification demonstrative slice. The description states its proposed use, expected result and kind, direct PatternID and name, current condition, and continuation disposition. That PatternID is a locator; neither it nor the referenced Solution establishes a `U.Method` or `U.MethodDescription`. If the pattern choice is unresolved, the description may point to a separate nested selection question. The phrase does not claim a recommendation, method, work plan, performed work, or operation merely by being readable.

```text
WordingUseDispositionValue: boundedDemonstratedContinuation
SubjectPatternLocator: E.11.PUA
RecoveredGovernedValueRef: PatternUsePracticeContinuationDescription@SeminarArchitectureUse
RecoveredGovernedValueKindRef: PatternUsePracticeContinuationDescription@Context
RetainedPlainWording: mantra move, only in the bounded CGUS-demonstrative context
GroundedNonUseBoundary: this bounded source phrase does not license a `U.Move`, performed Work, or universal sequence in the demonstrated receiving use
RemainingReaderUse: inspect the shown candidate, Solution, expected result, and condition
QualificationWindow: the current E.11.PUA continuation description and the named A.22.CGUS demonstrative slice
CurrentnessBasis: the enclosing structure qualifies under A.22.CGUS, the slice shows this E.11.PUA description, and E.10.MOVE admits the bounded Plain wording
ReopenCondition: the enclosing structure or slice boundary changes, the E.11.PUA description changes, or readers use the phrase as Work, recommendation, or universal sequence
```

#### E.10.MOVE:5.2 - Expected evaluation-result change

Source sentence: "The repair should create an upward evaluation movement."

If the claim predicts a later evaluation result, restore the evaluation pattern, coordinate, scale, current result, one expected scale value, range, or closed direction, candidate proposal basis, and protected tradeoffs. Write the result as `ExpectedEvaluationResultChange@Context`. If those positions are unavailable, keep a provisional prediction description or use E.22 and E.23; do not call the phrase a completed move.

#### E.10.MOVE:5.3 - Next FPF use

Source sentence: "The next FPF move is to check architecture."

If this is a project-local recommendation, restore `PatternUseRecommendation@Context` under `E.11.PUR` and cite the exact architecture pattern being recommended. The final wording may say "next useful pattern use" in ordinary explanation, but it cannot imply performed architecture work or a root `U.Move`.

#### E.10.MOVE:5.4 - TameFlow `MOVE`

Source sentence: "The MOVE is full-kitted and ready."

Preserve `MOVE` as imported source wording. Restore the target WorkPlan or PlanItem, full-kit criterion, A.15.5 work-entry readiness result, and any actual gate decision under their direct patterns. Do not claim target Work occurred unless a dated A.15.1 occurrence is current.

#### E.10.MOVE:5.5 - Workflow diagram

Source sentence: "This workflow is the next move after problem framing."

If the diagram describes a transformation-flow structure or method description, use `A.3.4.P`, `E.18`, or `A.3.2`. If the sentence recommends the next pattern use, use `E.11.PUR`. If it demonstrates one continuation through a wider CGUS, use A.22.CGUS. Split the sentence when more than one claim is current.

#### E.10.MOVE:5.6 - Evidence path

Source sentence: "Follow the evidence path to approval."

Recover the evidence or provenance relation under A.10, any gate decision under A.21, and any authorization or commitment under the pattern governing that exact relation. A path description neither passes a gate nor authorizes work by resemblance.

#### E.10.MOVE:5.7 - Manufacturing operation

Source sentence: "The next move is to heat-treat the shaft."

If this names the reusable way of changing the shaft, recover the `U.Method` and its description under A.3.1 and A.3.2. If it places a heat-treatment operation in intended work, recover the WorkPlan or PlanItem under A.15.2. If heat treatment has occurred, recover the dated A.15.1 Work occurrence, affected shaft, method enactment, and result. If the question is whether that intended work can start, recover A.15.5 work-entry readiness. The short phrase does not decide which of these claims is current.

#### E.10.MOVE:5.8 - Clinical readiness

Source sentence: "The patient is ready for discharge."

When `ready` hides a patient-state claim, use A.19.SPR to recover the patient as bearer, the clinical state frame or subject pattern, the current value or classification, its evidence and qualification window, and the practical discharge use. A discharge recommendation, accountable decision, work-entry condition, and completed discharge remain different claims under their direct clinical and FPF patterns. Do not infer a discharge decision or performed discharge from the adjective alone.

#### E.10.MOVE:5.9 - Reopen when a local mantra is not CGUS

Initial sentence: "The next mantra move is: name the thing."

An initial repair classified the phrase as `boundedDemonstratedContinuation`. Inspection then shows that the enclosing text is A.6.P's local RPR mantra: a short rendering of the A.6.P Solution. It has no qualifying wider `ConstraintGovernedUnfoldingStructure@Context`, no post-qualification `DemonstrativeUnfoldingSlice@Context`, and no E.11.PUA practice-continuation description with the required proposed use, expected result, pattern, condition, and disposition.

That evidence overturns the initial disposition. Remove the demonstrated-continuation claim, retain the local RPR mantra as Plain didactic wording, use the A.6.P Solution and its direct relation-recovery guidance, and write: "Apply the first clause of the local RPR mantra: name the thing; then recover the relation or comparison." The `A.6.P` locator and Solution establish neither a `U.Method` nor a `U.MethodDescription`. Establish a separate `U.Method`, a qualifying `U.MethodDescription` episteme, and any Method-use relation only if A.3.1 and A.3.2 independently admit them and the receiving claim depends on those identities. Reopen the demonstrative-slice question only if a later qualified structure and slice actually show a complete E.11.PUA practice-continuation description.

#### E.10.MOVE:5.10 - Trajectory under changing constraints

Source sentence from the R11 seminar guide *Development for Advanced*, section R11.5:12, edition for 1 February 2026: «Для семинара это важный предшественник: архитекторы уже умеют мыслить не одним окончательным состоянием, а траекторией под изменяющимися ограничениями.» Working English gloss: “For the seminar this is an important predecessor: architects already know how to think not in one final state, but as a trajectory under changing constraints.”

Read the complete source span through `F.19` first. Keep the contrast with one final state only when a plausible intended reader has independent local grounds to expect that reading and rejecting it changes understanding or action. Otherwise state the positive claim directly—for example, “architects treat architecture as a sequence of changes under changing constraints.” When an FPF inference relies on the sentence, recover the exact architecture or system subject, the changing constraints and reference window, whether the sentence concerns actual architecture editions, a proposed evolution policy, or a modelled sequence, and the direct architecture, transformation, or model owner. A C.29 curve or ordered rendering may represent that history but does not identify the architecture, transformation, or evidence.

If the intended claim is only that evolutionary-architecture practice supports incremental changes under changing constraints, preserve the domain label and stop at the domain Method and named source. Do not mint `Trajectory`, infer an actual transformation, or require a recovery note.

Overlap example: `The development trajectory improved.` Start with `E.10.DEV` to recover the developed subject and the basis of *improved*. Open this branch only when a separately relied-on ordered path, model, plan, or representation remains. A direct capability or organization-change claim may close without a second pass.

### E.10.MOVE:6 - Bias-Annotation


- **Synonym-replacement bias.** Replacing "move" with "action", "step", or "use" can preserve the same hidden ontology. Recover concern, relation, and subject pattern before choosing wording.
- **Imported-source-kind bias.** TameFlow `MOVE`, workflow, route, process, or path wording can smuggle a source ontology into FPF. Treat such wording as a trigger until the direct FPF target is named.
- **Readiness-as-gate bias.** Ready, full-kit, committed, or launch-ready wording can overclaim gate passage, work authorization, or performed work.
- **Local-wording generalization bias.** One direct pattern may define a local move-like expression. That expression does not create a shared project kind; every other use still restores its own governed value and subject pattern.
- **Lexical-shell trajectory bias.** A curve, ordered list, state sequence, route, lineage, plan, or archive history can share trajectory spelling while preserving different subjects, identity rules, evidence, posture, and action. Recover the direct claim before proposing a shared head.

### E.10.MOVE:7 - Conformance Checklist

| ID | A conforming repair... | Check |
| --- | --- | --- |
| `CC-E10MOVE-1` | names the governed text span, claim being made, and object under wording repair before choosing a replacement. | The word itself does not choose the ontology. |
| `CC-E10MOVE-2` | assigns one wording-use disposition and does not treat that local enumeration as project ontology. | Demonstrated row, evaluation-result prediction, direct governed use, imported source wording, ordinary prose, and quotation cases remain distinct. |
| `CC-E10MOVE-3` | names the exact recovered governed value, value kind, and non-semantic PatternID locator for the subject pattern whose content defines, constrains, or tests that value. For a relation claim, it names the admitted direct predicate and actual participants; it includes a `RelationSignature` reference only when an admitted reusable typed declaration is current and the receiving use needs it. | A wording disposition, neighbor list, or optional declaration apparatus cannot stand in for the recovered project value; the locator does not type the pattern or its Solution as `U.MethodDescription`. |
| `CC-E10MOVE-4` | blocks root `U.Move`. | No durable move kind is minted by wording pressure. |
| `CC-E10MOVE-5` | preserves remaining reader use. | The repaired text still says what the practitioner can do or inspect next. |
| `CC-E10MOVE-6` | splits change-situation wording from pattern-use or readiness wording. | `A.3.4.P` and `E.10.MOVE` are both used when both objects are current. |
| `CC-E10MOVE-7` | avoids synonym tables. | The repair recovers object and relation, not a preferred vocabulary list. |
| `CC-E10MOVE-8` | treats trajectory as a trigger and recovers bearer or represented subject, identity rule, ordering or reference domain, posture, direct owner, and receiving use; it adds a grounded non-use boundary only when the `F.19` plausible-intended-reader test requires one. | Actual, modelled, proposed, planned, population or lineage, archive or search, mathematical-lens, and specialized-account claims do not inherit one another's identity or evidence. |

#### E.10.MOVE:7.1 - Lowering and Reopen Conditions

Lower, block, or reopen the repair when the governed text span, claim being made, or object under wording repair is not recoverable, the wording-use disposition is uncertain, the proposed wording changes kind or relation without an accepted subject pattern, the subject pattern is missing, a change-situation claim was not separated from pattern-use or readiness wording, the repaired wording loses the reader use, or changed source wording invalidates the recorded source-licensed use.

### E.10.MOVE:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Better use |
| --- | --- | --- |
| Synonym replacement | "Move" becomes "action" or "use" without recovered kind. | Recover governed text span, claim being made, object under wording repair, relation, and subject pattern first. |
| Imported MOVE kind | TameFlow source wording becomes FPF ontology. | Recover intended work, readiness, gate, preparation work, or performed work. |
| Readiness as gate passage | A ready label becomes `GateDecision=pass`. | Use A.21 only when gate fields are present. |
| Path as work-authorization route | Evidence path or source-reference path becomes a way to authorize work by resemblance. | Recover evidence relation, source relation, graph path, gate relation, work authorization, or deontic permission separately. |
| Local expression generalized | A bounded local phrase is generalized to unrelated project work. | Keep `mantra move` bound to one E.11.PUA practice-continuation description shown inside a post-qualification demonstrative slice; restore every other phrase through its own governed value and direct pattern. |
| Trajectory shell generalized | Ordered points, paths, plans, histories, lineages, and archive or front succession are treated as one world-side kind or Method. | Recover the exact subject, identity or continuity, reference order, posture, direct owner, and receiving use; keep only a declared C.29 representation relation when that is the actual claim. |

### E.10.MOVE:9 - Consequences

Benefits:

- FPF keeps friendly move, readiness, route, path, and trajectory language without letting it mint false kinds.
- A trajectory sentence can return an actual, modelled, proposed, planned, population or lineage, archive or search, mathematical-lens, specialized-account, ordinary, or blocked claim instead of a generic trajectory record.
- Pattern-use recommendation, P2W, work readiness, gate decision, performed work, transformation, architecture, and call planning stay separable.
- Corpus cleanup can find move-headed debt without doing mechanical global renames.

Costs:

- Reliance-bearing or still-ambiguous phrases may need the small repair note before they can be rewritten safely; ordinary direct-pattern repair does not.
- Text may need to split one sentence into two governed claims when the original wording carried both change-situation and pattern-use meaning.

### E.10.MOVE:10 - Rationale

Move-, route-, readiness-, and trajectory-like wording is too useful to ban and too ambiguous to leave ungoverned. `E.10.MOVE` gives a narrow restoration path: recover the governed text span, claim, bearer or represented subject when relevant, posture, and object under wording repair; classify borrowed or ordinary wording; name the governed FPF value; preserve reader use; and apply the pattern that defines or constrains that value.

Use this wording restoration when move-, readiness-, route-, path-, or trajectory-like language still hides the claim a practitioner must inspect or use. The mantra and readiness branches retain their direct owners. The trajectory branch preserves ordinary wording, separates actual, modelled, proposed, planned, population, archive, and representation postures, and returns to the subject pattern or exact gap. `E.10.DEV` coordinates only when development or evolution still carries an independent ambiguity. Recommendation, transformation, readiness, gate, publication, choice, plan, and Work claims remain with their direct patterns.

### E.10.MOVE:11 - SoTA-Echoing

The pattern uses three bounded practice questions; their sources do different jobs and do not collectively establish one trajectory ontology.

| Practice question | Selected answer | Serious alternative or default and defect | Comparable effort and changed loci | Source role, limit, and smallest reopen |
| --- | --- | --- | --- | --- |
| When *route*, *path*, or *trajectory* is relied on, what smallest recovery distinguishes actual history, a modelled future, proposal, plan, population or lineage, archive or search record, representation, specialized account, ordinary wording, or exact gap? | Recover subject or bearer, identity and continuity basis, ordering or position space, posture, and direct owner before interpreting the wording. | Warning-only treatment gives no positive route; a general Trajectory kind, account, relation, or Method merges unlike identities and evidence; representation-first treatment covers only a declared mathematical lens. | Clear wording exits immediately; an ambiguous phrase takes one short pass instead of searching several subject neighborhoods. It changes `4.2b`, direct exits, `5.10`, `CC-E10MOVE-8`, consequences, and Relations. | Current FPF patterns govern the direct owners; TBRS is one serious domain case. Reopen only if validated cross-domain structure changes the required subject, identity, ordering, posture, direct owner, or general-head decision. |
| When a familiar local or imported cue helps a reader find the intended use, should the cue be retained? | Retain bounded Plain or source wording while making the governed value and contextual sense explicit. | Mechanical replacement can erase a useful cue; lexical equivalence can hide different governed values. | One cue check accompanies the same repair and changes only the local-mantra, ordinary-use, and source-wording loci. | The language-scent study informs cue preservation but does not define FPF ontology. Reopen if broader evidence shows the cue obscures the governed value or impedes the intended reader use. |
| When TameFlow `MOVE`, Full-Kitting, or readiness wording is imported, what survives? | Preserve the source-practice designation and route intended Work, work-entry condition, gate, preparation Work, target Work, and value claims to their direct owners. | Universalizing the source vocabulary imports a local work-management ontology; stripping the label loses source return. | The bounded source slice adds one direct-owner split, changing the imported-source example and readiness exits without affecting ordinary trajectory cases. | TameFlow supplies source-practice meaning only. Reopen if its current edition changes the used terms or if FPF work, readiness, or gate patterns change their result boundary. |

**Comparable-effort conclusion.** Each clear case takes the cheap exit; each ambiguous case opens only the row whose question is live. The deliberate cost is an honest exact gap when the subject or posture cannot be recovered.

| Source line | Contribution used here | Limitation and reopen condition |
| --- | --- | --- |
| FPF internal basis: `E.10`, `E.10.ARCH`, `A.6.P`, `A.6.RCD`, `A.3.4.P`, `A.19.SPR`, `A.22.CGUS`, `E.11.PUA`, `E.11.PUR`, and `E.23` | Treat a trigger word as evidence of a recovery problem, restore the governed value and relation before rewriting, preserve ordinary useful wording, and use the direct pattern for the final claim. | These patterns govern internal recovery rather than external empirical rank. Reopen only the affected slice when one changes the relevant kind settlement, authority boundary, or recovery fields. |
| Current `A.3.3`, `A.3.4`, `B.4`, `C.27.TA`, `C.29`, `C.17`–`C.19`, `C.36`, and `A.16.0`; Schaffter, Bounekkar, and Negre, [“Trajectory-Based Recommender Systems as Control Systems”](https://arxiv.org/abs/2606.22957), arXiv v1, 2026-06-22 | Supply direct internal owners and a serious domain case that preserves goal, state, model, action, and posture; these mutate the trajectory trigger, recovery fields, direct exits, exact-gap result, and no-general-head boundary. | The preprint is exploratory, synthetic, simplified, and specific to trajectory-based recommender systems. Reopen only if a later edition or serious rival supplies validated cross-domain structure that changes the subject, identity, ordering, posture, direct-owner, or general-head decision. Locator, publication-status, popularity, or unused-example changes alone do not reopen the pattern. Monitor at ordinary refresh intervals; use continuous monitoring only if this claim becomes both high-priority and volatile. |
| Zhu, Reinecke, and Mitra, [*Language Scent: Exploring Cross-Language Information Navigation*](https://arxiv.org/abs/2604.03604), arXiv:2604.03604, 2026 preprint | Supports retaining recognizable in-situ wording while keeping contextual sense and governed value explicit. | The study is small and cross-language; it establishes neither FPF ontology nor universal cue success. Reopen if larger evidence changes the cue's usefulness for the intended readers. |
| Steve Tendon, [*The Book of TameFlow: Theory of Constraints Applied to Knowledge-Work Management*](https://leanpub.com/tameflow), current Leanpub edition accessed 2026-07-11; Tendon, [*Constraints Everywhere*](https://tameflow.com/blog/2020-08-09/constraints-everywhere/), 2020 | Supplies the source-practice meanings of `MOVE` and Full-Kitting and the distinctions among effort, outcome or value, constraint, and pre-entry preparation. | This line is scoped to knowledge-work management and is not a universal move or readiness ontology. Reopen if the used source meanings or the FPF work and readiness boundaries change. |
| R11, *Development for Advanced*, seminar-guide edition for 1 February 2026, section R11.5:12 | Supplies the source case of evolutionary architecture as a trajectory under changing constraints and its explicit architecture subject. | It is a didactic source case, not rank evidence or a general trajectory kind. Reopen the worked slice only if the source claim meaning changes. |

The current best problem-solving line for trajectory wording is the FPF recovery architecture. The other source lines sharpen one domain comparison, cue preservation, imported vocabulary, or worked case; none assigns a general FPF kind.

### E.10.MOVE:12 - Relations

- **Builds on:** `F.19`, `E.10`, `E.10.ARCH`, `A.3.4.P`, `A.22.CGUS`, `E.11.PUA`, `E.11.PUR`, `E.23`, `A.15.5`, and `E.24`.
- **Coordinates with:** `E.11.PUA` for the `PatternUsePracticeContinuationDescription@Context` shown by a qualified practice continuation; `E.11.PUR` for `PatternUseCoordination@Context`, one `PatternUseOrderingRelation@Context`, or the bounded total-order `PatternUseSequence@Context`; `E.10.DEV` when development or evolution wording and trajectory wording carry independent ambiguities; `A.1.STM` for a non-CGUS system-thinking long-mantra map location; `A.3.3`, `A.3.4`, `A.3.4.P`, `B.4`, `C.27.TA`, `C.29`, `C.17`–`C.19`, `C.22.2`, `C.11`, A.15.2, `C.36`, and `A.16.0` for trajectory exits; and `E.18`, `E.18.1`, `A.15`, `A.21`, `C.24`, `C.30`, `E.17`, `F.17`, `F.18`, `G.11`, A.10, and each recovered value's direct subject pattern.
- **Selected by:** E.10 compact routing when move, readiness, route, path, or trajectory wording still has an unresolved FPF-governed use after the `F.19` reading and no direct subject pattern has already resolved it.

### E.10.MOVE:End

