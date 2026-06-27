## B.1.4 - Contextual and Temporal Aggregation

> **Type:** B-family aggregation pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Use this when.** Use this pattern when the current claim aggregates relations across a bounded context, ordered situation, phase set, or time window, and the question is not just ordinary part-whole construction. Typical cues are ordered steps, order-sensitive argument chains, version histories, asset histories, phases of one carrier, rolling windows, context-scoped roll-ups, or time-sliced evidence.

**Not this pattern when.** If the question is ordinary part-whole or collection admission, use `B.1`, `A.14`, and `C.13`. If the question is the method as such, method description, work plan, or dated work occurrence, use `A.3.1`, `A.3.2`, `A.15.2`, or `A.15.1`. If the question is work-resource accounting, use `B.1.6`. If the question is changed identity, use `A.3.4`; if a new whole must be reidentified, use `B.2` through `B.2.P`. If the question is temporal adequacy of a claim, use `C.27`.

**What goes wrong if missed.** Order, phase, context, or time-window wording becomes ordinary parthood, method order, performed work, evidence currentness, or whole reidentification by label.

**What this buys.** The practitioner can aggregate context-sensitive and temporal material while returning method, work, transformation, work-resource, temporal-adequacy, and MHT claims to their direct owners.

### B.1.4:1 - Problem Frame

Many useful aggregates are not simple unordered wholes. A manufacturing sequence changes meaning when steps are swapped. An argument chain depends on which premise is used before which lemma. A turbine, paper, or dataset may be considered as the same carrier across phases. In these cases the aggregation is about contextual order or temporal coverage, not about a new level, a generic boundary, or a hidden interaction kind.

`B.1.4` governs the aggregation claim. It asks which EntityOfConcern is being aggregated, which context or time window bounds the claim, which ordered or phase relation is being used, what the aggregate may be used for, and which neighboring owner must carry stronger claims.

### B.1.4:1.1 - Problem

Without this pattern, four errors recur. First, `SerialStepOf` or another ordered relation is read as ordinary parthood, so changing the order looks harmless even when the aggregate meaning changes. Second, a phase label is read as a new holon level or a new whole, so identity change is hidden instead of handled by whole reidentification. Third, design-time plans, possible method order, run-time histories, and evidence windows are folded together as one sequence. Fourth, mathematical order, graph, or operator notation starts to govern the in-life object instead of expressing a recovered relation for one bounded use.

The practical failure is not a missing diagram. It is an inadmissible aggregate: the user cannot tell which carrier is being followed, which relation is ordered, which time window is covered, whether gaps or overlaps matter, and which stronger owner must carry work, resource, transformation, evidence, or whole-reidentification claims.

### B.1.4:1.2 - Forces

| Force | Tension |
| --- | --- |
| Order sensitivity vs. ordinary parthood | Ordered positions must remain reviewable without recasting them as parts of one physical whole. |
| Temporal coverage vs. carrier identity | A phase aggregate needs useful time windows, but it must not hide that the carrier changed identity. |
| Design-time relation vs. run-time history | Method order, work plan, and performed work often share labels, but they are different claims. |
| Compact notation vs. ontology | `Gamma_ctx`, `Gamma_time`, graph, or algebra notation can make a relation easy to use, but cannot create a holon, method, work occurrence, or transformation. |
| Local aggregation vs. stronger return | The pattern should keep a small aggregation record, while sending resource, evidence-currentness, transformation, and MHT claims to their owners. |

### B.1.4:2 - Solution

Recover a `ContextTemporalAggregation@Context` before using the aggregate:

```text
ContextTemporalAggregation@Context:
  aggregationConcernRef
  aggregatedEntityOfConcernRef
  boundedContextRef
  aggregationMode: contextualOrder | temporalPhase | declaredMixedUse
  orderedRelationRefs?
  phaseRelationRefs?
  orderSpecRef?
  timeWindowRef?
  carrierIdentityRef?
  independenceOrJoinConditionRefs?
  coverageAndNonOverlapConditionRefs?
  boundaryCrossingRelationRefs?
  relatedMethodRefs?
  relatedMethodDescriptionRefs?
  relatedWorkOccurrenceRefs?
  relatedWorkResourceAggregationRefs?
  relatedTransformationRefs?
  relatedWholeReidentificationRefs?
  evidenceOrSourceRefs
  admissibleUse
  nonAdmissibleOverread
  strongerSourceReturnCondition
```

Use the record as a small typed relation, not as a new durable `U.Level`, `U.Boundary`, `U.Interaction`, or generic process object.

#### B.1.4:2.1 - Two Aggregation Modes

| Mode | Current object | Required relation discipline | Typical use |
| --- | --- | --- | --- |
| Contextual order aggregation | A bounded set of relation positions whose order, partial order, or join structure changes meaning. | `OrderSpec`, ordered relation refs, join or independence conditions, and a bounded context. | Ordered method relation, order-bound argument chain, staged construction description, controlled sequence. |
| Temporal phase aggregation | One carrier considered through phases or time slices. | Carrier identity, `PhaseOf` or phase relation refs, `TimeWindow`, coverage, and non-overlap conditions. | Asset history, revision history, experimental run phases, dated evidence window. |

If one source phrase mixes both modes, split the record. A method may have an ordered relation structure, and the work that enacts it may also have dated phases, but those are different claims.

#### B.1.4:2.2 - Direct Owner Map

| Current claim | Direct owner |
| --- | --- |
| Method as semantic way of doing | `A.3.1` |
| Method description, SOP, algorithm text, simulator configuration, or formal expression | `A.3.2`, with publication owners when publication use is current |
| Work plan | `A.15.2` |
| Dated work occurrence, performed episode, or evidence that work happened | `A.15.1` |
| Work-resource roll-up, spent resource, cost, effort, energy, material, or comparable ledger | `B.1.6` |
| Phase relation, portion relation, membership, or parthood | `A.14`, `B.1`, and `C.13` as appropriate |
| Holon delimitation or boundary-crossing relation | `A.1`, `B.1`, `A.12`, `A.3.4`, or the direct relation owner named by value |
| Bounded change under conditions | `A.3.4` |
| Whole reidentification, emergence-family wording, MHT, MET, MFT, synergy, or metric-mirage wording | Use `B.2.P` to test whether a whole-reidentification problem is current. If it remains current, use `B.2`, `B.2.2`, `B.2.3`, `B.2.4`, or `B.2.5` according to the recovered whole, emergence, autonomy, capability, or supervisor relation claim. |
| Architecture structural view or selected structure | `C.30.ASV`, `A.22`, or the architecture owner named by value |
| Mathematical order, graph, algebraic notation, graph path, or morphism used as expression | Use `C.29` when mathematical-lens adequacy, preserved structure, lost structure, payoff, or stop condition is being evaluated. Use `E.18` when the selected transformation-flow structure is current. Use `E.18.2` when the mathematical expression of that selected structure is current. |

### B.1.4:3 - Optional Operator Notation

`Gamma_ctx` and `Gamma_time` are optional notation for already recovered aggregation claims.

```text
Gamma_ctx(contextualAggregationRecord, orderSpec, independenceAndJoinConditions)
  -> contextual aggregate record

Gamma_time(temporalAggregationRecord, timeWindow, coverageAndNonOverlapConditions)
  -> temporal aggregate record
```

The notation does not create a holon, transformation, method, work occurrence, or whole reidentification by itself. It records how the selected relation set is combined for the current use.

If the source says a system actually sequences, combines, transforms, measures, or audits something, name that acting-side relation separately through `A.12`, `A.3.4`, `A.15.1`, `B.1.6`, `A.10`, or the direct owner. The person, team, controller, or tool that writes an aggregation record is not automatically the in-world transformer for the EntityOfConcern being aggregated.

### B.1.4:4 - Admissible Checks

For contextual order aggregation:

- the ordered relation refs are named by value;
- the `OrderSpec` is declared as total order, partial order, or another named relation;
- independence, branch, or join conditions are named when parallel factors are used;
- all claims stay within one bounded context unless a boundary-crossing relation is named;
- method, method-description, work, transformation, and resource claims use their direct owners.

For temporal phase aggregation:

- the carrier identity is recoverable;
- the time window is declared;
- phase intervals are covered and non-overlapping, or the admissible use is narrowed;
- identity change is not hidden as another phase;
- work-resource and evidence-currentness claims use `B.1.6`, `A.10`, and `C.27` when current.

**B.1 invariant carry-through.** `B.1.4` keeps B.1 invariants only after the current relation is recovered. A singleton ordered relation or singleton phase is idempotent for the selected use. Contextual aggregation is deterministic only relative to the declared `OrderSpec` and join or independence conditions. Temporal aggregation is valid only relative to carrier identity, coverage, and non-overlap. Weakest-link and monotonicity claims must name the characteristic being bounded or improved; otherwise the aggregate is only an aggregation record, not a performance, safety, or assurance claim.

#### B.1.4:4.1 - Compact Obligation Rows

| Obligation | What must be named | Why it matters |
| --- | --- | --- |
| Independence and joins | Branch relation refs, join relation refs, and the condition under which branches may be combined. | Prevents an ordered aggregate from silently treating dependent branches as independent evidence or work. |
| Order specification | Total order, partial order, precedence relation, or another named relation over the selected positions. | Keeps order-sensitive claims from being read as unordered collection claims. |
| Decisive dependency relation | The relation that makes one position, delay, or missing step decisive for the aggregate use. | Allows weakest-link claims only when the decisive relation is visible. |
| Carrier identity | The carrier being followed across phases and the condition under which it remains the same EntityOfConcern. | Prevents temporal aggregation from hiding identity change or MHT. |
| Temporal coverage | Time window, phase refs, coverage rule, and non-overlap or overlap policy. | Prevents missing phases and double counting. |
| Chronological discipline | The rule that separates chronological order, logical order, publication order, and performed-work order. | Keeps a document sequence, argument sequence, and work occurrence sequence from substituting for one another. |
| Monotone characteristic | The exact characteristic that is preserved, bounded, or improved when the aggregate grows. | Blocks generic monotonicity claims over an unspecified aggregate. |

### B.1.4:5 - Archetypal Grounding (Worked Slices)

**Manufacturing sequence.** A frame is prepared, welded, inspected, painted, and packed. `B.1.4` records the contextual order claim: selected steps, order specification, join conditions, and admissible use for planning or comparison. The actual shop-floor work occurrences use `A.15.1`; energy and material roll-ups use `B.1.6`; a changed frame state uses `A.3.4`.

**Paper revision history.** A paper has draft, reviewed, and camera-ready phases. `B.1.4` records the same episteme carrier across phases and the time or version window being claimed. Source-currentness and publication-use claims use `A.10` and `E.17`; the phase relation does not make the publication authoritative by itself.

**Cross-context evidence window.** A dashboard aggregates observations from two operating contexts. `B.1.4` records the bounded contexts and the admissible aggregation window. If one context has a different measurement basis, use `C.16` or `C.29` for comparability before relying on the aggregate.

### B.1.4:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Notation becomes ontology | `Gamma_ctx`, `Gamma_time`, graph, or algebra wording is treated as the governed object. | Recover the ordered or temporal relation first, then treat notation as a selected expression. |
| Sequence becomes work | A method order, plan order, document order, or performed-work history is treated as the same thing. | Name the direct owner: method, method description, work plan, dated work occurrence, or evidence window. |
| Phase becomes level | A phase label is used as a new system level or a new whole. | Recover carrier identity and `PhaseOf` or phase relation; return identity change to whole reidentification. |
| Coverage becomes authority | A complete-looking timeline is treated as sufficient evidence or currentness. | Use evidence, source-currentness, and temporal-adequacy owners when those claims are current. |

### B.1.4:6 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-B1.4-1 | The aggregate names the EntityOfConcern, bounded context, aggregation mode, and admissible use. | Prevents a context or time label from acting as ontology. |
| CC-B1.4-2 | Contextual aggregation names ordered relation refs and an `OrderSpec`; temporal aggregation names carrier identity, phase refs, and `TimeWindow`. | Keeps order and time as different relations. |
| CC-B1.4-3 | Independence, join, coverage, and non-overlap conditions are present when the claim uses them. | Keeps local composition reviewable. |
| CC-B1.4-4 | Method, method-description, work-plan, work-occurrence, work-resource, transformation, and whole-reidentification claims are assigned to their direct owners. | Prevents B.1.4 from absorbing neighboring objects. |
| CC-B1.4-5 | Mathematical notation is treated as a selected lens or expression, not as the governed object. | Keeps `Gamma_ctx`, `Gamma_time`, graph, and algebra language bounded. |
| CC-B1.4-6 | If identity changes, coverage breaks, or a new whole is claimed, the record narrows use or names the stronger owner. | Prevents temporal aggregation from becoming hidden MHT or transformation. |

### B.1.4:7 - Common Anti-Patterns and How to Avoid Them

| Overread | Repair |
| --- | --- |
| A sequence is treated as physical parthood. | Recover ordered relation refs and use contextual aggregation; use part-whole owners only for part-whole claims. |
| A phase label is treated as a new system level. | Recover the carrier identity and phase relation; use whole reidentification only if B.2.P keeps that claim current. |
| A planning order is treated as performed work. | Use `A.15.2` for work plan and `A.15.1` for dated work occurrence. |
| A resource total is placed inside temporal aggregation. | Use `B.1.6` for the work-resource ledger. |
| A diagram or table is treated as the aggregate. | Recover the Description episteme or publication relation and the EntityOfConcern separately. |

### B.1.4:8 - Consequences

This pattern makes ordered and temporal aggregation inspectable without turning every sequence, phase, or context label into a holon level. It also lets practitioners keep useful `Gamma_ctx` and `Gamma_time` notation while avoiding a category error: the notation is an apparatus over a recovered aggregation claim, not the in-life work, method, transformation, or whole.

The cost is that the practitioner must name the relation being aggregated. The gain is that contextual order, temporal coverage, work evidence, resource accounting, transformation, and whole reidentification stop interfering with one another.

### B.1.4:8.1 - Rationale

`B.1.4` exists because contextual order and temporal phase aggregation are neither ordinary part-whole construction nor generic process talk. The same carrier can be considered through phases; a selected relation set can be order-sensitive; and both cases need admissible aggregation without inventing a new holon kind. The pattern therefore keeps relation discipline explicit: `PhaseOf` and carrier identity for phase aggregation; ordered relation refs and `OrderSpec` for contextual aggregation; direct-owner return for method, work, resource, transformation, evidence, and whole reidentification.

The old `DesignRunTag` warning is preserved as a rule rather than a label: do not fold design-time possible order and run-time history into one aggregate. If both are needed, make two records and relate them by value.

### B.1.4:8.2 - SoTA-Echoing

| Source line | Practical implication for this pattern |
| --- | --- |
| Constructive and mereological treatment of phases and parts | Phase aggregation must preserve carrier identity and coverage conditions; it cannot borrow ordinary parthood when the current relation is temporal. |
| Engineering process and ordered-method notations | Ordered relations may be useful expressions of method or plan structure, but performed work and resource accounting need their direct owners. |
| Temporal modeling and evidence-currentness practice | A time window or complete phase list does not by itself prove source currentness, admissible evidence, or causal support. |
| Mathematical-lens discipline in FPF | Graph, order, and algebra notation are selected expressions over recovered relations, not ontology by spelling. |

### B.1.4:9 - Relations

- Builds on `B.1`, `A.14`, and `C.13` for part-whole, phase, and constructive grounding discipline.
- Coordinates with `A.3.1`, `A.3.2`, `A.15.2`, and `A.15.1` for method, method description, work plan, and dated work occurrence.
- Coordinates with `B.1.6` for work-resource aggregation.
- Coordinates with `A.3.4` for transformation. When whole reidentification or emergence-family wording is current, `B.2.P` tests the problem and the relevant B.2-family pattern governs the recovered claim.
- Coordinates with `C.27` for temporal-claim adequacy. When mathematical expression is selected, `C.29` governs lens-use adequacy, `E.18` governs selected transformation-flow structure, and `E.18.2` governs mathematical description of that selected structure.

### B.1.4:End

