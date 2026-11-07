## MNT.3 - Establish Degradation and Failure Evidence for Maintenance

> **Type:** Method
> **Status:** Stable

### MNT.3:1 - Problem frame

Use this pattern when a fault code, alarm or repair history leaves the mechanism or consequence needed for a maintenance decision unclear. “Bearing failure” may describe an observed damaged part without explaining whether lubrication, alignment, contamination or another condition changes the next policy or intervention.

Establish a qualified failure account for the receiving question. The result connects observed departures from required function with the causes and consequences that current evidence supports. [MNT.4](15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) interprets a current measurement or trend; [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) uses a failure account to choose the present response. A complete root-cause inquiry is unnecessary when remaining explanations lead to the same adequate answer.

### MNT.3:2 - Problem

Observation, diagnosis and consequence are easily collapsed. A high vibration value is an observation under particular measurement conditions. A damaged bearing is a condition claim. A lubrication mechanism is a causal explanation. Loss of district-heating service is a possible System-level consequence. Evidence supporting one does not automatically support the others.

Maintenance history adds another ambiguity: a removed component may have failed, been replaced preventively or been removed because another fault was suspected. Counting all removals as failures can change a policy for the wrong reason.

### MNT.3:3 - Forces

Detailed inquiry may discriminate mechanisms, but it consumes access, specialist time and potentially destructive examination. Early restoration may destroy useful evidence; preserving every part indefinitely may also be wasteful. Sparse failures favour physical reasoning, while confident causal stories can ignore contradictory observations. The required resolution is determined by the decision the evidence must support.

### MNT.3:4 - Solution

State the functioning question and the failure claim that would change the decision. Separate a complete loss, degraded contribution and loss of a protective function. Define the event sufficiently for another reader to distinguish it from an inspection finding or preventive removal.

Recover available evidence at its actual scope. For a physical component, this can include operating conditions, measurements, photographs, inspection returns, installation and removal facts, applicable configuration and the sequence of earlier work. Preserve when and how observations were obtained. An occurrence reconstructed from an operator's report has a different evidential limit from a directly inspected fracture surface.

Build the smallest useful causal account. Connect the required function to the observed departure, candidate mechanism, local effect, System effect and consequence. A short table can keep alternatives visible:

| Candidate explanation | Observation it explains | Evidence that could change the maintenance choice |
| --- | --- | --- |
| Bearing damage | A supported bearing-related signal or physical finding | The specialist interpretation and applicable component inspection. |
| Alignment or installation problem | A change associated with installation or operating load | Existing alignment and installation records, or a justified discriminating check. |
| Measurement or operating-context change | A discontinuity matching sensor, speed or load change | Comparable measurement conditions and instrument information. |

These are example hypotheses, not a diagnostic rule for all pumps. Include a different mechanism when the actual evidence makes it consequential.

If you need to construct a causal account for the maintenance question or work out what could distinguish explanations that imply different responses, use [FPF C.28.CM - Construct and Challenge a Causal Model](../../../sections/09-part-c---kernel-extension-specifications/55-c-28-cm---construct-and-challenge-a-causal-model.md). Its [measurement-and-device case (FPF C.28.CM:5.2)](../../../sections/09-part-c---kernel-extension-specifications/55-c-28-cm---construct-and-challenge-a-causal-model.md#c28cm52---construct-the-measurement-and-device-mechanisms-separately) shows how two mechanisms can explain one reading yet imply different responses. Carry this maintenance question, competing mechanisms and observation conditions into that construction. Return with the consequences each account predicts, the observation that could distinguish them or the precise premise that prevents that comparison. Use an adequate existing diagnosis directly.

Distinguish what is supported, what remains plausible and what is contradicted. Do not turn a possibility into a cause by placing it in a fault-tree box. Where several explanations support the same immediate recommendation, return that recommendation's evidential basis and leave the stronger causal claim unresolved. Where the alternatives require different actions, identify the smallest attainable observation that could discriminate them.

For population claims, recover the denominator and observation process. Operating hours, starts, cycles, calendar exposure and units under observation answer different questions. A unit still operating at the end of observation has a known survival interval, not a known eventual lifetime. A preventive removal ends or changes that component's exposure; an overhaul may not restore it to an as-new state. Treat those distinctions explicitly before fitting or comparing a failure model.

When selecting an investigation, compare its obtainable contribution with the whole burden. Include the effect of delay, disturbance, specimen preservation and specialist interpretation. A low-value inquiry can stop while an adequate maintenance answer remains available. If a claim has high consequence, use the applicable evidence and assurance rules for that claim; more records alone do not establish it.

Return a failure account whose uncertainty changes action where necessary. Preserve evidence needed by a real later decision in the maintenance history. State a reopen condition, such as recurrence under a supposedly corrected condition or a newly inspected part contradicting the diagnosis.

### MNT.3:5 - Archetypal Grounding

In the constructed PS17 case, the available specialist interpretation and comparable condition history support recommending bearing replacement at a suitable outage. They do not establish why the degradation arose or whether a recurring programme-level defect has been eliminated.

The planner can therefore give the recommendation now. If the selected intervention exposes material damage, the team preserves the observations needed for the relevant later cause question. It does not claim a lubrication cause merely because the bearing is replaced.

The 48-pump example exposes a different error. Group A has four relevant failure events in 20,000 operating hours; group B has six in 56,000. The comparable crude event rates are 0.20 and approximately 0.107 per 1,000 hours. The first group has fewer events but a higher exposure-adjusted rate. Neither comparison proves a causal policy difference: operating conditions, component histories, event coding and selection may differ.

If two of the six records are preventive removals, even that crude rate needs correction before use. The useful result is a qualified failure account and the event-coding error, not an automatically fitted lifetime distribution.

### MNT.3:6 - Bias-Annotation

The part found damaged at dismantling can attract all causal attention even when an upstream condition produced its damage. Work-order codes can favour the easily named component over installation, operating or maintenance-induced causes. Check those alternatives only where they can change the receiving answer.

### MNT.3:7 - Conformance Checklist

Can the reader distinguish the required functioning, observed departure, diagnosis and consequence? Does each decision-bearing causal claim have usable evidence? Are unknown or competing explanations retained at their actual strength? For a population claim, do event definitions, exposures and observation limits support the comparison?

The requested account is complete when it supports the receiving maintenance decision or identifies its evidential limit. It need not resolve every possible root cause.

### MNT.3:8 - Common Anti-Patterns and How to Avoid Them

A failure code becomes a mechanism when the record never established causation. Recover the observation and explain the inference. A list of removed parts becomes a failure count when preventive removals are silently included. Recover event meaning and exposure before comparing groups.

An open recurrence question can also be treated as a reason to withhold an already supported local recommendation. Separate the recommendation's claim from the stronger explanation that remains unresolved.

### MNT.3:9 - Consequences

Policy and intervention decisions can use evidence at a defensible resolution. Some inquiries become narrower; others stop because they would not change the answer. The remaining cost is preserving enough provenance and uncertainty to prevent a later user from making a stronger claim than the account supports.

### MNT.3:10 - Architectural Rationale

Mechanism, observed condition and consequence are connected in one account because their separation is what makes diagnosis usable. Population evidence is included when it changes that account, rather than treated as an automatic statistics exercise. The Method supports maintenance reasoning; it does not replace specialist materials analysis or a research design.

### MNT.3:11 - SoTA-Echoing

The practice question is how much failure knowledge is sufficient for a maintenance choice. The selected line combines physical explanation with qualified observation and decision relevance. It adapts the failure-mechanism emphasis in the [2025 maintenance optimization account](https://orbilu.uni.lu/bitstream/10993/61558/1/1-s2.0-S0377221724005241-main.pdf) and uses [FPF A.10](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/07-a-10---evidence-graph-referring-claim-bound-evidence-and-pro.md) and [FPF C.16](../../../sections/09-part-c---kernel-extension-specifications/27-c-16---measurement-metrics-characterization.md) for evidential and measurement claims. Against fault-code counting or mandatory exhaustive root-cause analysis, this Method uses the separated claims, observation limits and conditional inquiry in the Solution. The trade-off is an explicitly narrower causal answer in exchange for useful timely action. Reopen when new failure or exposure evidence can distinguish a consequential alternative.

### MNT.3:12 - Relations

[MNT.1](12-mnt-1---identify-the-maintained-system-use-and-permission-bo.md) supplies the functioning question, [MNT.4](15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) supplies current condition observations, and [MNT.12](23-mnt-12---maintain-maintenance-information-and-configuration.md) supports the relevant configuration and history. [MNT.2](13-mnt-2---select-and-reopen-the-maintenance-policy.md), [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) and [MNT.13](24-mnt-13---coordinate-the-maintenance-programme-and-fleet-lear.md) consume the resulting failure account for different decisions. [FPF A.10](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/07-a-10---evidence-graph-referring-claim-bound-evidence-and-pro.md) qualifies evidence, [FPF C.16](../../../sections/09-part-c---kernel-extension-specifications/27-c-16---measurement-metrics-characterization.md) governs measurement and [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) governs the contribution and burden of further inquiry.

### MNT.3:End
