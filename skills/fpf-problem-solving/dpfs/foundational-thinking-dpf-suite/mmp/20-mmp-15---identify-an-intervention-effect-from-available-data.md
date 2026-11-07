## MMP.15 - Identify an Intervention Effect from Available Data

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative within the stated use

### MMP.15:1 - Problem frame

**Use this when** the work asks what changing an action, operating condition or working method would do, and available observations or experiments might already determine the answer. A fitted association, even a precise one, does not by itself say what would happen under that change. Start by writing the intervention and the quantity needed, then ask which available probability laws and causal assumptions can determine it.

The practical gain is an expression that can be estimated from the available records, a useful bound, or an explanation of the remaining ambiguity. Identification can spare an unnecessary experiment or prevent an unsupported intervention claim.

This is a method of mathematical modeling within causal reasoning. It constructs the connection from available laws to an intervention target. C.28.MR supplies the meaning and consequences of replacing a mechanism in a given causal model; here the model's relevant mechanisms may remain unknown. Subject methods must justify what the intervention changes, which influences may be shared, and which relations remain applicable. The method applies to physical, biological and computational systems and to human or AI working methods.

Preparation requires conditional probability, expectation and the ability to follow a mathematical argument about assumed causal relations. For graphical derivations, the practitioner or an available specialist must be able to check which paths remain open under conditioning and intervention. A specialist contribution must return the target, assumptions, required observable quantities and derivation or obstruction; a software answer alone is insufficient.

Do not reconstruct identification when an applicable result already answers the unchanged question. Use MMP.13 for estimation under an already identified expression, and C.28.MR for a consequence inside a fully supplied causal model. Design another experiment only when the existing result is insufficient and further evidence is worth obtaining. For a question about the same observed case under another action, or a joint or nested comparison of its responses, MMP.19 constructs the common-case relation and determines what the available information fixes.

### MMP.15:2 - Problem

Several causal models can produce the same observable distribution and different intervention consequences. Selection adds another limitation: an experiment can identify an effect among its participants without identifying the effect in the receiving population.

The task is to determine whether the requested causal quantity follows from the available laws and stated assumptions. Failure to find an adjustment set is not failure of identification. Fitting, choosing a prior or simulating one compatible mechanism does not prove that all compatible models give the same answer.

### MMP.15:3 - Forces

- **The requested effect versus an unnecessarily complete model.** An average contrast may be determined while individual responses or the full intervention distribution remain unknown.
- **Usable assumptions versus attractive fit.** Temporal ordering, excluded pathways and invariance across populations carry causal meaning that goodness of fit cannot supply.
- **Available information versus convenient information.** Separate experimental, selected and population laws cannot be treated as one complete joint distribution without a derivation.
- **Simple sufficient construction versus broader search.** Adjustment is often enough. Mediated identification or a general identification algorithm can succeed where adjustment does not, at the cost of additional structural reasoning.
- **A conditional answer versus another investigation.** An explicit bound or assumption-dependent result may already suffice. New observations must answer an unresolved consequential question.

### MMP.15:4 - Solution

Define the target, recover the available laws and describe the admitted causal models. Derive a common expression for their intervention consequence, or demonstrate how they disagree. Limit the returned conclusion to what that argument establishes.

#### MMP.15:4.1 - Specify the causal quantity and what counts as the same intervention

For an action level \(a\), let \(Y(a)\) denote the outcome under the specified intervention setting the action to \(a\). For a target population \(T\), a common request is

\[
\mu_a=E_T[Y(a)], \qquad \Delta=\mu_1-\mu_0.
\]

Define the action, comparator, outcome, population and time horizon far enough to distinguish the actual question. A contrast of average outcomes differs from the chance that a particular unit would benefit. Identifying both marginal laws of \(Y(1)\) and \(Y(0)\) does not ordinarily identify their joint law or the distribution of individual differences.

Establish consistency: for a unit actually receiving the specified version of action \(a\), its observed outcome agrees with \(Y(a)\). Different doses, implementations or accompanying actions may give the same label different meanings. If one unit's outcome depends on other units' actions, represent the relevant joint assignment or policy; the notation \(Y(a)\) must not silently discard that dependence.

For static interventions, \(P(Y\mid do(A=a))\) denotes the corresponding intervention law. C.28.MR defines the change of mechanism that gives this notation its meaning. Identification below seeks that law or its required function without assuming all the changed model's numerical mechanisms are already known.

#### MMP.15:4.2 - Recover the available laws and the admissible causal models

Use MMP.7 to recover how records arise. With inclusion indicator \(S\), selected records supply a law such as \(P(A,Y,L\mid S=1)\), not automatically \(P(A,Y,L)\). Keep assignment, actual action, measurement and inclusion distinct when those distinctions affect the target. State which variables were jointly observed, which interventions were performed, and which population each source concerns.

For identification, provisionally treat these population laws as known. This asks what unlimited data of those kinds could determine. MMP.13 handles finite-sample estimation.

Describe the admitted causal relations. An acyclic causal graph is a useful representation: directed arrows allow direct causal influence, and a shared unobserved cause can be represented explicitly or by a bidirected edge. The absence of an arrow excludes a possible influence relative to the represented variables. A good observational fit does not justify that exclusion. Time-indexed variables can express feedback across time; a theorem for acyclic graphs must not be applied unchanged to an equilibrium model with unresolved cycles.

When these causal relations or material rival mechanisms still need construction, C.28.CM develops the model family, its subject meanings and the consequences that could distinguish its members. Bring that result back to the identification question. A sufficient already supplied family needs no additional construction.

The operative identification test is this: whenever two admitted causal models induce the same available laws, must they give the same requested quantity? If the assumptions themselves conflict with the available laws, return that conflict rather than declaring a result identified through an empty model class.

#### MMP.15:4.3 - Derive an expression, using the simplest sufficient route

Begin with a relation that replaces an unobserved intervention quantity by available quantities under an explicit assumption. Then combine it with ordinary conditioning, multiplication and averaging. Every final factor must come from an available law or an earlier justified step. Displayed sums concern discrete variables; for continuous or mixed variables, average against their actual probability laws.

For example, let \(L\) be measured before action. For a mean effect in the same population as the data, suppose that within each relevant \(L=l\), action assignment does not select a different mean potential outcome:

\[
E[Y(a)\mid L=l]=E[Y(a)\mid A=a,L=l].
\]

This mean exchangeability assumption, consistency and positive probability of each required action in the relevant strata give

\[
\mu_a
=\sum_l E[Y(a)\mid L=l]P(L=l)
=\sum_l E[Y\mid A=a,L=l]P(L=l).
\]

The first equality averages over the target strata. The second uses exchangeability to compare the same potential outcome, then consistency to replace it by an observed outcome. Average both actions with the same target weights. The different distributions \(P(L\mid A=a)\) generally answer an association question instead.

A common graphical justification is the back-door criterion: choose pretreatment variables that block every path into \(A\) capable of linking it to \(Y\) through other causes. In checking a path, conditioning on an intermediate non-collider blocks it; a collider, where two arrowheads meet, blocks it unless that collider or a descendant is conditioned on. Thus adding every available covariate can open a path rather than remove bias. This criterion is sufficient, not the only way to justify adjustment or identify an effect.

When adjustment of \(A\)'s effect is unavailable, derive other observable intermediate quantities. In a simple front-door construction, a measured mediator \(M\) carries every directed path from \(A\) to \(Y\); \(A\) to \(M\) has no open back-door path; and conditioning on \(A\) blocks all back-door paths from \(M\) to \(Y\). Under these conditions and the required support,

\[
P(Y=y\mid do(A=a))
=\sum_m P(M=m\mid A=a)
   \sum_{a'} P(Y=y\mid M=m,A=a')P(A=a').
\]

The outer factor identifies the effect of action on the mediator. The inner adjustment identifies the outcome law under intervention on the mediator. The pathway restrictions license combining them for the action's total effect. Merely including a post-action measurement in a regression does not perform this construction. These classical conditions are sufficient; their failure does not establish that this functional or another identifying expression is impossible. [Front-door criteria and their extension](https://arxiv.org/html/2604.15288v1), §§2.1.5–3.

For a more involved graph or several input laws, derive a sequence of intermediate distributions using the rules of do-calculus and probability. Each exchange between observation and intervention needs the corresponding separation condition in the modified graph. A suitable identification implementation can carry out that search: provide the graph, the target and the actual input laws, then recover the returned derivation and check its required factors. The historical ID algorithm covers a specified acyclic model class with latent common causes and an observed joint law; generalized search can use several incomplete or experimental laws. Do not replace those inputs by a joint law that the records never supplied. [ID algorithm](https://ftp.cs.ucla.edu/pub/stat_ser/r327.pdf), Figure 3; [generalized search](https://arxiv.org/html/1902.01073v5), §§2–3.

##### MMP.15:4.3.1 - Use a binary instrument for a specified local effect

Use this branch when a binary assignment or encouragement \(Z\) changes actual action \(A\in\{0,1\}\), and an instrumental-variable argument might identify an effect of \(A\). The effect of offering an action and the effect of performing it are different targets. If the receiving question requires the population average effect, determine whether the local quantity below answers it before using the result.

Let \(A(z)\) be the action a unit would take under assignment \(z\). Start with \(Y(z,a)\) for its outcome under assignment \(z\) and action \(a\). Use the simple argument only under these assumptions:

- **Consistency and stable versions:** observed \(A=A(Z)\) and \(Y=Y(Z,A)\); the specified interventions have fixed meanings and no interference between units.
- **Assignment independence and support:** \(Z\) is independent of the potential actions and outcomes, and both assignment levels have positive probability in the population supplying the law.
- **Exclusion:** \(Y(z,a)=Y(a)\); assignment has no effect on the outcome except through actual action.
- **Monotonicity:** \(A(1)\geq A(0)\) for each unit. Assignment 1 never discourages a unit that would act under assignment 0.
- **Relevance and finite means:** \(\delta_A=E[A\mid Z=1]-E[A\mid Z=0]>0\), and the required outcome expectations exist.

These premises can be more demanding than random assignment alone. Randomizing an offer can support assignment independence without establishing exclusion or monotonicity. This is the binary local-effect argument of [Angrist, Imbens and Rubin, 1996, §§2–4](https://www.math.mcgill.ca/dstephens/AngristIV1996-JASA-Combined.pdf).

The response pair \((A(0),A(1))\) separates always-takers \((1,1)\), never-takers \((0,0)\), compliers \((0,1)\) and defiers \((1,0)\). These are potential-response groups; observing one assignment and action generally does not label the individual's group. Monotonicity excludes defiers.

To derive the result, use exclusion and the binary-action identity \(Y(a)=Y(0)+a\{Y(1)-Y(0)\}\). Independence and consistency give

\[
\delta_Y=E[Y\mid Z=1]-E[Y\mid Z=0]
=E[(A(1)-A(0))(Y(1)-Y(0))].
\]

The same argument gives \(\delta_A=E[A(1)-A(0)]\). Under monotonicity, that difference is one for compliers and zero for the other admitted groups. Consequently,

\[
\frac{\delta_Y}{\delta_A}
=E[Y(1)-Y(0)\mid A(1)>A(0)].
\]

This Wald ratio identifies the local average treatment effect for compliers under the named instrument and population. It is neither automatically the effect for everyone who took the action nor the population average effect. Changing the encouragement can change the complier group.

If \(\delta_A=0\), the ratio is undefined. A small nonzero population first stage can still identify the local quantity under the assumptions, while finite-sample uncertainty and sensitivity to premise violations can be large; MMP.13 must supply suitable inference for the receiving use. If defiers are possible, the numerator and denominator instead mix oppositely signed response-group contributions. A direct \(Z\)-to-\(Y\) route, assignment dependence or interference also requires a different argument. Conditional instrument validity, continuous action and transport to another population need their own derivations; the simple unadjusted ratio does not supply them.

#### MMP.15:4.4 - Carry selection, transport and support through the expression

Identify which population supplies every average. For example, an experiment in \(S=1\) may supply action-specific outcome means by pretreatment \(L\), while an existing inventory supplies the target distribution \(P_T(L)\). If the intervention has the same meaning, assignment in the experiment is exchangeable, and the conditional potential-outcome means agree between the experimental and target populations, then

\[
\mu_a=\sum_l E[Y\mid A=a,L=l,S=1]P_T(L=l).
\]

This is a transport assumption followed by trial identification and target averaging. It requires trial coverage and both action levels wherever the target gives relevant weight. Equal variable names, similar marginal distributions, or randomization within the experiment do not establish the transport assumption. Selection after action or outcome requires its own recording and causal argument; it cannot automatically use this pretreatment bridge. [Generalizing trial results](https://arxiv.org/html/1709.04589v2), §§3–4.

Inspect the support needed by the chosen expression. Positivity means that a required conditional law is defined on the relevant target support; in the discrete adjustment example, \(P(A=a\mid L=l)>0\) whenever the target weights that stratum. For continuous variables, use the corresponding support condition. A fixed intervention value in a continuous action space may also need a continuity or other structural restriction: the observed law determines conditional responses only almost everywhere. An empty cell in a small sample does not prove a population probability is zero. A known structural exclusion is different: the missing conditional response cannot be learned there from that source.

Failure of support invalidates that expression at the excluded values. Another source, another identifying argument or an explicit structural restriction may still answer the question. Extrapolation through a response model can produce an assumption-dependent answer, but fitting or regularizing that model does not create observations at the missing support.

#### MMP.15:4.5 - Distinguish a proof of ambiguity from an unfinished search

To demonstrate nonidentifiability, construct two causal models satisfying the stated assumptions, reproducing all the available laws, and giving different values of the requested target. C.28.MR can calculate each model's intervention consequence. Show both the observational agreement and the difference after intervention, as in :5.2.

A complete identification algorithm can also return an obstruction; check its class and query. A time limit or exhausted search without an applicable completeness result leaves the derivation unresolved. Failure to identify a full intervention distribution also does not by itself prove failure to identify a particular mean or contrast. [ID completeness](https://ftp.cs.ucla.edu/pub/stat_ser/r327.pdf); [scope of search completeness](https://arxiv.org/html/1902.01073v5), §3.4.

When a point is not identified, use the assumptions to bound the requested quantity. Optimize it over compatible models, or derive an inequality valid for all of them. One compatible example establishes possibility; it does not establish a bound. If a bound is claimed sharp, show that compatible models attain or approach its endpoints. A bound that already settles the receiving question needs no complete reconstruction of unknown mechanisms.

A prior or added restriction may select among compatible answers; retain that dependence. It is not new evidence.

#### MMP.15:4.6 - Return the sufficient result and propagate consequential changes

Return the target and the assumptions under which its identifying expression, bound or ambiguity result holds. Make the data factors recoverable for estimation and uncertainty under MMP.13. Numerical evaluation belongs to an appropriate computational method; a completed optimization or simulation is not an identification proof.

Check the derivation as needed: verify a finite case, inspect a disputed graph condition, or calculate a countermodel's observational and intervention laws. These checks establish the mathematical consequence of assumptions. Assurance that the assumptions describe the subject requires relevant subject evidence; successful fitting or self-consistent simulation does not provide it by itself.

When an actual change admits a direct pathway, changes an intervention's version, alters selection, or changes the target population, propagate it through the affected derivation and calculation. Compare an alternative assumption when that comparison can change the intended use. Do not invent a sensitivity exercise for an already sufficient result under unchanged conditions.

C.11.DUA selects whether remaining uncertainty warrants more evidence, an explicitly conditional answer, a narrower agreed question or no further work. MMP.16 can design an observation if that further work is chosen. A mathematical identification result does not authorize or physically carry out the intervention.

### MMP.15:5 - Archetypal Grounding

These constructed population probabilities make the calculations inspectable. Each case assumes fixed intervention meanings and no interference between its units. Finite records add estimation uncertainty to the assumption dependence shown here.

#### MMP.15:5.1 - Separate a production action from the batches receiving it

A production team asks whether enabling a stabilization mode \(A=1\), rather than \(A=0\), increases the probability of a conforming item \(Y=1\). Incoming batch condition \(L\) is recorded before mode selection. Half the target batches have \(L=0\), half \(L=1\). Mode 1 is used on 80% of \(L=0\) batches and 20% of \(L=1\) batches.

| Batch condition | \(P(Y=1\mid A=0,L)\) | \(P(Y=1\mid A=1,L)\) |
| --- | --- | --- |
| \(L=0\) | 0.10 | 0.20 |
| \(L=1\) | 0.70 | 0.80 |

The subject account asserts consistency and mean exchangeability given \(L\); both modes occur in both strata. Adjustment therefore gives \(\mu_0=0.5(0.10)+0.5(0.70)=0.40\), \(\mu_1=0.5(0.20)+0.5(0.80)=0.50\), and \(\Delta=0.10\).

The selected groups instead give \(E[Y\mid A=1]=0.8(0.20)+0.2(0.80)=0.32\) and \(E[Y\mid A=0]=0.2(0.10)+0.8(0.70)=0.58\): an association of \(-0.26\). Its sign differs because the two modes receive different batch mixtures.

This positive average effect is conditional on the causal account; the table does not prove exchangeability. An already supported account and sufficient estimate need no new experiment.

#### MMP.15:5.2 - Use a mediator, then withdraw a pathway exclusion

A service's command \(A\) can activate a retry mechanism \(M\), which affects successful completion \(Y\). Unrecorded load can affect both command selection and completion. The initial causal account permits \(A\to M\to Y\) and an unobserved common cause of \(A,Y\), but no other arrows: in particular, no direct effect of \(A\) on \(Y\) and no hidden common cause of \(A,M\) or \(M,Y\).

All three variables are binary. The available joint law has \(P(A=1)=0.5\), \(P(M=1\mid A=0)=0.25\), \(P(M=1\mid A=1)=0.75\), and:

| Mediator and command | \(P(Y=1\mid M,A)\) |
| --- | --- |
| \(M=0,A=0\) | 0.10 |
| \(M=1,A=0\) | 0.70 |
| \(M=0,A=1\) | 0.30 |
| \(M=1,A=1\) | 0.90 |

There is no observed pretreatment adjustment variable for the shared load. The front-door conditions nevertheless hold. First adjust the mediator's effect over \(A\): the inner means are \(h(0)=0.5(0.10)+0.5(0.30)=0.20\) and \(h(1)=0.5(0.70)+0.5(0.90)=0.80\). Then average over the mediator law induced by each command:

\[
\mu_0=0.75(0.20)+0.25(0.80)=0.35,\qquad
\mu_1=0.25(0.20)+0.75(0.80)=0.65.
\]

Thus \(\Delta=0.30\). Directly comparing observed commands instead gives \(0.75-0.25=0.50\).

**Changed condition.** Inspection of the service reveals that the command can also change completion through a path bypassing retry. The revised account permits a direct \(A\to Y\) arrow. Retaining the previous formula is no longer justified.

The same full observational law now admits at least two answers. To demonstrate this, let unobserved \(U\) be a fair binary variable, let observational command selection be \(A=U\), and generate \(M\) with probability \(0.25+0.50A\) using independent random variation. In two alternative models, generate completion with respective probabilities

\[
\text{Model I: }0.10+0.60M+0.20U,\qquad
\text{Model II: }0.10+0.60M+0.20A,
\]

using a further independent random draw. Every probability lies between zero and one. Because \(A=U\) observationally, both models give every cell of the supplied joint law.

Under \(do(A=a)\), \(U\) remains fair. Model I gives \(\mu_0=0.35,\mu_1=0.65\); Model II gives \(\mu_0=0.25,\mu_1=0.75\). Their effects are 0.30 and 0.50. Both satisfy the revised account, which permits the listed influences without requiring every permitted influence to be nonzero. Model II was excluded by the original no-direct-effect premise.

This is a proof that the revised assumptions and available law do not identify the average effect. These are ambiguity witnesses, not discovered service mechanisms. More precise estimation of the same law cannot distinguish them. A substantive restriction might; further evidence is chosen by its value for the use.

#### MMP.15:5.3 - Transfer an experiment to another mixture of sites

An ecological model asks for the effect of a specified irrigation change \(A\) on establishment of a seedling \(Y\), averaged across a target collection of sites. Soil stratum \(L\) is known from an existing inventory. A selected experiment randomized both irrigation levels within each stratum, recorded every outcome, and used the same irrigation implementations as the target question.

Suppose the subject account supports equality of conditional potential-outcome means between experimental and target sites. Experimental sites are 80% \(L=0\) and 20% \(L=1\); the target inventory is 25% \(L=0\) and 75% \(L=1\).

| Soil stratum | Experimental mean under \(A=0\) | Experimental mean under \(A=1\) | Difference |
| --- | --- | --- | --- |
| \(L=0\) | 0.20 | 0.50 | 0.30 |
| \(L=1\) | 0.60 | 0.70 | 0.10 |

The experimental average effect is \(0.8(0.30)+0.2(0.10)=0.26\). The target means are \(\mu_0=0.25(0.20)+0.75(0.60)=0.50\) and \(\mu_1=0.25(0.50)+0.75(0.70)=0.65\). The requested effect is 0.15. Randomization identifies the comparisons inside the experiment; the transport assumption and target inventory justify the different outer average.

Now suppose the source is found to contain experimental outcomes only for \(L=0\); the supplied \(L=1\) values were extrapolations, with no justified response relation supporting them. Retain the target inventory and transport within the covered stratum. With no outcome restriction for \(L=1\) beyond binary outcomes, its mean effect \(\delta_1\) lies in \([-1,1]\). Therefore

\[
\Delta=0.25(0.30)+0.75\delta_1\in[-0.675,0.825].
\]

The endpoints are attainable by making every uncovered site respectively harmed or helped: \((Y(0),Y(1))=(1,0)\) or \((0,1)\). Those choices do not alter any available experimental outcome. The bound is sharp under these assumptions, and the sign of the target effect is not identified. The effect 0.30 remains available for the covered stratum if that is the agreed receiving question; it must not silently replace the original population target.

#### MMP.15:5.4 - Distinguish an offer effect, a local use effect and an overall effect

A team considers offering help with a work procedure. Let \(Z=1\) mean an independently randomized offer, \(A=1\) actual use, and \(Y=1\) successful completion. Assume fixed versions, no interference, exclusion, monotonicity and complete outcome recording. The following constructed population supplies one possible basis:

| Response group | Population share | \(A(0),A(1)\) | Mean \(Y(0)\) | Mean \(Y(1)\) |
| --- | --- | --- | --- | --- |
| Always-takers | 0.2 | \(1,1\) | 0.10 | 0.60 |
| Compliers | 0.4 | \(0,1\) | 0.40 | 0.65 |
| Never-takers | 0.4 | \(0,0\) | 0.30 | 0.30 |

Randomization is independent of response group and potential outcomes. The action rates are 0.2 without the offer and 0.6 with it. The outcome means are

\[
E[Y\mid Z=0]=0.2(0.60)+0.4(0.40)+0.4(0.30)=0.40,
\]
\[
E[Y\mid Z=1]=0.2(0.60)+0.4(0.65)+0.4(0.30)=0.50.
\]

The offer effect is 0.10. The first stage is 0.40, so the ratio gives \(0.10/0.40=0.25\), the complier mean effect. Under the stipulated full table, the population effect is instead \(0.2(0.50)+0.4(0.25)+0.4(0)=0.20\).

The observational law does not reveal the full table. Change the never-takers' mean \(Y(1)\) from 0.30 to 0.80 while retaining all other quantities. Their action remains zero under both assignments, so this change leaves the full observed law of \(Z,A,Y\) unchanged and preserves the assumptions. The overall effect becomes 0.40; the identified complier effect remains 0.25. This pair of models shows why the available law does not identify the overall effect under these premises.

Now change the offer itself: it teaches a technique that can improve success without use of the help. Exclusion no longer holds. Retain the randomized offer-effect question, but withdraw the former interpretation of the ratio as the complier use effect until a revised model supplies a valid argument. Observing the same four means would not restore the missing exclusion premise.

### MMP.15:6 - Bias-Annotation

Predictive success invites reading inputs as controls. Readily measured variables invite unjustified adjustment, while unmeasured common causes disappear for lack of a data column. Construct the causal account from the subject process.

Failure of a familiar criterion can instead encourage unnecessary data collection. Search more broadly when the answer matters, preserving unresolved search as unresolved. Check that calculation has not substituted a convenient population or intervention version for the requested one.

### MMP.15:7 - Conformance Checklist

- The intervention, comparator and receiving quantity are defined, with consistency and interference handled where relevant.
- A local instrumental-variable effect retains its assignment, response group and assumptions; a different requested population effect remains a different target.
- The derivation uses the laws actually supplied by the recording and selection procedures.
- Every causal substitution has an assumption or applicable graphical argument; every final data factor is available on its required support.
- A nonidentifiability claim has a target-matched witness or applicable complete-method obstruction. An unfinished search is reported separately.
- A returned bound is justified for all compatible cases; sharpness is claimed only with an attainability argument.
- Estimation uncertainty, causal assumption dependence and computational approximation retain their different meanings.
- Actual consequential changes are propagated. A sufficient existing result does not trigger an obligatory new study.

These conditions recognize a constructed identification result. They do not establish the subject truth of its causal assumptions or authorize an intervention.

### MMP.15:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Consequence | Repair |
| --- | --- | --- |
| Change a predictor value and call the prediction an effect | Conditions on naturally selected cases rather than specifying an intervention | Define the intervention target and derive its relation to the available law |
| Adjust for every recorded variable | Can block part of the requested effect or open a collider path | Justify the selected variables for that target |
| Treat no adjustment set as nonidentifiability | Misses mediated or other identifying constructions | Seek a justified broader derivation or a real obstruction |
| Pool experimental, selected and target records as one population | Changes the probability law behind the expression | Retain source conditions and derive the transport or selection correction |
| Fill unsupported cells by regression and claim data-only identification | Hides extrapolation assumptions | State the additional response restriction or return a bound |
| Treat a prior, fitted mechanism or simulation as fresh causal evidence | Conceals disagreement among compatible causal models | Show which assumption selected the answer and what the records distinguish |

### MMP.15:9 - Consequences

Estimation concentrates on the required observable quantities. Nonidentifiability becomes an explicit limitation of assumptions and information, not an unexplained numerical failure.

The causal argument may demand subject knowledge unavailable in the dataset. More elaborate identification does not strengthen an unjustified premise. A conditional answer or bound can be useful without recovering every mechanism.

In methodology, this changes how a proposed improvement to a working method is assessed. Define the method change and relevant outcome, recover how cases and results were recorded, and distinguish its effect from differences in which cases received it. The same reasoning can govern a human procedure, an automated procedure or their combination, without making a population experiment mandatory for every use of the method.

### MMP.15:10 - Architectural Rationale

Mechanism replacement gives intervention semantics within a model. Identification adds a different construction: showing that the needed intervention consequence is common to the causal models compatible with available laws and assumptions, or exposing where it is not.

The target-first construction avoids demanding a complete causal model when a mean, contrast or bound suffices. Separating derivation from estimation lets one identifying expression support different appropriate inferential methods. Separating source laws prevents mathematical convenience from turning selected records into information about an unobserved population.

### MMP.15:11 - SoTA-Echoing

The governing question is whether the available laws and defensible causal assumptions determine the requested intervention quantity. A serious default is justified covariate adjustment; another is to fit a response model and predict after changing its action input. Adjustment is retained when it supplies a valid, economical derivation. Prediction under a fitted response model is accepted as an intervention answer only when its structural assumptions identify that meaning.

**Historical completeness anchor.** Shpitser and Pearl, *Identification of Joint Interventional Distributions in Recursive Semi-Markovian Causal Models* (AAAI 2006, UCLA report R-327), Figure 3 and the soundness/completeness argument, supply an algorithm that can return an expression or a graphical obstruction in its specified model class. This supports :4.3 and :4.5: failure of adjustment is not the general stopping rule, and a negative algorithmic result requires the matching completeness conditions. The result is not a universal certificate for cyclic, selected or otherwise differently specified models. [Source](https://ftp.cs.ucla.edu/pub/stat_ser/r327.pdf).

**Several available laws rather than an invented joint law.** Tikka, Hyttinen and Karvanen, *Causal Effect Identification from Multiple Incomplete Data Sources: A General Search-based Approach* (2021; arXiv v5, 27 August 2021), §§2–3.4, develops do-search by retaining known distributions and deriving new ones with justified rules. This is adopted in :4.2–:4.3 when one adjustment formula or one complete observational law does not fit the information actually available. Its broader search costs more than a sufficient specialized derivation; its negative output has only the completeness scope established for the problem being solved. [Read version](https://arxiv.org/html/1902.01073v5).

**Current extension of a familiar sufficient criterion.** Wu and Robeva, *Generalization of Pearl's Front-Door Criterion* (arXiv v1, 16 April 2026), §3, gives weaker sufficient graphical conditions for the same front-door functional and worked derivations outside the classical criterion. This reinforces the broader derivation route in :4.3 instead of rejecting an effect merely because a familiar criterion fails. The simple case in :5.2 needs only the classical sufficient conditions. The newer result concerns a particular functional in its stated graphical setting; it neither removes the need for subject justification nor supplies a complete test for every causal target. [Read version](https://arxiv.org/html/2604.15288v1).

**Population scope is part of identification.** Dahabreh and colleagues, *Generalizing causal inferences from individuals in randomized trials to all trial-eligible individuals* (2019; arXiv v2, 29 October 2019), §§2–4, separates within-trial exchangeability from the conditional-mean and participation assumptions required for generalization. That distinction is adapted in :4.4 and :5.3: the target mixture can differ even when the experimental comparisons are valid. Its particular nested-trial setup is not presumed for arbitrary selected records. [Read version](https://arxiv.org/html/1709.04589v2).

**A local effect under a binary encouragement.** The serious alternative to :4.3.1 is reporting the randomized offer's effect, or seeking a population effect of actual use under additional assumptions. Adopt the narrower response-group derivation when its local target serves the receiving use: it needs no fully specified outcome mechanism, but does require substantive exclusion and monotonicity. The historical [Angrist–Imbens–Rubin argument, 1996, §§2–5](https://www.math.mcgill.ca/dstephens/AngristIV1996-JASA-Combined.pdf) supplies that identification result, not a complete modern inference method for weak instruments. The calculation and two compatible populations in :5.4 expose what the local result leaves undetermined. Reopen when assignment can affect outcomes directly, response types change, or the receiving population or target differs.

Reopen the chosen derivation when the target, available laws, causal exclusions, population bridge or support changes. Consider a different identification method when it answers the same question under more defensible assumptions or with materially less effort; source recency alone does not require replacing an already sufficient argument.

### MMP.15:12 - Relations

- **C.28** supplies the causal-use question and the distinction between identification, estimation and realizability. **C.28.MR** supplies intervention semantics and calculations within a specified causal model. **C.28.CM** constructs missing causal relations and material alternatives before their identifying implications are assessed.
- **C.16.IR** supplies compatible-case and sufficient-target reasoning; this pattern constructs the causal identification expressions and ambiguity witnesses.
- **MMP.7** supplies the observation law, including selection and missingness. **MMP.11** supplies an explicit model family when its restrictions are needed.
- **MMP.12** handles inverse ambiguity and justified regularization. A restriction used here remains an added causal or response assumption, not new evidence.
- **MMP.13** constructs inference for the identified expression or explicitly assumption-dependent target. **MMP.14** investigates failed model predictions; observational checks alone need not distinguish observationally equivalent causal models.
- **MMP.19** constructs and bounds history-conditioned, joint and nested counterfactual comparisons; an intervention mean can remain sufficient for a choice based on expected outcome.
- **MMP.16** addresses a chosen need for additional observation design. **C.11.DUA** governs whether that work is worthwhile.
- **Computational Thinking**, including **CMP.8 and CMP.9** where their numerical methods apply, obtains numerical values without supplying the missing causal argument. Subject methods justify and realize the intervention and the asserted invariances.

### MMP.15:End
