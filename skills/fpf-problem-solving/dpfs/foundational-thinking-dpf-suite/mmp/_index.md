# Mathematical Modeling DPF

**DocID:** `MMP` within **FPF Library**.

> Methods for constructing mathematical representations of a question, connecting unknown relations, observations and available actions, and revising the resulting models.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 24 October 2026
- **Status:** Eternal alpha: a growing language of general modeling methods.
- **License:** © 2026 Anatoly Levenchuk. Original framework text: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Cited sources retain their own terms.
- **Publication:** [FPF Library repository](https://github.com/ailev/FPF)

Begin with the question your model must answer. Use the Table of Contents to find a relevant pattern, then open its Problem frame, Solution, worked cases and checklist. Readme shows how results connect the methods; Architectural Reference explains their rationale and limits.

The code **MMP** names this DPF. Its numbers are stable pattern addresses; § shows position in this edition. References beginning MATH name patterns in [Mathematical Thinking (MATH)](../math/_index.md). References such as C.29 name patterns in [FPF](../../../sections/03-first-principles-framework-readme/_index.md). Core also supplies the Method-development constructions cited by their PatternIDs, including C.39.RQ for requirements, C.32.MWA.PP for performance and provision, and B.1.5.CM for a Method whole. Open the cited publication when that contribution is needed. When using another version, revisit a conclusion if its cited operation or condition has changed.

To cite this edition: Anatoly Levenchuk, *Mathematical Modeling DPF*, [FPF Library repository](https://github.com/ailev/FPF). Include the version date shown above.

# Table of Contents

## Public units

| Unit | Title | Use |
| --- | --- | --- |
| Readme | [Mathematical Modeling - Readme](_index.md#mathematical-modeling---readme) | Follow worked connections between modeling methods. |
| Architectural Reference | [Mathematical Modeling DPF Architectural Reference](_index.md#mathematical-modeling-dpf-architectural-reference) | Understand the connected methods, their rationale, sources and limits. |
| MMP.Reference:1 | [Problem frame - Make a mathematical question useful](01-mmp-reference-1---problem-frame---make-a-mathematical-questi.md) |  |
| MMP.Reference:2 | [Problem and forces - Choose what the model must retain](02-mmp-reference-2---problem-and-forces---choose-what-the-model.md) |  |
| MMP.Reference:3 | [Solution - Connect the contributions the question needs](03-mmp-reference-3---solution---connect-the-contributions-the-q.md) |  |
| MMP.Reference:3.1 | [Form the first account and recover its interpretation](03-mmp-reference-3---solution---connect-the-contributions-the-q.md#mmpreference31---form-the-first-account-and-recover-its-interpretation) |  |
| MMP.Reference:3.2 | [Represent admissible objects and construct missing relations](03-mmp-reference-3---solution---connect-the-contributions-the-q.md#mmpreference32---represent-admissible-objects-and-construct-missing-relations) |  |
| MMP.Reference:3.3 | [Construct change and observation together when they interact](03-mmp-reference-3---solution---connect-the-contributions-the-q.md#mmpreference33---construct-change-and-observation-together-when-they-interact) |  |
| MMP.Reference:3.4 | [Turn uncertainty into a question about available action](03-mmp-reference-3---solution---connect-the-contributions-the-q.md#mmpreference34---turn-uncertainty-into-a-question-about-available-action) |  |
| MMP.Reference:3.5 | [Simplify, diagnose and revise for the required consequence](03-mmp-reference-3---solution---connect-the-contributions-the-q.md#mmpreference35---simplify-diagnose-and-revise-for-the-required-consequence) |  |
| MMP.Reference:3.6 | [Use the model-forming result across the Suite](03-mmp-reference-3---solution---connect-the-contributions-the-q.md#mmpreference36---use-the-model-forming-result-across-the-suite) |  |
| MMP.Reference:3.7 | [Constituent actions in ongoing work](03-mmp-reference-3---solution---connect-the-contributions-the-q.md#mmpreference37---constituent-actions-in-ongoing-work) |  |
| MMP.Reference:3.8 | [Compare or construct the way work is performed](03-mmp-reference-3---solution---connect-the-contributions-the-q.md#mmpreference38---compare-or-construct-the-way-work-is-performed) |  |
| MMP.Reference:4 | [Archetypal Grounding - A report, an instruction and a changed question](04-mmp-reference-4---archetypal-grounding---a-report-an-instruc.md) |  |
| MMP.Reference:4.1 | [A total is sufficient until the question changes](04-mmp-reference-4---archetypal-grounding---a-report-an-instruc.md#mmpreference41---a-total-is-sufficient-until-the-question-changes) |  |
| MMP.Reference:5 | [Conformance Checklist - Can the result do its intended work?](05-mmp-reference-5---conformance-checklist---can-the-result-do.md) |  |
| MMP.Reference:6 | [Common Anti-Patterns and How to Avoid Them](06-mmp-reference-6---common-anti-patterns-and-how-to-avoid-them.md) |  |
| MMP.Reference:7 | [Consequences, biases and limits](07-mmp-reference-7---consequences-biases-and-limits.md) |  |
| MMP.Reference:8 | [Architectural Rationale - Organize by model-forming operations](08-mmp-reference-8---architectural-rationale---organize-by-mode.md) |  |
| MMP.Reference:9 | [Source use and currentness](09-mmp-reference-9---source-use-and-currentness.md) |  |
| MMP.Reference:10 | [Relations to continued inquiry and work](10-mmp-reference-10---relations-to-continued-inquiry-and-work.md) |  |

## A. Formulate the subject question

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MMP.10 - Construct and Revise a Mathematical Constraint Formulation](12-mmp-10---construct-and-revise-a-mathematical-constraint-form.md) | Stable | objects; representation; domains; constraints; recovery; multiplicity; optimization. How can the objects and conditions of a working question be expressed so that mathematical answers still refer to the intended possibilities? | B.5.FM for initial formulation; MATH.1 and MATH.5 for construction and representation; C.29.1 for transferring results; MMP.11 for unknown relations. |
| 2 | [MMP.11 - Construct a Mathematical Model Family from Known Relations](13-mmp-11---construct-a-mathematical-model-family-from-known-re.md) | Stable | unknown relation; family; grounded structure; parameterization; completeness; identifiability. How can an unknown contribution vary without losing known relations, and which remaining ambiguity changes the requested consequence? | MMP.10 for admissible representation; A.3.3.TR for state; C.16.IR for observation-based inference; C.28.MR for intervention; MMP.9 for reduction. |
| 3 | [MMP.8 - Formulate Information-Dependent Choices Mathematically](14-mmp-8---formulate-information-dependent-choices-mathematical.md) | Stable | available information; action; policy; decision timing; objective; conditional requirement; average performance. What can be chosen with information available in time, and which conditions must that choice satisfy? | MMP.7 for reports; A.3.3.TR for change; MMP.10 for constraints; MMP.22 for a mathematically constructed change and Core Method development for its wider working conditions. |
| 4 | [MMP.8.SD - Construct a Sequential Decision Model from Information and Consequences](15-mmp-8-sd---construct-a-sequential-decision-model-from-inform.md) | Stable | sequential decision; sufficient state; belief; policy; transition; accumulated consequence; continuation. What information must a continuing instruction retain, and how do present choices affect later possibilities and results? | MMP.8 for available choices; A.3.3.PI for predictive state and belief; MMP.7 for records; CMP.3, CMP.5 and CMP.9 for policy computation. |

## B. Infer, distinguish and revise

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MMP.7 - Construct a Probability Model of the Recorded Data](16-mmp-7---construct-a-probability-model-of-the-recorded-data.md) | Stable | observation; recorded data; selection; missing records; censoring; noise; probability law. What distribution does the recording procedure produce from the modeled possibilities? | C.16.IR for interpretation and inference; MMP.11 for unknown relations; MMP.8 when the record informs a choice. |
| 2 | [MMP.12 - Formulate an Inverse Problem and Choose Whether and How to Use Regularization](17-mmp-12---formulate-an-inverse-problem-and-choose-whether-and.md) | Stable | inverse problem; identifiability; conditioning; regularization; restriction; penalty; target. Which unknowns can the records resolve, and what improvement and loss does a stable reconstruction introduce? | C.16.IR for compatible cases; MMP.11 and MMP.7 for the forward and recording relations; MMP.13 for inferential uncertainty; CMP for solving the formulated problem. |
| 3 | [MMP.13 - Infer Unknowns Statistically under a Stated Observation Model](18-mmp-13---infer-unknowns-statistically-under-a-stated-observa.md) | Stable | estimator; confidence coverage; prior; posterior; predictive uncertainty; dependence; target propagation. Which inferential construction supports the statement the receiver needs? | MMP.7 for the record law; MMP.12 and C.16.IR for ambiguity; CMP.8 and CMP.9 for numerical computation; MMP.14 and MMP.8 for prediction checks and decisions. |
| 4 | [MMP.14 - Find and Repair a Mathematical Model's Failed Predictions](19-mmp-14---find-and-repair-a-mathematical-model-s-failed-predi.md) | Stable | model criticism; predictive comparison; residual; conditional response; selection; repair; held-out prediction. Which discrepancy changes the use, what assumption can repair it, and what consequence must be recalculated? | MMP.7, MMP.11 and MMP.13 for comparable predictions; B.5.RR for affected revision; CMP.8 and CMP.9 for numerical error; C.11.DUA for worthwhile further checking. |
| 5 | [MMP.15 - Identify an Intervention Effect from Available Data](20-mmp-15---identify-an-intervention-effect-from-available-data.md) | Stable | causal identification; intervention; adjustment; mediation; population transfer; support; partial identification. Which intervention consequence follows from the available laws and causal assumptions? | C.28.MR for intervention meaning; MMP.7 and MMP.13 for recording and estimation; C.16.IR for compatible possibilities; MMP.16 for worthwhile distinguishing observations. |
| 6 | [MMP.19 - Construct and Bound a Mathematical Counterfactual Comparison under a Causal Model](21-mmp-19---construct-and-bound-a-mathematical-counterfactual-c.md) | Stable | counterfactual; same case; factual inference; common input; joint response; pathway; bounds. What would happen to the same case under another action, and what does the available information determine? | C.28.MR for changed mechanisms; MMP.7 and MMP.13 for factual records and inference; MMP.15 for identification; MMP.10 and MMP.16 for bounds and useful observations. |
| 7 | [MMP.16 - Design Observations to Separate Mathematical Model Alternatives](22-mmp-16---design-observations-to-separate-mathematical-model.md) | Stable | observation design; discrimination; nuisance; recording law; value of information; feasible design. Which obtainable observation separates a consequential ambiguity, and can its benefit repay its burden? | MMP.7, MMP.11, MMP.12 and MMP.13 for predicted record laws; MMP.8 and MMP.8.SD for decisions; C.11.DUA for worthwhile further work; subject methods for realization. |

## C. Change the model while retaining its use

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MMP.9 - Derive a Reduced Mathematical Model of State Evolution](23-mmp-9---derive-a-reduced-mathematical-model-of-state-evoluti.md) | Stable | reduction; hidden state; closure; memory; approximation; error; sufficient bound. What contribution is left by eliminated detail, and which replacement preserves the consequence needed? | A.3.3.TR for evolution; C.29.1 for preserved structure; MMP.11 for a replacement family; B.5.RR for affected revision. |
| 2 | [MMP.17 - Construct a Surrogate for Selected Model Responses](24-mmp-17---construct-a-surrogate-for-selected-model-responses.md) | Stable | surrogate; selected response; input region; approximation; correction; tail; refinement. Which cheaper construction can supply the model response the next operation actually needs? | MMP.11 for retained structure; CMP.7 and CMP.6 for learning and updates; MMP.14 for consequential mismatch; MMP.18 for coupled use. |
| 3 | [MMP.18 - Couple Models with Compatible Exchanges and Scales](25-mmp-18---couple-models-with-compatible-exchanges-and-scales.md) | Stable | coupling; interface; scale; conservation; closure; shared uncertainty; double counting. How can component models exchange quantities and information without changing the required joint answer? | A.3.3.TR and MMP.10 for joint conditions; MATH.18 for retained consequences; MMP.9 and MMP.17 for missing contributions; CMP.8 and CMP.14 for interacting computation. |
| 4 | [MMP.20 - Obtain a Computable Continuation When Physical Constraints Change](26-mmp-20---obtain-a-computable-continuation-when-physical-cons.md) | Stable | multimode DAE; changing constraints; consistent initialization; hot restart; mode-change array; impulse; event. How can a composed physical model continue when its active equations change? | MMP.18 for a joint model; A.3.3.TR for events and continuation; C.29.2 for effective computation; CMP.8 for numerical approximation; subject laws for the transition. |

## D. Compare and construct ways of working mathematically

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MMP.21 - Compare Interacting Operations through Mathematical Models](27-mmp-21---compare-interacting-operations-through-mathematical.md) | Stable | order; interaction; shared capacity; retained observation; composition; schedule; counterexample. Which arrangement preserves the receiving result, and what do its joint constraints permit? | MMP.10 for formulation; MMP.18 for exchanges; MATH.17 and MATH.18 for operations and preservation; C.32.MWA.PP for the practical comparison. |
| 2 | [MMP.22 - Construct a Way of Working through Mathematical Transformation](28-mmp-22---construct-a-way-of-working-through-mathematical-tra.md) | Stable | mathematical redesign; factorization; reordering; shared preparation; dependence; reusable rule. Which changed operations can realize the derived mathematical gain under the actual working requirements? | MATH.17 and MATH.18 for transformation; MMP.21 for comparison; C.39.RQ and C.32.MWA.PP for requirements and practical arrangements; A.3.1.MV for a Method variant. |

# Mathematical Modeling - Readme

## Practical entries

Bring the question you need a model to answer. It may concern an unexplained observation, a proposed intervention, a design, a prediction or the way work is performed. A useful result can be a relation that makes calculation possible, a conditional answer, a reason to reject a proposal or a more precise question.

The methods in this language work together through the results they produce. A formulation says which possibilities the model admits. An observation model says which records those possibilities can produce. Recovery and inference determine what can be learned from those records. An information-dependent choice uses the resulting distinctions only when they are available in time. A failed prediction can send the work back to the observing procedure, a model relation or the calculation.

Enter where the difficulty occurs and reuse results you already have. If the question is not yet mathematical, FPF B.5.FM helps choose participants and propose relations; B.5.TU helps interpret an unfamiliar theory. C.29 connects the construction with what it represents. For example, a cart's total distance does not determine its final position. Signed displacements and a starting position answer that question on a straight path; a question about visits along the way needs further information. Once the needed objects are recognizable, MMP.10 expresses their constraints; MMP.11 constructs a family when a relation remains unknown.

The worked connections below show how an intermediate result changes the next operation. Use the Table of Contents for other questions and the pattern bodies for the methods, prerequisites and further examples. FPF supplies shared reasoning methods; Mathematical Thinking supplies reusable mathematical constructions.

You can ask an assisting agent: “Explain the result and give feedback in the language of my work, without framework jargon.”


If a composed physical model cannot continue after a diode switches or a rope becomes taut, use [MMP.20](26-mmp-20---obtain-a-computable-continuation-when-physical-cons.md). Start with the old and new equations and the values inherited at the event. The result is a consistent next state and computable segment, or the specific physical law still needed. Its circuit and rope examples include executable code and show what changes when the impact law or event changes.

### MMP-OBSERVATION-TO-ACTION - Turn an observing model into a workable instruction

- **Situation:** A proposed way of working includes an observation followed by a decision, but their combined benefit is unclear.
- **Question:** What instruction can use that report, and which change to the work is worth making?
- **First useful result or blocker:** An instruction with its required information, timing and supported performance, or a contribution still needed before it can be used.
- **Start with:** [MMP.8](14-mmp-8---formulate-information-dependent-choices-mathematical.md) to formulate the choice; [MMP.7](16-mmp-7---construct-a-probability-model-of-the-recorded-data.md) when its reporting law is missing; B.1.5.CM when the observing and acting methods must be combined or changed.
- **Stop or return:** Use a sufficient instruction. A changed recording procedure reopens the observation model; changed timing, allowed choices or success requirements reopen the decision. Use C.11.DUA when the benefit of further inquiry is uncertain.

#### Worked connection for MMP-OBSERVATION-TO-ACTION

**A noisy report and a changed success requirement.** The observing and acting methods are examined together through [FPF B.1.5.CM](../../../sections/08-part-b---trans-disciplinary-reasoning-cluster/09-b-1-5-cm---construct-and-qualify-a-composite-method.md).

Start with what successful work means. In MMP.8:5.2, one of two requests needs a scarce resource, and allocation must follow a report. With perfect timely information, an instruction can follow the report. Without a distinguishing report, each fixed allocation fails in one admitted circumstance.

For the noisy procedure, MMP.7 supplies a necessary intermediate result. Two channels may produce the report, but the record does not identify the channel. Sum over that unrecorded choice to obtain the reporting law for each actual circumstance. MMP.8:5.2 performs this calculation: following the report succeeds with probabilities 0.8 and 0.7 in the two circumstances. No prior probability for which circumstance is actual is needed for those conditional results.

Now construct what can be done with that report. MMP.8 compares the four deterministic instructions on a two-valued report. A requirement of at least 0.65 success in each circumstance admits following it. A zero-failure requirement does not. Changing the requirement to average success, with one circumstance occurring with probability 0.95, makes always allocating to that request preferable among the four instructions. The preferred instruction changed because the question changed; the observing procedure stayed the same.

Return this answer to the proposed work. The report must be produced before allocation, and the receiving participant must be able to follow the instruction. If obtaining a better report costs more than the improvement is worth, C.11.DUA can support a sufficient existing choice or acceptance of the remaining risk. If the observation itself changes the situation, first represent that intervention through C.28.MR and derive the reporting and outcome laws for the changed situation.

B.1.5.CM:4.1 helps examine the proposed composition: what each method contributes, how the report reaches the acting participant, and which timing and support conditions the whole needs. Its result can be a supported composition or a proposal with unresolved conditions. Retain the resource demands and timing when revising the mathematical question. The useful result is a change the work can perform, a supported explanation of why the present method suffices, or the specific contribution still needed to choose.

### MMP-RECORDS-TO-ANSWER - Reach a usable conclusion from incomplete and noisy records

- **Situation:** A fitted model produces an answer, but ambiguity in the unknowns or in the observing procedure may change what that answer supports.
- **Question:** Which conclusion do the records warrant, and what must be revised when a consequential assumption fails?
- **First useful result or blocker:** An identifiable target and an inferential result with a stated meaning, or the unresolved difference that still changes its use.
- **Start with:** [MMP.7](16-mmp-7---construct-a-probability-model-of-the-recorded-data.md) for the record law, [MMP.12](17-mmp-12---formulate-an-inverse-problem-and-choose-whether-and.md) for recovery and ambiguity, [MMP.13](18-mmp-13---infer-unknowns-statistically-under-a-stated-observa.md) for inference, and [MMP.14](19-mmp-14---find-and-repair-a-mathematical-model-s-failed-predi.md) when a prediction needs repair.
- **Stop or return:** Use a sufficient result under its stated assumptions. Additional diagnostics or observations are needed only when they can change the warranted use. A changed target, recording rule or dependence returns to the contribution it affects.

#### Worked connection for MMP-RECORDS-TO-ANSWER

**1. Construct what can be observed.** Suppose two nonnegative contributions, u and v, produce only a total T=u+v in a measuring procedure. The task is to determine whether T is below 10.5 in the stated units. Initially the measuring practice supplies the model y_i=T+e_i for nine complete readings, with independent normally distributed errors of mean zero and known standard deviation 3. Their observed mean is 8.

MMP.7 turns that account into the joint law of the records. If a procedure instead discards readings outside a reporting range, its probability law must condition on that selection before the same inference can be attempted. MMP.11 is needed earlier if the relation between the unknowns and the observations has yet to be constructed.

**2. Ask what the law can distinguish.** MMP.12 examines changes that leave the records unchanged. Replacing (u,v) by (u+h,v-h), while both remain nonnegative, leaves T and the record law unchanged. No increase in the number of these total readings identifies the two contributions separately. The present target T remains identifiable, so its estimation need not wait for that unresolved decomposition. A question about u alone would require a restriction, another observation relation or a sufficient bound.

**3. Construct the claim needed for the decision.** Under the supplied law, MMP.13 gives the sample mean standard deviation 3/sqrt(9)=1. The rule “mean plus or minus 2” has about 95.45% repeated-sampling coverage for T. Applied here it gives [6,10]. Its upper end is below 10.5. Whether this is sufficient for the intended action depends on the consequence of a wrong answer and the accepted uncertainty; the interval itself supplies no permission to act. The confidence level describes the rule across repetitions, not a posterior probability for this realized interval.

This inference uses the total that MMP.12 found recoverable and the dependence assumptions that MMP.7 made explicit. A different requested claim, such as a posterior probability or the distribution of the next reading, needs the corresponding MMP.13 construction. A regularized split of u and v supplies neither of those claims.

**4. Recalculate after the observation premise changes.** An existing calibration investigation now establishes that all nine readings can share an unknown offset b, with |b|≤2. The measuring practice supplies this bound; a residual plot alone would not establish it. This changes the relation used by MMP.7 to y_i=T+b+e_i.

MMP.12 now exposes ambiguity between T and b. MMP.13 retains the interval for T+b and expands it over the admitted b values, giving [4,12] for T with at least the earlier coverage for each fixed admissible offset. The former threshold conclusion no longer follows. More repeated readings reduce the independent noise but do not determine b. A useful next move is a sufficient existing calibration bound, a qualified narrower answer or a different observation when its benefit warrants the work.

**5. Return to the question that will consume the result.** If an action must be selected despite the remaining uncertainty, MMP.8 formulates that choice using the information and timing actually available. If the question concerns changing the mechanism, FPF C.28 and C.28.MR identify the causal question and replacement: observing a variable at a value differs from forcing it to that value. MMP.15 then determines whether the available laws and causal assumptions identify the requested intervention consequence. An observational fit alone cannot supply that inference. If the original inferential answer is sufficient, the connection ends there.

If instead a consequential difference between predicted and observed records is the unresolved difficulty, MMP.14 compares them under the modeled conditions and helps locate the contribution to repair. A supplied change of premise, as in step 4, can return to the affected construction without that additional diagnosis.

The same joins support other observing procedures. Their general contribution is carrying a model's remaining ambiguity into the inference and its receiving use, then revising only the affected construction when an assumption changes.

### MMP-SUFFICIENT-ANSWER - Answer the working question before reconstructing every detail

- **Situation:** A model omits internal distinctions, and reconstructing them may cost more than the requested answer needs.
- **Question:** Which consequences are shared by the remaining possibilities, and do they already decide the question?
- **First useful result or blocker:** A bound that settles the stated threshold, or the distinction whose unresolved value still changes the answer.
- **Start with:** [MMP.9](23-mmp-9---derive-a-reduced-mathematical-model-of-state-evoluti.md) for lost evolution information; [MATH.20](../math/23-math-20---bound-a-mathematical-unknown-by-comparable-constru.md) for bounds; FPF C.29 for subject interpretation and C.11.DUA when further inquiry is a live choice.
- **Stop or return:** Use a settled answer under the supplied premises. A changed threshold, observation, law or time horizon returns to the affected comparison.

#### Worked connection for MMP-SUFFICIENT-ANSWER

**1. Make the receiving question specific.** A supplied account has two nonnegative populations with laws x'=-x and y'=-2y, where time uses the unit in which these rates are stated. The initial total is 1, but its split is unknown. Is the total remaining at time 3 below 0.1? This case starts with those laws; establishing a physical or other subject law is a different contribution.

**2. Recover the omitted contribution.** With z=x+y, MMP.9 gives z'=-x-2y. The same z=1 can have derivative -1 or -2, so the current total alone does not determine its rate of change. This result identifies the missing distinction and supplies alternatives for a bounding calculation.

**3. Derive an answer shared by those alternatives.** Put x(0)=a and y(0)=1-a, with 0≤a≤1. The equations give `z(t)=a*exp(-t)+(1-a)*exp(-2t)`. MATH.20 uses this convex combination to derive exp(-2t)≤z(t)≤exp(-t) for t≥0. At time 3, exp(-3)<0.05<0.1. The upper bound settles the question for every initial split. No estimate of a is needed for this answer.

**4. Return the consequence to the work.** C.29 asks what the populations, rates, total and threshold represent and which assumptions permit the interpretation. Under the supplied account, the condition is satisfied at time 3. Using that consequence in a real decision also uses the subject premises that made these equations applicable.

**5. Reopen what changes the answer.** Suppose the next question is whether z(1)<0.2. The bounds straddle 0.2. The same formula reduces the decision to a<(0.2-exp(-2))/(exp(-1)-exp(-2)), approximately 0.278. An available bound on a may settle this. Obtaining more about a is useful when it can change the decision enough to justify its cost; C.11.DUA helps make that choice. Changed evolution laws instead return to step 2, since the old enclosure may fail.

A different population or physical decay process can use this example when it supplies the stated laws and interpretation. The reusable connection is broader: reduction exposes a lost distinction, a mathematical comparison bounds its effects, and the receiving question decides whether those effects need further work.

### MMP-INTERVENTION-AND-INFORMATION - Decide whether an observation will improve the next action

- **Situation:** Several actions have different consequences in circumstances that the current record does not fully distinguish.
- **Question:** What can the available data establish about those actions, and is another observation worth obtaining before acting? When the observation supplies a training label, which request and continuation improve the rule's further use enough to justify their cost?
- **First useful result or blocker:** A justified action comparison and a contingent instruction, or an assumption, distinction or timing condition still needed.
- **Start with:** [MMP.15](20-mmp-15---identify-an-intervention-effect-from-available-data.md) to identify the intervention consequences; [MMP.16](22-mmp-16---design-observations-to-separate-mathematical-model.md) to compare obtainable information; [MMP.8.SD](15-mmp-8-sd---construct-a-sequential-decision-model-from-inform.md) when observing and acting form successive choices.
- **Stop or return:** Use the sufficient existing instruction when further information cannot repay its burden. A changed recording law, effect of observing or available action reopens the affected construction.

#### Worked connection for MMP-INTERVENTION-AND-INFORMATION

**1. Establish what the actions would do.** A service must choose response A or B. Its current circumstance is H0 or H1, each with supplied probability 0.5. Earlier randomized work recorded the circumstance and supplies the following population mean losses:

| Circumstance | Response A | Response B |
| --- | ---: | ---: |
| H0 | 0 | 4 |
| H1 | 10 | 0 |

MMP.15 makes the use of these records explicit. The case assumes consistent response versions, no interference, positive assignment probability for each response in each recorded circumstance, and transfer of the conditional intervention means to the current service. Under those assumptions, randomization identifies the means in the table. They are stipulated population quantities here; estimates from finite records would also need MMP.13's uncertainty.

Without another indication, A has expected loss 5 and B has expected loss 2. This supplies the comparison that any proposed observation must improve.

**2. Construct the record the proposed observation would supply.** A diagnostic report is positive with probability 0.8 in H1 and 0.2 in H0. It does not change the circumstance or the subsequent action losses. Within each circumstance, the report supplies no further information about response loss. Its cost is 0.2 in the same loss units, and the report arrives before the response is chosen. MMP.7 retains this reporting law, rather than treating a positive report as certain knowledge of H1.

**3. Compare information through its consequence.** MMP.16 obtains a posterior probability of H1 equal to 0.8 after a positive report and 0.2 after a negative one. Choose B after positive: its conditional expected loss is 0.8. Choose A after negative: its conditional expected loss is 2. Each report has probability 0.5, so expected action loss is 1.4. The information reduces that loss by 0.6; including its 0.2 cost gives 1.6 rather than 2.

**4. Construct the continuing instruction.** MMP.8.SD represents the first choice, whether to obtain the report, and the later response choice. For the response choice after the report, the posterior belief is sufficient: the conditional mean losses depend only on H and there are no later choices. The resulting instruction is to obtain the report, then use the branch above. The subject practice supplies actual observing and acting capabilities; C.32.MWA.PP connects those contributions to their performers and provision. If the report cannot arrive in time, formulate the response choice from the information that will actually be available.

**5. Revise only what changed.** Suppose the available diagnostic now has the same positive probability, 0.5, in both circumstances. MMP.7's new law leaves the belief at 0.5 after either report. MMP.16 returns zero information benefit for the response decision; MMP.8.SD chooses B without the diagnostic and avoids its cost. If observing instead changes the circumstance, include that transition and the changed intervention consequences before reusing the former calculation.

**6. Recover the comparison if the question changes.** A later inquiry may ask which cases would have benefited from the other response, rather than which response minimizes future expected loss. [MMP.19](21-mmp-19---construct-and-bound-a-mathematical-counterfactual-c.md) constructs the relation between a case's alternative responses. For an observed case, MMP.7 and MMP.13 first recover what its factual record implies about the underlying conditions; C.28.MR then changes the mechanism while retaining that case information.

Check what the available laws actually determine. In MMP.19:5.2, two models have identical action-specific success probabilities and identical randomized records, but give different answers about the same observed case under the other action. MMP.19 returns that ambiguity; a feasible observation is considered through MMP.16 only if it could resolve a useful distinction. Returning to the future expected-outcome criterion can make the unresolved same-case relation irrelevant. The earlier choice is then usable without that extra inquiry.

The connection can stop at a sufficient existing choice. The needed comparison determines whether to construct a report, a continuing instruction or a same-case counterfactual.


#### Obtain labels for a rule that will be used on further cases

The next action can be another query rather than the final subject action. Use this branch when examples are available without their labels and obtaining a label can improve a rule used on further cases. The result is a policy: which label to request now, what to do with each possible answer, when to request another, and what rule to use when questioning ends. Use an adequate existing rule without further labeling when it already serves the receiving work.

**Construct the query and its consequence together.** First name the cases on which the rule will be used, the response it must give and the loss of a wrong response. A query that reveals much about a rare case can be less useful than a less uncertain query that changes many consequential predictions. Learning a rule and estimating the accuracy of a fixed rule are also different purposes; the same selected labels need not serve both.

Recover what is observable before asking. In a pool, the unlabeled cases are already available; in a stream, rejecting a case may lose the opportunity to label it. A synthesized input may not be interpretable or labelable by the person answering. Specify the available answer, its reliability and delay, and the full cost of requesting it, including preparation and waiting. If asking changes the object, include that transition as in the diagnostic connection above.

[CMP.7](../cmp/15-cmp-7---construct-a-learner-from-examples-and-feedback.md) supplies an effective procedure for obtaining and updating the rule from examples. MMP.16 then compares requests through what that procedure and the receiving use would obtain. For each affordable candidate query, enumerate or otherwise model its possible answers, update the rule under each answer, and calculate the resulting loss on the receiving cases. Average over the answers that have not yet been observed; do not use the future true label as if it were available when selecting the query. Include the query's cost in the same comparison as acting now.

Choose the organization that is feasible:

- **One-step adaptive choice:** compare the next query assuming the returned rule is then used. Repeat after each actual answer if further queries remain possible. This uses feedback but can miss a query whose value lies in its continuation.
- **Conditional continuation:** use MMP.8.SD to compare the present query together with later choices contingent on its answers. Retain the remaining requests, resources, timing and other conditions that change those choices, not just the current probabilities.
- **Fixed batch:** choose a set before receiving its answers. This can avoid waiting between requests, but pays for every member and cannot skip one made unnecessary by an earlier answer. Evaluate the set jointly; the highest individual scores can select redundant cases.

The full comparison may itself be too costly. Uncertainty, disagreement among plausible rules, expected change in a rule and coverage of the receiving cases are possible cheaper indicators. They estimate different things. Use one because its relation to the present use and cost is adequate, not because “most uncertain” defines “most useful.” Retain a way to investigate plausible regimes omitted by a confident but inadequate model. Preparing a sophisticated policy is worthwhile only when its improvement can repay that preparation as well as the queries.

**A finite construction.** A service will classify 100 documents: 95 of observable type X and 5 of type Y. Each wrong classification takes one minute to correct. Three candidate rules assign the following labels, with supplied initial probabilities:

| Rule | Label for X | Label for Y | Initial probability |
| --- | ---: | ---: | ---: |
| h1 | 0 | 0 | 0.45 |
| h2 | 0 | 1 | 0.45 |
| h3 | 1 | 1 | 0.10 |

These are stipulated teaching premises, not estimates or a claim about actual documents. Exactly one rule is assumed true, every document of a type has that type's label, and the available specialist answers without error. Requesting X costs two minutes; requesting Y costs three. These are full costs. At most these two requests are available, and an answer can arrive before the next request and before classification. Acquisition does not alter the labels or subsequent correction costs.

Construct the learner by retaining the rules consistent with each answer and renormalizing their probabilities. For a type, predict the label with smaller conditional expected correction loss; choose label 0 if the losses tie. Applying the returned rule to the documents is distinct from computing these updates. If an answer leaves no consistent rule, this construction has failed its premises and must return to the model or answer account.

With no request, predict X as 0 and Y as 1. The expected correction time is

`95 × 0.10 + 5 × 0.45 = 11.75 minutes`.

Work backwards from the final classification choice. After each possible first answer, compare stopping with obtaining the remaining label. This constructs the value of a first request from its obtainable continuation rather than from its uncertainty alone.

| First request | Possible answer and update | Best continuation under the stated costs |
| --- | --- | --- |
| X | X=0 has probability 0.9, leaving h1 and h2 at 0.5 each. | X is settled. The expected remaining correction time for Y is 2.5 minutes. Learning Y costs 3, so stop and use the tie rule for Y. |
| X | X=1 has probability 0.1, leaving h3 alone. | Both labels are settled; stop. |
| Y | Y=0 has probability 0.45, leaving h1 alone. | Both labels are settled; stop. |
| Y | Y=1 has probability 0.55, leaving h2 at 9/11 and h3 at 2/11. | Unresolved X costs `95 × 2/11`, about 17.27 expected minutes. Obtain X for 2 minutes, then apply h2 after X=0 or h3 after X=1. |

Thus requesting X first costs `2 + 0.9 × 2.5 = 4.25` expected minutes in total. Requesting Y first with its conditional continuation costs `3 + 0.55 × 2 = 4.10`. Select Y first under these premises and costs.

This choice is not obtainable by treating every first request as the last. Y alone leaves 9.5 expected minutes of correction, so its total of 12.5 is worse than the original 11.75. A one-step comparison chooses X instead. A fixed batch of X and Y costs 5 and settles both labels, but purchases X even when Y=0 already identifies h1. The conditional policy saves that unnecessary request. These numbers compare the stated acquisition and correction costs; if constructing the policy adds material work, add that burden before adopting it over the simpler choice.

**Use the actual answer.** If the specialist returns Y=1, retain the updated probabilities 9/11 and 2/11, ask X, and apply the corresponding rule. If Y=0, apply h1 without another query. Record and use the answer actually obtained; a predicted branch is not evidence that its label has been received. If the answer arrives too late for another query, the conditional policy is unavailable. With only one request allowed and the other premises unchanged, choose X, whose total remains 4.25. A feasible alternative that returns both batch answers in time can still be compared at its full cost.

**Recalculate what changed.** Suppose the full price of Y rises from 3 to 3.2 minutes. The response probabilities do not change. The Y-first policy now costs `3.2 + 0.55 × 2 = 4.30`, while X-first still costs 4.25, so choose X first. Y remains the more uncertain answer, but that fact no longer selects the better policy. After X=0, stop with Y unresolved: its remaining expected correction time is 2.5, less than the cost of settling it. This is a sufficient economic choice for this use, not knowledge of every label.

Changed proportions of X and Y, correction losses, time available or permissible predictions likewise reopen the affected comparison. Repeating an already answered type adds no information under the noiseless, constant-label premises. Noisy or dependent answers require their actual likelihood and a new update; a second answer cannot be treated as independent merely because it is a second request. A later observation of X=1 and Y=0 contradicts every rule in the example. Check the labels and the type definition, then revise the family or the response model through MMP.14 rather than continuing to report a zero model risk.

**Keep stopping and further-use evidence distinct.** A stopping decision can mean that the present rule is adequate, that additional expected benefit does not repay its cost, or that resources are exhausted while a required result remains unresolved. Return which of these holds. A narrow cost comparison does not establish a broader required accuracy level.

The example's expected losses are conditional on its supplied class, probabilities and constant labels. They are not measured accuracy on actual future documents. For an empirical accuracy claim, use assessment cases and a justified uncertainty account suited to the receiving population. Keep them separate from cases used to fit, select or repeatedly tune the rule. The average error on adaptively requested labels is generally not the receiving population's average: requests were chosen for another purpose. MMP.13 preserves the selection and stopping law in an inference. If assessment is itself adaptive, use a method qualified for that design; an ordinary fixed-sample interval or a naive reweighting does not supply that qualification. MMP.17 supplies a related adaptive construction when queries obtain responses of a costly source model, while keeping agreement with that model distinct from agreement with the world.

[Settles's Active Learning Literature Survey](https://burrsettles.com/pub/settles.activelearning.pdf), §§2–4 and 6, develops query settings, alternative selection criteria and their practical limitations. [Huan, Jagalur and Marzouk](https://arxiv.org/html/2407.16212v1), §5, develop the distinction between fixed designs and policies that use intermediate observations. [Farquhar, Gal and Rainforth](https://sebastianfarquhar.com/assets/papers/farquharStatistical2021.pdf) show why correcting an adaptively selected risk estimate and improving the learned predictor are different questions. The construction here uses a small explicit family; it does not supply those papers' specialized estimators or guarantee improvement for arbitrary learned models.

### MMP-REPLACE-AND-COUPLE - Use cheaper models without losing the combined answer

- **Situation:** A required answer combines expensive model contributions, and cheaper replacements are available.
- **Question:** What must each replacement supply, and which errors or shared dependencies can change the combined result?
- **First useful result or blocker:** A sufficient coupled answer with propagated approximation limits, or the component contribution that still needs refinement.
- **Start with:** [MMP.17](24-mmp-17---construct-a-surrogate-for-selected-model-responses.md) for the replacement's target and use region; [MMP.18](25-mmp-18---couple-models-with-compatible-exchanges-and-scales.md) for the exchanged quantities and dependencies; MATH.20 for the needed bound.
- **Stop or return:** Keep a sufficient approximation. Return to the affected source model or interface when the bound no longer settles the question, or to MMP.14 when an observed discrepancy needs diagnosis.

#### Worked connection for MMP-REPLACE-AND-COUPLE

Two components contribute distinct amounts u and v to a total, in the same units and over the same interval. MMP.18 establishes that the required combination is u+v and that neither contribution already contains the other. MMP.17 selects surrogates for these two amounts on the input region being used.

For the present input, suppose their estimates are 0.42 and 0.48, with supported absolute error bounds 0.03 and 0.04. The resulting total is in [0.83,0.97]. It is below a threshold of 1 throughout that interval. No independence assumption is needed for this worst-case sum bound. Errors measured only on a few training cases would not, by themselves, supply the stipulated bounds.

Now lower the threshold to 0.94. The interval no longer settles whether the total is below it. If obtaining the second component from its source model is worthwhile, and that calculation returns 0.46 with absolute error at most 0.001, retaining the first surrogate gives [0.849,0.911]. That narrower combination settles the new question without replacing both surrogates.

A different question can instead change what the interface must carry. A time of threshold crossing needs information about evolution within the interval; two final amounts do not supply it. MMP.18 then returns the missing temporal contribution, and MMP.17 changes the response that a replacement must preserve. More accurate final amounts alone would answer the wrong question.

### MMP-REPRESENT - Why does counting the records overcount the assignments?

- **Situation:** A request can be left unassigned or assigned option 0 or 1. The data format uses a presence bit and an option bit.
- **Question:** Does counting the records count the intended assignments?
- **First useful result or blocker:** A representation with three possibilities per request, or weights that correct duplicate representations. When the presence bit is zero, either option bit denotes the same absent assignment.
- **Start with:** [MMP.10 - Construct and Revise a Mathematical Constraint Formulation](12-mmp-10---construct-and-revise-a-mathematical-constraint-form.md), especially :5.2. Construct a valid representation, then determine whether its multiplicities preserve the requested count or sampling law.
- **Stop or return:** Use a sufficient count or representation. Reopen the translation when requirements or the requested operation change; a representation adequate for finding an assignment can still distort counting.

---

## Files of this publication

Generated by the skill's splitter: one file per section, in reading order.


### Mathematical Modeling DPF Architectural Reference

- [MMP.Reference:1 - Problem frame - Make a mathematical question useful](01-mmp-reference-1---problem-frame---make-a-mathematical-questi.md) (14 lines)
- [MMP.Reference:2 - Problem and forces - Choose what the model must retain](02-mmp-reference-2---problem-and-forces---choose-what-the-model.md) (20 lines)
- [MMP.Reference:3 - Solution - Connect the contributions the question needs](03-mmp-reference-3---solution---connect-the-contributions-the-q.md) (80 lines)
- [MMP.Reference:4 - Archetypal Grounding - A report, an instruction and a changed question](04-mmp-reference-4---archetypal-grounding---a-report-an-instruc.md) (20 lines)
- [MMP.Reference:5 - Conformance Checklist - Can the result do its intended work?](05-mmp-reference-5---conformance-checklist---can-the-result-do.md) (13 lines)
- [MMP.Reference:6 - Common Anti-Patterns and How to Avoid Them](06-mmp-reference-6---common-anti-patterns-and-how-to-avoid-them.md) (10 lines)
- [MMP.Reference:7 - Consequences, biases and limits](07-mmp-reference-7---consequences-biases-and-limits.md) (10 lines)
- [MMP.Reference:8 - Architectural Rationale - Organize by model-forming operations](08-mmp-reference-8---architectural-rationale---organize-by-mode.md) (14 lines)
- [MMP.Reference:9 - Source use and currentness](09-mmp-reference-9---source-use-and-currentness.md) (10 lines)
- [MMP.Reference:10 - Relations to continued inquiry and work](10-mmp-reference-10---relations-to-continued-inquiry-and-work.md) (8 lines)
- [MMP.Reference:End](11-mmp-reference-end.md) (2 lines)

### A. Formulate the subject question

- [MMP.10 - Construct and Revise a Mathematical Constraint Formulation](12-mmp-10---construct-and-revise-a-mathematical-constraint-form.md) (199 lines)
- [MMP.11 - Construct a Mathematical Model Family from Known Relations](13-mmp-11---construct-a-mathematical-model-family-from-known-re.md) (210 lines)
- [MMP.8 - Formulate Information-Dependent Choices Mathematically](14-mmp-8---formulate-information-dependent-choices-mathematical.md) (204 lines)
- [MMP.8.SD - Construct a Sequential Decision Model from Information and Consequences](15-mmp-8-sd---construct-a-sequential-decision-model-from-inform.md) (296 lines)

### B. Infer, distinguish and revise

- [MMP.7 - Construct a Probability Model of the Recorded Data](16-mmp-7---construct-a-probability-model-of-the-recorded-data.md) (195 lines)
- [MMP.12 - Formulate an Inverse Problem and Choose Whether and How to Use Regularization](17-mmp-12---formulate-an-inverse-problem-and-choose-whether-and.md) (239 lines)
- [MMP.13 - Infer Unknowns Statistically under a Stated Observation Model](18-mmp-13---infer-unknowns-statistically-under-a-stated-observa.md) (290 lines)
- [MMP.14 - Find and Repair a Mathematical Model's Failed Predictions](19-mmp-14---find-and-repair-a-mathematical-model-s-failed-predi.md) (276 lines)
- [MMP.15 - Identify an Intervention Effect from Available Data](20-mmp-15---identify-an-intervention-effect-from-available-data.md) (339 lines)
- [MMP.19 - Construct and Bound a Mathematical Counterfactual Comparison under a Causal Model](21-mmp-19---construct-and-bound-a-mathematical-counterfactual-c.md) (218 lines)
- [MMP.16 - Design Observations to Separate Mathematical Model Alternatives](22-mmp-16---design-observations-to-separate-mathematical-model.md) (251 lines)

### C. Change the model while retaining its use

- [MMP.9 - Derive a Reduced Mathematical Model of State Evolution](23-mmp-9---derive-a-reduced-mathematical-model-of-state-evoluti.md) (231 lines)
- [MMP.17 - Construct a Surrogate for Selected Model Responses](24-mmp-17---construct-a-surrogate-for-selected-model-responses.md) (270 lines)
- [MMP.18 - Couple Models with Compatible Exchanges and Scales](25-mmp-18---couple-models-with-compatible-exchanges-and-scales.md) (251 lines)
- [MMP.20 - Obtain a Computable Continuation When Physical Constraints Change](26-mmp-20---obtain-a-computable-continuation-when-physical-cons.md) (375 lines)

### D. Compare and construct ways of working mathematically

- [MMP.21 - Compare Interacting Operations through Mathematical Models](27-mmp-21---compare-interacting-operations-through-mathematical.md) (284 lines)
- [MMP.22 - Construct a Way of Working through Mathematical Transformation](28-mmp-22---construct-a-way-of-working-through-mathematical-tra.md) (225 lines)
