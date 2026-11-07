## SYSE.5 - Develop an Engineered System's Functional Organization and Bearer Alternatives

> **Status:** Stable

### SYSE.5:0 - Use This When

Use this pattern when engineers can name a desired outside effect, use situation, or observed functioning
failure, but have already treated one familiar bearer cue—for example, a component, product, service, software
partition, or supplier offering—as the only candidate. Use it also when a functional diagram exists but no one
can show which actual Systems or intended System referents could bear the contributions named by its claims under
decision-relevant conditions—for example, operating, interface, placement, integration, or assurance conditions.

The first result is an **account that compares several functional organizations with the Systems and
interfaces that could realize them**. It records proposed many-to-many allocations, the conditions under which
each proposal could work, conflicts among proposals, evidence limits, and the first unsupported dependency.
It is a proposal for later architecture selection. Realization, integration, and observed performance require
their own work and evidence.

**First move.** In one sentence, name the required outside effect, the current decision question, and the first
familiar bearer assumption. Add one materially different way in which the contribution might instead be borne. If no
bearer or allocation choice is current, stop and use `A.6.F` for the function-like claim.

Use this pattern while an allocation choice can change an engineering decision. For one function-like
claim, use `A.6.F`; for one module or interface claim, use `A.6.M`; for transdisciplinary candidate synthesis
across several structures, use `C.32`; and for choosing an architecture from developed alternatives, use
`SYSE.6`. When a subject-specific Method—for example, one for physics, software semantics, clinical action,
electrical protection, or structural integrity—determines the answer, use the relevant application DPF with this
allocation account.

For software allocations, `SYSE.6:4.4` explains how layers, pipelines, plugins and service arrangements
change the candidate mechanisms and consequences to compare. Use that repertoire while developing
alternatives; the style name itself supplies no allocation or performance result.

#### SYSE.5:0.1 - Terms and Distinctions

| Name in this pattern | What it denotes |
| --- | --- |
| required outside effect | A claim about a change or preserved condition needed in a named receiving System under stated use and operating conditions. Actual occurrence of that effect needs separate evidence. |
| functional contribution claim | A function-like claim recovered through `A.6.F`: it names a predicate, a possible bearer, conditions, and the larger effect or functioning to which the contribution matters. A label such as *sense*, *control*, *store*, or *protect* is only a source cue until those positions are recoverable. |
| functional organization | A selected structure of required effects, functional contribution claims, and relations among them for a named System and use. Its description states what is proposed or supported; an account of actual functioning needs its own evidence. |
| candidate bearer | An actual System considered for a contribution, or an intended System referent in a proposal. Identify the proposed contribution and the System that could bear it. |
| constructive organization | A selected structure of actual Systems and relations such as parthood, connection, or placement, with decision-relevant modules and physical interfaces. Candidate content can propose such a structure before it exists. |
| interface specification | A statement of conditions for interaction across a boundary between named participants: for example, exchanged quantity, units, geometry, protocol states, timing, capacity, error handling, or effectivity. Identify actual connectors, conduits, interactions, and compatibility evidence separately. |
| proposed function-to-bearer allocation | A proposal associating one or more functional contribution claims with one or more candidate bearers for stated use, conditions, configuration, and horizon. Ground actual assignments, performed work, demonstrated capability, and actual functioning separately. |
| bearer-and-interface proposal | One linked candidate functional organization, constructive organization, proposed allocations, interface specifications or gaps, operating conditions, and predicted consequences. |
| materially different alternative | A proposal whose physical principle, distribution, placement, containment, redundancy, control boundary, interface grammar, realization dependency, or other selected structure can change the answer to a named decision question. Renaming the same arrangement or changing only drawing notation does not create another alternative. |
| allocation conflict | An explicit incompatibility between claims that cannot be satisfied together under the same conditions, or a protected loss created by one proposal. The account names the affected claims, Systems, characteristics, and conditions. |


Words such as *functional block*, *module*, *service*, *component*, *agent*, *sensor*, *platform*, and *open
interface* do not establish a common kind. Restore their subjects and relations before using them in an
allocation proposal.

### SYSE.5:1 - Problem Frame

An engineered System participates in a use situation through interactions under stated conditions. A desired outside effect can often
be produced by several functional organizations, and one functional contribution can often be borne by several
Systems together. Conversely, one System can bear several contributions in one configuration and different
contributions in another. Distribution can change, for example, across operating modes, failure states, product
variants, sites, and time.

The engineer therefore needs more than functional decomposition and more than a component search. The working
result links functional and constructive candidates to their outside use, proposed allocations, interface
realizations, placement, integration dependencies, and evidence. The result table below states its required
content. These selected structures answer different questions and need explicit correspondence where the decision
depends on them.

### SYSE.5:2 - Problem

Starting from the incumbent construction makes familiar parts look necessary. Starting from a functional graph
alone makes abstract elements look like purchasable or assignable things. A supplier search can then be mistaken
for proof that the proposed functioning is feasible, while an unsuccessful search can be mistaken for proof
that no bearer is possible.

The result is an allocation that survives on paper but fails in use. For example, a bearer may lack power,
capacity, placement, access, timing, environmental tolerance, or realization support. Two nominally conforming
interfaces may fail to interoperate. Several Systems must cooperate but their joint contribution and failure
handling are absent. A standard connector admits a damaging wrong connection. A general-purpose supporting
System can reduce one development burden while increasing, for example, latency, energy use, certification Work,
or continuing-change burden. Procurement and Work are
then organized around functional labels before actual supply items, assembly relations, and evidence needs are
known.

The opposite failure is endless decomposition and candidate generation. The engineering account is useful only
when it exposes alternatives and conflicts for a named decision question and stops at the first unsupported
feasibility dependency.

### SYSE.5:3 - Forces

The move must manage these recurring tensions:

- Reusing an incumbent construction saves effort, while it can hide a better physical principle or distribution.
- Functional abstraction protects solution freedom, while abstract labels can conceal, for example, physics,
  operating conditions, or joint bearer requirements.
- A general-purpose bearer can absorb several contributions, while specialization can improve, for example,
  performance, safety, energy use, evidence production, or fault containment.
- Standard interfaces can reduce coordination cost, while compatibility, integration, substitutability, and
  correct-use claims still need their own grounds.
- More alternatives preserve option value, while every alternative adds Work—for example, modeling, specialist
  analysis, comparison, or evidence production.
- Early quantitative estimates help eliminate infeasible candidates, while premature precision can hide
  unknown models, wrong subjects, or unsupported measurements.
- AI-assisted generation can widen a functional candidate set quickly, while bearer-feasibility and
  project-correctness claims still need project evidence.
- Engineering Work must proceed under incomplete knowledge, while each commitment—for example, purchase,
  realization, integration or release—needs grounds appropriate to its consequences and conditions.
- Selected structures—for example, functional, constructive, placement, control, information, configuration,
  and evidence structures—constrain one another while each answers its own engineering question.

### SYSE.5:4 - Solution

Develop several functional organizations and materially different bearer-and-interface proposals together. Enter
at the claim that blocks the current decision, keep the outside effect and use visible, and iterate between
functional and constructive accounts. Make every allocation, interface condition, conflict, evidence limit, and
decision-relevant consequence explicit. Use `C.32` for the general multi-structure candidate palette; apply the
Systems Engineering content below to make that palette usable for realization, integration, procurement,
assurance, and continuing change.

#### SYSE.5:4.1 - Perform the Move

1. **Bind the engineering decision.** Name the actual System or intended System referent whose functioning and bearer alternatives are under consideration, the decision, use situation, required outside effect or observed failure, configuration, operating envelope, horizon and protected characteristics. For a creator, state the products or classes of use that ground its required contribution; its own functions and construction remain the subject here. Use `SYSE.2` candidates and unresolved use–System mismatches when
   they are current and compatible; otherwise use a qualified direct source or record the missing result.
2. **Restore the blocking function-like claims.** For each material contribution, use `A.6.F` to state the
   predicate, possible bearer, receiving whole or effect, conditions, and claim status. Begin from outside use,
   an observed internal failure, a candidate construction, or a feasibility result as the current question
   requires.
3. **Develop several functional organizations.** Construct how contributions cooperate to produce the required
   outside effect, using §4.1.1 when that connection is not already clear. Vary that organization together with
   its possible bearers. Include decision-relevant situations—for example, operating, degraded, maintenance,
   recovery, or consequential foreseeable use. A tree is optional; use the representation that reveals the
   material transformations, exchanges, states, feedback, or mode-dependent relations.
4. **Generate materially different bearer arrangements.** Start with actual or intended Systems that might
   carry the contributions. For each arrangement, state how each candidate System would be obtained and operated—
   for example, by using an available System, procuring or realizing one, relying on provider Work, or combining
   software and physical Systems. Record shared resources and changes to supporting Systems as dependencies
   unless they themselves carry a contribution. Vary decision-relevant structures—for example, physical principle,
   distribution, placement, redundancy, containment, control boundary, or interface grammar. State separately
   whether an actual System exists, whether it is procurable, what realization or provider Work is needed, and
   which candidate claim still lacks support.
5. **Write many-to-many proposed allocations.** Associate functional contribution claims and candidate bearers
   explicitly. Permit several bearers for one contribution, several contributions for one bearer, and different
   allocations by mode, use, configuration, place, or effectivity. Treat weak cues—for example, co-location,
   matching names, diagram overlap, product kind, ownership, or system-role assignment—only as possible evidence
   for a separately stated claim.
6. **Develop interface and placement conditions.** For every material interaction, state the boundary and
   participants. Add the conditions that matter to the decision—for example, exchanged quantity or signal,
   units, geometry, protocol states, timing, capacity, environment, error handling, configuration, and
   effectivity. Identify the physical realization or missing realization separately from the interface
   specification. Add decision-relevant constraints—for example, placement, access, assembly, maintenance,
   supply, or resource constraints—when they change feasibility.
7. **Challenge intended and unintended interaction.** Test the proposed arrangement against relevant cases—for
   example, loads, failures, swaps, reversals, stale configuration, unavailable resources, human or machine
   misuse, and external change. For consequential wrong use, compare candidate changes—for example, to geometry,
   keying, protocol, control, detection, containment, or operation. Test evidence supports a mitigation claim only
   for the tested interaction and conditions.
8. **Check realization and integration dependencies.** Identify each dependency needed to make and join the
   bearers—for example, a System, Method, capability, resource, service, assembly Work, configuration episteme,
   or specialist result. Record each dependency with its own kind and relation to the proposal. Distinguish a missing catalogue
   item from a missing physical principle and from a missing project capability. When a recursive realization
   dependency is current, use `SYSE.3` to develop it; do not hide it in a module name.
9. **Compare engineering consequences.** For each proposal, state predicted gains, losses, and unknowns for the
   current decision. Compare proposals for the engineering concerns that matter, such as performance, energy,
   safety, security, fault containment, latency, placement, service access, manufacture, assembly, integration,
   supply, cost, configuration, changeability, evidence burden, and affected-System consequences. Express each
   comparison through a characteristic with an explicit subject, conditions, Scale, and comparison frame.
   Bring in specialist Methods for the actual physics and risks.
10. **Examine a representative slice.** Use available evidence that supports the present claim under the needed
    representative conditions. When further challenge Work could change the decision, use `C.11.DUA` and the
    applicable `C.11` or specialist experimental-design Method to decide whether to obtain it, comparing its
    attainable contribution with the whole burden. For selected Work, choose the Method suited to the claim—for
    example, computation or simulation, prototype-building and testing, or a physical trial. For an analysis
    or trial whose result is relied on, identify the performed work, its performer and Method, configuration
    and conditions, observations, and claim limits. A model, simulation result, or trial observation remains
    an input to later claim assessment; its form alone does not establish feasibility of the whole proposal.
11. **State the decision use and local stop.** Record which alternatives remain usable, were revised, combined,
    or rejected; record the reasons, protected losses and dependencies that block the receiving commitment. When an architecture
    decision is current, use this account as an input to the Work governed by `SYSE.6`. When no admitted bearer
    can satisfy a sound contribution, choose explicitly among another bearer, a changed functional organization,
    new realization or supporting-System capability, bounded exploratory Work, or stopping the current proposal. Pause
    only the commitment whose basis is missing.

Revisit these questions in the order that helps answer the current decision. Functional reasoning,
construction search, realization, integration, and testing can overlap and recur. A claim's reliance on another
result does not require all work producing that result to finish before work on the dependent question starts.

##### SYSE.5:4.1.1 - Construct the Joint Functioning

For a decision-relevant use, build one connected explanation of how the proposed interactions produce the
outside effect. Begin with an existing arrangement when it supplies a useful starting point; its parts are
candidates, not limits on what can be constructed. The following questions connect functional reasoning with
bearer choices.

**Work back from the effect to what must happen.** Identify the receiving System, the condition to change or
preserve, and what must reach or act on it. Recover the relevant inputs and initial states: for example,
available energy, material, information, permissions, or a prior operating state. Ask what transformation,
transfer, decision, or maintained interaction could connect them to the effect. Follow each needed intermediate
result back to a possible producer or available source. This exposes cooperating contributions; it does not
require decomposing every function to a uniform depth.

**Make the cooperation possible.** Connect what one contribution produces to what another needs, retaining
the identity and relevant properties of what passes between them. Distinguish an exchange from a condition
for starting, continuing, or stopping an operation. State where contributions must coexist, synchronize, wait,
or feed back, and what changes with the operating mode. If two inputs must meet, explain the operation that
combines them and how candidate bearers could perform it. If production and use occur at different times,
identify what preserves the needed material, energy, information, or state between them.

**Reason forward through one complete use.** Starting from the available inputs and states, explain what
each cooperating contribution changes, what becomes available next, and why the receiving System would obtain
the required effect. Use relevant domain relations: energy and material balances, a valid data transformation,
or an operating rule, for example. Include simultaneous contributions where the effect depends on them.
Check that the account has no required input without a source, unavailable initial state, incompatible
handover, or unexplained jump from individual contributions to the whole effect. State assumptions that still
need support. A coherent conditional explanation is a candidate for investigation, not observed functioning.

If automated numerical planning can help, supply compatible initial states, goal conditions, and permitted
quantitative transformations with their units and constraints. Use the generated arrangement only within
that model's scope. A failed or timed-out search leaves the modeled search question unresolved unless its
result establishes more; it does not show that no physical arrangement is possible. §11 compares this branch
with construction that begins from less complete information.

**Change a relation together with its possible realization.** Try a different physical principle, move a
transformation, retain a resource for later use, distribute a decision, or change which interactions continue
during failure. Follow the changed relation forward to the outside effect and back to its required inputs.
Revise the affected bearer and interface proposals, state what still works unchanged, and expose new
dependencies. If no credible means of producing a required intermediate result is known, keep that gap
open and use specialist development or the local return in step 11.

Choose a representation that exposes the difficult relation:

| When the decision depends on... | Make this visible |
| --- | --- |
| Transfer, conversion, accumulation, or loss | A flow account with the quantities and conditions needed to relate inputs, intermediate states, and outputs. |
| Permitted behavior in different situations | States, triggering conditions, transitions, and what remains available in each state. |
| Several participants cooperating | Exchanges, ordering or concurrency, and the conditions under which participants can use one another's results. |
| Regulation or coordination through feedback | What is observed and actuated, how decisions affect the plant, and the assumptions between control functions. |

These are choices for the current question, not four required diagrams. A short explanation can suffice;
combine representations only when one hides a consequential relation. A control-layer split is also not a
physical containment hierarchy. When reliance depends on stability, response bounds, capacity, or another
specialist property, obtain the relevant domain construction and evidence; use `C.30.LCA` for the conditions
of a relied-on layered-control view. This pattern does not derive a controller or establish physical
adequacy from the organization alone.

#### SYSE.5:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| bounded use | Project System or intended referent, decision question, outside effect or observed failure, use situations, configuration, operating envelope, horizon, and protected characteristics. |
| functional alternatives | Several candidate functional organizations, or a justified smaller set; each explains how its contributions and interactions jointly produce the outside effect from the relevant inputs and states, under stated conditions and modes, with unresolved causal or functioning claims explicit. |
| bearer-and-interface alternatives | Candidate actual Systems or intended referents, obtaining or proposed constructive and placement structures, interface specifications and physical realizations or gaps, separate existence, procurement, provider-Work, and realization claims, and materially distinguishing principles. |
| proposed allocations | Explicit many-to-many function-to-bearer associations qualified by use, conditions, configuration, place, mode, and effectivity; actual functioning is grounded separately. |
| feasibility and conflict | Capability needs, loads, margins, resources, placement, realization and integration dependencies, wrong-use cases, conflicting characteristics, supported and unsupported claims, and first unsupported dependency. |
| evidence boundary | Models, sources, analyses or trials relied on; for performed analysis or trial work, its performer, Method, configuration, conditions, observations, uncertainty, and the claims those observations do and do not support. Retain source editions where the claims depend on them. |
| decision use and local stop | Alternatives retained, revised, combined, or rejected; reasons and protected losses; the decision question and architecture-decision Work that can use the account; and the unsupported commitments to pause or proposals to stop. |

The account can use several linked representations. Each representation names the functional organization,
constructive organization, or engineered System it describes, and the account states the correspondence among
those subjects.

#### SYSE.5:4.3 - What Changes in Practice

Engineers stop asking which named component implements each box and start asking which materially
different arrangements can produce the required outside effect under the actual use conditions. They no longer
treat functional names as purchase items or procurement specifications. Interface standards become inspectable
specifications and evidence questions. Failed feasibility reopens the affected functional or bearer claims instead of
silently collapsing the candidate set or restarting the whole project.

### SYSE.5:5 - Worked Case: Heat-Pump Plant Control and Protection

An occupied building has a heat-pump plant whose controller must respond to electricity-price and grid-flexibility
signals while maintaining room comfort and protecting compressors. The engineering team must choose a control
architecture for plant configuration `HP-2` that remains useful for the next three heating seasons. Earlier
concept-development Work produced two viable use/System concepts and one unresolved mismatch: centralized
optimization improves plant coordination, but communication loss must not remove local protection.

During allocation Work, the engineers restore four contribution families as claims whose bearer arrangements
remain to be chosen:

- modulate heat production against building demand under temperature, occupancy, tariff, and plant conditions;
- keep compressor pressure, temperature, cycling, and flow within protected limits;
- accept, validate, and act on external price or flexibility signals within declared timing and authority;
- retain local safe operation and recover state after communication, sensor, or controller failure.

They develop three materially different proposals:

1. A central building controller carries demand estimation, optimization, dispatch, and most protection logic;
   unit controllers provide actuation and a small emergency stop.
2. Local unit controllers carry protection and normal regulation; a supervisor sends bounded set-points and
   coordinates units, while loss of the supervisor leaves a declared local operating envelope.
3. Thermal storage and a tariff scheduler carry most time-shifting; local controllers retain protection and
   regulation, so grid response is split across storage, scheduler, drives, sensors, and plant state estimation.

To construct proposal 2, the team works back from room comfort. In this case the rooms receive heat through
water-fed emitters. Maintaining the selected room condition therefore requires heat delivery that can meet the
building's changing loss, a circulating water path, and suitable water conditions at the emitters. The heat
pump must transfer energy from its source, with electrical input, to that water circuit. This identifies a
cooperating thermal path before deciding which controller should carry each decision.

The team then connects regulation to that path. Room and water observations support an estimate of demand;
unit-state observations delimit the operating capability. A valid price or flexibility request can change
the supervisor's requested operating point within those limits. The local controller accepts a compatible
request and regulates the unit using local observations. Local protection can restrict or stop actuation
when a protected condition would be violated. Heat delivery requires the thermal source, electrical supply,
circulation, emitters, and admissible actuation to work together; issuing a set-point alone cannot produce
the outside effect.

In normal operation, a change in room demand can alter the requested and locally accepted operating point,
which changes heat transfer and subsequent room observations. Price information influences that choice but
does not replace the heat demand or the protection condition. During communication loss, the proposed local
mode continues regulation only from information and authority available locally; an unavailable remote
request cannot remain a required input. If local conditions permit protection but insufficient heat delivery,
the result is protected operation with reduced comfort, not satisfaction of the whole original requirement.
The team must expose that loss to the architecture decision.

Now change the relation between heat production and room delivery. Proposal 3 inserts thermal storage:
the plant can charge it when permitted, while the distribution circuit can draw stored energy later.
The scheduler consequently needs an estimate of usable stored energy and the permitted charge and discharge
conditions, as well as demand and external signals. Local protection and the heat-delivery path remain
necessary. What changes is the timing dependency: current delivery can depend on an earlier charge rather
than simultaneous compressor operation. Storage, sensors, valves, and circulation must realize that changed
relation.

For this candidate the team assumes a storage capacity and discharge rate adequate for a stated flexibility
interval. It still needs a thermal/hydraulic account that covers losses, usable temperature range and room
demand, together with storage-cycling evidence. If those conditions fail, the intended time-shift is
unsupported: shorten the interval, change the storage or operating proposal, or retain proposal 2. The
functional requirement and the local-protection contribution survive that return. Control behavior and
physical margins require their specialist analyses and trials before reliance. This is a worked candidate
construction, not a qualified plant design.

The functional contribution claims and candidate bearers are not one-to-one. Protection is distributed across
software, local electronics, sensors, drive limits, valves, and physical pressure relief. Grid response depends
on the supervisor or scheduler, communication bearer, storage state, unit capability, and operating permission.
Every bearer entry identifies an actual System or intended referent and its proposed allocation. A model-box
label such as *protection* or *optimization* is only a cue for recovering those claims.

The interface account separates signal semantics, units, timestamps, command validity, latency, state quality,
fallback behavior, configuration identity, and physical connections. The team separately tests rejection of stale
commands, agreement of sensor units, local fallback behavior, and the integrated plant contribution. Simulation
Work challenges thermal and tariff behavior; Hardware-in-the-Loop Work
challenges timing and fallback; a bounded plant trial challenges actual integration. Each produces observations
with different claim limits.

An AI coding Agent proposes a fourth function graph and controller split. That Agent and the engineers perform
candidate-generation and criticism Work; the generated graph is a description candidate. It enters the
account only after its functional claims, candidate bearers, interface assumptions, and unsupported physical
dependencies are recovered.

The account retains proposals 2 and 3 and rejects proposal 1 because its local protection split cannot satisfy
the declared communication-loss condition. It also records one unresolved storage-cycling evidence need. The
two alternatives, allocation conflicts, predicted losses, and conditions for revisiting the decision become
inputs to architecture-decision Work governed by `SYSE.6`.

#### SYSE.5:5.1 - Small Wrong-Use Check

A service machine uses one lubricant cartridge and one cleaning-solvent cartridge. Cross-connection damages
seals. The engineer states the two fluid-delivery contributions and service conditions, then compares candidate
cartridges, ports, seals, and connection arrangements. The retained proposal uses mechanically distinct keyed
couplings whose materials and geometry fit the relevant fluids, pressure, assembly, and service conditions.

The check attempts every intended connection and the consequential swapped connections under the declared
conditions. A colour label is a cue, not evidence that cross-connection is impossible. If an intended connection
fails or a damaging swap remains possible, the allocation and interface proposal reopens. The resulting observations can support claims only about the tested configurations and wrong-use
cases.

### SYSE.5:6 - Biases to Watch

Three recurring biases matter here. **Incumbent-form bias** lets a function tree, current parts, or a supplier
catalogue determine the candidate architecture; start from the required effect and compare materially different
arrangements. **Conformance-label bias** lets an interface name, standard, or certificate replace project evidence;
state the interface claim and test it under the relevant conditions. **Fluent-generator bias** lets a plausible
human- or AI-generated graph outrun bearer physics; recover the claims, Systems, and unsupported dependencies.


### SYSE.5:7 - Conformance Checklist

| ID | A conforming use... |
| --- | --- |
| `CC-SYSE5-1` | names the actual System or intended System referent selected for engineering, decision, use, configuration, operating envelope, horizon and required effect or failure; for a creator, preserves the product-use grounds of its required contribution. |
| `CC-SYSE5-2` | restores function-like claims through their predicates, possible bearers, conditions, and receiving effects rather than relying on functional labels. |
| `CC-SYSE5-3` | develops materially different functional and bearer-and-interface alternatives or justifies a smaller decision-sufficient set, explaining how the cooperating contributions would produce the required effect and what changes between arrangements. |
| `CC-SYSE5-4` | keeps functional organization, constructive organization, placement, Work, Method, descriptions, and evidence distinct. |
| `CC-SYSE5-5` | states many-to-many proposed allocations with use, mode, configuration, place, and effectivity where they change the decision. |
| `CC-SYSE5-6` | separates interface specifications, physical realizations, connections, interactions, and compatibility evidence. |
| `CC-SYSE5-7` | challenges consequential load, failure, integration, and wrong-use cases using available evidence, states its supported and unexamined boundaries, and selects further Work only when its attainable contribution warrants the whole burden. |
| `CC-SYSE5-8` | states separately whether an actual System exists, whether it is procurable, what realization or provider Work is needed, and which candidate claim remains unsupported. |
| `CC-SYSE5-9` | names each decision-relevant dependency by its own kind and relation to the proposal. |
| `CC-SYSE5-10` | makes alternatives and explicit conflicts usable by named architecture-decision Work and records selection and realization as separate Work and claims. |

### SYSE.5:8 - Common Failures and Repairs


| Failure | Symptom | Repair |
| --- | --- | --- |
| Incumbent-parts decomposition | The current bill of materials becomes the functional organization. | Restate the outside effect and develop rival functional organizations before preserving the incumbent allocation. |
| Functional element as purchase item | A box named *sensor*, *protection*, or *storage* is treated as a procurement specification or purchase item. | Recover the function-like claim, candidate actual or intended bearer, interfaces, placement, capability need, and assembly relation. |
| One-to-one allocation | Every contribution is forced into one component and every component into one contribution. | Permit many-to-many and mode-dependent proposals; inspect joint and shared functioning. |
| Diagram overlap as relation | Matching labels or co-located symbols establish identity, allocation, or functioning. | State the direct claim and supporting evidence; keep representation correspondence separate. |
| Interface label as proof | *Standard*, *open*, or a connector name establishes compatibility or substitution. | State interface conditions and test conformance, integration, intended interaction, and consequential wrong use separately. |
| Available product as only candidate | Catalogue availability is treated as the boundary of possible construction. | Keep physical candidate generation separate from the choice of obtaining arrangement; use `SYSE.24` when that obtaining choice becomes current. |
| Unavailable product as no construction | An unsuccessful search erases candidate bearer descriptions already examined. | Retain the candidates and failure reasons; distinguish market absence, physical infeasibility, and missing project capability. |
| Fewer bearers as automatic improvement | Consolidation or a universal platform is assumed superior. | State transferred contributions, affected characteristics, scale window, losses, and evidence burden; keep it as one candidate. |
| AI graph as design truth | A generated function graph is accepted because it is connected or plausible. | Recover claims and bearers, challenge physical and interface dependencies, and qualify the generator and evidence. |
| Trial as universal proof | One simulation or bench result establishes full functioning and architecture adequacy. | State the Agent, Method, conditions, configuration, observations, claim limits, and the later claim-assessment Work that can use them. |
| Architecture decision hidden in generation | The preferred candidate is silently selected during modeling. | Preserve the decision-usable candidate account, including explicit losses and unresolved claims, as an input to architecture-decision Work governed by `SYSE.6`. |
| Whole-project stop | One missing bearer blocks every Work stream. | Pause only the unsupported commitment; select another bearer, revise the function, change realization capability, explore, or stop the bounded proposal. |

### SYSE.5:9 - Consequences

Engineers gain alternatives that can survive contact with physical realization, integration, procurement, and
operation. Functional freedom remains tied to stated bearer claims and use conditions. Supplier
claims and AI-generated candidates become inspectable inputs. Wrong-use cases, interface gaps, unallocated
contributions, and unsupported realization dependencies appear early enough to change the architecture choice.

The cost is maintaining correspondence among several selected structures and qualifying claims by use,
configuration, and evidence. Candidate diversity also costs modeling and specialist Work. Those costs are bounded by the decision question and stop rule: stop with decision-sufficient alternatives and
the first unsupported feasibility dependency.

### SYSE.5:10 - Rationale

FPF already explains functions, structures, modules, interfaces, candidate synthesis, and architecture choices.
Apply these to engineering by keeping the required outside effect and use visible while engineers iteratively
develop functional organizations, actual or intended bearer arrangements,
many-to-many allocations, physically meaningful interfaces, realization dependencies, wrong-use challenges,
and bounded evidence use for one engineered-System decision. Procurement, realization, assurance, and continuing
engineering Work need those constructive and integration details.

### SYSE.5:11 - SoTA and Source Use

**Working question.** How can an engineer construct and vary the joint functioning that could produce a
required outside effect, while keeping bearer, interface, and realization choices usable for the next
architecture decision?

The selected answer is the synthesis in §4.1: construct a cooperating arrangement from relevant inputs and
states, reason through its effect, and vary its relations together with possible bearers. Preserve unknowns
where the decision can proceed conditionally; return a missing physical or operational contribution to its
actual producer. §4.1.1 supplies that connection and §5 works it through a changed timing dependency.

A serious alternative is the enhanced sequence diagram of [Yildirim and Campean (2020),
§§3–4.3](https://doi.org/10.1007/s00163-020-00343-8). It already connects functional flows with possible design
elements and supports changes to an existing arrangement. **Adapt** its treatment of transformation,
transmission, and joining conditions in §4.1.1; use the fuller ESD when a systematic flow representation is
needed. SYSE.5 makes representation conditional and carries the construction into alternative allocations,
obtaining arrangements, evidence limits, and local return. Compared with developing one ESD arrangement,
that adds comparison and realization work. The gain is that the next decision can distinguish
different ways of obtaining the effect and the unsupported dependency of each. The heat-pump case supports
this conditional reasoning; it establishes neither measured effort savings nor general superiority.

For a compatible quantified problem, [Rosenthal, Heesch, and Niggemann (2026),
§§3–5](https://doi.org/10.1017/pds.2026.10437) offers a serious numerical-planning alternative.
The cited formulation is linear; inherently nonlinear couplings such as pump or fan flow losses fall outside
it. Before choosing the method, check that the relations needed for the decision fit this boundary. For an
unsupported relation, justify a linear approximation for a stated operating range and error tolerance, with
evidence adequate for the intended decision, or use another Method with its own applicability and evidence
limits. Otherwise leave the affected quantitative conclusion unsupported.
**Adapt** the cited method's explicit states, goal conditions, and admissible quantitative transformations for the optional
automated branch in §4.1.1. Its two cases demonstrate model-level consistency, with results dependent on the
specified problem and search; they do not qualify this plant or every realization. Preparing that model costs
work. Prefer the branch when its consistency checks or search can change the decision and the requisite model
can be supplied. **Reject** making that formalization a prerequisite for every early alternative: unresolved
operating concepts may first need the joint reasoning and specialist inquiry described here. This choice
accepts less automatic assurance in exchange for useful conditional development with incomplete inputs.

The constructive connection and its realization/decision use are this pattern's authored synthesis. The
sources below support particular premises and limits, with their dispositions stated at that scope.

| Source line and role | Use here | Epistemic boundary |
| --- | --- | --- |
| [Eisenbart, Gericke, and Blessing 2017, §4.7](https://doi.org/10.1007/s00163-016-0242-3): evidence against a single function-model purpose | **Adopt** the distinction among modeling purposes and connected function/solution reasoning; §4.1.1 chooses representation for the consequential relation. | The ten-company exploration reports heterogeneous practice and collaboration gains; it does not establish controlled general effectiveness or one best notation. |
| [She, Belanger, and Bartels 2024, Abstract and §5](https://doi.org/10.1007/s00163-024-00434-w): bounded decomposition and metric alternative | **Adapt** exploratory decomposition as a way to generate candidates; **reject** a decomposition metric as sufficient grounds for selecting a bearer organization in steps 3 and 9. | The preliminary metrics, simple examples and subjective benchmark leave semantic coverage and its cost material. Decomposition quality alone does not decide the engineering consequences. |
| [Monetti, Lundström, and Maffei 2025](https://doi.org/10.1080/21693277.2025.2566066) and [Grønvald et al. 2026, §§4–5](https://link.springer.com/article/10.1007/s11740-025-01412-4): assembly consequences and evidence of data limits | **Adapt** early assembly consideration and **adopt** explicit economic/data limits in steps 8–9. | The bounded assembly and company evidence does not establish general modularity benefit, cost reduction, substitutability, or Method dominance. |
| [Haddad and Seibel 2025, §§3.3–4.2 and §5](https://doi.org/10.1017/pds.2025.10205) | Supports AI-assisted generation and iterative refinement of candidate function structures. | In the automated graph evaluation of 50 products, GPT-4o + MCTS-FD produced 42% of outputs without errors detected by the study's semantic/structural checks and 72% without disconnected components. The graduate-student comparison was a separate qualitative study. Non-functional requirements, domain interdependencies, physical effects, and principal solutions remained outside the demonstrated result. These graph metrics support the bounded generation use; project correctness, bearer feasibility, and architecture selection require project evidence. |
| Current FPF `A.6.F`, `A.6.M`, `A.22`, `C.30`–`C.32`, representation, comparison, evidence, and assurance patterns: governing distinctions and general synthesis | **Adopt** the distinctions and **adapt** the candidate palette to the engineering use in §4.1 and §12. | These contributions constrain claims, structures, interfaces and candidate use. The engineering construction and its subject-specific adequacy still need the explanation and domain grounds required here. |

For the AI-generation branch, **adapt** generated graphs as proposals to examine; **reject** using graph
connectivity or a study score as bearer-feasibility evidence. This is the boundary applied to the fourth
proposal in §5.

Reopen the selected construction when a credible rival produces equally usable alternatives and local returns
at lower total effort, when an actual use exposes a missing cooperation relation, or when a changed problem
makes the quantitative branch newly useful or inadmissible. Reopen only the dependent allocation, interface
test, AI-use boundary, or assembly/economic claim when its source or use conditions change.

### SYSE.5:12 - Relations

- When compatible, practitioners can use linked use/System candidates and unresolved mismatches from a
  `SYSE.2` result as inputs. They must still check the subject, configuration, horizon, evidence, and compatibility
  before developing the alternatives in this account.
- Use `A.6.F` to restore each function-like claim and possible bearer. `A.6.M` governs module and interface
  claims; `A.22` and `C.30` govern selected structures and architecture relations. Applying those patterns alone
  does not produce the Systems Engineering allocation account defined here.
- Use `C.32` for general multi-structure architecture-candidate synthesis: vary selected structures and retain
  their gains, losses, and next use. SYSE.5:4.1.1 develops the engineering connection from required effect to
  cooperating contributions and possible bearers; the remaining move supplies physical interfaces, realization,
  integration, wrong-use challenge, and decision use. Reuse a C.32 palette when its subject and content fit this
  question. For a relied-on layered-control view, `C.30.LCA` supplies its interlayer conditions; it does not
  prescribe a universal number of layers or replace specialist controller design.
- The allocation-alternative account is an input to architecture-decision Work governed by `SYSE.6`. That Work
  may produce a chosen architecture and conditions for revisiting it. Candidate generation in `SYSE.5` does not
  select the architecture.
- When an unsupported realization or build-the-builder dependency, evidence claim, description-correspondence
  problem, or assurance question is current, apply `SYSE.3`, `SYSE.10`, `SYSE.7`, or `SYSE.4` respectively to
  its own subjects and sources. The realization dependency, evidence claim, description-correspondence problem and assurance question concern different engineering subjects and need their own supported answers. The same Work may supply several answers if each meets its receiving question's conditions. A description ensemble remains distinct from candidate Systems, allocations,
  interfaces, and the selected architecture.
- Practitioners can reuse a compatible `SYSE.5` result in `MDPE.3` when an engineered instrument,
  robot, hybrid body, venue, or software System is itself an architecture subject in the performing whole. Recheck
  the reused result against the MDPE subjects, authority, conditions, evidence, and current music-and-dance
  sources.
- Agents performing downstream application Work—for example procurement, manufacturing, configuration,
  maintenance, operations, software, electrical, mechanical, safety, or human-factors Work—use the result through
  their own Methods, authority, conditions, and evidence.

### SYSE.5:End
