## E.24.PUB - Ontic Description and Publication Discipline

> **Type:** Part E FPF authoring discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### E.24.PUB:0 - Use This When

Use this pattern when an ontic or another entity is encountered through a card, table, diagram, file, pattern host, dashboard, or similar published expression and the current work depends on knowing what was described, what was made available, and what merely carries the expression.

**Primary working reader.** A practitioner or FPF author deciding whether a visible thing is a claim-bearing episteme, a `U.View`, a publication form, a C.29 representation, a `U.PresentationCarrier`, or evidence of one publication occurrence.

**First useful move.** Name the exact next `U.Work` for which the publication is expected to make claims available. Then say, in one sentence, which exact episteme edition is available, to which declared audience, for which bounded use, in which publication form, and on which presentation carrier. If that Work is choice work, keep its resulting C.11 `ChoiceResult` separate: publication establishes neither the Work nor the result, and the result is neither the Work nor a publication participant. Only when the Work actually uses a published claim, name the exact claim-bearing episteme and its direct route. For a premise, reference, other participant, or work-to-referent use, name the exact declared predicate, participant order, and actual values. For a declared operation argument, name the identified A.6.1 application and its exact declaration-local binding. If neither route exists, stop at publication availability or return the applicable A.15.1 `missing-governor` result. Open the heavier publication-relation declarations only when that next Work depends on exact availability, the declared use boundary, or publication-occurrence identity.

**What goes wrong if missed.** A visible layout is treated as the described subject, a file is treated as the claims it carries, a diagram is treated as a view merely because it is graphical, or a currently available episteme is turned into a durable `U.EpistemePublication` kind. The receiving work then cannot tell which object changed when claims, layout, carrier, audience, or use changes.

**What this buys.** The user can change a claim, view, form, carrier, audience, or declared bounded use without silently changing all the others. A publication can be inspected and repaired while the subject pattern remains centered on its subject.

**Not this pattern when.**

- Use `C.2.1` when the question is the identity or content of the episteme itself.
- Use `E.17.0` when the question is whether an exact episteme conforms to an exact viewpoint episteme and therefore has `U.View` membership. Use `A.6.3` separately when source-to-receiving viewing construction is current.
- Use `C.29` when representation elements and the operations admitted by a representation are current.
- Use `E.24.CD`, then `E.24`, when a durable ontic is still being considered.
- Use `E.24.UK` when a public `U.*` kind or dependent-kind disposition is unsettled.
- Use the subject pattern directly when publication does not affect the named receiving `U.Work`.

### E.24.PUB:1 - Problem Frame

Ontics and other entities are usually encountered through epistemes and physical or digital carriers. One completed inspection card can carry claims and therefore be a `U.Episteme`; its reusable arrangement can be used as a publication form; selected graphical elements can participate in a C.29 representation; a file, screen, sheet, or volume can be a `U.PresentationCarrier`; and one publication occurrence can make the selected card-episteme edition available to a declared audience for a bounded use.

Those are connected uses, not one presentation-side kind. E.24.PUB governs the publication relation and the two supporting relations needed to inspect that use. It keeps the described subject, description episteme, `U.View`, representation, publication form, carrier, and publication occurrence distinct without requiring every ordinary sentence to repeat the full stack.

Plain `published episteme` names an episteme while it participates as the selected edition in a current publication occurrence. It is a contingent qualification, not a durable U-kind and not a second identity beside `U.Episteme`.

Here a publication occurrence is an occurrence of `EpistemePublicationRelation`: an availability relation that can endure. It is not the instantaneous rendering, printing, uploading, or access-control work that may establish or restore that availability.

### E.24.PUB:2 - Problem

The practical problem is change localization. When a reader sees only “the diagram was updated” or “the model was published”, five materially different changes are hidden:

1. the selected episteme edition may have changed because its claim content, EntityOfConcern, or effective reference scheme changed;
2. another episteme edition may have been constructed, or the exact episteme may conform to a different viewpoint edition;
3. the publication form or C.29 representation may have changed while the claims stayed the same;
4. the presentation carrier or its availability may have changed;
5. the declared audience or bounded use may have changed while the same edition, form, and carrier remained.

Without the distinction, a receiving work occurrence cannot identify the smallest object or relation to inspect, revise, republish, or stop relying on.

### E.24.PUB:3 - Forces

| Force | Tension |
| --- | --- |
| Readable first use vs exact relation identity | Most users need one sentence; contested availability needs exact participants, obtaining, and occurrence identity. |
| One encountered thing vs several governed uses | A card or diagram can participate in several relations, but visible shape decides none of their kinds. |
| Stable episteme vs changing publication | The same episteme edition may be republished through another form or carrier, while a changed claim discriminator identifies another episteme. |
| Audience reach vs actual use | Making an edition available does not prove that any system read it, relied on it, or performed work from it. |
| Subject-first explanation vs semio-bias | Publication distinctions protect reasoning about the subject; they should not displace the subject from its governing pattern. |

### E.24.PUB:4 - Solution

Start with this readable publication statement:

> Publication occurrence `<P>` makes episteme edition `<E>` available to the audience identified by `<A>` for the use bounded by `<U>`, through publication form `<F>` borne by presentation carrier `<C>`.

The sentence names the five participant meanings without asking the user to fill a record. If it supplies the publication distinction needed by the named receiving `U.Work`, stop. If availability, identity, or a change is disputed, recover the three direct relations below.

#### E.24.PUB:4.1 - Identify the publication occurrence

`EpistemePublicationRelation` is the direct relation kind whose occurrence makes one selected episteme edition available to a declared audience for a declared bounded use.

Its actual participants are:

| Participant meaning | Admitted value | What the value supplies |
| --- | --- | --- |
| selected episteme edition | one exact `U.Episteme` identified under `C.2.1` | the claims made available |
| audience declaration | one `U.Episteme` whose claims identify the intended receiving entities or a C.3-governed local kind and its membership criterion | who is included; a reader label alone is insufficient when the boundary matters |
| bounded-use declaration | one `U.Episteme` whose claims state the operations or decisions supported, the conditions of that use, and the excluded stronger use | what availability is for; actual reliance remains another relation |
| publication form | one exact `U.Entity` used as the selected arrangement, notation, or rendering convention that expresses the edition for the bounded use | how the edition is expressed; visible shape alone does not establish this use |
| presentation carrier | one exact `U.PresentationCarrier` | what physically or digitally bears the selected form |

The use of common `U.Entity` for the publication-form participant does not admit a universal publication-form U-kind. `Publication form` is a relation-defined participant meaning here: the exact entity keeps the more specific kind and identity supplied by its direct pattern, and it fills `PublicationFormSlot` only while `PublicationFormExpressionRelation` obtains for the selected edition and bounded use. This is one predicate over a real common kind, not a prose union of cards, tables, diagrams, and files. E.8 governs FPF pattern form; E.17 governs multi-view publication forms and faces; a domain publication pattern may govern another form.

The reusable declaration is:

```text
EpistemePublicationRelationSignature:
  RelationKind: EpistemePublicationRelation
  SlotSpecs:
    SelectedEpistemeEditionSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    AudienceDeclarationSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    BoundedUseDeclarationSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    PublicationFormSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
    PresentationCarrierSlot: ValueKind=U.PresentationCarrier, refMode=U.EntityRef, Required
```

These SlotKinds name participant meanings only inside this `RelationSignature`. They do not create five new U-kinds, and a card field with a similar label does not become one of these SlotSpecs.

The audience-declaration episteme identifies the audience criterion; it is not the audience and does not prove access by any particular system. A concrete system's access, reading, reliance, or later work is another direct relation or work occurrence. This lets one publication be available to every entity satisfying a stable criterion without inventing `U.Audience` or treating a changing set of readers as changing participants of the same publication occurrence.

`EpistemePublicationRelation` obtains while all of the following are true:

1. `PublicationFormExpressionRelation` relates the selected edition, publication form, and bounded-use declaration;
2. `PublicationFormBearingRelation` relates the exact carrier and publication form;
3. entities admitted by the audience declaration can obtain the expressed edition from that carrier under the conditions stated by the bounded-use declaration;
4. the selected edition, declarations, form, and carrier remain the identified participants of this occurrence.

One occurrence is reidentified by those five fixed participants and their maximal continuous interval of availability. Changing any participant yields another publication occurrence. Demonstrated loss of availability followed by restoration yields a later occurrence. Missing or stale evidence leaves current obtaining unresolved; it does not prove a gap.

Publication work remains separate. Rendering, printing, uploading, indexing, or granting access can be dated `U.Work` that establishes, restores, changes, or fails to establish the publication relation. The work and its result do not become publication-relation participants.

#### E.24.PUB:4.2 - Recover expression and bearing only when needed

`PublicationFormExpressionRelation` relates one selected episteme edition, one exact publication form, and one bounded-use declaration. It obtains when the form expresses enough of that edition, under its effective reference scheme, for the declared use. One occurrence is reidentified by those three fixed participants and their maximal continuous interval of predicate truth. Omission, coarsening, changed notation, or changed admitted operations can end this relation even while the carrier remains unchanged. `A.6.3`, `C.29`, or `E.17` governs the more specific preservation, loss, view, or representation claim when that claim is current.

`PublicationFormBearingRelation` relates one exact `U.PresentationCarrier` and one exact publication form. It obtains while that carrier bears or renders that form as the same recoverable form. One occurrence is reidentified by the two fixed participants and their maximal continuous interval of bearing. Changing a filename or storage address does not by itself settle carrier identity; apply the carrier's direct identity and currentness pattern.

Their reusable declarations are:

```text
PublicationFormExpressionRelationSignature:
  RelationKind: PublicationFormExpressionRelation
  SlotSpecs:
    ExpressedEpistemeEditionSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    PublicationFormSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
    BoundedUseDeclarationSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required

PublicationFormBearingRelationSignature:
  RelationKind: PublicationFormBearingRelation
  SlotSpecs:
    PresentationCarrierSlot: ValueKind=U.PresentationCarrier, refMode=U.EntityRef, Required
    BornePublicationFormSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
```

These supporting relations prevent two shortcuts. A form does not make itself available, and a carrier does not express claims merely by storing bytes, ink, or another physical state. The publication occurrence depends on both relations but remains a distinct availability occurrence.

#### E.24.PUB:4.3 - Use progressive explicitness

Use the smallest statement that supports the current work:

1. **Ordinary use:** name the selected episteme edition, audience, bounded use, form, and carrier in one sentence.
2. **Changed-object use:** say which one of those objects changed and which relation must be re-evaluated.
3. **Contested availability:** state the `EpistemePublicationRelation` participants, obtaining evidence, and occurrence identity.
4. **Contested expression:** open `PublicationFormExpressionRelation` and the exact view, representation, preservation, or loss pattern.
5. **Contested carrier availability:** open `PublicationFormBearingRelation` plus the direct carrier-currentness or access pattern.

Do not materialize all five levels as a standing publication card. Stop as soon as the named receiving `U.Work` can distinguish the operative object and relation.

#### E.24.PUB:4.4 - Classify the encountered form by current use

Ask one question at a time:

| Current question | Governed object or relation |
| --- | --- |
| Does the filled card, diagram, or record carry identifiable claims about an EntityOfConcern under an effective reference scheme? | a `U.Episteme` under `C.2.1` |
| Does `EpistemeViewpointConformanceRelation(E,P)` obtain for that episteme E and at least one exact viewpoint episteme P? | the same E has dependent-kind membership as `U.View` under `E.17.0`; any A.6.3 construction remains a separate optional relation |
| Is an arrangement, notation, or rendering convention selected to express the edition for this bounded use? | the publication-form participant of `PublicationFormExpressionRelation` |
| Do selected elements correspond to independently recovered objects and change the admitted modeling or reasoning operations? | a C.29 representation and its correspondence |
| Does a physical or digital entity bear the form? | a `U.PresentationCarrier` in `PublicationFormBearingRelation` |
| Is the selected edition available to the declared audience for the declared use through that form and carrier? | one `EpistemePublicationRelation` occurrence |

The answers can be jointly positive because they concern different objects or relations. They do not follow from the words `card`, `record`, `table`, `schema`, `diagram`, `view`, `file`, or `publication` alone.

#### E.24.PUB:4.5 - Keep direct verbs with their relations

- an episteme carries claims and designations;
- a `U.View` is the same episteme individual for which E.17.0 conformance to at least one exact viewpoint episteme obtains;
- a publication form expresses a selected episteme edition for a bounded use;
- a C.29 representation stands in a declared correspondence to independently recovered objects;
- a presentation carrier bears a publication form;
- a publication occurrence makes one selected episteme edition available;
- a system performs publication work and may later access or rely on the published episteme through separately governed relations.

A designator designates and a governed reference resolves to a referent. Neither operation publishes, bears, represents, or makes the subject-side predicate obtain.

#### E.24.PUB:4.6 - Keep subject patterns subject-first

In a pattern about an ontic, structure, architecture, characteristic space, method, or another subject, explain the subject's identity, relations, practical problem, and solution before publication details. Add E.24.PUB only when the named work depends on distinguishing the description, selected edition, form, carrier, audience, or bounded use.

When the EntityOfConcern is itself a description episteme, the same rule applies one level up. The description stays the subject; publication of that description is a neighboring relation.

### E.24.PUB:5 - Archetypal Grounding

#### E.24.PUB:5.1 - Maintenance inspection card

A completed pump-inspection card states measured clearances and identified defects about Pump #37 under the maintenance reference scheme. The completed card is a claim-bearing `U.Episteme`. Its reusable arrangement is the inspection-card publication form. The PDF file is a `U.PresentationCarrier`. One publication occurrence makes edition 4 of the card episteme available to the maintenance-planning team for planning the next repair.

Changing the PDF filename changes neither the card episteme nor necessarily the carrier identity. Correcting a measured clearance changes the episteme edition. Replacing the card layout changes the form. Making the same edition available to a supplier for quotation creates another publication occurrence because the audience or bounded use changed.

#### E.24.PUB:5.2 - Architecture diagram

An architecture diagram can carry claims about selected structures of one holon and therefore be an architecture-description episteme. When that exact episteme conforms to one exact architectural viewpoint episteme under E.17.0, the same individual is a `U.View`; direct authoring and A.6.3 construction are independent construction routes. Its graphical notation can be the publication form, selected nodes and edges can participate in a C.29 representation, and a screen or sheet can be the presentation carrier.

The diagram does not become the architecture by being published. `C.30` governs the `ArchitectureOf@Context` claim and `A.22` governs selected `U.Structure` values. E.24.PUB lets the architect locate a publication defect without replacing the architectural question with a discussion of diagrams.

#### E.24.PUB:5.3 - Clinical procedure edition

A hospital procedure description is an episteme about a method. A wall poster expresses a selected edition for quick pre-procedure orientation; the laminated sheet is the carrier. A separate controlled publication makes the same edition available to clinicians for authoritative procedure enactment. The two publication occurrences differ in bounded use even if the words are identical. Neither publication proves that a clinician read the procedure or performed work according to it; those are access, reliance, role-assignment, method, and work claims under their direct patterns.

#### E.24.PUB:5.4 - FPF pattern host

An E.24 pattern host can be a publication form expressing an ontic-description episteme about `U.Ontic`. The repository file is a presentation carrier. A selected edition becomes a published episteme only while an exact publication occurrence makes it available to the declared FPF audience and use. The host layout does not create `U.Ontic`, and changing the carrier does not by itself change the ontic-description episteme.

#### E.24.PUB:5.5 - Training availability and later choice work

One instruction edition is available to a training group for studying a method. That `EpistemePublicationRelation` occurrence establishes availability to the declared audience for that bounded use; it establishes neither that anyone read the instruction nor that adjustment, inspection, acceptance, or release work occurred. The same availability alone does not support an acceptance commission's choice about releasing one named lot.

If the commission later performs exact choice `U.Work` under A.15.1 and applies C.11, name that Work and the resulting C.11 `ChoiceResult` separately. When an instruction claim actually participates in that Work, name the exact claim-bearing episteme and its direct route. For a premise, reference, other participant, or work-to-referent use, name the exact declared predicate, participant order, and actual values. For a declared operation argument, name the identified A.6.1 application and its exact declaration-local binding. If neither route exists, stop at publication availability or return the applicable A.15.1 `missing-governor` result instead of asserting actual use. The `ChoiceResult` is neither the choice Work, the bounded-use declaration, nor a participant of the publication occurrence.

### E.24.PUB:6 - Bias Annotation

Lenses tested: **Onto**, **Epist**, **Semio**, **Arch**, **Prag**, **Did**.

- **Onto:** direct relation occurrences and their actual participants remain primary; visible forms do not decide kinds.
- **Epist:** the selected edition, audience declaration, and bounded-use declaration retain C.2.1 identities.
- **Semio:** designation, expression, representation, bearing, and publication availability use different predicates.
- **Arch:** subject patterns keep their subject; E.24.PUB owns only the neighboring publication architecture.
- **Prag:** progressive explicitness stops at the first statement sufficient for the named receiving `U.Work`.
- **Did:** one readable sentence and heterogeneous cases precede the RelationSignature detail.

### E.24.PUB:7 - Conformance Checklist

| Check | Observable conformance condition |
| --- | --- |
| `CC-E24PUB-1` | The named receiving `U.Work` and the publication use it depends on are explicit. A claimed actual use names either the exact declared predicate, participant order, and actual values for a premise, reference, other participant, or work-to-referent use, or the identified A.6.1 application and exact declaration-local binding for a declared operation argument; otherwise the text stops at publication availability or returns the applicable A.15.1 `missing-governor` result. Choice work keeps its C.11 `ChoiceResult` separate from the Work and publication participants. |
| `CC-E24PUB-2` | The selected episteme edition, audience declaration, bounded-use declaration, publication form, and presentation carrier are distinguishable. |
| `CC-E24PUB-3` | `EpistemePublicationRelation` has the five exact participant meanings, the availability predicate, and the maximal-continuous-occurrence identity rule stated in section 4.1. |
| `CC-E24PUB-4` | `PublicationFormExpressionRelation` and `PublicationFormBearingRelation` are recoverable when expression or carrier availability is load-bearing. |
| `CC-E24PUB-5` | Plain `published episteme` is used only for contingent participation; `U.EpistemePublication` is not used as a durable kind. |
| `CC-E24PUB-6` | A `U.View` remains a same-individual dependent specialization of `U.Episteme` under an obtaining E.17.0 conformance relation; graphical appearance and A.6.3 construction alone supply no membership. |
| `CC-E24PUB-7` | C.29 representation elements and correspondence remain distinct from the publication form and direct subject-side objects. |
| `CC-E24PUB-8` | Publication work, actual access, reliance, evidence, decision, and performed work remain under their direct patterns. |
| `CC-E24PUB-9` | A changed edition, form, carrier, audience, or bounded use leads to the smallest affected object or relation rather than a whole-stack rewrite. |
| `CC-E24PUB-10` | Ordinary use stops at the readable sentence when no receiving work needs fuller relation detail. |

### E.24.PUB:8 - Common Misuses and Repairs

| Misuse | What actually failed | Repair move |
| --- | --- | --- |
| File equals episteme | Carrier continuity is used as claim-content identity. | Recover the C.2.1 episteme identity and the carrier's direct identity separately. |
| Diagram equals view | Graphical form or construction history is used as the `U.View` membership criterion. | Recover exact candidate episteme E, exact viewpoint episteme P, and E.17.0 conformance; keep any A.6.3 construction, selected use, form, and representation separate. |
| Publication equals expression | The form or rendered expression is treated as the publication occurrence. | Name the five `EpistemePublicationRelation` participants and test availability. |
| Available equals used | Publication is treated as proof of reading, reliance, decision, or work. | Open the exact access, reliance, decision, method, or work relation only when that stronger claim is current. |
| Republished equals revised | A new carrier or form is treated as another episteme edition. | Apply C.2.1 identity; another edition exists only when a discriminator changes. |
| Published-episteme kind | Temporary availability becomes a durable U-kind. | Keep `U.Episteme`; use Plain `published episteme` plus the exact publication occurrence. |
| Warning pile-up | A subject pattern lists every publication-side object before explaining its subject. | Keep the subject first and add only the distinction on which the named work depends. |

### E.24.PUB:9 - Consequences

The main gain is local repair. A stale carrier can be replaced without pretending that the claims changed. A revised claim can create another episteme edition without pretending that the audience or form changed. A narrower audience or use can create another publication occurrence while preserving the edition.

The cost is that load-bearing publication claims need five identified participants and two supporting relations. Progressive explicitness contains that cost: ordinary users state one sentence; only disputed availability, expression, or bearing opens the complete relation detail.

### E.24.PUB:10 - Rationale

Publication does not change an episteme into a nested publication object. It is a real availability relation supported by an expression relation and a bearing relation. That architecture explains why one encountered card, diagram, or file can matter in several ways without admitting one umbrella presentation kind.

The split also preserves agency. A system can perform work that renders, uploads, prints, indexes, withdraws, or replaces a carrier. The resulting publication relation may then obtain for a long interval with no continuing publication work. Conversely, publication work can fail while no publication occurrence begins. Treating enduring availability separately from the work that establishes it makes both claims inspectable.

### E.24.PUB:11 - SoTA-Echoing

| Source family | Decision-changing lesson | Adoption in this pattern | Practical implication |
| --- | --- | --- | --- |
| Modular ontology design patterns, including [Shimizu and Hitzler 2024](https://arxiv.org/abs/2411.09601) and [Eells, Dave, Hitzler, and Shimizu 2024](https://arxiv.org/abs/2402.18715) | Reusable ontology structure and the documentation or form through which it is encountered are different governed objects. | Separate the subject ontic, its description episteme, and the publication relations instead of making a reusable form the ontology. | In the inspection-card case, a layout repair does not force a pump-ontology repair. |
| [Norouzi, Hertling, Waitelonis, and Sack 2025](https://arxiv.org/abs/2509.23776) | Process-like forms can carry implicit ontology that domain experts need to recover explicitly. | Classify the claims and relations carried by a card or workflow-shaped expression before assigning publication use. | A workflow diagram can reveal an ontic candidate without becoming that ontic by notation. |
| [Nayyeri et al. 2025](https://arxiv.org/abs/2506.01232), and [Oyewale and Soru 2026](https://arxiv.org/abs/2602.01276) | Schemas and knowledge-graph pipelines help recover structure but also encourage schema or serialization overread. | Keep filled claim objects, reusable forms, C.29 representations, carriers, and publication occurrences distinct. | A table migration can change representation or carrier while preserving the published episteme edition. |
| OWL, SKOS, RDF, and triple-store practice | Labels, axioms, serializations, documents, and queries have different functions even when one tool exposes them together. | Use this lineage as an expression and implementation stress test, not as authority to identify ontology with serialization. | Tool export does not settle the kind of the exported subject or the truth of its claims. |
| FPF `C.2.1`, `A.6.REL`, `A.6.3`, `C.29`, `E.17`, and `E.24.UK` | Current FPF already separates episteme identity, direct relation identity, view membership, representation, publication use, and U-kind admission. | `E.24.PUB` coordinates those owners through one publication relation and two supporting relations; it does not duplicate their identity rules. | The architecture diagram case can be repaired at the exact changed relation without reopening architecture ontology. |

Smallest currentness trigger: reopen this source use when a newer ontology-publication or knowledge-representation line changes the distinction among claim-bearing episteme, view, publication form, representation, carrier, and availability relation. A new file format or storage tool alone does not trigger reopening.

### E.24.PUB:12 - Relations

- **Builds on:** `A.6.REL` for direct obtaining and occurrence identity, `C.2.1` for the selected edition and declaration epistemes, and `E.24` for ontic-description boundaries.
- **Coordinates with:** `E.17.0` for `U.View` membership and `E.17` for multi-view publication; `A.6.3` for optional viewing construction; `C.29` for representation and admitted operations; `E.8` for FPF pattern publication form; and the direct carrier-currentness or access pattern when carrier availability is current.
- **Coordinates with:** `E.24.CD` for candidate detection and `E.24.UK` for public U-kind and dependent-kind settlement. `U.EpistemePublication` is rejected there; this pattern uses Plain `published episteme` for contingent participation.
- **Used by:** subject patterns only when a named receiving `U.Work` depends on distinguishing the subject, description episteme, selected edition, view, representation, publication form, carrier, audience, bounded use, or publication occurrence.

### E.24.PUB:End

