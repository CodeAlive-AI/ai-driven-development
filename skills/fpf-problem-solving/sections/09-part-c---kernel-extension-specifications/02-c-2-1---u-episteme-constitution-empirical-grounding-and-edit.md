## C.2.1 - `U.Episteme`: Constitution, Empirical Grounding, and Edition Relations

> **Type:** Pattern
> **Status:** Stable
> **Normativity:** Normative except where a section is explicitly marked informative

**Plain name.** Episteme constitution.

**Use this pattern when.** You need to identify or compare a body of knowledge: what it claims, the exact entity those claims concern, and the rules under which they are interpreted. A pump specification with a changed pressure threshold carries different claims. Publishing the same claims about the same pump under the same interpretation in another file preserves the episteme.

**First useful move.** If the claim is still taking shape, use :4.1.1 to develop it in writing. Ask: what is claimed; what exact entity are the claims about; and what designation and interpretation rules make those claims readable about that entity? Include measurement, comparison or evaluation rules where the claims use them. If identity is all the task needs, stop after those answers. Otherwise name the concrete receiving use and open only the corresponding branch in :4.0. An unresolved uncertainty or choice is needed only when the use involves a real inquiry or decision.

**One-line summary.** A `U.Episteme` is a knowledge holon identified by exact claim content, one exact EntityOfConcern, and the effective `ReferenceScheme` that makes the claims interpretable about that entity. Changing any of these three discriminators identifies another episteme.

**Primary working reader and viewpoint.** The engineer or researcher comparing, revising, teaching, grounding or publishing that knowledge object. The working concern is to reidentify it through those uses and locate a change when it occurs.

**Primary governed object and architecture.** One `U.Episteme` and its `EpistemeConstitutionRelation`, `EpistemeEmpiricalGroundingRelation` and `EpistemeEditionRelation`. The EntityOfConcern of the episteme is the entity its claims concern; for a pump specification, it is the pump, while C.2.1 governs the specification's identity.

**What goes wrong if missed.** A shared filename hides changed claims, subject or interpretation; or a changed display is reported as a changed model. **What this buys.** The practitioner can identify the changed knowledge object or update only the relation affected by a new grounding, view or publication use.

A theory, model, specification, proof or diagnosis can be an episteme when the selected object is that claim-bearing whole. A diagram can carry such claims too. When the task concerns its layout or the calculations available through its notation, use the publication or representation branch in :4.0.

**Not this pattern when.** To inspect or change the pump, perform work, or apply a method, use that subject's direct pattern. Open C.2.1 when the identity of the claims describing it matters. A separately inspected classification assertion has its own claim content, subject and scheme; its governing criterion remains under `A.1` or `C.3.2`, with `E.24.UK` used for public U-kind admission.

### C.2.1:1 - Problem Frame

FPF treats an episteme as a holon, not as a document class or a filled record. It is a claim-bearing whole about an exact EntityOfConcern under an effective reference scheme. Carriers, notations, and admissible operations can differ; the identity question is what makes this one episteme and what changes it.


The core constructive question is whether an exact `ClaimGraph`, exact `U.Entity`, and effective `ReferenceScheme` stand in the relation that makes the claim content interpretable and evaluable as claims about that entity. When they do, their selected organization yields a whole-level epistemic characteristic: the resulting holon can be used as one defeasible or deductive body of knowledge. That characteristic is not supplied by any one participant alone.

Any exact `U.Entity` can participate as the EntityOfConcern. An episteme can therefore concern another episteme or itself without changing the constitution relation.

Different representation regimes can support different operations. Make the representation and its admitted operations explicit when the current use needs them. Identify the episteme by its claim content, EntityOfConcern, and effective ReferenceScheme.

### C.2.1:2 - Problem

Without one direct episteme ontology, several practical failures recur.

1. **Carrier and episteme collapse.** A PDF, database row, proof script, dashboard, or neural-model file is treated as the knowledge holon. File replacement is then reported as epistemic change even when claim content, EntityOfConcern, and interpretation are unchanged.
2. **Subject drift.** A specification or model keeps one label while the entity it concerns changes. Comparison and evidence use then combine claims about different entities.
3. **Interpretation drift.** The same tokens or graph are read under different designation, measurement, or evaluation rules while users assume one unchanged episteme.
4. **Neighboring-relation collapse.** Grounding holon, viewpoint, view, claim scope, model-use structure, evidence, edition, and publication become optional fields of one omnibus record. Their different obtaining and identity rules disappear.
5. **Representation-first ontology.** Tuple components, graph nodes, schema fields, and database keys are treated as actual relation participants or subject identity discriminators merely because a tool exposes them.
6. **Agency leakage.** An episteme or its claim graph is said to perform Work. Systems perform Work; the claim content can guide or constrain it.
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

Identify each `U.Episteme` through `EpistemeConstitutionRelation`: first state what it says, what exact entity it concerns, and the scheme under which those claims are read. Then name what the reader will do with that episteme. Add a neighboring relation only when the reader's next sentence or action requires it. The conditional branches below supply the relevant direct relation and its test.

**Local episteme mantra.** *Name the claims, what they concern, and the scheme that gives those claims their reference. Stop if identity is all the task needs. Otherwise name the concrete receiving use and add only the neighboring object or relation needed for its next sentence or action. Ask for an unresolved question only in a real inquiry or decision. Update episteme identity only when claim content, EntityOfConcern, or effective reference scheme changes; otherwise update the affected relation or object under its direct pattern.*

The mantra is a recall aid, not a work plan. The application method and stop conditions are carried by sections 4.1-4.9; section 4.10 is a later reference for relation and neighboring-object distinctions.

#### C.2.1:4.0 - First-use completeness questions

Begin with the three questions that identify the episteme. They are identity questions, not fields to fill. When the answers are still being developed, :4.1.1 connects the writing work in C.2.4:4.6 to the resulting constitution judgment.

| Always ask | Exact object recovered |
| --- | --- |
| What is being claimed? | the exact claim content carried by one `ClaimGraph` |
| What exact entity do those claims concern? | one identified `U.Entity` participating as the EntityOfConcern |
| Under which designation and interpretation rules are the claims read, and, where the claims use them, which measurement, comparison, or evaluation rules apply? | the effective `ReferenceScheme` |

If the task needs only the episteme's identity, stop after the three answers. Otherwise state the concrete receiving use. Ask for an unresolved uncertainty or choice only when that use is a real inquiry or decision.

Open a row below only when its first column names the reader's next sentence or action. Each positive answer adds an independently governed object or direct relation; none adds another slot or identity discriminator to the episteme.

| Open this row when the next sentence or action is... | Recover | Subject pattern |
| --- | --- | --- |
| A claim or relation must cite the exact constitution occurrence, not merely say that the episteme exists. | one exact obtaining `EpistemeConstitutionRelation` occurrence, reidentified by the participant triple; designate it when an epistemic receiver needs a reference, or use the occurrence itself as a participant when another direct relation is the receiver | C.2.1:4.2.3 and `A.6.REL` |
| A reader must cite one exact claim inside one exact episteme edition, rather than the whole episteme. | one `ClaimAddress`: an exact episteme-edition reference plus an intrinsic claim identity declared by that edition's exact ClaimGraph; if no such identity resolves uniquely, cite the whole episteme or identify the claim as a separate episteme | C.2.1:4.2.5 |
| A typed interface needs replaceable interpretation rules or exact content, or must recover that value from an addressable episteme. | the receiving range, exact constituent value and any required designation/resolution; keep membership separate from successful use | C.2.1:4.1.2 and :4.2.6 |
| An observer must inspect designated empirical claims against current observation, intervention, measurement, or test relations involving one exact holon. | one exact `EpistemeEmpiricalGroundingRelation` occurrence, its covered claim subgraph, claim-to-world mappings, and grounding holon; recover supporting evaluation or evidence use separately | C.2.1:4.3 and the direct observation, intervention, measurement, test, evaluation, or evidence pattern |
| A description must state the concern from which this episteme is read. | one exact `U.Viewpoint` episteme P and the named describing use that selects P; keep the episteme, its EntityOfConcern, the use, and P distinct | `E.10.D2` and `E.17.0` |
| A team will validate a Description as a specification before relying on it. | the exact Description episteme, checkable claims, and named harness or validation relation; preserve or update the named describing-use viewpoint only when that selection affects reliance | `E.10.D2` and C.2.1:6 |
| A classification assertion must say that this episteme conforms to a viewpoint and is a `U.View`. | one exact obtaining `EpistemeViewpointConformanceRelation` between this episteme and at least one exact `U.Viewpoint` episteme | `E.17.0` |
| A reader must trace how this episteme was constructed from an earlier source episteme. | the exact source and receiving epistemes plus the governed viewing relation; view membership remains a separate conformance judgment | `A.6.3` for construction and `E.17.0` for membership |
| A claim must be restricted to one declared part of the situation under study. | one exact `U.ClaimScope` and its membership relation over `U.ContextSlice` | `A.2.6` |
| A calculation or interpretation must use one selected organization of model use. | one exact `BoundedModelUseStructure` and the relation through which the receiving assertion or use selects it | `A.1.1` and the direct receiving-use pattern |
| A reader proposes to compare, substitute, translate, publish, or otherwise use an obtaining cross-context Bridge. | one ordinary C.2.1 assertion episteme whose EntityOfConcern is that exact Bridge and whose ClaimGraph states the proposed use, direction, correspondence rule, loss tolerance, and polarity; recover reliance and any use that actually happened separately | C.2.1:4.2.3 for claim identity; `F.9` for the Bridge; `A.10` for ordinary evidence reliance; `B.3` only when an actual named assurance claim is current; the direct receiver pattern for any actual use |
| A decision or inference must cite support links among the claims. | the exact `JustificationGraph` content that carries those dependencies | C.2.1:4.4; use `A.10` only when ordinary evidence reliance is current, and `B.3` only when an actual named assurance claim is current |
| A decision or evaluation will accept, reject, or withhold reliance because of evidence. | the exact evidence-use relation; evidence storage alone is insufficient | `A.10` for ordinary evidence reliance; `B.3` only for an actual named assurance claim |
| Reviewers must inspect or revise a classification judgment as an independent claim-bearing object. | one classification assertion episteme about the exact candidate, plus the exact governing criterion | C.2.1:4.2.3 with `A.1` or `C.3.2`; `E.24.UK` only for public U-kind admission |
| A reader must assert that a later episteme revises, refines, or supersedes an earlier one. | one exact `EpistemeEditionRelation` occurrence | C.2.1:4.5 |
| An account must assert that particular Work occurred. | identify the actual performer and admit the dated Work independently; if the account also attributes it to an assignment, test that attribution separately | `A.13` and `A.15.1`; `F.6` only for the stated attribution |
| A publisher must make one selected episteme edition available to a declared audience for a bounded use. | the publication occurrence, publication form, and `U.PresentationCarrier` as distinct objects | `E.17` and `E.24.PUB` |
| A user will calculate, infer, navigate, or inspect through a representation whose available operations matter. | the representation scheme, operations and correspondence needed for that use | the applicable representation pattern; `A.6.3.RT` for a same-EntityOfConcern transition; `C.29` only for an unresolved mathematical-lens choice, transfer or reliance question |
| One receiving System must select, decline, or co-use candidate results of different kinds as representations for the same exact action or decision. | one C.37 use-bounded representation-selection account; keep each direct subject result, optional A.2.4 first-use classification, A.10 reliance path when material, and receiving result separately governed | `C.37` |


Stop when no row describes the next sentence or action. A readable sentence naming the claims, EntityOfConcern, and effective reference scheme is then enough. Do not complete the table as a record. Use section 4.10 only when a later sentence or action actually needs the full relation and neighboring-object reference.

#### C.2.1:4.1 - Identify the episteme by its constitution

The shared C.2.1 identity of one `U.Episteme` is:

```text
<claim content, exact EntityOfConcern, effective ReferenceScheme>
```

`claim content` is the identity-bearing `ClaimGraph` carried as the episteme's constitutive claim structure. Each episteme selects one exact `U.Entity` as the EntityOfConcern of the current claim-bearing whole. Its ClaimGraph may also designate other independently governed entities as participants in relational, comparative, negative, counterfactual, or modal claims.

When the subject really is an admitted relation kind, an already individuated obtaining relation occurrence, an admitted collection-as-whole, or another independently identified joint entity, that object may be the EntityOfConcern. Several participant designations do not by themselves constitute such an object. A negative or counterfactual relation claim can designate the relation kind and its participants in the ClaimGraph without requiring an obtaining world-side occurrence.

Split the ClaimGraph only when it combines independent subjects in a way that makes the selected EntityOfConcern untruthful or breaks the intended identity or comparison use; do not split merely because one predicate connects several participants. The reusable predicate-definition boundary is stricter: before publication, name one truthful exact EntityOfConcern and state what the definition claims about it. If no such single concern can be selected, remain at local compound-claim level.

The effective `ReferenceScheme` supplies the designation and interpretation rules needed to read this ClaimGraph as claims about this EntityOfConcern. Add measurement, comparison, or evaluation rules only when the claims' meaning uses them. The corresponding measurement or evaluation entities and relation occurrences remain under their direct patterns.

A theorem read under a formal vocabulary and calculus needs designation and interpretation rules; it needs measurement or evaluation rules only if its meaning uses them. By comparison, a pump-tolerance episteme uses the applicable units, measurement procedure, and pass/fail criterion to make its claim meaningful; the actual measurement and evaluation occurrences remain neighboring objects rather than episteme constituents.

Changing any identity discriminator yields another episteme. Changing a carrier, layout, rendering, publication occurrence, evidence item, viewpoint assignment, or model-use setting does not by itself yield another episteme. A direct pattern may recognize the same individual as a dependent episteme kind through its stable membership condition, but it does not add another identity discriminator. `A.3.2` governs `U.MethodDescription` membership; `E.17.0` governs `U.Viewpoint` and `U.View` membership through fixed predicates over already identified epistemes. `A.6.3` governs an optional viewing construction between source and receiving epistemes, not view membership. If any work or construction changes claim content, EntityOfConcern, or effective reference scheme, those changed C.2.1 discriminators identify the resulting episteme, not the dependent-kind label.

This identity is constructive. The claim graph and reference scheme are epistemic constituents; the EntityOfConcern remains an independently governed entity related through aboutness and reference. When `EpistemeConstitutionRelation` obtains, their organization yields the whole-level characteristic of being one interpretable claim-bearing whole. The relation occurrence and the resulting episteme are distinct but reidentified from the same three discriminators.

##### C.2.1:4.1.1 - Obtain the content, recover its interpretation, and compare a change

Writing can help obtain the content before it is a finished knowledge object. Following C.2.4:4.6, put the cue or earlier expression beside a proposed claim. Recover what it is about, what is asserted, and the conditions that make that assertion meaningful. Compare the proposal with the observations and reasons that prompted it; use the subject's Method when a missing distinction requires further investigation. Keep unresolved alternatives visible when they affect the next use. A note or partial card can support this work before its content satisfies the episteme-constitution predicate.

**Recover the whole asserted content.** `ClaimGraph` names the semantic claim content organized as a whole: the claims, their participants and predicates, polarity, conditions, and the asserted relations among claims. Include quantification, modal force, and grounds asserted as part of that account where they change what it says. A field named `claim` may carry only part of this content. A graph representation can express it, but graph nodes and edges have the identity of that representation. An episteme describing this content is another object, with the described content as its EntityOfConcern. A separately obtaining justification or evidence relation remains separate unless the account also asserts something about it.

**Recover the effective rules.** `ReferenceScheme` names the rules that actually govern designation and interpretation of this content about its EntityOfConcern. Recover what the expressions designate and how their combinations, qualifications, and inferential uses are read. Include measurement, comparison, or evaluation rules only where the claim's meaning uses them. A document describing those rules is an expression of the scheme; a rule elsewhere in that document enters the effective scheme only when it governs this account. A citation can identify the rules when its selected content is unambiguous; otherwise state the missing rule. An unresolved choice between materially different readings leaves that part of the constitution unresolved.

**Individuate content and rules before assigning a kind.** An exact body of interpreted claim content and an exact collection of operative rules are abstract `U.Entity` individuals under A.1:4.1. For the content, the discriminator is the complete selected claims with their interpreted meanings and asserted organization; for the rule collection, it is the operative rules with their application domains and interpreted dependencies. These discriminators identify the individual independently of the text, graph, document or episteme through which a reader obtains it. Giving those claims or rules under an unambiguous interpretation can designate the individual directly; :4.2.6 also permits designation through an exact episteme edition and selection. Different such designations can return the same individual. Changing any of these identity discriminators identifies another content or rule collection; an expression change that preserves them does not.

This individuation and reference basis permits the content or rules to be an actual relation participant or the EntityOfConcern of an episteme about them. Neither a slot assignment nor a classification judgment supplies that basis. Entity status alone establishes no holonhood, episteme membership or obtaining relation. When the needed interpretation or identity remains unresolved, preserve the partial written result and recover the missing distinction before using it as an exact participant. That limit on the exact use does not prevent writing from helping obtain the content.

**Choose the precision the receiving work needs.** Express the claim and rules well enough to perform the named comparison, interpretation, or revision. Ordinary prose, a diagram with a clear interpretation, or a partial written comparison can be sufficient. Add a C.3.2 classification only when the receiver needs a membership, substitution, or quantified-range judgment; identify the candidates and criterion for that particular classification. Classifying whole epistemes does not establish a kind for each of their constituents. Section :4.2.1 governs a receiving use that specifically needs typed constitution participants.

**Judge identity separately from admissibility and use.** For full episteme identity, compare the complete claim content and its semantic organization, the exact EntityOfConcern, and the effective interpretation rules. Supply the correspondence that makes the preserved claims and their conditions recoverable on both sides. In a formal subject, the declared semantics and a proof or exhaustive comparison may supply it. In ordinary language, use the subject's distinctions and stated bounds to compare what each account commits to; expose an ambiguity that prevents the comparison. Agreement on selected questions establishes only that bounded agreement. A conservative derivation may omit content and therefore does not by itself establish full identity.

A change to asserted meaning or grounds is a content change even if the principal sentence remains. Choosing a different interpretation rule changes the effective scheme even if all signs remain. Making an already determined meaning easier to recover can preserve both; adding a previously unsettled condition or commitment requires a new identity judgment. When only part of the account has been compared, preserve that partial result without asserting equality of the whole. There is no general procedure here for deciding equality of arbitrary natural-language meanings.

**Reconsider what depended on the changed value.** Use :4.8 to locate the change. A :4.2.5 ClaimAddress continues to designate its claim in the original exact episteme while the edition reference resolves and that ClaimGraph declares exactly one claim with the intrinsic identity. To use corresponding content in another episteme, establish the claim-to-claim correspondence and resolve an address in that episteme; the old address remains an address in the original episteme. Changed claims or interpretation can defeat a proposed transfer of empirical coverage, an A.6.6 claim selection, or a predicate evaluation. Retest the affected viewpoint-conformance, edition-continuity, or receiving-use conclusion under its own rule. Reuse an unaffected part only with the correspondence and conditions that support that reuse. A different expression or carrier with the same complete content and scheme leaves episteme identity intact, while its suitability for the receiving action still needs that action's criterion.

##### C.2.1:4.1.2 - Declare the range needed by a receiving interface

Use an exact value directly when the receiving question concerns that value alone. A fixed-scheme operation can put its rules in the operation declaration, as in B.1.3. A reusable typed interface with a variable argument or replaceable participant needs a range: the receiver must be able to distinguish an eligible replacement from an expression that merely looks similar. State that distinction before choosing a type name.

For the recurring interpretation and claim-content uses below, the following declarations identify two C.3 kind individuals over the abstract entities individuated under :4.1.1. The candidate domains retain the distinction between those entities and their documents, graph representations or describing epistemes. Each row supplies the candidate interpretation and membership rule of its C.3.2 KindSignature; no context-slice-dependent extension is needed for these content-fixed individuals.

| Kind individual and candidate domain | Operative membership condition | Value identity and relevant boundary |
| --- | --- | --- |
| `EpistemeInterpretationScheme`: abstract rule-collection entities, identified with their application domains | The collection contains rules determining designation or interpretation of claim expressions: what a designation refers to, how a predicate or combination is read, or how a qualification or inference contributes to the claim's meaning. Its rule domains and imported semantic dependencies belong to the identified collection. | Identify a value by the operative rules, their domains and interpreted dependencies. A collection prescribing only font, page placement or file encoding is a non-member. A document describing a scheme is not the rule collection. A precisely specified partial scheme can be a member while lacking a rule needed by a particular receiver. |
| `NonemptyClaimContent`: abstract content entities, identified as collections of interpreted claims and their selected semantic relations | The collection contains at least one claim with its participant and predicate meanings, polarity, qualifications and asserted interclaim relations. A whole ClaimGraph or an exact nonempty semantic subgraph can satisfy this condition. | Identify a value by that content and semantic organization under the declared interpretation. An empty collection is a non-member. An uninterpreted graph, a carrier and an episteme about the content are not candidates of this content-entity domain. False, conflicting or insufficiently supported claims can still be members. |

Under these candidate interpretations, `EpistemeInterpretationScheme` is a subkind of `U.Entity`, and `NonemptyClaimContent` is a subkind of `U.Entity`. C.3.1's criterion-entailment branch applies: every member must have the independent semantic identity and reference basis in :4.1.1 and therefore satisfies A.1:4.1. A.6.5 can use either range as an entity ValueKind; actual participation still requires the receiving relation's predicate to obtain.

Recover the candidate independently of the classification. C.3.2 first checks that the proposed candidate is a value in the stated domain; then it judges membership as true, false or unknown. Missing knowledge of a needed rule or content relation leaves that judgment unknown. It does not turn a known document into a rule collection, nor turn an unidentified expression into a fully identified value.

For scheme identity, compare the actual rules and domains, including the dependencies that determine their meaning. A restatement can preserve the scheme when an explicit alignment preserves those rules; agreement on a few outputs cannot establish that identity. A changed interpretation rule or domain identifies another scheme even if its name and document remain. For content identity, apply :4.1.1 to the whole selected content. Two designations from different source editions may return the same content under the same scheme. Source, acceptance, currentness and witness qualifications attached to a designation do not enter the designated semantic base merely because they accompany it, as in A.6.6. When the selected content itself asserts such a fact, that assertion belongs to the content being compared. A change of graph encoding preserves content only when the interpretation supplies the complete correspondence; graph shape alone supplies none.

The kinds themselves continue when their candidate domains and operative membership distinctions remain the same under C.3.1's comparison. Rewording the declaration or citing it from another pattern need not create another kind. Replacing the semantic rule/content criterion with the presence of a schema label would create another classification distinction. A change of one member's rules or claims instead identifies another value; it need not change the kind.

These declarations supply a shared range for the receiving interfaces that cite them. A.1.1 uses `EpistemeInterpretationScheme` for its coherence participant R; A.2.6, A.19.CPM and A.19.SelectorMechanism use it for a bound scheme argument. A.6.0's R7/R8 predicates use `NonemptyClaimContent` for exact dependent content and semantic bases. Reusing one criterion preserves the same meaning of admissible input across those interfaces. A receiver adds any narrower language, semantic-domain or representation condition its operation actually needs; that condition does not become another kind merely because another pattern states it. A recurring independently different classification requires its own C.3 declaration.

**Test replacement in the receiving use.** Resolve the proposed value, check the declared range and any narrower input conditions, then apply the receiver's own predicate or operation law. An eligible scheme need not interpret every actual input. Two eligible schemes need not be equal or admit a meaning-preserving translation. An eligible content value need not be a sufficient basis or an actually used premise. Missing interpretation stops the dependent operation; a false subject predicate remains a different result. For a cross-scheme use, establish the required correspondence, F.9 Bridge and bounded-use assertion where the receiving rule requires them, with A.10 reliance or B.3 assurance only under their own conditions. Membership supplies none of these results.

Retest dependent bindings and conclusions when the resolved value or a used rule changes. Reuse unchanged content only with its established correspondence and applicability. Keep the old value and its qualified conclusions available instead of rewriting them as statements about the replacement. These bounded C.3 declarations do not admit public `U.ReferenceScheme` or `U.ClaimGraph`; E.24.UK governs any separately needed durable U-kind proposal.

#### C.2.1:4.2 - Govern the core direct relation

**Tech name:** `EpistemeConstitutionRelation`.

**Plain reading:** these claims, under this reference scheme, are claims about this exact entity and together constitute one episteme.

##### C.2.1:4.2.1 - Participants and the shared reusable-declaration rule

The constitution predicate uses three actual participants, each an exact `U.Entity`. The content and rule collection have the independent semantic identities given in :4.1.1; the EntityOfConcern has its own subject-governed identity. Recover each before judging whether the relation obtains:

| Relation-participant meaning | What identifies the participant for this constitution |
| --- | --- |
| constitutive claim content | the abstract content entity identified by its complete semantic content and organization under :4.1.1; a selected graph representation supplies an expression, not its identity by itself |
| exact EntityOfConcern | one entity independently identified under its subject's rule |
| effective reference scheme | the abstract rule-collection entity identified by the designation and interpretation rules governing this account, with their domains and dependencies, under :4.1.1 |

This is sufficient for a direct constitution judgment with exact values. A reusable typed interface has an additional question: which candidates may replace a participant under its declared range? For that use, A.6.5 requires a complete SlotSpec with an independently governed ValueKind and designation mode. State the candidate domain, membership criterion, identity rule, and applicability needed by the receiver; use C.3.2 for a local classification and E.24.UK for a proposed public U-kind. Carrying the designation ByValue does not remove the membership requirement.

For reusable designation of the EntityOfConcern, `EpistemeConstitutionRelationSignature` declares `EpistemeConstitutionRelation` as its subject and `U.Entity` as the ranged kind for that participant. Its vocabulary includes the relation designator and the SlotSpec below; its laws are the obtaining and participant-determined identity rules in :4.2.2. Its applicability is the reusable designation and typing of the EntityOfConcern in a constitution assertion or description whose claim content and effective rules are recovered under :4.1.1. This declaration's own claim content, relation-kind EntityOfConcern, and effective FPF interpretation identify one declaration episteme; these subject, range, vocabulary, laws, and applicability contents satisfy A.6.0's `U.Signature` predicate.

| SlotKind | Relation-participant meaning | ValueKind | refMode |
| --- | --- | --- | --- |
| `EntityOfConcernSlot` | exact entity the claims concern | `U.Entity` | `U.EntityRef` |

Use this SlotSpec for the EntityOfConcern designation in A.6.REL:5.5 or B.2:5.1. An eligible designation must resolve to an independently identified entity; that typing alone does not establish that the claims concern it or that the constitution predicate obtains. The other two participants remain necessary exact constituents. Section :4.1.2 supplies bounded C.3 ranges for a receiving typed use; this EOC declaration does not thereby acquire further SlotSpecs. A use that additionally needs `ClaimGraphSlot` or `ReferenceSchemeSlot` must select the range appropriate to its participants and complete its declaration under A.6.5. If the available range does not cover that use, establish the missing criterion before claiming the stronger interface. E.24.UK:4.2c separately retains the public U-kind questions. A card field or tuple position acquires none of this declaration meaning by its label alone.

The separately needed `EpistemeEmpiricalGroundingRelationSignature` and `EpistemeEditionRelationSignature` remain declarations over the governed episteme and holon kinds stated in :4.3 and :4.5. Each declaration is first a C.2.1 episteme: its own claim content declares the relation, its EntityOfConcern is that direct relation kind, and its effective scheme gives those declarations meaning. The A.6.0 predicate judges that same individual's `U.Signature` membership; `RelationSignature` is its relation-facing use, with no second identity.

A complete declaration states its relation-kind designator, the SlotSpecs required by its typed use, direct predicate, occurrence identity, applicability, and any actual dependencies or provided names. A manifest may expose those dependencies or names when a consumer needs them. A readable one-off assertion needs neither a signature nor a manifest; assertion wording does not make its relation obtain.

##### C.2.1:4.2.2 - Obtaining and occurrence identity

`EpistemeConstitutionRelation` obtains exactly when the effective reference scheme supplies a coherent designation and interpretation of the claim graph as claims about the exact EntityOfConcern, and the three participants are constitutively organized as one claim-bearing whole whose claims can in principle be evaluated under that scheme. Merely placing three designations in a card does not make the relation obtain.

The relation occurrence is participant-determined by the exact `<ClaimGraph, EntityOfConcern, ReferenceScheme>` triple. The same triple cannot constitute two distinct `U.Episteme` instances under the shared C.2.1 identity rule. Recognition of that individual as a dependent episteme kind adds a membership judgment under the dependent kind's subject pattern, not another constitution occurrence or discriminator. A tuple may represent the triple, but tuple order and storage keys contribute nothing to identity.

The episteme and the relation occurrence are not identical. The relation is the obtaining organization among the three participants. The episteme is the knowledge holon constructively identified through that organization and its whole-level claim-bearing characteristic.

##### C.2.1:4.2.3 - Ordinary assertion, classification assertion, and explicit occurrence use

An ordinary assertion can state that claim content concerns an entity under a scheme without explicitly naming a relation occurrence. For every direct predicate, keep four jobs separate: the direct pattern defines participant meanings, the obtaining predicate, applicability, and the occurrence-identity rule; the current case supplies the facts that satisfy or fail that predicate; the assertion carries affirmative or negative polarity; and a separately governed evaluation or evidence-use relation states supported, refuted, or unresolved reliance when the receiving use needs it. When a receiving relation or claim needs the exact constitution occurrence, inspect the current ClaimGraph, EntityOfConcern, and ReferenceScheme facts against C.2.1's predicate. Only after those facts satisfy the predicate may the participant-determined identity rule individuate the occurrence for designation. The assertion, designation, occurrence, case facts, and reliance judgment remain different objects.

Each classification judgment has one pattern governing its criterion. `A.1` governs constructive recognition of a candidate as an instance of an already admitted holon kind. `C.3.2` governs a local-kind membership judgment. `E.24.UK` governs the ontology-level decision that admits a public U-kind; it does not classify a project candidate. None of these judgments is a direct admission relation created by C.2.1.

When project work needs a classification judgment as a separately reviewable claim, identify one claim-bearing episteme whose exact EntityOfConcern is the candidate entity. For an admitted holon kind, its claim content states affirmative or negative polarity for the exact classification predicate, names the kind, cites the `A.1` constructive criterion and any kind-specific criterion, designates the direct part-relation occurrences used in the assessment, and cites any evidence-use relations that make supported, refuted, or unresolved reliance inspectable for the declared use. For a local kind, its claim content states the same polarity distinction for the candidate, local kind, selected `KindSignature` edition, context slice, and judgment governed by `C.3.2`; its reliance posture remains separate. A value classification inside another claim can remain claim content of that episteme instead of fabricating a value-shaped EntityOfConcern.

The assertion does not create the candidate, admit a U-kind, or make the candidate change kind when an FPF host is renamed or republished. For example, the assertion that Pump #37 satisfies the constructive `U.System` criterion may be revised when evidence changes, while Pump #37 and the criterion it satisfies retain their independently governed identities.

A card that calls a listed collection a holon is still only a classification assertion episteme. Its assertion polarity is affirmative, but the card alone leaves reliance unresolved for any use that requires `A.1` to recover the exact constituents and grounded part relations, their constructive assembly, the whole's reidentification rule, actual compatibility with a governed larger-assembly construction, a composition-grounded whole-level characteristic, and the already admitted holon kind with its kind-specific criterion. The card form supplies none of those facts and does not make the classification predicate true.

The same constitution rule applies when a reader proposes to use an obtaining F.9 Bridge. Say first in ordinary words what the reader proposes to compare, substitute, translate, publish, or otherwise do; name the direction `d`, use-specific correspondence rule `r`, tolerated semantic loss `t`, and affirmative or negative polarity for named use `u`. Identify that statement as one ordinary C.2.1 assertion episteme: the exact Bridge `b` is its EntityOfConcern, its ClaimGraph designates `<u,d,r,t>` and polarity, and its effective ReferenceScheme makes those designations, the rule, and the tolerance interpretable. The exact `<ClaimGraph, b, effective ReferenceScheme>` triple identifies the assertion. Changing `u`, `d`, `r`, `t`, or polarity changes the claim content and therefore the assertion episteme, not fixed Bridge `b`. Keep this local claim form in ordinary wording: it introduces no public U-kind, universal use relation, or durable CamelCase claim name. Reopen F.18 only if an independent later use actually needs a reusable name.

An affirmative bounded-use assertion is one premise for that use; it is neither permission nor proof that the use occurred. A negative assertion leaves an otherwise obtaining Bridge in place. Use A.10 to classify ordinary bounded reliance on the exact evidence-provenance path: `pass` supports only the named use, `degrade` supports only its named narrower use, and another disposition supplies no support for the attempted use.

Use B.3 only when an actual named assurance claim about this bounded use is current. That assurance result remains separate from the Bridge-use assertion and adds assessment Work, System, Method, assignment, bindings, witnesses, or a reusable note only when the assurance use depends on those identities. A direct domain rule may require an assurance claim for a consequential use, but neither consequence nor a display creates the claim. Neither the A.10 nor B.3 branch authorizes the use. If the use actually happened, recover the actual Work under A.15.1, assertion episteme under C.2.1, publication occurrence under E.17, direct relation under its domain predicate, operation application under A.6.1, or another result under its own pattern.

##### C.2.1:4.2.4 - State rule-content and subject assertions

In ordinary prose, cite the PatternID and state the concrete contribution: what the cited content defines, constrains, tests, distinguishes, or helps the practitioner do. This readable branch is normally sufficient. For example, “use A.1 to test constructive holon recognition” states the needed contribution.

Open an exact defining or constraining episteme edition or ClaimGraph only when its identity changes interpretation, migration, conflict analysis, publication, dependency repair, or reuse. Then identify the subject, predicate or constraint, polarity, exact defining content, case facts, and only the scope, time, scheme, or bounded-use qualifications that change the assertion. Do not fabricate an assertion episteme merely to avoid an ordinary pattern citation.

Definition or constraint is not actual rule-content use. State `derivedUsingRuleContent(dependentContent, baseContent)` only when one identified derivation claim used the exact nonempty base subgraph as a formal premise under a declared inference rule. State `evaluatedAgainstRuleContent(dependentContent, baseContent)` only when one identified criterion-selection claim selected that base for one exact bounded evaluation. Consultation, influence, quotation, provenance, evidence, evaluation Work, and later sufficiency establish neither predicate.

An E.4.PFR row is optional and opens only for a named framework-maintenance, edition-impact, comparison, publication/dependency-repair, or refresh receiver. It represents an already identified assertion; it creates neither the assertion nor a pattern-owner fact.

##### C.2.1:4.2.5 - Address one claim inside an exact episteme edition

`U.EpistemeRef` is the admitted RefKind for designating one already identified `U.Episteme`. Under the effective reference scheme of the receiving assertion or description, its resolution method returns exactly one episteme satisfying the C.2.1 identity rule. A value that resolves to none or more than one is unresolved. The reference, its token or serialization, the resolution act, and the episteme remain different objects. Retargeting the reference designates another already identified episteme; it does not revise either episteme.

Use the reusable C.2.1 value `ClaimAddress` only when a receiving claim or work item needs one exact claim inside a larger ClaimGraph:

```text
C.2.1 ClaimAddress ::= <
  exactEpistemeEditionRef: U.EpistemeRef,
  intrinsicClaimIdentity: identity declared by that exact ClaimGraph
>
```

The second component is not a printed node label interpreted by the episteme's general ReferenceScheme. It is a claim identity that the exact ClaimGraph itself declares and preserves across its admissible representations. Resolve the edition first, then require that its ClaimGraph contains exactly one claim with that intrinsic identity. Resolution fails when the edition is unresolved, the identity is absent or non-unique, or the token belongs only to one rendering or serialization.

Two ClaimAddress values are equal only when they resolve the same exact episteme edition and the same intrinsic claim identity in that edition. Reusing the same visible token in another edition does not preserve the address. An `EpistemeEditionRelation` also does not preserve it by itself; a receiving migration rule must state any claim-to-claim correspondence it uses.

When a ClaimGraph declares no stable intrinsic identity for the needed claim, cite the whole episteme or constitute the claim as its own C.2.1 episteme. Do not invent an address from a heading, row number, file location, or display token.

`C.2.1 ClaimAddress` designates claim content carried by the exact edition. It is neither a U-kind nor a RefKind, turns no claim content into a `U.Entity` or another `U.Episteme`, and carries none of the claim content itself. Use `U.EpistemeRef` for the whole episteme and the admitted reference kind for an independently identified entity or relation occurrence.

##### C.2.1:4.2.6 - Resolve a constituent designation to its exact value

Use a constituent designation when the receiving work needs to recover content or rules from an addressable episteme instead of carrying them by value. Ordinary writing can continue with the expressions and rules available in :4.1.1; it need not create a reference or a finished episteme merely to fit these forms.

```text
C.2.1 ClaimContentDesignation ::= <
  exactEpistemeEditionRef: U.EpistemeRef,
  selection: wholeClaimContent | intrinsic semantic selection declared by that ClaimGraph
>

C.2.1 SchemeDesignation ::= <
  exactEpistemeEditionRef: U.EpistemeRef,
  selection: effectiveScheme | schemeDefinedBy(intrinsic semantic selection)
>
```

Resolve the exact episteme first under :4.2.5. For `ClaimContentDesignation`, recover its whole claim content or the uniquely declared selection, retaining the selected claims' semantic qualifications and selected interclaim relations. A single intrinsic claim can use a :4.2.5 ClaimAddress as the selection. A subgraph selection must likewise be declared by the exact ClaimGraph and resolve uniquely across its admissible representations. A row number, heading or diagram position alone supplies no such identity. When that selection is unavailable, carry the exact content by value, cite the whole episteme, or constitute the needed content as its own episteme.

For `SchemeDesignation`, `effectiveScheme` selects the rules governing the source episteme itself. `schemeDefinedBy` selects content that defines one exact rule collection, with its domain and semantic dependencies; interpret that defining content under the source episteme's own effective scheme. A document can describe a different scheme from the one under which the document is read. A mention, name or example of a scheme is insufficient to select all of its rules. Follow an imported rule only through its exact source and interpretation; an unresolved or circular definition with no independently recoverable rules does not resolve the scheme.

Resolution succeeds only when the exact edition, selection and interpretation determine one value. Preserve an unresolved result when the source is absent, selection is ambiguous or a required rule is missing; do not silently choose the latest edition or a nearby document. The receiving interface then checks its declared range and use conditions under :4.1.2. Resolution alone establishes neither membership nor successful use.

These are composite designation values, not new U-kinds or RefKinds. Use an explicit designation field, such as `claimContentDesignation` or `schemeDesignation`, with the applicable C.2.1 form; an A.6.1 `ByRef` argument can specify this resolution method while keeping the resolved value as its argument range. The admitted `U.EpistemeRef` inside the form retains its own referent range. Two designations are the same designation only when they select the same constituent through the same exact episteme edition and selection. Different designations can resolve the same semantic value. Retargeting changes the designation and requires resolution again; it changes neither the old episteme nor the old value.

**Apply the distinctions together.** A declaration D describes a rule set S in ordinary mathematical prose, while S declares a propositional language with material implication and the inference rule that permits `q` from `p` and `p => q`. Selecting D's `effectiveScheme` returns the rules for reading D; selecting the exact content that defines S returns S. A formatting-only stylesheet is an identified rule collection but fails `EpistemeInterpretationScheme` membership. An exact partial S can pass membership and still leave `unless` uninterpreted in a proposed input; a consuming operation requiring that interpretation stops.

For an A.1.1 comparison, let R be the complete S and let M and E have the same effective S. Here the actual participant R is S, the abstract rule collection described by D. R passes the declared range; the coherence claim still requires its independently admitted predicate P to hold for the exact M and E content. Changing the interpretation of `=>` while retaining the signs yields another R and requires a new coherence judgment, including the bridged branch if its conditions now apply. Reprinting D while preserving its complete defining content changes no R.

For an A.6.0 basis use, let the exact dependent content be `q` and the selected base be the two claims `p` and `p => q`, under the stated inference rule. Both are `NonemptyClaimContent`. The base can be sufficient for deriving `q`, but R7 actual use additionally needs the identified derivation claim that used those premises. Replacing the base with the single claim `p` preserves membership and loses that sufficiency under the stated rule. Adding an asserted new reason to the dependent account changes its content even if the field still displays `q`. Two exact editions that designate the same unchanged base under S provide two source qualifications of that semantic base, not two bases merely because the addresses differ. An episteme asserting that this two-claim base is sufficient for deriving `q` under S can take that exact abstract content entity as its EntityOfConcern. That assertion has its own claim content and effective scheme; it does not replace the base it concerns.

#### C.2.1:4.3 - Add empirical grounding through its own relation
**Tech name:** `EpistemeEmpiricalGroundingRelation`.

**Plain reading:** these designated empirical claims of this episteme are inspectable through exact observation, intervention, measurement, or test relations involving this grounding holon.

C.2.1 uses **explicitly designated partial coverage**. For one candidate grounding occurrence, select one exact claim subgraph `C` from the episteme's already constitutive ClaimGraph. `C` may include formal claims but must contain at least one empirical claim. The occurrence says that every empirical claim in `C` is grounded; it says nothing about empirical claims outside `C`. To claim full empirical grounding for the episteme, `C` must contain every empirical claim in that episteme. Purely formal epistemes or selected claim subgraphs fall outside this relation's applicability; their formal derivation and any assurance remain under their applicable rules.

For every empirical claim in `C`, state a concrete claim-to-world mapping under the episteme's effective ReferenceScheme to independently governed direct observation, intervention, measurement, or test relation occurrences involving the exact grounding holon. The mapping names what observation, intervention outcome, measured characteristic, or test result bears on that claim. One measurement involving the same holon cannot ground an unrelated claim.

The selected claim subgraph is by-value predicate content drawn from the episteme's ClaimGraph; it is not a third world-side relation participant, another episteme constituent, or a new U-kind. An assertion about grounding designates that subgraph and the claim-to-world mappings but creates none of the mapped occurrences.

Applying the declaration rule in 4.2.1, `EpistemeEmpiricalGroundingRelationSignature` is one declaration episteme whose exact EntityOfConcern is `EpistemeEmpiricalGroundingRelation`; the same individual has `U.Signature` membership and relation-facing `RelationSignature` use only under `A.6.0`. Its complete declaration includes the covered-claim-subgraph rule, obtaining predicate, maximal-continuous-interval identity rule, applicability, actual dependencies and provided names, and these participant SlotSpecs:

| SlotKind | Relation-participant meaning | ValueKind | refMode |
| --- | --- | --- | --- |
| `GroundedEpistemeSlot` | episteme containing the exact covered claim subgraph | `U.Episteme` | `U.EpistemeRef` |
| `GroundingHolonSlot` | exact holon involved in the mapped observation, intervention, measurement, or test relations | `U.Holon` | `U.HolonRef` |

`EpistemeEmpiricalGroundingRelation` over participants `(E,H)`, with `covered=C`, obtains exactly while exact covered claim subgraph `C` contains at least one empirical claim and every empirical claim in `C` has a current claim-to-world mapping to the required independently governed direct observation, intervention, measurement, or test relation structure involving `H` under E's effective ReferenceScheme. Every mapped relation required by that coverage must obtain. An exact direct evaluation relation counts as part of the empirical test only when the mapping states its concrete use in that test; otherwise evaluation and evidence can support or challenge an assertion about grounding but are not its world-side base.

One occurrence is identified by `<episteme, exact covered claim subgraph, grounding holon, maximal continuous interval during which the complete coverage predicate is true>`. Closing the open end of that interval refines the description of the same occurrence. Demonstrated failure of any required mapping followed by restored complete coverage yields another occurrence. Evidence or evaluation availability alone establishes neither obtaining nor nonobtaining and proves no temporal gap. If the complete coverage predicate is known to obtain, grounding continues without a stored report or work log. If it is known not to obtain, the relation does not obtain. If its truth is unknown, an affirmative grounding assertion has unresolved reliance for the declared use; that posture is not a third world-side grounding state.

The grounding holon need not be identical to the EntityOfConcern. One method-description episteme may have one grounding occurrence for a claim subgraph mapped to exact enactment work and another for a different claim subgraph mapped to the system whose behavior was observed. Each occurrence names its own `C`, `H`, and mappings. Sharing one grounding holon makes comparison inspectable but proves neither the same subject, the same claim content, nor coverage of any unlisted claim.

#### C.2.1:4.4 - Keep neighboring uses under their direct relations

| Current distinction | Relation or object to use | Why it stays outside the core constitution relation |
| --- | --- | --- |
| classification judgment or assertion needed as a separate claim-bearing object | the `A.1` recognition judgment for an admitted holon kind or the `C.3.2` membership judgment for a local kind; one C.2.1 episteme when a receiving review treats the judgment as a separate claim-bearing object | the governing criterion states the membership condition; the classification judgment evaluates the candidate under it; the assertion carries that judgment but neither creates the candidate nor admits the kind |
| claim scope | exact `U.ClaimScope` and its A.2.6 membership semantics | scope delimits where claims hold; it does not identify every episteme |
| concern-bearing viewpoint use | one exact `U.Viewpoint` episteme P selected for one named describing use | selection states the concern under which the description is used; it neither establishes conformance nor enters episteme identity |
| view | the same episteme individual recognized as `U.View` when an exact `EpistemeViewpointConformanceRelation` to at least one exact viewpoint episteme obtains | conformance, source-to-receiving construction, current-use selection, publication, form, and carrier remain different relations or objects |
| bounded model use | optional relation to one `BoundedModelUseStructure : U.Structure` under A.1.1 | model-use organization can qualify interpretation without becoming a universal identity component |
| justification structure | exact `JustificationGraph` content | a justification structure organizes inferential dependencies without becoming claim content |
| evidence use or assurance for a claim | for ordinary bounded reliance, the descriptive A.10 evidence-provenance path, the independently established direct relations it cites, and local `RelianceDisposition`; when an actual named assurance claim is current, the exact B.3 `AssuranceResult` or its non-positive disposition | evidence and assurance can support, narrow, or stop reliance on the claim while the episteme's identity remains fixed |
| publication | exact publication occurrence and publication form under E.17 and E.24.PUB | making an edition available does not constitute or reidentify it |
| presentation carrier | any exact `U.PresentationCarrier` under E.17 and E.24.PUB | bearing a publication form or rendered expression does not constitute or reidentify the episteme |
| representation and admissible operations | the representation scheme, selected elements and operations used for the represented episteme, with any required correspondence or transition governed through :4.0 | a change of scheme or admitted operations can change the available work |

Names ending in `Slot` are admissible here only as SlotKinds inside the exact `RelationSignature` governed by the neighboring direct relation pattern. A card or other episteme form carries participant designations in ordinary fields; it does not acquire SlotKinds by using similar field labels. None of those neighboring SlotSpecs belongs to `EpistemeConstitutionRelationSignature`.

#### C.2.1:4.5 - Relate distinct episteme editions explicitly

**Tech name:** `EpistemeEditionRelation`.

**Plain reading:** this later episteme continues this earlier episteme as an edition under one applicable continuity rule.

`EpistemeEditionRelation` has exactly two direct participants. Applying the declaration rule in 4.2.1, `EpistemeEditionRelationSignature` is one declaration episteme whose exact EntityOfConcern is `EpistemeEditionRelation`; the same individual has `U.Signature` membership and relation-facing `RelationSignature` use only under `A.6.0`. Its complete declaration includes the direct predicate, participant-determined identity, applicability, actual dependencies and provided names, and these SlotSpecs:

| SlotKind | Relation-participant meaning | ValueKind | refMode |
| --- | --- | --- | --- |
| `EarlierEpistemeSlot` | exact episteme continued by the later edition | `U.Episteme` | `U.EpistemeRef` |
| `LaterEpistemeSlot` | exact episteme that continues the earlier edition | `U.Episteme` | `U.EpistemeRef` |

The relation obtains only when all of these conditions hold:

1. the two epistemes have different C.2.1 identities;
2. the later episteme actually uses the earlier episteme as the source for the claimed revision, refinement, or supersession;
3. one applicable edition-continuity policy or rule states which claim, EntityOfConcern, and effective-reference-scheme features must be preserved, which may deliberately change, and what counts as continuation for this episteme family;
4. the exact preserved and deliberately changed features satisfy that rule;
5. no failure condition in that rule classifies the case as a fork, translation, retargeting, or independent reconstruction instead.

Work, an enacted Method, provenance, and change results supply case facts. Their labels do not make continuity true. C.2.P may recover the source expression and source-to-revision use; the direct change patterns supply exact changed features. If the continuity claim separately consumes a first-existence fact, apply the shared boundary in 4.9. A missing required rule or fact blocks only that positive edition claim.

One occurrence is identified by the exact `<earlier episteme, later episteme>` pair. Two revision Work occurrences do not create two edition occurrences for the same pair. The relation is acyclic in its earlier-to-later direction. A renamed file, later publication, shared title, bare provenance edge, or Method named “revision” establishes no occurrence.

Several edition occurrences form a lineage structure only when a receiving use depends on their organization. A separately identified edition collection remains under A.14; collection membership does not establish continuity. `PhaseOf` may describe one unchanged episteme over a proper interval but does not connect two different C.2.1 identities.

When claim content, EntityOfConcern, or effective reference scheme changes, the later object is another episteme. Apply `A.6.4` separately when the current claim is effect-free retargeting between epistemes with different EntitiesOfConcern; retargeting alone does not establish edition continuity. A changed publication form alone identifies neither another episteme nor an edition relation.

#### C.2.1:4.6 - Keep descriptions, cards, publications, and representations downstream
A claim-bearing filled card can itself be an episteme when its claim content, EntityOfConcern, and effective reference scheme are recoverable. The reusable arrangement of that card can instead be a publication form, and a selected graphical or tabular element can participate in a C.29 representation. Identify each object through its own constitution and the direct relation in which it participates; visible shape does not determine its kind.

When a card or other form designates the participants of one direct relation, its field labels may correspond to SlotKinds in that relation's `RelationSignature`, and its field values may be by-value designations or references of the declared refModes. The form is not a filled direct relation occurrence; supplying fields does not make the predicate obtain or provide occurrence identity.

In a relational assertion, the claim graph designates the actual participants and states affirmative or negative polarity for the direct predicate. The direct pattern defines that predicate and the occurrence-identity rule; current case facts determine whether the predicate is satisfied or failed. A forecast, scenario, counterfactual, permission, or another claim family names its exact direct governor rather than using one common catch-all field. Only when an explicit reliance judgment is current for the declared use does `A.10` or the receiving evaluation separately state supported, refuted, or unresolved reliance. An affirmative assertion may designate an occurrence only after the case facts satisfy the predicate and the direct identity rule individuates that occurrence; a negative assertion creates no failed world-side occurrence. In a relation-occurrence description episteme, the EntityOfConcern is that exact already individuated occurrence. The assertion and description retain their own C.2.1 identities. Their forms do not by themselves supply case facts or the occurrence-identity rule, or establish obtaining; evidence supporting the case conclusion and any constitutive contribution are governed separately by the relevant evidence and direct-relation rules.

A designator designates an already recoverable referent. A governed reference resolves to that referent under an effective reference scheme.

For publication, `E.17` and `E.24.PUB` govern the occurrence that makes a selected edition available to a declared audience for a bounded use, the form that expresses it, and the `U.PresentationCarrier` that bears the form. Plain **published episteme** names the episteme's contingent participation in that occurrence. Its C.2.1 identity stays fixed before, during and after that availability relation.


One completed inspection card shows why the distinctions matter. Its filled claims can identify one episteme; its reusable layout can be a publication form; its paper sheet or file can be a presentation carrier; and a publication occurrence can make the selected card episteme edition available to the maintenance team. None of those uses makes the others identical.

Republishing the same claims about the same subject under the same effective scheme with another form or carrier preserves the episteme. Changed claim content, subject or effective scheme identifies another episteme. If the account also needs the rendering Work, use the conditional Work branch in :4.0.

A tuple can represent the identity triple and a graph or hypergraph can represent claim, justification, dependency, or relation structure. Use `C.29` for an unresolved mathematical-lens choice, transfer or reliance question. `ClaimGraph` names the semantic content being represented; `JustificationGraph` names the separately governed inferential organization. Nodes and edges in a selected graph remain representation elements. An explicit correspondence can relate one selected representation element to an independently recovered object, but it neither identifies the two nor makes the representation element a participant of the represented direct relation.

#### C.2.1:4.7 - Preserve description and meta-description recursion

If episteme `E1` describes pump `P`, `P` is the EntityOfConcern participant in the constitution relation that identifies `E1`. If review episteme `E2` describes `E1`, then `E1` is the EntityOfConcern participant for `E2`. The two relations have different triples and therefore identify different epistemes.

An episteme may describe itself when its own identity remains recoverable. Self-reference never closes an assurance argument by itself. Each justification or evaluation path terminates in independently governed evidence, observation, or formal derivation rather than in a cycle of claims that cite one another.

Description and specification use remain distinct. A Description episteme is admitted for specification use only when the E.10.D2 conditions are satisfied: checkable claims and a named harness or validation relation. If the relying use selects a viewpoint, name that describing use and preserve or update its exact selection only when the selection affects reliance. Formal notation alone does not grant specification use or change the episteme's kind.

#### C.2.1:4.8 - Locate the change before updating episteme identity

| Observed change | Disposition |
| --- | --- |
| claim content, EntityOfConcern, or effective reference scheme changes | identify another episteme; use `EpistemeEditionRelation` only for revision, refinement, or supersession when its historical-continuation predicate obtains, and use `A.6.4` separately only for an exact retargeting that satisfies its own predicate; otherwise stop at the new identity without inferring continuity |
| the explicit empirical-claim coverage predicate begins to obtain, ceases to obtain, or is restored | evaluate `EpistemeEmpiricalGroundingRelation` continuity for the exact covered claim subgraph and grounding holon; do not change episteme identity unless a core discriminator also changed |
| an evidence item, evaluation report, evidence store, or work log becomes available or unavailable without an established change in the complete claim-coverage predicate | revise only the separately governed support, warrant, confidence, evidence-use relation, or receiving-use reliance posture that changed; the mapped direct relations still determine world-side grounding and occurrence continuity: known complete coverage continues, known coverage failure remains nonobtaining, and uncertainty about coverage gives an affirmative grounding assertion unresolved reliance rather than a third world-side state |
| candidate episteme E or viewpoint episteme P changes | identify the changed episteme under C.2.1, then test the new exact E/P pair under `E.17.0`; for fixed E and P, conformance cannot change because of evaluator, evidence, project, publication, or current use, so state any changing adequacy or evaluation as a separate claim |
| one named describing use selects one already identified `U.Viewpoint` episteme P | update only that use's exact viewpoint selection; the selection creates no context object, selects no view, and establishes neither conformance, `U.View` membership, nor episteme identity |
| claim scope changes | update the exact `U.ClaimScope` and its A.2.6 membership semantics; do not infer another episteme automatically |
| selected bounded model-use or multi-view structure changes | update the exact collection or structure relation and re-evaluate affected interpretation claims; do not infer another episteme or view family automatically |
| publication form, carrier, rendering, audience, bounded use, or publication occurrence changes | establish the exact E.24.PUB change only; publication is not view membership or episteme succession |
| mathematical or tool representation changes | use `A.6.3.RT` for a same-EntityOfConcern representation transition, or the applicable direct transition pattern for another transition; use `C.29` only for an unresolved mathematical-lens choice, transfer or reliance question |

#### C.2.1:4.9 - Hand episteme transformations to their subject patterns

**Shared identity-inception boundary.** Work or transformation can explain how an entity came about, but C.2.1 by itself establishes neither when that entity first existed nor that the work caused its inception. Open this boundary only when a current receiving claim asks whether a new entity began. Then use the subject's direct inception rule: its pattern defines the predicate and identity rule, and current case facts must satisfy them. If no such rule is recoverable, return one `missing-governor` blocker naming the entity or candidate basis, available case facts, required inception predicate, and receiving use. When the current question is only changed episteme identity, form, representation, view, or publication, do not open this boundary.

When inception is attributed to Work, apply **A.15.PROD:4.5**. Begin with the subject's exact `productIdentitySpecification` and its named applicability predicate or filled local claim for the candidate basis, subject context, and boundary. Then recover actual Work effects and the declared Work-to-change and change-to-identity bases, locate the earliest satisfying `inceptionBoundary`, and identify exact `identityClosingWork`. Designate the resulting entity only on the after-side of that boundary and retain the exact specification and applicability basis used for the claim. A missing required basis stops the positive claim; missing recoverable Work granularity for `identityClosingWork` returns that section's work-granularity blocker.

A.6.2-A.6.4 define episteme-to-episteme morphing, source-to-receiving viewing construction, and retargeting. Identify every source and receiving episteme independently under C.2.1 before testing the exact transformation relation. Each transformation pattern states which identity discriminator is preserved or changed and names the exact correspondence, reinterpretation, or retargeting relation on which it relies. When a possible Bridge between exact F.17 cells is current, use F.9 to test whether that relation obtains. If the morphism relies on that Bridge for a proposed use, state a separate C.2.1 assertion with the Bridge as EntityOfConcern and `<u,d,r,t>` plus polarity in its ClaimGraph, then use A.10 for ordinary evidence reliance or B.3 only when an actual named assurance claim is current; none of those facts makes the morphism application occur. Categorical function, mapping, or tuple notation creates no direct relation occurrence.

For an A.6.3 source-to-receiving viewing construction, the two identified epistemes may retain the same EntityOfConcern while claim content or effective scheme is restricted. `E.17.0` alone judges whether the receiving episteme conforms to an exact viewpoint and therefore has dependent `U.View` membership. Direct authoring or query generation can yield a candidate episteme without an A.6.3 construction, and neither route creates a multi-view family. For retargeting, the EntityOfConcern changes and the case names the exact domain correspondence, retargeting rule, or relation on which it relies. An F.9 Bridge is additional only when the case separately asserts a semantic relation between exact F.17 local senses from different semantic contexts and the F.9 predicate obtains. For a same-EntityOfConcern representation transition, use A.6.3.RT; the represented episteme may remain unchanged while the representation scheme and admitted operations change.

#### C.2.1:4.10 - Relation and neighboring-object reference

| Current object | FPF kind or relation | Subject pattern |
| --- | --- | --- |
| `U.Episteme` | one knowledge holon with identity `<claim content, EntityOfConcern, effective ReferenceScheme>` | C.2.1 |
| `EpistemeConstitutionRelation` occurrence | the obtaining direct relation among the exact claim graph, exact EntityOfConcern, and effective reference scheme that constructively identifies one episteme | C.2.1 and `A.6.REL` |
| `EpistemeEmpiricalGroundingRelation` occurrence | the direct relation between one identified episteme and one exact grounding holon for one exact covered claim subgraph containing at least one empirical claim, while every empirical claim in that subgraph has a current mapping to the required observation, intervention, measurement, or test relations involving that holon; evaluation or evidence supports an assertion unless explicitly mapped as part of the empirical test | C.2.1 and the governing observation, intervention, measurement, test, evaluation, or evidence patterns |
| classification assertion episteme needed as a separate claim-bearing object | a claim-bearing episteme whose EntityOfConcern is the exact candidate and whose claim content states a classification judgment under the exact governing criterion: `A.1` for an admitted holon kind or `C.3.2` for a local kind | C.2.1 for assertion identity; the pattern governing the criterion for the judgment; `E.24.UK` only for public U-kind admission |
| `EpistemeEditionRelation` occurrence | the direct historical continuation relation between one exact earlier episteme and one exact later episteme; exact source use, the applicable continuation policy or rule, and the preserved and deliberately changed claim, EntityOfConcern, and scheme features decide whether it obtains; Work, Method, provenance, and change facts supply case facts only; apply the shared 4.9 inception boundary only when that separate fact is consumed | C.2.1, coordinated with `C.2.P`, A.3.1, A.3.4, and C.2.1:4.9 only for a separately current inception claim |
| `EpistemeConstitutionRelationSignature` | the declaration episteme for reusable EntityOfConcern designation under :4.2.1, with `EntityOfConcernSlot`, `U.Entity`, and `U.EntityRef`; typed replacement of claim content or effective scheme needs additional independently governed ranges and SlotSpecs | C.2.1:4.2.1, `A.6.0`, and `A.6.5` |
| `EpistemeEmpiricalGroundingRelationSignature` or `EpistemeEditionRelationSignature` | one C.2.1 declaration episteme whose EntityOfConcern is its direct relation kind; A.6.0 judges same-individual `U.Signature` membership, and `RelationSignature` is its relation-facing use with the complete semantics and SlotSpecs stated in :4.3 or :4.5 | C.2.1 for declaration identity, `A.6.0` for membership and reusable vocabulary, and `A.6.5` for SlotSpecs |
| `SlotSpec` | one declaration-content component of an identified complete `RelationSignature` | `A.6.5` |
| assertion or description episteme | a claim-bearing episteme that states or describes one of the direct relations | C.2.1 and the direct claim or description pattern |
| `U.MethodDescription` | the same `U.Episteme` individual when A.3.2 recognizes one admitted `U.Method` as its exact EntityOfConcern and its claims, interpreted under the effective `ReferenceScheme`, make at least one substantive claim about that method as a way of doing; mention, bibliographic metadata, or approval alone does not establish membership, and adequacy for a receiving use is evaluated separately | C.2.1 for episteme identity; `A.3.2` for dependent-kind membership |
| `U.View` | the same `U.Episteme` individual when it conforms to at least one exact `U.Viewpoint` episteme; formally, when `EpistemeViewpointConformanceRelation(E,P)` obtains for that pair | C.2.1 for episteme identity; `E.17.0` for dependent-kind membership; `A.6.3` only when source-to-receiving construction is current. Conformance of E to P, that construction, current-use selection, and publication remain separate. |
| describing-use viewpoint selection | one named describing use selects one already identified `U.Viewpoint` episteme through an exact reference; it selects no view | `E.10.D2` and `E.17.0` |
| multi-view collection or organization | an exact C.13 collection only when a receiving use depends on the plurality as a collection, and an exact A.22 `U.Structure` only when that use additionally depends on organization among those views | `C.13`, `A.22`, and the direct organizing relations |
| cross-view correspondence, consistency, realization, trace, or change-impact claim | one exact direct subject relation under its own governor; a C.2.1 episteme may assert or describe it, but a heading, edge, carrier, or E.17 publication invents no relation | the exact direct relation pattern; when none is current, return an exact missing-relation blocker naming the participants, required predicate and use, and missing governor |
| publication occurrence | the occurrence that makes one selected episteme edition available to a declared audience for a declared bounded use | `E.17` and `E.24.PUB` |
| publication form | the arrangement, notation, or rendering convention that expresses the selected episteme edition for that publication use | `E.17` and `E.24.PUB` |
| `U.PresentationCarrier` | the exact physical or digital carrier that bears the publication form | `E.17` and `E.24.PUB` |
| mathematical representation | a mathematical representation used for the stated modeling or reasoning purpose | the applicable mathematical or representation pattern; `C.29` only for an unresolved mathematical-lens question |

This reference table keeps the neighboring objects and relations visible after the application method. Ordinary prose names only the current object and its direct relation. A sentence such as “Model M concerns Pump P under Scheme S” is sufficient until another use needs explicit empirical grounding, a classification assertion, occurrence identity, edition continuity, publication, or representation correspondence.

### C.2.1:5 - Semantic triangle as a didactic projection  *(informative)*

The Symbol-Concept-Object triangle is a teaching projection, not the episteme ontology.

| Triangle corner | C.2.1 projection | What the projection suppresses |
| --- | --- | --- |
| Symbol | selected representation elements and any publication carrier | representation scheme, admitted operations, publication occurrence, and correspondence to the episteme |
| Concept | `ClaimGraph` interpreted under an effective `ReferenceScheme` | claim scope, justification, viewpoint, and edition relations |
| Object | exact EntityOfConcern and any current `EpistemeEmpiricalGroundingRelation` | the difference between what claims concern and the holon through which they are empirically inspectable |

A triangle diagram may be used to introduce expression, meaning, and subject if its caption says that it compresses the C.2.1 episteme ontology. Its corners and arrows are representation elements. They supply no SlotKinds, direct relation occurrences, or identity rules.

This limitation matters in practice. A proof-assistant term, wiring diagram, clinical chart, learned embedding, or verbal explanation can all occupy the Symbol corner while supporting different operations and different losses. Those questions belong to the representation-scheme and transition patterns; one geometric picture does not answer them.

### C.2.1:6 - Description and specification-use boundary  *(normative)*

A Description episteme is a `U.Episteme` whose exact EntityOfConcern is the entity being described. Description does not create a second kind beside ordinary epistemes; it names the current relation and use of one episteme.

For a description use, keep these values recoverable:

| Value | Meaning | Identity status |
| --- | --- | --- |
| `entityOfConcernRef` | designation of the exact EntityOfConcern in the description episteme's constitution relation | its resolved exact EntityOfConcern, not the reference value or designation, is C.2.1 identity-bearing |
| effective `ReferenceScheme` | rules by which the description claims refer to and can be checked against that entity | C.2.1 identity-bearing |
| `viewpointRef`, when current | governed reference resolving to the exact `U.Viewpoint` episteme selected for this describing use under E.17.0 | use qualifier outside episteme identity; work that changes an identity discriminator identifies another episteme independently |
| `claimScopeRef`, when current | designation of the exact `U.ClaimScope` under A.2.6 | claim-use qualifier |
| `modelUseStructureRef`, when current | designation of one independently selected `BoundedModelUseStructure : U.Structure` | optional interpretation qualifier, not a context root |


Use `E.10.D2` to keep the EntityOfConcern, its Description episteme, and specification use distinct. A Description episteme is admitted for specification use only when its claims are checkable and a named harness or validation relation can test them. Preserve or update a selected viewpoint only for the named describing use whose reliance depends on it. The suffix `Spec`, formal notation, approval appearance, or publication in a repository does not grant that use.

Self-description uses the same rule. If an episteme describes itself, its EntityOfConcern designation resolves to that episteme. If a review episteme describes it, the review episteme has the first episteme as EntityOfConcern and its own claim content and reference scheme.

### C.2.1:7 - Episteme morphing, viewing, and retargeting  *(normative)*

C.2.1 governs episteme identity discriminators and neighboring relations. A.6.2-A.6.4 govern transformations between epistemes.

#### C.2.1:7.1 - Effect-free episteme morphing

For a morphism from episteme `X` to episteme `Y`, state by value:

1. which of claim content, EntityOfConcern, and effective reference scheme are preserved, restricted, bridged, or changed;
2. which exact viewpoint selection the use names, which exact empirical-grounding, claim-scope, model-use, evidence, or representation occurrences the arrow rule reads, and which endpoint facts it compares; the arrow changes none of those occurrences and makes none obtain or cease;
3. which claims in `Y` are preserved from or supported by `X` under the named morphism, the exact correspondence or retargeting relation governed by that morphism pattern, and any `F.9` Bridge that governs cross-context sense use when current;
4. whether a separate operation application or Work actually produced or changed an episteme, and which direct pattern governs that occurrence.

The morphism declaration and its mathematical arrows are different objects. The declaration is a C.2.1 episteme, normally an A.6.0 FormalSubstrate signature, whose EntityOfConcern is the local mathematical family and whose claim content declares vocabulary, laws, and applicability. One arrow `f : X -> Y` is a local mathematical object identified inside that substrate by its exact endpoints, arrow rule or designator, and declared formal equivalence.

The mathematical statement `f : X -> Y` names no execution. When an exact operation application is current, A.6.1 separately identifies its argument and result bindings. For any precise performed-Work claim, use A.13 to identify the actual performer and A.15.1 to admit the dated Work independently. If that claim must also identify the assignment under which the Work was performed, check that relation separately through F.6. Identify the affected or newly constituted episteme, its C.2.1 discriminators, and any production or change relation under their direct governors. The same arrow may be used in several applications, and an arrow may relate already existing epistemes. No bare result, generic Work result, or universal production relation follows from an arrow or declaration.

A claim that one arrow is suitable for one exact use is another C.2.1 assertion. Its complete claim content names the arrow, use, conditions, and polarity. Evidence and reliance qualify that assertion; they do not identify the arrow or operation application.

#### C.2.1:7.2 - Epistemic viewing

`A.6.3` governs an exact source-to-receiving viewing construction when one separately identified receiving episteme is constructed from one separately identified source episteme. That construction may preserve the exact EntityOfConcern while restricting claim content or specializing the effective reference scheme. It neither grants `U.View` membership nor performs work. Direct authoring and query generation can identify receiving epistemes without this construction relation.

`E.17.0` independently asks whether one fixed receiving episteme E conforms to one fixed viewpoint episteme P; formally, whether `EpistemeViewpointConformanceRelation(E,P)` obtains. Only an obtaining relation gives the same E dependent `U.View` membership. A system may perform viewing, query, authoring, or rendering work, but neither that work nor an A.6.1 result position grants `U.View` membership or supplies C.2.1 identity.

Empirical grounding continues only while every mapped direct relation required by the receiving episteme's exact covered claim subgraph obtains. Changing publication, current use, evaluator, or evidence alone changes neither the conformance of fixed E to fixed P nor grounding. Several source or receiving epistemes do not automatically form a multi-view family; identify any current collection under C.13 and any selected organization under A.22.

#### C.2.1:7.3 - Epistemic retargeting

`A.6.4` governs a local class of effect-free arrows `r : X -> Y` whose exact endpoint epistemes concern different exact entities. It does not admit a durable `U.EpistemicRetargeting` kind. The A.6.0 FormalSubstrate signature that declares the class, one arrow r, a bounded-use assertion q, a current-case judgement, and any actual operation application remain different objects.

For one receiving use, q states one proposition with affirmative or negative polarity: whether r preserves the named invariant and makes the stated loss acceptable under named conditions. A separate current-case judgement compares exact current facts with that proposition and reports `satisfies`, `fails`, or `cannot decide`. The same r can have different q assertions and case results for different uses without changing arrow identity. A missing deciding fact yields `cannot decide`, names that fact, and states what would reopen the question; it does not create unresolved assertion polarity or require an assurance record.

Use A.20 only when the proposition is an internal constraint, A.10 only when an evidence-use claim is current, and B.3 only when an actual named assurance claim is current. Otherwise the named predicate and direct facts supply the case judgement. If the case also asserts a semantic relation between exact F.17 local senses, F.9 defines that separate Bridge and its bounded-use claim.

A system may perform exact retargeting work. Identify its enacted method, any exact A.6.1 operation application and binding, affected or newly constituted episteme, and actual change facts separately. The arrow itself performs no work, and the mathematical statement `r : X -> Y` infers no bare result or universal production relation.

Examples include retargeting from an episteme about a physical cabinet to one about a selected functional `U.Structure`, or from observations to a learned model, when the independently identified source and receiving entities really differ. For `Cab-7` as the cabinet and `Route-A` as the selected functional structure, an independently stated behaviour-test result can supply q's current-case basis; the judgement is `satisfies` only when that result meets q's named conditions. The source expression `Realises(Cab-7, Route-A)` has no current direct relation governor here and therefore stops at A.6.RCD `missing-governor`; it contributes nothing to that judgement. For a Fourier representation change, identify the endpoint subjects under C.2.1. If the same signal remains the EntityOfConcern, use A.6.3.RT or the applicable representation-transition pattern. Use C.29 when a mathematical-lens choice, transfer or reliance question remains.

### C.2.1:8 - Multi-view description and publication  *(normative)*

C.2.1 identifies each candidate episteme E and each viewpoint episteme P separately. `E.17.0` then asks whether E conforms to P; its formal name for that relation is `EpistemeViewpointConformanceRelation(E,P)`. Only when the relation obtains is the same E a `U.View` under P. For one named describing use, say that the use selects P. Keep E, its EntityOfConcern, the use, and P distinct. Selection changes neither episteme identity nor conformance and does not make E a view. If another receiving use selects an already identified view, name that use and the pattern that defines or constrains it separately.

Several conforming views remain a plurality. Recover an exact C.13 collection only when a receiving use depends on that plurality as a collection. Recover an exact A.22 `U.Structure` only when the use additionally depends on organization among those views, and state the exact direct organizing relations. A shared EntityOfConcern, package, table, heading set, diagram, or carrier creates neither a view family, a collection, nor that structure.

`A.6.3` governs only an obtaining source-to-receiving viewing construction when that history is current; direct authoring and query generation require no such relation. A system performs any viewing, authoring, query, comparison, or repair work. Neither that work route nor an A.6.1 result position grants `U.View` membership or identifies a multi-view family.

`E.17` governs multi-view publication forms and uses, while `E.24.PUB` governs publication occurrences, forms, and carriers. The same recognized view can participate as the selected episteme in several publication occurrences without changing identity or conformance. Publication establishes no view membership and no cross-view subject relation.

When cross-view correspondence, consistency, realization, trace, or change impact matters, name the exact participants and apply the exact direct subject-relation governor. A C.2.1 assertion or description episteme may carry that claim; it does not make the relation obtain. If no direct governor is recoverable, return an exact missing-relation blocker naming the participants, required predicate and use, and missing governor; do not invent a relation. `E.17`, a matching heading, graph edge, diagram position, or shared carrier invents no correspondence relation.

### C.2.1:9 - Archetypal Grounding — Worked Cases

These cases ground the pattern in practice; only a case that names an obtaining `EpistemeEmpiricalGroundingRelation` asserts empirical grounding.

#### C.2.1:9.1 - Physical engineering

A pump-maintenance specification has a claim graph about exact pump `P` under a reference scheme that resolves part names, states, units, and measurement procedures. Those three participants identify the episteme. For test bench `B`, exact covered claim subgraph `C_B` contains the discharge-pressure-tolerance and leakage claims. Its claim-to-world mapping names the direct pressure-measurement and leakage-inspection relations involving `B`; a maintenance-interval claim outside `C_B` is not grounded by those measurements. The grounding relation over `(E,B)`, with `covered=C_B`, continues for the maximal interval during which every required mapping obtains. If that coverage continues while an evidence archive or inspection-work log becomes unavailable, only a separately governed support, warrant, confidence, or evidence-use assertion may change. A publication occurrence makes the episteme available through a rendered checklist form borne by an exact carrier. When checklist marks assert particular maintenance or inspection Work, use :4.0's Work branch; assignment attribution is added only when the checklist account requires it. When a receiving use needs a separate assertion that `P` satisfies the constructive `U.System` criterion, identify it as another episteme about `P`; renaming or republishing the governing FPF pattern does not change `P` or create its systemhood.

The classification assertion changes only when its own claim content or reference scheme changes. Pump continuity is judged instead under the `A.1` reidentification rule; a changed or unchanged assertion does not establish that continuity.

#### C.2.1:9.2 - Medicine

A diagnostic model concerns one patient-state entity or one admitted patient cohort under a scheme that defines observations, measurements, and diagnostic interpretations. Each `EpistemeEmpiricalGroundingRelation` identifies the exact covered diagnostic-claim subgraph, grounding holon, mapping to the required current observation, measurement, or test relations, and maximal continuous interval of complete coverage; it grounds no unlisted claim. If a threshold revision changes claim content or the effective reference scheme, that changed discriminator identifies another episteme; moving the unchanged model to another screen changes only the exact publication or representation object that actually changed.

#### C.2.1:9.3 - Competence claims, teaching Work, and learner-facing views

A curriculum model concerns an exact competence structure under a scheme that relates assessment or performance evidence to competence claims. If *taught* or *learned* wording leaves the changed subject or result unclear, use `E.10.LRN` to recover the claim first: receiving an intervention and acquiring a capability call for different evidence.

A learner-facing episteme is a `U.View` when it conforms to an exact learner-facing viewpoint under `E.17.0`. If its construction from the source curriculum model matters to the account, `A.6.3` supplies that viewing relation. Changing the selected competence claims changes the receiving episteme; changing only its display preserves it.

If empirical grounding is needed, name the covered competence claims and their mappings to the relevant assessment or performance relations involving an exact admitted course-cohort or learning-environment holon, as required by :4.3. A later capability, transfer or retention claim uses `A.10` for its bounded reliance on the relevant result. If particular teaching, assessment or construction Work must be asserted, open :4.0's Work branch. The identity-only use finishes with the model's claims, exact subject and effective scheme.

#### C.2.1:9.4 - Episteme about an episteme

Simulation model `M` is one episteme. Review `R` concerns `M`, so the EntityOfConcern in `R` is the episteme `M`, not the physical system modeled by `M`. Claims in either episteme may cite separately governed evidence-use relations concerning the simulated or physical system. Publishing `R` does not revise `M`.

A theory episteme is recognized through its claim-bearing constitution and whole-level inferential characteristics. A textbook publication can make one edition of that theory available, but the publication occurrence, form, and carrier are not constituents of the theory and do not establish its holonhood.

#### C.2.1:9.5 - Edition succession

Episteme `E1` is the exact source used to produce candidate edition `E2`. The applicable continuity policy says that the EntityOfConcern remains the same, specified core claims must remain traceable, listed claims may be corrected, and a translation into another reference scheme counts as a derivative rather than an edition. The current case identifies the preserved core claims, deliberately corrected claims, unchanged EntityOfConcern, and source-to-revision use. Those facts satisfy the policy, so the positive `EpistemeEditionRelation(E1,E2)` assertion is available.

If the same Work instead retargets the claims to another EntityOfConcern, translates them under a rule that the policy classifies as a derivative, or reconstructs similar content without using E1 as source, the edition predicate fails even when the Method is named “revision.” Work, Method, provenance, change facts, evaluation, and evidence remain outside the two-participant relation. Later repackaging or publication establishes neither another episteme nor edition continuity.

#### C.2.1:9.6 - Grounded identity across two observations
A morning-observation episteme concerns an object designated `M`; an evening-observation episteme concerns an object designated `E` under another reference scheme. A.1.RI supplies the Method for deciding whether these observations concern the same continuing object: recover its continuation criterion, construct connections under the subject and observation rules, and compare the alternatives. Carry the identification with its supporting premises; retain ambiguity when the observations leave materially different connections possible.

The two observation epistemes can retain different identities after the object is identified: they can make different time-indexed claims or use different reference schemes. C.2.1:4.2.3 permits the identifying claim in ordinary language. If a later use needs a separately designated relation occurrence, apply A.6.REL with the direct relation pattern's obtaining predicate and occurrence-identity rule. A missing relation definition then blocks that occurrence-dependent use. It does not erase a conditional identification already established under stated premises; an unspecified object-continuation criterion, by contrast, leaves the identification itself unresolved.

**Construct a bounded identifying result.** A.1.RI:5.1 develops the complete two-object case: independent persistent point objects at 0 and 10 cm are observed one second later at 1 and 9 cm, with exact positions in one frame and crossing permitted. With one observation of each object at each end of the interval and a 2 cm/s speed bound, only the association requiring 1 cm per object is admissible. Raising the bound to 10 cm/s also permits the crossed association requiring 9 cm per object. The observation claims retain their different occasions after an identification; the changed premise instead leaves the object correspondence unresolved. The receiving use determines whether a discriminator is worth obtaining.

In [Rodin's astronomical reconstruction](https://philsci-archive.pitt.edu/12116/1/vh.pdf), the connecting trajectory is supplied through theory and observations. In the HoTT reconstruction, MS and ES are represented as terms of a point-object type Pt; `p : MS =_Pt ES` expresses the identifying construction as a term of their identity type.


#### C.2.1:9.7 - Readable wiring diagram as a proxy

Wiring-model episteme `E1` concerns exact harness `H` under reference scheme `S1`, which resolves connector designators, pin identities, and connection predicates. If only layout changes in a wiring-diagram representation, identify the exact representation transition and preserved connector, pin, and connection correspondence; `E1` remains the same. If instead only an exact publication form, carrier, or rendering changes, identify that E.17/E.24.PUB object and relation; `E1` again remains the same. If a connection claim is removed from `E1`'s ClaimGraph or the legend changes the effective reference scheme, the changed claim content or scheme identifies episteme `E2`.

The wiring-diagram representation under its stated diagram scheme represents the connectivity of `H`; its mapping resolves connector marks and pin marks to the independently identified connectors and pins. A layout-only transition preserves connector identity, pin identity, and connection predicates. If the diagram omits a connection that remains in `E1`'s ClaimGraph, that representation loses one connection predicate. If a revised legend no longer resolves an earlier mark to its connector, that mark-to-connector reference is lost. The diagram remains admissible for maintenance diagnosis only while the connections on which that diagnosis depends are preserved and recoverable; stop that use or return to the source relation structure when they are not.

For a concrete typed receiving use, let local kind `K_H` admit already identified epistemes about H whose complete content consists of affirmative or negative physical-connectivity claims between identified pins under S1. The criterion excludes other subjects, proximity readings, and additional claim families; it classifies whole epistemes, not claim-content or scheme individuals. C.3.2 judges candidates against that criterion. Let E1 assert that pin P1 is connected to pin P2.

| Proposed replacement | Constitution and receiving-use result |
| --- | --- |
| a layout change preserving every connector, pin, connection claim, and S1 rule | the same E1; the receiver still checks that its representation exposes the connections needed for diagnosis |
| the same claim field now denies that P1 is connected to P2 | a different episteme that still meets K_H; admissible input does not mean equal content or a conservative replacement of E1 |
| the same marks now mean spatial proximity under S2 | a different episteme because interpretation changes; it fails K_H's fixed physical-connectivity criterion |
| a proposed input whose governing legend is unavailable | membership and any identity comparison depending on that legend remain unresolved; a PDF carrier alone is not an episteme candidate |

A readability score can improve while the diagram makes the connections needed for diagnosis harder to recover. When that score is used as the practical value, apply `E.13`: name the intended diagnostic value, the readability proxy, and what became worse. Use the representation branch in :4.0 for the transition and its preserved or lost structure.

#### C.2.1:9.8 - Trained or probe-derived representation and tool-using inference

A distributed activation pattern observed during inference is a system-side phenomenon. A trained probe or decoded rendering can represent it for a declared use under `C.29` and `A.6.3.RT`. To identify a probe report as an episteme, recover what it claims about that exact phenomenon and the interpretation scheme that gives those claims meaning. Decodability or a readable label alone leaves that identity question unanswered. Use `E.10.LRN` when *learned representation* still leaves the subject or result unclear.

For a claim about particular inference or tool-call Work, open :4.0's Work branch. If a trace participates at an exact `A.6.1` result position, state that binding. When the trace carries claims about the call, identify its episteme through those claims, that Work as subject, and the effective scheme. A question about when the trace first existed separately opens :4.9.

An answer may carry a proposed solution, while an evaluation report states whether it passes a named test. To rely on the solution, inspect the support relevant to its claim; to assert empirical grounding, test :4.3's exact covered-claim mappings. A successful call or score does not supply those mappings.

When a changed tool regime changes inference behavior, locate the changed method, Work or representation and the evidence used to assess it. Update the grounding occurrence if its coverage predicate changes. Reidentify an episteme only when claim content, EntityOfConcern or effective reference scheme changes.

#### C.2.1:9.9 - Develop a naming claim in writing

A naming note starts with a concern that the proposed name hides a distinction. Following C.2.4:4.6, the author writes competing interpretations, identifies what the name would designate, and states the reason for preferring one reading. The note helps obtain the claim; a completed NameCard is useful only when the naming work needs its arrangement and comparison. Identify the resulting claim-bearing whole under :4.1.1 once its content, subject, and interpretation are recoverable.

Suppose the designation claim in that card stays the same, but `SelectionRationale` now asserts a different reason for the choice. The complete asserted content changed, so the card's episteme changed. Merely reordering fields or making the same reason easier to read can preserve it. A newly asserted reason needs its own support; preserving the designation does not transfer the earlier justification. If only an external evidence-use relation changes while every assertion in the card stays fixed, reconsider that relation and reliance without automatically changing the card's episteme.

### C.2.1:10 - Bias-Annotation  *(informative)*


C.2.1 deliberately favors explicit aboutness and interpretation because claims without an exact EntityOfConcern and effective reference scheme are difficult to compare or test. The mitigation is the `A.6.REL` minimum-current-object rule: ordinary use adds another object only when the reader's next sentence or action requires it, and states that object's direct relation to an already recoverable object.

The pattern also resists representation bias. Formal calculi, diagrams, learned representations, and interactive tools can materially change available reasoning operations, but their convenience or geometry cannot establish subject identity. State those differences under the exact C.29 lens-use or selected transition predicate, using the corresponding pattern description for any explanation needed to apply it.

Finally, the pattern has a claim-bearing-holon bias. Decodability alone does not make the decoded entity an episteme. The decoded entity is admitted as an episteme only when claim content, an exact EntityOfConcern, and an effective reference scheme are recoverable and together satisfy the constitution relation.

### C.2.1:11 - Conformance Checklist  *(normative)*

1. **Episteme identity.** Complete claim content, exact EntityOfConcern, and effective `ReferenceScheme` are recoverable under :4.1.1. Distinguish obtaining that content in writing, candidate admissibility, full identity, and suitability for the receiving action. A dependent episteme kind such as `U.MethodDescription` or `U.View` adds a governed membership judgment for the same individual, not another identity discriminator.
2. **Direct constitution and case judgment.** `EpistemeConstitutionRelation` has its three identified participants, obtaining predicate, and participant-determined occurrence-identity rule. C.2.1 defines that rule; current case facts satisfy or fail the predicate; an assertion states affirmative or negative polarity; and evaluation or evidence use states reliance only when needed. Designate an occurrence only after positive case facts and the identity rule individuate it.
3. **Declaration identity and Slot discipline.** A complete reusable declaration is first a C.2.1 episteme; A.6.0 independently judges its `U.Signature` membership. Grounding and edition declarations use the ranges in :4.3 and :4.5. The constitution declaration supplies the EntityOfConcern SlotSpec; any additional typed participant use needs its independently governed range and complete SlotSpec; a direct exact-value constitution judgment alone supplies no general ClaimGraph or ReferenceScheme ValueKind. Preserve predicate, occurrence identity, applicability, and actual dependencies. Signature-local SlotKinds never become participants, and a one-off assertion needs no signature or manifest.
4. **Classification discipline.** `A.1` governs recognition under an admitted holon kind, `C.3.2` governs local-kind membership, and `E.24.UK` governs public U-kind admission. A classification assertion needed as a separate claim-bearing object is a C.2.1 episteme about the exact candidate; it states affirmative or negative polarity for the exact classification predicate and keeps supported, refuted, or unresolved reliance separately governed. It neither creates the candidate nor changes the kind's admission.
5. **Empirical-grounding discipline.** `GroundingHolonSlot` occurs only inside `EpistemeEmpiricalGroundingRelationSignature`. Each occurrence names one exact covered claim subgraph containing at least one empirical claim and maps every empirical claim in it to the required current direct observation, intervention, measurement, or test relations involving the grounding holon. Unlisted claims receive no grounding from that occurrence. One occurrence is reidentified from the episteme, covered claim subgraph, grounding holon, and maximal continuous interval during which the complete coverage predicate is true; demonstrated coverage failure followed by restoration yields another occurrence. Evaluation counts in the empirical base only when its exact direct relation and use in the test are stated; otherwise evaluation and evidence support or challenge an assertion. Availability or loss of a report, store, or Work log alone neither makes nor unmakes grounding.
6. **Edition discipline.** `EpistemeEditionRelation` has exactly the earlier and later epistemes as participants and is acyclic in that direction. Positive continuity requires exact source use, an applicable edition policy or rule, and preserved and deliberately changed claim, EntityOfConcern, and scheme features satisfying that rule. Fork, translation, retargeting, and independent reconstruction are explicit failure branches. Work, Method, provenance, and change facts supply case facts but no label makes continuity true.
7. **View and neighboring-relation discipline.** C.2.1 identifies epistemes; E.17.0 alone tests the conformance of fixed E to fixed P and the resulting same-individual `U.View` membership. One named describing use may select one exact viewpoint P, but that selection creates no context value, selects no view, and remains separate from A.6.3 source-to-receiving construction. Several views remain a plurality. Recover a C.13 collection only when the use depends on that plurality as a collection, and an A.22 structure only when it depends on their organization. Cross-view claims use the pattern for their direct subject relation or return an exact blocker naming the participants, required predicate, use, and missing defining or constraining pattern. Use E.17 for view or publication form and E.24.PUB for publication occurrence, form, and carrier, not for view membership or correspondence.
8. **Description boundary.** Recover the EntityOfConcern and description episteme under their C.2.1 identities. Different constitution triples identify different epistemes. In permitted self-description, the EntityOfConcern designation resolves to that same episteme; self-reference supplies no assurance by itself.
9. **Specification use.** Specification force is admitted only when the E.10.D2 conditions obtain: checkable claims and a named harness or validation relation. A selected viewpoint is preserved or updated only for the named describing use whose reliance depends on it. Naming and appearance do not grant specification force.
10. **Agency, work-result, and identity-inception boundary.** Only systems perform Work. `A.6.1` declares typed argument and result positions; neither a position nor its binding says when the bound entity first existed. When a current claim asks that question, the subject's direct inception pattern must define the predicate and identity rule, and current case facts must satisfy them. When inception is attributed to Work, apply A.15.PROD:4.5 and retain the exact specification and applicability basis, actual effects, earliest satisfying boundary, and `identityClosingWork`; a missing required basis stops that positive claim. If no subject inception governor exists, return one `missing-governor` blocker naming the entity or candidate basis, facts, required predicate, and receiving use. When no first-existence claim is current, do not open the inception boundary. No morphism, heading, representation, form, bare A.6.1 `result`, generic work result, or universal production relation supplies that fact.
11. **Publication boundary.** Distinguish the episteme from its publication occurrence, form and carrier. A `U.View` is that same episteme classified under E.17.0's conformance condition. Plain `published episteme` states publication participation; a receiving classification need follows C.3.2 and public-kind admission follows E.24.UK.
12. **Representation boundary.** Tuple components, graph elements, schema fields, and notation tokens remain representation elements. An explicit correspondence may relate one to an independently recovered object without identifying the two or changing the represented direct relation's participants.
13. **Transformation and Bridge-use boundary.** A morphing, viewing, or retargeting declaration states which C.2.1 identity discriminators are preserved or changed and names the exact correspondence or retargeting relation used. For cross-context sense use, F.9 separately establishes the exact Bridge; one C.2.1 assertion about that Bridge carries `<u,d,r,t>` and polarity; A.10 handles ordinary evidence reliance; B.3 adds a result only when an actual named assurance claim is current; and the direct receiver defines or tests any actual Work, assertion, publication, relation, or operation application. The mathematical morphism performs no work, and none of these objects authorizes another.
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
| Grounding by evidence presence | Stored evidence or one unrelated measurement is treated as grounding the whole episteme. | Select the exact covered claim subgraph containing at least one empirical claim, map every empirical claim in it to its required observation, intervention, measurement, or test relations involving the grounding holon, and test continuity of that complete coverage predicate. Evaluation or evidence supports the grounding assertion unless an exact evaluation relation is explicitly part of the empirical test; availability alone determines no world-side grounding state. |
| Edition work as relation participant | Revision Work is inserted into `EpistemeEditionRelation`, so two Work occurrences appear to create two continuities between the same editions. | Keep earlier and later epistemes as the two participants. Use Work, Method, source use, provenance, and change facts only as case facts for the independently stated continuity rule. |
| Edition by filename or Method label | `v2`, a later timestamp, or a Method named `revision` is taken as continuity. | Recover both episteme identities, exact source use, the applicable continuity rule, its preserved and deliberately changed features, and its fork, translation, retargeting, and reconstruction failures. |
| Published-episteme kind | Publication participation alone is treated as sufficient admission of a durable episteme kind. | Keep C.2.1 identity and state the publication occurrence. If the receiving use needs classification by participation, apply C.3.2; E.24.UK separately decides whether a durable public kind is needed. |
| View as formatting, generation, or publication | A filtered table, diagram, query result, or published face is called a view because of appearance, construction history, or carrier, and a heading or edge is treated as cross-view correspondence. | Identify the receiving episteme under C.2.1 and apply `E.17.0` conformance for `U.View` membership. Add A.6.3 only for an actual source-to-receiving construction. Apply the exact direct subject-relation governor to correspondence; if none is recoverable, return an exact blocker naming the participants, required predicate and use, and missing governor. |
| Bridge as use verdict | An obtaining Bridge, its predicate profile, or a card is treated as proving that one comparison, translation, publication, or other use is suitable, authorized, or already performed. | Keep the Bridge under F.9. State the proposed use in a separate ordinary C.2.1 assertion with the Bridge as EntityOfConcern and `<u,d,r,t>` plus polarity; use A.10 for ordinary evidence reliance, B.3 only for an actual named assurance claim, and the direct pattern for any receiving object that actually exists. |
| Mathematical identity leak | A tuple key or graph node identity becomes episteme identity. | Keep representation identity separate and use the C.2.1 identity triple. |

### C.2.1:13 - Consequences  *(informative)*

**Benefits.** Episteme identity becomes stable across carrier and publication changes. Description, empirical grounding, viewing, edition, and representation questions can be repaired locally because each has a direct relation. Self-description and multi-view use need no second ontology. The same pattern works for physical engineering, medicine, learning, formal work, and computational modeling.

**Costs.** A load-bearing episteme use has a recoverable exact EntityOfConcern and effective reference scheme rather than relying on a title or file. Empirical-grounding and edition claims depend on their own obtaining and identity evidence. Existing record-shaped schemas sometimes need to distinguish their fields from actual relation participants.

**Limits.** C.2.1 does not decide whether an epistemic claim is true, sufficient, current, or authoritative. It does not prescribe a file format, graph database, proof calculus, or publication layout. Those questions remain with evidence, evaluation, temporal, representation, and publication patterns.

### C.2.1:14 - Rationale

The three constitution discriminators identify the knowledge holon; empirical grounding, viewpoint, scope, edition, and publication remain separately governed. A change in one of those neighboring relations can therefore be examined without reidentifying an unchanged episteme.

The constitution relation explains how the identity-bearing participants are organized. The episteme is the resulting holon with a whole-level capacity to carry interpretable claims. A relation declaration is first its own C.2.1 episteme; `A.6.0` judges whether its complete content satisfies `U.Signature` membership, including the declared range, and `RelationSignature` names its relation-facing use. A complete declaration carries the direct relation for its stated typed reuse; an assertion claims that the relation obtains, and a publication occurrence makes a selected episteme edition available. None replaces another.

### C.2.1:14.1 - SoTA-Echoing

**When does grounding cease?** For the pump case in :9.1, a compact record with one evidence-status flag is useful for finding the latest available report. If that flag also defines grounding, an unavailable archive would end the grounding occurrence even while the required measurements continue; an available pressure report could also be mistaken for coverage of the unrelated maintenance-interval claim. The questions about current empirical coverage and its continuity require more information.

Sections :4.3 and :4.8 therefore select explicit covered claims, their mappings and the maximal continuous interval of complete coverage. This costs claim-to-world mapping and continuity evidence when that relation is asserted. It allows the practitioner to keep grounding continuous through an archive outage, withhold reliance when coverage is unknown, and recognize another occurrence after a demonstrated break and restoration. The cheaper evidence-status record remains sufficient for the question of report availability. Reopen the grounding account when a required mapping fails, its covered claims change, or the purported evidence no longer establishes continuity.

**When is a revision an edition of this knowledge object?** [PROV-O, 2013 Recommendation, `wasRevisionOf`](https://www.w3.org/TR/2013/REC-prov-o-20130430/#wasRevisionOf), provides a usable provenance assertion: derivation as a revised version retaining substantial original content. It is economical for exchanging a producer's revision assertion. C.2.1's :9.5 asks the additional domain question of which changes count as continuation of this episteme family. A translation can retain substantial content while that family's policy classifies it as a derivative.

Section :4.5 therefore uses provenance as a case fact and tests an explicit continuity policy over the two episteme identities, source use, preserved features, permitted changes and failure conditions. The cost is recovering the policy and the changed features; the gain is a decision that distinguishes the accepted correction from translation, retargeting or independent reconstruction under the same policy. A trusted revision assertion can be consumed for a use that accepts its producer's criterion. A use requiring the local edition judgment must test the local criterion. Reopen that judgment when the source-use facts, policy or required preserved features change.

**When may observations be identified as concerning the same object?** [Rodin's reconstruction, §§2–7](https://philsci-archive.pitt.edu/12116/1/vh.pdf), makes a theoretically supported connection between observations part of the identifying construction. Section :9.6 retains the episteme/object distinction and directs the identifying construction to A.1.RI:5.1. The two association candidates require displacements of either 1 cm or 9 cm. The 2 cm/s premise selects one; the 10 cm/s premise admits both.

For this ordinary conditional identification, :4.2.3/:9.6 retain an ordinary identifying claim supported by A.1.RI's domain criterion, motion premises and comparison of associations. Requiring a separately governed relation occurrence first would add a declaration dependency without changing that calculation. The occurrence account is worth its additional cost when a later assertion must designate that exact occurrence; then `A.6.REL` supplies its predicate and identity requirements. A changed speed bound reopens the identification itself, whereas a missing occurrence rule blocks only the occurrence-dependent use.

These comparisons select different information for different questions. The three identity answers suffice for identifying the episteme; empirical coverage, edition continuity and occurrence designation are added for the respective uses above.

**Material interaction and grounding.** [Malafouris, *People Are STRANGE* (2026)](https://mitpress.mit.edu/9780262553902/people-are-strange/), develops the material-engagement account of how experienced self-boundaries change with tools, surroundings and ways of engaging with them. This motivates a question for :4.3 and :9.3: has a change of material interaction changed what can be observed or inferred about the subject? Reconsider the covered claims and grounding holon where that change affects their empirical support.

**Internal representation and reasoning.** [Anthropic's *A global workspace in language models* (2026)](https://www.anthropic.com/research/global-workspace) reports interventions in which changing an internally represented intermediate concept changes a later answer in the studied reasoning tasks. This supports a causal contribution of those representations in those tasks. Use :9.8 to distinguish the changed activation, the probe's rendering and the answer when interpreting the result.

**Tool availability and inference quality.** [Cheng et al. (2026)](https://arxiv.org/abs/2605.06326) report degraded reasoning under tool-enabled evaluation even when the studied models made almost no tool calls, and develop training methods that preserve reasoning while adding tool use. For an inference-quality claim, use evidence from the applicable tool regime and distinguish availability, actual calls and evaluated performance through :9.8.


### C.2.1:15 - Relations  *(overview)*

- **A.1.RI** constructs observation-based reidentification of the subject while C.2.1 retains the identities and claims of the observation epistemes.

- **Builds on:** `A.1` for holon recognition, `A.6.REL` for direct relation occurrences, `A.6.0` for independent same-individual `U.Signature` membership and relation-facing `RelationSignature` use, `A.6.5` for declaration-local SlotSpecs and participant designations, `A.7` for entity-description distinction, and `C.29` for mathematical-lens use.
- **Coordinates with:** `A.3.2` for `U.MethodDescription` membership without a second episteme identity; `C.3.2` for local-kind membership judgments; `E.24.UK` for ontology-level U-kind admission; `E.10.D2` for Description and specification-use discipline, including selection that creates neither conformance nor membership; `A.6.1` for typed operation positions and exact current application bindings; `A.6.2`, `A.6.3`, and `A.6.4` for morphing, source-to-receiving viewing construction, and retargeting; `A.6.3.RT` for representation transitions; `E.17.0` for conformance of fixed E to fixed P and `U.View` membership; `C.13` and `A.22` for separately current multi-view collections and structures; the pattern for the exact direct subject relation, or an exact missing-relation blocker naming the participants, required predicate, use, and missing defining or constraining pattern; `F.9` for exact Bridge semantics when a claim concerns a bounded cross-context use; `E.13` when a visible representation-quality proxy is used as practical epistemic value; `A.2.6` for claim scope; `A.1.1` for bounded model-use structure; `A.10` and `B.3` for evidence and assurance; `A.14` only when a phase or separately selected edition collection is current; `C.2.P`, `A.3.1`, and `A.3.4` when source use, revision method, or actual change is current in edition-continuity evaluation; C.2.1:4.9 only when a local claim separately asks when a new entity began; `E.17` for multi-view publication forms and uses; `E.24.PUB` for publication occurrences, forms, and carriers; and `G.11` for currentness.
- **Used by:** every pattern that identifies, describes, classifies through an explicit assertion, compares, grounds, transforms, views, publishes, or refers to a `U.Episteme`.

### C.2.1:End
