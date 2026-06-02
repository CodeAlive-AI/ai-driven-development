## C.16.P - Characteristic and Scale Precision Restoration

> **Type:** Characterization precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Characteristic-scale wording repair.

**Intent.**
Recover characteristic, scale, coordinate, score, metric, indicator, threshold, comparison, and scalar-quality wording whose construction is hidden before a reader applies `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.29`, `E.21`, or another exact receiving pattern.

This pattern is not a metrics-only pattern, not a measurement-method replacement, not a Q-bundle pattern, and not a gate or decision pattern. It repairs overloaded characterization wording so the exact `Characteristic`, `Scale`, `Coordinate`, `Value`, `Score`, `Unit`, `ScoringMethod`, indicator role, comparison basis, proxy role, admissible use, and receiving pattern become recoverable.

**Builds on.** `E.10`, `E.10.ARCH`, `A.17`, `A.18`, `C.16`, `A.19`, `C.25`, `C.29`, `E.21`, `F.18`, and `A.6.P`.

**Coordinates with.** `C.16.Q`, `A.19.ECS`, CHR mechanism patterns, `G.0`, `G.5`, `G.9`, `C.11`, `A.10`, `B.3`, `A.20`, `A.21`, `C.28`, `A.15`, exact evidence, assurance, gate, decision, causal-use, release, work, benchmark, and publication patterns.

### C.16.P:0 - Use this when

Use this pattern when wording such as `axis`, `dimension`, `feature`, `property`, `metric`, `indicator`, `score`, `strong`, `weak`, `robust`, `level`, `coordinate`, `threshold`, `rating`, `benchmark`, `quality coordinate`, or `architecture score` carries characterization force but does not yet show the recoverable construction.

**What goes wrong if missed.** A metric becomes a measure without a scale, a score becomes proof, `strong` becomes a verdict without a characteristic, a level becomes an undefined maturity status, an indicator becomes the thing indicated, or a benchmark result becomes gate passage or release permission.

**What this buys.** The reader can recover the bearer, characteristic, scale, value, score, unit, scoring method, indicator role, comparison basis, threshold, admissible use, and exact receiving pattern before treating a number, adjective, coordinate, or comparison as actionable.

**First useful move.** Ask which bearer, characteristic, scale, value or score construction is recoverable; then apply `C.16`, `A.19`, `C.25`, `C.29`, `E.21`, or the exact neighboring pattern instead of letting the compact word decide.


**Not this pattern when.**

- If the `Characteristic`, `Scale`, value set, scoring method, and admissible use are already recoverable, use `C.16`, `A.17`, `A.18`, or `A.19` directly.
- If the live claim is a Q-bundle, quality/evaluative characterization, or pattern-quality coordinate, use `C.25`, `C.16.Q`, or `E.21` directly after any needed characteristic-scale repair.
- If the live claim is mathematical-lens adequacy, use `C.29`.
- If the live claim is evidence, assurance, gate, work, decision, causal-use, release, benchmark harness, or project authority, use the exact pattern for that claim after characteristic/scale construction is recovered or blocked.

### C.16.P:1 - Problem frame

Working texts often need compact characterization words. The problem starts when compact words begin to carry comparison, proof, selection, gate, readiness, release, quality, or decision force without recoverable characteristic and scale construction.

The repair question is:

> What characteristic or scale construction is recoverable, and what exact receiving pattern carries the remaining claim?

The live object may be:

- a `Characteristic` under `A.17`;
- a `Scale`, coordinate, value, unit, scoring method, measure, or measurement use under `A.18` / `C.16`;
- a `CharacteristicSpace` under `A.19`;
- a Q-bundle under `C.25`;
- quality/evaluative characterization under `C.16.Q`;
- pattern-quality coordinate use under `E.21`;
- mathematical-lens adequacy under `C.29`;
- comparison, threshold, indicator, proxy, benchmark, gate, evidence, decision, or work claim under exact neighboring patterns;
- ordinary prose with no FPF force.

### C.16.P:2 - Problem

How can FPF repair characterization wording without:

- treating `metric` as a universal measurement object;
- treating `score` as proof, readiness, gate passage, release permission, or decision;
- treating `axis`, `dimension`, `feature`, `property`, or `level` as a recoverable characteristic by appearance;
- treating `strong`, `weak`, `robust`, `high`, `low`, or `better` as meaningful without a scale and comparison basis;
- turning `C.16.P` into a CHR super-pattern or replacement for `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.29`, or `E.21`;
- copying first-stage characterization repair lists into every receiving pattern.

### C.16.P:3 - Forces

| Force | Tension |
| --- | --- |
| Compact comparison vs recoverable construction | Readers want quick words such as strong, weak, metric, score, and level; FPF needs characteristic, scale, value, and use boundaries. |
| Measurement discipline vs ordinary evaluation | Some words are informal cues, some are real measurement claims, and some are quality/evaluative characterization. |
| Proxy usefulness vs proxy overread | Indicators and scores can be useful proxies but can also hide distortion, threshold choice, and non-comparability. |
| Characteristic-space breadth vs gate discipline | A characteristic space can guide comparison without becoming a gate, decision, or release authority. |
| Mathematical-lens use vs scalar shortcut | A mathematical lens may expose structure, but `C.29` lens adequacy is not repaired by score wording alone. |
| Small repair vs full form | Many cases need one repaired phrase or compact note, not a full measurement or characteristic-space publication. |

### C.16.P:4 - Solution

Repair compressed characterization wording by producing a `characteristic-scale repair note` or equivalent local rewrite.

Minimum fields:

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
  indicatorRole?:
  comparisonBasis?:
  thresholdBasis?:
  proxyDistortionRisk?:
  exactReceivingPattern:
  repairedWordingOrDemotion:
  admissibleUse:
  nonAdmissibleUse:
  remainingReaderMove:
  disposition:
```

Use the full note only when the repair must remain inspectable. Use a local rewrite when one sentence clearly states the characteristic/scale construction and exact receiving pattern.

#### C.16.P:4.1 - Recovery sequence

1. **Capture the trigger.** Copy the exact word or phrase and the sentence that uses it.
2. **Recover the bearer.** Name what is being characterized: holon, pattern, DRR, architecture description, structure, model, method, work result, publication, candidate, relation, decision option, evidence path, or another exact FPF kind.
3. **Recover the construction.** Decide whether the trigger means `Characteristic`, `Scale`, coordinate, value, score, unit, scoring method, indicator, threshold, comparison basis, proxy, Q-bundle, mathematical lens, gate, evidence, decision, or ordinary prose.
4. **Select direct exact pattern when possible.** If `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.29`, `E.21`, or another exact pattern is already recoverable, use it directly.
5. **Repair hidden characteristic/scale construction.** When construction is hidden, recover the minimal needed set: characteristic, scale, value set, score, unit, scoring method, indicator role, comparison basis, threshold basis, admissible use, and non-admissible use.
6. **Exit adjacent claims.** Evidence, assurance, gate, work, decision, causal-use, release, benchmark, publication, or authority claims go to exact receiving patterns.
7. **State remaining reader move.** Say what the reader can now compare, measure, score, block, or assign to a neighboring pattern. If the result is type-correct but gives no action or recognition reason, the repair is incomplete.

### C.16.P:5 - Trigger split

| Trigger wording | First recovery question | Not enough |
| --- | --- | --- |
| `metric` | Is there a declared `Characteristic`, `Scale`, measure, unit, scoring method, and admissible use? | Saying "metric" as a synonym for evidence, quality, performance, or success. |
| `score` | What value on which scale, computed how, and used for what comparison or threshold? | Score as proof, gate passage, readiness, or release. |
| `axis` / `dimension` | Is this a `Characteristic`, coordinate in a characteristic space, mathematical factor, latent coordinate, structural aspect, or ordinary explanatory direction? | Axis/dimension as self-evident ontology. |
| `feature` / `property` | Is this an observed feature, characteristic, model feature, object property, relation property, or ordinary prose? | Feature/property as automatic characteristic. |
| `strong` / `weak` | Strong or weak on which scale, for which characteristic, under which comparison basis? | Strength without scale. |
| `robust` | Robust to what perturbation, under which scale, comparison, loss, or preserved/lost structure? | Robust as general praise. |
| `level` | Level on which declared scale or abstraction, not a free hierarchy. | Level as undefined scale or maturity status. |
| `indicator` | Indicator of what characteristic or claim, with what proxy relation and distortion risk? | Indicator as the indicated property. |
| `threshold` | Threshold on which scale, with what comparison basis, gate relation, and non-use boundary? | Threshold as decision by itself. |
| `benchmark` | Benchmark for which characteristic, comparison set, front, archive, or harness? | Benchmark result as proof or release. |

### C.16.P:6 - Exact receiving-pattern exits

| Recovered object or claim force | Exit |
| --- | --- |
| `Characteristic` | `A.17` |
| `Scale`, value set, value, coordinate, unit, scoring method, measurement use | `A.18`, `C.16` |
| `CharacteristicSpace` | `A.19` or `A.19.ECS` when evaluation-characteristic-space construction is live |
| Q-bundle or quality-characterization discipline | `C.25` |
| Quality/evaluative characterization wording | `C.16.Q` after any needed characteristic/scale repair |
| Pattern-quality coordinate or pattern-quality evaluation | `E.21` |
| Mathematical function, mathematical lens, preserved/lost structure, model or lens adequacy | `C.29` |
| CHR mechanism, characteristic-space mechanism, selector, suite, or set-return law | `A.19.CN`, `G.0`, `A.19.UINDM`, `A.19.USCM`, `A.19.ULSAM`, `A.19.CPM`, `A.19.SelectorMechanism`, `G.5`, `C.11`, or exact mechanism pattern |
| Evidence or proof | `A.10` or exact evidence pattern |
| Assurance or engineering justification | `B.3` or exact assurance pattern |
| Gate, constraint, release, readiness threshold | `A.20`, `A.21`, release/admissibility pattern, or exact gate pattern |
| Decision, choice, selected option | `C.11` |
| Causal-use claim | `C.28` |
| Work, method, operation, implementation | `A.15`, `A.15.4`, method/work pattern |
| Source, publication, carrier, dashboard, documentation | `C.2.P`, `E.17`, or exact publication/source pattern |
| Relation construction, comparison relation, support-headed relation wording, basedness | `A.6.P` or retained exact relation specialization |

### C.16.P:6a - Refresh and reopen conditions

Reopen or narrow `C.16.P` when current pattern-language ecology changes the first characteristic/scale entry:

- a new exact characteristic, scale, evaluation, benchmark, proxy/indicator, gate/decision, mathematical-lens, quality, OEE/NQD, or publication pattern can receive one row directly;
- current best-known practice changes comparability, proxy-risk, threshold, measurement, scoring-method, or benchmark-harness discipline adopted in `C.16.P:8`;
- `J.4` entry projection changes the first practical entry for hidden characteristic/scale wording;
- a receiving pattern starts copying first-stage metric/score/axis/strong/indicator trigger lists that belong here;
- `C.16.P` begins to act as a metrics catalog, maturity scheme, or CHR super-pattern rather than a wording-use repair pattern for hidden construction.

The refresh action is to remove, narrow, or redirect the first-stage row. It is not to preserve old exits as history.

### C.16.P:7 - Worked cases


| Wording | Repair |
| --- | --- |
| "This pattern is stronger." | Recover the characteristic and scale. If the sentence means pattern-quality evaluation, use `E.21`; if it means relation strength, use `A.6.P`; if no scale exists, demote to ordinary prose or rewrite with the exact gain. |
| "Architecture score improved." | Recover whether this is a score on a declared scale, pattern-quality coordinate, architecture-description adequacy value, Q-bundle value, benchmark result, gate threshold, or ordinary comparison. Use `C.16.P` before using the score. |
| "The metric supports launch." | Recover measure, characteristic, scale, scoring method, threshold basis, and gate/decision pattern. The metric alone is not launch evidence, gate passage, decision authority, or launch justification. |
| "The model has robust quality." | Recover robustness perturbation and scale, quality/evaluative characterization under `C.16.Q`, Q-bundle under `C.25`, or mathematical-lens adequacy under `C.29`. |
| "Latent axis explains behavior." | Recover whether `axis` is a latent coordinate, factor, mathematical lens, characteristic, or ordinary source-local word. Use `C.29` when a mathematical lens is live. |
| "The benchmark proves the method is better." | Recover benchmark harness, characteristic space, comparison set, scale, statistical or evidential claim, and decision use. Use exact evidence/decision/work patterns as needed. |

### C.16.P:8 - Reduced SoTA row

Current measurement, quality, proxy-risk, and comparison practice distinguishes characteristics, scales, measures, scores, indicators, thresholds, comparability, proxy status, and decision use. FPF adopts this line only where it changes examples, non-comparability boundaries, indicator/proxy boundaries, scale and scoring method fields, gate/comparison exits, or conformance checks.

| Practice basis | Source posture | What `C.16.P` adopts or adapts | FPF import boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 15939:2017 systems and software measurement process. | Current-standard/reference support for measurement-process discipline. | Disciplines `CharacteristicScaleRepairNote` fields for measure, scale, indicator, measurement use, and information need; supports `CC-C16P-1` and direct exits to `C.16`, `A.17`, and `A.18`. | Does not make "metric" a recovered kind, evidence path, gate, or decision by itself. |
| ISO/IEC 25010:2023 product quality model. | Current-standard/reference support for quality-characteristic families. | Disciplines quality and scalar-quality cases: a quality word needs characteristic/scale or exact quality pattern use before comparison, score, or gate use. | Does not import ISO quality characteristics as the FPF quality ontology; quality/evaluative characterization still exits to `C.16.Q`, `C.25`, or `E.21` when live. |
| ISO/IEC 80000 quantities/units practice and VIM-style metrology vocabulary. | Current reference support for quantities, units, and measurement vocabulary. | Disciplines unit, value, scale, and scoring-method fields; blocks number-without-scale and unitless comparison overreads. | Does not force physical-quantity metrology onto qualitative, ordinal, or pattern-quality characteristic spaces. |
| NIST AI RMF 1.0 metric/risk-management practice, including measurement, monitoring, validity, and risk-tolerance framing. | Current practice/reference support for proxy and indicator risk. | Disciplines `indicatorRole`, `proxyDistortionRisk`, threshold basis, and non-admissible use; supports the indicator/proxy and score-as-gate anti-patterns. | Does not let a risk metric, dashboard, or benchmark become assurance, release permission, or decision authority. |
| Current FPF internal characterization stack: `A.17`, `A.18`, `C.16`, `A.19`, `C.25`, `C.29`, and `E.21`. | Current FPF governing-source support; primary authority for FPF characteristic and scale recovery. | Selects the exact receiving pattern after repair and prevents `C.16.P` from becoming a CHR super-pattern. | Does not copy local trigger lists into receiving patterns or replace exact characteristic-space, quality, mathematical-lens, benchmark, gate, or decision patterns. |

This row blocks scalar verdicts without declared scale and admissible use. It does not import metric lists, maturity-status schemes, or external scoring traditions as FPF ontology.
### C.16.P:9 - Conformance checklist

| Check | Requirement |
| --- | --- |
| `CC-C16P-1` | The repair names trigger span, bearer, recovered characteristic or scale construction, exact receiving pattern, admissible use, non-admissible use, and remaining reader move. |
| `CC-C16P-2` | `metric`, `score`, `axis`, `dimension`, `feature`, `property`, `indicator`, `strong`, `weak`, `robust`, `level`, `coordinate`, `threshold`, and `benchmark` are trigger words, not recovered kinds by themselves. |
| `CC-C16P-3` | Direct `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.29`, `E.21`, or exact receiving-pattern use applies the exact pattern directly when construction is already recoverable. |
| `CC-C16P-4` | Evidence, assurance, gate, work, decision, causal-use, release, publication, benchmark, and authority claims exit to exact receiving patterns. |
| `CC-C16P-5` | The repair does not create a metrics-only restoration pattern, CHR super-pattern, scalar verdict, undefined maturity-status scheme, or release decision. |
| `CC-C16P-6` | The repaired wording preserves one useful admissible reader move; type-correct but inert characterization wording is not recovered by value. |

### C.16.P:10 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Metric-as-evidence | A metric is treated as evidence, proof, gate input, or decision authority without exact evidence, gate, decision, and measurement construction. | Recover characteristic/scale construction, then apply `A.10` or exact evidence, gate, or decision pattern if that claim is live. |
| Score-as-gate | A score is treated as gate passage, readiness, release, or decision. | Recover scale, threshold basis, comparison basis, and exact gate/decision/release pattern. |
| Axis-as-ontology | Axis or dimension is treated as if it already named a characteristic or factor. | Recover `Characteristic`, coordinate, latent factor, mathematical lens, structural aspect, or ordinary prose. |
| Strong-without-scale | Strong or weak modifies a claim without scale, characteristic, or comparison basis. | Write the exact characteristic and scale or demote to ordinary prose. |
| Indicator-as-indicated-characteristic | Indicator wording hides the indicated characteristic or proxy relation. | Name indicator role, indicated characteristic or claim, and proxy-distortion risk. |
| Characterization repair copied everywhere | Receiving patterns keep their own metric/score/strong trigger lists. | Keep one thin cue and send hidden construction to `C.16.P`. |

### C.16.P:11 - Related patterns

- `E.10` catches hidden characteristic/scale wording and selects this pattern only when construction is hidden.
- `E.10.ARCH` defines the shared wording-use recovery order and applicability row.
- `A.17`, `A.18`, and `C.16` govern characteristics, scales, values, measures, and measurement use.
- `A.19` governs characteristic-space construction.
- `C.25` governs Q-bundles.
- `C.16.Q` governs quality/evaluative characterization wording.
- `E.21` governs pattern-quality evaluation characteristic spaces.
- `C.29` governs mathematical-lens adequacy.
- Exact evidence, assurance, gate, work, decision, causal-use, release, benchmark, and publication patterns govern their own claims.

### C.16.P:End


