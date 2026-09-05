## C.23 - MethodFamily Evidence & Maturity (Method‑SoS‑LOG)

*LOG (logic) for deductive shells for admissibility*
*First use expansion:* **SoS‑LOG = Science‑of‑Science LOG** (LEX short‑form discipline applied).

**Registration boundary.** A `MethodFamily` is registered by one exact G.5 registry row and registry edition. That record names the family, its admitted A.3.1 Method members and grouping basis, and intended selector use. Establish evidence, claim scope, validity, and the decision result under their respective rules.

**Builds on.** **G.5** (MethodFamily registry/selector), **G.4** (Acceptance & EvidenceProfiles), **C.22** (TaskSignature S2), **C.18 NQD‑CAL** (QD/illumination), **C.19 E/E‑LOG** (emitters/policies), **B.3** (named assurance claims; `R_eff` under a declared policy), **A.10** (Evidence Graph Ref), **E.10** (LEX), **E.18** (GateCrossing / CrossingBundle visibility when a selected structural crossing is current). **Coordinates with.** **G.6** (EvidenceGraph), **G.8** (LOG bundling), **G.9** (Parity), **G.11** (Refresh).

### C.23:1 - Problem frame

Families of methods compete inside a CG‑Frame. The selector (G.5) must **admit, degrade, or abstain** per family **without** universal scores, using **typed** problem descriptors and **auditable** evidence. Maturity of a family (its evidence-backed rung for the declared admission use) must be **visible to LOG** rules yet **separate from acceptance thresholds** (which live only in **AcceptanceClauses**, G.4).

### C.23:2 - Problem

Unstructured “readiness” stories and undisciplined evidence lead to:

* (i) **Illicit scalarisation** across mixed scale types,
* (ii) **Prose‑only** gating that a dispatcher cannot execute,
* (iii) reuse after the family, evidence profile, claim scope, qualification window, or comparison basis changed, or reliance on an unstated source-local, kind, or plane relation, and
* (iv) Immature families leaking into production.
  We need a **notation‑independent LOG layer** whose **executable rules** use **TaskSignature (S2)** + **EvidenceProfiles** to return *admit / degrade / abstain*, **routing CL penalties selected under R4 to `R_eff` only** (never mutating **F/G**).

### C.23:3 - Forces

* **Pluralism vs. dispatchability.** Competing Traditions expose different invariants; selection must compare **without semantic flattening**.
* **Maturity vs. opportunity.** Open‑ended exploration (E/E‑LOG) must coexist with **run‑safe** exploitation; *immature ≠ forbidden* → provide safe **degrade** paths.
* **Unknowns (tri‑state).** Missing or `unknown` values in live S2 fields must propagate **explicitly** to *Degrade(mode)* (including *sandbox*) or *Abstain*; no silent coercions.
* **Lexical discipline.** Head‑anchoring, EntityOfConcern / Description / specification-use separation, Bridge hygiene; **no tool names in Core**.

### C.23:4 - Solution — **Method‑SoS‑LOG**: deductive shells over Eligibility & Evidence

#### C.23:4.1 - Objects & heads (LEX/I‑D‑S)

*Tech heads; Plain twins are published via UTS.*
**`MethodFamily`** (registered in G.5) carries **Eligibility** and artefact identity; **`MaturityCard`** (this pattern) carries evidence‑aware maturity; **`SoS‑LOG.Rule`** (this pattern) is an executable rule schema; evaluating a rule returns one of `{Admit | Degrade(mode) | Abstain}` for a `(TaskSignature, MethodFamily)` pair. A qualifying description episteme uses `…Description`; `…Spec` names that same episteme only after the E.10.D2 specification-use gate grants the named use.

#### C.23:4.2 - Rule schema (normative)

For each `MethodFamily` **f**, author an **executable** rule set:

```
LOG.Deduce_f(TaskSignature S2) → {Admit | Degrade(mode) | Abstain}
```

with the following **branch obligations**:

**R0 — CG-Spec gate (precondition).** For the exact G.5 registry row and `MethodFamily`, verify the cited `CG-Spec.MinimalEvidence` and EvidenceProfile for every CHR characteristic used by the family's acceptance clauses and flows, under the declared claim scope and selected slices, qualification window, and intended selector use. Failure ⇒ `Abstain` with reasons. Publish the consulted CG-Spec, EvidenceProfile, registry, and policy editions.
*Rationale:* selector legality requires the CG‑Spec gate to be explicit, not implicit in prose. Publish associated **ReferencePlane** notes alongside the consulted ids.

**R0.QD — QD/OEE pre‑gates (if applicable).** If S2 declares **CharacteristicSpaceRef/ArchiveConfig/EmitterPolicyRef** or `PortfolioMode=Archive`, verify:
(i) **CharacteristicSpaceRef** characteristics are CHR‑typed, d≥2, **ReferencePlane** per characteristic declared;
(ii) **ArchiveConfig** is lawful (topology, resolution, **K**>0, `InsertionPolicyRef`, `DistanceDef` with **edition id** and declared metric/pseudometric status);
(iii) **EmitterPolicyRef** present (with **edition id**);
 (iv) resolve **DominanceRegime**; if absent, use **default= ParetoOnly**.
 Failure of any ⇒ `Abstain` with reasons.

**R1 — Admit.** `Admit` **IFF**
(a) S2 satisfies **Eligibility** predicates of *f* (tri‑state aware),
(b) the exact **EvidenceProfile minima** referenced by Acceptance/Flows for *f* are met for the declared claim scope and selected slices, qualification window, and intended selector use (post R0),
(c) all relevant **CAL.AcceptanceClauses** (G.4) evaluate to true under lawful CHR comparisons,
(d) any **maturity gating** (e.g., a floor on Maturity rungs) is expressed as an **AcceptanceClause** and referenced here by id (no acceptance thresholds inside LOG).
*LOG never sets acceptance thresholds; its rules use and cite Acceptance verdicts.*

**R2 — Degrade.** If (a) holds but (b) or (c) is **partially** satisfied or **unknown**, return `Degrade(mode)` where `mode ∈ {scope-narrow | sandbox | probe-only}`. Record the exact S2 unknowns or evidence minima, narrowed claim scope or execution mode, qualification window, governing policy edition, and result. LOG-Degrade never changes CHR scales or planes.
**Note (CAL vs LOG).** CAL‑level **`degrade.order`** (fall‑back to order‑only comparisons) is governed by **G.4**/**CG‑Spec** and is **not** a LOG mode. **SoS‑LOG never overrides CAL outcomes**; a LOG branch **only narrows** `Scope(G)` or **execution mode** (e.g., `sandbox`, `probe‑only`), it **does not** alter CHR scales or admissible orders.
`probe‑only` MUST cite an **E/E‑LOG policy id** (exploration budget) and Acceptance‑bound guards.

**R3 — Abstain.** If S2 violates **Eligibility** or R0 fails, return `Abstain` with the failed rule, policy edition, evidence profile, claim scope, qualification window, and reasons. Abstain is mandatory for illegal CHR operations and when a conclusion depends on an F.9 Bridge, kind relation, or plane relation that has not been established.

**R4 — Relation and loss routing.** Cite an F.9 Bridge, kind relation, or plane relation only when the admission decision actually relies on that obtaining relation. Record its participants, direction, what meaning is preserved and what is lost, receiving use, and applicable policy edition. When the admission use makes a separate named assurance claim, identify its exact target claim and receiving use under B.3. Apply a supported loss penalty only under that assurance policy's declared rule; route it to `R_eff` only, leaving `F` and `G` unchanged. A changed registry row, evidence profile, claim scope, qualification window, or intended use is not by itself a crossing.

**R5 — Proof hooks.** Every branch **MUST** cite **Evidence Graph Ref** (A.10), the lane tags (TA/VA/LA) and freshness windows required by its cited CG-Spec.MinimalEvidence and EvidenceProfile, and **Bridge ids + loss notes** when the branch relies on a Bridge; the decision is **SCR‑visible**. When **G.6 EvidenceGraph** is present, also **publish EvidenceGraph path id(s)** for the branch (admit/degrade/abstain). **A branch verdict is not its own evidence basis**.

**R6 — QD archive / PortfolioMode semantics (if applicable).** If `PortfolioMode=Archive`, G.5 selection after `Admit` may return a **QD archive** (per `ArchiveConfig`) instead of only a Pareto set. Unless **CAL** authorises `DominanceRegime=ParetoPlusIllumination` (**policy‑id recorded in SCR**), **IlluminationSummary** is a **report‑only telemetry summary** and any **coverage/regret** are **telemetry metrics** (reported) that **do not** affect dominance.

**R7 — GeneratorFamily branches (open‑ended).** If S2 includes `GeneratorIntent`, SoS‑LOG **MUST**:
 (i) verify **`EnvironmentValidityRegion`** is declared and lawful;
 (ii) verify **`TransferRulesRef`** exists; if `unknown` ⇒ `Degrade(scope‑narrow)` or `Abstain` per family policy;
 (iii) treat the selection surface as **pairs `{environment, method}`**; publish **coverage/regret** and **IlluminationSummary** as **report‑only telemetry** (IlluminationSummary = telemetry summary; coverage/regret = telemetry metrics); dominance participation per **R6**.

**R8 — Telemetry & Refresh hooks.** On any illumination increase or archive change, publish the current editions and any actual **edition increments** for **CharacteristicSpaceRef**/**DistanceDefRef**/**EmitterPolicyRef** and the applicable **policy‑id** (Emitter/Acceptance); expose **PathSliceId** for refresh/decay in SCR only when an E.18 path slice is current.

> *Aphorism.* **“Admit on admissibility and sufficiency; degrade on uncertainty; abstain on inadmissibility.”**

#### C.23:4.3 - Maturity ladder (poset, not a scalar; Description, not Spec)

Publish one editioned **`MaturityCardDescription`** for the exact evaluated `MethodFamily`, G.5 registry edition, evidence profile, claim scope and selected slices, qualification window, and intended admission use (UTS enum ids; scale kind = ordinal; reference plane declared). Do not embed acceptance thresholds here; an admission floor remains a G.4 AcceptanceClause cited by R1.

* **L0 — Anecdotal.** Claims exist; lanes sparse; examples ad‑hoc.
* **L1 — Worked‑Examples.** Multiple **worked examples** with lane tags and **Scope slices** declared; *no replication yet*.
* **L2 — Replicated.** Independent replications identify their distinct bearers or operating conditions and declare the claim scope and selected slices, source and method editions, and qualification windows used; lane separation is observed and decay windows are explicit.
* **L3 — Benchmark‑Severe.** Repeated wins or parity on **community baselines** or **severe tests**; cross‑Tradition bridges declared with **loss notes**.

*Optional rung (for QD/OEE‑heavy families; ordinal, closed enum):*
* **L4 — QD‑Hardened.** Archive stability under declared **InsertionPolicy/DistanceDef** editions; reproducible **IlluminationSummary** improvements under controlled budgets; OEE generators pass **EnvironmentValidityRegion** severe tests.

**Norms.**
**M1.** The ladder is **lane‑aware** (TA/VA/LA) and **freshness‑aware**; it is **not** a global numeric score. Declare **Scale kind=ordinal** and the **closed enumeration** of rungs; register the enum at **UTS** (twin labels; editioned).
**M2.** Transitions **MUST** be justified by **EvidenceGraph** paths (once G.6 is available) and published at UTS; missing anchors ⇒ no advance.
**M3.** Any maturity floor used for admission—for example, a run-critical selector use requiring at least L2—MUST be authored as a CAL.AcceptanceClause and cited by R1 with its policy edition, claim scope, qualification window, and verdict; SoS-LOG does not embed acceptance thresholds.
**M4.** Declare the MaturityCard reference plane. If an admission decision relies on a relation to another plane, cite that exact obtaining plane relation, its direction and loss, and the applicable policy edition; a supported loss penalty selected under R4 affects `R_eff` only.

> *Rationale note.* Treating maturity as a **poset** aligns with B.3's requirement for lawful comparisons and avoids **scalarisation across ordinal/ratio** scales; assurance penalties selected under R4 affect **`R_eff`**, never **F/G**.

#### C.23:4.4 - Unknowns & Shift classes (tri‑state discipline)

**U1. (LEX).** Enumerations for `Degrade(mode)` and Maturity rungs **MUST** be declared as **closed value sets** and **registered at UTS** (twin labels). **Lexical SD** (**E.10**) applies.
**U2.** A live S2 characteristic or predicate admits `unknown` only when its C.22 value rule permits it; `unknown` **MUST** map to a branch (`Degrade` or `Abstain`) declared on the **family** (no coercions). Each branch publishes a **branch‑id** and (where used) a `mode` from a **closed enum** registered at **UTS** (LEX enum clarity).
**U3.** `ShiftClass` semantics follow **C.22**. If `ShiftClass ∈ {covariate‑shift, concept‑drift, adversarial}` or `unknown`, default outcome is `Degrade(scope‑narrow)` unless a CAL.AcceptanceClause explicitly guards the regime.

#### C.23:4.5 - Publication & wiring

**W1.** For each evaluated `MethodFamily`, publish an editioned `MaturityCardDescription` naming the registry edition, evidence profile, claim scope, qualification window, reference plane, and intended admission use; register the SoS-LOG rule ids. RSCR tests cover `Admit`, `Degrade`, `Abstain`, and unknown paths. Relation and loss-policy ids appear only where a branch actually relies on them.
**W2. Admissibility Ledger.** Publish an editioned `AdmissibilityLedger`: each selector-facing row names the exact `MethodFamilyId`, G.5 registry edition, RuleId and rule edition, MaturityRung, EvidenceProfile, claim scope, qualification window, BranchIds, AcceptanceClause and policy ids, decision result, evidence paths, DominanceRegime, PortfolioMode, and any obtaining relation and loss-policy ids actually used. UTS registers the row vocabulary; the ledger records the admission result and its basis.
**W3. Strategy composition.** For a selection composition called a strategy, cite its governing G.5 rule and **E/E-LOG** policy.
**W4.** Selector (G.5) **consumes** these rules; results appear in the **Dispatcher Report** with reasons in/out and cited anchors/bridges.

### C.23:5 - Archetypal Grounding (Tell–Show–Show)

*(Plain register for pedagogy; Core remains notation‑independent per E.10/E.8.)*

**Show‑1 - Continuous dynamics (ODE task).**
*S2 excerpt.* `DataShape=ODE; stiff?=unknown; Size≈10^3; Objective={↓error@ratio, ↑throughput@ratio}; Constraints={safety_gate@ordinal}; Jacobian_sparsity=high; Missingness=MAR`.
*Families.* `Implicit‑BDF` vs `Explicit‑RK` vs `Symplectic`.
*Rules.*
- `Implicit‑BDF`: **Eligibility** tolerates `stiff?=unknown` if `Jacobian_sparsity=high` (guarded precondition); **MaturityCard**=`L3` (replicated & benchmarked). Outcome: `Admit`.
- `Explicit‑RK`: requires `stiff?=false`; with `unknown` ⇒ `Degrade(sandbox)` (probe).
- `Symplectic`: eligible only when `Hamiltonian=true`; here ⇒ `Abstain`.
*Didactic anchor.* This mirrors C.22’s typed‑signature discipline and CHR legality (no ordinal means; unit alignment for **ratio**).

> The cited ecosystem examples of these families (post‑2015) are organised in **DifferentialEquations.jl**, which exposes multiple solver **families** under one call surface—precisely the pattern G.5 expects. ([Journal of Open Research Software][17])

**Show‑2 - Planning/scheduling (MIP task).**
*S2 excerpt.* `DataShape=MIP; NoiseModel=deterministic; Objective={↓cost@ratio, ↑service_level@ordinal}; Size≈10^5 vars; convex_relaxation=available`.
*Families.* `MILP (branch‑and‑bound)`, `Constraint‑Programming`, `Heuristic meta‑search`.
*Rules.*
- `MILP`: **Eligibility** requires `convex_relaxation=available`; the cited L3 MaturityCard edition names the registered family, evidence profile, benchmark basis, claim scope, qualification window, and intended selector use ⇒ `Admit`.
- `Constraint‑Programming`: **MaturityCard**=`L2`; Acceptance demands `service_level≥B` (ordinal predicate). With `B` met but baseline parity unknown ⇒ `Degrade(scope‑narrow)`.
- `Heuristic meta‑search`: **MaturityCard**=`L1` ⇒ `Degrade(sandbox)` or `Abstain` depending on RSCR parity policy.
*Didactic anchor.* Selector returns a **Pareto set** (no cross‑ordinal weighting), as required by G.5.

> The cited “single call / many solvers” packaging that motivates MethodFamily rows is exemplified by **JuMP** (2017–2022), which cleanly separates **model description** from solver choice. ([Miles Lubin][18])

- *DifferentialEquations.jl* illustrates **family‑based** solver packaging (multi‑method under one interface), 2017–2024 ecosystem. ([Journal of Open Research Software][17])
- *JuMP* illustrates **model/solver separation** and registry‑like selection (2021–2022 papers, site). ([Miles Lubin][18])
- *Science of Science* review (2018) supports the emphasis on replication/benchmarks in maturity assessment. ([Science][19])

**Show‑3 - QD archive (policy search).**
*S2 excerpt.* `PortfolioMode=Archive; CharacteristicSpaceRef(d=2); ArchiveConfig(CVT, res=1k cells, K=1, DistanceDefRef.edition=v2, InsertionPolicyRef=dyn‑elite); EmitterPolicyRef=v3; DominanceRegime=ParetoOnly`.
*Rules.* After `Admit`, G.5 returns an **archive**; illumination **reported**; changes to `DistanceDef`/Emitter **editioned** in SCR; dominance remains **ParetoOnly**.

**Show‑4 - Open‑ended GeneratorFamily (POET‑class).**
*S2 excerpt.* `GeneratorIntent{GeneratorFamilyRef=GF‑01, EnvironmentValidityRegion=EVR‑A, TransferRulesRef=TR‑A, CoverageMetric=…}; PortfolioMode=Archive`.
*Rules.* After `Admit`, G.5 returns declared sets over `{environment, method}`; `Degrade(scope‑narrow)` if `TransferRules`=`unknown`; telemetry publishes **coverage/regret** and **IlluminationSummary** with **edition/policy‑id** on improvements.

[17]: https://openresearchsoftware.metajnl.com/articles/10.5334/jors.151 "DifferentialEquations.jl – A Performant and Feature-Rich … "
[18]: https://mlubin.github.io/pdf/jump-sirev.pdf "JuMP: A Modeling Language for Mathematical Optimization"
[19]: https://www.science.org/doi/10.1126/science.aao0185 "Science of science"

### C.23:6 - Bias‑Annotation

**Principle‑taxonomy lenses.** *Universality* (trans‑discipline), *Didactic primacy* (Tell–Show–Show), *Open‑ended evolution* (refresh‑ready), *Lexical firewall* (no tool names in Core), *Notation independence*. Limits: Worked examples reference widely‑used ecosystems **in Plain register** only.

### C.23:7 - Conformance Checklist (normative)

| ID           | Requirement                                                                                                                                                                                | Purpose                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| **CC-C23.1** | For each `MethodFamily`, an editioned `MaturityCard` SHALL name the exact family and registry edition, evidence profile, claim scope, qualification window, intended use, rung justification, A.10 anchors, and freshness windows; cite a relation and loss note only when the admission claim actually relies on it. | Makes maturity auditable for the declared family and admission use. |
| **CC-C23.2** | The `AdmissibilityLedger` row for each evaluation of an executable `SoS-LOG` rule on S2 MUST cite the exact MethodFamilyId and registry edition, rule and policy editions, Eligibility and CG-Spec verdicts, EvidenceProfile minima, Acceptance verdict, claim scope, qualification window, Γ-fold contributors where used, decision result, and EvidenceGraph path. Relation and loss-policy ids appear only when the branch relies on them. | Keeps every decision premise reconstructable. |
| **CC‑C23.3** | Enumerations used by the rules (**Degrade(mode)**; Maturity rungs) **SHALL** be **closed** and **UTS‑registered** (twin labels). | |
| **CC‑C23.4** | **Unknowns** in live S2 fields **SHALL** map to `Degrade(mode)` (including `sandbox`) or `Abstain` with explicit **branch‑ids**; no `unknown→0/false` coercions.                                                          | Tri‑state discipline.                          |
| **CC-C23.5** | If a branch relies on an F.9 Bridge, kind relation, or plane relation, it MUST cite that exact obtaining relation, direction, what meaning is preserved and what is lost, receiving use, and applicable loss policy; supported penalties selected under R4 affect `R_eff` only. A changed family, evidence profile, claim scope, qualification window, or use is not by itself a crossing. | Keeps `F` and `G` invariant and relation claims truthful. |
| **CC‑C23.6** | **No acceptance thresholds** in CHR or Maturity; acceptance thresholds **live only** in **AcceptanceClauses** (G.4).                                                                                             | Separation of concerns.                       |
| **CC‑C23.7** | `MaturityCard` **SHALL NOT** be turned into a global scalar; treat as **poset**; any ordering **MUST** be lawful over CHR types.                                                           | Forbids cross‑scale scalarisation.            |
| **CC‑C23.8** | Publish to **UTS** with twin labels. Run **GateCrossing visibility checks** only for a cited crossing of a selected **E.18** transformation-flow structure. Require **CrossingBundle** attestation only when the named receiving use needs it; apply **E.18/F.9/F.17/E.17** under their respective current uses. Apply **LanePurity** and **Lexical SD** (**E.10**); use GateChecks/GateProfile (**A.21**) only when a named gate decision is current. | Publication & crossing visibility hygiene. |
| **CC‑C23.9** | All enumerations (e.g., `Degrade(mode)`, Maturity rungs) **SHALL** declare a **closed value set** and **Scale kind**, and be registered at UTS (LEX enum clarity).                          | Avoids lexical drift; lawful typing.          |
| **CC‑C23.10** | **RSCR tests** cover negative/refusal paths (illegal CHR ops; CG‑Spec gate fail; Bridge missing when relied on; **Φ table/policy‑id missing** when that penalty policy is used; **Lexical SD violations (E.10)**); ensure **branch coverage** (Admit/Degrade/Abstain, unknown). | |
| **CC‑C23.11** | If QD fields are in scope, **R0.QD** **MUST** pass: lawful **CharacteristicSpaceRef** (d≥2, characteristics typed, planes declared per characteristic), **ArchiveConfig** (topology/resolution/K, `InsertionPolicyRef`, **editioned** `DistanceDef`), **EmitterPolicyRef** present. | QD legality gate. |
| **CC‑C23.12** | **DominanceRegime** **SHALL** default to `ParetoOnly`; switching to `ParetoPlusIllumination` **MUST** be authorised by **CAL** and cited by id in SCR.                                    | Prevents implicit scalarisation.              |
| **CC‑C23.13** | If `PortfolioMode=Archive`, LOG **MUST** allow G.5 archive outputs after `Admit` (R6) and publish **IlluminationSummary** as a report-only telemetry summary unless CAL opts‑in to dominance participation.                         | Lawful archive semantics.                     |
| **CC‑C23.14** | If `GeneratorIntent` present, **R7** **MUST** verify **EnvironmentValidityRegion** and **TransferRulesRef**; G.5 outputs are declared **{environment, method}** sets; coverage/regret telemetry published. | OEE legality & telemetry. |
| **CC‑C23.15** | On illumination increases/archive changes, current editions and any actual **edition increments** (CharacteristicSpaceRef/DistanceDefRef/EmitterPolicyRef) and the applicable **policy‑id** **SHALL** be logged (R8).                   | Reproducibility & refresh.                    |

### C.23:8 - Consequences

* **Explainable admission.** Every *Admit/Degrade/Abstain* is backed by **anchored** evidence and explicit unknown handling (selector reports are SCR‑linked).
* **Run‑safe pluralism.** Multiple families can co‑exist with **policy‑governed** exploration (E/E‑LOG) and maturity‑aware gating.
* **Portable governance.** Bridge hygiene makes cross‑Tradition reuse **deliberate**; when a supported penalty is selected under R4, declared CL routing makes it **costed** through **`R_eff`** only.

### C.23:9 - Rationale

For a named admission-assurance claim, B.3 requires each of **F**, **G**, and **R** that the use consumes to have a declared bearer, meaning, and scale. Claim scope and selected USM slices remain explicit; **WLNK** and **Φ(CL)** are used only under an applicable, calibrated aggregation or loss rule. Treating maturity as **evidence‑typed rungs**—rather than a “score”—avoids illegal arithmetic and lets **DesignRunTag** values remain separate via `DesignRunTag` discipline (A.4), with explicit GateCrossings only when a selected E.18 transformation-flow structure contains them. This mirrors the cited 2018 **science‑of‑science** insights: replication, benchmarking, and field health indicators are the **currency** of maturity, not anecdote.  ([Science][19])

### C.23:10 - Relations

**Builds on:** **G.5** (selector consumes these rules), **G.4** (Acceptance & EvidenceProfiles), **C.22** (S2 typing), **C.18 NQD‑CAL**, **C.19 E/E‑LOG**, **B.3** (named assurance claims and declared aggregation, including WLNK only when applicable).
**Publishes to:** **UTS** (MaturityCards, rule ids), **SCR/RSCR** (branch coverage; parity hooks).
**Constrains:** **G.8** (LOG Bundling must cite MaturityCards), **G.9** (parity harness draws baselines per rung), **G.11** (refresh windows per rung & decay), **G.5** (Open‑Ended Family mode for GeneratorFamily).
**Outcome.** **Admissibility logic** for MethodFamilies combines LOG shells, the maturity poset, degrade modes, and publication requirements with CG‑Spec legality rules, CHR guard‑macros, and CAL acceptance mechanics.

### C.23:End

