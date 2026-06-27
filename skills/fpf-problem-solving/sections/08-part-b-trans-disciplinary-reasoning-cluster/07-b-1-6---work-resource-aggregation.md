## B.1.6 - Work-Resource Aggregation

> **Type:** B-family aggregation pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Use this when.** Use this pattern when the current claim aggregates resources, effort, time, energy, material, information, cost, or another measured resource over dated work occurrences, phase slices, boundary partitions, or comparable work-resource ledgers.

**Not this pattern when.** If the current question is the method as a way of doing, use `A.3.1`. If it is a method description, SOP, algorithm text, simulator configuration, or formal expression, use `A.3.2`. If it is a work plan, use `A.15.2`. If it is whether work occurred, use `A.15.1`. If it is work-entry readiness, full-kit condition, or resource readiness before work entry, use `A.15.5`. If it is temporal phase aggregation without resource accounting, use `B.1.4`. If it is a transformation claim, use `A.3.4`. If apparent resource gain changes whole identity, use `B.2.P` before any B.2-family owner.

**What goes wrong if missed.** Resource, effort, time, energy, or cost totals are read from methods, plans, dashboards, or phase labels without a dated work occurrence, resource ledger, and overlap policy.

**What this buys.** The practitioner can aggregate resources over performed work while avoiding double counting and returning method, plan, transformation, evidence, and MHT claims to their direct owners.

### B.1.6:1 - Problem Frame

Practitioners need to roll up work-resource claims across runs, phases, teams, devices, stations, model-training epochs, or evidence-production episodes. The recurring error is to treat a method, method description, plan, phase label, dashboard, or expected efficiency as if it were measured performed work.

`B.1.6` governs the work-resource aggregation claim. It keeps dated work occurrence, method, method description, work plan, resource ledger, holon delimitation, transformation, evidence, and whole reidentification in their own owners.

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

### B.1.6:2 - Solution

Recover a `WorkResourceAggregation@Context`:

```text
WorkResourceAggregation@Context:
  aggregationConcernRef
  parentWorkOccurrenceRef?
  workOccurrenceRefs
  boundedContextRef
  transformedOrAffectedEntityRef?
  holonDelimitationRefs
  boundaryCrossingRelationRefs?
  timeWindowRef
  phaseRelationRefs?
  resourceBasisRefs
  resourceMeasureRefs
  resourceLedgerRefs
  overlapOrDeduplicationPolicyRef?
  methodRefs?
  methodDescriptionRefs?
  workPlanRefs?
  evidenceOrMeasurementRefs
  aggregationRuleRef
  aggregatedResourceValueRef
  admissibleUse
  nonAdmissibleOverread
  strongerSourceReturnCondition
```

The record is a resource-aggregation relation over work evidence. It is not a method, not a method description, not proof that planned work happened, not a new holon level, and not a whole reidentification claim.

Resource readiness is a neighboring claim, not a measured aggregation result. Planned capacity, reserved inventory, staffing availability, or a full-kit-looking label may be cited as a work-plan, source, or readiness reference, but `A.15.5` governs whether intended work is ready to enter performed-work execution. `B.1.6` governs only the resource-accounting basis, ledger, evidence, aggregation rule, and aggregated value for dated work occurrences or explicitly narrowed planned estimates.

#### B.1.6:2.1 - Direct Owner Map

| Current claim | Direct owner |
| --- | --- |
| Semantic way of doing | `A.3.1` |
| Description of the way of doing, including algorithm text or SOP | `A.3.2` |
| Planned work window or planned assignment | `A.15.2` |
| Work-entry readiness, full-kit condition, or resource readiness before work entry | `A.15.5` |
| Dated performed work occurrence and occurrence evidence | `A.15.1` |
| Work-resource aggregation over dated work occurrences | `B.1.6` |
| Holon delimitation, ports, interfaces, or part-whole boundary used for accounting | `A.1`, `B.1`, `A.14`, `C.13`, or the direct relation owner named by value |
| Boundary-crossing change under conditions | `A.3.4` |
| Phase relation or temporal coverage | `B.1.4` and `A.14`; use `C.27` when temporal claim adequacy is current |
| Measurement construction, units, scales, thresholds, or comparability | `C.16`, `C.16.P`, or `C.29` |
| Evidence provenance, source currentness, or source-use relation | Use `A.10` for evidence-use relations. Use `E.17` for publication and publication-use relations. Use the direct publication or source owner when a more specific source-use claim is being made. |
| Apparent free efficiency, synergy, or whole reidentification | `B.2.P`, then B.2-family owner only if recovered |

### B.1.6:3 - Optional `Gamma_work` Notation

`Gamma_work` is optional notation for a recovered `WorkResourceAggregation@Context`.

```text
Gamma_work(workResourceAggregationRecord, resourceBasis, aggregationRule)
  -> aggregated resource value plus ledger
```

The notation applies only after the work occurrence refs, resource-accounting basis, time window, holon delimitation, and evidence or measurement refs have been named. It does not order method steps, certify the method, create work evidence, or declare emergence.

### B.1.6:4 - Ledger Discipline

A conforming `WorkResourceAggregation@Context` includes a work-resource ledger with:

- work occurrence refs or parent and child work occurrence refs;
- resource-accounting basis and unit refs;
- time window and phase refs when time slicing is used;
- holon delimitation refs and any boundary-crossing relation refs used for accounting;
- method, method-description, and work-plan refs only when those objects are actually used;
- evidence, measurement, or source refs for the resource values;
- overlap or deduplication policy when work occurrences share resources, time windows, ports, stocks, people, tools, or data;
- admissible use and non-admissible overread.

For any resource type in the selected resource-accounting basis, the ledger should say whether the value is measured, estimated, normalized, or converted. If the value is measured, it names the measurement or evidence relation. If the value is planned, it stays marked as expected work-resource use and does not become performed-work evidence.

When the aggregation divides a stock or resource amount, use `PortionOf` or the direct quantitative relation owner. When the aggregation slices one work occurrence or one carrier over time, use `PhaseOf` or the direct phase owner. Do not use `MemberOf` for resource stock, resource portion, or time-slice composition.

### B.1.6:5 - Aggregation Rules

**Resource vectors stay typed.** Add joules to joules, hours to hours, kilograms to kilograms, and bytes to bytes. A conversion or equivalence relation needs its governing measurement, model, or mathematical-lens owner.

**Partition additivity requires declared partitions.** Resource values may be added across disjoint boundary partitions only after the boundary and stock relation are named. Shared stock, shared meters, shared people, shared tools, or overlapping time windows require an overlap or deduplication policy.

**Time slicing requires temporal coverage.** A resource roll-up over phases uses non-overlapping phase refs and a time window. If a missing phase matters, the admissible use is narrowed or `B.1.4`/`C.27` supplies the temporal owner.

**Plan and result stay separate.** A method description or work plan may provide expected yield, expected duration, or expected resource use. Measured work-resource aggregation uses dated work occurrence evidence. Do not overwrite one with the other.

**B.1 invariant carry-through.** `B.1.6` keeps B.1 invariants only for recovered work-resource ledgers. A singleton zero-resource occurrence is idempotent for the selected resource-accounting basis. Addition is commutative only for independent partitions, non-overlapping slices, or explicitly deduplicated overlaps. Weakest-link claims must name the critical resource, availability, or threshold; monotonicity claims must name the resource characteristic being improved. Apparent "free" gains remain measurement, equivalence, or whole-reidentification questions until their direct owner is recovered.

**Proof-sketch obligations.** For idempotence, show the zero-resource or singleton ledger under the selected resource-accounting basis. For commutativity or locality, show disjoint boundary partitions, disjoint time slices, or the declared deduplication relation. For weakest-link, name the critical resource and availability condition. For monotonicity, name the exact resource characteristic that cannot get worse under the selected improvement. These are user-facing obligations for the aggregation claim, not a separate proof package.

#### B.1.6:5.1 - Compact Obligation Rows

| Obligation | What must be named | Why it matters |
| --- | --- | --- |
| Typed resource vector | Resource-accounting basis, unit, measure, evidence refs, and source refs for each component. | Prevents hours, energy, material, cost, and data volume from becoming one undifferentiated total. |
| Disjoint partition | Boundary partition, stock relation, time window, and work occurrence refs. | Allows addition only where the partitions are actually disjoint for the selected resource-accounting basis. |
| Shared-stock handling | Shared meter, shared tool, shared person, shared data, shared inventory, or overlap policy. | Prevents double counting and false savings. |
| Critical resource cap | The capacity, availability, threshold, or bottleneck resource whose limit governs the claim. | Makes weakest-link and capacity claims inspectable. |
| Yield relation | Input resource refs, output result refs, loss refs, and measurement basis. | Keeps efficiency from being asserted without a result relation. |
| Embodied and dissipated split | Which resource remains embodied in the changed entity and which is dissipated, consumed, wasted, or externalized. | Keeps conservation, loss, and waste claims from being collapsed into one spent-resource label. |
| Loss monotonicity | The exact loss, waste, delay, cost, risk, or degradation characteristic being bounded or reduced. | Allows monotone improvement claims only for a named characteristic. |
| Plan-result separation | Expected resource use from method description or work plan versus measured resource use from dated work evidence. | Prevents a plan or algorithm from proving performed-work resource use. |

### B.1.6:6 - Archetypal Grounding (Worked Slices)

**Manufacturing cell.** A frame is welded and painted in two dated work occurrences. `B.1.6` records electricity, gas, consumables, and labor-hour ledgers with their time windows and meters. The step order belongs to `B.1.4` or the method owner; the state change of the frame belongs to `A.3.4`.

**Model training.** A model-training run has epochs as dated work slices. `B.1.6` aggregates compute energy, storage reads, and operator time from work evidence. The algorithm text is `A.3.2`; the trained model publication and source-use claims use episteme and publication owners; fairness or ethical assurance uses D-patterns when current.

**Architecture documentation effort.** A team records work spent building a multi-view architecture description. `B.1.6` can aggregate the work-resource ledger. The architecture description itself remains `C.30.AD`; the usefulness or adequacy of a view remains `C.30.ASV` or its direct owner.

### B.1.6:6.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Plan becomes evidence | Expected yield or expected resource use is read as performed work. | Keep planned and measured values separate and name the work occurrence evidence. |
| Boundary word carries accounting | A port, interface, team, device, or phase label is used without a holon delimitation or boundary-crossing relation. | Name the delimitation, stock, time window, and measurement relation before aggregating. |
| Untyped total hides conversion | Hours, energy, material, money, and data are added as one number. | Keep resource vectors typed until a measurement, model, or mathematical-lens owner admits conversion. |
| Shared stock is double-counted | The same person, tool, inventory, meter, dataset, or port appears in multiple work slices. | Declare overlap and deduplication policy, or narrow admissible use. |
| Efficiency becomes emergence | Reduced resource use is treated as a new whole or synergy without reidentification. | Use measurement and evidence owners first; return to `B.2.P` only when whole reidentification remains current. |

### B.1.6:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-B1.6-1 | The aggregation names dated work occurrence refs or explicitly narrows use to planned estimates. | Prevents plans and method descriptions from masquerading as performed work. |
| CC-B1.6-2 | Resource-accounting basis, units, measurement refs, evidence refs, and source refs are named. | Keeps resource values comparable and reviewable. |
| CC-B1.6-3 | Holon delimitation and any boundary-crossing relation used for accounting are named by value. | Prevents an unexplained boundary word from carrying the claim. |
| CC-B1.6-4 | Time windows, phase refs, and overlap and deduplication policy are present when slices or shared resources are aggregated. | Prevents double counting and missing epochs. |
| CC-B1.6-5 | Method, method-description, work-plan, transformation, and whole-reidentification claims use their direct owners. | Keeps work-resource aggregation from absorbing neighboring objects. |
| CC-B1.6-5a | Work-entry readiness, full-kit condition, and resource readiness before work entry use `A.15.5`; B.1.6 cites such refs only as neighboring inputs when a resource aggregation claim also exists. | Keeps planned or reserved resource availability from becoming measured performed-work aggregation. |
| CC-B1.6-6 | `Gamma_work` is used only as notation over a recovered aggregation record. | Keeps algebraic notation from becoming ontology by spelling. |

### B.1.6:8 - Common Anti-Patterns and How to Avoid Them

| Overread | Repair |
| --- | --- |
| A method or algorithm is treated as the work-resource roll-up. | Use `A.3.1` or `A.3.2`; use `B.1.6` only for the resource aggregation claim. |
| A work plan is treated as measured work. | Use `A.15.2` for the plan and `A.15.1` for performed work evidence. |
| A phase label or timeline is treated as a resource ledger. | Use `B.1.4` for phase aggregation and add `B.1.6` only when resource values are being aggregated. |
| A resource gain is treated as emergence. | Use measurement and evidence owners first; use `B.2.P` only if whole reidentification remains current. |
| A dashboard or report total is treated as proof. | Recover publication-use, source-use, and evidence relations before using the total. |

### B.1.6:9 - Consequences

This pattern gives FPF a conservative place for work-resource aggregation without turning it into a general method algebra. It makes resource claims usable across levels, phases, and contexts while keeping performed work evidence, measurement, temporal coverage, and transformation separate.

The cost is explicit accounting discipline. The gain is that resource roll-ups become comparable without claiming more than the evidence and boundary relation allow.

### B.1.6:9.1 - Rationale

`B.1.6` exists because work-resource accounting is easy to confuse with method, plan, phase, transformation, evidence, and whole reidentification. The governed object is the resource aggregation claim over dated work occurrences or explicitly narrowed estimates. That claim needs a ledger discipline: typed resource-accounting basis, holon delimitation, time window, stock and boundary-crossing relation, measurement or evidence relation, and overlap policy.

The pattern keeps the useful old `Gamma_work` notation, but only as notation over a recovered aggregation record. It also preserves the old planned-versus-measured warning: a method description or work plan can declare expected yield or expected resource use, but measured aggregation depends on dated work evidence.

### B.1.6:9.2 - SoTA-Echoing

| Source line | Practical implication for this pattern |
| --- | --- |
| Conservation and engineering accounting practice | Resource roll-ups need a selected resource-accounting basis, boundary, stock relation, and time window before addition is meaningful. |
| Constructive mereology and phase discipline | Resource portions, work phases, and collection membership are different relations; `PortionOf`, `PhaseOf`, and `MemberOf` cannot substitute for one another. |
| Measurement and mathematical-lens discipline | Unit conversion, normalization, efficiency, and typed vectors need their measurement, model, or mathematical-lens owner. |
| Work and method distinction in FPF | A method, method description, or work plan can guide expected resource use, but performed-work aggregation requires dated work occurrence evidence. |

### B.1.6:10 - Relations

- Builds on `A.15.1` for dated work occurrence and on `A.15` for role-method-work alignment.
- Coordinates with `A.3.1`, `A.3.2`, and `A.15.2` for method, method description, and work plan.
- Coordinates with `A.15.5` for work-entry readiness, full-kit condition, and resource readiness before work entry; B.1.6 may cite those refs but does not decide readiness.
- Coordinates with `B.1.4` and `C.27` for phase and temporal-claim adequacy.
- Coordinates with `A.1`, `B.1`, `A.14`, and `C.13` for holon delimitation, part-whole, phase, and constructive grounding.
- Coordinates with `A.3.4` for transformation. When whole reidentification or emergence-family wording is current, `B.2.P` tests the problem and the relevant B.2-family pattern governs the recovered claim.
- Coordinates with `C.16`, `C.29`, and `A.10` for measurement, mathematical lens, and evidence relations; source-use and publication-use relations remain with `E.17` or the direct source owner.

### B.1.6:End

