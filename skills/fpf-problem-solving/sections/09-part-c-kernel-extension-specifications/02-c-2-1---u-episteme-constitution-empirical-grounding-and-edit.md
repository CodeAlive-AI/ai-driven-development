## C.2.1 - `U.Episteme`: Constitution, Empirical Grounding, and Edition Relations

> **Type:** Pattern
> **Status:** Stable
> **Normativity:** Normative except where a section is explicitly marked informative

**Plain name.** Episteme constitution.

**Mint or reuse.** This pattern reuses `U.Episteme`, `U.ClaimGraph`, `U.Entity`, `U.ReferenceScheme`, `U.Holon`, `U.Signature`, `RelationSignature`, and `SlotSpec`. It introduces the direct relation names `EpistemeConstitutionRelation`, `EpistemeEmpiricalGroundingRelation`, and `EpistemeEditionRelation`; it introduces no U-kind. Each named `...RelationSignature` below is the relation-facing use of one declaration episteme for which the `A.6.0` membership predicate obtains; `A.6.0` therefore recognizes that same individual as a `U.Signature`, not as another identity. The signature-local SlotKinds named below identify participant meanings only inside their stated signatures. An episteme itself has no slots, and repeated slot spelling in another signature establishes no shared SlotKind by spelling alone.

**One-line summary.** A `U.Episteme` is a knowledge holon identified by exact claim content, one exact EntityOfConcern, and the effective `U.ReferenceScheme` that makes those claims interpretable as claims about that entity. `EpistemeConstitutionRelation` is the core direct relation of the episteme ontic. Empirical grounding, viewpoint, view, scope, model use, edition succession, description, publication, carrier, and mathematical representation remain neighboring objects and relations.

**Use this pattern when.** Use C.2.1 when a theory, model, specification, standard, proof, algorithm description, diagnosis, lesson, diagram, dashboard, or other claim-bearing object needs to remain identifiable while its subject, interpretation, empirical grounding, view, edition, or publication changes.

**Primary working reader.** An engineer or researcher who needs to identify a knowledge object and use it without mistaking its subject, file, view, evidence, or publication for that knowledge object.

**Primary working concern.** Keep one claim-bearing object reidentifiable through empirical grounding, viewing, revision, and publication, and detect when changed claims, subject, or interpretation identify another episteme.

**Primary viewpoint.** The practitioner using, comparing, revising, or publishing that knowledge object while keeping its identity and neighboring relations distinct.

**Primary EntityOfConcern.** The `U.Episteme` ontic: the knowledge holon, its identity-bearing constitution relation, and the neighboring relations needed for empirical grounding, use, change, description, and publication.

**First useful move.** Name the exact work or decision that will rely on the episteme and the uncertainty or choice the episteme is expected to resolve. Then name the claim content, the identified entity those claims concern, and the effective reference scheme that makes the claims interpretable as claims about that entity. If the named work or decision also depends on empirical grounding, classification, viewpoint, view, claim scope, bounded model use, edition succession, description, or publication, add only the neighboring object or direct relation on which it depends, then apply the pattern governing that object or relation.

**What goes wrong if missed.** A file or diagram becomes "the model"; a subject label drifts while the same episteme name is retained; the holon through which claims are empirically inspected, or the viewpoint from which claims are selected, is copied into episteme identity without justification; or a revised publication is mistaken for a changed knowledge object.

**What this buys.** Epistemes can be compared, revised, grounded, viewed, published, and used recursively while ordinary prose stays short. The complete distinction among the episteme, its direct relations, and their assertion, publication, and representation objects remains recoverable without making users restate every object for every claim.

**Not this pattern when.** Use the direct subject pattern when the current question concerns the system, work, method, relation occurrence, or other entity described by an episteme. Use `A.1` for constructive recognition of a candidate under an admitted holon kind, `C.3.2` for a local-kind membership judgment, and `E.24.UK` for FPF U-kind admission. Use `E.17` and `E.24.PUB` for publication, `A.10` and `B.3` for evidence or assurance, `C.29` for a mathematical representation, and `E.10`, `C.2.P`, or `F.18` for precision restoration or naming. C.2.1 governs episteme identity, including the identity of a separately current classification assertion.

### C.2.1:1 - Problem Frame

FPF treats an episteme as a holon, not as a document class or a filled record. A pump-maintenance specification, a clinical model, a theorem, a learned classifier description, and a curriculum model can all be epistemes when each is a claim-bearing whole about an exact EntityOfConcern under an effective reference scheme. Their carriers, notations, and admissible operations differ, but that difference does not remove the shared ontology question: what makes this one episteme, and what changes its identity?

The episteme ontic coordinates these distinct objects without collapsing them:

1. the `U.Episteme` knowledge holon;
2. direct relation occurrences that constitute, ground, or connect editions of that holon;
3. declaration epistemes whose C.2.1 identity is fixed independently, whose same individual has `U.Signature` membership under `A.6.0`, and whose relation-facing `RelationSignature` use declares reusable participant SlotSpecs for one exact relation kind;
4. assertion epistemes that claim a direct relation predicate obtains and description epistemes whose EntityOfConcern is one explicitly individuated occurrence;
5. publication occurrences that make one selected episteme edition available for a bounded audience and use;
6. publication forms that express the selected edition for that publication use;
7. `U.PresentationCarrier` entities that bear those forms;
8. C.29 mathematical representations that correspond to independently recovered objects for an explicit modeling or reasoning use.

The core constructive question is not which fields a card contains. It is whether an exact `U.ClaimGraph`, exact `U.Entity`, and effective `U.ReferenceScheme` stand in the relation that makes the claim content interpretable and evaluable as claims about that entity. When they do, their selected organization yields a whole-level epistemic characteristic: the resulting holon can be used as one defeasible or deductive body of knowledge. That characteristic is not supplied by any one participant alone.

Any exact `U.Entity` can participate as the EntityOfConcern. An episteme can therefore concern a system, work, method, relation occurrence, another episteme, or itself without changing the constitution relation. Episteme recursion does not introduce a second meta-episteme ontology.

Contemporary work on formal languages as cognitive tools, material and diagrammatic reasoning, distributed representations, and tool-assisted reasoning explains why representation regimes matter. C.2.1 preserves that insight by keeping representation and admitted operations explicit when current. It does not let notation, latent geometry, tool output, or a publication form determine episteme identity.

### C.2.1:2 - Problem

Without one direct episteme ontology, several practical failures recur.

1. **Carrier and episteme collapse.** A PDF, database row, proof script, dashboard, or neural-model file is treated as the knowledge holon. File replacement is then reported as epistemic change even when claim content, EntityOfConcern, and interpretation are unchanged.
2. **Subject drift.** A specification or model keeps one label while the entity it concerns changes. Comparison and evidence use then combine claims about different entities.
3. **Interpretation drift.** The same tokens or graph are read under different designation, measurement, or evaluation rules while users assume one unchanged episteme.
4. **Neighboring-relation collapse.** Grounding holon, viewpoint, view, claim scope, model-use structure, evidence, edition, and publication become optional fields of one omnibus record. Their different obtaining and identity rules disappear.
5. **Representation-first ontology.** Tuple components, graph nodes, schema fields, and database keys are treated as actual relation participants or subject identity discriminators merely because a tool exposes them.
6. **Agency leakage.** A standard, model, method description, or claim graph is said to perform work. Systems perform work; epistemes participate in use, description, evidence, decision, and publication relations.
7. **Dependent-kind identity fork.** A method description or view is assigned another identity merely because its direct pattern supplies a membership condition. The same episteme can then appear twice, and a viewpoint or method-description use can be mistaken for a change of knowledge object.

The familiar Symbol-Concept-Object triangle can still introduce the difference among expression, meaning, and subject. It cannot serve as the ontology because it suppresses reference scheme, grounding, viewpoint, evidence, and the distinction between a relation and a representation of that relation.

### C.2.1:3 - Forces

| Force | Tension |
| --- | --- |
| Readability vs precision | Ordinary use needs a short statement of what an episteme says and concerns; load-bearing use needs exact identity and direct relations. |
| Holon identity vs relation-occurrence identity | The same three participant identities reidentify both the episteme and its constitution-relation occurrence, but the episteme is the knowledge holon and the relation occurrence is the obtaining organization among those participants. |
| Shared episteme identity vs dependent-kind membership | The C.2.1 identity triple identifies every `U.Episteme`. Direct patterns may recognize the same individual as a `U.MethodDescription`, `U.View`, or another admitted dependent episteme kind by a stable membership condition; they do not add a second identity. Grounding, viewpoint, scope, and publication stay in their neighboring relations. |
| Recursion vs circular justification | Epistemes may describe epistemes, including themselves, while an assurance path terminates in separately governed evidence and evaluation relations. |
| Representation variety vs ontology stability | Text, diagrams, formal calculi, learned representations, and interactive tools differ operationally, while representation identity remains distinct from the governed-object identities. |
| Explicit relation distinctions vs usability | The complete set of direct relations, declaration epistemes, assertions, publications, and representations remains recoverable without forcing every engineer to publish a signature, card, or occurrence description for an ordinary claim. |

### C.2.1:4 - Solution

Identify each `U.Episteme` through `EpistemeConstitutionRelation`. State a neighboring relation only when a named receiving use depends on it. Keep declaration epistemes, assertions, descriptions, names, references, publication occurrences, publication forms, carriers, and representations distinct under their direct patterns.

**Local episteme mantra.** *Name the relying work or decision and its unresolved question. Name the claims, what they concern, and the scheme that gives those claims their reference. Add empirical grounding, viewpoint, scope, edition, or publication only when that work or decision depends on it. Update episteme identity only when claim content, EntityOfConcern, or effective reference scheme changes; otherwise update the affected neighboring relation, publication occurrence, publication form, or carrier under its direct pattern.*

The mantra is a recall aid, not a work plan. The application method and stop conditions are carried by sections 4.1-4.9; section 4.10 is a later reference for relation and neighboring-object distinctions.

#### C.2.1:4.0 - First-use completeness questions

Begin with the three questions that identify the episteme. They are identity questions, not fields to fill.

| Always ask | Exact object recovered |
| --- | --- |
| What is being claimed? | the exact claim content carried by one `U.ClaimGraph` |
| What exact entity do those claims concern? | one identified `U.Entity` participating as the EntityOfConcern |
| Under which designation, interpretation, measurement, and evaluation rules are the claims read? | the effective `U.ReferenceScheme` |

Before scanning the conditional questions, ask: **What exact work or decision will rely on this episteme, and what uncertainty or choice is the episteme expected to resolve?** Name that work or decision and the unresolved question in one sentence. Use that answer to select the conditional questions; the named work or decision does not become another constituent of the episteme.

Then scan the conditional questions below. Open only a row whose answer changes what the named work can do or what the named decision can settle. Each positive answer adds an independently governed object or direct relation; none adds another slot to the episteme.

| Ask when it can affect the named work or decision | If yes, recover | Governing pattern |
| --- | --- | --- |
| Does a receiving claim or relation need the exact constitution occurrence rather than only a readable assertion? | one exact obtaining `EpistemeConstitutionRelation` occurrence, reidentified by the participant triple; designate it when an epistemic receiver needs a reference, or use the occurrence itself as a participant when another direct relation is the receiver | C.2.1:4.2.3 and `A.6.REL` |
| Must the claims be empirically inspectable through current observation, intervention, measurement, or evaluation relations? | one exact `EpistemeEmpiricalGroundingRelation` occurrence and its grounding holon; recover any supporting evidence-use relation separately | C.2.1:4.3 and the direct observation, intervention, measurement, or evaluation pattern |
| Does one describing use select the concern under which this episteme is read? | one exact `U.Viewpoint` episteme and the `DescriptionContext` use qualification whose `viewpointRef` resolves to it | `E.10.D2` and `E.17.0` |
| Must a Description episteme be relied on with specification force? | the exact Description episteme, its `DescriptionContext`, checkable claims, and named harness or validation relation required for that use | `E.10.D2` and C.2.1:6 |
| Must this episteme be recognized as a `U.View`? | one exact obtaining `EpistemeViewpointConformanceRelation` between this episteme and at least one exact `U.Viewpoint` episteme | `E.17.0` |
| Was this episteme constructed from another source episteme, and does the current work depend on that history? | the exact source and receiving epistemes plus the governed viewing relation; view membership remains a separate conformance judgment | `A.6.3` for construction and `E.17.0` for membership |
| Are the claims intended to hold only in a declared part of the situation under study? | one exact `U.ClaimScope` and its membership relation over `U.ContextSlice` | `A.2.6` |
| Does interpretation depend on one selected organization of model use? | one exact `BoundedModelUseStructure` and the relation through which the receiving assertion or use selects it | `A.1.1` and the direct receiving-use pattern |
| Does a receiving decision depend on inferential support among claims? | the exact `JustificationGraph` content that carries those dependencies | C.2.1:4.4; use `A.10` or `B.3` only when an evidence-use or assurance-evidence relation is current |
| Does a receiving decision rely on evidence? | the exact evidence-use relation; evidence storage alone is insufficient | `A.10` or `B.3`, according to the evidence use |
| Must a classification judgment be reviewed as a claim-bearing object in its own right? | one classification assertion episteme about the exact candidate, plus the exact governing criterion | C.2.1:4.2.3 with `A.1` or `C.3.2`; `E.24.UK` only for public U-kind admission |
| Is a later episteme being treated as a revision, refinement, or superseding edition of an earlier one? | one exact `EpistemeEditionRelation` occurrence | C.2.1:4.5 |
| Must one selected episteme edition be made available to a declared audience for a bounded use? | the publication occurrence, publication form, and `U.PresentationCarrier` as distinct objects | `E.17` and `E.24.PUB` |
| Does a notation, diagram, mathematical structure, or tool representation change the operations available to the user? | the exact C.29 representation, correspondence, representation scheme, and any current transition relation | `C.29` and the selected representation-transition pattern |

Stop when the remaining conditional questions do not affect the named work or decision. In that ordinary case, a readable sentence naming the claims, EntityOfConcern, and effective reference scheme is enough. Do not complete the table as a record. Use section 4.10 only when a later work occurrence or decision needs the full relation and neighboring-object reference.

#### C.2.1:4.1 - Identify the episteme by its constitution

The shared C.2.1 identity of one `U.Episteme` is:

```text
<claim content, exact EntityOfConcern, effective ReferenceScheme>
```

`claim content` is the identity-bearing `U.ClaimGraph` carried as the episteme's constitutive claim structure. The `EntityOfConcern` is one identified `U.Entity`. When claims jointly concern several entities, identify their one joint EntityOfConcern under its direct pattern; if no one joint entity can be identified, split the claim content instead of filling one slot with unrelated referents. The effective `U.ReferenceScheme` supplies the designation, interpretation, measurement, and evaluation rules by which the claim graph is read as claims about that entity.

Changing any identity discriminator yields another episteme. Changing a carrier, layout, rendering, publication occurrence, evidence item, viewpoint assignment, or model-use setting does not by itself yield another episteme. A direct pattern may recognize the same individual as a dependent episteme kind through its stable membership condition, but it does not add another identity discriminator. `A.3.2` governs `U.MethodDescription` membership; `E.17.0` governs `U.Viewpoint` and `U.View` membership through fixed predicates over already identified epistemes. `A.6.3` governs an optional viewing construction between source and receiving epistemes, not view membership. If any work or construction changes claim content, EntityOfConcern, or effective reference scheme, those changed C.2.1 discriminators identify the resulting episteme, not the dependent-kind label.

This identity is constructive. The claim graph and reference scheme are epistemic constituents; the EntityOfConcern remains an independently governed entity related through aboutness and reference. When `EpistemeConstitutionRelation` obtains, their organization yields the whole-level characteristic of being one interpretable claim-bearing whole. The relation occurrence and the resulting episteme are distinct but reidentified from the same three discriminators.

#### C.2.1:4.2 - Govern the core direct relation

**Tech name:** `EpistemeConstitutionRelation`.

**Plain reading:** these claims, under this reference scheme, are claims about this exact entity and together constitute one episteme.

##### C.2.1:4.2.1 - Participants and the shared reusable-declaration rule

Before using any signature-local table, identify the declaration itself. Each of `EpistemeConstitutionRelationSignature`, `EpistemeEmpiricalGroundingRelationSignature`, and `EpistemeEditionRelationSignature` is first one exact C.2.1 episteme: its own `U.ClaimGraph` carries the declaration claims, its exact EntityOfConcern is the direct relation kind, and its effective `U.ReferenceScheme` makes those claims interpretable. For each of these three declarations the fixed `A.6.0` membership predicate obtains, so `A.6.0` independently recognizes that same episteme individual as a `U.Signature`. `RelationSignature` names the relation-facing use of that same individual; it is neither another U-kind nor another identity.

A complete declaration claim names the direct relation-kind designator, the exact `A.6.5` SlotSpecs needed by reusable typed uses, the obtaining predicate, the occurrence-identity rule, applicability, and only the dependencies and provided names that are actually current. The direct relation kind, its actual participants, an obtaining occurrence, an assertion about it, a relation-occurrence description episteme, the declaration episteme, its publication, and a representation of any of these remain distinct. A receiving need may justify typed reuse but does not identify the declaration. One readable assertion needs no signature or manifest. An A.6.0 manifest is optional and is used only when actual dependencies or provided names must be exposed; a manifest row, list, citation, identifier, or edition marker creates neither episteme identity nor dependency.

Applying that shared rule locally, typed reuse of `EpistemeConstitutionRelation` uses the one declaration episteme `EpistemeConstitutionRelationSignature`, whose exact EntityOfConcern is `EpistemeConstitutionRelation` and whose declaration includes these SlotSpecs:

| SlotKind | Relation-participant meaning | ValueKind | refMode |
| --- | --- | --- | --- |
| `ClaimGraphSlot` | constitutive claim content | `U.ClaimGraph` | `ByValue` |
| `EntityOfConcernSlot` | exact entity the claims concern | `U.Entity` | `U.EntityRef` |
| `ReferenceSchemeSlot` | effective designation and interpretation scheme | `U.ReferenceScheme` | `ByValue` |

The SlotKinds belong only to this declaration. An actual claim graph, EntityOfConcern, or reference scheme is an actual relation participant under its independently governed kind. A card field or assertion designation corresponds to a SlotKind but does not become the participant.

##### C.2.1:4.2.2 - Obtaining and occurrence identity

`EpistemeConstitutionRelation` obtains exactly when the effective reference scheme supplies a coherent designation and interpretation of the claim graph as claims about the exact EntityOfConcern, and the three participants are constitutively organized as one claim-bearing whole whose claims can in principle be evaluated under that scheme. Merely placing three designations in a card does not make the relation obtain.

The relation occurrence is participant-determined by the exact `<ClaimGraph, EntityOfConcern, ReferenceScheme>` triple. The same triple cannot constitute two distinct `U.Episteme` instances under the shared C.2.1 identity rule. Recognition of that individual as a dependent episteme kind adds a membership judgment under the dependent kind's governing pattern, not another constitution occurrence or discriminator. A tuple may represent the triple under `C.29`, but tuple order and storage keys contribute nothing to identity.

The episteme and the relation occurrence are not identical. The relation is the obtaining organization among the three participants. The episteme is the knowledge holon constructively identified through that organization and its whole-level claim-bearing characteristic.

##### C.2.1:4.2.3 - Ordinary assertion, classification assertion, and explicit occurrence use

An ordinary assertion can state that claim content concerns an entity under a scheme without explicitly naming a relation occurrence. When a receiving relation or claim needs the exact constitution occurrence, apply `A.6.REL`: establish obtaining, apply the participant-determined identity rule, then designate the already recoverable occurrence in the receiving episteme. The assertion, designation, and occurrence remain different objects.

Each classification judgment has one pattern governing its criterion. `A.1` governs constructive recognition of a candidate as an instance of an already admitted holon kind. `C.3.2` governs a local-kind membership judgment. `E.24.UK` governs the ontology-level decision that admits a public U-kind; it does not classify a project candidate. None of these judgments is a direct admission relation created by C.2.1.

When project work needs a classification judgment as a separately reviewable claim, identify one claim-bearing episteme whose exact EntityOfConcern is the candidate entity. For an admitted holon kind, its claim content states the kind, cites the `A.1` constructive criterion and any kind-specific criterion, designates the direct part-relation occurrences used in the assessment, and cites any evidence-use relations supporting its modality. For a local kind, its claim content states the candidate, local kind, selected `KindSignature` edition, context slice, and judgment governed by `C.3.2`. A value classification inside another claim can remain claim content of that episteme instead of fabricating a value-shaped EntityOfConcern.

The assertion does not create the candidate, admit a U-kind, or make the candidate change kind when an FPF host is renamed or republished. For example, the assertion that Pump #37 satisfies the constructive `U.System` criterion may be revised when evidence changes, while Pump #37 and the criterion it satisfies retain their independently governed identities.

A card that calls a listed collection a holon is still only a classification assertion episteme. The positive assertion is unsupported unless `A.1` recovers the exact constituents and grounded part relations, their constructive assembly, the whole's reidentification rule, actual compatibility with a governed larger-assembly construction, a composition-grounded whole-level characteristic, and the already admitted holon kind with its kind-specific criterion. The card form supplies none of those facts.

#### C.2.1:4.3 - Add empirical grounding through its own relation

**Tech name:** `EpistemeEmpiricalGroundingRelation`.

**Plain reading:** this episteme's claims are empirically grounded in this exact holon through the current observation, intervention, measurement, or evaluation relations.

This relation connects one already identified `U.Episteme` to one exact `U.Holon` when an empirically inspectable structure of independently governed direct observation, intervention, measurement, or evaluation relations involving that holon grounds the episteme's claims under its effective reference scheme. Purely formal epistemes need no grounding occurrence merely to fill a record.

Applying the shared declaration rule in 4.2.1, `EpistemeEmpiricalGroundingRelationSignature` is one declaration episteme whose exact EntityOfConcern is `EpistemeEmpiricalGroundingRelation`; the same individual has `U.Signature` membership and relation-facing `RelationSignature` use only under `A.6.0`. Its complete declaration includes the obtaining predicate, maximal-continuous-interval identity rule, applicability, actual dependencies and provided names, and these SlotSpecs:

| SlotKind | Relation-participant meaning | ValueKind | refMode |
| --- | --- | --- | --- |
| `GroundedEpistemeSlot` | episteme whose claims are grounded | `U.Episteme` | `U.EpistemeRef` |
| `GroundingHolonSlot` | exact holon involved in the direct observation, intervention, measurement, or evaluation relations that provide the grounding | `U.Holon` | `U.HolonRef` |

`EpistemeEmpiricalGroundingRelation(E,H)` obtains exactly while, under E's effective reference scheme, a current structure of direct observation, intervention, measurement, or evaluation relation occurrences involving H makes E's exact claims empirically inspectable. Those world-side relation occurrences, not the presence of an evidence episteme, evaluation report, storage record, or work log, supply the grounding condition. An exact evidence-use or assurance relation may support an assertion that grounding obtains or qualify its warrant or confidence; evidence storage, availability, or loss neither makes nor unmakes the grounding relation.

One occurrence is identified by `<episteme, grounding holon, maximal continuous grounding interval>`. Closing the open end of an ongoing interval refines the description of the same occurrence. A demonstrated loss and later restoration of the direct grounding-relation structure yields another occurrence. Evidence availability or absence alone licenses no inference that current obtaining is true, false, or unresolved and neither proves nor disproves a temporal gap. If the direct grounding-relation structure is known to obtain, the grounding relation obtains even when supporting evidence or a work log is absent. If that direct structure is known not to obtain, the grounding relation does not obtain even when evidence or a work log is absent. Only when the status of the direct structure itself is unknown is a positive assertion that grounding obtains unresolved.

The grounding holon need not be identical to the EntityOfConcern. A method description may concern a method while one grounding occurrence links that episteme to the exact enactment work and another links it to the system whose behavior was observed. A review episteme may concern another episteme while being grounded in the exact experiment work or operating system involved in the direct testing relations. Sharing one grounding holon makes comparison inspectable but does not prove that two epistemes have the same EntityOfConcern or content.

#### C.2.1:4.4 - Keep neighboring uses under their direct relations

| Current distinction | Relation or object to use | Why it stays outside the core constitution relation |
| --- | --- | --- |
| classification judgment or separately current classification assertion | the `A.1` recognition judgment for an admitted holon kind or the `C.3.2` membership judgment for a local kind; one C.2.1 episteme when a receiving review treats the judgment as a separate claim-bearing object | the governing criterion states the membership condition; the classification judgment evaluates the candidate under it; the assertion carries that judgment but neither creates the candidate nor admits the kind |
| claim scope | exact `U.ClaimScope` and its A.2.6 membership semantics | scope delimits where claims hold; it does not identify every episteme |
| concern-bearing viewpoint use | one exact `U.Viewpoint` episteme selected through the current `DescriptionContext` use qualification | selection states the concern under which the description is used; it neither establishes conformance nor enters episteme identity |
| view | the same episteme individual recognized as `U.View` when an exact `EpistemeViewpointConformanceRelation` to at least one exact viewpoint episteme obtains | conformance, source-to-receiving construction, current-use selection, publication, form, and carrier remain different relations or objects |
| bounded model use | optional relation to one `BoundedModelUseStructure : U.Structure` under A.1.1 | model-use organization can qualify interpretation without becoming a universal identity component |
| justification structure | exact `JustificationGraph` content | a justification structure organizes inferential dependencies without becoming claim content |
| evidence use | the evidence relation governed by A.10 or B.3 that the current claim uses | evidence may support or qualify an assertion about claim truth or grounding; storage, availability, or loss of evidence or a work log neither makes nor unmakes the world-side grounding relation |
| publication | exact publication occurrence and publication form under E.17 and E.24.PUB | making an edition available does not constitute or reidentify it |
| presentation carrier | any exact `U.PresentationCarrier` under E.17 and E.24.PUB | bearing a publication form or rendered expression does not constitute or reidentify the episteme |
| representation and admissible operations | representation scheme currently used for the exact represented episteme, its selected elements, and the C.29 correspondence or transition relations | a change of scheme or admitted operations can change the available work without becoming the represented ontology |

Names ending in `Slot` are admissible here only as SlotKinds inside the exact `RelationSignature` governed by the neighboring direct relation pattern. A card or other episteme form carries participant designations in ordinary fields; it does not acquire SlotKinds by using similar field labels. None of those neighboring SlotSpecs belongs to `EpistemeConstitutionRelationSignature`.

#### C.2.1:4.5 - Relate distinct episteme editions explicitly

**Tech name:** `EpistemeEditionRelation`.

**Plain reading:** this later episteme continues this earlier episteme as a revision, refinement, or superseding edition.

`EpistemeEditionRelation` has exactly two direct participants. Applying the shared declaration rule in 4.2.1, `EpistemeEditionRelationSignature` is one declaration episteme whose exact EntityOfConcern is `EpistemeEditionRelation`; the same individual has `U.Signature` membership and relation-facing `RelationSignature` use only under `A.6.0`. Its complete declaration includes the direct predicate, participant-determined identity, applicability, actual dependencies and provided names, and these SlotSpecs:

| SlotKind | Relation-participant meaning | ValueKind | refMode |
| --- | --- | --- | --- |
| `EarlierEpistemeSlot` | exact episteme continued by the later edition | `U.Episteme` | `U.EpistemeRef` |
| `LaterEpistemeSlot` | exact episteme that continues the earlier edition | `U.Episteme` | `U.EpistemeRef` |

The relation obtains when the two epistemes have different C.2.1 identities and one exact system performed revision, refinement, or supersession work under a method whose semantics establish historical continuation. `C.2.P` recovers the exact source expression and the source-to-revision-use relation by which the earlier episteme participates. Exact change facts already governed by their current patterns can contribute to evaluating the edition-continuity predicate. When the receiving claim additionally depends on first constitution of the later episteme by that work, use a current direct entity-identity-inception governor only if one actually exists; otherwise return the exact missing-governor blocker and do not assert the edition relation. Once all required facts have direct governors, those facts and the enacted method satisfy the edition-continuity predicate; evaluation and evidence make an assertion about that predicate inspectable. The system, work, method, source-use relation, change or inception claims, evaluation, and evidence are not participants of `EpistemeEditionRelation`.

One occurrence is participant-determined by the exact `<earlier episteme, later episteme>` pair. Two work occurrences that establish the same historical continuation do not create two edition-relation occurrences. The relation is acyclic in its earlier-to-later direction. A renamed file, later publication, shared title, or bare provenance edge establishes no occurrence. Loss of a work log can lower confidence in an assertion about the relation, but it does not turn the work log into a third participant.

Several edition-relation occurrences may be selected as a lineage structure only when a receiving use depends on their organization. If that use also selects an edition collection, `A.14` governs membership in that separately identified collection; collection membership does not establish edition continuity. `PhaseOf` may describe one unchanged episteme over a proper time interval, but it does not connect two different C.2.1 identities.

When claim content, EntityOfConcern, or effective reference scheme changes, the later object is another episteme. Apply `EpistemeEditionRelation` only when its historical-continuation predicate above obtains, whether the continuation is revision, refinement, or supersession. Apply `A.6.4` separately only when the current claim is an effect-free retargeting between epistemes with different but bridge-related EntitiesOfConcern under its invariant; retargeting does not by itself establish edition continuity. A changed publication form alone identifies neither another episteme nor an edition relation.

#### C.2.1:4.6 - Keep descriptions, cards, publications, and representations downstream

A claim-bearing filled card can itself be an episteme when its claim content, EntityOfConcern, and effective reference scheme are recoverable. The reusable arrangement of that card can instead be a publication form, and a selected graphical or tabular element can participate in a C.29 representation. Identify each object through its own constitution and the direct relation in which it participates; visible shape does not determine its kind.

When a card or other form designates the participants of one direct relation, its field labels may correspond to SlotKinds in that relation's `RelationSignature`, and its field values may be by-value designations or references of the declared refModes. The form is not a filled direct relation occurrence; supplying fields does not make the predicate obtain or provide occurrence identity.

In a relational assertion, the claim graph states a modality for the direct obtaining predicate and designates the actual participants. A positive assertion may also designate an already individuated occurrence. In a relation-occurrence description episteme, the EntityOfConcern is that exact occurrence. The assertion and description retain their own C.2.1 identities; neither supplies the occurrence's obtaining or identity rule.

Keep the direct verbs with their objects. A designator designates an already recoverable referent. A governed reference resolves to that referent under an effective reference scheme. An assertion or description episteme carries claims and participant designations. A C.29 representation stands in an explicit correspondence to what it represents. A publication occurrence makes a selected episteme edition available; a publication form expresses that edition for the use; a presentation carrier bears the form.

Plain **published episteme** means one already identified `U.Episteme` that currently participates as the selected edition in an exact publication occurrence. It is a contingent publication use, not a durable `U.EpistemePublication` kind and not a second identity for the episteme. The episteme keeps the same C.2.1 identity before, during, and after that availability relation.

A publication occurrence makes one selected episteme edition available to a declared audience for a declared bounded use. A publication form expresses that edition for the publication use. A `U.PresentationCarrier` bears the form. These are three different direct relations governed by `E.17` and `E.24.PUB`; an assertion that any one obtains is a separate episteme. C.2.1 governs the identity of the selected `U.Episteme`; it does not replace the participants, predicates, or occurrence rules of those publication relations.

One completed inspection card shows why the distinctions matter. Its filled claims can identify one episteme; its reusable layout can be a publication form; its paper sheet or file can be a presentation carrier; and a publication occurrence can make the selected card episteme edition available to the maintenance team. None of those uses makes the others identical.

When rendering is current, a system performs rendering work and the exact work-participation, transformation, or A.6.1 binding current in that case relates the work to its affected entities. If the work first constitutes a rendered entity and that identity-inception claim matters, use a current direct entity-identity-inception governor only when one actually exists; otherwise retain the exact missing-governor blocker. Rendering work, rendered entity, publication occurrence, form, carrier, and episteme retain their own identities. Republishing unchanged claims with another form or carrier creates no new episteme edition.

Under `C.29`, a tuple can represent the identity triple and a graph or hypergraph can represent claim, justification, dependency, or relation structure. `U.ClaimGraph` and `JustificationGraph` remain graph-valued epistemic structures. Their nodes and edges remain representation elements. An explicit correspondence can relate one selected representation element to an independently recovered object, but it neither identifies the two nor makes the representation element a participant of the represented direct relation.

#### C.2.1:4.7 - Preserve description and meta-description recursion

If episteme `E1` describes pump `P`, `P` is the EntityOfConcern participant in the constitution relation that identifies `E1`. If review episteme `E2` describes `E1`, then `E1` is the EntityOfConcern participant for `E2`. The two relations have different triples and therefore identify different epistemes.

An episteme may describe itself when its own identity remains recoverable. Self-reference never closes an assurance argument by itself. Each justification or evaluation path terminates in independently governed evidence, observation, or formal derivation rather than in a cycle of claims that cite one another.

Description and specification use remain distinct. A Description episteme is admitted for specification use only when the `E.10.D2` conditions are satisfied: checkable claims, a preserved or explicitly updated DescriptionContext, and a named harness or validation relation. Formal notation alone does not grant specification use or change the episteme's kind.

#### C.2.1:4.8 - Locate the change before updating episteme identity

| Observed change | Disposition |
| --- | --- |
| claim content, EntityOfConcern, or effective reference scheme changes | identify another episteme; use `EpistemeEditionRelation` only for revision, refinement, or supersession when its historical-continuation predicate obtains, and use `A.6.4` separately only for an exact retargeting that satisfies its own predicate; otherwise stop at the new identity without inferring continuity |
| direct empirical-grounding relation structure begins to obtain, ceases to obtain, or is restored | evaluate `EpistemeEmpiricalGroundingRelation` continuity; do not change episteme identity unless a core discriminator also changed |
| an evidence item, evaluation report, evidence store, or work log becomes available or unavailable while the status of the direct grounding-relation structure stays fixed | revise only the separately governed support, warrant, confidence, or evidence-use assertion that changed; the unchanged direct structure still determines grounding status and occurrence continuity: known obtaining continues, known nonobtaining remains nonobtaining, and unknown structure status leaves a positive grounding assertion unresolved |
| candidate episteme E or viewpoint episteme P changes | identify the changed episteme under C.2.1, then test the new exact E/P pair under `E.17.0`; for fixed E and P, conformance cannot change because of evaluator, evidence, project, publication, or current use, so state any changing adequacy or evaluation as a separate claim |
| one `DescriptionContext` has its `viewpointRef` resolve to one identified `U.Viewpoint` episteme for a describing use | update that use's exact `viewpointRef` only; `DescriptionContext` has no `viewRef`, selects no view, and establishes neither conformance, `U.View` membership, nor episteme identity |
| claim scope changes | update the exact `U.ClaimScope` and its A.2.6 membership semantics; do not infer another episteme automatically |
| selected bounded model-use or multi-view structure changes | update the exact collection or structure relation and re-evaluate affected interpretation claims; do not infer another episteme or view family automatically |
| publication form, carrier, rendering, audience, bounded use, or publication occurrence changes | establish the exact E.24.PUB change only; publication is not view membership or episteme succession |
| mathematical or tool representation changes | apply C.29 and the selected representation-transition relation |

#### C.2.1:4.9 - Hand episteme transformations to their governing patterns

A.6.2-A.6.4 govern episteme-to-episteme morphing, source-to-receiving viewing construction, and retargeting. Identify every source and receiving episteme independently under C.2.1 before testing the exact transformation relation. Each transformation pattern states which identity discriminator is preserved or changed and names the exact correspondence, reinterpretation, or retargeting relation on which it relies. When local senses cross contexts, `F.9` additionally governs Bridge direction, congruence, loss, and admitted use. Categorical function, mapping, or tuple notation creates no direct relation occurrence.

For an A.6.3 source-to-receiving viewing construction, the two identified epistemes may retain the same EntityOfConcern while claim content or effective scheme is restricted. `E.17.0` alone judges whether the receiving episteme conforms to an exact viewpoint and therefore has dependent `U.View` membership. Direct authoring or query generation can yield a candidate episteme without an A.6.3 construction, and neither route creates a multi-view family. For retargeting, the EntityOfConcern changes under an explicit bridge or correspondence. For a representation transition, the represented episteme may remain unchanged while the C.29 representation scheme and admitted operations change.

#### C.2.1:4.10 - Relation and neighboring-object reference

| Current object | FPF kind or relation | Governing pattern |
| --- | --- | --- |
| `U.Episteme` | one knowledge holon with identity `<claim content, EntityOfConcern, effective ReferenceScheme>` | C.2.1 |
| `EpistemeConstitutionRelation` occurrence | the obtaining direct relation among the exact claim graph, exact EntityOfConcern, and effective reference scheme that constructively identifies one episteme | C.2.1 and `A.6.REL` |
| `EpistemeEmpiricalGroundingRelation` occurrence | the direct relation between one identified episteme and one exact grounding holon when a current structure of direct observation, intervention, measurement, or evaluation relations involving that holon makes the claims empirically inspectable; evidence use may support an assertion but is not the obtaining condition | C.2.1 and the governing observation, intervention, measurement, or evaluation patterns |
| classification assertion episteme, when separately current | a claim-bearing episteme whose EntityOfConcern is the exact candidate and whose claim content states a classification judgment under the exact governing criterion: `A.1` for an admitted holon kind or `C.3.2` for a local kind | C.2.1 for assertion identity; the pattern governing the criterion for the judgment; `E.24.UK` only for public U-kind admission |
| `EpistemeEditionRelation` occurrence | the direct historical continuation relation between one exact earlier episteme and one exact later episteme; exact source-to-revision use, enacted-method semantics, actual change facts, and any required separately governed entity-identity-inception claim make its obtaining predicate evaluable but do not participate in the relation | C.2.1, coordinated with `C.2.P`, A.3.1, A.3.4, and a current direct entity-identity-inception governor only when that claim is required and such a governor exists; if a required claim lacks one, return the exact missing-governor blocker |
| `EpistemeConstitutionRelationSignature`, `EpistemeEmpiricalGroundingRelationSignature`, or `EpistemeEditionRelationSignature` | one C.2.1 declaration episteme whose exact EntityOfConcern is its direct relation kind; the fixed `A.6.0` predicate gives that same individual `U.Signature` membership, and `RelationSignature` is its relation-facing use with complete direct semantics and exact A.6.5 SlotSpecs | C.2.1 for declaration identity, `A.6.0` for membership and reusable vocabulary, and `A.6.5` for SlotSpecs |
| `SlotSpec` | one declaration-content component of that `RelationSignature` | `A.6.5` |
| assertion or description episteme | a claim-bearing episteme that states or describes one of the direct relations | C.2.1 and the direct claim or description pattern |
| `U.MethodDescription` | the same `U.Episteme` individual when A.3.2 recognizes one admitted `U.Method` as its exact EntityOfConcern and its claims, interpreted under the effective `U.ReferenceScheme`, make at least one substantive claim about that method as a way of doing; mention, bibliographic metadata, or approval alone does not establish membership, and adequacy for a receiving use is evaluated separately | C.2.1 for episteme identity; `A.3.2` for dependent-kind membership |
| `U.View` | the same `U.Episteme` individual when `EpistemeViewpointConformanceRelation` to at least one exact `U.Viewpoint` episteme obtains; fixed E/P conformance, source-to-receiving construction, current-use selection, and publication remain separate | C.2.1 for episteme identity; `E.17.0` for dependent-kind membership; `A.6.3` only when source-to-receiving construction is current |
| `DescriptionContext` viewpoint resolution | the exact `viewpointRef` in `<EntityOfConcernRef, BoundedContextRef, ViewpointRef>` resolves one already identified `U.Viewpoint` episteme for a describing use; it has no `viewRef` and selects no view | `E.10.D2` and `E.17.0` |
| multi-view collection or organization | an exact C.13 collection only when a receiving use depends on the plurality as a collection, and an exact A.22 `U.Structure` only when that use additionally depends on organization among those views | `C.13`, `A.22`, and the direct organizing relations |
| cross-view correspondence, consistency, realization, trace, or change-impact claim | one exact direct subject relation under its own governor; a C.2.1 episteme may assert or describe it, but a heading, edge, carrier, or E.17 publication invents no relation | the exact direct relation pattern; when none is current, return an exact missing-relation blocker naming the participants, required predicate and use, and missing governor |
| publication occurrence | the occurrence that makes one selected episteme edition available to a declared audience for a declared bounded use | `E.17` and `E.24.PUB` |
| publication form | the arrangement, notation, or rendering convention that expresses the selected episteme edition for that publication use | `E.17` and `E.24.PUB` |
| `U.PresentationCarrier` | the exact physical or digital carrier that bears the publication form | `E.17` and `E.24.PUB` |
| mathematical representation | a C.29 representation used for an explicit modeling or reasoning purpose | `C.29` |

This reference table keeps the neighboring objects and relations visible after the application method. Ordinary prose names only the current object and its direct relation. A sentence such as “Model M concerns Pump P under Scheme S” is sufficient until another use needs explicit empirical grounding, a classification assertion, occurrence identity, edition continuity, publication, or representation correspondence.

### C.2.1:5 - Semantic triangle as a didactic projection  *(informative)*

The Symbol-Concept-Object triangle is a teaching projection, not the episteme ontology.

| Triangle corner | C.2.1 projection | What the projection suppresses |
| --- | --- | --- |
| Symbol | selected representation elements and any publication carrier | representation scheme, admitted operations, publication occurrence, and correspondence to the episteme |
| Concept | `U.ClaimGraph` interpreted under an effective `U.ReferenceScheme` | claim scope, justification, viewpoint, and edition relations |
| Object | exact EntityOfConcern and any current `EpistemeEmpiricalGroundingRelation` | the difference between what claims concern and the holon through which they are empirically inspectable |

A triangle diagram may be used to introduce expression, meaning, and subject if its caption says that it compresses the C.2.1 episteme ontic. Its corners and arrows are representation elements. They supply no SlotKinds, direct relation occurrences, or identity rules.

This limitation matters in practice. A proof-assistant term, wiring diagram, clinical chart, learned embedding, or verbal explanation can all occupy the Symbol corner while supporting different operations and different losses. Those questions belong to the representation-scheme and transition patterns; one geometric picture does not answer them.

### C.2.1:6 - Description and specification-use boundary  *(normative)*

A Description episteme is a `U.Episteme` whose exact EntityOfConcern is the entity being described. Description does not create a second kind beside ordinary epistemes; it names the current relation and use of one episteme.

For a description use, keep these values recoverable:

| Value | Meaning | Identity status |
| --- | --- | --- |
| `entityOfConcernRef` | designation of the exact EntityOfConcern in the description episteme's constitution relation | its resolved exact EntityOfConcern, not the reference value or designation, is C.2.1 identity-bearing |
| effective `U.ReferenceScheme` | rules by which the description claims refer to and can be checked against that entity | C.2.1 identity-bearing |
| `viewpointRef`, when current | governed reference resolving to the exact `U.Viewpoint` episteme selected for this describing use under E.17.0 | use qualifier outside episteme identity; work that changes an identity discriminator identifies another episteme independently |
| `claimScopeRef`, when current | designation of the exact `U.ClaimScope` under A.2.6 | claim-use qualifier |
| `modelUseStructureRef`, when current | designation of one independently selected `BoundedModelUseStructure : U.Structure` | optional interpretation qualifier, not a context root |

When a filled card used to describe the entity has recoverable claim content, EntityOfConcern, and effective reference scheme, it is one episteme carrying these values. Its reusable layout can be a publication form, and the exact sheet or file that bears that layout can be a `U.PresentationCarrier`. The episteme, form, and carrier are not direct relation occurrences, and none makes a viewpoint, scope, or model-use relation obtain.

`E.10.D2` governs the distinction among the EntityOfConcern, its Description episteme, and specification use. A Description episteme is admitted for specification use only when `E.10.D2` checkability, DescriptionContext, and harness or validation conditions are satisfied. The suffix `Spec`, formal notation, approval appearance, or publication in a repository does not grant that use.

Self-description uses the same rule. If an episteme describes itself, its EntityOfConcern designation resolves to that episteme. If a review episteme describes it, the review episteme has the first episteme as EntityOfConcern and its own claim content and reference scheme.

### C.2.1:7 - Episteme morphing, viewing, and retargeting  *(normative)*

C.2.1 governs episteme identity discriminators and neighboring relations. A.6.2-A.6.4 govern transformations between epistemes.

#### C.2.1:7.1 - Effect-free episteme morphing

For a morphism from episteme `X` to episteme `Y`, state by value:

1. which of claim content, EntityOfConcern, and effective reference scheme are preserved, restricted, bridged, or changed;
2. which viewpoint, empirical-grounding, claim-scope, model-use, evidence, or representation relations are read or changed;
3. which claims in `Y` are preserved from or supported by `X` under the named morphism, the exact correspondence or retargeting relation governed by that morphism pattern, and any `F.9` Bridge that governs cross-context sense use when current;
4. whether the operation changes only epistemes or also entails separately governed work or transformation.

The morphism declaration and any categorical notation are epistemic or mathematical objects. Only systems perform exact authoring, query, translation, or other work. `A.6.1` declares typed argument and result positions. When an exact operation application is current, each application binding relates one exact entity to its declared argument or result position; every bound entity retains its independently governed kind, identity, and any domain-result algebra. Identify the affected or newly constituted entity, the actual change facts, and the C.2.1 discriminators independently. When a receiving claim depends on first constitution of that entity by the exact work and change facts, use a current direct entity-identity-inception governor only if one actually exists; otherwise return the exact missing-governor blocker. No bare A.6.1 `result`, generic work result, universal work-result relation, or universal production relation is inferred from a morphism arrow, declaration, or application.

#### C.2.1:7.2 - Epistemic viewing

`A.6.3` governs an exact source-to-receiving viewing construction when one separately identified receiving episteme is constructed from one separately identified source episteme. That construction may preserve the exact EntityOfConcern while restricting claim content or specializing the effective reference scheme. It neither grants `U.View` membership nor performs work. Direct authoring and query generation can identify receiving epistemes without this construction relation.

`E.17.0` independently judges `EpistemeViewpointConformanceRelation(E,P)` for one fixed receiving episteme E and one fixed viewpoint episteme P; only that obtaining relation gives the same E dependent `U.View` membership. A system may perform viewing, query, authoring, or rendering work. When exact work and change facts first constitute E and that inception claim matters, use a current direct entity-identity-inception governor only if one actually exists; otherwise return the exact missing-governor blocker.

Empirical grounding continues only while the receiving episteme has its own admissible direct grounding-relation structure. Changing publication, current use, evaluator, or evidence alone changes neither fixed E/P conformance nor grounding. Several source or receiving epistemes do not automatically form a multi-view family; identify any current collection under C.13 and any selected organization under A.22.

#### C.2.1:7.3 - Epistemic retargeting

`U.EpistemicRetargeting` is an effect-free morphism relating epistemes with different exact EntitiesOfConcern. `A.6.4` governs the exact correspondence, reinterpretation, or retargeting relation that states what is preserved across the change. When the move also crosses context-local senses, `F.9` supplies the Bridge direction, congruence level, loss notes, and admitted use; it does not replace the subject-side relation. A system may perform exact retargeting work; identify its enacted method and any exact A.6.1 operation application. For each current application, recover each application binding that relates one exact entity to its declared argument or result position; every bound entity retains its independently governed kind, identity, and any domain-result algebra. Identify the affected or newly constituted entity and the actual change facts separately. When first constitution of that entity by the exact work and change facts matters, use a current direct entity-identity-inception governor only if one actually exists; otherwise return the exact missing-governor blocker. The retargeting morphism itself performs no work, and no bare A.6.1 `result`, generic work result, or universal production relation is inferred.

Examples include retargeting from a module to a function it realizes, from observations to a learned model, or from one holon to a meta-holon or subholon with a different EntityOfConcern. A Fourier representation change is not automatically retargeting: use C.29 first to decide whether the signal remains the EntityOfConcern and only its representation changes. This test prevents mathematical notation from deciding ontology.

### C.2.1:8 - Multi-view description and publication  *(normative)*

C.2.1 identifies every candidate episteme and every viewpoint episteme separately. `E.17.0` alone judges each exact `EpistemeViewpointConformanceRelation(E,P)` and the resulting same-individual `U.View` membership. `DescriptionContext = <EntityOfConcernRef, BoundedContextRef, ViewpointRef>` qualifies one describing use: its singular `viewpointRef` resolves one exact viewpoint episteme, it has no `viewRef`, and it selects no view. If another exact receiving-use qualification selects an already identified view, name that use and its exact governor separately. Neither qualification enters episteme identity or establishes conformance.

Several conforming views remain a plurality. Recover an exact C.13 collection only when a receiving use depends on that plurality as a collection. Recover an exact A.22 `U.Structure` only when the use additionally depends on organization among those views, and state the exact direct organizing relations. A shared EntityOfConcern, package, table, heading set, diagram, or carrier creates neither a view family, a collection, nor that structure.

`A.6.3` governs only an obtaining source-to-receiving viewing construction when that history is current; direct authoring and query generation require no such relation. A system performs any viewing, authoring, query, comparison, or repair work. When exact work and change facts first constitute an episteme and that claim matters, use a current direct entity-identity-inception governor only if one actually exists; otherwise return the exact missing-governor blocker. Neither work route nor inception grants `U.View` membership.

`E.17` governs multi-view publication forms and uses, while `E.24.PUB` governs publication occurrences, forms, and carriers. The same recognized view can participate as the selected episteme in several publication occurrences without changing identity or conformance. Publication establishes no view membership and no cross-view subject relation.

When cross-view correspondence, consistency, realization, trace, or change impact matters, name the exact participants and apply the exact direct subject-relation governor. A C.2.1 assertion or description episteme may carry that claim; it does not make the relation obtain. If no direct governor is recoverable, return an exact missing-relation blocker naming the participants, required predicate and use, and missing governor; do not invent a relation. `E.17`, a matching heading, graph edge, diagram position, or shared carrier invents no correspondence relation.

### C.2.1:9 - Archetypal Grounding — Worked Cases

These cases ground the pattern in practice; only a case that names an obtaining `EpistemeEmpiricalGroundingRelation` asserts empirical grounding.

#### C.2.1:9.1 - Physical engineering

A pump-maintenance specification has a claim graph about exact pump `P` under a reference scheme that resolves part names, states, units, and measurement procedures. Those three participants identify the episteme. If the claims are tested on test bench `B`, an `EpistemeEmpiricalGroundingRelation` connects the specification episteme to `B` for the maximal continuous interval in which the direct inspection and measurement relation structure involving `B` remains admissible. If that structure is known to continue while an evidence archive or inspection-work log becomes unavailable, the grounding occurrence continues; only a separately governed support, warrant, confidence, or evidence-use assertion may change. A publication occurrence makes the episteme available through a rendered checklist form borne by an exact carrier; systems assigned the relevant roles perform the maintenance or inspection work recorded by checklist marks. A separately current assertion that `P` satisfies the constructive `U.System` criterion is another episteme about `P`; renaming or republishing the governing FPF pattern does not change `P` or create its systemhood.

The classification assertion changes only when its own claim content or reference scheme changes. Pump continuity is judged instead under the `A.1` reidentification rule; a changed or unchanged assertion does not establish that continuity.

#### C.2.1:9.2 - Medicine

A diagnostic model concerns one patient-state entity or one admitted patient cohort under a scheme that defines observations, measurements, and diagnostic interpretations. Systems and role assignments participating in clinical work retain their own direct relations; they are not absorbed into the model's EntityOfConcern. Empirical grounding is stated by an `EpistemeEmpiricalGroundingRelation` whose episteme, grounding holon, direct grounding-relation structure, and maximal continuous obtaining interval are identified. If a threshold revision changes claim content or the effective reference scheme, that changed discriminator identifies another episteme; moving the unchanged model to another screen changes only the exact publication or representation object that actually changed.

#### C.2.1:9.3 - Learning

A curriculum model concerns an exact competence structure under a scheme that relates learning evidence and performance observations to competence claims. One exact admitted course-cohort holon or one exact admitted learning-environment holon may participate in a separate grounding occurrence without becoming the competence structure. A learner-facing episteme is a `U.View` when it conforms to an exact learner-facing viewpoint under `E.17.0`. If it was constructed from the source curriculum-model episteme, `A.6.3` governs that separate viewing relation; systems in roles perform the lesson-session or receiving-episteme authoring or construction work. Any first-constitution claim requires a current direct entity-identity-inception governor; when none actually exists, retain the exact missing-governor blocker.

#### C.2.1:9.4 - Episteme about an episteme

Simulation model `M` is one episteme. Review `R` concerns `M`, so the EntityOfConcern in `R` is the episteme `M`, not the physical system modeled by `M`. Claims in either episteme may cite separately governed evidence-use relations concerning the simulated or physical system. Publishing `R` does not revise `M`.

A theory episteme is recognized through its claim-bearing constitution and whole-level inferential characteristics. A textbook publication can make one edition of that theory available, but the publication occurrence, form, and carrier are not constituents of the theory and do not establish its holonhood.

#### C.2.1:9.5 - Edition succession

Episteme `E1` participates in revision work `W2` through the exact source-to-revision-use relation recovered by `C.2.P`; `E2` has changed claim content and a separately recovered C.2.1 identity. The revision method enacted in `W2` and the actual change facts contribute to evaluating `EpistemeEditionRelation(E1, E2)`. If that evaluation additionally depends on first constitution of `E2` by `W2`, a current direct entity-identity-inception governor must supply that claim; when none actually exists, return the exact missing-governor blocker instead of asserting the edition relation. Once every required fact is governed, the relation chain makes an assertion about the predicate inspectable, but `W2` is not a third participant and does not distinguish another occurrence for the same pair. Later systems may perform repackaging work whose exact effects concern a publication form or carrier for `E2`; a publication occurrence then makes `E2` available. Neither repackaging nor publication establishes `E3`.

#### C.2.1:9.6 - Grounded identity across two observations

A morning-observation episteme concerns observed object `M` under one reference scheme; an evening-observation episteme concerns observed object `E` under another. A physically testable trajectory together with observations can support an assertion that `M` and `E` designate the same planet only under the exact direct identity or reidentification governor for the observed entity. If no such current governor is recoverable, keep the identity claim unresolved and return an exact missing-relation blocker naming `M`, `E`, the required identity predicate and use, and the missing governor. The assertion is another episteme whose claim content designates the direct identity and evidence relations that make its modality inspectable. Once both designations resolve to the same exact entity, the two observation epistemes still need not merge: their claim graphs or effective reference schemes can keep their C.2.1 identities different. A shared label or shared grounding holon alone establishes neither world-side identity nor episteme identity.

#### C.2.1:9.7 - Readable wiring diagram as a proxy

Wiring-model episteme `E1` concerns exact harness `H` under reference scheme `S1`, which resolves connector designators, pin identities, and connection predicates. A system performs exact diagram-redrawing work; any operation application, binding, or declared result position is governed separately by A.6.1. If only layout changes in a C.29 wiring-diagram representation, identify the exact representation transition and preserved connector, pin, and connection correspondence; `E1` remains the same. If instead only an exact publication form, carrier, or rendering changes, identify that E.17/E.24.PUB object and relation; `E1` again remains the same. These branches are not one undecided representation-or-form result. The redraw work and actual change facts remain independent. If a receiving claim also depends on first constitution of a changed entity by that work, use a current direct entity-identity-inception governor only if one actually exists; otherwise retain the exact missing-governor blocker. If a connection claim is omitted or the legend changes the effective reference scheme, the changed claim graph or scheme identifies episteme `E2` independently of the redraw-work identity or any inception claim.

For the `C.29` lens-use statement, the target phenomenon is the connectivity of `H`; the candidate mathematical object is the wiring-diagram representation under its stated diagram scheme; the mapping resolves connector marks and pin marks to the independently identified connectors and pins. A layout-only transition preserves connector identity, pin identity, and connection predicates. An omitted connection loses one predicate, while a changed legend loses the earlier mark-to-connector reference. The diagram remains admissible for maintenance diagnosis only while the connections on which that diagnosis depends are preserved and recoverable; stop that use or return to the source relation structure when they are not. This representation statement does not prove that the diagram is the harness, that visual similarity preserves claims, or that a higher readability score preserves episteme identity.

A readability score can therefore improve while diagnosable connectivity becomes worse. When that score is used as the practical value, apply `E.13`: name the intended diagnostic value, the readability proxy, and what became worse. `C.29` and `A.6.3.RT` govern the representation transition and its preserved or lost structure; C.2.1 decides whether the changed claim graph or effective reference scheme identifies another episteme.

#### C.2.1:9.8 - Learned representation and tool-using inference

A language-model system performs one inference-work occurrence and may perform tool-call work during it. First recover a distributed activation pattern as an exact system-side phenomenon observed during that work. A probe's learned representation or decoded rendering may represent that phenomenon for a declared use under `C.29` and `A.6.3.RT`; causal influence, decodability, or a readable label does not by itself make the activation pattern or its representation a `U.Episteme`. A probe result or decoded rendering is admitted as an episteme only when recoverable claim content concerns an exact EntityOfConcern under an effective reference scheme.

Keep the other entities and claims separate through their exact direct relations. A tool-call trace may fill an exact A.6.1 result position or another declared participant position for the call work. If exact work and change facts first constitute the trace and that identity-inception claim matters, use a current direct entity-identity-inception governor only if one actually exists; otherwise retain the exact missing-governor blocker. If the trace itself carries claims about that work, it may also be identified as another episteme through the C.2.1 triple. An answer entity identified at an exact declared result position and a separately identified evaluation-report episteme can have different kinds and EntitiesOfConcern; neither is a generic work result by wording alone. Tool availability, a successful call, or a high evaluation score establishes neither claim truth nor empirical grounding. When tool integration changes or degrades reasoning, locate the change in the enacted method, inference work, call work, operation binding, representation use, evidence relation, or empirical-grounding occurrence. Reidentify an episteme only when its claim content, EntityOfConcern, or effective reference scheme changed.

### C.2.1:10 - Bias-Annotation  *(informative)*

C.2.1 deliberately favors explicit aboutness and interpretation because claims without an exact EntityOfConcern and effective reference scheme are difficult to compare or test. The mitigation is the `A.6.REL` minimum-current-object rule: ordinary use adds another object only when the receiving use depends on it and states that object's direct relation to an already recoverable object.

The pattern also resists representation bias. Formal calculi, diagrams, learned representations, and interactive tools can materially change available reasoning operations, but their convenience or geometry cannot establish subject identity. C.29 and the selected transition pattern govern those differences.

Finally, the pattern has a claim-bearing-holon bias. Decodability alone does not make the decoded entity an episteme. The decoded entity is admitted as an episteme only when claim content, an exact EntityOfConcern, and an effective reference scheme are recoverable and together satisfy the constitution relation.

### C.2.1:11 - Conformance Checklist  *(normative)*

1. **Episteme identity.** Claim content, exact EntityOfConcern, and effective `U.ReferenceScheme` are recoverable, and the text states what changes each discriminator. A dependent episteme kind such as `U.MethodDescription` or `U.View` adds a governed membership judgment for the same individual, not another identity discriminator.
2. **Direct constitution.** `EpistemeConstitutionRelation` has its three identified participants, obtaining condition, and participant-determined occurrence identity.
3. **Declaration identity and Slot discipline.** Each of the three named relation declarations is first a C.2.1 episteme whose exact EntityOfConcern is its direct relation kind; the fixed `A.6.0` predicate gives that same individual `U.Signature` membership and `RelationSignature` is its relation-facing use. Its complete declaration carries the direct predicate, occurrence identity, applicability, exact A.6.5 SlotSpecs, and only actual dependencies and provided names. Signature-local SlotKinds never become participants, and a one-off assertion needs no signature or manifest.
4. **Classification discipline.** `A.1` governs recognition under an admitted holon kind, `C.3.2` governs local-kind membership, and `E.24.UK` governs public U-kind admission. A separately current classification assertion is a C.2.1 episteme about the exact candidate and neither creates that candidate nor changes the kind's admission.
5. **Empirical-grounding discipline.** `GroundingHolonSlot` occurs only inside `EpistemeEmpiricalGroundingRelationSignature`. Obtaining requires the exact current direct observation, intervention, measurement, or evaluation relation structure involving the grounding holon. One occurrence is reidentified from the episteme, grounding holon, and maximal continuous grounding interval; demonstrated loss followed by restoration yields another occurrence. Evidence availability or absence alone sets no grounding status and neither proves nor disproves a temporal gap: known obtaining or nonobtaining follows the direct structure, and only unknown status of that structure leaves a positive grounding assertion unresolved. Evidence use may support an assertion, but evidence storage, availability, or work-log loss neither makes nor unmakes grounding.
6. **Edition discipline.** `EpistemeEditionRelation` has exactly the earlier and later epistemes as participants and is acyclic in that direction. The identified edition work, exact source-to-revision use, enacted-method semantics, actual change facts, and any separately governed entity-identity-inception claim make the obtaining judgment inspectable without entering occurrence identity. If a required inception claim lacks a current direct governor, return the exact missing-governor blocker.
7. **View and neighboring-relation discipline.** C.2.1 owns episteme identity; `E.17.0` alone owns fixed E/P conformance and same-individual `U.View` membership; `DescriptionContext` resolves exactly one `viewpointRef`, selects no view, and remains separate from A.6.3 source-to-receiving construction. Several views remain a plurality. Recover an exact C.13 collection only when a receiving use depends on that plurality as a collection, and recover an A.22 structure only when the use additionally depends on their organization. Cross-view claims use their exact direct subject-relation governor or return an exact blocker naming the participants, required predicate and use, and missing governor. E.17 and E.24.PUB own publication, not view membership or correspondence.
8. **Description boundary.** The EntityOfConcern and any Description episteme about it remain distinct, including self-description and episteme-about-episteme cases.
9. **Specification use.** Specification force is admitted only when the `E.10.D2` conditions obtain: checkable claims, a preserved or updated DescriptionContext, and a named harness or validation relation. Naming and appearance do not grant it.
10. **Agency and work-result boundary.** Only systems perform authoring, evaluation, revision, publication, viewing, query, redrawing, and use work. `A.6.1` declares typed argument and result positions; for each exact current operation application, each application binding relates one exact entity to its declared argument or result position, and every bound entity retains its independently governed kind, identity, and any domain-result algebra. Identify actual change facts, the affected or newly constituted entity, and any separately governed entity-identity-inception claim. If the receiving claim requires inception and no current direct governor supplies it, return the exact missing-governor blocker. No morphism, heading, representation, form, bare A.6.1 `result`, generic work result, or universal production relation is inferred.
11. **Publication boundary.** Episteme, publication occurrence, publication form, view, and carrier keep separate identities. Plain `published episteme` names a contingent relation use, not another durable kind.
12. **Representation boundary.** Tuple components, graph elements, schema fields, and notation tokens remain representation elements. An explicit correspondence may relate one to an independently recovered object without identifying the two or changing the represented direct relation's participants.
13. **Transformation boundary.** A morphing, viewing, or retargeting declaration states which C.2.1 identity discriminators are preserved or changed and names the exact correspondence or retargeting relation used. Cross-context sense use additionally states the `F.9` Bridge direction, congruence, loss, and admitted use; the mathematical morphism performs no work.
14. **Recursive assurance.** Self-reference and meta-description do not form a minimal justification cycle; assurance terminates in independently governed evidence, observation, or formal derivation.
15. **Minimum current object.** Readable prose adds no object beyond the current use's dependency and states the direct relation to an already recoverable object.

### C.2.1:12 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Actual failure | Repair |
| --- | --- | --- |
| Filled-card ontology | A completed record is treated as what makes an episteme or relation exist. | Recover the C.2.1 identity first. Identify a filled card as an episteme only when its claim content, EntityOfConcern, and effective reference scheme are recoverable; identify its reusable layout, exact carrier, and publication occurrence separately under their direct patterns. |
| Manifest-created declaration | A manifest row, list, citation, identifier, or edition marker is treated as creating declaration identity, `U.Signature` membership, or a dependency. | Identify the declaration episteme through the C.2.1 triple, judge same-individual `U.Signature` membership under A.6.0, and expose a manifest only for actual dependencies or provided names. A readable one-off assertion stops without either. |
| Classification as admission relation | A candidate is said to acquire or lose holonhood when a governing FPF pattern or assertion changes. | Apply the `A.1` constructive criterion for an admitted holon kind; let `E.24.UK` govern only admission of that public kind; identify a separate C.2.1 assertion episteme when project review needs the classification claim. |
| Dependent kind as second identity | `U.MethodDescription`, `U.View`, or another dependent episteme kind is given an extra identity discriminator merely because its direct pattern supplies a membership condition. | Keep the C.2.1 identity of the same episteme individual. Apply the direct pattern only to judge dependent-kind membership; if work changes a C.2.1 discriminator, identify the resulting episteme through that changed discriminator. |
| Context identifier in episteme identity by habit | A surrounding project or model-use context identifier is treated as identifying every episteme used there. | Keep the shared C.2.1 identity context-independent; add claim scope, viewpoint, or bounded model-use structure only through the direct relation on which the current use depends. |
| Grounding by evidence presence | Stored evidence is treated as an automatic empirical-grounding relation. | Recover the direct observation, intervention, measurement, or evaluation relations involving the exact grounding holon and test continuity of `EpistemeEmpiricalGroundingRelation`. Evidence availability or absence alone sets no grounding status; known obtaining or nonobtaining follows the direct structure, and only unknown status of that structure leaves a positive grounding assertion unresolved. |
| Edition work as relation participant | Revision work is inserted into `EpistemeEditionRelation`, so two works appear to create two continuities between the same editions. | Keep earlier and later epistemes as the two participants; recover exact source-to-revision use, enacted-method semantics, actual change facts, any separately governed entity-identity-inception claim, evaluation, and evidence separately. If a required inception claim lacks a current direct governor, return the exact missing-governor blocker. |
| Edition by filename | `v2` or a later timestamp is taken as epistemic succession. | Recover the two episteme identities, then test edition continuity through identified revision work, exact source-to-revision use, enacted-method semantics, and actual change facts. If that test also requires an entity-identity-inception claim, use a current direct governor only when one actually exists; otherwise return the exact missing-governor blocker. |
| Published-episteme kind | Temporary participation in publication is treated as a second durable episteme kind. | Keep the episteme identity and state the exact publication occurrence; use Plain `published episteme` only for that contingent use. |
| View as formatting, generation, or publication | A filtered table, diagram, query result, or published face is called a view because of appearance, construction history, or carrier, and a heading or edge is treated as cross-view correspondence. | Identify the receiving episteme under C.2.1 and apply `E.17.0` conformance for `U.View` membership. Add A.6.3 only for an actual source-to-receiving construction. Apply the exact direct subject-relation governor to correspondence; if none is recoverable, return an exact blocker naming the participants, required predicate and use, and missing governor. |
| Mathematical identity leak | A tuple key or graph node identity becomes episteme identity. | Keep C.29 representation identity separate and use the C.2.1 identity triple. |

### C.2.1:13 - Consequences  *(informative)*

**Benefits.** Episteme identity becomes stable across carrier and publication changes. Description, empirical grounding, viewing, edition, and representation questions can be repaired locally because each has a direct relation. Self-description and multi-view use need no second ontology. The same pattern works for physical engineering, medicine, learning, formal work, and computational modeling.

**Costs.** A load-bearing episteme use has a recoverable exact EntityOfConcern and effective reference scheme rather than relying on a title or file. Empirical-grounding and edition claims depend on their own obtaining and identity evidence. Existing record-shaped schemas sometimes need to distinguish their fields from actual relation participants.

**Limits.** C.2.1 does not decide whether an epistemic claim is true, sufficient, current, or authoritative. It does not prescribe a file format, graph database, proof calculus, or publication layout. Those questions remain with evidence, evaluation, temporal, representation, and publication patterns.

### C.2.1:14 - Rationale

Adding empirical grounding, viewpoint, scope, edition, and publication to every identity would instead collapse distinct relations and make ordinary use needlessly heavy.

Separating the episteme from its constitution relation is equally important. The direct relation explains how the identity-bearing participants are organized. The episteme is the resulting holon with a whole-level capacity to carry interpretable claims. A relation declaration is first its own C.2.1 episteme; `A.6.0` independently recognizes that same individual as a `U.Signature`, and `RelationSignature` names its relation-facing use. Its claims declare the direct relation for typed reuse; an assertion claims that the relation obtains, and a publication occurrence makes a selected episteme edition available. None replaces another.

### C.2.1:14.1 - SoTA-Echoing

| Source and status | Adopted move | Rejected overread | Practical effect in C.2.1 |
| --- | --- | --- | --- |
| [Catarina Dutilh Novaes, *Formal Languages in Logic* (2012)](https://www.cambridge.org/core/books/formal-languages-in-logic/7D1DD805F7B3C70A0C32F2F6A66BE3DD), conceptual lineage | Treat a formal language as a cognitive tool whose notation and admissible operations affect reasoning. | A notation, calculus, or formal-language file does not thereby identify the episteme or its EntityOfConcern. | The semantic-triangle case keeps the effective reference scheme and C.29 representation operations explicit while episteme identity remains independently governed. |
| [Sybille Krämer, "Why notational iconicity is a form of operational iconicity" (2017)](https://benjamins.com/catalog/ill.15.17kra), diagrammatic-reasoning lineage | Preserve the operational consequences of spatial and material notation. | Visual arrangement does not make diagram elements actual relation participants and does not prove that a view preserves source claims. | The wiring-diagram and view cases use an explicit representation correspondence or viewing relation rather than relying on visual similarity. |
| [Lambros Malafouris, *People Are STRANGE* (2026)](https://mitpress.mit.edu/9780262553902/people-are-strange/), current continuation of Material Engagement Theory | Use changing boundaries under material engagement as pressure on grounding: when an engagement changes what can be inspected or inferred, FPF still identifies the exact holon in the current grounding occurrence. | A material setting, carrier, or tool is not automatically the episteme's EntityOfConcern or grounding holon. | The pump and learning cases name one exact grounding holon and the direct grounding relation structure instead of absorbing the surrounding setting into episteme identity. |
| [Florio and Linnebo, *Introduction to Constructional Ontology* (2024)](https://www.utwente.nl/en/eemcs/fois2024/resources/papers/florio-linnebo-introduction-to-constructional-ontology.pdf) and [Borgo and Righetti, *Towards Applied Constructional Ontology* (2025)](https://doi.org/10.3233/FAIA250480), current constructional-ontology line | Adapt the separation among accepted inputs, the construction by which a whole emerges, and the resulting identity rule as a stress discipline for episteme constitution. | `EpistemeConstitutionRelation` is not imported as a constructor object or work occurrence, and C.2.1 does not import a universal staged ontology. | Sections 4.1 and 4.2 make the exact claim graph, EntityOfConcern, reference scheme, and their constitutive organization explicit in the constitution test; a tuple, card, or carrier cannot substitute for that construction or its identity rule. |
| [Andrei Rodin, *Venus Homotopically* (2016)](https://philsci-archive.pitt.edu/12116/), constructive identity-grounding lineage | Adapt the use of observations, theoretical background, and a physically testable trajectory to make an identity judgment across different presentations inspectable. | Shared wording, one label, or one grounding referent does not by itself prove identical EntityOfConcern, episteme, or substitutable claim content. | The two-observation case in 9.6 separates the world-side identity assertion from both observation epistemes and keeps their C.2.1 identities independently testable. |
| [Chris Partridge, *BORO Ontology* (2025)](https://borosolutions.net/boro-ontology), bounded four-dimensional extensional comparator | Use extensional identity as a stress test when a grounding relation can cease and later recur: a demonstrated temporal gap distinguishes the occurrences. | C.2.1 does not import unrestricted composition, collapse work with participating systems, or attribute constructional input identity to BORO. | Section 4.3 uses the maximal continuous grounding interval as the recurrence discriminator, while evidence availability or absence alone neither proves nor disproves a temporal gap. |
| [W3C PROV-O Recommendation (2013)](https://www.w3.org/TR/prov-o/), stable provenance lineage | Keep an entity, the activity that uses or generates it, and revision or derivation relations distinct. | `wasRevisionOf` or generic derivation metadata alone does not establish FPF edition continuity, and the revision activity is not therefore a participant of the edition relation. | `EpistemeEditionRelation` keeps the earlier and later epistemes as its two participants; exact source-to-revision use, enacted-method semantics, change facts, and any needed separately governed entity-identity-inception claim make the obtaining judgment inspectable. A required inception claim without a current direct governor returns the exact missing-governor blocker. |
| [W3C RDF 1.2 Concepts, Candidate Recommendation Snapshot of 7 April 2026](https://www.w3.org/TR/2026/CR-rdf12-concepts-20260407/), current representation standard | Distinguish an asserted triple, an unasserted triple term, and a reifier used for statements about a proposition. | An RDF triple, reifier, graph edge, or annotation is not the direct relation occurrence merely by representation. | The relation-object boundary keeps assertion episteme, relation-occurrence description episteme, graph representation, and direct relation obtaining separate. |
| [Almeida, Guizzardi, Sales, and Fonseca, *gUFO: A Gentle Foundational Ontology for Semantic Web Knowledge Graphs* (March 2026)](https://arxiv.org/abs/2603.20948), current preprint | Use its typology and reification patterns for relational aspects as a current comparison case when deciding whether an explicit relation pattern is needed. | C.2.1 does not import a universal relator, situation, or graph-reifier ontology; each direct relation pattern governs its participants, obtaining condition, and occurrence-identity rule. | Constitution, grounding, and edition relations receive separate rules rather than one record-shaped reification scheme. |
| [Anthropic, *A global workspace in language models* (6 July 2026)](https://www.anthropic.com/research/global-workspace), current primary research summary with linked paper | Recognize that learned internal representations can causally mediate reasoning while remaining distinct from produced text. | A latent activation, probe label, or readable internal trace is not automatically a claim-bearing episteme. | Case 9.8 keeps the observed system-side activation phenomenon, its probe representation, decoded rendering, and any claim-bearing probe episteme distinct; C.2.1 admission still requires recoverable claim content, an exact EntityOfConcern, and an effective reference scheme. |
| [Cheng et al., *Teaching Thinking Models to Reason with Tools* (May 2026)](https://arxiv.org/abs/2605.06326), current preprint | Keep tool use, reasoning trajectories, evaluation, and their failure modes explicit because tool integration can change or degrade reasoning behavior. | Tool availability, a tool trace, or an evaluation harness does not by itself establish claim truth, grounding, or episteme identity. | Case 9.8 separates enacted inference and call work, the exact work-to-trace relation or A.6.1 binding current in that case, answer and evaluation epistemes, representation use, evidence, and empirical grounding; a changed tool regime reopens only the exact changed objects and relations. |

These sources discipline different parts of the same working problem; they do not jointly define `U.Episteme`. Constructional ontology disciplines the separation among accepted constituents, constitutive organization, and resulting identity without turning the relation into work. Rodin disciplines evidence-backed identity across different observations, while the bounded BORO comparison stresses temporal recurrence without supplying FPF construction rules. Formal-language and material-engagement work explains why representation and grounding matter. RDF 1.2 remains a representation standard, while gUFO remains an ontology comparator for relational aspects; neither graph terms nor reifiers establish the direct relation occurrence. PROV-O motivates keeping the earlier episteme, revision work, exact source-to-revision use, actual change or local inception claim, and later episteme distinct while C.2.1 keeps only the two epistemes as participants of the edition relation. Current learned-representation and tool-integration research makes the same separations necessary for computational epistemes. In every case, C.2.1 retains the minimum-current-object rule: add only the object and direct relation needed by the receiving use, without collapsing either into the episteme or its carrier.

### C.2.1:15 - Relations  *(overview)*

- **Builds on:** `A.1` for holon recognition, `A.6.REL` for direct relation occurrences, `A.6.0` for independent same-individual `U.Signature` membership and relation-facing `RelationSignature` use, `A.6.5` for declaration-local SlotSpecs and participant designations, `A.7` for entity-description distinction, and `C.29` for mathematical representation.
- **Coordinates with:** `A.3.2` for `U.MethodDescription` membership without a second episteme identity; `C.3.2` for local-kind membership judgments; `E.24.UK` for ontology-level U-kind admission; `E.10.D2` for Description and specification-use discipline, including selection that creates neither conformance nor membership; `A.6.1` for typed operation positions and exact current application bindings; `A.6.2`, `A.6.3`, and `A.6.4` for morphing, source-to-receiving viewing construction, and retargeting; `A.6.3.RT` for representation transitions; `E.17.0` for fixed E/P conformance and `U.View` membership; `C.13` and `A.22` for separately current multi-view collections and structures; the exact direct subject-relation pattern, or an exact missing-relation blocker naming the participants, required predicate and use, and missing governor; `F.9` when transformations cross context-local senses; `E.13` when a visible representation-quality proxy is used as practical epistemic value; `A.2.6` for claim scope; `A.1.1` for bounded model-use structure; `A.10` and `B.3` for evidence and assurance; `A.14` only when a phase or separately selected edition collection is current; `C.2.P`, `A.3.1`, and `A.3.4` when exact source use, revision method, or actual change is current in edition-continuity evaluation; a current direct entity-identity-inception governor only when that local claim is required and such a governor actually exists, with the exact missing-governor blocker otherwise; `E.17` for multi-view publication forms and uses; `E.24.PUB` for publication occurrences, forms, and carriers; and `G.11` for currentness.
- **Used by:** every pattern that identifies, describes, classifies through an explicit assertion, compares, grounds, transforms, views, publishes, or refers to a `U.Episteme`.

### C.2.1:End

