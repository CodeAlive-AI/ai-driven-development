## E.10.MOVE - Move and Readiness Wording Precision Restoration

> **Type:** Part E precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative for move-like and readiness-like wording-use restoration.

**At a glance.** `E.10.MOVE` restores the exact FPF value or relation hidden by move-like, movement-like, and readiness-like wording. It keeps bounded Plain `mantra move` only for one A.22.CGUS demonstrated row, restores evaluation-result change wording to an E.23 prediction, and returns every stronger claim to its direct governing pattern.

**Use this when.** Use this pattern when wording such as move, movement, step, action, readiness, route, workflow, or process is doing more than ordinary prose and a reader could mistake a demonstrated continuation, recommendation, prediction, transformation, readiness relation, gate decision, publication relation, or performed work for another kind.

**Primary EntityOfConcern.** One wording-use restoration over a bounded text span whose move-like or readiness-like wording has an FPF-governed use.

**First output.** One accepted wording repair, split, or blocker. When later replay relies on the repair, use a temporary `MoveAndReadinessWordingRepairNote` that names the governed span, claim, object under repair, wording-use disposition, direct governing pattern, exact governed value and kind, relation signature when applicable, blocked overread, final wording or blocker, and remaining reader use.

**Not this pattern when.** Use `A.3.4.P` first when the wording is primarily about transformation, flow, path, process, workflow, operation, or change as a change-situation label. Use the direct governing pattern immediately when the current object is already known and no move-like or readiness-like wording problem remains.

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

**Cheap ordinary use.** When the governed value and its direct pattern are already evident, name them, rewrite the phrase without changing the claim, confirm the remaining reader use, and stop. Do not materialize the repair note or traverse the disposition table. Open the fuller procedure only when the wording remains ambiguous, carries several governed values, imports a source term, or must be replayed later.

Restore the governed target before choosing replacement wording:

1. Name the exact `GovernedTextSpan`, the `ClaimBeingMade`, and the `ObjectUnderWordingRepair`.
2. Decide whether the wording is ordinary prose, a quotation, or wording relied on for an FPF-governed claim. Ordinary and quotation uses can close without inventing a technical target.
3. When the phrase is `mantra move`, first determine whether the local mantra has been admitted by `A.22.CGUS` as a `DemonstrativeUnfoldingSlice@Context`. If so, recover one `DemonstratedPatternUseRow@Context` and keep the phrase only when the enclosing slice, EntityOfConcern, practical-use question, public template or project candidate, direct pattern, Solution, expected result, and current condition are recoverable. If not, keep the local mantra as a compact rendering of its pattern's Solution and repair the move-like wording through that direct pattern rather than inventing a demonstrated row.
4. When `move`, `movement`, `direction`, or similar wording predicts a later evaluation result, recover `ExpectedEvaluationResultChange@Context` under `E.23`. That value is a coordinate-and-scale-qualified prediction episteme, not an operation, transition, movement, work occurrence, or proof of improvement.
5. For every other governed use, name the exact recovered value or relation, its kind, relation signature when the kind admits a relation, and its direct governing pattern. If that governed value is already clear, use its pattern directly.
6. Split the text when one phrase carries more than one governed value. A recommendation, method, transformation, readiness relation, gate decision, publication relation, and performed work do not become one value because the same word was used for them.
7. Preserve `RemainingReaderUse`: the repair is complete only when a practitioner can still tell what can be inspected, selected, evaluated, planned, performed, or returned to next.

#### E.10.MOVE:4.1 - MoveAndReadinessWordingRepairNote

```text
MoveAndReadinessWordingRepairNote:
  EncounteredWording:
  GovernedTextSpan:
  ClaimBeingMade:
  ObjectUnderWordingRepair:
  WordingUseDispositionValue: boundedDemonstratedContinuation | evaluationResultChangePrediction | directGovernedUse | importedSourceWording | ordinaryProse | quoteOnly
  DirectGoverningPatternRef?: U.EntityRef, referencing one U.MethodDescription
  RecoveredGovernedValueRef?: U.EntityRef
  RecoveredGovernedValueKindRef?: U.KindRef
  RecoveredRelationSignatureRef?: U.EntityRef, referencing one RelationSignature
  RetainedPlainWording?:
  BlockedOverread:
  SplitDisposition?:
  FinalWordingOrBlocker:
  RemainingReaderUse:
  QualificationWindow:
  CurrentnessBasis:
  ReopenCondition:
```

The governed-value ref and kind ref are both present or both absent. The relation-signature ref is present exactly when the recovered governed value is a relation. A governed use has a direct governing pattern and a recovered governed value. Ordinary prose and quote-only uses may leave those positions absent and record why no FPF object is being claimed. The `...Ref` fields carry references of the declared RefKinds; they do not carry the referenced values or kinds. A materialized note also states the edition, source, context, or time window in which the repair is relied on, the current pattern or source basis for that interpretation, and the smallest change that reopens it. Use `G.11` only when actual refresh orchestration is current; the note merely records its own currentness boundary. The note is a temporary wording-restoration aid, not a project result, method, plan, gate decision, or work occurrence. Ordinary immediate repair need not materialize the note.

#### E.10.MOVE:4.2 - Trigger groups

Run this restoration when one of these wording groups carries an FPF-governed use:

- `move`, `step`, `action`, `application`, `solution`, and `next action`;
- `readiness`, `ready`, `full kit`, `work entry`, and `launch-ready`;
- `movement`, `direction`, or `shift` used for an expected evaluation-result change;
- `route`, `workflow`, `process`, `path`, `loop`, or `flow` used for a demonstrated continuation, selected structure, transformation, method, work, gate, publication, decision, or currentness claim;
- imported source wording such as TameFlow `MOVE`.

The trigger group only opens the repair. It does not supply a replacement vocabulary or choose the governed-value kind.

#### E.10.MOVE:4.2a - No synonym closure

Replacing `move` with `step`, `action`, `use`, or `application` does not close the repair. Close only after the recovered governed value and its direct governing pattern or actual responsibility assignment are explicit, or after an ordinary-prose or quote-only disposition establishes that no FPF-governed value is claimed.

#### E.10.MOVE:4.3 - Wording-use dispositions

`WordingUseDispositionValue` is a local finite enumeration for choosing a repair branch. It is not a U-kind, relation kind, state frame, or claim about the project value being repaired.

| `WordingUseDispositionValue` | Selected recovery |
| --- | --- |
| `boundedDemonstratedContinuation` | One `DemonstratedPatternUseRow@Context` governed by A.22.CGUS; for Plain `mantra move`, retain the complete bounded CGUS-demonstrative context and exit stronger claims to their direct patterns. |
| `evaluationResultChangePrediction` | One E.23 `ExpectedEvaluationResultChange@Context` with evaluation pattern, coordinate, scale, current result, one expected value, range, or closed direction, proposal basis, and protected tradeoffs. |
| `directGovernedUse` | The exact governed value or relation, its kind, relation signature when applicable, and its direct governing pattern. The wording disposition itself contributes no project ontology. |
| `importedSourceWording` | Preserve the source expression only as source wording; recover every FPF use under its direct pattern. |
| `ordinaryProse` | Keep or lightly rewrite after recording that no FPF-governed value is being asserted. |
| `quoteOnly` | Preserve the quotation and block stronger project use not licensed by the quoted source. |

#### E.10.MOVE:4.4 - Relation to A.3.4.P

Use `A.3.4.P` first when the claim is about a change situation or transformation-flow structure. Return to `E.10.MOVE` only for the remaining wording-use question. If the same sentence also recommends a pattern use, claims readiness, or names a demonstrated continuation, split those claims and send each to its direct pattern.

#### E.10.MOVE:4.5 - Durable name repair

A durable name states the recovered subject value or relation; it does not retain an implementation head merely because the fields are typed.

| Misleading durable name | Repair |
| --- | --- |
| `localMoveLocus` | Name the exact local value or relation and its governing pattern. Do not preserve `locus` as a cross-pattern grouping head. |
| `ExpectedEvaluationMovement` | Use `ExpectedEvaluationResultChange@Context` only when the E.23 prediction positions are recoverable. |
| `FirstMoveRecord@Context` | Name the actual first result or relation governed by the direct pattern. |
| `Pattern-Use Sequence` | Use `PatternUseCoordination@Context` or `PatternUsePairwiseOrderingRelation@Context` when that exact relation is current. |

These are repair demonstrations, not a global replacement table.

### E.10.MOVE:5 - Archetypal Grounding - Worked Slices

#### E.10.MOVE:5.1 - Bounded `mantra move`

Source sentence: "The next mantra move is to compare the two patterns."

Keep `mantra move` only when the sentence presents one row inside a named `DemonstrativeUnfoldingSlice@Context`. The row names its public template or project candidate, direct PatternID and name, Solution, expected result, result-flow position, and continuation condition. If the pattern choice is unresolved, the row points to a separate nested pattern-selection slice. The phrase does not claim a recommendation, method, work plan, performed work, or operation merely by being readable.

```text
WordingUseDispositionValue: boundedDemonstratedContinuation
DirectGoverningPatternRef: A.22.CGUS
RecoveredGovernedValueRef: DemonstratedPatternUseRow@SeminarArchitectureUse
RecoveredGovernedValueKindRef: DemonstratedPatternUseRow@Context
RetainedPlainWording: mantra move, only in the bounded CGUS-demonstrative context
BlockedOverread: no U.Move; no actual work or universal sequence
RemainingReaderUse: inspect the shown candidate, Solution, expected result, and condition
QualificationWindow: published A.22.CGUS and E.10.MOVE pattern editions dated 2026-07-11
CurrentnessBasis: A.22.CGUS admits this named seminar slice and row; E.10.MOVE admits the bounded Plain wording
ReopenCondition: the enclosing slice loses CGUS admission, the demonstrated-row schema changes, or readers use the phrase as Work, recommendation, or universal sequence
```

#### E.10.MOVE:5.2 - Expected evaluation-result change

Source sentence: "The repair should create an upward evaluation movement."

If the claim predicts a later evaluation result, restore the evaluation pattern, coordinate, scale, current result, one expected scale value, range, or closed direction, candidate proposal basis, and protected tradeoffs. Write the result as `ExpectedEvaluationResultChange@Context`. If those positions are unavailable, keep a provisional prediction description or return to E.22 and E.23; do not call the phrase a completed move.

#### E.10.MOVE:5.3 - Next FPF use

Source sentence: "The next FPF move is to check architecture."

If this is a project-local recommendation, restore `PatternUseRecommendation@Context` under `E.11.PUR` and cite the exact architecture pattern being recommended. The final wording may say "next useful pattern use" in ordinary explanation, but it cannot imply performed architecture work or a root `U.Move`.

#### E.10.MOVE:5.4 - TameFlow `MOVE`

Source sentence: "The MOVE is full-kitted and ready."

Preserve `MOVE` as imported source wording. Restore the target WorkPlan or PlanItem, full-kit condition, work-entry readiness relation, and any actual gate decision under their direct patterns. Do not claim target work occurred unless a dated A.15.1 occurrence is current.

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

When `ready` hides a patient-state claim, use A.19.SPR to recover the patient as bearer, the clinical state frame or direct governing pattern, the current value or classification, its evidence and qualification window, and the practical discharge use. A discharge recommendation, accountable decision, work-entry condition, and completed discharge remain different claims under their direct clinical and FPF patterns. Do not infer a discharge decision or performed discharge from the adjective alone.

#### E.10.MOVE:5.9 - Reopen when a local mantra is not CGUS

Initial sentence: "The next mantra move is: name the thing."

An initial repair classified the phrase as `boundedDemonstratedContinuation`. Inspection then shows that the enclosing text is A.6.P's local RPR mantra: a short rendering of the A.6.P Solution. It has no named wider `ConstraintGovernedUnfoldingStructure@Context`, no admitted `DemonstrativeUnfoldingSlice@Context`, and no complete `DemonstratedPatternUseRow@Context`.

That evidence overturns the initial disposition. Remove the demonstrated-row claim, retain the local RPR mantra as Plain didactic wording, recover the A.6.P Solution as the direct `U.MethodDescription`, and write: "Apply the first clause of the local RPR mantra: name the thing; then recover the relation or comparison." Reopen CGUS admission only if a later demonstration supplies the enclosing slice and complete row positions.

### E.10.MOVE:6 - Bias-Annotation

- **Synonym-replacement bias.** Replacing "move" with "action", "step", or "use" can preserve the same hidden ontology. Recover concern, relation, and governing pattern before choosing wording.
- **Imported-source-kind bias.** TameFlow `MOVE`, workflow, route, process, or path wording can smuggle a source ontology into FPF. Treat such wording as a trigger until the direct FPF target is named.
- **Readiness-as-gate bias.** Ready, full-kit, committed, or launch-ready wording can overclaim gate passage, work authorization, or performed work.
- **Local-wording generalization bias.** One direct pattern may define a local move-like expression. That expression does not create a shared project kind; every other use still restores its own governed value and direct governing pattern.

### E.10.MOVE:7 - Conformance Checklist

| ID | A conforming repair... | Check |
| --- | --- | --- |
| `CC-E10MOVE-1` | names the governed text span, claim being made, and object under wording repair before choosing a replacement. | The word itself does not choose the ontology. |
| `CC-E10MOVE-2` | assigns one wording-use disposition and does not treat that local enumeration as project ontology. | Demonstrated row, evaluation-result prediction, direct governed use, imported source wording, ordinary prose, and quotation cases remain distinct. |
| `CC-E10MOVE-3` | names the exact recovered governed value, value kind, relation signature when applicable, and direct governing pattern. | A wording disposition or neighbor list cannot stand in for the recovered project value. |
| `CC-E10MOVE-4` | blocks root `U.Move`. | No durable move kind is minted by wording pressure. |
| `CC-E10MOVE-5` | preserves remaining reader use. | The repaired text still says what the practitioner can do or inspect next. |
| `CC-E10MOVE-6` | splits change-situation wording from pattern-use or readiness wording. | `A.3.4.P` and `E.10.MOVE` are both used when both objects are current. |
| `CC-E10MOVE-7` | avoids synonym tables. | The repair recovers object and relation, not a preferred vocabulary list. |

#### E.10.MOVE:7.1 - Lowering and Reopen Conditions

Lower, block, or reopen the repair when the governed text span, claim being made, or object under wording repair is not recoverable, the wording-use disposition is uncertain, the proposed wording changes kind or relation without an accepted governing pattern, the direct governing pattern is missing, a change-situation claim was not separated from pattern-use or readiness wording, the repaired wording loses the remaining reader use, or a stronger source quote is present and remains preserved with quote-only status.

### E.10.MOVE:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Better use |
| --- | --- | --- |
| Synonym replacement | "Move" becomes "action" or "use" without recovered kind. | Recover governed text span, claim being made, object under wording repair, relation, and governing pattern first. |
| Imported MOVE kind | TameFlow source wording becomes FPF ontology. | Recover intended work, readiness, gate, preparation work, or performed work. |
| Readiness as gate passage | A ready label becomes `GateDecision=pass`. | Use A.21 only when gate fields are present. |
| Path as work-authorization route | Evidence path or source-reference path becomes a way to authorize work by resemblance. | Recover evidence relation, source relation, graph path, gate relation, work authorization, or deontic permission separately. |
| Local expression generalized | A bounded local phrase is generalized to unrelated project work. | Keep `mantra move` bound to one `DemonstratedPatternUseRow@Context`; restore every other phrase through its own governed value and direct pattern. |

### E.10.MOVE:9 - Consequences

Benefits:

- FPF keeps friendly move and readiness language without letting it mint false kinds.
- Pattern-use recommendation, P2W, work readiness, gate decision, performed work, transformation, architecture, and call planning stay separable.
- Corpus cleanup can find move-headed debt without doing mechanical global renames.

Costs:

- Reliance-bearing or still-ambiguous phrases may need the small repair note before they can be rewritten safely; ordinary direct-pattern repair does not.
- Text may need to split one sentence into two governed claims when the original wording carried both change-situation and pattern-use meaning.

### E.10.MOVE:10 - Rationale

Move-like wording is too useful to ban and too ambiguous to leave ungoverned. `E.10.MOVE` gives a narrow restoration path: recover the governed text span, claim being made, and object under wording repair; classify borrowed or ordinary wording; name the governed FPF value; preserve reader use; and apply the pattern that governs that value.

The pattern is a child of E.10 because it starts as wording-use restoration. Two retained restorations are deliberately narrow: `mantra move` returns to one A.22.CGUS demonstrated row, while evaluation movement wording returns to one E.23 prediction about a later evaluation result. Recommendation, transformation, readiness, gate, publication, and work claims remain with their direct patterns.

### E.10.MOVE:11 - SoTA-Echoing

| Current source and status | Adopted or adapted move | Effect in E.10.MOVE | Limitation and reopen condition |
| --- | --- | --- | --- |
| Current FPF precision-restoration set dated 2026-07-11: `E.10`, `E.10.ARCH`, `A.6.P`, `A.19.SPR`, and `A.3.4.P` | Treat a trigger word as evidence of a recovery problem, restore the governed value and relation before rewriting, preserve ordinary useful wording, and return the final claim to its direct pattern. | Determines the cheap path, the seven-step repair, local-mantra boundary, readiness-bearer recovery, direct-pattern exits, useful-reader-use invariant, and fail-closed conditions. | This is the current governing basis, not external empirical proof. Reopen the affected slice when one of these patterns changes the relevant kind settlement, authority boundary, or recovery fields. |
| Zhu, Reinecke, and Mitra, ["Language Scent: Exploring Cross-Language Information Navigation"](https://arxiv.org/abs/2604.03604), arXiv:2604.03604, 2026 preprint | Preserve recognizable in-situ wording when it helps a reader locate the intended use, but keep contextual sense and governed value explicit rather than assuming lexical equivalence. | Supports retaining bounded Plain `mantra move`, ordinary `next useful pattern use`, and source `MOVE` while the pattern makes their distinct governed values recoverable. | The study is small and cross-language; it does not establish FPF ontology or prove these labels work for every reader. Reopen if larger evidence shows the retained cue obscures the governed value or impedes the remaining reader use. |
| Steve Tendon, [*The Book of TameFlow: Theory of Constraints Applied to Knowledge-Work Management*](https://leanpub.com/tameflow), current Leanpub edition accessed 2026-07-11; Tendon, ["Constraints Everywhere"](https://tameflow.com/blog/2020-08-09/constraints-everywhere/), 2020 | Recover `MOVE` and Full-Kitting as source-practice wording with useful distinctions about bounded effort, outcome or value, constraint, and pre-entry preparation. | Supplies the imported-source worked slice and routes intended work, full-kit condition, work-entry readiness, resource relation, gate decision, preparation Work, and target Work to A.15, A.15.5, A.21, and B.1.6. | This practice is scoped to knowledge-work management and is not selected as a universal current ontology of move or readiness. Reopen when its current source edition changes these terms or when FPF's work and readiness patterns change their recovery. |

The current best problem-solving line for this pattern is therefore the current FPF recovery architecture. The 2026 language-scent study changes cue preservation, subject to its evidence limit. TameFlow changes only the treatment of one encountered source vocabulary and remains source-practice lineage outside that bounded use; popularity or recency does not give it authority over FPF kinds.

### E.10.MOVE:12 - Relations

- **Builds on:** `E.10`, `E.10.ARCH`, `A.3.4.P`, `A.22.CGUS`, `E.11.PUR`, `E.23`, `A.15.5`, and `E.24`.
- **Coordinates with:** `E.18`, `E.18.1`, `A.15`, `A.21`, `C.24`, `C.30`, `E.17`, `F.17`, `F.18`, `G.11`, `A.10`, and each recovered governed value's direct governing pattern. `F.18` governs a durable-name decision; `G.11` governs refresh orchestration only when currentness, edition, telemetry, freshness, or decay is the actual claim.
- **Selected by:** E.10 trigger scan when move or readiness wording has FPF-governed use and no direct governing pattern has already resolved the wording.

### E.10.MOVE:End

