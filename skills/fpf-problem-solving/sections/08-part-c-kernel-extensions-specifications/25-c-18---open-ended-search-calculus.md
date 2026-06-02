## C.18 - Open‑Ended Search Calculus (NQD‑CAL)

**Status.** Calculus specification (**CAL**). Exports `Γ_nqd.*` operators for open‑ended, illumination‑style generation. **ΔKernel = 0** (no kernel primitives added). *Minting note:* this CAL **does not mint** new U‑types; it defines **CAL‑records** that MAY alias to registered U‑types where present via **E.10/UTS**.

**Depends on.** A‑kernel (A.1–A.15), **MM‑CHR** (C.16) for measurements, **KD‑CAL** for similarity/corpora, **Sys‑CAL** for carriers, **Decsn‑CAL** (objectives; advisory), **Compose‑CAL** (set aggregation; advisory).

**Coordinates with.** **B.5.2.1** (binding), **C.17 Creativity‑CHR** (characteristics & scales), **C.19 E/E‑LOG** (policies: emitter selection, explore/exploit).

**Exports (CAL; no U‑type minting here).**
 - Records: `NQD.DescriptorMap` (alias of `U.DescriptorMap` if minted), `NQD.NQDArchive` (alias of `U.NQDArchive`), `NQD.Niche`, `NQD.ArchiveCell`, `NQD.EmissionSeed?`, `U.EmitterPolicyRef`, `U.InsertionPolicyRef`, `U.IlluminationSummary`, and `NQD.CandidateSet` (alias of `Set<U.Hypothesis>`).

### C.18:1 - Problem frame
Open‑ended search (NQD) equips FPF with illumination‑style generation and Pareto / selected-set selection in multi‑criteria, partially ordered spaces; it feeds G.5 without scalarising ordinal or mixed‑scale characteristics.

### C.18:2 - Problem
Without a disciplined NQD calculus, contexts (a) conflate illumination telemetry with dominance, (b) lose reproducibility due to undeclared DescriptorMap/DistanceDefRef.editions, and (c) perform illegal aggregations across scales.

### C.18:3 - Forces
• Posets vs. scalarisation — selectors must return sets (Pareto/archive) rather than illegal weighted sums across mixed scales.
• Exploration vs. exploitation — emitters must adapt while preserving provenance and editioning.
• Telemetry metric vs. objective — Illumination (coverage/QD‑score) informs health but is not a dominance characteristic by default.
• Reproducibility vs. adaptivity — budgets, ε, K, and InsertionPolicy must be edition‑tracked.

### C.18:4 - Solution
Provide Γ_nqd.* operators and U.Types for DescriptorMap, Archive/Niche, policies, and illumination telemetry summaries; bind measurement legality to MM‑CHR and policy control to E/E‑LOG. (Exports/Type notes/Operator specs below are normative parts of this Solution.)

- Operators (Γ):
  - `Γ_nqd.generate(seed?, EmitterPolicyRef, Budget, DescriptorMapRef, QualityMeasuresRef, NoveltyMetricRef, CoverageGrid, CellCapacity K=1, EpsilonDominance ε=0, DedupThreshold?, InsertionPolicyRef?) → CandidateSet<U.Hypothesis>`
  - `Γ_nqd.updateArchive(Archive, CandidateSet, InsertionPolicyRef?) → Archive'`
  - `Γ_nqd.illuminate(Archive) → IlluminationSummary{coverage, QD-score, occupancyEntropy, filledCells}` (report‑only telemetry summary; not a dominance characteristic unless a policy explicitly promotes it).
  - `Γ_nqd.selectFront(Archive|CandidateSet, characteristics={Q components, Novelty@context, ΔDiversity_P, …}) → ParetoFront`

**Type notes.**
- `U.DescriptorMap (Tech; twin‑labelled Plain) : Hypothesis → ℝ^d` (declares encoder, invariances, version, **CharacteristicSpaceRef**). Publish Tech/Plain per **E.10**; declare `DescriptorMapRef.edition` and `DistanceDefRef.edition`. **Dimensionality rule.** **Require `d≥2` only when QD/illumination surfaces are active**; for non‑QD contexts `d≥1` is lawful.
- `NQD.CandidateSet` ≡ `Set<U.Hypothesis>` with attached per‑item vectors `{Q_i, N_i, D_i:=ΔDiversity_P, S_i?, provenance_i}`.
- `U.NQDArchive` holds per‑cell elites and genealogy refs; context‑local.
- `U.Niche` is a region in CharacteristicSpace (grid bucket / CVT centroid / cluster).
- `U.EmitterPolicyRef` points to a named policy in **C.19 E/E‑LOG**.
- `U.InsertionPolicyRef` — named archive‑update policy (e.g., `replace_if_better | replace_worst | bounded_age | bounded_regret`); versioned.
- `U.IlluminationSummary` is a **telemetry summary** over `Diversity_P` (see C.17), not a dominance characteristic.

**Operator specs (normative).**
- `Γ_nqd.generate(… )` SHALL:
  (a) respect **Budget**,
  (b) compute `{Q_i}` (vector), `N_i` (Novelty@context), `D_i := ΔDiversity_P(h_i | Pool)` under the same CharacteristicSpace & TimeWindow as the Pool, and optional `S_i` (Surprise),
  (c) deduplicate by `DedupThreshold` in CharacteristicSpace,
  (d) record `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `EmitterPolicyRef`, `ε`, `K`, `Seeds`, and genealogy references (parent/seed ids) to enable replay and selection auditing.
- `Γ_nqd.updateArchive` SHALL apply local competition per cell (keep up to K elites), preserve genealogy, and **enact the declared `InsertionPolicyRef`**; default is `replace_if_better` with deterministic tie‑breakers.
- `Γ_nqd.illuminate` SHALL return coverage and QD‑score computed against the declared grid and archive edition.
- `Γ_nqd.selectFront` SHALL compute the (ε‑)Pareto front over the declared characteristics; **Illumination** is excluded by default (report‑only).

**Pipeline:** apply **Eligibility (ConstraintFit=pass)** → **Dominance over the declared `DominanceSet`** → **Tie‑breakers (`Novelty@context`, `ΔDiversity_P`, `Surprise`; `Illumination` telemetry metric)**. When the context relies on the ordinary default, consume `DefaultId.DominanceRegime` from `G.Core/G.5` together with the active `C.19` emitter/archive policy instead of restating one local dominance doctrine here.
**Ordinary default Q-front mode:** When no narrower promotion policy is declared, dominance stays on the context-declared `Q` components while `N/ΔD` work through archive occupancy and tie-breakers. Any deviation SHALL be declared by policy id and recorded in provenance.

**Reproducibility & editions.** Each call SHALL emit provenance sufficient for replay: `{DHCMethodRef.edition, DescriptorMapRef.edition, EmitterPolicyRef (params), **InsertionPolicyRef**, DedupThreshold?, ε, K, Seeds, TimeWindow}`.
Telemetry hook: whenever IlluminationSummary increases (Δcoverage>0 or ΔQD‑score>0), the Context SHALL emit a Telemetry(PathSlice) record that cites {EmitterPolicyRef, DescriptorMapRef.edition, DistanceDefRef.edition, InsertionPolicyRef?, TimeWindow}. (Aligns with G.6/G.7/G.11 `PortfolioMode`/edition constraints.)

**Measurement alignment.** `Novelty@context`, `Use‑Value (ValueGain)`, `Surprise`, `Diversity_P` SHALL be measured per **C.17** (MM‑CHR templates). **IlluminationSummary** is a telemetry summary over `Diversity_P` (coverage/QD‑score); when CharacteristicSpace includes domain‑family cells, publish grid id and FamilyCoverage, plus **DescriptorMapRef.edition/DistanceDefRef.edition**.
.

#### C.18:4.1 - Front and archive are different returns

- Start from one declared `EligibilitySet`.
- Return the non-dominated `Front` over the declared `DominanceSet`.
- When archive mode is active, return the corresponding `ExplorationArchive` separately.
- Archive membership may use novelty, diversity, stepping-stone potential, or coverage policy and is not by itself evidence of membership in the current `Q-Front`.
- Keep `TieBreakerSet` and `TelemetrySet` explicit so diversity or illumination signals do not silently rewrite the front semantics.
- Use `RetentionIntent=steppingStone` when the point of retention is frontier expansion rather than current dominance.
- Here `EligibilitySet`, `DominanceSet`, `TieBreakerSet`, and `TelemetrySet` are comparison-bundle sets, while `RetentionIntent=steppingStone` is one archive-retention field value; none of them renames the returned `Front` or `ExplorationArchive`.
- If one line keeps both returns, say that the front answers current non-domination while the archive answers retained exploration value.
- When retained exploration value depends on future reachability or curriculum expansion across transitions, cite the declared reachability or transfer rule together with `LearningProgressSignal`, `CompetenceModelRef`, or `GoalSpaceExpansionCue`. That bridge stays archive/pool-policy-side unless one explicit policy promotes it; it does not require the heavier atlas layer and it does not rewrite front semantics.

### C.18:5 - Conformance Checklist
- **C18‑1** Declare `DescriptorMap` (encoder, invariances, corpus edition) before generation.
- **C18‑1b** When used in F/G triads, DescriptorMap SHALL declare a domain‑family coordinate (grid/cells) and reference an F1‑Card::DistanceDefRef & δ_family.
- **C18‑1c**  When a domain‑family coordinate is declared, the Context SHALL compute and publish **AliasRisk** for each front / declared set-result emission, together with the dSig collision rule and the policy id. AliasRisk is computed against `U.DomainDiversitySignature (dSig)`; **the DescriptorMap SHALL publish**: (i) `collisionRuleId` (near‑duplicate threshold, e.g. “≥3 characteristics equal”),  (ii) `dSigSource` pointers used for coding the five characteristics. The collision rule and formula **MUST** be part of `DescriptorMap` provenance (see **Creativity‑CHR**, Heterogeneity Characterisation).
- **C18‑2** Record `EmitterPolicyRef` (policy id from C.19) and parameter set.
- **C18‑3** Compute `D = ΔDiversity_P(h | Pool)` under the same DescriptorMap & TimeWindow as the Pool (see C.17).
- **C18‑4** Exclude Illumination from dominance unless policy explicitly promotes it.
- **C18‑5** Keep `Use‑Value` separate from assurance scores; do not alter `F/G/R` semantics (see B.3, C.17 §Use‑Value).
- **C18‑6** Emit full provenance; thinning after front computation MUST be recorded.
- **C18‑7** Before computing any front, apply **ConstraintFit = pass** as a hard eligibility filter.

**Defaults.** Default-governance responsibility is split on purpose: `G.Core` and `G.5` govern `DefaultId.DominanceRegime` and selector-facing default routing, while `C.19` governs emitter, insertion, and pool-policy defaults. `C.18` consumes those defaults and records the active refs instead of restating them locally. Minimum provenance remains: `DescriptorMapRef.edition` and `DistanceDefRef.edition`, `DHCMethodRef.edition`, `EmitterPolicyRef`, `InsertionPolicyRef`, `TimeWindow`, `Seeds`, `DedupThreshold?`; also record `FamilyCoverage/MinInterFamilyDistance`.

**Didactic quickstart (Context).**
1) Pick 2–4 Quality coordinates and a simple DescriptorMap (2–4 dims).
2) Set defaults: `K=1`, `ε=0`, a conservative `EmitterPolicy`.
3) Run `Γ_nqd.generate` to fixed Budget; inspect the front; log coverage (IlluminationSummary).
4) Apply abductive plausibility filters; promote prime hypothesis to L0.

### C.18:6 - Archetypal Grounding
**System.** Legged‑robot gait exploration: `Q = {forward speed, energy efficiency}`; `DescriptorMap/CharacteristicSpace = morphology/coordination descriptors (ℝ^d)`; `D = ΔDiversity_P(h | Pool)` computed over that declared descriptor space; `Archive = CVT grid`; illumination reports coverage without entering dominance.
**Episteme.** SoTA palette synthesis: `Q` is one declared objective tuple for the current synthesis task, for example external-validity gain, reuse value, or `Use-Value` only when the Context explicitly declares it inside `Q`; `DescriptorMap/CharacteristicSpace` carries method-family or claim-graph descriptors; `D = ΔDiversity_P(h | Pool)` is computed over that declared descriptor space or niche grid. Publish `DescriptorMapRef.edition` and `DistanceDefRef.edition` so the front remains reproducible.

### C.18:7 - Bias‑Annotation
Lexical firewall and notation independence apply; no vendor/tool tokens; ordinal characteristics never averaged; illumination treated as report‑only telemetry unless a policy promotes it. (E.5.1, E.5.2, C.16)

### C.18:8 - Consequences
• Selected-set honesty (no forced scalarisation). • Reproducibility (editioned maps/policies). • Healthy diversity signals via telemetry metrics.

### C.18:9 - Rationale
Post‑2015 Quality‑Diversity (MAP‑Elites & successors) demonstrates illumination efficacy; NQD‑CAL captures these ideas while preserving MM‑CHR legality and LOG governance.

### C.18:10 - Relations
Builds on: C.16, C.2. Coordinates with: B.5.2.1 (binding), C.17, C.19, G.5, G.6, G.11.

### C.18:End

---

