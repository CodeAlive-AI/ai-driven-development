## C.3.4 - KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning

> **One-line summary.** Use a `KindUseAdaptationDeclaration` when a procedure needs a narrower or differently named use of an existing kind without defining another kind. The declaration pins the base `KindSignature` edition, local candidate constraints or vocabulary bindings, intended guard use, and applicability. Check admissibility before returning `true`, `false`, or `unknown`. A locality change first triggers kind-identity comparison: the same kind needs no `KindBridge`; distinct kinds need one only when its exact correspondence predicate obtains.

**Status.** Normative in **Part C**. Identifier **C.3.4**.
**Audience.** Engineering managers, architects, reviewers, and editors.

### C.3.4:0 - Use This When

Use C.3.4 when a procedure needs a named local way of using an existing kind without claiming another kind. Typical cases include accepting `Vehicle` candidates only when they have ABS, using local spelling `X-Auth` for `AuthHeader`, or combining a candidate constraint with vocabulary bindings.

First identify the base kind, exact `KindSignature` edition, receiving use, and meanings of local names or predicates. Write one declaration for candidate constraints or vocabulary bindings and route claim-scope conditions separately. Check candidate and slice admissibility, then evaluate one candidate. Stop with the declaration and first reproducible result. If the distinction becomes a stable kind, identify it separately and establish any obtaining `U.SubkindOf` fact under C.3.1.

Do not use C.3.4 merely to rename a kind, represent a catalog row, narrow claim scope, or avoid deciding whether another kind is needed. A vocabulary-only change adds no candidate predicate. `not-applicable`, `unknown`, and a guard refusal are different results.

**Depends on.**

- **C.3.1 — U.Kind and U.SubkindOf:** kind identity follows the membership distinction; `U.SubkindOf` facts form a preorder and kinds carry no Scope.
- **C.3.2 — Kind intent, admissibility, judgment, and extension:** `KindSignature` is a declaration episteme; admissibility precedes the three-valued judgment.
- **C.3.3 — KindBridge and CL^k:** a directional correspondence only between independently identified distinct kinds, plus R-only bridge consequences.
- **A.2.6 — Context slices and Scopes:** Claim and Work scope over `U.ContextSlice`.
- **C.2.2 and C.2.3:** F–G–R and formality characterize the episteme being assessed.

**Non-goals.** This pattern mandates no repository or notation. A kind-use adaptation declaration is not a governance tier, data policy, mini-type system, kind, `KindBridge`, or Scope.

### C.3.4:1 - Purpose

Teams often need a local projection of a widely used kind: `Vehicle` with ABS for one procedure, or local spelling `X-Auth` for `AuthHeader`. Cloning a kind for every use fragments catalogs and creates false bridge pressure. A local-use declaration keeps the base-kind identity, makes constraints and bindings explicit, and gives a guard one versioned episteme to designate. It is not another kind, classification occurrence, or record ontology.

### C.3.4:2 - Context

C.3.1 and C.3.2 say what claims classify; A.2.6 says where claims hold. A procedure may still tailor use for a compliance procedure, product line, or cohort without changing the kind.

Three objects remain distinct:

1. `KindUseAdaptationDeclaration` states one named use of a base kind.
2. `KindUseAdaptationJudgment` is the three-valued result for one admissible candidate under pinned declaration and signature editions.
3. `KindUseAdaptationCorrespondenceDeclaration` records how one exact source declaration corresponds to one exact target declaration when their constraints or vocabulary bindings differ.

The third object is a C.2.1 declaration episteme. Its effective scheme makes source, target, and rule designations interpretable. It is not an executable adapter, mapping Method, representation correspondence, obtaining F.9 relation, `KindBridge`, or target judgment.

### C.3.4:3 - Problem

1. **Kind sprawl.** Teams mint near-duplicates for every procedure.
2. **Hidden constraints.** Informal acceptance rules leak into prose and cannot be replayed.
3. **Scope conflation.** Jurisdiction, API version, or another scope condition is smuggled into kind identity.
4. **Automatic bridge pressure.** A changed source or team is treated as proof of another kind and a bridge.
5. **Collapsed outcomes.** A non-applicable candidate, unsettled admissible candidate, and guard refusal are reported as one `unknown` or `false` result.

### C.3.4:4 - Forces

| Force | Tension to resolve |
| --- | --- |
| Local specialization vs common core | A use needs tailoring without forking the base kind. |
| Expressivity vs determinism | Real constraints must remain reproducibly checkable. |
| Applicability vs uncertainty | Candidate/slice mismatch stops before the judgment; missing facts preserve `unknown`. |
| Scope vs candidate constraints | Conditions on ClaimScope stay under A.2.6; conditions on the candidate enter classification. |
| Reuse vs proliferation | Stable conceptual distinctions may warrant a separately identified kind, but declaration reuse alone does not. |
| Locality vs identity | A changed locality prompts comparison of membership distinctions, not automatic bridging. |

### C.3.4:5 - Solution — Declaration, Correspondence, and Judgment

A `KindUseAdaptationDeclaration` is a named, versioned C.2.1 declaration episteme about one local use. The base kind is its `EntityOfConcern`; its effective scheme gives meaning to declaration names and predicates. Its claim content states:

1. the exact base kind and pinned base `KindSignature` edition;
2. the receiving use and adaptation type: constraint, vocabulary, or composite;
3. additional directly governed candidate conditions, when any;
4. vocabulary or notation bindings;
5. exact candidate and slice applicability plus dependencies;
6. scope expectations routed separately through A.2.6; and
7. intended guard use and this declaration episteme's formality, when current.

First evaluate adaptation admissibility. A candidate rejected by the base signature's ValueKind, an adaptation-specific candidate requirement needed merely to form the question, or the declared slice applicability is `not-applicable`; no adaptation judgment is formed. For an admissible request, use:

`J_kindUse(candidate, kind, kindSignatureEdition, adaptationDeclarationEdition, slice) ∈ {true, false, unknown}`

The judgment conjoins the base C.3.2 judgment with every added candidate-condition predicate. A known `false` gives `false`; all known `true` gives `true`; unresolved required facts give `unknown`. A vocabulary-only declaration adds no predicate and preserves the base judgment. A guard may decline use on `not-applicable` or `unknown` without rewriting either.

An optional pinned-edition representation may list admissible candidates judged `true`. It is not `U.EntitySet`, A.14 membership, another kind, or a direct classification relation. Scope conditions stay under A.2.6 rather than becoming kind identity.

When a use moves to another practice, source, or team, compare the base-kind membership distinctions first:

- if the same kind continues, use the declaration and signature edition selected for the receiving use and make a fresh receiving judgment; no `KindBridge` exists merely because locality changed;
- if independently identified kinds are distinct and the use claims a directional correspondence, establish the C.3.3 `KindBridge`; use the receiving signature and adaptation declaration and make a fresh receiving judgment; and
- if two adaptation declarations differ in constraints or bindings, a separate `KindUseAdaptationCorrespondenceDeclaration` may name source declaration as EntityOfConcern and state target, direction, deterministic rule, definedness, loss, and effective scheme. It creates no bridge or target truth.

A stable conceptual refinement may justify another kind and an obtaining C.3.1 subkind fact. A declaration, correspondence, judgment, catalog row, or representation creates neither.

### C.3.4:6 - Norms and Invariants

#### C.3.4:6.1 - Definition and Shape

**KUA-01 (Definition).** A `KindUseAdaptationDeclaration` SHALL be a named, versioned C.2.1 declaration episteme with exact base kind as EntityOfConcern, effective scheme, pinned base signature, receiving use, adaptation type, candidate constraints, vocabulary bindings, applicability, dependencies, intended guard use, and separate scope expectations. Its formality characterizes the episteme.

**KUA-02 (Not a new kind).** A declaration MUST NOT introduce a kind or subkind fact. Stable refinement requires an independently recovered kind and C.3.1 obtaining test.

**KUA-03 (Admissibility before judgment).** Fixed candidate, kind, base-signature edition, adaptation-declaration edition, and slice first yield `admissible` or `not-applicable`. Only an admissible request yields `true`, `false`, or `unknown`; implicit `latest` and guard-result coercion are forbidden.

**KUA-04 (Adaptation type).** A vocabulary declaration preserves the base judgment. Constraint and composite declarations use governed candidate conditions: any known `false` gives `false`, all known `true` gives `true`, and unresolved required facts give `unknown`.

#### C.3.4:6.2 - Separation of Channels

**KUA-05 (Scope versus candidate).** Conditions of the candidate may enter the adaptation judgment. Claim- or Work-scope conditions remain under A.2.6. A declaration may cite both, but a guard routes them separately.

**KUA-06 (Guard use).** A guard MAY designate a declaration only when its exact edition, base signature, dependencies, applicability, and candidate conditions are recoverable. It checks admissibility before the judgment and makes its use decision separately.

#### C.3.4:6.3 - Stable Refinement and Catalog Representation

**KUA-07 (Stable refinement).** Broad reuse triggers a review for another kind. If that kind and an obtaining subkind fact are established, retain the adaptation declaration only for any remaining local use or retire it. Declaration reuse, catalog action, or labeling performs no kind admission and establishes no subkind fact.

**KUA-08 (Addressability).** Every guard-addressable adaptation declaration resolves to its exact edition, base signature, dependencies, applicability, and intended use. A correspondence declaration also resolves its source declaration as EntityOfConcern, target declaration, direction, deterministic rule, effective scheme, definedness, and loss. A catalog represents those references; it is neither the declaration episteme nor ontology, and consolidation does not merge kind identities.

#### C.3.4:6.4 - Cross-local Use

**KUA-09 (Identity check before bridge).** A locality change first compares exact base-kind definitions. Same-kind reuse needs no `KindBridge` but still uses the receiving declaration and a fresh judgment. Distinct-kind use establishes a `KindBridge` only when its directional correspondence predicate obtains. Differing adaptation constraints or bindings may additionally require an exact correspondence declaration. Source judgments are never copied as receiving truth; justified bridge consequences affect R only.

**KUA-10 (Definedness and fail-closed use).** Outside adaptation applicability, return `not-applicable` and form no judgment. For an admissible request with an unavailable dependency, return `unknown`. Outside correspondence definedness, the guard declines that cross-local use without rewriting an independently evaluated receiving result.

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

A locality change first prompts kind-identity comparison. When the same base kind continues, select the receiving signature and adaptation declaration and evaluate a fresh candidate result without a `KindBridge`. When two independently identified kinds are distinct and an exact directional correspondence is relied on, establish the C.3.3 `KindBridge`, its assertion, the receiving declaration, and any needed adaptation-correspondence declaration. Only justified bridge penalties affect R; F, G, admissibility, and classification truth remain unchanged.

#### C.3.4:8.4 - With Guards

`Guard_KindUseAdaptation` designates exact adaptation and base-signature editions, checks admissibility, evaluates an admissible candidate, checks Scope separately, and keeps `not-applicable`, `unknown`, and refusal distinct. For distinct-kind cross-local use, it composes with the C.3.3 guard only after the bridge and receiving declarations are recoverable. For same-kind reuse, it performs the fresh receiving evaluation without inventing a bridge.

### C.3.4:9 - Anti-patterns and Repairs

| Anti-pattern | Why it is wrong | Repair |
| --- | --- | --- |
| Adaptation declaration treated as a new type | Duplicates the kind and hides the declaration episteme. | Keep the base kind; for a stable conceptual refinement identify another local kind and establish `U.SubkindOf` independently. |
| Claim- or Work-scope condition hidden in an adaptation judgment | Conflates the candidate with where a claim or Work applies. | Move the scope condition to A.2.6; keep candidate constraints and declaration applicability explicit. |
| Unversioned or applicability-free declaration used by a guard | Makes evaluation non-replayable. | Give the declaration a designator, pin its edition and dependencies, state applicability, and distinguish `not-applicable` from `unknown`. |
| Locality change treated as automatic bridge | Splits the same kind or transfers source truth. | Compare kind definitions first. Same-kind reuse needs no bridge and still gets a fresh receiving result; distinct-kind use needs an obtaining C.3.3 correspondence. |
| Many declarations with the same local meaning | Produces catalog entropy and inconsistent behavior. | Consolidate redundant declarations; for a stable conceptual distinction, separately identify a local kind and establish its obtaining `U.SubkindOf` relation. |
| Declaration name treated as a kind synonym | Hides constraints and invites misuse. | Designate the exact declaration edition and base kind separately in prose and guards. |

### C.3.4:10 - Worked Examples

#### C.3.4:10.1 - `Vehicle@ABSOnly` Constraint Use

`VehicleABSUse-2026` designates `Vehicle`, pins its signature, and adds the governed candidate condition that the vehicle has ABS. A physical vehicle in the declared slice is admissible; missing ABS support yields `unknown`, while a non-vehicle input is `not-applicable`. Surface, rig, and time conditions used only to bound the claim remain Scope. If ABS becomes a stable classification distinction, recover another kind and test its subkind relation separately.

#### C.3.4:10.2 - `AuthenticatedRequest@Frontend` Vocabulary Use

`FrontendAuthHeaderUse-2026` binds `authHeader` to local spelling `X-Auth` and adds no candidate condition. Its judgment therefore equals the admissible base judgment. Moving the same exact request kind to another team requires a fresh receiving evaluation but no `KindBridge` merely because the team or spelling changed. If two independently identified request kinds differ, establish any bridge separately.

#### C.3.4:10.3 - `AdultPatient@Clinic` Composite Use

`ClinicAdultPatientUse-2026` pins the base adult-patient signature and adds the candidate condition `ageAt(patient, slice) >= 21`; the chosen clinic and claim window remain separately governed scope/applicability values. A person in the declared candidate domain is admissible; unavailable birth support yields `unknown`.

In Jurisdiction Y, first compare the exact patient-kind membership distinctions. If the same kind continues, use the Y declaration and evaluate afresh without a bridge. If the threshold or interpretation makes a distinct target kind and a directional correspondence is relied on, establish the `KindBridge`. A separate adaptation-correspondence declaration may then state how the two exact use declarations differ. Neither object transfers source truth.

### C.3.4:11 - Authoring and Review Guidance

An adaptation card may show its declaration designator, base kind, effective scheme, pinned base-signature and declaration editions, adaptation type, intended use, candidate constraints, bindings, separately routed Scope, applicability, examples, known bridge or correspondence declarations, and a stable-distinction review note when current. A correspondence card shows its source declaration as EntityOfConcern and names target, direction, rule, definedness, loss, and effective scheme. A card represents the declaration; it is not the declaration or another kind.

Rules of thumb:

- Keep candidate conditions small and governed.
- Check ValueKind and applicability before the three-valued judgment.
- Put claim-scope conditions in Scope, not kind identity.
- Treat locality as a comparison cue. Require a bridge only for distinct kinds with an obtaining correspondence.
- If several teams reuse one stable conceptual constraint, review whether another kind is warranted; reuse alone establishes none.

Reviewer questions:

1. Are the exact base kind and declaration editions recoverable?
2. Is the type—constraint, vocabulary, or composite—correct?
3. Are candidate conditions, applicability, and ClaimScope separated?
4. Does evaluation distinguish `not-applicable`, `true`, `false`, `unknown`, and guard refusal?
5. On locality change, was kind identity compared before any bridge was claimed?
6. For distinct-kind use, do the bridge predicate, receiving declaration, fresh judgment, any adaptation correspondence, and only justified R consequence remain separate?
7. Does a stable conceptual distinction warrant another kind, or is the declaration sufficient?

### C.3.4:12 - Conformance Checklist

| ID | Requirement |
| --- | --- |
| **KUA-01** | The declaration is a C.2.1 episteme with base kind as EntityOfConcern, effective scheme, pinned editions, use, constraints/bindings, applicability, dependencies, and its own formality. |
| **KUA-02** | It creates no kind or subkind fact. |
| **KUA-03** | Admissibility precedes the three-valued judgment; guard refusal is separate. |
| **KUA-04** | Vocabulary preserves the base judgment; constraint/composite uses governed candidate conditions and the three-valued conjunction rule. |
| **KUA-05** | Claim-scope conditions remain under A.2.6 and are not folded into kind identity. |
| **KUA-06** | A guard designates exact editions, checks applicability, evaluates the exact candidate, and makes a separate use decision. |
| **KUA-07** | Stable refinement is independently identified and checked; declaration reuse does not promote it. |
| **KUA-08** | Guard-addressable adaptation and correspondence declarations resolve to their exact editions and all interpretation, dependency, definedness, direction, and loss values required by section 6.3; a catalog remains representation and does not merge kind identities. |
| **KUA-09** | Locality change triggers identity comparison. Same-kind reuse has no bridge and still gets a fresh receiving judgment; distinct-kind use requires an obtaining C.3.3 correspondence before bridge reliance. |
| **KUA-10** | Non-applicability forms no judgment; unavailable admissible dependencies yield `unknown`; correspondence failure blocks use without rewriting the receiving result. |

### C.3.4:End

