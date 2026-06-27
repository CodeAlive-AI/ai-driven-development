## C.32.P2S - Problem-to-Structure Architecturing Transformation Flow

> **Type:** Architectural process pattern under C.32
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.32.P2S:1 - Problem frame

Use this pattern when an architect or architecture-responsible practitioner starts from architecture-relevant problem pressure that needs to stay connected through selected structures, candidate synthesis, project architecture decision, realization work, actual-structure feedback, and the next owner-specific action.

The common first moment is practical: a required function has no recoverable bearer; an architecture characteristic is failing; a cross-scope residual survives local repair; a modularity, reuse, interface, scale, or description-loss problem blocks action; a transformer holon cannot yet produce the desired transformed holon; or operation shows that expected structures and actual structures diverge.

The first useful output is `ProblemToStructureArchitecturingFlowCard@Project`. The card is a local project record of one architecturing flow. It is not a new `U` kind, not an architecture claim, not an architecture decision, not a work plan, not an eval result, and not a publication format. It keeps the connected flow reviewable while each local object remains governed by its owner pattern.

For the first pass, fill only the fields that prevent the next wrong move: described holon, bounded context, problem pressure, first governing owner, one unknown or selected structure slot, and neighboring owner for the next claim. Add decision, work, eval, publication, and feedback refs only when the flow reaches the owner pattern that governs them.

```text
ProblemToStructureArchitecturingFlowCard@Project:
  flowId:
  describedHolonRef:
  boundedContextRef:
  architectingHolonOrRoleRef?:
  firstGoverningOwnerRef:
  problemPressure:
    pressureKind:
    sourceSignalRefs?:
    architectureConcernRefs?:
    currentStopOrReturnReason?:
  architectureContent:
    candidateStructureKindRefs:
    selectedStructureRefs?:
    expectedStructureRefs?:
    actualStructureRefs?:
    architectureCharacteristicRefs:
    architectureCharacteristicCriteriaSetRef?:
    qBundleRefs?:
    candidateSynthesisRef?:
  structuralInformation:
    unknownStructure:
    selectedStructure:
    expectedStructure:
    actualStructure:
    capturedInDescriptionsOrDecisions:
    handedToMethodsOrWork:
    latentOrHiddenStructure:
    lostStructure:
    sourceReturnCondition:
  decisionAndWorkDocking:
    candidateSetOrPaletteRef?:
    selectedSetRef?:
    architectureDecisionRef?:
    adrProjectionRef?:
    methodDescriptionRefs?:
    workPlanRefs?:
    readinessRefs?:
    performedWorkRefs?:
  transformerTransformed?:
    changingRelationRef:
    transformerHolonRef:
    transformedHolonRef:
    transformerSelectedStructureRefs:
    transformedSelectedStructureRefs:
    correspondenceFrameRef:
  feedback:
    evalProgramRefs?:
    evalResultRefs?:
    measurementRefs?:
    operationOrUseObservationRefs?:
    functionalCharacteristicImplications?:
    freshnessOrDecaySignalRefs?:
    ownerSpecificReturnOrRepair:
      c32NextSynthesisExit?
      c32PadOrAdaDecisionRepairOrSupersessionExit?
      e23ImprovementCycleRef?
      g11CurrentnessRefreshRef?
      e18TransformationFlowRefreshRef?
      c18C19ArchiveFrontPoolUpdateRef?
      c30DescriptionOrViewSourceReturnRef?
  neighboringOwnerForNextClaim:
```

Not this pattern when the current work is only a problem card, only a grounded architecture claim, only a structural view, only a candidate palette, only a project architecture decision, only an ADR-like publication, only work planning, only performed work, only measurement, only a mathematical lens, or only `G.11` currentness, freshness, telemetry, edition, or decay orchestration. Use the owner named in `Relations` for that narrower claim.

### C.32.P2S:2 - Problem

FPF has precise owners for problem records, grounded architecture, structural views, candidate palettes, architecture characteristics, eval programs, decisions, ADR-like projections, method and work records, measurements, mathematical lenses, improvement loops, and currentness or decay orchestration. A practitioner still needs one readable pattern for the architecture work that connects them.

Without C.32.P2S, architecture work can fail in two opposite ways.

First, the flow collapses into a description or decision artifact: a diagram, view set, ADR, memo, dashboard, score, or publication record is treated as if it carried the architecture, the decision, and the realized structure. The project then loses the distinction between selected structure, description, decision, method expectation, performed work, and actual structure.

Second, the flow disappears into relation rows: every local owner is correct, but no pattern tells the architect how to move from pressure and structural uncertainty to candidate structures, selection, realization, feedback, and the next owner-specific action. The user can name patterns but cannot carry the architecture problem through work.

### C.32.P2S:3 - Forces

| Force | Tension |
|---|---|
| Structure-first architecture | Architecture is selected structures of a described holon in a bounded context; the flow is not reducible to documents, labels, stages, or tools. |
| Structural uncertainty | Architecturing often starts before structure kinds, bearers, interfaces, allocations, or variation points are known. |
| Characteristic trade-off | Architecture characteristics compete; optimizing one can damage another or hide Goodhart pressure behind a metric. |
| Candidate plurality | Useful architecture work keeps structurally different alternatives alive until a comparison, selected-set, local choice, or architecture decision pattern is current. |
| Realization gap | Selected or expected structures become actual structures only through domain work over a transformed holon. |
| Transformer constraint | The holon that changes another holon has its own work, method, role, tool, communication, evidence, and placement structures that can enable or block the desired transformed architecture. |
| Description loss | Views, descriptions, decision records, method descriptions, and eval reports capture only part of the structural content needed for later use. |
| Evolution and feedback | Operation, use, telemetry, inspection, eval, decay, and new sources can return the work to the owner that governs the next claim: `C.32` synthesis, `C.32.PAD` or `C.32.ADA` repair or supersession, `E.23` improvement, `G.11` currentness refresh, `E.18` transformation-flow slice-local refresh, `C.18` or `C.19` archive, front, and pool update, or `C.30.AD` or `C.30.ASV` source-return for descriptions or views. |

### C.32.P2S:4 - Solution

Create or update one `ProblemToStructureArchitecturingFlowCard@Project` and move through the smallest useful spine below. Stop at the first owner that fully governs the current claim; continue the P2S card only while the connected architecture flow remains the current object needing review.

Use the analogy with `E.18.1` P2W narrowly. P2W carries accepted problem and principle material into method, plan, work, and telemetry. C.32.P2S carries architecture-relevant pressure and structural uncertainty into candidate structures, selected structures, project architecture decision, realization work, actual-structure feedback, and owner-specific next actions. The analogy ends when the current claim is method, work, telemetry, publication, or improvement-loop governance; then use the receiving owner pattern rather than stretching P2S into generic process management.

1. Recover the problem pressure or architecture concern. Name the pressure kind, source signals, affected holon, and the first owner. If the source is still only a problem-side signal, use `C.22.2` before P2S continues.
2. Recover the described holon, bounded context, candidate or selected structure kinds, selected structures when available, and architecture characteristics. Use `C.30` for the grounded architecture claim, `C.32.HCS` for starter characteristic heads, `C.32.ACS` for project criteria rows, and `C.25` when a composite quality family is current.
3. Represent future-structure uncertainty. State unknown structure kinds, unknown internal composition, candidate bearers, interfaces, allocations, variation points, constraints, expected structures, and source-return conditions. Record what is captured, handed off, latent, hidden, or lost.
4. Generate architecture ideas, principles, constraints, and candidate structure changes. Use source material as candidate-generation pressure only after the affected structure, characteristic, gain, loss, and receiving owner are recoverable.
5. Synthesize candidate architecture configurations and candidate sets through `C.32`. Keep function-bearing feasibility, constructive modules, placement, control, transformation-flow, work, role, information, evidence, scale, and other selected structures visible when they change the candidate.
6. Compare, retain, publish, or return alternatives through the governing set owner. Use `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.18` and `C.19` for archive, front, and pool policy, `G.5` for publication of a selected set, and `C.11` for a fixed local choice.
7. Make a project architecture decision through `C.32.PAD` when implementation commitment is current. The decision relation names the selected architecture option, affected structures, trade-off, accepted losses, method and work consequences, source-return, and owner-specific repair or supersession condition.
8. Publish descriptions, views, ADR-like records, or other records only as descriptions or publication forms of structures, decision relations, method expectations, source-return, and reader use. Use `C.30.AD`, `C.30.ASV`, `C.32.ADR`, `E.17`, and `E.24.PUB` as applicable.
9. Hand transformer roles the method descriptions, constraints, readiness expectations, work expectations, and source-return conditions needed to realize selected structures. Use `A.15`, `A.15.2`, and `A.15.5` for method, work-plan, and readiness claims.
10. Realize selected structures in the transformed holon through domain work. Use `A.15.1` for performed work and `A.3.4` when one bounded transformation claim is current. The P2S card records refs; it does not perform the work.
11. Observe, inspect, measure, and evaluate actual selected structures, architecture-characteristic results, and functional-characteristic or capability implications in operation or use. Ask whether the realized structures enable or block the functions and effects they were meant to bear, and ask what selected structure, accepted loss, counter-characteristic, or functional implication got worse when a visible metric improved. Do not turn functional demand into an architecture characteristic or an eval result into decision authority. Use `C.32.ACE` for eval programs and eval results, `C.16` for measurement, and `C.25` for Q-bundles. Use `E.23` when repeated improvement method is current, `G.11` when currentness, telemetry, edition, freshness, or decay orchestration is current, `E.18` for transformation-flow slice-local refresh, `C.18` or `C.19` for archive, front, and pool updates, `C.32.PAD` or `C.32.ADA` for decision repair or supersession, `C.32` for new synthesis, and `C.30.AD` or `C.30.ASV` for source-return tied to descriptions or views. Feed actual-structure divergence, eval results, functional implications, freshness loss, source-return, and new constraints into the owner-specific return or repair action.

When one holon changes another holon, add the transformer/transformed branch before candidate synthesis becomes narrow. Name the changing relation, the transformer holon, the transformed holon, and selected structures on both sides when they constrain the candidate set. Use `C.32.CONWAY` to frame candidate families: change transformer-side structures, change transformed-side structures, change both, or declare a bounded mismatch with source-return.

Stop conditions:

- stop at `C.22.2` when the signal is not yet a reviewable problem-side record;
- stop at `C.30` or `C.30.ASV` when the current need is only architecture claim or structural-view adequacy;
- stop at `C.32` when the next useful artifact is a candidate palette rather than a whole P2S carry-through record;
- stop at `C.32.PAD` when the project architecture decision is current;
- stop at the A.15 family when the current question is method, work planning, readiness, or performed work;
- stop at `C.16`, `C.25`, `C.29`, `C.32.ACE`, `E.23`, or `G.11` when the current claim is measurement, quality-bundle, mathematical-lens, eval, improvement, or `G.11` currentness refresh;
- return to P2S only when a later owner returns architecture pressure that changes candidate structures, expected structures, actual structures, selected structures, or source-return.

### C.32.P2S:5 - Archetypal Grounding

**Tell.** A capable architect does not merely "document the architecture." The architect transforms pressure into structure: first by finding which selected structures are missing or inadequate, then by constructing alternatives, deciding what will be pursued, enabling work that realizes the structures, and watching whether the actual holon has the intended architecture under operation.

**First-minute use slice.** A plant architect sees that expected throughput and actual throughput diverge after a layout change. The first P2S card pass names the production cell as described holon, the operating shift as bounded context, pressure kind `actualStructureDivergesFromExpectedStructure`, first owner `C.30`, unknown structure `material-flow bottleneck bearer`, selected structure candidate `buffer placement`, and neighboring owner `C.32`. The card does not yet add a PAD decision, work plan, or eval result; those refs appear only after their owners become current.

**Lens-use slice.** If the plant team builds a DSM or epiplexity-style lens over stations, buffers, and routing events, P2S records only the architecture use: which dependency or learnable structural content was preserved, which flow distinction was compressed away, which selected structures the lens can inform, and which source-return condition sends the claim back to `C.29`. The lens result is not architecture adequacy, an eval result, or a decision.

**Show A - built asset and technical system.** A clinic has rising instrument-turnaround delays and infection-control pressure. The first P2S move does not ask for a better diagram. It names the described holon, bounded context, candidate structure kinds, architecture characteristics, and uncertainty: room layout, sterile and contaminated flows, equipment modules, tray interface, maintenance work, throughput, contamination isolation, maintainability, and surge adaptability. Candidate synthesis compares a centralized autoclave bay, distributed sterilization modules, and a reusable tray-interface change. `C.32.PAD` decides a selected configuration, `C.30.AD` and `C.32.ADR` publish the decision and views, A.15-family records guide construction and operating work, and operation measures actual turnaround, contamination events, maintenance burden, and source-return triggers.

**Show B - organization and role/method holon.** An inspection practice catches ontological errors late. The described holon is a method and role arrangement, not a software module. Structure kinds include role boundaries, inspection steps, evidence handoffs, decision records, and live attention cues. Architecture characteristics include error containment, learnability, throughput, evidence reuse, and repair locality. Candidate synthesis compares a single checker role, a split intake and ontology-checking role, and a live-beat microstep method. The project architecture decision binds the selected role/method structure to method descriptions and readiness checks. Later inspection work and telemetry show whether errors are caught earlier or whether the method architecture needs repair.

**Show C - transformer and transformed co-synthesis.** A team wants a modular product architecture but its toolchain, team communication, release method, and evidence practice only support one tightly coupled build. P2S uses `C.32.CONWAY`: transformer-side structures and transformed-side product structures are both candidate variables. Candidate families include changing the product modules only, changing the team and toolchain only, changing both, or accepting a bounded mismatch while retaining source-return. The decision states which side changes now, what architecture characteristics are protected, what work realizes the change, and what operation or delivery feedback can return to the `C.32.CONWAY` correspondence frame or to decision repair.

### C.32.P2S:6 - Bias-Annotation

Use these rows as repair cues for source pressure, not as a catalogue of mistakes.

| Source pressure | Risk in P2S use | Repair |
|---|---|---|
| Description-first source | A view, model, diagram, ADR-like record, dashboard, or memo starts to carry architecture, decision, and work authority at once. | Recover selected structures and current use. Send description adequacy to `C.30.AD` or `C.30.ASV`, decision to `C.32.PAD`, projection to `C.32.ADR`, and work claims to A.15-family patterns. |
| Single-winner source | A score, workshop favorite, generated candidate, or apparent best alternative hides structurally different candidates. | Restore candidate plurality through `C.32`; keep archive, front, pool, selected-set, comparison, local-choice, or decision use with its owner. |
| Eval-shaped source | A metric, benchmark, source-side fitness-function term, eval result, or telemetry event is treated as the characteristic or the decision. | Recover characteristic, bearer, scale, eval program, measurement, and receiving use. Use `C.32.ACE`, `C.16`, `C.25`, and then the comparison, selected-set, local-choice, or decision owner. |
| Transformer-hidden source | Desired transformed-holon architecture is stated without asking whether the changing holon can produce it. | Open `C.32.CONWAY`; name changing relation, transformer, transformed holon, selected structures on both sides, affected characteristics, candidate changes, and bounded mismatch condition. |
| Work-shaped source | A schedule, task list, method recipe, or performed-work record is treated as the architecturing flow. | Keep work owners intact. P2S records method, readiness, work-plan, and performed-work refs only when they realize or evaluate selected structures. |

### C.32.P2S:7 - Conformance Checklist

| Check | Pass condition |
|---|---|
| `CC-C32P2S-1` | The card names described holon, bounded context, problem pressure, first owner, and at least one architecture-relevant structure or unknown-structure slot. |
| `CC-C32P2S-2` | The architecture claim, when made, is grounded through `C.30` over selected structures of the described holon; no description or publication record carries the architecture by itself. |
| `CC-C32P2S-3` | Architecture characteristics are separate from functional demands, measurements, eval programs, eval results, Q-bundles, comparison rules, and decisions. |
| `CC-C32P2S-4` | The structural-information lane records unknown, selected, expected, actual, captured, handed-off, latent or hidden, lost, and returned structure when those slots are live. |
| `CC-C32P2S-5` | Candidate synthesis exits to `C.32`, comparison and selection claims exit to their owners, and the P2S card does not choose a winner by score or prose preference. |
| `CC-C32P2S-6` | A project architecture decision, when current, exits to `C.32.PAD`; ADR-like publication exits to `C.32.ADR` and publication owners. |
| `CC-C32P2S-7` | Method, work-plan, readiness, and performed-work claims exit to A.15-family owners; the P2S card carries refs and expected structure effects. |
| `CC-C32P2S-8` | Measurement, Q-bundle, mathematical-lens, eval, improvement, `G.11` currentness refresh, and `E.18` transformation-flow slice-local refresh claims exit to `C.16`, `C.25`, `C.29`, `C.32.ACE`, `E.23`, `G.11`, or `E.18`. |
| `CC-C32P2S-9` | Transformer/transformed cases name the changing relation, both holons, selected structures on both sides when load-bearing, and the `C.32.CONWAY` correspondence frame. |
| `CC-C32P2S-10` | The pattern use covers at least one realized-structure feedback route that checks actual selected structures, architecture-characteristic results, and relevant functional-characteristic or capability implications through operation, use, inspection, measurement, eval result, telemetry, decay, source-return, or decision-repair trigger. |

### C.32.P2S:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Description stop | The project stops after producing a view set, diagram, ADR-like record, or architecture description even though no candidate structure, decision, realization, or feedback path is recoverable. | Return to step 2 or 5. Name selected or unknown structures, architecture characteristics, and the next owner: `C.30`, `C.30.ASV`, `C.32`, or `C.32.PAD`. |
| Relation index P2S | The P2S artifact lists neighboring patterns but does not tell the architect what to do from pressure to realized selected structures. | Write the positive action spine in the card: pressure, structures, uncertainty, candidates, retention or selection, decision, descriptions, method and work handoff, realized structures, feedback, and owner-specific return. |
| Eval-as-decision | An eval result, score, metric, telemetry event, or dashboard value selects the architecture. | Route the eval to `C.32.ACE`, measurement to `C.16`, and composite quality to `C.25`; ask what selected structure, accepted loss, counter-characteristic, or functional implication worsened; then use comparison, selected-set, local-choice, or `C.32.PAD` if selection or decision is current. |
| Hidden transformer | The transformed holon is designed as if the changing holon has no architecture. | Open the transformer/transformed branch and `C.32.CONWAY`; add candidate families that change transformer-side structures, transformed-side structures, both, or a bounded mismatch. |
| Lost structure left silent | The description, decision, method handoff, or eval report compresses away distinctions needed for later work. | Fill the structural-information lane: what is captured, handed off, latent or hidden, lost, and what source-return condition restores the stronger source. |
| Work owner takeover | P2S prose starts authorizing work or replacing method, readiness, work-plan, or performed-work records. | Keep P2S as architecture carry-through. Send method and work claims to A.15-family patterns and record only refs plus expected selected-structure effects. |

### C.32.P2S:9 - Consequences

The project gains one replayable architecturing flow from pressure to actual-structure feedback. Practitioners can see where the work currently stands and which owner pattern governs the next claim, without treating descriptions, decisions, eval results, or work records as interchangeable.

The cost is disciplined record work: the card preserves structural uncertainty, candidate plurality, accepted losses, handoffs, and source-return. If that cost is not justified because the question is already a narrow owner claim, use the owner directly and do not open P2S.

The pattern improves cross-holon reuse. The same spine works for systems, built assets, product families, organizations, roles, methods, epistemes, AI-agent setups, cultural practices, and other admitted holons because each case rebinds holon, structures, characteristics, transformer roles, eval modes, and receiving owners.

The pattern does not guarantee adequacy. It makes the architecturing flow inspectable. Candidate quality, decision adequacy, evidence, assurance, gate passage, release, measurement validity, and `G.11` currentness refresh still require their governing patterns.

### C.32.P2S:10 - Rationale

C.32.P2S belongs under C.32 because the central transformation is architecture synthesis: recovering problem pressure and structural uncertainty, generating candidate selected-structure changes, preserving alternatives, making decision-ready content, and returning actual-structure feedback to the next synthesis question.

It cannot be only a C.22 pattern because a problem card does not carry architecture synthesis, decision, realization, and feedback. It cannot be only a C.30 pattern because grounded architecture and structural-view adequacy do not themselves construct candidate palettes or govern downstream work. It cannot be only a C.32 pattern because the palette is only one stage of the larger architecturing flow. It cannot be only C.32.PAD or C.32.ADR because decisions and records do not create the candidate space and do not realize structures. It cannot be only A.15 or E.18.1 because method and work carry-through and P2W do not govern architecture candidate synthesis or selected-structure decision content.

The structural-information lane is selected now because otherwise P2S cannot explain what changes. Architecturing refines uncertainty about future structures into candidate, selected, expected, and actual structures, while descriptions, decisions, methods, work, and eval reports capture only part of that content. The practitioner records which structural content is captured by descriptions, decisions, method handoffs, work records, evals, and measurements; which structure remains latent, hidden, or lost; and which source-return condition returns the work to stronger structure inspection or a `C.29` lens use such as epiplexity, DSM, graph, coarse-graining, equivalence, or morphism.

### C.32.P2S:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.P2S. Software-system sources are used as source families and examples only; they do not narrow P2S to IT architecture.

| Source to inspect | Why this source is load-bearing here | Adopt, adapt, or reject disposition | Transfer into C.32.P2S | Blocked overread |
|---|---|---|---|---|
| ISO/IEC/IEEE 42010:2022 architecture-description standard (`https://www.iso.org/standard/74393.html`) | Current architecture-description practice separates architecture, description, concern, viewpoint, view, model kind, and correspondence. | Adopt the separation of architecture and description; adapt owner routing through `C.30.AD`, `C.30.ASV`, `C.32.ADR`, `E.17`, and `E.24.PUB`; reject any takeover of FPF holon and selected-structure ontology. | P2S step 8 and `CC-C32P2S-2` keep descriptions, views, and ADR-like records as captured structural content or publication forms with owner exits. | A description, view, diagram, or publication carrier is not the architecture, the project architecture decision, or performed work. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`) | Best current practitioner line for guided incremental change over declared architecture characteristics with feedback from eval practice. | Adopt guided evolutionary change and feedback; adapt source-side fitness-function practice into `C.32.ACE` eval programs and `C.16` measurement over `C.32.ACS` rows; reject treating eval success as a decision. | P2S step 11, the eval-shaped source row, and `CC-C32P2S-8` require architecture characteristics, eval exits, feedback, source-return, and owner-specific next-action triggers rather than one-time design settlement. | A source-side fitness-function name, metric, or passing eval result is not the architecture characteristic, decision, or proof of realized structure. |
| Richards and Ford, `Fundamentals of Software Architecture`, 2nd ed. (`https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/`) and Ford et al., `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Current practitioner sources for architecture characteristics, trade-offs, risk, coupling, cohesion, and difficult architecture decisions. | Adopt characteristic and trade-off discipline; adapt software-system examples to holons and selected structures; reject software-only module reduction. | P2S steps 2, 7, and 11 plus `CC-C32P2S-3` separate functional demand from architecture characteristics, require accepted-loss visibility, and feed realized functional implications back without confusing kinds. | A list of qualities, trade-off discussion, or rationale text is not candidate synthesis or decision adequacy by itself. |
| Architecture synthesis and multi-objective quality-attribute optimization, including Di Pompeo and Tucci 2023 (`https://arxiv.org/abs/2301.07516`) and ATRAF 2025 (`https://arxiv.org/abs/2505.00688`) | Current research line for competing quality attributes, multi-objective trade-offs, and architecture candidate evaluation. | Adopt candidate plurality and trade-off front inspection; adapt selection to FPF comparison, selected-set, local-choice, and decision owners; reject scalar or generated-winner authority. | P2S steps 5 and 6, the single-winner source row, and `CC-C32P2S-5` keep candidate plurality and route comparison, selection, selected-set publication, local choice, and decision to their owners after C.32 candidate synthesis. | A Pareto front, scalar score, optimization run, or generated winner does not select the architecture. |
| DSM, multiple-domain matrix, modularization, and dependency-structure practice; inherited C.32 source row for Jiang and Luo 2026 (`https://arxiv.org/abs/2604.28018`), epiplexity structural-information line (`https://arxiv.org/abs/2601.03220`), and `C.31.RSA` structure-accounting rows | Strong engineering-design line for inspecting dependency, coupling, modularity, learnable structural content, and structural loss; the inherited C.32 row also warns that functional priors and structural modularization objectives can diverge. | Adopt DSM, MDM, and epiplexity as structure-inspection lenses; adapt them through `C.29` lens refs and structural-information slots; reject matrix, cluster, compression, or epiplexity result as architecture adequacy. | P2S steps 3 and 5 and `CC-C32P2S-4` let the card cite DSM, MDM, graph, epiplexity, coarse-graining, equivalence, or morphism claims while recording preserved and lost structure. | A cluster, matrix, graph, compression, or epiplexity result is not architecture adequacy or a decision without recovered selected structures and owner exits. |
| Conway correspondence, mirroring, DORA loosely coupled teams (`https://dora.dev/capabilities/loosely-coupled-teams/`), and Team Topologies (`https://teamtopologies.com/key-concepts`) | Current socio-technical architecture practice shows that transformer structures can enable or block transformed-holon architecture and independent change. | Adopt co-synthesis of transformer and transformed structures; adapt through `C.32.CONWAY`; reject organization labels or communication diagrams as direct transformed-architecture claims. | P2S transformer branch, Show C, and `CC-C32P2S-9` require `C.32.CONWAY` when team, method, toolchain, communication, evidence, deployment, or work structures constrain the changed holon. | Organization labels, team diagrams, or communication patterns do not settle transformed-holon architecture; they become selected transformer structures only when mapped by value. |
| NASA Systems Engineering Handbook decision and trade-study practice (`https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf`), Michael Nygard's ADR practice (`https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions`), MADR 4.x (`https://adr.github.io/madr/`), and `C.32.ADR` source rows | Non-software domains often publish architecture choices as trade studies, engineering memos, review records, or certification rationale rather than Markdown ADR files; ADR practice supplies compact status, context, decision, options, consequences, links, and update conditions. | Adopt record-function discipline; adapt carrier form to project domain through `C.32.ADR`, `E.17`, and `E.24.PUB`; reject ADR file form as mandatory or authoritative by itself. | P2S step 8 and the Relations boundary treat decision records by section function and reader use, routing project architecture decisions to `C.32.PAD` and record projection to `C.32.ADR`. | ADR file form is not mandatory and does not create a second decision authority. |
| FPF `C.18`, `C.19`, `E.23`, and `G.11` with NQD, OEE, improvement, telemetry, freshness, and decay practice | Modern architecturing happens under evolution; retained alternatives, stepping stones, feedback, and decay affect the next synthesis question. | Adopt archive, front, pool, improvement, telemetry, freshness, and decay distinctions; adapt them as receiving-owner exits; reject `G.11` refresh state or archive state as architecture choice. | P2S steps 6 and 11 record archive, front, and pool refs, improvement-loop refs, telemetry, actual-structure observations, decay, source-return, and owner-specific return or repair refs without merging their owner semantics. | Archive membership, improvement-loop status, telemetry, or freshness signal does not decide architecture by itself. |

**Source-currentness boundary.** Use each source row only for the P2S field, spine step, boundary, or repair named in the row. Recheck the row when the source practice, FPF owner pattern, described holon, structure kinds, architecture characteristics, transformer relation, eval mode, or project use changes.

### C.32.P2S:12 - Relations

- **Builds on:** `C.22.2` for problem-side recovery, `C.30`, `C.30.AD`, and `C.30.ASV` for grounded architecture, architecture-description adequacy, and structural-view adequacy, `C.33`, `C.34`, and `C.35` for structural-information capture, preservation, and generated or discovered carrier adequacy inside the flow, `C.32` for candidate architecture synthesis, `C.32.HCS`, `C.32.ACS`, and `C.32.ACE` for characteristic starter heads, project criteria rows, and eval programs, `C.25` for Q-bundles, `C.31` family patterns for modularity, reusable structure, and scale preference, `C.29` for mathematical-lens use when claimed, and `E.17` and `E.24.PUB` for publication-face and publication-use claims.
- **Uses:** `C.30.TFS-REL`, `E.18`, and `A.3.4` when architecture pressure concerns transformation-flow or bounded change; `C.30.ILC`, `C.32.MLAO`, and `B.2` family patterns when cross-scope, interlevel, interlayer, meta-holon, emergence, or reidentification pressure changes the candidate frame; `C.32.CONWAY` when co-synthesis of transformer and transformed architectures is current; `C.32.FAIL` when a recognizable architecture-synthesis failure becomes a repair action.
- **Receiving patterns:** `A.19.CPM`, `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, and `C.11` for comparison, selection, archive, front, pool policy, publication of a selected set, and local choice; `C.32.PAD`, `C.32.ADR`, and `C.32.ADA` for project architecture decision, ADR-like projection, and decision adequacy; `C.30.AD`, `E.17`, and `E.24.PUB` for architecture descriptions, publication faces, and publication-use claims; `A.15`, `A.15.1`, `A.15.2`, and `A.15.5` for method, performed work, work plan, and readiness; `C.16`, `C.25`, `C.29`, `C.32.ACE`, `E.23`, `G.11`, and `E.18` for measurement, Q-bundle, mathematical lens, eval, improvement, `G.11` currentness refresh, and `E.18` transformation-flow slice-local refresh.
- **Boundary:** C.32.P2S governs the connected architecturing flow from architecture-relevant pressure to realized selected structures and feedback. `C.33`, `C.34`, and `C.35` deepen the structural-information lane already present in P2S; they do not move the whole architecturing spine out of P2S. C.32.P2S does not replace any owner pattern for architecture claim, architecture description, structural view, candidate palette, comparison, selected-set publication, decision, ADR-like publication, publication form, publication-use claim, method, work, measurement, eval, evidence, assurance, gate, release, improvement, `G.11` currentness refresh, or formal structural-information theory.

### C.32.P2S:13 - Footer marker

`C.32.P2S` governs one reader-facing problem-to-structure architecturing flow: pressure and structural uncertainty become candidate, selected, expected, realized, and evaluated selected structures with owner-specific return or repair exits named by value.

### C.32.P2S:End

