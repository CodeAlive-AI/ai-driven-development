## G.13 - External Interop Hooks for SoTA Discipline Packs (conceptual)

**Use this when.** A SoTA author or downstream consumer needs repeatable mappings from an external scholarly source into FPF inputs, with the source snapshot, transformation and receiving use recoverable. Start by naming that source and the input needed by the receiving operation. A sufficient direct source citation needs no interop kit.

Use :4.3 to establish the mapping from source meanings and actual records, then publish its inputs, outputs, conditions and revisions. Provider-specific ingestion, embedding and entity-resolution methods retain their own grounds; the extensions below identify their required wiring.


**Status.** Stable

**Normativity.** Normative when a `G.13` surface is authored, emitted or consumed. Informative otherwise.



### G.13:1 - Problem frame

External scholarly indexes and discipline repositories supply inputs for SoTA authoring. Examples include concept or dataset registries, paper/claim graphs, taxonomy stores and science-of-science indicator feeds. Their values must retain their source meaning and limits when used in FPF characterization, comparison, selection or reporting.

If the mapping assumptions are unstated, a receiver can miss an edition change or a cross-plane or cross-context use. A receiver may also take an external signal as the governing specification for the receiving claim.

`G.13` provides **registration, alignment and telemetry hooks** for whichever Part-G use needs those sources.

A source may supply G.2 synthesis, G.3 characterization, G.5 selection, G.9 comparison or G.12 reporting inputs. G.10 carries an interop surface when shipping is needed; G.11 reconsiders dependent uses after a relevant change. Choose the uses the receiving task requires.

### G.13:2 - Problem

External sources publish **claim‑adjacent signals** (citations, concept graphs, “task/method” tags, replication links, dataset usage, disruption‑style indicators, benchmark metadata). These signals can support audit and the generation of new inputs, for example by helping to build a palette, explore a declared set result or discover a candidate bridge. The mapping can fail in the following ways:

* **CN/CG spec-ref leakage.** A receiver treats external numeric signals as lawful scores without showing how they are bound to the applicable CHR/CAL/CG definitions.
* **Implicit crossings.** An opaque transformation hides the actual correspondence, its receiving-use grounds or the bundle anchors required by a real flow crossing or gate.
* **Edition drift + refresh brittleness.** Snapshots change, schemas drift, indicator definitions get revised; without edition‑pinned interop surfaces and typed trigger causes, parity and dashboard stability degrade.
* **Evidence disconnect.** A derived feature without recoverable source and transformation grounds cannot be checked or repaired in the receiving use.
* **Format‑as‑norm.** A convenient serialisation (KG export, JSON schema, RO‑Crate, etc.) is taken as the specification, undermining notation independence.

### G.13:3 - Forces

| Force                           | Tension                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Notation independence**       | Useful serialisations vs the requirement that conformance is judged on **conceptual** surfaces.        |
| **Pluralism vs parity**         | Diverse scholarly traditions and indexes vs lawful, edition‑aware comparability and reproducibility.   |
| **Interop as generation input** | Interop should speed SoTA authoring. Using it only to illustrate an audit report misses that use.                                |
| **Planes & bridges**            | Cross‑plane/context reuse must remain explicit and auditable rather than implicit in “aligners”.       |
| **Telemetry vs dominance**      | External telemetry should inform exploration and refresh without silently changing selector semantics. |
| **Operational drift**           | Source editions change; typed causes and payload pins must identify the affected inputs and receiving uses.  |

### G.13:4 - Solution — Conceptual interop kit: registered sources, alignment cards, feature derivations, and RSCR‑wired telemetry

#### G.13:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core`.

**GCoreLinkageManifest (normative).**
*(Canonical form, Nil‑elision, and Expansion rule are defined in `G.Core`.)*

```text
GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
    GCoreConformanceProfileId.PartG.ShippingBoundary
  },
  RSCRTriggerSetIds := {GCoreTriggerSetId.SoTAHarvestSynthesis},
  RSCRTriggerKindIds := {RSCRTriggerKindId.BaselineBindingEdit},   // delta: planned‑baseline linkage edits can be interop‑relevant

  CorePinSetIds := {
    GCorePinSetId.PartG.AuthoringMinimal,
    GCorePinSetId.PartG.CrossingVisibilityPins
  },

  CorePinsRequired := {
    // Interop pins (G.13‑specific; avoid duplicating `GCorePinSetId.PartG.CrossingVisibilityPins`)
    ExternalIndexRef.edition,
    ClaimMapperRef.edition?,
    MappingPolicyRef?,
    PlaneMapRef.edition?,
    ScaleEmbeddingSpecRef.edition?,

    EvidenceGraphId?,
    InteropSurfaceId?
  },

  DefaultsConsumed := {DefaultId.PortfolioMode, DefaultId.DominanceRegime}
⟩
```

**Payload‑pin note (informative).** When emitting RSCR triggers for interop‑driven changes, payload pins should include the edited edition/policy identifiers, the impacted scope, and the applicable crossing‑visibility pins (per `GCorePinSetId.PartG.CrossingVisibilityPins`) when crossings/UTS/paths are involved.

#### G.13:4.2 - Interop kit objects & surfaces (pattern-governed; notation‑independent)

All objects below are **conceptual**. Any concrete serialisation belongs to Annex/Interop or tooling notes and is not normative for Part‑G conformance.

* **`ExternalIndexCard@Context`** — registration of an external source and its snapshot.

  **Shape (conceptual):**
  `⟨ ExternalIndexId, ProviderName?, ExternalIndexType, CoverageScope, Licence?, ExternalEdition, FreshnessWindow?, entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩, Notes? ⟩`

  **Intent.** Register the provider snapshot as `ExternalEdition` on a stable, citable source card. Downstream artefacts cite the card edition through `ExternalIndexRef.edition`; they do not copy the provider snapshot id into other cards.

* **`ClaimMapperCard@Context`** — a declaration of the recipe whose application maps an external source into FPF-native inputs.

  **Shape (conceptual):**
  `⟨ MapperId, ExternalIndexId, MappingPolicyRef, Targets{ClaimSheet|BridgeHints|SoSFeatureSet|UTSProposals}, PlaneMapRef?, ScaleEmbeddingSpecRef?, EvidenceGraphId?, CSLCProofStubs? ⟩`

  **Notes.**

  * The mapper cites the governing definitions (`A.19`, `G.0`, `G.3`, `G.4`) and publishes the pins needed for audit and refresh. It supplies no separate legality gate.
  * When cross-plane or cross-context reuse is implicated, alignment outputs must cite the actual relation and the receiving-use and reliance grounds required by its governor. Carry bundle or gate anchors when an independently applicable `E.18` flow crossing or `A.21` gate consumes the alignment, as required by `CC‑GCORE‑CROSS‑1`.
  * Avoid “edition echo”: downstream artefacts cite `ExternalIndexRef.edition` and `ClaimMapperRef.edition` (and optional `PlaneMapRef.edition` / `ScaleEmbeddingSpecRef.edition`) rather than copying snapshot ids/editions as free fields.

* **`SoSFeatureTransform@Context`** — declares how external signals become **CHR‑typed** SoS features (for DHC/dashboard usage and/or SoS‑LOG rule evaluation).

  **Shape (conceptual):**
  `⟨ SoSFeatureTransformId, Inputs{ClaimSheetId[] | ExternalSignalsRef}, SoSFeatureSetId, FeatureTypingRefs{CharacteristicId/ScaleId/CoordinateId}, ReferencePlane, EvidenceGraphId?, PathSliceId[]?, ProofHooks? ⟩`

  **Notes.**

  * The derivation records **typing + provenance**; comparator and legality definitions remain with the cited governing patterns. When features are used as DHC measurements, establish or reuse C.16 measurement results. Make the active C.21 `DHCReplayBasis` recoverable for every persisted, compared, aggregated, or published coordinate.

* **`ScaleEmbeddingSpec@Context`** — optional constraints for representation/space alignment used inside an alignment recipe.

  **Shape (conceptual):**
  `⟨ ScaleEmbeddingSpecId, IntendedUse, AllowedTransformFamily, RequiredPins{NormalizationMethodRef.edition?}, ProhibitedCoercions ⟩`

  **Design intent.** State the constraints and pin the edition for each representation alignment. If the transformation introduces a new scale, establish its lawfulness under the applicable scale rules.

  **LEX/UTS note (informative).** `ScaleEmbeddingSpec` is a LEX head. When you mint a public id for one, publish its UTS row under F.17 with the Tech designation and any Plain designation needed for the stated didactic use.

* **`IndexTelemetryPin`** — an emitted refresh input that makes interop changes RSCR‑visible.

  **Shape (conceptual; RSCR‑typed):**
  `⟨ triggerKindId: RSCRTriggerKindId, scope: PathSliceId[] | PathId[] | PatternScopeId, payloadPins{ExternalIndexId, ExternalIndexRef.edition, ClaimMapperRef.edition?, MappingPolicyRef?, PlaneMapRef.edition?, ScaleEmbeddingSpecRef.edition?, PathId[]?, PathSliceId[]?, UTSRowId[]?, …} ⟩`

  **Publication.** Emitted to `G.11` as refresh input; recorded with canonical `RSCRTriggerKindId` causes.

* **`InteropSurface@Context`** — a selector-facing or dashboard-facing summary of what interop publications and records exist and how they are pinned.

  **Shape (conceptual):**
  `⟨ InteropSurfaceId, ExternalIndexId, ExternalIndexRef.edition, MapperId?, ClaimMapperRef.edition?, MappingPolicyRef?, SoSFeatureSetId?, EvidenceGraphId?, PathSliceId[]?, PlaneMapRef.edition?, ScaleEmbeddingSpecRef.edition?, UTSRowId[] ⟩`

  **Publication.** Published to UTS with twin labels as applicable.

#### G.13:4.3 - Use external sources to construct the needed input

Start with the input required by the receiving method and records from the external source. Reuse an adequate mapping recipe. To construct or revise one, establish the transformation and its limits before publishing its card and routing its outputs.

##### G.13:4.3.1 - Construct and check the mapping

1. **Recover the required output meaning.** Read the receiving operation’s input definition and conditions. For a G.2 ClaimSheet, this includes the claim, its subject, scope and source support; for a CHR feature, the subject, characteristic, scale, units and observation basis come from G.3/C.16. For a Bridge hint, preserve the two local meanings and the proposed relation for F.9 to examine. Select only the outputs needed by the receiving question.
2. **Recover what the available source fields denote.** Inspect actual records together with the provider’s definitions for that edition: the counted or described object, population, inclusion rules, units, dates/windows, missing-value conventions and identifiers. Follow a record’s citation to the underlying source when its metadata does not contain the claim or conditions needed. Use the name to locate the field. Its definition and examples establish what a value represents. If the definition is unavailable, ask the provider or obtain the specified source passage before using the ambiguous field for that output.
3. **Connect each required output to its basis.** Select the source passage or field that supplies the output, or define the operation that derives it. Direct copying requires compatible meanings. A count requires the population, inclusion predicate and identity/equivalence rule; a unit conversion requires a lawful scale conversion; a claim extraction retains the source’s subject, conditions and contrary evidence under G.2. For a semantic correspondence use F.9’s relation construction and its separate receiving-use test. For a measurement use C.16’s measurement model and G.3’s lawful operations. If those methods and the available domain methods leave a transformation unspecified, identify what is missing and the source or competent supplier needed to construct it.
4. **Apply the recipe to real records.** Work through at least one representative record to the required result and inspect a consequential variation, such as a duplicate identifier, an absent value, a changed time window or a different population definition. Choose the variation from the assumptions the recipe uses. Retain the source value and derivation sufficiently for the receiving use to check them. Missing or ambiguous values remain missing or ambiguous; they become zero, false or a negative claim only when the source meaning and derivation establish that result.
5. **Return the input or identify what prevents obtaining it.** A mapped result carries its source edition, applicable scope and transformation basis. A failed compatibility condition supports rejection of that mapping. An unresolved field definition, relation, measurement procedure or source claim prevents only the outputs that depend on it. Identify what source, observation or method construction could settle the gap and what can already be used. When the receiving contract requires a complete bundle, retain that unmet condition rather than treating a partial mapping as the bundle.

**Worked mapping.** Suppose a review needs the number of distinct research articles in a named collection published during 2025, and source-grounded ClaimSheets about their methods. The available index supplies records with `work_id`, `year`, `record_type`, a citation and an abstract. In this illustrative provider contract, `year` means first publication year, `work_id` identifies a work across duplicate records, and `record_type = research_article` is the relevant inclusion class.

The recipe filters the stated collection by year and class, groups qualifying records by `work_id`, and counts those groups. Three qualifying records with ids `w1, w1, w2` yield two works. The result retains that population and counting basis; use as a DHC measurement additionally establishes the C.16 result and C.21 replay basis.

For the ClaimSheets, the citation leads to the article text. The reviewer extracts the method claim with its tested population and conditions under G.2; an abstract that omits those conditions leaves an extraction gap to settle from the article. The count and metadata alone supply no performance claim.

If the provider instead defines `work_id` as a record identifier, the same three values no longer establish two distinct works: obtain an identity rule or source-level matching method before returning the work count.

If `year` means index ingestion year, the recipe must obtain publication dates to answer the original question. Changing the receiving question to the number of index records ingested in 2025 can make those fields sufficient for that different result.

##### G.13:4.3.2 - Publish and use the established recipe

1. **Register source editions.** Author `ExternalIndexCard@Context` for each external source snapshot mapped through this kit, including `ExternalEdition` and the `entityOfConcern` plane anchor.
2. **Author mapping recipes.** Create `ClaimMapperCard@Context` for the established transformation and its limits, identifying the produced artefacts and applicable policy/spec references. Include `PlaneMapRef` or `ScaleEmbeddingSpecRef` when the transformation uses them.
3. **Produce FPF-native inputs.** Apply the recipe and route its obtained outputs to the receiving operation, for example:

   * `G.2` harvesting (ClaimSheets / operator & object inventories / candidate bridge hints),
   * `G.3` CHR typing (when numeric signals are formalized as CHR characteristics/scales/coordinates),
   * `G.4` acceptance/threshold policies (when a downstream decision requires explicit CAL policy rather than telemetry),
   * `G.12` dashboards (when derived SoS features support DHC readings; measurement claims consume C.16 results with the C.21 replay basis required by their use).
4. **Use the resulting inputs under the receiving rules.** Open only the applicable branch:

   * When selection or a selector-facing declaration is needed, `G.5` consumes the applicable grounded inputs and returns its declared outcome: a set result, narrowed handoff, abstain or escalation.
   * When a reproducible parity report is needed, `G.9` consumes the pinned editions and windows under its comparison plan.
   * When shipping is needed, `G.10` may include interop surfaces as cited publications or records.
5. **Emit telemetry and refresh causes.** On any change in external editions, alignment policies, plane maps, or embedding specs, emit:

   * a canonical `RSCRTriggerKindId` (per `G.Core`),
   * the affected scope (`PathSliceId[]`, `PathId[]` or `PatternScopeId`),
   * payload pins (editions, policies and UTS rows).

   With these pins, `G.11` can identify dependent uses and decide whether their changed basis calls for further work.

#### G.13:4.4 - Interfaces — minimal I/O standard (conceptual; kit‑only)

| ID   | Interface   | Consumes  | Produces   |
| ---- | ----------- | --------- | ---------- |
| **G.13‑1 `Register_ExternalIndex`**  | Register `ExternalIndexCard@Context` | Provider metadata, scope, **ExternalEdition**, freshness, entityOfConcern anchor   | `ExternalIndexCard@Context` (+ UTS row when published)   |
| **G.13‑2 `Map_ClaimsToFPF`**   | Apply `ClaimMapperCard@Context`   | `ExternalIndexCard@Context`, `MappingPolicyRef`, optional `PlaneMapRef`/`ScaleEmbeddingSpecRef`, optional EvidenceGraph hooks | `ClaimSheet@Context`, `BridgeHints`, optional `SoSFeatureSet@Context`, optional UTS proposals |
| **G.13‑3 `Derive_SoSFeatures`**  | Produce CHR‑typed SoS features  | ClaimSheets / external signals refs, CHR typing refs, legality proof hooks | `SoSFeatureSet@Context` (CHR‑typed; provenance pinned)   |
| **G.13‑4 `Publish_InteropSurface`**  | Publish interop summary | outputs of G.13‑2/‑3, UTS refs | `InteropSurface@Context` (+ UTS rows/twins) |
| **G.13‑5 `Emit_IndexTelemetryPin`** | Emit refresh input  | edition/policy changes + scope + payload pins  | telemetry to `G.11` (typed causes + payload pins)   |
| **G.13‑6 `Wire_To_SoTA_Pack`** | Provide shipping hook  | `InteropSurface@Context` + citations to upstream artefacts  | `G.10` pack hooks (as cited payload; no serialisation mandated)  |

### G.13:5 - Extensions (pattern‑scoped; non‑core)

Use `GPatternExtension` blocks with stable **PatternScopeId**s for provider- and method-specific requirements. The blocks identify the required pins, editions and policies. Cite the governing pattern and the provider or method that supplies the meaning or transformation used.

#### G.13:5.1 - `G.13:Ext.ExternalIndexProviderWiring`

- **PatternScopeId:** `G.13:Ext.ExternalIndexProviderWiring`
- **GPatternExtensionId:** `ExternalIndexProviderWiring`
- **GPatternExtensionKind:** `InteropSpecific`
- **GoverningPatternId:** `G.13` (source registration and refresh wiring)
- **Uses:** `{G.13}`
- **⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ExternalIndexType`
* `ExternalEdition` *(as published on `ExternalIndexCard@Context`)*
* `Licence?`
* `CoverageScope`
* `ProviderChangePolicyId?` *(if provider‑specific “schema drift” handling exists)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*

**Notes (wiring-only):**

* Provider‑specific ingestion choices (e.g., OpenAlex‑class, Crossref‑class, ORKG‑class, discipline repositories) **must not** become Part-G-wide norms. This module only records which provider cards exist and which editions/policies are pinned.

#### G.13:5.2 - `G.13:Ext.EmbeddingBasedAlignment`

- **PatternScopeId:** `G.13:Ext.EmbeddingBasedAlignment`
- **GPatternExtensionId:** `EmbeddingBasedAlignment`
- **GPatternExtensionKind:** `MethodSpecific`
- **GoverningPatternId:** `G.13` (mapping interface); the selected alignment method governs its transformation and qualification.
- **Uses:** `{G.13, A.19, E.5.2}`
- **⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ScaleEmbeddingSpecRef.edition`
* `NormalizationMethodRef.edition?` *(when a declared normalization/representation transform is used)*
* `MappingPolicyRef`
* `EvidenceGraphId?` *(when evidence paths for alignment decisions are published)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*

**Notes (wiring-only):**

* A selected embedding-based method supplies the transformation and its qualification for the receiving relation. Cite that method and its edition with the applicable `ScaleEmbeddingSpec` and `NormalizationMethod` references.

#### G.13:5.3 - `G.13:Ext.EntityResolutionAndAliasDocking`

- **PatternScopeId:** `G.13:Ext.EntityResolutionAndAliasDocking`
- **GPatternExtensionId:** `EntityResolutionAndAliasDocking`
- **GPatternExtensionKind:** `InteropSpecific`
- **GoverningPatternId:** `G.13` (mapping interface), `F.17` (public naming); the selected entity-resolution method governs the identity judgement.
- **Uses:** `{F.17, E.10}`
- **⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `UTSRowId[]` *(for externally‑sourced entities that become publicly citable)*
* `ExternalIdAliasSetId?` *(labels only; canonical ids remain UTS ids)*
* `TokenizationPolicyId?`

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*

**Notes (wiring-only):**

* Establish source-entity identity through the selected resolution method before docking its external identifiers as aliases. Preserve the basis for identifying two records as one entity, or leave that identity unresolved; publishing an alias does not establish it.

### G.13:6 - Archetypal grounding

**System.** *Software architecture portfolio design.*
Register an external scholarly index edition for “software architecture” concept neighborhoods. Align extracted technique/tactic claims into ClaimSheets and derive a CHR‑typed feature set (e.g., evidence depth, maturity). Select a **set** of tactics under multi‑objective tradeoffs, use `G.5` to declare that result, and ship a SoTA pack that cites the interop surface.

**Episteme.** *Science‑of‑science discipline dashboard.*
Align external claim graphs (replication, standardisation, disruption-style proxies) into CHR-typed features. For the selected DHC coordinates, establish or reuse C.16 measurement results and recover their active C.21 `DHCReplayBasis`. Use those result refs in the DHC series and its dashboard slice. Publish the selected series episteme through the dashboard form, citing `ExternalIndexRef.edition`, `ClaimMapperRef.edition`, and `MappingPolicyRef`; emit refresh triggers when the external edition updates.

**OEE/QD.** *Open‑ended environment generation.*
Register external environment/task taxonomies as index cards. Align them into generator‑family registries (as cited publications or records), using coverage and regret only as telemetry in this example. When the taxonomy edition changes, use G.11 to assess the mappings and downstream uses that depend on it; realign those whose basis no longer suffices.

### G.13:7 - Bias‑Annotation (informative)

* **Vendor/tool bias.** The kit names conceptual surfaces only; it avoids vendor‑specific file formats or tooling claims.
* **Metric‑authority bias.** External indicators are treated as *inputs* that must be typed, pinned, and evidenced; they are not authority by default.
* **Representation bias.** State which representation or embedding specification was used and pin its edition so the reader can recover the meaning of the alignment.
* **Discipline bias.** Interop supports pluralism by preserving explicit crossings and versioned alignments instead of forcing a single canonical external ontology.

### G.13:8 - Conformance Checklist (CC‑G13; applies when G.13 surfaces are used)

1. **CC‑G13‑CoreRef.** *(normative)* `G.13` implementations **MUST** satisfy the *effective* `G.Core` obligations declared by `G.13:4.1` (`GCoreLinkageManifest`), including trigger typing, Default Governing Definition Index citation, and crossing‑visibility pin discipline.

2. **CC‑G13‑InteropIsNotASpecRefSurface.** *(delegated)* Interop surfaces cite the CN‑Spec/CG‑Spec/CHR/CAL definitions and pins applicable to their transformation and receiving use. They MUST NOT introduce separate legality or comparability gates.
   → delegate to `CC‑GCORE‑CN‑CG‑1`.

3. **CC‑G13‑CrossingsAreExplicitWhenInteropTouchesPlanesOrContexts.** *(delegated)* For reuse across planes or contexts, the alignment **MUST** identify the obtaining relation and the receiving-use and reliance grounds required by its governor. An independently applicable E.18 flow crossing or A.21 gate **MUST** retain its required visibility anchors.
   → delegate to `CC‑GCORE‑CROSS‑1`.

4. **CC-G13-PlanePenaltyPoliciesArePinned.** *(local; governing-definition citing)* When a receiving use applies a numerical plane loss, interop surfaces **MUST** publish the relevant model and policy-id pins under the crossing-visibility discipline, and those policies **MUST** satisfy the constraints governed by `CG-Spec` (cite `CC-G0-Φ`). A `PlaneMapRef` alone supplies no loss model or penalty. Interop surfaces **MUST NOT** define interop-local penalty functions.

5. **CC‑G13‑SetReturnPreserved.** *(delegated)* Interop **MUST NOT** introduce hidden scalarisation or forced single‑winner selection.
   → delegate to `CC‑GCORE‑SET‑1`.

6. **CC‑G13‑DefaultClaimsAreCitationsOnly.** *(delegated)* Any mention of defaults (e.g., dominance regime, `PortfolioMode`) is a **citation** to the default's governing definition through `G.Core.DefaultGoverningDefinitionIndex`, not a local default statement.
   → delegate to `CC‑GCORE‑DEF‑1`.

7. **CC‑G13‑EditionDisciplineForInteropCards.** *(local)* `ExternalIndexCard@Context` and `ClaimMapperCard@Context` **MUST** expose edition pins (`ExternalIndexRef.edition`, `ClaimMapperRef.edition`). Any interop surface published to UTS **MUST** cite the relevant `…Ref.edition` values (incl. `PlaneMapRef.edition?`, `ScaleEmbeddingSpecRef.edition?`) when present.
   FPF edition keys **MUST** appear only on `…Ref.edition` pins when a reference is present. Provider snapshot labels (e.g., `ExternalEdition` on `ExternalIndexCard@Context`) may exist on the source card, but **MUST NOT** be copied into downstream artefacts as free‑floating “edition fields”; downstream artefacts cite the corresponding `…Ref.edition` pins instead.


8. **CC‑G13‑SoSFeaturesAreCHRTypedAndLegal.** *(local; governing-definition citing)* If `SoSFeatureTransform@Context` is used, produced SoS features **MUST** be CHR‑typed via `FeatureTypingRefs{CharacteristicId/ScaleId/CoordinateId}` (governed by `G.3`) and any legality/units obligations must be satisfied via CSLC/CG governing definitions (cite `A.18` / `G.0` / `G.4`; do not invent interop‑local legality gates). When those features serve as DHC measurements, the use **MUST** consume C.16 measurement results; every persisted, compared, aggregated, or published coordinate **MUST** make its active C.21 `DHCReplayBasis` recoverable.

9. **CC‑G13‑TelemetryEmitsCanonicalTriggerKinds.** *(delegated)* Interop‑driven changes (external edition bumps, mapping policy changes, plane‑map edits, embedding‑spec edits) **MUST** emit canonical `RSCRTriggerKindId` causes with scope and payload pins.
   → delegate to `CC‑GCORE‑TRIG‑1`, `CC‑GCORE‑TRIG‑2`, `CC‑GCORE‑TRIG‑3`, `CC‑GCORE‑TRIG‑4`.

10. **CC‑G13‑IDContinuityForExternallySourcedIdentifiers.** *(delegated)* Interop publication **MUST** follow Δ‑discipline: no “renaming by meaning”; use aliases/deprecations as required.
    → delegate to `CC‑GCORE‑ID‑1`, `CC‑GCORE‑ID‑2`.

11. **CC‑G13‑NotationIndependence.** *(local)* Conformance is judged on the conceptual objects in `G.13:4.2`. Any serialisation is non‑normative and must not redefine semantics.
   *(Cites `E.5.2` for notation independence.)*

Interop transforms **MUST NOT** perform illicit arithmetic on ordinal/compare‑only scales (e.g., averaging or subtraction); any aggregation must be via lawful CAL operators with explicit scale legality (cite `A.18` / `CC‑G0‑CSLC`).

### G.13:9 - Common Anti‑Patterns and How to Avoid Them

* **Anti‑pattern: “Format == spec”.** Treating an export schema (KG dump, JSON, RO‑Crate, etc.) as the normative definition.
  **Remedy:** Keep `ExternalIndexCard` / `ClaimMapperCard` / `InteropSurface` as the conceptual specification; treat serialisation as an appendix/tooling concern.

* **Anti‑pattern: Hidden scale invention.** An embedding similarity becomes a “score” without explicit typing/binding.
  **Remedy:** Require `ScaleEmbeddingSpecRef` + edition pins and bind any derived features through CHR/CAL governing definitions.

* **Anti‑pattern: Implicit plane/context reuse.** Using an external concept mapping without its actual relation and receiving-use grounds.
  **Remedy:** Establish the actual sense, kind or plane relation under its governing rule and retain the receiving-use grounds. Publish the bundle or gate anchors required by any actual E.18/A.21 use.

* **Anti‑pattern: Edition‑free dashboards.** Feeding externally derived rows into dashboards without pinned editions/policies.
  **Remedy:** Pin `ExternalIndexRef.edition` and `ClaimMapperRef.edition`; emit RSCR triggers on changes.

* **Anti‑pattern: Interop asserts defaults.** “Interop decides dominance regime / `PortfolioMode`.”
  **Remedy:** Treat defaults as citations only (the relevant governing definition is cited through `G.Core.DefaultGoverningDefinitionIndex`).

### G.13:10 - Consequences

* **Changes become locatable.** External source changes produce typed RSCR causes with scope and payload pins for reconsidering dependent uses.
* **External material supports construction.** External claims and features can support SoTA synthesis, candidate exploration and audit with their source basis recoverable.
* **Recoverable source meaning.** Source and mapper cards, with their edition pins, help keep a provider, tool or format from changing how the result is interpreted.
* **Cross‑tradition reuse becomes auditable.** The alignment exposes the relation used across planes or contexts and its receiving-use grounds. An independently applicable flow crossing or gate retains its required visibility anchors.

### G.13:11 - Rationale

An interop kit lets authors use external scholarly sources while keeping comparisons, editions and transformations visible.

`G.13` connects source meanings and records to receiving inputs through :4.3, then makes the transformation and source editions citable. Its cards and surfaces retain the applicable provenance and refresh inputs. Extensions bind provider or method details used by that transformation.

### G.13:12 - SoTA-Echoing (informative)

* **Scholarly claim graphs & open indexes.** Research knowledge graphs and scholarly indexes can supply claim representations and concept taxonomies as mapping inputs. Treat these as *sources* registered via `ExternalIndexCard`, not as governing patterns.

* **Neural representations for scientific text.** Scientific encoders, such as SciBERT-class and citation-aware SPECTER-class representations, are candidates for alignment heuristics whose suitability must be established for the receiving question. In FPF terms, they belong behind `ScaleEmbeddingSpec` + pinned editions/policies (see `G.13:Ext.EmbeddingBasedAlignment`).

* **Schema matching and entity resolution.** Candidate approaches include deep entity matching, contrastive representation alignment and graph alignment. Select a mapping procedure for the stated relation and evidence, then record its use and limitations through the applicable extension.

* **Systematic-review reporting.** PRISMA-style records make source selection and exclusions inspectable. They can supply provenance and coverage inputs; G.2 still judges coverage for the receiving question. Preserve source editions and windows when consuming those records.

* **QD / Illumination and OEE declared set results.** When a QD or OEE use consumes an external taxonomy or environment corpus, expose its edition and mapping basis. Coverage and regret remain telemetry unless the applicable governing rule explicitly promotes them into the decision criteria.

### G.13:13 - Relations

**Builds on:** `G.Core`.

**Imports:** `G.2`, `G.3`, `G.4`, `G.5`, `G.6`, `G.7`, `G.9`, `G.10`, `G.11`, `A.19`, `A.18`, `G.0`, `F.17`, `E.5.2`, `E.18`.

**Publishes to:** UTS (twin labels where applicable); refresh inputs to `G.11`; shipping hook surfaces to `G.10` (as cited publications or records).

**Relates to:** `G.12` (dashboards), `G.8` (SoS-LOG bundle surfaces) when interop-derived publications or records are consumed there.

### G.13:14 - Author’s quick checklist (informative)

1. Establish the needed input and mapping from source definitions and actual records under :4.3; register each source snapshot with its `ExternalEdition`.
2. Author a `ClaimMapperCard@Context` with the `MappingPolicyRef` and required edition pins.
3. If you derive SoS features, declare a `SoSFeatureTransform@Context` and cite CHR typing refs and provenance hooks.
4. Publish an `InteropSurface@Context` that cites all active `…Ref.edition` values and UTS rows.
5. On any external edition or policy change, emit canonical RSCR trigger causes with the affected scope and payload pins.
6. Keep provider and method conditions with the applicable extension and its cited procedure.

### G.13:End
