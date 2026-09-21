## B.5.FM - Construct a First Model for the Working Question

> **Type:** Method pattern
> **Status:** Draft
> **Normativity:** Normative unless marked informative

### B.5.FM:1 - Problem frame

Use this pattern when you need to reason about a situation or formal problem but do not yet have an account on which to perform the needed inference. You may know relevant laws, facts or techniques while still being unable to choose the participants, distinctions and relations that make them useful here.

Begin with what the answer should help you understand or do, the observations or formal rules already available, and enough subject knowledge to propose a relation. Construct a provisional model, obtain a consequence and use it to answer the question or locate the next missing contribution. A sketch and a limiting argument may provide that first result.

“First” means the first usable model for this question. An earlier model, an analogy or a specialist's explanation can supply its starting material. Use an adequate existing model directly when construction is unnecessary. If an available concept is understood but its correspondence to the situation is missing, B.5.4 supplies that interpretation work. If the required inference needs subject knowledge you cannot recover, obtain that contribution.

### B.5.FM:2 - Problem

A request to “model the system” leaves important work unstated. Which things may change separately? Which interactions matter? What may be treated as fixed? What operation on the proposed description could answer the question?

An early description can hide the decisive relation. A device described by one temperature conceals a heat-transfer restriction inside it. A draining vessel described only by liquid height conceals the effect of trapped air. Counting all possible binary strings ignores a rule that forbids some continuations.

A model becomes useful when its selected distinctions and relations permit an inference whose meaning can be returned to the working question. Constructing that possibility is part of the reasoning.

### B.5.FM:3 - Forces

| Force | Consequence for construction |
| --- | --- |
| A question selects what matters; a model can reveal that the question needs changing. | Keep the receiving use visible while allowing the construction to expose a better question. |
| Familiar concepts provide useful relations; the situation may need a new combination. | Reuse what works and explain the connections introduced between contributions. |
| A detailed description can be expensive to build and difficult to reason with. | Add a distinction because its omission changes a needed consequence. |
| A cheap consequence can guide action before the model is fully developed. | State what supports that consequence and which unresolved choices matter to its use. |
| Different representations expose different operations. | Choose or change the expression while constructing the inference. |

### B.5.FM:4 - Solution

Construct a model by selecting distinctions, proposing their relations and making those relations usable in an inference. Work can move back and forth between these contributions. Keep the question and the consequence connected as the model changes.

#### B.5.FM:4.1 - Recover the contrast the answer must resolve

State what alternatives the answer should distinguish: whether an intervention can reach a target, which arrangement could explain an observation, how many constructions meet a rule, or what condition prevents a result.

Inspect a small instance or the available arrangement. Describe the supplied facts separately from the account you propose. Ask what changes between the cases that matter. The first question can be provisional; preserve a new question when the attempted construction reveals a more useful distinction.

An existing answer may already resolve the contrast. Use it under its conditions. C.11.DUA helps when obtaining more information or refining a model competes with acting on a sufficient answer.

#### B.5.FM:4.2 - Choose the participants and distinctions

Follow what can be transformed, exchanged, combined, constrained or observed. Propose the objects and relations needed to describe those changes. For a physical situation, an interaction may cross the first proposed boundary: air surrounding a vessel or a path through its casing can matter to the answer.

Try a consequential variation. If two situations receive the same description but permit different answers, recover the distinction that separates them. An object can need several quantities; several objects can sometimes be represented together. Choose the coarsening from the inference it must preserve.

For a question about permitted continuations, A.3.3 helps construct a sufficient state description. For an observation, C.16 helps connect the quantity of interest to what the observation reports.

#### B.5.FM:4.3 - Build relations that can produce a consequence

Use subject knowledge to propose how the selected participants interact or which operations are permitted. Explain how each proposed relation answers part of the question. A physical interaction law, a mathematical formation rule and an execution rule supply different kinds of premise.

Starting material can come from more than one source. A known model may need to be altered before it becomes a useful analogy. Recover the corresponding participants and relations, then examine the changes needed in the present situation. The construction can improve both the proposed model and the understanding of what it represents.

Keep coupled choices compatible. If liquid leaving a closed vessel increases the space occupied by trapped gas, a pressure calculation must use that changed space. If two classes of formal objects permit different extensions, their counts must remain distinguishable until the extension is performed.

Use an expression that lets you carry out the next inference: an annotated sketch, a table of permitted operations, equations, a physical surrogate or a computational construction. A physical surrogate has its own material behavior; establish which of its results can inform the original situation. C.29 helps construct and use a mathematical representation, including when no mathematical object has yet been selected. A.6.3.RT helps when the expression itself prevents the operation.

#### B.5.FM:4.4 - Obtain the smallest useful consequence

Work one case through the proposed relations. A direction of change, a limiting value, an obstruction or a small construction may answer the current question before a detailed numerical model is needed.

Show which premise makes the consequence follow. If calculation or simulation is needed, C.29.2 supplies computational formulation and C.29.3 supplies realization. If the reasoning is available but difficult to follow, B.5.RA helps recover the decisive inference.

Return the consequence to the question. A limiting value can rule out an intervention under the model's assumptions. A constructed recurrence can supply a count. An unresolved interaction can turn “calculate the system” into a specific request for another contribution.

#### B.5.FM:4.5 - Examine a choice that can change the answer

Challenge the model at a consequential choice: an omitted interaction, a grouping of cases, a fixed quantity, an operation rule or a correspondence. Use an available observation, a contrasting case or an inexpensive trial when it can distinguish the remaining alternatives.

An operation performed on a model establishes a model consequence. Reliance on a physical prediction also depends on the physical correspondence and conditions. Obtain the assurance needed for that receiving use; a sufficient conditional answer can remain useful while a premise is unresolved.

When a discrepancy has several possible explanations, retain those possibilities until the question needs them distinguished. B.5.MPC.R helps repair a failed physical, mathematical and computational connection. B.5.RR carries a changed premise through affected reasoning.

#### B.5.FM:4.6 - Apply the result and choose the continuation

Use what the model now supports: make a design choice, reject an option, construct an object, specify a calculation, select an observation or revise the question. Try the proposed use of that consequence. For example, sufficient average delivery can settle a capacity question; continuous supply also depends on delivery times, consumption and available stock. If the intended action needs such a further relation or condition, keep the supported answer and identify the missing contribution. Supply the assumptions another contributor needs to use the result.

Name a missing contribution by the result it must provide. For example, ask which heat-transfer path a proposed change affects, which state distinguishes two continuations, or which operation produces the needed formal object. A.15.9 helps obtain that contribution from another practice.

Keep an explanatory trace when later use or collaboration requires it. A new model-building move can also become material for C.39's method development and C.36.RP's shared-method renewal when that further work is needed.

### B.5.FM:5 - Archetypal Grounding

These constructed cases expose different model choices. Their calculations establish conditional consequences; no apparatus test is reported.

#### B.5.FM:5.1 - Choose the heat path before commissioning a calculation

An engineer asks whether a stronger external fan can bring an overheating component below 65 °C. Inspection finds the component attached to a metal case through a pad; the fan blows over the outside of the case.

Trace the proposed path from component to case and then to the surrounding air. Keep the component, the case at its attachment and the air distinguishable: their temperatures can differ, and the fan acts on one part of that path.

Try a steady account with constant component heating, all generated heat passing through the pad, and an unchanged linear conductance between component and case. Carrying the same heat per second then requires the same temperature difference across that path. Treat outward case-to-air transfer as driven by temperature difference. A steady case receiving positive heat must remain warmer than the air.

Use supplied steady readings of 80 °C at the component, 25 °C at the case attachment and 20 °C in the air. The component-to-case difference is 55 °C. Even ideal external cooling of the case to the air temperature leaves the component at 75 °C under these assumptions. The fan-only proposal cannot reach 65 °C in this model.

The result directs work toward the component-to-case contact, another heat path or reduced heating. Direct airflow onto the component would change the assumed path; temperature-dependent heating or conductance would change the fixed-difference argument. Measurement uncertainty matters to the real-device conclusion.

A useful next request is: “Can this component stay below 65 °C after changing its contact to the case, and which observations distinguish the relevant heat paths?” The model supplies that request before a detailed equation set is commissioned.

#### B.5.FM:5.2 - Include the air when modeling liquid discharge

Consider a rigid vessel with a liquid outlet near its bottom and trapped air above the liquid. The question is whether enlarging the outlet will allow most of the liquid to drain. A model based only on liquid height can miss what changes when liquid leaves.

For a first conditional account, assume that no air enters and the liquid is incompressible. Treat the trapped air as an ideal gas at constant temperature and fixed amount. Consider slow flow whose inertia is negligible and whose motion is dissipated by resistance at the outlet. Include the gas volume and absolute pressure, the liquid height above the outlet and the outside pressure. Liquid leaving increases gas volume and lowers gas pressure.

At the no-flow equilibrium, the internal pressure at the outlet equals the outside pressure. For the following rough calculation take liquid density as 1,000 kg/m³ and gravitational acceleration as 10 m/s². Initial liquid height is 20 cm, trapped gas volume is 100 cm³, vessel cross-section is 100 cm² and initial gas and outside pressures are both 100 kPa.

Let q be the discharged volume in cm³. The gas occupies 100+q cm³; liquid height is 20−q/100 cm. The isothermal gas relation and hydrostatic head give the equilibrium equation:

```text
10000/(100+q) + 0.1*(20−q/100) = 100   [kPa]
```

The positive solution is about 2.039 cm³, with gas pressure about 98.002 kPa and liquid height about 19.980 cm. In this slow-flow account, the discharge approaches a stop after a very small volume. Changing outlet size changes resistance and the approach to equilibrium; this same equilibrium balance applies while air entry and inertial effects remain negligible.

Allowing ambient air to reach the gas space changes the model: gas pressure can remain near outside pressure as liquid leaves. Air entering through the outlet, gas-temperature change, vessel deformation or appreciable capillary pressure requires another account. The immediate useful result is the distinction between an outlet-flow restriction and a gas-replacement restriction. Investigate the air path before treating outlet enlargement as the answer.

#### B.5.FM:5.3 - Construct classes that permit a counting inference

We need counts of binary strings at several lengths under a rule that forbids consecutive 1s. Use length four as a small case. The question supplies symbols and a restriction, but no recurrence.

Start with short valid prefixes and examine their allowed next symbols. A prefix ending in 1 may receive only 0. A prefix ending in 0 may receive either symbol; the empty prefix has the same two permissions. Group prefixes by those extension permissions.

Let r_n count valid length-n prefixes that are empty or end in 0; let b_n count those ending in 1. Every valid prefix can receive 0, while only the r_n prefixes can receive 1:

```text
r_0 = 1, b_0 = 0
r_(n+1) = r_n + b_n
b_(n+1) = r_n
```

The pairs for lengths 1 through 4 are (1,1), (2,1), (3,2), (5,3). There are eight valid strings of length four.

The inference works because each extension produces a distinct string, deleting its final symbol recovers its unique predecessor, and the two resulting classes exhaust the permitted cases. The total alone does not tell how many prefixes permit appending 1; keeping the two classes makes that operation possible.

If the restriction changes to “no three consecutive 1s”, the same grouping loses a needed distinction. Separate prefixes with zero, one or two trailing 1s and reconstruct the permitted transitions. This change identifies what the state must retain; the subsequent recurrence or program is a further computational contribution.

### B.5.FM:6 - Bias-Annotation

The examples use small explicit accounts so that the reader can inspect the construction. Complex systems can require learned representations, instruments and multiple specialist contributions. Their suitability depends on the inference and available means.

Source studies of human scientific work motivate some construction moves. Their transfer to AI agents concerns the work to perform and the result to supply; it does not assert identical cognitive mechanisms or learning requirements.

### B.5.FM:7 - Conformance Checklist

- The working question identifies a consequence that would help a receiving use.
- Selected participants and distinctions support that inference.
- Proposed relations have interpretable participants, conditions and appropriate subject grounds.
- Coupled quantities and operation rules are used consistently.
- At least one useful consequence is worked through, or the missing contribution is identified.
- The consequence is returned with the conditions needed for its application.
- Further refinement, observation or assurance answers a remaining question that matters to use.

### B.5.FM:8 - Common Anti-Patterns and How to Avoid Them

| Recognizable failure | Repair |
| --- | --- |
| Fit a model whose variables cannot express the proposed intervention. | Recover the participants and relations through which the intervention could change the result. |
| Copy a familiar analogy while its operation has a different meaning in the present case. | Construct the needed correspondence and test the transferred consequence. |
| Aggregate cases before performing an operation whose permissions differ between them. | Keep the permission-changing distinction until that operation is complete. |
| Increase simulation detail while an omitted interaction determines the answer. | Obtain a limiting or contrasting case that exposes that interaction. |
| Give a specialist a broad modeling request that leaves the needed result unclear. | Supply the provisional account and ask for the contribution that would change the next decision. |

### B.5.FM:9 - Consequences

A first model can turn an open request into an answer, a bound or a well-formed next contribution. It makes model-building choices available for criticism and allows others to continue the reasoning.

Its cost is the work of selecting and connecting distinctions. Keep an adequate simple account while its conditions suffice; develop it when the receiving question exposes a consequential limitation.

### B.5.FM:10 - Architectural Rationale

Model construction and model use often develop together. Trying an operation reveals which distinctions are missing, while the revised distinctions permit another inference. The method therefore keeps selection, relation construction, expression and consequence in one connected reasoning move.

The heat case depends on separating temperatures and locating an intervention along a path. The vessel case requires coupling two interacting media. The counting case creates classes from permitted operations. Their shared method is the construction of an inferentially useful account; their subject premises remain different.

B.5 coordinates the overall inquiry. This method develops its model-building contribution. B.5.4 gives a narrower entry when an available concept needs a situational interpretation. C.29 supplies mathematical representation choice. A.3.3, C.16 and A.6.3.RT supply state, measurement and expression construction when those questions occur within model building.

### B.5.FM:11 - SoTA-Echoing

**Construction as a reasoning contribution.** Adapt Nersessian's [2025 account, §3](https://onlinelibrary.wiley.com/doi/10.1111/tops.12777): a useful analogy may have to be built, with its correspondence revised during use. The present method applies that contribution in :4.2–:4.4: select distinctions through a needed consequence, build compatible relations and use a small case to revise the correspondence. Reusing a calibrated domain model is cheaper when it already expresses the proposed change. Constructing another account becomes worthwhile when the available model cannot express a consequential interaction or operation; the vessel and prefix cases show those failures.

**Qualitative consequences and application.** The [ISLE explanation by Etkina and Brookes](https://www.islephysics.net/why-isle.html) connects observation, proposed explanation, predicted consequence, testing and application, first qualitatively and then quantitatively. Use that progression in :4.4–:4.6 when a physical prediction needs examination and application. A formal construction can instead proceed from its formation rules and a derivation, as in :5.3.

**Subject premises of the physical cases.** [OpenStax, University Physics 2, §1.6](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer) supplies the conducting-layer and convection relations. [Volume 2, §2.1](https://openstax.org/books/university-physics-volume-2/pages/2-1-molecular-model-of-an-ideal-gas) supplies the isothermal fixed-amount gas relation; [Volume 1, §14.1](https://openstax.org/books/university-physics-volume-1/pages/14-1-fluids-density-and-pressure) supplies the hydrostatic pressure relation. The chosen arrangements, simplifications and receiving questions are the present constructions.

Reopen the method when another construction approach supplies a more useful model at comparable effort, or when a recurring difficulty calls for a model-building move absent from this account.

### B.5.FM:12 - Relations

- **B.5** coordinates inquiry; **B.5.4** constructs a supplied concept's correspondence to a situation.
- **C.29** selects and uses a mathematical representation. **C.29.1, C.29.2 and C.29.3** supply transfer, computational formulation and realization.
- **A.3.3**, **C.16** and **A.6.3.RT** supply state, measurement and expression construction.
- **B.5.RC** and **B.5.RA** recover an available construction or argument. **B.5.RR** revises reasoning; **B.5.MPC.R** repairs a failed joint physical answer.
- **C.11.DUA** governs worthwhile further effort; **A.15.9** obtains another practice's needed result.
- **C.39**, **C.36.RP** and **E.10.INT** support later method development, shared-method renewal and recovery of the interest guiding further work.

### B.5.FM:End
