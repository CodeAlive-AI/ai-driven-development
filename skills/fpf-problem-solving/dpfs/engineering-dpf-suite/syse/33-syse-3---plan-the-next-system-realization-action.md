## SYSE.3 - Plan the Next System-Realization Action (Recursive Realization Network)

> **Status:** Stable

### SYSE.3:0 - Use This When

Use this pattern when a grounded engineering architecture candidate or decision exists, but one realization
branch is unsupported: the capable System, Method or enabling condition needed to produce or change the
engineered System remains unresolved.

Name that branch, its proposed transformer System or the need to find one, the missing support and one next
planned action. Expand only when interacting branches or building the builder changes that action; name the
earlier answer to revisit if the branch proves infeasible.

The result is a provisional realization-network description and a distinct WorkPlan. Performed Work, actual
change, feasibility and an obtaining network require their own evidence. If the architecture or function
bearer is still open, return to the architecture patterns. If the question concerns production, capability,
operations, organization, configuration or assurance beyond this first action, use the specialist return in :4.6.

#### SYSE.3:0.1 - Terms and Distinctions

| Cue | Meaning used here |
| --- | --- |
| realization | Actual or intended Work and transformations by which an engineered System or configuration can be produced or changed. |
| realization-network description | A project episteme describing proposed transformations, participating Systems, result dependencies and gaps. It is distinct from the world-side network whose recognition conditions appear in :4.4. |
| build the builder | A recursive branch in which Work changes or produces a System, capability, Method support, tool or platform needed by later realization Work. |

### SYSE.3:1 - Problem frame

An architecture can name suitable bearers for required functioning while fabrication, adaptation, integration,
configuration, installation or qualification remains unsupported. A product tree, WBS, schedule or toolchain
diagram can then look like a realization argument. Engineers may plan Work for a System that does not exist,
assign it to a label with no capable holder, or discover late that a selected interface, material or access
condition cannot be realized.

The useful gain is a bounded feasibility question: identify the first unsupported dependency, plan an attainable
action and use its result to revise only the affected earlier answer. The pump case in :5.1 shows how an inquiry
into a supplier and fixture can precede fabrication without expanding into a complete production-network plan.

Use this pattern after the architecture has at least one candidate bearer for every required functioning at
issue. Otherwise keep the architecture question open with `A.6.F`, `C.30` and `C.32`. Use `A.3.4` for an actual
bounded change, the A.15 family for Work and production claims, and `E.18` or `E.18.NET` only when their
selected-structure conditions are met. Use Operations Management or project-portfolio practice when the live
question is queue, capacity, priority or shared-resource coordination.

When a source names a builder or enabling means—for example, a *manufacturer*, *platform* or *toolchain*—recover
the System and its contribution to the current branch. Establish assignment, capability, Method, Work order and enabling
relations separately under :4.2–4.6. Use the local `TransformerSystemRole` when that contribution needs the
distinction; a source label alone supplies none of those claims.

### SYSE.3:2 - Problem

An architecture candidate proposes an organization of the System, but it does not make that organization
exist. For example, a selected module, interface, placement, control relation, or configuration may depend on
changes to pre-existing materials and Systems, first constitution of new Systems, integration Work, and Systems capable
of performing that Work. Those transformer Systems can themselves need new capabilities, tools, Methods,
resources, configuration, or prior change.

A single decomposition rarely exposes all of these dependencies. A component tree follows the proposed
System; a WBS follows intended Work; an organization chart follows one organization; a platform inventory or
diagram follows selected technical means. Those decompositions alone do not establish which actual Systems
can perform the needed Work under the stated conditions. Connect the descriptions while keeping architecture,
intended change, transformer capability, WorkPlan, performed Work and evidence distinct.

### SYSE.3:3 - Forces

| Force | Tension |
| --- | --- |
| Architecture intent and physical feasibility | Selected structures guide realization, while their candidate or decided status does not make them actual. |
| Backward dependency and forward Work | Reasoning backward reveals missing support, while actual Work and change proceed through their own facts and may follow another order. |
| Useful recursion and endless decomposition | A missing transformer capability can open another realization branch, while a bounded next-action question may need only the first unsupported branch. |
| Readable provisional description and typed relations | A provisional realization-network description makes dependencies visible, while an actual `E.18.NET` selection requires independently identified members, obtaining relations, and endpoint bindings. |
| Shared platforms and local conditions | A platform can enable several branches, while its name does not establish availability, fit, capability, or one universal pipeline. |
| Project focus and specialist depth | Systems Engineering must keep the whole realization question connected, while specialist practices retain their Methods and decisions. |
| Plan stability and revision from feasibility evidence | A WorkPlan coordinates the next action, while new evidence can revise the branch, architecture candidate, system concept, or project focus. |

### SYSE.3:4 - Solution

#### SYSE.3:4.1 - Start from one named architecture result

Start with one current architecture result for one described holon:

1. the current `C.30` architecture question and claim;
2. one `C.32` candidate configuration or one `C.32.PAD` project architecture decision;
3. the selected structures, constraints, assumptions, and expected architecture gain that matter to
   realization; and
4. the next use for which feasibility must be known.

The input may remain modal. A candidate structure is not an obtaining `ArchitectureRelation`, and a project
decision does not make the decided structure actual. Keep the architecture result and the realization account
as separate claims. When provider capability, continuing provision, access, custody, responsibility, or recovery
can change realization, use only the supported claims and design constraints from a compatible `SYSE.8`
provider-arrangement account for the same subject, configuration, use, horizon, decision, and evidence window.
Without a compatible current account, use a qualified direct source for the claim needed by this branch or
record the missing result. The account supplies supported provider claims and design constraints. Establish the
provider arrangement, provider Systems, performed Work, responsibility, and authority separately when the branch
uses them.

Check the architecture boundary before proceeding. If the candidate lacks a bearer for required functioning,
reopen the bearer question under `A.6.F` and `C.32`. Continue here when the candidate has a proposed functional and
structural answer but the Systems and Work needed to constitute, change, integrate, or qualify it remain
uncertain.

#### SYSE.3:4.2 - Describe one realization branch

Write one branch in ordinary language. Include only the distinctions that change the feasibility question:

- the architecture result to be realized;
- the pre-existing System, material, assembly, description, or other referent that would be changed, or the
  identity and completion conditions for a System that does not yet exist;
- the intended change, production result, interface state, integration state, or configuration relation;
- the proposed transformer System or unresolved need for one and the local `TransformerSystemRole` condition
  it would meet for this Work;
- the needed Method, capability envelope, resource, tool or platform contribution, access condition, interface,
  integration, and configuration relation; and
- the fact or specialist result that would make the branch usable, require its repair, or reopen an earlier answer.

Keep modal and actual claims apart. An intended change belongs in a plan or description until an actual
continuing referent, boundary, conditions, and before/during/after facts satisfy `A.3.4`. When the proposed
System does not yet exist, describe changes to pre-existing materials or assemblies and use `A.15.PROD` later
for independently grounded identity inception and production completion. Do not describe transformation of a
future System before it exists.

The claim that a candidate transformer will perform the Work is also modal. Name the candidate holder System,
or the unresolved need for one, and the local `TransformerSystemRole` condition in the WorkPlan. Use `A.2.1` only when an assignment occurrence actually obtains, and use `A.2.2` only when the
holder's capability has a recoverable Work family, envelope, measures, qualification window, and currentness
condition. Treat a job title, supplier category, tool list, past success, or Method description as possible
evidence inputs; establish the capability claim through its Work family, envelope, measures, qualification
window, and currentness.

#### SYSE.3:4.3 - Find the first unsupported answer

Use the `A.1.STM` long mantra to keep the architecture result, intended outside use, and builder dependencies in
attention. Read the logical dependency backward and find the first unsupported answer that prevents one credible
next realization action. *First* means logically first for this dependency, not earliest in a calendar or
prescribed process.
Use these six working questions to classify the first gap:

| Working question | Result or next practice that resolves the gap |
| --- | --- |
| Which existing System could perform the intended Work? | Name a candidate transformer System and role condition, or use the System-recognition or specialist-search Method that can supply one. |
| Can that System perform the Work under the required conditions? | State the missing `A.2.2` capability claim, threshold, envelope, qualification, or currentness result. |
| Which Method and means make the intended result plausible? | Name the Method question and the missing resource, tool, access condition, or platform contribution. |
| Can the selected structures be constituted and connected? | Name the missing interface, integration, configuration, placement, or production-feasibility result. |
| Which prior change makes the transformer or means available? | Open one recursive realization branch for that System, capability, Method, tool, or platform contribution. |
| Does the proposed architecture still have an admissible realization? | If no branch remains, name the `C.32` candidate, architecture decision, or linked use-and-system concept that the failure requires the practitioner to reopen. |

Record the first gap even when later gaps are already suspected. Use it to choose the next action.

#### SYSE.3:4.4 - Recurse only when the next action depends on it

Open another branch when the current transformer System, capability, Method, tool, or platform contribution
must itself be brought about or changed before the current branch can proceed. Apply the same questions to that
branch. Do not introduce fixed builder levels: a transformer System can serve several branches or projects,
and evidence from a later branch can change an earlier branch claim.

When several branches must be considered together, begin with a Plain provisional realization-network
description. Name the proposed members and the missing cross-branch relation or binding. Use `E.18` only for one
selected transformation-flow structure whose identity is established. Use `E.18.NET` only after at least two
independent member structures, the obtaining cross-flow relation occurrences, the endpoint bindings,
applied constraints, and the current use frame are recoverable. Until then, the episteme describes a proposed
realization network; it is not the selected network itself.
When a cross-branch arrow uses a generic cue—for example *creates*, *builds*, *uses*, *supplies*, or *depends
on*—replace it with the actual production, participation, use, evidence, integration, configuration, supply, or
other relation through the pattern that defines it. If the relation kind or case facts are not yet available, keep the dependency as a
provisional claim and name what must be established.

When a formal flow description uses `DesignRunTag`, keep each tag local to one leaf-position binding under
`E.18`/`E.18.NET`. Represent wider dependencies and Work order through the direct relations that establish them.

#### SYSE.3:4.5 - Plan the next Work separately

Create or amend one `A.15.2` WorkPlan after the first unsupported answer is visible. For one bounded next action,
a WorkPlan can start with one substantive PlanItem that states:

- the present EntityOfConcern and planning horizon;
- the intended Work or investigation;
- the candidate performer System and local SystemRole-kind conditions;
- the Method, capability threshold, resources, tools, access, and dependencies needed for that Work; and
- the result or evidence that will update the branch or reopen an earlier answer.

The next Work can take different forms—for example, investigating a supplier, qualifying a capability,
developing a fixture, changing a transformer System, obtaining a specialist result, integrating a bounded slice,
or revising the architecture candidate. Select the
action that resolves the first unsupported answer; do not schedule every visible branch.

The WorkPlan states intended Work and its conditions. Establish every later assignment, capability, resource
availability, relation, Work occurrence, transformation, and result through its direct evidence and pattern. When Work is later performed, use `A.13` for its actual performer and `A.15.1` for independent Work admission,
`F.6` when precise assignment-bound attribution is needed, `A.3.4` for actual changes, and `A.15.PROD` for
production, identity-inception, or completion claims. Compare the resulting facts with the plan only when that separate question is current.

#### SYSE.3:4.6 - Obtain specialist results without absorbing their Methods

Keep the realization branch connected while leaving specialist decisions with the practice that can make
them. Examples include:


| Current gap | Result needed here | Practice that keeps the detailed Method |
| --- | --- | --- |
| A shared tool or platform cannot yet support the Work | capability, availability, interface, configuration, or change result for the named platform System | Platform Engineering or the applicable domain engineering practice |
| A transformer organization lacks a suitable structure, assignment, authority, or coordination relation | a named organizational or authority result and its conditions | Organization Engineering, Systems Management, Governance, or the applicable authority practice |
| Several projects contend for a transformer or resource | the direct interdependency, capacity, timing, or priority result used by this branch | Operations Management or project-portfolio practice |
| A configuration or integration relation is unresolved | the configuration identification, compatibility, change, integration, or release result needed by the branch | configuration or integration practice for that domain |
| A capability or use claim needs a challenge | the claim-bound evidence and reliance result | `SYSE.4` and the applicable assurance or specialist practice |

Name the contribution that an enabling arrangement actually makes. For example, identify the bounded contribution
of a platform, team, supplier, administrative service, or configuration repository. When no maintained receiving
pattern exists, retain the unresolved specialist need and the decision it blocks.

#### SYSE.3:4.7 - Stop at one actionable gap and name the affected earlier answer

The project-local result is a `RecursiveRealizationArrangementResult@Project`, a `U.Episteme` containing a
provisional realization-network description plus a distinct `U.WorkPlan`. It identifies the unsupported branch,
proposed transformer and enabling Systems, gaps, result dependencies and the earlier answers each gap can reopen.
The first result can be stated in five lines:

1. **Architecture input:** the named candidate or decision and the selected structures at issue.
2. **Unsupported branch:** the intended result or change whose realization is not yet supported.
3. **Missing support:** the proposed transformer System or unresolved need for one and the capability,
   Method, resource, platform contribution, interface, integration, or configuration result still needed.
4. **Next Work:** one WorkPlan item that can resolve that gap.
5. **Affected earlier answer:** the branch, architecture answer, linked concept, or project-focus claim to reopen if the result defeats it.

Stop when these five lines make the next action and affected earlier answer clear. Expand only when interacting branches or
build-the-builder recursion changes that next action.

Reuse the branch description and distinct WorkPlan already supplied by an implementation-preparation account
when they identify the unsupported branch, the attainable next action and the earlier answer that adverse
evidence would reopen. Add only a missing decision or relation. The five lines above are a way to expose that reasoning, not a second
required record. When the next decision concerns readiness to make, buy or reuse the product, use the applicable
implementation Method and its wider readiness conditions; this first-gap result does not discharge them.
The comparison in :11.1 works this choice through the pump case.

When feasibility evidence arrives, update the branch description and WorkPlan. If one branch fails but another
admissible branch remains, repair or replace that branch. If no admissible realization remains, reopen the
architecture candidate or decision. Reassess the linked use-and-system concept under `SYSE.2` only when its use or concept claim must change,
and reassess the choice account under `SYSE.1` when its immediate engineering subject or product-use grounds must change. A revised local scope does not by itself change the product SoI. Cost already incurred supplies no
reason to preserve an unsupported answer.

### SYSE.3:5 - Archetypal Grounding


#### SYSE.3:5.1 - Pumping station under flood risk


`FloodPumpStation-7 : U.System` exists at configuration `FPS7-C18`. `SYSE.2` supplies a compatible station
concept for changing that station so it can move water under the selected flood load without unacceptable
downstream harm. `StationArchitectureDecision-7`, a compatible `SYSE.6` result, selects
`StationArchitectureCandidate-7` with a changed discharge assembly, interfaces, placement, and control
relations. The architecture has proposed bearers for the required station functioning; the open question is how
to realize the changed assembly. `Station7ProviderArrangementAccount-R1`, a compatible `SYSE.8` result, supplies
only current provider, access, custody, and recovery claims that bear on the supplier branch. It establishes no
supplier capability, assignment, Work, or production result.
The first use produces this filled five-line result:

1. **Architecture input:** `StationArchitectureCandidate-7`, including the selected discharge interface,
   placement, material, geometry, and tolerance claims.
2. **Unsupported branch:** `ManifoldRealizationBranch-1`; a pre-existing discharge-manifold blank must be
   changed, and a newly constituted mounted subassembly must satisfy those claims.
3. **Missing support:** `SupplierWeldCell-4` is the candidate transformer System for later welding Work. The
   branch still needs a capability result for the selected material and geometry and a feasible positioning
   fixture.
4. **Next Work:** the WorkPlan contains `FixtureAndSupplierFeasibilityInvestigation-1`. Its intended performer
   is `StationRealizationEngineeringTeam-2`, not the supplier weld cell whose later production capability is
   being investigated.
5. **Affected earlier answer:** if no fixture-and-weld branch meets the selected interface and access conditions,
   reopen the `C.32` comparison of interface, material, module split, and placement alternatives.

For this case, the PlanItem records the following intended Work and conditions:

| PlanItem part | Pump case value |
| --- | --- |
| Present EntityOfConcern and horizon | The one present EntityOfConcern is the already identified architecture-candidate episteme `StationArchitectureCandidate-7`. `ManifoldRealizationBranch-1` remains PlanItem content about the unsupported branch. The case-local supplier-feasibility window is 2026-09-07 through 2026-09-18, before the next discharge-interface choice. |
| Intended Work | Compare feasible fixture and welding arrangements for the selected manifold material, geometry, tolerance, access, and interface conditions. |
| Intended performer and local role condition | The already admitted System `StationRealizationEngineeringTeam-2` is the intended performer. The plan requires a positive classification judgment under local `FixtureAndSupplierFeasibilityInvestigatorSystemRole`, constituted in `StationRealizationFeasibilityPractice-2026` by the assignable contribution of comparing fixture-and-weld branches and producing `FixtureAndWeldFeasibilityAccount-1`. This investigation-facing condition is distinct from `SupplierWeldCell-4` as the candidate transformer System for later welding Work. The plan establishes neither the classification judgment nor an assignment occurrence. |
| Method, capability, resources, and dependencies | The plan names `FixtureAndSupplierFeasibilityMethod-v2`; requires a current capability-fit result for the engineering team before Work entry; and supplies the architecture candidate, manifold material and geometry claims, access conditions, supplier capability statements, and their evidence references as inputs. These planned conditions establish no capability or resource availability. |
| Planned result and affected earlier answer | The intended result is `FixtureAndWeldFeasibilityAccount-1`, which identifies a supported fixture-and-supplier branch or names the failed interface, material, module, or placement assumption that requires renewed `C.32` comparison. |

`Station7RecursiveRealizationArrangement-R1 : U.Episteme` is the case result. Its EntityOfConcern is
`StationArchitectureDecision-7` for the bounded station-realization question. It cites the provisional
realization-network description and the distinct WorkPlan, names `ManifoldRealizationBranch-1` as the first
unsupported branch, records the proposed transformer and enabling Systems, and names the earlier architecture claim that the
fixture-and-weld gap can reopen. It establishes neither an obtaining realization network nor performed Work.

If the fixture itself must be developed, that need opens one recursive branch for a toolmaking System and its
capability. The engineer stops there unless this branch changes the immediate investigation. If no admissible
weld or fixture branch remains, the engineer reopens the `C.32` comparison of interface, material, module split,
and placement alternatives. The engineer reassesses the linked station concept under `SYSE.2` only if the concept or outside-use claim must change.
The fixture does not become part of the pump merely because realization needs it.


#### SYSE.3:5.2 - Manufacturer's ERP-enabled planning change


The architecture candidate concerns one deployed production-planning System. It names the software bearer,
interfaces to order and shop-floor Systems, selected data and decision relations, and the planning functions
that those Systems are expected to support.

The first unsupported branch is the change from current product, order, and resource descriptions to the
configuration and integration state required by the candidate. `PlanningIntegrationTeam-2` is the candidate
transformer System for `RepresentativePlanningDataIntegrationWork-1`: mapping one representative data family
and configuring its source-to-planning interface. The planned holder-dependent capability requirement is the
ability of that team to apply `BoundedPlanningDataMappingMethod-v1` under the actual source semantics, access,
timing, and configuration conditions. This is WorkPlan content until `A.2.2` supplies a current capability
result and `A.2.1` supplies an assignment occurrence when one is needed.

`MigrationToolService-3` is a separate proposed tool or service contribution to that Work: access to a named
mapping-execution interface under the selected configuration. This case attributes no transformer assignment
or data-mapping capability to that service label. If a later claim relies on it as an acting System, the
engineer applies System recognition before making separate claims about its role, capability, and Work. The
immediate WorkPlan item names `PlanningIntegrationTeam-2` as intended performer of the representative-slice
feasibility investigation and asks for `RepresentativeIntegrationFeasibilityAccount-1` plus any organization-
design result needed to make the slice feasible.

If the gap concerns who may change source definitions, which organization holds an assignment, or which
authority relation applies, the engineer obtains that result from Organization Engineering or Governance
rather than encoding it as a technical interface. If the branch cannot preserve the required decision timing
or data meaning, the engineer reopens the `C.32` comparison of interface, placement, and responsibility
structures. The engineer reassesses the linked planning concept under `SYSE.2` only when the planning-use claim must change.


#### SYSE.3:5.3 - Occupied building retrofit


`SYSE.2` supplies the continuing building, the occupied-use claim, and a candidate concept through the occupied
region, safe-entry, egress, and essential-service interfaces. `C.30` and `C.32` supply candidate building zones,
service paths, interfaces, and load-bearing relations. Temporary access, work-area isolation, and construction
sequencing remain realization and WorkPlan questions.

The first unsupported branch is how a contractor System can reach and change the selected building region
while the occupied-use boundary and essential services remain supported. The candidate transformer System is
one contractor team. Access-equipment Systems remain separate resources or participating Systems unless their
relation to the team is independently established. The missing support is a capability claim under the occupied
configuration, access, isolation, load, and service-continuity conditions. The first WorkPlan item is a
contractor-capability and temporary-access investigation for those conditions.

If no admissible access arrangement remains, the engineer reopens the `C.32` comparison of zones, service
paths, placement, and interfaces. The engineer reassesses the linked occupied-use concept under `SYSE.2` if continuing occupancy or the use boundary must change. A
construction sequence is plan content; it is not the building concept, the changed building, or evidence that
the Work has occurred.

### SYSE.3:6 - Biases to Watch

Two recurring biases matter here. **Diagram-made feasibility** treats a product tree, schedule, or toolchain
description as proof that capable transformers and relations obtain; return to the first unsupported branch.
**Endless builder recursion** expands every dependency before choosing useful Work; recurse only when the added
branch changes the next action.

### SYSE.3:7 - Conformance Checklist

| ID | Requirement |
| --- | --- |
| `CC-SYSE3-1` | A conforming use SHALL start from one named `C.30`/`C.32` architecture candidate or decision and SHALL state the selected structures and use for which realization feasibility matters. |
| `CC-SYSE3-2` | If required functioning has no candidate bearer, the practitioner SHALL reopen the bearer question under `A.6.F` and `C.32` rather than treating the missing architecture answer as realization Work. |
| `CC-SYSE3-3` | The first result SHALL name one unsupported realization branch, the proposed transformer System or unresolved need for one, the missing enabling condition, one next WorkPlan item, and the earlier answer to reopen if it fails. |
| `CC-SYSE3-4` | Intended change SHALL remain modal; an actual transformation claim SHALL satisfy `A.3.4`, and a not-yet-existing System SHALL use production and identity-inception claims rather than a fictional prior transformation. |
| `CC-SYSE3-5` | A proposed transformer-role assignment and capability SHALL remain plan or candidate content until `A.2.1` and `A.2.2` supply their direct results. |
| `CC-SYSE3-6` | The realization description and `A.15.2` WorkPlan SHALL remain different epistemes; neither SHALL be treated as performed Work, actual change, production, or an actual selected network. |
| `CC-SYSE3-7` | Recursion SHALL be added only when realizing a transformer System, capability, Method, tool, resource, or platform contribution changes the next action. |
| `CC-SYSE3-8` | `E.18` and `E.18.NET` SHALL be used only after their member, relation, constraint, endpoint-binding, and use-frame conditions are met; otherwise the result SHALL remain a Plain provisional realization-network description. |
| `CC-SYSE3-9` | Platform, organization, operations, portfolio, configuration, integration, authority, and assurance questions SHALL retain their specialist Methods and supply named results to this branch. |
| `CC-SYSE3-10` | A branch failure SHALL reopen only the affected architecture, concept, use or project-focus claims; a local failure SHALL not reopen every earlier answer. |
| `CC-SYSE3-11` | `DesignRunTag` and flow valuation SHALL remain local to their leaf bindings; the result SHALL establish no global stage or lifecycle order. |

### SYSE.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Working symptom | Repair |
| --- | --- | --- |
| Architecture realizes itself | A selected module or interface is treated as evidence that it can be produced, changed, integrated, or qualified. | Name one realization branch, transformer System, enabling condition, and the earlier claim to reopen if feasibility fails. |
| WBS as realization network | Work packages or schedule rows stand in for changed referents, transformer Systems, capabilities, and relations. | Keep the WorkPlan as intended Work and describe the realization dependency separately. |
| Transformation before existence | A future pump assembly, software deployment, or building configuration is said to change before it exists. | Name changes to pre-existing referents and use `A.15.PROD` for later identity inception and completion. |
| Creator hierarchy | Fixed developer, builder, producer, and operator levels replace case-specific transformer roles and recursive dependencies. | Recurse from the first unsupported branch without fixed levels; admit each System and assignment separately. |
| Universal platform pipeline | One toolchain or internal platform is prescribed for every engineered System. | Treat the named platform System and its capability, interface, availability, and change contribution as one possible branch. |
| Diagram-made network | Arrows labelled *builds*, *uses*, or *depends on* are treated as an actual `E.18.NET` structure. | Keep a provisional realization-network description until the member structures, obtaining cross-flow relations, endpoint bindings, constraints, and use frame are established. |
| Specialist absorption | Systems Engineering silently chooses organization structure, resource priority, configuration policy, safety argument, or platform Method. | Obtain the specialist result needed by the branch and keep its Method and decision with the specialist practice. |
| Restart every earlier decision | Any failed fixture, interface, or supplier result reopens project focus and all earlier decisions. | Reopen only the branch or architecture claims that the result changes; reopen a wider decision only when that answer also fails. |

### SYSE.3:9 - Consequences

Engineering participants can plan the next realization action without first planning every dependent branch.
One unsupported branch becomes visible together with the System and Work needed to resolve it. Recursive
build-the-builder dependencies can be added where they change the next action, while architecture candidates
remain open to repair.

The cost is explicit incompleteness. A provisional realization-network description can contain unresolved
Systems, capabilities, Methods, relations, and specialist needs. Maintaining the distinction between that
episteme, a WorkPlan, and actual Work takes care, but it prevents planned or drawn dependencies from being
mistaken for physical feasibility.

### SYSE.3:10 - Rationale

Systems Engineering connects a proposed System to the Systems and Work that can make or change it. The systems
mantra keeps outside use, architecture, and transformer dependencies in view. In this pattern, engineers inspect
those dependencies toward the first unsupported branch and relate later observed Work and change through their
own facts. These are two views of the case, not one calendar sequence.

The recursive account is deliberately demand-driven. An exhaustive description of every supplier, tool, team,
capability, and possible dependency would be expensive and unstable. One unsupported branch plus one WorkPlan
item can be enough to change what the project does next. Further recursion is justified only by that next
decision.

### SYSE.3:11 - SoTA-Echoing


| Current practice line | What changes in this pattern | Source and use | Adoption status |
| --- | --- | --- | --- |
| Current manufacturing work links product architecture with process, resource, and capability choices and uses assembly or production infeasibility to revise design. | The Solution starts from a named architecture result, exposes one transformation-and-capability branch, and uses feasibility evidence to revise the architecture claim it changes. | Eichenwald et al. (2024), Ghanjaoui et al. (2024), and Meixner et al. (2024). These are manufacturing, aircraft-assembly, and cyber-physical-production studies with proposed ontologies, methods, prototypes, and small evaluations. | **Adopt and bound.** Use the product-process-resource-capability connection and architecture revision from feasibility evidence; select the receiving ontology, toolchain, and planning Method for the project. |
| Multi-project scheduling and portfolio selection require different relations: job precedence and shared resource capacity constrain feasible timing; portfolio interactions can change resource demand or combined benefit. | When either relation changes the next realization action, request the corresponding scheduling or portfolio result in :4.6. Common network membership establishes none of these relations, priorities or authorizations. | Gómez Sánchez et al., [*Resource-constrained multi-project scheduling problem: A survey*](https://doi.org/10.1016/j.ejor.2022.09.033) (2023), §§3–4.1, especially §3.2's shared-resource example; Vieira et al., [*Project Portfolio Selection considering interdependencies: A review of terminology and approaches*](https://doi.org/10.1016/j.plas.2023.100115) (2024), §§4.2.2–4.2.5. The first reviews scheduling models; the second compares varying portfolio terminology and proposes a clarification. Neither establishes a particular project's relations or a universally best allocation rule. | **Adapt.** Preserve the distinct relations and let the receiving operations or portfolio decision establish the schedule, priorities, boundary and participating Systems. |
| Continuous integration, delivery, CPS, and SRE practice uses frequent integration, automated and physical checks, feedback, and risk-sensitive change review in bounded technology settings. | A realization branch may request an integration or feedback result and revise the branch from it, while cadence, pipeline structure, release, and assurance remain local questions. | Current DORA capability pages; Thurgood's SRE error-budget example (2018); Zampetti et al. (2022) on ten CPS organizations and a 55-practitioner survey. | **Adapt narrowly.** Use frequent feedback where its engineering conditions fit; establish the local pipeline, cadence, automation boundary, and reliability policy separately. |
| Software Platform Engineering guidance connects platform usefulness to user tasks, interfaces and extensibility. Platform-based manufacturing treats shared Systems as enabling means under its own production and operating conditions. | A platform appears as one possible transformer or enabling branch with a named capability and interface contribution, not as a mandatory layer. | DORA’s [Platform engineering capability guide](https://dora.dev/capabilities/platform-engineering/), “Design for extensibility,” supplies the software interface and contribution guidance; *State of AI-assisted Software Development* v2025.2, pp. 66–72, supplies survey and model evidence about platform experience and outcomes. Tolio et al., “Platform-based manufacturing” (2023), supplies the separate manufacturing contribution. | **Adapt and keep plural.** Evaluate the named platform contribution in its domain and establish the receiving organization, service relations, and platform design separately. |

The manufacturing, portfolio, integration and platform sources above support particular contributions;
their domain results do not establish the superiority of the combined Method. The same-question choice below
determines when its bounded first result is useful and when an implementation Method already supplies enough.

#### SYSE.3:11.1 - Choose the next action with an implementation-preparation alternative

**Question and common basis.** In the pump case in :5.1, what can the engineering team plan next before
committing the manifold to fabrication? Compare the two ways using the same architecture, material and
geometry claims, supplier statements, access conditions and feasibility window. Both require the team's
capability fit and access before the investigation can begin. Count source retrieval, specialist coordination,
recording and the preparation still needed later, rather than equating a shorter description with less total effort.

A serious alternative is the [NASA Systems Engineering Handbook, §5.1, *Product Implementation*](https://www.nasa.gov/reference/5-1-product-implementation/),
especially §§5.1.1.1 and 5.1.1.2.1–5.1.1.2.2. **Adopt** its review of implementation inputs, personnel skills and
enabling products, and its distinct make, buy and reuse duties. It permits tailoring preparation to complexity;
reuse requires fitness for the new requirements and environment. Its enabling-product questions already expose the missing fixture and qualification evidence in this case.

| Receiving decision in the same pump case | Tailored implementation preparation | First-gap planning under this pattern |
| --- | --- | --- |
| Choose an attainable next action while the welding capability and fixture are unsupported. | Review the selected implementation inputs and enabling means. Open a fixture-and-supplier feasibility action before treating the manufacturing branch as ready. Retain the remaining preparation duties. | :4.3 locates the same unsupported branch; :4.5 names the engineering team as the intended investigator, with the supplier weld cell still a candidate for later welding. The useful next action can therefore be the same. |
| Decide how far to investigate the fixture's own production now. | Tailor the enabling-product inquiry to the current implementation decision; a sufficient existing preparation plan may already bound it. | :4.4 asks whether a toolmaking dependency changes the immediate investigation. Expand that branch only if it does; otherwise stop without completing a production-network description. |
| Respond when the feasibility account defeats every fixture-and-weld branch within the selected material, geometry and access conditions. | Reconsider the affected implementation inputs and feasible means; retain the implementation duties for the revised choice. | :4.7 and :5.1 identify the receiving decision: reopen the C.32 comparison of interface, material, module split or placement. Keep the station's flood-use claim unless the result also defeats that claim. |

**Selection and accepted cost.** For this narrow planning question, use the first unsupported dependency together
with an explicit stopping condition and a named return. The stopping condition limits the fixture inquiry to dependencies that change its next action;
the named return directs adverse evidence to the architecture choice it actually changes. These are requirements on the reasoning, not benefits conferred by another form.
If the implementation-preparation account already supplies them through its branch description and WorkPlan,
:4.7 reuses those results; rewriting the account in five lines adds no gain. If they are missing, add the bounded dependency and return to the existing account.

This choice deliberately defers completeness of production preparation. Obtaining a first action leaves personnel,
enablers, quality controls, verification inputs and implementation records to be established for the eventual
make, buy or reuse decision. Their later effort remains in the comparison. When that wider readiness is the
present question, the implementation Method supplies the needed readiness result. The worked comparison supports this
conditional choice; it supplies no measured time saving or general ranking of the two Methods.

Reopen the choice when a second interacting branch or shared-resource constraint can change the selected action,
when the remaining preparation can no longer be deferred, or when another implementation Method supplies the
same bounded decision with less total work. Use :4.4 or the specialist return in :4.6 for the changed dependency;
do not preserve a separate SYSE.3 account merely because it was started.

### SYSE.3:12 - Relations

- A compatible `SYSE.6` architecture decision supplies only the selected structures, constraints, alternatives,
  accepted losses, and reopen conditions needed by this realization question. A compatible `SYSE.8` provider-
  arrangement account supplies only supported provider claims and design constraints that change a branch.
  Each use rechecks subject, configuration, use, horizon, evidence window, and availability; otherwise it uses a
  qualified direct source or records the missing result.
- `C.30` supplies the grounded architecture question and claims; `C.32` supplies candidate configurations over
  selected structures; `C.32.PAD` supplies a project architecture decision when that question is current.
  A missing architecture function bearer reopens the bearer question under `A.6.F` and `C.32`.
- `A.1.STM` keeps the outside-use, architecture, and realization questions in attention while the engineer finds
  the first unsupported answer and later relates observed Work and change through independently grounded facts.
  It supplies neither Work order nor an actual realization network.
- `A.2` supplies the local `TransformerSystemRole` kind; `A.2.1` supplies an obtaining assignment; `A.2.2`
  supplies holder-dependent capability and its envelope, measures, qualification window, and currentness.
  Candidate wording and WorkPlan content establish none of these facts.
- `A.15.2` supplies a WorkPlan for intended Work. `A.15.1` and `A.3.1` govern actual Work and enacted Method.
  `A.3.4` governs actual bounded change, and `A.15.PROD` governs subject-specific production results and
  completion claims when those distinct questions are current.
- `E.18` supplies one selected transformation-flow structure. `E.18.NET` supplies a selected network only after
  independent members, obtaining relation occurrences, endpoint bindings, constraints, and use frame are
  established. Before that boundary, keep a provisional description and name the missing discriminator.
- `SYSE.11` may use only the recursive realization arrangement from a compatible result for the same increment
  boundary. It does not perform Work, establish platform use or constituent commitments, or make the proposed
  System actual.
- Feasibility, integration, configuration, cost, delay, and evidence results can change the affected branch,
  architecture, concept, use or project-focus claims. Platform Engineering, Organization Change,
  Operations, portfolio selection, configuration, safety, security, governance, law, finance, and other
  specialist practices retain their Methods and decisions.

### SYSE.3:End
