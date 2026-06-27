## E.11.PUR - Pattern-Use Recommendation and Pattern-Use Sequence

> **Type:** Pattern-language governance pattern (E)
> **Status:** Stable
> **Normativity:** Normative for FPF pattern-use recommendation and pattern-use sequence records.

**At a glance.** `E.11.PUR` governs the relation in which one FPF pattern use, or a short sequence of pattern uses, is recommended for a current project concern. It keeps ordinary "first useful move" speech teachable while preventing a new root `U.Move` kind.

**Use this when.** Use this pattern when a practitioner, manager, or assisting agent needs to decide which FPF pattern use is worth taking next for a recognizable project concern after applicability has been checked.

**Primary EntityOfConcern.** One `PatternUseRecommendation@Context`: the relation between a current project concern, a bounded context, one or more candidate FPF pattern uses, an applicability finding, the recommended pattern use, and the expected practical result.

**First output.** One compact `PatternUseRecommendation@Context` or `PatternUseSequence@Context` record that names the current concern, the recommended pattern use, the reason for recommending it, the expected output shape, blocked stronger uses, and any neighboring governing pattern that becomes current after this use.

**Not this pattern when.** If accepted problem-side material is being carried through P2W, use `E.18.1`. If work is being planned or performed, use the A.15 family. If a gate decision is current, use `A.21`. If a tool-call plan is current, use `C.24`. If the sentence is only about publication, phrase wording, or description use, use `E.8`, `E.17`, or the direct publication or description pattern.

### E.11.PUR:1 - Problem Frame

FPF is meant to help a working team find a useful next pattern use in an actual problem situation. The natural way to say this in teaching and project conversation is often "what is the next useful move?" or "what professional move does FPF give here?"

That speech is useful, but it becomes unsafe when the word "move" starts to name a new ontology. A recommended pattern use is not the work itself, not a gate passage, not a work plan, not an architecture decision, and not an authorization to act. It is a pattern-use relation that helps the user choose the next FPF pattern application and its expected output.

### E.11.PUR:2 - Problem

Without an explicit pattern-use recommendation relation, four failures recur:

1. A pattern that only recommends a next FPF use is overread as if it performed work, passed a gate, or authorized work.
2. Applicability and recommendation collapse: "this pattern can be used" becomes "this pattern is the selected useful use now."
3. Several pattern uses are described as a workflow or lifecycle, even when they are only a recommended pattern-use sequence.
4. Teaching language such as "first useful move" becomes a false kind and starts competing with `U.Work`, `U.WorkPlan`, P2W, A.16 language-state moves, C.24 call planning, and C.30 architecture candidate material.

### E.11.PUR:3 - Forces

| Force | Pressure |
| --- | --- |
| Teachability | Engineer-facing speech needs simple words such as first useful move, working move, and professional move. |
| Ontological precision | FPF must not create a root `U.Move` when the direct governed value is pattern use, plan, work, gate, source, publication, architecture, or transformation. |
| Applicability vs recommendation | A pattern can be applicable without being the recommended use for the current concern. |
| Composition | Several pattern uses can form a useful FPF phrase without becoming a work plan or process. |
| Practical payoff | The result must still tell the practitioner what can be produced or inspected next. |

### E.11.PUR:4 - Solution

Use three registers deliberately.

In engineer-facing speech, phrases such as "first useful move", "working move", "professional move", "SoTA move", "strong move", "admissible move", and "next move" may stay when they help a team ask what to do next.

In didactic pattern-language speech, the same idea can be explained as building a useful FPF phrase from pattern words: one pattern may frame the problem, another preserve variants, another recommend an architecture question, another carry the decision toward work, and another update SoTA or wording.

In the precise FPF layer, do not create a `Move` kind from either metaphor. Recover `PatternUseRecommendation@Context` for the recommended use of one pattern, `PatternUseSequence@Context` for several pattern uses, and the direct governing pattern for work, plan, gate, decision, publication, architecture, source, or transformation claims.

#### E.11.PUR:4.1 - PatternUseRecommendation@Context

`PatternUseRecommendation@Context` is a dependent durable pattern-use relation value. It says which FPF pattern use is recommended now for one current concern.

E.24.UK settlement: this pattern does not introduce a root `U.PatternUseRecommendation`, a root `U.Move`, or an independent pattern-use ontic. The governed value is a context relation over existing values: project concern, bounded context, candidate pattern uses, governing pattern, applicability finding, recommended pattern use, expected practical result, and neighboring governing-pattern refs. `PatternUseSequence@Context` is the sequence form of the same relation discipline, not a workflow, lifecycle, route, WorkPlan, or performed work.

```text
PatternUseRecommendation@Context:
  ProjectConcernRef
  BoundedContextRef
  PatternUserOrAgentRef?
  GoverningPatternRef
  CurrentEntityOfConcernRef?
  CurrentClaimOrRelationKindRef?
  RecognitionCueRef?
  CandidatePatternUseSet?
  ApplicablePatternUseSet?
  ApplicabilityFinding
  RecommendedPatternUse
  ReasonForRecommendation
  ExpectedPracticalGain?
  OutputRefOrOutputShape
  AdmissibleUse
  BlockedStrongerUse
  StopCondition
  NextGoverningPatternRef?
  ReturnOrReopenCondition?
```

`RecommendedPatternUse` is stronger than an applicability finding. It means: this pattern use is selected as useful for the current concern, given the available candidate pattern uses and the expected practical result. If a project actor then plans or performs work, that resulting object is governed by `U.WorkPlan`, A.21, or `U.Work`, not by this pattern-use relation.

#### E.11.PUR:4.2 - PatternUseSequence@Context

Use `PatternUseSequence@Context` when several recommended or applied pattern uses must be kept together:

```text
PatternUseSequence@Context:
  ProjectConcernRef
  BoundedContextRef
  SequencePurpose
  PatternUseRefs
  OrderingReason?
  OutputChain
  DirectGoverningPatternForEachUse
  BlockedWorkflowOverread
  StopCondition
  ReturnOrReopenCondition?
```

The sequence is not a work plan, route, workflow, lifecycle, or performed work. It is only a relation among pattern uses unless a neighboring pattern makes work planning, call planning, transformation-flow structure, gate decision, or performed work current.

#### E.11.PUR:4.3 - Boundary Table

| Current claim | Use |
| --- | --- |
| Which FPF pattern use is recommended now? | `PatternUseRecommendation@Context`. |
| Which several FPF pattern uses belong together for this concern? | `PatternUseSequence@Context`. |
| Accepted problem-side material is carried toward a next FPF value. | `E.18.1`. |
| Work is intended, scheduled, or prepared. | `A.15.2`, `A.15.3`, or `A.15.5`. |
| Work actually occurred. | `A.15.1`. |
| A gate admits, degrades, blocks, or abstains. | `A.21`. |
| An AI agent is planning tool calls. | `C.24`. |
| Architecture candidate material is current. | `C.30` or the direct architecture child pattern. |
| Language-state transition is current. | `A.16`. |
| Publication expression makes the pattern use visible. | `E.8`, `E.11`, `E.17`, or the direct publication pattern. |

### E.11.PUR:5 - Archetypal Grounding - Worked Slices

#### E.11.PUR:5.1 - Architecture Entry

Situation: a team says, "We need the next useful FPF move for our reactor-cooling architecture problem."

Use `PatternUseRecommendation@Context`:

```text
ProjectConcernRef: reactor-cooling architecture uncertainty
BoundedContextRef: concept review before module selection
CandidatePatternUseSet: C.30, C.30.ASV, C.29, A.21
ApplicablePatternUseSet: C.30 and C.30.ASV are applicable
RecommendedPatternUse: C.30 first, then C.30.ASV if selected structure is still unclear
ReasonForRecommendation: the question is about architecture and selected structures before a gate or work plan is current
OutputRefOrOutputShape: ArchitectureQuestionCard@Project
BlockedStrongerUse: no gate passage, no work authorization, no performed work
NextGoverningPatternRef: C.30
```

The ordinary sentence may still say "first useful move", but the FPF record names recommended pattern use.

#### E.11.PUR:5.2 - Agent Repair

Situation: an assisting agent notices vague "process" wording in a technical standard and asks what to do next.

Use `PatternUseRecommendation@Context` when the current question is which FPF pattern to apply. Recommend `E.10` first. If `E.10` recovers transformation-situation wording, use `A.3.4.P`. If it recovers work-entry readiness wording, use `E.10.MOVE` and possibly `A.15.5`. If the agent plans tool calls, use `C.24` for the call plan.

#### E.11.PUR:5.3 - P2W Boundary

Situation: a problem card has accepted problem-side material and the team asks for the next useful FPF use.

Use `E.18.1` for the carry-through relation. `E.18.1` may cite `PatternUseRecommendation@Context` when the next recovered value is a recommended FPF pattern use. P2W remains the relation from accepted problem-side material to the next governed value; `E.11.PUR` does not replace it.

#### E.11.PUR:5.4 - Proxy Failure

Situation: a team keeps recommending `C.30` because it is the familiar architecture pattern, even when the current concern is a work-entry readiness question before a test run.

Do not treat the familiar pattern id as the value. Fill `PatternUseRecommendation@Context` against the current concern and expected practical result. If the needed result is a readiness disposition, recommend `A.15.5`; if the needed result is an architecture question, recommend `C.30`. The visible proxy, "we used the architecture pattern again", gets worse when it hides missing kit, commitment, or launch-gate relations.

### E.11.PUR:6 - Bias-Annotation

- **Move-kind bias.** Ordinary speech such as "first useful move" can become a false root kind. Keep the plain phrase only when the durable FPF value remains `PatternUseRecommendation@Context`, `PatternUseSequence@Context`, or a direct neighboring governed value.
- **Favorite-pattern proxy bias.** A familiar pattern id can substitute for the current project concern. Check the expected practical result and the blocked stronger use before recommending a pattern.
- **Workflow overread bias.** Several pattern uses can be useful together without becoming a lifecycle, route, WorkPlan, or performed work.

### E.11.PUR:7 - Conformance Checklist

| ID | A conforming use... | Check |
| --- | --- | --- |
| `CC-E11PUR-1` | names the project concern before recommending a pattern use. | The concern is not replaced by a pattern id alone. |
| `CC-E11PUR-2` | separates applicability from recommendation. | `ApplicabilityFinding` and `RecommendedPatternUse` are both recoverable when both claims are made. |
| `CC-E11PUR-3` | blocks stronger uses. | Work, plan, gate, decision, source, publication, architecture, and transformation overreads are named only when their governing pattern is current. |
| `CC-E11PUR-4` | preserves the remaining reader use. | The result says what the practitioner can inspect, write, decide, or apply next. |
| `CC-E11PUR-5` | uses `PatternUseSequence@Context` only for pattern-use relations. | The sequence is not a work plan, workflow, lifecycle, or performed work. |
| `CC-E11PUR-6` | keeps didactic move language plain. | "First useful move" can remain in teaching prose, but durable FPF text names the recovered relation. |

#### E.11.PUR:7.1 - Lowering and Reopen Conditions

Lower, reject, or reopen the recommendation when the project concern changes, a candidate pattern becomes inapplicable, the expected output shape no longer answers the concern, a stronger neighboring claim becomes current, a proxy pattern id is being optimized instead of practical gain, or the first applied result shows that the recommended pattern use did not produce the promised inspection, decision input, or work-preparation value.

### E.11.PUR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Better use |
| --- | --- | --- |
| Move as kind | A useful phrase becomes a false `U.Move`. | Recover recommended pattern use, work, plan, gate, source, publication, architecture, or transformation. |
| Applicability as recommendation | Every applicable pattern appears equally selected. | State why this pattern use is recommended for the current concern. |
| Pattern phrase as work plan | A pattern-use sequence is treated as intended or performed project work. | Use `A.15.2` for work planning and `A.15.1` for performed work. |
| Pattern recommendation as authorization | A pattern recommendation is read as gate passage, source sufficiency, assurance, or work authorization. | Use A.21, source restoration, assurance, or the direct work-authorization pattern when those claims are current. |

### E.11.PUR:9 - Consequences

Benefits:

- FPF can keep friendly "what is the next useful move?" language without minting a root `Move`.
- The first-entry and seminar-facing pattern-language metaphor becomes useful but bounded.
- P2W, work planning, performed work, gates, architecture, source, and publication claims keep their governing patterns.

Costs:

- Users must name the current concern and expected output shape rather than only naming a favorite pattern.
- A pattern-use sequence needs one line per governed use when several patterns are composed.

### E.11.PUR:10 - Rationale

The practical question "what should I do next with FPF?" is real. It deserves a stable relation because it recurs in first-entry use, seminar teaching, AI assistance, and multi-pattern composition. The relation is not a new kind of project object. It is a pattern-use recommendation relation that points to the pattern likely to produce the next useful result.

This keeps FPF action-guiding: users can still ask for a first useful move, while FPF can answer with a precise pattern use and then use the pattern that governs work, gates, architecture, source, publication, or transformation.

### E.11.PUR:11 - SoTA-Echoing

| Source family | Use in this pattern | Local adoption |
| --- | --- | --- |
| Pattern-language practice for problem-situation recognition and pattern composition | Supports the "patterns as words, phrases as composed uses" teaching line. | Adopt the metaphor only as didactic guidance; precise FPF text still names pattern-use relations and direct governing patterns. |
| Current recommender-system and human-centered XAI practice | Separates candidate generation, applicability or ranking, recommendation, explanation, user control, and bias or proxy checks. | Adapt the separation without importing an IT recommender ontology: `CandidatePatternUseSet`, `ApplicablePatternUseSet`, `RecommendedPatternUse`, `ReasonForRecommendation`, expected practical gain, and proxy-failure checks make pattern recommendation reviewable by a practitioner. |
| Human-centered guidance for task-suitable labels and first-use recognition | Supports keeping engineer-facing phrases such as "first useful move" when they help recognition. | Adapt by requiring the durable FPF relation name to remain recoverable after the friendly label. |
| Current FPF `E.11`, `E.8`, and `E.10` governance | Governs entry publication, pattern-local recognition, and wording restoration. | Reuse existing first-entry and authoring law; this child pattern supplies only the pattern-use recommendation relation. |

### E.11.PUR:12 - Relations

- **Builds on:** `E.11`, `E.8`, `E.10`, `E.10.ARCH`, `E.18.1`, and `E.24`.
- **Coordinates with:** `A.15`, `A.15.1`, `A.15.2`, `A.15.3`, `A.15.5`, `A.16`, `A.21`, `C.24`, `C.30`, `C.30.AD`, and `E.17`.
- **Selected by:** `E.10.MOVE` when move wording recovers recommended pattern use rather than work, plan, gate, transformation, publication, architecture, or source use.

### E.11.PUR:End

