## SYSE.2 - Develop Linked Use and System Concepts

> **Status:** Stable

### SYSE.2:1 - Problem frame

Use this pattern when a project has selected an actual System, retained an intended System referent, or bounded
another engineering subject, but the proposed concept cannot yet be defended through concrete use. The team may
have, for example, an internal block diagram, requirement set, component list, product concept, or preferred
technical solution while phrases such as *environment*, *suprasystem*, *using system*, *Concept of Operations*, *use case*,
*scenario*, *requirement*, or *user story* stand in for several Systems, intended System referents, conditions,
relations, and effects. A compatible `SYSE.16` use-context account supplies decision-relevant operational
structures, neighbours, conditions, and outside changes. A compatible `SYSE.17` affected-system account supplies
qualified consequence claims and unresolved bearers. Use only result claims compatible with the current decision.

The result is a **linked use-and-system concept proposal**: bounded claim content that connects a concrete
use situation with a candidate System concept and states any main uncertainty. One or more descriptions may
carry the claims; no document form is required.

First useful move: link one concrete use claim to one candidate system-concept claim and state any main
uncertainty. This is enough to expose a grounded architecture question. Add further content—for example,
another use situation, structure, participant, failure, effect, or representation—only when it can change the
candidate or its boundary.

If this link is missing, internal elegance can substitute for usefulness. A pump passes a component test but
worsens downstream flooding; planning software is installed but cannot support production decisions with the
available data; a retrofit design works in an empty building but cannot be realized while the building is
occupied.

The payoff is a revisable account that keeps outside use connected to the concept for the selected subject.
Evidence about use can change that concept, while architecture and realization findings can change the use,
boundary, or affected-System claims.

Use this pattern while a concrete use claim and a candidate System concept still need to be developed together.
Use `C.30` and `C.32` when the current question is grounded architecture and candidate synthesis, `A.3.4` when
the question is whether one actual bounded change occurred, and the applicable Operations Management pattern
for continuing Work. Return to `SYSE.1` when evidence changes which System should orient the project.

At the first consequential use of source wording, ask: **does this claim connect the concept for the selected
subject with a concrete use situation, participating or affected Systems, conditions, and outside effects?** If yes, name those
subjects and relations and use this pattern. A representation—for example, a ConOps, use case, scenario,
requirement, user story, diagram, or model—presents some of these claims. Its form establishes neither their
truth nor the required form for the proposal.

When the concrete use itself is disputed across participants, `SYSE.54` supplies collaborative event
modelling to recover behaviour and its consequential alternatives. Bring its compatible account back to
the linked concept here; an already adequate scenario needs no workshop.

### SYSE.2:2 - Problem

A project-system choice does not determine the useful boundary or organization of the selected actual System or
intended referent. The same desired effect can be achieved through different actual or proposed changes—for
example, changes to the designated System, an external System, an interface, a
Work arrangement, or several sides together. A containing System may matter, but parthood must be established
directly. Use, interaction, placement, ownership, authority, affectedness, and shared environment are other
relation kinds and require their own grounds.

One-way handoffs make this worse. A supposedly complete use description is handed to concept development, then
architecture or realization discovers that the use cannot be supported. Conversely, one attractive technical
concept narrows the use description until only its successes remain visible. The recurring engineering problem
is to develop the use claims and system concepts together while preserving the distinctions needed to return a
failed claim.

### SYSE.2:3 - Forces

| Force | Tension |
| --- | --- |
| Outside effect and project boundary | Use justifies the System concept, while the useful change may cross the assumed boundary. |
| Several environment Systems and one simple story | A compact scenario helps reasoning, while one hierarchy can hide non-nested participants and affected Systems. |
| Function and feasible bearer | Required functioning guides concept development, while a function word or diagram does not supply a bearer. |
| Working descriptions and physical grounding | Models and scenarios keep claims inspectable, while their form does not establish use, transformation, architecture, or evidence. |
| Early usefulness and completeness | One linked claim can expose the next question, while a comprehensive form can add work that does not change that question. |
| Continuing revision and decision stability | Use and concept claims must change with evidence, while each downstream architecture question needs a stated current basis. |

### SYSE.2:4 - Solution

#### SYSE.2:4.1 - Start with one decision-changing use situation

Take the immediate engineering subject and its receiving purpose from the project-system choice account, or identify that bounded subject directly when no SoI question remains. For a creator, retain the product-use grounds while developing the creator's own use and System concepts. If that choice is
needed but no compatible `SYSE.1` account is available for the same subject and decision, use a qualified direct
source for the focus claim or record the missing project-focus result and stop only the linked claim
it blocks. An individual can explore a linked proposal from a provisional focus. When its use depends on
joint action, use `SYSE.1:4.4.1` to establish the common referent and contribution connections for that action,
or retain the unresolved coordination condition. For an actual System, describe an actual or possible-future
situation in which it participates. For a not-yet-present referent, keep the
intended participation in modal plan, decision or description content; do not report the intended System or
participation as already actual. State:

1. the subject that relies on, uses, changes, or is affected by the proposal;
2. the direct relation by which that subject enters the use;
3. the condition or change expected;
4. the outside effect that matters to the current decision; and
5. any uncertainty that could change the concept.

Name the relying subject under its admitted kind; a person and a System are only two possible kinds. State the
direct relation by which it enters the use—for example, reliance, participation, performance of Work, or affectedness.
Include affected Systems or intended System referents whenever their qualified consequence claims can change the
decision; participation in or ownership of the designated System is not required.

#### SYSE.2:4.2 - Name the subjects and direct relations hidden by environment language

Start from compatible current `SYSE.16` and `SYSE.17` results for the same subject, configuration, use, horizon,
and decision. If either result is unavailable, recover only the subjects and direct relations needed for the first
linked claim. Use `SYSE.16` when the decision needs several operational structures or a co-change boundary, and
`SYSE.17` when it needs active discovery of consequence-bearing Systems. A neighbouring System may matter, for
example, through constructive parthood, placement, interface, interaction, causal participation, use,
transformation, collection membership, assignment, ownership, permission, authority, or affectedness. State
only relations that are current and apply the FPF pattern that defines or constrains each claim.

Use `A.1.SCR` when the System status of a proposed participant or containing whole is unresolved. Use `A.22`
when the current question selects an organization among independently identified constituents and obtaining
relations for a named use. Keep several non-nested structures when one decomposition would hide a relevant
claim—for example, an interaction, control relation, affected System, or source-return condition.

Authority constrains who may change a System; it does not draw the System boundary. Ownership can matter to a
decision without establishing containment. A containing whole matters when its actual or proposed proper-part
relations and whole-level consequences change the use or concept. Distinguish supported actual relations from
proposed relations and qualified predictions; a future whole need not already exist for its proposed
arrangement to affect the concept.

#### SYSE.2:4.3 - Develop the use claim and candidate system concept together

Write one outside-facing use claim and one inside-facing concept claim:

```text
Linked use-and-system concept proposal:
  concrete use claim:
  candidate system-concept claim:
  main uncertainty, if any:
  architecture question exposed:
  reopen condition:
```

Use any readable form for this content. The use claim names participating or affected Systems,
conditions, expected transformations or behavior, and outside effects only as far as the current decision
needs. The system-concept claim names what the proposed concept needs—for example, a boundary, functioning,
interface, resource, constraint, or placement—while leaving full architecture selection open.

When an available construction starts the inquiry, ask who could use it, in what situation, and for what
outside effect. Follow one consequential behaviour path from the triggering change through the participating
Systems to that effect. Try the condition most likely to defeat the proposal. Use the resulting success or
failure to revise the functioning, bearer, interface or use claim that made the difference. Expand the path
only when another condition could change the concept; no complete scenario set is needed for the first link.

Use `A.6.F` when function-like wording carries a claim. Name the required functioning and its proposed bearer.
Any remaining question—for example, about function, capability, Method, Work, module, interface, evidence, or
architecture—stays under the pattern that defines or constrains it. Use `A.6.M` only when a module or interface claim is
current. If no feasible bearer can support required functioning, revise the concept or use claim before
admitting an architecture candidate.

Use `A.3.4` for an actual observed transformation only after the continuing subject, boundaries,
before/during/after facts, and continuity rule are available. A required, intended, or simulated transformation
remains modal claim content; its description does not establish that the change occurred.

A functional or transformation-flow description of relevant environment structure can support the linked
proposal by showing selected functioning or flow relations for a named use. The proposal also states which use situation matters, which Systems participate or are affected, which outside
effect changes the decision, which candidate System concept is being considered, and what remains uncertain.
Model only the environment structure needed by those claims.

#### SYSE.2:4.4 - Compare changes on either side of the boundary

Develop alternatives when changing a different subject would change the engineering answer. Compare, for
example:

- an actual or proposed change to the designated System;
- a change to an external System or operating arrangement;
- a changed interface, placement, or resource relation; or
- coordinated changes on several sides.

Use a compatible `SYSE.8` provider-arrangement account when its supported provider-arrangement claims
or design constraints change the use, candidate System or intended referent, boundary, interfaces, realization
needs, or evidence. Use only the compatible claims named for this use. Without a compatible current
`SYSE.8` account, use a qualified direct source for the needed provider-arrangement claim or record the missing
result and stop only the linked claim it blocks. Either account
may need revision when a shared claim changes; that dependency does not prescribe the order of engineering Work.
Obtain other decision-changing results from the specialist practice that owns them—for example, organization
change, Operations Management, Platform Engineering, Governance, safety, security, ethics, law, or finance. Keep each result claim linked to the
use or concept claim that depends on it.

For example, when source material names a product-service system, digital twin, digital thread, MBSE, PDM, PLM,
eXperience platform, or Multi-D arrangement, recover the actual contribution before using the umbrella term. A
concrete contribution—for example, a maintained model, configuration relation, simulation, observation return,
integration capability, or change decision—can enter the linked proposal through its direct claim. The umbrella
name alone does not decide whether this pattern, architecturing, realization, assurance, or a specialist practice
is the next use.

#### SYSE.2:4.5 - Expand only when another claim can change the candidate

The first result is one linked use claim, one candidate concept claim, and any main uncertainty.
Reuse an adequate scenario or use-case slice as the proposal: retain its compatible use and concept claims and
add only the missing relation, consequence or uncertainty needed for this decision. The progressive-slice
comparison in §11 helps choose when to continue toward implemented, tested behaviour.

Expand
when further content—for example, another use situation, load, failure, participant, affected System, harm,
benefit, or representation—could change the candidate. Add only the relevant:

- environment structures and obtaining relations;
- transformations, interactions, conditions, and effects;
- functioning, interface, placement, resource, and constraint claims;
- correspondence between a representation and the represented claims;
- alternatives, assumptions, evidence limits, and specialist returns.

If source words such as *operational system*, *system in operation*, *operations*, or *operational flow* are
current, distinguish two questions. Use this pattern for a System's participation in use and the concept that
supports it. Use Operations Management when the difficulty is managing continuing Work, queues, policies, or
flows. An operational adjective does not settle that choice.

#### SYSE.2:4.6 - Stop at a grounded architecture question and reopen from failed support

Stop when the current use claim and candidate concept expose a grounded architecture question and any
uncertainty carried into it. The linked proposal supplies required functioning, operating conditions, outside effects,
decision-relevant environment structures, assumptions, and evidence limits to `C.30` and `C.32`.

Use `C.30.ASV` only when a structural description and its adequacy for a selected architecture use are current.
Do not open a full view or architecture-description apparatus merely because a sketch helped the discussion.

Reopen the affected linked claims when:

- the use claim and concept claim no longer support each other;
- a candidate architecture lacks a feasible bearer or hides a harmful effect;
- realization evidence defeats an interface, resource, placement, or capability assumption;
- operating observation changes a condition or effect; or
- a specialist result changes permission, feasibility, harm, value, or the participating Work arrangement.

Return to `SYSE.1` when the failed claim changes the immediate engineering subject or the product and use grounds. Distinguish those returns: a changed local scope can preserve the product SoI.

### SYSE.2:5 - Archetypal Grounding


#### SYSE.2:5.1 - Pumping station under flood risk


In the preceding `SYSE.1` use, the engineer retains the intended referent `PumpingStation-P1` in decision content
and records downstream exposure as unresolved. No actual `PumpingStation-P1` exists yet. The first linked proposal
says:

```text
use claim: the intended referent would move water under the selected flood load without unacceptable downstream harm
system-concept claim: the description assigns pumping, positioning, power, control, and discharge functioning to the intended station referent
main uncertainty: downstream conditions may make the proposed discharge harmful
architecture question: which selected structures and possible bearers could support the claim
```

This is enough to use `C.30` and `C.32`. A component pump test can contribute evidence about an actual bearer,
but it establishes neither the not-yet-present station nor its outside effect. The engineer uses downstream-harm evidence to revise the use claim. The project-system choice reopens only if
the station referent no longer supports the project decision.


#### SYSE.2:5.2 - Manufacturer's ERP-enabled planning change

An available construction starts this concept question: deployed `ERP-Runtime-E3` offers automatic rescheduling
when an order date changes. The manufacturer considers using that facility to revise production commitments.
Its usefulness depends on what the planners would receive and could act on.

The manufacturer keeps `PlanningSystem-P1` as the intended creator being engineered; actual System identity remains unestablished. As in `SYSE.1:5.2`, the product SoIs remain the water-supply and irrigation installations in their intended uses. The planning capability must support their different orders and commitments with shared production resources. Actual person Systems `Planner-A` and `Planner-B` perform `PlanningWork-PW1`.
They use `ERP-Runtime-E3` and demand, capacity, material, and production-order records as resources and evidence.
The records are epistemes; `PlanningAPI-PA2` and the user interface are separately identified interfaces.
The common-focus exchange in `SYSE.1:5.2` has made the missing stock-information contribution visible.

The first linked proposal lets the software reschedule a moved order and release the revised production
commitment. Its use claim is that the planners could promise the earlier date from the resulting plan; its
main assumption is that the runtime's material and capacity information supports that commitment.

Follow the proposed behaviour. When an order needs six units, ten are recorded and actually available, and the
needed capacity is available, the proposed schedule has support for those constraints. Now try a failure path:
the imported record still shows ten unreserved units, but eight have since been allocated elsewhere. The moved
order needs six, while only two remain unreserved. A successful date recalculation leaves the proposed commitment
unsupported. It has exposed a stale-input failure, without establishing that rescheduling itself is useless.

Revise the linked concept. Required functioning becomes proposing a schedule, obtaining current material and
capacity confirmation and any needed reservation, and holding commitment when that support is missing.
One proposed allocation gives `ERP-Runtime-E3` schedule proposal and an explicit unconfirmed state;
`Planner-A` obtains the needed confirmation and reservations, and `Planner-B` makes the commitment decision
under the applicable authority. This changes the bearer proposal from software alone to a coordinated use of
the runtime and people. Their proposed organization still has to satisfy the System criterion for
`PlanningSystem-P1`; a list of participants and records does not establish that composite.

The resulting `C.32` question is which arrangement can support that functioning before the required commitment
time. Use `SYSE.5` to develop and compare event-fed information with reservation interfaces against provisional
software plans with human confirmation and a hold on unsupported commitments. Compare latency, available
contributions and the burden of exceptions as well as normal use. The concept now gives that comparison a
specific function, possible bearers, failure path and uncertainty; it does not select a finished architecture.

If confirmation cannot arrive in time, return to the timing claim or proposed allocation. If the required
stock-control contribution or authority cannot be obtained, hold the commitment relying on it and revisit the
affected concept claims or choice of the immediate engineering subject. Reopen the product SoI designation only when its product or use grounds change; a failed local arrangement or new contract alone does not make the planning creator the SoI.

The independent ERP supplier can select its software product as its own SoI on the usable supply, decision and acceptance grounds in `SYSE.1:5.2`. The manufacturer's planning project can close its agreed capability result through representative order changes and operating conditions. Software installation or an organization chart alone does not establish that capability or the existence of the composite `PlanningSystem-P1`. Its System identity, qualified capability and later product consequences require their respective evidence; local acceptance need not wait for every later product outcome.



#### SYSE.2:5.3 - Occupied building heat-pump control


For `HeatPumpPlant-HP1`, `ControllerConfig-C2`, the next heating season, and `ArchitectureDecision-AD1`, the three
compatible input accounts use the same subject, configuration, use, horizon, evidence window, and receiving
decision:

- the `SYSE.16` use-context account states the `BuildingHeatingSystem-BH1` proper-part claim, energy and
  information transfers, plant-room access permission, and unsupported latency, override, insulation, and
  clearance assumptions;
- the `SYSE.17` affected-system account supplies the qualified `AcousticResult-AR4`, `SafetyResult-SR7`,
  `ThermalResult-TR5`, and their authority boundaries, including the unmeasured neighbour-noise and cabinet-
  clearance branches; and
- the `SYSE.8` provider-arrangement account supplies only the supported provider claims and design constraints:
  actual provider System `MaintenanceTeam-MT4`, the current access permission, expected diagnostic Work, the
  communications bearer, and the missing commitment and authority result for remote monitoring.

The three accounts change the linked proposal as follows:

```text
use claim: occupied rooms remain within the selected thermal range while qualified neighbour-noise and maintenance-access constraints hold
system-concept claim: ControllerConfig-C2 includes a cycle-rate limit, a low-noise branch, a measurable cabinet-location alternative, and a latency-tested override-safe branch
main uncertainty: night acoustic measurement and plant-room clearance are unavailable; remote-monitoring authority and commitment are unresolved
architecture question: which controller, sensor, cabinet, communications, and operating structures support those qualified claims
reopen condition: a specialist result, measurement, provider result, or operating observation defeats one of the linked claims
```

The remote-monitoring branch remains conditional because the provider-authority and commitment result is
unavailable. Realization and WorkPlan descriptions may include cabinet relocation, access preparation, and test
Work. Keep those realization and WorkPlan descriptions distinct from the System concept. If no feasible architecture supports the linked claims, revise this proposal. Reopen `SYSE.1` only if the
failure changes the project focus itself.

### SYSE.2:6 - Biases to Watch

Two recurring biases matter here. **Representation lock-in** treats a familiar use-model form as the use itself;
recover the represented Systems, relations, conditions, and effects. **Concept lock-in** narrows use until the
preferred concept always succeeds; keep the use claim revisable and return evidence to the claims it calls into question.

### SYSE.2:7 - Conformance Checklist

| ID | Requirement |
| --- | --- |
| `CC-SYSE2-1` | A conforming use SHALL name one concrete use situation, one candidate system-concept claim, and any main uncertainty before requesting fuller documentation. |
| `CC-SYSE2-2` | It SHALL name the participating and affected subjects and SHALL state each decision-changing relation through the applicable FPF pattern. |
| `CC-SYSE2-3` | It SHALL distinguish parthood, placement, interaction, use, ownership, authority, and affectedness when more than one is current. |
| `CC-SYSE2-4` | Function-like wording SHALL identify the required functioning and proposed bearer through `A.6.F` before architecture use relies on it. |
| `CC-SYSE2-5` | Required or intended transformations SHALL remain modal claims; an actual transformation claim SHALL satisfy `A.3.4`. |
| `CC-SYSE2-6` | A ConOps, use case, scenario, requirement, model, diagram, or other representation SHALL remain distinct from the linked claims it presents. |
| `CC-SYSE2-7` | Conditional expansion SHALL add only information that can change the current concept, architecture question, evidence use, or return. |
| `CC-SYSE2-8` | The stop SHALL expose a grounded `C.30` or `C.32` question and any uncertainty carried into it. |
| `CC-SYSE2-9` | When architecture, realization, observation, or specialist evidence challenges a claim, that evidence SHALL return to the use, concept, or project-focus claims it can change. |

### SYSE.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Working symptom | Repair |
| --- | --- | --- |
| Environment-as-container | One box called environment, owner, or suprasystem is assumed to contain every relevant System. | Name the participating and affected Systems and the direct relation by which each changes the decision. |
| Representation lock-in | A ConOps, use-case, SysML, FAS, requirements, or story format is required before the working question is known. | Start from one linked claim and choose representations only for the use they improve. |
| Concept-as-finished-architecture | An internal concept diagram is treated as the selected architecture and other structures disappear. | Stop this pattern at the grounded architecture question; use `C.30` and `C.32` for architecture relations, selected structures, and candidates. |
| Fixed outside world | External Systems and Work arrangements are treated as fixed while only the designated System or its intended design may change. | Compare actual or proposed changes to the designated System, an external System, their relations, or several subjects; obtain specialist results where needed. |
| Test-as-benefit | One component or integration test is used as proof of outside use, benefit, acceptance, or complete assurance. | State which claim the evidence can support, its conditions, and which use or concept claim remains open. |

### SYSE.2:9 - Consequences

The project can ask architecture questions from a concrete outside-use basis without waiting for a complete
requirements package. It can compare changes across the assumed boundary, preserve non-nested environment
structures, and return evidence to the claim it can actually change.

The cost is ongoing concept maintenance. A use claim, System concept and representation can diverge as new
evidence arrives. Keeping their relations usable takes maintenance; an obsolete description can otherwise be
used as though it still describes the current use or architecture.

### SYSE.2:10 - Rationale

A System concept becomes useful to an engineering decision through concrete relations with other Systems and
conditions, while a chosen containing whole or representation can omit a consequential relation. Linking
use and System concepts makes the outside reason and inside proposal inspectable while leaving architecture
selection to the applicable FPF patterns.

The link is intentionally small. One use claim, one concept claim, and one uncertainty can already reveal a
missing bearer, harmful effect, or misplaced boundary. Fuller descriptions are justified by decisions they can
change, not by a prescribed documentation sequence.

### SYSE.2:11 - SoTA-Echoing

The practice question is how much use description is needed to change the concept or expose the next
architecture question. The selected approach develops a small linked proposal with progressive behavioural
detail. Existing scenarios and slices can supply that content directly.


| Current practice line | What changes in this pattern | Source and use | Adoption status |
| --- | --- | --- | --- |
| Current use-case practice starts from user goals, admits human and nonhuman participants and failure paths, and revises end-to-end slices as work proceeds. Model-based system-architecture practice connects use cases to candidate functional groupings and interfaces. | The Solution starts with a concrete use situation and keeps success, failure, participants, behavior, and the system-concept claim connected while both change. | Jacobson et al., *Use-Case 3.0: The Definitive Guide — Refreshed* (2024); Weilkiens et al., *Model-Based System Architecture*, 2nd ed. (2022). These are provider and textbook Methods, not comparative proof of one universal sequence. | **Adopt and adapt.** Use revisable slices and explicit links to candidate functioning; choose the representation form for the receiving engineering decision. |
| Agile and continuing requirements research treats models, requirements, traceability, monitoring, and compliance links as maintained parts of changing work rather than one frozen preliminary package. | The linked proposal stays revisable, and representations are chosen for the decision and maintained only while they continue to carry useful claims. | Liebel and Knauss, [*Aspects of modelling requirements in very-large agile systems engineering*](https://doi.org/10.1016/j.jss.2023.111628) (2023; [author preprint](https://arxiv.org/abs/2209.01993)), report one Ericsson case, including model-maintenance and tool trade-offs. [SYSE.19:11](40-syse-19---revalidate-engineering-decisions-when-a-relied-on.md#syse1911---sota-and-source-use) gives the distinct source scopes and references for Hernández, Moros and Nicolás (2023), Norheim et al. (2024), and Kosenkov et al. (2025): DevOps requirements management, LLM requirements tasks, and regulatory compliance. | **Adapt.** Maintain useful claims and choose representations by use; let the receiving project determine how requirements Work is organized. |
| Product-service system and servitization research treats useful offerings as configurations of products, service Work, provider and customer relations, capabilities, operations, digital support, and consequences. Reported performance is mixed and configuration-dependent. | The Solution compares actual or proposed changes to the designated System, external Systems, interfaces, and Work arrangements and asks for the specialist results that make those alternatives credible. | [Brambila-Macias, Sakao and Kowalkowski (2018)](https://doi.org/10.1017/dsj.2018.3), [Braga Junior, de Toledo and González (2020)](https://doi.org/10.4322/pmd.2019.017), [Kim (2020)](https://doi.org/10.1017/dsj.2019.30), [Brax et al. (2021)](https://doi.org/10.1108/IJOPM-08-2020-0535), [Åkesson et al. (2024)](https://doi.org/10.1108/JMTM-11-2021-0457), [Menon et al. (2024)](https://doi.org/10.1016/j.jclepro.2024.142459), and [Zhao et al. (2025)](https://doi.org/10.1016/j.jclepro.2025.146690). [SYSE.8:11](29-syse-8---develop-an-integrated-offering-and-provider-concept.md#syse811---sota-echoing) develops the bounded offering/provider comparison. | **Adapt.** Use the cross-boundary design pressure; establish each System, Work, provider relation, Method, and consequence directly in the receiving project. |

A serious alternative is a progressive use-case slice following the
[Use-Case 3.0 guide](https://www.ivarjacobson.com/files/use-case_3.0_v1.0.pdf). It starts with a user goal and can
grow from a sketch through selected normal and failure paths toward a testable increment. It need not enumerate
all scenarios before useful work starts.

Compare the two on the same moved-order facts in §5.2, including the stale stock record. A small slice for
rescheduling an order can already reveal the unsupported commitment and supply a failure path that holds it.
The linked proposal should reveal the same failure. Its selected next result is the architecture question:
which functioning, people, runtime and interfaces could support a commitment under the stated conditions?
An adequate slice can already supply those claims; use them without a second description.

The trade-off depends on the next result. This linked proposal leaves implementation and path-specific
acceptance tests unprovided while the bearer and interface choices remain open. Progressive slice practice
supplies the route toward implemented, tested behaviour when that is needed. Neither representation earns a
general effort advantage from being called small. In the ERP case, the proposed confirmation and reservation
arrangements still need comparison, so §§4.3–4.6 return the functional and bearer question to `C.32` and
`SYSE.5`; a later testable slice can use that result.

Reopen the choice of a thin linked proposal when it appears coherent but a consequential path changes the
functioning or bearer—for example, when another order consumes the promised stock between proposal and
commitment. Add the missing path or use the progressive slice directly. Prefer an available scenario treatment
when it supplies the required architecture claims with less reconstruction or maintenance. These are selection
conditions, not evidence that one description form has superior project outcomes.

These current lines support continuing, use-led, model-linked revision within their stated domains. This pattern connects a use situation, subjects and relations, qualified consequences and a candidate concept, using compatible SYSE.16, SYSE.17 and SYSE.8 results. Relate evidence to the claim it can change. Apply each source within its stated domain and assess cross-domain transfer against the receiving use, Systems, relations and evidence.

### SYSE.2:12 - Relations

- A `SYSE.1` account can supply the immediate engineering subject, its relation to the product SoI, current reason, boundary question, alternatives and reopening condition. Use the subject of the present concept question; developing a creator's concept retains the product grounds. Return a changed local subject or product purpose to the corresponding choice.
- A compatible `SYSE.16` result supplies selected operational structures, conditions, and unsupported
  assumptions; a compatible `SYSE.17` result supplies qualified consequence claims and unresolved representation
  or protection needs; a compatible `SYSE.8` account supplies only its supported provider-arrangement claims and
  design constraints. Use each result only for a compatible subject, configuration, use, horizon, evidence
  window, and decision. These relations do not prescribe an order of engineering Work.
- Use `A.3.4` for the identity and boundary test of an actual bounded transformation. Intended, required, and
  simulated transformations remain claims or representations until that test applies.
- Use `A.6.F` to recover the object or claim meant by function-like wording and select the direct subject
  pattern. Use `A.6.M` only when a module or interface claim is current.
- Use `A.22` for selected-structure identity in decision-relevant environment structures. Use `C.30.ASV` for
  structural-view adequacy only when a description is relied on for a selected architecture use.
- The linked use-and-system concept proposal supplies functioning, operating conditions, outside effects,
  selected environment structures, assumptions, and evidence limits to the architecture question. `C.30`
  defines grounded architecture claims and relations; `C.32` guides candidate synthesis over selected
  structures. `SYSE.5` develops the engineering functional and bearer alternatives, their allocations,
  interfaces and feasibility limits from those compatible claims.
- Architecture, realization, operation, or assurance evidence returns to the affected linked claims it can
  change. Practitioners in organization change, Operations Management, Platform Engineering, Governance, safety,
  security, ethics, law, finance, and other specialist practices keep their Methods and supply only the results
  used in the linked proposal.

### SYSE.2:End
