## C.3.2 - Kind Intent, Membership Judgment, and Extension

> **Type:** Kind declaration and classification pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### C.3.2:0 - Use This When

Use this pattern when repeated typed reasoning needs one explicit kind criterion, when one exact entity or non-entity value must first be checked as applicable and then judged against that criterion in one context slice, or when a named use needs a representation of the candidates currently judged `true`.

**What goes wrong if missed.** A kind is confused with its declaration, a practice label splits one kind, a measurement or schema label creates membership, an out-of-domain request becomes `unknown`, missing information becomes `false`, a set becomes ontology, or a guard decision rewrites the classification.

**What this buys.** A practitioner can state an ordinary result, pin the declaration and slice when reliance requires it, distinguish `not-applicable` from `true`, `false`, and `unknown`, and materialize an extension only for a receiving query or review. A manager can separately change declaration formality, assurance for a relied-on assertion, or claim scope without treating them as one maturity ladder.

**Primary EntityOfConcern.** One classification use: exact candidate, kind, `KindSignature` edition, context slice, pre-judgment admissibility, and—only when admissible—the judgment value.

**First useful move.** Write the readable result first: `Pump #14 counts as a cooling pump in this plant slice because it satisfies the declared cooling-pump condition.` Before evaluating, confirm that a pump candidate and this slice are within the declaration's candidate domain and applicability. Cite support only when the receiving use relies on it; create a reusable signature or extension only for repeated or set-consuming use.

**Not this pattern when.** Use the direct subject pattern to establish the candidate and the exact quality, relation, episteme, status, publication occurrence, or other condition named by the criterion; A.14 for membership in a collection; C.3.3 for a claimed correspondence between distinct kinds; C.29 for a claim-bearing mathematical representation; and `E.24.UK` for admission of another durable public kind.

### C.3.2:1 - Problem Frame

A kind can support useful typed reasoning without acquiring its own public `U.*` label. Its intent may need a reusable declaration, one candidate may need a current judgment, and a query may need a set representation. These are different objects. Before a judgment exists, the candidate must satisfy the declared candidate `ValueKind` and the slice must lie within declared applicability. Once admissible, the governed condition named by the criterion settles `true` or `false` when known; missing support or an unavailable dependency yields `unknown`.

The rule about evidence is conditional, not lexical. An observation used merely to support a claim does not create an independently governed quality or relation. But a criterion may directly concern an episteme, an obtaining registration or certification relation, a publication occurrence, legal status, or another governed fact. In that case its direct pattern decides whether that very condition obtains; calling the same object evidence in another use does not erase its criterion role. This concept-level rule requires no particular ontology language, schema technology, rule engine, or programming type system.

### C.3.2:2 - Problem

The shorthand `MemberOf(e,k,slice)` is unsafe because readers can take it as an A.14 collection relation, an ontic occurrence, a classification result, a database lookup, or a guard. It also hides whether the request was applicable. C.3.2 restores a declaration, an admissibility result, a three-valued judgment only for admissible candidates, and an optional representation while leaving candidate identity and the criterion's governed conditions with their direct patterns.

### C.3.2:3 - Forces

| Force | Tension |
| --- | --- |
| Readable use vs reusable declaration | One case should stay ordinary, while repeated classification needs a stable criterion and assumptions. |
| Admissibility vs uncertainty | Candidate or slice mismatch means no judgment; missing knowledge for an admissible request means `unknown`. |
| Criterion condition vs evidentiary use | The direct condition named by the criterion can be physical, relational, epistemic, institutional, or publication-dependent; use as evidence alone creates none of them. |
| False vs unknown | Known criterion failure differs from unavailable support or dependency. |
| Intent vs extension | A declaration can stay fixed while candidate state or selected slice changes the true-candidate set. |
| Set use vs ontology | A query may need a set without creating a collection holon, direct relation occurrence, or `U.EntitySet`. |
| Scope vs evaluation input | Claims may be scoped; the kind is not. The context slice is an explicit input. |

### C.3.2:4 - Four Objects and One Applicability Result

| Object | Meaning | Identity and governor |
| --- | --- | --- |
| `U.Kind` individual and order | The intensional kind and any obtaining `U.SubkindOf` facts used by typed reasoning. | C.3 and C.3.1; not this declaration, a practice/source label, or a new public-kind admission. |
| `KindSignature` | A `U.Signature` declaration episteme whose exact `EntityOfConcern` is the kind. | A.6.0 and C.2.1 govern the episteme and its editions. |
| classification judgment | One evaluation for an admissible exact candidate, kind, signature edition, and slice, returning `true`, `false`, or `unknown`. | C.3.2; it is not a direct relation occurrence or guard result by default. |
| `KindExtension(k, slice)` | An optional set-valued representation of admissible candidates judged `true` for the pinned signature edition and slice. | Local calculation unless C.29 governs a claim-bearing use. |

`ClassificationAdmissibility(candidate, kind, signatureEdition, slice)` returns `admissible` or `not-applicable`. It is a precondition result, not another kind or membership value. `not-applicable` means the candidate fails the declared candidate `ValueKind`/interpretation or the slice falls outside signature applicability; no classification judgment is formed.

Scope is not attached to the kind. A `KindSignature` episteme may have its own `U.ClaimScope`; a separate classification assertion has the scope of that assertion; and `U.ContextSlice` remains an evaluation input.

### C.3.2:5 - KindSignature Declaration

Author a reusable `KindSignature` only when a named receiving use needs the criterion and assumptions to persist across more than one classification. Its claim content declares:

- the exact kind that is its `EntityOfConcern`;
- the candidate `ValueKind` or exact value interpretation admitted as input;
- the membership condition in terms of directly governed candidate qualities, relations, constructive grounding, epistemes, registrations, certifications, publications, legal statuses, or other exact conditions;
- the exact `U.ContextSlice` applicability in which the evaluation may be formed;
- the effective `U.ReferenceScheme`;
- named assumptions, dependencies, standards, versions, units, and temporal policy;
- its `U.Formality`; and
- an optional `ExtentRule` for a named extension-consuming use.

In A.6.0 terms, `SubjectKind` is the broad candidate kind and `RangedValueKind` is `{true, false, unknown}`. `not-applicable` is returned before this ranged evaluation. `ExtentRule` is declaration content, not a new ontic relation. Formality characterizes the declaration episteme, not the kind, candidate, truth, or extension. A changed membership condition, candidate-domain declaration, `EntityOfConcern`, applicability, or effective scheme identifies another signature edition; C.3.1 separately decides kind continuity.

### C.3.2:6 - Admissibility and One Candidate Judgment

For exposition, this pattern uses:

`A(candidate, kind, signatureEdition, slice) ∈ {admissible, not-applicable}`

and, only when `A = admissible`:

`J(candidate, kind, signatureEdition, slice) ∈ {true, false, unknown}`

These are local result notations, not newly admitted kinds, A.14 membership occurrences, direct classification relations, or evidence relations. For a fixed candidate, kind, signature edition, and slice, unchanged governed conditions yield the same result; the slice resolves concrete versions and an explicit temporal selector rather than implicit `latest` or `current`.

1. **Recover the candidate first.** An entity is already individuated under its direct pattern. A non-entity value keeps the identity, unit, scale, and interpretation supplied by its governor.
2. **Pin the inputs.** Name candidate, kind, exact signature edition, and exact slice; avoid implicit `latest` or `current`.
3. **Check admissibility.** If the candidate does not satisfy the declared candidate `ValueKind` or interpretation, or the slice is outside declared applicability, return `not-applicable` and stop. Do not form `J`.
4. **Evaluate the governed condition.** For an admissible candidate, a satisfied criterion gives `true`; a known failed criterion gives `false`.
5. **Keep non-settlement visible.** Missing support or an unavailable declared dependency gives `unknown`, not `false`.
6. **Distinguish condition from evidentiary use.** A measurement result, source episteme, certification, registration, publication occurrence, legal-status relation, or record may itself be a criterion condition only when the signature says so and its direct pattern makes that condition obtain. Its mere use as evidence for some other condition creates neither that condition nor membership.
7. **Separate guard disposition.** A guard checks admissibility, scope coverage, and any judgment as separate predicates. It may decline use on `not-applicable` or `unknown` without converting either to `false`.

When a separate claim-bearing classification assertion is current, it is a C.2.1 episteme. Its content designates the candidate, kind, signature edition, slice, admissibility, any judgment, and relied-on support. Its exact `EntityOfConcern` is the governed entity about which classification matters; a value classification may stay in another claim's content rather than fabricating a value-shaped entity. The assertion creates neither candidate nor kind.

A domain that genuinely needs a durable classification-relation occurrence must supply a separate direct pattern with exact participants, obtaining condition, identity, and relation to these results. C.3.2 does not mint that occurrence.

### C.3.2:7 - Extension as Representation

Materialize `KindExtension(k, slice)` only when a named query, quantification, comparison, review, or publication needs the current true-candidate set.

- Pin the signature edition even though the compact name shows only `k` and `slice`.
- State the candidate domain without inventing `U.EntitySet`.
- Include exactly admissible candidates whose judgment is `true`. Keep `unknown` and `not-applicable` distinct when the receiver needs those exclusions explained.
- Treat braces, rows, indexes, or database results as representations. They create neither a collection holon, A.14 membership occurrence, direct classification relation, nor criterion condition.
- Use C.29 when the represented set changes a claim-bearing use; otherwise the extension may remain a local calculation.

Candidate state or a later slice can change an extension without changing the signature or kind. An extension row cannot repair an inconsistent declaration or subkind fact.

### C.3.2:8 - Subkind Comparison and Change

Whenever `SubkindOfObtains(k1,k2)` holds under C.3.1, its practical consequence is checked only where both candidate requests are admissible under the aligned declarations:

> For the same candidate and slice, an admissible `true` judgment for `k1` must not coexist with an admissible `false` judgment for `k2` within the relation's declared applicability.

C.3.1 decides whether exact criterion entailment or exhaustive evaluation over a deliberately closed finite domain makes the relation obtain. Non-exhaustive classifications support its assertion or expose a counterexample; they do not establish an open-domain relation. A `not-applicable` request is outside the comparison. Cross-local use first compares kind identities: reuse the same kind directly when its membership distinction continues; only distinct kinds with an obtaining correspondence use C.3.3. A bridge never transfers source classification truth.

Keep these changes distinct:

| Change | Direct consequence | What does not follow automatically |
| --- | --- | --- |
| practice, source, team, or locality changes | compare the exact kind definitions and declaration meanings | another kind or `KindBridge` |
| two distinct kinds and a directional correspondence are current | test C.3.3 obtaining and evaluate the receiving candidate afresh | transferred source truth |
| criterion, candidate domain, applicability, `EntityOfConcern`, or scheme changes | another `KindSignature` edition; C.3.1 decides kind continuity | another kind merely by edition |
| candidate fails ValueKind or slice applicability | `not-applicable`; no judgment | `unknown` or `false` |
| candidate state changes | reevaluate in the relevant slice when admissible | a new signature or kind |
| support or dependency becomes unavailable | `unknown` for an admissible request | `not-applicable` or known `false` |
| publication form changes | another form or carrier may express the same episteme | another signature, kind, or classification |

### C.3.2:9 - Required Worked Cases

#### C.3.2:9.1 - Physical pump

`CoolingPumpSignature-2` admits physical pump candidates and applies in plant slice `S-14`. Pump #14 is independently identified as a physical pump, so the request is admissible. Governed flow, heat-transfer, and operating-state conditions satisfy the criterion; a calibrated measurement result supports that claim without becoming the pump or its performance. The result is `true`. A maintenance-query extension may represent Pump #14 but does not create its classification.

#### C.3.2:9.2 - Episteme and publication form

Maintenance-instruction episteme `MI-22` is admissible for `DiagnosticInstructionKind` and is evaluated through its claim-bearing content and governed subject. `MI-22-PDF-Layout` and `MI-22-HTML-Layout` are different publication forms for the chosen episteme edition; files that bear them are presentation carriers. Arrangement, form, carrier, or encoding alone changes neither the episteme, criterion satisfaction, kind, nor judgment.

#### C.3.2:9.3 - Non-entity temperature value

Value `87 °C`, with declared scale, unit, interpretation, and time, is admissible for `HighTemperatureValueKind` when the signature's ValueKind accepts that quantity. It can then be judged against the declared interval without fabricating a value-shaped entity.

#### C.3.2:9.4 - Schema label

A row carries label `Customer`, but the claim asks whether account holder #441 is a contractual customer. If the kind admits account-holder Systems or persons rather than database rows, the row itself is not an admissible candidate. For the actual account holder, the label may support recovery of the governed contractual relation but does not make that relation obtain. A different row-shape kind could make the row admissible under its own criterion.

#### C.3.2:9.5 - Unavailable measurement

Pump #14 remains an admissible physical candidate in later slice `S-15`, but a required flow-measurement dependency is unavailable. The judgment is `unknown`. A safety guard may decline reliance; it does not return `false` or remove the pump from a historical `S-14` extension.

#### C.3.2:9.6 - Not-applicable request

The value `87 °C` is submitted to `CoolingPumpSignature-2`, whose candidate ValueKind is physical pump. The request is `not-applicable`; no cooling-pump judgment is formed. Lack of a pump judgment says nothing about whether the temperature value is known.

#### C.3.2:9.7 - Registration-defined membership

`RegisteredSupplierKind` declares supplier candidates and requires an exact obtaining registration-status relation under the current register rule. Supplier #27 is admissible. If that governed relation obtains, it is part of the membership condition even though a registration episteme may also be used as evidence. A copied row or certificate image alone does not create the relation. This preserves legitimate institutional kinds without treating every record as a world-side fact.

### C.3.2:10 - Additional Transfer Cases

| Case | Repaired use |
| --- | --- |
| Vehicle and PassengerCar | Check candidate admissibility and use C.3.1's exact obtaining branch; a registry result is an extension representation, not `U.EntitySet`. |
| AuthenticatedRequest | Name the standard and key-validity dependency. An admissible request with unavailable key support yields `unknown`; a non-request value is `not-applicable`. |
| AdultPatient | Pin jurisdictional threshold, measurement time, and candidate identity. A patient with missing birth support is `unknown`; a non-person value rejected by ValueKind is `not-applicable`. |

### C.3.2:11 - Work Boundary

Classification does not weaken the work ontology:

- `U.Work` is the admitted kind;
- `W : U.Work` is one independently grounded dated 4D work occurrence under its direct pattern;
- a plan, expected-work item, log, card, database row, assertion, or description about W is a separate episteme; and
- performer assignment, enacted method, temporal extent, containing system, affected referent, material binding, resource use, transformation, production, result, delivery, and acceptance remain separately governed.

A kind may classify an already identified W. A kind symbol, work label, plan, or record never occupies W's individual position, and record existence does not make planned Work actual.

### C.3.2:12 - Authoring Rhythm

1. Start with one readable classification sentence and its practical use.
2. Recover the exact candidate and the governed criterion conditions before discussing support.
3. Reuse an existing signature edition only when it truly governs candidate ValueKind, criterion, applicability, scheme, and dependencies.
4. Check admissibility. Stop with `not-applicable` when candidate or slice lies outside the declaration.
5. For an admissible request, return `true`, `false`, or `unknown` without folding in the guard decision.
6. Create an extension only for a named set-consuming use.
7. If a separate assertion is required, give its C.2.1 episteme the exact EntityOfConcern, content, scope, support use, and edition.

### C.3.2:13 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C32-1` | Kind, `KindSignature`, pre-judgment admissibility, admissible three-valued judgment, and optional extension remain separately recoverable. |
| `CC-C32-2` | The signature's EntityOfConcern is the kind, and its content names candidate ValueKind/domain, criterion, applicability, scheme, assumptions, dependencies, formality, and any extent rule. |
| `CC-C32-3` | Candidate mismatch or slice outside applicability yields `not-applicable` and no judgment; only admissible requests return `true`, `false`, or `unknown`. |
| `CC-C32-4` | The directly governed condition named by the criterion decides satisfaction. Evidentiary use alone does not constitute an independently governed condition; an episteme, relation, status, or publication occurrence may be the condition when its direct pattern says so. |
| `CC-C32-5` | Missing support or unavailable dependency for an admissible request yields `unknown`, distinct from known `false`. |
| `CC-C32-6` | No world-side collection-belonging claim, `U.EntitySet`, collection holon, or direct classification occurrence is inferred from judgment or extension. |
| `CC-C32-7` | A separate classification assertion is a C.2.1 episteme and creates neither candidate nor kind. |
| `CC-C32-8` | Subkind checks compare admissible judgments and use C.3.1's criterion-entailment or exhaustive closed-domain branch; samples only support an assertion. |
| `CC-C32-9` | Locality change triggers kind-definition comparison. Only independently identified distinct kinds with an obtaining correspondence use C.3.3; receiving judgments remain fresh. |
| `CC-C32-10` | The kind carries no scope; the slice is an evaluation input and declaration/assertion scopes stay on their epistemes. |
| `CC-C32-11` | Physical, episteme/publication, value, schema, unavailable-support, not-applicable, registration-status, and Work cases respect the same architecture. |
| `CC-C32-12` | Ordinary use stays readable, and declarations or extensions appear only for named receiving uses. |

### C.3.2:14 - Common Anti-Patterns and Remedies

| Anti-pattern | Remedy |
| --- | --- |
| Treating a kind and its `KindSignature` as one object | Identify the kind and declaration episteme separately. |
| Returning `unknown` for a candidate outside ValueKind or applicability | Return `not-applicable` and form no judgment. |
| Returning `false` for missing support | Preserve `unknown`; let the receiving guard decide whether to decline use. |
| Treating any evidence item or record as membership | Ask whether the criterion directly concerns that governed episteme, relation, status, or publication occurrence. If not, keep it only as support. |
| Reusing a world-side belongs-to predicate or minting a relation by notation | Keep the result as a classification judgment unless a direct relation pattern is justified. |
| Treating an extension or braces as ontology | Keep the candidate domain and extension as representations; use C.29 when claim-bearing. |
| Attaching scope or formality to the kind | Keep them on their declaration or assertion epistemes. |
| Editing an extension to hide a subkind counterexample | Repair the relation proposal, declaration alignment, or distinct-kind bridge. |
| Classifying a record as actual Work | Recover an independently grounded `W : U.Work`; keep its record separate. |

### C.3.2:15 - Consequences

**Benefits.** Classification becomes inspectable without ontology growth, evidence-created truth, or coercion among non-applicability, uncertainty, and falsity. Repeated criteria can be reused, and set-consuming uses can receive a bounded representation.

**Costs.** Reliance-bearing uses must pin a declaration and slice, check candidate/slice applicability, preserve `unknown`, and recover any criterion-bearing status or relation under its direct pattern.

**Risks avoided.** Kind/declaration collapse, locality-as-identity, record ontology, not-applicable-as-unknown, false-for-unknown, mathematical-set overread, silent subkind repair, and kind/individual substitution are blocked.

### C.3.2:16 - Rationale

The kind, its declaration, pre-judgment applicability, one admissible candidate judgment, and a representation of current true candidates answer different questions. Their separation prevents evidence, locality, time, scope, and notation from rewriting ontology while still allowing a criterion to concern a directly governed episteme, status, or relation when that is the actual classification condition.

### C.3.2:17 - SoTA-Echoing

Model theory and type systems distinguish intensional declarations, satisfaction judgments, and extensions; measurement and evidence disciplines distinguish the subject feature from its observation or support. C.3.2 combines those separations with FPF's episteme identity, context-slice, representation, and direct-object boundaries.

### C.3.2:18 - Relations

- **Builds on:** `C.3`, `C.3.1`, A.6.0 declaration identity, C.2.1 episteme identity, A.2.6 context slices and claim scope, and direct patterns for candidate identity and features.
- **Coordinates with:** `C.3.3` correspondence between independently identified distinct kinds, `C.3.4` local adaptations, `C.29` mathematical representations, C.2.3 formality, F-G-R evidence and assurance, A.14 collection membership, and `E.24.UK` durable U-kind admission.
- **Does not replace:** the direct subject pattern, evidence-use relation, collection membership, claim-scope governor, guard decision, public-kind admission, or a separately justified durable classification-relation pattern.

### C.3.2:End

