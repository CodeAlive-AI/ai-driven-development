## C.26.3 - Viability-Envelope Boundary Regulation

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.26.3:1 - Problem frame

Use this pattern when architecture work is maintaining, recovering, or changing viable operating ranges across boundaries. The working problem is not "optimize one metric"; it is "keep a bundle of characteristics inside a viable region while disturbances, probes, actuators, boundary conditions, and operating regimes change."

**What goes wrong if missed.** The team treats one dashboard value, stability slogan, or local metric as viability, while another envelope variable, actuator cost, boundary condition, or failure mode is already breaking the protected promise or function.

**What this buys.** The viability claim becomes an inspectable envelope-regulation decision: bearer, protected promise or function, variables, disturbances, sensors or probes, actuators, boundary condition, adaptation cost, and failure mode are all named before acting.

Most envelope work covered by this pattern is ordinary control, quality, SRE, causal, or work discipline, not QL. FEP, allostasis, and active inference are source analogies for envelope discipline, sensor and action coupling, and partial observability; ordinary control, SRE, quality-bundle, causal, and work patterns remain primary unless probe, order, export, or coarsening cue remains load-bearing after ordinary viability, quality, dynamics, measurement, boundary, and work patterns have carried their part.

| Working card | Value |
| --- | --- |
| Primary reader | Architect, platform lead, reliability lead, product manager, or operations lead preserving viability under changing conditions. |
| Primary EntityOfConcern | A viability-envelope claim or plan over a declared viability bearer, with protected promise/function named separately. |
| Admissible move | Name the bearer, envelope variables, disturbance, sensors/probes, actuators, boundary condition, adaptation cost, and failure mode. |
| Outside work | One-metric quality tuning, generic control theory, biological proof, full FEP doctrine, and ordinary feedback without an envelope/boundary claim. |
| What changes in practice | The team stops treating one dashboard value as viability and designs the actual envelope-regulation move. |

Plain glosses:
- `viability bearer`: the `U.System`, collective system, delivery system, role configuration, organism-as-system, or explicitly modelled market slice whose viable range is being regulated.
- `protected promise / function`: the `U.PromiseContent`, stakeholder value, function, operating regime, commitment payload, or delivery promise the bearer is trying to keep viable.
- `service situation`: an `A.6.8` facet-binding lens that identifies access point, delivery system, provider principal, promise content, commitment, delivery work, and evidence; it is not itself a new root bearer unless the relevant system facet is declared.
- `viability envelope`: the region where the bearer can still keep the relevant promise or function, across several dimensions.
- `envelope variable`: one characteristic that must stay within bounds, such as latency, reliability, support load, compliance exposure, safety margin, energy, or operator attention.
- `actuator`: a work action that can change the situation, such as cache policy, throttle, staffing, routing, bridge rewrite, protocol, access, escalation, or measurement design.
- `allostasis`: preserving function by changing settings, environment, boundary condition, actuation, or operating regime when circumstances change.

### C.26.3:2 - Problem

Teams often collapse viability into one dashboard value or fixed target. They optimize latency and damage operator load. They improve availability and increase compliance exposure. They preserve one metric while exhausting the team, hiding risk, or making recovery slower.

A second failure is passive sensing. A metric, probe, dashboard, alert, or health check is treated as a neutral window into viability, even when it changes behavior, hides unmeasured dimensions, or becomes an actuator through Goodhart effects.

A third failure is static stability. Teams say "keep the system stable" as if stability always means holding one internal variable fixed. In real architecture work, preserving viability may require changing environment, access, staffing, caching, throttling, routing, protocol, context split, or measurement design.

### C.26.3:3 - Forces

| Force | Tension |
| --- | --- |
| Bundle vs scalar | Viability usually concerns a bundle, but dashboards often expose one or two proxies. |
| Stability vs change | The system may preserve function by changing internal settings, external environment, boundary conditions, or operating regime. |
| Sensing vs actuation | Measurements may be sensors, probes, or actuators, depending on how they change behavior. |
| Ordinary control vs QL lens | `C.25`, `U.Dynamics`, `A.6`, `A.15`, and `C.16` remain primary patterns; QL enters only for probe, frame, export, or coarsening cue. |
| Light use vs dynamics detail | Rate, inertia, damping, actuator latency, and effort matter only when load-bearing. |

### C.26.3:4 - Solution

Use `C.25` / `U.Dynamics` alone for ordinary envelope work. Use C.26.3 only when the viability-envelope reading is distorted or constrained by probe, frame, export, coarsening, or incompatible representation cue. Otherwise use ordinary viability, quality-bundle, dynamics, measurement, boundary, and work patterns.

Start with this recognition note:

| Mini-entry | Question |
| --- | --- |
| Viability bearer | Which `U.System`, collective system, delivery system, role configuration, organism-as-system, or explicitly declared bearer is being kept viable? |
| Protected promise / function | Which `U.PromiseContent`, stakeholder value, function, operating regime, commitment payload, or delivery promise is protected? |
| Envelope variables | Which two to five variables matter, rather than one comfort scalar? |
| Disturbance | What pushes the bearer outside the envelope? |
| Sensor / probe / actuator | What reads the situation, and what can actually change it? |
| Trade-off / failure | What gets worse, what cost is paid, and what failure would show the envelope move did not work? |

Use the fuller envelope-regulation record below when the viability reading will change a metric, actuator, boundary, staffing, routing, promise, or evidence decision.

Full envelope-regulation record:

| Field | Question |
| --- | --- |
| Viability bearer | Which `U.System`, collective system, delivery system, role configuration, organism-as-system, or explicitly declared bearer is being kept viable? |
| Protected promise / function | Which `U.PromiseContent`, stakeholder value, function, operating regime, commitment payload, or delivery promise is protected? |
| Service situation facets, if used | Which `A.6.8` facets are involved: access point, delivery system, provider principal, promise content, commitment, delivery work, and evidence? |
| Envelope variables | Which characteristics or quality-bundle dimensions define viability? |
| Viable region / bounds | What counts as inside, near edge, degraded, or outside the envelope for this use? |
| QL cue or formal cue if retained | Which probe, order, export, coarsening, incompatible-frame, open-information-system update law, probe-frame relation, export admissibility, or measurement-changing-state cue remains after ordinary viability patterns are active? |
| Disturbance | What pushes the bearer outside the envelope? |
| Sensors / probes | Which metric, dashboard, alert, health check, review, trace query, observation setup, or probe reads the envelope, and can it change behavior or hide unmeasured dimensions? |
| Available actuators | What work, method, boundary action, staffing change, cache, throttle, bridge, access, protocol, or routine can change the situation? |
| Boundary condition preserved / changed | Which access, ownership, context, interface, promise, or environment condition matters? |
| Trade-off condition | Which envelope dimension is protected, relaxed, delayed, made more expensive, or deliberately held constant? |
| Adaptation cost | What is spent, delayed, damaged, risked, or made harder by the adaptation? |
| Failure mode | What breakdown, drift, unsafe persistence, or loss of viability shows that the move failed? |

#### C.26.3:4.1 - Homeostasis and allostasis reading

`Homeostasis` means keeping a parameter or bundle inside viable bounds. `Allostasis` means preserving functioning by changing internal settings, external environment, boundary conditions, actuation, or operating regime when circumstances change.

Do not say that all architecture is homeostasis. Say that some architecture decisions are viability-envelope decisions.

#### C.26.3:4.2 - Finish conditions

This pattern emits one of these results:

| Result | Meaning |
| --- | --- |
| Envelope-regulation claim | State bearer, protected promise/function, envelope variables, viable region/bounds, disturbance, sensors/probes, actuators, boundary condition, trade-off condition, authority, latency, adaptation cost, and failure mode. |
| Actuator redesign | Change cache, throttle, routing, staffing, protocol, access, bridge, escalation, measurement, or context split because the existing actuator cannot keep the envelope viable. |
| Measurement/probe redesign | Redesign a dashboard, alert, health check, readiness score, or review process because it distorts the envelope it reports. |
| Ordinary neighboring-pattern application | Use `C.25`, `C.16`, `A.6`, `A.15`, `U.Dynamics`, `C.18`, `C.19`, or `A.19` when the QL cue is not load-bearing. |
| No envelope claim | Drop the viability-envelope wording when bearer, protected promise/function, viable region/bounds, disturbance, actuators, adaptation cost, and failure mode cannot be stated. |

#### C.26.3:4.3 - Metric-induced distortion

Treat sensors, probes, dashboards, alerts, and metrics as possible participants in the viability relation, not as neutral windows by default.

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Metric-as-envelope | A proxy is treated as the whole envelope. | Recover bearer, protected promise, full envelope, unmeasured dimensions, and admissible use. |
| Goodharted viability | Actors optimize measured slots while damaging unmeasured survivor relations or future adaptability. | Treat probe-caused behavior with `C.26.1`; add evidence for unmeasured envelope dimensions. |
| Actuator overfit | An action preserves one parameter while pushing another cost, latency, boundary relation, or promise outside bounds. | Add trade-off condition, actuator authority, latency, adaptation cost, and failure mode. |

#### C.26.3:4.4 - Conditional dynamics detail

When rate, acceleration, second-order change, inertia, damping, resistance, effort, or actuator strength is load-bearing, state:

- what rate or acceleration matters;
- what slows or speeds the change;
- whether the rate of change itself is changing, rebounding, overshooting, or damping out;
- which inertia is useful and which is harmful;
- which actuator can actually change the envelope fast enough;
- which evidence shows the dynamic state.

If those variables are not load-bearing, do not force dynamics machinery into the case. The short recognition note or the full envelope-regulation record is enough.

#### C.26.3:4.5 - Primary EntityOfConcern and operational sequence

The primary EntityOfConcern is a viability-envelope claim or plan. It is not a generic quality score, not a control-theory survey, and not a biological analogy. The claim says that some bearer can keep a promise, function, or operating regime viable only if a set of variables remains inside a usable region under declared disturbances, probes, sensors, actuators, boundary conditions, and adaptation costs.

The first useful move is to turn a one-scalar stability story into an inspectable envelope-regulation decision.

Envelope-regulation sequence:

1. Name the viability bearer and the promise or function being preserved; if service or market language is used, declare whether the bearer is a collective `U.System`, delivery system, trace population, evidence set, or relevant `A.6.8` facet-binding before treating the situation as a bearer.
2. Name the envelope variables and the viable range or qualitative boundary for each.
3. Name the disturbance or regime change.
4. Name sensors/probes and say whether they only report, also frame, or also change behavior.
5. Name available actuators and who or what can enact them in time.
6. State the boundary condition being preserved or changed.
7. State the trade-off condition and adaptation cost.
8. State the failure mode and re-probe/destabilization condition.
9. Add dynamics detail only if rate, inertia, damping, latency, resistance, or acceleration changes the decision.

Ordinary output: produce a viability-envelope record with envelope variables and viable region, a disturbance/sensor/actuator map, and a trade-off, adaptation, and failure condition that tells the practitioner what changes in the work.

The output should tell a practitioner what changes in the work: redesign the metric, change cache policy, adjust staffing, reroute traffic, split or merge a context, add a bridge note, change an escalation promise, or drop the envelope claim.

#### C.26.3:4.6 - Viability envelope record

A usable envelope record is a pattern-local writing card, not a constructor. Use the fields below when envelope regulation is load-bearing:

```text
bearer: ...
protected promise or function: ...
envelope variables: ...
viable region: ...
disturbance: ...
sensors or probes: ...
available actuators: ...
actuator authority and latency: ...
boundary condition: ...
trade-off condition: ...
adaptation cost: ...
failure mode: ...
re-probe or destabilization condition: ...
```

The record is not `U.ViabilityEnvelopeRegulation`, not a new U-kind, and not a universal architecture constructor. It is a pattern-local normal form for writing envelope work clearly.

Well-formedness constraints:

- the bearer is a declared `U.System`, collective system, delivery system, role configuration, organism-as-system, explicitly modelled market slice, or other explicitly bounded bearer of viability;
- service-situation language identifies its `A.6.8` facets rather than treating the situation label as a root bearer by itself;
- at least two envelope dimensions are visible when the claim says "viability" rather than one ordinary metric;
- at least one actuator is named when the text proposes regulation rather than only diagnosis;
- the actuator has an authority and latency story, otherwise the recommendation is only a wish;
- the adaptation cost is named, because allostasis hides cost when phrased as "stability through change";
- the failure mode is named, because viability is otherwise indistinguishable from optimism.

#### C.26.3:4.7 - Sensor, probe, actuator, and metric split

Do not let one dashboard value stand for the whole envelope.

| Role | Viability-facing question |
| --- | --- |
| Envelope variable | Which quality, resource, promise, risk, or operating dimension is inside/outside viable range? |
| Sensor | Which metric, alert, trace, health check, survey, review, or observation reports part of the envelope? |
| Probe | Which measurement setup, dashboard, readiness check, review, experiment, or incident query may change behavior or expose hidden dimensions? |
| Actuator | Which cache, throttle, routing rule, staffing change, protocol, escalation, access change, bridge rewrite, or context split can change the envelope? |
| Boundary condition | Which access, ownership, context, interface, promise, environment, or information constraint shapes the envelope? |
| Adaptation cost | Which latency, risk, effort, attention, support load, compliance exposure, energy, trust, or future flexibility is spent? |

A metric value or dashboard carrier is not an actuator by itself. A measurement regime, publication act, alerting workflow, or governance routine may function as an actuator when the system responds through work: routing changes, escalation changes, staffing changes, cache policy changes, access changes, or boundary changes. An actuator can damage another envelope variable while repairing the one that triggered the work.

#### C.26.3:4.8 - Homeostasis, allostasis, and architecture work

Homeostatic wording is useful when the work preserves one variable or bundle inside a stable range. Allostatic wording is useful when the work preserves function by changing settings, boundary conditions, environment, access, staffing, routing, protocol, cache policy, or operating regime.

Use the minimal reading that carries the case:

| Reading | Use when | Practical output |
| --- | --- | --- |
| Scalar quality repair | One characteristic or Q-bundle dimension is enough. | Apply `C.25`, measurement patterns, or evidence patterns as appropriate. |
| Homeostatic envelope | The target is to keep a bundle inside a stable range under disturbance. | State variables, range, disturbance, sensor, actuator, and failure mode. |
| Allostatic envelope | Function is preserved by changing settings, boundary, environment, access, work routine, or operating regime. | State what changes, why function is preserved, and what cost moves elsewhere. |
| Probe-coupled viability | The measurement, dashboard, review, or readiness check changes the envelope it reports. | Coordinate with `C.26.1`. |
| Enacted viability state | Coordinated work evidences the envelope state better than one report. | Coordinate with `C.26.2`. |

Do not call every adaptation allostasis. The term earns its place only when stability-through-change is the useful architecture reading.

#### C.26.3:4.9 - Case bank and near misses

| Case | Supported C.26.3 reading | Near miss / reroute |
| --- | --- | --- |
| Checkout cache under spike | Cache aggressiveness preserves latency but increases stale payment-failure status and support load. | If only cache latency is at issue, use ordinary performance and quality-bundle patterns. |
| Smart-building energy control | Energy, comfort, privacy, occupancy, and abrupt weather changes form one envelope with sensors and actuators. | If the case only tunes one thermostat setting, use ordinary control/measurement language. |
| Incident staffing | Adding responders preserves recovery time but increases coordination overhead and error risk. | If staffing is merely a work allocation issue, use `A.15` / planning patterns. |
| Compliance exposure | A fast remediation path lowers outage time but increases evidence gaps and audit risk. | If audit evidence is primary, apply `A.10` or `B.3`; keep C.26.3 only for envelope trade-off. |
| Service boundary split | Splitting a service reduces deployment coupling but increases bridge loss and operational support transfer cost. | If the issue is only semantic bridge loss, use `F.9`; if the split changes the envelope, use C.26.3. |
| Body-temperature analogy | Function may be preserved by clothing, room air, activity, or exposure, not only internal heat production. | Use only as explanatory analogy; do not make biology the proof for software. |

#### C.26.3:4.10 - Source-to-pattern translation

Allostasis, active inference, FEP, Markov blankets, and computational-boundary sources are useful here only after translation into FPF architecture terms:

| Source-side term | FPF-facing translation |
| --- | --- |
| Homeostasis | Keep one parameter or bundle inside viable bounds. |
| Allostasis | Preserve function by changing settings, environment, boundary condition, actuation, or operating regime. |
| Active inference / perception as action | Measurement, sensor placement, and action have cost and can change later state estimates. |
| Markov blanket or computational boundary | Statistical or probabilistic boundary-lens cue only after recovery. Accepted local Markov dynamics stay with `A.3.3`; lens use stays with `C.29`, and C.26 or C.26.3 stays current only when quantum-like, probe, frame, viability, or measure-model-act claims remain. Physical boundary, interface module, component, functional element, boundary description or publication, and agency threshold require their direct owners; Markov wording does not admit them by itself. |
| Criticality / metastability | Stability may be regime-bounded and fluctuation-bearing, not one final fixed point. |
| Expected free energy / precision control | Information gathering, action, and confidence have cost; use only when those costs change the architecture decision. |

This translation keeps the pattern practical for architects. The reader should be able to move from a source line to an action: change a metric, change a probe, change an actuator, change a boundary condition, state a trade-off, or reroute.

### C.26.3:5 - Archetypal Grounding

Tell: A platform team tries to preserve checkout latency during a traffic spike. The first move is to increase cache aggressiveness. Latency improves, but support load rises because stale payment-failure status causes confused customer contacts.

Show, System side: the viability bearer is the checkout/payment service situation. Envelope variables include latency, payment correctness, support load, customer-promise reliability, and operator attention. Actuators include cache policy, retry policy, routing, dashboard query, escalation promises, and context bridge changes.

Show, Episteme side: the supported claim is not "latency is the viability state." It is an envelope-regulation claim: latency was preserved by an actuator that damaged another envelope dimension. The repair is to state the trade-off, adaptation cost, actuator authority, and failure mode.

### C.26.3:6 - Bias-Annotation

This pattern biases authors against scalar comfort. That bias prevents "green dashboard" from replacing viability.

It also biases authors toward actionable architecture work. The pattern asks who or what can actually change the boundary, access, protocol, staffing, cache, throttle, bridge, or measurement setup, and how quickly that action can matter.

The pattern may feel too broad if it is applied to every quality concern. It is not for every quality concern. Use `C.25` alone when one quality bundle or metric can be handled without envelope, disturbance, boundary condition, actuator, adaptation cost, or viability failure mode.

### C.26.3:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-C26.3.1 | The viability bearer is named. |
| CC-C26.3.2 | The protected promise or function is named. |
| CC-C26.3.3 | Envelope variables or quality-bundle dimensions and the viable region / bounds are named. |
| CC-C26.3.4 | Disturbance class and scenario/window are named. |
| CC-C26.3.5 | Sensors/probes and their possible behavior-changing or dimension-hiding effects are named when measurement carries the envelope claim. |
| CC-C26.3.6 | Available actuators and actuator authority/latency are named. |
| CC-C26.3.7 | Boundary condition, trade-off condition, and adaptation cost are stated. |
| CC-C26.3.8 | Failure mode and re-probe/destabilization condition are stated. |
| CC-C26.3.9 | Metrics or dashboards are not treated as the envelope itself. |
| CC-C26.3.10 | The QL cue / formal cue is named if QL wording is retained. |
| CC-C26.3.11 | QL wording appears only when probe, order, export, coarsening, or incompatible frame interaction remains load-bearing. |
| CC-C26.3.12 | Rate/inertia/damping/effort and second-order dynamics variables appear only when load-bearing. |
| CC-C26.3.13 | Homeostasis, allostasis, active inference, and Markov-boundary wording are restored into direct FPF owners before they carry the claim; Markov-blanket wording does not by itself create boundary, interface, component, agency, or viability authority. |
| CC-C26.3.14 | The pattern does not mint `ViabilityParameter`, `HomeostasisOntology`, or a new control ontology. |

### C.26.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| One metric as viability | Availability, latency, or score stands for the whole envelope. | Add the bearer, protected promise, other dimensions, and failure mode. |
| Fixed setpoint thinking | Stability means one variable must never move. | Ask whether allostasis preserves function by changing settings, environment, boundary, or regime. |
| Passive sensor assumption | A dashboard is treated as neutral even after it changes behavior. | Use `C.26.1` and evidence patterns. |
| Actuator without authority | The text recommends a change no one can enact in time. | State actuator authority and latency. |
| Biological proof jump | Homeostasis or FEP language is used as proof for software or organizations. | Treat it as modeling discipline and apply existing FPF patterns to claims. |
| Markov-blanket collapse | A statistical separation, physical interface, interface module, functional element, component, boundary description, and agency threshold are all called the Markov blanket. | Split the source phrase through `A.6.RSIR`: use `C.29` or `C.26` for lens use; use `A.1` plus the direct relation owner for holon delimitation or boundary crossing; use `A.6.P`, `A.6.0`, and `A.6.5` for relation, signature, or slot claims; use `A.6.M` for module-interface claims; use `A.6.F` for functional claims; use `A.14`, `C.13`, or `B.3.5` for component claims; use `C.30.AD` or `E.17` for descriptions; use `A.13`, `A.19`, or `C.16` for agency-threshold claims. |

### C.26.3:9 - Consequences

This pattern helps architects see stability-through-change. It supports decisions such as throttling, staffing, routing, protocol redesign, context split/merge, cache changes, measurement redesign, and escalation changes as envelope-regulation moves.

The cost is that simple metric stories become less simple. That is acceptable when the metric story hides the actual viability relation.

### C.26.3:10 - Rationale

Ordinary quality-bundle work does not always show boundary conditions, actuators, disturbances, adaptation cost, and failure modes together. C.26.3 coordinates those elements while preserving ordinary FPF patterns.

The QL lens is secondary. It matters when the way viability is probed, exported, or coarsened changes the state reading or admissible use of the representation.

### C.26.3:11 - SoTA-Echoing

| Pattern claim | Practice source | Pattern implication | Adoption stance |
| --- | --- | --- | --- |
| Viability maintenance is not fixed-value homeostasis only; stability can be relational, variational, dynamic, allostatic, metastable, and resilient. | [Conceptual foundations of physiological regulation incorporating the free energy principle and self-organized criticality](https://www.sciencedirect.com/science/article/pii/S0149763423004281). | Use viability envelopes and stability-through-change; reject one-scalar optimization and "all architecture is homeostasis." | Adapt as architecture-facing envelope discipline. |
| Action and perception are coupled under partial observability and cost. | [Active inference as a theory of sentient behavior](https://www.sciencedirect.com/science/article/pii/S0301051123002612). | Treat sensors, probes, dashboards, and actuators as part of the envelope relation when they change behavior or viability. | Adapt for measurement-as-action and planning cost. |
| Active-inference engineering already appears in energy/building control under privacy, partial observability, evolving conditions, and abrupt changes. | [Active Inference for Energy Control and Planning in Smart Buildings and Communities](https://arxiv.org/abs/2503.18161). | Use engineering examples cautiously: they show the kind of control problem, not settled FPF doctrine. | Use as emerging engineering anchor. |
| Boundaries can be statistical or computational descriptions of what a system can measure, model, and affect. | [The Computational Boundary of a Self](https://philpapers.org/rec/LEVTCB-3) and [The Markov blankets of life](https://philarchive.org/rec/KIRTMB). | Name boundary conditions and information constraints without reifying a boundary substance. | Adapt with map-territory caution. |
| Excess Bayesian / active-embodied inference shows the cost of moving sensor, body, instrument, or access point to obtain a discriminating observation. | [Connecting the free energy principle with quantum cognition](https://www.frontiersin.org/articles/10.3389/fnbot.2022.910161/full). | Treat probe placement, access placement, and observation cost as part of viability-envelope work when they change the decision. | Adapt for probe/action cost, not as a replacement for ordinary Bayesian or active-inference routes. |
| Platform and software engineering already treats many quality concerns as trade-off bundles. | Reliability, incident, platform, compliance, energy, support, operator-load practice, and [Google SRE SLO / error-budget practice](https://sre.google/workbook/implementing-slos/), coordinated with `C.25`. | Make the quality bundle explicit and state actuator authority, latency, adaptation cost, and failure mode. | Adopt through FPF quality-bundle routes. |

Worked-slice discipline from these rows:

- state the envelope before importing source terminology;
- translate source terms into selected structures, `ArchitectureOf@Context` relations, architecture descriptions, structural views, or named C.30 subcases;
- keep sensors, probes, actuators, and metrics distinct;
- state adaptation cost and failure mode;
- apply ordinary quality and measurement patterns to one-scalar quality concerns.

### C.26.3:12 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: braking, throttling, cadence, recovery, or stabilization moves in claims such as slow rollout protecting support capacity, request throttling preventing collapse, or cadence change preserving attention/team health.
- This pattern keeps: viability bearer, protected promise/function, viable region, disturbance, sensor/probe/action split, adaptation cost, and failure mode.
- Non-admissible use: stabilization wording is not a viability envelope, and C.27 is not the pattern for all stability-through-change claims.
- Exit: if the claim being made is only better quality, healthier team, or more resilient service without a declared viability envelope, use C.25, E.13, or the relevant quality/proxy/value pattern rather than C.26.3 or a C.27 profile.

- Builds on: `C.26`, `C.25`, `U.Dynamics`, `A.6`, `A.15`, `C.16`, `A.10`, `B.3`, `A.3`, `A.19`, `C.18`, `C.19`.
- Coordinates with: `C.26.1` when sensors, probes, dashboards, or metrics change represented state; `C.26.2` when coordinated work evidences the envelope state.
- Does not replace: ordinary quality-bundle patterns, generic control theory, full FEP doctrine, or biological homeostasis claims outside FPF bridge and loss discipline.
- Name boundary: `Viability-Envelope Boundary Regulation` names architecture work over a viability envelope and boundary/action conditions, not `Homeostasis Pattern`, `Allostasis Doctrine`, `Control Ontology`, `Quality Optimization Pattern`, or `Viability Substance`.

### C.26.3:End

