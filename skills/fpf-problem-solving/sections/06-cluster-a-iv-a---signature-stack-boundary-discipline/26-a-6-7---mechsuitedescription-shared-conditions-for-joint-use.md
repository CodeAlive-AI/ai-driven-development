## A.6.7 - `MechSuiteDescription` — Shared Conditions for Joint Use of Distinct Mechanisms

> **Type:** Architectural pattern.
> **Status:** Stable.
> **Normativity:** Normative [A] (Core).

**Use this when.** Several distinct operation declarations must be used together under shared conditions. Select their exact contracts, cite the required specifications, and state the permitted operation order.

**First useful result.** Each protocol step resolves to one declaration edition and one operation in that declaration. Two implementations of the same declaration do not become two members.

**Not this pattern when.** Use A.6.1 for one operation declaration, A.3.1 for a way of doing, and A.15.2 for an ordinary plan or edition baseline. A suite is useful only when several declarations have joint conditions to express.

A `MechSuiteDescription` is a Kernel **Description** token that names a **set of distinct** `U.Mechanism` (different declaration contracts, not different realizations of one contract) and declares **suite-level obligations**, **required spec pins**, and any **allowed usage protocols**, without conflating this with `MechFamilyDescription` or with publication `Pack`s.

**Plain-name.** mechanism suite description; mechanism suite passport.

**Builds on.** A.6.1 (`U.Mechanism` canonical form), A.6.5 (SlotSpecs where a RelationSignature is current), E.10 (lexical + ontological rules; strict distinction; minimal specificity; kind suffixes), E.18 (transformation-flow structure and crossing visibility), E.18.1 (P2W carry-through), A.21 (gate-level decisions).

**Used by.** Mechanism stacks governed by **shared admissibility, transport and audit obligations** and selected operation declarations, including shared suites reused by Part G patterns such as G.5.

**Declared vocabulary and references.**

* **Declares:** `MechSuiteDescription` (KernelToken, Description) and the record names used by its canonical form: `MechSuiteId`, `SuiteObligation`, `SuiteObligations`, `SuiteSpecPins`, `SuiteProtocol`, `ProtocolStep`, `SuiteAuditObligations`.
* **Reuses (by reference):** `U.Mechanism` (members), `MechFamilyDescription` / `MechInstanceDescription` (optional citations), existing pinned references such as `CN‑Spec` / `CG‑Spec` (as pins), and E.18/P2W notions (as obligations/pins), without introducing new U-kinds.

**LEX.TokenClass.**
* `LEX.TokenClass(MechSuiteDescription) = KernelToken.`
* `LEX.TokenClass(MechSuiteId) = KernelToken.`
* `LEX.TokenClass(SuiteObligations) = KernelToken.`
* `LEX.TokenClass(SuiteSpecPins) = KernelToken.`
* `LEX.TokenClass(SuiteProtocol) = KernelToken.`
* `LEX.TokenClass(SuiteAuditObligations) = KernelToken.`

**EntityOfConcern.** A finite set of distinct mechanism declarations intended for joint use. The description's Tech name ends with `…Description`.
Lexical note: do **not** prefix this token with `U.`. The `U.*` namespace is for admitted U-kinds and governed kernel values; `MechSuiteDescription` is a description value for a suite of mechanism declarations, not a root kind.

### A.6.7:1 - Problem frame

In FPF, a **mechanism** is a node-level `U.Mechanism` with explicit argument and result declarations for each operation and a declared LawSet/guards/transport/audit (A.6.1). Many architectures, however, require **a stable bundle of multiple different mechanisms** that are intended to be used together under shared admissibility and crossing discipline (e.g., a characterization chain, an admissibility-gated selection pipeline, or a universal Part-G kernel that multiple `G.*` patterns must reuse).

FPF already has `MechFamilyDescription`, but its meaning is: **many realizations of one and the same `U.Mechanism`**. That construct cannot correctly represent a bundle of different mechanisms (different declarations), and trying to overload it creates a level error.

Additionally, FPF reserves “Pack” for publication/shipping bundling (e.g., G.10); using “Pack” to mean “container of mechanisms” creates ontological collisions and downstream confusion.

### A.6.7:2 - Problem

The suite user needs one description that can:

1. represent a **set of distinct mechanisms** (distinct `U.Mechanism`),
2. declare **shared obligations** that must hold across the set (e.g., crossing visibility, admissibility-citation discipline, guard decision format, penalty routing),
3. provide **shared spec pins** (e.g., “this suite is governed by CN-Spec and CG-Spec”), without duplicating those spec contents,
4. constrain **allowed protocols** of use (allowed pipelines / permitted ordering), without turning the suite into a mechanism, and
5. preserve strict distinction among:

   * a suite of mechanisms (`MechSuiteDescription`),
   * a family of realizations of one mechanism (`MechFamilyDescription`),
   * a publication bundle (`Pack`, e.g., G.10).

### A.6.7:3 - Forces

1. **Strict distinction (level hygiene).**
   *“many mechanisms”* must not be encoded as *“many realizations of one mechanism”*.
   Violating this blurs specialization laws, mechanism-declaration invariants, and audit/crossing responsibilities.

2. **Minimal specificity + kind suffix discipline (E.10).**
   The token name should encode only what is essential: it is a description, it is about mechanisms, it is a suite.
   It must not capture a particular domain (e.g., CHR) in the Kernel name.

3. **Governing spec ref centrality (CN‑Spec and CG‑Spec).**
   Suites must cite governing spec refs as pins, not duplicate their internals, otherwise multiple competing admissibility centers arise.

4. **Transport and crossing visibility discipline.**
   An asserted semantic correspondence needs its F.9 Bridge; a kind correspondence needs its C.3.3 basis; a plane relation retains its own defining rule. Expose the anchors required by each actual relation and receiving use. An independently governed E.18 crossing or A.21 gate retains its required bundle or gate evidence. Any applicable penalty routes to `R/R_eff` only; suites do not embed CL/Φ/Ψ/Φ_plane tables.

5. **Guard vs gate separation.**
   Mechanisms can output tri-state guard outcomes and explanations; **gate decisions** (including `block`) and `DecisionLog` remain gate-level (`OperationalGate(profile)`). A suite must not collapse these layers.

6. **FPF is conceptual.**
   The suite is a conceptual descriptor: no implementation fields, no “lint rules”, no machine governance. The suite expresses obligations as conceptual constraints and required pins/anchors.

### A.6.7:4 - Solution

Declare the members and their shared conditions in a `MechSuiteDescription`:

#### A.6.7:4.1 `MechSuiteDescription` (data model)

`MechSuiteDescription` declares:

1. **Suite identifier:** a stable identifier for downstream citation.
2. **Membership:** a finite set of distinct mechanism declarations.
3. **Suite obligations:** shared invariants that every member (and any permitted composition of members) must respect.
4. **Suite spec pins:** required citations/pins to governing spec refs and other “anchor” references.
5. **Suite protocols:** allowed pipelines of use (permitted ordering and optional steps), expressed at the descriptive level.
6. **Suite audit obligations:** required audit/pin visibility for downstream uses (UTS/Path pins, crossing pins, guard pins), expressed as required anchors (not run-time values).
7. **Notes:** didactic boundaries and anti-pattern warnings.

A minimal canonical form:

```
MechSuiteId := Identifier  // PascalCase; stable citation handle. Versioning MAY be carried externally.

SuiteObligation := declared suite-level obligation
// Canonical reusable names (not exhaustive):
//   bridge_only_crossings,
//   two_bridge_rule_for_described_entity_change,
//   transport_declarative_only,
//   penalties_route_to_r_eff_only,
//   guard_decision_tristate(pass|degrade|abstain),
//   unknown_never_coerces_to_pass,
//   gate_decision_separation,
//   guard_lexeme_reservations,
//   cg_spec_cite_required_for_numeric_ops,
//   no_silent_scalarisation_of_partial_orders,
//   no_silent_totalisation,
//   no_thresholds_in_suite_core,
//   crossing_visibility_required,
//   planned_slot_filling_in_work_planning_only,
//   finalize_launch_values_in_work_enactment_only,
//   implementation_export_discipline_when_cited

SuiteObligations := { SuiteObligation[*] } // clause set; duplicates-free.

MechSuiteDescription := ⟨
  mech_suite_id: MechSuiteId ,
  mechanisms: MechanismDeclarationRef[+] ,     // references to exact member declarations
  suite_obligations: SuiteObligations ,
  suite_spec_pins: SuiteSpecPins ,
  suite_protocols?: SuiteProtocol[*] ,
  suite_audit_obligations?: SuiteAuditObligations ,
  suite_notes?: DidacticNotes
⟩
```

**Norms.**

* **Suite identifier.**
  `mech_suite_id` MUST be present and stable: it is the citation handle for downstream planning and `U.Work.Audit`.

**Well-formedness constraints (admissibility; non-deontic).**

* **WF‑MS‑1 (Membership set semantics).** `mechanisms` resolves to pairwise distinct A.6.1 declaration epistemes under C.2.1 identity; field order carries no semantics. Two citations of the same declaration are one member.
* **WF‑MS‑2 (Protocol closure and resolution).** Every `ProtocolStep.mechanism` resolves to one member declaration at its selected edition, and `step.operation` resolves to one operation designator in that declaration. The selected operation supplies its arguments, results, laws and admission conditions. A stage label or unqualified family name is insufficient.
* **WF‑MS‑3 (Suite ≠ Pack).** `MechSuiteDescription` does not carry shipping/publication payloads; use the applicable shipping or publication pattern for those results.
* **WF‑MS‑4 (Suite ≠ Mechanism).** `MechSuiteDescription` contains no `OperationAlgebra`/`LawSet`/execution semantics and is not admissible where a `U.Mechanism.*` node is required.

* **Membership is by exact declaration (order-free).**
  `mechanisms` MUST denote a duplicates-free set of distinct `U.Mechanism` members. Membership order has no semantics; any intended ordering is expressed only in `suite_protocols`. A suite is defined by selected operation declarations and suite protocols.

**Declaration reference and edition selection.** `MechanismDeclarationRef` is a reference to an independently identified A.6.1 `U.Mechanism` episteme, not a new kind. Resolve it under the effective reference scheme to its content and EntityOfConcern. The published edition used for that resolution must be explicit or uniquely determined by the cited suite baseline. When several editions qualify, state a selection condition that yields one before using a protocol step; otherwise return the unresolved alternatives. There is no implicit latest.

Changing declaration content, EntityOfConcern or effective reference scheme follows A.6.1/C.2.1 identity. Changing a carrier, layout or citation alone can leave the member unchanged. A changed guard or argument selects a different declaration contract and requires the affected protocol bindings to be checked again. A claim that two declarations concern the same operation family needs that subject's own identity rule; suite membership does not establish it. Distinct declaration contracts can be selected without inventing a universal operation-family kind.

* **No substitution by `MechFamilyDescription`.**
  A suite MUST NOT be encoded as a `MechFamilyDescription`.
  If desired, a suite MAY additionally **cite** `MechFamilyDescription` / `MechInstanceDescription` for particular members (e.g., “preferred realization for this context”), but such citations do not redefine membership.

* **No “Pack” meaning.**
  A suite MUST NOT be named or treated as a publication pack. `Pack` remains reserved for publication/shipping bundling (e.g., G.10).

* **No mechanism semantics in the suite.**
  A suite is a **Description**, not a mechanism: it does not define `OperationAlgebra` and does not absorb gate logic.

#### A.6.7:4.2 SuiteObligations (canonical obligation vocabulary)

`MechSuiteDescription` MAY declare any obligations. The canonical names in §4.1 support reuse across Part G and admissibility-gated characterization stacks; they are not an exhaustive inventory.

`SuiteObligations` SHOULD be written as an explicit, duplicates-free clause set. Select applicable clauses from the canonical vocabulary in §4.1 and state any additional obligations explicitly. The requirements below remain applicable under their stated conditions.

**Obligation meanings (normative).**

1. **`bridge_only_crossings`.**
   For an actual semantic correspondence between distinct recovered local senses, recover the F.17 endpoints and an obtaining F.9 Bridge, then the bounded-use and reliance claims required for this use. A suite creates none of those facts. A changed entity, reference scheme, plane or notation alone establishes no semantic crossing under A.6.4.

   1.1. **`two_bridge_rule_for_described_entity_change`.**

   * When both an F.9 semantic correspondence and a C.3.3 kind correspondence are claimed, establish each under its direct rule. Any separately claimed plane relation keeps its own governor. Changing the EntityOfConcern alone creates neither relation. Retain the separate use conditions and applicable penalty policy; do not invent a second Bridge from the change label.

   1.2. **`transport_declarative_only`.**
   * Well-formedness constraint: suite obligations do not introduce any additional graph edge kind beyond E.18 `U.Transfer` and do not embed CL/Φ/Ψ/Φ_plane tables. Any transport-related obligation is expressed only as referenced pins/anchors whose realization is mediated by E.18 / gate surfaces.

2. **`penalties_route_to_r_eff_only`.**
   Well-formedness constraint: CL/Φ/Ψ/Φ_plane penalties associated with crossing discipline route to `R/R_eff` only; suites do not define transport penalties that alter `F/G`.

3. **`guard_decision_tristate(pass|degrade|abstain)` and `unknown_never_coerces_to_pass`.**
   Well-formedness constraint: admissibility/eligibility outcomes use a tri-state guard result `GuardDecision := {pass|degrade|abstain}`. Unknown/insufficient evidence is not coerced to `pass`; it resolves to `{degrade|abstain}` under declared failure behavior (e.g., probe-only as a SoS‑LOG branch id, not as a new decision value).

4. **`gate_decision_separation`.**
   Well-formedness constraint: suites do not define or use `GateDecision` values (including `block`) as part of mechanism/suite semantics. Gate-level outcomes and `DecisionLog` remain on `OperationalGate(profile)`.

5. **`guard_lexeme_reservations`.**
   Well-formedness constraint: `USM.CompareGuard` and `USM.LaunchGuard` denote gate-owned guard events/pins; member mechanisms and suite protocols use `…Admissibility` / `…Eligibility` for guard predicates, not the reserved gate lexemes.

6. **`cg_spec_cite_required_for_numeric_ops`.**
   Well-formedness constraint: any member operation that performs numeric comparison/aggregation/admissibility-sensitive scoring cites the applicable `CG-Spec` (and relevant subrefs) as spec pins, rather than embedding equivalent local admissibility content.

7. **`no_silent_scalarisation_of_partial_orders` and `no_silent_totalisation`.**
   Well-formedness constraint: if a member mechanism induces a partial order, it preserves set-/relation-valued semantics; it does not silently reduce to a scalar/total order. Any totalization is explicit and policy-bound.

8. **`no_thresholds_in_suite_core`.**
   Well-formedness constraint: suite core does not publish acceptance thresholds (“passing scores” / hidden cutoffs). Thresholds belong to acceptance clauses / task signatures / gate profiles.

9. **`crossing_visibility_required`.**
   Well-formedness constraint: any GateCrossing relevant to suite use publishes a `CrossingBundle` (E.18) and can be cited as an audit anchor.
   Apply E.18 only for an independently selected TransformationFlowStructure and its actual governed crossing; apply A.21 for a current work-entry gate. An edition, entity or notation change alone supplies neither that crossing nor a semantic Bridge.
   Suites may require `CrossingBundleRef` / UTS / Path pins and policy-id pins as anchors, and MUST NOT embed CL/Φ/Ψ/Φ_plane tables.

10. **`planned_slot_filling_in_work_planning_only`.**
    Well-formedness constraint: any planned slot filling used as a baseline for suite use is authored in `WorkPlanning` as a planned baseline (no run-time slot instances; no launch values).

11. **`finalize_launch_values_in_work_enactment_only`.**
   Well-formedness constraint: `FinalizeLaunchValues` (and any witness of actual launch values) occurs only in `U.WorkEnactment`; neither the suite nor any planned-baseline WorkPlanning plan item is a place for launch values.

#### A.6.7:4.3 SuiteSpecPins

A `MechSuiteDescription` MUST be able to declare required spec pins as references, not as duplicated content. Canonically:

```
SuiteSpecPins := ⟨
  required_spec_refs?: {CNSpecRef?, CGSpecRef?, ...},
  required_edition_pins?: EditionPin[*],
  required_policy_id_pins?: PolicyIdPin[*],
  required_planned_baseline_ref?: PlannedBaselineRef?
⟩
```

**Norms.**

* If the suite is admissibility-gated for characterization, `CNSpecRef` and `CGSpecRef` MUST be required (as references/pins).
* Spec pins are citations and anchors. They do not replace the underlying `…Spec` objects.
* A suite may require an edition/reference baseline in ordinary A.15.2 WorkPlan content. Address it through the exact plan and its local content locator; it supplies no launch value or gate decision.
* Use A.15.3 typed planned filling only when an existing declaration member independently supplies the position meaning, designation, cardinality and actual-use predicate. A suite Description field is not a SlotSpec or operation argument merely because a plan names it. Missing planned information can remain unknown in the plan; a missing governor requires recovery or definition of that member before typed filling. Actual launch bindings and any FinalizeLaunchValues witness remain with actual enactment.

#### A.6.7:4.4 SuiteProtocols

A suite MAY describe allowed protocols (pipelines) as descriptive constraints on how suite members are intended to be composed. A `SuiteProtocol` describes the member-operation sequence. Its description:

* MUST name the member mechanisms it uses (explicitly; no “implicit use”),
* MAY mark steps as optional,
* MUST NOT introduce hidden crossings or hidden admissibility steps,
* MUST identify any “publish/telemetry” as an external step of the surrounding protocol, realized through existing publication surfaces (e.g., Part G shipping), rather than as a hidden tail inside a mechanism. This external step is not a `ProtocolStep` in the suite-member sequence.

A canonical shape for the suite-member sequence:

```
SuiteProtocol := ⟨
  steps: [ ProtocolStep₁, …, ProtocolStepₙ ],
  invariants?: ProtocolInvariant[*],
  notes?: DidacticNotes
⟩

ProtocolStep := ⟨
  mechanism: MechanismDeclarationRef, // resolves to the exact selected edition
  operation: declaration-local operationDesignator,
  optionality: {required|optional},
  requires_pins?: PinRef[*]
⟩
```

#### A.6.7:4.5 SuiteAuditObligations

A suite MAY require that downstream use provide certain audit anchors. These are **requirements**, not run-time values. A suite audit obligation MAY include:

* required `UTS` + `Path` pins,
* required crossing-surface visibility pins for any crossing relevant to suite use,
* required presence of `USM.CompareGuard` and/or `USM.LaunchGuard` **pins** (not gate checks),
* required declaration of guard ownership (e.g., a `GuardOwnerGateSlot` anchor),
* required expression of guard violations as `GuardFail` events aggregated by the guard-owning gate (per `GuardOwnerGateSlot`), not as extra mechanism/suite states,
* required policy-id pins for any degrade/sandbox/probe-only branches (SoS‑LOG branch id anchors).
* required parity/selection-grade pins when applicable (e.g., when suite use claims parity-grade comparison/selection surfaces downstream).

**Norm.** A suite must never publish a `DecisionLog` or `GateDecision`. If the suite requires guard pins, it requires their **presence** as anchors so that the gate-level owner can aggregate `GuardFail`s and decide `degrade|block` per gate profile.

#### A.6.7:4.6 Examples

**Example 1 — compare two offers and retain the nondominated set.** The question is whether either offer can be discarded without accepting a worse cost or quality. This is a stipulated mathematical use; the following specifications and applications are case facts, not empirical measurements or dated Work claims.

**Selected contracts and specifications.** The baseline `OfferChoiceB1` selects `Dcmp = A.19.CPM §4.1` and `Dsel = A.19.SelectorMechanism §4.1`, including their operation-local declarations, application/binding predicates, identity and extent rules, in the same publication edition as this case. These references mean that edition's content, not a later revision. Resolve another publication's references again before reuse. Their effective scheme is the CHR reference scheme declared there.

The case's independently stipulated specification editions are:

| Reference | Content consumed in this use |
| --- | --- |
| `OfferCN@1` | Admits exactly offers A and B with complete cost and quality profiles on `OfferBasis@1`. Comparability is componentwise on those same positions and scales, with no normalization requirement. Both candidates meet acceptance; there is no additional acceptance threshold. |
| `OfferCG@1` | Admits `OfferPareto@1` in ComparatorSet. SCP permits order comparisons on each declared scale and conjunction of those comparisons; it permits no cross-characteristic addition. MinimalEvidence requires both exact profile values and their common basis. |
| `OfferPareto@1` | Lower cost and higher quality are better. X dominates Y iff X is no worse on both positions and strictly better on at least one. Equal profiles return parity; a trade-off returns the pair's incomparability token. No epsilon or tie-breaker applies. |
| `OfferSelection@1` | Select every nondominated candidate. Compare every unordered pair once under OfferPareto@1. No singleton preference or hidden default applies. Missing required comparison, failed evidence or unknown value means abstain; no degrade branch is enabled. |

These definitions are the cited case specifications, outside the suite description. `OfferBasis@1` gives position `cost` the price Characteristic and EUR ratio scale, and position `quality` the declared defect-free proportion Characteristic and a dimensionless ratio scale. The already admitted measure profiles are A=(10 EUR, 0.8), B=(12 EUR, 0.9). Both use these positions, with complete exact stipulated values.

**Filled suite description.** `OfferChoiceSuiteDescription` has `mech_suite_id = OfferChoiceSuite`, membership `{Dcmp, Dsel}`, required spec references `{OfferCN@1, OfferCG@1}`, and required policy/comparator references `{OfferSelection@1, OfferPareto@1}`. Its shared obligations are tri-state eligibility with unknown never passing, explicit numeric admissibility, set-valued comparison/selection without hidden scalarization or totalization, and gate-decision separation. The one protocol contains four required steps:

| Selected member | Operation | Required references |
| --- | --- | --- |
| Dcmp | CompareEligibility | OfferCN@1, OfferCG@1, OfferPareto@1 |
| Dcmp | Compare | the same three references |
| Dsel | SelectEligibility | OfferCN@1, OfferCG@1, OfferSelection@1 |
| Dsel | Select | the same three references |

The protocol invariant requires both members to use the same admitted profiles, scope, slices, scheme, plane and evaluation point, and Select to consume the actual returned Compare binding. The audit obligation is to recover those effective arguments, eligibility judgments and output bindings, including token provenance. There is no public naming, semantic/kind/plane correspondence, flow crossing, gate, implementation export or planned-launch claim in this use, so it requires none of their conditional anchors. The description supplies no operation law or runtime output of its own.

**Application and result.** Outside the description, stipulate one completed application of each of the four selected operations, in the listed order. Each takes up the following arguments and ends at its own return; those four invocation episodes are distinct from the evaluation point they share. `OfferScope@1` delimits the comparison and selection of A and B for this offer question; `{OfferSlice@1}` is its selected A.2.6 context-slice set. Both members bind that scope and set, the CHR reference scheme, the concept reference plane, and evaluation point `2030-01-01T00:00Z` in UTC. No additional CharacteristicSpacePredicate or MinimalEvidence override is used. Normalization has no dependency because OfferCN@1 compares the original matched scales.

The comparator guard uses A as LeftProfileSlot and B as RightProfileSlot, with OfferCN@1, OfferCG@1 and OfferPareto@1, and returns `pass`: both profiles are complete, admitted and scale-compatible. Application `c1` then returns `ComparisonResultSlot = {A ∥ B}`. Its returned binding, not an equal saved token, supplies the selection basis.

The selector guard binds CandidateSetSlot={A,B}, comparisonBasis={c1}, requiredComparisons={(A,B,OfferPareto@1)}, tokenProvenance={A ∥ B ↦ c1's returned binding}, and ComparisonResultSlot={A ∥ B}. CriteriaSlot contains the single clause “retain all nondominated candidates”; selectorPolicy is OfferSelection@1; TaskSignatureSlot is absent because no default is obtained from it. CN, CG and the common use arguments are those above. Coverage is complete and the guard returns `pass`. Select consumes that exact eligibility result and returns `SelectionSlot = {A,B}`. Incomparability is retained; neither offer is silently chosen as the winner.

**Changed condition and stop.** If B's quality is unknown, OfferCG@1's evidence condition fails: CompareEligibility returns `abstain`, no Compare result is fabricated, and the selector has no complete comparison basis. Its guard returns `abstain`, with no Select application or selected-set result. Changing only the selected comparator declaration to an unresolved edition also stops at protocol resolution before calculation. A suite-shaped record cannot cure either missing basis.

The description answers which contracts can be jointly used and under what conditions. The four stipulated applications answer what happened in this case. A gate decision, dated Work account or published result would need its own independently established basis.

**Declaration-change case.** The CHR `normalize` stage resolves to `apply` in a selected UNM declaration edition. Let D1 admit `pass` and policy-supported `degrade`, as A.19.UNM §4.1 does. Suppose a separately proposed D2 changes the operation guard to `pass` only. For the same input whose eligibility is `degrade`, D1 permits the qualified output and D2 does not. Merely pinning both sources or writing `UNM + normalize` cannot decide which contract governs. A step selecting D1 remains on D1; substituting D2 changes the member contract and requires the new guard to pass. These are illustrative edition names, not claims that both editions are published.

Two different realizers of D1 still use one member. UNM and the independently identified UINDM declaration are different members. A differently formatted publication of D1 can preserve the declaration identity. A new declaration about an independently established same family is still a new contract when its content changes; any family-continuity claim remains separate. Thus the protocol can resolve exactly even where family continuity is irrelevant or unresolved.

**Example 2 (non-conformant).** Misusing a family as a suite:

```
CHRMechanismFamily : MechFamilyDescription := { UNM, UINDM, USCM, ... }
```

This is a level error: `MechFamilyDescription` is reserved for realizations of a single mechanism declaration.

**Example 3 (non-conformant).** Turning a suite into a hidden gate:

* The suite declares `GateDecision` values or embeds a `DecisionLog`.
* The suite defines acceptance thresholds (“pass score ≥ 0.7”) as part of suite obligations.
* The suite embeds Φ/CL tables or invents an additional graph edge kind beyond E.18 `U.Transfer`.

All violate the separation between mechanism/suite descriptions and gate-level operational control.

### A.6.7:5 - Archetypal Grounding

A suite is an archetypal mechanism-suite “passport”:

* It answers **what mechanisms exist in the bundle** and **what shared invariants** make their composition lawful.
* It provides **shared governing spec anchors** (pins) that downstream planning and work must cite.
* It remains descriptive: it does not contain run-time outputs, and it does not replace the transformation-flow structure selected under E.18 for composition and crossing visibility.

### A.6.7:6 - Bias-Annotation

Common biases this pattern guards against:

* **Overloading “family”.** Treating “many different mechanisms” as “many realizations of one mechanism” destroys level hygiene and encourages semantic drift across members.
* **Publication conflation.** Using “pack” semantics to smuggle publication/shipping obligations into the meaning of a mechanism bundle.
* **Gate conflation.** Treating suite-level obligations as gate decisions (“block”) instead of keeping `block` at the gate layer.
* **Convenience totalization.** Collapsing partial orders into scalars “for ease of selection”, which undermines set-return semantics and admissibility gating.

### A.6.7:7 - Conformance Checklist

A `MechSuiteDescription` is conformant iff all applicable items hold:

**CC‑A.6.7‑1 (Correct level).** The suite’s `mechanisms` enumerate **distinct** `U.Mechanism` members. The suite is not encoded as `MechFamilyDescription`.

**CC‑A.6.7‑2 (Description token, not `U.*`).** The suite token is a Description token and MUST NOT be introduced under `U.*`. Its name ends with `…Description`.

**CC‑A.6.7‑3 (No execution semantics).** The suite MUST NOT define mechanism blocks (`OperationAlgebra`, `LawSet`, etc.) and MUST NOT be used as a mechanism node.

**CC‑A.6.7‑4 (No gate decisions).** The suite MUST NOT define `GateDecision`, MUST NOT publish `DecisionLog`, and MUST preserve gate/mechanism separation.

**CC‑A.6.7‑5 (Spec pins, not duplication).** If the suite is admissibility-gated for numeric comparison/aggregation/scoring, it MUST require `CG-Spec` citation pins (and SHOULD require `CN-Spec` pins where applicable). It MUST NOT duplicate spec content as “local CG-Spec”.

**CC‑A.6.7‑5a (CN+CG pins for admissibility-gated characterization).** If the suite is admissibility-gated for characterization, it MUST require both `CNSpecRef` and `CGSpecRef` as pins (references), consistent with A.6.7:4.3.

**CC‑A.6.7‑6 (Transport discipline preserved).** The suite MUST NOT introduce transport exceptions. An actual semantic crossing must recover its obtaining Bridge and bounded use under its direct rule, with any applicable penalties routed to `R/R_eff` only. Entity, scheme, plane or notation changes alone establish no Bridge.

**CC‑A.6.7‑7 (Tri-state guard discipline when used).** If the suite declares admissibility/eligibility semantics, it MUST use `GuardDecision := {pass|degrade|abstain}` and MUST NOT coerce unknown to pass.

**CC‑A.6.7‑8 (No thresholds in core).** The suite MUST NOT publish acceptance thresholds or “passing scores”. Thresholds must remain in acceptance clauses / task signatures / gate profiles.

**CC‑A.6.7‑9 (Crossing visibility anchors).** If suite use consumes an actual semantic crossing or an independently governed E.18 crossing/A.21 gate, require only that claim’s applicable visibility and audit anchors, including Bridge, CL, policy, UTS or Path pins when its direct rule requires them. A changed edition alone creates none of those objects; keep the exact changed edition pin without manufacturing a crossing.

**CC‑A.6.7‑10 (Suite id present).** The suite MUST declare `mech_suite_id: MechSuiteId` so that downstream planning/audit can cite it stably.

**CC‑A.6.7‑11 (Independent correspondence conditions).** A claimed kind correspondence MUST satisfy C.3.3 and retain the calibration and use conditions actually required there. When the use also relies on an F.9 semantic correspondence, establish that Bridge independently and retain both channels' applicable policies and penalties. A new EntityOfConcern of the same kind or a plane-only change creates neither correspondence by itself.

**CC‑A.6.7‑12 (Implementation export hygiene when cited).** If the suite cites realizations/implementations, the citations MUST preserve export/import discipline (LOG/CHR: no Γ export; CAL: exactly one Γ; imports acyclic).

**CC‑A.6.7‑13 (No Pack conflation).** The suite MUST NOT be introduced, named, or used as a publication/shipping `Pack`.

**CC‑A.6.7‑14 (Protocol closure & explicitness).** Each step resolves to one member declaration edition and one operation designator in that declaration (WF‑MS‑2). The operation's argument, result, law and admission meanings are recoverable. No unresolved edition choice, implicit operation or implicit crossing can supply that resolution.

**CC‑A.6.7‑15 (P2W split preserved when applicable).** If the suite requires a planned-baseline pin, that baseline MUST be a `WorkPlanning` plan item and MUST NOT contain launch values or `FinalizeLaunchValues` witnesses; such witnesses remain `U.WorkEnactment`-only.

### A.6.7:8 - Common Anti-Patterns and How to Avoid Them

1. **Anti-pattern: “Family-as-suite”.**
   Using `MechFamilyDescription` to list multiple distinct mechanisms.
   **Fix:** use `MechSuiteDescription` for “many mechanisms”, and keep `MechFamilyDescription` for “many realizations of one mechanism”.

2. **Anti-pattern: “Pack-as-suite”.**
   Naming/using the suite as a `Pack`.
   **Fix:** reserve `Pack` for publication/shipping bundling; use `Suite` for mechanism bundles.

3. **Anti-pattern: “Suite contains admissibility tables”.**
   Duplicating CG‑Spec or embedding CL/Φ/Ψ tables in suite obligations.
   **Fix:** publish pins and references only; keep admissibility content in `...Spec` and policy registries; keep crossing realization in E.18/gate surfaces.

4. **Anti-pattern: “Suite is a hidden gate”.**
   Introducing thresholds, `block`, or `DecisionLog` in the suite.
   **Fix:** suite declares guard formats and required pins; the gate issues decisions.

5. **Anti-pattern: “Implicit calls”.**
   A protocol implies “normalize happens somewhere” without explicit member and pin visibility.
   **Fix:** protocols enumerate steps and required pins; E.18 `Uses` edges remain explicit.

### A.6.7:9 - Consequences

**Benefits.**

* Eliminates level confusion between “family of realizations” vs “bundle of mechanisms”.
* Provides a Kernel governing pattern for universal obligations reused across multiple patterns (notably Part G universalization).
* Makes admissibility/transport/audit obligations shared and explicit, reducing semantic drift across member mechanisms.

**Costs.**

* Introduces an additional `MechSuiteDescription` publication that must be maintained as suites evolve.
* Requires discipline: suites must remain descriptive and must not become “meta-mechanisms” or “hidden gates”.

### A.6.7:10 - Rationale

Characterization and admissibility-gated selection pipelines are unified by:

* shared governing spec refs (e.g., CN‑Spec / CG‑Spec),
* shared conditions for actual semantic, kind and plane relations, independently governed flow/gate crossings, and any penalties routed to `R_eff`,
* shared guard semantics (tri-state, no coercion),
* and explicit protocol constraints (allowed pipelines).

Encoding this unity as “one mechanism” or “one family” forces false commonality and invites hidden semantics. A dedicated **suite descriptor** preserves modularity and keeps the level separation clean.

### A.6.7:11 - SoTA-Echoing

**Question and selected answer.** How can a practitioner reuse several operation contracts under one set of conditions without selecting an implementation prematurely? For this question, **adapt** the explicit process-reference, input/output and requirement separation in [CWL Workflow v1.2.1, §3.3 and §4.3](https://www.commonwl.org/v1.2/Workflow.html#WorkflowStep). Its [abstract Operation](https://www.commonwl.org/v1.2/Workflow.html#Operation) describes inputs and outputs before binding a concrete process. This is the best-known-line candidate for declaration-first composition here; it does not establish FPF admissibility or operation identity.

**Serious alternative.** A pinned executable pipeline is preferable when the task is already to fit and run compatible estimators. [scikit-learn 1.9.1 Pipeline, `steps`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) exposes named estimator steps; each has fit, and intermediate steps have transform. It is a substantive composition alternative, not evidence that every characterization contract should have that interface.

For OfferChoice, compare both approaches with the same two contracts, four operation uses and four specification references. **Adopt** explicit member/operation resolution and one common specification baseline; **reject** the shortcut of identifying these contracts only by stage names or selected realizers. An executable pipeline could carry the same facts through adapters and metadata, but those additions still need their declarations and checks. The suite keeps them inspectable before an implementation exists. The deliberate cost is another reference layer; it offers no execution or performance advantage. Once executable estimators and their composition fully answer the question, use that pipeline and do not add a suite merely for documentation.

This choice is expressed in §4.1's exact declaration/edition resolution, §4.4's separate protocol and the filled §4.6 case: a returned comparison binding supplies selection, and absent evidence stops the chain. The architectural comparison is a local inference from the stated use and these primary specifications, not a measured productivity result or a claim that either source defines FPF. Reopen it if a receiving use needs only one already complete executable pipeline, if an additional reference layer hides a required condition, or if a rival represents the same distinct contracts and joint conditions with less total reader work.

### A.6.7:12 - Relations

* **Relates to A.6.1:** suite members are `U.Mechanism`; the suite does not replace the mechanism definition.
* **Relates to A.6.5:** member operation declarations retain A.6.1 argument/result meanings, ValueKinds and binding rules. A.6.5 applies only where a cited `RelationSignature` independently declares participant SlotSpecs; there SlotKind stability, correct refMode and non-semantic SlotIndex remain required.
* **Relates to E.18 / P2W:** suite protocols describe intended composition; use E.18 for the selected transformation-flow structure and its crossings, and E.18.1 for P2W carry-through.
* **Suite conformance:** Suite-level conformance uses the conceptual checklist in §7; suites require pins/anchors rather than procedural validation.
* **Relates to G.10:** suites are not packs; G.10 handles shipping of Part-G outputs as a SoTA pack, while E.17 publishes reader-facing forms of an already accepted engineering account.

### A.6.7:End
