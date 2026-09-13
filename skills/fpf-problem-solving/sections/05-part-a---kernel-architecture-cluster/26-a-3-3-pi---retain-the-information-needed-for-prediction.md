## A.3.3.PI - Retain the Information Needed for Prediction

> **Type:** Method pattern
> **Status:** Draft
> **Normativity:** Normative

### A.3.3.PI:1 - Problem frame

Use this pattern when a description of the present leaves a future result unresolved, or when you want to simplify a predictive account without losing an answer that matters. A total can hide components that change at different rates. A current readout can merge situations whose next outcomes have different probabilities. A summary adequate for the next output can lose information needed two steps later.

**First useful move.** Find two admitted situations that the proposed description treats as the same. Apply the supplied change rule under the same inputs and compare the future result needed by the question. If one kilogram of substance A becomes half a kilogram after treatment, while one kilogram of substance B becomes a quarter, the description “one kilogram remains” cannot determine the next total. It can still supply the range from a quarter to half a kilogram.

The Method constructs information sufficient for a stated prediction: additional state values, a usable history, a distribution over possible states or a bound that settles the question. Its result can also identify which missing distinction would change the answer. It connects the state, transition and observation contributions recognized by A.3.3.

The elementary cases require arithmetic, equations and conditional probabilities. More demanding models need their subject-specific estimation, reduction or computational Methods. The common task is to choose and use the retained information with the prediction it supports.

When an available prediction or bound already settles the working question, use it. When the missing contribution is a rule of change, A.3.3.TR helps construct that rule. The present Method applies when the retained information and the desired prediction need to be reconciled.

### A.3.3.PI:2 - Problem

A description can correctly report the present while omitting what determines its continuation. Recovering every underlying detail is often impractical, and a useful future distinction may require only a small part of that detail.

Adding observations does not automatically solve the problem. Their timing, the actions taken between them, measurement error and the assumed law determine what can be inferred. A fitted predictor can also work for one interval and accumulate consequential error when repeatedly applied.

The practical problem is to retain enough information for the future question, and to know what result remains obtainable when the available information supports only a range, a conditional probability or a shorter horizon.

### A.3.3.PI:3 - Forces

| Force | Tension |
| --- | --- |
| Compact description and predictive distinctions | Aggregation simplifies a model but can merge states that evolve differently. |
| Observation and model state | A reading reports some aspect of the situation; a prediction may need an unobserved quantity or a distribution over possible values. |
| Present values and history | A past observation can recover a missing distinction, while a long history can make computation expensive. |
| One result and repeated prediction | Information can determine one requested output without supplying a state that can be updated indefinitely. |
| Ideal recovery and measurement error | Algebra can reconstruct hidden values while amplifying errors in the readings used. |
| Additional information and usable uncertainty | A bound can settle a decision before identifying the actual underlying state. |

### A.3.3.PI:4 - Solution

Begin with the future distinction needed in the work. Compare the situations merged by the proposed description, construct a description or uncertainty account that retains the consequential differences, and use it at the required horizon.

#### A.3.3.PI:4.1 - Specify the future question and the available account

Name the quantity, event or choice being predicted, the horizon and the inputs over that horizon. Specify the accuracy or decision boundary when it changes what information is needed. Predicting a total after one treatment cycle, determining whether it will be below a limit, and estimating a long-run average can require different information.

Recover the rule of change, observation meanings, sampling times and available initial information. Separate uncertainty about the state from uncertainty about the rule or future input. A longer observation history cannot replace an unspecified intervention.

State what the proposed description retains: present readings, model coordinates, past inputs and outputs, derived features or weights over possible states. Where future actions are chosen by a controller, retain the action assumptions needed by the comparison.

#### A.3.3.PI:4.2 - Compare situations merged by the description

Construct two admitted states or histories with the same retained description. Keep the rule, input conditions and future question fixed. Derive their relevant continuations. A difference in the requested result identifies information lost by that description.

For a deterministic discrete model, let x be its state, u its input, F(x,u) the next state and z = r(x) the retained description. An update z' = G(z,u) is well-defined when r(F(x,u)) has the same value for every admitted x having the same z, for each input covered by the claim. This condition says how to construct G: choose any compatible x, apply F and retain r of the result. All compatible choices must give the same answer. C.29.1 supplies the general comparison of operations under a representation change.

A prediction of one selected output at a fixed horizon may need less information than an update of the entire retained state. Compare the output that the question asks for. If the result will be used repeatedly, also determine how to update the information from which the next prediction is made.

For a probabilistic model, compare the distributions of the relevant future result under the merged states or histories. The current readout can conceal different next-event probabilities even when the full model is Markov, as :5.2 shows.

One divergent pair refutes sufficiency for a claim covering both cases. Matching a few pairs supports only those comparisons. A general sufficiency claim needs an argument or subject Method covering its stated class; a local counterexample or conditional forecast may already be enough for the present work.

#### A.3.3.PI:4.3 - Choose the least costly useful repair

Use the missing distinction to choose a repair.

- **Retain additional state values.** Keep component amounts, velocity, operating mode, pending input or another variable whose difference changes the result. Include a way to obtain or estimate it in the intended use.
- **Retain relevant history.** Use observations and intervening actions to infer the missing state or construct a direct recurrence. Derive the needed history length from the rule and observation account where possible.
- **Retain an uncertainty account.** Carry the admitted state set or a distribution over possible states and propagate it through the rule. Use probability weights when a probability model is supplied.
- **Answer a weaker question that still serves the work.** A range, threshold decision or shorter-horizon result can be sufficient even when a unique future value remains unresolved.

Compare the available repairs by what they change in the decision and by their cost. C.11.DUA helps decide whether another measurement or calculation is worth obtaining. Use an already adequate bound directly.

A finite history can close some models, including the two-substance example. Other projections need a longer history, an approximate memory account or retained uncertainty. Choose the repair from the dynamics and the intended error, rather than assuming a fixed number of observations always reconstructs the state.

#### A.3.3.PI:4.4 - Construct the prediction and its update

For an algebraic reconstruction, solve the observation and change equations for the hidden values. Check the admitted domain and substitute the result back. Derive a recurrence if the next prediction will use a rolling history. Include how to discard old information and incorporate the next reading.

For a set of possible states, apply the change rule to that set under the admitted inputs, then use the observation relation to obtain possible outputs. A simpler enclosing interval can be enough for a threshold question. Keep the direction of the bound that makes the decision valid.

For a finite hidden-state probability model, let Pij be the probability of transition from state i to state j, and let pi be the current probability of state i given the observations and actions already used. First predict the next-state weights:

    predicted_pj = sum_i(pi * Pij)

When a new observation y arrives, multiply each predicted weight by the observation likelihood Lj(y), then divide by the sum of those products. For a discrete readout, Lj(y) is the probability of y in state j. For a continuous readout with a modeled density, use that density at y. Under the Markov and observation assumptions, the normalized weights summarize the history for the next prediction. Use the transition probabilities for the action actually taken when actions affect the model.

Supply the initial weights and observation likelihoods from the selected model. If the normalizing sum is zero, this update cannot supply posterior weights. Check the observation account, initial possibilities and numerical calculation before proceeding. The weights describe the current uncertainty about the modeled state.

For example, two equally weighted hidden states have Gaussian observation densities with means 0 and 1 and variance 1. An observation y=0 gives likelihoods proportional to 1 and exp(-1/2), so the first state's updated probability is 1/(1+exp(-1/2)), about 0.622. Using the probability of a single value would give zero for both continuous distributions and prevent this valid update.
A learned predictor offers another construction. Train or select it for the output, horizon, inputs and error that matter. A direct prediction several steps ahead and repeated application of an approximate one-step model can behave differently. Evaluate the intended use, including how the predictor receives the information available at each step.

#### A.3.3.PI:4.5 - Test the horizon, error and changing conditions

Work a case through to the requested future result. Include a pair merged by the simpler description when one motivated the repair. Identify which retained information now changes the calculation.

When readings are imperfect, propagate their stated uncertainty far enough to determine whether it changes the result. A reconstruction can amplify observation error even when the underlying equations have a unique solution. Parameter and input uncertainty require their own treatment; changing a sampling interval can change the update rule.

Check repeated use at its claimed horizon. A universally valid closed update can be iterated while its domain and input assumptions hold. A good fit over one observed step does not provide that result for an approximate predictor. Check the errors or bounds relevant to its use and shorten the horizon or change the account when needed.

Keep forecast performance and aggregate statistics tied to their questions. A model can reproduce a long-run average yet lose the history that changes the next-event probability. Conversely, a useful short-horizon predictor may not reproduce long-run behavior.

#### A.3.3.PI:4.6 - Return the prediction with the information needed to reuse it

Return the prediction, bound or unresolved distinction in the work where it is needed. Keep its observation meanings, inputs, horizon and consequential assumptions available in the calculation or explanation.

If additional information is worthwhile, identify the measurement, state distinction or model contribution that would change the answer. A result can be useful while the actual hidden state remains unknown. Reopen the affected comparison when the input policy, law, observation scheme or question changes, using B.5.MPC.R where several accounts must change together.

### A.3.3.PI:5 - Archetypal Grounding

#### A.3.3.PI:5.1 - Recover a treatment forecast from component masses or a short history

Let a_n and b_n be nonnegative masses in kilograms after n treatment cycles. Each cycle leaves half of the first substance and a quarter of the second, with no new material:

    a_(n+1) = a_n/2
    b_(n+1) = b_n/4
    y_n = a_n + b_n

The instrument reports only y_n. States (a_0,b_0) = (1,0) and (0,1) both report y_0 = 1 kg but give next totals 1/2 kg and 1/4 kg. The aggregate has lost the composition needed for a unique next total.

One repair retains the two masses and updates them separately. Another uses two successive readings without measurement error. From y_0 = a_0 + b_0 and y_1 = a_0/2 + b_0/4,

    a_0 = 4*y_1 - y_0
    b_0 = 2*y_0 - 4*y_1
    y_2 = (3/4)*y_1 - (1/8)*y_0

The recovered masses must be nonnegative, requiring y_0/4 <= y_1 <= y_0/2. For y_0 = 1 kg and y_1 = 0.35 kg, the masses are 0.4 kg and 0.6 kg, and y_2 = 0.1375 kg.

The recurrence applies at later cycles under the same law. A rolling pair (previous total, current total) can replace the hidden component values for predicting future totals. On receiving a new total, retain it and the former current total. If no new measurement arrives, the recurrence can propagate the pair as a conditional model prediction.

With only y_0, nonnegativity yields the bound

    y_0/4^n <= y_n <= y_0/2^n, for integer n >= 0.

For y_0 = 1 kg, the next total is at most 0.5 kg. This settles a requirement at most 0.6 kg without learning the composition. A limit of 0.4 kg remains unresolved by that bound.

Now suppose the two readings each have absolute error at most epsilon kilograms while the retention law is fixed. The reconstructed a_0 can err by at most 5*epsilon, and b_0 by at most 6*epsilon. The formula for y_2 has error at most (7/8)*epsilon from those two reading errors: add the absolute contributions (3/4)*epsilon and (1/8)*epsilon. At epsilon = 0.01 kg this gives 0.00875 kg. A marginal threshold decision must account for that interval; a recovered negative mass calls for checking the measurement uncertainty and the model assumptions.

If both substances instead have the same fixed retention factor r, the total obeys y_(n+1) = r*y_n. Composition is then unnecessary for predicting totals under that law. The needed information changes with the operations and the question.

#### A.3.3.PI:5.2 - Preserve predictive memory under a coarse readout

A modeled device has hidden states A, B and C, with fixed transition probabilities:

| Present state | Next A | Next B | Next C |
| --- | --- | --- | --- |
| A | 0.7 | 0.2 | 0.1 |
| B | 0.1 | 0.2 | 0.7 |
| C | 0.2 | 0.3 | 0.5 |

The readout is 0 in A or B and 1 in C. A current 0 leaves next-1 probabilities from 0.1 to 0.7, depending on the hidden state. A single value such as their unweighted mean would add an unsupported assumption about which state is present.

For this calculation, take the initial distribution to be the stationary distribution (19/54,13/54,22/54). After observing 1, the current state is C. Its next-state weights are (0.2,0.3,0.5). Observing 0 next removes C and gives current A/B weights (2/5,3/5). The probability of the following 1 is

    (2/5)*0.1 + (3/5)*0.7 = 23/50 = 0.46.

For the history 0,0, the first 0 gives weights (19/32,13/32,0). Apply the matrix, retain A and B after the next 0, and normalize. Their weights become (73/105,32/105), giving

    (73/105)*0.1 + (32/105)*0.7 = 99/350, about 0.283.

A decision that changes when next-1 probability exceeds 0.4 takes different actions after those histories. Keeping only the latest 0 with the stationary A/B mixture would give 11/32, about 0.344, and lose the relevant difference. The distribution conditioned on history is the useful retained information.

The same matrix also gives a long-run fraction of readout 1 equal to 22/54. This finite positive chain has the conditions for that ergodic average. The average answers an aggregate question; the conditional probabilities answer the next-event question.

Initial weights other than the stationary distribution can give different finite-history predictions. If only a current 0 is known and no mixture is justified, the range [0.1,0.7] remains available. A probabilistic estimate requires its initial and transition account.

#### A.3.3.PI:5.3 - Distinguish a next output from an updatable state

A processor emits and removes the head bit of a pending finite queue once per step. Two possible queues are (0,1) and (0,0). In both cases the next output is 0, so retaining the next bit answers the immediate output question.

After emitting that bit, the next outputs are respectively 1 and 0. The retained next bit cannot update itself without information about the remaining queue. To predict the next two outputs, retain both pending bits. To keep predicting after later steps and arrivals, retain the relevant queue and arrival account, or a summary proved adequate for the selected output question.

The difference is between knowing one output and carrying information that can be updated for further prediction. A description can be economical and sufficient for a short task. Increasing the horizon changes the information it must supply.

### A.3.3.PI:6 - Bias-Annotation

The elementary cases use known change rules and small descriptions. A learned or partially known model can require a separate account of law uncertainty, data coverage and approximation error. A small hidden-state example makes probability updating easy to inspect; larger state spaces can require approximate filtering or bounds.

Observability and useful predictability can also diverge. Identifying every hidden quantity may be difficult while a required output remains tightly bounded. Choose the result from the working question and the information that can economically affect it.

### A.3.3.PI:7 - Conformance Checklist

- **CC-A3.3.PI-1 - Future question.** The output, event or decision, horizon and consequential input assumptions are recoverable.
- **CC-A3.3.PI-2 - Retained information.** The description identifies the state values, observations, history, features or weights used in the prediction.
- **CC-A3.3.PI-3 - Lost distinction.** The comparison keeps the rule and inputs fixed and identifies whether merged situations can change the requested result.
- **CC-A3.3.PI-4 - Usable construction.** The additional state, recurrence, uncertainty propagation or weaker answer supplies the claimed prediction or identifies what remains unresolved.
- **CC-A3.3.PI-5 - Probabilistic account.** A probability claim supplies the initial, transition and observation assumptions it uses.
- **CC-A3.3.PI-6 - Scope and error.** A sufficiency or performance claim is supported over its stated cases and horizon, with consequential observation and approximation error accounted for.
- **CC-A3.3.PI-7 - Repeated use.** Repeated prediction supplies an update of the retained information or a predictor covering the intended horizon.
- **CC-A3.3.PI-8 - Worthwhile return.** The result changes the calculation or decision; further information is sought when its expected contribution warrants the work.

### A.3.3.PI:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Why it matters | Repair |
| --- | --- | --- |
| Use an aggregate as a predictive state without comparing its merged cases | Components or hidden modes can produce different continuations. | Compare those cases and retain their relevant distinction or output range. |
| Substitute a long-run average for a history-conditioned forecast | A decision about the next event can depend on recent observations. | Condition on the available history or retain its predictive distribution. |
| Turn a recovered value into a measurement without carrying its assumptions | Algebraic reconstruction can amplify errors and depends on the supplied law. | Propagate the reading uncertainty and inspect the admitted domain. |
| Repeat a one-step predictor beyond its supported use | Prediction error can accumulate, or the retained output may lack its own update. | Construct an adequate state update or a predictor for the required horizon. |
| Keep a longer history without the intervening inputs | Similar observations can follow different actions and call for different forecasts. | Retain the actions that enter the transition account. |
| Obtain a full hidden-state estimate after a bound has settled the question | The extra work adds cost without changing the present choice. | Use the bound and reopen the distinction when another question needs it. |

### A.3.3.PI:9 - Consequences

The reader can simplify a predictive account while preserving the relevant future distinction, recover missing information from history, or act using a useful bound. The construction also makes visible why a changed horizon, law or observation scheme can require a different description.

The result is relative to its supplied model, observations and use. More retained information can increase storage, estimation and computational cost, and reconstructed quantities can be sensitive to measurement error.

### A.3.3.PI:10 - Architectural Rationale

The independently useful result is a description or uncertainty account that supports a prediction. Configuration construction determines compatible values; rule construction relates their changes. Prediction-information work asks which distinctions from those accounts must remain available for the future question.

That question is shared by physical measurement, mathematical reduction and computational state design. The common construction compares merged cases and repairs a consequential loss. Subject Methods supply physical laws, observability results, estimation techniques and efficient approximations.

A present model state, an observed value, a history and a distribution conditioned on observations carry different information. Keeping their roles explicit permits a compact predictor without claiming that its retained values identify every physical detail. A short-horizon output and an iteratively updated predictive state are also different useful results.

### A.3.3.PI:11 - SoTA-Echoing

The working question is to obtain a useful future result from the available observations and change law. **Selected approach:** retain the distinctions needed by that result, together with their update or uncertainty. **Serious alternative:** reconstruct and carry the full model state. Full-state recovery supports a broader range of subsequent questions and is convenient when those values are already available. It can require extra measurement, estimation or storage when only an aggregate is observed.

Compare the alternatives for the same law, observations, inputs, horizon and decision, including the preparation needed to use each. In :5.1, a one-total upper bound already settles the 0.6 kg limit; reconstructing composition would require information that cannot improve that decision. For a unique forecast, two available totals support a rolling recurrence. In :5.2, a distribution over hidden states supports the history-dependent forecast without identifying the actual hidden state. That filter costs more than retaining the current readout alone, whose merged histories lose the decision-changing probability. These are chosen information and computation trade-offs, derived in the cases rather than measured as a general efficiency gain.

**Reduction and memory.** Lin and Lu's [Data-driven model reduction, Wiener projections, and the Koopman-Mori-Zwanzig formalism, §§2.1-2.3](https://arxiv.org/html/1908.07725v5) separates forecasting from long-time statistics and exposes memory after projection. **Adapt:** :4.1-:4.3 fix the output and horizon, compare merged states, and choose retained state, history or uncertainty. The projection identity needs a closure construction to become an economical predictor; the elementary mixture and its bounds in :5.1 are authored.

**Filtering a hidden state.** Poole and Mackworth's [Artificial Intelligence: Foundations of Computational Agents, third edition, §§9.6.2-9.6.3](https://artint.info/3e/html/ArtInt3e.Ch9.S6.html) derives filtering under Markov transition and observation assumptions. **Adopt:** :4.4 and :5.2 propagate state weights, incorporate the observation likelihood and normalize. [Section 9.1.1](https://artint.info/3e/html/ArtInt3e.Ch9.S1.html) distinguishes probability masses and densities; :4.4 keeps that distinction for discrete and continuous readouts. The resulting distribution summarizes the history for the supplied model. Learning the model or approximating a larger state space requires further Methods.

**Finite-chain forecasts and averages.** [Cambridge's Markov Chains notes, §§9-10](https://www.statslab.cam.ac.uk/~rrw1/markov/M.pdf) distinguish distribution convergence and ergodic averages. **Adopt:** :4.5 and :5.2 preserve their different questions. The three-state matrix, histories and threshold comparison are authored. Stationary initial weights are used only where stated; the positive finite chain supports the illustrated long-run average.

**Prediction at the intended horizon.** De Jong, Breschi, Schoukens and Lazar's [Koopman Data-Driven Predictive Control with Robust Stability and Recursive Feasibility Guarantees](https://arxiv.org/html/2405.01292v1) constructs multi-step predictors from past inputs and outputs and addresses errors from iterated approximate one-step dynamics. **Adapt:** :4.4-:4.5 compare the predictor at its intended horizon and input policy. The paper's controller guarantees require its specialized construction; the present Method adopts the comparison question, not those guarantees for every predictor.

The common procedure is a conceptual synthesis. Reopen its comparative choice when another description or estimator answers the same question under the same available observations, reader preparation and acceptable error at lower cost, or when a changed law, input policy or consequential prediction failure exposes a distinction it lost. Delay reconstruction, observability, filtering, system identification and model reduction then supply concrete alternative constructions.

### A.3.3.PI:12 - Relations

- **A.3.3 - U.Dynamics** distinguishes the state, transition and observation contributions used in this prediction.
- **A.3.3.CC** constructs compatible configurations; **A.3.3.TR** constructs the rule of change used to compare their continuations.
- **C.29.1** compares operations across mathematical representations; **C.29.2** constructs and judges computations at their intended use.
- **C.16** supplies the observation relation and consequential measurement uncertainty.
- **B.5.MPC** connects physical, mathematical and computational contributions; **B.5.MPC.R** revises them when the question changes.
- **C.11.DUA** selects additional information by what it can improve in the working decision.

### A.3.3.PI:End
