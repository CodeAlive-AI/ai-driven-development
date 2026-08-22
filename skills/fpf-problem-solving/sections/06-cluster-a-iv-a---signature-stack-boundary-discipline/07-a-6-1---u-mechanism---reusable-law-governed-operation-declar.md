## A.6.1 - U.Mechanism - Reusable Law-Governed Operation Declaration

> **Status:** Stable

**Pattern kind.** Ontic declaration pattern.

**Builds on.** A.6.0 for signature identity and content, C.2.1 for episteme identity, and A.2.6 for claim scope.

**Coordinates with.** A.6.REL for relation occurrences, A.6.RCD for the lightest honest comparison claim, A.6.5 for RelationSignature SlotSpec discipline, C.3 for local operation ValueKinds, A.1 for holon recognition, A.3.1 for Methods, A.15.1 for performed Work, F.9 for exact cross-scheme sense correspondence, C.2.1 for the separate claim that one Bridge suits one bounded use, A.10 for ordinary reliance on that claim, B.3 only for an actual named assurance claim, CHR for selected `CHR:ReferencePlane` values, A.1.1 and A.22 for a selected `BoundedModelUseStructure`, C.29 for mathematical-lens use, E.20 for mechanism introduction, E.24.PUB for publication, A.22.CGUS for a constraint-governed potential-continuation structure and its separate case results, and G.11 for currentness.

### A.6.1:1 - Problem frame

An engineer needs a reusable declaration of operations, their typed argument and result positions, the laws they preserve, and the conditions under which an operation is admitted. The declared operation family may be used for physical modeling, clinical calculation, selection, normalization, or another named engineering use.

Use this pattern when the working question is:

> What operation family is being declared, which laws govern it, and under which claim scope, time, selected `CHR:ReferencePlane`, and mechanism conditions may its operations be used?

**Primary governed object.** One claim-bearing episteme being identified as `U.Mechanism`. Inside that episteme's C.2.1 identity, its exact `EntityOfConcernRef` identifies the declared operation family. `U.Mechanism` is a dependent durable U-kind governed through the `U.Signature` identity and content settlement; it adds operation and admission semantics to the reusable declaration. The operation family does not become the episteme, and the episteme does not become its operation family.

**Primary working reader and concern.** The reader is an engineer who needs to reuse or compare an operation declaration without confusing it with the method that uses it, the entity that realizes it, the work that evaluates it, or a publication that presents it.

The first useful move is to name the declared operation family, its `SubjectKind`, and its family-level `RangedValueKind`, then state its `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, and exact Applicability. Add a family-level `ResultKind` only when one distinct result kind is current. For each reused operation, point to the argument or result meaning that carries the `SubjectKind`, `RangedValueKind`, or `ResultKind` meaning, then declare every additional argument and result meaning and exact ValueKind. Also state the operation's `ApplicationPredicate`, `ApplicationExtentRule`, and `ApplicationIdentityRule`. `ApplicationExtentRule` maps the facts at one independently grounded application locus to the semantically relevant boundary or interval over which that operation's predicate obtains; it is not the signature-level `ExtentRule` that determines kind membership at a selected context slice. Open an actual operation-application binding only when one particular application has been independently identified and a downstream claim says which value that application used or returned. Add a dependency manifest only when removing one named provider term or law would make this declaration uninterpretable or prevent law replay; shared wording or a background citation is not a dependency.

What goes wrong if this pattern is missed: implementation behavior, method instructions, evaluation outcomes, and publication metadata enter the declaration as if they were operation laws. A later user cannot tell whether the declaration changed, one realization failed, or only the evidence became stale.

What this buys: the declaration can remain stable while methods, realizers, evaluations, descriptions, and publications evolve under their own patterns.

Do not use this pattern merely because prose contains words such as mechanism, algorithm, process, or workflow. Recover the current object first. Use A.3.1 when the current object is a semantic way of doing, A.15.1 when it is performed work, and the direct system or episteme pattern when it is a physical assembly or a model description.

### A.6.1:2 - Problem

FPF needs reusable operation declarations for scope, normalization, selection, comparison, physical modeling, and other domains. Without one precise ontic:

1. an operation name does not reveal its typed arguments or result;
2. declared laws are mixed with admission predicates and evaluation outcomes;
3. applicability is hidden behind an unexplained context label;
4. a realization is confused with the declaration it realizes;
5. mathematical notation or imperative prose is overread as an executable sequence;
6. descriptions, publications, methods, and dated work acquire mechanism identity by proximity.

The repair is not a larger declaration form. It is a smaller set of exact distinctions with progressive explicitness.

### A.6.1:3 - Forces

| Force | Tension |
|---|---|
| Reuse and semantic locality | Reusers need stable operation meaning, while every use has an effective `U.ReferenceScheme` and bounded Applicability. |
| Law and admission | Laws state reusable regularities; admission predicates decide whether one proposed operation use is admissible. |
| Declaration and realization | A declaration can have several realizers; changing one realizer does not by itself change declaration identity. |
| Light use and typed reuse | One readable operation sentence is often enough, while repeated use may need exact argument and result declarations; a receiving claim about one use may additionally need a particular application and its bindings. |
| Domain breadth and kind precision | The same form serves physical engineering, medicine, learning, and software without treating code or documents as the default object. |
| Mathematical precision and ontology | Algebraic notation can expose preservation claims, but a mathematical lens does not decide the FPF kind by form. |
| Recall and conditional structure | A short mantra helps a reader remember the distinctions; A.22.CGUS applies only when selected relations and constraints define one reusable structure with at least two potential continuations. |

### A.6.1:4 - Solution

Use `U.Mechanism` as the dependent durable U-kind for a reusable law-governed operation declaration episteme. Identify it through C.2.1. Put operation vocabulary, typed argument and result declarations, application rules, laws, admission conditions, and applicability in its content. Keep each actual application and binding, realizing entity and realization occurrence, method, Work, evaluation, evidence, description, representation, and publication as its own object or relation. Section 4.7 handles each question under the pattern that can identify it.

**Local mechanism mantra.** *Name the operation family and subject. Declare exact arguments, results, application rules, laws, admission conditions, and applicability. Bind actual values only in one independently identified exact application. State a realization relation only when a named realizer satisfies its predicate. Keep method, work, evidence, description, and publication separate.*

This mantra is Plain recall wording. Its imperative grammar creates neither an executable sequence nor a work order. Apply A.22.CGUS only when one independently identified A.22 structure has local loci and at least two potential continuations defined by selected relations and applied constraints. A post-qualification presentation may show one traversal as a separate `DemonstrativeUnfoldingSlice@Context`; a prescribed order of performed work still belongs to the direct method-description or work-plan pattern.

#### A.6.1:4.1 - Admit and identify U.Mechanism

`U.Mechanism` is a dependent durable U-kind governed through `U.Signature` and therefore through `U.Episteme`. Its identity is:

```text
<content, EntityOfConcernRef, effectiveReferenceScheme>
```

The dependence reuses the `U.Signature` identity settlement and subject pattern. It is not parthood and does not make `U.Mechanism` a root beside `U.Episteme`.

Use this early object-and-relation guide:

| Current object | Exact reading |
|---|---|
| `U.Mechanism` | The reusable declaration episteme governed here. |
| declared operation family | The exact subject identified by `EntityOfConcernRef`; its direct kind is preserved. |
| realizing entity | The entity claimed to realize the declaration; it keeps its own direct kind. |
| mechanism-realization relation | The direct relation between the mechanism episteme and a realizing entity under stated scope and time. |
| mechanism description | A C.2.1 episteme about the `U.Mechanism` episteme when such meta-description is actually needed. |
| mechanism publication | An E.24.PUB use that presents the episteme without changing its identity. |

A machine part does not become `U.Mechanism` by being called a mechanism. For example, a pump assembly remains a `U.System`; this pattern defines or constrains a reusable operation declaration to which a realizing entity may be related while retaining its direct kind.

#### A.6.1:4.2 - State mechanism content

The following is a conceptual content outline, not a mandatory record or publication layout. The field and content-group names do not admit new U-kinds, relation kinds, SlotKinds, RefKinds, application records, or work objects.

```text
U.Mechanism content:
  EntityOfConcernRef
  effectiveReferenceScheme
  SubjectKind
  RangedValueKind
  ResultKind?
  SliceSet?
  ExtentRule?
  OperationAlgebra:
    OperationDeclaration*:
      operationDesignator
      ArgumentDeclaration*:
        argumentDesignator
        argumentMeaning
        ValueKind
        bindingDesignationRule
        bindingPredicate
        cardinality?
      ResultDeclaration*:
        resultDesignator
        resultMeaning
        ValueKind
        bindingDesignationRule
        bindingPredicate
        cardinality?
      ApplicationPredicate
      ApplicationIdentityRule
      ApplicationExtentRule
  LawSet
  AdmissibilityConditions
  Applicability
  SignatureManifest?
```

The content components have distinct jobs:

| Content component | Meaning and use |
|---|---|
| `EntityOfConcernRef` | Identifies the exact declared operation family. |
| effective `U.ReferenceScheme` | Supplies the meaning under which the content identifies this episteme. A changed effective reference scheme changes episteme identity. |
| `SubjectKind`, `RangedValueKind`, and optional `ResultKind` | Name the declared subject and value range, plus a distinct result kind when current. No additional container kind is implied. |
| optional `SliceSet` and `ExtentRule` | Use only when membership of the same `SubjectKind` can differ across selected `U.ContextSlice` values. `SliceSet` names those addressable slices; `ExtentRule` maps one selected slice to `Extension(SubjectKind, slice)` by stating how membership is judged there. Leave both out for a time interval, time-varying result, measurement series, operation-application extent, value or result range, arbitrary change function, changing dataset, or claim-bearing mathematical set representation; C.29 is the pattern for the last case. |
| `OperationAlgebra` | Contains one exact `OperationDeclaration` for every reused operation. Each argument and result declaration gives a declaration-local designator, semantic meaning, exact ValueKind, binding designation rule, binding predicate, and any semantic cardinality. The application predicate says what applying that operation means; the extent and identity rules distinguish its particular applications. |
| `LawSet` | States equations, invariants, closure conditions, and other reusable regularities of the declared operations. |
| `AdmissibilityConditions` | States predicates that decide whether one proposed operation application is admitted under current values and conditions. |
| Applicability | Delimits declaration use by exact `U.ClaimScope`, selected time value, selected `CHR:ReferencePlane` when current, and mechanism-specific conditions. Cite `GammaTimePolicy` only when the temporal selection rule matters. When the selected `CHR:ReferencePlane` value is `world`, `WorldRegime in {prep, live}` may distinguish preparation from live use. |
| `SignatureManifest` | Names actual imported and provided declaration content when dependency replay matters. It is not a second U-kind or publication manifest. |

Choose the three headline fields before listing operation positions. In plain terms: name the common kind of thing this operation family is about in `SubjectKind`, and name the common value domain over which the family ranges in `RangedValueKind`. Add `ResultKind` only when one distinct family-level result kind is current. For every operation, point to the argument or result meaning that realizes each current family-level declaration; extra arguments and results keep their own exact ValueKinds. A collection or reference wrapper likewise keeps its own ValueKind and must state how it refers to or contains the family-level kind. If the operations do not share one truthful subject-and-range pair, do not hide that fact in a union, `Any`, or an input or output list: split the declaration or stop. If several result kinds are only operation-local, omit the singular family-level `ResultKind` and keep them in their exact `ResultDeclaration`s.

`OperationDeclaration`, `ArgumentDeclaration`, and `ResultDeclaration` are declaration-content terms, not U-kinds, direct-relation participants, actual values, or records. A `bindingDesignationRule` says whether a binding carries the value itself or one exact governed reference that resolves to it; a stored token or compatible reference does not establish a binding. An operation index may be derived from the operation designators for retrieval, but it is not another semantic content group.

A.6.5 SlotSpecs are not used here. They declare participant meanings only inside a `RelationSignature` for one already governed direct relation kind. A.6.1 argument and result declarations instead govern the named values of an operation application. Mathematical operand order remains a C.29 representation unless an explicit correspondence relates it to these independently declared operation meanings.

Keep neighboring facts outside mechanism identity-bearing content. Cite an F.9 Bridge only when two exact `SchemeSenseCell` values are being related across semantic contexts and its predicate obtains. Cite an actual application binding only when the downstream claim asserts which value the application used or returned. Evaluation, subject participation, evidence use, and realization each require their own obtaining predicate. A new neighboring occurrence or binding does not change `U.Mechanism` identity unless it reveals changed semantic content. A stable designator can refer to a mechanism episteme; file path, publication state, release label, and layout do not enter episteme identity merely because a tool stores them beside the content.

#### A.6.1:4.3 - State meaning and applicability without a generic context slot

Meaning and applicability answer different questions:

- the effective `U.ReferenceScheme` determines how the declaration content is interpreted;
- `U.ClaimScope` identifies the entities and relations to which the current use claim applies;
- the applicability interval states when that use is claimed;
- the selected `CHR:ReferencePlane` states the world, conceptual, or epistemic referent mode when that distinction is current;
- mechanism-specific conditions state assumptions that affect operation admission;
- optional `modelUseStructureRef : U.StructureRef` cites one selected `BoundedModelUseStructure` only when its relations delimit or change mechanism use.

Do not replace these values with one generic context field. Do not add `modelUseStructureRef` merely to preserve an old context column.

When one proposed receiving use spans different local senses, take these steps. First, use F.9 only to test the exact `SchemeSenseCell` correspondence and identify an obtaining Bridge. Second, state a separate current C.2.1 claim about whether that Bridge suits this use, in this direction, under this correspondence rule, and within this loss tolerance; give the claim affirmative or negative polarity. Third, choose the reliance branch from the consequence of the proposed use:

- for ordinary reliance with no actual assurance claim, use A.10. Name the exact evidence-provenance relation, bounded use, unsupported stronger use, window, and reopen or stop condition; proceed only with `RelianceDisposition=pass`;
- when an actual named assurance claim about this use is current, use B.3 and require its result for that same bounded assurance use. A direct domain rule may require the claim, but no Bridge, operation, display, or consequence creates it.

A Bridge, bounded-use claim, or reliance result neither admits an operation application nor says that reuse or Work occurred. A.6.1 `AdmissibilityConditions` still decide whether the proposed operation application is admitted; the actual application and bindings remain under A.6.1, and dated Work remains under A.15.1.

For example, let `BridgeDoseTerms-7` be the obtaining F.9 Bridge between exact cells `WardDoseValueCell` and `ProtocolDoseValueCell` under its exact `BridgePredicateProfile`. The separate C.2.1 claim for reusing the protocol mechanism in the ward-to-protocol prescribing direction is negative because the use rule cannot meet the ward's zero tolerance for changing the dose unit or scale. That reuse stops before reliance. It also stops when the bounded-use claim is absent, when A.10 does not return `RelianceDisposition=pass` for an ordinary bounded use, or, when an actual named assurance claim is current, when B.3 has no `AssuranceResult` for the same use with `disposition=supported-for-use`. None of those outcomes makes the Bridge cease to obtain or makes an operation application admitted or actual.

A changed effective `U.ReferenceScheme` identifies another mechanism episteme through C.2.1. A changed selected `CHR:ReferencePlane` reopens the exact CHR assertion; a changed `BoundedModelUseStructure` requires exact A.1.1/A.22 assertions. If the project also claims that a plane transition or model-use change relation occurred, name its admitted predicate and participants or stop that claim. In every branch, name the exact source and target objects, the comparison or relation actually asserted, and the meaning or structure it preserves and loses. Any reliability claim remains under its direct reliability relation; neither a Bridge nor transition wording alters Formality or Guarantee by itself.

Numeric comparison and aggregation use A.19 and the direct measurement and scale patterns. Orders are declared before arithmetic is applied, units are made compatible before values are combined, and any reduction to one score cites its governing scalarization relation.

#### A.6.1:4.4 - Separate laws, admission, evaluation, and evidence

`LawSet` states regularities of the declared operations. `AdmissibilityConditions` decide whether one proposed application may proceed under current values and declared conditions. If a mechanism uses `admit`, `degrade`, or `abstain`, those are declared application dispositions with declared effects; they are not automatically the operation's result algebra.

A recognition-evaluation operation declares its own finite result value `true | false | unknown`. It returns `true` when its governed bound argument values determine that the candidate satisfies the selected world-side criterion, `false` when they determine that the candidate fails it, and `unknown` when missing evidence or an unavailable dependency prevents either determination. `unknown` is neither `false`, non-obtaining, a third candidate state, nor a receiving-work disposition. One admissible application can therefore return `unknown`.

World-side satisfaction or failure follows the direct criterion and candidate facts whether or not the project can currently determine them. Measurements, evidence, and assurance may support or warrant claims about those facts or about the returned judgment. If an exact evidence or interpretation-basis episteme is also a declared operation argument, its actual binding establishes only that the application used that value under the declared argument meaning. It does not make the criterion true, make the evidence correct, or constitute the candidate.

A separately materialized evaluation-result or classification-assertion episteme remains under C.2.1. Its claim content may state the returned value, while exact evidence and assurance relations govern support or warrant and G.11 governs edition currentness. Neither the episteme nor its currentness is the operation result value itself. Thus a mechanism realization may obtain while current evidence is insufficient to rely on it, and an evaluation may return a value without changing mechanism identity.

#### A.6.1:4.5 - Bind one actual operation application exactly

Use the readable direct forms first:

```text
During exact application P of declared operation O, value V is bound under argument declaration a.
Exact application P returns value R under result declaration r.
```

A particular application is an occurrence of the `ApplicationPredicate` declared for exact operation O. The exact operation declaration supplies the application identity and extent rules; the phrase *operation application* does not admit a public `OperationApplication` U-kind, one universal application relation kind, or a work record. Its identity rule must name the semantically relevant application locus and boundary: for example, one physical cycle, one calculation invocation from call to return, or one comparison act from selected operands to returned judgment. If none of those examples fits, name the domain event that starts and ends the application. A trace identifier can designate that occurrence but cannot identify it by storage convention alone. If the declaration supplies no truthful application predicate, extent rule, or identity rule at the granularity required by the receiving claim, the actual application is blocked rather than reconstructed from a method name, plan row, log, or nearby result.

An *operation-application binding* is an occurrence of one declaration-local binding predicate under that exact application. Its direct participants are the exact application occurrence and the exact bound entity or value. The exact mechanism episteme and the named argument or result declaration govern the predicate; they are not substituted for the actual value. An argument binding obtains only when the value actually participates in P under the declared argument meaning, resolves under the binding designation rule, satisfies the declared ValueKind and cardinality, and lies within P's governed extent. A result binding obtains only when P actually returns that value under the declared result meaning; type compatibility, a planned filling, a method-description field, a stored reference, or a matching token establishes neither binding.

One binding occurrence is identified by `<exactApplicationOccurrence, exactMechanismEpisteme, operationDesignator, argumentOrResultDesignator, exactBoundValue, maximalContinuousBindingExtent>`. The extent lies within the exact application extent; a result-binding extent cannot begin before that result is returned. Repeated applications remain distinct through their independently governed application identities, and the same value bound under two declaration-local meanings yields two distinct bindings. A declaration may state a different cardinality or binding-continuity rule only when that semantics is part of the exact operation declaration.

The controlled phrase *operation-application binding* names this family of declaration-local binding occurrences; it is not a renamed universal work-participant, input, output, result, evidence, or production relation kind. A result binding says which value the application returned. It does not say that dated work produced or first constituted that entity, that a result episteme exists, or that another claim should rely on it.

A dated performance is a separate Work individual admitted under `U.Work` by A.15.1. When a Work claim also relies on one already identified application and its bindings, identify the Work occurrence independently. Name the admitted performer System `S` and the obtaining assignment `RA`; verify that `S = RA.HolderSystemSlot`, that `RA` covers the attributed Work extent, and that F.6 `performedUnderAssignment(W, RA)` obtains. State the Work temporal extent, at least one obtaining `enactsMethod -> U.Method` relation, any additional enactment relation used by the application claim, and at least one obtaining locally declared A.15.1 Work-to-System containment relation with its exact boundary. Add a work-to-referent relation, performed resource use, continuity policy, or Work mereology only when the claim asserts that relation and its own predicate obtains. A.6.1 does not identify the Work occurrence. If neither a direct subject relation nor a truthful A.6.1 application binding establishes the claimed participation, retain the exact missing-governor blocker.

#### A.6.1:4.6 - State realization as a direct relation

Use the readable direct form first:

```text
Entity E realizes U.Mechanism M for ClaimScope S during interval T.
```

The relation has these positions when typed reuse needs them:

| Relation position | Value kind | Meaning |
|---|---|---|
| declared mechanism | `U.Mechanism` | The declaration whose operations and laws are current. |
| realizing entity | `U.Entity` or a narrower direct kind | The entity claimed to realize the declaration; its direct kind remains unchanged. |
| realization scope | `U.ClaimScope` | The exact entities and relations for which the realization claim is made. |
| derived realization extent | temporal interval | The maximal continuous interval over which the realization predicate obtains; this is an identity contribution, not a writable participant. |

The realization predicate obtains when the realizing entity provides the declared operations and preserves the declared laws for admitted uses in the stated scope and interval. A refined mechanism declaration may narrow Applicability or strengthen laws or admission conditions only with the preserved and changed semantic content stated explicitly. The realizing entity realizes the exact mechanism episteme named in the relation; it neither creates nor constitutes a refinement or edition relation. A claimed realization is lowered when it relaxes a declared law, bypasses an admission condition, or relies on undeclared operation meanings.

The non-derived participants are the declared mechanism, realizing entity, and realization scope. When a later use needs one occurrence distinguished from another, its direct identity is `<declaredMechanism, realizingEntity, realizationScope, maximalContinuousRealizationInterval>`. The interval is derived as the maximal continuous interval over which the realization predicate obtains. A new evaluation window or a gap in available evidence does not split the occurrence; demonstrated cessation followed by later realization does.

Ordinary use stops at the readable sentence. If another claim must refer to or compare one realization occurrence, the direct relation pattern and A.6.REL govern explicit occurrence identity. Evidence, evaluation, application, and binding occurrences remain supporting or use-side neighbors rather than realization participants.

#### A.6.1:4.7 - Keep mechanism, application, method, work, and description questions separate

One project concern can need several linked values. Recover each by its working question:

| Working question | Governing object and pattern |
|---|---|
| What reusable operation declaration is current? | `U.Mechanism` under A.6.1. |
| What particular operation application and actual argument or result values are current? | The exact declaration-local application and operation-application binding occurrences under A.6.1. |
| What semantic way of doing is selected? | `U.Method` under A.3.1. |
| What episteme describes that method? | `U.MethodDescription` under A.3.2. |
| What work is intended? | `U.WorkPlan` under A.15.2. |
| What dated work occurred? | One Work occurrence admitted under `U.Work` by A.15.1. |
| What entity realizes the mechanism? | The entity's direct kind plus the mechanism-realization relation in A.6.1. |
| What supports a claim about admission, application, result, or realization? | Domain-local evaluation, measurement, evidence, assurance, and currentness relations under their direct patterns. |
| How is the mechanism represented or published? | A.6.3, A.6.3.RT, and E.24.PUB. |

A MethodDescription may cite a mechanism declaration. An independently established selector result or one actual A.6.1 application may select a Method, and a direct constraint relation may constrain one; the mechanism declaration does not act merely by being named. An operation declaration may type a `U.Method` as an argument or result only when that is the operation's declared meaning; one actual application may then bind a Method value. Neither the declaration nor binding establishes a planned assignment, actual `enactsMethod`, or dated Work occurrence. One Work occurrence admitted under `U.Work` may enact the Method; the claim about that occurrence may cite the independently identified application and bindings under A.15.1. Performer assignment, extent, locally declared containing-system relations, resources, affected referent, continuity, and neighboring result or effect claims must each be established separately.

#### A.6.1:4.8 - State exact comparison claims among mechanism declarations

State a mechanism-declaration comparison only when its predicate is defined and the case facts satisfy it. A relation label alone admits neither a relation kind nor an occurrence.

| Current comparison claim | Exact preservation test |
|---|---|
| refinement | Preserves the inherited operation, argument, result, application, and binding meanings selected by the claim; states every narrowed Applicability or strengthened law or admission condition; and makes no substitution claim outside the retained applicability. |
| conservative extension | Adds exact operation declarations or declared optional arguments or results while preserving the meanings, application predicates, identity and extent rules, laws, and admitted uses of inherited operations. |
| equivalence | Supplies an explicit mapping that preserves and reflects the selected operation declarations, argument and result meanings, binding meanings, application predicates, identity and extent rules, and law and admission structure. |

These rows test declaration content; they do not admit a relation kind or occurrence. If the corpus already admits the exact comparison relation, use its direct pattern. If one case-specific comparison claim is enough, use A.6.RCD disposition 2 only after its exact claim subject, constructor, endpoint facts, and preservation facts are recoverable; otherwise return A.6.RCD's exact missing-substrate or missing-governor result. When the same predicate must be reused across cases, apply A.6.RCD's reusable predicate-definition branch. If a downstream use instead needs comparison occurrences with their own identity and no relation kind has been admitted, return `missing-governor[mechanism-comparison-occurrence]`; a label such as *refinement* or the adjective *direct* does not fill that gap.

In every branch, identify the exact endpoint mechanism epistemes, their effective `U.ReferenceScheme` values, claim scope, comparison predicate, and preserved and changed semantic content. Changed C.2.1 identity discriminators identify another episteme. If historical continuation matters to the comparison or receiving use, test the separate `EpistemeEditionRelation(earlierMechanismEpisteme, laterMechanismEpisteme)` under C.2.1. The two endpoint epistemes remain distinct participants; refinement, extension, equivalence, a shared name, or a later date establishes neither that relation nor one continuing episteme.

**Continuing revision and replacement contrast.** `FixtureSelectionMechanism-R2` has changed claim content relative to `FixtureSelectionMechanism-R1`, so it is another mechanism episteme. In the continuing branch, the exact source use and the applicable continuity rule identify which claim, EntityOfConcern, and scheme features must be preserved or may deliberately change; the current facts satisfy that rule. Revision Work, Method, provenance, and change facts supply evidence for the test but no label makes continuity true. `EpistemeEditionRelation(FixtureSelectionMechanism-R1, FixtureSelectionMechanism-R2)` then lets G.11 follow the lineage to the later episteme, but every current application and realization claim is still re-evaluated against R2's own applicability and laws; an R1 realization does not automatically realize R2. In the replacement branch, `FixtureSelectionMechanism-Alt1` has another C.2.1 identity and no obtaining edition relation to R1. Treat it as an independent declaration: carry forward neither R1 currentness nor its realization claims, and compare or select Alt1 only through its own applicability and an exact comparison predicate.

`transport` is not a generic A.6.1 mechanism relation. If the current question is cross-context `SchemeSenseCell` correspondence, identify the two exact F.17 cells, test the direct F.9 predicate, and cite a Bridge only when it obtains; infer neither mechanism identity nor equivalence from it. A changed effective reference scheme identifies another episteme; changed `CHR:ReferencePlane` or model-use organization requires its subject pattern. Compare mechanism content only after those exact endpoints and relations have been recovered.

Quotient, product, categorical morphism, and similar constructions are mathematical-lens claims under C.29 when they are current. The lens states which mechanism content is preserved and lost. Mathematical notation does not create an application, binding, realization occurrence, or mechanism U-kind by form.

#### A.6.1:4.9 - Keep description, representation, and publication separate

`U.Mechanism` is already an episteme. A second episteme that explains, summarizes, or compares it is a C.2.1 meta-description whose `EntityOfConcernRef` identifies the mechanism episteme. A diagram, equation set, program, or table is a representation governed by A.6.3 and A.6.3.RT when representation transition matters. An E.24.PUB publication relation makes one selected episteme edition available; an information-carrier relation may carry that publication, but neither relation becomes the mechanism episteme.

A grouping of several mechanism epistemes and realizations may be selected as a `U.Structure` or shown through a `U.View` when that structure or view is current. The grouping does not admit another root kind by itself.

#### A.6.1:4.10 - Use progressive explicitness

Use five degrees of explicitness:

1. A direct sentence names one operation and its condition clearly enough for present work.
2. A `U.Signature` is identified when reusable vocabulary, laws, or applicability matter.
3. A `U.Mechanism` is identified when reusable operation and admission semantics matter.
4. One particular application and its exact argument or result bindings are identified only when a downstream claim asserts that the application occurred or that one exact value participated or was returned.
5. A mechanism-realization relation occurrence is explicitly individuated only when another claim relies on that occurrence identity.

These are thresholds of explicitness, not a continuation structure. If entries, branches, returns, or stops form one reusable structure, apply A.22.CGUS only after its A.22 identity, local loci, selected relations and constraints, and potential continuations are recoverable.

#### A.6.1:4.11 - Change the exact object that changed

When mechanism content, `EntityOfConcernRef`, or the effective `U.ReferenceScheme` changes, identify another `U.Mechanism` episteme under C.2.1. A changed operation, argument or result declaration, application predicate, application identity or extent rule, law, admission predicate, applicability claim, or relied-on dependency therefore changes the declaration episteme when its semantic content changes.

Call that later episteme an edition of an earlier mechanism episteme only when the exact C.2.1 `EpistemeEditionRelation` obtains. With that relation, G.11 may follow the lineage to discover the later declaration and then re-evaluate its applicability, applications, bindings, and realizations. Without it, keep the later declaration as a non-continuing replacement and open those current-use and realization questions independently. A shared label, refinement claim, later publication, or changed filename supplies no continuity.

A new particular application or binding, new realizer, failed evaluation, new evidence item, changed work occurrence, returned value, or new publication does not change the mechanism episteme by itself. Repair that neighboring object and the affected relation. Reconsider the declaration only when the change overturns relied-on mechanism-content semantics.

Use E.20 when introducing a new mechanism declaration or changing the governing assignment of mechanism semantics. Use G.11 when the question is currentness, freshness, selection of a continuing later episteme, or decay of a relied-on declaration or cited source episteme.

### A.6.1:5 - Archetypal Grounding

#### A.6.1:5.1 - Physical modeling: thermal connector operations

A physical-modeling team repeatedly uses a thermal connector operation family. The mechanism episteme declares named temperature and heat-flow argument and result meanings with their exact ValueKinds, connection operations, equality and conservation laws, application identity and extent rules, and admission conditions for unit compatibility and steady-state conduction. Applicability names a `U.ClaimScope` over the modeled systems, the use interval, selected `CHR:ReferencePlane = conceptual` for these model-side connector claims, and the steady-state conduction condition; a component port is a modeled participant or locus, not a `CHR:ReferencePlane` value.

One equation-based model can realize that declaration for simulation use. The modeled heater and pipe remain physical systems. Solver work, validation measurements, and a connection diagram remain work, evidence, and representation under their own patterns.

Practical payoff: another model can be compared against the same operation and law declaration without treating equation order, solver choice, or a diagram as mechanism identity.

#### A.6.1:5.2 - Clinical work: dose-adjustment operations

A clinical team declares a dose-adjustment mechanism over one common patient subject and one common dose-value domain. The headline fields and the heterogeneous operation positions connect as follows; every named ValueKind must already resolve under the effective reference scheme, and this example admits no new U-kind.

| Declaration locus | Filled value and connection |
|---|---|
| `SubjectKind` | `Patient`; required argument `patient` has `ValueKind = Patient` and identifies the patient for whom one calculation is proposed. |
| `RangedValueKind` | `DoseValue`; required argument `currentDose` has `ValueKind = DoseValue`, and the LawSet states the dose bounds and unit-preserving rules over that domain. |
| optional `ResultKind` | `DoseRange`; result `proposedDoseRange` has `ValueKind = DoseRange`. This field is present because the returned range is not one `DoseValue`. If the operation instead returned one `DoseValue`, omit the separate `ResultKind`; if several operations returned unrelated local kinds, keep those kinds in their own result declarations rather than forming a union. |
| other operation-local arguments | `drug : Drug`, `patientMass : MassValue`, and `renalFunction : RenalFunctionMeasure`; these exact ValueKinds constrain this operation but do not replace or widen the family-level subject and range. |

Admission conditions state which measurements and qualification intervals make one calculation admissible. Applicability names the patient-population `U.ClaimScope`, qualification interval, selected `CHR:ReferencePlane` (normally `world` for the patient-side use claim), and clinical conditions under which the declaration is used.

An exact claim-bearing clinical-protocol episteme is a `U.MethodDescription` only when it describes one admitted `U.Method` and satisfies A.3.2; its publication form and carrier remain separate. One clinician's treatment occurrence is work only when the A.15.1 occurrence basis obtains. Exact laboratory measurement values may be bound as arguments of one admitted calculation application, while the measurement and evidence relations that warrant their use remain separate. The returned dose-range binding does not say that the calculation produced or constituted the patient, prescription, or result episteme. None of those neighboring values becomes the mechanism episteme.

Practical payoff: a changed protocol presentation or one anomalous treatment does not silently rewrite the declared calculation laws.

#### A.6.1:5.3 - Manufacturing: fixture selection

A machining team declares a fixture-selection mechanism. Its operations filter candidate fixtures, compare admissible loading envelopes, and return a non-dominated candidate set. Laws preserve units and the partial order over constraints. The admission predicate evaluates true only when current workpiece geometry, machine envelope, and measurement qualification interval are available.

The machinist's setup method and the dated setup work remain separate. A fixture is a system. A selector implementation may realize the mechanism for a stated scope and interval.

**Positive realization in plain terms.** `FixtureSelectorRuntime-12-E3` realizes exact mechanism episteme `FixtureSelectionMechanism-E3` for `Cell7FixtureSelection-Q3` during `[2026-07-01T08:00Z, 2026-07-19T14:32Z)`. During that interval the independently identified runtime provided `filterCandidates`, `compareLoadingEnvelopes`, and `returnNonDominatedSet`; every admitted use required current workpiece geometry, the current machine envelope, and a current measurement-qualification interval; and its results preserved the declared unit and constraint-partial-order laws.

| Realization position or test | Filled value |
|---|---|
| declared mechanism | `FixtureSelectionMechanism-E3 : U.Mechanism`, the exact mechanism episteme containing those operations, laws, admission conditions, and Applicability |
| realizing entity | `FixtureSelectorRuntime-12-E3 : U.System`; the runtime keeps its system kind |
| realization scope | `Cell7FixtureSelection-Q3 : U.ClaimScope`, covering fixture selection for machining cell 7 under the named machine-envelope and qualification conditions |
| realization predicate | the runtime provides all three declared operations, enforces `GeometryCurrent`, `MachineEnvelopeCurrent`, and `MeasurementQualificationCurrent` before an application is admitted, and preserves `UnitPreservationLaw` and `ConstraintPartialOrderLaw` in returned candidate sets |
| derived extent | the maximal continuous interval `[2026-07-01T08:00Z, 2026-07-19T14:32Z)` over which those facts obtain |

This replay needs one occurrence distinguished from its failing successor, so its identity is `<FixtureSelectionMechanism-E3, FixtureSelectorRuntime-12-E3, Cell7FixtureSelection-Q3, [2026-07-01T08:00Z, 2026-07-19T14:32Z)>`. The interval is derived, not a fourth writable participant.

**Nearest failing variant.** `FixtureSelectorRuntime-12-FastPath-E4 : U.System` exposes the same three operation names but accepts a loading-envelope comparison when `MeasurementQualificationCurrent` is false. It therefore bypasses one declared admission condition and does not realize `FixtureSelectionMechanism-E3` for that scope, even if its returned candidate set happens to match E3 in one run. A missing audit-log segment for E3 instead reopens evidence and warrant under A.10. Without demonstrated cessation or bypass, that gap does not make the world-side realization predicate false or split its occurrence, although the project may have to withhold its positive assertion until warrant recovers. Demonstrated cessation followed by later restored conformity would create a later maximal-continuous realization occurrence.

Practical payoff: the team can replace the implementation without turning a scalar convenience score into the declared ordering law, and it can reject a look-alike implementation without rewriting the declaration.

#### A.6.1:5.4 - FPF scope and normalization declarations

A.2.6 scope operations and A.19 normalization operations may use the `U.Mechanism` declaration shape when their direct patterns need reusable operations, laws, admission conditions, and typed results. A.2.6 and A.19 retain their domain semantics. A.6.1 supplies the declaration and realization distinctions; it does not redefine scope or comparison.

Practical payoff: shared mechanism form does not create a second governing locus for scope or normalization meaning.

#### A.6.1:5.5 - Publication operations

E.24.PUB may cite a mechanism declaration for operations that assemble, validate, and expose a publication package. The mechanism episteme declares those operations, laws, and admission conditions. The dated publication work, resulting publication use, information carrier, evidence, and currentness relations remain with their direct patterns.

Practical payoff: reusable publication-operation semantics do not turn a released package or its carrier into the mechanism.

#### A.6.1:5.6 - Reduced ordinary use

An engineer states, "this conversion is admitted only for values in the calibrated interval." No later claim reuses an operation family, compares declarations, identifies an actual application, or refers to a realization occurrence. The direct sentence and its governing characteristic and measurement patterns are enough. No mechanism episteme is opened.

Practical payoff: precision grows only when a receiving use needs reusable mechanism identity or an exact application binding.

#### A.6.1:5.7 - Recognition evaluation: Pump #37

A project repeatedly evaluates the A.1 holon-recognition criterion. In ordinary language, one bounded evaluation act applies the selected criterion to Pump #37 and returns `true`, `false`, or `unknown`. For this replay, resolving `HolonRecognitionMechanism-E1_Ref` under its effective reference scheme returns exact mechanism episteme `HolonRecognitionMechanism-E1`; neither label nor suffix establishes an edition relation. That episteme has `SubjectKind = U.Entity`, `RangedValueKind = RecognitionJudgmentValue`, no separate `ResultKind`, and operation `recognizeAdmittedHolonCandidate`.

The operation declares these meanings:

| Declaration-local meaning | Exact declaration |
|---|---|
| `candidate` argument | one exact `U.Entity` being evaluated |
| `admittedHolonKind` argument | one already admitted holon-kind value whose direct pattern supplies any kind-specific condition |
| `recognitionCriterion` argument | one exact criterion-bearing `U.Episteme`, designated through a governed reference |
| `criterionParameter` argument, repeated only as separately declared | one exact value of the parameter-specific ValueKind needed by this operation application |
| `interpretationBasis` argument | one exact separately identified episteme containing the selected interpretation basis, designated through a governed reference |
| `recognitionJudgment` result | one value of the declaration-local finite `RecognitionJudgmentValue = {true, false, unknown}` |

`RecognitionJudgmentValue` is one local finite `U.Kind` under C.3, used here as the operation's `RangedValueKind`; its membership rule admits exactly the three values shown. It is not a public U-kind, universal claim-status algebra, candidate state, evidence status, episteme-currentness value, or receiving-work disposition. The argument and result rows are A.6.1 declarations, not A.6.5 SlotSpecs.

For this exact mechanism episteme, the declaration-local designation, cardinality, and binding predicates are:

| Member | ValueKind and designation rule | Cardinality | Declaration-local binding predicate |
|---|---|---:|---|
| `candidate` | `U.Entity`; an exact `U.EntityRef` must resolve to the entity | exactly one | `recognitionCandidateBound(P, E)` holds only when application `P` actually evaluates `E` as its candidate |
| `admittedHolonKind` | one already identified C.3 `U.Kind` value, carried by value | exactly one | `recognitionKindBound(P, K)` holds only when `P` evaluates the candidate against admitted kind `K` |
| `recognitionCriterion` | `U.Episteme`; an exact `U.EpistemeRef` must resolve to the selected criterion-bearing episteme | exactly one | `recognitionCriterionBound(P, C)` holds only when `P` applies the claims in `C` as its recognition criterion |
| `criterionParameter[constructionFacts]` | `U.Episteme`; an exact `U.EpistemeRef` resolves to the candidate-facts episteme used by the evaluation | exactly one | `recognitionParameterBound(P, constructionFacts, V)` holds only when `P` uses `V` under that meaning |
| `criterionParameter[reidentificationRule]` | `U.Episteme`; an exact `U.EpistemeRef` resolves to the reidentification-rule episteme used by the evaluation | exactly one | `recognitionParameterBound(P, reidentificationRule, V)` holds only when `P` uses `V` under that meaning |
| `interpretationBasis` | `U.Episteme`; an exact `U.EpistemeRef` must resolve to the selected basis episteme | exactly one | `recognitionBasisBound(P, B)` holds only when `P` uses `B` as its interpretation basis |
| `recognitionJudgment` | `RecognitionJudgmentValue`, carried by value | exactly one | `recognitionJudgmentReturned(P, J)` holds only when `P` returns `J` under this result meaning |

These predicate names are local to `HolonRecognitionMechanism-E1`; they do not admit public binding relation kinds. `Pump_37_Ref` can be type-correct without a binding: the candidate predicate is current only when the exact application actually uses its resolved referent under the `candidate` meaning. The same rule applies to each argument, and a result predicate is current only after the application returns that value.

For this mechanism episteme, `ApplicationPredicate(P)` holds only when bounded evaluation act `P` fixes exactly one value for every required argument above, applies `recognizeAdmittedHolonCandidate` from `HolonRecognitionMechanism-E1`, and returns exactly one `RecognitionJudgmentValue`. Its `ApplicationExtentRule` sets the maximal extent from the moment all required argument bindings are fixed and evaluation begins through the terminal judgment return. Its `ApplicationIdentityRule` reidentifies one application by `<HolonRecognitionMechanism-E1, recognizeAdmittedHolonCandidate, independently grounded evaluation-act locus, maximal application extent>`. A later invocation is another application even with the same bound values. A trace token or reused work label can designate an act but cannot merge the two.

For the worked case, `Pump37RecognitionApplication-2026-07-21T100000Z` designates the evaluation act that began at 10:00:00 and returned at 10:00:04. It used `Pump_37_Ref -> Pump_37 : U.Entity`, admitted kind `U.System`, `A1-Holons-Criterion-E1_Ref`, `Pump37-Construction-Facts-E1_Ref`, `Pump37-Reidentification-Rule-E1_Ref`, and `Pump37-Interpretation-Basis-E1_Ref`. The six argument-binding predicates have maximal continuous extents from 10:00:00 through the terminal return. A required fastening-relation fact could not be resolved during this act, so the bound values could determine neither satisfaction nor failure. The act returned `unknown`; the extent of `recognitionJudgmentReturned(Pump37RecognitionApplication-2026-07-21T100000Z, unknown)` is the terminal return event at 10:00:04 and does not begin earlier. The application did occur; Pump #37's world-side satisfaction or failure did not change; and `unknown` is not an admission refusal.

If the project also claims that dated classification Work occurred, identify a separate Work occurrence `W` under A.15.1. Name the admitted System `S` that performed it and the obtaining assignment `RA` under which it performed; verify `S = RA.HolderSystemSlot`, assignment coverage, and F.6 `performedUnderAssignment(W, RA)`, then state the Work temporal extent, at least one obtaining `enactsMethod -> U.Method` relation, any additional enactment relation used by the classification-work claim, and at least one obtaining locally declared containing-system relation with its exact boundary. The candidate application binding above can establish Pump #37's participation in the application; add a separate work-to-candidate or resource-use claim only when its declared predicate obtains, and add `workContinuityPolicyRef` only when an identity or segmentation question needs it. Any materialized classification-assertion or evaluation-result episteme remains under C.2.1. Evidence and assurance support or warrant its claim content through their own relations, and G.11 tests edition currentness. The result binding alone establishes none of Work, evidence, warrant, episteme identity, world-side criterion satisfaction, or B.2 whole reidentification.

Practical payoff: another evaluation can reuse the same typed operation while binding another candidate or basis, and evidence loss can change the returned value to `unknown` without rewriting the candidate or criterion.

### A.6.1:6 - Bias-Annotation

**Scope declaration:** Universal across FPF-governed domains.

- **Gov.** Favors one direct governing declaration for operation meaning. Counter-risk: every operation becomes a mechanism card. Mitigation: use the progressive-explicitness threshold.
- **Arch.** Favors separate declaration, realization, method, work, and publication relations. Counter-risk: too many linked objects. Mitigation: materialize only objects whose identity or obtaining is asserted or used as a premise.
- **Onto-Epist.** Favors `U.Mechanism` as declaration episteme and preserves the direct kind of its subject and realizer. Counter-risk: the familiar word mechanism is overread as a machine part. Mitigation: the early object-and-relation guide and heterogeneous cases expose the distinction.
- **Prag.** Favors explicit argument and result declarations, application rules, laws, admission conditions, and applicability. Counter-risk: formal apparatus outruns value. Mitigation: ordinary direct statements remain admissible, and an actual binding opens only when a downstream claim asserts which value participated or was returned.
- **Did.** Favors a short mantra and concrete cases. Counter-risk: readers treat imperative recall as execution order. Mitigation: apply A.22.CGUS only to an independently identified potential-continuation structure and keep actual Work or Transformation separate.

### A.6.1:7 - Conformance Checklist

1. **Exact episteme.** One `U.Mechanism` episteme and its exact `EntityOfConcernRef` are recoverable.
2. **Identity.** Content, EntityOfConcern, and effective `U.ReferenceScheme` remain recoverable.
3. **Signature dependence and family-level anchors.** The mechanism uses A.6.0 signature content and adds operation and admission semantics without becoming a second root beside `U.Episteme`. One truthful family-level `SubjectKind` and `RangedValueKind` pair is connected to the exact argument or result meanings that realize those declarations; optional `ResultKind` is present only for one distinct family-level result kind. Additional operation-local ValueKinds remain local. If no common pair exists, split the declaration or stop instead of using a union or generic input or output list.
4. **Typed operation declarations.** Every reused operation has declaration-local argument and result meanings, exact ValueKinds, binding designation rules, and semantic cardinalities when needed. None is an A.6.5 SlotSpec.
5. **Application semantics.** Every claimed particular application has an exact application predicate, identity rule, extent rule, and recoverable occurrence boundary.
6. **Actual bindings.** Every claimed actual argument or returned result has an obtaining declaration-local binding with the exact application and bound value; type compatibility, description, plan, record, or token match is insufficient.
7. **Binding identity.** The application, exact mechanism episteme, operation designator, argument or result designator, bound value, and maximal continuous binding extent distinguish the binding occurrence.
8. **Recognition result.** A recognition-evaluation declaration uses `true | false | unknown` with the A.1 meanings; `unknown` is not false, a candidate state, evidence status, currentness, or receiving disposition.
9. **Law and admission split.** Reusable laws, proposed-application admission predicates, and the operation's own returned value remain distinct.
10. **Exact applicability.** `U.ClaimScope`, time, selected `CHR:ReferencePlane` when current, and mechanism-specific conditions replace generic context wording.
11. **Optional structure.** A model-use structure is cited only when its selected relations delimit or change the receiving mechanism use; it does not replace the effective reference scheme or claim scope.
12. **Dependency truth.** SignatureManifest content names actual imports and provided names only when dependency replay matters.
13. **Realization relation.** A realizer keeps its direct kind; the direct relation declares its participants, obtaining predicate, and maximal-continuous-interval identity rule.
14. **Evaluation and evidence boundary.** Evidence availability can change evaluation or warrant without changing world-side satisfaction; an argument binding establishes use, not truth or warrant.
15. **Method and work boundary.** Method, method description, work plan, dated work, actual application, and binding remain separately identifiable. A.6.1 defines neither dated-work identity nor work mereology.
16. **Result boundary.** A result binding neither produces nor constitutes its bound entity and does not materialize a C.2.1 result episteme.
17. **Mechanism comparison claims.** Every refinement, conservative-extension, or equivalence claim names exact endpoint mechanism epistemes, reference schemes, scope, predicate, and preserved and changed content. Historical continuation is stated only through a separately obtaining C.2.1 `EpistemeEditionRelation`; a comparison or shared label supplies none. The claim uses an already admitted direct relation, the applicable A.6.RCD branch, or the exact missing-governor stop. Generic mechanism `transport` is absent; exact cross-context `SchemeSenseCell` correspondence requires F.9.
18. **Mathematical-lens boundary.** Quotient, product, morphism, operand order, and tuple claims use C.29 when mathematical structure preservation is current.
19. **Progressive explicitness.** One-off direct use is not forced into a mechanism declaration or application-binding apparatus.
20. **CGUS boundary.** Mnemonic imperatives are not called an executable sequence; condition-governed continuation uses A.22.CGUS.
21. **Changed object.** Declaration, application, binding, realization, evaluation, evidence, work, representation, and publication changes return to the object that actually changed.

### A.6.1:8 - Common Failure Modes and Repairs

| Failure | Ontological diagnosis | Correct action |
|---|---|---|
| A mechanism is identified by its document or file. | Publication or representation has taken the episteme position. | Recover `<content, EntityOfConcernRef, effectiveReferenceScheme>` and state publication separately. |
| One implementation defines the mechanism. | Realizer and declaration are collapsed. | State the mechanism-realization relation and keep implementation identity with its direct kind. |
| Operation arguments or results are written as A.6.5 SlotSpecs. | Direct-relation participant declaration and operation declaration are collapsed. | Declare argument and result meanings inside the exact A.6.1 `OperationDeclaration`; reserve SlotSpecs for one `RelationSignature`. |
| A planned value, method-description field, compatible kind, reference, or matching token is treated as an actual binding. | Declaration or representation is substituted for an obtaining application-side relation. | Identify the exact application occurrence and prove the declaration-local binding predicate, extent, and identity; otherwise retain the missing-governor blocker. |
| Admission tests are written as laws or as the operation's returned result. | Proposed-application disposition is confused with reusable regularity or domain result. | Put the admission predicate in `AdmissibilityConditions`, invariants in `LawSet`, and returned values in the exact result declaration. |
| `unknown` means that the candidate fails or that the application did not occur. | Evaluation uncertainty is collapsed with world-side failure or occurrence. | Keep the application and its result binding; use `unknown` only when the available governed argument values and dependencies cannot determine satisfaction or failure. |
| Evidence bound as an argument makes the criterion true. | Actual evidence use is confused with world-side satisfaction and warrant. | Keep the binding as an application-use fact; evaluate the direct criterion from governed candidate facts and state evidence or assurance relations separately. |
| A returned value is called the entity produced by work. | Operation result binding is confused with production or entity-identity inception. | State only the returned-value binding; use A.15.PROD and the subject identity rule when production or inception is separately current. |
| Applicability says only "in this context." | Reference scheme, claim scope, time, selected `CHR:ReferencePlane`, and conditions are hidden. | Recover each current value under its subject pattern and add a model-use structure only when its relations matter. |
| F.9 is used for every reference-scheme, `CHR:ReferencePlane`, or model-use change. | Cross-context sense correspondence is collapsed with episteme identity and independently governed applicability or structure changes. | Apply the three-step split in 4.3: F.9 supplies only the exact `SchemeSenseCell` correspondence; a separate C.2.1 claim states whether that Bridge suits the named bounded use; then apply the ordinary A.10 or assurance-bearing B.3 branch selected there. Use C.2.1 for reference-scheme identity, the selected plane to CHR, and model-use organization to A.1.1/A.22. If an actual transition or use relation is asserted, name its predicate and participants or stop that claim. |
| A graph or imperative list is called the executable mechanism. | Representation order is overread as condition-governed continuation. | Keep the representation claim here; use A.22.CGUS for actual entries, branches, returns, and stops. |
| An evaluation result changes mechanism identity. | Support for a claim is confused with declaration content. | Repair evaluation, binding, or evidence; revise the mechanism only when semantic content changed. |
| A comparison returns one score from incomparable values. | Scalarization has replaced the declared order and scale relations. | Return the admissible set or cite the exact scorer and comparison pattern that defines or constrains reduction. |
| A declaration materializes every optional component and neighboring relation before a receiving use needs them. | Apparatus completeness is substituting for use-value and blurring the mechanism boundary. | Add only the content needed to define the reusable operation family. Add a neighboring application, binding, dependency, Bridge, evaluation, evidence-use, or realization claim only when that exact occurrence or dependency is asserted and its own rule passes. |

### A.6.1:9 - Consequences

**Benefits.**

- Mechanism declarations can remain stable while realizers and work change.
- Physical, clinical, manufacturing, epistemic, and software cases use one declaration discipline without one domain becoming the default ontology.
- Admission, evaluation, and evidence claims become independently inspectable.
- Independently governed cross-reference-scheme, cross-`CHR:ReferencePlane`, and cross-model-use comparisons expose preserved and lost meaning without one generic transport relation.
- A reader can stop at a direct sentence when durable mechanism identity has no receiving use.

**Costs and trade-offs.**

- Authors recover the declared subject, effective reference scheme, and exact applicability rather than relying on one context label.
- A realization claim may need a separate relation and evidence-use statement.
- Mechanism comparison may require explicit mappings among operation argument and result declarations and a C.29 lens.
- Some familiar single-score or implicit-latest practices become unusable until their scale, scorer, or time policy is stated.

### A.6.1:10 - Rationale

`U.Mechanism` earns a dependent durable name because many later patterns rely on one reusable declaration of operations, laws, admission predicates, and applicability. Treating that declaration as only a table format loses identity. Treating it as the realizing system or method makes every implementation change look like a law change.

The declaration uses the `U.Signature` identity and content settlement because its reusable vocabulary, laws, applicability, and dependencies have the same episteme discipline. It remains a separate dependent U-kind because operation algebra and admission semantics create recurring action-facing claims that an ordinary signature does not govern. This dependence does not assert a C.3 subkind relation by itself.

The actual application and each binding are separate because the stable declaration can be reused with different actual values, and the same value can participate under different declaration-local meanings. Exact application and binding predicates, extents, and identities prevent a plan, description, reference, compatible type, or result record from fabricating participation. They also avoid one universal work-input or work-result relation.

The realization relation is separate because several entities can realize the same declaration and one entity can realize it only for a bounded scope and interval. Evidence can change without changing that world-side or semantic relation. This keeps mechanism evolution local and makes failure diagnosis practical.

Progressive explicitness serves didactic primacy. The pattern begins with a readable engineering question and a mantra, then introduces typed content only when reuse requires it. The mantra improves recall; A.22.CGUS enters only for an independently identified structure of potential continuations, while an enabled continuation, Work occurrence, and actual Transformation remain separate values.

### A.6.1:11 - SoTA-Echoing

| Source line | Source refs | Adopt, adapt, or reject | Effect in this pattern |
|---|---|---|---|
| Current complete semantics for effect handlers | Satoshi Kura, ["On Complete Categorical Semantics for Effect Handlers"](https://arxiv.org/abs/2602.03275), 2026. | Adapt as a software-derived stress case. The work distinguishes operation signatures, equational theories, handlers, and semantic models, and shows that one familiar realization model is not uniquely forced by the declaration. It does not supply a universal ontology for physical or social mechanisms. | `U.Mechanism`, its laws, a realizing entity, and the realization relation remain separate. One implementation cannot define mechanism identity by itself. |
| Current dependent effect semantics | Kura, Gaboardi, Sekiyama, and Unno, ["A Category-Theoretic Framework for Dependent Effect Systems"](https://arxiv.org/abs/2601.14846), 2026. | Adapt the use of indexed predicates and graded structure to stress typed positions and condition-dependent operation claims. Reject the inference that one categorical formalism determines the FPF ontology. | Argument and result declarations, application rules, `AdmissibilityConditions`, `U.ClaimScope`, and mathematical-lens boundaries are explicit. |
| Current relation-first multi-domain modeling, with historical acausal lineage | JuliaHub Dyad 3.2 component and analysis documentation, 2026; Modelica Language Specification 3.7 as historical lineage. | Adapt Dyad's current separation of reusable relation-first components from separately selected analyses and their result objects. Retain Modelica only for the historical distinction between acausal equations and imposed calculation order. Neither source is FPF ontology authority. | The physical case separates declaration laws, component relations, analysis choice, solver or simulation Work, result, and diagram. Equation or display order does not create a continuation structure; apply A.22.CGUS only when its own structure conditions hold. |
| Scoped operations, resources, and handlers | Bosman, van den Berg, Tang, and Schrijvers, ["A Calculus for Scoped Effects and Handlers"](https://arxiv.org/abs/2304.09697), LMCS 20(4), 2024; Matache, Lindley, Moss, Staton, Wu, and Yang, ["Scoped Effects as Parameterized Algebraic Theories"](https://arxiv.org/abs/2402.03103), 2024. | Adapt the separation among operations, equations, scopes, resources, and handlers. Keep it as one demanding software case rather than the default transdomain model. | `OperationAlgebra`, `LawSet`, Applicability, and realization remain distinct content and relation positions. |

Review this pattern when stronger work changes the distinction among operation declaration, law, admission predicate, realization, evaluation, and evidence; when A.6.0 or C.2.1 changes episteme identity; or when physical-modeling and effect-semantics practice reveals a mechanism claim that this content cannot express without kind collapse.

### A.6.1:12 - Relations

- **Builds on:** A.6.0, C.2.1, and A.2.6.
- **Governs:** reusable `U.Mechanism` declaration epistemes, their mechanism-specific content, declaration-local application and binding semantics, exact particular operation applications and bindings when current, and direct realization claims.
- **Coordinates with:** A.6.REL for occurrence identity; A.6.RCD for compound comparison claims and missing-relation stops; A.6.5 for RelationSignature SlotSpec discipline; C.3 for operation ValueKinds; A.1 for recognition criteria; A.3.1 and A.3.2 for Method and Method description; A.15.2 and A.15.1 for planned and performed Work; C.2.1 for mechanism epistemes, editions, result epistemes, and bounded Bridge-use claims; A.19 for comparison; F.9 for cross-scheme sense correspondence; A.10 for ordinary reliance; B.3 only for an actual named assurance claim; CHR for selected reference planes; A.1.1 and A.22 for selected model-use structure; C.29 for mathematical-lens use; E.20 for introduction; E.24.PUB for publication; A.22.CGUS for potential-continuation structure and case results; and G.11 for currentness.
- **Described and published through:** C.2.1, A.6.3, A.6.3.RT, and E.24.PUB.
- **Uses for precision restoration:** E.10, E.10.ARCH, and F.18 after the current object and relation positions have been recovered.

#### A.6.1:12.1 - Transformation-flow use

When E.18.1 reaches a mechanism question, A.6.1 supplies the reusable operation declaration and any current exact application, application binding, or realization relation. E.18.1 carries that governed object to the next locus; it does not define mechanism semantics, bind an actual value, choose a method, identify performed work, evaluate evidence, or pass a gate.

When selected relations and applied constraints connect signature, mechanism, method, Work, and evaluation constituents into one independently identified A.22 structure with local loci and at least two potential continuations, apply A.22.CGUS to that structure. A presentation of one traversal through a qualified CGUS is a separate demonstrative slice. The local mechanism mantra remains Plain mnemonic wording unless that wider structure actually qualifies and the later presentation is about it.

#### A.6.1:12.2 - Lowering and return conditions

Lower or withdraw a `U.Mechanism` identification when the text cannot recover an exact declared operation family, typed argument and result meanings, application rules, laws, admission conditions, and Applicability. Lower an actual application or binding when its declaration-local predicate, participants, extent, or identity cannot be recovered. Lower a realization claim when the entity does not preserve a declared law for admitted use or the claimed scope and interval cannot be recovered.

Return to the smallest changed object:

- changed declaration content, EntityOfConcern, or effective reference scheme requires A.6.1 and identifies another mechanism episteme; call it a continuing edition only when the separate C.2.1 `EpistemeEditionRelation` obtains, otherwise treat it as a non-continuing replacement;
- exact cross-context `SchemeSenseCell` correspondence requires F.9; a selected `CHR:ReferencePlane` change requires CHR, and a model-use-structure change requires A.1.1/A.22. An asserted transition or use relation must name its predicate and participants or stop; none becomes a generic mechanism-transport claim;
- a particular application or binding returns to its exact declaration-local predicate, extent, and identity rules; if they cannot govern the claimed actual use, retain the exact missing-governor blocker rather than widen A.6.1 into a universal work-participant relation;
- realizer capability or realization scope returns to the direct realization relation;
- evaluation and evidence currentness require their exact predicates and G.11 when currentness is the claim;
- method and work changes require A.3.1, A.15.2, or A.15.1;
- representation and publication changes require A.6.3, A.6.3.RT, or E.24.PUB;
- a changed governing-definition assignment requires E.20.

### A.6.1:End

