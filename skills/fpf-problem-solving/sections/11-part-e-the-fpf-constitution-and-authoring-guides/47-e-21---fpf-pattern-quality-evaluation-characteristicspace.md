## E.21 - FPF Pattern-Quality Evaluation CharacteristicSpace

> **Type:** Pattern
> **Status:** Stable

### E.21:1 - Problem frame

Use this when one authored FPF pattern of concern must be evaluated for quality under the use required by the governing evaluation frame: ordinary practitioner use, authoring input, landing input, release input, external-review input, high-assurance reuse input, canonization input, or another explicitly requested pattern-quality use. The evaluator does not replace the required `ClaimScope` with an easier one. If the pattern fails the required use, the result is `repairBeforeUse`, `holdForArchitectureDecision`, or `refreshNeeded`; a different use needs a different evaluation frame and does not rescue the current result.

Not this pattern when the evaluated object is one `DRR`, an FPF-level corpus object, a single wording repair, a source-use decision, or a project-side evidence, assurance, gate, release, safety, compliance, work, or decision claim. Use `E.9.DA`, `E.2.DA`, `E.10` and precision-restoration neighboring patterns named by value, or the project-side pattern governing the claim for those objects.

First useful move: recover the required scope from the governing request, `E.22` frame, campaign seam, landing check, release check, or review assignment; then name the governing pattern of concern, required scope, working reader, intended use, and qualification window; then evaluate every coordinate in `RequiredPatternQualityCoordinates` with a value and short rationale.

`floorEvaluation` changes the declared floor and expected evidence economy. It never creates a partial `E.21`, inactive coordinates, overlay-trigger shortcuts, narrowing to an easier use, blocker-only substitution, or a permission to skip precision-restoration discharge. Fragmentary, wrong-shaped, or weak pattern text is still evaluated under the required scope; weakness receives low coordinate values, repair status, architecture hold, or refresh status.

What goes wrong if missed: pattern quality becomes taste, checklist closure, source count, review state, landing state, or length. Short patterns can pass while missing mature content; long patterns can pass while hiding the first user-facing action; semio material can take over a non-semio pattern.

What this pattern buys: one scoped quality claim over one pattern of concern, one complete coordinate set, explicit evidence basis, adjacent-value rationales, and a visible stop, repair, hold, or refresh status.

Primary EntityOfConcern in plain terms: the quality claim of one governing FPF pattern of concern for a declared use.

### E.21:2 - Problem

FPF patterns need a quality evaluation that is stronger than a style checklist and lighter than a project assurance audit. Earlier review habits produced two opposite failures:

1. **Too weak.** A reviewer marks a pattern "ready" because no blocker is obvious, because it landed, or because headings exist.
2. **Too heavy.** A reviewer adds more warnings, evidence cards, source rows, boundary notes, and process residues until the pattern becomes harder to use.

`E.21` solves this by measuring the pattern of concern against one complete coordinate set. The coordinates ask whether the pattern is usable, coherent, current, precise, affordable, mature enough for its claim, and safe from proxy improvement.

### E.21:3 - Forces

| Force | Tension |
|---|---|
| Comparability vs false precision | Pattern versions must be comparable, but ordinal qualities cannot be averaged. |
| Completeness vs affordability | Every coordinate is evaluated; rationale and evidence can stay compact. |
| Maturity vs length | A short pattern is mature only when selected mature-pattern ingredients are present in the body or neighboring pattern governing the claims. |
| Ontology vs usability | Names and kinds must be precise enough for the governed use without burying the first user-facing action. |
| Semio precision vs semio-bias | Episteme and publication distinctions matter, but non-semio patterns still lead with their own `EntityOfConcern`. |
| Open-ended improvement vs stop | Improvement can continue forever, while one version needs a scoped stop condition. |

### E.21:4 - Solution

`E.21` is the FPF pattern-quality specialization of `A.19.ECS`. It evaluates one pattern of concern under one declared quality claim.

There is one evaluation shape:

1. frame the object and use;
2. apply the ordinal scale to every required coordinate;
3. justify each value with `ShortRationale`;
4. assign `PatternQualityStatus`;
5. state stop, repair, architecture hold, or refresh condition;
6. when improvement is requested, return proposal rows without changing the coordinate result into a work plan.

There is no separate pre-check result. If a pattern lacks frame, first move, source basis, mature comparison, or naming clarity, the relevant coordinates fall.

#### E.21:4.1 - Local names and kind settlement

| Local name | Kind and function |
|---|---|
| `PatternQualityEvaluation` | Authored quality evaluation record over one pattern of concern. |
| `PatternOfConcernRef` | FPF pattern named by value that this `E.21` evaluation makes the pattern of concern: host, monolith section, edition, or pinned version. `PatternOfConcern` is relation-relative: the same pattern can also be the pattern of concern in another use, review, or evaluation flow, for example when a reader selects, applies, or reviews that pattern. This row names the concern of the quality-evaluation flow, not a special kind of pattern and not a second text. The evaluated pattern also has its own primary `EntityOfConcern`: the subject that its Problem, Solution, or guidance is about. FPF patterns are applied to situations, claims, texts, or work objects. Use `governing pattern` only in the typed form `governing pattern for <claim, relation, or boundary>` when the pattern actually governs that specific item; use `related pattern` for a looser pattern relation; use `relation` only for the relation itself. |
| `ClaimScope` | Quality claim boundary recovered from the governing frame: ordinary use, authoring input, landing input, release input, external-review input, high-assurance reuse input, canonization input, or another explicitly requested pattern-quality use. It is not chosen by the evaluator to make a failing request pass. |
| `WorkingReaderScope` | Working-reader family, viewpoint, and first-use situation the pattern must serve. |
| `IntendedUse` | Action that may use the result: continue drafting, admit for declared use, repair, refresh, or compare candidates. |
| `QualificationWindow` | Edition, SoTA, related-pattern, release, time, or comparison window in which the evaluation is current. |
| `EvaluationEvidenceBasis` | Evidence loci named by value for the evaluation: pattern body version, host or monolith section, README scenario, ToC row, `E.11` entry-distribution locus, `I.2` expanded entry-disambiguation case when corpus-facing, card or retrieval cue when claimed, source-currentness locus when SoTA/currentness is valued, mature comparator set when maturity is valued, and worked case or absence of worked case when case coverage is valued. |
| `QualityEvaluationQuestionFrameRef` | `E.22` frame when purpose, floor, trade-offs, absorption, or proposal expectation needs to be declared. |
| `CoordinateValueRationales` | One row for every required coordinate: `Coordinate`, `Value`, `ShortRationale`. |
| `CoordinateEvidenceRefs` | Per-coordinate text, case, relation, SoTA, mature comparator, projection, or review refs where the short rationale depends on evidence outside the pattern body row being discussed. |
| `PrecisionRestorationProfile` | Compact profile over six precision-restoration layers: word, head, and use precision; phrase-level apparatus; repeated or distributed material; ontic and slot-relation clarity; description, publication, and source boundary separation; and pattern-application ontology. It collapses those layers into one scalar effect for the `E.21` result, not one coordinate per defect. The profile names present or bounded issues, checked absence scope when clean, affected coordinates, and the selected restoration or governing pattern such as `E.10`, `E.10.ARCH`, `F.18`, `F.19`, `E.24.CD`, `E.24.PUB`, or an object-specific pattern. |
| `DominanceSet` | Coordinates used to compare already evaluated candidate versions. It never changes the required coordinate set. |
| `PatternQualityStatus` | Scoped pattern-quality result assigned by `E.21`; it is not an `E.19` admission or refresh decision by itself. |
| `StopCondition` | Why improvement may stop, continue, refresh, or hold. |
Names are local to pattern-quality evaluation unless `F.18` promotes a durable name. They are not project evidence, release state, review state, or assurance.

#### E.21:4.2 - Evaluation record

```text
PatternQualityEvaluation:
  PatternOfConcernRef: <governing pattern of concern>
  ClaimScope: <declared quality claim>
  WorkingReaderScope: <reader and first-use situation>
  IntendedUse: <what may consume the result>
  QualificationWindow: <edition, source, neighbour, release, or comparison window>
  EvaluationEvidenceBasis: <checked pattern, corpus, source, comparator, case, and projection loci; missing or unchecked loci named explicitly when they affect values>
  PrecisionRestorationProfile: <collapsed profile: word, head, and use; phrase-apparatus; repetition-and-distribution; ontic-slot clarity; description-publication-source boundary; pattern-application; scalar effect, affected coordinates, and selected restoration or governing pattern>
  CoordinateValueRationales: <all required coordinates, values, short rationales>
  PatternQualityStatus: <status>
  StopCondition: <local stop, first repair, hold, or refresh>
```

#### E.21:4.3 - Ordinal scale, result row, and adjacent-value rationale

| Value | Label | Meaning |
|---:|---|---|
| 0 | `absent` | The characteristic is not expressed for the declared scope. |
| 1 | `namedOnly` | It is named or implied but not usable as quality evidence. |
| 2 | `partiallyExpressedForDeclaredUse` | It is present but incomplete, fragile, or insufficient for the declared use. |
| 3 | `sufficientlyExpressedForDeclaredUse` | It is usable for the declared scope, with limits visible. |
| 4 | `wellExpressedForDeclaredUse` | It is clear, evidenced, and bounded for the declared scope. |
| 5 | `exceptionallyExpressedForDeclaredUse` | It is exceptional for the declared use across reinforcing loci and cases, without hidden cost or neighbour loss. |

Values are ordinal content evaluations. They are not `U.Measure`s, averages, percentages, maturity-ladder steps, review votes, or landing status.

The result-bearing coordinate row has exactly this shape:

| Coordinate | Value | ShortRationale |
|---|---:|---|
| `<E.21 coordinate>` | `<0..5>` | `<assigned-value basis; why the lower adjacent value would understate the evidence; why the higher adjacent value would overstate the evidence, or for 5 what evidence makes 4 too weak and what would lower or reopen>` |

A two-column coordinate-and-value table, a narrative paragraph, a table whose comment lacks adjacent-value comparison, or a result whose value depends on unchecked external loci is not an `E.21` result. It is only draft evaluation material until every coordinate has a `ShortRationale` row and the result names the `EvaluationEvidenceBasis` used for values that depend on source, comparator, corpus, projection, or worked-case evidence.

A `ShortRationale` is allowed to be compact, but it is not allowed to be evidenceless. When the value depends on a source-currentness row, mature comparator, README scenario, ToC row, `E.11` entry-distribution locus, `I.2` expanded entry-disambiguation case, card, retrieval cue, monolith section, worked slice, near-miss, or anti-case, the rationale names that locus by value or says that the locus was missing or unchecked. "By value" means a recoverable section, row, case, checklist item, relation, source row, projection row, comparator id plus selected ingredient, or specific absent locus; a category list such as "entry, first move, boundaries, SoTA, checklist, relations" is not by-value discharge. Missing or unchecked evidence lowers the value for the coordinate that needs it; it does not create a separate "not evaluated" result.

A `5` is not a reward for clear early wording, named neighbour relations, or a well-formed field set alone. It needs exceptional expression for the declared use: reinforcing loci, a worked or otherwise replayable slice where the coordinate demands one, and no hidden cost or neighbour loss. When the evaluator cannot say why `4` would understate the evidence, assign `4` or lower.

When a coordinate's `5` meaning names a filled case, replayable slice, near-miss, anti-case, worked comparison, projection evidence, currentness basis, or selected-neighbour replay, absence of that evidence caps that coordinate at `4` even if the prose is otherwise strong. Do not hide the same absence only in `CaseCountercaseAndTransferCoverage`; lower every coordinate whose own `5` meaning needs that missing evidence. A `5` rationale names the reinforcing evidence loci that make `4` too weak.

For `MaturePatternParityAndSelectedContentSufficiency`, the rationale names a mature-pattern comparison set and the selected mature ingredients being claimed. For non-epistemic patterns, include at least one mature non-epistemic comparator when one exists: work, method, role, system, control, architecture, selection, engineering-action, or another pattern whose primary `EntityOfConcern` is not an episteme or publication. Value `4` requires by-value discharge of selected ingredients in the body or neighboring pattern governing the claims; comparator IDs plus a generic "main ingredients are present" sentence are only value `3`. The comparison is not a length target and not permission to copy semio apparatus.

For a `4` or `5` on `MaturePatternParityAndSelectedContentSufficiency`, include a compact maturity-discharge payload in the rationale or `CoordinateEvidenceRefs`: `comparator=<pattern id>; selectedIngredient=<ingredient name>; currentLocus=<section, row, case, checklist item, relation, or neighboring pattern governing the claim>; missingOrLowering=<absent or weak ingredient, if any>`. A category list such as "frame, first move, neighbour relations, CC, SoTA, relations" without current loci is still value `3`, even when the listed categories are plausible mature ingredients.

#### E.21:4.3a - Precision-restoration profile

Before assigning the coordinate table, record one `PrecisionRestorationProfile`. This is not an optional scan and not a lexical grep result. It is a pattern-text-use attention discharge: the evaluator asks which governed object, claim, relation, and reader use the sentence, table, section, or repeated content family serves in the pattern of concern.

Use this compact shape:

```text
PrecisionRestorationProfile:
  overallEffect: <clean | boundedLocal | lowersCoordinates | repairBeforeUse>
  wordHeadUsePrecision: <clean | E.10, E.10.ARCH, F.18, or governing pattern needed | lowers coordinates>
  kindRestorationCheck: <pre-repair kind, relation, current ontic slot, relation position, use relation, or claim kind, and admissible use -> proposed post-repair kind, relation, current ontic slot, relation position, use relation, or claim kind, and admissible use; preserved | split | intentionally changed | blocker>
  phraseApparatus: <clean | F.19 needed | lowers coordinates>
  repetitionAndNegativeDistribution: <clean | bounded-local | lowers coordinates>
  onticAndSlotRelationClarity: <clean | hidden candidate ontic or slot-relation drift | lowers coordinates>
  descriptionPublicationSourceBoundary: <clean | description-publication-source boundary leakage | lowers coordinates>
  patternApplicationOntology: <clean | application relation unclear | lowers coordinates>
  checkedLoci: <sections, rows, cases, and relations checked>
  affectedCoordinates: <coordinates lowered or protected>
  repairProposal: <repair, no-repair disposition with loci, or owning locus>
```

This profile deliberately collapses several small diagnostic checks into one scalar effect. The scalar is the strongest quality effect that any layer requires: clean, bounded local repair, coordinate lowering, or repair-before-use. The layers are diagnostic, not extra coordinates, checklists, or proposal quotas. A new precision-restoration symptom is classified into one of these layers or assigned to the selected restoration or governing pattern; it does not mint a new `E.21` coordinate. Details belong in the patterns that govern those objects: word, head, and name problems apply `E.10`, `E.10.ARCH`, or `F.18`; phrase-level boilerplate and plain-technical rewriting apply `F.19`; hidden candidate ontics and ontic-vs-description-vs-publication boundaries apply `E.24.CD`, `E.24.PUB`, or the direct subject pattern when the governed object is already clear; claim, relation, evidence, work, decision, assurance, publication, or pattern-application problems apply the pattern that governs that object. `E.21` consumes only the result: which coordinates fall, which stay protected, and what repair would make the quality claim true.

When this layer finds a hidden candidate ontic or publication-form confusion, `E.21` records the quality effect and affected coordinates only. Candidate detection, ontic placement, slot-relation design, and publication-boundary repair remain with `E.24.CD`, `E.24.PUB`, or the direct governing pattern. A quality evaluation does not become an ontic-discovery pattern by noticing that defect.
The `kindRestorationCheck` is required whenever a precision-restoration finding or repair proposal changes wording. It records the meaning-bearing object, kind, relation, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope before and after the proposed repair, then names the governing pattern when another pattern governs the affected kind, relation, claim, or position (`A.6.0`, `A.6.5`, `A.6.P`, `C.29`, `A.15`, `E.24.CD`, `E.24.PUB`, `E.10.ARCH`, or another governing pattern). `E.21` does not restate slot discipline, ontic architecture, publication-form discipline, or mathematical-lens ontology; it only checks that the repair preserved or deliberately changed them by value. The check is a bounded complete preservation proof, not a blanket demand to formalize every sentence and not a license to do the least visible work. Complete means every field whose value can drift because of the changed wording receives one explicit disposition: `not triggered`, `ordinary prose`, or `no FPF-governed phrase changed` with checked loci, `preserved`, `split`, `intentionally changed by accepted decision`, or `blocker`. A no-repair result is valid only as one of those dispositions with loci; "nothing to do" without that discharge is a missing repair. Expand the row only when a kind, relation, claim, current ontic slot, relation position, use relation, or claim kind, or admissible use can drift. A lexical replacement is not a repair when it only removes a trigger word, substitutes one umbrella for another, narrows a graph or method into a work sequence, widens a work occurrence into a method, turns a publication form or evidence source into the object itself, or otherwise changes kind or current ontic slot, relation position, use relation, or claim kind without an accepted decision. If the kind or current ontic slot, relation position, use relation, or claim kind cannot be recovered, the profile is at least `lowersCoordinates`; if the proposed repair would change kind or current ontic slot, relation position, use relation, or claim kind and no accepted DRR or governing pattern justifies that change, the result is `repairBeforeUse` or `holdForArchitectureDecision`.

When the profile is not clean, lower every affected coordinate named by the profile. Do not hide a present precision-restoration issue only in `EntityOfConcernPrimacyAndSemioBiasResistance`, and do not raise the result through related-pattern-boundary praise, projection evidence, or "correct but true" guards when the profile shows that those materials compete with the positive subject-and-action spine.

#### E.21:4.4 - RequiredPatternQualityCoordinates

Every `E.21` evaluation of an FPF pattern of concern evaluates every coordinate below.

| Coordinate | What it evaluates |
|---|---|
| `WorkingSituationAndUseBoundaryRecognizability` | Whether the reader recognises the situation, ordinary use, non-use, harm if missed, and boundary early. |
| `EntityOfConcernAndClaimScopeStability` | Whether the primary `EntityOfConcern` and quality-claim scope stay stable across title, Problem frame, Solution, cases, checklist, relations, and status. |
| `PatternApplicationGuidance` | Whether the Solution gives usable pattern-application guidance after the first move is recovered. |
| `ClosureAndBoundedNonUseRecoverability` | Whether stop conditions, repair conditions, bounded non-use, and any `governing pattern for <claim, relation, or boundary>` statements are recoverable. |
| `SemanticKindAndNameRecoverability` | Whether names, kinds, relations, qualifiers, and claim boundaries recover the same FPF interpretation. |
| `NeighborAuthorityAndBoundedUseFit` | Whether evidence, assurance, measurement, naming, work, gate, decision, publication, release, and project claims stay with the pattern that governs each claim, relation, or boundary. |
| `EntityOfConcernPrimacyAndSemioBiasResistance` | Whether the pattern leads with its own `EntityOfConcern` and action guidance instead of letting description, publication, source, evidence, review talk, standard non-use warnings, precision-repair material, quality or projection evidence, package rationale, or cross-pattern reference boilerplate take over. The `PrecisionRestorationProfile` supplies the collapsed diagnosis across word, head, and use precision; phrase apparatus; repetition-and-distribution; ontic-slot clarity; description-publication-source boundary separation; and pattern-application ontology. This coordinate consumes that profile by lowering the value when those materials compete with the positive subject-and-action spine. Semio-bias is one special case when the displaced content concerns descriptions, sources, publications, notes, records, diagrams, or evidence-like publications. |
| `PracticalUseDeltaAndHarmPrevention` | Whether the pattern changes a real reader use, prevents a named misuse, reduces a named cost, or preserves a named boundary. |
| `UseAffordabilityAndApparatusProportionality` | Whether ordinary first use stays affordable and heavier apparatus appears only when it buys admissible use. |
| `RepairLocalityAndChangeImpactPredictability` | Whether repairs have the smallest locus and predictable downstream impact. |
| `ProxyForValueSubstitutionResistance` | Whether the evaluation asks what became worse when visible quality coordinates improved, and applies `E.13` when a visible quality value, metric, review result, or release cue is being used as the practical value itself. |
| `ClaimJustificationTraceabilityCurrentnessAndReplayability` | Whether the claim is replayable from pinned text, scope, evidence, currentness basis, limitations, status, and stop reason. |
| `CaseCountercaseAndTransferCoverage` | Whether positive cases, near-misses, anti-cases, and transfer cases match the breadth claimed. |
| `MaturePatternParityAndSelectedContentSufficiency` | Whether selected mature-pattern ingredients are present in the body or related patterns for this `EntityOfConcern` and use. |
| `SoTABindingAndCurrentness` | Whether current best-known practice changes the pattern and has reopen and currentness discipline. |
| `FormalClaimAdmissibilityAndLensFit` | Whether measurement, scale, comparison, formal model, simulation, causal, mathematical, QL, or learned-lens claims are admissible for their stated use, bounded to the governing pattern that owns the claim, or correctly absent. |
| `FalsifiabilityAndLoweringCondition` | Whether coordinate values, status, and stop claims say what would raise, lower, or reopen the evaluation. |
| `CorpusEntryProjectionAndEcologyFit` | Whether README scenarios, ToC query cues, Preface cues, `E.11` entry-distribution loci, `I.2` expanded entry-disambiguation cases, cards, summaries, retrieval snippets, durable names, relations, and corpus ecology preserve the scoped quality result without becoming authority-bearing publication faces, stale echoes, or pattern content. Corpus-entry and projection evidence belongs in the `E.21` result, `E.19` run record, README, ToC, `E.11`, `I.2`, retrieval or card publication locus, or other quality evaluation locus unless the pattern of concern's own `EntityOfConcern` and user-facing action are that projection or evaluation work. |
| `EvolutionFrontAndRefreshDiscipline` | Whether variants, fronts, archives, refresh windows, and smallest-reopen rules preserve open-ended evolution without endless polishing. |

Constraint, harm, safety, security, compliance, deontic, self-application, recursion, and high-assurance questions do not add a second coordinate family. Evaluate them through the coordinate that owns the content: related-pattern authority, traceability, formal-claim admissibility, falsifiability, affordability, corpus ecology, evolution, or refresh.

**Coupled-flow unity and separation for pattern quality.** An `E.21` run evaluates a `PatternOfConcernRef` inside a development, refresh, or admission flow. Another flow may make the same pattern a pattern of concern for a different use relation, for example a practitioner selecting and using it, a reviewer applying it to another text, or a subsequent evaluator reopening it. One `TransformationFlowStructure` may join pattern development, pattern use, use-found evaluation, and repair or refresh flows through transfer, feedback, return, edition-change, or projection relations. Keep three positions distinct in each sentence: the pattern as concern of the current flow, the intended reader addressed by the pattern, and the pattern's own primary `EntityOfConcern` inside its Problem, Solution, or guidance. `E.21`, `E.19`, handoffs, ledgers, README, ToC, `E.11`, `I.2`, retrieval checks, and landing evidence are checking operations or evidence loci in the development or evaluation flow. They can cause edits to the pattern, but they are not automatically user-facing content for the reader addressed by the pattern. `DesignRunTag` stays on the subject-context, claim, work, trace, publication-form relation, or source relation inside the transformation-flow structure; it does not decide whether a pattern is current, obsolete, under development, or being used. Treat FPF pattern development as the local pilot case: quality-loop proof changes the pattern through edits, not by being copied into the pattern.

#### E.21:4.4a - Frequent value-3, value-4, and value-5 calibration points

These rows calibrate common disagreements. They do not replace the coordinate definitions above.

| Coordinate family | 3 is typical when | 4 is typical when | 5 is typical when |
|---|---|---|---|
| `WorkingSituationAndUseBoundaryRecognizability` | The use situation is recoverable but late, abstract, or missing harm, payoff, or non-use detail. | The situation, first move, harm, payoff, and non-use are early and clear. | Early recognition is reinforced by a filled or replayable first-use slice showing that a cold practitioner can enter correctly. |
| `EntityOfConcernAndClaimScopeStability` | The primary object is named but related record, evidence, lens, or project claims keep pulling the scope. | The primary `EntityOfConcern` and claim scope stay stable, with bounded related-pattern material. | Scope stability is reinforced across title, recognition text, Solution, worked or replayable case material, checklist, relations, and non-use without any local apparatus stealing attention. |
| `PatternApplicationGuidance` | The first action is named but only partly executable, or the Solution mostly assigns governing loci instead of giving this pattern's own action. | The first action and continuation are executable in this pattern's own subject terms; related-pattern statements are declarative, compact, and late. | The application guidance is demonstrated by a filled worked slice or equivalent replayable evidence. |
| `ClosureAndBoundedNonUseRecoverability` | Non-use or related-pattern statements are present but not tied to stop, repair, or lowering conditions. | Stop, repair, bounded non-use, and governing-pattern statements for specific claims, relations, or boundaries are recoverable for declared use. | A worked stop, overturn, or non-use case shows how closure changes status or the next applicable pattern relation. |
| `NeighborAuthorityAndBoundedUseFit` | Related patterns are named but some authority split remains generic, future-pattern-like, ambiguous, role-nicknamed, or too early in the Solution. | Related patterns named by value and limited declarative relations are clear enough for declared use and do not replace the pattern's own content. | Related-pattern authority is replayable across examples, relations, and overread cases, with pattern application and authority kept explicit. |
| `EntityOfConcernPrimacyAndSemioBiasResistance` | The pattern is about its object but one or more precision-restoration layers lead or leak into the pattern in a developer, reviewer, or evaluator role. | The pattern leads with its own object and application guidance; auxiliary material is compact, declarative, and late; role, slot, publication-form, source, locus, flow, and status words are used only when they add a real kind, relation, evidence value, or user-facing action; quality or projection evidence about the pattern stays outside the pattern. | The primary object and application guidance are first recoverable across recognition text, Solution, cases, and checks even when auxiliary material is present, and any precision-restoration, quality, or projection material is in its proper evaluation, projection, or publication locus rather than in the pattern. |
| `PracticalUseDeltaAndHarmPrevention` | The prevented harm is named but not demonstrated. | The pattern changes a recoverable use and blocks named misuse for declared use. | A worked or near-miss case shows the practical delta, cost of the missed pattern, and prevented harm. |
| `UseAffordabilityAndApparatusProportionality` | The first move exists but apparatus is heavy for ordinary readers. | Ordinary first use is affordable and heavier apparatus opens only when useful. | A minimal first-use example shows the thin ordinary use works before heavy apparatus. |
| `RepairLocalityAndChangeImpactPredictability` | Repair conditions or related-pattern relations are named but downstream impact is not shown. | Repairs have local loci and predictable impact for declared use. | A worked repair or downstream-impact slice shows the smallest locus and changed related-pattern relation. |
| `ProxyForValueSubstitutionResistance` | Proxy risks are named but "what got worse" is not applied. | The pattern blocks visible proxy substitutions and asks what worsened. | A proxy-failure case shows a visible improvement damaging intended value, and the pattern prevents that stop. |
| `ClaimJustificationTraceabilityCurrentnessAndReplayability` | Fields or sources exist but replayability and currentness basis are incomplete. | The claim can be replayed from pinned text, evidence, currentness basis, status, and stop reason. | A filled evidence and currentness slice shows how the claim is replayed and when it reopens. |
| `CaseCountercaseAndTransferCoverage` | Archetypes are listed, but no filled worked case or near-miss exercises the claim. | At least one filled worked case plus a near-miss or anti-case covers the declared use. | Heterogeneous cases, countercases, and transfer slices cover the breadth claimed. |
| `MaturePatternParityAndSelectedContentSufficiency` | Mature comparators are named or implied, but selected mature ingredients are not discharged by value. | Mature comparators are named and selected ingredients are discharged by value in the body or related patterns named by value. | Mature parity is shown across reinforcing body sections, related patterns, omissions, cases, and lowering conditions without copying irrelevant apparatus. |
| `SoTABindingAndCurrentness` | Sources are relevant and not decorative, but currentness, source-use status, or reopen conditions are compact or incomplete. | Decision-governing sources state adopt, adapt, or reject disposition, content mutation, currentness window, and reopen condition. | The pattern compares current best-known practice against popular, official, or lineage alternatives and carries the resulting source decisions into solution, cases, boundaries, and refresh. |
| `FormalClaimAdmissibilityAndLensFit` | Formal, scale, lens, or measurement terms are bounded but not exercised. | Formal, lens, and measurement claims are admissible for their stated use, bounded, and governed by the related pattern that owns the claim when the evaluated pattern makes such claims. | A worked formal, lens, or scale comparison shows what is preserved, lost, admissible, and not proved. |
| `FalsifiabilityAndLoweringCondition` | Stop, waiver, or non-use fields exist, but lowering and reopen triggers for the main claims are mostly implicit. | The pattern states explicit lowering and reopen triggers for its main claims; named fields alone do not reach `4` unless they say what evidence change lowers, overturns, rejects, or reopens the claim. | Worked lowering or overturn cases show how values, status, or use change. |
| `CorpusEntryProjectionAndEcologyFit` | Host text is coherent, but README, ToC, `E.11`, `I.2`, card, retrieval, monolith, or projection evidence is absent for a corpus-facing claim, or that evidence is placed anywhere in the pattern as method, note, appendix, relation, rationale, or quality-status content about the pattern. | Corpus-facing entry or projection loci are named and aligned enough for the declared use, and their evidence stays in the evaluation, result, or projection locus rather than entering the pattern. | Retrieval, stale-projection, cold-reader, or projection-update evidence shows corpus ecology stays aligned after change without leaking into the pattern. |
| `EvolutionFrontAndRefreshDiscipline` | Reopen is delegated to related patterns or implied by source-return. | The smallest reopen locus, source or currentness trigger, or variant or front condition is explicit. | Variant, front, archive, or ongoing refresh discipline is replayable for the declared use. |

For `EntityOfConcernPrimacyAndSemioBiasResistance`, do not compensate a bad `PrecisionRestorationProfile` with `NeighborAuthorityAndBoundedUseFit` or `CorpusEntryProjectionAndEcologyFit`. This is a pattern-text-use evaluation, not a lexical search: ask which governed object, claim, relation, and reader use the sentence serves. Material about developing, reviewing, projecting, landing, evaluating, or proving this pattern's quality belongs in the evaluation, projection, release, or publication locus that owns that work, not in the pattern. Related-pattern statements named by value can be true and still damage the pattern of concern when they appear before the pattern's own `EntityOfConcern` and application guidance are recoverable. If the opening Problem frame or Solution starts with precision-restoration material before the pattern's own subject and move, this coordinate is at most `2`; if a positive action exists but the reader must traverse that material across sections to find it, it is at most `3`. Compact related-pattern statements belong in `Relations` or short late boundary rows and must preserve kind. Local boundary prose is admissible only when it states a documented local confusion and local stop condition not already carried by the owning pattern for that specific distinction or claim boundary. Also lower `PatternApplicationGuidance`, `WorkingSituationAndUseBoundaryRecognizability`, `PracticalUseDeltaAndHarmPrevention`, and `UseAffordabilityAndApparatusProportionality` when the profile shows that precision-restoration issues displace first-use content.
If the declared use is `Stable`, landing-input, release-input, external-review-ready, or another corpus-facing use, the evaluation must use evidence for corpus entry and projection coordinates. A host-only body evaluation can still evaluate the pattern body, but it cannot silently turn missing README, ToC, `E.11`, `I.2`, card, retrieval, monolith, or projection evidence into a high `CorpusEntryProjectionAndEcologyFit` value.

#### E.21:4.5 - Status and stop condition

| Status | Meaning |
|---|---|
| `admissibleForDeclaredUse` | Every coordinate meets the declared floor for the scoped use, and bounded non-use is stated. |
| `repairBeforeUse` | One or more coordinate floors fail for the declared use. |
| `holdForArchitectureDecision` | The defect is not local prose; `EntityOfConcern`, neighbour authority, split, merge, or placement must be decided. |
| `refreshNeeded` | A SoTA, neighbour, terminology, retrieval, telemetry, use-scope, or corpus change invalidates a previous evaluation. |

Default floor is `4 wellExpressedForDeclaredUse` on every coordinate for ordinary practitioner use, authoring-input use, landing-input use, `Stable`, external-review-ready, release-input, canonization-input, stop-improving claims, and ordinary improvement-loop use. A diagnostic or exploratory request still measures every coordinate and reports values; it does not create an admissible-use shortcut. If the assignment asks for corpus-facing, landing-input, `Stable`, release, or external-review use, the evaluator measures that required use and returns `repairBeforeUse`, `holdForArchitectureDecision`, or `refreshNeeded` when the floor is missed.

An all-`5` result is a local exceptional result under the declared scope and qualification window. It is not a permanent end of development. `E.23` can reopen improvement when use, source, comparison set, front, affordability, or payoff changes.

#### E.21:4.6 - Compact result form

An `E.21` result uses this result-bearing form:

```text
E.21 result:
  Pattern of concern: <PatternOfConcernRef>
  Declared scope, use, reader, and window: <ClaimScope, IntendedUse, WorkingReaderScope, QualificationWindow>
  Evidence basis checked: <EvaluationEvidenceBasis>
  Status: <PatternQualityStatus>
```

| PrecisionRestorationProfile | OverallEffect | KindRestorationCheck | Loci | AffectedCoordinates | RepairProposal |
|---|---|---|---|---|---|
| `<word, head, and use; phrase-apparatus; repetition-and-distribution; ontic-slot; description-publication-source; pattern-application profile>` | `<clean | boundedLocal | lowersCoordinates | repairBeforeUse>` | `<pre-repair and post-repair kind, relation, current ontic slot, relation position, use relation, or claim kind, and not-triggered, ordinary, preserved, split, changed, or blocker disposition>` | `<by-value loci or absence scope>` | `<affected coordinates or none>` | `<repair, no-repair disposition with loci, or owning locus>` |

| Coordinate | Value | ShortRationale |
|---|---:|---|
| `<all RequiredPatternQualityCoordinates rows>` | `<0..5>` | `<assigned-value basis; why not lower; why not higher or what would lower or reopen>` |

```text
First repair or stop: <repair | hold | local stop>
Reopen if: <smallest changed locus or condition>
```

Status is not assigned from a two-column table, a prose summary, a checklist count, an `E.19` pass or fail row, a table missing `ShortRationale`, a result missing the required `PrecisionRestorationProfile`, or a result missing the evidence basis needed for the values it claims. Such material can support a subsequent evaluation, but it is not the `E.21` result. Conversely, an `E.21` status is a pattern-quality status, not a release crossing: `E.19` or the release or admission process named by value still checks gate-specific carry-through, projection, monolith, packaging, authority, and non-overread conditions.

#### E.21:4.7 - Finding and proposal rows

```text
E.21 finding:
  Pattern of concern: <PatternOfConcernRef>
  Coordinate or status affected: <coordinate | status | stop>
  Pattern locus: <section, row, example, relation, source row, projection>
  Value or status effect: <value, status, floor, or stop impact>
  Correction direction: <what should change>
  Closure test: <what changed pattern text would show>
```

When `E.22`, `E.23`, returned-finding absorption, or `exceptionalImprovementEvaluation` asks for improvements, add finding rows for every below-floor coordinate and proposal rows only for substantive non-dominated improvement opportunities inside the declared scope. Do not treat every value below `5` as a defect. For above-floor coordinates, the evaluator still searches by value when exceptional improvement is requested, but the proposal must name a content improvement such as stronger positive action guidance, a worked slice, case or countercase, source-currentness carry-through, mature-content discharge, relation cleanup, deletion of displaced apparatus, split of overloaded content, or another content gain. A `4` can be the correct stop value only with a checked no-proposal disposition showing why further content movement is dominated, unavailable, or outside scope.

### E.21:5 - Archetypal Grounding - worked slices

**Names named by value, no first move.** A pattern has precise Tech names and current source rows but no first user-facing action. `WorkingSituation...`, `PatternApplicationGuidance`, and `PracticalUseDelta...` fall; source currentness does not rescue ordinary use.

**Short architecture pattern.** A compact pattern has a triage form but no worked slice and no mature-pattern comparison. It can be useful as local expert reference material, but `MaturePatternParity...` and `CaseCountercase...` stay below exceptional until selected mature content is present.

**Precision-restoration profile in a non-semio pattern.** A pattern about architecture, work, system levels, method, P2W, or another non-semio `EntityOfConcern` tries to introduce the subject through a catalog of other claim kinds or objects that are outside its own subject. That catalog is unbounded because every EoC is outside infinitely many other EoCs. If copied boundary doctrine leads the Problem frame or Solution, `EntityOfConcernPrimacyAndSemioBiasResistance` falls to `2` or `3` even when every individual boundary is true. Repair by leading with this pattern's own `EntityOfConcern` and action spine, and replace copied boundary doctrine with one governing pattern id or one `governing pattern for <claim, relation, or boundary>` statement unless a documented local confusion needs an local stop condition not already carried there. If the same doctrine is spread across Problem frame, Solution, anti-patterns, checklist, and Relations, classify the aggregate under the profile's repetition-and-distribution layer and repair the distribution, not just each local sentence.

**Reference apparatus before Solution content.** A pattern's first Solution paragraph assigns other patterns or related-pattern mappings before it unfolds the ontology, method, norm, worked action, or other positive solution for the pattern of concern's own `EntityOfConcern`. Even if the related pattern id is correct, `PatternApplicationGuidance`, `EntityOfConcernPrimacyAndSemioBiasResistance`, `PracticalUseDeltaAndHarmPrevention`, and sometimes `NeighborAuthorityAndBoundedUseFit` fall. Repair by moving discoverability to README, ToC, `E.11`, `I.2`, or retrieval or projection loci, moving compact pattern-id or `governing pattern for <claim, relation, or boundary>` statements to `Relations` or a late boundary row, moving architecture-placement rationale to `DRR` or architecture documents, and rewriting the Solution to answer "what do I do with this pattern's EoC?" before any statement about another pattern.

**Overformalized precision.** A pattern uses correct FPF kinds, slots, references, and governing-pattern pointers so densely that the working reader cannot recover the first useful move, practical delta, or generalizing insight without doing an internal audit. Precision is then present but not usable. Lower `UseAffordabilityAndApparatusProportionality`, `WorkingSituationAndUseBoundaryRecognizability`, and sometimes `PatternApplicationGuidance`. Repair by keeping the ontology named by value only where it carries a current FPF-governed claim, moving restoration evidence to the evaluation result or DRR, and adding a short worked slice or plain recognition sentence that preserves the same kind without extra apparatus.

**QualityEvidenceLeakage in the pattern.** The pattern says that corpus projection, README, ToC, `E.11`, or `I.2` alignment, retrieval or cold-reader evidence, monolith parity, external-review readiness, landing evidence, `PatternQualityStatus`, all-`4` or all-`5` result framing, or another quality-result locus is what the user should do with the pattern's `EntityOfConcern`, or records developer, reviewer, or executor correspondence as if it were pattern content. The defect is not limited to `Problem frame`, `Solution`, examples, or checklist; notes, appendices, `Relations`, `Rationale`, `SoTA-Echoing`, tables, and conformance rows are also parts of the pattern in hosts and the monolith. That evidence may be required for `E.21`, `E.19`, landing, or retrieval loci, but it is not automatically a user action in the pattern of concern. Lower `EntityOfConcernPrimacyAndSemioBiasResistance`, `PatternApplicationGuidance`, `UseAffordabilityAndApparatusProportionality`, and `CorpusEntryProjectionAndEcologyFit` when this evidence enters the pattern. Repair by moving the evidence to the `E.21` result, `E.19` run record, README, ToC, `E.11`, `I.2`, card, retrieval, projection, or release or landing evidence locus, and keeping in the pattern only the user-facing move or boundary that follows from that evidence.


**Quality table without rationale.** A result gives values but no adjacent-value rationale. Values are unsupported. Add `ShortRationale` or lower.

**Goodharted improvement.** A rewrite improves source refs and proof sketches but becomes hard to use, or treats every non-`5` coordinate as a defect to be fixed with more apparatus. Re-evaluate affordability, repair locality, proxy-for-value, and corpus ecology before stopping. When exceptional improvement is requested, keep searching for content movement, not proof movement; record no-proposal only with loci showing that further content change is dominated, unavailable, or outside scope.

### E.21:5.1 - Bias-Annotation

`E.21` resists Goodhart-style quality substitution: a high value is not produced by length, source count, approval state, checklist closure, or elegant phrasing when the required coordinate evidence is absent. It also blocks semio-bias by checking whether the evaluated pattern leads with its own `EntityOfConcern` and user-facing action rather than with description, publication, source, review, or repair apparatus.

### E.21:6 - Conformance checklist

| Check | Requirement |
|---|---|
| `CC-E21-1` | Recover `ClaimScope` from the governing request, `E.22` frame, campaign seam, landing check, release check, or review assignment; then name `PatternOfConcernRef`, `ClaimScope`, `WorkingReaderScope`, `IntendedUse`, `QualificationWindow`, and `EvaluationEvidenceBasis`. |
| `CC-E21-2` | Evaluate the full `RequiredPatternQualityCoordinates` set. |
| `CC-E21-2a` | Before assigning coordinate values, record one `PrecisionRestorationProfile` with word, head, and use; phrase-apparatus; repetition-and-distribution; ontic-slot; description-publication-source; and pattern-application layers. A missing, grouped, or memory-only profile makes the `E.21` result incomplete. |
| `CC-E21-3` | Use the result-bearing three-column table: coordinate, value, and `ShortRationale`; a two-column coordinate-and-value table is not an `E.21` result. |
| `CC-E21-4` | Let `floorEvaluation` change floor and evidence cost only, not the coordinate set. |
| `CC-E21-5` | Assign values from checked pattern content and named content evidence, not review, landing, popularity, praise, or absence of prior use. |
| `CC-E21-6` | For corpus-facing values, name the checked README, ToC, `E.11`, `I.2`, card, retrieval, monolith, or projection loci, or lower the affected coordinate when those loci are missing or unchecked. |
| `CC-E21-6a` | Keep corpus-projection; README, ToC, `E.11`, and `I.2` alignment; retrieval or cold-reader evidence; monolith-parity; `PatternQualityStatus`; developer, reviewer, and executor correspondence; and other quality evidence out of the pattern unless the pattern's own `EntityOfConcern` and user-facing action are that evaluation or projection work. Part E patterns may govern FPF-pattern authoring, review, evaluation, entry, or publication as their subject matter; that does not license rationale or instructions about developing the same pattern version. This is a role test, not a word-list test. If such material appears anywhere in the pattern, including notes, appendices, `Relations`, `Rationale`, `SoTA-Echoing`, examples, tables, conformance rows, or any other host or monolith pattern section, as development, review, projection, or quality-status content about the pattern, lower `CorpusEntryProjectionAndEcologyFit`, `EntityOfConcernPrimacyAndSemioBiasResistance`, and the affected action or usability coordinates. |
| `CC-E21-7` | For any `5`, name the reinforcing evidence loci required by that coordinate's `5` meaning; otherwise lower the coordinate to `4` or below. |
| `CC-E21-8` | For `MaturePatternParityAndSelectedContentSufficiency = 4` or `5`, include a compact maturity-discharge payload: comparator id, selected ingredient, current locus, and missing or lowering item if any; category lists without loci cap the coordinate at `3`. |
| `CC-E21-9` | Make SoTA rows adopt, adapt, or reject current practice and change the pattern. |
| `CC-E21-10` | Keep measurement, score, scale, formal, causal, mathematical, QL, simulation, representation, or learned-lens claims under `C.16`, `A.17`, `A.18`, `A.19`, or the pattern that governs the claim when the evaluated pattern makes those claims. |
| `CC-E21-11` | State floor satisfaction, remaining bounded non-use, and lowering or reopen conditions in any stop claim. |
| `CC-E21-12` | Keep coordinate rationale separate from improvement proposal rows. |
| `CC-E21-13` | Keep quality results out of project evidence, assurance, gate, work, safety, compliance, release, and publication truth claims. |
| `CC-E21-14` | Do not raise a pattern with a bad `PrecisionRestorationProfile` through related-pattern-boundary, projection, or quality-result praise. When the profile shows defects before the pattern of concern's primary subject action is recoverable, or enough volume to compete with the Solution, lower `EntityOfConcernPrimacyAndSemioBiasResistance` and the affected action and usability coordinates; do not offset that loss with generic related-pattern-boundary praise or correct corpus projection evidence. |
| `CC-E21-15` | Keep ordinal values as measurement results, not repair targets. Below-floor values require findings or repair. Values at or above the floor receive proposal rows only for concrete non-dominated content opportunities when improvement is requested; a non-`5` value is not automatically a defect. No proposal may raise a value by adding quality proof, guards, relation catalogues, or process evidence that worsens use, affordability, locality, ecology, or the positive subject-and-action spine. A no-proposal disposition must name checked loci and why no substantive content improvement remains. |

### E.21:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| **Score illusion.** `Pattern quality = 87 out of 100`. | Use ordinal coordinate values; no arithmetic aggregation. |
| **Two-column table.** Coordinate-and-value table has no rationale. | Add `ShortRationale` for every coordinate. |
| **Floor as omission.** A floor evaluation omits maturity, SoTA, formal, corpus, or evolution coordinates. | Keep floor low if needed; evaluate all coordinates. |
| **Scope laundering.** A landing-input, corpus-facing, `Stable`, release, or external-review request is reported under an easier use, local-only use, diagnostic pass, or evaluator-selected use. | Re-evaluate under the governing scope; if it fails, return `repairBeforeUse`, `holdForArchitectureDecision`, or `refreshNeeded` with the missed coordinates and repairs. |
| **Administrative proxy.** "4 because landed" or "3 because not externally reviewed". | Evaluate pattern content. |
| **Comparator-free or locus-free maturity.** `MaturePatternParity... = 4` by impression, comparator IDs only, or category list such as "frame, first move, checklist, SoTA, relations". | Name mature comparison patterns and use the maturity-discharge payload: comparator, selected ingredient, current locus, and missing or lowering item. Without that payload, cap at `3`. |
| **Omission account as maturity.** A note explaining absence raises the value. | Add content to the body or neighboring pattern governing the claim, lower value, or mark the current request `repairBeforeUse`. |
| **Semio-biased maturity.** Non-semio pattern is judged by episteme or publication exemplars only. | Include non-epistemic mature comparators and score action on the primary `EntityOfConcern`. |
| **Quality-evidence leakage.** Corpus projection, retrieval evidence, README, ToC, `E.11`, or `I.2` alignment, monolith parity, `PatternQualityStatus`, developer, reviewer, or executor correspondence, or other quality evidence is written anywhere in the pattern as method, problem, note, appendix, relation, rationale, or status content about the pattern. | Move the evidence to the `E.21` result, `E.19` run record, README, ToC, `E.11`, `I.2`, card, retrieval, projection, or release or landing evidence locus; keep only the user-facing action or boundary that the evidence justifies. |
| **Apparatus overwrap.** A simple FPF claim is wrapped in extra role, publication-form, locus, flow, state, status, text-state, package, or process words, such as `current pattern text`, `current object`, `active record`, `field used in the current pass`, or route-like pattern talk where no real state or use relation is named, so the reader sees a bureaucratic apparatus instead of the object, relation, action, or boundary. | Apply `F.19`; record the scalar effect in `PrecisionRestorationProfile`, then lower the affected coordinates or name the completed repair. |
| **Apparatus maximalism.** Every pattern gets evidence cards, telemetry, archives, and companions. | Keep evidence compact unless it changes value, status, stop, or candidate comparison. |
| **Quality veto theatre.** "Not ready" has no E.21 coordinate named by value, evidence, status effect, and repair. | Rewrite as an `E.21` finding or remove the veto. |

### E.21:8 - Consequences

| Benefit | Trade-off or mitigation |
|---|---|
| Pattern quality becomes inspectable without a fake score. | Authors must name scope and all coordinate values. |
| Compact evidence remains possible. | The coordinate table is still complete. |
| Maturity claims become harder to fake. | Mature-pattern comparison adds cost where maturity or corpus-facing use is claimed. |
| Semio-bias becomes visible. | Semio distinctions remain auxiliary unless they are the pattern's own `EntityOfConcern`. |
| Stop decisions become less taste-based. | Open-ended improvement remains possible through `E.23` when a stronger aim is requested. |

### E.21:9 - Rationale

`E.21` keeps the measuring device simple: one object kind, one ordinal scale, one required coordinate set, one status set, and one stop condition. The evaluation never asks whether a coordinate is active. It asks what value the current pattern and its named evidence basis earn under the declared use.

The mature-pattern parity coordinate is deliberately strict because recent short patterns looked formally clean while lacking the worked slices, source carry-through, lowering conditions, and transfer coverage present in mature FPF patterns. The repair is not "make everything long"; it is "carry the selected mature ingredients that the declared use needs."

### E.21:10 - SoTA-Echoing

| Claim | Source-use disposition | Concrete E.21 effect |
|---|---|---|
| Feedback connects desired state, current state, next action, and available tactics. | Adopt from formative-assessment lineage such as Sadler and Hattie and Timperley. | `ShortRationale` and proposal rows are separated: value now, next improvement when requested, and checked no-proposal when no substantive improvement remains. |
| Questions and metrics derive from the goal. | Adopt from GQM and GQM+Strategies measurement discipline. | Scope, reader, use, and window precede coordinate values. |
| Multi-criteria improvement needs explicit trade-offs. | Adopt from MCDA, Pareto, ATAM, and current QD and OEE lines. | Dominance comparisons and protected trade-offs replace one-score closure. |
| Proxy optimization can make intended value worse. | Adopt from Goodhart and Campbell, management-accounting surrogation, reward-hacking, and specification-gaming lines. | `ProxyForValueSubstitutionResistance`, `PrecisionRestorationProfile`, `E.13`, and stop condition ask what got worse; `5`, all-`5`, discharge count, and proof apparatus cannot replace pattern content or pragmatic value. |
| Evaluation results are not governance, safety, or compliance proof. | Adopt as non-overread boundary from current evaluation-governance practice. | Neighbour authority and status boundaries keep project claims outside `E.21`. |

### E.21:11 - Relations

| Neighbour | Relation |
|---|---|
| `A.19.ECS` | Constructs or repairs the general evaluation `CharacteristicSpace`; `E.21` is one specialization. |
| `E.8.ECSPF` | Publishes an evaluation `CharacteristicSpace` as an FPF pattern when that form is selected. |
| `E.8` | Authors the pattern body whose quality `E.21` evaluates. |
| `E.19` | Runs admission and refresh review profiles; it can consume or request `E.21`, but it does not assign `E.21` coordinate values or replace the required pattern-quality table. |
| `E.22` | Frames purpose, floor, trade-offs, and proposal expectation before an evaluation. |
| `E.23` | Runs repeated improvement using `E.21` values and stop meanings for pattern versions. |
| `E.13` | Governs pragmatic utility and proxy-to-value alignment when quality values, visible measures, review results, all-`5` result framing, or release cues are used as practical value, target, incentive, gate, or improvement proof. |

| `E.9.DA` | Evaluates upstream `DRR` decision adequacy when pattern-quality defects trace to decisions. |
| `C.16`, `A.17`, `A.18`, `A.19` | Govern scale, coordinate, and measurement admissibility. |
| `F.18`, `E.10`, `A.6.P`, `C.2.P`, `C.16.P`, `C.16.Q` | Govern naming and wording-use precision when quality defects are lexical or ontological. |
| `A.10`, `B.3`, `A.20`, `A.21`, `A.15` | Govern project evidence, assurance, local CV state, gates, and work authority. |
| `E.11` and `I.2` | Govern entry-distribution and expanded entry-disambiguation cues; `E.21` supplies only the scoped quality result. |

### E.21:End

