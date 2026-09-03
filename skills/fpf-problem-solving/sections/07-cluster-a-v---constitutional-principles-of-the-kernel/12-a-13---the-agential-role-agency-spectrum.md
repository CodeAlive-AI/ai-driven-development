## A.13 - The Agential Role & Agency Spectrum

> *“Agency is not a kind of thing; it is a way some systems operate.”*

### A.13:1 - Intent & Context

The concept of "agency"—the capacity of an entity to act purposefully—is central to engineering, biology, and AI, yet it remains one of the most overloaded and ambiguous terms. Without a precise, falsifiable, and substrate-neutral definition, models of autonomous systems risk descending into "self-magic," where actions have no clear cause and accountability is lost.

This pattern builds directly on the FPF Kernel. A.1 establishes that the acting holder must be a `U.System`. A.2 and A.2.1 distinguish a local system-role kind, classification by that kind, and an obtaining occurrence of a directly declared `U.SystemRoleAssignment` species. A.12 supplies the acting-side externalization principle.

The intent of this pattern is to:
1.  Define **agency** not as an intrinsic *type* of holon, but as an assignment claim: an exact local agential system-role kind is assigned to a `U.System` through an obtaining `U.SystemRoleAssignment`.
2.  Introduce a measurable, multi-dimensional **spectrum of agency** via a dedicated agency-characteristic profile, moving beyond a simple binary "agent/not-agent" switch.
3.  Provide a clear, **didactic grading system** that allows engineers and managers to assess and communicate the Agency Grade of any system in a consistent, evidence-backed manner.

### A.13:2 - Problem

If agency is treated as a monolithic, intrinsic property or a mere label, four critical failure modes emerge, undermining the rigor of FPF:

1.  **Episteme-as-Actor:** Models might incorrectly assign agency to knowledge epistemes or publications (`U.Episteme`), leading to nonsensical claims like "the specification decided to update the system." This is a direct violation of **Strict Distinction (A.7)**.
2.  **Type Inflation:** Introducing a root agent kind alongside `U.System` and `U.Episteme` would violate **Ontological Parsimony (C-5)**. The same System may qualify for an agential system-role kind and receive an assignment in one working situation but not another. The agency claim states its scope and window separately; a root type cannot express these differences.
3.  **Unfalsifiable Claims:** Without a measurable basis, "agency" becomes a subjective label. A team might call their system an "agent" for marketing purposes, but this claim has no verifiable meaning and cannot be audited, violating **Evidence Graph Referring (A.10)**.
4.  **The Binary Trap:** A simple "agent/not-agent" classification is too coarse. It fails to distinguish between a simple thermostat, a predictive cruise control system, and a strategic, self-learning robotic swarm, even though their cognitive capabilities differ by orders of magnitude.

### A.13:3 - Forces

| Force | Tension |
| :--- | :--- |
| **Scientific Fidelity vs. Simplicity** | Contemporary science (e.g., Active Inference) models agency as a continuous, scale-free spectrum. FPF needs to honor this rigor while providing a simple, teachable model for practitioners. |
| **Role vs. Type** | The intuition is to think of "agent" as a *type* of thing. FPF's architecture demands role assignment plus agency characteristics to preserve dynamism and ontological hygiene. |
| **Measurement vs. Label** | Engineers and managers need a quick, intuitive label (e.g., "this is a Level 3 agent"), while formal assurance requires a detailed, multi-dimensional, evidence-backed measurement. |
| **System-only Action vs. Collective Action**| How does agency apply to groups like teams or swarms? This requires a clear link to the rule from A.1 that any *acting group* must be modeled as a `U.System`. |

### A.13:4 - Solution

FPF's solution is threefold: establish agential participation through an obtaining system-role assignment, measure agency with a dedicated Characterization, and provide a didactic summary through a graded scale.

#### A.13:4.1 - The Core Definition: Agential participation through an exact system-role assignment

An ordinary-language **"agent"** is not a fundamental FPF type. When a precise agency claim is needed, name four things:

1. the acting holder recognized as a `U.System`;
2. the exact local agential system-role kind whose membership criterion the holder satisfies;
3. an occurrence of a directly declared `U.SystemRoleAssignment` species that assigns that kind to the holder and actually obtains; and
4. any claim scope, working situation, and time window needed by the intended use, kept separate from the assignment's identity.

This keeps a useful ordinary word without creating a universal `Agent` or `AgentialRole` kind. Classification by the local kind does not by itself establish an assignment or performed Work. Because the holder must be a `U.System`, an episteme cannot become the acting holder of this assignment.

#### A.13:4.2 - Local Agential System-Role Kinds and Their Specializations

*   **Local agential system-role kind:** A practice or source may define a local kind whose stable work-facing contribution is goal-directed action. The kind classifies candidate Systems under its own criterion; it is not a universal root kind, an assignment occurrence, or Work.
*   **Specialized agential system-role kinds:** A local practice may distinguish transformation, observation, planning, or another contribution when it supplies a real criterion for the distinction. An assignment to one such kind establishes only that assignment; any transformation, observation, plan, or performed Work still needs its own claim.

#### A.13:4.3 - Measuring Agency: The Agency Characteristic Profile and the Spectrum

Agency is not a binary switch; it is a multi-dimensional spectrum of capabilities. A.13 defines the current domain profile and attaches its measurable characteristics to the exact holder and agency claim; A.17, A.18, A.19, C.16, and A.10 govern characterization, measurement, and evidence. Planned **C.9 Agency Characteristic Profile** may later consolidate that profile but supplies no current definitions or governing force.

The agency-characteristic profile is grounded in contemporary research (e.g., Active Inference, Basal Cognition) and includes the following key characteristics. Each measurement names its exact holder and, where relevant, its task family or work target, claim scope, working situation, and time window; A.10 supplies the evidence basis.

1.  **Boundary Maintenance Capacity (BMC):** The ability of the system to maintain its structural and functional integrity against perturbations. *(How robust is it?)*
2.  **Predictive Horizon (PH):** The temporal or causal depth of the holder's internal model. *(How far ahead can it "see"?)*
3.  **Model Plasticity (MP):** The rate at which the agent can update its internal model (`U.GenerativeModel`) in response to prediction errors (`U.Error`). *(How quickly can it learn?)*
4.  **Policy Enactment Reliability (PER):** The probability that the agent will successfully execute its chosen `U.Method` under operational conditions. *(How reliably does it do what it decides to do?)*
5.  **Objective Complexity (OC):** A measure of the complexity of the `U.Objective` the holder can pursue, from simple set-points to abstract, multi-scale goals.

##### A.13:4.3.1 - Task-family specialization claims

When Work shifts to a new `TaskFamily`, describe evidence-backed specialization for that task family and work target rather than greater intelligence in general. Keep the task family, work target, claim scope, working situation, measurement window, work-measure threshold, adaptation budget, and provenance basis as separate values. The same holder may show different specializations for different task families without becoming a new U-kind; the claim here is **time-to-usable specialization** for the stated task family and target.

Low-human-overlap or newly discovered task families remain admissible when the task family, evidence basis, and reuse window are explicit by value.

#### A.13:4.4 - The Agency Grade (Didactic Layer)

While the multi-dimensional agency-characteristic profile is essential for formal assurance, engineers and managers need a simpler, at-a-glance summary. The **Agency Grade** is a **non-normative, didactic** scale from 0 to 4 that synthesizes the profile into an intuitive autonomy grade.

| Grade | Label | Typical agency-characteristic profile (Conservative Lower Bound) | Archetypal Example |
| :--- | :--- | :--- | :--- |
| **0** | **Non-Agential** | `BMC ≈ 0`, `PH ≈ 0`, `MP ≈ 0` | A rock, a document, a passive structural component. |
| **1** | **Reactive** | `BMC > 0`, `PH ≈ 0`, `MP ≈ 0` | A thermostat; a simple feedback controller. Follows fixed rules. |
| **2** | **Predictive** | `BMC > 0`, `PH > 0`, `MP ≈ 0` | A model-predictive controller with a fixed model; a chess engine that plans moves but doesn't learn new strategies. |
| **3** | **Adaptive** | `BMC > 0`, `PH > 0`, `MP > 0` | A self-calibrating sensor system; a machine learning agent that updates its model with new data. |
| **4** | **Reflective/Strategic** | High `BMC`, `PH`, `MP`, `PER`, and `OC`. Capable of meta-cognition (reasoning about its own reasoning) and pursuing abstract goals. | An autonomous R&D system; a cohesive, self-organizing DevOps team. |

**Crucial Distinction:** The agency-characteristic profile is the **normative evidence**. The Grade is a **pedagogical shortcut**. A holder cannot claim an Agency Grade without having a corresponding, auditable characteristic profile to back it up.

### A.13:5 - Archetypal Grounding

The cases below apply the same test to individual and collective Systems, and then contrast them with a knowledge artifact. Each positive case names the holder, one illustrative local agential system-role kind, and one distinct assignment occurrence that relates that holder to that kind. The characteristic sketch and grade remain separate claims. The names are didactic examples, not a universal `AgentialRole` vocabulary.

| Archetype | Holder (`U.System`) | Illustrative local agential system-role kind | Distinct obtaining assignment occurrence | Agency-characteristic profile sketch | Resulting Agency Grade |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Simple Controller** | `Thermostat_Model_T800` | `HomeHeatingController` | `T800-home-heating-assignment` assigns `Thermostat_Model_T800` to `HomeHeatingController` for the stated household-temperature-control use. | `BMC`: High (maintains temperature). <br> `PH`: Zero (no prediction). <br> `MP`: Zero (fixed logic). <br> `PER`: Very High. <br> `OC`: Low (single set-point). | **Grade 1 (Reactive)** |
| **Advanced Controller** | `PredictiveCruiseControl_v3` | `VehicleDynamicsController` | `PCC-v3-vehicle-dynamics-assignment` assigns `PredictiveCruiseControl_v3` to `VehicleDynamicsController` for the stated driving situation. | `BMC`: High. <br> `PH`: High (predicts traffic flow). <br> `MP`: Zero (fixed model). <br> `PER`: High. <br> `OC`: Medium (optimization). | **Grade 2 (Predictive)** |
| **Learning System** | `SelfCalibratingSensorArray` | `IndustrialProcessAdaptiveController` | `sensor-array-process-adaptation-assignment` assigns `SelfCalibratingSensorArray` to `IndustrialProcessAdaptiveController` for the stated calibration task family and window. | `BMC`: High. <br> `PH`: High. <br> `MP`: Medium (learns drift). <br> `PER`: High. <br> `OC`: Medium. | **Grade 3 (Adaptive)** |
| **Collective acting holder** | `DevOpsTeam_Phoenix` (a collective `U.System`) | `ProjectPhoenixDeliveryCoordinator` | `phoenix-team-delivery-assignment` assigns the collective System `DevOpsTeam_Phoenix` to `ProjectPhoenixDeliveryCoordinator` for the stated project work. | `BMC`: High (maintains delivery capacity). <br> `PH`: High (release planning). <br> `MP`: High (retrospectives). <br> `PER`: Medium-High. <br> `OC`: High (abstract business goals). | **Grade 4 (Reflective/Strategic)** |
| **Knowledge artifact** | No acting holder. `ISO_26262_Standard.pdf` is a file carrier; the selected standard edition and any exact claim episteme made available through it remain distinct. | **N/A** | **N/A**: neither the carrier nor an episteme is a `U.System`, so neither can receive an agential system-role assignment. | N/A | **Grade 0 (Non-Agential)** |

**Key takeaway from grounding:**
The same ontology works for a thermostat, a predictive controller, a learning System, and a collective System: classification by a local kind and an obtaining assignment are both stated, while scope, situation, Work, evidence, profile, and grade remain separate. An exact ISO claim episteme may be cited in an A.10 evidence-use or B.3 reliance claim when that relation actually obtains; its file carrier merely bears a publication form. Neither the citation nor the publication acts.

### A.13:6 - Conformance Checklist

To ensure the agency model is applied rigorously and consistently, all FPF publications must adhere to the following normative checks.

| ID | Requirement (Normative Predicate) | Purpose / Rationale |
| :--- | :--- | :--- |
| **CC-A13.1 (Holder Type)** | The holder System of an obtaining agential `U.SystemRoleAssignment` **MUST** be a `U.System`. | Prevents the "episteme-as-actor" category error. Enforces **Strict Distinction (A.7)**. |
| **CC-A13.2 (Assignment Mandate)** | A precise claim of agency **MUST** name the exact local agential system-role kind and an obtaining occurrence of a directly declared `U.SystemRoleAssignment` species. Any claim scope, working situation, and time window needed by the use remain separate. | Binds agency to a specific holder and assignment without turning a generic context field into their identity. |
| **CC-A13.3 (Characteristic Evidence)** | Any claim about a holder's Agency Grade or autonomy profile **MUST** be substantiated by an auditable agency-characteristic profile with Evidence Graph Ref (A.10). | Makes claims of agency falsifiable and prevents "agency by marketing." |
| **CC-A13.4 (Grade is Didactic)**| The **Agency Grade (0-4)** **SHALL NOT** be used as a normative input for formal reasoning. It is a didactic summary of the agency-characteristic profile. | Prevents oversimplification in formal models. The detailed profile, not the summary grade, must be used for assurance cases. |
| **CC-A13.5 (Collective as System)** | To claim agency for a collective (e.g., a team, a swarm), the collective **MUST** first be modeled as a `U.System` with a defined `U.Boundary` and a coordination `U.Method`. | Prevents the error of assigning agency to a mere set or collection (`MemberOf`). Aligns with **A.1** and **A.14**. |
| **CC-A13.6 (MHT for Emergent Agency)** | If a collection of systems, previously non-agential or at a lower grade, develops a new supervisory structure and crosses a documented agency-characteristic threshold, a **Meta-Holon Transition (MHT, B.2)** **MUST** be declared. | Makes the emergence of collective agency an explicit, auditable event, preventing "magic" emergence. |

### A.13:7 - Consequences

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Category Safety & Clarity:** The pattern provides a clear, unambiguous definition of agency that prevents common modeling errors and is consistent across all of FPF. | **Increased Modeling Granularity:** Requires practitioners to distinguish the local system-role kind, classification, obtaining assignment, and any performed Work, and to state scope or window only when it changes the claim. *Mitigation:* Use the short ordinary-language claim first; expose identifiers only when a receiving use needs them. |
| **Falsifiable & Measurable Agency:** By grounding agency in the agency-characteristic profile, the framework transforms a vague philosophical concept into a set of concrete, evidence-backed engineering properties. | **Measurement Effort:** Populating the profile requires real work (testing, analysis, data gathering). *Mitigation:* The profile can be built iteratively. An initial estimate can be used, with the understanding that its `Reliability (R)` score is low until backed by evidence. |
| **Scalable Autonomy Model:** The graded scale provides a sophisticated language for describing and comparing different Agency Grades, from simple automation to strategic intelligence. | **Risk of Misinterpreting Grades:** The simple 0-4 scale could be misused as a simplistic marketing label. *Mitigation:* The normative requirement (**CC-A13.4**) to always link a grade to its underlying CHR profile acts as a guardrail against this. |
| **Elegant Handling of Collectives:** The pattern provides a clean way to model the agency of teams, swarms, and organizations without violating ontological principles. | - |

### A.13:8 - Rationale

This pattern's value comes from its synthesis of contemporary, post-2015 research into a single, operational model.

*   **Grounded in Science:** The move away from a binary, type-based view of agency towards a **graded, spectrum-based model** is directly aligned with modern research in Active Inference (Friston et al.), Basal Cognition (Fields, Levin), and evolutionary cybernetics. The agency-characteristic profile provides a direct, practical implementation of these ideas.
*   **Ontologically Sound:** Agential participation uses an exact local system-role kind and a separately obtaining `U.SystemRoleAssignment` instead of a new base type. Holder, kind, classification, assignment, performed Work, claim scope, and time window remain distinct. This follows **Strict Distinction (A.7)** without making the practitioner carry a universal context tuple.
*   **Pragmatic and Actionable:** The pattern is designed for engineers and managers. The `Agency Grade` provides a quick communication tool, while the underlying agency-characteristic profile provides the detailed, auditable data needed for formal assurance and risk management. This duality satisfies both **Didactic Primacy (P-2)** and **Pragmatic Utility (P-7)**.

In essence, this pattern does not *invent* a new theory of agency. It **distills and operationalizes** the emerging scientific consensus, packaging it into a rigorous, falsifiable, and practical tool for the FPF ecosystem.

### A.13:9 - Relations

*   **Builds on:**
    *   `A.1 Holonic Foundation`: Establishes that only `U.System`s can be bearers of behavioral roles.
    *   `A.2 System-Role Kinds and Assignments`: Distinguishes an exact local system-role kind, classification by that kind, and an obtaining `U.SystemRoleAssignment`.
    *   `A.12 External Transformer`: Work by an acting holder is modeled using the external transformer principle.
*   **Coordinates with:**
    *   `B.2 Meta-Holon Transition (MHT)`: A significant jump in the agency-characteristic profile of a collective can trigger an MHT.
    *   `B.3 Trust & Assurance Calculus`: The agency-characteristic profile provides crucial inputs for assessing the reliability and safety of an autonomous system.
    *   `D.2 Multilevel Ethics For System-Holon Work`: The Agency Grade is used to determine the moral-responsibility posture and accountability assigned to a system.
*   **Future consolidation:**
    *   Planned `C.9 Agency Characteristic Profile` may later consolidate the characteristics (BMC, PH, etc.), but provides no current definitions or governing force; the current profile is defined here and measured under A.17/A.18/A.19/C.16/A.10.

### A.13:End

