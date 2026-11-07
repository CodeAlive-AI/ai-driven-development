## MMP.16 - Design Observations to Separate Mathematical Model Alternatives

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative within the stated use

### MMP.16:1 - Problem frame

Use this pattern when several mathematical accounts remain possible and the next useful answer depends on a difference between them. You can choose which cases to observe, under which conditions, or how to record them. The difficulty is to find an attainable observation that exposes the relevant difference.

The desired result may be a better decision, a supported prediction, a distinction between proposed mechanisms, or a new research direction. For example, two response laws agree at all previously tried inputs but imply different behavior in the intended use. Repeating those inputs more accurately may leave the disagreement untouched.

This pattern constructs the mathematical design of an observation. It returns what to observe, what records the alternatives would produce, and how those records would change the answer. It can instead return a useful limitation: the available observation choices leave the needed distinction unresolved. The subject practice supplies feasible access and performs the observation; PHY.9 and PHY.10 do that work for a physical readout and test.

Start with the receiving question, the alternative models and the observation law from MMP.7. Set-valued reasoning needs functions and sets. Probabilistic design also needs conditional probability and the inferential meaning chosen in MMP.13. An analyst can supply that mathematics while another participant supplies the observing conditions and interprets the result.

Use the present answer directly when the remaining alternatives make no consequential difference. A new observation is only one possible response to uncertainty. C.11.DUA supplies the comparison with using what is already known, changing the claim or taking another feasible step. A routine prescribed measurement with an already sufficient design needs no new design study.

### MMP.16:2 - Problem

A model can predict a large difference that the actual record cannot show. An instrument may saturate, a log may aggregate away timing, or an unknown offset may account for the apparent difference. Conversely, overlapping distributions can still support a useful distinction; requiring one observation to identify the model without error can reject worthwhile designs.

An observation can also be highly informative about something irrelevant to the requested result. Choosing a design by parameter uncertainty, fit or model label can therefore direct effort away from the question that made the modeling useful.

The problem is to construct a feasible observation whose possible records support a consequential comparison, with the uncertainty and cost that this use can tolerate.

### MMP.16:3 - Forces

| Force | Tension |
| --- | --- |
| Visible contrast and recorded contrast | Models can disagree about an unobserved quantity while predicting the same available record. |
| Model identity and receiving result | Different models may support the same answer; a single model family may contain the important disagreement. |
| Discrimination and uncertainty | One certain separating observation is attractive, but useful statistical distinctions often retain error. |
| Informative design and model adequacy | A design can be excellent within an inadequate model family. |
| Learning and available work | A better distinction can cost more time, access or computation than its contribution warrants. |
| Immediate gain and continued inquiry | One observation may prepare a later useful test without answering the final question itself. |

### MMP.16:4 - Solution

State the disagreement that matters. Derive the records each alternative can produce under feasible observation choices. Construct a comparison of those records that improves the receiving answer, and compare the attainable benefit with the work involved. Obtain the selected observation only when that comparison supports it; otherwise use the present result or change the question or access.

#### MMP.16:4.1 - Locate the consequential disagreement

Write the answer that would differ. It may be a threshold response, a predicted event, an intervention consequence or which conjecture to develop next. For a numerical target, write it as q(h,theta), where h selects a model and theta contains its remaining unknowns. Different theta within one model can matter as much as different model labels.

Recover what the present observations and assumptions leave possible. MMP.11 constructs the family of models; MMP.12 exposes a recovery ambiguity; MMP.13 supplies probabilistic conclusions when used. Group equivalent parameterizations by the behavior relevant to this question.

Ask which remaining disagreements change the intended answer or a worthwhile later inquiry. If all retained alternatives already support the same sufficient answer, return it.

#### MMP.16:4.2 - Construct the law of the obtainable records

Let d denote a feasible design: the selected inputs or cases, preparation, observing times and recording procedure. For each alternative derive either:

- a set R(h,theta,d) of possible records under its bounded uncertainties; or
- a probability law P(Y | h,theta,d) for the records Y.

The record includes what the procedure would actually retain. Compose the modeled response with the selection, measurement, censoring, rounding or aggregation operation. If an intervention changes the subject, derive its response under that intervention; an observational association alone supplies no such law.

Keep unknowns shared across readings shared. An unknown calibration offset cannot take one arbitrary value for the first reading and an unrelated value for the next if the same offset governs both. A repeated observation can reduce independent noise while leaving that common ambiguity intact.

A probabilistic comparison integrates unknowns only under a supplied probability law. Otherwise retain them as conditional possibilities or compare performance across their admitted range. Choosing a convenient nuisance value separately for each model can make a design look more discriminating than it is.

For an adaptive design, later observation choices are functions of records already available. Derive their joint law with that dependence. A sequence of fixed-design calculations does not by itself describe an outcome-dependent stopping or sampling rule.

#### MMP.16:4.3 - Find what a design can distinguish

First seek a simple consequential contrast. For a set-valued model, take the union of R(h,theta,d) over the remaining possible theta. Disjoint unions for two alternatives give a separating observation under those assumptions. If the unions overlap, identify records that would settle the needed distinction and records that would leave it open.

Equal sets alone do not establish equal statistical information: probability laws can weight the same possible records differently. In a probabilistic model, compare the full record laws or a statistic whose retained information suffices for the requested result. Distinct means are one possible contrast, not a universal criterion.

An impossibility conclusion needs its scope. Two alternatives that give the same record law under every currently feasible design, yet different required answers, demonstrate a distinction unavailable through those designs. More repetitions under the same uninformative access do not resolve it. Changing the observation type, access or target may do so. Failure of a numerical search to find a good design establishes only that search result.

A narrower target can remain obtainable. Suppose all feasible records leave the individual parameters unresolved, but every compatible parameter pair gives the same total response. Return the total when it answers the work question. Recovering each parameter is then unnecessary.

#### MMP.16:4.4 - Construct the design criterion from the receiving use

For a required distinction with controlled statistical error, construct a rule T(Y) that returns the answer or an unresolved result. For example, let two specified hypotheses have record densities p0(y;d) and p1(y;d) relative to the same measure. For a chosen threshold c, the rule selects H1 on the region A={y: p1(y;d)>c\*p0(y;d)} and H0 otherwise. Calculate P0(A), the chance of selecting H1 under H0, and P1(A-complement), the opposite error. Compare designs and thresholds that meet the required error bound. For a composite hypothesis, the claimed protection across its parameter range requires controlling the error across that range, rather than only at a fitted value.

Other decision rules can retain an unresolved answer when that is useful. Their comparison likewise follows from their record laws and the error consequences the use requires.

When probability, actions and losses are appropriate, let pi be the current joint law of the unknowns, a an available action, and L(a,h,theta) its loss. For a finite set of action choices and an observation that changes information alone, compare:

~~~
R0 = min_a E_pi[L(a,h,theta)]

R(d) = E_Y[min_a E[L(a,h,theta) | Y,d]]

value of sample information = R0 - R(d).
~~~

The inner choice uses the observed record; the outer expectation averages records that are still unknown when the design is chosen. In this formulation the recipient can ignore the record and retain the old action, so R(d) cannot exceed R0 under the same model. Subtracting the full cost of obtaining and using the information can still make the proposal unattractive. :5.2 carries out the calculation.

If the experiment itself changes the state, available actions or their consequences, include those effects in the decision model. The simple information-only comparison above is then insufficient. MMP.8.SD constructs the continuing state, information and consequence model.

An information criterion is another branch. For a selected unknown Q, expected information gain is the mutual information I(Q;Y | d) under the supplied joint law. Choosing Q as the model label, all parameters or a wanted prediction defines different design problems. Use this criterion when resolving that uncertainty serves the stated inquiry. It does not measure every practical consequence of the observation.

The comparison need not be a probability calculation. A guaranteed separation, an ordinal improvement, or a change in attainable answers can suffice. Use the existing FPF choice and portfolio methods when several gains and burdens remain incomparable. This pattern supplies the modeled observation consequences, not a new general system for valuing research.

#### MMP.16:4.5 - Construct and compare attainable designs

Use the contrast to generate alternatives: observe where responses differ, resolve an omitted component, vary an input independently, measure at a different scale or time, or change how the record is made. Derive the resulting record laws before optimizing a convenient proxy.

For a small set of designs, calculate the selected criterion directly. For a large set, use the applicable search or numerical method from Computational Thinking. Count the cost of evaluating a design as part of the work. If approximate criteria cannot reliably order close candidates, return that uncertainty, retain several designs, or refine the calculation where a changed ranking matters.

Compare against using current information. C.11.DUA governs the attainable contribution, delay, displaced work and any disputed evidence demand. When an information-only design has a bound on its possible benefit below its cost, that bound can end the comparison without computing its criterion more accurately.

For a sequence of observations, decide whether the immediate comparison represents the intended horizon. An apparently uninformative first step may enable a later separating observation. Construct that continuation with MMP.8.SD when it changes the choice; do not require a full sequential optimization for a sufficient one-step design.

#### MMP.16:4.6 - Use the result and reopen the implicated assumption

Return enough for the observation to be performed and interpreted: the selected conditions, records to retain, comparison rule, and the consequence of an unresolved or conflicting result. A design calculation remains a prediction about possible records; it is not an observation already obtained.

After observing, use the inference and comparison that match the actual procedure. If access, stopping or recording changed, revise the affected law before interpreting the result. For example, replacing a numerical readout by a threshold alarm changes the available distinction.

Model discrimination compares the alternatives supplied. If every alternative fails to explain an important record, MMP.14 returns to the relevant subject or observation assumption. Selecting the least poor alternative can support a limited approximation, but its winning score alone does not establish adequacy.

Where the intended use covers different conditions from the selected observations, carry that difference into the receiving prediction. Recent work on active learning under model misspecification shows why concentrating observations for parameter information can worsen prediction elsewhere. Compare alternative observation regions or model families when this vulnerability can change the design or receiving prediction.

### MMP.16:5 - Archetypal Grounding

The cases use stipulated models and costs so that the design can be reconstructed. They demonstrate the method.

#### MMP.16:5.1 - The largest response difference disappears in the readout

A team has two candidate response laws for a calibrated device assumed valid over the input range 0 to 2:

- H1: y=x;
- H2: y=x^2.

Both agree at the previously inspected inputs 0 and 1. The team needs to know whether the modeled response at x=2 is below or above 3. The laws answer differently: 2 and 4. Their applicability across the range is an assumption supplied for this case.

With a numerical readout r=y+e and a known error bound -0.1 <= e <= 0.1, the design x=2 gives:

| Design | H1 records | H2 records | Consequence |
| --- | --- | --- | --- |
| x=2, numerical readout | [1.9,2.1] | [3.9,4.1] | Disjoint intervals separate the alternatives. |

Now recover a missed feature of the actual instrument: it saturates at 1. Its record is r=min(1,y+e). At x=2 both alternatives always record 1. The large latent response difference gives no distinction at all.

Changing the input to x=0.5 yields:

| Design | H1 records | H2 records | Consequence |
| --- | --- | --- | --- |
| x=0.5, saturating readout | [0.4,0.6] | [0.15,0.35] | Both ranges lie below saturation and are disjoint. |

This design separates the supplied alternatives without replacing the instrument. A record 0.27 retains H2; a record 0.52 retains H1. A record 0.37 fits neither under the given error bound, so it reopens the response or observing assumptions rather than forcing a label.

The result at x=0.5 supports the answer at x=2 through the supplied response families. If those families were justified only up to x=1, this design would not establish the requested extrapolation. The next work would concern that range extension or access to a suitable direct observation.

If the only available inputs were 0 and 1 and the record error law were the same under both accounts, the available designs would not separate them. That conclusion concerns the stated access; it does not say the response question is unanswerable under every possible instrument.

#### MMP.16:5.2 - A useful signal is still too costly

A service team must choose one of two recovery procedures. It models two possible failure modes H0 and H1 with current probabilities 0.5 each. The loss is remaining recovery time, in hours:

| Procedure | H0 | H1 |
| --- | --- | --- |
| A | 0 | 10 |
| B | 4 | 0 |

With current information, expected losses are 5 for A and 2 for B. The team chooses B.

A proposed diagnostic produces either "+" or "-". Its supplied law is P(+ | H1)=0.8 and P(+ | H0)=0.2. Each signal has marginal probability 0.5. Bayes conditioning gives P(H1 | +)=0.8 and P(H1 | -)=0.2.

After "+", A has expected loss 8 and B has 0.8, so the team chooses B. After "-", A has expected loss 2 and B has 3.2, so it chooses A. Expected loss with the signal, excluding diagnostic cost, is therefore:

~~~
R(d) = 0.5*0.8 + 0.5*2 = 1.4 hours.
R0 - R(d) = 2 - 1.4 = 0.6 hours.
~~~

If obtaining, interpreting and waiting for the diagnostic adds 0.7 hours to recovery, its total expected loss is 2.1 hours; using current information is better under these conditions. At an all-inclusive cost of 0.2 hours, the diagnostic gives 1.6 hours and improves the choice. The example assumes the diagnostic does not change the failure mode or the two procedures.

A different test might reveal a device identifier perfectly. If that identifier is independent of the failure mode and losses in this model, its information gain about the identifier does not reduce this recovery loss. Selecting all available uncertainty as the target would misdirect the design.

Now change the current probability of H1 to 0.95. The "-" posterior is 0.19/(0.19+0.04), approximately 0.826, and the "+" posterior is 0.76/(0.76+0.01), approximately 0.987. B remains the better procedure after either result. The diagnostic still changes beliefs about the mode, but its sample-information value for this particular choice is zero.

A later method-development investigation could use the same signal for another target, such as learning how failure modes arise. That research value needs its own question and horizon; the zero above applies to the specified recovery choice.

### MMP.16:6 - Bias-Annotation

The worked cases make the candidate models and observing conditions unusually explicit. In practice, deriving the record law can be the hardest contribution. The mathematical design must retain uncertainty about that law rather than quietly treating a convenient simulator as the subject.

A small named model set also favors choosing a winner. Keep the possibility that all proposed accounts fail the receiving use. Conversely, do not turn that possibility into a demand for an unlimited search for alternatives: pursue it when a discrepancy or consequential vulnerability makes it useful.

### MMP.16:7 - Conformance Checklist

A constructed design supports its intended use when:

- the remaining disagreement and the answer it could change are identifiable;
- its predicted records follow from the alternatives and the actual selection and recording procedure;
- shared unknowns and adaptive choices retain their dependencies;
- the claimed separation, error property or expected improvement follows from a reconstructible comparison;
- any criterion based on information names the unknown being learned and its receiving use;
- feasibility and burden are compared at the scope needed for the decision, using present information as an available alternative;
- the result explains how the selected records change the answer and when an incompatible record returns to the model or observation assumptions.

These conditions concern the mathematical design and its stated assumptions. They do not establish that the observation was performed, that its subject assumptions hold, or that access is authorized. Stronger assurance belongs to the actual intended use.

### MMP.16:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Maximize a difference before deriving the record | Saturation, selection or aggregation can erase it | Compare the obtainable records, as in :5.1 |
| Demand disjoint supports for every useful test | Discards informative but uncertain observations | Construct the required error or decision comparison |
| Average away an unknown without a probability basis | Hides the assumption deciding which design looks best | Retain conditional cases or supply the probability law |
| Maximize information about every model parameter | Can favor learning that leaves the receiving question unchanged | Select the target or consequences that matter |
| Treat the best candidate as an adequate account | A closed comparison can select a poor explanation of the subject | Use a consequential mismatch to reopen the family |
| Require new data whenever models disagree | Spends effort even when the answer is already sufficient | Compare with the attainable use of current information |
| Interpret an adaptive sample as if it were fixed in advance | Can invalidate the claimed uncertainty or error property | Derive the law for the actual choices and stopping rule |

### MMP.16:9 - Consequences

The next observation becomes a constructed part of modeling: a specified change in available information with a stated consequence. A no-separation result can redirect effort from repeated measurement to a different readout, access route or question.

Good designs depend on assumptions about records and their use. A computed optimum can change when the observer, cost, model family or research horizon changes. For expensive searches, a sufficient feasible design may be more useful than a more precisely optimized proposal.

In methodology, the same construction helps compare alternative accounts of a working method. Choose a case or observation that makes their consequential disagreement visible. Human and automated procedures can both be studied this way; the subject method supplies what can be changed and observed.

### MMP.16:10 - Architectural Rationale

The general contribution is the construction of discriminating observations from models and their receiving use. It is separate from performing a physical test, deriving an estimator after observations, or choosing among all possible projects.

Separating the predicted response from its recording prevents a mathematical contrast from being mistaken for an observable one. Separating information from decision consequence lets exploratory research retain its own value while avoiding an automatic demand for more evidence in ordinary work.

The deterministic and probabilistic branches share that construction. Their guarantees differ, so the pattern does not reduce every use to one statistical test or one information metric. Existing FPF choice, resource and improvement methods receive the consequences produced here.

### MMP.16:11 - SoTA-Echoing

**Design according to its goal.** Huan, Jagalur and Marzouk, *Optimal experimental design: Formulations and computations* (Acta Numerica, 2024), §2.2 and the goal-oriented and model-discrimination formulations, distinguish information targets and decision utilities. The adopted contribution is the explicit selection of what an observation should improve in :4.4. A design maximizing information about every parameter is a serious default when that is the actual aim; it is replaced when the receiving target differs. Numerical optimization methods are delegated to the applicable computational construction. [Source](https://arxiv.org/html/2407.16212v1).

**Information that can change a decision.** Heath and colleagues, *Simulating Study Data to Support Expected Value of Sample Information Calculations: A Tutorial* (2022), “Background and Notation,” gives the pre-observation comparison of decisions after possible records. Its loss-form equivalent is used in :4.4 and the original recovery example in :5.2. The model's costs and consequences must describe the receiving work; the source's health-economic conventions are not generalized into mandatory monetary valuation. [Source](https://journals.sagepub.com/doi/10.1177/0272989X211026292).

**An informative design can misdirect learning.** Tang, Sloman and Kaski, *Representative, Informative, and De-Amplifying: Requirements for Robust Bayesian Active Learning under Model Misspecification* (arXiv v2, 2026), §§2–4, studies prediction under a fixed, potentially inadequate model family. Its analysis separates approximation error, estimation error and their interaction under the intended input distribution. This motivates the explicit receiving conditions in :4.6. Their proposed acquisition rule is not a universal remedy: its assumptions and quantities need their own justification before use. The adopted general move is to compare consequential model inadequacy and observation placement, rather than assuming that higher information gain implies better prediction. [Read version](https://arxiv.org/html/2506.07805v2).

These sources develop statistical branches. The bounded-error construction in :5.1 is an elementary set-valued derivation; it needs no prior distribution. Reopen the selected design when the target, record law, feasible access, receiving population or substantive model alternatives change. A newer optimization technique matters when it improves that same construction at worthwhile effort.

### MMP.16:12 - Relations

- **MMP.7** constructs the law of what is recorded; **MMP.11** constructs the admitted model family.
- **MMP.12** exposes recovery ambiguities; **MMP.13** supplies inference and uncertainty claims that match the chosen observation procedure.
- **MMP.14** investigates failed predictions and returns to the implicated subject or observation assumption.
- **MMP.15** supplies causal identification when the target is an intervention effect. A new association does not by itself identify that effect.
- **MMP.8** formulates the receiving choice; **MMP.8.SD** constructs a longer observation-and-action sequence when continuation changes the design.
- **C.11.DUA** appraises an evidence demand and its attainable contribution; **C.11** and the applicable portfolio methods compare attainable gains with resources and other consequences.
- **C.16.IR** supports a sufficient answer despite unresolved distinctions. **B.5.TC** relates a test to the theoretical comparison it is meant to change.
- **PHY.9** constructs a physical readout and **PHY.10** a physical test. Other subject practices realize the corresponding access and observation.
- **Computational Thinking** supplies the selected search, sampling or approximation procedure. **MMP.17** consumes an informative-case design when constructing a surrogate.

### MMP.16:End
