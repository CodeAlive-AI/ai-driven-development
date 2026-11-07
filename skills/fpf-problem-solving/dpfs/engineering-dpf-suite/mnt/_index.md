# Maintenance Engineering and Management Principles Framework

**DocID:** `MNT` within **FPF Library**.

Anatoly Levenchuk · Release: 7 October 2026

Original framework content © 2026 Anatoly Levenchuk, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Third-party sources retain their own terms.


# Table of Contents

Search for the maintenance difficulty or result you need. Dependencies identify useful result relations, not a mandatory sequence.

## Public units

| Unit | Reader use |
| :--- | :--- |
| [Maintenance Engineering and Management Principles Framework Readme](_index.md#maintenance-engineering-and-management-principles-framework-readme) | Follow condition-to-result work, fleet learning and shared-work reconciliation. |
| [Citation](_index.md#citation) | Cite the framework or one continuing pattern contribution. |
| [Maintenance Engineering and Management Principles Framework Architectural Reference](_index.md#maintenance-engineering-and-management-principles-framework-architectural-reference) | Understand the language, its result relations, alternatives and limits. |
| [MNT.Reference:1](01-mnt-reference-1---the-working-problem-and-practical-gain.md) | The working problem and practical gain |
| [MNT.Reference:2](02-mnt-reference-2---organizing-the-methods-around-different-re.md) | Organizing the Methods around different results |
| [MNT.Reference:3](03-mnt-reference-3---what-the-principal-objects-mean-in-practic.md) | What the principal objects mean in practice |
| [MNT.Reference:4](04-mnt-reference-4---competing-values-and-the-whole-use-constra.md) | Competing values and the whole-use constraints |
| [MNT.Reference:5](05-mnt-reference-5---architectural-rationale.md) | Architectural Rationale |
| [MNT.Reference:6](06-mnt-reference-6---applying-and-checking-the-whole-language.md) | Applying and checking the whole language |
| [MNT.Reference:7](07-mnt-reference-7---assumptions-costs-and-limits.md) | Assumptions, costs and limits |
| [MNT.Reference:8](08-mnt-reference-8---shared-source-synthesis-and-useful-neighbo.md) | Shared source synthesis and useful neighbours |
| [MNT.Reference:9](09-mnt-reference-9---returns-to-engineering-and-operating-pract.md) | Returns to engineering and operating practice |
| [MNT.Sources:1](32-mnt-sources-1---source-roles-and-scope-of-reliance.md) | Source roles and scope of reliance |
| [MNT.Application - Cross-Pattern Applications](_index.md#cross-pattern-applications) | Follow PS17, the fleet comparison and shared-resource coordination. |
| [Maintenance Engineering and Management Principles Framework Sources and Edition Notes](_index.md#maintenance-engineering-and-management-principles-framework-sources-and-edition-notes) | Recover source contributions and their applicable limits. |
| [MNT.Reference:10 - Framework boundary and revision](10-mnt-reference-10---framework-boundary-and-revision.md) | Understand scope, pattern continuity and action-changing refresh. |

**Part A - Maintained Use, Policy, Failure, and Condition**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MNT.1 - Identify the Maintained System, Use, and Permission Boundary](12-mnt-1---identify-the-maintained-system-use-and-permission-bo.md) | Stable | *Keywords:* equipment identity, required function, configuration, control. *Query:* "Which System and use does this maintenance question concern?" Bound the question and its operating and permission conditions. | [FPF A.1.SCR](../../../sections/05-part-a---kernel-architecture-cluster/05-a-1-scr---finding-the-acting-or-changed-system.md), [FPF A.2.8.PER](../../../sections/05-part-a---kernel-architecture-cluster/17-a-2-8-per---granted-permission-exercise-and-non-prohibition.md); [SYSE.13](../syse/38-syse-13---establish-configuration-identity-variants-and-effe.md) |
| 2 | [MNT.2 - Select and Reopen the Maintenance Policy](13-mnt-2---select-and-reopen-the-maintenance-policy.md) | Stable | *Keywords:* maintenance policy, corrective, preventive, condition-based, failure-finding. *Query:* "Which task should be retained or changed for this failure?" Compare applicable tasks and response conditions without a technology ladder. | [MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md), [MNT.4](15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md), [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md); [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) |
| 3 | [MNT.3 - Establish Degradation and Failure Evidence for Maintenance](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md) | Stable | *Keywords:* failure evidence, mechanism, cause, exposure, censoring. *Query:* "What does the failure history actually support?" Separate observation, diagnosis and consequence at the resolution needed by the decision. | [MNT.1](12-mnt-1---identify-the-maintained-system-use-and-permission-bo.md), [MNT.4](15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md), [MNT.12](23-mnt-12---maintain-maintenance-information-and-configuration.md); [FPF A.10](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/07-a-10---evidence-graph-referring-claim-bound-evidence-and-pro.md), [FPF C.16](../../../sections/09-part-c---kernel-extension-specifications/27-c-16---measurement-metrics-characterization.md) |
| 4 | [MNT.4 - Monitor and Interpret System Condition for Maintenance](15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) | Stable | *Keywords:* condition monitoring, alarm, baseline, forecast, remaining life. *Query:* "What does this signal mean under the actual operating conditions?" Return a qualified condition account or the precise interpretation limit. | [MNT.1](12-mnt-1---identify-the-maintained-system-use-and-permission-bo.md), [MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md); [FPF C.16](../../../sections/09-part-c---kernel-extension-specifications/27-c-16---measurement-metrics-characterization.md) |

**Part B - Readiness, Intervention Choice, Coordination, and Protection**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 5 | [MNT.5 - Prepare Maintenance Service Capability, Spares, Tools, and Authority](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) | Stable | *Keywords:* spare applicability, tools, competence, readiness, lead time. *Query:* "Can the selected maintenance task obtain usable support in time?" Establish task-specific readiness or its action-changing deficiency. | [MNT.2](13-mnt-2---select-and-reopen-the-maintenance-policy.md), [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md); [SYSE.12](../syse/35-syse-12---develop-or-retain-an-engineering-platform-for-prac.md); [FPF A.2.2](../../../sections/05-part-a---kernel-architecture-cluster/10-a-2-2---system-capability-conditions-measures-and-fit.md) |
| 6 | [MNT.6 - Diagnose Condition and Choose a Maintenance Response](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) | Stable | *Keywords:* diagnosis, repair, replace, defer, restriction, recommendation. *Query:* "What maintenance response is supported now?" Compare plausible maintenance responses and finish sufficient advice without compulsory physical work. | [MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md), [MNT.4](15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md), [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md), [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md); [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) |
| 7 | [MNT.7 - Coordinate Maintenance Intervention and Continuing Operation](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) | Stable | *Keywords:* outage, service capacity, preparation, testing, restoration, contingency. *Query:* "Does the whole intervention fit the operating commitment?" Compare complete elapsed demand with the qualified service envelope. | [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md), [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md); [OPS.10](../../management-dpf-suite/ops/40-ops-10---qualify-operating-capacity-under-variability.md) |
| 8 | [MNT.8 - Isolate, Make Safe, and Authorize the Maintenance Intervention](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md) | Stable | *Keywords:* isolation, energy, protection, intervention permission, scope. *Query:* "What supports beginning this protected intervention?" Establish applicable actual protection and bounded authority, or return the unmet condition. | [MNT.1](12-mnt-1---identify-the-maintained-system-use-and-permission-bo.md), [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md), [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md); [FPF A.2.8.PER](../../../sections/05-part-a---kernel-architecture-cluster/17-a-2-8-per---granted-permission-exercise-and-non-prohibition.md) |

**Part C - Performed Intervention, Functioning, and Return to Use**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 9 | [MNT.9 - Perform and Record the Maintenance Intervention](20-mnt-9---perform-and-record-the-maintenance-intervention.md) | Stable | *Keywords:* performed maintenance, deviation, interruption, actual parts, work record. *Query:* "What work actually occurred and in what resulting state?" Perform within operative conditions and preserve useful intervention evidence. | [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md), [MNT.8](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md); [FPF A.13](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/12-a-13---the-agential-role-agency-spectrum.md), [FPF A.15.1](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/15-a-15-1---u-work-dated-performed-work-occurrence.md) |
| 10 | [MNT.10 - Verify Restored Functioning after Maintenance](21-mnt-10---verify-restored-functioning-after-maintenance.md) | Stable | *Keywords:* restored function, representative load, verification, test limits. *Query:* "What required functioning does the evidence support?" Check the actual resulting configuration and return qualified functioning evidence. | [MNT.9](20-mnt-9---perform-and-record-the-maintenance-intervention.md); [FPF B.3](../../../sections/08-part-b---trans-disciplinary-reasoning-cluster/17-b-3---is-this-claim-supported-for-this-use-trust-and-assuran.md), [FPF A.10](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/07-a-10---evidence-graph-referring-claim-bound-evidence-and-pro.md), [FPF C.16](../../../sections/09-part-c---kernel-extension-specifications/27-c-16---measurement-metrics-characterization.md) |
| 11 | [MNT.11 - Hand Back and Authorize Resumed Use after Maintenance, with Certification Where Required](22-mnt-11---hand-back-and-authorize-resumed-use-after-maintenan.md) | Stable | *Keywords:* hand-back, release, certification, control, resumed use. *Query:* "Who can resume which use of the returned System?" Reconcile functioning, state and applicable release conditions while transferring control. | [MNT.8](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md), [MNT.9](20-mnt-9---perform-and-record-the-maintenance-intervention.md), [MNT.10](21-mnt-10---verify-restored-functioning-after-maintenance.md); [FPF A.2.8.PER](../../../sections/05-part-a---kernel-architecture-cluster/17-a-2-8-per---granted-permission-exercise-and-non-prohibition.md) |

**Part D - Information, Programme, Methods, Simultaneous Work, and Culture**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 12 | [MNT.12 - Maintain Maintenance Information and Configuration Continuity](23-mnt-12---maintain-maintenance-information-and-configuration.md) | Stable | *Keywords:* maintenance history, serial unit, configuration, effectivity, event coding. *Query:* "Which history and description apply to this installed state?" Restore event and configuration continuity for the receiving decision. | [SYSE.13](../syse/38-syse-13---establish-configuration-identity-variants-and-effe.md); [MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md), [MNT.9](20-mnt-9---perform-and-record-the-maintenance-intervention.md) |
| 13 | [MNT.13 - Coordinate the Maintenance Programme and Fleet Learning](24-mnt-13---coordinate-the-maintenance-programme-and-fleet-lear.md) | Stable | *Keywords:* fleet, programme, failure rate, exposure, support, improvement. *Query:* "What programme decision does comparable fleet evidence support?" Return a qualified programme decision with its population and causal limits. | [MNT.2](13-mnt-2---select-and-reopen-the-maintenance-policy.md), [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md), [MNT.12](23-mnt-12---maintain-maintenance-information-and-configuration.md); [FPF E.23](../../../sections/11-part-e---the-fpf-constitution-and-authoring-guides/63-e-23---quality-improvement-loop-method.md) |
| 14 | [MNT.14 - Compare Maintenance Methods for Retention or Change](25-mnt-14---compare-maintenance-methods-for-retention-or-change.md) | Stable | *Keywords:* Method comparison, predictive maintenance, practical worth, variant, refresh. *Query:* "Should this way of obtaining maintenance results be retained or replaced?" Compare the same use and whole burden, with conditional trials and useful retain decisions. | [MNT.2](13-mnt-2---select-and-reopen-the-maintenance-policy.md), [MNT.13](24-mnt-13---coordinate-the-maintenance-programme-and-fleet-lear.md); [FPF C.11.MV](../../../sections/09-part-c---kernel-extension-specifications/25-c-11-mv---compare-the-worth-of-a-method-option.md), [FPF A.3.1.MV](../../../sections/05-part-a---kernel-architecture-cluster/27-a-3-1-mv---construct-and-maintain-a-method-variant.md) |
| 15 | [MNT.15 - Reconcile Simultaneous Maintenance, Operation, and Support Work](26-mnt-15---reconcile-simultaneous-maintenance-operation-and-su.md) | Stable | *Keywords:* simultaneous work, shared specialist, overload, fallback, coordination. *Query:* "Why do individually feasible jobs fail together?" Resolve shared demands and moved burden at the whole-combination scope. | [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md), [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md), [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md); [FPF C.32.MWA](../../../sections/09-part-c---kernel-extension-specifications/82-c-32-mwa---synthesize-an-architecture-account-of-methods-and.md); [FPF C.32.MWA.PP](../../../sections/09-part-c---kernel-extension-specifications/83-c-32-mwa-pp---construct-and-compare-method-performance-and-p.md) |
| 16 | [MNT.16 - Deliberately Continue and Change Maintenance Culture](27-mnt-16---deliberately-continue-and-change-maintenance-cultur.md) | Stable | *Keywords:* maintenance culture, transmission, enactment, recognition, retention. *Query:* "Is the practice actually being continued or changed?" Separate availability, actual use and effects, and select a supported continuation. | [MNT.13](24-mnt-13---coordinate-the-maintenance-programme-and-fleet-lear.md), [MNT.14](25-mnt-14---compare-maintenance-methods-for-retention-or-change.md); [FPF C.36](../../../sections/09-part-c---kernel-extension-specifications/91-c-36---cultural-evolution-and-cultural-evolution-engineering.md) |

# Maintenance Engineering and Management Principles Framework Readme

## Practical entries

Maintenance methods connect a condition or failure account with the result someone needs, such as advice, a selected intervention, functioning evidence, return to use or a programme decision. Each connection consumes a particular result. A suitable spare supports readiness; readiness and an operating allowance support a feasible intervention; performed work identifies the configuration to be tested; functioning evidence supports the receiving operating decision.

These are selected examples of the language at work. Enter where the question starts, using adequate existing results. The [Table of Contents](_index.md#table-of-contents) provides direct pattern access, and the [Architectural Reference](_index.md#maintenance-engineering-and-management-principles-framework-architectural-reference) explains the shared conditions and boundaries. You can ask an assisting agent to explain a pattern or comment on your case in the language of your work, without framework jargon.

The cases are constructed. Their equipment, operating, protection and measurement premises illustrate the reasoning; they do not supply a procedure, time standard or limit for actual equipment. Actual work uses competent practitioners and the applicable professional and operating sources.

### MNT-CARD-01 — From a condition concern to the result actually needed

- **Situation:** A condition concern may justify intervention, but usable support, continuing service and return to operation impose different conditions.
- **Question:** What can be answered now, and what further results does selected physical work actually need?
- **First useful result or blocker:** Sufficient advice, a feasible selected arrangement, or the particular unmet condition limiting the next act.
- **Start with:** [MNT.1 - Identify the Maintained System, Use, and Permission Boundary](12-mnt-1---identify-the-maintained-system-use-and-permission-bo.md) if the unit, use or requested result is unclear; otherwise enter [MNT.6 - Diagnose Condition and Choose a Maintenance Response](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) with the adequate condition and failure accounts.
- **Stop or return:** A supported recommendation can finish before repair. Continue only when that intervention is selected and its operative conditions are met; reopen the result whose condition changes.

1. **Give the choice a condition and failure account it can use.** In [PS17](28-mnt-application-1---app-mnt-01-ps17-advice-selected-interven.md), the question concerns PumpTrain-PS17-B, configuration C41. [MNT.4 - Monitor and Interpret System Condition for Maintenance](15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) supplies abnormal, increasing bearing-location vibration under comparable duty. [MNT.3 - Establish Degradation and Failure Evidence for Maintenance](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md) uses the case's separate machine-specific inspection and diagnostic account: the rolling contact has a localized defect, while the mounting and lubrication findings support replacement under the unchanged design basis.
2. **Finish the bounded recommendation.** The supplied operating assessment permits a lower-duty arrangement that meets present service needs until the planned outage two days away, while its condition and protection limits hold. Normal demand then returns. [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) uses that temporary bridge and the identified defect to recommend replacement at the suitable outage. The two days are a service boundary, not a predicted failure time. [MNT.5 - Prepare Maintenance Service Capability, Spares, Tools, and Authority](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) finds the spare physically available but its required specialist applicability return missing. The advice is complete; replacement cannot begin. Compatible information, tools and provider preparation can continue.
3. **Test the whole window after the missing support is supplied.** In the extended branch, the applicability return arrives and the intervention is selected. [MNT.7 - Coordinate Maintenance Intervention and Continuing Operation](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) uses a separate operating allowance of four hours for reduced-capacity operation. Thirty minutes for shutdown and isolation, 95 for intervention, 45 for controlled testing, 25 for restoration and hand-back, and thirty of explicit contingency total 225 minutes within 240. Ninety minutes of preparation occurs before the outage. A further twenty-minute demand beyond all included allowances raises the total to 245: revise the arrangement rather than consume required testing or hand-back time.
4. **Carry the selected scope through actual work.** [MNT.8 - Isolate, Make Safe, and Authorize the Maintenance Intervention](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md) establishes applicable protection and permission. An uncontrolled shared energy path prevents the affected work from starting. In the branch where the conditions are met, [MNT.9 - Perform and Record the Maintenance Intervention](20-mnt-9---perform-and-record-the-maintenance-intervention.md) records removal of bearing R551 and installation of compatible R607, resulting in configuration C42. [MNT.12 - Maintain Maintenance Information and Configuration Continuity](23-mnt-12---maintain-maintenance-information-and-configuration.md) connects the C41 condition history to those events and the C42 test.
5. **Return functioning and control at their supported scope.** [MNT.10 - Verify Restored Functioning after Maintenance](21-mnt-10---verify-restored-functioning-after-maintenance.md) uses C42, the applicable acceptance basis and the case's representative run to judge the immediate-duty claim. A failed flow result returns to diagnosis or engineering while the performed intervention remains recorded. With adequate functioning evidence, [MNT.11 - Hand Back and Authorize Resumed Use after Maintenance, with Certification Where Required](22-mnt-11---hand-back-and-authorize-resumed-use-after-maintenan.md) reconciles the returned state, obtains any required certification and resumed-use decision, and transfers control. If the receiving authority is unavailable, the test result survives but the intended permission remains outstanding. Return the tested duty and horizon with the permission.

A lost standby train reopens the earlier operating allowance; a finding that a shared mounting defect would defeat replacement reopens [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md)'s choice. Those changes affect different results. The unchanged evidence remains available, and an unresolved recurrence question need not turn a completed local answer into a new investigation.

### MNT-FLEET — Learn from maintenance history

- **Situation:** One pump group has fewer recorded failures, a proposed monitoring service promises improvement, and an upcoming task already lacks an applicable spare.
- **Question:** Which programme, task or support change does the available evidence warrant?
- **First useful result or blocker:** A comparable fleet account and supported retain or change decision, or the event, exposure or applicability discrepancy that prevents the relevant conclusion.
- **Start with:** [MNT.13 - Coordinate the Maintenance Programme and Fleet Learning](24-mnt-13---coordinate-the-maintenance-programme-and-fleet-lear.md), using [MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md) and [MNT.12](23-mnt-12---maintain-maintenance-information-and-configuration.md) only where the failure or history basis needs work.
- **Stop or return:** Retain an adequate current policy or fix a known support deficiency on its existing basis. Further inquiry is selected only for a worthwhile attainable answer.

1. **Make the comparison mean the same thing.** In the [48-pump case](29-mnt-application-2---app-mnt-02-a-fleet-comparison-that-rever.md), twenty pumps have four relevant failures over 20,000 operating hours; 28 have six over 56,000 hours. The crude rates are 0.20 and approximately 0.107 events per 1,000 hours. Counts favor the first group, rates the second. [MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md) establishes what counts as a failure, and [MNT.12](23-mnt-12---maintain-maintenance-information-and-configuration.md) attaches events and exposure to the actual components and intervals.
2. **Propagate a corrected history before changing the policy.** If two of the second group's six records are preventive removals, correct that event classification and the affected rate. Duty, component histories and selection into the groups still limit any causal policy comparison.
3. **Keep a policy decision separate from a support decision.** [MNT.2 - Select and Reopen the Maintenance Policy](13-mnt-2---select-and-reopen-the-maintenance-policy.md) can retain the current task where its existing failure-and-response basis remains adequate. The weak comparative data do not establish that adequacy. [MNT.13](24-mnt-13---coordinate-the-maintenance-programme-and-fleet-lear.md) can separately select repair of the known spare deficiency, using [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) to establish readiness for the upcoming task. A broader redesign of recurring support returns to the relevant enabling-arrangement practice; it need not wait for a causal fleet study.
4. **Compare the proposed method at the response it can improve.** [MNT.14 - Compare Maintenance Methods for Retention or Change](25-mnt-14---compare-maintenance-methods-for-retention-or-change.md) compares the online predictor with current periodic interpretation at the same maintenance use. In its case, existing provider information shows no improvement in feasible response: the same specialist and part constraints dominate, while integration and interpretation add work. Retain the present method for that use and address support. Another family with rapidly changing condition and an available response can reopen the comparison for that family.

The policy alternatives also depend on the function. An obvious, low-consequence indicator failure may justify deliberate run-to-failure; a hidden protective-function failure needs an applicable means of finding it.

### MNT-SHARED-WORK — Reconcile individually feasible jobs that cannot be performed together

- **Situation:** Two maintenance jobs fit their own windows but demand the same specialist or fallback.
- **Question:** Which combined commitment can actually be met, and what does changing it do to service and failure consequences?
- **First useful result or blocker:** A supported allocation or timing change, or the specific combined commitment that remains infeasible.
- **Start with:** [MNT.15 - Reconcile Simultaneous Maintenance, Operation, and Support Work](26-mnt-15---reconcile-simultaneous-maintenance-operation-and-su.md), using the existing job, readiness and operating accounts.
- **Stop or return:** A simple shared-demand bound can finish the feasibility question. Selecting a repair needs the relevant consequence, capability and authority results.

1. **Compare the whole shared demand.** In the [packaging-plant case](30-mnt-application-3---app-mnt-03-individually-feasible-jobs-an.md), each job needs four hours of the same qualified specialist inside one six-hour access window. Eight hours cannot fit six. Preparation overlapping production leaves the shared eight-hour specialist demand unchanged.
2. **Use the separate methods to distinguish feasible alternatives.** [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) supplies the failure consequence of deferring a job; [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) determines whether an additional provider is capable, available and permitted to act; [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) checks another window or changed operating arrangement against continuing service. [MNT.15](26-mnt-15---reconcile-simultaneous-maintenance-operation-and-su.md) consumes those results to return a supported combined arrangement or an unmet commitment.
3. **Reopen the combination when a shared premise changes.** If both jobs rely on the same standby equipment, each plan's separate fallback claim no longer settles their joint use. Extend the comparison to the actual operating dependencies and relevant [MNT.8](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md) protection conditions. If a longer shift would impair the specialist's later protected work, change allocation, relief or timing.

## How to read and apply the framework

Use a pattern's Problem frame and Solution for the first working move. Its worked case shows the result and a consequential branch. Its checklist, source comparison and relations provide the further assurance and context needed for a more consequential use.

## Citation

Cite: Anatoly Levenchuk, *Maintenance Engineering and Management Principles Framework*, version shown above. For a particular contribution, add its PatternID and title. The framework was developed with AI-assisted authoring and review. The original text is reusable under the license above; cited third-party works are not relicensed by this publication.

---

## Files of this publication

Generated by the skill's splitter: one file per section, in reading order.


### Maintenance Engineering and Management Principles Framework Architectural Reference

- [MNT.Reference:1 - The working problem and practical gain](01-mnt-reference-1---the-working-problem-and-practical-gain.md) (16 lines)
- [MNT.Reference:2 - Organizing the Methods around different results](02-mnt-reference-2---organizing-the-methods-around-different-re.md) (17 lines)
- [MNT.Reference:3 - What the principal objects mean in practice](03-mnt-reference-3---what-the-principal-objects-mean-in-practic.md) (10 lines)
- [MNT.Reference:4 - Competing values and the whole-use constraints](04-mnt-reference-4---competing-values-and-the-whole-use-constra.md) (8 lines)
- [MNT.Reference:5 - Architectural Rationale](05-mnt-reference-5---architectural-rationale.md) (14 lines)
- [MNT.Reference:6 - Applying and checking the whole language](06-mnt-reference-6---applying-and-checking-the-whole-language.md) (10 lines)
- [MNT.Reference:7 - Assumptions, costs and limits](07-mnt-reference-7---assumptions-costs-and-limits.md) (8 lines)
- [MNT.Reference:8 - Shared source synthesis and useful neighbours](08-mnt-reference-8---shared-source-synthesis-and-useful-neighbo.md) (10 lines)
- [MNT.Reference:9 - Returns to engineering and operating practice](09-mnt-reference-9---returns-to-engineering-and-operating-pract.md) (6 lines)
- [MNT.Reference:10 - Framework boundary and revision](10-mnt-reference-10---framework-boundary-and-revision.md) (14 lines)
- [MNT.Reference:End](11-mnt-reference-end.md) (3 lines)

### Part A - Maintained Use, Policy, Failure, and Condition

- [MNT.1 - Identify the Maintained System, Use, and Permission Boundary](12-mnt-1---identify-the-maintained-system-use-and-permission-bo.md) (83 lines)
- [MNT.2 - Select and Reopen the Maintenance Policy](13-mnt-2---select-and-reopen-the-maintenance-policy.md) (163 lines)
- [MNT.3 - Establish Degradation and Failure Evidence for Maintenance](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md) (91 lines)
- [MNT.4 - Monitor and Interpret System Condition for Maintenance](15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) (91 lines)

### Part B - Readiness, Intervention Choice, Coordination, and Protection

- [MNT.5 - Prepare Maintenance Service Capability, Spares, Tools, and Authority](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) (81 lines)
- [MNT.6 - Diagnose Condition and Choose a Maintenance Response](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) (92 lines)
- [MNT.7 - Coordinate Maintenance Intervention and Continuing Operation](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) (90 lines)
- [MNT.8 - Isolate, Make Safe, and Authorize the Maintenance Intervention](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md) (83 lines)

### Part C - Performed Intervention, Functioning, and Return to Use

- [MNT.9 - Perform and Record the Maintenance Intervention](20-mnt-9---perform-and-record-the-maintenance-intervention.md) (81 lines)
- [MNT.10 - Verify Restored Functioning after Maintenance](21-mnt-10---verify-restored-functioning-after-maintenance.md) (85 lines)
- [MNT.11 - Hand Back and Authorize Resumed Use after Maintenance, with Certification Where Required](22-mnt-11---hand-back-and-authorize-resumed-use-after-maintenan.md) (81 lines)

### Part D - Information, Programme, Methods, Simultaneous Work, and Culture

- [MNT.12 - Maintain Maintenance Information and Configuration Continuity](23-mnt-12---maintain-maintenance-information-and-configuration.md) (107 lines)
- [MNT.13 - Coordinate the Maintenance Programme and Fleet Learning](24-mnt-13---coordinate-the-maintenance-programme-and-fleet-lear.md) (83 lines)
- [MNT.14 - Compare Maintenance Methods for Retention or Change](25-mnt-14---compare-maintenance-methods-for-retention-or-change.md) (85 lines)
- [MNT.15 - Reconcile Simultaneous Maintenance, Operation, and Support Work](26-mnt-15---reconcile-simultaneous-maintenance-operation-and-su.md) (87 lines)
- [MNT.16 - Deliberately Continue and Change Maintenance Culture](27-mnt-16---deliberately-continue-and-change-maintenance-cultur.md) (83 lines)

### Cross-Pattern Applications

- [MNT.Application:1 - APP-MNT-01 — PS17: advice, selected intervention and return to use](28-mnt-application-1---app-mnt-01-ps17-advice-selected-interven.md) (20 lines)
- [MNT.Application:2 - APP-MNT-02 — A fleet comparison that reverses when exposure is counted](29-mnt-application-2---app-mnt-02-a-fleet-comparison-that-rever.md) (12 lines)
- [MNT.Application:3 - APP-MNT-03 — Individually feasible jobs and one shared specialist](30-mnt-application-3---app-mnt-03-individually-feasible-jobs-an.md) (10 lines)
- [MNT.Application:End](31-mnt-application-end.md) (3 lines)

### Maintenance Engineering and Management Principles Framework Sources and Edition Notes

- [MNT.Sources:1 - Source roles and scope of reliance](32-mnt-sources-1---source-roles-and-scope-of-reliance.md) (20 lines)
- [MNT.Sources:End](33-mnt-sources-end.md) (1 lines)
