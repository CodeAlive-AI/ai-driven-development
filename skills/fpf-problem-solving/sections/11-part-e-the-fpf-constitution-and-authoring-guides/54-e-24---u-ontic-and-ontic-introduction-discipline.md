## E.24 - U.Ontic and Ontic Introduction Discipline

> **Type:** Part E FPF authoring discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### E.24:0 - Use This When

Use this pattern when FPF work appears to need a durable ontic: a connected action-facing ontology unit whose stable identity and admissible uses depend on keeping several direct relation kinds, their relation-participant meanings and admitted actual-participant kinds, reusable declarations, and neighboring governing patterns coherent.

On first reading, distinguish four outcomes. A durable ontic is a reusable ontology unit whose governing pattern states its identity and core relations for dependent FPF use. A bounded local episteme is a claim-bearing `U.Episteme` that coordinates already governed entities and relations for one named use. Direct governing-pattern use means relying on those existing patterns without adding another ontology unit. Quote-only or reduced use keeps a source expression available without giving it FPF kind or governing force.

Typical, non-exhaustive working situations include:

- a bounded local episteme starts being cited as though it were a new ontology unit;
- a source expression or project-side expression keeps pointing to several FPF values at once;
- a draft ToC row names a calculus or object family, but no current pattern carries its governing meaning;
- a subject pattern begins to carry local slot-relation doctrine that other patterns also need;
- a proposed subject needs one core direct relation kind and several governing patterns to remain coherent for use.

**Primary EntityOfConcern.** The EntityOfConcern is `U.Ontic`, the durable action-facing ontology unit. The work governed here is the ontic-introduction decision about whether a candidate subject needs such an ontic, remains claims in a bounded local episteme under C.2.1, is already handled by existing governing patterns, or stays quote-only or reduced-use source wording. The decision episteme describes and justifies that choice; it is not part of `U.Ontic`.

**Primary working reader.** The first reader is an FPF pattern author or reviewer deciding whether several nearby patterns are describing one ontic, several existing governed values, or only a compressed source expression. The downstream reader is the practitioner who needs the resulting subject pattern to say what can be done, claimed, relied on, repaired, compared, or stopped.

**Working concern and viewpoint.** From the FPF-authoring viewpoint, preserve the subject's governing relations without duplicating kinds or promoting a claim-bearing episteme for one named use into durable ontology.

**First useful move.** Decide whether the candidate subject needs a durable ontic, is already governed by existing patterns, needs only a bounded local episteme whose ClaimGraph states the claims required by one named work or decision, or remains a quote-only or reduced-use source expression.

**What goes wrong if missed.** FPF grows shadow ontology. The same project concern becomes a method in one place, a mechanism in another, a record in a third, and a local checklist in a fourth. Later uses then repair visible symptoms instead of settling the underlying kind, slot, and governing-pattern question.

**What this buys.** A durable ontic gets an explicit identity plus named direct relation kinds, participant meanings, obtaining conditions, and occurrence-identity rules. RelationSignature and SlotSpec declarations are added only where dependent uses need reusable participant typing. Otherwise, state the coordination in a bounded local episteme whose ClaimGraph cites the direct entities, relations, and governing patterns already carrying the work.

Main gains:

- it prevents duplicate ontology by recovering the direct entities and relations first, then reusing their governing patterns;
- it replaces negative catalogues with positive relation discipline: state the direct relation kind, relation-participant meanings, admitted actual-participant kinds, obtaining condition, and occurrence-identity rule; add `RelationSignature` and `SlotSpec` declarations only when a receiving use needs reusable typing;
- it gives dependent patterns one stable durable ontic and one governing pattern to cite without copying direct relation rules or reusable SlotSpecs;
- it separates durable ontic introduction from bounded local epistemes, direct governing-pattern use, other claim-bearing assertion and description epistemes, publication occurrences, publication forms, presentation carriers, views, representations, and quote-only source expressions;
- it makes wording follow ontology: each local term names the identified entity, named direct relation kind, declaration episteme, claim-bearing episteme, publication occurrence, selected publication form, identified presentation carrier, governed view, or C.29 representation under its governing pattern.

**Not this pattern when.**

- If one existing governing pattern already carries the claim, use that pattern directly.
- If the issue is only one wording-use repair row, use `E.10` and `E.10.ARCH`.
- If the issue is only a new or revised mechanism meaning, use `E.20`.
- If the issue is only durable naming, use `F.18`.
- If the issue is only a pattern publication-form or section-order matter, use `E.8`.

### E.24:1 - Problem Frame

Some FPF governed objects are small enough to define through one direct relation pattern. Others become candidates for a durable ontic when several direct relations and governing patterns need persistent coordination across dependent use. `U.Episteme` is the central example: correct reuse depends on keeping its identity, components, direct relations, dependent same-individual episteme kinds, descriptions, and publication-side relations coherent without treating a card field, RelationSignature, or C.29 representation as the episteme itself.

The same failure recurs elsewhere. A project label such as algorithm, process, model, architecture, service, quality, time, rhythm, change, or source can point to several FPF objects. Choosing a better word does not recover those objects. Introducing one umbrella kind fuses entities and relations that already have direct governing patterns. E.24 governs the decision whether a durable ontology unit is needed and the declaration of the direct relations that make it useful.

### E.24:2 - Problem

Without this discipline:

1. **Local epistemes become pseudo-ontics.** A repeated claim-bearing episteme or reusable publication form starts to be cited as a new ontology unit even though its claims or layout only refer to existing governed values.
2. **Draft ToC rows become false authorities.** A planned ToC row is cited as if it already supplied current governing text.
3. **Pattern placement is mistaken for ontology.** A numbering or placement label becomes the proposed ontic even though no primary governed subject kind, core direct relation, or governing pattern is named.
4. **Reusable SlotSpecs are copied without a direct relation.** Several patterns list similar SlotSpecs, but no direct pattern states the relation kind, participant meanings, obtaining condition, or occurrence identity.
5. **Existing typed values are duplicated.** A new head repeats `U.Method`, `U.Mechanism`, `U.WorkPlan`, `U.Work`, evidence, gate, source, or result relations under a new name.

### E.24:3 - Forces

| Force | Tension |
| --- | --- |
| Ontic stability vs bounded local explanation | A durable FPF ontic needs stable identity plus named direct relation kinds and their governing rules; a bounded local episteme keeps its C.2.1 identity and needs only the claims and references required for one application family. |
| Reuse vs overgrowth | Dependent patterns may need one stable direct relation and a reusable declaration; premature `U.*` growth creates another ontology. |
| Ontology governance vs pattern placement | The primary governed subject kind, core direct relation, and governing patterns determine the ontic-introduction decision; a pattern nest is only publication and specialization placement under E.8. |
| Draft citeability vs current governance | Draft ToC rows can guide investigation, and an accepted DRR can carry the authoring decision, but only current governing-pattern text carries governing meaning for current FPF use. |
| Naming vs ontology | F.18 can improve a name, but naming cannot decide identity, direct relations, declarations, species, or the reliance basis of dependent patterns. |

### E.24:4 - Solution

E.24 governs `U.Ontic` as the FPF kind for a connected action-facing ontology unit. Before dependent patterns rely on that unit, the accepted ontic-introduction decision states its primary governed subject kind, stable identity, core direct relation, neighboring direct relations, any reusable RelationSignature declarations, governing patterns, named dependent-pattern reliance, and non-use boundary.

`Connected` is an admission condition here, not a metaphor. For every kind or relation included in the ontic, the decision states how named direct relations connect it to the primary governed subject kind and core relation, and identifies the pattern governing each direct relation. `Action-facing` means that the decision names at least one work or decision whose use of those relations changes when their coordination is absent. Topic adjacency and a shared label satisfy neither condition.

Named dependent-pattern reliance states each dependent pattern and the identified ontic identity, direct relation rule, or `RelationSignature` declaration on which it relies. A dependent pattern name without that reliance basis is insufficient.

Reidentify one `U.Ontic` by its primary governed subject kind and its core direct relation kind, including that relation's predicate, relation-participant meanings, and admitted actual-participant kinds. A new name, ontic-description edition, publication occurrence, publication form, presentation carrier, view, representation, dependent-pattern set, or neighboring relation does not by itself create another ontic. A change of primary governed subject kind, core predicate, participant meaning, or admitted actual-participant kind reopens the ontic-introduction decision; do not preserve identity merely by retaining the old name.

Keep the subject under decision separate from the claim-bearing epistemes and publication-side relations through which people inspect or receive that decision:

- the proposed or selected `U.Ontic` is the ontology unit under concern;
- a claim-bearing ontic-introduction decision episteme records and justifies the selected ontology unit without becoming that ontic;
- an ontic-description episteme may describe the selected ontic, using that identified ontic as its EntityOfConcern under C.2.1;
- when a receiving use needs publication, one publication occurrence makes one selected episteme edition available to a declared audience for a declared bounded use, one publication form expresses that edition for the use, and one `U.PresentationCarrier` may bear the form.

A `U.View` remains the same episteme individual for which E.17.0 conformance to at least one exact viewpoint episteme obtains. Any A.6.3 viewing construction remains a separate relation. A C.29 representation remains a representation in explicit correspondence with independently recovered objects. None is inferred from the visible shape of a card, table, schema, diagram, file, or pattern section.

Keep the direct verbs with their objects. A designator designates an already recoverable referent. A governed reference resolves under an effective reference scheme. An assertion or description episteme carries claims and participant designations. A publication occurrence makes an episteme edition available; a publication form expresses it for that use; a presentation carrier bears the form.

Start from the ontic and add only a named neighboring object whose independently governed identity or direct relation changes the current decision or receiving use. Non-exhaustive examples of such neighboring objects are a claim-bearing episteme, `U.View`, C.29 representation, publication occurrence, publication form, or `U.PresentationCarrier`. These objects are downstream of the ontic-introduction question and do not establish that a durable ontic is needed.

When a durable ontic is selected, its branch of the ontic-introduction decision states at least:

- the primary governed subject kind and the practical concern through which users recognize why coherence among its direct relations matters to the named work or decision;
- the `onticSlotRelation`, meaning the direct relation kind that connects the ontic's core participants; its governing pattern states participant meanings, predicate obtaining, and occurrence identity;
- any `RelationSignature` episteme used to declare reusable SlotSpecs for those relation-participant meanings;
- the current FPF patterns that govern the primary subject kind, the core direct relation, and the named neighboring direct relations;
- the pattern that governs the durable ontic;
- the named dependent-pattern reliance: each dependent pattern and the identified ontic identity, direct relation rule, or `RelationSignature` declaration on which it relies without copying that rule or declaration.

A project entity does not fill an ontic. It keeps its own kind and may participate in the ontic's direct relation or in a neighboring direct relation. A SlotSpec belongs to a `RelationSignature` declaration. An assertion or description episteme may designate the world-side participants by value or reference and claim that the direct predicate obtains. The participant, SlotSpec, designation, assertion, and relation occurrence remain different objects.

FPF ontology is therefore not one flat class list and not a collection of filled records. A durable ontic is one connected ontology unit over a small group of direct kinds and relations. The same project entity may participate in relations governed by several ontics without changing its kind or becoming part of a second ontology.

E.24 carries the accepted decision to use `U.Ontic` because a connected ontology unit needs stable identity and one pattern that governs its direct relation set. Without that governing pattern, nearby patterns repeatedly reconstruct the direct relation rules, declaration rules, and basis for dependent-pattern reliance. With `U.Ontic`, those patterns can cite the accepted ontic-introduction decision and governing pattern while each entity, relation occurrence, assertion episteme, description episteme, publication occurrence, publication form, presentation carrier, view, and representation retains its own governing pattern.

The cost is kernel growth and metamodel risk. E.24 contains that cost by making `U.Ontic` narrow. A bounded local episteme, source expression, project-side expression, recurring table-shaped episteme or publication form, pattern nest, or draft ToC row is not a `U.Ontic` merely because it looks ontology-shaped. A candidate becomes a `U.Ontic` only when the E.24 decision names the primary governed subject kind, stable identity, core direct relation and governing pattern, neighboring direct relations, the reliance basis of each named dependent pattern, existing-pattern reuse, and non-use boundary by value.

U-kind admission is a neighboring E.24-family question, not the main body of E.24. E.24 keeps the minimal invariant:

- a durable ontic is a connected action-facing ontology unit;
- durable `U.*` kindhood is admitted only through an accepted E.24-compatible ontic-introduction decision;
- one ontic-introduction decision may govern a root U-kind and dependent durable values; E.24.UK decides which names receive U-kind force;
- ontic, claim-bearing description episteme, publication occurrence, publication form, presentation carrier, view, and representation stay distinct.

Use `E.24.UK` when the authoring decision asks whether a `U.*` spelling, type or kind wording, title, filename, heading, ToC row, or structural name is retained, governed by `C.3` typed reasoning, kept as a dependent durable value, or renamed to the actual governed object. `E.24.UK` governs the detailed U-kind admission rule, root and dependent U-kind governance, relation to `C.3` typed reasoning, and structural `U.*` handling. E.24 only records the result when the ontic-introduction decision needs to say whether a candidate name is retained as a root U-kind, retained as a dependent durable value, governed by `C.3` typed reasoning, or treated as a non-U object governed elsewhere.

#### E.24:4.0 - Constructive Foundation And Math-Lens Boundary

If a reader asks where FPF ontics get constructive grounding, start here and then follow the chain named by the current claim. E.24 governs the ontic-introduction decision. The ontic is the `EntityOfConcern`; its `onticSlotRelation` is the core direct relation governed as constitutive for that ontology unit. Any `RelationSignature` or description remains a separate episteme; any publication occurrence, publication form, presentation carrier, view, or C.29 representation retains its own kind and direct relation.

For structural identity claims, the constructive chain is `E.14 -> B.3.5 -> C.13`: Working-Model relation first, declared `validationMode`, `tv:groundedBy`, and a reconstructible `Γ_m.sum`, `Γ_m.set`, or `Γ_m.slice` trace. The `Γ_m` trace is the reconstructible grounding object cited through `tv:groundedBy` under B.3.5. If a graph, tuple, or another mathematical expression represents that trace, the expression is a separate C.29 representation. Neither the trace nor its representation becomes the public relation vocabulary, and this structural grounding apparatus is not required for non-structural ontics.

For non-structural ontics, use the governing identity, grounding, or recognition rule named by the direct pattern. Non-exhaustive examples of such direct-pattern bases include `EpistemeConstitutionRelation`, work occurrence identity, `C.3` typed reasoning, `A.6` declaration shape, Concept-Set witnesses, formal-substrate or principle-frame declaration, and another accepted identity test. Use `C.29` when the mathematical lens itself is current; use `E.24.UK` when a `U.*` name is being admitted; use C.2.1 for the identity of a description episteme; use `E.24.PUB` for the publication occurrence that makes one selected episteme edition available, its audience and bounded use, publication form, and presentation carrier.

`A.14`, `B.2`, and `A.15.1` carry BORO- and CCO-compatible identity and occurrence discipline. They support the constructive foundation; they do not create a separate durable-kind ontology.

Keep the world-side direct relation, its reusable declaration, the claim-bearing episteme, and any mathematical representation separate before dependent patterns rely on the ontic.

An ontic is selected when FPF needs one connected ontology unit because the stability of its core relation and neighboring relations matters across several patterns. The ontic is not a relation occurrence, `RelationSignature`, schema, table, or value assignment.

Keep four governed objects and their relations distinct:

1. **Direct relation.** The direct governing pattern names the relation kind, each relation-participant meaning, each admitted actual-participant kind, the predicate obtaining condition, and the occurrence-identity rule.
2. **Reusable declaration.** When several uses need the same participant typing, a `RelationSignature` episteme declares one `SlotSpec = <SlotKind, ValueKind, refMode>` for each relation-participant meaning needed by typed reuse. `ValueKind` constrains the kind of an actual participant corresponding to that SlotSpec. `refMode` governs only how a describing episteme designates that participant.
3. **Assertion or description.** A current episteme may supply values or references that designate the participants and may claim that the predicate obtains. Supplying those designations neither creates the participants nor makes the relation obtain.
4. **Mathematical representation.** `C.29` may represent a declaration, assertion, or selected relation occurrence as a tuple, graph, or hypergraph. Operands, tuple components, nodes, and edges remain representation elements. An explicit correspondence relation can relate one such element to a previously recovered relation object without identifying them.

#### E.24:4.0a - Dispatch description, viewing, representation, and publication by governed object

Use this dispatch only when one of these neighboring objects is current. The ontic-introduction decision names the direct relation through which that object matters to the selected ontology unit; the object's direct pattern governs its identity, participant meanings, admitted participant kinds, obtaining condition, and admitted use.

| Current neighboring object | Governed use in an ontic-introduction decision | Direct governing pattern |
|---|---|---|
| claim-bearing ontic-introduction decision, assertion, or ontic-description episteme | carries claims and designations about the proposed or selected ontic while retaining its own C.2.1 identity | C.2.1 and the direct decision, assertion, or description pattern |
| `U.View` | the same episteme individual when E.17.0 conformance to at least one exact viewpoint episteme obtains; selected use and optional A.6.3 construction remain separate | E.17.0 for membership; A.6.3 only for construction |
| publication occurrence | makes one selected episteme edition available to a declared audience for a declared bounded use | E.24.PUB |
| publication form | expresses the selected edition for that publication use | E.24.PUB and E.17 |
| `U.PresentationCarrier` | bears the publication form | E.24.PUB and E.17 |
| C.29 representation | corresponds to independently recovered objects for a declared modeling or reasoning use | C.29 |

One encountered inspection card can expose several governed objects whose identities and relations need separate recovery. Its filled claim set may be a claim-bearing episteme; its reusable layout may be a publication form; a selected diagram element may be a C.29 representation element; and its paper sheet or file may be a `U.PresentationCarrier`. A publication occurrence can make the selected card-episteme edition available to a maintenance team. The word `card` identifies none of these objects by itself.

When several current governing patterns already address the same project concern, select an ontic only if its named core and neighboring direct relations keep those governed values coherent without fusing their kinds. A `U.Method`, `U.Work`, `U.Mechanism`, role-assignment occurrence, transformation-flow structure, assertion episteme, publication occurrence, publication form, presentation carrier, view, and representation remain distinct. The ontic-introduction decision includes them in the ontology unit only by naming the direct relation kinds and governing patterns that connect them.

Record the ontic-introduction decision in this order:

1. **Selected ontology unit or bounded local episteme.** Name the durable ontic and its identity criterion. If no ontic is selected, identify the bounded local episteme under C.2.1 and state its non-governing bounded use.
2. **Core direct relation.** Name `onticSlotRelation`, its relation-participant meanings, admitted actual-participant kinds, obtaining condition, occurrence-identity rule, and direct governing pattern.
3. **Reusable declaration when needed.** Name the `RelationSignature` and SlotSpecs needed by dependent patterns.
4. **Neighboring direct relations.** Name each direct relation that connects an independently governed neighboring entity to the core. When availability is current, name the direct relation whose occurrence makes one selected episteme edition available. Do not promote a neighboring entity into an extra core slot merely because it affects use.
5. **Description and publication boundary.** Name each description episteme whose EntityOfConcern is the ontic. When availability is current, name the publication occurrence, selected episteme edition, declared audience, bounded use, publication form, and presentation carrier without identifying any of them with the ontic or a world-side relation occurrence.

A relation-participant meaning belongs in the core direct relation only when the direct predicate depends on an actual participant having that meaning and the direct pattern states the admitted kind of that participant. When typed reuse is needed, a compatible `RelationSignature` declares that admitted kind as the SlotSpec's `ValueKind`. A neighboring entity stays outside the core when its relevance is already expressed by another direct relation. Reuse pressure can justify a `RelationSignature`; it cannot turn a neighboring relation, record field, or mathematical operand into a core participant or a SlotKind.

Optional-in-use status belongs to a declaration or description. It does not mean that a world-side relation occurrence has an unfilled participant. A missing designation leaves the assertion incomplete or the participant unknown to the current user. It does not show that the participant is absent, and it does not make the direct predicate obtain or cease.

Not every ontic needs every neighboring object. Add a `RelationSignature` only when dependent patterns need reusable participant constraints. Add an assertion or description episteme only when a named work or decision depends on stating or inspecting a current claim. Add a publication occurrence, publication form, or presentation carrier only when availability to an audience and use is current. Recognize `U.View` membership only through E.17.0 conformance, add A.6.3 construction only when that history matters, and add a C.29 representation only when the declared modeling or reasoning use depends on it. Keep neighboring entities under their direct relations rather than adding record fields to the core relation.

Keep annotation proportional. E.24 calls for recovery only where wording can change ontic identity, a direct relation, participant meaning, a reusable SlotSpec declaration, a description claim, admissible use, or the reliance basis of a dependent pattern. If readable domain prose already preserves those objects, do not replace it with declaration syntax merely to show that an ontic exists.

This differs from pure ontology engineering because FPF patterns are action-facing: they help an engineer-manager decide what can be done, claimed, relied on, repaired, compared, or stopped in a problem situation. The accepted ontic-introduction decision supplies the object discipline that makes those actions intelligible. It states which objects and relations the subject pattern's Solution may use, while that subject pattern still carries the practical move, boundary, evidence, and consequence.

Precision restoration uses the same discipline without turning it into lexical style. First recover the source-side entities, direct relations, assertions, descriptions, and governing patterns compressed by the wording. Then repair toward a current FPF ontic only when one accepted ontic-introduction decision states how those objects are coordinated. If no such ontic exists, use the direct governing patterns, state only the needed claims in a bounded local episteme under C.2.1, or open an E.24 ontic-introduction decision.

When a source expression opens the ontic-introduction question, preserve its source-to-use path. Name the exact expression and its source episteme; name the source publication occurrence when availability through that occurrence matters; recover the entities, relations, and claims actually carried forward; state the current quote-only, reduced, or direct governed use; and state the smallest stronger-use condition. If that condition occurs, reopen the source expression through `C.2.P` or the direct source-use pattern instead of treating the repaired noun as a substitute for the source relation.

When an `E.10.ARCH` wording-use restoration row opened the case, retain its four coordinates inside that source-to-use trace: `semanticAreaBaseConcept` is the source cue, `semanticArea` is the selected Part-F row or bounded row-set, `semanticAreaSenseFamily` prevents theme-level overgeneralization, and `ontologicalNeighborhood` is the applicability neighborhood used to recover the subject kind, relations, and governing patterns. These are coordinates of the wording repair under E.8 and E.10.ARCH. They are not components or identity criteria of `U.Ontic`; a subject discovered directly through engineering work does not need them.

E.24 governs introduction of `U.Ontic` and describes that decision discipline. Under self-application, the ontology unit, core direct relation, `RelationSignature`, claim-bearing episteme, publication occurrence, publication form, presentation carrier, view, and representation remain distinct; E.24 does not license every local ontology-shaped bundle as a `U.*` kind.

E.24 is compatible with modular ontology and ontology-design-pattern practice: modular ontology libraries and ontology design patterns show why reusable small ontology structures matter, and recent process-modeling work reports loss of reuse when process patterns remain implicit. E.24 is narrower and more FPF-specific: it governs the decision whether FPF should introduce a durable action-facing ontic, rather than importing an external microtheory or treating every reusable repair table as ontology.

If these three candidate dispositions need reusable comparison, apply `A.19.ECS` to construct the evaluation `CharacteristicSpace`: retain the current governing-pattern relations, add one bounded local episteme whose claims cite them for a declared use, or add a durable ontic and its governing pattern. E.24 supplies those candidate dispositions and the ontic constraints applicable to each; `A.19.ECS` owns characteristic selection and evaluation. A comparison result does not establish ontic identity.

Within this split, E.24 carries the distinction among the ontic, the claim-bearing decision episteme, reusable declarations, and publication-side objects, plus the ontic-introduction decision needed before dependent patterns rely on a durable ontic. Publication-section rules, adequacy scales, wording-use restoration rules, and evaluation of the resulting FPF pattern-set structures are handled by the neighboring patterns named above.

Use the current split this way:

- use `E.24` for `U.Ontic` identity, the primary governed subject kind, core direct relation, governing patterns, named dependent-pattern reliance, and non-use boundary;
- use `E.24.CD` when the current problem is detecting and characterizing an apparent subject before deciding whether it should enter an E.24 ontic-introduction decision at all; `E.24.CD` supplies detection and characterization only and selects no E.24 disposition. `Local use frame` is not an E.24 disposition: when detection material uses that phrase, recover whether it means direct governing-pattern use, a bounded local episteme under C.2.1, or source-expression use before E.24 can rely on the result;
- use `E.24.PUB` when the current problem is the distinction among the ontic, an ontic-description episteme, the publication occurrence that makes one selected edition available, the publication form that expresses it for that use, and the `U.PresentationCarrier` that bears the form; use `E.17.0` for `U.View` membership, A.6.3 for optional viewing construction, and `C.29` for a representation;
- use `A.19.ECS` only when the contested question is how to construct an evaluation `CharacteristicSpace` for comparing the resulting FPF pattern-set structures after retaining the governing-pattern relations, adding one bounded local episteme whose claims cite them for a declared use, or adding a durable ontic and its governing pattern.

This split keeps E.24 ontic-first. Questions about candidate detection, publication discipline, and contested evaluation remain under their neighboring governing patterns rather than becoming sections that turn E.24 into a general discovery, documentation, or scoring pattern.


Introduce or rely on a durable FPF ontic only after the ontic-introduction decision satisfies four checks.

#### E.24:4.1 - Check 1: Existing Governing Pattern Check

Name the current claim under decision and ask whether an existing pattern already carries it.

Use direct governing patterns first. If the case is method semantics, use `A.3.1`; if it is method description, use `A.3.2`; if it is mechanism meaning, use `A.6.1` and `E.20`; if it is work planning or dated work, use `A.15.2` or `A.15.1`. For evidence, gate, source, assurance, decision, release, publication, or another case, name the current claim and its current direct governing pattern by exact pattern ID before selecting direct governing-pattern use. If no current governor can be recovered by value, that disposition is unavailable; return to the other E.24 dispositions rather than treating the topic word as authority.

Do not introduce a durable ontic only because several patterns are near each other or because one source word appears often.

#### E.24:4.2 - Check 2: Stable Identity Test

A candidate qualifies as a durable ontic only when it has stable identity beyond one local wording issue, source expression, or bounded local episteme used for first explanation.

Ask:

1. What candidate subject and primary governed subject kind are under decision?
2. If a durable ontic is selected, which identified ontic becomes the decision episteme's `EntityOfConcern`?
3. What changes the identity of that ontic?
4. What does not change ontic identity, even if an ontic-description episteme, publication form, notation, view, or presentation carrier changes?
5. Which direct world-side relations and grounding conditions are required for identity?
6. Which dependent patterns may rely on that identity?
If those questions cannot be answered, keep any needed coordination in a bounded local episteme under C.2.1 or use the direct governing patterns without another coordination episteme.

#### E.24:4.3 - Check 3: Direct Relation and Declaration Test

An ontic-introduction decision identifies the direct relation before it introduces reusable SlotSpecs in a separate `RelationSignature` episteme.

One-screen first-use card:

The following code block is a compact publication form for a claim-bearing ontic-introduction decision episteme. Its labels prompt claims; they are not SlotSpecs, actual relation participants, or a `RelationSignature`.

Treat a filled card as the decision episteme only when its claim content, exact EntityOfConcern—the candidate subject or selected ontic under decision—and effective ReferenceScheme are recoverable under C.2.1. Otherwise the card remains a publication-form prompt and cannot be relied on as the identified decision.

For ordinary first use, complete the common prompts `practicalConcern`, `decision`, and `blockedLocalOverread`, and state `primaryGovernedSubjectKind` only when a current FPF kind has actually been recovered. In the source-expression-only branch, record that field as `unrecovered` rather than inventing a kind. Then complete only the selected disposition's current fields. A durable-ontic decision needs its root, core relation, and any declaration, neighboring relation, or dependent reliance actually consumed; a bounded-local-episteme decision needs `boundedLocalEpistemeIfSelected`; direct governing-pattern use needs `directGoverningPatternsIfSelected`; source-expression use needs `sourceExpressionUseIfCurrent`. Omit every other `IfNeeded` prompt unless that neighboring object is current; the printed form is a branch menu, not a completion checklist.

```text
OnticIntroductionDecisionCard:
  primaryGovernedSubjectKind: the exact current FPF kind when recovered; otherwise unrecovered in the source-expression-only branch.
  practicalConcern: the named work or decision that needs those relations to stay coherent.
  decision: exactly one value from this closed disposition set, selected by the current claim and required coordination: durable ontic | bounded local episteme under C.2.1 | direct governing-pattern use | source expression only (quote-only or reduced use).
  sourceExpressionUseIfCurrent: exact expression; source episteme; source publication occurrence when current; recovered entities, relations, and claims; current admissible use; smallest stronger-use condition.
  directGoverningPatternsIfSelected: exact current claim and exact current direct governing pattern for the direct-use disposition.
  boundedLocalEpistemeIfSelected: identified C.2.1 episteme; declared bounded use; ClaimGraph; EntityOfConcern; effective ReferenceScheme; non-governing stop.
  onticRootIfSelected: the EntityOfConcern and stable identity criterion.
  coreDirectRelation: relation kind; relation-participant meanings; admitted actual-participant kinds; obtaining condition; occurrence-identity rule; direct governing pattern.
  reusableDeclarationIfNeeded: RelationSignature and one SlotSpec per relation-participant meaning needed by typed reuse.
  neighboringDirectRelations: named direct relation kinds that connect other governed entities to the core.
  claimBearingEpistemesIfNeeded: identified decision, assertion, or description epistemes and the identified EntityOfConcern of each.
  viewIfNeeded: identified candidate episteme, exact viewpoint episteme, obtaining E.17.0 conformance relation, and the same candidate recognized as U.View; optional source episteme and A.6.3 construction only when current.
  representationIfNeeded: identified represented object, C.29 representation, explicit correspondence, effective representation scheme, and admitted use.
  publicationOccurrenceIfNeeded: selected episteme edition, declared audience, bounded use, and obtaining publication occurrence.
  publicationFormIfNeeded: selected publication form that expresses the selected edition for that publication use.
  presentationCarrierIfNeeded: identified U.PresentationCarrier and the bearing relation for that form.
  dependentPatterns: patterns that rely on the accepted decision without copying its direct relation rules.
  blockedLocalOverread: what this decision does not identify, create, prove, publish, represent, or authorize.
```

Before opening the full `OnticIntroductionDecision` form, run two guards. First, write the direct relation as a readable sentence and identify its relation-participant meanings and admitted actual-participant kinds. Only then declare each `SlotKind`, `ValueKind`, and `refMode` under A.6.5; when `refMode` is a `RefKind`, name the declared `RefKind`. Second, keep work-facing `U.Role` and `U.RoleAssignment` under A.2, A.2.1, and A.15; a declaration-local SlotKind is not a role value.

When an encountered card, table, schema, diagram, or record is current, recover which governed use is current before adding it to the decision. Its filled claims may identify an episteme; its reusable arrangement may be a publication form; selected elements may participate in a C.29 representation; and an identified `U.PresentationCarrier` may bear the form. Co-occurrence of fields establishes none of those uses and establishes neither a relation kind nor an obtaining relation occurrence.

Introducing an ontic organizes kinds, direct relation rules, declarations, and named dependent-pattern reliance in FPF. It does not create or individuate any project-side relation occurrence. For each such occurrence, apply the direct predicate and domain identity rule under A.6.REL. A designator may designate the already reidentified occurrence; a governed reference may resolve to it; an assertion or description episteme may carry a claim and designation about it. A publication occurrence instead makes one selected episteme edition available and neither designates nor creates the world-side occurrence.

Worked replay:

The filled card below applies the form to a pump-maintenance specification. It names the actual participants of the core relation and keeps empirical grounding, viewing, evidence, edition, and publication outside that relation.

```text
OnticIntroductionDecisionCard:
  primaryGovernedSubjectKind: `U.Episteme`.
  practicalConcern: maintenance engineers need one stable way to identify the PumpStation37 specification while grounding, views, evidence, editions, and publications change.
  decision: durable ontic.
  onticRootIfSelected: `U.Episteme`, identified under `C.2.1` through `EpistemeConstitutionRelation`.
  coreDirectRelation: `EpistemeConstitutionRelation` among `MaintenanceClaims_v7` as constitutive claim content, `PumpStation37` as the identified EntityOfConcern, and `StationMaintenanceReferenceScheme_2026` as the effective reference scheme. The admitted actual-participant kinds are `U.ClaimGraph`, `U.Entity`, and `U.ReferenceScheme`. The relation obtains when the scheme makes that claim graph interpretable and evaluable as claims about that entity and the three participants are organized as one claim-bearing whole. That participant triple identifies the occurrence. `C.2.1` governs the relation.
  reusableDeclarationIfNeeded: `EpistemeConstitutionRelationSignature` with the three SlotSpecs declared in `C.2.1`, only where another pattern needs reusable participant typing.
  neighboringDirectRelations: `EpistemeEmpiricalGroundingRelation` and `EpistemeEditionRelation` under C.2.1; `EpistemeViewpointConformanceRelation` under E.17.0 when view membership is current; and `EpistemePublicationRelation` under E.24.PUB when availability is current. A.6.3 viewing construction remains in `viewIfNeeded` and is not relabeled as one of these relation kinds. A.10 evidence-provenance use remains separately governed and enters this field only after an exact direct relation kind and direct governor are current; this worked case asserts no such evidence relation.
  claimBearingEpistemesIfNeeded: this decision is identified under C.2.1 by `PumpMaintenanceOnticDecisionClaims_v1` as its ClaimGraph, the selected `U.Episteme` ontic as its EntityOfConcern, and `FPF-Ontic-Decision-Scheme-2026` as its effective ReferenceScheme; a separate assertion about the named constitution occurrence is added only when that claim is current.
  viewIfNeeded: exact maintenance episteme E is the same individual as a `U.View` only when E.17.0 conformance to exact maintenance viewpoint P obtains; any source episteme and A.6.3 construction remain separate.
  representationIfNeeded: a wiring-diagram representation remains under C.29 and corresponds to independently recovered objects.
  publicationOccurrenceIfNeeded: if the specification edition is made available to the maintenance team for scheduled repair work, name that selected edition, audience, bounded use, and publication occurrence.
  publicationFormIfNeeded: name the form that expresses the selected edition for that use.
  presentationCarrierIfNeeded: name the identified paper sheet, file, display, or other `U.PresentationCarrier` that bears the form.
  dependentPatterns: `E.17.0` relies on the same C.2.1 episteme identity plus exact viewpoint conformance when the specification is admitted as a `U.View`; `A.6.3` relies on the independently identified source and receiving epistemes only when viewing construction is current. Neither pattern copies the constitution rule.
  blockedLocalOverread: grounding holon, viewpoint, view, evidence, edition work, publication occurrence, form, carrier, and representation are not extra participants of `EpistemeConstitutionRelation`.
```

The full replay form is heavier:

For ordinary first use, stop at the one-screen card unless dependent patterns will rely on the proposed ontic, the current claim changes admissible use, or a receiving use needs a replayable reason why a bounded local episteme under C.2.1 was not enough.

The following fuller code block is an optional publication form for one claim-bearing ontic-introduction decision episteme. Its labels prompt decision claims; they are not world-side participants, SlotSpecs, or components of the selected ontic.

```text
OnticIntroductionDecision:
  CandidateSubjectExpression:
  SourceExpressionUseIfCurrent:
    ExactSourceExpression:
    SourceEpistemeIfRecoverable:
    SourcePublicationOccurrenceIfCurrent:
    RecoveredEntitiesRelationsAndClaims:
    CurrentAdmissibleUse:
    StrongerUseCondition:
    WordingUseRestorationCoordinatesIfE10ARCHOpenedTheCase:
      SemanticAreaBaseConcept:
      SemanticArea:
      SemanticAreaSenseFamily:
      OntologicalNeighborhood:
  SelectedOnticNameIfAny:
  PrimaryGovernedSubjectKind:
  PracticalConcern: named work or decision and how absent coordination changes its use.
  OnticAsEntityOfConcernIfSelected:
  StableIdentityCriterion:
  UKindDecisionIfCurrent:
    E24UKDecisionRef: exact E.24.UK `UKindAdmissionDecision` episteme.
    AdmissionDisposition: exactly one value from E.24.UK's closed set: root | same-individual-dependent | identity-dependent | reuse | local-kind | reject.
    BranchDetailRefIfRequired: the exact branch-specific reference or references required by E.24.UK for that disposition.
    LocalGainCostAndDuplicateOntologyRisk: the decision-changing local rationale; not another disposition field.
  OnticSlotRelation:
    DirectRelationKind:
    DirectGoverningPattern:
    ParticipantMeanings:
    AdmittedActualParticipantKinds:
    ObtainingCondition:
    OccurrenceIdentityRule:
    RelationSignatureIfNeeded:
      SlotSpecs:
  NeighboringDirectRelations: for every included kind or relation, the named connecting direct relation and its current governing pattern.
  DependentKindsIfAny:
  NeighboringGovernedEntitiesOutsideCoreRelation:
  ClaimBearingEpistemesIfNeeded:
  ViewsIfNeeded:
  RepresentationsIfNeeded:
  PublicationUsesIfNeeded:
    PublicationOccurrence:
    SelectedEpistemeEdition:
    DeclaredAudienceAndBoundedUse:
    PublicationForm:
    PresentationCarrier:
  GoverningPatterns:
    OnticGoverningPatternIfSelected:
    SubjectKindAndCoreRelationPatterns:
    NeighboringDirectRelationPatterns:
    DirectUsePatternsBeforeNewOntic:
  ExistingGoverningPatternsReused:
  DependentPatternReliance: for each named dependent pattern, the exact ontic identity, direct relation rule, or RelationSignature declaration relied on.
  RelationLabelsThatAreNotNewKinds:
  NonUseBoundary:
```

For every other candidate, complete the decision form by value; no candidate inherits the `U.*` decision from E.24.

When typed reuse needs a declaration of the core direct relation, its `RelationSignature` uses A.6.5 and the E.24 decision defines no second slot discipline; the direct relation itself remains governed by its direct pattern. A SlotKind names one participant meaning only inside the selected `RelationSignature`, and its ValueKind constrains the admitted kind of the actual participant corresponding to that SlotSpec. Neither the SlotKind label nor its wording decides that kind; the participant's direct governing pattern does.

#### E.24:4.4 - Check 4: Governing-Pattern and Dependent-Use Test

State:

- the pattern governing the selected durable ontic;
- the direct pattern governing its core relation;
- each dependent pattern and the identified ontic identity, direct relation rule, or `RelationSignature` declaration on which it relies;
- each draft ToC row, planned pattern label, or absent governing-pattern section that remains non-governing.

Naming, publication placement, and evaluation remain neighboring authoring work under `F.18`, `E.8`, `E.9.DA`, and `E.21`. The ontic-introduction decision may point to those next moves, but none establishes ontic identity or replaces the governing pattern.

If the decision selects a durable ontic, write the pattern that governs it before dependent patterns rely on it. If the decision selects only a bounded local episteme, identify that episteme under C.2.1 and state its non-governing bounded use and claims by value. If no pattern governing the proposed durable ontic is written, do not cite that candidate as governing current FPF use.

#### E.24:4.5 - Bounded Local Episteme Decision

Use a bounded local episteme when one application family needs a readable coordination of entities and direct relations that are already governed elsewhere, but no new durable ontology unit is justified.

A bounded local episteme is a `U.Episteme` identified under C.2.1, not a new U-kind. Its ClaimGraph states only the claims needed to coordinate references to the existing governed entities and relations for the declared use. It therefore has an identified EntityOfConcern and effective ReferenceScheme, while every cited entity and relation retains its own identity and governing pattern.

For that bounded use:

- name the application concern and the claims the episteme carries;
- identify each governed entity and direct relation being coordinated;
- cite the pattern governing each direct relation rather than restating its participant or identity rules;
- state the tempting ontic overread that the episteme does not license;
- stop before dependent patterns treat this one episteme as a durable ontology unit.

Precision restoration may produce such an episteme when P2W, work planning, evidence use, gate use, architecture use, or publication use needs one readable local explanation. A receiving pattern may rely on the episteme's claims for that declared use, but still applies the direct governing patterns for the entities and relations to which those claims refer.

### E.24:5 - Archetypal Grounding

Use these slices as archetypes for the ontic-introduction decision. They are not a recommended progression. Each slice shows which object is being governed, whether the decision selects a durable ontic or a bounded local episteme, and which tempting overread is blocked.

#### E.24:5.1 - Episteme as Durable Ontic

`U.Episteme` passes E.24 because C.2.1 supplies stable episteme identity, direct constitution, empirical-grounding and edition relations, reusable declarations where needed, dependent same-individual episteme-kind conditions, and explicit boundaries among description epistemes, publication occurrences, publication forms, presentation carriers, views, and representations. An actual episteme is not a filled record: its components, the direct relations among them, any assertion about those relations, and any publication occurrence remain distinct.

#### E.24:5.2 - Multi-Pattern Subject Matter as an Ontic-Candidate Archetype

A project phrase such as "algorithm", "process", "solver", "workflow", "system", "quality", "time", "source", or "architecture" can point to one recognizable subject that is spread across several FPF values and patterns. The point of this archetype is not that all such subjects are one kind. The E.24 decision instead settles the status of the cross-pattern subject before patterns rely on it.

In this archetype, "process" and "workflow" are source-side expressions until recovered. They may point to method, method description, work plan, dated work, transformation-flow structure, evidence relation, source relation, gate relation, result relation, publication occurrence and its named direct relation, or another governed value. They become durable FPF ontology only through the same E.24 decision as any other proposed ontic; otherwise keep them quote-only, reduced-use, or resolved under the exact governing patterns that already carry the claim.

A source-driven use closes only after the exact expression remains linked to what was carried forward. For example, a source expression `workflow` may be retained in quotation while its current use relies only on one recovered `U.MethodDescription` under `A.3.2` and one selected `TransformationFlowStructure` under `E.18`. The source expression neither becomes their common kind nor disappears from the provenance of that use. If a later claim needs the source's stronger ordering, execution, or evidence meaning, reopen the named source episteme and apply the exact direct governing pattern for that stronger claim.

The E.24 move is:
1. name the candidate subject under concern;
2. list the direct entities and relations that currently carry the subject; for every reused declaration, separately list its RelationSignature and SlotSpecs;
3. decide whether those pieces already close under direct governing patterns, whether a bounded local episteme under C.2.1 is enough for the declared use, whether a durable ontic with a governing pattern and slot relation is required, or whether the apparent subject is only a source expression or wording compression;
4. if a durable ontic is selected, write or cite the pattern governing that ontic before dependent patterns rely on it.

Method, work, and change are one current stress case for this archetype. A project concern about changing, producing, selecting, deriving, controlling, maintaining, planning, performing, measuring, or carrying a result may involve `U.Method`, `U.MethodDescription`, `U.Mechanism`, formal-substrate declaration, mathematical-lens use, `U.WorkPlan`, dated `U.Work`, source-local process labels or workflow labels, a selected `TransformationFlowStructure`, a separate C.29 representation of that structure when current, evidence relation, source relation, gate relation, result relation, publication occurrence and its named direct relation, and temporal relation. That spread is an E.24 applicability signal. It does not by itself settle either "make one new ontic" or "the existing governing patterns are sufficient".

As non-exhaustive examples, apply the same decision to candidate subjects expressed as `system`, `relation`, role-participation, role-assignment, slot-discipline, `characteristic space`, `temporal dynamics`, or `architecture`; none is admitted as an ontic by the head alone. E.24 supplies the decision form; the governing subject pattern supplies the subject ontology and source set by value.

Dependent subject patterns may keep a thin cue: when one recognizable concern spans several direct entities and relations, name the relation currently being asserted and use its governing pattern. That cue does not license treating a local set of references as a durable ontic before the E.24 decision, assigning one entity to two kinds without direct admission, or treating a SlotKind label as alternate ontology.

#### E.24:5.3 - Draft ToC Row or Planned Pattern Label as False Authority

A draft ToC row or older source label may name a calculus, family, or object before current FPF has a governing pattern for it. Such a label can guide investigation, but it cannot govern current use.

Example: older source wording may name a method calculus before current pattern text carries it. If no current pattern text carries it, it is not a governing pattern for current FPF use. Use the patterns that govern the direct entities and relations: `A.3.1` for method semantics, `A.3.2` for method description, `A.15.2` for work planning, `A.15.1` for dated work, and `B.1.5` for method composition when ordering is current. A separate method calculus can govern other patterns only after it has its own E.24-style ontic decision, stable identity, named direct relation kinds with obtaining and occurrence-identity rules, and dependent-pattern declaration.

The same test applies to any draft ToC row or planned pattern label. If no current pattern carries the label's governing meaning, do not cite it as ontology. Either cite current governing patterns, keep the label as investigation context, or open an E.24 ontic-introduction decision.

#### E.24:5.4 - Broad Terms That Hide Several Governed Objects

Non-exhaustive examples of broad heads include `system`, `episteme`, `architecture`, `method`, `mechanism`, `temporal claim`, `dynamics`, and `change`; each can stand in for many dependent FPF patterns. That breadth is not itself enough to create a durable FPF ontic. Apply E.24 before treating a broad head as current governing ontology: name the primary governed subject kind, stable identity, core direct relation and governing pattern, neighboring direct relations, dependent patterns, description-episteme boundary, and the boundaries among publication occurrence, form, carrier, view, and representation. If those claims are missing, use the current governing patterns that already carry the work and do not cite the broad head as if it supplied current slot discipline.

### E.24:5.6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto and Epist**, **Prag**, **Did**.
Scope: the authoring decision about one candidate ontology unit: introduce a durable `U.Ontic`, rely directly on existing governing patterns, retain only the claims needed for one bounded use in a local `U.Episteme` under C.2.1, or keep source wording at quote-only or reduced use. The scope does not include the subject matter governed by the resulting pattern.

This pattern intentionally biases toward explicit identity, direct relation rules, reusable declarations where needed, and governing-pattern reuse. It resists five recurring distortions:

- **shadow-kind bias:** repeated use of one bounded local episteme is mistaken for evidence that a new durable ontic exists;
- **placement bias:** a pattern nest or draft ToC row is mistaken for the governed subject kind or governing text;
- **name bias:** a cleaner term hides unresolved kinds, slots, and relations;
- **semio-bias:** discussion of description epistemes, publication occurrences, forms, carriers, or review evidence displaces the ontic or subject matter being introduced;
- **process-bias:** development-state, publication-state, evaluation-state, or process evidence status is copied into ontic or subject-matter content.

The mitigation is the same in each case: recover the primary governed subject kind, stable identity, core direct relation, any required RelationSignature, named neighboring direct relations, and governing-pattern reuse before naming, placement, dependent-pattern reliance, or publication form starts governing the decision.

### E.24:6 - Conformance Checklist

| Check | Observable conformance condition |
| --- | --- |
| `CC-E24-1` | The authoring decision names the working problem situation, candidate subject, primary governed subject kind, current claim, practical concern, and declared bounded use before proposing a durable ontic. If a durable ontic is selected, the decision episteme identifies that ontic as its `EntityOfConcern`. |
| `CC-E24-1a` | For every kind or relation included in the durable ontic, the decision states how named direct relations connect it to the primary governed subject kind and core relation, identifies the governing pattern for each direct relation, and names at least one work or decision whose use changes when that coordination is absent. Topic adjacency and a shared label do not satisfy this condition. |
| `CC-E24-2` | Existing governing patterns are checked by value before a new ontic is selected. |
| `CC-E24-3` | The ontic-introduction decision states stable identity criteria and says what does and does not change identity. |
| `CC-E24-4` | A durable ontic names its core direct relation kind, relation-participant meanings, admitted actual-participant kinds, obtaining condition, occurrence-identity rule, and direct governing pattern. A RelationSignature and SlotSpecs are added only when a receiving use needs reusable participant typing. |
| `CC-E24-4a` | When constructive grounding is claimed, the text names the direct grounding rule. Structural identity claims use the `E.14 -> B.3.5 -> C.13` chain with Working-Model, `tv:groundedBy`, and `Γ_m`; non-structural ontics use the identity, grounding, or recognition rule of their governing pattern. |
| `CC-E24-4b` | Ontic introduction creates no project-side relation occurrence. A designator designates and a governed reference resolves only after the direct predicate and identity rule reidentify the occurrence; an assertion or description episteme carries the claim and designation. A publication occurrence makes a selected episteme edition available and neither designates nor creates the world-side occurrence. |
| `CC-E24-5` | The ontic-introduction decision states the primary governed subject kind, stable identity criterion, core direct relation and governing pattern, neighboring direct relations, the reliance basis of each named dependent pattern, existing-pattern reuse, and non-use boundary by value. E.10.ARCH wording-restoration coordinates remain in the source-to-use trace when that restoration opened the case, and the E.8 pattern nest remains publication placement; neither becomes a component or identity criterion of the ontic. |
| `CC-E24-5a` | The pattern keeps ontic identity, direct relation occurrence, `RelationSignature`, `SlotSpec`, actual participant, participant designation, claim-bearing episteme, publication occurrence, publication form, presentation carrier, `U.View`, C.29 representation, and neighboring direct relations distinct. |
| `CC-E24-5b` | An encountered card, table, schema, diagram, file, or record is classified by the governed use that is current: filled claims can identify an episteme, reusable arrangement can be a publication form, selected elements can participate in a C.29 representation, and an identified `U.PresentationCarrier` can bear the form. Visible shape and field co-occurrence decide none of those uses. Only a `U.System` performs description, rendering, or publication work. |
| `CC-E24-5c` | Mathematical operands, tuple components, nodes, and edges remain C.29 representation elements. A correspondence to a relation object neither identifies the two nor contributes to world-side occurrence identity. |
| `CC-E24-6` | Draft ToC rows and planned pattern labels remain non-governing. Until a current governing pattern is written, a bounded local episteme carries only its stated claims for its declared use; for every governed entity and direct relation, those claims identify the current pattern that governs it. |
| `CC-E24-7` | A bounded local episteme remains a `U.Episteme` under C.2.1, not a newly minted U-kind or durable ontic; its claims point each governed entity and relation to the direct governing pattern. |
| `CC-E24-8` | The selected name passes `F.18`; the name does not hide a second ontology or one umbrella for several kinds. |
| `CC-E24-8a` | Durable `U.*` names, reusable SlotKind heads, dependent-kind names, publication-form names, public ids, Core-facing heads, and cross-context labels use `F.18`; `F.17 UTS` and Name Card material is opened only when that name becomes public, Core-facing, or cross-context, and never replaces `A.6.5` SlotSpec discipline. |
| `CC-E24-8b` | A `U.*` spelling, type or kind wording, structural heading, title, filename, or ToC row that claims U-kind force is governed by `E.24.UK` before naming patterns are asked to choose or keep a public term. |
| `CC-E24-9` | Pattern-quality and DRR-adequacy checks stay in `E.21` and `E.9.DA`; they are not copied as user-facing ontic or subject-matter content. |
| `CC-E24-10` | Each named dependent pattern is paired with the identified ontic identity, direct relation rule, or `RelationSignature` declaration on which it relies, and does not duplicate that rule or declaration. |
| `CC-E24-11` | A declaration-local SlotKind names one relation-participant meaning inside its RelationSignature and does not create another ontology. `U.Role` is a work-facing role value, not a SlotKind in a RelationSignature. A role-assignment occurrence uses its own direct relation pattern and RelationSignature under A.2, A.2.1, and A.15. |
| `CC-E24-12` | Ontic slot talk uses slot-language (`onticSlotRelation`, `RelationSignature`, `SlotSpec`, `SlotKind`, `ValueKind`, `refMode`, `RefKind`, slot discipline, slot boundary, relation boundary); `interface` is used only when a governing boundary, module, signature, mechanism, or architecture pattern makes interface meaning current. |
| `CC-E24-13` | Source-ontology annotation is proportional: decision-changing kind, slot, relation, admissible-use, and governing-pattern differences are recovered, while stable domain prose is not expanded into type labels. When a source expression affects the decision, the exact expression, source episteme, any current source publication occurrence, content carried forward, current admissible use, and smallest stronger-use condition remain recoverable. |
| `CC-E24-14` | When candidate detection, publication-side object distinction, or contested evaluation is current, apply `E.24.CD`, `E.24.PUB`, or `A.19.ECS` respectively; E.24 itself stays centered on the primary governed subject kind, U.Ontic identity, core direct relation, governing patterns, named dependent-pattern reliance, and non-use boundary. |

### E.24:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Shadow-kind by repetition | The same claim-bearing episteme or reusable publication form appears in several patterns and starts being cited as an ontology object. | Apply E.24; either write a durable ontic pattern or keep the coordination in a bounded local episteme under C.2.1. |
| Draft ToC row as authority | A ToC row is cited as if it supplied current governing text. | Treat it as an investigation cue only; use current governing patterns until the pattern exists. |
| Slot list without identity | A pattern lists record fields as if they were SlotSpecs but never states what identifies the proposed ontic. | Add stable ontic identity criteria and the direct relation, or keep the claims and references in a bounded local episteme under C.2.1 without proposing a durable ontic. |
| Pattern nest as ontology | A numbering or placement group is treated as the governed subject. | Name the primary governed subject kind, core direct relation, and governing patterns; keep the pattern nest as publication and specialization placement under E.8. |
| New name as solution | The repair invents a smoother term while the typed values remain mixed. | Recover the primary governed subject kind, core direct relation, neighboring direct relations, and governing patterns first; name only after the ontology is settled. |
| SlotKind label becomes participant kind | A declaration-local SlotKind is reused as the world-side participant's kind. | Keep the participant under its direct governing pattern and keep the SlotSpec inside the separate RelationSignature declaration. |
| Interface metaphor for slots | A relation-participant meaning, SlotSpec, assertion-side participant designation, or participant-kind constraint is called an interface without a governing interface pattern. | Use the named direct-relation or declaration term unless a boundary, module, signature, mechanism, or architecture pattern makes interface meaning current. |
| Typed paraphrase overload | A readable subject sentence is rewritten as a full chain of kinds, slots, and source-ontology labels without changing the claim. | Keep the subject sentence and annotate only the decision-changing slot or value under decision. |

### E.24:9 - Consequences

- FPF can introduce rich ontology units without treating every bounded local episteme as a new durable ontic.
- Draft ToC rows and planned pattern labels stop acting like current governing patterns.
- Dependent patterns can rely on the ontic-governing pattern and its named direct-relation patterns instead of reconstructing those rules locally.
- Selecting a durable ontic has an ongoing maintenance consequence: a change to the primary governed subject kind or core relation semantics reopens the ontic-introduction decision and may affect dependent patterns. The bounded-local-episteme and direct-use outcomes avoid that cost when no durable coordination is needed.

### E.24:5.7 - Rationale

FPF needs a pattern for ontic introduction because many important ontology units require several direct relation patterns to remain coherent. The repair is not to make one record-shaped episteme whose fields stand in for every nearby object. It is to give the ontic stable identity, state its core direct relation, reuse named neighboring direct relations, and add RelationSignature declarations only where dependent uses need them.

`U.Episteme` is the main stress case. C.2.1 identifies one episteme through claim content, an identified EntityOfConcern, and an effective reference scheme, then governs empirical grounding and edition continuation through separate direct relations. A `RelationSignature` may declare SlotSpecs corresponding to those relation-participant meanings for repeated use without becoming an episteme or direct relation occurrence. A completed card can itself be a claim-bearing episteme; its reusable arrangement can be a publication form; a publication occurrence can make one selected card-episteme edition available; and a presentation carrier can bear the form. None of those publication-side relations constitutes the episteme or makes its claims true.

Role assignment is the second stress case. `U.Role` remains a work-facing role value, and generic `U.RoleAssignment` is a direct relation occurrence with exactly four participants: an admitted `U.System` holder, one `U.Role` value, the identified role-taxonomy episteme, and the effective `U.ReferenceScheme`. A.2.1 states obtaining and occurrence identity; its `RelationSignature` declares four SlotSpecs corresponding to those four relation-participant meanings for repeated assertion and reference use. `AssignmentInterval` belongs to an assertion or occurrence description. A selected `BoundedModelUseStructure` belongs to the receiving assertion or use unless a separately governed narrower relation kind makes it a required participant and states the stronger predicate.

This preserves ontology compactness without inventing a new kind for every participation name. Use `U.Role` only for a work-facing role value assigned to an admitted `U.System`. For another relation-participant meaning, the direct relation pattern states that meaning and the admitted actual-participant kind; a reusable `RelationSignature` may declare the corresponding SlotKind without changing the actual participant's kind.
Without E.24, FPF ontology development oscillates between two bad moves. One move invents a new umbrella name and leaves the mixed ontology intact. The other refuses the new name but still leaves several patterns carrying duplicated local slot doctrine. E.24 gives a bounded authoring decision: use an existing governing pattern, introduce a durable ontic, state only the needed claims in a bounded local episteme under C.2.1, or keep the source expression quote-only or reduced-use.

The pattern is deliberately about the introduction decision. It does not define every ontic and does not become a registry of system, episteme, method, mechanism, architecture, source, quality, temporal, dynamics, or change objects. Each accepted subject matter still needs its own governing pattern; a bounded local episteme may carry claims for one declared use but does not govern the ontology.

### E.24:5.8 - SoTA-Echoing

E.24 does not claim to replace ontology engineering, OWL-style formal ontology, or UFO-style foundational ontology. Its governing reason is the current FPF need for action-facing ontology compactness, plus a narrow SoTA echo:

| Source family | Current lesson for E.24 | FPF decision |
| --- | --- | --- |
| W3C [SKOS Reference](https://www.w3.org/TR/skos-reference/), 2009, and W3C [OWL 2 Primer](https://www.w3.org/TR/owl2-primer/), 2012. | Reference-baseline use, not a current-best SoTA claim: SKOS remains useful for controlled vocabularies, labels, broader and narrower relations, and concept schemes; OWL remains useful for classes, properties, individuals, axioms, and declarative semantics. | Adopt as baseline and adapt: do not present FPF ontology as one taxonomy tree. Use taxonomy relations where they fit, but introduce an ontic only when stable identity and typed slot relation are required. Current competitive guidance comes from the 2024-2026 modular ontology, interoperability, process-representation, and foundational-ontology rows below. |
| Modular ontology design patterns, MODL/MOMo, and commonsense ontology micropatterns, including [Shimizu and Hitzler 2024](https://arxiv.org/abs/2411.09601) and [Eells, Dave, Hitzler, and Shimizu 2024](https://arxiv.org/abs/2402.18715). | Current ontology-engineering work emphasizes reusable small ontology structures and pattern libraries, including LLM-assisted ontology engineering where modularity becomes more important, not less. | E.24 adapts the modular-pattern lesson: a durable ontic is a reusable FPF ontology unit with a pattern governing its direct relation set and with each dependent pattern paired to its exact reliance basis, not a local checklist copied across patterns. |
| [Qiang 2025, revised 16 June 2026 (v12)](https://arxiv.org/abs/2507.12311). | Overlapping and conflicting concepts block interoperability; the proposed framework combines design patterns, matching and versioning, and validation across the ontology lifecycle. | E.24 prevents shadow ontology and type explosion before matching and versioning becomes a rescue operation. It asks whether a proposed ontology unit becomes a durable ontic, is already governed by existing patterns, stays only as claims in a bounded local episteme, or is not admitted for use. |
| [Norouzi, Hertling, Waitelonis, and Sack 2025 process-representation ODP work](https://arxiv.org/abs/2509.23776). | Process ontologies and workflow ontologies often contain implicit design patterns; reuse suffers when those patterns are not explicit and accessible to domain experts. | Adopt as a caution for any process-like or temporal subject: a bounded local episteme carries only the claims and references needed for one use; reusable process, method, work, or temporal ontology stays explicit. If such material needs a durable ontic, state its direct relation kinds, participant meanings, obtaining and occurrence-identity rules, and governing patterns. |
| [Almeida, Guizzardi, Sales, and Fonseca 2026 gUFO](https://arxiv.org/abs/2603.20948); UFO and OntoUML role, relator, situation, and high-order type practice. | Current foundational-ontology work uses type typology, reification of intrinsic and relational aspects, situations, and high-order types to avoid naive taxonomic flattening. | Use as a stress comparator. Keep role assignment, relation occurrence, RelationSignature, SlotSpec, episteme, publication occurrence, publication form, presentation carrier, view, representation, mechanism, method, and work distinct rather than importing one external taxonomy. |

For the working reader, these rows discipline named parts of the method. The SKOS and OWL baseline bounds taxonomy-only use in `E.24:4.1` and `E.24:5.4`; modular ontology patterns support the reusable ontic and governing-pattern move in `E.24:4.3` and `E.24:4.4`; interoperability work supports the stable-identity and currentness tests; process-representation work disciplines the workflow case in `E.24:5.2`; and gUFO stress-tests the role-assignment separation in the checklist and rationale.

This SoTA echo justifies a bounded conclusion: FPF ontology can remain more compact than a taxonomy-only design when one governed subject needs stable identity, several coordinated direct relations, reusable declarations, and dependent patterns. It does not make every modular ontology pattern an FPF ontic. External source content changes an ontic-introduction decision only when an accepted source-use decision selects it for the subject under concern; current FPF use still depends on the resulting governing pattern.

Use external sources when one ontic or subject matter itself depends on a source tradition. Put that source decision in the DRR and in the governing pattern for that subject matter. Do not make E.24 carry a borrowed external theory of every durable ontic.

#### E.24:5.9 - Currentness and Lowering Logic

Treat E.24 as current for ontic-introduction decisions while the governing patterns for relation-occurrence identity, reusable relation declarations, episteme identity, U-kind admission, wording-use restoration, and durable naming preserve the boundaries used here. Reopen one subject's ontic-introduction decision when one of these changes governs that subject:

- a new accepted FPF pattern changes direct relation identity, SlotSpec discipline, `EntityOfConcern` discipline, U-kind admission, or durable-name discipline;
- a bounded local episteme begins to be cited as if it governed a durable ontic;
- a planned pattern label acquires current governing pattern text and changes the ontic-introduction decision;
- dependent patterns start copying direct-relation rules or `RelationSignature` declarations instead of relying on their governing patterns;
- external source work governs the introduction method itself rather than one selected ontic or subject matter.

Do not let an unresolved decision govern dependent use. When the ontic-introduction decision remains unresolved among the four closed dispositions—a durable ontic, a bounded local episteme under C.2.1, existing governing-pattern use, or source-expression-only use in its quote-only or reduced-use mode—return to `E.24:4.1` and settle the primary governed subject kind, stable identity criterion, core direct relation, named neighboring direct relations, governing patterns, and non-use boundary.

### E.24:8 - Relations

- **Builds on:** `A.6.REL` for direct relation occurrence identity; `A.6.0` and `A.6.5` for reusable `RelationSignature` and `SlotSpec` declarations; and `C.2.1` for decision, assertion, and description epistemes.
- **Coordinates with:** `E.8` for pattern publication placement, `E.10` and `E.10.ARCH` for wording-use restoration, and `F.18` for durable naming after ontology is settled.
- **Coordinates with:** `E.24.CD` for candidate detection before the ontic-introduction decision, `E.24.UK` for U-kind admission, and `E.24.PUB` for ontic-description and publication distinctions.
- **Coordinates with:** `E.17.0` for `U.View` membership, A.6.3 for optional viewing construction, `C.29` for mathematical representation, and the `E.14 -> B.3.5 -> C.13` chain for structural constructive grounding. Each ontic-introduction decision names any additional subject-specific governing patterns instead of treating this relation list as a registry.
- **Coordinates with:** `A.19.ECS` for contested comparison of candidate dispositions, `E.9` and `E.9.DA` for recording and evaluating the authoring decision, and `E.21` for evaluating the resulting pattern. Those evaluation results do not become part of the selected ontic.
- **Used by:** FPF authors when repeated relation and declaration material may need one durable ontic rather than direct governing-pattern use or claims coordinated only inside a bounded local episteme.

### E.24:End

