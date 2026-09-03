## E.10.MOVE - Move and Readiness Wording Precision Restoration

> **Type:** Part E precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative for move-like, movement-like, readiness-like, route-like, path-like, and trajectory-like wording-use restoration.

**At a glance.** `E.10.MOVE` restores the exact FPF value or relation hidden by move-like, movement-like, readiness-like, route-like, path-like, or trajectory-like wording. Its branches cover demonstrated continuation, prediction, readiness, and trajectory use. Recover the subject, posture, ordering, and representation needed to reach the direct owner; the pattern admits no generic Move or Trajectory head.

**Use this when.** After the normal `F.19` reading and compact `E.10` routing, use this pattern only while move-like, movement-like, readiness-like, route-like, path-like, or trajectory-like wording still hides the governed claim—for example, a demonstrated continuation, a prediction, readiness for a named Work, or an actual, planned, or modelled trajectory.

**Primary EntityOfConcern.** One wording-use restoration over a bounded text span whose move-like, movement-like, readiness-like, route-like, path-like, or trajectory-like wording has an FPF-governed use.

**First output.** Repaired wording, a truthful split, or a blocker. When later replay relies on the repair, use a temporary `MoveAndReadinessWordingRepairNote` that names the governed span, claim, object under repair, wording-use disposition, subject pattern, exact governed value and kind, relation signature when applicable, repaired wording or blocker, and remaining admissible reader use. A grounded non-use boundary is optional under `F.19`; it is not a required repair field.

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

**Cheap ordinary use.** When the governed value and its direct pattern are already evident, apply `F.19`, name the value, rewrite the phrase without changing the claim, confirm the remaining admissible reader use, and stop. Do not materialize the repair note or traverse the disposition table. Open the fuller procedure only when the wording remains ambiguous, carries several governed values, imports a source term, or must be replayed later.

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
  BlockedOverread?:
  SplitDisposition?:
  FinalWordingOrBlocker:
  RemainingReaderUse:
  QualificationWindow:
  CurrentnessBasis:
  ReopenCondition:
```

The governed-value ref and kind ref are both present or both absent. `BlockedOverread?` states a rejected reading and appears only when independent local evidence makes the exact rival reading plausible to the intended reader and deleting the boundary would change understanding, selection, safety, reliance, stop, or action. The relation-signature ref is present only when an admitted reusable typed declaration is current and the receiving use needs that declaration. Otherwise a relation claim names the admitted direct predicate and actual participants without a signature ref. A governed use has a non-semantic `SubjectPatternLocator`: an ordinary PatternID that identifies the pattern whose content defines, constrains, or tests the recovered value. Where the receiving claim needs a Method or MethodDescription, use the independent `A.3.1` and `A.3.2` conditions; admit any Method-use relation under its direct relation owner. For ordinary prose or quote-only use, the disposition explains why no FPF object is claimed; the corresponding object positions may remain absent. The `...Ref` fields carry references of the declared RefKinds; they do not carry the referenced values or kinds. A materialized note also states the edition, source, context, or time window in which the repair is relied on, the current pattern or source basis for that interpretation, and the smallest change that reopens it. Use `G.11` only when actual refresh orchestration is current; the note merely records its own currentness boundary. `FinalWordingOrBlocker` gives the wording or blocker for this bounded repair under its qualification and currentness conditions; a later change can reopen it. The note is a temporary wording-restoration aid; substantive results use their direct pattern's admission rules. Ordinary immediate repair need not materialize the note.

#### E.10.MOVE:4.2 - Trigger groups

After `E.10` selects this pattern, use these cue groups to find the appropriate recovery branch while an action-changing ambiguity remains:

- `move`, `step`, `action`, `application`, `solution`, and `next action`;
- `readiness`, `ready`, `full kit`, `work entry`, `committed`, and `launch-ready`;
- `movement`, `direction`, or `shift` used for an expected evaluation-result change;
- `route`, `workflow`, `process`, `path`, `trajectory`, `loop`, or `flow` used for an unresolved claim about a path, ordering, or what it represents; use the direct exits below;
- imported source wording such as TameFlow `MOVE`.

The cue group locates a recovery branch. The recovered claim and its direct owner determine the governed-value kind.

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

Recover the governed value and its subject pattern before closing a synonym replacement. Ordinary-prose or quote-only use closes when no FPF-governed value is claimed.

If responsibility is the remaining claim, name the admitted System, direct domain predicate, actual participants, and applicability, or return the exact A.6.RCD missing governor; an assignment is not a responsibility result. Individuate the responsibility-relation occurrence separately only when a named receiving use needs to distinguish that occurrence.

#### E.10.MOVE:4.2b - Trajectory wording recovery

Use this branch when *trajectory* or close path wording remains claim-bearing after any primary transformation wording has been recovered. The first result is an ordinary repaired claim or exact gap, not a trajectory record.

Ask only the questions the receiving use needs:

1. What exact bearer or represented subject is positioned or ordered?
2. What identity, continuity, membership, lineage, or edition rule matters?
3. Which declared position space, state space, configuration space, or possibility space and edition is relied on, if any?
4. What is the ordering or reference domain—time, event, generation, plan order, graph order, or another index?
5. What counts as a position, segment, branch, interval, generation, or edge for this use?
6. What posture does the claim need—for example, actual, observed, reconstructed, predicted, simulated, proposed, recommended, or planned?
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
| `boundedDemonstratedContinuation` | One E.11.PUA `PatternUsePracticeContinuationDescription@Context` shown inside a post-qualification demonstrative slice. A.22.CGUS supplies the structure and slice boundary, not a wrapper-row kind. Retain the complete bounded use and route any separate FPF-governed claim to its direct pattern. |
| `evaluationResultChangePrediction` | One E.23 `ExpectedEvaluationResultChange@Context` with evaluation pattern, coordinate, scale, current result, one expected value, range, or closed direction, proposal basis, and protected tradeoffs. |
| `directGovernedUse` | The exact governed value or relation, its kind, and its subject pattern. For a relation claim, name the admitted direct predicate and actual participants; include a `RelationSignature` reference only when an admitted reusable typed declaration is current and the receiving use needs it. The wording disposition itself contributes no project ontology. |
| `importedSourceWording` | Preserve the source expression only as source wording; recover every FPF use under its direct pattern. |
| `ordinaryProse` | Keep or lightly rewrite when no FPF-governed value is being asserted. |
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

Keep `mantra move` only when the sentence presents one E.11.PUA practice-continuation description inside a named post-qualification demonstrative slice. The description states its proposed use, expected result and kind, direct PatternID and name, current condition, and continuation disposition. That PatternID locates the applicable pattern. If the pattern choice is unresolved, the description may point to a separate nested selection question.

Selected fields of an optional note; include `BlockedOverread` only for an observed or independently grounded misreading:

```text
WordingUseDispositionValue: boundedDemonstratedContinuation
SubjectPatternLocator: E.11.PUA
RecoveredGovernedValueRef: PatternUsePracticeContinuationDescription@SeminarArchitectureUse
RecoveredGovernedValueKindRef: PatternUsePracticeContinuationDescription@Context
RetainedPlainWording: mantra move, only in the bounded CGUS-demonstrative context
BlockedOverread: this bounded source phrase does not license a `U.Move`, performed Work, or universal sequence in the demonstrated receiving use
RemainingReaderUse: inspect the shown candidate, Solution, expected result, and condition
QualificationWindow: the current E.11.PUA continuation description and the named A.22.CGUS demonstrative slice
CurrentnessBasis: the enclosing structure qualifies under A.22.CGUS, the slice shows this E.11.PUA description, and E.10.MOVE admits the bounded Plain wording
ReopenCondition: the enclosing structure or slice boundary changes, the E.11.PUA description changes, or readers use the phrase as Work, recommendation, or universal sequence
```

#### E.10.MOVE:5.2 - Expected evaluation-result change

Source sentence: "The repair should create an upward evaluation movement."

If the claim predicts a later evaluation result, restore the evaluation pattern, coordinate, scale, current result, one expected scale value, range, or closed direction, candidate proposal basis, and protected tradeoffs. Write the result as `ExpectedEvaluationResultChange@Context`. If those positions are unavailable, keep a provisional prediction description or use E.22 and E.23 to obtain the missing prediction basis.

#### E.10.MOVE:5.3 - Next FPF use

Source sentence: "The next FPF move is to check architecture."

If this is a project-local recommendation, restore `PatternUseRecommendation@Context` under `E.11.PUR` and cite the exact architecture pattern being recommended. With this sentence alone, the architecture, check question, and expected result remain unspecified. Return the blocker: "Specify which architecture is to be checked, which question the check must answer, and which result is required." Once those are known, the recommendation may say "next useful pattern use" and name the operation on that architecture and its expected result.

#### E.10.MOVE:5.4 - TameFlow `MOVE`

Source sentence: "The MOVE is full-kitted and ready."

Preserve `MOVE` as imported source wording. Restore the target WorkPlan or PlanItem, full-kit criterion, A.15.5 work-entry readiness result, and any actual gate decision under their direct patterns. Do not claim target Work occurred unless a dated A.15.1 occurrence is current.

#### E.10.MOVE:5.5 - Workflow diagram

Source sentence: "This workflow is the next move after problem framing."

If the diagram describes a transformation-flow structure or method description, use `A.3.4.P`, `E.18`, or `A.3.2`. If the sentence recommends the next pattern use, use `E.11.PUR`. If it demonstrates one continuation through a wider CGUS, use A.22.CGUS. Split the sentence when more than one claim is current.

For example, if the surrounding text identifies an admitted MethodDescription for heat-treating a shaft, the descriptive clause becomes: "This diagram describes the method for heat-treating the shaft." State any recommended next pattern use separately, with its object and expected result; return a blocker while those remain unspecified.

#### E.10.MOVE:5.6 - Evidence path

Source sentence: "Follow the evidence path to approval."

Recover the evidence or provenance relation under A.10. Identify separately the decision meant by *approval*: an applicable gate decision is governed by A.21; any authorization or commitment uses the pattern governing that exact relation.

#### E.10.MOVE:5.7 - Manufacturing operation

Source sentence: "The next move is to heat-treat the shaft."

If this names the reusable way of changing the shaft, recover the `U.Method` and its description under A.3.1 and A.3.2. If it places a heat-treatment operation in intended work, recover the WorkPlan or PlanItem under A.15.2. If heat treatment has occurred, recover the dated A.15.1 Work occurrence, affected shaft, method enactment, and result. If the question is whether that intended work can start, recover A.15.5 work-entry readiness. If the receiving context does not select among them, return the blocker: "Specify whether this describes the heat-treatment method, plans the work, reports completed heat treatment, or asks whether the planned work can start."

#### E.10.MOVE:5.8 - Clinical readiness

Source sentence: "The patient is ready for discharge."

When `ready` hides a patient-state claim, use A.19.SPR to recover the patient as bearer, the clinical state frame or subject pattern, the current value or classification, its evidence and qualification window, and the practical discharge use. A discharge recommendation, accountable decision, work-entry condition, and completed discharge remain different claims under their direct clinical and FPF patterns.

#### E.10.MOVE:5.9 - Reopen when a local mantra is not CGUS

Initial sentence: "The next mantra move is: name the thing."

An initial repair classified the phrase as `boundedDemonstratedContinuation`. Inspection then shows that the enclosing text is A.6.P's local RPR mantra: a short rendering of the A.6.P Solution. It has no qualifying wider `ConstraintGovernedUnfoldingStructure@Context`, no post-qualification `DemonstrativeUnfoldingSlice@Context`, and no E.11.PUA practice-continuation description with the required proposed use, expected result, pattern, condition, and disposition.

That evidence overturns the initial disposition. Remove the demonstrated-continuation claim, retain the local RPR mantra as Plain didactic wording, use the A.6.P Solution and its direct relation-recovery guidance, and write: "Apply the first clause of the local RPR mantra: name the thing; then recover the relation or comparison." The `A.6.P` locator and Solution establish neither a `U.Method` nor a `U.MethodDescription`. Establish a separate `U.Method`, a qualifying `U.MethodDescription` episteme, and any Method-use relation only if A.3.1 and A.3.2 independently admit them and the receiving claim depends on those identities. Reopen the demonstrative-slice question only if a later qualified structure and slice actually show a complete E.11.PUA practice-continuation description.

#### E.10.MOVE:5.10 - Trajectory under changing constraints

Source sentence from the R11 seminar guide *Development for Advanced*, section R11.5:12, edition for 1 February 2026, source blob `3dc4d26ad018c4587ee3ab55b849a1fe8068d25c`: «Для семинара это важный предшественник: архитекторы уже умеют мыслить не одним окончательным состоянием, а траекторией под изменяющимися ограничениями.» Working English gloss: “For the seminar this is an important predecessor: architects already know how to think not in one final state, but as a trajectory under changing constraints.”

Read the complete source span through `F.19` first. Keep the contrast with one final state only when a plausible intended reader has independent local grounds to expect that reading and rejecting it changes understanding or action. Otherwise state the positive claim directly—for example, “architects already know how to reason about a sequence of architecture changes under changing constraints.” When an FPF inference relies on the sentence, recover the exact architecture or system subject, the changing constraints and reference window, whether the sentence concerns actual architecture editions, a proposed evolution policy, or a modelled sequence, and the direct architecture, transformation, or model owner. For a C.29 curve or ordered rendering, name its correspondence to the architecture and the losses allowed by that use; establish transformation and evidence claims under their direct owners.

If the intended claim is only that evolutionary-architecture practice supports incremental changes under changing constraints, preserve the ordinary domain-practice wording and named source. Use A.3.1 and A.3.2 only when the receiving claim depends on an independently admitted Method or MethodDescription.

R11 is used here as a didactic source case of evolutionary architecture under changing constraints. For source refresh, reopen the worked slice only if the source claim meaning changes.

Overlap example: `The development trajectory improved.` Start with `E.10.DEV` to recover the developed subject and the basis of *improved*. Open this branch only when a separately relied-on ordered path, model, plan, or representation remains. A direct capability or organization-change claim may close without a second pass.

### E.10.MOVE:6 - Bias-Annotation

Lenses: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: FPF-governed move, readiness, route, path, and trajectory wording uses.

The method deliberately foregrounds Onto/Epist distinctions and direct subject ownership. The cheap ordinary-use path protects practical use and readability: recover only the distinctions that matter to the current claim and keep useful familiar wording. The concrete recurring misuses and their repairs are in §8.

### E.10.MOVE:7 - Conformance Checklist

| ID | A conforming repair... | Check |
| --- | --- | --- |
| `CC-E10MOVE-1` | names the governed text span, claim being made, and object under wording repair before choosing a replacement. | Resolve the kind from the current claim and its direct pattern. |
| `CC-E10MOVE-2` | assigns one wording-use disposition and does not treat that local enumeration as project ontology. | Demonstrated row, evaluation-result prediction, direct governed use, imported source wording, ordinary prose, and quotation cases remain distinct. |
| `CC-E10MOVE-3` | names the exact recovered governed value, value kind, and non-semantic PatternID locator for the subject pattern whose content defines, constrains, or tests that value. For a relation claim, it names the admitted direct predicate and actual participants; it includes a `RelationSignature` reference only when an admitted reusable typed declaration is current and the receiving use needs it. | Confirm the recovered project value under its direct pattern. Any relied-on MethodDescription identity needs independent A.3.2 admission, as in §4.1. |
| `CC-E10MOVE-4` | blocks root `U.Move`. | No durable move kind is minted by wording pressure. |
| `CC-E10MOVE-5` | preserves remaining reader use. | The repaired text still says what the practitioner can do or inspect next. |
| `CC-E10MOVE-6` | splits change-situation wording from pattern-use or readiness wording. | `A.3.4.P` and `E.10.MOVE` are both used when both objects are current. |
| `CC-E10MOVE-7` | avoids synonym tables. | Closure requires the recovered object and relation. |
| `CC-E10MOVE-8` | recovers the current trajectory claim, its direct owner or exact gap, and the remaining admissible reader use. It recovers bearer or represented subject, identity rule, ordering or reference domain, and posture only where those distinctions affect that claim or use; a grounded non-use boundary appears only when the `F.19` plausible-intended-reader test requires it. | Keep the subject, posture, ordering, and representation distinctions needed by the use; apply each direct owner's identity and evidence rules. |

#### E.10.MOVE:7.1 - Lowering and Reopen Conditions

Lower, block, or reopen the repair when the governed text span, claim being made, or object under wording repair is not recoverable, the wording-use disposition is uncertain, the proposed wording changes kind or relation without an accepted subject pattern, the subject pattern is missing, a change-situation claim was not separated from pattern-use or readiness wording, the repaired wording loses the remaining reader use, or changed source wording invalidates the recorded source-licensed use.

### E.10.MOVE:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Better use |
| --- | --- | --- |
| Synonym replacement | "Move" becomes "action" or "use" without recovered kind. | Recover governed text span, claim being made, object under wording repair, relation, and subject pattern first. |
| Imported MOVE kind | TameFlow source wording becomes FPF ontology. | Recover intended work, readiness, gate, preparation work, or performed work. |
| Readiness as gate passage | A ready label becomes `GateDecision=pass`. | Use A.21 only when gate fields are present. |
| Path as work-authorization route | Evidence path or source-reference path becomes a way to authorize work by resemblance. | Recover evidence relation, source relation, graph path, gate relation, work authorization, or deontic permission separately. |
| Local expression generalized | A bounded local phrase is generalized to unrelated project work. | Keep `mantra move` bound to one E.11.PUA practice-continuation description shown inside a post-qualification demonstrative slice; restore every other phrase through its own governed value and direct pattern. |
| Trajectory shell generalized | Ordered points, paths, plans, histories, lineages, and archive or front succession are treated as one world-side kind or Method. | Recover the direct claim and owner, then the subject, identity or continuity, reference order, posture, and receiving-use distinctions it needs; keep only a declared C.29 representation relation when that is the actual claim. |

### E.10.MOVE:9 - Consequences

Benefits:

- FPF keeps friendly move, readiness, route, path, and trajectory language without letting it mint false kinds.
- A trajectory sentence reaches its direct claim owner or exact gap. Subject, posture, ordering, and representation are recovered separately where the use needs them.
- Pattern-use recommendation, P2W, work readiness, gate decision, performed work, transformation, architecture, and call planning stay separable.
- Corpus cleanup can find move-headed debt without doing mechanical global renames.

Costs:

- Reliance-bearing or still-ambiguous phrases may need the small repair note before they can be rewritten safely; ordinary direct-pattern repair does not.
- Text may need to split one sentence into two governed claims when the original wording carried both change-situation and pattern-use meaning.

### E.10.MOVE:10 - Rationale

Familiar move, route, readiness, and trajectory wording can hide different governed claims. `E.10.MOVE` gives a narrow restoration path: recover the governed text span, claim, bearer or represented subject when relevant, posture, and object under wording repair; classify borrowed or ordinary wording; name the governed FPF value; preserve the remaining admissible reader use; and apply the pattern that defines or constrains that value.

The pattern is a child of E.10 because it starts as wording-use restoration and returns to the direct owner once the claim and remaining use are recovered. Its mantra branch routes an admitted demonstrative use through one A.22.CGUS and its E.11.PUA continuation description, a Plain local use to its bounded result's direct pattern, and a Plain long use to the subject pattern of the current map answer or stop. Evaluation-movement wording uses E.23 for a separate prediction about a later evaluation result.

The trajectory branch separates the subject from posture, ordering, and representation and returns to the subject pattern or exact gap. `E.10.DEV` coordinates only when development or evolution still carries an independent ambiguity. Recommendation, transformation, readiness, gate, publication, choice, plan, and Work claims remain with their direct patterns.

### E.10.MOVE:11 - SoTA-Echoing

The comparison separates direct-claim recovery, cue preservation, and imported source meanings.

| Practice question | Selected answer | Serious alternative or default and defect | Same-use effort and changed loci |
| --- | --- | --- | --- |
| When *route*, *path*, or *trajectory* still hides an action-changing distinction, which direct claim should the reader use? | Recover the subject or bearer, identity and continuity basis, ordering or position space, and posture needed by that use; then return to the direct owner or exact gap. | Warning-only treatment gives no positive route; a general Trajectory kind, account, relation, or Method merges unlike identities and evidence; representation-first treatment covers only a declared mathematical lens. | For the same claim and required result, clear wording exits immediately and unresolved wording opens only the relevant recovery branch. The rule changes `4.2b`, direct exits, `5.10`, `CC-E10MOVE-8`, consequences, and Relations. |
| When a familiar local or imported cue helps a reader find the intended use, should the cue be retained? | Retain bounded Plain or source wording while making the governed value and contextual sense explicit. | Mechanical replacement can erase a useful cue; lexical equivalence can hide different governed values. | One cue check accompanies the same repair and changes only the local-mantra, ordinary-use, and source-wording loci. |
| When TameFlow `MOVE`, Full-Kitting, or readiness wording is imported, what survives? | Preserve the source-practice designation and route intended Work, work-entry condition, gate, preparation Work, target Work, and value claims to their direct owners. | Universalizing the source vocabulary imports a local work-management ontology; stripping the label loses source return. | The bounded source slice adds one direct-owner split, changing the imported-source example and readiness exits without affecting ordinary trajectory cases. |

**Effort boundary.** Each clear case takes the cheap exit; an ambiguous case opens only the branch whose question is live. The deliberate cost is an honest exact gap when the subject or posture cannot be recovered.

| Source line | Contribution used here | Limitation and reopen condition |
| --- | --- | --- |
| FPF internal basis: `E.10`, `E.10.ARCH`, `A.6.P`, `A.6.RCD`, `A.3.4.P`, `A.19.SPR`, `A.22.CGUS`, `E.11.PUA`, `E.11.PUR`, and `E.23` | Use a trigger word as a cue to inspect the current claim; restore any unresolved governed value and relation before rewriting, preserve ordinary useful wording, and use the direct pattern for the final claim. | These patterns govern internal recovery rather than external empirical rank. Reopen only the affected slice when one changes the relevant kind settlement, authority boundary, or recovery fields. |
| Current `A.3.3`, `A.3.4`, `B.4`, `C.27.TA`, `C.29`, `C.17`–`C.19`, `C.36`, and `A.16.0`; Schaffter, Bounekkar, and Negre, [“Trajectory-Based Recommender Systems as Control Systems”](https://arxiv.org/abs/2606.22957), arXiv v1, 2026-06-22 | Supply direct internal owners and a serious domain case that preserves goal, state, model, action, and posture; the comparison informs the trajectory trigger, recovery questions, direct exits, exact-gap result, and no-general-head boundary. | The preprint is exploratory, synthetic, simplified, and specific to trajectory-based recommender systems. Reopen only if a later edition or serious rival supplies validated cross-domain structure that changes the subject, identity, ordering, posture, direct-owner, or general-head decision. Locator, publication-status, popularity, or unused-example changes alone do not reopen the pattern. Monitor at ordinary refresh intervals; use continuous monitoring only if this claim becomes both high-priority and volatile. |
| Zhu, Reinecke, and Mitra, [*Language Scent: Exploring Cross-Language Information Navigation*](https://arxiv.org/abs/2604.03604v2), arXiv v2, 2026-08-06 | Analogy for cue preservation: the study concerns query-language selection and proximal cues, with a laboratory study of 16 multilingual speakers. It motivates testing whether a familiar cue helps the current reader; the in-situ wording decision still uses `F.19`. | Cross-language navigation is the study's scope. Reopen the adopted cue hypothesis if broader evidence shows that a cue obscures the governed value or impedes the intended reader use. |
| Steve Tendon, [*The Book of TameFlow: Theory of Constraints Applied to Knowledge-Work Management*](https://leanpub.com/tameflow), publisher's contents accessed 2026-09-02; historical source context: Tendon, [*Constraints Everywhere*](https://tameflow.com/blog/2020-08-09/constraints-everywhere/), 2020 | The book supplies `MOVE` (Minimal Outcome-Value Effort) and Full-Kitting; the historical article distinguishes forward-looking preparation from current execution. These ground the source-practice distinctions among effort, outcome or value, constraint, and pre-entry preparation. | This line is scoped to knowledge-work management and is not a universal move or readiness ontology. Reopen if the used source meanings or FPF work, readiness, or gate patterns change their result boundaries. |

The selected line is FPF's direct-claim recovery. The external sources contribute a domain comparison, a cue-preservation hypothesis, and imported practice meanings; the R11 worked case is in §5.10.

### E.10.MOVE:12 - Relations

- **Builds on:** `F.19`, `E.10`, `E.10.ARCH`, `A.3.4.P`, `A.22.CGUS`, `E.11.PUA`, `E.11.PUR`, `E.23`, `A.15.5`, and `E.24`.
- **Coordinates with:** `E.11.PUA` for the `PatternUsePracticeContinuationDescription@Context` shown by a qualified practice continuation; `E.11.PUR` for `PatternUseCoordination@Context`, one `PatternUseOrderingRelation@Context`, or the bounded total-order `PatternUseSequence@Context`; `E.10.DEV` when development or evolution wording and trajectory wording carry independent ambiguities; `A.1.STM` for a non-CGUS system-thinking long-mantra map location; `A.3.3`, `A.3.4`, `A.3.4.P`, `B.4`, `C.27.TA`, `C.29`, `C.17`–`C.19`, `C.22.2`, `C.11`, A.15.2, `C.36`, and `A.16.0` for trajectory exits; and `E.18`, `E.18.1`, `A.15`, `A.21`, `C.24`, `C.30`, `E.17`, `F.17`, `F.18`, `G.11`, A.10, and each recovered value's direct subject pattern. `F.18` governs a durable-name decision; `G.11` governs refresh orchestration only when currentness, edition, telemetry, freshness, or decay is the actual claim.
- **Selected by:** E.10 compact routing when move, readiness, route, path, or trajectory wording still has an unresolved FPF-governed use after the `F.19` reading and no direct subject pattern has already resolved it.

### E.10.MOVE:End

