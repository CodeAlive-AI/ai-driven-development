## SYSE.50 - Construct and Calibrate an Agent's Assistance Policy

> **Type:** Method pattern
> **Status:** Stable

### SYSE.50:1 - Problem frame

**Use this when** a person or technical agent repeatedly obtains unhelpful assistance, misses a needed contribution, or makes help decisions from poorly qualified confidence. This Method constructs a reusable rule for the specified performer, task and available input: continue from present grounds, use an aid, retrieve evidence, clarify or stop. Assistance may be worthwhile even when unaided performance is possible.

The first result is an executable decision rule with its applicable signals, qualified need evidence, costs and fallback. Recognizing overconfidence or repetition starts the construction; evidence about the acted policy is needed before relying on it.

Keep an adequate direct rule, such as always reading current service state before a consequential change. A single invocation can use an existing policy. This construction becomes useful when deciding whether and which help to obtain is itself a recurring difficulty. It cannot create missing permission, an unavailable observation or an execution capability.

### SYSE.50:2 - Problem

A confident answer may be wrong; disagreement may be harmless; an uncertain phrase may merely reflect style. Repeated requests can also arise because useful evidence disappeared from the next input. Without locating the decision and qualifying its signal, tuning a confidence threshold can suppress necessary help or institutionalize needless interruption.

### SYSE.50:3 - Forces

More assistance can reduce some errors while adding delay, exposure, expense and new sources of error. A performer-relative rule can be useful under one set of conditions and misleading after a capability, tool, input or task change. Conservative fallback preserves a needed condition but may make the task infeasible. Average accuracy can conceal the rare unsupported action that determines the use limit.

### SYSE.50:4 - Solution

#### SYSE.50:4.1 - Select the decision and what the policy can observe

Name one decision unit: a particular claim, tool argument, action proposal or task continuation. Fix the performer or performing arrangement, relevant task family and information available at that point; identify the configured model when one is used. Distinguish an uncertain interpretation from a missing current fact, missing access, unresolved effect and absent authority. Further thinking can resolve some interpretation questions; it cannot manufacture an unavailable fact or authority.

List feasible responses and what each can supply. Retrieval may supply a source premise; clarification may settle the user's intended target; an outcome lookup may resolve a previous effect. A generic request for “more confidence” supplies none of these by itself.

Choose signals obtainable before the decision. For a person these may include observed error patterns, the presence of needed information, current working demands and an elicited judgement of confidence. For a model they may include exposed response scores, sampled disagreement, evidence coverage or a trained estimator. Record the signal's meaning and access conditions. A person's confidence report and a model score have different qualification bases; text alone is not an internal probability. A hidden-state estimator is unavailable to a text-only API. Keep instruction and evidence access comparable.

#### SYSE.50:4.2 - Obtain evidence of useful and necessary assistance

Assemble representative decision inputs with independently qualified target answers or allowed continuations. Preserve the evidence available to the performer. Distinguish a contribution indispensable to the result from an aid that improves reliability or reduces burden despite adequate unaided ability. Record what the complete assisted way changes, including obtaining, checking and using its return. Another person's or teacher model's tool use does not establish this performer's need.

Use paired conditions where they discriminate need: present versus withheld premise, ambiguous versus settled target, applicable versus revised rule. Obtain actual assistance returns where the policy relies on them. An oracle answer unavailable in deployment cannot qualify the deployed help branch.

Keep final policy comparisons outside rule construction. When calibration is selected, give it separate calibration examples. Select enough variation for the consequence and reliance; do not infer population calibration from a few illustrative examples. SYSE.49 can construct the missing distinction and challenge the labels. A disputed label remains unresolved until its result meaning has grounds. When the target is human acquisition, use HCD's practice purpose and permitted help: a hint and a complete answer can have different effects on the action being learned.

#### SYSE.50:4.3 - Construct the rule and its fallback

Relate the available signal to qualified outcomes, then select a decision rule under the receiving loss and resource constraints. For a threshold rule, compare supported continuation and assistance outcomes on calibration cases across candidate thresholds. Inspect unsupported continuation and unnecessary help separately, including the delay or cost of obtaining that help. A favorable average is insufficient when a protected error exceeds the declared allowance.

A set-valued construction is another option: score the allowed candidate actions and calibrate which remain plausible under the source method's assumptions. One supported candidate can permit selection; several consequentially different candidates can trigger clarification. An empty or inapplicable set needs an explicit fallback. A probability or coverage claim requires the corresponding sampling, labeling and calibration basis; a hand-chosen cutoff is an engineering rule until such evidence exists.

Make the output implementable: response, target question or source, decisive grounds, applicability and stop condition. Keep required facts, permissions and effect recovery as independent conditions. No confidence value authorizes replay of an attempt whose effect remains unknown.

Define behavior outside qualification. A changed performer/model condition, inaccessible signal, unrecognized input or defeated calibration premise can return to an adequate direct rule, request the specific missing contribution, or stop with the gap. It must not silently become permission to guess.

#### SYSE.50:4.4 - Test the acted policy and return the right defect

Put the rule into the person's practicable procedure or the technical controller through SYSE.47, and use SYSE.46 to compare whole receiving tasks with the incumbent or direct rule. Test both unsupported continuation and over-asking, plus confident common-source error, unavailable assistance and relevant drift. Calibrated scores alone do not establish that the selected help is timely, accurate or consumed.

Inspect the actual next input and transition when a supported premise is requested again. Return missing input to SYSE.52 and ignored return to SYSE.47. Repair the assistance rule here only when the decision uses the relevant input yet selects the wrong help behavior. Reopen calibration when a relied-on model, input, signal, source or task population changes. Stop at the bounded rule and evidence, or its qualification gap.

### SYSE.50:5 - Archetypal Grounding


#### SYSE.50:5.1 - Build a useful human assistance rule


A person regularly totals stock lots. Prior comparable work supports mental decomposition of 347 × 6, but some occasions require keeping other intermediate values or retaining written working. The constructor compares complete mental, paper and calculator ways: entry, setup, arithmetic, checking and reporting all count. In the constructed evidence, a ready calculator frees working attention when those other values must be held; the mental way is adequate and cheaper when no such benefit or written record is needed.

Build a short rule from observable conditions. If the current quantity per lot is missing, obtain it from the relevant source or return the gap. If the expression is complete and the person has the supported mental way with no added record/burden need, use it and report the computed total: 2082 for this case. If a recoverable digit record is required, use the adequate written layout. If an already available, checkable calculator protects the other task values at worthwhile whole cost, enter and inspect 347 × 6, use its 2082 return and stop. This is an explicit engineering rule for the supplied conditions, not a statistically calibrated confidence threshold.

Test the rule on fresh comparable tasks, including an already sufficient case, a missing quantity and an aid whose display cannot support the required input check. Compare missed support and needless setup as well as correct totals. A high confidence report cannot replace the missing quantity, and adequate unaided ability does not negate the calculator's possible benefit. Return a mistyped expression to SYSE.42 and a lost carry row to SYSE.52 before changing this assistance rule.

If the target instead is learning to use a carry, HCD's practice design can select a hint that lets the person perform the addition. Giving 2082 can finish the numeric task while removing that practice contribution. The rule and its evidence must follow the declared target; supported success alone supplies no unaided-learning conclusion.


#### SYSE.50:5.2 - Build a technical rule with accessible signals


An agent must update a service once and report its observed state. It keeps requesting an already applicable maintenance rule. The engineer first verifies that the next input contains the rule, its edition and target applicability, and that the controller would execute a proposal to proceed. This isolates the assistance decision from lost context and ignored returns.

Construct three decision inputs. In A, the applicable rule and an unambiguous target are supplied. In B, the rule is supplied but two target identifiers fit the request. In C, the rule's required current capacity observation is absent. The qualified responses are respectively proceed to the remaining checks, ask which target, and obtain current capacity. “Proceed” in A still requires execution preconditions and actual effect observation.

A text-only endpoint exposes no token scores. The engineer chooses observable premise coverage and sampled target disagreement as candidate signals, then compares rules on separately labeled calibration inputs. A simple candidate routes settled interpretation to continuation, target ambiguity to clarification, and missing current capacity to its actual observation. A confidence-based alternative must justify any additional discrimination it offers over this direct rule.

Challenge both with a source that confidently names the wrong target. Agreement among samples cannot establish the target's identity; the qualified reference defeats it. Challenge the acquisition branch with an unavailable capacity endpoint: repeated requests cannot repair access, so the result is the missing observation. A new rule edition requiring another measurement defeats the earlier completeness assessment.

The trial compares supported completion, unwarranted continuation, unnecessary assistance and total burden on separate service tasks. If a small direct rule performs adequately, retain it without claiming statistical calibration. If the more adaptive rule earns reliance, retain its observed scope and fallback. These are constructed cases and a proposed comparison.

### SYSE.50:6 - Bias-Annotation

A labeler can mistake their own difficulty for another performer's need, or treat successful help as proof that help was necessary. Shared sources can make model, labeler and checker agree on a false premise. Include a source-independent challenge and preserve uncertainty about necessity when the comparison cannot isolate it.

### SYSE.50:7 - Conformance Checklist

- The decision unit, performer/configuration, task and obtainable signals are explicit.
- Qualified outcomes distinguish unsupported continuation, useful help and needless interruption.
- The rule consumes information actually available at the decision.
- Calibration claims have their own basis; the acted policy has a separate comparison.
- Permission, current facts and unresolved effects keep independent conditions.
- Drift, unavailable assistance and unrecognized inputs have a usable fallback.

### SYSE.50:8 - Common Anti-Patterns and How to Avoid Them

**Use “90% confident” as the success test.** Relate the signal to qualified outcomes at the receiving decision and test the resulting behavior.

**Ask after every disagreement.** Determine whether the alternatives change the action and whether the requested help can resolve them.

**Fix a threshold when the prompt lost the answer.** Restore the consequential input through SYSE.52 before attributing the failure to assistance selection.

### SYSE.50:9 - Consequences

Assistance becomes a purposeful response to a bounded uncertainty or missing contribution. Its estimator, labels and fallback create maintenance cost. Better calibration can coexist with worse task performance when help is slow, wrong or unused; retain both levels of evidence.

### SYSE.50:10 - Architectural Rationale

The rule can be revised while the performer, execution procedure and effort allowance stay fixed. It can supply a human procedure, external controller or learned policy. Constructing the relation from observable conditions to useful help has a different result from invoking the chosen aid, allocating further effort or testing the whole configuration.

### SYSE.50:11 - SoTA-Echoing

The available abstract-level account of [Gilbert, 2024](https://doi.org/10.1016/j.cognition.2024.105783) motivates considering opportunity cost when external support can be useful despite available human ability. That bounded source use supplies neither a universal cost scale nor a validated human/model estimator. The worked human rule makes no statistical calibration claim; such a claim requires its own calibration evidence.

For the technical signal-to-rule construction, [KnowNo, CoRL 2023, §§2–3 and 6](https://proceedings.mlr.press/v229/ren23a/ren23a.pdf) is a historical constructive anchor: action scores and separately labeled calibration cases produce an action set that controls help. Its guarantee depends on sampling conditions, accurate help, grounded observations and executable actions; dependent steps need its sequence treatment. Adopt the score-to-decision construction only with those conditions.

[SMART, ACL 2025, §§4.1–4.3](https://aclanthology.org/2025.findings-acl.239.pdf) offers a learned alternative using mixed subproblems, need annotations and actual tool returns. Its teacher and source heuristics require qualification for the receiving model. [The Confidence Dichotomy, ACL 2026, §§3–4](https://aclanthology.org/2026.acl-long.520.pdf) separates answer accuracy from verbalized confidence; improving the latter does not itself demonstrate a routing policy.

These mechanisms support alternative bounded constructions. They establish no universally best signal or threshold. Reopen the selected construction when access, model, source assumptions or the cost of mistaken help changes.

### SYSE.50:12 - Relations

C.38 constructs complete comparable ways; C.11 applies the receiving choice criterion. A.15.7 consumes the supplied cue for current action; A.15.9 obtains the selected contribution; C.24 plans a fixed technical action. HCD supplies human acquisition and its permitted help when that is the target. SYSE.47 implements the rule, SYSE.45 can learn it, SYSE.49 constructs qualified decision experience and SYSE.46 tests receiving use. SYSE.51 controls further effort; SYSE.52 supplies the actual decision input. None substitutes for the domain meaning of a supported answer.

### SYSE.50:End
