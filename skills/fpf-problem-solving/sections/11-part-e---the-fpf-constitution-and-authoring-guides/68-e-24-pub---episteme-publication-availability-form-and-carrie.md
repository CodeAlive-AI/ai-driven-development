## E.24.PUB - Episteme Publication: Availability, Form and Carrier

> **Type:** Part E FPF authoring discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### E.24.PUB:0 - Use This When

Use this pattern when an ontic or another entity is encountered through a card, table, diagram, file, pattern host, dashboard, or similar published expression and the current work depends on knowing what was described, what was made available, and what merely carries the expression.

**Primary working reader.** A practitioner or FPF author distinguishing a claim-bearing episteme, a `U.View`, its expression, a reusable publication form, a carrier or an exact publication occurrence. Open representation methods when the expression also supports reasoning through a correspondence to its subject.

**First useful move.** Put the intended receiving use in the bounded-use declaration itself. Then say which episteme is available, to which declared audience, for which bounded use, through which expression and carrier. Name a reusable form when its constraints matter. Cite a separate plan, decision question or `U.WorkPlan` only when it independently exists and changes the publication claim. Distinguish availability from a claim of actual access or use. Open fuller relation detail when needed to resolve disputed availability, its boundary or publication-occurrence identity.

**What goes wrong if missed.** A visible layout is treated as the described subject, a file is treated as the claims it carries, a diagram is treated as a view merely because it is graphical, or publication availability alone is used to admit a durable `U.EpistemePublication` kind. The receiving work then cannot tell which object changed when claims, layout, carrier, audience, or use changes.

**What this buys.** The user can change a claim, view, form, carrier, audience, or declared bounded use without silently changing all the others. A publication can be inspected and repaired while the subject pattern remains centered on its subject.

**Not this pattern when.**

- Use `C.2.1` when the question is the identity or content of the episteme itself.
- Use `E.17.0` when the question is whether an exact episteme conforms to an exact viewpoint episteme and therefore has `U.View` membership. Use `A.6.3` separately when source-to-receiving viewing construction is current.
- Use `A.6.3.RT` and `A.6.3.RT.OE` to construct or change an expression and recover its correspondence; use `C.29` when a mathematical lens and its inference or transfer conditions are current.
- Use `E.24.CD`, then `E.24`, when a durable ontic is still being considered.
- Use `E.24.UK` when a public `U.*` kind or dependent-kind disposition is unsettled.
- Use the subject pattern directly when publication does not affect the receiving use.

### E.24.PUB:1 - Problem Frame

Ontics and other entities are usually encountered through expressions of epistemes and physical or digital carriers. In a completed inspection card, the claims about the inspected subject can constitute a `U.Episteme`; the particular signs express those claims; reusable arrangement rules supply a publication form; and a file or sheet bears the expression. A publication occurrence makes the selected episteme available through that expression and carrier to a declared audience for a bounded use.

These relations connect separately identified objects. E.24.PUB defines exact publication through expression and bearing, and reusable-form conformance when a form is selected. It also supplies form-mediated claims and broader availability for uses that do not require one fixed expression. Ordinary publication can be stated in one sentence.

Plain `published episteme` names an episteme while it participates as the selected edition in a current publication occurrence. C.2.1 continues to govern that episteme's identity. If the receiving use needs classification by publication participation, use C.3.2 with its declared criterion and slice. E.24.UK:5.0 rejects the additional public kind `U.EpistemePublication` for the availability-only use; a different classification need follows its admission tree.

Here a publication occurrence is an occurrence of `EpistemePublicationRelation`: an availability relation that can endure. It is not the instantaneous rendering, printing, uploading, or access-control work that may establish or restore that availability.

### E.24.PUB:2 - Problem

The practical problem is change localization. When a reader sees only “the diagram was updated” or “the model was published”, five materially different changes are hidden:

1. the selected episteme edition may have changed because its claim content, EntityOfConcern, or effective reference scheme changed;
2. another episteme edition may have been constructed, or the exact episteme may conform to a different viewpoint edition;
3. the expression, reusable form or representation correspondence may have changed while the claims stayed the same;
4. the presentation carrier or its availability may have changed;
5. the declared audience or bounded use may have changed while the same episteme, expression and carrier remained.

Without the distinction, the receiving use cannot identify the smallest object or relation to inspect, revise, republish, or stop relying on.

### E.24.PUB:3 - Forces

| Force | Tension |
| --- | --- |
| Readable first use vs exact relation identity | Most users need one sentence; contested availability needs exact participants, obtaining, and occurrence identity. |
| One encountered thing vs several governed uses | A card or diagram can participate in several relations, but visible shape decides none of their kinds. |
| Stable episteme vs changing publication | The same episteme edition may be republished through another form or carrier, while a changed claim discriminator identifies another episteme. |
| Audience reach vs actual use | Making an edition available does not prove that any system read it, relied on it, or performed work from it. |
| Subject-first explanation vs semio-bias | Publication distinctions protect reasoning about the subject; they should not displace the subject from its subject pattern. |

### E.24.PUB:4 - Solution

Start with this readable publication statement:

> Publication occurrence `<P>` makes episteme `<E>` available to the audience identified by `<A>` for the use bounded by `<U>`, through expression `<X>` recoverable from carrier `<C>`.

The sentence names the five participant meanings without asking the user to fill a record. If it supplies the distinction needed by the receiving use, stop. When the selected expression follows reusable form F and that conformance matters, name F separately. For disputed availability, identity or change, recover the predicates below.

#### E.24.PUB:4.1 - Identify the publication occurrence

`EpistemePublicationRelation` is the direct relation kind whose occurrence makes one selected episteme edition available to a declared audience for a declared bounded use.

Its actual participants are:

| Participant meaning | Admitted value | What the value supplies |
| --- | --- | --- |
| selected episteme edition | one exact `U.Episteme` identified under `C.2.1` | the claims made available |
| audience declaration | one `U.Episteme` whose claims identify the intended receiving entities or a C.3-governed local kind and its membership criterion | who is included; a reader label alone is insufficient when the boundary matters |
| bounded-use declaration | one `U.Episteme` whose claims state the operations or decisions supported, the conditions of that use, and any stronger-use boundary needed to interpret those claims | what availability is for; actual reliance remains another relation |
| publication expression | one independently identified `U.Entity`, X, under its expression domain's formation and equality rules | the particular sign construction from which the required claims can be recovered |
| presentation carrier | one independently identified `U.Entity`, C, under its physical or digital domain's identity rule | the entity whose actual state or realization provides that exact expression |

The `U.Entity` ranges leave X, F and C with their independently established domain identities. The positive predicates below determine expression, conformance and bearing. E.8 supplies FPF pattern-form rules, E.17 selects multi-view publication forms, and a domain publication pattern can supply another form.

**Obtain X with an identity that answers the actual comparison.** X is an independently identified sign construction: specified elements organized under the formation and equality rules of an expression domain. The domain tells a receiver which differences change that construction. A construction can be compared before anyone establishes which episteme it expresses. Two useful domains are:

- An ordered Unicode text has the declared codepoint sequence as its value. Changing a codepoint or its position changes X. Encoding the same sequence in UTF-8 or UTF-16 can preserve X while changing the stored bytes. Any normalization of line endings or Unicode variants must be part of the selected domain's equality or its decoding rule before comparison; it is not inferred from visual similarity.
- A keyed typed table has its column definitions, key-to-row mapping and typed cell values as its value. Keys are unique; missing, unknown and numeric zero have separately declared representations. Under an unordered-row domain, displaying rows in another order preserves X. A domain that includes row order instead gives a different X after that permutation. If the receiving use or selected F relies on order, the expression domain must retain it.

These are independently specified domains, not a closed taxonomy. Another notation supplies its own elements, organization, equality and formation conditions. The chosen domain remains fixed in a comparison. A move between domains requires an explicit correspondence and cannot obtain identity merely by choosing a coarser equality after the change. Concrete copies of a construction do not multiply X when the domain gives them the same value; their carrier tokens can differ.

**Obtain F as reusable rules.** F is an independently identified collection of rules for constructing or arranging eligible expressions. Its identity is the interpreted rules, their application domains and imported dependencies. A layout-only F can leave subject claims unconstrained; another F can require fields, units, coverage or particular interpretations. The episteme that describes F retains its own C.2.1 identity. An expression X conforms to F when it belongs to the applicable expression domain and satisfies each applicable rule and dependency. A rule referring to R uses C.2.1:4.1.1's distinction; a label such as format does not exclude a semantic requirement.

**Obtain C through its own domain.** C is a physical or digital entity from which X can actually be recovered under the stated conditions. For a continuing file object, a write can preserve C while changing its state and X. For an immutable digital snapshot identified by its complete byte value, different bytes identify another C. For a physical sheet or copy token, another copy has another identity. A route such as a URL is the designation or access path used to reach the chosen carrier; it does not determine that carrier's continuity. State which domain the current comparison uses before judging it.

A snapshot value alone establishes no actual availability. Its bearing and publication claims require an actual retrievable realization with a decoding path to X. When several copies realize the same snapshot value, a value-based availability claim can remain true while one copy disappears. A claim about which physical or managed file copy was supplied instead selects that copy as C. These choices preserve the question each consumer actually asks.

The reusable declaration is:

```text
EpistemePublicationRelationSignature:
  RelationKind: EpistemePublicationRelation
  SlotSpecs:
    SelectedEpistemeEditionSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    AudienceDeclarationSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    BoundedUseDeclarationSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    PublicationExpressionSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
    PresentationCarrierSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
```

These SlotKinds name participant meanings only inside this `RelationSignature`. They do not create five new U-kinds, and a card field with a similar label does not become one of these SlotSpecs.

The audience-declaration episteme identifies the audience criterion; it is not the audience and does not prove access by any particular system. A concrete system's access, reading, reliance, or later work is another direct relation or work occurrence. This lets one publication be available to every entity satisfying a stable criterion without inventing `U.Audience` or treating a changing set of readers as changing participants of the same publication occurrence.

`EpistemePublicationRelation` obtains while all of the following are true:

1. `PublicationExpressionRelation(E,X,U)` relates the selected episteme, exact expression and bounded-use declaration;
2. `PublicationExpressionBearingRelation(C,X)` relates the exact carrier and that same expression;
3. entities admitted by the audience declaration can obtain X from C and recover the required content of E under the conditions stated by the bounded-use declaration;
4. E, A, U, X and C remain the identified participants of this occurrence.

One occurrence is reidentified by those five fixed participants and their maximal continuous interval of availability. Changing any participant yields another publication occurrence. Demonstrated loss of availability followed by restoration yields a later occurrence. Missing or stale evidence leaves current obtaining unresolved; it does not prove a gap.

Rendering, printing, uploading, indexing, or granting access are activities separate from the publication occurrence. When a precise performed-Work claim is independently current, recover each exact actual performer through A.13 and let A.15.1 independently admit the dated Work; add F.6 only when that claim or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment. F.6 identifies neither assignment nor performer, and missing or failed F.6 alone leaves independently admitted Work intact. Follow A.6.1 for an operation binding, C.11 for a `ChoiceResult`, or the exact access, reliance, or use relation without reproducing its test here. The activity and any result remain separate from the publication-relation participants.

#### E.24.PUB:4.2 - Recover expression and bearing only when needed

1. `PublicationExpressionRelation(E,X,U)` obtains when interpreting X through its specified decoding conventions and E's effective R yields the claims of that selected E needed for U, with their operative participants, qualifications, modal force and asserted dependencies, and X supports the operations named by U. The recovered content must be traceable to E. If the bounded use requires only a selection, identify that selection and retain the conditions needed to use it; A.6.3's direct construction or loss rule governs any stronger claim of viewing or coarsening. A newly introduced claim belongs to the resulting episteme under C.2.1. It cannot be counted as content expressed from unchanged E.
2. `PublicationExpressionBearingRelation(C,X)` obtains while an actual state or realization of C provides a recovery procedure that yields that exact X under the specified decoding conditions. For a digital value, the procedure reaches an actual accessible realization. The predicate retains the distinction between a continuing carrier and its changing state.
3. `PublicationFormConformanceRelation(X,F)` obtains when the independently identified X satisfies the applicable rules, domains and dependencies of F. It establishes neither which E is expressed nor audience access.

Each of these occurrences is identified by its ordered participant values and maximal continuous interval of predicate truth. Missing evidence leaves obtaining unresolved; it does not itself establish an interruption.

Their reusable declarations are:

```text
PublicationExpressionRelationSignature:
  RelationKind: PublicationExpressionRelation
  SlotSpecs:
    ExpressedEpistemeEditionSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    PublicationExpressionSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
    BoundedUseDeclarationSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required

PublicationExpressionBearingRelationSignature:
  RelationKind: PublicationExpressionBearingRelation
  SlotSpecs:
    PresentationCarrierSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
    BornePublicationExpressionSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required

PublicationFormConformanceRelationSignature:
  RelationKind: PublicationFormConformanceRelation
  SlotSpecs:
    PublicationExpressionSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
    PublicationFormSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
```

**Form-mediated uses.** `PublicationFormExpressionRelation(E,F,U)` obtains while at least one independently identified X conforms to F and satisfies `PublicationExpressionRelation(E,X,U)`. It states that the selected form has an actual adequate expression for this E and U. The existence of a template alone is insufficient.

`PublicationFormBearingRelation(C,F)` obtains while C bears at least one independently identified X that conforms to F. It establishes the recoverability of a conforming construction; the expressed episteme and audience access require their own predicates.

Each of these form-mediated occurrences retains its fixed participants and maximal continuous interval of predicate truth. X is a witness for the quantified claim. Replacing X1 by X2 can preserve either occurrence when that predicate remains continuously true. Changing a filename or storage address does not by itself settle carrier identity; apply the carrier's direct identity and currentness pattern.


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
    PresentationCarrierSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
    BornePublicationFormSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
```

For form-mediated availability through C, the same X must witness expression, bearing and F-conformance. An adequate X1 elsewhere and a different X2 on C do not establish that E is available through C. Recover the shared witness whenever the availability claim depends on both form-mediated relations.

##### E.24.PUB:4.2.1 - Keep the granularity of the availability claim

A consumer can claim continuous availability of E to A for U over an interval when, at every time in that interval, at least one appropriate X and C provides that availability. If the consumer fixes F, C or a set of permitted carriers, retain those constraints in that claim. A change of exact publication does not prove an interruption of this broader availability. A gap is established when the required availability fails across the permitted alternatives. Failure of one copy or route alone does not establish that broader gap. This broader statement needs no new public publication kind or generic occurrence unless a receiving use independently needs its identity.

#### E.24.PUB:4.3 - Use progressive explicitness

Use the smallest statement that supports the current work:

1. **Ordinary use:** name the selected episteme, audience, bounded use, expression and carrier in one sentence; add selected form conformance when needed.
2. **Changed-object use:** say which one of those objects changed and which relation must be re-evaluated.
3. **Contested availability:** state the `EpistemePublicationRelation` participants, obtaining evidence, and occurrence identity.
4. **Contested expression:** open `PublicationExpressionRelation` and the applicable representation, preservation or loss pattern; inspect form conformance when the claim relies on it.
5. **Contested carrier availability:** open `PublicationExpressionBearingRelation` plus the direct carrier-currentness or access pattern; preserve the fixed or quantified alternatives of the actual availability claim.

Do not materialize all five levels as a standing publication card. Stop as soon as the receiving use can distinguish the operative object and relation.

#### E.24.PUB:4.4 - Classify the encountered form by current use

Ask one question at a time:

| Current question | Governed object or relation |
| --- | --- |
| Do the selected claims form an identifiable whole about an EntityOfConcern under an effective reference scheme? | a `U.Episteme` under `C.2.1`; the filled card or diagram supplies its expression |
| Does `EpistemeViewpointConformanceRelation(E,P)` obtain for that episteme E and at least one exact viewpoint episteme P? | the same E has dependent-kind membership as `U.View` under `E.17.0`; any A.6.3 construction remains a separate optional relation |
| Does the particular expression follow selected reusable formation or arrangement rules? | `PublicationFormConformanceRelation(X,F)`; expression of E for U is checked separately |
| Do selected elements correspond to independently recovered objects and support modeling or reasoning operations? | a representation and its correspondence under A.6.3.RT and A.6.3.RT.OE; C.29 supplies the additional grounds for a mathematical lens |
| Does an actual state or realization of the selected carrier yield exact X? | `PublicationExpressionBearingRelation(C,X)` |
| Is the selected episteme available to the declared audience for the declared use through X and C? | one `EpistemePublicationRelation(E,A,U,X,C)` occurrence |

The answers can be jointly positive because they concern different objects or relations. They do not follow from the words `card`, `record`, `table`, `schema`, `diagram`, `view`, `file`, or `publication` alone.

#### E.24.PUB:4.5 - Keep direct verbs with their relations

- an episteme carries claims and designations;
- a `U.View` is the same episteme individual for which E.17.0 conformance to at least one exact viewpoint episteme obtains;
- a particular expression conveys the selected episteme's required claims for a bounded use;
- a reusable publication form constrains eligible expressions;
- a representation stands in an identified correspondence to its subject; C.29 governs the mathematical-lens branch;
- a carrier bears a particular expression through its actual state or realization;
- a publication occurrence makes one selected episteme edition available;
- a system may perform publication activity and may later access or rely on the published episteme, but those are separate claims under their direct patterns; publication availability establishes none of them;

A designator designates and a governed reference resolves to a referent. Neither operation publishes, bears, represents, or makes the subject-side predicate obtain.

#### E.24.PUB:4.6 - Keep subject patterns subject-first

In a pattern about an ontic, structure, architecture, characteristic space, method, or another subject, explain the subject's identity, relations, practical problem, and solution before publication details. Add E.24.PUB only when the receiving use depends on distinguishing the description, selected edition, form, carrier, audience, or bounded use.

When the EntityOfConcern is itself a description episteme, the same rule applies one level up. The description stays the subject; publication of that description is a neighboring relation.

### E.24.PUB:5 - Archetypal Grounding

#### E.24.PUB:5.1 - Maintenance inspection card

A completed pump-inspection card states measured clearances and identified defects about Pump #37 under the maintenance reference scheme. Those organized claims constitute the card episteme E. The filled card supplies expression X; its reusable layout rules supply F. The PDF file is C under its selected file-object or snapshot identity. One publication occurrence makes edition 4 of the card episteme available through X and C to the maintenance-planning team for planning the next repair.

Changing the PDF filename changes neither E nor necessarily C. Correcting a measured clearance changes the claim content and therefore E; a later-edition claim also needs C.2.1:4.5 continuity. Replacing the layout changes F. If this changes X, it also changes the exact publication, while broader availability of E can continue. Making the same E available to a supplier for quotation creates another exact publication because A or U changes.

#### E.24.PUB:5.2 - Architecture diagram

An architecture diagram can express claims about selected structures of one holon. Those claims can constitute an architecture-description episteme. When that exact episteme conforms to an architectural viewpoint under E.17.0, the same individual is a `U.View`; direct authoring and A.6.3 construction are independent construction routes. Reusable graphical conventions can supply F; the constructed diagram supplies X. A correspondence connects its elements to the represented subject, with C.29 additionally governing any mathematical inference or transfer. A screen or sheet can supply C.

The diagram does not become the architecture by being published. `C.30` governs the `ArchitectureOf@Context` claim and `A.22` governs selected `U.Structure` values. E.24.PUB lets the architect locate a publication defect without replacing the architectural question with a discussion of diagrams.

#### E.24.PUB:5.3 - Clinical procedure edition

A hospital procedure description is an episteme about how a procedure is performed. Treat it as a `U.MethodDescription` only when its EntityOfConcern is one independently admitted `U.Method` and its claims describe how that Method is carried out. A wall poster expresses a selected edition for quick pre-procedure orientation; the laminated sheet is the carrier. A separate controlled publication makes the same edition available to clinicians for authoritative use during the procedure. The two publication occurrences differ in bounded use even if the words are identical. Neither publication proves access, reliance, Method enactment, or clinical Work. If later clinical Work is independently claimed, route that claim to its direct Work and attribution patterns rather than restating their basis here. Keep the publication occurrence and every separately current access, reliance, assignment, Method, Work, or result claim distinct.

#### E.24.PUB:5.4 - FPF pattern host

An E.24 pattern host contains an expression X of an ontic-description episteme about `U.Ontic`; its layout follows a reusable form F. The repository file is C. The selected episteme participates in an exact publication occurrence while X and C make it available to the declared FPF audience for the stated use. Changing C alone leaves the episteme's claim content, subject and interpretation unchanged.

#### E.24.PUB:5.5 - Training availability and later choice work

One instruction edition is available to a training group for studying a method. That `EpistemePublicationRelation` occurrence establishes availability to the declared audience for that bounded use; it establishes neither that anyone read the instruction nor that adjustment, inspection, acceptance, or release work occurred. The same availability alone does not support an acceptance commission's choice about releasing one named lot.

If a commission later makes a release choice and that stronger claim is current, recover each exact actual choice-work performer through A.13 and let A.15.1 independently admit any dated choice Work. Add F.6 only when the choice account or receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; F.6 identifies neither assignment nor performer, and missing or failed F.6 alone leaves independently admitted choice Work intact. Identify the resulting `ChoiceResult` separately under C.11. Keep both Work and result separate from the publication occurrence; the publication statement need not carry their identity, staffing, or omission rules.

When the later claim says that the published instruction was actually used, state that exact use under its direct relation, or under A.6.1 only when a declared operation application is current. If no such route is established, stop at publication availability and let the receiving pattern identify its own blocker. The `ChoiceResult` is neither the choice Work, the bounded-use declaration, nor a participant of the publication occurrence.

### E.24.PUB:6 - Bias Annotation



- **Onto:** direct relation occurrences and their actual participants remain primary; visible forms do not decide kinds.
- **Epist:** the selected edition, audience declaration, and bounded-use declaration retain C.2.1 identities.
- **Semio:** designation, expression, representation, bearing, and publication availability use different predicates.
- **Arch:** keep each subject claim with its applicable pattern; E.24.PUB defines only the neighboring publication architecture.
- **Prag:** progressive explicitness stops at the first statement sufficient for the receiving use.
- **Did:** ordinary first use stops at one readable sentence; the cases show which object or relation changes when a publication is revised.

### E.24.PUB:7 - Conformance Checklist

| Check | Observable conformance condition |
| --- | --- |
| `CC-E24PUB-1` | The bounded-use declaration itself names the intended receiving use. A separate plan, decision question, or `U.WorkPlan` is cited only when it independently exists and changes the publication claim. The publication statement names the selected edition, audience, bounded use, expression and carrier; it establishes no actual access, reliance, use, Work, or result. Any independently current stronger claim is routed to its direct pattern without reproducing that pattern's test here. |
| `CC-E24PUB-2` | The selected episteme edition, audience declaration, bounded-use declaration, particular expression and carrier are independently identified; an optional reusable form has its own rules and conformance predicate. |
| `CC-E24PUB-3` | `EpistemePublicationRelation` has the five exact participant meanings, the availability predicate, and the maximal-continuous-occurrence identity rule stated in section 4.1. |
| `CC-E24PUB-4` | Exact expression and bearing predicates are recoverable when load-bearing. A selected form has its conformance predicate. Form-mediated availability uses the same X as witness for expression, bearing and conformance; broader availability retains its permitted alternatives. |
| `CC-E24PUB-5` | Plain `published episteme` states publication participation. A receiving classification use has its C.3.2 basis; public-kind admission follows E.24.UK. The availability-only use retains the rejection `E24UK-NAR-EPUB-01`. |
| `CC-E24PUB-6` | A `U.View` remains a same-individual dependent specialization of `U.Episteme` under an obtaining E.17.0 conformance relation; graphical appearance and A.6.3 construction alone supply no membership. |
| `CC-E24PUB-7` | Representation correspondence is stated for the applicable operation; C.29 is used for its mathematical branch. Expression elements, reusable-form rules and subject-side objects retain their own identities. |
| `CC-E24PUB-8` | Publication activity, actual access, reliance, evidence, decision, performed Work, operation binding, and result remain under their direct patterns. E.24.PUB checks only that publication availability is not used as proof of those stronger claims. |
| `CC-E24PUB-9` | A changed episteme, expression, form, carrier, audience, or bounded use leads to the smallest affected object or relation rather than a whole-stack rewrite. |
| `CC-E24PUB-10` | Ordinary use stops at the readable sentence when the receiving use needs no fuller relation detail. |

### E.24.PUB:8 - Common Misuses and Repairs

| Misuse | What actually failed | Repair move |
| --- | --- | --- |
| File equals episteme | Carrier continuity is used as claim-content identity. | Recover the C.2.1 episteme identity and the carrier's direct identity separately. |
| Diagram equals view | Graphical form or construction history is used as the `U.View` membership criterion. | Recover exact candidate episteme E, exact viewpoint episteme P, and E.17.0 conformance; keep any A.6.3 construction, selected use, form, and representation separate. |
| Publication equals expression | The form or rendered expression is treated as the publication occurrence. | Name the five `EpistemePublicationRelation` participants and test availability. |
| Available equals used | Publication is treated as proof of reading, reliance, decision, Work, or result. | Open the exact direct pattern only when that stronger claim is current; E.24.PUB supplies none of its admission or obtaining proof. |
| Republished equals revised | A new expression, form or carrier is treated as another episteme edition. | Apply C.2.1 identity. A changed discriminator identifies another E; a later-edition claim additionally needs the :4.5 source and continuity conditions. |
| Published-episteme kind | Temporary availability becomes a durable U-kind. | Keep `U.Episteme`; use Plain `published episteme` plus the exact publication occurrence. |
| Warning pile-up | A subject pattern lists every publication-side object before explaining its subject. | Keep the subject first and add only the distinction on which the receiving use depends. |

### E.24.PUB:9 - Consequences

The main gain is local repair. A stale carrier can be replaced without pretending that the claims changed. A revised claim can create another episteme edition without pretending that the audience or form changed. A narrower audience or use can create another publication occurrence while preserving the edition.

The cost is that load-bearing publication claims need five identified participants and two supporting relations. Progressive explicitness contains that cost: ordinary users state one sentence; only disputed availability, expression, or bearing opens the complete relation detail.

### E.24.PUB:10 - Rationale

Publication does not change an episteme into a nested publication object. It is a real availability relation supported by an expression relation and a bearing relation. That architecture explains why one encountered card, diagram, or file can matter in several ways without admitting one umbrella presentation kind.

The split also preserves agency. A System can render, upload, print, index, withdraw, or replace a carrier, but the publication occurrence is the enduring availability relation, not that activity. It may obtain with no continuing publication Work, and an attempted publication activity can fail while no publication occurrence begins. If an actual Work claim matters, its direct patterns govern it; E.24.PUB only keeps it and its result outside the publication-relation participants.



In OWL, SKOS, RDF and triple-store implementations, one interface can expose labels, axioms, serializations, documents and queries together. Recover their functions for the intended use: an export operation by itself establishes neither the kind of the exported subject nor the truth of its claims.

### E.24.PUB:11 - SoTA-Echoing

The practical question is what an audience can obtain for a stated use, and which availability continues when the expression or carrier changes. Sections 4.1–4.2 use the following comparison.

| Construction | Question it can answer | Reason to select or limit it |
| --- | --- | --- |
| Exact publication with fixed E, A, U, X and C | Which expression of this episteme was available to this audience, for this use, through this carrier? | Select it when the provided content or copy matters. Comparing X first makes an expression change visible without inferring a change of E. |
| Form-mediated availability with a permitted expression X | Is some expression of E conforming to F available through C for A and U? | This is sufficient when the receiving use needs availability in that form. It leaves the particular X open; identify X as well when the question becomes what exactly was provided. |
| Exact publication with mandatory F as an additional participant | Which exact expression and reusable form were provided? | Record a selected F through form conformance. Making F a fixed participant of every publication requires a separate form selection even when the receiving use needs only the ordinary expression. |
| Identify a publication change with a change of E | Did the account itself change? | This collapses two comparisons. Carrier or expression changes can preserve E; recover E through C.2.1 and compare its publication separately. |

For form-mediated availability, one and the same X must satisfy expression, bearing and form conformance. An adequate expression elsewhere and a different conforming expression on C do not establish that C makes E available. This shared witness is the binding that the two separate existential support claims leave open.

A change of exact X or C creates another exact publication occurrence. Broader availability can nevertheless continue while at least one permitted expression and carrier remains available at every time in the stated interval. Keep any form or carrier restriction that the receiving use actually requires. A failure of one copy establishes a broader gap only if all permitted alternatives fail.

The cost of the exact comparison is selecting the expression domain and equality, carrier identity, and relevant time interval before comparing publications. A continuing managed file and an immutable snapshot answer different identity questions. For ordinary use, the readable publication sentence suffices; recover this detail when its alternatives can change the answer.

The following bounded comparisons support those choices. Their source models retain their own meanings.

| Source and scope | What changes in this pattern |
| --- | --- |
| [RDF 1.1 Concepts, §§1.5 and 1.8](https://www.w3.org/TR/rdf11-concepts/): a static graph, its concrete-syntax document and a mutable source have different change conditions. | Sections 4.1–4.2 preserve independent E, X and C comparisons. This is a technical counterexample to equating content, expression and source identity; it does not identify an FPF episteme with an RDF graph. |
| [OpenWEMI specification](https://www.dublincore.org/specifications/openwemi/specification/): its broadly defined classes can be used separately, and its relations permit more than a mandatory linear chain. | This is a serious alternative to requiring every intermediary for every publication. Section 4.2 selects F only for an actual reusable-rule use; it does not import the OpenWEMI hierarchy or its entity meanings. |
| [Norouzi, Hertling, Waitelonis and Sack 2025](https://arxiv.org/abs/2509.23776v1), author abstract: implicit patterns in process ontologies may lack explicit publication or documentation accessible to domain experts. | The audience and bounded-use participants, and the expression test in section 4.1, require recoverable content for the intended use. Presence in an ontology or workflow-shaped display alone does not answer that question. |
| [Fathallah et al. 2026, v2 of 26 July](https://arxiv.org/abs/2506.01232v2), author abstract: RIGOR starts from relational schemas and enriches them with domain information to construct OWL ontologies. | The expression test retains the interpreted claims; section 4.2 permits a schema or table migration to change X or C while E is preserved. Mapping or serialization alone is not treated as full recovery of domain meaning. |
| [Oyewale and Soru 2026](https://arxiv.org/abs/2602.01276v1), author abstract: ontology construction separates extraction, hierarchy formation and RDF serialization, with reported limitations in scope and hierarchy. | Sections 4.4–4.5 and CC-E24PUB-8 keep construction and its epistemic adequacy separate from publication availability. Export success supplies no missing adequacy judgement. |

The abstracts supply these bounded problem comparisons, not a validated performance ranking or the five-participant FPF predicate. A.6.REL supplies the direct-relation and occurrence rules; C.2.1 supplies episteme identity. A.6.3, C.29, E.17 and E.24.UK retain their construction, mathematical-representation, view-membership and admission questions. Their combination here is the FPF construction justified by the publication questions above.

Reopen the choice when a real receiving use cannot distinguish the provided content under the declared identities, or when the broader-availability rule reports a gap despite continuous availability through its permitted alternatives. Reopen a source comparison when a newer result changes the distinction it supports. A different file format or storage tool alone supplies neither counterexample.

### E.24.PUB:12 - Relations

- **Builds on:** `A.6.REL` for direct obtaining and occurrence identity, `C.2.1` for the selected edition and declaration epistemes, and `E.24` for ontic-description boundaries.
- **Coordinates with:** `E.17.0` for `U.View` membership and `E.17` for multi-view publication; `A.6.3` for optional viewing construction; `A.6.3.RT` and `A.6.3.RT.OE` for representation construction; `C.29` for a mathematical lens; `E.8` for FPF pattern-form rules; and the direct carrier-currentness or access pattern when that question is current.
- **Coordinates with:** `E.24.CD` for candidate detection and `E.24.UK` for public U-kind and dependent-kind settlement. Its result `E24UK-NAR-EPUB-01` rejects `U.EpistemePublication` for the availability-only use; this pattern states that participation, while C.3.2 governs a receiving classification use.
- **Used by:** subject patterns only when a receiving use depends on distinguishing the subject, description episteme, selected edition, view, representation, publication form, carrier, audience, bounded use, or publication occurrence.

### E.24.PUB:End
