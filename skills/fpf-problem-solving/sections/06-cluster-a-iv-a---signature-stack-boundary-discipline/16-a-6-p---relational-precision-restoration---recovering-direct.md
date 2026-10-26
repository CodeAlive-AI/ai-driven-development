## A.6.P - Relational Precision Restoration - Recovering Direct Relations from Under-Specified Claims

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain name.** Relation precision restoration.

### A.6.P:1 - Problem frame

**Use this when.** Use this pattern when a claim contains a relation-bearing phrase, but the phrase does not yet determine the direct relation, exact participants, direction, or detail needed by a later engineering claim or operation. Common recognition moments include a broad predicate such as "linked", "aligned", or "supports"; a participant named by metonymy; a qualifier that sounds precise while leaving the head kind unknown; service, server, provider, delivery, access, or bare *role* wording that leaves the promise, interface, System, system-role kind or assignment, direct participation, Method, Work, or evidence object unclear; whole, part, complete, turnkey, or end-to-end wording that leaves a candidate whole, boundary, parthood, composition, coverage, or Work claim unresolved; and `integrity` wording that still leaves open whether the sentence is about a structural whole, a characteristic or measurement, or evidence or assurance. When bare *role* is the trigger, use E.10.ROLE to recover the intended branch before applying A.6.P to a direct relation claim.

Quoted, external, or ordinary source prose may remain as written. Use A.6.P only when an FPF statement will use the phrase to guide action, justify a decision or gate, support assurance or reliance, publish a claim, or reuse it in another named source, practice, or model-use setting. Repair that receiving FPF statement; preserve the source wording as a quotation or source expression instead of rewriting it as though the source had made the repaired claim.

**Primary working reader, viewpoint, and concern.** The working reader is an engineer viewing the sentence as input to a later claim or operation. The concern is that another person can find the same world-side or episteme-side objects, find the same pattern that defines the relation or constrains the operation, and know which additional declaration, assertion, occurrence, designation, or representation detail that later use actually needs.

**Primary EntityOfConcern.** One relation-bearing claim in an episteme whose current expression leaves the direct relation kind or one or more actual participants unresolved, or leaves unclear whether a later claim or operation needs reusable declaration, explicit occurrence identity, designation, or representation.

**First useful move.** Replace the broad phrase with one readable sentence that names the exact participants and the direct relation believed to obtain. Name the pattern that defines that relation's participants, obtaining condition, and identity rule. If either the participants or the relation remain genuinely ambiguous, keep a small working candidate note and resolve that ambiguity before adding a reusable declaration, assigning a designator, or choosing a representation.

**First-minute result.** The draft `Bearing_B is linked to Pump_P` becomes `Bearing_B is part of Pump_P during Interval_T` after inspection establishes the intended parthood claim under the applicable A.14 rule. The ordinary repair stops there. If a later maintenance claim must distinguish installation episodes, §5.1 returns the missing installed-part predicate and occurrence-identity rule; a `RelationSignature`, occurrence reference or graph representation cannot supply them.

**What goes wrong if missed.** A lexical replacement can make the sentence sound technical while preserving the same ambiguity. At the opposite extreme, an engineer can turn every relation phrase into a record-shaped episteme and then confuse that episteme, a declaration, or an identifier with the relation that obtains. Both failures obscure what is true, which object changes, and which pattern defines or constrains the needed claim or operation.

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

**Local RPR mantra.** *Name the referents. State the direct relation or comparison with its participants and use the pattern that defines it. Add a declaration, occurrence identity, designation or representation only when the receiving claim needs that contribution. For a change claim, identify what changed and apply its continuity rule. Then shorten without hiding the relation or its participants.*

`Referents` means the objects recovered in 4.1; it is not a shared kind. `Comparison` means the direct comparison relation governed by `A.19.CPM`. `Actual participants` means the independently governed entities that participate under the relation's participant meanings. The mantra does not ask the reader to fill slots or positions or to create a record.

Sections 4.1–4.12 develop the same repair: resolve participants and hidden arity, preserve polarity, separate facts from assertions and representations, and stop at the sufficient readable claim. The additional branches are selected by the receiving use.

#### A.6.P:4.1 - Recover the objects before choosing relation notation

Start from the claim as written and ground each load-bearing head:

1. Identify the exact referent intended by each participant expression.
2. Recover the participant kind required by the direct predicate. State that classification explicitly when it changes interpretation or the receiving use, using its applicable admission rule.
3. Separate a world-side object from an episteme about it and from a publication or representation of that episteme.
4. Recover metonymy explicitly. The phrase `at the table` may state physical location or participation in a negotiation meeting. Evidence from the current case selects the direct relation; neither reading by itself establishes a local system-role kind or system-role assignment.
5. Leave the claim unresolved when the current evidence does not select one referent. A more technical synonym is not a repair.

The result of this step is an ordinary sentence containing identifiable objects. It is not a newly minted object kind. When several candidates remain live, use the small working note in A.6.P:4.9.

Copying an expression such as “my left” or “our project” into another participant's instruction can change its referent. Use `A.6.P.RI` when the receiving use still needs to establish whose reference is intended, what must remain the same, or which performer is to act. The result is a usable interpretation or instruction, or a specific missing condition. When those references and the task are already clear, use ordinary clarification or the relevant domain transformation; A.6.3.RT governs a needed change of representation scheme while the EntityOfConcern stays the same.

If the material is still a cue and no relation-bearing claim can yet be stated, stay with `A.16.1` or `B.4.1` instead of forcing relation publication. If the cue has stabilized into an open explanatory question but still has no selected relation answer, use `B.5.2.0`.

If counter-evidence or a failed use shows that a published relation statement overstates its articulation, closure, or framing, use `A.16.2` to reopen, back off, or respecify that publication. `A.16.2` records the retreat; A.6.P repairs the relation again only after the engineer can name a grounded candidate relation, its participants, and a discriminating check. Use `A.16.0` only when readers must see lineage, branching, loss, or responsibility-transfer history; a local return needs no trajectory account.

A.6.P begins when the available observations or claims let the engineer name at least one grounded candidate relation, its participants, and a discriminating check.

#### A.6.P:4.2 - State the direct relation, participant meanings, and obtaining condition

Write the smallest readable direct-relation sentence that answers the current question:

```text
<actual participant 1> <direct relation predicate> <actual participant 2> ...
```

Then name the pattern that defines or constrains the direct relation and recover from it:

- the admitted direct relation kind and its governed `RelationKind` token; the token designates that kind but is neither the kind nor an occurrence;
- the relation-participant meanings and actual participants, each retaining its independently governed kind;
- the condition under which the relation obtains and its semantic predicate is satisfied by those participants considered under the participant meanings;
- applicability, direction, symmetry, inverse law, polarity, and temporal qualification when they change the predicate;
- the occurrence-identity rule, whether or not the current use needs explicit individuation;
- when the direct ontology says that a new occurrence is constructed or constituted, the constructor, inputs, construction work or process, and their contribution to occurrence identity.

Every in-scope positive or governed-negative direct subject-relation result names an explicit admitted `RelationKind` token. When no suitable token exists, first settle the relation value and any required relation-kind admission using the pattern that defines them, `A.6.RCD`, and `E.24`; then apply `F.8` and, for durable naming, `F.18` and `F.17`. Naming does not admit a kind or occurrence. An exact `A.6.1` operation-application binding, local `A.15.PROD` or `A.6.RCD` claim, or non-assertability result keeps the semantics defined for that operation, production, or missing-relation claim and is not coerced into this relation-kind family.

An ordinary assertion may name the actual participants directly. When reusable typed use is current, a compatible `RelationSignature` declaration can restate the participant meanings, obtaining predicate, applicability, and identity rule and contain only the declaration-local `SlotSpec`s needed by the receiving typed uses. The declaration remains an episteme; it neither makes the relation obtain nor supplies occurrence identity.

Assertion polarity remains claim-side. An affirmative assertion claims that the direct predicate is satisfied; a negative assertion denies it. Refutation or unresolved reliance belongs to `A.10` or the receiving evaluation. Denial, refutation, or unresolved reliance creates no negative world-side occurrence.

Do not select ontology from grammar. A verb-shaped phrase supplies neither constructive identity nor agency. Use the pattern that defines, constrains, or tests the relation, object, Work, Method, change, local system-role kind, system-role assignment, or admitted System named by the current claim.

#### A.6.P:4.3 - Recover actual participants, hidden arity, qualifiers, and typed declaration only when needed

Ask which actual participation belongs to the direct relation's obtaining condition. Add a participant or qualifier only when it changes one of these:

- predicate satisfaction or relation obtaining;
- applicability or admissible use;
- occurrence identity;
- whether one participant can replace another without changing the claim;
- interpretation under an effective reference scheme;
- scope, `Γ_time`, viewpoint, view, or another exact qualification defined by the direct relation or receiving claim;
- witness or evidence expectations for a named decision or publication use;
- the exact later claim or operation.

For `Sample_S wasMeasuredBy Instrument_I`, a later evidence claim may separately refer to the measurement work occurrence, its interval, the applied measurement method, a measurement-result episteme, and a calibration episteme. The measured-by relation includes only the actual participants selected by its direct obtaining condition; the other objects remain participants or content of their own work, evidence, temporal, method-use, measurement, assertion, or description relations.

When reusable typed use is current, declare each participant meaning needed by that use through A.6.5:

```text
SlotSpec := <SlotKind, ValueKind, refMode>
```

One `SlotKind` names one participant meaning locally inside one exact `RelationSignature`. `ValueKind` states the independently governed kind of the corresponding actual participant. `refMode` states how a receiving assertion or occurrence-description episteme designates that participant. The `SlotSpec` is declaration content; the participant does not become or occupy that declaration component. If one proposed `ValueKind` hides objects for which the predicate has different meaning, recover a real common kind or split the direct relation kind instead of preserving a hidden union as a prose list.

#### A.6.P:4.4 - Keep world-side, declaration, assertion, designation, and representation objects distinct

| Object | Engineering question | Defining or constraining rule |
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
| representation element | Which mark, field, edge or expression represents which object or claim content, under which conventions? | the selected representation scheme and its governing pattern; `C.29` when a mathematical representation or transfer question remains |

State the correspondence needed to interpret the representation: which element represents which relation, assertion, declaration, participant or occurrence. Use the selected scheme directly when its conventions settle that question. C.29 applies when choosing, transferring or relying on a mathematical representation leaves a separate correspondence or inference question. The mere form establishes neither obtaining nor identity; its content may still state a claim or carry a supporting argument.

Functional and arrow forms are assertion or representation notation. The following installed-part example is hypothetical: a relied use first needs the missing direct relation and occurrence rules identified in §5.1.

```text
installedPartOf(Bearing_B, Pump_P, during=Interval_T)
Bearing_B --installedPartOf{during=Interval_T}--> Pump_P
```

The first can represent the content of a relational assertion; the second is a binary projection in a selected representation. After those rules exist, a use that relies on either notation declares how its argument or endpoint elements correspond to the actual participants, direct predicate, qualifications, and any designated occurrence. The ordinary readable sentence remains sufficient when no representation-dependent use is current.

#### A.6.P:4.5 - Increase explicitness only for a named receiving use

Here **receiving use** is Plain shorthand for the exact later claim or operation that needs an additional object. It is not a shared FPF kind. Name that claim or operation and the rule that defines or constrains it before using it to justify more apparatus.

Use progressive elaboration from one recovered direct relation:

```text
readable direct-relation sentence with actual participants
  +-- compatible RelationSignature and SlotSpecs, when reusable typed declaration is current
  +-- explicit occurrence individuation, when a named receiver needs occurrence identity
      +-- occurrence-description episteme or stable designation, only when that receiver needs it
  +-- relational assertion detail, when polarity, modality, or reliance is current
  +-- representation and its correspondence, when the receiving use needs them
```

The diagram shows independently optional additions. A `RelationSignature` is not a prerequisite for explicit occurrence identity, and an assertion may name participants directly. A relation can obtain without a local occurrence designator. A stored row, graph edge, tuple or identifier may carry a claim or its grounds; its presence alone establishes no relation.

Apply A.6.REL when a receiving use needs to identify or reidentify the occurrence, compare its history, refer to it, or use it as a participant in another relation. A direct assertion can stop without explicit occurrence identity when that identity adds nothing to the receiving use. Repeated occurrences may have the same participants; their direct identity rule supplies the discriminator.

#### A.6.P:4.6 - Resolve relation-dependent wording by the actual object

| Current reading | Actual object | Next move |
|---|---|---|
| world-side participation | one exact entity participates directly in an obtaining relation under one relation-participant meaning and retains its independently governed kind | use the direct relation pattern; add no `SlotSpec` unless reusable typed declaration is separately current |
| assertion- or description-side designation | a claim-bearing assertion or occurrence-description episteme designates an actual participant, or an already recoverable occurrence when identity is current | use `C.2.1` plus the direct claim or description pattern; use A.6.5 only when a compatible `RelationSignature` actually supplies typed reuse |
| local kind used for participation-based reasoning | one exact local kind recovered through its candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule, whose later typed claim quantifies over entities participating under one designated participant meaning and a declared extent rule; a practice or source reference may locate or prompt comparison of the definition but does not identify the kind | use `C.3` and `C.3.1` only for typed membership, quantification, substitution, or kind-order reasoning |

These readings leave no fourth qualification object. A readable word such as `result`, `input`, `problem bearer`, or `next continuation` can remain in Plain prose when the direct relation or claim is recoverable. Naming that reading creates neither a kind nor an occurrence. The world-side participant never becomes a declaration-local `SlotSpec`; the receiving episteme's designation denotes the participant without replacing it.

#### A.6.P:4.7 - Name change by the object that actually changes

There is no universal relation-edit operation. First point to the object that the sentence says changed. If the sentence says that the same object continued, use that object's identity rule to test that claim. If identity-bearing episteme content changed, name the result as another episteme rather than an in-place edit:

| Object named as changed | What the reader does | subject pattern and stop |
|---|---|---|
| obtaining relation occurrence | Ask whether the later event is the same occurrence. Apply the direct relation's identity rule. For a temporally extended occurrence, record that it began, continued, ceased, or split. If the rule says it is not the same occurrence, name a second occurrence; do not say that the first occurrence became it. | direct relation pattern with `A.6.REL` |
| `RelationSignature` declaration content | If vocabulary, participant meanings, `SlotSpec`s, laws, applicability, identity-rule content, EntityOfConcern, or effective reference scheme differs, identify the resulting content as another episteme and keep any claimed revision Work separate. Test that output anew as a `U.Signature`. Call the two epistemes editions, refinements, or successors only after the complete direct predicate for that relation is satisfied; otherwise stop at two distinct epistemes. | `C.2.1` and `A.6.0`; `A.15.1` for revision Work |
| relational assertion content | If claim content, EntityOfConcern, or effective reference scheme differs, name another assertion episteme. Keep any claimed revision Work, the later episteme, retraction or currentness claim, publication, reliance posture, and continuity relation separate. Then test the world-side predicate again; edited text is not evidence that the world-side relation changed. | `C.2.1`, the direct claim pattern, and `A.15.1` for revision Work |
| reliance posture for one declared use | Record reliance as supported, refuted, or unresolved for that use. Do not change assertion polarity or create an occurrence. | `A.10` or the receiving evaluation |
| evidence or witness relation | State which evidence-bearing episteme or carrier bears on which claim, then test whether that relation begins, ceases, or is superseded. Record time and freshness through the exact evidence/currentness predicates. | `A.10`, `B.3`, or the pattern that defines the direct evidence predicate |
| participant designation in a receiving episteme | If an author substitutes another by-value designation inside the receiving claim, the resulting claim content identifies another episteme. If the same reference value receives another interpretation, state the exact interpretation relation separately. If another reference value replaces the earlier reference value, apply A.6.5's reference-retargeting rule. Recheck the world-side predicate; A.6.5 reference retargeting is available only when the receiving claim reuses a compatible declared `SlotSpec`. | `C.2.1` and `F.18`; `A.6.5` for the declared reuse |
| occurrence designator | Assign, replace, retire, or interpret a designator only for an already recoverable occurrence. The name does not create or change the occurrence. | `F.18` and the effective reference scheme |
| description episteme | If claim graph, EntityOfConcern, or effective reference scheme differs, identify another description episteme and keep any claimed revision Work separate. Assert an edition, refinement, or supersession relation only after its own predicate is satisfied; otherwise stop at two descriptions. | `C.2.1`; `A.15.1` for revision Work |
| publication relation | State that one selected episteme was made available, that its availability ceased, or that another episteme was published. Do not infer a content or world-side change from publication alone. | `E.17` and `E.24.PUB` |
| representation-bearing episteme | If its claim content, EntityOfConcern, or effective reference scheme differs, name another episteme and keep any claimed revision Work separate. Do not infer a represented-world change from that new episteme. | `C.2.1`; `A.15.1` for revision Work |
| representation form or element | First ask: did one mark or form change, or is practical content being re-represented for the same concern under another scheme or reasoning medium? For a mark or form change, name the resulting representation object under that object's identity rule; do not call it a scheme transition. State a changed `C.29` correspondence or lens-use claim separately as another claim-bearing episteme. Ordinary `A.6.3.RT` use may stop with the target representation, source comparison, preserved content, representation delta, loss, use boundary, and return. When the needed claim makes exact identity material, independently identify source episteme `X`, receiving episteme `Y`, their same exact EntityOfConcern and effective schemes, and `v : X -> Y` with applicability, preservation, loss, and prohibited strengthening. Only when the needed sentence asserts the historical six-participant occurrence also require the selected model-use structure, two scheme-description epistemes, actual Work, direct predicate, applicability, and occurrence-identity rule; a declaration-local SlotKind or a reference record is not enough. If that exact occurrence claim lacks a current predicate, record the established A.6.RCD `missing-governor` result. None of these changes by itself changes the represented world-side object. | `A.6.3.RT` for the ordinary note, triggered exact construction, or later-specific occurrence; `C.2.1` and `C.29` for separate claims; `A.6.RCD` only for a missing direct occurrence governor |
| actual correspondence occurrence, separate from a `C.29` claim or representation | The presence of a `C.29` claim, Card, edge or representation alone does not establish an occurrence. Its content may assert or support a correspondence; judge that claim and its grounds under the direct rule. Name the representation element and what it represents, then write the plain correspondence sentence the next task needs. If a current exact ClaimGraph states that predicate and its applicability, test whether it holds. If the task only needs to know whether the correspondence holds, stop there. If it needs to identify or reidentify an occurrence, refer to it or use it as a participant, apply its identity rule with A.6.REL. If no current predicate source supplies the predicate and identity rule, record the established A.6.RCD `missing-governor` result while keeping the element, represented object or claim content, and needed sentence visible. A changed representation form, lens-use account, or preservation or loss claim does not by itself change an actual correspondence occurrence. | the pattern that defines the exact correspondence predicate and identity rule, with `A.6.REL` when explicit occurrence identity is required; use `A.6.RCD` if the direct governor is missing; the separate `C.29` representation/correspondence assertion remains distinct |
| claim-bearing lens-use, preservation, or loss-account episteme | If the selected representation, represented object or claim content, `LensMappingMode`, `PreservedStructure`, `LostStructure`, declared lens use, any stated blocked overread, stop or return condition, EntityOfConcern, or effective reference scheme changes the claim content, name another episteme. Recheck the correspondence occurrence and any world-side claim separately. Select any blocked overread through F.19's plausible-reader test. A changed display form alone does not establish a changed lens-use or loss claim. | `C.2.1` and `C.29` |
| direct Bridge occurrence | Name the local-sense endpoints and write the Bridge sentence the next task needs. Use only a pattern that states that direct predicate. If the task only needs to know whether the Bridge holds, stop after testing the predicate. If it must identify or reidentify an occurrence, refer to it or use it as a participant, apply that pattern's identity rule. State beginning, continuation, cessation or a second occurrence only when the facts and that rule establish it. A new Card, direction statement, `CL`, loss note, licence, evidence item, or publication does not by itself change the occurrence. | the pattern that states the direct Bridge predicate and identity rule; if none exists, `A.6.RCD` |
| Bridge description or Bridge Card episteme | If Bridge kind, direction, `CL`, loss, admitted use, substitution licence, or EntityOfConcern content differs, name another episteme. Keep any claimed revision Work, the later episteme, any edition or refinement relation, evidence and publication separate. Do not report a changed Bridge occurrence unless its predicate or identity rule says so. | `C.2.1`; `F.9` for Bridge-description content |

The changed object controls the operation and continuity test. Ordinary revision can remain an activity description. When a claim deliberately asserts a particular dated `U.Work`, recover its A.13 basis and independent A.15.1 admission. F.6 applies only to a separate precise assignment-bound attribution through the same A.13 assignment; missing or failed attribution leaves the Work intact. The resulting episteme is independently identified. A shared title, sequence, identifier or authoring intention alone does not establish edition, refinement or supersession. If no identifying fact changed, do not invent a change claim.

#### A.6.P:4.8 - Preserve polarity and inverse meaning

Participant order is part of many relation predicates. `Bearing_B isPartOf Pump_P` and `Pump_P hasPart Bearing_B` can be paired as inverse readings only when that inverse law is declared under the direct parthood pattern. A symmetric relation is symmetric under its direct law, not because a sentence sounds reciprocal.

When two viewpoints use different readable directions:

1. keep the same participant referents and their exact kinds;
2. name the forward predicate defined or constrained by the direct relation rule;
3. use an explicit inverse predicate or inverse reading when one is available under that pattern;
4. keep scope, time, viewpoint, and reference scheme fixed while checking equivalence;
5. treat a change of participant kind or predicate as a semantic change rather than a stylistic rewrite.

#### A.6.P:4.9 - Use an actionable guide and keep a small candidate note when grounding is unresolved

For each ambiguity cluster, guide the reader through this order:

> trigger expression -> candidate grounded objects and direct relations -> discriminating observations or tests -> readable direct-relation rewrite -> only the additional declaration, assertion, occurrence, designation, or representation needed by the named receiver -> applicable defining or testing rule

Do not organize the guide as a synonym list or make a table field the ontology. A qualifier such as `comparative`, `safe`, `interactive`, or `reliable` narrows wording but does not restore the head kind by itself.

When grounding remains unresolved and the work needs a note, use these prompts to keep the alternatives and discriminator recoverable. They prescribe no reusable schema or tuple kind.

| Question | What to write |
|---|---|
| Which wording is unresolved? | quote the phrase whose head, participant, predicate, or qualifier is unresolved |
| Which distinction is unresolved? | name the exact question about head kind, participant referent, direct relation kind, direction, or qualification |
| Which grounded alternatives remain? | name candidate objects, kinds, or direct relations, not synonyms |
| What separates the alternatives? | name the observation, claim, identity test, or direct-pattern condition |
| What reading is selected now? | write the selected objects and direct relation, or state that the distinction remains unresolved |
| What changes after selection? | write the readable sentence, optional declaration need, occurrence-identity need, assertion or representation need, or condition for applying a neighboring pattern |

For `Alice is at the table`, the physically present place and participation in a meeting are both plausible only while local evidence leaves them open. A location observation selects a located-at relation. A meeting roster may support a separately governed participation claim; an exact `U.SystemRoleAssignment` may also be relevant when its direct species predicate independently obtains. The note combines neither relation and infers neither a system-role kind nor an assignment from the place expression.

Unresolved alternatives prevent a conclusion that depends on selecting one of them. Name that dependent claim or action and the observation, test or direct-pattern condition that would decide it. The note can still support comparison, further inquiry, publication of the uncertainty, or a decision warranted under every live alternative. Stop only the dependent use; preserve the alternatives and any sufficient unaffected result.

#### A.6.P:4.10 - Classify boundary claims and keep engineered rewriting epistemic

Use `A.6.B` only when a sentence at the boundary does at least one of four things: defines a truth-conditional relation or signature rule (**L**); decides whether one identified mechanism application may start or continue (**A**); states a generic prescription from an exact normative source, an individual duty with its actual bearer and obtaining `U.Commitment`, or a grant under A.6.B:8.4.1's permission-word branch (**D**); or states observations, effects or evaluation results and the conditions under which they are obtained (**E**). A sentence about claim scope or use, when to start or stop A.6.P, how to correct an endpoint kind, or whether a Bridge is needed does not qualify merely because it limits the repair.

Before giving a sentence an **A** label, answer two questions: Which mechanism application is about to start or continue? What predicate is checked at that point to admit or reject it? If either answer is missing, do not label the sentence **A**. Keep its scope or use, A.6.P start or stop decision, endpoint-kind correction, and Bridge need with the patterns that define or constrain those questions. Split any mixed sentence before classifying its claims:

- **L** states the direct relation semantics, declaration invariants, polarity, participant meanings, and any reusable `SlotSpec` typing;
- **A** states one predicate checked when an identified mechanism application starts or runs. Its result says whether that application is admitted, may continue, or is rejected. A condition does not become **A** merely because it limits a claim, tells an author when to enter or stop this pattern, asks for an endpoint-kind correction, or requires a Bridge;
- **D** states what an exact normative episteme prescribes, an obtaining individual `U.Commitment` with its actual duty bearer under A.2.8, or a grant selected by A.6.B:8.4.1 under A.2.8.PER. A generic prescription needs no invented individual bearer or commitment. An individual duty names its actual bearer; a system-role kind or assignment may be a rule ground but is neither that bearer nor the commitment relation. A grant retains its beneficiary, action and own obtaining basis; actual admission decisions and exercise remain separate E claims;
- **E** states observations, effects or evaluation results and the conditions under which they are obtained. A separately claimed Work, evidence relation or freshness condition follows its own pattern.

Scope, `Γ_time`, viewpoint, reference scheme, witnesses, admissible use, any justified non-admissible overread, and stop or return condition stay with the direct relation or claim that actually needs them. They are not a universal qualifier kit. Select a non-admissible overread through F.19's plausible-reader test. An `admissible use` sentence is not an **A** claim unless the reader can point to both the mechanism application and its runtime entry predicate.

If a later task must state a relation between a source episteme `X` and a receiving episteme `Y`, or describe an operation that produces `Y`, first identify `X` and `Y` independently under `C.2.1`. A difference in claim content, EntityOfConcern, or effective ReferenceScheme identifies another episteme; no component is rewritten in place. Keep `X`, `Y`, the mathematical arrow or construction, any use-specific assertion, and any operation application distinct. Use `A.6.3` only for an exact compatible construction between epistemes about the same exact EntityOfConcern. Use `A.6.2` for a local effect-free arrow family. Use `A.6.4` for an exact arrow `r` whose endpoint epistemes concern independently different entities. A separate C.2.1 bounded-use assertion `q` is about exact `r`; its ClaimGraph states the invariant, visible loss, named receiving use, conditions, and affirmative or negative polarity. A separate current-case judgement records comparison of the exact facts with `q` and returns exactly `satisfies`, `fails`, or `cannot decide`; `cannot decide` names the missing fact and reopen condition. None of these patterns rewrites an episteme component or substitutes a declaration-local SlotKind or reference record for the arrow or application. If the needed entry or result condition is missing, preserve `X`, `Y`, the changed EntityOfConcern if any, and the sentence the next task needs as an explicit stop that names the missing arrow, use-claim, or application condition. Call `X` and `Y` editions, refinements, or successors only when that direct continuity relation independently obtains; a shared title, sequence, or authoring intention is not enough.

Ordinary authoring, checking or publication can be described directly. If the account deliberately asserts a particular dated `U.Work`, establish its A.13 basis and independent A.15.1 admission. Keep that Work, any operation application, mathematical arrow, endpoint epistemes and use assertion distinct. None alone makes the repaired world-side relation begin or cease, changes its participants or supplies occurrence identity. Stop before introducing these objects when the receiving use needs none.

#### A.6.P:4.11 - Relax wording, then apply the exact governing rule

After the relation has been recovered, Plain wording may be shorter than the Tech explanation. The shorter wording remains usable when a reader can still recover the exact participants, direct relation, the pattern that defines its participant and obtaining rules, every qualification that changes the declared use, and the point at which reusable declaration, occurrence identity, assertion detail, or representation becomes necessary.

Stop using A.6.P when the direct relation and participants are selected. The selected direct pattern defines or constrains that relation. Apply the relevant pattern separately to any remaining assertion, occurrence-identity, evidence, work, Bridge, description, publication, designation, or representation question.

When generic relation recovery identifies one current claim at a method, intended-work, actual-work, production, evaluation, delivery, acceptance, transfer, or receiving-use boundary, apply `A.6.P.WMR`. Its application records exactly one of four result families:

1. an exact direct subject-relation claim, positive or governed negative;
2. an exact `A.6.1` operation-application binding;
3. a local `A.15.PROD` claim or another local relation-bearing claim selected under `A.6.RCD` disposition 2;
4. an exact non-assertability result with the reason defined in `A.6.P.WMR:4.3`: `factually unsupported`, `missing-information`, `missing-governor`, the governing rule's inapplicable result, or `missing-substrate`.

`Missing-governor` names the affected receiving use, exact participants, and missing predicate or obtaining law. A known rule's inapplicable result retains that rule and its unmet applicability condition; `missing-substrate` names unavailable constructor semantics under A.6.RCD:4.2. Neither by itself calls for a new relation kind. When participant referents and the named receiving claim are exact but no current direct relation closes that claim outside A.6.P.WMR, require `A.6.RCD` rather than improvising a relation or kind.

| Recovered question | What the reader does | Result or governing rule |
|---|---|---|
| interface, port, signature, participant, field, parameter, or representation-position wording | Name the actual interface-side object and the direct claim needed next; keep any schema field or representation position separate from that object. | `A.6.RSIR`, then the pattern defining the exact interface-side claim |
| basedness or dependence on an explicit base | Name the actual dependent, base, and direct relation; apply that relation's predicate and stop when the readable assertion answers the receiving use. Add scope, time, evidence, a reusable declaration, or occurrence identity only when the selected predicate or one named receiver needs it. Include a blocked overread only when it passes F.19's plausible-reader test. | `A.6.6` |
| service, server, provider, SLA, API, delivery, connection, entitlement, or access wording | State the decision, explanation, design choice, or action that depends on the phrase, then use A.6.P:4.11a to name each concrete subject or relation in a readable sentence. The branch is a wording-use recovery rule, not a service kind or case record. | `A.6.P:4.11a`, then the pattern defining or constraining each recovered claim |
| sameness, correspondence, export, alignment, mapping, or substitution between locally interpreted values | Use A.6.9 to distinguish designation of one value, an operation, and a cross-local semantic-correspondence claim. Designation and an operation stay with their direct rules. For a semantic-correspondence claim, name the exact F.17 endpoints and the claim the next task needs; apply F.9 only when their interpretation bases differ. Shared spelling or the presence of a mapping artefact or Card alone does not establish the Bridge. Its asserted content and grounds can be examined under the direct Bridge rule. | `A.6.9` for disambiguation, then the defining rule for the recovered claim; `F.9` for a current Bridge question, `C.2.1` only for a separate claim or description, and `A.6.RCD` only after the participants and needed relation claim are exact but its governing predicate is missing |
| `integrity` wording — first question | Ask what the sentence lets the next reader do. Does it make a whole, part, structure, or coverage claim; characterize or measure something; or use evidence to support an assurance claim? The word `integrity` selects none of these branches by itself. | choose one of the three direct branches below; if evidence does not discriminate them, keep the alternatives explicit and stop only the use that requires one selected reading |
| `integrity` as a characteristic or measurement | Identify the bearer and integrity characteristic. If a value is reported, also name the scale, coordinate or level, unit when needed, measurement method, result, and evidence pointer. For example, `structural integrity is measured at X` takes this branch without inventing a candidate whole or parthood claim. | `C.16.P` until characteristic and scale construction are clear, then `C.16` and the exact measurement pattern |
| `integrity` as evidence or assurance | Name the exact claim, the evidence that bears on it, and the reliance or assurance use under consideration. A report called an integrity report is neither a whole nor assurance by title. | `A.10`; `B.3` only when an assurance claim is current |
| actual whole, part, structural-whole, complete, turnkey, or end-to-end claim | Name the actual bearer, participants, and direct claim. Recover a candidate whole, its boundary, and the relevant parts or constituents only when that claim requires them. Common examples are parthood, membership, portion, phase, composition, selected structure, holon recognition, whole reidentification, work coverage, and completion; this is not a closed taxonomy. In `the assembled pump remains an integral whole`, recover that pump, its boundary, parts, and the rule that defines or constrains the whole, part, or structure claim; include a selected structure only when the receiving use consumes it. A `wholenessSituation`, bundle, or adjective proves none of those claims. | `A.14`, `C.13`, `A.22`, `A.1`, `B.2`, `A.15.1`, or `A.15.PROD` as selected by the claim; otherwise `A.6.RCD` after the exact missing predicate is shown |
| evidence bearing on a named claim | Name the evidence-bearing episteme or carrier, the claim it bears on, and the exact reliance or assurance use. | `A.10`, with `B.3` only when an assurance claim is current |
| method/work/result/production/delivery/acceptance wording whose exact governor is hidden | Name the exact objects and the sentence needed at the method, work, result, production, delivery, acceptance, transfer, or receiving-use boundary. | `A.6.P.WMR`, then one of its four truthful result families |
| exact participants but no current direct relation for the named receiving claim | Preserve the exact participants and sentence needed next; do not improvise a relation or kind. | `A.6.RCD` |
| one work occurrence enabling, preparing, or producing for another exact use | Name both work-side objects and the exact enabling, preparing, or producing claim; do not substitute a plan, method, or package. | `A.15.1`, `A.15.4`, `A.15.PROD`, or the direct work relation |
| an episteme assertion or description | Identify the claim-bearing episteme, its EntityOfConcern, and its effective reference scheme; keep publication separate. | `C.2.1`, then `E.17` when publication is current |
| architecture wording | Name the architecture object, scope, and claim the sentence actually makes. | `C.30.P` |
| characteristic, measurement, comparison, or quality wording | Name the bearer, characteristic, scale or comparison basis, result, and use that are current. | `C.16`, `C.16.P`, `A.17`-`A.19`, or `C.25` as selected by the actual claim |
| palette, front, archive, shortlist, or selected-set wording | Name the selected-set object and the exact selection, comparison, currentness, archive, or use claim. | `G.2`, `A.19`, `C.18`, `C.19`, or `G.5` as selected by the actual object and use |
| quantum-like relation or probe wording | First recover the ordinary direct relation; only then state the remaining probe, frame, order, export, or state-representation claim. | the pattern defining the ordinary relation first; `C.26` only for the residual quantum-like claim |
| mathematical tuple, graph, arrow, function or other formal representation with an unresolved use or transfer question | Name the mathematical object, represented subject, needed correspondence and inference, preservation and loss. Use an adequate local calculation directly when no such question remains. Any excluded use follows F.19's full guard test. | `C.29` for the separate mathematical-lens question; `F.9` only for a separately claimed semantic Bridge |
| designation after ontology is settled | Recover the object and relation first, then state why one durable designation is needed. | `F.18` |

##### A.6.P:4.11a - Recover service/access claims through their concrete rules

Start with the decision, not a facet list. Ask what the reader must choose, do, accept, explain, restart, or stop. Then write one plain sentence naming the concrete subject or relation. If the source sentence carries several claims, write several plain sentences and name the pattern that defines or constrains each claim. The first useful result names each referent or relation, the claim needed for the current decision, and the next action. Add an exact C.2.1 assertion and `ClaimGraph` identity only when a named downstream use must carry or compare that claim independently.

**Source-domain guard.** Bare *service* has no default System reading. In ordinary business and physical-world talk it may name a dated occurrence of service provision, a reusable way of providing it, offered outcome or eligibility content, provider participation, or another direct claim. In software talk it may be metonymic wording for an exact process, deployed component, endpoint, application, host, or cluster. Name the referent before choosing Work, Method, `U.PromiseContent`, a local system-role kind, `U.SystemRoleAssignment`, `U.System`, or a direct relation. Never rewrite *service* automatically as *server* or as a System.

This table is a local recovery aid. Select the rows for the actual claims and stop when their direct results answer the receiving use.

| Current claim behind service/access wording | Plain action first | Concrete rule |
| --- | --- | --- |
| What a consumer may rely on | State the promised outcome, eligibility, access description, and acceptance content that the present decision uses. | Use one `U.PromiseContent` episteme under A.2.3. Open a further subject, action, or result claim only through the row and predicate that govern it. |
| Provider or consumer participation | Name the participation meaning, admitted participant, and participation predicate needed now. If the same claim also needs a work-facing System classification, name its local system-role kind under A.2; if assignment identity matters, cite the assignment occurrence and its declared `U.SystemRoleAssignment` species. | Use the pattern that defines the participation relation. Add A.2 classification or A.2.1 assignment only when that separate identity matters. |
| Individual duty, recommendation-as-duty, or prohibition | State the actual bearer, direct commitment predicate, exact modality, referents, scope and time, constitutive rule, and required instituting basis. Test any responsibility claim separately through its direct domain predicate or return the exact missing governor. | Use one obtaining A.2.8 `U.Commitment`. |
| A communicative offer, approval, revocation or other instituting act | Identify the actual communicative occurrence and its participants; a grant or duty mentioned in the sentence does not by itself establish such an act. | Use A.2.9 `U.SpeechAct` for the communication; test any resulting grant, commitment or delivery under its own relation. |
| Permission, non-prohibition, exercise, non-violation, or conflict | State which permission-side question is current and name the exact bearer or beneficiary, action specification, normative-frame edition, ClaimScope, qualification or validity window, and obtaining case facts that the result needs. | Use the exact A.2.8.PER result. |
| Exact software or physical bearer, access point, delivery entity, or proposed physical/operational arrangement | Name the process, component, endpoint, host, application, cluster, front desk, equipment, arrangement, or other exact referent and state the claim made about that entity. Preserve an arrangement proposed by the source; do not replace it with one convenient endpoint before evaluation. | Use A.1/A.1.SCR only when the repaired claim depends on whether that exact entity is a `U.System`. |
| Reusable way of requesting, connecting, repairing, providing, or delivering | State the reusable way of doing. | Use one `U.Method` under A.3.1; handle its description and any dated enactment in their own rows when those claims are current. |
| API, interface, access procedure, runbook, or other description | Name the claim-bearing description and what it describes. | Use C.2.1; use `U.MethodDescription` only after A.3.2's same-individual membership test, and add publication or specification use only when current. |
| Intended delivery, connection, repair, or provisioning | State the intended Work and its intended fillings. | Use one `U.WorkPlan` under A.15.2; open the Work row when performed history becomes current. |
| Actual service provision, request handling, connection, provisioning, repair, or delivery | Recover each exact actual performer through A.13, then use A.15.1 to admit one dated occurrence and name its Method, extent, and containing System. Add F.6 only when this service account also consumes precise assignment-bound attribution; its absence or failure leaves the Work intact. | Use A.15.1 `U.Work` and only direct Work relations that obtain. |
| Capability to provide or sustain service or access | Name the holder, work or result, conditions and attained bounds; recover the support whose currentness matters. | Use the qualified holder-ability claim and separate fit comparison under A.2.2. |
| Ticket, case, log, measurement, evidence, or evaluation | State the particular claim carried or supported and the decision that relies on it. | Use C.2.1 for the episteme and only the measurement, evaluation-operation, result-binding, or A.10 evidence relations needed now. |
| Promise use, outcome delivery, fulfilment, or acceptance | State the exact relation claimed and its participants. | Use A.2.3 relations when their conditions hold, plus separately governed evaluation, result, delivery, or acceptance relations actually used. |
| Current status, connectivity, entitlement, delivery, acceptance, exposure, or another subject relation | Name the bearer and direct relation or characteristic asserted now. | Use A.19.SPR while the state wording remains unresolved; otherwise use the pattern that defines the asserted relation or characteristic, adding Work only for a dated performed occurrence. |
| No current direct relation states the needed claim | Preserve the participants, write the sentence the next task needs, and name the decision that cannot proceed. | Record the established A.6.RCD result `missing-governor[...]` and retain that exact unresolved sentence. |

**Four language probes.** Use these probes to select the current question and its relevant rows.

- **“My service stopped.”** Ask what stopped. Service-provision Work may have ceased; an exact deployed software or physical bearer may have stopped or become unavailable; or promised availability or fulfilment may have failed. The sentence alone selects none. State, Work, promise, evidence, and fulfilment remain separate. Use A.1.SCR only if the repaired bearer claim itself depends on systemhood.
- **“Which services do we provide?”** Name the offerings or promise contents being compared and any provider assignments that are current. Open performed Work or fulfilment only when the question needs those claims.
- **“How is this service provided?”** A reusable way of providing it selects a Method; a procedure or API text selects an episteme and perhaps MethodDescription; a dated provision selects Work. The wording alone selects none.
- **“Restart the service.”** Name the exact bearer to restart—for example, a process, deployed component, endpoint, host, application, or cluster—and the action's governor.

**Addressability is an aid, not a classification rule.** If the sentence says call, visit, connect to, route to, restart, deploy, or scale, use it to ask which exact access point, delivery bearer, or other entity the claim concerns. Apply A.1 only when the repaired claim depends on systemhood. Actual Work still passes A.15.1, and every relation is tested against its defining predicate and obtaining condition. An endpoint may be an access point without being the whole delivery system.

**Internet-access case.** “We sell internet access” first becomes the commercial claim the reader needs: promise content, permission, provider or consumer participation, status, fulfilment, or another direct relation. For the promise reading, state the concrete claim—for example, `Customer-18 may rely on PromiseContent-IA-18 for the named connectivity outcome and acceptance content`—using the pattern that defines or constrains it. If actual participation matters, state the exact direct provider and consumer participation predicates. State local system-role classifications or assignments separately only when their own A.2/A.2.1 conditions hold. If the source instead proposes the physical or operational whole `InternetAccessArrangement-CA17`, preserve that exact entity beside `ProviderGateway-2`, `HomeRouter-18`, and the status claims; use A.1.SCR only when the decision depends on whether the arrangement itself is a System. Do not substitute one gateway or endpoint before that evaluation. Keep the connection Method and API or procedure description separate. `ProvisionConnectionPlan-18` is intended Work; `ConnectionEstablishmentWork-42` is one dated occurrence. A real grant uses A.2.8.PER and is not inferred from a credential. Connectivity status, measurement, evidence, evaluation, delivery, fulfilment, and acceptance each need their own claim. After these claims are recovered, use A.1.STM only when the live question is how one result contributes to use of a named project system-of-interest; otherwise stop after stating the direct claim.

**Physical repair-shop case.** For “The repair service is delayed,” select the subject from the blocked decision. If the blocked decision is where to leave the machine, name the front desk or intake point and test systemhood only if that decision needs it. If the decision is what physically performs the repair, name the workshop, equipment, or other exact bearer. If it is who is responsible, name the direct responsibility predicate, its actual participants, applicability, and occurrence identity or return the exact missing governor; a provider label, classification, or assignment is insufficient. What the customer was promised is promise content; an individual deadline duty is a separately obtaining commitment; how repair is done is a Method; the procedure card is a separate description; the repair that happened is dated Work. Fulfilment or acceptance requires its own relation.

**No duplication boundary.** A.6.P defines only this recovery move. The recovery table introduces no common service/access kind or record. When the named decision depends on systemhood, cite A.1.SCR for the exact bearer or arrangement assertion. When the next question asks how an already recovered result contributes to project use, cite A.1.STM. State every other subject assertion under its exact predicate or constraint.

The selected predicate, its obtaining rule, and the current facts determine the result.

##### A.6.P:4.11b - Recover pattern-governance and pattern-routing shorthand

Treat "pattern X governs/owns Y" as under-specified language. Recover exact `Y` and ask what X actually contributes: does it define a predicate, constrain a use, supply a test, describe a method, or only serve as a citation? State that contribution in ordinary prose. Add an exact C.2.1 assertion or `ClaimGraph` only when a named downstream use needs claim identity. A pattern id may remain as a locator for that content. If the sentence asserts actual formal-premise use, use A.6.RCD to derive or test the needed claim. If it asserts membership in or selection by a reusable signature, use A.6.0 to test that criterion under the signature's exact laws. Attribute any actual action, ownership, or authority claim through the direct relation that establishes it.

Likewise, "return/route/send/exit to the pattern for the next question" is procedural shorthand unless an actual relation is current. A true stop has no receiver. If work should continue, state the condition or unresolved question and name a candidate pattern whose `Use this when` entry accepts it. Preserve a real work, control, communication, API/tool, transport, graph, source/carrier, access, mathematical, or admitted B.4.1 route relation when that is the sentence's actual subject.

Ordinary instructions may say that an agent “uses” or “applies” a pattern. Expand that wording only when the claim depends on the identity of the actor, Method, description, dated Work, result, Transformation, or transformation-flow structure; then distinguish those objects using A.3.2, A.15.1, A.3.4, or the applicable flow pattern. A displayed sequence of pattern descriptions may describe a Method or constrain a separately admitted transformation-flow structure; establish any separately claimed Work, Transformation, or flow under its direct pattern.

#### A.6.P:4.12 - Lexical guardrails

Overloaded words are diagnostic entry points, not relation kinds. In Tech or normative prose, `same`, `synced`, `linked`, `connected`, `anchored`, `grounded`, `supported`, and similar words cannot substitute for an unnamed direct relation or claim family. `Bind` and `rebind` remain name-binding or relation-specific vocabulary and are not generic relation-change verbs. A Plain gloss is admissible when its direct reading and the next applicable rule remain recoverable.

`E.10` is the pattern for the trigger scan and `E.10.ARCH` the shared wording-use recovery architecture. `F.18` is the pattern for durable name selection after the governed object is known. A.6.P does not maintain a second trigger registry or mint one specialization for every repeated word.

### A.6.P:5 - Archetypal Grounding

#### A.6.P:5.1 - Physical assembly and repeated occurrences

**Tell.** A maintenance note says `replacement bearing is linked to Pump_P`.

**Show the ordinary repair.** Recover physical bearing `Bearing_B`, pump `Pump_P`, and interval `Interval_T` independently. The readable candidate claim is `Bearing_B is part of Pump_P during Interval_T`. Select the intended direct parthood reading under A.14 and its applicable subject rule. Where that predicate and the case facts already settle the receiving question, state the assertion and stop; an installation history or occurrence identifier is not required merely to report current parthood.

**Show the identity-dependent stop.** A reliability analysis needs to distinguish the installed-part relation before removal from that after reinstallation. Current A.14 does not define an `InstalledPart` relation kind, its participant meanings, obtaining predicate, applicability, or same-versus-new-occurrence rule. Return A.6.RCD `missing-governor` for that proposed relation, naming `Bearing_B`, `Pump_P`, the relevant intervals, and the reliability comparison. Removal and reinstallation alone do not establish two occurrences. A.6.REL explains how to apply a supplied identity rule; it does not supply this missing rule.

**Conditional continuation.** If a direct installed-part definition is accepted, apply its obtaining and same-versus-new-occurrence rules to the case facts. Distinguish two occurrences only when that rule and those facts warrant them; add stable designations or occurrence descriptions only when the receiving use needs them. For repeated typed reuse, an `InstalledPartRelationSignature` may then declare `InstalledPartSlot` and `AssemblyWholeSlot` under A.6.5. Until that definition exists, these names remain hypothetical declaration candidates, as in A.6.REL:5.2 and A.6.5:5.2.

If the adopted construction rule makes installation Work constitutive, identify that independently admitted Work and its declared identity contribution. Database rows, diagram edges, assertions, and declaration components retain their own identities and do not supply the obtaining or recurrence rule. When a mathematical representation is used, state its C.29 correspondence separately. A separate relator is needed only if the direct ontology identifies and justifies it.

#### A.6.P:5.2 - Clinical evidence use and negative reliance

**Tell.** A care note says `the measurement supports the dose change`.

**Show.** The repair distinguishes the measurement work occurrence, its measurement-result episteme, the work-plan claim, the measured characteristic, the applicable range, and the exact evidence relation. `C.16` governs measurement construction and applicability; `A.10` governs whether that episteme bears on the named dose-change claim for this use. The broad predicate is not replaced by a universal support relation.

**Show the boundary.** If current evidence refutes the dose-change assertion or leaves reliance unresolved, the receiving evaluation records that posture. It does not create a negative world-side measurement, treatment, or evidence occurrence. A fresh publication of the same measurement-result episteme changes availability, not the measured condition or evidence relation by itself.

#### A.6.P:5.3 - Episteme correspondence and representation

**Tell.** Two teams say `the models are aligned`, and one tool draws an edge between their model nodes.

**Show — models.** Model epistemes `DesignModel_E` and `MaintenanceModel_E` have `EntityOfConcern` `PumpAssembly_P204` and effective reference schemes `CAD-Part-Scheme-v7` and `Asset-Register-Scheme-2026Q2`, respectively. `AlignmentEdge_17` joins nodes labelled `BRG-6204` and `bearing-4471`.

**Structure decision.** No established model-use structure changes either label's reading or whether replacement approval may use the pairing. Add no `BoundedModelUseStructure`; a diagram boundary is not evidence.

**Needed sentence.** `For bearing-replacement planning on PumpAssembly_P204, CAD-Part-Scheme-v7 label BRG-6204 and Asset-Register-Scheme-2026Q2 label bearing-4471 denote the same installed bearing.` This is a candidate claim, not yet a fact.

**Edge meaning.** Under the selected graph convention, `AlignmentEdge_17` expresses the candidate sentence. Its presence does not establish one referent or a Bridge occurrence. Use C.29 only if a separate mathematical representation or transfer question remains.

**Adjacent reading.** Record `ninety-seven percent of endpoint pairs passed the mapping test` with `C.16`. If approval relies on that measurement, `A.10` governs the evidence relation. The percentage does not establish the needed sentence.

**Result.** Bearing-replacement approval is not yet supported. First recover what each label designates under its reference scheme and the grounding or identity evidence for those referents. If the applicable designation and subject-identity rules establish one independently identified bearing, return that bounded identity claim; it does not by itself authorize replacement. If the labels designate different referents, or a kind and an individual, revise or reject the candidate claim as warranted. Keep missing interpretation or evidence explicit. Return `A.6.RCD missing-governor` only when the exact remaining predicate or a required applicability or identity rule is absent, naming that gap and the affected use.

**Representation boundary.** The edge and endpoint positions represent the assertion and its participants under the graph convention. Their interpretation makes the claim readable; the designation and subject-identity evidence decide its truth. Neither shared labels nor a visible edge establishes substitutability or an individuated relation occurrence by itself.

When the claim is that both model epistemes concern the same world-side holon, recover each episteme's exact EntityOfConcern or grounding designation plus the observations, trajectory, or identity evidence governed for that holon. A Bridge preserves stated correspondences and losses; it does not prove the common world-side referent.

**Show the viewpoint-conformance use.** A review must decide whether model episteme `E` conforms to maintenance viewpoint episteme `P`. Identify `E` from its claim content, EntityOfConcern, and effective reference scheme, and resolve `P` as one claim-bearing viewpoint edition before reading a diagram, field, or reference as ontology. Then apply the direct predicate governed by `E.17.0`: `EpistemeViewpointConformanceRelation(E,P)`. Plainly, `E` conforms to this exact viewpoint.

For unchanged `E` and `P`, the pair `<E,P>` determines one positive occurrence. Selecting `P` for this review is a separate use qualification: selection neither makes conformance obtain nor enters occurrence identity. If another review selects `P2`, test `<E,P2>` instead of retagging `E`. A `viewpointRef` or diagram label does not identify either participant by itself. A query, transformation, or projection may supply construction history for `E`, but neither that history nor an assertion, evaluation, representation, or publication makes conformance obtain.

Add an occurrence designator when a receiving use needs to refer to or reidentify that conformance occurrence, distinguish it from another, or use it as a participant. Add evaluation, evidence, construction history, representation or publication detail only when the corresponding question matters. A.6.P stops after recovering E, P and the direct relation. E.17.0 governs the predicate and any separately requested U.View recognition; actual Work retains its own basis.

#### A.6.P:5.4 - Method, Work, system-role objects, and agency

The sentence `the inspection method checks Pump_P` may remain ordinary metonymy under F.19. For a separate claim about actual inspection history, recover the following exact case. The source basis says that admitted `System_S` has the A.13 core for inspection: it is independently classified under local kind `InspectorSystemRole` and holds obtaining `InspectionAssignment-17` of declared `MaintenanceInspectionAssignment` species for the stated scope and window. A.15.1 then independently admits `InspectionWork_W` and its `enactsMethod(InspectionWork_W, InspectionMethod_M)` relation; the examination relation separately connects the Work to `Pump_P`. Because this worked account expressly states under which assignment the inspection was performed, F.6 then establishes `performedUnderAssignment(InspectionWork_W, InspectionAssignment-17)` and checks the already recovered performer against the holder. If the deciding F.6 fact were missing, attribution would remain unresolved; contrary facts would refute that attribution. The independently admitted Work remains in either case. Taxonomy episteme and reference scheme may interpret the assertion but are not assignment participants. `System_S` performs `InspectionWork_W`.

#### A.6.P:5.5 - Formal reduced case

`3 < 5` states an ordinary mathematical comparison. The numerals designate values and the sign expresses the less-than predicate under familiar arithmetic conventions. No separate representation or transfer question remains, so C.29 requires no additional account. If a later use introduces one, explain the correspondence it needs. The present use requires no explicit occurrence identity and can stop at the assertion. A tool's graph edge, tuple or reifier represents that content without constituting the relation.

### A.6.P:6 - Bias-Annotation

This pattern favors ontology-first recovery, direct relation sentences, and the lightest explicit form that serves the named receiving use. That bias counters record-first and vocabulary-first repair.

The counter-risk is under-specification: an engineer may stop before a load-bearing participant, applicability condition, occurrence identity, or reference is exposed. The receiving-use test, hidden-arity check, three-way relation-dependent wording distinction, and explicit conditions for applying neighboring patterns provide the counterweight.

The pattern also favors neutral domain language. Examples span physical assembly, clinical Work, epistemes, ambiguous source *role* wording, system-role kinds and assignments, Methods, and formal relations so that one publication technology or professional tradition does not become the default ontology.

### A.6.P:7 - Conformance Checklist

1. **Recognition.** The use begins with one actual relation-bearing claim and states which later claim or operation is blocked by its ambiguity.
2. **Grounded heads.** Every load-bearing head refers to an exact object or remains explicitly unresolved; a qualifier does not substitute for the head kind.
3. **Direct relation.** Every positive or governed-negative direct subject-relation result names exact actual participants, an explicit admitted `RelationKind` token, and the pattern that defines its predicate, participant meanings, obtaining condition, and identity rule. The A.6.P.WMR non-relation result families remain defined or tested by the rules for the recovered Method, Work, result, production, delivery, acceptance, transfer, or receiving-use claim.
4. **Participant meanings.** The direct pattern states the participant meanings, actual participation, obtaining predicate, applicability, and occurrence-identity rule; every participant retains its independently governed kind.
5. **No negative occurrence.** Negative assertion, refutation, or unresolved reliance remains claim- or evaluation-side and creates no negative world-side occurrence.
6. **Demand-driven declaration.** A compatible `RelationSignature` and declaration-local `SlotSpec`s appear only when reusable typed use is current; an ordinary assertion may name participants directly.
7. **Designation separation.** A participant designation or occurrence reference remains content of a receiving episteme and neither replaces the referent nor makes the relation obtain.
8. **Hidden arity and qualifiers.** Every participant or qualifier included in the repair changes predicate satisfaction, applicability, identity, substitution, interpretation, admissible use, witness needs, or the named later claim or operation.
9. **Occurrence identity when needed.** Apply the direct identity rule when a receiving use needs to identify, reidentify, compare or use an occurrence as a participant. Repeated occurrences with equal participants retain the direct discriminator.
10. **Construction choice.** When construction is identity-bearing, the pattern defining that construction names the constructor, inputs, construction work or process, and identity contribution; otherwise the repair introduces no constructor.
11. **Object separation.** Direct relation kind, participant meaning, actual participant, declaration, assertion, occurrence description, occurrence, designator, reference, publication, Bridge, and representation remain distinct where present.
12. **Relation-dependent wording.** The reading resolves to world-side actual participation, an assertion- or description-side designation, or a justified C.3 local kind; no fourth qualification object is introduced.
13. **Polarity.** Participant order, inverse wording, symmetry, assertion polarity, and temporal qualification follow the direct relation law.
14. **Changed object.** Every change statement selects one exact changed object and its governing row in A.6.P:4.7; no generic relation-edit operation remains.
15. **Boundary classification.** Apply L, A, D, and E only to an actual A.6.B boundary statement. Before marking **A**, point to the particular mechanism application and the predicate checked at entry; if either is absent, leave claim use or scope, A.6.P entry or stop, endpoint-kind correction, and Bridge need with their own patterns.
16. **Candidate guide and stop.** Unresolved alternatives are grounded candidates with a discriminating check. Name and stop the use that requires selecting one reading; preserve warranted inquiry, an explicit uncertainty report and decisions sufficient under all live alternatives.
17. **Representation boundary.** The selected scheme makes the needed element-to-content correspondence recoverable. C.29 applies to a separate mathematical representation or transfer question; form alone establishes neither the direct relation nor its identity.
18. **Optional episteme relation or operation.** Use this path only when a later task must relate source and receiving epistemes or describe an operation that produces the receiving episteme. Identify both endpoints independently under `C.2.1`. Use `A.6.3` for an exact compatible same-EntityOfConcern construction, `A.6.2` for a local effect-free arrow that satisfies its entry and laws, and `A.6.4` for an exact different-EntityOfConcern arrow `r`. Its separate C.2.1 bounded-use assertion `q` is about exact `r` and has a ClaimGraph stating the invariant, visible loss, named receiving use, conditions, and affirmative or negative polarity. A separate current-case judgement reports exactly `satisfies`, `fails`, or `cannot decide` from the exact facts; `cannot decide` names the missing fact and reopen condition. If the selected pattern's entry or result condition is missing, preserve the endpoints, changed EntityOfConcern if any, and needed sentence as an explicit stop naming the missing arrow, use-claim, or application condition. Keep any continuity relation separate, and use `A.15.1` for actual authoring, materialisation, checking, or publication Work. The arrow, use assertion, operation application, and Work remain distinct and none supplies occurrence identity for the repaired world-side relation.
19. **Plain relaxation.** Short final wording retains a recoverable direct relation, actual participants, and visible escalation points.
20. **Neighboring subject result.** The repaired claim closes under one exact predicate or constraint selected in A.6.P:4.11, including exactly one of the four A.6.P.WMR families when that specialization is current; the neighboring pattern identifier is only its locator.

### A.6.P:8 - Common Anti-Patterns and How to Avoid Them

| Failure mode | Why it fails | Repair |
|---|---|---|
| Replace a broad word with a more technical synonym | The same participants and obtaining condition remain unresolved. | Ground the objects, select the direct relation, and write the readable sentence before naming. |
| Turn every relation phrase into a record-shaped episteme | Representation burden appears before any receiver needs the episteme or occurrence identity. | Use the direct sentence and apply the `A.6.REL` receiving-use test. |
| Let the declaration make the relation obtain | A declaration episteme is confused with the world-side relation. | Keep reusable laws and `SlotSpec`s in `A.6.0` and `A.6.5`; keep obtaining and identity with the pattern that defines the relation. |
| Treat the actual participant as occupying a declaration component | World-side participation is replaced by a schema metaphor. | State participation under the direct participant meaning; use the `SlotSpec` only inside a compatible reusable declaration. |
| Treat relation-dependent wording as an intrinsic kind | A participant described as result, input, or next continuation loses its own kind. | Apply the three-way distinction and use C.3 only for actual typed reasoning. |
| Use one generic relation-change verb | Occurrence change, assertion revision, declaration revision, evidence change, reference retargeting, EntityOfConcern retargeting, and representation change collapse. | Select the changed object and use the operation governed for that object. |
| Infer agency or identity from an active verb | Grammar is treated as ontological evidence. | Recover the exact acting system or direct identity rule independently of grammar. |
| Preserve a hidden union as a long list | The predicate changes meaning across listed participant kinds. | Recover the common predicate or split the relation kind and any compatible declarations. |
| Reverse a sentence for style | Participant meanings and polarity can change silently. | Use the direct inverse law or keep the forward predicate explicit. |
| Use a graph, tuple, function, arrow or table as ontological proof | Representation form is mistaken for an obtaining relation. | Recover what the elements mean and examine the claim and grounds under the direct rule. Add C.29 only for a separate mathematical representation or transfer question. |

### A.6.P:9 - Consequences

**Benefits**

- Engineers can retain short practical relation language without surrendering exact ontology.
- Hidden participants and kind collapses become repairable through one repeatable sequence.
- Reusable declarations, occurrence identity, designations, and representations appear only for named receiving uses.
- Assertion, declaration, occurrence, evidence, designation, publication, Bridge, and representation changes remain independently reviewable.
- Neighboring claims remain separate subject assertions under their exact predicates rather than entering a generic container.

**Costs and mitigations**

- Grounding an ambiguous phrase takes more work than lexical replacement. The first useful move and small candidate note keep that work bounded.
- Some claims become longer when their truth depends on scope, time, viewpoint, witness, or another participant. Plain relaxation restores readability after the precise reading is stable.
- Domain-specific direct relation patterns still need their own obtaining and identity rules. A.6.P supplies recovery and selection of the defining or constraining rule, not a universal relation ontology.

### A.6.P:10 - Rationale

The problem is ontological before it is lexical. A broad expression is dangerous because it can hide different objects, predicates, participant meanings, actual participants, or later claims and operations. Replacing the expression without recovering those objects merely moves the ambiguity.

FPF therefore begins with relation realism: a relation may obtain independently of an assertion about it. Actual participants retain their independently governed kinds while participating under relation-local meanings. An optional `RelationSignature` makes those meanings reusable as typed declaration content; an assertion or description can designate participants or an already recoverable occurrence; a representation corresponds to the selected object or claim content. None of those adjacent objects substitutes for world-side obtaining or identity.

Construction matters only when the direct ontology makes it identity-bearing. In that case, constructor, inputs, construction work or process, and output identity explain how another occurrence begins. Other relations may obtain without such a constructor. A.6.P therefore uses constructional analysis as a discriminating test rather than as a universal ontology.

Progressive elaboration preserves affordability. An engineer can stop at a readable direct fact. Typed declaration, assertion detail, occurrence identity, stable references, descriptions, publications, and representations appear only when a named later claim or operation depends on them. This order also explains why naming comes late: a good name helps designate a recovered distinction but cannot create it.

The changed-object rule prevents a second ontology collapse. Revising an assertion, declaration, evidence relation, designation, reference, publication, Bridge, or representation is not automatically a change in the direct relation being discussed. Naming the changed object makes continuity, evidence, and return conditions intelligible.

Neutral terminology matters because A.6.P is cross-domain. Every claim about an object uses the rule that defines or constrains that claim; A.6.P does not collect unlike objects under one local umbrella. Domain-specialized vocabulary enters only when a direct local pattern defines or constrains the current object.

### A.6.P:11 - SoTA-Echoing

#### A.6.P:11.1 - Ontological SoTA and constructive grounding

These sources constrain relation occurrence, identity, and construction. They are not interchangeable: FPF takes constructor-and-input discipline from the constructional-ontology line, uses BORO as a distinct 4D comparison, and treats implementation ontologies as stress comparators rather than proof.

| Ontological source and status | What it contributes | FPF adoption, mutation, and practical effect |
|---|---|---|
| Florio and Linnebo, [Introduction to Constructional Ontology](https://www.utwente.nl/en/eemcs/fois2024/resources/papers/florio-linnebo-introduction-to-constructional-ontology.pdf), 2024 | Separates constructors, constructor inputs, and constructional process, and examines functional and relational ways to characterize construction and output identity. | **Adopt the discriminating construction test.** Recover constructor, inputs, process, and identity only when the direct relation ontology makes construction constitutive. A storage operation is not thereby an ontological constructor. |
| Borgo and Righetti, [Towards Applied Constructional Ontology](https://doi.org/10.3233/FAIA250480), 2025 | Tests how constructional analysis can expose conceptual, structural, completeness, and consistency choices while marking unresolved application questions. | **Adopt as improvement pressure, not an imported ontology.** A.6.P exposes the exact construction and identity choice whenever it changes occurrence identity. |
| Partridge, [BORO Ontology](https://borosolutions.net/boro-ontology), C-FORS 2025 presentation | Presents BORO as a 4D extensional, category, and constructional ontology with an evolution method. | **Use as an ontological comparison under an explicit boundary.** A.6.P may use temporal extent when the direct identity rule needs it; FPF does not import universal 4D identity, unrestricted composition, or BORO's category architecture. |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint | Provides a foundational-ontology implementation with differentiated relation and reification patterns. | **Use the distinctions as a comparator; do not treat the implementation as proof.** Direct relation, optional explicit occurrence, assertion, and representation remain separate without importing the source category hierarchy. |
| [OntoUML Relator](https://ontouml.readthedocs.io/en/init-ontouml/classes/sortals/relator/index.html), specification lineage | Models a relator as a dependent truth-maker whose existence connects participants in a material relation. | **Retain as a material-relation comparator, not a universal answer.** The physical case requires the direct parthood ontology to identify and justify such a truth-maker before a relator is introduced; formal and other relations receive none by analogy. |
| Andrei Rodin, [Venus Homotopically](https://philsci-archive.pitt.edu/12116/), 2016 | Shows that identity across presentations is not obtained from a shared label alone; background, observations, and a trajectory can establish the same world-side referent. | **Retain as constructive-grounding lineage.** Candidate referents are separated through observations, identity tests, and direct-pattern conditions; naming does not close ontology. |

#### A.6.P:11.2 - Representation and implementation stress tests

These sources do not decide what exists. They test whether a representation can preserve the ontological distinctions selected above without turning a statement, row, graph term, tuple, or reifier into the world-side occurrence.

| Representation or implementation line | Distinction tested | Bounded use in A.6.P |
|---|---|---|
| [TypeDB 3.x `links` statement](https://typedb.com/docs/typeql-reference/statements/links/) and relation model | A query can select an explicit relation variable with named source-language role players, while shorthand remains available when no reference to the represented item is needed. | **Test progressive explicitness, not ontology.** A.6.P makes explicit occurrence identity conditional on a named receiver. TypeDB demonstrates one implementable representation; it does not establish the FPF relation kind, actual participation, obtaining condition, or identity rule. |
| [RDF 1.2 Concepts](https://www.w3.org/TR/rdf12-concepts/), Candidate Recommendation Snapshot, 7 April 2026 | RDF distinguishes proposition expressed by a triple term, assertion of a triple, and reifiers used for further statements. | **Test proposition, assertion, and reifier separation.** A statement term or graph edge can represent claim content but cannot establish that the direct relation obtains. |

#### A.6.P:11.3 - Service and access separation pressure

These sources constrain the recovery of service or access wording; they do not define a service ontology for FPF.

| Source line | Separation pressure | FPF adoption, adaptation, and rejection |
|---|---|---|
| [S-OPL: Service Ontology Pattern Language, specification v1.7](https://nemo.inf.ufes.br/en/projetos/patterns-and-pattern-languages/) | Offering, agreement, participants, and delivery are related but different modeling problems. | **Adopt** the separation; **adapt** it by using the existing patterns for promise content, commitment, speech acts, direct participation, system-role kinds, direct system-role assignments, Work, evidence, and evaluation. **Reject** the imported process ontology and service ontology, participant taxonomy, and any common service-situation carrier or service bundle. |
| [NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) | Requester, resource, policy decision, and enforcement functions must remain distinguishable in an access decision. | **Adopt** the demand to name the exact requester, requested use, resource, policy or grant, and enforcement facts; **adapt** grants through A.2.8.PER and performed enforcement through a system, assignment, and dated Work when those facts are current. **Reject** the component diagram as FPF ontology and infer neither `U.Access` nor `AccessRelation`. |
| [The Open Group ArchiMate 3.2 specification](https://pubs.opengroup.org/architecture/archimate32-doc/) | Service, interface or point of access, and realization system are not interchangeable. | **Retain as a comparison only.** Distinguish a service provision, access description or Method, exact access point, and realization bearer; use A.1 only for a separate system-dependent claim. **Reject** imported ArchiMate elements and relations, source-word-induced systemhood, and addressability as a classification rule. |

Further practice lineage includes ITIL 4, ISO 24617-2 speech-act work and SRE literature. ITIL offer and service-level wording can cue A.2.3 or A.6.C; A.2.9 separates a communicative act from its content and from any binding under A.2.3 or A.2.8. SRE interface, SLO, deployment, telemetry and incident distinctions help locate different subject claims. Apply those distinctions to the actual sentence; a word alone establishes no commitment, SpeechAct, Work or evidence relation.

These sources help separate the subject claims in §4.11a. Each claim retains its direct definition and obtaining basis; no shared service/access kind follows from the comparison.

Construction and identity comparisons inform the first recovery; representation questions follow the settled subject meaning. Service and access supply one recurring domain branch of the same method. The physical, clinical, epistemic and formal cases show how each receiving question selects its own direct rule.

**Reopen the smallest affected passage.** Start with the one claim, case, continuation, or source row that uses the changed fact. Reopen it when the exact subject predicate changes who participates, when the relation obtains, or how an occurrence is reidentified; when newer source evidence overturns or narrows the construction or reification distinction used there; or when an actual use can no longer reach the practical result or stopping boundary promised by that passage. Do not reopen the whole pattern unless the same change reaches several passages. If a continuation no longer matches the cited pattern's `Use this when` condition and promised result, stop using that continuation until it is repaired.

### A.6.P:12 - Relations

- The direct relation pattern defines or constrains obtaining, predicate satisfaction, and the occurrence-identity rule. After A.6.P recovers that relation, `A.6.REL` governs demand-driven explicit individuation, application of that identity rule, and occurrence-as-participant use.
- `A.6.0` governs `U.Signature` and compatible `RelationSignature` declarations; `A.6.5` governs declaration-local `SlotSpec`, `SlotKind`, participant `ValueKind`, and receiving-episteme designation mode.
- Use `A.6.RSIR` to distinguish direct participation, declaration, operation, assertion or description, and representation when interface, role, slot, field, parameter, or endpoint wording is the entry cue.
- `A.6.B` separates L, A, D, and E claims after the direct relation is recovered. When the next task needs a relation between epistemes or an operation that produces a receiving episteme, identify both endpoints independently under `C.2.1`. Use `A.6.3` for its compatible same-EntityOfConcern construction, `A.6.2` for its local effect-free arrow, and `A.6.4` for an exact different-EntityOfConcern arrow `r`, its separate C.2.1 bounded-use assertion `q` about exact `r`, and the separate three-valued current-case judgement defined there. If the selected pattern lacks an entry or result condition for the case, stop explicitly and name the missing arrow, use-claim, or application condition. Use `A.15.1` for actual authoring, materialisation, checking, or publication Work; keep the arrow, assertion, judgement, application, and Work distinct; and assert an edition or successor relation only after its own predicate is satisfied. Ordinary A.6.P repair stops before these objects.
- `A.6.6` provides specialized recovery for basedness. Service/access wording stays in A.6.P:4.11a until the exact predicate is recovered; cite the pattern that states it when the reference must travel. A.1.SCR applies only after one exact bearer or arrangement claim has been recovered and the decision depends on systemhood; A.1.STM applies only after recovery when the separate question is contribution to use of a named project system-of-interest. Cross-context and whole-part wording may use `A.6.9` or `A.6.H` only when that pattern's entry accepts the objects named in 4.11 and its result states the direct predicate and participants or an explicit blocker. If either check fails, keep the 4.11 blocker and name the missing predicate or unmet entry condition. A situation record, Card, or bundle does not replace the direct relation, claim-bearing episteme, or representation.
- `A.6.P.WMR` defines the method, work, result, production, delivery, acceptance, transfer, and receiving-use boundary and the four result families listed in 4.11.
- Use `A.6.RCD` after the reader can name the participants and the sentence the next task needs, but no current pattern supplies its predicate. Broad wording alone is not a `missing-governor` result.
- `C.2.1` governs assertions and descriptions. A.6.P identifies one candidate episteme `E`, one viewpoint episteme `P`, and the conformance question; `E.17.0` tests `EpistemeViewpointConformanceRelation(E,P)`. If the next task also asks whether `E` is a `U.View`, `E.17.0` handles that recognition separately. Viewpoint selection, evaluation, construction, representation, and publication do not establish conformance; `A.10` governs reliance, while `E.17` and `E.24.PUB` govern publication.
- Use `C.3` and `C.3.1` only if the next claim must quantify over a locally defined participant set, test membership or substitution, or order kinds. Otherwise do not mint a local kind.
- Use `A.1`, `A.2`, `A.2.1`, `A.3.1`, `A.3.4`, and `A.15.1` for the direct criteria for Systems, exact local system-role kinds, separate System-classification judgments, direct `U.SystemRoleAssignment` species, Methods, actual bounded change, and Work.
- The exact predicates defined in `A.10` constrain evidence relations, and those in `B.3` constrain assurance. `F.9` directly defines `Bridge` as a species of `U.Relation`, its two local-sense participants, its `BridgePredicateProfile`, the condition under which the predicate is true, and its occurrence-identity and recurrence rule. Use `C.2.1` separately for assertions, occurrence descriptions, and Bridge Cards; use `A.10` or `B.3` for evidence reliance or assurance, `E.24.PUB` for publication, and the receiving object's own pattern for any use that actually occurs. Use `A.6.RCD` only when the needed relation is not supplied by F.9 or another current defining or testing pattern after the participants and needed sentence are explicit. `C.30.P` defines or constrains architecture wording, `C.16.P` characteristic wording, `G.2` palette/front/archive distinctions, and `A.6.F` function-like wording. Each cited pattern contributes the named definition or constraint; its identifier is a locator only when that reference must travel.
- `A.16.1` and `B.4.1` retain cue material that has not reached a grounded relation-bearing claim; `B.5.2.0` carries a stabilized open explanatory question that has no selected relation answer; `A.16.2` records reopen, backoff, or respecification when a published relation overstates articulation, closure, or framing. Use `A.16.0` only when lineage, branching, loss, or responsibility-transfer history itself must be published.
- Use `F.19` for ordinary precise-plain-language repair and its plausible-reader test. Use `E.10` for wording triggers, E.10.ROLE to recover the actual branch of bare *role*, and `E.10.ARCH` for the shared recovery architecture. Use `F.18` for designation after objects and relations are recovered.

### A.6.P:12b - C.29 mathematical-lens account and representation boundary

Use C.29 when choosing or transferring a mathematical representation could expose a needed relation, invariant, obstruction, approximation or resource limit, or when a proposed inference exceeds the representation's supported correspondence. Its operation identifies a concrete mathematical object, establishes the needed correspondence, performs the mathematical work and returns the consequence with its limits. An adequate local equation, algorithm or domain model needs no C.29 note when no separate representation or transfer question remains. A relied-on representation still follows its selected interpretation conventions; neither a lens-use account nor visible form makes a world-side relation obtain or supplies occurrence identity.

For cross-context meaning, export or substitution wording, first distinguish designation, an operation and a semantic-correspondence claim under A.6.9. Only the last opens F.9: recover both local senses and test its direct Bridge predicate. F.9 supplies the obtaining condition and occurrence-identity rule when the two exact local-sense endpoints resolve, their interpretation bases differ, and the declared profile applies. `C.2.1` separately identifies an assertion, occurrence description, or Bridge Card and the bounded-use claim; `A.10` and `B.3` separately govern evidence reliance and assurance, `E.24.PUB` governs publication, and the receiving object's pattern governs any use that actually occurs. A changed claim, Card, evidence item, reliance result, or publication is not a changed Bridge occurrence. Use C.29 when a separate mathematical representation or transfer question remains. A representation may state or support a Bridge claim; its presence alone establishes neither the Bridge nor the represented world-side relation. If the sentence needs no cross-context correspondence or substitution claim, add no Bridge. If it needs another relation for which no current pattern supplies a defining or testing rule after the participants and needed sentence are explicit, record the established A.6.RCD `missing-governor` result.

### A.6.P:End
