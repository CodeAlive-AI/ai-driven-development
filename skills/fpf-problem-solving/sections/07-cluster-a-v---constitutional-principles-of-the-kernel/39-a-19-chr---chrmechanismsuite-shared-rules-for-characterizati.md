## A.19.CHR - CHRMechanismSuite: Shared Rules for Characterization and Selection

> **Type:** Architectural (A)
> **Status:** Stable

**Use this when.** A characterization or selection task combines normalization, indicator choice, scoring and comparison, and the stages must agree on admissibility, uncertainty and the meaning of their results. A locally reasonable calculation can still be unusable downstream if it changes a scale, hides a default or discards a distinction needed for comparison.

**Start here.** Select the exact declaration edition for each of the six CHR roles in §4.2. For the intended protocol, resolve each stage to its operation and governing specifications before choosing input values. The first useful result is a chain whose arguments, results and stop conditions agree. §4.8.1 works this through from a baseline to a concrete selected set.

**Ordinary boundary.** For one operation, use its A.19 member pattern directly. For a different set of jointly used contracts, use A.6.7. For an edition/reference plan without shared CHR conditions, use A.15.2. A CHR suite describes the shared contract; actual applications, gate decisions and publication retain their own rules.

`CHRMechanismSuiteDescription` is the canonical `MechSuiteDescription` instance for the six CHR roles. Its selected edition can be cited through `MechSuiteDescriptionRef`. An ordinary A.15.2 WorkPlan records the chosen baseline; `CHRMechanismSuiteSlotFillingsPlanItem` is used only when A.15.3 typed filling is needed for an independently declared position.

### A.19.CHR:1 - Problem frame

A team compares options whose measurements use different units or scales. Normalization must preserve the distinctions its comparator needs; indicator choice must retain exact basis positions; scoring must respect the declared scale rules; selection must consume the comparisons actually made. Missing evidence can interrupt any stage.

When each stage silently chooses its own editions, defaults or handling of uncertainty, the final selected set no longer follows from one recoverable basis. A shared suite makes those conditions explicit while leaving each operation's law in its own declaration. On a P2W path, the plan records the intended editions and references; actual applications supply their own bindings later.

### A.19.CHR:2 - Problem

This pattern applies when a workflow (especially in Part G) needs lawful characterization over measurable slots/coordinates (e.g., in Q‑bundles), including normalization, indicatorization, scoring, aggregation, comparison, and selection.

### A.19.CHR:3 - Forces

* **No implicit crossings.** Identify the relations actually claimed or consumed: F.9 semantic correspondence, C.3.3 kind correspondence, or a separately governed plane relation. Use E.18/A.21 visibility and gate anchors when their actual crossing or gate is present. Context, entity, plane and edition changes alone create none of those relations.
* **CN‑Spec and CG‑Spec must remain the governing spec refs.** Mechanisms cite them; mechanisms do not duplicate them.
* **Strict separation of layers.** Universal CHR core vs discipline/method specializations vs generators vs packaging.
* **SlotKind invariance.** Specialisation chains must preserve SlotKind meaning and only refine ValueKind / strengthen guards/laws.
* **No silent scalarization / totalization.** Partial orders must remain set‑valued; any numeric summary is report‑only unless explicitly declared as a lawful comparator/policy.
* **P2W split.** Planned slot filling belongs to WorkPlanning; launch values belong to WorkEnactment.

### A.19.CHR:4 - Solution

Select the six declarations, cite one CN-Spec and CG-Spec baseline, and state the protocol under §§4.2–4.5. Check the arguments and result of each used operation against that baseline. Record planned editions in A.15.2 when a P2W path is involved; add A.15.3 typed filling only for an independently declared position. Actual launch values and any `FinalizeLaunchValues` witness belong to enactment.

The suite contains membership, shared obligations, references and permitted protocols. It supplies no operation result or gate decision.

#### A.19.CHR:4.0 - Resolve the contract before use

A usable step names the selected member declaration, its operation and the governing argument, result, law and admission content. Use §4.2.2 to locate the declaration and the selected baseline to resolve its edition. A missing contract or unresolved edition stops that dependent step; a stage name or source list cannot fill the gap.

#### A.19.CHR:4.1 - Objects published by this pattern

##### A.19.CHR:4.1.1 - `CHRMechanismSuiteDescription`

A concrete `MechSuiteDescription` instance whose role is to:

* enumerate the canonical CHR mechanisms (as `MechanismDeclarationRef`s),
* declare suite‑level obligations/invariants,
* declare suite‑level spec pins (refs only),
* declare admissible suite protocols (Uses pipelines),
* require an edition/reference baseline in WorkPlanning on P2W paths; add typed planned fillings only when their independently declared positions are current.

A.6.7 supplies the general suite form. This pattern selects the six CHR roles and their shared obligations, with the P2W baseline specified below.

##### A.19.CHR:4.1.2 - Planned baseline and conditional typed filling

Use ordinary A.15.2 WorkPlan content for the selected suite, declaration and CN-Spec/CG-Spec editions, method and comparator references, time rule, expected guards and any required crossing references. Address that content through the exact WorkPlan and its local locator.

Use `CHRMechanismSuiteSlotFillingsPlanItem` under A.15.3 only when a selected operation argument or relation position already has its own meaning, designation, ValueKind, cardinality and binding predicate. Cite that governing declaration and position. A suite field or a name in the CHR lexicon does not create such a position. A missing fact may remain unknown in the plan; a missing declaration must be recovered before typed filling. Actual bindings and launch witnesses remain with actual enactment.

#### A.19.CHR:4.2 - Canonical mechanism membership

**Tell.** Select one exact A.6.1 declaration contract for each of the following six CHR roles. The resulting `mechanisms` set contains six distinct declaration epistemes, not implementations or unqualified operation-family names:

1. `UNM` — Unified Normalization Mechanism
2. `UINDM` — Unified Indicatorization Mechanism
3. `USCM` — Unified Scoring Mechanism
4. `ULSAM` — Unified Lawful Scale Aggregation Mechanism
5. `CPM` — Unified Comparison Mechanism
6. `SelectorMechanism` — universal set‑returning selection kernel

**Show.**

```
CHRMechanismSuiteDescription.mechanisms :=
  [ UNM.IntensionRef,
    UINDM.IntensionRef,
    USCM.IntensionRef,
    ULSAM.IntensionRef,
    CPM.IntensionRef,
    SelectorMechanism.IntensionRef ]
```

**Membership semantics note (normative).**
`mechanisms` denotes a duplicates-free **set** of exact declaration epistemes; order carries no semantics. The displayed `…IntensionRef` labels are retained citation names for those declarations. In a concrete suite baseline, each resolves to one selected edition under A.6.7 §4.1. They are not references to a newly defined operation-family kind. Any intended ordering is expressed only in `suite_protocols`.

**Rationale.** This suite is unified by **governance card, admissibility gate, and Transport discipline** (CN-Spec + CG-Spec + Transport), with membership by exact operation declarations.

#### A.19.CHR:4.2.1 - CHR SlotKind Lexicon (suite‑wide minimum)

**Tell.** To prevent SlotKind drift across the CHR mechanism chain and across SoTA wiring modules, CHR mechanism declarations SHOULD use the SlotKind tokens from this lexicon whenever they refer to the corresponding semantic roles. New SlotKinds MAY be introduced, but only by first extending this lexicon (suite‑governed), then citing the new SlotKind from the affected mechanism card.

**Lexicon (minimum).** Tokens below are **SlotKind** names (not types). Concrete meanings, `ValueKind` / reference designation and binding rules come from the governing A.6.1 operation-local declarations; A.19 and G.0 constrain their domain use. A.6.5 relation SlotSpecs are not the source of these operation positions.

- **Core suite SlotKinds**
  - `CharacteristicSpaceSlot`
  - `CNSpecSlot`
  - `CGSpecSlot`
  - `ContextSlot`

- **Indicatorization**
  - `IndicatorChoicePolicySlot`
  - `IndicatorSetSlot` — A.19.UINDM's selected declaration-local basis positions, retained with the exact CharacteristicSpace basis; each position keeps its Characteristic and Scale
  - `JustificationSlot`

- **Scoring**
  - `InputProfileSlot`
  - `ScoreProfileSlot`

- **Aggregation**
  - `MeasureSetSlot`
  - `GammaFoldSlot`
  - `GammaTimeRuleSlot` *(optional)*
  - `AggregatedMeasureSlot`
  - `ContributorSetSlot` *(optional)*

- **Comparison**
  - `LeftProfileSlot`
  - `RightProfileSlot`
  - `ComparatorSpecSlot`
  - `ComparisonResultSlot`

- **Selection**
  - `CandidateSetSlot`
  - `CriteriaSlot`
  - `TaskSignatureSlot` *(optional)*
  - `SelectionSlot`

- **Evidence / admissibility (optional, policy‑bound)**
  - `MinimalEvidenceSlot` *(optional)*

**Note.** This lexicon is intentionally small and role‑based: it constrains naming, not method semantics. Method/discipline specifics belong in SoTA packs (G.2) and wiring‑only `GPatternExtension` modules, not in the suite core.

#### A.19.CHR:4.2.2 - Canonical Intension targets (no dangling refs)

**Tell.** Each `…IntensionRef` resolves through its governing pattern below to one exact A.6.1 declaration edition. These targets locate the declaration; the selected suite/WorkPlan baseline supplies edition resolution for use. A draft stub can locate unfinished work but cannot resolve an operation contract it does not declare.

**Canonical targets (normative anchors).**

- `UNM.IntensionRef` → `A.19.UNM`
- `UINDM.IntensionRef` → `A.19.UINDM`
- `USCM.IntensionRef` → `A.19.USCM`
- `ULSAM.IntensionRef` → `A.19.ULSAM`
- `CPM.IntensionRef` → `A.19.CPM`
- `SelectorMechanism.IntensionRef` → `A.19.SelectorMechanism`

#### A.19.CHR:4.3 - Suite obligations

`CHRMechanismSuiteDescription.suite_obligations` MUST be written using the **canonical obligation vocabulary** from A.6.7:4.2 and MUST include the following clauses (duplicates-free set semantics; order carries no meaning):

`{ bridge_only_crossings,
   two_bridge_rule_for_described_entity_change,
   transport_declarative_only,
   penalties_route_to_r_eff_only,
   guard_decision_tristate(pass|degrade|abstain),
   unknown_never_coerces_to_pass,
   gate_decision_separation,
   guard_lexeme_reservations,
   cg_spec_cite_required_for_numeric_ops,
   no_silent_scalarisation_of_partial_orders,
   no_silent_totalisation,
   no_thresholds_in_suite_core,
   crossing_visibility_required,
   planned_slot_filling_in_work_planning_only,
   finalize_launch_values_in_work_enactment_only,
   implementation_export_discipline_when_cited }`.

##### A.19.CHR:4.3.1 - Crossings, visibility, and penalties

* **`bridge_only_crossings`:** a semantic correspondence between distinct recovered local senses requires the obtaining F.9 Bridge and the bounded-use/reliance basis consumed by this use.
* **`two_bridge_rule_for_described_entity_change`:** a C.3.3 kind correspondence retains its own endpoints, obtaining and receiving-use conditions. If an F.9 correspondence is also used, establish it independently. EntityOfConcern change alone supplies neither relation. Plane-only claims stay under their direct governor.
* **`transport_declarative_only`:** the suite does not embed CL/Φ/Ψ/Φ_plane tables and does not introduce any additional graph edge kind beyond E.18 `U.Transfer`; it requires only refs/pins/anchors whose realization is mediated by E.18 / gate surfaces.
* **`penalties_route_to_r_eff_only`:** CL/Φ/Ψ/Φ_plane penalties route to `R/R_eff` only; `F/G` are invariant under penalty routing.
* **`crossing_visibility_required`:** an actual E.18 crossing in an independently selected TransformationFlowStructure retains its required CrossingBundle; an A.21 work-entry gate retains its applicable gate anchors. A changed edition pin triggers the recheck required by its receiving use, but does not itself create a crossing, Bridge or gate.

##### A.19.CHR:4.3.2 - Guards and gate separation

* **Guard decision tristate:** mechanism‑level guards return
  `GuardDecision := {pass | degrade | abstain}`.
* **Unknown never coerces to pass:** unknown/insufficient evidence MUST map to `degrade` or `abstain`, not to `pass`.
* **Gate decision separation:** mechanisms and suite objects MUST NOT publish `GateDecision` nor `DecisionLog`. `block` is gate‑only (OperationalGate(profile)).
* **Guard lexeme reservations:** `USM.CompareGuard` / `USM.LaunchGuard` are gate‑level pins; mechanism predicates use suffixes `…Admissibility` / `…Eligibility`.

##### A.19.CHR:4.3.3 - Numeric admissibility and order lawfulness

* **CG‑Spec citation required:** any numeric scoring/aggregation/comparison MUST cite CG‑Spec (SCP + ComparatorSet + MinimalEvidence + Γ_fold + Φ/CL pins), and MUST NOT embed a “shadow CG‑Spec” inside mechanisms/suite.
* **No silent scalarisation of partial orders:** partial order comparisons remain set‑valued; any scalar summary is report‑only unless explicitly declared as a lawful comparator/policy.
* **No silent totalisation:** absence of totality MUST NOT be hidden by “tie‑breakers” or implicit weights.

##### A.19.CHR:4.3.4 - P2W discipline

* **Edition/reference baselines use A.15.2 WorkPlan content. Typed planned filling uses A.15.3 only for independently declared positions.**
* **FinalizeLaunchValues in WorkEnactment only.**
* Suite and plan objects MUST NOT contain launch‑value witnesses.

##### A.19.CHR:4.3.5 - Thresholds and defaults

* **`no_thresholds_in_suite_core`:** acceptance thresholds live in AcceptanceClauses / TaskSignature / GateProfile, not in CHR suite core.
* **Default discipline (no competing defaults):** the suite MUST NOT introduce competing defaults. If a default is used (e.g., `PortfolioMode`), it MUST be cited from its single declared source (typically a TaskSignature or an explicit policy-id), and all other mentions are citations.

##### A.19.CHR:4.3.6 - Implementation export discipline (when cited)

* Suite MAY cite implementations (CAL/LOG/CHR) as refs, but:

  * LOG/CHR do not export Γ,
  * CAL exports exactly one Γ,
  * imports are acyclic.

##### A.19.CHR:4.3.7 - Claim reference index

The existing claim identifiers resolve to the rules below. The rules are stated once at their governing locations.

| Claim identifiers | Governing content |
| --- | --- |
| L-A67CHR-01 | §4.2 membership set semantics |
| L-A67CHR-02, L-A67CHR-03, A-A67CHR-02 | §§4.1.2 and 4.6 planned baseline and its separation from enactment |
| A-A67CHR-01 | §4.5 operation/edition resolution |
| D-A67CHR-01, D-A67CHR-02 | CC-A67CHR-1 kind and level |
| D-A67CHR-03 | §4.2 and CC-A67CHR-2 canonical membership |
| D-A67CHR-04 | §4.4 and CC-A67CHR-3 specification references |
| D-A67CHR-05 | §§4.3.1 and 4.4; CC-A67CHR-13 transport/crossing content |
| D-A67CHR-06 | §4.6 and CC-A67CHR-10 planned baseline |
| D-A67CHR-07, D-A67CHR-08 | CC-A67CHR-10a and CC-A67CHR-11 typed filling and plan/enactment separation |
| D-A67CHR-09 | CC-A67CHR-16 anchors required by the actual claim |
| E-A67CHR-01, E-A67CHR-02 | §4.6 and CC-A67CHR-14 baseline citation and actual enactment evidence |

#### A.19.CHR:4.4 - Suite spec pins

`CHRMechanismSuiteDescription.suite_spec_pins` MUST be refs‑only and MUST include:

1. **Required spec refs:** `{CNSpecRef, CGSpecRef}` (as required pins, not copied content).
2. **Required planned baseline:** cite the exact A.15.2 WorkPlan and content locator carrying the selected suite, declaration and spec editions. A typed A.15.3 item is additional only when §4.1.2 applies.
3. **Required edition pins / policy pins (when applicable):**

   * `editions{CG‑Spec, ComparatorSet, UNM.TransportRegistryΦ, …}` when the chosen protocol path is edition‑sensitive,
   * policy‑id pins for Φ/Ψ/Φ_plane when crossings are expected.

**Tell (discipline).** Spec pins are **anchors**; they do not embed tables (CL ladders, Φ registries) and do not introduce transport edges.

#### A.19.CHR:4.5 - Suite protocols

`CHRMechanismSuiteDescription.suite_protocols` follows A.6.7: each step resolves to one selected member declaration edition and one operation designator in that declaration. Its guards, laws, arguments and results come from that edition. Stage names below are readable labels, not substitute operation designators.

If `suite_protocols` is present, it SHALL include at least one protocol that is equivalent to the canonical **suite-closed** pipeline below (with `fold_Γ` explicitly optional).

The declaration-local bindings for the canonical stages are:

| Stage label | Governing declaration | Operation designator |
|---|---|---|
| normalize | selected `UNM.IntensionRef` edition, A.19.UNM §4.1; consume its directed value and preservation/loss basis, adding class use only under its conditions | `apply` |
| indicatorize | selected `UINDM.IntensionRef` edition, A.19.UINDM §4.1 | `Indicatorize` |
| score | selected `USCM.IntensionRef` edition, A.19.USCM | `Score` |
| fold_Γ, optional | selected `ULSAM.IntensionRef` edition, A.19.ULSAM | `Fold_Γ` |
| compare | selected `CPM.IntensionRef` edition, A.19.CPM §4.1 | `Compare` |
| select | selected `SelectorMechanism.IntensionRef` edition, A.19.SelectorMechanism | `Select` |

Resolve each cited edition before applying these bindings; a changed designator or contract requires a revised binding. A list of source pins alone selects no operation. If two editions remain eligible, the suite baseline must state the condition that selects one, or stop that dependent step with the unresolved choice.

**Show (canonical suite-closed protocol).**

```
normalize (UNM) →
indicatorize (UINDM) →
score (USCM) →
fold_Γ? (ULSAM) →
compare (CPM) →
select (SelectorMechanism)
```

**Tell.**

* The `fold_Γ` step is optional (explicitly optional, not implicit inside `score/compare/select`).
* `suite_protocols` encodes a pipeline/Uses contour between mechanisms; it does **not** define a specialisation relation (`⊑/⊑⁺`). A claimed refinement, conservative extension or equivalence uses its own `A.6.1 §4.8` content-preservation test, exact predicate and endpoint facts, including the applicable A.6.RCD missing-governor/substrate branch. Project extensions retain their independently declared restrictions; a pipeline order or ⊑/⊑⁺ label establishes no such comparison.
* Any publish/telemetry step is **outside** `suite_protocols` (to preserve WF‑MS‑2 closure) and is governed by established publication patterns (G.10 and/or PTM), not as “hidden tails” inside CHR mechanisms.

#### A.19.CHR:4.6 - P2W hook: planned edition and reference baseline

For each P2W path that uses the suite, record the chosen suite and member declaration editions, CN-Spec and CG-Spec, method/comparator references, time selection, and applicable guard or crossing references in A.15.2 WorkPlan content. That baseline selects the contracts expected by the protocol and remains separate from actual values and gate decisions.

When a downstream claim needs a typed planned filling, apply §4.1.2 and A.15.3 to the independently declared argument or relation position. At enactment, identify the actual application and its bindings under the selected declaration. The planned baseline alone establishes neither binding nor performed Work.

#### A.19.CHR:4.7 - Canonical concept card fragments

##### A.19.CHR:4.7.1 - `CHRMechanismSuiteDescription` as a concrete `MechSuiteDescription`

**Show (canonical skeleton; refs only).**

```
CHRMechanismSuiteDescription := ⟨
  mech_suite_id        : MechSuiteId,
  mechanisms           : [UNM.IntensionRef, UINDM.IntensionRef, USCM.IntensionRef,
                          ULSAM.IntensionRef, CPM.IntensionRef, SelectorMechanism.IntensionRef],

  suite_obligations    : SuiteObligations {
                          bridge_only_crossings,
                          two_bridge_rule_for_described_entity_change,
                          transport_declarative_only,
                          penalties_route_to_r_eff_only,
                          guard_decision_tristate(pass|degrade|abstain),
                          unknown_never_coerces_to_pass,
                          gate_decision_separation,
                          guard_lexeme_reservations,
                          no_thresholds_in_suite_core,
                          cg_spec_cite_required_for_numeric_ops,
                          no_silent_scalarisation_of_partial_orders,
                          no_silent_totalisation,
                          crossing_visibility_required,
                          planned_slot_filling_in_work_planning_only,
                          finalize_launch_values_in_work_enactment_only,
                          implementation_export_discipline_when_cited
                        },

  suite_spec_pins  : SuiteSpecPins {
                          required_spec_refs := {CNSpecRef, CGSpecRef},
                          required_planned_baseline_ref := exact WorkPlan ref + local baseline locator,
                          required_edition_pins? := …,
                          required_policy_id_pins? := …
                        },

  suite_protocols?     : SuiteProtocol[*],            // includes the canonical pipeline
  suite_notes?         : …,                            // didactic boundaries + anti-patterns
  suite_audit_obligations? : …                         // UTS+Path pins, crossings visibility, guard governing-pattern assignment
⟩
```

##### A.19.CHR:4.7.2 - Baseline content and conditional `CHRMechanismSuiteSlotFillingsPlanItem`

The baseline names the selected declaration edition for every protocol step, the CN-Spec and CG-Spec editions, and any selected method or comparator references. Retain the described entity, bounded context, CG-frame, path slice, publication scope and explicit time selector when they qualify the planned use; a reference plane may be derivable from its cited governing context. There is no implicit latest.

Expected `USM.CompareGuard` or `USM.LaunchGuard` pins identify their gate owner where needed to aggregate later `GuardFail` events. An expected crossing carries only the applicable obtaining Bridge/plane relation and policy references, plus a crossing-bundle anchor when its rule requires it. The baseline copies no governing table.

For an A.15.3 typed filling, cite the exact declaration edition and its independently declared argument or relation position. `target_slot_bearing_description_ref` cannot point to the suite merely because the suite lists a CN-Spec field. Reuse the position's actual meaning, designation and binding rules. In the UNM `apply` case, planning CN-Spec use first requires the actual selected operation's CN-Spec argument declaration; the suite's own citation is not that argument.

The baseline and typed plan contain planned values and references only. Actual launch values, `FinalizeLaunchValues`, actual bindings, `GateDecision` and `DecisionLog` retain their enactment or gate governors.

#### A.19.CHR:4.8 - Examples

##### A.19.CHR:4.8.1 - Worked case — two offers from baseline to selected set

**Situation and planned baseline.** The question is whether either offer can be discarded without accepting a worse price or defect-free proportion. Stipulate an A.15.2 WorkPlan `OfferReviewPlan@1`, local content locator `characterization`, selecting suite `OfferCHRSuite@1`. This case's suite has the six distinct member declarations in §4.2.2, each at its §4.1 content in the same publication edition as this example. Its stable `mech_suite_id` is `OfferCHRSuite`; its obligations are exactly the §4.3 clause set. The full canonical protocol is available, with Fold_Γ optional. The selected path uses `apply → Indicatorize → Score → Compare → Select`, under the operations' own eligibility evaluations.

The plan pins `OfferCHR-CN@1`, `OfferCHR-CG@1`, the methods and policies below, and the point `2030-01-01T00:00Z` in UTC. The suite requires those same references and the exact `OfferReviewPlan@1#characterization` baseline. No typed filling is needed for this ordinary reference selection. These are planned references; no application or result is claimed by the plan.

**Case specifications, outside the suite.** Take the two offers, lower-price/higher-quality Pareto rule and all-nondominated selection rule defined as `OfferPareto@1` and `OfferSelection@1` in A.6.7 §4.6. The raw case values here are A=(1000 eurocents, 0.8), B=(1200 eurocents, 0.9), stipulated exact rather than measured in a claimed real-world episode. `OfferCHRSpace@1` has basis positions `cost` and `quality`, with the price and defect-free-proportion Characteristics. Its input price chart uses eurocents; its normalized price chart uses EUR. Quality uses the same dimensionless ratio scale in both charts.

| Pinned case reference | Content used by the protocol |
| --- | --- |
| `OfferCHR-CN@1` | Admits A and B on this basis; binds the bearer identified by each coordinate/profile to `OfferScope@1`, selected slice set `{OfferSlice@1}`, the concept plane, the CHR reference scheme and the planned evaluation point. Its comparability mode is normalization-based into the EUR/quality chart. The admitted normalizers are `CentsToEUR@1` and `QualityIdentity@1`; indicator_policy is `BothPositions@1`. Both complete candidates satisfy acceptance, with no further threshold. |
| `CentsToEUR@1` | Configured ratio:scale method on cost values from 0 to 1,000,000 eurocents; n(x)=x/100 EUR. Bound coordinate set={cost}. Preserves price, equality and order; loses no distinction on this domain. |
| `QualityIdentity@1` | Configured ratio:scale method on quality values in [0,1]; n(q)=q. Bound coordinate set={quality}. Preserves all values and their order. |
| `BothPositions@1` | Select exactly {cost,quality} from OfferCHRSpace@1, retaining position meanings and order for profile projection. The policy is evidence-gated and uses the CG default; missing either required value means abstain. |
| `IdentityScore@1` | Description of the stipulated admitted identity-scoring Method: apply the identity to each normalized measure. Domain/codomain are price in [0,10000] EUR and quality in [0,1]; result cardinality is two measures. Preserve scales and polarities (lower price, higher quality). No aggregation or scalarization occurs. |
| `OfferCHR-CG@1` | SCP permits the two declared ratio-scale normalizations, identity scoring and componentwise order comparisons. ComparatorSet contains OfferPareto@1. MinimalEvidence requires the exact two input values, basis, configured-method declarations and their algebraic preservation facts. CN normalization evidence uses the same requirement. No evidence override or degrade branch is selected. |

Both normalizer instances and their method descriptions are declared by the case CN-Spec, with validity window `[2030-01-01T00:00Z, 2030-01-02T00:00Z)`. Their positive scale factors establish the stated preservation facts. The profiles retain their exact bearer, basis positions and the resulting EUR/quality chart. No quotient, class representative or additional CharacteristicSpacePredicate is used.

**Applied protocol, separate from the plan.** Stipulate the following actual mathematical invocation episodes, each extending from taking up its named inputs to returning its result. Its inputs bind by actual use and its results bind at that return under the selected declaration. The evaluation point qualifies the offers; it is not the calculation interval. All episodes retain the case's scope, slice set, scheme, plane, point, basis and cited evidence. This account asserts no dated U.Work.

| Resolved stage | Bound inputs and eligibility | Returned value |
| --- | --- | --- |
| `A.19.UNM §4.1 / apply` | Four invocations, one per coordinate: the bound normalizer, raw CoordinateValueSlot, OfferCHRSpace@1 and OfferCHR-CN@1. Each UNM_Eligibility evaluation passes: coordinate, method, domain, invariants, validity and evidence agree. | The cost invocations return 10 EUR and 12 EUR; the quality invocations return 0.8 and 0.9. Each has its own NCVSlot binding. |
| `A.19.UINDM §4.1 / Indicatorize` | For each bearer, OfferCHRSpace@1, OfferCHR-CN@1, BothPositions@1 and OfferCHR-CG@1; no MinimalEvidence override. The exact policy and complete evidence yield pass. | Each invocation returns {cost,quality}; the projected profiles retain those positions and their normalized values. |
| `A.19.USCM §4.1 / Score` | Each projected InputProfileSlot, OfferCHR-CN@1, OfferCHR-CG@1 and IdentityScore@1; no override. ScoreEligibility passes the admitted method, normalized input and evidence. | Two separate ScoreProfileSlot bindings: A=(10 EUR,0.8), B=(12 EUR,0.9). |
| `A.19.ULSAM §4.1 / Fold_Γ` | The baseline selects its declaration as the sixth suite member but skips this optional step. There is no multi-value fold in this use. | No fold application or output is asserted. |
| `A.19.CPM §4.1 / Compare` | The exact A/B score profiles, case CN/CG, OfferPareto@1 and the common use arguments. CompareEligibility passes; normalization refs and preservation facts are retained. | Invocation `cCHR` returns {A ∥ B}. |
| `A.19.SelectorMechanism §4.1 / Select` | CandidateSetSlot={A,B}; comparisonBasis={cCHR}; requiredComparisons={(A,B,OfferPareto@1)}; tokenProvenance maps A ∥ B to cCHR's own returned binding. ComparisonResultSlot is its exact token union. CriteriaSlot retains all nondominated candidates, selectorPolicy=OfferSelection@1, and TaskSignatureSlot is absent. The same CN/CG and use arguments apply, with no predicate or evidence override. Select consumes its exact SelectEligibility pass result. | SelectionSlot={A,B}. Both offers survive because each is better on one criterion. |

The suite's audit requirement is to recover these operation refs, effective arguments, guards and returned bindings, together with the baseline citation. Shared order and uncertainty obligations are satisfied without constructing a total score. There is no semantic, kind or plane correspondence, E.18 flow crossing, A.21 gate, implementation export or publication claim in this case; their conditional anchors are therefore inactive.

**Changed condition.** Move the evaluation point to `2030-01-03T00:00Z` while retaining the selected method validity windows. UNM_Eligibility returns abstain. The planned method refs remain readable, but there is no new admitted NCV and no basis for continuing this selected normalization-based path to a new selected set. Reusing yesterday's values by changing their date would fail their actual binding and use conditions. A new valid method baseline and new applications are needed.

The useful result is the justified retained set under one resolved contract chain. Acceptance or authorization to buy, an independently admitted dated Work account, and publication of the result are separate claims; none follows from {A,B} or from the plan. A PlainView may say “both offers remain; neither dominates at the stated evaluation point” and cite the baseline. It may not say “purchase approved” or erase the expiry stop.

##### A.19.CHR:4.8.2 - Variant — archive retention with report-only illumination

For an Archive-mode use, retain the selected set under the explicitly selected selector policy. The two-offer case can retain {A,B}; archive maintenance requires its own admitted policy and declarations. Record the exact DescriptorMap and DistanceDef editions when computing illumination, together with the policy declaring that result report-only. A separate CAL policy is required before illumination influences dominance. An archive label, descriptor display or diversity summary cannot silently change the comparison or discard either offer.

#### A.19.CHR:4.9 - Evolution rules

* **Kernel-first stability.** This suite is intentionally minimal. Adding a new core CHR mechanism to this kernel suite is a suite-version change and MUST be accompanied by alias docking (F.18) so existing references remain citeable. For exploratory or domain‑specific extra stages, prefer a suite variant (e.g., `A.19.CHR+` / `A.19.CHR.Extended`) or project‑level specializations (patterns P.\*) instead of mutating the kernel.
* **Mechanism specializations are not wiring.** Domain/project variants are expressed via A.6.1 (`⊑/⊑⁺`) under their governing pattern (typically a project pattern `P.*`), not by editing suite membership. The suite binds to exact declaration editions through `…IntensionRef`; the A.15.2 planned baseline records the selected contracts and any concrete method or realizer references. A specialization that changes a used contract requires the corresponding suite member and protocol binding to change.
* **Protocols evolve within the suite boundary.** Adding/changing suite protocols (A.19.CHR:4.5) is allowed as long as each protocol remains suite‑closed and does not import publish/telemetry as a mandatory step. If a protocol introduces a new required stage not present in membership, treat it as a suite variant rather than a protocol edit.
* **SoTA harvesting updates methods, not the kernel.** Updates from SoTA harvesting/synthesis (G.2) are carried via edition‑pinned `MethodDescriptionRef` / `ComparatorSpecRef` selections and wiring modules (`G.x:Ext.*`), preserving the selected declaration set while its content stays unchanged. If a SoTA update requires changing a mechanism’s signature/laws, the change happens in the governing A.6.1 mechanism card and MUST emit RSCR triggers from `G.Core`.
* **New mechanism families (outside CHR).** Introduce new mechanism kinds as new family-specific patterns under the appropriate mechanism family. If they require suite-level composition and P2W binding, add a corresponding suite pattern `A.6.7.<FamilyKey>` with an A.15.2 edition/reference baseline and A.15.3 typed filling only when independently declared positions require it, mirroring the governing-pattern assignment routing of this pattern.

#### A.19.CHR:5.1 - `U.System` vignette (Tell–Show–Show)

**Tell.** A system-level decision must select a declared set of options when measurable evidence comes from multiple slices (test rigs, simulations, field trials). Measurements are multi-scale and not always comparable without explicit normalization, and some evidence is missing or stale. The team needs lawful comparison and selection without forcing a single scalar “fitness”.

**Show.** Use the filled reference selection in §4.8.1 as the baseline: exact contracts, scales, methods, time rule and policies yield a retained set of two offers. When the inputs instead come from tests or field trials, replace the stipulated case evidence with the evidence required by the actual CN-Spec/CG-Spec; incomplete evidence follows the declared failure rule. A claimed dated Work and any launch witness require their independent enactment basis. Any actual semantic/kind/plane relation or flow/gate crossing retains its own required anchors.

**Show.** If the team instead embeds normalization inside scoring (“we always normalize to [0,1]”) or collapses a partial order into a single weighted sum, the suite protocol explicitness and “no silent scalarization/totalization” obligations make the violation legible at review time, and the planned baseline cannot honestly pin the missing UNM/ULSAM steps.

#### A.19.CHR:5.2 - `U.Episteme` vignette (Tell–Show–Show)

**Tell.** A research episteme compares methodological claims across traditions where some evaluation scales are ordinal (rank-based) and others are interval or ratio. The group wants to select a method family for a task while keeping uncertainty explicit and avoiding illicit aggregation (e.g., averaging ranks).

**Show.** The episteme’s planned baseline pins `CNSpecRef` (comparability mode and indicator policy) and `CGSpecRef` (SCP, ComparatorSet, MinimalEvidence, Γ_fold). The suite runs `UINDM` to select indicators, `USCM` to compute lawful score measures under SCP, `ULSAM` only when Γ_fold is explicitly selected, and `CPM` to compare without scalarizing partial orders. The selector returns a selected set rather than forcing a single winner.

**Show.** If a draft evaluation writes “take the mean rank and pick the minimum”, replace that step with a scale-lawful comparator declared in CG-Spec. For report-only telemetry, retain the rank distribution or another summary justified by the declared ordinal scale, such as a median when applicable. An arithmetic mean requires a separately justified quantitative model; calling it telemetry does not make ordinal averaging lawful.

### A.19.CHR:6 - Bias-Annotation

The following trade-offs matter when using the suite:

* **Gov.** Bias toward fail-closed admissibility and explicit auditability (applicable relation/crossing references, pinned spec refs, guard–gate separation). Mitigation: the tri-state `GuardDecision` allows uncertainty to degrade or abstain without forcing gate-level blocking; exploration can still proceed via explicit SoS‑LOG policy branches.
* **Arch.** Bias toward explicit node-level composition (E.18) and explicit planned baselines and conditional typed fillings. Mitigation: the suite fixes only the universal core; discipline-specific generators and extensions remain separate mechanisms connected by `Uses`, keeping the suite compact.
* **Onto/Epist.** Bias toward a strict separation of CN‑Spec and CG‑Spec spec refs, mechanisms (A.6.1), and planning epistemes (A.15.2; A.15.3 for typed fillings). Mitigation: specialization is explicitly supported (`⊑/⊑⁺`) and does not require inventing new kernel constructs; method diversity is expressed via MethodDescription refs and ComparatorSpec refs.
* **Prag.** Bias toward conservative uncertainty handling (unknown does not coerce to pass) may reduce decisiveness. Mitigation: “probe-only” and “sandbox” behaviors are permitted as explicit, audited degrade modes (policy-id + branch-id), not as silent coercions.
* **Did.** Bias toward explicit terminology and pins increases authoring surface area. Mitigation: this pattern provides a canonical protocol and ordinary baseline content with reusable references so authors can reuse a stable template rather than re-inventing local prose conventions.

### A.19.CHR:7 - Conformance Checklist

A CHR mechanism-suite publication set is conformant to **A.19.CHR** iff all applicable items below hold. Existing claim references resolve through §4.3.7.

#### A.19.CHR:7.1 - Suite object checks

**CC‑A67CHR‑1 (Correct kind and level).**
A conforming `CHRMechanismSuiteDescription` SHALL be a `MechSuiteDescription` instance and SHALL NOT be encoded as a `MechFamilyDescription`.

**CC‑A67CHR‑1a (Stable citation handle).**
A conforming `CHRMechanismSuiteDescription` SHALL include a stable `mech_suite_id` suitable for downstream planning and `U.Work.Audit` citation.

**CC‑A67CHR‑2 (Canonical membership).**
A conforming `CHRMechanismSuiteDescription` SHALL enumerate exactly the six CHR mechanisms (UNM, UINDM, USCM, ULSAM, CPM, SelectorMechanism) as `MechanismDeclarationRef`s.

**CC‑A67CHR‑2a (Membership set semantics).**
A conforming `CHRMechanismSuiteDescription.mechanisms` SHALL be duplicates-free and SHALL NOT treat order as semantic (WF‑MS‑1).

**CC‑A67CHR‑2b (No dangling IntensionRefs).**
Each member reference resolves to one exact declaration edition under §4.2.2, and each used operation resolves within that declaration. A stub without the contract is insufficient for use.

**CC‑A67CHR‑3 (Governing spec refs are pins, not copies).**
A conforming `CHRMechanismSuiteDescription` SHALL cite `CN‑Spec` and `CG‑Spec` as required spec refs and SHALL NOT duplicate them as “shadow specs”.

**CC‑A67CHR‑3a (Planned-baseline requirement is pinned).**
A conforming suite cites the exact WorkPlan and baseline locator that will hold its selected editions and references. A.15.3 typed filling is conditional on independently declared positions.

**CC‑A67CHR‑4 (Crossing discipline is complete).**
A conforming `CHRMechanismSuiteDescription.suite_obligations` SHALL include, at minimum:
`bridge_only_crossings`,
`two_bridge_rule_for_described_entity_change`,
`transport_declarative_only`,
`penalties_route_to_r_eff_only`,
`guard_decision_tristate(pass|degrade|abstain)`,
`unknown_never_coerces_to_pass`,
`gate_decision_separation`,
`guard_lexeme_reservations`,
`cg_spec_cite_required_for_numeric_ops`,
`no_silent_scalarisation_of_partial_orders`,
`no_silent_totalisation`,
`no_thresholds_in_suite_core`,
`crossing_visibility_required`,
`planned_slot_filling_in_work_planning_only`,
`finalize_launch_values_in_work_enactment_only`,
`implementation_export_discipline_when_cited`.

**CC‑A67CHR‑5 (Guard/gate separation).**
A conforming `CHRMechanismSuiteDescription.suite_obligations` SHALL:
1) enforce tri‑state guard decisions (`pass|degrade|abstain`),
2) enforce `unknown_never_coerces_to_pass`,
3) enforce guard–gate separation (no `GateDecision` / `DecisionLog` at mechanism/suite level; `block` remains gate‑only), and
4) enforce guard lexeme reservations (`USM.CompareGuard` / `USM.LaunchGuard` are gate-level pins; mechanism predicates use `…Admissibility/…Eligibility`).

**CC‑A67CHR‑6 (No hidden scalarization/totalization).**
A conforming `CHRMechanismSuiteDescription.suite_obligations` SHALL include explicit bans on silent scalarization of partial orders and silent totalization.

**CC‑A67CHR‑7 (No thresholds in core + single-source defaults).**
A conforming `CHRMechanismSuiteDescription.suite_obligations` SHALL include `no_thresholds_in_suite_core`.
If any suite protocol relies on defaults (e.g., `PortfolioMode`), the suite description and plan items SHALL cite those defaults from their single declared source (typically a TaskSignature or explicit policy-id), and SHALL NOT introduce competing defaults in the suite.

**CC‑A67CHR‑8 (Protocol explicitness + closure).**
If `suite_protocols` is present, a conforming `CHRMechanismSuiteDescription` SHALL:
1) express any dependence as an explicit protocol step (no hidden invocation of UNM/UINDM/ULSAM inside score/compare/select), and
2) satisfy WF‑MS‑2: every step resolves to one member declaration edition and one operation in that declaration, with no unresolved edition choice.

**CC‑A67CHR‑8a (Canonical protocol is available when protocols are published).**
If `suite_protocols` is present, a conforming `CHRMechanismSuiteDescription` SHALL include at least one protocol equivalent to:
`normalize (UNM) → indicatorize (UINDM) → score (USCM) → fold_Γ? (ULSAM) → compare (CPM) → select (SelectorMechanism)`,
where `fold_Γ` is explicitly optional.
Any publish/telemetry continuation is governed externally (e.g., by G.10 and/or PTM) and MUST NOT be encoded as a `ProtocolStep` inside `suite_protocols` (to preserve WF‑MS‑2 closure).

**CC‑A67CHR‑9 (Packaging separation).**
If protocols include `publish/telemetry`, it is governed by G.10 and/or PTM; the suite does not act as a pack or shipping publication.

#### A.19.CHR:7.2 - Planned baseline checks

**CC‑A67CHR‑10 (Planned baseline exists).** Every P2W path slice using the suite has an A.15.2 WorkPlan baseline with the selected suite and member declaration editions.

**CC‑A67CHR‑10a (Typed filling has its governor).** Use a `CHRMechanismSuiteSlotFillingsPlanItem` only when A.15.3 applies to an independently declared operation argument or relation position. Cite that declaration and position; a suite field is insufficient.

**CC‑A67CHR‑11 (Plan and enactment).** Planned references and values establish no actual binding, launch value, execution witness or gate decision.

**CC‑A67CHR‑11a (Use anchors).** Recover the described entity, bounded context, CG-frame, path slice, publication scope, reference plane when current, and explicit time rule needed for the declared use.

**CC‑A67CHR‑11b (Expected guards).** Expected guard pins belong to `{USM.CompareGuard, USM.LaunchGuard}` and name the responsible gate when later event aggregation requires it.

**CC‑A67CHR‑11c (Spec baseline).** The baseline cites CN-Spec and CG-Spec and their selected editions. Cite the independently declared position separately when either reference is also used as a typed planned argument filling.

**CC‑A67CHR‑12 (Exact edition resolution).** Each used declaration and operation has one governing edition. Multiple applicable editions require a selection condition before use; a source list or implicit latest does not resolve them.

**CC‑A67CHR‑13 (Applicable crossing references).** Expected crossings cite only the relations, policies and bundle anchors their governing rules require; the baseline embeds no CL/Φ tables.

**CC‑A67CHR‑14 (Audit traceability).** Later Work audit can cite the exact WorkPlan and baseline locator and distinguish actual bindings or deviations from planned values.

#### A.19.CHR:7.3 - MVPK face checks (when projected)

**CC‑A67CHR‑15 (Views do not add meaning).**
Any `TechCard(…)` / `PlainView(…)` projection of the plan item does not introduce new assertions beyond the plan item.

**CC‑A67CHR‑16 (Fail-closed pins on claimful faces).**
If a face publishes an edition reference, retain that exact reference. For a comparability or launch claim, also publish every anchor required by the relations, receiving policy and gate actually used; a gate-owned USM pin retains its `GuardOwnerGateSlot`. Missing a required anchor makes that claim nonconformant. A note that only pins a new declaration edition needs no invented BridgeCard, UTS crossing row, CrossingBundle or gate event.

### A.19.CHR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Avoid / repair |
|---|---|---|
| Using `MechFamilyDescription` as a suite container | Collapses “many implementations of one mechanism” into “many mechanisms”, mixing levels and breaking reuse constraints | Use `MechSuiteDescription` for multi-mechanism sets; use `MechFamilyDescription` only for multiple implementations of a single `U.Mechanism` |
| Embedding a second CG‑Spec or CL/Φ/Φ_plane tables inside the suite or plan item | Duplicates the governing spec refs and creates drift between planning, gates, and audit | Publish refs and pins only (`CGSpecRef`, `BridgeCardRef`, policy-id pins); keep tables in their canonical registries and cite them |
| Implicit UNM/UINDM/ULSAM “inside” score/compare/select | Breaks auditability and violates the suite protocol explicitness obligation | Make dependencies explicit as protocol steps (`Uses`) and cite the chosen mechanism instances in the planned baseline and audit pins |
| Hidden thresholds or weights in CHR core | Moves acceptance criteria into the wrong layer, defeating the declared defaults source and traceability | Keep thresholds in AcceptanceClauses, TaskSignature, or GateProfile; if a policy is needed, mint a policy-id and cite it explicitly |
| Scalarizing partial orders “for convenience” | Violates set-return semantics and hides incomparability | Keep comparisons set-valued via CPM and selectors set-returning; any scalar summary must be declared as report-only telemetry or as an explicit lawful comparator |
| Treating planned baseline as a launch witness | Smuggles execution facts into planning and blurs P2W separation | Record the edition/reference baseline in A.15.2; add A.15.3 fillings only for declared positions and keep actual bindings and launch witnesses in enactment |
| Using `CompareGuard` / `LaunchGuard` as mechanism lexemes | Collides with reserved gate-level pins and blurs guard vs gate responsibilities | In mechanisms use `…Eligibility` / `…Admissibility`; reserve `USM.CompareGuard` and `USM.LaunchGuard` for gate-visible pins |

### A.19.CHR:9 - Consequences

| Consequence | Upside | Cost / risk | Mitigation |
|---|---|---|---|
| Shared CHR contracts across uses | A later comparison can recover the same member declarations and joint conditions | Resolving the declarations and their editions takes effort | Reuse the baseline while its contracts and intended use remain applicable; keep method-specific choices in their governing descriptions |
| Explicit P2W planned baseline | Eliminates hidden slot filling and improves auditability of editions, time selectors, and crossings | Adds a planning plan item per path slice | Keep the plan item minimal (refs and pins only) and project it to views for readability when needed |
| Tri-state guard semantics | Avoids false precision and prevents unknown from silently passing | More conservative behavior can yield larger selected sets or more abstentions | Use explicit SoS‑LOG degrade branches for probe-only exploration while preserving traceability |
| Spec pins, not copied spec content | Reduces drift and keeps CN‑Spec/CG‑Spec as real centers of gravity | Requires discipline in authoring and review | Enforce “refs-only” at suite/plan level and use conformance items CC‑A67CHR‑3 and CC‑A67CHR‑13 to keep the surface clean |

### A.19.CHR:10 - Rationale

This pattern deliberately fixes the CHR core as a **description object** rather than a new “meta-mechanism” so that:

1. **Level separation stays clean.** The suite is a D-episteme that enumerates mechanisms and obligations; the mechanisms remain A.6.1 declaration epistemes with their own arguments, results, laws and admission conditions. This prevents a “god object” that re-implements A.6.1 inside a new container.

2. **Spec refs remain centralized.** CN-Spec and CG-Spec already define the governance card and admissibility gate that own comparability, normalization, indicatorization policy, and numeric admissibility. The suite requires those specs as pins and forbids duplicating them, making “one center of gravity” operational rather than rhetorical.

3. **P2W integration becomes explicit without turning planning into execution.** Ordinary A.15.2 content records the edition/reference baseline. Typed A.15.3 filling is needed only for an independently declared position; only enactment supplies actual bindings and launch witnesses.

4. **Uncertainty handling is made safe by construction.** Tri-state guard decisions are a minimal guard-decision form that supports admissible abstention and degradation while keeping gate decisions and decision logs in their proper place (OperationalGate(profile)).

In short: *governing specs are cited, not copied; plans are declared, not executed; and admissibility is a first-class surface, not a hidden tail.*

### A.19.CHR:11 - SoTA-Echoing

**Working question.** How should a team connect normalization, indicator choice, scoring, comparison and selection so that the final result still follows from the selected scales, evidence and method conditions when one of them changes?

For this question, **adapt** declaration-first workflow composition, the selected line compared in A.6.7 §11. [CWL v1.2.1's process references, requirements and abstract operations](https://www.commonwl.org/v1.2/Workflow.html#Operation) supply the substantive external model for distinguishing a described operation from a concrete process. The CHR adaptation makes the shared CN/CG conditions and each operation's result bindings explicit. CWL supplies neither these FPF laws nor the justification of the offer comparison.

The serious alternative is one pinned executable estimator pipeline, exemplified by [scikit-learn 1.9.1 Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html). It is attractive when fitting and sequential transformation already express the whole task. For the same five used CHR stages, compare it with the suite while holding the methods, data, policy and evidence requirements fixed. Both can calculate the two offers correctly. A pipeline plus explicit checks can also reject expired normalization. Its executable composition alone, however, does not state the case's scale-preservation argument or resolve the separately governed selection policy; those facts still need an inspectable account.

**Adopt** explicit method/specification resolution and **reject** a stage-name-only chain as sufficient justification. The suite accepts the extra reference cost to expose these conditions before choosing implementations. This is a trade-off in explanation and reuse, not a claimed runtime benefit or measured authoring saving. If a single existing pipeline already exposes every condition needed by the receiving use, reuse its account; creating another suite copy adds no gain.

The concrete effect is in §§4.0, 4.5 and 4.8.1: choose each contract before using a stage, retain every transformation's basis through the actual comparison, and stop the normalization-based path when its selected validity window fails. The final {A,B} remains a set even though the five stages could be packaged behind one callable interface. That packaging cannot add a singleton preference or purchase approval.

The two primary specifications are source models and a serious comparator; the choice for CHR is an explicit local architectural inference. They establish no empirical superiority of this pattern. Reopen the comparison if the receiving task becomes one fully self-contained executable pipeline, if its account already makes the same conditions cheaper to recover, or if a changed member contract makes the common baseline insufficient.

### A.19.CHR:12 - Relations

#### A.19.CHR:12.1 - Builds on

* **A.6.7 `MechSuiteDescription`** (the base suite description kind and obligations surface)
* **A.15.2 WorkPlan** for edition/reference baselines; **A.15.3** for conditional typed planned filling
* **A.6.1 `U.Mechanism`** (operation-local argument/result declarations, their derived SlotIndex, and the exact comparison tests in §4.8)
* **A.19 CN-Spec** and **G.0 CG-Spec** (governance card and admissibility gate)
* **E.18 / E.18** (P2W, crossings, UTS and Path pins)
* **E.10** (lexical and ontological discipline) and **E.19** (conformance style)

#### A.19.CHR:12.2 - Coordinates with

* **G.5** (selector semantics, set-return defaults, archive semantics and report-only illumination discipline)
* **G.10** and **PTM** (publication and telemetry as external steps, not suite internals)
* **A.21 OperationalGate(profile)** and **USM.Guards** (gate-level decisions and reserved guard pins)
* **C.23 SoS‑LOG** (explicit degrade branches such as probe-only and sandbox)

#### A.19.CHR:12.3 - Constrains and informs

* Constrains Part G universalization: G patterns should reference this suite for the universal CHR node set and express method and generator specifics only as (a) explicit specializations (`⊑/⊑⁺`) or (b) separate provider mechanisms connected via `Uses`.
* Informs other kits and suites: record the selected edition/reference baseline in A.15.2 WorkPlan content; use A.15.3 only where independently declared positions require typed planned filling.

#### A.19.CHR:12.4 - Notes for Part‑G

**Tell.** This pattern is intended as a universal core anchor for the Part‑G:

* G patterns not mixing universal CHR admissibility mechanics with CG-frame specifics, discipline-specific method content, and packaging concerns in one construct.
* Instead, they cite `CHRMechanismSuiteDescription` (universal node set and obligations) and keep specifics in explicit specializations or separate `Uses` providers.
* P2W integration cites the ordinary planned baseline and any applicable typed fillings, while actual bindings and launch witnesses remain enactment claims.

### A.19.CHR:End
