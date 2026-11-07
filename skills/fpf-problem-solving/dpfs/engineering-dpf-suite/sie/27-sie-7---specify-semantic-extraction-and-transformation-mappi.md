## SIE.7 - Specify Semantic Extraction and Transformation Mappings

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** an `ExecutableSemanticMappingSpecification@Use` that states source and target schemes, accepted correspondence premises and any relied-on identity or claim-composition premises, extraction and transformation rules, selection and cardinality, units and codes, conditions, defaults, errors, information loss, trace, examples, and tests.

### SIE.7:1 - Problem Frame

**Use this when** accepted semantic correspondences must become repeatable extraction or transformation behavior, or existing code contains joins, conversions, defaults, and exclusions that cannot be traced to their semantic premises. The recognizable failure is a pipeline that runs successfully while changing meanings, merging unresolved identities, dropping conflicts, or inventing values through defaults.

The primary EntityOfConcern is one executable semantic rule set for a named use, independent of the physical pipeline that may enact it. The first move is to bind each output claim to accepted input senses and relation, identity, or composition results. The first result is a mapping specification precise enough to implement and test without reopening its semantic choices in code.

The payoff is a clean handoff to Data Engineering or another implementer and a traceable object for validation. Do not use SIE.7 to choose virtual versus materialized realization, build or operate the pipeline, or authorize access. A correspondence set is an input, not executable behavior; a running transform is evidence, not the specification itself.

### SIE.7:2 - Problem

Mapping logic is often dispersed across SQL, ETL configuration, model transformations, lookup tables, API adapters, and undocumented operator knowledge. The same “mapping” word then refers to a semantic relation, an extraction query, a unit conversion, a data movement, and the Work that ran it.

When these objects collapse, semantic review happens after implementation and cannot identify what was intended. Defaults conceal missing inputs, many-to-one mappings drop distinctions, identifiers are normalized without issuer context, and error rows vanish. A code diff reveals mechanics but not the receiving-use claim it is allowed to produce.

### SIE.7:3 - Forces

| Force | Tension |
| --- | --- |
| Executability | Rules must be precise enough to run, while binding them to one technology can hide their semantic intent. |
| Completeness | Every output branch needs behavior, while invented defaults make an incomplete rule appear total. |
| Performance | Efficient joins and precomputation matter, while optimization must preserve semantic premises and trace. |
| Cardinality | Source and target structures differ, while one-to-many and many-to-one choices can create loss or duplication. |
| Error handling | Operational systems prefer a value or null, while semantic failure needs distinct unresolved, incompatible, stale, and source-error branches. |
| Change | Stable rule identifiers aid maintenance, while source editions and accepted correspondences can invalidate a rule. |

### SIE.7:4 - Solution

Specify semantic mapping rules separately from their implementation. Bind every rule to a receiving-use contract, exact source and target schemes, accepted correspondence premises, and any identity or claim-composition premise on which that rule depends. Make selection, cardinality, conversions, defaults, errors, loss, trace, and tests explicit. Require implementations to preserve these behaviors or return a named discrepancy.

#### SIE.7:4.1 - Pattern-Use Unfolding

1. **Name the output claim and receiver.** State the target field or proposition, its meaning, grain, interval/effectivity, and the action it supports.
2. **Bind source and target schemes.** Reference exact `SIE.2` source rows and target interface/model definitions, editions, profiles, units, codes, identifiers, and access assumptions.
3. **Bind semantic premises.** Reference accepted `SIE.4` correspondence rows and every load-bearing `SIE.5` identity disposition. Reference a `SIE.6` composition or conflict result when the rule depends on that result. Stop on an unresolved required premise; do not require identity or claim-composition work that cannot change the rule.
4. **Specify selection and extraction.** State source records, predicates, joins, windows, configuration/effectivity filters, ordering, and behavior for missing or duplicate inputs.
5. **Specify transformation.** State direction, construction, decomposition, aggregation, unit/code conversion, normalization, derivation, and required external lookup. Name the authority for any conversion or code table.
6. **Specify cardinality and identity preservation.** State one-to-one, one-to-many, many-to-one, or conditional behavior; keep source identifiers and disposition references when rows combine or split.
7. **Specify defaults and errors.** Distinguish absent, unknown, not applicable, inaccessible, stale, incompatible, unresolved, source failure, and actual zero or empty value. Permit a default only when the contract and semantic warrant state its meaning and loss.
8. **State information loss and forbidden reuse.** Name omitted distinctions, coarsening, precision, interval, provenance, or conflict and the use for which the loss is accepted.
9. **Provide trace and examples.** Give stable rule identifiers, input-to-output trace positions, positive examples, boundary and counterexamples, and expected negative branches.
10. **Define implementation conformance and reopen.** State observable behavior an implementation must match and source, premise, contract, or target changes that invalidate the rule.

#### SIE.7:4.2 - Record the Result

| Mapping position | Required content |
| --- | --- |
| rule and use | stable rule identifier, receiver, output claim, grain, interval/effectivity |
| schemes | source/target assets, models/schemas, editions/profiles, fields/types/relations, units/codes |
| semantic inputs | accepted correspondence rows and any relied-on identity dispositions or composition/conflict results, with their conditions |
| extraction | selection, joins, filters, windows, effectivity, duplicates, missing-input behavior |
| transformation | direction, construction/decomposition/aggregation, conversions, lookups, derivation |
| cardinality and identifiers | source-target multiplicity, split/merge behavior, source-ID and premise preservation |
| defaults and errors | distinguished states, permitted default and meaning, failure branches, quarantine or stop |
| loss and trace | accepted/forbidden loss, provenance, rule and premise references, input-output trace |
| examples and conformance | positive, boundary, negative/unlike examples, expected outputs, implementation predicate, reopen |

#### SIE.7:4.3 - What Changes in Practice

Semantic rules and their premises become independently reviewable. Data Engineering can optimize or replace an implementation while preserving the mapping behavior, and a failed output can be traced to a source premise, rule, implementation discrepancy, or receiving-use change.

### SIE.7:5 - Archetypal Grounding - AP242/QIF Mapping Rules

The AP242/QIF package needs a row set for the configuration-bound inspection query. Its specification includes these constructed rules:

| Rule | Semantic and executable behavior |
| --- | --- |
| `MAP-SIE-APQ-01` | Select the released AP242 product-definition revision/configuration supplied by Systems Engineering and filter features by effectivity `E`. Do not select “latest” as a substitute. |
| `MAP-SIE-APQ-02` | For each accepted `SIE.4` plan-characteristic-concerns-feature row, join exact source identifiers only under the referenced `SIE.5` feature disposition. Preserve AP242 and QIF IDs and issuers. |
| `MAP-SIE-APQ-03` | Compose AP242 definition/effectivity and QIF plan/result claims through the referenced `SIE.6` result. Emit compatible qualified claims, explicit contradiction, non-comparability, or unresolved branches; never overwrite. |
| `MAP-SIE-APQ-04` | Convert units only through the contract-approved code/unit table and retain original value, unit, conversion rule, precision, and loss. An unknown unit stops that result row. |
| `MAP-SIE-APQ-05` | Return unmatched AP242 feature, unmatched QIF characteristic, stale result, missing provenance, and source-error states distinctly. No state defaults to an accepted match. |

Positive examples cover one known configuration/feature/characteristic/result chain. Boundary cases cover one-to-many characteristics and repeated results. Negative cases cover an obsolete revision, incompatible feature, unresolved identity, unknown unit, contradictory result status, and absent QIF plan. A SQL view, R2RML mapping, QVT transformation, or application code may implement the rules; none changes the specification without reopening the affected rule.

### SIE.7:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | Mapping code silently decides source priority, identity, or authoritative value. | Require references to accepted premises and the direct authority for conversions or defaults. |
| Architecture | A tool's expressiveness defines the semantic rule. | State implementation-independent behavior and return an implementation gap when the tool cannot preserve it. |
| Ontology/Epistemology | Correspondence truth, transformation rule, performed transformation, and output claim collapse. | Keep the rule and its evidence separate from execution occurrences and resulting claims. |
| Pragmatics | The specification reproduces every implementation detail. | Include only behavior needed to preserve semantics, errors, trace, and conformance. |
| Didactics | Examples are copied as the complete rule. | State the general condition and use examples as tests, including counterexamples. |

### SIE.7:7 - Conformance Checklist

- [ ] Every rule names a receiving output claim and use.
- [ ] Source and target schemes, editions/profiles, meanings, units, codes, and identifiers are exact.
- [ ] Accepted correspondence premises and any relied-on identity or composition premises are referenced rather than re-decided in code.
- [ ] Selection, joins, filters, windows, effectivity, duplicates, and missing inputs are explicit.
- [ ] Transformations, conversions, external lookups, and their authority are explicit.
- [ ] Cardinality, split/merge behavior, and source-identifier preservation are specified.
- [ ] Absent, unknown, not applicable, inaccessible, stale, incompatible, unresolved, source failure, zero, and empty values remain distinguishable where relevant.
- [ ] Defaults have a semantic warrant, accepted loss, and test.
- [ ] Information loss, forbidden reuse, provenance, and input-output trace are inspectable.
- [ ] Positive, boundary, negative, and unlike cases define observable implementation conformance.
- [ ] The specification claims no running pipeline, service level, or receiving-use validation.

### SIE.7:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| SQL execution treated as semantic justification | Recover the semantic rule, premises, loss, errors, and tests; check the SQL implementation against them. |
| Crosswalk equals transformation | Add selection, direction, cardinality, conversions, defaults, errors, trace, and examples. |
| Null for every failure | Define distinct semantic and operational states and their receiver behavior. |
| Latest record wins | Use the direct configuration/effectivity or justified interval rule. |
| Normalize identifiers | Preserve scheme and issuer and reference the identity disposition. |
| Hidden unit conversion | Record source/target units, authority, precision, loss, and counterexample tests. |

### SIE.7:9 - Consequences

Implementers receive a bounded contract that can survive technology change, and reviewers can distinguish a semantic defect from an implementation defect. Negative branches and accepted loss become testable, and optimization can proceed under a preservation predicate.

The cost is explicit rule and example work before or alongside coding. Some tools cannot represent the required branches or trace and must be wrapped, changed, or rejected for this use.

### SIE.7:10 - Rationale

A semantic correspondence states a relation; an executable mapping states how source occurrences produce target claims under conditions. Making that extra structure explicit prevents implementation convenience from becoming a semantic decision and lets Data Engineering own execution without inheriting unstated SIE authority.

### SIE.7:11 - SoTA-Echoing

The best-known line combines declarative mapping languages, model transformation, traceability, and representation-preservation checks. The serious default is code-first ETL that leaves semantic premises and loss implicit. SIE.7 makes the receiving-use mapping contract independently recoverable, including its negative states. Code and its documentation can carry that contract when the semantic requirements and their grounds remain distinguishable from the implementation being tested.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| Current FPF `A.6.3.RT` | adopt | Governs preservation through representation transition; it does not specify this domain mapping. |
| [R2RML](https://www.w3.org/TR/r2rml/) | adapt | Demonstrates declarative relational-to-RDF mapping structures; RDF and relational sources are optional technology families. |
| [OMG QVT 1.3](https://www.omg.org/spec/QVT/) | adapt | Contributes model-query/view/transformation and trace forms; MOF/QVT is not mandatory. |
| [PROV-O](https://www.w3.org/TR/prov-o/) | adapt | Supports derivation and activity/agent/entity trace; provenance does not prove semantic preservation. |
| code-first ETL with implicit semantic premises | reject as sufficient | Execution must be checked against an independently recoverable rule, loss, and branch contract. |

Reopen when an input or target scheme changes, a correspondence/identity/composition premise changes, a counterexample defeats the rule, the receiver changes accepted loss, or implementations cannot satisfy the preservation predicate.

### SIE.7:12 - Relations

- `SIE.1` supplies the output claims, accepted loss, service conditions, tests, and stop.
- `SIE.2` supplies exact source and target semantics, editions, identifiers, units/codes, provenance, and gaps.
- `SIE.4` supplies accepted correspondence premises; `SIE.5` and `SIE.6` supply identity and composition results when a rule relies on them.
- `SIE.8` consumes rule behavior and implementation conditions to compare realization alternatives.
- `SIE.9` exposes the rule outputs and error branches to the receiver.
- `SIE.10` tests both specification semantics and implementation conformance. Data Engineering owns pipeline construction, operation, observability, reliability, and recovery.

### SIE.7:End
