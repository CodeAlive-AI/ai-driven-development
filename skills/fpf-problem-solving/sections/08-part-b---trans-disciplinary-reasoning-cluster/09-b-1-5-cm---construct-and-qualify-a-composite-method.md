## B.1.5.CM - Construct and Qualify a Composite Method

> **Type:** Method pattern
> **Status:** Stable

> **Primary working result:** either a bounded composition result whose whole, participants, and load-bearing relations are independently supported, or a **prospective candidate Method account** with proposed relation sets, guards, variation, recovery, stops and unresolved conditions needed by its receiving use. Writing the account creates neither the Method nor an obtaining architecture.

### B.1.5.CM:0 - Use This When

Use this pattern when a proposal already names an intended Method whole—often a methodology, operating model, playbook, integrated process, or local way of working—and the next decision needs to know what can truthfully be said about that whole now.

Begin with the proposal's intended result, participants, relation claims, guards, burdens, unresolved conditions, and selection reason. Recover the whole semantics needed for identification before choosing the result branch.

The first useful result is deliberately two-branched. If the whole and participant Methods are identified and the required relations are shown to obtain, record the bounded composition result. Otherwise return the strongest prospective account or lower claim that the evidence supports. That account can finish a present design comparison while whole identity or relation truth remains unresolved. Select later realization or testing only when its obtainable contribution warrants the full burden and is feasible.

Do not require prior performance of C.32.MWA.PP when equivalent proposal content is already available. Do not treat a coherent description, selected architecture, WorkPlan, tool implementation, or successful first trial as Method construction or identification by itself.

#### B.1.5.CM:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| proposed Method whole | A claim that several contributions form one reusable Method for a stated use. It may be no more than a candidate account. |
| whole semantics | Intended result or preserved condition, reusable procedure or invariant, applicability, participants, permitted variation, bounds, and reidentification rule. |
| participant status | Whether each named participant is an identified Method, candidate account, other kind, or unresolved subject. |
| obtaining composition result | A result about an identified whole and identified participant Methods whose required `B.1.5` relations are independently shown to obtain for the bounded claim. |
| prospective candidate account | An episteme proposing a possible reusable whole while identity or relation conditions remain unresolved. |
| relation set | Named proposed or obtaining composition, order, result-use, allocation, support, authority, or other relations. Their truth statuses remain explicit. |
| realization/test WorkPlan | A plan for later Work that could implement the proposal and return observations. It is not performed Work or evidence that the Method exists. |

### B.1.5.CM:1 - Problem Frame

Method Engineering often produces coherent proposals before the proposed practice exists. Situational Method Engineering and design-Method research offer useful construction and adaptation moves, while FPF keeps the proposed account, world-side Method, MethodDescription, WorkPlan, performed Work, and obtaining relations distinct.

A proposed whole can still be valuable. It can state an invariant, guards, variants, participant roles, stops, and a bounded trial. The error is reporting possible-future content as already obtaining.

### B.1.5.CM:2 - Problem

One failure declares a whole whenever a document gives several steps a shared name. Another refuses to state anything useful until a mature Method has already been identified. A third treats participant co-use, Work order, or a successful tool integration as `methodPartOf` evidence.

The first error overclaims, the second prevents learning, and the third confuses several relation structures. B.1.5.CM needs a positive lower branch that supports present comparison or later realization while keeping uncertainty explicit.

### B.1.5.CM:3 - Forces

| Force | Tension |
| --- | --- |
| Useful proposal | A project needs a coherent possible-future account, while coherence does not identify a Method. |
| Composition evidence | Participant Methods and relations may be supported unevenly, while one missing load-bearing relation can defeat the whole claim. |
| Variation | A reusable Method permits bounded variation, while unlimited adaptation destroys reidentification. |
| Trialability | A WorkPlan can make uncertainty testable, while planned or performed Work does not backdate Method existence. |
| Honest lowering | A lower result must remain actionable, while it cannot hide unresolved identity or relation claims. |

### B.1.5.CM:4 - Solution

B.1.5 supplies the exact composition test. This construction supplies the candidate whole, constituent contributions, interfaces and grounds to which that test applies; it can also return a useful relation account below the whole-Method threshold. Use an already complete B.1.5 result directly rather than reconstructing it.

Recover the proposed whole's semantics, test whole and participant identity separately from relation truth, and return the strongest branch the evidence supports.

#### B.1.5.CM:4.1 - Pattern-Use Unfolding

1. **Name the receiving use.** State the result or preserved condition, situation family, intended users or performers, consuming decision, configuration or edition, and time window.
2. **Recover whole semantics.** State the reusable operations or invariant, entry and exit, applicability, participants, permitted variation, bounds, stops, and reidentification rule. If these cannot be stated, return the missing-account question.
3. **Preserve participant statuses.** Identify each Method under `A.3.1` where supported. Keep candidate accounts and other subjects at their existing statuses.
4. **Name the relation sets.** State every load-bearing proposed or obtaining relation, including Method composition, Work order or overlap, result use, allocation, support/provider access, authority, and description correspondence as applicable. Do not infer one relation from another.
5. **Test the positive branch.** Record an obtaining composition only when the whole and parts are identified as Methods and the required `B.1.5` relations are shown to obtain within the bounded claim.
6. **Return the prospective branch when needed.** State the candidate whole, participant statuses, proposed relation sets, guards, adapters, alternatives, recovery, variation points, burdens and unresolved conditions needed for the receiving use. A traceable proposal can answer that use while its stronger whole claim remains unresolved.
7. **Lower independently.** When whole semantics, identity, or one relation remains too weak even for a useful candidate, return the supported fragment, relation claim, WorkPlan question, or stop. Do not pad the account to look complete.
8. **Choose a useful continuation when needed.** Use C.11.DUA to compare the result a realizable implementation or trial could add with its full burden, including access, allocation, authority and the available window. When that Work is selected, name its observations, acceptance and failure conditions, authority and reconsideration rule; prepare a WorkPlan where coordination needs one. Otherwise finish with the supported account or lower result and the limitation that matters to its recipient.

#### B.1.5.CM:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| use and whole semantics | Intended result/preserved condition, situation, operations or invariant, applicability, participants, variation, bounds, and reidentification. |
| participant account | Each subject, kind or status, identity basis or open condition, and proposed contribution. |
| relation sets | Each direct relation, truth status, evidence, guard, and receiving use. |
| branch verdict | Obtaining composition result, prospective candidate account, or lower return with decisive reason. |
| prospective content | Guards, adapters, alternatives, recovery, stops, burdens, and variation points when the lower branch applies. |
| continuation, when selected | Later Work and observations, authority, acceptance/failure and reconsideration condition; a realization/test WorkPlan where its coordination needs one. |

#### B.1.5.CM:4.3 - What Changes in Practice

Practitioners can write and test a coherent proposed Method without pretending that documentation created it. A positive composition claim becomes stronger because its identity and relation evidence are explicit; a prospective account remains useful for comparison through its guards, variation, recovery and stated limits. A selected implementation or trial adds the continuation needed to learn more.

### B.1.5.CM:5 - Archetypal Grounding — `C-EC-Release-v2`

The EC-417 project proposes `C-EC-Release-v2` as a whole for safety-relevant release coordination.

Under A, the team waits for signed supplier evidence before integrating the software. Under B2, it integrates from a versioned provisional edition, reconciles it with signed evidence before safety closure, and assigns most preparation of the changes between the editions to the supplier-configuration role to keep the safety engineer within the peak limit. [C.32.MWA.PP §5.3](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwapp53---possible-future-alternatives-a-b-and-b2) gives the timing and capacity comparison. A is selected before integration; recovery R is used when closure fails after early B2 integration.

The proposed account states:

| Whole position | Proposed content |
| --- | --- |
| intended result | a release-authorizable evidence and integration state for one safety-relevant change |
| situation family | internal or supplier-originated hardware/software changes with versioned provisional or signed pinout evidence |
| invariant | provisional evidence may support reversible early integration, but signed evidence and repeated checks are required before safety closure and release authorization |
| participants | identified `M-HW-Verify`, `M-SW-Integrate`, `M-Supplier-Approve`, and `M-Release-Authorize`; candidate reconciliation accounts remain separate |
| permitted variation | pre-entry A when signed evidence or B2 entry conditions differ; B2 for bounded early integration; post-entry recovery R after a failed B2 closure |
| bounds and stops | confidentiality, human authority, `D-8` safety peak at or below `0.40`, signed evidence before closure, and reversibility until `D-1` |
| reidentification | preserve the intended result, invariant, participant-status boundary, evidence-version guard, authority, and A/B2/R branch meanings |

The four participant Methods are identified, but the proposed whole is not. Their co-use and the proposed order do not establish that they are Method parts. The relation sets therefore remain proposed:

- provisional-evidence integration at `D-21` and signed-evidence reconciliation at `D-8`;
- signed evidence and accepted safety result before release authorization;
- supplier preparation responsibility for `1.60 h` under B2;
- separate safety and release authority;
- PLM, rig, and provider-access conditions; and
- description correspondences from evidence version through integration bundle and verification result.

For this selected trial, B.1.5.CM returns a prospective candidate account with a WorkPlan covering at most three B2 releases. The whole and relation claims remain proposed.

Before each entry, `SafetyReviewer-17` performs `W-SafetyEvidenceDecision-17` under `ASG-SafetyReview-17` and `AUTH-SafetyEvidence-17` to accept or reject the named evidence conditions; `ReleaseDecider-17` then performs `W-ReleaseDecision-17` under `ASG-ReleaseDecision-17` and `AUTH-ReleaseDecision-17` to decide branch entry and release, withhold, or next-slot disposition. Neither decision or authority relation substitutes for the other.

In B2, `TraceReviewer-17` accepts or rejects each AI trace suggestion used by the release branch under `ASG-TraceReview-17` and `PERM-TraceAcceptReject-17`. [The full EC-417 application, §16.9.5](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#fpfreference1695---5-build-the-repertoire-and-criteria-without-preselecting-an-architecture) records the one permission grant and the dated Work `W-TraceAcceptReject-17-01` that returns acceptance in the filled case. The separate relation `PEX-TraceAcceptReject-17-01` connects that dated Work to the permission it exercised. `EV-PEX-TraceAcceptReject-17-01` supplies evidence about this exercise. Each additional used suggestion requires its own dated decision Work and result, confirmation that the permission applies at that time, and its own Work-to-permission exercise relation.

Missing signed evidence after early integration triggers recovery R. In R, preserve the performed-integration record and evidence history. Repeat the evidence comparison and affected verification when evidence arrives by `D0` while the existing evidence and reversibility guards still hold. Record whether early integration is retained, rolled back, or repeated, and the added burden. If closure remains unresolved at `D0`, the release result is withhold/next-slot and this R occurrence ends as a failed B2 trial.

`ASG-TraceReview-17` and `PERM-TraceAcceptReject-17` also end at `D0`; continuing safety or release relations extend neither. The trial WorkPlan therefore contains no post-`D0` AI suggestion, trace-review Work, assignment, permission, result, or exercise, and claims no other later Work. Unresolved R may motivate later planning, but this case asserts no post-`D0` recovery WorkPlan, PlanItem, planned endpoints, qualification/currentness result, readiness, assignment, permission/authority, or later Work.

When later non-AI recovery needs coordination, the project may create a new `A.15.2` WorkPlan; `A.15.2` itself does not require planning before every otherwise valid later Work. Planned or unplanned Work would still need its separate qualification/currentness, readiness, assignment, permission/authority, and `A.15.1` occurrence as applicable. These stops preserve all earlier Work and evidence history. A is only a pre-entry alternative.

Acceptance observations include whether each trial respects confidentiality and authority, remains below the `D-8` capacity bound, preserves evidence/version correspondence, and reaches a truthful release or recovery result by `D0`. An attempted post-`D0` AI-supported continuation, or an assertion of later Work without a separately admitted `A.15.1` dated Work occurrence, is an explicit stop and failed trial observation. The withhold/next-slot result preserves earlier Work and may motivate planning; it creates neither a recovery WorkPlan nor later Work. Those observations may support, narrow, split, or reject the account. They do not by themselves identify the whole; `A.3.1` remains the identity owner.

#### B.1.5.CM:5.1 - Finish a Design Comparison Before a Trial Is Available

Suppose an earlier design use asks whether this release-coordination proposal preserves signed-before-closure, confidentiality and the A/B2/R distinctions well enough to compare with another proposal. The current sources support that account, but whole identity and composition relations remain unresolved, and the team has no rig access, allocated effort or trial window. Return the traceable prospective account with those identity and relation limits. The receiving designer can compare the proposals and finish that question on the available content.

A later opportunity with useful obtainable observations can warrant implementation or a trial and its coordination plan. The already selected three-release case above retains its WorkPlan, observations and stops.

### B.1.5.CM:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| document-whole bias | Shared title and ordered sections become one world-side Method. | Recover whole semantics, identity, and relations independently. |
| co-use bias | Several Methods used in one project become participant parts of a composite. | Require identified whole/parts and obtaining `B.1.5` relations. |
| trial-success bias | One successful Work occurrence identifies a reusable Method whole. | Use trial observations as later evidence and keep `A.3.1` separate. |
| unlimited-adaptation bias | Every changed proposal keeps the same identity. | State permitted variation, bounds, and reidentification rule. |
| architecture-decision bias | Selecting a proposed relation set makes it obtain. | Preserve proposal truth until realization and evidence support a stronger claim. |

### B.1.5.CM:7 - Conformance Checklist

- [ ] The proposed whole has an intended result or preserved condition, situation, reusable operations/invariant, applicability, participants, variation, bounds, and reidentification rule.
- [ ] Whole identity and every participant status are independently stated.
- [ ] Method composition, Work order/overlap, result use, allocation, support, authority, and description relations are not inferred from one another.
- [ ] The positive branch requires identified whole and parts plus obtaining `B.1.5` relations.
- [ ] The prospective branch preserves proposed truth and names guards, adapters, alternatives, recovery, stops, burdens, and unresolved conditions.
- [ ] WorkPlan, performed Work, observations, MethodDescription, and Method identity remain distinct.
- [ ] The result can lower below a candidate whole when load-bearing semantics or relations are missing.
- [ ] A supported account or lower result can complete its receiving use. Any selected continuation has a worthwhile feasible contribution and names the needed later Work, observations, authority, acceptance/failure and reconsideration.

### B.1.5.CM:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “We wrote the method.” | Say that a candidate account or MethodDescription was written; identify the Method separately. |
| “The architecture was selected, so its relations obtain.” | Keep the decision and proposed relations separate from realization evidence. |
| “All participants passed A.3.1.QM, so they form a whole.” | Test whole identity and `B.1.5` composition independently. |
| “A failed trial falls back into the earlier history.” | Preserve performed Work and define a separate recovery branch. |
| “Wait for perfect proof before saying anything.” | Return the supported prospective account or lower claim with the limits needed for its use; select further testing when its obtainable contribution warrants it. |

### B.1.5.CM:9 - Consequences

Projects can move from architecture proposal to realization and learning under explicit identity and relation conditions. Strong composition claims are recoverable, while weaker proposals remain actionable without treating their Methods or relations as established.

The cost is a visible open identity or relation question. Some proposed methodologies will remain candidate accounts after useful trials, and some will split into several Methods or a relation structure instead of maturing as one whole.

### B.1.5.CM:10 - Rationale

Construction and description can change epistemes and WorkPlans immediately; they do not create a reusable way of doing in the world by assertion. The two-branch result preserves this difference while letting possible-future content guide real Work.

B.1.5.CM does not depend on applying C.32.MWA.PP first. C.32.MWA.PP is one common source of proposed relation sets, but any equivalent content can enter B.1.5.CM directly.

### B.1.5.CM:11 - SoTA-Echoing

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| Henderson-Sellers and Ralyté, [Situational Method Engineering review](https://opus.lib.uts.edu.au/handle/10453/13456) | Construction and adaptation of Methods for situations. | Source-local fragment, process, role, and assembly concepts do not establish FPF identity or composition. |
| Gericke, Eckert, and Stacey, [Elements of a design method](https://doi.org/10.1017/dsj.2022.23) | Intended use, procedure, representation, tool, ecosystem, and adaptation conditions for a coherent proposal. | Conceptual completeness does not prove world-side Method existence or relations. |
| Current FPF `A.3.1`, `A.22`, `B.1.5`, and `C.32.MWA` | Method identification, selected structures, Method composition, and several-structure synthesis. | B.1.5.CM adds the truthful whole-versus-prospective-account resolution and realization continuation. |

Reopen when a representative proposal cannot be expressed through the positive/prospective/lower branches, when variation repeatedly defeats reidentification, or when a positive composition claim cannot be distinguished from Work order or co-use.

### B.1.5.CM:12 - Relations

- `A.3.1` governs whole and participant Method identification; `B.1.5` governs any Method-composition claim.
- C.32.MWA.PP commonly supplies proposed relation sets and architecture alternatives, but it is not a compulsory predecessor.
- A.3.1.QM supplies individual qualifications without whole identity or compatibility.
- Later realization, identification, description, support, trial, and assurance patterns consume only the branch and truth status returned here.
- A prospective account, WorkPlan, selected architecture, or trial result supplies no obtaining ArchitectureRelation or `methodPartOf` fact by itself.

### B.1.5.CM:End
