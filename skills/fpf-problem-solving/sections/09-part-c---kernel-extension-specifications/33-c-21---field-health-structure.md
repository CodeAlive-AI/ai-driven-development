## C.21 - Field Health & Structure (Discipline-CHR)

> **Status:** Stable
> **Type:** Pattern

> *Purpose.* Give FPF a typed, reviewable way to characterize the health, maturity, and structure of a scientific or engineering discipline without collapsing the result into taste, anecdotes, a dashboard view, an audit label, or one score. C.21 defines discipline-health Characteristics and the conditions under which their readings may be compared. It does not make a dashboard, publication, record, or Work occurrence part of the discipline.

### C.21:0 - Use This When

Use this pattern when a team must say something practical about the health, maturity, or structure of an already identified discipline. Typical questions concern reproducibility, formal standard status, actual adoption, cross-tradition alignment, disruption balance, evidence resolution, diversity, engineering-claim recoverability, or pressure to mistake representations for their subjects.

**What goes wrong if missed.** Field-health claims become attractive labels: incompatible readings are compared, ordinals are averaged, formal approval is treated as adoption, entropy and concentration are read in the same direction, stale evidence looks current, and a dashboard or standards list starts acting as the discipline or as proof of health.

**What this buys.** A cold reader can recover one health claim, its Characteristic and Scale, the discipline and claim scope, the comparison and time or population basis, the measurement definition when one is used, and the exact extra relation required only for an actual cross-local comparison.

**First useful move.** Name the discipline and practical question, choose one relevant Characteristic, state its scope and comparison basis, and say in ordinary language what the current material supports and what it does not. Stop there when the receiving use needs no measured comparison, aggregate, reusable series, or publication.

**Not this pattern when.** Use C.20 to decide whether the candidate is a discipline, C.16 to construct a measurement, A.19 for comparison or aggregation work, F.9 only when the use actually relates distinct local senses, E.24.PUB for audience availability, G.12 for a reusable dashboard view, and G.4 for an acceptance threshold. C.21 supplies none of those results merely by naming a health Characteristic.

**Placement.** Part C, Cluster C.I. **Builds on:** C.20, A.17, A.18, C.16, A.2.6, C.2.1. **Coordinates with:** F.9, G.0, G.4, G.9, G.11, G.12, E.24.PUB.

### C.21:1 - Problem Frame

A discipline can persist as its constituents and associated epistemes, practices, standards, institutions, and Work change. Teams routinely say “replication is improving,” “the field is fragmented,” or “standards are converging.” Such a sentence can be useful before it becomes a dashboard row, but any relied-on comparison needs exact Characteristic, Scale, measurement, scope, and basis semantics.

C.21 therefore treats health as a vector of separately typed coordinate claims. It does not imply one scalar health value. A threshold or target band is an acceptance declaration under G.4, not part of the Characteristic. A dashboard is a representation over already constituted claims, not their ontology or authority.

### C.21:2 - Problem

Five recurrent failures make discipline-health claims unreliable:

1. **Object collapse.** A definition set, Method, MethodDescription, measurement Work, result episteme, series episteme, publication occurrence, form, and carrier are called one “DHC artefact.”
2. **Scope slippage.** `ClaimScope` and a selected `TargetSlice` are treated as interchangeable, although the scope states where the claim holds and the slice is only an optional computation or publication input.
3. **False crossing.** Different sources or editions are assumed to require a Bridge even when C.16 direct-comparability conditions hold; conversely, distinct local senses are compared without their obtaining F.9 relation and loss account.
4. **Scale collapse.** Formal recognition is ordered with adoption, alternative ratios are called one Characteristic, or entropy and HHI are placed in one field despite opposite directions.
5. **Assurance inflation.** A cheap readable claim is forced through evidence graphs, registries, dashboard pins, and publication machinery that its receiving use does not consume.

### C.21:3 - Forces

| Force | Tension |
| --- | --- |
| Comparability vs nuance | A wider field picture is useful, but exact definitions, populations, windows, schemes, and local meanings must survive. |
| Readable minimum vs replay | One ordinary claim should be cheap; a numerical comparison or reusable series needs enough identity to be repeated. |
| Ordinal vs interval or ratio | Ranks and categories invite illegal arithmetic. |
| Formal status vs actual adoption | Approval by a standards body and use by a population can vary independently. |
| Direct comparison vs cross-local relation | Compatible readings compare directly; a comparison that relies on a cross-local semantic relation needs its truth, bounded use, and loss account established separately. |
| Recency vs stability | Health changes through time; a trend needs explicit windows and current definition editions. |
| Evidence vs publication | Support, measurement, series content, dashboard representation, and audience availability answer different questions. |

### C.21:4 - Solution — Discipline Health Characterisation (DHC)

#### C.21:4.0 - The objects used by DHC

“DHC” names this vocabulary and method of use. It does not admit `U.DHCPack`, `U.DHCMethodSpec`, or `U.DHCSeries` as public kinds.

| Object | What it is | What it is not |
| --- | --- | --- |
| DHC Characteristic and Scale declarations | Exact A.17 Characteristic and A.18 Scale definitions, with Unit and polarity when applicable. | A dashboard field or a health verdict. |
| `DHCDefinitionSet` when a reusable selection is needed | One C.2.1 episteme about the already identified discipline. Its ClaimGraph states the intended use and selects exact Characteristic, Scale, Unit, and measurement-definition editions. | A slot-set kind, the discipline, or a publication. Ordinary one-coordinate use needs no such episteme. |
| `DHCMethodRef.edition` | The existing C.16 measurement-definition value for one Characteristic and Scale. It resolves the exact `U.Method`, any `U.MethodDescription` edition, model, calibration basis, uncertainty treatment, construction, and time or population policy used by the reading. | The Method, MethodDescription, measurement Work, or result. |
| DHC coordinate result | A C.16 measurement result and, when persisted as a claim, one C.2.1 result episteme about the discipline. | A time-series publication, dashboard row, or acceptance decision. |
| `DHCSeries` when repeated use needs one | One C.2.1 episteme whose EntityOfConcern is the discipline and whose ClaimGraph orders exact coordinate-result episteme refs by window under one intended use, ClaimScope, comparison basis, and definition basis. Changed claim content identifies another episteme; historical continuation is tested separately under C.2.1's applicable edition rule. | A publication occurrence, form, carrier, table, or the Work that assembled it. |
| dashboard row or slice | A C.29 or G.12 representation over exact result or series refs. | The result, evidence, series episteme, publication, or discipline. |
| publication occurrence | An obtaining E.24.PUB availability relation among one selected episteme edition, audience declaration, bounded-use declaration, form, carrier, and availability interval. | Rendering, upload, release, measurement, or series-assembly Work. |

Rendering, measuring, assembling a series, uploading, and maintaining availability may each be Work when actually performed. A work record or carrier does not make that Work occur.

#### C.21:4.0a - One replay basis for every persisted coordinate

Every persisted, compared, aggregated, or published coordinate makes the following values recoverable. This is a field group, not another public kind:

`DHCReplayBasis := <DisciplineRef, IntendedUse, ClaimScopeRef, ComparisonBasis, CharacteristicRef.edition, ScaleRef.edition, UnitRef.edition?, DHCMethodRef.edition, MethodRef, MethodDescriptionRef.edition?, MeasurementModelRef.edition?, CalibrationBasisRef?, TimeOrPopulationBasis, DHCDefinitionSetRef.edition?, TargetSliceRef?, DistanceDefRef.edition?>`

- `DHCMethodRef.edition` resolves the same Characteristic, Scale, Method, MethodDescription, model, calibration, and uncertainty semantics named by the active fields. A mismatch is not repaired by choosing one field as “primary.”
- `DHCDefinitionSetRef.edition` appears only when a named reusable definition selection exists.
- `TargetSliceRef` appears only when the named computation or publication actually consumes an A.2.6 selection. Every selected slice must be shown to belong to, or otherwise be covered by, the authoritative `ClaimScope`; the slice never substitutes for that scope.
- `DistanceDefRef.edition` appears only when the Scale comparison or target-distance rule uses a separately declared distance.
- Evidence paths, lane tags, currentness, assurance, acceptance, public names, and publication refs are added only when the receiving use consumes those separate results.

#### C.21:4.1 - Portable Characteristics

Each bullet below names one exact Characteristic and Scale family. A DHC use selects only the coordinates needed by its question.

1. **ReproducibilityRate** — ratio in `[0,1]`; Unit `replicated_claims/tested_claims`; polarity higher-is-more-reproducible, not “healthier in every respect.” Declare the tested claim or benchmark population, independent-team condition, protocol, corpus or cohort, and time window.

2. **FormalRecognitionStatus** — nominal by default. Values such as `none`, `draft`, `approved`, `withdrawn`, or another lifecycle vocabulary belong to one named standards body and exact status scheme. Use an ordinal only when that scheme itself supplies a lawful order. There is no general `de facto < de jure` ladder and no default health polarity.

3. **PracticeAdoptionRate** — ratio in `[0,1]`; Unit `adopting_units/eligible_units`. Declare the population, adoption criterion, observation window, and treatment of partial adoption. Higher means wider observed adoption, not automatically better health or SoTA.

4. **AlignmentDensity** — ratio; Unit `obtaining_relations/100_compared_cells`. Count only exact obtaining directed F.9 relations in the declared F.17 cell set. For each counted relation, state its orientation and admitted-use qualifier; keep observed loss in its evidence account, separate from any bounded-use claim under section 4.2. A higher value means denser declared alignment for that set; any health band belongs to G.4.

5. **DisruptionBalance** — interval reading over one exact disruption/consolidation method and corpus. Polarity is target-is-best, using an explicit target-band distance rule; the band belongs to G.4 Acceptance.

6. **EvidenceUnitResolution** — ordinal, compare-only, under one exact segmentation scheme whose levels are nested, for example `artifact < section < claim < subclaim`. Higher means a finer addressable unit under that scheme. It does not say how many claims an artifact contains or how densely claims are supported.

7. **ClaimsPerArtifact** — ratio; Unit `claims/artifact`, with exact claim segmentation and artifact population. It measures claim breadth or packing, not support density. Declare a target band when the use needs one; no universal monotone health polarity applies.

8. **SupportAnchorsPerClaim** — ratio; Unit `anchors/claim`, with exact anchor admissibility and claim segmentation. It measures support-anchor density, not claim size. It has no universal monotone health polarity.

9. **TraditionShareEntropy** — one exact entropy Characteristic and Scale, with log base, normalization, category set, and population fixed. Higher entropy means greater dispersion on that scale. Any desired band is separate.

10. **TraditionShareConcentration** — HHI or another exact concentration Characteristic, normally ratio in `[0,1]`; higher HHI means greater concentration and therefore lower dispersion. Do not place it in the entropy field. `1 - HHI` may be introduced only as an explicit transformation to a separately declared receiving Scale. Comparing that result with normalized entropy still requires an explicit common comparison rule.

#### C.21:4.1a - Engineering-grade extension Characteristics

A discipline-health use may add these coordinates when its question needs them. They do not become evidence, assurance, gate, release, Work, or project-authority results.

11. **EngineeringClaimJustificationRecoverability** — ordinal, polarity higher-is-more-recoverable. It asks whether the exact construction, source, model, lens, or relation carrying an engineering claim's force can be recovered for the intended use. The reading cites the direct pattern and rule that define or constrain that force.

12. **SemioSubstitutionPressure** — ordinal or ratio as separately declared, polarity lower-is-less-substitution-pressure. It asks how often a representation, fluent wording, record, dashboard, view, or source chain is mistaken for its engineering subject, relation, or claim.

When either extension is active, add a short explanation naming the current claim kind or use boundary, the direct pattern and rule, admissible use, prohibited overread, and stop or reopen condition. The explanation is claim content, not a new evidence or assurance object.

#### C.21:4.2 - Comparison and legality rules

1. **Direct same-semantics comparison.** Compare readings directly when C.16's conservative conditions hold: the same measurement definition, Characteristic, Scale and Unit semantics, compatible model and calibration regime, and compatible time or population basis. Record the admitted comparison basis. Different source labels or editions alone require no Bridge.
2. **Cross-local comparison.** When a comparison relies on a semantic relation between distinct F.17 local senses, cite the exact obtaining F.9 Bridge only after its predicate and dependencies hold. Keep its separate C.2.1 bounded-use claim, with the use, direction, correspondence rule, permitted-loss tolerance, and polarity, distinct from observed loss and current reliance. Follow F.9's A.10 reliance branch or, for an actual named assurance claim, its B.3 branch for the same bounded use. If the assurance use requires an R adjustment, cite the applicable domain model and keep the adjustment in that use's AssuranceResult. The relation supplies none of ClaimScope, measurement, comparison, or acceptance semantics.
3. **Reference-plane crossing.** When a reading is used across distinct world, concept, or episteme planes, cite the exact crossing basis. Any R adjustment follows the named assurance-use and domain-model condition in rule 2. A dashboard row or source label does not establish the crossing.
4. **Cross-scale transformation.** A conversion, normalization, distance, or aggregate names its exact Method, Scale, legal operation, and loss or uncertainty. No common scale is inferred from similar labels.
5. **Freshness.** A persisted or reused coordinate carries its observation window and applicable currentness rule. Staleness leads to the receiving pattern's degrade, abstain, or reopen result; it does not rewrite the historical measurement.
6. **Target bands.** “Target-is-best” is not “higher-is-better.” A comparison to a band uses an explicit distance-to-band rule and leaves the G.4 threshold separate.
| Scale family | Lawful ordinary operations | Prohibited shortcut |
| --- | --- | --- |
| nominal status | equality, membership, mode when justified | lifecycle ranking or arithmetic without an ordered scheme |
| ordinal resolution | order, median or mode where meaningful | mean, ratio, or affine arithmetic |
| ratio rate or density | operations allowed by its exact Scale and Unit | unit mixing or comparison across changed construction |
| interval balance | differences and target distance under its exact rule | ratios or silent target-band polarity |
| entropy and concentration | operations under their own definitions | treating entropy and HHI as interchangeable or equally directed |

### C.21:5 - Three progressive uses

#### C.21:5.1 - Minimal readable health claim

State the discipline, intended use, one Characteristic, the ClaimScope, comparison or observation basis, time stance, and ordinary result. Name the support actually relied on. Stop when this answers the working question. Do not require an EvidenceGraph, UTS row, registry, dashboard, definition set, series, or publication occurrence.

#### C.21:5.2 - Measurement, comparison, or aggregation

Open C.16 when an actual measurement is claimed. Make the DHC replay basis recoverable, identify measurement Work and result separately, and apply A.18 legality. For direct comparison use the same-semantics branch in section 4.2. For a comparison that relies on a cross-local semantic relation, add the exact F.9 branch. Open G.0, A.19, normalization, distance, evidence-reliance, or assurance only when the operation or receiver actually consumes it.

#### C.21:5.3 - Reusable series, dashboard, or publication

Create a `DHCDefinitionSet` only when a reusable selection of definitions is needed. Create a `DHCSeries` episteme only when the receiving use needs ordered coordinate-result refs across windows. Use G.12 for a dashboard representation and refresh wiring. When an audience must be able to obtain a selected edition, use E.24.PUB and keep the availability relation, form, carrier, and any publishing Work distinct. Public naming and registry behavior remain conditional on a named use.

### C.21:6 - Archetypal Grounding (five domains)

#### C.21:6.1 - Computer vision: direct comparison without a Bridge

Two `ReproducibilityRate` results concern the same benchmark population and ClaimScope. Both cite the same Characteristic and ratio Scale editions, the same `DHCMethodRef.edition`, compatible model and calibration rules, and matching 24-month population windows. The team compares the two rates directly under that basis. The source reports have different publication editions, but no distinct F.17 local senses are being related, so no F.9 relation is invented.

Formal benchmark approval and actual benchmark adoption are reported separately as `FormalRecognitionStatus` and `PracticeAdoptionRate`.

#### C.21:6.2 - Biomedicine: evidence resolution without ratio substitution

One claim reports `EvidenceUnitResolution = claim` under `ClinicalClaimSegmentation-3`. A separate result reports `SupportAnchorsPerClaim = 2.4 anchors/claim` for the declared corpus. Neither value is substituted for `ClaimsPerArtifact`. Replication is a separate `ReproducibilityRate` over independent cohorts and a 36-month window.

#### C.21:6.3 - Software performance engineering: explicit cross-local use

The compared cells are `OpenTelemetry:SLO/latency-objective@E4` and `VendorB:SLO/service-level-target@E7`. For this example, take `F9-SPE-SLO-12` as an independently established directed F.9 Bridge from the OpenTelemetry cell to the VendorB cell under a satisfied predicate profile. A separate C.2.1 bounded-use claim states suitability for “compare service-latency objective coverage in the 2026 survey” in that direction, using only rows with the aligned 30-day window and tolerating no rolling-window mismatch. The evidence loss note records that the target cell permits a different rolling-window convention; the comparison still requires current A.10 reliance on the bounded-use claim. That directed relation is one counted member of the declared AlignmentDensity cell set; it does not make all tracing-ecosystem readings comparable.

#### C.21:6.4 - Decision-making: entropy and concentration stay separate

`TraditionShareEntropy` uses normalized Shannon entropy with base and category set fixed. `TraditionShareConcentration` uses HHI over the same population and has the opposite dispersion direction. A view may show both. If a receiving comparison wants one orientation, it declares `1-HHI` as a transformation and still does not equate that Scale with normalized entropy.

#### C.21:6.5 - Evolutionary architecture: banded disruption

`DisruptionBalance` is computed over one declared corpus and method edition. The result is interpreted against an explicit target band and distance rule; a higher raw value is not automatically healthier. Architecture decision records and fitness tests remain inputs or neighboring objects, not evidence that the field itself is healthy.

### C.21:7 - Authoring Rhythm

1. State the ordinary health question and smallest useful conclusion.
2. Identify the discipline under C.20 and one exact Characteristic and Scale.
3. State ClaimScope, comparison or observation basis, and time or population basis.
4. Stop if an ordinary typed claim is enough.
5. If measuring, comparing, or aggregating, recover the C.16 chain and DHC replay basis; add only the exact legal-operation and crossing branches used.
6. If repeated windows matter, construct a series episteme from exact result refs.
7. If a dashboard matters, represent those results under G.12.
8. If audience availability matters, establish E.24.PUB publication separately.

### C.21:8 - Bias-Annotation

C.21 counters dashboard, standard-status, popularity, and pseudo-precision bias. A public standard can have little adoption; a widespread practice can lack formal recognition; a dense relation map can preserve important losses; and a polished dashboard can represent weak or stale claims. The progressive path keeps the remedy proportional.

### C.21:9 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-C.21-1` | The discipline, intended use, one exact Characteristic, Scale, ClaimScope, comparison or observation basis, and time stance are recoverable. |
| `CC-C.21-2` | `ClaimScope` is authoritative. A `TargetSliceRef` appears only when consumed and its exact relation to the scope is stated. |
| `CC-C.21-3` | A minimal readable claim may stop without a definition set, EvidenceGraph, registry, dashboard, or publication apparatus. |
| `CC-C.21-4` | Every persisted, compared, aggregated, or published coordinate carries the active DHC replay basis; no generic “metric edition” substitutes for an exact object. |
| `CC-C.21-5` | Characteristic, Scale, Unit, polarity or target rule, and legal operations are coherent. Ordinals are not averaged and Units are not mixed. |
| `CC-C.21-6` | Direct comparison uses C.16's compatible-semantics branch. A comparison that relies on a cross-local semantic relation keeps the obtaining F.9 relation, its separate bounded-use claim, observed loss, and current reliance distinct as specified in section 4.2. |
| `CC-C.21-7` | Formal recognition and actual adoption or convergence are separate Characteristics; neither rank proves health or SoTA. |
| `CC-C.21-8` | EvidenceUnitResolution, ClaimsPerArtifact, and SupportAnchorsPerClaim are separate; their constructions and Units are not interchanged. |
| `CC-C.21-9` | Entropy and concentration are separate, with opposite directions explicit; any transformation and receiving Scale are declared. |
| `CC-C.21-10` | Measurement definition, exact Method, MethodDescription, model, calibration, Work, result, result episteme, series episteme, dashboard representation, publication occurrence, form, and carrier remain distinct where present. |
| `CC-C.21-11` | Freshness, evidence reliance, assurance, acceptance, public naming, and refresh machinery appear only when a named receiver consumes them. |
| `CC-C.21-12` | Unknown inputs remain unknown under the receiving method; missing inputs are not coerced to zero or to a health verdict. |
| `CC-C.21-13` | Engineering-grade extension readings cite the direct pattern and rule and do not become evidence, assurance, gate, release, Work, or project authority. |

### C.21:10 - Common Anti-Patterns and How to Avoid Them

* Treating discipline health as one scalar before separately typed coordinates exist.
* Treating `ClaimScope` and `TargetSlice` as two spellings for one object.
* Requiring a Bridge merely because sources, schemes, or editions differ.
* Comparing distinct local senses without the exact obtaining F.9 relation and loss.
* Ordering formal status and adoption on one universal maturity ladder.
* Calling `claims/artifact` and `anchors/claim` alternative Units of one Characteristic.
* Writing `<entropy/HHI>` as if either formula produced the same reading.
* Treating a definition set, method description, Work record, series, dashboard row, or publication carrier as the measurement result.
* Requiring publication and assurance machinery before one useful health claim exists.

### C.21:11 - Consequences

**Benefits.** Field-health claims remain readable, scale-admissible, comparable when justified, and reusable without turning a dashboard or standard into authority.

**Costs.** A numerical or reused claim must expose its definition and comparison basis. A cross-local comparison must additionally expose the exact relation and loss.

**Risks avoided.** False maturity ladders, hidden polarity reversal, scope substitution, Bridge inflation, stale trends, publication-as-result, and assurance-by-record are blocked.

### C.21:12 - Rationale

Discipline health is not one thing. Reproducibility, formal recognition, adoption, alignment, disruption, evidence resolution, and diversity answer different questions and can move independently. Their definitions, measurement results, series, representations, and publications also change for different reasons. Keeping those distinctions explicit makes the result both more precise and easier to use.

### C.21:12.1 - SoTA-Echoing

| SoTA or practice anchor | Contribution used here | Non-overread |
| --- | --- | --- |
| Open Science Collaboration (2015), Munafò et al. (2017), and current reproducibility and metascience practice | Reproducibility, claim resolution, support visibility, freshness, and population definition remain separate coordinates and bases. | A field-level rate does not certify one claim as true. |
| Fortunato et al. (2018) and Wu, Wang, and Evans (2019) disruption-index work | Disruption and consolidation are read through a declared corpus, method edition, and target band rather than a monotone novelty target. | Disruption is not quality, truth, safety, or usefulness by itself. |
| Standards lifecycle and ecosystem-adoption practice | Formal recognition and observed adoption are separate. | Official status, popularity, and convergence do not prove one another or SoTA. |
| Plural-tradition and relation-mapping practice | AlignmentDensity counts exact obtaining directed relations with visible loss. | A relation count is not universal language, consensus, or authority. |
| Diversity measurement practice | Entropy and concentration retain their separate constructions and directions. | Similar labels do not make their Scales interchangeable. |

### C.21:13 - Relations

* **Builds on:** C.20 for the discipline, A.17-A.18 for Characteristic and Scale, C.16 for measurement and direct comparability, A.2.6 for ClaimScope and optional selected slices, and C.2.1 for result and series epistemes.
* **Coordinates with:** F.9 for actual cross-local sense relations; G.0 and A.19 for numerical operation, comparison, or aggregation; G.4 for target bands and acceptance; G.9 for parity; G.11 for currentness and refresh; G.12 for dashboard representations; A.10/G.6 and B.3 only for named evidence-reliance or assurance uses; E.24.PUB for publication availability.
* **Constrains:** G.5 and G.10 when they consume a DHC coordinate: they carry the same active DHC replay basis rather than a generic method-spec or metric-edition pin.

### C.21:14 - Practitioner Quick Template

```text
Minimal DHC claim
  Discipline: <exact discipline>
  Intended use: <question or action>
  ClaimScope: <where the claim holds>
  Characteristic and Scale: <exact definitions>
  Comparison or observation basis: <population/corpus/cohort/window>
  Ordinary result: <what is supported; what is not>

Only if measurement, comparison, or aggregation is current
  DHC replay basis: <active exact refs and editions from C.21:4.0a>
  TargetSlice: <optional; only if consumed, with relation to ClaimScope>
  Comparison branch: <direct compatible semantics | exact F.9 relation + separate use/direction/rule/tolerance claim + loss evidence + current reliance>
  Legal operation or target-distance rule: <exact ref>

Only if a reusable series, dashboard, or publication is current
  Series episteme: <exact coordinate-result refs and windows>
  Dashboard representation: <optional G.12 row/slice refs>
  Publication: <optional E.24.PUB relation, audience, bounded use, form, carrier, interval>
```

### C.21:End

