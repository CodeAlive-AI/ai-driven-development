## C.3.4 - KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning

> **One-line summary.** A `KindUseAdaptationDeclaration` is a C.2.1 declaration episteme for one named local use of an exact base kind. It pins the base `KindSignature` edition, candidate-feature constraints, vocabulary bindings, intended guard use, and definedness. Applying it yields a `KindUseAdaptationJudgment` with value `true`, `false`, or `unknown`; it creates neither a new kind nor a membership relation. Cross-context use needs an obtaining `KindBridge`, a target declaration, and a separate `KindUseAdaptationCorrespondenceDeclaration` when constraints or bindings differ.

**Status.** Normative in **Part C**. Identifier **C.3.4**.
**Audience.** Engineering managers, architects, reviewers, and editors.

### C.3.4:0 - Use This When

Use C.3.4 when a procedure needs a named local way of using a well-known kind without claiming a new kind. Typical cases include:

- accepting `Vehicle` candidates only when they have ABS;
- using the local spelling `X-Auth` for `AuthHeader`; and
- combining a local candidate criterion with vocabulary bindings.

First useful move: identify the exact base kind and `KindSignature` edition, name the receiving use, and write one declaration of the local use. Keep candidate features in the declaration and route context conditions separately through A.2.6 Scope. The first useful result is a named declaration plus a reproducible `true | false | unknown` judgment for one candidate. If the local distinction becomes a stable conceptual distinction, stop using this declaration as a substitute for kind admission: identify a separate local kind and establish any obtaining `U.SubkindOf` relation independently.

Do not use C.3.4 merely to rename a kind, represent a catalog row, narrow claim scope, or avoid deciding whether a stable new kind is needed. A vocabulary-only change adds no candidate predicate. A guard refusal is a separate use decision, not a `false` classification.

**Depends on.**

- **C.3.1 — U.Kind and U.SubkindOf:** kinds are intensional, `U.SubkindOf` is a partial order, and kinds carry no Scope.
- **C.3.2 — Kind intent, judgment, and extension:** `KindSignature` is a declaration episteme; the exact candidate judgment is three-valued; an extension is a pinned-edition representation of true candidates.
- **C.3.3 — KindBridge and CL^k:** cross-context kind correspondence and R-only bridge consequences.
- **A.2.6 — Context slices and Scopes:** Claim and Work scope over `U.ContextSlice`.
- **C.2.2 and C.2.3:** F–G–R and formality characterize the episteme being assessed.

**Non-goals.** This pattern mandates no repository or notation. A kind-use adaptation declaration is not a governance tier, data policy, mini-type system, new kind, or Scope. Context conditions remain A.2.6 Scope predicates.

### C.3.4:1 - Purpose

Teams often need a local projection of a widely used kind:

- **Constraint:** “For our procedure, take `Vehicle` with ABS only.”
- **Vocabulary:** “Here, `AuthHeader` is called `X-Auth`.”

Cloning a kind for every local use fragments catalogs and multiplies bridges. A declaration of a local use keeps the base-kind identity, makes constraints and bindings explicit, and gives a guard one named, versioned episteme to designate. The declaration is not a new U-kind, record ontology, or classification occurrence.

The practical gains are fewer near-duplicates, cleaner cross-context reuse, deterministic guards, and auditable narrowing instead of an unexplained “this is the version we mean.”

### C.3.4:2 - Context

C.3.1 and C.3.2 are used to say what claims quantify over. A.2.6 is used to say where claims hold. A procedure may still need a local use of a kind for, for example, a compliance procedure, product line, or cohort. `KindUseAdaptationDeclaration` supplies that tailoring without changing the kind or its Scope.

Three objects remain distinct:

1. `KindUseAdaptationDeclaration` states one named local use of a base kind.
2. `KindUseAdaptationJudgment` is the three-valued result for one candidate under pinned declaration and signature editions.
3. `KindUseAdaptationCorrespondenceDeclaration` states deterministic correspondence and loss between two exact adaptation declarations when their constraints or vocabulary bindings differ.

The third object is a C.2.1 declaration episteme. It is not an executable adapter, mapping Method, representation correspondence, obtaining F.9 Bridge, or target judgment.

### C.3.4:3 - Problem

1. **Kind sprawl.** Teams mint near-duplicate kinds such as `Account_PCI` and `Account_Ledger`, and alignment decays.
2. **Hidden constraints.** Informal “we only accept …” statements leak into prose, so guards cannot check them deterministically.
3. **Scope conflation.** Jurisdiction, API version, or another context condition is smuggled into type talk, blurring Scope and Kind.
4. **Cross-context fragility.** Local declarations do not travel safely unless differences in constraints and bindings are stated explicitly.

### C.3.4:4 - Forces

| Force | Tension to resolve |
| --- | --- |
| Local specialization versus common core | A context needs local tailoring without forking the base kind. |
| Expressivity versus determinism | The declaration must express real constraints and remain reproducibly checkable at guard time. |
| Context versus entity constraints | Conditions over `U.ContextSlice` belong to Scope; conditions over the candidate belong to the classification judgment. |
| Reuse versus proliferation | Reuse is useful, but a stable conceptual distinction may warrant a separately identified local kind and independently obtaining `U.SubkindOf` relation. |

### C.3.4:5 - Solution — Declaration, Correspondence, and Judgment

A `KindUseAdaptationDeclaration` is a named, versioned C.2.1 declaration episteme. Its exact `EntityOfConcern` is the base local kind used by the named procedure. Its claim content states:

1. the exact base kind and pinned base `KindSignature` edition;
2. the named receiving use and adaptation type: constraint, vocabulary, or composite;
3. additional direct candidate-feature predicates, when any;
4. vocabulary or notation bindings;
5. the exact `U.ContextSlice` conditions and dependencies under which evaluation is defined;
6. any context expectations routed separately to A.2.6 Scope; and
7. the intended guard use and the declaration episteme's own `U.Formality`, when current.

For classification, evaluate the declaration-local notation:

`J_kindUse(candidate, kind, kindSignatureEdition, adaptationDeclarationEdition, slice) : KindUseAdaptationJudgment ∈ {true, false, unknown}`

The judgment is the three-valued conjunction of the base C.3.2 judgment and every additional direct candidate-feature predicate. It is `false` when the base judgment or any added predicate is known `false`; it is `true` only when the base and every added predicate are known `true`; otherwise it is `unknown` because a required component cannot settle or the candidate is outside its evaluation domain. A vocabulary-only declaration adds no predicate and preserves the base judgment exactly. A guard may decline use on `unknown`; that refusal does not change the judgment to `false`.

An optional pinned-edition representation may list candidates whose exact `KindUseAdaptationJudgment` is `true`. It pins both declaration editions and the slice. The representation has no family-level constructor name here and is not `U.EntitySet`, an A.14 membership occurrence, a new kind, or a direct classification relation. Context conditions such as jurisdiction, API version, and time remain Scope predicates and do not become candidate features.

When two local adaptation declarations differ in constraint predicates or vocabulary bindings, a separate `KindUseAdaptationCorrespondenceDeclaration : U.Episteme` may state the deterministic correspondence, direction, definedness, and loss between those exact declarations. It neither executes a transformation nor creates a Bridge, representation correspondence, or target truth.

A stable conceptual refinement may justify a separately identified local kind and an obtaining C.3.1 `U.SubkindOf` relation. The adaptation declaration, correspondence declaration, judgment, catalog row, and representation create neither object.

### C.3.4:6 - Norms and Invariants

The following norms apply to the declaration epistemes, three-valued judgment, Scope split, and cross-context correspondence boundary.

#### C.3.4:6.1 - Definition and Shape

**KUA-01 (Definition).** A `KindUseAdaptationDeclaration` SHALL be a named, versioned C.2.1 declaration episteme with exact base kind, pinned `KindSignature` edition, named receiving use, adaptation type, direct candidate-feature constraints, vocabulary bindings, definedness conditions, intended guard use, and Scope expectations stated separately under the applicable scope rule. Its formality characterizes this episteme, not the kind or one judgment result.

**KUA-02 (Not a new kind).** A declaration MUST NOT introduce a new `U.Kind`. If the domain needs a stable conceptual refinement, identify another local kind and establish an obtaining `U.SubkindOf` relation under C.3.1; a catalog row or declaration does neither.

**KUA-03 (Determinism and three values).** `KindUseAdaptationJudgment` MUST be reproducible for a fixed candidate, kind, kind-signature edition, adaptation-declaration edition, and slice. It returns `true`, `false`, or `unknown`; implicit `latest` is forbidden and guard refusal does not rewrite `unknown`.

**KUA-04 (Adaptation type).** A declaration SHALL state constraint, vocabulary, or composite. A vocabulary declaration preserves the base judgment. Constraint and composite declarations use only direct candidate-feature predicates and apply the three-valued conjunction rule: any known `false` conjunct gives `false`, all known `true` conjuncts give `true`, and every other combination gives `unknown`.

#### C.3.4:6.2 - Separation of Channels

**KUA-05 (Context versus candidate).** Direct governed features of the exact candidate may contribute to `J_kindUse`. Predicates about `U.ContextSlice`, including jurisdiction, standards, environment, and `Gamma_time`, SHALL be enforced through A.2.6 Scope. The declaration may cite both, but a guard routes them separately and never hides Scope inside classification.

**KUA-06 (Guard use).** A guard MAY designate a `KindUseAdaptationDeclaration` only when its exact edition, base `KindSignature` edition, dependencies, and definedness are recoverable and the required candidate features can be evaluated. A declaration name is not a kind synonym. The guard consumes the three-valued judgment and makes a separate use decision.

#### C.3.4:6.3 - Stable Refinement and Catalog Representation

**KUA-07 (Stable refinement).** When an additional criterion becomes a broadly reused conceptual distinction, review whether another local kind is warranted. If so, identify it under C.3 and C.3.2 and establish any obtaining `U.SubkindOf` relation under C.3.1. Retire or retain the adaptation declaration only for its remaining local use; no declaration, catalog action, or label performs kind admission.

**KUA-08 (Addressability and catalog representation).** Every adaptation-declaration edition used by a guard SHALL have a durable designator or reference that resolves to its exact edition, base `KindSignature` edition, dependencies, definedness, and intended use. A context MAY present those references, constraints, bindings, examples, and cross-context dependencies in a catalog. The catalog row represents the declaration; it is neither the declaration episteme nor a new kind. Consolidation changes the catalog and may motivate a declaration revision, but it does not merge kind identities.

#### C.3.4:6.4 - Cross-Context Use

**KUA-09 (Bridge and correspondence boundary).** For cross-context adapted classification, first establish the obtaining `KindBridge` relation between independently identified source and target kinds. Use the target `KindSignature` edition and a target `KindUseAdaptationDeclaration`. When constraint predicates or vocabulary bindings differ, a separate `KindUseAdaptationCorrespondenceDeclaration` states deterministic correspondence and loss between the exact declaration endpoints. It is not the Bridge occurrence, Bridge assertion, executable adapter, mapping Method, representation correspondence, or target judgment. Evaluate the target `KindUseAdaptationJudgment`; do not copy the source result. `CL^k` and any scope-bridge consequence affect R only.

**KUA-10 (Definedness and fail-closed use).** Each adaptation declaration and correspondence declaration SHALL state its definedness. Outside an adaptation declaration's definedness, or when its required evaluation dependency is unavailable, the target judgment is `unknown`. Outside the correspondence declaration's definedness, that correspondence is unavailable and a guard declines the cross-context use without rewriting an independently evaluated target judgment. In both cases fail-closed is a use disposition, not an assertion of `false`.

### C.3.4:7 - Invariants and Non-goals

- **No Scope leakage.** An adaptation declaration cannot widen or narrow Claim scope G; context conditions are enforced by A.2.6 guards.
- **Identity preservation.** The base kind remains `k`; the declaration does not change its `EntityOfConcern`.
- **Weakest-link unaffected.** Adaptation and correspondence declarations do not alter weakest-link rules on F or R; guards route candidate-feature predicates to the exact judgment and context predicates to Scope.

### C.3.4:8 - Interactions

#### C.3.4:8.1 - With Kinds and Subkinds

Use an adaptation declaration for procedural tailoring. If the criterion becomes conceptual and stable, identify another local kind and establish the exact obtaining `U.SubkindOf` relation. Repeated declaration use, promotion language, and a catalog link do not establish that relation.

#### C.3.4:8.2 - With Judgment and Declarations

- The base `KindSignature` episteme supplies the kind criterion and its own F.
- The separate adaptation declaration supplies additional candidate-feature constraints or vocabulary bindings and may have its own F.
- The exact `KindUseAdaptationJudgment` pins both editions and preserves `unknown`; neither formality value belongs to the kind, candidate, or truth value.
- An optional extension-like result remains only a pinned-edition representation of true adaptation judgments.

#### C.3.4:8.3 - With KindBridge

Cross-context use needs an obtaining `KindBridge`, its separate Bridge assertion, the target adaptation declaration, and—when constraints or bindings differ—a separate correspondence declaration. R receives justified penalties while F, G, and the target judgment remain unchanged. If the target constraint is a stable conceptual refinement, consider a target-side local kind and an independently obtaining `U.SubkindOf` relation.

#### C.3.4:8.4 - With Guards

`Guard_KindUseAdaptation` designates the exact adaptation-declaration and base `KindSignature` editions, evaluates `J_kindUse` for the exact candidate and slice, checks A.2.6 Scope separately, and preserves `unknown` when classification cannot settle. For cross-context use, it composes with `Guard_XContext_Typed` only after the `KindBridge`, Bridge assertion, target declarations, and any correspondence declaration are recoverable. The guard applies justified `Phi(CL)` and `Psi(CL^k)` effects to R and then makes its separate use decision; it changes neither F, G, nor classification truth.

### C.3.4:9 - Anti-patterns and Repairs

| Anti-pattern | Why it is wrong | Repair |
| --- | --- | --- |
| Adaptation declaration treated as a new type | Duplicates the kind and hides the declaration episteme. | Keep the base kind; for a stable conceptual refinement identify another local kind and establish `U.SubkindOf` independently. |
| Scope hidden in an adaptation judgment | Conflates context with candidate features. | Move context predicates to A.2.6 Scope; keep only direct candidate-feature predicates in `J_kindUse`. |
| Unversioned declaration used by a guard | Makes evaluation non-deterministic and unauditable. | Give the declaration a durable designator, pin its edition and dependencies, and decline use when they cannot be recovered. |
| Cross-context use without exact Bridge and declaration objects | Silently reuses source truth. | Establish the `KindBridge` and Bridge assertion, target declarations, and any correspondence declaration; then evaluate the target judgment and apply only justified R penalties. |
| Many declarations with the same local meaning | Produces catalog entropy and inconsistent behavior. | Consolidate redundant declarations; for a stable conceptual distinction, separately identify a local kind and establish its obtaining `U.SubkindOf` relation. |
| Declaration name treated as a kind synonym | Hides constraints and invites misuse. | Designate the exact declaration edition and base kind separately in prose and guards. |

### C.3.4:10 - Worked Examples

#### C.3.4:10.1 - `Vehicle@ABSOnly` Constraint Use

`VehicleABSUse-2026 : KindUseAdaptationDeclaration` designates `Vehicle`, pins its `KindSignature` edition, and adds the direct candidate-feature predicate `hasABS(candidate)=true`. For one vehicle and `TargetSlice`, evaluate `J_kindUse(vehicle, Vehicle, vehicleEdition, absUseEdition, TargetSlice)`. Surface, speed, rig, and time remain Scope predicates. Missing ABS evidence gives `unknown`; a guard may decline use. If ABS becomes a stable conceptual distinction, identify local kind `VehicleWithABS` and establish an obtaining `U.SubkindOf` relation separately.

#### C.3.4:10.2 - `AuthenticatedRequest@Frontend` Vocabulary Use

`FrontendAuthHeaderUse-2026 : KindUseAdaptationDeclaration` binds `authHeader` to local spelling `X-Auth` and adds no candidate criterion. Its judgment therefore equals the base `J(request, AuthenticatedRequest, authEdition, slice)`. Another spelling, row, or field does not classify the request. Cross-context kind use still requires the exact `KindBridge`; local aliases need no correspondence declaration unless their correspondence is relied on across contexts.

#### C.3.4:10.3 - `AdultPatient@Clinic` Composite Use

`ClinicAdultPatientUse-2026 : KindUseAdaptationDeclaration` pins the base adult-patient signature edition and adds the direct candidate-feature criterion `ageAt(patient, slice) >= 21`; `EHR system = X` remains Scope. A date-of-birth record may support the age claim, but record availability is not the patient feature or adaptation criterion.

In Jurisdiction Y, establish the `KindBridge` to the independently identified target kind and use a target adaptation declaration. If the age threshold or interpretation differs, add a `KindUseAdaptationCorrespondenceDeclaration` whose endpoints are the two exact adaptation declarations and whose content states direction, rule, loss, and definedness. That declaration creates no Bridge or target truth. Evaluate the target `J_kindUse`; an unavailable date-of-birth dependency yields `unknown`, the guard declines use separately, and R receives only justified Bridge penalties.

### C.3.4:11 - Authoring and Review Guidance

#### C.3.4:11.1 - Authoring a Declaration Card

A card or catalog row may represent the adaptation declaration's designator, base kind, pinned kind-signature edition, declaration edition, type, intended use, candidate-feature constraints, separately routed Scope expectations, bindings, definedness, examples, known Bridge and correspondence declarations, and any stable-distinction review note. The card is not the declaration episteme or a new ontic object.

Rules of thumb:

- Keep candidate predicates small and testable.
- Put context predicates in Scope, not in the adaptation judgment.
- If several teams reuse the same stable conceptual constraint, review whether a separately identified local kind and an obtaining `U.SubkindOf` relation are warranted; declaration reuse establishes neither.

#### C.3.4:11.2 - Reviewer Checklist

1. Is the adaptation declaration durably identified and versioned?
2. Is its type—constraint, vocabulary, or composite—stated correctly?
3. Are candidate features and context conditions separated?
4. Is evaluation deterministic, with no implicit `latest`?
5. Does the guard evaluate the exact three-valued judgment, check Scope separately, and keep refusal distinct?
6. Does every cross-context use recover the `KindBridge`, Bridge assertion, target declarations, any correspondence declaration, target judgment, and only justified R penalties?
7. Is declaration consolidation sufficient, or does a stable conceptual distinction warrant a separately identified local kind and independently obtaining subkind relation?

### C.3.4:12 - Conformance Checklist

| ID | Requirement |
| --- | --- |
| **KUA-01** | `KindUseAdaptationDeclaration` is a C.2.1 declaration episteme with exact base kind, pinned `KindSignature` edition, declaration edition, intended use, constraint or binding content, definedness, and its own formality when current. |
| **KUA-02** | It creates no new kind or `U.SubkindOf`; any stable refinement is independently identified and checked under C.3.1. |
| **KUA-03** | `J_kindUse(candidate, kind, kindSignatureEdition, adaptationDeclarationEdition, slice)` is reproducible and returns `true`, `false`, or `unknown`; guard refusal is separate. |
| **KUA-04** | Vocabulary declarations preserve the base judgment; constraint and composite declarations use direct candidate-feature predicates and apply false-if-any-false, true-if-all-true, otherwise-unknown conjunction. |
| **KUA-05** | Context conditions remain A.2.6 Scope predicates and are not folded into classification. |
| **KUA-06** | A guard designates exact declaration editions, evaluates the exact candidate, and does not treat a declaration name as a kind synonym. |
| **KUA-07** | Broad stable reuse triggers review for a separately identified local kind and an obtaining subkind relation; a declaration or catalog row does not perform promotion. |
| **KUA-08** | Every guard-addressable declaration resolves durably to its exact edition and dependency editions; a catalog represents those references without becoming ontology. |
| **KUA-09** | Cross-context use establishes the exact `KindBridge`, target declarations, and any separate `KindUseAdaptationCorrespondenceDeclaration` before evaluating the target judgment. |
| **KUA-10** | Adaptation non-settlement yields target `unknown`; correspondence non-settlement blocks the cross-context use without rewriting an independent target judgment; fail-closed is never `false`. |

### C.3.4:End

