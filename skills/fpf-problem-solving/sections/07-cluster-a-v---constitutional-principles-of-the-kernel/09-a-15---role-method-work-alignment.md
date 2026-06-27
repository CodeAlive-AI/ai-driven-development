## A.15 - Role–Method–Work Alignment (Contextual Enactment)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** This pattern is the enactment-alignment pattern for engineer-managers when the real confusion is not "what component is this" but `who is responsible`, `how the work is supposed to happen`, `when the plan applies`, and `what actually happened`.

**Use this when.** Use this pattern when the real job is to separate role, method, plan, capability, and actual work before a team treats one cue, one schedule, one display, one copied or generated statement, or one document as if it already counted as the role assignment, the method, the work plan, execution evidence, or the work itself.

**Start here when.** The dominant ambiguity is role vs method vs schedule vs actual run, and the team keeps arguing over a source-side "process" cue without separating recipe, plan, capability, and executed work.

**First output.** One explicit separation of `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work`, plus the shortest traceable chain that already exists from `U.RoleAssignment` through the governing `U.Method` and its method-description source to the intended `U.WorkPlan` or actual `U.Work` occurrence, or an explicit source gap that blocks admission of the claim.

**Working enactment-alignment spine.** Role, method, plan, and work confusion -> separate role, holder, bounded context, method description, intended `U.WorkPlan`, and actual `U.Work` -> choose proceed, plan, bounded probe, narrow, apply the direct governing pattern for any non-A.15 claim, or stop -> output the smallest alignment frame needed for the next work-family use -> use `A.15.4` only when an encountered episteme publication, display, credential view, explanation, copied statement, provenance mark, dashboard tile, schema wording, API wording, or composed source chain begins to carry or justify a work claim or reliance claim.

**Working alignment applications.**
1. Name the role, holder, and context distinction under repair.
2. Name the method or method description that is meant to govern the work.
3. Name the intended `U.WorkPlan` or actual `U.Work` occurrence being claimed.
4. Choose the next governed use: proceed inside the recovered relation, plan, run a bounded reversible probe, narrow scope, apply the governing FPF pattern and project-side FPF kind and reference named by value for the claim or effect being made, or stop.
5. If an encountered source candidate or display is being used by appearance for a work claim, reliance claim, or source-restoration claim, apply `A.15.4 Work-Relevant Source Restoration` to that source-restoration claim; keep `A.15` only for the `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation.

**Action-pattern protection.** This pattern is not about classifying encountered publications, displays, or cues. It keeps role, method, plan, capability, and actual work distinct so the acting engineer-manager can choose the next admissible work-family or reliance use. Work-relevant source restoration is handled by the related `A.15.4` cluster member.

**Minimum sufficient governed use.** Choose the minimum sufficient governed use, recover only the project-side FPF kind and reference named by value needed for that use, and do not raise the claim beyond that recovered relation, source, or admissible-use boundary.

**Recovered-source sufficiency condition.** If the required project-side FPF kind and reference named by value is present and its scope and window match the role, method, plan, or work-family claim under repair, proceed inside that recovered scope and window. If not, narrow scope, run a bounded reversible probe, source-find, or create only the smallest source-restoration request, decision-request record, prospective work-plan entry, source-gap note, or missing-source admission block needed for the next governed use.

**Ordinary use.** If the team only needs to separate role, method, plan, capability, and actual work for orientation or planning, one separation sentence or small working card is enough.

**Reliance-bearing use.** Use the fuller alignment frame when an encountered source candidate or display is about to guide planned work, actual work, role attribution, role-state attribution, release reliance, disputed responsibility, or cross-context use. Use `A.15.4` when the issue under repair is whether that source candidate exposes the project-side FPF kind and reference named by value needed for that work claim or reliance claim.

**Stop condition.** Stop once the separation changes no next admissible work-family use or reliance use and blocks no concrete overclaim about role, role-state, method, plan, work, approval, evidence, or release.

**Admissible-use examples.**

| Admissible project use | Source-finding or reversible probe | Non-admissible use |
| --- | --- | --- |
| A maintenance team names `PumpInspectorRole`, the inspection method description, the current `U.WorkPlan`, and the dated `U.Work` record that will be created after the inspection. The team may plan and perform the inspection under those distinct records. | A short briefing says the inspection is ready, but the method description or work plan is missing; use the briefing only to find or repair the missing source before planned work proceeds. | A dashboard tile, copied approval, generated explanation, or briefing is used as the source for a work or reliance claim by appearance. Use `A.15.4` for that source-restoration question. |

**Alignment frame in plain terms.** One alignment frame linking `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` through `U.RoleAssignment`; not a single work occurrence, not a checklist, not a language-style repair pattern, and not a mere cue note.

**First admissible work-family use in plain terms.** Keep design-time role, method, and work plan distinct from run-time work while making the chain between them inspectable enough for enactment, audit, and source restoration.

**What goes wrong if missed.** Teams collapse role, recipe, plan, capability, and actual run into one fuzzy source-side "process" label, then mistake documentation for execution, capability for evidence, schedule for occurrence, or a narrower briefing for the source that makes work admissible.

**What this buys.** One inspectable enactment frame that lets a team ask who held what role, which method governed, what plan existed, and what work actually occurred before treating follow-on work, blame, or approval as if those distinctions were the same.

**Not this pattern when.** Not this pattern when the honest need is only one dated work occurrence (`A.15.1`), only planning or schedule baseline (`A.15.2`), only work-entry readiness or full-kit preparation (`A.15.5`), only a cue note that has not yet become an enactment-alignment question (`A.16` or `A.16.1`), only boundary wording or policy wording without a role-method-work question under repair (`A.6` or `A.6.B`), or work-relevant source restoration for an encountered source candidate or display (`A.15.4`).

**Related project records and governing patterns.** `A.15.1` governs dated execution records, `A.15.2` schedule or baseline planning records, `A.15.3` slot-filling plan items, `A.15.4` work-relevant source restoration, `A.15.5` work-entry readiness and full-kit preparation, `B.5.1` Explore -> Shape -> Evidence -> Operate for project progression, `F.11` method and work vocabulary alignment across contexts, and `F.17` the human-facing work sheet.

**Causal-use work boundary.** Realized counterfactual-sampling work, counterfactual randomization, intervention assignment, target-trial emulation work, and causal evidence collection remain `U.MethodDescription`, `U.WorkPlan`, and `U.Work` structures here. `A.15` can say who performs which sampling or intervention work under which method and role; it does not make the resulting causal use admissible. `C.28` governs the causal-use question, `CausalityLadderRung`, causal estimand, `CausalEvidenceSupportBasis`, counterfactual sampling realizability, and supported use and unsupported use.

**Related-record mistakes.** If the first honest encountered source cue is still only a cue, keep it under `A.16` or `A.16.1`; if the question under repair is boundary wording, promise, agreement-like service, or policy wording, recover the corresponding `A.6` boundary-claim record; if you only need one executed occurrence rather than the alignment frame, recover the `A.15.1` dated work-occurrence record; if an encountered source candidate or display is being used for a work relation or reliance relation, use `A.15.4`.

**Boundary to coarsened renderings.** A lighter briefing, summary, redacted note, or coarsened rendering may orient work or cue attention. It becomes sufficient for work execution, plan use, approval, gate decision, or execution evidence only when the required method, plan, approval, gate, or evidence source remains explicit and reopenable. Treat the coarsened-rendering relation through `A.6.3.CSC Controlled Semantic Coarsening` when the rendering itself changes what can be relied on.

**Use boundary.** Use `A.15` when the current project question needs role-method-work alignment. If the current claim is one single work occurrence, source-restoration note, wording repair, assurance claim, or source-side "process" label, use the governing pattern for that claim and keep only the A.15 separation that remains needed.

### A.15:1 - Problem frame

In any complex system, from a software project to a biological cell, there is a fundamental distinction between **what something is** (its structure), **what it is supposed to do** (its role and specified capability), and **what it actually does** (its work). Confusing these distinctions is a primary source of design flaws, budget overruns, and failed projects. Teams argue over a source-side "process" cue without clarifying whether the FPF object under repair is a `U.Method`, a `U.MethodDescription`, a `U.Capability`, a `U.WorkPlan`, or a specific `U.Work` occurrence that happened last Tuesday.

This pattern provides the canonical alignment for modeling contextual enactment in FPF. It applies the **Strict Distinction Principle (A.7)** to the passage from intended work to planned and actual `U.Work`, without making A.15 the whole strict-distinction ontology. It weaves together current governing relations into a single, coherent model:
*   **A.2 and A.2.1:** Provide `U.Role` values and `U.RoleAssignment` as the typed work-facing assignment relation with holder, role, bounded-context, window, and justification slots governed through A.6.5-style slot discipline.
*   **A.15.2 and A.15.1:** Separate `U.WorkPlan` intent windows from dated `U.Work` occurrences.
*   **A.3.1 and A.3.2:** Separate `U.Method` from `U.MethodDescription`, so recipes, algorithms, procedures, and source-side "process" cues do not become performed work by word choice.
*   **A.3.4:** Provides `U.Transformation` for bounded change under conditions when the actual change, affected entity, pre/post state, mechanism, method, or work relation is current.
*   **A.10, C.2.1, and E.17:** Keep evidence, source, publication, and carrier relations outside the work-facing role assignment unless a system or acting holon is actually assigned a role for performed work.

The intent of this pattern is to establish a normative, unambiguous vocabulary and set of relations for describing the passage from role and method capability to planned and actual, resource-consuming `U.Work`.

To keep plan-run separation explicit, this pattern references **A.15.2 `U.WorkPlan`** for **schedules and calendars** and **A.15.1 `U.Work`** for **dated execution**. Ambiguous source terms like "process", "workflow", "activity", and "schedule" are handled by `E.10` and `E.10.ARCH`: recover the project concern first, then assign the source cue to `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work`, or another direct governing pattern.

**Terminology note.** The words _action_ and _activity_ are not normative kernel names by themselves. When a generic "doing" cue appears, recover the FPF kind being claimed: **`U.Method`**, **`U.MethodDescription`**, **`U.Work`**, **`U.WorkPlan`**, or a neighboring governed value such as `U.Transformation`, `U.Dynamics`, evidence, gate, source, or publication use.

### A.15:2 - Problem

Without this formal framework, models suffer from a cascade of category errors:

1.  **Role-as-Part:** A Role (e.g., `AuditorRole`) is incorrectly placed inside a structural parts list (`ComponentOf`), making the system's architecture brittle and nonsensical.
2.  **Specification-as-Execution:** A `MethodDescription` (the "recipe") is treated as evidence that the work was done. This leads to "paper compliance," where a system is considered complete simply because its documentation exists.
3.  **Capability-as-Work:** A team's *ability* to perform a task (`Capability`) is conflated with the *actual performance* of that task (`Work`). This obscures the reality of resource consumption and actual outcomes.
4.  **Work-without-Context:** An instance of work is logged without a clear link back to the role, capability, and specification that governed it, making the work unauditable and its results impossible to reproduce.
5.  **Ambiguous source-side "process" or "activity" cue:** The overloaded term "process" is used indiscriminately to refer to all of the above, creating a fog of miscommunication. Repair generic doing or activity terms through `E.10` and `E.10.ARCH` to `U.Method`, `U.MethodDescription` (recipe), `U.WorkPlan` (schedule), `U.Work` (run), or another direct governing pattern.

### A.15:3 - Forces

| Force | Tension |
| :--- | :--- |
| **Structure vs. Contextual Enactment** | The need to model stable structural decomposition (`mereology`) vs. the need to model holder-in-role assignment, capability expectation, method, plan, and dated work occurrence. |
| **Design vs. Run** | The need for a timeless, reusable description of a capability (`design-time`) vs. the need for a specific, dated record of its execution (`run-time`). |
| **Clarity vs. Jargon** | The need for a precise, formal vocabulary to prevent ambiguity vs. the reality that teams use informal, domain-specific source cues like "process" or "workflow." |
| **Accountability vs. Complexity** | The need for a complete, end-to-end audit trail for every decision-relevant work occurrence vs. the desire to keep models simple and avoid excessive documentation. |

### A.15:4 - Solution

**Method and work governing-pattern cue.**
 When a source-side "process", "algorithm", "solver", "workflow", "procedure", or similar label points to changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern`, use `E.10.ARCH:3.1` to recover the project concern first and then assign separately governed typed values. A.15 carries only the alignment among role, method, method-description, work-plan, and performed-work references. Formal substrate, mathematical-lens use, mechanism declaration or realization, evidence, gate, source, result, publication, and temporal claims are governed by their own patterns.

When methods are related to one another, A.15 keeps only the alignment use of that relation. The method-side object is `MethodRelationStructure@BoundedContext` under `A.3.1`, `A.3.2`, `G.5`, or a direct method-composition pattern when current. A method algebra, workflow graph, process calculus, matrix, category, embedding, or neural representation is a lens or method description over that structure, not a role relation, work plan, dated work occurrence, or assignment relation.
The solution is a stratified alignment that cleanly separates the `design-time` and `run-time` for contextual **enactment**. The bridge between these worlds is the **`U.RoleAssignment`**.

#### A.15:4.1 - The Core Entities: A Strict Distinction

FPF mandates the use of the following distinct, non-overlapping entities to model method, plan, and work enactment. Using them interchangeably is a conformance violation.

**A) Design-Time Entities (The World of Potential):**

*   **`U.Role`:** A contextual "mask" or "job title" (e.g., `TesterRole`). It specifies expected contribution or responsibility in a bounded context; it is not the holder, method, capability, work plan, or work occurrence.
*   **`U.Method`:** The **abstract way-of-doing** inside a context (paradigm-agnostic; may be imperative, functional, logical, or hybrid).
*   **`U.MethodDescription`:** A **`U.Episteme` describing a `U.Method`**; it may be expressed in an SOP, algorithm, proof, recipe, or other method-description publication.
*   **`U.Capability`:** An **attribute** of a `U.System` that represents its **ability** to enact the declared `U.Method` under stated conditions. A `MethodDescription` may describe that method; the capability is not the description and not the work occurrence.
*   **`U.WorkPlan`:** An **`U.Episteme`** declaring **intended `U.Work` occurrences** (windows, dependencies, intended performers as role kinds, budgets) - see **A.15.2**.

**B) The Bridge Entity:**
*   **`U.RoleAssignment`:** The typed work-facing assignment relation that links a holder system or acting holon, a `U.Role`, a `U.BoundedContext`, any current window, and justification or source references when they matter.

**C) Run-Time Entity (The World of Actuality):**

*   **`U.Work`:** An **occurrence** or **event**. It is the concrete, dated, resource-consuming enactment or execution of a `U.Method` by a `Holder` acting under a `U.RoleAssignment`; capability checks are evaluated at run time against the holder, and `methodDescriptionRef` names the source episteme used to identify or constrain the method when that source is being used for the work claim. This is the only entity that has a start and end time and consumes resources.

**Kinds of Work and the primary target**

**Well-formedness constraint A15-WF-1 (work target and kind).** A `U.Work` occurrence has `primaryTarget: U.Holon` with cardinality `1..1 (total)` and `kind` with cardinality `1..1 (total)`.

Local `kind` values used here:
* Operational - transforms a `U.System` or its environment.
* Communicative (SpeechAct) - transforms a deontic or organizational frame (e.g., commitments, authority effects, approvals).
* Epistemic - transforms a `U.Episteme` (e.g., curating a dataset).
The `primaryTarget` disambiguates enactment: what is being acted upon. Example: an approval is `kind=Communicative`, `primaryTarget = Commitment(change=4711)`. A deployment is `kind=Operational`, `primaryTarget = ServiceInstance(prod-us-eu-1)`.

**Didactic Note for Managers: The "Chef" Analogy**

This model can be easily understood using the analogy of a chef in a restaurant.

*   **`ChefRole`** is the **Role**. It's a job title with certain expectations.
*   A **Cookbook (`U.MethodDescription`)** contains the **recipe** for a Souffle. It's a piece of knowledge.
*   The chef's **skill** in making souffles is their **`U.Capability`**. They have this skill even when they are not cooking.
*   The restaurant's rulebook (`U.BoundedContext`) states that a holder assigned to `ChefRole` needs the capability to follow the recipes in the cookbook before the relevant cooking work is admitted.
*   The actual act of **making a souffle** on Tuesday evening - using eggs and butter, taking 25 minutes, and consuming gas - is the **`U.Work`**.

Confusing these is like mistaking the cookbook for the souffle. FPF's framework simply makes these common-sense distinctions formal and mandatory.

#### A.15:4.2 - The Canonical Relations: Connecting the Layers

The entities are connected by precise, normative relations that form a traceable alignment chain. The following diagram illustrates the relation chain from bounded context and method description to dated work occurrence.

```mermaid
graph TD
    subgraph Design-Time Scope (Tᴰ)
        A[U.BoundedContext] -- defines --> B(U.Role)
        M[U.Method] -- isDescribedBy --> D[U.MethodDescription]
        Cap[U.Capability] -- is capability for --> M
        H(U.System as Holder) --> RB(U.RoleAssignment)
        B -- is the role in --> RB
        A -- is the context for --> RB
        A -- bindsCapability(Role,Capability) --> Cap
    end

    subgraph Run-Time Scope (Tᴿ)
        W[U.Work]
    end

    W -- performedBy --> RB
    W  -- enactsMethod --> M

    style A fill:#e6f3ff,stroke:#36c,stroke-width:2px
    style B fill:#fff2cc,stroke:#d6b656,stroke-width:2px
    style Cap fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    style M fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    style D fill:#f8cecc,stroke:#b85450,stroke-width:2px
    style H fill:#e1d5e7,stroke:#9673a6,stroke-width:2px
    style RB fill:#dae8fc,stroke:#6c8ebf,stroke-width:3px,stroke-dasharray: 5 5
    style W fill:#ffe6cc,stroke:#d79b00,stroke-width:2px,font-weight:bold
```

*   **`bindsCapability(Role, Capability)`:** A `U.BoundedContext` asserts that a given `Role` requires a specific `Capability`. This is a `design-time` rule.
*   **`isDescribedBy(Method, MethodDescription)`:** A `U.Method` is formally described by one or more `MethodDescription`s. This links the abstract way-of-doing to the method-description episteme and to the publication used when that source is being used for the method claim.
*   **`enactsMethod(Work, Method)`:** A specific `U.Work` is a run-time enactment of a `U.Method` under a `U.RoleAssignment`. Capability checks are evaluated against the holder at run time; the `MethodDescription` remains the source episteme or method-description reference used to identify, constrain, or justify the method when that source is being used for the work claim.
*   **`performedBy(Work, RoleAssignment)`:** A `U.Work` is performed by the holder named through a specific `U.RoleAssignment`. This links the work occurrence to the holder-in-role-in-context.

_At run time, capability thresholds declared by the context or specification are **checked** against the holder; `U.Work` outcomes provide **evidence** for capability conformance._

This chain provides complete traceability: a specific instance of `U.Work` can be traced back to the `U.Method` it enacts, the `MethodDescription` or source publication used to identify or constrain that method, and the `U.RoleAssignment` relation whose holder, role, bounded-context, and current-window slots make the work-facing assignment explicit.

#### A.15:4.3 - Bounded specialization scouting and `CheckpointReturn`

When one human-plus-AI pair faces a new task family or candidate solution family, the governed work system may temporarily compose four distinct local roles inside the same dyad: a human-held `OutcomeCriterionHolderRole`, an `AIScoutRole`, an `AISpecialistProbeRole`, and a human-held `CommitAuthorityRole`. The payoff of the dyad is faster admissible specialization of the next work-family use, not disappearance of the human decision step.

For this bounded dyadic work question, the pair declares one outcome criterion first, enumerates heterogeneous candidate approaches that may satisfy that target, spends a bounded scouting budget or probing budget before any committed approach is chosen, and returns one `CheckpointReturn` that compares the tested approaches rather than silently treating one successful probe as a committed rollout. `A.15` governs this dyadic alignment use and local role split only; it does not restate the checkpoint-record semantics of `C.24` or the budget and guard enforcement of `E.16`.

Every `CheckpointReturn` carries:
- the declared outcome criterion and current `TaskFamily`
- the candidate approaches actually tested
- the evidence observed on each tested approach, including progress toward the named work-measure threshold and important failure signals
- the budget already burned and the residual budget still available
- the recommended next work-family use or reliance use: continue probing, commit to planned work, narrow the method or claim, apply the direct governing pattern for a non-A.15 claim, or stop
- the commit trigger named by value that would justify leaving the bounded probe

The return is candidate-approach evidence, burned and residual budget amounts, observed result, and commit-trigger condition. It is not the selected method, `U.WorkPlan`, performed `U.Work`, execution evidence/provenance relation, or rollout decision. Those claims need the project-side FPF kind and reference named by value before committed rollout.

Low-human-overlap approaches remain admissible here only while they stay tied to the declared outcome criterion, budget limits, and evidence/provenance relation by value.

#### A.15:4.4 - Boundary to A.15.4 Work-Relevant Source Restoration

Use `A.15.4` when an encountered episteme, episteme publication, display, credential view, generated explanation, copied statement, provenance mark, dashboard tile, schema wording, API wording, or composed source chain is being used by appearance for a work claim, reliance claim, role-assignment currentness claim, role-state currentness claim, source-currentness claim, approval, authorization, gate passage, evidence, engineering justification, release reliance, or performed `U.Work`.

`A.15` itself keeps the kernel separation: `U.Role`, holder, context, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, actual `U.Work`, and the `U.RoleAssignment` chain between them. The source-restoration question recovers the project-side FPF kind and reference named by value before the encountered source candidate or display can carry the work claim, reliance claim, or effect claim being made; that question belongs to `A.15.4` or to the source-restoration pattern governing that reliance named there.

A principle scheme, functional diagram, scenario, screen, or explanation that makes an `E.18.1` P2W carry-through structure recoverable may help the team plan work or find the needed source.

#### A.15:4.5 - Boundary to A.15.5 Work-Entry Readiness

Use `A.15.5` when the current question is whether intended work is ready enough to enter a work boundary. `A.15` keeps the role-method-work separation; `A.15.5` carries `WorkEntryReadiness@Context`, `FullKitCondition`, commitment disposition, resource-readiness refs, WIP or flow-policy refs, planned-baseline refs, and launch-gate refs when they are current.

Readiness is not performed work, not evidence sufficiency, and not gate passage by itself. A readiness-looking briefing, dashboard, source bundle, or P2W record may cue `A.15.5`, but the readiness relation is admitted only when the target work plan or plan item, missing inputs, preparation work if performed, planned baseline, and stop or degraded-use condition can be named.

### A.15:5 - Archetypal Grounding

The role-method-work alignment applies whenever the question under repair is holder-in-role, method description, intended plan, or performed work. Physical engineering, knowledge work, and socio-technical cases can all use the same distinction without turning A.15 into a universal process ontology.

| Archetype | **`U.System` Archetype (Manufacturing)** | **`U.Episteme` Archetype (Scientific Peer Review)** |
| :--- | :--- | :--- |
| **`BoundedContext`** | `FactoryFloor:ProductionLine_B` | `Journal:PhysicsLetters_A` |
| **`Role`** | `WeldingRobotRole` | `PeerReviewRole` |
| **`Holder`** | `ABB_Robot_Model_IRB_6700` (`U.System`) | `Dr_Alice_Smith` (modeled as a `U.System`) |
| **`U.RoleAssignment`** | assignment with holder slot `ABB_Robot_Model_IRB_6700`, role slot `WeldingRobotRole`, context slot `Line_B`, and current-window slots and source-reference slots when they matter | assignment with holder slot `Dr_Alice_Smith`, role slot `PeerReviewRole`, context slot `PhysicsLetters_A`, and current-window slots and source-reference slots when they matter |
| **`MethodDescription` (`U.Episteme`)** | `Welding_Procedure_WP-28A.pdf` (SOP) | `Peer_Review_Guidelines_v3.docx` |
| **`Capability` (Attribute of Holder)** | `executeWeldingSeam(Type: 3F)` | `evaluateManuscript(Field: QuantumOptics)` |
| **`Work` (`Occurrence`)** | Manufacturing Work: `Weld_Job_#78345` (15:32-15:34 UTC, consumed 1.2 kWh, 5g Argon) - **enactsMethod** `WeldingMethod`, with `methodDescriptionRef = Welding_Procedure_WP-28A.pdf` | Peer-review Work: `Review_of_Manuscript_#PL-2025-018` (Completed 2025-08-15, took 4 hours) - **enactsMethod** `PeerReviewMethod`, with `methodDescriptionRef = Peer_Review_Guidelines_v3.docx` |

**Key takeaway from grounding:**
This side-by-side comparison reveals the power of the framework. A seemingly different activity like welding a car chassis and reviewing a scientific paper are shown to have the same underlying enactment structure. Both involve a `Holder` (a system) acting in a `Role` within a `Context`, using a `Capability` to enact a `U.Method`, citing a `MethodDescription` when a recipe or source is used to identify or constrain the method, and producing a specific, auditable instance of `Work`. This universality is what allows FPF to compare and align disparate domains without collapsing their local structure.

#### A.15:5.1.a - Briefing guides orientation, not execution

**Source set.** A release team has one deployment method description, one current work plan, one approval or decision record when required, and the evidence records and evidence relations used to decide whether the rollout may proceed. A short rollout briefing is prepared for the daily stand-up.

**Briefing slice.** `Status briefing only: rollback procedure appears verified in the current source bundle. Execution remains tied to the deployment method, work plan, required approval or decision record, and evidence relation.`

This briefing may orient the team and cue attention. If the team wants to execute from the briefing alone, use `A.15.4` or the evidence, gate, decision, or assurance pattern governing the claim to recover the missing project-side kind and reference. Inside `A.15`, keep only the role, method, plan, and work-occurrence separation.

#### A.15:5.1.b - P2W principle-scheme publication guides planning, not occurrence

**Source set.** A team has a principle scheme that shows an `E.18.1` P2W carry-through structure for a fabrication task: signature or principle episteme, method-family selection, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, and result measurement.

**Published slice.** `For this batch family, method M-2 is selected from the declared method family; prepare work plan WP-17 before any run is recorded.`

This publication may guide method inspection and work-planning preparation under `A.15`. A conforming use keeps selected method, `U.WorkPlan`, actual `U.Work`, work-result record, and result measurement distinct. If the publication is used for evidence, provenance, engineering justification, gate or constraint decision, material carrier, screen, export, OCR behavior, or publication-use, apply the governing pattern for that claim being made. If no project-side kind and reference named by value exists, create only a source-restoration request, decision-request record for the next decision, prospective work-plan entry, or explicit source-gap note.

#### A.15:5.1.c - Scenario guides method selection, not performed work

**Source set.** A method-selection scenario says that material X is below threshold T, resource window W is available, and the fabrication cell is under setup condition S. The scenario is the source episteme or source publication for choosing between method families.

**Published slice.** `Under scenario S, method family MF-2 is admissible for planning; choose the selected method and prepare the work plan before execution.`

The scenario can guide method-family selection and work-planning preparation. Once the team selects a method or prepares a plan, record that project choice or plan as the selected `A.15` selected-method, work-plan, or work-occurrence record named by value. If the scenario is used for evidence, gate, or engineering-justification reliance, first recover the project evidence relation, gate or constraint decision, or engineering-justification record named by value under `A.10`, `A.20`, `A.21`, or `B.3`; otherwise record only a source-restoration request, decision-request record, prospective work-plan entry, or source-gap note.

### A.15:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto and Epist**, **Prag**, **Did**. Scope: **Universal** for contextual enactment across engineering, operational, and knowledge-work settings.

Bias risks and mitigations:

* **Governance bias (Gov):** teams may over-treat role labels or approval displays as enough evidence that work happened.
  *Mitigation:* keep `U.RoleAssignment`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` distinct, and let only `U.Work` carry actuals and resource use.
* **Architectural bias (Arch):** modelers may pull roles or capabilities into structural part hierarchies because those diagrams are already present.
  *Mitigation:* preserve role and capability as context-bound assignment and ability values, not parts.
* **Epistemic bias (Onto and Epist):** a documented recipe or schedule can be mistaken for proof of execution.
  *Mitigation:* require the traceability chain from `U.RoleAssignment` and `U.MethodDescription` to dated `U.Work`.
* **Pragmatic bias (Prag):** teams may keep using one overloaded source-side "process" word because it feels faster.
  *Mitigation:* resolve "workflow", "schedule", and "what happened" source cues through `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work`.
* **Didactic bias (Did):** the chef analogy can make the pattern seem intuitive while hiding the need for explicit model links.
  *Mitigation:* pair the analogy with the canonical relations and checklist.

### A.15:7 - Conformance Checklist

To preserve role-method-work modeling, check the following predicates.

| ID | Predicate | Purpose and rationale |
| :--- | :--- | :--- |
| **CC-A15-1 (Entity Distinction)** | Keep `U.Role`, `U.Method`, `U.MethodDescription`, `U.Capability`, `U.WorkPlan`, and `U.Work` as distinct values. | This is the core use of A.7 strict distinction for role-method-work alignment. |
| **CC-A15-1a (Work target and kind predicate)** | A `U.Work` record satisfies `A15-WF-1`: `primaryTarget` and `kind` are present. Missing target or kind lowers the work-record conformance claim. | Keeps target and work kind enforceable as work-record predicates without RFC deontic prose. |
| **CC-A15-2 (Temporal Scope)** | `U.Method`, `U.MethodDescription`, and `U.WorkPlan` are design-time or plan-side values; `U.Work` is the dated performed occurrence. Operational events do not mutate method descriptions or work plans. | Preserves design-time and run-time separation. |
| **CC-A15-3 (RoleAssignment link)** | A `U.Work` record links through `performedBy` to a `U.RoleAssignment` satisfying the governing role, holder, bounded-context, and window constraints. | Gives every work occurrence a context-bound actor without making the role act by itself. |
| **CC-A15-4 (Traceability Chain)** | Each `U.Work` occurrence can be traced through `Work -performedBy-> RoleAssignment`, `Work -enactsMethod-> Method`, and, when a description or source is used to identify or constrain the method, `Method -isDescribedBy-> MethodDescription` or `methodDescriptionRef`. Capability checks are evaluated against the holder at run time. | Keeps auditability from occurrence back to method and the method-description source when that source is used. |
| **CC-A15-5 (No Roles in Mereology)** | Do not place `U.Role` or `U.Capability` in a mereological `partOf` hierarchy. | Blocks role-as-part and capability-as-part mistakes. |
| **CC-A15-6 (Resource Honesty)** | Associate resource consumption with `U.Work`, not with `U.MethodDescription`, `U.WorkPlan`, or `U.Capability`. | Keeps costs tied to actual occurrences rather than recipes, plans, or abilities. |
| **CC-A15-7 (Plan and Run Split)** | Represent schedules and calendars as `U.WorkPlan` under A.15.2. Do not use a `U.WorkPlan` as evidence that execution occurred; only `U.Work` carries actuals. | Preserves plan-side and run-time separation and prevents schedule-as-actual drift. |
| **CC-A15-8 (Source-cue resolution)** | Interpret unqualified "process", "workflow", "activity", or "schedule" source cues through `E.10` and `E.10.ARCH`: recover whether the cue points to `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work`, or another direct governing pattern. | Keeps source vocabulary auditable without creating a generic process object. |
| **CC-A15-9 (Enactment)** | A `U.Work` record enacts a `U.Method` under a `U.RoleAssignment`; a `MethodDescription` is the source episteme or method-description reference when the method is identified, constrained, or justified by a source. Spontaneous physical evolution without role-method-work alignment is modeled as `U.Dynamics`, not as `U.Work`. | Prevents background dynamics and recipe documents from being miscast as governed work. |
| **CC-A15-10 (Gate split)** | A speech act that institutes a role, authorization, or gate-relevant effect is a distinct communicative `U.Work` occurrence when the act itself is being modeled. It may create a gate-relevant condition for later operational work, but it is not that operational work. | Preserves communicative effects as distinct acts. |
| **CC-A15-11 (Kind fit)** | A `performedBy` relation uses a `U.RoleAssignment` whose role fits the `U.Work` kind and context, such as an approver role for communicative approval work or deployer role for operational deployment work. | Prevents kind-mismatched role attribution. |
| **CC-A15-12 (Causal-use work boundary)** | Intervention assignment, counterfactual randomization, target-trial emulation, causal evidence collection, and realized counterfactual-sampling work may be represented here only as `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work`, and role-assigned execution structure. Any causal-use admissibility claim cites `C.28` for causal-use question, `CausalityLadderRung`, causal estimand, `CausalEvidenceSupportBasis`, `CausalUseSupportVerdict`, supported use, and unsupported use. | Prevents method, plan, or occurrence structure from being mistaken for causal-use authority. |
| **CC-A15-13 (A.15.4 boundary)** | If an encountered source candidate or display is being used for a work relation or reliance relation by appearance, use `A.15.4` for the source-restoration question and keep only the role, method, method-description, work-plan, and work separation here. | Prevents the A.15 kernel from absorbing source-restoration claims. |
| **CC-A15-14 (P2W publication boundary)** | Do not treat a principle scheme, functional diagram, scenario, screen, or explanation that makes an `E.18.1` P2W carry-through structure recoverable as the selected method, `U.WorkPlan`, performed `U.Work`, work-result record, result measurement, or non-A.15 claim by publication alone. | The project use names the selected A.15 object by value; any non-A.15 claim uses its governing pattern or `A.15.4` source restoration. |

### A.15:8 - Common Anti-Patterns and How to Avoid Them

- **Role-as-part.** Do not place `U.Role` or `U.Capability` inside structural `partOf` decomposition; keep role as contextual assignment value and capability as ability value under stated conditions.
- **Recipe-as-evidence.** A `U.MethodDescription` or SOP may identify or constrain a method; dated `U.Work` records carry the occurrence claim.
- **Plan-as-actual.** Do not let schedules, calendars, or intended assignments stand in for actual execution; use `U.WorkPlan` for intent and `U.Work` for actuals.
- **Capability-as-work.** Do not treat possession of a capability as if the task has already been performed; capability enables execution under conditions but is not execution.
- **Approval collapse.** Keep approval or authorization speech acts distinct from the operational step they permit; model them as communicative `U.Work` when they institute a role, gate, or commitment effect.
- **Process soup.** Do not leave "process", "workflow", or "activity" uninterpreted in FPF-governed passages; resolve the source cue to `U.Method`, `U.MethodDescription`, `U.WorkPlan`, or `U.Work`.
- **Briefing-as-execution-cue.** A lighter review note, rollout summary, or redacted operations note may orient work; use `A.15.4` or the source-restoration pattern governing that reliance before relying on it for execution, approval, gate, evidence, or plan claims.
- **P2W publication as work occurrence.** A principle scheme, functional diagram, scenario, screen, or explanation may guide selected method or work-planning uses named by value; recover the project-side FPF kind and reference named by value for any selected-method, work-plan, work-occurrence, result, evidence, gate, or engineering-justification claim, and keep the `E.18.1` carry-through structure separate from those typed values.
- **Source candidate or display as work source.** A dashboard tile, credential display, copied approval, generated explanation, provenance label, command-like cue, or composed source chain is only a source candidate until `A.15.4` recovers the project-side kind and reference named by value needed for the work or reliance claim under repair.

### A.15:9 - Consequences

| Benefits | Trade-offs and Mitigations |
| :--- | :--- |
| **Unambiguous Communication:** Provides a shared, precise vocabulary for teams to discuss roles, methods, work plans, work occurrences, and results, eliminating the ambiguity of source terms like "process." | **Initial Learning Curve:** Requires teams to learn and internalize the distinctions between the core entities. *Mitigation:* The "Chef" analogy and clear archetypes serve as powerful didactic tools. FPF tooling can guide users with templates. |
| **End-to-End Traceability:** The framework creates a traceability relation that links each admitted operational event (`U.Work`) back to its role assignment, context, method-description source, plan when current, and evidence/provenance relations. This is critical for regulated industries and for root-cause analysis. | **Increased Formality:** Requires more explicit modeling than informal approaches. *Mitigation:* This is a strategic investment. The upfront cost of formal modeling is offset by downstream savings in debugging, re-work, and compliance efforts. |
| **Enables True Modularity:** By separating capability from execution, the framework allows for easier substitution. A `MethodDescription` can be updated without invalidating past `Work` records. A `Holder` can be replaced with another, as long as it possesses the same `Capability`. | - |
| **Foundation for role-source accountability:** The model makes it possible to state role-bound work rules without making the role or publication act. For example: "Only a holder acting under `AuditorRole` in a `U.RoleAssignment` satisfying the governing role, holder, and bounded-context constraints can perform the `U.Work` that instantiates the `ApproveRelease` capability." | - |

### A.15:10 - Rationale

This pattern solves a problem that has plagued systems modeling for decades: the conflation of what a system *is* with what it *does*. Its rigor is not arbitrary but is grounded in several key intellectual traditions.

*   **Ontology Engineering:** The pattern is a direct application of best practices from foundational ontologies (like UFO), which have long insisted on the distinction between *endurants* (objects like a `U.System`) and *perdurants* (events and performed occurrences such as `U.Work`), and between intrinsic properties and relational roles. FPF makes these powerful distinctions accessible to practicing engineers.
*   **Process-theory source tradition:** Formalisms like the Pi-calculus or Petri Nets model dynamic interactions under terms often translated as processes. A.15 does not import `process` as a new FPF object; it maps the useful local use to `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and dated `U.Work`. The `U.Work` entity can be seen as an occurrence recognized by such a source tradition, but FPF adds the crucial context of the `Role`, `Capability`, enacted `U.Method`, and `MethodDescription` source that make the occurrence inspectable.
*   **Pragmatism and Practice:** The framework is deeply pragmatic. The distinctions it makes (e.g., between a `MethodDescription` and `U.Work`) are precisely the ones that matter in the real world of project management, compliance, and debugging. When a failure occurs, a manager needs to know: was the recipe wrong (`MethodDescription`), did the chef lack the skill (`Capability`), or did they just make a mistake this one time (`U.Work`)? This framework provides the vocabulary to ask and answer that question precisely.

By creating this clean, stratified alignment for enactment, FPF provides a stable and scalable foundation for downstream resource accounting, decision, constraint, gate, evidence, assurance, ethics, and transformation patterns without letting any one of those neighboring claims collapse into A.15.

### A.15:11 - SoTA-Echoing: Adopted and Adapted Invariants and Rejected Shortcuts

**SoTA alignment rule.** Read each row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and Relations of this pattern.

**Claim 1.** Best-known current workflow, digital-thread, and service-operations source traditions keep recipe, plan, and execution separate.

**Practice source, local alignment, and adoption decision.** Contemporary process-modeling source traditions, service operations, and auditability practice after 2015 separate procedure, schedule, and executed occurrence because otherwise paper compliance becomes indistinguishable from completed work. In the manufacturing and peer-review slices above, this means a procedure or calendar never counts as the weld or the review itself. This pattern **adopts** that separation, **adapts** it through `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work`, and **rejects** the shortcut where one undifferentiated "process" label carries all three meanings.

**Claim 2.** Best-known current accountability practice keeps actor-in-context explicit rather than attributing work to a role label or a document.

**Practice source, local alignment, and adoption decision.** Contemporary service delivery, incident practice, and role-accountability practice distinguish accountable assignee, governing procedure, and actual run record because after-the-fact review depends on knowing who acted, under what role, and under which method. In the slices above, that is why the welding robot or peer-review assignee acts under `U.RoleAssignment` rather than the role or guideline acting on its own. This pattern **adopts** explicit actor-in-context attribution through `U.RoleAssignment`, **adapts** it to bounded-context semantics, and **rejects** anonymous work logs and role-as-part modeling.

**Claim 3.** Best-known current approval and execution practice treats communicative gate acts and operational acts as distinct kinds of work.

**Practice source, local alignment, and adoption decision.** Contemporary release, compliance, and safety-critical practice separates approval, authorization, and review acts from the operational steps they permit because authority change and world change are not the same event. In the examples above, that means an approval is not the same work as a deployment or a weld. This pattern **adopts** that split, **adapts** it through communicative versus operational `U.Work` kinds, and **rejects** the collapse of approval into the thing being approved.

**Local claim.** The FPF-governed SoTA claim for this pattern is practical and narrow: contextual enactment remains reviewable only when role, method, plan, and work stay distinct enough that audits can tell whether the problem was in the assignment, the recipe, the schedule, the capability, or the run itself.

**Claim 4.** Best-known current agentic work practice treats fast bounded specialization as a checkpointed scout and probe discipline rather than as a naked winner claim.

**Practice source, local alignment, and adoption decision.** Contemporary agentic tool-use, adaptive method-selection, and human-in-the-loop work-control practice separates bounded exploration from committed rollout because a successful probe is not yet an admissible committed approach. In the working moment above, that is why the pair returns one `CheckpointReturn` with candidate approaches, evidence, burned and residual budget, and a commit trigger rather than only a winner label. This pattern **adopts** checkpointed scout and probe discipline, **adapts** it through the dyad-local roles and `CheckpointReturn`, and **rejects** the shortcut where an early probe silently becomes a committed rollout.

| Claim need | Source idea and current source | Current source reference | Local FPF invariant and practical local test | Adopted invariant, adapted invariant, and rejected shortcut |
| --- | --- | --- | --- | --- |
| Recipe, plan, case, decision, and executed occurrence stay separable. | Case-management, decision-modeling, and service-change practice distinguish discretionary case work, decision logic, planned change source material, and the realized service or product change. | OMG CMMN 1.1 (2016); OMG DMN 1.5 (2024); ITIL 4 Practitioner: Change Enablement (2023); source maturity = mature modeling standards plus current practitioner guidance. | The manufacturing, peer-review, and rollout slices keep `U.MethodDescription`, `U.WorkPlan`, approval work, and `U.Work` separate so a calendar or procedure never counts as the weld, review, deployment, or actual run. | **Adopt and adapt.** Adopt the separation of case, decision, plan, and occurrence; adapt it to FPF's `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work`; reject an undifferentiated "process" label as an FPF object. |
| Architecture and digital-thread practice need traceable views without confusing description, authority, and occurrence. | Architecture-description and model-based systems practice treat descriptions, viewpoints, requirements, behavior, verification, and traceability as explicit review targets. | ISO/IEC/IEEE 42010:2022; OMG SysML v2.0 Language Specification (2025); source maturity = mature standard plus current technical specification. | `A.15` uses actor-in-context, role assignment, method description, and work occurrence so after-the-fact review can ask whether the problem was assignment, capability, recipe, plan, approval, or run. | **Adopt and adapt.** Adopt explicit trace and viewpoint discipline; adapt it to role, method, work-plan, and work-occurrence alignment; reject attributing work to a role label or document alone. |
| Approval and execution are distinct practical acts. | Change-enablement and decision-modeling practice separates risk assessment, authorization, scheduling, decision logic, and the work that realizes change. | ITIL 4 Practitioner: Change Enablement (2023); OMG DMN 1.5 (2024); source maturity = current practitioner guidance plus mature modeling standard. | In the release and gate examples, an approval or authorization institutes an authorization or gate-relevant effect; it is not the same work as deployment, welding, or other operational occurrence. | **Adopt.** Adopt the distinction between communicative work and operational work, and reject collapse of approval into the thing approved. |
| Fast bounded exploration does not become committed rollout by convenience. | Contemporary agentic tool-use and adaptive-work practice, including ReAct, Toolformer, and Reflexion-style tool-use and self-correction lines, allows bounded probing while preserving explicit transition from option exploration to committed change. | Current agentic tool-use and self-correction practice; ITIL 4 Practitioner: Change Enablement (2023); ISO/IEC/IEEE 42010:2022; OMG SysML v2.0 Language Specification (2025); source maturity = current technical and practitioner guidance plus mature and current modeling standards. | The scout and probe moment returns candidate-approach evidence, observed result, burned and residual budget amounts, and a commit trigger rather than a selected method, `U.WorkPlan`, performed `U.Work`, or rollout decision. | **Adapt and reject.** Adapt bounded scout and probe discipline to FPF role, method, work-plan, and work-occurrence splits; reject the shortcut where an early probe silently becomes a committed method choice, work plan, or rollout. |

For visible credential, provenance, dashboard, explanation, or composed-source cases that need project-side FPF kind and reference named by value before work or reliance, use `A.15.4`. The A.15 family carries only the role, method, plan, and work portion of the case.

The nearest recovery loci are the manufacturing, peer-review, rollout briefing, `CC-A15-7`, `CC-A15-10`, `CC-A15-12`, and the boundary to `A.15.4`. If a SoTA row cannot be recovered through those local checks, do not let the source citation stand in for the local `A.15` rule.

### A.15:12 - Relations
*   **Architecture method/work boundary:** `C.32.P2S` and `C.32.PAD` may cite method descriptions, pattern-use refs, responsible roles, readiness exits, and expected structure effects as architecturing or decision-output duties. `C.32.ADR` may publish those refs. A.15 still governs method, method description, work plan, work-entry readiness, performed work, and role enactment claims.

*   **Directly applies:** `A.7 Strict Distinction` for the role, method, method-description, plan, and work split.
*   **Builds upon:** `A.2` for `U.Role`, `A.2.1` for `U.RoleAssignment`, `A.2.2` for `U.Capability`, `A.2.5` for role-state admission, `A.2.7` for role relation structure, `A.6.5` for slot-relation discipline used by assignment and relation declarations, `A.3.1` for `U.Method`, `A.3.2` for `U.MethodDescription`, `A.3.3` for `U.Dynamics`, `A.3.4` for `U.Transformation`, `A.15.1` for `U.Work`, `A.15.2` for `U.WorkPlan`, `A.15.3` for slot-filling plan items, and `A.15.5` for work-entry readiness.
*   **Coordinates with:** `A.15.4` for work-relevant source restoration; `A.15.5` for full-kit preparation and work-entry readiness; `E.10` and `E.10.ARCH` for source cue recovery around process, workflow, activity, schedule, algorithm, solver, and procedure wording; `A.6`, `A.6.B`, and `A.6.C` for mixed boundary, policy, API, schema, agreement-like, or promise wording; `A.10` for evidence, currentness, and provenance; `B.3` for assurance claims; `A.21` for `OperationalGate(profile)`, `GateDecision`, and `DecisionLogRef`; `A.20` for `ConstraintValidity` status or witness; `C.28` for causal-use admissibility; `C.29` for mathematical-lens use; `E.18.1` for P2W carry-through; `C.32.P2S` for architecturing flow refs to method, work plan, readiness, and performed work; and `E.17.EFP` for generated-explanation faithfulness or source-finding.
*   **Used by:** patterns that need to keep systems or acting holons with role assignments, method descriptions, work plans, work occurrences, result records, and source-restoration claims distinct. A.15 is not a generic process ontology, workflow engine, evidence graph, gate pattern, or publication pattern.

### A.15:12a - Coordinated-work evidence and distributed-state relation note

Use A.15 first when the claim is about who acts, by which method, under which role, under which work plan, producing which work result. Coordinated work, routine skill, team alignment, tacit knowledge, and role-method fit are not quantum-like by default.

Application choices:

1. Name the role, method, and work result before naming any distributed state.
2. State which work traces, records, events, observations, reports, metrics, `U.Work` occurrences, or `RoleEnactmentFact` records make the coordination visible.
3. Ask whether role-method-work alignment alone explains the case. If yes, stay in A.15.
4. If no participant statement, local component report, single evidence record, dashboard, or exported representation carries the inferred state faithfully enough for the intended state use, add a `C.26.2` low-recoverability distributed-state reading.
5. State the weakest evidence-bound state-reading claim, time window, rival explanations, and export loss.
6. Carry evidence use through `A.10` and assurance claims through `B.3` when the reading will guide work, reliance, audit, readiness, release, or compliance.

Add a `C.26.2` low-recoverability distributed-state reading only when coordinated work is being used as evidence for a state that no participant statement, local component report, single evidence record, dashboard, or exported representation carries faithfully enough for the intended state use. In C.26.2 terms, the reading is a minimal evidence-bound `U.Episteme` claim under carriers, window, rivals, and export limits; it is not a group mind, not performed work, not evidence sufficiency, and not assurance by itself. That evidence-bound reading states:

| Field | Required content |
| --- | --- |
| Evidence/provenance source relation | Work trace, record, event, observation, report, metric, `U.Work` occurrence, or `RoleEnactmentFact` record used by `A.10` or `G.6` for the stated claim |
| Time window | When the distributed-state reading holds and when it decays or needs refresh |
| Probe or occasion | What question, task, workshop, incident, handover, dashboard, or coordination situation made the state inferable |
| Weakest claim | The minimal distributed-state reading carried by the evidence sources |
| Rival explanations | Routine compliance, policy, command, coincidence, incentive, documentation record, or local skill that could explain the same work |
| Export loss | What is lost when the state is summarized into one report, score, or statement |

Useful outputs:

- an A.15 work-alignment claim when work roles explain the case;
- a C.26.2 low-recoverability distributed-state reading when coordination evidence survives ordinary rivals;
- an `A.10` evidence relation or `B.3` assurance claim relation when the distributed-state reading will be used as evidence or assurance for a work claim or reliance claim;
- no distributed-state reading when evidence sources, rivals, or time window cannot be named.

### A.15:12b - C.29 mathematical-lens use relation

> If a mathematical lens helps select a method, compare method families, shape a work plan, or diagnose work, use `C.29` only for the fit of that mathematical diagnostic or method-selection reason. The next concrete object remains under the A.15 family: `ChoiceResult` or local choice record when a choice is made, selected method or method-family selection when the method-governance claim is being made, `U.WorkPlan` for a plan, performed `U.Work` and work-result record for execution, and an `A.15.4` source-restoration reference when the issue is work-relevant source restoration. A mathematical lens may explain why a diagnostic distinction is useful; it does not make a plan into performed work or a method explanation into execution evidence.

### A.15:12c - P2W Work-Family Split

When a P2W use under `E.18.1` produces a `WorkPlanning` or work-entry readiness relation, this family carries the split among selected method, `U.WorkPlan`, `SlotFillingsPlanItem`, `WorkEntryReadiness@Context`, performed `U.Work`, and result-related records. A P2W principle scheme, functional diagram, or scenario may guide method inspection and work-planning preparation only after the current work-family object is named.

WorkPlanning may place evidence-reference hooks and source-currentness requests for the governing pattern that carries the relation under repair. `A.15.5` may cite WorkPlan and SlotFillingsPlanItem baselines when readiness is the current relation. If the relation under repair is evidence, gate passage, launch-value finalization, performed work, result measurement, assurance, or refresh, name that relation before relying on the work-planning or readiness record.

### A.15:12d - P2W Performed-Work Relation

When `E.18.1` reaches performed work, this family keeps the current kind as `U.Work`. WorkEnactment wording is explanatory only: it points to dated performed work, not to a second work kind.

A performed-work record may cite a `U.WorkPlan` and planned baseline, while recording launch values, actuals, substitutions, variance, telemetry, outputs, outcome, and result-related records in the performed-work occurrence. Comparator, transport, `PrincipleFrame`, `U.Signature(profile=FormalSubstrate)`, evidence, assurance, and gate relations are named separately when those claims are being made.

### A.15:12e - P2W Integration As Role Enactability

When `E.18.1` uses integration wording to mean role enactability under interface constraints, this family carries the role, method, plan, and performed-work part of the claim. Name the selected role, `U.RoleAssignment` when the role-assignment claim is being made, method or method description, relevant `U.WorkPlan` or performed `U.Work`, and the interface constraints governed by the architecture or module-interface pattern.

If the same phrase also raises connected artifacts, telemetry, acceptance records, diagrams, module-interface claims, selected-structure claims, checks, gates, evidence, or provenance, split those relations before relying on the integration wording.

### A.15:12f - Lowering, Repair, and Refresh Conditions

Lower an `A.15` claim when the role, holder, bounded context, method, method description, work plan, work-entry readiness relation, performed work occurrence, or capability check cannot be named at the granularity required by the next work-family use. A weaker but admissible result is a separation note, source-gap note, source-restoration request, decision-request record for the next decision, prospective work-plan entry, or `A.15.5` readiness-gap note.

Repair the local alignment frame when a subsequent source shows that the role assignment, method description, work-plan baseline, performed-work occurrence, capability threshold, role-state currentness record, or source-currentness window was wrong for the claimed use. Repair only the changed relation: do not rewrite the method when only the work plan changed, do not rewrite the work occurrence when only the evidence relation changed, and do not treat a source-restoration request as carrying a non-A.15 claim.

Refresh the `A.15` use before relying on it across a new context, new role assignment, new method family, new work plan, new execution window, new result measurement, or new evidence, assurance, gate, source-restoration, or mathematical-lens relation. If the issue under repair after refresh is no longer role-method-work alignment, use the governing pattern for that relation and keep only the remaining `A.15` separation here.

### A.15:End

