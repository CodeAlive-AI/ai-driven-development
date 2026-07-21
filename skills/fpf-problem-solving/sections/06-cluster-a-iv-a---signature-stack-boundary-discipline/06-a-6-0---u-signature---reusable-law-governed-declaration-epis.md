## A.6.0 - U.Signature - Reusable Law-Governed Declaration Episteme
> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Pattern kind.** Ontic declaration pattern.

**Builds on.** A.7 for strict distinction, C.2.1 for episteme identity, C.3 for kinds, A.2.6 for claim scope, and A.6.5 for relation-slot discipline.

**Coordinates with.** A.6.REL for relation occurrences, A.6.1 for mechanisms, C.29 for mathematical-lens use, E.24.UK for durable U-kind admission, and E.24.PUB for publication.

### A.6.0:1 - Problem frame

An engineer has a vocabulary and a set of laws that need to remain stable across several dependent epistemes, such as model epistemes, method descriptions, and patterns. For example, a physical-modeling team needs one stable declaration of connector variables and conservation laws; a clinical team needs one stable declaration of a dose-response relation and its applicability; a formal-methods team needs one stable declaration of terms, inference forms, and invariants.

Use this pattern when the working question is:

> What reusable declaration episteme identifies its subject, states the vocabulary entries and specialized typed declarations available for reuse, states the declared laws, and bounds where those claims apply?

The primary `EntityOfConcern` of this pattern is the `U.Signature` episteme. Its declaration identifies one exact `EntityOfConcern`, whose kind remains governed independently. A relation kind opens the `RelationSignature` specialization; a mechanism family or formal calculus opens the corresponding A.6.1 or FormalSubstrate declaration; a method kind remains governed by A.3.1.

**Primary working reader and concern.** The reader is an engineer who authors or reuses a declaration and needs stable meaning, applicability, and typed reuse without authoring declaration or occurrence-identity apparatus beyond what the current use needs.

For the lightest useful declaration, name that subject through `SubjectKind` and `RangedValueKind`, add `ResultKind` when the result has another kind, and state `Vocabulary`, `Laws`, and `Applicability`. Add `SliceSet` and `ExtentRule` only when a receiving use depends on varying extension. Add A.6.5 SlotSpecs that declare the direct relation's participant meanings only inside a reusable `RelationSignature`; add operation argument and result declarations under A.6.1 when a mechanism declaration needs them. Add dependency declarations only when another signature relies on provided names or laws.

What goes wrong if this pattern is missed: content about later realization, evaluation, and publication accumulates inside the declaration. A later user cannot tell which names and laws are reusable, where they apply, or whether a changed implementation has changed the declaration.

What this buys: one identifiable declaration can be reused while later realizations and uses change under their own governing patterns.

Do not use this pattern merely to state that a direct relation obtains or that one work occurrence produced a result. State that claim directly. Construct a signature only when reusable declaration content is the current object.

### A.6.0:2 - Problem

FPF uses a signature whenever one independently governed `EntityOfConcern` needs reusable vocabulary, laws, and applicability. Current non-exhaustive uses include theory or `A.3.3 U.Dynamics` epistemes, mechanism or `A.19.SelectorMechanism` declarations, method kinds, formal substrates, and direct relation kinds; these examples create neither a shared subject kind nor a closed family of signature profiles. Without one precise ontic:

1. the signature is confused with the entity it describes;
2. a relation declaration is confused with an obtaining relation occurrence;
3. applicability is reduced to an unexplained context label;
4. every declaration is forced into one rigid table-shaped publication form, even when a readable sentence is enough;
5. imported names and exported names remain implicit, so dependent declarations cannot be replayed safely.

The central problem is not missing syntax. It is failure to keep the declaration episteme, its declared subject, the subject's occurrences, and later uses of the declaration as different objects.

### A.6.0:3 - Forces

| Force | Tension |
|---|---|
| Reuse and locality | Reusers need stable names and laws, but those claims are meaningful only under an effective reference scheme and bounded applicability. |
| Light first use and typed reuse | An ordinary receiving use starts from a direct assertion, while repeated use may need relation SlotSpecs under A.6.5, operation declarations under A.6.1, direct relation occurrence-identity rules, and independently governed dependencies. |
| Declaration and realization | Reusers need to assess a realization against declared laws, while the declaration, realizing entity, evaluation work, result episteme, and evidential reliance retain separate identities and direct relations. |
| Stable identity and evolution | Reusers need to know whether the same signature remains current, while a change in a realization alone leaves the signature unchanged. |
| Transdomain form and domain meaning | The same declaration form serves physical engineering, medicine, learning, and formal work while preserving their domain objects. |

### A.6.0:4 - Solution

Use `U.Signature` as the dependent durable U-kind for a reusable law-governed declaration episteme. Identify the episteme through its content, exact `EntityOfConcernRef`, and effective `U.ReferenceScheme`. Let the declaration state its vocabulary, laws, and applicability. Keep the declared subject and every later realization under their direct kinds and relations.

**Local signature mantra.** *Name what the declaration is about. State the vocabulary and laws. Bound where those claims apply. Add specialized typed declarations and dependencies only when reuse needs them. Keep realization and later use with their governing patterns.*

In the mantra, `what the declaration is about` means the exact `EntityOfConcernRef`; `specialized typed declarations` means A.6.5 SlotSpecs that declare a direct relation's participant meanings inside a `RelationSignature`, or A.6.1 operation argument and result declarations for a mechanism; and `dependencies` means actual imports and provided names needed by a dependent signature. The mantra is Plain recall wording. Its imperative grammar does not assert condition-governed continuation. When such executable continuation is current, its object is a Constraint-Governed Unfolding Structure (CGUS) governed by A.22.CGUS.

#### A.6.0:4.1 - Admit and identify U.Signature

`U.Signature` is a same-individual dependent durable U-kind under `U.Episteme`. C.2.1 first identifies one episteme through one `EpistemeConstitutionRelation` by its complete claim content, exact independently governed `EntityOfConcern`, and effective `U.ReferenceScheme`. The claim graph and reference scheme are epistemic constituents; the `EntityOfConcern` is not. A.6.0 adds a stable membership condition and practitioner-facing declaration use to that already identified individual. It adds no second constitution relation, identity discriminator, assembly, composition rule, or holon test.

An already identified episteme is a `U.Signature` exactly when, under its effective `U.ReferenceScheme`, its complete identity-bearing claim content carries a reusable law-governed declaration about its exact `EntityOfConcern` and includes all of the following with substantive meaning:

- direct `SubjectKind` and `RangedValueKind` declarations that identify the declared subject and value range;
- `Vocabulary` that supplies the designators needed to reuse the declaration;
- `Laws` that state the reusable predicates, equations, invariants, closure conditions, or other declared regularities;
- `Applicability` that bounds where those claims are used;
- `ResultKind`, `SliceSet`, `ExtentRule`, and dependency, import, or provided-name declarations only when those distinctions are current for the declaration.

Judge the complete claim content, not a selected subset or the presence of field names. A minimal directly authored signature may carry the declaration content required by the A.6.0 membership predicate in one claim graph without citing any smaller episteme. A signature may instead cite separately identified source or dependency epistemes, provided its own claim graph names the dependency relation and the declaration meaning thereby reused. Those source epistemes remain separate individuals connected through their governing dependency, source-use, edition, or other direct relations; they are not components assembled into the signature, and their citation alone does not establish signature membership.

E.24.UK governs the one-time public admission of the dependent kind. In project work, authoring a new declaration candidate, or revising a declaration so that its claim content, exact `EntityOfConcern`, or effective `U.ReferenceScheme` changes, yields a resulting C.2.1 discriminator triple. When the one `EpistemeConstitutionRelation` for that triple obtains, C.2.1 identifies the resulting episteme; A.6.0 then judges whether that already identified individual satisfies the `U.Signature` membership predicate, without adding a second constitution occurrence or identity discriminator. An optional separately reviewable membership judgment is another classification-assertion episteme whose exact `EntityOfConcern` is the candidate; that assertion neither creates the candidate nor admits the public kind. Citing, comparing, or reusing an unchanged episteme, or judging its membership without changing a C.2.1 discriminator, creates neither another episteme nor another constitution occurrence.

The signature keeps the C.2.1 identity of the same episteme. Two designations resolve to that same individual only while the complete claim content, exact `EntityOfConcern`, and effective `U.ReferenceScheme` are unchanged. Changing any discriminator identifies another `U.Episteme`; call that new individual a `U.Signature` only if it independently satisfies the membership predicate above. State an edition, refinement, or supersession relation only when its own direct predicate obtains.

The declared subject remains the independently governed `EntityOfConcern`, not the signature. A realization of the declaration remains under its direct pattern. A description whose `EntityOfConcern` is the signature is another episteme. Publication occurrence, publication form, `U.PresentationCarrier`, and C.29 representation remain separate objects and relations; publication or visible form establishes neither identity nor membership. G.11 currentness and every later work or use likewise remain neighboring judgments and relations rather than signature identity components.

#### A.6.0:4.2 - Write the minimum declaration content

The four content groups are semantic components, not a mandatory visual table. A publication form may present them as paragraphs, a table, formal declarations, or another representation. A publication occurrence makes a selected episteme edition available through that form without changing its content.

| Content group | Content and use |
|---|---|
| `SubjectKind`, `RangedValueKind`, optional `ResultKind`, `SliceSet`, and `ExtentRule` | Name the declared subject, value range, optional distinct result kind, and any varying extension on which a receiving use depends. No additional container kind is implied. |
| `Vocabulary` | Declares the public designators for value kinds, relation kinds, operators, and other independently identified declared objects. A `RelationSignature` may include SlotSpecs under A.6.5; each SlotSpec gives a declaration-local SlotKind name and the exact participant ValueKind and designation mode. A mechanism may include operation argument and result declarations under A.6.1. A vocabulary token does not by itself admit a durable U-kind. |
| `Laws` | States semantic predicates, equations, invariants, closure conditions, and other declared regularities. A.6.1 governs an operation-admission predicate for a mechanism; A.3.1 governs the method, and A.15.1 governs the dated work occurrence that enacts it, including direct `performedBy` to the exact covering `U.RoleAssignment`. Writing the operation-admission predicate as a condition does not make it a signature law. |
| `Applicability` | States the exact `U.ClaimScope` and any other use qualifiers current for this declaration, such as a relevant time interval or selected `CHR:ReferencePlane`. Cite an optional `modelUseStructureRef : U.StructureRef` only when an independently selected model-use structure changes interpretation. |

`SubjectKind` and `RangedValueKind` are declaration-content components. They do not create a second hierarchy beside C.3 or E.24.UK. A trivial `SliceSet` or constant `ExtentRule` added solely as filler contributes no declaration meaning.

Applicability and meaning remain distinct. The effective `U.ReferenceScheme` is part of episteme identity. The exact `U.ClaimScope` delimits use; when current for the declaration, a relevant time interval, selected `CHR:ReferencePlane`, or selected `BoundedModelUseStructure : U.Structure` further delimits or organizes applicability. None replaces the reference scheme or claim scope.

#### A.6.0:4.3 - Use RelationSignature for reusable relation declaration

`RelationSignature` is the relation-facing use of one `U.Signature`. It is not a second U-kind.

Its `EntityOfConcernRef` identifies one already admitted direct relation kind. For an admitted derived relation kind, the direct governor must already supply its obtaining and occurrence-identity laws. A predicate-definition episteme whose `EntityOfConcern` is the reusable predicate definition rather than that admitted relation kind is not a `RelationSignature`. Its content declares:

- the relation-kind designator;
- one `SlotSpec` for each world-side participant meaning that needs reusable typed declaration;
- the direct pattern's obtaining predicate and declared laws, restated for reuse without claiming that the predicate is satisfied;
- applicability of those claims;
- the occurrence-identity rule supplied by the direct relation pattern, restated for reuse without applying it to any occurrence.

The direct relation pattern remains authoritative for when the relation obtains and how an individuated occurrence keeps identity. The signature declares those rules for reuse; it does not make the predicate true and does not create an occurrence.

A direct relation may obtain before anyone writes a signature. Ordinary prose may therefore stop at:

> Bearing B-17 is installed in pump P-4 at seat S-2.

When many patterns need to reuse `InstalledAtRelationKind`, its three participant meanings, its obtaining predicate, and its occurrence identity, a `RelationSignature` becomes useful: its SlotSpecs declare those three participant meanings for typed assertion and description reuse. When another claim needs to refer to one particular installation occurrence, A.6.REL governs explicit individuation.

#### A.6.0:4.4 - Declare participant meanings and operation parameters under different specializations

For each world-side participant meaning whose reusable declaration is current, a `RelationSignature` declares one A.6.5 SlotSpec. The following code sketch is a compact representation of that declaration, not the world-side relation or its participants:

```text
SlotSpec := <SlotKind, ValueKind, refMode>
refMode := ByValue | RefKind
```

| Component | Meaning in a RelationSignature |
|---|---|
| `SlotKind` | The declaration-local name by which this `RelationSignature` distinguishes one participant meaning of its EntityOfConcern relation kind. It is not a participant, system role, or mathematical operand. |
| `ValueKind` | The exact world-side kind admitted for the relation participant. |
| `refMode` | How a receiving episteme, such as an assertion, description, or occurrence record, carries a participant designation: by value or through one exact governed RefKind. That designation denotes the actual participant. The relation occurrence itself does not store the reference, and the occurrence record is not that occurrence. |

A.6.5 governs these declarations of participant meanings. Use SlotKind names that expose the participant distinction, such as `InstalledItemSlot`, `InstallationSiteSlot`, and `AssemblySlot`. Do not force SlotSpecs into a one-off assertion that has no receiving typed use.

A formal or mechanism declaration may instead need named operation arguments and a result. A.6.1 governs that `OperationAlgebra`; C.29 governs any mathematical operand order, product, function, or tuple used to represent it. Those operation parameters do not become `RelationSignature` SlotSpecs or SlotKinds merely because the same notation uses angle brackets or numbered arguments. When a relation claim consumes a mathematical representation, state an explicit correspondence between the representation's operands and the independently declared SlotSpecs.

#### A.6.0:4.5 - Expose real declaration dependencies

Add a `SignatureManifest` section when this signature uses non-local declared names or when another signature depends on names provided here. The compatible heading is retained for dependent patterns; it names neither another U-kind nor one uniform ontic object. It co-locates entries with three roles: `id` is an identity-neutral display designator; `signatureRef` and its optional `.edition` pin form a governed reference to an already recoverable signature episteme; and `imports` and `provides` may state dependency or name-introduction claims in the signature's exact `U.ClaimGraph` or visibly represent those claims. Co-location makes neither every entry identity-bearing claim content nor any entry a relation occurrence.

The compatible section may carry entries with these roles:

| Entry | Meaning |
|---|---|
| `id : SignatureId` | An identity-neutral display designator or representation metadata for one already independently identified signature episteme. It is not a governed reference and does not enter the C.2.1 identity triple. |
| `signatureRef : U.EpistemeRef` | A governed reference resolving to the already identified signature episteme selected for replay. Changing its serialization preserves the referent only while resolution returns that same episteme under the effective reference scheme. |
| `signatureRef.edition` | An optional edition pin on `signatureRef` for one already recoverable episteme edition. The pin neither enters the C.2.1 identity triple nor establishes that an `EpistemeEditionRelation` obtains. |
| `imports` | When the signature's exact `U.ClaimGraph` states that it uses provided names or cited laws from named provider declarations, this entry carries that claim content or visibly represents it. The designators, governed references, or list membership alone establish no dependency or source-use occurrence. |
| `provides` | When the signature's exact `U.ClaimGraph` states that it introduces public names for dependent use, including public SlotKinds and RefKinds, this entry carries that claim content or visibly represents it. Being listed establishes no consumer dependency by itself. |

A change confined to the spelling of `id` or the serialization of `signatureRef` preserves episteme identity only when the reference still resolves to the same episteme and its exact claim content, exact EntityOfConcern, and effective `U.ReferenceScheme` remain unchanged. Changing `signatureRef.edition` selects another already recoverable edition; it does not by itself establish an edition relation, historical continuity, or `U.Signature` membership for the referent. If a C.2.1 identity discriminator changes, A.6.0:4.10 governs the resulting identity.

Use these dependency-manifest predicates:

- **SM-1 Name resolution.** Every referenced non-local declaration name resolves under the effective reference scheme to one named imported provider that declares that name.
- **SM-2 No redeclaration.** A provided name is not also provided by a transitive import under the same effective reference scheme.
- **SM-3 Replay order.** When a selected replay method orders the declared import designations from providers to consumers, that order is acyclic. Any graph, cycle check, or ordering notation remains a C.29 representation; replay order does not make a generic dependency relation obtain.
- **SM-4 Export boundary.** A dependent declaration relies on provided names and cited laws, not on private publication layout or implementation detail.

When interpretation or replay actually depends on another declaration or source, name the already-governed dependency or source-use relation only when its own predicate obtains. A citation, manifest entry, list membership, or replay result can support an assertion about that relation but does not create the relation occurrence. A provider or provider-edition change may require resolution, replay, or currentness review; it changes the consumer signature's identity only when the consumer's own claim content, exact EntityOfConcern, or effective reference scheme changes.

A governed reference to a separately identified object is not an exported vocabulary name merely because that reference appears in the signature.

#### A.6.0:4.6 - Specialize declaration use without minting another root kind

A signature profile is a constrained use of the same `U.Signature` kind. The profile states which content is current and which neighboring patterns govern later use.

**`profile = FormalSubstrate`.** Declare vocabulary and terms, inference kinds, formal laws, applicability, and the actual declaration dependencies carried in the signature's claim content. A.6.1 separately governs `OperationAlgebra`, operation designators, typed argument and result positions, admission conditions, application, and realization. An A.6.1 declaration may cite the FormalSubstrate signature; that citation does not make the operation part of this signature. When a mathematical object is selected as a lens for another entity, C.29 governs the lens-use claim; usefulness does not make the mathematical object a signature.

**`profile = PrincipleFrame`.** Declare postulates, invariants, and observability intent. Characteristic definitions, units, and scales remain under A.17, A.18, and C.16; `CHR:ReferencePlane` values remain under CHR; comparison remains under A.19.CPM; and normalization remains under A.19.UNM. The PrincipleFrame cites those independently identified declarations when they are current; their objects do not become extra PrincipleFrame identity components merely by citation.

A relation between two signatures is stated directly as refinement, conservative extension, equivalence, or another independently governed relation only when that relation's own predicate obtains. A claimed refinement states which vocabulary and laws are preserved, strengthened, or changed. Use a C.29 morphism only when a mathematical structure-preservation claim is actually current.

#### A.6.0:4.7 - Keep declaration, realization, and use under their direct patterns

| Current object or claim | Governing pattern |
|---|---|
| Constitution and C.2.1 identity of the exact claim-bearing episteme, including a separately identified relation-occurrence description episteme | C.2.1; the direct object or relation pattern still governs the described EntityOfConcern |
| Reusable declaration episteme and `U.Signature` membership | A.6.0 |
| Relation obtaining and explicitly individuated occurrence | Direct relation pattern and A.6.REL |
| `RelationSignature` SlotSpecs and participant-designation discipline | A.6.5 |
| Mechanism `OperationAlgebra`, typed argument and result positions, admission conditions, application, and realization | A.6.1 |
| Method | A.3.1 |
| Performed work | A.15.1 |
| Optional source-to-receiving-episteme viewing construction | A.6.3 |
| Same-EntityOfConcern representation-scheme transition | A.6.3.RT |
| Cross-reference-scheme, cross-plane, or cross-model-use-structure use with explicit preservation and loss | F.9 for the exact bridge relation; the direct pattern for the affected meaning or structure remains authoritative |
| Numeric comparison, normalization, units, scales, and measurement | A.19.CPM and A.19.UNM, together with A.17, A.18, C.16, and the direct measurement pattern when each object or relation is current |
| Actual mathematical or diagrammatic lens, operand mapping, or correspondence use | C.29 |
| Current representation-factor bundle for governed episteme publication positions | C.2.7 |
| Publication-face use and the distinct publication occurrence, form, and carrier relations | E.17 for the publication-face use profile; E.24.PUB for the direct occurrence, form, and carrier relations |
| Evidence-use or status-use relation | A.2.4 |
| Evidence-provenance graph or path | A.10 |
| Assurance claim or reliance-safety assurance record | B.3 |
| Operational gate profile and the decision that uses its result | A.21 and C.11 |

The rows name the direct patterns that govern these common adjacent objects and claims. Their co-location is only a compact representation and does not change any governing pattern's scope.

#### A.6.0:4.8 - Add explicit objects only for a named receiving use

Make three receiving-use decisions while keeping their objects distinct:

1. A readable direct relational assertion designates the actual participants and states affirmative or negative assertion polarity for the direct obtaining predicate. The exact direct claim family governs a forecast, scenario, counterfactual, permission, or other non-ordinary claim when one is current. When an explicit reliance judgment is current for the receiving use, `A.10` or the receiving evaluation separately states supported, refuted, or unresolved reliance; without that question, the readable direct assertion is sufficient. The direct relation pattern still determines whether the relation obtains.
2. Repeated typed use may justify authoring, selecting, or reusing a shared signature declaration for vocabulary, laws, applicability, or dependencies. When a new declaration is authored, its own claim content, exact EntityOfConcern, effective reference scheme, and C.2.1 constitution identify the episteme; A.6.0 then judges whether that same episteme satisfies `U.Signature` membership.
3. An obtaining `U.Relation` occurrence is explicitly recognized and individuated when a receiving claim or operation consumes that occurrence's identity.

These decisions concern explicitness for different objects and distinct acts of explicit recognition, not stages that construct a relation or an episteme from need. A receiving need is a reason to author, select, reuse, or explicitly individuate; it is not an identity criterion and creates neither the episteme nor the relation occurrence. A claim about condition-dependent entries, branches, returns, or stops is a CGUS claim governed by A.22.CGUS.

Stop when the named receiving use is served. Engineers author signature, assertion, and description epistemes only when their receiving uses need them; selecting or reusing an existing episteme leaves its identity unchanged. They assign or use occurrence designators and references separately under F.18 only when another claim or operation needs occurrence identity. Neither episteme authorship nor reference use creates the relation occurrence.

#### A.6.0:4.9 - Recover formal-substrate and PrincipleFrame uses by direct governing relation

| Current claim | Direct governed use |
|---|---|
| Author, select, or cite a formal declaration | Use `U.Signature(profile=FormalSubstrate)` with its subject, vocabulary, inference kinds, laws, applicability, and real dependencies. |
| Use a mathematical object to preserve selected structure while hiding other structure | Use C.29 and state the mathematical-lens relation. |
| Declare, apply, or realize an operation | Use A.6.1 for the `OperationAlgebra`, typed argument and result positions, admission conditions, application, and realization; cite a FormalSubstrate signature only when that named dependency is current. |
| Carry an encountered distinction toward later work | Use E.18.1 for the carry-through relation; that relation does not decide signature, operation, or lens adequacy. |

The same independently identified formal object or episteme can participate in these different uses while retaining its own identity and kind. Its identity does not decide which declaration, dependency, operation, lens, or carry-through relation is current.

For `PrincipleFrame`, write postulates and observability intent first. Cite an independently identified ontology, characteristic, measurement, scale, comparator, or normalization declaration only when that citation is current for the PrincipleFrame's claims. A cited declaration may be superseded, or an independently obtaining dependency relation may cease or be replaced, without retroactively changing the PrincipleFrame's identity. Changing the PrincipleFrame's own citation or dependency claim changes its claim content and therefore identifies another episteme; the same follows when its exact EntityOfConcern or effective reference scheme changes. Any edition, refinement, or supersession relation between the two epistemes must independently obtain.

#### A.6.0:4.10 - Change the exact object that changed

Apply C.2.1 first. Every `U.Episteme` is identified by exact claim content carried by one exact `U.ClaimGraph`, one exact EntityOfConcern, and one effective `U.ReferenceScheme`. Changing any member of this mandatory triple identifies another episteme. That episteme is a `U.Signature` only when it independently satisfies A.6.0 membership. A changed discriminator, `SignatureId`, or `signatureRef.edition` value does not by itself establish signature membership or historical continuity.

A change to `imports` or `provides` changes the consumer signature's identity only when it changes that signature's own claim content. A changed provider or provider edition can instead leave the consumer episteme unchanged while requiring the named dependency or source-use assertion, resolution result, replay result, or currentness judgment to be reconsidered.

A changed later use does not change the signature unless the change alters one of its C.2.1 identity discriminators. For example, a new mechanism realization remains a new realization, and a new publication layout remains a new publication form.

Connect two different epistemes by `EpistemeEditionRelation`, refinement, supersession, or another independently governed continuity relation only when that relation's own predicate obtains under its direct governor. Revision work, shared title, changed identifier, citation, or sequence alone establishes no such occurrence.

When a once-current signature becomes stale while its identity remains recoverable, G.11 governs currentness and selection among recoverable editions. G.11 creates neither a later episteme nor an edition, refinement, or supersession relation.

### A.6.0:5 - Archetypal Grounding

#### A.6.0:5.1 - Physical modeling: electrical connector declaration

A multi-domain modeling team repeatedly uses an electrical connector declaration. The signature's `EntityOfConcernRef` identifies the connector-relation kind. Its Vocabulary names potential and flow variables. Its Laws state potential equality and the zero-sum flow condition. Applicability states the modeling assumptions and selected `CHR:ReferencePlane`.

A concrete connection assertion among modeled component instances is a later model-side relation claim. A dated equation-generation work occurrence enacts a selected method and has a direct `performedBy` relation to the exact covering `U.RoleAssignment` whose holder is the modeling system; any mechanism realization is a separate A.6.1-governed claim. A diagram is an optional representation episteme; a publication occurrence may make its selected edition available through a diagram-shaped publication form. The signature remains the declaration cited by those later epistemes and work claims.

Practical payoff: engineers can compare the connector variables and laws in two declaration epistemes irrespective of which tools render them. The direct connection pattern remains authoritative for an actual assembly relation, generated equations remain result epistemes of equation-generation work, and a drawing remains a representation episteme.

#### A.6.0:5.2 - Clinical work: dose-response relation

A clinical modeling group reuses `DoseResponseRelationKind`. The relation signature names `PatientEpisodeSlot`, `InterventionSlot`, `OutcomeCharacteristicSlot`, and `ObservationWindowSlot`. Its Laws declare the response predicate and the temporal-aggregation conditions under which that predicate is evaluated. Applicability identifies the studied population, intervention kind, declared dosing frequency and timing conditions, and observation interval. The effective reference scheme separately fixes how the declaration content is interpreted.

The signature does not assert that one patient responded. A response assertion designates the actual participants and states affirmative or negative assertion polarity for the response predicate. When an evidence-use question is current, an evidence-use relation using A.2.4 SlotKinds may relate a selected assay-result episteme to that response assertion and carry the assay episteme, target assertion, named claim scope, evidential polarity, relevance window, and provenance constraints. When an explicit reliance judgment is also current for the declared use, `A.10` or the receiving evaluation separately returns supported, refuted, or unresolved reliance. Neither the evidence-use relation nor that reliance result determines whether the response relation obtains; the direct response pattern does so independently. A changed assay result or later use leaves the signature unchanged. If the declared outcome characteristic or Applicability changes, the exact claim content carried by the signature's `U.ClaimGraph` changes and C.2.1 identifies another episteme. A.6.0 then judges `U.Signature` membership independently, and any edition, refinement, or supersession relation must separately obtain.

Practical payoff: protocol authors and analysts can share the relation declaration while keeping patient occurrences, evidence epistemes, and their claim-bound evidence-use relations under their own identities.

#### A.6.0:5.3 - Learning: demonstrated-competence relation

A curriculum-design team reuses `DemonstratedCompetenceRelationKind` for a learning program. The signature declares `LearnerSlot`, `PerformanceSlot`, `CriterionSlot`, and `AssessmentWindowSlot`. Its laws state how the criterion relates observed performance to the competence claim. Applicability fixes the curriculum edition and assessment conditions.

A learner's performance occurrence and an assessor's claim remain separate. The signature makes the judgment-relation declaration reusable; it does not make the competence claim true.

Practical payoff: changing the publication form or making a new publication occurrence for the course description changes neither the signature episteme nor any demonstrated-competence relation occurrence. A changed declared criterion changes the exact claim content carried by the signature's `U.ClaimGraph` and identifies another episteme; A.6.0 separately judges `U.Signature` membership, and the named continuity predicate must independently obtain before the later episteme is called a continuing signature edition.

#### A.6.0:5.4 - Formal work: dependent operation parameters

A FormalSubstrate signature is used with an operator whose result kind depends on one input. A separate A.6.1 operation declaration names the input arguments, their ValueKinds, the ResultKind, and the dependent law; it cites the FormalSubstrate signature only when that declaration dependency is current. A Lean structure or another dependent-type representation can encode those declarations precisely, but its fields, argument order, and tuple forms remain representation-side.

When an FPF relation claim consumes that formal representation, C.29 states what structure the representation preserves and an explicit correspondence relates its operands to the independently declared `RelationSignature` SlotSpecs. A.6.3.RT governs the representation transition. Neither notation nor correspondence changes either declaration's EntityOfConcern, effective `U.ReferenceScheme`, Applicability, or identity.

Practical payoff: formal-methods engineers can inspect the dependency in the operation declaration and compare another representation without importing mathematical operand order into relation ontology.

#### A.6.0:5.5 - Reduced ordinary-use case

The sentence `Bearing B-17 is installed in pump P-4 at seat S-2` is enough when no later use needs a reusable declaration or occurrence reference. Stopping here serves the named receiving use because neither a reusable declaration nor an occurrence reference is current; it is not an incomplete signature.

### A.6.0:6 - Bias-Annotation

**Scope declaration:** Universal across FPF-governed domains.

- **Gov.** Favors making the direct governor of declaration membership, declared content, and neighboring claims inspectable, together with explicit dependencies. Counter-risk: declaration administration can grow beyond reuse value. Mitigation: add `SignatureManifest` only for actual dependency.
- **Arch.** Favors a small declaration core with direct neighboring patterns. Counter-risk: the signature becomes a central container. Mitigation: keep realization, work, evaluation, and publication with their direct patterns.
- **Onto-Epist.** Favors strict separation of declaration episteme, declared subject, obtaining occurrence, assertion, and representation. Counter-risk: excessive explicitness. Mitigation: stop when the named receiving use is served.
- **Prag.** Favors reusable named SlotSpecs and laws. Counter-risk: one-off work becomes formal paperwork. Mitigation: ordinary direct sentences remain sufficient.
- **Did.** Favors the four content groups and local mantra. Counter-risk: readers mistake the mnemonic order for executable work. Mitigation: A.22.CGUS governs any claimed executable conditional continuation.

The examples deliberately span physical modeling, medicine, learning, and formal work. Each worked declaration has its own C.2.1 identity, which remains independent of its publication form; the examples do not share one declaration individual.

### A.6.0:7 - Conformance Checklist

1. **Exact declaration object.** The text identifies one `U.Signature` episteme and one exact `EntityOfConcernRef`.
2. **Identity.** Content, EntityOfConcern, and effective `U.ReferenceScheme` remain recoverable.
3. **Minimum content.** `SubjectKind` and `RangedValueKind`, together with Vocabulary, Laws, and Applicability, carry semantic content rather than empty publication rows. `ResultKind`, `SliceSet`, and `ExtentRule` appear only when their declared distinctions are current.
4. **Optional quantification.** SliceSet and ExtentRule appear only when a receiving use depends on varying extension.
5. **Vocabulary boundary.** A declared token is not treated as durable U-kind admission without E.24.UK and its direct pattern.
6. **Relation declaration.** A `RelationSignature` identifies one already admitted direct relation kind. An admitted derived relation kind already has obtaining and occurrence-identity laws under its direct governor. A predicate-definition episteme is not treated as that `RelationSignature`, and the declaration does not assert an occurrence.
7. **Direct relation-pattern governance.** The direct relation pattern governs obtaining and occurrence identity.
8. **Typed-declaration boundary.** Reused participant meanings are declared inside a `RelationSignature` by A.6.5 SlotSpecs with exact SlotKind, ValueKind, and refMode. Operation arguments and results remain A.6.1 declaration content. Mathematical operands remain C.29 representation elements, with explicit correspondence to `RelationSignature` SlotSpecs only when a relation claim consumes them.
9. **Semantic locality.** Meaning uses the effective reference scheme; applicability uses the exact claim scope and only qualifiers current for the declaration, such as a relevant time interval, selected `CHR:ReferencePlane`, or genuinely current model-use structure.
10. **Dependency truth.** Imports and provided names correspond to actual declaration dependencies; SM-1 through SM-4 hold for the claimed use.
11. **Realization boundary.** Mechanism behavior and admission conditions remain with A.6.1.
12. **Progressive elaboration.** Explicit signature and relation-occurrence identity appear only for named receiving uses.
13. **CGUS boundary.** Mnemonic imperatives are not called an executable sequence; any condition-governed unfolding claim uses A.22.CGUS.
14. **Profile identity.** FormalSubstrate and PrincipleFrame remain profiles of `U.Signature` rather than new root kinds.
15. **Changed object.** Changed exact claim content carried by the `U.ClaimGraph`, exact EntityOfConcern, or effective reference scheme identifies another episteme. Judge A.6.0 membership for that episteme independently, and assert edition, refinement, supersession, or another continuity relation only when its own predicate obtains. A changed use, identifier, publication form, carrier, provider currentness, or G.11 refresh state does none of those things by itself.
16. **Cross-domain fit.** The declaration preserves the direct physical, biological, social, and epistemic EntityOfConcern kinds in its worked cases.

### A.6.0:8 - Common Anti-Patterns and How to Avoid Them

| Failure mode | Why it fails | Repair |
|---|---|---|
| Signature as publication template | Visual rows and publication metadata become signature identity. | Recover the declaration content and C.2.1 identity; govern publication separately. |
| Relation signature as relation occurrence | Declaring participant meanings and laws is treated as evidence that the relation obtains. | Evaluate the direct predicate for the actual participants, state affirmative or negative assertion polarity under the exact direct claim family, keep supported, refuted, or unresolved reliance with `A.10` or the receiving evaluation, and use A.6.REL only when a receiving use needs occurrence identity. |
| Applicability as context label | One undefined context word hides reference scheme, claim scope, time, selected `CHR:ReferencePlane`, and model use. | Recover each current qualifier under its direct kind or relation. |
| Mandatory maximum form | Every sentence receives SlotSpecs, dependencies, editions, and occurrence records. | Name the receiving use and include only the declaration or occurrence-identity objects it needs. |
| Mnemonic as executable sequence | Imperative wording is treated as a runnable continuation structure. | Keep it as Plain recall or declare the actual condition-governed structure with A.22.CGUS. |
| Realization inside the declaration | Current mechanism behavior or test outcomes become signature laws. | Keep declared laws here; state the mechanism declaration or realization under A.6.1 and the evaluation claim under its direct evaluation pattern. |

### A.6.0:9 - Consequences

**Benefits.**

- Reusable declarations receive one stable episteme identity.
- `RelationSignature` epistemes can expose named typed SlotSpecs without forcing every relation occurrence into a record.
- Meaning becomes inspectable through the exact reference scheme; applicability becomes inspectable through the exact claim scope plus any current time interval, selected `CHR:ReferencePlane`, or selected model-use structure.
- Physical and clinical work retain their world-side entities while using the same declaration discipline.
- A changed realization can be repaired independently from its declaration.

**Costs and trade-offs.**

- Authors recover the exact declared subject and effective reference scheme; a familiar label is not enough.
- Typed reuse can add authoring effort for A.6.5 relation SlotSpecs or A.6.1 operation declarations, plus A.6.0 dependency declarations when another signature relies on its provided names or laws.
- A change to exact claim content, EntityOfConcern, or effective reference scheme identifies another episteme even when the publication looks identical; authors must separately judge `U.Signature` membership and any claimed edition, refinement, or supersession relation.
- The practitioner separately judges whether a receiving use needs a reusable declaration or occurrence identity. The worked cases and checklist make that judgment reviewable.

### A.6.0:10 - Rationale

The ontic is needed because the same reusable declaration is cited across work occurrences, publication occurrences, and representations. Treating it as only a table-shaped publication form loses identity; treating it as the declared world-side object collapses episteme and EntityOfConcern.

The declaration components answer four different engineering questions. `SubjectKind`, `RangedValueKind`, optional `ResultKind`, `SliceSet`, and `ExtentRule` identify what is declared and any varying extension. Vocabulary supplies reusable names and, for a RelationSignature, named participant SlotSpecs; A.6.1 supplies operation arguments and results for a mechanism declaration. Laws state the reusable regularities. Applicability states where those regularities are used. Their conceptual separation is stable even when publication layout changes.

`RelationSignature` is a use of `U.Signature` because it has the same episteme identity and content duties. Introducing a second root kind would duplicate those duties while leaving obtaining and occurrence identity with direct relation patterns anyway.

Progressive elaboration protects didactic primacy. A practitioner can begin with a readable relation sentence and add formal declaration only when reuse creates value. Exactness is increased for a named claim or operation, not for ceremony.

### A.6.0:11 - SoTA-Echoing

| Current source | What it contributes | FPF disposition and practical implication |
|---|---|---|
| The current Modelica 3.8 development specification, Chapter 9, separates connector declarations, concrete connect equations, generated connection sets, and optional graphics. | A reusable declaration can specify named connector variables and laws without becoming the connection occurrence or its diagram. | **Adopt and generalize.** A physical-modeling engineer can compare declarations independently from actual assemblies and generated equations. The source is the current primary language-specification basis, not FPF ontology authority. This disciplines case 5.1. |
| The current Lean Language Reference, covering Lean `4.33.0-rc1`, describes structures through named fields whose types may depend on earlier fields, while the kernel checks formal terms independently from presentation convenience. | Named formal fields and dependent types make the operation dependency inspectable and reduce reliance on numeric argument convention. | **Adapt as a current dependent-type representation precedent.** A formal-methods engineer can inspect dependent argument and result declarations under A.6.1 while C.29 keeps Lean fields and operand order representation-side; an explicit correspondence is required when a relation claim consumes those operands. Lean remains one representation, not FPF ontology. This disciplines case 5.4. |
| TypeDB 3.x declares relation types through explicit related role types and can specialize those declarations. | Reusable relation declarations benefit from stable local names for participant meanings. | **Adapt with a stricter boundary.** A schema author can reuse stable participant names through `RelationSignature` SlotSpecs without treating database role types as system roles or world-side participants; relation obtaining remains independent from schema declaration. This disciplines sections 4.3 and 4.4. |
| For the RDF-validation branch, SHACL 1.2 Core gives the current standards-track answer by separating shapes graphs, evaluated data graphs, validation work, and validation reports; its Working Draft status and 30 June 2026 date are not by themselves the basis for use. | Declared constraints, evaluated entities, and evaluation results remain different objects. | **Adapt as a work-in-progress representation precedent beyond RDF.** A protocol or curriculum author can keep signature laws, governed subjects, evaluation work, evaluation-result epistemes, and later evidence-use relations separate across domains without importing draft SHACL terms as ontology. This disciplines the clinical and learning cases. |
| For the semantic-web foundational-ontology branch, the March 2026 gUFO preprint gives a current branch answer by using reification patterns for relational aspects; its recency is not by itself the basis for use. | Relation representation makes arity and participant dependence explicit. | **Reject as FPF ontology; retain only as a current stress comparator.** A practitioner can start with a direct relation assertion and introduce a `RelationSignature` or explicit occurrence identity only when a named receiving use needs it, rather than importing gUFO taxonomy. This disciplines sections 4.3 and 4.8. |

Sources:

- Modelica Association, [Connectors and Connections](https://specification.modelica.org/master/connectors-and-connections.html).
- Lean project, [Inductive Types and Structures](https://lean-lang.org/doc/reference/latest/The-Type-System/Inductive-Types/).
- TypeDB, [`relates` statement](https://typedb.com/docs/typeql-reference/statements/relates/).
- W3C, [SHACL 1.2 Core](https://www.w3.org/TR/shacl12-core/).
- Almeida, Guizzardi, Sales, and Fonseca, [gUFO: A Gentle Foundational Ontology for Semantic Web Knowledge Graphs](https://arxiv.org/abs/2603.20948).

These sources test the separation among declaration, represented structure, realization, and use. FPF's constructive ontology, C.2.1 episteme identity, A.6.5 relation-slot discipline, A.6.1 operation declaration, and direct relation patterns remain authoritative for the solution.

### A.6.0:12 - Relations

- **Builds on:** A.7, C.2.1, C.3, A.2.6, and A.6.5.
- **Governs:** reusable `U.Signature` declaration epistemes, including `RelationSignature` use and the FormalSubstrate and PrincipleFrame profiles.
- **Coordinates with:** A.6.REL for relation occurrence, A.6.1 for mechanism declaration and realization, A.3.1 for methods, A.15.1 for work, F.9 for explicit bridge use, A.17, A.18, C.16, A.19.CPM, and A.19.UNM for characteristic, scale, comparison, and normalization questions, C.29 for mathematical-lens use, and E.24.UK for durable U-kind admission.
- **Described and published through:** C.2.1, E.17, and E.24.PUB.
- **Evolves with:** G.11 for currentness and explicit direct relations between signature editions.
- **Used by:** C.22 task signatures for A.6.0 declaration identity and content; a changed C.22 discriminator identifies another episteme and establishes an edition only when the direct continuity predicate obtains. Also used by A.19.CPM comparison declarations, A.19.SelectorMechanism selection declarations, C.29 and E.18.1 when their current claim requires a FormalSubstrate declaration, and any pattern that needs reusable vocabulary, laws, applicability, or relation SlotSpecs. Specialized operation declarations remain under A.6.1 rather than A.6.0.

### A.6.0:End

