## G.2 - Harvest and Synthesize SoTA for a CG-Frame

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative *(unless explicitly marked informative)*
>
> **Purpose.** Provide a repeatable, auditable way to **discover**, **triage**, and **synthesize** state‑of‑the‑art (SoTA) across competing `Tradition` lineages *before* minting CHR/CAL/LOG assets for a `CG‑Frame`.
>
> **Start here.** Write the question the receiving CHR, CAL or selector work must answer. Before counting coverage, fix the source population and what counts as the same family. Distill the first source claims with their editions, evidence and limits, keeping competing lineages separate. The first useful result is a claim set that can answer part of that question and expose what is still missing. Use the manifest below when developing it into a conforming synthesis pack; a single-source fact lookup can return its source directly without creating such a pack.
> The primary output is a **`SoTA Synthesis Pack@CG‑Frame`** that feeds:
>
> * naming/publication (UTS),
> * CHR authoring (G.3),
> * CAL authoring (G.4),
> * method/generator registries and dispatch (G.5).
>
> **Scope note.** This pattern **governs** the harvesting + synthesis *generator* in Part G. Use **G.10** to ship the pack and **G.11** to orchestrate refresh.
>
> **Terminology note (normative).** In normative clauses below, **`Tradition`** refers to the *Tech* token `Tradition` (a plural lineage with internally coherent commitments). Plain “tradition” is allowed only as a 1:1 synonym.

### G.2:1 - Problem frame

A team extends FPF into a new `CG‑Frame`. The relevant literature is typically:

* **plural** (multiple `Tradition` lineages with incompatible commitments),
* **source- and use-sensitive** (results depend on the exact source and edition, claim region, EntityOfConcern, comparison basis, evidence, and receiving use),
* **method‑heterogeneous** (different evidence styles, operator sets, and validity regions),
* **time‑sensitive** (rapid drift post‑2015; frequent benchmark/protocol shifts).

Downstream Part-G work in CHR, CAL, selection, shipping, and refresh depends on citation-ready claims that keep each exact CG-frame, source edition, claim region, EntityOfConcern, comparison basis, evidence anchor, and actual cross-source relation recoverable.

### G.2:2 - Problem

How can we systematically assemble a SoTA view that is:

1. **pluralist but comparable** (plurality preserved; comparability is achieved only via explicit crossings),
2. **evidence‑addressable** (claims cite auditable evidence surfaces and anchors),
3. **actionable** (produces inventories and citable publication forms usable in G.3, G.4, and G.5 without treating a card as a meaning container or selector authority),
4. **refreshable** (editions/policies/windows are pinned so RSCR/refresh can re‑audit and re‑run without semantic drift)?

### G.2:3 - Forces

* **Pluralism vs. consolidation.** Consolidation is valuable, but unqualified fusion destroys meaning.
* **Breadth vs. load‑bearing depth.** Too broad becomes shallow; too deep misses rival lineages.
* **Recency vs. stability.** Freshness matters, yet durable “backbone” claims must be identified and kept visible.
* **Pedagogy vs. rigour.** Outputs must be teachable enough to support review, while remaining audit‑ready.
* **Authoring vs. operations.** This pattern governs authoring; use the applicable Work and decision patterns for operational runs and decisions.

### G.2:4 - Solution

#### G.2:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

**GCoreLinkageManifest (normative).**
*(Canonical form, Nil‑elision, and Expansion rule are defined in `G.Core`.)*

```text
GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted
  },
  RSCRTriggerSetIds := {GCoreTriggerSetId.SoTAHarvestSynthesis},
  CorePinSetIds := {GCorePinSetId.PartG.CrossingVisibilityPins}, // expands only for actual channel/receiving-use conditions under G.Core:4.2.3; no crossing means no crossing pins

  CorePinsRequired := {
    // Scope pins (G.2‑specific)
    CGFrameId, // identifies the exact CG-frame, which is the declared framing episteme; its cited ClaimGraph keeps source and edition, claim regions, EntityOfConcern, comparison basis, and intended use recoverable
    Tradition[],
    entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩,
    SoTA_SetId,
    SoTAPaletteDescriptionId,

    // Evidence / provenance pins (G.2‑specific)
    CorpusLedgerId,
    FlowRecordId,
    EvidenceAnchorRef[],
    EvidenceGraphId?,

    // Crossing / synthesis pins (delta beyond CorePinSetIds; only when used)
    GammaEpistSynthId[]?,

    // Edition / policy pins (only when used)
    HarvestPolicyRef?, // required when a coverage judgement is made
    CoverageJudgementRef?, // the pack judgement, required for a relied-on coverage result
    DistanceDefRef.edition?,
    InclusionCriteriaId?,
    ScreeningRubricId?
  },

  DefaultsConsumed := ∅,
  TriggerAliasMapRef := ∅
⟩
```

*(RSCR payload pins: `ClaimSheetId[]`, `SoTA_SetId`, `SoTAPaletteDescriptionId`, `BridgeMatrixId?`, `GammaEpistSynthId[]?`, `UTSRowId[]?`, `DistanceDefRef.edition?`, `HarvestPolicyRef?`, `InclusionCriteriaId?`, `ScreeningRubricId?`, `PathId/PathSliceId?` when path‑citable evidence or a stable freshness window is pinned.)*

**Pattern‑local default rules (governed by this pattern; not a Part‑G‑wide `DefaultId`).**

`FamilyCoverageFloorK := 3` *(unless explicitly overridden by `HarvestPolicyRef` and recorded in `FlowRecord`)*. This threshold supplies no counted population or same-family rule; those must be explicit before a coverage judgement. An undefined basis is unassessable, not a measured failure. Whenever coverage is judged, `HarvestPolicyRef` is required even when k uses this fallback; its applicability, receiving question, counted population/scope, grouping and same-family equivalence must be fixed before counting. An override changes k, not the unit or the independent pluralism duties.

**Counted-family basis.** The HarvestPolicy defines which candidates enter the counted population and when two entries represent the same family for this receiving question. Count equivalence classes under that rule. Repeated cards, aliases and source references for one family add zero. A combined method/generator population needs one receiving purpose and an overlap rule: a generator that is also a method is not counted twice unless the policy deliberately defines separate role-qualified units and justifies that interpretation. Freeze this basis before inspecting the count; changing it to turn a failure into three is not a repair of coverage.

The pack's coverage judgement carries the policy/edition, counted units, deduplication basis, count, k and pass/fail result, or the exact missing basis when unassessable. Give this existing pack component a local `CoverageJudgementRef` for citation. Evaluate lineage and materially distinct entry plurality separately. Cards and downstream consumers cite this same judgement instead of choosing their own unit. Compare counts across packs only when their bases match, or after an explicitly justified common-basis recount.

#### G.2:4.2 - Kit: `SoTA Synthesis Pack@CG‑Frame` (surface governed by this pattern)

A conforming `G.2` publication produces a **notation‑independent pack** whose internal organisation is free, but whose exported **named components and views** are stable and citable:

Each named component is addressable via a stable **pack‑local identifier** (e.g., `CorpusLedgerId`, `ClaimSheetId`, `FlowRecordId`) for citation and RSCR scoping. If any component is minted/evolved as a **public id**, it is published and cited via `UTSRowId[]` per `CC‑GCORE‑UTS‑1` (delegation).

0. **`SoTA_Set@CG‑Frame`** *(export view; “M2 output” consumed downstream)*
   A read‑optimised view over the harvested candidate set that downstream generator/selector work treats as the “harvester output set”.
   **Constraint (normative):** `SoTA_Set@CG‑Frame` **MUST** be reconstructible from pack components by id (no “hidden extra set”). Its coverage result cites the pack's `CoverageJudgementRef`, including its fixed HarvestPolicy basis; the export view does not redefine family membership.

1. **`G.2a CorpusLedger`**
   Ledger of candidate sources. Each row names the exact source and edition, claim region used, triage status (for example, include, park, or retire), evidence locator, and rationale for this CG-frame and receiving use.

2. **`G.2b ClaimSheets[Tradition]`**
   Typed Claim Sheets per `Tradition`, each with:

   * exact source and edition, claim region, effective ReferenceScheme where meaning matters, EntityOfConcern, and comparison basis for the stated use,
   * explicit evidence anchors/citations (A.10 and/or EvidenceGraph refs when available),
   * explicit freshness window notes and risk/trust cues *(cite `B.3` governing definitions when using trust/decay language)*.

3. **`G.2c OperatorAndObjectInventory`**
   Inventory of candidate CHR terms (characteristics/scales/coordinates) and candidate CAL operators/flows *as stubs* for downstream authoring.

4. **`G.2d BridgeMatrix`**
   A citable alignment/divergence surface across `Tradition`×`Tradition`, with explicit losses and row scopes.
   If any row asserts substitution or fusion across sources or across `Tradition` records, the pack **MUST** attach a `GammaEpistSynthId` record (alias: **`G.2‑F`**) per `G.2:Ext.GammaEpistSynthesis` (no silent fusion).

5. **`G.2e MicroExamples`**
   Worked micro-examples for load-bearing claims. Each names the exact source and edition, claim region, EntityOfConcern, comparison basis, and intended use; cites its evidence carrier or A.10 evidence-provenance path; and annotates applicable assurance types (`TA`, `VA`, or `LA`). The example card is only a publication form for those claims.

6. **`G.2f UTSProposals`**
   Draft Name Cards + Minimal Definitional Sheets (MDS) + alias proposals (incl. concept‑set linkage where applicable), with the required publication pins.

7. **`G.2g entityOfConcern Map`**
   Map from key terms/claims/public ids to `GroundingHolon`, `ReferencePlane`, and minimal reference cues for later CHR/CAL authoring.

8. **`G.2h PRISMA Flow Record`**
   A screening/eligibility trail for how sources entered the pack (method‑profile is allowed; see Extensions).
   *(Name is historical; the artefact remains notation‑independent.)* The pack coverage judgement and its policy basis are recoverable here, separately from the lineage and material-entry pluralism results.

9. **`G.2i SoSIndicatorFamilies`**
   Indicator *families* as variants (windows/constraints/assumptions) **with explicit Acceptance branches per variant** (branch ids/labels only; threshold semantics belong to CAL governing definitions).

10. **`G.2j MethodFamilyCards`**
    Candidate method families with a shared signature and a plurality of implementations, each with validity regions, cost/complexity notes, and known failure modes.
    When the pack targets downstream registry/dispatch, MethodFamily cards **SHOULD** include the declared refs and pins `G.5` needs (eligibility predicate refs, assurance profile cues, and the pack ids that justify the family).

11. **`G.2k GeneratorFamilyCards`** *(if applicable)*
    Candidate generator families for environment/task generation with declared validity regions and transfer hooks.

12. **`G.2l Annexes`** *(optional; governing-definition-cited; see Extensions)*
    For example: QD/NQD annexes, discipline‑specific indicator annexes, interop forms.

**SoTAPaletteDescription** *(export view; required downstream)*
A view‑friendly description object (pack‑local `SoTAPaletteDescriptionId`) that binds together:

* the `SoTA_Set@CG‑Frame` view,
* `ClaimSheetId[]`, `OperatorAndObjectInventory`, `BridgeMatrixId?`,
* `SoSIndicatorFamilies` (with variant/branch structure),
* `MethodFamilyCards` / `GeneratorFamilyCards?`,
* `MicroExamples`, `UTSProposals`,
* and the `entityOfConcern Map` for citation and later CHR/CAL authoring.

**Note (normative intent):** this is the primary “consumable surface” for `G.3/G.4/G.5`; it prevents downstream patterns from scraping free prose.

**Editorial template: 1‑page “SoTA Sheet” per Tradition (informative).**
When authoring `ClaimSheets[Tradition]`, teams often benefit from a single‑page template: scope + claims + evidence anchors + validity region + failure modes + freshness window + cross‑Tradition reuse notes + pointers to micro‑examples.

#### G.2:4.3 - Harvester loop (conceptual choreography; pattern-governed)

A conforming `G.2` pack publication is built by iterating the following conceptual loop until the declared gates are satisfied:

1. **Declare scope and plurality.**
   Identify the exact CG-frame (the declared framing episteme), the initial `Tradition` set, each intended claim region and EntityOfConcern, the comparison basis, and the receiving use. Record the cited CG-frame and source editions and evidence anchors in the pack pins rather than hiding them in a generic context field. Before counting, fix the HarvestPolicy's receiving question, counted population, grouping and same-family equivalence, including overlap handling for a combined population.

2. **Discover and triage sources (ledger‑first).**
   Populate `CorpusLedger` via:

   * adding seed sources,
   * expansion via citation chaining and keyword family exploration,
   * pruning using load‑bearing relevance tests tied to the declared CG‑Frame scope.

3. **Distill claims per `Tradition`.**
   For each `Tradition`, author a Claim Sheet that preserves internal commitments and cites evidence anchors. Do not fuse cross‑`Tradition` claims at this stage.

4. **Inventory operators/objects for downstream authoring.**
   Extract candidate measurement terms and operator stubs for later CHR/CAL authoring (without asserting legality or thresholds locally).

5. **Build alignment/divergence surfaces.**
   Where reuse across `Tradition` is desired, record the obtaining correspondence and its exact basis in `BridgeMatrix`: F.9 for sense correspondence, C.3.3 for kind correspondence, or the direct rule for a plane relation, as actually used. State preserved distinctions and losses for the receiving question. Consolidation requires explicit alignment proof. Add bundle or gate anchors only for an independently applicable E.18 flow crossing or A.21 gate, under `CC‑GCORE‑CROSS‑1`.

6. **(Alias: G.2‑F) Produce Γ_epist synthesis records when fusion/substitution is asserted.**
   If a `G.2` pack publication asserts fusion or substitution across sources or across `Tradition` records (beyond mere “parallel divergent claims”), it **MUST** emit `GammaEpistSynthId` records per `G.2:Ext.GammaEpistSynthesis` (provenance union + explicit object alignment refs + assurance tuple refs), and it **MUST** keep penalties routed to `R_eff` only by delegation (`CC‑GCORE‑PEN‑1`).

7. **Publish teachable micro‑groundings.**
   Attach worked micro-examples to load-bearing claims, each tied to the exact source and edition, claim region, EntityOfConcern, comparison basis, intended use, and evidence carrier or A.10 evidence-provenance path.

8. **Apply gates and record repairs.**
   Apply that fixed HarvestPolicy basis and count its distinct units before comparing coverage with `FamilyCoverageFloorK` (and apply any optional diversity-by-distance gate under its own basis). Missing count semantics returns an unassessable result and the exact missing basis, not an instruction to search more. If a defined gate fails, the pack **MUST**:
   * record the failure and the repair iteration in `FlowRecord` and `CorpusLedger`,
   * pin the updated `HarvestPolicyRef` / criteria ids (if changed),
   * iterate the loop rather than silently weakening the gate.

9. **Emit hand‑off manifests and export views.**
   Produce explicit manifests to:

   * `G.3` (CHR authoring),
   * `G.4` (CAL authoring),
   * `G.5` (registry/dispatch),

   so that downstream work can cite pack components by id rather than re‑authoring them. Each relied-on coverage result carries the same `CoverageJudgementRef` and its policy basis; a downstream method-selection use cannot treat a combined method/generator count as a method-only count.
   The pack **MUST** also export `SoTA_Set@CG‑Frame` and `SoTAPaletteDescription` as the default downstream consumption surfaces (ids pinned).

#### G.2:4.4 - Interfaces (minimal I/O Standard)

| Interface         | Consumes                                                      | Produces                                                                    |
| ----------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **G.2-1 Harvest** | exact CG-frame (the declared framing episteme) identified by `CGFrameId`, initial `Tradition[]`, source edition and claim-region boundary, EntityOfConcern, comparison basis, receiving use, `HarvestPolicyRef` whenever coverage is judged | `SoTA Synthesis Pack@CG-Frame` (G.2a-G.2l) |
| **G.2‑2 Extend**  | existing Pack + new sources/anchors + updated policy pins     | updated Pack + RSCR‑relevant trigger emissions (canonical kinds)            |
| **G.2‑3 HandOff** | Pack                                                          | `CHR‑handoff` (to G.3), `CAL‑handoff` (to G.4), `Registry‑handoff` (to G.5) |

*Note:* Orchestration of re‑runs is governed by `G.11`; this pattern only defines what a conforming (re)harvest produces and what pins it must expose.

#### G.2:4.5 - Extensions (pattern‑scoped; non‑core)

`Extensions` are pattern‑scoped annexes. They do not introduce Part‑G‑wide norms; they declare the additional pins required when those semantics are active and cite the corresponding governing patterns.

###### G.2:4.5.1 - GPatternExtension: GammaEpistSynthesis

**PatternScopeId:** `G.2:Ext.GammaEpistSynthesis`
**GPatternExtensionId:** `GammaEpistSynthesis`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.2`
**Uses:** `{G.Core, B.3, F.9, G.6}` *(penalty routing + trust/decay cues + bridges/CL + evidence path citation when used)*
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `GammaEpistSynthId[]` *(pack‑local ids of synthesis records; emitted iff fusion/substitution is asserted)*
* `EvidenceAnchorRef[]` *(provenance union; evidence carriers cited by A.10 evidence-provenance paths)*
* `BridgeMatrixId` and `BridgeCardId[]` *(explicit object alignment references when crossing is involved)*
* `CL/CL^plane` and `Φ/Ψ/Φ_plane policy-ids` when required by the cited crossing or actually used loss model *(semantics and penalties → `R_eff` remain governed by the cited definitions)*
* `PathId/PathSliceId?` *(only when citing via `G.6`)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange}`

**Notes (normative intent; duplication‑avoidant):**
* The auditable synthesis record identified by `GammaEpistSynthId` binds: (i) provenance union, (ii) explicit object alignment refs, (iii) assurance tuple refs (via their governing definitions) for each asserted fusion/substitution. A B.1.3 `Γ_epist^synth` application and its returned episteme remain separate from this record.
* This extension cites the `Γ‑fold`, `Φ`, and penalty rules through `G.Core` and exposes the pins needed for replay. When B.3/C.2.2 supplies no justified common numerical score or loss calculation, retain the separate support, actual mapping limitations and bounded assurance conclusion; a synthesis record does not supply the missing model.

###### G.2:4.5.2 - GPatternExtension: HarvestProtocols

**PatternScopeId:** `G.2:Ext.HarvestProtocols`
**GPatternExtensionId:** `HarvestProtocols`
**GPatternExtensionKind:** `Phase3Seed`
**GoverningPatternId:** `G.2`
**Uses:** `{B.3, A.10}` *(for freshness/decay and provenance anchors, when protocol requires them explicitly)*
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `HarvestPolicyRef` *(declares the chosen protocol family and its parameters)*
* `FlowRecordId` *(protocol‑specific profile id or rubric id may be attached here)*
* `InclusionCriteriaId` / `ScreeningRubricId` *(ids only; semantics remain local to the protocol family)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (extension discipline):**
* This extension binds a declared protocol profile to the pack’s `FlowRecord` without redefining evidence semantics.

###### G.2:4.5.3 - GPatternExtension: DHCAlignmentHooks

**PatternScopeId:** `G.2:Ext.DHCAlignmentHooks`
**GPatternExtensionId:** `DHCAlignmentHooks`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `C.21` *(DHC semantics are governed by C.21)*
**Uses:** `{C.21, G.6, G.7}` *(DHC series + evidence path citations + bridge/CL regimes when alignment density is claimed)*
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DHCMethodRef.edition`
* `WindowRef?` *(if the DHC series is windowed)*
* exact F.17 `SchemeSenseCell` refs used by the DHC comparison set (use `SenseCellAddressRef` where a durable address is needed; cite `UTSRowId[]` only for independently public ids)
* `UTSRowId[]?` *(only if a cited cell or series id is independently minted or evolved as a public id)*
* `PathId[]` / `PathSliceId[]` *(when alignment summaries cite evidence paths via G.6)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.TelemetryDelta}`

**Notes (extension discipline):**
* If DHC alignment summaries are emitted, this extension ensures the DHC method edition and the cited evidence paths are visible.
* AlignmentDensity uses C.21's Unit `obtaining_relations/100_compared_cells`: fix the exact compared F.17 cell set and count the exact obtaining directed F.9 relations, retaining each relation's orientation and admitted-use qualifier. Keep observed loss in its evidence account. A CL calibration label does not include or exclude a relation by itself. Any independently justified receiving-use filter must name its own policy and resulting population; it is not a C.21 CL threshold.
* For example, three obtaining directed relations in a fixed set of 100 compared cells give a density of 3 in that Unit. Changing a CL label while relation truth, population and admitted-use qualifier remain fixed leaves the density 3. A fourth calibration row labelled CL=2 with no obtaining relation adds nothing. If a use condition actually changes which relations qualify, restate that changed population before comparing densities.

###### G.2:4.5.4 - GPatternExtension: NQDAnnex

**PatternScopeId:** `G.2:Ext.NQDAnnex`
**GPatternExtensionId:** `NQDAnnex`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18` *(NQD-CAL semantics are governed by C.18; explore/exploit logging is governed by C.19 when used)*
**Uses:** `{C.18, C.19}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `InsertionPolicyRef` *(policy‑id/ref)*
* `EmitterPolicyRef` *(policy‑id/ref)*
* `TaskSignatureRef?` *(when QD mode is trait‑gated)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (extension discipline):**
* This extension only pins the required references for replayability; it does not redefine QD semantics, dominance, or acceptance rules.

###### G.2:4.5.5 - GPatternExtension: InteropForms

**PatternScopeId:** `G.2:Ext.InteropForms`
**GPatternExtensionId:** `InteropForms`
**GPatternExtensionKind:** `InteropSpecific`
**GoverningPatternId:** `G.13`
**Uses:** `{G.13}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ExternalIndexRef.edition`
* `ClaimMapperRef.edition`
* `MappingPolicyRef` *(policy‑id/ref)*
* `UTSRowId[]` *(for published external ids/aliases where relevant)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TokenizationOrNameChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`

**Notes (extension discipline):**
* Interop affects only representation and citation routes; it must not introduce alternate legality gates or acceptance semantics.

#### G.2:4.6 - Palette first

- `SoTAPaletteDescription` is one plurality-preserving palette.
- It is not by itself one `Front`, one `Archive`, or one `Shortlist`.
- When that palette's members are traditions, `TraditionPalette` is the reader-facing tradition-only palette head over the same palette declaration, not one second governing definition. For methods, hypotheses, or other members, keep `SoTAPaletteDescription` or `Palette + SubjectKind` explicit instead.
- Traditions remain in the palette until a later surface declares comparison, retention, or choice semantics explicitly.
- `TraditionFront` is one derived view over the declared palette under one declared `Q`; the `Q` basis stays pinned separately and the view does not rename `Tradition` or `SoTAPaletteDescription`.
- `TraditionArchive` is one derived retention view over that same palette under one declared reachability or coverage rule; that rule stays pinned separately and the view does not turn the palette into one archive by default.
- When one derived tradition view is shown, keep the base palette recoverable at the same time.
- When comparison or retention needs richer geometry or atlas language, treat that as support for the derivation rather than as the default meaning of the palette.
- A reader should be able to say both `this is the palette` and `this is the derived tradition view currently being shown` without collapsing those two objects.

#### G.2:4.7 - Optional atlas interpretation of a declared palette

Use `TraditionAtlasView` only when the reader needs several derived views or interpretive qualifiers together to understand a grouping, omission risk or comparison boundary. Otherwise use the palette and its declared front, archive or shortlist, or the thinner `DeclaredSubstrateInterpretiveView`. A naming-only question belongs to F.18.

`TraditionAtlasView` specializes `DeclaredSubstrateAtlasView` under A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW and retains that declaration by value: the base palette, active source set or result, `TypedSetViews` when several declared views are combined, the space/map references and interpretive qualifiers actually used, and the reason the thinner view is insufficient. Cite `SearchSpaceRef` or `OutcomeSpaceRef` for the corresponding declared spaces. Add `SpaceMetricRef`, `TransitionRelationRef` and `BridgeDistortionNote` only for the comparison, reachability, transition or cross-scale claim that needs them. An `OutcomeMapRef` identifies a mapping from the stated result into an outcome/effect space; it does not turn the palette or result into that space. Their formal claims retain their own governing definitions.

If the interpretation changes the base source-to-outcome relation or its distortion, reopen the substrate declaration. Different atlas views may use different spaces, metrics, relations or mathematical traditions; one view does not settle those choices for every other view.

### G.2:5 - Archetypal Grounding (System / Episteme)

| Template element   | `U.System` illustration                                                                                                                                                                                                                                                  | `U.Episteme` illustration                                                                                                                                                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tell** | A safety engineering team needs to choose a control stack across robust-control, learning-based, and formal-verification lineages. It identifies the exact CG-frame (the declared framing episteme), vehicle and operating-envelope EntityOfConcern, source editions, claim regions, test or comparison basis, evidence anchors, and intended decision use. | A research group synthesizes SoTA on decision quality across named causal, evidential, bounded-rationality, and active-inference lineages, keeping each source edition, local claim, evidence norm, comparison basis, and intended research use explicit. |
| **Show (failure)** | The team merges source-local terms, treats incompatible test protocols and populations as comparable, and collapses partially ordered trade-offs into one unqualified score. A later safety review cannot recover which source, claim region, basis, or evidence supported the choice. | The group publishes one “best” metric and retrofits definitions to it. Conflicting claims cannot be traced because source editions, evidence anchors, comparison bases, and any actual cross-source relation were never made explicit. |
| **Show (repair)** | Keep parallel Claim Sheets with exact sources, editions, claim regions, EntitiesOfConcern, comparison bases, and evidence. Cite an F.9 Bridge and loss only for an actual relation. Authors of CHR, CAL, and selection methods can then use the citable claims without attributing authority to a card. | Preserve plural claims, represent indicators as families or variants, and expose freshness and evidence. Any justified alignment names its exact cells and obtaining relation; the card or matrix merely represents that result. |

#### G.2:5.1 - Count one pack under a declared basis

Consider this illustrative control-stack pack, extending the System case above. These are stipulated source entries for a counting example, not a finding that a real corpus has adequate breadth.

| Entry and distinct claim region | Lineage | Declared family unit |
| --- | --- | --- |
| e1: robust controller's operating-envelope claim | robust control | method M-R |
| e2: that family's distinct disturbance-rejection claim | robust control | method M-R |
| e3: learned controller's adaptation claim | learning-based control | method M-L |
| e4: scenario generator's counterexample-generation claim | formal verification | generator G-S |

For the question “which control-method families can be selected?”, policy P-method counts method families only and equates entries exactly when they name the same declared method-family unit. The classes are {e1,e2} and {e3}: count 2, below k=3. Additional cards for e1 or citations for M-R leave the count at 2.

For the different question “which method and scenario-generator families can support building and evaluating this control stack?”, policy P-combined includes the three declared units M-R, M-L and G-S. Its overlap rule merges repeated references to one unit; these three units are stipulated distinct and G-S is not also M-R or M-L. Count 3 meets k=3 for that receiving purpose. This is not a passing method-only judgement and cannot be substituted after P-method fails. If one generator also qualified as a counted method, the overlap rule would have to resolve it before the count.

Four claim regions remain four material entries. The example independently has three lineages, so its two-lineage and three-material-entry pluralism duties pass under the stated facts in both policies. With no counted-family basis, family coverage is unassessable even though that pluralism result remains available. A justified k=2 override for P-method changes its threshold result while leaving its count at 2 and those independent duties unchanged.

G.1 M2 and the G.3–G.5 consumers cite the chosen pack judgement with its purpose and policy; they do not reconstruct a more convenient count from the cards.

### G.2:6 - Bias-Annotation (informative)

Bias lenses: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: harvesting and synthesis for a `CG‑Frame`.

* **Selection bias (Gov/Onto).** Any harvesting protocol can over‑represent certain venues, languages, or evidence styles.
  *Mitigation:* pluralism floor + explicit `CorpusLedger` + explicit protocol pins.

* **Consolidation bias (Onto/Epist).** Pressure to “merge” lineages can erase incompatible commitments.
  *Mitigation:* keep Claim Sheets disjoint by default; require explicit alignment proof for fusion; preserve loss notes.

* **Recency bias (Prag).** Overweighting newest papers can hide durable backbone results; underweighting them misses SoTA drift.
  *Mitigation:* publish freshness windows and make them RSCR‑relevant.

* **Didactic bias (Did).** Micro‑examples can steer interpretation toward familiar domains.
  *Mitigation:* require heterogeneous substrates and explicit A.10 anchors.

### G.2:7 - Conformance Checklist (normative) — **CC‑G2**

| ConformanceId             | Requirement                                                                                                                                                                                                                                                                                                                                        | Purpose / Notes                                                                     |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **CC‑G2‑CoreRef**         | A conforming `G.2` artefact **MUST** satisfy the **effective** core obligations declared by the `GCoreLinkageManifest` in `G.2:4.1` (per `G.Core` Expansion rule).                                                                                                                                                                                 | Keeps core invariants governed by `G.Core`. |
| **CC-G2-Pluralism-1** | A conforming pack MUST include at least two `Tradition` lineages and at least three materially distinct entries, each identified by its source edition and claim region, with its EntityOfConcern, evidence norm, and comparison limits visible. | Prevents a single lineage or one renamed source cut from masquerading as synthesis. |
| **CC‑G2‑Ledger‑1**        | A conforming pack **MUST** include `G.2a CorpusLedger` with inclusion/triage status and explicit rationale hooks per entry.                                                                                                                                                                                                                        | Makes discovery/triage auditable.                                                   |
| **CC‑G2‑FlowRecord‑1**    | A conforming pack **MUST** include `G.2h FlowRecord` that traces identification → screening → eligibility → included at a minimum granularity sufficient to reproduce the corpus boundary.                                                                                                                                                         | Prevents “mystery inclusion” and supports refresh.                                  |
| **CC-G2-ClaimSheets-1** | For each included `Tradition`, the pack MUST include a `ClaimSheetId` naming exact sources and editions, claim regions, effective schemes where meaning matters, EntitiesOfConcern, comparison bases, evidence anchors, freshness notes, and intended use; it MUST NOT fuse cross-`Tradition` claims by default. | Keeps plurality and provenance explicit without a Context container. |
| **CC‑G2‑Palette‑1**       | A conforming pack **MUST** export `SoTA_Set@CG‑Frame` and `SoTAPaletteDescription` as citable views (via `SoTA_SetId`, `SoTAPaletteDescriptionId`) and ensure both are reconstructible from pack components by id (no hidden extra structure).                                                                                                      | Prevents downstream scraping of prose; keeps “M2 output” explicit.                  |
| **CC‑G2‑Palette‑2**       | If the pack exports one derived tradition view such as `TraditionFront` or `TraditionArchive`, it **MUST** keep `SoTAPaletteDescription` explicit as the default base palette, keep that derivation recoverable, and cite the declared `Q` or reachability/coverage rule that disciplined that view. Derived tradition views **MUST NOT** silently replace the palette's default meaning. | Keeps non-default tradition views recoverable without redefining palette-first semantics. |
| **CC‑G2‑AtlasInterpretation‑1** | If the pack exports `TraditionAtlasView`, it MUST satisfy §4.7 and the cited A.19 interpretive-view declaration by value, including the reason a thinner view is insufficient. | Keeps atlas use conditional and its interpretation recoverable. |
| **CC‑G2‑entityOfConcernMap‑1** | A conforming pack **MUST** include `G.2g entityOfConcern Map`, mapping (at minimum) each load‑bearing claim family and each minted/evolved public id to `entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩`, and citing the relevant `ClaimSheetId` and evidence anchors (A.10 and/or G.6 paths when used).                                         | Keeps plane/holon boundaries explicit and citable.                                  |
| **CC‑G2‑Alignment‑1** | Cross‑`Tradition` consolidation **SHALL** present either disjoint parallel claims with explicit divergence or an explicitly justified alignment proof. Reuse **MUST** cite the exact basis for every sense, kind or plane relation actually used and disclose its preservation and losses. Bundle/gate anchors **MUST** be supplied when an E.18 flow crossing or A.21 gate independently requires them, per `CC‑GCORE‑CROSS‑1`. | A kind correspondence alone requires neither an F.9 sense Bridge nor a flow-crossing bundle. |
| **CC‑G2‑GammaSynth‑1**    | If the pack asserts **fusion or substitution** across sources or across `Tradition` records (not merely “parallel divergent claims”), it **MUST** emit `GammaEpistSynthId` records satisfying `G.2:Ext.GammaEpistSynthesis` (provenance union + explicit alignment refs + assurance tuple refs). If no fusion or substitution is asserted, the pack **SHALL** state so explicitly. | Keeps the synthesis record (alias: `G.2‑F`) citable under its governing definitions. |
| **CC‑G2‑Inventory‑1**     | A conforming pack **MUST** include `G.2c OperatorAndObjectInventory`, sufficient for downstream CHR/CAL authoring to begin without re‑harvesting terms.                                                                                                                                                                                            | Ensures the pack is actionable.                                                     |
| **CC‑G2‑Inventory‑2**     | `G.2c OperatorAndObjectInventory` entries **MUST** be treated as **stubs** for downstream authoring: they **MUST NOT** embed acceptance thresholds or claim legality decisions locally. If an entry is not a citation of an already governed CHR/CAL artefact, it **MUST** be explicitly marked as `stub` (typing/lawfulness `TBD`) and **MUST NOT** be used as if lawful. Legality/threshold semantics are governed by `G.3` for CHR and `G.4` for CAL via explicit ids/pins. | Prevents “shadow CHR/CAL” and preserves lawfulness discipline without redefining it locally. |
| **CC‑G2‑MeasurementLawful‑1** | If any inventory entry is presented as **non‑stub** (i.e., already lawful/typed), the pack **MUST** cite the governing lawfulness discipline (e.g., `A.17–A.19/C.16` as applicable) and provide the minimal evidence anchors needed to justify that typing claim.                                                                                      | Prevents “quietly lawful” measurement claims inside the harvester pack.             |
| **CC-G2-MicroExamples-1** | For every load-bearing claim family, a conforming pack MUST include at least two worked micro-examples on heterogeneous substrates. Each names the source and edition, claim region, EntityOfConcern, comparison basis, and intended use; cites its evidence carrier or A.10 evidence-provenance path; and gives an applicable assurance tag. | Makes the synthesis teachable and inspectable; the example form supplies no meaning or authority. |
| **CC‑G2‑UTS‑1**           | If the pack proposes or evolves any public ids, it **MUST** publish UTS proposals *(Name Cards + MDS where applicable)* and cite them via `UTSRowId[]`, satisfying `CC‑GCORE‑UTS‑1` (delegation).                                                                                                                                               | Keeps naming and evolution disciplined.                                             |
| **CC‑G2‑Families‑1**      | SoS indicators and candidate evaluation constructs **SHALL** be represented as **families/variants** (windows/constraints/assumptions) **with explicit Acceptance branch structure per variant** (branch ids/labels only), not as single unqualified scalars; any scalar summary **MAY** be included only as report‑only unless explicitly promoted by governing patterns. *(Set-return discipline is delegated to `CC‑GCORE‑SET‑1`.)* | Prevents covert scalarization and keeps acceptance governed by downstream patterns.                |
| **CC‑G2‑HandOff‑1**       | A conforming pack **MUST** emit hand‑off manifests to `G.3`, `G.4`, and `G.5` that cite pack components by id and identify which families/operators are intended for downstream formalisation or registry entry.                                                                                                                                   | Prevents downstream re‑authoring and drift.                                         |
| **CC‑G2‑CoverageGate‑1**  | The pack **MUST** declare `FamilyCoverageFloorK` and enforce it as a harvesting gate. It **MUST** either (i) specify `k` explicitly in an explicit `HarvestPolicyRef`, or (ii) use the pattern‑local default rule governed by `CC‑G2‑CoverageGate‑1`. *Default threshold (pattern-local):* `k=3`. In both threshold branches, an explicit `HarvestPolicyRef` **MUST** fix the receiving question, population/scope, grouping, same-family equivalence and overlap rule before counting. The pack judgement cites that basis, its distinct units and result; all consumers reuse it. Missing basis returns unassessable. Duplicate references add zero, and a threshold override changes neither units nor independent pluralism duties. The independent CC-G2-Pluralism-1 duties remain. If the defined gate fails, the pack **MUST** (a) record the repair iteration in `FlowRecord`, and (b) broaden the search radius (new venues/corpora/contexts/traditions) rather than silently weakening the gate; if an exploration policy is used for this broadening, it **MUST** be pinned as a policy id/ref. | Makes “coverage floor” explicit and prevents “silent narrowing” under failure.      |
| **CC‑G2‑DistanceGate‑1**  | If a diversity‑by‑distance gate is used, the pack **MUST** pin `DistanceDefRef.edition` and the declared threshold (δ), and treat edits as RSCR‑relevant per `CC‑GCORE‑TRIG‑*` (delegation). If no such gate is used, the pack **SHALL** explicitly state that it is not used.                                                                     | Avoids implicit distance defaults and improves refreshability.                      |
| **CC‑G2‑RSCR‑1**          | A conforming pack **MUST** emit canonical `RSCRTriggerKindId` causes (not free text) for edits to evidence surfaces, name/tokenization surfaces (e.g., UTS proposals/aliases), crossings, planes, edition pins, and harvesting policy pins (`HarvestPolicyRef`), per `CC‑GCORE‑TRIG‑1…TRIG‑4` (delegation).                                                                                      | Keeps refresh reason codes stable and typed.                                        |
| **CC‑G2‑Ext‑GammaEpist‑1** | If `G.2:Ext.GammaEpistSynthesis` is used (i.e., any fusion/substitution is asserted), the pack **SHALL** expose the required pins listed in that extension and **SHALL NOT** redefine `Γ‑fold/Φ/penalty` semantics locally (cite governing definitions by delegation).                                                                                       | Keeps synthesis auditable without creating shadow specs.                            |
| **CC‑G2‑Ext‑HarvestProtocols‑1** | If `G.2:Ext.HarvestProtocols` is used, the pack **SHALL** expose the required pins/criteria ids listed in that extension and **SHALL NOT** redefine evidence/quality semantics outside the declared protocol profile.                                                                                                                            | Keeps protocol variation explicit and separately citable.                           |
| **CC-G2-Ext-DHC-1** | If `G.2:Ext.DHCAlignmentHooks` is used, expose the DHC method edition, exact compared F.17 cell population, counted obtaining directed F.9 relation refs with their orientation and admitted-use qualifiers, evidence paths, and C.21 Unit `obtaining_relations/100_compared_cells`. CL labels alone neither change that population nor impose a counting threshold. Cite any separate receiving-use policy under its own authority. | Keeps the quantity identical to the C.21/G.7 definition. |
| **CC‑G2‑Ext‑NQD‑1**       | If `G.2:Ext.NQDAnnex` is used, the pack **SHALL** expose the required pins/editions/policies listed in that extension and **SHALL NOT** redefine QD semantics locally.                                                                                                                                                                             | Keeps QD/OEE extension pins replayable and non‑shadowing.                          |
| **CC‑G2‑Ext‑Interop‑1**   | If `G.2:Ext.InteropForms` is used, the pack **SHALL** expose the required interop pins and **SHALL NOT** introduce alternative legality/acceptance semantics.                                                                                                                                                                                      | Prevents “foreign gate” shadowing.                                                  |

### G.2:8 - Common Anti‑Patterns and How to Avoid Them

* **AP‑G2‑1: “One true SoTA score.”**
  **Avoid:** selecting a single unqualified scalar metric as “the” SoTA.
  **Do instead:** represent evaluation constructs as families/variants; keep partial orders set‑returning (delegated).

* **AP‑G2‑2: Fusion without explicit alignment proof.**
  **Avoid:** merging rival `Tradition` claims into one statement “by common sense.”
  **Do instead:** preserve parallel Claim Sheets; if consolidation is required, publish explicit alignment proof or keep a divergence record.

* **AP‑G2‑3: Hidden protocol drift.**
  **Avoid:** changing the harvesting protocol (inclusion criteria, windowing, screening rubric) without pins.
  **Do instead:** pin harvesting policy/profile ids and treat changes as RSCR‑relevant.

* **AP‑G2‑4: Unanchored pedagogy.**
  **Avoid:** micro‑examples without carriers (they become folklore).
  **Do instead:** bind micro‑examples to A.10 anchors and declare `entityOfConcern`.

* **AP‑G2‑5: Atlas by default.**
  **Avoid:** writing as if every tradition comparison or NQD/OEE note needs `TraditionAtlasView`, or as if atlas wording renames the palette itself.
  **Do instead:** keep the base palette and derived front, archive, or shortlist explicit; use atlas form only when several declared views or interpretive qualifiers must be held together, and prefer thinner `DeclaredSubstrateInterpretiveView` when that is enough.

### G.2:9 - Consequences

* **Positive:** Downstream CHR/CAL/dispatch work becomes faster and less ambiguous because the pack is citable and structured.
* **Positive:** Plurality is preserved while still enabling disciplined comparability through explicit crossings.
* **Positive:** Refresh becomes tractable because pins and typed causes exist.
* **Negative:** Adds authoring overhead (ledger, flow record, micro‑examples, explicit pins).
* **Negative:** Requires governance discipline to prevent the pack from becoming an uncontrolled “everything bucket”.

### G.2:10 - Rationale

SoTA synthesis is a bottleneck for new `CG‑Frame` work: without a disciplined harvest, downstream formalization (CHR/CAL) and operational selection (G.5) either (i) inherit hidden semantic collisions, or (ii) re‑invent incompatible “mini‑standards.”
`G.2` resolves this by treating SoTA work as a **publishable kit**: explicit plurality, explicit crossings, explicit evidence anchors, and explicit hand‑offs.

### G.2:11 - SoTA-Echoing — keep a reusable synthesis current without restarting it

**Practice question.** How should several downstream authors reuse a synthesis when new sources can change a consequential, unsettled comparison? The selected line keeps a question-bound source ledger, separable claims and explicit update causes; a living protocol is chosen when continuing evidence surveillance is worth its cost. A serious alternative is a well-reported static review with an explicit search date and a separately commissioned update. That alternative is sufficient for a stable question or a one-time decision and avoids maintaining a continuing review service.

The [Cochrane Handbook, Chapter 22, §§22.2.3–4](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-22) supplies the conditional living-review line and its resource trade-off: priority, uncertainty and likely new evidence can justify frequent updates, while additional searching needs resources. **Adapt** this conditional choice in `HarvestProtocols`; declare the search/update policy rather than treating every G.2 pack as perpetually living. The clinical-review guidance does not establish coverage or evidence adequacy for an arbitrary engineering CG-frame.

The [PRISMA 2020 reporting guidance](https://www.prisma-statement.org/prisma-2020) supplies the substantive static-review comparator and a shared reporting basis. Its [explanation of study selection](https://www.bmj.com/content/372/bmj.n160) distinguishes records, reports and included studies. **Adapt** the distinction to `CorpusLedger`, `FlowRecord` and the declared family units in §4.3: multiple source entries can concern one counted family. **Reject** treating a publication count or a completed flow diagram as proof of adequate family coverage. G.2's k threshold, lineage duties and FPF alignment rules remain local decisions, not PRISMA requirements.

The [2024 PRISMA-LSR extension](https://www.bmj.com/content/387/bmj-2024-079183) supplies the more specific reporting line for an actually selected living protocol: justify that mode, identify the version's trigger and changes, and plan when to retire it. **Adapt** that distinction to the policy pins, change causes and downstream handoffs in §4.3 and `G.2-2 Extend`; G.11 governs refresh orchestration. Source reporting guidance does not supply an automatic update schedule or establish that a newly added claim is sound.

The control-stack case in §5.1 makes the improvement concrete. If e1's operating-envelope claim is revised, the existing ledger identifies M-R and its consumers; re-examine that claim and the comparisons that depend on it. The new report does not add a family. The method-only count remains 2 until a distinct admitted method-family unit is found. A static review can also be updated correctly, but each separate consumer must recover the changed basis unless a shared update is published. For the same new source and receiving question, the selected pack reuses existing screening and claim relations; its added maintenance burden is justified only while repeated shared use and consequential change make that work useful.

Reopen the choice of protocol when the evidence rate, decision importance, uncertainty or maintenance resources change; retire living surveillance when its reason no longer holds. Reopen an individual synthesis when a new source changes a relied-on claim, coverage judgement or alignment. A source with a new date but no relevant content change does not by itself warrant reconstructing every downstream conclusion.

### G.2:12 - Relations

* **Builds on:**

  * `G.Core` (core invariants, typed RSCR causes, Default Governing Definition Index)
  * `E.8` (pattern template discipline)
  * `E.10` (lexical/ontological rules; strict distinction; kind‑suffix discipline)
  * `E.19` (conformance discipline)
  * `A.10` (evidence-provenance paths and cited source/carrier anchors)
  * `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` (generic interpretive-view and atlas discipline when `TraditionAtlasView` is used)
  * `A.6.P` (space/view/publication precision restoration when palette/support claims collapse)
  * `B.3` (trust, freshness/decay as cited governing patterns)
  * `F.9` (bridges and CL as cited governing patterns)
  * `F.17` (UTS publication discipline; via delegation)
  * `G.0` (CG‑Spec legality gate; cited when legality surfaces are referenced)
  * `G.6` (EvidenceGraph / path citation surfaces when used)

* **Used by:**

  * `G.1` (generator chassis consumes harvested SoTA sets)
  * `G.3` (CHR authoring consumes operator/object inventory and claim sheets)
  * `G.4` (CAL authoring consumes operator stubs, acceptance branch scaffolding)
  * `G.5` (registry/dispatch consumes MethodFamily/GeneratorFamily cards)
  * `G.10` (shipping cites the pack as payload)
  * `G.11` (refresh orchestration can re‑invoke harvest via typed causes)

* **Relates to:**

  * `G.13` (interop surfaces when external indices are used)
  * `F.18` (naming-side support wording when the question is label choice rather than synthesis geometry)

### G.2:End

---
