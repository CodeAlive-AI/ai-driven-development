## A.19.ECS - Evaluation CharacteristicSpace Construction

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative

### A.19.ECS:1 - Problem frame

Use `A.19.ECS` when an object version is to be improved or judged, but the evaluation that says what "better" means is not yet available, not yet explicit, or not yet adequate for the object.

`A.19` says how a `CharacteristicSpace` is structured: declared characteristics, declared scales, slots, value sets, optional overlays, and no hidden normalization or aggregation. `A.19.ECS` says how to make such a `CharacteristicSpace` for the evaluated object, so that an evaluation can later read that object and `E.23` can run an improvement loop without inventing values.

The ordinary output is an evaluation characteristic-space specification: a grouped set of characteristics, scales, value meanings, evidence rules, missingness rules, protected trade-offs, status meanings, and stop or reopen conditions for one evaluated object kind and use scope.

**Not this pattern when.** If a suitable evaluation already exists, cite it and use `E.22` for question framing or `E.23` for repeated improvement. Use `A.17`, `A.18`, and `C.16` when the live problem is one characteristic, one scale, or measurement legality. Use `C.16.P` first when candidate coordinate wording still hides whether the live object is a characteristic, scale, coordinate, score, metric label, quality-term repair, or another receiving object. Use `A.19` when the live problem is the structure of `CharacteristicSpace` itself. Use `C.25` when the evaluated object is a composite engineering quality family that already fits Q-Bundle form. Use `F.18` when the live problem is durable naming. Use `E.21`, `E.9.DA`, or `E.2.DA` when the object is respectively one FPF pattern version, one `DRR`, or one FPF-level Pillar-adequacy evaluated object.

**First useful move.** State the sentence: "good as what kind of object, for which use, against which contrast cases?" Then name the evaluated object kind, the use scope, and at least three contrast cases: one admissible evaluated object, one below-floor evaluated object, and one not-applicable object.

**Cheap stop.** If the answer is "use this existing evaluation" and the evaluated object kind, use scope, floor, protected trade-offs, and stop meanings are already recoverable, do not construct a new `CharacteristicSpace`.

**What goes wrong if missed.** A team says "improve this" and then chooses convenient scores. A scale set appears from nowhere. Chairs, coal plants, nuclear plants, and FPF patterns all get compared on coordinates that do not distinguish the evaluated object kind. One visible value improves while the intended use gets worse. A review can say "better" but cannot say which object property changed, what trade-off was protected, or why improvement may stop.

**What this buys.** `A.19.ECS` gives improvement work a way to create the missing evaluation before the loop starts. It keeps `E.23` universal and simple: `E.23` changes the object and asks an evaluation to re-read it; `A.19.ECS` helps build that evaluation when none is yet adequate.

**Governed object in plain terms.** The governed object is the construction of one evaluation `CharacteristicSpace` for one evaluated object kind and declared use.

**Primary working reader.** The first reader is the engineer, analyst, pattern author, reviewer, steward, or method designer who must define what counts as improvement for an evaluated object before running an improvement loop.

### A.19.ECS:2 - Problem

FPF already has exact machinery for single characteristics, scales, coordinate readings, Q-Bundles, and repeated improvement. The gap is the construction of a useful grouped scale set for an evaluated object kind.

Recurring failures:

1. **Scale set from air.** An evaluation lists coordinates because they are familiar, not because they discriminate the evaluated object kind or use.
2. **Wrong-kind comparison.** Objects outside the declared kind are scored as if they were weak objects under improvement instead of being marked not applicable.
3. **One-score collapse.** Several independent characteristics are averaged into one score, hiding hard blockers and trade-offs.
4. **Unstated polarity.** Readers cannot tell which direction is preferred or when a value has no preferred direction.
5. **No floor or exceptional meaning.** Values are recorded, but nobody can say what is viable, exceptional, or still inadmissible for the declared use.
6. **No evidence or missingness rule.** A coordinate value is asserted without saying what observation, content locus, test, example, source, or judgment can justify it, or what absence means.
7. **No protected trade-off.** The evaluation encourages improvement on visible coordinates while damaging safety, usability, affordability, source preservation, entry cost, neighbour fit, or another value that should constrain the change.
8. **No stop or reopen condition.** Improvement continues forever or stops after a convenient checklist closure, not because the evaluation says the evaluated object has reached the declared aim.
9. **Specification underdeclaration.** A new evaluation is mentioned in prose, table, rule, or local rubric, but its declared specification does not make evaluated object kind, coordinate set, value meanings, status meanings, relations, and non-use boundaries recoverable.

### A.19.ECS:3 - Forces

| Force | Tension |
|---|---|
| **evaluated-object-kind discrimination vs broad reuse** | The evaluation must fit the evaluated object kind, but it should reuse existing FPF characteristic and scale discipline where possible. |
| **Small first version vs enough coordinates** | A useful first evaluation can be compact, but it needs enough coordinates to block false improvement and wrong-kind comparison. |
| **Measurement legality vs ordinal judgment** | Some coordinates are measured through `C.16`; others are evidence-backed ordinal content readings. The evaluation must say which is which. |
| **Improvement direction vs trade-off protection** | Preferred movement must be visible without turning every coordinate into an optimization command. |
| **Contrast cases vs overfitting** | Contrast cases are needed to test the scale set, but the evaluation must not become a list of examples only. |
| **Reusable specification vs local use** | A reusable evaluation must make the same intensional objects recoverable across uses. A local project can use a smaller specification when the use is bounded and non-reusable. |
| **Local stop vs open-ended improvement** | A loop may stop for the declared use while the object and the scale set remain improvable under new use, source, or comparison pressure. |

### A.19.ECS:4 - Solution

Construct an evaluation `CharacteristicSpace` by declaring the evaluated object kind, use scope, contrast cases, characteristic slots, scale bindings, value meanings, evidence rules, protected trade-offs, status meanings, and stop or reopen conditions.

`EvaluationCharacteristicSpaceSpec := <EvaluatedObjectKindRef, ObjectVersionUnderImprovementRef?, DeclaredUseScope, WorkingReaderScope, QualificationWindow, DiscriminatingCaseSet, ApplicabilityRule, CharacteristicSlotSet, ScaleBindingSet, PolarityAndPreferredMovement, FloorAndExceptionalMeaningSet, EvidenceAndMissingnessRule, ProtectedTradeoffSet, DominanceOrComparisonRule?, StatusValueSet, StopOrReopenCondition, NeighborPatternExitSet, E22QuestionFrameUse?, E23StartCondition>`

#### A.19.ECS:4.1 - Local names and kind settlement

| Local name | Role | Non-use boundary |
|---|---|---|
| `EvaluationCharacteristicSpaceSpec` | Local specification for constructing one evaluation `CharacteristicSpace`. | Not a score sheet, review packet, work plan, gate, evidence record, or project approval. |
| `EvaluatedObjectKindRef` | Exact kind of object the evaluation reads. | Not a vague artifact, file bundle, campaign, chat, or source collection. |
| `DeclaredUseScope` | Use for which the evaluated object is being judged or improved. | Not all possible uses. |
| `DiscriminatingCaseSet` | Positive, below-floor, and not-applicable cases used to test whether the characteristic space distinguishes the evaluated object kind and use. | Not a substitute for the coordinate set. |
| `ApplicabilityRule` | Rule for admissible evaluated object, below-floor evaluated object, and not-applicable object. | Not a low score by default for every different object kind. |
| `CharacteristicSlotSet` | The grouped slots, each binding one characteristic to one scale. | Not an arbitrary checklist and not hidden aggregation. |
| `ScaleBindingSet` | The chosen scale and value meaning for each characteristic slot. | Not a metric dashboard unless a distance or measurement claim is explicitly declared by the neighbour. |
| `PolarityAndPreferredMovement` | Direction of preferred movement for each coordinate, or a statement that the coordinate has no simple preferred direction. | Not permission to optimize one coordinate while damaging protected trade-offs. |
| `FloorAndExceptionalMeaningSet` | Viable-for-use and exceptional-for-use value meanings for active coordinates. | Not a maturity ladder and not proof that future improvement is impossible. |
| `EvidenceAndMissingnessRule` | What justifies a value and how missing, censored, unknown, or not-applicable values are handled. | Not project evidence, assurance, or gate proof by itself. |
| `ProtectedTradeoffSet` | Qualities or neighbour claims that must be checked when visible coordinates improve. | Not a hidden veto without a declared evaluation pattern or value meaning. |
| `StatusValueSet` | Local admissible-use result values for the evaluation. | Not release state, gate status, or reviewer praise. |
| `E23StartCondition` | Minimum condition for using this evaluation inside `E.23`. | Not the improvement loop itself. |

These names are local to this pattern. They do not mint kernel `U.*` kinds, measurement templates, gate states, evidence kinds, or release states.

#### A.19.ECS:4.2 - Construction moves

Use these moves when constructing or repairing an evaluation. They are not a mandatory work sequence; each move is a required content question whose answer must be recoverable before the evaluation is used for improvement.

1. **Name the evaluated object kind and use.** Say what object kind is being read and for which declared use. If the evaluated object kind is not recoverable, stop before choosing coordinates.
2. **Build the discriminating cases.** Include at least one evaluated object that should pass, one object of the same general family that should fail the floor, and one different object kind that should be not applicable rather than scored.
3. **Choose candidate characteristics.** Draw candidates from the object kind's real failure modes, first-principles structure, user or operator harms, domain tradition, current `SoTA`, existing evaluations, and exact FPF neighbours.
4. **Bind each slot.** For each candidate, state the characteristic, chosen scale, value set, admissible domain, missingness semantics, and whether the value is a measurement claim or an ordinal content reading.
5. **Remove false coordinates.** Drop coordinates that do not change admissible action, do not discriminate the evaluated object, duplicate another coordinate without a different repair move, or belong to another exact evaluation.
6. **Split compound coordinates.** If a coordinate mixes two repair moves, two object kinds, or two incompatible scales, split it or assign one part to the exact neighbouring pattern that governs it.
7. **State preferred movement and trade-offs.** For each active coordinate, state the preferred direction or explain why no simple direction exists. Name the protected trade-offs that must be checked when the coordinate improves.
8. **Define floor, exceptional, status, and stop.** State the viable-for-use floor, exceptional-for-use meaning, status values, and local stop or reopen condition.
9. **Record neighbour exits.** Name the exact FPF pattern that governs evidence, assurance, gate, work, decision, publication, naming, quality-bundle, measurement, OEE/NQD, or mathematical-lens claims when those become live.
10. **Start `E.23` only after evaluation values exist.** A repeated improvement loop can start only when the evaluated object version and evaluation are recoverable enough for re-read.

#### A.19.ECS:4.3 - Evaluation specification minimum

A.19.ECS does not prescribe a publication or record form. It states which intensional objects must be recoverable before an evaluation characteristic space is reusable for judgement or improvement. The selected publication or record form may be an FPF pattern, local engineering standard, rubric, table, review form, model card section, protocol note, or project rule, but that form is not governed here. The evaluation characteristic-space specification must make these items recoverable by value:

| Specification item | Required content |
|---|---|
| `Evaluation problem frame` | Evaluated object kind, declared use, first useful move, cheap stop, and what goes wrong if no evaluation exists. |
| `Non-use boundary` | Boundaries to single-characteristic, measurement, Q-Bundle, naming, evidence, assurance, gate, work, decision, publication, and loop-method patterns. |
| `Local names and kind settlement` | Local field names, exact roles, and non-use boundaries. |
| `Evaluation record shape` | The local record or bundle shape used by the evaluation. |
| `Eligibility set` | Hard filters checked before coordinates are read. |
| `Coordinate set` | Coordinate heads, properties of the evaluated object, activation conditions, scale/value meanings, evidence loci, and protected trade-offs. |
| `Status and stop condition` | Admissible-use statuses, local stop meanings, and reopen conditions. |
| `Worked slices` | At least one passing evaluated object, one below-floor evaluated object, and one not-applicable object. |
| `Common anti-patterns` | The false readings the evaluation must block. |
| `Neighbouring-pattern claim assignment` | Exact neighbouring FPF patterns and the live claims each neighbour governs. |

This minimum is a content requirement, not a file-format requirement. For an FPF pattern publication form, `E.8` still governs the authoring form. `A.19.ECS` only states what the evaluation must make recoverable so that `E.22` can frame an improvement-oriented quality read and `E.23` can run a repeated improvement loop.

#### A.19.ECS:4.4 - Discriminating-case test

An evaluation is not ready if it cannot distinguish these three outcomes:

1. **Admissible evaluated object.** The object is of the evaluated object kind and can meet or exceed the floor under the declared use.
2. **Below-floor evaluated object.** The object is of the evaluated object kind or a declared comparable family, but fails one or more floors.
3. **Not-applicable object.** The object is not of the evaluated object kind for this use and should not receive coordinate values except an explicit not-applicable status.

Example: for a nuclear-plant adequacy evaluation, a nuclear plant can vary along safety, output, maintenance, regulatory, thermal, waste-handling, grid, and resilience coordinates. A coal plant may be a power-generation alternative, but it is not a nuclear plant unless the declared use explicitly compares power-generation options across plant kinds. A chair or FPF pattern is not applicable as a nuclear plant; scoring it as "low nuclear plant quality" would show that the applicability rule is wrong.

#### A.19.ECS:4.5 - Scale-set improvement

The evaluation characteristic space itself can be improved. In that case, the evaluated object is the current `EvaluationCharacteristicSpaceSpec` version, not the original evaluated object.

Use `E.23` for the repeated improvement method over the scale set when the improvement aim is live. The evaluation for that meta-level improvement may be:

- this pattern's conformance checklist for whether the scale set is constructible and usable;
- `E.21` when the evaluation characteristic-space specification is itself an FPF pattern version;
- `E.9.DA` when the decision record selecting the scale set is the `DRR` decision-adequacy object being evaluated;
- `E.2.DA` when the scale set changes FPF-level Pillar adequacy;
- `F.18` when the live problem is name choice for the scale-set heads;
- `C.16`, `A.17`, `A.18`, or `A.19` when the live problem is measurement or characteristic-space legality.

Do not improve an evaluated object by silently changing its evaluation. If the evaluation changes, the loop record names the changed evaluation version and states whether earlier object-version readings remain comparable, need a bridge, or must be retired for the new use.

### A.19.ECS:5 - Worked slices

**Show, FPF pattern quality.** The evaluated object kind is one FPF pattern version. The existing evaluation is `E.21`, so `A.19.ECS` stays closed unless `E.21` itself is being redesigned. `E.23` may improve the pattern version under `E.21`.

**Show, DRR adequacy.** The evaluated object kind is one `DRR` version for a declared campaign-decision use. The existing evaluation is `E.9.DA`. If a campaign needs a different DRR adequacy coordinate, `A.19.ECS` can test whether that coordinate belongs inside `E.9.DA`, another evaluation, or no current FPF pattern.

**Show, FPF Pillar adequacy.** The evaluated object is FPF as a corpus or release candidate. `E.2` gives the Pillars; `E.2.DA` is the evaluation. `A.19.ECS` explains why `E.2.DA` needs evaluated object, use, eligibility, coordinates, evidence loci, stop meanings, and neighbour exits rather than a Pillar essay.

**Show, name improvement.** The evaluated object is a durable term candidate. `F.18` already supplies a grouped lexical quality vector: `SemanticFidelity`, `CognitiveErgonomics`, `MorphologicalActionFit`, and `AliasRisk`, plus NQD discipline over candidate names. `A.19.ECS` treats `F.18` as an existing local evaluation for naming, not as a reason to build another one.

**Show, no evaluation yet.** A team says "make this onboarding method better" but cannot say better for whom, by what values, or with what stop. `A.19.ECS` opens before `E.23`: it names evaluated object kind, user, use, contrast cases, candidate characteristics, scales, floors, missingness, protected trade-offs, and neighbour exits. Only then can `E.22` frame an improvement-oriented quality read and `E.23` improve the method.

### A.19.ECS:6 - Conformance checklist

| Check | Requirement | Why |
|---|---|---|
| `CC-A19ECS-1` | An evaluation characteristic-space specification SHALL name evaluated object kind, use scope, reader scope, and qualification window. | Prevents context-free quality claims. |
| `CC-A19ECS-2` | It SHALL include admissible, below-floor, and not-applicable contrast cases. | Tests evaluated-object-kind discrimination. |
| `CC-A19ECS-3` | Each coordinate SHALL bind one characteristic to one scale or state why it is an ordinal content reading rather than a measurement claim. | Preserves A.17/A.18/C.16/A.19 discipline. |
| `CC-A19ECS-4` | Each coordinate SHALL state value meanings, polarity or no-simple-direction posture, evidence rule, and missingness rule. | Makes readings replayable. |
| `CC-A19ECS-5` | The specification SHALL state floor, exceptional, status, stop, and reopen meanings for the declared use. | Lets improvement stop locally without claiming final perfection. |
| `CC-A19ECS-6` | Protected trade-offs SHALL be named when improving visible coordinates can harm another live value. | Blocks Goodhart-style improvement. |
| `CC-A19ECS-7` | The specification SHALL not average ordinal coordinates or turn inactive coordinates into hidden pass, waiver, or failure. | Preserves non-scalar comparison. |
| `CC-A19ECS-8` | Wrong-kind objects SHALL be marked not applicable unless the declared use explicitly compares across those object kinds. | Prevents false low scores. |
| `CC-A19ECS-9` | If made reusable beyond one local use, the evaluation characteristic-space specification SHALL make the minimum items in `A.19.ECS:4.3` recoverable by value. If the selected publication form is an FPF pattern, `E.8` also applies to that publication form. | Prevents underspecified evaluations. |
| `CC-A19ECS-10` | If the evaluation itself changes during improvement, the loop record SHALL name the changed evaluation version and the comparability effect on earlier object-version readings. | Prevents silent value drift. |
| `CC-A19ECS-11` | The evaluation characteristic-space specification SHALL assign evidence, assurance, gate, work, decision, publication, naming, measurement, Q-Bundle, OEE/NQD, and mathematical-lens claims to exact neighbouring patterns when those claims are live. | Prevents an evaluation from becoming a second ontology. |
| `CC-A19ECS-12` | A reusable evaluation characteristic-space specification SHALL state what would lower, reopen, or retire the evaluation: missing contrast case, changed use, changed source posture, hidden trade-off loss, or corrected neighbouring-pattern claim assignment. | Makes high-value evaluation claims falsifiable instead of permanent praise. |

### A.19.ECS:7 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
|---|---|---|
| **Scale set from air.** | Coordinates appear because they are familiar. | Rebuild from evaluated object kind, use, contrast cases, failure modes, domain tradition, first principles, and current source posture. |
| **Everything gets a low score.** | Objects outside the declared kind are scored instead of marked not applicable. | Add an applicability rule and not-applicable cases. |
| **Checklist masquerading as characteristic space.** | A list of tasks is treated as coordinates. | Convert each live item to an evaluated object property with a characteristic, scale, value meaning, and evidence rule, or move it to work planning. |
| **One total quality score.** | Several ordinal readings are averaged. | Use coordinates, statuses, dominance or comparison rule, and protected trade-offs; do not scalarize unless an exact neighbouring pattern explicitly declares the operation. |
| **Improvement without floor.** | A loop continues because more change is possible. | State floor, exceptional meaning, stop condition, and reopen condition. |
| **Hidden value drift.** | The evaluation changes while old readings are compared as if nothing changed. | Version the evaluation and state comparability, bridge, or retirement. |
| **Evaluation theft.** | The new evaluation starts governing evidence, assurance, gate, work, decision, or publication truth. | Return each claim to the exact neighbouring pattern and leave only the value read here. |

### A.19.ECS:8 - Relations

| Pattern | Relation |
|---|---|
| `A.19` | Defines `CharacteristicSpace`. `A.19.ECS` gives the method for constructing one evaluation `CharacteristicSpace` for an evaluated object. |
| `A.17`, `A.18`, `C.16` | Govern characteristics, scales, scale values, coordinates, measures, units, and measurement legality. `A.19.ECS` uses them by reference for each slot. |
| `C.25` | Governs Q-Bundle normal form for composite engineering quality families. `A.19.ECS` may select or repair the characteristic-space part before a Q-Bundle endpoint is used. |
| `E.22` | Frames one improvement-oriented quality-read question after an evaluation is declared. `A.19.ECS` constructs the missing or inadequate evaluation. |
| `E.23` | Governs repeated improvement after evaluated object version and evaluation are declared. `A.19.ECS` provides the evaluation when it is missing or underdesigned. |
| `E.21` | Existing evaluation for one FPF pattern version. `A.19.ECS` explains the construction shape but does not replace `E.21`. |
| `E.9.DA` | Existing evaluation for one `DRR` decision-adequacy claim. `A.19.ECS` does not replace it. |
| `E.2.DA` | Existing evaluation for FPF-level Pillar adequacy. `A.19.ECS` explains why it must publish evaluated object, coordinates, values, evidence loci, status, and stop meanings. |
| `F.18` | Existing naming discipline with a grouped lexical quality vector. Use `F.18` for durable term and name improvement. |
| `C.16.P`, `C.16.Q`, `E.10`, `A.6.P`, `C.2.P` | Repair overloaded characteristic/scale/score, quality, lexical, relation, and source-transfer wording before it becomes a coordinate or status value. |
| `C.18`, `C.19`, `G.5`, `G.9`, `G.11` | Govern OEE/NQD novelty, diversity, archive, pool, selected-set, parity, and refresh semantics. An evaluation may supply `Q` readings, but it does not govern the rest of OEE/NQD. |
| `C.29` | Governs mathematical lens adequacy when a mathematical structure is used to define or justify coordinates. |
| `A.10`, `B.3`, `A.20`, `A.21`, `A.15` | Govern evidence, assurance, local CV, gates, and work when an evaluation result is reused for those claims. |

### A.19.ECS:9 - Consequences

A conforming `A.19.ECS` result lets `E.22` ask a useful improvement-oriented quality-read question and lets `E.23` run a repeated improvement loop without inventing values during the loop. It also gives object-specific evaluation patterns such as `E.21`, `E.9.DA`, `E.2.DA`, and `F.18` a common construction shape: evaluated object kind, use, contrast cases, coordinates, value meanings, evidence and missingness rules, protected trade-offs, status meanings, and local stop or reopen condition.

The cost is intentional. A reusable evaluation is heavier than a local checklist, because it must prevent wrong-kind use, hidden value drift, proxy-for-value substitution, neighbour theft, and false stop claims. When a local rubric is enough, keep the rubric local. When reuse is needed, carry the evaluation by value.

### A.19.ECS:10 - SoTA-Echoing

| Claim | Current practice line | Adoption in A.19.ECS | Boundary |
|---|---|---|---|
| Evaluation artifacts must declare intended use, object, criteria, and missingness before their readings are useful. | Current reporting anchors: BenchmarkCards/EvalCards practice for evaluation-card structure, model-card lineage for intended-use and performance-characteristic reporting, and HELM/VHELM/AHELM-style evaluation suites for scenario, metric, raw-result, and modality-extension transparency. | `A.19.ECS` starts from evaluated object kind, use scope, contrast cases, coordinate meanings, evidence rule, and missingness rule. | It is not a benchmark harness, automated judge, or publication format by itself. |
| Multicriteria evaluation needs preserved dimensions and protected trade-offs. | Current QD overview: `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, Swarm and Evolutionary Computation 100:102240 (2026); retained design lineage: MCDA and value-focused thinking for criterion separation and trade-off visibility. | The pattern requires coordinate values, polarity or no-simple-direction posture, protected trade-offs, status meanings, and stop or reopen conditions. | Scalarization belongs only to an exact neighbouring pattern or explicitly declared local method. |
| Improvement pressure can damage the intended value when the evaluation is a weak proxy. | Current proxy-risk anchors: `Goodhart's Law in Reinforcement Learning` (ICLR 2024) and current catastrophic-Goodhart reward-misspecification work (NeurIPS 2024); retained lineage: Goodhart taxonomy. | `A.19.ECS` requires evidence rules, missingness rules, protected trade-offs, and lowering/reopen conditions before a loop can treat a value as improved. | It is not an anti-measurement rule; it makes the measurement or ordinal read explicit enough to be challenged. |
| OEE/NQD separates the quality side from novelty, diversity, archive, pool, and selected-set semantics. | Current QD and OEE/NQD neighbour posture: QD uses quality pressure with novelty/diversity and archive/front practice, while current FPF `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` keep the exact archive, pool, selected-set, parity, and refresh semantics. | The evaluation may supply `Q` readings, while novelty, diversity, archive, front, pool, selected-set publication, parity, and refresh remain with exact neighbouring patterns. | `A.19.ECS` does not govern OEE/NQD generation, selection, archive, parity, or refresh. |
### A.19.ECS:11 - Rationale

Improvement cannot be better than its evaluation. A loop that changes an object version without a declared characteristic space can only produce activity, persuasion, or reviewer preference. An evaluation that lists scales without evaluated-object-kind discrimination, floor, evidence, missingness, trade-offs, and stop meanings cannot guide improvement safely.

Placing this method under `A.19` keeps the ontology clean. `A.19` governs the structure of `CharacteristicSpace`; `A.19.ECS` governs the construction method for evaluations of declared object kinds and uses. `A.19.ECS` governs the intensional content of the evaluation characteristic space, not its publication or record form. An FPF pattern is only one possible publication form when the evaluation belongs in FPF; a local rubric, standard, table, or project rule is enough when the use is local. `E.23` stays a universal loop method because it does not need to know how every domain chooses its scales. Domain and FPF-specific evaluations such as `E.21`, `E.9.DA`, `E.2.DA`, and `F.18` keep coordinate choices inside those evaluations.

### A.19.ECS:End

