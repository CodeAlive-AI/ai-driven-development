## MMP.18 - Couple Models with Compatible Exchanges and Scales

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative within the stated use

### MMP.18:1 - Problem frame

Use this pattern when the required answer combines models whose shared quantities, representations or scales differ. One model may return an average while another needs a distribution. Two simulations may exchange a flow at different times. Two statistical analyses may reuse the same prior or observations.

Begin at one exchange that affects the answer. Identify what the supplying model returns, what the receiving model uses it to mean, and the relation needed to connect them. A matching variable name or software interface leaves that relation to be constructed.

The result is a joint formulation: component models with their shared quantities, interface relations and the assumptions needed to use their combined answer. It may expose a missing closure, incompatible conditions or a dependency that an available simulator cannot realize. The first useful result can be that obstruction, or a restricted coupled answer sufficient for the work.

This is mathematical coupling across models. A.3.3.TR supplies joint relations and change rules; MMP.10 supplies their constraint formulation. The additional work here constructs exchanges between representations, preserves the quantities the use depends on, and accounts for shared information. Subject methods supply the meaning and applicability of those exchanges.

The reader needs the mathematics used by the components and their connection. Algebra suffices for the first coupling steps; time-dependent, spatial or probabilistic branches require the corresponding integration, mapping or probability knowledge. A collaborator can construct the mathematics from supplied models and a recoverable subject question.

Use an already adequate joint model directly. Merely keeping several alternative models in a portfolio does not require coupling them into one model. Use portfolio and improvement methods when the alternatives serve complementary questions without exchanging modeled quantities or information.

### MMP.18:2 - Problem

Locally useful models can give an unusable combination. An exchange may be counted twice or disappear between different time steps. Components may share an unknown while their combined calculation treats its values as independent. An average may conceal a variation needed by a nonlinear response. A sequential software call may insert a delay into relations intended to hold together.

The difficulty is to construct the joint model without silently changing what the components mean or the answer they are meant to support. Compatibility at the interface and adequacy in the subject remain separate questions.

### MMP.18:3 - Forces

| Force | Tension |
| --- | --- |
| Reuse and joint meaning | Existing components save work but may describe their common quantity differently. |
| Local accuracy and combined behavior | Accurate component calculations can lose a balance or destabilize feedback through their exchange. |
| Different scales and required detail | A coarse result can omit the variation, timing or dependence another component needs. |
| Separate uncertainty and common information | Independent treatment can count shared evidence twice or remove correlation. |
| One joint solve and separate execution | Separate solvers retain existing tools but introduce exchange approximations and synchronization work. |
| More coupling and sufficient use | Recovering every interaction can cost more than the question warrants. |

### MMP.18:4 - Solution

Choose the combined answer. Recover the meaning and conditions of each consequential exchange. Construct interface relations that preserve what the receiving use needs, then impose them with the component models. Obtain and interpret a joint result, distinguishing a formulation defect from an approximation in its computation. Reopen only the exchange or component whose changed assumption affects that result.

#### MMP.18:4.1 - Identify what the models share and what they exchange

Start from the required result and trace which component supplies each quantity it uses. Recover the quantity's referent, unit and reference point, as well as any time interval, spatial region or probability conditioning that changes its meaning.

Distinguish a shared quantity from a transferred result. If both models describe the same unknown offset, retain one common offset or a justified relation between their coordinates. If one supplies an estimated offset to the other, specify whether the receiving calculation uses its uncertainty or only an approximation by a point value.

Locate overlapping subject effects. If both component laws already include the same interaction, composing them may count it twice. Decide from the subject model which contribution is being retained and which is a second description of it. A.3.3.TR and C.29.BB supply the resulting joint change and balance relations.

Also recover the operating conditions. A component calibrated for one boundary condition may cease to apply when connected to a responsive neighbor. Replacing a supplied input by another model's output can therefore require a changed component law, even when the variable types match.

#### MMP.18:4.2 - Construct the interface relation

Express the exchange as a relation between the component descriptions. A deterministic map is appropriate when the supplied result determines the needed input. Use a broader relation or conditional law when several inputs remain possible.

For a conversion, translate the quantity and its reference point. For an aggregate, state the operation over the specified region or interval. For example, an amount over [t0,t1] is the integral of a rate over that interval; a rate at t0 alone determines that amount only under an additional evolution assumption.

Let x range over values expressed by the supplying model and y over those used by the receiving model. A relation H(x,y) states the compatible pairs. A.3.3.TR supplies composition with other relations, and MMP.10 expresses the joint possibilities. MATH.18 helps determine which operations and consequences the interpretation preserves. Equality of numerical values is one possible relation, not the default.

Derive the property the map must preserve. For amounts at locations, a linear map b=W\*a preserves their total for every a when every column of W sums to one. For values of an intensive field, a map preserving a constant field instead has every row sum to one. If amounts must remain nonnegative, nonnegative weights are an additional sufficient condition. The needed property chooses the map; a convenient interpolation routine does not choose the property.

The two conditions solve different problems. A common field value should remain that value on another discretization. The total amount distributed among cells should remain the same total. When both requirements matter, construct a map with the appropriate geometry or integration weights rather than substituting one condition for the other.

#### MMP.18:4.3 - Restore what the receiving scale needs

Apply the receiving operation to the proposed supplied description. If the result still depends on discarded detail, identify that dependency before choosing a closure.

For example, a component supplies only the mean of x over a region, while a neighboring response requires the mean of x^2. The missing contribution is the variance:

~~~
mean(x^2) = mean(x)^2 + variance(x).
~~~

Two fields with the same mean can therefore yield different received responses. Supplying the squared mean silently sets the variance to zero. Retain the needed statistic, obtain it from the finer model, supply a justified closure or return bounds sufficient for the question. MMP.9 derives reduced evolution and closures; MMP.17 constructs a surrogate when that is the chosen supplier.

A time-scale change can create memory. An interval average need not determine a response at an intermediate instant. A rapidly changing component can also leave an accumulated effect after its local state has relaxed. Recover the information needed by the receiving answer instead of assuming that a small or fast component has no relevant contribution.

Use a coupled approximation only within the conditions supporting it. If feedback drives a surrogate or closure into a different regime, revise that contribution or return to a suitable supplier. Good behavior on isolated component inputs does not establish behavior on inputs generated by the coupled system.

#### MMP.18:4.4 - Impose the joint conditions before choosing execution order

Combine the component relations and interface conditions for the same modeled situation. Shared boundary values and initial conditions must satisfy that joint formulation. Redundant equations can express a useful invariant; contradictory equations expose incompatible assumptions or a failed identification of the shared quantities.

Feedback can require a joint solve. Suppose the selected same-instant relations are x=1+y and y=x/2. Substitution gives x=2 and y=1. Starting from y=0 and calling the first model once, then the second, returns x=1 and y=0.5; those values fail x=1+y. That call order is only one unfinished computation of the joint relation.

Choose between a common solve and separate interacting computations from the available capabilities and error needed by the answer. For time-dependent components, specify which inputs are held, interpolated or extrapolated between communication times, how events are synchronized, and whether a proposed step can be repeated. These are computation assumptions unless the actual subject has that delay or sampling behavior.

Compare the obtained exchange against the joint conditions and the required result. A residual can reveal a mismatch. Turning a small residual into an error bound needs the relevant conditioning or stability argument; CMP.8 supplies that approximate-computation work. CMP.14 supplies interaction between computations. More iterations cannot repair an incompatible physical or statistical premise.

#### MMP.18:4.5 - Combine uncertainty without duplicating information

When components are probabilistic, construct a joint law for the common quantities and the component-specific quantities. Marginal distributions alone generally leave dependence unspecified. Obtain the needed dependence from the modeled mechanism, a conditional law or an explicit additional assumption.

For components sharing z, one possible factorization is:

~~~
p(z,u1,u2) = p(z) * p(u1 | z) * p(u2 | z).
~~~

It assumes conditional independence of u1 and u2 given z. If that assumption is unavailable, construct their joint conditional law or retain the unresolved dependence. A common random quantity is sampled or integrated once as that same quantity; two independent draws would describe a different model.

For two analyses using the same positive prior pi(z) and conditionally independent data D1,D2, their posteriors satisfy q1(z) proportional to pi(z)\*L1(z) and q2(z) proportional to pi(z)\*L2(z). The combined posterior is proportional to q1(z)\*q2(z)/pi(z) on the common prior support. Multiplication without the division counts the prior twice.

If the analyses use overlapping records, first recover which observations and likelihood factors are shared. Dividing out a prior does not remove a duplicated observation. If component priors disagree, selecting a common prior or a pooling rule changes the model and needs a stated basis. MMP.7 supplies the record law and MMP.13 the resulting inference; a computational sampler obtains values from that law.

Point estimates can still be sufficient for a particular receiving use. To replace a distribution by a point, establish that the omitted uncertainty does not alter the required result at its chosen tolerance. Keep a consequential dependence when a nonlinear operation or tail probability needs it.

#### MMP.18:4.6 - Return the coupled result and localize a failure

Return the combined formulation with the exchanged quantities and assumptions needed to reproduce the required result. The subject recipient must be able to interpret that result, including any approximation or unresolved interface contribution that changes its use.

Check the consequence at the scope actually claimed. An interval balance establishes the amount transferred over that interval, not the time of a threshold crossing within it. A joint posterior accounts for the supplied data under its dependence assumptions; it does not establish that those assumptions describe the subject.

If a result fails, locate whether the problem lies in the quantity identification, map, closure, component law, dependence or computation. Repair that contribution and its affected consumers. For a physical question, B.5.MPC.R coordinates a change crossing the physical, mathematical and computational accounts.

Stop with the sufficient coupled answer or the missing contribution that prevents it. C.11.DUA governs whether obtaining that contribution is preferable to a restricted answer or a different method. More detailed coupling is useful when its difference matters to the work.

### MMP.18:5 - Archetypal Grounding

These constructed cases keep the model assumptions visible so that the reader can change the exchange and recompute its consequence.

#### MMP.18:5.1 - Preserve a transfer across different time resolutions

Two components model stores A and B. Material flows from A to B with the supplied rate q(t)=k\*t, where t is time since the interval's start and k=1 unit per minute squared. The stores have enough material and capacity for the stipulated transfer over T=1 minute. Initially A=10 units and B=0.

The donor computes the interval amount:

~~~
Q = integral from 0 to T of k*t dt = k*T^2/2 = 0.5 units.
A(T) = 10 - 0.5 = 9.5 units.
~~~

The receiving simulator takes the initial rate q(0)=0 and holds it throughout the minute. It obtains B(T)=0. The combined stores now total 9.5 units, although the model contains no external removal.

The error is in the exchange. Both components must use the same transferred amount over the same interval. Sending Q=0.5 units and applying A(T)=10-Q, B(T)=Q gives a total of 10 units. C.29.BB supplies the balance; this construction makes the exchange between the two component representations satisfy it.

Now change the requested result: when does B first reach 0.125 units? Under the supplied continuous rate, B(t)=k\*t\^2/2, so it reaches the threshold at t=0.5 minutes. A receiver that inserts the entire amount only at T=1 minute reports a different crossing time despite preserving the final balance.

For that question, send or reconstruct the cumulative transfer Q(t)=k\*t\^2/2 over the interval, or use a computation with adequate intermediate and event resolution. Exchanging only the interval amount is sufficient for the final stores but insufficient for the crossing. The changed question reopens the temporal representation, not the already correct conservation argument.

A nonlinear receiver can likewise need more than an averaged input. Suppose two equally weighted fine cells supply x values (0,2), and the receiver requires the average of x^2. The mean input is 1, but the required response is (0+4)/2=2. Sending only the mean and squaring it gives 1. Supplying variance 1 restores 1^2+1=2; a justified closure could supply the same missing contribution in a larger model.

#### MMP.18:5.2 - Join two analyses without counting their prior twice

Two analyses concern the same binary condition z. Both start from P(z=1)=0.2 and P(z=0)=0.8. Each has one positive observation with the supplied law:

~~~
P(positive | z=1) = 0.75
P(positive | z=0) = 0.25.
~~~

The two observations are distinct and conditionally independent given z. Each separate posterior gives:

~~~
P(z=1 | one positive) = (0.2*0.75)/(0.2*0.75 + 0.8*0.25) = 3/7.
~~~

Multiplying the two posterior mass functions and normalizing gives 9/(9+16)=9/25=0.36. This has counted the shared prior twice.

Construct the joint model from one prior and the two likelihood factors:

~~~
P(z=1 | two positives)
 = (0.2*0.75^2)/(0.2*0.75^2 + 0.8*0.25^2)
 = 9/13, approximately 0.692.
~~~

The same result is recoverable from the separate posteriors by dividing their product by the common prior before normalizing. That operation preserves their intended contributions under the supplied conditional independence.

Now discover that the two reports contain the same observation, copied into two analyses. There is only one likelihood factor. The correct result under the original observation model is again 3/7; the 9/13 calculation is no longer supported. If there are two dependent observations instead, their joint conditional law is needed.

The exchange therefore includes the identity and dependence of the contributing information, not just two numbers labeled “probability.” In a method assessment, the same problem appears when two models of performance use overlapping case records.

### MMP.18:6 - Bias-Annotation

Coupling is often presented through physical simulations, which can suggest that every interface carries a conserved flow. Statistical components instead require coherent shared distributions and dependence. Both cases need an explicit relation between components; the relation's governing property comes from the modeled quantity.

The examples use small equations with known solutions. A large coupled formulation may be well defined but expensive to compute, or locally accurate but poor for the receiving use. Preserve that distinction when choosing a simpler interface or component.

### MMP.18:7 - Conformance Checklist

The coupled construction supports its stated use when:

- the requested combined result and the component contributions needed for it are recoverable;
- shared quantities retain their subject meanings and relevant units, reference points and conditions;
- each consequential exchange has a relation that connects what is supplied to what is used;
- aggregation or scale change retains, obtains or bounds the information the receiving operation needs;
- jointly applicable component and interface conditions hold for the claimed solution;
- computational exchange approximations are distinguished from actual subject delays or events;
- shared uncertainty and evidence have the dependence and multiplicity asserted by the joint model;
- the result retains a consequential limit and a usable return to the contribution that failed.

These conditions recognize the coupled model. Establishing its subject applicability or a numerical error guarantee needs the corresponding subject or computational argument when the use requires it.

### MMP.18:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Connect equal names as equal quantities | Different intervals, references or populations become silently identified | Construct the quantity correspondence before exchanging values |
| Use an interpolation because the tool offers it | A total or constant field may be altered | Derive the preservation condition from the receiving use |
| Pass an average into an arbitrary nonlinear operation | Lost variation changes the result | Derive and supply the missing statistic or closure |
| Treat software call order as the subject law | Inserts a delay or leaves same-instant relations unsatisfied | Formulate the joint conditions, then choose their computation |
| Preserve the final balance and claim the trajectory | Intermediate timing remains unresolved | Retain the temporal information required by the question |
| Multiply fitted component distributions | Can duplicate a prior or shared records | Recover and combine the actual likelihood and dependence contributions |
| Reuse an isolated closure under changed feedback | The coupled system can leave the closure's supported regime | Revise its supply conditions or use a suitable richer component |

### MMP.18:9 - Consequences

A component can be replaced without rebuilding the entire model when its replacement supplies the same required exchange under the same conditions. MATH.18 gives the mathematical comparison; the present method identifies what the neighboring models actually require.

Coupling may reveal that a previously useful component is insufficient or incompatible. The resulting repair can add a shared state, a closure or a joint solve. It can also remove unnecessary detail when the receiving answer depends only on an aggregate already preserved.

For working methods, this helps model the interaction of distinct procedures: a scheduling account may consume a resource or duration distribution supplied elsewhere. The coupling explains that mathematical dependence. MMP.22 reconstructs a changed working rule where the mathematics suggests one; C.32.MWA.PP retains its actual execution and provision conditions.

### MMP.18:10 - Architectural Rationale

The general relation-composition method supplies the way to impose conditions together. Model coupling adds the construction needed when those conditions use different representations, scales or overlapping information. It makes the supplier's result usable by the receiver.

A separate interface relation keeps three possible repairs distinguishable: change a component, change how its contribution is represented, or change the computation of their joint conditions. Without that distinction, solver adjustments can conceal a subject-model error, while a harmless numerical approximation can provoke an unnecessary redesign of the subject account.

Conservation and probabilistic coherence are different preservation questions. Their coexistence here reflects a common modeling task, not an assertion that a probability distribution is a physical flow. The appropriate mathematics remains with its governing pattern or specialist method.

### MMP.18:11 - SoTA-Echoing

**Interoperable components still need a coupling construction.** The Modelica Association's *Functional Mock-up Interface* 3.0.2, §§3–4, distinguishes exchanging model equations from co-simulation and leaves the coordinating solver to the importer. This supports :4.4: an interface format does not select the numerical interaction or establish its error. Reusing existing simulators remains valuable when their exchange capabilities support the required result; a joint solve is the alternative when independently advanced components do not. [Specification](https://fmi-standard.org/docs/3.0.2/).

**Choose a map by what it preserves.** The current preCICE documentation, “Mapping configuration,” distinguishes sum-preserving maps, constant-field interpolation and weighted integral preservation. The adopted move in :4.2 is to derive the required map property from the exchanged quantity. The documentation's mesh algorithms are useful specialized realizations, not universal choices for every representation. A cheap nearest-neighbor map can suffice when its error and preserved quantities fit the use. [Source](https://precice.org/configuration-mapping).

**A common unknown needs a coherent joint distribution.** Goudie and colleagues, *Joining and splitting models with Markov melding* (2019; arXiv v3), §3, constructs combinations through shared variables and addresses inconsistent marginal priors. This supplies a serious alternative to informal transfer of fitted summaries. The simple common-prior case in :4.5 and :5.2 is adopted here; more general pooling requires its additional assumptions. [Read version](https://arxiv.org/html/1607.06779v3). Manderson and Goudie, *Combining chains of Bayesian models with Markov melding* (2023), extends the construction to distinct shared quantities along a chain while retaining their dependence. That extension matters when one shared variable cannot represent all interfaces; an arbitrary network or dependent evidence still requires its own joint construction. [Source](https://arxiv.org/html/2111.11566v2).

**Scale interfaces can need learned or derived closures.** Sanderse and colleagues, *Scientific machine learning for closure models in multiscale problems: a review* (2024), §2, locates the missing contribution when reduction and evolution do not commute. That result supports :4.3's return to MMP.9 or a suitable surrogate. A learned closure is one candidate alongside derived memory, retained state and sufficient bounds; its isolated fit does not settle its coupled use. [Source](https://arxiv.org/html/2403.02913v2).

Revisit the coupling when a component, exchange representation, shared data, scale or receiving result changes. A new numerical or learned method is useful when it improves that same coupling under its applicability conditions and available resources.

### MMP.18:12 - Relations


- **A.3.3.TR** constructs joint change rules and **A.3.3.PI** tests whether retained information suffices for the needed continuation.
- **C.29.1** transfers a result between mathematical accounts. **C.29.BB** constructs a balance whose exchange this pattern may need to preserve.
- **MATH.18** compares mathematical accounts and the consequences their interpretations carry.
- **MMP.10** formulates constraints on the combined possibilities; **MMP.9** derives reduced evolution and closures.
- **MMP.7** supplies the observation law and **MMP.13** the inference under the combined probabilistic assumptions. **MMP.14** investigates a failed model prediction.
- **MMP.17** constructs a surrogate for a needed contribution. Its approximation conditions remain relevant inside the coupling.
- **[MMP.20](26-mmp-20---obtain-a-computable-continuation-when-physical-cons.md)** obtains a consistent continuation when the active constraints of the composed physical model change, including a restart derived from its history and impact law.
- **CMP.8** controls numerical approximation, while **CMP.14** constructs interactions between computations. These obtain a result from the formulation rather than supplying its subject meaning.
- **PHY.5** selects effective physical descriptions by scales and couplings; **PHY.6** supplies physical evolution from balances and response laws.
- **B.5.MPC.R** coordinates repairs across physical, mathematical and computational accounts when the receiving question is physical; **C.11.DUA** compares further coupling work with an adequate restricted answer.
- **MMP.21** compares arrangements using the coupled model; **MMP.22** constructs a working-rule candidate from a mathematical transformation. **C.32.MWA.PP** receives the practical conditions, and **B.1.5.CM** judges a claimed Method whole.

### MMP.18:End
