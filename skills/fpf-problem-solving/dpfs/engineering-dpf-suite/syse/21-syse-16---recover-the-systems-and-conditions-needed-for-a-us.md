## SYSE.16 - Recover the Systems and Conditions Needed for a Use Decision

> **Status:** Stable

### SYSE.16:0 - Use This When

Use this pattern when an engineering decision concerns an actual System or intended System referent selected for engineering, but everything outside it
has been reduced to one box called *environment*, *stakeholders*, *users*, *the business*, or *the platform*.
The decision needs to know which larger Systems contain it, which other Systems interact with it, which
transformation flows and interfaces matter, and which outside conditions can change the result.

Begin with one use situation and one receiving engineering decision. Recover only the Systems, direct relations,
selected structures, conditions, evidence, and assumptions that can change that decision.

The first useful result is a **bounded engineering-use account**. It describes how an actual System participates,
or how an intended System is expected to participate, in one named use situation. The account is an episteme used
by the decision. The situation, actual Systems, containing wholes, and other obtaining relations remain its
world-side subjects.

Do not use this pattern merely to draw a context diagram or inventory every nearby object. Use the governing FPF
pattern directly when one already-known relation—such as parthood, interface, interaction, flow, or an architecture
relation—answers the question. Use `SYSE.1` when the relation between that engineering subject and the product SoI is unclear. A creator retains its own engineering-use question while serving the product use.

#### SYSE.16:0.1 - Terms and Distinctions

| Name in this pattern | What it denotes |
| --- | --- |
| engineering subject and product SoI | The actual System or intended referent examined here can be the product, a component or a creator. For a creator, retain the products and intended uses that ground its required capability. Engineering subject, product role, identity and existence are separate claims. |
| use situation | A bounded actual situation in which the System participates, or a described possible-future situation in which the intended referent would participate. A scenario or diagram is a description of that situation. |
| containing whole | An actual System of which the selected System is a proper part under a stated relation, or a possible-future whole in a proposed proper-part claim. One System can belong to several relevant wholes under different relations. |
| suprasystem | Optional source wording for a containing whole. Use it only when the proper-part claim is stated. |
| other System in the use situation | An actual System, or intended referent, connected by a named non-part relation that matters to the decision. Examples include an interaction or transfer between named Systems; observation of one System by another; access granted by a provider System to a receiving System; supply of a named result from provider to receiver; receipt or use of that result; a commitment between named Agents; or a consequence relation. Each example names its own relation. |
| operating condition | A decision-relevant condition—for example, temperature, load, connectivity, price, an applicable regulation, or an available resource. A condition is a System only when it independently meets the System criteria. |
| functional organization | Selected transformation flows, interactions, and contributions, with the actual Systems that bear or participate in them. |
| constructive organization | Selected actual or proposed parts, bearers, modules, interfaces, and connections. Establish its parthood and connection relations independently of functional contribution. |
| engineering-use account | The episteme returned here: selected Systems, relations, structures, conditions, evidence, unsupported assumptions, and reopen conditions for one use decision. |

### SYSE.16:1 - Problem Frame

Engineering choices—such as choices about System functions, architecture, interfaces, offerings, assurance,
or change—depend on larger working situations. Teams nevertheless often begin with an inside representation,
such as a product boundary, organization chart, component list, requirement set, or model repository. Outside
Systems appear only as labels around a box.

Distinguish the functional transformation and interaction, constructive parts and interfaces, boundary relations,
operating conditions and possible changes that matter to the decision. Use representations that keep these
distinctions usable.

### SYSE.16:2 - Problem

A generic environment box hides incompatible claims. A customer can own a System without operating it. An
operator can interact with it without containing it. A building can spatially contain a device while another
System whole receives the result of its functioning. A cloud service can sit outside a product boundary while
remaining part of an offering arrangement. A regulator can constrain Work without being part of the operational
System.

When those relations remain implicit, a plausible concept can fail in use, an interface can be assigned to the
wrong bearer, a provider can promise a result no arrangement can deliver, or later evidence can have no clear
decision to reopen.

### SYSE.16:3 - Forces

Recurring tensions include:

- An account must be broad enough for the decision while affordable to obtain and maintain.
- Project boundaries simplify Work, while outside Systems and conditions can still change the engineering choice.
- One System can participate in several wholes and selected structures at once.
- Functional transformation and constructive structure must correspond without being collapsed.
- Design choices concern possible futures; actual participation and observed conditions concern what obtains.
- Relevant surroundings continue to change—for example, providers, users, infrastructure, rules, competing
  offerings, or operating conditions.
- Existing vocabulary helps communication but can import ownership, lifecycle, or stakeholder assumptions that do
  not match the current relation.

### SYSE.16:4 - Solution

Recover the Systems, structures, relations and conditions needed to ground one use decision.
Begin with the actual System or intended System referent selected for engineering and its named use situation; stop when the account supports the receiving decision or identifies the condition that prevents it.

Reuse an adequate existing account or direct relation result for the same decision and conditions.
Use the bounded recovery below when a missing connection prevents that answer. If the operating situations
themselves need development or agreement, use a suitable scenario or concept-of-operations Method;
obtain any missing specialist result from its domain before relying on it.

#### SYSE.16:4.1 - Perform the Move

1. **Bound the use and decision.** State the actual System or intended System referent selected for engineering, its use situation, configuration or variant, decision, relevant place, horizon and description sources. When it is a creator, retain the products or classes of use that ground the required contribution and local acceptance. Keep the descriptions separate from the Systems and situation.
2. **Find containing and receiving Systems.** Identify every larger System that matters because the selected
   System is, or would be, its proper part, and every System that receives or would receive a result of its
   functioning. State each direct relation and whether it is actual or proposed; retain several wholes when
   the decision depends on them.
3. **Recover functional organization.** Identify the transformation flows, interactions, and contributions in
   which the System participates, including the changed or receiving Systems and conditions. Use `A.6.F` for
   function-like claims and `E.18.NET` when a transformation-flow network is needed.
4. **Recover constructive organization.** Identify the structures that matter to this use—for example, parts,
   bearers, modules, interfaces, or connections. Use `A.22` for each selected structure and `A.6.M` only when
   module or interface claims obtain. Do not infer constructive parthood from a functional contribution.
5. **Add other Systems and conditions.** Include only a System or condition whose named relation can alter the use
   result or engineering choice. State that relation and its participants or state the relevant condition. Examples
   include a transfer from a named supplier System to a named receiver, access granted by a provider System, a
   permission or commitment between named participants, an available resource, or an operating constraint. When
   performed provider Work matters, identify the dated Work occurrence, performer Agent, and applied Method
   separately. For proposed provider Work, identify the intended Work, performer and Method, and the commitment
   or capability evidence actually available. Then name only the direct relations used by the decision: Agent
   participation in the Work, result production, supply or access from provider to receiver, receipt or use of
   the result, a commitment, or another governed provision relation. Distinguish obtaining relations from
   proposed ones; a commitment does not establish that Work or delivery occurred. Do not hide these objects or
   relations under *environment*.
6. **Separate future choices from present facts.** Mark descriptions as observations, predictions, design choices,
   commitments, or unsupported assumptions. A proposed interface or whole does not obtain merely because a model
   contains it.
7. **Test outside change.** Ask which relevant outside factors—for example, Systems, conditions, interfaces,
   providers, uses, or regulations—can change during the relevant horizon and which change would reopen the
   concept, architecture, offering, assurance, or configuration decision.
8. **Return the result needed by the decision.** Supply the supported relations and conditions, or the material
   mismatch, alternative, evidence need or unresolved assumption, to the receiving engineering Work. Leave unrelated surroundings out.

The numbered steps explain the Method. Determine Work order from the actual dependencies. Observation,
concept development, architecture development and trials can overlap and recur while outside Systems change.

#### SYSE.16:4.2 - Record the Result

| Field | Required content |
| --- | --- |
| focus and decision | Actual System or intended referent being engineered, its use, receiving decision, configuration, relevant place and horizon; for a creator, the product uses and contribution that ground its capability and local acceptance. |
| containing and receiving Systems | Each larger or receiving System and the proper-part, transfer, interaction, or other direct relation that matters. |
| functional organization | Selected transformations, flows, interactions, contributions, changed or receiving Systems, and operating conditions. |
| constructive organization | Selected parts, bearers, interfaces, modules, and connections needed by the use. |
| other Systems and conditions | Providers, users, resources, constraints, and their stated obtaining or possible-future relations. |
| epistemic status | Observation, evidence-backed claim, prediction, design choice, commitment, or unsupported assumption. |
| co-change and return | Outside changes that reopen the decision, evidence that would reveal them, and the mismatch, alternative, or missing result supplied to receiving Work. |

For a bounded first result, one decision-changing containing or neighbouring System, one named relation or
condition, its epistemic status and one result for that decision may suffice. For an unknown that can change
the result, state which decision it blocks. Use several representations when needed, keeping them distinct
from the use situation and System whole they describe.

#### SYSE.16:4.3 - What Changes in Practice

The engineer stops asking only what lies outside a product box and asks which Systems, structures, direct
relations, and conditions make this use work. Functional transformation and constructive structure stay
separate, outside change becomes an engineering input, and unsupported assumptions become visible results rather
than hidden context.

### SYSE.16:5 - Worked Case: Upgrading an Occupied Building's Heat-Pump Plant

An engineering team is deciding whether to add a new controller configuration to an existing heat-pump plant for
the next heating season. The decision asks whether occupied rooms can remain within the selected thermal range
while the plant responds to grid signals.

The engineering-use account distinguishes these structures and relations:

- **Actual System and containing whole.** The heat-pump plant is an actual System and a proper part of the
  building heating System. The proposed controller is still an intended referent. The occupied building and its
  heating System are not assumed to be the same whole.
- **Functional transformation and transfers.** An electricity-distribution System transfers electrical energy
  through the feeder. A signal channel transmits demand-response information. The plant transfers thermal energy
  to the hydronic loop, and the loop and radiators transfer it to room air. Envelope heat transfer and occupant
  control actions also change room temperature.
- **Constructive organization.** The feeder, sensors and controller cabinet are physical bearers. The account
  also identifies the hydronic connections, proposed controller interface and signal channel. Required clearance
  around the cabinet is a spatial condition on its location and maintenance access. Establish the part and
  connection relations independently of the functional-flow description.
- **Maintenance supply, access, and Work.** Under `MaintenanceCommitment-14`, maintenance company `HeatCare-7` commits to supply `ControllerInspectionResult-14` to building operator `BuildingOperator-1` before the controller-configuration decision. The building operator grants `HeatCare-7` plant-room access during stated windows. Technician `T-4` is the intended Agent for `ControllerInspectionWork-14`; that Work has not occurred. If it occurs, the Work produces the inspection result, `HeatCare-7` supplies the result to `BuildingOperator-1`, and the operator receives it for the controller-configuration decision.
- **Systems that may bear consequences.** Residents in a nearby building may experience increased low-frequency
  noise during night cycling. A model supports this possible consequence; no night measurement yet establishes
  an observed effect.
- **Unsupported assumptions.** Sensor latency and occupant override behaviour are unknown at the required load. A
  planned insulation change may alter the thermal model. Cabinet clearance is supported by a drawing but has not
  been checked in the plant room.

For the cabinet-location choice, the next result is confirmation of the required and available clearance under
the installation and access conditions. If those conditions already determine the required clearance, the team
can answer that spatial question directly. If occupant and grid-control behaviour leave the operating situation
unsettled, develop the relevant scenarios before relying on that use.

The account changes three next decisions. The Agent applying `SYSE.17` uses the possible acoustic-exposure and
maintenance-access consequences. The Agent applying `SYSE.8` uses the maintenance commitment, provider and access
relations, and the need for the inspection result. The Agent applying `SYSE.2` uses the revised use claims and
low-noise and cabinet-location alternatives. If the team also considers remote monitoring, that is a proposed
offering: this account establishes neither its provider commitment nor its authority. The dependent remote-
monitoring claim remains conditional. The team can act on the supported inputs.
**When the full pattern is unnecessary.** If the current question is only whether one already identified sensor
is a proper part of one known controller under an admitted relation, use the direct System and parthood patterns.
A broader engineering-use account adds no value.

### SYSE.16:6 - Bias Annotation

A source or representation—such as an official context diagram, stakeholder list, standard, or organization
chart—does not by itself establish that a relation obtains or a Method is effective. Any capable and authorized
Agent may develop the account. Capability and authority require grounds appropriate to that Work; a professional
title, substrate or organization label is not sufficient on its own.
Specialist Methods and evidence remain with their domains—for example, electrical, building, safety, legal,
environmental, or financial practice. Agents with the relevant authority make the corresponding decisions.

### SYSE.16:7 - Conformance Checklist

- [ ] The actual System or intended System referent selected for engineering, use situation, receiving decision, configuration and horizon are stated; a creator retains its product-use grounds and bounded acceptance.
- [ ] Actual Systems and intended referents remain distinct from accounts, models, scenarios, and diagrams.
- [ ] *Suprasystem* is used only with a stated actual or possible-future proper-part relation.
- [ ] Functional transformation remains separate from constructive parts, bearers, and interfaces.
- [ ] Other Systems and conditions appear only when a named relation can change the decision.
- [ ] Observations, predictions, design choices, commitments, and unsupported assumptions remain distinct.
- [ ] Outside changes and evidence that reopen the decision are stated.
- [ ] The account supplies the relations and conditions sufficient for the receiving decision, or identifies
      a material mismatch, alternative, evidence need or unresolved assumption.

### SYSE.16:8 - Common Failures and Repairs

These recurring abstractions hide a relation that changes the engineering decision:

| Failure | Repair |
| --- | --- |
| Everything outside becomes one environment box | Recover only the wholes, other Systems, conditions, and direct relations used by the decision. |
| Stakeholders stand for operational structure | Identify actual Systems and relations; use `SYSE.17` for consequence-bearing Systems. |
| Every larger or influential object is called suprasystem | Require a proper-part claim or use the actual relation. |
| Function is treated as a component | Keep transformation flows and constructive structures separate and state their correspondence. |
| Diagram is treated as reality | Keep the representation, subject, currentness, and evidence distinct. |
| Outside Systems are held constant | Record co-change and reopen evidence for the relevant horizon. |
| Environment analysis becomes an early phase | Revisit the account when concepts, architecture, evidence, configuration, or outside Systems change. |
| The team models surroundings that cannot change the decision | Stop when the bounded account sufficiently supports the receiving decision or identifies the missing result. |

### SYSE.16:9 - Consequences

Engineering alternatives become comparable in the use that gives them meaning. Interface choices expose their
bearers and receiving Systems, outside changes gain reopen conditions, and System or offering concepts no longer
rely on an unexplained environment label.

The cost is maintaining the selected structures, conditions and their correspondence. A bounded account
accepts incomplete coverage of other uses; broaden the work when an omitted situation can change the decision.

### SYSE.16:10 - Rationale

Systems matter through particular part, interaction, transformation, interface, transfer, and consequence
relations under conditions. FPF supplies the general ontology for those claims. The engineering specialization is
the repeatable move from one use decision to the outside relations and conditions that can change concept,
architecture, offering, assurance, configuration, or continuing development.

### SYSE.16:11 - SoTA and Source Use

**Working question:** Which Method should an engineer use when different relations hidden inside an
"environment" label prevent one use decision?

The selected answer depends on what is missing. Use an adequate existing account or the direct relation
Method when it settles the question. Use this bounded recovery when the needed result depends on connecting
several Systems, relations and conditions. A developed concept-of-operations (ConOps) Method is an
alternative when operational situations or agreement about intended use still need to be constructed.
It develops and challenges scenarios; identifying a few relations cannot supply that broader result.

The bounded connection accepts limited coverage in exchange for concentrating the account on one decision.
It still needs the applicable evidence and specialist contributions. Section :4 makes this choice at entry;
steps 1–6 recover the missing connections, and steps 7–8 return changed conditions to the affected decision.
The thin :4.2 result is sufficient only within that use. In :5, cabinet location returns a spatial-evidence
question, whereas unsettled occupant/grid behaviour returns scenario development. An adequate earlier answer
can be reused in either branch.

| Source answer and comparison role | Disposition, operative contribution and limit |
| --- | --- |
| Current FPF `A.22:4.1`, with the direct subject patterns named in :12: a supplying Method and a direct-use alternative | **Adopt** independent constituent, relation, constraint and use identification. **Adapt** that selection to the engineering decision in steps 1–6 and the :4.2 account. A spatial condition keeps its own meaning even when the same decision also needs a bearer or interface. The engineering-use account connects these selections to the receiving decision. |
| [NASA Systems Engineering Handbook, §4.1.1.2.2–4.1.1.2.5](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/): a developed professional alternative | **Adapt** elicitation, operational scenarios and agreement about use when those results are missing at :4's entry. Follow significant nominal and off-nominal situations into interfaces and operator/support contributions. The handbook's mission-specific organization is not imposed on every thin account. |

Reopen the Method choice when
a sufficient account becomes available, an omitted condition defeats the receiving use, the question expands
to other scenarios, or a supported alternative offers a preferable combination of coverage and effort.
Retain qualified evidence for unaffected claims while revising the dependent conclusions.

### SYSE.16:12 - Relations

- `SYSE.1` can supply the engineering subject and its product-use grounds, decision, boundary question, alternatives and reopening evidence. A creator is usable as the engineering subject without another SoI designation. These dependencies create no temporal order.
- `A.1.SCR` distinguishes an actual acting or changed System from a designation, role word, description, process,
  or organization label.
- `A.22` governs each selected structure. `A.6.F` restores function, bearer, capability, Work, and
  MethodDescription distinctions; `A.6.M` applies only to an obtaining module or interface claim.
- `E.18.NET` applies when the use needs a network of transformation-flow structures. It identifies the
  selected structure; use `E.18.2` for its graph or other mathematical description. Neither the network nor
  its description is the containing whole or a lifecycle.
- Agents applying `SYSE.17`, `SYSE.8`, or `SYSE.2` can use the account's consequence, provider, or concept
  results. Each Agent rechecks subject, configuration, horizon, evidence, and compatibility for the receiving use.
- Application profiles retain domain Methods and evidence—for example, Methods and results for operating physics,
  safety, legal compliance, medical use, finance, software, electrical systems, buildings, or ships.

### SYSE.16:End
