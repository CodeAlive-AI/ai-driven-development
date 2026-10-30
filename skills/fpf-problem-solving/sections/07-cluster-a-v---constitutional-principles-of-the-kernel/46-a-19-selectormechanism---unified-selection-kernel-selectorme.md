## A.19.SelectorMechanism - Unified Selection Kernel, SelectorMechanism

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> This pattern declares Select and SelectEligibility under A.6.1. Actual applications and any separately asserted Work use the conditions in §4.1.

### A.19.SelectorMechanism:0 - At a glance — didactic, informative

* **What it is:** a universal **set-returning** selection kernel: it takes candidates, admissible comparison outcomes, and explicit criteria, and returns a **selected set**, not a forced single winner.
* **Why it exists:** to prevent three recurring failure modes: **hidden thresholds**, **silent scalarization**, and **winner‑take‑all defaults** under partial orders and uncertain evidence.
* **Use this when:** admitted candidates must be selected under explicit criteria after comparison. Identify the candidate universe and choice rule, recover the required comparisons and their conditions, then return the justified subset. Stop with comparison when the receiving question needs no selection; a selection result alone supplies no authorization to act.
* **What this buys:** the practitioner gets one selected-set value whose criteria, finite basis of exact upstream binary CPM applications, required comparison coverage, token provenance, scope, predicate basis, plane, window, and policy bindings are explicit. `degrade` and `abstain` remain eligibility values, not selected-set members or alternative result kinds.
* **First output:** read the by-value candidate set bound to `SelectionSlot`. Read the candidate universe, finite upstream CPM application basis, required pair coverage, derived comparison-token union, selection conditions, claim scope and context slices, reference plane, evaluation window, eligibility value, and evidence use from the actual `Select` application and direct neighboring relations; they are not fields inside the selected set.
* **How it evolves:** method semantics and SoTA algorithm families connect via `G.2` packs and wiring modules; the kernel signature stays stable and teachable.
* **Suite stage:** `select` (ordering lives only in `A.19.CHR:4.5` and `suite_protocols`; suite membership is a set in `A.19.CHR:4.2`).
* **Inputs (conceptual):** admitted candidates; a finite by-value basis of exact upstream binary CPM applications, each with its exact pair, realized `GuardDecision`, and own `ComparisonResultSlot` binding when produced; the exact union of justified relation or poset tokens from those bindings; explicit `CriteriaSlot`, `CNSpecSlot`, `CGSpecSlot`; one `U.ClaimScope` with selected A.2.6 `U.ContextSlice` members; the same A.19 predicate basis when one governs the comparisons or selection criteria; effective reference plane; explicit evaluation window; and optional TaskSignature and MinimalEvidence policy refs.
* **Output (conceptual):** the by-value `SelectionSlot` candidate set. A singleton is allowed when the explicit criteria determine one candidate; a total order supplies comparison information but needs a choice rule. The output is not a decision log, guard value, result episteme, generic result relation, publication, or replay record.
* **Planned use:** on a P2W path, an A.15.2 baseline selects editions and policies. A.15.3 and SlotFillingsPlanItem apply only to independently declared receiving positions under A.19.CHR:4.7.2. The actual Select application carries its effective arguments and SelectionSlot binding under §4.1. Dated selection Work and an A.10 provenance account retain their independent grounds.
* **Transformation-flow use:** when selection is represented by an E.18 node, that node cites this declaration. Planned refs use A.15.3 typed filling only for independently declared receiving positions; actual Select bindings remain governed by §4.1.
* **Failure mode:** tri‑state guard (`pass|degrade|abstain`); missing or unknown evidence never coerces to `pass`.
* **Mental model:** `SelectEligibility` gates the step; `Select` applies explicit criteria to set‑valued comparison outcomes; the result is a selected set whose “single winner” behavior must be explicit.

---

### A.19.SelectorMechanism:1 - Problem frame

FPF’s Characterization (CHR) suite treats selection as a **distinct mechanism boundary** within the suite (authoritative membership: `A.19.CHR:4.2`).
Suite membership is a **set**; order has no semantics. Any intended ordering is expressed only via `suite_protocols` (`A.19.CHR:4.5`), under suite obligations (`A.19.CHR:4.3`).

Within the suite‑closed protocol, `SelectorMechanism` appears as the `select` stage (after admissible comparison; optional stages remain explicitly optional per `suite_protocols`). The kernel’s role is concept‑level and governed by CN‑Spec and CG‑Spec:

* consume **admissible** comparison outcomes without collapsing them into a hidden scalar,
* apply **explicit** criteria and policy references, and
* return a **selected-set** result whose defaults are policy-bound and whose dated work, actual `Select` application, `SelectionSlot` binding, and evidence-provenance basis can be replayed.

The kernel uses the CHR suite SlotKind lexicon (`A.19.CHR:4.2.1`) to prevent SlotKind drift across specializations and across SoTA wiring layers.

---

### A.19.SelectorMechanism:2 - Problem

Engineering teams regularly need to make “a selection decision” under conditions that are normal in real projects:

* comparisons are partial, multi‑criteria, or set‑valued,
* evidence is incomplete or policy‑gated, and
* different stakeholders ask for different “best” notions.

If selection is not a first‑class mechanism boundary with stable semantics, the same high‑risk drift happens repeatedly:

* **Silent winner forcing:** partial orders get collapsed to a single winner by ad‑hoc tie‑breakers or hidden weights.
* **Hidden thresholds and constants:** thresholds, weights, dominance regimes, and default `PortfolioMode` fields get smuggled into implementations and become invisible in discussion and audit.
* **Scalarization by convenience:** set‑valued comparison outcomes get replaced by a scalar “score summary” that is treated as decision‑relevant without being declared as such.
* **Evidence coercion:** missing or unknown evidence gets treated as “good enough” (implicit pass) rather than yielding explicit `degrade` or `abstain`.
* **Boundary erosion:** selection quietly performs comparison, scoring, aggregation, or publishing.
* **Selection-boundary drift:** a selected-set label is reused after candidate universe, finite upstream comparison-application basis or its required coverage, selection conditions, A.19 predicate, claim scope, selected context slices, reference plane, or evaluation window changed.
* **Guard-output collapse:** `degrade` or `abstain` is treated as a selected-set member or as a generic selection result.

---

### A.19.SelectorMechanism:3 - Forces

1. **Set‑valued reality vs single‑winner convenience.** Many admissible comparisons are partial orders. The kernel must preserve set‑valued semantics while still allowing single‑winner outcomes when explicitly requested by criteria.

2. **Policy primacy vs method freedom.** Criteria and defaults must be explicit and policy‑bound, while multiple method families and decision styles must remain add‑able without mutating the kernel.

3. **No hidden thresholds vs usability pressure.** Engineers often want “just pick one.” If the spec does not constrain this, hidden thresholds and tie‑breakers become de facto policy.

4. **Evidence discipline vs delivery pressure.** Under uncertainty, teams default to coercion (unknown → pass). The kernel must enforce tri‑state eligibility and fail‑closed discipline.

5. **Replayability vs conceptual minimalism.** The mechanism declaration stays small, while dated selection work, the actual `Select` application and its argument and `SelectionSlot` bindings, and the evidence-provenance path retain the effective editions, policies, candidates, and selected set needed for replay.

6. **Evolvability vs didactic usability.** The kernel must be stable enough to support SoTA wiring and specialisation chains, but also teachable: one place states the mechanism boundary, laws, eligibility behavior, and the neighboring replay basis for realized use.

7. **Planned use and gate/guard separation.** On a P2W path, A.15.2 carries the intended baseline; A.15.3 typed filling is conditional on independently declared positions. Selection must not mutate into a gate pattern: no GateDecision or decision logs inside the mechanism boundary.

8. **No competing defaults.** If defaults exist for `PortfolioMode`, dominance regime, or archive policy, cite their declared sources rather than re-declaring them in the kernel.

9. **Scope continuity vs legitimate reselection.** Selection may narrow candidates or apply explicit policy, but it may not silently change the finite upstream comparison-application basis, its required pair coverage, any member's predicate basis, claim scope, selected context slices, reference plane, or evaluation window. A justified change is a new selection application and may require new binary comparisons.

---

### A.19.SelectorMechanism:4 - Solution

`SelectorMechanism` is the canonical **selection kernel** for CHR and for selector specializations. It provides:

* a stable mechanism boundary for `select`,
* a stable SlotKind field set (via the CHR lexicon),
* a minimum law set that preserves set‑valued semantics and forbids hidden thresholds and hidden scalarization,
* a tri‑state admissibility guard that is fail‑closed under missing admissibility or evidence,
* a replay basis that separates effective occurrence bindings, the selected-set result, and supporting evidence from reusable selector semantics;
* an explicit selection-use boundary that keeps candidate universe, the finite upstream comparison-application basis and required coverage, the derived token union, selection conditions, scope, predicate basis, plane, and window distinct; and
* output discipline: `SelectionSlot` contains only the selected candidate set, while eligibility, evidence use, provenance, currentness, result epistemes, and publications remain separate.

Method semantics and SoTA algorithm families do not live inside the kernel: they connect via `G.2` SoTA packs and wiring modules, and via explicitly declared specializations subject to the local restrictions in CC‑A19SelectorMechanism‑10. A claimed refinement, conservative extension or equivalence uses its own comparison test in `A.6.1 §4.8`; the labels `⊑` and `⊑⁺` do not supply that test.

#### A.19.SelectorMechanism:4.1 - Operation declaration — normative core

* **Declaration boundary:** this A.6.1 intension declares `Select` and `SelectEligibility`; it does not bind project-specific pins or create selection scope, dated work, an actual operation application, gate decision, selected-set episteme, evidence use, provenance path, currentness relation, or publication relation. Each neighboring object or relation uses its direct governor.
* **Declaration identity:** SelectorMechanism.IntensionRef cites this exact A.6.1 U.Mechanism episteme. The CHR select stage resolves to its local Select operation. A changed argument, selection law or guard requires explicit selection of the changed declaration; another realizer of the same declaration changes no suite member.

* **IntensionHeader:** `id = SelectorMechanism`, `version = 1.0.0`, `status = stable`.

* **IntensionRef:** `SelectorMechanism.IntensionRef` designates this `U.Mechanism` episteme as the canonical suite member named in `A.19.CHR:4.2`; it is not the `EntityOfConcernRef` of the declared operation family.

* **Purpose:** universal set‑returning selection kernel over candidates and criteria; defaults remain policy‑bound; **no hidden thresholds**.

* **Imports:** `A.6.1:4.8 (exact declaration comparisons)`, `A.6.1 (operation-local declarations and bindings)`, `A.19.CN (CN‑Spec governance card)`, `C.22 (TaskSignature as a policy-reference artifact when used)`, `G.5 (selector conformance and default selection policy)`, `G.0 (CG‑Spec admissibility and evidence gates)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`.

* **EntityOfConcernRef:** the selection operation family declared by `Select` and `SelectEligibility` in this section.

* **Effective reference scheme:** the CHR suite reference scheme in which the A.19.CHR SlotKind lexicon, CN-Spec, CG-Spec, and any current TaskSignature tokens are interpreted.

* **Direct signature components:**

  * **SubjectKind:** `Selection`.
  * **RangedValueKind:** pair of values `<admitted candidate set, relation or poset token set over the same candidate universe>`.
  * Results are operation-local: the selected candidate set and the separate guard judgment.
  * Input qualification: selection ranges over one admitted candidate set and the exact union of justified relation or poset tokens from a finite basis of binary CPM applications whose pair endpoints lie in that candidate set and whose coverage satisfies the explicit selection conditions, all in one exact `U.ClaimScope`; selected `U.ContextSlice` values are members of that scope under A.2.6 and do not create duplicate membership.

  These are direct A.6.0 declaration components. They do not form another selector-content container, and they do not absorb candidate admission, comparison work, dated selection work, result, evidence-provenance, or replay relations.
**Operation-local argument and result declarations**

Each argument below is declared separately for Select and SelectEligibility, except the realized eligibility argument of Select itself. ByValue carries the stated value; a named Ref or ByRef resolves one exact value and edition. Cardinality is per application. The guard can assess an incomplete proposal with 0..1 of each required argument; missing inputs have no binding and prevent pass.

| Direction | Local designator | Meaning and ValueKind | Designation; cardinality |
| --- | --- | --- | --- |
| Argument | CandidateSetSlot | Set of admitted candidate values, each retaining its governing kind and identity | ByValue; 1 set |
| Argument | ComparisonResultSlot | Set of relation/poset tokens, exactly the union of the comparisonBasis members' own returned values | ByValue; 1 set |
| Argument | CriteriaSlot | Set of selection clauses and explicit tie-breakers used to determine the selected set; acceptance thresholds remain in their own declarations | ByValue; 1 set |
| Argument | TaskSignatureSlot | TaskSignature supplying selector policy defaults when used; it does not replace CN-Spec or CG-Spec | TaskSignatureRef; 0..1 |
| Argument | CNSpecSlot | CN-Spec supplying admission/acceptance and candidate-use conditions | CNSpecRef; 1 |
| Argument | CGSpecSlot | CG-Spec supplying selector admissibility and default evidence conditions | CGSpecRef; 1 |
| Argument | MinimalEvidenceSlot | MinimalEvidence override used instead of CGSpecSlot.MinimalEvidence | MinimalEvidenceRef; 0..1 |
| Argument | comparisonBasis | Finite set of exact binary CPM Compare application references, each with its left/right pair, realized eligibility and own output binding or explicit absence | ByValue set; 1 |
| Argument | requiredComparisons | Finite set of required binary comparisons derived from the candidates, criteria and effective policy, including direction/comparator distinctions that affect selection | ByValue set; 1 |
| Argument | tokenProvenance | Mapping from every consumed token to at least one exact producing CPM output binding in comparisonBasis | ByValue; 1 mapping |
| Argument | claimScope | U.ClaimScope delimiting candidate universe and selection use | ByRef; 1 |
| Argument | selectedSlices | Set of selected U.ContextSlice members of claimScope under A.2.6 | ByValue set of exact references; 1 set |
| Argument | characteristicPredicate | A.19 CharacteristicSpacePredicate basis shared as required with the relevant CPM members | ByValue; 0..1, explicitly absent when none governs the use |
| Argument | referenceScheme | `EpistemeInterpretationScheme` (C.2.1:4.1.2), governing this selection | ByRef through C.2.1 SchemeDesignation; 1 |
| Argument | referencePlane | CHR:ReferencePlane value qualifying selection | ByValue; 1 |
| Argument | evaluationTime | Selection-evaluation point or interval in the declared time basis | ByValue; 1 |
| Argument | selectorPolicy | Effective selection policy and resolved defaults, including exact candidate-level failure behavior when degrade is used | ByRef to the declared policy; 1, resolved through TaskSignature when it supplies that policy |
| Select argument | eligibility | GuardDecision actually determined by SelectEligibility for these same proposal arguments, used to admit this selection | ByValue; 1, with its exact producing guard-result binding recoverable |
| Select result | SelectionSlot | Set of candidate values selected under those criteria and policy | ByValue; 1 set on completed admitted selection, 0 on abstain |
| SelectEligibility result | GuardDecision | Judgment determined by the eligibility predicates: pass, degrade or abstain | ByValue; 1 on completed evaluation |

Resolve the scheme designation under C.2.1:4.2.6 to one exact rule collection, then check its C.2.1:4.1.2 range and the rules needed by these actual selection inputs. The reference token is not the bound scheme. An unresolved required interpretation cannot support a completed admitted selection; apply the guard and abstention rules below. Membership alone supplies neither successful selection nor a cross-scheme correspondence. The application and result bindings below remain independently required.

For each argument row, its **bindingPredicate** holds when that application actually uses the resolved value for its stated purpose: candidates supply the selection universe, criteria/policy supply the choice rule, specifications/evidence requirements govern admission, and the basis, coverage and provenance supply the comparisons on which the choice relies. Scope, slices, predicate, scheme, plane and time bind only when they qualify that application. A nearby policy or copied comparison record does not supply those bindings.

The **SelectionSlot bindingPredicate** holds when that Select application returns the candidate subset determined by its bound criteria/policy from the justified comparison basis, under its declared pass/degrade conditions. The **GuardDecision bindingPredicate** holds when that SelectEligibility application returns its assessed judgment. An equal selected set or guard value stored elsewhere is insufficient. A.6.1 governs each binding's identity and continuous extent within the application; result binding begins at its actual return.

**SlotIndex (derived projection).** Project the designators, ValueKinds, designation and cardinalities above. Historical Slot names support CHR lookup. The other local names declare operation arguments, not new U-kinds or CHR SlotKinds; A.6.5 relation SlotSpecs supply none of their semantics.

**OperationAlgebra.** The select stage resolves to Select with the declared candidate/token, criteria/specification and selection-use arguments, returning SelectionSlot. SelectEligibility evaluates that proposal under the guard below. ComparisonResultSlot contains only the exact token union; application references, coverage, scope and provenance remain separate arguments. A CPM abstain with no output contributes no token. Every required comparison must be discharged by an exact basis member; degraded selection names excluded candidates under the bound failure behavior and retains complete coverage for its reduced use.

**ApplicationPredicate.** Select obtains when a selection act actually applies the bound criteria and effective policy to the candidate universe using the bound justified CPM outputs and use restrictions, with pass or an explicitly permitted degrade outcome under SelectEligibility. It returns the resulting set; on abstain no Select act proceeds. SelectEligibility obtains when an evaluation actually checks that proposal's coverage, provenance, admission and evidence conditions and returns the corresponding judgment. A valid proposal or an equal saved selected set does not establish that selection act.

**ApplicationIdentityRule.** One application is one selection invocation or guard-evaluation invocation at its calculation locus, from taking up its declared arguments until return or termination. References to that same episode reidentify it. Two independently begun invocations remain distinct even when the complete CPM basis, criteria, policies, qualification window and results are equal. Law 6 additionally makes a changed binding a new selection application; a completed prior application cannot acquire the replacement basis or result.

**ApplicationExtentRule.** Select extends from actual use of its candidates, CPM basis and choice rules through selected-set return or termination; SelectEligibility extends from proposal assessment through judgment or termination. An unfinished invocation has an open extent and no unreturned result binding. The selection-evaluation window qualifies the use and does not determine these actual calculation intervals. A trace designates an established episode; ordinary set-selection mathematics asserts no dated U.Work.

For example, use the admitted incomparable supplier pair from A.19.CPM §4.1 and the declared criterion “retain every nondominated candidate.” With complete required coverage and the exact CPM token binding, two separately performed selections can each return {A,B}. Their Select occurrences and result bindings differ even when they reuse the same CPM producer application. A copied {A,B} without a corresponding selection return establishes no fresh binding. A copied comparison token whose producing CPM return is unestablished fails tokenProvenance and causes abstain; it cannot enter the basis merely because its text matches.

* **LawSet** (minimum): the selection kernel is set-returning and policy-bound

  1. **Set‑returning by default:** a conformant `Select` MUST return a declared selected set by default. It MUST NOT silently collapse partial orders or incomparabilities to a single winner; a singleton outcome MUST follow from the explicit criteria applied to the admitted comparison outcomes.
  2. **No hidden thresholds or constants:** a conformant publication MUST NOT smuggle thresholds, weights, dominance rules, or tie‑breakers. Selection‑level commitments MUST be explicit in `CriteriaSlot` and, where needed, in explicit policy defaults exposed through `TaskSignatureSlot`. Admissibility and acceptance thresholds are applied only via `SelectEligibility` using `CNSpecSlot.acceptance` and the effective evidence policy (`MinimalEvidenceSlot?` or `CGSpecSlot.MinimalEvidence`).
  3. **No hidden scalarization or token aggregation by assertion:** a conformant publication MUST consume `ComparisonResultSlot` as the exact union of the finite basis members' justified set-valued or partial outputs. Every consumed token MUST be traceable to at least one exact producing CPM application. Scalar summaries or relation tokens inferred from a missing pair, empty output, `degrade`, or `abstain` are forbidden; scalar summaries, if produced at all, are report-only unless explicitly promoted by policy outside suite closure.
  4. **Evidence gating is explicit:** when selection depends on evidence, it MUST cite either `MinimalEvidenceSlot` or the effective `CGSpecSlot.MinimalEvidence` policy and evaluate selection with the tri-state predicate. Candidate-level ineligibility handling MUST be explicit in current criteria or upstream results and bound by the actual selection application; the kernel MUST NOT invent evidence thresholds.
  5. **No competing defaults:** effective `PortfolioMode`, dominance regime, and other defaults come from declared policy refs and are bound by the actual application.
  6. **No silent boundary change:** `Select` does not silently change candidate universe, comparison-application basis membership, required comparison coverage, any member's pair, eligibility or output binding, selection conditions, A.19 predicate basis, claim scope, selected context slices, reference scheme or plane, or evaluation window. A changed binding is another selection application and may require new binary comparisons.
  7. **Guard-output separation:** `GuardDecision` is not a selected-set member. On `abstain`, no `SelectionSlot` value is fabricated. A `degrade` eligibility value permits a reduced set only under the explicitly bound failure behavior and criteria.

* **AdmissibilityConditions** (tri-state guard; fail-closed on missing admissibility, comparison coverage, token provenance, or evidence)

  * `SelectEligibility(CandidateSetSlot, ComparisonResultSlot, CriteriaSlot, CNSpecSlot, CGSpecSlot, TaskSignatureSlot?, MinimalEvidenceSlot?; selection-use bindings) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires: (i) every basis member's exact pair lies inside `CandidateSetSlot`; (ii) the basis covers every binary comparison required by the candidate universe and explicit selection conditions; (iii) every consumed relation token traces to a member's own output binding; (iv) explicit selection conditions and tie-breakers; (v) compatible A.19 predicate basis, claim scope, selected A.2.6 context slices, reference plane, and evaluation window across the basis and selection; (vi) coherent CN-Spec and CG-Spec editions; and (vii) satisfied admission, acceptance, and effective MinimalEvidence predicates under their direct owners.
  * If `MinimalEvidenceSlot` is absent, `SelectEligibility` MUST evaluate evidence against `CGSpecSlot.MinimalEvidence` by explicit rule, and missing or unknown evidence MUST NOT yield `pass`.
  * A basis member with `GuardDecision = degrade` may support a reduced set only when a current selector policy names the exact candidate-level failure behavior and the remaining basis still covers the comparisons required for that reduced use. The actual selection application binds that policy and its own realized eligibility value.
  * A missing required comparison, untraceable token, or required basis member with `GuardDecision = abstain` makes `SelectEligibility = abstain`; selection does not proceed and no selected-set output is created.

* **Applicability:**

  * Intended for the CHR `select` stage after the required finite set of admissible binary comparisons and produces a selected-set value. Selection remains distinct from comparison, acceptance, gate decision, publication, and telemetry.
  * Applicable only when `CNSpecSlot`, `CGSpecSlot`, explicit criteria, the effective evidence policy, and a finite comparison-application basis with complete required coverage and token provenance are current for the candidate universe. Missing declarations or coverage fail closed.
  * Inside the CHR suite, `A.19.CHR:4.5` alone determines stage ordering and optionality.
  * Every actual selection binds one exact `U.ClaimScope`, selected A.2.6 `U.ContextSlice` members, the finite basis of exact binary CPM applications and their pair, eligibility, and output bindings, the derived token union, A.19 predicate basis, effective reference plane, selection conditions, and explicit evaluation point or interval. There is no implicit latest value and no default window inherited from the predicate or comparison label.
  * A selection across reference schemes or planes follows the relations the case actually needs. When it relates two exact F.17 `SchemeSenseCell` values from different semantic contexts, test the F.9 `BridgePredicateProfile` and cite the Bridge only when its direct predicate obtains; state suitability for the named selection use in a separate C.2.1 claim. If that predicate is false or unresolved and the semantic crossing is required by the selection conditions, `SelectEligibility` cannot be `pass`; follow the already declared explicit `degrade` policy when applicable, otherwise `abstain`. When the selection crosses exact ReferencePlanes, cite the applicable plane relation and policy. If both facts are current, state both under their own predicates. A cell or plane difference alone establishes neither relation, and one branch never fabricates the other. Neither relation supplies candidate universe, comparison-application basis or coverage, relation tokens, selection conditions, scope, predicate, or time.

* **Neighboring semantic-Bridge, bounded-use, and reference-plane relations:**

  When candidates or comparison tokens require interpretation across different semantic contexts, resolve the two exact F.17 `SchemeSenseCell` endpoints and test one F.9 `BridgePredicateProfile`. For an obtaining Bridge, state its exact endpoints and profile separately. State suitability for the named selection use in a C.2.1 assertion whose EntityOfConcern is that Bridge and whose ClaimGraph designates `<u,d,r,t>` and polarity. Include `CL` or an observed-loss note only when the receiving use consumes it; permitted loss remains `t` in the bounded-use claim. For a ReferencePlane crossing, cite the applicable plane relation and policy separately. Open A.10 only when bounded reliance is current and B.3 only when an actual named assurance claim is current. If that assurance argument consumes a locally declared `R_eff` calculation, cite its applicable domain model and calculation; neither the Bridge nor `CL` creates a penalty. Adding or changing any of these neighboring objects does not by itself change the selector declaration.

* **Neighboring dated work, operation application, result binding, and evidence relations:**

  The identified Select application binds the candidate set, finite comparison basis, required coverage, token union, selection-use arguments, policies and returned SelectionSlot. If the account also asserts dated selection U.Work, first establish its A.13 core: the performing System, exact local agential-role kind and membership criterion, and an obtaining assignment of its declared direct species for the relevant scope and time. A.15.1 independently admits that performance; F.6 applies afterward only for precise assignment-bound attribution. The Work identity and extent are not automatically those of one Select application. When the account asserts them or the receiving use consumes them, A.2.4 governs evidence use with its own claim scope and relevance window, A.10 governs reliance and provenance, and G.11 governs source or assertion-edition currentness. A durable selected-set episteme, when needed, is governed by C.2.1, and any current entity-identity inception claim by A.15.PROD. No universal work-result, comparison-result, or selection-result relation is presumed. To replay the selection, recover:

  * the candidate set and required binary comparisons; for every basis member, the exact CPM application, pair, realized `GuardDecision`, and its own output binding or explicit absence; and the trace from every consumed token to its producing member;
  * one `U.ClaimScope`, selected A.2.6 context slices, A.19 predicate basis, effective reference scheme and plane, and evaluation point or interval shared as required by the selection conditions;
  * `CNSpecRef.edition`, `CGSpecRef.edition`, and `TaskSignatureRef.edition` when TaskSignature is used;
  * the effective MinimalEvidence policy, either the explicit override or `CGSpecSlot.MinimalEvidence`;
  * the Selector's realized `GuardDecision` and, for `degrade` or `abstain`, the current failure-behavior policy;
  * the candidate-set value and exact derived union bound to the Selector's `ComparisonResultSlot` argument;
  * the effective criteria and selector-default refs; and
  * the selected-set result; any current obtaining F.9 Bridge and its separate C.2.1 bounded-use claim; any optional `CL` or observed-loss note actually consumed; and any applicable ReferencePlane relation and policy. Recover A.10 reliance or B.3 assurance only when the selection use actually consumes it.

  These neighboring objects support replay. The finite basis is a binding of the actual selection application, and none of them is selector-declaration content or a generic result container.

#### A.19.SelectorMechanism:4.2 - Boundary and layering rules

0. **Selection conditions are explicit values, not a new object kind.** The actual application binds `CriteriaSlot` plus effective selector-policy refs, defaults, and `degrade` failure behavior. Acceptance and admission predicates remain separate. `SelectionSlot` contains only the resulting candidate set; eligibility, conditions, scope, evidence, and replay metadata stay outside it.

1. **Selection consumes a traceable finite basis of upstream CHR products; it does not invent them.** Any indicator-derived scoring or comparison input retains its exact A.19 basis and the UINDM positions selected under that declaration. A changed basis requires rechecking affected upstream position resolutions and dependent results, preserving reuse where their grounds still hold; the selector cannot carry old naked indices into the new declaration. The actual use binds exact binary CPM applications separately and supplies `ComparisonResultSlot` only as the union of their justified outputs. The kernel MUST NOT perform normalization (UNM), indicatorization (UINDM), scoring (USCM), folding (ULSAM), comparison (CPM), batch-result fabrication, or missing-pair completion inside `Select`. If a scalar “overall score” is desired, it must be declared upstream as an admissible scoring or comparator choice, not invented inside selection.

2. **Threshold discipline (acceptance is not selection).** Acceptance and admission thresholds are not selection criteria: they remain in their governing declarations and are applied only through `SelectEligibility`. Selection-level tie-breakers, `PortfolioMode`, and selected-set constraints may exist, but they MUST be explicit in current criteria or policy refs and bound by the actual selection application, never hidden as unnamed constants.

3. **Report‑only summaries inside suite closure.** Any scalar summaries, illumination metrics, or auxiliary “why not chosen” telemetry are report‑only unless explicitly promoted by policy, and MUST NOT be used as hidden dominance rules (`A.19.CHR:4.3.3`).
   Publishing and telemetry remain outside suite closure and are handled by established publication forms such as `G.10` or `PTM`, not as hidden tails inside selection.

4. **Specializations are explicit and disciplined.** A proposed specialization of `SelectorMechanism` must retain these local restrictions:

   * SlotKind invariance for inherited operations,
   * no new mandatory inputs to inherited `Select`,
   * added capabilities appear as explicitly declared new operations or additional results under the local `⊑⁺` notation.

   For the exact refinement, conservative-extension or equivalence claim, apply its own `A.6.1 §4.8` test, preserving the applicable operation, application and binding meanings. CC‑A19SelectorMechanism‑10 retains the exact predicate, endpoint facts and A.6.RCD gap branch.

5. **Planned use and actual binding.** On a P2W path, an A.15.2 baseline selects TaskSignature, CG-Spec and evidence-policy editions. A.15.3 supplies planned filling only for an independently declared receiving position. Actual Select arguments and returns are established under this declaration; the planned values remain available for a separately governed comparison with what occurred.

---

### A.19.SelectorMechanism:5 - Archetypal Grounding — informative

#### A.19.SelectorMechanism:5.1 - Tell

When comparisons are partial or set-valued, selection must not pretend there is a single best candidate by default. `SelectorMechanism` makes selection explicit, policy-bound, and replayable: it returns a set, including a singleton when the criteria determine one candidate.

#### A.19.SelectorMechanism:5.2 - Show, U.System example

**Scenario.** A platform team must pick a set of deployment options for a subsystem under multiple criteria: latency, cost, and regulatory risk. Comparisons are multi-criteria and do not induce a total order.

* `CandidateSetSlot = {OptionA, OptionB, OptionC}`.
* `CriteriaSlot` requires Pareto selection over the three unordered pairs `{A,B}`, `{A,C}`, and `{B,C}`, returns all non-dominated admissible candidates, and preserves the full selected set unless an explicit current criterion requires a singleton.
* The finite upstream comparison-application basis covers all three required pairs:

  * exact `Compare(OptionA, OptionB, ...)` has `GuardDecision = pass`: OptionB is strictly better than OptionA on latency, while OptionA is strictly better than OptionB on cost under the declared comparator. Its `ComparisonResultSlot` records those strict opposite wins, so neither dominates the other;
  * exact `Compare(OptionA, OptionC, ...)` has `GuardDecision = degrade` because OptionC lacks the required risk attestation. In this constructed case, the admitted comparator and partial-evidence policy explicitly define the empty token set as the lawful output for this restricted use; its output binding contributes no relation token about OptionC; and
  * exact `Compare(OptionB, OptionC, ...)` has the same explicit `degrade` basis and likewise contributes no relation token about OptionC.

  The Selector's `ComparisonResultSlot` argument is exactly the union of those justified member outputs, so its two tokens both trace to the `{A,B}` CPM application. No equality, worse-than, or `abstain` token is fabricated for OptionC.
* `MinimalEvidenceSlot?` is absent, so evidence is evaluated against `CGSpecSlot.MinimalEvidence`.
* The actual selection binds the three exact CPM applications and their pair, eligibility, and output bindings; the required-pair coverage and token trace; the deployment-option claim scope and selected regulatory `U.ContextSlice` members; the same predicate basis or explicit `none`; the reference plane and evaluation interval; and a `degrade` policy that permits exclusion of OptionC.

**Outcome.**

* Under that explicitly bound `degrade` policy, `SelectEligibility` returns `degrade`, excludes OptionC without coercing unknown evidence, and `SelectionSlot` returns `{OptionA, OptionB}`.
* If either required comparison involving OptionC instead had `GuardDecision = abstain`, that basis member would have no output binding, `SelectEligibility` would return `abstain`, and no selected-set value would be created. Neither guard value is a member of `ComparisonResultSlot` or `SelectionSlot`.
* The actual selection or eligibility application, finite CPM application basis, policies and returned value or explicit absence preserve the branch taken. An A.10 provenance account is added for the bounded reliance at issue; any dated Work claim requires the independent grounds in §4.1.

#### A.19.SelectorMechanism:5.3 - Show, U.Episteme example

**Scenario.** A methods group selects a declared set of analysis methods for a task. Candidates are method family refs. The group wants diversity in the selected set, but does not want diversity metrics to silently become dominance criteria.

* `CandidateSetSlot` = `{Family1, Family2, Family3, Family4}`
* The selection conditions declare which binary method-family comparisons are required. A finite basis identifies every relied-on CPM application, its exact pair, eligibility value, and own output binding; the Selector's `ComparisonResultSlot` argument is their exact justified-token union.
* `TaskSignatureSlot` is present and is the single policy-default slot or ref:

  * `PortfolioMode` and dominance regime,
  * budgeting and telemetry hooks (when used).
* `CriteriaSlot` declares that diversity signals are telemetry unless explicitly promoted by policy.

**Outcome.**

* `SelectionSlot` returns a selected set; any archive‑style behavior is a specialization and policy choice, not a hidden kernel default.
* The actual `Select` application retains its `TaskSignatureRef.edition`, effective criteria and `SelectionSlot` bindings for later explanation. Add provenance and dated Work only under their independent grounds in §4.1.

---

### A.19.SelectorMechanism:6 - Bias-Annotation — informative

This pattern intentionally biases selection authoring toward explicitness and admissibility.

* **Governance bias.** Bias toward explicit criteria and policy-reference records rather than implicit constants. Risk: perceived overhead. Mitigation: use existing prose or code when it makes the criteria recoverable, and centralize defaults via `TaskSignatureSlot` when used.
* **Architecture bias.** Bias toward set‑return semantics and against forced total orders. Risk: consumers may expect a single winner. Mitigation: make the choice rule explicit; a declared total order alone does not choose a candidate.
* **Epistemic bias.** Bias toward fail‑closed evidence handling and against unknown coercion. Risk: more `degrade` or `abstain` early. Mitigation: improve evidence pins and policy clarity; do not relax the kernel.
* **Practice bias.** Bias against embedding telemetry and publication into selection. Risk: teams want one step to select and report. Mitigation: keep those relations under their governing patterns; retain replay through actual selection bindings and the separately applicable Work, evidence and currentness relations in §4.1.

---

### A.19.SelectorMechanism:7 - Conformance Checklist

| ID | Requirement |
| --- | --- |
| **CC-A19SelectorMechanism-0** | **Mechanism declaration completeness:** one `U.Mechanism` episteme, its exact selection-operation-family `EntityOfConcernRef`, its effective reference scheme, the operation-local argument/result declarations, `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, and Applicability are recoverable under A.6.1. |
| **CC‑A19SelectorMechanism‑1** | **Single governing pattern:** the canonical SelectorMechanism `U.Mechanism` declaration is governed by `A.19.SelectorMechanism:4.1`; other descriptions cite this section rather than restating the kernel law. |
| **CC‑A19SelectorMechanism‑2** | **Set‑return default:** a conformant `Select` MUST be set‑returning by default; it MUST NOT silently collapse partial orders or incomparabilities to a single winner. |
| **CC‑A19SelectorMechanism‑3** | **No hidden thresholds or constants:** a conformant SelectorMechanism publication MUST NOT smuggle thresholds, weights, dominance rules, tie‑breakers, or default `PortfolioMode` fields. Selection‑level commitments MUST be explicit in `CriteriaSlot` and explicit policy defaults when used (e.g., via `TaskSignatureSlot`). Acceptance thresholds remain governed by `AcceptanceClauses`, `TaskSignature`, or `GateProfile` records and MUST be applied only via `SelectEligibility`. |
| **CC‑A19SelectorMechanism‑4** | **No hidden scalarization:** if `ComparisonResultSlot` is set‑valued or partial, a conformant publication MUST consume it as such; scalar summaries are report‑only unless explicitly promoted by policy outside suite closure. |
| **CC-A19SelectorMechanism-5** | **Evidence gating:** `SelectEligibility` returns `pass`, `degrade`, or `abstain`; missing or unknown evidence never yields `pass`. Candidate exclusion or restricted use is explicit in the current criteria or policy bound by the actual selection application. |
| **CC‑A19SelectorMechanism‑6** | **SlotKind discipline:** SlotKind tokens used in the SelectorMechanism intension MUST come from the CHR SlotKind lexicon (`A.19.CHR:4.2.1`). New SlotKinds require lexicon extension first. |
| **CC-A19SelectorMechanism-7** | **Bridge and reference-plane discipline:** a semantic crossing cites an F.9 Bridge only between two exact F.17 `SchemeSenseCell` values when its profile applies and direct predicate obtains; its C.2.1 bounded-use claim is separate and `CL` is optional. A ReferencePlane crossing cites its applicable relation and policy separately. A scheme, cell, or plane difference alone establishes neither relation. A false or unresolved required Bridge predicate permits no `pass`; use only the explicit `degrade` or `abstain` route already declared. A.10 enters only for current reliance, and B.3—including any locally defined `R_eff` calculation—only for an actual named assurance claim under its declared domain model and calculation. All remain outside selector-declaration content. |
| **CC-A19SelectorMechanism-8** | **Replay basis completeness:** recover the actual `Select` application, its candidate set, required binary comparisons, every exact upstream CPM application with pair, eligibility and own output binding or absence, token-to-producer trace, criteria and policy, `U.ClaimScope`, selected A.2.6 context slices, predicate basis, reference scheme and plane, evaluation window, derived token union, and returned `SelectionSlot` binding or explicit absence. Independently recover dated Work through the A.13 core and A.15.1 admission in §4.1, evidence use under A.2.4, reliance and provenance under A.10, currentness under G.11 and a result episteme under C.2.1 only when asserted by the account or consumed by the receiving use. A Select application does not itself require separately admitted upstream comparison Work. The output values carry none of this metadata. |
| **CC-A19SelectorMechanism-9** | **Planned-filling separation:** on a P2W path, A.15.2 carries intended editions/policies; A.15.3 typed filling applies only to independently declared positions. Actual Select applications carry effective argument/result bindings; dated selection Work and any relied-on A.10 provenance remain separately established. |
| **CC‑A19SelectorMechanism‑10** | **Extension discipline:** a proposed SelectorMechanism specialization MUST preserve inherited SlotKind designators and their meanings and add no mandatory input to inherited Select. For a claimed refinement, conservative extension or equivalence, apply the corresponding A.6.1 §4.8 preservation test, including application/binding predicates, identity and extent. The exact comparison predicate and endpoint facts must be established; use A.6.RCD’s missing-governor/substrate result when they are absent. The symbols ⊑ and ⊑⁺ alone establish none of these comparisons. |
| **CC-A19SelectorMechanism-11** | **Guard and gate separation:** `SelectorMechanism` publishes neither `GateDecision` nor `DecisionLog`; `SelectEligibility` returns `pass`, `degrade`, or `abstain` separately from the selected set. |
| **CC-A19SelectorMechanism-12** | **Selection-condition completeness:** `CriteriaSlot`, effective selector policies and defaults, and any `degrade` failure behavior are explicit and bound by the actual application; acceptance and admission predicates remain separate. |
| **CC-A19SelectorMechanism-13** | **Selection-scope completeness:** every actual application binds candidate universe, finite exact binary CPM application basis, required comparison coverage, token-to-producer trace, `U.ClaimScope`, selected A.2.6 context slices, A.19 predicate basis, effective reference scheme and plane, and explicit evaluation point or interval. No generic context input, optional structure, batch result, or label supplies them. |
| **CC-A19SelectorMechanism-14** | **Output separation:** `SelectionSlot` contains only the by-value selected candidate set. On `abstain` no output is fabricated; a reduced set under `degrade` requires explicit current policy. |
| **CC-A19SelectorMechanism-15** | **Comparison continuity:** selection cites the finite exact basis of binary CPM applications and may not silently change its membership, required coverage, member pairs, eligibility or output bindings, predicate basis, scope, selected slices, plane, or window. A justified change is a new application and may require recomparison. |
| **CC-A19SelectorMechanism-16** | **No generic result relation:** the A.6.1 operation application binds `SelectionSlot`; C.2.1 governs a durable selected-set episteme when needed; direct subject patterns govern other result relations. |
| **CC-A19SelectorMechanism-17** | **Finite comparison-basis coverage:** selection conditions derive the required binary comparisons; each is discharged by an exact CPM application, and every consumed relation token traces to its producing member output. A missing pair, untraceable token, or required member that abstains forces selector abstention rather than a fabricated batch result. |

---

### A.19.SelectorMechanism:8 - Common Anti-Patterns and How to Avoid Them — informative

| Anti-pattern                 | What it looks like                                                              | Remedy                                                                                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| GateDecision leakage | `Select` emits `GateDecision` or writes a decision log | Keep gate decisions in their governing patterns. `SelectEligibility` remains the mechanism predicate; the actual application retains its realized eligibility value and direct replay basis. |
| Forced single winner         | `Select` always returns exactly one candidate even under incomparability        | Return a declared selected set by default; if single winner is required, make it explicit in `CriteriaSlot` and ensure the induced order is admissible and declared |
| Hidden tie-breakers          | “If incomparable, pick lower cost” without declaring that as policy             | Move tie-breakers into explicit criteria or into declared comparator policies; never embed inside the kernel                                        |
| Scalarization by convenience | Replace set-valued comparison with a scalar “summary score” treated as decisive | Keep summaries report-only unless explicitly declared as admissible comparator outputs                                                                  |
| Unknown coerced to pass      | Missing evidence treated as acceptable                                          | Use tri-state `SelectEligibility`; unknown maps to `degrade` or `abstain`                                                                           |
| Selection does comparison    | Selection stage recomputes scoring or comparison internally                     | Keep comparisons upstream; `SelectorMechanism` binds exact CPM applications and consumes only their justified-token union in `ComparisonResultSlot` |
| One binary comparison treated as a batch | One `Compare(left,right)` application is said to cover three or more candidates, or a token union loses its producing applications | Bind a finite basis of exact binary CPM applications, derive required pair coverage from the selection conditions, and trace every consumed token to a member output |
| Selected set as replay record | Candidate universe, comparison ref, criteria, scope, evidence, or currentness are placed inside `SelectionSlot` | Keep `SelectionSlot` to selected candidates; bind use arguments on the actual application and use direct evidence, provenance, and currentness relations |
| Boundary drift | Selection reuses a token union after comparison-basis membership, coverage, member pair or eligibility, predicate, scope, selected slices, plane, or window changed | Treat it as another selection application and perform the required binary comparisons again when their governed basis changed |
| Publish inside selection | Selection emits a publication or telemetry relation as part of mechanism semantics | Keep publication and telemetry under their governing patterns; actual application bindings and applicable direct relations retain replay |

---

### A.19.SelectorMechanism:9 - Consequences

**Benefits**

* Preserves incomparable candidates when the criteria require them.
* Makes thresholds, weights and scalarization choices inspectable; correct selection still depends on applying the admitted criteria to the justified inputs.
* Supports replay through actual application bindings and the direct relations that the receiving use consumes.
* Supports evolvability: new method families and selection styles can be wired without changing the kernel signature.

**Costs and trade-offs**

* Selected-set results can require explicit downstream handling when a single decision is needed.
* Strict evidence discipline increases early `degrade` or `abstain` until criteria and evidence policies are explicit.
* Teams must make the selection criteria recoverable; existing descriptions may already suffice.

---

### A.19.SelectorMechanism:10 - Rationale

Selection is where many systems accidentally convert admissible but nuanced information into an unjustified scalar decision. Making selection a separate, explicit mechanism boundary achieves two things that matter for engineering management:

1. **Technical integrity:** the declared guard tests the admissibility and evidence conditions needed by this selection.
2. **Organizational clarity:** it makes defaults and thresholds discussable, reviewable, and maintainable as explicit policy references.

The set‑returning default is not a preference for large retained sets; it is a correctness safeguard when the order is not total. Single-winner outcomes remain possible when the criteria select one candidate from the admitted comparison outcomes.

---

### A.19.SelectorMechanism:11 - SoTA-Echoing

The research lines below supply application families and design comparisons. Their distinct output meanings and conditions remain with the cited methods; they do not establish the selector laws by themselves.

Concrete selector-family SoTA packages are cited through their current Part G pack or claim sheet when one governs the use. They connect through `CriteriaSlot` and `TaskSignatureSlot` references while kernel semantics remain unchanged.

#### A.19.SelectorMechanism:11.1 - SoTA alignment map (normative)

| SoTA practice pointer, post‑2015+                                                                               | Primary source examples, post‑2015+                                                                           | Where it connects to SelectorMechanism                                                                             | Adoption status |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | --------------- |
| Retain several candidates under explicit criteria | Quality Diversity, e.g., Pugh et al. 2016; Vassiliades et al. 2018 | QD supplies one retained-set application family. Its archive criteria are not the general Pareto-selection rule; declare the actual choice rule in each use. | Adapt |
| Use archive-based retained sets where diversity is part of the result, but do not silently promote it to dominance | Modern QD and archive practices post‑2015, including map-elites descendants and archive insertion policies | Expressed as policy‑bound criteria and report‑only telemetry unless explicitly promoted                            | Adapt           |
| Pair environments and methods in open-ended or co-evolutionary settings without breaking kernel semantics       | Open-ended environment-method pairing, e.g., Wang et al. 2019 and successors                                  | Expressed as candidate and criteria structuring plus admissible specializations; kernel unchanged                      | Adapt           |
| Admit a declared rejection option | Selective prediction, e.g., Geifman and El-Yaniv 2017 | The possibility of rejection informs FPF eligibility design. A selective-prediction rejection rule is not identical to this three-valued guard; apply each rule under its own conditions. | Adapt |
| Make architecture commitments traceable | ISO/IEC/IEEE 42010:2022 architecture description discipline | FPF assigns this declaration to one governing pattern; that assignment is an FPF design choice. | Adapt |

### A.19.SelectorMechanism:12 - Relations

* **Builds on**

  * `A.6.1` and its conformance checklist for mechanism identity, declaration content, applicability, and specialisation-chain discipline.
  * `A.19.CHR` for suite membership, suite protocol closure, SlotKind lexicon, and threshold and default discipline.
  * `G.0` for `CG‑Spec` admissibility and evidence declarations.
  * `A.19` for the exact `CharacteristicSpacePredicate` basis when one governs selection.
  * `A.19.CPM` for every exact binary `Compare` application in the finite basis, its pair, realized eligibility value, and own set-valued output binding.
  * `A.2.6` for `U.ClaimScope` identity and exact `U.ContextSlice` membership.
  * `A.19.CN` for `CN-Spec` governance card used as an explicit input.
  * `C.22` for `TaskSignature` as a policy-reference artifact when used.
  * `A.6.1 §4.2` for operation-local argument/result meanings and their SlotIndex projection; the local extension rule preserves inherited meanings.
  * `A.15.2` for the edition/policy baseline on P2W paths; `A.15.3` plus `A.19.CHR:4.7.2` for typed filling of independently declared positions.
  * `C.27.TA` for the explicit selection-evaluation point or interval.
  * `A.2.4`, `A.10`, and `G.11` for evidence-use scope, provenance, and currentness, separately from selection scope and output.
* **Used by**

  * `A.19.CHR` as the canonical `select` stage in CHR pipelines.
  * `G.5` as the primary conformance and specialization context for selector-based method dispatch and `PortfolioMode` policies.
  * `E.18` when this declaration is used by transformation-flow nodes. A.15.3 governs planned refs only for independently declared receiving positions; actual operation bindings and any dated selection Work retain their direct rules.
* **Coordinates with**

  * `CPM` and other admissible comparison stages as producers of the exact result bindings whose justified-token union fills the Selector's `ComparisonResultSlot` argument.
  * `ULSAM` and other admissible aggregation stages that must remain explicit rather than hidden inside selection.
  * `E.20` for governing-pattern discipline; `F.18` when a reusable name or alias needs to be chosen. An F.9 semantic Bridge requires its own predicate, not merely a source term.

### A.19.SelectorMechanism:End
