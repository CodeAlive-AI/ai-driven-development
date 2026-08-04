## A.6.3.RT - Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition

> **Type:** Specialization pattern
> **Status:** Stable
> **Normativity:** Normative

### A.6.3.RT:1 - Problem frame

Use this pattern when one exact source episteme `X` and one exact receiving episteme `Y` concern the same exact EntityOfConcern but use different declared representation schemes or reasoning media: prose to table, table to diagram, diagram to structured notation, or another declared representation regime. Before calling either endpoint a representation episteme, recover its exact C.2.1 claim content, exact EntityOfConcern, and effective `U.ReferenceScheme`. A file, page, table, diagram, model display, publication occurrence, publication form, or carrier may expose an endpoint; none substitutes for it.

**Governed construction.** The ordinary governed object is the exact A.6.3 viewing declaration `v : X -> Y`, including the claim-content construction, relation between the two effective reference schemes, preserved content, admitted loss, prohibited strengthening, and applicability. The stronger `RepresentationSchemeTransitionRelation@Context` occurrence is opened only for the later-specific case in which a system actually performs representation-transformation Work and all six exact relation participants in section 4.1.a.1 are present. The viewing declaration, relation occurrence, performed Work, and any transition-description episteme are four different objects.

**Primary EntityOfConcern.** `X` and `Y` have the same exact EntityOfConcern. The transition-description episteme, when needed, instead has the exact transition-relation occurrence as its own EntityOfConcern. Neither use changes the world-side entity or makes a relation involving that entity obtain.

**First useful move.** Name `X` and `Y` with their three C.2.1 identity discriminators; state the exact `v : X -> Y` and the relation between their effective reference schemes; then state preserved claims, loss or recoverability, admissible use, non-admissible downstream use, and return condition. Only when asserting the `...@Context` occurrence, additionally name the independently constituted source and receiving scheme-description epistemes, an exact selected bounded model-use structure, and actual representation-transformation Work. Recover correspondence, C.29 representation, viewpoint conformance, publication, form, carrier, grounding, and receiving use separately when one of them is current.

**What goes wrong if missed.** A table, diagram, notation, model display, or decoded rendering is treated as an episteme endpoint merely by appearance. Scheme difference then hides an EntityOfConcern shift, unsupported claims, absent transformation Work, unproved correspondence, or a publication/form/carrier substitution.

**What this buys.** One inspectable same-EntityOfConcern episteme construction, plus a separately testable historical transition occurrence only when its six participants and actual Work exist. Representation-factor and reasoning-medium change, preservation, loss, and return remain visible without converting a rendering into knowledge, work, a view, or authority.

**Ordinary use.** For inspection, source-finding, comparison, technical review, or reversible planning preparation, a readable statement of `X`, `Y`, `v`, preservation, loss, use, and return is normally sufficient. Do not materialize the `...@Context` occurrence merely because the receiving form is visible.

**Reliance-facing use.** Open the fuller continuity-review content only when the receiving episteme will be externally relied on, disputed, cited as an admissibility reason, used across bounded model-use structures or schemes, treated as release, gate, or work-preparation justification, carried through decode-mediated access, or used for temporal, dynamics, or transformation-flow currentness. Each stronger claim still requires its direct governor.

**Not this pattern when.** Use `ConservativeRetextualization` when only wording changes, explanation governance when explanation is primary, `A.6.4` when the exact EntityOfConcern changes, and the carrier or extraction governor when no receiving episteme has yet been constituted. Use `A.6.3.CSC` when exact receiving episteme `Y` remains honest only under a narrower admissible use, explicit loss, and return to exact source episteme `X` or its governed source relations.

### A.6.3.RT:2 - Problem

Without a dedicated named pattern for representation-scheme transitions:
1. teams treat text-to-table, table-to-diagram, and notation shifts as if they were all the same kind of harmless rewrite;
2. changes in reasoning medium and recoverability remain implicit;
3. latent representation or distributed representation cases tempt users to treat geometry or feature clusters as ontology-by-default;
4. users cannot tell when a case is still same-entity viewing and when it has become retargeting, explanation, carrier work, or decode-mediated reconstruction;
5. representation factors governed near `C.2.7` are discussed rhetorically rather than as explicit deltas.

### A.6.3.RT:3 - Forces

- **Same entity, different reasoning medium.** Teams need different representational forms without silently changing the EntityOfConcern.
- **Legibility vs recoverability.** A clearer representation is useful only if users can still recover how it relates to source claims, source-relation records, and pins.
- **Representation change vs EntityOfConcern shift.** A new notation or geometry can make structure more visible; that visibility does not establish a new EntityOfConcern or ontology.
- **Recoverability before decode ambition.** Start from cases where recoverability can be reviewed directly before leaning on decode-mediated reconstruction.
- **Governing-pattern restraint.** This pattern remains under `A.6.3`; explanation governance, retargeting, bridge work, and carrier work remain with their direct patterns.

### A.6.3.RT:4 - Solution — entityOfConcernRef-preserving representation-scheme transition under `A.6.3`

#### A.6.3.RT:4.1 - Informal definition

> `RepresentationSchemeTransition` is a named pattern specialized under `A.6.3 U.EpistemicViewing` for entityOfConcernRef-preserving transitions across declared representation schemes.
>
> It preserves `entityOfConcernRef`, keeps the representation change effect-free, and makes explicit what changes in representation factors, reasoning medium, recoverability, and loss profile.
>
> It may move between prose, table, diagram, structured notation, or another declared representation regime. It may not silently change the EntityOfConcern, silently import bridge semantics, or treat decode-mediated structure as if it were directly given.

#### A.6.3.RT:4.1.a - Pattern, construction, occurrence, Work, and description

`RepresentationSchemeTransition` is a pattern description specialized under `A.6.3`. One ordinary case first identifies exact source episteme `X`, exact receiving episteme `Y`, and exact viewing declaration `v : X -> Y`. The declaration is a mathematical and claim-bearing construction; it performs no Work and is not a relation occurrence merely because a table, diagram, or file was produced.

Keep four objects distinct:

1. the A.6.3 construction `v : X -> Y`;
2. an optional positive `RepresentationSchemeTransitionRelation@Context` occurrence satisfying the rule below;
3. exact dated representation-transformation Work performed by a system under A.15.1; and
4. an optional C.2.1 episteme that describes the occurrence, preservation, loss, use, and return.

#### A.6.3.RT:4.1.a.1 - Six-participant transition relation and non-hybrid entry

`RepresentationSchemeTransitionRelation@Context` is the later-specific, bounded-model-use species of `U.Relation`. The suffix `@Context` is a retrieval label for one exact A.1.1 Plain **bounded context**, technically an independently selected `BoundedModelUseStructure : U.Structure`; it admits no discarded generic context kind or reference and no description-context field.

```text
RepresentationSchemeTransitionRelation@Context <: U.Relation:
  TransitionModelUseStructureSlot = <TransitionModelUseStructureSlot, U.Structure, U.StructureRef constrained to one exact BoundedModelUseStructure>
  PreservedEntityOfConcernSlot = <PreservedEntityOfConcernSlot, U.Entity, U.EntityRef>
  SourceRepresentationEpistemeSlot = <SourceRepresentationEpistemeSlot, U.Episteme, U.EpistemeRef>
  ReceivingRepresentationEpistemeSlot = <ReceivingRepresentationEpistemeSlot, U.Episteme, U.EpistemeRef>
  SourceRepresentationSchemeDescriptionSlot = <SourceRepresentationSchemeDescriptionSlot, U.Episteme, U.EpistemeRef>
  ReceivingRepresentationSchemeDescriptionSlot = <ReceivingRepresentationSchemeDescriptionSlot, U.Episteme, U.EpistemeRef>
  direction = SourceRepresentationEpistemeSlot -> ReceivingRepresentationEpistemeSlot
```

These six SlotSpecs and the direction are the exact `RelationSignature`. The two endpoint epistemes are independently constituted under C.2.1: each has exact claim content, the same exact EntityOfConcern bound in `PreservedEntityOfConcernSlot`, and its own effective `U.ReferenceScheme`. Each scheme-description episteme is also independently constituted; its claim content describes one exact source or receiving scheme, its EntityOfConcern is that scheme, and its own effective reference scheme makes the description interpretable. Neither a scheme label nor a visible notation fills that position.

**Obtaining rule.** A positive occurrence obtains only when all of the following hold together:

1. all six participants resolve exactly and the `BoundedModelUseStructure` is already selected under A.1.1 because its model-use organization changes this transition use;
2. one system under an exact role assignment performs exact dated representation-transformation Work whose governed input, result, reference, or A.6.1 bindings use all six participant values for this transition;
3. the exact A.6.3 declaration `v : X -> Y` states the claim-content construction, the relation between the endpoint effective reference schemes, the same-EntityOfConcern condition, preserved content, explicit loss or recoverability, prohibited strengthening, and applicability for the receiving use; and
4. every correspondence on which the construction depends is an exact separately governed relation or claim, not a graph edge, similar content, scheme difference, or a generic correspondence record.

The Work, performer, role assignment, method, operation application, source-use relations, and any A.15.PROD inception claim remain under their direct owners and are not seventh relation participants or identity discriminators. Performed Work alone does not prove the A.6.3 construction or make the relation obtain. Conversely, an inspectable `v : X -> Y` without exact Work and an independently selected `BoundedModelUseStructure` remains an ordinary RT construction; do not assert `RepresentationSchemeTransitionRelation@Context`.

**Occurrence identity.** The occurrence is participant-determined by the complete six-participant tuple, including the exact source/receiving scheme-description pair. A change to any participant identifies another occurrence. A repeat Work episode, evidence change, publication occurrence, form, carrier, layout, transition-description edition, or C.29 output does not reidentify an unchanged participant tuple. Changing `X` or `Y` claim content, EntityOfConcern, or effective reference scheme first identifies another episteme and therefore another tuple.

#### A.6.3.RT:4.1.a.2 - Transition-description and source-relation epistemes

When the occurrence must be described for reuse or review, identify one ordinary C.2.1 transition-description episteme by:

- exact claim content that designates the six-participant occurrence and states the relied-on Work and viewing declaration, source-relation or correspondence dependencies, preserved and lost content, scheme and reasoning-medium delta, admissible use, non-admissible use, and return condition;
- that exact relation occurrence as its EntityOfConcern; and
- the effective `U.ReferenceScheme` under which those claims designate the occurrence and its participants.

This is an ordinary C.2.1 episteme, not a context-selection record, another relation, a work record, or a filled-card ontology. A changed description claim graph identifies another description episteme without changing the occurrence.

If the declared use needs a reference-bearing episteme for one exact source relation, identify it independently by its own C.2.1 triple: claim content designating the exact relation occurrence and stating its exact relation kind, signature, direct governor, and use in `v`; that source relation as EntityOfConcern; and its effective reference scheme. The episteme is not the source relation and citation does not make the relation obtain.

The endpoints of the transition are exact epistemes `X` and `Y`. A selected publication occurrence may make either edition available, a publication form may express it, a `U.PresentationCarrier` may bear that form, and a C.29 representation may correspond to it for an explicit modeling or reasoning use. None of those neighbors substitutes for an endpoint or enters the six-participant identity.

At least one explicit loss or recoverability claim is present. The description also states the receiving use and the condition for return to exact `X` or to an exact governed source relation. Changed EntityOfConcern exits to A.6.4; a receiving episteme that is useful only under a narrower-use card exits to A.6.3.CSC; narrative ordering exits to A.6.3.NAR. Viewpoint, `U.View` membership, grounding, publication, evidence, assurance, bridge, gate, and receiving Work remain independently governed.

#### A.6.3.RT:4.1.b - Local working vocabulary

Use this vocabulary only after the ordinary use field set leaves ambiguity or a claim-bearing relation-change question. Ordinary text-to-table, table-to-diagram, or diagram-to-notation cases do not need every term below; use only the term that changes the next representation decision or blocks a concrete overclaim.
- **Representation scheme** = the declared regime under which exact episteme claim content is represented and interpreted for the current use; a publication form or carrier may express that content but is not the scheme, episteme, or transition.
- **Reasoning medium** = the form-specific inspection possibilities users actually use when inspecting the published rendering.
- **Semiotic mode** = which meaning-bearing relation is doing the main work in the rendering, such as structural likeness, trace relation, index relation, conventional code, model-mediated correspondence, or decode-mediated recoverability.
- **Factor delta** = the explicit change in representation factors that matters for review.
- **Source-relation chain** = exact governed relations and C.2.1 source epistemes on which `v : X -> Y` depends; pointers, graph edges, publication availability, and provenance prose do not make those relations obtain.
- **Decode-mediated case** = a case where interpreting exact receiving episteme `Y` depends on a declared decoding or access relation. A published source form, latent state, decoded output, or carrier may provide access but cannot substitute for exact source episteme `X`, exact `Y`, or the relation.
- **actionabilityShift** = a changed user action-possibility interpretation or apparent readiness created by the rendering. It is not execution authority, gate status, action invitation, work authority, or proof that work may proceed.
- **recoverabilityEvidenceClass** = a local review field naming the recoverability evidence needed for decode-mediated or latent cases. It is not an `EvidenceKind`; it remains absent for an ordinary non-latent representation shift unless recoverability is part of the question under repair.
- **representationAdmissibilityValue** = a local admissibility value used only when the representation shift is disputed, assurance-facing, gate-adjacent, externally relied on, decode-mediated, or likely to invite gate, evidence, work, or authority use beyond declared admissible use. It says which use the shifted representation makes admissible now; it is not a score, ordered rank, improvement scale, ontology class, evidence class, or `authoritySourceRef` destination.
- **sourceRelationClass** = the shared `E.17:5.1b` vocabulary used beside representation-admissibility value when the source relation itself is disputed or claim-bearing: pointer-only, available, retrieved, used, faithful, claim-admissible, claim-non-admissible, claim-contradicted, claim-plausible-only, source-omitted, source-loss-declared, claim-widened, added-linkage, independent-verification-present, admissible-for-this-use, downstream-use-forbidden, or reopen-trigger-present.

| representationAdmissibilityValue | Admissible use | Relation-set completeness condition | Shortcut rejected |
| --- | --- | --- | --- |
| `readability-only` | Inspection, discussion, source-finding, or planning preparation. | Source-relation chain and non-admissible downstream-use line. | Clearer rendering means a wider claim. |
| `source-recoverable` | Receiving-side relations can be traced back to source-relation records. | Source-relation records, loss and provenance note, and recoverability statement. | Receiving form replaces source relation. |
| `structure-preserving` | Technical review of preserved relation structure. | Declared relation structure, preservation witness, and no-new-claim check. | Diagram form or topology defines ontology by form. |
| `decode-bounded` | Bounded decode-mediated report or review. | Decode relation, `recoverabilityEvidenceClass`, and recoverability scope. | Readable decode output is direct givenness. |
| `probe-bounded` or `intervention-bounded` | Bounded representation-to-property or representation-to-behavior claim. | Probe evidence, intervention evidence, or causal-abstraction relation that names the declared admissible use. | Probe confidence or intervention success becomes general ontology. |
| `bridge-bounded-source-equivalence` | Equivalence, substitution, or bridge use only where another governing pattern supplies it. | Existing bridge, equivalence, or substitution record outside RT, with the governing pattern named. | RT itself grants source equivalence or substitution. |

**Recoverability-for-use rule.** If the declared admissible use is inspection, source-finding, comparison, or technical review, `RepresentationSchemeTransition` can close with entityOfConcernRef-preserving preservation, source-relation chain, representation-scheme delta, and loss or recoverability notes. If the declared admissible use is work-planning preparation, this pattern is admissible only for reversible preparation until `A.15` supplies the role, method, plan, and work source relation. Evidence or currentness, gate or release, assurance, commitment, bridge or substitution, and engineering-justification uses are admitted only when the case names the downstream governing source relation; otherwise the receiving representation remains orientation or review use only.

These terms are local review aids. They inherit the `E.17:5.1e` local-field rule: they do not create `U.Kind`, `publication-face kind`, `RelationKind`, `KindBridge`, `MechanismKind`, `EvidenceKind`, project-side FPF kind and reference named by value, new face family, or new ontology governing pattern.

#### A.6.3.RT:4.2 - Scope and exclusions

**In scope**
- text-to-table shift over the same EntityOfConcern;
- table-to-diagram shift over the same EntityOfConcern;
- diagram-to-structured-notation shift where the represented entity and claim-bearing source episteme stay preserved;
- functional-description diagrams, tables, screens, or notations when the same EntityOfConcern remains fixed and the main change is representation scheme or reasoning medium;
- other same-entity representation-scheme changes with explicit recoverability discipline.

**Out of scope**
- any change of `entityOfConcernRef` or hidden change of EntityOfConcern (`A.6.4`);
- explanation-facing renderings whose main purpose is didactic or explanatory rendering work (`ExplanationFaithfulnessProfile`);
- purely textual rewrites that stay inside one representation regime (`ConservativeRetextualization`);
- carrier work such as rendering, export, upload, serialization, OCR-style extraction, or parsing-style extraction;
- latent- or distributed-representation use without exact source episteme `X`, exact receiving episteme `Y`, construction `v`, decoding/access relation, recoverability evidence, admissible use, and remaining user action; a source publication occurrence is only an access neighbor;

#### A.6.3.RT:4.2.a - User guidance

Use this pattern when exact `X` and exact `Y` keep the same EntityOfConcern while their effective representation schemes or reasoning media differ. A published form may expose `Y`; publication is not the construction.
- If only wording changes, stay in `ConservativeRetextualization`.
- If the receiving rendering mainly teaches, narrates, or explains, apply ExplanationFaithfulnessProfile.
- If same-EntityOfConcern continuity fails, apply A.6.4.
- Stay here when changed representation scheme or reasoning medium remains the primary review question, even if some loss is present.
- If the receiving representation stays honest only by carrying its own narrower-use card, declared source-loss mode, non-admissible downstream-use line, and a condition for return to the exact source representation or source relations, apply A.6.3.CSC Controlled Semantic Coarsening; do not keep the case here as ordinary representation-scheme transition.

#### A.6.3.RT:4.2.b - What the user checks first

A user usually starts with five questions:
1. Is the EntityOfConcern still the same, or has the EntityOfConcern shifted?
2. What changed in representation scheme and reasoning medium?
3. Can exact receiving episteme `Y` still cite the governed source relations needed by `v` and return to exact source episteme `X`; if access is through publication, are the occurrence, form, and carrier separately identified?
4. Has the case quietly become explanation, bridge-bearing comparison, retargeting, or carrier work?
5. If decoding is involved, is the evidence class adequate for the declared admissible use rather than only for readable review?

If the representation shift is no longer the main review problem, and the receiving rendering instead stays honest only by carrying a narrower-use card with non-admissible downstream use and reopen duty, the case has crossed out of ordinary representation-scheme transition even if the new form still looks like a neat table, diagram, or notation. Use `A.6.3.CSC Controlled Semantic Coarsening` for that source-to-rendering relation.

Here, **return to source** means returning to exact source episteme `X` or to the exact governed source relations on which `v` depends. A changed explanation, retargeting, bridge, work, evidence, gate, assurance, temporal, dynamics, carrier, or transformation-flow claim opens its named direct governor; controlled coarsening may require both source return and another governor.

Only after these questions are answered clearly does a fuller claim-bearing continuity-review field set normally become necessary.

#### A.6.3.RT:4.3 - Ordinary construction statement; occurrence description only after occurrence obtains

Most representation-scheme changes do not need a giant record. They do always need exact epistemic endpoints. For an ordinary non-latent case, state:

- exact source episteme `X` and receiving episteme `Y`, with each C.2.1 identity triple recoverable;
- exact A.6.3 construction `v : X -> Y`, including how source claims construct receiving claims and how the two effective reference schemes relate;
- same exact EntityOfConcern, preserved content, admitted omission or loss, and prohibited strengthening;
- the representation-scheme or reasoning-medium delta;
- admissible use, non-admissible downstream use, and return to exact `X` or its governed source relations.

That ordinary statement is admissible for inspection, source-finding, comparison, technical review, or reversible planning preparation. When dispute, reliance, correspondence, decode-mediated access, assurance, a gate-adjacent use, or justification requires more detail but the six-participant `...@Context` occurrence does not obtain, expand this same `v` statement with the exact source-relation or correspondence dependencies, scheme and reasoning-medium delta, loss or recoverability detail, admissible and non-admissible use, and return. Stronger reliance does not by itself require separately constituted scheme-description epistemes, an exact selected bounded model-use structure, the representation-transformation Work used by the §4.1.a.1 obtaining test, a transition-occurrence reference, or an occurrence-description episteme. Recover any independently current Work, publication, viewpoint, grounding, evidence, assurance, or receiving-use fact under its direct owner without converting the ordinary construction into the stronger occurrence.

**Occurrence-description content.** Only after an exact `RepresentationSchemeTransitionRelation@Context` occurrence obtains under §4.1.a.1 may a durable C.2.1 transition-description episteme describe it. That episteme has the exact six-participant occurrence as its EntityOfConcern, claim content that designates the occurrence and states the relied-on construction, Work, preservation, loss, use, and return, and its own effective `U.ReferenceScheme`. Dispute, reliance, correspondence, decode, assurance, gate adjacency, or justification may make this description useful, but none makes the occurrence obtain. Its claim content may make the following values recoverable; they are content about the already obtaining occurrence, not additional episteme identity fields or relation participants:

| Content needed for this occurrence-description use | Interpretation |
| --- | --- |
| `transitionRelationRef` | Required exact six-participant occurrence; its signature resolves the selected `BoundedModelUseStructure`, preserved EntityOfConcern, `X`, `Y`, and the exact source- and receiving-scheme-description epistemes. |
| `viewingConstructionRefOrStatement` | Exact `v : X -> Y` with claim construction, endpoint effective-scheme relation, applicability, preservation, loss, and prohibited strengthening. |
| `representationTransformationWorkRef` | Exact A.15.1 Work already used in the occurrence obtaining test; its performer, role assignment, method, bindings, and any inception claim remain separate. |
| `sourceRelationReferenceEpistemeRefs[]` | C.2.1 epistemes about exact governed source relations actually used; each relation still needs its own obtaining basis. |
| `preservedClaimRefs[]` | Exact source claims carried into `Y` for the declared use. |
| `preservedCommitmentRefs[]?` | Exact commitments preserved when a commitment is current; otherwise absent. |
| `representationSchemeDeltaDescriptionRef` | What differs between the exact source and receiving scheme-description epistemes already participating in the occurrence. |
| `reasoningMediumDeltaDescriptionRef?` | Changed inspection, comparison, inference, or replay affordance when material. |
| `representationLossDescriptionRef?` | Lost, narrowed, foregrounded, or rearranged distinctions. |
| `recoverabilityDescriptionRef?` | How omitted content is recovered from exact `X` or exact source relations for the declared use. |
| `admissibleUseDescriptionRef` | What the receiving episteme supports now. |
| `nonAdmissibleDownstreamUseDescriptionRef` | Which stronger use has not been established. |
| `returnConditionDescriptionRef` | When the user returns to exact `X`, its source relations, or another direct governor. |

At least one of loss and recoverability is explicit; both are explicit when distinctions are lost and a recovery route is claimed. A publication may expose the occurrence description, but publication does not constitute `X`, `Y`, `v`, the transition occurrence, the Work, or the description episteme.

#### A.6.3.RT:4.3.a - Working admissibility defaults

By default in this pattern:
- primary admissible faces for non-latent cases are `PlainView` and `TechCard`;
- bounded report-only use is admissible when source pins, provenance, loss notes, and entityOfConcernRef-preserving continuity remain visible, and when the receiving rendering is not relying on one separate narrower-use card to remain honest;
- `InteropCard` use is admissible only when the governing publication-face source explicitly permits source-pinned, structure-preserving export without added semantics;
- `AssuranceLane` or gate-bearing use is admitted only under a governing publication-face policy and source-pinned same-EntityOfConcern continuity;
- latent-representation variants and distributed-representation variants remain bounded until explicit recoverability evidence and decoding-relation discipline are published.

#### A.6.3.RT:4.4 - Direct and correspondence-mediated constructions

**Direct representation-scheme construction.** Exact receiving episteme `Y` is constructed from exact source episteme `X` and fixed declared configuration. The construction names the exact claim-content rule, the source and receiving effective reference schemes, preserved content, loss, and applicability. No generic correspondence object is required.

**Correspondence-mediated representation-scheme construction.** `Y` depends on additional exact source epistemes or exact governed relations among their claim-bearing contents. Recover each needed direct relation and, when the construction cites a claim about it, the exact C.2.1 assertion episteme. The viewing declaration names those exact dependencies. A correspondence table, model, graph edge, scheme difference, or similar content is neither the relation nor proof that it obtains.

Both profiles retain the same exact EntityOfConcern for `X` and `Y`. Correspondence does not repair retargeting and does not grant bridge, substitution, comparative-review, evidence, or publication licence. A C.29 mathematical representation is added only when a current mathematical modeling or reasoning use needs it; its output stays local and does not become the transition occurrence.

#### A.6.3.RT:4.4.a - Recurring same-entity representation moves

Recurring same-entity moves under this pattern include:
- **Tabulation** — prose or dispersed claims are rendered into a table that exposes comparison or coverage more clearly.
- **Diagramming** — a table or prose relation set is rendered into a diagram that foregrounds structure while keeping the source-relation chain visible.
- **Structured notation shift** — prose, table, or diagram content is rendered into a notation better suited for disciplined replay or technical inspection.
- **Correspondence-admissible representation shift** — the receiving representation depends on declared same-EntityOfConcern correspondence witness without thereby becoming a bridge case.

These are recurring move shapes under one specialization relation. They are not separate governing patterns and they do not override `E.17` face discipline.

#### A.6.3.RT:4.4.b - How the user states representation-factor and reasoning-medium change
A user can state, in one short paragraph, what changed in representational shape, what changed in reasoning medium, and whether the primary change is also a `semioticModeShift` rather than only a scheme change. Typical statements are: "the table foregrounds comparability across rows", "the diagram foregrounds dependency shape", or "the notation foregrounds explicit argument positions."

When the case is more demanding, that paragraph also names whether salience, topology, actionability, admissible-use interpretation, calibration, or interactivity materially changed. If those shifts cannot be stated without slipping into new ontology, hidden bridge work, or a changed EntityOfConcern, the case is not yet ready to stay here. Use the representation-delta review crib sheet and the current semiotic-mode note when the deltas need a more normalized statement.

#### A.6.3.RT:4.5 - Shared representation rule bundle

##### A.6.3.RT:4.5.a. Preservation rule
`RepresentationSchemeTransition` preserves the same exact EntityOfConcern across independently constituted `X` and `Y` while changing the declared representation scheme and, often, reasoning medium. An exact `BoundedModelUseStructure` participates only in the stronger `...@Context` occurrence; it is not an episteme identity discriminator. The transition account is complete only when it identifies `X`, `Y`, their effective schemes, exact construction, preserved and lost content, admissible use, and return; publication scope, pins, provenance, grounding, and selected model-use structure enter only through their independently governed relations when current.

##### A.6.3.RT:4.5.a.1. Local conservativity witness
For this pattern, a new EntityOfConcern-side claim is introduced when the receiving rendering:
- upgrades a source-visible relation into relation theory or dependency semantics not present in the source;
- turns geometry, notation, embedding proximity, or decoder output into ontology-by-default;
- adds bridge, substitution, comparative-review, or mechanism claims not already licensed by the source line or declared correspondence;
- collapses source alternatives, uncertainty, or bounded scope into one wider commitment;
- or treats decode-mediated recoverability as if it were direct givenness.

Conservativity is approximated here by checking, together, `entityOfConcernPolicy = preserve`, source-relation class, factor delta, reasoning-medium delta, loss profile, ontic scaffold preservation, and whether each receiving-side connective can be pointed back to pinned source `U.Episteme` claim graph or declared same-EntityOfConcern correspondence witness.

##### A.6.3.RT:4.5.b. Loss and reliability rule
A reviewed case under this pattern makes explicit which distinctions, inspection possibilities, or local cues are lost, foregrounded, or rearranged by the shift in representation regime. Reliability transport may remain source-bounded or be explicitly downgraded; a clearer, more structured, or more formal receiving form does not widen the reliability claim.

##### A.6.3.RT:4.5.c. Governing-pattern boundary rule
A case stays here when the **required field set** remains visible: exact `X`, exact `Y`, `v : X -> Y`, preserved EntityOfConcern, governed source-relation chain, scheme/medium delta, loss or recoverability, admissible use, non-admissible use, and return. This is Plain completeness guidance, not a new structure or identity record.

When the current claim is no longer that representation shift, state the claim being made and apply the governing pattern for that claim. Typical crossed claims are retargeting, bridge stance, explanation governance, carrier work, gate authority, evidence force, assurance force, work enactment, abductive selection, temporal currentness, dynamics currentness, and transformation-flow currentness. Until that governing source relation is supplied, the shifted representation remains limited to source-finding, inspection, comparison, technical review, reversible planning preparation, report-only use, or exploratory use.

##### A.6.3.RT:4.5.c.1. Decode-mediated entry condition
A decode-mediated case, latent-representation case, or distributed-representation case may stay here only when the receiving rendering carries this entry set:
- exact source episteme `X` for the same EntityOfConcern, with any publication occurrence, form, or carrier identified separately when used for access;
- source-relation chain back to the pinned source `U.Episteme` claim graph;
- decoding relation or access relation;
- recoverability evidence for the intended use;
- admissible-use value;
- remaining user action.

A source expression, latent region, distributed activation pattern, embedding, probe result, decoded rendering, publication form, or carrier may help locate the case but cannot fill `X` or `Y`. Recover both exact epistemes, the same EntityOfConcern, the construction, decoding or access relation, recoverability evidence, admissible use, and remaining user action separately. If this entry set is missing, keep the use report-only, exploratory, or blocked and return to exact `X` or its governed source relations; if another claim is being made, apply its direct governor.


##### A.6.3.RT:4.5.d. Composition and reopen rule
Repeated same-regime normalization may be idempotent, but heterogeneous regime shifts are generally order-sensitive. Multi-publication chains are checked pairwise, and the final use carries accumulated loss rather than restarting as if each pair erased earlier losses.

Each step in a chain keeps recoverable:
- exact source and receiving epistemes with their C.2.1 identity triples and preserved EntityOfConcern;
- claim or commitment under test;
- representation-scheme delta;
- preserved and withdrawn commitments;
- loss and recoverability;
- remaining admissible user action.

The case reopens whenever recoverability assumptions, pins, provenance, correspondence witness, publication-face admissibility, primary semiotic mode, or accumulated loss changes. A representation shift also reopens if what looked like one same-entity line turns out to concern a new EntityOfConcern, a counter-witness disposition, or a decoding relation whose current evidence basis no longer satisfies its declared use.

#### A.6.3.RT:4.6 - Boundary trigger table

Use this table after the required field set. It is not a second catalogue of everything RT cannot do; it names the local trigger that changes the next FPF move.

| Boundary trigger | Governing result |
| --- | --- |
| `entityOfConcernRef`, EntityOfConcern kind, ontology frame, admissible predicate set, or invariant-bearing receiving rendering changes | Apply `A.6.4` or the ontology-facing governing pattern. |
| The receiving rendering is only a textual rewrite | Apply `ConservativeRetextualization`. |
| The primary job is explanation-use adequacy for an existing source on an MVPK face | Apply `ExplanationFaithfulnessProfile` unless EntityOfConcern or ontology-frame change makes `A.6.4` primary. |
| Selected source structures are ordered into a sequential narrative for a declared reader or listener use | Apply `A.6.3.NAR`; keep RT only for the representation-scheme shift that remains after the narrative ordering, source loss, and source return are declared. |
| The work is rendering, export, upload, serialization, OCR-style extraction, parsing-style extraction, or other carrier work | Keep carrier work outside RT; start with the pattern governing carrier or extraction use, such as `A.7` when source extraction is the current question. |
| Geometry, notation, embedding space, feature clustering, decoded output, `PathSliceId`, `CrossingRef`, or `DecisionLogRef` is being used as ontology, continuity proof, gate, work, evidence, assurance, or transformation-flow currentness claim | Keep RT only for the representation shift and apply the governing pattern for the stronger claim. |
| Problem formulation, temporal claim, dynamics claim, control claim, or transformation-flow claim becomes primary | Apply `B.5.2`, `C.27`, `A.3.3`, `E.18`, or the governing pattern for that claim. |
| Exact receiving episteme `Y` remains useful but the construction, loss, or return account cannot honestly hold | Lower or block the use; apply controlled coarsening when a narrower-use `Y` exists, otherwise return to exact `X` or its governed source relations. A readable form or carrier alone is not `Y`. |

If recoverability depends on decoding, probing, or intervention, the evidence class bounds the admissible use. Low-evidence decode-mediated results remain bounded exploratory or report-only renderings; non-latent cases remain the default entry case until decode-mediated recoverability is made explicit.

### A.6.3.RT:5 - Archetypal grounding

#### A.6.3.RT:5.1 - Same-entity text-to-table construction

Exact source episteme `LatencyFinding-X` has claim content stating three evening-batch latency spikes with trace and dashboard support, exact EntityOfConcern `Service-S-during-W`, and effective reference scheme `ServiceTelemetryScheme-4`. Exact receiving episteme `LatencyTable-Y` has table-structured claim content about the same exact EntityOfConcern under effective reference scheme `TabularTelemetryScheme-2`; it preserves the spike-count claim and source designations and omits the prose ordering.

`TabulateLatency : LatencyFinding-X -> LatencyTable-Y` states that exact construction, the relation between the schemes, the omission, prohibited strengthening, and inspection-only use. The visible table form and its file carrier are not `Y`. Unless an exact bounded model-use structure and actual representation-transformation Work also satisfy section 4.1.a.1, this example asserts the A.6.3 construction but not `RepresentationSchemeTransitionRelation@Context`.

#### A.6.3.RT:5.2 - Positive six-participant table-to-diagram occurrence

Exact source episteme `CoolingLoopRelationTable-X` states two already governed connection claims about exact EntityOfConcern `CoolingLoop-7` under effective reference scheme `TabularPlantScheme-5`. Exact receiving episteme `CoolingLoopDependencyDiagram-Y` states the same two claims in diagrammatic claim content about `CoolingLoop-7` under effective reference scheme `DirectedDiagramPlantScheme-3`; it is a candidate episteme, not automatically a `U.View`.

Exact scheme-description epistemes `TabularPlantSchemeDescription-5` and `DirectedDiagramPlantSchemeDescription-3` concern their respective schemes and state their interpretation rules. Independently selected `CoolingLoopReviewModelUseStructure` satisfies A.1.1 because its exact model-use organization changes this review use. System `PlantModelingTool-2`, under exact role assignment, performs dated Work `CoolingLoopDiagrammingWork-18`; its governed bindings use the selected structure, `CoolingLoop-7`, `X`, `Y`, and both scheme descriptions. Exact construction `DiagramCoolingLoop : X -> Y` states the source-to-receiving claim rule, scheme relation, preserved connection claims, omitted table-cell qualifiers, prohibited strengthening, and applicability.

Only with all those facts does this occurrence obtain:

```text
RepresentationSchemeTransitionRelation@Context(
  CoolingLoopReviewModelUseStructure,
  CoolingLoop-7,
  CoolingLoopRelationTable-X,
  CoolingLoopDependencyDiagram-Y,
  TabularPlantSchemeDescription-5,
  DirectedDiagramPlantSchemeDescription-3)
```

The transition-description episteme has this exact occurrence as EntityOfConcern. Its claim content cites `CoolingLoopDiagrammingWork-18`, `DiagramCoolingLoop`, the exact source connection relations, the omitted qualifier, topology-inspection use, the blocked control-timing/work-order inference, and return to `X` when qualifiers matter. It also states the example-level representation and reasoning-medium deltas—rows become directed diagram edges and pairwise lookup becomes topology inspection—and the recoverability mechanism that each edge links to its exact source-table relation in `X`. A later publication occurrence, diagram form, or SVG carrier remains separate. `Y` is a `U.View` only if an exact E.17.0 conformance occurrence independently obtains.

#### A.6.3.RT:5.2.a - Correspondence-mediated text-to-table shift
**Source prose slice.** `In the safety view, CL-2 maintains the required temperature condition during standard operating demand.`

**Published table slice.** `| View | Entity | Condition | Correspondence model |
| Safety | CL-2 | required temperature condition during standard operating demand | CM-12 |`

This case stays only if exact text-source episteme `X`, exact table episteme `Y`, and `v : X -> Y` are identified, their EntityOfConcern is the same, and every relied-on correspondence is an exact governed occurrence. The source prose form and table form are not endpoints; the correspondence record or visible row is not the relation.

#### A.6.3.RT:5.2.b - Same-entity diagram-to-structured-notation shift
**Source diagram slice.** `CoolingLoop -> Sensor A; CoolingLoop -> Valve B`

**Published notation slice.** `dependsOn(CoolingLoop, SensorA)`
`dependsOn(CoolingLoop, ValveB)`

This remains under `RepresentationSchemeTransition` when the notation states the same relation line already visible in the diagram, the EntityOfConcern remains preserved, and no additional dependency theory is silently imported by the notational rendering.

#### A.6.3.RT:5.2.c - Functional-description diagram, table, or screen shift

**Source slice.** `The mixing cell transfers liquid from Tank A through heat exchanger H-2 to reactor R-4; the source description is about the same declared functional slice and keeps instrumentation claims and control claims outside this relation.`

**Published table or screen slice.** `| Function relation | Source | Target | Limit |`
`| transfer and heat before reaction | Tank A | R-4 via H-2 | no control-loop claim |`

This remains `RepresentationSchemeTransition` only when the same EntityOfConcern is preserved and the table or screen changes representation scheme or reasoning medium without adding performed-work order, module structure, evidence, gate passage, or control architecture. If the diagram, table, or screen turns the receiving representation into a functional, control, or flow architecture claim rather than re-rendering the already declared functional slice, apply `A.6.4`, `OntologicalReframing`, or `E.18` as applicable. If the diagram order is explanatory, causal, dependency-like, or didactic, do not treat it as physical time order or performed-work sequence unless that temporal claim is present in the source episteme and separately admissible. If a parser step or OCR step only extracts pixels, text, or carrier layout from a scanned diagram or screen, start with `A.7`; apply this pattern only when the extracted structure is being treated as an entityOfConcernRef-preserving representation of source `U.Episteme` claims with source-relation chain and loss notes visible.

If exact receiving episteme `Y`, exposed through the screen, remains honest only by omitting exceptions, confidence bands, or source distinctions and carrying a narrower use plus return to exact `X`, apply CSC. The screen form or carrier alone is neither `Y` nor a controlled-coarsening construction.

#### A.6.3.RT:5.3 - Boundary to textual rewrite
A source prose note is shortened, reordered, or translated but remains essentially textual. That case stays with `ConservativeRetextualization`, not this pattern.

#### A.6.3.RT:5.4 - Boundary to explanation-facing renderings
A representation shift is performed mainly to teach or narrate rather than to publish another same-entity representation regime. That case leaves this pattern and is reviewed under explanation governance.

#### A.6.3.RT:5.4.a - Boundary to bridge-bearing comparison
**Source slice.** `Local reliability note: Pump P-2 remained within operating range during test window W-3.`

**Published comparative slice.** `Pump P-2 in W-3 behaves like Unit U-7 in Plant B and can therefore be treated as operationally equivalent for this comparison.`

This does **not** stay in RepresentationSchemeTransition. The rendering has changed from an entityOfConcernRef-preserving representation shift to comparative or bridge-bearing interpretation across contexts. Once the publication starts asserting cross-context equivalence, substitution, or comparative licence, the case is governed by explicit bridge-governed review.

#### A.6.3.RT:5.4.b - Boundary to carrier work and export work
**Source rendering slice.** `| Service | Window | Spike count | Source pins |`

**Published export slice.** `latency-report.csv` and dashboard PNG generated from the same table.

This also stays outside `RepresentationSchemeTransition`. The representation scheme was already chosen; what follows is carrier formatting, export, packaging, or rendering work on that representation. The didactic point is that not every change in visible form is a new entityOfConcernRef-preserving representation transition.

#### A.6.3.RT:5.4.c - Boundary to coarsened dashboard view
**Source slice.** `The incident worksheet tracks three causal branches, two confidence bands, and one still-open ambiguity note for Service S.`

**Published dashboard tile.** `Service S: current dashboard view foregrounds cache-failover evidence; alternative branches and confidence bands remain in the incident worksheet.`

This does **not** remain ordinary RepresentationSchemeTransition if the tile is treated as more than a narrow report view. The tile foregrounds one causal branch and suppresses uncertainty and alternative branches, so it stays honest only with an explicit return to the exact incident worksheet and its source relations, plus a non-admissible downstream-use line. It is not a causal proof, service status verdict, or action cue. Once that narrower-use card becomes primary, ordinary entityOfConcernRef-preserving representation-scheme transition no longer governs; apply A.6.3.CSC Controlled Semantic Coarsening rather than treating it as a normal scheme shift.

#### A.6.3.RT:5.4.d - Boundary to structure-to-narrative rendering

**Source structure slice.** `Architecture candidate C-2 has module split M, data-custody constraint D, placement constraint P, and unresolved latency versus maintainability trade-off T.`

**Published narrative slice.** `The team first tried to preserve module split M, then discovered that data custody D forced placement P, so candidate C-2 accepts latency residual T to keep maintainability within the selected range.`

This does not stay ordinary `RepresentationSchemeTransition` merely because prose is one representation of architecture. The receiving rendering orders selected source structures into a narrative path for a reader. Apply `A.6.3.NAR` for ordering rationale, preserved and lost structure, admissible use, and source return. Use RT only for any remaining representation-scheme shift that does not depend on narrative ordering.

#### A.6.3.RT:5.5 - Boundary to decode-mediated latent cases
A decode-mediated case stays outside RT until exact `X`, exact `Y`, `v`, the decoding/access relation, recoverability evidence, admissible use, and remaining user action are present. A latent region, feature cluster, probe result, source publication occurrence, or readable decoded output cannot fill an episteme endpoint.

#### A.6.3.RT:5.5.a - Guarded decode-mediated rendering
**Pinned source cluster.** `Probe run P-8 is tied to model-state log M-12 and evaluation bundle EV-4 for the same diagnostic case.`

**Published exploratory slice.** `A decoded rendering suggests a cluster that may correspond to the same failure episode already pinned in P-8, M-12, and EV-4. This rendering stays exploratory and report-only until recoverability evidence sufficient for that use is published.`

This example remains guarded-open rather than green. The didactic point is that a decode-mediated rendering may still be useful, but it does not become a normal same-entity publication merely because the result looks readable.

### A.6.3.RT:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto**, **Epist**, **Prag**, **Did**.
This pattern intentionally biases toward same-entity representation shifts and away from hidden retargeting, explanation inflation, or ontology-by-default through notation or geometry. The main mitigation is explicit recoverability discipline, preserve-vs-retarget escape rules, and directly reviewable entry cases before decode-mediated ones.

### A.6.3.RT:7 - Conformance and counterexample replay

A check is retained only if it changes the next admissible use, blocks a concrete overclaim, or preserves an exact source or return relation.

#### A.6.3.RT:7.1 - RT-Core

1. **CC-RT-1 — Exact endpoints.** `X` and `Y` are independently constituted C.2.1 epistemes; each exact claim content, EntityOfConcern, and effective `U.ReferenceScheme` is recoverable. A model label, graph, display, publication occurrence, form, carrier, or readable output substitutes for neither.
2. **CC-RT-2 — Same EntityOfConcern, no hidden retargeting.** `EntityOfConcern(X)=EntityOfConcern(Y)` exactly. Otherwise apply A.6.4.
3. **CC-RT-3 — Exact construction.** The declaration states `v : X -> Y`, the claim-content rule, relation between effective schemes, preservation, loss, prohibited strengthening, and applicability.
4. **CC-RT-4 — Six-participant occurrence only at its trigger.** A positive `RepresentationSchemeTransitionRelation@Context` has the exact A.1.1 `BoundedModelUseStructure`, preserved EntityOfConcern, `X`, `Y`, and exact two scheme-description epistemes, plus actual representation-transformation Work satisfying section 4.1.a.1. No discarded generic context kind/reference, description-context field, scheme label, or Work record fills a participant.
5. **CC-RT-5 — Occurrence, Work, and description stay distinct.** The participant tuple identifies the relation occurrence; system, role assignment, Work, method, operation bindings, and production claim stay with their direct owners; the transition-description episteme has its own C.2.1 identity.
6. **CC-RT-6 — Exact correspondence dependencies.** Every correspondence-mediated dependency resolves to exact source epistemes and governed relations. Similar content, graph adjacency, a correspondence model, or scheme difference proves none.
7. **CC-RT-7 — Use and return.** Preserved content, explicit loss or recoverability, admissible use, non-admissible downstream use, and return to exact `X` or governed source relations are visible.
8. **CC-RT-8 — Neighbors remain separate.** C.29 representation is opened only for a current mathematical lens; viewpoint and `U.View` membership require E.17.0; grounding, publication occurrence, form, carrier, evidence, assurance, bridge, gate, and receiving use keep their direct owners.

#### A.6.3.RT:7.2 - Counterexample replay

| Case | Required result |
| --- | --- |
| Preserve vs retarget | Equal exact EntityOfConcern permits the A.6.3 test; a changed EntityOfConcern exits to A.6.4 even when labels or content overlap. |
| Same scheme | If effective scheme and reasoning medium are unchanged and only wording changes, use A.6.3.CR; do not invent RT. |
| Different scheme | Scheme difference is explicit but does not itself establish `v`, correspondence, Work, Bridge, or the six-participant occurrence. |
| Candidate vs `U.View` | A valid receiving episteme and RT construction may still fail E.17.0 conformance and remain a non-View candidate. |
| Publication/form/carrier | Making `X` or `Y` available, changing its form, or replacing its carrier does not replace an endpoint or reidentify an unchanged construction or occurrence. |
| Work without conservativity | A system may actually produce `Y`, yet unsupported strengthening or unreported loss blocks the RT construction and relation occurrence. |
| Grounded source, ungrounded receiver | Grounding of `X` does not transfer through `v`; `Y` has an `EpistemeEmpiricalGroundingRelation` only when its own exact covered claims and grounding conditions make one obtain. |
| Selected structure overread | The exact `BoundedModelUseStructure` is one participant only in the triggered `...@Context` occurrence; it is not the transformer, viewpoint, `U.View`, representation, publication, or EntityOfConcern. |
| Cross-scheme dependency without transition or Bridge | If neither the exact six-participant transition occurrence required by that dependency use nor an exact applicable F.9 Bridge and bounded-use/reliance path exists, block the cross-scheme dependency. Scheme difference, similar content, a description, or C.29 output cannot fill the gap. |
| Description or C.29 output | Editing the transition-description episteme or mathematical output does not change the occurrence unless one of the exact six participants changes. |

Reopen only the affected item. After a bounded repair, replay its local counterexample and then run this complete table once for the final package; do not restart the full file after every local correction.

### A.6.3.RT:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it is wrong | How to avoid it |
|---|---|---|
| Treating every format shift as harmless formatting | representation changes can alter reasoning possibilities and recoverability | publish factor delta and reasoning-medium delta explicitly |
| Collapsing representation-scheme shift, semiotic-mode shift, and viewpoint shift into one vague change | users cannot tell what actually changed or which admissibility relation is primary | name scheme, mode, and viewpoint separately and use the canonical boundary exemplars when only one of them changed |
| Letting notation become ontology-by-default | diagram or geometry starts pretending to define the world rather than represent it | keep ontic scaffold preservation and recoverability explicit |
| Treating the transition description as the transition relation | Description claims, publication editions, C.29 outputs, or carrier changes appear to change relation identity. | Keep the six-participant signature and identity on the occurrence; identify the transition-description episteme separately by its C.2.1 triple. |
| Hiding retargeting under representation language | a changed EntityOfConcern is mislabeled as same-entity representation work | apply `A.6.4` whenever `EntityOfConcernRef` changes |
| Starting with latent-representation or distributed-representation cases before recoverability is explicit | decode demand overwhelms same-entity review | keep decode-mediated cases out until decoding access and evidence class are explicit |

### A.6.3.RT:9 - Consequences

- Same-EntityOfConcern episteme constructions get an admissible place without treating a visible rendering, publication, form, carrier, Work record, or description as an endpoint or occurrence.
- Representation-factor and reasoning-medium changes become explicit rather than rhetorical.
- Recoverability and decode dependence become reviewable instead of hidden behind cleaner renderings.
- The pattern remains safely bounded by `A.6.3`, `A.6.4`, explanation governance, and carrier work.

### A.6.3.RT:10 - Rationale

This pattern is worth splitting out because representation changes are already happening in practice and they are not well served by treating every such case as either mere rewriting or full retargeting. Keeping the family under `A.6.3` preserves governing-pattern boundary while making representation-factor and recoverability evidence needs explicit.

### A.6.3.RT:11 - SoTA-Echoing

| Source and currentness role | Adopted transition move | Rejected overread | Practical implication |
| --- | --- | --- | --- |
| OMG, `SysML Version 2.0`, formal specification adopted September 2025, as a current industrial modeling-language and view-practice anchor. The 2026 OMG issue tracker still records unresolved table and matrix view-mechanism gaps, so the standard is not treated as complete general representation-transition theory. | Name source and receiving representation schemes, preserved subject, and actual source relations rather than treating a tool view as decorative layout. | SysML v2 conformance proves same-EntityOfConcern continuity, losslessness, or downstream authority. | A model view can enter RT: the transition relation states the exact source-to-receiving relation, while its transition-description episteme carries source-relation references, loss or recoverability, and admitted use. |
| Reyes et al., `Shades of Uncertainty: How AI Uncertainty Visualizations Affect Trust in Alzheimer's Predictions`, `arXiv:2602.01264`, as current empirical evidence that representation choices alter confidence, perceived reliability, recognition of limitations, and expert versus non-expert reliance. | Record reasoning-medium delta, representation loss, recoverability, and admitted use when a visual encoding changes what users notice or trust. | A more continuous, vivid, or confident display is automatically more truthful or suitable for stronger action. | Preserve omitted uncertainty and restrict the receiving visualization to the use supported by its evidence and audience. |
| Hoang and Hasan, `The Abstraction Gap in Vision-Language Causal Reasoning`, `arXiv:2605.28779`, as a current demonstration that fluent causal text can diverge sharply from explicit causal-chain performance. | Treat readable decoded or generated representation as a receiving episteme whose source relations and recoverability must still be checked. | Linguistic fluency or diagram readability is continuity proof, causal fidelity, evidence, or ontology. | A decoded explanation stays report-only or exploratory until the relation chain and evidence support the stronger use. |
| Geiger et al., `Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability`, JMLR 26 (2025), originating as `arXiv:2301.04709`, together with the 2025 limitation pressure in `The Non-Linear Representation Dilemma: Is Causal Abstraction Enough for Mechanistic Interpretability?`, `arXiv:2507.08802`. | Use correspondence and intervention evidence as possible continuity support for latent or distributed representations, and keep counter-witnesses and graded faithfulness visible. | A fitted alignment map, probe score, geometry, or feature cluster alone establishes the represented ontology or faithful causal abstraction. | Decode-mediated RT use names the access or decoding relation, evidence class, recoverability limit, and return condition; stronger causal claims exit to their direct governor. |

These sources discipline RT in different domains, but none makes its source vocabulary a new FPF kind. The shared safeguard is operational: representation scheme and reasoning medium are reviewable, while clarity, notation, geometry, probe output, or decoded prose do not acquire ontology, evidence force, gate admissibility, work authority, or engineering justification without the relations that support that exact use.

### A.6.3.RT:12 - Relations

- **Builds on:** `C.2.1` for exact endpoint and description-episteme identity; `A.6.3` and `A.6.2` for effect-free source-to-receiving construction; `A.1.1` for the exact `BoundedModelUseStructure` used only by the later-specific `...@Context` occurrence; `A.15.1` for actual representation-transformation Work; and `A.7`, `E.10.D2`, `C.2.7`, `E.17.0`, `E.17`, `F.9`, and `F.18` at their own triggers.
- **Coordinates with:** `ConservativeRetextualization`, `A.6.3.NAR Structure-to-Narrative Rendering`, `A.6.3.CSC Controlled Semantic Coarsening`, `ExplanationFaithfulnessProfile`, `E.17.ID.CR ComparativeReviewUnit`, `A.6.4`, `F.9`, `F.9.1`, `E.18`, `A.15`, `A.10`, `B.3`, `B.5.2`, `A.20`, `A.21`, `C.27`, `A.3.3`, explicit decoding-access review
- **Boundary notes:** textual same-regime rewrites stay with `ConservativeRetextualization`; source-structure-to-sequence constructions apply `A.6.3.NAR`; narrower-use coarsened constructions apply `A.6.3.CSC`; EntityOfConcern changes apply `A.6.4`; E.17.0 alone establishes `U.View`; E.24.PUB alone governs a publication occurrence, form, carrier, audience, and bounded use; C.29 enters only for a current mathematical representation; bridge, work, grounding, evidence, assurance, gate, temporal, dynamics, and transformation-flow consequences remain with their direct governors.

### A.6.3.RT:12a - Boundary with quantum-like state-representation shortcuts

Use RT first when the same EntityOfConcern is represented through a different representation scheme: text-to-table, model to diagram, diagram to structured record, state vector to typed description, or one notation to another. Ordinary representation-scheme change remains RT even when the new scheme is more compact.

Representation-shortcut review steps:

1. Confirm that the EntityOfConcern stays the same. If it changes, RT no longer governs; apply A.6.4.
2. Name the source representation scheme and receiving representation scheme.
3. State what changed in representation factor, reasoning medium, mode, salience, topology, actionability, calibration, or interactivity.
4. State recoverability: what can be recovered from the receiving representation, by which decoding relation, and with which evidence.
5. If the receiving representation claims to preserve action, intervention, manipulation, explanation, or cross-abstraction structure, state the causal-abstraction or approximate-causal-abstraction mapping before treating the shortcut as QL coarsening.
6. Ask whether the shortcut depends on a QL cue: contextual probability, incompatible probes, instrument-like update, Hilbert-like or orthomodular representation, open-information-system update rule, probe frame, export-admissibility evidence condition, or declared lossy export of a state that matters to the decision.
7. If no, keep the case under RT, CSC, ordinary abstraction, compression, diagramming, causal abstraction, approximation, or a declared representation-learning access pattern, whichever governs the actual admissibility claim.
8. If yes, coordinate with the `C.26` state-representation coarsening admissibility section and state admissible use, non-admissible use, and return condition.

For ordinary use, start with the standard shortcut mini-form:

| Mini-entry | Question |
| --- | --- |
| Source-loss question | Which representation scheme, state interpretation, fuller model, or evidence set loses distinctions in the shortcut? |
| Shortcut | Which cheaper, typed, quantized, symbolic, lower-detail, or otherwise changed representation is used? |
| Loss | Which precision, expressivity, compatibility, recoverability, or evidence relation is not carried? |
| Admissible use | Which decision, explanation, triage, comparison, or action-selection move remains admissible for the shortcut? |
| Reopen | Which dispute, decision change, demand for use with a stronger evidence basis, evidence gap, or recoverability failure opens source-representation return or a fuller model? |

Use a fuller C.26 coarsening record only when the shortcut becomes reusable, formal, empirical, high-stakes, or tied to comparative performance or tractability claims. In that fuller record, add the mechanism, baseline relation, non-admissible use, and QL cue needed for the additional-admissibility claim.

Do not describe ordinary compression, low-bit implementation, diagramming, or representation learning as quantum-like unless the formal cue is claim-bearing.

### A.6.3.RT:12b - C.29 mathematical-lens use relation

> When an entityOfConcernRef-preserving representation-scheme transition imports a contested or claim-bearing mathematical lens, `A.6.3.RT` still governs the source and receiving representation schemes, entityOfConcernRef-preserving relation, preserved and lost scheme features, and representation-scheme-transition boundary. The applicable `C.29` output for the stated use (`MathLensUse.LensCandidateNote`, `MathLensUse.OneLine`, `MathLensUse.MiniCard`, or `MathLensUse.FullCard` when the declared use needs it) may be cited only for adequacy of the mathematical lens used in that transition. It does not replace the representation-scheme-transition record or broaden the transition into bridge, evidence, or causal-claim-kind.

### A.6.3.RT:End

