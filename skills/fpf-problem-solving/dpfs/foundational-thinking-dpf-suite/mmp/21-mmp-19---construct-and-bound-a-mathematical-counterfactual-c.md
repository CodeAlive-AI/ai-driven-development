## MMP.19 - Construct and Bound a Mathematical Counterfactual Comparison under a Causal Model

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### MMP.19:1 - Problem frame

Use this pattern when the question concerns the same case under another action, a joint comparison of its possible responses, or a specified pathway through which a change would act. A population average may be available while the case-specific or pathway question remains unanswered.

Start with the intended use, the observations about the case or population, and a causal account of the relevant mechanisms. Construct what remains common across the alternatives, carry factual information into that construction and calculate the consequence or range it supports. A useful first result can be two compatible models that give different answers: the supplied information then leaves this distinction unresolved.

The mathematical prerequisites are function evaluation and the probability operations used in the chosen construction. A qualified contributor can supply them. The meaning of the variables, observations and interventions still needs subject knowledge. Small finite cases can be calculated by hand.

For a population intervention effect, use MMP.15 and C.28.MR directly. A choice maximizing expected realized outcome under each action can also need only those intervention distributions, conditional on the information available before acting. Constructing a joint counterfactual law is useful when the receiving question actually depends on it.

### MMP.19:2 - Problem

An intervention distribution describes results across the selected population. Information about an observed case can select different underlying conditions. Reusing the population distribution then answers another question.

There is also a difference between knowing each alternative's distribution and knowing how their results correspond for the same unit. Two causal accounts can agree on every available observation and intervention yet disagree about whether this unit would have succeeded under both actions. Independent simulation of the two distributions silently chooses one such correspondence.

A pathway question adds another dependency: a variable may be set to the value it would have had under a different action. Substituting its population mean can erase the case relation that the question needs.

### MMP.19:3 - Forces

| Force | Consequence for construction |
| --- | --- |
| Case information and population variation | Infer the case's conditions under the factual account before changing its mechanisms. |
| Marginal agreement and joint ambiguity | Recover or bound the dependence across alternatives when the target uses it. |
| Mechanistic detail and obtainable information | A supplied model can determine a conditional consequence that the data alone do not identify. |
| Pathway meaning and interactions | State which nested comparison is intended; different decompositions can answer different questions. |
| Useful decisions and unresolved counterfactuals | A sufficient action comparison may finish without recovering the whole joint law. |

### MMP.19:4 - Solution

**Specify the comparison → construct the common case → use its factual information → evaluate the alternative mechanisms → identify or bound the target → return the consequence to use.**

#### MMP.19:4.1 - State what the comparison must answer

Name the unit, relevant time and population. State the action or mechanism alternatives and what would count as their outcomes. C.28 distinguishes the causal-use question; C.28.MR supplies the meaning of mechanism replacement.

Distinguish the targets that the question could need. Common examples are a mean under an intervention, the response under another action given what happened to this case, and a joint property such as succeeding under one action while failing under another. For a pathway question, name which mechanism's input is to be changed and which other route remains as specified.

Recover what the recipient will do with the answer. A future choice based on expected outcome and action cost can depend only on each action's marginal distribution. A probability of benefit, an explanation of an observed result or a nested pathway contrast can depend on more. C.11 and MMP.8 retain the decision criterion; the mathematical construction must answer that criterion rather than substituting another one.

#### MMP.19:4.2 - Construct one common basis for the alternatives

In a structural model, write the relevant variables as functions of their parents and underlying inputs U. Recover the joint law p(u), given input values, or a set of admissible input laws and mechanisms. U can include shared disturbances and persistent characteristics; its meaning depends on the subject account.

For each action a, let Y_a(u) denote the output of the modified model at the same underlying input u. A response-type representation can instead give a joint vector such as (Y_0,Y_1) directly. Its joint distribution states which responses belong to the same modeled unit. Having the two marginal distributions alone does not supply this dependence.

Keep common conditions common, and identify which changes the action itself causes. Two runs with independently drawn U describe different modeled cases. Reusing a random seed is a numerical way to implement a specified coupling; the seed does not justify that coupling in the subject. Repeating work later with changed conditions likewise needs an account of which inputs persist and which are newly drawn.

Use a model with well-defined responses for the requested inputs. In the finite acyclic case, evaluation in dependency order suffices. Continuous, cyclic or multiple-solution models require their own existence and solution-selection conditions; a solver's returned trace does not settle an unspecified response relation.

#### MMP.19:4.3 - Infer case conditions from the factual observations

Let e denote the available factual record. Use the model and recording procedure that produced it, including the actual action regime. MMP.7 constructs the recording law; MMP.13 supplies the needed conditioning.

For a finite supplied input law and record likelihood k(e given u), form

```text
w(u given e) = k(e given u) p(u) / sum_v k(e given v) p(v).
```

The denominator must be positive. An exact deterministic record has a likelihood of one for compatible inputs and zero for incompatible ones. A noisy or selected record needs its actual likelihood. An individually observed continuous value uses the appropriate conditional distribution or density, not division by the probability of a zero-probability point.

This operation uses the factual mechanisms. Conditioning after replacing them can select a different set of cases. If the supplied account cannot produce the record, return the conflict; changing an assumed mechanism or observation model is a separate justified repair.

A probability law need not be invented when only possible inputs are supported. Retain the inputs compatible with the record and derive the range of responses they permit. If there is no factual conditioning in the query, use the selected population law or set directly.

#### MMP.19:4.4 - Evaluate the compared responses with that common basis

Replace the selected mechanisms using C.28.MR. At each retained u, evaluate all the responses needed by the question before averaging. For a finite conditional comparison,

```text
P(Y_a=y, Y_b=z given e)
    = sum_u w(u given e) 1[Y_a(u)=y and Y_b(u)=z].
```

Here the indicator is one when both conditions hold. A single response or expected difference uses the corresponding function inside the same sum. The shared u preserves the modeled relation between alternatives. Use integration when the model supports a continuous version of this operation.

For a nested response Y_(a,M_b)(u), first compute the intermediate value M_b(u) under b. In the second model set A to a and M to that computed value for the same u, then evaluate Y. Averaging M_b before this replacement generally changes the target. The construction defines a model consequence even when no available physical procedure can jointly realize every term; C.28:4.5 governs a separate claim about obtaining samples.

For a pathway decomposition, state both component contrasts and verify that their sum is the intended total. Interactions can make another choice of reference mechanism give different components. A component's numerical size does not by itself establish the adequacy of the explanation or the feasibility of a proposed physical intervention.

#### MMP.19:4.5 - Determine what the available information fixes

A fully supplied model gives a consequence conditional on that model. Identification asks whether all admissible models agreeing with the available information give the same target. Use MMP.15's distinction between a proof of ambiguity and an unfinished search on the counterfactual construction now specified.

Two compatible models with different target values prove non-identification under their shared assumptions and available laws. More samples from those same laws cannot distinguish them. A narrower quantity can nevertheless be identified.

For a finite response-type construction, assign a nonnegative mass to each admitted type, with total mass one. Express the known marginal, joint and regime laws as constraints on those masses. Add a structural restriction only when the causal account supports it. Minimize and maximize the target over the compatible masses; for a conditional probability retain its conditioning denominator. MMP.10 helps formulate the constraints and an appropriate computational method can solve them.

Call the resulting bounds tight only when the construction establishes that no smaller range follows and that its extremes are attainable, or specifies unattained limiting extremes. A numerical search that finds two values supplies witnesses, not necessarily the full range. Uncertainty from estimating an input law with finite data is another layer, handled by MMP.13; it is not the same as ambiguity remaining even when that law is known.

#### MMP.19:4.6 - Use a sufficient consequence and reopen the affected assumption

Return the target's meaning, the supported value or range, and the assumptions that determine its use. The calculation can already carry these facts; a separate record is needed only by a receiving use.

If every compatible answer supports the same sufficient action or explanation, use that result. If the distinction matters, identify what would change it: a defensible restriction on mechanisms, informative existing records, a feasible different observation, or a different question. MMP.16 and C.11.DUA compare the value and burden of obtaining that contribution. Unavailable evidence can leave a bounded answer and a choice under uncertainty.

A revised recording rule changes the factual conditioning. A revised intervention changes the response functions. A changed criterion can make joint dependence irrelevant. Recalculate the affected contribution while retaining the rest.

During an investigation, this construction can perform its mathematical-modeling contribution while conditioning and mechanism evaluation supply constituent Methods. The investigator or subject specialist supplies the case and causal interpretation; a mathematical or AI collaborator may supply the calculation. Availability of one contribution leaves the others to be obtained where the work needs them.

### MMP.19:5 - Archetypal Grounding

These are constructed cases with supplied mechanisms or exact probability laws. They demonstrate the mathematical operations and limits.

#### MMP.19:5.1 - Change the route for an already observed processing case

A routing model gives latency in ticks as Y=2A+U. Route A=1 adds two ticks; residual latency U is 0 or 1 with equal probability. The recorded case used A=1 and had Y=3.

Under the factual equation only U=1 is compatible. Keeping that input and replacing the route by A=0 gives Y_0=1. Drawing a fresh U from the population instead gives mean latency 1/2. That is a new-case mean, not the requested alternative for the observed case.

If the record is noisy, use its likelihood rather than selecting U with certainty. If an exact Y=4 is reported under the unchanged model, neither admitted U is compatible; return the conflict instead of calculating a posterior with zero denominator. Whether the same residual condition would persist under a real route change is a subject premise of this model.

#### MMP.19:5.2 - Expose a coupling that experiments do not determine

Let a randomized binary action A be independent of the response type U=(Y_0,Y_1). Consider two possible type distributions:

| Type (Y_0,Y_1) | Model S | Model T |
| --- | ---: | ---: |
| (0,0) | 3/8 | 1/8 |
| (0,1) | 1/8 | 3/8 |
| (1,0) | 1/8 | 3/8 |
| (1,1) | 3/8 | 1/8 |

Each action succeeds with probability 1/2 in both models. With a fair random assignment, all four observed (A,Y) combinations have probability 1/4 in each model.

For a case observed with A=1,Y=1, only types (0,1) and (1,1) remain. In S, the probability that it would also succeed under A=0 is (3/8)/(1/2)=3/4. In T it is (1/8)/(1/2)=1/4. Both models fit the supplied observational and intervention laws, so these laws do not identify the answer.

For a future choice scored only by expected success, the actions tie at 1/2 under both models. If A=1 adds a positive cost and no other consequence, A=0 is sufficient for that criterion. Resolving the counterfactual ambiguity would not improve this choice.

#### MMP.19:5.3 - Bound benefit without inventing a joint law

Suppose binary success probabilities under actions 1 and 0 are p1=7/10 and p0=2/5. Let b=P(Y_0=0,Y_1=1), the probability of succeeding only under action 1. The four type masses must be

```text
P(0,1)=b                 P(1,1)=p1-b
P(1,0)=p0-p1+b           P(0,0)=1-p0-b.
```

Nonnegativity gives max(0,p1-p0) <= b <= min(p1,1-p0), hence 3/10 <= b <= 3/5. At b=3/10 the masses in order (00,01,10,11) are (3/10,3/10,0,2/5); at b=3/5 they are (0,3/5,3/10,1/10). Both attain the supplied marginals, establishing the bounds for this unrestricted response-type class.

Now suppose assignment A is independent of the response pair (Y_0,Y_1), P(A=1)>0, and a case is observed with A=1,Y=1. The probability that this case would fail under action 0 is P(Y_0=0 given A=1,Y=1)=b/p1, hence between 3/7 and 6/7. Conditioning retains the types with Y_1=1; the independent assignment probability cancels from numerator and denominator. The same endpoint distributions attain these conditional bounds, since their denominator is the fixed positive p1=7/10.

The mean effect is p1-p0=3/10 in every compatible model. An expected-success criterion with an action-1 cost of 1/10 therefore has net gain 1/5 without identifying b. A criterion that explicitly requires b to exceed 2/5 remains unsettled by these bounds.

If subject knowledge warrants that action 1 never changes a success into failure, P(1,0)=0 fixes b=3/10. That is an additional monotonicity assumption; it was not learned from the two marginal probabilities.

#### MMP.19:5.4 - State which mediated contrast is being calculated

Take the supplied mechanisms M=A+U and Y=3A+2M+AM, with U=0 or 1. Compare actions 0 and 1 for the same u. The total change is 6+u.

First retain the mediator at M_0=u while changing A: Y_(1,M_0)-Y_(0,M_0)=3+u. Then change the mediator to M_1=1+u while retaining A=1: Y_(1,M_1)-Y_(1,M_0)=3. The components sum to 6+u.

Reversing that decomposition gives mediator change 2 at A=0, followed by direct change 4+u at M_1. These components also sum to 6+u. The interaction AM makes the two decompositions different. A request for “the part caused through M” must select its intended contrast. Knowing the total effect alone supplies neither decomposition; observing data that identify it is a further question.

### MMP.19:6 - Bias-Annotation

The explicit examples use finite inputs and simple structural functions. Their transparency helps inspect a comparison but does not show that such a causal account is obtainable for every subject. Subject ambiguity can remain after a numerical method computes a definite answer.

The same-unit relation is part of the model. Its appropriateness in a physical, organizational or human setting depends on what is held common and what each action changes. A purely numerical pairing can be useful for variance reduction while lacking the interpretation required by the causal question.

### MMP.19:7 - Conformance Checklist

- The target states the unit, alternatives, relevant factual information and receiving use.
- Common conditions and changed mechanisms have a subject interpretation.
- Factual conditioning uses the factual mechanism and recording law.
- Joint or nested responses use the specified common-case dependence.
- A model-conditional calculation is distinguished from identification across admissible models.
- An ambiguity or bound is returned at its proved scope, with estimation uncertainty kept distinct.
- A sufficient action can finish without recovering an irrelevant joint law.

### MMP.19:8 - Common Anti-Patterns and How to Avoid Them

| Recognizable failure | Repair |
| --- | --- |
| Use the population input law after receiving information about the case. | Condition under the factual account before evaluating its alternative response. |
| Independently simulate two marginals and interpret the pairs as the same units. | Construct or bound the joint response law the interpretation needs. |
| Replace a nested intermediate value by its population mean. | Compute the intermediate response for each common input before evaluating the outer mechanism. |
| Report a uniquely identified answer because one chosen model yields a number. | Examine the target across the admissible models, or report the result as conditional on that model. |
| Demand a benefit probability for a choice determined by expected outcomes. | Recover the criterion and use the sufficient marginal comparison. |

### MMP.19:9 - Consequences

The recipient obtains a comparison whose case relation and assumptions can be inspected, changed and used. A proved range exposes what remains unresolved without replacing the result by a generic request for more data.

Constructing a common causal account and solving its constraints has a cost. Its value depends on whether the joint, conditional or pathway distinction changes the explanation or decision. An intervention mean or conditional outcome prediction can remain the sufficient result.

### MMP.19:10 - Architectural Rationale

The hard step is often the relation between calculations, rather than each calculation separately. Ordinary conditioning recovers case information; mechanism replacement constructs an alternative; the common input or response-type law connects them. Maintaining that relation permits a joint question and exposes assumptions invisible in separate marginal fits.

The same construction supports historical explanation, probabilities of benefit and nested pathways. Their targets remain distinct. In particular, a decision based on realized outcomes can use less structure than a question about how those outcomes would differ for the same unit.

### MMP.19:11 - SoTA-Echoing

[Correa and Bareinboim (2025)](https://proceedings.mlr.press/v267/correa25a.html), Definitions 1.1–1.3 and §2.1.1, supply the shared-input and nested-response semantics used in :4.2–:4.4. The finite examples here use those definitions; the richer graphical calculus has further conditions and operations.

[Mueller and Pearl (2023)](https://ftp.cs.ucla.edu/pub/stat_ser/r513.pdf) separate average effects from probabilities of benefit or harm. [Dawid and Senn (2025, v2)](https://arxiv.org/pdf/2301.11976), §§2–4, supply a serious alternative: intervention distributions suffice for maximizing expected realized outcomes under the stated information and constraints. Adopt the target distinction in :4.1/:4.6. In :5.2 the same two models require a joint account for the historical question but no such recovery for the stated future choice. The changed question justifies the more elaborate construction.

[Raghavan and Bareinboim (2026, preprint)](https://arxiv.org/html/2602.23541v1), §§2 and 4–5, distinguish identification, partial identification and physically realizable counterfactual sampling. Adapt those distinctions in :4.4–:4.5. Their available-action, finite recursive and positivity assumptions limit the algorithmic results. Establishing a model consequence leaves its physical sampling conditions to be established separately when sampling is needed.

Reopen the selected construction when a supported additional mechanism or information source changes the compatible comparisons, or when another method obtains the required answer with less unsupported structure or burden. The worked finite constructions establish their stated mathematical consequences; practical validity still depends on the subject account.

### MMP.19:12 - Relations

- **C.28** governs causal-use questions and support; **C.28.MR** constructs mechanism replacements and their consequences.
- **MMP.7 and MMP.13** supply the recording and inferential operations used to recover factual case information. **MMP.15** identifies intervention effects from available laws and supplies the identification/ambiguity distinction reused here.
- **MMP.10** formulates compatible response-type constraints. **MMP.16** constructs a worthwhile distinguishing observation; **MMP.14** repairs an account contradicted by appropriate records.
- **MMP.8**, **MMP.8.SD**, **C.11** and **C.11.DUA** connect the consequence to choice, continuation and proportionate further inquiry. **EXD.1** recovers what connection an explanation must supply.

### MMP.19:End
