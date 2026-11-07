## MNT.5 - Prepare Maintenance Service Capability, Spares, Tools, and Authority

> **Type:** Method
> **Status:** Stable

### MNT.5:1 - Problem frame

Use this pattern when a maintenance policy or intervention depends on support that may not be ready at the required time. The spare is in stock, but its applicability is unresolved; the tool is available, but no competent provider can use it in the outage.

Establish the support that makes the selected maintenance task feasible, or return the deficiency that changes the choice. This is maintenance readiness for a stated task and use. Designing a changed workshop, service platform or supply arrangement uses [SYSE.12](../syse/35-syse-12---develop-or-retain-an-engineering-platform-for-prac.md) where needed. A recommendation can already be complete while readiness for its performance remains incomplete.

### MNT.5:2 - Problem

An available resource can be unsuitable for the task. Stock presence does not establish part compatibility, an organization chart does not establish available competence and a tool listing does not establish a usable measurement capability. A nominally quick repair can therefore have a long or uncertain real response time.

The opposite error is to require every conceivable support record before answering any maintenance question. Readiness concerns the selected work, not a universal administrative package.

### MNT.5:3 - Forces

More reserve support reduces some response delays but consumes storage, money and maintenance effort. Shared specialists and repairable pools can improve use of resources while creating contention. Long-term support must address obsolescence and shelf condition; an urgent task needs the smallest adequate answer now. Readiness decisions also affect the people expected to extend a shift or absorb unexpected work.

### MNT.5:4 - Solution

Derive support from the actual task content and its uncertainty. Identify the relevant procedure, access, expected work and foreseeable branches. A bearing replacement and a fault diagnosis may use different competence, tools and information even when they concern the same unit.

Check readiness at the point of use. For spares, establish applicability to the installed configuration and the condition needed for installation. Resolve material compatibility, preservation, shelf-life or specialist-return requirements where they actually govern this task. A certificate is useful when it supplies a required claim; collecting an unrelated certificate does not repair a compatibility gap.

For tools and information, determine whether the practitioner can perform and judge the task. This may require the applicable instruction, fit-for-purpose measurement capability, access to configuration information and suitable workspace. A calibration label alone does not settle whether the instrument's range and uncertainty suit the measurement.

For providers, establish relevant competence, actual availability, access and action-specific authority. Include working conditions and likely task duration when these affect capability. If unexpected work would require relief, obtain a viable relief arrangement or preserve the resulting limit.

Relate obtaining lead times to the maintenance need. Distinguish what can be prepared during continuing operation from what requires shutdown or protected access. Include supplier uncertainty, transit, acceptance and replenishment where they change response feasibility. For a repairable pool, consider units already removed for repair and common demands on the same stock; nominal pool size is not available reserve.

Choose the smallest adequate support action. It may be to use an existing spare, reserve a qualified specialist, resolve one applicability question, obtain another window or change the intervention alternative. If the support arrangement itself is inadequate across recurring tasks, return that enabling-arrangement development question to [SYSE.12](../syse/35-syse-12---develop-or-retain-an-engineering-platform-for-prac.md) and the programme decision to MNT.13.

Return the task-specific readiness result with the condition that can invalidate it. A part reserved for this job can be reassigned; a provider can become unavailable; an installed configuration can change. Reopen only the affected readiness claim. A support deficiency limits the proposed work but need not prevent a useful diagnosis or recommendation.

### MNT.5:5 - Archetypal Grounding

In APP-MNT-01, a replacement bearing for PS17 is physically available. The case's governing conditions require a specialist applicability/certification return for that replacement in configuration C41. Until that return arrives, the proposed replacement cannot begin. The planner's supported recommendation remains complete.

The team uses the available time to prepare the applicable instruction, reserve the qualified provider and check the required tools without entering the protected work area. When the specialist return arrives, it closes the part question only; the actual isolation and permission remain [MNT.8](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md)'s result.

A late return can invalidate the intended outage even though the part becomes acceptable. [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) then compares another window or another supported response. Entering the outage first and hoping the return will arrive would turn a support uncertainty into service exposure.

For a fleet of obsolete components, a different result may be necessary: a repairable pool with a credible turnaround arrangement or an engineering-approved replacement design. Purchasing more unusable legacy stock does not establish readiness.

### MNT.5:6 - Bias-Annotation

Inventory systems make material shortages visible while hiding interpretation work, contractor access and specialist fatigue. Include those support demands when they change the task. A procurement saving can move cost to downtime or the people expected to compensate for an unsuitable resource.

### MNT.5:7 - Conformance Checklist

Can the selected task be performed and judged with the actual available part, provider, tool, information and access? Are material compatibility and permission conditions supported? Do obtaining and relief arrangements fit the needed time? Are shared demands and support uncertainties retained where they change feasibility?

A readiness answer can be “adequate for this task” or a specific deficiency. It does not require a new platform, a complete stock catalogue or closure of an advice request through physical work.

### MNT.5:8 - Common Anti-Patterns and How to Avoid Them

“Two in stock” is taken as proof that two replacements can proceed. Check applicable condition, reservations and shared resources. A named service provider is treated as available capability when its competent person is committed elsewhere. Recover the actual obtaining arrangement and timing.

A complete support checklist is imposed on a simple recommendation. Limit readiness work to what the present result consumes, and preserve requirements that govern any later intervention separately.

### MNT.5:9 - Consequences

The plan uses support that can actually contribute to maintenance. Some apparent quick fixes become infeasible; some preparation can proceed without consuming the outage. The added work is checking readiness and replenishment where planning previously relied on nominal resource counts.

### MNT.5:10 - Architectural Rationale

Readiness belongs between maintenance intent and feasible performance because selecting a technically sensible task does not obtain its means. Keeping the Method domain-specific preserves compatibility, repairable-stock and maintenance-access reasoning while reusing the general enabling-arrangement contribution from SYSE.12.

### MNT.5:11 - SoTA-Echoing

The question is how to turn nominal resources into a feasible maintenance response. This pattern adapts the human/material-support emphasis in GFMAM's 2021 framework, §6.5, into task-specific readiness reasoning. Against stock-count-only planning, the Method adds applicability, provider availability and obtaining lead time. It accepts some reservation and reconciliation effort to expose a real support limit before an outage begins. The source supplies breadth, not a universal documentation checklist. Reopen when task content, support lead time or available capability changes. See [GFMAM's maintenance framework](https://www.gfmam.org/sites/default/files/2021-02/GFMAM%20Maintenance%20Framework%20-%202nd%20Edition%20Final.pdf).

### MNT.5:12 - Relations

[MNT.2](13-mnt-2---select-and-reopen-the-maintenance-policy.md) and [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) identify task needs; [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) and [MNT.15](26-mnt-15---reconcile-simultaneous-maintenance-operation-and-su.md) consume readiness in coordination. [MNT.8](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md) establishes permission for the actual protected work. [MNT.12](23-mnt-12---maintain-maintenance-information-and-configuration.md) supplies configuration and history where applicability depends on them. [SYSE.12](../syse/35-syse-12---develop-or-retain-an-engineering-platform-for-prac.md) supplies enabling-arrangement development, and [FPF A.2.2](../../../sections/05-part-a---kernel-architecture-cluster/10-a-2-2---system-capability-conditions-measures-and-fit.md) supports capability-envelope claims.

### MNT.5:End
