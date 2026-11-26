## OCE.4 - Design an Organization's Contribution Architecture

> **Type:** Method pattern
> **Status:** Stable
>
> **Primary working result:** an **inspectable contribution-architecture design**: a supported description or proposal and, when a choice is authorized, the design decision. The result states the relevant specialization boundaries, contribution-relation specifications, acceptance and exception conditions, affected burdens, receiving decisions, and the evidence needed to establish which direct relations later obtain.

### OCE.4:0 - Use This When

Use this pattern when an organization concept has been selected or narrowed, but its chart, topology, or operating-model label still does not say how contributions reach their receivers. Enter when specialization boundaries, supplied results, information use, decisions, services, resource access, or coordination must be designed before positions or assignments can be settled.

Begin with a compatible `OCE.1` focus, `OCE.2` current account, and `OCE.3` concept comparison or equivalent content. Use an adequate existing design directly. State any gap that limits the design and what can be decided on the available grounds.

An organization concept specifies which results each participant must obtain, from whom and under which conditions the contributions will fit together. Its necessary reach follows from the service, capability or explanation commissioned. A question about one handover can be settled by its supplier, receiver and enabling conditions. A design spanning several units also has to show how those contributions can be available to the recipients that depend on them.

Use `C.30` directly when the question is only whether one actual or candidate structure is architecture-relevant. Use `OCE.5` for position identity, `OCE.6` for holder assignments and enabling relations, `OCE.7` for paired product-or-service and organization architecture decisions, and `OCE.9` for realization and organization-capability evidence.

#### OCE.4:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| specialization boundary | A selected boundary between domains of organization contribution or Work for the current design use. Decide separately which organization units, positions, assignments, and authority relations are needed at that boundary. |
| contribution-relation specification | Possible-future design content naming an intended direct relation kind or predicate, supplier and receiver, result or preserved condition, applicability, acceptance or use condition, exception return, scope, horizon, and evidence need. The specified relation remains proposed until its obtaining conditions are met. |
| contribution relation occurrence | One obtaining occurrence of the admitted direct relation named by a specification or current account. Its predicate, participants, applicability, interval, and evidence must be recoverable independently of the design. |
| contribution structure | An actual `A.22` structure selecting obtaining contribution relation occurrences and their participants for one declared use. Describe a candidate contribution structure as possible-future content until the selected occurrences obtain. Information-use, decision, access, service, coordination, legal-entity, and Work structures can remain separate. |
| contribution architecture | The way selected structures organize the named organization for its intended contribution, qualified under `C.30`. Actual architecture requires the applicable subject relations and architecture relation to obtain; candidate or desired architecture remains claim or description content. |
| position-design need | A need to decide whether one or more expected contributions warrant a stable organization position. Use `OCE.5` to assess that need and define a proposed or established position. The applicable rule determines who may establish it. |
| acceptance condition | The condition under which a receiver can use or accept the supplied result for the named decision. State the condition in the specification or claim, then use the applicable predicate and evidence to test whether it is met. |
| exception and escalation relation | An obtaining direct relation for returning an unusable result, resolving a conflict, or issuing a decision when ordinary contribution cannot continue. Specify that relation explicitly when designing a possible future. |
| contribution-architecture decision | A decision selecting possible-future organization structures, relation specifications, constraints, and open refinements for later change Work. Use evidence of realization to establish which selected relations obtain. |

### OCE.4:1 - Problem Frame

Organization design often begins with grouping: functions, products, customers, regions, programmes, professions, or platforms. Grouping helps attention, yet the organization contributes through relations that cross those groups. Evidence is supplied and used, decisions are issued and accepted, materials move, services are provided, resources are accessed, and exceptions return.

A contribution-architecture description makes intended relation specifications, any obtaining occurrences, and their receiving decisions visible while distinguishing proposed from actual relations. It may use several structures because activity grouping, decision representation, legal entities, information use, and service provision answer different questions. The design can then state which boundaries should change and which cross-boundary contributions must remain.

### OCE.4:2 - Problem

A target chart can move boxes while preserving the failed contribution path. A topology can give every group a familiar label while leaving the result, receiver, acceptance condition, or exception owner unknown. A generic “interface” can hide that one boundary carries evidence supply, a separate release decision, resource access, provider service, and field information.

The design then cannot guide position definition or realization. Teams infer authority from placement, capability from staffing, and acceptance from handoff. When problems appear, nobody can tell whether the missing element is Work, an assignment, access, an authority relation, a contribution predicate, or evidence that the relation obtains.

### OCE.4:3 - Forces

| Force | Tension |
| --- | --- |
| Specialization | Concentrated knowledge and equipment can improve contribution, while coordination and exception handling can add cost where a contribution crosses the boundary. |
| Stable ownership | Receivers need reliable contribution, while fixed boxes can preserve obsolete Work and authority assumptions. |
| Several structures | One picture is easy to communicate, while contribution, decision, access, service, legal, and Work structures need not coincide. |
| Participant knowledge | People performing Work and using its results can expose hidden relations, while participation does not transfer design authority. |
| Provider boundaries | External provision can add capability and scale, while contracts, access, recovery, evidence, and decision authority remain separate. |
| Realization | Designers need a usable possible-future account now; later Work may realize the relations, and observations can support claims that they obtain. |

### OCE.4:4 - Solution

Design from the intended contribution and the relations needed to produce, use, accept, and return results. Select the structures needed to explain or decide the design. Specify proposed crossings and identify the boundaries and conditions that implementation would require. Return the supported description or proposal to its intended recipient. When a choice is requested, make it within your authority or refer it to the decision holder.

A selected concept with an unsettled path from supplier to receiver is enough to start. For a claim that the arrangement operates, each actual contribution, information-use, decision, service, access, material-transfer, or coordination claim needs its own predicate, participants, scope, window, and evidence.

First inspect an existing coordination model, if one is available. A competent transaction account may already explain who requests a result, who commits to supply it, what is produced and declared ready, and how the receiver accepts or returns it. Reuse that account when the specialization boundaries and other enabling conditions can stay fixed. Broaden the design when changing a boundary could alter access, decision independence, support or another receiving contribution. Use the evidence available about the suppliers, receivers and effects. Seek their knowledge where a consequential assumption remains uncertain. Add the structures needed to settle the choice. Also ask whether the policies supporting the exchange fit together. For example, participants may report that early mismatch returns are penalized while nominal completion is rewarded. Compare a change to that recognition policy with moving the boundary; the policy owner must decide the change, and later use must test the expected improvement. Reuse the compatible policy and participant results from `OCE.3`. Section 11 explains this choice against transaction modeling and interacting organization-design policies.

#### OCE.4:4.0 - One bounded first design

For a small first use, keep the selected concept and already qualified constraints fixed and resolve one troublesome contribution crossing. Suppose a small engineering organization has the authority and participant inputs needed to decide how compatibility evidence reaches its release integrator. A short design note can state:

> Electrical supplies a configuration-C7 compatibility-evidence package to Integration for Friday's review. Each claimed interface must have a traceable source and test; Integration returns an unsupported claim to Electrical before evidence closure. The design decision keeps electrical expertise with Electrical and package assembly with Integration, using the agreed review time rather than merging the two specializations. Safety acceptance and release remain separate decisions. A missing source or an unworkable review burden reopens this design. Use the first package to test whether the planned supply and exception return actually work.

This is one bounded design result, not evidence that the supply relation already obtains. Reuse the supporting focus, current account, participant correction and decision basis instead of restating them. Add another structure, alternative or specialist result when it could change the decision or its grounds. State which decision or work a missing authority or protection premise limits. The same short note can carry the needed content listed below. Elaborate the questions that remain open rather than turning this first use into a full-organization redesign.

#### OCE.4:4.1 - Pattern-Use Unfolding

1. **Bind the design question.** Name the organization, intended outside contribution, selected concept, decision subject, authority, horizon, affected Systems, and first receiving use of the result.
2. **Recover the current relation basis.** Carry forward current Work and direct-relation evidence from `OCE.2`, plus constraints, participants, assumptions, and burdens from `OCE.3`. Record unavailable or incompatible inputs explicitly.
3. **Select structures by question.** Choose contribution, Work, decision, information-use, material-transfer, service, access, coordination, legal-entity, or other structures when they help establish or change the design. Select process, project or case viewpoints for the Method, coordination, state and authority questions they can answer. State each view's subject and whether the views concern the same Work. Retain the account of obtaining occurrences unless new evidence warrants revision; keep proposed structures and crossings modal. Preserve differences among the selected structures when those differences matter to the decision.
4. **Set specialization boundaries.** Group contribution or Work where shared knowledge, equipment, evidence, decision, locality, customer, product, service, or provider conditions justify it. State the condition and the burden moved by each boundary.
5. **Write contribution-relation specifications.** For every decision-bearing crossing, name the intended direct relation kind or predicate, supplier and receiver Systems, result or preserved condition, applicability, acceptance or use condition, exception return, scope, horizon, and evidence need. Use “interface” only as an orientation label after this content is visible. Do not report an occurrence before its predicate is satisfied. Where participants must negotiate a contribution, distinguish a request, the accepted commitment, production of the result, its declaration and receiving acceptance. Use `LDR.2` for the cooperation that obtains agreed terms and `OPS.13` when a promise must be established or changed. A changed request or withdrawn support returns to the affected participants; it does not silently change their existing commitments.
6. **Use participant knowledge.** Check assumptions about work, burden, accessibility, safety, provider support and service continuity against available evidence. Where further input matters, use a view the relevant participants can examine. State what their contribution supports or changes and any material gap that remains.
7. **Compare whole structures.** Compare how each candidate handles intended contribution, coordination load, decision latency, evidence, scarce capability, resilience, provider dependence, affected Systems, reversibility, and change burden. Keep unlike characteristics separate unless a justified aggregation Method exists. Include retaining the present specialization, with any coordination repair it needs, where that is a credible option. Compare total effort: recovering the existing model, participant inquiry, making the decision, establishing changed relations, maintaining descriptions and handling exceptions. A more detailed model earns its cost only through a decision or receiving use that needs it.
8. **Return the design or make the requested choice.** Return a description or proposal with its scope and conditions to the intended recipient. For a requested selection, use `C.32.PAD`, `C.11` or the applicable domain method. Identify the competent decision holder, the choice and its constraints, any accepted losses or open refinements, and grounds for rejecting alternatives or reopening the decision. Distinguish proposed relations from those in effect.
9. **Return position and paired-architecture questions.** Use `OCE.5` when continuity or eligibility warrants a position question and `OCE.7` when a product or service decision interacts with the organizational boundary. Keep holder, authority, capability, and realization questions with their owners.
10. **Specify realization evidence.** Name which later Work and observations can show that each specified relation obtains, fails, or remains unresolved. Supply design constraints to `OCE.9` without reporting organization capability.
11. **Test the contribution path against the commission.** For an organization concept, follow the promised result through the participating units and establish that the contributions fit together in time, authority and usable form. Check the alternatives the participants can still choose and the conditions that would reopen the design. An explanation of current operation needs grounds for which of those connections actually sustained it. An order to introduce the arrangement continues through the changes and their use in Work.

The steps are a reasoning aid. Existing structures may be repaired, new boundaries may be tried, and participant evidence may reopen an earlier decision at any time.

#### OCE.4:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| design boundary | Organization, contribution, concept, authority, horizon, first receiver, and affected Systems. |
| selected structures | Structure kind, constituents, occurrence refs when actual, modal structure or relation claims when proposed, declared use, and known losses. |
| specialization decisions | Boundary, reason, expected gain, any transferred burden, retained cross-boundary contribution and any open refinement. |
| contribution-relation specifications | Intended direct relation kind or predicate, supplier, receiver, result or preserved condition, applicability, acceptance/use, exception return, scope, horizon, and evidence need; occurrence ref only when independently established. |
| participant knowledge | Relevant evidence or participant contribution, what it supports or changes, and any material missing voice, burden or protection condition. |
| architecture decision | Design proposal or authorized selection, fixed constraints, any accepted losses or rejected alternatives, and the grounds for its stated status. |
| downstream returns | Any position, paired product/service, realization or specialist questions that remain, and the source or holder needed for each. |
| continuation | Realization observations, evidence windows, and the smallest event that reopens the decision. |

#### OCE.4:4.3 - What Changes in Practice

Practitioners design the contribution path before finalizing boxes. Every stable boundary has a reason, every decision-bearing crossing has an explicit relation specification, and every target relation retains its modal status until its direct predicate is satisfied. Position, assignment, capability, authority, and provider questions remain available for their own decisions instead of being hidden in the chart.

### OCE.4:5 - Archetypal Grounding -- PumpWorks Contribution Architecture

PumpWorks takes the revised `OC-PW-STREAM-ENABLING` option from OCE.3 into detailed design. It needs weekly evidenced AI-inspection releases alongside protected field service. `PumpWorks-EngineeringOrg` is the organization. Its first proposed Electrical interval is already occupied by service diagnostics. A different qualified interval, recognition of the specialist's cross-group contribution and an available exception route are conditions of this design. The owners can work out its interfaces now.

For that option, specify how each result reaches the person who needs it, who may accept safety evidence, who may authorize release, who has access to the test rig and model artifacts, and how field observations and provider support reach the group.

| Proposed crossing | Contribution-relation specification | Acceptance, exception, and evidence need |
| --- | --- | --- |
| Electrical → Release Integration | supply compatibility-evidence package for the named configuration | Integration can trace every claimed interface and test; unresolved mismatch returns to Electrical before evidence closure |
| Platform → Release Integration | provide qualified test environment and deployment service | Configuration and availability window match the release candidate; outage opens the fallback environment decision |
| AI provider → PumpWorks Integration | supply versioned model artifact and remote support under named access conditions | Provenance, compatibility, recovery, and access are present; provider supplies neither safety acceptance nor release authority |
| Release Integration → Safety | supply assembled evidence package and unresolved assumptions | Safety can evaluate the named release claim; rejection returns the exact missing or contradicted evidence |
| Safety → Release director | issue an evidence-acceptance result | Acceptance concerns the evidence question; the release director separately issues the release decision |
| Field Service → product and integration teams | provide incident and use-condition information | The report identifies product configuration and service episode; privacy and customer-use gaps return to their owners |

PumpWorks first considers a transaction-based repair of the Electrical–Integration exchange. Integration requests evidence for C7; Electrical can accept that request, produce the package and declare it ready; Integration checks the specified receiving conditions and accepts or returns it. This can fix an unclear handoff while keeping the two specializations. A team with an adequate existing model can reuse it without creating another account.

For the wider weekly-release decision, however, moving package assembly into Electrical would also change who challenges its claims and who needs the rig and provider support. PumpWorks therefore retains that transaction account and adds the separate decision, access and service questions represented above. It accepts the inquiry and maintenance cost of those additional views because the assembly-location choice cannot be settled from the evidence exchange alone. A competent transaction model extended with the same policy and resource answers would also be sufficient; redrawing its information in an OCE-specific format would add no gain. The design preserves independent Safety acceptance and compares the coordination burden of keeping Integration separate with the burden and conflicts a merger would introduce.

Now suppose the product team asks for C8 after Electrical has committed to C7. Electrical’s declaration that C7 is ready does not satisfy the C8 request. Integration identifies the missing C8 condition, and the affected participants can negotiate a different package and review time through `LDR.2`. Use `OPS.13` to establish whether the promise holder has accepted any change. The C7 obligation continues on its existing terms until an authorized change takes effect. The C7 evidence remains useful for that configuration. A proposed new interval still needs rig access and the appropriate safety acceptance. Reconsider other boundaries where the revised burden would affect them.

The proposed arrangement groups recurring release integration while retaining Electrical, Safety, platform, provider and field-service specialization. Send the design of the integration position to `OCE.5`, its holder and access conditions to `OCE.6`, and the product-module and organization boundary question to `OCE.7`. Before promising weekly releases, obtain the replacement specialist interval, protected service coverage, recognized cross-group work and fallback from their owners. If these cannot be supplied, the smaller repair to the Electrical–Integration handoff remains available for comparison. A narrower service promise requires its owner's decision.

The table describes proposed relations. In later realization, use `OCE.9` to compare actual Work and independently evidenced relation occurrences with the design and determine whether a bounded organization-capability increment is supported.

#### OCE.4:5.1 - Transfer Probes

| Setting | Reusable move | Required return or changed content |
| --- | --- | --- |
| public-hospital emergency flow | Start from the patient-care contribution, separate clinical decision, diagnostic-information, transfer, access, escalation, and continuing-service structures | Use clinical terms. Apply the legal, clinical-authority, labor, privacy, safety, bed-access or Operations findings the case needs. Identify the limit or obtain the missing professional decision where necessary. |
| distributed standards association | Start from the standard-publication contribution, volunteer Work, editorial evidence, member decision, ballot, publication-service, and employer-resource relations | Use the association’s bylaws and elected authority; retain several employers, volunteer availability, publication, and finance conditions rather than assuming one employer hierarchy |

These are hypothetical transfer probes of the design move. Adoption and benefit would require evidence from actual use.

### OCE.4:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| chart completion | Every required contribution receives a box, so the design appears complete. | Trace direct results to receiving decisions and exception returns. |
| interface bundling | Several unlike relations become one line. | Name each direct predicate and use a visibly reduced orientation label only afterward. |
| symmetry preference | Similar product or customer groups receive identical organization units. | Preserve differences in Work, authority, evidence, capability, provider, and service conditions. |
| informal-relation erasure | Useful observed coordination disappears because policy does not name it. | Preserve the observed relation and decide whether to formalize, support, replace, or stop relying on it. |
| participation-as-approval | A workshop is treated as design authority or adoption. | Record the knowledge contribution and keep authority and realization separate. |
| future-as-current | The selected picture is called the new organization. | Keep possible relations in claim and decision content until direct evidence shows they obtain. |

### OCE.4:7 - Conformance Checklist

- [ ] The organization, contribution, concept, authority, horizon, and first receiving use are explicit.
- [ ] Each selected structure answers a declared question and states its losses.
- [ ] Specialization boundaries name their gain and moved burden.
- [ ] Every decision-bearing crossing has a contribution-relation specification naming the intended direct relation kind or predicate, supplier, receiver, result, conditions, acceptance/use, exception return, and evidence need.
- [ ] A relied-on interface identifies its participants, contribution and receiving use.
- [ ] The design identifies relevant participant knowledge and what it supports, changes or leaves uncertain.
- [ ] Contribution-relation specifications, modal architecture claims, and obtaining relation occurrences remain distinguishable.
- [ ] Position, holder, assignment, capability, authority, product/service, and realization questions are referred to the appropriate source or decision holder where their answers are needed.
- [ ] The description or proposal identifies the relevant boundaries and conditions. Where a decision has been made, its authority, fixed constraints, any accepted losses or open refinements, and grounds for reopening are clear.

### OCE.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Create product teams and define interfaces.” | Name the contribution and Work basis for each boundary, then write separate possible-future specifications for supplied-result, decision, information-use, access, service, and coordination relations. |
| “One owner per deliverable.” | Recover the result, receiver, acceptance decision, contributing Systems, authority, and exception path; choose an ownership predicate only when it is actually governed. |
| “Put everyone involved in one team.” | Select the smallest contribution-bearing boundaries and preserve scarce capability homes, independent acceptance, providers, and continuing service where they change the decision. |
| “The matrix has two reporting lines.” | State which contribution, decision, authority, access, or coordination relation each line is intended to represent. |
| “The architecture is now implemented.” | Compare actual Work and obtaining relations after change; retain the current item as decision and possible-future description until then. |

### OCE.4:9 - Consequences

The contribution-architecture design becomes inspectable before a chart is finalized. Position design can start from expected contributions, and realization can test independently obtaining relation occurrences against explicit specifications instead of visual conformity.

Examining and maintaining several structures can take time, and an attractive topology can remain undecided when a provider, authority, access, safety, or service condition is missing.

### OCE.4:10 - Rationale

An organization contributes through actual Systems, Work, and direct relation occurrences. Design-time specifications preserve why a proposed boundary exists without asserting that the relation already obtains, so later evidence can show whether the intended architecture was realized.

Several structures are expected. The activity arrangement, decision representation, legal entities, information use, access, and service provision can overlap without becoming one structure. Their non-isomorphism can expose a design risk rather than a modeling defect.

### OCE.4:11 - SoTA-Echoing

#### OCE.4:11.1 - Current-Line Selection for Contribution Design

The question is how Electrical's compatibility evidence can reach Integration in a usable form, and whether the specialization that supports that exchange should change. Compare methods on that same crossing and release horizon, including investigation, participant time, implementation, exceptions and upkeep of the account.

| Competent answer | What it supplies and when it is sufficient | Choice made here |
| --- | --- | --- |
| A bounded DEMO transaction model, including its BPMN expression | The initiator/executor exchange distinguishes coordination from production and includes rejection and allowable revocation. It can repair the evidence exchange while leaving existing boundaries intact. | **Adopt** the request-to-receiving-result distinctions in step 5 and the changed-C8 case. Reuse an adequate model. **Adapt** its questions into ordinary contribution specifications; a DEMO model and its full transaction semantics are not prerequisites for every OCE design. |
| An organization design using Galbraith's interacting policies | Strategy, structure, information/decision processes, rewards and people policies allow a designer to examine why a boundary and its coordination are or are not supported. A competent use includes lateral relations, rather than stopping at the chart. | **Adopt** the need to examine policy fit in steps 4, 6 and 7. If the problem is an unrewarded or unsupported exchange, changing the relevant policy may be sufficient; another specialization boundary is not automatically the answer. |
| The scoped combination used by OCE.4 | Keep a sufficient exchange account, then connect only the decision, access, service or other structures that can change the specialization choice. Preserve each result's acceptance and realization conditions. | **Construct** the boundary decision from these answers in steps 7–10 and the PumpWorks case. Accept additional inquiry when it prevents a boundary choice from hiding a consequential burden or independent decision. |

The combination is selected for the multi-relation PumpWorks choice, not ranked above the other methods for every use. It costs more than fixing one adequately modeled exchange and does not supply DEMO's formal protocol analysis. That is an accepted trade-off when a small, inspectable decision across unlike relations is needed and a complete formal model would have no receiving use. If an established transaction or policy-design practice already supplies those answers, use its result and stop.

Reopen when the extra structures add no useful ground for the decision, maintaining separate views creates inconsistent commitments, or another method supplies the same boundary and receiving-use answers at lower total effort.


#### OCE.4:11.2 - Source Contributions and Boundaries

| Source line | Retained contribution | Use boundary |
| --- | --- | --- |
| Guerreiro and Dietz, [DEMO enhanced BPMN](https://arxiv.org/abs/2410.08215) (2024), §§2 and 4–6 | Serious constructive alternative for coordination: transaction roles, production and receiving acceptance, exceptions and conditional revocation. | The paper develops a modeling construction and illustration. It does not establish comparative effectiveness for PumpWorks; OCE does not import the whole DEMO ontology or claim its protocol guarantees for plain specifications. |
| Galbraith, [Star Model](https://jaygalbraith.com/services/star-model/) and [organization-design practice](https://jaygalbraith.com/services/organization-design/) | Serious policy-design alternative: compare organization options through interacting structure, processes, rewards and people policies for the strategy. | These practitioner explanations support the policy questions, not an empirical ranking or a rule that every design needs all five policies changed. |
| Current FPF `A.22`, `C.30`, `C.30.AD`, `C.32`, and `C.32.PAD` | Selected structures, actual versus modal architecture, candidate synthesis, descriptions, and decisions remain separate. | Use these distinctions to qualify the local design; derive specialization boundaries and contribution content from the organization’s working problem. |
| Joseph and Sengul, [current organization-design review](https://doi.org/10.1177/01492063241271242) | Contemporary organization design uses complementary configuration, control, channelization, and coordination approaches; one representation or feature does not cover the field. | The review organizes research rather than selecting a local organization, relation predicate, or architecture decision. |
| Albert, [organization-structure perspectives](https://doi.org/10.1007/s41469-023-00152-y) | Activity arrangement, decision representation, and legal-entity perspectives can expose different design consequences. | Select the local organization and any additional perspective needed for its design question. |
| Grote et al., [contribution-based engineering role modeling](https://doi.org/10.1109/ISSE65546.2025.11370103) | Required contributions and stakeholder evidence can expose organization-specific contribution bundles and gaps. | The evidence covers three industrial cases and one workshop/clustering Method. Test transfer beyond those cases; decide local positions and assignments separately. |
| Fraccaroli, Zaniboni, and Truxillo, [work-design review](https://doi.org/10.1146/annurev-orgpsych-081722-053704) | Work characteristics, technology, diversity, and affected-person outcomes belong in design. | Supply the target organization and authority basis locally, and select a Method suited to its design problem. |
| Schulze-Meeßen and Hamborg, [participatory work-design representations](https://doi.org/10.1016/j.apergo.2023.104012) | Participant-facing representations can improve recognition and design knowledge. | Use representations to elicit design knowledge; test actual relations, authority, capability, and effects with the evidence appropriate to each claim. |

Reopen when representative use exposes a recurring contribution crossing the result cannot express, a serious alternative produces the same decision with less modeling burden, or a direct source changes the specialization or participant action.

### OCE.4:12 - Relations

- `OCE.1` supplies the organization, contribution, authority boundary, and affected-System scope. `OCE.2` supplies current Work and direct-relation evidence. `OCE.3` supplies candidate relation structures, assumptions, participants, and burdens.
- `A.22` governs actual selected structures; `C.30` governs possible-future structure and relation content; `A.6.REL` and the applicable domain predicates govern obtaining direct relation occurrences; `C.32.PAD` governs an architecture decision when that use is current.
- `OCE.5` consumes stable position-design needs. Use `OCE.6` to establish which assignments and enabling relations hold and which require action from their responsible parties. `OCE.7` consumes organization-side structure for paired product-or-service decisions.
- `OCE.9` consumes design constraints and later returns realization evidence. `LDR.1` may consume contribution architecture for leadership-contribution distribution. Use `LDR.2` to negotiate contributions where agreement is needed, and `OPS.13` to establish the status, terms and authority of an operating promise or its proposed change. Their results can refine a crossing while other architecture decisions remain in force.
- Strategy, Corporate Governance, Operations, Administration, Systems Engineering, finance, legal, labor, safety, privacy, and other specialists supply only their available compatible results or qualified direct sources.

### OCE.4:End
