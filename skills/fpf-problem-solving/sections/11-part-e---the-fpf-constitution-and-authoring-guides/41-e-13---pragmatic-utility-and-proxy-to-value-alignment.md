## E.13 - Pragmatic Utility and Proxy-to-Value Alignment

> **Type:** Part E FPF evaluation and repair pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is marked informative

### E.13:0 - Use This When

Use this pattern when a project treats a visible measure, score, proxy, benchmark, dashboard, quality value, review result, release posture, or evidence volume as if it were the practical value or objective itself.

Look for situations such as these:

- a metric improves, but the team cannot say what intended value improved;
- a quality score, all-`5` posture, assurance level, citation count, source count, or review pass becomes the target;
- a proxy is used as a gate, incentive, resource-allocation signal, reputation signal, or release argument;
- a model, method, pattern, or system is formally better while users or operators are worse off, or safety, maintainability, learning, or decision quality worsens;
- an evaluation loop adds apparatus to satisfy the evaluator instead of improving the object of concern.

**First useful move.** Name the intended value or objective and the proxy or visible measure. State how the proxy is used now: measure, target, incentive, gate, release argument, decision driver, reputation signal, repair target, or orientation cue.

**What goes wrong if missed.** The team optimizes the proxy and loses the value. It can produce a better score, cleaner review proof, larger source packet, or more complete record while practical utility gets worse.

**What this buys.** FPF can keep measurement, evaluation, and quality loops useful without letting their visible outputs replace the value they were meant to serve.

**Not this pattern when.**

- If the question is whether a measurement scale is admissible, use `C.16`.
- If the question is ordinary pattern quality, use `E.21`; use `E.13` only when a visible quality value is being treated as the practical value.
- If the question is DRR adequacy, use `E.9.DA`; use `E.13` only when DRR marks become a surrogate for decision usefulness.
- If the question is whole-FPF Pillar adequacy, use `E.2.DA`; use `E.13` only when Pillar values become the target.
- If the question is assurance, gate passage, evidence sufficiency, or decision authority, use the governing pattern for that claim before treating the visible proxy as value.

### E.13:1 - Problem Frame

Practical work often needs visible measures. Teams use scores, dashboards, quality coordinates, tests, evidence counts, source freshness rows, release checks, and worked examples because practical value can be hard to observe and steer directly.

The danger starts when the visible measure becomes the object being optimized. A proxy can be useful as a signal and harmful as a target.

A pattern can become easier to defend while harder to use. A safety dashboard can look better while unmeasured hazards increase. A review result can look more complete while the decision it was meant to support becomes less decisive.

`E.13` governs the proxy-to-value repair. It asks whether the visible measure still serves the intended value in the declared use, and what became worse when the measure improved.

### E.13:2 - Problem

Typical failures include:

1. **Measures replace objectives.** Teams speak as if the score, metric, benchmark, assurance level, or all-`5` posture is the value.
2. **Evaluation loops become reward functions.** A checking reader asks for improvement; the author adds fields, guards, source rows, proof sketches, and relation catalogues until the visible evaluation looks better.
3. **Unmeasured value is damaged.** Usability, safety margin, maintainability, learning, domain fit, affordability, or operator action quality gets worse while the proxy improves.
4. **The proxy's use is unspecified.** The same metric is treated as orientation cue, target, incentive, gate, and release proof without saying which use applies.
5. **No value slice exists.** The text claims practical payoff, but gives no minimally viable case that shows the value being realized.

### E.13:3 - Forces

| Force | Tension |
| --- | --- |
| Measurement vs value | Projects need visible signals, but signals can replace the value they indicate. |
| Local optimization vs protected qualities | A local score can improve while another value-bearing dimension worsens. |
| Evaluation signal vs object improvement | A visible evaluation mark can be easier to raise than the object is to improve. |
| Proxy affordability vs value evidence | A proxy is cheap; demonstrating value can be expensive. |
| Release confidence vs ongoing distortion | A proxy may be safe for orientation but unsafe as a gate, incentive, or release argument. |

### E.13:4 - Solution

Use `ProxyToValueAlignment` to recover the intended value, the proxy's current use, the value at risk, and the justified repair or stop. A short answer or local repair is enough when it settles the case.

When later review, reuse, or reliance needs a note, use the fields below that change the conclusion.

```text
ProxyToValueAlignment:
  ObjectOfConcern:
  IntendedValueOrObjective:
  ProxyOrVisibleMeasure:
  ProxyKind:
  CurrentProxyUse: <orientation | measure | target | incentive | gate | release argument | decision driver | reputation signal | repair target>
  AffectedDecisionOrWork:
  ProtectedQualities:
  WhatImproved:
  WhatGotWorse:
  MinimallyViableValueSlice:
  AdmissibleUseNow:
  BlockedOverread:
  RepairOrStop:
  ReopenCondition:
```

Record only the fields needed for the current conclusion, repair, stop, or later reliance. Use them to explain the relationship between the proxy and the intended value.

#### E.13:4.1 - Name the Value Before the Proxy

Name the intended value, objective, or practical payoff in terms of the work it is supposed to improve. If only the proxy can be named, report that the project has a measure. Its connection to the intended value has yet to be shown.

#### E.13:4.2 - Type the Proxy Use

A proxy can be harmless as an orientation cue and dangerous as a target. State how the proxy is being used.

| Proxy use | Admissible use | Danger |
| --- | --- | --- |
| Orientation cue | Helps decide where to look next. | Mistaken for evidence of value. |
| Measure | Reports one declared characteristic under `C.16`. | Treated as the whole objective. |
| Decision driver | Informs a choice under the applicable decision rule. | The proxy displaces the intended objective or protected qualities in the choice. |
| Target | Work is optimized to move the proxy. | Goodhart pressure. |
| Incentive | People or agents are rewarded for the proxy. | Behavioral distortion and gaming. |
| Gate or release argument | Passage depends on the proxy. | Proxy becomes authority. |
| Reputation or status signal | People, teams, models, or patterns are ranked by the proxy. | Surrogation and status gaming. |
| Repair target | The object is changed to raise a coordinate or score. | Apparatus is added instead of value. |

#### E.13:4.3 - Ask What Got Worse

Whenever a proxy improves under optimization pressure, ask what became worse or more fragile.

Check at least usability, affordability, safety or harm boundary, maintainability, domain fit, source preservation, decision quality, learning, and neighboring-pattern fit when they are live in the case.

If nothing worsened, identify what was checked. If nothing was checked, do not claim value alignment.

#### E.13:4.4 - Require a Minimally Viable Value Slice

Require a minimally viable value slice: one compact case, worked slice, observation, trial, user/operator moment, or decision replay where the intended value is visible enough for the declared use.

State whether the slice is an illustration, desk replay, or observed use, and what conclusion it supports.

The slice may be small. It must show the intended value for the declared use. A proxy reading alone is insufficient.

A worked illustration can explain how a proposed repair would serve that value; it does not by itself establish an observed gain. Keep any claim about actual improvement within the comparison and evidence that support it.

#### E.13:4.5 - Repair by Value Movement

When the proxy has displaced the value, choose one or more of these repairs:

- where the governing rule permits it, change the proxy use from target/gate/incentive to orientation or bounded measure. If a binding requirement must change, propose the amendment under its authority and keep the current requirement in force until that amendment takes effect;
- add a protected quality or counter-metric that names the value at risk;
- change the work or design so the value slice improves, not only the proxy;
- split the claim: one measure report, one value claim, one assurance or gate claim if needed;
- stop the value claim until a value slice or better proxy relation exists.

### E.13:5 - Archetypal Grounding

| Case | Proxy pressure | E.13 repair |
| --- | --- | --- |
| Pattern quality loop | All-`5` pattern-quality posture becomes the target. | Use `E.21` values as measurements. Revise the pattern only where its substantive content can improve. Record what worsened when apparatus was added. |
| DRR review | Source rows and selected-locus tables grow while the decision remains vague. | Use `E.9.DA`; the DRR improves only when selected answer, source payload, or first drafting action improves. |
| Safety dashboard | A lower incident count is used as proof of safety. | Split measure, reporting behavior, unreported hazard, and safety assurance; use the safety/assurance pattern for the stronger claim. |
| AI reward model | A model gets higher reward or judge score by exploiting the specification. | Treat the score as proxy; inspect unmeasured intended outcome and blocked value dimensions. |
| Manufacturing throughput | Throughput rises while rework, fatigue, or latent defect risk rises. | Keep throughput as a measure; add protected qualities and a value slice for delivered usable output. |

### E.13:6 - Bias-Annotation

E.13 rules out two substitutions. In proxy-for-value bias, the visible measure, score, evidence volume, review result, release posture, or dashboard state is treated as the practical value itself.

In evaluator-satisfaction bias, a team adds apparatus to satisfy an evaluation signal while the governed object, user work, safety, maintainability, or decision quality does not improve.

### E.13:7 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-E13-1` | The repair names the intended value or objective before the proxy. |
| `CC-E13-2` | The proxy or visible measure is typed by current use: orientation, measure, target, incentive, gate, release argument, decision driver, reputation signal, or repair target. |
| `CC-E13-3` | If a proxy improved, the repair asks what got worse and names checked loci or protected qualities. |
| `CC-E13-4` | A minimally viable value slice shows the intended value for the declared use, or the value claim is lowered. |
| `CC-E13-5` | The repair does not treat evaluation values, source counts, review praise, all-`5` posture, assurance level, or release status as value by itself. |
| `CC-E13-6` | Stronger claims are governed by their direct patterns: measurement by `C.16`; quality evaluation by `E.21`, `E.9.DA`, or `E.2.DA`; assurance by `B.3`; gate passage by `A.21`; choice among options by `C.11`; decision authority by the applicable domain rule; and value and proxy alignment here. |
| `CC-E13-7` | The repair changes value movement, proxy use, protected qualities, claim split, or stop condition; it does not close by adding proof apparatus alone. |

### E.13:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Score as value | A higher score is reported as practical improvement. | Name intended value, proxy use, and value slice. |
| All-`5` targeting | A pattern or DRR is rewritten to make every coordinate defensible as `5`. | Use the evaluation as measurement; improve the content and address the trade-offs for protected qualities. |
| Source-count proof | More citations or source rows are treated as better decision quality. | Ask what changed in the substance of the decision. |
| Dashboard myopia | A visible dashboard metric improves while unmeasured harm rises. | Add protected qualities and split measure from value. |
| Proxy as gate authority | A proxy is treated as authority for release or gate passage without satisfying the rule that governs that decision. | Apply the governing release rule for release, `A.21` for gate passage, and `B.3` for an assurance claim; keep proxy use bounded. |
| Value slice missing | Practical payoff is asserted but never shown in a case. | Add a minimally viable value slice or lower the payoff claim. |

### E.13:12 - Consequences

- FPF can use scores and metrics without making them the object of optimization.
- Improvement loops gain a simple value-proxy stop condition.
- Practical payoff claims need at least a small value slice.
- Some attractive proxy improvements are rejected, split, or lowered.
- The cost is a small proxy-to-value check whenever a visible measure becomes a target, incentive, gate, release argument, or repair target.

### E.13:9 - Rationale

FPF needs measurement, evaluation, assurance, and release checks as instruments for pursuing practical value. `E.13` keeps the visible instrument attached to the intended value and asks whether the value survives optimization pressure.

To repair a Goodhart-style failure, restore the relation among the intended value, the proxy, its use, the protected qualities, and a small case that shows the value. Adding another large audit cannot by itself restore that relation.

### E.13:10 - SoTA-Echoing

| Claim | Source lineage | Local adoption |
| --- | --- | --- |
| A measure used for decision or control can corrupt the process it monitors. | [Campbell, *Assessing the Impact of Planned Social Change* (1976), pp. 49–52](https://www.humanlearning.systems/uploads/08%20Assessing%20the%20Impact%20of%20Planned%20Social%20Change.pdf), a historical account of indicator pressure and distortion. | `CurrentProxyUse` distinguishes measure, target, incentive, gate, and release argument. |
| Proxy optimization has distinct failure modes. | [Manheim and Garrabrant, *Categorizing Variants of Goodhart's Law* (2018/2019)](https://arxiv.org/abs/1803.04585), distinguishing mechanisms of harmful proxy overoptimization. | `WhatGotWorse` and protected qualities prevent a single proxy from standing for value. |
| Measures can replace the strategic construct in decision makers' minds. | [Choi, Hecht and Tayler, *Lost in Translation* (2012)](https://scholarsarchive.byu.edu/facpub/8208/), on strategy surrogation and incentive compensation. | The proxy is never named as the value; the intended value is named first. |
| Optimizing an imperfect reward or specification can satisfy the formal signal while missing the intended outcome. | [Skalse et al., *Defining and Characterizing Reward Hacking* (2022)](https://arxiv.org/abs/2209.13085), a formal treatment of proxy and true reward divergence under stated policy assumptions. | Evaluation values, judge scores, and all-`5` posture are treated as proxies that require value-slice and protected-quality checks. |
| Useful measures should be derived from goals and questions. | [Basili, Caldiera and Rombach, *The Goal Question Metric Approach*](https://www.cs.umd.edu/~mvz/handouts/gqm.pdf), deriving measurement from goals, questions and interpretation context. | E.13 asks for intended value/objective before proxy and asks which decision or work the proxy affects. |
| Human values require stakeholder and use-context inquiry, not only formal metrics. | [Value Sensitive Design's tripartite methodology](https://vsdesign.org/vsd/), connecting stakeholder values with conceptual, empirical and technical investigations. | The minimally viable value slice may include user, operator, manager, safety, or affected-stakeholder evidence when those values are live. |

### E.13:11 - Relations

- **Implements:** `E.2` Pillar `P7 Pragmatic Utility`.
- **Complements:** `E.12` for cognitive ergonomics and `E.14` for human-facing working models.
- **Coordinates with:** `E.8` for authoring practical-payoff claims, `E.19` for review/admission proxy-to-value checks, `E.22`/`E.23` for improvement framing and repeated improvement loops, `C.16` for measurement admissibility, `C.25` for engineering quality-family endpoints, `E.21` for pattern quality, `E.9.DA` for DRR adequacy, `E.2.DA` for whole-FPF Pillar adequacy, `B.3` for assurance, `A.21` for gate passage, `C.11` for decisions, and `A.10` for evidence.
- **Used by:** improvement loops, release checks, pattern reviews, dashboards, metric-driven work, AI reward or judge-score cases, and any project where visible performance may displace intended value.

### E.13:End
