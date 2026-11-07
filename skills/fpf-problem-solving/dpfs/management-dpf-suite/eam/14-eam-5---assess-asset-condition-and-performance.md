## EAM.5 - Assess Asset Condition and Performance

> **Type:** Method
> **Status:** Stable

### EAM.5:1 - Problem frame

Use this pattern when condition observations or service performance can change an asset decision. A warning appears on a dashboard while the asset continues delivering service, or apparently good availability conceals deterioration.

Start with the claim the decision needs. Return an applicable account of observed condition, its supported interpretation and the service consequence. Reuse an adequate maintenance or operating result instead of commissioning another assessment.

### EAM.5:2 - Problem

Condition, delivered performance and future failure are different claims. A vibration increase can be real without identifying its cause or remaining life. Successful service during one interval can coexist with a condition that requires intervention. Aggregating them into a single health score can hide the reason an option is eligible or unacceptable.

### EAM.5:3 - Forces

Earlier interpretation can improve response while false signals cause unnecessary work. More observations can clarify deterioration but impose access, analysis and delay costs. The useful resolution depends on the asset choice, duty, consequences and time available.

### EAM.5:4 - Solution

Identify the asset, installed configuration, required functioning and decision horizon. Recover the condition account from [MNT.4](../../engineering-dpf-suite/mnt/15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) when available. Check the measurement location, method, units, operating state, observation window and relevant limitations before comparing values.

Keep observed, inferred and forecast claims separate. State what changed in the observations, what the applicable diagnostic evidence supports and what future-duty assumptions a forecast requires. Use a specialist's diagnosis where the mechanism matters; an alarm alone does not supply it.

Recover the relevant service-performance evidence. The useful content from [OPS.18](../ops/52-ops-18---control-operating-quality-and-reliability.md) might be an affected population, observed loss, quality result or reliability evidence, with its requirement and window. A favorable operating decision is not an asset-condition certificate.

Relate condition and performance to the proposed options. Identify what contribution is at risk, the consequence of delay and the supported intervention effect. Distinguish a condition ranking from risk: risk additionally depends on the exposure, uncertainty and consequence needed for this decision.

Reconcile apparent disagreements before drawing a stronger conclusion. A change in sensor, load or reporting population can explain a discontinuity. When no adequate correspondence exists, retain separate accounts and state the claim they cannot jointly support.

Return the supported interpretation and its implication for [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) or EAM.8. Ask for more evidence only when its attainable result could change the option, response or justified claim enough to warrant the full burden. If the existing condition assessment answers the recipient's question, provide it and finish the inquiry. Estimate remaining life only when that further answer is needed.

### EAM.5:5 - Archetypal Grounding

In the constructed D case, the supplied maintenance account identifies abnormal increasing vibration under comparable duty. A separate specialist diagnosis and policy qualification support the initial intervention and five-year continued-use policy under stated conditions. Those are distinct premises; the vibration observation does not establish the policy by itself.

Suppose the operating record also shows delivery meeting the service requirement during the observed month. The practitioner can report both maintained service during that month and abnormal condition needing the supported response. Neither claim erases the other.

If later inspection finds a different structural defect outside the policy's qualification, the EAM practitioner removes D continuation from the eligible alternatives. The portfolio changes to FFLR under the common application's unchanged limits. A continued green service dashboard does not restore the invalid engineering support.

### EAM.5:6 - Bias-Annotation

Easily measured signals can dominate attention while poorly observed failure mechanisms are neglected. Preserve the measurement's actual coverage. A predictive model's apparent precision can also disguise a duty change or insufficient evidence for its receiving use.

### EAM.5:7 - Conformance Checklist

Do the records concern the same asset and duty? Are observation, diagnosis, forecast and service result distinguishable? Does the inferred consequence follow from applicable evidence, and is the option's qualification still valid?

### EAM.5:8 - Common Anti-Patterns and How to Avoid Them

Interpreting a health score as a remaining-life date gives an unsupported forecast. Recover the model and duty assumptions or report the narrower condition result.

Interpreting current service success as proof of sound condition ignores deterioration. Keep the actual condition and functioning claims separate.

### EAM.5:9 - Consequences

The asset decision can use the available evidence without overstating it. Some options become conditional or ineligible; some investigations are unnecessary for the bounded answer. Remaining uncertainty is visible at the claim it limits.

### EAM.5:10 - Architectural Rationale

The pattern joins condition and performance at their asset consequence while leaving diagnosis, measurement and operating decisions with their supplying practices. A single score is convenient only when its construction and intended use preserve the distinctions the choice needs.

### EAM.5:11 - SoTA-Echoing

For deciding what the available condition evidence implies for an asset option, adopt the separation of observation, interpretation and forecast in [MNT.4](../../engineering-dpf-suite/mnt/15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md), and use the applicable service-evidence component of OPS.18. The Solution matches those claims to the actual unit and duty before using them in eligibility or consequence reasoning. In D's case, the supplied diagnosis and policy qualification support the continued-use option while the observed vibration alone supports a narrower condition statement.

A serious technical alternative, when the asset choice needs a life forecast, is to fit a degradation model and project time to a supported failure criterion. The NIST/SEMATECH *e-Handbook of Statistical Methods*, [section 8.4.2.3, “Fitting models using degradation data instead of failures”](https://www.itl.nist.gov/div898/handbook/apr/section4/apr423.htm), supplies an established regression-based comparator and its physical, measurement and model assumptions. It is useful where that relationship and future-duty transfer are supported; a vibration trend by itself does not supply them. Adapt this modeling route when an obtainable life forecast could change the asset policy or timing. For the already qualified D alternatives, developing it anew would add data, fitting and validation work without being necessary for the stated comparison. The trade-off is a supported option implication with no independently derived remaining-life date. Neither the handbook nor [MNT.4](../../engineering-dpf-suite/mnt/15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) supplies a real pump's failure threshold. Reopen the choice when the diagnosis, duty or policy qualification changes, or when a forecast's expected decision contribution justifies the work of establishing its applicable model and evidence.

### EAM.5:12 - Relations

[EAM.3](12-eam-3---establish-the-asset-information-and-configuration-ba.md) establishes the information match. [MNT.4](../../engineering-dpf-suite/mnt/15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) supplies condition interpretation and [MNT.6](../../engineering-dpf-suite/mnt/17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) diagnosis and intervention content. [OPS.18](../ops/52-ops-18---control-operating-quality-and-reliability.md) supplies the relevant operating evidence. [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) assesses consequences and capability; [EAM.8](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md) uses the account in asset alternatives. [FPF A.10](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/07-a-10---evidence-graph-referring-claim-bound-evidence-and-pro.md) and [FPF C.16](../../../sections/09-part-c---kernel-extension-specifications/27-c-16---measurement-metrics-characterization.md) support the relied-on evidence and measurement claims.

### EAM.5:End
