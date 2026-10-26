## C.32.FAIL - Architecture Failure Recognition and Repair

> **Type:** Architectural subpattern under C.32
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.32.FAIL:1 - Problem frame

Use this pattern when a recurring architecture-synthesis failure needs a first justified repair action over a named architecture object. The action may recover a missing premise before a structural change can be chosen.

Primary working reader: an architect or architecture-responsible practitioner who sees a warning sign during synthesis and needs the first architecture repair action, not a larger risk catalogue.

Typical entry cues:

```text
"This looks modular, but changes still cross hidden dependencies."
"The model is called a module, but the interface is weak."
"The platform promise hides exception growth."
"The search picked a winner, but the alternatives and losses disappeared."
"The graph looks convincing, but we cannot say which architecture object it repairs."
```

**First-minute use slice.** A team calls an ML model a module in a safety-relevant product architecture. Using C.32.FAIL, the practitioner names the architecture object under stress: a candidate module-interface relation for the described product holon. The blocked overread is: model file equals stable module. The first repair action is to recover interface behavior, admissible-use conditions, change policy, and evidence-decay boundary before using the model as a module. If a safety assurance claim is current, use its subject pattern with the identified architecture question and available evidence.

The primary `EntityOfConcern` is one repair cue for one architecture object under stress. The cue is a working repair aid, not a risk register, assurance case, selection result, release argument, or decision object.

What goes wrong if C.32.FAIL is missed: failure language degenerates into a warning bank. The team can say what looks suspicious, but it cannot say which architecture object must be repaired or which pattern defines or constrains the next claim.

What C.32.FAIL buys in practice: a practitioner can convert a vague failure signal into one typed repair action, keep the repair near the selected structure, and stop before nearby decision, release, or governance claims expand the case.

Ordinary working move: explain the symptom, affected architecture object, first justified repair action and its stop or continuation condition. Name a mistaken inference when it explains the failure.

After using C.32.FAIL, the reader can identify the affected architecture object, the first repair action and its stop or continuation condition.

Use another pattern when the current work is only lexical cleanup, evidence sufficiency, release, architecture description, MVPK publication face, comparison, selection, archive, front, selected-set result declaration, actual publication, local choice, or final architecture decision. Use C.32.FAIL only when the failure cue changes the first architecture repair action.

Common exits by claim kind:

- `C.30.P`, `A.6.F`, `A.6.M`, `C.31`, `C.32`, `C.32.MLAO`, and `C.32.CONWAY` for architecture or selected-structure repair.
- `A.19.CPM` for explicit comparison and `A.19.SelectorMechanism` for set-returning selection.
- `C.18` and `C.19` for archive, front, pool-treatment, or retained-stepping-stone claims.
- `A.10` for evidence, `B.3` for assurance, `A.20` for internal-constraint validity, and `A.21` for a named gate decision under an applicable profile, including a release gate when current. Release requirements remain with the patterns that define them.
- `C.30.AD` for architecture description, `E.17` for a source-backed publication face and source return, and `E.24.PUB` for the publication occurrence and audience availability.
- `G.5` for selected-set result declaration, `C.11` for local choice, and `C.32.PAD` for a project decision. For publication, keep the distinct E.17 and E.24.PUB uses just named.

The first useful output names the affected architecture object and a justified next action. An ordinary explanation can suffice; `ArchitectureRepairCue@Project` can organize it when a record is useful:

```text
ArchitectureRepairCue@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureRepairCueProjectUseRelationRef?: U.RelationRef defined by the exact repair-use or work-use pattern
  symptom:
  describedHolonRef:
  architectureClaimRef?:
  architectureConcern:
  intendedRepairUse:
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?:
  architectureObjectUnderStress:
  selectedStructureRef?:
  sourceCueRef?:
  failureEvidenceRefs?:
  blockedOverread?:
  firstPatternLocator?:
  repairAction:
  sourceReturnCondition?:
  stopCondition:
  escalationIfCurrent?:
```

Here `@Project` is a compatibility and retrieval cue only. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. When the repair cue is genuinely used in one actual project, `projectWorkOccurrenceRef` identifies the exact composite `U.Work` and `architectureRepairCueProjectUseRelationRef` identifies the direct relation by which that exact project Work uses the cue. Any separately claimed repair Work and its own cue-use or work-to-change relation remain under their direct governors. The cue, the actual repair Work, the architecture object under stress, and the composite project Work remain distinct.

### C.32.FAIL:2 - Problem

Architecture synthesis often fails before formal evidence or decision work starts. The defect is not only that a word is vague. The practical defect is that the architecture object under stress is missing or misread.

Most first-contact failures cluster into a few repair-entry families:

* a proposed bearer, module, platform, or universal substrate hides interface behavior, variation pressure, function bearing, evidence burden, or new coupling;
* a proxy result, generated artifact, architecture description, graph, dashboard, front member, or workshop favorite is used before the selected structures, losses, and pattern for the next question are named;
* one structure, function, system-role kind or assignment, responsibility, control relation, evidence relation, or Method step is improved while the synthesis frame loses the architecture characteristics and other structures that made the trade-off real;
* a current candidate is treated as a durable optimum, or ideality pressure deletes a bearer without naming the function still carried, the lost structure, and the new burden;
* an influence-source architecture and the transformed-side architecture content collapse into one claim instead of opening C.32.CONWAY and separating the changed referent, each obtaining C.30 architecture relation or modal `ArchitectureClaim`, any asserted direct influence occurrence, and any separately current actor, assignment, Work, or actual transformation facts.

These cues are useful only when each one is converted into a repair shape: symptom, architecture object under stress, first repair action, and stop or pattern for the next question.

```text
symptom -> affected architecture object -> justified repair action -> stop or continuation
```

Use C.32.FAIL for that conversion. It does not mint a local ontology of failure kinds.

### C.32.FAIL:3 - Forces

| Force | Tension |
|---|---|
| Fast recognition | Practitioners need short warning cues while the repair object is still unclear. |
| Object recovery | Source expressions and domain habits can hide the architecture object under stress. |
| Repair locality | The first useful repair action should change architecture handling, not open a broad audit. |
| Neighboring claim patterns | Evidence, assurance, gate, release, selection, and decision claims may be nearby but governed elsewhere. |
| Cue inflation | Warning rows can multiply without improving repair unless admission requires a concrete repair action. |

### C.32.FAIL:4 - Solution

Develop the first repair action from the warning cue. The following six moves guide that work:

1. State the symptom in ordinary practitioner language.
2. Name the affected architecture object, described holon, concern and intended repair use. Preserve available observations and unresolved questions; add an architecture claim, scope or qualification window when material.
3. If a mistaken inference explains the failure, state it and the distinction needed to correct it.
4. Use the subject pattern for the architecture object or lens relation when its definition or test is needed; cite it when the next user needs that route.
5. Propose the smallest action that can resolve the architecture difficulty. If a consequential premise is unknown, first recover the observation or subject result that can settle it.
6. State where to stop, or which neighboring pattern defines or constrains the next claim if another claim is already current.

Core repair families for a first repair-cue draft:

| Repair family | Symptom | Architecture object under stress | First repair action | Stop or pattern for the next question |
|---|---|---|---|---|
| Weak module-interface | A source-side bearer is called a module because it has a convenient boundary. | Candidate module-interface relation and selected structure boundary. | Recover interface behavior, admissible-use boundary, change policy, and interface-conformance witness. | Stop at repaired interface cue; module-interface structure claims belong to `A.6.M`, `C.30.ASV`, or `C.31` when current. |
| False platform | A reusable-structure promise hides variation pressure and local exceptions. | Variation structure, substitution policy, evidence scope, and exception boundary. | Recover variation slots, substitution rules, substitution-conformance checks, and exception-growth trigger. | Cross-scope residual work belongs to `C.32.MLAO` when current. |
| Hidden single winner | A comparison or generation result is treated as selected architecture. | Candidate palette and retained alternatives. | Recover the C.32 alternatives, expected gains and losses, including source-return conditions when needed. Reuse an adequate palette; develop missing alternatives when they can change the choice. | State explicit comparison under the A.19.CPM predicate, set-returning selection under A.19.SelectorMechanism, selected-set result declaration under G.5, local choice under C.11, and a project architecture decision under C.32.PAD. For publication, state the E.24.PUB occurrence and audience availability, with E.17 source-backed face and source return when needed. |
| Proxy result or description as authority | A score, graph, residual vector, generated output, architecture-description artifact, or MVPK publication face is used to accept or prefer an architecture candidate before the selected structure and pattern for the next question are named. | Candidate architecture claim and selected-structure relation hidden behind the proxy, description, or visible result. | Recover the selected structure, source-side referent, view relation, or lens-output relation first. Use `C.29` for mathematical-lens output, `C.30.ASV` or `C.30.AD` for view or description use, `A.19.CPM` for comparison, `C.11` for local choice, `A.19.SelectorMechanism` for set-returning selection, and `G.5` for selected-set result declaration. For publication, use `E.24.PUB` for the occurrence and audience availability; add `E.17` when a source-backed face and source return are needed. | Stop when the visible work product only orients repair; evidence claims belong to `A.10` and assurance claims belong to `B.3`. |
| Coordination cost displaced by responsibility change | A change in ordinary work organization or a responsibility relation improves local flow while pushing coordination into module interfaces, shared test, evidence, approval, or deployment structures. | Team or organization System and its relations; coordination relation; module-interface, evidence, deployment, Method or plan structure; and, only when current, local kind, separate System-classification judgment, assignment, enactor relation, and actual Work network. | Recover the shifted coordination cost and the structure under stress. If responsibility retargeting is claimed, name its direct predicate, old and proposed participants, and occurrence identity or return `missing-governor`; then decide whether the architecture repair belongs to `C.32.CONWAY`, `A.6.M`, or `C.32.MLAO`. | Route unresolved role wording through `E.10.ROLE`. Keep ordinary work organization, Method or plan structure, local kind, separate System-classification judgment, assignment, enactor relation, dated Work, and responsibility as separate branches under their subject patterns. |
| Temporal or control coupling | Named parts need brittle timing or control coordination. | Temporal relation, control relation, and affected work or evidence relation. | Recover the timing or control constraint and ask whether a candidate architecture change affects the selected structure. | Temporal adequacy claims belong to `C.27`, control or mechanism placement claims belong to the governing mechanism pattern, and flow-structure claims belong to `E.18` when current. |
| Evidence jump | The team asks for more evidence without naming the architecture uncertainty it would settle. | Architecture object whose evidence relation may be stale, misplaced, or bearer-dependent. | Name the affected architecture object and the uncertainty the evidence must settle. Reuse available evidence or obtain the needed result under `A.10` and the subject rule; then choose the justified repair. | Evidence relations belong to `A.10`, assurance to `B.3`, internal-constraint validity to `A.20`, and a named gate decision to `A.21` under an applicable profile. Release requirements remain with the patterns that define them. |
| Generated output as authority | A generated architecture-looking output is treated as carrying an authority relation for architecture adequacy. | Source cue, generated description, candidate selected structure, and evaluation boundary. | Treat the output as a source cue; recover source-side referent, selected structure, architecture-change kind, gain, loss, and the review needed for the intended reliance. | Use `C.32` for candidate generation and `C.30.AD` for generated-description use. For publication, use `E.24.PUB` for the occurrence and audience availability; add `E.17` when a source-backed face and source return are needed. |
| Single-structure synthesis | One selected structure is improved and called the architecture synthesis. | Synthesis structure map and architecture characteristic bundle. | Use C.32; name the other selected structures that must be coordinated and the architecture characteristics that make the trade-off real. | Stop at repaired C.32 palette, or open `C.32.MLAO` if the failure crosses scopes. |
| User function as architecture characteristic | A user-visible function is treated as the architecture quality being optimized. | Functional demand, architecture characteristic, and quality bundle boundary. | Recover the function through `A.6.F` or `C.30.ASV`; then name the architecture characteristic or `C.25` quality bundle separately. | Keep function and characteristic distinct in the explanation before relying on their comparison. |
| Function with no feasible bearer | A function graph, workflow, use case, method step, or neural cell graph names a required function whose feasible bearer is missing or unresolved under the current constraints. | Functional demand, candidate bearer set, module-interface relation, placement or deployment relation, resource access, control relation, and evidence burden. | Use `C.32`. Possible first repairs include adding or changing a bearer, splitting the function, changing placement or resource access, changing control responsibility, reducing demand, or rejecting the candidate. | Keep feasibility unresolved or reject the candidate for the affected use. Comparison can retain a provisional or infeasible alternative with that status; stronger conclusions require their own premises. |
| Static optimum | A front member or local winner is treated as durable optimum. | Evolution window, pattern for the next question result, front or archive relation, and reopen trigger. | Recover the preference's evolution window and grounds, with source-return conditions where needed; use C.18 and C.19 for retention or pool policy. | Use `A.19.CPM` for comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, `G.5` for selected-set result declaration, and `C.32.PAD` for an architecture decision. For publication, use `E.24.PUB` for the occurrence and audience availability; add `E.17` when a source-backed face and source return are needed. |
| Ideality shortcut | Having fewer bearers or fewer modules is treated as architecture improvement by itself. | Function-bearing allocation, selected structure count, and architecture characteristic bundle. | Recover the function-bearing transfer; name the removed or generalized bearer, the functions still carried, the new burden, and lost structure. | Use `C.32`; use `C.31`, `A.6.F`, `A.6.M`, and `C.19.1` when their claims are current. |
| Universal bearer as adequacy shortcut | A universal module or general substrate is treated as architecture adequacy or scale adequacy by itself. | Scale-amenability claim, module-interface relation, evidence burden, control burden, and safety or admissibility boundary. | Treat the proposed universal module or general substrate as a candidate bearer; require BLP scale window or waiver when scale advantage is claimed and record coupling, evidence, control, and source-return effects. | Stop before G.5 selected-set result declaration, actual publication, assurance, release, or decision claims unless patterns for the next questions are current. |
| Mismatch between architecture influence and transformed-side structure | An influence-source architecture is collapsed with transformed-side architecture content, a desired transformed-side structure is paired with no compatible influence-source arrangement, or an architecture or selected structure is treated as the changing actor. | The exact changed referent; each influence-source-side and transformed-side obtaining C.30 `ArchitectureRelation` or modal `ArchitectureClaim`; and the direct architecture-influence or correspondence occurrence only when independently governed and obtaining. | Open `C.32.CONWAY`; recover the two exact architecture sides, the direct influence kind and predicate or `missing-governor`, and then prepare influence-source-side, transformed-side, joint, or bounded-mismatch candidates. Add acting systems, assignments, Work, and actual transformation only through their subject patterns when those claims are current. | Use `A.6.M` only for module-interface repair, `C.29` only when mathematical structural similarity is claimed, and E.18.NET only for an independently selected network; a C.32.CONWAY frame or exact pair row is neither an actor, network, nor cross-flow occurrence. |

Admit a new repair family only when its row tells the practitioner what to repair first. A suspicious name alone is not enough; the row must name the architecture object under stress, the first repair action, and the stop or pattern for the next question.

**Stop condition.** Stop when the affected object and justified next action are clear. Carry a source-return condition or another pattern when the next use needs it. A precise unresolved question can be the useful return; the cue itself supplies no evidence, assurance or decision verdict.

**Reconsideration condition.** Keep the symptom, affected object, supported observations and justified action current. If the object or repair remains unknown, retain the observation and the question needed to recover it. Missing documentation alone does not invalidate a known action. After a repair, examine whether it resolved the failure before retiring the active cue; preserve useful history. A changed object reopens the affected use. Use `A.6.P` or `E.10` when the case is only source-expression recovery, `C.32` when candidate repair is current, `C.32.MLAO` or `C.32.CONWAY` when their residual or correspondence repair is current, and the named pattern for the next question when a stronger downstream claim is current.

### C.32.FAIL:5 - Worked Repair Cases

**Tell.** C.32.FAIL is a repair-entry pattern. It takes a recognizable warning cue and returns one typed repair action over a selected architecture object. It is useful only when the repair action changes architecture handling.

**Show-A - Safety-relevant model-as-module.** A model file is being treated as a module in a product architecture. The repair cue names the candidate module-interface relation, blocks the file-equals-module overread, and recovers interface behavior, admissible-use conditions, change policy, and evidence-decay boundary. Safety assurance follows only through its subject pattern.

**Show-B - Product-family platform with exception growth.** A platform promise reduces local delivery effort but grows evidence exceptions at the product-family scope. The repair cue names variation structure, substitution policy, and evidence scope as the architecture objects under stress. The first repair action is not to declare the platform adequate; it is to repair variation slots and bounded-exception rules, then use `C.32.MLAO` to frame residual-reducing candidates if cross-scope burden is current; use `A.19.CPM` when an explicit comparison is needed.

**Show-C - Responsibility change shifts coordination cost.** A stream-aligned team improves local delivery flow, but release testing and evidence responsibility remain shared. The repair cue names the team or organization System, the coordination relation, and the module-interface and evidence structures under stress. A proposed responsibility retargeting names its direct predicate, the current and proposed participants, and the occurrence to replace; without that basis it returns `missing-governor`. Ordinary work organization, Method or plan structure, local kind, separate System-classification judgment, assignment, enactor relation, and actual Work network remain separate. C.32.CONWAY supplies only the architecture-influence synthesis frame or qualified pair row; it supplies none of those other facts.

**Show-D - Generated architecture candidate.** An agent system produces a high-scoring blueprint. The repair cue treats the blueprint as a source cue, recovers the selected-structure changes encoded in it, names preserved and lost structure, and recovers an adequate candidate palette for any comparison or decision that needs it. A publication can retain the proposal and its unresolved conditions under its own rules.

**Show-E - Built-asset maintenance dashboard.** A facility maintenance dashboard shows a dependency graph and freshness scores. The repair cue keeps the graph's mathematical-lens use bounded, recovers the actual selected structures under stress in maintenance work and asset interfaces, and keeps timing or evidence claims with their subject patterns.

**Show-F - Function with no feasible bearer.** A searched AI workflow adds a verification function after model output, but the edge device has no resource margin and the cloud placement violates latency. The repair cue names the function-bearing gap, then opens C.32. Candidate repairs can, for example, add a local bearer, split verification into local and cloud steps, change deployment placement, reduce the demand, or reject the candidate for the current evolution window.

### C.32.FAIL:6 - Repair-Entry Failure Modes

| Failure mode | C.32.FAIL repair action |
|---|---|
| **Warning name without repair action** | A warning row is useful only when it names the architecture object under stress and the first repair action. Otherwise keep the warning name out of the pattern. |
| **Evidence collection without a repair question** | Name the affected object and the uncertainty that evidence could settle. Obtain evidence or assurance through its subject pattern when needed; use that result to choose or revise the architecture repair. |
| **Decision jump** | A repair cue does not select an architecture. Recover adequate candidate or residual information for the intended use. Build what is missing; retain a sufficient existing result. Publication, selection and decision keep their own conditions. |
| **Source expression substitutes for architecture object** | Use a source term, method word, benchmark result, or generated output as a cue to recover selected structures and characteristics; the applicable subject pattern defines or constrains the architecture claim. |
| **Software-source overfit** | Software and AI sources can supply strong repair actions, but the action must be translated to selected structures of the described holon. |
| **Description carrier substitutes for repair** | Architecture descriptions and publication faces can make the problem visible; the repair cue must name the selected architecture object under stress and the repair action. |
| **Function and characteristic collapse** | Keep user functions and architecture characteristics distinct where they change the repair or comparison; separate record fields are optional. |
| **Function without bearer** | A functional architecture can remain a provisional candidate while feasibility is unresolved. Claim feasible use only when the required bearers and constraints support it. |
| **Ideality used as deletion admissibility** | Ideal final result wording is a generation pressure; deleting a bearer is admissible only after function bearing, lost structure, new burden, and architecture characteristics are named. |
| **Universal bearer admitted by name** | A universal module or general substrate must be treated as a candidate bearer under BLP scale-window discipline and declared architecture-characteristic criteria rows. |
| **Conway wording without correspondence repair** | For a correspondence repair, use `C.32.CONWAY` to recover the changed referent, relevant architecture sides, influence claim and its truthful disposition, affected characteristics and useful candidate alternatives. A preliminary account can retain unresolved questions; an exact pair requires its own admitted relations. Architecture influence supplies no actor, assignment, Work, actual transformation, network membership, or cross-flow relation. |

### C.32.FAIL:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-C32.FAIL-1` | The cue states a recognizable symptom in practitioner language. | Keeps the pattern usable at first contact. |
| `CC-C32.FAIL-2` | The affected object, described holon, concern, repair use and available observations or unresolved questions are recoverable, with claim, scope or qualification window when material. | Prevents source wording or a generic context field from replacing object recovery. |
| `CC-C32.FAIL-3` | A mistaken inference is stated when it explains the failure and changes the repair. | Makes the failure precise enough to repair. |
| `CC-C32.FAIL-4` | The applicable subject definition or test is used when needed; a locator is supplied when the receiving user needs it. | Keeps architecture, lens, work, evidence, assurance, and decision claims distinct. |
| `CC-C32.FAIL-5` | The repair action changes architecture handling. | Prevents warning-only rows. |
| `CC-C32.FAIL-6` | The stop condition or pattern for the next question is named. | Keeps the cue lightweight and composable. |
| `CC-C32.FAIL-7` | New cue rows name the architecture object, first repair action, and stop or pattern for the next question. | Prevents warning-bank inflation. |

### C.32.FAIL:9 - Consequences

| Positive consequence | Cost or trade-off |
|---|---|
| Failure recognition produces repair action. | Many tempting warning rows are rejected. |
| Repair stays near the architecture object under stress. | The team may need an observation or subject result before choosing a structural change. |
| Source expressions can be used as cues without carrying ontology. | Each cue must recover the described holon and selected structure. |
| C.32 candidate repair stays separate from final selection. | Selected-set result declaration, actual publication, or choice requires the pattern for the next question. |
| Generated or tool-derived architecture material can widen discovery. | Generated material must still recover source-side referent, selected structures, architecture-change kind, gain, loss and a review boundary appropriate to the intended candidate use. |

### C.32.FAIL:10 - Rationale

C.32 needs a failure-recognition subpattern because candidate architecture work repeatedly breaks at the repair-entry point. The useful work is to recover the architecture object under stress and make the next repair action reviewable.

The pattern stays intentionally small. It does not establish failure, make a score-based risk finding, select a candidate, or authorize a release. It gives practitioners a disciplined way to go from "something is wrong here" to "this architecture object needs this repair, and this neighboring pattern defines or constrains the next claim if it is current."

### C.32.FAIL:11 - SoTA-Echoing

These rows show how source practice informs C.32.FAIL repair fields, repair families, boundaries, and receiving-pattern exits.

| Source to inspect | Why this source is load-bearing here | Transfer into C.32.FAIL | Blocked overread |
|---|---|---|---|
| Current FPF architecture kernel: `C.30`, `C.30.AD`, `C.30.ASV`, `C.31`, `C.32`, `C.32.MLAO`, plus `A.6.P` and `E.10` | Current local law for architecture objects, source-expression recovery, and candidate repair. It prevents failure names from becoming ontology. | Treat a failure cue as repair-entry material until described holon, selected structure, object under stress, and subject pattern are recovered. | A warning name, source expression, or domain habit is not an architecture kind. |
| Parnas information hiding (`https://doi.org/10.1145/361598.361623`), MOSA and open-systems practice (`https://www.cto.mil/sea/mosa/`), product-line and platform practice, and the current `C.31` source line | Strong architecture lineage for stable boundaries, hidden variation, replacement policy, and interface conformance. | Repair weak-module and false-platform cues by restoring interface behavior, variation slots, substitution policy, conformance expectation, and bounded exceptions. | Module wording, platform promise, or published interface text does not establish modularity, substitutability, or architecture adequacy. |
| ISO 42010:2022 architecture-description practice (`https://www.iso.org/standard/74393.html`), plus `C.30.AD`, `C.30.ASV`, `E.17`, and `E.24.PUB` | Current standard and FPF line for distinguishing architecture, architecture description, view, viewpoint, concern, model kind, correspondence, and publication face. | Treat architecture-description artifacts and publication faces as description or publication material until selected-structure repair is recovered. | A description artifact or publication face is not architecture adequacy, evidence sufficiency, or project architecture decision. |
| Evolutionary architecture practice (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`), DORA loosely coupled teams, last updated 2025-10-20 (`https://dora.dev/capabilities/loosely-coupled-teams/`), DORA trunk-based development (`https://dora.dev/capabilities/trunk-based-development/`), and Team Topologies key concepts (`https://teamtopologies.com/key-concepts`) | Current practitioner line for changeability, small batches, independent change, dependency reduction, and fast flow. | Use change pain, coordination load, and flow bottlenecks as cues for selected-structure stress while keeping organization relations, local kinds, separate System-classification judgments, assignments, enactor relations, ordinary work or procedure organization, actual Work, independently typed influence sources, transformed-side architecture content, module-interface structures, and direct responsibility relations distinct. | Fast-flow evidence can guide architecture repair only after it is interpreted as stress on named selected structures; it neither makes an architecture act nor establishes a direct influence or responsibility relation. |
| `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`), design-space practice (`https://arxiv.org/abs/2407.18502`), architecture-spread research (`https://arxiv.org/abs/2402.19171`), and C.18 and C.19 open-ended search governance | Strong current line for hard trade-offs, dynamic candidate fronts, retained stepping stones, and preserving structurally different alternatives instead of hiding them behind one score. | Recover an adequate candidate palette and the preference's conditions for hidden-single-winner or static-optimum cases. Develop missing content where the intended comparison or decision needs it. | A score, Pareto front, generated winner, retained stepping stone, or workshop favorite is not a selected architecture. |
| TRIZ ideality and laws of technical-system evolution, with `C.19.1` BLP | Older heuristic line for useful-function consolidation and removing unnecessary bearers, plus FPF scale-amenability discipline for general bearers. | Repair ideality and universal-module shortcuts by turning them into typed C.32 candidates. | Ideality, fewer parts, or one universal module is not architecture adequacy, scale adequacy, assurance, release, or project architecture decision. |
| Multi-objective NAS, hardware-aware co-design, scaling-law practice (`https://www.jmlr.org/papers/v20/18-598.html`, Sukthanker et al. v3 revised 2025-02-04 at `https://arxiv.org/abs/2402.18213`, Sinha et al. 2024 at `https://arxiv.org/abs/2404.12403`), and `C.19.1` BLP | Current ML architecture line makes functional graph search, resource constraints, hardware constraints, and scale-amenability visible as architecture-synthesis pressure. | Repair a feasibility or scale-advantage claim whose bearer, applicable scale window or affected characteristics remain unsupported. | A functional graph, neural architecture, benchmark result, or scale curve is not architecture adequacy, assurance, release, or project architecture decision. |
| MAAD submitted 2025-07-28 (`https://arxiv.org/abs/2507.21382`), LLM-assisted ADD submitted 2025-06-27 (`https://arxiv.org/abs/2506.22688`), and model-card or evaluation-drift practice | AI-assisted architecture work exposes evaluation-boundary, hallucination, drift and oversight questions that must be resolved for the intended reliance. | Treat generated outputs and model behavior records as source cues; recover source-side referent, selected structure, architecture-change kind, gain, loss, review boundary, and evidence-decay boundary. | A generated or model-bearing artifact does not carry an architecture-adequacy authority relation, evidence sufficiency, assurance, or gate passage. |

**Source-use boundary.** Each row supplies a bounded repair contribution. Recheck a dependent use when a source or application premise changes materially. Preserve independently supported observations and repairs; an unsupported source transfer can remain historical background.

### C.32.FAIL:12 - Relations

- **Builds on:** `C.32` for candidate palette repair; `C.32.CONWAY` for a synthesis frame or qualified pair connecting architecture influence with transformed-side architecture while keeping the changed referent, C.30 architecture relations or modal claims, direct influence occurrence, organization relations, local kinds, separate System-classification judgments, assignments, enactor relations, ordinary work or procedure organization, actual Work, direct responsibility relations, actual transformation, and any E.18.NET network distinct; `C.30` and `C.30.AD` for architecture relation, claim, and description boundaries; `C.30.ASV` for architecture structural views; `C.31` for module and interface architecture; `C.32.MLAO` for cross-scope residual repairs; `C.29` for mathematical-lens use; `E.17` and `E.24.PUB` for publication-face boundaries; and `A.6.P`, `E.10`, and `E.10.ROLE` for source-expression and role-word recovery.
- **Coordinates with:** `A.6.F` when function and architecture-characteristic wording is mixed; `A.6.M` for module-interface repair; `C.19.1` for a general scale-amenable bearer or Method; A.2/C.3 for a local system-role kind and any separate System-classification judgment; A.2.1 for an assignment species and occurrence; A.13 for every precise performer's core, A.15.1 for independent actual-Work admission, and F.6 only for current precise assignment-bound attribution; and the exact enactor, coordination, or responsibility predicate, or A.6.RCD `missing-governor`, when that direct route is absent. Use `E.10.ROLE` only for unresolved claim-bearing *role* wording. Ordinary work or procedure organization may remain ordinary. For other current claims, use the applicable exits in §1; `C.27` additionally governs temporal adequacy, `E.18` transformation-flow structure, and `C.32.P2S` reopened carry-through.
- **Patterns for the next questions:** Use the applicable exits in §1 for the needed contribution, including evidence that can determine the repair action.
- **Boundary:** C.32.FAIL contains repair cues for architecture-synthesis failures. It does not decide final candidate selection, evidence sufficiency, assurance, gate passage, release, or an architecture decision.

### C.32.FAIL:End
