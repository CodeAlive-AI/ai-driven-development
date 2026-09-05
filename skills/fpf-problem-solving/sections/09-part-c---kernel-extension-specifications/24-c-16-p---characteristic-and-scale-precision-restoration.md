## C.16.P - Characteristic and Scale Precision Restoration

> **Type:** Characterization precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Characteristic-scale wording repair.

**Intent.**
Recover characteristic, scale, coordinate, score, metric, indicator, threshold, comparison, and scalar-quality wording whose construction is hidden before a reader applies `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.29`, `E.21`, or another subject pattern.

Repair overloaded characterization wording so the exact `Characteristic`, `Scale`, `Coordinate`, `Value`, `Score`, `Unit`, `ScoringMethod`, indicated characteristic or claim, direct indicator or proxy relation, comparison reference or comparator set, admissible use, and subject pattern become recoverable.

**Builds on.** `E.10`, `E.10.ARCH`, `A.17`, `A.18`, `C.16`, `A.19`, `C.25`, `C.29`, `E.21`, `F.18`, and `A.6.P`.

**Coordinates with.** `C.16.Q`, `A.19.ECS`, CHR mechanism patterns, `G.0`, `G.5`, `G.9`, `C.11`, `A.10`, `B.3`, `A.20`, `A.21`, `C.28`, `A.15`, and the evidence, assurance, gate, decision, causal-use, release, work, benchmark, and publication patterns that define or constrain those claims.

**E.10.ARCH relation-function boundary.** When `E.10` encounters `metric`, `score`, `axis`, `dimension`, `feature`, `property`, `indicator`, `strong`, `weak`, `robust`, `level`, `coordinate`, `threshold`, `benchmark`, or scalar-quality wording whose characteristic and scale construction is hidden, `E.10.ARCH` selects `C.16.P` only until bearer, characteristic, scale, value or score construction, comparison reference or comparator set, threshold rule or reference, proxy relation, admissible use, and subject-pattern locator are recovered. After that recovery, state the subject assertion under its exact invariant or predicate.

### C.16.P:0 - Use this when

Use this pattern when wording such as `axis`, `dimension`, `feature`, `property`, `metric`, `indicator`, `score`, `strong`, `weak`, `robust`, `level`, `coordinate`, `threshold`, `rating`, `benchmark`, `quality coordinate`, or `architecture score` carries a characterization claim but does not yet show the recoverable construction.

**What goes wrong if missed.** A metric becomes a measure without a scale, a score becomes proof, `strong` becomes a verdict without a characteristic, a level becomes an undefined maturity status, an indicator becomes the thing indicated, or a benchmark result becomes gate passage or release permission.

**What this buys.** The reader can recover the bearer, characteristic, scale, value, score, unit, scoring method, indicated characteristic or claim, exact direct indicator or proxy relation, comparison reference or comparator set, threshold, admissible use, and subject pattern before treating a number, adjective, coordinate, or comparison as actionable.

**First useful move.** Ask which bearer, characteristic, scale, value or score construction is recoverable; then apply `C.16`, `A.19`, `C.25`, `C.29`, `E.21`, or the neighboring pattern governing that claim instead of letting the compact word decide.

**Not this pattern when.**

- If the `Characteristic`, `Scale`, value set, scoring method, and admissible use are already recoverable, use `C.16`, `A.17`, `A.18`, or `A.19` directly.
- If the claim being made is a Q-bundle, quality-term or evaluative characterization, or pattern-quality coordinate, use `C.25`, `C.16.Q`, or `E.21` directly after any needed characteristic-scale repair.
- If the claim being made is mathematical-lens use, use `C.29`.
- If the claim being made is evidence, assurance, gate, work, decision, causal-use, release, benchmark harness, or project-side authority claim, use the subject pattern for that claim after characteristic and scale construction is recovered or blocked.

### C.16.P:1 - Problem frame

Working texts often need compact characterization words. The problem starts when compact words begin to carry comparison, proof, selection, gate, readiness, release, quality, or decision claim without recoverable characteristic and scale construction.

The repair question is:

> What characteristic or scale construction is recoverable, what exact assertion states the remaining claim, and where is its defining or constraining `ClaimGraph` located?

The recoverable item may be:

- a `Characteristic` under `A.17`;
- a `Scale`, coordinate, value, unit, scoring method, measure, or measurement use under `A.18` and `C.16`;
- a `CharacteristicSpace` under `A.19`;
- a Q-bundle under `C.25`;
- quality-term or evaluative characterization under `C.16.Q`;
- pattern-quality coordinate use under `E.21`;
- mathematical-lens use under `C.29`;
- a comparison, threshold, indicator, proxy, benchmark, gate, evidence, decision, or work claim under a neighboring pattern that defines or constrains it;
- ordinary prose with no FPF-governed use.

### C.16.P:2 - Problem

How can FPF repair characterization wording without:

- treating `metric` as a universal measurement kind;
- treating `score` as proof, readiness, gate passage, release permission, or decision;
- treating `axis`, `dimension`, `feature`, `property`, or `level` as a recoverable characteristic by appearance;
- treating `strong`, `weak`, `robust`, `high`, `low`, or `better` as scalar or ordered characterizations without their characteristic, scale, and comparison reference or comparator set;
- turning `C.16.P` into a CHR super-pattern or replacement for `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.29`, or `E.21`;
- copying first-stage characterization repair lists into every subject pattern.

### C.16.P:3 - Forces

| Force | Tension |
| --- | --- |
| Compact comparison vs recoverable construction | Readers want quick words such as strong, weak, metric, score, and level; FPF needs characteristic, scale, value, and use boundaries. |
| Measurement discipline vs ordinary evaluation | Some words are informal cues, some are real measurement claims, and some are quality-term or evaluative characterization. |
| Proxy usefulness vs proxy overread | Indicators and scores can be useful proxies but can also hide distortion, threshold choice, and non-comparability. |
| Characteristic-space breadth vs gate discipline | A characteristic space can guide comparison without becoming a gate, decision, or release authority. |
| Mathematical-lens use vs scalar shortcut | A mathematical lens may expose structure, but `C.29` lens-use result is not repaired by score wording alone. |
| Small repair vs full form | Many cases need one repaired phrase or compact note, not a full measurement or characteristic-space publication. |

### C.16.P:4 - Solution

Repair compressed characterization wording by producing a `characteristic-scale repair note` or equivalent local rewrite.

Minimum fields when a note is needed:

```text
CharacteristicScaleRepairNote:
  triggerSpan:
  boundedTextSpanOrPublicationUnit:
  bearer:
  candidateConstruction:
  recoveredCharacteristic?:
  recoveredScale?:
  recoveredCoordinate?:
  recoveredValue?:
  recoveredScore?:
  unit?:
  scoringMethod?:
  indicatorRelationRef?: U.RelationRef for the selected indicated-characteristic, proxy, measurement-use, evidence-use, or other direct relation
  indicatorRelationDisposition: direct-relation | ordinary-indicator-wording | missing-governor
  comparisonReferenceOrComparatorSet?:
  thresholdRuleOrReference?:
  proxyDistortionRisk?:
  relationFunctionClaimRef:
  repairedWordingOrDemotion:
  admissibleUse:
  nonAdmissibleUse?:
  remainingReaderUse:
  disposition:
```

Use the full note only when the repair must remain inspectable. Use a local rewrite when one sentence clearly states the characteristic and scale construction and subject pattern. Keep necessary subject applicability or stop conditions in the repaired wording or `admissibleUse`. Include `nonAdmissibleUse` as an explanatory guard only under F.19:4's full independent-ground, plausible-reader, contribution, and smallest-clear-correction test; an unused guard needs no absence entry.

#### C.16.P:4.1 - Recovery sequence

1. **Capture the trigger.** Copy the exact word or phrase and the sentence that uses it.
2. **Recover the bearer.** Name what is being characterized: holon, pattern, design-rationale record, architecture description, structure, model, method, work result, publication, candidate, relation, decision option, evidence relation, or another subject identified by value. For a relational characteristic, retain the tuple of bearers required by its definition.
3. **Recover the construction.** Decide whether the trigger means `Characteristic`, `Scale`, coordinate, value, score, unit, scoring method, indicator, threshold, comparison reference or comparator set, proxy, Q-bundle, mathematical lens, gate, evidence, decision, or ordinary prose.
4. **Select subject pattern when possible.** If `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.29`, `E.21`, or another subject pattern is already recoverable, use it directly.
5. **Repair hidden characteristic and scale construction.** When construction is hidden, recover the minimal needed set: characteristic, scale, value set, score, unit, scoring method, indicated characteristic or claim, exact direct indicator or proxy relation, comparison reference or comparator set, threshold rule or reference, admissible use, and any necessary applicability or stop condition. Add an explanatory non-admissible-use guard only under the full F.19:4 test. If the text relies on an indicator relation but no governing rule can state or test that claim, return `missing-governor` rather than storing an `indicatorRole` label. Use `A.6.RCD:0.1` to distinguish an absent rule from missing case facts or a failed positive test.
6. **Separate adjacent claims.** Evidence, assurance, gate, work, decision, causal-use, release, benchmark, publication, or authority claims are governed by their direct patterns.
7. **State remaining reader use.** Say what the reader can now compare, measure, score, block, or assign to a neighboring pattern. If the result is type-correct but gives no action or recognition reason, the repair is incomplete.

### C.16.P:5 - Trigger split

| Trigger wording | First recovery question | Not enough |
| --- | --- | --- |
| `metric` | Is there a declared `Characteristic` and `Scale`, with the measure, unit when applicable, scoring method when used, and admissible use required by the claim? | Saying "metric" as a synonym for evidence, quality, performance, or success. |
| `score` | What value on which scale, computed how, and used for what comparison or threshold? | Score as proof, gate passage, readiness, or release. |
| `axis` or `dimension` | Is this a `Characteristic`, coordinate in a characteristic space, mathematical factor, latent coordinate, structural aspect, or ordinary explanatory direction? | `Axis` or `dimension` as self-evident ontology. |
| `feature` or `property` | Is this an observed feature, characteristic, model feature, entity property, relation property, or ordinary prose? | `Feature` or `property` as automatic characteristic. |
| `strong` or `weak` | Does it state a degree of a characteristic or another claim? For a degree, on which scale and under which comparison reference or comparator set? | A degree of a characteristic without its scale. |
| `robust` | Robust to what perturbation, under which scale, comparison, loss, or preserved-structure and lost-structure? | Robust as general praise. |
| `level` | Level on which declared scale or abstraction, not a free hierarchy. | Level as undefined scale or maturity status. |
| `indicator` | Indicator of what characteristic or claim, through which direct relation? If it is a proxy, what is the proxy relation and distortion risk? | Indicator as the indicated property. |
| `threshold` | Predicate over which characteristic space coordinates, with the applicable comparison operator, cut value, band, region, or dominance condition, scalarization policy if any, comparison reference or comparator set, any gate or acceptance relation used by the claim, and necessary applicability or stop conditions? Add an explanatory non-use guard only under F.19:4. | Threshold as characteristic, measure, scalar score, decision, or proof by itself. |
| `benchmark` | Benchmark for which characteristic, comparison set, front, archive, or harness? | Benchmark result as proof or release. |

### C.16.P:6 - Adjacent Claim Governance Named by Value

| Recovered construction, claim kind, or admissible-use boundary | Subject pattern |
| --- | --- |
| `Characteristic` | `A.17` |
| `Scale`, value set, value, coordinate, unit, scoring method, measurement use | `A.18`, `C.16` |
| `CharacteristicSpace` | `A.19` or `A.19.ECS` when evaluation-characteristic-space construction is live |
| Q-bundle or quality-family decomposition into differently typed contributors | `C.25` |
| Quality-term or evaluative characterization wording | `C.16.Q` after any needed characteristic and scale repair |
| Pattern-quality coordinate or pattern-quality evaluation | `E.21` |
| Mathematical function, mathematical lens, preserved-structure and lost-structure, model adequacy or lens-use result | `C.29` for the mathematical-lens-use part; direct model or domain pattern for a non-lens adequacy claim; ordinary mathematics when no FPF-governed use is claimed. |
| CHR mechanism, characteristic-space mechanism, selector, suite, or set-return law | `A.19.CN`, `G.0`, `A.19.UINDM`, `A.19.USCM`, `A.19.ULSAM`, `A.19.CPM`, `A.19.SelectorMechanism`, `G.5`, `C.11`, or mechanism pattern named by value |
| Evidence or proof | The pattern governing the evidence or proof claim; `A.10` when the source-to-use account for a relied-on claim remains implicit. |
| Assurance or engineering justification | `B.3` or the governing assurance pattern for an assurance claim with a named target claim and use; otherwise the pattern governing the engineering justification. |
| Gate, constraint, release, readiness threshold | `A.20`, `A.21`, release or admissibility pattern, or gate pattern governing the claim |
| Decision, choice, selected option | `C.11` |
| Causal-use claim | `C.28` |
| Work, method, operation, implementation | The subject pattern defining the claim; `A.15` for alignment; `A.15.4` only for appearance-based reliance. |
| Source, publication, carrier, dashboard, documentation | `C.2.P`, `E.17`, or publication or source-use pattern governing the claim |
| Relation construction, comparison relation, or wording that says one value supports or is based on another | `A.6.P` while relation meaning is hidden; otherwise the direct relation governor. |

### C.16.P:6a - Refresh and reopen conditions

Reopen or narrow `C.16.P` when current pattern-language ecology changes the first characteristic and scale entry:

- a new characteristic named by value, scale, evaluation, benchmark, proxy or indicator, gate or decision, mathematical-lens, quality, OEE, NQD, or publication pattern can receive one row directly;
- current best-known practice changes comparability, proxy-risk, threshold, measurement, scoring-method, or benchmark-harness discipline adopted in the SoTA-Echoing section;
- README, ToC, `E.11`, retrieval, or local Problem-frame entry cues change the first practical entry for hidden characteristic and scale wording;
- a subject pattern starts copying first-stage `metric`, `score`, `axis`, `strong`, or `indicator` trigger lists that belong here;
- `C.16.P` begins to act as a metrics catalog, maturity scheme, or CHR super-pattern rather than a wording-use repair pattern for hidden construction.

The refresh action is to remove, narrow, or reassign the first-stage row.

### C.16.P:7 - Archetypal Grounding - Worked cases

| Wording | Repair |
| --- | --- |
| "This pattern is stronger." | Recover which claim is meant, including any characteristic and scale it uses. If the sentence means pattern-quality evaluation, use `E.21`; if it means relation strength, use `A.6.P`; if the claimed degree of a characteristic has no scale, demote to ordinary prose or rewrite with the exact gain. |
| "Architecture score improved." | Recover whether this is a score on a declared scale, pattern-quality coordinate, grounded architecture adequacy value, selected-structure characteristic value, Q-bundle value, benchmark result, gate threshold, or ordinary comparison. Use `C.16.P` before using the score. |
| "The metric supports launch." | Recover measure, characteristic, scale, scoring method, threshold predicate or reference, and gate or decision pattern. The metric alone is not launch evidence, gate passage, decision authority, or launch justification. |
| "The model has robust quality." | Recover robustness perturbation and scale, quality-term or evaluative characterization under `C.16.Q`, Q-bundle under `C.25`, or mathematical-lens use under `C.29`. |
| "Latent axis explains behavior." | Recover whether `axis` is a latent coordinate, factor, mathematical lens, characteristic, or ordinary source-local word. Use `C.29` when a mathematical-lens use is being claimed. |
| "The benchmark proves the method is better." | Recover benchmark harness, characteristic space, comparison set, scale, statistical or evidential claim, and decision use. Use evidence named by value, decision, and work patterns as needed. |

### C.16.P:8 - Bias-Annotation

| Bias | Symptom | Correction |
| --- | --- | --- |
| Scalar verdict bias | `strong`, `weak`, `robust`, or `high` is used as a verdict without characteristic, scale, and comparison reference. | Recover the characteristic-scale construction or demote the adjective to ordinary prose. |
| Proxy promotion bias | An indicator, metric, score, or benchmark result is treated as the thing indicated. | Name the direct indicator relation, any proxy relation and distortion risk used by the claim, admissible use, and subject pattern for any wider claim. |
| Gate-by-number bias | A threshold or score is treated as release, readiness, proof, or decision authority. | Recover the threshold rule and cite the gate, assurance, decision, or release pattern that actually governs the use. |

### C.16.P:10 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C16P-1` | The repair names trigger span, bearer, recovered characteristic or scale construction, subject pattern, admissible use, and remaining reader use. Necessary subject applicability and stop conditions remain explicit; an explanatory `nonAdmissibleUse` is optional under the full F.19:4 test. |
| `CC-C16P-2` | `metric`, `score`, `axis`, `dimension`, `feature`, `property`, `indicator`, `strong`, `weak`, `robust`, `level`, `coordinate`, `threshold`, and `benchmark` are trigger words, not recovered kinds by themselves. |
| `CC-C16P-3` | Direct `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.29`, `E.21`, or subject-pattern use applies the subject pattern directly when construction is already recoverable. |
| `CC-C16P-4` | Evidence, assurance, gate, work, decision, causal-use, release, publication, benchmark, and authority claims are governed by their direct patterns. |
| `CC-C16P-5` | The repair does not create a scalar verdict, undefined maturity-status scheme, or release decision. |
| `CC-C16P-6` | The repaired wording preserves one useful admissible reader use; type-correct but inert characterization wording is not recovered by value. |

### C.16.P:11 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Metric-as-evidence | A metric is treated as evidence, proof, gate input, or decision authority without evidence named by value, gate, decision, and measurement construction. | Recover characteristic and scale construction, then apply `A.10` or evidence named by value, gate, or decision pattern if that claim is being made. |
| Score-as-gate | A score is treated as gate passage, readiness, release, or decision. | Recover scale, threshold rule or reference, comparison reference or comparator set, and exact gate, decision, or release pattern. |
| Axis-as-ontology | Axis or dimension is treated as if it already named a characteristic or factor. | Recover `Characteristic`, coordinate, latent factor, mathematical lens, structural aspect, or ordinary prose. |
| Strong-without-scale | Strong or weak asserts a degree of a characteristic without its scale or comparison reference or comparator set. | Write the characteristic named by value and scale or demote to ordinary prose. |
| Indicator-as-indicated-characteristic | Indicator wording hides the indicated characteristic or proxy relation. | Name the indicated characteristic or claim, exact direct relation, and proxy-distortion risk when a proxy is used; return `missing-governor` only when no governing rule can state or test that claim. Keep missing facts and failed positive tests distinct under `A.6.RCD:0.1`. |
| Characterization repair copied everywhere | Patterns for the next questions keep their own `metric`, `score`, or `strong` trigger lists. | Keep one thin cue and use `C.16.P for hidden construction`. |

### C.16.P:12 - Consequences

**Benefits.** C.16.P gives a first-stage repair point for overloaded characterization words, so patterns for the next questions do not need to copy long trigger lists. It makes the next subject pattern visible before a number, adjective, level, score, metric, or benchmark result is treated as actionable.

**Trade-offs.** Some compact phrases become longer because the bearer, characteristic, scale, threshold, proxy, or subject pattern must be named. The gain is that measurement, quality, mathematical-lens, evidence, assurance, gate, decision, and causal-use claims do not hide inside one scalar word.

**Stop condition.** Stop using C.16.P once the characteristic-scale construction and the subject pattern are recoverable. The repaired claim then belongs to `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.29`, `E.21`, or the neighboring pattern named by value.

### C.16.P:12.1 - Rationale

The rationale for C.16.P is narrow: compact characterization wording is useful, but FPF cannot let compact words decide the kind of claim. The pattern restores the bearer, characteristic, scale, value or score construction, proxy relation, threshold rule, admissible use, and subject pattern before the text is allowed to support measurement, comparison, assurance, gate, decision, causal-use, benchmark, or mathematical-lens work.

### C.16.P:12.2 - SoTA-Echoing

Current measurement, quality, proxy-risk, and comparison practice distinguishes characteristics, scales, measures, scores, indicators, thresholds, comparability, proxy status, and decision use. FPF adopts this line only where it changes examples, non-comparability boundaries, indicator and proxy boundaries, scale and scoring method fields, gate and comparison exits, or conformance checks.

| Practice source | Source-use relation and currentness | What `C.16.P` adopts or adapts | FPF import boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 15939:2017 systems and software measurement process. | Current-standard reference for measurement-process discipline. | Disciplines `CharacteristicScaleRepairNote` fields for measure, scale, indicator, measurement use, and information need; informs `CC-C16P-1` and direct use of `C.16`, `A.17`, and `A.18`. | Does not make "metric" a recovered kind, evidence relation, gate, or decision by itself. |
| ISO/IEC 25010:2023 product quality model. | Current-standard reference for quality-characteristic families. | Disciplines quality and scalar-quality cases: a quality word needs characteristic and scale construction or quality-pattern use named by value before comparison, score, or gate use. | Does not import ISO quality characteristics as the FPF quality ontology; quality-term or evaluative characterization still requires `C.16.Q`, `C.25`, or `E.21` when live. |
| ISO/IEC 80000 quantities and units practice and VIM-style metrology vocabulary. | Current reference for quantities, units, and measurement vocabulary. | Disciplines unit, value, scale, and scoring-method fields; blocks number-without-scale and unitless comparison overreads. | Does not impose physical-quantity metrology on qualitative, ordinal, or pattern-quality characteristic spaces. |
| NIST AI RMF 1.0 metric and risk-management practice, including measurement, monitoring, validity, and risk-tolerance framing. | Current practice reference for proxy and indicator risk. | Disciplines `indicatorRelationRef`, `indicatorRelationDisposition`, `proxyDistortionRisk`, threshold rule or reference, and non-admissible use; informs the indicator and proxy and score-as-gate anti-patterns. | Does not let a risk metric, dashboard, or benchmark become assurance, release permission, or decision authority. |
| Current FPF internal characterization stack: `A.17`, `A.18`, `C.16`, `A.19`, `C.25`, `C.29`, and `E.21`. | Current FPF governing-source relation; primary authority for FPF characteristic and scale recovery. | Selects the subject pattern after repair and prevents `C.16.P` from becoming a CHR super-pattern. | Does not copy local trigger lists into subject patterns or replace characteristic-space, quality, mathematical-lens, benchmark, gate, or decision patterns. |

These distinctions block scalar verdicts without declared scale and admissible use. They do not import metric lists, maturity-status schemes, or external scoring traditions as FPF ontology.

### C.16.P:13 - Relations

- `E.10` catches hidden characteristic and scale wording and selects this pattern only when construction is hidden.
- `E.10.ARCH` defines the shared wording-use recovery order and applicability row.
- `A.17`, `A.18`, and `C.16` govern characteristics, scales, values, measures, and measurement use.
- `A.19` governs characteristic-space construction.
- `C.25` governs Q-bundles.
- `C.16.Q` governs quality-term or evaluative characterization wording.
- `E.21` governs pattern-quality evaluation characteristic spaces.
- `C.29` governs mathematical-lens use.
- Exact evidence, assurance, gate, work, decision, causal-use, release, benchmark, and publication patterns define or constrain their own claims.

### C.16.P:End

