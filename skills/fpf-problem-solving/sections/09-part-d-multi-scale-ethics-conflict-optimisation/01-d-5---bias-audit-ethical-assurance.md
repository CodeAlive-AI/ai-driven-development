## D.5 - Bias-Audit & Ethical Assurance

**Use this when.** Use this pattern when a holon, model, metric, decision system, policy, or authored FPF claim may create unfair, biased, or ethically unsafe effects for people or groups. If the fairness claim is causal — for example "this intervention is fair", "this policy would have prevented harm", "this model is counterfactually fair", or "this practice causally reduces disparity" — keep the ethical audit in `D.5` and cite `C.28` for causal-use question, causality-ladder rung, estimand, causal evidence support basis, identification, realizability, evidence design, support record, and support verdict.

**Not this pattern when.** If the live question is only measurement construction, use `C.16`; if it is only causal-use support without fairness or ethical audit, use `C.28`; if it is only an assurance claim or assurance support posture, use `B.3`. Metric disparity alone is not yet causal fairness.


**Causal-fairness boundary.** A local `C.28` causal-fairness repair, such as adding a causal-use question, estimand, support basis, support record, or supported-fairness-use and unsupported-fairness-use pair, is not by itself the Bias-Audit Cycle. It remains a local support repair until the claim, model, metric, policy, or decision system is in a `D.5` project, release, assurance, or human/group-impact audit condition.

### D.5:1 - **Problem Frame**

FPF is designed to produce reliable, objective, and trustworthy holons. However, formal correctness (`FV` score) and empirical validation (`EV` score) are not sufficient on their own. Any record, model, metric, policy, or decision system designed by humans or trained on human-generated data is susceptible to hidden cognitive, cultural, and algorithmic biases. A perfectly verified control system can still be unsafe if its requirements were based on a biased assumption about operator behavior. A highly accurate machine learning model can be deeply unfair if its training data was not representative.

A fairness claim can also be unsafe by causal overclaim. "This policy is fair because a metric improved" is not the same claim as causal fairness, counterfactual fairness, or path-specific fairness. `D.5` therefore brings causal fairness into the audit entry surface: the audit must distinguish metric disparity, associative fairness evidence, interventional fairness proxy, and counterfactual fairness claim before the ethical assurance record is treated as supported.

### D.5:2 - **Problem**

Without a formal, repeatable method for surfacing and mitigating these biases, FPF models risk becoming "flawed by design." This leads to three critical failure modes:

1.  **Systemic Harm:** The deployed holon, despite meeting all its technical specifications, causes unintended negative consequences for certain groups or in certain contexts.
2.  **Eroded Trust:** Stakeholders or the public lose trust in the system (and its creators) when its inherent biases are exposed after deployment.
3.  **Hidden Risk:** The assurance case looks well-supported on paper, but it is built on a foundation of unexamined and potentially dangerous assumptions, creating a significant hidden risk.

### D.5:3 - **Forces**

| Force | Tension |
| :--- | :--- |
| **Objectivity vs. Inevitable Subjectivity** | How to strive for objective, neutral models while acknowledging that all creation is influenced by the subjective perspectives of the creators. |
| **Speed of Delivery vs. Depth of Reflection** | How to integrate a thoughtful ethical review process without paralyzing ordinary iterative work cycles. |
| **Expertise vs. Inclusivity** | How to leverage specialized ethical expertise without disenfranchising the core engineering team from moral responsibility. |
| **Process vs. Culture** | Is ethical assurance a bureaucratic checklist to be completed, or a cultural practice of continuous self-critique? |

### D.5:4 - **Solution**

FPF introduces the **Bias-Audit Cycle (BA-Cycle)**, a lightweight, iterative review loop designed to integrate ethical reflection directly into the engineering development cycle. It is not a one-time gate but a continuous loop of inquiry.

#### D.5:4.1 - The Bias-Audit Cycle: Four Phases

The cycle consists of four distinct phases, aligned with the project's natural rhythm.

| Phase | Trigger | Core Activity | Output |
| :--- | :--- | :--- | :--- |
| **BA-0: Kick-off** | Project start or major new feature. | **Framing the ethical scope.** The team identifies potential areas of bias and creates an initial, living document called the **Bias Register**. | A skeleton Bias Register with initial questions. |
| **BA-1: Rapid Scan**| End of each sprint or design session. | **Continuous lightweight check.** A rotating member of the core team (the *Engineer-Scrutineer*) quickly scans recent changes against a checklist, flagging potential issues in the Bias Register. | Updated Bias Register with new items flagged for discussion. |
| **BA-2: Panel Review**| Before a major integration or release decision (e.g., before moving to the `Evidence` state). | **Deep, multi-perspective critique.** A small panel, including individuals in roles like **Ethicist**, **Domain Sociologist**, and **UX Design Critic**, reviews the flagged items and proposes concrete mitigations. | A structured, auditable record called the **Bias-Audit Report**, documenting findings and required actions. |
| **BA-3: Closure** | At the release freeze. | **Ensuring accountability.** The facilitator confirms that all "blocking" issues from the Bias-Audit Report have either been resolved or have a documented, accepted risk. | The final Bias-Audit Report is marked as *resolved* or *risk-accepted* for that release. |

#### D.5:4.2 - The Bias Taxonomy: A Shared Language for Critique

To structure the audit, FPF provides a minimal, extensible taxonomy of common bias categories.

| Code | Bias Category | Manager's View: The Simple Question to Ask |
| :--- | :--- | :--- |
| **REP** | **Representation Bias** | "Whose voice, data, or perspective is missing from this model?" |
| **ALG** | **Algorithmic Bias** | "Could our automated rule or formula unintentionally amplify unfairness for minority or edge cases?" |
| **VIS** | **Visual Framing Bias** | "Does this diagram, color choice, or dashboard visualization steer the user towards a preferred conclusion?" |
| **MET** | **Metric Proxy Bias** | "Are we chasing a metric that is easy to measure, at the expense of the real, harder-to-measure objective?" (Connects to ADR-015) |
| **LNG** | **Lexical Bias** | "Do our naming choices (e.g., 'master/slave', 'blacklist/whitelist') encode unintended value judgments or historical baggage?" |

> **Didactic Note for Managers: This is Risk Management, Not a Philosophy Seminar**
>
> The Bias-Audit Cycle is FPF's "immune system." It's designed to find and neutralize hidden assumptions before they become costly product failures or public relations disasters. Think of it like a security audit, but for the ethical and social integrity of your system.
>
> *   **It's not about being "perfect"; it's about being "aware."** The goal is not to eliminate all bias (an impossible task) but to make your team's biases explicit, documented, and consciously managed.
> *   **It's cost-effective.** The lightweight "Rapid Scan" catches most issues early, during a sprint. The more intensive "Panel Review" is reserved for key moments, ensuring that expert time is used efficiently.
> *   **It creates a defensible record.** The Bias-Audit Reports provide a clear, auditable trail showing that your team has taken a systematic and responsible approach to identifying and mitigating potential harms. In an era of increasing scrutiny on AI and autonomous systems, this record is not just good practice—it's a critical business asset.

#### D.5:4.3 - Normative Artifacts

The Bias-Audit Cycle produces two key records that serve as the auditable record of ethical deliberation.

*   **The Bias Register:**
    *   **Nature:** A living, evolving **episteme** that serves as a repository of questions, concerns, and potential biases identified throughout a holon's evolution.
    *   **Content:** It is a structured collection of inquiries, organized by the Bias Taxonomy (REP, ALG, etc.). It is continuously updated during the Rapid Scans (BA-1) and represents the "running log" of ethical and bias-related considerations for the project.

*   **The Bias-Audit Report:**
    *   **Nature:** A formal, versioned **episteme** that documents the findings of the Panel Review (BA-2).
    *   **Content:** It contains a structured record of findings. Each finding is a `U.Episteme` with attributes for:
        *   `biasCode`: The category from the Bias Taxonomy.
        *   `severity`: An ordinal level (`high`, `medium`, `low`).
        *   `description`: A narrative explaining the issue.
        *   `mitigation`: A proposed `U.Method` or `U.ConstraintRule` to address the issue.
        *   `status`: A state (`blocking`, `resolved`, `risk-accepted`).
    *   **Conceptual Example:**
        *   `finding-01`: An episteme with `biasCode: REP`, `severity: high`, and a `description` stating that the training data for a recognition holon lacks representation from certain demographics. The `mitigation` would be a `U.Method` for acquiring a balanced dataset, and the `status` would be `blocking` until this method is executed and its outcome validated.

#### D.5:4.4 - Causal fairness use audit

When a fairness claim is causal rather than metric-only, `D.5` records the ethical-audit question and cites `C.28` for causal-use support:


```text
CausalFairnessUseAuditCard {
  causalUseQuestionRef: U.CausalUseQuestion
  protectedVariableRef
  decisionVariableRef
  outcomeVariableRef
  fairnessCausalityLadderRung: CausalityLadderRung
  fairnessEstimandRef: U.CausalEstimand
  permittedPathSet?
  prohibitedPathSet?
  pathSpecificFairnessEstimandRef?
  pathSpecificExcessLossRef?
  comparatorOrCounterfactualRef
  causalEvidenceSupportBasis: CausalEvidenceSupportBasis
  causalIdentificationProfileRef?
  counterfactualSamplingRealizabilityProfileRef?
  causalUseEvidenceDesignRef?
  causalUseSupportRecordRef?
  causalUseSupportVerdict: CausalUseSupportVerdict
  fairnessCausalEthicalConstraintRef?
  supportedFairnessUse
  unsupportedFairnessUse
}
```

Metric-only fallback: if only a metric disparity is claimed and no causal fairness use is made, record it as metric/evaluation use, not `C.28`-heavy causal fairness.

Local causal-fairness repair does not by itself trigger the full Bias-Audit Cycle, a panel review, or release-cycle duties. It may only downgrade causal wording, add the missing `C.28` support reference, or mark unsupported causal fairness use.

The full `D.5` duties activate under `D.5` project or release conditions: the holon, model, metric, decision system, policy, or authored claim may materially affect people or groups; the fairness/ethical claim is release-bearing; or the local causal-fairness repair becomes an input to audit, assurance, deployment, publication, or risk acceptance.

Fairness escalation rule: interventional-action proxy may support bounded interventional fairness use but cannot be published as counterfactual fairness.

What changes in practice: a fairness audit must say whether the claim is associative, interventional, or counterfactual, and a counterfactual fairness claim must carry the causal-use question, comparator/counterfactual, permitted paths, prohibited paths, causal evidence support basis, causal identification or counterfactual sampling realizability, causal-use support verdict, and supported fairness use and unsupported fairness use.

What this does not authorize: `D.5` does not replace `C.28` for causal-use question, causality-ladder rung, estimand, identification, realizability, or `CausalUseSupportVerdict`; it keeps ethical audit and fairness assurance, while `B.3` keeps assurance claim support and non-admissible-use consequences.


### D.5:5 - **Conformance Checklist**

*   **CC-D5.1 (Cycle Mandate):** Any project developing a holon that interacts with or makes decisions about humans **MUST** conduct the Bias-Audit Cycle.
*   **CC-D5.2 (Artifact Mandate):** The project **MUST** maintain a **Bias Register** and produce a **Bias-Audit Report** before any major release.
*   **CC-D5.3 (Blocking Issue Mandate):** A release **SHALL NOT** be considered conformant if its latest Bias-Audit Report contains any unresolved findings with `status: blocking`. The issue must either be moved to `resolved` (mitigated) or `risk-accepted` (formally signed off by a designated authority).
*   **CC-D5.4 (Role Mandate):** The Panel Review (BA-2) **MUST** involve at least three individuals representing distinct perspectives, ideally aligning with the roles of *Ethicist*, *Domain Sociologist*, and *UX Design Critic* from the Intellect Stack.
*   **CC-D5-CF-1:** A fairness claim MUST declare whether it is associative, interventional, or counterfactual.
*   **CC-D5-CF-2:** An interventional-action-rung fairness proxy MUST NOT be published as a counterfactual-rung fairness result.
*   **CC-D5-CF-3:** If a counterfactual fairness estimand is claimed actionable, it MUST cite `CausalIdentificationProfile` or `CounterfactualSamplingRealizabilityProfile`.
*   **CC-D5-CF-4:** A causal fairness audit MUST cite `C.28` for causal-use question, causality-ladder rung, causal estimand, causal evidence support basis, identification, realizability, evidence design, `causalUseSupportRecordRef` when one is consumed, and `CausalUseSupportVerdict`; `D.5` keeps ethical audit and fairness assurance.
*   **CC-D5-CF-5:** A local causal-fairness wording repair or support-reference repair does not trigger the full Bias-Audit Cycle unless `D.5` project, release, assurance, or human/group-impact audit conditions are live.


### D.5:6 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Ethics Ghetto"** | One person is the "ethics officer," and the rest of the engineering team sees bias as "not my job." | The **Rapid Scan (BA-1)** is a conceptual activity performed by a rotating member of the core team. This distributes the responsibility for ethical reflection across all roles. |
| **The "Checklist Charade"** | The team mechanically answers "yes/no" to bias questions just before a release, without any real reflection, simply to satisfy a process requirement. | The **Panel Review (BA-2)** is a moment of deep, multi-perspective critique that a perfunctory checklist cannot survive. The requirement for a structured **Bias-Audit Report** also forces concrete findings and mitigation methods, not just checkmarks. |
| **The "Bias Whack-a-Mole"** | The team fixes one bias issue, only for another to pop up, because they are only addressing symptoms. | The **Bias Taxonomy** encourages a more systematic approach. By considering categories like Representation (REP) and Metric Proxy (MET), the team is prompted to look for root causes (e.g., flawed data collection methods or poorly chosen objectives) rather than just patching individual algorithmic flaws. |

### D.5:7 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Proactive Risk Mitigation:** The cycle surfaces and addresses potential ethical and social harms *before* they are deployed, preventing costly failures and reputational damage. | **Additional Ceremony:** The cycle introduces extra review steps and records into the work cycle. *Mitigation:* The process is designed to be lightweight and to align with ordinary iteration cadences (e.g., the Rapid Scan is a brief conceptual check at the end of a work cycle). |
| **Creates an Auditable Ethical Record:** The Bias-Audit Reports provide a transparent, defensible trail demonstrating that the organization has a systematic process for managing ethical risks. | **Finding the Right Expertise:** It may be challenging to find individuals to fill the required roles. *Mitigation:* These roles represent perspectives, not necessarily formal job titles. The key is the diversity of viewpoints. |
| **Builds a Culture of Responsibility:** By making ethical reflection a routine part of the engineering process, the cycle fosters a culture where every team member is empowered and expected to think critically about the broader impact of their work. | - |
| **Improves Holon Quality:** Designing for a wider range of users and edge cases, as prompted by the audit, often leads to more robust, user-friendly, and innovative holons. | - |

### D.5:8 - **Rationale**

Formal correctness is not a substitute for moral responsibility. This pattern recognizes that bias is not an occasional flaw but a systemic feature of any human-led design process. The Bias-Audit Cycle is FPF's formal mechanism for managing this reality. It is a direct implementation of the **Cross-Disciplinary Bias Audit Guard-Rail (E.5.4)**.

By integrating this cycle into the core engineering work cycle, FPF moves ethical assurance from a peripheral, often-ignored "nice-to-have" into a central, non-negotiable component of engineering excellence. It ensures that the powerful tools of formal reasoning and validation provided by FPF are always directed towards creating holons that are not only correct, but also conscionable.

### D.5:9 - **Relations**

*   **Implements:** The `Cross-Disciplinary Bias Audit` Guard-Rail (E.5.4).
*   **Complements:** `D.4 Trust-Aware Mediation Calculus` by providing inputs on fairness and value alignment; `B.3.4 Evidence Decay & Epistemic Debt` by questioning the longevity of assumptions about social context.
*   **Coordinates with:** `C.28` for causal fairness use, causality-ladder rung, causal estimand, causal evidence support basis, identification, realizability, evidence design, causal-use support record, and causal-use support verdict; `B.3` for assurance claim support and unsupported-use consequences.
*   **Operationalizes:** The conceptual roles of `Ethicist`, `Domain Sociologist`, and `UX Design Critic` from the Intellect Stack.

### D.5:End


