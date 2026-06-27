## E.10.MOVE - Move and Readiness Wording Precision Restoration

> **Type:** Part E precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative for move-like and readiness-like wording-use restoration.

**At a glance.** `E.10.MOVE` restores the FPF object hidden by wording such as move, step, action, application, solution, next action, work item, work entry, full kit, readiness, TameFlow `MOVE`, route, workflow, and process when that wording is about project concern, pattern-use recommendation, work-entry readiness, or another direct governing pattern.

**Use this when.** Use this pattern when move-like or readiness-like wording helps recognition but starts to hide whether the current value is pattern use, P2W carry-through, WorkPlan, SlotFillingsPlanItem, WorkEntryReadiness, GateDecision, performed Work, transformation, method, publication, source use, language-state move, call plan, or architecture candidate material.

**Primary EntityOfConcern.** One wording-use restoration over a bounded text span whose move-like or readiness-like wording has an FPF-governed use.

**First output.** One `MoveAndReadinessWordingRepair` note naming the project concern, source-use class, recovered relation or value, direct governing pattern, retained plain wording, blocked overread, split if needed, final wording or blocker, and remaining reader use.

**Not this pattern when.** Use `A.3.4.P` first when the wording is primarily about transformation, flow, path, process, workflow, operation, or change as a change-situation label. Use the direct governing pattern immediately when the current object is already known and no move-like or readiness-like wording problem remains.

### E.10.MOVE:1 - Problem Frame

"Move" is useful in project conversation. It can mean a chess-like next choice, a first FPF use, a TameFlow `MOVE`, an architecture candidate, a language-state transition, a call-planning next action, a work-preparation item, or an ordinary action. "Ready", "full kit", and "work entry" can likewise mean source currentness, work planning, preparation work, gate passage, or performed work.

The defect is not the word. The defect is letting that word choose the ontology. `E.10.MOVE` restores the project concern and the direct FPF relation before any rewrite is accepted.

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

Apply this recovery order:

1. Recover the project concern first: what object, situation, relation, or intended result made the wording matter?
2. Classify source use: seminar pattern-use language, TameFlow `MOVE` source use, work-entry readiness, local move locus, ordinary prose, or quote-only wording.
3. Decide the direct governed value: `PatternUseRecommendation@Context`, E.18.1 P2W, `U.WorkPlan`, PlanItem, `SlotFillingsPlanItem`, `WorkEntryReadiness@Context`, A.21 `GateDecision`, performed `U.Work`, `U.Transformation`, `U.Method`, `U.MethodDescription`, A.16 language-state move, C.24 call planning, C.30 architecture candidate move, selected set, publication expression, source relation, or ordinary prose.
4. If several values are current, split them and name the direct governing pattern for each.
5. Preserve the remaining reader use. The repair fails if the text becomes formally clean but no longer tells the practitioner what can be done now.
6. Use `A.3.4.P` for the change-situation branch and return to `E.10.MOVE` only for pattern-use, project concern, or work-entry readiness wording left after the transformation branch is recovered.

#### E.10.MOVE:4.1 - MoveAndReadinessWordingRepair note

```text
MoveAndReadinessWordingRepair:
  EncounteredWording:
  BoundedTextSpan:
  ProjectConcern:
  SourceUseClass: seminarPatternUse | tameFlowMoveSource | workEntryReadiness | localMoveLocus | ordinaryProse | quoteOnly
  RecoveredRelations:
  DirectGoverningPatterns:
  RetainedPlainWording:
  BlockedOverread:
  RequiredSplit?:
  FinalWordingOrBlocker:
  RemainingReaderUse:
```

The note is a temporary wording-use restoration aid. It does not create project records, gate decisions, WorkPlans, or work occurrences.

#### E.10.MOVE:4.2 - Short Cue Set

Trigger this pattern only when the wording has FPF-governed use:

- move, first useful move, working move, professional move, SoTA move, strong move, admissible move, next move;
- step, action, application, solution, next action, work item, work entry;
- full kit, full-kitting, readiness, ready, committed, launch-ready;
- TameFlow `MOVE` or source MOVE;
- route, workflow, and process when the wording hides pattern-use, project-concern, or readiness relation rather than a transformation-situation claim.

The list is not a replacement vocabulary. It is a recognition aid for the recovery order.

#### E.10.MOVE:4.3 - Source-Use Classes

| SourceUseClass | Typical recovery |
| --- | --- |
| `seminarPatternUse` | `PatternUseRecommendation@Context`, `PatternUseSequence@Context`, publication phrase, or direct neighboring pattern. |
| `tameFlowMoveSource` | WorkPlan, PlanItem, full-kit preparation, `WorkEntryReadiness@Context`, A.21 when gate decision is current, preparation `U.Work`, target `U.Work`, resource relation, or result relation. |
| `workEntryReadiness` | `WorkEntryReadiness@Context`, `FullKitCondition`, A.15.2, A.15.3, A.15.1, A.21, B.1.6, or A.15.4. |
| `localMoveLocus` | A.16 language-state move, C.24 call-planning action, C.30 architecture candidate move, or another accepted local locus. |
| `ordinaryProse` | Keep or lightly rewrite without FPF restoration. |
| `quoteOnly` | Keep as source wording and block stronger use. |

#### E.10.MOVE:4.4 - Relation to A.3.4.P

Use `A.3.4.P` first when the wording is mainly about change in the world or a transformation-flow structure:

- process, workflow, path, pipeline, operation, flow, transformation, change, circuit, network, and route-like wording;
- graph path, path slice, flow valuation, or transformation-flow structure claims;
- method, mechanism, work, or publication-description confusion caused by change-situation wording.

Use `E.10.MOVE` when the remaining question is: which project concern, pattern use, work-entry readiness relation, or local move locus should the reader use next? If both are current, split the text and apply both patterns to their own current objects.

#### E.10.MOVE:4.5 - Durable Name Repair

Durable field and record names must name their direct governed value. Examples:

| Dirty durable name | Prefer |
| --- | --- |
| `FirstMoveRecord@Context` | `FirstApplicationRecord@Context` when the object is the first application record. |
| `RelationMoveNow` | `CurrentRelationGovernedUse` when the object is source-restoration use. |
| `NextMoveHypothesis` | `RecommendedPatternUse` or another direct candidate, selected set, work, gate, or architecture object. |
| `Pattern-Use Sequence` | `PatternUseSequence@Context` when the durable relation is meant. |

Do not run these as mechanical global replacements. Recover the governed object first.

### E.10.MOVE:5 - Archetypal Grounding - Worked Slices

#### E.10.MOVE:5.1 - "What is the next FPF move?"

Source sentence: "The next FPF move is to check architecture."

Repair:

```text
ProjectConcern: architecture uncertainty in a current project
SourceUseClass: seminarPatternUse
RecoveredRelations: PatternUseRecommendation@Context
DirectGoverningPatterns: E.11.PUR, C.30
RetainedPlainWording: "next useful move" may stay in teaching prose
BlockedOverread: no U.Move, no performed architecture work
FinalWordingOrBlocker: recommend C.30 as the next pattern use
RemainingReaderUse: write or inspect ArchitectureQuestionCard@Project
```

#### E.10.MOVE:5.2 - TameFlow `MOVE`

Source sentence: "The MOVE is full-kitted and ready."

Repair: source `MOVE` is wording from Steve Tendon's TameFlow framework. Recover target WorkPlan or PlanItem, `FullKitCondition`, `WorkEntryReadiness@Context`, and possible A.21 gate decision. Do not claim target `U.Work` occurred unless dated work evidence is current.

#### E.10.MOVE:5.3 - Workflow Diagram

Source sentence: "This workflow is the next move after problem framing."

Repair: if the diagram describes a transformation-flow structure or method description, use `A.3.4.P`, `E.18`, or `A.3.2`. If the current question is which FPF pattern use should follow problem framing, use `PatternUseRecommendation@Context`. Split if both claims are present.

#### E.10.MOVE:5.4 - Evidence Path

Source sentence: "Follow the evidence path to approval."

Repair: if a graph-theoretic or provenance path is current, use A.10 or G.6. If the claim is evidence support for a decision, use the evidence relation. If the claim is gate passage, use A.21. If the claim is work authorization or deontic permission, use the pattern that governs that claim. Do not turn evidence path wording into a route that authorizes work by resemblance.

### E.10.MOVE:6 - Bias-Annotation

- **Synonym-replacement bias.** Replacing "move" with "action", "step", or "use" can preserve the same hidden ontology. Recover concern, relation, and governing pattern before choosing wording.
- **Imported-source-kind bias.** TameFlow `MOVE`, workflow, route, process, or path wording can smuggle a source ontology into FPF. Treat such wording as a trigger until the direct FPF value is named.
- **Readiness-as-gate bias.** Ready, full-kit, committed, or launch-ready wording can overclaim gate passage, work authorization, or performed work.
- **Local-locus generalization bias.** A.16, C.24, and C.30 have accepted local move-like terms; they do not define a general project-move ontology.

### E.10.MOVE:7 - Conformance Checklist

| ID | A conforming repair... | Check |
| --- | --- | --- |
| `CC-E10MOVE-1` | names the project concern before choosing a replacement. | The word itself does not choose the ontology. |
| `CC-E10MOVE-2` | classifies source use. | Seminar, TameFlow, readiness, local move locus, ordinary prose, and quote-only cases are separated. |
| `CC-E10MOVE-3` | names the direct governing pattern. | The result cites E.11.PUR, E.18.1, A.15, A.15.5, A.21, A.3.4.P, C.24, C.30, or another direct pattern. |
| `CC-E10MOVE-4` | blocks root `U.Move`. | No durable move kind is minted by wording pressure. |
| `CC-E10MOVE-5` | preserves remaining reader use. | The repaired text still says what the practitioner can do or inspect next. |
| `CC-E10MOVE-6` | splits change-situation wording from pattern-use or readiness wording. | `A.3.4.P` and `E.10.MOVE` are both used when both objects are current. |
| `CC-E10MOVE-7` | avoids synonym tables. | The repair recovers object and relation, not a preferred vocabulary list. |

#### E.10.MOVE:7.1 - Lowering and Reopen Conditions

Lower, block, or reopen the repair when the project concern is not recoverable, the source-use class is uncertain, the proposed wording changes kind or relation without an accepted governing pattern, the direct governing pattern is missing, a change-situation claim was not separated from pattern-use or readiness wording, the repaired wording loses the remaining reader use, or a stronger source quote requires preserving the original wording with quote-only status.

### E.10.MOVE:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Better use |
| --- | --- | --- |
| Synonym replacement | "Move" becomes "action" or "use" without recovered kind. | Recover project concern, relation, and governing pattern first. |
| Imported MOVE kind | TameFlow source wording becomes FPF ontology. | Recover intended work, readiness, gate, preparation work, or performed work. |
| Readiness as gate passage | A ready label becomes `GateDecision=pass`. | Use A.21 only when gate fields are present. |
| Path as work-authorization route | Evidence or source path becomes a way to authorize work by resemblance. | Recover evidence, source, graph path, gate relation, work authorization, or deontic permission separately. |
| Local move generalized | A.16, C.24, or C.30 local move wording is generalized to all project work. | Keep local loci local and use the direct governing pattern elsewhere. |

### E.10.MOVE:9 - Consequences

Benefits:

- FPF keeps friendly move and readiness language without letting it mint false kinds.
- Pattern-use recommendation, P2W, work readiness, gate decision, performed work, transformation, architecture, and call planning stay separable.
- Corpus cleanup can find move-headed debt without doing mechanical global renames.

Costs:

- Some short phrases require a small repair note before they can be rewritten safely.
- Text may need to split one sentence into two governed claims when the original wording carried both change-situation and pattern-use meaning.

### E.10.MOVE:10 - Rationale

Move-like wording is too useful to ban and too ambiguous to leave ungoverned. `E.10.MOVE` gives a narrow restoration path: recover the concern, classify the source use, name the direct FPF value, preserve reader use, and apply the pattern that governs the recovered value.

The pattern is a child of E.10 because it starts as wording-use restoration. It stays small because the substantive objects are already governed elsewhere: `E.11.PUR`, `A.15.5`, `E.18.1`, the A.15 family, A.21, A.3.4.P, C.24, C.30, A.16, E.17, and source-restoration patterns.

### E.10.MOVE:11 - SoTA-Echoing

| Source family | Use in this pattern | Local adoption |
| --- | --- | --- |
| Current FPF E.10 and E.10.ARCH precision-restoration architecture | Supplies trigger scan, governed-object recovery, and anti-synonym discipline. | Adopt the recovery order and specialize it only for move and readiness wording. |
| Current FPF transformation precision restoration | Supplies the split between change-situation wording and project concern or pattern-use wording. | Use `A.3.4.P` first when transformation, flow, path, process, workflow, or operation is current. |
| TameFlow `MOVE` and Full-Kitting source material | Supplies one important source-use class for readiness wording. | Treat as source material whose distinctions are recovered under A.15, A.15.5, A.21, and B.1.6. |

### E.10.MOVE:12 - Relations

- **Builds on:** `E.10`, `E.10.ARCH`, `A.3.4.P`, `E.11.PUR`, `A.15.5`, and `E.24`.
- **Coordinates with:** `E.18.1`, `A.15`, `A.15.1`, `A.15.2`, `A.15.3`, `A.15.4`, `A.21`, `B.1.6`, `A.16`, `C.24`, `C.30`, `C.30.AD`, `E.17`, `A.10`, and `G.6`.
- **Selected by:** E.10 trigger scan when move or readiness wording has FPF-governed use and no direct governing pattern has already resolved the wording.

### E.10.MOVE:End

