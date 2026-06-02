## E.17 - Multi‑View Publication Kit

**At a glance.** Use `E.17` when one source-backed episteme, episteme-lane view, morphism, or functional relation must be published in several readable faces for different readers without changing the underlying claim.

**Use this when.** The engineering team needs a plain view, technical card, interoperability card, or assurance lane that helps people read, inspect, exchange, or cite the same source-backed relation without turning the face into work occurrence, evidence, gate passage, engineering justification, control architecture, or release permission by presentation alone.

**First output.** One source-pinned publication face with the underlying `U.Episteme`, `D` episteme, or `S` episteme, publication scope, face kind, admissible publication use, and any live downstream typed value named only as far as the current use needs, such as a `GateDecision`, evidence path, work occurrence, status source, or authority-reference relation.

**Working action spine.** Publish one source-pinned face -> separate source episteme or episteme-lane view, face, carrier, admissible publication use, and any live downstream typed value plus its governing FPF pattern/reference -> use the face for inspection, source-finding, review, exchange, or planning preparation -> output one source-pinned publication face -> apply the exact neighboring FPF pattern if work, evidence, gate, engineering-justification, control, or release use becomes live.

**Ordinary formality rule.** If the face only supports orientation, source-finding, review, comparison, or planning preparation, keep the publication light: one pinned face or compact card plus a clear admissible-use line is enough.

**Load-bearing formality rule.** Add the fuller MVPK record only when the face will support external-impact reliance, cross-context exchange, evidence citation, gate or release pressure, engineering-justification use, disputed interpretation, or another use where a concrete overclaim would change the next engineering move.

**Stop condition.** Do not create a new publication record merely because a face exists. Stop when the current face changes no next engineering move and blocks no concrete overclaim.

**Admissible publication-use examples.**

| Admissible publication use | Source-finding or bounded inspection with no downstream claim or effect | Non-admissible publication use |
| --- | --- | --- |
| A source-pinned MVPK face lets the team inspect one morphism, review it, exchange it, or prepare planning without changing the claim. | A face helps planning support, but the team still needs to recover the exact method, evidence, gate, control, or carrier source before work, evidence, gate, control, carrier, or other downstream use. | A face, screen, export, or diagram is treated as performed work, gate passage, evidence, engineering justification, supervisory relation or control relation, or release permission by layout or readability alone. |


**Boundary aid pointer.** If one encountered publication-facing item is easy to read as work, evidence, gate, approval, status, explanation, comparison, or narrower-use rendering, handle one live claim or effect at a time using `E.17:5.1d`.

Here in the first-screen read, keep only the MVPK publication move: one source-pinned face, one admissible publication use, and exact neighboring FPF patterns or typed downstream values only as far as the current use needs.


**Not this pattern when.** Not this pattern when the live issue is performed `U.Work`, a work plan, evidence path, provenance path, engineering justification, gate decision, control architecture, carrier work, OCR work, or a narrower-use rendering that needs its own source-bearing return. Use the exact FPF pattern that governs that issue.

> **Tech‑name:** `U.MultiViewPublicationKit` (**MVPK**)
> **Plain‑name:** Multi‑view publication kit. The morphism-publication profile is the canonical formal profile.
> **General publication-face form:** one MVPK face is a `U.View` emitted over one source `U.Episteme` or episteme-lane `U.View`, under one publication `U.Viewpoint`, one `U.PublicationScope`, declared pins where needed, one face kind, and one admissible publication use. The face adds no claim by readable form. Evidence use, authority use, gate use, work use, release use, and engineering-justification use require the exact neighboring FPF pattern and typed project-side value/reference that carry that downstream use, such as a `GateDecision`, evidence path, work occurrence, status source, or authority-reference relation.
> **Canonical morphism profile (conceptual form):**  `MVPK : (U.Morphism, Σ_viewpoints) ↦ U.ViewFamily` with per‑viewpoint components
> `ViewObj_s : U.Object → U.ViewObj_s` and `Emit_s(-) : U.Morphism → U.ViewMorph_s`,
> such that `(ViewObj_s, Emit_s)` forms a functor `U → View_s(U)`. For each `s ⪯ t`, a **reindexing coercion**
> `PromoteView[s→t]_X : ViewObj_s(X) → ViewObj_t(X)` exists and is **natural in `X`**: for every `f : X → Y`,
> `PromoteView[s→t]_Y ∘ Emit_s(f) = Emit_t(f) ∘ PromoteView[s→t]_X` (see Rules §6.2).
> **Notation:** `Σ_viewpoints` is abbreviated as `Σ` where convenient.
> **Twin‑register aliases (naming discipline):**
> • **Tech:** `Emit_PlainView`, `Emit_TechCard`, `Emit_InteropCard`, `Emit_AssuranceLane`; `PromoteView[s→t]_-`.
> • **Plain:** `PlainView(x)`, `TechCard(x)`, `InteropCard(x)`, `AssuranceLane(x)`; “Promote to *t*”.

> **USM binding (overview):** `PublicationScope` is a **USM‑class** object that parameterizes MVPK; see §5.0.
> **Episteme lane.** MVPK treats each face as a `U.View` in the sense of C.2.1 and E.17.0 (species `U.EpistemeView`). For any MVPK face, the source is a named `U.Episteme` or episteme-lane `U.View`; the face declares a publication `U.Viewpoint` (`PublicationVPId`) drawn from a `U.ViewpointBundle` (E.17.1 and E.17.2). In the morphism profile, every `Emit_s(f)` has `DescribedEntitySlot` and `DescriptionContext` target `f : U.Morphism`. In a non-morphism publication, the face names the exact source episteme, episteme-lane view, described entity, or claim relation that the face publishes, and no functorial composition claim is live unless the corresponding FPF pattern supplies it. Slot discipline (`ViewSlot` and `ViewRef`) is inherited from C.2.1 and A.6.5 and is not redefined in MVPK.

### E.17:1 - Intent

Provide a disciplined way to publish one source episteme or episteme-lane view across multiple didactic faces without adding semantics, while keeping publication viewpoints explicit and auditable. The canonical formal profile is morphism publication: a small view-pack applied to any `U.Morphism`, including compositions, yields a family of views that commute with arrow composition and respect edition and measurement pinning.

### E.17:2 - Problem frame

* Teams routinely need several **faces** of the *same* arrow: a **`TechCard`** for the catalog, an **`InteropCard`** for machine exchange, a **`PlainView`** for narrative, and an **`AssuranceLane`** for evidence.
* Informal “renderings” quietly **drift semantics**; **composite arrows** are often published piecemeal, breaking traceability; **evidence** forgets unit, scale, and edition pins.
* “View” and “viewpoint” are **blurred** in practice; authors conflate **publication** with **mechanism**.
* L‑SURF requires **`SurfaceKind` token discipline**; Core allows only **PublicationSurface** or **InteropSurface**; faces are named **...View**, **...Card**, or **...Lane** (no ad‑hoc `...Surface` kinds).

**MVPK** fixes this by making publication a typed projection from existing source epistemes or episteme-lane views via species of `U.EpistemicViewing` subject to explicit viewpoint specs and pinning guards. In the morphism profile, this projection is the functorial D and S episteme publication discipline described below. **Part E is conceptual:** no machine-exchange formats are specified here.

### E.17:3 - Problem

1. **Semantic drift in publication.** Unchecked “presentations” introduce claims not present in the D-side or S-side epistemes about the arrow (epistemes with `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` in the sense of E.10.D2 and E.17.0).
2. **Non‑compositionality.** Publishing `g∘f` yields faces that do not match composing the faces of `f` and `g`.
3. **View vs viewpoint confusion.** A single template is treated as “the view”, with no declared concerns or conformance rules.
4. **Unpinned numbers.** Numeric claims lack unit, scale, reference‑plane, and **edition pins** from Part F or Part G, undermining auditability.

### E.17:4 - Forces

| Force | Tension |
| --- | --- |
| **Compositionality vs legibility** | Preserve arrow invariants across views ↔ keep each view didactic and audience‑appropriate. |
| **Neutral naming vs domain idioms** | Use vocabulary stable across domains ↔ allow local templates (SOPs, APIs, checklists). |
| **Publication-face independence (A.7)** | Publication must not mutate I-, D-, and S-semantics ↔ authors expect rich presentations. |
| **Evidence discipline** | Views must cite CG‑Spec and CHR anchors ↔ authors want compact cards. |

### E.17:5 - Solution — the **MVPK Kit**

#### E.17:5.0 - USM anchoring (normative)
* **PublicationScope (USM).** `U.PublicationScope` is defined in **USM** (A.2.6 §6.5) analogously to `U.WorkScope` and `U.ClaimScope` as a **set‑valued scope object** over `U.ContextSlice`. In MVPK, every emitted `U.View` SHALL declare a `U.PublicationScope` that bounds where that face is admissible.
  * **Non‑overload rule.** `U.PublicationScope` MUST NOT encode viewpoint choice, MVPK profile selection, or Publication Characteristics (PC); those are governed by `PublicationVPId`/`U.Viewpoint` and MVPK profile rules (§5.1/§5.2/§5.5).
* **Scope lineage.** `U.PublicationScope` participates in the same USM lineage regime as `U.WorkScope`/`U.ClaimScope` (Δ‑moves, editioning and migration rules); MVPK emits faces **under** a declared `PublicationScopeId`.
* **MVPK profile (kit configuration).** The canonical MVPK profiles (MVPK‑Min, MVPK‑Lite, MVPK‑SetReady, and MVPK‑Max) fix:
  * (a) the **viewpoint index** `Σ` and its partial order `⪯`,
  * (b) the admissible **Publication characteristics (PC)** and required **pinning requirements**,
  * (c) any cross‑Context or cross-plane constraints (Bridge and CL policies) applicable to emitted faces.
* **MVPK face-name quartet.** The canonical MVPK-Max profile enumerates exactly four **face kinds**: `PlainView (P)`, `TechCard (T)`, `InteropCard (I)`, `AssuranceLane (A)`. MVPK face ids, `SurfaceKind` values, claim quadrants, `governingPatternRef`, and local field values must not use an L-, P-, D-, and E-mnemonic; use the P-, T-, I-, and A-face-name initials only when an abbreviation is unavoidable.

#### E.17:5.1 - Terminology (normative)

* **View** (`U.View`): an episteme-lane view (`U.EpistemeView` in the sense of C.2.1 and E.17.0) produced under a publication viewpoint. In MVPK each face (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) is such a `U.View`. In the morphism profile its `DescribedEntitySlot` and `DescriptionContext` target is a `U.Morphism`; in a non-morphism publication, the target is the exact source episteme, episteme-lane view, described entity, or claim relation named by the source.
  Every MVPK `U.View` **SHALL** declare:
  `SurfaceKind ∈ {PublicationSurface, InteropSurface}`, `PublicationVPId : U.ViewpointRef`, references to the underlying D epistemes and S epistemes produced by `Describe_ID` or `Specify_DS` in `A.7` and `E.10.D2`, and a `U.PublicationScope` (USM §6.5).
  Any carrier rendering is separate **`U.Work` on SCR and RSCR carriers** and is not part of `U.View`.
* **Publication vs presentation vs rendering vs representation (guard):**
    * **Publication** = typed projection from existing source epistemes or episteme-lane views into a `U.View` governed by a `PublicationSurface` or `InteropSurface` `SurfaceKind` via species of `U.EpistemicViewing` (`A.6.3`). In the morphism profile, the source epistemes are the D and S epistemes about a morphism under the I, D, and S discipline of `A.7` and `E.10.D2`.
    * **Presentation** = rhetorical arrangement of a published carrier; **notation-neutral**, adds no claims and is **not** a `SurfaceKind`.
    * **Rendering** = display layout of a carrier, purely graphical formatting; **`U.Work` on carriers** (A.7), not a `SurfaceKind`.
    * **Representation** = episteme↔referent relation (`C.2.1`, `A.6.2` through `A.6.4`); **not** a publication operation and not a `SurfaceKind` operation. Use **publication** and **view** here; treat presentation and rendering as **`U.Work` on carriers** (`A.7`).
* **ISO mapping note.** ISO **viewpoint** → `PublicationVPId` (publication lane); **engineering viewpoint** → `EngineeringVPId` (E.TGA E.18:5.12). An ISO **view** may be a single MVPK face; “bundles” are packaging only.
* **No‑mechanism equivalence:** MVPK **is not** a mechanism; any operational activity, such as build, render, or upload work, is **separate `U.Work` by a system on carriers** (A.7; see **Rule 5 — No Γ-leakage** in §6).
* **ViewpointSpec (`U.Viewpoint`)** — a typed specification that declares stakeholders, concerns, conformance rules, allowed **Publication Characteristics**, and pinning requirements per profile. The index set `Σ` consists of identifiers of `U.Viewpoint` instances, typically drawn from `U.ViewpointBundle` species (E.17.1 or E.17.2) (see §5.3).
* **Explanation-use profile values.** Existing faces may state an explanation-use profile value as `SourcePinnedExplanation`, `SourceLinkedExplanationReconstruction`, `DidacticRetelling`, or `SpeculativeRetelling`, but those are local profile values over already existing MVPK faces rather than new face kinds, explanation kinds, or carrier-rendering kinds. Per-face pins, provenance anchors, and no-new-A.6.B-boundary-claims discipline still apply.

#### E.17:5.1a - Episteme-publication lane binding  *(normative)*

For functional-description publications, MVPK governs the publication lane only.

**Publication lane.** A principle scheme, functional diagram, comparison table, screen, export, scenario, explanation, or code-like method description may support interpretation, source-finding, comparison, selected-method inspection, or work-planning support.

**Unsupported neighboring claims.** The publication does not by itself assert performed `U.Work`, gate passage, evidence, engineering justification, supervisory relation or control relation, release permission, or a new TGA kind.

**Interface and protocol proximity.** When interface, protocol, schema, boundary, or API wording appears beside a functional-flow description, keep the operational boundary, interface, or protocol claim with its own project claim set and exact typed project-side value and reference, governed by the relevant FPF pattern such as `A.6.B`, `A.6.C`, or `E.18`. Do not absorb it into the functional-flow publication by layout proximity.

**Retargeting.** If the publication changes the governed target from an already described component, process, material `U.Entity`, or source claim into a functional, control, or flow architecture claim, this is not a same-entity publication-use change. Use `A.6.4`, `OntologicalReframing`, or `E.18` as applicable.

**Source recovery.** When a requested use requires an exact typed project-side value and reference beyond the publication face, the engineer first recovers the corresponding existing project-side FPF value if one already carries the needed claim:

- work-relevant source restoration under `A.15.4`;
- project `U.Method`, `U.WorkPlan`, or work-result record under `A.15`;
- evidence and provenance path under `A.10`;
- engineering-justification record under `B.3`;
- constraint or gate decision under `A.20` or `A.21`;
- supervisory or control architecture record under `B.2.5`;
- carrier, export, OCR, or front-end record under `A.7`;
- same-entity textual relation under `A.6.3.CR`;
- representation relation under `A.6.3.RT`;
- reduced-use-rendering relation under `A.6.3.CSC`.

**No backdating.** If no existing exact typed project-side value and reference carries a claim that was supposed to be already supported, do not create a backdated source. Create only a prospective repair request, decision request, future work-plan entry, or explicit source-gap note, and treat the earlier claim or effect as unsupported until the required source exists.

Ordinary orientation and source-finding can stay as an inline note.

**Functional-description guard (`CC-MVPK-FD`).** A functional-description publication face must separate the source `U.Episteme` or episteme-lane `U.View`, the MVPK face, any live carrier or rendering work, the admissible engineering use, and non-admissible neighboring use. The guard applies only when a functional-description face is present; it is not the first universal MVPK conformance gate.

MVPK inherits the C.2.1 distinction between `U.Episteme`, `U.EpistemePublication`, publication form, `U.View`, carrier, and authority-reference relation. MVPK does not introduce a generic semio kind and does not let a publication face act as `governingPatternRef`, `authoritySourceRef`, or the source claim for a claim.

When a morphism publication is encountered or reused, name the relevant lane before relying on it:

* the underlying `U.Episteme`, `D` episteme, or `S` episteme whose ClaimGraph is being projected;
* the `U.EpistemePublication` or governed `U.Episteme` publication when the episteme is available as a published episteme;
* the publication form used by the local pattern, if one is live;
* the `U.View`-typed MVPK face (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) that renders the publication for a viewpoint;
* the SCR/RSCR carrier or rendering work that holds or displays it;
* the exact typed project-side value and reference or authority-reference relation when the next work or reliance claim depends on that named authority-reference relation, approval source, gate source, release source, or exact typed project-side value and reference.

The practical payoff is that a reader can recover exactly what may be relied on: the episteme claim, the published form, the view, the carrier, the exact typed project-side value and reference, or the authority-reference relation. A dashboard tile, generated explanation, card face, credential view, or carrier can guide source-finding, but it does not by itself become the source claim or effect, gate decision, evidence relation, assurance claim, role or status, work occurrence, or permission.

**Source-exposure rule.** A publication face, carrier, rendering, dashboard tile, credential view, status view, comparison unit, explanation rendering, signed decision memo, release decision record, approval speech-act publication, or gate dashboard may expose, cite, or carry an exact typed project-side value and reference only when that value is recoverable under its governing FPF pattern and exact source relation. It does not become that value by readability, layout, title, color, fluency, proximity, copying, generation, or reuse. When the exposed value is a real `SpeechAct`, `GateDecision`, evidence path, credential source, status source, `U.Work` occurrence record, `U.Episteme`, or `U.EpistemePublication`, rely on that typed and recoverable value and its FPF-governed source relation; otherwise treat the face, carrier, display, or rendering as orientation or source-finding only.

**No retroactive source creation.** When required source support is missing, a new entry can be only a prospective repair request, future decision request, prospective work-plan entry, or explicit source-gap note. It must not be read as earlier evidence, approval, gate passage, instituting speech act, `U.Work` occurrence, release permission, engineering justification, or assurance for the unsupported past claim or effect.

#### E.17:5.1b - Shared source-support posture vocabulary

Use this vocabulary when a publication face, rendering, generated text, comparison note, narrower-use rendering, source-finding cue, or authority-looking display may be over-read as carrying wider source support than it actually carries. The vocabulary names support posture for one claim or use. It does not instantiate evidence, gate, assurance, work, commitment, speech act, decision, release, or authority.

| Source-support posture | Meaning for the local claim or use |
| --- | --- |
| `source-pointer-only` | The item points to a possible source but does not show that the source is available, was used, or supports the claim. |
| `source-support-unknown` | The item does not yet show whether the needed source relation exists or supports the local claim. This blocks the downstream use until checked; it does not show that the underlying world claim is false. |
| `source-support-not-needed` | No operative work, reliance, evidence, gate, assurance, bridge, source-dispute, release, or durable-naming claim is live for this item. Orientation, learning, source-finding, review, or planning preparation may proceed without inventing source support. |
| `source-not-recoverable-here` | The needed source relation may exist elsewhere, but it is not recoverable from this publication-facing item or its stated source anchors. Treat the item as orientation or source-finding only, or reopen the source-bearing side. |
| `source-support-absent` | The needed source relation is known absent from the current item and available source set for the stated use. Block that use; do not infer that the underlying world claim is false merely from this absence. |
| `source-available` | The cited source can be recovered or inspected for the current use. This does not yet show that the rendering used it correctly. |
| `source-retrieved` | The cited source has actually been recovered for the current check. This still does not show that it was used correctly or supports the local claim. |
| `source-used` | The inspectable generation, rewrite, rendering, comparison, work, or reliance source-use relation actually used the named source rather than only similar background. If that relation is unavailable, treat the item as pointer-only or orientation-only until a source-use relation is recovered. |
| `source-faithful` | The item stays within the source claim relation or source support relation for the stated use; omissions, declared source-loss modes, and additions are visible enough to inspect. |
| `claim-supported` | The local claim is recoverable from the source, declared correspondence support, or required exact typed project-side value and reference for the stated use. |
| `claim-unsupported` | The local claim is not recoverable from the source support currently available. |
| `claim-contradicted` | The local claim conflicts with the available source support. |
| `claim-plausible-only` | The claim may sound reasonable, but the source support currently available does not carry it. |
| `source-omitted` | Relevant source claim, source passage, qualifier, condition, alternative, caveat, or uncertainty is missing from the item. |
| `source-loss-declared` | The item declares a source-loss mode such as omitted-detail, qualifier-loss, redaction, aggregation, scope-narrowing, recoverability-loss, representation-factor-loss, or coarsening-loss for the local source-to-rendering relation. |
| `claim-widened` | The item turns a source possibility, hypothesis, bounded condition, low-confidence statement, narrower permission, or source-finding cue into a wider claim or use. |
| `added-linkage` | The item adds a causal, explanatory, bridge, comparison, work, evidence, gate, or authority relation not already carried by the source support. |
| `independent-verification-present` | A separate check supports the local claim or use independently of the item only through a named governing pattern and exact record, such as an `A.10` evidence path, `B.3` assurance claim, `A.21` `GateDecision`, `A.20` constraint profile, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, or `F.9` Bridge Card. |
| `admissible-for-this-use` | The item is admissible for the named use only; wider downstream use still needs the exact neighboring FPF pattern and exact typed project-side value and reference. |
| `downstream-use-forbidden` | The item must not be used for the named downstream claim or effect because the needed source support is absent, source-loss-declared, contradicted, or outside scope. |
| `reopen-trigger-present` | A stated change, dispute, use escalation, source update, context shift, missing support, or contradiction forces return to the source-bearing side or to the governing FPF pattern and exact typed project-side value and reference. |

Patterns may use shorter local field names such as `sourceSupportPosture`, `explanationSourcePosture`, or `representationValiditySupportPosture` when the local object is clear. Comparative patterns split source-support posture from comparative-relation posture instead of using one overloaded field. The local field must still be interpretable through the vocabulary above, and the admissible use must be named beside it when downstream reliance could change.

For ordinary use, only name the posture distinction that changes the next admissible use. The common light states are `source-pointer-only`, `source-support-unknown`, `source-support-not-needed`, `source-not-recoverable-here`, `admissible-for-this-use`, `downstream-use-forbidden`, and `reopen-trigger-present`. The vocabulary is not an ordered scale, maturity ladder, source-record taxonomy, authority-reference source taxonomy, or project-side support substitute. If source support is missing from the publication-facing item, only the unsupported downstream use is blocked; the missing support does not by itself prove the underlying world claim false. If `independent-verification-present` is relied on, name the separate governing pattern and exact record that performs that independent support: `A.10` evidence path, `B.3` assurance claim, `A.21` `GateDecision`, `A.20` constraint profile, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, or `F.9` Bridge Card.

#### E.17:5.1c - Shared use-boundary terms

Use these terms when a publication face, rendering, narrower-use rendering, explanation, comparison note, source-finding cue, or authority-looking display may be read beyond the support it carries. Define them once here and link back to this section from local patterns instead of minting local synonyms.

| Term | Meaning for FPF use |
| --- | --- |
| `orientation use` | The item helps a reader find, inspect, triage, compare, teach, discuss, or prepare planning while the item itself does not support a downstream work, reliance, claim, or effect. |
| `reliance use` | The item is used as support for an engineering claim or effect that changes a next work or reliance move, such as method choice, work plan, performed-work claim, release, gate, approval, role or status, evidence, assurance, or external-impact move. |
| `work, reliance, claim, or effect` | A claim or instituted effect about method selection, selected method, `U.WorkPlan`, performed `U.Work`, work result, gate or release, role or status, evidence, assurance, boundary or policy effect, or another exact typed project-side value and reference. |
| `operative claim` | A claim whose acceptance would change the next admissible work or reliance move, the exact typed project-side value and reference to recover, or the cross-context use of the item. Explanatory prose, examples, and source-finding cues are not operative claims unless they are used that way. |
| `non-admissible downstream use` | A wider use that the current item source relation does not carry. It requires narrowing the use, returning to the source-bearing side, recovering source support, or using the exact neighboring FPF pattern and exact typed project-side value and reference that governs the wider claim or effect. |
| `reopen trigger` | A dispute, use escalation, missing, stale, or contradictory source support, source update, context or window change, or wider claim or effect that requires source-bearing return, source refresh, re-expansion, or use of the governing pattern. |
| `authority-looking case` | A recognition phrase for an encountered item that may be over-read as permission, approval, evidence, gate passage, role or status, work occurrence, assurance, or release support. It is not a `U.*` kind, not an exact typed project-side value and reference, and not a governing pattern. |

#### E.17:5.1d - Compact Boundary Aid For The Live Claim or Effect

When a publication-facing item, publication face, rendering, narrower-use rendering, explanation, comparison note, dashboard tile, credential view, status view, carrier, or generated item creates more than one possible reading, separate the live claim or effect being used now and cite the exact governing source relation for that claim or effect. This is a compact boundary aid, not a standing selection guide, project process order, software call path, or item taxonomy. The same encountered item may expose several typed records; handle one live claim or effect at a time instead of pretending there is one overall governing relation for the encountered item.

**Mixed-case precedence.** When several publication-use patterns appear possible, repair the smallest unstable reading that changes the current admissible use before applying a neighboring pattern whose claim or effect is live:

1. If one local head is the only unstable part, apply `E.17.AUD.LHR` or `C.2.P` and stop when the repaired sentence names the local kind, relation, and admissible use.
2. If the bounded `PublicationUnit` or its primary described-entity reading is unstable, apply `E.17.AUD` or `E.17.AUD.OOTD` before using `E.17.ID.CR` or `E.17.EFP`.
3. If the unit is stable and the live problem is comparison overread, apply `E.17.ID.CR`; use `F.9`, `C.11`, `A.20`, or `A.21` only when equivalence, recommendation, selection, decision, gate, or release claim is actually live.
4. If the unit is stable and the live problem is explanation overread, apply `E.17.EFP`; use `A.10`, `B.3`, `A.20`, `A.21`, or `A.15.4` only when evidence, engineering-justification, gate, release, work, or reliance claim is actually live.
5. If the live problem is a durable reusable name, UTS row, Core-facing term, or cross-context naming relation, apply `F.18`; otherwise keep the lighter local repair pattern.

| Live claim or effect question | Apply or recover |
| --- | --- |
| Is the item being used to guide a work or reliance move by appearance, while the acting user still needs the exact typed project-side value and reference before proceeding? | `A.15.4` for the restoration step; the recovered value may then be `A.15`, `A.15.1`, `A.10`, `B.3`, `A.20`, `A.21`, `A.2.8`, `A.2.9`, `A.6.B`, or another exact typed project-side value and reference. If that exact value is already the live question, use it directly. |
| Is the item being used as evidence, provenance, attestation, currentness, freshness, or claim-bound support? | `A.10` evidence, provenance, or currentness path for the exact claim. |
| Is the item being used as engineering justification, assurance, confidence, readiness, or limitations support? | `B.3` assurance or engineering-justification claim with evidence, limits, and decay explicit. |
| Is the item being used as gate passage, constraint validity, adjudication, or release decision support? | `A.20` or `A.21` project records, including gate profile, constraint profile, decision record, log reference, scope, window, replay support, and freshness support. |
| Is it the same described entity with textual restatement only? | `A.6.3.CR Conservative Retextualization`. |
| Is it the same described entity with representation scheme or reasoning medium changed? | `A.6.3.RT Representation Transduction`. |
| Is it deliberately reduced-use and useful only under narrower admissible use, non-admissible downstream use, and source-bearing reopen? | `A.6.3.CSC Controlled Semantic Coarsening`. |
| Is the primary issue explanation-facing rendering class on an existing MVPK face? | `E.17.EFP ExplanationFaithfulnessProfile`. |
| Is the primary issue one bounded comparative review unit over sources? | `E.17.ID.CR ComparativeReading`. |
| Did the described entity, target, ontology frame, or governed claim change? | `A.6.4`, `OntologicalReframing`, or the exact retargeting or reframing pattern. |
| Is the item being used as bridge, substitution, equivalence, "same", "equivalent", "align", or "map" wording, or cross-context comparison support? | Use Part F and `A.6.9` for repairing "same", "equivalent", "align", or "map" wording into explicit bridge work; use `F.9` or `F.9.1` for Bridge Cards, bridge kind, direction, `CL`, loss notes, admissible use, and stance overlays. Comparison alone is not a bridge. |
| Is the live question carrier, export, OCR, screen, front-end behavior, or work on carriers? | `A.7` and the exact carrier relation, front-end relation, or work-on-carrier record. |

**Evidence-path boundary.** An `A.10` evidence, provenance, attestation, freshness, or currentness path supports only the exact claim it instantiates. It does not approve or authorize work, pass a gate, perform work, supply release permission, or raise assurance or engineering-justification posture unless the exact typed project-side value and reference that carries that downstream claim is also instantiated, such as `A.15.4`, `A.15`, `A.20`, `A.21`, or `B.3`.

**Gate-display boundary.** A dashboard tile, status view, or release screen may expose a gate decision only when the `GateDecisionRef`, gate or constraint profile version, target release or work scope, time window, currentness, freshness or replay support, and evidence path are recoverable. Without that exact gate support, the display remains orientation or source-finding only; it is not a gate decision, gate passage, release permission, or performed-work record by color, label, layout, or proximity.

#### E.17:5.1e - Local review fields are not FPF kinds

Local review fields and values in CR, RT, CSC, EFP, ID.CR, or a neighboring publication-use pattern are local review aids for one case. They are not `U.Kind`, `SurfaceKind`, `RelationKind`, `KindBridge`, `EvidenceKind`, `SlotKind`, `GateDecision`, `SpeechAct`, `Commitment`, `U.Work`, publication face, `authoritySourceRef` target, or exact typed project-side value and reference unless another governing FPF pattern explicitly instantiates that object. When a local field starts carrying one of those downstream claims, cite or apply the governing FPF pattern and exact typed project-side value and reference that carry it.

#### E.17:5.1f - Shared anti-overread invariants for publication-facing items

Use the exact FPF pattern that governs the live claim or effect. Keep any local review field local, preserve reduced admissible use, and assign only the non-admissible wider claim or effect to its governing source relation.

**Source-relation minimality.** Name the smallest exact FPF source relation sufficient for the live use. A source pointer, source-exposure relation, evidence path, engineering-justification record, gate decision, and release decision are different FPF relations; choosing one does not license another. Do not apply `A.10`, `B.3`, `A.20`, or `A.21` when the live use only needs source finding, orientation, or inspection of an existing source `U.Episteme`, source `U.EpistemePublication`, or status-register entry.

**Local repair vs publication redesign.** A local epistemic precision repair is enough only when it can preserve the current publication face or `PublicationUnit` while fixing one head, boundary, source relation, admissible use, explanation class, or unsupported downstream claim. If layout, grouping, visual emphasis, comparison arrangement, generated explanation, hidden source limitation, or mixed described-entity packaging still induces overread after the local relation is repaired, create a redesigned publication face or `PublicationUnit` instead of adding warning text around the misleading form.

**Most-likely careful reading constraint.** Design and word a publication-facing item so its most likely careful reading does not exceed its named source relation, admissible use, and governing FPF pattern. A visible head such as `Approved` needs a visible `GateDecision` or a different head; a sorted comparison needs its comparator or sorting basis visible if no recommendation claim is intended; a generated explanation separates inferred links from pinned source claims by wording, label, or source anchor.

**Visual cue claim pressure.** Layout, order, color, prominence, icon, grouping, and proximity are carrier or front-end cues that can carry publication-move pressure even when the words do not. Green color may imply readiness, top position may imply preference, grouping may imply equivalence, proximity to evidence may imply support, a badge form may imply approval, and a lock or checkmark may imply verification. If the visual cue would make the reader treat the item as evidence, gate passage, decision, recommendation, reliance support, bridge support, or approval, recover the exact governing FPF pattern and exact project-side kind and reference, or redesign the publication face so the overread is no longer invited.


**Extraction survival.** When a `PublicationUnit` is excerpted, quoted, screenshotted, summarized, copied into a tutorial, retold by a generator, or moved to a slide, it keeps only the claims, source pins, boundary line, exact references, and admissible use carried in that extracted item. Any use that depended on hidden neighboring context is lost unless that context is carried by source pins, a boundary line, or an exact reference. A dashboard screenshot does not carry the underlying gate record, a quoted comparison row does not carry the full comparison basis unless the basis is included or referenced, a copied explanation paragraph does not carry source pins unless pins remain recoverable, and a pattern excerpt does not carry the whole pattern boundary unless the excerpt states or cites it.






**No-extra-pattern case.** If a publication-facing item only supports ordinary orientation, learning, source-finding, review, comparison, or planning preparation, and no operative work or reliance, evidence, gate, assurance, bridge, source-dispute, or release claim is live, keep the existing publication source relation and proceed with ordinary use. The visible closure may be: no operative work or reliance, evidence, gate, assurance, bridge, source-dispute, release, durable naming, or project-side support claim recovered; ordinary publication wording remains admissible for the current use.

**Pattern-inflation anti-pattern.** Do not apply a neighboring pattern merely because the publication-facing item resembles a worked example. Apply the neighboring pattern only when a live claim or effect changes the next admissible project move.

**Strategic overread invariant.** Apply the same anti-overread rules whether the misleading reading is accidental, conventional, incentive-driven, or intentionally induced by publication design. Green status color without `GateDecisionRef`, reviewed-looking wording without approval, selective source links without operative-claim support, comparison ordering without selection decision, hidden caveats behind a source link, or pins for trivial claims beside unpinned causal linkage do not create evidence, gate, decision, assurance, work, release, or bridge support by design pressure.

**Carrier-travel invariant.** A copied, exported, screenshotted, summarized, generated, translated, or re-rendered publication-facing item may carry orientation or source-finding cues. It does not carry evidence support, authority-reference support, gate passage, approval, engineering-justification support, work occurrence, currentness, or release support unless the governing FPF pattern and exact typed project-side value and reference remain recoverable for that exact use.

**Derivative-chain decay.** A second-order rendering inherits at most the admissible use that is explicitly carried from the prior source relation. It does not inherit source faithfulness, source support, currentness, authority-reference support, gate support, work support, or reliance support by default.

**Publication-face snapshot and refresh identity.** A publication face may keep the same visible layout, face name, or carrier while its source pins, source data window, source-support posture, freshness or currentness support, `EditionId`, or admissible use changes. Visual sameness across time is not source, evidence, or use-boundary sameness. When a refreshed, revised, translated, regenerated, screenshotted, or re-rendered face is used beyond orientation or source-finding, name the face edition or snapshot, the source pins or data window that still carry the claim, and any changed admissible use. If those cannot be recovered, treat the face as orientation or source-finding only, or reissue the face under the governing pattern before work, evidence, gate, assurance, release, or reliance use continues.

**Claim-level support only.** Do not assign one whole-item support posture unless every operative claim in that publication-facing item has the same support relation for the same use and non-admissible downstream uses are explicit.

**Modality and deontic-force preservation.** Publication-facing transformations must preserve possibility, obligation, permission, recommendation status, decision status, confidence, scope, and temporal window when those are load-bearing. If one of these changes, narrow the admissible use or apply the governing pattern that carries the changed claim or effect. Comparison does not become recommendation or decision; explanation does not become evidence; a publication face does not become authority; a publication unit does not smuggle a downstream effect; source-linked does not mean source-supported for reliance; ready-looking does not mean gate-passed.

This preservation rule also applies across extraction, translation, screenshotting, summary, and generated retelling. A translated permission is not wider permission, a screenshot of approval-looking display is not an approval record, a summary of evidence is not an evidence path, and a generated retelling of a decision is not the decision record unless the exact governing source relation and source pins survive in the new publication-facing item.


**Reader position is not project role.** Reader position, audience, target user model, verifier position, reviewer position, and learner position do not become project roles, role assignments, decision authority, gate authority, issuer roles, or work roles unless a typed project-side value and reference instantiates that role relation.

**Source-gap states.** When support is missing, say which gap is live: source not named; source named but unavailable; source available but not used; source used but insufficient; source stale or outside its window; source contradicted; source accountable role or register mismatch. Block only the unsupported effect and keep any reduced admissible use available.

**Measure and display overread.** A number, score, percentage, color, rank, confidence value, similarity value, dashboard state, or measurement display is orientation only until the measurement source, aggregation rule, validity window, population or scope, calibration or evidence path, and intended use are governed by the exact typed project-side value and reference. Evidence-like use applies `A.10`; assurance-like use applies `B.3`; gate-like use applies `A.20` or `A.21`; work or reliance use applies `A.15.4` and then the recovered exact typed project-side value and reference; bridge or substitution use applies `F.9` or `F.9.1`.


**World-contact stop.** Publication-facing items do not self-refresh after source update, revocation, policy change, system-state change, incident, model update, environmental change, or new external observation. A live outside change requires source refresh, reissued publication, or a new governed exact typed project-side value and reference before work, evidence, gate, control, carrier, or other downstream use continues.

**Functional-description boundary.** A functional, architectural, descriptive, representational, or explanatory fit claim does not create permission, obligation, approval, gate passage, release support, performed-work evidence, or engineering justification. Those uses require the exact neighboring FPF pattern and exact typed project-side value and reference.

**Mixed bundle no-shared-evidence-support rule.** A bundle with source-pinned, reduced-use, speculative, didactic, comparison, and evidence-facing parts cannot be read under one shared evidence-support class or admissible-use posture borrowed from another member. Each operative claim keeps its own source relation and non-admissible downstream use.

**Educational usefulness.** Didactic, onboarding, tutorial, and workshop usefulness is real orientation support. It is not evidence, gate passage, approval, work occurrence, engineering justification, release permission, or bridge support.

**Comparison exposes conflict; it does not adjudicate it.** A comparison note may expose contradiction, asymmetry, different foregrounding, or unresolved residue. It does not settle the conflict, select an option, approve release, pass a gate, or create bridge or substitution support unless the exact neighboring FPF pattern and exact typed project-side value and reference carry that result.

**Same publication-facing item, multiple readings.** A green release dashboard can be one MVPK face for source-finding, an `A.10` currentness path or evidence path when the evidence query is recoverable, an `A.21` gate-decision view when the `GateDecisionRef` is recoverable, or an unsupported release cue when those sources are missing. A generated comparative explanation can be an `E.17.EFP` explanation-use case, an `E.17.ID.CR` comparison case, a `A.6.3.CR` generated-summary case, or source-finding only; it is never all of those under one shared evidence-support class or admissible-use posture by fluency alone.

**Archetypal publication-use cases.** Use these as quick recognition slices, not as a closed taxonomy:

- **Green dashboard tile.** A tile says `Model ready`. Treat the tile as the `PublicationUnit` when that tile carries the live release overread. The useful action is source-finding and status orientation unless an exact `GateDecisionRef`, gate profile, source relation, and evidence or currentness support are recoverable. Without those, the tile is not release permission or gate passage by green color or placement.
- **Generated explanation with source links.** A generated text explains a method and cites sources. The explanation rendering is not source replacement. Source links support only the pinned operative claims they actually carry. If work or reliance is live, use `A.10` for the exact evidence path or keep the rendering as reader help; if the rendering is deliberately reduced-use, use `A.6.3.CSC`.
- **Comparison table.** A table compares two methods and places one first. Ordering is not selection. The comparison basis, source anchors, shared review frame, and unsupported downstream claim remain visible. Choice or decision needs `C.11`; equivalence or bridge support needs `F.9` or `F.9.1`.
- **Unrecovered source wording.** A draft uses source-object wording, undeclared interpretive-view shorthand, or generic unit wording without naming the FPF kind. Recover the FPF kind stack instead of minting support-object pseudo-kinds or undeclared interpretive-view pseudo-kinds. Use `PublicationUnit` only when a bounded reader-inspected unit inside a publication is live; otherwise use the exact episteme, view, publication, carrier relation, section of a named non-pattern FPF publication form whose support function and reference are recoverable, `A.6.P` relation claim, or exact typed project-side value and reference.

- **Translated tutorial.** A translated tutorial may improve reader access to an FPF pattern. It is a derivative rendering, not the original source. Operative claims need source mapping for reliance, translated heads may need `E.17.AUD.LHR` or `C.2.P`, and `F.18` is live only when durable naming, UTS, Core-facing, or cross-context naming work is intended.

**Practical harm prevented by neighboring pattern.** Use this map when the reader asks what the discipline buys in practice:

**Blocked overread with useful action remaining.**

- A comparison table appears to select option B. Block the selection reading when no `C.11` `ChoiceResult`, decision record, or visible selection basis exists. Useful action remains: use the table as a bounded comparison under `E.17.ID.CR`, or apply `C.11` when selection is intended.
- A green dashboard tile appears to permit release. Block the release or gate-passage reading when no `GateDecisionRef`, gate profile, evidence or currentness support, and source relation are recoverable. Useful action remains: use the tile for source-finding and status orientation, then inspect the exact gate or evidence source if release work is intended.
- A generated explanation appears to prove a causal relation. Block the evidence or assurance reading when source pins and evidence path are absent or insufficient. Useful action remains: use the explanation as reader help or source-finding, then apply `A.10` or `B.3` only for the exact evidence or engineering-justification claim they govern.


- `C.2.P` prevents the wrong object from being treated as source, the wrong relation from being treated as support, and a loose phrase from being treated as an FPF kind.
- `E.17.AUD` and `E.17.AUD.OOTD` prevent action on a publication unit whose primary described entity, carried publication move, or outside boundary shifted silently.
- `E.17.ID.CR` prevents a comparison unit from being used as decision, equivalence, bridge, evidence, or release basis.
- `E.17.EFP` prevents fluent explanation from laundering unsupported claims into reliance, assurance, gate, or evidence use.
- `E.17` MVPK prevents a readable publication face from being treated as evidence, gate, work, authority, or release support by display quality.
- `F.18` prevents a local name from becoming global identity without context, kind, lineage, and bridge or cross-context naming support.

**Anti-escalation examples.** Do not apply a neighboring pattern when its live claim is absent:

- Do not apply `F.18` when a one-off local phrase repair restores the local kind, relation, and admissible use without minting a durable reusable name.
- Do not apply `A.10` when the publication-facing item is not being used for reliance, evidence, provenance, currentness, or claim-bound support.
- Do not apply `A.21` when a dashboard tile is merely status orientation and no `GateDecisionRef` or gate profile is live.
- Do not apply `F.9` when a comparison does not claim sameness, substitution, bridge support, or cross-context equivalence.
- Do not apply `E.17.EFP` when the text is only a same-entity rewrite or representation change governed by `A.6.3.CR` or `A.6.3.RT`.

**Concrete reopen trigger.** A reopen trigger must name the condition and the nearest source-bearing side or governing pattern. A vague "reopen if needed" does not preserve source support.

#### E.17:5.2 - Allowed `SurfaceKind` values at Part E (L-SURF discipline)
Part E restricts `SurfaceKind` values to **PublicationSurface** and **InteropSurface**. Concrete publication faces SHALL be named **...View**, **...Card**, or **...Lane**.

**USM linkage (normative).** Every `U.View` **SHALL** declare a `U.PublicationScope` (USM §6.5).
For a view **about an episteme** `E`: `PublicationScope(view_E) ⊆ ClaimScope(E)`.
For a view **about a capability** `C`: `PublicationScope(view_C) ⊆ WorkScope(C)`. This is the publication scope of a capability description, not permission to perform work and not evidence that work occurred. Work admissibility still requires `A.15.4` source restoration when the view is used for work or reliance, and the `A.15` role, method, plan, and work source relation for the actor, target, context, scope, and time window in use.
Cross‑context views **SHALL** cite Bridge + CL; **CL penalties apply to R only** (scope membership unchanged).

**L‑PUBSURF naming discipline**
 * Allowed `SurfaceKind` values: **PublicationSurface**, **InteropSurface**.
 * Concrete faces MUST be named **...View**, **...Card**, or **...Lane**.
* The tokens **carrier, bearer, and holder** MUST NOT name a `U.View` or any publication entity.
  Use **`U.View`** (PlainView, TechCard, InteropCard, or AssuranceLane) for conceptual publication faces.
  Reserve **carrier** exclusively for **SCR/RSCR** (symbol, document, or data carriers) and **`U.Work` on carriers**.
* Avoid geometric metaphors such as axis or dimension for publication forms; use **Characteristic** or **CharacteristicSpace** only when referring to CHR‑MM entities.
* **Non‑collision guard.** `ViewFamilyId` (lexical tag for viewpoint families) MUST NOT be used to name any `U.View` or `SurfaceKind`; MVPK face kinds remain **{PlainView, TechCard, InteropCard, AssuranceLane}** only.

**MVPK‑Max viewpoints (normative; exactly four; governed by the MVPK profile):**
* `PlainView` (explanatory prose view)
* `TechCard` (typed catalog card)
* `AssuranceLane` (evidence bindings and lanes)
* `InteropCard` (conceptual interoperability view; **mapping to concrete exchange formats lives in the interop annex; Part E does not specify schemas**)

`AssuranceLane` may expose evidence bindings, evidence-carrier references, pins, and presence bits. It is not a `B.3` assurance claim, readiness or confidence verdict, engineering-justification record, or evidence-sufficiency result. When a published face is used to raise or lower assurance, readiness, confidence, limitation, or engineering-justification posture, the governing source relation is `B.3`; the lane only helps recover the cited evidence bindings.

**Lean profiles (small‑team friendly, optional; as MVPK kit profiles):**
* **MVPK‑Min (F0–F1):** Σ = {`PlainView`, `TechCard‑Lite`}. `AssuranceLane` omitted. No interop face.
* **MVPK‑Lite (F1–F3):** Σ = {`PlainView`, `TechCard‑Lite`, `AssuranceLane‑Lite` gated by crossing trigger}. `InteropCard` only if external consumers exist.
* **MVPK‑SetReady (F3–F5):** add `InteropCard` when replayability or external interchange is required (details outside Part E).
* **Profile‑upgrade triggers:** (i) cross‑Context reuse or ReferencePlane crossing; (ii) QD replay needs or OEE replay needs; (iii) external consumption.
* **“‑Lite” variants (definition):** A *‑Lite* face removes optional fields only (never claims), keeps the same typing as its full counterpart, and MUST retain pins for any numeric content. Upgrading from *‑Lite* to full is a monotone **add‑fields** operation (no retractions).

#### E.17:5.3 - The kit (constructs)

1. **Object component** `ViewObj_s` for each viewpoint (see §5.1), to make types explicit.
2. **Viewpoint set** `Σ : FinSet(U.Viewpoint)` with declared **partial order** `⪯` for formality or refinement (default chain: `PlainView ⪯ TechCard ⪯ InteropCard`; `AssuranceLane` is an **independent evidence-binding face** and not ordered with respect to others).
3. **Emitters** `Emit_s(-) : U.Morphism → U.ViewMorph_s` (one per `s ∈ Σ`).
4. **Coherence** (rules and invariants §6) + **Pin Characteristics** policy (UnitType, ScaleKind, ReferencePlane, and EditionId) for any numeric or comparable content, grounded in CHR and UNM.
5. **Interop anchors (conceptual)** for `InteropCard` (concerns and semantics only); **any concrete schema or exchange mapping is outside Part E** (Annex or Interop).

**Result:** `MVPK(f, Σ)` returns `U.ViewFamily(f)` whose components are `Emit_s(f)`. Reindexing across `s ⪯ t` is mediated by total view-object coercions `PromoteView[s→t]_X` (see §6.2).

#### E.17:5.4 - Intensional Input and Output vs Publication (normative convention)
1) **Input and Output are intensional.** The **Input and Output** sections of a morphism describe **intensional** data types (I, D, and S) only; they do **not** depend on any publication face.
2) **No duplication on faces.** MVPK faces **do not duplicate** Input and Output lists; they publish a **minimal profile**: **presence‑pins**, **CG‑Spec and CHR anchors**, and **EditionId** only.
3) **Signature reserved to intensional.** Use **“Signature”** exclusively for intensional objects (`U.Signature`, `U.PrincipleFrame`, …). On faces, avoid “signature” and use **TechName** or **PlainName**.
4) **Admissible orders, return sets.** Whenever a face shows **selection or comparison**, it **returns sets or admissible partial orders** and **never hides scalarization**; cite a **ComparatorSetRef** for any total order.
5) **Bridge crossing penalties.** Crossings cite **Bridge and CL**; publish **Φ(CL)** and **Φ_plane** ids; penalties apply to **R only** (never F or G).
6) **Carrier anchoring and lanes.** On first mention, anchor carriers (**SCR/RSCR**); keep **Work occurrences** distinct from **epistemic claims** via lanes.
7) **Publication ≠ execution.** No time or resource semantics on faces; any build, render, or upload work is separate **`U.Work`**.

#### E.17:5.5 - Pin & Publication characteristics (normative; never “axes”)
**Intent.** Make pinning and publication-time measurement claims explicit, typed, and auditable without importing geometric metaphors. This section introduces **Publication characteristics** (PC) as CHR-grounded, publication-facing facets that can admissibly appear on MVPK faces.

**Terminology (aligned with CHR‑MM & UNM).**
* **Characteristic** (`U.Characteristic`): a measured aspect as defined in CHR‑MM (entity characteristic or relation characteristic with a chosen **Scale**).
* **CharacteristicSpace** (`U.CharacteristicSpace`): a CHR‑typed product of slots used by dynamics and measurement theories (A.19).
* **Publication characteristic** (`U.PubCharacteristic`, **PC**): a **declarative facet** that a view, card, or lane may expose *about a morphism* under a stated **Viewpoint**. Each PC is **backed by** CHR and CG‑Spec publications and **pinned** by unit, scale, reference‑plane, and edition. PCs are **not** geometry and do **not** define “axes”.

**PC catalog (initial set).** MVPK defines a minimal open set of PCs that are frequently shown on publication faces:
* **PC.Number** — numeric or comparable entries (thresholds, budgets, counts). **Pins required:** unit, scale, reference‑plane, edition.
* **PC.EvidenceBinding** — bindings to evidence carriers and policies (e.g., PathSliceId, BridgeId, CL notes).
* **PC.ComparatorSetRef** — an explicit comparator family for admissible partial orders on faces.
* **PC.CharacteristicSpaceRef?** — optional pointer when a face needs to cite the **space** in which a claim is interpreted (e.g., dominance on a declared space).
The catalog **MAY** be extended (see “Extensibility” below); PCs **must** remain declarative (no embedded mechanisms).

**Norms (E17‑PC).**
* **E17‑PC‑1 (CHR grounding).** Every PC that yields numeric or comparable content **SHALL** cite CHR and CG‑Spec anchors and carry pins {unit, scale, reference‑plane, edition}.
* **E17‑PC‑2 (Lexical discipline — no geometry).** Faces and PCs **MUST NOT** use “axis”, “dimension”, or geometric metaphors; use **Characteristic**, **slot**, **CharacteristicSpace** where applicable (**E.10**; see also A.19).
* **E17‑PC‑3 (No hidden arithmetic).** Faces **MUST NOT** smuggle aggregation or normalization; any such logic lives in **CG‑Spec** (UNM or NormalizationMethod) and is cited by **…Ref.edition**.
* **E17‑PC‑4 (Plane & crossing).** When a PC depends on **ReferencePlane** or crosses ReferencePlane crossings or Context crossings, the face **SHALL** cite `BridgeId` and **CL** policy‑ids; penalties apply to the **R‑channel only**.
* **E17‑PC‑5 (Edition pinning).** PCs that rely on maps or distances **SHALL** pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and, if used, both `CharacteristicSpaceRef.edition` and `TransferRulesRef.edition`.
* **E17‑PC‑6 (Viewpoint scope).** Each PC instance declares the **Viewpoint** under which it is valid; promotion `PromoteView[s→t]` **MUST NOT** add or widen claims; at most, it reindexes or annotates.
* **E17‑PC‑7 (Comparator or SetSemantics edition).** `PC.ComparatorSetRef` and any `SetSemanticsRef` **SHALL carry edition identifiers**; cards MUST be re‑emitted upon edition change with migration notes.

**Publication faces and responsibilities.**
* **PlainView** MAY include **PC.Number** iff fully pinned; otherwise it uses **compare‑only** language.
* **TechCard** SHOULD carry **PC.Number**, **PC.ComparatorSetRef**, and **PC.CharacteristicSpaceRef?** when faces enable admissible ordering.
* **AssuranceLane** SHALL carry **PC.EvidenceBinding** and the pins for any numeric claims it relays.
* **InteropCard** MAY reference PCs conceptually but SHALL remain notation‑neutral in Part E (schemas map in the interop annex).

**Rationale.** MVPK is a publication discipline, not a measurement calculus. By naming **Publication characteristics** and pinning them to CHR and UNM, we:
1) prevent geometric leakage (no “axes”);
2) keep publication neutral yet auditable;
3) enable admissible set and ordering behavior on faces via explicit **ComparatorSet**;
4) make plane-crossing requirements first-class and checkable by declared publication checks or **OperationalGate(profile)** GateChecks.

**Extensibility.**
* **E17‑PC‑Ext‑1 (Open catalog).** New PCs MAY be added under `U.PubCharacteristic` provided they are declarative and CHR- and UNM-grounded.
* **E17‑PC‑Ext‑2 (Kinding).** New PCs MUST declare `kind ∈ {Number, EvidenceBinding, SelectorHint, ...}` and a **pinning requirement**.
* **E17‑PC‑Ext‑3 (Twin‑register names).** Supply **Tech** and **Plain** twins; avoid tokens that collide with E.10 bans; do not coin “…Space” names for publication forms.
* **E17‑PC‑Ext‑4 (Edition discipline).** If a PC depends on a definition or specification publication, **edition‑pin** the reference (`…Ref.edition`) and document migration rules.

**Adding invariants.**
1) Place **new invariants** for PCs in **CG-Spec** (specification lane), not on faces; supply acceptance tests.
2) Version any affected **CharacteristicSpace**; publish embeddings if semantics change; never mutate slots in place.
3) Update the relevant **GateChecks** or **GateProfiles** (`A.21`, including GateCrossing checks and crossing-visibility checks from `E.18`, `F.9`, and relevant Part G bridge or crossing wiring) to warn or block on invariant violations; never weaken functorial invariants.
4) **Document** edition and migration rules; extend §9 with a conformance item and provide **Lean‑profile downgrade** (advisory vs block) where applicable.

#### E.17:5.6 - Author ergonomics (non‑normative)
*Quick author steps (three steps and a micro-template):*
1. **Declare Σ and profile.** Choose `{PlainView, TechCard, …}` and whether faces are full or *‑Lite*.
2. **Pin once, reuse everywhere.** Attach `{UnitType, ScaleKind, ReferencePlane, EditionId}` to the arrow; cards reference these pins by ID (no duplication).
3. **Emit & verify.** Generate all faces from the arrow.

*Guidance:* treat *‑Lite* as **field‑drop only**; never add claims in *‑Lite*.

### E.17:6 - Rules and Invariants (normative)

**Publication-composition local test bundle.** A face that claims compositional publication passes only when five local tests are visible:

1. `identity`: `Emit_s(id_X)` is the identity view for `ViewObj_s(X)`.
2. `composition witness`: the published face for `g∘f` matches the composition of the published faces for `f` and `g`, or the face is marked non-compositional or explanatory-only.
3. `no-new-claim diff`: red-line against the governing D-side or S-side episteme shows formatting, indexing, pinning, or view-refinement work only.
4. `monotone promotion`: promotion from a plainer face to a richer face adds fields, pins, or typing without retracting or strengthening the source claim.
5. `scope non-widening`: `PublicationScope` stays within the relevant `ClaimScope` or `WorkScope`, and promotion does not widen it.



For any composable arrows `X —f→ Y —g→ Z` in `U`, and any `s, t ∈ Σ_viewpoints`:

1. **Functoriality & typing (per‑viewpoint).**
    * (a) **Identity:** `Emit_s(id_X) = id_{ViewObj_s(X)}`.
    * (b) **Composition:** `Emit_s(g∘f) = Emit_s(g) ∘ Emit_s(f)`. A face that claims compositional status carries a local witness: compare the published face for `g∘f` with the composition of the published faces for `f` and `g`. If the witness is absent or fails, mark that face non-compositional or explanatory-only and do not use it to satisfy the composition rule.

    * (c) **Typing (totality):** if `f : X → Y` then `Emit_s(f) : ViewObj_s(X) → ViewObj_s(Y)` is **total**; ill-typed composites must be fixed via `ViewObj_s`, not by weakening invariants.
    * *Intuition:* every viewpoint acts functorially on arrows; publication does not break arrow algebra.
2. **Reindexing coherence (monotone refinement + naturality).**
    * (a) If `s ⪯ t` then the `t`‑view **refines** the `s`‑view for the same morphism (**no content extension**; increased formality and typing only).
    * (b) For each `s ⪯ t` there are **object‑components** `PromoteView[s→t]_X : ViewObj_s(X) → ViewObj_t(X)` natural in `X`, i.e., for every `f : X → Y`
      `PromoteView[s→t]_Y ∘ Emit_s(f) = Emit_t(f) ∘ PromoteView[s→t]_X`.
    * (c) **Coherence:** `PromoteView[s→s]_X = id_{ViewObj_s(X)}`, and if `s ⪯ t ⪯ u` then `PromoteView[s→u]_X = PromoteView[t→u]_X ∘ PromoteView[s→t]_X` for all `X`.
    * *Defaults:* `PlainView ⪯ TechCard ⪯ InteropCard`.
    * *Note:* `AssuranceLane` is independent of the formality chain; it binds **evidence‑about‑claims** and MUST NOT introduce new claims **of** the morphism.
3. **D-side and S-side sourcing and EpistemicViewing compatibility (A.7 and E.10.D2, A.6.2–A.6.3, E.17.0).**
    * (a) Inputs to `Emit_s(-)` are **existing D-side or S-side epistemes** about the same arrow (for example, `MethodDescription`, `MethodSpec`) produced by `Describe_ID` and `Specify_DS` or `Formalize_DS` in A.7 and E.10.D2. MVPK does **not** redefine or collapse these I→D→S morphisms.
    * (b) Each `Emit_s(-)` SHALL be realised as a species of `U.EpistemicViewing` (A.6.3) over those D-side or S-side epistemes: describedEntity‑preserving, effect‑free and conservative in the sense of A.6.2 and A.6.3. Publication adds no new commitments beyond what is present in the referenced D-side or S-side epistemes.
    * (c) Edition governance respects `U.EditionSeries` and UTS; rows remain the identity anchors for names; MVPK faces MUST be (re‑)emitted when the underlying D-side or S-side editions change.
4. **Pin discipline (Part F and Part G).**
     * Any numeric or comparable content in a view SHALL pin {UnitType, ScaleKind, ReferencePlane}. **EditionId MAY be coarse at Lean profiles**; if units and scale are unknown, **declare ordinal compare-only** and **forbid arithmetic** until CHR pins are available.  Pins upgrade monotonically with profile and risk.
5. **No Γ‑leakage (publication independence).**
    Publication morphisms carry **no** Γ\_method, Γ\_time, or Γ_work semantics. Any build, render, or upload activity is **separate `U.Work` by a system on carriers** (`A.7`).
     **Lean assurance lane:** `AssuranceLane‑Lite` MAY expose only presence bits for {PathId or PathSlice?, Γ_time window?, BridgeId?}; unknowns propagate (tri‑state) with an explicit {degrade|abstain|sandbox} policy note.
6. **Carrier provenance.**
    Every emitted view records its **SCR/RSCR ids** on first occurrence (A.7 §5.6).
7. **Isomorphism preservation.**
    * If `f` is an isomorphism in `U`, then `Emit_s(f)` is an isomorphism in `View_s(U)`; inverses map accordingly.
8. **Cross‑Context and ReferencePlane bridging.**
    * If a view crosses contexts or reference planes, it **SHALL** cite the **Bridge + CL policy ids** (A.7 §5.8, bridge crossing). Such crossings MUST be explicit on `TechCard` and `AssuranceLane`.
9. **Totality of publication morphisms.**
    * Publication maps are total on their domains; when a composition in a view would be ill‑typed, the author **must** fix the view-object mapping (via `ViewObj_s`) rather than weakening functoriality or reindexing rules.
10. **PublicationScope discipline (subset & composition).**
    * (a) **Subset rule:** If a view `v` is about episteme `E` then `PublicationScope(v) ⊆ ClaimScope(E)`; if about capability `C` then `PublicationScope(v) ⊆ WorkScope(C)` only as the publication scope of a capability description, not as work admissibility, gate passage, release permission, or evidence that `U.Work` occurred.
    * (b) **No widening by refinement:** If `s ⪯ t`, then promotion `PromoteView[s→t]` MUST NOT widen `PublicationScope`.
    * (c) **Compositional bound:** For composable arrows `X —f→ Y —g→ Z`,
      `PublicationScope(Emit_s(g∘f)) ⊆ PublicationScope(Emit_s(g)) ∩ PublicationScope(Emit_s(f))`.

### E.17:7 - Structure & participants
```
                 Σ_viewpoints
                      │
            ┌─────────┴─────────┐
            │                   │
        Emit_s(-)           Emit_t(-)      … (family)
            │                   │
U :  X ──f──▶ Y ──g──▶ Z    X ──f──▶ Y ──g──▶ Z
        U.ViewMorph        U.ViewMorph
            │                   │
        Emit_s(f),…         Emit_t(f),…
```
* **Author** chooses `Σ_viewpoints` (declared concerns + conformance rules).
* **MVPK** emits `U.ViewFamily(f)` for each arrow `f`.
* **Declared publication checks** verify that pins, anchors, and IDs are present and that MVPK invariants are respected. Use `OperationalGate(profile)` GateChecks only when a live project gate profile actually governs the next project move.

### E.17:8 - Examples (SoTA-aligned Local Tests)

Read these examples as local tests for MVPK invariants, not as source citations by reputation.


1. **Composite service pipeline (`InteropCard` + `AssuranceLane`).**
    `f: Parse → Normalize`, `g: Normalize → Score`.
    `InteropCard(g∘f)` is an interoperability **view** whose path set equals the **relational composition** of the two cards; `AssuranceLane(g∘f)` cites test records as evidence **carriers** with edition pins. (Carriers, not semantics; concrete envelope formats are outside Part E.)
2. **Control loop morphism (`TechCard` + `PlainView`).**
    * For `h: Setpoint → Actuation`, `TechCard(h)` is a typed card with units; `PlainView(h)` narrates the same mapping with no new claims. (Monotone formalization echoes refinement‑typed stacks.)
3. **Optics-informed composition witness.**
    * Profunctor and optic accounts are useful only as a source idea for why compositional publication matters. The local FPF test is still the MVPK witness: emit the face for `g∘f`, compose the emitted faces for `f` and `g`, and compare them. If the comparison is not supplied or fails, the face stays non-compositional or explanatory-only; optics vocabulary does not carry the rule by analogy.

4. **Functional-description publication (`PlainView` + `TechCard`).**
    A principle scheme or functional diagram can publish a readable relation from signature or principle episteme content to method-family selection, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, and result measurement. The MVPK faces may help a team inspect that relation and prepare a work plan, but they do not turn the diagram, table, screen, or export into work occurrence, gate passage, evidence, engineering justification, or supervisory or control architecture. For those uses, the team first recovers the existing exact typed project-side value and reference that carries the claim when available: work-relevant source restoration under `A.15.4`, project `U.Method`, `U.WorkPlan`, and dated `U.Work` occurrence under `A.15` and `A.15.1`, evidence or provenance path under `A.10`, engineering-justification record under `B.3`, gate or constraint decision under `A.20` or `A.21`, or supervisory or control architecture record under `B.2.5`. If no existing source carries the needed claim, create only a prospective repair request, future decision request, prospective work-plan entry, or explicit source-gap note; do not backdate evidence, gate passage, work occurrence, release permission, engineering justification, or assurance for the earlier claim.


### E.17:9 - Conformance checklist (normative)

`CC-MVPK-FD` is the functional-description guard in §5.1a. It is conditional on a functional-description publication face and must not read as the first universal MVPK gate.

A conformance check is retained only if it changes the next admissible use of the publication face, blocks a concrete overclaim, or preserves a source anchor or reopen condition needed for the declared admissible use.

#### E.17:9.1 - Core ordinary checks

| ID | Requirement | Practical test |
| --- | --- | --- |
| **CC‑MVPK‑1 (Viewpoint explicit)** | Each view declares its **Viewpoint** (stakeholders, concerns, conformance) as a publication `U.Viewpoint`. | Cards show `PublicationVPId` (or equivalent publication‑viewpoint field) and concerns. |
| **CC‑MVPK‑3 (No content extension)** | `PlainView`, `TechCard`, and `InteropCard` add **no new claims** beyond the underlying D-side or S-side epistemes. | Red‑line vs D-side or S-side episteme output (`Describe_ID` or `Specify_DS`) shows only formatting or indexing. |
| **CC‑MVPK‑4 (Pins & anchors)** | Numbers and thresholds pin {...}. **Lean exception:** at MVPK‑Min or MVPK‑Lite profiles, EditionId MAY remain coarse; ordinal claims are admissible only as compare‑only (no means or z-scores). | Validation shows pins present or compare‑only mode engaged. |
| **CC‑MVPK‑4j (PublicationScope present)** | Each view **declares `U.PublicationScope`** (USM §6.5). | Field present; presence‑bit green. |
| **CC‑MVPK‑5 (Carrier anchoring)** | First mention includes **SCR/RSCR** ids when carrier work or rendering work is live. | SCR ids visible on the card when used. |

#### E.17:9.2 - Conditional checks

| ID | Requirement | Practical test |
| --- | --- | --- |
| **CC‑MVPK‑0 (Lean publication guard)** | For Lean profiles, a minimal guard runs: (i) set‑returning selection present; (ii) ReferencePlane present; (iii) any crossing cites BridgeId+CL with penalties applied to R only. | Validation report shows presence bits; penalties apply to R only. |
| **CC‑MVPK‑2 (Functoriality)** | `Emit_s(id)` is identity; `Emit_s(g∘f) = Emit_s(g)∘Emit_s(f)`. | Compose two cards and diff with the card of the composite. |
| **CC‑MVPK‑3b (Boundary claim‑set integrity)** | If a published arrow is a boundary, interface, or protocol and an A.6.B claim set exists (`L-*`, `A-*`, `D-*`, and `E-*`), then any normative text on faces **MUST** be traceable to that claim set (prefer claim‑ID citations); faces **MUST NOT** become a second boundary specification. | Lint flags uncited normative clauses; faces reduce to {claim‑ID citations + informative commentary}. |
| **CC‑MVPK‑4b (Lean assurance)** | If `AssuranceLane‑Lite` is used, presence bits for {PathSliceId?, BridgeId?} suffice; full evidence-carrier lists stay with the governing evidence source. | Presence bits visible; required evidence-carrier refs stay outside Lite. |
| **CC‑MVPK‑4c (Input and Output vs publication)** | Faces **do not** restate Input and Output; they carry **presence‑pins + anchors + EditionId** only. | Face inspection shows no Input and Output duplication. |
| **CC‑MVPK‑4d (Admissible orders)** | Any selection or comparison on faces **returns sets or admissible partial orders** with a **ComparatorSet** citation. | No hidden scalarization; ComparatorSetRef present. |
| **CC‑MVPK‑4e (Signature on faces — banned)** | The term **“signature”** is **not used** on faces; use **TechName** or **PlainName**. | Token scan: no “signature” on faces. |
| **CC‑MVPK‑4f (PC discipline)** | Any numeric or comparable publication uses **Publication characteristics** (PC) and carries pins {unit, scale, reference‑plane, edition}. | Cards show PC fields + pins; validation passes. |
| **CC‑MVPK‑4g (No axis or dimension)** | Faces avoid “axis”, “dimension”, and “plane” metaphors except **ReferencePlane**; use CHR terms (**Characteristic**, slot, or **CharacteristicSpace**). | Lexical check flags none; only `ReferencePlane` appears. |
| **CC‑MVPK‑4h (Edition pins on defs)** | Where maps, distances, or spaces are cited, the face pins `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `CharacteristicSpaceRef.edition?`. | Validation shows edition fields populated. |
| **CC‑MVPK‑4i (Crossings gated)** | ReferencePlane crossings or Context crossings cite **Bridge + CL** policies; penalties apply to **R‑channel** only. | IDs present; R-channel penalty application verified in harness logs. |
| **CC‑MVPK‑4k (Subset‑of underlier)** | For views about epistemes or capabilities, `PublicationScope ⊆ ClaimScope or WorkScope`; reindexing **does not widen** it. | Subset witness passes; promotion diff shows no widening. |
| **CC‑MVPK‑6 (Γ‑separation)** | No cost, time, or data-spend on publication morphisms. | CI shows proof records or witness records; gate validation passes. |
| **CC‑MVPK‑7 (Reindexing monotone)** | If `s ⪯ t`, then `Emit_s(x) ⪯ Emit_t(x)`. | `TechCard` ≤ `InteropCard` (more structure, same claims). |
| **CC‑MVPK‑8 (`SurfaceKind` discipline)** | Only **PublicationSurface** or **InteropSurface** are used; faces are named **...View** or **...Card**. | Token scan; no “rendering” or “presentation” as `SurfaceKind` values. |
| **CC‑MVPK‑9 (Reindexing naturality)** | Reindexing coercions `PromoteView[s→t]` exist, are total, and commute with composition. | Witness shows `PromoteView[s→t]_Z ∘ Emit_s(g∘f) = (Emit_t(g) ∘ Emit_t(f)) ∘ PromoteView[s→t]_X`. |
| **CC‑MVPK‑10 (Iso‑preservation)** | Isomorphisms in `U` remain isomorphisms under each viewpoint. | Cards show mapped inverses or an iso‑witness. |
| **CC‑MVPK‑11 (Typing & totality)** | Ill‑typed composites are rejected at `ViewObj_s` rather than weakening functoriality. | Type‑check fails early; no “best‑effort” composition in cards. |
| **CC‑MVPK‑12 (Bridge+CL on crossings)** | Any cross‑Context view or ReferencePlane-crossing view cites **Bridge + CL** policy ids. | IDs present on `TechCard` or `AssuranceLane`. |

### E.17:10 - Anti‑patterns (with fixes)

1. **“Presentation logic” as semantics.**
    *Fix:* Move any logic to `Describe_ID`, `Specify_DS`, CG‑Spec, or KD‑CAL; keep views declarative; publication adds **zero** claims.
2. **Publishing only view objects.**
    *Fix:* MVPK **acts on arrows**. Always emit views for `g∘f`, not just for `ViewObj_s(X)`, `ViewObj_s(Y)`, and `ViewObj_s(Z)`.
3. **Unpinned numbers.**
    *Fix:* Reject card; supply **pins** plus CG and CHR anchors.
4. **Viewpointless views.**
    *Fix:* Define Viewpoint; attach concerns + conformance; re‑emit.
5. **`InteropCard` equivalent to `TechCard` duplication.**
    *Fix:* `InteropCard` may refine typing or shape but cannot contradict `TechCard` (reindexing monotone).

### E.17:11 - Consequences

| Benefit | Why it matters | Trade-off and mitigation |
| --- | --- | --- |
| **Arrow traceability.** | Composition preserved across views enables chain‑of‑evidence on pipelines. | Slight authoring overhead → MVPK templates. |
| **Review-ready faces.** | Pins + CHR anchors make numeric claims verifiable. | Declared publication checks perform MVPK checks; project gates stay with the relevant `OperationalGate(profile)` or `GateDecision` source when the gate claim is live. |
| **Terminology hygiene.** | Clear View vs Viewpoint, Publication vs Presentation. | Enforce L‑SURF tokens in CI. |
| **Notation independence.** | Viewpoints talk concerns, not tools. | Provide adapters to local stacks. |

### E.17:12 - SoTA Alignment: Adopted And Adapted Invariants And Rejected Shortcuts

**SoTA alignment rule.** Read each row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and Relations of this pattern.

| Source idea and current source | Local FPF invariant and practical local test | Adopted, adapted, or rejected shortcut |
| --- | --- | --- |
| Joint ISO, IEC, and IEEE 42010:2022 architecture-description practice separates architecture description, stakeholder concern, viewpoint, view, model kind, correspondence, and correspondence rule instead of letting one readable model face stand in for all of them. | MVPK publishes one source-pinned face over an existing source `U.Episteme` or `U.View`; every load-bearing face names its publication `U.Viewpoint` and the `PublicationVPId` reference when that reference is used, names concerns, keeps `U.View`, viewpoint, carrier work, rendering work, correspondence support, concrete exchange envelope, and evidence envelope separate, and passes the no-new-claim diff before any work, evidence, gate, assurance, carrier, or bridge use is considered. | Adopt explicit source, concern, view, viewpoint, correspondence, and model-kind separation; reject the shortcut where a readable architecture or model face becomes evidence, work occurrence, gate passage, release permission, bridge support, or concrete exchange authority by presentation alone. |
| Profunctor and optic accounts (2017-2019; source maturity = research or theory line, not load-bearing without local witness) support compositional views that compose like arrows. | MVPK adopts only local publication-composition tests: identity, composition witness, no-new-claim diff, monotone promotion, and scope non-widening. | Adopt the five-test publication-composition bundle; reject optics vocabulary as proof by analogy or as a replacement for local witnesses. |
| Refinement-typed ecosystems (2016+; source maturity = widely used technical practice) keep units, scales, and type-like constraints attached to values. | MVPK publication faces carry pins and CHR and CG anchors; local test: numbers, thresholds, and characteristic claims on faces have units, scales, reference-plane support, and edition support where load-bearing. | Adapt pin discipline; reject readable numbers as self-validating values. |
| Interoperability and evidence-envelope practice (source maturity = mature standards or practice, depending on concrete envelope) separates exchange format and carrier evidence from the claim being carried. | MVPK faces may expose evidence carriers or exchange envelopes, but concrete formats live outside Part E; local test: the face adds no claim and points back to the governing source or evidence path. | Adapt envelope discipline; reject treating envelope presence as semantic authority, evidence sufficiency, work occurrence, or gate passage. |

(References are selected because they support local MVPK invariants and tests; MVPK remains notation-agnostic.)


### E.17:13 - Relations

* **Builds on:** `A.7` and `E.10.D2` for carrier and front-end discipline plus strict I-, D-, and S-discipline; `A.6.2`-`A.6.3` for episteme morphisms, `U.EffectFreeEpistemicMorphing`, and `U.EpistemicViewing`; `E.17.0` for `U.MultiViewDescribing`; `E.8` and `E.10` for authoring and publication-language discipline; Part F and Part G for bridge, terminology, characteristic, and pin discipline.
* **Constrains:** publication-face-emitting automation and hand-written publication faces. They remain species of `U.EpistemicViewing` over existing D-side and S-side epistemes and may not become a second I->D->S mechanism, evidence path, gate decision, work occurrence, assurance record, release source, or bridge declaration by readable form.
* **Current neighboring-pattern boundaries from `E.17:5.1d`:** work or reliance support applies `A.15.4`, with `A.15` for role, method, plan, and work alignment and `A.15.1` for one dated `U.Work` occurrence; evidence, provenance, attestation, currentness, and freshness apply `A.10`; engineering justification, assurance, confidence, readiness, and limitations apply `B.3`; gate passage, constraint validity, adjudication, and release decision support apply `A.20` or `A.21`; same-entity textual restatement applies `A.6.3.CR`; same-entity representation-scheme or reasoning-medium change applies `A.6.3.RT`; deliberately narrower-use rendering applies `A.6.3.CSC`; explanation-facing rendering applies `E.17.EFP`; bounded comparative review applies `E.17.ID.CR`; changed described entity, target, ontology frame, or governed claim applies `A.6.4`, `OntologicalReframing`, or the exact retargeting or reframing pattern; carrier, export, OCR, screen, front-end behavior, or work on carriers applies `A.7`.
* **Part F bridge wording boundary:** when the publication face uses or invites "same", "equivalent", "align", "map", substitutable, interchangeable, attribute, entity, or profile matching, or other bridge-wording claim pressure across contexts, the wording repair belongs to Part F and `A.6.9`; the bridge support belongs to `F.9` or `F.9.1`. `E.17` does not create a local bridge taxonomy.
* **Coordinates with:** B-operators for no Gamma-leakage, C-cluster selection or archive patterns where views remain publication faces rather than selections, CHR and UNM for measurement and normalization semantics, `F.9` or `F.9.1` for bridge support, `A.6.9` for sameness wording, and the neighboring source patterns named above. This section is a relation and neighboring-pattern boundary statement for publication use, not a standing decision tree or process order.

### E.17:14 - Minimal authoring template (Part E)

**Header:** `MVPK v⟨edition⟩ — Σ = {PlainView ⪯ TechCard ⪯ InteropCard, AssuranceLane ⟂}`
**For each arrow `f`:** emit `{Emit_s(f) | s ∈ Σ}` (or use the plain aliases `{PlainView(f), TechCard(f), …}`) with: **PublicationScope**, ViewpointId, pins, CHR and CG anchors, SCR ids, Bridge+CL ids (if crossing), and—if composite—machine‑checkable witnesses that `Emit_s(g∘f) = Emit_s(g)∘Emit_s(f)` **and** for each `s ⪯ t` the naturality square `PromoteView[s→t]_Y ∘ Emit_s(f) = Emit_t(f) ∘ PromoteView[s→t]_X`.

### E.17:15 - Manager’s one‑page review (copy‑paste)

> “We publish every **morphism** under a declared **set of viewpoints** using **MVPK**. Each **view** that claims functorial composition carries the local composition witness; without that witness it stays non-compositional or explanatory-only. Each face **adds no new claims** and pins **unit, scale, reference‑plane, and edition** with **CHR and CG** anchors. **`InteropCard`** views clarify concerns and semantics only (concrete exchange lives outside Part E); **`AssuranceLane`** cites evidence carriers (SCR). Any cross‑Context or cross-plane view cites **Bridge+CL** (Φ→R only). Publication build, render, or upload activity is **`U.Work` on carriers**, not a mechanism change.”

### E.17:End
