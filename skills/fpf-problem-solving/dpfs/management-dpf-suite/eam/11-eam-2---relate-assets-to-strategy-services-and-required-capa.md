## EAM.2 - Relate Assets to Strategy, Services, and Required Capability

> **Type:** Method
> **Status:** Stable

### EAM.2:1 - Problem frame

Use this pattern when a desired outcome has been translated directly into an asset purchase or renewal, or when an existing asset's continuing contribution is unclear. A requirement for reliable water delivery has become “buy another pump,” but the practitioner needs to establish which capability is actually missing.

Begin with the receiving service and show how the asset could contribute to it. Return the supported outcome–service–capability relationship and any gap that changes the option choice. A supplied local service mandate can be enough.

### EAM.2:2 - Problem

An asset can be technically effective without serving the current purpose. Conversely, an important service can depend on several assets whose individual records do not explain their joint contribution. Broad strategic language leaves those relations unresolved and can make a familiar construction appear necessary.

### EAM.2:3 - Forces

Long-term outcomes guide investment while immediate commitments constrain what can change now. An asset can support several services with competing priorities. A detailed model can expose a missing dependency, but excessive tracing can delay a decision already supported by a simple relationship.

### EAM.2:4 - Solution

State the desired outcome and its recipient. Distinguish an aspiration from an adopted objective or service obligation. Identify the required service, population, location, conditions and horizon at the grain that changes the asset decision.

Describe the contribution needed to supply that service. Use quantities and conditions where they matter: flow at the delivery point, usable storage, response time or an available operating interval. A count of installed assets is not itself that contribution.

Relate the contribution to possible assets or arrangements. One contribution can require several interacting Systems, and one asset can support several contributions. Preserve the actual dependencies instead of forcing the relationships into a one-to-one hierarchy. Use [SYSE.5](../../engineering-dpf-suite/syse/26-syse-5---develop-an-engineered-system-s-functional-organizat.md) when the bearer or allocation alternatives need engineering development.

Compare the needed capability with an applicable account of the present arrangement. Identify the consequential gap and its evidence. A supplied qualified result can be used directly; otherwise obtain the specific service or engineering result required. Separate a known shortfall from an uncertain forecast.

Challenge the necessity of the first asset proposal. Consider a different bearer, shared service, operating change or demand change when it could satisfy the same need. Keep a materially different alternative only with the conditions that would make its contribution real.

Return the supported relations and the next asset question. Stop when they are sufficient to generate or compare options. Reopen when the service, outcome priority or a relied-on capability changes.

### EAM.2:5 - Archetypal Grounding

CityWater's North area requires at least 1,100 m³/h in the wet season, while the supplied account supports 1,000. The gap is 100 m³/h of delivered service. The two shortlisted C options each add 200: a modification or a leased service. Both therefore meet the quantity requirement, subject to their technical and operating qualifications.

The useful relationship is from the water-delivery requirement to additional usable service capability, then to those alternative arrangements. It is not from a general growth objective directly to ownership of a new pump. The extra 100 above the minimum can matter as margin, but it is not proof that every contingency is covered.

If an authorized demand-management arrangement could reduce the wet requirement to 1,000 without an unacceptable loss, it would be another alternative. A planner's desire to reduce the requirement does not amend CityWater's water-service mandate; its issuing authority must make that decision.

### EAM.2:6 - Bias-Annotation

Internal objectives can omit losses experienced by customers or another service area. Trace the contribution to the actual recipient and identify whose outcome changes. Do not assume that a locally favorable utilization or accounting measure represents the service's value.

### EAM.2:7 - Conformance Checklist

Is the service requirement recoverable from its source? Does each relied-on asset contribution have the right quantity and conditions? Can the reader distinguish a demonstrated gap, a forecast and an alternative proposal?

### EAM.2:8 - Common Anti-Patterns and How to Avoid Them

A line from “strategy” to a purchase request does not establish the missing contribution. State the service and capability relation.

Treating installed capacity as delivered service hides configuration, access and network constraints. Use a qualified operating or engineering result.

### EAM.2:9 - Consequences

The practitioner can generate alternatives against a concrete need and identify assets whose contribution is no longer required. A missing relation becomes a bounded question, while unrelated strategic analysis can remain outside the current task.

### EAM.2:10 - Architectural Rationale

This pattern connects outcomes to engineering capability because asset ownership is only one way of obtaining a contribution. It retains the strategy and service decisions with their actual sources and makes the engineering allocation a separate question. That structure supports both new investment and continued-use decisions.

### EAM.2:11 - SoTA-Echoing

For deciding which asset contribution a strategic or service need requires, select an explicit comparison between the required service and a qualified present capability, followed by alternative ways to close the gap. Adopt the bounded service and commitment result from [OPS.1](../ops/29-ops-1---identify-the-operating-system-commitments-and-flow-u.md) and adapt the functional-organization and bearer comparison in [SYSE.5](../../engineering-dpf-suite/syse/26-syse-5---develop-an-engineered-system-s-functional-organizat.md) to this asset question. The Solution therefore keeps the required contribution separate from the first proposed purchase and preserves many-to-many dependencies where they matter. In North, the comparison reveals a 100 m³/h shortfall and leaves both a modification and a leased contribution available.

A serious starting alternative is to trace the investment through the organization's strategic asset-management objectives. GFMAM's *Asset Management Landscape*, third edition, June 2024, section 3.1 ([pp. 29–30](https://gfmam.org/sites/default/files/2024-06/GFMAM_AM_Landscape_v3.0_English_2024.pdf#page=29)), provides that strategic-alignment comparator. Its contribution is the link to organizational objectives; it does not qualify either CityWater option's delivered flow. Adapt that alignment by asking what service must change before treating an aligned project as necessary. The extra effort is one explicit service/capability comparison where adequate results already exist. It can expose a different bearer or demand option that an objective-to-purchase shortcut misses. The trade-off is that this local result does not settle competing strategic priorities; obtain that decision from its responsible source when it can change the asset choice. Reopen the comparison when that priority, the service mandate or a relied-on capability changes, or when an option cannot be distinguished without a more detailed allocation analysis. The professional source does not require the one-to-one hierarchy that the shortcut assumes.

### EAM.2:12 - Relations

[EAM.1](10-eam-1---frame-the-engineered-assets-and-required-outcomes.md) supplies the asset question; [EAM.4](13-eam-4---assess-demand-and-service-need-for-asset-decisions.md) qualifies demand and [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) compares capability. [EAM.7](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md) develops alternatives. [OPS.1](../ops/29-ops-1---identify-the-operating-system-commitments-and-flow-u.md) supplies service and commitment facts; [SYSE.5](../../engineering-dpf-suite/syse/26-syse-5---develop-an-engineered-system-s-functional-organizat.md) supplies functional-organization and bearer alternatives. [FPF A.6.F](../../../sections/06-cluster-a-iv-a---signature-stack-boundary-discipline/22-a-6-f---function-and-functional-precision-restoration.md) supports function-like claims when their meaning requires restoration.

### EAM.2:End
