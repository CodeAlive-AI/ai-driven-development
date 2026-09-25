## G.5 - Method-Family Registry, Dispatch and Selected-Set Result Declaration

> **Type:** General (G)
> **Status:** Stable
> **Normativity:** Normative

**Intent.** Help an engineer use a dispatcher and registry for rival method families and state selector-facing set outcomes. The outcome distinction covers retained alternatives and members jointly included for one named use without collapsing plurality into one hidden scalar winner.

**Primary working reader and object.** An engineer or framework author who already has a set of identified candidates or members and must state the selector-facing result—outcome kind, members, ordering, named use when required, and basis pins—for a named downstream use, without also claiming a choice, Work, or publication occurrence that has not happened.

### G.5:0 - Use this when
When loop-engineering work retains several already identified candidates for downstream use—for example, loop candidates, harness variants, method families, workflow-store entries, or DPF framework candidates—or when several already identified values are all included for one named use, use `G.5` only when the live claim is the selector-facing declaration of that set result. The declared result states the outcome kind, members or keyed member entries, ordering status, named use when applicable, and basis pins. It does not prove that any member improved, that work occurred, that a local choice has been made, or that the result is available to an audience.

Use `Shortlist` or `RankedShortlist` for alternatives retained for later choice. Use `JointUseSet` only when every named member is included for one bounded use. This joint-use branch consumes exact member identities under their own rules; it does not require `MethodRef`, a method-family registry row, or Method classification for framework editions or other non-Method values.

When an earlier choice or other current inclusion basis has already fixed the exact members, use `G.5-6 DeclareSetResult` with those member refs, the named use, inclusion conditions, ordering, and sufficient basis pins. This branch declares selector-facing result content without running method-family registration or `G.5-3 Select`; non-Method members never enter those method-family operations.

For ordinary method-family dispatch, open `G.5` when two or more already admitted Methods are live under grounded selector rows for the same declared task and the current question is the selector-facing set result: which candidates remain admissible, whether the emitted result may truthfully order them, or whether it must be a shortlist, narrowed handoff, abstain, or escalation. If the live question is still one local choice among available options, first constitute the exact C.11 choice assertion under its predicate. Reuse already grounded method-family rows when they exist; do not rebuild a registry on every run. Create a new reusable row only when the grouping itself must recur, carry family-level policy, be versioned, or be published. Crossing, evidence/reliance, assurance, stable public identity, and actual publication are conditional branches, not an entry fee.


For Method dispatch, resolve each exact A.3.1 Method and the row's independent grouping basis under S1 (§4.2). An unresolved member or grouping basis blocks that row. If the claim concerns actual selection, use S3's application and Work-admission conditions; a result declaration alone supplies no such occurrence. S5 governs any separately needed result episteme, public identity and publication claim.

Typical selector situations include:

- Methods or generators from several families are admissible for the same declared task family or work target
- you need one selector to return a `Shortlist`, `RankedShortlist`, `JointUseSet`, one `SpecialistHandoff`, one other narrowed handoff plan, or one abstain outcome without pretending that there is always one scalar winner or that all set results are alternatives
- the declared result must carry enough basis pins for its named downstream use—for example, later comparison, handoff, or escalation—without changing its declared outcome kind or any applicable public selected-set label

### G.5:0.1 - What goes wrong if missed

- rival families are compared under silent comparator drift, hidden baseline changes, or unspoken crossing costs
- the selector hides one dogmatic winner even when only a partial order is admissible
- selector-facing result content stays hidden inside `C.11`, `C.19`, or `C.24`, so the G.5 result no longer states which upstream choice, pool treatment, or enactment result it consumes and what set result it declares
- exploration, open-ended, or specialization pressure leaks in as one architecture convenience rather than one explicit policy-bound choice

### G.5:0.2 - What this buys

- one registry that keeps rival method families disjoint but dispatchable
- one selector result form that uses the closed `SelectorOutcomeKind` rules in §4.4b and the closed `SetResultFamily` set when the result is set-shaped
- one trace addressable by DRR and SCR records with explicit basis pins instead of one hidden selector rationale
- one explicit selected-set result that states the outcome kind, applicable public label, retained members or keyed joint-use entries, ordering, named use where required, handoff content, and basis pins instead of leaving them implicit upstream

Registry and dispatch remain the primary selector question here; the explicit selected-set result closes that question without replacing registry or dispatch.

### G.5:0.3 - First-minute questions

- Which exact members and grouping or inclusion basis are already established?
- Are they alternatives for later choice or members all included for one named use?
- Does the declared comparison justify ordering them?
- Which eligibility, evidence or other receiving-use conditions actually apply?
- What result can be handed over, and what prevents a complete result?
- Does the current question additionally claim actual selection, composition, a relation between meanings, public identity or publication? Open only the applicable branch in §4.2.

### G.5:0.4 - First output

State one `SelectorOutcome` under §4.4b: its kind, applicable members or keyed entries, ordering, named use and inclusion conditions where required, handoff or blocking content, and sufficient basis pins. Use the quick card in §4.4c. For an ordinary result over grounded rows, direct refs to the grouping, eligibility and comparison basis plus the S3 audit refs suffice; the same compact record can carry them.

A prior C.11 choice, C.19 pool-policy result, C.24 next action or another governed inclusion basis can supply the inputs. G.5 states the resulting membership or handoff. Exact framework editions retain their own identities and use `G.5-6 DeclareSetResult`; E.4.PFR governs their dependency or compatibility claims. Add a stable public identity only when needed. For audience availability, use E.17's source-backed face and E.24.PUB's publication conditions through S5.

### G.5:0.5 - Minimum ordinary slice and bounded non-use

**Situation.** A pump-maintenance team has two already admitted A.3.1 Methods, `ThresholdTrendReviewMethod-E2` and `SpectralResidualReviewMethod-E1`, behind the exact project-local selector rows `<ThresholdTrendReview-local, R3>` and `<SpectralResidualReview-local, R2>`. These are `MethodFamilyRowRef` values: each fixes its row edition, exact `MethodRef[]`, and declared grouping basis `PumpTriageCandidateGrouping-E1`. The same `TaskSignatureRef=PumpVibrationTriage-T1` and effective reference scheme apply to both. The task signature requires a 24-hour series input and a 30-minute review budget, and both declared Method interfaces meet those constraints. No G.4 CAL gate is current in this ordinary case, so `TaskMapRef` is absent. No admitted comparator justifies ordering one above the other. The live `G.5` question is now how to surface that admissible set, not which pump action a decision-maker should choose.


The minimum truthful result is:

```text
GroundedCandidateRows = [
  { methodFamilyRowRef = <ThresholdTrendReview-local, R3>,
    MethodRef = [ThresholdTrendReviewMethod-E2],
    groupingBasis = PumpTriageCandidateGrouping-E1 },
  { methodFamilyRowRef = <SpectralResidualReview-local, R2>,
    MethodRef = [SpectralResidualReviewMethod-E1],
    groupingBasis = PumpTriageCandidateGrouping-E1 }
]

SelectorOutcome(

  selectorOutcomeKind = SetResultOutcome,
  setResultFamily = Shortlist,
  members = [<ThresholdTrendReview-local, R3>, <SpectralResidualReview-local, R2>],
  ordering = unordered,
  basisPins = [<ThresholdTrendReview-local, R3>,
               <SpectralResidualReview-local, R2>,
               PumpTriageEligibility-E1],
  auditRefs = [DRR-PumpTriage-01, SCR-PumpTriage-01],

  nextUse = maintenance_method_handoff

)
```

**What changes in practice.** The team stops leaving the retained pair implicit in a comparison note and stops saying “the spectral method is best.” It emits one unordered `Shortlist` that another receiver can cite, with the exact survivors and basis visible, while making no local-choice, actual-use, or winning-method claim. A later receiver can request one missing comparator, use the bounded handoff, or open its separately governed decision question without rewriting either Method or inventing a winner.


**Near misses and non-use.** Do not use `G.5` merely because several names appear in one list.

- If the Method-dispatch candidates are only labels, descriptions, cards, or unresolved references, require A.3.1 and C.2.1 before dispatch.
- If the current question is one local choice among already available options, use `C.11`; if it is the policy for retaining or retiring live candidate lines, use `C.19`; if it is enactment planning after choice, use `C.24` for the plan and the applicable A.15/A.6 patterns for actual Work and operation applications.
- If the current object is only a composition sketch, keep the S4 template; use B.1.5 only for a qualified composite Method and A.22 only for an independently selected Structure.
- If no rival candidate set, selector result, narrowed handoff, abstain, or escalation is current, do not open `G.5`.
- Open F.9, A.10, B.3, stable registry or UTS identity, and E.24.PUB only for an actual crossing, relied-on evidence, assurance claim, reusable identity, or audience-availability claim respectively; their absence does not invalidate the smaller same-scheme selector result.

#### G.5:0.6 - Reuse a local grouping, then register it publicly when needed

The pump team in §0.5 already dispatches through R3 and R2. That unordered shortlist requires no new row. If the grouping of both Methods must recur across triage runs, the team can define:

```text
MethodFamilyRowRef = <PumpReviewCandidates-local, R1>
MethodRef[] = [ThresholdTrendReviewMethod-E2, SpectralResidualReviewMethod-E1]
GroupingBasis = PumpTriageCandidateGrouping-E1
EligibilityBasis = PumpTriageEligibility-E1
TaskSignatureRef = PumpVibrationTriage-T1
ComparisonBasis = no admitted ordering; retain admissible alternatives unordered
```

The grouping criterion is “these admitted review Methods are candidates for pump vibration triage using the stated 24-hour input and 30-minute budget.” This project-local row fixes those exact members and basis; changed membership or an action-changing policy makes R2. It requires neither a UTS row nor an AssuranceProfile when this ordinary use has no assurance gate. A later real gate still consumes its required evidence and follows its unknown/fail behavior.

If the team instead intends a stable public registry entry, its proposed public continuation can be `<PumpReviewCandidates, P1>`, linked by an explicit naming/continuity mapping to the local R1 grouping. P1 retains the same exact Method refs and grouping criterion, adds the typed `EligibilityStandardRef` for the pump task and an `AssuranceProfileRef` stating expectations for its declared uses, and satisfies UTS naming/publication requirements under S1 and CC-G5.6. Registration is complete only when those public-contract obligations are met. For this P1 example, `PumpTriageEligibilityStandard-E1` states the two Methods' required 24-hour series and 30-minute budget, with unknown when a required input cannot be determined. `PumpTriageAssuranceProfile-E1` names the evidence expectations and failure behavior for the declared triage uses; `UTS-PumpReviewCandidates-P1` supplies the public name and continuity mapping to R1. P1 registration consumes these completed declarations and that UTS entry alongside the unchanged exact member/grouping basis. A missing one leaves public registration incomplete. The assurance profile supplies no B.3 result.

R1 itself completes through RegisterFamily with the six values shown above: neither AuthoringBase nor AuthoringMinimal is activated because this local grouping has no CG-Frame use. P1 adds the three public references just described and activates UTSWhenPublicIdsMinted. Now suppose a later G.5-3 Select use is governed by `PumpTriage-CG-E1`, whose MinimalEvidence clause requires a valid sensor calibration for the cited vibration series. Its CN/CG editions and frame pins are required. If the calibration input is missing, the evidence predicate is unknown and this example's gate rule returns abstain; neither successful local R1 registration nor completed public P1 registration makes that selection pass.

Making local R1 available to the project audience may itself be an E.24.PUB publication occurrence when that pattern's conditions obtain. Conversely, the intention or declaration of P1 establishes no availability. Neither branch creates a Method or an ontic family relation. Non-Method joint-use members continue through `DeclareSetResult` with their existing identities and inclusion basis.

### G.5:1 - Problem frame


The exact `CG‑Frame` card from **G.1** and `SoTA Synthesis Pack@CG‑Frame` from **G.2** name the frame, `EntityOfConcernRef`, ReferencePlane, source rows, and rival internally coherent **method families** (and sometimes **generator families**) that may address the same declared task. If their breadth is used as a premise, cite G.2's pack `CoverageJudgementRef` and its HarvestPolicy basis. Registration does not recount cards as families; a combined method/generator coverage result does not establish method-only coverage for dispatch.

At the same time, the scale and coordinate definitions from **G.3** and the typed operator-argument and result declarations from **G.4** make admissible calculi and acceptance clauses explicit - enough to formulate *eligibility*, *assurance*, and *admissibility* constraints, but not enough to pick "the method" without collapsing plurality.

You need a **notation‑independent** way to:

1. register method families and generator families as *auditable, versioned* entries,
2. select, compose, or fall back among them at run time for a concrete task instance,
3. declare stable selected-set results, including retained-alternative and all-member results, and publish stable identities to UTS when required, and
4. emit RSCR‑relevant triggers and pins without inventing new “shadow specs”.

### G.5:2 - Problem

How to design a **general, auditable dispatcher** that:

* preserves **pluralism** (families from competing Traditions stay disjoint) while remaining **dispatchable** (selection is possible and explainable);
* does **not embed algorithmic dogma** in the core selector kernel;
* when expressions carry distinct F.17 source-local meanings, requires the complete crossing path—exact local senses, an obtaining F.9 Bridge, a separate bounded-use proposition, and the appropriate reliance or assurance branch—while treating pins as audit references rather than as the crossing facts;

* produces **set-valued outcomes** when only partial orders are admissible or when every named member is included for one bounded use, without confusing those meanings; when exact non-Method members already have a current inclusion basis, it declares that result without routing them through method-family selection;
* cleanly separates:

  * **selector object set and components** (registry, selector boundary, and result-declaration records),
  * **universal Part‑G invariants** (carried by `G.Core`),
  * **method-specific and generator-specific semantics** (carried only through `Extensions` blocks).

### G.5:3 - Forces

* **Pluralism vs. forced totalisation.** Many selection regimes are inherently partial-order; forcing a scalar winner often creates inadmissible semantics.
* **Evidence realism vs. hard gates.** Eligibility and acceptance frequently depend on incomplete evidence; selection must remain auditable under tri-state unknowns.
* **Reuse vs. leakage.** Reuse across distinct source-local meanings remains valuable, but it starts from exact F.17 cells and an obtaining F.9 Bridge, then keeps the proposed use, direction, rule, tolerated loss, reliance or assurance, and actual selector use separate. Bridge, CL, loss, registry, bundle, or policy pins cannot silently re-ground semantics.

* **Exploration vs. exploitation.** Dispatch sometimes must probe alternatives under explicit policy envelopes and risk envelopes, but probing must not become an implicit fourth status.
* **Evolvability vs. churn.** Registries evolve (new families, deprecations, edition bumps); continuity must not be broken by “rename by meaning”.

### G.5:4 - Solution
#### G.5:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; Default Governing Definition Index citation)

**GCoreLinkageManifest (normative; size-controlled via profiles and sets).**
For the operation in use, expand the applicable profile and set ids by union with its explicit deltas (per `G.Core:4.2.1`). The activation conditions below select those ids before expansion; `Nil‑elision` does not waive an activated obligation. `Select` retains its exact task, row editions and DRR/SCR-addressable audit result. `DeclareSetResult` instead consumes its exact result family, identified members, inclusion basis, ordering and named use where required; it acquires no TaskSignature, Method or registry row merely by declaring that set.

Select profile activation before expanding the G.Core sets. RegisterFamily always retains S1's immutable row edition, exact admitted members, grouping criterion and applicable eligibility/comparison basis. A project-local row without a CG-Frame activates neither AuthoringBase nor AuthoringMinimal; it still satisfies those S1 obligations. Intentional public registration adds EligibilityStandardRef, AssuranceProfileRef and UTS obligations even when no CG gate is in use. When a real CG-Frame registry or Select use is current, both authoring sets apply in full; omitting their required CN/CG pins is a failure, not nil-elision.

For crossing-aware selection, `CorePinsRequired` below lists the crossing pins individually. Each conditional pin is mandatory when its stated condition holds. When consuming `G.7` calibration records or a named `B.3` assurance account, retain all pins, editions, and evidence required by that account, including `CC‑G7‑SCRLinkage‑1` for cited calibration evidence.

* `CoreConformanceProfileIds :=`

  * `GCoreConformanceProfileId.PartG.AuthoringBase` *(when the current operation authors a registry in an actually selected CG-Frame or performs G.5-3 Select within that frame)*
  * `GCoreConformanceProfileId.PartG.TriStateGuard` *(when evaluating eligibility or acceptance predicates)*
  * `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted` *(when public identities are minted or evolved, including intentional public registration under S1/S1′ and CC-G5.6; a reusable project-local row alone does not activate this profile)*
  * `GCoreConformanceProfileId.PartG.ShippingBoundary` *(when an output is shipped)*
* `CorePinSetIds :=`

  * `GCorePinSetId.PartG.AuthoringMinimal` *(for the same actual CG-Frame registry-authoring or G.5-3 Select use; local registration or a set declaration alone does not activate it)*
* `CorePinsRequired :=` *(delta over PinSets; pins and refs are id-only; prefer strengthening optional-to-required over restating pins already covered by PinSets)*

  * `TaskSignatureRef` *(the C.22 TaskSignature edition for `Select`; see `G.5:4.2`, S2)*
  * `TaskMapRef?` *(exact G.4 map edition, only when this selection uses G.4 CAL gates)*
  * `MethodFamilyRowRef[]` *(exact `<MethodFamilyId, rowEdition>` values when method-family rows are consumed or registered)*
  * `MethodRef[]` *(exact A.3.1 Methods resolved from every method-bearing registry row consumed or registered)*
  * `SelectedStructureRef[]?` *(exact independently selected A.22 Structures consumed only when their organization changes this selector use)*

  * `GeneratorFamilyRowRef[]?` *(exact `<GeneratorFamilyId, rowEdition>` values when generator families are in scope)*
  * `PathId[]?`, `PathSliceId[]?` *(when audit or evidence citations use a G.6 graph, or an independently applicable gate or shipping contract requires those citations)*
  * `UTSRowId[]?` *(when the operation mints, evolves or consumes a public identity; intentional public registration activates S1/S1′ and CC-G5.6 obligations)*
  * `FailureBehaviorPolicyId?` *(only when degrade or abstain behavior is explicitly policy‑bound)*
  * `SoSLogBranchId?` *(only when degrade or abstain behavior is explicitly policy‑bound)*
  * `BridgeId/BridgeCardId?` *(the obtaining Bridge actually used by this selection; a Bridge Card is cited only when that Card is relied on)*
  * `BridgeMatrixId?` *(when this selection uses a BridgeMatrix)*
  * `CL/CL^k/CL^plane?` *(the applicable values when cited or required by the consumed calibration or named assurance account)*
  * `Φ/Ψ/Φ_plane policy-ids?` *(the applicable policy ids and editions when required by the consumed calibration or named assurance account, or when crossing or plane penalties are applied)*
  * `CrossingBundleId?` *(when the selector cites a CrossingBundle or its named downstream use requires one under `E.18` or `CC‑G5.27`)*
* `DefaultsConsumed :=`

  * `DefaultId.GammaFoldForR_eff`
  * `DefaultId.PortfolioMode`
  * `DefaultId.DominanceRegime`
* `RSCRTriggerSetIds :=`

  * `GCoreTriggerSetId.RefreshOrchestration`
    *(payload: exact changed source and affected-use scope; `SCRId`, `DRRId`; `TaskSignatureRef`, `MethodFamilyRowRef[]`, `CGSpecRef.edition` and `CNSpecRef.edition` for a `Select` result; and the actually applicable `TaskMapRef?`, `GeneratorFamilyRowRef[]?`, `AcceptanceClauseId[]?`, `SoSLogBranchId?`, `FailureBehaviorPolicyId?`, `DescriptorMapRef.edition?`, `DistanceDefRef.edition?`, `TransferRulesRef.edition?`, `InsertionPolicyRef?`, `PathId[]?`, `PathSliceId[]?`, `RSCRTestId[]?`. Nongraph scope uses the existing G.Core `PatternScopeId` branch.)*

#### G.5:4.2 - Dispatcher and Registry object set (notation‑independent)

G.5 defines the **object-set components** below. Their purpose is to make dispatch **possible and auditable** without embedding any method-family semantics in the selector kernel.

**S1 — `MethodFamily Registry` (design-time; project-local or within a selected CG-Frame).**
A reusable row represents one declared grouping. Choose its registry-identity contract: project-local reuse, or intentional registration under a stable public registry identity. This distinction concerns the identity contract, not who can see the row. Both branches fix these replayable values:

* `Identity and continuity`: `MethodFamilyId` names the continuing row lineage; `rowEdition` names one immutable edition; `MethodFamilyRowRef := <MethodFamilyId, rowEdition>` designates that edition. Lineage and Tradition notes and `UTSRowId` remain descriptive or publication values.
* `Exact method members`: non-empty `MethodRef[]`, each resolving to one `U.Method` already admitted under A.3.1.
* `Grouping basis`: exact claim, criterion, or direct relation reference that justifies this row's grouping for the current selector use; if no ontic family or membership relation is directly governed, the basis is explicitly project-local and creates none.

One exact row edition fixes its method members, grouping basis, and every selection-changing pin. Changing any of those values creates a new `rowEdition`; retain the `MethodFamilyId` only while the declared grouping remains the same continuing row lineage. Old `MethodFamilyRowRef` values continue to resolve their old editions. Add task, eligibility, policy, scheme, source, `ClaimScope`, validity, or intended-use pins only when they change selection or a named receiver needs them; none replaces the members or grouping basis.

* `Eligibility and comparison basis`: the actual rule and applicable editions used for this selection, including whether any comparison justifies ordering. A local row may cite its existing project rule; it need not manufacture a public eligibility artifact.
* `Assurance expectations`, only when the local use requires them, with the applicable evidence, unknown and failure rules. A real assurance or minimal-evidence gate keeps every input required by its governing clause.

**Public-registry continuation.** Intentional registration under a stable public identity additionally requires `EligibilityStandardRef` as a typed predicate record (tri-state per G.Core, using CHR/CAL terms and applicable edition pins), `AssuranceProfileRef` for declared evidence-lane expectations and assurance-lane pins, and the UTS naming/continuity obligations of CC-G5.6. The AssuranceProfile states expectations; it is not a B.3 assurance result. The public contract retains the same immutable members and grouping basis. The remaining fields below apply when their subject conditions hold in either branch.
* `AdmissibilityBindings`: when the row is authored for an actual CG-Frame or consumed by its gate, cite its single governance card and gate (`CNSpecRef`, `CGSpecRef`) and every required admissibility constraint, such as scale/unit conditions for a measurement use. An ordinary local grouping with no such use adds no CN/CG reference.
* `EvidencePins`: the source and evidence citations supporting asserted claims or guarantees. Cite `G.6` `PathId` or `PathSliceId` values when that support is represented in a graph or an independently applicable receiving contract requires those citations.
* `CrossingAllowance`: references to the exact F.17 endpoint senses, one obtaining F.9 Bridge, the separate C.2.1 bounded-use proposition, and the current A.10 or B.3 reliance basis, plus CL or observed-loss evidence when material, **only** when expressions with distinct recovered source-local meanings are actually related for this selector use. These are audit references; the field makes none of the referenced facts obtain.

For an actual crossing, first resolve both exact F.17 `SchemeSenseCell` endpoints and establish the two-participant F.9 Bridge under its own predicate profile. Then identify a separate C.2.1 episteme whose exact `EntityOfConcern` is that Bridge and whose ClaimGraph states the proposed use `u`, direction `d`, use-specific rule `r`, tolerated loss `t`, and polarity. For ordinary reliance require the matching current A.10 evidence-provenance path and local `RelianceDisposition`; when an actual named assurance claim is current, use B.3's separate assurance branch. A consequential use without one retains its direct governing rule. Observed loss and CL are evidence, defeater or assurance-policy material, not Bridge participants or permission. Authorization and the actual `Select` application remain with their subject patterns. A Bridge id, `CrossingAllowance`, registry row, policy pin, `CrossingBundle`, DRR or SCR entry cannot substitute for any step.

* `PolicyHooksRef?`: optional pointers to policy records (not defined here; wired via Extensions).

Here “a registry row represents a family” means that the row is the auditable selector-facing record for one declared grouping. The family id preserves that row lineage; the row ref selects one immutable edition for replay. Neither value identifies the grouped Methods, makes a membership relation obtain, or turns a common label, shared description, lineage note, eligibility rule, maturity card, evidence record, or policy into a method-family fact. Changing a row edition changes the registry artifact; it changes a Method or a separate family relation only when that object's direct identity rule or the relation's predicate independently says so.


**S1′ — `GeneratorFamily Registry` (design‑time; optional; per CG‑Frame).**
A reusable row groups generators of tasks and environments, which may co-evolve solver families. It uses the same local/public identity-contract distinction as S1 while retaining its own generator member and signature rules:

* `Identity and continuity`: `GeneratorFamilyId` names the continuing row lineage; `rowEdition` names one immutable edition; `GeneratorFamilyRowRef := <GeneratorFamilyId, rowEdition>` designates that edition. `UTSRowId` is required by intentional public registration; project-local reuse does not require it.
* `Exact generator members`: non-empty references, each resolving to a generator already identified under its subject pattern.
* `Grouping basis`: the independently established classification, membership relation, or explicit project-local criterion that groups those generators for this selector.
* `GeneratorSignatureRef`: conceptual input and output semantics plus budget semantics.
* `EnvironmentValidityRegionRef?`: pinned constraints for generated environments or tasks.
* `TransferRulesRef.edition?`: required when the Open-Ended mode is enabled (semantics come from the cited extension refs).
* `CouplerRefs?`: exact `MethodFamilyRowRef[]` values that may be coupled with this generator-row edition.

Both branches also fix the applicable eligibility/comparison basis and every selection-changing source or policy pin; assurance expectations are conditional on the use. Changing generator members, grouping basis, or another selection-changing pin creates a new generator `rowEdition`; old `GeneratorFamilyRowRef` values continue to resolve their old editions. Intentional public registration activates CC-G5.6 naming, continuity and UTS obligations, with the applicable generator signature and use contracts. It does not import A.3.1 Method membership into generator rows.

**S2 — C.22 `TaskSignature` input and conditional G.4 map.**
C.22 constitutes the `TaskSignature` episteme and defines its edition rule. G.5 consumes its `TaskSignatureRef` and does not reconstruct it from a task, CAL pack, or map. Its function here is pinning and auditability, not over-specification.

When this selector actually uses G.4 CAL gates, it also consumes one exact `TaskMapRef`. Resolve that immutable map edition, require its `taskSignatureRef` to equal the C.22 `TaskSignatureRef` supplied to this selector, and follow its exact `CALCharterRef` and edition-bearing clause, operator, flow, and evidence-profile refs. The map supplies no TaskSignature field and no threshold value. If no G.4 gate is current, omit `TaskMapRef`; an ordinary selector does not need a CAL pack merely to return a truthful bounded result.

For the G.4 safety example, G.5 receives `TaskSignatureRef=SafetyPortfolioTaskSignature-E4` and `TaskMapRef=<SafetySelectionMap, E3>`. The map resolves `CALCharterRef=<SafetyCALCharter, E2>` and the cited gate declarations. A different signature ref or an unresolved charter or component blocks only that gated selector use.

**S3 — `Selection kernel boundary` (run‑time; policy‑governed).**
A notation‑independent selector that:

* consumes `TaskSignatureRef`, exact method- or generator-family row refs, pinned spec refs, and an exact matching `TaskMapRef` only when G.4 CAL gates are current,
* applies the declared eligibility conditions and any assurance gates actually required for this use (tri-state),
* computes an admissible (possibly partial) order,
* returns one declared selector outcome over the exact Method candidates admitted through this kernel: most often `Shortlist` or `RankedShortlist`, and `JointUseSet` only when every returned Method candidate is included for one named use; otherwise it returns one `SpecialistHandoff`, one other narrowed handoff, one abstain outcome, or one escalation outcome (per `DefaultId.PortfolioMode` and explicit overrides),
* emits audit records with pins addressable by DRR and SCR records.

When `TaskMapRef` is present, resolve its exact immutable G.4 map edition before applying any cited gate. Its `taskSignatureRef` must match this selector's C.22 `TaskSignatureRef`; its `CALCharterRef` must recover the CG frame, EntityOfConcern, ReferencePlane, specification editions, and assumption envelope; and each cited clause, operator, flow, and evidence profile must resolve at its exact edition. Carry the exact map ref among the result basis and refresh pins. Do not copy thresholds or acceptance semantics into G.5.

If a cited gate consumes R, resolve the quantity and support model under `CC‑G5.4` before evaluating its threshold. Keep formal and empirical inputs, required premises, complementary support, dependence, scope, and counterevidence distinguishable. No common model means no invented aggregate: retain a qualified synthesis, and apply the clause's unknown behavior only where that missing quantity is actually required. The ordinary selector result in §0.4 is not an assurance claim and needs no new R calculation.

For every `MethodFamilyRowRef` consumed here, resolve the exact immutable row edition and then its A.3.1 `MethodRef[]`, grouping basis, and selection-changing pins before admitting the candidate. Apply the same rule to `GeneratorFamilyRowRef`. The selector may compare or return exact row refs as auditable selector-facing addresses, but row selection neither creates its members nor proves that every listed member belongs, is admissible, is selected, or will be enacted. An unresolved Method reference or missing grouping basis blocks that row's method-bearing use; it is not repaired by a label, description, UTS identity, policy, or evidence pin.

When a selector consumes an organization among Methods, cite an exact `SelectedStructureRef` only after A.22 has independently identified the `U.Structure` from exact constituents, exact already-obtaining relation occurrences, applied constraints, and one named use frame. G.5 neither supplies those discriminators nor selects the Structure by listing it. If the organization instead constitutes one composite Method, consume the exact A.3.1 Method only after B.1.5 has qualified that candidate from its independent parts and whole-forming basis.

S3 states reusable selector behavior. It does not itself perform selection. For an actual selector use, first recover every precise performer's A.13 core for the exact selection action, scope, working situation, and window, including the same obtaining assignment later used by any exact attribution. A.15.1 then independently admits the dated selector Work from its exact performance history, enacted Method, temporal extent, and containing-System relation. State the actual A.6.1 `Select` application, its effective argument bindings, and the A.19 `SelectionSlot` binding for any selected set returned by value. Add F.6 afterward only when the receiving claim needs exact assignment-bound attribution through the same obtaining A.13 assignment. The declaration, planned pins, registry rows, policy, assignment, F.6 relation, and `CandidateSet` type create none of the A.13, Work-admission, application, or result facts.

A compact selector account may omit only an assignment identifier unused by its receiving claim; it omits no criterion, classification, assignment, Work-admission, or attribution fact that the claim consumes. A root-family reference, the same holder, overlapping times, or silence in the receiving text establishes or removes neither the assignment nor F.6 attribution. Ordinary selector discussion not admitted as `U.Work` does not enter this branch.

In this actual-selector branch, the independently admitted dated selector Work and its actual Select application are required. Replay the upstream CPM applications through their own declaration-local bindings; separately admitted comparison Work is required only if the account asserts it. Evidence use, A.10 reliance/provenance, G.11 currentness and a C.2.1 result episteme retain their complete independent grounds when asserted or consumed by the receiving use. A bounded selection that consumes none of these additional claims requires no such additional object.

**S3.A — `TaskFamilySpecializationProfile@Context` (run‑time; conditional).**
When the real selector question is acquisition of usable specialization on a declared task family, the selector may emit one `TaskFamilySpecializationProfile@Context` for each candidate, one `SpecialistHandoff`, or one narrowed handoff plan. Here `profile` means one selector-time comparison record for bounded specialization, not a new U-kind and not a generic narrative profile. `G.5` carries this selector-time specialization question here; it does not redefine the adaptation-signature field vocabulary from `C.22.1`.

The profile should therefore cite one `AdaptationSignatureRef` or equivalent pinned field set carrying the declared `TaskFamilyRef` or `TaskSignature`, the work-measure threshold target, prior exposure declaration, time-to-threshold, budget-to-threshold, post-threshold efficiency when relevant, any declared transfer or retention claim, any downside cost or downside on adjacent tasks, and any specialization-entry baseline, specialization-entry evidence, or stepping-stone evidence item that materially affects comparison.

Admission rule for `SpecialistHandoff`: use that handoff kind only when the truthful declared result is one heterogeneous handoff bundle whose members occupy different specialization positions that still need to travel together. Do not use it when a `SetResultOutcome` with `Shortlist`, `RankedShortlist`, or `JointUseSet`, or a `HandoffOutcome` with another admitted handoff kind, already states the result more precisely.

When the declared task family is heterogeneous, the selector may return one `SpecialistHandoff`, one other narrowed handoff plan, or one `SetResultOutcome` with an admitted `SetResultFamily` that preserves rival specialists rather than collapsing them into a fake single winner. Low-human-overlap candidates remain admissible only when the profile, evidence basis, and policy constraints are explicit.

**S4 — `Composition and fallbacks` templates (design‑time).**
A library of composition shapes—`preconditioner -> solver -> verifier`, cascades, and meta-selectors—remains available **as design-time templates**, admissibility-checked and pinned. A template is a description or policy-bound arrangement for possible composition; its existence, diagram order, registry placement, or selection does not create a Method, `methodPartOf` occurrence, obtaining relation, or selected Structure.

If exact A.3.1 Methods, exact B.1.5 `methodPartOf` occurrences, all other required whole-forming claims and constraints, whole semantics, interface boundary, and reidentification rule qualify one already identified candidate as a composite `U.Method`, consume that exact Method through the B.1.5 branch. If independently identified Methods and already-obtaining relations are instead organized for one use without constituting one Method, consume an independently selected A.22 `U.Structure` only after its exact constituents, selected obtaining relation occurrences, applied constraints, and named selection-use frame are present. `MethodRelationStructure` may remain a local readable designator for that actually selected Structure; it is not a U-kind, relation kind, Method holon, registry-row identity, or generic `@BoundedContext` object.

A C.2.1 episteme may describe either governed object. A.3.2 applies only when the episteme's exact `EntityOfConcern` is one already admitted Method and its claims substantively describe that Method; an episteme whose exact concern is the selected Structure is not thereby a `U.MethodDescription`. Concrete strategy semantics stay in the referenced method families; G.5 only carries the composition template, selector relation, registry row, exact consumed Method or Structure reference, or selected-set result. None of those G.5 artifacts supplies the B.1.5 or A.22 construction facts.

Algebraic, graph, matrix, embedding, or neural selector notation remains a mathematical or representation lens when that representation is current; use C.29 for its correspondence and preserved-or-lost structure rather than reading notation as composition or selection.


**S5 — `Result, public identity, and telemetry` record boundary (run-time).**
Declare the following S5 outputs:

* `DRR` (decision rationale) and `SCR` (evidence and confidence citation) with explicit pins,
* declared selector and selected-set records produced either by method-family `G.5-3 Select` or by the already-grounded-member `G.5-6 DeclareSetResult` branch,
* telemetry pins to refresh orchestration (`G.11`), without governing orchestration.

S5 governs the selector-facing record boundary, not truth or actuality by record existence. A DRR, SCR, selected-set record, shortlist id, telemetry event, refresh cue, policy pin, or result label does not create dated Work, an actual operation application, the selected-set binding, a domain result, an evidence-provenance relation, assurance, authorization, or publication availability. Persist a selector-result claim as its own C.2.1 episteme when another use must rely on it; connect evidence through A.10, assurance through B.3, authorization through its direct governor, and actual availability through E.24.PUB only when each claim has its independently established basis.


Use §4.4b for outcome kinds and §4.4c for conditional public-identity fields.

**S6 — `Governance and evolution` declaration boundary (design-time).**
Versioning, deprecation, and registry evolution discipline (UTS publication; continuity), without minting new Part‑G‑wide types.

#### G.5:4.3 - Selector head and narrower selector families

Selection and dispatch stay one generic selector head. Narrower selector families may refine it, but they do not redefine the universal invariants pinned through `G.Core`, do not add new mandatory inputs to inherited `Select`, and do not mutate inherited SlotKinds. Required policy and edition refs use the declared input meanings.

Method- and generator-specific pressures such as `QD` archives, open-ended declared sets, explore and exploit lenses, or preference comparators do not become part of the selector head. They arrive only through explicit extension declarations and the pins those extensions require.

#### G.5:4.4 - Selector Relation Fields

| Selector relation                 | Consumes                                                                                                                                                     | Produces                                                                                                                                                                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **G.5-1 RegisterFamily** | declared local or public registry-identity contract; continuing MethodFamilyId and new immutable row edition; nonempty exact admitted A.3.1 MethodRef[]; obtaining grouping relation or explicit grouping criterion; eligibility/comparison basis; selection-changing source, policy and CHR/CAL/CN/CG pins as applicable; public-continuation fields when selected | One immutable MethodFamilyRowRef = <MethodFamilyId, rowEdition>, resolving the members, grouping, eligibility/comparison basis and applicable pins. Public registration additionally fixes EligibilityStandardRef, AssuranceProfileRef and UTSRowId under S1/CC-G5.6. A local row retains conditional assurance expectations without requiring a public UTS entry. Neither branch creates Methods or grouping facts. |
| **G.5-2 RegisterGeneratorFamily** | declared local or public registry-identity contract; continuing GeneratorFamilyId and immutable row edition; nonempty exact generator refs under their subject patterns; grouping basis; GeneratorSignatureRef; applicable eligibility/comparison, source and policy pins, including TransferRulesRef.edition when required | One immutable GeneratorFamilyRowRef = <GeneratorFamilyId, rowEdition>, resolving those members, basis, signature and applicable pins. Intentional public registration additionally meets S1′/CC-G5.6 naming, continuity and UTS requirements. Local reuse retains the same replayable member/basis core; neither branch creates generator identity or membership. |
| **G.5-3 Select**                  | `TaskSignatureRef`; exact matching `TaskMapRef` when G.4 CAL gates are current; exact `MethodFamilyRowRef[]` in scope whose immutable editions resolve to non-empty exact A.3.1 `MethodRef[]` and exact grouping bases; optional exact `GeneratorFamilyRowRef[]`; pinned `CNSpecRef` and `CGSpecRef` editions; policy refs if any; sufficient audit basis refs, with `PathId` or `PathSliceId` only for actual graph citations or an independently applicable gate or shipping contract | `CandidateSet` (set-returning), declared selector result with `PortfolioMode` recorded, exact row refs and any current `TaskMapRef` among the result basis pins, and `DRR` and `SCR` pins; if no admissible candidate exists: return `CandidateSet = EMPTY` plus an escalation hint (`ActionHint`) and the pins required to plan next steps (P2W split applies) |
| **G.5-4 Compose**                 | `CandidateSet`, composition template refs, pinned admissibility constraints                                                                                       | Composite strategy template (template-level; admissibility-checked; pinned)                                                                                                                                                                                      |
| **G.5-5 Telemetry**               | run outcomes, citations, and policy or edition pins                                                                                                               | refresh cues (typed RSCR causes and payload pins), parity deltas (if parity harness is in use), telemetry pins (selector-side; orchestration governing definition is `G.11`)                                                                                              |
| **G.5-6 DeclareSetResult**        | one exact `SetResultFamily`; exact already identified `memberRef[]`; `namedUse` for `JointUseSet`; ordering; inclusion or selection conditions; and sufficient `basisPins` to the already current choice, pool treatment, accepted decision, or other governed inclusion basis | one `SelectorOutcome` with `SelectorOutcomeKind = SetResultOutcome` and the exact membership form required by that family. For `JointUseSet`, it emits keyed unique `memberEntries`, `ordering = unordered`, the named use, inclusion conditions, and basis pins without a method-family row or `Select` pass. |

`RegisterFamily` produces only the local or public registry row selected under S1. It does not produce any A.3.1 Method or independently governed membership fact. `Select` may address candidates through those rows only after their exact Methods and grouping bases resolve; its returned candidate or selected-set value does not retroactively ground a row member.

`Compose` produces only the pinned template named in its output column. It neither qualifies one composite Method under B.1.5 nor selects one A.22 Structure. When a later selector use consumes either governed object, the exact Method or Structure reference is an independently grounded input rather than a result inferred from this template.

`DeclareSetResult` begins only after its exact members and inclusion or selection basis are current. An upstream C.11 `ChoiceResult`, C.19 pool treatment, accepted decision, or another governed basis may appear among `basisPins`; the G.5 branch does not repeat or perform that decision. It declares the selector-facing set-result content and stops. It creates no member identity or relation, method-family row, `Select` application, dated selection Work, persisted C.2.1 result episteme, assurance or authority claim, or E.24.PUB availability occurrence.

#### G.5:4.4a - Worked selector slice

- A catalyst-search team is choosing among three method families for the same declared `TaskSignature` and `C.22.1` adaptation signature.
- The shared profile pins one work-measure threshold target, one freshness window, one prior-exposure declaration, and one adaptation budget. One family reaches threshold quickly but carries high downside on adjacent tasks. One family is slower but transfers cleanly. One family never clears `MinimalEvidence` and must receive an abstain verdict.
- The `G.5` result in this slice therefore declares one unordered `Shortlist` retaining the first two families, with DRR and SCR records citing why the third family was excluded and why the first two remain non-dominated. The selector does not invent one scalar winner and does not hide the specialization profile in auxiliary side notes.
- If the project also claims that this selection actually occurred, A.13 first recovers `CatalystSelectorSystem-17 : U.System` for exact action `CatalystFamilySelectionAction-17`. `CatalystSelectorBoundary-17` contains the deployed selector runtime, its effective policy state, and its registry/evidence interfaces; it excludes the method-family rows, `TaskMap`, result records, assignment, and containing team System. The action applies the effective selector to the three candidate families and returns the retained set. Its scope is `CatalystFamilySelectionClaimScope-17`, its working situation is `CatalystSearchSelectionSituation-17`, and its window is `2026-07-30T10:00:00Z` through `2026-07-30T10:08:00Z`. `CatalystSelectionAdmissibilityNorm-17` directs the selector to exclude candidates that fail `MinimalEvidence`, preserve admissible non-dominated alternatives, and abstain rather than manufacture a scalar winner. Relevant conditions include the exact `CatalystTaskSignature-17`, current row and map editions, eligibility evidence, comparison policy, and adaptation-signature values.
- A.2 declares local agential kind `CatalystMethodSelectorSystemRole`. Its membership criterion requires the stable work-facing contribution of method-family selection and goal-directed, condition-sensitive regulation under `CatalystSelectionAdmissibilityNorm-17`: the holder must apply the current gates, preserve the admissible set-return semantics, and abstain or escalate when no candidate qualifies. `CatalystSelectorDecisionTrace-17` shows `CatalystSelectorSystem-17` excluding the third family for failed `MinimalEvidence`, retaining the first two as non-dominated, and emitting no scalar winner. The trace and boundary/runtime records support the criterion facts under A.2's membership rule; A.10 makes that source-to-use account recoverable. The case independently classifies `CatalystSelectorSystem-17` under `CatalystMethodSelectorSystemRole`; neither the assignment nor the candidate Work supplies the classification. No Grade, autonomy result, characteristic profile, or stronger assurance claim is consumed.
- The same A.13 core uses `CatalystSelectorAssignment`, a directly declared species under `U.SystemRoleAssignment`. The species declares holder, assigned-kind, and task-signature participant meanings and the assignment predicate. `CatalystSelectorAssignment-17` obtains with `CatalystSelectorSystem-17`, `CatalystMethodSelectorSystemRole`, and `CatalystTaskSignature-17` as its exact participant values; its maximal uninterrupted predicate-true interval covers the stated scope, situation, and window.
- Only after that core is established does A.15.1 independently admit `CatalystSelectionWork-17 : U.Work` from the exact selection-action history, enacted `CatalystFamilySelectionMethod`, temporal extent, and obtaining containing-System relation to independently admitted `CatalystSearchTeamSystem`. Actual application `CatalystSelectApplication-17` separately carries its effective candidate, criteria, and A.19 `SelectionSlot` bindings. Neither the assignment nor F.6 is an A.15.1 admission premise.
- Because this account explicitly attributes the Work under `CatalystSelectorAssignment-17`, F.6 afterward establishes `performedUnderAssignment(CatalystSelectionWork-17, CatalystSelectorAssignment-17)` through that same obtaining A.13 assignment. The direct case fact links the exact pair, holder equality holds, and the assignment interval covers the Work. A different overlapping assignment held by the same System would not establish this attribution. A short result may omit the assignment identifier only after every fact consumed by the attribution remains recoverable.
- A persisted shortlist assertion is a separate C.2.1 episteme; its DRR or SCR references do not by themselves prove the exclusion facts, warrant the result, authorize downstream action, or make that episteme available to an audience.

- When one upstream `C.19` pass has already narrowed the live pool to one internal retained subset over registered families, `G.5-6 DeclareSetResult` may declare that result as one `Shortlist` with one `ShortlistId` and explicit basis pins only when selector-facing result declaration is now the question. Until that declaration occurs, the internal retained subset is not yet one G.5 shortlist result.
- When one upstream `C.11` pass has already fixed one local choice over one declared source set, `C.19` has fixed one retained pool treatment, an accepted decision has fixed all-member inclusion, or `C.24` has produced one enactment-facing narrowed handoff, use `G.5-6 DeclareSetResult` when selector-facing set-result content is now the question. Until that declaration occurs, the `ChoiceResult`, `PoolPolicyResult`, accepted inclusion basis, `CallPlan`, or `CheckpointReturn` is not itself that G.5 result. Non-Method members do not pass through `RegisterFamily` or `G.5-3 Select`.

#### G.5:4.4b - Declared selected-set result and closure rule

When the current question is selector-facing result declaration, state one explicit selected-set result rather than leave it implicit in a selector trace, comparison note, or local choice.

For method dispatch, that result closes selector work over grounded rows. For a `JointUseSet`, it records already identified members that are all included for one named use. It does not replace registry maintenance, comparison rules, the upstream choice or inclusion basis, or the patterns that identify the members and their relations.

The admissible selector outcome families here are:

- `SelectorOutcomeKind = SetResultOutcome`, whose closed `SetResultFamily` value set is `Shortlist` when alternatives are retained for later choice and the result does not order them, `RankedShortlist` when the result orders those retained alternatives, and `JointUseSet` when every named member is included for one named use;
- `SelectorOutcomeKind = HandoffOutcome`, with `HandoffKind = SpecialistHandoff` or one other narrowed handoff plan when heterogeneity is the truthful downstream result;
- `SelectorOutcomeKind = AbstainOutcome` when no admissible candidate exists and the truthful result is one abstain; and
- `SelectorOutcomeKind = EscalationOutcome` when no admissible candidate exists and the truthful result is one escalation.

`G.5-3 Select` may emit one of these outcome kinds only over the exact Method candidates admitted through its kernel; `G.5-6 DeclareSetResult` emits `SetResultOutcome` from exact already identified members and a current inclusion basis. Neither branch performs an upstream choice, makes a member relation obtain, or proves actual selection Work.

A `JointUseSet` uses this bounded representation:

- `namedUse` states the one joint use;
- `memberEntries` contains one keyed entry per included member;
- every entry has one exact `memberRef`; the membership result adds no per-member contribution or basis field;
- each exact `memberRef` occurs at most once, and entry order has no semantic effect;
- if a serialization also emits top-level `members`, it is only the unique set projection of `memberRef` values from `memberEntries`, never a second maintained list;
- `ordering`, inclusion conditions, and sufficient top-level `basisPins` remain explicit; and
- candidate-pool membership and excluded candidates stay separate from emitted joint-use membership.

Exact content, claims about a member's use or contribution, and direct relations keep their own governed records. When one supports the membership result, cite that existing record among `basisPins`; `memberEntries` creates neither the cited content nor a new contribution relation.

For framework use, `memberRef` may name an exact already identified edition under its existing identity rules. Do not populate `MethodRef`, create a registry row, or classify that edition as a Method merely to emit the result.

Every outcome still states its `SelectorOutcomeKind`, public result kind when applicable, members, keyed entries, handoff content, or blocking condition, ordering, and sufficient basis pins. A handoff also states its next downstream use boundary.

A compact retained-alternative result may look like:

```text
SelectorOutcome(
  selectorOutcomeKind = SetResultOutcome,
  setResultFamily = Shortlist,
  members = [family_A, family_C],
  shortlistId = shortlist_17,
  ordering = unordered,
  basisPins = [pathSlice_41, scr_22],
  nextUse = downstream_comparison
)
```

A compact joint-use result may look like:

```text
SelectorOutcome(
  selectorOutcomeKind = SetResultOutcome,
  setResultFamily = JointUseSet,
  namedUse = cohort_review,
  memberEntries = [
    { memberRef = Core@C },
    { memberRef = Domain@D },
    { memberRef = Local@L }
  ],
  ordering = unordered,
  inclusionConditions = [all_three_editions_required_for_cohort_review],
  basisPins = [choice_result_12, edition_basis_7]
)
```
Close with `Shortlist` or `RankedShortlist` when the result retains alternatives. Close with `JointUseSet` only when every member is included for the named use and its keyed membership can be stated truthfully. Close with a handoff, abstain, or escalation outcome when that is the actual result. If the result omits its result family, members or member entries, ordering, named use where required, or basis pins, it is not a complete `G.5` result.

#### G.5:4.4bb - Public labels over archive, front, and style source sets

When a selector consumes a declared `ExplorationArchive`, `Archive`, `Front`, or `Q-front`, keep that object as a source-set family or source-set reference; it is not the emitted G.5 outcome. The emitted result states one admitted `SelectorOutcomeKind` and, for a set result, one admitted `SetResultFamily`. `StyleShortlist` and `TraditionShortlist` may be public domain labels over an admitted set-result family after their term bridges and cultural meaning are clear; they do not extend either closed set.

```text
SelectedSetResultLabelLine@Context:
  selectorOutcomeKind:
  setResultFamily?:
  sourceSetFamily:
  publicSelectedSetLabel?:
  namedUse?:
  memberEntries?:
  membersOrHandoff?:
  derivedViewKind?:
  basePaletteOrArchiveRef?:
  ordering:
  basisPins:
  nextUse:
```

Earlier records may keep `membersOrHandoff`. Read it as `members` for `Shortlist` or `RankedShortlist` and as `handoffContent` for a `HandoffOutcome`. It cannot replace keyed `memberEntries` in a `JointUseSet`; if it also lists joint-use members for compatibility, that list is only the unique set projection of the entry keys.

`sourceSetFamily` may name a declared `Front`, `Q-front`, `ExplorationArchive`, `Archive`, current pool subset, or derived tradition view. For retained alternatives, `publicSelectedSetLabel` normally names `Shortlist` or `RankedShortlist` and may use a domain label such as `StyleShortlist` or `TraditionShortlist` only when the term bridge is already clear. `JointUseSet` is not a shortlist label: it names an all-member result and therefore uses `namedUse` plus keyed `memberEntries`. G.5 does not create the archive, compute the comparison, govern the pool policy, decide the cultural-evolution case, establish member identity or relations, or repair the term bridge. Use `C.18` for archive formation, `A.19.CPM` for comparison, `C.19` for pool policy, `C.36` for cultural-evolution claims, each member's own identity and relation patterns for those facts, and `F.17`/`F.18`/`F.9` for local meanings, naming settlement, and any obtaining term Bridge.

#### G.5:4.4c - Result-declaration quick card

Use the outcome definitions in §4.4b and fill only the applicable fields:

| Field | When and what to state |
| --- | --- |
| `selectorOutcomeKind` | Every result: the admitted set, handoff, abstain or escalation kind. |
| `setResultFamily`, `members` | For retained alternatives: the admitted shortlist family and exact surviving refs; preserve a justified order for `RankedShortlist`. |
| `setResultFamily`, `namedUse`, `memberEntries`, `inclusionConditions` | For joint inclusion: `JointUseSet` and its §4.4b keyed membership declaration. |
| `handoffKind`, `handoffContent` | For a handoff: `SpecialistHandoff` or another admitted narrowed handoff and the content the next receiver needs. |
| `blockingPins` | For abstain or escalation: the actual blocking conditions. |
| `ordering` | Ranked, unordered or not applicable, as the outcome permits. |
| `basisPins`, `nextUse` | The supporting basis and next use boundary; `none` when there is no next use. |
| `publicId` | Only when stable public identity is needed; `ShortlistId` is specific to a shortlist. |

The pump result in §0.5 and the joint-use declaration in §4.4b show complete filled forms. A missing required value leaves the result incomplete.

#### G.5:4.4ca - Derived tradition-view result stays derived over one declared palette

When the source is `TraditionFront` or `TraditionArchive`, keep its base `SoTAPaletteDescription` recoverable. State `SourceSetFamily`; add `DerivedViewKind` when it changes interpretation or later publication and `SourceSetComposition` only when several source-set families were actually composed. Cite the derivation's declared Q, reachability or coverage rule among the DRR/SCR or equivalent basis pins. The view qualifies the source; §4.4b still defines the emitted outcome.

#### G.5:4.4d - Worked result-declaration closure slice

| Receiving situation | Complete result and changed action |
| --- | --- |
| The two pump Methods in §0.5 survive, with no admitted ordering. | Emit its unordered `Shortlist`; the receiver still has a choice to make. |
| A declared comparator orders family_B before family_A for the specialist handoff. | Emit a `RankedShortlist` with `[family_B, family_A]`, the comparator and supporting basis pins, and the handoff use. A request for an order alone supplies no comparator. |
| The cohort decision includes `Core@C`, `Domain@D` and `Local@L` together. | Emit the §4.4b `JointUseSet`; the receiver uses all three exact editions under the inclusion conditions. |
| No candidate clears the applicable admissibility/evidence gates. | Emit `AbstainOutcome` or `EscalationOutcome`, naming the blocking pins, basis and next use; an empty shortlist leaves the stop unexplained. |

The following extensions apply only when their corresponding mode is active. Their declared `Uses` and pins cite the governing semantics.

**GPatternExtension block: `G.5:Ext.EELog`**

* `PatternScopeId`: `G.5:Ext.EELog`
* `GPatternExtensionId`: `EELog`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.19`
* `Uses`: `{C.19}`
* `⊑` and `⊑⁺`: `∅`
* Required pins, edition pins, and policy pins (minimum):

  * `EELensPolicyRef` *(or equivalent lens or policy id carried by `C.19`)*
  * `RiskBudgetRef?`
  * `ProbeAccountingRef?`
  * `FailureBehaviorPolicyId?` *(if degrade behavior is governed by policy)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (extension discipline; semantics cited):`

  * This block activates exploration and exploitation-governed dispatch.
  * Post‑2015 examples that typically land here: modern bandit‑style or Bayesian selection under explicit risk budgets; adaptive evaluation and probing regimes; safe‑exploration variants where “abstain” or “degrade” is policy-bound.

**GPatternExtension block: `G.5:Ext.SoSLOG`**

* `PatternScopeId`: `G.5:Ext.SoSLOG`
* `GPatternExtensionId`: `SoSLOG`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.23`
* `Uses`: `{C.23}`
* `⊑` and `⊑⁺`: `∅`
* Required pins, edition pins, and policy pins (minimum):

  * `SoSLogRuleId[]`
  * `SoSLogBranchId[]` *(including escalation branches, if used)*
  * `FailureBehaviorPolicyId` *(if degrade behavior is made explicit)*
  * `MaturityRungId[]?` *(when maturity ladders are used as gates; semantics come from `C.23`)*
  * `AdmissibilityLedgerRef?` *(when selector consumes admissibility rows rather than recomputing thresholds)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
* `Notes (extension discipline; semantics cited):`

  * This block pins dispatch decisions to explicit rule and branch ids, enabling auditable “why” without inventing a fourth acceptance status.

**GPatternExtension block: `G.5:Ext.NQD`**

* `PatternScopeId`: `G.5:Ext.NQD`
* `GPatternExtensionId`: `NQD`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.18`
* `Uses`: `{C.18, C.19}`
* `⊑` and `⊑⁺`: `∅`
* Required pins, edition pins, and policy pins (minimum):

  * `DescriptorMapRef.edition`
  * `DistanceDefRef.edition`
  * `InsertionPolicyRef`
  * `TaskSignatureRef` *(when QD is enabled via TaskSignature flags or traits)*
  * active fields from C.21's DHC replay basis *(only when this telemetry consumes a C.21 DHC coordinate; carry exactly the fields that coordinate used)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (extension discipline; semantics cited):`

  * G.5 core remains QD‑agnostic; QD semantics are governed by `C.18`.
  * Post-2015 families that typically use this extension declaration: MAP-Elites-class QD including later archive-centric refinements, CMA-ME-class hybrids, modern illumination and coverage telemetry regimes where admissibility and edition pinning matter.

**GPatternExtension block: `G.5:Ext.OpenEndedFamilyWiring`**

* `PatternScopeId`: `G.5:Ext.OpenEndedFamilyWiring`
* `GPatternExtensionId`: `OpenEndedFamilyWiring`
* `GPatternExtensionKind`: `GeneratorSpecific`
* `GoverningPatternId`: `G.2`
* `Uses`: `{G.2, C.19, C.23}`
* `⊑` and `⊑⁺`: `∅`
* Required pins, edition pins, and policy pins (minimum):

  * `GeneratorFamilyRowRef[]`
  * `TransferRulesRef.edition` *(mandatory when Open‑Ended is enabled)*
  * `EnvironmentValidityRegionRef?`
  * `CoEvoCouplerRef[]?`
  * `SoSLogBranchId[]?` *(when validity of generated tasks is gated by explicit branches)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (extension discipline; semantics cited):`

  * This block enables declared sets of `{Environment, MethodFamily}` pairs without redefining generator semantics in G.5.
  * Post‑2015 examples typically referenced via `G.2` family cards: POET‑class and later open‑ended and co‑evolutionary regimes, including enhanced variants where transfer policies and validity gates must be edition‑pinned.


#### G.5:4.4e - Source sets, operating modes and comparison policy

Use §4.4b for the emitted outcome and §4.4bb–ca for its source and public-label interpretation. An actual `SelectionSlot` binding carries the by-value selected candidate set; it is separate from G.5's declared `SelectorOutcome`. `ChoiceSet` remains an ordinary mathematical set gloss, not an additional public result kind.

| Declaration | Meaning and applicable condition |
| --- | --- |
| `Front` | The non-dominated source set under the declared `DominanceSet`. |
| `Archive` | The exploration set retained under its policy. |
| `PortfolioMode` | How the selector operated. The default `Archive` retains exploration evidence; it establishes neither an emitted Archive nor a different result family or DominanceSet. |
| `SourceSetFamily`, `SourceSetComposition` | State the immediate source family; use composition only when several source families were actually consumed, for example a front and an archive. |
| `DerivedViewKind`, `BasePaletteRef` | Qualify an actual derived view under §4.4ca; the latter is a reference, not a kind. |
| `PromotionPolicy` | Required when tie-break or telemetry signals are promoted into dominance. |
| `SubjectKind`, `RetentionIntent=steppingStone` | Qualify the relevant declaration or retention policy; neither names another emitted set result. |

Use controlled tokens, cited ids or already declared head labels for these fields. CostToProbe, ValueOfInformation, ValueOfComputation, explore_share, graduation conditions and sequencing pressure belong to the surrounding choice doctrine when they affect the decision; a result field does not establish them. All-member membership and candidate/exclusion records retain the separation in §4.4b.

#### G.5:4.6a - Causal method dispatch declarations

When method dispatch compares causal uses, each compared Method declares its causal question/rung and whether it is being used as an observational predictor, intervention optimizer, counterfactual strategy, causal fairness estimator, causal-RL policy, or simulation-only Method.

```text
MethodFamily.causalUseDispatchSpec?:
  causalUseQuestionRef?: CausalUseQuestionRef
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind: CausalUseClaimKind
  causalActionPolicyClass?: CausalActionPolicyClass
  causalSupportComponentRefs?: CausalSupportComponentRefs
  causalUseSupportResultRef?: CausalUseSupportResultRef
  causalMethodUseClassification:
    observationalPredictor |
    interventionOptimizer |
    counterfactualStrategy |
    causalFairnessEstimator |
    causalRLPolicy |
    simulationOnlyMethod
  supportedUse
  unsupportedUse
```

`CausalUseQuestionRef` identifies the question content used by C.28; it is not a durable root U-kind. `causalMethodUseClassification` describes the Method's proposed selector-facing use and supplies no system-role assignment, responsibility, authority, or causal certification.

A simulation-only Method cites `simulationResultRef` inside its support components and states bounded model use plus unsupported realized/interventional use. G.5 declares the dispatch result; C.28 supplies the causal-support result. A selector may still abstain even when a C.28 result is supported.

### G.5:5 - Archetypal Grounding

**Tell (archetype).**
The selector-bearing **System** must choose among rival families without lying about measurement admissibility, crossings, or evidence. The result **Episteme** keeps the comparison basis, audit pins, and refresh conditions recoverable. When the current result instead includes several already identified members together, the same result-content boundary must not disguise that all-member meaning as retained alternatives.

**Show 1 (multi-Tradition dispatch; unordered shortlist).**
A `CG-Frame` includes multiple decision-theoretic families with different admissibility assumptions. Evidence for some CHR traits is incomplete.
System registers families (S1), then runs `Select` (S3) on a pinned `TaskSignatureRef`. Eligibility is tri-state; some families **receive abstain** due to missing minimal-evidence pins. Among remaining candidates, only a partial order is admissible, so the selector emits one `Shortlist` with explicit `basisPins` instead of inventing one scalar winner. No shadow acceptance logic appears in the selector; it consumes pinned acceptance and admissibility records.

**Show 2 (specialist handoff; ranked result).**
A bounded-specialization comparison keeps two method families live under a pinned admissible comparator that orders them, and downstream handoff needs that ordering.
Declare one `RankedShortlist` with that ordering and comparator among its basis pins, `ShortlistId` when public identity is needed, and handoff-facing `nextUse`. If no admissible comparator supplies an order, retain an unordered `Shortlist`; the request for a ranked handoff does not establish one.

**Show 3 (no admissible survivor; abstain or escalation).**
In this frame, one admissibility gate and one minimal-evidence gate fail at the same time.
The truthful `G.5` result is one abstain or escalation result that names the blocking pins and the next downstream use boundary, not one empty shortlist that leaves downstream users unsure whether selection silently failed or admissibly stopped.

**Show 4 (complementary framework editions; unordered joint use).**
A training cohort needs `Core@C`, `Domain@D`, and `Local@L` together. The editions are already identified under their own edition rules; they are not Method candidates or registry rows. An accepted cohort decision supplies the exact members and basis. `G.5-6 DeclareSetResult` emits one unordered `JointUseSet` with one keyed entry per edition, the named cohort-review use, inclusion conditions, and sufficient top-level basis pins. Direct dependencies and pairwise compatibility claims remain with E.4.PFR; publication and access remain with E.17/E.24.PUB and the applicable access-carrier pattern. The G.5 result declares membership but does not perform the choice, make those neighboring claims obtain, or create a contribution relation.

**Show 5 (support-sensitive Method eligibility).**

Keep the exact admitted Methods, row editions, and grouping basis from §0.5. In a gated variant, the matching G.4 task map makes `AC_InputConditionGate-E1` from G.4 §5 applicable to `ThresholdTrendReviewMethod-E2`. Consume that clause's value and threshold rather than define either in G.5. For the two-condition case there, the returned `fail` excludes that row from the assurance-gated set. Replacing its joint probability with minimum would wrongly retain it. An otherwise admissible row stays in the set under its own declared eligibility basis; if none survives, return the existing abstain or escalation outcome.

If the dependence model is missing, use the clause's `unknown` branch rather than pass by a high F. In the ordinary, non-assurance question of §0.5, both grounded rows still form the unordered `Shortlist`. A formal proof, a limited complementary study, and an overlapping contrary result can remain separate support with their limitations; neither weak additional evidence nor the absence of an unjustified common score automatically removes a Method. A defeated necessary premise still changes the eligibility that actually relies on it.

**Show 6 (one calibrated correspondence, two receiving uses).**

Use G.7 §4.5's `VehicleTransportOrder` row from C.3.3 to select among independently admitted Methods for a transport review. The task's applicability comparison uses only the preserved transport/passenger order and explicitly ignores propulsion. When receiving admissibility, fresh target classification of the subject vehicles, the bounded comparison conditions and matching reliance pass, that row can support Method eligibility under the task's other rules. Keep those premises with the result.

For a second task that requires battery-health evidence, the same CL^k=2 row loses the necessary EV distinction and cannot support that criterion. Return the missing battery premise through the existing unknown/abstain or evidence-request branch. Raising a scalar summary or citing a waiver does not restore that distinction. G.7 reports the correspondence; the exact TaskSignature and receiving rules decide each selection use.

### G.5:6 - Bias-Annotation

Potential biases and failure modes this pattern explicitly guards against:

* **Monoculture bias (single Tradition dominance by default).** Mitigation: rows retain an explicit eligibility basis and conditional assurance expectations; public registration adds its stronger records; selection is set‑returning under partial orders; method‑specific policies stay explicit pins rather than hard-coded defaults.
* **Hidden scalarisation bias.** Mitigation: set-return semantics is pinned through `G.Core`; dominance regimes are explicit and each default cites one declared governing definition.
* **“Tool equals method” bias.** Mitigation: notation independence and prohibition of tool keywords in core registry and eligibility fields; tool choices are outside the core.
* **Cross-sense leakage bias.** Mitigation: when expressions have distinct source-local meanings, require exact F.17 endpoint senses, an obtaining F.9 Bridge, a separate C.2.1 bounded-use proposition, and the matching A.10 or B.3 reliance branch; keep loss and CL visible where material. Crossing pins and bundles remain audit or publication references and cannot make an implicit crossing admissible.

* **Survivorship bias in refresh.** Mitigation: RSCR triggers are typed and id-based; freshness, decay, and telemetry deltas are first‑class causes with canonical ids.

### G.5:7 - Conformance Checklist (normative)

| ConformanceId   | Statement |
| --------------- | ----------|
| `CC‑G5‑CoreRef` | **Core conformance bridge.** `G.5` is conformant only if the **effective** `G.Core` obligations referenced by `G.5:4.1 (GCoreLinkageManifest)` are satisfied (after profile and set expansion plus explicit deltas). |
| `CC‑G5.0`       | Core standards **SHALL** remain notation‑independent; vendor or tool keywords are forbidden in registry, eligibility, assurance, or selector‑kernel obligations (`E.5.*`). |
| `CC‑G5.1` | Every reusable MethodFamily row **SHALL** fix its exact members, grouping basis, eligibility/comparison basis and selection-changing pins in one immutable edition. Intentional public registration additionally declares EligibilityStandardRef using CHR/CAL terms and applicable edition pins. Both branches remain notation-independent. |
| `CC-G5.2`       | Selection **SHALL** be a pure function of `TaskSignatureRef`, exact method- and generator-family row refs, any conditionally current exact `TaskMapRef`, and pinned policy or edition refs; side effects are limited to emitting DRR and SCR pins, telemetry triggers, and RSCR triggers (no hidden mutation of constraint-bearing spec refs). |
| `CC‑G5.3`       | **Delegated (ID‑continuity) plus F.9 use boundary.** When a selector use relates expressions with distinct F.17 source-local meanings, it **MUST** resolve the exact cells, an obtaining F.9 Bridge, a separate C.2.1 `<u,d,r,t,polarity>` proposition, and the matching A.10 or B.3 reliance branch. G.Core crossing visibility and penalty-assignment semantics still apply. **Delegation targets:** `CC‑GCORE‑CROSS‑1`, `CC‑GCORE‑PEN‑1`. Pins alone **MUST NOT** establish the Bridge, use, reliance, or actual selector application. |
| `CC‑G5.4` | **Governing rule for** `DefaultId.GammaFoldForR_eff`. An R or R_eff composition **MUST** use a justified receiving quantity, input meanings and scales, dependency model and operation under B.3/C.2.2; cite contributors and pin the actual model/policy. Neither a universal minimum/maximum or best-source cap, an ungrounded F-to-R conversion, nor monotonicity and boundedness alone supplies that model. Without a justified common model, retain separate support and a bounded synthesis. If an actual G.4 gate requires the missing quantity, follow that clause's unknown behavior; a calculated threshold failure remains a failure. G.4 owns acceptance conditions and thresholds. Ordinary selection with no assurance condition remains usable without a new R calculation. |
| `CC-G5.5`       | Ordinal scales **MUST NOT** be averaged or subtracted; any aggregation or comparison must respect CHR scale typing and admissibility constraints, including CSLC where applicable. |
| `CC‑G5.6` | **Public registration.** Intentional registration of a MethodFamily or GeneratorFamily under a stable public registry identity **SHALL** publish that identity to UTS with the applicable naming and lexical-continuity discipline. Project-local reusable rows keep the immutable member/basis contract of S1/S1′ without this added duty. Visibility alone does not select the public identity contract; actual audience availability is a separate E.24.PUB occurrence. |
| `CC‑G5.7`       | **Conditional.** If `G.5:Ext.EELog` is present, exploration **MUST** be budgeted under the pinned exploration and exploitation log policy; probe outcomes **MUST** feed refresh through canonical RSCR trigger kinds. |
| `CC‑G5.8` | **Actual CG-Frame gate enforced.** When selection uses a CG-Frame gate, retain its pinned CG-Spec.MinimalEvidence requirements for the cited characteristics. Failed requirements reject or abstain under that gate's rule; missing required input remains unknown/abstain and cannot pass. Registering a local grouping without this selection/gate use does not activate that gate. |
| `CC-G5.9`       | **Delegated (ID-continuity).** Set-return semantics are pinned through `G.Core`. **Delegation target:** `CC-GCORE-SET-1`. Candidate ordering **MUST** be admissible over typed traits and admissibility constraints. If only a partial order is available, selection **MUST** return one declared selector outcome, for example one `SetResultOutcome` with `Shortlist` or `RankedShortlist`, one `HandoffOutcome` with `SpecialistHandoff`, or another pinned outcome result, with no forced totalisation via inadmissible scalarisation. |
| `CC-G5.10`      | **SCR completeness.** SCR **MUST** enumerate Gamma-fold contributors when used, referenced constraint-bearing spec editions, the source and evidence citations used in gating and rationale (`PathId` or `PathSliceId` when graph citations are used or independently required), and `MinimalEvidence` gating verdicts by lane and carrier when such gating is relied upon. |
| `CC‑G5.11`      | **Delegated (ID‑continuity).** Tri‑state eligibility and acceptance semantics plus unknown handling are pinned through `G.Core`. **Delegation target:** `CC‑GCORE‑GUARD‑1`. *(Includes the rule that `degrade(...)` is expressed through a pinned FailureBehavior or SoS‑LOG branch id, not as a fourth status.)* |
| `CC-G5.12`      | **Applicability of a selected method set.** A selected method-set result **MUST** state the exact task, exact row refs or other exact members, grouping and selection basis, truthful outcome kind, ordering, selection or inclusion conditions, and the named next use. Add `ClaimScope`, selected A.2.6 slices, a validity or evaluation window, source or scheme editions, intended-use restrictions, counterexamples, evidence pins, and transfer or change conditions only when they change eligibility, selection, applicability, or a receiver's justified reliance. Omitting any such action-changing value fails this check and reopens the affected result; values that change no current action stay out. Coverage, descriptors, and distance may guide a named search for omissions but **MUST NOT** establish broader applicability. Apply `E.24.UK` or `A.8` only to a separate claim about a durable kind or kernel placement; neither claim widens the selected set's applicability. |
| `CC‑G5.13`      | **Conditional.** If the selector consumes admissibility or maturity records (e.g., through `G.5:Ext.SoSLOG`), it **MUST NOT** recompute thresholds; it consumes pinned admissibility ledger rows and cites clause and rung ids in audit pins. |
| `CC‑G5.14`      | **Φ(CL) and Φ_plane discipline.** If crossing or plane penalties are applied, the active penalty policy ids (e.g., `Φ(CL)`, `Φ_plane`) **MUST** be explicit in audit pins, and the pinned policies **MUST** satisfy the monotone and bounded requirements asserted by their cited constraint-bearing spec refs and be published through those same cited spec refs (e.g., `CG‑Spec`). SCR **MUST** record the policy id in use; penalty assignment semantics remain pinned through `G.Core`. |
| `CC-G5.15`      | Unit and scale admissibility **MUST** be established via CSLC (A.18) before any aggregation or Gamma-fold; unit and scale mismatches are a fail-fast defect. |
| `CC‑G5.16`      | Hidden thresholds are forbidden. Thresholds live in explicitly pinned acceptance or eligibility policy records, not in selector prose, LOG shells, or code.  |
| `CC‑G5.17`      | ReferencePlane **MUST** be declared (pinned) for any claim that is used in dispatch, and the selector’s audit records must cite it (including plane‑crossing pins when applicable). |
| `CC-G5.18`      | Numeric comparisons and aggregations used by dispatch **MUST** cite an admissible, edition-pinned comparator or spec publication (as provided by the constraint-bearing spec refs); inadmissible mixes of scale types are forbidden. |
| `CC-G5.19`      | **Conditional (QD).** If `G.5:Ext.NQD` is present, the required QD telemetry triple (quality, diversity, and QD summary) **MUST** be computable and ready for emission under the pinned descriptor and distance definitions and archive policy, without redefining their semantics in G.5. If actual publication is current, use E.17 for a source-backed face and return to source and E.24.PUB for the publication occurrence and audience availability. |
| `CC‑G5.20`      | **Conditional (QD).** QD and illumination summaries are treated as telemetry unless explicitly promoted by a pinned acceptance or policy record; the selector must record the promoting policy id in audit pins. |
| `CC-G5.21`      | **Conditional (Archive and QD).** Any use of archives **MUST** declare `InsertionPolicyRef` and pin the required editions for reproducibility, including descriptor and distance definitions and any method editions they depend on. |
| `CC‑G5.22`      | **Conditional (QD).** Twin‑naming discipline for descriptor vs plain space (if used) must be respected (distinct objects; no aliasing).  |
| `CC-G5.23`      | **Default rule for** `DefaultId.PortfolioMode`. The selector **MUST** expose `PortfolioMode` with values `Pareto` or `Archive`, with **default = `Archive`**, and echo it in DRR and SCR records and declared selector results when not explicitly overridden by pinned policy or TaskSignature. The default is a retention and evidence-preservation policy, not a public selected-set label, not a dominance default, and not a substitute for `SetResultFamily`. Epsilon-fronts are allowed as *local* decision aids under `CG-Spec` when explicitly pinned. |
| `CC-G5.23a`     | **Parity-run publication.** If parity harness is in use, a selector or generator **MUST** publish a parity run and `ParityCard` to **UTS** (see `G.9`). This obligation remains mandatory irrespective of dominance policy or `PortfolioMode` policy. |
| `CC‑G5.24`      | **Conditional (Open‑Ended).** If `G.5:Ext.OpenEndedFamilyWiring` is present, the selector **MUST** return declared sets of `{Environment, MethodFamily}` pairs as set‑valued outcomes under explicit pins. |
| `CC‑G5.25`      | **Conditional (Open‑Ended).** In Open‑Ended mode, `TransferRulesRef.edition` is mandatory and **MUST** be visible to telemetry and RSCR triggers.  |
| `CC-G5.26`      | **Conditional (Archive and QD).** Within any archive niche or cell, ordering and tie-breaks **MUST** remain admissible over compatible scales; inadmissible mixed-scale weighted sums are forbidden. |
| `CC‑G5.27`      | If the selector cites any `GateCrossing`, the corresponding `CrossingBundle` publication **MUST** be present and conformant; missing or non‑conformant `CrossingBundle` blocks downstream consumption. The bundle packages already governed crossing evidence for that named use; it **MUST NOT** create the F.17 endpoints, F.9 Bridge, bounded-use proposition, A.10/B.3 reliance, gate decision, authorization, or actual selector use. |
| `CC‑G5.28`      | **Default rule for** `DefaultId.DominanceRegime`. `DominanceRegime` **SHALL** default to `ParetoOnly`. Any inclusion of additional telemetry dimensions into dominance (e.g., illumination) requires an explicitly pinned acceptance or policy record and must be recorded in audit pins. **Parity‑run publication (CC‑G5.23a) remains mandatory** irrespective of dominance policy. |
| `CC-G5.29`      | **Conditional (QD and Open-Ended).** Any telemetry event that materially changes an archive state or retained-set state **MUST** identify the exact changed state and affected-use scope, log `PathSliceId` when graph-scoped or independently required by the receiving contract, and retain the active policy id and active editions of the relevant definition pins (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `TransferRulesRef.edition` when applicable) and expose them to RSCR triggers. |
| `CC‑G5.30`      | **No Strategy minting.** Within `G.5`, “strategy” is a policy‑bound composition template; the pattern **SHALL NOT** mint a durable U-kind named `Strategy` (E.10 and E.24.UK discipline). If a stable reference is needed, publish composition and policy ids (e.g., UTS entries) rather than minting a universal kind. |
| `CC-G5.31`      | **Strategy hint on non-admissible sets.** If selection yields `CandidateSet = EMPTY`, the selector **SHALL** emit an explicit escalation hint (`ActionHint`) that is compatible with DRR and SCR records and auditable: include the top three actual blocking constraints as cited ids and pins, or all actual blockers when fewer than three exist, and where applicable include the relevant edition pins, for example `TransferRulesRef.edition` in Open-Ended mode, to guide exploration under explicitly pinned lenses such as the exploration and exploitation log policy. |
| `CC‑G5.32`      | **Parity‑run publication and admissible roll-ups.** If parity harness is in use, parity publication is required per `CC‑G5.23a` (ID‑continuity). Any scalar roll-up or summary view **MUST** be admissible under **CG‑Spec** (no mixed‑scale sums), and published views must preserve set‑return semantics (no single‑score leaderboards as authoritative outputs without an explicit, admissible comparator publication). |
| `CC‑G5.33`      | **Conditional (bounded specialization).** When the selection question is acquisition of usable specialization on a declared `TaskFamilyRef` or `TaskSignature`, selector outputs **SHALL** either emit `TaskFamilySpecializationProfile@Context` or cite equivalent pins carrying the `C.22.1` adaptation-signature fields needed for comparison: work-measure threshold target, prior exposure declaration, time-to-threshold, budget-to-threshold, post-threshold efficiency when relevant, and any declared transfer, retention, downside, or specialization-entry notes. |
| `CC‑G5.34`      | **Selected-set result kind.** When `SelectorOutcomeKind = SetResultOutcome`, the public result kind **MUST** be explicit. Use `Shortlist` for unordered alternatives retained for later choice, `RankedShortlist` only when the result orders those alternatives, and `JointUseSet` only when every named member is included for one named use. `ChoiceSet` **MUST NOT** silently replace the public result kind. |
| `CC‑G5.34a`     | **Selector outcome typing.** Declared selector results **MUST** state `SelectorOutcomeKind`. `SetResultFamily` is required only when `SelectorOutcomeKind = SetResultOutcome`; `HandoffKind` is required only when `SelectorOutcomeKind = HandoffOutcome`. Non-set outcomes **MUST NOT** masquerade as one public selected-set label. |
| `CC‑G5.35`      | **Result-content closure.** Any declared selector result **MUST** state the `SelectorOutcomeKind`, applicable public result kind, retained members or keyed joint-use entries, ordering, named use and inclusion conditions when required, and basis pins directly in the emitted result rather than relying on upstream `C.11`, `C.19`, or `C.24` notes. |
| `CC‑G5.36`      | **Neighboring-pattern boundary.** If the current question is still local choice among already-available options, pool policy over still-live candidate lines, or enactment planning after choice, a `G.5` use **MUST** consume the result produced by applying `C.11`, `C.19`, or `C.24` rather than restating those patterns as if declaring selector-facing content decided the upstream matter. |
| `CC‑G5.37`      | **Derived tradition-view result discipline.** If the selector emits one result through a derived tradition view such as `TraditionFront` or `TraditionArchive`, it **MUST** keep the declared base `SourceSetFamily` explicit, keep `SoTAPaletteDescription` recoverable through `BasePaletteRef`, and **MUST NOT** let the derived view become the default meaning of `Tradition`, `TraditionPalette`, or the base palette. |
| `CC‑G5.38`      | **Causal method dispatch declarations.** If method selection involves causal methods, each compared method **MUST** declare `causalMethodUseClassification` as observational predictor, intervention optimizer, counterfactual strategy, causal fairness estimator, causal-RL policy, or simulation-only method, and **MUST** carry `causalUseSupportResultRef` and the cited result's verdict when it consumes `C.28` causal-use support rather than treating method dispatch as causal certification. |
| `CC-G5.39`      | **Registry grounding, edition, and grouping boundary.** Every consumed method-family row **MUST** be addressed by one exact `MethodFamilyRowRef` whose immutable edition resolves its non-empty `MethodRef[]` to exact A.3.1 Methods; every consumed generator-family row **MUST** use one exact `GeneratorFamilyRowRef` and resolve non-empty exact generator refs under their subject patterns. Each row edition cites the independently established classification, membership relation, or explicit project-local grouping criterion used by this selector. A row, id, label, description, family card, eligibility or maturity record, policy, evidence pin, shortlist, or publication **MUST NOT** create a member or membership fact. Missing grounding or an unresolved row edition blocks that row's family use. |
| `CC-G5.40`      | **Composition and selected-structure boundary.** A composition shape **MUST** remain a template unless one already identified A.3.1 Method separately passes B.1.5's complete composite-method qualification. An organization that does not constitute one Method **MUST** be consumed as an A.22 `U.Structure` only after all four A.22 identity discriminators are present. A template, A.3.2 description, registry row, selector outcome, diagram, label, or notation **MUST NOT** create either governed object or its underlying relations. |
| `CC-G5.41`      | **Declaration, actuality, performer, result and publication boundary.** A registry, selector, policy, template, shortlist, DRR, SCR, telemetry or publication-content declaration **MUST NOT** be treated as an A.13 performer core, dated Work, F.6 attribution, actual A.6.1 `Select` application or binding, domain-result truth, C.2.1 result episteme, A.10 evidence-provenance path, B.3 assurance claim, authorization, or E.24.PUB publication occurrence. Every claimed precise performer **MUST** first have the A.13 core; A.15.1 **MUST** admit the Work independently; F.6 enters only for a current exact assignment-bound attribution through the same obtaining assignment. Every other claimed actual object or relation **MUST** be recovered under its subject pattern; missing actuality blocks only that stronger claim. |
| `CC-G5.42`      | **Crossing completeness.** A selector use that relates expressions with distinct source-local meanings **MUST NOT** proceed from Bridge, CL, loss, registry, policy, `CrossingAllowance`, `GateCrossing`, `CrossingBundle`, DRR, or SCR pins alone. It requires exact F.17 endpoint senses, an obtaining F.9 Bridge, a separate C.2.1 bounded-use proposition, and the matching A.10 reliance disposition or B.3 assurance branch; authorization and the actual selector application remain separate. |
| `CC-G5.43`      | **Ordinary-use proportionality.** A bounded selector run over already grounded rows **MUST** be usable from the exact task, immutable row-edition refs, Methods and grouping bases, declared eligibility or comparison basis, truthful outcome, members, ordering status, basis refs and next use. It **MUST NOT** demand a fresh registry build, crossing branch, A.10 reliance claim, B.3 assurance claim, stable public identity, or E.24.PUB occurrence unless that stronger object or claim is current. The dated selector Work required by S3 remains independently admitted; upstream mathematical comparisons need their actual application bindings, with separate comparison Work only when asserted. Missing conditional apparatus blocks only the stronger claim. |
| `CC-G5.44`      | **Joint-use membership integrity.** A declared selector-result record with `SetResultFamily = JointUseSet` **MUST** name one bounded use, set `ordering = unordered`, and use keyed `memberEntries` with each exact `memberRef` present at most once. Entry order has no semantic effect; the result **MUST NOT** add an undefined per-member contribution or basis field; and any top-level `members` **MUST** be only the unique set projection of the entry keys, never an independently maintained list. Exact supporting content or claims remain in their own records and may be cited only among sufficient top-level `basisPins`. |
| `CC-G5.45`      | **Joint-use ontic and actuality boundary.** A declared selector-result record with `SetResultFamily = JointUseSet` is well formed only if every exact framework-edition or other non-Method `memberRef` resolves under its existing identity and the record adds no `MethodRef` value or registry row merely for membership. Candidate-pool and excluded-candidate records, direct member relations, local choice, actual selection Work, publication availability, and access remain separate. |
| `CC-G5.46`      | **Operation-path integrity.** A `JointUseSet` over non-Method members **MUST** be emitted through `G.5-6 DeclareSetResult` from exact already identified `memberRef` values and a current inclusion basis; it **MUST NOT** use `RegisterFamily` or `G.5-3 Select`. `DeclareSetResult` **MUST NOT** be treated as the upstream choice, an actual `Select` application, dated Work, persisted result episteme, or E.24.PUB availability occurrence. |
| `CC-G5.47`      | **G.4 TaskMap receiving boundary.** `TaskMapRef` is required only when this selector uses G.4 CAL gates. Its immutable map edition **MUST** cite the same C.22 `TaskSignatureRef` supplied to selection, resolve one exact `CALCharterRef` and every cited clause, operator, flow, and evidence profile at its exact edition, and travel in result-basis and refresh pins. A mismatch or unresolved ref blocks that gated use. The map **MUST NOT** construct the TaskSignature, copy thresholds, duplicate acceptance semantics, or become mandatory for an ordinary selector with no G.4 gate. |

### G.5:8 - Common Anti-Patterns and How to Avoid Them

* **Anti‑pattern: “Selector as a shadow spec.”**
  *Symptom:* local acceptance or admissibility rules appear in selector prose or code, diverging from CN, CG, and CAL.
  *Avoid:* govern constraint semantics through `CNSpecRef` and `CGSpecRef` plus pinned CAL records; keep G.5 core as a boundary.

* **Anti‑pattern: “Implicit crossings.”**
  *Symptom:* reuse across distinct source-local meanings is claimed from a shared label, Bridge or CL pin, registry row, policy, DRR or SCR line, `GateCrossing`, or `CrossingBundle` without the required relation, use, and reliance facts.
  *Avoid:* resolve the exact F.17 endpoint senses; establish the F.9 Bridge; state the separate C.2.1 `<u,d,r,t,polarity>` claim; require the matching A.10 disposition or B.3 assurance branch; and keep authorization and actual selector use separate. Materialize or cite a bundle only when its named downstream use requires that durable package.


* **Anti‑pattern: “Hidden scalarisation.”**
  *Symptom:* partial orders are flattened into single winners “for convenience”.
  *Avoid:* return declared sets; make dominance regimes explicit; keep telemetry report‑only unless promoted by explicit policy.

* **Anti‑pattern: “Method specifics in the selector head.”**
  *Symptom:* QD, OEE, or preference models become mandatory for basic dispatch.
  *Avoid:* keep them in `G.5:Ext.*` blocks with explicit pins and `Uses`.

* **Anti‑pattern: “Churn by meaning.”**
  *Symptom:* a continuing family id silently resolves different members, grouping basis, or selection pins after a row changes.
  *Avoid:* keep the lineage id only for the continuing declared grouping, publish a new immutable row edition, and carry its exact row ref through selection, result basis, refresh, and deprecation notices.

* **Anti‑pattern: “Result declaration hidden in upstream reasoning.”**
  *Symptom:* the retained alternatives or all-member result exist only as one implication inside `C.11`, `C.19`, or `C.24`, while `G.5` never names the declared result kind.
  *Avoid:* declare the selected-set result directly, with its result kind, applicable members or keyed entries, ordering, named use where required, and basis pins instead of leaving it implicit upstream.

* **Anti-pattern: “Shortlist used for complementary members.”**
  *Symptom:* every named member is needed for one use, but the result calls them alternatives in a `Shortlist`.
  *Avoid:* use `JointUseSet`, name the joint use, and key one entry per exact member; keep direct member relations and actual selection separate.

* **Anti‑pattern: “Declared result missing required content.”**
  *Symptom:* a `Shortlist`, `JointUseSet`, narrowed handoff, or abstain result is named, but the emitted result still omits its members or keyed member entries, ordering, named use where required, or basis pins.
  *Avoid:* state the result kind, retained members or keyed joint-use entries, ordering, named use where required, abstain or escalation condition, and basis pins directly in `G.5`.

### G.5:9 - Consequences

* **Auditable plurality.** Multiple Traditions can co-exist without forced semantic flattening; dispatch remains explainable and evidence-pinned.
* **Core stability.** Universal invariants are pinned through `G.Core`; method innovation and generator innovation do not churn the selector head.
* **Evolvability.** Registries allow growth, retirement, and refresh with typed RSCR causes and explicit payload pins.
* **Composability.** Strategy templates and fallbacks remain admissibility-checked and portable across implementations.
* **Recoverable result content.** Selected-set results can travel downstream as explicit shortlist-family, joint-use, handoff, abstain, or escalation results rather than one hidden implication inside upstream reasoning.

### G.5:10 - Rationale

* **Why registries?** Reusable method-family dispatch requires stable, auditable row editions with explicit eligibility and assurance records, so later uses can recover the grouping and its dispatch basis.
* **Why separation via Extensions?** QD, OEE, preference-learning, and similar families are fast-moving and method-specific; making them part of the selector head would force a universal semantics and violate strict distinction.
* **Why set-return?** Partial orders are common and often the only admissible representation under heterogeneous scales; set-return preserves semantics and makes tie criteria explicit.
* **Why explicit defaults with one declared source?** Defaults are unavoidable; single-source indexing prevents competing defaults from silently diverging across patterns.
* **Why selected-set result declaration here?** Once the current question is to state retained alternatives or an all-member result for downstream use, the selector should declare that result directly instead of leaving it implicit in local choice, pool-policy, or enactment notes written for other purposes.
* **Why `JointUseSet`?** A shortlist preserves alternatives for later choice; an all-member result says that removing one member changes the result for the named use. G.5 mints `JointUseSet` only as a local `SetResultFamily` value and reuses the existing outcome schema and member identities. `G.5-3 Select` may emit it only over exact Method candidates admitted through that kernel; `G.5-6 DeclareSetResult` covers exact already grounded members without retyping them as Methods. Neither branch mints a new U-kind, Method kind, relation kind, or registry kind. `CoUseSet` is less plain, `ComplementarySet` would imply a relation among the members, and `Bundle` would misname a package form.

### G.5:11 - SoTA-Echoing — return what the receiving use can actually select

**Practice question.** What should a dispatcher hand over when several candidates remain useful but the declared comparison does not justify one winner? The selected line returns the admissible alternatives with their ordering status and basis. A serious default chooses one best candidate under a declared objective and returns it ready for use. That default is efficient when the objective settles the choice; it loses a needed alternative when an undeclared scalar objective is substituted for an unresolved trade-off.

The [scikit-learn GridSearchCV documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html), `refit` and `best_estimator_`, supplies the concrete default. It can choose one estimator by a scorer or a custom rule over the evaluation results; multi-metric evaluation still needs a specified refit choice. **Adopt** that explicit-choice requirement when G.5 emits an ordered result. **Reject** reading a single best-estimator interface as a warrant to invent the missing comparator. The library supports custom choices and exposes other candidate results; it does not require G.5 to discard them.

[PS-AAS, Kostovska et al. (2023)](https://proceedings.mlr.press/v224/kostovska23a.html) supplies a substantive alternative-selection line: form a complementary portfolio for later algorithm selection, balancing coverage with the cost of a larger choice problem. Its experiments concern specified CMA-ES variants and BBOB tasks, not arbitrary Methods. **Adapt** the distinction between forming an eligible pool and selecting a member to `Shortlist` and `RankedShortlist` in §4.4b, S3 and the pump case in §0.5. The selected line here is this result discipline, not a claim that PS-AAS is the best portfolio algorithm for every task.

A different receiving use combines members. [Split-Ensemble, Chen et al. (2024)](https://proceedings.mlr.press/v235/chen24aw.html) supplies a concrete counterexample to treating every retained set as alternatives: its submodels serve complementary subtasks in one ensemble. **Adapt** that use distinction to `JointUseSet` and `G.5-6 DeclareSetResult`. G.5 states all-member inclusion; the paper's trained ensemble does not establish compatibility or effective combined use for an arbitrary set of framework editions. Show 4 therefore keeps those claims with their own patterns.

In §0.5 both grounded pump Methods meet the task constraints, but no admitted comparator orders them. With the same candidate evidence, returning the pair as an unordered `Shortlist` preserves the receiving choice at the cost of one further decision. Naming the spectral Method “best” would require an additional criterion and its supporting comparison. If that criterion is supplied and actually orders the candidates, a ranked result is available. If the receiving use includes every exact member, declare that different membership meaning; a ranking does not establish it. These distinctions govern the outcome declarations and the positive, ranked, no-survivor and joint-use cases in §5.

Reopen when new evidence changes eligibility, a comparator supplies or defeats an ordering, the downstream use changes from alternatives to joint inclusion, or keeping the retained set costs more than the receiving decision can bear. A bounded handoff or abstain outcome remains available. None of these sources establishes actual selection Work, a Method's identity, public availability or assurance merely from the emitted result.

### G.5:12 - Relations

**Builds on (normative):** `G.Core` (core invariants + linkage discipline).

**Uses (conceptual dependencies; cited via pins and ids):**

* Specification refs required by this result: `A.19.CN (CN‑Spec)`, `G.0 (CG‑Spec)`. Use `A.2.6` only when a `U.ClaimScope` or selected `U.ContextSlice` changes selection, applicability, or a receiver's justified reliance; validity and evaluation windows and intended-use restrictions follow the same conditional boundary.
* Method identity and family grouping: `A.3.1` for every exact selectable `U.Method`; `A.3.2` only for the same C.2.1 episteme that substantively describes one already admitted Method; and C.2.1 or the defining declaration or pattern for the family relation cited by a registry row. G.5 creates none of those source facts.
* Method composition and selected organization: `B.1.5` for the complete composite-Method qualification, `A.22` for an independently selected organization that does not constitute one Method, and `C.29` for algebraic, graph, matrix, embedding, neural, or other representation-lens use. G.5 consumes exact resulting references and does not construct them.


* Upstream object sets: `G.1 (CG‑Frame Card)`, `G.2 (SoTA Pack)`, `G.3 (CHR Pack)`, and `G.4 (CAL Pack)`. C.22 alone constitutes the TaskSignature. When G.4 CAL gates are current, G.5 additionally consumes the exact `TaskMapRef` that relates that same `TaskSignatureRef` to one exact charter and the cited CAL declarations; otherwise the map is absent.
* Evidence and crossings: `G.6` for EvidenceGraph citations; `F.17` for exact local senses; `F.9` for the direct Bridge; C.2.1 for the separate bounded-use proposition; and `A.10` or `B.3` for reliance or assurance. Add a `CrossingBundle` under `E.18` or a GateCheck under `A.21` only when that named downstream use requires one. A G.7 calibration artifact remains a cited policy or evidence input; it does not define the Bridge, bounded use, reliance, or selector actuality.

* Planning and enactment boundary: `A.15.2` identifies the `U.WorkPlan` used as `plannedBaselineRef`; A.15.3 defines any planned-filling rows kept inside that WorkPlan. G.5 does not redefine them.
* Actual selector use and result availability: `A.19.SelectorMechanism` and A.6.1 for the actual `Select` application and bindings; A.13 for every precise performer's local-kind criterion, classification, same obtaining assignment, scope, situation, window, and evidence; A.15.1 for independent Work admission; A.2.1 for the assignment species and occurrence; and F.6 only for a current exact assignment-bound attribution. When asserted by the account or consumed by its receiving use, A.2.4 governs evidence use, A.10 governs reliance and provenance, G.11 governs currentness, C.2.1 governs a persisted result episteme, B.3 governs assurance, the direct authority pattern governs authorization, and E.24.PUB governs publication. Upstream CPM applications retain their local bindings without requiring separately admitted comparison Work unless that Work is asserted. A root-family assignment reference, temporal overlap, or omission from short wording supplies no attribution and removes no world-side fact. G.5 declarations and records create none of those neighboring facts.
* Joint-use members outside Method dispatch: the direct identity pattern identifies every `memberRef`; `C.11` supplies a local choice result when one is current; another accepted decision or governed inclusion basis may establish all-member inclusion; E.4.PFR states framework-edition dependency or pairwise compatibility separately; `G.11` supplies currentness; and E.17/E.24.PUB plus the applicable access-carrier pattern supply exposure and source return. `G.5-6 DeclareSetResult` consumes the exact members and sufficient basis pins and emits only the selector-facing membership result.

* Causal-use method dispatch: `C.28` when method selection involves causal effect, counterfactual comparison, causal fairness, causal policy, causal RL, or simulation-only causal-use claims.
* Optional Method or generator extensions through `G.5:Ext.*`: `C.18`, `C.19`, `C.23`, plus extension-bearing patterns whose exact Part G admission relation is established when they add extra selector pins.
* Mathematical-lens use: apply `C.29` when a selector input depends on a mathematical object or mapping whose use is not yet recoverable—for example, a comparator, distance, descriptor geometry, embedding, normalization, surrogate model, learned representation, QD archive descriptor, model-family label, or model-selection basis. For claim-bearing lens use, recover that object's mapping mode, preserved or lost structure, and stop condition. A `LensCandidateNote` may instead retain the recognition and next-action account while `CandidateMathObject?` remains unresolved. The recorded result is a C.29 lens-use result; non-exhaustive examples include no lens use, a lens-candidate note, a one-line note, a mini-card, a full card, or a note naming the applicable pattern for the stated selector use. That result does not declare a selector result or its supporting records, such as the selected set, selector policy, registry row, shortlist, ranked shortlist, or selector evidence pins; use `G.5` for those objects and cite the exact references used.

**Provides to:** downstream uses such as `G.6` audit citations, RSCR emission records with typed triggers and payload pins, and packs shipped through `G.10`. When a named use needs stable public identity, publish the required family ids, selector policy records, or selected-set identities—such as `ShortlistId`—to `UTS` under the applicable identity rule.

**Coordinates with:** `C.11` for local choice results; E.4.PFR for direct framework-edition dependency and pairwise compatibility claims; G.11 for edition currentness; E.17 for a source-backed publication face and return to source; E.24.PUB for a publication occurrence and audience availability; `C.19` for pool-policy records; `C.32.P2S` when a selected-set result declaration feeds architecture problem-to-structure carry-through; `C.35` when a generated or discovered structure-bearing output is not yet a selector-facing result; `C.24` for enactment-facing next-action records; and `C.18` when a `Front` or `Q-front` is the source set for a G.5 use.

A `Q-front` stays a C.18 source set; it is not the emitted G.5 outcome or a `SetResultFamily`. The G.5 result states one admitted `SelectorOutcomeKind`; a set result also states `Shortlist`, `RankedShortlist`, or `JointUseSet`, and any public selected-set label resolves to that family.

Architecture discovery boundary: when a generated or discovered structure-bearing output is only a representation or carrier—for example, a description, query result, graph, cluster, or search trace—use `C.35` before G.5. Use G.5 only when the live claim is declaration of selected-set result content with selector-policy and selected-set identity; stable public identity and actual publication remain conditional neighboring branches.

### G.5:End
