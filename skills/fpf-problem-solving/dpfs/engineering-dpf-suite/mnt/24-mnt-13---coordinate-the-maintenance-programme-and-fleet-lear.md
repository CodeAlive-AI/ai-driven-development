## MNT.13 - Coordinate the Maintenance Programme and Fleet Learning

> **Type:** Method
> **Status:** Stable

### MNT.13:1 - Problem frame

Use this pattern when maintenance decisions span a population of equipment and repeated work: which policies to retain, where support is inadequate and what can be learned from the accumulated history. A fleet report shows fewer failures in one group, but its operating exposure and maintenance conditions differ.

Return a qualified programme or fleet-learning decision. The result can be to retain an adequate programme, correct one misleading comparison or change a supported policy or resource arrangement. A fleet maintenance programme remains a maintenance question. An asset-management question can concern just one pump: compare continued use, renewal, replacement, repurposing or withdrawal by the desired value, costs, risks and service alternatives over the relevant horizon. Maintenance consequences inform that choice without settling it. Portfolio acquisition and disposal are further asset-management uses, not the scale boundary between the fields.

### MNT.13:2 - Problem

Local repairs can repeatedly succeed while the programme leaves the same failure, delay or support deficiency untouched. Conversely, crude fleet comparisons can trigger a large policy change on weak evidence.

A programme is the arrangement of maintenance policies, support and work for an identified population. Its document describes that arrangement. Writing a new programme does not establish that it was enacted or improved equipment performance.

### MNT.13:3 - Forces

Common policies and resources can improve continuity, but equipment, duty and consequences vary. Pooling data increases apparent sample size while possibly mixing unlike events. Fleet-wide improvement can consume access and specialist capacity needed for current service. Compare gains and burdens for operation, maintenance staff and affected service users.

### MNT.13:4 - Solution

Bound the population, service question and horizon. Identify the programme decision at stake: retain a policy, change a task, improve spare readiness, resolve a backlog or compare performance. An equipment-family name alone does not establish that units have comparable duty or failure behaviour.

Recover the event and exposure basis under [MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md) and MNT.12. Distinguish failures, inspections, preventive removals and incomplete observation. Compare units at compatible configuration, operating conditions and consequence where those differences can change the answer. Retain a stratified account when aggregation would conceal the difference.

Relate the observations to possible programme causes and actions. Repeated waiting for an applicable spare can justify a support decision without proving that the preventive policy is ineffective. A changed reporting rule can increase counted failures without worsening the machine. Use the failure and operating evidence to distinguish these interpretations.

Compare credible programme alternatives. Retain a sound existing arrangement, change one policy family, improve support, alter coordination or return a design question as appropriate. Include the total obtaining and continuing burden of the change, its effect on service and any protected trade-offs. A local cost reduction that increases shared downtime is not an unqualified programme gain.

When a deliberate improvement is selected, use [FPF E.23](../../../sections/11-part-e---the-fpf-constitution-and-authoring-guides/63-e-23---quality-improvement-loop-method.md)'s loop at this subject: name the programme arrangement and the maintenance contribution sought, choose the evaluation that will judge it, perform the selected change only when authorized, and compare the changed arrangement through the same relevant measures. Selection, implementation and observed effect remain different facts.

Choose further fleet inquiry only when its attainable result can change the decision enough to warrant its design, access, measurement, interpretation and displaced work. If current evidence already supports retaining the policy or fixing a known support deficiency, return that answer now. Sparse or incomparable data withholds the stronger causal claim, not every programme decision.

Return the decision with the population and evidence limits that affect its use. Identify the recurrence, changed duty, support failure or new professional result that would reopen it. A long-term learning question can remain open while today's programme answer is complete.

### MNT.13:5 - Archetypal Grounding

APP-MNT-02 is a constructed comparison of 48 pumps. Twenty units have four relevant failures over 20,000 operating hours; 28 units have six over 56,000 hours. The rates are 0.20 and approximately 0.107 events per 1,000 hours. Raw counts favour the first group, while exposure-adjusted rates favour the second.

Neither result establishes a causal policy effect. The engineer recovers duty, component histories, event definitions and the reasons units entered each group. The answer to “Do these counts justify replacing the fleet policy?” is no on this basis. In the retention branch of this constructed case, the policy's existing failure-and-response basis remains adequate for the stated duties; the counts do not establish that adequacy. Retaining the policy on that existing basis can be the completed decision while the support deficiency below is corrected. If that basis no longer holds, return the unsupported policy choice without waiting for these data to prove a rival policy.

The same current records identify an applicable spare unavailable for a known upcoming task. Correcting that support deficiency can be selected on its own evidence; the engineer does not wait for a new causal fleet study to address it.

If a different question warrants a policy comparison, its achievable design must account for the small event count, available population and operating constraints. It may support only a narrower conclusion. The first return remains valid without commissioning that further inquiry.

### MNT.13:6 - Bias-Annotation

Fleet averages can hide the units with the greatest exposure or service consequences. Improved reporting can appear as worse reliability. Programmes also tend to count scheduled labour while omitting operator work, waiting and corrective disruption. Preserve those differences where the decision depends on them.

### MNT.13:7 - Conformance Checklist

Is the population and receiving programme decision clear? Do event meanings, exposure and observation conditions support the comparison? Are causal and descriptive claims distinguished? Does the selected change improve the intended maintenance contribution without concealing moved burden? If implementation or improvement is claimed, is that claim supported separately from the proposal?

An adequate retained programme or qualified fleet account is a completed answer. Further inquiry needs its own attainable contribution and burden justification.

### MNT.13:8 - Common Anti-Patterns and How to Avoid Them

Fewer failures are read as a better policy without exposure. Recover a compatible comparison. A dashboard target is improved by recoding failures rather than changing functioning. Preserve event meaning and compare the actual programme contribution.

Every incomplete causal explanation becomes a research programme. Return the supported maintenance decision first and select only the inquiry that can improve a real next use.

### MNT.13:9 - Consequences

Repeated work can change the programme when the evidence warrants it, while adequate policies avoid unnecessary churn. Some comparisons remain descriptive or population-limited. Learning effort is directed toward maintenance decisions rather than data accumulation for its own sake.

### MNT.13:10 - Architectural Rationale

Programme coordination joins policies, support and population evidence because changes in one can explain apparent changes in another. It is broader than [MNT.2](13-mnt-2---select-and-reopen-the-maintenance-policy.md)'s task policy and [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md)'s present intervention, but does not subsume the asset-value choice for one asset, an asset System or a portfolio. The question and justified result distinguish the contributions; the number of assets does not.

[FPF E.23](../../../sections/11-part-e---the-fpf-constitution-and-authoring-guides/63-e-23---quality-improvement-loop-method.md) supplies the reusable improvement organization. This pattern supplies the maintenance population, event meaning, response alternatives and operating consequences that make the loop useful here.

### MNT.13:11 - SoTA-Echoing

The question is how fleet evidence should change a maintenance programme. This pattern adapts GFMAM's programme-management breadth and the consequence-oriented evaluation concern in the 2025 NIST review, with [FPF E.23](../../../sections/11-part-e---the-fpf-constitution-and-authoring-guides/63-e-23---quality-improvement-loop-method.md) supplying conditional improvement. Against raw-count ranking or automatic technology expansion, the Method uses the qualified population comparison and separate support-deficiency decision. It accepts narrower conclusions when comparison is weak, preserving a useful current answer. Neither source proves that a particular policy will win in this fleet. Reopen with changed exposure, failure meaning, operating consequences or applicable evaluation evidence. See [GFMAM](https://www.gfmam.org/sites/default/files/2021-02/GFMAM%20Maintenance%20Framework%20-%202nd%20Edition%20Final.pdf) and [NIST's evaluation review](https://www.nist.gov/publications/comprehensive-evaluations-condition-monitoring-based-technologies-industrial).

### MNT.13:12 - Relations

[MNT.2](13-mnt-2---select-and-reopen-the-maintenance-policy.md) supplies policies, [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) support and [MNT.12](23-mnt-12---maintain-maintenance-information-and-configuration.md) usable history. [MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md) qualifies failure claims; [MNT.14](25-mnt-14---compare-maintenance-methods-for-retention-or-change.md) compares Method changes and [MNT.16](27-mnt-16---deliberately-continue-and-change-maintenance-cultur.md) addresses actual continuation in the practice. [FPF E.23](../../../sections/11-part-e---the-fpf-constitution-and-authoring-guides/63-e-23---quality-improvement-loop-method.md) supplies improvement, [FPF C.16](../../../sections/09-part-c---kernel-extension-specifications/27-c-16---measurement-metrics-characterization.md) measurement and [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) conditional inquiry. Engineering Asset Management receives the specific investment or retirement question when maintenance cannot settle it.

### MNT.13:End
