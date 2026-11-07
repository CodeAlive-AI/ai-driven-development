## OPS.11 - Coordinate Interacting Operating Structures

> **Status:** Stable


### OPS.11:0 - Use This When

Use this Method when a local operating change depends on, or changes, another arrangement: material processing and order transactions, test work and release evidence, resource access and service commitments, or observation and supervisory decisions. Typical symptoms are a feasible local plan that cannot be completed in practice, a faster resource followed by more waiting elsewhere, or incompatible decisions by people responsible for different parts of the operation.

The first useful result is a bounded coordination decision: the affected structures and concrete couplings, feasible alternatives and consequences, decisions required from their respective owners, unresolved relations, and a return condition. Start from one operating question or proposed change, not from a map of the whole enterprise.

Use OPS.8 for a queue-policy question that does not require wider coordination, OPS.9 for an unresolved constraint diagnosis, and OPS.10 for a capacity/service calculation. Product or organization redesign belongs to the corresponding engineering practice when that is the object being changed.

### OPS.11:1 - Problem frame

An operation depends on several actual structures. Its resource participation, material transformation, case and commitment relations, information production/use, financial settlement and decisions may be described in different views. Those structures overlap through particular subjects and relations; the views need not be isomorphic.

Here the Method governs coordination of an operating change across the selected structures. It does not make their diagrams into the structures, reduce them to one “flow,” or give one coordinator authority over every participating decision.

### OPS.11:2 - Problem

A local plan can omit a necessary coupling. Product is made but goods cannot be issued without documents. Tests complete but the evidence does not apply to the release configuration. Capacity exists but access is not granted in the required window. A resource-saving change transfers cost, risk or burden to another participant.

The opposite error builds an elaborate network description without changing any decision. The operation needs the smallest set of actual couplings that can reverse the proposed action, together with a usable coordination result.

### OPS.11:3 - Forces

| Force | Practical tension |
| --- | --- |
| local clarity and cross-structure effects | A narrow view makes one decision easy while hiding a prerequisite or consequence elsewhere. |
| end-to-end coordination and independent authority | The result depends on several decisions, but their authority does not merge. |
| unlike quantities and comparison | Material, time, money, risk and human burden can all matter without having one valid scalar measure. |
| model detail and useful action | More represented relations can increase effort without improving the current choice. |
| stable agreements and changing conditions | A coordinated plan can become infeasible after access, evidence, demand or commitment changes. |

### OPS.11:4 - Solution

#### OPS.11:4.1 - Start from the proposed operating change

Name the operating result, current arrangement, proposed change and horizon. State which consequence would make the change useful or unacceptable. Reuse the current OPS.1–OPS.4 account and a matching OPS.8–OPS.10 result where available.

Select the affected Systems and participants by the actual consequences, not by the organizational chart alone. A supplier, customer, operator or neighboring service can matter without appearing inside the local department boundary.

If one direct pattern already settles the decision and no cross-structure relation can change it, use that result and stop.

#### OPS.11:4.2 - Identify the structures needed for this question

For each selected structure, recover the actual constituents, obtaining relations, applied constraints and use. Say what the current view shows and which material features it omits.

Use A.22 for the general structural question. Use E.18 for one transformation-flow structure and E.18.2 for a mathematical description when that lens is useful. Select an E.18.NET network only when at least two transformation-flow structures are independently identified and obtaining cross-flow relations connect their positions under the applicable constraints and use frame.

A branching process, several views of one flow, and several independently identified flows are different cases. Financial or decision relations need not be reclassified as a transformation flow to be relevant. If a required relation or identity cannot be recovered, retain the proposed description and name the missing basis.

#### OPS.11:4.3 - Recover each decision-changing coupling

For each coupling, state what depends on what, through which relation, under what condition and timing. Keep subject correspondence separate from production, supply, permission, evidence support, commitment or causal influence.

A useful working statement is: “This shipment can use this product only after these required documents are available”; “this test result applies to this configuration”; or “this provider grant permits this resource use during this interval.” Name the basis and responsible decision-maker when reliance on that statement matters.

Distinguish a missing fact from evidence that a proposed relation does not obtain. Missing permission does not establish forbiddenness; it means the action lacks the required permission basis. Conversely, a positive relation claim can still be unusable when an endpoint, scope or time binding is missing.

Follow only the couplings that can change the current decision. If another step is unaffected, leave its details with its own account rather than reconstructing it here.

#### OPS.11:4.4 - Compare coordinated alternatives

Trace the finite change through the selected couplings. Compare the current arrangement with feasible alternatives, preserving the operating-result unit, horizon, acceptance conditions and protected consequences.

Include resource demand, service effects, financial timing, recovery, human burden and other consequences only when they can change the choice. Obtain financial quantities from the responsible financial Method and assumptions; a generic “value” label cannot stand in for cash, cost, obligation or benefit. Do not add unlike quantities into one score without an applicable comparison rule.

Check that the proposed decisions can coexist. A new release limit can overload a shared acceptance activity; a batch change can delay the information needed for another decision; an earlier delivery can require funding or access that has not been supplied. Use OPS.10 for the relevant load/service question and OPS.9 when the claimed limiting mechanism is still uncertain.

When the operating model itself needs to be built or reconciled, use OPS.11.1 to connect activities, shared resources, branch joins and completion at the required scales. Reuse an adequate model when the needed couplings are already represented.

Keep modeling assumptions and evidence limits visible. A simulation can compare its modeled alternatives; it does not establish that the actual operation has the same relations or effects.

#### OPS.11:4.5 - Obtain or return the coordinated decisions

Name which operating policies can change within existing authority, which decisions must be obtained from other holders, and what remains held until an unresolved result is supplied. Distinguish an agreed coordinated plan, a proposed plan awaiting decisions, and the observed implementation.

Return the smallest actionable account: the selected change or alternatives, operative couplings, affected decision-makers, conditions and sequence needed for compatibility, protected consequences, unresolved inputs and next review. Use the existing operating account where it can carry that meaning.

A coordination result can be a partial agreement plus an exact missing return.

#### OPS.11:4.6 - Observe the consequences and reopen the affected part

After authorized implementation, inspect the accepted result and the affected coupling assumptions. Reopen the relevant decision when a provider changes access, evidence applies to another configuration, an acceptance condition changes, a resource becomes unavailable or an affected party's commitment changes.

When observation, actuation, supervision or feedback changes the operating choice, recover those actual relations and their delays through the current FPF control and temporal patterns.

An organization-design, capability-realization or product/service-engineering change returns to its owning practice. Keep a bounded operating adjustment local when that larger change is not needed.

### OPS.11:5 - Archetypal Grounding

#### OPS.11:5.1 - PumpWorks: a rig plan is not a release decision

PumpWorks continues weekly evidenced controller releases while incident I73, release candidate R42, safety question S19 and provider change P8 coexist. In this constructed use, the four ready test packages carry eight rig-hours of estimated load. The current capacity comparison names actual usable rig windows rather than the number of board cards.

The question is whether a changed readiness and rig-access plan can support the release work without losing another necessary condition.

| Selected structure or relation set | Concrete coupling needed for the decision | Receiving action |
| --- | --- | --- |
| rig-use arrangement | provider access, qualified operator and configuration jointly permit the specified test during the booked window | choose only feasible slots and return changed access to OPS.10 |
| test-evidence relations | T9's result must concern the configuration used for R42's release decision | preserve configuration/result correspondence; a result for another version does not close the evidence gap |
| release-supervision relations | ReleaseSupervisorTeam-S2 uses the required evidence and safety result to issue its authorized release, hold or other decision | obtain that decision separately from completing the test |
| existing service commitments | the evidenced-release horizon has parties, conditions and authority for revision | return changed feasibility to OPS.7 and the commitment holder |

Suppose lab-test permission is current and S19 concerns field release. The coordinated result can permit T9 within its actual test conditions, keep the field release held pending S19 and the release decision, and request the needed provider access. If S19 also governs the lab test, that test lacks a sufficient permission basis and remains held too.

OPS.8 maintains the ready queue and keeps incomplete matters visible. OPS.9 distinguishes readiness loss from an unsupported rig-bottleneck claim. OPS.10 compares the usable windows with eligible load and recovery scenarios. OPS.11 returns the compatible decisions and the missing safety or provider result to the appropriate owner.

If P8 reduces available rig time, reopen the capacity and dependent admission/release-policy decisions. Do not reinterpret a completed test as approval to bypass S19 or as evidence that the weekly service commitment has been fulfilled.

This case does not require claiming that every row is an independent flow structure. The selected permission, evidence, supervision and commitment relations are sufficient for the stated coordination question.

#### OPS.11:5.2 - Chemical make-to-order: material completion and document work

In a chemical make-to-order setting, goods issue depends on both available product and required commercial documents. The same order-processing resource can be needed for new-order transactions and invoicing. A material-only plan can therefore produce stock that cannot be shipped under the actual transaction conditions.

The first coordination result names that shared-resource and shipment-prerequisite coupling, then compares a compatible transaction/release policy with the local manufacturing plan. Actual commercial rules, financial consequences and authorization remain supplied inputs. The [Perez et al. (2023) model](https://doi.org/10.1016/j.compchemeng.2023.108363) is a worked comparison of this kind, not proof of a particular plant's realized improvement.

#### OPS.11:5.3 - AI-assisted operation: generation, acceptance and deployment

An AI-assisted software operation can generate candidate changes faster while human acceptance, test environments or deployment permissions remain unchanged. Candidate changes, tool calls, episodes, evidence and accepted releases have different identities and resource demands.

The practitioner follows only the relevant couplings: which configuration a test supports, who can accept the change, which provider/tool access is available, and what deployment conditions apply. A useful result might reduce admissions to the acceptance capacity, reserve a compatible test environment and return an unresolved release decision. It does not infer agent capability or software assurance from a higher generation count.

### OPS.11:6 - Bias-Annotation

| Bias | Consequence | Countermeasure |
| --- | --- | --- |
| diagram realism | A represented connection is treated as an obtaining relation. | Recover participants, relation basis, constraints and use. |
| one-flow reduction | Money, decisions, materials and evidence are merged because all are drawn as arrows. | State each relation and quantity under its own meaning. |
| department-boundary bias | A provider, customer or neighboring service consequence is omitted. | Select affected participants by the operating consequence. |
| local optimum confidence | A feasible local plan is treated as a feasible end-to-end plan. | Trace the necessary cross-structure conditions and shared resources. |
| authority aggregation | One coordinator appears able to grant every participating decision. | Obtain or return decisions to their actual authority holders. |

### OPS.11:7 - Conformance Checklist

1. Is one operating change or conflict and its intended result clear?
2. Are the selected actual structures distinguished from their views and mathematical descriptions?
3. Does each consequential coupling have recoverable participants, relation, conditions, timing and basis?
4. Are incompatible units and protected consequences retained in the comparison?
5. Can the proposed decisions coexist under the actual resource, evidence and authority conditions?
6. Does the result distinguish agreed change, proposed change, missing return and implementation evidence?
7. Is the next change that reopens each affected decision explicit?

Recognition means a practitioner can produce this bounded coordination result. Assurance requires the obtaining relations, qualified consequences and authority on which the chosen action relies; a complete map supplies none of them by itself.

### OPS.11:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Call every connected diagram a flow network. | Different structures and descriptions are collapsed. | Apply A.22/E.18/E.18.NET only to the object that meets the corresponding conditions. |
| Optimize material production while ignoring transaction prerequisites. | Product can accumulate without an admissible shipment. | Recover the actual goods-issue and shared-resource coupling. |
| Use evidence from the wrong configuration. | A completed test does not support the current release claim. | Bind the result to the exact subject and conditions. |
| Turn missing information into a negative world claim. | Lack of evidence is mistaken for evidence of absence. | Return the exact unresolved basis and its consequence for use. |
| Treat a coordinated diagram as permission. | The relevant decision-maker may not have authorized the action. | Obtain or return the required decision explicitly. |
| Build an exhaustive enterprise map when a smaller account already settles the question. | Unneeded modeling work delays the useful result. | Select only relations that can reverse the current choice. |

### OPS.11:9 - Consequences

The operation can coordinate a change without making local gains invisible to affected participants. A small coupling account can prevent incompatible schedules, unsupported release claims and displaced costs.

The cost is recovering the relations and obtaining decisions across boundaries. Some outcomes remain partial because another practice owns a necessary result. That partial result is useful when it identifies the exact next decision and preserves what can already proceed.

### OPS.11:10 - Rationale

Cross-structure coordination is needed because one operating result can depend on relations that no single view preserves. The useful unit is not the biggest possible model; it is the set of couplings that can change a concrete decision.

Retaining different relation meanings also preserves responsibility. A financial consequence, a safety permission and a causal explanation can all constrain the same plan while requiring different evidence and different decisions.

### OPS.11:11 - SoTA-Echoing

| Practice question and selected line | Serious alternative, trade-off and pattern change | Source roles, limits and reopen condition |
| --- | --- | --- |
| How can a locally feasible plan fail at completion? **Adapt** coordination of actual material, transaction and shared-resource prerequisites. | A material-only or transaction-only plan is cheaper but can omit a condition that makes its result unusable. Sections 4.3–4.5 and 5.2 retain the coupling and compare only the detail needed for the decision. | [Perez et al. (2023)](https://doi.org/10.1016/j.compchemeng.2023.108363) supplies a coupled-scheduling candidate and modeled failure evidence. Its chemical-supply-chain simulations do not validate every operation or a universal financial objective. Reopen when the business rule, shared resource or material/transaction coupling changes. |
| How much cross-structure representation is useful? **Adapt** a question-relative selection of obtaining relations at the relevant scales. | One universal flow diagram loses relation meaning; an exhaustive enterprise map costs more than some local decisions warrant. Sections 4.1–4.3 and 5.1 use a small actual-coupling account and keep descriptions separate. | [Wassick and Perez (2025)](https://doi.org/10.1002/aic.18688), §§3.2–3.5, supplies the current network-of-networks perspective. A.22 and E.18.NET supply the exact structural distinction. The perspective does not establish realized autonomous coordination or make every relation a flow. Reopen for a missing decision-changing structure or a simpler adequate representation. |
| Can faster software generation be treated as faster service? **Adopt** subject-correct coupling of generation, evidence, acceptance and permission. | Counting episodes or artifacts is cheaper but can omit acceptance capacity and deployment conditions. Section 5.3 retains the accepted-result boundary while 4.4 traces resource and permission consequences. | The existing Operations subject/current-account Methods and current FPF evidence and relation patterns supply the governing distinctions. They do not establish model capability, software assurance or field performance. Reopen when the actual acceptance path, provider constraint or evidence binding changes. |

### OPS.11:12 - Relations

OPS.1–OPS.4 supply the operating focus, relevant views, subject distinctions and qualified current claims. OPS.8–OPS.10 supply queue, diagnostic and capacity results that can require coordination. OPS.5–OPS.7 consume the resulting conditions within their own admission, continuation, priority and commitment questions.

Current FPF A.22, E.18, E.18.2 and E.18.NET govern selected structures and their descriptions; A.6.REL governs direct relation questions. C.11.CRC and C.11 govern finite comparison and choice. B.2.5 and the current control/temporal patterns apply when actual supervision, feedback and response timing affect the choice.

Organization Change Engineering supplies a relevant organization or coexistence Method only at its current scope; a case-specific result still has to exist. Engineering, clinical, safety, labor, legal, financial and other practices retain their direct decisions. OPS.12–OPS.18 provide their own human-condition, service, financial, account, Method-improvement, repertoire and quality Methods. OPS.19 consumes an OPS.11 coupling result only when several otherwise valid operating results conflict across subjects, scales, or horizons. OPS.16 local Method improvement and OPS.20 cultural continuation remain separate questions with their own evidence and authority.

### OPS.11:End
