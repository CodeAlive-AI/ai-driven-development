## C.27.TA - Temporal Aspect: Time Windows, Rhythm, Cadence, and Currentness

> **Type:** Definitional pattern
> **Status:** Stable
> **Normativity:** Normative except where a section is explicitly informative

### C.27.TA:0 - Use This When

Use this pattern when a project needs to state a positive temporal-aspect claim about one exact object or exact claim—for example, its time window, cadence, freshness, recovery timing, or currentness.

Use it when the working question is:

- which time window, interval, duration, latency, cadence, rhythm, synchronization, currentness, freshness, validity window, recovery timing, stabilization timing, trajectory, effort over time, inertia, or refresh condition matters;
- which bearer has that temporal property: system, episteme, work plan, work occurrence, claim, source, benchmark, architecture-selected structure, method description, publication, or project-world object;
- which temporal reference makes the statement reviewable: calendar time, clock time, event order, cycle, sprint, epoch, release train, sampling interval, follow-up interval, or domain-local timing reference; and
- whether the property is merely stated, measured, used in a temporal claim, used in a transformation claim, or used in a work, evidence, or decision relation.

**Primary EntityOfConcern.** The `EntityOfConcern` is the independently identified bearer or exact claim being qualified. A temporal label such as *cadence*, *freshness*, or *recovery timing* is a predicate or qualifier in the ClaimGraph; it is not a second entity.

**C.2.1 and publication boundary.** A materialized temporal-aspect statement is ClaimGraph content in one `C.2.1` episteme whose effective ReferenceScheme makes the temporal terms interpretable. Changing that claim content identifies another episteme. A changed layout, publication occurrence, form, or carrier can leave the episteme unchanged; those publication objects remain separate under `E.24.PUB` when availability matters. When the claim depends on another direct relation, cite that relation's exact declaration or independently established occurrence. A PatternID remains an ordinary rule citation and is never a relation reference.

**First useful move.** Identify the bearer or claim, state its temporal property, and supply the reference and extent needed to interpret it. An observed cadence needs the period observed; a general ordering rule can instead name the event types and their relative order.

**First result.** `CheckoutSystem-1 had a weekly release cadence during release train R14.` This is enough when the receiving action needs no further distinction. Stop there.

Open the fuller statement only when the receiving use also depends on measurement, an exact scheme or scope, a selected Structure, a source or use boundary, currentness, reopen conditions, coupling, another direct relation, or an explicit rule citation or blocked overread.

**What goes wrong if missed.** A cadence has no bearer, a currentness claim has no reference date, or a recovery estimate omits its starting event. Readers then cannot tell which temporal claim could support the receiving action.

**What this buys.** A practitioner can state one positive temporal-aspect claim before selecting `C.27`, `A.3.4`, `A.3.3`, `A.15.2`, `A.15.1`, `C.16`, `C.28`, `G.9`, or the relevant evidence, source, gate, or assurance pattern for the receiving use.

**Not this pattern when.**

- If the question is adequacy or supported use of an authored temporal claim, use `C.27`.
- If the question is bounded transformation under conditions, use `A.3.4`.
- If the question is a state-space and transition-law episteme, use `A.3.3`.
- If the question is work planning or dated work, use `A.15.2` or `A.15.1`.
- If the question is measurement construction, rate construction, scale, score, or metric comparability, use `C.16` and related characterization patterns.
- If the question is causal use of an intervention or policy, use `C.28`.
- If the temporal phrase is ordinary prose and no practical use changes, do not introduce a C.27.TA statement.

### C.27.TA:1 - Problem Frame

Distinguish two concerns. One concern is temporal-claim adequacy: whether an authored claim about speed, rhythm, rate-change, recovery, or stabilization can carry a named use. The other concern is positive temporal subject matter: windows, duration, cadence, synchronization, freshness, currentness, inertia, effort over time, recovery, stabilization, and trajectory as aspects of objects or claims.

C.27.TA addresses the second concern. It lets a practitioner state what temporal aspect is in play without immediately opening an adequacy card, a dynamics model, a work plan, a causal-use record, or a transformation statement.

### C.27.TA:2 - Problem

Without C.27.TA:

1. **Cadence and rhythm become decorative words.** A text says "release cadence" or "team rhythm" without naming the bearer, timing reference, or the extent to which the claim applies.
2. **Freshness becomes a vague virtue.** A source, benchmark, dashboard, or claim is called current without a reference date or the conditions that make it current for the intended use.
3. **Recovery and stabilization hide their interval.** A claim says "recover faster" or "stabilize" without saying after which disturbance, over what duration, and for which bearer.
4. **Effort and inertia float free.** A text speaks about momentum, residue, stored work, adaptation cost, or resistance without linking it to the relevant object and course of change.
5. **Transformation absorbs time silently.** A transformation statement names a change but leaves timing and ordering implicit, so method, mechanism, work, evidence, and temporal claims get tangled.

### C.27.TA:3 - Forces

| Force | Tension |
| --- | --- |
| Positive temporal subject vs claim adequacy | Some temporal aspects merely need to be named; others become authored temporal claims whose adequacy must be judged by C.27. |
| Bearer and interval | A rhythm, latency, recovery time, or validity window means little without a bearer and temporal reference. |
| Local timing vs durable use | A local work note may need one interval; a public claim, benchmark, source use, or assurance relation may need currentness and refresh discipline elsewhere. |
| Transformation and dynamics pressure | A temporal aspect can time a transformation or dynamics model without becoming the transformation or the dynamics episteme. |
| Measurement pressure | Some temporal aspects require measurement construction; others only need a named temporal reference. |

### C.27.TA:4 - Solution

#### C.27.TA:4.1 - Definition

A temporal-aspect claim says that an object or claim has a time-bearing or order-bearing property. Its temporal reference and extent must make that property interpretable: these may be a dated interval, a duration from an event, or a relation among recurring event types. For example, "each approval follows its corresponding review" specifies relative order without selecting a calendar window. A separate adequacy judgement under `C.27` is needed only when its answer could change the receiving use.

Typical temporal predicates and qualifiers include:

- `timeWindow`;
- `duration`;
- `latency`;
- `freshness`;
- `currentness`;
- `validityWindow`;
- `cadence`;
- `rhythm`;
- `synchronization`;
- `trajectory`;
- `recoveryTiming`;
- `stabilizationTiming`;
- `effortOverTime`;
- `inertiaOrResidue`;
- `refreshOrReopenCondition`.



#### C.27.TA:4.2 - Temporal Aspect Statement

Use this fuller statement when the receiving use needs the corresponding references or distinctions:

```text
TemporalAspectStatementClaimContent:
  entityOfConcernRef:
  aspectPredicate:
  temporalReference:
  windowOrInterval?:
  entityRulePatternCitation?:
  effectiveReferenceSchemeRef?:
  claimOrWorkScopeRef?:
  selectedStructureRef?:
  sourceOrUseBoundaryRef?:
  localUseCondition?:
  measuredReadingRef?:
  directRelationDeclarationRef?:
  obtainingRelationOccurrenceRef?:
  receivingUseRulePatternCitation?:
  validityOrCurrentnessCondition?:
  refreshOrReopenCondition?:
  blockedLocalOverread?:
```

When the statement is materialized, its claim content belongs to a `C.2.1` episteme. `entityOfConcernRef` resolves the bearer or claim being qualified; `aspectPredicate` states the property; `temporalReference` supplies the clock, event order or other timing basis. Include `windowOrInterval` when the claim is restricted to that extent or its interpretation requires one. Preserve any interval already asserted by the claim.

Add the remaining fields only when their values change the claim or receiving action. PatternID citations identify applicable rules. A claim about another direct relation needs that relation's declaration; an assertion of an obtaining occurrence also needs its actual participants and conditions. Scheme, scope, Structure, source and use references retain the identity and conditions defined by their respective patterns.

#### C.27.TA:4.3 - Direct Use and Rule Citation

| Temporal use | Direct pattern or rule citation |
| --- | --- |
| positive temporal-aspect claim about an object or claim | `C.27.TA` |
| adequacy or supported use of an authored temporal claim | `C.27` |
| bounded transformation under conditions with temporal reference | `A.3.4` plus `C.27.TA` |
| state-space or transition-law model | `A.3.3` |
| planned work timing | `A.15.2` |
| dated work occurrence or trace | `A.15.1` for the occurrence; `A.10` for evidence and provenance when a claim relies on the trace |
| measurement construction for rate, duration, latency, or freshness | `C.16` and related characterization patterns |
| causal-use timing, intervention window, comparator, or follow-up interval | `C.28` |
| benchmark freshness, baseline window, comparator edition, or parity window | `G.9` |
| source currentness, evidence decay, provenance, or assurance refresh | evidence, source, provenance, assurance, and refresh patterns |



#### C.27.TA:4.4 - Rhythm, Cadence, And Synchronization

A rhythm or cadence claim needs its bearer, recurrence or ordering property and timing reference. An empirical assertion such as a weekly cadence observed during R14 also needs that observation window. A planned rule such as "run a review every Friday while this plan applies" can state its recurrence and applicability directly. Add phase, synchronization, entrainment or other cross-bearer relations when the claim depends on them.

Optional reference-bearing form:

```text
RhythmAspectClaimContent:
  entityOfConcernRef:
  aspectPredicate: rhythm | cadence | synchronization
  timingReference:
  rhythmWindowRef?:
  intervalStructure?:
  rulePatternCitation?:
  directCouplingRelationDeclarationRef?:
  obtainingCouplingOccurrenceRef?:
  validityWindowRef?:
```

The optional fields appear only when the receiving use relies on them. A PatternID citation identifies the rule used to judge a claim; it is not the coupling relation.

A plain "release cadence" or "workshop rhythm" may remain ordinary prose. It needs C.27.TA when cadence or rhythm changes transformation, work planning, benchmark, source, assurance, coordination, or claim-use decisions.

#### C.27.TA:4.5 - Currentness, Freshness, And Validity Window

A currentness or freshness claim identifies the bearer, the property asserted, and the reference time or edition for the intended use. State a validity interval when the claim promises or establishes validity over that interval. "The registry entry was current when checked on 3 June" establishes no later validity period. A source, benchmark, model, dashboard, or claim may be fresh enough for one use and stale for another.

Add a source-use boundary, currentness condition, refresh condition, or reopen condition only when the receiving use changes when that value changes. Use the direct source, evidence, benchmark, assurance, or refresh pattern for the separate provenance, parity, assurance, or refresh-work claim.

#### C.27.TA:4.6 - Recovery, Stabilization, Inertia, And Effort Over Time

For recovery, stabilization, inertia or effort over time, identify the bearer and property, then recover the relevant starting event, timing reference and duration or observation interval. State the extent actually supported. Use C.27 when an unresolved question about the claim's adequacy changes the receiving action; a sufficient temporal-aspect claim can finish here.

Add the disturbance or starting condition, measured reading, effort, resistance, residue, inertia relation, rule citation, or direct-relation reference when the receiving use needs that distinction.

### C.27.TA:5 - Archetypal Grounding

#### C.27.TA:5.1 - Release Cadence

`CheckoutSystem-1 had a weekly release cadence during release train R14.`

This result identifies the bearer, cadence, release-train timing reference and R14 observation window. It is sufficient when the receiving use needs that cadence; a claim about its quality or effect needs separate grounds.

#### C.27.TA:5.2 - Source Freshness

A benchmark comparison uses a model report from April and a competitor report from June.

Identify what each report needs to be current about for the comparison, the relevant date or edition, and any period over which validity is claimed. April versus June publication dates alone establish neither staleness nor comparability. If no currentness basis is available, retain only the supported dated-report claim. `G.9` and the applicable source, evidence and benchmark patterns govern the separate parity, provenance and reliance questions.

#### C.27.TA:5.3 - Architecture Recovery Timing

An architecture move is expected to reduce an interlevel conflict after two release cycles.

C.27.TA states the expected recovery timing for the exact selected structure discussed by the C.30 architecture claim, under the release-cycle reference and window. Use A.22 and the applicable architecture pattern to identify that structure independently; the claim episteme is not its proxy. Use A.3.4 for the proposed structure transformation and evidence/result patterns for any observed effect.

```text
TemporalAspectStatementClaimContent:
  entityOfConcernRef: the exact independently identified selected structure discussed by the C.30 interlevel-conflict claim.
  entityRulePatternCitation: A.22 plus the applicable C.30 architecture-structure pattern.
  sourceOrUseBoundaryRef?: the exact C.30 architecture claim supplying this expected recovery-timing assertion.
  claimOrWorkScopeRef?: exact A.2.6 claim scope for the pump-station operations-service architecture concern during release train R14-R15.
  aspectPredicate: recoveryTiming.
  temporalReference: release train cycle.
  windowOrInterval: two release cycles after the accepted architecture move starts.
  measuredReadingRef?: measurement result for the operations-service conflict indicator, if C.16 measurement is being made.
  directRelationDeclarationRef?: A.3.4 transformation declaration, if that relation is current.
  obtainingRelationOccurrenceRef?: omitted here; the expected reduction is not an obtaining transformation occurrence.
  receivingUseRulePatternCitation: A.3.4 for bounded transformation, C.30 for selected architecture structure, and the evidence/result pattern for an observed effect.
  validityOrCurrentnessCondition?: valid only while the same selected structure, release train, and conflict indicator remain in force.
  refreshOrReopenCondition?: reopen if the conflict indicator worsens, the release train changes, or the selected structure changes before R15 close.
  blockedLocalOverread: this recovery-timing claim does not prove that the architecture move reduced the conflict.
```

#### C.27.TA:5.4 - Work Rhythm

A review practice depends on a two-day response rhythm across several review positions and participants. Keep a responsibility claim separate when the temporal account relies on it.



C.27.TA states the bearer, rhythm or cadence, timing reference and applicable extent. When cross-bearer coordination matters, identify the direct coupling relation and establish its conditions before asserting an obtaining occurrence.

### C.27.TA:6 - Bias-Annotation

Lenses: **Onto**, **Prag**, **Epist**, **Arch**, **Gov**.

Distortions to watch for:

- **unqualified rhythm:** rhythm or cadence appears without its bearer, timing reference or the extent needed to interpret the claim;
- **freshness-as-permission:** currentness is treated as permission, evidence, or gate passage;
- **time-as-transformation:** timing language is treated as the transformation relation;
- **temporal aspect mistaken for dynamics:** a temporal aspect is treated as a state-space or transition-law episteme;
- **temporal aspect mistaken for measurement:** a temporal aspect is treated as a completed measurement construction.

### C.27.TA:7 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C27TA-1` | The result identifies the bearer or claim, temporal property, and reference and extent needed to interpret it. A window is required when the asserted claim depends on that window. A materialized result has claim content in a `C.2.1` episteme. |
| `CC-C27TA-1a` | No generic context value is required. Measurement, effective scheme or scope, selected Structure, source or use boundary, local-use condition, currentness, reopen, coupling, direct relation, PatternID citation, and blocked overread appear only when changing that value could change the claim or receiving action. |
| `CC-C27TA-2` | The aspect label is a predicate or qualifier in claim content, not an identified temporal-aspect object, and the statement distinguishes the positive claim from C.27 adequacy. |
| `CC-C27TA-3` | When present, PatternID citations are ordinary rule locators. Any direct relation uses a separate exact declaration reference and cites an obtaining occurrence only after its own predicate passes. |
| `CC-C27TA-4` | Rhythm or cadence claims identify recurrence or order and its timing basis. Observational claims retain their observation window; general or planned rules retain their applicability. Cross-bearer fields are needed when the receiving use depends on that relation. |
| `CC-C27TA-5` | Currentness or freshness claims add a source-use boundary, currentness, refresh, or reopen condition only when it changes the receiving use. |
| `CC-C27TA-6` | Recovery, stabilization, inertia and effort-over-time claims retain the starting event, timing reference and extent required by their meaning. Further disturbance, measurement, effort, relation and rule fields are conditional on the receiving use. |
| `CC-C27TA-7` | The claim does not infer evidence, permission, value, gate passage, work completion, causal use, or a relation occurrence from a temporal predicate. |
| `CC-C27TA-8` | Measurement construction, dynamics laws, transformations, work, benchmark parity, and source or evidence use stay with their direct patterns; publication occurrence, form, and carrier do not reidentify unchanged claim content. |

### C.27.TA:8 - Common Anti-Patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Cadence without bearer | "Weekly cadence" appears without saying what has the cadence. | Identify the bearer, recurrence and timing reference, with the observation period or applicability needed by the claim. |
| Unqualified currentness | A source is called current without saying as of when or for which use. | Identify the source, relevant reference time or edition and currentness basis; specify a validity period only if one is claimed. |
| Recovery without an adequate temporal claim | "Recovery improved" omits the bearer, starting event or relevant duration. | State those values and the comparison that supports improvement; add measurement or other relation details as needed. |
| Rhythm as value | A rhythm is treated as good by default. | Use the direct value, assurance, quality, or proxy pattern for those separate claims. |
| Timing as transformation | A time window is treated as if it specified the change. | Use `A.3.4` for the transformation relation and C.27.TA for the temporal aspect. |

### C.27.TA:9 - SoTA-Echoing

| Source family | Contribution to C.27.TA | FPF decision |
| --- | --- | --- |
| Control and model-predictive practice | Horizons, constraints, update intervals, and feedback timing are distinct from the controlled object and the control law. | Express temporal aspects as predicates or qualifiers in claim content; use `A.3.3`, evidence, and control-related patterns for models and control claims. |
| David Deutsch and Chiara Marletto, "Constructor theory of time" (`arXiv:2505.08692v3`), version-specific source posture. | A task or transformation specification need not itself specify duration or the internal course of performance; duration and dynamics can be recovered through timer and clock relations among attributes. Reopen this row if a later version changes the task/duration/timer/clock separation used here. | Require C.27.TA temporal aspects to name bearer and temporal reference. Use `A.3.4` for the transformation, `A.3.3` for dynamics episteme, and C.27 for an unresolved temporal-adequacy question that changes the receiving use. |
| Dynamic treatment regimes and policy evaluation | Intervention timing, follow-up interval, policy window, and outcome window must be separated before causal or policy claims are made. | Use C.27.TA for temporal windows; use `C.28` and evidence patterns for causal-use and policy claims. |
| Object-centric process and event-log practice | A scalar throughput or latency can hide multiple bearers, event types, and interaction windows. | Name the exact EntityOfConcern, temporal predicate, and temporal reference before using a rate, cadence, or trajectory across objects. |
| Rhythm and synchronization research | Recurrence, phase relations and coupling distinguish temporal properties; empirical claims also depend on the observation interval. | State the bearer, timing reference and extent appropriate to the claim. Resolve an adequacy or other subject question through C.27 or its direct pattern when that question remains open. |

### C.27.TA:10 - Consequences

- C.27 addresses adequacy and supported use of authored temporal claims.
- A.3.4 identifies the actual transformation; C.27.TA states its temporal aspect.
- A.3.3 stays the dynamics episteme pattern.
- Use the direct patterns for work planning, actual work, source currentness, benchmark parity, and evidence use.
- Users gain one positive temporal-aspect claim before heavier adequacy, dynamics, causal, benchmark, or assurance patterns are needed.

### C.27.TA:11 - Relations

- **Builds on:** `E.24`, `A.6.5`, `A.7`, `C.2.1`.
- **Coordinates with:** `C.27`, `A.3.4`, `A.3.3`, `A.15.2`, `A.15.1`, `C.16`, `C.28`, `G.9`, evidence, source, assurance, refresh, and publication patterns.
- **C.27 consumer boundary:** `C.27` assesses the temporal claim for its receiving use while preserving its bearer, predicate, timing, coupling and currentness conditions. Use an exact episteme or `C.2.1 ClaimAddress` when the receiving relation depends on that identity; an ordinary adequate explanation does not require a separate temporal-aspect record.
- **Used by:** patterns that need a positive temporal-aspect claim without making a temporal-claim adequacy judgement.

### C.27.TA:End
