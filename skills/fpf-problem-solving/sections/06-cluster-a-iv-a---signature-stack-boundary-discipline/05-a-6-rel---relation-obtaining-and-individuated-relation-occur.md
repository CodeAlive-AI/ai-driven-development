## A.6.REL - Relation Obtaining and Individuated Relation Occurrences

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative


### A.6.REL:1 - Problem frame

**Plain name.** Relation occurrence.

**Primary EntityOfConcern.** One obtaining relation occurrence of an admitted relation kind when one named receiving use needs that occurrence to remain distinguishable from another.

**Primary working reader.** An engineer who states a direct relation and needs to decide whether a named receiving use justifies exposing one occurrence's identity.

**Working concern and viewpoint.** Preserve the readable direct relation assertion while viewing occurrence identity from the named receiving use that depends on it; do not substitute an epistemic, designation, or representation-side object for the world-side relation.

**Use this when.** Use this pattern when one named receiving use needs to distinguish an obtaining relation occurrence from another occurrence of the same relation kind. A work-attribution assertion may designate one role-assignment occurrence; a reliability comparison may compare two installed-part occurrences; a dependent evaluative relation may have one actual-condition relation occurrence as a participant. Each case needs occurrence identity, not only a sentence that states the direct relation.

**First useful move.** Write the direct relation assertion with its named participants. Recover the direct governing pattern, then check that the relation obtains for those participants. In technical terms, those participants jointly satisfy the semantic predicate within the direct relation pattern's declared applicability and temporal conditions. Name the receiving use and apply its direct branch in section 4.2. If that use does not need one occurrence distinguished from another, keep the readable assertion and stop. If it does, apply the direct occurrence-identity rule before assigning an identifier, designating the occurrence in an episteme, or relying on it as a participant of another direct relation.

**What goes wrong if missed.** An epistemic, designation, or representation-side object is treated as what creates the relation it is meant to describe or designate. Repeated assignments or successive assembly episodes with the same participants then collapse into one. At the opposite extreme, every ordinary relational sentence is expanded into a relation-occurrence description episteme even though no receiving use needs that identity.

**What this buys.** Engineers can keep ordinary relation assertions readable. When a receiving use depends on exactly one occurrence, a system performing comparison or evaluation work can distinguish repetition, change, or constitution while assertions, descriptions, designations, representations, and publication occurrences retain their own identities.

**Not this pattern when.** If the wording does not yet identify the direct relation and participants, start with `A.6.P` or `A.6.RSIR`. If the only current basis is an assertion that denies the direct obtaining predicate or belongs to a forecast, scenario, counterfactual, permission, or another separately governed claim family, keep the claim episteme under `C.2.1` and its exact direct claim governor; none of those claim-side facts invents an obtaining occurrence. Only when an explicit reliance judgment is current for the declared use, keep its supported, refuted, or unresolved reliance result separately under `A.10` or the receiving evaluation; that reliance result likewise does not establish obtaining. When the direct relation owner independently establishes obtaining, A.6.REL remains available if a named receiving use needs occurrence identity. If the question concerns only the SlotSpecs of a reusable relation declaration, apply `A.6.5`. If no named receiving use depends on occurrence identity, stop at the direct relation sentence.

### A.6.REL:2 - Problem

When a later engineering use needs one obtaining relation occurrence to remain distinguishable from another, descriptions often state five different claim contents as if one assertion or identifier established them all. The claims have this dependency order; the order does not turn them into five project-time decisions:

1. the direct relation obtains for the named participants, those participants jointly satisfy its semantic predicate, one occurrence therefore exists, and the direct identity rule governs its reidentification and distinction from another occurrence;
2. FPF ontology settlement already admits occurrences of that relation kind under `U.Relation`; the direct pattern states the relation-specific participant meanings, obtaining condition, and occurrence-identity rule, while a compatible `RelationSignature` episteme declares corresponding SlotSpecs for reusable descriptions;
3. a system performing explicit-individuation work applies the admitted identity rule so the named receiving use can recoverably distinguish one occurrence; a separate relation-occurrence description episteme is produced only when the selected receiver needs that description;
4. an identifier designates that already recoverable occurrence under a reference scheme;
5. the selected receiving object is either an episteme whose content designates that occurrence, another direct relation that has the occurrence as a participant, or an operation-application assertion episteme whose content designates it as an argument under an A.6.1 `OperationAlgebra` SlotSpec.

The later claim contents do not make the earlier relation obtain. Root `U.Relation` admission is a corpus ontology decision governed by `E.24.UK`. `A.6.REL` supplies the common occurrence discipline, while each direct relation pattern supplies the relation-specific participant meanings, obtaining condition, and occurrence-identity rule used as the admission witness. Project work does not repeat that classification decision. A system performing explicit-individuation work applies the direct identity rule so one existing occurrence is recoverably distinguishable for the current use; that work neither creates the occurrence nor by itself requires a separate description episteme. A system performing naming work may subsequently associate a designator with the occurrence, and a receiving episteme may subsequently contain a reference that designates it.

Relation-heavy work often begins from a table row, graph edge, identifier, or reified statement. An engineer can then mistake the represented row, edge, identifier, or reifier identity for world-side relation identity. Applying this method permits exact use of relation-occurrence identity without reversing representation and ontology and without forcing a relation-occurrence description episteme into every readable sentence.

### A.6.REL:3 - Forces

| Force | Tension |
|---|---|
| Readable assertion vs explicit identity | Engineers need short relation sentences, while some later assertion or description epistemes need one stable occurrence as their EntityOfConcern or designated object and receiving direct relations may need it as a participant. |
| Relation obtaining vs predicate satisfaction | The world-side relation obtains; the actual relation participants, considered under their participant meanings, satisfy the truth-valued condition stated by the semantic predicate. Conflating these substitutes a formal expression for the obtaining relation. |
| Relation kind vs semantic predicate | A relation kind classifies occurrences under an identity rule; a predicate states a satisfaction condition for the jointly considered participants. One is not a synonym for the other. |
| Occurrence vs assertion or representation | An occurrence can exist before anyone asserts, describes, explicitly individuates, names, references, or represents it. |
| Participant identity vs repeated occurrences | Participant identities may suffice for some relation kinds, while repeated assignments, assembly episodes, and exact production, delivery, acceptance, or evaluation relations may need an additional domain discriminator supplied by their own patterns. |
| Construction vs description | A system can create a relation occurrence while performing constitutive work when the direct construction rule says so; that work occurrence may contribute to identity. Producing a row or description episteme is not constitutive by form. |
| Cross-domain reuse vs universal reification | Formal, physical, social, and engineering relations do not share one universal truth-maker or representation form. |
| Stable reference vs false creation | Identifiers enable later reference, but identifier assignment neither creates the occurrence nor makes the direct relation obtain. |

### A.6.REL:4 - Solution

Use progressive relation-occurrence individuation. Start from an obtaining direct relation and stop as soon as the named receiving use is served.

**Local relation-occurrence mantra.** *State the direct relation and recover its governing pattern. Check whether the relation obtains. Name the exact receiving use and its direct branch. If that use does not need occurrence identity, keep the readable assertion and stop. If it does, apply the direct identity rule to individuate the already-existing occurrence; only then designate it in an episteme, recover it as a relation participant, or designate it as an argument of a declared operation. If a system evaluates epistemes connected by a current A.10 evidence relation to an assertion that an object changed, identify that exact changed object and use its own governing pattern.*

This short formula keeps the progressive-individuation Solution in attention; it does not replace sections 4.1-4.7. It is a mnemonic, not a work plan or performed work. When a receiving use instead needs one reusable constraint-governed unfolding structure for those continuations and stops, `A.22.CGUS` governs that structure.

#### A.6.REL:4.1 - Apply the relation-object architecture discipline

**Relation-object architecture discipline** is the rule set in this subsection. It is not another U-kind. Conforming prose keeps the objects around one direct relation distinct, names the direct relation between adjacent objects, and uses a recoverable name for each current object. `A.6.5` specializes only the `SlotSpec` part of this rule set.

**Short use rule.** State the world-side relation and its actual participants first. Add another named object from the relation-object architecture only when the current receiving use depends on that exact object, and state its direct relation to the object already in view. The tables below help select that additional object and relation; they are not a mandatory form for ordinary relation prose.

The world-side relation comes first. An **actual relation participant** is one exact `U.Entity` participating in one obtaining relation occurrence under one relation-participant meaning. Participation leaves the entity under its independently governed intrinsic kind. A **relation occurrence** is the obtaining `U.Relation` occurrence itself. The direct relation obtains when the actual participants satisfy the obtaining predicate; the occurrence-identity rule provides the criteria for reidentification, continuity, and distinction from another occurrence. Signatures, assertions, names, references, and representations retain their separate identities.

##### A.6.REL:4.1.1 - World-side objects

| Canonical FPF name | What this object is | Direct relation to preserve | Naming rule | Direct governing pattern |
|---|---|---|---|---|
| **actual relation participant** | one exact `U.Entity`; this is a relation-qualified use of the entity, not a new kind | the entity participates in this relation occurrence under one relation-participant meaning | use the entity's direct kind and current name; use a governed designator only when naming or reference is current; in relation prose add the domain participant meaning, as in `Bearing_B as the installed part` | the participant's direct pattern and the direct relation pattern |
| **relation occurrence** | one obtaining occurrence admitted under `U.Relation` | the occurrence has the actual participants and is classified by the direct relation kind; it obtains when those participants satisfy the relation obtaining predicate within its applicability | use the readable direct relation sentence until stable occurrence reference is needed; then use a relation-occurrence designator assigned after the identity rule is applicable | the direct relation pattern and `A.6.REL` |

The phrase **actual relation participant** therefore never replaces the entity's own name. It says how that entity participates in this occurrence. Likewise, a readable sentence such as `Bearing_B is installed in Pump_P` can state that the direct relation obtains without first creating a relation-occurrence description episteme.

##### A.6.REL:4.1.2 - Relation-kind settlement

The relation kind is a classificatory distinction over relation occurrences. The accepted ontological settlement stated by the direct relation pattern or its ontic includes the relation-participant meanings, obtaining predicate, and occurrence-identity rule as semantic and rule content. World-side entities participate according to that settlement while retaining their own kinds.

| Canonical FPF name | What this object is | Direct relation to preserve | Naming rule | Direct governing pattern |
|---|---|---|---|---|
| **relation kind** | a classificatory distinction whose individuals are relation occurrences; `E.24.UK` admits a durable U-kind only when the direct relation pattern supplies the required witness, while a narrower relation distinction remains governed without automatic `U.*` admission | classifies relation occurrences governed by one obtaining predicate and one occurrence-identity rule | use the accepted domain relation name; a new durable Tech name follows `E.24.UK` admission and `F.18` naming, while morphology alone establishes neither | the direct relation pattern and `A.6.REL`; `E.24.UK` when durable U-kind admission is current |
| **relation-participant meaning** | relation-local semantic content specifying one domain contribution to the obtaining predicate | says how one actual participant contributes to the obtaining predicate while that participant retains its intrinsic kind | use a domain noun phrase such as `installed part` or `installation site`; keep it local to the direct relation kind | the direct relation pattern |
| **relation obtaining predicate** | truth-valued rule content over the actual participants considered under their relation-participant meanings | satisfaction of this predicate is the stated criterion for the direct relation obtaining | name it from the domain relation and the exact condition, for example `installed-at obtaining predicate`; notation used to express it keeps its source name under `C.29` | the direct relation pattern |
| **relation occurrence-identity rule** | rule content for reidentifying one occurrence and distinguishing it from another | a system applies this rule only after obtaining is established and a receiving use needs occurrence identity | name the exact world-side discriminator supplied by the direct relation pattern, such as participant-determined identity or maximal continuous obtaining interval | the direct relation pattern and `A.6.REL` |

**Public name settlement.** The following F.18 NameCard names the already governed root occurrence kind. It neither admits a new kind nor makes a relation obtain.

```text
NameCard:
  NameCardId: NC-U-RELATION
  GovernedValueRef: U.Relation under A.6.REL
  GoverningPatternRef: A.6.REL
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: individuable obtaining relation occurrence whose direct pattern supplies participants, obtaining conditions, and identity
  TechLabel: U.Relation
  PlainLabel: relation occurrence
  CandidateSet: U.Relation; U.RelationOccurrence; U.ObtainingRelation; U.IndividuatedRelation
  RejectedCandidates: longer candidates expose occurrence or obtaining but lose the established root retrieval head; U.Relation remains safe only with the A.6.REL identity discipline
  SelectionRationale: preserve the root name while distinguishing existence, kind admission, explicit individuation, identifier assignment, and reference use
  LineageEntries: existing local U.Relation declarations narrowed to individuable obtaining occurrences
  RefreshCondition: reopen if direct relation patterns cannot supply stable occurrence identity for an admitted relation kind
```

Use `U.Relation` for the admitted root kind only. A direct relation kind keeps its own governed name, participant meanings, obtaining predicate, and occurrence-identity rule.

In the world-side relation, the actual entities participate directly under the relation-participant meanings. When assertions and descriptions need typed reuse, a reusable declaration episteme declares those meanings without becoming the world-side relation.

##### A.6.REL:4.1.3 - Reusable declaration episteme

| Canonical FPF name | What this object is | Direct relation to preserve | Naming rule | Direct governing pattern |
|---|---|---|---|---|
| **`RelationSignature`** | a `U.Signature` declaration episteme whose EntityOfConcern is the direct relation kind | its content states a reusable declaration of the relation-participant meanings, obtaining predicate, applicability, occurrence-identity rule, and only the SlotSpecs needed by receiving typed uses | name it from the accepted relation-kind name, for example `InstalledAtRelationSignature`; the name denotes the declaration episteme, not the relation kind or an occurrence | `A.6.0` |
| **`SlotSpec`** | a declaration-content component identified inside one exact `RelationSignature` by its declaration-local `SlotKind` | corresponds to one relation-participant meaning and states the actual participant `ValueKind` plus the receiving-episteme designation mode | name the `SlotKind` with a domain noun phrase plus `Slot`, for example `InstalledPartSlot`; refer to the complete component as that SlotSpec in the named RelationSignature | `A.6.5` |

`SlotKind`, `ValueKind`, and `refMode` answer different questions. `SlotKind` identifies the declaration component locally. `ValueKind` is the independently governed kind of the actual relation participant. `refMode` states how a receiving episteme designates that participant. Together they specify one declaration component; world-side entities and occurrences keep their independently governed identities.

##### A.6.REL:4.1.4 - Claim and description epistemes

| Canonical FPF name | What this object is | Direct relation to preserve | Naming rule | Direct governing pattern |
|---|---|---|---|---|
| **relation-participant designation** | a value or governed reference in a receiving episteme; it retains its own value kind or RefKind | denotes the actual relation participant corresponding to one SlotSpec | use the SlotKind as the representation field label and the participant's own value or reference designator as the field value; the field value is not renamed as a participant kind | `C.2.1`, `A.6.5`, and `F.18` when durable naming is current |
| **relational assertion** | a claim-bearing `U.Episteme` | its content states affirmative or negative assertion polarity for the direct obtaining predicate with relation-participant designations; an affirmative assertion may also designate an already individuated occurrence only after the direct relation owner independently establishes obtaining; a forecast, scenario, counterfactual, permission, or other claim family keeps its own direct semantics, while supported, refuted, or unresolved reliance belongs to `A.10` or the receiving evaluation | name the asserted direct relation and its polarity; name the exact direct claim family whenever ordinary affirmation or denial is insufficient | `C.2.1`, the direct claim pattern, and `A.10` or the receiving evaluation for reliance |
| **relation-occurrence description episteme** | a `U.Episteme` whose EntityOfConcern is one explicitly individuated relation occurrence | describes that occurrence without replacing it or supplying its identity | use `description of <relation-occurrence designator>` in readable prose; give a reusable description-episteme kind its own governed name only when another use depends on that kind | `C.2.1` |

A receiving episteme can therefore contain a representation field whose label corresponds to a SlotKind and whose value is a relation-participant designation. That designation denotes an actual participant. The actual participant remains a `U.Entity`, and the obtaining relation occurrence remains a `U.Relation`. The receiving episteme keeps its own identity under `C.2.1`.

##### A.6.REL:4.1.5 - Naming, reference, and representation

| Canonical FPF name | What this object is | Direct relation to preserve | Naming rule | Direct governing pattern |
|---|---|---|---|---|
| **relation-occurrence designator** | a name associated with one already recoverable relation occurrence under a naming relation and effective reference scheme | designates the occurrence; assignment of the designator does not create or individuate it | apply `F.18`; select a name that exposes enough of the direct relation and identity distinction for its receiving use | `F.18` |
| **relation-occurrence reference** | a reference value of one exact RefKind under an effective `U.ReferenceScheme` | a system applying the governed resolution method obtains the already recoverable relation occurrence as referent | use the exact governed RefKind whose declared referent range admits this relation kind; a field ending in `Ref` names the reference value, not the occurrence | `F.18` and the direct RefKind pattern |
| **representation element** | an element of a declared representation under `C.29` | represents an object, claim content, or declaration, or corresponds to one independently governed object in this relation-object architecture | keep the source representation's own name and state an explicit correspondence naming both the source element and the FPF object; do not rename the source element into that object | `C.29` and the applicable representation-transition pattern |

A source-specific term remains the name of its source-side object until an explicit correspondence is stated. That correspondence never identifies a source representation element with the represented FPF object. Representation preservation stays with `C.29` and the selected representation-transition pattern, structural equivalence goes to `C.34`, and cross-context sameness goes to `A.6.9`.

##### A.6.REL:4.1.6 - Use the governing pattern for the current object

| Current question | Governing pattern |
|---|---|
| What relation obtains, under which participant meanings, predicate, and identity rule? | the direct relation pattern, with `A.6.REL` for occurrence individuation |
| What reusable declaration and SlotSpecs are needed? | `A.6.0` and `A.6.5` |
| What assertion or description episteme is current? | `C.2.1` and the direct claim or description pattern |
| What durable designator or reference is current? | `F.18` and the direct reference pattern |
| What selected representation element is current, and what object or claim content does it represent? | `C.29` and the selected representation-transition pattern |
| Which object is hidden by unresolved source wording? | `A.6.P`, `A.6.RSIR`, and `E.10`, followed by the direct governing pattern recovered there |

Only systems perform authoring, evaluation, individuation, naming, reference-resolution, and representation work. Relation occurrences obtain; epistemes contain declarations, assertions, and descriptions; names and references stand in governed designation relations. This grammar keeps agency with systems without suppressing the semantic relations that make the relation-object architecture useful.

##### A.6.REL:4.1.7 - Name only the minimum current object

The relation-object architecture organizes the distinct objects that may become current; it is not a publication form repeated for every relation sentence. Stable relation-kind semantics belong once in the direct relation pattern or ontic. A reusable declaration belongs once in its `RelationSignature`. A durable name belongs once in its F.18 naming settlement. Later prose names the object current for its use and cites the direct governing pattern for already established neighboring objects.

| Current use | Minimum sufficient text | Add another object only when |
|---|---|---|
| ordinary direct relation assertion | one readable direct relation sentence naming the actual participants | predicate interpretation or occurrence identity changes the next engineering move |
| repeated typed assertion or description episteme | cite the direct `RelationSignature`; use representation field labels corresponding to its SlotKinds with exact relation-participant designations | the declaration, ValueKind, RefKind, or correspondence itself is under examination |
| occurrence-dependent assertion or description episteme | use the relation-occurrence designator or reference and cite the direct occurrence-identity rule | participant meaning, obtaining, continuity, or repeated-occurrence identity is disputed |
| representation-dependent use | name the source representation element, the represented FPF object or claim content, and their explicit correspondence | representation preservation or loss is current under `C.29`, structural equivalence is current under `C.34`, or cross-context sameness is current under `A.6.9` |
| ontology or wording repair | traverse the complete relation-object architecture in this subsection | the repair has not yet recovered a unique current object and direct governing pattern |

In recognition text, prefer the readable direct relation sentence. Put the reusable declaration, occurrence-identity rule, naming settlement, or representation correspondence in nearby Tech or assurance text governed by its direct pattern, and refer to it when another declared use depends on it. Precision comes from recoverable governing patterns and explicit relations between adjacent objects, not from repeating the complete architecture.

This rule keeps elaboration additive. Each new receiving use introduces only the object on which that use depends and the object's direct relation to an already recoverable object. When the use stops at the world-side relation, the prose adds no signature, occurrence-description, naming, or representation apparatus.

#### A.6.REL:4.2 - Apply the receiving-use test

Here **receiving use** is a Plain head, not a common FPF kind. Resolve it to the exact receiving object before applying the test. A receiving assertion or description is an episteme under `C.2.1` and designates the occurrence. A receiving direct relation has the occurrence itself as a world-side participant. For a declared operation, A.6.1 governs the `OperationAlgebra` and argument SlotSpec, while an operation-application assertion episteme designates the occurrence as that argument; any acting system, enacted method, and performed work remain separately governed. Name the exact receiving object and governing pattern.

1. Name the direct relation kind and participants in a readable sentence.
2. Recover the direct governing pattern, relation obtaining predicate, relation-participant meanings, actual relation participants, applicability, and relation occurrence-identity rule. Cite the established settlement rather than restating it unless this use introduces or changes one of those objects. Recover the `RelationSignature` SlotSpecs only when typed assertion or description reuse is current.
3. Check through the direct relation owner whether the relation obtains and the named participants jointly satisfy the predicate. A denial, a forecast, scenario, counterfactual, permission, or another separately governed claim, and supported, refuted, or unresolved reliance do not establish an obtaining occurrence; do not infer occurrence identity from any of them. Individuate only an occurrence whose obtaining the direct owner establishes, or return to the exact direct claim pattern or `A.6.P`.
4. Ask whether the named receiving assertion or description episteme, direct relation, or operation-application assertion episteme depends on this occurrence being distinguishable from another.
5. If not, keep the readable assertion and stop. Do not create a relation-occurrence description episteme for completeness.
6. If yes, apply the direct identity rule and explicitly individuate one occurrence.
7. Assign an identifier only when stable reference is needed.
8. Apply the selected receiving branch: designate the occurrence in the receiving episteme; for a receiving direct relation, verify its obtaining with that occurrence as a participant; or designate the occurrence as an argument in the operation-application assertion episteme according to the A.6.1 SlotSpec.

Occurrence existence depends on the direct relation obtaining. Reidentification and distinction from another occurrence depend on the direct identity rule. Explicit individuation depends on a named receiving use. Identifier assignment and reference use depend on an already recoverable occurrence. None of the later moves makes the earlier relation obtain.

#### A.6.REL:4.3 - Select an identity rule that survives repetition

Use participant-determined identity only when the direct ontology establishes that two distinct occurrences of this relation kind cannot have the same participant identities. The `RelationSignature` SlotSpecs declare how assertion or description episteme content designates those participants; neither the SlotKinds nor any database-row or representation key contributes to world-side identity.

When the same participants can enter more than one occurrence, the direct pattern declares the discriminator that exists in that domain:

| Occurrence-identity condition | Direct identity contribution |
|---|---|
| One occurrence is determined by its participants | the direct relation kind and identities of the actual participants jointly determine occurrence identity |
| The same participants stand in the relation during separate episodes | participant identities together with the maximal continuous obtaining interval or another declared episode boundary determine occurrence identity |
| Performed constituting work creates a new occurrence | participant identities together with the constituting work occurrence determine occurrence identity |
| A transformation occurrence rather than its producing work contributes to identity | participant identities together with that transformation occurrence determine occurrence identity, but only when the direct transformation and relation patterns include it in the relation occurrence-identity rule |
| The relation kind uses another domain identity rule | the exact discriminator supplied by its direct governing pattern |

When a relation occurrence is a constructed result under its direct construction rule, recover the constructing system, its constructor role assignment, the enacted constructor method, input entities, performed construction work, and the identity contribution of that work occurrence. For an installed-part relation, the installer system creates the new assembly episode while performing installation work; the parthood identity rule may use that work occurrence to distinguish the episode. Producing only an epistemic object, designation, or representation does not construct the relation unless the direct ontology states that the corresponding performed work is constitutive.

A changed episteme contributes to occurrence identity only when that episteme itself is a constitutive participant under the direct identity rule. A changed publication occurrence contributes only when that publication occurrence is itself a constitutive participant under the same rule. A system merely learning about the relation, describing it, or publishing an episteme about it changes no world-side occurrence.

#### A.6.REL:4.4 - Separate occurrence, assertion, reifier, relator, description, and publication

A relational assertion is an episteme whose content affirms or denies the direct obtaining predicate for the designated participants. Forecast, scenario, counterfactual, permission, and other claim families keep their exact direct governors rather than entering one common catch-all field; `A.10` or the receiving evaluation separately states supported, refuted, or unresolved reliance. The assertion and its reliance posture can be revised or superseded while the world-side relation remains unchanged.

A reifier is a representation-side term or node. A system may use it to represent statements about a proposition, assertion episteme, or relation-occurrence description episteme. Its presence does not make the direct relation obtain and is not a world-side occurrence-identity rule.

A direct material-relation ontology may identify a relator: a dependent material truth-maker through which its participants stand in the relation. Introduce one only when that ontology identifies the relator, its dependence relations to the participants, and its occurrence-identity rule. Do not generalize that relator to relation kinds whose direct ontology does not provide those three settlements.

An episteme can describe a relation occurrence. A second episteme can describe the first episteme. Under a publication-relation occurrence, a selected episteme edition is available to the declared audience and use. If an information carrier is current, `E.17` governs its publication-kit use and `E.24.PUB` governs publication; carrier identity replaces neither episteme identity nor relation-occurrence identity. None of these objects replaces the direct occurrence-identity rule.

#### A.6.REL:4.5 - Use one relation occurrence as a participant of another

Before one relation occurrence participates in another relation, explicitly individuate the first occurrence under its direct identity rule. The receiving direct pattern states a participant meaning whose ValueKind admits `U.Relation` or the exact relation kind; its `RelationSignature` episteme declares the corresponding SlotSpec. In the world-side receiving occurrence, the first occurrence itself is the participant. A participant designation in the receiving assertion or description episteme denotes it by value or through the RefKind declared by that SlotSpec.

This is ordinary typed participation, not a relation-of-relations exception. The first occurrence keeps its kind, participants, obtaining condition, and identity. The receiving relation keeps its participant meanings, obtaining condition, and identity rule; the receiving `RelationSignature` keeps its SlotSpecs. The reference used by an assertion belongs to neither world-side occurrence.

#### A.6.REL:4.6 - Keep ordinary relation use lightweight

Ordinary users write one readable direct relation assertion with named participants and stop when no named receiving assertion or description episteme, direct relation, or declared operation application depends on more. The direct relation pattern states the shared participant meanings, obtaining predicate, and identity rule once; later uses cite that settlement. Add only the independent declaration, occurrence-identity, description, designation, or reference branch consumed by the named receiving use.

This is demand-driven progressive elaboration within the Solution, not a drafting sequence. The branches below share one recovered direct relation; they are not stages, and no branch requires the branch written above it.

```text
readable direct relation assertion with named participants
  +-- direct obtaining and predicate-satisfaction check, whenever occurrence use is current; affirmative assertion polarity alone does not supply obtaining
  +-- RelationSignature and SlotSpecs, when typed reuse matters
  +-- explicit occurrence individuation, when a named receiving use needs identity
      +-- relation-occurrence description episteme, when a receiving episteme describes the occurrence
      +-- identifier assignment, when stable cross-reference matters
      +-- occurrence as a participant of another direct relation, when that receiving predicate consumes it
      +-- occurrence designation in a receiving episteme, when that episteme contains a designation of it
```

This is a C.29 representation of independent optional increases in explicitness. Its branch marks are representation elements, not direct relations or work occurrences. The indentation under explicit occurrence individuation records only that description, identifier assignment, occurrence participation, and later designation require one recoverable occurrence; it does not make a `RelationSignature` prerequisite for occurrence identity. The represented branches are neither a plan nor a method for documentation work and do not construct the world-side relation.

#### A.6.REL:4.7 - Keep world-side change separate from episteme editions

When a system evaluates epistemes connected by a current A.10 evidence relation to an assertion that an object changed, first select that changed object:

| Changed object | Exact move |
|---|---|
| direct relation occurrence | evaluate continued identity or a distinct occurrence under the direct identity rule; for a temporally extended occurrence, establish its beginning, continuation, cessation, or split |
| relational assertion | revise, retract, replace, or supersede the assertion episteme under `C.2.1` |
| `RelationSignature` | revise the reusable declaration and establish its edition relation under `A.6.0` |
| identifier assignment | assign, retire, or replace the designator under `F.18` |
| reference use in an episteme | reinterpret or retarget the designation under `F.18` and the receiving SlotSpec |
| description episteme | revise the episteme or establish another edition under `C.2.1` |
| publication occurrence | end the current publication occurrence or establish another under `E.17` and `E.24.PUB` |

A relation occurrence has identity under its direct rule; a temporally extended occurrence also has temporal history under that rule. When a system performs revision work on an episteme, the episteme or its edition changes; no world-side occurrence changes unless a system applies the direct identity rule and establishes cessation, continuation, or another occurrence. Another edition of an assertion, signature, or description episteme, or another publication occurrence, entails no new relation occurrence unless a system applying the direct identity rule separately distinguishes one.

### A.6.REL:5 - Archetypal Grounding

#### A.6.REL:5.1 - Physical assembly through the relation-object architecture

Start with `Bearing_B isPartOf Pump_P` and trace only the objects needed by the current use.

1. **World-side entities and occurrence.** `Bearing_B` and `Pump_P` retain their independently governed holon kinds and names. In this occurrence, the bearing participates under the installed-part meaning and the pump under the assembly-whole meaning. The direct installed-part relation obtains while its domain predicate is satisfied.
2. **Relation-kind settlement.** The direct parthood pattern contains the two relation-participant meanings, the installed-part obtaining predicate, and the occurrence-identity rule. The identity rule states whether continuity is determined by one maximal continuous installation interval, constituting installation work, or another exact world-side discriminator stated by that pattern.
3. **Reusable declaration.** When several maintenance assertions use one `InstalledPartRelationSignature`, that signature contains `InstalledPartSlot` and `AssemblyWholeSlot`. Each SlotSpec states `U.Holon` as ValueKind and `U.HolonRef` as RefKind. These SlotKinds are declaration-local names corresponding to the two relation-participant meanings.
4. **Assertion and relation-participant designations.** A maintenance assertion may use `InstalledPartSlot` as the field label and `Bearing_B_Ref` as its value, and `AssemblyWholeSlot` with `Pump_P_Ref`. The two reference values are relation-participant designations. Resolution under the effective reference scheme yields the bearing and pump; the assertion content claims that the direct relation obtains. If current maintenance work needs no occurrence identity, the engineer stops here.
5. **Occurrence identity, designator, and reference.** A system performing reliability-analysis work compares the installation before removal with the installation after reinstallation. A system performing relation-identification work applies the direct identity rule and distinguishes two occurrences when the exact world-side discriminator stated by that rule differs. A system performing naming work can then associate a designator such as `Bearing_B installation in Pump_P, episode 2` with the second occurrence. A `U.EntityRef` constrained to the installed-part relation kind may serve as its relation-occurrence reference for a receiving reliability assertion.
6. **Representation.** A database row or diagram edge may represent the assertion episteme or relation-occurrence description episteme under `C.29`. Its key, fields, and edge endpoints keep their representation-side meanings. A declared C.29 correspondence relates each representation element to the assertion field, relation-participant designation, or occurrence reference used by the receiving episteme; row or edge identity does not replace the direct occurrence-identity rule.

The practical payoff is visible at each stop. Ordinary maintenance work keeps the readable relation sentence. Repeated typed assertions add the signature and designations. A system comparing repeated installation episodes performs explicit-individuation work when the comparison depends on occurrence identity. Stable cross-reference use motivates naming and reference work. No earlier object is renamed as a later one.

#### A.6.REL:5.2 - Repeated role assignment

**Tell.** `Robot_7 holds InspectorRole` is sufficient while the current assignment alone matters.

**Show identity-dependent use.** The robot holds the role during two separated inspection intervals, and later work attribution names the assignment current during the second work occurrence. Under `A.2.1`, each assignment occurrence is identified by its fixed holder, role value, role-taxonomy episteme, effective reference scheme, and one uninterrupted obtaining interval. The demonstrated gap ends the first occurrence; later resumption begins another. The attribution assertion explicitly designates the second occurrence. Assignment-signature, assertion, and roster epistemes may describe the assignment; an evidence relation may connect one of those epistemes to an attribution assertion about the assignment. Under a publication-relation occurrence, one selected edition may be available to its declared audience and use. None constitutes the assignment merely by form.

#### A.6.REL:5.3 - Formal reduced case

The expression `3 < 5` is assertion content written in a mathematical notation. Under the referenced arithmetic structure, the values three and five satisfy the less-than predicate. The expression is not thereby a relation occurrence. No receiving use in this case needs the obtaining less-than relation occurrence explicitly individuated under `U.Relation`, so the engineer stops at the assertion. A graph edge or RDF reifier introduced by tooling remains a representation of the proposition or assertion and is not an occurrence-identity rule in the formal subject domain.

#### A.6.REL:5.4 - Relation occurrence as a participant

`C.22.PFR` has one actual-condition relation occurrence and one problem-criterion-applicability relation occurrence as world-side participants. Each is individuated under its own direct identity rule. The PFR direct pattern states those two participant meanings, its obtaining condition, and its identity rule; the PFR `RelationSignature` episteme declares the corresponding SlotSpecs. A PFR assertion designates the two occurrences according to those SlotSpecs. PFR is a direct relation, not an episteme whose content merely groups two assertions.

#### A.6.REL:5.5 - Description and publication recursion through the relation-object architecture

Let `R1` be an already individuated installed-part relation occurrence between a bearing and a pump.

1. An installation-description episteme `E1` has `R1` as its EntityOfConcern. In the C.2.1 declaration, the entity-of-concern relation-participant meaning corresponds to `EntityOfConcernSlot`. In a card representation of `E1`, the field label `entityOfConcernRef` corresponds to that SlotKind and its `U.EntityRef` value is a relation-participant designation that resolves to `R1`.
2. A second episteme `E2` contains the result of evaluation work concerning the adequacy of `E1`. Its own `EntityOfConcernSlot` designation resolves to `E1`, not to `R1`. The two epistemes therefore have different EntitiesOfConcern and retain separate C.2.1 identities: `E1` describes `R1`, while `E2` evaluates the adequacy of `E1`.
3. Under a publication-relation occurrence, the current edition of `E1` is available to a declared audience and use. The selected episteme edition is an actual participant of that publication relation under the publication pattern's participant meaning. The publication form and its representation elements retain their own kinds and correspond to the published episteme only through the declared publication and representation relations.

A system performing revision work can establish another edition of `E1` or `E2`; a system performing publication work can establish another publication-relation occurrence for a selected edition. `R1` continues or ceases only as the installed-part obtaining predicate and occurrence-identity rule determine. This recursive case preserves the distinction: a description episteme can itself become the actual participant or EntityOfConcern of another relation without becoming the relation occurrence it describes.

### A.6.REL:6 - Bias-Annotation

This pattern has an individuation bias because it serves receiving uses that need relation identity. The lightweight stop rule prevents that bias from turning every direct relation into an explicit relation-occurrence description episteme.

The physical and role-assignment cases can over-emphasize participant identities. A direct relation pattern may instead use constituting work or another exact world-side discriminator. The repeated-episode cases can also over-emphasize temporal extent. Time enters an occurrence-identity rule only when the direct pattern states that contribution.

Engineers can easily picture relation instances through data-model examples. The prescribed move therefore begins with direct relation obtaining, predicate satisfaction, and the direct identity rule. A system introduces database rows, graph edges, reifiers, tuples, and data-model objects only afterwards as representations for a declared use.

### A.6.REL:7 - Conformance Checklist

1. Across the direct governing pattern and the current use, the relation kind, relation-participant meanings, relation obtaining predicate, actual relation participants, applicability, relation occurrence-identity rule, and any currently needed `RelationSignature` SlotSpecs are recoverable. An ordinary relation sentence remains complete without repeating that settlement.
2. The text does not conflate relation obtaining, predicate satisfaction, root-kind admission, explicit-individuation work, identifier assignment, and reference use.
3. Root `U.Relation` admission is governed by `E.24.UK` from the common `A.6.REL` discipline and the relation-specific witness supplied by each direct relation pattern; project use does not repeat the admission decision.
4. The current use names one receiving assertion or description episteme, direct relation, or operation-application assertion episteme whose dependence on a distinguishable occurrence makes explicit occurrence identity necessary.
5. A denial, a separately governed non-actual claim, or unresolved reliance does not create an obtaining occurrence; affirmative polarity alone does not create one either.
6. The direct governing pattern declares the occurrence-identity rule.
7. Participant-determined identity is used only when the direct ontology establishes that the same participant identities cannot recur in distinct occurrences of that relation kind.
8. When the same participants can recur, the direct pattern declares the domain discriminator; maximal continuous obtaining interval and constituting work are possible choices only when that pattern includes them in the occurrence-identity rule.
9. When construction is constitutive, the constructing system, input entities, performed construction work, and identity contribution are named; representation creation is not substituted for construction.
10. Each object in the relation-object architecture is reidentified under its direct governing pattern and connected to adjacent objects only by the direct relations stated in section 4.1.
11. A relation occurrence used as another relation's world-side participant is individuated first; the receiving assertion's reference remains distinct from that participant.
12. Ordinary use can stop at a readable direct relation sentence when no receiving use needs occurrence identity; when identity is current, the direct identity rule can be applied without first creating a `RelationSignature`.
13. Another episteme edition, publication occurrence, name association, or reference use is not evidence of another world-side relation occurrence; apply the direct occurrence-identity rule independently.

### A.6.REL:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
|---|---|---|
| Representation-first relation | A table row, edge, or object identifier is treated as what makes the relation obtain. | State the direct relation, participants, and obtaining condition first; treat the row as a representation unless the direct ontology demonstrates that the corresponding representation-producing work is constitutive. |
| Predicate-as-relation | A semantic predicate or its expression is treated as the world-side occurrence. | State the direct relation and its actual participants; use the predicate only to state the truth-valued obtaining condition. |
| Designation treated as occurrence creation | A relation is said to exist only because another assertion designates it. | Establish occurrence existence under the direct pattern; let the named receiving dependency justify only explicit-individuation and reference work. |
| Participant-identity collapse | Two assignments or part-relation episodes with the same participants become one occurrence. | Apply the direct identity rule and recover its domain discriminator; use a maximal continuous obtaining interval or constituting work only when that rule includes it in occurrence identity. |
| Observation-window identity | A new measurement or assessment window is treated as a new relation occurrence. | Keep the observation window with its measurement or assessment assertion; recognize another occurrence only when the direct relation ceases and resumes or the direct identity rule supplies another discriminator. |
| Edition-as-world-change | Another edition of an assertion, signature, or description episteme, or another publication occurrence, is called a new version of the world-side relation. | Select the changed episteme or publication occurrence first, then re-evaluate the world-side relation through the current A.10 evidence relation; recognize a distinct occurrence only under the direct identity rule. |
| Relator by analogy | A dependent truth-maker is introduced although the direct relation ontology does not identify its dependence relations and occurrence identity. | Introduce a relator only where the direct material ontology identifies the relator, its dependence relations to the participants, and its occurrence-identity rule. |
| Full occurrence description by default | Simple engineering prose becomes a mandatory signature-and-description exercise. | Apply the receiving-use test and stop after the direct relation sentence when no occurrence identity is consumed. |

### A.6.REL:9 - Consequences

**Benefits.** The content of receiving epistemes can designate repeated relation occurrences stably; receiving relations can have those occurrences as typed participants. The discipline applies to physical composition, role assignment, exact production, delivery, acceptance and evaluation relations, formal relation assertions, and dependent evaluative relations without making their obtaining conditions or identity rules identical. Ordinary prose remains readable because explicit individuation is demand-driven.

**Costs.** A direct relation pattern needs a stated occurrence-identity rule, not only participants, when a receiving assertion, description, direct relation, or declared operation application depends on distinguishing one occurrence from another. A system performing relation-identification work establishes whether participants, temporal extent, constituting work, or another domain discriminator distinguishes repetition. Data schemas that used row identity as ontology may need to expose the domain identity they hid.

**Limits.** `A.6.REL` does not decide whether a particular direct relation obtains, define every relation kind, or prescribe a storage model. It does not supply evidence, comparison, publication, forecast, scenario, counterfactual, permission, or temporal semantics governed by neighboring patterns. It also does not turn assertion polarity, a separately governed claim family, or a reliance posture into an obtaining occurrence.

### A.6.REL:10 - Rationale

Applying this method lets an engineer use exact occurrence identity without equating ontology with documentation. A direct relation can obtain for its participants before an FPF episteme states a sentence about it. The actual relation participants, considered under their participant meanings, satisfy the semantic predicate within the direct relation pattern's declared applicability and temporal conditions; an assertion is an episteme whose content affirms or denies that predicate under its exact direct claim family; `A.10` or the receiving evaluation separately governs supported, refuted, or unresolved reliance; explicit-individuation work is performed by a system for a named receiving use; and an identifier only enables later reference. Keeping those objects and moves distinct prevents semio-bias in which an episteme is mistaken for the world-side relation.

The identity rule belongs to the direct relation pattern because the direct ontology determines whether participant identities suffice. The same holder and role value can stand in two assignments, and the same component and whole can participate in distinct assembly episodes. Conversely, an ordinary formal order assertion may need no explicit occurrence object in project work. A universal key would be too weak for repetition and too heavy for ordinary use.

Assertion, description, and signature epistemes can have editions; a system performing publication work can establish another publication-relation occurrence for a selected edition. A relation occurrence instead begins, continues, or ceases under its direct rule; when a system applying that rule distinguishes another occurrence, the other occurrence has its own identity. Keeping episteme edition change, publication occurrence, and relation occurrence continuity separate makes repair local and prevents publication history from masquerading as world history.

### A.6.REL:11 - SoTA-Echoing

#### Ontological SoTA and constructional sources

This pattern uses these sources to constrain its account of occurrence existence and identity. Their role here is ontological comparison, not notation selection.

| Ontological source | What it contributes | FPF adoption, mutation, and practical effect |
|---|---|---|
| Florio and Linnebo, [Introduction to Constructional Ontology](https://www.utwente.nl/en/eemcs/fois2024/resources/papers/florio-linnebo-introduction-to-constructional-ontology.pdf), 2024 | Separates constructors, constructor inputs, the source account's construction process, and output identity. | **Adopt the construction test and adapt the source process to FPF method and work distinctions.** Section 4.3 asks which system acts as constructor, which method it enacts, which entities are inputs, which work it performs, and how that work occurrence contributes to output or relation identity. Row creation and assertion remain non-constructive unless the direct rule declares the corresponding work constitutive. |
| Borgo and Righetti, [Towards Applied Constructional Ontology](https://doi.org/10.3233/FAIA250480), 2025 | Tests how constructional analysis could reconstruct existing foundational ontologies and exposes conceptual, structural, completeness, and consistency questions; it is an early applied step, not a finished recipe. | **Adapt as current improvement pressure with that maturity boundary.** Checklist 9 and the physical case require a recoverable construction choice instead of accepting an inherited relation representation or taxonomy. |
| Partridge, [BORO Ontology](https://borosolutions.net/boro-ontology), C-FORS 2025 presentation | Presents a 4D extensional, categorical, and constructional ontology with an ontology-evolution method. | **Adapt as a current ontological comparison under a boundary.** Sections 4.3 and 5.1 use temporal extent and constituting occurrences when the direct identity rule needs them. FPF rejects universal 4D identity, unrestricted composition, and BORO's category architecture for this pattern. |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint | Provides a current foundational-ontology implementation with differentiated relational-aspect and reification patterns. | **Adapt its ontological distinctions as a current comparison; reject its OWL implementation as proof of FPF occurrence existence or identity.** Section 4.4 separates direct relation, assertion, reifier, and optional relator without importing the complete category hierarchy. |
| [OntoUML Relator](https://ontouml.readthedocs.io/en/init-ontouml/classes/sortals/relator/index.html), specification lineage | Models a relator as a dependent truth-maker for a material relation. | **Reject as current competitive SoTA; retain and adapt as a lineage comparison for material relators.** Section 4.4 permits a relator only when the direct material ontology identifies the relator, its dependence relations to the participants, and its occurrence-identity rule. |

#### Representation and implementation stress tests

This pattern uses these sources to test whether the selected ontological distinctions can be represented and used. They do not determine what relation occurrences exist or how they are identified.

| Representation or implementation line | Distinction tested | Bounded use in A.6.REL |
|---|---|---|
| [TypeDB 3.x `links` statement](https://typedb.com/docs/typeql-reference/statements/links/) and current relation model | A query can expose a relation variable with named source-language role players, while shorthand remains available when the relation instance need not be referenced. TypeDB role player is not FPF `U.Role`. | **Adapt as a representation stress test; reject as an ontology source.** Sections 4.2, 4.5, and 4.6 preserve a readable direct relation before explicit individuation. TypeDB demonstrates one implementable representation; it does not establish the FPF relation kind, obtaining condition, or identity rule. |
| [RDF 1.2 Concepts](https://www.w3.org/TR/rdf12-concepts/), Candidate Recommendation Snapshot, 7 April 2026 | Distinguishes a proposition expressed by a triple term, assertion of a triple, and reifiers used for further statements. | **Adapt as a representation stress test; reject graph syntax and reifier identity as world-side identity sources.** Sections 4.4 and 5.3 apply that distinction to proposition, assertion, and reifier separation. |

This pattern uses the ontological sources to constrain its occurrence-existence and occurrence-identity method. It uses the representation sources to test implementability only after those choices are made. The worked cases expose both boundaries outside information-system projects.

### A.6.REL:12 - Relations

- `A.6.0` declares RelationSignature participant SlotSpecs and restates the direct predicate, applicability, and exact identity rule for reuse without making the relation obtain.
- `A.6.5` separates world-side participants from RelationSignature SlotKinds and from participant designations in assertions or descriptions.
- `A.6.P` governs restoration of hidden direct relations and participants before occurrence identity is attempted.
- `A.6.RSIR` governs selection among a direct relation, relation-participant meaning, declaration SlotSpec, `RelationSignature`, and another exact interface object when wording is ambiguous.
- `A.2.1` governs role-assignment obtaining and identity; `F.6` governs later attribution to performed work.
- `A.14` and direct mereology patterns govern part-relation identity and part-whole change.
- `A.15.1` governs work occurrence identity and readable links to separately governed participation, change, operation-result, production, evaluation, delivery, and acceptance claims.
- `C.2.1` governs assertions and descriptions about relation obtaining, predicate satisfaction, and occurrences; `E.17` and `E.24.PUB` govern publication relations.
- `C.22.PFR` supplies a worked case with two explicitly individuated relation occurrences participating in one dependent evaluative relation.
- `C.29` governs a declared mathematical or data-model lens, including graph, tuple, or database representations used to describe relation structure.
- `E.24` governs ontic settlement and `E.24.UK` governs root `U.Relation` admission. `A.6.REL` supplies the common occurrence discipline, and each direct relation pattern supplies the relation-specific witness. `E.24.CD` dispatches an unsettled ontic candidate only after those exits are recoverable; none replaces the direct occurrence-identity rule.
- `F.18` governs durable names and identifier use after the relation kind and occurrence identity are settled.

### A.6.REL:End

