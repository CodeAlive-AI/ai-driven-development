## MNT.12 - Maintain Maintenance Information and Configuration Continuity

> **Type:** Method
> **Status:** Stable

### MNT.12:1 - Problem frame

Use this pattern when a maintenance decision depends on connecting service history to the correct unit, installed part, configuration or applicable description. The work log says a bearing was replaced, the stock system says it was returned and the condition trend still carries the previous unit's identifier.

Restore a usable information basis for the receiving maintenance question. Reuse the configuration identity and effectivity contribution from [SYSE.13](../syse/38-syse-13---establish-configuration-identity-variants-and-effe.md); this Method adds the service-event and exposure continuity that maintenance decisions consume. A new database, complete digital twin or plant-wide inventory is unnecessary when a smaller reconciliation answers the question.

For practice with entry dates, replacement events and component intervals, use [the first-use task](23-mnt-12---maintain-maintenance-information-and-configuration.md#mnt1241---first-use-with-a-replacement-history).

### MNT.12:2 - Problem

The same part number can identify a design used by many physical units. A new document edition can exist while the installed machine remains unchanged. A planned replacement can appear in a system before the work occurs. Treating those entries as one current configuration can attach evidence to the wrong subject.

History can also lose the difference between failure, inspection, preventive removal and restoration. A later policy comparison then counts unlike events or assigns exposure to a component after it was removed.

### MNT.12:3 - Forces

More detail supports future analysis but burdens people recording work under time pressure. A unified schema can aid retrieval while concealing meaningful local distinctions. Preserving provenance helps resolve disagreement, but retaining obsolete duplicated “current” records creates another disagreement. Keep one usable account for the decision and recoverable supporting sources where needed.

### MNT.12:4 - Solution

Start from the receiving maintenance decision and its required distinctions. A spare-applicability question needs different history from a recurrence study or a hand-back. Identify the actual unit, component individuals and configuration changes that can affect that use.

Recover the configuration basis under SYSE.13. Distinguish actual, intended and unknown installed state; part or variant descriptions; document editions; and the conditions under which a description applies. A date or shared label cannot establish those correspondences by itself.

Connect the maintenance events to that basis over time. Preserve relevant installation, removal, inspection, condition, intervention and restoration facts, including the sources that support them. Where exposure matters, establish which unit or component accumulated it during which interval and under what operating conditions. A replaced component does not inherit the predecessor's age merely because the equipment tag is unchanged.

Resolve contradictions according to their consequence. A stock return may refer to unused material while the intervention record identifies the installed part. Compare subject, event, time and identifier scheme before treating the records as inconsistent. If they actually conflict, use the available observation or accountable source that can resolve the receiving question; preserve uncertainty when it cannot.

Maintain the intended user's ability to retrieve and interpret the result. Use the existing work log, engineering system or maintenance database when it can carry the necessary relations. Avoid copying one mutable current-state claim across several manually edited files. A source history can remain historical while one current account describes the relevant installed state.

Keep corrections distinguishable from new physical events. Correcting a mistaken serial number changes the account; replacing the component changes the machine. A Method or software change can also alter the meaning of a code without changing earlier events. Preserve the interpretation needed for comparison instead of silently recoding the past as if the categories were always identical.

Return the qualified information basis, its source links and any uncertainty that changes the next use. If the present question is answered, stop. Broader data repair is selected only when another real use warrants the work. Where retention or access is governed by operative requirements, preserve those obligations without inventing a new universal retention rule.

#### MNT.12:4.1 - First use with a replacement history

Use this practice when you can read maintenance records but still need to distinguish an entry date, an actual replacement and the interval belonging to each component. Make and retain your own answer before reading the discussion. The constructed time window uses equal operating conditions and continuous operation, so exposure here equals each component's installed duration.

**Make a first attempt.** In `[6,12)`, configuration C41 contains bearing R551 until its replacement at 8; C42 contains R607 from 8 onward. The replacement account was entered at 10. There is a condition observation at 7 and a functioning test at 9. The test records PS17 without an independent identification of the bearing's serial number: its component attribution relies on the supported installation history. Allocate the exposure in this window and identify which configuration the observation and test concern. State the grounds for each attribution.

Choose an available edition containing [Use a record for one configuration-dependent claim (SYSE.13:4.4)](../syse/38-syse-13---establish-configuration-identity-variants-and-effe.md#syse1344---use-a-record-for-one-configuration-dependent-claim), including its uncertain-time explanation, and keep that copy available for the exercise. Read that bounded fragment with your attempted answer in view. Return here with the actual component intervals, the relevant event times and any unresolved attribution. You need another part of [SYSE.13](../syse/38-syse-13---establish-configuration-identity-variants-and-effe.md) only if another configuration question requires it.

**Compare your reasoning.** R551 accumulates `8−6=2` time units and R607 accumulates `12−8=4`, totaling 6. The observation at 7 concerns C41; the test at 9 concerns C42. Entry at 10 does not move the replacement from 8 to 10. Preserve R551's earlier history; R607 does not inherit its predecessor's exposure.

Revise the part of your answer whose grounds differ. Try each changed premise below before reading its discussion.

**Corrected event account.** Reconciliation of the original evidence establishes that replacement actually occurred at 10. The former boundary at 8 was an error in the account; its supported correction was entered at 11. What changes?

**Discussion.** R551 now has 4 time units and R607 has 2, still totaling 6. The test at 9 preceded replacement and no longer supports the former claim about testing C42/R607. This conclusion follows from the reconciled event evidence, not from preferring the latest entry. Correcting the account creates no second replacement. [MNT.10](21-mnt-10---verify-restored-functioning-after-maintenance.md) and [MNT.11](22-mnt-11---hand-back-and-authorize-resumed-use-after-maintenan.md) retain the requirements for functioning evidence and resumed use; changing a record does not meet them.

**Uncertain event time.** For a separate variation, replace the exact replacement time with evidence of one transition `τ∈[8,10]` in the same `[6,12)` operating window. There were no other replacements or gaps. What exposure and test attribution can you still return?

**Discussion.** R551 has `τ−6` time units and R607 has `12−τ`. Each lies between 2 and 4, but they vary together: `τ=8 → (2,4)`, `τ=9 → (3,3)`, `τ=10 → (4,2)`. The total remains 6 for every admissible time. It is not a range from 4 to 8. The observation at 7 still concerns the earlier configuration. The test at 9, without independent component identification, cannot be attributed confidently to R607.

Return the result at the scope the receiving question needs. A total-exposure question may use 6; a component-specific duration or restored-function question may require the actual boundary or separate evidence about the new component. Seek that relevant observation or accountable source answer when worthwhile; otherwise retain the uncertainty. Preserve unaffected history.

Apply the same distinctions to one of your own event records and state which premise could change your answer. Work with these explanations can support correction; it does not establish independent performance on new material. Obtain competent feedback on an unresolved step before relying on its attribution.

### MNT.12:5 - Archetypal Grounding

In the extended constructed PS17 case, the pre-intervention configuration C41 contains bearing R551. The performed intervention removes R551 and installs compatible bearing R607. C42 identifies the resulting installed configuration under the same approved design basis.

The work record describes those events. The condition account before the intervention concerns C41; the functioning test after it concerns C42. The change of record alone would not have established that installation, and the new bearing does not erase the older unit's useful failure history.

Suppose the stock system also lists R607 as returned. The receiving question is whether the functioning evidence concerns the actually installed bearing. The team compares the material movement and intervention evidence and obtains the relevant physical or accountable return if the conflict remains.

In the fleet case, two preventive removals originally coded as failures are corrected as descriptions of those events, not counted as new maintenance occurrences. Exposure is assigned to the component intervals that actually existed. That smaller reconciliation can restore a usable comparison without migrating the whole fleet database.

### MNT.12:6 - Bias-Annotation

A central database may seem more authoritative than an inconvenient local observation. Conversely, a practitioner's recollection can override a traceable record without adequate evidence. Use the claim's subject and evidential support, not the prestige of its storage location.

### MNT.12:7 - Conformance Checklist

Can the recipient connect the relevant events and evidence to the actual unit and configuration? Are intended, observed and unknown states distinguishable? Are part individuals, descriptions and editions kept separate where they affect applicability? Are exposure and event meanings compatible with the intended comparison?

The information basis is complete for its receiving use, not necessarily for every future analysis. Material uncertainty remains visible rather than being hidden by a current-status field.

### MNT.12:8 - Common Anti-Patterns and How to Avoid Them

The equipment tag is treated as a lifetime identifier for every replaceable component. Recover component intervals when failure or life claims depend on them. A planned configuration is marked current before installation. Establish the actual state separately.

Every record discrepancy triggers a new digital-twin project. Resolve the contradiction needed by the present decision first and return any genuinely broader need on its own merits.

### MNT.12:9 - Consequences

Condition, policy and hand-back decisions can refer to the same actual maintenance history without confusing records with the machine. Some data remains qualified or incomplete. The cost of maintaining useful correspondence is concentrated on the distinctions that affect use.

### MNT.12:10 - Architectural Rationale

General configuration identity belongs in SYSE.13. Maintenance adds event meaning, exposure intervals and continuity across service replacements. Fleet learning needs those distinctions to interpret work-order counts.

### MNT.12:11 - SoTA-Echoing

The practice question is which information is sufficient for a maintenance decision across changing installed state. This pattern adopts the distinction in [SYSE.13](../syse/38-syse-13---establish-configuration-identity-variants-and-effe.md) between actual configuration, descriptions and effectivity, and adapts GFMAM's maintenance-information concern to service events and exposure. Against a latest-record-only default, the Method uses the time-bound event/configuration correspondence in the Solution and C41-to-C42 case. It accepts focused provenance work while rejecting a complete information-platform replacement as an automatic prerequisite. Reopen when an event definition, installed state or receiving comparison changes. See [GFMAM's information-management account](https://www.gfmam.org/sites/default/files/2021-02/GFMAM%20Maintenance%20Framework%20-%202nd%20Edition%20Final.pdf).

### MNT.12:12 - Relations

[SYSE.13](../syse/38-syse-13---establish-configuration-identity-variants-and-effe.md) supplies configuration identity and effectivity. [MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md) and [MNT.4](15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) consume failure and condition history; [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) uses applicability; [MNT.9](20-mnt-9---perform-and-record-the-maintenance-intervention.md)–[MNT.11](22-mnt-11---hand-back-and-authorize-resumed-use-after-maintenan.md) supply intervention, functioning and hand-back facts. [MNT.13](24-mnt-13---coordinate-the-maintenance-programme-and-fleet-lear.md) uses comparable population history. [FPF A.10](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/07-a-10---evidence-graph-referring-claim-bound-evidence-and-pro.md) supports evidential qualification.

### MNT.12:End
