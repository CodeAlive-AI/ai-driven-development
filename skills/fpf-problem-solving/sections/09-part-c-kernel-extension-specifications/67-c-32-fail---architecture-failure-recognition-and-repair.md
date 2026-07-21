## C.32.FAIL - Architecture Failure Recognition and Repair

> **Type:** Architectural subpattern under C.32
> **Status:** Draft
> **Normativity:** Normative unless explicitly marked informative

### C.32.FAIL:1 - Problem frame

Use this pattern when a practitioner sees a recurring architecture-synthesis failure and needs to turn that warning into the smallest repair action over a named architecture object before evidence, assurance, selection, or decision claims are current.

Primary working reader: an architect or architecture-responsible practitioner who sees a warning sign during synthesis and needs the first architecture repair action, not a larger risk catalogue.

Typical entry cues:

```text
"This looks modular, but changes still cross hidden dependencies."
"The model is called a module, but the interface is weak."
"The platform promise hides exception growth."
"The search picked a winner, but the alternatives and losses disappeared."
"The graph looks convincing, but we cannot say which architecture object it repairs."
```

**First-minute use slice.** A team calls an ML model a module in a safety-relevant product architecture. Using C.32.FAIL, the practitioner does not add another warning name. The practitioner names the architecture object under stress: a candidate module-interface relation for the described product holon. The blocked overread is: model file equals stable module. The first repair action is to recover interface behavior, admissible-use conditions, change policy, and evidence-decay boundary before using the model as a module. If a safety assurance claim is current, the case escalates only after that architecture repair is named.

The primary `EntityOfConcern` is one repair cue for one architecture object under stress. The cue is a working repair aid, not a risk register, assurance case, selection result, release argument, or decision object.

What goes wrong if C.32.FAIL is missed: failure language degenerates into a warning bank. The team can say what looks suspicious, but it cannot say which architecture object must be repaired or which pattern governs the next claim.

What C.32.FAIL buys in practice: a practitioner can convert a vague failure signal into one typed repair action, keep the repair near the selected structure, and stop before nearby decision, release, or governance claims expand the case.

Ordinary working move: convert the symptom into four fields: architecture object under stress, blocked overread, first repair action, and stop or escalation condition.

Adoption test: after using C.32.FAIL, a reader can see four things in the cue: the architecture object under stress, the blocked overread, the first repair action, and the receiving pattern or stop condition.

Use another pattern when the current work is only lexical cleanup, evidence sufficiency, release, architecture description, MVPK publication face, comparison, selection, archive, front, publication of a selected set, local choice, or final architecture decision. Use C.32.FAIL only when the failure cue changes the first architecture repair action.

Common exits by claim kind:

- `C.30.P`, `A.6.F`, `A.6.M`, `C.31`, `C.32`, `C.32.MLAO`, and `C.32.CONWAY` for architecture or selected-structure repair.
- `A.19.CPM` for explicit comparison and `A.19.SelectorMechanism` for set-returning selection.
- `C.18` and `C.19` for archive, front, pool-treatment, or retained-stepping-stone claims.
- `A.10` for evidence, `B.3` for assurance, and `A.20` or `A.21` for gate or release claims.
- `C.30.AD` for architecture description and `E.17` or `E.24.PUB` for publication faces.
- `G.5` for publication of a selected set, `C.11` for local choice, and `C.32.PAD` for project decision.

The first useful output is `ArchitectureRepairCue@Project`. It is the project working record for one repair action. It names the stressed architecture object and first repair; it is not a failure ontology, risk register, assurance case, release argument, selection result, or decision:

```text
ArchitectureRepairCue@Project:
  symptom:
  describedHolonRef:
  boundedContextRef:
  architectureObjectUnderStress:
  selectedStructureRef?:
  sourceCueRef?:
  blockedOverread:
  firstGoverningPatternRef:
  repairAction:
  sourceReturnCondition:
  stopCondition:
  escalationIfCurrent:
```

### C.32.FAIL:2 - Problem

Architecture synthesis often fails before formal evidence or decision work starts. The defect is not only that a word is vague. The practical defect is that the architecture object under stress is missing or misread.

Most first-contact failures cluster into a few repair-entry families:

* a proposed bearer, module, platform, or universal substrate hides interface behavior, variation pressure, function bearing, evidence burden, or new coupling;
* a proxy result, generated artifact, architecture description, graph, dashboard, front member, or workshop favorite is used before the selected structures, losses, and receiving pattern are named;
* one structure, function, role, responsibility, control relation, evidence relation, or method step is improved while the synthesis frame loses the architecture characteristics and other structures that made the trade-off real;
* a current candidate is treated as a durable optimum, or ideality pressure deletes a bearer without naming the function still carried, the lost structure, and the new burden;
* a changing holon's architecture and the changed holon's architecture collapse into one claim instead of opening transformer and transformed architecture correspondence repair.

These cues are useful only when each one is converted into a repair shape: symptom, architecture object under stress, first repair action, and stop or receiving pattern.

```text
symptom -> architecture object under stress -> blocked overread -> first governing pattern -> repair action -> stop or escalation
```

C.32.FAIL governs that conversion. It does not mint a local ontology of failure kinds.

### C.32.FAIL:3 - Forces

| Force | Tension |
|---|---|
| Fast recognition | Practitioners need short warning cues while the repair object is still unclear. |
| Object recovery | Source expressions and domain habits can hide the architecture object under stress. |
| Repair locality | The first useful repair action should change architecture handling, not open a broad audit. |
| Neighboring claim patterns | Evidence, assurance, gate, release, selection, and decision claims may be nearby but governed elsewhere. |
| Cue inflation | Warning rows can multiply without improving repair unless admission requires a concrete repair action. |

### C.32.FAIL:4 - Solution

Convert the warning cue into an `ArchitectureRepairCue@Project`. Work in six steps:

1. State the symptom in ordinary practitioner language.
2. Name the described holon, bounded context, and architecture object under stress.
3. State the blocked overread that would lead the team astray.
4. Name the first governing pattern for the architecture object or lens relation.
5. Propose the smallest repair action that changes architecture handling.
6. State where to stop, or which neighboring pattern governs the next claim if another claim is already current.

Core repair families for first-draft use:

| Repair family | Symptom | Architecture object under stress | First repair action | Stop or receiving pattern |
|---|---|---|---|---|
| Weak module-interface | A source-side bearer is called a module because it has a convenient boundary. | Candidate module-interface relation and selected structure boundary. | Recover interface behavior, admissible-use boundary, change policy, and interface-conformance witness. | Stop at repaired interface cue; module-interface structure claims belong to `A.6.M`, `C.30.ASV`, or `C.31` when current. |
| False platform | A reusable-structure promise hides variation pressure and local exceptions. | Variation structure, substitution policy, evidence scope, and exception boundary. | Recover variation slots, substitution rules, substitution-conformance checks, and exception-growth trigger. | Cross-scope residual work belongs to `C.32.MLAO` when current. |
| Hidden single winner | A comparison or generation result is treated as selected architecture. | Candidate palette and retained alternatives. | Rebuild the C.32 palette with candidate gain, loss, preserved structure, hidden structure, and source-return condition. | Explicit comparison belongs to `A.19.CPM`, set-returning selection to `A.19.SelectorMechanism`, publication of a selected set to `G.5`, local choice to `C.11`, and project architecture decision to `C.32.PAD`. |
| Proxy result or description as authority | A score, graph, residual vector, generated output, architecture-description artifact, or MVPK publication face is used to accept or prefer an architecture candidate before the selected structure and receiving pattern are named. | Candidate architecture claim and selected-structure relation hidden behind the proxy, description, or visible result. | Recover the selected structure, source-side referent, view relation, or lens-output relation first. Use `C.29` for lens output, `C.30.ASV` or `C.30.AD` for view or description use, `A.19.CPM` for comparison, `C.11` for local choice, `A.19.SelectorMechanism` for set-returning selection, and `G.5` for publication of a selected set. | Stop when the visible work product only orients repair; evidence claims belong to `A.10` and assurance claims belong to `B.3`. |
| Coordination cost displaced by responsibility change | A team, work, or responsibility change improves local flow while pushing coordination into module interfaces, shared test, evidence, approval, or deployment structures. | Correspondence among role-enactor structure, work structure, coordination relation, module-interface structure, and evidence or deployment structure. | Recover the shifted coordination cost, then decide whether the repair belongs to `C.32.CONWAY`, `A.6.M`, `C.32.MLAO`, or a work and role pattern. | Role and work claims belong to the A.15 family; use architecture only for selected structures and architecture characteristics. |
| Temporal or control coupling | Named parts need brittle timing or control coordination. | Temporal relation, control relation, and affected work or evidence relation. | Recover the timing or control constraint and ask whether a candidate architecture change affects the selected structure. | Temporal adequacy claims belong to `C.27`, control or mechanism placement claims belong to the governing mechanism pattern, and flow-structure claims belong to `E.18` when current. |
| Evidence jump | The team asks for more evidence before naming the architecture repair. | Architecture object whose evidence relation may be stale, misplaced, or bearer-dependent. | Name the architecture repair first, then record the A.10 evidence relation, source-currentness relation, bearer, scope, and decision-use boundary. | Evidence relations belong to `A.10`, assurance to `B.3`, and gate or release claims to `A.20` or `A.21` when those patterns are current. |
| Generated output as authority | A generated architecture-looking output is treated as carrying an authority relation for architecture adequacy. | Source cue, generated description, candidate selected structure, and evaluation boundary. | Treat the output as a source cue; recover source-side referent, selected structure, architecture-change kind, gain, loss, and human review boundary. | Candidate generation belongs to `C.32`; generated-description use belongs to `C.30.AD`; publication-face use belongs to `E.17` or `E.24.PUB` when current. |
| Single-structure synthesis | One selected structure is improved and called the architecture synthesis. | Synthesis structure map and architecture characteristic bundle. | Return to C.32; name the other selected structures that must be coordinated and the architecture characteristics that make the trade-off real. | Stop at repaired C.32 palette, or open `C.32.MLAO` if the failure crosses scopes. |
| User function as architecture characteristic | A user-visible function is treated as the architecture quality being optimized. | Functional demand, architecture characteristic, and quality bundle boundary. | Recover the function through `A.6.F` or `C.30.ASV`; then name the architecture characteristic or `C.25` quality bundle separately. | Stop before comparison until function and characteristic occupy distinct fields. |
| Function with no feasible bearer | A function graph, workflow, use case, method step, or neural cell graph names a required function that no admitted bearer can perform under the current constraints. | Functional demand, candidate bearer set, module-interface relation, placement or deployment relation, resource access, control relation, and evidence burden. | Return to `C.32`; add or change bearer, split function, change placement or resource access, change control responsibility, reduce demand, or reject the candidate. | Stop before comparison, G.5 publication, assurance, or decision claims. |
| Static optimum | A front member or local winner is treated as durable optimum. | Evolution window, receiving pattern result, front or archive relation, and reopen trigger. | Add evolution window, source-return condition, and receiving pattern; keep C.18 and C.19 as retention or pool policy only. | Comparison belongs to `A.19.CPM`, set-returning selection to `A.19.SelectorMechanism`, local choice to `C.11`, publication of a selected set to `G.5`, and architecture decision to `C.32.PAD` when the decision claim is being made. |
| Ideality shortcut | Fewer bearers or fewer modules is treated as architecture improvement by itself. | Function-bearing allocation, selected structure count, and architecture characteristic bundle. | Recover the function-bearing transfer; name the removed or generalized bearer, the functions still carried, the new burden, and lost structure. | Return to `C.32`; use `C.31`, `A.6.F`, `A.6.M`, and `C.19.1` when their claims are current. |
| Universal bearer as adequacy shortcut | A universal module or general substrate is treated as architecture adequacy or scale adequacy by itself. | Scale-amenability claim, module-interface relation, evidence burden, control burden, and safety or admissibility boundary. | Treat universality as a candidate; require BLP scale window or waiver when scale advantage is claimed and record coupling, evidence, control, and source-return effects. | Stop before G.5 publication, assurance, release, or decision claims unless receiving patterns are current. |
| Transformer and transformed architecture mismatch | The architecture of a holon that changes another holon is collapsed with the changed holon's architecture, or the changed architecture is desired without a feasible changing holon. | Transformer-side selected structures, transformed-side selected structures, and the changing relation. | Open `C.32.CONWAY`; recover the changing relation through `A.3.4`, `E.18`, work, or method patterns; generate candidate repairs that change the transformer side, the transformed side, both sides, or a bounded mismatch. | Use `A.6.M` only for module-interface repair and `C.29` only when structural similarity is claimed. |

Admit a new repair family only when its row tells the practitioner what to repair first. A suspicious name alone is not enough; the row must name the architecture object under stress, the first repair action, and the stop or receiving pattern.

**Stop condition.** Stop after the repair action, receiving pattern, and source-return condition are named. Do not grow the cue into a risk register, evidence case, release argument, or final architecture choice.

**Lowering condition.** Keep the row as a C.32.FAIL repair cue only while the symptom, described holon, architecture object under stress, blocked overread, first governing pattern, repair action, stop condition, and escalation condition remain current. Lower the row to an observation when the architecture object is unknown, the repair action is missing, the first governing pattern is not named, or the symptom belongs only to evidence, assurance, release, description, publication, comparison, selection, choice, or decision work. Retire the cue when the repair action has been applied or the stressed architecture object is no longer current. Return to `A.6.P` or `E.10` when the case is only source-expression recovery, to `C.32` when candidate repair is current, to `C.32.MLAO` or `C.32.CONWAY` when their residual or correspondence repair is current, and to the named receiving pattern when a stronger downstream claim is current.

### C.32.FAIL:5 - Worked Repair Cases

**Tell.** C.32.FAIL is a repair-entry pattern. It takes a recognizable warning cue and returns one typed repair action over a selected architecture object. It is useful only when the repair action changes architecture handling.

**Show-A - Safety-relevant model-as-module.** A model file is being treated as a module in a product architecture. The repair cue names the candidate module-interface relation, blocks the file-equals-module overread, and recovers interface behavior, admissible-use conditions, change policy, and evidence-decay boundary. Safety assurance follows only through its governing pattern.

**Show-B - Product-family platform with exception growth.** A platform promise reduces local delivery effort but grows evidence exceptions at the product-family scope. The repair cue names variation structure, substitution policy, and evidence scope as the architecture objects under stress. The first repair action is not to declare the platform adequate; it is to repair variation slots and bounded-exception rules, then open `C.32.MLAO` residual comparison if cross-scope burden is current.

**Show-C - Responsibility change shifts coordination cost.** A stream-aligned team improves local delivery flow, but release testing and evidence responsibility remain shared. The repair cue names the shifted coordination cost, keeps role-enactor and work structures distinct from module-interface and evidence structures, and asks whether the candidate should change transformer-side work, transformed-side module interfaces, evidence scope, or all three.

**Show-D - Generated architecture candidate.** An agent system produces a high-scoring blueprint. The repair cue treats the blueprint as a source cue, recovers the selected-structure changes encoded in it, names preserved and lost structure, and rebuilds the candidate palette before G.5 publication of a selected set or decision.

**Show-E - Built-asset maintenance dashboard.** A facility maintenance dashboard shows a dependency graph and freshness scores. The repair cue keeps the graph as a lens output, recovers the actual selected structures under stress in maintenance work and asset interfaces, and keeps timing or evidence claims with their governing patterns.

**Show-F - Function with no feasible bearer.** A searched AI workflow adds a verification function after model output, but the edge device has no resource margin and the cloud placement violates latency. The repair cue names the function-bearing gap, then returns to C.32: add a local bearer, split verification into local and cloud steps, change deployment placement, reduce the demand, or reject the candidate for the current evolution window.

### C.32.FAIL:6 - Repair-Entry Failure Modes

| Failure mode | C.32.FAIL repair action |
|---|---|
| **Warning name without repair action** | A warning row is useful only when it names the architecture object under stress and the first repair action. Otherwise keep the warning name out of the pattern. |
| **Architecture repair skipped for evidence or assurance** | Evidence may be needed, but the first repair action is still to name the architecture object under stress and the candidate change. Evidence and assurance claims belong to their governing patterns after that. |
| **Decision jump** | A repair cue does not select an architecture. Rebuild the candidate palette or residual frame before G.5 publication, choice, or decision work. |
| **Source expression substitutes for architecture object** | A source term, method word, benchmark result, or generated output starts recovery; it does not govern the architecture claim until selected structures and characteristics are named. |
| **Software-source overfit** | Software and AI sources can supply strong repair actions, but the action must be translated to selected structures of the described holon. |
| **Description carrier substitutes for repair** | Architecture descriptions and publication faces can make the problem visible, but they do not repair architecture unless the selected architecture object under stress and repair action are named. |
| **Function and characteristic collapse** | User functions and architecture characteristics must occupy distinct fields before comparison or repair. |
| **Function without bearer** | A functional architecture is only a candidate when admissible bearers are recoverable under current constraints. |
| **Ideality used as deletion admissibility** | Ideal final result wording is a generation pressure; deleting a bearer is admissible only after function bearing, lost structure, new burden, and architecture characteristics are named. |
| **Universal bearer admitted by name** | A universal module or general substrate must be treated as a candidate bearer under BLP scale-window discipline and declared architecture-characteristic criteria rows. |
| **Conway wording without correspondence repair** | Conway, mirroring, or inverse-Conway wording is useful only when it opens `C.32.CONWAY` and names the changing relation, selected structures on both sides, affected architecture characteristics, gains, losses, and receiving pattern. |

### C.32.FAIL:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-C32.FAIL-1` | The cue states a recognizable symptom in practitioner language. | Keeps the pattern usable at first contact. |
| `CC-C32.FAIL-2` | The described holon, bounded context, and architecture object under stress are named. | Prevents source wording from replacing object recovery. |
| `CC-C32.FAIL-3` | The blocked overread is stated in one sentence. | Makes the failure precise enough to repair. |
| `CC-C32.FAIL-4` | The first governing pattern is named. | Keeps architecture, lens, work, evidence, assurance, and decision claims distinct. |
| `CC-C32.FAIL-5` | The repair action changes architecture handling. | Prevents warning-only rows. |
| `CC-C32.FAIL-6` | The stop condition or receiving pattern is named. | Keeps the cue lightweight and composable. |
| `CC-C32.FAIL-7` | New cue rows name the architecture object, first repair action, and stop or receiving pattern. | Prevents warning-bank inflation. |

### C.32.FAIL:8 - Common repair cues

| Anti-pattern | Symptom | Repair |
|---|---|---|
| `WarningNameOnly` | A memorable warning name does not change the next repair action. | Add the architecture object, blocked overread, governing pattern, and repair action, or remove the row. |
| `EverythingIsFailureCue` | Any architecture worry is admitted as a C.32.FAIL cue. | Admit only recurring failures that change the first architecture repair action. |
| `AuditPromptAsPattern` | The row says to measure, review, or audit. | Demote it unless it names the architecture object and repair action first. |
| `EvidenceAsRepair` | More evidence is treated as the repair. | Name the architecture repair first; evidence may follow under its own pattern. |
| `DecisionInsideRepairCue` | The cue says which architecture to choose. | Local choice belongs to `C.11`; project architecture decision belongs to `C.32.PAD` after the candidate repair is available. |
| `DescriptionCarrierAsRepair` | A diagram, report, dashboard, or publication face is treated as the repair. | Description use belongs to `C.30.AD`; publication-face use belongs to `E.17` or `E.24.PUB`; dashboard, report, or generated carrier use must stay under source-use or publication governance. Keep C.32.FAIL only if an architecture object under stress and repair action are named. |
| `FunctionAsQuality` | A function such as teach, compute, certify, or regulate is treated as the architecture characteristic. | Recover the function under `A.6.F` and name the separate architecture characteristic or quality bundle. |
| `FunctionalGraphNoBearer` | A functional graph, workflow, or method structure names a required function that no admitted bearer can perform under the module, placement, resource, control, or evidence constraints declared for the case. | Return to C.32; add or change bearer, split function, change placement or resource access, change control responsibility, reduce demand, or reject the candidate. |
| `IdealityAsAdequacyShortcut` | The phrase ideal architecture, no modules, or fewer parts is used as architecture adequacy by itself. | Convert it into a C.32 candidate and name function bearing, lost structure, new burden, architecture characteristics, and receiving pattern. |
| `UniversalBearerAsAdequacyClaim` | A universal module, general substrate, or existing resource is used as better architecture because it can carry more functions. | Use `C.19.1` only when scale advantage is claimed; otherwise recover module-interface, coupling, evidence, control, safety, admissibility, and source-return effects before explicit comparison belongs to `A.19.CPM`, local choice to `C.11`, set-returning selection to `A.19.SelectorMechanism`, or publication of a selected set to `G.5`. |
| `ConwayNameAsRepair` | A warning row says Conway, mirroring, or inverse Conway but gives no architecture repair. | Open `C.32.CONWAY`; name the transformer and transformed holons, selected structures on both sides, changing relation, affected characteristics, candidate repair, loss, and stop condition. |

### C.32.FAIL:9 - Consequences

| Positive consequence | Cost or trade-off |
|---|---|
| Failure recognition produces repair action. | Many tempting warning rows are rejected. |
| Repair stays near the architecture object under stress. | The team may need to postpone evidence, assurance, or decision work. |
| Source expressions can be used as cues without carrying ontology. | Each cue must recover the described holon and selected structure. |
| C.32 candidate repair stays separate from final selection. | Publication of a selected set or choice requires the receiving pattern. |
| Generated or tool-derived architecture material can widen discovery. | Generated material must still recover source-side referent, selected structures, architecture-change kind, gain, loss, and human review boundary before candidate use. |

### C.32.FAIL:10 - Rationale

C.32 needs a failure-recognition subpattern because candidate architecture work repeatedly breaks at the repair-entry point. The useful work is not to collect more warnings. The useful work is to recover the architecture object under stress and make the next repair action reviewable.

The pattern stays intentionally small. It does not establish failure, make a score-based risk finding, select a candidate, or authorize a release. It gives practitioners a disciplined way to go from "something is wrong here" to "this architecture object needs this repair, and this neighboring pattern governs the next claim if it is current."

### C.32.FAIL:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.FAIL. Each row states which field, repair row, boundary, or receiving-pattern exit the draft sets or revises from the source. Do not keep a citation when the draft uses it only as decoration.

| Source to inspect | Why this source is load-bearing here | Transfer into C.32.FAIL | Concrete C.32.FAIL mutation | Blocked overread |
|---|---|---|---|---|
| Current FPF architecture kernel: `C.30`, `C.30.AD`, `C.30.ASV`, `C.31`, `C.32`, `C.32.MLAO`, plus `A.6.P` and `E.10` | Current local law for architecture objects, source-expression recovery, and candidate repair. It prevents failure names from becoming ontology. | Treat a failure cue as repair-entry material until described holon, selected structure, object under stress, and governing pattern are recovered. | `ArchitectureRepairCue@Project` now requires `architectureObjectUnderStress`, `blockedOverread`, `firstGoverningPatternRef`, `repairAction`, and `sourceReturnCondition`. | A warning name, source expression, or domain habit is not an architecture kind. |
| Parnas information hiding (`https://doi.org/10.1145/361598.361623`), MOSA and open-systems practice (`https://www.cto.mil/sea/mosa/`), product-line and platform practice, and the current `C.31` source line | Strong architecture lineage for stable boundaries, hidden variation, replacement policy, and interface conformance. | Repair weak-module and false-platform cues by restoring interface behavior, variation slots, substitution policy, conformance expectation, and bounded exceptions. | Repair table rows for `Weak module-interface` and `False platform`; worked cases A and B. | Module wording, platform promise, or published interface text does not establish modularity, substitutability, or architecture adequacy. |
| ISO 42010:2022 architecture-description practice (`https://www.iso.org/standard/74393.html`), plus `C.30.AD`, `C.30.ASV`, `E.17`, and `E.24.PUB` | Current standard and FPF line for distinguishing architecture, architecture description, view, viewpoint, concern, model kind, correspondence, and publication face. | Treat architecture-description artifacts and publication faces as description or publication material until selected-structure repair is recovered. | Repair row `Proxy result or description as authority`; fields for `sourceCueRef?` and `firstGoverningPatternRef`; worked cases D and E. | A description artifact or publication face is not architecture adequacy, evidence sufficiency, or project architecture decision. |
| Evolutionary architecture practice (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`), DORA loosely coupled teams, last updated 2025-10-20 (`https://dora.dev/capabilities/loosely-coupled-teams/`), DORA trunk-based development (`https://dora.dev/capabilities/trunk-based-development/`), and Team Topologies key concepts (`https://teamtopologies.com/key-concepts`) | Current practitioner line for changeability, small batches, independent change, dependency reduction, and fast flow. | Use change pain, coordination load, and flow bottlenecks as cues for selected-structure stress while keeping role, work, transformer-side, and module-interface structures distinct. | Repair rows `Coordination cost displaced by responsibility change`, `Temporal or control coupling`, and `Transformer and transformed architecture mismatch`; field `sourceReturnCondition`; stop rule before decision work. | Fast-flow evidence can guide architecture repair only after it is interpreted as stress on named selected structures. |
| `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`), design-space practice (`https://arxiv.org/abs/2407.18502`), architecture-spread research (`https://arxiv.org/abs/2402.19171`), and C.18 and C.19 open-ended search governance | Strong current line for hard trade-offs, dynamic candidate fronts, retained stepping stones, and preserving structurally different alternatives instead of hiding them behind one score. | Repair hidden-single-winner and static-optimum cases by rebuilding candidate palette content before publication of a selected set, local choice, or architecture decision. | Repair rows `Hidden single winner` and `Static optimum`; fields for preserved and lost structure through the C.32 palette; receiving exits to `A.19.CPM`, `A.19.SelectorMechanism`, `G.5`, `C.18`, `C.19`, `C.11`, and `C.32.PAD`. | A score, Pareto front, generated winner, retained stepping stone, or workshop favorite is not a selected architecture. |
| TRIZ ideality and laws of technical-system evolution, with `C.19.1` BLP | Older heuristic line for useful-function consolidation and removing unnecessary bearers, plus FPF scale-amenability discipline for general bearers. | Repair ideality and universal-module shortcuts by turning them into typed C.32 candidates. | Repair rows `Ideality shortcut` and `Universal bearer as adequacy shortcut`; anti-pattern rows `IdealityAsAdequacyShortcut` and `UniversalBearerAsAdequacyClaim`. | Ideality, fewer parts, or one universal module is not architecture adequacy, scale adequacy, assurance, release, or project architecture decision. |
| Multi-objective NAS, hardware-aware co-design, scaling-law practice (`https://www.jmlr.org/papers/v20/18-598.html`, Sukthanker et al. v3 revised 2025-02-04 at `https://arxiv.org/abs/2402.18213`, Sinha et al. 2024 at `https://arxiv.org/abs/2404.12403`), and `C.19.1` BLP | Current ML architecture line makes functional graph search, resource constraints, hardware constraints, and scale-amenability visible as architecture-synthesis pressure. | Repair cases where a functional architecture or universal bearer is admitted without feasible bearers, scale window, or affected characteristics. | Repair row `Function with no feasible bearer`; anti-pattern row `FunctionalGraphNoBearer`; worked Show-F. | A functional graph, neural architecture, benchmark result, or scale curve is not architecture adequacy, assurance, release, or project architecture decision. |
| MAAD submitted 2025-07-28 (`https://arxiv.org/abs/2507.21382`), LLM-assisted ADD submitted 2025-06-27 (`https://arxiv.org/abs/2506.22688`), and model-card or evaluation-drift practice | Current AI-assisted architecture work makes generated alternatives common, while also making evaluation boundary, hallucination, drift, and human oversight concerns that must be declared. | Treat generated outputs and model behavior records as source cues; recover source-side referent, selected structure, architecture-change kind, gain, loss, review boundary, and evidence-decay boundary. | Repair rows `Weak module-interface`, `Evidence jump`, and `Generated output as authority`; worked cases A and D. | A generated or model-bearing artifact does not carry an architecture-adequacy authority relation, evidence sufficiency, assurance, or gate passage. |

**Source-currentness boundary.** Use each source row only for the repair field, repair row, boundary, or receiving-pattern exit named in that row. Recheck the row when a cited standard, book edition, research result, DORA or Team Topologies page, model-practice source, FPF receiving pattern, described holon, selected structure, or source cue changes. If the source no longer supports the repair, lower it to background lineage and keep the cue only when the architecture object under stress, blocked overread, repair action, stop condition, and receiving pattern remain recoverable.

### C.32.FAIL:12 - Relations

- **Builds on:** `C.32` for candidate palette repair, `C.32.CONWAY` for transformer and transformed architecture correspondence repair, `C.30` and `C.30.AD` for architecture description boundaries, `C.30.ASV` for architecture structural views, `C.31` for module and interface architecture, `C.32.MLAO` for cross-scope residual repairs, `C.29` for mathematical-lens use, `E.17` and `E.24.PUB` for publication-face boundaries, `A.6.P` and `E.10` for source-expression and relation recovery.
- **Coordinates with:** `A.6.F` when function and architecture-characteristic wording is mixed, `A.6.M` when module-interface repair is current, `C.19.1` when a general scale-amenable bearer or method is preferred, the A.15 family when role or work structure is current, `A.10` and `B.3` when evidence or assurance claims are current, `A.20` and `A.21` when gate or release claims are current, `C.18` and `C.19` for archive, front, pool-treatment, or stepping-stone claims, `C.27` when temporal adequacy is current, `E.18` when transformation-flow structure is current, `C.32.P2S` when the failure reopens problem-to-structure carry-through, `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `G.5` for publication of a selected set, `C.11` for local choice, and `C.32.PAD` for project architecture-decision claims.
- **Receiving patterns after the repair cue:** `A.10` for evidence claims, `B.3` for assurance claims, `A.20` or `A.21` for gate or release claims when those claims are being made, `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `G.5` for publication of a selected set, `C.11` for local choice, and `C.32.PAD` for project architecture decisions, only after the architecture repair cue has named the object under stress and the repair action.
- **Boundary:** C.32.FAIL governs repair cues for architecture-synthesis failures. It does not govern final candidate selection, evidence sufficiency, assurance, gate passage, release claims, or architecture decision.

### C.32.FAIL:13 - Footer marker

`C.32.FAIL` governs conversion of a recognizable architecture-synthesis failure into one repair action over one architecture object under stress.

### C.32.FAIL:End

