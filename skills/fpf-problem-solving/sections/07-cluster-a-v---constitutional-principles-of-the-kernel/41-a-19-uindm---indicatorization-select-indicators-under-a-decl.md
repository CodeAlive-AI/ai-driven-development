## A.19.UINDM - Indicatorization (UINDM): Select Indicators Under a Declared Policy

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A / CN-Spec cluster (A.19) / CHR mechanism-governing patterns

### A.19.UINDM:0 - At a glance (didactic, informative)

* **Suite stage:** `indicatorize` (ordering lives only in `A.19.CHR:suite_protocols`).
* **Inputs (conceptual):** exact `U.CharacteristicSpaceRef`, `CNSpecRef`, and `IndicatorChoicePolicyRef`, with the bearer, claim scope and selected slices, qualification window, evidence basis, and intended use declared by those editions; when the selected policy is evidence-gated, also supply `CGSpecRef` and, optionally, a `MinimalEvidenceRef` override.
* **Output:** `IndicatorSetSlot` = `S⊆I`, a set of positions in the exact A.19 space declaration's ordered basis I. Each position retains its Characteristic, Scale and meaning. The selection is not a measurement or conversion.
* **Non‑goals:** does **not** normalize, score, compare, aggregate, threshold, publish, or emit telemetry; it only selects a subset under explicit policy.
* **P2W seam:** the A.15.2 baseline records concrete space/spec/policy editions; A.15.3 typed filling applies only to independently declared positions. Actual use retains its effective refs and pins in Audit.
* **Failure mode:** tri‑state guard (`pass|degrade|abstain`); unknown never coerces to `pass`.
* **Quick rule of thumb:** if `CN‑Spec.indicator_policy` is absent → `IndicatorizeEligibility = abstain` (fail‑closed); if the selected policy is evidence‑gated → `CGSpecRef` MUST be available and the effective MinimalEvidence MUST be explicit (override or `CG‑Spec.MinimalEvidence`).

### A.19.UINDM:1 - Problem frame

FPF’s Characterization (CHR) suite treats indicatorization as a **distinct mechanism boundary** within the CHR suite (authoritative membership: `A.19.CHR:4.2`).
Suite membership is a **set** (order has no semantics); any intended ordering is expressed only via `suite_protocols` (`A.19.CHR:4.5`), under the suite obligations (`A.19.CHR:4.3`).

Within the canonical suite‑closed protocol, UINDM appears as the `indicatorize` stage (after `normalize`, before `score/compare/select`; optional stages remain explicitly optional per `suite_protocols`).

UINDM’s job is concept‑level and governed by CN‑Spec and CG‑Spec: it selects an **indicator subset** over an existing `U.CharacteristicSpace` under `CN‑Spec.indicator_policy`, using the suite-wide SlotKind lexicon to prevent SlotKind drift across the CHR mechanism chain and across SoTA wiring modules.
A “subspace view” (if needed) is treated as a **derived support view** over the chosen set (see `A.19.UINDM:4.2`), not as an extra mandatory output of the kernel signature.

### A.19.UINDM:2 - Problem

Engineering teams routinely need to decide “which characteristics count as indicators” for a CN‑frame—before they can score, compare, aggregate, or select. If indicatorization is not given a **first‑class mechanism boundary**, several failure modes emerge:

* **Hidden indicatorization:** downstream mechanisms (scoring/comparison/selection) implicitly decide which characteristics matter, making the CHR pipeline opaque and hard to audit.
* **NCV conflation:** measurability (or “having an NCV”) is treated as sufficient to be an indicator, collapsing the crucial distinction between “measurable characteristic” and “indicator chosen under policy.”
* **Drift and non-determinism:** indicator sets vary between teams, bearer classes, source or corpus editions, windows, and intended uses without stable policy and basis pins, making comparisons and decisions irreproducible.
* **Silent evidence coercion:** missing/unknown evidence is implicitly treated as acceptable (“pass”) or collapsed to an empty set, degrading decision quality without visibility.

### A.19.UINDM:3 - Forces

1. **Policy primacy vs method freedom.** Indicatorization must be governed by explicit `IndicatorChoicePolicy`, while still allowing multiple method families (e.g., theory‑first, invariance‑driven, evidence‑gated) to be wired later without mutating the mechanism’s signature.

2. **Selection‑only vs “semantic alchemy.”** UINDM must not smuggle normalization, scaling, polarity flips, aggregation, or scoring inside “indicator choice.” It is a selection mechanism over the declared characteristic-space basis, not a transformation mechanism.

3. **Declared-use locality vs reuse.** An indicator set is valid for its characteristic-space and CN-Spec editions, bearer, scope and window, evidence basis, policy, and intended use; a later use must recheck those premises and cite any source-local, kind, or plane relation it actually relies on.

4. **Auditability vs authoring overhead.** Engineer‑managers need to see *why* an indicator set was chosen and *which editions/policies* were in effect, but FPF stays conceptual (no data governance, no tool‑enforced metadata). Audit obligations must therefore be minimal yet decisive.

5. **Evolvability vs didactic usability.** CHR mechanisms must remain evolvable (stable slot lexicon; method specifics in SoTA packs / wiring), while the spec must remain teachable: a reader should find UINDM’s purpose, boundary, laws, guard behavior, and audit obligations in one place.

6. **Fail‑closed discipline.** Unknown/insufficient evidence must never be coerced into “pass”; tri‑state guards (`pass|degrade|abstain`) are required to preserve correctness under uncertainty.

7. **P2W separation and gate/guard separation.** UINDM must expose eligibility and audit pins without turning into (i) a WorkPlanning baseline binder or (ii) an admissibility gate:
   planned slot fillings belong to WorkPlanning plan items, while GateDecision/GateLog live in gate patterns / WorkEnactment (suite protocols remain mechanism‑steps only).

### A.19.UINDM:4 - Solution

Resolve the indicator policy against the exact characteristic-space basis and return the selected positions with their Characteristic, Scale and original relative order. Keep their values unchanged. If the policy is absent or an action-changing match remains unresolved, apply the declared abstain behavior. An evidence-gated policy also needs its CG-Spec and effective MinimalEvidence.

Use the operation and guard declarations below for eligibility and actual bindings. Audit keeps the selected editions and the bearer, scope/window, evidence basis and intended use needed for replay. A receiving use adds relation references only for relations it actually relies on. Gate decisions, publication and telemetry follow their own patterns; methods for choosing indicators can be supplied through G.2 and extension declarations.

#### A.19.UINDM:4.1 - Operation declaration (normative)

`UINDM.IntensionRef` cites the exact A.6.1 U.Mechanism declaration episteme presented here. CHR selects that declaration and its edition; its indicatorize stage resolves to the local Indicatorize operation. A changed basis-selection law or eligibility rule requires explicit selection of the changed declaration, while another realizer of the same declaration changes no suite member.

* **Scope note:** A.6.1 governs this declaration's operations, arguments, results, application identities and laws. An A.15.2 plan can select its editions; typed filling under A.15.3 is needed only for an independently declared receiving position. Actual application bindings are governed below. Indicatorization returns S; its guard and audit remain separate from GateDecision/GateLog.
* **IntensionHeader:** `id = UINDM`, `version = 1.0.0`, `status = stable`.
* **IntensionRef:** `UINDM.IntensionRef` (canonical target for the suite member named in `A.19.CHR:4.2`).
* **Tell.** Policy‑bound indicatorization: select an indicator subset over an existing `U.CharacteristicSpace` under `CN‑Spec.indicator_policy`.
* **Purpose:** freeze a policy‑bound indicator subset early so downstream CHR mechanisms can assume a declared indicator profile (or explicitly `degrade/abstain`) rather than silently “choosing indicators” inside scoring/comparison/selection.
* **Imports:** `A.19.CN (CN‑Spec.indicator_policy)`, `A.6.1 (operation declarations and actual bindings)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`, and (when evidence‑gated) `G.0 (CG‑Spec.MinimalEvidence)`.
* **SubjectBlock:**

  * **SubjectKind:** `U.CharacteristicSpace`, supplied by CharacteristicSpaceSlot.
  * **RangedValueKind:** declaration-local basis positions of that space. Indicatorize selects from them; IndicatorizeEligibility assesses their selection under the policy.
  * **SliceBasis:** the declared `U.ClaimScope` and its selected `U.ContextSlice` members, together with the qualification window and intended use.
  * **Input qualification:** indicatorization ranges over the declared characteristic-space basis `CNSpecSlot.cs_basis` (within `CNSpecSlot.chart`) for the exact bearer, claim scope and selected slices, qualification window, evidence basis, and intended use; it never enlarges that basis.
  * Result kinds are declared per operation: a finite basis-position subset and a separate guard judgment.
**Operation-local declarations**

Each argument row declares the same meaning separately for Indicatorize and IndicatorizeEligibility. References identify one exact value and edition under the declaration's effective reference scheme. Cardinalities below are for Indicatorize; the guard can assess a proposal with a missing required argument, which then has no binding and yields abstain.

| Direction | Local designator | Meaning and ValueKind | Designation; cardinality |
| --- | --- | --- | --- |
| Argument | CharacteristicSpaceSlot | U.CharacteristicSpace whose exact basis I supplies the candidate positions, their Characteristic and Scale | CharacteristicSpaceRef; 1 |
| Argument | CNSpecSlot | CN-Spec used to delimit that basis and the bearer, scope/slices, qualification window and intended use | CNSpecRef; 1 |
| Argument | IndicatorChoicePolicySlot | IndicatorChoicePolicy whose rules select positions in I and govern unresolved choices and evidence failure | IndicatorChoicePolicyRef; 1 |
| Argument | CGSpecSlot | CG-Spec supplying evidence conditions when the selected policy is evidence-gated | CGSpecRef; 0..1, required for evidence-gated use |
| Argument | MinimalEvidenceSlot | MinimalEvidence override used instead of CGSpecSlot.MinimalEvidence when supplied in evidence-gated use | MinimalEvidenceRef; 0..1 |
| Indicatorize result | IndicatorSetSlot | Finite subset S of the exact space declaration's basis-position set I | ByValue; 1 on an admitted resolved selection, 0 on abstain |
| IndicatorizeEligibility result | GuardDecision | Policy-governed eligibility judgment: pass, degrade or abstain | ByValue; 1 on completed evaluation |

For each argument, its **bindingPredicate** holds when this application actually uses that resolved value in the stated role: the space supplies I, the CN-Spec delimits the use, the choice policy supplies the selection or eligibility rule, and any evidence arguments supply the effective evidence condition. An unused evidence reference in a non-evidence-gated use creates no binding. For the guard, each required argument has cardinality 0..1 so that missing inputs can be assessed; absent inputs cannot be counted as actual bindings.

The **IndicatorSetSlot bindingPredicate** holds when that Indicatorize application returns S after applying the bound policy to the bound basis under the admitted use; the laws below govern S. The **GuardDecision bindingPredicate** holds when that IndicatorizeEligibility application returns the judgment determined by its stated predicates. A compatible set or guard value copied into an audit entry establishes neither return. A.6.1 identifies each binding by the exact application, local declaration, value and continuous binding extent; input extents are within the selection/evaluation episode and result binding begins at return.

**SlotIndex (derived projection).** The argument/result designators, ValueKinds, designation modes and cardinalities in the table are its sole source. Their historical Slot names support CHR lookup; A.6.5 relation SlotSpecs do not define operation arguments.

* **OperationAlgebra** (suite stage = `indicatorize`, per `A.19.CHR:4.5`; canonical stage‑op = `Indicatorize`):

  * `Indicatorize(CharacteristicSpaceSlot, CNSpecSlot, IndicatorChoicePolicySlot, CGSpecSlot?, MinimalEvidenceSlot?) → IndicatorSetSlot`; the exact space declaration supplies I and each position's Characteristic, Scale and meaning. Resolve any policy stated by Characteristic criteria to positions before returning S. If several positions match, apply the declared choice or all-matches rule; without a resolving rule, return the policy's unresolved/abstain disposition rather than select an arbitrary position.
**ApplicationPredicate.** Indicatorize obtains when a selection episode actually resolves the bound policy against the bound space's basis positions for the CN-Spec use and determines S. It proceeds on pass, or on degrade only when that policy permits a degraded selection; abstain yields no S. IndicatorizeEligibility obtains when a separate evaluation episode assesses those inputs under the eligibility predicates and determines its GuardDecision. A planned choice or a passing guard is not an Indicatorize episode.

**ApplicationIdentityRule.** Each operation's occurrence is one selection or eligibility-evaluation invocation at its calculation locus, starting when it takes up its arguments and ending at return or termination. Two references to that same episode identify one application. Taking up the same values and policy for a second calculation identifies another, even when both return the same S or judgment. Replacing the input basis or policy for a fresh calculation likewise begins another application; a mere copied result begins none.

**ApplicationExtentRule.** Indicatorize extends from taking up the basis/policy for selection through return of S or termination without S; IndicatorizeEligibility extends from taking up the proposal for assessment through judgment or termination. An unfinished episode has an open extent and no unreturned result binding. These are the actual calculation extents, which can differ from the selected data window. An invocation reference designates that episode only when its identity is established; no U.Work claim follows from ordinary selection or projection mathematics.

For example, select Celsius temperature twice from CS7 under the same policy in §5.4. Each completed selection returns {i1}, but the two operand-to-return episodes and their result bindings are distinct. An audit record copied from the first episode can describe its result; it cannot establish a result binding for the second without the second return. Re-reading the first record also creates no new selection application.

* **LawSet** (CHR‑lawful indicatorization):

  1. **Selection‑only:** `Indicatorize` MUST NOT alter units, scales, and polarities; it only selects a subset (no implicit `UNM`).
  2. **Declared-basis restriction:** return `S⊆I` for the exact A.19 basis identified by the space and CN-Spec editions. The projection `x|_S` retains the selected positions' original relative order, Characteristic, Scale and meaning. Re-resolve the policy after a basis change; naked indices from the preceding declaration do not identify positions in the new one.
  3. **No implicit NCV⇒indicator:** measurability/NCV is not sufficient; indicators exist only via `IndicatorChoicePolicySlot` (cites `A.19.CN` `indicator_policy`).
  4. **Edition-determinism for the declared use:** for fixed editions of all **ByRef** inputs (`CharacteristicSpaceRef`, `CNSpecRef`, `IndicatorChoicePolicyRef`, and—when evidence-gated—`CGSpecRef` plus optional `MinimalEvidenceRef`) and fixed bearer, claim scope and selected slices, qualification window, evidence basis, and intended use, the `IndicatorSetSlot` result is stable.
  5. **No silent evidence coercion:** if evidence is insufficient/unknown under the chosen policy, the result MUST NOT be “silently emptied” nor silently treated as “pass”; use tri‑state guards.
* **AdmissibilityConditions** (tri‑state guard; fail‑closed on missing admissibility/evidence):

  * `IndicatorizeEligibility(CharacteristicSpaceSlot, CNSpecSlot, IndicatorChoicePolicySlot, CGSpecSlot?, MinimalEvidenceSlot?) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires: (i) `CNSpecSlot.indicator_policy` is present, (ii) `IndicatorChoicePolicySlot` matches that policy reference and edition, (iii) `CharacteristicSpaceSlot` matches the declared characteristic-space basis, and (iv) that policy's eligibility conditions hold for the exact bearer, claim scope and selected slices, qualification window, evidence basis, and intended use.
  * If the chosen `IndicatorChoicePolicy` is evidence‑gated:
    (i) `CGSpecSlot` MUST be present,
    (ii) define `EffectiveMinimalEvidence := (MinimalEvidenceSlot if present, else CGSpecSlot.MinimalEvidence)`,
    and (iii) insufficient/unknown evidence MUST yield `degrade` or `abstain` per the **effective** failure‑behavior policy (never a silent `pass`).
  * If the chosen `IndicatorChoicePolicy` is **not** evidence‑gated, absence of `MinimalEvidenceSlot` MUST NOT affect eligibility; no accidental “always‑evidence‑gated” behavior is permitted.
* **Applicability:**
  * Intended to be used before any scoring/comparison/selection that assumes an indicator profile, while remaining a distinct step (no hidden indicatorization inside downstream mechanisms).
  * Reuse for another bearer, source-local meaning, scope and window, evidence basis, reference plane, or intended use requires a new eligibility decision. Cite an F.9 Bridge, kind relation, or plane relation only when the new use actually relies on it.
  * Pin‑binding note: choosing concrete policy editions/pins is a planned baseline concern (P2W); UINDM only consumes those refs and records the effective ones in `Audit`.
* **Relation boundary:** indicatorization creates no transfer relation. When a receiving use relies on an obtaining F.9 Bridge, kind relation, or plane relation, cite it with direction, preserved or lost meaning, and receiving use; supported penalties route to **`R_eff` only**.
* **Γ_timePolicy:** `point` by default (no implicit “latest”).
* **PlaneRegime:** the indicator set keeps the reference plane declared by the characteristic-space and CN-Spec editions; UINDM introduces no plane shift.
  When a receiving conclusion depends on a relation between different planes, cite that exact plane relation, its direction and loss, and keep its use separate from the indicator set.
* **Audit:**

  * MUST record: `CharacteristicSpaceRef.edition`, `CNSpecRef.edition`, `IndicatorChoicePolicyRef.edition`, exact bearer, claim scope and selected slices, qualification window, evidence basis, and intended use.
  * When evidence‑gated, MUST record: `CGSpecRef.edition` and effective MinimalEvidence (`MinimalEvidenceRef` when provided; otherwise `CGSpecSlot.MinimalEvidence`).
  * SHOULD record: the realized `GuardDecision` (`pass|degrade|abstain`) and, when non‑`pass`, the policy‑bound failure behavior reference that justified it.
  * SHOULD record: a stable description of `IndicatorSetSlot` (or an id reference to a **citable** indicator-set publication unit), plus any F.9 Bridge, kind relation, or plane relation only when the result or receiving use actually relies on it.

#### A.19.UINDM:4.2 - Interpretation notes (informative)

* **IndicatorSet selects basis positions.** A Characteristic reference can match several positions with different Scales. S identifies the selected positions in the exact space declaration; each resolves uniquely through that basis. Obtain or reuse their values under the corresponding measurement/evaluation rule and retain the position and Scale in the profile. UINDM computes no measurement or conversion.

* **Subspace views are derived, not mandatory.** If a project needs an explicit subspace view, treat it as a derived support view `CS|_S`, with `S = IndicatorSetSlot` over the exact base `CS = CharacteristicSpaceSlot`. Restrict its ordered basis and any state `x|_S` to S without reordering the retained positions. Do not add a new mandatory output to the kernel signature; model a first-class subspace support view via `⊑⁺` only when it is genuinely needed.

* **Justification is optional and externalized.** The CHR SlotKind lexicon includes `JustificationSlot`, but the canonical UINDM intension does not require it.
  If a project needs a first‑class justification output, treat it as an **extension** (`⊑⁺`) rather than by mutating the base `Indicatorize` signature,
  and model the justification as a justification `U.Episteme` (e.g., `JustificationSlot : ⟨ValueKind = U.Episteme, refMode = U.EpistemeRef⟩`).

* **Evidence-gated indicatorization is explicit.** Evidence gating is activated only by the chosen `IndicatorChoicePolicy`. In that case `CGSpecSlot` is required and the effective MinimalEvidence is explicit: use `MinimalEvidenceSlot` when supplied, otherwise `CGSpecSlot.MinimalEvidence`. The override remains optional.

### A.19.UINDM:5 - Archetypal Grounding (informative)

#### A.19.UINDM:5.1 - Tell

Think of UINDM as a **policy‑bound projection**:

* Input: “the declared characteristic basis for this exact bearer, claim scope and selected slices, qualification window, evidence basis, and intended use, plus an explicit indicator choice policy”
* Output: “the selected positions of this exact basis, each retaining its Characteristic, Scale and meaning for downstream use”

The key didactic boundary is: **UINDM chooses coordinates; it does not alter coordinates.**

#### A.19.UINDM:5.2 - Show (U.System) — cross‑unit engineering dashboard

A program manager maintains a `U.CharacteristicSpace` for manufacturing sites, including ~30 characteristics (quality, safety, cost, throughput, sustainability).

* The CN‑Spec’s `indicator_policy` for the “weekly executive dashboard” selects a subset:
  `{DefectRate, IncidentRate, UnitCost, LeadTime, EnergyPerUnit, OnTimeDelivery}`.
* In this example each named Characteristic has one basis position. UINDM resolves the six names to those exact positions and returns S; each position retains its original Scale.
* One site lacks reliable incident reporting for the last week. The indicator policy is evidence‑gated; `IndicatorizeEligibility` returns `degrade` (not `pass`), and the audit records the effective MinimalEvidence and the edition pins used.

Downstream mechanisms can now be held to the invariant: **they may only score/compare/select using the declared indicator profile (or explicitly abstain/degrade).** This avoids “dashboard drift” where different teams silently score on different subsets.

#### A.19.UINDM:5.3 - Show (U.Episteme) — robust evaluation across environments

A research lead wants indicators for model robustness under distribution shift (different hospitals, sensors, geographies).

* The declared characteristic-space basis includes many candidate metrics (accuracy slices, calibration, subgroup error, OOD detection quality).
* The indicator choice policy is “invariance‑driven”: prefer indicators whose semantics remain stable under environment changes; deprioritize proxy metrics known to be environment‑sensitive.
* UINDM returns an indicator set used by the scoring and comparison stages; uncertain indicators are handled via tri‑state guarding rather than coerced to zero or silently dropped.

#### A.19.UINDM:5.4 - One Characteristic at two Scale positions

Let the exact space declaration `CS7` have ordered positions `i1=(Temperature, Celsius)` and `i2=(Temperature, kelvin)`, followed by an unrelated cost position. A state contains `x_i1=20 °C` and `x_i2=293.15 K`. The policy “select Celsius temperature” returns `S={i1}`. The explicit all-matches policy “all Temperature positions” returns `{i1,i2}`, with `x|_S` in the original order and both Scale meanings retained. UINDM converts neither value.

For the first policy, a separately admitted USCM scoring use can read the Celsius value under its declared method `g_C(c)=(c-0)/(40-0)` on Celsius interval `[0,40]`, returning `0.5` at 20. The interval endpoints are part of this illustrative scoring declaration. Supplying 293.15 as though it were Celsius violates that method's input basis; a TemperatureRef alone would not reveal the error. All-matches selection requires a receiving method that accepts those two Scale-specific positions, or a narrower selection; it is not a universal default.

Suppose a new declaration `CS8` reverses these two positions. Resolving “Celsius temperature” now selects its CS8-local position i2. Reusing CS7's naked integer 1 would select kelvin and is invalid. If the policy merely says “Temperature” and supplies no rule for the two matches, return its unresolved/abstain disposition. A missing indicator policy retains the defined abstain result, and evidence gating still applies only when the selected policy requires it.

### A.19.UINDM:6 - Bias-Annotation (informative)

* **Gov (governance).** Bias toward explicit policy surfaces (`IndicatorChoicePolicyRef`, edition pins, auditable outcomes) rather than tacit “expert choice.” Risk: perceived extra work. Mitigation: keep the mechanism minimal (selection‑only) and push method detail into wiring modules.

* **Arch (architecture).** Bias toward stable interfaces: SlotKind tokens come from the suite lexicon and evidence gates are explicit inputs. Risk: reduced “quick hacks.” Mitigation: allow `⊑⁺` extensions for richer outputs (e.g., justification) without mutating the kernel signature.

* **Onto/Epist.** Bias toward a strict distinction between “measurable characteristic” and “indicator under policy.” Risk: teams accustomed to “everything measurable is an indicator” may resist. Mitigation: embed this as an explicit LawSet clause (“No implicit NCV⇒indicator”).

* **Prag (pragmatics).** Bias toward fail‑closed guards and traceability under uncertainty. Risk: more `abstain/degrade` outcomes early. Mitigation: couple `degrade` with explicit downstream behaviors (policy‑bound) rather than silent coercions.

* **Did (didactics).** Bias toward “one place to learn the mechanism”: the problem/forces/solution narrative is co‑located with the operation declaration.

### A.19.UINDM:7 - Conformance Checklist

A UINDM publication or use is conformant if it satisfies:

1. **A.6.1 declaration completeness.** Indicatorize and the separately reused IndicatorizeEligibility have local argument/result declarations, obtaining predicates and application identity/extent rules. Their declared selection and guard laws hold; SlotIndex projects those declarations. An actual binding requires the value used or returned by the identified application, not a compatible audit record.

2. **SlotKind discipline.** SlotKind tokens match the CHR SlotKind lexicon for the roles used (`CharacteristicSpaceSlot`, `CNSpecSlot`, `IndicatorChoicePolicySlot`, etc.); no generic `ContextSlot` is introduced. New SlotKinds, if any, first extend the suite lexicon rather than appearing ad hoc in the mechanism.

3. **Selection-only behavior.** `Indicatorize` returns positions in the exact declared basis, retaining their Characteristic, Scale and meaning. A projected state keeps their original relative order. There is no implicit normalization or enlargement. After a basis change, resolve the policy again rather than reuse naked indices.

4. **No NCV shortcut.** “Measurable/NCV” is not treated as sufficient for indicatorhood; indicatorhood arises only via `IndicatorChoicePolicySlot` consistent with `CN‑Spec.indicator_policy`.

5. **Evidence gating is explicit.** When the chosen `IndicatorChoicePolicy` is evidence‑gated, `CGSpecSlot` is present and the effective MinimalEvidence is explicit and auditable
   (`MinimalEvidenceSlot` when provided; otherwise `CGSpecSlot.MinimalEvidence`); insufficient/unknown evidence must yield `degrade/abstain` per the effective failure‑behavior policy, never a silent `pass`.

6. **Reuse is explicit.** Another bearer, scope and window, basis, plane, or intended use gets a fresh eligibility decision; any F.9 Bridge, kind relation, or plane relation is cited only when the conclusion relies on that obtaining relation, with supported loss routed to `R_eff`.

7. **Gate/guard separation + lexeme discipline.** UINDM uses `…Eligibility` returning `GuardDecision ∈ {pass|degrade|abstain}` and does not embed GateDecision/GateLog in suite steps.
   Reserved gate‑lexemes (e.g., `…Guard`) are not used for mechanism‑level predicates; the mechanism stays at the guard/admissibility layer.

8. **Planning and actual use.** An A.15.2 WorkPlan selects the intended editions; A.15.3 governs typed filling only for independently declared positions. Record the actual application and its effective bindings under §4.1, keeping the refs and pins needed for replay in Audit.

9. **Extension discipline (if extended).** A proposed UINDM specialization MUST preserve the inherited SlotKind designators and their meanings, add no mandatory input to Indicatorize, and declare any additional output or operation explicitly (the local extension notation is ⊑⁺). A refinement, conservative-extension or equivalence claim additionally uses its own A.6.1 §4.8 preservation test and exact comparison predicate; those three claims are not interchangeable. Preserve inherited application/binding meanings, identity and extent to the degree required by the claimed comparison, and retain narrowed applicability or stronger conditions explicitly. A missing comparison predicate or substrate returns the applicable A.6.RCD gap.

For example, an extended Indicatorize may add an optional justification result while retaining the original inputs and selected-position result. To claim a conservative extension, establish that every inherited admitted use, result and application/binding rule remains as specified; the new output has its own declaration. Making a new explanation input mandatory fails the local restriction. A label such as ⊑⁺ does not settle the comparison: use the admitted comparison relation or A.6.RCD's case-specific claim branch under A.6.1 §4.8, returning its exact missing-governor/substrate gap if necessary.

### A.19.UINDM:8 - Common Anti‑Patterns and How to Avoid Them

* **“NCV ⇒ indicator.”** Treating all measurable characteristics as indicators. Violates “No implicit NCV⇒indicator.”

* **Indicatorization hidden in scoring.** A scoring method silently ignores some characteristics or introduces an implicit “feature selection” without an explicit indicator set.

* **Characteristic reference substituted for a position.** Temperature occurs at Celsius and kelvin positions, but the returned set contains only TemperatureRef. Resolve the policy to the requested position or its explicitly selected all-matches set before returning S.

* **Silent emptying.** When evidence is insufficient, returning an empty indicator set (or treating missing evidence as “pass”) without a tri‑state guard decision.

* **Reusing an indicator set after its basis or use changed.** Reusing it for another bearer, scope and window, evidence basis, reference plane, or intended use without a new eligibility decision; or naming Bridge or plane-relation pins without an actual obtaining relation.

* **Smuggling plan‑binding into the mechanism.** Binding concrete edition pins / planned slot fillings (“launch values”) inside the UINDM description instead of using the P2W seam (WorkPlanning) and recording only effective refs/pins in `Audit`.

* **GateDecision leakage.** Emitting or implying GateDecision/GateLog as part of the `indicatorize` step (gate decisions are separated from suite steps; keep UINDM at guard+audit level).

### A.19.UINDM:9 - Consequences

**Benefits**

* Makes “which characteristics count as indicators” explicit, auditable, and policy‑bound.
* Prevents downstream semantic drift by freezing an indicator subset early in the CHR pipeline.
* Improves reproducibility via edition‑determinism (fixed editions ⇒ stable result).
* Preserves evolvability: new indicator selection method families can be added via wiring (packs/extensions) without changing the mechanism’s intension.

**Costs / trade‑offs**

* Adds an explicit step (and explicit policy work) before scoring/comparison.
* Strict fail‑closed behavior can increase early `degrade/abstain` outcomes until evidence and policies are properly specified.

### A.19.UINDM:10 - Rationale

Indicatorization is separated because it is a different kind of commitment than scoring or comparison:

* Indicatorization commits to **which coordinates are allowed to matter** under policy.
* Scoring/aggregation/comparison commit to **how** allowed coordinates are transformed, folded, or ordered under admissibility gates.

By making indicatorization selection‑only, UINDM avoids “semantic alchemy” (changing meanings while claiming to merely “pick indicators”) and supports the CHR suite’s broader discipline: explicit spec refs, explicit crossings, and explicit handling of uncertainty via tri‑state guards.

### A.19.UINDM:11 - SoTA-Echoing — choose indicators for their intended use

**Practice question.** Which coordinates should a dashboard or receiving method use when several available columns are plausible indicators? The selected line makes the phenomenon and intended use govern an explicit choice policy, then checks the selected positions and their Scale meanings. A serious alternative ranks available features by a statistical score and keeps the best k. That alternative is useful for its declared predictive or exploratory objective; its ranking alone does not decide which quantities a particular dashboard must report.

The European Commission JRC's [10 Step Guide, steps 1–2](https://knowledge4policy.ec.europa.eu/composite-indicators/toolkit_en/navigation-page/10-step-guide_en), published as a navigation guide in March 2025, supplies the purpose-led line for composite indicators: define the conceptual basis and choose relevant, analytically sound, obtainable indicators. **Adapt** that ordering to `CN-Spec.indicator_policy`, the IndicatorChoicePolicy argument in §4.1 and the selection-only law. UINDM selects existing coordinates; the guide's later normalization, weighting and aggregation steps belong to their separately declared mechanisms. The guide does not prove that any particular policy is adequate or stable under distribution shift.

The [scikit-learn SelectKBest documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html) supplies the concrete statistical alternative: choose k features using a declared scoring function; equal scores can be resolved in an unspecified way. **Adopt** statistical selection when the intended use actually chooses that criterion, with the data, scoring rule and treatment of ties declared in the policy. **Reject** substituting a top-k result for an undeclared semantic choice. The documentation establishes the selector's behavior, not the meaning or fitness of the selected indicators.

The two Temperature positions in §5.4 expose the distinction. Suppose the Celsius and kelvin columns receive equal statistical scores and k=1. Either could be retained under an unspecified tie rule, while the downstream Celsius scoring method accepts only the Celsius position. At comparable effort, the explicit Celsius policy resolves the required input directly; when prediction is the real objective, the statistical policy can instead choose a position and bind its actual Scale to an appropriate receiving method. This changes checklist items 3–4 in §7: retain the exact selected position, and resolve an action-changing tie by the policy or return its unresolved result. A promise that both columns concern Temperature is insufficient.

The trade-off is deliberate: a purpose-led policy makes the required indicator meaning inspectable, but it does not by itself optimize prediction. A statistical policy needs data and a justified score, and its selected subset can vary with them. Neither approach permits UINDM to silently rescale values. Reopen the comparison when the receiving question changes, evidence shows that the selected indicators fail that question, or a rival policy preserves the needed meaning with better usefulness at comparable effort.

### A.19.UINDM:12 - Relations

* **Builds on**

  * `A.19.CN` (CN‑Spec, specifically `indicator_policy`).
  * `A.6.1 §4.2` for operation-local declarations and `§4.8` for the exact refinement, conservative-extension or equivalence comparison being claimed.
  * `A.19.CHR:4.2.1` (CHR SlotKind lexicon).
* **Used by**

  * `A.19.CHR` (suite membership and suite protocols; UINDM is the `indicatorize` stage).
* **Coordinates with**

  * `G.0` (CG‑Spec / MinimalEvidence) when indicator choice is evidence‑gated.
  * `E.20` for the governing declaration and `F.18` when resolving a legacy alias.

### A.19.UINDM:End
