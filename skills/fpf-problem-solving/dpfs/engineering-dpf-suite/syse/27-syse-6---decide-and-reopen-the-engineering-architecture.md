## SYSE.6 - Decide and Reopen the Engineering Architecture

> **Status:** Stable

### SYSE.6:0 - Use This When

Use this pattern when an engineering project has several architecture candidates, yet local design choices are
accumulating without one recoverable decision about the project-shaping structures of the engineered System.
Use it also when an earlier architecture decision still appears in a record, but changed conditions—for
example, use, integration, configuration, evidence, or operation—may have made its accepted losses and open
refinements stale.

The intended result is an **engineering architecture decision that selects one option, fixes the
project-shaping constraints, and states when to reconsider it**. In FPF this is an
`ArchitectureDecisionRelation@Project` supplied by `C.32.PAD`, not a second decision kind. In this Systems
Engineering specialization, the decision uses the required engineering content recorded below: each
candidate's use, functional organization, bearers, interfaces, realization, integration, affected-System
consequences, and evidence. The decision names
the selected option, explicit constraints, and results needed by later engineering Work.

**First move.** Name the architecture question, the decision subject, and a project-shaping
structure choice that two current candidates answer differently. When the choice requires authority, cite the
separate authority relation; an assignment or architecture record does not supply it.

This pattern begins after candidate development and ends with a decision plus conditions for reconsideration.
For software proposals named by architectural style, §4.4 explains the mechanisms and trade-offs to recover
before comparison; §4.4.4 follows a choice and a changed premise.
Use `C.32` and `SYSE.5` to develop the candidates, `SYSE.7` to maintain architecture descriptions, `C.32.PAD`
directly when no Systems Engineering specialization changes the choice, and `SYSE.4` to qualify the decision or
identify the basis it still lacks. Release approval and evidence that the intended architecture now obtains
remain separate decisions and claims.

#### SYSE.6:0.1 - Terms and Distinctions

| Name in this pattern | What it denotes |
| --- | --- |
| engineering architecture | The selected structures of an engineered System that shape consequential engineering choices, such as its functional allocation, interfaces, control, or redundancy. For a realized System, `C.30` identifies the `ArchitectureRelation` between that System and each actual selected `U.Structure`. Architecture descriptions state claims about these structures; proposals describe possible future arrangements and the conditions for their realization. |
| architecture candidate | An episteme that proposes selected-structure content, consequences, and conditions for one architecture option. It does not make an architecture relation obtain. |
| engineering project architecture decision relation | The `ArchitectureDecisionRelation@Project` supplied by `C.32.PAD` for an actual engineered System or intended referent and a recoverable composite project `U.Work`. It links the decision subject, candidate basis, selected option, constraints, accepted losses, and reconsideration conditions. The relation does not create the intended System or perform implementation Work. |
| chosen architecture | The structural option selected by the architecture decision, whether retained or intended to be realized. The decision record describes that choice and its constraints. Claims about future realization state what is intended; later observations establish the actual structure. |
| architecture characteristic criterion | One decision-specific criterion row supplied by `C.32.ACS`, with the characteristic, bearer, scale or qualitative frame, use, conditions, protected loss, and guardrail or comparison use needed by the decision. A quality word or metric name is not a criterion row. |
| architecture evaluation result | The result of an eval program under `C.32.ACE`, with its subject, configuration, conditions, parity frame, observations, and limits. It informs a decision; it does not select an option. |
| engineering architecture residual | An unresolved mismatch, loss, unsupported dependency, or omitted consequence tied to selected-structure content, a bearer or affected System, use and operating conditions, and a receiving engineering decision. The tie to that decision distinguishes a residual from an unrelated open task. |
| accepted loss | A disadvantage or unresolved residual that the decision subject knowingly accepts for the declared option, scope, horizon, and protected characteristics. Acceptance does not erase the consequence or establish permission from another decision subject. |
| open refinement | Decision content that leaves named lower-scope or neighboring structure choices undecided while fixing the project-shaping constraints they must satisfy. Interface, evidence, and affected-System claims retain their own Methods and grounds. |
| reopen condition | A stated event or observation—for example, a source or configuration change, characteristic crossing, failed dependency, or changed use—that requires the named decision subject to reconsider the decision. The condition opens reconsideration; the later decision remains a separate occurrence. |

Words such as *architecture*, *style*, *pattern*, *platform*, *modular*, *open*, *integrated*, *distributed*,
*AI-native*, and *evolutionary* are recognition cues until the current claim identifies the selected structures,
criteria, Method, decision relation, or observed change meant.

### SYSE.6:1 - Problem Frame

Engineering architecture decisions coordinate many later choices without deciding every detail. They can fix a
functional allocation, module boundary, interface grammar, placement, control boundary, redundancy principle,
product-family variation policy, evidence boundary, or other selected structure that several realization and
specialist decisions must respect.

The decision sits between possible futures and physical realization. Its grounds may include, for example,
current descriptions, comparisons, estimates, experiments, or specialist returns. Later Work may produce a different actual structure
or expose consequences that were not visible. The architecture decision must close enough choice for current
engineering Work while preserving alternatives and explicit conditions for revision.

### SYSE.6:2 - Problem

Without a bounded architecture decision, local choices become a de facto architecture. Contributors—for
example, component suppliers, software teams, construction specialists, operators, safety specialists, or
providers of supporting Systems—each optimize their own structure. Their decisions can be individually
reasonable and jointly incompatible. Burdens such as interface, placement, configuration, assurance, or
affected-System consequences appear only during integration or operation.

An oversized architecture decision causes the opposite failure. It fixes low-level details without the local
knowledge needed to choose them, substitutes centralized approval for specialist contribution, and makes every
revision look like a whole-project exception. A broad quality catalogue or one score does not solve the problem:
characteristics have different bearers, Scales, conditions, evidence, and protected losses.

A decision record can hide both failures. A file can be complete while the candidate basis is narrow, accepted
losses are absent, the selected structure is unclear, or no observation can reopen the decision. Engineers then
preserve documentation instead of maintaining a current engineering choice.

### SYSE.6:3 - Forces

The decision must manage these recurring tensions:

- Current engineering contributors need stable constraints, while architecture knowledge and operating
  conditions continue to change.
- Whole-System coherence requires cross-boundary constraints, while detailed choices need local specialist
  knowledge and room to vary.
- A small characteristic set makes trade-offs visible, while omitted affected Systems or scales can move the
  burden outside the chosen boundary.
- Early estimates are cheaper than realization, while integration and operating evidence are often more
  decision-relevant.
- Architecture moves such as modularity, reuse, distribution, or standardization can reduce one burden while
  increasing others—for example, coordination, evidence, latency, supply, cost, or failure-coupling burdens.
- Current contributors need one selected option as a common decision basis, while rejected or deferred
  alternatives can remain valuable when the environment, technology, or evidence changes.
- AI-assisted synthesis and analysis can widen and criticize alternatives, while authority, accepted loss, and
  the engineering decision still require an identified decision subject and adequate grounds.
- A decision that is easy to supersede supports continuing change, while a decision with no stable identity or
  effectivity cannot coordinate implementation and configuration.

### SYSE.6:4 - Solution

Apply `C.32.PAD` to the Systems Engineering decision. Compare candidates only when their engineering
consequences are visible enough for the current commitment. Select the project-shaping
structures needed to coordinate later Work. State accepted losses and open refinements, then state which
later results—for example, from realization, integration, configuration, specialist, assurance, or operating
Work—can confirm or reopen the choice.

#### SYSE.6:4.1 - Perform the Move

1. **Bind the architecture question.** Name the actual engineered System or intended referent, composite
   project Work, decision subject, deciding Agent, use, configuration or variant, operating envelope, horizon,
   and the later decisions this architecture choice must coordinate. If the intended System does not yet exist,
   keep its referent in claim content as required by `C.32.PAD`. When the decision requires authority, cite the
   independently obtaining direct authority relation with its bearer, scope, basis, applicability, and interval.
   If that relation lacks a governing rule or does not obtain, candidate analysis may continue. Report the
   missing rule or authority relation; do not treat an assignment or record's presence as authorization.
2. **Select the project-shaping structures.** Identify the selected structures whose alternatives can change
   several downstream choices or a protected characteristic. Examples include functional, constructive,
   placement, control, transformation-flow, information, evidence, Method, Work, and organization structures.
   Name each structure and the relation under discussion; *important*, *cross-cutting*, and *hard to change* are
   prompts, not membership tests.
3. **Prepare candidates for the decision.** Start with a compatible `SYSE.5` account or a qualified direct
   source for functional organizations, candidate bearers, allocations, interfaces, and conflicts. Add
   provider-arrangement constraints from `SYSE.8`, description evidence from `SYSE.7`, specialist results from
   `SYSE.9`, and engineering claim assessments from `SYSE.10` only when they fit the same subject, configuration,
   use, horizon, decision, and evidence window. For each input, state what it describes and which claim it can
   support. Evidence informs the decision but neither authorizes nor entails it; a specialist result answers only
   its receiving question under its stated conditions. If an input is unavailable or incompatible, use a
   qualified direct source or record the missing result. Keep a candidate only when its unsupported
   dependencies—for example, bearer, interface, realization, integration, configuration, or evidence
   dependencies—are visible as bounded residuals that the decision subject can knowingly accept.
4. **Define the criteria before evaluating.** Select a small set of `C.32.ACS` rows tied to this use and decision.
   For every characteristic, name the bearer, scale or qualitative frame, operating conditions, protected loss,
   comparison use, and guardrail or reopen reading when one is justified. Keep non-equivalent characteristics—
   for example, safety, performance, cost, resilience, changeability, or evidence burden—in separate rows unless
   the decision supplies and justifies an aggregation Method that preserves the distinctions it uses.
5. **Compare coherent candidates.** Compare whole proposals rather than isolated module choices. Include
   decision-relevant consequences—for example, expected functioning, physical principle, interfaces, placement,
   failure containment, realization and integration dependencies, supply and provider conditions, configuration
   continuity, operating and maintenance effects, affected Systems, evidence burden, or change consequences. Use `A.19.CPM`, `C.11`, or another direct
   comparison or choice pattern for the claim actually being made.
6. **Challenge the preferred option.** Ask which omitted structure or affected System could reverse the
   preference. Examine the relevant existing analyses and observations under their configuration, conditions,
   and claim limits. Before commissioning further Work, use `C.11.DUA` to compare it with proceeding on the
   present basis, narrowing the commitment, or stopping. Include what the inquiry could change, its cost and delay.
   Applicable evidence requirements govern that choice. The challenge may use specialist criticism,
   computation, simulation, prototype or
   bench tests, integration trials, or operating observation. For challenge Work whose result the decision uses,
   keep its performer, Method, configuration, conditions, and claim limits recoverable from that result; reuse
   the existing account where it is sufficient. Use an AI-produced ranking or architecture description as one
   input. The identified deciding Agent remains responsible for the choice. A claim of physical adequacy needs
   evidence about the physical System; selecting an option with stated residual uncertainty does not assert
   that stronger claim.
7. **Make the decision relation explicit.** Fill the current `ArchitectureDecisionRelation@Project` with the
   candidate basis, selected option, affected structures, criteria and trade-offs, accepted losses, rationale,
   consequences, effectivity and currentness claims, horizon, and rejected or retained alternatives. A bounded exception is a decision only
   when its scope, cost, protected loss, and reopen condition are explicit.
8. **Fix constraints and preserve refinement freedom.** State the decision-relevant constraints—for example,
   structure relations, interfaces, allocations, variation policies, or characteristic guardrails—that later
   Work must preserve. Separately state
   which implementation details and lower-scope structures remain open. Establish Work assignments, authority,
   commitments, and permissions through their own relations rather than through the architecture decision.
9. **Name the engineering uses.** Identify the receiving Work and the constraint or question it needs. Where
   later Work can change the grounds for this choice, connect its relevant result or return condition to the
   affected architecture question and decision subject. Use an existing compatible decision or configuration
   account for these connections when it already supplies them. Supply
   compatible selected-structure constraints and reconsideration conditions to `SYSE.3`, `SYSE.13`, and
   `SYSE.18` only where they change the receiving design choice. During decision Work, use `SYSE.9` to request a
   specialist contribution when one is needed. Use `SYSE.7`, `SYSE.10`, or `SYSE.4` for a current description
   gap, evidence question, or assurance question. Each receiver rechecks subject, configuration, horizon,
   authority, and compatibility.
10. **Design the continuation.** For each material assumption or accepted loss, name the event or observation
    that calls for reconsideration—for example, a source change, actual-structure comparison, characteristic
    reading, failed interface, changed use, or affected-System consequence. Name the decision subject and the question to reconsider. A
    threshold crossing supplies an observation, not an automatic replacement decision.
11. **Check what actually obtains.** After realization or integration Work, compare the observed configuration
    and selected structures with the decision content. Record divergence and evidence separately from the
    decision and its description. Supersede the decision when a material changed claim alters the
    selected option, accepted loss, fixed/open boundary, or receiving Work.
12. **Stop at coordination sufficiency.** Return when affected practitioners can tell what current structures
    and constraints guide their Work, what remains open, which losses are accepted, which result they must
    return, and what can reopen the choice. Do not wait for complete detailed design.

This list is a learning and reasoning aid, not a lifecycle or temporal order. Work such as candidate
development, specialist analysis, realization preparation, evaluation, configuration, or architecture revision
can overlap. A
result dependency states which earlier result the receiving decision Work needs; it does not prescribe when each
producing Work occurrence must finish.

#### SYSE.6:4.2 - Record the Result

Record the decision with `C.32.PAD`. For Systems Engineering use, include the following content in the
decision relation and its cited subjects:

| Result position | Required content |
| --- | --- |
| bounded decision | Composite project Work, actual engineered System or intended referent, decision subject, use, configuration, operating envelope, horizon, question, and intended receiving decisions. |
| candidate basis | Compatible `SYSE.5` alternatives or qualified direct sources; provider-arrangement, affected-System, specialist, realization, configuration, and evidence conditions material to the choice. |
| selected structures | Obtaining structures or possible-future claim content, affected relations, selected option, fixed project-shaping constraints, and open refinements. |
| criteria and evidence | Decision-specific `C.32.ACS` rows, any `C.32.ACE` results, comparison or choice result, sources, observations, uncertainty, and limits. |
| trade-offs | Expected gains, accepted losses, unresolved residuals, rejected or retained alternatives, protected characteristics, and affected-System consequences. |
| engineering returns | Named constraints, questions, and result conditions supplied to receiving decisions—for example, realization, integration, configuration, description, specialist, assurance, supporting-System, operation, or maintenance decisions. When a returned result can change this choice, name the affected architecture question. |
| continuation | Observations and source changes that call for reconsideration, the decision subject and authority for that reconsideration, the supersession condition, and comparison of later actual structures with decision content. |

An ADR-like file or architecture description can publish parts of this result through `C.32.ADR` and
`C.30.AD`. Identify its correspondence to the decision relation. Ground the actual architecture and later Work's
use of the decision independently.

#### SYSE.6:4.3 - What Changes in Practice

The engineering project makes a bounded, inspectable commitment across the structures that constrain several
contributors. Downstream teams receive constraints and questions their Work must answer. Detailed design
remains free where the decision leaves it open. Later integration or operating evidence can give the decision
subject grounds to reconsider the affected decisions while preserving choices whose grounds still hold.

#### SYSE.6:4.4 - Compare software architecture arrangements by their mechanisms

Use this explanation when software candidates are being compared by labels such as *layered*, *pipeline*,
*plugin*, *service-oriented* or *microservices*. A style restricts how parts may depend on, communicate with
and change one another. Those restrictions can produce useful properties under particular workloads and
change patterns. The name alone supplies neither the restrictions nor their effects in your candidate.

The following repertoire helps an engineer understand and question a software proposal before detailed
implementation. It assumes ordinary knowledge of program modules, calls, storage and deployment. It does
not replace the specialist design of algorithms, security, distributed transactions or hard real-time
execution. Use §4.1 to decide among sufficiently developed candidates; return an unexplained mechanism to
candidate development rather than awarding points for a familiar style.

##### SYSE.6:4.4.1 - Identify which structure each name constrains

Keep four boundaries visible in the same candidate. A **module boundary** controls which implementation
knowledge other code may use. A **runtime boundary** separates executing processes or machines, with
communication and failure consequences. A **data boundary** determines who may change particular state
and which invariants must hold together. A **release boundary** determines what can change without a
coordinated update of its consumers. Team responsibility is a further organizational relation: draw it
alongside these boundaries rather than deriving it from a box count.

These boundaries need not coincide. A well-structured application can contain many modules in one
release. Several separately running services can still need one coordinated release because they share
a changing schema or incompatible protocol. If an *architectural quantum* is used in discussion, ask
which execution, state and compatibility dependencies make the proposed unit independently deployable
under the stated conditions. Calling each team or process a quantum does not answer that question.

The alternatives below are not successive generations or mutually exclusive bins. A service can contain
layers; its import job can be a pipeline; its domain logic can use ports and adapters. Compare complete
combinations at the boundary relevant to the decision.

| Arrangement | Organizing mechanism and useful consequence | What can defeat that consequence |
| --- | --- | --- |
| Layers, often within a modular monolith | Responsibilities are separated and allowed dependencies constrained. The responsibility groups are functional layers. Identify separately the modules that realize them and any levels in their dependency or interface structure. Presentation changes can remain apart from domain rules; internal calls and a shared transaction can keep a small application straightforward to operate. | A feature cutting across all layers still requires coordinated changes. Pass-through layers add work without isolating a changing decision. Logical layers need not be separate network tiers; adding tiers changes latency and failure handling. |
| Pipes and filters | A task becomes transformations with explicit input/output contracts, connected by streams or queues. A filter can be reused or replaced when its contract remains compatible; stages and independent items can execute concurrently. | Global state, order requirements, blocking joins and an expensive serial stage limit concurrency. Serialization, transport and intermediate storage can dominate small transformations. Recovery must distinguish replayable processing from irreversible effects. |
| Core with plugins, often called microkernel architecture | Stable common responsibilities stay in the core; variable behaviour enters through extension contracts. A document tool can accept another format or analysis without editing every existing extension. | The extension contract may not express the new variation. Core changes then affect many plugins. Loading a plugin into the same process does not isolate a crash, malicious access or resource exhaustion; isolation needs an actual mechanism. |
| Service-oriented arrangement | Capabilities are accessed through described interfaces, potentially across ownership domains. Consumers can use a capability without taking over its implementation. | A shared database, central orchestration or common schema may create substantial coupling. SOA itself does not require one database, a particular bus or one deployment model. Compare the actual coordination arrangement. |
| Autonomous services, including microservices | Responsibility and writable state are encapsulated behind compatible interfaces, with separately operable releases. A capability can change or scale without changing unrelated implementations. | Cross-service invariants, synchronous call chains and incompatible contracts restore coupling. Separate storage adds synchronization, recovery and observation work. A small endpoint is not automatically an autonomous business capability. |
| Event-driven communication | Producers publish occurrences that interested consumers interpret under agreed contracts. New reactions and independent consumer rates can be supported without adding each consumer to the producer's call chain. | Delivery delay, duplication, ordering, schema change and incomplete processing become explicit design problems. Removing a synchronous call does not remove the business dependency or make a timely joint result inevitable. |

A **modular monolith** is a serious candidate, not a failure label: one deployment with enforced module
interfaces can retain local transactions and inexpensive calls. Its cost is a shared release and often
shared scaling or failure scope. Current Spring Modulith supplies one concrete implementation of exposed
module interfaces and hidden internals; it does not prove that every single-deployment application is modular.

Two commonly confused arrangements answer other questions. **Ports and adapters** place domain-facing
interactions behind interfaces so that a user interface, database adapter or test double can change without
embedding its technology in the application logic. The original hexagonal architecture explains this
inside/outside distinction; it is not a claim that a particular number of layers or machines is necessary.
A **sidecar** is a separately executing companion deployed with an application instance, often for proxying
or telemetry. Its resource cost and lifecycle follow that placement. A sidecar can coexist with ports and
adapters; it is not their replacement or a rule about ownership of domain data.

##### SYSE.6:4.4.2 - Derive performance claims from the actual path

Separate **latency**, the elapsed time for one requested result, from **throughput**, completed results per
unit time. For an illustrative three-stage pipeline, suppose each item requires 2, 8 and 2 milliseconds of
service, each stage has one dedicated worker, and independent items stream without batching, transport cost
or contention. The first item needs 12 ms. Once filled, the pipeline can complete at most one item per 8 ms,
or 125 items/s. Executing all three transformations on one worker would allow at most 1/0.012, about
83 items/s. Pipelining can therefore improve throughput without reducing that item's service latency.

Two independent workers at the middle stage raise its ideal capacity to 250 items/s; the other stages
each allow 500 items/s. That bound assumes independent items can be routed to either worker and there is
no shared serialization point. If every item
must update the same locked state, or a later stage waits for a complete batch, this calculation does not
apply. Queueing, retries and networking add elapsed time. At a sustained arrival rate above the slowest
stage's capacity, backlog grows unless work is rejected, reduced or capacity changes. Below that bound,
variability can still make a tail-latency target fail. Calculate the dependency path and capacity constraints.
Use qualified evidence for the performance commitment being made; obtain representative measurements when its required basis is missing.

The same reasoning applies to services. Five dependent remote calls add waiting and partial-failure cases;
five independent computations may run concurrently, but the result still waits for whichever contributions
it requires. Count the actual calls and shared resources. A style rating such as “high performance” cannot
answer whether a caller receives the needed result within its deadline. For a high-rate image conversion
job, separating and scaling a slow filter may be useful; for a short local lookup, the added transport may
cost more than the transformation.

##### SYSE.6:4.4.3 - Follow state, compatibility and change across the boundaries

Start with a representative behaviour and a consequential change. Trace which modules, running services,
data and consumers must participate. For a reservation, ask which state prevents two parties receiving the
same remaining item. If two modules share one transaction, its isolation and locking still need qualification,
but it can supply one place to enforce the invariant. If two services own separate state, name the coordination
that preserves the required promise, or explicitly change the promise and supply an acceptable failure or
compensation path. Eventual consistency is suitable only where the receiving use tolerates that interval.

Next change an interface or stored representation. A service may be separately deployable only if old and
new consumers can coexist, required data are available, and the provider can observe and recover from a
failed update. `SYSE.34` develops compatible data changes; `SYSE.35` and `SYSE.41` supply controlled exposure
and actual deployment. Their work is part of the cost of the architecture, not a benefit obtained by drawing
more boxes. For plugins, apply the same question to the extension API and host version; `SYSE.53` resolves a
particular compatible component selection once those conditions are known.

Use the trace to compare three kinds of change: changing an internal algorithm while preserving the contract,
extending a capability through an existing contract, and changing the contract itself. The first two may be
local; the third exposes affected consumers. Check persistent data and operational procedures as well as code.
If every modest feature crosses the same boundaries, reconsider the partition instead of continually adding
coordination machinery. `SYSE.23` compares the resulting investments in the target and its builder arrangement.

This produces a reasoned comparison: the useful independence, the mechanism carrying it, the coupled work
that remains, and the condition that would reverse the choice. It does not rank styles outside that use.

##### SYSE.6:4.4.4 - Software case: booking equipment without distributing the reservation invariant

A small field-service organization needs equipment booking, a searchable catalogue and inspection reports.
The stipulated current conditions are one development team, a common weekly release, moderate booking load,
and a promise that one available kit cannot be committed to two crews. Inspection photographs arrive in bursts;
search results may lag by a minute, but confirming a booking must use current authoritative availability.
These are constructed decision inputs, not measured production results.

Candidate A has one application deployment with separate catalogue, reservation and inspection modules,
a controlled shared transaction for the booking invariant, and a queued image-processing worker. Module
interfaces prevent an inspection-screen change from reaching into reservation internals. Candidate B splits
catalogue, reservation and inspection into independently deployed services with owned storage, keeping the
reservation authority in one service. Both can use ports and adapters for external maintenance reports.

A saves distributed-operation work while meeting the team's common release arrangement. The queued worker
can scale for photograph processing without partitioning booking state. B could release inspection changes
separately, but the current team does not need that freedom; it must nevertheless design version compatibility,
message recovery, replicated search data and tracing. Splitting availability and reservation into separately
updated stores without a coordination mechanism would create a third, currently inadmissible candidate:
a favourable latency estimate cannot compensate for an unsupported booking promise.

For these inputs the decision retains A, with enforced internal interfaces, one authoritative reservation
operation and bounded search freshness. It accepts the shared application release and application-process
failure scope. The decision requires workload evidence before asserting response-time adequacy. A plugin
mechanism would be considered if separately supplied inspection algorithms became a recurring variation;
a pipeline is useful for the photographs, not automatically for the entire booking interaction.

Now change the premise. Inspection is maintained by another provider, must be released several times a day,
and processes untrusted large files; its execution failures must not stop booking. A separate inspection
service or isolated worker with a versioned result contract becomes a stronger candidate. Compare a separation of inspection that supplies those properties with B's wider partition. Retain reservation authority
and its still-valid invariant argument; define how delayed or rejected inspection results affect booking.
The new preference follows from release and failure conditions, not from team count alone. Actual isolation,
compatible updates and resource limits need implementation evidence.

An unlike use changes the choice again: an offline inspection desktop tool accepts third-party file readers
but has no independent service operators. A stable core with compatible plugins and an isolation mechanism
for untrusted readers may address its variation. A network service per reader would add an availability
condition the offline use cannot meet.

### SYSE.6:5 - Worked Case: Architecture Decision for the Heat-Pump Plant Controller

Engineers using `SYSE.5` have developed two alternatives for the same occupied-building heat-pump plant.
In A, local unit controllers carry protection and normal regulation while a supervisor sends bounded
set-points. B adds thermal storage and tariff scheduling; its local controllers retain protection and regulation.

The decision is which architecture should guide engineering of configuration `HP-2` for the next three
heating seasons. The architecture board is the decision subject; a separate project relation gives it
authority for that choice. The assignment and decision record do not create that authority.

Continue the `SYSE.5` proposals with additional stipulated design inputs: a thermal/hydraulic account
and a compatible sensing and control arrangement. These are premises of this worked case, not reported plant
results. If the sensor-variant conflict in `SYSE.7` remains open, follow that return before relying on the
storage comparison below.

Both proposals use the same building heat-demand and weather envelope, comfort requirement, communication-loss
condition, installation window and budget. Compatible unit results and design analyses support both at the
scope of the architecture commitment; whole-plant qualification is still required before operation. Seasonal
energy and storage-cycling claims remain unresolved as shown below. Layout and supply estimates leave both
options within the window and budget, with the required maintenance access.

After protection and comfort, the building owner gives priority to less installation disturbance and a
smaller added maintenance burden. Peak-period flexibility is desirable but is not a current requirement.
The board compares the complete arrangements under those conditions:

| Decision-relevant consequence and basis | A — local regulation with bounded supervision | B — storage with tariff scheduling |
| --- | --- | --- |
| Protection and comfort under the shared envelope | Uses the qualified local protection and the existing heat-delivery path. The design analysis supports the required comfort response. | Retains the same local protection. The design analysis includes the storage charging and discharge modes needed for comfort. Neither option gains preference by dropping the protection condition. |
| Installation and maintenance burden in the stipulated plans | Retains the heat path and adds supervisory connections and configuration. It needs fewer site changes and no storage-loop servicing. | Adds a tank, pump, valves, sensors and charging controls. The layout allows access, but installation and later servicing cover these additional parts and modes. |
| Response during a two-hour utility peak | Can adjust set-points within the comfort envelope, but the stipulated heat balance does not support a two-hour compressor stop at the declared cold-weather load. | A design-stage heat balance supports delivery from the charged store during that stop, including usable stored energy, discharge rate and losses. This is model support for the declared conditions, not an observed operating result or zero electricity use by the whole plant. |
| Seasonal energy, cycling and economic consequences | Peak-period compressor use remains. Comparative seasonal consumption and total cost are not established. | Tariff scheduling could move purchases out of the peak period; storage losses and charging cycles also matter. The available comparison does not establish a seasonal energy or total-cost advantage. |
| Continuing change | Storage can be added later through reserved interfaces, but that would require another physical alteration and qualification. | Storage flexibility is developed now, at the cost of the added equipment, control modes and their continuing configuration and evidence burden. |

**Present choice.** The board selects A. Both proposals meet the conditions needed for this bounded
commitment, and A is better on the owner's stated priority. B's supported peak-shifting possibility does not
override that priority while flexibility remains optional and its seasonal economic advantage is unknown.
No aggregate score is needed. The board accepts A's lack of the modeled two-hour shift, continued exposure
to peak-period purchases, and the possibility of a later retrofit. It does not claim that A has the lowest
lifetime cost.

The resulting `ArchitectureDecisionRelation@Project` fixes these structures:

- local protection remains within each unit boundary and does not depend on supervisor or utility communication;
- supervisory set-points stay inside declared unit operating envelopes;
- plant-state and command interfaces carry units, timestamps, quality, validity, fallback, configuration and effectivity conditions;
- a later storage branch enters through the declared thermal, control, configuration and assurance interfaces.

Algorithm choice, hardware supplier, detailed state estimator and user-interface design remain open
provided they preserve those constraints. The controller and integration teams use the constraints while
shaping controller, bench, installation and integration Work with `SYSE.3`. Configuration and interface-version
Work uses `SYSE.13`; utility-signal authority and service conditions use `SYSE.18`. Model and trial results are
assessed through `SYSE.10`, and assurance through `SYSE.4`. Each receiving practitioner applies the relevant
Method to produce the needed result; the architecture decision supplies constraints and questions.

**Changed premise.** Suppose the utility contract now requires that same two-hour compressor stop while
the building's comfort requirement remains. The accepted flexibility loss is no longer admissible. Reopen
the A/B choice: with the other stated premises still current, B's heat balance supports selecting it for
further engineering, while A's does not support the new requirement. The board can make a new decision for
the remaining horizon; this does not qualify B for operation. Preserve the local protection constraint and
still-applicable unit results, and return the storage, charging-control and integration questions to their
receiving work. If the relied-on storage calculation or installation premise fails, reopen that unsupported
branch instead of treating the new contract as proof that B works.

A lower tank price alone would not automatically overturn A: the board would examine whether it changes
the burden comparison or the owner's priority. Unknown seasonal savings remain unknown. Communication-loss
failures, comfort or cycling guardrail crossings, changed utility-signal semantics and material installed
divergence also retain their named return to the affected architecture question.

After integration, compare the actual installed Systems and relations with the decision content. Different
wiring, fallback or control allocation is an implementation divergence even if the architecture record was
left unchanged. The decision, its later supersession and evidence of the obtaining plant configuration
remain separate.

### SYSE.6:6 - Biases to Watch

Three recurring biases matter here. **Record-presence bias** treats a complete diagram or file as a current
decision; recover the selected option, constraints, accepted losses, effectivity, and reopen conditions.
**Single-score bias** lets a modularity measure, connection count, maturity level, or aggregate score hide different
bearers and losses; compare decision-specific criteria. **Software-transfer bias** imports a software architecture
example as a general engineering rule; recheck the physical realization, operating conditions, and evidence of
the engineered System.

Agents may contribute when their capability and assignment fit the needed work. The deciding Agent remains
responsible for the choice under the applicable authority and evidence conditions. Application DPFs supply
the subject-specific Methods and safeguards needed for the engineering question.

### SYSE.6:7 - Conformance Checklist

| ID | A conforming use... |
| --- | --- |
| `CC-SYSE6-1` | names the composite project Work, actual engineered System or intended referent, decision subject, use, configuration, horizon, and receiving decisions. |
| `CC-SYSE6-2` | identifies project-shaping selected structures and relation claims rather than using *important* or *hard to change* as an architecture definition. |
| `CC-SYSE6-3` | admits candidates only with explicit functional, bearer, interface, realization, integration, affected-System, and evidence consequences or bounded residuals. |
| `CC-SYSE6-4` | defines decision-specific architecture-characteristic criteria before relying on eval results or scores. |
| `CC-SYSE6-5` | compares coherent alternatives and exposes gains, accepted losses, unknowns, and burdens moved elsewhere. |
| `CC-SYSE6-6` | returns one `C.32.PAD` decision relation and grounds the architecture claim, description, actual architecture, Work, and evidence through their own kinds and relations. |
| `CC-SYSE6-7` | distinguishes fixed project-shaping constraints from open refinement and preserves specialist authority. |
| `CC-SYSE6-8` | names each result needed by receiving Work—for example, a realization, configuration, specialist, description, assurance, supporting-System, operating, or maintenance result. |
| `CC-SYSE6-9` | states observable reopen conditions, the decision subject for reconsideration, and the question reopened. |
| `CC-SYSE6-10` | later checks the actual configuration and structures separately from the decision content and its publication. |

### SYSE.6:8 - Common Failures and Repairs


| Failure | Symptom | Repair |
| --- | --- | --- |
| Local choices as architecture | Interfaces, modules, suppliers, and software partitions accumulate without a joint decision. | Select the project-shaping structures and make one bounded `C.32.PAD` decision relation with explicit receiving Work. |
| Architecture as everything important | The decision includes every design detail and unresolved issue. | Keep only selected structures coordinating several choices or protected characteristics; leave named refinement open. |
| Hard-to-change definition | Costly change alone makes an item architectural. | Name the selected structure, current alternatives, consequences, and decision use; difficulty is one possible characteristic. |
| Quality catalogue | Generic qualities are scored without bearers, conditions, Scales, or protected losses. | Create a small `C.32.ACS` criteria set for the current decision and preserve non-equivalent readings. |
| Metric as selector | A dashboard or eval result chooses the architecture automatically. | Interpret the reading under its subject and parity frame, then use the direct comparison and decision patterns. |
| Modularity as universal good | More modules, fewer connections, an open standard, or one supporting System is assumed better. | Compare decision-relevant consequences—for example, function bearing, coupling, cohesion, substitution, integration, evidence, cost, supply, or change—under the stated use. |
| Candidate without realization | A plausible structure lacks a needed realization dependency—for example, a transformer System, capability, interface realization, integration relation, or evidence return. | Record a bounded residual or return the unsupported branch to `SYSE.3`; do not hide it in an architecture label. |
| Organization mirroring shortcut | Current teams or communication links are copied into technical architecture by analogy. | Use `C.32.CONWAY` only for a stated influence or correspondence question; keep organization and engineered-System structures distinct. |
| Record as decision | An ADR or diagram exists, but selected option, relation, losses, and effectivity are unclear. | Recover the decision relation first; publish it afterward through the description and publication patterns. |
| Decision as actual structure | Possible-future selected content is reported as installed architecture. | Inspect the actual Systems and obtaining relations after Work; keep divergence and evidence separate. |
| Frozen architecture | Later integration or operation contradicts the basis, but the old record remains authoritative. | Reconsider the affected decisions under their named reopen conditions; supersede those whose content must change. |
| Whole-project exception | Any local refinement or residual requires centralized architecture approval. | Preserve the fixed/open boundary and escalate only changes that cross a declared structure, guardrail, or affected decision. |

### SYSE.6:9 - Consequences

Engineering contributors gain a current structural commitment that is strong enough to coordinate their Work
and narrow enough to preserve local design knowledge. Accepted losses and unresolved residuals become visible.
Realization, configuration, assurance, operation, and maintenance receive explicit questions and return
conditions. The architecture can evolve through superseded decisions rather than through undocumented drift.

The cost is deliberate comparison and continuing maintenance of decision identity, descriptions, evidence, and
effectivity. Some candidates remain open longer, and a preferred local solution can be rejected because it
moves an unacceptable burden elsewhere. Limit that cost by selecting the project-shaping structures needed
for coordination and further inquiry whose expected contribution warrants its burden, while meeting applicable
evidence requirements.

### SYSE.6:10 - Rationale

`C.32.PAD` already supplies the transdisciplinary architecture decision relation. This specialization changes
the Systems Engineering move: candidates must expose use, functional organization, actual or intended bearers,
physical and informational interfaces, realization and integration feasibility, affected Systems, and
specialist evidence. The decision turns the selected option into constraints and result conditions for
realization, configuration, integration, assurance, operation, maintenance, and later checks of the actual
structure.

### SYSE.6:11 - SoTA and Source Use

**Practice question.** In a project using FPF, how should engineers choose among developed architecture
options and keep that choice useful when realization, integration or operation changes its grounds?

**Selected answer.** Combine proportionate decision analysis with an explicit fixed/open boundary and
connections from the decision to receiving engineering work and back. Use the direct comparison and choice
Methods for selection; use `C.32.PAD` for the commitment, accepted losses, refinement freedom and
reconsideration. The Systems Engineering contribution is to fill those connections with the actual
realization, interface, configuration and evidence dependencies that could change this choice.

A serious alternative is [NASA's Systems Engineering Handbook, §6.8, especially
§§6.8.1–6.8.1.2.5](https://www.nasa.gov/reference/6-8-decision-analysis/).
It distinguishes mandatory and enhancing criteria, scales the analysis to the decision, examines whether
reducing uncertainty is worth its cost and delay, allows closely ranked alternatives to reach the decision
maker, and separates a recommendation from the authorized choice. **Adopt** these disciplines in §4.1
steps 4–7. They support the qualitative A/B choice in §5; neither a compulsory aggregate score nor exhaustive
inquiry is needed.

[NASA §6.5, especially §§6.5.1.2.2–6.5.1.2.3 and the configuration-verification
activity](https://www.nasa.gov/reference/6-5-configuration-management/) connects approved
baselines, change authority, impact evaluation and verification of implementation. A project applying these
together can maintain an architecture decision through change. Its actual arrangement may already supply
the connections used here.

The remaining practical question is what this choice constrains and what a later result can overturn.
For HP-2, the ordinary supplier choice remains open while local protection and command limits remain fixed.
The new two-hour curtailment requirement changes the acceptability of the flexibility loss and reopens the
A/B decision. It preserves the still-valid local-protection basis. That is the connection made explicit in
§4.1 steps 8–11 and the engineering-return position in §4.2: the receiving work, its relevant result or changed
condition, and the affected architecture question stay joined.

**Adapt** decision-analysis and configuration information to these bounded engineering uses. The
`C.32.PAD` fixed/open and source-return distinction supplies the general move; the HP-2 filling is authored
here. Compared with a choice report and product baseline that leave those connections for each receiver to
reconstruct, this account gives the installer, controller developer and architecture board a shared answer
about which change needs which decision. If the existing report and configuration arrangement already give
that answer, cite and use them. This pattern calls for no duplicate account or replacement of their change
authority.

The deliberate cost is identifying and maintaining the few receiving questions and return conditions that
matter. Accept that effort when an engineering result can invalidate a material decision premise or expose
a conflict between fixed constraints and open refinement. For a self-contained choice whose consequences
need no such coordination, use the direct decision Method. The comparison supports this bounded connection
and its worked changed-condition return; it supplies no measured reduction in engineering time or failure
rate and no general ranking above NASA's wider process.

[Ford, Richards, Sadalage and Dehghani, *Software Architecture: The Hard Parts*, chapter 7,
“Finding the Right Balance” and “Ticket Assignment Granularity,” pp. 24–28](https://www.thoughtworks.com/content/dam/thoughtworks/documents/books/bk_software_architecture_hard_parts_ch7_en.pdf)
provides a developed comparison of opposed consequences. **Adopt** its explanatory move: connect the choice
to the actual interactions and priorities, and retain a disadvantage of the selected option. The heat-pump
case applies that move to installation burden and peak flexibility. **Reject** transferring a particular
software granularity choice into a universal engineering rule; the physical dependencies and qualifications
in §§4–5 govern this use.

Reopen this selection if the connections fail to identify the affected decision, their maintenance costs
more than the receiving use warrants, or another applicable method supplies the same decision and return
with less effort and no lost constraint. Changed source or engineering conditions reopen the affected
comparison. Recheck an affected AI allocation or evidence claim when the tool generation, task distribution,
engineering profile or quality outcome changes.

#### SYSE.6:11.1 - Software-style comparison and its source limits

The software explanation in §4.4 adopts mechanism-and-condition comparison, not a universal score table.
Current [Microsoft N-tier guidance](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/n-tier)
separates logical layers from physical tiers. Its [Pipes and Filters explanation](https://learn.microsoft.com/en-us/azure/architecture/patterns/pipes-and-filters)
allows independently scaled stages, while its [event-driven architecture guidance](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven)
exposes ordering, recovery, consistency and observation costs. Use these as concrete explanations; their
Azure deployments are alternatives, not requirements of SYSE. The pipeline arithmetic and cases here are
constructed from their stated premises, not performance measurements from those sources.

For service autonomy, compare current [Microsoft microservices guidance](https://learn.microsoft.com/en-us/azure/architecture/microservices/)
with the serious single-deployment alternative illustrated by [Spring Modulith's module model](https://docs.spring.io/spring-modulith/reference/fundamentals.html).
The latter makes provided interfaces and internal implementation distinguishable without requiring a service
per module. **Adapt** these mechanisms to the candidate's actual consistency and release needs; neither
technology establishes the appropriate partition by itself.

Historical anchors remain useful for specific distinctions: [Cockburn's Hexagonal Architecture (2005)](https://alistair.cockburn.us/hexagonal-architecture)
for application ports and technology adapters; [OASIS SOA Reference Model 1.0 (2006), §§2.1 and 3.2](https://docs.oasis-open.org/soa-rm/v1.0/soa-rm.html)
for using capabilities across ownership boundaries; [Richards, Software Architecture Patterns, chapter 3 (2015)](https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/ch03.html)
for core/plugin organization; and [Fowler's Microservice Trade-Offs (2015)](https://martinfowler.com/articles/microservice-trade-offs.html)
for modularity benefits and distribution costs. These are historical explanations, not evidence that one style
is today's general winner. The current [VS Code extension-host account](https://code.visualstudio.com/api/advanced-topics/extension-host)
shows why plugin execution location and runtime constraints need explicit treatment. [Sidecar guidance](https://learn.microsoft.com/en-us/azure/architecture/patterns/sidecar)
answers the separate companion-process placement question.

The selected synthesis keeps a simple candidate, tests consequential changes, and separates state, execution,
module and release boundaries. Its advantage over a style catalogue is an inspectable reason for the choice;
its cost is tracing actual behaviour and change. Reopen it when a newly relevant workload, invariant, extension,
provider or operating capability changes that comparison. Detailed software design remains a specialist task.

### SYSE.6:12 - Relations

- `SYSE.5` describes how to produce explicit allocation choices and conflicts. Practitioners using `SYSE.6`
  recheck a compatible result's subject, configuration, horizon, evidence, and conditions before using it as a
  candidate-set input; generation does not select.
- A compatible `SYSE.8` account can supply provider-arrangement constraints that change this architecture
  decision. Recheck its subject, configuration, use, horizon, evidence window, and availability. If it does not
  fit, use a qualified direct source or record the missing result. Keep the described offering or arrangement,
  provider Systems, performed Work, consequences, responsibility, and authority as distinct objects.
- A compatible `SYSE.7` account or `SYSE.10` assessment supplies evidence only when it can change this decision
  at the same configuration and horizon. A compatible `SYSE.9` account supplies a specialist result for its
  receiving question and conditions. During decision Work, a conditional `SYSE.9` request names the question,
  subject, conditions, authority, and desired result. Evidence and specialist results inform the choice; the
  decision subject retains the authority to make it. If an input does not fit, use a qualified direct source or
  record the missing result.
- `C.32.PAD` supplies the decision relation and the distinction among selected option, affected structures,
  Method and Work consequences, publication projection, and reopen conditions. `C.32.ACS` defines criteria rows;
  `C.32.ACE` defines eval programs and results; direct comparison and choice patterns govern their own claims.
- `SYSE.6` can supply selected-structure constraints and reconsideration conditions to `SYSE.3`, `SYSE.13`,
  and `SYSE.18` when they constrain the receiving design choice. The Agent performing each receiving Work
  applies its Method to generate and compare that Work's own alternatives and checks subject, configuration,
  horizon, and compatibility. If the decision result does not fit, use a qualified direct source or record the
  missing result.
- Practitioners use `SYSE.4` in assurance Work to qualify the engineering decision or identify the basis it
  still lacks. That assurance result is separate from architecture selection and from later acceptance,
  permission, release, and observed use success.
- `C.32.ADR`, `C.30.AD`, `E.17`, and `E.24.PUB` govern decision projection, architecture description,
  source-backed publication, and audience availability. A current decision can exist without one particular
  file, and a file can persist after the decision is superseded.
- Application DPFs retain the subject-specific architecture Methods and safeguards needed for the
  engineered System's profile.

### SYSE.6:End
