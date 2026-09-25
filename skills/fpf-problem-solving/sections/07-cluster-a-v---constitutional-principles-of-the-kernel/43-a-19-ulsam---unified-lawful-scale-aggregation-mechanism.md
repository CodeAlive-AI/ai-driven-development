## A.19.ULSAM - Unified Lawful Scale Aggregation Mechanism (ULSAM)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)

`ULSAM.IntensionRef` identifies the exact `U.Mechanism` declaration in §4.1 under A.6.1. CHR resolves its optional fold_Γ? stage to the local Fold_Γ operation; the declaration supplies the meanings and actual application/binding rules below.

### A.19.ULSAM:0 - At a glance (didactic, informative)

* **Suite stage:** `fold_Γ?` (ordering lives only in `A.19.CHR:suite_protocols`; `mechanisms[]` membership is a set, not an order).
* **Input surface:** an admitted `MeasureSetSlot`, `CNSpecSlot`, `CGSpecSlot`, and `GammaFoldSlot`, with the grouping or membership basis, fold and policy editions, claim scope and selected slices, qualification window, evidence basis, contributors, and intended result declared by those inputs; `MinimalEvidenceSlot?` may override the CG-Spec minimum.
* **Output surface:** `AggregatedMeasureSlot` (+ optional `ContributorSetSlot?` as an explanation surface).
* **Non‑goals:** no scoring, no comparison, no selection, no “method catalog”, no hidden defaults, no hidden thresholds.
* **P2W seam:** an A.15.2 baseline selects the fold, evidence policy and their editions. A.15.3 typed filling applies only to independently declared receiving positions under the CHR P2W hook. Actual fold arguments bind under §4.1; a planned value does not establish that binding.
* **Failure mode:** tri‑state guard `GuardDecision := {pass|degrade|abstain}`; unknown/insufficient evidence never coerces to “pass”.
* **Rule of thumb:** if you are about to “average/sum/roll up”, you probably need an explicit ULSAM `Fold_Γ` stage (or a justified decision to *not* fold).

**What this mechanism is.** `ULSAM` is the CHR mechanism that makes **aggregation explicit**: it performs an explicit **Γ‑fold** over a set of **admitted measures**, producing an **aggregated measure** (and optionally a contributor surface) under **declared admissibility**.

**What this mechanism is not.**
- It is **not** a scoring method (that is `USCM`).
- It is **not** a comparison mechanism (that is `CPM`).
- It is **not** a selection mechanism (that is `SelectorMechanism`).
- It is **not** a “method catalog”: method specifics belong to SoTA packs and wiring (`G.*:Ext.*`), not here.
- It is **not** a place to hide defaults (“implementation default fold”) or hidden thresholds.

**When you need ULSAM.**
- You want to “roll up” multiple measures into one measure (e.g., an overall reliability/assurance coordinate, a single aggregated risk measure, an aggregate score coordinate).
- You need the fold to be **auditable** (what contributed; what was excluded by evidence/admissibility).
- You need the fold to be **scale-lawful** (no ordinal arithmetic; no illegal mixing of units).
- You need the fold to be **policy-bound and edition-stable** (replayability and pin traceability).

**Choosing the fold.** If the law for the intended result or a required property is unresolved, use A.9 or reuse a sufficient domain result. When the result selects a fold, its law and conditions supply the basis for the explicit fold reference; ULSAM still governs admission of the measures, scale lawfulness and the actual mechanism operation.

**Where it sits in CHR.**
- In the CHR suite protocol, ULSAM corresponds to the optional stage `fold_Γ?` (i.e., **explicitly optional** and never hidden inside `score/compare/select`).

**60‑second script for engineer-managers.**
> "If you're about to average, sum, or otherwise compress multiple measures into one, stop. Ask: (i) do we have a declared Γ‑fold policy and SCP admissibility, (ii) are the measures admissible and scale-compatible, (iii) what do we do if evidence is missing? If you cannot answer with explicit pins/refs, you are not folding -- you are smuggling an assumption. Use ULSAM's `Fold_Γ`, record the effective Γ‑fold and contributor set, and keep the fold as an explicit step."

### A.19.ULSAM:1 - Problem frame (normative)

Within CHR, teams frequently need an **explicit aggregation step** (Γ‑fold) to produce an aggregated measure that is later consumed by comparison and/or selection. Without a dedicated mechanism boundary, aggregation tends to:
- leak into scoring (“the score function also averages everything”),
- leak into selection (“the selector silently computes a scalar”),
- become an “implementation default” rather than a declared policy,
- violate scale lawfulness (especially via ordinal arithmetic or unit-mixing),
- become unauditable (“what exactly got folded, and under what evidence posture?”).

### A.19.ULSAM:2 - Problem (normative)

How do we define an aggregation step that:
1) is **explicit** (separate from scoring/comparison/selection),
2) is **scale-lawful** and admissibility-gated (`CSLC` + `CG-Spec.SCP`),
3) is **Γ‑fold-policy-bound** (`CG‑Spec.Γ_fold` or explicit override),
4) is **evidence-gated** with tri‑state guards (no `unknown → 0/false` coercions),
5) is **auditable** (editions, effective fold, contributor surface),
6) preserves **kernel stability** while allowing SoTA evolution via wiring,
7) remains **didactically readable** (one governing pattern; no scavenger hunt).

### A.19.ULSAM:3 - Forces (normative)

- **Lawfulness vs convenience.** The most “convenient” aggregation (e.g., weighted sums) is often illegal across scales/units; lawful folds require explicit constraints.
- **Explicitness vs brevity.** A single scalar is short to discuss, but expensive in hidden assumptions.
- **Kernel stability vs method evolution.** Aggregation methods evolve; the kernel must not.
- **Evidence gating vs “always return a number.”** The mechanism must support abstain/degrade rather than coercion.
- **Optional stage vs pipeline clarity.** `fold_Γ?` is optional in CHR protocols; optionality must be explicit (not implicit “sometimes scoring folds”).
- **Auditability vs minimal overhead.** Recording contributor sets and effective pins adds overhead but prevents semantic drift.
- **Declared-set locality vs reuse.** A fold is valid for one admitted measure set, grouping or membership basis, policy editions, scope and window, evidence basis, contributors, and intended result; a later use must recheck those premises and cite any relation it actually relies on.
- **P2W separation and gate/guard separation.** ULSAM must expose eligibility and audit pins without turning into (i) a WorkPlanning baseline binder or (ii) an admissibility gate: planned slot fillings belong to WorkPlanning plan items, while GateDecision/GateLog live in gate patterns / WorkEnactment (suite protocols remain mechanism-steps only).

### A.19.ULSAM:4 - Solution (normative)

ULSAM is the **canonical scale‑aggregation mechanism** in the CHR suite. It defines:
* a stable **mechanism boundary** (`fold_Γ?` is a stage with its own operation and eligibility predicate),
* a stable **SlotKind surface** (via the suite lexicon),
* a **tri‑state admissibility guard** (fail‑closed on missing admissibility/evidence),
* and an **audit minimum** (admitted set and membership basis, fold and policy editions, scope and window, evidence, contributors, result, and any relation actually used).

Method semantics (“which aggregation family to use”) remain out of suite core: they belong in SoTA packs (`G.2`) and wiring‑only extension modules (`GPatternExtension` blocks), while ULSAM remains the stable mechanism boundary.

#### A.19.ULSAM:4.1 - Operation declaration (normative)

`ULSAM.IntensionRef` cites this exact A.6.1 U.Mechanism declaration episteme. CHR resolves its fold stage to the local Fold_Γ operation. A changed argument, fold law or guard requires explicit selection of that changed declaration; another realizer of the same declaration changes no suite member.

* **Scope note:** A.6.1 governs the operation and its actual bindings below. A planned baseline selects the fold and specification editions; typed filling is conditional on an independently declared receiving position. Fold_Γ returns the aggregate and any declared contributor set. Eligibility, Audit, GateDecision/GateLog and publication retain their separate meanings.

* **IntensionHeader:** `id = ULSAM`, `version = 1.0.0`, `status = stable`.
* **IntensionRef:** `ULSAM.IntensionRef` (canonical target for the suite member named in `A.19.CHR:4.2`).
* **Tell.** Explicit **Γ‑fold** over admitted measures — no hidden aggregation inside scoring/comparison/selection.
* **Purpose:** explicit **Γ‑fold** (and, when declared, time‑fold) over admitted measures — no hidden aggregation inside scoring/selection.
* **Imports:** `G.0 (CG‑Spec.Γ_fold, CG‑Spec.SCP, CG‑Spec.MinimalEvidence)`, `A.18 (CSLC)`, `A.19.CN (CN‑Spec.acceptance + aggregation routing)`, `A.6.1 (operation declarations and actual bindings)`, `B.3 (justified quantity and dependency model for any R_eff fold)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`.

* **SubjectBlock:**
  * **SubjectKind:** `U.Measure`, supplied by the members of MeasureSetSlot.
  * **RangedValueKind:** `U.Measure`; Fold_Γ aggregates the admitted measures, and FoldEligibility_Γ assesses that proposed aggregation.
  * **SliceBasis:** the declared `U.ClaimScope` and selected `U.ContextSlice` members, together with the qualification window and intended result use.
  * **Input qualification:** aggregation ranges over the admitted measure set and its declared grouping or membership basis, scope and window, evidence basis, contributors, and intended result; `CNSpecSlot.acceptance` routes admission while `CG-Spec.Γ_fold` and `CG-Spec.SCP` govern admissibility.
  * Results are operation-local: aggregate, optional contributors and separate eligibility judgment.

**Operation-local argument and result declarations**

Each input is declared separately for Fold_Γ and FoldEligibility_Γ. References resolve to one exact value and edition. Cardinalities shown are for Fold_Γ; the guard may assess an incomplete proposal with 0..1 of each otherwise required input. A missing value has no argument binding and invokes the corresponding abstain condition.

| Direction | Local designator | Meaning and ValueKind | Designation; cardinality |
| --- | --- | --- | --- |
| Argument | MeasureSetSlot | Set of U.Measure values offered for aggregation, with its grouping or membership basis | ByValue; 1 set |
| Argument | CNSpecSlot | CN-Spec whose acceptance conditions delimit the admitted portion, scope/window and intended aggregate use | CNSpecRef; 1 |
| Argument | CGSpecSlot | CG-Spec supplying SCP, the declared fold and default evidence conditions | CGSpecRef; 1 |
| Argument | GammaFoldSlot | ΓFold actually selected through CGSpecSlot.Γ_fold or an explicit admitted override | ΓFoldRef; 1 |
| Argument | MinimalEvidenceSlot | MinimalEvidence override used in place of CGSpecSlot.MinimalEvidence | MinimalEvidenceRef; 0..1 |
| Fold_Γ result | AggregatedMeasureSlot | U.Measure returned by applying the effective fold to its admitted contributors | ByValue; 1 on completed admitted folding, 0 without a result |
| Fold_Γ result | ContributorSetSlot | Set of U.Measure values actually used as contributors to that aggregate | ByValue; 0..1 set, optional |
| FoldEligibility_Γ result | GuardDecision | Eligibility judgment under the predicates below: pass, degrade or abstain | ByValue; 1 on completed evaluation |

An argument's **bindingPredicate** holds when that application uses the resolved value in the row's stated role: as offered measures, acceptance/use conditions, fold/admissibility declaration or evidence override. The AggregatedMeasureSlot **bindingPredicate** holds when that Fold_Γ application returns the measure it computes using its bound effective fold and admitted contributors. The ContributorSetSlot binding holds only when the same application also returns that actual contributor set; Law 5 requires both its subset condition and equality of the aggregate to the effective fold of that subset. An omitted contributor result creates no contributor binding. The guard result binds when that FoldEligibility_Γ evaluation returns its determined judgment. A.6.1 governs binding identity and maximal continuous extent within the application, with result binding beginning at return.

**SlotIndex (derived projection).** Project the local designators, ValueKinds, designation modes and cardinalities above. Historical Slot names support CHR lookup; A.6.5 relation SlotSpecs add no operation meanings. The optional FoldTime_Γ extension is not a base operation or a prerequisite of ordinary folding.

* **OperationAlgebra** (suite stage = `fold_Γ?`, per `A.19.CHR:4.5`; canonical stage‑op = `Fold_Γ`):
  * `Fold_Γ(MeasureSetSlot, CNSpecSlot, CGSpecSlot, GammaFoldSlot, MinimalEvidenceSlot?) → (AggregatedMeasureSlot, ContributorSetSlot?)`; the cited inputs supply the set, grouping and use qualifications.

**ApplicationPredicate.** Fold_Γ obtains when a calculation actually applies the resolved effective fold to the admitted contributors selected from the bound measure set under the bound acceptance/use conditions. It proceeds on pass or an explicitly permitted degrade branch; abstain produces no folding result. FoldEligibility_Γ obtains when an evaluation actually assesses the proposed set, fold and conditions under the guard predicates and returns its judgment. Numerical equality to a lawful fold and a passing guard alone establish neither calculation nor its result binding.

**ApplicationIdentityRule.** One Fold_Γ occurrence is one aggregation invocation at its calculation locus, from taking up the admitted operands/fold to return or termination. One FoldEligibility_Γ occurrence is one corresponding proposal-evaluation invocation. A second invocation remains distinct even when every measure, contributor, fold, policy, qualification window and returned value is equal. Several references to the same established invocation identify one application; creating another reference or copying its result creates none.

**ApplicationExtentRule.** The fold extends from actual use of its operands and rule through aggregate/contributor return or termination. The guard extends from actual proposal assessment through judgment or termination. An unfinished invocation has an open extent and no unreturned result binding. A time window qualifying the measures or an explicitly declared time-fold does not supply the occurrence interval of the calculation that processes them. Ordinary folding mathematics needs no asserted dated U.Work.

For example, two separate lawful sums of admitted 2 kg and 3 kg measurements under the same fold, grouping and policy both return 5 kg, with contributor set {2 kg, 3 kg} if requested. Law 5 holds for both contents. The first and second operand-to-return episodes nevertheless supply different aggregate/contributor bindings. A copied pair (5 kg, {2 kg, 3 kg}) is not evidence of another performed sum; two descriptions of the first sum still describe one application.

* **LawSet** (minimum; explicit, scale‑lawful folding only):
  1. **No hidden aggregation:** any Γ‑fold MUST be explicit as `Fold_Γ` (no folding hidden inside `Score/Compare/Select`).
  2. **Scale‑lawfulness:** aggregation MUST be CSLC‑lawful and admissible under `CGSpecSlot.SCP`; ordinal arithmetic (e.g., means on ordinal ranks) is forbidden unless explicitly allowed by the relevant CSLC fragment.
  3. **Γ‑fold admissibility:** `GammaFoldSlot` MUST resolve to either `CGSpecSlot.Γ_fold` or an explicitly pinned override (CAL policy) -- never an implicit "implementation default".
  4. **Evidence‑gated folding:** if evidence is insufficient/unknown, folding MUST follow tri‑state guard behavior and MUST NOT silently coerce.
  5. **Contributor accountability (when produced):** when `ContributorSetSlot?` is produced, it MUST be a subset of the admitted portion of `MeasureSetSlot`, and `AggregatedMeasureSlot` MUST be the result of applying the effective Γ‑fold to that contributor subset (no “hidden contributors”).
  6. **No implicit UNM:** ULSAM MUST NOT silently normalize/rescale to “force comparability.” If establishing a compare‑on‑invariants surface requires UNM for the measures being folded, UNM MUST appear as an explicit stage (Uses + pins) upstream; ULSAM itself remains folding‑only.

* **AdmissibilityConditions** (tri‑state guard; fail‑closed on missing admissibility/evidence):
  * `FoldEligibility_Γ(MeasureSetSlot, CNSpecSlot, CGSpecSlot, GammaFoldSlot, MinimalEvidenceSlot?) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires: (i) `CGSpecSlot` provides `SCP` and `Γ_fold`, (ii) `GammaFoldSlot` resolves to the admitted fold or an explicit override, (iii) the measure set and its grouping or membership basis are admitted by `CNSpecSlot.acceptance`, (iv) scope, window, evidence, contributors, and intended result are recoverable, and (v) the set is scale-compatible for that fold.
  * Define `EffectiveMinimalEvidence := (MinimalEvidenceSlot if present, else CGSpecSlot.MinimalEvidence)`; the guard MUST evaluate evidence against `EffectiveMinimalEvidence`.
  * If evidence is missing/unknown under `EffectiveMinimalEvidence`, the guard MUST NOT return `pass` (return `degrade` or `abstain` per the effective failure behavior; record the basis in Audit).

* **Applicability:**
  * Intended to be used only when a fold is explicitly required (and never as a hidden sub‑step of scoring/comparison/selection).
  * Applicable only when `CGSpecSlot` provides the admissibility surface (`Γ_fold` and `SCP`) (fail‑closed otherwise).
  * If comparability routing is UNM-based, applicability requires the explicit upstream result and preservation/loss basis needed by the fold. A fold inherited on classes requires equivalent outputs and representative-independent availability; a requested aggregate answer must be recoverable. Otherwise retain/refine the original inputs or return the missing distinction.

* **Relation boundary:** folding creates no transfer relation. If the admitted set or receiving use relies on an F.9 Bridge, kind relation, aggregation or membership relation, or plane relation, cite the exact obtaining relation, its direction and loss; supported penalties route to **`R_eff` only**.
* **Γ_timePolicy:** `point` by default; time‑fold requires explicit windowing policy (if an explicit operator is needed, introduce `FoldTime_Γ` as an `⊑⁺` extension using `GammaTimeRuleSlot` from the CHR SlotKind Lexicon).
* **PlaneRegime:** each contributor and aggregated measure keeps its declared reference plane; ULSAM introduces no plane crossing. When a result depends on a relation between planes, cite that relation, its direction and loss, and keep the receiving use separate.

* **Audit:**
  * MUST record: the admitted measure set and grouping or membership basis; `CNSpecRef.edition`, `CGSpecRef.edition`, and effective `ΓFoldRef`; claim scope and selected slices, qualification window, intended result, and the aggregated measure.
  * MUST record the evidence refs used to admit the measure set and evaluate `FoldEligibility_Γ`.
  * If `GammaFoldSlot` resolves via an explicit override, SHOULD record the override’s `policy-id` (or its stable ref) alongside `ΓFoldRef`.
  * When `MinimalEvidenceSlot?` is present, MUST record `MinimalEvidenceRef`; otherwise MUST cite `CGSpecSlot.MinimalEvidence` as the effective evidence policy.
  * When `ContributorSetSlot?` is produced, SHOULD record it (or an id reference) as an auditable explanation surface.
  * SHOULD record: any explicit UNM invocation ids/pins when folding presumes a compare‑on‑invariants surface established by UNM.
  * SHOULD record: an F.9 Bridge, kind relation, aggregation or membership relation, or plane relation only when the fold or receiving use actually relies on that obtaining relation.
  * SHOULD record: the evaluated `GuardDecision` (especially when not `pass`) and, when applicable, the effective evidence policy / failure behavior reference used to justify `degrade|abstain`.

#### A.19.ULSAM:4.2 - Interpretation notes (didactic, informative)

- **Γ‑fold is a declared governing spec ref, not an implementation choice.** In FPF terms, “how we fold” is a **policy-level commitment**: `GammaFoldSlot` MUST be resolvable to `CGSpecSlot.Γ_fold` routing or an explicit pinned override. If you cannot cite it, you do not have a fold — you have a hidden default.
- **ULSAM is not normalization.** ULSAM does not establish comparability by itself: it does not normalize, rescale, or “align units” as a hidden convenience. If a compare‑on‑invariants surface is required, invoke UNM explicitly upstream and cite the effective pins in Audit.
- **Prefer vector semantics when possible.** If you do not strictly need one aggregated measure, keep measures separate and let `CPM` + `SelectorMechanism` operate on a partial order (set-return semantics). A fold can discard distinctions; state which distinctions the declared fold preserves and loses.
- **Contributor surfaces are not “nice-to-have” in practice.** `ContributorSetSlot?` is optional in the signature, but operationally it is the simplest way to prevent “mystery rollups” and to preserve an explanation surface.
- **Time-fold is a specialization, not a loophole.** The base ULSAM declares `Γ_timePolicy` and allows time-fold only via explicit windowing policy. If a project needs an explicit `FoldTime_Γ` operator, introduce it as an `⊑⁺` extension with no mutation of inherited operations or SlotKind drift.
  - Use the suite lexicon token `GammaTimeRuleSlot` for the additional windowing rule input; do not overload `GammaFoldSlot` or invent a generic context input to carry time semantics.

### A.19.ULSAM:5 - Archetypal grounding (didactic, informative)

#### A.19.ULSAM:5.1 - Tell

- In CHR, ULSAM exists to keep the stage `fold_Γ?` **explicit**: if a pipeline wants folding, it invokes `ULSAM.Fold_Γ`; otherwise it skips the stage. Folding MUST NOT be smuggled into `USCM.Score`, `CPM.Compare`, or `SelectorMechanism.Select`.
- For a `U.System` decision: ULSAM explicitly folds the admitted measures about the named System, under the declared grouping or membership basis and CG-Spec fold policy, only when that aggregate result is actually needed.
- For a `U.Episteme` assessment: ULSAM explicitly folds the admitted evidential or measurement set about that episteme into an aggregate coordinate, using an aggregation model justified for that exact quantity and support dependence; reliability-like wording alone supplies no weakest-link law.

#### A.19.ULSAM:5.2 - Show

**Scenario A (manager-facing): “roll up” a multi-metric readiness into one reliability-like coordinate.**
1. A CHR pipeline produces a set of admitted measures (post-`USCM` or directly from characteristic measures):
   `MeasureSetSlot = {m₁, m₂, …, m_k}`.
2. The team wants a single “readiness” measure `m_ready` to be used as an input to later comparison/selection.
   The temptation is to “just average” or “just do weighted sum”.
3. ULSAM forces three explicit questions before folding:
   - **Admissibility:** Is the fold admissible under `CGSpecSlot.SCP` (units/scale) and `CGSpecSlot.Γ_fold` (declared fold kinds)?
   - **Evidence:** Is the evidence posture sufficient under `MinimalEvidence`? If not, do we `degrade` or `abstain`?
   - **Policy identity:** What is the identity of the fold (which ΓFoldRef, which edition)?
4. Only then, the pipeline performs:
   `Fold_Γ(MeasureSetSlot, CNSpecSlot, CGSpecSlot, GammaFoldSlot, MinimalEvidenceSlot?) → (AggregatedMeasureSlot, ContributorSetSlot?)`.
   The audit records `ΓFoldRef` and (optionally) the contributor surface.

**Scenario B (engineer-facing): proposed aggregation across different bases.**
- A project tries to fold measures with different bearers, membership rules, scales, comparison bases, or reference planes. ULSAM first checks whether one admitted set and lawful fold can be stated. If the conclusion relies on an F.9 Bridge, kind relation, aggregation or membership relation, or plane relation, the project cites that exact obtaining relation and its loss; otherwise it constitutes separate folds or fails closed.

### A.19.ULSAM:6 - Bias-Annotation (informative)

This pattern intentionally biases CHR authoring toward **explicit aggregation boundaries** and against “scalarization by convenience”.

* **Gov (governance).** Bias toward auditable folds (editions, effective ΓFoldRef, contributor surfaces). Risk: perceived overhead. Mitigation: keep the signature stable and move method specifics to SoTA wiring.
* **Arch (architecture).** Bias toward keeping `fold_Γ` a distinct stage (no leakage into score/compare/select). Risk: longer pipelines. Mitigation: the stage is explicitly optional (`fold_Γ?`) and can be omitted when not required.
* **Onto/Epist (ontology/epistemology).** Bias toward scale-lawful aggregation (no illegal ordinal arithmetic; SCP-bound). Risk: forbids many informal “single-number” habits. Mitigation: use partial orders and set-return selection unless a lawful fold is truly needed.
* **Prag (practice).** Bias toward policy-bound defaults (no “implementation default Γ‑fold”). Risk: teams must name policies. Mitigation: provide conservative defaults in `CG‑Spec.Γ_fold` and keep overrides explicit.
* **Did (didactic).** Bias toward one-governing pattern readability (this pattern is the governing pattern; no scavenger hunt). Risk: duplication temptation elsewhere. Mitigation: enforce Tell+Cite canonicalization.

### A.19.ULSAM:7 - Conformance Checklist (normative)

| ID | Requirement |
|----|-------------|
| **CC‑A19ULSAM‑0** | **Mechanism declaration completeness:** §4.1 MUST supply the A.6.1 operation-local arguments/results, application predicates, identity/extent rules, laws and admissibility/applicability conditions. SlotIndex projects those declarations. |
| **CC‑A19ULSAM‑1** | **Single governing pattern:** the ULSAM declaration is governed by §4.1; a use cites it rather than inferring semantics from a copied summary. |
| **CC‑A19ULSAM‑2** | **No hidden aggregation:** any Γ‑fold MUST be explicit as `ULSAM.Fold_Γ` (no folding hidden inside `Score/Compare/Select`, including inside `USCM/CPM/SelectorMechanism`). |
| **CC‑A19ULSAM‑3** | **Scale-lawfulness:** a conformant ULSAM fold MUST be CSLC-lawful and admissible under `CGSpecSlot.SCP`. Ordinal arithmetic is forbidden unless explicitly allowed by the relevant CSLC fragment. |
| **CC‑A19ULSAM‑4** | **Γ‑fold admissibility:** a conformant ULSAM publication MUST ensure `GammaFoldSlot` resolves to `CGSpecSlot.Γ_fold` or an explicitly pinned override (CAL policy). "Implementation default fold" is non-conformant. |
| **CC‑A19ULSAM‑5** | **Evidence gating:** a conformant ULSAM publication MUST guard folding via `FoldEligibility_Γ` with `GuardDecision ∈ {pass|degrade|abstain}`; missing/unknown evidence MUST NOT yield `pass`. If `MinimalEvidenceSlot?` is absent, the guard MUST evaluate against `CGSpecSlot.MinimalEvidence`. |
| **CC‑A19ULSAM‑6** | **SlotKind discipline:** SlotKind tokens used in the ULSAM intension MUST come from the CHR SlotKind Lexicon (`A.19.CHR:4.2.1`). New SlotKinds require lexicon extension first. |
| **CC‑A19ULSAM‑7** | **Audit surface:** Audit MUST record `CNSpecRef.edition`, `CGSpecRef.edition`, and the effective `ΓFoldRef`; and MUST record `MinimalEvidenceRef` when overridden (else cite `CGSpecSlot.MinimalEvidence`). |
| **CC‑A19ULSAM‑8** | **Contributor accountability:** when `ContributorSetSlot?` is produced, it SHOULD be recorded (or referenced by stable id) as an explanation surface for what contributed after admissibility/evidence gating. |
| **CC‑A19ULSAM‑9** | **P2W separation:** the A.15.2 baseline MUST select the intended fold/evidence policies and editions. A.15.3 typed filling applies only to independently declared positions. Actual Fold_Γ bindings MUST obtain under §4.1 and remain distinct from planned values and their Audit representation. |
| **CC‑A19ULSAM‑10** | **Gate/guard separation:** ULSAM MUST NOT embed GateDecision/GateLog or publish/telemetry operations in the `fold_Γ?` stage; admissibility is via `FoldEligibility_Γ` (tri‑state) and run‑time observability via `Audit` pins only. |
| **CC‑A19ULSAM‑11** | **No implicit UNM:** ULSAM MUST NOT silently normalize/rescale to force comparability. When normalized inputs are required, cite the upstream directed result and preservation/loss basis in Audit. A class-level fold also needs compatibility, partial-availability and receiving-query recovery under A.19.UNM; invoking UNM alone supplies none of them. |

### A.19.ULSAM:8 - Common anti-patterns (didactic, informative)

| Anti-pattern | Symptom | Why it fails in FPF | How to avoid |
|---|---|---|---|
| Hidden rollup inside scoring | “Our score already averages everything.” | Violates the “no hidden aggregation” law and hides Γ‑fold identity. | Keep `USCM.Score` scoring-only; use `ULSAM.Fold_Γ` as an explicit stage. |
| Averaging ordinals | Means on ranks/levels, or unitless mixing | Illegal under CSLC/SCP unless explicitly allowed. | Keep ordinal outputs as ordinal; compare via CPM; if folding is required, use an ordinal-legal fold explicitly declared by Γ_fold policy. |
| Implementation default Γ‑fold | "If not specified, we use X." | Breaks replayability and violates Γ‑fold admissibility. | Require `GammaFoldSlot` to resolve to `CGSpecSlot.Γ_fold` or pinned override. |
| Coercing unknown to a number | “Missing metric becomes 0.” | Violates tri-state guard discipline; silently changes meaning. | Use `FoldEligibility_Γ` with `{pass|degrade|abstain}` and record the effective evidence policy. |
| Folding after the admitted set or basis changed | Measures with different bearers, membership rules, scales, scopes or windows, comparison bases, or planes are folded “as-is” | The result no longer follows from one declared set and lawful fold; relation labels cannot repair that gap. | Re-establish the admitted set and eligibility. Cite an obtaining relation and supported loss only when the fold or receiving use actually relies on it; otherwise keep separate folds or abstain. |
| Treating fold_Γ as mandatory | Always folding even when not needed | Unnecessary aggregation can hide distinctions needed by the receiving use. | Keep `fold_Γ?` explicitly optional in protocols; prefer vector+CPM+Selector when possible. |

### A.19.ULSAM:9 - Consequences (didactic, informative)

| Benefits | Costs / trade-offs |
|---|---|
| Clear separation of concerns: folding is explicit and auditable. | Adds an explicit step; authors must name Γ‑fold policies. |
| Prevents illegal “single-number” shortcuts (ordinal means, unit mixing). | Some familiar heuristics become non-conformant. |
| Improves evolvability: folding methods evolve via wiring, while the kernel signature stays stable. | Requires discipline to keep method specifics out of kernel prose. |
| Supports evidence-aware aggregation via tri-state guards. | Guard + Audit expectations may feel heavier than ad-hoc aggregation. |

### A.19.ULSAM:10 - Rationale (didactic, informative)

Aggregation is a **semantic commitment**: it changes a set/vector of measures into a single measure, and therefore changes what later comparison/selection can legitimately claim. In CHR, that commitment must be explicit, admissibility-gated, and auditable.

Keeping ULSAM as its own mechanism preserves:
- the strict boundary between **method choice** (SoTA packs) and **operation declaration**,
- the strict boundary between **planned baseline** (pins chosen in WorkPlanning) and **run-time audit** (what actually executed),
- and the engineer-facing clarity that “we folded here, not everywhere”.

### A.19.ULSAM:11 - Known uses (didactic, informative)

- CHR suite optional stage `fold_Γ?` (explicitly optional; never hidden).
- Folding a trust/assurance quantity only under its justified model and applicable policy; a declared default alone supplies no numerical warrant.
- Any project that requires an auditable “roll-up” measure prior to lawful comparison/selection.
- In E.18 transformation-flow structures: ULSAM appears as a mechanism instance node whose `ΓFoldRef` / `MinimalEvidenceRef` are bound in planned baseline (P2W), while Audit records the effective pins used at run time.

### A.19.ULSAM:12 - Builds on / Relates to

**Builds on (cite, don’t duplicate).**
- `A.6.1` (operation declarations and actual application/binding rules).
- `A.6.1 §4.2` (operation-local argument/result declarations as the source of SlotIndex).
- `A.19.CHR` (CHR suite boundary; stage `fold_Γ?`; CHR SlotKind Lexicon).
- `G.0` (`CG-Spec.Γ_fold`, `CG-Spec.SCP`, `CG-Spec.MinimalEvidence`; admissibility gate).
- `A.18` (CSLC).
- `B.3` (support dependence and the justified model for any `R_eff` calculation).

**Relates to (coordination, not governing-pattern assignment).**
- `A.19.CN` (`CN‑Spec`), via `CNSpecSlot.acceptance` gating in admissibility.
- `A.19.UINDM`, `A.19.USCM`, `A.19.CPM`, and `A.19.SelectorMechanism` as adjacent CHR stages (Uses contour; no governing-pattern assignment transfer).
- Part G SoTA packs and wiring (`G.2` + `G.*:Ext.*`) for method family selection and edition/policy binding.

### A.19.ULSAM:13 - SoTA-Echoing (informative; not a center of gravity)

SoTA here is treated as **method-family source publications and `G.2` claim sheets to be wired** through `G.*:Ext.*` wiring, not as kernel semantics. ULSAM’s contribution is the stable boundary: explicit, admissible, auditable folding.

**SoTA vs popular note.** This section records alignment to post‑2015 evidence‑backed practice. It is **not** a mandate to use fashionable methods; method semantics stay in SoTA packs (`G.2`) and wiring modules, while this pattern fixes the stable mechanism boundary.



| SoTA practice pointer (post‑2015+) | Primary source | Where it connects | Adoption status |
|---|---|---|---|
| Permutation‑invariant set aggregation as a *method family* (set → summary) | Zaheer et al., “Deep Sets” (2017) [1] | Candidate `ΓFold` families can include permutation‑invariant folds; ULSAM keeps them admissibility-gated and policy-pinned. | **Adapt** (keep admissibility/pins explicit; do not treat learned folds as implicit defaults). |
| Attention-based permutation‑invariant set aggregation as a *method family* | Lee et al., “Set Transformer” (2019) [4] | Alternative learnable set folds (pooling by attention); still requires explicit policy binding and admissibility gating. | **Adapt** (publish as method family in SoTA pack; pin editions/policies; keep kernel unchanged). |
| Robust aggregation under uncertainty/outliers as a *policy-selectable fold family* | Rahimian & Mehrotra, “Distributionally Robust Optimization: A Review” (2019) [2] | Treat “worst‑case / risk‑aware” folds as explicit Γ‑fold options (policy-bound), not as hidden safety margins. | **Adapt** (policy‑bound and SCP/CSLC‑gated). |
| Governing-pattern discipline for architectural statements | ISO/IEC/IEEE 42010:2022 [3] | Supports the “one governing pattern” rule: ULSAM intension content lives here; other places cite. | **Adopt** (principle-level; applied to FPF pattern governing-pattern assignment). |

**Reminder.** “SoTA” means best known methods; it is not a synonym for “popular right now”. SoTA material should be curated and versioned in SoTA packs and connected via wiring modules, not embedded into kernel mechanism signatures.

[1]: https://arxiv.org/abs/1703.06114 "Zaheer et al., Deep Sets, 2017"
[2]: https://arxiv.org/abs/1908.05659 "Rahimian & Mehrotra, Distributionally Robust Optimization: A Review, 2019"
[3]: https://www.iso.org/standard/74393.html "ISO/IEC/IEEE 42010:2022 — Systems and software engineering — Architecture description"
[4]: https://arxiv.org/abs/1810.00825 "Lee et al., Set Transformer, 2019"

### A.19.ULSAM:End
