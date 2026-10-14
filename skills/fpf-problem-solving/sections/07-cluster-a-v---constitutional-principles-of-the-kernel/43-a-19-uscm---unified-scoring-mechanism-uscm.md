## A.19.USCM - Unified Scoring Mechanism, USCM

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)

`USCM.IntensionRef` identifies the exact `U.Mechanism` declaration in §4.1 under A.6.1. CHR resolves its score stage to the local Score operation; the declaration supplies the meanings and actual application/binding rules below.

### A.19.USCM:0 - At a glance — didactic, informative

* **Suite stage:** `score` (ordering lives only in `A.19.CHR:4.5` / `suite_protocols`; suite membership is a set in `A.19.CHR:4.2`).
* **Inputs, conceptual:** an admitted measure profile for the exact evaluated bearer, plus `CNSpecRef`, `CGSpecRef`, and `ScoringMethodDescriptionRef`; their editions name the criteria, claim scope and selected slices, qualification window, comparison or reference basis, evidence policy, and intended result use. `MinimalEvidenceRef` may override the CG-Spec minimum.
* **Output:** `ScoreProfileSlot` = a set of score measures (vector scores are first‑class; a scalar score is allowed only if explicitly declared).
* **Non‑goals:** does **not** normalize (UNM), aggregate (ULSAM), compare (CPM), select (SelectorMechanism), threshold, publish, or emit telemetry; it is a scoring step with explicit admissibility and evidence surfaces.
* **P2W seam:** an A.15.2 baseline selects editions and policies, including ScoringMethodDescriptionRef when USCM is used. A.15.3 typed filling applies only to independently declared receiving positions under A.19.CHR:4.7.2. Actual Score bindings obtain under §4.1; Audit records the effective refs and pins.
* **Failure mode:** tri‑state guard (`pass|degrade|abstain`); unknown never coerces to `pass`, and MUST NOT be coerced to `0/false`.
* **Quick rule of thumb:** if `CGSpecSlot.SCP` is missing → `ScoreEligibility = abstain` (fail‑closed); if `ScoringMethodDescriptionSlot` is missing → `ScoreEligibility = abstain` (no implicit scoring method); if `CN‑Spec.comparability` requires normalization‑based comparability → normalization MUST be explicit in choreography (Uses/pins), never hidden inside `Score`.

### A.19.USCM:1 - Problem frame

FPF’s Characterization (CHR) suite treats scoring as a **distinct mechanism boundary** within the CHR suite (authoritative membership: `A.19.CHR:4.2`). Suite membership is a **set** (order has no semantics); any intended ordering is expressed only via `suite_protocols` (`A.19.CHR:4.5`), under the suite obligations (`A.19.CHR:4.3`).

Within the canonical suite-closed protocol, USCM appears as the `score` stage (after `normalize` and `indicatorize`, before comparison and selection). USCM’s surface is admissibility-first: it produces **score measures** from admitted profiles while remaining constrained by the admissibility gate (`CG-Spec.SCP`) and by scale-lawfulness (CSLC).

USCM exists to keep a strict distinction between:

* **normalization** (UNM),
* **indicatorization** (UINDM),
* **scoring** (USCM),
* **aggregation/folding** (ULSAM), and
* **comparison/ordering/selection** (CPM + SelectorMechanism),

so that each commitment has a single place to live, can be audited, and can evolve without smuggling extra semantics into adjacent steps.

### A.19.USCM:2 - Problem

Engineering teams often need to convert an admitted (indicator or NCV) profile into one or more **score measures** for downstream comparison and selection. If scoring is not given a **first‑class mechanism boundary** with explicit admissibility and evidence surfaces, the following failure modes are common:

* **Illicit arithmetic by convenience:** teams apply weighted sums, averages, or nonlinear transforms across mixed scale kinds without an explicit admissibility profile, creating scores that are not CSLC‑lawful.
* **Hidden normalization:** scoring implementations silently normalize, align, or flip polarities, collapsing the distinction between “normalize” and “score” and making downstream reasoning non‑reproducible.
* **Silent scalarization:** multi‑criteria realities (vector scores, partial‑order comparability) are reduced to a single scalar via hidden tie‑breakers, producing an apparent total order that is not justified.
* **Unknown coercion:** missing or insufficient evidence is coerced into `0/false` or treated as “good enough,” yielding scores that look precise while being epistemically unsafe.
* **Drift and non-auditability:** different teams score the same admitted scoring target differently because admissibility constraints and effective policies (editions, evidence rules, crossings) are not explicit and not recorded.

### A.19.USCM:3 - Forces

1. **Admissibility discipline vs operational pressure.** Scoring is where "just compute a number" pressure is strongest, but admissibility must remain explicit and checkable: SCP and CSLC constraints must bound permissible transforms.

2. **Method diversity vs stable mechanism boundary.** Scoring methods evolve rapidly; USCM’s signature must remain stable so method families can be wired through SoTA packs and extensions without mutating the mechanism boundary.

3. **Vector reality vs scalar simplicity.** Many situations require multiple score dimensions. A single scalar score may be convenient but must be an explicit, declared commitment, not a hidden reduction.

4. **Uncertainty vs decisiveness.** Teams need decisions under uncertainty; the framework must prevent epistemic overconfidence. Tri‑state admissibility guards preserve correctness without forcing silent coercions.

5. **Strict distinction across CHR steps.** USCM must not absorb UNM, ULSAM, or CPM semantics “for convenience,” or the suite becomes opaque and non‑teachable.

6. **Evolvability vs didactic usability.** Interfaces must remain evolvable (stable SlotKind surface; method semantics externalized), while the spec remains teachable: a reader must find USCM’s purpose, boundary, laws, guard behavior, and audit minimum in one place.

7. **P2W separation and gate/guard separation.** Planned baseline binding, including editions and policy ids, belongs to WorkPlanning plan items; gate decisions belong under gate patterns and work‑enactment logs belong with `WorkEnactment`. USCM must expose eligibility and audit pins without turning into a gate or a planner.

### A.19.USCM:4 - Solution

USCM is the **canonical scoring mechanism** in the CHR suite. It defines:

* a stable **mechanism boundary** (`score` is its own stage with a canonical `Score` operation and a tri‑state eligibility predicate),
* a stable **SlotKind surface** (via the suite lexicon),
* an admissibility‑first **LawSet** anchored in `CG‑Spec.SCP` and CSLC,
* an explicit **anti‑smuggling rule** (no implicit normalization), and
* an **audit minimum** (the evaluated bearer and input profile, exact editions, criteria, scope and window, comparison basis, evidence used, effective evidence policy, result use, and any relation actually used).

USCM preserves the suite obligations by construction: it does not embed GateDecision/GateLog, it does not perform publish/telemetry steps, and it cites relation pins only when the score or its receiving use actually depends on an obtaining relation; supported loss stays in `R_eff`.

Method semantics (“how to score”) remain out of suite core: they belong in SoTA packs (`G.2`) and wiring‑only extension modules (`GPatternExtension` blocks), while USCM remains the stable conceptual mechanism boundary.

#### A.19.USCM:4.1 - Operation declaration

`USCM.IntensionRef` cites the exact A.6.1 U.Mechanism declaration episteme here. The CHR score stage resolves to its local Score operation. Selecting a changed argument, scoring law or guard requires selecting that changed declaration explicitly; another realizer of the same declaration changes no suite member.

* **Scope note:** A.6.1 governs the operation and its actual argument/result bindings below. The planned baseline selects method and specification editions; independently declared receiving positions may use A.15.3 typed filling. Score returns a score profile, while eligibility and Audit retain their own meanings. GateDecision/GateLog remain outside this declaration.

* **IntensionHeader:** `id = USCM`, `version = 1.0.0`, `status = stable`.

* **IntensionRef:** `USCM.IntensionRef` (canonical target for the suite member named in `A.19.CHR:4.2`).

* **SignatureManifest (optional; importability):** if a USCM publication is intended to be imported/reused, it SHOULD publish a `SignatureManifest` (A.6.0:4.5 and A.6.1; A.6.0 checklist item 10 with `SM-1` through `SM-4`) consistent with `IntensionHeader`/`Imports`, explicitly exposing the stable SlotKind surface (including `ScoringMethodDescriptionSlot`) and any declared scalarization commitment.

* **Tell.** **SCP‑first** scoring: produce score measures from admitted profiles without violating CSLC / scale lawfulness.

* **Purpose:** **SCP‑first** scoring: produce score measures from admitted profiles without violating CSLC / scale lawfulness.

* **Imports:** `G.0 (CG‑Spec.SCP, CG‑Spec.MinimalEvidence)`, `A.18 (CSLC)`, `C.16 (measurement constitution and scale-lawful operations when measurement is claimed)`, `A.19.CN (comparability.mode + normalization routing)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`.

* **SubjectBlock:**

  * **SubjectKind:** `U.Measure`, supplied by the measures in InputProfileSlot; each measure retains its bearer, Characteristic and Scale.
  * **RangedValueKind:** `U.Measure`; Score transforms the admitted profile under the selected method, and ScoreEligibility assesses that proposed transformation.
  * **SliceBasis:** the declared `U.ClaimScope` and selected `U.ContextSlice` members, together with the qualification window and intended result use.
  * **Input qualification:** scoring ranges over the admitted indicator or NCV profile for the exact evaluated bearer, criteria, claim scope and selected slices, qualification window, comparison or reference basis, and intended result use; `CN-Spec.comparability` routes comparison and `CG-Spec.SCP` gates admissibility.
  * Results are declared per operation: the score-measure profile and the eligibility judgment.

**Operation-local argument and result declarations**

Each input meaning is declared separately for Score and ScoreEligibility. ByRef inputs resolve to the stated exact value and edition. Cardinalities shown are for Score. ScoreEligibility may assess an incomplete proposal: each required input then has cardinality 0..1, and an absent value has no binding and triggers the corresponding missing-input rule.

| Direction | Local designator | Meaning and ValueKind | Designation; cardinality |
| --- | --- | --- | --- |
| Argument | InputProfileSlot | Admitted set of U.Measure values to score; each UINDM-derived value retains its exact basis position, Characteristic and Scale | ByValue; 1 profile |
| Argument | CNSpecSlot | CN-Spec used for the bearer, basis, scope/slices, qualification window, intended use and comparability routing | CNSpecRef; 1 |
| Argument | CGSpecSlot | CG-Spec supplying the SCP restrictions and default evidence requirement for this scoring use | CGSpecRef; 1 |
| Argument | ScoringMethodDescriptionSlot | ScoringMethodDescription supplying the selected Coordinate→Score rule, domain, codomain, Scale, polarity and use-required properties | ScoringMethodDescriptionRef; 1 |
| Argument | MinimalEvidenceSlot | MinimalEvidence override used in place of CGSpecSlot.MinimalEvidence | MinimalEvidenceRef; 0..1 |
| Score result | ScoreProfileSlot | Set of U.Measure values actually returned by the declared scoring rule | ByValue; 1 profile on completed admitted scoring, 0 on abstain or termination without a result |
| ScoreEligibility result | GuardDecision | Eligibility judgment under the predicates below: pass, degrade or abstain | ByValue; 1 on completed evaluation |

An argument's **bindingPredicate** holds when this Score or ScoreEligibility application actually uses the resolved value for that row's purpose: the profile supplies the operands, the method supplies the transformation, CN-Spec delimits its use and routing, and CG-Spec plus any override supplies its admission and evidence conditions. Mere inclusion in an Audit record is insufficient. The ScoreProfileSlot **bindingPredicate** holds when that Score application returns the profile obtained by applying the bound method lawfully to those operands, with the declared scalar/vector cardinality. The guard's result binding holds when that ScoreEligibility application returns its evaluated judgment. Each binding follows A.6.1 identity and continuous extent within the application; the result begins to bind at return.

**SlotIndex (derived projection).** Project this table's local designators, ValueKinds, designation modes and cardinalities. Its historical Slot names permit CHR lookup and introduce no separate meanings; A.6.5 relation SlotSpecs do not govern these operation positions. A repeated Characteristic name alone cannot select a profile value whose basis position and Scale matter.

* **OperationAlgebra** (suite stage = `score`, per `A.19.CHR:4.5`; canonical stage‑op = `Score`):

  * `Score(InputProfileSlot, CNSpecSlot, CGSpecSlot, ScoringMethodDescriptionSlot, MinimalEvidenceSlot?) → ScoreProfileSlot`; the cited inputs supply the evaluated bearer and use qualifications.

**ApplicationPredicate.** Score obtains when a calculation actually applies the bound scoring method to the bound input profile under the CN-Spec/CG-Spec conditions. It proceeds on pass or on an explicitly permitted degrade branch and returns the lawful score profile; abstain starts no Score calculation. ScoreEligibility obtains when an evaluation actually assesses the proposal under the eligibility predicates and returns the corresponding judgment. A passing guard or a cached compatible profile does not establish a new Score calculation.

**ApplicationIdentityRule.** One application is one scoring calculation or eligibility evaluation at its calculation locus, from taking up the chosen operands/rules until return or termination. Reidentifying that same invocation preserves identity. A second invocation with identical profile, method, specifications, qualification point and output is a distinct application; changing those arguments for another calculation also makes another application. A record identifier designates an established invocation and cannot create it.

**ApplicationExtentRule.** Score extends from actual use of the input profile under the selected method to the return of its score profile or termination; ScoreEligibility extends from actual proposal assessment to judgment or termination. An unfinished invocation has an open extent and no unreturned result binding. The qualification point or input window identifies what is scored, not when the scoring occurs. Ordinary use of a scoring function does not by itself assert dated U.Work.

For the Celsius example in §4.2, two separate calculations of (20−0)/(40−0) each return 0.5 under the same declared method. Their operand-to-return episodes and result bindings differ. A saved 0.5 can refer to the earlier result when that return is established; numerical agreement and the same method pins cannot establish a second return. The example retains its specified Celsius input and explicit interval endpoints.

* **LawSet** (minimum; admissibility‑first, no hidden scalarization):

  1. **SCP+CSLC lawfulness:** any numeric transform used to produce `ScoreProfileSlot` MUST be admissible under `CGSpecSlot.SCP` and CSLC‑lawful (cites `G.0` + `A.18`).
  2. **ScoringMethod is explicit (no hidden defaults):** `Score` MUST cite `ScoringMethodDescriptionSlot` (edition-pinned via P2W when reproducibility matters; see `A.19.CHR:4.7.2`). Disclose the scoring method **𝒢** (Coordinate→Score), its domain, codomain, Scale, polarity and the properties required by the declared scoring use. Apply C.16 when measurement is claimed and enforce the actual SCP/CSLC restrictions. Boundedness or monotonicity is required only when the selected method or use requires it. USCM MUST NOT rely on an implicit default scoring method.
  3. **No implicit normalization:** `Score` MUST NOT silently perform UNM; if `CNSpecSlot.comparability` requires normalization‑based comparability, the normalization step MUST be explicit in choreography (Uses/pins), not hidden in `Score`.
  4. **Vector scores allowed; scalarization must be explicit:** producing a single scalar score is allowed only if explicitly declared (e.g., by fixing `ScoreProfileSlot` cardinality to 1 and citing the lawful transform); partial‑order semantics MUST NOT be silently reduced to a scalar “tie‑breaker”.
  5. **Unknown is not coerced:** unknown / insufficient evidence MUST NOT be mapped to `0`/`false`; use tri‑state guards and explicit failure behavior.

* **AdmissibilityConditions** (tri‑state guard; fail‑closed on missing admissibility/evidence):

  * `ScoreEligibility(InputProfileSlot, CNSpecSlot, CGSpecSlot, ScoringMethodDescriptionSlot, MinimalEvidenceSlot?) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires: (i) `CGSpecSlot.SCP` is present, (ii) the scoring method and edition are explicit, (iii) the input profile is admitted for the exact bearer and criteria, (iv) the cited specs apply to the exact claim scope and selected slices, qualification window, comparison or reference basis, and intended result use, (v) the evidence supporting the admitted profile passes the effective minimum, and (vi) `CN-Spec.comparability` routing is satisfied, including explicit UNM when needed.
  * If `MinimalEvidenceSlot` is absent, the guard MUST evaluate evidence against `CGSpecSlot.MinimalEvidence` (by explicit rule), and MUST NOT return `pass` when evidence is missing/unknown.
  * If `ScoringMethodDescriptionSlot` is missing or unpinned/ambiguous under the active planned baseline, the guard MUST return `abstain` (fail‑closed), not “assume a default”.

* **Applicability:**

  * Intended to be used after indicatorization (when indicator profiles are used) and before comparison/selection.
  * Applicable only when admissibility/evidence surfaces are present via `CGSpecSlot` (fail‑closed otherwise).
  * Applicable only when a scoring method is explicitly declared via `ScoringMethodDescriptionSlot` (edition‑pinned when reproducibility matters). A “do nothing / identity scoring” intent (if ever needed) MUST still be declared as an explicit scoring method description, not as an implicit default.

* **Relation boundary:** scoring creates no transfer relation. If the input profile or receiving use relies on an F.9 Bridge, kind relation, or plane relation, cite that exact obtaining relation, its direction and loss; supported penalties route to **`R_eff` only**.

* **Γ_timePolicy:** `point` by default (no implicit “latest”).

* **PlaneRegime:** each admitted input and score keeps its declared reference plane; USCM introduces no plane crossing. When a conclusion depends on a relation between planes, cite that relation, its direction and loss, and keep the receiving use separate.

* **Audit:**

  * MUST record: the exact evaluated bearer and admitted input profile; `CNSpecRef.edition`, `CGSpecRef.edition`, and `ScoringMethodDescriptionRef.edition`; criteria, claim scope and selected slices, qualification window, comparison or reference basis, and intended result use.
  * MUST record the evidence refs used to admit the input profile and evaluate `ScoreEligibility`.
  * MUST record the **effective evidence policy**:
    * if `MinimalEvidenceSlot?` is present → record `MinimalEvidenceRef` as effective;
    * otherwise → cite `CGSpecSlot.MinimalEvidence` as effective.
  * SHOULD record the realized `GuardDecision` for `ScoreEligibility`, and (when `degrade`/`abstain`) the referenced failure behavior / downstream handling policy id (e.g., SoS‑LOG branch id) when such a policy is in scope.
  * SHOULD record: a stable description of `ScoreProfileSlot`; any F.9 Bridge, kind relation, or plane relation only when the score or receiving use actually relies on it; and, when normalization-based comparability was required, the explicit upstream UNM ref or pin.

#### A.19.USCM:4.2 - Interpretation notes — informative

* **Selected-input basis.** Consume the exact UINDM S and space declaration when an indicator profile is used. For CS7 in A.19.UINDM §5.4, the Celsius policy selects i1 and the declared Celsius scoring rule reads 20, giving 0.5. It cannot read the kelvin position's 293.15 under that rule. After a basis change, resolve the selected positions and the scoring method's input requirements again; keep any projection in the original basis order.

* **A score profile is a set of measures.** `ScoreProfileSlot` is a `U.Set (of U.Measure)`. Treat this as “vector scoring by default.” If a project truly needs a single scalar score, declare that explicitly (per LawSet item 4), rather than assuming scalarity.

* **USCM does not order; it scores.** USCM produces score measures. Any ordering, dominance, or set‑valued comparison is performed by CPM and SelectorMechanism (and any optional aggregation is made explicit via ULSAM). Treating the score as “the decision” is a category error in CHR terms.

* **ScoringMethod is explicit (no hidden defaults).** USCM requires `ScoringMethodDescriptionSlot`: the scoring method is a first‑class, auditable choice (typically pinned in planned baseline). This keeps “how we score” evolvable (wired via method packs) without making it implicit or accidental.

* **No implicit UNM is a boundary guard.** This discourages convenience implementations that “just normalize inside scoring.” USCM forbids that: if comparability requires normalization‑based routing, the UNM step is explicit in choreography (Uses/pins) and visible in audit surfaces.

* **Evidence policy is explicit and auditable.** `MinimalEvidenceSlot?` is an optional override; otherwise the effective policy is `CGSpecSlot.MinimalEvidence`. Failures do not disappear; they must show up as `degrade/abstain` and be traceable.

* **Relations are explicit and loss stays in `R_eff`.** When a score or receiving conclusion depends on another source-local meaning, bearer kind, or reference plane, cite the exact obtaining relation and supported loss. A changed bearer, scope, method, basis, or use is not by itself a crossing.

### A.19.USCM:5 - Archetypal Grounding — informative

#### A.19.USCM:5.1 - Tell

Think of USCM as **admissibility‑gated scoring**:

* Input: “an admitted profile of measures for this exact bearer, criteria, scope and window, comparison basis, evidence policy, and result use, plus the CN-Spec and CG-Spec editions that declare those bounds”
* Output: “a set of score measures that downstream steps may compare/select on”

The key didactic boundary is: **USCM is allowed to transform measures only within the admissibility surface (SCP+CSLC), and it must not hide normalization, aggregation, or ordering.**

#### A.19.USCM:5.2 - Show — U.System

A program manager evaluates competing rollout plans for a product launch.

* The admitted profile includes measures like `{Cost, LeadTime, Reliability, RiskExposure, CarbonPerUnit}`.
* The CG‑Spec’s `SCP` admits only scale‑lawful transforms (e.g., monotone transforms on ratio/interval measures, explicit unit alignment rules, and prohibited operations on ordinal measures).
* USCM runs `Score(...)` and outputs a score profile such as `{UtilityScore, RiskScore}` rather than forcing a single number.
* A plan lacks sufficient evidence for `RiskExposure` for the named planning bearer, selected claim slices, and qualification window; `ScoreEligibility` returns `degrade`, and the audit records the effective MinimalEvidence policy and the exact CN-Spec and CG-Spec editions.

Downstream steps can now compare and select with an explicit audit trail, instead of pretending that “the score was objective.”

#### A.19.USCM:5.3 - Show — U.Episteme

A research lead compares several model families for deployment across heterogeneous environments.

* Indicators include calibration and robustness metrics; scoring is done using a calibrated probabilistic score plus uncertainty‑aware score dimensions.
* A post‑2015 practice example is to keep monotonicity and interpretability constraints explicit (e.g., monotone additive models or monotone deep lattice style models) and to treat uncertainty as first‑class (e.g., conformal set‑valued scoring that yields intervals rather than point scores).
* USCM produces a score profile that can remain vector‑valued and uncertainty‑aware, and it refuses to coerce “unknown” into a point score. Comparisons and selections occur downstream using set‑valued semantics where appropriate.

### A.19.USCM:6 - Bias-Annotation — informative

* **Gov (governance).** Bias toward explicit admissibility and evidence surfaces (`CGSpecRef`, `SCP`, `MinimalEvidence`) rather than "standard practice" arithmetic. Risk: perceived overhead. Mitigation: keep the kernel signature small and push method specifics into SoTA packs and wiring modules.

* **Arch (architecture).** Bias toward stable interfaces and strict step boundaries (no implicit UNM; no hidden scalarization). Risk: reduced room for ad‑hoc shortcuts. Mitigation: allow richer scoring method families via wiring, without mutating the USCM intension.

* **Onto/Epist.** Bias toward treating scores as measures with declared semantics, not as “the truth.” Risk: teams accustomed to one‑number rankings may resist. Mitigation: treat scalarization as an explicit, auditable commitment, not as the default.

* **Prag (pragmatics).** Bias toward fail‑closed guards and traceability under uncertainty. Risk: more `degrade/abstain` outcomes early. Mitigation: couple `degrade` with explicit downstream behavior policies, rather than silent coercion.

* **Did (didactics).** Bias toward “one place to learn the mechanism”: the problem/forces/solution narrative is co‑located with the canonical Mechanism.Intension.

### A.19.USCM:7 - Conformance Checklist

A USCM publication or use is conformant if it satisfies:

1. **Mechanism declaration completeness.** The A.6.1 operation-local arguments/results, application predicates, identity/extent rules and laws in §4.1 are recoverable, together with the declared imports, subject, admissibility, applicability, transport, time, plane and Audit conditions. SlotIndex projects the argument/result declarations; eligibility retains its tri-state result.

2. **SlotKind discipline.** SlotKind tokens match the CHR SlotKind lexicon for the roles used (`InputProfileSlot`, `CNSpecSlot`, `CGSpecSlot`, `MinimalEvidenceSlot`, `ScoringMethodDescriptionSlot`, `ScoreProfileSlot`); no generic `ContextSlot` is introduced. If a required token is missing, suite-dock it rather than introducing it ad hoc in the mechanism.

3. **SCP+CSLC admissibility is enforced.** Any numeric transform used to produce score measures is admissible under `CGSpecSlot.SCP` and CSLC-lawful; illicit operations (especially “convenient arithmetic” over non-lawful scales) are excluded.

4. **ScoringMethod is explicit and auditable.** `Score` cites `ScoringMethodDescriptionSlot` (edition-pinned when reproducibility matters). Its domain, codomain, Scale, polarity and use-required properties are disclosed and satisfy the applicable SCP/CSLC restrictions. Apply C.16 for any measurement claim.

5. **No implicit normalization.** `Score` does not silently perform UNM. If `CN‑Spec.comparability` requires normalization‑based routing, the normalization step is explicit in choreography (Uses/pins) and auditable.

6. **No hidden scalarization.** Vector scores are permitted. A scalar score is produced only when explicitly declared, and partial‑order semantics are not reduced to a scalar tie‑breaker.

7. **Unknown and evidence handling is explicit.** Unknown / insufficient evidence is not coerced to `0/false`. Eligibility uses `GuardDecision ∈ {pass|degrade|abstain}` and evaluates evidence against the effective policy (`MinimalEvidenceSlot` override or `CGSpecSlot.MinimalEvidence`).

8. **Planning and actual binding remain separate.** A.15.2 carries the intended edition/policy baseline; A.15.3 governs typed filling only for independently declared positions. The actual application uses its effective bindings under §4.1, and Audit records their refs and pins. Planned selection alone does not establish actual use.

9. **Relation and plane discipline.** Another bearer, scope and window, basis, method, plane, or result use gets a fresh eligibility decision. Any F.9 Bridge, kind relation, or plane relation is cited only when the score or conclusion relies on that obtaining relation, and supported loss routes to `R_eff`.

10. **Specialization discipline, if extended.** Any specialization of USCM (`⊑/⊑⁺`) follows the following extension conditions: SlotKind invariance for inherited ops, no new mandatory inputs to the inherited `Score` op, and any extra outputs or ops expressed only via `⊑⁺`.

### A.19.USCM:8 - Common Anti‑Patterns and How to Avoid Them

* **Hidden normalization inside scoring.** Scoring silently normalizes or aligns measures. Avoid by making UNM explicit in choreography and keeping USCM's `Score` admissibility‑only.

* **Weighted sum across mixed or non-admissible scales.** Treating “weights + sum” as universal. Avoid by requiring SCP+CSLC admissibility; if the scale operation is not scale-admissible, it is not admissible.

* **Silent scalarization.** Collapsing vector scores or partial orders into a single “overall score” via an untracked tie‑breaker. Avoid by leaving vector scores intact, and making scalarization an explicit declared commitment.

* **Implicit scoring method (“we just use the standard formula”).** The scoring method is assumed rather than declared and pinned. Avoid by requiring `ScoringMethodDescriptionSlot` and edition pinning in planned baseline; treat “identity scoring” (if ever needed) as an explicit method description, not a hidden default.

* **Unknown → 0 coercion.** Treating missing evidence as zero, false, or “good enough.” Avoid by tri‑state guards and explicit failure behavior, with auditable effective evidence policy.

* **Shadow CG‑Spec.** Hard‑coding admissibility rules inside a scoring method description instead of citing `CGSpecSlot.SCP`. Avoid by keeping admissibility in CG‑Spec and treating method details as wiring.

* **Telemetry or publish leakage.** Treating scoring as a reporting step. Avoid by keeping publish/telemetry outside suite closure and using the appropriate post-suite mechanisms.

* **SlotKind drift.** Renaming or re‑purposing slots across specializations or across mechanisms. Avoid by using the suite SlotKind lexicon and the `⊑/⊑⁺` discipline.

### A.19.USCM:9 - Consequences

**Benefits**

* Makes scoring a first‑class, admissibility‑gated CHR step, reducing illicit arithmetic and silent assumptions.
* Improves auditability and reproducibility via explicit edition pins and explicit evidence policy selection (override vs default).
* Preserves evolvability: scoring method families can change via SoTA wiring without changing the USCM intension.
* Supports correctness under uncertainty via tri‑state guards and explicit unknown handling.

**Costs / trade‑offs**

* Requires explicit CG‑Spec admissibility surfaces (SCP) and explicit evidence policies to achieve `pass`; this can feel slower than "just compute a score."
* Vector scores can be less immediately comfortable than a single number; downstream comparison/selection must be explicit about how vector scores are used.

### A.19.USCM:10 - Rationale

Scoring is a frequent source of semantic precision loss: it is easy to smuggle normalization, illegal arithmetic, implicit thresholds, and uncertainty coercion into “a simple scoring function.” USCM prevents that by forcing a clean boundary:

* **Admissibility first:** all transforms are justified by `CG‑Spec.SCP` and CSLC.
* **No hidden steps:** normalization is explicit (UNM), aggregation is explicit (ULSAM), ordering is explicit (CPM/SelectorMechanism).
* **Uncertainty is visible:** admissibility is tri‑state; unknown is not coerced.
* **Audit is minimal yet decisive:** effective editions and effective evidence policy are always traceable.

This increases both evolvability (stable interface, externalized method semantics) and didactic usability (a single place to learn USCM’s boundary and obligations).

### A.19.USCM:11 - SoTA-Echoing

**SoTA vs popular note.** This section records alignment to post‑2015 evidence‑backed practice. It is **not** a mandate to use fashionable methods; method semantics stay in SoTA packs (`G.2`) and wiring modules, while this pattern fixes the stable mechanism boundary.



#### A.19.USCM:11.1 - SoTA alignment map

| SoTA practice pointer, post‑2015+                                             | Primary source examples, post‑2015+                                                                                                               | Where it connects to USCM                                                                                                                                        | Adoption status |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| Prefer monotone and interpretable scoring surfaces where appropriate          | Explainable additive and monotone model lines, e.g., Lou et al. 2016; Nori et al. 2019; monotone deep lattice style models, e.g., You et al. 2017 | Expressed as **admissibility‑bounded transform freedom** via `CGSpecSlot.SCP` and explicit scalarization rules; method details stay out of the kernel                 | Adapt           |
| Treat probabilistic scores as measures requiring calibration, not raw outputs | Calibration practice, e.g., temperature scaling (Guo et al. 2017) and successors                                                                  | Expressed as “score is a measure on an explicit scale,” bounded by SCP+CSLC and evidence gating; calibration itself is wired as method semantics, not kernel law | Adapt           |
| Keep uncertainty explicit and allow set‑valued scoring when appropriate       | Modern conformal prediction practice, e.g., Romano et al. 2019; Barber et al. 2021                                                                | Expressed as “vector scores allowed; unknown not coerced; no hidden scalarization,” enabling downstream set‑valued comparison/selection                          | Adapt           |
| Keep architectural commitments traceable to one governing pattern                     | ISO/IEC/IEEE 42010:2022 architecture description discipline                                                                                       | Expressed as explicit governing-pattern assignment and Tell+Cite stubs elsewhere (no competing semantics)                                                                  | Adopt           |

**Notes per row**

1. USCM does not "implement a particular scoring model"; it preserves a stable, admissibility‑gated surface on which such models can be wired.
2. Calibration is treated as a lawful transform family that must live within SCP+CSLC; the kernel does not mandate a specific calibration method.
3. Set‑valued scoring aligns with USCM’s “vector first, scalar by declaration” law, and is naturally consumed by CPM/SelectorMechanism without forcing a spurious total order.
4. Governing-pattern traceability is used here to keep the spec teachable and non-duplicative; it does not add new governance cards or admissibility gates.

### A.19.USCM:12 - Relations

* **Builds on**

  * `A.6.1` (operation declarations and actual application/binding rules).
  * `A.19.CHR:4.2.1` (CHR SlotKind lexicon).
  * `G.0` (CG‑Spec, specifically `SCP` and `MinimalEvidence`).
  * `A.18` (CSLC lawfulness discipline).
  * `C.16` (measurement constitution and scale-lawful operations when measurement is claimed).
  * `A.15.2` for the planned edition/policy baseline; `A.15.3` plus `A.19.CHR:4.7.2` for typed filling of independently declared positions.
  * `A.19.CN` (CN‑Spec, specifically `comparability` routing and normalization‑based comparability expectations).
* **Used by**

  * `A.19.CHR` (suite membership and suite protocols; USCM is the `score` stage).
  * Downstream CHR stages that require score measures as inputs (e.g., `CPM`, `SelectorMechanism`).
  * `E.18` when USCM instances are used as nodes in a selected `TransformationFlowStructure`; the selected `ScoringMethodDescriptionRef@edition(…)` and other pins live in planned baselines (P2W), while executions surface effective refs/pins via `Audit`.
* **Coordinates with**

  * `UNM` when `CN‑Spec.comparability` requires normalization‑based comparability (explicit choreography, no hidden UNM).
  * `ULSAM` when folding/aggregation is needed as a distinct, explicit step.
  * `G.2` and `GPatternExtension` wiring modules for post‑2015 method families, without mutating the USCM kernel.
  * `E.20` (governing-pattern discipline) and `F.18` (alias docking) for governing-source references and designation continuity.

### A.19.USCM:End
