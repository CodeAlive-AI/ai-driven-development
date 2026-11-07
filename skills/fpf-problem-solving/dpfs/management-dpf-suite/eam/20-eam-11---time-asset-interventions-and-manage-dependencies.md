## EAM.11 - Time Asset Interventions and Manage Dependencies

> **Type:** Method
> **Status:** Stable

### EAM.11:1 - Problem frame

Use this pattern when the timing of an asset intervention can change whether the service or portfolio plan is feasible. A job estimate fits the window, but its preparation, shutdown, testing, return or shared resources do not.

Begin with the complete intervention and its service conditions. Return a feasible timing arrangement or the exact unmet condition. A value recommendation can be delivered before a particular work window has been authorized.

### EAM.11:2 - Problem

Task hours are often substituted for elapsed outage time. Local plans can share the same crew or remove each other's fallback. Reordering work can improve feasibility, but cannot reduce the total demand on one exclusive resource below its actual work requirement.

### EAM.11:3 - Forces

A larger window and more contingency improve recoverability while consuming service and resources. Combining work can reduce repeated access but increase interference. Deferral can preserve an opportunity only when the continued-use policy remains supported.

### EAM.11:4 - Solution

Recover the selected or proposed interventions, the required service and the actual calendars. Use the whole-outage arrangement from [MNT.7](../../engineering-dpf-suite/mnt/18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) where applicable and the operating envelope from OPS.10. Identify the duty, configuration, access and protection assumptions those results need.

Separate preparation possible during operation from work requiring the outage. Include supported shutdown, protected access, intervention, testing and return. Establish whether estimates already include allowance before adding contingency. Distinguish person-hours, exclusive-team occupancy and elapsed service-loss time.

Represent the dependencies that determine timing. Some activities must precede others; some can overlap only with independent providers and compatible service conditions. A shared standby unit, isolation or recovery resource can prevent overlap even when labor is available.

Place the complete demands in actual windows. A necessary resource bound is total exclusive demand no greater than available time. Passing it is not sufficient when release dates, simultaneous resources or service dependencies prevent a schedule. Use a finite schedule for a small known set.

If the arrangement fails, compare a real change: another window, another supported option, a qualified provider, a service-preserving fallback or justified deferral. Include its cost and moved burden.

State what happens if an important condition changes during the window. Identify the time, personnel, access or fallback needed to return this asset to a supported operating state, and keep those resources available. Agree with the people controlling maintenance and operation when they must decide on a supported hold or return before that option is lost. Obtain the required allocation or operating decision before relying on reassigned resources, an extended window or changed service.

Return the timing arrangement to the people controlling the work and operation. Stop when the requested planning question is answered. Actual protected work and resumption require their own applicable permissions and evidence.

### EAM.11:5 - Archetypal Grounding

For FFMK in CityWater, the supplied whole durations are A two days, B two, C three and D one. One qualified team is available for twelve comparable work days. A on days 1–2, B on 3–4, C on 5–7 and D on 8 uses eight days, and every asset is restored before the next begins.

North's A and C outages cannot coincide: their combined loss would reduce delivery below the dry-window minimum. East's B and D outages have the same incompatibility. The serial schedule respects both conditions and the shared team. The four remaining days are uncommitted allowance.

If only seven days are available, the eight-day plan fails. The declared options permit FRLK—A refurbishment, B replacement, C leased service and D continuation—in seven days at higher present cost. The practitioner compares that real option or another qualified arrangement.

### EAM.11:6 - Bias-Annotation

Optimistic duration estimates can favor a preferred option. Treat estimate uncertainty, readiness and actual staffing explicitly. An apparent schedule saving can transfer fatigue, recovery burden or service loss to another participant.

### EAM.11:7 - Conformance Checklist

Does the schedule include the complete outage and return? Are exclusive resources and actual dependencies respected? Do service conditions hold in each interval, and is there a supported response if the work exceeds its plan?

### EAM.11:8 - Common Anti-Patterns and How to Avoid Them

Summing labor-hours and calling them an outage mixes quantities. Model the actual elapsed dependencies.

Assuming that two individually feasible outages can overlap can remove the fallback supporting each. Check their combined service and resource conditions.

### EAM.11:9 - Consequences

The programme can be planned against real windows and revised when a constraint changes. Some apparently cheaper options become infeasible. The schedule remains a prospective arrangement; actual work, functioning and resumed-use authority require their own results.

### EAM.11:10 - Architectural Rationale

Timing follows the whole intervention's participation in service. This keeps scheduling, technical support and authority distinct while allowing a small finite plan to settle the current question.

### EAM.11:11 - SoTA-Echoing

[MNT.7](../../engineering-dpf-suite/mnt/18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) supplies whole-outage reasoning and [OPS.10](../ops/40-ops-10---qualify-operating-capacity-under-variability.md) qualified service analysis. The common asset-management sources recognize outage and resource planning. This pattern uses those results at the asset programme's horizon.

### EAM.11:12 - Relations

[EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) supplies the service envelope; [EAM.8](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md)–[EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md) supply options and combinations. [MNT.7](../../engineering-dpf-suite/mnt/18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) supplies intervention timing and [MNT.15](../../engineering-dpf-suite/mnt/26-mnt-15---reconcile-simultaneous-maintenance-operation-and-su.md) shared-work coordination. [EAM.12](21-eam-12---integrate-specialist-results-for-an-asset-recommend.md) receives the feasible arrangement for the asset decision, and [EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) revisits its assumptions after relevant observations.

### EAM.11:End
