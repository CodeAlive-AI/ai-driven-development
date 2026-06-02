## E.8.ECSPF - Evaluation CharacteristicSpace FPF Pattern Publication Form

> **Type:** Authoring method pattern
> **Status:** Stable
> **Normativity:** Normative

### E.8.ECSPF:1 - Problem frame

Use `E.8.ECSPF` when an evaluation `CharacteristicSpace` constructed or repaired under `A.19.ECS` must be published as an FPF pattern. The live question is not "what values should this evaluated object be judged by?" but "how do we write the FPF pattern publication form so those values remain usable, reviewable, and bounded?"

`A.19.ECS` governs the intensional object: evaluated object kind, use scope, contrast cases, coordinate set, value meanings, missingness, protected trade-offs, status meanings, and stop or reopen conditions. `E.8` governs ordinary FPF authoring form. `E.8.ECSPF` governs their intersection: an FPF pattern whose main payload is a reusable evaluation.

**Not this pattern when.** Use `A.19.ECS` when the characteristic-space specification itself is missing or inadequate. Use `E.8` when the pattern is not an evaluation-characteristic-space pattern. Use `E.21`, `E.9.DA`, `E.2.DA`, `F.18`, `C.25`, or a project-local evaluation when one already supplies the value meanings for the evaluated object and use. Use `E.22` to frame one quality read and `E.23` to run repeated improvement. Use a local rubric, table, or project rule instead of an FPF pattern when the evaluation is not intended for durable FPF reuse.

**First useful move.** Start from the accepted `A.19.ECS` specification. Name the evaluated object kind, declared use, and first action-guiding evaluation use in the pattern's recognition text before presenting coordinate tables or conformance rows.

**Cheap stop.** If the evaluation is local, temporary, or project-specific, do not publish an FPF pattern. Keep the `A.19.ECS` specification in the local publication form and cite the exact FPF neighbours it uses.

**What goes wrong if missed.** An evaluation-characteristic-space pattern becomes a score sheet, review form, checklist, or taxonomy. The coordinate table appears before the working situation. Readers can see values but cannot tell when to use them, what to do after an evaluation result, which objects are not applicable, or which neighbouring pattern governs evidence, assurance, gate, work, decision, naming, measurement, or improvement-loop claims.

**What this buys.** `E.8.ECSPF` lets FPF publish evaluations as real patterns: practitioner-readable first, exact enough for review, and bounded enough that `E.22` and `E.23` can consume them without stealing their values.

**Governed object in plain terms.** The governed object is the authored FPF pattern publication form for one evaluation `CharacteristicSpace`.

**Primary working reader.** The first reader is an FPF author or reviewer turning an accepted evaluation characteristic-space specification into a reusable FPF pattern for later practitioners, managers, and stewards.

### E.8.ECSPF:2 - Problem

`A.19.ECS` can produce a good evaluation characteristic-space specification without saying how to publish that specification as an FPF pattern. `E.8` can produce a good generic FPF pattern without saying how a coordinate set, eligibility rule, status set, and stop condition should be placed when they are the pattern's main payload.

Recurring failures:

1. **Publication-form/content collapse.** The FPF pattern is treated as the evaluation itself, instead of a publication form for an intensional object specification.
2. **Table-first pattern.** Coordinate rows arrive before evaluated object kind, use, first move, cheap stop, and not-applicable boundary.
3. **Checklist substitution.** Conformance rows replace the `Solution` instead of checking a readable evaluation method.
4. **Underpublished values.** Coordinate names are present, but value meanings, missingness, polarity, protected trade-offs, status meanings, or stop conditions are missing.
5. **Wrong-kind examples.** Worked cases show only passing examples, so the pattern cannot teach below-floor and not-applicable outcomes.
6. **Neighbour theft.** Evidence, assurance, gate, work, decision, naming, measurement, OEE/NQD, or mathematical-lens claims are carried as if the evaluation-characteristic-space pattern governed them.
7. **Pattern-quality confusion.** The author uses `E.21` to judge whether the FPF pattern version is good, but forgets that the new pattern must still publish the evaluation for one evaluated object kind by value.

### E.8.ECSPF:3 - Forces

| Force | Tension |
|---|---|
| **Recognition first vs coordinate completeness** | An evaluation-characteristic-space pattern needs tables, but the reader must first see the working situation and first evaluation use. |
| **Generic E.8 form vs ECS payload** | The canonical pattern skeleton stays fixed, but the payload has special fields from `A.19.ECS`. |
| **Reusable FPF pattern vs local evaluation** | FPF publication is useful only when the evaluation is durable and reusable beyond one local project. |
| **Exact values vs checklist feel** | Values and statuses must be exact without making the pattern feel like an administrative form. |
| **Neighbour exits vs second ontology** | The pattern must keep outside claims with exact neighbours without becoming a directory of every adjacent pattern. |
| **Evaluation of object vs evaluation of FPF pattern version** | The evaluation judges its evaluated object; `E.21` may separately evaluate whether the authored FPF pattern publication form is good enough. |

### E.8.ECSPF:4 - Solution

When an `A.19.ECS` specification is selected for durable FPF publication, author the evaluation as an `E.8` pattern with these additional placement rules:

1. **Keep the intensional object separate from the publication form.** The pattern publishes an evaluation `CharacteristicSpace`; it is not itself the evaluated object, the evaluation result, the improvement loop, or the evidence record.
2. **Put recognition before coordinates.** The opening text names evaluated object kind, declared use, first evaluation use, cheap stop, what goes wrong, and what the pattern buys before any dense table.
3. **Place the `A.19.ECS` specification by value.** The `Solution` carries the record shape, local names, eligibility rule, coordinate set, value meanings, missingness rule, protected trade-offs, status meanings, and stop or reopen condition.
4. **Use worked slices as the discriminating-case test.** Archetypal Grounding and worked cases include a passing evaluated object, a below-floor evaluated object, and a not-applicable object.
5. **Keep checklist rows secondary.** Conformance checks verify that the evaluation is recoverable and usable. They do not become the user's method.
6. **Keep outside claims with exact neighbours.** Relations and non-use boundaries name the exact neighbour for evidence, assurance, gate, work, decision, naming, measurement, OEE/NQD, mathematical lens, `E.22` quality-read, and improvement-loop claims.
7. **Evaluate the publication form with `E.21`.** When the FPF pattern publication form is under quality improvement, `E.21` evaluates the FPF pattern version's quality. The evaluation coordinates inside the pattern continue to judge the evaluated object declared by that evaluation.

#### E.8.ECSPF:4.1 - Canonical placement table

| E.8 section | ECS-specific payload |
|---|---|
| `Problem frame` | Evaluated object kind, declared use, first useful evaluation use, cheap stop, what goes wrong without this evaluation, and what practical move the evaluation enables. |
| `Problem` | Failure modes that the evaluation prevents: wrong-kind scoring, hidden value drift, proxy value, one-score collapse, missingness confusion, or neighbour theft. |
| `Forces` | Tensions among reuse, coordinate count, readability, measurement legality, trade-off protection, local stop, and open-ended improvement. |
| `Solution` | `A.19.ECS` record shape, local names, eligibility rule, coordinate set, value meanings, evidence and missingness rules, protected trade-offs, status meanings, stop and reopen conditions. |
| `Archetypal Grounding` | At least one passing evaluated object, one below-floor evaluated object, and one not-applicable object. |
| `Bias-Annotation` | Known skew in source examples, reader family, domain tradition, measurement preference, benchmark preference, or FPF-internal reuse. |
| `Conformance Checklist` | Checks that the specification is recoverable, not that a reviewer likes the evaluated object. |
| `Common Anti-Patterns` | Score-sheet pattern, checklist-as-solution, table-first recognition failure, neighbour theft, one total score, hidden value drift. |
| `Consequences` | What a conforming evaluation use permits, what it does not permit, and which neighbours govern claims that exceed the evaluation. |
| `Rationale` | Why this coordinate set and publication-form are selected, including relation to `A.19.ECS` and exact existing evaluations. |
| `SoTA-Echoing` | Current practice that changes evaluated-object selection, coordinate choice, value meaning, missingness, comparison, or stop discipline. |
| `Relations` | `A.19.ECS`, `E.8`, `E.21`, `E.22`, `E.23`, and exact domain or neighbour patterns. |

#### E.8.ECSPF:4.2 - Local names and kind settlement

| Local name | Role | Non-use boundary |
|---|---|---|
| `EvaluationCharacteristicSpaceFPFPatternPublicationForm` | The authored FPF pattern body that publishes one evaluation `CharacteristicSpace`. | Not the evaluated object being evaluated, evaluation result, improvement loop, evidence record, or release approval. |
| `ECSPayload` | The by-value `A.19.ECS` specification inside the pattern. | Not an arbitrary table or checklist. |
| `RecognitionEvaluationUseLine` | Early line saying what object is evaluated, for which use, and what the first admissible evaluation use does. | Not a slogan or pattern-title paraphrase. |
| `DiscriminatingCaseBank` | Passing, below-floor, and not-applicable worked slices. | Not only positive examples. |
| `NeighbourExitBlock` | Exact neighbouring FPF pattern applications for claims outside the evaluation. | Not a general directory of possibly related patterns. |
| `PatternVersionQualityEvaluation` | Optional `E.21` evaluation over the authored pattern publication form. | Not a replacement for the evaluation for one evaluated object kind. |

### E.8.ECSPF:5 - Archetypal Grounding

**Tell.** An evaluation `CharacteristicSpace` becomes reusable in FPF only when a practitioner can recognize the evaluated object and use before reading the coordinate table. The publication form must teach the evaluation use, not merely list the values.

**Show, pattern-quality evaluation.** `E.21` is an evaluation for one FPF pattern version. Its publication form must still open with the working question "is this pattern good enough for the declared use?" before showing coordinates such as first-move recoverability, boundary fit, and SoTA binding.

**Show, local rubric that should not become an FPF pattern.** A project team defines a temporary rubric for choosing a meeting room. The `A.19.ECS` specification may be adequate locally, but no durable FPF pattern is needed because the evaluated object kind and use do not recur across FPF practice.

**Show, not-applicable boundary.** A nuclear-plant evaluation can judge nuclear plants and declared comparable power-generation alternatives. It should mark a chair or FPF pattern as not applicable, not as a low-quality nuclear plant. The pattern publication form must show that boundary before readers try to use the coordinate table.

### E.8.ECSPF:6 - Bias-Annotation

Evaluation-characteristic-space patterns are vulnerable to domain-example bias: the first examples can silently choose the evaluated object kind, use, and value family for later readers. A conforming publication form names known skew in examples, sources, reader family, domain tradition, measurement preference, benchmark preference, or FPF-internal reuse. When the evaluation claims broad use, the case bank must include heterogeneous evaluated object situations or explicitly narrow the claim.

### E.8.ECSPF:7 - Conformance Checklist

| Check | Requirement | Why |
|---|---|---|
| `CC-E8ECSPF-1` | The pattern publication form SHALL name the `A.19.ECS` evaluation characteristic-space specification or carry its evaluated object kind, use, eligibility, coordinate set, value meanings, missingness, trade-offs, status, and stop condition by value. | Prevents publication-form/content collapse. |
| `CC-E8ECSPF-2` | Recognition text SHALL state evaluated object kind, declared use, first evaluation use, cheap stop, and not-applicable boundary before dense coordinate tables. | Keeps the pattern usable before it becomes reviewable. |
| `CC-E8ECSPF-3` | The `Solution` SHALL carry the ECS payload rather than leaving it only in conformance rows, SoTA rows, or examples. | Prevents checklist substitution. |
| `CC-E8ECSPF-4` | Worked cases SHALL include passing, below-floor, and not-applicable outcomes. | Tests evaluated-object-kind discrimination. |
| `CC-E8ECSPF-5` | Each coordinate SHALL state value meanings, polarity or no-simple-direction posture, missingness rule, and protected trade-off when live. | Makes evaluation uses repeatable and bounded. |
| `CC-E8ECSPF-6` | Relations SHALL name exact neighbouring governing patterns for evidence, assurance, gate, work, decision, naming, measurement, OEE/NQD, mathematical-lens, `E.22` quality-read, and improvement-loop claims when those claims are live. | Prevents a second ontology. |
| `CC-E8ECSPF-7` | If the authored publication form is under improvement, `E.21` SHALL evaluate FPF pattern-version quality separately from the evaluation's evaluated object result. | Keeps pattern quality distinct from evaluated object quality. |
| `CC-E8ECSPF-8` | The pattern SHALL not publish a local, temporary, or one-project evaluation as FPF unless reuse scope and neighbouring-pattern claim assignment justify FPF publication. | Blocks needless pattern growth. |
| `CC-E8ECSPF-9` | The publication form SHALL state what would lower, reopen, or retire the published evaluation: changed object kind, changed use, changed source posture, missing contrast case, coordinate-value drift, missingness-rule change, or corrected neighbouring-pattern claim assignment. | Makes maintenance of the evaluation pattern testable. |

### E.8.ECSPF:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| **Score-sheet pattern.** | The pattern is mostly a table of values. | Move evaluated object kind, use, first evaluation use, cheap stop, and practical consequence into recognition text before the table. |
| **Checklist-as-solution.** | Users are told only what must be checked. | Put the actual evaluation method and record shape in `Solution`; let checklist rows verify it. |
| **Publication-form/content collapse.** | The FPF pattern is treated as the evaluated object being evaluated or evaluation result. | State that the pattern is a publication form for the `CharacteristicSpace`; the evaluated object and evaluation result are separate. |
| **Positive-only case bank.** | Every example passes. | Add below-floor and not-applicable cases. |
| **Neighbour theft.** | The pattern claims evidence, assurance, gate, release, measurement, naming, or improvement authority. | Return each claim to the exact neighbouring pattern and keep only the evaluation claim here. |
| **Rubric promotion.** | A local rubric becomes an FPF pattern because it was useful once. | Keep it local unless durable FPF reuse, evaluated object scope, and neighbouring-pattern claim assignment are declared. |
| **Frozen evaluation publication form.** | The evaluated object kind, use, source posture, or coordinate meanings change, but the pattern keeps the old values as if still current. | Reopen `A.19.ECS` for the evaluation object and state whether earlier evaluation results remain comparable, need a bridge, or must be retired. |

### E.8.ECSPF:9 - Consequences

A conforming `E.8.ECSPF` publication form makes an evaluation findable, teachable, and reusable inside FPF. It lets `E.22` frame quality reads and `E.23` run improvement loops without re-inventing values. It also makes the cost visible: a reusable evaluation-characteristic-space pattern must publish more than a local rubric, because it must prevent wrong-kind use, hidden value drift, neighbour theft, and proxy-for-value substitution.

The pattern publication form does not certify the evaluated object, approve a release, prove evidence, or finish improvement. It only publishes a bounded evaluation.

### E.8.ECSPF:10 - Rationale

The split between `A.19.ECS` and `E.8.ECSPF` preserves the FPF distinction between intensional object and publication form. `A.19.ECS` says what must exist for an evaluation to be adequate. `E.8.ECSPF` says how that adequate evaluation is authored as an FPF pattern when FPF publication is selected. This prevents two symmetric mistakes: stuffing FPF pattern-format requirements into a general characteristic-space construction method, and publishing an evaluation-characteristic-space pattern whose coordinate set is not recoverable by value.

### E.8.ECSPF:11 - SoTA-Echoing

**Source posture convention.** This section uses source rows only where they change the publication form: evaluated object and use before checklist, coordinate meanings and missingness, worked cases, non-scalar comparison, protected trade-offs, or action-guiding recognition text. Reporting frameworks and standards are reference support unless they solve the exact publication-form problem.

| Claim | Current practice line | Source posture and representative anchors | Adoption in E.8.ECSPF | Boundary |
|---|---|---|---|---|
| Evaluation rubrics are useful only when criteria, value meanings, and use context are explicit. | Current reporting practice makes evaluation cards, scenario descriptions, metric meanings, raw-result visibility, intended use, and performance-characteristic reporting explicit. | **Current practice and reference support.** BenchmarkCards and EvalCards are current evaluation-card reporting anchors; HELM, VHELM, and AHELM are current suite-reporting anchors for scenarios, metrics, inference settings, prompts, raw outputs, and comparable reporting; model cards are retained lineage for intended-use and performance-characteristic reporting. | The publication form must publish evaluated object kind, use, coordinate meanings, missingness, and worked cases before checklist closure. | `E.8.ECSPF` is not a benchmark harness, model-card schema, automated evaluator, or reporting standard. |
| Multicriteria evaluation needs non-scalar comparison and trade-off visibility. | Current QD and multicriteria practice keeps dimensions, dominance, trade-offs, objective heads, and diversity or descriptor choices visible when one total score would hide important loss. | **Current-best support for QD overview in this narrow use, plus retained lineage.** `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, *Swarm and Evolutionary Computation* 100:102240 (2026), supplies the current QD overview used here. MCDA and older QD practice are retained lineage for dimensions, dominance, and trade-offs. | The publication form keeps coordinate values, protected trade-offs, and status meanings distinct. | Scalarization belongs only to an exact neighbouring pattern or explicitly declared local method. |
| Pattern publication must remain action-guiding. | Pattern-language practice treats a pattern as reusable action guidance for recurring situations, not as a static rubric table. | **Lineage and current FPF reference support.** Pattern-language practice is retained as lineage and problem pressure; current FPF `E.8` supplies the governing publication-form rules for recognition text, first useful move, worked cases, and relations. | The publication form keeps recognition text and first evaluation use before coordinate tables. | `E.8.ECSPF` does not replace `E.8`; it specializes it for evaluation-characteristic-space patterns. |

### E.8.ECSPF:12 - Relations

| Pattern | Relation |
|---|---|
| `E.8` | Governs the canonical FPF authoring form. `E.8.ECSPF` specializes that form for evaluation `CharacteristicSpace` pattern publication forms. |
| `A.19.ECS` | Constructs or repairs the evaluation `CharacteristicSpace`. `E.8.ECSPF` authors the FPF pattern publication form for the selected specification when FPF reuse is selected. |
| `A.19`, `A.17`, `A.18`, `C.16` | Govern `CharacteristicSpace`, characteristic, scale, coordinate, and measurement legality. |
| `E.21` | Evaluates quality of the authored FPF pattern publication form. It does not replace the evaluation for one evaluated object kind. |
| `E.22` | Frames one quality read using the evaluation published by the publication form. |
| `E.23` | Runs repeated improvement using the evaluation published by the publication form. |
| `E.9.DA`, `E.2.DA`, `F.18`, `C.25` | Existing or candidate evaluations that may use this authoring specialization when their publication-form is being written or refreshed. |
| `A.10`, `B.3`, `A.20`, `A.21`, `A.15` | Govern evidence, assurance, gate, decision, and work claims when an evaluation result is reused for those purposes. |
| `C.18`, `C.19`, `G.5`, `G.9`, `G.11` | Govern OEE/NQD archive, novelty, diversity, pool, selected-set, parity, and refresh claims. |
| `C.29` | Governs mathematical-lens adequacy when a mathematical structure defines or justifies coordinate choice. |

### E.8.ECSPF:End

