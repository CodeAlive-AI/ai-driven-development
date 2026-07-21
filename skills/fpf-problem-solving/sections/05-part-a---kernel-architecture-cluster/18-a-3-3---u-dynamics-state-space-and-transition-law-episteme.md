## A.3.3 - U.Dynamics: State-Space and Transition-Law Episteme

> **Type:** Definitional pattern
> **Status:** Stable
> **Normativity:** Normative

### A.3.3:1 - Problem frame

Use this pattern when a project needs one reusable model of **how state changes** in a bounded context: a state space, a transition law, an observation relation, and the conditions under which prediction, simulation, calibration, conformance, drift, or gating claims are warranted.

Use it when the working question is:

* which holon, episteme, system-in-role, claim, service, resource bundle, architecture, or other EntityOfConcern has changing state;
* which characteristics define the state space;
* which transition law states how those coordinates evolve;
* which observations or work-derived traces can be compared with the law;
* whether a prediction can be used for comparison, gating, assurance, planning, or control.

**Primary EntityOfConcern.** The `EntityOfConcern` is `U.Dynamics`: an `U.Episteme` that specifies a state space and a state-transition law for one or more EntitiesOfConcern in a bounded context.

**E.24.UK settlement.** `U.Dynamics` is retained as a dependent durable U-kind under the `U.Episteme` settlement. Its durable value is the reusable state-space and transition-law episteme for changing state in a bounded context. It is not a root change kind, not the changed EntityOfConcern, not a work occurrence, and not a flow structure; components such as `stateSpace`, `transitionLaw`, `observationRelation`, and `calibrationOrParameterSource` remain slots or claim graphs inside the dynamics episteme unless another governing pattern makes one of them separately addressable.

**First useful move.** Name the changing EntityOfConcern, the bounded context, the state-space characteristics, the transition law, the observation relation, and the applicability window. If these cannot be named, the current claim is not yet ready for prediction, conformance, or gate use.

**What goes wrong if missed.** Procedure text becomes "the dynamics", telemetry becomes a law, one observed run becomes a prediction, a dashboard becomes a state space, or a simulation becomes permission to act.

**What this buys in practice.** Practitioners can compare predictions with traces, decide whether stale predictions may still be used, separate methods from laws of change, and decide where mathematical-lens, temporal, evidence, assurance, or gate patterns must take over.

**Not this pattern when.** If the source only states a semantic way of doing, use `A.3.1`. If it states an episteme describing that way, use `A.3.2`. If it states bounded transformation under conditions, use `A.3.4`. If it states planned work or dated work, use `A.15.2` or `A.15.1`. If it states a mechanism algebra, use `A.6.1` and `E.20`. If it states only freshness, rhythm, inertia, delay, window, or currentness as a positive temporal aspect, use `C.27.TA`; if it states adequacy or supported use of an authored temporal claim, use `C.27`. If it states only evidence or assurance, use `A.10` or `B.3`.

### A.3.3:2 - Problem

Without a first-class `U.Dynamics`, state-change claims collapse into nearby but different claims:

1. **Recipe becomes law.** Teams put procedure text, a control diagram, a workflow diagram, or a method description where a state-transition law should be.
2. **Trace becomes law.** Dated work logs, telemetry, and incident sequences are treated as if past events defined what must happen.
3. **Dashboard becomes state space.** Metric lists appear without characteristics, units, scales, topology, geometry, invariants, or operating region.
4. **Prediction becomes authority.** A model output is used for a gate, release, safety, or work decision without freshness, non-expansiveness, commutation, observation, or assurance conditions.
5. **Domain vocabulary blocks transfer.** Physics, control, finance, reliability, operations, knowledge dynamics, and architecture all talk about change differently; FPF needs one kernel pattern that preserves their differences without inventing separate ontologies.

### A.3.3:3 - Forces

| Force | Tension |
| --- | --- |
| Universality and domain richness | One kernel pattern must cover ODEs, PDEs, Markov kernels, queues, discrete events, Bayesian updates, enterprise characteristic evolution, and architecture-quality change without flattening the domain-specific model. |
| Model and world | `U.Dynamics` is an episteme, while evidence comes from dated work, telemetry, observation, and source relations. |
| Continuous, discrete, stochastic, and hybrid forms | Time references, update rules, likelihood models, and disturbances differ; the state-space and transition-law declaration must keep them explicit. |
| Prediction and intervention | A law can inform planning, diagnosis, simulation, model-predictive control, or assurance, but it does not itself assign work authority or responsibility. |
| Mathematical power and transfer risk | Mathematical form can make prediction precise, but transfer across domains, scales, or representations needs `C.29` and sometimes `A.6.0`. |
| Freshness and gate pressure | Predictions are attractive when observation is slow or expensive; gate use still needs stated currentness and applicability conditions. |

### A.3.3:4 - Solution

#### A.3.3:4.1 - Definition

Within a `U.BoundedContext`, `U.Dynamics` is an `U.Episteme` that specifies a **state space** and a **state-transition law** for one or more EntitiesOfConcern, possibly under exogenous inputs, constraints, and observation relations.

`U.Dynamics` can be deterministic or stochastic, continuous, discrete, or hybrid. It can describe physical systems, software services, organizations, episteme states, claim states, resource states, architecture characteristics, or other holons whose state change is being modeled.

It does not prescribe what an agent should do. A semantic way of doing belongs to `U.Method`; an episteme describing that way belongs to `U.MethodDescription`; a dated occurrence belongs to `U.Work`; a planned occurrence belongs to `U.WorkPlan`; a mechanism law belongs to `U.Mechanism`; evidence and assurance claims belong to their own governing patterns.

#### A.3.3:4.2 - Dynamics statement

Use this compact statement when applying the pattern:

```text
Dynamics statement:
  EntityOfConcern:
  BoundedContext:
  StateSpace:
  TransitionLaw:
  TimeReference:
  Stochasticity:
  InputsOrDisturbances:
  ObservationRelation:
  ConstraintsOrInvariants:
  ApplicabilityWindow:
  CalibrationOrParameterSource:
  PredictionUse:
  EvidenceRelation:
  StopCondition:
```

This statement is not an instruction sequence. It is the smallest episteme-facing record needed to keep the law of change separate from methods, work, evidence, and authority.

#### A.3.3:4.3 - Working distinction table

| Current claim | Governing pattern |
| --- | --- |
| state space and transition law for changing state | `A.3.3 U.Dynamics` |
| semantic way of doing | `A.3.1 U.Method` |
| text, code, diagram, model, proof script, or protocol describing a method | `A.3.2 U.MethodDescription` |
| planned dated work | `A.15.2 U.WorkPlan` |
| dated work occurrence and actuals | `A.15.1 U.Work` |
| mechanism algebra, admissible operation, or law-governed application over a subject kind | `A.6.1 U.Mechanism` and `E.20` |
| formal object, invariant, postulate set, or mathematical substrate | `A.6.0`, `C.29`, or the direct mathematical pattern |
| observation, trace, conformance result, source, or provenance used as evidence | `A.10` and direct evidence-related patterns |
| assurance case, trust calculus, or safety argument | `B.3` or the direct assurance pattern |
| gate passage, release, authority, or permission to act | `A.20`, `A.21`, or the direct gate or authority pattern |
| bounded transformation under conditions | `A.3.4 U.Transformation` |
| freshness, delay, rhythm, currentness, inertia, cadence, or validity window as a positive temporal aspect | `C.27.TA` |
| adequacy or supported use of an authored temporal claim | `C.27` |

#### A.3.3:4.4 - State-space and transition-law fields

```text
U.Dynamics {
  context: U.BoundedContext
  entityOfConcern: EntityOfConcern
  stateSpace: state-space declaration over FPF characteristics
  transitionLaw: claim graph inside U.Dynamics
  timeReference: continuous | discrete | hybrid
  stochasticity: deterministic | stochastic
  inputsOrDisturbances?: CharacteristicSet
  observationRelation?: claim graph or relation reference inside U.Dynamics
  constraintsOrInvariants?: claim graph inside U.Dynamics
  applicabilityWindow?: ConditionSet
  calibrationOrParameterSource?: source or calibration episteme reference
}
```

`stateSpace` is the state-space declaration of this `U.Dynamics` episteme. It uses FPF characteristics with units, scales, and comparability rules, and may cite `A.19` or `C.16` when characteristic or measurement construction is being made. It is not the same object as a receiving-evaluation `CharacteristicSpace` used to score an object for improvement. The dynamics state space may include topology, geometry, aggregation policy, or coordinate transformations when trajectories or comparisons need them.

`transitionLaw` is paradigm-agnostic. It can be an equation, relation, kernel, finite-state transition, queueing model, Bayesian update, Petri-net firing relation, simulation rule, learned predictor, or hybrid model, provided the state space and applicability window are declared.

`transitionLaw`, `observationRelation`, `constraintsOrInvariants`, and `calibrationOrParameterSource` are components or claim graphs inside the `U.Dynamics` episteme unless another governing pattern makes one of them a separately addressable episteme, source, or relation value. Naming one component does not split `U.Dynamics` into several unrelated epistemes.

`observationRelation` separates state from what can be measured, sampled, logged, estimated, or inferred. Identity observation is allowed only when the context says the state coordinate is directly observed.

#### A.3.3:4.5 - Evidence, prediction, conformance, drift, and calibration

Let `D` be a `U.Dynamics` in context `C`, and let `W` be dated `U.Work` records or observation records produced under `C`.

| Derived value | Meaning |
| --- | --- |
| `trace(W, D)` | ordered observed values produced by applying `D.observationRelation` to work records, telemetry, source records, or measurements |
| `initialState(W, D)` | stated, measured, or estimated state at trace start |
| `predict(D, initialState, inputs, horizon)` | trajectory or distribution generated by the transition law over the declared horizon |
| `insideOperatingRegion(D, state)` | check against constraints, invariants, and applicability window |
| `residuals(D, trace)` | discrepancies between predicted and observed values under a stated alignment |
| `fits(D, trace, tolerancePolicy)` | conformance verdict under a declared tolerance, likelihood, interval, or distributional policy |
| `drift(D1, D2, domain)` | divergence between two dynamics versions over a declared operating domain |

Calibration outcomes produce a new or updated dynamics episteme. They do not turn the old law into a dated work record and do not make the new law authoritative for gates without the gate pattern.

#### A.3.3:4.6 - Prediction use in comparison or gating

When predicted coordinates from `U.Dynamics` are used for comparison, release, gate, assurance, or work-preparation use, one of these conditions must hold:

1. a fresh observation is available for the gate or comparison window; or
2. the applied transition map `Phi_dt` is declared non-expansive under the declared distance structure, and the transition commutes with the invariantization or quotient step on the domain of use.

If neither condition is satisfied, prediction does not carry the gate or comparison claim. Use observation, state currentness through `C.27.TA`, use `C.27` when authored temporal-claim adequacy is the concern, or move the gate claim to `A.20`, `A.21`, or the direct authority pattern.

Every use of `Phi_dt` states its applicability window: operating region, horizon, scale band, time step, parameter regime, and source-currentness condition.

#### A.3.3:4.7 - A.3.4, C.27.TA, C.27, and C.29 boundaries

`A.3.4` governs bounded transformation under conditions. A dynamics episteme can model, predict, simulate, or constrain a transformation, but it is not the transformation itself.

`C.27.TA` names positive temporal aspects: freshness, delay, rhythm, currentness, inertia, cadence, trajectory, recovery timing, stabilization timing, and validity window. `C.27` judges adequacy or supported use of authored temporal claims that use those aspects. A `Dyn2TemporalClaimAdequacyCard` or temporal classification is not itself a law of change.

Stay in `A.3.3` when `transitionLaw` or `observationRelation` uses accepted local dynamics, Markov kernels, ODEs, simulations, queueing theory, control theory, or domain theory inside one context.

Use `C.29` when the law depends on contested transfer, cross-domain analogy, learned or speculative mathematical lens, scale change, abstraction, quotienting, or reusable explanation across contexts. The `C.29` output states preserved structure, lost structure, operating-region or scale window, rival lens when current, lens-use boundary value, and stop condition. `A.3.3` remains the governing pattern for state space, transition law, observation, constraints, and calibration semantics.

#### A.3.3:4.8 - Method, mechanism, and governing-pattern constellation boundary

A source label such as `process`, `algorithm`, `dynamics`, `workflow`, `model`, `controller`, or `simulator` may point to linked slot positions under `E.10.ARCH`, not to one typed value. Recover the relevant slots first, then split the linked values:

* `U.Method` for the semantic way of doing;
* `U.MethodDescription` for the representation describing that way;
* `U.Dynamics` for the state-space and transition-law episteme;
* `U.Mechanism` for an admissible operation or law-governed application over a subject kind;
* `U.WorkPlan` and `U.Work` for planned and dated occurrences;
* `TransformationFlowStructure` for selected flow structure when the source is describing a flow-shaped arrangement of transformations;
* evidence, gate, authority, and assurance values when those claims are current.

The linkage among relation positions does not become a process, method, mechanism, dynamics model, plan, work occurrence, or evidence object. Assign one typed value as both `U.Method` and `U.Dynamics` only when a governing pattern explicitly admits that dual typing for the current claim.

### A.3.3:5 - Archetypal Grounding

#### A.3.3:5.1 - Reactor control

A reactor team models temperature and concentration under a nonlinear ODE with disturbances. The ODE, state space, observation relation, and operating region are `U.Dynamics`. The control policy is `U.Method`; the controller code is `U.MethodDescription` when it describes the method, and dated controller runs or mechanism claims stay with their governing patterns. Thermocouple readings become evidence only through `A.10` or the direct evidence pattern.

Side-by-side split:

| Filled question | `U.Dynamics` value | `U.Transformation` value |
| --- | --- | --- |
| EntityOfConcern | reactor temperature and concentration state in bounded operating context | catalyst-bed condition changed from fouled to regenerated during one maintenance intervention |
| Core relation | state-space coordinates plus nonlinear transition-law claim graph, observation relation, disturbances, operating region, and applicability window | transformed entity, bounded maintenance context, pre-state, post-state or delta, transformation relation, and boundary condition |
| Use | prediction, simulation, conformance, drift, and gate input only when freshness or mathematical conditions are satisfied | bounded change statement about what changed under conditions; it may cite a dynamics model but is not the model |
| Kept outside | method, controller code, dated runs, evidence, and gate authority | reusable law of state change, method description, work occurrence, evidence relation, and permission to act |

#### A.3.3:5.2 - Reliability and operations

A service platform models backlog, arrival rate, and incident recovery with a queueing or birth-death model. The model can predict whether an SLO is feasible, but the service promise remains `U.PromiseContent`, and release or gate use needs the gate pattern.

#### A.3.3:5.3 - Evolutionary architecture

An architecture group tracks latency, coupling, operational cost, and change lead time across releases. A discrete-time transition map over those characteristics can be `U.Dynamics`. Architecture moves, selected structures, and views stay with architecture patterns; work occurrences and measurements stay with work and evidence patterns.

#### A.3.3:5.4 - Knowledge dynamics

A claim portfolio uses belief, evidence weight, source currentness, and contestability as state coordinates. A Bayesian or likelihood update is a dynamics episteme over claim state. The studies, reviews, and source records are evidence values; the dynamics model does not make a claim true by itself.

#### A.3.3:5.5 - Natural physical evolution

The Moon orbiting Earth can be modeled as `U.Dynamics` without pretending that the Moon enacts a method or performs governed work. A role assignment such as satellite classification may be well-formed, but it does not create method-work alignment.

### A.3.3:6 - Bias-Annotation

Typical biases:

* **recipe-as-law bias**: procedure text or controller code is treated as the law of change;
* **trace-as-law bias**: logs or one observed run are treated as reusable dynamics;
* **dashboard-as-state-space bias**: visible metrics substitute for declared characteristics, units, scales, and comparability relations;
* **prediction-as-authority bias**: model output is treated as permission, gate passage, or safety proof;
* **mathematical-prestige bias**: equations, learned predictors, and simulations are accepted without applicability window, observation relation, and transfer boundary;
* **semio-bias**: the pattern drifts into arguments about descriptions of dynamics while losing the state-space and transition-law EntityOfConcern.

### A.3.3:7 - Conformance Checklist

**CC-A3.3-1 (Type).** `U.Dynamics` is an `U.Episteme` for a state-space and transition-law claim. It is not `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work`, `U.Mechanism`, evidence, assurance, or gate authority.

**CC-A3.3-2 (Bounded context).** Every `U.Dynamics` is declared inside a `U.BoundedContext`. Units, characteristic names, operating region, time base, approximation regime, and source-currentness condition are local to that context.

**CC-A3.3-3 (EntityOfConcern).** The changing EntityOfConcern is named. It may be a physical holon, service, organization, episteme, claim portfolio, architecture, resource bundle, or other holon with modeled state.

**CC-A3.3-4 (State space).** The state space enumerates characteristics with units, scales, comparability rules, and any needed topology, geometry, aggregation policy, or invariantization rule.

**CC-A3.3-5 (Transition law).** The transition law states a relation, map, kernel, equation, rule, learned predictor, or simulation rule suitable for the declared time base and stochasticity.

**CC-A3.3-6 (Observation relation).** Evidence use states how work records, telemetry, measurements, or source records become observed coordinates. Direct observation is declared rather than assumed.

**CC-A3.3-7 (Constraints and applicability).** Constraints, invariants, operating region, approximation regime, parameter range, horizon, and scale window are stated before prediction or gate use.

**CC-A3.3-8 (No imperative overread).** `U.Dynamics` does not prescribe agent steps, responsibilities, or ordered work occurrences. Planning or control methods that use dynamics belong to `U.Method` and `U.MethodDescription`.

**CC-A3.3-9 (No actuals on dynamics).** Resource actuals, timestamps, work logs, and telemetry attach to work, evidence, or source values. Calibration creates a new or revised dynamics episteme.

**CC-A3.3-10 (Prediction use).** Predicted coordinates used for comparison or gating require fresh observation or a declared non-expansive, invariant-commuting transition map over the domain of use.

**CC-A3.3-11 (Temporal boundary).** Positive temporal aspects stay with `C.27.TA`; temporal-claim adequacy, freshness-use, delay-use, rhythm-use, inertia-use, and currentness-use claims stay with `C.27`; reusable transition laws stay with `A.3.3`.

**CC-A3.3-12 (C.29 boundary).** Contested, cross-domain, learned, speculative, scale-changing, or transferable mathematical-lens use is assigned to `C.29`; `A.3.3` keeps the dynamics semantics.

**CC-A3.3-13 (Source-label repair).** `Process`, `workflow`, `algorithm`, `model`, `controller`, `simulator`, and `dynamics` wording must not be repaired to `U.Dynamics` until the current slot is recovered: method, method description, work plan, dated work, selected transformation-flow structure, transition-law claim graph, evidence relation, or another governed value.

### A.3.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| "The procedure is the dynamics." | Put the semantic way of doing in `U.Method`, the procedure text in `U.MethodDescription`, and the law of state change in `U.Dynamics`. |
| "Telemetry is the dynamics." | Treat telemetry as evidence or source material; derive `trace(W, D)` and compare it with the declared law. |
| "The dashboard is our state space." | Recover characteristics, units, scales, comparability relations, operating region, and invariants. |
| "The simulation approved the release." | Keep simulation as prediction; use `A.20`, `A.21`, `A.10`, or `B.3` for gate, evidence, and assurance claims. |
| "The model works everywhere." | State the applicability window and lowering condition; use `C.27.TA` for currentness and `C.29` for transfer. |
| "A workflow diagram proves the dynamics." | Recover whether the diagram describes a method, method description, work plan, dated work occurrence, selected transformation-flow structure, evidence relation, mechanism, or transition-law claim graph. |
| "A learned predictor is the law." | State training domain, observation relation, uncertainty, error policy, and applicability window before using prediction. |

### A.3.3:9 - Consequences

| Benefit | Cost or caution |
| --- | --- |
| Prediction, simulation, conformance, drift, and calibration claims become reviewable. | The project must name state-space characteristics and observation relations rather than relying on dashboard labels. |
| Methods, method descriptions, mechanisms, work, flow structures, and dynamics stop substituting for each other. | Source labels like `process`, `workflow`, and `model` often need `E.10.ARCH` recovery before typed assignment. |
| Gate and release use becomes safer because prediction needs freshness or a stated mathematical condition. | Some attractive predictions become inadmissible until observation or proof is supplied. |
| Dynamics can cover physical, organizational, epistemic, software, architectural, and resource examples under one FPF kind. | Domain-specific laws still need their own notation, assumptions, and evidence disciplines. |
| Mathematical-lens transfer is visible rather than hidden inside equations. | `C.29` may be needed when the dynamics model crosses contexts, scales, or representation regimes. |

#### A.3.3:9.1 - Quick use cards

* **Dynamics predicts.** It is a state-space and transition-law episteme.
* **Work reveals.** Measurements, logs, and actuals belong to work, evidence, or source values.
* **Method guides.** A method may use dynamics, but dynamics is not the method.
* **State space first.** No state-space characteristics, no reviewable dynamics claim.
* **Observation matters.** A law without observation relation cannot be compared with traces.
* **Prediction is not authority.** Gate and release claims need their governing patterns.

### A.3.3:10 - Rationale

FPF needs `U.Dynamics` because many practical questions are not about what an agent should do, but about how a state changes when the world evolves, a model is simulated, evidence arrives, a resource pool fluctuates, or an architecture changes. Those questions need a law of change, not a procedure, not a work log, and not a promise.

The pattern is deliberately broad because state-change reasoning appears in physics, control, software operations, reliability, strategy, architecture, and knowledge work. The shared kernel is not a universal notation. It is the distinction between state-space, transition law, observation relation, applicability window, and related governed claim families such as method, work, transformation, evidence, assurance, and gate use.

### A.3.3:11 - SoTA-Echoing

| Source line | Source refs | Adopt, adapt, or reject | Effect in this pattern |
| --- | --- | --- | --- |
| Current constructor-theory and process-theory work | Gogioso, Wang-Mascianica, Waseem, Scandolo, and Coecke, "Constructor Theory as Process Theory", EPTCS 397, 2023, arXiv:2401.05364; Deutsch and Marletto, "Constructor theory of time", arXiv:2505.08692v3, revised 2026-06-05. | Adapt: dynamics, transformations, tasks, and processes are kept close without collapsing law, method, mechanism, and work. | `U.Dynamics` is a law-of-change episteme; transformation claims stay with `A.3.4`, and method/work claims stay in their governing patterns. |
| Current data-driven predictive-control work | de Jong, Breschi, Schoukens, and Lazar, "Koopman Data-Driven Predictive Control with Robust Stability and Recursive Feasibility Guarantees", arXiv:2405.01292; Shang, Cortes, and Zheng, "On the Exponential Stability of Koopman Model Predictive Control", arXiv:2511.02008. | Adopt: prediction, lifted state, stability, recursive feasibility, and prediction error need explicit state-space, model, horizon, and constraint declarations. | `stateSpace`, `transitionLaw`, `applicabilityWindow`, `constraintsOrInvariants`, and prediction-use conditions are mandatory before comparison or gate use. |
| Current stochastic predictive-control work | Knaup and Tsiotras, "Recursively Feasible Stochastic Model Predictive Control for Time-Varying Linear Systems Subject to Unbounded Disturbances", arXiv:2410.11107. | Adopt: stochasticity, unbounded disturbances, time variation, feasibility, and chance constraints must not be hidden behind one model label. | `stochasticity`, `inputsOrDisturbances`, tolerance policy, and applicability window are explicit fields. |
| Current digital-twin validation pressure | Russell Bernal, Petterson, Alarcon Granadeno, Murphy, Mason, and Cleland-Huang, "Validating Terrain Models in Digital Twins for Trustworthy sUAS Operations", arXiv:2508.16104. | Adapt: model validation depends on operational context, observation limits, granularity, uncertainty, and real-world use conditions. | Observation relation, evidence relation, operating region, and source-currentness condition remain separate from the dynamics law. |
| Historical state-space, declarative, and imperative contrasts | Classical state-space control, early declarative programming, workflow slogans, and process-model slogans. | Reject as current SoTA by themselves; retain only as lineage and recognition cues. | The pattern repairs by FPF kind, state-space declaration, and slot relation rather than by programming-paradigm or process-slogan labels. |

Lower current use of this pattern when current work on process theory, predictive control, hybrid systems, stochastic dynamics, digital twins, causal dynamics, learned world models, graph representations, equivalence representations, or FPF's own characteristic-space, temporal, mathematical-lens, transformation, work, evidence, and gate patterns changes the governing distinction.

### A.3.3:12 - Relations

* **Builds on:** `A.1.1 U.BoundedContext`; `A.19 CharacteristicSpace`; episteme machinery for description, source, and publication when those claims are current.
* **Coordinates with:** `A.3.1 U.Method`; `A.3.2 U.MethodDescription`; `A.3.4 U.Transformation`; `A.15.2 U.WorkPlan`; `A.15.1 U.Work`; `A.6.1 U.Mechanism`; `E.20`; `C.27.TA`; `C.27`; `C.29`; `A.10`; `B.3`; `A.20`; `A.21`; architecture patterns when dynamics describes architecture-characteristic change.
* **Separates from:** services and promise content; PBS and SBS structural breakdowns; causal-use claims; gate authority; assurance arguments; publication-use claims.
* **Uses for precision restoration:** `E.10`, `E.10.ARCH`, `F.18`, and `C.2.P.DR` when source labels hide whether the claim is law, method, method description, mechanism, work, evidence, authority, or dynamics.

### A.3.3:End

