## E.20 - Mechanism Introduction Protocol

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative

### E.20:1 - Problem frame

FPF is intentionally **open-ended**: new `U.Mechanism` definitions, suite compositions, and SoTA-driven wiring modules can be added over time. This flexibility creates a recurrent authoring problem: introducing a new mechanism (or revising an existing one) tends to touch multiple subject patterns, specification loci, and extension blocks across Parts A/E/F/G and can easily create drift:

* semantics appear in the wrong governing locus (e.g., Part G wiring starts carrying mechanism meaning),
* suites degrade into “meta‑mechanisms” or hidden gates,
* planned baselines (WorkPlanning) are conflated with execution witnesses (WorkEnactment),
* token drift breaks public references, or
* the corpus accumulates dangling references and non-normative drafting commitments without a governing definition.

This pattern provides a **repeatable, governing-definition assignment protocol** for introducing mechanisms. It preserves kernel coherence by keeping extension points and governing definitions explicit.

**Use this when.** Use E.20 when a proposed FPF change introduces or revises mechanism meaning, suite denotation, suite closure, suite obligations, suite pins, suite protocol semantics, planned-baseline pins, wiring semantics, governing-definition assignment, or what a citeable token denotes.

**First useful move.** Classify the edit with MIP trigger triage: `MIP not triggered`, `local wording or alias-docking only`, or `MIP-run manifest required`. If a manifest is required, name exactly one governing definition for each changed item before writing the pattern text.

**Smallest sufficient governing-definition assignment guidance.** Use the lightest governing-definition assignment that preserves the next bounded reader use. Add MIP-run manifest fields, resolvable mechanism-declaration targets, reference-reservation stubs, suite fields, planned-baseline pins, wiring refs, RSCR triggers, PQG coverage, or deprecation-continuity material only when the current mechanism-declaration or citeable-token claim would otherwise become false, unsafe, non-replayable, or lack a named governing-definition locus.

**Minimum sufficient MIP result.** If the edit does not change citeable-token denotation, mechanism meaning, suite denotation, suite closure, suite obligations, suite pins, suite protocol semantics, planned-baseline pins, wiring semantics, or governing-definition assignment, a MIP-run manifest is not opened; name the current governing locus or alias-docking relation and stop.

**Do not escalate when.** Do not create a MIP-run manifest when alias docking or local wording repair preserves denotation. Do not treat a suite, plan, wiring module, or lexical cleanup as mechanism meaning unless the changed item needs a new or revised governing definition.

**Same problem, different question under repair.** For a mechanism-adjacent transformation-flow problem, use `E.18` for transformation-flow structure, graph/path, valuation, or crossing claims, `A.20` for internal step validity, `A.21` for gate-decision publication, and `E.20` for mechanism-meaning placement; do not open the other three until their own claim is present.

**Semantic repair return.** When E.20 blocks a misleading word, face, alias, or source label, the repair must return to the enabled authoring move: name the governing definition, canonical location, alias-docking relation, or non-trigger stop that remains available under E.20. Do not stop at a classification of vocabulary or publication faces.

**Subject and relation separation.** Keep the graph object and path or crossing relation (`E.18`), MVPK publication faces (`E.17`), internal CV status and witness (`A.20`), gate decision and `DecisionLog` (`A.21`), evidence or provenance relation (`A.10`/`G.6`), work plan or work occurrence (`A.15`), and mechanism-definition assignment (`E.20`) distinct. An MVPK face, `DecisionLog`, evidence value, provenance reference, MIP manifest, or work witness does not supply another subject's project-side value unless an exact dependent-use assertion and its defining or constraining `ClaimGraph` establish that relation.

**Smallest affected locus.** Localize the change to the smallest current locus: `PathSlice` or crossing in `E.18`, CV step in `A.20`, `GateDecision` equivalence class in `A.21`, or mechanism-governing definition in `E.20`. Do not widen to a whole flow or unrelated claim, locus, or EntityOfConcern when that locus is enough.

**Ordinary success.** For ordinary E.20 use, success is that the edit is classified, the current governing locus or alias-docking relation is named, and no MIP-run manifest is opened unless denotation, mechanism meaning, suite denotation, suite closure, suite obligations, suite pins, suite protocol semantics, planning pins, wiring semantics, or governing-definition assignment actually changes.

**Locality asymmetry.** `E.18` is graph-local, `A.20` is step-local, `A.21` is gate-local, and `E.20` is trigger-local. Do not normalize the four patterns into one assurance regime.

**Do not merge these pairs.** Keep `CV.Status` distinct from `GateDecision`, `E.18` `Check` locus distinct from `GateCheckKind`, MIP manifest distinct from `DecisionLog`, `ViewpointMap` distinct from graph semantics, `PathSlice` distinct from a work run, and `GateProfile=Lite` distinct from `PublishMode=Lite`.

**Field applicability.** Always core for E.20: trigger triage and the current governing locus or alias-docking relation. Conditional fields: MIP-run manifest fields, resolvable mechanism-declaration targets, reference-reservation stubs, suite fields, planned-baseline pins, wiring refs, RSCR triggers, PQG coverage, and deprecation continuity; open them only when the corresponding denotation, mechanism-meaning, suite, planning, wiring, lexical, refresh, review, or retirement claim is present.

**Retrieval trap guard.** When excerpted alone, E.20 manifest language must not be read as requiring a full MIP-run for every mechanism-adjacent edit. Pure currentness cleanup, alias docking, optional suite-member citation of an already-defined mechanism, and local wording repair stop at the current governing locus unless denotation, mechanism meaning, suite closure, suite obligations, suite pins, suite protocol semantics, planning pins, wiring semantics, or governing-definition assignment changes.

**Anti-Goodhart guard.** A complete MIP-run manifest is not a substitute for the governed mechanism result. The cited `U.Mechanism` episteme must recover `<content, EntityOfConcernRef, effectiveReferenceScheme>` and the A.6.1 content needed by the receiving use. Realization, refinement, bridge, evaluation, evidence-use, and publication relations remain neighboring claims under their direct patterns.

**Generative side.** E.20 preserves open-ended action by allowing new mechanism definitions, suite variants, wiring, and citeable tokens to enter FPF with a named governing definition; the discipline prevents semantic drift so new work can be added rather than merely blocked.

**What goes wrong if missed.** A suite can start defining mechanism meaning, a plan item can start carrying enactment witnesses or gate decisions, a wiring module can carry kernel semantics, or a token rename can break citations while looking like harmless cleanup.

**What this buys.** E.20 gives the reader one current authoring move: assign the change to the right governing definition and keep mechanism, suite, planning, wiring, and lexical continuity distinct.

**Not this pattern when.** If the edit is only pure currentness, typo, reference, or old-label cleanup and changes no semantics or citeable-token denotation, record the current governing locus and stop. If the question under repair is runtime gate passage, gate decision, approval, suite-as-mechanism, plan-as-enactment, or performed work, use the applicable gate, suite, planning, or Work pattern for that question. A MIP-run manifest is not a runtime gate, gate passage, approval packet, or binary pass/fail decision.

### E.20:2 - Problem

When a new mechanism (or mechanism family) is introduced without an explicit authoring protocol:

1. **Governing-definition ambiguity** causes partial changes: a suite enumerates a new `MechanismDefinitionRef`, but that designator has no resolvable A.6.1 `U.Mechanism` episteme or resolves only to a card-shaped placeholder without mechanism identity and content.
2. **Boundary erosion** occurs: suite descriptions start to define mechanism semantics; method wiring starts to redefine kernel meaning; publication/telemetry becomes a hidden tail.
3. **Plan/enactment confusion** appears: planned slot fillings start to carry launch values, witnesses, or gate decisions.
4. **Terminology drift** breaks citations: renames happen silently; tokens fragment across registers; downstream references become unstable.
5. **Review becomes non‑local**: every introduction is a bespoke scavenger hunt across patterns, making training, review, and refresh unreliable.

### E.20:3 - Forces

| Force | Tension |
|---|---|
| **Extensibility vs Kernel stability** | New mechanisms need to be addable ↔ kernel reference loci need to remain citeable and minimal. |
| **One governing definition vs cross-locus reach** | Each mechanism meaning, suite change, plan item, wiring module, or token migration needs one governing definition while a mechanism introduction often spans suites, plans, wiring, and lexicon. |
| **Didactic usability vs inspectability** | Humans need clear recognition text and examples, while declarations, obligations, and pins must remain checkable at their governing loci. |
| **SoTA evolution vs semantic integrity** | Methods evolve fast ↔ mechanism meaning SHALL NOT silently shift via wiring updates. |
| **Local naming freedom vs global reference continuity** | Context-local labels are necessary ↔ references need to remain stable across editions and refactors. |

### E.20:4 - Solution — the Mechanism Introduction Protocol (MIP)

#### E.20:4.0 - Terminology note (disambiguation)

*This protocol and any MIP-run manifest are authoring-side semantic-governing-definition assignment maps.* A manifest is not an approval packet, gate, runtime decision, or pass/fail result. It names where mechanism meaning is governed and what must not be inferred from suites, plans, wiring, aliases, or gates.

MIP governs **how changes are assigned to their governing definitions**, not how systems execute.

**MIP trigger triage.** Not every reference cleanup is a MIP-run. Classify the proposed edit before requiring a manifest:

* **MIP not triggered:** pure currentness, reference, typo, or old-label cleanup that changes no mechanism, suite, planned-baseline, wiring, governing-definition, or citeable-token semantics.
* **Local wording or alias-docking only:** wording clarifies an already-governed mechanism relation, or `F.18` alias docking preserves citeability of an old token without changing what the token denotes.
* **MIP-run manifest required:** the edit changes mechanism meaning, suite denotation, suite closure, suite obligations, suite pins, suite protocol semantics, planned-baseline pins, wiring semantics, governing-definition assignment, or what a citeable token denotes.

Only the third outcome uses the manifest in `E.20:4.2`. The first two still name the current governing locus or alias-docking relation when the text will be published. When the only current result is no denotation change, the published content should not carry MIP-run vocabulary except as a short non-trigger note.

#### E.20:4.0.1 - Mint vs reuse

**Mints:**
* **MIP** — Mechanism Introduction Protocol (this pattern).
* **MIP-run** — an authoring event that applies this protocol to a concrete change set, captured as a short manifest (recorded as a DRR-linked change record or an equivalent, explicitly citeable change record).

**Reuses:**
* A.6.1 `U.Mechanism` epistemes, their `MechanismDefinitionRef` designators, non-mechanism reference-reservation stubs, suite descriptions (`MechSuiteDescription` and specializations), WorkPlanning plan items (`SlotFillingsPlanItem` and specializations), alias docking (F.18), RSCR triggers (G.Core), and PQG profiles (E.19).

#### E.20:4.1 - Step 1: Classify the introduction

A MIP-run SHALL first classify the change, because different classes have different governing definitions:

1. **New declared operation family or archetypal grounding.** The `EntityOfConcernRef` names an operation family not previously declared at the selected governing locus.
2. **New mechanism declaration or semantic edition.** One A.6.1 `U.Mechanism` episteme receives new identity-bearing content or a new effective `U.ReferenceScheme`.
3. **Neighboring mechanism-relation change.** A realization, refinement, conservative extension, equivalence, bridge, evaluation, evidence-use, or publication relation changes while the mechanism content does not.
4. **Suite change** (membership, obligations, spec pins, or suite protocols).
5. **Planned-baseline change** (new or revised `SlotFillingsPlanItem` specialization, or changes to its pins).
6. **Wiring change** (new or revised Part-G extension modules, SoTA method packs, or selectors).
7. **Terminology migration** (renames, token splits or merges, or register changes).
8. **Deprecation, supersession, or retirement** (status change, successor relation, and preserved citeability; apply E.20:4.9.1).

**Mechanism-kind boundary.** `MechanismDefinitionRef` is a designator. Minting it neither creates a `U.Mechanism` episteme nor admits a new U-kind. A new U-kind claim requires E.24.UK; a new mechanism episteme must satisfy A.6.1 identity and content; a new transformation-flow structure requires E.18.

**A.6.1 compatibility.** Mechanism identity is `<content, EntityOfConcernRef, effectiveReferenceScheme>`. Identity-bearing content comprises direct subject and range fields, `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, Applicability, and an optional `SignatureManifest` when dependency replay matters. An operation index may be derived from the declaration-local `operationDesignator` values; it is not another content group. Each operation's arguments and results remain A.6.1 `ArgumentDeclaration` and `ResultDeclaration` content. A.6.5 SlotSpecs remain exclusive to a `RelationSignature` for an already governed direct relation. Realization, refinement, extension, bridge, evaluation, evidence-use, and publication relations are governed separately.

**New-declaration criterion.** Treat a change as a new declared operation family when `EntityOfConcernRef` changes. Treat changed mechanism content or effective reference scheme as a new semantic edition. A changed neighboring relation alone does not create a new mechanism identity, although it may reopen reliance on the current declaration.
A single MIP-run MAY span multiple classes, but SHALL treat each class with its correct governing-definition assignment (below).

#### E.20:4.2 - Step 2: Declare the governing-definition assignment map (mandatory)

For every new or modified change item, the MIP-run SHALL name **exactly one governing definition** and assign the change there. In FPF, that governing definition is a citeable, patchable `PatternId`, `PatternId:SectionPath`, `PatternScopeId = G.x:Ext.*`, or `DRRId` (E.9). The core MIP-run manifest in a citeable change record is limited to:

* each changed item,
* its governing definition,
* its canonical location (expressed as `PatternId:SectionPath`, `PatternScopeId`, or `DRRId`, not as prose), and
* the forbidden overread or forbidden move blocked by that assignment.

Conditional manifest fields appear only when the corresponding claim is present:

* the change class(es) from E.20:4.1 when needed to disambiguate the assignment,
* new or changed citeable tokens, including a `MechanismDefinitionRef` or a public operation, argument, or result designator, when token denotation or citeability changes,
* the best-known Delta-Class (`Δ-0` to `Δ-3`) and impact radius estimate (E.15) when the run is plausibly `Δ-2` or `Δ-3`,
* intended RSCR trigger types when a refresh or regression-wiring claim is present, and
* the PQG (E.19) profile set when the run crosses an E.19-governed review boundary.

**Note (normative).** If the canonical location is a Part‑G wiring module, it SHALL be cited as a `PatternScopeId` (`G.x:Ext.*`) and the module SHALL declare `GoverningPatternId` (wiring is binding-only; meaning remains governed by its cited pattern).

**Canonical governing-definition map (normative):**

| Change kind | Governing definition | Canonical location | Forbidden move |
|---|---|---|---|
| `U.Mechanism` identity and content: exact `EntityOfConcernRef`, effective reference scheme, direct subject and range fields, operation algebra, laws, admissibility, Applicability, and optional dependency manifest | **Mechanism-subject pattern under A.6.1** | Designated mechanism-subject pattern | A suite, plan, wiring module, card layout, or MIP manifest does not supply mechanism semantics; neighboring relations stay with their direct patterns. |
| Suite membership, obligations, spec pins, and suite protocols | **Suite-subject pattern** | `A.6.7` or `A.6.7.<FamilyKey>` | SHALL NOT carry mechanism semantics, acceptance thresholds, gate criteria, DecisionLogs, or publication tails into the suite. |
| Planned baseline pins (planned slot fillings, edition-pinned refs, explicit time selector) | **WorkPlanning subject pattern** | `A.15.3` plus suite-specific specialization when needed | SHALL NOT embed launch values, witnesses, or gate decisions in planning. |
| SoTA method, comparator, or generator **definitions**, including provenance and evaluation semantics | **SoTA-pack subject pattern** | `G.2` (SoTA synthesis packs) | SHALL NOT rephrase SoTA evolution as kernel semantics. |
| Wiring that binds SoTA packs into flows or tasks | **Extension module governing definition** | `G.x:Ext.*` (`GPatternExtension` with explicit `PatternScopeId`) | SHALL NOT mint new semantics; SHALL bind only. |
| Token renames and drift management | **Lexical subject pattern** | `F.18` (alias docking) plus registers per E.10/F.17 | SHALL NOT silently rewrite tokens or break citations. |
| Change-cause taxonomy and regression triggers | **RSCR subject pattern** | `G.Core` | SHALL NOT invent ad hoc “reason kinds” scattered in patterns. |
| Project specializations of a mechanism | **Project specialization pattern** | `P.*` patterns (using `⊑/⊑⁺`) | SHALL NOT mutate kernel membership to express project variants. |

**Guard (normative).** Any proposed change that cannot name a governing definition from the table above SHALL be treated as a non-normative drafting note or candidate intake and SHALL NOT be relied upon as an FPF architectural commitment. Such material may exist only in an explicitly marked non-normative source note until assigned to its governing definition.

#### E.20:4.3 - Step 3: Resolve the designator before dependent use

When a change introduces `MechanismDefinitionRef`, create one resolvable target at the subject-pattern locus before another declaration cites it. Distinguish two target states:

1. **Reference-reservation stub.** This is a draft authoring episteme, not `U.Mechanism`. It reserves the designator, names the intended operation-family EntityOfConcern, cites the subject pattern, and lists the missing A.6.1 identity or content needed for introduction. A publication may expose the stub as a candidate. A suite may cite it only in an explicitly candidate-valued position; the stub cannot satisfy admitted suite membership, closure, planned-baseline, wiring, gate, reuse, or import claims.
2. **Introduced mechanism episteme.** `MechanismDefinitionRef` resolves to one A.6.1 `U.Mechanism` episteme with recoverable identity and sufficient content for the receiving use. Only this state can fill a position whose ValueKind is `U.Mechanism`.

A card, table row, file, or register entry may publish either state. Its layout and publication identity do not determine which state obtains.

#### E.20:4.4 - Step 4: Complete mechanism semantics

An introduced mechanism has the A.6.1 identity tuple:

```text
<content, EntityOfConcernRef, effectiveReferenceScheme>
```

Its minimum semantic content for ordinary reuse names:

* direct `SubjectKind` and `RangedValueKind`, with `ResultKind`, `SliceSet`, and `ExtentRule` only when current;
* `OperationAlgebra` with one exact A.6.1 `OperationDeclaration` per reused operation and one declaration-local `ArgumentDeclaration` or `ResultDeclaration` for every typed argument or result position, including its meaning, exact ValueKind, binding designation rule, binding predicate, and any semantic cardinality;
* `LawSet`;
* `AdmissibilityConditions`;
* Applicability through exact claim scope, selected time, reference plane when current, and mechanism-specific conditions;
* `SignatureManifest` only when actual imported or provided declaration content must replay.

An operation index may be derived from the declaration-local operation designators for retrieval; it is not another content group. Argument and result declarations remain inside their exact A.6.1 operation declaration and never become A.6.5 SlotSpecs. Refinement, conservative extension, equivalence, bridge use, mechanism realization, evaluation, evidence use, method use, dated work, description, representation, and publication remain neighboring objects or relation occurrences. A MIP-run names their subject patterns instead of copying them into the mechanism declaration.

Create a new semantic edition when content, `EntityOfConcernRef`, or effective reference scheme changes. Keep the current edition when only a neighboring relation occurrence or publication changes. E.20 relies on the current numbered A.6.1 conformance checklist and does not maintain a second checklist-ID family.

If a suite or family claims shared operation-member vocabulary across several mechanism declarations, apply E.20:4.5.

#### E.20:4.5 - Step 5: Suite-scoped operation-member vocabulary discipline (prevent member-name drift)

Use this step only when a suite or family claims that several mechanism declarations intentionally share operation, argument, or result vocabulary. Repeated spelling by itself does not establish that claim.

1. The suite-subject pattern SHALL name one citeable vocabulary locus and the exact member mechanism declarations to which the shared terms apply. That vocabulary coordinates names only; it creates no `OperationDeclaration`, `ArgumentDeclaration`, `ResultDeclaration`, ValueKind, binding predicate, or actual binding.

2. Each member mechanism SHALL still declare every current operation, argument, and result locally under A.6.1, including its exact meaning, ValueKind, designation rule, binding predicate, and cardinality. A cited shared term or equal spelling imports none of those semantics.
3. When a public shared term is introduced, renamed, split, or merged, update the shared vocabulary locus and every affected declaration or alias route. When only one declaration changes meaning, keep the change local unless the intended shared denotation also changes. Apply E.20:4.9 whenever citeability changes.

This step prevents one intended suite term from silently fragmenting while preserving the declaration-local semantics of every A.6.1 operation member. It supplies no operation position and no actual application binding.

#### E.20:4.6 - Step 6: Suite integration (if the mechanism is a suite member)

If the introduction changes a suite (`MechSuiteDescription` or specialization):

1. **Membership set semantics (WF‑MS‑1).** `mechanisms` is a set: duplicates are nonconformant and list order carries no semantics.
2. **Ordering is only in protocols.** If ordering matters, express it only in `suite_protocols`.
3. **Protocol closure (WF‑MS‑2).** If `suite_protocols` is present, then for every `ProtocolStep` in every `SuiteProtocol`, `step.mechanism ∈ mechanisms`.
4. **No hidden tails.** Required stages (e.g., normalization/aggregation/Γ‑fold) are explicit protocol steps; do not hide them inside other steps.
5. **Guard/gate separation.** Suites and mechanisms SHALL NOT publish `GateDecision`/`DecisionLog`. `AdmissibilityConditions` and tri‑state `GuardDecision` remain governed by the mechanism definition; `OperationalGate(profile)` acceptance thresholds and pass/fail criteria remain gate/acceptance concerns.
6. **Suite is descriptive only (WF-MS-3/4).** A suite states membership, obligations, pins, and suite protocols. It does not restate `U.Mechanism` identity-bearing content. Any publication or telemetry continuation remains outside the suite protocol and requires its own exact publication or flow assertion and predicate.

**Kernel stability rule (recommended).** If the suite is a kernel suite, and the change adds a new required stage, prefer creating a **suite variant** rather than mutating the kernel membership. If mutation is unavoidable, pair it with terminology continuity (E.20:4.9) and RSCR triggers (E.20:4.10).

#### E.20:4.7 - Step 7: Planned baseline & P2W planning-to-work boundary (if planning changes)

If the mechanism introduction changes what a WorkPlanning baseline pins (e.g., selected comparator specs, method descriptions, time selector, guard pins):

1. Introduce or revise a `SlotFillingsPlanItem` specialization under the WorkPlanning subject pattern.
2. The plan item SHALL remain planning-only:
   * pins/refs only (ByValue or `<RefKind>`),
   * no launch values,
   * no `FinalizeLaunchValues` witnesses,
   * no gate decisions or decision logs.
   * time is explicit: include `Γ_time_selector` or `Γ_time_rule_ref` (XOR); implicit “latest/current” is nonconformant.
3. The plan item SHALL target exactly one **Description-scoped, edition-addressable** slot-bearing description via `target_slot_bearing_description_ref` (typically a kit or suite) and SHALL NOT target a `MechanismDefinitionRef`. If a "standalone mechanism baseline" is needed, introduce an explicit Description-scoped slot-bearing description wrapper (e.g., a mech kit or a suite-of-one) and target that.

This step exists to keep the P2W planning-to-work boundary crisp: planning defines **planned fillers**, enactment witnesses **actual runs**.

#### E.20:4.8 - Step 8: Wiring & SoTA updates (keep method evolution out of kernel)

If the introduction involves methods, comparators, selectors, or other SoTA-sensitive choices:

1. Put method/comparator family semantics in **SoTA packs** (G.2) and reference them by edition-pinned refs.
2. Pin the chosen SoTA refs for a baseline in WorkPlanning plan items (E.20:4.7); wiring consumes pins rather than silently overriding them.
3. Put flow/task binding logic in **wiring modules** (`GPatternExtension`), with an explicit `PatternScopeId` and declared subject pattern.
4. Wiring may bind, select, dispatch, or cite SoTA method packs; it may not redefine the mechanism's identity-bearing A.6.1 content. A bridge, realization, evaluation, evidence-use, or publication claim named by wiring remains governed by its direct relation pattern.
5. If a SoTA update changes a mechanism's signature/laws, that semantic change SHALL be performed in the mechanism-subject pattern, under the A.6.1 mechanism-definition template; the change SHALL emit RSCR triggers (E.20:4.10).

#### E.20:4.9 - Step 9: Terminology continuity (alias docking)

If the introduction renames any public token or changes canonical naming:

1. Use lexical alias docking (F.18) so old tokens remain citeable.
2. Update registers and twin labels per lexical discipline.
3. Avoid silent rewrites: the MIP-run SHALL make the alias relation and successor relation explicit.

#### E.20:4.9.1 - Deprecation / supersession / retirement (preserve citeability)

If the change class includes deprecation/supersession/retirement (E.20:4.1 #8), the MIP-run SHALL preserve reference continuity while making the status change explicit:

1. **Preserve the canonical target.** The deprecated `U.Mechanism` episteme, reference-reservation stub, suite description, plan item, or wiring module SHALL remain resolvable at its canonical location; deprecation MUST NOT be implemented by removal that would break citations.
2. **Keep the public token citeable.** The deprecated token (`MechanismDefinitionRef`, suite token, plan-item token, etc.) SHALL remain citeable. If a successor token/name is introduced, the old token SHALL be alias-docked per F.18 (E.20:4.9).
3. **Declare successor (or “no successor”).** The deprecated mechanism episteme, reference-reservation stub, suite description, plan item, or wiring module SHALL declare a successor relation or explicitly state that none is current, using the direct supersession or deprecation pattern.
4. **Assign downstream updates to governing definitions.** Any needed suite denotation, closure, obligation, pin, protocol-semantic, WorkPlanning-pin, or wiring-semantic change SHALL be performed in its respective governing definition (E.20:4.2), preferably by introducing a suite variant rather than silently swapping kernel membership.
5. **Emit RSCR triggers.** Deprecation/supersession SHALL emit typed RSCR triggers and extend the regression envelope (E.20:4.10), including checks for dangling refs and alias coverage.

#### E.20:4.10 - Step 10: RSCR triggers + regression envelope

A MIP-run that changes any of:
* mechanism signatures,
* suite membership/protocols,
* planned baseline pins,
* shared operation-member vocabulary or declaration-local operation, argument, or result designators,
* terminology/alias docking that changes citeable tokens,
* or other reference loci

SHALL emit typed RSCR triggers via the RSCR subject pattern and SHALL extend the regression envelope to include, at minimum:

* no dangling `MechanismDefinitionRef` enumerations,
* suite membership set semantics + protocol closure,
* guard/gate separation preservation,
* P2W planning-to-work boundary preservation (planning vs enactment).

**Guard (normative).** Trigger kind identifiers (e.g., `RSCRTriggerKindId`) SHALL be selected from the RSCR trigger catalogue governed by `G.Core`. A MIP-run SHALL NOT mint ad hoc trigger kinds (“reason kinds”) scattered in arbitrary patterns/modules.

**Manifest hook (recommended).** The MIP-run manifest SHOULD list emitted trigger types and the regression envelope deltas as checkable items.

#### E.20:4.11 - Step 11: Apply PQG profiles (E.19) and close the run

Every MIP-run SHALL be reviewed using PQG (E.19) with:

* **PCP‑BASE** always, and
* the triggered profiles implied by the change class (at least):
  * **PCP‑SUITE** if any suite locus changed,
  * **PCP‑P2W** if any planned-baseline locus changed,
  * **PCP‑TERM** if any new terms/renames are introduced,
  * **PCP‑SOTA** if SoTA packs are introduced/modified,
  * **PCP‑NORM** if the run introduces/changes normative requirements or conformance items,
  * **PCP‑DEONT** if RFC keyword clauses are introduced/modified (or if invariant/predicate vs deontic form is ambiguous),
  * **PCP‑BRIDGE** if cross-context reuse, crossings, or bridges are introduced or changed,
  * **PCP‑REFRESH** if refresh-sensitive claims (SoTA lists, “current practice”, enumerations) are touched,
  * plus any applicable modularity / boundary / normativity profiles required by the delta.

**MIP-run outcomes (normative set).**
A reviewed MIP-run SHALL be closed as one of:

1. **Proceed (single change set).**
2. **Proceed via governing-definition split** (mandatory when semantics were placed under the wrong governing definition; the change is split into governing-definition-correct edits).
3. **Proceed via suite variant** (preferred when kernel stability is threatened by adding new required stages).
4. **Block with explicit missing condition** (insufficient semantics; stub exists but completion condition is DRR-tracked).
5. **Reject** (violates invariants such as suite-as-gate, plan-as-enactment, or governing-definition ambiguity).

### E.20:5 - Archetypal Grounding *(Tell–Show–Show)*

**Show 0 (suite member, no new mechanism meaning).** A suite adds an already-introduced `U.Mechanism` episteme by its `MechanismDefinitionRef` and changes no identity component, declaration content, or neighboring relation on which the suite use relies. E.20 records the suite-governing locus and stops; no new mechanism declaration target or MIP-run manifest is opened.

|  | Tell | Show #1 — add a mechanism to an existing suite *variant* | Show #2 — introduce a new mechanism family + suite |
|---|---|---|---|
| **Scene** | Mechanisms evolve: new stages appear, methods mature, and planning records need to remain citeable. | A team wants an additional “stage” in a characterization pipeline, but does not want to mutate the kernel suite. | A new domain needs a mechanism family or species not yet present in any existing mechanism-profile cluster (for characterization: `A.19.*`), plus a suite that composes several distinct mechanisms with a P2W hook. |
| **Governing-definition assignment** | Each change item has one governing definition; changes are assigned there, not smeared. | 1) Add the introduced `U.Mechanism` episteme under the mechanism-subject pattern. 2) Add a suite variant under the suite-subject pattern. 3) Pin the variant via a planned-baseline specialization. 4) Wire the variant via a `GPatternExtension`. | 1) Add the new operation-family declaration and archetypal grounding under the subject pattern. 2) Add `A.6.7.<FamilyKey>` describing the suite. 3) Add a suite-specific `SlotFillingsPlanItem` specialization. 4) Add SoTA packs and wiring modules. |
| **Resolvable target first** | No suite treats a dangling designator or reservation stub as an introduced mechanism. | Create the reservation stub or introduced mechanism target first; add only an introduced mechanism to admitted suite membership. | Create each mechanism target first; then publish suite membership by designator. |
| **Suite discipline** | Suites are descriptive: membership, obligations, pins, protocols; not mechanisms and not gates. | The variant’s `suite_protocols` explicitly names the new stage; publish/telemetry remains outside the suite. | The new suite defines shared obligations and allowed pipelines without embedding mechanism semantics. |
| **P2W planning-to-work boundary** | Planning pins refs; enactment witnesses runs. | The plan item pins the chosen suite variant and any method/spec refs; no launch values or decision logs. | The plan item specialization defines the planned fillers/pins that downstream flows cite. |
| **SoTA updates** | Methods change faster than kernel meaning; wiring is where choices are governed. | A `GPatternExtension` selects a post-2015 scoring method by edition‑pinned ref; no kernel mutation required. | The family ships method packs and wiring modules; the identity-bearing content of each introduced `U.Mechanism` remains at its mechanism-subject pattern. |

### E.20:6 - Bias-Annotation

Lenses tested: **Governance** (governing-definition assignment, continuity), **Architecture** (boundary hygiene and modularity), **Onto/Epist** (meaning placement and type discipline), **Pragmatic authoring** (reviewability, governing-definition split handling), **Didactic** (Tell-Show-Show training scaffold).

### E.20:7 - Conformance Checklist (normative)

**Conformance use.** This checklist tests the governing-definition assignment guidance already stated in the Solution. It is not the first entry text for ordinary use or a mandatory full-corpus check; an item is applied only when its corresponding trigger triage, manifest, declaration target, suite, planning, wiring, lexical, RSCR, PQG, or deprecation move is present. Before applying any item, name the Solution guidance it tests; if no such reader use is present, treat the item as orientation-only or not applicable rather than expanding the applied assurance material.

**Conformance groups.** Ordinary E.20 use starts with trigger triage and stops at the current governing locus when no denotation or mechanism-meaning change is present. Manifest-core items apply only when a MIP-run is actually triggered. Publication and assurance items apply only when citeability, reference-reservation stubs, alias docking, RSCR, PQG, or deprecation continuity is part of the current claim. Crossing, launch, and work-enactment checks are not governed by E.20; if those claims become present, use the gate, planning, or work loci and keep E.20 to governing-definition assignment.

| ID | Requirement | Purpose |
|---|---|---|
| **CC-E20-0 (MIP trigger triage).** | Every proposed mechanism, suite, planned-baseline, wiring, governing-definition, or citeable-token edit is classified as `MIP not triggered`, `local wording or alias-docking only`, or `MIP-run manifest required` before E.20 is cited to start a MIP-run. | Prevents pure currentness cleanup from becoming a false runtime gate or expanded authoring event. |
| **CC-E20-1 (Governing-definition assignment declared).** | Every MIP-run **SHALL** provide a MIP-run manifest that lists each changed item, exactly one governing definition, and the canonical location; each changed item **SHALL** be written in that canonical location. | Prevents “floating commitments” and semantic placement errors. |
| **CC-E20-2 (Resolvable mechanism target).** | Every `MechanismDefinitionRef` resolves either to an explicitly non-mechanism reservation stub or to an introduced A.6.1 `U.Mechanism` episteme. Only the latter fills admitted mechanism positions. | Eliminates dangling references and card-form semio-bias. |
| **CC‑E20‑3 (Suite discipline preserved).** | If a suite is edited, it **SHALL** preserve: membership set semantics, protocol closure, no hidden tails, no gate decisions/logs, no publication records. | Prevents suite-as-gate and suite-as-mechanism drift. |
| **CC-E20-4 (Shared operation-member vocabulary preserves declaration locality).** | If a suite or family claims shared operation, argument, or result vocabulary, one citeable shared locus **SHALL** name its exact member declarations, and every member **SHALL** still define its own A.6.1 operation members and binding semantics. Equal spelling or a shared-term citation imports no declaration member or actual binding. | Prevents vocabulary drift without collapsing declaration-local semantics into a suite lexicon. |
| **CC-E20-5 (P2W planning-to-work boundary preserved).** | If planned baselines are edited, plan items **SHALL** remain WorkPlanning-only (pins/refs only), **SHALL** target exactly one Description-scoped slot-bearing description via `target_slot_bearing_description_ref` (and **SHALL NOT** target a `MechanismDefinitionRef`), and **SHALL NOT** contain enactment witnesses, launch values, or gate decisions. | Keeps planning and enactment distinct and replayable. |
| **CC‑E20‑6 (Kernel stability handled).** | If a kernel suite would gain a new required stage, the change **SHOULD** be expressed as a suite variant; if mutation occurs, it **SHALL** include continuity measures (alias docking and explicit delta). | Minimizes E.15 impact radius of kernel edits. |
| **CC‑E20‑7 (SoTA wiring, not kernel semantics).** | Method/comparator choices **SHALL** be represented via SoTA packs and wiring modules; if a SoTA update changes mechanism semantics, that change **SHALL** be made in the mechanism-subject pattern and not by wiring. | Prevents silent semantic shifts. |
| **CC‑E20‑8 (Terminology continuity).** | Any rename changing citeable tokens **SHALL** use alias docking and register updates; silent rewrites are non‑conformant. | Preserves reference stability. |
| **CC‑E20‑9 (RSCR triggers + regressions).** | Any semantic or reference-change **SHALL** emit RSCR triggers and extend the regression envelope to cover dangling refs + suite closure + guard/gate separation + P2W planning-to-work boundary. | Makes changed loci and regression obligations explicit and testable. |
| **CC‑E20‑10 (PQG coverage).** | Every MIP-run **SHALL** be reviewed under PQG (E.19) with PCP‑BASE and the triggered profiles implied by the change. | Normalizes review and refresh. |
| **CC‑E20‑11 (Deprecation preserves citeability).** | Any deprecation, supersession, or retirement action **SHALL** preserve citeability of the deprecated token, keep the mechanism episteme or reservation stub and every affected suite description, plan item, or wiring module resolvable, and state the direct successor relation or its absence (E.20:4.9.1). | Prevents broken citations and orphaned semantics during evolution. |

### E.20:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | Repair |
|---|---|---|---|
| **Wiring carries semantics** | Part G extensions start redefining what a mechanism “means”. | Meaning becomes edition-fragile and non-local. | Move semantics back to the mechanism-subject pattern; keep extensions as binding only. |
| **Suite becomes a meta-mechanism** | Suite text defines ops/laws or embeds thresholds/decisions. | Collapses suite, mechanism, and gate kinds; creates hidden gate behavior. | Restore suite as description-only; push thresholds to acceptance/gate kind. |
| **Plan becomes enactment** | Plan items contain launch values, witnesses, or decisions. | Destroys the P2W planning-to-work boundary and prevents replay of what was planned versus what occurred. | Strip enactment content; pin only refs, policies, and time selectors. |
| **Kernel churn by convenience** | New required stage is added directly to kernel suite membership. | Expands the E.15 impact radius; destabilizes citations. | Prefer suite variant; if not possible, pair with alias docking and explicit deltas. |
| **Token drift by silent rename** | “Just rename UNM to ...” without aliasing. | Breaks citations and downstream reasoning. | Use F.18 alias docking; update registers explicitly. |
| **MIP as gate surrogate** | A MIP-run manifest is treated as a runtime pass/fail result or gate passage. | Governing-definition assignment is being mistaken for project execution or gate decision. | Keep MIP as authoring-side governing-definition assignment; use `A.21` for gate decisions and `A.15` for work or enactment claims. |
| **Governing-definition ambiguity** | “We’ll put it somewhere later.” | Leaves incompleteness and drift invisible. | Name the governing definition up front; otherwise treat as non-normative. |

### E.20:9 - Consequences

**Benefits**
* Mechanism introductions become **trainable and reviewable** (a repeatable governing-definition map).
* Reduces drift by requiring one subject pattern for each mechanism meaning and keeping semantics in their subject pattern.
* Keeps suites descriptive and the P2W planning-to-work boundary inspectable.
* Supports SoTA evolution without destabilizing kernel meaning.

**Costs**
* Introductions use more explicit assignment records (governing-definition map, PQG coverage).
* Some changes will be split into multiple governed edits (by design), which increases authoring overhead.
* Kernel stability discipline can feel “slow” when a team wants a quick mutation.

### E.20:10 - Rationale

Mechanism declarations are high-leverage epistemes: a small change can affect suites, planned baselines, wiring modules, evaluations, and evidence uses. Without a protocol, the corpus tends toward semantic duplication across governing loci, so a reader cannot recover which declaration or neighboring relation actually changed.

Governing-definition-directed authoring is a pragmatic compromise: it does not depend on tooling, yet it gives a stable governing-definition map that enables subsequent review and refresh.

### E.20:11 - SoTA-Echoing

| SoTA source idea | FPF invariant | Reader use | Rejected shortcut |
| --- | --- | --- | --- |
| Mechanism semantics in A.6.1, effects-handler practice, and refinement-style declaration discipline require an explicit operation, law, admission, and applicability locus. | `U.Mechanism` identity is `<content, EntityOfConcernRef, effectiveReferenceScheme>`; direct subject and range fields, operation algebra, laws, admission conditions, Applicability, and an optional dependency manifest are identity-bearing content. Each reused operation carries declaration-local argument and result declarations; an operation index may be derived from operation designators, while A.6.5 SlotSpecs remain `RelationSignature` content and realization, bridge, evaluation, evidence-use, and publication relations remain neighboring. | When a mechanism is introduced or changed, make the A.6.1 declaration target resolvable before suites, plans, or wiring cite it; state each operation member in its exact operation declaration and handle every neighboring claim under its direct pattern. | Treating suite vocabulary, wiring prose, a card layout, or a MIP manifest as mechanism semantics. |
| SoTA method evolution is carried by SoTA synthesis packs, shipping boundaries, and refresh wiring rather than silent kernel mutation. | Use `G.2`, `G.10`, and `G.11` for method-evolution apparatus: SoTA packs, release/shipping boundary, and refresh wiring. If the SoTA change alters mechanism meaning, the mechanism-governing definition changes. Current-source examples are usable only through named pack refs, such as SLSA v1.2 for provenance and attestation discipline, RO-Crate 1.2 for research-package publication discipline, QDax JMLR 2024 for QD-library practice, or a named current domain survey or source when that domain claim is present. | Tie a mechanism-changing SoTA update to the SoTA pack or source ref named by value and the refresh or shipping locus, then edit the mechanism-subject pattern if semantics changed. | Rephrasing a fashionable method update as kernel semantics or hiding it in wiring. |
| Open-ended and set-valued method evolution may return candidate sets, archives, or selector outputs. | C.18, C.19, and G.5 preserve set-return and selection boundaries; MIP must not force one approved mechanism too early. | Keep candidate mechanisms, selected sets, abstain/reject states, and archive semantics in their receiving loci until a mechanism-governing definition is actually selected for introduction. | Collapsing open-ended exploration or selector output into one prematurely approved mechanism. |
| Mechanism-related refresh uses explicit pins and trigger kinds rather than restating method semantics. | G.11-style refresh uses edition pins, policy pins, `PathSliceId`, and RSCR trigger kinds; refresh wiring enables comparable reruns but does not redefine the method. | When a mechanism change affects refresh, name the pins and RSCR trigger kinds and keep method semantics in the mechanism or SoTA-pack locus. | Letting refresh wiring become a second method definition. |
| Stable identifiers and modular vocabularies preserve reference continuity. | Names, aliases, lexicons, and stable identifiers preserve citeability; they do not establish mechanism law, admissibility, evidence, or gate fit. Mechanism meaning and admissibility belong in definitions, signature, law, and admissibility patterns, suite boundaries, SoTA packs, and wiring modules according to their exact use named by value. | Use alias docking and lexicon updates to preserve references, then return mechanism meaning to the definition that supplies it. | Treating ontology or vocabulary modularity as sufficient mechanism introduction. |

### E.20:12 - Relations

**Builds on:**
* **E.8** (pattern structure and normative authoring discipline)
* **E.10 / F.17–F.18** (lexical registers, twin labels, alias docking)
* **E.19** (PQG/PCP profile-based review)
* **E.15** (evolution discipline; DRR/edition thinking)

**Coordinates with:**
* **A.6.1** (`U.Mechanism` definition template governance)
* **A.6.7** (`MechSuiteDescription` integrity)
* **A.15.3** (`SlotFillingsPlanItem` and planned baseline seam)
* **E.18** (`TransformationFlowStructure` values that cite planned baselines)
* **G.Core** (RSCR trigger catalogue)
* **G.2** (SoTA synthesis packs)
* **G.x:Ext.\*** (wiring modules via `GPatternExtension`)

**Constrains:**
* Any change set that introduces or revises mechanisms, suites, planned baselines, or wiring in a way that changes citeable loci.

### E.20:End

