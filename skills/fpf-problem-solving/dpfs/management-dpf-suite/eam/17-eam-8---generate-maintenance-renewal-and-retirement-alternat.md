## EAM.8 - Generate Maintenance, Renewal, and Retirement Alternatives

> **Type:** Method
> **Status:** Stable

### EAM.8:1 - Problem frame

Use this pattern when an engineered asset's future use is in question: retain it with maintenance, renew it, replace it, repurpose it or withdraw it. A feasible repair has been proposed, but the decision maker needs comparable asset policies over the relevant service horizon.

Return supported or explicitly conditional alternatives, with the consequences needed for value comparison. An adequate existing set can be reused. If the only question is which intervention maintains the already chosen function, the maintenance recommendation may answer it directly.

### EAM.8:2 - Problem

A repair estimate describes one intervention. It can omit years of energy, inspection, support and further work. A replacement estimate can omit commissioning, service interruption, exit cost or remaining value. Comparing those estimates as if they described the same service policy produces a misleading choice.

Continued use can also become a fictitious zero-cost alternative when its required maintenance and fallback are omitted. Ending a spreadsheet after two years does not establish that the asset stops working then or that its remaining contribution is worthless.

### EAM.8:3 - Forces

Early replacement can reduce continuing burden but discard useful service life. Renewal can preserve infrastructure while retaining a limiting design. Withdrawal can avoid future cost while removing a needed contribution. Long-horizon comparisons need enough detail to expose those consequences while retaining uncertainty about future duty and condition.

### EAM.8:4 - Solution



#### EAM.8:4.1 - Establish the service that each policy must support


Recover the required service, asset configuration and horizon. Use the relevant condition and diagnostic account to establish which maintained-use responses are supported. [MNT.4](../../engineering-dpf-suite/mnt/15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) supplies condition interpretation; [MNT.6](../../engineering-dpf-suite/mnt/17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) supplies the diagnosis and intervention recommendation. Their result must apply to this asset and proposed duty.

Form policies rather than isolated job labels. A continued-use policy includes its initial intervention, recurring maintenance, permitted duty, contingency and exit conditions. A renewal policy states what capability or useful life it changes. Replacement includes the new asset's integration and the old asset's disposition. Repurposing names the different receiving use; withdrawal names how a still-required service will be supplied or the decision that ends that requirement.

Lay out the period covered by each technical qualification. An initial repair supported for three years cannot by itself supply a four-year policy. Obtain the further intervention, replacement or service alternative that closes the remaining interval. Where condition determines the next work, state the observation and threshold that trigger it, the time needed to respond and how service remains supported while responding. A conditional forecast retains its duty and mechanism assumptions.

Keep technical eligibility separate from preference. Label an option conditional when a decisive engineering, support or permission result is missing. A proposal can be worth discussing while that result is sought, but it cannot be treated as a feasible immediate act.



#### EAM.8:4.2 - Construct the dated consequence account


For each policy, follow the work and use through time: initial preparation and integration, recurring operation and support, subsequent interventions, interruptions and temporary provision, and the intended ending. Attach each consequence to its cause and date. Include the whole intervention and return to service supplied by [MNT.7](../../engineering-dpf-suite/mnt/18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md); the time spent physically repairing equipment alone can understate the interruption. Carry the resulting work and service conditions into EAM.11.

Then obtain the economic consequences of that same policy. [FIN.6](../fin/19-fin-6---value-capital-projects.md) develops a dated incremental cash account: compare the proposed policy with its actual alternative, include changed operating and investment cash, and distinguish historical expenditure from future avoidable consequences. Identify the asset and configuration, receiving service, comparison perspective and date, price and discount-rate basis, relevant tax and financing treatment, and ending premise. Ask the finance supplier to return the amounts and dates, significant assumptions and unresolved limits. Its corporate-finance assumptions apply only where appropriate to the receiving case.

A recurring service price may already include maintenance, response or replacement. Check those inclusions before adding separate allowances. Conversely, a required future overhaul is still a consequence when it falls outside the current capital request. Preserve unpriced service loss, safety, environmental or other material consequences for [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md) instead of silently treating them as zero. A finance result values the stated policy; it does not establish that the policy can supply the service.



#### EAM.8:4.3 - Reconcile horizon and ending


Place the alternatives on a common service and analysis horizon. If their technical lives differ, describe the further work needed to cover that horizon or obtain an applicable value of remaining service. A repeating replacement chain needs supported availability, duty and cost assumptions; extending an annuity factor cannot supply them.

Distinguish the end of the study from the end of use. If the asset continues beyond the explicit account, obtain a remaining-value estimate consistent with that continuation and its further support needs. [FIN.7](../fin/20-fin-7---value-assets-and-the-corporation.md) develops valuation under a stated continued-use or disposal premise. If the asset will actually be withdrawn, use realizable proceeds and the dated cost of disconnection, disposal, closure or replacement service as applicable. Book value alone supplies neither answer. Do not add liquidation proceeds for resources whose continuing use is already included in the terminal value.

When only the explicit table endpoint moves, reconcile the value at the new endpoint with the same later payments and ending premise. The whole policy's present cost remains the same. If a supplied valuation disagrees, use [FIN.7](../fin/20-fin-7---value-assets-and-the-corporation.md) to identify the changed cash, dates, rights or assumptions before relying on it.

Use constant prices with a real discount rate, or a consistent current-price basis with its corresponding rate. Changing the required service horizon calls for reconsidering which interventions occur, which support still applies and what ending is being valued. If the service itself ends, reconsider withdrawal and other alternatives.



#### EAM.8:4.4 - Return comparable choices and their conditions


Compare eligible policies using the applicable criterion in EAM.9. Return their service and configuration, dated work and consequences, ending premise, technical support and material conditions. [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md) can then combine them without losing a later funding need or counting shared work twice.

Retain the smallest alternative set that includes materially different feasible ways to meet the need. Obtain more diagnosis or costing only when an attainable answer could change eligibility, preference or the requested claim enough to justify its full burden. If [EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) reports a changed duty, price or support result, revise the affected policy and its recipients; an unrelated qualified policy need not be reconstructed.

### EAM.8:5 - Archetypal Grounding



#### EAM.8:5.1 - Constructing a four-year policy


Consider a separate constructed asset E supplying the same required service under two technically qualified policies. All amounts are constant-price €million; the comparison uses a 3% real rate, year-end cash and sufficient resources for either policy. Tax and financing differences are held equal.

Policy X retains E: initial work costs 0.40 and supports its duty through year three; a 0.90 overhaul at the end of year three supplies the further support needed for year four. Policy Y replaces E initially for 1.50 and has qualified support throughout the four years. The following account includes recurring operation and routine maintenance separately from the overhaul.

| Consequence and date | Retain and overhaul X | Replace Y |
| --- | ---: | ---: |
| Initial work at year zero | 0.40 | 1.50 |
| Recurring cost at each year end, years 1–4 | 0.30 | 0.15 |
| Further work at the end of year three | 0.90 | 0 |
| Value of continued use at the end of year four | 0.20 | 0.50 |

The teaching qualifications include permitted eight-hour work windows and temporary service sufficient to preserve the requirement during initial work and X's later overhaul. The corresponding costs are included in the initial and overhaul amounts. That makes the policies service-comparable; omitting the later window or temporary provision would leave X conditional. No other material consequence distinguishes the eligible policies in this example.

At 3%, the four-year annuity factor is 3.717098, the year-three discount factor 0.915142 and the year-four factor 0.888487. X's present cost is `0.40 + 0.30 × 3.717098 + 0.90 × 0.915142 − 0.20 × 0.888487 = 2.161060`. Y's is `1.50 + 0.15 × 3.717098 − 0.50 × 0.888487 = 1.613321`. Replacement has the lower comparable cost. Omitting the overhaul would report X as 1.337432 and reverse the recommendation while removing the work needed to support year four.

Now move the end of the explicit cash table to year two, keeping both complete policies, the required service, the rate and all later amounts unchanged. Express the remaining year-three and year-four cash, including the stated year-four continuing value, as an equivalent net value at year two:

- X: `V_X(2) = −(0.30 + 0.90)/1.03 + (0.20 − 0.30)/1.03² ≈ −1.259308`.
- Y: `V_Y(2) = −0.15/1.03 + (0.50 − 0.15)/1.03² ≈ 0.184278`.

These values represent the same remaining account on the cost-comparison basis. X's negative value means its later support payments exceed its discounted year-four continuing value. The common required service remains the same and its equal benefits are outside both cost accounts. The calculation does not estimate a sale price.

Let `a₂ = 1/1.03 + 1/1.03²` and `d₂ = 1/1.03²`. Using unrounded values, the shortened explicit accounts give X: `0.40 + 0.30 × a₂ − V_X(2) × d₂ = 2.161060`; Y: `1.50 + 0.15 × a₂ − V_Y(2) × d₂ = 1.613321`. Replacement remains cheaper. Moving the table boundary has moved later consequences into the ending value; it has removed neither their cost nor their service obligations. A different supplied appraisal needs reconciliation of its changed assumptions before it can support a different recommendation.

Actual withdrawal at year two is another case. If the authority ends the service and X incurs a net exit cost of 0.10 while Y yields net sale proceeds of 0.60, replace the continuing values with those consequences. Present costs are then 1.068300 and 1.221463. X is cheaper in this different case because the service requirement and exit consequences have changed. There is no year-three service obligation in this case. If the service remains required, withdrawal alone is incomplete: a qualified replacement service and its consequences must join the policy.



#### EAM.8:5.2 - Comparing the complete supplied policies for D


For the constructed D case, both policies supply the same required service for five years under their stated engineering qualifications. Continued use needs €0.50 million initially as operating expenditure and €1.00 million at each year end, with zero terminal value. Replacement needs €3.00 million capital, €0.35 million each year and has €1.20 million terminal value.

At a 3% real rate, the five-year annuity factor is 4.579707 and the terminal factor is 0.862609. The comparable present costs are 0.50 + 1.00 × 4.579707 = 5.079707 and 3.00 + 0.35 × 4.579707 − 1.20 × 0.862609 = 3.567767 million. The comparison therefore favors replacement when both options are eligible and resources are available.

The continued-use policy is supported for the stated horizon; a one-year forecast alone would not justify five-year use. If a new finding invalidates that support, the practitioner marks the policy ineligible before comparing cost. If instead the service is no longer required, withdrawal becomes a new alternative with its own exit consequences. [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md) examines D's choice together with competing assets.

### EAM.8:6 - Bias-Annotation

Retaining an asset can be favored because its purchase cost is remembered; replacing it can be favored because a supplier reports only purchase savings. Use the same receiving service and future-cost boundary, and disclose where data come from interested parties.

### EAM.8:7 - Conformance Checklist

Can the practitioner trace each policy from required service through supported intervals, later work and ending? Are its cash dates, unpriced consequences, horizon and valuation premise compatible? Can the recipient distinguish a supported option from a conditional proposal and identify what would change that distinction?

### EAM.8:8 - Common Anti-Patterns and How to Avoid Them

Treating “do nothing” as free hides maintenance and service consequences. Write the actual continued-use policy.

Treating a maintenance recommendation as the asset decision loses alternative service and lifetime-value questions. Preserve the recommendation and compare its policy with the other relevant options.

Using a valuation for a different date or continuation can create a false change in preference. Reconcile the remaining cash and ending premise before comparing.

### EAM.8:9 - Consequences

Decision makers obtain alternatives whose differences can be explained and recalculated. Some options are excluded, some remain conditional and some investigations stop. The result supports asset choice. The maintenance team carries out the intervention and returns the equipment to service under the applicable maintenance and operating decisions.

### EAM.8:10 - Architectural Rationale

This pattern joins maintained-functioning results to the asset-value question without merging them. A policy description exposes continuing consequences that a list of interventions hides. Keeping repurposing and withdrawal available prevents replacement from becoming the assumed end of a universal lifecycle.

### EAM.8:11 - SoTA-Echoing

NIST HB135e2025, chapter 4, develops the timing of initial, recurring, replacement and residual consequences on a common study period. That discipline supports the dated account here; its federal rates and programme rules are not adopted. A payback-only screen loses later support and the ending premise.

[FIN.6](../fin/19-fin-6---value-capital-projects.md) supplies the incremental financial construction, and [FIN.7](../fin/20-fin-7---value-assets-and-the-corporation.md) supplies a valuation consistent with continued use or actual disposal. Use their developed treatment when financial construction or appraisal is needed; retain a sufficient qualified local answer when it already supplies the result. EAM connects those returns to the technically supported asset policy.

### EAM.8:12 - Relations

[EAM.3](12-eam-3---establish-the-asset-information-and-configuration-ba.md) and [EAM.5](14-eam-5---assess-asset-condition-and-performance.md) supply applicable asset and condition information. [MNT.6](../../engineering-dpf-suite/mnt/17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) supplies the maintenance recommendation and [MNT.7](../../engineering-dpf-suite/mnt/18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) the whole intervention and return. [EAM.7](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md) supplies alternative ways of obtaining a changed service contribution. [FIN.6](../fin/19-fin-6---value-capital-projects.md) and [FIN.7](../fin/20-fin-7---value-assets-and-the-corporation.md) supply the dated financial account and qualified ending value; their perspective and conditions must match the asset policy. [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md) compares the policies, [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md) tests combinations and [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md) tests timing. [EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) returns changed premises. [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) governs the worth of further inquiry.

### EAM.8:End
