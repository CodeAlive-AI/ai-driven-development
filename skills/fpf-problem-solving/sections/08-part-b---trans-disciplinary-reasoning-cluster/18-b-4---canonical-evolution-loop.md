## B.4 - Canonical Evolution Loop
> **Status:** Stable
> **Type:** Pattern

**Use this when.** Use this pattern when repeated adaptation must keep one exact subject's current identity, an observed basis, a proposed or actual successor, the Systems and dated Work that make the change, and renewed use connected. Name the subject kind first: System, episteme, Method, MethodDescription, or a sequence of distinct Work occurrences.

**What goes wrong if missed.** Teams treat drift, learning, release, and improvement as unrelated events. Specifications become stale, operational surprises lose their evidence relation, and changes appear without a clear predecessor, successor, performing System, or dated Work. At the opposite extreme, one generic loop is imposed on every subject: a description edit is called a Method change, completed Work is said to be revised, or an internal adaptation is rejected because its acting System is not external.

**What this buys.** A compact, reviewable adaptation cycle whose identity rule comes from the subject pattern. It keeps observed basis, design-time change, run-time use, acting Systems, dated Work, evidence, publication, acceptance, and responsibility distinct while connecting only the facts needed by the receiving use.

**Not this pattern when.** Not this pattern when one direct subject-pattern claim answers the change question without a repeated adaptation cycle. Use `B.3.5` for relation grounding, `B.4.1` for early cue stabilization and routing, `B.5.2.0` for abductive hypothesis work, `C.27` for temporal status, or `A.15` for method/work alignment without an adaptation-loop claim.

### B.4:1 - **Problem Frame**

The FPF is built on the **Principle of Open-Ended Evolution (P-10)**: continued use can reveal reasons to adapt a System, an episteme, a Method, or a description. The useful commonality is a repeated move from use through an observed basis and an explicit change back to use. The identity question is not common. The same subject may continue through a change, a successor may be identified, or later dated Work may be a distinct occurrence rather than a revision of earlier Work. B.4 therefore supplies a shared cycle only after the relevant subject pattern has supplied that distinction.

### B.4:2 - **Problem**

Without a canonical, shared model for evolution, projects fall into predictable and costly failure modes:

1. **Design-Reality Divergence (The "Drift"):** The run-time subject in use slowly diverges from its design-time account. Formal models become elegant fictions, assurance cases become irrelevant, and the project loses the ability to reason reliably about what it uses.
2. **Learning Stagnation (The "Ivory Tower"):** Observation produces valuable findings, but no explicit change path carries them into a revised design or renewed use. "Lessons learned" remain static documents.
3. **Chaotic Change (The "Whack-a-Mole"):** Reactive patches have no stated observed basis, identity decision, or return-to-use condition. Hidden dependencies and unintended consequences accumulate.

### B.4:3 - **Forces**

| Force | Tension |
| :--- | :--- |
| **Stability vs. Change** | How to adapt continuously while retaining the identity and assurance commitments that still hold. |
| **Learning vs. Operating** | How to keep use stable enough to serve its purpose while gathering and acting on evidence. |
| **Top-Down Intent vs. Bottom-Up Reality** | How to connect intended improvement with what actual use reveals. |

### B.4:4 - **Solution**

Use the **Canonical Evolution Loop** as a coordinating cycle, not as a universal identity rule. First recover the exact subject and what continuity means for it. Then name the actual Systems and dated Work, traverse only the phases that occurred, and connect the result to renewed use.

#### B.4:4.1 - Name the subject and continuity question

| Subject kind | State before using the shared cycle |
| :--- | :--- |
| **System** | Name the current System and the relevant continuity or transformation rule. State whether the changed System remains the same System or whether a successor System is identified. Use `A.1` for System recognition, `A.3.4` for an actual bounded change of the continuing System, and `A.15.PROD` when the claim concerns first existence through production Work. |
| **Episteme** | Identify the earlier and later epistemes under `C.2.1`. Assert an `EpistemeEditionRelation` only when its historical-continuation conditions obtain; otherwise state replacement or another direct relation. |
| **Method** | Identify the current Method under `A.3.1`. If intended results, participant meanings, admissible conditions, safety bounds, semantic basis, acceptance criteria, or composition change, state whether the result is a refinement, substitute, or distinct successor Method. Use `B.1.5` when order-sensitive composition is current. |
| **MethodDescription** | Identify each exact claim-bearing episteme under `A.3.2` and `C.2.1`, and any obtaining edition relation. A later description does not by itself change the Method it describes. |
| **Work** | Identify each dated occurrence under `A.15.1`. Completed Work is not revised: later review, repair, deployment, or follow-up is other Work, even when the occurrences belong to one longer effort. |

Not every holon is an adaptation-loop subject, and the five branches are not interchangeable. If the continuity or successor relation is still open, keep that question explicit rather than hiding it behind the word *evolution*.

#### B.4:4.2 - Separate the changed subject from the acting side

The subject does not observe, refine, or deploy itself by grammatical convenience. A System performs each actual piece of Work. The changed subject, performing System, dated Work, Method enacted by that Work, and result remain distinct. Practitioner prose can still say "the engineer refined the design" or "the controller adjusted the valve" when that recognizable actor and action are enough. If that ordinary sentence is all the receiver needs, do not open a technical Work account. If B.4 identifies one particular dated `U.Work` occurrence, first recover every actual performer's A.13 core and independently admit the Work under A.15.1 from its performance history, enacted Method, temporal extent, and containing System. Add F.6 only when the receiving claim also needs precise assignment-bound attribution. A short B.4 account may omit an unused assignment identifier or classification only when every relation it consumes remains recoverable.

The performing System need not be external to the larger holon. For internal adaptation, apply the `A.12` reflexive split: identify the changed subsystem or part and the acting subsystem or part as exact, distinct participants, and establish their parthood in the containing holon independently. Use an external System when that is what the case actually has. For any particular dated `U.Work`, recover every performer's A.13 core and independently admit the occurrence under A.15.1; add F.6 afterward only when precise assignment-bound attribution is current. Name an assignment in the short B.4 account only when the receiving claim uses its identity. State authority, responsibility, permission, acceptance, or admission through its own direct predicate, actual participants, and applicability basis; neither a phase label nor Work supplies them.

#### B.4:4.3 - Keep the four phases non-overlapping

| Phase | Current question | Output and boundary |
| :--- | :--- | :--- |
| **1. Operate** | How is the current subject actually operating or being used? | Name the current use or operation and any records that actually exist. Monitoring may occur, but a record does not by itself establish an observation, comparison, or change. |
| **2. Observe** | What do records, measurements, testimony, or other evidence show for the named use? | Name the observation, comparison, or interpretation Work. Separately identify the observed basis, finding, hypothesis, or still-unclear cue through the direct result or evidence rule that actually applies; Work has no generic result field. Observe does not yet choose a change. |
| **3. Refine** | What change should be developed and tested in response, and what identity relation would that change have? | Name the design, revision, selection, and testing Work. Separately identify the selected candidate and the subject-specific identity question or intended treatment. State a continuity, successor, substitution, refinement, or edition relation only when its exact endpoints exist and its own conditions obtain. Refine does not make the candidate available for renewed use. |
| **4. Deploy** | What concrete deployment Work occurred for the selected candidate? | Name that Work. Then state separately what actually happened—for example, a changed or produced entity, publication, configuration, release, or availability—using the rule that establishes that fact. Acceptance, admission, and actual later use remain separate facts. |

Use explicit transition conditions:

1. **Operate -> Observe:** a named cue, question, monitoring result, or review need requires interpretation.
2. **Observe -> Refine:** the receiving use has an observed basis or a routed cue from which a change question can be formed.
3. **Refine -> Deploy:** one candidate is selected and its subject-specific identity question or intended treatment is explicit. State an obtaining continuity, successor, substitution, refinement, or edition relation here only when both endpoints already exist; otherwise keep the question open until the relevant change or production has occurred.
4. **Deploy -> Operate:** actual renewed operation or use begins; availability alone does not close this transition.

Evidence is not a fifth phase. Evidence relations warrant the observed basis, candidate choice, transition, or renewed-use claim when a receiver relies on them. Evidence can be produced or used during several phases without duplicating those phases.

#### B.4:4.4 - Connect neighbouring cycles without collapsing them

The Canonical Reasoning Cycle (`B.5`) can supply reasoning Work within Observe and Refine. The B.5.1 development states and B.4 phases coordinate, but they are not a one-to-one implementation: a finding may reopen Exploration or Shaping, evidence use can support Evidence, and renewed use can enter or return to Operation.

When Observe finds only a weakly articulated cue, use the optional `B.4.1` sequence **Notice -> Stabilize -> Route**. Its routed result can return to Refine or enter another subject pattern. That sequence does not replace the four B.4 phases.

Keep the account proportional. A local repair can name only the current subject, observed basis, actual Work, resulting identity relation, and next use. Expand to a complete cycle trace when a named relying decision, assurance case, audit, or later replay needs it. Never invent phases merely to make the record look complete.

> **Didactic Note: four practical questions**
>
> 1. **Operate:** What exact subject is operating or being used now?
> 2. **Observe:** What has actual use shown, and through whose Work?
> 3. **Refine:** What change is being considered, and would it continue or replace the subject?
> 4. **Deploy:** What deployment Work occurred, and what separately established fact now supports the next use?
>
> The gain is a readable connection from an observed basis to a real change and back to use, without losing subject identity, performers, Work, or evidence.

### B.4:5 - **Archetypal Grounding**

The phase names can be shared, but each subject branch keeps its own identity and return-to-use rule.

* **B.4.1 - Observe -> Notice -> Stabilize -> Route (optional pre-abductive route):**
  * **Context:** A fleet of autonomous delivery drones (`U.System`) is in operation, and operators begin to notice that winter deliveries feel "off" before a clean anomaly statement exists.
  * **Loop Example:**
    1. **Operate:** The drones perform deliveries.
    2. **Observe:** The monitoring service and named operators perform observation Work and find recurring cold-weather battery strain, but the cue still has low articulation.
    3. **Optional B.4.1 route inside Observe:** A named team performs stabilization Work. Under `A.16.1`, a `U.PreArticulationCuePack` preserves the cue nucleus, primary witness traces, and current language-state position without pretending that a final anomaly or action record exists; when the pack is made available for this use, name the separate publication occurrence under `E.24.PUB`. The same or another team performs routing Work. Under `B.4.1`, a `RoutedCueSet` keeps multiple continuations visible—for example, battery-chemistry investigation or route-planning adjustment; again, name its publication occurrence under `E.24.PUB` when availability matters.
    4. **Continue the loop:** The selected route enters Refine or another fitting subject pattern. Only a selected and tested change proceeds to Deploy and renewed drone operation.

* **Knowledge-instantiation slice (theory refinement loop):**
  * **Context:** A scientific theory of protein folding (`U.Episteme`) is used to predict structures.
  * **Loop Example:**
    1. **Operate:** Named researchers perform theory-application Work using the current theory episteme.
    2. **Observe:** A research lab performs observation Work. A separately identified `C.2.1` finding episteme states that the current theory fails to predict the structure of a protein class; name separately any `E.24.PUB` publication occurrence that makes this finding available.
    3. **Refine:** A research team performs revision and testing Work. A later theory episteme, identified under `C.2.1` from its changed claim content, includes a term for the new protein class. Assert an edition relation between the two theory epistemes only if that relation obtains.
    4. **Deploy:** The team performs publication Work for the later theory. The publication occurrence, journal acceptance, admission into a configured knowledge base, and later community use are separate relations. **Note.** If a *chart* or CG-frame readings are derived from this episteme, they MUST cite the `MethodDescription` of the measurement protocol actually used (per A.19.CN CC-A19.D1-3) to keep comparability auditable.

  **Adaptive-specialization note.** When the knowledge-instantiation slice carries a bounded-specialization claim for one declared task family, that claim **SHALL** name the prior basis being refined from, the named work-measure threshold being pursued, the adaptation budget being spent, and the freshness or provenance basis for claiming the specialization is reusable. If the refinement is claimed as one specialization step, it **SHALL** also cite the declared `TaskFamily` or `TaskSignature` anchor consumed by `C.22.1`, `G.5`, and `G.9`. This keeps the refinement legible as contextual task-family specialization rather than vague general capability growth.

* **Method-instantiation slice (adaptive method loop):**
  * **Context:** A field-maintenance organization uses a declared inspection-and-repair Method (`U.Method`) described by one current `U.MethodDescription`.
  * **Loop Example:**
    1. **Operate:** Maintenance teams perform dated maintenance Work that enacts the current Method.
    2. **Observe:** A reviewer performs review Work and records that the time from fault detection to safe restoration repeatedly exceeds the allowed window.
    3. **Refine:** Method maintainers perform revision and testing Work. A wording clarification can yield a later MethodDescription while the same Method remains current. Adding an earlier isolation action or changing a classification checkpoint can instead change identity-bearing Method semantics; decide under `A.3.1` whether the result is a refinement, substitute, or distinct successor Method, and use `B.1.5` if its composition changes. Then identify the MethodDescription episteme that describes the chosen Method.
    4. **Deploy:** A named publishing team performs publication or release Work for the later MethodDescription and, where needed, configuration or training Work for renewed Method use. Decision results, authority, acceptance, admission, and later Work that enacts the Method remain separate. Completed maintenance Work is never revised.

  **Adaptive-specialization note.** When the method-instantiation slice carries a bounded-specialization claim for one declared task family, that claim **SHALL** name the narrower higher-fit specialist method or specialist portfolio being activated, the refinement budget being spent, the escalation or commit checkpoints, and the fallback when that method fails. If the method update is being used as evidence of specialization, the note **SHALL** keep the bearer of that specialization explicit: the holder, dyad, team, or scoped portfolio carries the claim; the method is only one selected vehicle. This keeps method evolution reviewable as bounded specialist acquisition rather than as hidden budget inflation.

### B.4:6 - **Bias-Annotation**

| Bias | Symptom | Correction |
| :--- | :--- | :--- |
| Self-evolution bias | The subject is said to observe, refine, or deploy itself, so the performing System and its Work disappear. | Name the changed subject and distinct acting side. Ordinary actor wording can remain short. When one particular dated `U.Work` is identified, recover each performer's A.13 core and independently admit the occurrence under A.15.1; add F.6 only when precise assignment-bound attribution is current. A short account may omit an unused assignment identifier only when every relation it consumes remains recoverable. The acting side may be external, or it may be an exact distinct subsystem or part established through the `A.12` reflexive split. |
| Design-time/run-time smear | A live operational change is treated as if it had already updated the design-time episteme, or a design-time edit as if it had already changed the System in operation. | Keep the design-time episteme, run-time System or use, deployment Work, evidence relation, and renewed use distinct. |
| Method/description smear | A MethodDescription edit is called a Method change, or a changed Method is hidden as a documentation update. | Test Method identity under `A.3.1` and composition under `B.1.5`; identify MethodDescription editions separately under `A.3.2` and `C.2.1`. |

### B.4:7 - **Conformance Checklist**

* **CC-B4.1 (Proportional loop integrity):** Record the actual path from observed basis through change to renewed use. A complete phase-by-phase trace is required only when a named relying decision, assurance case, audit, or replay needs it. Do not invent a phase or claim completion merely to fill a loop.
* **CC-B4.2 (Subject identity):** Name the exact subject kind and apply its direct continuity rule: System continuity or transformation; episteme predecessor, successor, or edition; Method identity, refinement, substitution, or successor; MethodDescription edition; or separate dated Work occurrences.
* **CC-B4.3 (Acting-side distinction):** Work that observes or changes a subject **MUST** have an identified performing System distinct from the changed subject in that Work account. Internal adaptation is permitted when `A.12` establishes exact distinct subsystems or parts and their independently obtaining parthood. Every particular dated `U.Work` reuses each performer's A.13 core and is independently admitted under A.15.1; F.6 is added afterward only for precise assignment-bound attribution. Its short B.4 account may omit an assignment identifier unused by the receiver only when every consumed relation remains recoverable.
* **CC-B4.4 (Adaptive-specialization anchoring):** When the knowledge-instantiation or method-instantiation slice carries a bounded-specialization claim, that claim **MUST** name the declared `TaskFamily` or `TaskSignature`, the work-measure threshold target, the adaptation budget, and the freshness or provenance basis for reuse.
* **CC-B4.5 (Adaptive-specialization boundary):** The knowledge-instantiation and method-instantiation slices **SHALL NOT** silently re-govern selector or parity semantics. If transfer, retention, downstream exploitation efficiency, corridor entry, or downside cost are comparison-relevant, the pattern-local note **MUST** leave those fields recoverable by the downstream `C.22.1`, `G.5`, and `G.9` patterns.
* **CC-B4.6 (Phase and transition separation):** Operate, Observe, Refine, and Deploy **MUST** have the distinct outputs and transition conditions stated in B.4:4.3. Evidence use and optional B.4.1 cue routing do not become duplicate phases.
* **CC-B4.7 (No success inference):** Deployment or publication establishes neither acceptance nor successful renewed use. Record failure, reopening, fallback, or another iteration when that is what occurred.

### B.4:8 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Observable symptom | How FPF prevents it conceptually |
| :--- | :--- | :--- |
| **The "Immaculate Conception"** | A feature or design appears with no observed basis or identity decision. | **CC-B4.1** and **CC-B4.2** connect the change to an observed basis and state whether the subject continues or has a successor. |
| **The "Self-Healing Illusion"** | "The system automatically improves itself" hides who or what performed the Work. | **CC-B4.3** requires a distinct acting-side System. An internal control or adaptation loop is valid when exact internal participants, their parthood, the Work, Methods, and phase transitions are identified; physical externality is not required. |
| **The "Perfect Hotfix"** | A quick run-time repair is reported as a complete successful loop, although design repair, evidence, or renewed-use confirmation did not occur. | Record only the urgent observation, change Work, deployment, and immediate result that actually occurred. Later description repair, testing, assurance, and follow-up operation are separate Work and may reopen the loop. A hotfix can compress time, not truth. |

### B.4:9 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Creates a learning architecture:** The loop gives repeated adaptation a readable structure and connects learning to actual change. | **Record overhead:** A full trace is too heavy for many local changes. *Mitigation:* keep the account proportional to the receiver and expand it only for reliance, assurance, audit, or replay. |
| **Exposes design-reality divergence:** Separate phase outputs make stale descriptions, failed deployment, and missing renewed use visible. | **No automatic success:** The loop cannot guarantee reconciliation. Deployment can fail, evidence can overturn a candidate, and renewed use can reveal another problem. |
| **Makes evolution auditable:** Named subjects, Systems, Work, identity relations, and evidence let a reviewer reconstruct why a change was made. | **Several patterns remain necessary:** B.4 coordinates their results; it does not replace the subject's identity, Work, evidence, publication, or acceptance patterns. |

### B.4:10 - **Rationale**

This pattern operationalizes the **Open-Ended Evolution Principle (P-10)** by connecting use, observation, explicit change, and renewed use. It does not supply one generic ontology of evolution. Subject patterns decide identity and continuity; Systems perform dated Work; evidence supports relied-on claims; and B.4 makes their repeated coordination inspectable.

### B.4:10.1 - **SoTA-Echoing**

The phase rhythm has historical lineage in iterative cycles such as Plan-Do-Check-Act and Observe-Orient-Decide-Act. B.4 adapts that lineage rather than treating those labels as an ontology: it distinguishes design-time accounts from run-time use, applies a kind-specific identity rule, identifies actual Systems and dated Work, admits internal acting-side splits, and keeps evidence, deployment, publication, acceptance, and renewed use separate.

The result is a practical review language for repeated adaptation. It avoids both agentless "self-evolution" stories and the opposite mistake of requiring every acting System to be external. Canonical means the four questions recur; it does not mean every subject or project follows one identical history.

### B.4:11 - **Relations**

* **Operationalizes:** `P-10 Open-Ended Evolution`.
* **Uses:** `A.4 Temporal Duality` for design-time/run-time distinctions; `A.12` for external or reflexively split acting sides; `A.15.1` for dated Work; and the direct subject patterns named in B.4:4.1 for identity and continuity.
* **Coordinates with:** `B.5 Canonical Reasoning Cycle`, `B.5.1` development states, and `B.3 Trust & Assurance Calculus`. B.4 does not implement the B.5.1 states one-for-one, and evidence is not a B.4 phase.
* **Is detailed by:** `B.4.1 Observe -> Notice -> Stabilize -> Route` for optional early cue routing, together with B.4.x instantiation patterns for specific subject families.

#### B.4:11.1 - Pre-abductive seam compatibility

For early language-state routing, Observe does not have to jump directly into anomaly or hypothesis forms. Observe may publish a `U.PreArticulationCuePack` and a `RoutedCueSet` through `B.4.1`; a selected route then enters Refine or another fitting pattern. A downstream loop consumes the routed cue publication directly or a later typed publication such as `U.AbductivePrompt`, as appropriate.

### B.4:End

