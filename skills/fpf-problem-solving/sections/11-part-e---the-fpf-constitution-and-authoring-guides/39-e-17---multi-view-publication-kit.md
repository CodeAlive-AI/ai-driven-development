## E.17 - Multi‑View Publication Kit
> **Status:** Stable
> **Type:** Part E publication-governance pattern
> **Normativity:** Normative unless explicitly marked informative

**At a glance.** Use `E.17` when one source-backed episteme, episteme-side view, morphism, or functional relation needs several readable publication faces for different readers without changing the underlying claim.

**Use this when.** The engineering team needs a plain view, technical card, interoperability card, or `AssuranceLane` face that helps people read, inspect, exchange, or cite the same source-backed relation without turning the face into work occurrence, evidence, gate passage, assurance claim, engineering justification, control architecture, authority, or release permission by presentation alone.

**What goes wrong if missed.** A readable face, card, dashboard tile, export, generated explanation, or comparison view starts acting as evidence, work claim, gate passage, assurance claim, release permission, authority, or source relation merely because it is readable and well placed.

**What this buys.** The publication face remains useful for orientation, inspection, exchange, and citation while the underlying episteme, publication scope, face kind, source relation, and any downstream typed value stay separately recoverable.

**First output.** One source-pinned publication face with the underlying `U.Episteme`, Description episteme, or Description episteme selected for specification use, publication scope, face kind, bounded publication use, and any present downstream typed value named only as far as the current use needs, such as a `GateDecision`, evidence path, work occurrence, status source, or authority-reference relation.

**Working publication move.** Publish one source-pinned face; separate source episteme or episteme-side view, face, carrier, bounded publication use, and any present downstream typed value plus its governing FPF pattern and reference; use the face for inspection, source-finding, review, exchange, or planning preparation; apply the neighboring FPF pattern governing that claim if work, evidence, gate, assurance, engineering-justification, authority, control, or release use is present.

**Ordinary formality rule.** If the face is used only for orientation, source-finding, review, comparison, or planning preparation, keep the publication light: one pinned face or compact card plus a clear bounded-publication-use line is enough.

**Load-bearing formality rule.** Add the fuller MVPK record only when the face will be used for external-impact reliance, cross-context exchange, evidence citation, gate or release pressure, engineering-justification use, disputed interpretation, or another use where a concrete overclaim would change the next engineering move.

**Stop condition.** Do not create a new publication record merely because a face exists. Stop when the current face changes no next engineering move and blocks no concrete overclaim.

| Useful publication case | Ordinary reduced use | Overread to block |
| --- | --- | --- |
| A source-pinned MVPK face lets the team inspect one morphism, review it, exchange it, or prepare planning without changing the claim. | Source-finding or bounded inspection with no downstream claim or effect. | A face, screen, export, or diagram is treated as performed work, gate passage, evidence, engineering justification, supervisory relation or control relation, or release permission by layout or readability alone. |
| A skill pack or MCP-backed access service exposes one framework face, pattern card, explanation, or retrieval result. | Framework access, source-finding, bounded inspection, or pattern-use orientation with edition and bounded-use visible. | The callable access carrier is treated as framework architecture, evidence about source material or source relation, currentness proof, tool permission, performed work, release authority, or gate authority by protocol availability alone. |
| A README, preface, front matter, or publication carrier states scope, edition, intended use, or source pointers. | Orientation, source-finding, bounded inspection, edition awareness, or declared publication-use guidance. | The front matter or carrier is treated as truth, currentness proof, authorization, assurance, gate passage, work readiness, or source relation by publication appearance alone. |

**Boundary aid pointer.** If one encountered publication-facing unit is easy to interpret as work, evidence, gate, approval, status, explanation, comparison, or narrower-use rendering, handle one claim being made or effect at a time using `E.17:5.1d`.

Here in the first-screen interpretation, keep only the MVPK publication move: one source-pinned face, one bounded publication use, and neighboring FPF pattern governing any present typed downstream value only as far as the current use needs.

**Not this pattern when.** Not this pattern when the issue under repair is performed `U.Work`, a work plan, work claim, evidence path, provenance path, assurance claim, engineering justification, gate decision, authority relation, control architecture, carrier work, OCR work, release decision, or a narrower-use rendering that needs its own source-bearing return. Use the FPF pattern that governs that issue.

> **Tech-name:** `MultiViewPublicationKit` (**MVPK**)

> **General publication-face form:** Plain `MVPK face` names the publication-form use of one selected `U.Episteme` edition under one exact publication `U.ViewpointRef`, one `U.PublicationScope`, declared pins where needed, and one bounded publication use. It is not a U-kind. The selected episteme is a `U.View` only when the E.17.0 conformance relation obtains; readable form alone adds no claim and grants no view membership. Evidence use, authority use, gate use, work use, assurance use, release use, and engineering-justification use require the neighboring FPF pattern governing that exact claim.
> **USM binding (overview):** `PublicationScope` is a **USM‑class** object that parameterizes MVPK; see §5.0.
> **Episteme-side view position.** MVPK can publish an already recognized `U.View`, or A.6.3 construction can yield a separately identified candidate episteme for a face. E.17.0 then tests that episteme independently against the exact viewpoint episteme resolved from `publicationViewpointRef : U.ViewpointRef`; `PublicationVPId` is that episteme's designator, not the reference. In the morphism profile, the selected episteme's exact EntityOfConcern is the governed morphism value `f : EpMorphism`; neither a face field nor a publication form substitutes for that C.2.1 identity. Publication occurrence, form, carrier, optional viewing construction, and `U.View` membership remain separate.

### E.17:1 - Intent

Provide a disciplined way to publish one source episteme or episteme-side view across multiple didactic faces without adding semantics, while keeping publication viewpoints explicit and auditable. The canonical formal profile is morphism publication: a small publication-face kit applied to a governed morphism value, typically `EpMorphism` under A.6.2, yields a family of face-use epistemes and forms whose conceptual representation can be checked against arrow composition, edition, and measurement pinning.

### E.17:2 - Problem frame

* Teams routinely need several **faces** of the *same* arrow: a **`TechCard`** for the catalog, an **`InteropCard`** for machine exchange, a **`PlainView`** for narrative, and an **`AssuranceLane`** for evidence.
* Informal “renderings” quietly **drift semantics**; **composite arrows** are often published piecemeal, breaking traceability; **evidence** forgets unit, scale, and edition pins.
* “View” and “viewpoint” are **blurred** in practice; authors conflate **publication** with **mechanism**.
* publication-face-kind discipline requires **`publication-face kind` token discipline**; Core allows only literal values **publication face/form** or **interop publication form**; faces are named **...View**, **...Card**, or **...Lane** with no ad-hoc face-kind names outside the literal set.

**MVPK** fixes this by selecting one exact episteme edition, one exact publication viewpoint, one publication form, one bounded use, and any required pins. A.6.3 viewing is an optional construction route when another episteme is actually constructed from the source; E.24.PUB governs publication availability. In the morphism profile, the construction and publication rules preserve the declared functorial discipline for Description epistemes, including Description epistemes admitted for specification use. **Part E is conceptual:** no machine-exchange formats are specified here.

### E.17:3 - Problem

1. **Semantic drift in publication.** Unchecked presentations introduce claims not present in the exact C.2.1 source epistemes about the arrow. Each such episteme, including a Description episteme admitted for specification use, keeps its exact claim content, EntityOfConcern, and effective `U.ReferenceScheme`; publication form, viewpoint reference, scope, or carrier supplies none of those identity discriminators.
2. **Non‑compositionality.** Publishing `g∘f` yields faces that do not match composing the faces of `f` and `g`.
3. **View, viewpoint, and face confusion.** A template or face is treated as the view or viewpoint, with no exact conformance relation between two claim-bearing epistemes.
4. **Unpinned numbers.** Numeric claims lack unit, scale, reference‑plane, and **edition pins** from Part F or Part G, undermining auditability.

### E.17:4 - Forces

| Force | Tension |
| --- | --- |
| **Compositionality vs legibility** | Preserve arrow invariants across views ↔ keep each view didactic and audience‑appropriate. |
| **Neutral naming vs domain idioms** | Use vocabulary stable across domains ↔ allow local templates (SOPs, APIs, checklists). |
| **Publication-face independence (A.7)** | Publication preserves EntityOfConcern, Description-episteme, and specification-use boundaries ↔ authors expect rich presentations. |
| **Evidence discipline** | Views cite CG-Spec and CHR references when numeric or comparable claims are exposed ↔ authors want compact cards. |

### E.17:5 - Solution — the **MVPK Kit**

#### E.17:5.0 - Publication-scope and face-profile binding (normative)

* **PublicationScope.** Every publication-face use declares one `U.PublicationScope` under A.2.6. It bounds that publication use and establishes neither `U.View` membership nor permission, evidence, work, assurance, or release.
* **No overload.** `U.PublicationScope` does not encode the selected episteme, publication viewpoint, MVPK face profile, Publication Characteristics, or presentation carrier. The face use names those objects through their own exact references and relations.
* **Profile.** An MVPK profile fixes:
  * exact face-use designators `F_face` and any declared partial order among them;
  * Publication Characteristics and required pins;
  * cross-context or reference-plane constraints current for emitted faces.
* **Canonical faces.** MVPK-Max contains exactly `PlainView`, `TechCard`, `InteropCard`, and `AssuranceLane` as publication-face designators. Despite the historical `PlainView` spelling, none of these designators identifies a `U.View` or `U.Viewpoint`. The selected episteme gains `U.View` membership only through E.17.0 conformance to the exact viewpoint episteme resolved by `publicationViewpointRef`.

#### E.17:5.1 - Terminology (normative)

* **View** (`U.View`): the same C.2.1 episteme individual for which `EpistemeViewpointConformanceRelation` to at least one exact `U.Viewpoint` episteme obtains under E.17.0. Direct authoring and A.6.3 viewing are construction routes only. An MVPK face name (`PlainView`, `TechCard`, `InteropCard`, or `AssuranceLane`) does not grant this membership. Each face use names the selected episteme edition, `publicationViewpointRef : U.ViewpointRef`, publication form, `U.PublicationScope`, and any source relation or pins needed for the use. `PublicationVPId` remains the exact viewpoint episteme's designator. Any carrier rendering is separate `U.Work`; the publication occurrence, form, and carrier are governed by E.24.PUB.
* **Publication vs expression vs bearing vs presentation vs rendering vs representation (guard):**
    * **Publication** = one exact E.24.PUB `EpistemePublicationRelation` occurrence with five fixed participants: the selected C.2.1 episteme edition, audience-declaration episteme, bounded-use-declaration episteme, exact publication form, and exact `U.PresentationCarrier`. It makes that edition available to entities admitted by the audience declaration for the bounded use. Changing any participant identifies another occurrence; a demonstrated availability gap followed by restoration creates a later occurrence. If A.6.3 constructs another episteme from a source first, that construction remains separate; if the candidate conforms to the exact publication viewpoint, E.17.0 recognizes the same episteme as `U.View`. Neither construction nor publication substitutes for conformance.
    * **Form expression** = `PublicationFormExpressionRelation` among the selected edition, exact publication form, and bounded-use declaration. It states that the form expresses enough of that edition for the use; omission, coarsening, or changed admitted operations can end it without changing the carrier.
    * **Carrier bearing** = `PublicationFormBearingRelation` between the exact `U.PresentationCarrier` and exact publication form. It states that this carrier bears the recoverable form; it is neither publication availability nor episteme identity.
    * **Presentation** = rhetorical arrangement of a published carrier; **notation-neutral**, adds no claims and is **not** a `publication-face kind`.
    * **Rendering** = display layout of a carrier, purely graphical formatting; performed rendering is separate `U.Work` on its exact carrier, not a `publication-face kind` or publication occurrence.
    * **Representation** = a C.29 representation and its exact correspondence to independently recovered objects or relations; it is not a publication occurrence, publication form, view-membership rule, or carrier. Publication or representation makes no world-side subject relation obtain.
* **Architecture-description mapping note.** An architecture **viewpoint** maps to one exact `U.Viewpoint` episteme; `PublicationVPId` or `EngineeringVPId` designates it and a `U.ViewpointRef` resolves it. An architecture **view** maps to one exact episteme that passes E.17.0 conformance. An MVPK face is the separate publication form or use through which that episteme may be exposed.
* **No‑mechanism equivalence:** MVPK **is not** a mechanism; any operational activity, such as build, render, or upload work, is **separate `U.Work` by a system on carriers** (A.7; see **Rule 5 — No Γ-leakage** in §6).
* **Viewpoint (`U.Viewpoint`)** - the exact claim-bearing episteme edition recognized under E.17.0's dependent-kind membership rule. It states stakeholders or audience referents when current, concerns, target and admitted episteme-kind criteria, conformance rules, declared **Publication Characteristics**, and pinning expectations. `PublicationVPId` is its designator and the corresponding `U.ViewpointRef` resolves to that episteme; a bundle packages references without redefining membership or edition.
* **Explanation-use profile values.** Existing faces can state an explanation-use profile value as `SourcePinnedExplanation`, `SourceLinkedExplanationReconstruction`, `DidacticRetelling`, or `SpeculativeRetelling`, but those are local profile values over already existing MVPK faces rather than new face kinds, explanation kinds, or carrier-rendering kinds. Per-face pins, provenance references, and no-new-A.6.B-boundary-claims discipline still apply.

#### E.17:5.1a - Episteme-publication relation-position binding  *(normative)*

For functional-description publications, MVPK governs only the publication relation position.

**Publication relation position.** A principle scheme, functional diagram, comparison table, screen, export, scenario, explanation, or code-like method description can help interpretation, source-finding, comparison, selected-method inspection, or work-planning preparation.

**Unsupported neighboring claims.** The publication does not by itself assert performed `U.Work`, a work claim, gate passage, evidence, assurance, engineering justification, supervisory relation or control relation, authority, release permission, or a new transformation-flow kind.

**Interface and protocol proximity.** When interface, protocol, schema, boundary, or API wording appears beside a functional-flow description, keep the operational boundary, interface, or protocol claim with its own project claim set and typed project-side FPF kind and reference named by value, governed by the relevant FPF pattern such as `A.6.B`, `A.6.C`, or `E.18`. Do not absorb it into the functional-flow publication by layout proximity.

**Retargeting.** If the publication changes the EntityOfConcern or retargeting target from an already described component, recovered transformation, method, work occurrence, transformation-flow structure, material `U.Entity`, or source claim into a functional, control, or flow architecture claim, this is not a same-entity publication-use change. Use `A.6.4`, `OntologicalReframing`, or `E.18` as applicable.

**Source recovery.** When a requested use requires a typed project-side FPF kind and reference beyond the publication face, the engineer first recovers the corresponding existing project-side FPF reference if one already carries the needed claim. The bullets below are alternative governing-pattern exits, not one grouped source-headed kind:

- source wording, publication construction, carrier-relation construction, source relation, project-side reference, or explicit non-use disposition under `C.2.P`;
- appearance-based reliance repair under `A.15.4`;
- project `U.Method`, `U.WorkPlan`, or work-result record under `A.15`;
- evidence and provenance path under `A.10`;
- engineering-justification record under `B.3`;
- constraint or gate decision under `A.20` or `A.21`;
- supervisory or control architecture record under `B.2.5`;
- carrier, export, OCR, or front-end record under `A.7`;
- same-entity textual relation under `A.6.3.CR`;
- representation relation under `A.6.3.RT`;
- reduced-use-rendering relation under `A.6.3.CSC`.

**No backdating.** If no existing typed project-side FPF kind and reference named by value carries a claim that was supposed to already have a source relation, do not create a backdated source. Create only a prospective repair request, prospective decision request, prospective work-plan entry, or explicit missing-source-relation note, and treat the earlier claim or effect as unsupported until the required source exists.

Ordinary orientation and source-finding can stay as an inline note.

**Functional-description guard (`CC-MVPK-FD`).** A functional-description publication face separates the source `U.Episteme` or episteme-side `U.View`, the MVPK face, any present carrier or rendering work, the bounded engineering use, and unsupported neighboring use. The guard applies only when a functional-description face is present; it is not the first universal MVPK conformance gate.

MVPK inherits the distinction among `U.Episteme`, contingent published-episteme use, publication occurrence, publication form, `U.View`, `U.PresentationCarrier`, and authority-reference relation. It introduces no durable published-episteme kind or other generic semio kind, and it does not let a publication face act as `governingPatternRef`, `authoritySourceRef`, or the source claim for another claim.

When a morphism publication is encountered or reused, name only the relation positions needed by the current use:

* the exact underlying `U.Episteme`, `D` episteme, or `S` episteme edition whose ClaimGraph is being exposed;
* the exact `PublicationFormExpressionRelation` occurrence among that selected edition, exact form, and exact bounded-use declaration;
* the exact `PublicationFormBearingRelation` occurrence between the presentation carrier and form;
* the exact five-participant `EpistemePublicationRelation` occurrence when that selected edition is available to the declared audience for the bounded use;
* the selected episteme's independent E.17.0 `U.View` membership when the publication use calls it a view, plus any separate A.6.3 construction history when current;
* the exact system-performed carrier or rendering Work, and A.10 carrier-currentness, source-currentness, or provenance records, only when those neighboring facts are current; and
* the typed project-side FPF kind and reference or authority-reference relation when the next work or reliance claim depends on that exact governed object.

Changed claim content, EntityOfConcern, or effective reference scheme identifies another episteme edition under C.2.1. Re-evaluate `PublicationFormExpressionRelation` only when its selected edition, form, bounded-use declaration, or obtaining predicate changes; re-evaluate `PublicationFormBearingRelation` only when its carrier, form, or obtaining predicate changes. Independently, changing any of the five `EpistemePublicationRelation` participants identifies another publication occurrence without reidentifying an otherwise unchanged episteme. Publication availability lost and later restored creates a later occurrence; a file rename or layout change alone proves none of those changes.
The practical payoff is that a reader can recover which relation is available for reliance: the episteme claim, the published form, the view, the carrier, the typed project-side FPF kind and reference named by value, or the authority-reference relation. A dashboard tile, generated explanation, card face, credential view, or carrier can guide source-finding, but it does not by itself become the source claim or effect, gate decision, evidence relation, assurance claim, role or status, work occurrence, or permission.

**Source-exposure rule.** A publication face, carrier, rendering, dashboard tile, credential view, status view, comparison unit, explanation rendering, signed decision memo, release decision record, approval speech-act publication, or gate dashboard exposes, cites, or carries a typed project-side FPF kind and reference named by value only when that reference is recoverable under its governing FPF pattern and direct relation. It does not become that reference by readability, layout, title, color, fluency, proximity, copying, generation, or reuse. When the exposed reference is a real `SpeechAct`, `GateDecision`, evidence path, credential source, status source, `U.Work` occurrence, `U.Episteme`, or exact publication occurrence, rely on that typed and recoverable object and its governed relation; otherwise treat the face, carrier, display, or rendering as orientation or source-finding only.

**No retroactive source creation.** When the required source relation is missing, a new entry can be only a prospective repair request, prospective decision request, prospective work-plan entry, or explicit missing-source-relation note. It is not used as earlier evidence, approval, gate passage, instituting speech act, `U.Work` occurrence, release permission, engineering justification, or assurance for the unsupported past claim or effect.

#### E.17:5.1b - Shared source-relation and bounded-use vocabulary

Use this vocabulary when a publication face, rendering, generated text, comparison note, narrower-use rendering, source-finding cue, or authority-looking display can be overinterpreted as carrying a wider source relation or bounded-use permission than it actually carries. The vocabulary names the source relation or bounded-use value for one claim or use. It does not instantiate evidence, gate, assurance, work, commitment, speech act, decision, release, or authority.

| Source-relation or bounded-use value | Meaning for the local claim or use |
| --- | --- |
| `source-pointer-only` | The publication-facing unit points to a possible source but does not show that the source is available, was used, or makes the claim recoverable. |
| `source-relation-unknown` | The publication-facing unit does not yet show whether the needed source relation exists or makes the local claim recoverable. This blocks the downstream use until checked; it does not show that the underlying world claim is false. |
| `source-relation-not-needed` | No operative work, reliance, evidence, gate, assurance, bridge, source-dispute, release, or durable-naming claim is present for this publication-facing unit. Orientation, learning, source-finding, review, or planning preparation can proceed without inventing a source relation. |
| `source-not-recoverable-here` | The needed source relation can exist elsewhere, but it is not recoverable from this publication-facing unit or its stated source refs. Treat the unit as orientation or source-finding only, or reopen the source-bearing side. |
| `source-relation-absent` | The needed source relation is known absent from the current publication-facing unit and available source set for the stated use. Block that use; do not infer that the underlying world claim is false merely from this absence. |
| `source-available` | The cited source can be recovered or inspected for the current use. This does not yet show that the rendering used it correctly. |
| `source-retrieved` | The cited source has actually been recovered for the current check. This still does not show that it was used correctly or makes the local claim recoverable. |
| `source-used` | The inspectable generation, rewrite, rendering, comparison, work, or reliance source relation actually used the named source rather than only similar background. If that relation is unavailable, treat the unit as pointer-only or orientation-only until a source relation is recovered. |
| `source-faithful` | The publication-facing unit stays within the source claim relation for the stated use; omissions, declared source-loss modes, and additions are visible enough to inspect. |
| `claim-recoverable-from-source` | The local claim is recoverable from the source, declared correspondence relation, or required typed project-side FPF kind and reference named by value for the stated use. |
| `claim-not-recoverable-from-source` | The local claim is not recoverable from the source relation currently available. |
| `claim-conflicts-with-source` | The local claim conflicts with the available source relation. |
| `claim-plausible-only` | The claim can sound reasonable, but the source relation currently available does not carry it. |
| `source-omitted` | Relevant source claim, source passage, qualifier, condition, alternative, caveat, or uncertainty is missing from the publication-facing unit. |
| `source-loss-declared` | The publication-facing unit declares a source-loss mode such as omitted-detail, qualifier-loss, redaction, aggregation, scope-narrowing, recoverability-loss, representation-factor-loss for the local source-to-rendering relation. |
| `claim-widened` | The publication-facing unit turns a source possibility, hypothesis, bounded condition, low-confidence statement, narrower permission, or source-finding cue into a wider claim or use. |
| `added-linkage` | The publication-facing unit adds a causal, explanatory, bridge, comparison, work, evidence, gate, or authority relation not already carried by the source relation. |
| `independent-verification-present` | A separate check makes the local claim or use available independently of the publication-facing unit only through a named governing pattern and record named by value, such as an `A.10` evidence path, `B.3` assurance claim, `A.21` `GateDecision`, `A.20` constraint profile, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, or `F.9` Bridge Card. |
| `admissible-for-this-use` | This bounded-use value means admissible use for the named use only; wider downstream use still needs the neighboring FPF pattern governing that claim and typed project-side FPF kind and reference named by value. |
| `downstream-use-forbidden` | The publication-facing unit is not used for the named downstream claim or effect because the needed source relation is absent, source-loss-declared, contradicted, or outside scope. |
| `reopen-trigger-present` | A stated change, dispute, use escalation, source update, context shift, missing source relation, or contradiction forces return to the source-bearing side or to the governing FPF pattern and typed project-side FPF kind and reference named by value. |

Patterns can use shorter local field names such as `sourceRelationStatus`, `explanationSourceStatus`, or `representationValidityStatus` when the local object is clear. Comparative patterns split source-relation status from comparative-relation status instead of using one overloaded field. The local field remains interpretable through the vocabulary above, and the bounded use is named beside it when downstream reliance could change.

For ordinary use, name only the status distinction that changes the next bounded use. The common light states are `source-pointer-only`, `source-relation-unknown`, `source-relation-not-needed`, `source-not-recoverable-here`, `admissible-for-this-use`, `downstream-use-forbidden`, and `reopen-trigger-present`. The vocabulary is not an ordered scale, source-stage model, source-record taxonomy, authority-reference source taxonomy, or project-side evidence and assurance, gate, or work substitute. If a source relation is missing from the publication-facing unit, only the unsupported downstream use is blocked; the missing relation does not by itself prove the underlying world claim false. If `independent-verification-present` is relied on, name the separate governing pattern and record named by value that performs that independent check: `A.10` evidence path, `B.3` assurance claim, `A.21` `GateDecision`, `A.20` constraint profile, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, or `F.9` Bridge Card.

#### E.17:5.1c - Shared use-boundary terms

Use these terms when a publication face, rendering, narrower-use rendering, explanation, comparison note, source-finding cue, or authority-looking display can be interpreted beyond its named source relation. Define them once here and link back to this section from local patterns instead of minting local synonyms.

| Term | Meaning for FPF use |
| --- | --- |
| `orientation use` | The publication-facing unit helps a reader find, inspect, triage, compare, teach, discuss, or prepare planning while the unit itself does not carry a downstream work, reliance, claim, or effect. |
| `reliance use` | The publication-facing unit is used as the source relation for an engineering claim or effect that changes a next work occurrence or reliance use, such as method choice, work plan, performed-work claim, release, gate, approval, role or status, evidence, assurance, or external-impact action. |
| `work, reliance, claim, or effect` | A claim or instituted effect about method selection, selected method, `U.WorkPlan`, performed `U.Work`, work result, gate or release, role or status, evidence, assurance, boundary or policy effect, or another typed project-side FPF kind and reference named by value. |
| `operative claim` | A claim whose acceptance would change the next bounded work occurrence or reliance use, the typed project-side FPF kind and reference named by value to recover, or the cross-context use of the publication-facing unit. Explanatory prose, examples, and source-finding cues are not operative claims unless they are used that way. |
| `non-admissible downstream use` | A wider use that the current source relation does not carry. It requires narrowing the use, returning to the source-bearing side, recovering the source relation named by value, or using the neighboring FPF pattern governing that claim and typed project-side FPF kind and reference named by value that governs the wider claim or effect. |
| `reopen trigger` | A dispute, use escalation, missing, stale, or contradictory source relation, source update, context or window change, or wider claim or effect that requires source-bearing return, source refresh, re-expansion, or use of the governing pattern. |
| `authority-looking case` | A recognition phrase for an encountered publication-facing unit that can be overinterpreted as permission, approval, evidence, gate passage, role or status, work occurrence, assurance, or release source relation. It is not a `U.*` kind, not a typed project-side FPF kind and reference named by value, and not a governing pattern. |

#### E.17:5.1d - Compact boundary aid for the present claim or effect

When a publication-facing unit, publication face, rendering, narrower-use rendering, explanation, comparison note, dashboard tile, credential view, status view, carrier, or generated unit creates more than one possible interpretation, separate the claim being made or effect being used now and cite the source relation that makes the operative claim recoverable by value for that claim or effect. This compact boundary aid governs the present claim or effect only; it does not classify the whole encountered unit. The same encountered unit can expose several typed records; handle one claim being made or effect at a time instead of pretending there is one overall governing relation for the encountered unit.

**Mixed-case precedence.** When several publication-use patterns appear possible, repair the smallest unstable interpretation that changes the current bounded use before applying a neighboring pattern whose claim or effect is present:

1. If one local head is the only unstable part, apply `E.17.AUD.LHR` or `C.2.P` and stop when the repaired sentence names the local kind, relation, and bounded use.
2. If the bounded `PublicationUnit` or its primary EntityOfConcern interpretation is unstable, apply `E.17.AUD` or `E.17.AUD.OOTD` before using `E.17.ID.CR` or `E.17.EFP`.
3. If the unit is stable and the present problem is comparison overread, apply `E.17.ID.CR`; use `F.9`, `C.11`, `A.20`, or `A.21` only when equivalence, recommendation, selection, decision, gate, or release claim is actually being made.
4. If the unit is stable and the present problem is explanation overread, apply `E.17.EFP`; use `A.10`, `B.3`, `A.20`, `A.21`, or `A.15.4` only when evidence, engineering-justification, gate, release, work, or reliance claim is actually being made.
5. If the present problem is a durable reusable name, UTS row, Core-facing term, or cross-context naming relation, apply `F.18`; otherwise keep the lighter local repair pattern.

| Present claim or effect question | Apply or recover |
| --- | --- |
| Is the publication-facing unit being used to guide a work occurrence or reliance use by appearance, while the acting user still needs the typed project-side FPF kind and reference named by value before proceeding? | `A.15.4` for appearance-based reliance repair before the governing pattern slot or relation is recovered; the recovered project-side reference can then be `A.15`, `A.15.1`, `A.10`, `B.3`, `A.20`, `A.21`, `A.2.8`, `A.2.9`, `A.6.B`, or another typed project-side FPF kind and reference named by value. If that exact reference is already the live question, use it directly. |
| Is the publication-facing unit being used as evidence, provenance, attestation, currentness, freshness, or claim-bound evidence relation? | `A.10` evidence, provenance, or currentness path for the claim named by value. |
| Is the publication-facing unit being used as engineering justification, assurance, confidence, readiness, or limitations relation? | `B.3` assurance or engineering-justification claim with evidence, limits, and decay explicit. |
| Is the publication-facing unit being used as gate passage, constraint validity, adjudication, or release decision source? | `A.20` or `A.21` project records, including gate profile, constraint profile, decision record, log reference, scope, window, replay reference and freshness reference. |
| Is it the same EntityOfConcern with textual restatement only? | `A.6.3.CR Conservative Retextualization`. |
| Is it the same EntityOfConcern with representation scheme or reasoning medium changed? | `A.6.3.RT Representation-Scheme Transition`. |
| Is it deliberately reduced-use and useful only under narrower bounded use, `non-admissible downstream use`, and source-bearing reopen? | `A.6.3.CSC Controlled Semantic Coarsening`. |
| Is the primary issue explanation-facing rendering class on an existing MVPK face? | `E.17.EFP ExplanationFaithfulnessProfile`. |
| Is the primary issue one bounded comparative review unit over sources? | `E.17.ID.CR ComparativeReviewUnit`. |
| Did the EntityOfConcern, target, ontology frame, or claim or relation record named by value change? | `A.6.4`, `OntologicalReframing`, or the retargeting or reframing pattern named by value. |
| Is the publication-facing unit being used as bridge, substitution, equivalence, "same", "equivalent", "align", or "map" wording, or cross-context comparison relation? | Use Part F and `A.6.9` for repairing "same", "equivalent", "align", or "map" wording into explicit bridge work; use `F.9` or `F.9.1` for Bridge Cards, bridge kind, direction, `CL`, loss notes, bounded use, and stance overlays. Comparison alone is not a bridge. |
| Is the live question carrier, export, OCR, screen, front-end behavior, or work on carriers? | `A.7` and the exact carrier relation, front-end relation, or work-on-carrier record. |

**Evidence-path boundary.** An `A.10` evidence, provenance, attestation, freshness, or currentness path carries only the claim named by value it instantiates. It does not approve or authorize work, pass a gate, perform work, supply release permission, or raise assurance or engineering-justification use unless the typed project-side FPF kind and reference named by value that carries that downstream claim is also instantiated, such as `A.15.4`, `A.15`, `A.20`, `A.21`, or `B.3`.

**Gate-display boundary.** A dashboard tile, status view, or release screen exposes a gate decision only when the `GateDecisionRef`, gate or constraint profile version, target release or work scope, time window, currentness, freshness reference or replay reference, and evidence path are recoverable. Without that exact gate record, the display remains orientation or source-finding only; it is not a gate decision, gate passage, release permission, or performed-work record by color, label, layout, or proximity.

#### E.17:5.1e - Local review fields are not FPF kinds

Local review fields and values in CR, RT, CSC, EFP, ID.CR, or a neighboring publication-use pattern are local review aids for one case. They are not `U.Kind`, `publication-face kind`, `RelationKind`, `KindBridge`, `EvidenceKind`, `SlotKind`, `GateDecision`, `SpeechAct`, `Commitment`, `U.Work`, publication face, `authoritySourceRef` target, or typed project-side FPF kind and reference named by value unless another governing FPF pattern explicitly instantiates that object. When a local field starts carrying one of those downstream claims, cite or apply the governing FPF pattern and typed project-side FPF kind and reference named by value that carry it.

#### E.17:5.1f - Shared anti-overread invariants for publication-facing units

Use the FPF pattern that governs the claim being made or effect under use. Keep any local review field local, preserve reduced bounded use, and assign only the unsupported wider claim or effect to its governing source relation.

**Source-relation minimality.** Name the smallest direct FPF relation sufficient for the live use. A governed reference, publication occurrence, evidence path, engineering-justification record, gate decision, and release decision are different objects or relations; choosing one does not license another. Do not apply `A.10`, `B.3`, `A.20`, or `A.21` when the live use only needs source finding, orientation, or inspection of an existing source `U.Episteme`, exact publication occurrence, or status-register entry.

**Local repair vs publication redesign.** A local epistemic precision repair is enough only when it can preserve the current publication face or `PublicationUnit` while fixing one head, boundary, source relation, bounded use, explanation class, or unsupported downstream claim. If layout, grouping, visual emphasis, comparison arrangement, generated explanation, hidden source limitation, or mixed EntityOfConcern packaging still induces overread after the local relation is repaired, create a redesigned publication face or `PublicationUnit` instead of adding warning text around the misleading form.

**Most-likely careful interpretation constraint.** Design and word a publication-facing unit so its most likely careful interpretation does not exceed its named source relation, bounded use, and governing FPF pattern. A visible head such as `Approved` needs a visible `GateDecision` or a different head; a sorted comparison needs its comparator or sorting relation visible if no recommendation claim is intended; a generated explanation separates inferred links from pinned source claims by wording, label, or source reference.

**Visual cue claim pressure.** Layout, order, color, prominence, icon, grouping, and proximity are carrier or front-end cues that can carry publication-move pressure even when the words do not. Green color can imply readiness, top position can imply preference, grouping can imply equivalence, proximity to evidence can imply an evidence relation, a badge form can imply approval, and a lock or checkmark can imply verification. If the visual cue would make the reader treat the unit as evidence, gate passage, decision, recommendation, reliance relation, bridge relation, or approval, recover the governing FPF pattern and project-side kind and reference named by value, or redesign the publication face so the overread is no longer invited.

**Extraction survival.** When a `PublicationUnit` is excerpted, quoted, screenshotted, summarized, copied into a tutorial, retold by a generator, or moved to a slide, it keeps only the claims, source pins, boundary line, references named by value, and bounded use carried in that extracted unit. Any use that depended on hidden neighboring context is lost unless that context is carried by source pins, a boundary line, or a reference named by value. A dashboard screenshot does not carry the underlying gate record, a quoted comparison row does not carry the full comparator or sorting relation unless that relation is included or referenced, a copied explanation paragraph does not carry source pins unless pins remain recoverable, and a pattern excerpt does not carry the whole pattern boundary unless the excerpt states or cites it.

**No-extra-pattern case.** If a publication-facing unit has bounded use only for ordinary orientation, learning, source-finding, review, comparison, or planning preparation, and no operative work or reliance, evidence, gate, assurance, bridge, source-dispute, or release claim is present, keep the existing publication source relation and proceed with ordinary use. The visible closure is: no operative work or reliance, evidence, gate, assurance, bridge, source-dispute, release, durable naming, or project-side source-relation claim recovered; ordinary publication wording remains bounded to the current use.

**Pattern-inflation anti-pattern.** Do not apply a neighboring pattern merely because the publication-facing unit resembles a worked example. Apply the neighboring pattern only when a claim being made or effect changes the next available project move.

**Strategic overread invariant.** Apply the same anti-overread rules whether the misleading interpretation is accidental, conventional, incentive-driven, or intentionally induced by publication design. Green status color without `GateDecisionRef`, reviewed-looking wording without approval, selective source links without operative-claim source relation, comparison ordering without selection decision, hidden caveats behind a source link, or pins for trivial claims beside unpinned causal linkage do not create evidence, gate, decision, assurance, work, release, or bridge relation by design pressure.

**Carrier-travel invariant.** A copied, exported, screenshotted, summarized, generated, translated, or re-rendered publication-facing unit can carry orientation or source-finding cues. It does not carry evidence relation, authority-reference relation, gate passage, approval, engineering-justification relation, work occurrence, currentness, or release source relation unless the governing FPF pattern and typed project-side FPF kind and reference named by value remain recoverable for that use named by value.

**Derivative-chain decay.** A second-order rendering inherits at most the bounded use that is explicitly carried from the prior source relation. It does not inherit source faithfulness, evidence relation, currentness relation, authority-reference relation, gate decision, work relation, or reliance relation by default.

**Publication-face snapshot and refresh identity.** A publication face can keep the same visible layout, face name, or carrier while its source pins, source data window, source-relation status, freshness or currentness relation, `EditionId`, or bounded use changes. Visual sameness across time is not source, evidence, or use-boundary sameness. When a refreshed, revised, translated, regenerated, screenshotted, or re-rendered face is used beyond orientation or source-finding, name the face edition or snapshot, the source pins or data window that still carry the claim, and any changed bounded use. If those cannot be recovered, treat the face as orientation or source-finding only, or reissue the face under the governing pattern before work, evidence, gate, assurance, release, or reliance use continues.

**Claim-level source relation only.** Do not assign one whole-unit source-relation status unless every operative claim in that publication-facing unit has the same source relation named by value for the same use and unsupported downstream uses are explicit.

**Modality and deontic-force preservation.** Publication-facing transformations preserve possibility, obligation, permission, recommendation status, decision status, confidence, scope, and temporal window when those values change the claim or use. If one of these changes, narrow the bounded use or apply the governing pattern that carries the changed claim or effect. Comparison does not become recommendation or decision; explanation does not become evidence; a publication face does not become authority; a publication unit does not smuggle a downstream effect; source-linked does not mean source-available for reliance; ready-looking does not mean gate-passed.

This preservation rule also applies across extraction, translation, screenshotting, summary, and generated retelling. A translated permission is not wider permission, a screenshot of approval-looking display is not an approval record, a summary of evidence is not an evidence path, and a generated retelling of a decision is not the decision record unless the source relation that makes the operative claim recoverable by value and source pins survive in the new publication-facing unit.

**Reader position is not project role.** Reader position, audience, target user model, verifier position, review-reader position, and learner position do not become project roles, role assignments, decision authority, gate authority, issuer roles, or work roles unless a typed project-side value and reference instantiates that role relation.

**Source-gap states.** When the source relation is missing, say which source gap is present: source not named; source named but unavailable; source available but not used; source used but insufficient; source stale or outside its window; source contradicted; source accountable role or register mismatch. Block only the unsupported effect and keep any reduced bounded use available.

**Measure and display overread.** A number, score, percentage, color, rank, confidence value, similarity value, dashboard state, or measurement display is orientation only until the measurement source, aggregation rule, time window, population or scope, calibration or evidence path, and intended use are governed by the typed project-side FPF kind and reference named by value. Evidence-like use applies `A.10`; assurance-like use applies `B.3`; gate-like use applies `A.20` or `A.21`; work or reliance use applies `A.15.4` and then the recovered typed project-side FPF kind and reference named by value; bridge or substitution use applies `F.9` or `F.9.1`.

**World-contact stop.** Publication-facing units do not self-refresh after source update, revocation, policy change, holon-state change, incident, model update, environmental change, or new external observation. An outside change under the current use requires source refresh, reissued publication, or a new governed typed project-side FPF kind and reference named by value before work, evidence, gate, control, carrier, or other downstream use continues.

**Functional-description boundary.** A functional, architectural, descriptive, representational, or explanatory fit claim does not create permission, obligation, approval, gate passage, release source relation, performed-work evidence, or engineering justification. Those uses require the neighboring FPF pattern governing that claim and typed project-side FPF kind and reference named by value.

**Mixed bundle no-shared-evidence-relation rule.** A bundle with source-pinned, reduced-use, speculative, didactic, comparison, and evidence-facing parts is not interpreted under one shared evidence relation or use-boundary value borrowed from another member. Each operative claim keeps its own source relation and unsupported downstream use.

**Educational usefulness.** Didactic, onboarding, tutorial, and workshop usefulness is real orientation aid. It is not evidence, gate passage, approval, work occurrence, engineering justification, release permission, or bridge relation.

**Comparison exposes conflict; it does not adjudicate it.** A comparison note can expose contradiction, asymmetry, different foregrounding, or unresolved residue. It does not settle the conflict, select an option, approve release, pass a gate, or create bridge relation or substitution relation unless the neighboring FPF pattern governing that claim and typed project-side FPF kind and reference named by value carry that result.

**Same publication-facing unit, multiple interpretations.** A green release dashboard can be one MVPK face for source-finding, an `A.10` currentness path or evidence path when the evidence query is recoverable, an `A.21` gate-decision view when the `GateDecisionRef` is recoverable, or an unsupported release cue when those sources are missing. A generated comparative explanation can be an `E.17.EFP` explanation-use case, an `E.17.ID.CR` comparison case, a `A.6.3.CR` generated-summary case, or source-finding only; it is never all of those under one shared evidence-relation class or bounded-use value by fluency alone.

**Archetypal publication-use cases.** Use these as quick recognition slices, not as a closed taxonomy:

- **Green dashboard tile.** A tile says `Model ready`. Treat the tile as the `PublicationUnit` when that tile carries the present release overread. The useful publication use is source-finding and status orientation unless an exact `GateDecisionRef`, gate profile, source relation, and evidence or currentness relation are recoverable. Without those, the tile is not release permission or gate passage by green color or placement.
- **Generated explanation with source links.** A generated text explains a method and cites sources. The explanation rendering is not source replacement. Source links carry only the pinned operative claims they actually carry. If work or reliance is present, use `A.10` for the evidence path named by value or keep the rendering as reader help; if the rendering is deliberately reduced-use, use `A.6.3.CSC`.
- **Comparison table.** A table compares two methods and places one first. Ordering is not selection. The comparator or sorting relation, source references, shared review frame, and unsupported downstream claim remain visible. Choice or decision needs `C.11`; equivalence or bridge relation needs `F.9` or `F.9.1`.
- **Unrecovered source wording.** A draft uses source-object wording, undeclared interpretive-view shorthand, or generic unit wording without naming the FPF kind. Recover the FPF kind and relation positions instead of minting source-relation pseudo-kinds or undeclared interpretive-view pseudo-kinds. Use `PublicationUnit` only when a bounded reader-inspected unit inside a publication is present; otherwise use the exact episteme, view, publication, carrier relation, section of a named non-pattern FPF publication form whose reader-help function and reference are recoverable, `A.6.P` relation claim, or typed project-side FPF kind and reference named by value.
- **Translated tutorial.** A translated tutorial can improve reader access to an FPF pattern. It is a derivative rendering, not the original source. Operative claims need source mapping for reliance, translated heads can need `E.17.AUD.LHR` or `C.2.P`, and `F.18` is present only when durable naming, UTS, Core-facing, or cross-context naming work is intended.

**Practical harm prevented by neighboring pattern.** Use this map when the reader asks what the discipline buys in practice:

**Blocked overread with useful publication use remaining.**

- A comparison table appears to select option B. Block the selection interpretation when no `C.11` `ChoiceResult`, decision record, or visible selection relation exists. Useful publication use remains: use the table as a bounded comparison under `E.17.ID.CR`, or apply `C.11` when selection is intended.
- A green dashboard tile appears to permit release. Block the release or gate-passage interpretation when no `GateDecisionRef`, gate profile, evidence or currentness relation, and source relation are recoverable. Useful publication use remains: use the tile for source-finding and status orientation, then inspect the exact gate or evidence source if release work is intended.
- A generated explanation appears to prove a causal relation. Block the evidence or assurance interpretation when source pins and evidence path are absent or insufficient. Useful publication use remains: use the explanation as reader help or source-finding, then apply `A.10` or `B.3` only for the evidence named by value or engineering-justification claim they govern.

- `C.2.P` prevents the wrong object from being treated as source, the wrong relation from being treated as source relation, and a loose phrase from being treated as an FPF kind.
- `E.17.AUD` and `E.17.AUD.OOTD` prevent action on a publication unit whose primary entity of concern, carried publication move, or outside boundary shifted silently.
- `E.17.ID.CR` prevents a comparison unit from being used as decision, equivalence, bridge, evidence, or release source relation.
- `E.17.EFP` prevents fluent explanation from laundering unsupported claims into reliance, assurance, gate, or evidence use.
- `E.17` MVPK prevents a readable publication face from being treated as evidence, gate, work, authority, or release source relation by display quality.
- `F.18` prevents a local name from becoming global identity without context, kind, lineage, and bridge or cross-context naming relation.

**Anti-escalation examples.** Do not apply a neighboring pattern when its claim being made is absent:

- Do not apply `F.18` when a one-off local phrase repair restores the local kind, relation, and bounded use without minting a durable reusable name.
- Do not apply `A.10` when the publication-facing unit is not being used for reliance, evidence, provenance, currentness, or claim-bound evidence relation.
- Do not apply `A.21` when a dashboard tile is merely status orientation and no `GateDecisionRef` or gate profile is present.
- Do not apply `F.9` when a comparison does not claim sameness, substitution, bridge relation, or cross-context equivalence.
- Do not apply `E.17.EFP` when the text is only a same-entity rewrite or representation change governed by `A.6.3.CR` or `A.6.3.RT`.

**Concrete reopen trigger.** A reopen trigger names the condition and the nearest source-bearing side or governing pattern. A vague "reopen if needed" does not preserve the source relation.

#### E.17:5.2 - Declared `publication-face kind` values at Part E

Part E restricts `publication-face kind` values to the literals **publication face/form** and **interop publication form**. Concrete publication faces use names ending in **...View**, **...Card**, or **...Lane**.

**USM linkage (normative).** Every MVPK publication-face use declares a `U.PublicationScope` (USM §6.5). `U.View` membership remains governed by E.17.0 conformance.
For a face use selecting episteme `E`: `PublicationScope(face_E) ⊆ ClaimScope(E)`.
For a face use selecting a capability-description episteme about `C`: `PublicationScope(face_C) ⊆ WorkScope(C)`. This is a publication bound, not permission to perform work and not evidence that work occurred. Work-use reliance still requires `A.15.4` appearance-based reliance repair when the face itself is being used as a reason before the governing relation is named, plus the exact A.15 role, method, plan, and work relations current in that use.
Cross-context views cite Bridge + CL; CL penalties apply to R only (scope membership unchanged).

**Publication-face-kind naming discipline.**
* Declared `publication-face kind` values: **publication face/form**, **interop publication form**.
* Concrete faces use names ending in **...View**, **...Card**, or **...Lane**.
* The tokens **carrier, bearer, and holder** do not name a `U.View` or any publication entity.
  Use **`U.View`** only for an episteme that passes E.17.0 conformance. `PlainView`, `TechCard`, `InteropCard`, and `AssuranceLane` name MVPK face uses; none is a view-membership rule.
  Reserve **carrier** for symbol, document, data, transport, or display carriers and for **`U.Work` over those carriers**; source-currentness and evidence-provenance records are governed by A.10 and G.6 when reliance is current.
* Avoid geometric metaphors such as axis or dimension for publication forms; use **Characteristic** or **CharacteristicSpace** only when referring to CHR-MM entities.
* **Non-collision guard.** `ViewFamilyId` is a lexical tag for viewpoint families; it is not used to name any `U.View` or `publication-face kind`. MVPK face kinds remain **{PlainView, TechCard, InteropCard, AssuranceLane}** only.

**MVPK-Max publication faces (normative; exactly four; governed by the MVPK profile):**
* `PlainView` (explanatory prose face; the historical suffix does not grant `U.View` membership)
* `TechCard` (typed catalog card)
* `AssuranceLane` (evidence bindings)
* `InteropCard` (conceptual interoperability face; mapping to concrete exchange formats lives in the interop annex; Part E does not specify schemas)

`AssuranceLane` can expose evidence bindings, evidence-carrier references, pins, and presence bits. It is not a `B.3` assurance claim, readiness or confidence verdict, engineering-justification record, or evidence-sufficiency result. When a published face is used to raise or lower assurance, readiness, confidence, limitation, or engineering-justification result, the governing source relation is `B.3`; the face only helps recover the cited evidence bindings.

**Lean profiles (small-team friendly, optional; as MVPK kit profiles):**
* **MVPK-Min (F0-F1):** `F_face = {PlainView, TechCard-Lite}`. `AssuranceLane` omitted. No interop face.
* **MVPK-Lite (F1-F3):** `F_face = {PlainView, TechCard-Lite, AssuranceLane-Lite}` when the assurance trigger is current. `InteropCard` appears only for an exact external receiving use.
* **MVPK-SetReady (F3-F5):** add `InteropCard` when replayability or external interchange is required (details outside Part E).
* **Profile-upgrade triggers:** (i) cross-Context reuse or ReferencePlane crossing; (ii) QD replay needs or OEE replay needs; (iii) external consumption.
* **"-Lite" variants (definition):** A *-Lite* face removes optional fields only (never claims), keeps the same typing as its full counterpart, and retains pins for any numeric content. Upgrading from *-Lite* to full is a monotone **add-fields** operation (no retractions).

#### E.17:5.3 - The publication-face kit

The optional morphism-publication profile uses representation-side constructors, not another viewpoint ontology:

1. `FaceObj_s` is the conceptual object component for publication face designator `s`.
2. `F_face` is the finite set of exact face-use designators. Its default formality order is `PlainView <= TechCard <= InteropCard`; `AssuranceLane` remains independent.
3. `Emit_s(-) : EpMorphism -> FaceMorph_s` constructs the candidate face episteme and publication-form content for `s` when this formal profile is current.
4. The coherence rules in section 6 and the pin policy govern this representation-side construction.
5. `InteropCard` may carry exact interoperability-concern references; concrete exchange schemas remain outside Part E.

`FaceObj_s`, `FaceMorph_s`, and `Emit_s` are local conceptual-form symbols. They are not public U-kinds, `U.Viewpoint` epistemes, `U.View` individuals, publication occurrences, or presentation carriers.

**Result.** `MVPK(f,F_face)` yields a C.13 collection of exact face-use epistemes and their selected publication forms. For each actual publication, E.24.PUB separately tests form expression, carrier bearing, and the five-participant publication occurrence with its declared audience, bounded use, and recurrence rule. A.6.3 construction, E.17.0 conformance, A.22 organization, and C.29 representation remain separately governed. If a current use depends on organization among face epistemes, select exact `U.Structure` under A.22 from the exact collection, exact obtaining organizing relations, applied constraints, and use frame; the face collection does not supply that structure by itself. `PromoteFace[s->t]` changes publication formality; it changes neither episteme identity nor viewpoint membership and adds no claims.

#### E.17:5.4 - EntityOfConcern-side input and output vs publication (normative convention)

1. **Input and Output are signature-side declarations.** The **Input and Output** sections of a morphism describe declared input and output data or episteme types under the morphism signature; they do **not** depend on any publication face.
2. **No duplication on faces.** MVPK faces **do not duplicate** Input and Output lists; they publish a **minimal profile**: **presence-pins**, **CG-Spec and CHR references**, and **EditionId** only.
3. **Signature reserved to signature-governed entities.** Use **Signature** only for entities already governed by signature patterns, such as `U.Signature`. On faces, use **TechName** or **PlainName**.
4. **Set-returning comparison.** Whenever a face shows selection or comparison, it returns sets or declared partial orders and does not hide scalarization; cite a `ComparatorSetRef` for any total order.
5. **Bridge crossing penalties.** Crossings cite Bridge and CL; publish `Φ(CL)` and `Φ_plane` ids; penalties apply to R only (never F or G).
6. **Carrier references and relation positions.** On first mention, name carrier references and any A.10 or G.6 source-currentness or provenance records when downstream reliance is current; keep `U.Work` occurrences distinct from epistemic claims via relation positions.
7. **Publication is not execution.** Faces carry no time or resource semantics; any build, render, or upload work is separate **`U.Work`**.

#### E.17:5.5 - Pin & Publication characteristics (normative; never "axes")

**Intent.** Make pinning and publication-time measurement claims explicit, typed, and auditable without importing geometric metaphors. This section introduces **Publication characteristics** (PC) as CHR-grounded, publication-facing facets that can appear on MVPK faces under a declared scope and viewpoint.

**Terminology (aligned with CHR-MM & UNM).**
* **Characteristic** (`U.Characteristic`): a measured aspect as defined in CHR-MM (entity characteristic or relation characteristic with a chosen **Scale**).
* **CharacteristicSpace** (`U.CharacteristicSpace`): a CHR-typed product of slots used by dynamics and measurement theories (A.19).
* **Publication characteristic** (`U.PubCharacteristic`, **PC**): a declarative facet that a face can expose about a morphism under the exact publication viewpoint resolved by `publicationViewpointRef`. Each PC is grounded by CHR and CG-Spec epistemes and pinned by unit, scale, reference-plane, and edition. PCs are not geometry and do not define axes.

**PC catalog (initial set).** MVPK defines a minimal open set of PCs that are frequently shown on publication faces:
* **PC.Number** - numeric or comparable entries (thresholds, budgets, counts). **Pins required:** unit, scale, reference-plane, edition.
* **PC.EvidenceBinding** - bindings to evidence carriers and policies (e.g., PathSliceId, BridgeId, CL notes).
* **PC.ComparatorSetRef** - an explicit comparator family for declared partial orders on faces.
* **PC.CharacteristicSpaceRef?** - optional pointer when a face cites the **space** in which a claim is interpreted (e.g., dominance on a declared space).

The catalog is open to extension through `U.PubCharacteristic`. PCs remain declarative and do not embed mechanisms.

**Norms (E17-PC).**
* **E17-PC-1 (CHR grounding).** Every PC that yields numeric or comparable content cites CHR and CG-Spec references and carries pins {unit, scale, reference-plane, edition}.
* **E17-PC-2 (Lexical discipline - no geometry).** Faces and PCs avoid "axis", "dimension", or geometric metaphors; use **Characteristic**, **slot**, **CharacteristicSpace** where applicable (**E.10**; see also A.19).
* **E17-PC-3 (No hidden arithmetic).** Faces do not smuggle aggregation or normalization; any such logic lives in **CG-Spec** (UNM or NormalizationMethod) and is cited by `...Ref.edition`.
* **E17-PC-4 (Plane & crossing).** When a PC depends on **ReferencePlane** or crosses ReferencePlane crossings or Context crossings, the face cites `BridgeId` and CL policy ids; penalties apply to the R channel only.
* **E17-PC-5 (Edition pinning).** PCs that rely on maps or distances pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and, if used, both `CharacteristicSpaceRef.edition` and `TransferRulesRef.edition`.
* **E17-PC-6 (Viewpoint scope).** Each PC instance declares the exact `publicationViewpointRef` under which it applies; `PromoteFace[s->t]` does not add or widen claims and at most reindexes or annotates the publication form.
* **E17-PC-7 (Comparator or SetSemantics edition).** `PC.ComparatorSetRef` and any `SetSemanticsRef` carry edition identifiers; cards are re-emitted upon edition change with change notes.

**Publication faces and responsibilities.**
* **PlainView** includes **PC.Number** only when fully pinned; otherwise it uses **compare-only** language.
* **TechCard** carries **PC.Number**, **PC.ComparatorSetRef**, and **PC.CharacteristicSpaceRef?** when faces enable declared ordering.
* **AssuranceLane** carries **PC.EvidenceBinding** and the pins for any numeric claims it relays.
* **InteropCard** references PCs conceptually while remaining notation-neutral in Part E; schemas map in the interop annex.

**Rationale.** MVPK is a publication discipline, not a measurement calculus. By naming **Publication characteristics** and pinning them to CHR and UNM, we:
1. prevent geometric leakage (no "axes");
2. keep publication neutral yet auditable;
3. enable set and ordering behavior on faces via explicit **ComparatorSet**;
4. make plane-crossing requirements first-class and checkable by declared publication checks or **OperationalGate(profile)** GateChecks.

**Extensibility.**
* **E17-PC-Ext-1 (Open catalog).** New PCs are added under `U.PubCharacteristic` when they are declarative and CHR- and UNM-grounded.
* **E17-PC-Ext-2 (Kinding).** New PCs declare `kind ∈ {Number, EvidenceBinding, SelectorHint, ...}` and a **pinning requirement**.
* **E17-PC-Ext-3 (Twin-register names).** Supply **Tech** and **Plain** twins; avoid tokens that collide with E.10 bans; do not coin "...Space" names for publication forms.
* **E17-PC-Ext-4 (Edition discipline).** If a PC depends on a definition or specification publication, edition-pin the reference (`...Ref.edition`) and document edition-change rules.

**Adding invariants.**
1. Place **new invariants** for PCs in **CG-Spec** (specification-use relation position), not on faces; supply acceptance tests.
2. Version any affected **CharacteristicSpace**; publish embeddings if semantics change; never mutate slots in place.
3. Update the relevant **GateChecks** or **GateProfiles** (`A.21`, including GateCrossing checks and crossing-visibility checks from `E.18`, `F.9`, and relevant Part G bridge or crossing wiring) to warn or block on invariant violations; never weaken functorial invariants.
4. State edition and edition-change rules; name the conformance check that detects the changed invariant and state the **Lean-profile downgrade** result (advisory vs block) where applicable.

#### E.17:5.6 - Author ergonomics (non‑normative)
*Quick author steps (three steps and a micro-template):*
1. **Declare `F_face` and profile.** Choose the exact face-use designators and whether faces are full or Lite.
2. **Pin once, reuse everywhere.** Attach `{UnitType, ScaleKind, ReferencePlane, EditionId}` to the arrow; cards reference these pins by ID (no duplication).
3. **Emit & verify.** Generate all faces from the arrow.

*Guidance:* treat *‑Lite* as **field‑drop only**; never add claims in *‑Lite*.

### E.17:6 - Rules and Invariants (normative)

**Publication-composition local test bundle.** A face that claims compositional publication passes five local tests:

1. `identity`: `Emit_s(id_X)` is the identity face morphism for `FaceObj_s(X)`;
2. `composition witness`: the face for `g o f` matches the composition of the faces for f and g, or is marked non-compositional or explanatory-only;
3. `no-new-claim diff`: comparison with the selected source episteme shows only formatting, indexing, pinning, or conservative construction;
4. `monotone promotion`: a richer face adds fields, pins, or typing without retracting or strengthening the source claim;
5. `scope non-widening`: `U.PublicationScope` stays within the exact claim or work scope used by the selected description.

For composable arrows `X -f-> Y -g-> Z` and exact `s,t` in `F_face`:

1. **Functoriality and typing per face.**
   * `Emit_s(id_X) = id_{FaceObj_s(X)}`.
   * `Emit_s(g o f) = Emit_s(g) o Emit_s(f)` only when the face carries the local witness.
   * If `f : X -> Y`, then `Emit_s(f) : FaceObj_s(X) -> FaceObj_s(Y)` is total in the selected formal substrate. An ill-typed composite blocks that formal claim; it is not repaired by weakening conformance.
2. **Face-promotion coherence.**
   * If `s <= t`, the t-face is a more explicit publication form for the same selected source claims.
   * `PromoteFace[s->t]_X : FaceObj_s(X) -> FaceObj_t(X)` is natural in X.
   * Identity and composition of `PromoteFace` follow the selected formal substrate. `AssuranceLane` is outside the default formality chain.
3. **Source episteme and construction.**
   * Every `Emit_s` use names the exact source episteme edition and exact publication viewpoint reference.
   * When another episteme is actually constructed from the source, A.6.3 may govern that source-to-receiving relation. The face constructor is not a species of `U.EpistemicViewing`, and A.6.3 does not establish `U.View` membership.
   * Changed claim content, EntityOfConcern, or effective reference scheme identifies another episteme under C.2.1. Changed form, carrier, or publication occurrence does not by itself.
4. **Pin discipline.** Numeric or comparable claims used from a face retain exact unit, scale, reference-plane, and edition pins under their direct characteristic and measurement patterns.
5. **Publication is not work.** Build, rendering, upload, or delivery is exact `U.Work` performed by a system under exact role and method relations. A face, emitter symbol, view episteme, or publication occurrence does not act.
6. **Publication and carrier separation.** E.24.PUB identifies the selected episteme edition, publication occurrence, form, and presentation carrier separately. Provenance and assurance relations remain under A.10, G.6, and B.3.
7. **Cross-context and reference-plane use.** When a face makes a current bridge or translation claim, recover the exact contexts, senses, bridge, and governing relation. Visual juxtaposition and scheme difference alone establish none of them.
8. **PublicationScope discipline.** For a face use v selecting episteme E, `PublicationScope(v)` does not exceed the claim scope on which that publication relies. A capability description may also cite a work scope, but the publication scope does not grant work admissibility. `PromoteFace` does not widen either scope.

The equations are conceptual-form constraints on the optional morphism-publication profile. They do not turn face symbols, formulas, or diagrams into world-side relations, viewpoints, views, publication occurrences, or work.

### E.17:7 - Objects used by the optional formal profile

| Object or symbol | Exact job | Boundary |
|---|---|---|
| source episteme E | carries the selected claims about exact EntityOfConcern | identified under C.2.1 |
| `publicationViewpointRef` | resolves exact publication viewpoint episteme P | designator and reference remain distinct from P |
| `F_face` | finite C.13 collection of face-use designators or descriptions for this profile | not a viewpoint bundle or `U.ViewFamily` |
| `Emit_s`, `FaceObj_s`, `FaceMorph_s`, `PromoteFace` | conceptual-form symbols for constructing and checking face content | governed as representation-side formalism; no U-kind membership follows |
| receiving face episteme, when constructed | separately identified episteme whose claims are checked against the source and P | A.6.3 construction and E.17.0 conformance are independent claims |
| publication occurrence, form, carrier | makes the selected episteme available to a declared audience and use | E.24.PUB owns identity and obtaining |

The author selects exact source E, exact P, and face profile `F_face`. A system performs any authoring, rendering, checking, or publication work. MVPK names the publication method and constraints; it neither acts nor mints a view-family entity.

### E.17:8 - Archetypal Grounding (SoTA-aligned Local Tests)

Read these examples as local tests for MVPK invariants, not as source citations by reputation.

1. **Composite service pipeline (`InteropCard` + `AssuranceLane`).**
    `f: Parse → Normalize`, `g: Normalize → Score`.
    `InteropCard(g∘f)` is an interoperability face whose path claim matches the declared relational composition of the two source claims; `AssuranceLane(g∘f)` cites exact evidence or provenance records under their own governors. The faces neither establish that composition nor become evidence carriers.
2. **Control loop morphism (`TechCard` + `PlainView`).**
    * For `h: Setpoint → Actuation`, `TechCard(h)` is a typed card with units; `PlainView(h)` narrates the same mapping with no new claims. (Monotone formalization echoes refinement‑typed specification toolchains.)
3. **Optics-informed composition witness.**
    * Profunctor and optic accounts are useful only as a source idea for why compositional publication matters. The local FPF test is still the MVPK witness: emit the face for `g∘f`, compose the emitted faces for `f` and `g`, and compare them. If the comparison is not supplied or fails, the face stays non-compositional or explanatory-only; optics vocabulary does not carry the rule by analogy.

4. **Functional-description publication (`PlainView` + `TechCard`).**
    A principle scheme or functional diagram can publish a readable relation from signature or principle episteme content to method-family selection, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, and result measurement. The MVPK faces can help a team inspect that relation and prepare a work plan, but they do not turn the diagram, table, screen, or export into work occurrence, gate passage, evidence, engineering justification, or supervisory or control architecture. For those uses, the team first recovers the existing typed project-side FPF kind and reference named by value that carries the claim when available: `A.15.4` appearance-based reliance repair when the face is being used as the reason before the governing pattern slot or relation is named, project `U.Method`, `U.WorkPlan`, and dated `U.Work` occurrence under `A.15` and `A.15.1`, evidence or provenance path under `A.10`, engineering-justification record under `B.3`, gate or constraint decision under `A.20` or `A.21`, or supervisory or control architecture record under `B.2.5`. If no existing typed project-side FPF record or source relation carries the needed claim, create only a prospective repair request, prospective decision request, prospective work-plan entry, or explicit missing-source-relation note; do not backdate evidence, gate passage, work occurrence, release permission, engineering justification, or assurance for the earlier claim.

### E.17:8.1 - Bias-Annotation

E.17 blocks publication-face bias: a face, card, view, rendering, source pointer, dashboard tile, or generated explanation is treated as if readability or layout created the underlying claim, evidence, work, gate, authority, or release relation. It also blocks source-proximity bias: a source-proximate face points near source material or a source relation, but the operative source relation still has to be recoverable by value.

### E.17:9 - Conformance Checklist (normative)

`CC-MVPK-FD` is the functional-description guard in §5.1a. It is conditional on a functional-description publication face and does not function as the first universal MVPK gate.

A conformance check is kept only if it changes the next bounded use of the publication face, blocks a concrete overclaim, or preserves a source reference or reopen condition needed for the declared bounded use.

#### E.17:9.1 - Core ordinary checks

| ID | Requirement | Practical test |
| --- | --- | --- |
| **CC‑MVPK‑1 (Viewpoint explicit)** | Each face use carries `publicationViewpointRef : U.ViewpointRef` resolving to one exact admitted publication viewpoint episteme; any `U.View` claim additionally cites the obtaining E.17.0 conformance relation. | The card exposes the reference and optional `PublicationVPId` designator; generation or selection alone is not accepted as membership. |
| **CC-MVPK-1a (Publication relations explicit when load-bearing)** | A claimed publication occurrence has one selected episteme edition, audience declaration, bounded-use declaration, exact form, and exact carrier; `PublicationFormExpressionRelation` and `PublicationFormBearingRelation` obtain separately. | The five values and both supporting relations resolve; changed participants or an availability gap produce the E.24.PUB recurrence result rather than reidentifying an unchanged episteme. |
| **CC‑MVPK‑3 (No content extension)** | `PlainView`, `TechCard`, and `InteropCard` add **no new claims** beyond the underlying Description epistemes, including Description epistemes admitted for specification use. | Red‑line vs Description episteme, including any exact specification-use source, shows only formatting or indexing. |
| **CC-MVPK-4 (Pins and source references)** | Numbers and thresholds pin {...}. **Lean exception:** at MVPK-Min or MVPK-Lite profiles, EditionId can remain coarse; ordinal claims stay compare-only (no means or z-scores). | Validation shows pins present or compare-only mode engaged. |
| **CC-MVPK-4j (PublicationScope present)** | Each publication-face use declares `U.PublicationScope` under A.2.6. | Exact scope reference is recoverable. |
| **CC-MVPK-5 (Carrier reference)** | First mention includes carrier references and any A.10 or G.6 source-currentness or provenance records when carrier work, rendering work, reliance, evidence, or replay is present. | Carrier and provenance references are visible when used. |

#### E.17:9.2 - Conditional checks

| ID | Requirement | Practical test |
| --- | --- | --- |
| **CC‑MVPK‑0 (Lean publication guard)** | For Lean profiles, a minimal guard runs: (i) set‑returning selection present; (ii) ReferencePlane present; (iii) any crossing cites BridgeId+CL with penalties applied to R only. | Validation report shows presence bits; penalties apply to R only. |
| **CC‑MVPK‑2 (Functoriality)** | `Emit_s(id)` is identity; `Emit_s(g∘f) = Emit_s(g)∘Emit_s(f)`. | Compose two cards and diff with the card of the composite. |
| **CC-MVPK-3b (Boundary claim-set integrity)** | If a published arrow is a boundary, interface, or protocol and an A.6.B claim set exists (`L-*`, `A-*`, `D-*`, and `E-*`), then normative text on faces is traceable to that claim set (prefer claim-ID citations); faces do not become a second boundary specification. | Lint flags uncited normative clauses; faces reduce to {claim-ID citations + informative commentary}. |
| **CC‑MVPK‑4b (Lean assurance)** | If `AssuranceLane‑Lite` is used, presence bits for {PathSliceId?, BridgeId?} suffice; full evidence-carrier lists stay with the governing evidence source. | Presence bits visible; required evidence-carrier refs stay outside Lite. |
| **CC-MVPK-4c (Input and Output vs publication)** | Faces **do not** restate Input and Output; they carry **presence-pins, source references, and EditionId** only. | Face inspection shows no Input and Output duplication. |
| **CC-MVPK-4d (Set-returning ordering)** | Any selection or comparison on faces returns sets or declared partial orders with a **ComparatorSet** citation. | No hidden scalarization; ComparatorSetRef present. |
| **CC‑MVPK‑4e (Signature on faces — banned)** | The term **“signature”** is **not used** on faces; use **TechName** or **PlainName**. | Token scan: no “signature” on faces. |
| **CC‑MVPK‑4f (PC discipline)** | Any numeric or comparable publication uses **Publication characteristics** (PC) and carries pins {unit, scale, reference‑plane, edition}. | Cards show PC fields + pins; validation passes. |
| **CC‑MVPK‑4g (No axis or dimension)** | Faces avoid “axis”, “dimension”, and “plane” metaphors except **ReferencePlane**; use CHR terms (**Characteristic**, slot, or **CharacteristicSpace**). | Lexical check flags none; only `ReferencePlane` appears. |
| **CC‑MVPK‑4h (Edition pins on defs)** | Where maps, distances, or spaces are cited, the face pins `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `CharacteristicSpaceRef.edition?`. | Validation shows edition fields populated. |
| **CC‑MVPK‑4i (Crossings gated)** | ReferencePlane crossings or Context crossings cite **Bridge + CL** policies; penalties apply to **R‑channel** only. | IDs present; R-channel penalty application verified in harness logs. |
| **CC‑MVPK‑4k (Subset‑of underlier)** | For views about epistemes or capabilities, `PublicationScope ⊆ ClaimScope or WorkScope`; reindexing **does not widen** it. | Subset witness passes; promotion diff shows no widening. |
| **CC‑MVPK‑6 (Γ‑separation)** | No cost, time, or data-spend on publication morphisms. | CI shows proof records or witness records; gate validation passes. |
| **CC‑MVPK‑7 (Reindexing monotone)** | If `s ⪯ t`, then `Emit_s(x) ⪯ Emit_t(x)`. | `TechCard` ≤ `InteropCard` (more structure, same claims). |
| **CC‑MVPK‑8 (`publication-face kind` discipline)** | Only literal `publication-face kind` values **publication face/form** or **interop publication form** are used; faces are named **...View** or **...Card**. | Token scan; no “rendering” or “presentation” as `publication-face kind` values. |
| **CC‑MVPK‑9 (Reindexing naturality)** | Conceptual-form coercions `PromoteFace[s->t]` exist, are total in the selected formal substrate, and commute with composition. | The local witness uses `PromoteFace` and is not overread as a world-side relation. |
| **CC‑MVPK‑10 (Iso‑preservation)** | Isomorphisms in `U` remain isomorphisms under each viewpoint. | Cards show mapped inverses or an iso‑witness. |
| **CC‑MVPK‑11 (Typing & totality)** | Ill-typed composites are rejected at `FaceObj_s` rather than weakening the selected conceptual-form rules. | Type-check fails early; no best-effort composition claim appears on cards. |
| **CC‑MVPK‑12 (Bridge+CL on crossings)** | Any cross‑Context view or ReferencePlane-crossing view cites **Bridge + CL** policy ids. | IDs present on `TechCard` or `AssuranceLane`. |

### E.17:10 - Common Anti-Patterns and How to Avoid Them

1. **“Presentation logic” as semantics.**
    *Fix:* Move any logic to `Describe_EoC_DescEp`, an exact specification-use or episteme-refinement gate, CG‑Spec, or KD‑CAL; keep views declarative; publication adds **zero** claims.
2. **Publishing only view objects.**
    *Fix:* The optional formal profile constructs faces for `g o f`, not only endpoint faces for `FaceObj_s(X)`, `FaceObj_s(Y)`, and `FaceObj_s(Z)`. A system performs the construction work; MVPK does not act.
3. **Unpinned numbers.**
    *Fix:* Reject card; supply **pins** plus CG and CHR references.
4. **Face presented as a view without conformance.**
    *Fix:* Resolve the exact viewpoint episteme and apply E.17.0 to the exact candidate episteme; redesign or re-emit the face only after the semantic repair.
5. **`InteropCard` equivalent to `TechCard` duplication.**
    *Fix:* `InteropCard` can refine typing or shape but cannot contradict `TechCard` (reindexing monotone).

### E.17:11 - Consequences

| Benefit | Why it matters | Trade-off and mitigation |
| --- | --- | --- |
| **Arrow traceability.** | Composition preserved across views enables chain‑of‑evidence on pipelines. | Slight authoring overhead → MVPK templates. |
| **Review-ready faces.** | Pins plus CHR references make numeric claims verifiable. | Declared publication checks perform MVPK checks; project gates stay with the relevant `OperationalGate(profile)` or `GateDecision` source when the gate claim is present. |
| **Terminology hygiene.** | Clear View vs Viewpoint, Publication vs Presentation. | Enforce publication-face-kind discipline tokens in CI. |
| **Notation independence.** | Viewpoints talk concerns, not tools. | Provide adapters to local publication toolchains. |

### E.17:11.5 - Rationale

Multi-view publication is needed because one description can serve several concerns without one view becoming the whole object. A publication unit, viewpoint, correspondence relation, freshness condition, and source relation must be explicit enough that practitioners can rely on the right face for the current use while returning evidence, assurance, decision, architecture, and release claims to their direct governing patterns.

### E.17:12 - SoTA-Echoing: Adopted And Adapted Invariants And Rejected Shortcuts

**SoTA alignment rule.** Read each row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and Relations of this pattern.

| Source idea and current source | Local FPF invariant and practical local test | Adopted, adapted, or rejected shortcut |
| --- | --- | --- |
| Joint ISO, IEC, and IEEE 42010:2022 architecture-description practice, used as established practice lineage rather than current architecting SoTA, separates architecture description, stakeholder concern, viewpoint, view, model kind, correspondence, and correspondence rule. | MVPK publishes one source-pinned face over an exact selected episteme edition; every face used for downstream reliance resolves its exact viewpoint episteme, keeps independent E.17.0 view membership, publication occurrence, form, carrier work, rendering work, correspondence relation, concrete exchange envelope, and evidence envelope separate, and passes the no-new-claim diff. | Adopt the object distinctions; reject the shortcut where a readable face or standards label becomes a view, evidence, work occurrence, gate passage, release permission, bridge relation, or exchange authority by presentation alone. |
| Profunctor and optic accounts (2017-2019; source classification = research or theory line, not admissible for downstream reliance without local witness) provide source material for compositional views that compose like arrows. | MVPK adopts only local publication-composition tests: identity, composition witness, no-new-claim diff, monotone promotion, and scope non-widening. | Adopt the five-test publication-composition bundle; reject optics vocabulary as proof by analogy or as a replacement for local witnesses. |
| Refinement-governed ecosystems (2016+; source classification = widely used technical practice) keep units, scales, and value-kind constraints attached to values. | MVPK publication faces carry pins and CHR and CG references; local test: numbers, thresholds, and characteristic claims on faces have units, scales, reference-plane relation and edition relation when relied on downstream. | Adapt pin discipline; reject readable numbers as self-validating values. |
| Interoperability and evidence-envelope practice (source classification = stable standard or established practice, depending on the concrete envelope) separates exchange format and carrier evidence from the claim being carried. | MVPK faces can expose evidence carriers or exchange envelopes, but concrete formats belong outside Part E; local test: the face adds no claim and points back to the governing source or evidence path. | Adapt envelope discipline; reject treating envelope presence as semantic authority, evidence sufficiency, work occurrence, or gate passage. |

(References are selected because they supply source material for local MVPK invariants and tests; MVPK remains notation-agnostic.)

### E.17:13 - Relations
* **Architecture ADR projection boundary:** `C.32.ADR` is the architecture-specific publication projection for `ArchitectureDecisionDescription@Project`. E.17 keeps publication face, source episteme, carrier, scope, and downstream typed value separate for the broader MVPK claim.
  In that name, `@Project` is a compatibility and retrieval cue only. E.17 infers no project entity, composite-work identity, context, authority, viewpoint, or parthood from it; `C.30.AD` and `C.32.ADR` must identify the exact composite `U.Work` and the direct description-use or publication-use relation when project locality is current.

* **Builds on:** `C.2.1` for selected-edition identity; `E.24.PUB` for `PublicationFormExpressionRelation`, `PublicationFormBearingRelation`, and the exact publication occurrence; `E.17.0` for viewpoint and `U.View` membership; `A.22` for selected structure; `C.29` for representation; `A.7` and `E.10.D2` for carrier, front-end, EntityOfConcern, Description-episteme, and specification-use discipline; `A.6.2`-`A.6.3` for optional source-to-candidate construction; `E.8` and `E.10` for authoring and publication-language discipline; and Part F and Part G for bridge, terminology, characteristic, and pin discipline.
* **Constrains:** publication-face-emitting automation and hand-written publication faces. When one receiving episteme is actually constructed from a source, A.6.3 governs that separate relation; the face and publication occurrence are not species of viewing. Readable form creates no second EntityOfConcern-to-Description mechanism, specification-use gate, evidence path, gate decision, work occurrence, assurance record, release source, or bridge declaration.
* **Neighboring-pattern boundary use:** use the compact boundary aid in `E.17:5.1d` when a publication-facing unit starts carrying work, reliance, evidence, assurance, gate, release, bridge, explanation, comparison, retargeting, carrier, or front-end claims beyond ordinary publication use. This Relations section cites that aid instead of repeating the whole map.
* **Part F bridge wording boundary:** when the publication face uses or invites "same", "equivalent", "align", "map", substitutable, interchangeable, attribute, entity, or profile matching, or other bridge-wording claim pressure across contexts, the wording repair belongs to Part F and `A.6.9`; the bridge relation belongs to `F.9` or `F.9.1`. `E.17` does not create a local bridge taxonomy.
* **Coordinates with:** `C.2.P` for exact source-expression and source-to-use recovery before publication-facing wording is relied on; `A.15.4` for appearance-based reliance repair; C-cluster selection or archive patterns when exact face epistemes are selected or retained; CHR and UNM for measurement and normalization semantics; `F.9` or `F.9.1` for exact bridge relations; and `A.6.9` for sameness wording. Publication faces remain publication forms and uses, never views by face status.

### E.17:14 - Minimal authoring template (Part E)

**Header:** `MVPK v<edition> - F_face = {PlainView <= TechCard <= InteropCard; AssuranceLane independent}`
**For each arrow f:** construct `{Emit_s(f) | s in F_face}` with the exact selected source episteme, `publicationViewpointRef`, `U.PublicationScope`, pins, CHR and CG references, and selected publication form. When an actual publication is current, also name the exact audience and bounded-use declarations, carrier, form-expression relation, form-bearing relation, and publication occurrence. If compositional publication is claimed, carry the local `Emit` and `PromoteFace` witnesses as conceptual-form constraints.

### E.17:15 - Manager’s one‑page review (copy‑paste)

> We publish every selected source episteme under one exact publication viewpoint and declared face profile. A face claiming compositional publication carries the local conceptual-form witness; otherwise it remains non-compositional or explanatory-only. Each face adds no claim and keeps exact pins and source references. An actual publication separately names its selected edition, audience, bounded use, form, carrier, expression, bearing, and availability occurrence; none becomes the view episteme, evidence, Work, or a world-side subject relation.

### E.17:End

