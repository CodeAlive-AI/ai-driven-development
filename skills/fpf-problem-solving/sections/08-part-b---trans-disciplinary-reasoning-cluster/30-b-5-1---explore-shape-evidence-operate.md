## B.5.1 - Explore → Shape → Evidence → Operate

### B.5.1:1 - **Problem Frame**

Use this state model when a development project needs a shared account of whether a `U.Episteme` or `U.System` is being explored, shaped, evaluated or operated. The practical gain is to make the current development focus and the conditions for an intended transition visible. Without that distinction, a team may refine a design indefinitely or claim operational readiness before the required validation.

A development state describes the project's treatment of its subject, not the assurance of every claim about it. A qualified explanation, proof or empirical result may already answer its receiving question while development remains in an earlier state. Ordinary use of that result needs no new development-state assignment.

### B.5.1:2 - **Problem**

How can a project coordinate concept development and operational readiness without confusing completion of its present task, the subject's development state and the support for a particular claim?

### B.5.1:3 - **Solution**

Use the four development states to name the current focus for the episteme or system under development. For an intended transition, identify the design, evidence and operational conditions that actually need to hold. The Canonical Reasoning Cycle (B.5) can supply the relevant reasoning contributions; the state names do not prescribe an assurance ladder.

**The Four Development States:**

| State | Core Activity | Manager's View: What It Means | Reasoning Contribution | What the state leaves to the receiving claim and use |
| :--- | :--- | :--- | :--- | :--- |
| **1. Exploration** | **Generating possibilities.** Frame the problem and compare candidate explanations or designs. | "We are looking for a plausible direction and keeping the serious alternatives visible." | **Abduction** (B.5.2) | A qualified conjecture may be sufficient for the present question; its origin does not assign `L0`. |
| **2. Shaping** | **Defining a coherent form.** Develop the selected direction and derive its relevant consequences. | "We are making the design and its implications clear enough for the next intended use." | **Deduction** | Logical support concerns the consequence under its premises. A coherent design alone does not establish actual performance. |
| **3. Evidence** | **Evaluating the relevant claims.** Use applicable empirical or formal results and obtain missing evidence when it is required and feasible. | "We are deciding whether the needed claims are supported in the intended conditions." | **Empirical evaluation and applicable formal reasoning** | Relevant existing support can be sufficient. A passed test does not automatically confer a higher assurance level. |
| **4. Operation** | **Using in a live environment.** Begin or continue the intended operation and monitor what its actual conditions require. | "The system or episteme is in use, with the required operational conditions in place." | **Reasoning about operating observations and needed changes** | Readiness and continuing use depend on the actual qualification, protective and authority conditions, not maintained `L2`. |

B.3.3 governs any assurance conclusion about the particular claim and receiving use. Retain an applicable domain profile, proof obligation or validation requirement where that use requires it. Existing results count only when they cover the present conditions; a missing required result can block the intended transition. A proposal to improve an excessive requirement does not waive a currently binding condition.

> **Didactic Note for Managers: Aligning States with Your Project Plan**
>
> Exploration can describe discovery, Shaping design, Evidence evaluation, and Operation live use and maintenance. Name the subject and the intended transition so that the team can tell what remains to be done. Completing a useful answer during Exploration does not mean that the developed system has entered Operation, nor that the answer must wait for every later project state.

**Worked case.** A service team completes B.5.2's latency-spike inquiry with a qualified backup-interaction conjecture and live rivals. The possible causal probe is unavailable, so the explanatory result remains limited. An existing operational qualification separately supports a permitted diversion to a spare instance for this traffic and interval. The team can use that basis for the diversion without declaring the explanation validated or advancing a new design through Evidence. If the team instead proposes a new deployment whose required load test is missing, that deployment remains blocked; the useful conjecture does not supply the missing qualification.

### B.5.1:4 - **Conformance Checklist**

* **CC-B5.1.1 (State Explicitness):** A state-bearing `U.Episteme` or `U.System` coordinated through this development model **MUST** be tagged with its current state from {Exploration, Shaping, Evidence, Operation}. Identify the development subject; a separate bounded result need not be given that subject's state.
* **CC-B5.1.2 (Sequential Progression):** When advancing the development subject through this cycle, the project **SHALL** follow the state sequence. A departure **MUST** be justified against the intended transition's actual prerequisites; it cannot waive binding proof, validation or operational conditions. Completing or using a sufficient bounded result without advancing the development subject is not a skipped state and needs no skip justification.
* **CC-B5.1.3 (Reasoning Cycle Alignment):** A transition **MUST** have the reasoning contributions and results needed by its applicable project and domain conditions. Before a hypothesis-led test, derive the consequences needed to interpret it. Reuse applicable prior reasoning or evidence when it meets those conditions; repeat a phase only for an actual unresolved need. Phase completion alone **SHALL NOT** confer an assurance level or operational permission.

### B.5.1:5 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Clear Project Visibility:** The states give a shared language for the development focus and intended transition. | **Risk of Bureaucracy:** Treating states as a universal evidence recipe can create unnecessary work. Use the actual transition conditions and reuse covering results. |
| **Improved Focus:** Exploration, design, evaluation and live operation have distinguishable immediate questions. | A result can serve another use without changing the development subject's state; keep those two judgements separate. |
| **Reduces "It's Done" Ambiguity:** The team can say whether it completed the present answer, the design or the conditions for operation. | A state label cannot replace the applicable readiness criteria. |

### B.5.1:6 - **Rationale**

This pattern operationalizes the **Principle of State Explicitness (P-9)** for development coordination. The four states make the project's focus and transition obligations inspectable. B.5 supplies reasoning contributions and B.3.3 qualifies assurance for a claim and use. Keeping those questions distinct supports iterative development without requiring every useful idea or result to become an operational holon.

### B.5.1:7 - **Relations**

* **Uses reasoning contributions from:** `B.5 Canonical Reasoning Cycle`; `B.5.2 Abductive Loop` commonly supplies Exploration with qualified conjectures.
* **Uses for claim-specific assurance:** `B.3.3 Assurance Subtypes & Levels`. Development states neither organize its levels nor establish the adequacy of a claim.
* **Coordinates with:** `B.4 Canonical Evolution Loop`. Its evolution phases and these development states are not a one-to-one mapping.

### B.5.1:End
