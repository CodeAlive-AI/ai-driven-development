## C.2.2 - Reliability R in the F–G–R triad

> Reliability (R) is a conservative, evidence-bound warrant signal for a typed claim under an explicit claim scope (G). When reuse changes scope, kind, reference plane, notation, source-local meaning, model-use basis, or evidence basis, name the actual relation or operation and route only its declared congruence loss to **R**.

> **Type:** Architectural (A)
> **Status:** Stable

### C.2.2:1 - Problem frame

KD‑CAL asks a simple operational question: *“Where can I safely use this claim?”*
FPF answers with a minimal “epistemic location” built from three coordinates. Any relations traversed by a justification path are named separately:

* **F** (Formality) describes *how the claim is expressed* and how strongly it supports verification workflows (C.2.3).
* **G** (Claim scope) describes *where the claim is asserted to apply* as a set-like object (A.2.6).
* **R** (Reliability) describes *how strongly the claim is warranted* by linked evidence under that scope.
* **CL / CL^k / CL^plane** (Congruence Levels) describe fit or loss for the relation families that define them—for example, a semantic relation, kind relation, or reference-plane relation (B.3, C.3, F.9).
  A CL value belongs to the declared relation or traversal used by the path, not to the claim as a fourth coordinate. Shared wording about a "context" creates no relation and no loss value.
In practice, the triad is frequently used before it is made explicit:

* Authors implicitly “average” disparate evidence and report a single confidence.
* Teams treat higher formality (F) as if it automatically implies higher warrant (R).
* Scope growth is smuggled in through phrasing instead of explicit scope operators (A.2.6).
* A claim or its evidence is reused after a change of scope, kind, plane, notation, source-local meaning, model-use basis, or evidence basis without naming the actual relation and routing its declared loss into R.

This pattern makes **R** explicit in KD‑CAL and fixes the **triad discipline** required by Kind‑CAL (C.3) and the Trust & Assurance calculus (B.3).

### C.2.2:2 - Problem

FPF needs a reliability coordinate that is:

1. **Auditable.** A reader can trace R to concrete evidence and see how reuse penalties were applied.
2. **Composable.** R can be propagated through claim graphs conservatively, without illegal scale arithmetic.
3. **Orthogonal.** R is not conflated with F (expression) or G (scope).
4. **Relation-aware.** Any loss declared by an actual scope-translation, kind, plane, notation, source-local, model-use, or evidence-reuse relation is explicit and affects **R only**.
5. **Minimal.** The solution does not introduce new core types or new face-kinds.

### C.2.2:3 - Forces

| Force                                         | Tension                                                                                                            |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Single number vs multi-tradition evidence** | People want one scalar ↔ evidence comes from heterogeneous practices (proofs, tests, telemetry, expert review).    |
| **Rigor vs humility**                         | Claims need to be usable in decisions ↔ overconfident scores are dangerous and hard to unwind.                     |
| **Formal vs empirical warrant**               | Proof can be decisive in a formal theory ↔ real-world deployment requires empirical adequacy and drift management. |
| **Scope realism vs marketing scope**          | Narrow scopes raise R ↔ incentives push for broad statements with hidden preconditions.                            |
| **Reuse vs relation-specific loss**           | Reuse is valuable ↔ a changed scope, kind, plane, notation, local meaning, model-use basis, or evidence basis can introduce a different and separately governed loss. |
| **Toolability vs expressive freedom**         | A validator needs crisp rules ↔ authors want flexible narratives and domain nuance.                                |

### C.2.2:4 - Solution

#### C.2.2:4.1 - Canonical triad relation

**Definition DEF‑C2.2‑1 (Epistemic location).**
An epistemic location for a claim `c` is the tuple:

`Loc(c) = ⟨F(c), G(c), R_eff(c)⟩`

where:

* `F(c)` is Formality (C.2.3), treated as an **ordinal**.
* `G(c)` is Claim scope (A.2.6), treated as a **set-like scope object**.
* `R_eff(c)` is Effective reliability for `c`, treated as a **ratio-scale** scalar in `[0,1]` (or an **ordinal proxy** at **[M‑0/M‑1]**; see §4.5.A).
  `R_eff` is computed **pathwise** (DEF‑C2.2‑3): when more than one admissible justification path exists, publish multiple path records (PathId rows) and cite which PathId(s) a guard/decision consumed (see §4.8.A / G.6). Any collapse to a single scalar is an explicitly declared Γ‑policy (no implicit averaging).

A location always concerns one exact claim. `G` carries its `U.ClaimScope`; any stance, reference plane, effective scheme, model-use basis, working situation, evidence basis, or validity window is stated separately when it changes interpretation or use:
* No generic `K` or Context value is part of epistemic-location identity; the exact subject-specific values above remain independently governed.
* `S ∈ {design, run}` is the claim’s stance carrier (no DesignRunTag chimeras).
* `ReferencePlane` is declared where applicable; plane crossings apply `CL^plane` and penalize **R only**.
* When the claim is published on the Working‑Model surface, the author also declares `validationMode ∈ {postulate, inferential, axiomatic}` (E.14 / B.3).

**Mode-to-lane hint (informative).** `validationMode` sets the *default expectation* for which assurance lane carries the initial support load (B.3.3 or B.3.5).
It does **not** add a new characteristic and does **not** change the meaning of `R`:
* `axiomatic` → VA-dominant (constructive grounding or proof carriers); if `ReferencePlane=world`, LA may still be required.
* `inferential` → VA+TA-dominant (reasoned chain + typing/alignment assurance); LA is optional and scope-bound.
* `postulate` → LA-dominant (empirical validation with freshness/decay); VA is optional.
In all modes, **R remains warrant**, not ontological truth; “proof ⇒ R=1 in the world” is a category error.

**Profile note (informative; fold compatibility).** Some profiles treat empirical `R` as N/A for strictly **axiomatic** lines and use a tagged proxy `R_proxy := F` (`line=formal`) for folding, as an explicit proxy rather than an implicit “F⇒R” rule (B.1.3).

`⟨F,G,R⟩` is an **assurance tuple**, not a `U.CharacteristicSpace`; do not draw “trajectories” in `⟨F,G,R⟩`.

#### C.2.2:4.2 - What Reliability R means in KD‑CAL

**Definition DEF‑C2.2‑2 (Reliability as warrant).**
`R` is a conservative, evidence-bound indicator of how strongly the claim "holds as stated" under its declared `U.ClaimScope` and the separately named evidence and use conditions. It is interpreted as *warrant strength*, not as truth.

**Prophylactic clarification.**

* A higher `R` means “the evidence and its relevance supports relying on this claim under this scope.”
* A higher `F` means “the claim’s form is amenable to higher-formality checking and wider reuse,” but does not itself imply the claim is warranted.
* A larger `G` means “the claim applies to more cases,” but does not itself imply the claim is warranted in those cases.

#### C.2.2:4.3 - Pathwise weakest-link propagation (series vs parallel)

KD‑CAL’s default Γ‑fold is **weakest‑link** on the *entailment spine* (the premises/lemmas actually needed), computed per justification path. It is conservative, monotone, and auditable.

**Definition DEF‑C2.2‑3 (Pathwise weakest-link fold).**
Let `P` be a justification path for claim `c`. Let `SpineClaims(P)` be the required supports on the entailment spine, and let `SpineRelations(P)` be the exact scope, kind, plane, notation, source-local, model-use, or evidence-reuse relations actually traversed on that spine.

Define the raw warrant of the path as:

`R_raw(P) = min_{i ∈ SpineClaims(P)} R_eff(i)`

and compute the effective warrant of the path by applying congruence penalties (see §4.5 for policy shape):

`R_eff(P) = Π(R_raw(P); Φ(CL_min(P)), Ψ(CL^k_min(P)), Φ_plane(CL^plane_min(P)))`

**Spine discipline.** The `min` is taken over the *entailment spine* only (no satellites, no “nice-to-have” citations).

This matches the KD‑CAL propagation rule (C.2:4.3) and the Trust & Assurance skeleton (B.3): weakest-link on the spine, penalize only by the worst (lowest) congruence encountered on the path (no averaging).

**Parallel support (optional, declared).**
If the same claim `c` has multiple **independent** justification paths `{P_j}` (OR‑style support), the default is:

`R_eff(c) = max_j R_eff(P_j)`

Independence is recorded as an explicit note (e.g., separate rigs/datasets/proof lines), per CC‑C.2.2‑10 and the KD‑CAL composition rule (C.2:4.3).
If the “multiple paths” actually cover **different** scope slices, do not use `max` to hide weaker slices; instead publish distinct `G_path` (SpanUnion‑style coverage) and keep per‑path `R_eff` traceable (A.2.6 / C.2:4.3).

**Conflict detection (no averaging).**
If the evidence graph supports both `p` and `¬p` with overlapping scope, do **not** average. Separate the claims by the exact source, scheme, scope, model use, situation, or evidence basis that distinguishes them, or mark the claim **provisional** with explicit conflict edges until resolved.

#### C.2.2:4.4 - Relation-specific congruence penalties route to R only

A reused claim may traverse more than one independently governed relation. Before calculating `R_eff`, state what actually changed and use the rule for that change. A.2.6 owns claim-scope operations; C.3/C.3.3 owns kind relations; F.9 owns a semantic Bridge between exact local-sense cells; notation, reference-plane, model-use, and evidence-reuse relations keep their own definitions. None is a universal crossing relation.

**Invariant INV-C2.2-1 (R-only penalty routing).** For each traversed relation `r` whose rule declares a congruence loss:

`F_out = F_in`
`G_out = translate(r, G_in)` only when `r` is an applicable A.2.6 scope translation; otherwise `G_out = G_in`
`R_out ≤ R_in`, with the exact penalty determined by `r` and the cited policy

A scope translation may narrow or re-express `G`; it never widens the claim silently. A change in formality is a new episteme or explicit ΔF move, not a transport penalty. A semantic Bridge changes neither kind nor scope by itself. A kind or plane relation supplies no semantic correspondence unless that separate relation also obtains. Evidence reuse changes warrant only through its own evidence-use or reliance claim.

There is no implicit crossing. If a reuse depends on a changed value and its required relation or operation is absent, unresolved, or outside its applicability, the reuse is non-conformant. This keeps guard macros simple: each path records the relations it actually traverses and routes their declared losses to `R`, while every other coordinate changes only under its own rule.

#### C.2.2:4.4.A - Worked micro-example: scope revision and evidence reuse

A materials-lab claim says:

> `c_lab:` "Adhesive X retains ≥85% tensile strength on Al6061 for 2 h at 120–150 °C."

Its declared scope is `G_lab := {substrate=Al6061, temp∈[120,150]°C, dwell≤2h, evidenceWindow=1y, rig=Calib-v3}`. A plant engineer proposes a narrower claim for Plant B. Two different moves are required.

1. **State the plant claim and its scope.** Under A.2.6 the engineer explicitly narrows the temperature interval to `[122,148]°C` because the plant calibration rule reports a ±2 °C bias. This changes `G`; it is not an F.9 semantic Bridge and is not inferred from the words "lab" and "plant".
2. **Judge reuse of the lab evidence.** The exact A.10 or B.3 evidence-use and reliance claim names the lab evidence, plant claim, calibration edition, validity window, and intended use. If that relation's declared fit is `CL=2` under policy `Φ_v1`, compute `R_eff := max(0, R_lab − Φ_v1(2))`. The penalty reduces warrant; it does not perform the scope edit.

If lab and plant use distinct local meanings for a material term, F.9 separately tests a Bridge between their exact F.17 cells. Its semantic loss is not the calibration correction or the evidence-reuse result. A further safety narrowing to `[125,145]°C` is another explicit A.2.6 ΔG− decision.

The example therefore preserves one simple rule: name each changed value and relation once, change `G` only through the scope rule, and reduce `R` only through the loss rule that actually applies.

#### C.2.2:4.5 - Effective reliability under transport (policy-defined, monotone, bounded)

When a claim is reused through declared relations, `R_eff` is computed by applying the penalties those relations assign to their congruence levels.

**Definition DEF‑C2.2‑4 (Effective reliability under transport).**
Let:

* `CL` be the congruence level declared by the applicable scope, semantic, notation, model-use, or evidence-reuse relation (B.3 and its direct subject pattern).
* `CL^k` be the congruence level of an applicable kind relation (C.3/C.3.3).
* `CL^plane` be the congruence level of an applicable reference-plane relation (B.3 / plane patterns).

Let `Φ`, `Ψ`, and `Φ_plane` be **policy-defined**, **monotone**, **bounded**, **table-backed** penalty policies applied on the relevant edges:
* `Φ(CL)` — penalty declared for the applicable scope, semantic, notation, model-use, or evidence-reuse relation.
* `Ψ(CL^k)` — penalty declared for an applicable kind relation.
* `Φ_plane(CL^plane)` — plane-crossing penalty when `ReferencePlane` differs.

**Important (direction of monotonicity).** Congruence ladders are “polarity up” (higher CL = better fit). Per **CC‑G0‑Φ** and the Trust & Assurance skeleton, penalty tables are monotone **decreasing** in their CL ladders (if `CL1 < CL2` then `Φ(CL1) ≥ Φ(CL2)`, analogously for `Ψ` and `Φ_plane`) and bounded so that `R_eff` remains within `[0,1]` after clipping. Penalty magnitudes are not required to lie in `[0,1]` (tables may exceed 1 to force `R_eff → 0` under the subtractive default); what matters is monotonicity, boundedness, and published policy identifiers.

Define:

`R_eff(P) = clip_0^1( Π(R_raw(P); Φ(CL_min(P)), Ψ(CL^k_min(P)), Φ_plane(CL^plane_min(P))) )`

where each `*_min(P)` is the **lowest** congruence level encountered on the entailment spine of `P` for that dimension (a bottleneck; no averages), and `clip_0^1(x)` truncates to `[0,1]`.

**Default (safe) instantiation (subtractive).**
When policies are expressed as subtractive penalties, a safe default is:

`R_eff(P) = max(0, R_raw(P) − Φ(CL_min(P)) − Ψ(CL^k_min(P)) − Φ_plane(CL^plane_min(P)) )`

This generalises the B.3 skeleton to multiple congruence ladders (scope vs kind vs plane) without introducing new penalty characteristics. If a dimension is not present on the path, its penalty term is treated as neutral (`0` in the subtractive default).

**Provisional marking.**
Default admissibility thresholds for reuse are set by the relevant relation-calibration profile (e.g., G.7). Typically, `CL=1` requires an explicit waiver to proceed and `CL=0` is inadmissible; this pattern only specifies that such thresholds gate reuse before any numeric penalty is meaningful.

#### C.2.2:4.5.A - Math-by-level gating (B.1.3:4.3)

* **[M‑0/M‑1]** allow **ordinal** comparisons only (no arithmetic on `R_eff`); Φ/Ψ/Φ_plane may be qualitative (“low/med/high”). Publish evidence links + lane tags.
* **[M‑2/L1]** numeric `R_eff` requires referencing numeric, table-backed policy identifiers for Φ/Ψ/Φ_plane (and Π if not default), plus reproducibility tags for empirical legs; otherwise treat the claim as [M‑1] semantics.

#### C.2.2:4.6 - Evidence lanes are not new characteristics

KD‑CAL does not add new global coordinates beyond F–G–R. Instead, it requires that reliability be *explainable* via **assurance lanes** (B.3.3):

* **TA** (Typing assurance): semantic/type alignment sufficient for transport and composition.
* **VA** (Verification assurance): logical/algorithmic checking, proof, model checking, static guarantees.
* **LA** (Validation assurance): empirical adequacy under declared conditions, tests, benchmarks, telemetry.

Lane reporting is how KD-CAL supports the common research distinction between logical soundness and empirical adequacy **without introducing new global characteristics**.
Lanes remain **separable** in SCR/Notes; they are not averaged into a “single tradition score”.

#### C.2.2:4.7 - Scope operations are kind-safe (and use the ClaimScope algebra)

Reliability is meaningless if scope operations are applied to ill-typed entities.

**Well-formedness constraint WFC‑C2.2‑1 (Type before scope).**
Let `G1` and `G2` be claim scopes for claims about entities of kinds `K1` and `K2`. A scope operation that combines them—such as `G1 ∩ G2` for serial intersection or `SpanUnion({G_i})` for parallel coverage—is defined only if:

* `K1 = K2`; or
* an exact C.3/C.3.3 kind relation or cast makes the operation well typed for these participants and this direction.

An A.2.6 scope translation changes `G` only under its own rule. A kind relation does not translate scope. If distinct source-local meanings also matter, an actual F.9 Bridge and its bounded-use claim are separate; neither repairs an ill-typed scope operation.
This constraint prevents “type-by-scope” anti-patterns where scope manipulation is used to hide type mismatch.

#### C.2.2:4.8 - Minimal authoring recipe

A minimal, conforming KD‑CAL authoring flow for reliability is:

1. **Fix the typed claim.** State the claim as a typed proposition about a EntityOfConcern (Kind‑CAL, C.3).
2. **Declare claim scope.** Write `G` explicitly using A.2.6 operators; avoid scope-by-wording.
3. **Declare interpretation conditions.** State design or run stance, `ReferencePlane`, effective scheme, model-use basis, working situation, and `validationMode ∈ {postulate, inferential, axiomatic}` only where each changes this claim or its use. `G` already carries claim scope; do not add a generic Context identifier.
4. **Bind evidence.** Attach evidence stubs and lane tags (TA/VA/LA) and validity windows / decay policy where applicable (B.3.3, B.3.4).
5. **Choose Γ-mode.** Declare whether the support is **series** (required) or **parallel** (independent lines to the same claim).
6. **Compute R_raw.** Use the weakest-link fold on the entailment spine; for parallel support, use `max` only with an explicit independence note.
7. **Name actual relations on reuse.** Use A.2.6 for an applicable scope translation, C.3/C.3.3 for a kind relation, F.9 for a semantic relation between exact local-sense cells, and the direct pattern for notation, plane, model-use, or evidence reuse. Record the fit or loss declared by each traversed relation. If a required relation is absent or unresolved, stop that reuse; a generic cross-context Bridge cannot substitute for it.
8. **Compute R_eff.** Apply the declared penalty policies into `R` (never into `F` or `G`), and publish `⟨F,G,R_eff⟩` with traceable references and policy identifiers.

A reliable claim is not a loud claim; it is a claim that can be *carried*.

#### C.2.2:4.8.A - Authoring template: Path summary row (copy/paste)

When publishing `R_eff` for a claim, authors SHOULD include a compact, claim-local **path summary**. This is intentionally shaped so it can be turned into tooling later (EvidenceGraph/PathId in G.6) without introducing new Core types or face-kinds.

| PathId | Entailment spine (required supports) | CL_min | CL^k_min | CL^plane_min | Policy-id(s) (Φ / Ψ / Φ_plane) | R_raw | R_eff | Lane tags (TA/VA/LA) | valid_until |
| ------ | ----------------------------------- | ------ | -------- | ----------- | ------------------------------ | ----- | ----- | --------------------- | ---------- |
| P‑1    | `c ← {c_a, c_b, c_c}`               | 2      | 3        | —           | `Φ=Φ_v1`, `Ψ=Ψ_v2`             | 0.82  | 0.67  | {TA, LA}              | 2026‑09‑30 |

Notes:
* `CL_*_min` values are **bottlenecks** on the relevant path/dimension (no averaging).
* `valid_until` is the **earliest** expiry across empirical legs (or `—` / “fenced to TheoryVersion” for non-decaying proof legs).
* If you publish multiple admissible paths, include multiple rows and cite which PathId(s) your decision/guard consumed.

### C.2.2:5 - Archetypal Grounding

Informative; non-binding.

#### C.2.2:5.1 - System illustration

**System.** A brake controller `S` has a claim:

> `c1:` “For road friction μ ∈ [0.2, 0.9] and vehicle mass m ∈ [900, 2200] kg, wheel slip stays in [0.05, 0.25] under ABS control.”

* `F(c1)=F5` because the controller and constraints are expressed as a machine-checkable model plus executable test harness (C.2.3).
* `G(c1)` is the declared operating envelope (A.2.6) as a product set in `(μ, m, speed, tire)` space.
* Evidence:

  * VA: model-checking of a simplified plant/controller model (strong, but only for the simplified plant).
  * LA: HIL simulation + track tests under sampled conditions with recorded telemetry windows (freshness required).
  * TA: typed alignment between “μ” in simulations, “μ” in the estimation pipeline, and “μ” inferred from real-world sensors.

If track telemetry is used as evidence for the road claim, establish the exact A.10 or B.3 evidence-use and reliance claim, including the road claim, telemetry edition, operating scope, validity window, and intended use. Apply only the fit or loss declared for that evidence reuse; `G(c1)` changes only through a separate A.2.6 scope revision.

#### C.2.2:5.2 - Episteme illustration

**Episteme.** A paper asserts two claims about an algorithm `A`:

* `c2:` “A terminates for all inputs in domain D.” (axiomatic / proof-carrying)
* `c3:` “A achieves ≥ 0.92 F1 on dataset family F under deployment preprocessing P.” (empirical)

`c2` can achieve high VA with a proof carrier; its LA lane may be N/A, but its TA lane remains relevant because the intended meaning of “domain D” must align with the implementation’s input model.
`c3` requires LA evidence and a freshness or shift policy because dataset and preprocessing drift can change both scope and warrant. For production use, state the exact dataset/preprocessing relation and the A.10 or B.3 evidence-reuse claim, then apply its declared loss to `R_eff`; change `G` separately if the production claim has another scope.

### C.2.2:6 - Bias-Annotation

Informative; non-binding.

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal**.

* **Onto/Epist bias:** High formality is often mistaken for high warrant (“proof therefore true in the world”). This pattern mitigates by forcing LA/TA visibility and by routing transport loss into R rather than mutating the claim.
* **Prag bias:** Teams may Goodhart R by narrowing scope or selecting easy tests. This pattern mitigates by requiring explicit scope declaration and by making scope changes first-class (A.2.6).
* **Gov bias:** Overconfident reuse after a changed scope, scheme, model use, evidence basis, kind, or plane is a recurring failure. This pattern requires the actual relation and its declared loss instead of one generic crossing label.
* **Did bias:** A single scalar is seductive; it hides what kind of warrant exists. Lane reporting keeps the scalar honest.

### C.2.2:7 - Conformance Checklist

Normative.

| ID                                            | Requirement                                                                                                                                                                                                                 | Purpose                                                                       |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **CC‑C.2.2‑1 (Triad publication).**           | Authors of a KD‑CAL location **SHALL** publish `⟨F,G,R_eff⟩` for one exact claim, rather than publishing `R` alone.                                                                                                      | Keeps the warrant attached to its claim and declared scope.                   |
| **CC‑C.2.2‑2 (R-only penalty routing).**      | A conforming implementation of KD‑CAL reuse **SHALL** satisfy **INV‑C2.2‑1**.                                                                                                                                                | Ensures declared relation losses reduce warrant without silently mutating expression or scope. |
| **CC‑C.2.2‑3 (Weakest-link fold).**           | A conforming implementation of KD‑CAL reliability propagation **SHALL** use **DEF‑C2.2‑3** as the default for required supports, unless an alternative Γ‑fold is explicitly declared and remains monotone and conservative. | Prevents confidence laundering through aggregation.                           |
| **CC‑C.2.2‑4 (Relation visibility for reuse).** | Authors **SHALL** name every scope-translation, kind, plane, notation, source-local, model-use, or evidence-reuse relation traversed by the path and cite the fit or loss rule that affects `R_eff`.                                      | Makes each actual reuse loss auditable without inventing one crossing kind.   |
| **CC‑C.2.2‑5 (Penalty policy visibility).**   | Authors or tooling **SHALL** reference the active policy identifiers used for `Φ`, `Ψ`, `Φ_plane` **and** the penalty aggregation rule `Π` (if not the default) when computing `R_eff`.                                   | Ensures repeatability and prevents hidden policy drift.                       |
| **CC‑C.2.2‑6 (Type before scope).**           | Authors and validators **SHALL** enforce **WFC‑C2.2‑1** for scope composition operations.                                                                                                                                   | Prevents ill-typed scope algebra from creating incoherent reliability claims. |
| **CC‑C.2.2‑7 (Evidence binding).**            | Authors **SHALL** bind any asserted `R_eff` to evidence references that enable TA/VA/LA inspection, consistent with the assurance lane discipline (B.3.3) and evidence decay discipline (B.3.4).                            | Keeps R grounded and updateable.                                              |
| **CC‑C.2.2‑8 (No ordinal arithmetic).**       | Validators **SHALL** reject any computation that treats `F` or `CL` as if they were ratio-scale numbers (e.g., averaging, subtraction), except where explicitly permitted as a policy-defined penalty function on `R`. Validators **SHALL** also reject arithmetic over `R_eff` when it is published as an **ordinal proxy** ([M‑0/M‑1]). | Enforces CSLC legality and prevents silent scalarisation.                     |
| **CC‑C.2.2‑9 (Interpretation conditions declared).** | Authors **SHALL** distinguish design- and run-time assurance and declare `ReferencePlane`, effective scheme, model-use basis, working situation, and `validationMode` where each changes the claim or use.                               | Makes interpretation auditable without a generic Context identity field.     |
| **CC‑C.2.2‑10 (Parallel requires independence).** | Authors **SHALL** treat `max`-composition of support paths as admissible **only** when an explicit independence justification is recorded; otherwise supports are treated as one entangled line and remain weakest-link. | Prevents confidence inflation by double-counting correlated evidence.         |

### C.2.2:8 - Common Anti-Patterns and How to Avoid Them

Informative; non-binding.

| Anti-pattern               | Symptom                                                                                       | Why it fails                                                     | How to avoid / repair                                                                                    |
| -------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Averaging assurance**    | A mean/weighted sum of `R` values is reported as “confidence”.                               | It violates WLNK and is usually illegal scale arithmetic.        | Use weakest-link `min` on the entailment spine, then apply congruence penalties into `R` only.          |
| **Truth-by-score**         | `R=0.9` is treated as “the claim is true.”                                                    | R is warrant strength, not ontological truth.                    | Require explicit evidence links and scope; treat R as decision warrant only.                             |
| **Scope laundering**       | The claim’s applicability grows by wording changes while `G` is unchanged.                    | It silently widens scope, making comparisons meaningless.        | Use A.2.6 operators and treat scope changes as explicit revisions.                                       |
| **Relation laundering**    | A claim or its evidence is reused after a changed scope, kind, plane, notation, local meaning, model use, or evidence basis, while `R` is carried over unchanged. | It hides the actual change and its relation-specific loss. | Name the direct relation or scope operation and recompute `R_eff` from its declared loss; stop if that relation is missing. |
| **DesignRunTag chimera**     | Design-time proofs and run-time telemetry are mixed as if they were the same evidence object. | Evidence belongs to different stances and decays differently.    | Separate lanes and validity windows; treat crossings explicitly.                                         |
| **Ordinal arithmetic**     | CL or F levels are averaged to produce a pseudo-score.                                        | It violates scale legality and produces non-auditable numbers.   | Keep CL/F ordinal; convert only via declared penalty tables on R.                                        |
| **Many-weak-makes-strong** | Numerous low-quality supports are combined to inflate confidence.                             | It violates the weakest-link intent of conservative propagation. | Default to `min` for required supports; allow `max` only with explicit independence arguments.          |

### C.2.2:9 - Consequences

Informative; non-binding.

| Benefits                                                                                                     | Trade-offs and mitigations                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Comparability.** Different claims can be compared in a disciplined way when F and G are explicit.          | **Conservatism.** Weakest-link propagation can feel pessimistic; mitigate by making support structure explicit and improving the weakest evidence. |
| **Auditability.** Relation-specific reuse loss is visible and localised to R.                                | **Overhead.** Declaring the relations actually traversed and the evidence links is work; mitigate with templates and reuse of standard lane schemas. |
| **Upgradeable knowledge.** R can improve incrementally as evidence accumulates, without rewriting the claim. | **Scalar temptation.** People still want one number; mitigate by requiring lane breakdown visibility behind the number.                            |

### C.2.2:10 - Rationale

A triad only works if each coordinate has a single job.

* **G carries entitlement.** It states where the claim is asserted to apply. If G is implicit, teams argue about “what was meant” instead of updating scope.
* **F carries checkability.** It states how much the claim’s form supports mechanised scrutiny and reuse. If F is conflated with R, formalisation becomes a rhetorical weapon.
* **R carries warrant.** It states how much evidence supports relying on the claim under G. If R is not conservative, evidence with a low `R` coordinate can be laundered into high confidence.

Routing a traversed relation's declared congruence loss into **R only** prevents a subtle failure: a change of scope, kind, plane, notation, source-local meaning, model-use basis, or evidence basis cannot silently rewrite the claim or carry its old warrant forward.

Weakest-link propagation is chosen because it is the simplest rule that is monotone, conservative, and auditable. When better combination rules exist, they can be introduced as explicit Γ‑policies, but the default must be safe.

### C.2.2:11 - SoTA-Echoing

Normative.

**SoTA pack binding note.** If a G.2 SoTA Synthesis Pack has sources that bear on reliability under the exact changed claim scope, kind, reference plane, notation, source-local meaning, model use, or evidence basis in this case, cite the relevant ClaimSheet IDs and CorpusLedger entries. Cite a `BridgeMatrix` row only when the current path actually uses an F.9 cross-local semantic Bridge represented by that row. Otherwise record `SoTA-Pack: TBD/none` and treat this section as the seed; neither a generic Context nor a generic transport package is required.

| Practice claim                                                                                                      | Post‑2015 source anchor                                                                   | Alignment to this pattern                                                                                                                                                           | Adoption status                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Verification and validation should be distinguished and tied to evidence quality, not to rhetoric.                  | ASME V&V 40‑2018 (model credibility assessment).                                          | This pattern separates VA and LA lanes and binds `R_eff` to evidence and declared scope rather than to narrative confidence.                                                        | **Adopt**, with KD‑CAL’s conservative fold as an explicit default.                                                   |
| Trustworthiness depends on intended use, affected risks, operating conditions, and explicit limits.              | NIST AI Risk Management Framework 1.0 (2023).                                             | This pattern makes claim limits explicit through `G` and applies CL penalties only through the actual relation used by a reuse path.                                               | **Adapt**, because FPF treats declared relation loss as an epistemic penalty, not only as an organisational risk statement. |
| Safety arguments should make claims, evidence, and assumptions explicit and reviewable. | UL 4600 (2020) and related assurance-case practice in autonomous systems. | This pattern treats `R` as an auditable warrant signal whose inputs are explicit evidence items; any reuse names the exact relation traversed and its declared loss. | **Adopt**, while remaining notation-independent and avoiding tool mandates. |
| Empirical results should be accompanied by structured provenance and usage conditions to enable reuse and critique. | “Datasheets for Datasets” (Gebru et al., 2018) and “Model Cards” (Mitchell et al., 2019). | Scope discipline and lane reporting make empirical warrant reusable only when the exact evidence, claim, use, conditions, and any evidence-reuse or dataset relation are explicit; that relation's declared loss routes to `R_eff` only. | **Adopt**, with relation-specific congruence penalties as the reuse control mechanism. |
| Reproducibility requires packaging evidence and making it re-checkable by others. | ACM Artifact Review and Badging (updated practices post-2015) and The Turing Way (2019). | This pattern treats evidence as inspectable across TA/VA/LA lanes and lets reliability decay when evidence becomes stale or non-replayable. | **Adapt**, because FPF treats freshness and relation-specific reuse losses as first-class calculus inputs. |
| Strong inference benefits from “severe tests” rather than from accumulation of weak confirmations.                  | Mayo (2018) on severity in statistical inference.                                         | Weakest-link propagation and explicit scope declarations discourage superficial confirmation piling and encourage explicit, discriminating evidence.                                | **Adapt**, because KD‑CAL is agnostic to frequentist vs Bayesian inference but requires auditability.                |

### C.2.2:12 - Relations

**Builds on:** C.2 (KD-CAL overview), A.2.6 (claim scope and scope revision), C.2.3 (Formality F), B.3 and B.3.3/B.3.4 (assurance, evidence lanes, and refresh), B.1.3 (Γ-fold patterns), C.3.3 (cross-kind use), G.6 (EvidenceGraph PathId discipline), C.29/A.6.3.RT (notation and representation relations), A.1.1 (selected model-use structure), and A.10/B.3 for exact evidence-use and reliance relations. F.9 is used only when an obtaining relation between distinct local meanings, reference schemes, or reference planes is part of the path.
**Coordinates with:** C.16 for measurement claims, E.14 for working-model assertions, F.17 for optional local-meaning addresses, and E.18/E.17/A.21 when their own transfer, publication, or gate objects are current. G.2 supplies relevant source-pack entries; G.7 remains the conditional calibration path for its declared cross-Tradition/F.9 Bridge use, not a universal calibration owner.
**Used by:** C.3.3 for cross-kind reuse discipline, guard macro bundles in C.3.A and C.21, and acceptance or gating logic that consumes `R_eff` while preserving `F` and `G`.
**Clarifies:** the KD-CAL meaning of reliability implicit in C.2:4.1 and the relation-specific reuse claims referenced across B.3 and C.3; it does not create a universal transport relation.

### C.2.2:End

