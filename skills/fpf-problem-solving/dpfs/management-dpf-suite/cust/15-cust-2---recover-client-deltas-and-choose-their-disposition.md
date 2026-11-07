## CUST.2 - Recover Client Deltas and Choose Their Disposition

> **Type:** Method pattern
> **Status:** Stable

### CUST.2:1 - Problem frame

Use this method when “the customer needs customization” conceals several different changes, or when a completed deployment contains unexplained local work. You need a supported basis, an intended or observed customer result, and access to the people or material that can reveal the consequential work.

The first useful move is to compare the result and the conditions for obtaining it with the supported offering. The output is an explained set of differences and compatible dispositions, not a catalogue of every difference between two customers.

If an established configuration already explains the case and its obligations, use that configuration. A label such as “enterprise” or “special customer” is not a reason to reconstruct all its details.

### CUST.2:2 - Problem

Artifact comparison misses work that leaves no code change: interpretation, data repair, repeated consultation, negotiation, access, training and exception handling. Conversely, a long list of customer attributes can obscure the few differences that actually change provision. Choosing a route before recovering these differences makes the proposed solution determine the diagnosis.

### CUST.2:3 - Forces

| Tension | Practical consequence |
| --- | --- |
| Enough detail and decision cost | Split differences only when a decision, dependency, performer or qualification changes. |
| Local meaning and familiar vocabulary | Preserve the meaning needed for the customer's decision before translating it into provider terms. |
| Distinct changes and coupled effects | Keep a report, input repair and support obligation separate while preserving their dependence. |
| Known work and unknown causes | Keep the observed extra action distinct from its possible explanations. |

### CUST.2:4 - Solution

#### CUST.2:4.1 - Choose a real comparison basis

Name the supported offering or method from which this case differs. Include the version or effective conditions when they change use. Recover what ordinary delivery assumes about inputs, participants, skills, access, timing, acceptance and support. A marketing description can locate the offering but may not expose its operating basis.

Describe the customer's intended result in their work. Separate what is explicitly required from your inference and from a proposed solution. “Needs a custom dashboard” might mean a decision-maker needs a monthly eligibility answer, or that an operator needs continuous intervention.

When there is no supported predecessor, use a sufficiently explicit proposed basis and mark it as proposed. You can still compare alternatives; you cannot describe deviations from an imaginary established standard as observed facts.

#### CUST.2:4.2 - Recover changes backward and forward

Work backward from acceptance: what must be true for the customer to use the result? Identify the work needed to establish each condition. Then walk forward through a representative episode, using records, observation or the participants' account. Ask where someone changed an input, made an interpretation, sought help, waited, overrode a default or accepted a continuing duty.

For each consequential difference, state the basis, the changed condition or action and the consequence. Distinguish observation from explanation. “An expert recoded thirty records” is an observation; “the product lacks a general mapping function” is one possible explanation. A legitimate difference in meaning might make general recoding inappropriate.

Inspect meaning where a mismatch changes the answer. [SIE.1 — Bound the Receiving Use and Semantic Contract](../../engineering-dpf-suite/sie/21-sie-1---bound-the-receiving-use-and-semantic-contract.md) supplies a bounded semantic-use question; [SIE.4 — Judge Cross-Source Correspondences and Their Permitted Uses](../../engineering-dpf-suite/sie/24-sie-4---judge-cross-source-correspondences-and-their-permitt.md) qualifies cross-source correspondences and their permitted uses. Receive what can be mapped, under which interpretation and with what loss or restriction. Use that result to change the delta and the proposed action. A matching field name is insufficient.

#### CUST.2:4.3 - Divide by independently different decisions

Split a difference when its continuation can change independently. The same customer may need a supported SSO configuration, a new meaning of “active,” a local report and an exceptional response time. They have different grounds and recipients.

Keep coupled effects visible. Private hosting may alter monitoring, upgrades and support access together. Describing hosting as one technical delta does not remove those consequences. A useful statement can group the linked changes while preserving the separate decisions.

Use ordinary material already needed for the work. The following form is a reminder, not a required registry:

| Recoverable fact | Example |
| --- | --- |
| Supported basis | The service counts active accounts from the monthly batch under the provider's definition. |
| Customer difference | The customer excludes suspended accounts but includes pending renewals. |
| Evidence and uncertainty | The operating policy states the first exclusion; treatment of renewals still needs the customer's decision. |
| Consequence for the work | Input mapping and acceptance examples must change before results are comparable. |
| Linked obligation | The customer must supply the status information each month. |
| Next useful result | An agreed meaning and qualified mapping, then a delivery choice. |

Remove incidental details that cannot change the decision. Keep an apparently small distinction when it changes acceptance, permission, work or liability.

#### CUST.2:4.4 - Choose disposition on separate axes

Decide first whether the difference should be accepted at all. A useful customer result may still be unavailable under actual capacity, rights or professional conditions. A smaller result or later date can be preferable to an unsupported exception.

Then distinguish three choices:

- What remains local and what, if anything, should become shared?
- How will the contribution be realized and provided? Consider configuration, code, hardware, a procedure, training or an assisted service, and whether a partner should supply it.
- What is actually promised, to whom, for how long and with which support?

These choices can coexist. A common adapter does not remove a local operating change; a repeatable service can include specialist help; a partner can deliver either a common or bespoke contribution. They are not rungs of a maturity ladder.

For a candidate common change, identify the property or operation expected to transfer and the difference that could defeat it. Send that question to CUST.3 with the recovered cases and their limits. For a known permitted variation, send the actual fit question to CUST.4. For an unresolved causal or transfer question, ask CUST.5 for a discriminating answer.

#### CUST.2:4.5 - Recombine the decisions around the customer result

Follow the proposed dispositions together. Does the new semantic mapping still fit the standard interface? Does the common adapter require access forbidden in the private environment? Does the local report create a new monthly obligation? Can the same specialist provide both the new support and existing commitments?

Resolve these interactions before promising the combination. CUST.7 supplies the complete burden comparison; CUST.8 supplies the effect on existing consumers. A qualified engineering result can settle technical feasibility while the commercial or operating choice remains open.

Identify the actual decision holder and enabling conditions for consequential changes. The decision arrangement in CUST.1:4.3 can be used directly here. If the field practitioner cannot admit a shared component or commit support, obtain those decisions rather than interpreting silence as approval.

#### CUST.2:4.6 - Return an actionable result

Deliver the explained differences with their compatible dispositions, unresolved question and next recipient. Preserve the basis so a later case can be compared meaningfully. The result can be small: “The interface is unchanged; only status meaning and the customer's monthly input responsibility differ. Resolve those before configuring the standard service.”

Reopen only the affected differences when new evidence changes a premise. A new legal-use restriction can alter material transfer without invalidating a permitted local calculation. An unexpected manual intervention may reopen the delivery method without changing the customer's desired result.

### CUST.2:5 - Archetypal Grounding

In the analytical-service case, an initial request lists five features. The recovered differences are more useful:

| Request wording | Recovered difference | Disposition and join |
| --- | --- | --- |
| “Use our login” | Existing identity interface, customer-specific credentials and access conditions. | Supported configuration, after access is supplied. |
| “Use our active-account count” | A different operational meaning, not only a column rename. | Semantic clarification and qualified mapping before computation. |
| “Run inside our network” | Hosting, monitoring and upgrade access differ together. | Bounded field inquiry; support conditions remain open. |
| “Add our report” | A local output with monthly preparation. | Funded local service; no automatic common feature. |
| “Respond immediately” | A new service obligation using scarce capacity. | Accept only a feasible response arrangement, otherwise narrow it. |

A developer who starts by adding five product features misses the status decision and continuing service obligations. A practitioner using the recovered differences can keep the supported identity path, investigate only hosting and preserve the report locally.

Change the setting to a public literacy service. “Translate the course” can hide language, reading ability, device access and facilitator help. Translation alone cannot repair missing devices or different prior capability. The same delta recovery separates the contributions while preserving the participant's intended activity.

### CUST.2:6 - Bias-Annotation

The method can favor what is easy to record. Ask recipients and performers about invisible preparation, relationship work and assistance. Observations may still be partial; preserve that limit.

A provider's standard is only the chosen comparison basis, not a judgement that the customer's difference is defective.

### CUST.2:7 - Conformance Checklist

- Is the supported or proposed basis explicit?
- Can a recipient understand each difference's consequence for useful work?
- Are observations separated from hypotheses about their cause?
- Are distinct decisions separated without losing their dependencies?
- Are local/shared result, realization/provision and promise choices distinguished?
- Does the recombined answer still obtain the customer's result under actual conditions?

### CUST.2:8 - Common Anti-Patterns and How to Avoid Them

**Feature-list diagnosis.** Recover the operating difference before choosing a feature.

**Everything is a delta.** Retain differences that change result, obtaining conditions or obligations; do not inventory the customer's entire organization.

**One route per customer.** Several compatible dispositions may be needed within one case.

**A semantic label settles meaning.** Obtain the interpretation and permitted correspondence needed by the receiving decision.

### CUST.2:9 - Consequences

The result can reduce unnecessary common changes and expose work that needs separate funding or qualification. It also makes legitimate customer differences harder to dismiss as “nonstandard.”

Recovery takes effort. Use existing adequate evidence and stop when the live disposition can be made.

### CUST.2:10 - Architectural Rationale

The method organizes comparison around consequential work rather than artifact shape. Separating decision axes prevents a choice of technical form from silently deciding common ownership, delivery responsibility or the customer promise. Recombination is necessary because separately plausible dispositions can be incompatible together.

### CUST.2:11 - SoTA-Echoing

Customer-solution research distinguishes the customer's continuing process from a bundle of products. The primary abstract of Tuli, Kohli and Bharadwaj supports that distinction. CUST uses it to inspect requirements, integration, deployment and continuing help.

Compared with a generic request tracker, the stronger receiving-use line in the full SIE and Implementation Facilitation methods changes the first action: recover meaning and obtaining difficulty before allocating a feature. CUST adopts those results and adds the particular local/shared disposition and recombination. Reopen the recovery method if repeated cases reveal a consequential class of difference it cannot expose.

### CUST.2:12 - Relations

CUST.2 can be used independently or as the difference-recovery constituent of CUST.1. CUST.3 receives a common-contribution question; CUST.4 receives a fit question; CUST.5 receives an unresolved inquiry; CUST.7 receives linked work and resource implications; CUST.8 receives effects on existing obligations. These are conditional result uses, not compulsory sequential stages.

### CUST.2:End
