## B.1.6 - Work-Resource Aggregation

> **Type:** B-family aggregation pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Use this when.** Use this pattern when the current claim aggregates resources, effort, time, energy, material, information, cost, or another measured resource over exact dated Work occurrences, A.15.1 temporal or operational Work parts, event-bounded episodes, non-Work carrier phases with an established identity and `PhaseOf` relation, boundary partitions, or comparable work-resource ledgers.

**Not this pattern when.** If the current question is the method as a way of doing, use `A.3.1`. If it is a method description, SOP, algorithm text, simulator configuration, or formal expression, use `A.3.2`. If it is a work plan, use `A.15.2`. If it is whether Work occurred or which Work temporal part, episode, operational part, retry, resumption, or later occurrence is current, use `A.15.1`. If it is work-entry readiness, full-kit condition, or resource readiness before work entry, use `A.15.5`. If it is bounded aggregation of already recovered temporal relations without resource accounting, use `B.1.4`. If it is a transformation claim, use `A.3.4`. If apparent resource gain changes whole identity, use `B.2.P` before any B.2-family pattern.

**What goes wrong if missed.** Resource, effort, time, energy, or cost totals are read from methods, plans, dashboards, or phase labels without a dated work occurrence, resource ledger, and overlap policy.

**What this buys.** A replayable chain that keeps the resource Characteristic, measurement work/result episteme, aggregation work/result, exact policy, work parthood/overlap, and provenance separately recoverable while preventing double counting.

### B.1.6:1 - Problem Frame

Practitioners need to roll up work-resource claims across runs, exact A.15.1 Work temporal parts or episodes, teams, devices, stations, model-training epochs, non-Work carrier phases with an established identity and `PhaseOf` relation, or evidence-production occurrences. The recurring error is to treat a method, method description, plan, phase label, dashboard, or expected efficiency as if it were measured performed Work or as if the label established a Work relation.

Use `B.1.6` for the work-resource aggregation claim. Treat dated work occurrence, Method, MethodDescription, WorkPlan, resource ledger, holon delimitation, transformation, evidence, and whole reidentification as separate claims under their applicable patterns.

### B.1.6:1.0 - Problem

Work-resource totals are often borrowed from plans, method descriptions, dashboards, or phase labels even when no performed-work evidence, resource-accounting basis, holon delimitation, time window, and overlap policy have been recovered. The failure is to treat a convenient total as a work-resource aggregation claim before the dated work occurrences and resource ledger are explicit.

### B.1.6:1.1 - Forces

| Force | Tension |
| --- | --- |
| Measured work vs. planned work | Expected yield, duration, or resource use helps planning, but cannot prove performed-work resource use. |
| Typed resources vs. convenient totals | Energy, mass, time, cost, data volume, and attention can be compared only after their resource-accounting basis and conversion relation are declared. |
| Boundary accounting vs. local convenience | Resource values are useful only when the holon delimitation, boundary-crossing relation, stock relation, and time window are named. |
| Additivity vs. shared stocks | Disjoint partitions can be added; shared meters, tools, people, inventories, data, or ports need overlap and deduplication policy. |
| Efficiency vs. whole reidentification | Apparent free gain may be measurement, changed accounting basis, substitution, or a new whole; B.1.6 cannot decide that by resource wording alone. |

### B.1.6:2 - Solution — separate measurement from aggregation

Start with one direct sentence:

> Dated aggregation work `W_agg` applied policy `P` to the exact C.16 resource-result epistemes for work set `W_set`, under declared work-part/overlap relations and accounting boundary `B`, and obtained aggregation result `R_agg`; C.2.1 episteme `E_agg` states that result and A.10/G.6 record its provenance.

If any referenced resource value lacks its resource Characteristic, measurement work, result episteme, Scale/Unit, uncertainty when current, or provenance, it is not repaired by adding a ledger row.

`WorkResourceAggregation@Context` is a descriptive account for one aggregation claim:

```text
WorkResourceAggregation@Context:
  aggregationConcernRef
  claimScopeRef?: U.ClaimScope
  accountingBoundaryRefs
  timeWindowRefs
  aggregatedWorkOccurrenceRefs
  resourceUseRelationRefs
  workPartOrOverlapRelationRefs
  nonWorkCarrierPhaseRelationRefs?
  resourceCharacteristicRefs
  measurementWorkRefs
  measurementResultEpistemeRefs
  aggregationMethodRef
  aggregationOperationDeclarationRef?
  aggregationPolicyRef
  conversionOrNormalizationRefs?
  aggregationWorkRef
  aggregationResultRef
  aggregationResultEpistemeRef
  provenancePathRefs
  admissibleUse
  stopOrReturnCondition
  groundedNonAdmissibleOverread?
```

Recover each of these objects and claims independently:

- a **resource Characteristic** says which quantity or property is accounted for;
- **measurement work** and a **C.16 measurement-result episteme** supply each attributed resource value, Scale, Unit, uncertainty, model, calibration, and time stance;
- the **aggregation policy** declares inclusion, conversion, weighting, missing-value, partition, overlap, and deduplication rules;
- **aggregation work** has its actual performer identified through A.13 and is independently admitted as dated `U.Work` through A.15.1; if the aggregation account must also identify the assignment under which the Work was performed, F.6 checks that relation separately; Method, actual inputs through direct relations or A.6.1 bindings, resources, and temporal extent remain separate;
- the **B.1.6 aggregation result** is the typed total, vector, interval, or bounded estimate obtained under that policy and work set;
- a distinct **C.2.1 aggregation-result episteme** states the result, work set, policy, boundary, time window, qualifications, and uncertainty; and
- **A.10/G.6 provenance** makes the measurement sources, transformations, aggregation work, and result episteme replayable.

A ledger, dashboard, policy, profile, clause, citation, or graph edge may represent or cite this chain. None establishes work occurrence, actual participation, measurement, aggregation, or result identity by presence.

#### B.1.6:2.1 - Subject Pattern Map

| Current claim | Subject pattern |
| --- | --- |
| Resource Characteristic, Scale, Unit, measurement model/calibration, measurement work and result | `C.16` for measurement; A.13 for each actual performer; A.15.1 for independent Work admission; F.6 when the result must also identify the assignment under which the Work was performed; and A.6.1 for actual bindings |
| Dated aggregation Work and actual performer | A.13 identifies the actual performer, then A.15.1 independently admits the Work. Add F.6 only if the result must also identify the assignment under which the Work was performed. Method enactment and actual inputs remain separately governed, including A.6.1 bindings when used. |
| Work temporal part, episode, operational part, partition, overlap, retry, resumption, or later occurrence | `A.15.1` and the exact Work relation pattern; use `B.1.4` only to aggregate already recovered temporal relations |
| Proper temporal restriction of another enduring carrier | that carrier's direct identity pattern plus `A.14` `PhaseOf`; never a substitute for Work relations |
| Overlap, shared-stock, boundary, and deduplication facts | C.27.TA for interval overlap; the exact stock, resource-use, boundary, or accounting relation pattern for the other fact |
| Aggregation policy and typed aggregation result | `B.1.6` |
| Measurement-result and aggregation-result epistemes | `C.2.1`; A.15.PROD only when their inception through work matters |
| Source recovery and provenance | `A.10` and `G.6`; `E.17` for publication |
| Edition currentness | `G.11` |
| Planned work or resource readiness | `A.15.2` or `A.15.5`, never a measured aggregation result |
| Transformation, whole reidentification, assurance, comparison, or decision | the applicable A.3.4, B.2, B.3, A.19, C.11, or other pattern for that exact claim |

### B.1.6:3 - Optional `Gamma_work` Notation

`Gamma_work` is optional notation for a recovered `WorkResourceAggregation@Context`.

```text
Gamma_work(workResourceAggregationRecord, resourceBasis, aggregationPolicy)
  -> aggregationResultRef, aggregationResultEpistemeRef
```

Use the notation only after naming the resource Characteristics, C.16 measurement Work and results, dated Work set and relevant A.15.1 Work-part relations, any C.27.TA overlap fact, any current non-Work carrier identity and `PhaseOf` relation, accounting boundary and time window, aggregation policy, and dated aggregation Work. The notation then summarizes that recovered aggregation record; each object, relation, method, Work, and emergence claim remains under its direct pattern.

### B.1.6:4 - Ledger Discipline

The ledger is a replay surface, not the source of the aggregation claim. For every resource component it records:

- resource Characteristic, Scale, Unit, polarity when relevant, and accounting boundary;
- exact measured or estimated subject, time window, and work occurrence to which the value applies;
- C.16 measurement work and measurement-result episteme, including model, calibration, uncertainty, and provenance refs when current;
- every A.15.1 Work-part relation used by the ledger, every C.27.TA overlap fact used by it, and any separately current non-Work carrier `PhaseOf`, each independently established by its subject pattern;
- shared resource, meter, person, tool, stock, data, port, or time-window overlap and the exact deduplication rule;
- conversions, normalizations, imputations, and their declared method/policy refs;
- the aggregation policy edition and actual aggregation work occurrence;
- aggregation result and distinct C.2.1 result episteme; and
- A.10/G.6 source and provenance refs, G.11 currentness when current, admissible use, stop or reopen condition, and one grounded source-use guard only when an actual source or ledger feature makes that error live.

Measured, estimated, normalized, converted, allocated, and planned values remain visibly different. A planned value does not become a measurement result or performed-work resource use. A citation to a meter or invoice does not establish the measurement work; a ledger row does not establish work parthood or overlap.

Use `PortionOf` only for a resource portion with its A.14 measure and additivity basis. Use `PhaseOf` only for a proper temporal restriction of one unchanged non-Work carrier after its direct identity rule and interval conditions hold. For Work, use A.15.1 `TemporalPartOf_work`, `EpisodeOf_work`, `OperationalPartOf_work`, or another admitted Work-part relation only between independently admitted Work participants after its predicate passes. Route interval overlap through C.27.TA. Use retry or resumption only through a locally declared species with the needed participant meanings, predicate, identity, cardinality, and applicability; otherwise keep separately identified occurrences. Belonging to a collection, common timestamps, shared identifiers, a phase label, or co-listing in the ledger establishes none of those relations.

### B.1.6:5 - Aggregation Rules

**Typed resource basis.** Aggregate only values whose resource Characteristic, Scale, Unit, subject, and accounting boundary are compatible under the declared policy. Joules, hours, kilograms, currency, bytes, and attention do not become one scalar by co-location.

**Measurement before aggregation.** Each measured input points to exact C.16 measurement work and one measurement-result episteme. Raw meter output, indication, resource stock, attributed value, aggregation input, and later efficiency verdict remain distinct.

**Exact Work set.** Name every dated Work occurrence included. Parent–child, `TemporalPartOf_work`, `EpisodeOf_work`, `OperationalPartOf_work`, and other admitted Work-part relations must already obtain between exact Work participants under A.15.1 or their direct subject patterns. Any overlap fact comes through its exact C.27.TA temporal declaration. A Method, plan, epoch or phase label, invoice period, or dashboard grouping does not establish the Work set.

**Exact policy.** The aggregation policy states inclusion/exclusion, conversion, normalization, weighting, missing-value treatment, boundary allocation, uncertainty treatment, overlap/deduplication, and output kind. A policy declaration is not aggregation work or a result.

**Overlap and shared stocks.** Addition is admissible only for disjoint partitions or after an exact policy handles overlap. Shared people, tools, meters, inventories, datasets, ports, and time windows require the direct shared-use/overlap fact and a justified allocation or deduplication rule.

**Aggregation work and result.** Use A.13 to identify the actual performer and A.15.1 to admit the dated aggregation Work independently. If the aggregation account must also identify the assignment under which the Work was performed, check that relation separately through F.6. Keep the Method, actual bindings, resources, and time separate. State the B.1.6 result as a typed total, vector, interval, or bounded estimate under the named policy and Work set; then state it in a distinct C.2.1 episteme.

**Uncertainty and provenance.** Propagate measurement and model or conversion uncertainty through the exact aggregation policy. Use A.10/G.6 paths to record the established Work, measurements, policy application, transformations, result, and sources.

**Plan/result separation.** Keep expected use from a method description or WorkPlan as planned and resource readiness under A.15.5. Use A.15.1 and the measurement or aggregation predicates for performed Work and measured results.

**Efficiency and yield.** A ratio or yield claim names its input resource results, exact output/domain result, measurement bases, aggregation work, and comparison policy. It does not use a generic output-result relation. Apparent free gain remains a measurement, accounting-boundary, substitution, or whole-reidentification question until its subject pattern is recovered.

#### B.1.6:5.1 - Compact Obligation Rows

| Obligation | What must be named |
| --- | --- |
| Resource input | Resource Characteristic, Scale/Unit, subject, C.16 measurement work/result episteme, uncertainty, time, and provenance |
| Work set | Dated Work occurrences, every A.15.1 Work-part relation used by this aggregation, and every C.27.TA overlap fact it uses; any non-Work carrier phase keeps its own identity rule and `PhaseOf` relation |
| Policy | Edition, inclusion, conversions, weights, missing values, boundary allocation, uncertainty, overlap/deduplication, and output kind |
| Aggregation execution | Actual performer identified through A.13; dated `U.Work` independently admitted through A.15.1; a separate F.6 check when the result must also identify the assignment under which the Work was performed; separate Method, resources, and actual direct/A.6.1 bindings |
| Aggregation result | Typed result, work set, policy, boundary, window, qualifications, and distinct C.2.1 episteme |
| Provenance/currentness | A.10/G.6 paths and G.11 result when currentness affects use |
| Later use | Exact receiving work and direct premise/reference/argument/decision-use relation |

### B.1.6:6 - Archetypal Grounding

**Engine test programme.** C.16 measurement Work attributes fuel mass, electrical energy, operator time, and emissions values to exact subjects under their Scales, models, calibration bases, windows, and uncertainties. Each has its own result episteme. Exact test-run occurrences and obtaining A.15.1 Work-part relations define the included Work set; independently declared C.27.TA overlap facts state shared timing. A test-cell or engine phase enters only through the carrier's identity rule and proper phase relation. Shared warm-up energy is recorded under the exact temporal and resource-use facts. Dated aggregation Work applies `ProgrammeResourcePolicy-v3`, which allocates warm-up energy once and propagates input uncertainty. The B.1.6 result is a typed resource vector plus qualifications; a C.2.1 episteme states it. A later emissions verdict remains separate evaluation Work and result.

**Manufacturing cell.** Welding and painting are two dated Work occurrences. Electricity, gas, consumables, and labor time are separate resource Characteristics with measurement-result epistemes. A shared extraction fan and overlapping operator time require direct shared-use facts and an allocation policy. The resource ledger represents the established facts; recover Work, parts, overlap, measurements, aggregation, and any frame transformation through their direct patterns.

**Model training.** Epoch labels alone do not establish work parts. Ground the training work and exact slices, then recover C.16 measurements for compute energy, storage traffic, and operator time. Aggregation work applies an edition-pinned policy to those result epistemes. The algorithm remains a method description; trained-model identity, fairness result, provenance, assurance, and deployment decision stay with their subject patterns.

### B.1.6:6.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Plan becomes measurement or aggregation | Expected resource use is presented as performed work or an obtained total. | Keep the plan, dated work, C.16 measurement result, aggregation work, and B.1.6 result distinct. |
| Boundary or phase word carries accounting | A port, interface, team, device, epoch, or phase label is used as Work parthood, overlap, or accounting boundary. | Establish the exact delimitation, A.15.1 Work relation or non-Work carrier identity and phase relation, stock, window, and policy before aggregation. |
| Untyped total hides conversion | Hours, energy, material, money, and data are added as one number. | Keep resource vectors typed until an explicit conversion relation or model is declared admissible under the applicable measurement or mathematical-lens pattern. |
| Shared stock is double-counted | The same person, tool, inventory, meter, dataset, or port appears in multiple work slices. | Declare overlap and deduplication policy, or narrow admissible use. |
| Efficiency becomes emergence | Reduced resource use is treated as a new whole or synergy without reidentification. | Use measurement and evidence-use patterns first; use `B.2.P` only when whole reidentification remains current. |

### B.1.6:7 - Conformance Checklist

| ID | Requirement |
| --- | --- |
| CC-B1.6-1 | Every resource component names its Characteristic, Scale/Unit, subject, time stance, C.16 measurement work/result episteme, and uncertainty/provenance when current. |
| CC-B1.6-2 | The included dated Work occurrences, every A.15.1 Work-part relation used by the aggregation, every C.27.TA overlap fact it uses, and every separately used shared-stock relation are independently grounded; a separately used non-Work `PhaseOf` passes that carrier's direct identity rule. |
| CC-B1.6-3 | The aggregation policy names inclusion, conversion, weighting, missing values, boundary allocation, uncertainty, overlap/deduplication, and output kind. |
| CC-B1.6-4 | For dated aggregation Work, A.13 identifies the actual performer and A.15.1 independently admits the occurrence. F.6 is present only when the result must also identify the assignment under which that Work was performed. The Method, actual direct/A.6.1 bindings, resources, and temporal extent remain separate. |
| CC-B1.6-5 | The B.1.6 aggregation result and the distinct C.2.1 result episteme are recoverable; neither is a ledger row or generic result field. |
| CC-B1.6-6 | A.10/G.6 provenance and G.11 currentness remain separate from measurement and aggregation results. |
| CC-B1.6-7 | Planned values and A.15.5 resource readiness are not presented as measured performed-work aggregation. |
| CC-B1.6-8 | A ledger, policy, profile, clause, citation, dashboard, or graph edge establishes none of work, participation, measurement, part/overlap, aggregation, or result identity. |
| CC-B1.6-9 | Any yield, efficiency, comparison, assurance, transformation, whole-reidentification, or decision claim names its exact subject pattern. |

### B.1.6:8 - Common Anti-Patterns and How to Avoid Them

| Overread | Repair |
| --- | --- |
| A method or algorithm is treated as the work-resource roll-up. | Use `A.3.1` or `A.3.2`; use `B.1.6` only for the resource aggregation claim. |
| A work plan is treated as measured work. | Use `A.15.2` for the plan and `A.15.1` for performed work evidence. |
| A phase label or timeline is treated as a resource ledger or as proof of a Work relation. | Recover the exact subject first: A.15.1 for Work temporal parts or occurrences, the carrier's identity pattern plus A.14 for proper non-Work `PhaseOf`, and B.1.4 only for bounded aggregation of already recovered temporal relations. Add B.1.6 only when typed resource values are being aggregated. |
| A resource gain is treated as emergence. | Use measurement and evidence-use patterns first; use `B.2.P` only if whole reidentification remains current. |
| A ledger, dashboard, or report total is treated as the aggregation result. | Recover the source publications, C.16 measurements, work set and relations, policy, dated aggregation work, B.1.6 result, C.2.1 episteme, and A.10/G.6 provenance. |

### B.1.6:9 - Consequences

This pattern defines a conservative predicate and result form for typed resource aggregation while keeping each input measurement, performed work occurrence, aggregation policy/application, result episteme, work relation, and provenance path distinct.

The cost is explicit accounting discipline. The gain is that resource roll-ups become comparable without claiming more than the evidence and boundary relation allow.

### B.1.6:9.1 - Rationale

`B.1.6` exists because a convenient total can hide several ontically different chains. Admit its result after exact resource measurement, Work-set and overlap grounding, an edition-pinned aggregation policy, and dated aggregation Work. The ledger represents that recovered account.

The pattern keeps the useful old `Gamma_work` notation, but only as notation over a recovered aggregation record. It also preserves the old planned-versus-measured warning: a method description or work plan can declare expected yield or expected resource use, but measured aggregation depends on dated work evidence.

### B.1.6:9.2 - SoTA-Echoing

Source qualification was checked against the publishers' current surfaces on 2026-07-30. Because ISO and GHG Protocol announced active joint development of an updated product-accounting standard in 2026, these decisions remain qualified only through 2027-01-30 unless a new draft, amendment, confirmation status, or published replacement appears earlier. Internal FPF neighbour authority stays in Relations; it is not presented as an external source decision.

| Exact source and source-use decision | Visible B.1.6 mutation | Rejected overread | Smallest source-change replay |
| --- | --- | --- | --- |
| [ISO 14040:2006 with Amendment 1:2020, confirmed current in 2022](https://www.iso.org/standard/37456.html), and [ISO 14044:2006 with Amendments 1:2017 and 2:2020, confirmed current in 2022](https://www.iso.org/standard/38498.html) — **adapt** goal/scope, system-boundary, inventory, allocation, reporting, and intended-use discipline to one exact work-resource aggregation. | `Exact policy`, `Overlap and shared stocks`, the engine-programme case, and `CC-B1.6-2/3` require boundary, work set, allocation, overlap/deduplication, output kind, and intended use before a total is admitted. | An LCA boundary, inventory table, category, or reported total does not establish FPF work parthood, measurement, aggregation work, result identity, or admissibility for every later use. | Reopen only `Exact policy`, `Overlap and shared stocks`, the engine-programme allocation paragraph, and `CC-B1.6-2/3` if ISO changes boundary or allocation requirements. |
| [GHG Protocol *Product Life Cycle Accounting and Reporting Standard*, 2011](https://ghgprotocol.org/product-standard), including its allocation and double-counting requirements — **adapt** process subdivision/system expansion before allocation, physical or other justified allocation, and explicit double-count control for shared processes/stocks. | The ledger's shared-resource row, `Overlap and shared stocks`, the manufacturing-cell case, and `CC-B1.6-2/3` require an independently grounded overlap/shared-use fact and one edition-pinned allocation or deduplication rule. | Co-listing, a common meter, corporate/category membership, or a convenient allocation key does not prove disjointness, work structure, or a universal resource share. | Reopen only the shared-resource ledger row, `Overlap and shared stocks`, the manufacturing-cell case, and `CC-B1.6-2/3` when the joint ISO/GHG replacement changes shared-process allocation or double-count rules. |
| [JCGM GUM-6:2020, *Developing and using measurement models*](https://doi.org/10.59161/JCGMGUM-6-2020) — **adapt** input-quantity, model-adequacy, covariance, and uncertainty-propagation discipline to the edition-pinned aggregation policy. | `Uncertainty and provenance`, the engine-programme case, and `CC-B1.6-1/3` require the input measurement uncertainties, correlations/conversions, propagation method, and qualified output uncertainty to remain distinct from provenance. | Adding source refs, estimates, or point totals does not propagate uncertainty; aggregation does not make incompatible models or quantities commensurable. | Reopen only `Uncertainty and provenance`, the engine-programme uncertainty sentence, and `CC-B1.6-1/3` if GUM changes model or propagation requirements. |
| [ISO 80000-1:2022, *Quantities and units — Part 1: General*](https://www.iso.org/standard/76921.html) — **adapt** quantity-kind, unit, quantity-value, dimension, and coherent-unit discipline only for typed aggregation inputs and outputs. | `Typed resource basis`, the model-training case, and `CC-B1.6-1/3` keep joules, hours, mass, currency, bytes, and attention distinct unless an exact conversion/normalization and output kind are declared. | A shared numeral, unit label, normalized score, or vector slot does not authorize cross-kind addition, scalarization, efficiency, or comparability. | Reopen only `Typed resource basis`, the affected typed component in the model-training case, and `CC-B1.6-1/3` if ISO 80000 changes the mapped quantity/unit distinction. |

Source refresh is local: replay the row's named rule, case, and checklist rows first. Widen only when that replay contradicts another current B.1.6 locus; a changed accounting source cannot by itself create work, overlap, measurement, result episteme, provenance, or a downstream verdict.

### B.1.6:10 - Relations

- Builds on A.13 for actual performers, A.15.1 for independently admitted dated measurement or aggregation Work, F.6 when a result must also identify the assignment under which that Work was performed, and A.6.1 for declarations and actual bindings; C.2.1 governs measurement-result and aggregation-result epistemes.
- Coordinates with `A.3.1`, `A.3.2`, and `A.15.2` for method, method description, and work plan.
- Coordinates with `A.15.5` for work-entry readiness, full-kit condition, and resource readiness before work entry; B.1.6 may cite those refs but does not decide readiness.
- Coordinates with `A.15.1` for exact Work temporal parts, episodes, operational parts, overlaps, retries, resumptions, and later occurrences; with `B.1.4` only for bounded aggregation of already recovered temporal relations; and with `C.27` for temporal-claim adequacy.
- Coordinates with `A.1`, `B.1`, `A.14`, and `C.13` for holon delimitation, part-whole, proper temporal restriction and `PhaseOf` for a non-Work carrier, and constructive grounding.
- Coordinates with `A.3.4` for transformation. When whole reidentification or emergence-family wording is current, `B.2.P` tests the problem and the relevant B.2-family pattern defines or constrains the recovered claim.
- Coordinates with `C.16` for resource Characteristics and measurement results; `A.10` and `G.6` for provenance; `G.11` for currentness; `C.29` for representation or mathematical-lens claims; A.15.1 for Work relations; A.14 and B.1.4 for non-Work part or phase relations and their bounded aggregation; E.17 for publication; and the applicable comparison, assurance, transformation, reidentification, or decision pattern when those uses are current.

### B.1.6:End

