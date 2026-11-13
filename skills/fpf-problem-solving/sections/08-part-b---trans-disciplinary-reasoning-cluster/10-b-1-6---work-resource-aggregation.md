## B.1.6 - Work-Resource Aggregation

> **Type:** B-family aggregation pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Use this when.** Use this pattern when the claim aggregates measured or estimated resource use, such as effort, time, energy, material, information or cost, across identified accounting subjects. These may include dated Work occurrences, A.15.1 temporal or operational Work parts, event-bounded episodes, non-Work carrier phases with an established identity and `PhaseOf` relation, or boundary partitions with the relations needed for their resource account.

**Not this pattern when.** If the question is the Method as a way of doing, use `A.3.1`. If it concerns whether an episteme is a MethodDescription, or the use of its claims about a Method as a way of doing, use `A.3.2`. If it is a work plan, use `A.15.2`. If it is whether Work occurred or which Work temporal part, episode, operational part, retry, resumption, or later occurrence is current, use `A.15.1`. If it is work-entry readiness, full-kit condition, or resource readiness before work entry, use `A.15.5`. If it is bounded aggregation of already recovered temporal relations without resource accounting, use `B.1.4`. If it is a transformation claim, use `A.3.4`. If resource gain leaves whole identity in question, use `B.2`; use `B.2.P` only when emergence-family wording is unresolved.

**What goes wrong if missed.** A convenient resource total is taken from a method description, plan, dashboard or phase label without warranted input values, identified accounting subjects and a combination rule that handles any overlap.

**What this buys.** The practitioner can justify a typed total, vector, interval or bounded estimate from its input values, included subjects, accounting scope, time basis and operative rules, and check whether the same resource contribution has been counted more than once.

### B.1.6:1 - Problem Frame

Practitioners need resource totals across identified Work occurrences and their A.15.1 temporal parts or episodes. A non-Work carrier phase can enter the account when its identity and `PhaseOf` relation are established. The recurring error is to treat a method, method description, plan, phase label, dashboard, or expected efficiency as if it were measured performed Work or as if the label established a Work relation.

Use `B.1.6` for the work-resource aggregation claim. Treat dated work occurrence, Method, MethodDescription, WorkPlan, resource ledger, holon delimitation, transformation, evidence, and whole reidentification as separate claims under their applicable patterns.

### B.1.6:1.0 - Problem

A convenient total becomes an unsupported resource claim when its input values, included subjects, accounting scope, time basis or combination rule are missing. Claims about performed Work also need evidence for those occurrences and their resource use; accounts that depend on holon delimitation, boundary crossing or stock relations need those relations established.

### B.1.6:1.1 - Forces

| Force | Tension |
| --- | --- |
| Measured work vs. planned work | Expected yield, duration, or resource use helps planning, but cannot prove performed-work resource use. |
| Typed resources vs. convenient totals | Energy, mass, time, cost, data volume and attention need compatible accounting bases and any conversion required for the proposed comparison. |
| Boundary accounting vs. local convenience | Resource values need an accounting scope and time basis, together with any holon-delimitation, boundary-crossing or stock relations on which that account depends. |
| Additivity vs. shared contributions | Disjoint resource contributions can be added; repeated inclusion of the same use, stock portion or contribution requires a justified allocation or deduplication rule. |
| Efficiency vs. whole reidentification | Apparent free gain may be measurement, changed accounting basis, substitution, or a new whole; B.1.6 cannot decide that by resource wording alone. |

### B.1.6:2 - Solution — separate measurement from aggregation

Start with the resource question and the values needed to answer it. State the result:

> Under rule `P`, the resource values attributed to the included subjects `S` within accounting boundary `B` and time window `T` yield typed result `R`, with the stated qualifications. The result statement identifies those inputs and grounds.

A sufficient ordinary sentence or table can state this claim. Stop when it answers the receiving resource question with the required basis. If a needed input or relation remains unresolved, keep the dependent result or use unresolved while retaining supported components or a sufficient narrower result.

For each input, retain its subject, resource Characteristic, Scale, applicable Unit, attribution basis and uncertainty relevant to the use. A claimed performed measurement retains its C.16 Work and result; an estimated or derived value retains the source values, model and conditions that warrant it. A ledger row supplies no missing basis merely by displaying the value.

`WorkResourceAggregation@Context` is one possible descriptive outline for the aggregation claim. Use it when that organization helps the receiving use; ordinary prose or another adequate representation can carry the same content. Fields marked `?` are included when the corresponding claim or use needs them; the conditions below govern their required content:

```text
WorkResourceAggregation@Context:
  aggregationConcernRef
  claimScopeRef?: U.ClaimScope
  accountingBoundaryRefs
  timeWindowRefs
  includedSubjectRefs
  aggregatedWorkOccurrenceRefs?
  resourceUseRelationRefs?
  workPartOrOverlapRelationRefs?
  nonWorkCarrierPhaseRelationRefs?
  resourceCharacteristicRefs
  resourceValueBasisRefs
  measurementWorkRefs?
  measurementResultEpistemeRefs?
  aggregationMethodRef?
  aggregationOperationDeclarationRef?
  aggregationPolicyRef
  conversionOrNormalizationRefs?
  aggregationWorkRef?
  aggregationResultRef
  aggregationResultEpistemeRef?
  provenancePathRefs?
  admissibleUse
  stopOrReturnCondition
  nonAdmissibleOverread?
```

`stopOrReturnCondition` states when to stop or return to another pattern. Include `nonAdmissibleOverread?` only when it passes F.19's plausible-reader test. `groundedNonAdmissibleOverread?` is an alias for that same optional value.

Recover the following content for the claims made and the use being proposed:

- a **resource Characteristic** says which quantity or property is accounted for;
- each **resource value** retains its attribution basis: a claimed performed measurement has C.16 measurement Work and a measurement-result episteme; an estimated or derived value keeps its source values, model and conditions. Retain Scale, applicable Unit, time stance, and the calibration and uncertainty basis needed for the use;
- the **aggregation policy** states the inclusion rule and output kind, together with the conversion, normalization, weighting, missing-value, allocation, uncertainty and overlap rules needed to interpret or justify this result. Identify the policy edition when the result or its use depends on that edition;
- when the claim asserts **dated aggregation Work**, or the receiving use needs that occurrence, A.13 identifies its performer and A.15.1 independently admits it as `U.Work`. If assignment-bound attribution is also needed, F.6 checks that relation separately. The Method, inputs through direct relations or A.6.1 bindings, resources and temporal extent retain their grounds;
- the **B.1.6 aggregation result** is the typed total, vector, interval or bounded estimate warranted by the input values, included accounting subjects and operative rules;
- the **result statement** conveys the result, included subjects, rule, boundary, time basis, qualifications and relevant uncertainty. When the receiving claim or use needs a claim-bearing episteme, identify it through C.2.1 by its claim content, EntityOfConcern and effective ReferenceScheme. Keep the resource value, claim content, episteme and expression distinct; and
- keep the **source basis** recoverable: the measurement or estimate sources, operative rules and derivations needed to justify the result. Use A.10 when source-to-use reliance must be replayable, and G.6 when that chain needs a stable address for citation, replay, audit or refresh. Apply G.11 when currentness affects the use.

A ledger or other representation may describe this account. Establish each Work, participation, measurement, part/overlap or result-identity claim on which the proposed use depends under its predicate; an adequate existing representation can then carry the warranted result.

#### B.1.6:2.1 - Subject Pattern Map

| Claim | Subject pattern |
| --- | --- |
| Resource Characteristic, Scale, applicable Unit and value-attribution basis | `C.16` for measurement and derived value attribution; for a claimed measurement Work, A.13 identifies its performer and A.15.1 independently admits the occurrence. Add F.6 when assignment-bound attribution is needed, and A.6.1 for bindings when used. |
| Dated aggregation Work and performer | A.13 identifies the performer, then A.15.1 independently admits the Work. Add F.6 only if the result must also identify the assignment under which the Work was performed. Method enactment and inputs remain separately governed, including A.6.1 bindings when used. |
| Work temporal part, episode, operational part, partition, overlap, retry, resumption, or later occurrence | `A.15.1` and the Work relation pattern; use `B.1.4` only to aggregate already recovered temporal relations |
| Proper temporal restriction of another enduring carrier | that carrier's identity pattern plus `A.14` `PhaseOf`; never a substitute for Work relations |
| Overlap, shared-stock, boundary, and deduplication facts | C.27.TA for interval overlap; the stock, resource-use, boundary, or accounting relation pattern for the other fact |
| Aggregation policy and typed aggregation result | `B.1.6` |
| Measurement-result and aggregation-result epistemes | `C.2.1`; A.15.PROD only when their inception through work matters |
| Source recovery, replayable reliance, provenance or publication | Recover the sources needed for the claim. Use `A.10` for a needed replayable source-to-use reliance account, `G.6` for a needed stable address of that chain, and `E.17` for a publication question. |
| Edition currentness | `G.11` |
| Planned work or resource readiness | `A.15.2` or `A.15.5`, never a measured aggregation result |
| Transformation, whole reidentification, assurance, comparison, or decision | the applicable A.3.4, B.2, B.3, A.19, C.11, or other pattern for that claim |

### B.1.6:3 - Optional `Gamma_work` Notation

`Gamma_work` is optional notation for a recovered `WorkResourceAggregation@Context`.

```text
Gamma_work(workResourceAggregationRecord, resourceBasis, aggregationPolicy)
  -> aggregationResultRef [, aggregationResultEpistemeRef when required by the receiving claim or use]
```

The notation summarizes an aggregation whose required basis has been recovered: resource Characteristics and input-value grounds; included accounting subjects and any Work-part, temporal-overlap, resource-use or stock relations used by the account; a non-Work carrier phase's identity and `PhaseOf` grounds when that phase is included; accounting scope, time basis and operative rules; and the typed result with its qualifications. Any asserted measurement or aggregation Work keeps its independent occurrence grounds. The notation adds none of those facts.

### B.1.6:4 - Ledger Discipline

A ledger can organize the grounds needed to reconstruct the aggregation. Whether using a ledger or another representation, retain for each resource component:

- resource Characteristic, Scale, applicable Unit, polarity when relevant, and accounting boundary;
- the measured or estimated subject, time window, and included Work occurrence, non-Work carrier phase or other admitted accounting subject to which the value applies;
- the attribution basis: C.16 measurement Work and its result episteme for a claimed performed measurement, or the source values, model and conditions for an estimated or derived value, including the calibration and uncertainty basis needed for its use;
- every A.15.1 Work-part relation used by the ledger, every C.27.TA overlap fact used by it, and any current non-Work carrier `PhaseOf`, each independently established by its subject pattern;
- whether component values include the same resource use, stock portion or attributed contribution, and the justified allocation or deduplication rule where they do;
- any conversions, normalizations or imputations used, with the operative methods and rules;
- the operative aggregation rule, its edition when the result or use depends on it, and the aggregation Work occurrence when that dated occurrence is asserted or required;
- the typed aggregation result and its statement, with a separately identified C.2.1 result episteme when the receiving claim or use needs one; and
- sources and derivations needed to justify the result; A.10/G.6 accounts under the conditions in §2; G.11 currentness when it affects use; and the admissible use, stop or reopen condition, with any guard justified by F.19's plausible-reader test.

Keep visible which values are measured, estimated or planned, and which normalization, conversion or allocation has been applied. These descriptions can overlap: an estimated value may result from an indirect measurement. Its basis determines the claim.

A planned value does not become a measurement result or performed-work resource use. A citation to a meter or invoice does not establish the measurement Work; a ledger row does not establish Work parthood or overlap.

Use `PortionOf` only for a resource portion with its A.14 measure and additivity basis. Use `PhaseOf` only for a proper temporal restriction of one unchanged non-Work carrier after its identity rule and interval conditions hold. For Work, use A.15.1 `TemporalPartOf_work`, `EpisodeOf_work`, `OperationalPartOf_work`, or another admitted Work-part relation only between independently admitted Work participants after its predicate passes. Route interval overlap through C.27.TA. Use retry or resumption only through a locally declared species with the needed participant meanings, predicate, identity, cardinality, and applicability; otherwise keep separately identified occurrences. Belonging to a collection, common timestamps, shared identifiers, a phase label, or co-listing in the ledger establishes none of those relations.

### B.1.6:5 - Aggregation Rules

**Typed resource basis.** Aggregate only values whose resource Characteristic, Scale, applicable Unit, subject and accounting boundary are compatible under the operative rule. Joules, hours, kilograms, currency, bytes and attention do not become one scalar by co-location.

**Measurement before aggregation.** Each measured input points to C.16 measurement work and one measurement-result episteme. Raw meter output, indication, resource stock, attributed value, aggregation input, and later efficiency verdict remain distinct.

**Included accounting subjects.** Identify every subject included, including each dated Work occurrence and any non-Work carrier phase. Parent–child, `TemporalPartOf_work`, `EpisodeOf_work`, `OperationalPartOf_work` and other admitted Work-part relations must already obtain between independently admitted Work participants under A.15.1 or their subject patterns. A non-Work phase keeps its carrier's identity and `PhaseOf` grounds. For temporal overlap, recover the participants, temporal reference and interval facts under C.27.TA; establish resource-use or stock overlap under its accounting rule. A Method, plan, epoch or phase label, invoice period or dashboard grouping does not establish these subjects or relations.

**Operative policy.** State inclusion and output kind, and the conversion, normalization, weighting, missing-value, boundary-allocation, uncertainty and overlap/deduplication rules needed to interpret or justify the result. Identify the edition when the result or use depends on it. A policy declaration remains distinct from its application and result.

**Overlap and shared stocks.** Addition is admissible only for disjoint contributions or after a justified policy handles overlap. Determine whether the component values include the same resource use, stock portion or attributed contribution. Apply allocation or deduplication where they do; retain the established disjointness where they do not. Reuse of one person, tool or meter across distinct resource contributions does not by itself duplicate those contributions.

**Aggregation result and any asserted Work.** State the typed total, vector, interval or bounded estimate warranted by the input values, included subjects and rule, with the qualifications needed for its use. An ordinary statement or table can convey that result. When a claim-bearing result episteme is needed, identify it through C.2.1 as in §2, retaining the distinction between resource value, claim content and expression.

When a dated aggregation occurrence is asserted or required, use A.13 to identify the performer and A.15.1 to admit that Work independently. Add F.6 when assignment-bound attribution is needed. The Method, bindings, resources and time retain their separate grounds.

**Uncertainty and provenance.** Propagate measurement, model and conversion uncertainty under the operative rule where it affects the result or use. Keep the necessary sources and derivations recoverable. Use A.10 for needed replayable source-to-use reliance and G.6 for a needed stable address of that chain, preserving any Work, measurement, policy-application and transformation facts the use requires.

**Plan/result separation.** Keep expected use from a method description or WorkPlan as planned and resource readiness under A.15.5. Use A.15.1 and the measurement or aggregation predicates for performed Work and measured results.

**Efficiency and yield.** A ratio or yield claim names its input resource results, output or domain result, attribution bases and applicable comparison rule. Any asserted dated aggregation Work retains its independent grounds. Explain a claimed gain through the measurement, accounting and domain-result grounds on which it depends; use B.2 when whole identity remains the question.

#### B.1.6:5.1 - Aggregation obligations

| Obligation | What must be named |
| --- | --- |
| Resource input | Characteristic, Scale, applicable Unit, subject, time basis, attribution grounds and uncertainty relevant to the use. A claimed performed measurement retains its C.16 Work/result; an estimate or derived value retains its sources, model and conditions. |
| Included subjects | Identified accounting subjects, including each dated Work occurrence; every Work-part, temporal-overlap, resource-use or stock relation used by this aggregation; and the identity and `PhaseOf` grounds for any included non-Work carrier phase. |
| Policy | Inclusion and output kind; every conversion, weighting, missing-value, allocation, uncertainty or overlap rule needed for the result or use; and an edition when either depends on it. |
| Dated aggregation Work, when asserted or required | Performer identified through A.13; dated `U.Work` independently admitted through A.15.1; a separate F.6 check when assignment-bound attribution is needed; separate Method, resources and direct/A.6.1 bindings. |
| Aggregation result | Typed result, included subjects, rule, boundary, time basis and qualifications, conveyed by an adequate statement. When the receiving claim or use needs a result episteme, identify it through C.2.1 as in §2. |
| Source basis and currentness | Recoverable sources and derivations; A.10 when source-to-use reliance must be replayable, G.6 when that chain needs a stable address, and G.11 when currentness affects use. |
| Later use | The receiving claim, action or judgement and any premise, reference, argument or decision-use relation it requires. |

### B.1.6:6 - Archetypal Grounding

**Ordinary operator-time total.** Two existing records, with their value-attribution grounds, attribute one hour each to two admitted Work occurrences by the same operator. Their participant and time facts establish that these are distinct, disjoint resource contributions within the chosen accounting period. Addition yields two operator-hours; an existing table can state that result and its basis. This answer need not assert a separate dated occurrence of aggregation Work. If both entries instead copy the same one-hour contribution, adding them would double-count it: recover the common contribution and count it once, or leave the affected total unresolved until that identity is established.

**Engine test programme.** C.16 measurement Work attributes fuel mass, electrical energy, operator time, and emissions values to subjects under their Scales, models, calibration bases, windows, and uncertainties. Each has its result episteme. Test-run occurrences and obtaining A.15.1 Work-part relations define the included Work set; independently declared C.27.TA overlap facts state shared timing. A test-cell or engine phase enters only through the carrier's identity rule and proper phase relation. Shared warm-up energy is recorded under the temporal and resource-use facts.

Dated aggregation Work applies `ProgrammeResourcePolicy-v3`, which allocates warm-up energy once and propagates input uncertainty. The B.1.6 result is a typed resource vector plus qualifications; a C.2.1 episteme states it. A later emissions verdict remains separate evaluation Work and result.

**Manufacturing cell.** Welding and painting are two dated Work occurrences. Electricity, gas, consumables and labor time are separate resource Characteristics with measurement-result epistemes. Recover what each component includes: the same fan-energy contribution or operator-time contribution must not be counted twice. For a combined cell total, count a shared contribution once; if the question allocates it to individual jobs, apply a justified allocation rule. Distinct, disjoint uses of the same fan or operator remain separately countable. The resource ledger represents those facts. Establish any separately claimed Work-part relation or frame transformation through its pattern.

**Model training.** Epoch labels alone do not establish work parts. Ground the training work and slices, then recover C.16 measurements for compute energy, storage traffic, and operator time. Aggregation work applies an edition-pinned policy to those result epistemes. The training Method, any algorithm text that qualifies as its MethodDescription, and the dated training Work remain distinct; trained-model identity, fairness result, provenance, assurance, and deployment decision stay with their subject patterns.

### B.1.6:6.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Plan becomes evidence of actual use | Expected resource use is presented as evidence of performed resource use. | Keep the plan, any claimed dated Work, the value-attribution basis and the B.1.6 result distinct. |
| Boundary or phase word carries accounting | A port, interface, team, device, epoch or phase label is used as Work parthood, overlap or accounting boundary. | Establish the accounting scope, time basis and operative rule, together with any delimitation, Work relation, carrier identity/PhaseOf, crossing or stock relation on which the account depends. |
| Untyped total hides conversion | Hours, energy, material, money, and data are added as one number. | Keep resource vectors typed until a conversion relation or model is declared admissible under the applicable measurement or mathematical-lens pattern. |
| A resource contribution is double-counted | The same resource use, stock portion or attributed contribution is counted more than once. | Establish the repeated contribution and apply a justified allocation or deduplication rule, or restrict the result to the supported account. |
| Efficiency becomes proof of a new whole | Reduced resource use is treated as proof of a new whole. | Use measurement and evidence-use patterns for the gain; use `B.2` when whole identity remains the question and `B.2.P` for unresolved emergence-family wording. |

### B.1.6:7 - Conformance Checklist

| ID | Requirement |
| --- | --- |
| CC-B1.6-1 | Every resource component names its Characteristic, Scale, applicable Unit, subject, time stance and attribution basis, with uncertainty relevant to use. A claimed performed measurement retains its C.16 Work and result; an estimated or derived value retains its sources, model and conditions. |
| CC-B1.6-2 | Included accounting subjects and each relation used by the aggregation are independently grounded. Every included Work occurrence and used A.15.1 Work-part relation has its basis; temporal overlap follows C.27.TA, resource-use or stock overlap follows its rule, and an included non-Work phase satisfies its carrier's identity and PhaseOf conditions. |
| CC-B1.6-3 | The operative policy names inclusion and output kind, every additional rule needed to interpret or justify the result, and an edition when the result or use depends on it. |
| CC-B1.6-4 | For dated aggregation Work, A.13 identifies the performer and A.15.1 independently admits the occurrence. F.6 is present only when the result must also identify the assignment under which that Work was performed. The Method, direct/A.6.1 bindings, resources, and temporal extent remain separate. |
| CC-B1.6-5 | The typed aggregation result and its statement are recoverable. When a claim-bearing result episteme is needed, its claim content, EntityOfConcern and effective ReferenceScheme are identified through C.2.1. The resource value, claim content, episteme and expression remain distinct. |
| CC-B1.6-6 | Sources and derivations needed for the result are recoverable. Any required A.10/G.6 provenance account or G.11 currentness result remains separate from the measurement and aggregation results. |
| CC-B1.6-7 | Planned values and A.15.5 resource readiness are not presented as measured performed-work aggregation. |
| CC-B1.6-9 | Any yield, efficiency, comparison, assurance, transformation, whole-reidentification or decision claim names its applicable subject pattern. |

### B.1.6:8 - Common Anti-Patterns and How to Avoid Them

| Overread | Repair |
| --- | --- |
| A method or algorithm is treated as the work-resource roll-up. | Recover the resource claim and its grounds through `B.1.6`. Use `A.3.1` for a separate Method question, or `A.3.2` for a MethodDescription membership or description-use question. |
| A work plan is treated as measured work. | Use `A.15.2` for the plan and `A.15.1` for performed work evidence. |
| A phase label or timeline is treated as a resource ledger or as proof of a Work relation. | Recover the subject first: A.15.1 for Work temporal parts or occurrences, the carrier's identity pattern plus A.14 for proper non-Work `PhaseOf`, and B.1.4 only for bounded aggregation of already recovered temporal relations. Add B.1.6 only when typed resource values are being aggregated. |
| A resource gain is treated as emergence. | Use measurement and evidence-use patterns first; use `B.2` when whole identity remains the question; use `B.2.P` for unresolved emergence-family wording. |
| A ledger, dashboard or report total is relied on without the grounds its use requires. | Recover the existing result statement, input records, included subjects and relations, operative rule and qualifications. Preserve an adequate account; obtain only missing grounds under §§4–5. An asserted dated aggregation Work or a needed replayable provenance account retains its requirements. |

### B.1.6:9 - Consequences

This pattern grounds typed resource aggregation in attributed input values, identified accounting subjects, operative rules and the conditions of the receiving use. Measurement, performed Work, aggregation policy/application, result episteme, subject relations and provenance retain their separate grounds whenever claimed or needed.

The cost is establishing the accounting basis. A comparison can then use totals whose value-attribution bases, boundaries and aggregation rules are compatible, within the limits of their evidence.

### B.1.6:9.1 - Rationale

`B.1.6` exists because a convenient total can hide different subjects, repeated contributions or incompatible value bases. A warranted result requires the input-value grounds, included subjects and relations, accounting scope, time basis and combination rule needed for that claim. Policy editions, dated aggregation Work and provenance accounts are added when the claim or receiving use depends on them. An adequate ledger or other expression can state this account.

`Gamma_work` denotes the aggregation described by that account. A MethodDescription or WorkPlan can state expected yield or resource use; a claim about actual use needs evidence for the included subjects and their attributed resource contributions. Any claimed performed Work retains its independent occurrence grounds.

### B.1.6:9.2 - SoTA-Echoing

The following contributions are adapted from the cited editions for work-resource aggregation.

| Source | Contribution to the method | Use boundary |
| --- | --- | --- |
| [ISO 14040:2006 with Amendment 1:2020](https://www.iso.org/standard/37456.html) and [ISO 14044:2006 with Amendments 1:2017 and 2:2020](https://www.iso.org/standard/38498.html) | Adapt goal/scope, system-boundary, inventory, allocation, reporting and intended-use discipline. Recover the boundary, included subjects, output kind, intended use and any allocation or overlap rules required by the account before relying on the total. | An LCA boundary or reported total does not establish FPF Work parthood, measurement, aggregation Work, result identity or admissibility for every later use. |
| [GHG Protocol, *Product Life Cycle Accounting and Reporting Standard* (2011)](https://ghgprotocol.org/product-standard) | Adapt process subdivision or system expansion before allocation, physical or other justified allocation, and double-count control for shared processes and stocks. Recover which resource contributions overlap and apply justified allocation or deduplication where needed. | A common meter or convenient allocation key does not establish disjointness, Work structure or a universal resource share. |
| [JCGM GUM-6:2020, *Developing and using measurement models*](https://doi.org/10.59161/JCGMGUM-6-2020) | Adapt input-quantity, model-adequacy, covariance, and uncertainty-propagation discipline. Retain input uncertainties, correlations and conversions, the propagation method, and qualified output uncertainty separately from provenance. | Source references and point totals do not propagate uncertainty; aggregation does not make incompatible models or quantities commensurable. |
| [ISO 80000-1:2022, *Quantities and units — Part 1: General*](https://www.iso.org/standard/76921.html) | Adapt the distinctions among quantity kind, unit, quantity value, and dimension, and the use of coherent units, for typed inputs and outputs. Keep resource quantities distinct unless a conversion or normalization and output kind are justified. | A shared numeral, unit label, normalized score, or vector position does not justify cross-kind addition, scalarization, efficiency, or comparability. |

### B.1.6:10 - Relations

- For claims about dated measurement or aggregation Work, A.13 identifies performers and A.15.1 independently admits the occurrences. F.6 applies when assignment-bound attribution is needed; A.6.1 governs declarations and bindings when used. C.2.1 governs the measurement-result and aggregation-result epistemes.
- Coordinates with `A.3.1`, `A.3.2`, and `A.15.2` for method, method description, and work plan.
- Coordinates with `A.15.5` for work-entry readiness, full-kit condition, and resource readiness before work entry; B.1.6 may cite those refs but does not decide readiness.
- Coordinates with `A.15.1` for Work temporal parts, episodes, operational parts, overlaps, retries, resumptions, and later occurrences; with `B.1.4` only for bounded aggregation of already recovered temporal relations; and with `C.27` for temporal-claim adequacy.
- Coordinates with `A.1`, `B.1`, `A.14`, and `C.13` for holon delimitation, part-whole, proper temporal restriction and `PhaseOf` for a non-Work carrier, and constructive grounding.
- Coordinates with `A.3.4` for transformation. Use `B.2` for a remaining whole-identity question and `B.2.P` for unresolved emergence-family wording; the relevant B.2-family pattern defines or constrains the recovered claim.
- Coordinates with `C.16` for resource Characteristics and measurement results; `A.10` and `G.6` for provenance; `G.11` for currentness; `C.29` for representation or mathematical-lens claims; A.15.1 for Work relations; A.14 and B.1.4 for non-Work part or phase relations and their bounded aggregation; E.17 for publication; and the applicable comparison, assurance, transformation, reidentification, or decision pattern when those uses are current.

### B.1.6:End
