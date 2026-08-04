## E.17.0 - Viewpoint and View Recognition for Multi-View Describing
> **Status:** Stable

**Use this when.** One or more epistemes are being read, compared, constructed, or published under explicit concerns, and the work must distinguish the described entity, the viewpoint, the view, any viewing construction, cross-view correspondence, and publication.

**First useful result.** A readable judgment of the form `episteme E conforms to viewpoint edition P`, with the exact two epistemes recoverable. Add a designated relation occurrence, evaluation result, source-viewing relation, correspondence claim, or publication objects only when the next work or decision depends on them.

> **Tech-name:** `MultiViewDescribing`
> **Plain-name:** recognizing viewpoints and views in multi-view describing

`MultiViewDescribing` names this pattern's method. It is not a public U-kind, a family record, or an extra entity beside the epistemes and relations recovered below.

**Builds on:** C.2.1 for episteme identity; C.13 for collections; A.22 for selected structures; A.6.5 for relation-signature participant SlotSpecs; A.6.3 for an optional source-to-view construction relation; E.10.D2 for Description epistemes and specification use; E.24.PUB for publication; C.29 for representations.

**Used by:** E.17 publication, E.17.1 viewpoint bundles, E.17.2 TEVB, E.18 transformation-flow descriptions, and domain patterns that compare several views.

### E.17.0:1 - Problem frame

An engineer may have several claim-bearing epistemes about one system, method, structure, work occurrence, or another exact entity. A functional description, safety description, maintenance description, and allocation description may serve different concerns. One episteme may also be constructed from another by a query or projection, rendered in several forms, published several times, or compared with another view.

Those uses involve different objects and relations:

1. the exact EntityOfConcern of each episteme;
2. the episteme itself, identified under C.2.1;
3. an exact `U.Viewpoint` episteme carrying fixed concerns and conformance rules;
4. an obtaining `EpistemeViewpointConformanceRelation` occurrence;
5. dependent `U.View` membership of the same episteme individual;
6. an optional A.6.3 viewing relation recording how one episteme was constructed from another;
7. a viewpoint selected for one current describing use;
8. exact correspondence relations and epistemes that assert or describe them;
9. publication occurrences, forms, carriers, and representations.

The list is an orientation, not a form to fill. Ordinary use often needs only items 1 through 5.

### E.17.0:2 - Problem

How can an engineer recognize and use views under explicit viewpoints while preserving exact episteme identity and direct relation semantics, without treating a selected viewpoint, a query result, a diagram, a family label, or a publication as what makes an episteme a view?

The common practical failure is not merely loose wording. The wrong object is used to justify the next action. A generated table is accepted as a view because it was generated; a published diagram is accepted because it is readable; a `viewpointRef` is treated as proof of conformance; or several documents are put in one package and called a multi-view model without recovering any cross-view relation.

### E.17.0:3 - Forces

| Force | Tension |
|---|---|
| Lightweight use vs inspectable assurance | Most uses need one readable conformance judgment; contested use needs exact participants, predicate, occurrence identity, evaluation, and warrant. |
| Stable kind membership vs changing use | An episteme can remain a view after a reading, project, publication, or selected-use episode ends. |
| Direct authoring vs derivation | Some views are authored directly; others are constructed through a query or projection. Construction history must not define view membership. |
| Reusable viewpoint vs exact edition | Viewpoint libraries support reuse, while conformance depends on one exact claim-bearing viewpoint edition. |
| Several views vs one invented container | Multi-view work needs organization and correspondence, but a package, graph, or shared heading does not establish either. |
| Readable domain language vs ontological precision | Practitioners need `functional view` and `safety view`; load-bearing use still needs exact epistemes and direct relations. |
| Correspondence vs consistency repair | A correspondence can obtain while later evaluation finds an inconsistency or while repair work is still pending. |
| View vs publication | A view can be unpublished, and one view can be published repeatedly through different forms and carriers. |

### E.17.0:4 - Solution

**Local mantra.** Identify the candidate episteme. Resolve the exact viewpoint episteme. Test their fixed conformance predicate. Recognize the same episteme as a view only when conformance obtains. Add construction, selection, correspondence, evaluation, or publication only for the current use.

The mantra is a recall aid. Sections 4.1 through 4.9 supply the object distinctions, obtaining rules, and stopping conditions.

#### E.17.0:4.1 - Identify the candidate episteme before calling it a view

Recover candidate `E : U.Episteme` through C.2.1:

- exact claim content;
- exact EntityOfConcern `T`;
- effective `U.ReferenceScheme`.

These three discriminators identify E. A layout, file, query run, `viewpointRef`, selected project context, publication form, or carrier does not add another episteme identity discriminator.

If the current thing is only a diagram element, graph node, form, or carrier, recover that object under C.29 or E.24.PUB first. Do not promote it to an episteme or view by appearance.

#### E.17.0:4.2 - Resolve one exact viewpoint episteme

`U.Viewpoint` is a same-individual dependent durable kind under `U.Episteme`. One exact viewpoint P is the same individual as a C.2.1 episteme, not a slot value, method, publication form, bundle member, selected structure, local result value, or RelationSignature.

P has one independently selected viewpoint-convention structure `S_viewpoint : U.Structure` as its exact EntityOfConcern. That structure organizes the exact editions of the convention epistemes and exact obtaining relations among them. It introduces no new public or local kind and no organization record.

##### E.17.0:4.2.1 - Recover the least-powerful exact constituents

Construct `C_viewpoint` under C.13 from the exact constituent episteme editions. The collection may be heterogeneous: its invariant is exact constituent identity, not uniform declaration power. Give each constituent the least-powerful independently governed kind that carries its actual claims.

| Constituent | Admit it when | Exact subject and practical job | Do not collapse it with |
|---|---|---|---|
| `E_target` | A target-kind criterion is current. | One C.2.1 episteme whose exact EntityOfConcern is the admitted target kind and whose claims cite the direct membership rule. For a context-local target, the exact C.3.2 `KindSignature` is the constituent; use another `U.Signature` only when the criterion is itself a reused law-governed declaration. It says which entities a conforming view may concern. | a raw kind reference, target mention as membership proof, or a wrapper Signature around a local KindSignature |
| `E_stakeholder.system[i]` | The concern names one stakeholder system. | One C.2.1 episteme whose exact EntityOfConcern is the independently admitted exact `U.System`. | system mention, stakeholder-family typing, a current role assignment, or the episteme substituted for the system |
| `E_stakeholder.roleValue[i]` | The concern addresses holders of one work-facing role. | One C.2.1 episteme whose exact EntityOfConcern is the exact `U.Role` value interpreted through the selected role-taxonomy episteme and effective scheme. Actual holder facts remain exact `U.RoleAssignment` occurrences. | role spelling, taxonomy episteme, holder reference, or assignment obtaining |
| `E_stakeholder.collection[i]` | Several exact systems jointly form the concern referent. | One C.2.1 episteme whose exact EntityOfConcern is the independently identified C.13 collection-as-whole. | list adjacency, a system or role, the member plurality, or a description substituted for the collection whole |
| `E_stakeholder.localKind[i]` | The concern quantifies over one context-local classification. | The exact C.3.2 `KindSignature` episteme together with its fixed `U.ContextSlice`; its membership criterion and extension bound the concern. Cross-context reuse requires C.3.3. | a wrapper Signature, raw class spelling, silent public-kind promotion, or a local extension treated as universal |
| `E_concern[i]` | One exact question or concern claim is needed. | Ordinarily one C.2.1 episteme about one independently governed entity. It states what a conforming episteme must address. Promote it to `U.Signature` only when the concern predicate itself is a reused declaration with vocabulary, laws, and applicability. | a public `U.Concern`, unresolved EntityOfConcern, one-use question inflated into a Signature, or a concern label |
| `E_admittedKind[i]` | One independently admitted episteme kind may enter conformance. | One C.2.1 episteme that cites the exact kind and its governing membership rule; an exact local `KindSignature` may itself be the constituent. | a raw label or reference, admission by citation, a local wrapper, circular `U.View` admission, or the reference substituted for the membership rule |
| `E_rule[i]` | A construction, interpretation, coverage, semantic-form, completeness, consistency, or omission constraint is current. | Ordinarily one C.2.1 episteme stating the constraint about its exact EntityOfConcern. Use `U.Signature` only for genuinely reusable law-governed declaration content; use `U.MethodDescription` only when the claims describe one independently admitted method as a way of doing. | every rule coerced to Signature, procedural appearance as method-description admission, missing exact subject, or one-use constraint inflated with declaration fields |
| `D_method[i]` | A method-based convention is actually current. | One A.3.2 `U.MethodDescription` whose exact EntityOfConcern `M_method[i]` independently passes A.3.1. The description supplies the convention; the raw method stays outside `C_viewpoint`. | method mention as membership, raw method as constituent, several descriptions inferred to form one workflow, or description as performed work |

Preserve every exact edition. A concern question, kind citation, or one-use rule acquires none of `SubjectKind`, `RangedValueKind`, Vocabulary, Laws, or Applicability merely to fit a common table. Conversely, a constituent that independently is a reusable relation declaration, kind declaration, or method description keeps that stronger governed kind. Collection position grants no convention job and no stronger membership.

##### E.17.0:4.2.2 - Select the viewpoint-convention structure

When authoring or revising a reusable viewpoint:

1. identify the least-powerful exact constituents above;
2. construct exact `C_viewpoint` from those editions under C.13;
3. recover each selected direct relation occurrence among them under its own governor;
4. identify ordinary constraint episteme `Q_org` about exact `C_viewpoint` and the admissible describing-use frame;
5. have an exact system perform the applicable method-governed A.22 selection over C, the selected obtaining occurrences, the applied Q constraints, and the use frame, yielding exact `S_viewpoint`; and
6. identify P under C.2.1 with `EntityOfConcern(P)=S_viewpoint`, then apply the membership conditions below.

P is admitted as `U.Viewpoint` only when its fixed claim content, interpreted under its effective reference scheme:

1. identifies exact `S_viewpoint` selected as above;
2. states the exact EntityOfConcern-kind criterion for candidate view epistemes and cites its direct durable-kind authority or exact C.3.2 local-kind declaration and ContextSlice;
3. states exact stakeholder or audience referents when current, exact concerns, and independently admitted episteme kinds allowed for candidates;
4. states fixed concern-coverage, semantic-form, completeness, consistency, omission, and conformance rules without circularly using `U.View` or another conformance-dependent kind as a premise; and
5. states the describing-use frame and fixed applicability qualifiers needed to interpret those rules.

P needs no parent `U.Signature`: its claim-bearing edition and positive predicate do the viewpoint job, while the conformance RelationSignature declares a different object. Changed P claim content, exact S, or effective reference scheme identifies another episteme edition. Bundle repackaging, publication, evaluation, representation, or changed current-use selection does not.

**Ordinary reuse stops early.** When P is already admitted, resolve one `U.ViewpointRef` to exact P, recover its exact S, inspect P's fixed claims, and apply conformance. Do not reconstruct C or Q, manufacture Signatures, or republish Q merely to use P.

##### E.17.0:4.2.3 - Keep explicit evaluation values optional

The fixed `E17ViewpointSemanticsSlice@FPFEdition` selects the exact FPF and E.17.0 declaration editions, effective `U.ReferenceScheme`, and `Γ_time`. In that slice this pattern admits exactly two optional C.3.2 local ValueKinds, each carried by its own C.2.1 KindSignature episteme:

| Local ValueKind | Exact extension | Admit an explicit value only when |
|---|---|---|
| `KS.ViewpointConformanceValue.E17`, carrying `KindSignature(ViewpointConformanceValue@E17)` | the two exact values designated `conforms` and `doesNotConform` | separately performed conformance-evaluation work emits the value and a named A.21 gate or C.11 comparison/selection decision consumes it |
| `KS.ViewpointOrganizationSatisfactionValue.E17`, carrying `KindSignature(ViewpointOrganizationSatisfactionValue@E17)` | the two exact values designated `satisfiesOrganization` and `doesNotSatisfyOrganization` | separately performed candidate-structure evaluation emits the value and a named C.11 comparison or selection decision consumes it |

The four exact values remain distinct from their designators. Both kinds use F4 formality, deterministic exact-equality membership, no `SubkindOf`, and fail-closed definedness. Incomplete evidence or interpretation leaves the optional evaluation unsupported or undefined; it supplies neither a negative result nor a third `unknown` member.

Omit both local values from P, Q_org, direct relation obtaining, and structure identity unless the named consumer actually needs one. Without such a consumer, state the direct conformance judgment or the Q_org constraint judgment. `KindMembershipJudgment` and `ConcernCoverageJudgment` remain withdrawn and do not return as kinds or result fields.

##### E.17.0:4.2.4 - State Q_org and select S without hidden organization

`Q_org` is one ordinary C.2.1 constraint episteme with exact `EntityOfConcern(Q_org)=C_viewpoint`. Its ClaimGraph carries the applied semantic constraints under its effective reference scheme and the named admissible describing-use frame. Q is not C, a selected relation occurrence, S, P, a result value, Signature, MethodDescription, organization record, actor, or method.

For a reusable viewpoint, Q carries these eight organization constraints by value:

1. **One target criterion.** Select exactly one `E_target` by its exact claim content and cited direct target-kind authority; a raw kind label, viewpoint name, or collection position proves neither selection nor membership.
2. **Concerns depend on the target.** Every exact `E_concern[i]` depends on `E_target`. When stakeholder attribution changes the concern, cite one exact stakeholder referent recovered as a system, role value, collection-as-whole, or context-local classification under its actual governor.
3. **Coverage depends on exact concerns and claim families.** Each coverage constraint depends on the exact concern constituents and exact claim families it evaluates; a heading, graph edge, unresolved family label, or coverage result is neither the dependency nor proof of coverage.
4. **Semantic form depends on the admitted kind.** Each semantic-form constraint depends on the exact independently admitted-kind constituent to which it applies; notation, form, or a raw kind reference grants no admission or dependence.
5. **Method conventions depend on exact method descriptions.** Each method-based convention depends on one exact `D_method[i]` whose exact EntityOfConcern is an independently admitted A.3.1 method. The raw method remains outside C, and description, method, dependence, and performed work remain distinct.
6. **Completeness, consistency, and omission name their subjects.** Each such constraint depends on the exact concern or claim components it constrains and names any admitted omission condition by value; a bare status or whole-P label is insufficient.
7. **Resolution does not establish a relation.** Resolve every designation and governed reference under the effective scheme, while keeping spelling equality, lookup, graph adjacency, compatible schemes, token presence, and reference resolution from counting as direct-relation obtaining.
8. **No circular view admission.** No admitted-kind constituent may depend on `U.View` membership or the same conformance judgment being established. Every mutually dependent group needs one named joint-interpretation method or fixed-point criterion.

Replay mutually dependent groups through stratified or witnessed joint/fixed-point semantics. Without that witness, the candidate fails the A.22 selection criterion for the named use. A graph, strongly connected component, iteration syntax, or fixed-point diagram is at most a C.29 representation of already judged occurrences and semantics; it is not the witness, criterion, or selected structure.

An exact system—not A.22, Q, P, or a relation—performs the applicable method-governed structure-selection work over exact C, exact obtaining occurrences `r_1,...,r_n`, the applied Q constraints, and the admissible-use frame. The symbols `r_1,...,r_n` are local notation, not an O object or collection kind. The selection yields exact S under A.22; C stays governed by C.13 and every r by its direct pattern.

Identity and change stay local:

- Q changes only with its claim content, exact C EntityOfConcern, or effective reference scheme; another graph, form, carrier, representation, or publication leaves the same Q edition unchanged.
- Replacing a selected obtaining occurrence changes the organization used to identify S. Replacing only its assertion, occurrence description, D, J, result, production or use relation, provenance, or graph leaves that occurrence unchanged, although use-specific admissibility may need reevaluation.
- S changes when C, any selected obtaining occurrence, the applied semantic constraint set, or the admissible-use frame changes. Replacing only Q while those discriminators remain semantically unchanged leaves S unchanged.
- P changes only with its fixed claim content, exact S EntityOfConcern, or effective reference scheme. P is neither S, its reference, a bundle position, a publication object, nor an evaluation result.

Resolve P's target criterion, admitted kinds, coverage, semantic-form, completeness, consistency, and omission rules through exact constituent claims and selected obtaining occurrences cited by P. Do not leave them as untyped fields, mandatory Signature constituents, or graph edges treated as occurrences.

The selected public individual is exact episteme P about S. These nearby alternatives remain rejected:

- S itself is not `U.Viewpoint`: consumers require the exact claim-bearing edition P, while `EntityOfConcern(P)=S`.
- An episteme about one method is a neighboring `U.MethodDescription` only when exact M and that description independently pass A.3.1 and A.3.2; it is not the viewpoint genus. A method-description constituent does not retarget P from S to M.
- No viewpoint record, wrapper, organization object, context entity, or non-entity value is needed; P, S, C, and selected relation occurrences already exhaust the identity-bearing objects.
- Bundle position, bundle edition, package ID, or publication grouping does not constitute P or grant membership.
- P requires no parent `U.Signature`, is not a public C.3 local kind, and is not `EpistemeViewpointConformanceRelationSignature`. A reusable classifier, context-local classification, and direct-relation declaration are different jobs with different subjects.

`U.Viewpoint` is therefore the same P under the complete positive predicate above: no new root identity, wrapper identity, method requirement, selection-dependent membership, or generic-episteme shortcut.

##### E.17.0:4.2.5 - Author progressively and stop at the needed assurance

Authoring is a progressive assurance path, not a mandatory workflow:

1. identify every exact constituent edition and state each proposed dependent-to-base claim readably;
2. resolve both endpoint designations, apply the direct obtaining criterion, and construct exact C from those editions under C.13;
3. add D only for a named A.22 selection-use claim, and J or evaluation only when that receiving use needs the additional assurance;
4. apply exact Q constraints and have an exact system perform the applicable method-governed A.22 selection over C and the selected obtaining occurrences, producing exact S; and
5. identify ordinary episteme P about S, apply the positive viewpoint-membership predicate, and only then mint or reuse `U.ViewpointRef`.

Citation, collection membership, graph adjacency, and displayed edges never close step 2. Selection returns a governed reference to an existing selected object; it is not construction of another constituent episteme. Viewpoint authoring requires neither five fixed stages, one composite method, empirical/formal evaluation, nor J. Identify every cited method under A.3.1 and use B.1.5 only when an order-sensitive method whole independently obtains. Stop as soon as the named receiving use is served; add no assurance artifact merely because a longer path exists.

#### E.17.0:4.3 - Keep viewpoint-convention dependence direct


Use `ViewpointConventionDependencyRelation(E_dependent,E_base)` only when interpreting or replaying the fixed claims of exact dependent constituent episteme `E_dependent` depends on an exact criterion, law, public name, or method claim carried by exact base constituent episteme `E_base`, and replacing that base edition or making its exact used content unavailable can change the interpretation or replay. It is the A.6.6 base-dependence case specialized to viewpoint-convention constituents.

Citation, co-membership, reference resolution, compatible schemes, or a graph edge alone does not establish this predicate. For fixed endpoint editions, one positive occurrence `r` is participant-determined by `<E_dependent,E_base>`. Scope, time, status, evaluator, evidence, result, use, selection, representation, and publication are neither participants nor occurrence-identity discriminators.

`ViewpointConventionDependencyRelationSignature` is a separate RelationSignature episteme about the direct relation kind. It declares exactly:

| SlotSpec | ValueKind | RefKind |
|---|---|---|
| `DependentConstituentSlot` | `U.Episteme` | `U.EpistemeRef` |
| `BaseConstituentSlot` | `U.Episteme` | `U.EpistemeRef` |

The SlotSpecs declare reusable participant meanings and polarity. They do not fill themselves, make the relation obtain, or identify an occurrence. The current A.6.6 vocabulary resolution chain is `viewpointConventionDependsOn` -> current vocabulary entry -> `ViewpointConventionDependencyRelationSignature` -> its EntityOfConcern, `ViewpointConventionDependencyRelation`. The NameToken, its separate NameCard, vocabulary entry, signature episteme, direct kind, and occurrence remain distinct; spelling or citation proves none of them equivalent and makes no occurrence obtain.

##### E.17.0:4.3.1 - Public designation of the direct relation kind

The complete F.18 NameCard for this relation-kind designation is:

| Field | Exact value or rule |
|---|---|
| `NameCardId` | `NameCard.ViewpointConventionDependencyRelation.FPFPublic`; this identifies the card only. |
| `GovernedValueRef` | exact direct kind `ViewpointConventionDependencyRelation`, not r, its signature, vocabulary entry, token, assertion, or card |
| `GoverningPatternRef` | E.17.0 for obtaining and occurrence identity; A.6.6 governs reusable vocabulary-entry use; F.18 governs this naming act, not the relation semantics |
| `BoundedContextRef` | `FPF English public publication, edition 2026-07-14`; this is naming context, not occurrence time |
| `LocalSenseRef` | semantic dependence of one exact viewpoint-convention constituent episteme on another exact base constituent episteme, dependent first |
| `TechLabel` | `ViewpointConventionDependencyRelation` |
| `PlainLabel` | `this viewpoint-convention constituent depends on that exact base constituent` |
| Candidate set | dependency candidates: selected label, `ConstituentSemanticDependencyRelation`, `ViewpointConventionRelianceRelation`; representation candidates: `ConstituentReferenceRelation`, `ViewpointLinkRelation`, `ViewpointOrganizationEdge` |
| Rejections | `ConstituentSemanticDependencyRelation` drops the viewpoint-convention boundary; reliance widens to decision reliance; reference states resolution only; link leaves predicate and polarity unstated; organization-edge names a graph representation rather than obtaining. None is an alias. |
| Selection rationale | the selected label names both the viewpoint-convention domain and semantic-dependency predicate; the RelationSignature, not the label, carries participant meanings |
| `BridgeRefs` | none in this bounded context; a future cross-context sameness claim requires an exact F.9 Bridge Card |
| Lineage | rejected reference, link, organization-edge, semantic-dependency, and reliance spellings remain source lineage only, never synonyms |
| Refresh | reopen when participant kinds, obtaining predicate, A.6.6 use policy, or repeated reader evidence changes; do not refresh for document churn, an occurrence change, or a token-only change that leaves this card's governed sense unchanged |

##### E.17.0:4.3.2 - Add only the neighboring object the receiving use needs

The compact positive statement may stop at “this exact constituent depends on that exact base constituent.” Add the following objects only under their positive trigger; do not flatten them into one witnessed-base record or add their fields to the two-participant relation.

| Object | Positive trigger and exact identity | Boundary |
|---|---|---|
| `A_dependency` | a separately reviewable readable assertion is needed: one C.2.1 assertion episteme whose exact EntityOfConcern is `E_dependent` and whose claims state the direct predicate for exact `E_base` | authoring does not make r obtain; A is neither r, an occurrence description, nor a third participant |
| `O_dependency` | an already recoverable r needs a separate description: one C.2.1 description episteme whose exact EntityOfConcern is r and whose claims may state endpoints and participant-determined identity | the description is not r, and endpoint mention without independently recoverable r is insufficient |
| `D_dependencyUse` | one named A.22 structure-selection judgment needs a reviewable claim that exact r is admissible: one C.2.1 episteme identified through obtaining `EpistemeConstitutionRelation(G_dependencyUse,r,S_decl)`, where G is its exact `U.ClaimGraph`, r is its exact EntityOfConcern, and `S_decl` is its effective `U.ReferenceScheme` | D is not G, r, `S_decl`, an assertion, occurrence description, `U.Signature`, RelationSignature, selected structure, actor, or third dependency-relation participant; the participant triple does not constitute itself, and obtaining r does not entail use-specific admissibility |
| `J_dependency` | that named selection judgment needs inspectable inferential support | J is non-constitutive justification content, distinct from G; it makes no claim true, identifies no occurrence, and performs no work |
| empirical or formal evaluation package | a named receiving use needs a tested result or formal conclusion | its actors, work, methods, bases, results, evidence, production, and use relations remain separate from r and D |
| later selection work and C.11 result | accountable selection or project choice is separately current | an exact system performs method-governed work; A.22, a pattern, episteme, graph, method, or result never acts, and no generic acceptance relation follows |

`D_dependencyUse` is therefore the exact C.2.1 episteme identified through obtaining `EpistemeConstitutionRelation(G_dependencyUse,r,S_decl)`. The ordered triple names the exact ClaimGraph, EntityOfConcern, and effective ReferenceScheme participants; it is not a self-constituting card or record and does not make the relation obtain.

`G_dependencyUse` designates exact r and the receiving A.22 use: exact `C_viewpoint`, exact Q_org constraints applied, and the named admissible-use frame. It carries two separate claim values:

- `c_dependencyObtains`: exact direct predicate obtains, independently of use and evidence;
- `c_dependencyAdmissibleForSelection`: exact r is admissible among candidate organizing occurrences for that named use frame.

Both are claim values in G, not C.2.1 epistemes, occurrences, or decision results. Changing the use frame can change the second claim while r remains unchanged. Add exact `U.ClaimScope` or a time qualification to G only when it changes the represented claim; neither becomes a participant. Cite the exact current A.6.6 vocabulary entry and exact RelationSignature as declarations, not as r or proof of r. D is reidentified only when one of exact `<G_dependencyUse,r,S_decl>` changes; a changed claim value changes D only through changed constitutive G.

When J is present, keep separate conclusion nodes for the two claims and at least these distinct premises when they are actually relied on:

1. exact `E_base` under exact `S_base` carries the criterion, law, public name, or method claim used to interpret or replay `E_dependent`;
2. an exact system in exact interpretation or replay work, enacting an admitted method, resolves and applies that base content to `E_dependent` under exact `S_dep`; and
3. replacing exact base edition `E_base` or making its exact used content unavailable can change interpretation or replay of fixed exact `E_dependent`.

Designation, citation, graph location, co-membership, scheme compatibility, version difference alone, or a failed lookup supplies none of those premises. If the interpretation is method-dependent, cite the exact `U.MethodDescription`, but identify the acting system, admitted method, and work occurrence separately.

##### E.17.0:4.3.3 - Keep empirical and formal evaluation local

When empirical interpretation or replay testing is current, identify separately:

- `H_dependencyEvaluator : U.System` under A.1 as performer;
- `RA_dependencyEvaluator : U.RoleAssignment` under A.2.1 for the current evaluator-role use, distinct from holder, role value, and work;
- `M_dependencyTest : U.Method` under A.3.1 and, when needed, `D_dependencyTest : U.MethodDescription` under A.3.2; D describes M but is neither method, work, RelationSignature, nor OperationAlgebra, and a separate A.6.1 operation declaration is cited only when typed application is current;
- exact `W_dependencyTest : U.Work` performed by H under RA with `enactsMethod(W_dependencyTest,M_dependencyTest)` obtaining;
- exact `B_dependencyEmpirical`, a C.2.1 episteme identifying the model, calibration, assumptions, and interpretation basis; and
- exact result episteme `T_dependency = <G_dependencyTestResult,E_dependent,S_test>`, whose ClaimGraph designates exact `E_base`, predicate, method, conditions, basis, and positive or negative result.

Establish actual participation of `E_dependent`, `E_base`, each parameter, and `B_dependencyEmpirical` during W only through their exact governed subject relations or A.6.1 operation-application bindings. A MethodDescription or compatible SlotSpec establishes no participation. Open a local A.15.PROD claim only when the receiving use needs to say W first constituted T or later completed its declared production; inception, completion, episteme identity, and dependency obtaining remain distinct.

When formal interpretation is current, constitute exact formal-evidence episteme `E_dependencyProof = <G_dependencyProof,E_dependent,S_proof>` and exact `B_dependencyFormal` identifying the theory, axiom set, proof semantics, and interpretation basis. Its ClaimGraph designates exact `E_base`, proof obligation, formal method, basis, and result. Preserve entailment, refutation, malformed input, timeout, and checker failure as different outcomes; neither a refutation nor a checker failure fabricates positive r. The proof episteme performs no verification and is not r or a participant.

If reusable target claims are needed, constitute them separately under C.2.1:

- `C_dependencyObtains` has `c_dependencyObtains` as its principal claim and concerns the exact endpoint pair and predicate;
- `C_dependencyDoesNotObtain` carries a distinct negative principal claim and is not a state of the positive episteme; and
- `C_dependencyAdmissibleForSelection` concerns exact r under the named use frame and remains distinct from both obtaining claims.

Co-representation in one ClaimGraph does not merge these epistemes. T carries its empirical conclusion locally; `E_dependencyProof` carries its formal conclusion locally. If a target-claim episteme separately represents one conclusion, use C.29 only when representation correspondence matters—never as truth, use, or r. Mint no duplicate evidence-bearing relation and no new A.10 ontology.

Keep these three cases distinct:

1. exact r obtains while support for `c_dependencyObtains` is unknown; a selecting system may decline reliance without deleting or reidentifying r;
2. a negative empirical or formal result may support `C_dependencyDoesNotObtain` without presupposing r, fabricating D, or becoming a positive occurrence; and
3. T may support the claim that r obtains without supporting use-specific admissibility; a later decision method may consume empirical and formal result epistemes in separate declared premise slots and produce a separate C.11 result.

Historical use of any claim or result requires exact work, enacted method, and an obtaining premise, decision-use, reference-use, or operation-argument relation. Storage, inspection, citation, attachment, production, graph membership, or adjacency is not use. Keep empirical and formal algebras distinct; keep provenance and assurance with A.10, G.6, and B.3. Retain a missing-governor blocker instead of inventing a generic evidence, use, or acceptance relation.

##### E.17.0:4.3.4 - Schemes, scope, transformation, and change

Recover `S_dep` from `E_dependent`, `S_base` from `E_base`, and `S_decl` from D. They are three uses of existing `U.ReferenceScheme`, outside r and its RelationSignature. G may designate exact endpoints, claim values, and declared names through those schemes; designation is neither occurrence obtaining, truth, nor historical participation.

Within one bounded context, keep claim-scope `widen`, `narrow`, and `refit` under A.2.6. Use `translate` only across exact context-local senses through an obtaining F.9 Bridge between exact SenseCells. Scheme difference, same spelling, token reuse, or translation intent triggers no Bridge.

Open `RepresentationSchemeTransitionRelation@Context` only when all six governed participants—one independently selected `BoundedModelUseStructure : U.Structure`, the preserved EntityOfConcern, source and receiving representation epistemes, and source and receiving scheme-description epistemes—are independently recoverable before dependency testing and an exact system performs actual representation-transformation Work. The `@Context` suffix is only the retrieval label for that A.1.1 bounded-context use; no bounded-context object or generic context field participates, and the required Work is part of the obtaining test rather than a seventh participant. Require the same exact EntityOfConcern, declared preservation for the receiving use, explicit loss or recoverability, tuple-plus-scheme-pair occurrence identity, and a separate transition-description episteme whose EntityOfConcern is that occurrence. Add C.29 only for a current mathematical lens and keep its output local. If no exact transition or Bridge applies, block the proposed cross-scheme dependency use.

Changing only J, an assertion or occurrence description, evaluation result, basis, provenance, production, later-use relation, or representation leaves r unchanged while its endpoint pair is fixed. It also leaves D unchanged while exact `<G_dependencyUse,r,S_decl>` is fixed. Unknown support does not make an obtaining r non-obtaining, and support for a negative claim creates no positive r. A changed representation transition invalidates judgments that depended on that transition, but changes r only when an endpoint episteme or the direct predicate also changes.

**Progressive stopping rule.** Use the lightest sufficient rung: readable dependency assertion; reusable RelationSignature when declaration reuse matters; D only for a named A.22 selection-use claim; J only for inspectable inference; evaluation work and exact participation only when evaluation is current; local A.15.PROD only for a needed result-inception or completion claim; provenance, assurance, representation transition, mathematical lens, scope translation, and Bridge only at their own triggers. No higher rung proves a lower-rung occurrence.

#### E.17.0:4.4 - Test the direct conformance relation

`EpistemeViewpointConformanceRelation` is a direct species of `U.Relation`. Plainly: **the episteme conforms to this exact viewpoint**.

Its only two actual participants are independently identified before the test:

- candidate episteme `E : U.Episteme`;
- viewpoint episteme `P : U.Viewpoint`.

`EpistemeViewpointConformanceRelationSignature` is a separate RelationSignature episteme about that direct kind and declares exactly:

| SlotSpec | ValueKind | RefKind |
|---|---|---|
| `CandidateEpistemeSlot` | `U.Episteme` | `U.EpistemeRef` |
| `ViewpointEpistemeSlot` | `U.Viewpoint` | `U.ViewpointRef` |

The declaration, SlotSpecs, references, and participant fillers neither make the relation obtain nor identify its occurrence. P remains the ordinary episteme about S; P is not this signature.

`EpistemeViewpointConformanceRelation(E,P)` obtains exactly when:

1. E is one independently identified episteme and P is one independently admitted viewpoint episteme;
2. exact `T := EntityOfConcern(E)` is recovered only from E's C.2.1 constitution;
3. P's fixed `EntityOfConcernKindCriterion` applied to exact T yields membership under the cited direct durable-kind governor, or under one exact C.3.2 `KindSignature` edition and one exact `U.ContextSlice` fixed by P for a local criterion;
4. E has at least one independently governed episteme kind referenced by P's admitted-kind claims, excluding `U.View` and every kind whose membership depends on this same conformance; and
5. E's fixed claim content, interpreted under its effective reference scheme, satisfies P's fixed concern-coverage and semantic-form rules, including each exact completeness rule and each admitted omission or loss condition named by P.

T is recovered from E, not guessed from a use qualifier, topic, P, label, reference spelling, or evaluator input, and it is not a hidden third participant. Changing T changes E. Changing P's target criterion, direct governor, local KindSignature, ContextSlice, admitted-kind claims, or conformance rules changes P.

For fixed E and P, one positive occurrence is participant-determined by `<E,P>`. A classifier, evaluation work, assertion, evidence path, result value, operational state, publication, audience, current use, or newly selected slice may discover, warrant, or use the judgment but enters neither its participants nor identity. If conformance could change while E and P remain fixed because another current object changed, route that condition to a separately identified adequacy or evaluation claim or reopen the relation architecture.

Conformance covers E's semantic content relative to P's fixed convention claims. Truth about T, decision fitness, stakeholder satisfaction, evidence-backed adequacy, publication usefulness, and operational usefulness remain separate evaluations. Evaluation never makes the direct predicate obtain or produces another occurrence for the same fixed pair.

##### E.17.0:4.4.1 - Public designation of conformance

The complete F.18 NameCard for the direct conformance kind is:

| Field | Exact value or rule |
|---|---|
| `NameCardId` | `NameCard.EpistemeViewpointConformanceRelation.FPFPublic`; card identity only |
| `GovernedValueRef` | exact direct kind `EpistemeViewpointConformanceRelation`, not a source line, card, signature, token, phrase, occurrence, or reference |
| `GoverningPatternRef` | E.17.0; F.18 governs naming only, while A.6.5 declares SlotSpecs and E.24.UK admits the dependent kinds |
| `BoundedContextRef` | `FPF English public publication, edition 2026-07-14`; not project context, host path, current use, effective scheme, local ContextSlice, or relation time |
| `LocalSenseRef` | exact two-participant semantic conformance of one episteme to one viewpoint episteme |
| `TechLabel` | `EpistemeViewpointConformanceRelation` |
| `PlainLabel` | `the episteme conforms to this exact viewpoint` |
| Candidate set | selected label, `EpistemeConformsToViewpointRelation`, `ViewpointConformanceRelation`, `ViewConformanceRelation`, `EpistemeViewpointGovernanceRelation`, `ViewpointGovernanceRelation`, `ViewMembershipRelation`, `viewpoint-to-description relation` |
| Rejections | shorter conformance names hide a participant or assume view membership; governance collapses selection with semantic conformance; membership names the derived classification; the description placeholder narrows arbitrary episteme and omits the predicate. None is an alias. |
| Selection rationale | the selected Tech label names both participant kinds and the obtaining predicate without presupposing that E is already a `U.View` |
| `BridgeRefs` | none; scheme difference, spelling, candidate similarity, and public reuse create no cross-context sameness claim |
| Lineage | the selected name replaces `viewpoint-to-description relation` without admitting that placeholder as a synonym or second public designation |
| Refresh | reopen only when either participant kind, the conformance predicate, direct occurrence identity, or repeated reader evidence changes; not for spelling preference, one reaction, layout, repackaging, or unchanged semantics |

The card, label, candidate list, and former placeholder are naming evidence only. None is relation admission, occurrence identity, or proof of obtaining.

#### E.17.0:4.5 - Recognize the same episteme individual as `U.View`

An episteme is a `U.View` exactly when `EpistemeViewpointConformanceRelation(E,P)` obtains for at least one exact viewpoint P. This is same-individual dependent-kind membership of E under `U.Episteme`, not a second view individual, wrapper, form, carrier, result value, or identity discriminator.

One unchanged E may conform to zero, one, or several viewpoint editions through different pair-determined occurrences while remaining one episteme. Direct authoring and A.6.3 construction—including identity viewing—are separate histories: either may be present or absent, and neither grants membership. Selection, transformation, bundling, naming, rendering, publication, audience, or current use also grants none.

Membership survives the end of reading, selection, use, evaluation, bundle membership, or publication. `P_old` and `P_new` are different C.2.1 epistemes when their fixed claims, S, or effective scheme differ; an obtaining `EpistemeEditionRelation` relates them but transfers no conformance. A current use may select `P_new` while unchanged E still conforms to `P_old`; adequacy and conformance for `<E,P_new>` are judged separately. If E's claim content, EntityOfConcern, or effective scheme changes, C.2.1 identifies another episteme and its membership is judged anew.

**Ordinary stopping rule.** Stop at the readable judgment `this episteme conforms to viewpoint edition P` when the next work needs neither an exact occurrence designator nor warrant. Add an occurrence designator, assertion episteme, evaluation episteme or local result value, evidence path, work record, or decision-use episteme only for the named receiving need. A readable assertion is not occurrence identity, but neither is mandatory reification or evidence justified without a consumer.

The stable gain is one viewpoint extent over convention structures with zero, one, or several independently grounded methods, plus one view extent spanning direct and derived construction without identity, use, or publication collapse. The cost is explicit A.22 structure recovery when a reusable P is authored and explicit conformance work only when a load-bearing claim is contested; ordinary reuse remains reference resolution plus the fixed E/P test.

#### E.17.0:4.6 - Keep selection for one describing use separate

For one current describing use, its use qualification carries one singular `viewpointRef : U.ViewpointRef`. Resolve that reference under the effective reference scheme to exact P. `ViewpointId` is P's designator; designator, reference, and episteme remain different objects.

The use qualification selects P for that use only. It does not establish conformance or `U.View` membership, enter C.2.1 identity, reidentify E, or create a universal selection relation, legacy context tuple, bounded-context object, or generic model-use identity field. Another use may select another P while E remains unchanged. A use needing several viewpoints first identifies their exact governed C.13 collection and membership; it does not overload `viewpointRef` with a collection value.

The architecture therefore keeps exactly two positive dependent-kind rules—P as `U.Viewpoint` by its fixed content about selected S, and E as `U.View` by obtaining conformance—and two direct relation kinds—viewpoint-convention dependence and E/P conformance. D remains optional for a named A.22 use; the two local explicit-result ValueKinds remain optional for named evaluation consumers. Bundles carry exact `U.ViewpointRef` values. C.2.1 identity, MethodDescription, A.6.3 construction, E.24.PUB publication, C.29 representation, and unrelated interfaces keep their own owners and identities.

#### E.17.0:4.7 - Add viewing construction only when its history matters

A.6.3 governs an exact viewing relation from a source episteme to a separately identified receiving episteme. It preserves the same exact EntityOfConcern. Claim content and the effective reference scheme may be preserved or changed only within A.6.3's declared construction law. If the exact EntityOfConcern changes, the move exits to A.6.4 rather than counting as viewing construction.

Keep these claims independent:

- **constitution:** C.2.1 identifies the receiving episteme;
- **construction:** A.6.3 states an obtaining source-to-receiving viewing relation when one exists;
- **membership:** E.17.0 states whether the receiving episteme conforms to an exact viewpoint;
- **work:** A system may perform query, authoring, or rendering work;
- **production:** A.15.PROD is opened only when a local work/change/entity-identity-inception or completion claim about the receiving episteme is current.

Do not infer one claim from the label `generated view`.

#### E.17.0:4.8 - Recover multi-view organization and correspondence only as needed

Several conforming views do not automatically form one new entity. For ordinary comparison, exact view epistemes, exact viewpoint epistemes, and their conformance occurrences can remain a plurality.

When the work depends on the collection as a whole, construct it under C.13. When it depends on an organization among those views, recover the exact direct relation occurrences and select one `U.Structure` under A.22. A package, table, graph, or shared EntityOfConcern is not that structure by appearance.

When cross-view correspondence matters:

1. name the exact participant epistemes or represented entities;
2. state the direct correspondence, consistency, realization, trace, or change-impact relation that is claimed;
3. apply that relation's direct governing pattern, including its obtaining and occurrence-identity rules;
4. identify a C.2.1 assertion or description episteme only when the correspondence claim itself must be reviewed or used;
5. use C.29 when a graph, matrix, or diagram represents the already recovered objects and relations.

Plain `correspondence model` may describe such a claim-bearing episteme after its exact EntityOfConcern and direct relations are recoverable. It is not a universal `U.CorrespondenceModel` kind, a substitute for the relations, or proof that they obtain. If the needed direct relation has no governor, return the exact missing-relation blocker or use A.6.RCD; do not close the case with `linked`, `mapped`, or `consistent`.

Temporary inconsistency is represented by exact evaluation claims and, when current, repair work. It does not silently weaken the conformance predicate or erase an obtaining correspondence relation.

#### E.17.0:4.9 - Keep publication and conceptual form outside view identity

E.24.PUB keeps three direct relation occurrences distinct:

- `PublicationFormExpressionRelation(selectedEdition,publicationForm,boundedUseDeclaration)` states that the exact form expresses enough of that selected episteme edition for the declared use;
- `PublicationFormBearingRelation(presentationCarrier,publicationForm)` states that the exact `U.PresentationCarrier` bears the recoverable form; and
- `EpistemePublicationRelation(selectedEdition,audienceDeclaration,boundedUseDeclaration,publicationForm,presentationCarrier)` makes that edition available to entities admitted by the audience declaration for the bounded use, only while both supporting relations obtain and the audience can get the edition through the carrier.

Expression has its exact three participants, bearing its exact two, and publication its exact five. Each occurrence retains its own maximal continuous obtaining or availability interval. Changing a participant identifies another occurrence; an availability gap followed by restoration creates a later publication occurrence. None of those changes reidentifies an otherwise unchanged C.2.1 episteme.

Rendering, upload, or carrier manipulation is `U.Work` only when an exact system performs it. C.29 separately governs a mathematical, diagrammatic, or other representation and its correspondence to independently recovered objects and relations. A form, carrier, representation, rendering, or publication occurrence grants no `U.Viewpoint` or `U.View` membership and establishes no world-side subject relation.

Plain `published view` therefore means an already recognized view episteme participating as the selected edition in an exact publication occurrence. It is not another durable kind. One unchanged view may participate in several publications through different audiences, uses, forms, carriers, and availability intervals.

### E.17.0:5 - Worked cases

#### E.17.0:5.1 - Directly authored architecture view

Architecture episteme E concerns exact system T. Maintainability viewpoint episteme P concerns its selected viewpoint-convention structure and states the target-kind, concern, admitted-kind, coverage, and semantic-form rules. E satisfies those fixed rules, so `EpistemeViewpointConformanceRelation(E,P)` obtains and the same E is a `U.View`. No source episteme or A.6.3 viewing is required.

#### E.17.0:5.2 - Query output that is not yet a view

A query over source episteme X constructs episteme Y, and A.6.3 records the source-to-Y viewing relation. Y omits a concern component that exact viewpoint P requires. The construction relation obtains, but conformance does not; Y is not a `U.View` under P. A later repair may create Y2 with different claim content and a new C.2.1 identity.

#### E.17.0:5.3 - One episteme, two viewpoints, one selected use

Unchanged episteme E conforms to safety viewpoint P1 and maintenance viewpoint P2. Two participant-determined conformance occurrences obtain, while the exact use qualification for a current review selects only P1 through one singular `viewpointRef`. E remains one `U.View`; the selection neither creates the P1 conformance nor removes the P2 conformance.

#### E.17.0:5.4 - Viewpoint revision and library repackaging

Moving unchanged viewpoint episteme P into another E.17.1 bundle edition changes packaging only. Revising P's conformance rules creates another episteme `P_new`; conformance of E to `P_old` does not imply conformance to `P_new`. An `EpistemeEditionRelation` may relate the editions, but it is not a conformance occurrence.

#### E.17.0:5.5 - Two publications of one view

View episteme E conforms to P. A web page and a printed sheet use exact forms F1 and F2 borne by exact carriers K1 and K2. Separate expression and bearing relations obtain, and two five-participant publication occurrences make the same E edition available under their own audience, bounded-use, and maximal availability intervals. E remains one view episteme; none of the forms, carriers, supporting relations, or occurrences becomes E or P.

#### E.17.0:5.6 - Cross-view correspondence

A functional view names transformation F and a structural view names module M. A project claim says M realizes F. The shared system EntityOfConcern and aligned diagram positions do not establish realization. Recover exact F and M, apply the direct realization-relation pattern, then identify an assertion episteme about that occurrence if review needs it. A traceability matrix may represent the assertion and occurrence under C.29; its cell is not the realization relation.

#### E.17.0:5.7 - Procedural view is not a method description

A TEVB procedural view E concerns exact holon H and carries claims about methods, order, state, concurrency, and recovery through their exact relations to H. E may conform to procedural viewpoint P and therefore be a `U.View`, but it is not a `U.MethodDescription` because its exact EntityOfConcern is H rather than one admitted method. A true method-description view retargets to the method and uses a viewpoint whose target-kind criterion admits methods.

### E.17.0:6 - Consequences

| Gain | Cost or boundary |
|---|---|
| Directly authored and derived views share one stable membership rule. | A contested view claim requires inspection of one exact viewpoint edition and its fixed rules. |
| One episteme can serve several viewpoints without duplicated view individuals. | Current-use selection must be kept separate from conformance. |
| Viewpoint libraries package references without redefining viewpoint identity. | Authors of a new reusable viewpoint must recover its selected convention structure and exact constituent relations. |
| Multi-view structures and correspondences become inspectable. | A package or graph cannot substitute for collection, structure, or direct-relation recovery. |
| Publication and rendering can evolve independently of view identity. | Publication users must name the exact occurrence, form, and carrier when those distinctions affect work. |

Reopen the pattern when either conformance participant kind changes, the fixed predicate changes, or a proposed condition makes occurrence identity depend on an object other than E and P. Reopen a particular use when the candidate episteme, viewpoint edition, selected describing use, direct correspondence, or publication occurrence changes.

### E.17.0:7 - Rationale and SoTA-Echoing

| Source or practice line | Adopted move | Rejected overread | Practical effect |
|---|---|---|---|
| Architecture-description viewpoint practice, including ISO 42010, used as established practice lineage rather than current architecting SoTA | Separate concern-bearing viewpoint, view, described entity, correspondence, and publication. | A standards vocabulary does not supply FPF identity, obtaining, or work methods. | Readers can recover familiar distinctions while using FPF direct relations and dependent-kind criteria. |
| Model-based view-as-query practice | Treat a query or projection as one possible construction route between separately identified epistemes. | Query execution does not grant `U.View` membership or prove claim preservation. | Direct authoring and generated views use the same independent conformance test. |
| Bidirectional-transformation and model-synchronization research | Keep correspondence predicates, consistency evaluation, and repair work distinct. | A trace link, graph edge, or correspondence episteme does not make the subject relation obtain. | Inconsistency and repair can be stated without collapsing relation, evaluation, and work. |
| FPF constructive relation and episteme architecture | Identify E, P, selected S, and direct relation occurrences independently; derive dependent-kind membership from obtaining conformance. | Do not materialize a universal family record, context slot bundle, or correspondence-model kind. | Ordinary use stays short while disputed uses remain replayable. |

### E.17.0:8 - Relations and ownership

- **C.2.1** owns episteme, claim-content, EntityOfConcern, scheme, and edition identity, including P, E, D, and optional assertion, description, result, basis, and target-claim epistemes. E.17.0 adds dependent `U.Viewpoint` and `U.View` membership to the same individuals.
- **C.13** owns construction of exact `C_viewpoint` and any separately needed collection of selected viewpoints or views.
- **A.6.6** owns the reusable `viewpointConventionDependsOn` vocabulary entry; **A.6.5** owns the four SlotSpecs inside the two RelationSignature declarations. E.17.0 alone owns direct dependency/conformance obtaining and occurrence identity.
- **C.3.2** owns the two optional local explicit-result ValueKinds and any exact local target/stakeholder KindSignature; their values do not own direct judgments.
- **A.22** owns exact method-governed selection of `S_viewpoint` and any separately current multi-view structure. E.17.0 supplies Q and exact candidate occurrences but no pattern or episteme acts.
- **A.6.3** owns optional source-to-receiving viewing construction, including identity viewing. It does not own view membership.
- **E.10.D2** owns Description epistemes and specification-use qualification. A describing-use viewpoint selection does not own conformance.
- **F.18** owns the two relation-kind NameCards; naming metadata does not own relation semantics or admission. **F.9** opens only for an exact cross-context SenseCell relation.
- **E.17.1 and E.17.2** own bundle packaging and engineering viewpoint content. Bundles carry exact references and grant no viewpoint or view membership.
- **E.24.UK** owns one-time public admission of dependent `U.Viewpoint` and `U.View`; E.17.0 owns their stable positive membership predicates.
- **E.24.PUB** owns form expression, carrier bearing, publication availability, and recurrence. **C.29** owns representations and correspondence; neither establishes a world-side subject relation.
- **A.1, A.2.1, A.3.1, A.3.2, A.15.1, and A.15.PROD** own exact actors, role assignments, methods, method descriptions, work, and any separately needed local inception or completion claim.
- **A.10, G.6, and B.3** retain provenance and assurance. **A.6.RCD** is the exit when a needed cross-view or use relation has no direct governor.

### E.17.0:9 - Conformance checklist

1. Candidate E has recoverable C.2.1 claim content, exact EntityOfConcern, and effective reference scheme.
2. `U.ViewpointRef` resolves to one exact viewpoint episteme P; designator, reference, P, selected S, and bundle position remain distinct.
3. P's exact EntityOfConcern is an A.22-selected viewpoint-convention structure over least-powerful exact constituent editions and exact obtaining relations; Q carries all eight organization constraints.
4. Every dependency occurrence has only exact dependent/base epistemes as participants; assertion, description, D, J, evaluation, work, scope, time, scheme, representation, publication, and use remain conditional neighbors.
5. `EpistemeViewpointConformanceRelation` has exactly E and P as participants, the fixed five-condition semantic predicate, and pair-determined positive-occurrence identity.
6. `U.View` membership follows only from an obtaining conformance relation, never from authoring, identity viewing, query, selection, packaging, form, carrier, rendering, or publication.
7. A singular viewpoint reference selects P for one describing use without becoming episteme identity or conformance; multi-selection uses a governed collection.
8. Optional local result values, evaluation, evidence, occurrence designation, decision-use D, and J exist only for a named receiving work or decision need; unsupported evaluation is not a third or negative value.
9. Any multi-view collection, selected structure, or cross-view relation has its own governor and obtaining test; a table, graph, matrix, or shared subject proves none.
10. Form expression, carrier bearing, five-participant publication availability and recurrence, rendering work, and C.29 representation remain distinct from E, P, view membership, and world-side subject relations.
11. Ordinary use stops at a readable direct judgment unless a named consumer needs more structure; authoring stops at the shortest progressive path that produces exact P and its reference.

### E.17.0:End

