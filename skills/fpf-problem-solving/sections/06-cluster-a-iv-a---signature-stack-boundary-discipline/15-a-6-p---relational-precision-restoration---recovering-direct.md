## A.6.P - Relational Precision Restoration - Recovering Direct Relations from Under-Specified Claims

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain name.** Relation precision restoration.

**Mint or reuse.** This pattern reuses direct relation kinds, direct obtaining predicates, relation-participant meanings, `RelationSignature`, `SlotSpec`, `U.Relation`, `U.Episteme`, designators, references, descriptions, publications, and representations from their governing patterns. It introduces no U-kind, universal record-shaped relation object, qualification object, or generic relation-change object. A `RelationKind` token designates an already settled relation kind in a local or public vocabulary; the token is neither the kind nor an occurrence.

**Plain object stack.** A direct relation is what obtains among its actual participants under the participant meanings and obtaining condition stated by its direct pattern. Each participant keeps its independently governed kind. A compatible `RelationSignature` is a declaration episteme; one declaration-local `SlotSpec` can correspond to one participant meaning when reusable typed use is current. An assertion or occurrence-description episteme may designate the participants or an already recoverable occurrence. A table row, tuple, record, graph edge, functional expression, or arrow is a representation only through an explicit `C.29` correspondence. None of those epistemic or representational objects makes the relation obtain or supplies occurrence identity by form.

### A.6.P:1 - Problem frame

**Use this when.** Use this pattern when a claim contains a relation-bearing phrase, but the phrase does not yet determine the direct relation, exact participants, direction, or detail needed by a later engineering claim or operation. Common recognition moments include a broad predicate such as "linked", "aligned", or "supports"; a participant named by metonymy; a qualifier that sounds precise while leaving the head kind unknown; service, server, provider, delivery, or access wording that leaves the promise, interface, system, role, method, work, or evidence object unclear; whole, part, complete, turnkey, or end-to-end wording that leaves a candidate whole, boundary, parthood, composition, coverage, or work claim unresolved; and `integrity` wording that still leaves open whether the sentence is about a structural whole, a characteristic or measurement, or evidence or assurance.

Quoted, external, or ordinary source prose may remain as written. Open A.6.P only when an FPF statement will use the phrase to guide action, justify a decision or gate, support assurance or reliance, publish a claim, or reuse it across contexts. Repair that receiving FPF statement; preserve the source wording as a quotation or source expression instead of rewriting it as though the source had made the repaired claim.

**Primary working reader, viewpoint, and concern.** The working reader is an engineer viewing the sentence as input to a later claim or operation. The concern is that another person can find the same world-side or episteme-side objects, select the same direct governing pattern, and know which additional declaration, assertion, occurrence, designation, or representation detail that later use actually needs.

**Primary EntityOfConcern.** One relation-bearing claim in an episteme whose current expression leaves the direct relation kind or one or more actual participants unresolved, or leaves unclear whether a later claim or operation needs reusable declaration, explicit occurrence identity, designation, or representation.

**First useful move.** Replace the broad phrase with one readable sentence that names the exact participants and the direct relation believed to obtain. Name the governing pattern for that relation. If either the participants or the relation remain genuinely ambiguous, keep a small working candidate note and resolve that ambiguity before adding a reusable declaration, assigning a designator, or choosing a representation.

**First-minute result.** The draft `Bearing_B is linked to Pump_P` becomes `Bearing_B isInstalledPartOf Pump_P during Interval_T` after inspection identifies the physical part relation governed by `A.14` and its current interval. If no later maintenance claim or operation distinguishes this installation episode from another, the repair stops there. A `RelationSignature`, explicit occurrence reference, or graph representation is added only when a named later claim or operation needs it.

**What goes wrong if missed.** A lexical replacement can make the sentence sound technical while preserving the same ambiguity. At the opposite extreme, an engineer can turn every relation phrase into a record-shaped episteme and then confuse that episteme, a declaration, or an identifier with the relation that obtains. Both failures obscure what is true, which object changes, and which pattern governs the needed claim or operation.

**What this buys.** The repaired claim remains readable. Load-bearing uses gain exact relation kinds, participant meanings, reusable typed declarations, occurrence identity, designations, and representations only where those distinctions change the later claim or operation.

**Not this pattern when.** Use the direct relation pattern when the relation and participants are already clear. Use `A.6.5` when only reusable `SlotSpec`s are needed, `A.6.REL` when one obtaining occurrence needs explicit identity, `C.2.1` when the issue is assertion or description identity, and `F.18` when the object and relation are known and only designation remains unresolved.

FPF treats relation realism and epistemic access separately. A relation can obtain among its participants before anyone states, stores, diagrams, or names that fact. An assertion can affirm or deny the direct obtaining predicate. A declaration episteme carries reusable vocabulary and laws. A designator denotes an already recoverable object under an effective reference scheme. An episteme becomes available through a publication relation. A representation corresponds to an independently governed object or claim content. Relation precision restoration keeps these objects connected without collapsing them.

### A.6.P:2 - Problem

An under-specified relation claim blocks a later claim or operation because several ontological questions remain hidden inside one phrase:

1. What kinds of objects are being related?
2. Which direct relation predicate is asserted to obtain?
3. Which relation-participant meanings are current, and are all actual participants named?
4. Does the current text state world-side participation, make an episteme claim about the direct relation, or define a local kind of entities participating under one meaning?
5. Does reusable typed use require a compatible `RelationSignature` and declaration-local `SlotSpec`s?
6. Does a later claim or operation need one obtaining occurrence to have explicit identity?
7. If something changes, is the changed object the occurrence, a declaration edition, assertion content or reliance posture, an evidence relation, a designation, a receiving-episteme reference, a description, a publication relation, a Bridge, or a representation edition?

Without answers, readers cannot tell whether two statements disagree, whether one participant may replace another, whether an inverse sentence preserves meaning, or whether a later claim refers to an obtaining occurrence rather than to an assertion or representation of it.

### A.6.P:3 - Forces

| Force | Tension |
|---|---|
| Readability and precision | Ordinary work benefits from short relation sentences, while reuse may need exact participant typing and identity. |
| Relation realism and epistemic access | A relation may obtain independently of its assertion, yet engineering work reaches it through observations, epistemes, descriptions, publications, and representations. |
| Generality and grounding | The method applies across domains, while every repaired relation needs domain-grounded participants and an exact obtaining condition. |
| Minimal explicitness and later claims | Premature declarations and records create burden; insufficient detail makes a named later comparison, substitution, change, or reference unreliable. |
| Natural-language direction and relation polarity | Inverse wording can aid readers, while silent participant reversal can change the predicate. |
| Stable world-side facts and evolving epistemes | The relation kind can stay stable while assertions, declarations, evidence, descriptions, publications, and representations change independently. |
| Grammar and ontology | Verb-shaped wording can express a relation, work, method, or change, but grammatical form settles neither identity nor agency. |

### A.6.P:4 - Solution

Begin with the objects named by the claim. Recover exact actual participants and one direct relation first. Then add only the declaration, assertion detail, occurrence identity, designation, reference, or representation demanded by the exact later claim or operation.

**Local RPR mantra — five moves.** *Name the referents. State the direct relation or comparison with its actual participants, then follow its governing pattern. For the next named reader or task, add a declaration only to reuse typed rules, occurrence identity only to distinguish occurrences, a designation only to refer back to one object, or a representation only to show it in another form; otherwise add none. If a later sentence says something changed, name which object changed—the relation occurrence, claim-bearing episteme, designation relation, or representation—and follow that object's pattern. Then shorten without hiding the relation or its participants.*

`Referents` means the objects recovered in 4.1; it is not a shared kind. `Comparison` means the direct comparison relation governed by `A.19.CPM`. `Actual participants` means the independently governed entities that participate under the relation's participant meanings. The mantra does not ask the reader to fill slots or positions or to create a record.

The mantra keeps the repair order and stop in attention. Sections 4.1-4.12 remain the governing Solution for hidden arity, world-side and epistemic separation, demand-driven declaration and individuation, relation-dependent wording, polarity, unresolved candidates, exact changed objects, Plain relaxation, and direct-pattern exit. The mantra is Plain didactic wording, not a second method, work plan, or performed work.

#### A.6.P:4.1 - Recover the objects before choosing relation notation

Start from the claim as written and ground each load-bearing head:

1. Identify the exact referent intended by each participant expression.
2. State the independently admitted kind of each referent under its direct governing pattern.
3. Separate a world-side object from an episteme about it and from a publication or representation of that episteme.
4. Recover metonymy explicitly. The phrase `at the table` may state physical location or participation in a negotiation meeting. Evidence from the current case selects the direct relation; neither reading by itself establishes a role assignment.
5. Leave the claim unresolved when the current evidence does not select one referent. A more technical synonym is not a repair.

The result of this step is an ordinary sentence containing identifiable objects. It is not a newly minted object kind. When several candidates remain live, use the small working note in A.6.P:4.9.

If the material is still a cue and no relation-bearing claim can yet be stated, stay with `A.16.1` or `B.4.1` instead of forcing relation publication. If the cue has stabilized into an open explanatory question but still has no selected relation answer, continue through `B.5.2.0`.

If counter-evidence or a failed use shows that a published relation statement overstates its articulation, closure, or framing, use `A.16.2` to reopen, back off, or respecify that publication. `A.16.2` records the retreat; A.6.P repairs the relation again only after the engineer can name a grounded candidate relation, its participants, and a discriminating check. Use `A.16.0` only when readers must see lineage, branching, loss, or responsibility-transfer history; a local return needs no trajectory account.

A.6.P begins when the available observations or claims let the engineer name at least one grounded candidate relation, its participants, and a discriminating check.

#### A.6.P:4.2 - State the direct relation, participant meanings, and obtaining condition

Write the smallest readable direct-relation sentence that answers the current question:

```text
<actual participant 1> <direct relation predicate> <actual participant 2> ...
```

Then name the direct governing pattern and recover from it:

- the admitted direct relation kind and its explicit governed `RelationKind` token;
- the relation-participant meanings and actual participants, each retaining its independently governed kind;
- the condition under which the relation obtains and its semantic predicate is satisfied by those participants considered under the participant meanings;
- applicability, direction, symmetry, inverse law, polarity, and temporal qualification when they change the predicate;
- the occurrence-identity rule, whether or not the current use needs explicit individuation;
- when the direct ontology says that a new occurrence is constructed or constituted, the constructor, inputs, construction work or process, and their contribution to occurrence identity.

Every in-scope direct subject-relation claim that exits A.6.P as positive or governed negative names an explicit admitted `RelationKind` token. When no suitable token exists, first settle the governed relation value and any required relation-kind admission under its direct pattern, `A.6.RCD`, and `E.24`; then apply `F.8` and, for durable naming, `F.18` and `F.17`. Naming does not admit a kind or occurrence. An exact `A.6.1` operation-application binding, local `A.15.PROD` or `A.6.RCD` claim, or non-assertability result keeps its direct owner's semantics and is not coerced into this relation-kind family.

An ordinary assertion may name the actual participants directly. When reusable typed use is current, a compatible `RelationSignature` declaration can restate the participant meanings, obtaining predicate, applicability, and identity rule and contain only the declaration-local `SlotSpec`s needed by the receiving typed uses. The declaration remains an episteme; it neither makes the relation obtain nor supplies occurrence identity.

Assertion polarity remains claim-side. An affirmative assertion claims that the direct predicate is satisfied; a negative assertion denies it. Refutation or unresolved reliance belongs to `A.10` or the receiving evaluation. Denial, refutation, or unresolved reliance creates no negative world-side occurrence.

Do not select ontology from grammar. A verb-shaped phrase supplies neither constructive identity nor agency. Use the exact direct pattern for the relation, object, work, method, change, role, or acting system named by the current claim.

#### A.6.P:4.3 - Recover actual participants, hidden arity, qualifiers, and typed declaration only when needed

Ask which actual participation belongs to the direct relation's obtaining condition. Add a participant or qualifier only when it changes one of these:

- predicate satisfaction or relation obtaining;
- applicability or admissible use;
- occurrence identity;
- whether one participant can replace another without changing the claim;
- interpretation under an effective reference scheme;
- scope, `Γ_time`, viewpoint, view, or another exact qualification owned by the direct relation or receiving claim;
- witness or evidence expectations for a named decision or publication use;
- the exact later claim or operation.

For `Sample_S wasMeasuredBy Instrument_I`, a later evidence claim may separately refer to the measurement work occurrence, its interval, the applied measurement method, a measurement-result episteme, and a calibration episteme. The measured-by relation includes only the actual participants selected by its direct obtaining condition; the other objects remain participants or content of their own work, evidence, temporal, method-use, measurement, assertion, or description relations.

When reusable typed use is current, declare each participant meaning needed by that use through A.6.5:

```text
SlotSpec := <SlotKind, ValueKind, refMode>
```

One `SlotKind` names one participant meaning locally inside one exact `RelationSignature`. `ValueKind` states the independently governed kind of the corresponding actual participant. `refMode` states how a receiving assertion or occurrence-description episteme designates that participant. The `SlotSpec` is declaration content; the participant does not become or occupy that declaration component. If one proposed `ValueKind` hides objects for which the predicate has different meaning, recover a real common kind or split the direct relation kind instead of preserving a hidden union as a prose list.

#### A.6.P:4.4 - Keep world-side, declaration, assertion, designation, and representation objects distinct

| Object | Engineering question | Governing pattern |
|---|---|---|
| direct relation kind | Which obtaining occurrences fall under this classificatory distinction? | direct relation pattern, with `A.6.RCD` and `E.24` when admission is current |
| relation-participant meaning | How does one actual participant contribute to the obtaining predicate while retaining its own kind? | direct relation pattern |
| actual participant | Which exact independently governed entity participates under that meaning? | participant's direct pattern and the direct relation pattern |
| semantic predicate and applicability | Under which condition and qualifications does the direct relation obtain for those participants? | direct relation pattern |
| `RelationSignature` declaration | Which relation semantics and typed participant declarations are reusable? | `A.6.0` |
| declaration-local `SlotSpec` | Which participant meaning, participant `ValueKind`, and receiving-episteme designation mode are declared for typed reuse? | `A.6.5` |
| relation-participant designation | Which value or governed reference in a receiving episteme denotes one actual participant? | `C.2.1`, with `A.6.5` only when a compatible `SlotSpec` is current |
| relational assertion | Which episteme affirms or denies the direct predicate, or carries another exact claim-family modality? | `C.2.1` plus the direct claim pattern |
| relation-occurrence description episteme | Which episteme describes one already individuated occurrence? | `C.2.1` |
| individuated relation occurrence | Which obtaining occurrence does a later claim or direct relation compare, qualify, nest, or reference? | direct relation pattern with `A.6.REL` |
| designator and reference use | Which governed name denotes an already recoverable object, and which receiving episteme uses that reference? | `F.18` and the receiving claim pattern |
| publication relation | Which episteme edition is made available, to whom, and for which use? | `E.17` and `E.24.PUB` |
| representation element | Which table field, row, tuple component, graph edge, formula position, functional expression, or arrow corresponds to an independently governed object or claim content? | `C.29` for the explicit correspondence; the representation object's own pattern for its identity and change |

A representation can correspond to a direct relation, assertion content, declaration, participant designation, or already recoverable occurrence. State the exact source element, represented FPF object or claim content, and explicit `C.29` correspondence. Representation form neither makes the relation obtain nor supplies participant or occurrence identity.

Functional and arrow forms are therefore assertion or representation notation, not world-side relation objects:

```text
installedPartOf(Bearing_B, Pump_P, during=Interval_T)
Bearing_B --installedPartOf{during=Interval_T}--> Pump_P
```

The first can represent the content of a relational assertion; the second is a binary projection in a selected representation. A use that relies on either notation declares how its argument or endpoint elements correspond to the actual participants, direct predicate, qualifications, and any designated occurrence. The ordinary readable sentence remains sufficient when no representation-dependent use is current.

#### A.6.P:4.5 - Increase explicitness only for a named receiving use

Here **receiving use** is Plain shorthand for the exact later claim or operation that needs an additional object. It is not a shared FPF kind. Name that claim or operation and its direct governing pattern before using it to justify more apparatus.

Use progressive elaboration from one recovered direct relation:

```text
readable direct-relation sentence with actual participants
  +-- compatible RelationSignature and SlotSpecs, when reusable typed declaration is current
  +-- explicit occurrence individuation, when a named receiver needs occurrence identity
      +-- occurrence-description episteme or stable designation, only when that receiver needs it
  +-- relational assertion detail, when polarity, modality, or reliance is current
  +-- C.29 representation and correspondence, when a representation-dependent use is current
```

This diagram is itself a `C.29` representation of independent elaboration branches, not a world-side structure or mandatory process. A `RelationSignature` is not a prerequisite for explicit occurrence identity. An assertion may name actual participants without a reusable declaration. A relation can obtain under its direct rule even when no local episteme exposes an occurrence designator. Conversely, a stored row, graph edge, tuple, or identifier does not establish obtaining.

Apply the `A.6.REL` receiving-use test before explicit individuation. Comparison, occurrence history, nesting, and participation of an occurrence in another direct relation normally need identity. A direct relation assertion can stop without explicit occurrence identity when no later claim or operation distinguishes that occurrence. Repeated occurrences may have the same participants; the direct identity rule, not participant equality or row identity, supplies the discriminator.

#### A.6.P:4.6 - Resolve relation-dependent wording by the actual object

| Current reading | Actual object | Next move |
|---|---|---|
| world-side participation | one exact entity participates directly in an obtaining relation under one relation-participant meaning and retains its independently governed kind | use the direct relation pattern; add no `SlotSpec` unless reusable typed declaration is separately current |
| assertion- or description-side designation | a claim-bearing assertion or occurrence-description episteme designates an actual participant, or an already recoverable occurrence when identity is current | use `C.2.1` plus the direct claim or description pattern; use A.6.5 only when a compatible `RelationSignature` actually supplies typed reuse |
| context-local derived kind | a later typed claim quantifies over entities participating under one designated participant meaning and a declared extent rule | use `C.3` and `C.3.1` only for typed membership, quantification, substitution, or kind-order reasoning |

These readings leave no fourth qualification object. A readable word such as `result`, `input`, `problem bearer`, or `next continuation` can remain in Plain prose when the direct relation or claim is recoverable. Naming that reading creates neither a kind nor an occurrence. The world-side participant never becomes a declaration-local `SlotSpec`; the receiving episteme's designation denotes the participant without replacing it.

#### A.6.P:4.7 - Name change by the object that actually changes

There is no universal relation-edit operation. First point to the object that the sentence says changed. If the sentence says that the same object continued, use that object's identity rule to test that claim. If identity-bearing episteme content changed, name the result as another episteme rather than an in-place edit:

| Object named as changed | What the reader does | Owner and stop |
|---|---|---|
| obtaining relation occurrence | Ask whether the later event is the same occurrence. Apply the direct relation's identity rule. For a temporally extended occurrence, record that it began, continued, ceased, or split. If the rule says it is not the same occurrence, name a second occurrence; do not say that the first occurrence became it. | direct relation pattern with `A.6.REL` |
| `RelationSignature` declaration content | If vocabulary, participant meanings, `SlotSpec`s, laws, applicability, identity-rule content, EntityOfConcern, or effective reference scheme differs, name the revision Work and its output as another episteme. Test that output anew as a `U.Signature`. Call the two epistemes editions, refinements, or successors only after the complete direct predicate for that relation is satisfied; otherwise stop at two distinct epistemes. | `C.2.1` and `A.6.0`; `A.15.1` for revision Work |
| relational assertion content | If claim content, EntityOfConcern, or effective reference scheme differs, name another assertion episteme. Keep the revision Work, later episteme, retraction or currentness claim, publication, reliance posture, and continuity relation separate. Then test the world-side predicate again; edited text is not evidence that the world-side relation changed. | `C.2.1`, the direct claim pattern, and `A.15.1` for revision Work |
| reliance posture for one declared use | Record reliance as supported, refuted, or unresolved for that use. Do not change assertion polarity or create an occurrence. | `A.10` or the receiving evaluation |
| evidence or witness relation | State which evidence-bearing episteme or carrier bears on which claim, then test whether that relation begins, ceases, or is superseded. Record time and freshness under that owner. | `A.10`, `B.3`, or the direct evidence pattern |
| participant designation in a receiving episteme | If an author substitutes another by-value designation inside the receiving claim, the resulting claim content identifies another episteme. If only a reference interpretation or retargeting relation changes, state that relation separately. Recheck the world-side predicate; use `A.6.5` only when the receiving claim reuses a compatible declared `SlotSpec`. | `C.2.1` and `F.18`; `A.6.5` for the declared reuse |
| occurrence designator | Assign, replace, retire, or interpret a designator only for an already recoverable occurrence. The name does not create or change the occurrence. | `F.18` and the effective reference scheme |
| description episteme | If claim graph, EntityOfConcern, or effective reference scheme differs, name another description episteme and the revision Work separately. Assert an edition, refinement, or supersession relation only after its own predicate is satisfied; otherwise stop at two descriptions. | `C.2.1`; `A.15.1` for revision Work |
| publication relation | State that one selected episteme was made available, that its availability ceased, or that another episteme was published. Do not infer a content or world-side change from publication alone. | `E.17` and `E.24.PUB` |
| representation-bearing episteme | If its claim content, EntityOfConcern, or effective reference scheme differs, name another episteme and keep the revision Work separate. Do not infer a represented-world change from that new episteme. | `C.2.1`; `A.15.1` for revision Work |
| representation form or element | First ask: did one mark or form change, or is the same EntityOfConcern represented first by a source episteme under one scheme and then by a receiving episteme under another? For a mark or form change, name the resulting representation object under that object's identity rule; do not call it a scheme transition. State a changed `C.29` correspondence or lens-use claim separately as another claim-bearing episteme. Use `A.6.3.RT` for a true scheme transition only if its entry accepts the named source episteme, receiving episteme, common EntityOfConcern, both schemes, and the transition sentence the task needs. Its result must state the predicate, participants, applicability, and rule for telling occurrences apart; a slot/ref record is not enough. If either test fails, do not use `A.6.3.RT`: name the missing pattern for identifying the changed representation object, or return `missing-governor` through `A.6.RCD` when the blocked next sentence needs the direct transition relation. None of these changes by itself changes the represented world-side object. | the pattern that identifies the changed representation object or transition; `C.2.1` and `C.29` for the separate claim; guarded `A.6.3.RT` or `A.6.RCD` for a direct transition claim |
| actual correspondence occurrence, separate from a `C.29` claim or representation | A `C.29` correspondence claim, Card, edge, or representation does not prove that an occurrence exists. Name the representation element and what it represents, then write the plain correspondence sentence the next task needs. If a current pattern states that predicate and its applicability, test whether it holds. If the task only needs to know whether the correspondence holds, stop there. If it must distinguish two occurrences, use that pattern's identity rule with `A.6.REL`. If no current pattern supplies the predicate and identity rule, return `missing-governor` through `A.6.RCD` while keeping the element, represented object or claim content, and needed sentence visible. A changed representation form, lens-use account, or preservation or loss claim does not by itself change an actual correspondence occurrence. | the pattern that supplies the correspondence predicate and identity rule, with `A.6.REL` only when occurrence distinction is required; otherwise `A.6.RCD`; `C.29` governs only the separate representation/correspondence claim |
| claim-bearing lens-use, preservation, or loss-account episteme | If the selected representation, represented object or claim content, `LensMappingMode`, `PreservedStructure`, `LostStructure`, declared lens use, blocked overread, stop condition, EntityOfConcern, or effective reference scheme changes the claim content, name another episteme. Recheck the correspondence occurrence and any world-side claim separately. A changed display form alone does not establish a changed lens-use or loss claim. | `C.2.1` and `C.29` |
| direct Bridge occurrence | Name the local-sense endpoints and write the Bridge sentence the next task needs. Use only a pattern that states that direct predicate. If the task only needs to know whether the Bridge holds, stop after testing the predicate. If it must distinguish occurrences, use that pattern's identity rule and say whether one occurrence began, continued, or ceased, or whether another occurrence exists. A new Card, direction statement, `CL`, loss note, licence, evidence item, or publication does not by itself change the occurrence. | the pattern that states the direct Bridge predicate and identity rule; if none exists, `A.6.RCD` |
| Bridge description or Bridge Card episteme | If Bridge kind, direction, `CL`, loss, admitted use, substitution licence, or EntityOfConcern content differs, name another episteme. Keep revision Work, the later episteme, any edition or refinement relation, evidence, and publication separate. Do not report a changed Bridge occurrence unless its predicate or identity rule says so. | `C.2.1`; `F.9` for Bridge-description content |

The object in the first column controls the operation and continuity test. `Revision` may name an activity family; one actual revision is one exact dated `W : U.Work` occurrence under `A.15.1`. If `S : U.System` performed it, recover the exact obtaining `RA : U.RoleAssignment`, check that `S = RA.HolderSystemSlot`, and state `S performed W under RA` or `performedUnderAssignment(W, RA)` under `F.6`. The revised episteme output is a separate object; performing the revision does not let an identity-bearing episteme change in place. A shared title, sequence, identifier, or authoring intention does not establish an edition, refinement, or supersession relation. If none of the identifying facts for the selected row changed, do not invent a change claim.

#### A.6.P:4.8 - Preserve polarity and inverse meaning

Participant order is part of many relation predicates. `Bearing_B isPartOf Pump_P` and `Pump_P hasPart Bearing_B` can be paired as inverse readings only when that inverse law is declared under the direct parthood pattern. A symmetric relation is symmetric under its direct law, not because a sentence sounds reciprocal.

When two viewpoints use different readable directions:

1. keep the same participant referents and their exact kinds;
2. name the forward predicate selected by the direct pattern;
3. use an explicit inverse predicate or inverse reading when one is available under that pattern;
4. keep scope, time, viewpoint, and reference scheme fixed while checking equivalence;
5. treat a change of participant kind or predicate as a semantic change rather than a stylistic rewrite.

#### A.6.P:4.9 - Use an actionable guide and keep a small candidate note when grounding is unresolved

For each ambiguity cluster, guide the reader through this order:

> trigger expression -> candidate grounded objects and direct relations -> discriminating observations or tests -> readable direct-relation rewrite -> only the additional declaration, assertion, occurrence, designation, or representation needed by the named receiver -> exact governing exit

Do not organize the guide as a synonym list or make a table field the ontology. A qualifier such as `comparative`, `safe`, `interactive`, or `reliable` narrows wording but does not restore the head kind by itself.

When grounding remains unresolved, use this informative temporary episteme. The prompts are not a reusable schema or tuple kind.

| Question | What to write |
|---|---|
| Which wording is unresolved? | quote the phrase whose head, participant, predicate, or qualifier is unresolved |
| Which distinction is unresolved? | name the exact question about head kind, participant referent, direct relation kind, direction, or qualification |
| Which grounded alternatives remain? | name candidate objects, kinds, or direct relations, not synonyms |
| What separates the alternatives? | name the observation, claim, identity test, or direct-pattern condition |
| What reading is selected now? | write the selected objects and direct relation, or state that the distinction remains unresolved |
| What changes after selection? | write the readable sentence, optional declaration need, occurrence-identity need, assertion or representation need, or neighboring-pattern exit |

For `Alice is at the table`, the physically present place and participation in a meeting are both plausible only while local evidence leaves them open. A location observation selects a located-at relation. A meeting roster and role assignment may instead select participation in meeting work. The note does not combine those relations and does not infer a role from a place expression.

When alternatives remain unresolved, the note may support explanation only. It cannot justify a decision, mechanism gate, publication claim, assurance, reliance, or cross-context reuse. Before stopping, name the reader, decision, or work that is blocked and name the observation, test, or direct-pattern condition that would separate the alternatives. Continue only after that discriminator selects one grounded reading; otherwise keep the alternatives explicit and keep the named use blocked.

#### A.6.P:4.10 - Classify boundary claims and keep engineered rewriting epistemic

Use `A.6.B` only when a sentence at the boundary does at least one of four things: defines a truth-conditional relation or signature rule (**L**); decides whether one identified mechanism application may start or continue (**A**); assigns a duty to an accountable actor (**D**); or states which execution effect or evidence can be observed and under which conditions (**E**). A sentence about claim scope or use, when to start or stop A.6.P, how to correct an endpoint kind, or whether a Bridge is needed does not qualify merely because it limits the repair.

Before giving a sentence an **A** label, answer two questions: Which mechanism application is about to start or continue? What predicate is checked at that point to admit or reject it? If either answer is missing, do not label the sentence **A**. Keep its scope or use, A.6.P start or stop decision, endpoint-kind correction, and Bridge need with the patterns that govern those questions. Split any mixed sentence before classifying its claims:

- **L** states the direct relation semantics, declaration invariants, polarity, participant meanings, and any reusable `SlotSpec` typing;
- **A** states one predicate checked when an identified mechanism application starts or runs. Its result says whether that application is admitted, may continue, or is rejected. A condition does not become **A** merely because it limits a claim, tells an author when to enter or stop this pattern, asks for an endpoint-kind correction, or requires a Bridge;
- **D** states duties of accountable systems or role assignments and does not turn a declaration into an actor;
- **E** states work and evidence expectations, witness carriers, observation conditions, and freshness under their direct owners.

Scope, `Γ_time`, viewpoint, reference scheme, witnesses, admissible use, and non-admissible overread stay with the direct relation or claim that actually needs them. They are not a universal qualifier kit, and an `admissible use` sentence is not an **A** claim unless the reader can point to both the mechanism application and its runtime entry predicate.

If a later task must describe an engineered episteme operation, first identify input `X` and output `Y` independently under `C.2.1`. A difference in claim content, EntityOfConcern, or effective reference scheme identifies another episteme; no component is rewritten in place. Keep the operation separate from `X` and `Y`. Use `A.6.3` only for an exact compatible viewing or construction case: its entry must accept independently identified `X` and `Y` about the same exact EntityOfConcern, and its result must state the construction, preservation and loss, and applicability without substituting a slot/ref record for the operation. This edition does not route to `A.6.2` or `A.6.4`: their current bodies still describe component-slot rewriting and retargeting by replacing `EntityOfConcernSlot`. When the needed operation is morphing or retargeting, stop with `X`, `Y`, the changed EntityOfConcern if any, and the sentence the next task needs; name `A.6.2` or `A.6.4` as the future owner that still requires a compatible repair. Call `X` and `Y` editions, refinements, or successors only when that direct continuity relation independently obtains; a shared title, sequence, or authoring intention is not enough.

If a system authors, materialises, checks, or publishes the output, that dated activity is `U.Work` under `A.15.1`; it is not the effect-free operation. Neither the operation nor that Work by itself makes the repaired world-side relation begin or cease, changes its actual participants, or supplies occurrence identity. Ordinary A.6.P repair stops before this step unless the reader's later task actually needs the operation described.

#### A.6.P:4.11 - Relax wording, then exit to the exact governor

After the relation has been recovered, Plain wording may be shorter than the Tech explanation. The shorter wording remains usable when a reader can still recover the exact participants, direct relation and governing pattern, every qualification that changes the declared use, and the point at which reusable declaration, occurrence identity, assertion detail, or representation becomes necessary.

A.6.P ends when the direct relation and participants are selected. The selected direct pattern governs that relation. Separate assertion, occurrence-identity, evidence, work, Bridge, description, publication, designation, and representation questions leave through their own patterns.

When generic relation recovery identifies one current claim at a method, intended-work, actual-work, production, evaluation, delivery, acceptance, transfer, or receiving-use boundary, apply `A.6.P.WMR`. It returns exactly one of four families:

1. an exact direct subject-relation claim, positive or governed negative;
2. an exact `A.6.1` operation-application binding;
3. a local `A.15.PROD` claim or another local relation-bearing claim selected under `A.6.RCD` disposition 2;
4. an exact non-assertability result independently reasoned as `factually unsupported`, `missing-information`, or `missing-governor`.

Only `missing-governor` is an ontology blocker, and it names the affected receiving use and future owner. When participant referents and the named receiving claim are exact but no current direct relation closes that claim outside A.6.P.WMR, exit to `A.6.RCD` rather than improvising a relation or kind.

| Recovered question | What the reader does | Governing exit |
|---|---|---|
| interface, port, signature, participant, field, parameter, or representation-position wording | Name the actual interface-side object and the direct claim needed next; keep any schema field or representation position separate from that object. | `A.6.RSIR`, then the exact direct owner |
| basedness or dependence on an explicit base | Name the dependent, base, direct base relation, scope, applicable time, witnesses, allowed use, and blocked stronger use. | `A.6.6` |
| service, server, provider, delivery, or access wording — first question | Do not choose from a closed service-facet list. Ask what concrete object the sentence is about and what the next reader must decide or do. The common branches immediately below are examples, not a `Service` kind or complete taxonomy; an unlisted but already recoverable object goes straight to its direct owner. If the referent is still unclear, return to 4.1. | `E.10` for the wording trigger, then the exact direct owner |
| service promise | Ask what outcome the consumer may rely on. Write that promise clause and its acceptance content without assigning an accountable duty or claiming that delivery work occurred. | `A.2.3`; use `A.6.C` when contract, SLA, or guarantee wording must be unpacked |
| service commitment or instituting act | Ask who is accountable for what, under which modality, scope, and time. If the question is instead whether an approval, notice, declaration, or revocation instituted or ended the commitment, identify that performed communicative act separately. A document or interface performs neither act. | `A.2.8`; `A.2.9` for the distinct speech act; `A.6.C` when contract language carries both |
| service access point or interface | Point to the endpoint, port, interface, providing system, and receiving participant needed by the sentence, then write the direct access or interface claim. Use `A.6.RSIR` only to recover which of those objects the wording names; the exact interface or access owner must supply the predicate. An API description is not the interface or access relation. | `A.6.RSIR`, then the exact direct interface or access owner; otherwise `A.6.RCD` after the objects and needed predicate are exact |
| service or API description and publication | Ask which claim-bearing episteme describes which promise, method, interface, or access object. If a selected edition was made available, state publication separately. Description or publication neither promises the outcome nor provides access by itself. | `C.2.1`; `E.17` and `E.24.PUB` when publication is current |
| other recovered service facet | Name the providing or receiving system, role assignment, method, planned or performed Work, production, delivery, acceptance, or evidence claim actually meant. Neither `service`, a `serviceSituation`, nor a bundle closes that claim. | `A.1`, `A.2`/`A.2.1`, `A.3.1`, `A.15.1`, `A.6.P.WMR`, or `A.10` as selected by the sentence; `A.6.RCD` only after an exact missing predicate is shown |
| sameness, correspondence, export, alignment, mapping, or substitution across contexts | Name what each endpoint means in its own context and write the Bridge sentence the next task needs. Shared spelling, a mapping artefact, or a Card is not evidence that the Bridge obtains. | the direct Bridge pattern for predicate and occurrence identity; `C.2.1` and `F.9` only for a separate description or Card; otherwise `A.6.RCD` after both endpoints and the needed sentence are exact |
| `integrity` wording — first question | Ask what the sentence lets the next reader do. Does it make a whole, part, structure, or coverage claim; characterize or measure something; or use evidence to support an assurance claim? The word `integrity` selects none of these branches by itself. | choose one of the three direct branches below; if evidence does not discriminate them, keep the alternatives explicit and block the named use |
| `integrity` as a characteristic or measurement | Identify the bearer and integrity characteristic. If a value is reported, also name the scale, coordinate or level, unit when needed, measurement method, result, and evidence pointer. For example, `structural integrity is measured at X` takes this branch without inventing a candidate whole or parthood claim. | `C.16.P` until characteristic and scale construction are clear, then `C.16` and the exact measurement owner |
| `integrity` as evidence or assurance | Name the exact claim, the evidence that bears on it, and the reliance or assurance use under consideration. A report called an integrity report is neither a whole nor assurance by title. | `A.10`; `B.3` only when an assurance claim is current |
| actual whole, part, structural-whole, complete, turnkey, or end-to-end claim | Only after the sentence makes a whole, part, structure, or coverage claim, point to the candidate whole and boundary, list the relevant parts or constituents, and state the direct claim. Common examples are parthood, membership, portion, phase, composition, selected structure, holon recognition, whole reidentification, work coverage, and completion; this is not a closed taxonomy. In `the assembled pump remains an integral whole`, recover that pump, its boundary, parts, selected structure, and direct owner. A `wholenessSituation`, bundle, or adjective proves none of those claims. | `A.14`, `C.13`, `A.22`, `A.1`, `B.2`, `A.15.1`, or `A.15.PROD` as selected by the claim; otherwise `A.6.RCD` after the exact missing predicate is shown |
| evidence bearing on a named claim | Name the evidence-bearing episteme or carrier, the claim it bears on, and the exact reliance or assurance use. | `A.10`, with `B.3` only when an assurance claim is current |
| method/work/result/production/delivery/acceptance wording whose exact governor is hidden | Name the exact objects and the sentence needed at the method, work, result, production, delivery, acceptance, transfer, or receiving-use boundary. | `A.6.P.WMR`, then one of its four truthful exits |
| exact participants but no current direct relation for the named receiving claim | Preserve the exact participants and sentence needed next; do not improvise a relation or kind. | `A.6.RCD` |
| one work occurrence enabling, preparing, or producing for another exact use | Name both work-side objects and the exact enabling, preparing, or producing claim; do not substitute a plan, method, or package. | `A.15.1`, `A.15.4`, `A.15.PROD`, or the direct work relation |
| an episteme assertion or description | Identify the claim-bearing episteme, its EntityOfConcern, and its effective reference scheme; keep publication separate. | `C.2.1`, then `E.17` when publication is current |
| architecture wording | Name the architecture object, scope, and claim the sentence actually makes. | `C.30.P` |
| characteristic, measurement, comparison, or quality wording | Name the bearer, characteristic, scale or comparison basis, result, and use that are current. | `C.16`, `C.16.P`, `A.17`-`A.19`, or `C.25` as selected by the actual claim |
| palette, front, archive, shortlist, or selected-set wording | Name the selected-set object and the exact selection, comparison, currentness, archive, or use claim. | `G.2`, `A.19`, `C.18`, `C.19`, or `G.5` as selected by the actual object and use |
| quantum-like relation or probe wording | First recover the ordinary direct relation; only then state the remaining probe, frame, order, export, or state-representation claim. | the ordinary direct owner first; `C.26` only for the residual quantum-like claim |
| mathematical tuple, graph, arrow, function, or other representation | Name the representation elements, represented objects or claim content, explicit correspondences, declared use, and blocked overread; keep any Bridge separate. | `C.29`; `F.9` separately for a Bridge description or Card |
| designation after ontology is settled | Recover the object and relation first, then state why one durable designation is needed. | `F.18` |
The word that triggered the repair does not govern the result. The exact direct pattern does.

#### A.6.P:4.12 - Lexical guardrails

Overloaded words are diagnostic entry points, not relation kinds. In Tech or normative prose, `same`, `synced`, `linked`, `connected`, `anchored`, `grounded`, `supported`, and similar words cannot substitute for an unnamed direct relation or claim family. `Bind` and `rebind` remain name-binding or direct-owner vocabulary and are not generic relation-change verbs. A Plain gloss is admissible when its direct reading and governing exit remain recoverable.

`E.10` owns the trigger scan and `E.10.ARCH` the shared wording-use recovery architecture. `F.18` owns durable name selection after the governed object is known. A.6.P does not maintain a second trigger registry or mint one specialization for every repeated word.

### A.6.P:5 - Archetypal Grounding

#### A.6.P:5.1 - Physical assembly and repeated occurrences

**Tell.** A maintenance note says `replacement bearing is linked to Pump_P`.

**Show.** Inspection finds that `Bearing_B` participates as the installed part and `Pump_P` as the assembly whole in the direct installed-part relation during `Interval_T`. Both remain physical holons of their independently governed kinds. `A.14` governs the parthood predicate and obtaining condition. The maintenance assertion names them directly. If no later claim distinguishes installation episodes, the repair stops at the readable sentence.

**Show the identity-dependent use.** A reliability analysis compares the installed-part relation before removal with the relation after reinstallation. The same bearing and pump can participate in two occurrences. The analysis applies the direct identity rule and `A.6.REL`, exposes the two already obtaining occurrences, and designates them separately in its assertion. Maintenance database rows and diagram edges may represent the assertion or occurrence descriptions through explicit `C.29` correspondences; row or edge identity is not physical relation identity.

When repeated maintenance assertions need one typed declaration, an `InstalledPartRelationSignature` may contain declaration-local `InstalledPartSlot` and `AssemblyWholeSlot` `SlotSpec`s corresponding to the two participant meanings. Those declaration components type the assertions' participant designations. They are not world-side places occupied by the bearing and pump.

Installation work constitutes the beginning of another installed-part occurrence only when the direct parthood identity rule says that it does. Creating or updating the maintenance row is representation work and is not an ontological constructor. The material character of the installed-part relation also does not by itself introduce a separate relator; the direct parthood ontology would have to identify and justify any constitutive truth-maker.

#### A.6.P:5.2 - Clinical evidence use and negative reliance

**Tell.** A care note says `the measurement supports the dose change`.

**Show.** The repair distinguishes the measurement work occurrence, its measurement-result episteme, the work-plan claim, the measured characteristic, the applicable range, and the exact evidence relation. `C.16` governs measurement construction and applicability; `A.10` governs whether that episteme bears on the named dose-change claim for this use. The broad predicate is not replaced by a universal support relation.

**Show the boundary.** If current evidence refutes the dose-change assertion or leaves reliance unresolved, the receiving evaluation records that posture. It does not create a negative world-side measurement, treatment, or evidence occurrence. A fresh publication of the same measurement-result episteme changes availability, not the measured condition or evidence relation by itself.

#### A.6.P:5.3 - Episteme correspondence and representation

**Tell.** Two teams say `the models are aligned`, and one tool draws an edge between their model nodes.

**Show — models.** Model epistemes `DesignModel_E` and `MaintenanceModel_E` have `EntityOfConcern` `PumpAssembly_P204` and effective reference schemes `CAD-Part-Scheme-v7` and `Asset-Register-Scheme-2026Q2`, respectively. `AlignmentEdge_17` joins nodes labelled `BRG-6204` and `bearing-4471`.

**Structure decision.** No established model-use structure changes either label's reading or whether replacement approval may use the pairing. Add no `BoundedModelUseStructure`; a diagram boundary is not evidence.

**Needed sentence.** `For bearing-replacement planning on PumpAssembly_P204, CAD-Part-Scheme-v7 label BRG-6204 and Asset-Register-Scheme-2026Q2 label bearing-4471 denote the same installed bearing.` This is a candidate claim, not yet a fact.

**Edge boundary.** Under `C.29`, `AlignmentEdge_17` represents that sentence. It does not make the sentence true, prove one referent, or identify a Bridge occurrence.

**Adjacent reading.** Record `ninety-seven percent of endpoint pairs passed the mapping test` with `C.16`. If approval relies on that measurement, `A.10` governs the evidence relation. The percentage does not establish the needed sentence.

**Result.** `A.6.RCD missing-governor`: bearing-replacement approval is blocked; participants are `BRG-6204` and `bearing-4471`; the needed sentence is above; the edge remains a representation. No current direct correspondence or Bridge pattern states when the cross-scheme claim holds. A future direct pattern must state its predicate, conditions, and, if occurrences must be distinguished, identity rule. Until then, do not assert `the models are aligned` or mint a Bridge from the edge or a Card.

**Show the boundary.** The graph edge and its endpoint positions remain representation elements. An explicit `C.29` correspondence states which assertion content, participants, and direct relation the edge represents. The edge does not make the correspondence obtain, prove same EntityOfConcern, or individuate a relation occurrence. Shared labels likewise establish neither same world-side referent nor substitutability.

When the claim is that both model epistemes concern the same world-side holon, recover each episteme's exact EntityOfConcern or grounding designation plus the observations, trajectory, or identity evidence governed for that holon. A Bridge preserves stated correspondences and losses; it does not prove the common world-side referent.

**Show the viewpoint-conformance use.** A review must decide whether model episteme `E` conforms to maintenance viewpoint episteme `P`. Identify `E` from its claim content, EntityOfConcern, and effective reference scheme, and resolve `P` as one claim-bearing viewpoint edition before reading a diagram, field, or reference as ontology. Then apply the direct predicate governed by `E.17.0`: `EpistemeViewpointConformanceRelation(E,P)`. Plainly, `E` conforms to this exact viewpoint.

For unchanged `E` and `P`, the pair `<E,P>` determines one positive occurrence. Selecting `P` for this review is a separate use qualification: selection neither makes conformance obtain nor enters occurrence identity. If another review selects `P2`, test `<E,P2>` instead of retagging `E`. A `viewpointRef` or diagram label does not identify either participant by itself. A query, transformation, or projection may supply construction history for `E`, but neither that history nor an assertion, evaluation, representation, or publication makes conformance obtain.

Add an occurrence designator only if the next decision must distinguish two conformance occurrences. Add an evaluation result or evidence path only if the reader must rely on the conformance verdict. Add construction history only if the task asks how `E` was produced; add a representation or publication only if another reader must inspect or receive it; add associated Work only if the task asks who performed which activity. Otherwise add none of these objects. A.6.P stops after recovering `E`, `P`, and the direct relation; `E.17.0` governs the predicate and, if the use separately asks whether an episteme is a `U.View`, that recognition.

#### A.6.P:5.4 - Method, work, role, and agency

The sentence `the inspection method checks Pump_P` uses active grammar. The repaired ontology says: one exact `RA : U.RoleAssignment` obtains under `A.2.1` with four actual participants—admitted `System_S` as holder, `InspectorRole`, `InspectorRoles_2026 : U.Episteme` as the role-taxonomy episteme, and `InspectionReferenceScheme : U.ReferenceScheme` as the effective scheme. `F.6` then states that `System_S` performed `InspectionWork_W` under `RA` (`performedUnderAssignment(InspectionWork_W, RA)`); `InspectionWork_W` applies `InspectionMethod_M`; and the direct examination relation connects the work occurrence to `Pump_P`. The example names the assignment participants but does not duplicate its interval or full assignment card. Each object keeps the identity and relations of its direct pattern. Only the holder system acts; the assignment does not.

#### A.6.P:5.5 - Formal reduced case

`3 < 5` is assertion content in mathematical notation. The numeral occurrences, comparison sign, and operand places are representation elements under `C.29`. An explicit correspondence can relate them to the values, direct less-than predicate, and any compatible declaration used for typed reuse. No receiving use here distinguishes one obtaining occurrence from another, so the engineer stops at the assertion. A graph edge, tuple, or statement reifier introduced by a tool represents the proposition or assertion; it does not constitute the direct relation.

### A.6.P:6 - Bias-Annotation

This pattern favors ontology-first recovery, direct relation sentences, and the lightest explicit form that serves the named receiving use. That bias counters record-first and vocabulary-first repair.

The counter-risk is under-specification: an engineer may stop before a load-bearing participant, applicability condition, occurrence identity, or reference is exposed. The receiving-use test, hidden-arity check, three-way relation-dependent wording distinction, and neighboring-pattern exits provide the counterweight.

The pattern also favors neutral domain language. Examples span physical assembly, clinical work, epistemes, roles, methods, and formal relations so that one publication technology or professional tradition does not become the default ontology.

### A.6.P:7 - Conformance Checklist

1. **Recognition.** The use begins with one actual relation-bearing claim and states which later claim or operation is blocked by its ambiguity.
2. **Grounded heads.** Every load-bearing head refers to an exact object or remains explicitly unresolved; a qualifier does not substitute for the head kind.
3. **Direct relation.** Every positive or governed-negative direct subject-relation exit names exact actual participants, an explicit admitted `RelationKind` token, and the direct governing pattern. The A.6.P.WMR non-relation exits remain under their exact owners.
4. **Participant meanings.** The direct pattern states the participant meanings, actual participation, obtaining predicate, applicability, and occurrence-identity rule; every participant retains its independently governed kind.
5. **No negative occurrence.** Negative assertion, refutation, or unresolved reliance remains claim- or evaluation-side and creates no negative world-side occurrence.
6. **Demand-driven declaration.** A compatible `RelationSignature` and declaration-local `SlotSpec`s appear only when reusable typed use is current; an ordinary assertion may name participants directly.
7. **Designation separation.** A participant designation or occurrence reference remains content of a receiving episteme and neither replaces the referent nor makes the relation obtain.
8. **Hidden arity and qualifiers.** Every participant or qualifier included in the repair changes predicate satisfaction, applicability, identity, substitution, interpretation, admissible use, witness needs, or the named later claim or operation.
9. **Occurrence threshold.** Explicit `U.Relation` identity appears only when a named receiver needs one occurrence distinguished from another; repeated occurrences with the same participants use the direct identity discriminator.
10. **Construction choice.** When construction is identity-bearing, the direct owner names the constructor, inputs, construction work or process, and identity contribution; otherwise the repair introduces no constructor.
11. **Object separation.** Direct relation kind, participant meaning, actual participant, declaration, assertion, occurrence description, occurrence, designator, reference, publication, Bridge, and representation remain distinct where present.
12. **Relation-dependent wording.** The reading resolves to world-side actual participation, an assertion- or description-side designation, or a justified C.3 local kind; no fourth qualification object is introduced.
13. **Polarity.** Participant order, inverse wording, symmetry, assertion polarity, and temporal qualification follow the direct relation law.
14. **Changed object.** Every change statement selects one exact changed object and its governing row in A.6.P:4.7; no generic relation-edit operation remains.
15. **Boundary classification.** Apply L, A, D, and E only to an actual A.6.B boundary statement. Before marking **A**, point to the particular mechanism application and the predicate checked at entry; if either is absent, leave claim use or scope, A.6.P entry or stop, endpoint-kind correction, and Bridge need with their own patterns.
16. **Candidate guide and stop.** Unresolved alternatives are grounded objects, kinds, or relations with a discriminating check, not a synonym list or representation-first ontology. Until the check selects one reading, the note remains Plain or informative, names the blocked reader, decision, or work and the needed discriminator, and carries no decision, gate, publication, assurance, reliance, or cross-context reuse.
17. **Representation boundary.** A table, row, field set, tuple, graph edge, functional expression, arrow, formula, or reifier has explicit `C.29` correspondence for any relied-on FPF use and does not constitute the represented relation by form.
18. **Optional episteme operation.** Use this path only when a later task must describe an operation on an episteme or representation. Identify input and output independently under `C.2.1`; use only an exact compatible `A.6.3` viewing or construction case, keep any continuity relation separate, and use `A.15.1` for actual authoring, materialisation, checking, or publication Work. Do not route from this edition to the current slot/write profiles in `A.6.2` or `A.6.4`; for morphing or retargeting, preserve the exact input, output, changed EntityOfConcern if any, and needed sentence as the explicit future-owner stop. Neither an operation nor that Work by itself changes the repaired world-side relation or supplies occurrence identity.
19. **Plain relaxation.** Short final wording retains a recoverable direct relation, actual participants, and visible escalation points.
20. **Neighbor exit.** The repaired claim leaves A.6.P through one exact governing exit in A.6.P:4.11, including exactly one of the four A.6.P.WMR families when that specialization is current.

### A.6.P:8 - Common Anti-Patterns and How to Avoid Them

| Failure mode | Why it fails | Repair |
|---|---|---|
| Replace a broad word with a more technical synonym | The same participants and obtaining condition remain unresolved. | Ground the objects, select the direct relation, and write the readable sentence before naming. |
| Turn every relation phrase into a record-shaped episteme | Representation burden appears before any receiver needs the episteme or occurrence identity. | Return to the direct sentence and apply the `A.6.REL` receiving-use test. |
| Let the declaration make the relation obtain | A declaration episteme is confused with the world-side relation. | Keep reusable laws and `SlotSpec`s in `A.6.0` and `A.6.5`; keep obtaining and identity with the direct owner. |
| Treat the actual participant as occupying a declaration component | World-side participation is replaced by a schema metaphor. | State participation under the direct participant meaning; use the `SlotSpec` only inside a compatible reusable declaration. |
| Treat relation-dependent wording as an intrinsic kind | A participant described as result, input, or next continuation loses its own kind. | Apply the three-way distinction and use C.3 only for actual typed reasoning. |
| Use one generic relation-change verb | Occurrence change, assertion revision, declaration revision, evidence change, designation retargeting, and representation change collapse. | Select the changed object and use the operation governed for that object. |
| Infer agency or identity from an active verb | Grammar is treated as ontological evidence. | Recover the exact acting system or direct identity rule independently of grammar. |
| Preserve a hidden union as a long list | The predicate changes meaning across listed participant kinds. | Recover the common predicate or split the relation kind and any compatible declarations. |
| Reverse a sentence for style | Participant meanings and polarity can change silently. | Use the direct inverse law or keep the forward predicate explicit. |
| Use a graph, tuple, function, arrow, or table as ontological proof | Representation is mistaken for what it represents. | State an explicit `C.29` correspondence and keep world-side obtaining and identity with the direct pattern. |

### A.6.P:9 - Consequences

**Benefits**

- Engineers can retain short practical relation language without surrendering exact ontology.
- Hidden participants and kind collapses become repairable through one repeatable sequence.
- Reusable declarations, occurrence identity, designations, and representations appear only for named receiving uses.
- Assertion, declaration, occurrence, evidence, designation, publication, Bridge, and representation changes remain independently reviewable.
- Neighboring patterns receive the object they actually govern rather than a generic container.

**Costs and mitigations**

- Grounding an ambiguous phrase takes more work than lexical replacement. The first useful move and small candidate note keep that work bounded.
- Some claims become longer when their truth depends on scope, time, viewpoint, witness, or another participant. Plain relaxation restores readability after the precise reading is stable.
- Domain-specific direct relation patterns still need their own obtaining and identity rules. A.6.P supplies recovery and governing-pattern selection, not a universal relation ontology.

### A.6.P:10 - Rationale

The problem is ontological before it is lexical. A broad expression is dangerous because it can hide different objects, predicates, participant meanings, actual participants, or later claims and operations. Replacing the expression without recovering those objects merely moves the ambiguity.

FPF therefore begins with relation realism: a relation may obtain independently of an assertion about it. Actual participants retain their independently governed kinds while participating under relation-local meanings. An optional `RelationSignature` makes those meanings reusable as typed declaration content; an assertion or description can designate participants or an already recoverable occurrence; a representation corresponds to the selected object or claim content. None of those adjacent objects substitutes for world-side obtaining or identity.

Construction matters only when the direct ontology makes it identity-bearing. In that case, constructor, inputs, construction work or process, and output identity explain how another occurrence begins. Other relations may obtain without such a constructor. A.6.P therefore uses constructional analysis as a discriminating test rather than as a universal ontology.

Progressive elaboration preserves affordability. An engineer can stop at a readable direct fact. Typed declaration, assertion detail, occurrence identity, stable references, descriptions, publications, and representations appear only when a named later claim or operation depends on them. This order also explains why naming comes late: a good name helps designate a recovered distinction but cannot create it.

The changed-object rule prevents a second ontology collapse. Revising an assertion, declaration, evidence relation, designation, reference, publication, Bridge, or representation is not automatically a change in the direct relation being discussed. Naming the changed object makes continuity, evidence, and return conditions intelligible.

Neutral terminology matters because A.6.P is cross-domain. Every object named by the method remains under its direct governing pattern; A.6.P does not collect unlike objects under one local umbrella. Domain-specialized vocabulary enters only when a direct local pattern governs the current object.

### A.6.P:11 - SoTA-Echoing

#### Ontological SoTA and constructive grounding

These sources constrain relation occurrence, identity, and construction. They are not interchangeable: FPF takes constructor-and-input discipline from the constructional-ontology line, uses BORO as a distinct 4D comparison, and treats implementation ontologies as stress comparators rather than proof.

| Ontological source and status | What it contributes | FPF adoption, mutation, and practical effect |
|---|---|---|
| Florio and Linnebo, [Introduction to Constructional Ontology](https://www.utwente.nl/en/eemcs/fois2024/resources/papers/florio-linnebo-introduction-to-constructional-ontology.pdf), 2024 | Separates constructors, constructor inputs, and constructional process, and examines functional and relational ways to characterize construction and output identity. | **Adopt the discriminating construction test.** Recover constructor, inputs, process, and identity only when the direct relation ontology makes construction constitutive. A storage operation is not thereby an ontological constructor. |
| Borgo and Righetti, [Towards Applied Constructional Ontology](https://doi.org/10.3233/FAIA250480), 2025 | Tests how constructional analysis can expose conceptual, structural, completeness, and consistency choices while marking unresolved application questions. | **Adopt as improvement pressure, not an imported ontology.** A.6.P exposes the exact construction and identity choice whenever it changes occurrence identity. |
| Partridge, [BORO Ontology](https://borosolutions.net/boro-ontology), C-FORS 2025 presentation | Presents BORO as a 4D extensional, category, and constructional ontology with an evolution method. | **Use as an ontological comparison under an explicit boundary.** A.6.P may use temporal extent when the direct identity rule needs it; FPF does not import universal 4D identity, unrestricted composition, or BORO's category architecture. |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint | Provides a foundational-ontology implementation with differentiated relation and reification patterns. | **Use the distinctions as a comparator; do not treat the implementation as proof.** Direct relation, optional explicit occurrence, assertion, and representation remain separate without importing the source category hierarchy. |
| [OntoUML Relator](https://ontouml.readthedocs.io/en/init-ontouml/classes/sortals/relator/index.html), specification lineage | Models a relator as a dependent truth-maker whose existence connects participants in a material relation. | **Retain as a material-relation comparator, not a universal answer.** The physical case requires the direct parthood ontology to identify and justify such a truth-maker before a relator is introduced; formal and other relations receive none by analogy. |
| Andrei Rodin, [Venus Homotopically](https://philsci-archive.pitt.edu/12116/), 2016 | Shows that identity across presentations is not obtained from a shared label alone; background, observations, and a trajectory can establish the same world-side referent. | **Retain as constructive-grounding lineage.** Candidate referents are separated through observations, identity tests, and direct-pattern conditions; naming does not close ontology. |

#### Representation and implementation stress tests

These sources do not decide what exists. They test whether a representation can preserve the ontological distinctions selected above without turning a statement, row, graph term, tuple, or reifier into the world-side occurrence.

| Representation or implementation line | Distinction tested | Bounded use in A.6.P |
|---|---|---|
| [TypeDB 3.x `links` statement](https://typedb.com/docs/typeql-reference/statements/links/) and current relation model | A query can select an explicit relation variable with named source-language role players, while shorthand remains available when no reference to the represented item is needed. | **Test progressive explicitness, not ontology.** A.6.P makes explicit occurrence identity conditional on a named receiver. TypeDB demonstrates one implementable representation; it does not establish the FPF relation kind, actual participation, obtaining condition, or identity rule. |
| [RDF 1.2 Concepts](https://www.w3.org/TR/rdf12-concepts/), Candidate Recommendation Snapshot, 7 April 2026 | RDF distinguishes proposition expressed by a triple term, assertion of a triple, and reifiers used for further statements. | **Test proposition, assertion, and reifier separation.** A statement term or graph edge can represent claim content but cannot establish that the direct relation obtains. |

The first table governs the ontological moves. The second checks representability only after those moves have been selected. The physical, clinical, episteme, work, and formal cases test that the resulting method is not specialized to information systems.

**Reopen the smallest affected passage.** Start with the one claim, case, exit, or source row that uses the changed fact. Reopen it when its governing pattern changes who participates, when the relation obtains, or how an occurrence is reidentified; when newer source evidence overturns or narrows the construction or reification distinction used there; or when an actual use can no longer reach the practical result or stopping boundary promised by that passage. Do not reopen the whole pattern unless the same change reaches several passages. If an exit no longer matches its owner's entry and result, stop using that exit until it is repaired.

### A.6.P:12 - Relations

- The direct relation pattern governs obtaining, predicate satisfaction, and the occurrence-identity rule. After A.6.P recovers that relation, `A.6.REL` governs demand-driven explicit individuation, application of that identity rule, and occurrence-as-participant use.
- `A.6.0` governs `U.Signature` and compatible `RelationSignature` declarations; `A.6.5` governs declaration-local `SlotSpec`, `SlotKind`, participant `ValueKind`, and receiving-episteme designation mode.
- `A.6.RSIR` selects among direct participation, declaration, operation, assertion or description, and representation when interface, role, slot, field, parameter, or endpoint wording is the entry cue.
- `A.6.B` separates L, A, D, and E claims after the direct relation is recovered. When the next task explicitly needs an operation on an episteme or representation, identify its input and output independently under `C.2.1`; use `A.6.3` only for an exact compatible viewing or construction result, and `A.15.1` for actual authoring, materialisation, checking, or publication Work. Current `A.6.2` and `A.6.4` are not exits from this edition because their slot/write profiles fail that compatibility test; keep them as named future owners for the explicit morphing or retargeting stop. Assert an edition or successor relation only after its own predicate is satisfied. Ordinary A.6.P repair stops before these objects.
- `A.6.6` provides specialized recovery for basedness. Service, cross-context, and whole-part wording use the object tests and owner exits in 4.11. Before routing to `A.6.8`, `A.6.9`, or `A.6.H`, check that its entry accepts the objects named in 4.11 and that its result returns the direct predicate and participants or an explicit blocker. If either check fails, do not use that specialization; stay with the 4.11 exit and its current direct owner. A situation record, Card, or bundle does not replace the direct relation, claim-bearing episteme, or representation.
- `A.6.P.WMR` governs its method, work, result, production, delivery, acceptance, transfer, and receiving-use boundary and returns one of the four results listed in 4.11.
- Use `A.6.RCD` after the reader can name the participants and the sentence the next task needs, but no current pattern supplies its predicate. Broad wording alone is not a `missing-governor` result.
- `C.2.1` governs assertions and descriptions. A.6.P identifies one candidate episteme `E`, one viewpoint episteme `P`, and the conformance question; `E.17.0` tests `EpistemeViewpointConformanceRelation(E,P)`. If the next task also asks whether `E` is a `U.View`, `E.17.0` handles that recognition separately. Viewpoint selection, evaluation, construction, representation, and publication do not establish conformance; `A.10` governs reliance, while `E.17` and `E.24.PUB` govern publication.
- Use `C.3` and `C.3.1` only if the next claim must quantify over a locally defined participant set, test membership or substitution, or order kinds. Otherwise do not mint a local kind.
- `A.1`, `A.2`, `A.2.1`, `A.3.1`, `A.3.4`, and `A.15.1` govern the direct criteria for systems, roles, role assignments, methods, actual bounded change, and work.
- `A.10` governs evidence relations and `B.3` assurance. `F.9` governs Bridge-description or Bridge Card content and its admitted cross-context use; it does not supply the separate direct Bridge predicate, obtaining condition, or occurrence identity. Use only a pattern that states that predicate and identity rule. If none exists after both endpoints and the needed sentence are explicit, return `missing-governor` through `A.6.RCD`. `C.30.P` governs architecture wording, `C.16.P` characteristic wording, `G.2` palette/front/archive distinctions, and `A.6.F` function-like wording. Each direct domain pattern governs its recovered relation.
- `A.16.1` and `B.4.1` retain cue material that has not reached a grounded relation-bearing claim; `B.5.2.0` carries a stabilized open explanatory question that has no selected relation answer; `A.16.2` records reopen, backoff, or respecification when a published relation overstates articulation, closure, or framing. Use `A.16.0` only when lineage, branching, loss, or responsibility-transfer history itself must be published.
- `E.10` governs wording triggers and `E.10.ARCH` shared recovery architecture. `F.18` governs designation after objects and relations are recovered.

### A.6.P:12b - C.29 mathematical-lens account and representation boundary

`C.29` governs a declared mathematical-lens-use account or representation only when a mathematical object, tuple, graph, function, arrow, table, or other formalism is used for a stated subject and purpose. It owns the candidate mathematical object designation, mapping mode, explicit correspondence, preserved structure, lost structure, declared use, blocked overread, and stop condition. It does not assert world-side participation, make a direct relation obtain, admit its kind, or supply occurrence identity.

When a sentence claims cross-context meaning, export, correspondence, or substitution, first name what each endpoint means locally and write the Bridge predicate being asserted. The direct Bridge owner decides whether that predicate obtains and whether one occurrence continues; `F.9` and `C.2.1` govern the separate Bridge description or Card episteme and its direction, `CL`, loss, and admitted-use claims. A changed Card, evidence item, or publication is not a changed Bridge occurrence. Use `C.29` only when the reader relies on a representation or mathematical-lens account; a representation does not establish the Bridge or the represented world-side relation. If the sentence needs no cross-context correspondence or substitution claim, add no Bridge. If it does need one but no current pattern supplies the predicate or identity rule after the endpoints are named, return `missing-governor` through `A.6.RCD`.

### A.6.P:End

