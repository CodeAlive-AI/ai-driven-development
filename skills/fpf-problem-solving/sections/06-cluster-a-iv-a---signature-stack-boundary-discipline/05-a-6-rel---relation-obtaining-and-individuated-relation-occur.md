## A.6.REL - Relation Obtaining and Individuated Relation Occurrences

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative


### A.6.REL:1 - Problem frame

**Plain name.** Relation occurrence.

**Primary EntityOfConcern.** One obtaining relation occurrence of an admitted relation kind, opened only when later work must distinguish it from another occurrence of that same relation.

**Primary working reader.** An engineer who has stated a direct relation and must decide whether a readable current report is enough or later work must distinguish repeated occurrences.

**Working concern and viewpoint.** Preserve the readable direct relation assertion and ask first what later work must distinguish. Open occurrence identity only when that work must tell this occurrence from another; do not substitute an epistemic, designation, or representation-side object for the world-side relation.

**Use this when.** Use this pattern when later use must tell one obtaining relation occurrence from another occurrence of the same relation. With `Robot-7 is assigned as inspector through InspectionAssignment-17`, a report that only says who is currently assigned can keep that direct sentence and stop. A history or comparison that must tell a second `MaintenanceInspectionAssignment` episode from the first, even with the same `Robot-7` and `InspectorSystemRole`, needs the occurrence-identity branch. A dependent direct relation may likewise require one already distinguished occurrence as its participant.

**First useful move.** Write the direct relation with its named participants, using the subject pattern's participant meanings and obtaining predicate only as far as needed to state that relation accurately. The subject pattern defines the test; it does not inspect the current case. Relevant world facts or constituting history from that case must satisfy the test, and a claim-bearing episteme may state the result without making it true. Then ask: **Will later work need to tell this occurrence from another occurrence of the same relation, including another episode with the same participants?** If no, keep the readable direct sentence and stop. If yes, recover and apply the subject pattern's same-versus-new-occurrence rule. Only after that rule distinguishes the occurrence should you name or reference it and map the exact receiving assertion, description, direct relation, or declared operation application.

**What goes wrong if missed.** An epistemic, designation, or representation-side object is treated as what creates the relation it is meant to describe or designate. Repeated assignments with the same participants then collapse into one. At the opposite extreme, every ordinary relational sentence is expanded into a relation-occurrence description episteme even though later work does not need to distinguish occurrences.

**What this buys.** Engineers can report a current relation in ordinary prose without opening unused apparatus. When history, comparison, evaluation, or another direct relation must distinguish repeated occurrences, a system can apply the domain identity rule while assertions, descriptions, designations, representations, and publication occurrences retain their own identities.

**Not this pattern when.** If the wording does not yet identify the direct relation and participants, start with `A.6.P` or `A.6.RSIR`. If no exact ClaimGraph yet defines the participant meanings, applicability, and obtaining predicate, recover that content rather than inventing a case test here. If the current case lacks relevant world facts or constituting history, keep its claim under `C.2.1` and the exact direct predicate; a denial, forecast, scenario, counterfactual, permission, or other claim-side fact invents no obtaining occurrence. An explicit reliance judgment may record supported, refuted, or unresolved reliance under `A.10` or the current evaluation, but neither evidence nor reliance makes the relation obtain. When current case facts satisfy the direct predicate, A.6.REL remains available only if later work must tell this occurrence from another occurrence of the same relation. If the question concerns only the SlotSpecs of a reusable relation declaration, apply `A.6.5`. If later work only reports the current relation, keep the direct sentence and stop.

### A.6.REL:2 - Problem

When a later engineering use needs one obtaining relation occurrence to remain distinguishable from another, descriptions often state five different claim contents as if one assertion or identifier established them all. The claims have this dependency order; the order does not turn them into five project-time decisions:

1. the direct relation obtains for the named participants, those participants jointly satisfy its semantic predicate, one occurrence therefore exists, and the direct identity rule governs its reidentification and distinction from another occurrence;
2. FPF ontology settlement already admits occurrences of that relation kind under `U.Relation`; the direct pattern states the relation-specific participant meanings, obtaining condition, and occurrence-identity rule, while a compatible `RelationSignature` episteme declares corresponding SlotSpecs for reusable descriptions;
3. a system performing explicit-individuation work applies the admitted identity rule so the named receiving use can recoverably distinguish one occurrence; a separate relation-occurrence description episteme is produced only when the selected receiver needs that description;
4. an identifier designates that already recoverable occurrence under a reference scheme;
5. the selected receiving object is either an episteme whose content designates that occurrence, another direct relation that has the occurrence as a participant, or an assertion episteme whose content states that one exact A.6.1 operation application binds the occurrence as its actual argument value under one named `ArgumentDeclaration`.

The later claim contents do not make the earlier relation obtain. Root `U.Relation` admission is a corpus ontology decision governed by `E.24.UK`. `A.6.REL` supplies the common occurrence discipline, while each direct relation pattern supplies the relation-specific participant meanings, obtaining condition, and occurrence-identity rule used as the admission witness. Project work does not repeat that classification decision. A system performing explicit-individuation work applies the direct identity rule so one existing occurrence is recoverably distinguishable for the current use; that work neither creates the occurrence nor by itself requires a separate description episteme. A system performing naming work may subsequently associate a designator with the occurrence, and a receiving episteme may subsequently contain a reference that designates it.

Relation-heavy work often begins from a table row, graph edge, identifier, or reified statement. An engineer can then mistake the represented row, edge, identifier, or reifier identity for world-side relation identity. Applying this method permits exact use of relation-occurrence identity without reversing representation and ontology and without forcing a relation-occurrence description episteme into every readable sentence.

### A.6.REL:3 - Forces

| Force | Tension |
|---|---|
| Readable assertion vs explicit identity | Engineers need short relation sentences, while some later assertion or description epistemes need one stable occurrence as their EntityOfConcern or designated object and receiving direct relations may need it as a participant. |
| Relation obtaining vs predicate satisfaction | The world-side relation obtains; the actual relation participants, considered under their participant meanings, satisfy the truth-valued condition stated by the semantic predicate. Conflating these substitutes a formal expression for the obtaining relation. |
| Relation kind vs semantic predicate | A relation kind classifies occurrences under an identity rule; a predicate states a satisfaction condition for the jointly considered participants. One is not a synonym for the other. |
| Occurrence vs assertion or representation | An occurrence can exist before anyone asserts, describes, explicitly individuates, names, references, or represents it. |
| Participant identity vs repeated occurrences | In one direct species under `U.SystemRoleAssignment`, the same complete participant set can recur after a demonstrated predicate-false gap; another direct relation may use a different discriminator only when its own pattern declares one. |
| Construction vs description | A system can create a relation occurrence while performing constitutive work when the direct construction rule says so; that work occurrence may contribute to identity. Producing a row or description episteme is not constitutive by form. |
| Subject-pattern variation vs universal reification | A.6.REL supplies no universal truth-maker, occurrence-identity discriminator, or representation form. Each direct relation pattern supplies its own obtaining and identity settlement; each concrete representation remains under its direct representation pattern and explicit correspondences. |
| Stable reference vs false creation | Identifiers enable later reference, but identifier assignment neither creates the occurrence nor makes the direct relation obtain. |

### A.6.REL:4 - Solution

Use progressive relation-occurrence individuation. Start from a readable obtaining direct relation, ask whether later work must distinguish a repeated occurrence, and stop before technical receiving branches when the answer is no.

**Local relation-occurrence mantra.** *State the direct relation, using its governing predicate enough to say it accurately. Ask whether later work must tell this occurrence from another occurrence of the same relation, including another episode with the same participants. If no, keep the readable sentence and stop. If yes, recover and apply the direct same-versus-new-occurrence rule. Only then name or reference the occurrence and map the exact receiving assertion, description, direct relation, or declared operation application.*

This short formula keeps the progressive-individuation Solution in attention; it does not replace sections 4.1-4.7. It is a mnemonic, not a work plan or performed work. When a receiving use instead needs one reusable constraint-governed unfolding structure for those continuations and stops, `A.22.CGUS` governs that structure.

#### A.6.REL:4.1 - Apply the relation-object architecture discipline

**Relation-object architecture discipline** is the rule set in this subsection. It is not another U-kind. Conforming prose keeps the objects around one direct relation distinct, names the direct relation between adjacent objects, and uses a recoverable name for each current object. `A.6.5` specializes only the `SlotSpec` part of this rule set.

**Short use rule.** State the world-side relation and its actual participants first. Add another named object from the relation-object architecture only when the current receiving use depends on that exact object, and state its direct relation to the object already in view. The tables below help select that additional object and relation; they are not a mandatory form for ordinary relation prose.

The world-side relation comes first. An **actual relation participant** is one exact `U.Entity` participating in one obtaining relation occurrence under one relation-participant meaning. Participation leaves the entity under its independently governed intrinsic kind. A **relation occurrence** is the obtaining `U.Relation` occurrence itself. The direct relation obtains when the actual participants satisfy the obtaining predicate; the occurrence-identity rule provides the criteria for reidentification, continuity, and distinction from another occurrence. Signatures, assertions, names, references, and representations retain their separate identities.

##### A.6.REL:4.1.1 - World-side objects

| Canonical FPF name | What this object is | Direct relation to preserve | Naming rule | Subject pattern |
|---|---|---|---|---|
| **actual relation participant** | one exact `U.Entity`; this is a relation-qualified use of the entity, not a new kind | the entity participates in this relation occurrence under one relation-participant meaning | use the entity's direct kind and current name; use a governed designator only when naming or reference is current; in relation prose add the domain participant meaning, as in `Robot-7 as the holder system` | the participant's direct pattern and the direct relation pattern |
| **relation occurrence** | one obtaining occurrence admitted under `U.Relation` | the occurrence has the actual participants and is classified by the direct relation kind; it obtains when those participants satisfy the relation obtaining predicate within its applicability | use the readable direct relation sentence until stable occurrence reference is needed; then use a relation-occurrence designator assigned after the identity rule is applicable | the direct relation pattern and `A.6.REL` |

The phrase **actual relation participant** therefore never replaces the entity's own name. It says how that entity participates in this occurrence. Likewise, the readable sentence `Robot-7 is assigned as inspector through InspectionAssignment-17` can state the direct assignment without first creating a relation-occurrence description episteme.

##### A.6.REL:4.1.2 - Relation-kind settlement

The relation kind is a classificatory distinction over relation occurrences. Every admitted direct or derived relation kind has one direct subject settlement that states relation-participant meanings, an obtaining predicate, applicability, and an occurrence-identity rule as semantic and rule content. A derived kind additionally names its base-definition and substrate dependencies. Ordinary use may omit explicit individuation when no receiver needs it; that omission does not mean the identity rule is absent. World-side entities participate according to the settlement while retaining their own kinds.

| Canonical FPF name | What this object is | Direct relation to preserve | Naming rule | Subject pattern |
|---|---|---|---|---|
| **relation kind** | a classificatory distinction whose individuals are relation occurrences; `E.24.UK` admits a durable U-kind only when the direct relation pattern supplies the required witness, while a narrower relation distinction remains governed without automatic `U.*` admission | classifies relation occurrences governed by one obtaining predicate and one occurrence-identity rule | use the accepted domain relation name; a new durable Tech name follows `E.24.UK` admission and `F.18` naming, while morphology alone establishes neither | the direct relation pattern and `A.6.REL`; `E.24.UK` when durable U-kind admission is current |
| **relation-participant meaning** | relation-local semantic content specifying one domain contribution to the obtaining predicate | says how one actual participant contributes to the obtaining predicate while that participant retains its intrinsic kind | use the domain meaning declared by the direct pattern, such as `holder System` or `assigned local system-role kind` in an A.2.1 direct species; keep it local to that relation kind | the direct relation pattern |
| **relation obtaining predicate** | truth-valued rule content over the actual participants considered under their relation-participant meanings | satisfaction of this predicate is the stated criterion for the direct relation obtaining | use the exact condition from the subject pattern, such as the predicate of one directly declared species under `U.SystemRoleAssignment`; notation used to express it keeps its source name under `C.29` | the direct relation pattern |
| **relation occurrence-identity rule** | rule content for reidentifying one occurrence and distinguishing it from another | a system applies this rule only after relevant current-case facts or constituting history satisfy the direct obtaining predicate and later work needs occurrence identity | name the exact world-side discriminator supplied by the direct relation pattern, such as participant-determined identity or maximal continuous obtaining interval | the direct relation pattern and `A.6.REL` |

**Public name settlement.** The following F.18 NameCard names the already governed root occurrence kind. It neither admits a new kind nor makes a relation obtain.

```text
NameCard:
  NameCardId: NC-U-RELATION
  GovernedValueRef: U.Relation under A.6.REL
  SubjectPatternLocator: A.6.REL
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: individuable obtaining relation occurrence whose direct pattern supplies participants, obtaining conditions, and identity
  TechLabel: U.Relation
  PlainLabel: relation occurrence
  CandidateSet: U.Relation; U.RelationOccurrence; U.ObtainingRelation; U.IndividuatedRelation
  RejectedCandidates: longer candidates expose occurrence or obtaining but lose the established root retrieval head; U.Relation remains safe only with the A.6.REL identity discipline
  SelectionRationale: preserve the root name while distinguishing existence, kind admission, explicit individuation, identifier assignment, and reference use
  PublicRowStatus: pending
  LineageEntries: existing local U.Relation declarations narrowed to individuable obtaining occurrences
  RefreshCondition: reopen if direct relation patterns cannot supply stable occurrence identity for an admitted relation kind
```

Use `U.Relation` for the admitted root kind only. A direct relation kind keeps its own governed name, participant meanings, obtaining predicate, and occurrence-identity rule.

In the world-side relation, the actual entities participate directly under the relation-participant meanings. When assertions and descriptions need typed reuse, a reusable declaration episteme declares those meanings without becoming the world-side relation.

##### A.6.REL:4.1.3 - Reusable declaration episteme

| Canonical FPF name | What this object is | Direct relation to preserve | Naming rule | Subject pattern |
|---|---|---|---|---|
| **`RelationSignature`** | a `U.Signature` declaration episteme whose EntityOfConcern is the direct relation kind | its content states a reusable declaration of the relation-participant meanings, obtaining predicate, applicability, occurrence-identity rule, and only the SlotSpecs needed by receiving typed uses | name the declaration episteme from its accepted direct relation species, for example the `RelationSignature` for `MaintenanceInspectionAssignment`; the name denotes the declaration episteme, not the relation kind or an occurrence | `A.6.0` |
| **`SlotSpec`** | a declaration-content component identified inside one exact `RelationSignature` by its declaration-local `SlotKind` | corresponds to one relation-participant meaning and states the actual participant `ValueKind` plus the receiving-episteme designation mode | use the exact declaration-local name supplied by the subject pattern, such as `HolderSystemSlot` in the `MaintenanceInspectionAssignment` signature; refer to the complete component as that SlotSpec in the named `RelationSignature` | `A.6.5` |

`SlotKind`, `ValueKind`, and `refMode` answer different questions. `SlotKind` identifies the declaration component locally. `ValueKind` is the independently governed kind of the actual relation participant. `refMode` states how a receiving episteme designates that participant. Together they specify one declaration component; world-side entities and occurrences keep their independently governed identities.

##### A.6.REL:4.1.4 - Claim and description epistemes

| Canonical FPF name | What this object is | Direct relation to preserve | Naming rule | Subject pattern |
|---|---|---|---|---|
| **relation-participant designation** | a value or governed reference in a receiving episteme; it retains its own value kind or RefKind | denotes the actual relation participant through the content position corresponding to one declared SlotSpec | name the value or reference under its own governor and effective reference scheme; if a concrete representation field carries it, keep that field's source name and state the explicit declaration or C.29 correspondence to the SlotKind; equal spelling is only a representation choice, never object identity | `C.2.1`, `A.6.5`, and `F.18` when durable naming is current |
| **relational assertion** | a claim-bearing `U.Episteme` | its content states affirmative or negative assertion polarity for the direct obtaining predicate with relation-participant designations; an affirmative assertion may designate an already individuated occurrence only after current case facts or constituting history satisfy that predicate and the direct identity rule has been applied; the assertion states that result but does not establish or constitute it; a forecast, scenario, counterfactual, permission, or other claim family keeps its own direct semantics, while supported, refuted, or unresolved reliance belongs to `A.10` or the receiving evaluation | name the asserted direct relation and its polarity; name the exact direct claim family whenever ordinary affirmation or denial is insufficient | `C.2.1`, the direct claim pattern, and `A.10` or the receiving evaluation for reliance |
| **relation-occurrence description episteme** | a `U.Episteme` whose EntityOfConcern is one explicitly individuated relation occurrence | describes that occurrence without replacing it or supplying its identity | use `description of <relation-occurrence designator>` in readable prose; give a reusable description-episteme kind its own governed name only when another use depends on that kind | `C.2.1` |

A receiving episteme contains a relation-participant designation in a content position corresponding to one declared SlotSpec. A concrete representation may carry that designation in a field, but the field keeps its source name and corresponds to the declaration-local SlotKind only through an explicit declaration or C.29 correspondence. Reusing the SlotKind spelling for convenience does not identify the field, SlotKind, designation, or participant. The designation denotes the actual participant; the participant remains a `U.Entity`, the obtaining occurrence remains a `U.Relation`, and the receiving episteme keeps its own C.2.1 identity.

##### A.6.REL:4.1.5 - Naming, reference, and representation

| Canonical FPF name | What this object is | Direct relation to preserve | Naming rule | Subject pattern |
|---|---|---|---|---|
| **relation-occurrence designator** | a name associated with one already recoverable relation occurrence under a naming relation and effective reference scheme | designates the occurrence; assignment of the designator does not create or individuate it | apply `F.18`; select a name that exposes enough of the direct relation and identity distinction for its receiving use | `F.18` |
| **relation-occurrence reference** | a reference value of one exact RefKind under an effective `U.ReferenceScheme` | a system applying the governed resolution method obtains the already recoverable relation occurrence as referent | use the exact governed RefKind whose declared referent range admits this relation kind; a field ending in `Ref` names the reference value, not the occurrence | `F.18` and the direct RefKind pattern |
| **representation element** | an element of a declared representation under `C.29` | represents an object, claim content, or declaration, or corresponds to one independently governed object in this relation-object architecture | keep the source representation's own name and state an explicit correspondence naming both the source element and the FPF object; do not rename the source element into that object | `C.29` and the applicable representation-transition pattern |

A source-specific term remains the name of its source-side object until an explicit correspondence is stated. That correspondence never identifies a source representation element with the represented FPF object. Representation preservation stays with `C.29` and the selected representation-transition pattern, structural equivalence goes to `C.34`, and cross-context sameness goes to `A.6.9`.

##### A.6.REL:4.1.6 - Use the subject pattern for the current object

| Current question | Subject pattern |
|---|---|
| What relation obtains, under which participant meanings, predicate, and identity rule? | the direct relation pattern, with `A.6.REL` for occurrence individuation |
| What reusable declaration and SlotSpecs are needed? | `A.6.0` and `A.6.5` |
| What assertion or description episteme is current? | `C.2.1` and the direct claim or description pattern |
| What durable designator or reference is current? | `F.18` and the direct reference pattern |
| What selected representation element is current, and what object or claim content does it represent? | `C.29` and the selected representation-transition pattern |
| Which object is hidden by unresolved source wording? | `A.6.P`, `A.6.RSIR`, and `E.10`, followed by the subject pattern recovered there |

Only systems perform authoring, evaluation, individuation, naming, reference-resolution, and representation work. Relation occurrences obtain; epistemes contain declarations, assertions, and descriptions; names and references stand in governed designation relations. This grammar keeps agency with systems without suppressing the semantic relations that make the relation-object architecture useful.

##### A.6.REL:4.1.7 - Name only the minimum current object

The relation-object architecture organizes the distinct objects that may become current; it is not a publication form repeated for every relation sentence. Stable relation-kind semantics belong once in the direct relation pattern or ontic. A reusable declaration belongs once in its `RelationSignature`. A durable name belongs once in its F.18 naming settlement. Later prose names the object current for its use and cites the subject pattern for already established neighboring objects.

| Current use | Minimum sufficient text | Add another object only when |
|---|---|---|
| ordinary direct relation assertion | one readable direct relation sentence naming the actual participants | predicate interpretation or occurrence identity changes the next engineering move |
| repeated typed assertion or description episteme | cite the direct `RelationSignature`; carry exact relation-participant designations in content positions corresponding to its SlotSpecs; if a concrete representation field carries one, keep its source name and state the explicit declaration or C.29 correspondence | the declaration, ValueKind, RefKind, designation, or correspondence itself is under examination |
| occurrence-dependent assertion or description episteme | use the relation-occurrence designator or reference and cite the direct occurrence-identity rule | participant meaning, obtaining, continuity, or repeated-occurrence identity is disputed |
| representation-dependent use | name the source representation element, the represented FPF object or claim content, and their explicit correspondence | representation preservation or loss is current under `C.29`, structural equivalence is current under `C.34`, or cross-context sameness is current under `A.6.9` |
| ontology or wording repair | traverse the complete relation-object architecture in this subsection | the repair has not yet recovered a unique current object and subject pattern |

In recognition text, prefer the readable direct relation sentence. Put the reusable declaration, occurrence-identity rule, naming settlement, or representation correspondence in nearby Tech or assurance text governed by its direct pattern, and refer to it when another declared use depends on it. Precision comes from recoverable subject patterns and explicit relations between adjacent objects, not from repeating the complete architecture.

This rule keeps elaboration additive. Each new receiving use introduces only the object on which that use depends and the object's direct relation to an already recoverable object. When the use stops at the world-side relation, the prose adds no signature, occurrence-description, naming, or representation apparatus.

#### A.6.REL:4.2 - Apply the receiving-use test

Here **receiving use** is a Plain head, not a common FPF kind. Do not decode it into the architecture before the cheap decision. First state the readable relation and ask what later work must distinguish. Only after that work needs occurrence identity, resolve it to the exact receiving object: an assertion or description episteme under `C.2.1`, a direct relation that has the occurrence as a world-side participant, or an assertion episteme that states one exact A.6.1 application binds the occurrence as its actual argument value under a named `ArgumentDeclaration`. Any acting system, enacted method, and performed work remain separately governed.

1. Name the direct relation kind and participants in a readable sentence. Use only the direct relation-participant meanings, obtaining predicate, and applicability needed to state that sentence accurately; do not yet require a `RelationSignature`, SlotSpecs, occurrence designator, representation correspondence, or the complete occurrence-identity rule.
2. Immediately ask: **Will later work need to tell this occurrence from another occurrence of the same relation, including another episode with the same participants?**
3. Apply the observable contrast. A current report that only says `Robot-7 is assigned as inspector through InspectionAssignment-17` answers no. A history or comparison that must distinguish a second occurrence of the same direct species from the first, despite the same participant values, answers yes.
4. If no, keep the readable direct sentence and stop this pattern. Do not create a relation-occurrence description episteme for completeness.
5. If yes, recover the participant meanings, applicability, and obtaining predicate from the subject pattern. Inspect the relevant world facts or constituting history in the current case and judge whether they satisfy that test. Only when the case facts satisfy the predicate is there an obtaining occurrence to individuate; otherwise use the exact direct claim predicate and keep its subject pattern only as a locator or `A.6.P`. A claim-bearing episteme may state an affirmative or negative result, but its polarity, a forecast, scenario, counterfactual, permission, another separately governed claim, evidence, and supported, refuted, or unresolved reliance neither establish nor constitute that occurrence.
6. Recover and apply the subject pattern's same-versus-new-occurrence rule. Explicitly individuate one occurrence; assign an identifier only when stable reference is needed.
7. Only now name the exact receiving object and subject pattern. Designate the occurrence in a receiving assertion or description episteme; for a receiving direct relation, verify its obtaining with that occurrence as a participant; or, for an already identified operation application, verify the named A.6.1 `ArgumentDeclaration`, designation rule, ValueKind, cardinality, and binding predicate before an assertion episteme states that the occurrence is its actual bound argument value.

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
| The relation kind uses another domain identity rule | the exact discriminator supplied by its subject pattern |

When a relation occurrence is a constructed result under its direct construction rule, recover the constructing `U.System` and the performed construction Work. Use F.6 to identify the assignment under which each constructing System acted; a short occurrence-identity explanation may omit an assignment identifier that no later claim uses. Also recover the enacted constructor Method, input entities, and the identity contribution of that Work occurrence. An installed-part relation is only a hypothetical candidate here: installation Work may distinguish its occurrences only after an accepted pattern for that relation declares the participant meanings, obtaining predicate, applicability, and constitutive identity contribution. Until then, do not infer an installed-part occurrence from the Work, row, drawing, assertion, designation, or representation.

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

Ordinary users write one readable direct relation sentence with named participants and immediately ask whether later analysis or reporting must distinguish this occurrence from another occurrence of the same relation. A report that only states the current `Robot-7` assignment to `InspectorSystemRole` through `InspectionAssignment-17` stops there. A history or comparison that must distinguish a later occurrence of the same species opens its direct occurrence-identity rule. Only after that rule distinguishes the occurrence does the user add the exact receiving assertion, description, direct-relation participant, operation argument, identifier, or reference branch. The direct relation pattern states the shared participant meanings, obtaining predicate, applicability, and identity rule once; later uses cite only what their branch consumes.

This is demand-driven progressive elaboration within the Solution, not a drafting sequence. The alternatives below share one readable direct relation. Indentation marks only a real dependency: the receiving occurrence branch follows a positive distinguishability decision and the direct identity rule, while the `RelationSignature` branch remains independent and opens only for typed reuse.

```text
readable direct relation sentence with named participants
  +-- later work only reports the current relation -> stop
  +-- later work must distinguish another occurrence, even with the same participants
      +-- check direct obtaining and apply the direct same-versus-new-occurrence rule
      +-- then add only the receiving branch that consumes the distinguished occurrence
          +-- description or assertion designation
          +-- identifier or stable reference
          +-- occurrence as another direct relation's participant
          +-- occurrence as a declared operation argument
  +-- RelationSignature and SlotSpecs independently, only when typed reuse matters
```

This is a C.29 representation of the stop decision and optional increases in explicitness. Its branch marks are representation elements, not direct relations or work occurrences. The indentation below the same-versus-new-occurrence rule records only that description, identifier assignment, occurrence participation, and later designation require one recoverable occurrence; it does not make a `RelationSignature` prerequisite for occurrence identity. The represented branches are neither a documentation plan nor a method for constructing the world-side relation.

#### A.6.REL:4.7 - Keep world-side change separate from episteme editions

Whenever current wording or work says that a relation occurrence, claim, reusable declaration, name, reference, description, or publication "changed," first name which exact object changed and apply that object's own continuity, identity, revision, or edition rule. This selection does not require an A.10 evidence relation:

| Changed object | Exact move |
|---|---|
| direct relation occurrence | apply the direct identity rule to the current case facts or constituting history and determine continuation, cessation, split, or another occurrence; for a temporally extended occurrence, use only the temporal boundary declared by that rule |
| relational assertion | revise, retract, replace, or supersede the assertion episteme under `C.2.1` |
| `RelationSignature` | revise the reusable declaration and establish its edition relation under `A.6.0` |
| identifier assignment | assign, retire, or replace the designator under `F.18` |
| reference use in an episteme | reinterpret or retarget the designation under `F.18` and the receiving SlotSpec |
| description episteme | revise the episteme or establish another edition under `C.2.1` |
| publication occurrence | end the current publication occurrence or establish another under `E.17` and `E.24.PUB` |

A relation occurrence has identity under its direct rule; a temporally extended occurrence also has temporal history under that rule. Revision work may change an episteme or establish another edition, but it changes no world-side occurrence. Current case facts or constituting history must separately satisfy the direct continuation, cessation, or same-versus-new-occurrence rule. Another edition of an assertion, signature, or description episteme, or another publication occurrence, therefore entails no new relation occurrence.

Use `A.10` only when current receiving work separately asks whether to rely on a claim in light of evidence. That reliance judgment neither triggers changed-object selection nor supplies or causes the world-side change.

### A.6.REL:5 - Archetypal Grounding

#### A.6.REL:5.1 - Repeated occurrence of one direct system-role-assignment species

Start with `Robot-7 is assigned as inspector through InspectionAssignment-17` and trace only the objects needed by the current use.

1. **World-side participants and occurrence.** `Robot-7` remains an admitted `U.System`; `InspectorSystemRole` remains one exact local C.3 kind. `InspectionAssignment-17` is an occurrence of directly declared `MaintenanceInspectionAssignment <: U.SystemRoleAssignment`, with `Robot-7` filling `HolderSystemSlot` and `InspectorSystemRole` filling its declaration-local assigned-kind slot. This simple species has no generic taxonomy, reference-scheme, context, or interval participant.
2. **Direct settlement.** A.2.1 supplies the species' participant meanings, direct predicate, applicability, and same-versus-new-occurrence rule. The occurrence continues while that predicate obtains without interruption for the same complete participant set. A demonstrated predicate-false gap ends it; later resumption starts another occurrence. An evidence gap by itself does neither.
3. **Reusable declaration.** For typed reuse, the `MaintenanceInspectionAssignment` `RelationSignature` contains `HolderSystemSlot : U.System / U.EntityRef` and one declaration-local assigned-kind SlotSpec whose ValueKind is the exact `InspectorSystemRole` domain. A stronger direct species adds only its real identity-bearing participants. `assignmentInterval` remains assertion or occurrence-description content, not another participant SlotSpec.
4. **Assertion and participant designations.** An `InspectionAssignmentAssertion` carries designations corresponding to the species' declared SlotSpecs and states the currently known `assignmentInterval` separately. Its claim may say that `Robot-7` is currently assigned as inspector through `InspectionAssignment-17`. If later use only needs that current report, keep the assertion and stop without adding another occurrence object.
5. **Occurrence identity, designator, and reference.** Suppose two episodes of the same direct species have the same complete participant values but occur in inspection shifts separated by a demonstrated predicate-false period. A history or Work-attribution claim applies the A.2.1 continuity rule, distinguishes the second occurrence, and may designate it. A roster-row identifier, copied field set, taxonomy edition, reference scheme, or reused source key cannot collapse or split the two episodes.
6. **Representation.** A roster row or diagram edge may represent the assignment assertion or an occurrence-description episteme under `C.29`. Its source fields and key keep their representation-side meanings. An explicit declaration or C.29 correspondence relates a source field to the exact SlotKind and the carried value or reference to the participant designation; using the same spelling for field and SlotKind is optional and establishes no identity. Representation identity does not replace the A.2.1 occurrence rule.

The practical payoff is visible at each stop. A current staffing report keeps the readable direct sentence. Typed reuse opens the existing declaration. A history or work-attribution claim opens occurrence identity only when it must distinguish the repeated episode. Stable cross-reference use may then motivate naming and reference work.

#### A.6.REL:5.2 - Hypothetical installed-part boundary

`Bearing_B isPartOf Pump_P` may be a readable source claim, but current A.14 does not supply an `InstalledPart` relation kind, installed-part participant meanings, an installed-part obtaining predicate, or its same-versus-new-occurrence rule. Names such as `InstalledPartRelationSignature`, `InstalledPartSlot`, and `AssemblyWholeSlot` are therefore hypothetical candidates, not current declarations. Do not use them to claim conformance or an individuated installed-part occurrence.

A future accepted subject pattern could make installation work or a continuous installation interval identity-bearing, but A.6.REL does not choose that ontology. Until such a subject pattern exists, keep the physical entities, installation work, proposed part relation, assertion, occurrence description, designator, reference, and database or drawing representation separate, and stop before an occurrence-identity result.

#### A.6.REL:5.3 - Formal reduced case

The expression `3 < 5` is assertion content written in a mathematical notation. Under the referenced arithmetic structure, the values three and five satisfy the less-than predicate. The expression is not thereby a relation occurrence. No receiving use in this case needs the obtaining less-than relation occurrence explicitly individuated under `U.Relation`, so the engineer stops at the assertion. A graph edge or RDF reifier introduced by tooling remains a representation of the proposition or assertion and is not an occurrence-identity rule in the formal subject domain.

#### A.6.REL:5.4 - Relation occurrence as a participant

`C.22.PFR` has one actual-condition relation occurrence and one problem-criterion-applicability relation occurrence as world-side participants. Each is individuated under its own direct identity rule. The PFR direct pattern states those two participant meanings, its obtaining condition, and its identity rule; the PFR `RelationSignature` episteme declares the corresponding SlotSpecs. A PFR assertion designates the two occurrences according to those SlotSpecs. PFR is a direct relation, not an episteme whose content merely groups two assertions.

#### A.6.REL:5.5 - Description and publication recursion through the relation-object architecture

Let `R1` be the already individuated second `MaintenanceInspectionAssignment` occurrence from 5.1.

1. An assignment-occurrence description episteme `E1` has `R1` as its exact EntityOfConcern. In the reusable C.2.1 `EpistemeConstitutionRelationSignature`, the declaration-local SlotKind `EntityOfConcernSlot` names the entity-of-concern participant meaning. In a card representation of `E1`, the source field `entityOfConcernRef` corresponds to that SlotKind only through a declared C.29 correspondence; its `U.EntityRef` value is the participant designation that resolves to `R1`. Neither spelling nor containment identifies the field, SlotKind, designation, or occurrence.
2. A second episteme `E2` contains the result of evaluation work concerning the adequacy of `E1`. Its exact EntityOfConcern is `E1`, not `R1`. A field in a reusable card or other C.29 representation may carry a `U.EntityRef` designating `E1`; it corresponds to `EntityOfConcernSlot` only through a declared representation correspondence. The two epistemes therefore have different EntitiesOfConcern and retain separate C.2.1 identities: `E1` describes `R1`, while `E2` evaluates the adequacy of `E1`.
3. Under a publication-relation occurrence, the current edition of `E1` is available to a declared audience and use. The selected episteme edition is an actual participant of that publication relation under the publication pattern's participant meaning. The publication form and its representation elements retain their own kinds and correspond to the published episteme only through the declared publication and representation relations.

A system performing revision work can establish another edition of `E1` or `E2`; a system performing publication work can establish another publication-relation occurrence for a selected edition. `R1` continues or ceases only as the A.2.1 obtaining predicate and occurrence-identity rule determine from the assignment facts. This recursive case preserves the distinction: a description episteme can itself become the actual participant or EntityOfConcern of another relation without becoming the relation occurrence it describes.

### A.6.REL:6 - Bias-Annotation

This pattern has an individuation bias because it serves receiving uses that need relation identity. The lightweight stop rule prevents that bias from turning every direct relation into an explicit relation-occurrence description episteme.

The admitted system-role-assignment case can over-emphasize participant identities and temporal continuity. Another direct relation may instead use constituting Work or another world-side discriminator, but only when its own accepted pattern states that contribution. The hypothetical installed-part boundary demonstrates why A.6.REL must not invent that rule.

Engineers can easily picture relation instances through data-model examples. The prescribed move therefore begins with direct relation obtaining, predicate satisfaction, and the direct identity rule. A system introduces database rows, graph edges, reifiers, tuples, and data-model objects only afterwards as representations for a declared use.

### A.6.REL:7 - Conformance Checklist

1. Across the subject pattern and the current use, the relation kind, relation-participant meanings, relation obtaining predicate, actual relation participants, applicability, relation occurrence-identity rule, and any currently needed `RelationSignature` SlotSpecs are recoverable. An ordinary relation sentence remains complete without repeating that settlement.
2. The text does not conflate relation obtaining, predicate satisfaction, root-kind admission, explicit-individuation work, identifier assignment, and reference use.
3. Root `U.Relation` admission is governed by `E.24.UK` from the common `A.6.REL` discipline and the relation-specific witness supplied by each direct relation pattern; project use does not repeat the admission decision.
4. Immediately after the readable direct relation, the current work answers whether it must tell this occurrence from another occurrence of the same relation. A current-status report is the explicit no branch; a history or comparison that distinguishes repeated episodes with the same participants is the explicit yes branch.
5. The subject pattern defines the obtaining test; relevant current-case facts or constituting history supply its factual basis; a claim-bearing episteme states polarity. An affirmative assertion, evidence, or a supported, refuted, or unresolved reliance result neither establishes nor constitutes the world-side occurrence.
6. Every admitted direct or derived relation kind has a direct governing settlement that declares its occurrence-identity rule; ordinary omission of explicit individuation or an occurrence designator does not count as absence of that rule.
7. Participant-determined identity is used only when the direct ontology establishes that the same participant identities cannot recur in distinct occurrences of that relation kind.
8. When the same participants can recur, the direct pattern declares the domain discriminator; maximal continuous obtaining interval and constituting work are possible choices only when that pattern includes them in the occurrence-identity rule.
9. When construction is constitutive, the constructing system, input entities, performed construction work, and identity contribution are named; representation creation is not substituted for construction.
10. Each object in the relation-object architecture is reidentified under its subject pattern and connected to adjacent objects only by the direct relations stated in section 4.1.
11. A relation occurrence used as another relation's world-side participant is individuated first; the receiving assertion's reference remains distinct from that participant.
12. Ordinary use stops at the readable direct relation when later work only reports the current relation. When later work must distinguish repetition, the direct same-versus-new-occurrence rule is applied without first creating a `RelationSignature`; only then is the occurrence named, referenced, or mapped into its exact receiving branch.
13. Another episteme edition, publication occurrence, name association, or reference use is not evidence of another world-side relation occurrence; apply the direct occurrence-identity rule independently.

### A.6.REL:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
|---|---|---|
| Representation-first relation | A table row, edge, or object identifier is treated as what makes the relation obtain. | State the direct relation, participants, and obtaining condition first; treat the row as a representation unless the direct ontology demonstrates that the corresponding representation-producing work is constitutive. |
| Predicate-as-relation | A semantic predicate or its expression is treated as the world-side occurrence. | State the direct relation and its actual participants; use the predicate only to state the truth-valued obtaining condition. |
| Designation treated as occurrence creation | A relation is said to exist only because another assertion designates it. | Recover the test from the subject pattern and determine whether current-case facts or constituting history satisfy it; let the assertion state the result and let designation justify only later reference, never occurrence creation. |
| Participant-identity collapse | Two assignments or part-relation episodes with the same participants become one occurrence. | Apply the direct identity rule and recover its domain discriminator; use a maximal continuous obtaining interval or constituting work only when that rule includes it in occurrence identity. |
| Observation-window identity | A new measurement or assessment window is treated as a new relation occurrence. | Keep the observation window with its measurement or assessment assertion; recognize another occurrence only when the direct relation ceases and resumes or the direct identity rule supplies another discriminator. |
| Edition-as-world-change | Another edition of an assertion, signature, or description episteme, or another publication occurrence, is called a new version of the world-side relation. | Name the exact changed object and apply its own identity or edition rule. Apply A.10 only when receiving work separately needs a reliance judgment about a claim and evidence; it is neither the trigger nor the source of world-side change. |
| Relator by analogy | A dependent truth-maker is introduced although the direct relation ontology does not identify its dependence relations and occurrence identity. | Introduce a relator only where the direct material ontology identifies the relator, its dependence relations to the participants, and its occurrence-identity rule. |
| Full occurrence description by default | Simple engineering prose becomes a mandatory signature-and-description exercise. | Ask whether later work must tell this occurrence from another occurrence of the same relation; when it only reports the current relation, keep the readable direct sentence and stop. |

### A.6.REL:9 - Consequences

**Benefits.** One common discipline travels without flattening unlike objects: A.6.REL supplies no universal truth-maker, occurrence-identity discriminator, or representation form; for each direct relation, use the truth and occurrence-identity conditions in its defining pattern, and for the selected representation, use the form in its representation pattern. In a direct species under `U.SystemRoleAssignment`, A.2.1 uses uninterrupted predicate obtaining and a demonstrated false gap to distinguish repeated episodes for history or Work attribution. In the formal reduced case, `3 < 5` remains assertion content and needs no explicitly individuated relation occurrence. In `C.22.PFR`, the actual-condition and criterion-applicability relation occurrences are already individuated under their own direct rules before PFR uses them as participants. Each assertion remains a claim-bearing episteme; none is placed in a list of world-side relation kinds.

**Costs.** A direct relation pattern needs a stated occurrence-identity rule, not only participants, when a receiving assertion, description, direct relation, or declared operation application depends on distinguishing one occurrence from another. A system performing relation-identification work establishes whether participants, temporal extent, constituting work, or another domain discriminator distinguishes repetition. Data schemas that used row identity as ontology may need to expose the domain identity they hid.

**Limits.** `A.6.REL` does not decide whether a particular direct relation obtains, define every relation kind, or prescribe a storage model. It does not supply evidence, comparison, publication, forecast, scenario, counterfactual, permission, or temporal semantics governed by neighboring patterns. It also does not turn assertion polarity, a separately governed claim family, or a reliance posture into an obtaining occurrence.

### A.6.REL:10 - Rationale

Applying this method lets an engineer use exact occurrence identity without equating ontology with documentation. A direct relation can obtain for its participants before an FPF episteme states a sentence about it. The actual relation participants, considered under their participant meanings, satisfy the semantic predicate within the direct relation pattern's declared applicability and temporal conditions; an assertion is an episteme whose content affirms or denies that predicate under its exact direct claim family; `A.10` or the receiving evaluation separately governs supported, refuted, or unresolved reliance; explicit-individuation work is performed by a system for a named receiving use; and an identifier only enables later reference. Keeping those objects and moves distinct prevents semio-bias in which an episteme is mistaken for the world-side relation.

The identity rule belongs to the direct relation pattern because the direct ontology determines whether participant identities suffice. The same complete participant set can stand in two occurrences of one A.2.1 direct species when a demonstrated predicate-false gap separates them. The same component and whole may belong to distinct part-relation episodes only if their accepted subject pattern declares the relevant discriminator; A.6.REL supplies none. Conversely, an ordinary formal order assertion may need no explicit occurrence object in project work. A universal key would be too weak for repetition and too heavy for ordinary use.

Assertion, description, and signature epistemes can have editions; a system performing publication work can establish another publication-relation occurrence for a selected edition. A relation occurrence instead begins, continues, or ceases under its direct rule; when a system applying that rule distinguishes another occurrence, the other occurrence has its own identity. Keeping episteme edition change, publication occurrence, and relation occurrence continuity separate makes repair local and prevents publication history from masquerading as world history.

### A.6.REL:11 - SoTA-Echoing

#### Ontological SoTA and constructional sources

This pattern uses these sources to constrain its account of occurrence existence and identity. They provide ontological comparisons, not notation selection.

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
| [TypeDB 3.x `links` statement](https://typedb.com/docs/typeql-reference/statements/links/) and current relation model | A query can expose a relation variable with named source-language *role players*, while shorthand remains available when the represented relation instance need not be referenced. That source term denotes neither an FPF system-role kind nor a system-role assignment. | **Adapt as a representation stress test; reject as an ontology source.** Sections 4.2, 4.5, and 4.6 preserve a readable direct relation before explicit individuation. TypeDB demonstrates one implementable representation; it does not establish the FPF relation kind, obtaining condition, or identity rule. |
| [RDF 1.2 Concepts](https://www.w3.org/TR/rdf12-concepts/), Candidate Recommendation Snapshot, 7 April 2026 | Distinguishes a proposition expressed by a triple term, assertion of a triple, and reifiers used for further statements. | **Adapt as a representation stress test; reject graph syntax and reifier identity as world-side identity sources.** Sections 4.4 and 5.3 apply that distinction to proposition, assertion, and reifier separation. |

This pattern uses the ontological sources to constrain its occurrence-existence and occurrence-identity method. It uses the representation sources to test implementability only after those choices are made. The worked cases expose both boundaries outside information-system projects.

### A.6.REL:12 - Relations

- `A.6.0` declares RelationSignature participant SlotSpecs and restates the direct predicate, applicability, and exact identity rule for reuse without making the relation obtain.
- `A.6.5` separates world-side participants from RelationSignature SlotKinds and from participant designations in assertions or descriptions.
- `A.6.P` governs restoration of hidden direct relations and participants before occurrence identity is attempted.
- `A.6.RCD` governs the residual case in which exact participants are known but no current direct relation closes the named receiving claim; any admitted derived or primitive relation kind must include its own direct subject settlement and identity rule.
- `A.6.RSIR` governs selection among a direct relation, relation-participant meaning, declaration SlotSpec, `RelationSignature`, and another exact interface object when wording is ambiguous.
- Use `A.2.1` to state direct `U.SystemRoleAssignment` species, predicate obtaining, and occurrence identity, and `F.6` for later attribution to performed Work.
- `A.14` and exact direct mereology patterns define or constrain only the part-relation kinds and part-whole changes they actually declare; A.6.REL adds no installed-part settlement.
- `A.15.1` governs work occurrence identity and readable links to separately governed participation, change, operation-result, production, evaluation, delivery, and acceptance claims.
- `C.2.1` governs assertions and descriptions about relation obtaining, predicate satisfaction, and occurrences; `E.17` and `E.24.PUB` govern publication relations.
- `C.22.PFR` supplies a worked case with two explicitly individuated relation occurrences participating in one dependent evaluative relation.
- `C.29` governs a declared mathematical or data-model lens, including graph, tuple, or database representations used to describe relation structure.
- `E.24` governs ontic settlement and `E.24.UK` governs root `U.Relation` admission. `A.6.REL` supplies the common occurrence discipline, and each direct relation pattern supplies the relation-specific witness. `E.24.CD` supplies the candidate-detection rule only after the prerequisite subject results are recoverable; it does not replace the direct occurrence-identity rule.
- `F.18` governs durable names and identifier use after the relation kind and occurrence identity are settled.

### A.6.REL:End

