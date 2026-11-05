## B.4 - Coordinate Repeated Adaptation (Canonical Evolution Loop)
> **Status:** Stable
> **Type:** Pattern

**Use this when.** Use this pattern when repeated adaptation needs a connection between a subject's use, observations about it, a proposed or actual change, and renewed use. Identify the subject and its continuity question: a System, episteme, Method, MethodDescription, or sequence of distinct Work occurrences. Describe the activity and results needed for that connection; use the dated Work branch in B.4:4.2 when the receiving claim needs particular `U.Work` occurrences.

**What goes wrong if missed.** Teams treat drift, learning, release, and improvement as unrelated events. Specifications become stale, findings lose the evidence needed for their use, and changes appear without a clear basis or treatment of the subject's continuity. When particular Work is asserted, its performer and admission grounds can also be missing. At the opposite extreme, one generic loop is imposed on every subject: a description edit is called a Method change, completed Work is said to be revised, or an internal adaptation is rejected because its acting System is not external.

**What this buys.** An adaptation account whose identity rule comes from the subject pattern. It connects the observed basis, change and use while keeping the activities, evidence, publication, acceptance and responsibility claims that matter distinct.

**Not this pattern when.** Not this pattern when one direct subject-pattern claim answers the change question without a repeated adaptation cycle. Use the direct relation pattern for relation grounding, adding `B.3.5` when its working-model assurance profile is required. Use `B.4.1` to publish candidate routes from a stabilized cue, `B.5.2` for abductive hypothesis work, `C.27` for temporal status, or `A.15` for method/work alignment without an adaptation-loop claim.

### B.4:1 - **Problem Frame**

The FPF is built on the **Principle of Open-Ended Evolution (P-10)**: continued use can reveal reasons to adapt a System, an episteme, a Method, or a description. The useful commonality is a repeated move from use through an observed basis and an explicit change back to use. The identity question is not common. The same subject may continue through a change, a successor may be identified, or later dated Work may be a distinct occurrence rather than a revision of earlier Work. Use the relevant subject pattern to settle that distinction or retain the open continuity question while coordinating the next needed contribution.

### B.4:2 - **Problem**

When use, observation, and change are disconnected, three failures can follow:

1. **Design-reality divergence:** The subject in use diverges from its design-time account. Models and assurance cases can continue to describe conditions that no longer hold.
2. **Unused findings:** A finding that calls for a response has no usable path to the needed decision, change or renewed use. "Lessons learned" remain static documents.
3. **Unexplained change:** Reactive patches have no stated observed basis, identity decision, or return-to-use condition. Hidden dependencies and unintended consequences accumulate.

### B.4:3 - **Forces**

| Force | Tension |
| :--- | :--- |
| **Stability vs. Change** | How to adapt while retaining the identity and assurance commitments that still hold. |
| **Learning vs. Operating** | How to keep use stable enough to serve its purpose while gathering and acting on evidence. |
| **Top-Down Intent vs. Bottom-Up Reality** | How to connect intended improvement with what actual use reveals. |

### B.4:4 - **Solution**

Use the **Canonical Evolution Loop** to connect the parts of repeated adaptation needed by the current question. Recover the subject and its continuity rule, then identify the relevant activities, results and dependencies. Keep proposed steps distinct from phases that occurred; use B.4:4.2 when a claim needs particular dated Work.

Start from the available observations and results. If they answer the receiving question, return that result without requiring another phase. Keep the current subject and use when those grounds support doing so. If a needed premise remains unresolved, state that limit and the contribution still needed. Develop a change or gather further evidence when the remaining decision requires it, reusing adequate results whose conditions still hold.

#### B.4:4.1 - Name the subject and continuity question

| Subject kind | State before using the shared cycle |
| :--- | :--- |
| **System** | Name the current System and the relevant continuity or transformation rule. State whether the changed System remains the same System or whether a successor System is identified. Use `A.1` for System recognition, `A.3.4` for an actual bounded change of the continuing System, and `A.15.PROD` when the claim concerns first existence through production Work. |
| **Episteme** | Identify the episteme or epistemes actually involved under `C.2.1`. Assert an `EpistemeEditionRelation` only when its historical-continuation conditions obtain. State replacement or another direct relation only when its own grounds obtain; retain any unresolved continuity question. |
| **Method** | Identify the current Method under `A.3.1`. If intended results, participant meanings, admissible conditions, safety bounds, semantic basis, acceptance criteria, or composition change, state whether the result is a refinement, substitute, or distinct successor Method. Use `B.1.5` when order-sensitive composition is current. |
| **MethodDescription** | Identify each exact claim-bearing episteme under `A.3.2` and `C.2.1`, and any obtaining edition relation. A later description does not by itself change the Method it describes. |
| **Work** | Identify each dated occurrence under `A.15.1`. Completed Work is not revised: later review, repair, deployment, or follow-up is other Work, even when the occurrences belong to one longer effort. |

Not every holon is an adaptation-loop subject, and the five branches are not interchangeable. If the continuity or successor relation is still open, keep that question explicit rather than hiding it behind the word *evolution*.

#### B.4:4.2 - Separate the changed subject from the acting side

Name the acting participant separately from the subject being changed. A System performs each actual piece of Work. The changed subject, performing System, dated Work, Method enacted by that Work, and result remain distinct. Practitioner prose can still say "the engineer refined the design" or "the controller adjusted the valve" when that recognizable actor and action are enough. If that ordinary sentence is all the receiver needs, do not open a technical Work account. If B.4 identifies one particular dated `U.Work` occurrence, first recover every actual performer's A.13 core and independently admit the Work under A.15.1 from its performance history, enacted Method, temporal extent, and containing System. Add F.6 only when the receiving claim also needs precise assignment-bound attribution. A short B.4 account may omit an unused assignment identifier or classification only when every relation it consumes remains recoverable.

The performing System need not be external to the larger holon. For internal adaptation, apply the `A.12` reflexive split: identify the changed subsystem or part and the acting subsystem or part as exact, distinct participants, and establish their parthood in the containing holon independently. Use an external System when the case has one. Apply the same Work-admission and conditional attribution rules above to either acting side. State authority, responsibility, permission, acceptance, or admission through its own direct predicate, actual participants, and applicability basis; neither a phase label nor Work supplies them.

#### B.4:4.3 - Keep the four phase claims distinct

These phases distinguish questions and results, not necessarily disjoint clock intervals. Operation and observation can overlap. Identify the activities and result dependencies needed for the current transition; qualify particular Work claims under B.4:4.2.

| Phase | Current question | Output and boundary |
| :--- | :--- | :--- |
| **1. Operate** | How is the current subject actually operating or being used? | Name the current use or operation and any records that actually exist. Monitoring may occur, but a record does not by itself establish an observation, comparison, or change. |
| **2. Observe** | What do records, measurements, testimony, or other evidence show for the named use? | Identify the observation, comparison or interpretation and who carried it out when that matters. State the observed basis, finding, hypothesis or still-unclear cue under the applicable result or evidence rule, including what remains unresolved. A sufficient observation result can finish the current question before a change is selected. |
| **3. Refine** | What change, if any, does the receiving use need, and what identity relation would it have? | Develop or select a candidate change when needed. Establish the grounds required for its intended use, reusing applicable results and performing any needed revision or tests. State a continuity, successor, substitution, refinement or edition relation only when its endpoints exist and its conditions obtain; otherwise retain the identity question or intended treatment. A selected candidate alone does not establish availability for renewed use. |
| **4. Deploy** | How was the selected change made available for use? | Identify the actual deployment activity and what it established—for example, a changed or produced entity, publication, configuration, release or availability—under the rule for that fact. Acceptance, admission and actual later use remain separate claims. |

Use explicit transition conditions:

1. **Operate -> Observe:** a named cue, question, monitoring result, or review need requires interpretation.
2. **Observe -> Refine:** the remaining question requires considering a change, and an observed basis or routed cue supports forming that change question.
3. **Refine -> Deploy:** one candidate is selected, the conditions required for that deployment are met, and its subject-specific identity question or intended treatment is explicit. State an obtaining continuity, successor, substitution, refinement, or edition relation here only when both endpoints already exist; otherwise keep the question open until the relevant change or production has occurred.
4. **Deploy -> Operate:** actual renewed operation or use begins; availability alone does not close this transition.

Evidence is not a fifth phase. Evidence relations warrant the observed basis, candidate choice, transition, or renewed-use claim when a receiver relies on them. Evidence can be produced or used during several phases without duplicating those phases.

#### B.4:4.4 - Connect neighbouring cycles without collapsing them

The Canonical Reasoning Cycle (`B.5`) can supply reasoning Work within Observe and Refine. The B.5.1 development states and B.4 phases coordinate, but they are not a one-to-one implementation: a finding may reopen Exploration or Shaping, evidence use can support Evidence, and renewed use can enter or return to Operation.

When a preserve-worthy cue needs publication while its interpretation remains open, `A.16.1` supplies a `PreArticulationCuePack`. Use `B.4.1` after stabilization when a recipient needs possible continuations or a route choice made explicit. Its routed result can return to Refine or enter another subject pattern when that pattern's entry conditions hold.

Keep the account proportional. A local answer can identify the current subject, observed basis, what occurred, the supported identity conclusion or open question, and the next use or contribution still needed. A sufficient answer need not complete another phase. Expand to a complete cycle trace when a named relying decision, assurance case, audit or later replay needs it; retain missing phases as missing.

> **Didactic Note: four practical questions**
>
> 1. **Operate:** What exact subject is operating or being used now?
> 2. **Observe:** What has actual use shown, and who made the observation or interpretation when that matters?
> 3. **Refine:** What change is being considered, and would it continue or replace the subject?
> 4. **Deploy:** How was the selected change made available, and what separately established fact now supports the next use?
>
> The gain is a readable connection from an observed basis to a real change and back to use, preserving the subject's identity, the relevant activities and results, and their grounds.

### B.4:5 - **Archetypal Grounding**

The phase names can be shared, but each subject branch keeps its own identity and return-to-use rule.

* **Cue preservation and optional B.4.1 routing:**
  * **Context:** A fleet of autonomous delivery drones (`U.System`) is in operation, and operators begin to notice that winter deliveries feel "off" before a clean anomaly statement exists.
  * **Loop Example:**
    1. **Operate:** The drones perform deliveries.
    2. **Observe:** The monitoring service and named operators perform observation Work and find recurring cold-weather battery strain, but the cue still has low articulation.
    3. **Optional B.4.1 route inside Observe:** A named team performs stabilization Work. Under `A.16.1`, a `PreArticulationCuePack` preserves the cue nucleus, primary witness traces, and current language-state position without pretending that a final anomaly or action record exists; when the pack is made available for this use, name the separate publication occurrence under `E.24.PUB`. The same or another team performs routing Work. Under `B.4.1`, a `RoutedCueSet` keeps multiple continuations visible—for example, battery-chemistry investigation or route-planning adjustment; again, name its publication occurrence under `E.24.PUB` when availability matters.
    4. **Continue when needed:** When a route is selected and its entry conditions hold, it enters Refine or another fitting subject pattern. While selection remains open, retain the live routes and any unresolved conditions relevant to their use or selection. A selected change proceeds to Deploy when its required deployment conditions have been established; renewed drone operation is a further actual event.

* **Knowledge-instantiation slice (theory refinement loop):**
  * **Context:** A scientific theory of protein folding (`U.Episteme`) is used to predict structures.
  * **Loop Example:**
    1. **Operate:** Named researchers perform theory-application Work using the current theory episteme.
    2. **Observe:** A research lab performs observation Work. A separately identified `C.2.1` finding episteme states that the current theory fails to predict the structure of a protein class; name separately any `E.24.PUB` publication occurrence that makes this finding available.
    3. **Refine:** A research team performs revision and testing Work. A later theory episteme, identified under `C.2.1` from its changed claim content, includes a term for the new protein class. Assert an edition relation between the two theory epistemes only if that relation obtains.
    4. **Deploy:** The team performs publication Work for the later theory. The publication occurrence, journal acceptance, admission into a configured knowledge base, and later community use are separate relations. **Note.** If a CN-frame is used for a chart or CG-frame readings derived from this episteme, identify the chart's reference state and coordinate patch. For measured values, cite the applicable measurement method and protocol; for evaluated or otherwise ascribed values, cite the rule and basis that establish them, as required by A.19.CN CC-A19.D1-3.

  **Adaptive-specialization note.** For a bounded task-family specialization claim, identify the bearer, declared task family or work target, prior basis and the result the refinement supports. Use `C.22` for the needed `TaskFamily` or `TaskSignature` anchor. Use `C.22.1` when the receiving question concerns specialization acquisition or its claimed transfer, retention, downside or corridor entry; preserve its acquisition fields and any additional claim-specific grounds. Ordinary task-family and threshold anchoring can finish under `C.22` without an acquisition signature.

* **Method-instantiation slice (adaptive method loop):**
  * **Context:** A field-maintenance organization uses a declared inspection-and-repair Method (`U.Method`) described by one current `U.MethodDescription`.
  * **Loop Example:**
    1. **Operate:** Maintenance teams perform dated maintenance Work that enacts the current Method.
    2. **Observe:** A reviewer performs review Work and records that the time from fault detection to safe restoration repeatedly exceeds the allowed window.
    3. **Refine:** Method maintainers perform revision and testing Work. A wording clarification can yield a later MethodDescription while the same Method remains current. Adding an earlier isolation action or changing a classification checkpoint can instead change identity-bearing Method semantics; decide under `A.3.1` whether the result is a refinement, substitute, or distinct successor Method, and use `B.1.5` if its composition changes. Then identify the MethodDescription episteme that describes the chosen Method.
    4. **Deploy:** A named publishing team performs publication or release Work for the later MethodDescription and, where needed, configuration or training Work for renewed Method use. Decision results, authority, acceptance, admission, and later Work that enacts the Method remain separate. Completed maintenance Work is never revised.

  **Adaptive-specialization note.** When the method-instantiation slice carries a bounded task-family specialization claim, identify the selected specialist Method or portfolio and the grounds for its claimed fit. When the Method update is used as evidence of specialization acquisition, name the holder, dyad, team or scoped portfolio that carries that claim and explain what the Method change contributes. Use the `C.22.1` branch above for the acquisition or reuse question. Retain any budget, escalation or commit checkpoint, and fallback required by the selected plan or use.

### B.4:6 - **Bias-Annotation**

| Bias | Symptom | Correction |
| :--- | :--- | :--- |
| Self-evolution bias | The subject is said to observe, refine, or deploy itself, so the acting participant and activity disappear. | Name the changed subject and distinct acting side. Ordinary actor wording can remain short. When one particular dated `U.Work` is identified, recover each performer's A.13 core and independently admit the occurrence under A.15.1; add F.6 only when precise assignment-bound attribution is current. A short account may omit an unused assignment identifier only when every relation it consumes remains recoverable. The acting side may be external, or it may be an exact distinct subsystem or part established through the `A.12` reflexive split. |
| Design-time/run-time smear | A live operational change is treated as if it had already updated the design-time episteme, or a design-time edit as if it had already changed the System in operation. | Keep the design-time episteme, run-time System or use, deployment activity, evidence relation, and renewed use distinct. |
| Method/description smear | A MethodDescription edit is called a Method change, or a changed Method is hidden as a documentation update. | Test Method identity under `A.3.1` and composition under `B.1.5`; identify MethodDescription editions separately under `A.3.2` and `C.2.1`. |

### B.4:7 - **Conformance Checklist**

* **CC-B4.1 (Proportional loop integrity):** Connect the observed basis to the actual change and renewed use where they occurred, or to the sufficient answer or unresolved condition returned by the current question. A complete phase-by-phase trace is required only when a named relying decision, assurance case, audit or replay needs it. Keep proposed phases distinct from actual events.
* **CC-B4.2 (Subject identity):** Name the exact subject kind and apply its direct continuity rule: System continuity or transformation; episteme predecessor, successor, or edition; Method identity, refinement, substitution, or successor; MethodDescription edition; or separate dated Work occurrences.
* **CC-B4.3 (Acting-side distinction):** Work that observes or changes a subject **MUST** have an identified performing System distinct from the changed subject in that Work account. Internal adaptation is permitted when `A.12` establishes exact distinct subsystems or parts and their independently obtaining parthood. Every particular dated `U.Work` reuses each performer's A.13 core and is independently admitted under A.15.1; F.6 is added afterward only for precise assignment-bound attribution. Its short B.4 account may omit an assignment identifier unused by the receiver only when every consumed relation remains recoverable.
* **CC-B4.4 (Adaptive-specialization anchoring):** A bounded task-family specialization claim **MUST** identify its bearer, declared `TaskFamily` or `TaskSignature`, work target, claimed result and grounds. When a `C.22.1` adaptation signature is selected, retain its threshold target, `timeToThreshold`, `budgetToThreshold` and `priorExposureDeclaration`, including a not-reached or unresolved result when the history warrants it.
* **CC-B4.5 (Adaptive-specialization boundary):** Claimed transfer, retention, post-threshold efficiency, corridor entry and downside **MUST** retain the targets, baselines, windows and evidence required by the claim or receiving comparison. `C.22.1` defines the selected adaptation-signature meanings; `G.5` and `G.9` retain their selector and parity rules when consuming that result.
* **CC-B4.6 (Phase and transition separation):** Each claimed phase and transition **MUST** retain its distinct question, result and applicable conditions from B.4:4.3. Evidence can be used across phases, and cue preservation or routing can contribute within Observe without requiring another phase.
* **CC-B4.7 (No success inference):** Deployment or publication establishes neither acceptance nor successful renewed use. Record failure, reopening, fallback, or another iteration when that is what occurred.

### B.4:8 - **Common Anti-Patterns and How to Avoid Them**

| Anti-pattern | Observable symptom | Repair |
| :--- | :--- | :--- |
| **Change without a basis** | A feature or design appears with no observed basis or identity decision. | **CC-B4.1** and **CC-B4.2** connect the change to an observed basis and state whether the subject continues or has a successor. |
| **Unidentified internal adaptation** | "The system automatically improves itself" hides who or what performed the activity. | Identify who or what changes which subject. Use **CC-B4.3** for a Work claim. For an internal acting side, recover the distinct participants and their parthood under `A.12`, together with the Work, Method and phase facts the receiving claim consumes; physical externality is not required. |
| **Incomplete hotfix account** | A quick run-time repair is reported as a complete successful loop, although design repair, evidence, or renewed-use confirmation did not occur. | State only the urgent observation, change activity, deployment and immediate result that occurred. Later description repair, testing, assurance and follow-up operation are subsequent activities and may reopen the loop; qualify any particular Work occurrences under B.4:4.2. |

### B.4:9 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Connects learning to change:** The loop relates an observed basis, a change, and renewed use across repeated adaptations. | **Record overhead:** A full trace is too heavy for many local changes. *Mitigation:* keep the account proportional to the receiver and expand it only for reliance, assurance, audit, or replay. |
| **Exposes design-reality divergence:** Separate phase outputs make stale descriptions, failed deployment, and missing renewed use visible. | **No automatic success:** The loop cannot guarantee reconciliation. Deployment can fail, evidence can overturn a candidate, and renewed use can reveal another problem. |
| **Makes adaptation inspectable:** Named subjects, actual activities, identity conclusions and evidence let a reviewer reconstruct why a change was made. | **Needed subject contributions:** B.4 coordinates the identity, Work, evidence, publication or acceptance results on which the current use depends. |

### B.4:10 - **Rationale**

This pattern operationalizes the **Open-Ended Evolution Principle (P-10)** by connecting use, observation, explicit change, and renewed use. Subject patterns decide identity and continuity. The account distinguishes actual activities and their results and retains the evidence needed for relied-on claims. B.4 makes their coordination inspectable while permitting a sufficient local answer to stop before another phase.

### B.4:10.1 - **SoTA-Echoing**

The phase rhythm has historical lineage in iterative cycles such as Plan-Do-Check-Act and Observe-Orient-Decide-Act. B.4 adapts that lineage rather than treating those labels as an ontology: it distinguishes design-time accounts from run-time use, applies a kind-specific identity rule, identifies relevant activities and results, admits internal acting-side splits, and keeps evidence, deployment, publication, acceptance, and renewed use separate.

Canonical means the four questions recur across repeated adaptation; it does not mean every subject or project follows one identical history.

### B.4:11 - **Relations**

* **Operationalizes:** `P-10 Open-Ended Evolution`.
* **Uses:** `A.4` when Observe needs a comparison of a System's intended design with its actual operating conditions; `A.12` for external or reflexively split acting sides; `A.15.1` for dated Work; and the direct subject patterns named in B.4:4.1 for identity and continuity.
* **Coordinates with:** `B.5 Choose the Next Reasoning Contribution (Canonical Reasoning Cycle)`, `B.5.1` development states, and `B.3 Is This Claim Supported for This Use? — Trust and Assurance Calculus`. B.4 does not implement the B.5.1 states one-for-one, and evidence is not a B.4 phase.
* **Is detailed by:** `B.4.1 Publish Candidate Routes for a Stabilized Cue (RoutedCueSet)` for optional early cue routing. The subject patterns in B.4:4.1 supply each subject's identity and continuity rules.

#### B.4:11.1 - Pre-abductive seam compatibility

During Observe, use `A.16.1` when a cue needs publication while its interpretation remains open, and `B.4.1` when possible continuations or a justified route choice need publication. Keep multiple routes live while selection is unresolved. A selected route can enter Refine or another fitting pattern when the receiving work calls for that continuation and its entry conditions hold. The receiving operation can use the routed cue publication directly or an available later typed publication such as `U.AbductivePrompt`, as appropriate.

### B.4:End
