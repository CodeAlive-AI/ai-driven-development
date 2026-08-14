## C.21 - Field Health & Structure (Discipline-CHR)
> **Status:** Stable
> **Type:** Pattern

> *Purpose.* Give FPF a **typed, reviewable** way to characterize the *health, maturity, and structure* of a scientific or engineering **discipline**, without collapsing into taste, anecdotes, dashboard views, audit labels, or single-number scores. The pattern defines a portable set of Characteristics and guards for scale admissibility, freshness, scope, and comparison; each use names the exact schemes, bases, and measurement editions it relies on.

*This pattern supplies the CHR vocabulary of health for disciplines. C.20 composes the discipline; C.21 declares discipline-health characteristics and admissible readings; Part G may publish SoTA palettes or time-series views. When a reading actually relates distinct F.17 local senses, F.9 keeps that relation and its loss explicit; assurance penalties touch **R** only.*

### C.21:0 - Use This When

Use this pattern when a team must characterize the health, maturity, or structure of a discipline without reducing the field to a dashboard score, popularity signal, or one preferred tradition. Typical cases include judging reproducibility, standards convergence, cross-tradition alignment, disruption balance, evidence granularity, or method-family diversity.

**What goes wrong if missed.** Field-health claims become attractive labels: ordinals get averaged, stale evidence looks current, local scope and comparison basis disappear, and values produced under different schemes or measurement editions are treated as comparable without an obtaining relation.

**What this buys.** Discipline health becomes a vector of typed characteristics with exact scheme and method editions, comparison basis, scale, unit, polarity, freshness, `ClaimScope`, and any actually consumed cross-local relation visible before comparison or publication.

**First useful move.** Name the discipline and practical question, choose one relevant characteristic, state the comparison basis and scope, and say in ordinary language what the current evidence supports and what it does not. Stop there when no numeric comparison, aggregation, or reusable publication is needed.

**Placement.** Part C (Kernel Extension Specifications) -> Cluster C.I (Core CHRs/CALs).
  **Depends on:** **MM-CHR** (C.16), **KD-CAL** (C.2), **USM/Scope** (A.2.6), **Trust & Assurance** (B.3), **E.10 (LEX‑BUNDLE)**.
  **Coordinates with:** **C.20 Discipline‑CAL** (what a `U.Discipline` is), **G.2** (SoTA palette), **G.12** (dashboard), **G.0** (CG‑Spec registry).

### C.21:1 - Problem Frame

FPF treats *disciplines* as first-class holons (see **C.20**): they aggregate epistemes, practices, standards, institutions, and observed Work. Teams routinely say “the field is fragmented,” “standards are converging,” or “replication is improving,” but these claims are rarely **typed** (scale/unit/polarity) or **replayable** (evidence lanes, freshness, scope). C.21 supplies the CHR vocabulary: named Characteristics with CSLC typing, so discipline-health claims can be compared admissibly (CG-Spec) and monitored through time (G.12) when a project needs that use. Each published value declares ReferencePlane ∈ {world|concept|episteme} and DisciplineId (U.Discipline@UTS); cross-plane use applies CL^plane in Assurance (penalty to R_eff only).

### C.21:2 - Problem

Narrative health claims cause three recurrent failure modes:

1. **Scale inadmissibility.** Averaging ordinals, mixing units, or comparing values produced under incompatible characteristic, scale, method, or distance editions yields nonsense roll-ups.
2. **Staleness.** Health “scores” rarely declare **freshness windows** or evidence lanes (TA/VA/LA).
3. **Scope and basis slippage.** “The field” and the comparison basis are left implicit; values from different corpora, traditions, cohorts, or schemes are treated as commensurable without an obtaining relation. Any numeric comparison or aggregation cites a **CG-Spec** row (characteristics, **ScaleComplianceProfile (SCP)**, **Γ-fold**, MinimalEvidence) and the exact input editions before computation.

### C.21:3 - Forces

| Force                            | Tension                                                                                                                    |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Comparability vs nuance** | Need wider pictures without erasing the exact schemes, corpora, traditions, cohorts, and local claims that make each reading meaningful. |
| **Ordinal vs interval/ratio**    | Powerful stats tempt inadmissible operations on ranks and categories.                                                                  |
| **Local evidence vs federation** | A reading is computed from a named evidence set and `ClaimScope`; federation requires an admitted comparison basis and any actually obtaining cross-local relation, with assurance penalties applied to **R** only. |
| **Recency vs stability**         | Health evolves; time-series or dashboard views need **freshness**, not just cumulative history.                           |

### C.21:4 - Solution — **Discipline Health Characterisation (DHC)**

#### C.21:4.0 - Ontology quick sheet (normative, clarifying)
**What “DHC” is.** DHC is a **CHR vocabulary pack** that defines **Characteristics** + **Scales/Units/Polarity** for discipline health; it is not a document or a run.
**Artifacts.**
• **`U.DHCPack`** (I-lane name; published as an episteme): the **slot set** of Characteristic and Scale declarations selected for a named discipline-health use under an exact effective `ReferenceScheme`.
• **`U.DHCMethodSpec`** (S-lane): the **computational specification(s)** for deriving each DHC slot (e.g., replication‑window definition, CD‑index class), table‑backed; multiple per slot allowed, editioned separately.
• **`U.DHCSeries`** (episteme with an `EditionSeries`): a **time-indexed publication** of computed DHC readings for one named discipline, `ClaimScope`, comparison basis, and intended use; each value is bound to `…Ref.edition` for every referenced characteristic, scale, method, metric, and distance.
**Edition subjects.**
(i) **DHCPack.edition** — when the **slot semantics** (Characteristic/Scale) change.
(ii) **DHCMethodSpecRef.edition** — when a **computation method** (formula/class/policy) changes.
(iii) **DHCSeries.edition** — when the **published series** changes its content (not carriers).
**Publication.** Releases are **Work** on Carriers; **no** edition change unless content changes per `U.EditionSeries`.
**Ref discipline.** All bindings to packs/methods/distances use `...Ref.edition` (dot on the Ref).

Define a **portable minimal set** of CHR **slots**. Each slot is CHR-typed (Characteristic, Scale, Unit, and Polarity per **A.17–A.18**) and each reading names its effective `ReferenceScheme`, `ClaimScope`, comparison basis, freshness window, evidence lanes, and exact characteristic, scale, method, metric, and distance editions that matter. A local extension is another declared slot; it does not alter an existing scale type in place.

**“Health” is a vector** of CHR‑typed coordinates; **no single scalar** is implied. Scale-admissible scalarization lives in **Acceptance** (G.4) under an explicit **CG‑Spec ScaleComplianceProfile (SCP)** and **Γ‑fold** rules, and is never embedded in CHR.

#### C.21:4.1 - Core Characteristics (kernel-portable names)

1. **ReproducibilityRate** *(ratio ∈ [0,1]; polarity ↑; ReferencePlane=episteme; CG‑Spec‑bound)*
   Fraction of tested claims or benchmarks that independent teams **replicate** for a named benchmark, corpus, cohort, protocol, and `ClaimScope` within a declared **Γ_time** window. **Lane tags:** LA (validation) with TA (typing) for protocols.

2. **StandardisationLevel** *(ordinal; polarity ↑; ReferencePlane=episteme)*
   {none, *emerging*, *de facto*, *de jure*}. **No mean.** Use medoid/mode; admissible comparisons are ≤/=/> only. Tracks convergence on vocabularies, interfaces, or procedures.

3. **AlignmentDensity** *(ratio; polarity ↑; ReferencePlane=episteme; CG‑Spec‑bound)*
   Density of obtaining **F.9 Substitution Bridges** with `CL≥2` between exact F.17 `SchemeSenseCell` values used by major `U.Tradition`s, per 100 cells in the declared comparison set. Free substitution is permitted at `CL=3`; at `CL=2`, substitute only with the stated extra guard. Units: `bridges_per_100_cells`. The reading names every cell set, Bridge relation, admitted use, and loss note; penalties affect **R_eff** only.

 4. **DisruptionBalance** *(interval; polarity = target band; ReferencePlane=episteme; CG‑Spec‑bound)*
  Relative share of **disruptive vs consolidating** works within **Γ_time** using a **registered CD‑index class** (editioned; cite **method id** in UTS). **Default plane:** *episteme*. Publish the **target band** via **Acceptance (G.4)**; not in CHR.

  5. **EvidenceGranularity** *(ordinal or ratio as declared by the selected characteristic and scale editions; polarity ↑; ReferencePlane=episteme)*
   If ratio: units = `claims_per_artifact` or `anchors_per_claim` (declare). If ordinal: publish level names and **ORD_COMPARE_ONLY**.
   Fineness of evidential units and declared envelopes (experiment cards, benchmark tasks, audit granules). Encourages *smaller, well-scoped* claims over monoliths.

  6. **MetaDiversity** *(portfolio dispersion; polarity ↑ to band; ReferencePlane=episteme; CG‑Spec‑bound)*
  Use entropy/HHI **over MethodFamily/Tradition shares** (method edition id in UTS); publish **guard‑band** as **Acceptance** binding; cross‑ordinal scalarisation is forbidden.
  Entropy- or Herfindahl-type dispersion across `U.Tradition`s, method families, or data regimes, bounded by the guard-band declared for this use under the selected policy edition (too low ⇒ monoculture; too high ⇒ incoherence).

> **Typing & admissibility.** Each slot declares **Scale/Unit/Polarity**; inadmissible operations (for example, means on ordinals or unit mixing) fail fast per **A.18/MM-CHR**.

#### C.21:4.1a - Engineering-grade and semio-substitution extension slots

A discipline-health use MAY add these DHC slots when its question asks either how recoverable the justification of an engineering claim is or how strongly representations are being mistaken for their subjects. Such questions arise, for example, in architecturing, optimization, prediction, comparison, assurance or decision input, first-principles justification, mathematical-lens use, and source-publication overread. These slots remain discipline-health characteristics. They do not become evidence relations, assurance relations, gate decisions, mathematical-lens use, measurement admissibility, release permission, or project authority.

7. **EngineeringClaimJustificationRecoverability** *(ordinal; polarity ↑; ReferencePlane=episteme|world by declared claim; CG-Spec-bound when aggregated)*
   Degree to which engineering-grade claims in the named discipline and `ClaimScope` expose the exact justification that carries their force for the intended use. That justification is the named construction, source, model, lens, or relation on which the claim relies. Examples include evidence, characteristic, assurance, gate, and method relations, as well as a stated heuristic triage boundary. When that force is live, the claim cites the pattern and exact rule that define or constrain the operative construction or relation (`A.10`, `B.3`, `A.15`, `A.20`, `A.21`, `C.16`, `C.29`, or another applicable pattern). Heuristic examples may carry recognition and triage only; prediction, comparison, optimization, falsification, assurance-input, decision-input, or architecture-readiness force requires the recoverable justification.

8. **SemioSubstitutionPressure** *(ordinal or ratio; polarity ↓ to band; ReferencePlane=episteme; CG-Spec-bound when aggregated)*
   Degree to which a discipline mistakes a representation or its apparent fluency for the engineering subject, relation, or claim it is meant to support. Representations include, for example, wording, publication forms, records, dashboards, views, and source chains. The displaced subject may be an entity, relation, Work occurrence, evidence or assurance claim, gate, decision, method, or mathematical-lens claim. Lower pressure is healthier when an EntityOfConcern remains distinct from epistemes about it and from their publications, sources, and carriers, and each current project-side claim or use boundary cites the pattern and rule that define or constrain it.

**Extension guard.** Activating either extension slot requires a local `EngineeringClaimJustification` note or semio-substitution note that names the current claim kind or admissible-use boundary, the pattern and rule that define or constrain it, admissible use, non-admissible overread, and stop or reopen condition. The note is a DHC value explanation, not a new evidence source, assurance case, gate, release record, or work authority.

#### C.21:4.2 - Guard Macros (normative)

* **ORD\_COMPARE\_ONLY(x)** — for **StandardisationLevel** (ordinal).
* **UNIT\_CHECK(x)** — forbid cross-unit aggregation (AlignmentDensity, ReproducibilityRate).
* **POLARITY_CHECK(x)** — enforce declared polarity (↑/↓/target-band) per MM‑CHR.
* **FRESHNESS(x; window)** — ensure values come from evidence within declared **Γ_time**; record **valid_until**; stale ⇒ {degrade|abstain} at Acceptance.
* **PLANE_NOTE(x)** — record **ReferencePlane**; compute **CL^plane** on crossings; penalties → **R_eff** only.
* **LANE\_TAGS(x; {TA|VA|LA})** — annotate contribution lanes.
* **SCOPE\_COVERS(x; TargetSlice)** — enforce **USM** coverage of the computation.
* **CROSS_LOCAL_RELATION(x; relation, admittedUse)** — when a roll-up actually relates distinct F.17 cells, require the exact F.9 relation, its CL, admitted use, and loss notes; penalties affect **R** only. If ReferencePlanes differ, also apply the exact plane relation and cited policy. For **AlignmentDensity**, count only obtaining relations in the declared comparison set; `CL=3` counts as free substitution and `CL=2` requires the stated extra guard.

#### C.21:4.3 - Legality Matrix (extract)

| Operation     | ReproducibilityRate (ratio) | StandardisationLevel (ordinal) | AlignmentDensity (ratio) | DisruptionBalance (interval) |
| ------------- | --------------------------: | -----------------------------: | -----------------------: | ---------------------------: |
| mean          |                      **OK** |                     **FORBID** |                   **OK** |                       **OK** |
| median        |                          OK |                         **OK** |                       OK |                           OK |
| compare (<,>) |                          OK |                         **OK** |                       OK |                           OK |
| unit mix      |                  **FORBID** |                            n/a |               **FORBID** |                          n/a |

*Note:* For **MetaDiversity/EvidenceGranularity (ordinal)** use **median/mode**; forbid affine ops; unit mix always fails.

### C.21:5 - DHC Inputs, Outputs, and Comparison Use

* **Inputs.** One `U.Discipline` from **C.20**; the intended use and `ClaimScope`; exact characteristic, scale, method, metric, and distance editions; named corpora, benchmarks, traditions, cohorts, or other comparison basis; freshness window; and exact evidence. A G.2 SoTA Palette or BridgeMatrix is an input only when this reading actually consumes it.
* **Outputs.** DHC coordinate claims for the named discipline, scope, basis, and intended use; when useful, an editioned series publication and F.18 names for already constituted results. Method-edition changes carry the applicable refresh hooks and may feed **G.12** time-series views.
* **Comparison and cross-local use.** Values are comparable only under an admitted comparison basis and compatible declared editions. When the comparison actually relates distinct F.17 cells, cite the obtaining F.9 relation, its CL, admitted use, and loss notes; assurance penalties apply to **R** only. Different sources or editions alone do not create a Bridge.

### C.21:6 - Archetypal Grounding (three fields)

#### C.21:6.1 - Computer Vision (Benchmarks 2015→)
* **ReproducibilityRate.** Ratio of independently reproduced results on ImageNet-style tasks within **rolling 24 mo** (LA lane).
* **StandardisationLevel.** *de facto* for dataset specs and metrics in *Vision\_2024*; *emerging* for robustness protocols.
* **DisruptionBalance.** Use an editioned CD‑index class (e.g., Wu‑style disruption family) with method id; publish target band via Acceptance; annotate ReferencePlane=episteme.
* **AlignmentDensity.** Bridges with **CL≥2** across sub-traditions (supervised vs self-supervised).
* **MetaDiversity.** Entropy across method families (CNN/ViT/Hybrid) kept within guard-band to avoid monoculture.

#### C.21:6.2 - Biomedicine (Gene–Disease Associations)
* **ReproducibilityRate.** Fraction of associations replicated in independent cohorts within **Γ\_time(36 mo)**; LA lane with TA (typing of protocols).
* **StandardisationLevel.** *de jure* for certain reporting guidelines; *emerging* for pre-registration norms.
* **EvidenceGranularity.** Move from “paper-level” to *claim-level* units when the selected characteristic and scale editions assign the higher reading to finer evidential units.
* **DisruptionBalance.** Target band discourages sustained “novelty spikes” unbacked by replication.

#### C.21:6.3 - Software Performance Engineering (SPE)
* **StandardisationLevel.** *emerging* → *de facto* for SLO taxonomies and trace schemas across vendors.
* **AlignmentDensity.** CL-rated Bridges between tracing ecosystems.
* **ReproducibilityRate.** Share of publicly replicable perf claims in rolling windows.
* **MetaDiversity.** Balance across load models, failure modes, and toolchains.

#### C.21:6.4 - Decision‑Making (2015→)
• ReproducibilityRate — share of causal effect estimates replicated across independent datasets within Γ_time; LA lane.
• StandardisationLevel — *emerging* for identification checklists; *de facto* for SCM notation in leading stacks (ordinal; no means).
• AlignmentDensity — obtaining F.9 relations between exact F.17 cells from structural-causal-modeling or DoWhy sources and cells from reinforcement-learning or Bayesian-optimization sources, per 100 cells in the declared comparison set.
• MetaDiversity — dispersion across method families (SCM/RL/BO/DT) within guard‑band; entropy/HHI (units declared in CG‑Spec).

#### C.21:6.5 - Evolutionary Architecture (software)
• ReproducibilityRate — fraction of architecture fitness results reproduced on independent workloads (rolling 18–24 mo; LA lane).
• StandardisationLevel — *de facto* for ADR/ATAM patterns; *emerging* for continuous fitness protocols.
• AlignmentDensity — obtaining F.9 relations among exact ATAM, SAAM, and ADR local-sense cells per 100 cells in the declared comparison set, with `CL≥2` and the admitted-use limits stated.
• MetaDiversity — portfolio dispersion across patterns (microservices, event‑driven, layered) with guard‑bands; no ordinal arithmetic.

### C.21:7 - Characteristic Reading and Publication Use

1. **Declare the reading.** Name the discipline, intended use, `ClaimScope`, comparison basis, freshness window, and exact characteristic, scale, method, metric, and distance editions.
2. **Collect evidence.** Bind sources via **G.6 EvidenceGraph**; tag lanes and freshness.
3. **Compute DHC slots.** Enforce **Legality Matrix** and Guard Macros.
4. **State a cross-local relation only if needed.** When the reading actually relates distinct F.17 cells, cite the exact F.9 relation, CL, admitted use, and loss notes; apply any assurance penalty to **R** only.
5. **Publish to UTS.** Name Cards (Tech/Plain), twin labels; **bind `DHCMethodSpecRef.edition`**, `DistanceDefRef.edition`, and, where templates are used, `DHCMethodRef.edition`; register RSCR triggers (method change, ScoringMethod/NormalizationMethod edits).
6. **Publication view.** Feed G.12 with time-series and guard-bands (disruption, diversity) when a dashboard or trend publication is live.

### C.21:8 - Bias-Annotation (E-cluster lenses)

* **Didactic.** Plain names + twin labels; one-screen tables for managers.
* **Architectural.** No ordinals are averaged; every comparison names its basis and exact editions, and any actually consumed cross-local relation is explicit; assurance penalties never touch either `F` or `G`.
* **Pragmatic.** Freshness-aware; unknowns tri-state; values are decision-input cues, not trophies.
* **Epistemic.** Evidence lanes explicit; reproducibility is LA, typing is TA; validation distinct from dashboard or report publication.

### C.21:9 - Conformance Checklist

This checklist verifies a DHC reading after the practitioner has selected the live discipline-health question. It is not an audit form and not a dashboard specification.

| Check | Passing reading | Boundary preserved |
| --- | --- | --- |
| **CC-C.21-1 CHR typing.** | Every DHC slot declares Characteristic, Scale/Unit, and Polarity, with CSLC admissibility visible before aggregation. | Prevents health labels from becoming untyped opinion. |
| **CC-C.21-2 Freshness.** | Published values carry a `Γ_time` selector and freshness window; stale rows produce `{degrade|abstain}` in G.4 Acceptance. | Prevents stale cumulative history from masquerading as current health. |
| **CC-C.21-3 Plane.** | `ReferencePlane` is declared; cross-plane reuse publishes `CL^plane` policy id alongside CL, with penalties applied to `R_eff`. | Keeps world, concept, and episteme readings distinct. |
| **CC-C.21-4 Design/run tag.** | Each DHC row declares `DesignRunTag ∈ {design, run}` and does not mix design- and run-characteristics in one value or aggregate. | Prevents design claims and run observations from collapsing. |
| **CC-C.21-5 Lane tags.** | Each value tags TA/VA/LA lanes of contributing evidence. | Keeps typing, validation, and live-assurance lanes visible. |
| **CC-C.21-6 Ordinal discipline.** | `StandardisationLevel` remains ordinal: comparisons only, no means or z-scores. | Blocks pseudo-quantification. |
| **CC-C.21-7 Scope.** | All computations declare `TargetSlice`; USM membership is decidable for the declared use. | Prevents free-floating field-health claims. |
| **CC-C.21-8 Cross-local relations.** | A comparison or publication that actually relates distinct F.17 cells cites the exact F.9 relation, CL, admitted use, and loss notes; penalties apply to `R_eff`, never to `F` or `G`. | Keeps local meaning loss visible without inventing a Bridge for every source difference. |
| **CC-C.21-9 UTS.** | DHC rows are publishable as UTS Name Cards with Tech/Plain twin labels. | Keeps each name tied to its governed value and named scheme. |
| **CC-C.21-10 Registry.** | DHC methods are table-backed; method changes bump `DHCMethodSpecRef.edition` and trigger RSCR. | Prevents silent method drift. |
| **CC-C.21-11 Unknowns.** | Unknown inputs propagate tri-state `{pass|degrade|abstain}` to Acceptance; `unknown -> 0` coercion is excluded. | Preserves honest uncertainty. |
| **CC-C.21-12 Lexical firewall.** | Core narrative follows E.5.1 and does not use tool/vendor tokens as discipline-health kinds. | Prevents vendor or tool labels from becoming characteristics. |
| **CC-C.21-13 CG-Spec citation.** | Numeric comparison or aggregation in DHC cites CG-Spec: characteristics, `ScaleComplianceProfile`, `Γ-fold`, and MinimalEvidence. | Keeps operations scale-admissible. |
| **CC-C.21-14 Phi policies.** | `Phi(CL)` and `Phi_plane` are monotone, table-backed, and published by policy id. | Prevents hidden penalty functions. |
| **CC-C.21-15 Ref discipline.** | Edition pinning appears as `...Ref.edition` on the relevant reference field; bare `...Edition` fields are repaired. | Keeps edition subject explicit. |
| **CC-C.21-16 System-role kit, informative.** | Local system-role kinds described under F.4 may be used: `DisciplineStewardSystemRole`, `DHCMethodAuthorSystemRole`, `DHCSeriesPublisherSystemRole`; values still declare design and run stance and `ReferencePlane`. | A system-role kind or assignment does not become evidence or authority. |
| **CC-C.21-17 Engineering-grade and semio-substitution extensions.** | When `EngineeringClaimJustificationRecoverability` or `SemioSubstitutionPressure` is active, the DHC row names the current engineering claim kind, admissible-use boundary, or semio-substitution repair and cites the pattern and rule that define or constrain it. It also states admissible use, non-admissible overread, and the stop or reopen condition. | The extension note is not evidence, assurance, gate passage, mathematical-lens use, release permission, work authority, or project certification. |

### C.21:10 - Common Anti-Patterns and How to Avoid Them

* Treating discipline health as one scalar score before the typed characteristic vector is declared.
* Averaging ordinal characteristics or mixing units because a dashboard wants one roll-up.
* Reusing a discipline-health value outside its intended use, `ClaimScope`, comparison basis, freshness window, or declared edition alignment.
* Treating a standard, source publication, or dashboard view as proof that the discipline is healthy.
* Using engineering-grade or semio-substitution extension slots as evidence, assurance, gate passage, or project authority.

### C.21:11 - Consequences

**Benefits.** Scale-admissible comparisons; freshness-aware governance; explicit cross-tradition alignment; dashboard views that do not lie by averaging ranks.
**Costs.** Some ceremony (scales, windows, lanes, bridges), offset by template macros and UTS automation.
**Risks avoided.** “Phlogiston disciplines” (charisma-driven fields) surface as unhealthy in DHC readings; **No-Free-Lunch** preserved by G.5 (selector returns sets, not universal scalars).

### C.21:12 - Rationale

C.21 reads discipline health through typed characteristics rather than one global health score. This keeps reproducibility, freshness, disruption, standardization, bridge density, engineering-claim recoverability, and semio-substitution pressure inspectable without turning any dashboard or source tradition into authority by itself.

### C.21:12.1 - SoTA-Echoing

| SoTA/practice anchor | What it changes in C.21 | Adoption stance | Boundary of non-overread |
|---|---|---|---|
| Open Science Collaboration (2015), Munafò et al. (2017), and current reproducibility and metascience practice on replication, transparency, claim granularity, and freshness. | `ReproducibilityRate`, `EvidenceGranularity`, freshness windows, and evidence-lane tagging are live discipline-health characteristics rather than one global credibility score. | Adopt and adapt: use reproducibility as one typed characteristic with scope, window, and evidence lanes. | C.21 does not certify any single claim as true; claim evidence uses `A.10`, `G.6`, or another pattern that defines or constrains the evidence relation being asserted. |
| Fortunato et al. (2018) science-of-science framing and Wu, Wang, and Evans (2019) disruption-index family. | `DisruptionBalance` is a banded characteristic, not a monotone novelty target; the method id and edition are declared before use. | Adapt: use disruption/consolidation as a typed reading over a declared corpus and method edition. | Disruption is not quality, truth, safety, or project usefulness by itself. |
| Standards and ecosystem-convergence practice in engineering disciplines. | `StandardisationLevel` stays ordinal with comparison-only operations, and every comparison names the exact schemes and standard-status editions it uses. | Adopt lightly: use standardization as an ordinal characteristic and preserve local meanings. | Standard status is not SoTA proof, evidence sufficiency, gate passage, or assurance. |
| Current plural-tradition and relation-mapping practice in mature fields. | `AlignmentDensity` counts obtaining F.9 relations per exact declared set of F.17 cells; it rewards recoverable substitutions without semantic collapse. | Adopt: name exact cells, relations, admitted uses, and loss notes, and keep penalties in `R` or `R_eff` only. | A high relation count is not a universal language, consensus, or authority claim. |
| Engineering architecture and semio-bias control practice from the current FPF architecture workstream. | Adds `EngineeringClaimJustificationRecoverability` and `SemioSubstitutionPressure` as discipline-health extension slots. | Adopt for FPF-facing engineering disciplines: evaluate whether engineering claim kinds, admissible-use boundaries, and semio-substitution repairs remain recoverable and cite the patterns and rules that define or constrain them. | These slots do not replace mathematical-lens use, evidence, assurance, gate, release, work, or project certification patterns. |

The practical consequence is that C.21 reads discipline health through typed characteristics. It can feed dashboards or time-series publications, but the dashboard is only a publication view over DHC readings; it is not the discipline-health ontology and not project authority.

### C.21:13 - Relations

* **Builds on:** **A.17–A.18** (Characteristic/CSLC), **A.2.6** (USM scopes), **B.3** (assurance lanes), **C.16** (MM-CHR templates).
* **Coordinates with:** **C.20** (what a `U.Discipline` *is*), **G.2** (SoTA palettes and relation matrices), **G.12** (dashboard publication), and **G.9** (parity harness for fair comparisons). **Constrains:** **G.10** (pack ships DHC rows plus method ids), **G.11** (refresh windows and decay), and **G.5** (selector may reference DHC only via admissible predicates; no cross-ordinal scalarisation). **Coordinates with F.9** only when a comparison actually consumes a relation between distinct F.17 cells.

### C.21:14 - Annex - Practitioner Quick Template

```
C.21.DHC(Discipline: <id>; IntendedUse: <use>; ClaimScope: <scope>; EffectiveReferenceScheme: <scheme-id-and-edition>; ComparisonBasis: <declared-comparison-set>; Γ_time: <policy>)
  ReproducibilityRate:
    value: <0..1>   lane: LA   window: <…>   scope: <…>
  StandardisationLevel:
    value: {none|emerging|de_facto|de_jure}   compare_only: true
  AlignmentDensity:
    value: <ratio>   units: bridges_per_100_cells   cell_set: <exact F.17 refs>   relation_refs: <exact F.9 refs>   CL_min: 2   scope: <…>
  DisruptionBalance:
    value: <−1..1>   method: <CD-index class / edition>   target_band: [l,u]
  EvidenceGranularity:
    value: <ordinal|ratio per selected scale edition>   notes: <…>
  MetaDiversity:
    value: <entropy/HHI>   target_band: [l,u]
Guards: ORD_COMPARE_ONLY(StandardisationLevel), UNIT_CHECK(*), FRESHNESS(*), LANE_TAGS, SCOPE_COVERS, CROSS_LOCAL_RELATION(if distinct F.17 cells are related)
Publish: UTS twin labels; RSCR triggers on method edition change.
```

### C.21:End

