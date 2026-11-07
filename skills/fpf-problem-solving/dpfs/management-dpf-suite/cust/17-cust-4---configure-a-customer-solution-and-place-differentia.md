## CUST.4 - Configure a Customer Solution and Place Differentiation

> **Type:** Method pattern
> **Status:** Stable

### CUST.4:1 - Problem frame

Use this method when a supported family offers meaningful choices, but selecting a valid configuration or arranging customer-specific work remains difficult. It also applies when early preparation creates waste or late customization creates unacceptable delay.

Begin with the customer's use and the family’s actual conditions. Select a fitting combination and decide which work can be done before the customer is known and which must await their order, information or participation.

If the required result is outside the family, return the difference to CUST.2 or CUST.3. A configurator is not a reason to force the customer into an unsuitable result.

### CUST.4:2 - Problem

A technically selectable combination may be unusable, confusing or too expensive to provide. Standardization can leave customers unable to identify a fitting choice. Postponement can reduce premature commitment but move essential work into the time when the customer expects delivery. Configuration therefore joins meaningful choice with feasible differentiation.

### CUST.4:3 - Forces

| Tension | Choice to make |
| --- | --- |
| Useful variety and decision burden | Which choices matter to the recipient, and which can be safely handled by a default. |
| Early preparation and wasted work | How much common work can be completed before uncertain demand is known. |
| Late differentiation and lead time | What customer-dependent work can actually finish inside the promise. |
| Customer autonomy and qualified assistance | When a person can choose directly and when an expert must help. |
| Technical option and service obligation | Whether the selected variant changes support, evidence, access or responsibility. |

### CUST.4:4 - Solution

#### CUST.4:4.1 - Translate the customer situation into consequential choices

Recover the intended result, operating environment, timing, recipient capability and constraints. Separate requirements from preferences. An inaccessible environment can rule out an offering; a preferred report layout may be an optional adaptation.

Use the family's variation rules to identify live choices. Explain each in the customer's terms: what changes in result, effort, delay, support or responsibility. Do not expose every internal parameter as a customer decision. A default is useful when its assumptions are visible and it does not conceal a consequential trade-off.

Check understanding where a term can change selection. “Managed” might mean software hosting to the provider and complete operating responsibility to the customer. Resolve that difference before comparing prices or configurations.

#### CUST.4:4.2 - Help the customer navigate the solution space

Eliminate combinations that violate a necessary condition. Compare the remaining alternatives by the differences that matter for the intended use. Present a manageable subset with the reason for exclusion or preference; preserve access to a qualified exception when the subset does not fit.

A direct configurator suits choices whose consequences the recipient can understand and whose rules are sufficiently expressed. Assisted selection suits unfamiliar consequences, coupled options or incomplete information. A demonstrated example can expose meaning better than another field in a form. Obtain the customer's missing input only when it can change the choice.

Use defaults and recommendations as explained assistance, not hidden commitments. When a choice transfers work to the recipient, show that work. For example, customer-hosted delivery may require local monitoring, updates and access arrangements that provider-hosted delivery supplies differently.

The result is a selected or short-listed combination with fit grounds and remaining conditions. If no combination fits, say what fails and return the substantive difference. Do not add an unqualified option merely to make the form submit.

#### CUST.4:4.3 - Place common work and customer-dependent work

For each consequential activity, ask what information or commitment must be known before it can be performed correctly. This identifies the point where customer-specific work begins, often called the customer order decoupling point in production settings.

Compare at least the feasible early and late arrangements. Common preparation might include a base assembly, a tested module, a training method or a reserved service slot. Customer-dependent work might include final assembly, calibration, semantic mapping, local training or permission-dependent configuration.

| Arrangement | Potential benefit | Condition to test |
| --- | --- | --- |
| Prepare a complete variant early | Short response after selection. | Demand and allowed variation justify inventory, reservation or maintenance of that variant. |
| Prepare a common base, finish after selection | Reuse of preparation with less premature differentiation. | Final work, inputs and qualified performers remain available within the promise. |
| Start most work after the order | Less speculative preparation and greater local adaptation. | Lead time, workload and cost remain acceptable. |
| Obtain a partner contribution at the needed point | Access to a capability or location not held internally. | The contribution, coordination and failure response are actually obtainable. |

Do not assume later is always better. Late calibration can become the bottleneck. Early software preparation can avoid customer delay but require maintaining many variants. Physical stock and software configuration have different cost and failure models; carry only the relevant dependence idea between them.

#### CUST.4:4.4 - Construct the complete chosen route

Follow the selected member from preparation to acceptance. Name the customer-dependent input, its supplier and required arrival time. Join it to the operation that consumes it. Resolve what happens if it is late, ambiguous or unusable.

Obtain an operating-capacity result through [OPS.10 — Qualify Operating Capacity Under Variability](../ops/40-ops-10---qualify-operating-capacity-under-variability.md) when variability or a shared resource can defeat the timing. Receive more than an average utilization figure: use the relevant demand mix, waiting, variability, resource availability and supported operating conditions. Revise the differentiation point or promise if they do not fit.

Use CUST.6 where the route itself needs a repeatable delivery method. Use CUST.7 for the complete resource comparison. A configuration with a shorter quoted installation can be worse when qualification, customer preparation or support is included.

#### CUST.4:4.5 - Reopen the form of provision when it changes the answer

Sometimes the live alternatives are not variants of the same service. Buying an engineered result, receiving a maintained service and contracting for a bounded outcome distribute work and responsibility differently.

Use [SYSE.8 — Develop an Integrated Offering and Provider Concept for Using an Engineered Result](../../engineering-dpf-suite/syse/29-syse-8---develop-an-integrated-offering-and-provider-concept.md) for its full integrated offering and provider-concept method when that engineered-result question applies. Supply the needed use result and candidate arrangement. Receive the contributing systems and parties, required customer participation, operating concept, observation and acceptance, responsibilities and risk conditions. Then test whether this concept fits the family, delivery capacity, resource comparison and existing commitments.

Observation alone is not influence over an outcome. A provider need not control every causal factor, but the promise must be compatible with its actual means, the other parties' contributions, disturbances and the agreed consequences of failure. If the concept cannot support the proposed outcome, choose a narrower contribution, obtain further subject-specific evidence or decline that promise. Obtain the relevant professional method and evidence when the promised result extends beyond engineering.

#### CUST.4:4.6 - Make the selected configuration usable and revisable

Give the recipient and delivery participants the chosen result, variations, required contributions, timing, support and acceptance conditions. Where choices are reversible, preserve a cheap return; where changing them later creates rework or obligation, make that consequence visible before commitment.

Return recurring no-fit requests to CUST.3 as evidence about the solution-space boundary. Return an isolated unsupported difference to CUST.2 for local disposition. Preserve the selected configuration identity for later support and CUST.8 transitions.

### CUST.4:5 - Archetypal Grounding

A test-bench supplier can stock complete benches, stock a common base and install measurement modules after the order, or build everything after the order. The customer needs a qualified measurement range and a delivery date, not a catalogue of every internal component.

The supplier first excludes module combinations whose joint accuracy is unqualified. It then compares two supported choices: a stocked complete bench available sooner, and a base with later calibration providing the requested range. The latter saves speculative variant preparation only if a calibration slot and the required module are available. A queue at calibration can make the apparently leaner arrangement miss the promise.

The selected route reserves the module and calibration resource, obtains the customer's range confirmation before final work and states the acceptance evidence. If the customer changes the range afterward, the route returns to fit and resource qualification rather than silently substituting a module.

In an analytical service, private hosting is not “inventory” in the same physical sense. The common deployment tooling may be prepared early, but identity, access and data interpretation must be resolved with the customer. The relevant postponement question concerns dependency and timing, not stock cost copied from manufacturing.

### CUST.4:6 - Bias-Annotation

Choice reduction can become paternalistic, while unlimited choice can transfer design work to an unprepared customer. Explain consequential exclusions and offer assistance where the recipient cannot reasonably infer effects.

The production vocabulary can overfit material flows. Use subject-specific models for services and digital provision.

### CUST.4:7 - Conformance Checklist

- Are live choices expressed through the customer's result and consequences?
- Are infeasible combinations excluded for stated reasons?
- Does a recommendation expose transferred work and responsibility?
- Is the customer-dependent work placed where its inputs and capacity are obtainable?
- Has the complete timing and resource effect been considered?
- Does a changed form of provision have its own supported responsibility and evidence basis?

### CUST.4:8 - Common Anti-Patterns and How to Avoid Them

**The interface permits it.** Check useful fit and provision, not only syntactic validity.

**Postpone everything.** Retain early work whose later execution would defeat timing or quality.

**Outcome is a pricing option.** Reconstruct the provider and responsibility concept before changing the promise.

**No-fit becomes a hidden custom variant.** Return it explicitly to family development or bounded local work.

### CUST.4:9 - Consequences

The method can make variety usable and reduce premature differentiation. It can also justify earlier preparation, fewer options or assisted selection. Each has operating and maintenance costs.

The supported result is a choice and delivery arrangement under named conditions.

### CUST.4:10 - Architectural Rationale

Configuration and differentiation are joined because a selected option determines work, timing and responsibility. Treating choice as a front-end task and postponement as a back-end task can hide their common constraint: the recipient must actually obtain the chosen result.

### CUST.4:11 - SoTA-Echoing

The method joins Salvador, de Holan and Piller's choice navigation and robust process design with the customer order decoupling tradition. The primary abstract of Harfeldt-Berg and Olhager's 2024 review supports considering multiple contextual factors.

Naldi, Galizia and Bortolini's optimization study shows a concrete storage-cost/customization-time trade-off under explicit demand, availability and cost assumptions. CUST adopts the need for a joint comparison and rejects a universal rule that postponement is best. Use a qualified optimization model when its assumptions fit; use the supported operating comparison when they do not.

The full SYSE.8 method supplies the engineering offering branch. Reopen this method's arrangement when an observed queue, customer burden or responsibility change defeats its present selection rule.

### CUST.4:12 - Relations

CUST.3 supplies the supported solution space; CUST.2 receives differences outside it. CUST.6 develops the delivery method, CUST.7 compares total burden and CUST.8 uses the retained configuration in later transitions. CUST.4 can also be used directly for an already established family without a new CUST.1 programme.

### CUST.4:End
