## C.16.P - Restore Precision to Characteristic and Scale Wording

> **Type:** Characterization precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Characteristic-scale wording repair.

**Intent.** Restore the meaning of a characterization claim when a compact word hides what is characterized, how it is assessed or compared, or what the result supports. Once those relations are clear, use the applicable subject pattern.

### C.16.P:0 - Use this when

Use this pattern when a word such as `metric`, `strong`, `indicator` or `threshold` carries a characterization claim whose basis is unclear. A score may hide its Scale, an indicator its relation to the property indicated, or an apparent improvement the comparison that supports it.

**First useful move.** Ask what is being characterized, what the sentence asserts about it, and which basis the reader needs to interpret or use that assertion. Repair only the missing contribution. An ordinary sentence can be sufficient.

When the meaning and applicable conditions are already recoverable, use the subject pattern or ordinary domain explanation directly. The neighboring patterns in §6 govern their own questions; use C.16.P only for the unresolved wording.

### C.16.P:1 - Problem frame

Working texts often use compact characterization words. A problem arises when a term implies a comparison or further conclusion while hiding the construction that could support it.

The repair question is:

> What does the sentence assert about which subject, what supports its intended comparison or use, and which rule governs any further FPF claim?

### C.16.P:2 - Problem

The same compact word can denote different constructions. An “axis” can be a coordinate in a model, a Characteristic or an ordinary explanatory direction. A score can supply a value for a comparison without establishing a wider claim about evidence, readiness or permission.

The repair must recover the meaning needed by the receiving work. It should not require a new measurement, characteristic space or formal record when an ordinary explanation or an already applicable subject rule settles the question.

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

Rewrite the claim so the reader can recover its subject, the relevant characterization or comparison, its basis and the use it supports. Keep necessary applicability and stop conditions.

When the receiving work needs a separate inspectable note, the following scaffold can retain the repair. Include only fields relevant to that claim:

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
  indicatorRelationDisposition?: direct-relation | ordinary-indicator-wording | missing-governor
  comparisonReferenceOrComparatorSet?:
  thresholdRuleOrReference?:
  proxyDistortionRisk?:
  relationFunctionClaimRef?:
  repairedWordingOrDemotion:
  admissibleUse:
  nonAdmissibleUse?:
  remainingReaderUse:
  disposition:
```

A local rewrite is sufficient when the sentence conveys the needed meaning and conditions. An ordinary PatternID can locate the governing rule. Include `relationFunctionClaimRef` only when the use depends on the identity of its defining or constraining ClaimGraph. Include `indicatorRelationDisposition` when an indicator or proxy relation is under repair, following §4.1. An explanatory `nonAdmissibleUse` guard is optional under F.19:4's independent-ground, plausible-reader, contribution and smallest-clear-correction test; its absence needs no entry.

#### C.16.P:4.1 - Recovery sequence

1. **Read the trigger in its sentence.** Recover the complete assertion. Retain the source wording when the repair needs an inspectable comparison.
2. **Recover the bearer.** Name the subject being characterized. For a relational Characteristic, retain the tuple required by its definition.
3. **Recover the construction.** Use §5 to identify what the wording means. A trigger can be ordinary prose; its appearance does not create an FPF kind.
4. **Use a recovered subject rule directly.** Once the construction is clear, apply its subject pattern from §6 or the relevant domain practice.
5. **Repair what remains hidden.** Recover the contributions needed by this claim: for a measurement, its Characteristic, Scale and interpretation; for a comparison, its reference or comparator set; for a threshold, its predicate and applicability; for an indicator, the indicated property or claim and the direct relation, including distortion risk when it is a proxy. Keep necessary use and stop conditions. If an indicator relation is required but no governing rule can state or test it, return `missing-governor` rather than storing an `indicatorRole` label. Use A.6.RCD:0.1 to distinguish that absent rule from missing case facts or a failed positive test. Add explanatory non-use guards only under the F.19:4 test.
6. **Separate further claims.** A measurement or score may contribute to evidence, a decision or another use. Apply the governing conditions for that additional claim; repairing the characterization alone does not establish it.
7. **Return a useful statement.** Say what the reader can now recognize, compare or conclude, or which missing contribution leaves the claim unresolved. Type-correct wording with no useful interpretation is insufficient.

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

### C.16.P:7 - Archetypal Grounding - Worked cases

| Wording | Repair |
| --- | --- |
| "This pattern is stronger." | Recover which claim is meant, including any characteristic and scale it uses. If the sentence means pattern-quality evaluation, use `E.21`; if it means relation strength, use `A.6.P`; if the claimed degree has no basis, state the supported narrower gain or leave that degree unresolved. |
| "Architecture score improved." | Recover whether this is a score on a declared scale, pattern-quality coordinate, grounded architecture adequacy value, selected-structure characteristic value, Q-bundle value, benchmark result, gate threshold, or ordinary comparison. Repair the wording only while the intended comparison remains unclear; use the recovered score construction directly. |
| "The metric supports launch." | Recover measure, characteristic, scale, scoring method, threshold predicate or reference, and gate or decision pattern. A measurement may support a named launch criterion; establish that evidence use and any further launch conditions under their governing rules. |
| "The model has robust quality." | Recover robustness perturbation and scale, quality-term or evaluative characterization under `C.16.Q`, Q-bundle under `C.25`, or mathematical-lens use under `C.29`. |
| "Latent axis explains behavior." | Recover whether `axis` is a latent coordinate, factor, mathematical lens, characteristic, or ordinary source-local word. Use `C.29` when a mathematical-lens use is being claimed. |
| "The benchmark proves the method is better." | Recover benchmark harness, characteristic space, comparison set, scale, statistical or evidential claim, and decision use. Use evidence named by value, decision, and work patterns as needed. |

**Worked comparison.** A report calls a new implementation “stronger.” Its supplied observations concern response time in four matched workload cases under the same conditions. Response time is elapsed duration on a ratio Scale, expressed in milliseconds. The earlier times are 80, 100, 120 and 140 ms; the new times are 70, 90, 110 and 130 ms. Both comparisons use the median, defined here as the mean of the two middle ordered values. The respective medians are 110 and 100 ms.

The supported rewrite is: “For these four matched workload cases, median response time fell by 10 ms, from 110 to 100 ms.” It names the Characteristic, Unit, comparison set and scoring operation and can finish the wording repair. It supplies no comparison for other workloads. If a receiving criterion requires median response time at most 105 ms on these cases, the new value satisfies that numerical condition. Any other release conditions remain separate. If the new trials used different workload cases, the original comparison would need an account of their comparability before supporting the same claim.

### C.16.P:8 - Bias-Annotation

| Bias | Symptom | Correction |
| --- | --- | --- |
| Scalar verdict bias | `strong`, `weak`, `robust`, or `high` is used as a verdict without characteristic, scale, and comparison reference. | Recover the intended construction and its basis, state a supported narrower gain, or leave the characterization unresolved. |
| Proxy promotion bias | An indicator, metric, score, or benchmark result is treated as the thing indicated. | Name the direct indicator relation, any proxy relation and distortion risk used by the claim, admissible use, and subject pattern for any wider claim. |
| Gate-by-number bias | A threshold or score is treated as release, readiness, proof, or decision authority. | Recover the threshold rule and cite the gate, assurance, decision, or release pattern that actually governs the use. |

### C.16.P:10 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C16P-1` | The repaired statement makes its subject, relevant characterization or comparison, basis and supported use recoverable. It identifies an applicable subject rule when that rule is needed; a separate note is conditional on the receiving work. Necessary subject applicability and stop conditions remain explicit; an explanatory `nonAdmissibleUse` is optional under the full F.19:4 test. |
| `CC-C16P-2` | The words in §5 are triggers for interpretation, not recovered kinds by themselves. |
| `CC-C16P-3` | Direct `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.29`, `E.21`, or subject-pattern use applies the subject pattern directly when construction is already recoverable. |
| `CC-C16P-4` | Evidence, assurance, gate, work, decision, causal-use, release, publication, benchmark, and authority claims are governed by their direct patterns. |
| `CC-C16P-5` | The repair does not create a scalar verdict, undefined maturity-status scheme, or release decision. |
| `CC-C16P-6` | The repaired wording preserves one useful admissible reader use; type-correct but inert characterization wording is not recovered by value. |

### C.16.P:11 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Metric-as-evidence | A metric is used to assert evidence, proof, gate passage or decision authority without the conditions that establish that relation. | Recover characteristic and scale construction, then apply `A.10` or evidence named by value, gate, or decision pattern if that claim is being made. |
| Score-as-gate | A score is treated as gate passage, readiness, release, or decision. | Recover scale, threshold rule or reference, comparison reference or comparator set, and exact gate, decision, or release pattern. |
| Axis-as-ontology | Axis or dimension is treated as if it already named a characteristic or factor. | Recover `Characteristic`, coordinate, latent factor, mathematical lens, structural aspect, or ordinary prose. |
| Strong-without-scale | Strong or weak asserts a degree of a characteristic without its scale or comparison reference or comparator set. | State the Characteristic and Scale used by the claim, or replace the unsupported degree with a supported narrower statement. |
| Indicator-as-indicated-characteristic | Indicator wording hides the indicated characteristic or proxy relation. | Name the indicated characteristic or claim, exact direct relation, and proxy-distortion risk when a proxy is used; return `missing-governor` only when no governing rule can state or test that claim. Keep missing facts and failed positive tests distinct under `A.6.RCD:0.1`. |

### C.16.P:12 - Consequences

**Benefits.** The reader can interpret the characterization, identify the supported comparison or use, and locate a missing contribution without constructing a larger measurement account unnecessarily.

**Trade-offs.** Some compact phrases become longer because the bearer, characteristic, scale, threshold, proxy, or subject pattern must be named. The gain is that measurement, quality, mathematical-lens, evidence, assurance, gate, decision, and causal-use claims do not hide inside one scalar word.

**Stop condition.** Stop when the intended characterization, its basis and applicable conditions are recoverable. An adequate ordinary statement can finish the repair. Continue to a subject pattern only for a remaining question that needs it.

### C.16.P:12.1 - Rationale

A compact word can summarize a construction once the reader can recover it. Restoring only the missing subject, relation or condition lets that shorthand remain useful while making its actual implication inspectable.

### C.16.P:12.2 - SoTA-Echoing

Measurement and comparison practice distinguishes characteristics, scales, measures, indicators and their intended uses. These sources contribute different parts of that recovery:

| Practice source | Contribution to wording repair | Use boundary |
| --- | --- | --- |
| ISO/IEC/IEEE 15939:2017, systems and software measurement process | Connects measures, indicators and measurement use to an information need. | The word “metric” alone supplies neither a measure's construction nor its evidence or decision use. |
| ISO/IEC 25010:2023, product quality model | Distinguishes quality-characteristic families and their interpretation in comparison. | Its characteristics retain their source meanings; FPF quality-term and evaluative uses follow C.16.Q, C.25 or E.21 when applicable. |
| ISO/IEC 80000 quantities and units practice and VIM-style metrology vocabulary | Distinguishes quantity, unit, value and measurement meanings. | Qualitative and ordinal characterizations retain their own Scale conditions rather than importing physical-quantity arithmetic. |
| NIST AI RMF 1.0, measurement and risk-management practice | Connects validity, monitoring and risk tolerance to interpretation of indicators, proxies and thresholds. | A risk reading can contribute to a named assessment; a wider assurance or release claim requires its own grounds. |

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
