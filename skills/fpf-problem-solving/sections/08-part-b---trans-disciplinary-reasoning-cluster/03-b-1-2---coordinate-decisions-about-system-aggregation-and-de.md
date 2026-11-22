## B.1.2 - Coordinate Decisions About System Aggregation and Delimitation

> **Type:** Part B holonic construction pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is marked informative

### B.1.2:0 - Use This When

Use this pattern when an engineering decision about a system whole depends on several independently grounded claims: its part-whole relations, delimitation, boundary crossings, functions and their bearers, or whole-level characteristics. The entity may already be recognized under `U.System` or still be under evaluation through A.1.

Typical moments:

- a machine, building asset, or organization is proposed as a whole assembled from identified constituents;
- a system-level characteristic is to be rolled up from constituent characteristics;
- a supply, signal, measurement, control, source, publication, evidence, or transformation relation is being mistaken for a part relation;
- a functional element must be distinguished from and allocated to physical, organizational, software, or operational bearers;
- a named decision needs one recoverable view of the system boundary, crossings, and compatibility choices without turning that view into the system.

**First useful move.** Start from the receiving decision and the system or proposed assembly it concerns. Follow its use outward when the enclosing arrangement can change that decision, and inward when two admissible internal arrangements give different answers. Identify the whole's A.1 recognition status when systemhood matters to the claim. For each claim, use the applicable subject pattern to recover its result or identify the missing defining rule or information. Then ask whether considering the results' joint organization changes the decision.

**What goes wrong if missed.** A reader may infer components and containment from placement in a diagram, treat a functional element as a physical part, or mistake an external transformation or measurement relation for parthood. A coordination record then appears to establish facts that each need grounds.

**What this buys.** The practitioner can combine the results needed for one engineering aggregation decision while retaining each claim's grounds and use conditions.

**Not this pattern when.**

- If the only open question is whether an entity qualifies as a `U.System`, use `A.1`.
- If one part-whole relation is the question, use `A.14` and its specialization.
- If constructive assembly grounding is the question, use `C.13`.
- If the question is a functional claim, use its behavior or realization predicate; use `A.6.F` when the function wording is unresolved and `C.30.ASV` when architecture-view conformance is needed.
- If bearer allocation or parthood is the question, use the allocation or part-relation pattern; use `A.6.M` only when module or interface wording needs repair.
- If a mathematical aggregation lens is the question, use `C.29`.
- For the system-of-interest role in an extended enterprise or the system-in-hand for local investigation or change, use `A.1.STM` and `A.1.SCR`. For a technical system-role assignment, Work, transformation, service or access, evidence, description, or publication, use its subject pattern.

### B.1.2:1 - Problem Frame

B.1.2 specializes B.1 for system holons. It coordinates independently grounded facts for one aggregation or delimitation decision; each relation retains its defining pattern.

Keep the following meanings separate when identifying the whole:

1. **The system whole.** For an existing system whose identity matters, establish it under A.1 and its identity rule. For a proposed design, identify the system to be built through its intended use, arrangement and assumptions.
2. **Its environment.** In this pattern, `environment` means the external referents and crossing relations made relevant by a stated delimitation and use. It is not a generic surrounding object; a medium is named separately when that medium is the subject.
3. **A containing system.** The larger system of which `S` is an admitted part exists for this claim only when a part-whole relation independently obtains. Interaction or spatial surrounding is not enough.
4. **System-of-interest and system-in-hand.** The system-of-interest is the product System that a named extended enterprise is organized to create, change, sustain in use or retire. The system-in-hand is the system locally being investigated or changed. Use A.1.STM:4.1 and A.1.SCR:4.7 to establish the grounds for the designation or local focus. Neither establishes System identity, environment, parthood or architecture; any technical system-role classification and assignment also needs its own grounds.
5. **Use qualification and neighboring relations.** `Context` is not one world-side container supplied by B.1.2. When claim scope, effective reference scheme, or a bounded model-use structure qualifies a use, recover that qualifier under its subject pattern. Recover any system-role assignment or other neighboring relation separately. None delimits the system, identifies its environment, or establishes containment by itself.

For a system-aggregation decision, use :4.1 to recover the identity, part, boundary, crossing or characteristic results needed by that decision. Use :4.2 only when their joint organization changes that decision.

### B.1.2:2 - Problem

When these distinctions are missed:

1. **Boundary by drawing.** A box in a diagram is accepted as system delimitation.
2. **External relations become parts.** Suppliers, grids, sensors, controllers, teachers, measuring instruments, or digital twins are placed inside the system because they interact with it.
3. **Functional and physical structures collapse.** A resistor symbol, control function, chassis function, or service label is treated as a physical component by name alone.
4. **Whole-level characteristics lack grounding.** Mass, capacity, reliability, safety, throughput, assurance, or agency-like characteristics are rolled up without saying which bearers, relations, and scales support the claim.
5. **Transformation becomes containment.** A tool, teacher, actuator, script, or controller changes a holon and is then treated as its part or containing whole.
6. **Coordination record becomes ontology.** One aggregate-shaped record creates systemhood, parts, boundary, crossings, allocation, evidence, and representation instead of pointing to independently governed facts.

### B.1.2:3 - Forces

| Force | Tension |
| --- | --- |
| Engineering concreteness vs broad FPF holon scope | System aggregation must be practical for systems without making all holons systems. |
| Delimitation vs external dependency | A named use needs a system boundary while critical relations can cross it and remain external. |
| Component structure vs functional structure | Physical or organizational bearers may realize several functions, and one function may require several bearers. |
| Conservative roll-up vs redundancy | Weakest-link and conservation checks are useful, but redundancy or substitution may require B.2 whole reidentification. |
| Description vs described system | A description must preserve the distinctions needed for the decision while remaining distinguishable from the system it describes. |
| Coordination vs ownership | One decision may need many facts, but the coordinating pattern must not become the source of all those relations. |

### B.1.2:4 - Solution

Coordinate one named system-aggregation or delimitation decision using the independently grounded results below. A record can bring those results together; establishing any further relation requires grounds.

Use an established fact about the whole directly when it settles the decision. To compare proposed designs, hold their common requirements fixed and follow each proposed allocation or crossing to its consequence for the intended use. A model may group designs with the same relevant consequence and grounds. An inventory of existing components supports a different decision from choosing or realizing a new assembly. Read the questions below for the claims the result actually needs. For a proposal, identify its stipulated relations and conditions of use. Evidence that they obtain is needed for an as-built claim.

#### B.1.2:4.1 - Recover Each Result Or Blocker

| Working question | Subject pattern | Result or stop |
| --- | --- | --- |
| Which whole is being considered? | `A.1` and the kind-specific recognition pattern | For a design comparison, the proposed whole, its intended use and the arrangement under consideration. For a claim about an existing `U.System`, a recognized entity or the A.1 evaluation of its six constructive components and kind-specific condition, including any unresolved basis. |
| Which constituents are parts, portions, phases, or members, and how do they assemble? | `A.14`, the part-relation specialization, and `C.13` for constructive assembly grounding | For an actual system, the obtaining part relations and assembly. For a design comparison, the proposed relations and their consequences under the stated assumptions; otherwise the missing governor, participant identity, obtaining fact, or assembly basis. |
| Which facts and selected boundary-use claim delimit the system for this decision? | `A.1` for system identity; `A.14`, the part-relation specialization, and `C.13` for parthood and assembly; every crossing-relation pattern for external participants; `C.11` for a local choice among already available boundary readings; `C.32.PAD` for a post-synthesis architecture decision concerning project Work; `C.2.1` only for a separately persistent claim | First identify the system and the parts, assembly or boundary crossings that affect this question. For a proposed option identify the corresponding design stipulations. For a claim about the actual system establish the relevant facts. If those facts answer the question, stop. If the named use additionally selects a boundary reading, return the C.11 `ChoiceResult` or C.32.PAD `ArchitectureDecisionRelation@Project` that makes its inclusion, exclusion, identity-preservation, and use claim current. Another choice branch passes only after its admitted decision predicate, source, and result are named; otherwise return the missing predicate or defining pattern, participant, obtaining fact, decision governor, or information blocker. When durable reliance is needed, one separate C.2.1 episteme states that claim and cites its basis; it creates none of the world facts. A selected `U.Structure` remains a separate B.1.2:4.2 branch. |
| Which relation crosses the selected boundary? | The source, supply, flow, coupling, control, measurement, evidence, publication, transformation, commitment, or other relation pattern; `F.9` only for a needed semantic correspondence or difference between two F.17 local senses from different semantic contexts | For an actual crossing, the obtaining relation with its participants and predicate. For a proposed crossing, the specified endpoints, relation and conditions; otherwise the missing governor, endpoint, binding, or obtaining fact. |
| Which function is realized by which bearer? | The behavior, realization, allocation or parthood pattern; `A.6.F` or `A.6.M` only for unresolved wording; `C.30.ASV` only for architecture-view qualification | For a current arrangement, recover the functional claim, bearer and obtaining realization or allocation relation. For a proposed allocation, establish what its bearer would have to do and whether the design supports that use. Establish parthood separately when it is claimed. If a relation required by the claim cannot be established, identify the missing predicate, participant or defining source. |
| Which whole-level characteristic is claimed? | `C.16` and `A.19`; `C.29` when a mathematical representation-choice, transfer or reliance question remains unresolved | Recover the bearer, characteristic, assignment or value, and scale, together with any threshold, aggregation or inference rule, and lens-use boundary required by the claim; identify any missing basis needed for that claim. |
| Which evidence, description, representation, or publication supports inspection? | `C.2.1` for the account; `A.2.4` for evidence-use or status-use classification. Use `A.10` for an unresolved source-to-use account, `B.3` for a requested assurance claim, `C.29` for an unresolved mathematical-lens question, or `E.17` for a needed publication face; use the applicable source or architecture-description pattern when that relation is the question | The episteme and evidence, assurance, description, representation, source-use, or publication relation; otherwise the missing identity, relation, applicability, or reliance basis. |

If grounds are missing, check whether the remaining possibilities support the same decision. Give that decision and its grounds when they do. Otherwise return the established contribution and identify the missing result that could change the answer.

#### B.1.2:4.2 - Select A Structure Only When The Joint Organization Matters

When a decision depends on several results together, explain how they combine for that decision. In a design comparison, the relations and constraints stipulated for each option can warrant a conditional conclusion. When the claim selects a `U.Structure` under `A.22`, identify the subject whose organization is selected. Establish its independently identified constituents, the relation occurrences that obtain for that subject, the applied constraints and the named selection-use frame with its admissible action or stop. Relations between elements of a design can be present before the designed assembly exists.

The selected structure is non-agentive. Selecting it does not establish systemhood or the relations being selected. A diagram or other representation can express the selected organization; its form alone supplies none of the four discriminators.

#### B.1.2:4.3 - Make Interface Choices About Crossing Relations

When choosing an interface arrangement, identify the existing or proposed crossing and the use affected by the choice. Options include exposing the crossing, assigning it a namespace, internalizing it, excluding it, or leaving its treatment with its subject pattern. These are ordinary decision options.

Name the relevant world facts or design stipulations, affected endpoints, crossing predicate and any occurrence claimed, preserved obligation or information, evidence if relied on, and the C.11 `ChoiceResult` or C.32.PAD `ArchitectureDecisionRelation@Project` that chooses among the ordinary interface options when its predicate applies. A different choice passes only after its subject assertion, predicate, and result are named; otherwise stop with the established `missing-governor` blocker, whose content identifies the absent predicate source.

If a later use must inspect the choice, identify a separate C.2.1 episteme whose claim content describes it and cites that result; the episteme does not make the crossing, parthood, compatibility, or decision fact obtain. This account lets the practitioner check whether an interface change loses an external obligation or leaves an endpoint unmanaged.

#### B.1.2:4.4 - Whole-Level Characteristics

Roll up system-level characteristics only after the bearer, characteristic relation or assignment, scale, and aggregation or inference rule are selected under their subject patterns.

Useful families include:

- additive quantities such as mass, cost, energy stock, or material amount;
- limiting quantities such as pressure rating, weakest connector, safety class, or availability bottleneck;
- logical or capability claims such as emergency-stop availability or vulnerability exposure;
- architecture characteristics that depend on selected structure.

Use `C.16` and `A.19` for the characteristic, scale and aggregation rule. Retain the correspondence, assumptions and limits needed to rely on a mathematical lens; use `C.29` when its choice, transfer or reliance remains unresolved. Use B.2 when changed facts leave a consequential question about whether the existing whole still supports the claim or a new whole is required. A sufficient existing-whole explanation ends that inquiry; missing deciding grounds leave the comparison unresolved.

#### B.1.2:4.5 - Functional Elements And Bearers

A functional element in a functional view is not automatically a system part. Recover the functional claim and its intended behavior, the bearer under its kind and identity rule, the independently established realization or allocation relation, and any obtaining parthood relation. C.2.1 identifies a claim episteme when one must be cited; C.30.ASV qualifies an architecture structural view when that is the use.

Use A.6.F only to resolve an unclear function expression and A.6.M only to resolve module or interface wording. Neither pattern admits the bearer or establishes allocation or parthood. One bearer can realize several functions and one function can require several bearers when the domain relations support those claims.

### B.1.2:5 - Archetypal Grounding (Worked Cases)

#### B.1.2:5.1 - Pump Skid

A pump skid may be one entity proposed for recognition under the already admitted `U.System` kind. Pumps, frame, valves, controller, and connectors become its components only when their A.14 part-relation occurrences obtain and C.13 grounds the assembly; the proposal, drawing, and component list establish none of those facts.

The power grid, maintenance crew, telemetry dashboard, and supplier are not skid components merely because the skid depends on them. Recover the systems or epistemes and their supply, work, telemetry, publication, source-use, or other relations. If a maintenance-isolation decision needs their joint organization, an A.22 selected structure may include the obtaining crossings without turning them into parts.

**Coordination result.** In an illustrative component-inventory case, skid S is already recognized under A.1. Inspection and assembly evidence have established the A.14 component relations of pump P, frame F, valve V and controller C to S, with the C.13 assembly basis. The inventory is complete for this example. A documented electrical-supply relation has grid G as source and S as receiver; dashboard D is an episteme describing S. These independently supplied facts are the inputs to the decision, not conclusions inferred from the drawing.

For the question “Which of these objects belongs in S's component inventory?”, B.1.2 returns P, F, V and C, retaining each part relation's basis. G remains an external supply participant and D remains a description. The inventory establishes no total mass, reliability or safe-isolation conclusion: each would need its characteristic rule or decision basis. If inspection instead leaves V's part relation unresolved, return the three established components and that gap; do not present the inventory as complete. Changed assembly or supply facts reopen the affected result.

#### B.1.2:5.2 - Resistor In A Circuit

A resistor symbol in a circuit diagram is a functional or design-description element. The physical bearer may be a packaged resistor, a length of wire, a transistor region, or a module. Recover the function, bearer, allocation or correspondence, and any part relation separately; B.1.2 only coordinates them for the circuit decision.

#### B.1.2:5.3 - Digital Twin Of A Building Asset

A BIM model, asset register, dashboard, or digital twin may describe the built asset and its systems. It is not the asset's part by being linked in a model. Identify what the model or account says about the asset; use C.2.1 if that description needs clarification. Follow the further questions in :4.1 only when the use depends on them. Establish any claimed parthood through its relation.

#### B.1.2:5.4 - Lathe And Workpiece

The lathe can change the workpiece through a bounded transformation and work occurrence. Those facts do not make the workpiece a lathe component or make the lathe the larger whole containing it. Use A.3.4, A.15.1, A.12, and the crossing or participation pattern; use part-whole only when a relation independently obtains.

### B.1.2:5.5 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Box as ontology | A diagram boundary becomes system delimitation by appearance. | Name the system and obtaining part and crossing relations. Stop if they answer the question. If a distinct use-relative boundary choice remains, name the C.11 `ChoiceResult`, C.32.PAD `ArchitectureDecisionRelation@Project`, or another admitted result; otherwise stop with the missing-governor blocker. Use an A.22 selected structure only when its four discriminators are independently grounded. |
| Interface as part | Supply, signal, measurement, control, publication, or evidence relation becomes a component. | Recover the crossing occurrence under its subject pattern and keep it separate from parthood. |
| Function as bearer | A functional block or symbol is treated as a physical or organizational component. | Recover function, bearer, allocation or correspondence, and any parthood claim separately. |
| Description as system | BIM model, dashboard, digital twin, register, or source record is treated as the system. | Identify the description and the system it describes; use C.2.1 if that relation is unclear, and the applicable further pattern only for a remaining question. |
| Transformation as containment | A tool or teacher changes a holon and is read as its part or containing whole. | Use A.3.4, A.15.1, A.12, and the participation or crossing pattern; require a separately obtaining part-whole relation for containment. |
| Coordination as ownership | A convenient B.1.2 record is treated as the source of all named facts. | Use its subject pattern for each relation the conclusion needs; select an A.22 `U.Structure` only when the organization changes the decision. |

### B.1.2:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-B1.2-1` | A design conclusion identifies the proposed whole and the stipulations on which the conclusion depends. When the conclusion needs an existing `U.System`, give its recognition under A.1 or identify the unresolved recognition question. |
| `CC-B1.2-2` | The result identifies the system and the relations the named decision depends on. A design comparison states the assumed arrangements. Conclusions about as-built parts or actual crossings identify the obtaining relations under their subject patterns. When a distinct use-relative inclusion/exclusion choice is claimed, it cites the applicable C.11 `ChoiceResult`, C.32.PAD `ArchitectureDecisionRelation@Project`, or another admitted result; without that predicate, source, and result it returns a missing-governor blocker. Any durable C.2.1 episteme states but does not create those facts. An optional selected structure separately satisfies all four A.22 discriminators. |
| `CC-B1.2-3` | External supply, signal, control, measurement, source, publication, evidence, transformation, or coupling claims retain participant bindings and relation patterns; none becomes parthood by crossing or importance. |
| `CC-B1.2-4` | When a conclusion uses functional elements, their bearers, an allocation or a part relation, it identifies the grounds for each relation used. |
| `CC-B1.2-5` | A whole-level characteristic names its bearer, characteristic relation or assignment, scale and supporting evidence. A roll-up or other inference identifies the rule and any mathematical-lens boundary it uses. |
| `CC-B1.2-6` | Changing, controlling, teaching, measuring, or repairing another holon does not make that holon a part of the acting system; any containing-whole claim has its part-whole relation. |
| `CC-B1.2-7` | Description artifacts, models, dashboards, digital twins, and registers remain distinct from the system holon and from any selected structure they describe. |
| `CC-B1.2-8` | A claim to have selected a `U.Structure` identifies its subject and establishes the four A.22 discriminators for that subject. A conditional conclusion about a proposed design identifies the stipulated organization that warrants it. |
| `CC-B1.2-9` | Environment, containing system, the system-of-interest role in a named extended enterprise, the local system-in-hand, and any claim or model-use qualifier remain separately identified; `Context` is not used as their common owner. |

### B.1.2:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Box as boundary | A diagram rectangle determines system membership. | Recover the identity, part and crossing facts needed for the boundary question. If they settle it, give the answer. If a distinct use-relative boundary choice remains, name the applicable C.11 `ChoiceResult`, C.32.PAD `ArchitectureDecisionRelation@Project`, or another admitted result; otherwise stop with the missing-governor blocker. Add a C.2.1 episteme only when that claim must persist; use an A.22 selected structure only when its four discriminators are independently grounded. |
| Supplier as component | External supplier or grid is treated as part of the system. | Recover the supply, commitment, evidence, source-use, or other crossing relation under its subject pattern; infer no parthood. |
| Function block as module | A functional block is treated as a physical component. | Recover the functional element, proposed bearer, allocation or correspondence, and any obtaining part relation separately. |
| Digital twin as part | A model or dashboard appears inside the system aggregate. | Recover the description relation; add parthood only if its predicate independently obtains. Follow :4.1 for a further question about relying on or publishing the description. |
| Redundancy as arithmetic | Redundancy is averaged into a better system score. | Check the characteristic scale and applicable existing-whole explanations; use B.2 when the decision still depends on whether the existing whole is sufficient. |

### B.1.2:8 - Consequences

Positive consequences:

- System aggregation remains practical for engineering systems and organizations.
- Boundary and interface decisions expose the facts and rules they depend on.
- Practitioners can distinguish functional architecture, module allocation, and physical parthood within a shared diagram.
- The description remains distinct from the system it describes; any further claimed relation between them needs grounds.

Costs:

- A decision diagram needs clarification when a relevant relation or its basis cannot be recovered from the diagram and its available explanation.
- Some familiar component lists must be split into physical parts, functional elements, external systems, sources, and descriptions.
- Whole-level characteristic claims need scale and relation discipline.

### B.1.2:9 - Rationale

An engineering decision may depend on several relations involving the same system. Drawing them inside one box can obscure which objects are parts and which participate through other relations. B.1.2 coordinates the independently grounded results and selects an A.22 structure only when their joint organization changes the decision.

### B.1.2:10 - SoTA-Echoing

The coordination method uses A.1 for system recognition, A.14 and C.13 for parts and assembly, and the applicable characteristic or relation method for each further claim. In the pump-skid case (:5.1), assigning membership from diagram placement can include the external grid and the description. Keeping the independently established relations yields the component inventory and exposes an unresolved component relation while retaining the established ones. This is the bounded comparison the case supports. A comparative claim against a named systems-engineering or reliability-engineering method requires that method's delimitation and inference rules, assessed on the same decision at comparable effort.

### B.1.2:11 - Relations

- **Builds on:** `B.1`, `A.1`, `A.14`, `C.13`, `A.22`, and the relation patterns selected for the decision.
- **Coordinates with:** `A.6.F` for function wording, `A.6.M` for module/interface wording, subject patterns for bearer identity and allocation, `A.22` and `C.30` for selected structure and architecture, `C.16` and `A.19` for characteristics, `C.29` for mathematical lenses, `A.3.4` and `A.12` for transformation and acting-side externalization, and `C.30.AD` or `C.30.AD.BA` for architecture-description cases.
- **Can contribute evidence to:** `B.2` when changed system facts raise a consequential question about continuing with the existing whole or identifying a new one.

### B.1.2:End
