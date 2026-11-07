## EAM.7 - Generate Ways to Supply an Asset-Dependent Service

> **Type:** Method
> **Status:** Stable

### EAM.7:1 - Problem frame

Use this pattern when a needed service contribution has become a proposal to acquire or modify an asset. A team has a preferred machine, supplier or design, but materially different ways of obtaining the contribution could change cost, risk or feasibility.

Begin by separating the required contribution from the first bearer assumption. Return technically meaningful alternatives with the realization conditions the next comparison needs.

### EAM.7:2 - Problem

Searching only within the familiar equipment category can exclude sharing, leasing, reconfiguration or demand change. The opposite mistake lists attractive concepts without showing how their contributions could be realized. A vendor's availability claim then substitutes for an applicable engineering answer.

### EAM.7:3 - Forces

Ownership can provide control while creating continuing support and exit burdens. Shared or leased service can reduce initial capital while adding dependency and recurring cost. A technically novel arrangement can improve value but require evidence and integration work that the decision window cannot support.

### EAM.7:4 - Solution

Recover the required outside contribution, recipients, conditions and horizon from [EAM.1](10-eam-1---frame-the-engineered-assets-and-required-outcomes.md) and EAM.2. Identify which feature of the incumbent arrangement is an assumption rather than a requirement.

Form materially different ways to supply the contribution. Depending on the problem, these can include changing an existing asset, acquiring a new one, redistributing capability, sharing a provider, leasing a service or changing demand. A renamed supplier offering with the same relevant behavior is not a distinct architectural alternative.

Describe how each option could work. Identify the asset or provider, integration with the present arrangement, interfaces, access, support and changes to operation. Use an applicable [SYSE.5](../../engineering-dpf-suite/syse/26-syse-5---develop-an-engineered-system-s-functional-organizat.md) result when functional organization and bearer allocation determine the option. Obtain subject-specific engineering where physics or other specialist constraints decide feasibility.

State the realization conditions and consequences at the same service basis. Include procurement and integration time, interruption, continuing cost, dependency, reversal and exit. Preserve what remains unknown; a proposed interface is not demonstrated compatibility.

Compare the set with the incumbent or a no-build response. Explain why withdrawal, demand change or another contribution is included or excluded in this case. If an option requires amending a service commitment, identify that separate decision rather than assuming the amendment.

Return enough alternatives for [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md) to make a genuine comparison. Stop adding options when further generation is unlikely to improve the requested answer at a worthwhile burden. Keep the precise unsupported dependency that prevents a promising option from being used.

### EAM.7:5 - Archetypal Grounding

CityWater's wet-season North requirement exceeds the present 1,000 m³/h capability by 100. The shortlisted C modification and leased service each add a qualified 200. The modification requires €3 million initial capital and €0.20 million annually; the leased service requires no initial capital and €1.20 million annually, under the supplied five-year terms.

The alternatives differ in funding, continuing cost, realization time and dependence on the service provider. Their common quantity contribution does not make them interchangeable. The lease can free capital for D replacement, while its recurring cost changes the whole portfolio comparison.

If the proposed leased service has no applicable evidence for the required connection and delivery conditions, it remains conditional. A quotation and a nominal pump rating do not establish that service. The practitioner asks for the needed engineering result.

### EAM.7:6 - Bias-Annotation

A procurement channel can narrow the set before the asset question is answered. Supplier information can favor purchase or service contracts according to commercial interest. Preserve the costs and dependencies borne by the utility and service users.

### EAM.7:7 - Conformance Checklist

Are the alternatives materially different ways to provide the same needed contribution? Are their realization conditions and continuing consequences visible? Can the recipient distinguish a supported candidate from a concept awaiting a decisive result?

### EAM.7:8 - Common Anti-Patterns and How to Avoid Them

Three bids for effectively the same arrangement can conceal a missing service alternative. Challenge the bearer assumption before counting options.

Treating a service contract as removal of engineering dependence hides the provider and interface conditions. State the actual contribution and evidence required.

### EAM.7:9 - Consequences

The comparison can reveal a lower-capital, more reversible or otherwise valuable alternative. Some concepts remain conditional, and more engineering may be required for a consequential choice.

### EAM.7:10 - Architectural Rationale

The pattern separates desired contribution from physical or contractual form. That preserves meaningful alternatives while allowing the engineering and financial consequences to be reconciled later. It complements [EAM.8](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md)'s policies for existing assets instead of making acquisition the default beginning.

### EAM.7:11 - SoTA-Echoing

For finding materially different ways to obtain an asset's required contribution, adopt SYSE.5:4.1's joint development of functional organization, bearers, interfaces and realization conditions. Adapt it to the receiving asset comparison by retaining the alternatives whose capital, continuing burden, service or dependency differences can change the choice. In CityWater, modification and qualified leased service provide the same additional flow but compete differently for capital and continuing expenditure. The Solution therefore establishes the contribution before fixing ownership or a particular construction.

A serious alternative is specification-led acquisition: hold an already justified asset arrangement fixed and compare designs or suppliers able to realize it. GFMAM's *Asset Management Landscape*, third edition, June 2024, section 6.2 ([pp. 72–73](https://gfmam.org/sites/default/files/2024-06/GFMAM_AM_Landscape_v3.0_English_2024.pdf#page=72)), provides the acquisition and integration comparator; its section 3.4 also keeps new, existing and non-asset responses available at planning scope. Retain specification-led comparison when the bearer decision is already supported. Where ownership is only an initial assumption, selecting it first could exclude C's service option before its funding consequence is examined. The broader contribution comparison costs some additional provider/interface analysis, accepted because it can change the feasible asset programme; it stops short of detailed engineering for every conceivable option. These sources supply operations and professional scope, not the lease's actual availability or compatibility. Reopen the choice when a required interface cannot be realized, a provider qualification changes, an incumbent assumption becomes an actual requirement, or a newly supported arrangement could improve the decision enough to justify examining it.

### EAM.7:12 - Relations

[EAM.2](11-eam-2---relate-assets-to-strategy-services-and-required-capa.md) and [EAM.4](13-eam-4---assess-demand-and-service-need-for-asset-decisions.md) supply the need; [EAM.3](12-eam-3---establish-the-asset-information-and-configuration-ba.md) and [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) supply configuration and capability conditions. [SYSE.5](../../engineering-dpf-suite/syse/26-syse-5---develop-an-engineered-system-s-functional-organizat.md) supports bearer and interface alternatives. [EAM.8](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md) supplies existing-asset policies, [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md) compares value and [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md) tests realization timing.

### EAM.7:End
