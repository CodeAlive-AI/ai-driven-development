## C.27.TA - Temporal Aspect: Time Windows, Rhythm, Cadence, and Currentness

> **Type:** Definitional pattern
> **Status:** Stable
> **Normativity:** Normative except where a section is explicitly informative

### C.27.TA:0 - Use This When

Use this pattern when a project needs to name a positive temporal aspect of a governed object, claim, transformation, work plan, evidence relation, architecture move, benchmark, source use, or publication use.

Use it when the working question is:

- which time window, interval, duration, latency, cadence, rhythm, synchronization, currentness, freshness, validity window, recovery timing, stabilization timing, trajectory, effort over time, inertia, or refresh condition matters;
- which bearer has that temporal aspect: system, episteme, work plan, work occurrence, claim, source, benchmark, architecture-selected structure, method description, publication, or project-world object;
- which temporal reference makes the statement reviewable: calendar time, clock time, event order, cycle, sprint, epoch, release train, sampling interval, follow-up interval, or domain-local timing reference;
- whether the temporal aspect is merely named, measured, used in a temporal claim, used in a transformation claim, or used in a work, evidence, or decision relation.

**Primary EntityOfConcern.** The `EntityOfConcern` is a temporal aspect of a governed object or claim. `C.27.TA` introduces no new `U.TemporalAspect` kind; it supplies slot discipline for temporal aspects that fill relations in other patterns.

**E.24 ontic boundary.** C.27.TA follows `E.24` by refusing a new ontic root here. A temporal aspect is identified by its bearer, aspect kind, temporal reference, window or interval, relation to the governed object or claim, and governing use relation. Those slots make the aspect reviewable without claiming that `timeWindow`, `cadence`, `freshness`, `trajectory`, or `recoveryTiming` are standalone `U.*` kinds. If an authored temporal claim uses the aspect as sufficient for action, C.27 carries adequacy; if a transformation, dynamics model, work plan, evidence use, benchmark, or assurance claim is being made, the governing pattern for that use carries it.

**First useful move.** Write a `TemporalAspectStatement`: bearer, aspect kind, bounded context, temporal reference, interval or window, relation to the governed object or claim, and the governing FPF pattern relation that carries the use.

**What goes wrong if missed.** Temporal words become vibe labels. A cadence is named without bearer, a freshness claim has no validity window, a rhythm has no timing reference, a recovery claim has no interval, an architecture trajectory has no changed structure, and a transformation claim smuggles timing into method, mechanism, or evidence.

**What this buys.** A practitioner can name the temporal aspect as a positive subject before deciding whether `C.27`, `A.3.4`, `A.3.3`, `A.15.2`, `A.15.1`, `C.16`, `C.28`, `G.9`, evidence, source, gate, or assurance patterns carry the actual use.

**Not this pattern when.**

- If the question is adequacy or supported use of an authored temporal claim, use `C.27`.
- If the question is bounded transformation under conditions, use `A.3.4`.
- If the question is a state-space and transition-law episteme, use `A.3.3`.
- If the question is work planning or dated work, use `A.15.2` or `A.15.1`.
- If the question is measurement construction, rate construction, scale, score, or metric comparability, use `C.16` and related characterization patterns.
- If the question is causal use of an intervention or policy, use `C.28`.
- If the temporal phrase is ordinary prose and no practical use changes, do not introduce a C.27.TA statement.

### C.27.TA:1 - Problem Frame

C.27 previously carried two different concerns. One concern is temporal-claim adequacy: whether an authored claim about speed, rhythm, rate-change, recovery, or stabilization can carry a named use. The other concern is positive temporal subject matter: windows, duration, cadence, synchronization, freshness, currentness, inertia, effort over time, recovery, stabilization, and trajectory as aspects of objects or claims.

This pattern carries the second concern. It lets FPF say "what temporal aspect is in play?" without immediately opening an adequacy card, a dynamics model, a work plan, a causal-use record, or a transformation statement.

### C.27.TA:2 - Problem

Without C.27.TA:

1. **Cadence and rhythm become decorative words.** A text says "release cadence" or "team rhythm" without naming bearer, interval, timing reference, or use.
2. **Freshness becomes a vague virtue.** A source, benchmark, dashboard, or claim is called current without a validity window or refresh relation.
3. **Recovery and stabilization hide their interval.** A claim says "recover faster" or "stabilize" without saying over which window, after which disturbance, and for which bearer.
4. **Effort and inertia float free.** A text speaks about momentum, residue, stored work, adaptation cost, or resistance without linking it to a temporal window and governed object.
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

A temporal aspect is a time-bearing or order-bearing aspect of a governed object, claim, or relation. It is not automatically a temporal claim, dynamics law, work trace, method, mechanism, gate, evidence relation, or permission.

Typical temporal aspects include:

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

These names are aspect labels inside a statement, not new `U.*` kinds.

#### C.27.TA:4.2 - Temporal Aspect Statement

Use this compact statement when the temporal aspect changes the governing pattern use relation:

```text
TemporalAspectStatement:
  bearerRef:
  bearerGoverningPattern:
  boundedContext:
  aspectKind:
  temporalReference:
  windowOrInterval:
  measuredReadingRef?:
  relationToGovernedObjectOrClaim:
  governingUseRelationRef:
  validityOrCurrentnessCondition?:
  refreshOrReopenCondition?:
  blockedLocalOverread:
```

`bearerRef` names the object or claim that has the temporal aspect. `temporalReference` states the clock, event order, cycle, sprint, epoch, release train, sampling interval, follow-up interval, or domain-local timing reference. `blockedLocalOverread` names one local overread blocked by this aspect statement: for example, "this cadence statement does not prove recovery", "this freshness window does not create permission", or "this rhythm statement is not yet a C.27 adequacy card".

#### C.27.TA:4.3 - Governing Use Relation

| Temporal use | Governing pattern |
| --- | --- |
| positive temporal aspect of an object or claim | `C.27.TA` |
| adequacy or supported use of an authored temporal claim | `C.27` |
| bounded transformation under conditions with temporal reference | `A.3.4` plus `C.27.TA` |
| state-space or transition-law model | `A.3.3` |
| planned work timing | `A.15.2` |
| dated work occurrence or trace | `A.15.1` |
| measurement construction for rate, duration, latency, or freshness | `C.16` and related characterization patterns |
| causal-use timing, intervention window, comparator, or follow-up interval | `C.28` |
| benchmark freshness, baseline window, comparator edition, or parity window | `G.9` |
| source currentness, evidence decay, provenance, or assurance refresh | evidence, source, provenance, assurance, and refresh patterns |

#### C.27.TA:4.4 - Rhythm, Cadence, And Synchronization

Rhythm and cadence require bearer, timing reference, and window. Coupling, phase, synchronization, entrainment, dependency, or coordination wording appears only when the claim depends on a cross-bearer temporal relation.

Compact rhythm statement:

```text
RhythmAspect:
  rhythmBearerRef:
  timingReference:
  rhythmWindowRef:
  intervalStructure:
  governingUseRelationRef:
  couplingRelation?:
  validityWindowRef?:
```

A plain "release cadence" or "workshop rhythm" may remain ordinary prose. It needs C.27.TA when cadence or rhythm changes transformation, work planning, benchmark, source, assurance, coordination, or claim-use decisions.

#### C.27.TA:4.5 - Currentness, Freshness, And Validity Window

Currentness and freshness need a reference time and a validity window. A source, benchmark, model, dashboard, or claim may be fresh enough for one use and stale for another.

Use C.27.TA to name:

- what object or claim is current;
- relative to which reference time or edition;
- for which window or use;
- which refresh or reopen condition changes the temporal aspect.

Use source, evidence, benchmark, assurance, or refresh patterns for the actual evidence, provenance, parity, assurance, or refresh work.

#### C.27.TA:4.6 - Recovery, Stabilization, Inertia, And Effort Over Time

Recovery, stabilization, inertia, and effort over time are temporal aspects when they name timing, interval, persistence, residue, or reversal cost for a governed object. They become C.27 temporal-claim adequacy only when an authored claim uses them to carry a practical use.

Use C.27.TA to name:

- disturbance or starting condition;
- bearer;
- recovery or stabilization window;
- effort, resistance, residue, or inertia relation;
- governing pattern relation that carries transformation, work, evidence, value, or assurance.

### C.27.TA:5 - Archetypal Grounding

#### C.27.TA:5.1 - Release Cadence

A platform team says its release cadence changed from monthly to weekly.

C.27.TA names the bearer, release-train timing reference, window, interval structure, and governing use relation. It does not by itself say that the change is good, that quality improved, that work happened, or that a promised service level was met.

#### C.27.TA:5.2 - Source Freshness

A benchmark comparison uses a model report from April and a competitor report from June.

C.27.TA names the source-currentness and validity windows. `G.9`, source-use, evidence, and benchmark patterns carry comparator parity, provenance, and evidence use.

#### C.27.TA:5.3 - Architecture Recovery Timing

An architecture move is expected to reduce an interlevel conflict after two release cycles.

C.27.TA names the recovery window, cycle reference, bearer, and trajectory. `A.3.4` names the structure transformation; architecture patterns govern the selected structure and characteristic; evidence and result patterns govern observed effects.

```text
TemporalAspectStatement:
  bearerRef: ArchitectureOf@PlantOperationsService selected interlevel conflict.
  bearerGoverningPattern: C.30 plus the selected architecture-structure pattern.
  boundedContext: pump-station operations-service architecture move during release train R14-R15.
  aspectKind: recoveryTiming.
  temporalReference: release train cycle.
  windowOrInterval: two release cycles after the accepted architecture move starts.
  measuredReadingRef?: operations-service conflict indicator, if C.16 measurement is being made.
  relationToGovernedObjectOrClaim: temporal aspect of the expected conflict-reduction transformation; not the transformation relation itself.
  governingUseRelationRef: A.3.4 for bounded transformation, C.30 for selected architecture structure, evidence/result pattern for observed effect.
  validityOrCurrentnessCondition?: valid only while the same selected structure, release train, and conflict indicator remain in force.
  refreshOrReopenCondition?: reopen if the conflict indicator worsens, the release train changes, or the selected structure changes before R15 close.
  blockedLocalOverread: this recovery-timing statement does not prove that the architecture move reduced the conflict.
```

#### C.27.TA:5.4 - Work Rhythm

A review practice depends on a two-day response rhythm across several roles.

C.27.TA names the rhythm bearer, timing reference, rhythm window, and coupling relation when cross-bearer coordination matters. Work planning, role assignment, and method-description patterns carry their own claims.

### C.27.TA:6 - Bias-Annotation

Lenses tested: **Onto**, **Prag**, **Epist**, **Arch**, **Gov**.

Resisted distortions:

- **rhythm-as-vibe:** rhythm or cadence appears without bearer, timing reference, and window;
- **freshness-as-permission:** currentness is treated as permission, evidence, or gate passage;
- **time-as-transformation:** timing language is treated as the transformation relation;
- **dynamics theft:** a temporal aspect is treated as a state-space or transition-law episteme;
- **measurement theft:** a temporal aspect is treated as a completed measurement construction.

### C.27.TA:7 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C27TA-1` | The temporal aspect statement names bearer, governing pattern, bounded context, aspect kind, temporal reference, and window or interval. |
| `CC-C27TA-2` | The statement distinguishes positive temporal aspect from temporal-claim adequacy. |
| `CC-C27TA-3` | Rhythm or cadence statements name bearer, timing reference, and window; cross-bearer terms appear only with a named relation. |
| `CC-C27TA-4` | Currentness or freshness statements name reference time, validity window, and refresh or reopen condition when one changes the use. |
| `CC-C27TA-5` | Recovery, stabilization, inertia, and effort-over-time statements name bearer, interval, and governing use relation. |
| `CC-C27TA-6` | The statement does not infer evidence, permission, value, gate passage, work completion, or causal use from a temporal aspect. |
| `CC-C27TA-7` | Measurement construction, dynamics laws, transformations, work, benchmark parity, and source or evidence use stay with their governing patterns. |

### C.27.TA:8 - Common Anti-Patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Cadence without bearer | "Weekly cadence" appears without saying what has the cadence. | Name bearer, timing reference, interval, and governing use relation. |
| Freshness without window | A source is called current without reference time or validity window. | Write currentness/freshness with reference time, validity window, and refresh condition. |
| Recovery without disturbance | A claim says "recovery improved" without starting condition or interval. | Name disturbance, bearer, recovery window, and governing use. |
| Rhythm as value | A rhythm is treated as good by default. | Keep value, assurance, quality, or proxy claims with their governing patterns. |
| Timing as transformation | A time window is treated as if it specified the change. | Use `A.3.4` for the transformation relation and C.27.TA for the temporal aspect. |

### C.27.TA:9 - SoTA-Echoing

| Source family | Current lesson for C.27.TA | FPF decision |
| --- | --- | --- |
| Control and model-predictive practice | Horizons, constraints, update intervals, and feedback timing are distinct from the controlled object and the control law. | Treat temporal aspects as named slots; use `A.3.3`, evidence, and control-related patterns for models and control claims. |
| David Deutsch and Chiara Marletto, "Constructor theory of time" (`arXiv:2505.08692v3`), version-specific source posture. | A task or transformation specification need not itself specify duration or the internal course of performance; duration and dynamics can be recovered through timer and clock relations among attributes. Reopen this row if a later version changes the task/duration/timer/clock separation used here. | Require C.27.TA temporal aspects to name bearer and temporal reference. Use `A.3.4` for the transformation, `A.3.3` for dynamics episteme, and C.27 only when an authored temporal claim uses the aspect for a practical use. |
| Dynamic treatment regimes and policy evaluation | Intervention timing, follow-up interval, policy window, and outcome window must be separated before causal or policy claims are made. | Use C.27.TA for temporal windows; use `C.28` and evidence patterns for causal-use and policy claims. |
| Object-centric process and event-log practice | A scalar throughput or latency can hide multiple bearers, event types, and interaction windows. | Name temporal bearer and temporal reference before using a rate, cadence, or trajectory across objects. |
| Rhythm and synchronization research | Rhythm requires bearer, timing reference, interval structure, and coupling only when cross-bearer coordination matters. | Keep rhythm/cadence as temporal aspects; use C.27 temporal-claim adequacy or another governing pattern only for the use that pattern carries. |

### C.27.TA:10 - Consequences

- C.27 can be narrowed to adequacy and supported use of authored temporal claims.
- A.3.4 gains a clean temporal reference slot without carrying the whole temporal ontology.
- A.3.3 stays the dynamics episteme pattern.
- Work planning, actual work, source currentness, benchmark parity, and evidence use keep their own governing patterns.
- Users gain a small positive statement for temporal aspects before heavier adequacy, dynamics, causal, benchmark, or assurance patterns are needed.

### C.27.TA:11 - Relations

- **Builds on:** `E.24`, `A.6.5`, `A.7`, `C.2.1`.
- **Coordinates with:** `C.27`, `A.3.4`, `A.3.3`, `A.15.2`, `A.15.1`, `C.16`, `C.28`, `G.9`, evidence, source, assurance, refresh, and publication patterns.
- **Used by:** patterns that need a positive temporal aspect without making a temporal-claim adequacy judgement.

### C.27.TA:End

