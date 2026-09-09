## C.32 - Architecture Candidate Synthesis

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.32:1 - Problem frame

Use this pattern when a practitioner has a C.30-grounded architecture question for one exact described holon and needs to synthesize several candidate architecture configurations across selected structures before comparison, archive or front-policy work, selected-set result declaration, actual publication, or decision. Keep any obtaining C.30 `ArchitectureRelation` occurrences, the selected `U.Structure` values they relate to the holon, and any candidate, required, desired, or expected structures named only in an `ArchitectureClaim` distinct throughout the synthesis.

Primary working reader: an architect or architecture-responsible practitioner preparing alternatives for one described holon before comparison, selection, selected-set result declaration, actual publication, local choice, or project decision.

Typical entry phrases:

```text
"The functional structure is clear, but module allocation and placement change the trade-off."
"One platform proposal improves reuse and worsens evidence or control burden."
"A search or workshop produced options; which selected structures and architecture characteristics do they change?"
"We need a candidate palette with structurally different architecture configurations before choosing one."
"The architecture of the team or tool that changes the target holon no longer fits the target architecture."
```

**First-minute use slice.** A regulated product-family team has a C.30-grounded architecture question for one exact field-device-family holon. The question names its current obtaining `ArchitectureRelation` occurrences and their selected structures separately from candidate or expected structures stated only in the current `ArchitectureClaim`. The work question is synthesis: how should required functions, constructive modules, field placement, control responsibility, and certification evidence be coordinated so maintainability, substitutability, latency, and evidence reuse stay acceptable? Using C.32, the practitioner first records the selected structures and what each contributes to the synthesis, then records three candidate configurations: one shared module grammar with tighter evidence scope, one product-family split with lower interface burden, and one bounded exception that keeps the existing module split but changes evidence responsibility and reopen trigger. The team now has candidate architecture configurations under declared characteristics, not one attractive platform proposal and not new obtaining architecture relations by candidate wording.

The primary `EntityOfConcern` is the candidate architecture palette for one C.30-grounded synthesis question. Its inputs are the described holon, any obtaining `ArchitectureRelation` occurrences and their selected `U.Structure` participants, and any candidate, required, desired, or expected structures stated only in an `ArchitectureClaim`.

The described holon may be a system, product family, organization-as-system, discipline, AI-agent setup, built asset, episteme, Work occurrence, or another admitted holon kind. Do not admit a source label as a holon. For example, *practice*, *culture*, *tradition*, *style*, *Method*, or *role* may refer to a Method, Method relation structure, relation among local system-role kinds, classification, assignment, Work structure, episteme, source-local meaning, or C.36 cultural-evolution relation. Recover the actual object and claim through its subject pattern; route unresolved claim-bearing *role* wording through `E.10.ROLE`.

ClaimScope and a bounded model-use structure qualify the named use; neither becomes the holon. Architecture pressure may concern Method-family structures, relations among local kinds, classifications, or assignments. Keep each as a selected structure or separate input for the named architecture use, not as a holon kind or function bearer by label. C.32 is not software-system architecture by default; software-system sources are one source family and one domain example.

What goes wrong if C.32 is missed: the team optimizes one visible structure, such as modules, placement, team responsibility, control relation, or evidence package, and then treats that local improvement as architecture synthesis. The competing structures, architecture characteristics, losses, and alternatives disappear before they can be compared.

What C.32 buys in practice: a practitioner can build a small set of candidate architecture configurations, each grounded in selected structure changes, architecture characteristics, known losses, and patterns for the next questions.

Ordinary working move: name the selected structures that really change, name the few architecture characteristics that make the trade-off real, then write two to five candidate configurations with gain, loss, preserved structure, hidden loss, and next receiving use.

Adoption test: after using C.32, another practitioner can see at least two structurally different candidate configurations, the selected-structure changes, the architecture characteristics under pressure, each gain and loss, the source-return condition, and the next receiving use.

Use C.32 only for candidate palette construction. Do not use it to ground the architecture claim, recover one structure, build characteristic criteria rows, design eval programs, handle architecture-influence correspondence, run archive or front-policy work, declare a selected-set result, publish it to an audience, choose locally, or decide the project architecture.

Use `C.32.MWA` instead when several structures of Methods, Work, subjects and their descriptions, capabilities and providers, and cultural change do not line up one-for-one and the needed result is one usable practice architecture. Keep C.32 for a palette of candidate configurations for one grounded architecture question.

Common exits by claim kind:

- `C.30` grounds the described holon, any obtaining `ArchitectureRelation`, its selected `U.Structure`, and any separate `ArchitectureClaim`; `C.30.ASV`, `A.6.F`, and `A.6.M` recover structural views, function wording, and module-interface relations.
- `C.32.HCS`, `C.32.ACS`, `C.32.ACE`, `C.25`, `C.31`, `C.31.ASAP`, and `C.16` govern starter heads, project criteria rows, eval programs, Q-Bundles, modularity or scale-preference claims, and measurement.
- `C.32.MLAO`, `C.32.CONWAY`, `C.32.FAIL`, and `C.29` govern residual-reducing frames, architecture-influence and transformed-architecture correspondence, candidate repair, and mathematical-lens use.
- Use `A.19.CPM` for comparison, `A.19.SelectorMechanism` for set-returning selection, `C.18` and `C.19` for archive, front, and current-pool treatment, `G.5` for selected-set result declaration, `C.11` for local choice, and `C.32.PAD` for a project architecture decision. When audience availability is current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability.
- `C.30.AD`, `E.17`, `E.24.PUB`, `A.10`, and `B.3` govern architecture-description, publication-face, publication-occurrence, evidence, and assurance claims, respectively.

The first useful output is `CandidateArchitecturePalette@Project`. It is the project working record for candidate-palette construction. The name does not introduce a new `U.*` kind, and the record does not carry selection, publication, evidence, assurance, or decision authority.

For a first pass, fill only the described holon, synthesis question, intended palette use, current architecture relations and selected structures that change the question, selected-structure contribution rows, live architecture-characteristic rows, candidate configurations, and palette stop condition. Add ClaimScope or a bounded model-use structure only when it changes synthesis; add other optional refs only when they change the next use of the palette:

```text
CandidateArchitecturePalette@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureSynthesisProjectUseRelationRef?: U.RelationRef resolving to the exact synthesis-use or work-use relation
  architectureQuestionCardRef?: C.30 ArchitectureQuestionCard@Project ref when that exact card is the intake
  describedHolonRef:
  architectureClaimRef?: C.30 ArchitectureClaimRef when a durable actual, candidate, required, desired, or expected claim is current
  currentArchitectureRelationRefs[]?: exact obtaining C.30 ArchitectureRelation refs only
  currentSelectedStructureRefs[]?: the U.Structure participants of those obtaining relations
  synthesisQuestion:
  intendedPaletteUse:
  claimScopeRef?: U.ClaimScope
  boundedModelUseStructureRef?: A.1.1 BoundedModelUseStructure, only when its organization changes synthesis
  architectureSynthesisFrameRef?:
  selectedStructureContributionRows:
    - structureKindRef:
      selectedStructureRef?:
      contributionToSynthesis:
      constraintOrAffordance:
      relationFunctionClaimRef:
      sourceReturnCondition?:
  architectureCharacteristicCriteriaSetRef?:
  architectureCharacteristicCriteriaRowRefs:
  qBundleRefs?:
  characteristicImprovementCycleRef?:
  architectureIdealityPressureRef?:
  scaleAmenabilityPolicyRef?:
  functionBearerFeasibilityRef?:
  candidateArchitectureConfigurations:
    - candidateId:
      candidateName:
      selectedStructureChanges:
        - structureKindRef:
          selectedStructureRef?:
          changeMade:
          relationFunctionClaimRef:
      affectedArchitectureCharacteristicRefs:
      affectedCriteriaRowRefs?:
      architectureCharacteristicEvalResultRefs?:
      qBundleRefs?:
      expectedArchitectureGain:
      knownArchitectureLoss:
      constraintFit:
      preservedStructure:
      lostOrHiddenStructure:
      sourceCueRefs?:
      sourceSideReferent?:
      sourceReturnCondition:
      nextUse:
  tradeoffFrontOrArchiveRef?:
  evolutionWindowRef:
  architectureInfluenceCorrespondenceRef?: C.32.CONWAY frame or exact pair-row ref
  paletteStopCondition:
```

Across C.32, `@Project` is a compatibility and retrieval cue, not a project kind or relation assertion. `CandidateArchitecturePalette@Project`, `ArchitectureSynthesisFrame@Project`, and `ArchitectureCharacteristicImprovementLoop@Project` establish no composite project work, context, authority, viewpoint, or parthood by name. When one of these records is genuinely local to one actual project, identify the exact composite `U.Work` and the direct relation by which synthesis framing, palette construction, or improvement feedback concerns that work. Otherwise no project-work relation is implied. A cited `ArchitectureQuestionCard@Project` transfers neither project locality nor architecture truth: each affirmative `currentArchitectureRelationRef` must already resolve to one obtaining C.30 occurrence, while candidate, required, desired, or expected structure remains claim content until the C.30 predicate is independently satisfied.

### C.32:2 - Problem

Architecture synthesis is the constructive middle of architecture work. A practitioner may already know the described holon, architecture question and intended use, some obtaining architecture relations and selected structures, and some concerns, but still need to configure those structures together before later comparison or decision can be honest.

The typical synthesis problem is multi-structure. State each required function or functioning claim through the predicate and bearer recovered with `A.6.F`. Candidate module, placement, control, transformation-flow, information, evidence, Method, Work, local-kind, classification, or assignment structures may constrain or help explain a candidate, but a kind or assignment establishes no functioning, participation, capability, function bearing, or Work. A control relation can improve supervision while increasing timing or responsibility burden; an information structure can improve maintenance access when exposed through a digital-twin view while still hiding source-return loss; a team structure can improve flow while failing to match module or deployment structure. Every positive responsibility claim still needs its direct domain predicate, actual participants, applicability, and occurrence identity, or the exact A.6.RCD missing governor.

A functional architecture is not enough by itself. A function graph, use case decomposition, workflow, neural cell graph, Method step, or source function from cultural or practice material can enter architecture synthesis only after `A.6.F` identifies the function or functioning claim and its possible bearer, and after any selected structure or source label is recovered. If no bearer can satisfy the predicate recovered with A.6.F under the relevant module, Method, resource, placement, control, Work, evidence, local-kind, classification, or assignment constraints, the candidate must be repaired before it enters comparison, selection, local choice, or decision work. Those neighboring structures constrain the candidate; they do not bear the function by label.

The typical synthesis problem is also multi-characteristic. Architecture characteristics such as cohesion, coupling, substitutability, evidence reuse, work repeatability, latency, locality, control separation, source-return cost, and composite quality families often compete. Functional demands describe what the holon is to do; architecture characteristics describe whether the selected structures make those demands maintainable, controllable, evolvable, replaceable, inspectable, and otherwise acceptable in the current context.

One recurring candidate-generation heuristic is idealization: ask whether an existing bearer or resource can carry an additional required function under the selected-structure constraints, whether a support bearer can disappear, or whether a more general scale-amenable bearer can replace several special bearers. Admit that heuristic only as a candidate. The candidate must name the functions transferred to a bearer, the bearer removed or generalized, the architecture characteristics improved and worsened, and any BLP scale window or waiver when scale advantage is claimed.

Use C.32 to make the constructive translation explicit. Build a small palette whose candidates answer: which selected structures are configured together, which architecture characteristics improve or worsen, which constraints remain admissible, what source detail must remain recoverable, and which pattern supplies the next claim or test.

### C.32:3 - Forces

| Force | Tension |
|---|---|
| Decision pressure | Teams want one answer before the alternatives are explicit. |
| Candidate plurality | Several plausible variants may be useful for different reasons. |
| Source richness | Source cues can suggest candidate work without establishing the architecture claim. |
| Compression risk | A short palette can hide source distinctions needed later. |
| Neighboring claim patterns | Front, G.5 result declaration, publication availability, local choice, evidence, assurance, and decision claims are admissible only through patterns for the next questions after the architecture content is shaped. |

### C.32:4 - Solution

Create an `ArchitectureSynthesisFrame@Project` when the selected structures and characteristics are not yet visible enough. The frame is a temporary visibility aid for C.32 use; the palette remains the first useful output. Then create a `CandidateArchitecturePalette@Project`. Treat the palette as a small constructive object over selected structures of a described holon, not as a checklist, not as a decision, not as a selected-set result declared under `G.5`, and not as a publication occurrence.

Work in seven steps:

1. Anchor the palette to one described holon or holon family, synthesis question, and intended next use. Name any current C.30 architecture relations and selected structures that can change that question.
2. Write the smallest useful set of selected-structure contribution rows. Start with the functional demand and candidate bearer recovered with `A.6.F`, constructive module or manufacture structure, and placement or deployment structure when they shape the question; add control, transformation-flow, Method, Work, local-kind relation or classification, assignment, information, evidence, scale, or other selected structures only when they change the synthesis question. Send unresolved claim-bearing “role” wording through `E.10.ROLE`. For each required function, name at least one admissible bearer under the declared constraints.
3. Reference the architecture-characteristic criteria rows and any Q-Bundle slots that make the trade-off real. Separate functional demand, architecture characteristics, criteria rows, eval results, and decisions.
4. Generate candidate architecture configurations. A candidate claim may propose, for example, changed decomposition, allocation, A.6.F function bearing, bearer count, placement, interface grammar, a control or transformation-flow relation, Method use, future assignment conditions, an independently established responsibility relation, evidence scope, information structure, or a bounded exception. Modal candidate wording creates no assignment occurrence and proves no Work occurred. Use a WorkPlan, policy, commitment, permission, decision, or other truthful prospective object when one applies. For actual precise Work, recover each exact actual performer System through A.13 and let A.15.1 independently admit the dated Work and enacted Method; add an assignment occurrence, its declared species, and F.6 only when the candidate account or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment. F.6 identifies neither assignment nor performer, missing or failed F.6 leaves the Work intact, and an assignment never carries responsibility by itself.
5. For each candidate, state selected structure changes, expected architecture gain, known architecture loss, constraint fit, preserved structure, lost or hidden structure, and source-return condition.
6. When a front, archive, search result, or pool-treatment policy is being used, cite `C.18`, `C.19`, or NQD and OEE support as generation or retention support only. Keep the C.32 candidate content separate from archive work, front membership, pool treatment, selected-set result declaration, actual publication, and local choice.
7. Stop when the palette contains the fields required by the pattern for the next question, such as comparison, C.18 or C.19 front-policy use, selected-set result declaration, actual publication, local choice, decision, or repair.

These contribution rows are not an audit checklist. Together they name only the structures that actually change the candidate configuration.

**Architecture-characteristic improvement loop.** C.32 is one turn in a continuing improvement cycle over architecture characteristics, not a one-shot search for final form. The practitioner starts with characteristic pressure or criteria rows from `C.32.ACS`, `C.31`, `C.25`, `C.16`, `C.16.P`, `C.31.ASAP`, or a local Q-Bundle; synthesizes candidate selected-structure changes; and records which criteria rows are expected to improve and which protected rows may worsen.

`ArchitectureCharacteristicImprovementLoop@Project` is a local feedback record for reopening C.32 synthesis when characteristic pressure changes. It is not an E.23 method, an ACE eval program, a comparison rule, a selection result, or a decision.

Keep each receiving claim with its subject pattern.
Criteria rows stay with `C.32.ACS`; Q-Bundles with `C.25`; scale preference with `C.31.ASAP`; measurement with `C.16`; eval programs and eval results with `C.32.ACE`.
Improvement-question framing and repeated-improvement method stay with `E.22` or `E.23`.
Use `A.19.CPM` for comparison, `A.19.SelectorMechanism` for set-returning selection, `G.5` for selected-set result declaration, `C.11` for local choice, and `C.32.PAD` for a project architecture decision. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability.
For this loop, bring only the changed characteristic pressure into C.32 and return the next candidate palette.
Open the next synthesis question from the resulting eval result, front relation, retained alternative, rejected candidate, or source-return trigger.

An eval result that cohesion improved, evidence reuse decayed, coupling changed, latency worsened, or exception growth changed does not choose an architecture. A practitioner may use it as feedback only after the bearer, criteria row, scale or qualitative reading frame, selected structures, parity frame, and pattern for the next question are recoverable.

```text
ArchitectureCharacteristicImprovementLoop@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureSynthesisProjectUseRelationRef?: U.RelationRef resolving to the exact synthesis-feedback or work-use relation
  describedHolonRef:
  currentArchitectureCharacteristicPressureRefs:
  architectureCharacteristicCriteriaSetRef?:
  architectureCharacteristicCriteriaRowRefs?:
  synthesisQuestion:
  candidatePaletteRef:
  architectureCharacteristicEvalResultRefs?:
  changedSelectedStructureRefs:
  improvementClaimPatternLocator: C.32.ACS | C.32.ACE | C.31 | C.25 | C.16 | C.16.P | C.31.ASAP | other pattern for the next question
  nextSynthesisQuestion?:
  sourceReturnCondition:
```

| Synthesis position | Typical selected structure | What it contributes | First pattern for the next question |
|---|---|---|---|
| Functional demand | `FunctionalStructure` | A.6.F-recovered functional demands, dependencies, constraints, and candidate bearer pressure. | `C.30.ASV`, `A.6.F`, `C.30.TFS-REL` when flow relation is current. |
| Constructive bearer | `ModuleInterfaceStructure`, material, manufacturing, or component relation. | Candidate modules, interface grammar, substitutability, variation slots, and fabrication burden. | `A.6.M`, `C.31`, `C.30.ASV`. |
| Placement and locality | `PlacementDeploymentStructure` or `MaterialSpatialStructure`. | Location, latency, access, environment, maintenance, and source-return burden. | `C.30.ASV`, domain pattern when current. |
| Control and flow | `ControlStructure` and `TransformationFlowStructure`. | Feedback, supervisor relation, rate, flow relation, crossing, and transformation relation. | `C.30.LCA`, `E.18`, `C.30.TFS-REL`, `C.27` when timing is current. |
| Method, Work, local-kind or assignment, information, and evidence | Method and Work structures; relations among local system-role kinds, classifications, or assignment structures; direct allocation or responsibility relations; information and evidence structures. | Prospective enactment burden, independently established responsibility, data custody, evidence reuse, assurance pressure, and source return. | `E.10.ROLE` for unresolved wording; A.2 and A.2.1 for recovered kind, classification, or assignment; A.15 for actual Work, with F.6 only when precise assignment-bound attribution is expressly consumed; the admitted direct domain predicate or exact missing governor for responsibility; `A.10`, `B.3`, `C.25`, and `C.31` when those claims are current. |

Candidate architecture changes are local C.32 entries for candidate configurations. They are not FPF work occurrences, method steps, or receiving-pattern claims. A change is admissible only when the selected structure being changed is named.

| Architecture-change kind | Constructive use | Minimum repair against overread |
|---|---|---|
| `configurationSynthesis` | Coordinate several selected structures into one candidate architecture configuration. | State the selected-structure contribution rows and architecture characteristics before claiming improvement. |
| `functionalAllocationChange` | Change the candidate A.6.F bearer or the module, Method, Work, local kind, separate System-classification judgment, assignment, control, or other structures that constrain its functioning. | Keep the functional predicate and bearer distinct from every neighboring structure; unresolved “role” wording goes through `E.10.ROLE`. |
| `functionBearerFeasibilityRepair` | Repair a candidate whose functional structure names a required function that no admitted bearer can bear under module, placement, resource, control, or evidence constraints. | Add or change an A.6.F bearer, split the function, change placement or resource access, change the direct control or responsibility relation, reduce the functional demand, or reject the candidate. |
| `functionBearerConsolidation` | Transfer a required function onto an existing bearer under the selected-structure constraints, remove a support bearer, or propose one more general bearer for several functions. | State the functions transferred, the bearer removed or generalized, the affected architecture characteristics, the lost options, and the BLP scale window or waiver when scale advantage is claimed. |
| `structuralSubstitution` | Replace one selected structure with another candidate structure. | State what is preserved and what is lost. |
| `relationRetargeting` | Change an affected relation endpoint, direct responsibility relation, system-role assignment, dependency relation, admissible-use boundary, or source-return relation. | Name the relation kind and its actual predicate before using the change in a candidate; if a needed responsibility predicate is absent, record the exact missing governor. |
| `architectureInfluenceCorrespondenceSynthesis` | Coordinate candidate structures when an independently typed architecture or other source constrains transformed-side architecture content for a changed referent. | Open `C.32.CONWAY`; name the changed referent and any independently grounded A.3.4 transformation separately; name each typed influence source by kind and its exact direct relation when an influence occurrence is asserted, otherwise keep the pressure synthesis-local with its `missing-governor`, unresolved-grounding, or false-predicate disposition; for each actual architecture side keep the exact C.30 holon, obtaining `ArchitectureRelation`, and selected `U.Structure` visible, and keep modal content in `ArchitectureClaim`; then prepare influence-source-side, transformed-side, joint, or bounded-mismatch candidates with affected architecture characteristics, expected gain, known loss, source-return condition, and pattern for the next question. |
| `decompositionOrAllocationChange` | Propose reallocation of a module, future assignment condition, Work boundary, evidence relation, data custody, control relation, or variation slot across structures; retarget responsibility only through its direct domain predicate. | State the proposed boundary, participant conditions, prospective object, and migration burden. Do not create an assignment or Work occurrence from candidate wording; return the exact missing governor when the needed responsibility relation has no current predicate. |
| `placementOrDeploymentChange` | Change locality, deployment, material placement, installation, or maintenance access. | Name the affected structure and the latency, access, source-return, or environment burden. |
| `flowOrControlVariant` | Change transformation flow, control depth, rate band, feedback boundary, or mediator relation. | State the timing, control, observability, or accountability burden created by the change. |
| `interfaceGrammarChange` | Narrow, split, widen, or stabilize an interaction boundary. | Apply `A.6.M` when module-interface relation repair is current. |
| `declaredScopeOrHolonLevelChange` | Split, merge, add, or remove a declared holon-level reference, declared scope, evidence scope, work-method scope, or aggregation scope. | Name the affected reference, use `C.30.STRAT` when the wording is only a stratification term, and use `B.2` only when whole reidentification is current. |
| `boundedException` | Keep a residual because removing it costs more than it buys now. | State the exception, reopen trigger, and next subject pattern if later source use or decision use expands. |

**Didactic mini-slices.** Use these as examples of the kind of work C.32 expects, not as domain-specific templates.

| Situation | First C.32 step | Candidate repair |
|---|---|---|
| A sterilization function is placed in a shared field module, but the field placement has no power and no certified evidence relation for that heat cycle. | Keep the functional demand separate from the module and placement structures. | Add a local certified bearer, split the function into pre-field and field steps, change placement, or reject the shared-module candidate. |
| An ML functional graph includes retrieval, planning, and action, but no module-interface relation or direct domain predicate carries evidence-refresh responsibility or admissible-use control. | Treat the graph as functional structure and recover module-interface, evidence, control, admitted-System, and responsibility relations separately. | Add a retrieval service and an admitted evidence-refresh responsibility relation with actual participants, add a supervisor relation, narrow model-interface behavior, return the exact missing governor, or reject the candidate. |
| A Method family says the review function is automated, but A.6.F identifies no bearer and no direct responsibility predicate identifies who is responsible for exceptions. | Recover the Method structure and A.6.F function bearer first. Keep any admitted Systems, local kinds, separate System-classification judgments, assignments, actual Work and separately needed F.6 attribution, responsibility relation, and evidence structure separate. | Propose an assignment condition only in truthful plan or candidate content; cite a direct exception-responsibility relation or exact missing governor; split the Method step, change evidence scope, or keep the automation as source cue. Use a full Work chain only after performance. |

When one independently typed architecture-side or other source constrains transformed-side architecture content for a changed referent, use `C.32.CONWAY` before using Conway, mirroring, or inverse-Conway language in candidate synthesis. The practitioner names the changed referent and any actual A.3.4 transformation separately, each influence source by exact kind and its direct relation only when that occurrence is asserted, and, for each actual architecture side, the exact C.30 described holon, obtaining `ArchitectureRelation`, and selected `U.Structure`; modal architecture content stays in an exact `ArchitectureClaim`. Without an admitted and satisfied direct influence predicate, the pressure stays synthesis-local in the C.32.CONWAY frame with its `missing-governor`, unresolved-grounding, or false-predicate disposition and no exact pair row. Candidate work then names influence-source-side, transformed-side, joint, or bounded-mismatch changes, architecture characteristics under pressure, expected gains, known losses, and source-return conditions.

Keep the candidate palette as the C.32 result. `C.32.CONWAY` carries the architecture-influence correspondence frame or one exact reusable pair-row episteme. Influence alone supplies no acting System, local system-role kind, System-classification judgment, assignment, Work, changed-referent identity, or transformation participation. Transformation, acting and Work attribution, exact influence, transformation-flow, and module-interface claims belong to `A.3.4`, `A.12`, `A.2.1`, `A.15.1`, `F.6`, the direct influence pattern, `E.18`, `C.30.TFS-REL`, or `A.6.M` when current. Structural-similarity or preservation claims belong to `C.29` when they are current.

A richer dossier is optional. Open it only when one candidate must carry source views, relation notes, measurements, C.29 lens outputs, evidence notes, or failure repairs that affect the next architecture use. Ordinary C.32 use should remain one row per candidate configuration.

**Downstream use.** The C.32 result is architecture-specific candidate content. Use `G.5` to declare a selected-set result, `C.11` for a fixed local choice, and `C.32.PAD` for a project architecture decision. Use `C.18` or `C.19` for archive, front, pool-treatment, or generation policy when that claim is current. Use `C.30.AD` for architecture-description work. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability.

**Stop condition.** Stop C.32 when the palette can support the next use without hiding the selected structures, architecture-change kind, architecture gain, architecture loss, constraint fit, source-return condition, or pattern for the next question.

**Lowering condition.** Leave C.32 candidate construction when the needed architecture claim is not grounded, the item is only a source artifact, only one configuration is visible, the candidate lacks selected-structure change, the functional demand has no feasible bearer, the architecture gain or loss is unnamed, or the next use is already comparison, selection, selected-set result declaration, actual publication, local choice, decision, evidence, or assurance. Use `C.30` for grounding, the source or description pattern for source artifacts, `C.32.FAIL` for candidate repair, and the named pattern for the next question when the downstream claim is current. Reopen C.32 when a criteria row, eval result, retained alternative, front relation, source-return trigger, or source-currentness change alters the selected structures under pressure or the acceptable loss profile.

### C.32:5 - Archetypal Grounding

**Tell.** The regulated product-family first-minute slice in the Problem frame shows the minimum complete move: one grounded question, a small set of selected-structure contribution rows, three genuinely different candidate configurations, explicit gains and losses, and no premature decision. **Show.** The cases below vary the described holon and the selected structures while keeping that move recognizable. **Show again.** The didactic mini-slices in Solution 4 show what to repair when a required function has no feasible bearer. These three views are one grounding set, not three additional procedures.

| Grounded working case | Synthesis question | C.32 candidate work | Stop condition |
|---|---|---|---|
| Regulated product family with growing field exceptions | How should functions, module interfaces, placement, and evidence scope be configured so substitutability and certification burden stay acceptable? | Prepare candidates that narrow interface grammar, split the family by evidence scope, change placement responsibility, or keep a bounded exception with source return. | Stop at palette unless G.5 selected-set result declaration, publication availability, assurance, or architecture decision is current. |
| Built-asset digital-twin handover where a method-defined digital-twin view hides source loss | Which selected structures do the digital-twin dimensions actually describe, and which source-return obligations must survive maintenance use? | Prepare candidates that split information view, add source-return scope, retarget maintenance responsibility, or change module and placement structure. | Stop before built-asset architecture-description, MVPK publication-face, or A.10 evidence-relation claims unless `C.30.AD.BA`, `E.17`, `E.24.PUB`, or evidence patterns are current. |
| Emergency-department triage arrangement whose local desk is fast but hospital-wide escalation is brittle | How should admitted Systems, local system-role kinds or classifications, future assignment conditions, procedure and Method structure, control, direct responsibility, evidence, and any actual Work and separately needed F.6 attribution be configured so speed does not erase escalation adequacy? | Prepare candidates that retarget responsibility only through an admitted direct predicate, state a possible mediator assignment as plan or candidate content rather than an occurrence, split triage scope by patient class, or adjust evidence capture; use the exact missing governor when needed. | Stop before ethical mediation, evidence, staffing decision, assignment occurrence, or performed Work unless those claims are current. |
| AI-agent review setup where local autonomy conflicts with policy scope | How should control, module-interface, evidence-refresh, and work-method structures be configured so autonomy and policy conformance stay jointly acceptable? | Prepare candidates that add supervisor relation, narrow model interface behavior, change evidence refresh cadence, or alter work-method responsibility. | Stop before safety, release, gate, or causal claims unless their subject patterns are current. |
| Method family whose reusable template speeds authoring and slows review | How should Method structure, authored-section structure, review evidence, admitted Systems, possible future assignment conditions, and direct review-responsibility relations be configured so repeatability does not create hidden review residue? | Prepare candidates that split Method variants, add review evidence scope, change a planned assignment condition, retarget responsibility through its direct predicate or record the exact missing governor, or accept bounded local Method residue. | Stop before Method governance, curriculum decision, assignment occurrence, performed Work, description use, or publication-face use unless the pattern for the next question is current. |

### C.32:6 - Bias-Annotation

**Scope:** Limited to constructing a small candidate architecture palette for one C.30-grounded architecture question about one described holon or holon family. C.32 is not a universal architecting Method, a software-architecture default, a comparison or selection rule, a publication route, or a decision procedure.

| Lens | Likely drift | Repair |
|---|---|---|
| Gov | A candidate, front member, generated option, or workshop consensus is treated as selected, authorized, accepted, published, or current. | Stop at the palette and use the pattern for the next claim; candidate wording creates none of those relations. |
| Arch | One visible structure, source diagram, functional graph, or organizational arrangement is treated as the architecture. | Ground the exact holon and architecture question, then coordinate only the selected structures and characteristics that actually change the candidate. |
| Onto-Epist | A description artifact, claim, model, role-shaped label, or proposed structure is treated as an obtaining architecture relation or world-side structure. | Keep the holon, obtaining relations, selected structures, modal claim content, source artifact, and candidate change distinct; use each direct subject pattern. |
| Prag | The palette becomes a dossier or exhaustive search although two to five useful alternatives would support the next use. | Keep the smallest useful set of selected-structure contribution rows, keep one row per candidate, and add richer evidence only when it changes the next architecture use. |
| Did | Formal records or software examples obscure the constructive move for another field. | Lead with the ordinary move—structures changed, gain, loss, constraint fit, source return, next use—and use unlike grounded cases; keep the richer record optional. |

### C.32:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-C32-1` | The use names one synthesis question, described holon, intended palette use, and the current architecture relations and selected structures that change the question; ClaimScope or a bounded model-use structure is added only when action-changing. | Keeps the palette local without a generic context premise. |
| `CC-C32-2` | The selected-structure contribution rows name the smallest useful set of selected structures and subject patterns and state what each contributes. | Prevents one-structure optimization from masquerading as synthesis. |
| `CC-C32-3` | Architecture characteristics and any quality bundles are named before candidate comparison. | Keeps functional demand distinct from architecture trade-offs. |
| `CC-C32-4` | Each candidate configuration names selected structure changes, expected gain, known loss, and constraint fit. | Makes the candidate actionable. |
| `CC-C32-5` | Compressed, generated, or view-derived candidates carry a source-return condition. | Keeps later source-use or decision-use claims tied to recoverable sources. |
| `CC-C32-6` | Archive, front, pool-treatment, G.5 result declaration, publication availability, local choice, and decision uses have named patterns for the next questions. | Keeps synthesis separate from downstream receiving claims. |
| `CC-C32-7` | Worked slices show what changes in practice across multiple selected structures. | Keeps the pattern constructive. |
| `CC-C32-8` | If an independently typed source constrains transformed-side architecture content for a changed referent, `C.32.CONWAY` is opened before Conway, mirroring, or inverse-Conway language is used as guidance; the source kind, its exact obtaining direct relation or precise provisional disposition, and both exact C.30 architecture sides or modal claims are named without inferring acting, Work, or transformation facts. | Keeps influence-source and transformed-side content distinct while making correspondence synthesis constructive. |

### C.32:8 - Common Anti-Patterns and How to Avoid Them

#### C.32:8.1 - Architecture trade-off failures

| Anti-pattern | Repair |
|---|---|
| **Local structure win hides other-scope loss.** A module split, control placement, evidence scope, or direct responsibility-relation change helps one concern while worsening another architecture characteristic. | Rebuild the selected-structure contribution rows and record the gained and lost characteristics before comparison; do not infer responsibility from a team label or assignment. |
| **Function and architecture characteristic collapse.** The candidate is argued from user-visible function while evolvability, coupling, cohesion, latency, evidence burden, or another architecture characteristic remains unnamed. | Recover the function through `A.6.F` or the structural-view pattern, then name the architecture characteristic separately. |
| **Function without feasible bearer.** A functional architecture, workflow, Method step, or searched graph asks for a function but A.6.F identifies no bearer that satisfies the functional predicate under the relevant module, resource, placement, control, evidence, local-kind, classification, or assignment constraints. | Repair the bearer claim before admitting the candidate. |
| **No real trade-off.** Only one configuration is visible, or alternatives differ only by description. | Generate structurally different candidates, or state why the project work is not architecture synthesis and use the subject pattern. |
| **Description artifact stands in for candidate content.** A diagram, ADR, view, dashboard, benchmark output, or digital-twin view is the visible work product, but the selected structures and architecture-characteristic trade-off are still missing. | Keep the visible work product with its description-use, C.29 mathematical-lens, benchmark, publication, or source-use pattern and recover candidate content before C.32 use. |
| **Front member treated as durable optimum.** A front member, local winner, or benchmark leader is used as if the evolution window will stay fixed. | Record evolution window, source-return condition, and retained alternatives under the exact C.18 or C.19 predicates; use G.5 only to declare a selected-set result from those alternatives. If the result is published, use E.17 for a source-backed face and source return and E.24.PUB for the publication occurrence and audience availability. |
| **Software-source overfit.** A software architecture source supplies a useful architecture-change idea, but the described holon is not a software system. | Translate only the change over selected structures and characteristics; do not import the software ontology. |
| **Architecture-influence source omitted.** The candidate architecture for a changed referent cannot be built, tested, deployed, certified, or evolved under the current architecture, Work, communication, method, tool, deployment, evidence, selected-structure, or other source, but that source's exact kind and influence status are hidden. | Open `C.32.CONWAY`; recover the source kind and either its exact obtaining direct relation or the precise provisional disposition, keep the acting System, any local system-role kind or assignment, Work, changed referent, and any actual transformation distinct, and prepare influence-source-side change, transformed-side change, joint change, and bounded mismatch as candidate alternatives or comparison inputs. |
| **Method-defined dimensions lose their semantics.** A BIM, digital-twin, or view-method dimension already carries method-defined structure, constraint, cost, schedule, use-phase, or maintenance semantics, but the synthesis text keeps only the dimension name or dimension count. | Preserve the method semantics and map them to selected structures, constraints, characteristics, and source-return conditions. |
| **Ideality shortcut.** Fewer bearers, fewer modules, or one universal module is only a candidate direction until functions, architecture characteristics, scale window, safety, admissibility, and losses are named. | Keep it as one candidate and expose those missing tests before comparison. |

#### C.32:8.2 - More repair cues

| Repair cue | Symptom | First repair |
|---|---|---|
| `SingleStructureSynthesis` | One structure is optimized and the result is called the architecture. | Write the selected-structure contribution rows and name the architecture characteristics before admitting the candidate as C.32 work. |
| `UserFunctionAsArchitectureCharacteristic` | The user-visible function is treated as the architecture quality being optimized. | Recover the functional demand through `A.6.F` or `C.30.ASV`; then name the architecture characteristic or quality bundle separately. |
| `FunctionNoFeasibleBearer` | A functional architecture names a required function, but no bearer satisfies the predicate recovered with A.6.F under the relevant System, module, Method, resource, placement, control, evidence, local-kind, classification, or assignment constraints. | Repair with `functionBearerFeasibilityRepair`: add or change the bearer, split the function, change placement or resource access, change control relations, reduce the demand, or reject the candidate. A kind or assignment never becomes the bearer by form, and any responsibility claim remains a separate direct predicate or exact missing governor. |
| `DescriptionFormAsArchitecture` | An architecture-description artifact is treated as the architecture because it is the most visible representation. | Keep the visible work product under `C.30.AD`, `C.30.ASV`, `E.17`, `E.24.PUB`, `C.29`, or source-use governance as applicable; recover described holon, selected structures, candidate architecture change, and characteristic bundle before admitting any C.32 candidate. |
| `BenchmarkWinnerAsArchitecture` | A comparison result is treated as architecture selection. | Treat the result as comparison input or as source material for an A.10 evidence relation when that claim is current; admit a C.32 candidate only after selected structure, architecture-change kind, gain, loss, and pattern for the next question are recovered. |
| `MethodDimensionSemanticsLost` | A BIM, digital-twin, or architecture-view method supplies dimensions, but C.32 use keeps only the dimension name or dimension count and loses the method's structure, constraint, schedule, cost, use-phase, or maintenance semantics. | Preserve the source method semantics, then map each method-declared dimension to selected structures, constraints, preserved and lost structure, architecture characteristics, and source-return condition. |
| `ArchitectureInfluenceMismatch` | One independently typed source is incompatible with transformed-side architecture content needed for the changed referent, or the source's influence status is still provisional. | Open `C.32.CONWAY`; recover the changed referent, each source's exact kind and obtaining relation or precise provisional disposition, both exact C.30 architecture sides or modal claims, and any separately grounded acting, Work, method-side or direct method-use relation, A.3.4 transformation, or E.18 flow facts through their subject patterns; generate candidates that change the influence-source side, the transformed side, both sides, or a bounded mismatch. Use `C.29` only if structural similarity is claimed. |
| `ShortlistByName` | A set is called shortlist before the result fields required by `G.5` exist. | Keep it as a local palette or open `G.5`. |
| `UniversalBearerAsArchitecture` | A universal module, general substrate, or existing resource is treated as better architecture by name. | Create a C.32 candidate that names functions transferred to the bearer, bearer count change, coupling change, evidence burden, control burden, safety and admissibility boundary, and BLP scale window or waiver if scale advantage is claimed. |
| `SourceCompressionNoReturn` | A candidate hides source distinctions. | Add a source-return condition or demote the item to a source cue. |

### C.32:9 - Consequences

| Positive consequence | Cost or trade-off |
|---|---|
| Candidate architecture configurations are visible before local choice or decision. | Losses and constraint fits must be named earlier. |
| Architecture-characteristic improvement is handled as iterative architecture work. | Each iteration must say which characteristic pressure changed, which selected structures were changed, which reading or feedback is admissible as synthesis input, and what source-return condition opens the next synthesis question. |
| Multi-structure synthesis is reviewable. | The practitioner must keep functional, module, placement, control, Work, evidence, and other selected structures distinct when they matter. |
| Architecture characteristics and quality bundles are recorded as comparison inputs for the pattern for the next question. | The palette may need characteristic repair through `C.25`, `C.31`, `C.16`, or later comparison, local-choice, selection, or selected-set result-declaration work through `A.19.CPM`, `C.11`, `A.19.SelectorMechanism`, or `G.5`, respectively, when those claims are being made. |
| Holonic architecture breadth is preserved. | Examples and candidates must name the described holon and selected structures instead of using domain defaults as unstated selected structures. |
| Source cues can inform architecture work without importing source-domain ontology. | Source-side expressions require recovery of referent, selected structure, architecture-change kind, and source-return condition. |
| Downstream G.5 result declaration and architecture-decision work stay cleaner. | The team must open the pattern for the next question when it wants to declare a selected-set result, publish it to an audience, make a local choice, or decide the project architecture. |
| Evolutionary and search practices are usable without hidden single-winner optimization. | The palette may need retained alternatives even when one candidate looks convenient. |

### C.32:10 - Rationale

Architecture practice needs a method between a grounded architecture question and an architecture decision. Use `C.30` to ground the question over selected structures of a described holon. Use `C.30.ASV`, `A.6.F`, `A.6.M`, `C.30.LCA`, `C.30.TFS-REL`, `C.25`, and `C.31` to recover the particular structures and characteristics. Later, use `C.18` or `C.19` for front, archive, or pool treatment, `G.5` for selected-set result declaration, `E.17` and `E.24.PUB` for their distinct publication jobs, `C.11` for local choice, and the applicable decision pattern for a project decision.

Use C.32 for the constructive middle: building a small set of candidate architecture configurations whose selected structures, allocations, characteristic trade-offs, known losses, source-return conditions, and patterns for the next questions are explicit.

The same middle repeats during improvement. A later criteria-row change, scale-row change, C.16 reading, C.25 or C.31 pressure change, C.31.ASAP scale-preference change, or C.18 or C.19 front, archive, or retained-alternative relation can reopen C.32 when it changes the architecture-characteristic pressure, the selected structures under stress, or the acceptable loss profile. The practitioner then synthesizes another candidate palette; the trigger does not decide the architecture.

The work is to make synthesis real enough that architecture content is available for a later front, comparison, selected-set result declaration, actual publication, or decision.

### C.32:11 - SoTA-Echoing

These rows show how source practice contributes to C.32. The opening of each second-column entry classifies the source use; the opening of each transfer states its disposition. The blocked-overread column gives the use limit, and the source-currentness boundary below gives the reopen rule. Software-system sources are comparison inputs, examples, or lineage only; they do not narrow C.32 to IT architecture.

| Source to inspect | Source-use class and why it matters here | Transfer into C.32 | Where this contribution appears in C.32 | Blocked overread |
|---|---|---|---|---|
| Architecture synthesis and quality-attribute optimization: Di Pompeo and Tucci 2023 (`https://arxiv.org/abs/2301.07516`), ATRAF 2025 (`https://arxiv.org/abs/2505.00688`), and current FPF `C.32.HCS`, `C.32.ACS`, `C.32.ACE`, `C.25`, `C.31`, `C.16` | **Current comparison input plus current FPF authority:** quality attributes and architecture characteristics compete, and multi-objective treatment gives the architect a trade-off view instead of one scalar winner. | **Adapt:** make candidate configurations name ACS criteria rows and Q-Bundle slots before comparison, and use ACE evaluation results as feedback for the next synthesis question only through the pattern for that question. | `CandidateArchitecturePalette@Project` includes `architectureCharacteristicCriteriaSetRef?`, `architectureCharacteristicCriteriaRowRefs`, `qBundleRefs?`, `affectedCriteriaRowRefs?`, `architectureCharacteristicEvalResultRefs?`, `constraintFit`, and `tradeoffFrontOrArchiveRef?`; Problem separates functional demand from architecture characteristics. | A user function, metric, benchmark, scalarized score, evaluation result, or apparent improvement is not architecture synthesis, comparison, project architecture decision, or improvement-cycle closure. |
| DSM, multiple-domain matrix, and current DSM modularization research, including Jiang and Luo 2026 (`https://arxiv.org/abs/2604.28018`) | **Current research comparison with established DSM lineage:** modularization is useful, while LLM-based DSM work also exposes divergence between functional priors and structural objectives. | **Adapt:** use DSM or clustering as one candidate-generation and inspection source; recover selected structures, structural objective, and engineering semantics before treating the result as architecture-synthesis material. | Solution adds `selectedStructureContributionRows`; candidate work coordinates functional, constructive, placement, control, work, information, and evidence structures rather than accepting a cluster as architecture. | A cohesive cluster, graph partition, or generated modularization is not architecture adequacy by itself. |
| Current FPF architecture kernel: `A.22`, `C.30`, `C.30.ASV`, `C.30.ILC`, `C.31`, `C.31.ASAP` | **Current internal authority:** obtaining architecture relations connect an exact described holon to selected structures for a named architecture question and use. | **Adopt:** use SoTA and domain sources only after recovering described holon, synthesis question and use, current architecture relations, selected-structure contribution rows, architecture criteria rows, selected structure changes, gain, loss, and pattern for the next question. | `CandidateArchitecturePalette@Project` requires `selectedStructureContributionRows`, architecture-characteristic criteria rows, selected structure changes, `constraintFit`, preserved and lost structure, source-return condition, and `nextUse`; worked cases cover heterogeneous holon kinds. | Diagrams, source expressions, software-system templates, and platform proposals remain source cues until the described holon, selected structures, architecture criteria, gain, loss, and pattern for the next question are recovered. |
| ISO 42010:2022 architecture-description standard (`https://www.iso.org/standard/74393.html`) | **Current normative comparison:** it distinguishes architecture, description, view, viewpoint, concern, correspondence, and model kind, while leaving architecture itself outside the standard's subject. | **Adopt narrowly:** treat architecture-description artifacts as source cues or description material until a candidate selected-structure change is recovered. | C.32 fields distinguish source cues, source-side referents, selected structures, and architecture characteristics. For description or view repair, use `C.30.AD` or `C.30.ASV`; for publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability. | An architecture-description artifact or publication face is not a candidate architecture by itself. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed.; overview at `https://evolutionaryarchitecture.com/` and O'Reilly page `https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/` | **Current practitioner comparison:** guided incremental change makes affected architecture characteristics and feedback visible. | **Adapt:** add reversible first steps where useful, affected criteria rows, ACE evaluation results, source-return triggers, a next synthesis question, and no source-term takeover. | Solution and SoTA rows state that source-side fitness-function practice is represented through exact `C.32.ACE` evaluation-program assertions over ACS rows; candidate rows can name `affectedCriteriaRowRefs?`, `architectureCharacteristicEvalResultRefs?`, next synthesis question, and source-return condition; measurement claims use the exact C.16 predicate. | Evaluation results need an exact comparison, local-choice, or other preference-use assertion before they affect preference. They can start the next synthesis iteration when characteristic pressure changes and the feedback conditions in Solution 4 hold. |
| Shaw and Petre, `Design Spaces and How Software Designers Use Them` (`https://arxiv.org/abs/2407.18502`); Cortellessa, Diaz-Pace, Di Pompeo, Tucci, `Towards Assessing Spread in Sets of Software Architecture Designs` (`https://arxiv.org/abs/2402.19171`) | **Current research comparison:** design-space work distinguishes structural alternatives from objective-space scores. | **Adapt:** preserve a candidate palette when one scalar winner would hide structurally different alternatives; distinguish objective-space signals from selected-structure differences. | Retain candidate plurality until `G.5`, `C.11`, or a `C.32.PAD` project architecture decision relation is current; each candidate must name selected structure, architecture-change kind, gain, loss, and hidden or preserved structure. | A Pareto front, score, spread indicator, or generated set does not select the architecture and does not replace architecture-space inspection. |
| MOSA and open-system engineering from `C.31.RSA` (`https://www.cto.mil/sea/mosa/`; `https://www.cto.mil/wp-content/uploads/2025/03/MOSA-Implementation-Guidebook-27Feb2025-Cleared.pdf`); product-line variability and product-platform practice from `C.31.RSA` and `C.31.ASAP` (`https://www.sei.cmu.edu/library/variability-in-software-product-lines/`; `https://arxiv.org/abs/2605.21353`; `https://link.springer.com/article/10.1007/s00163-023-00427-1`; `https://arxiv.org/abs/2510.11089`); information-hiding lineage carried by `C.31.RSA` | **Current standards and practice comparison plus information-hiding lineage:** the sources expose interface conformance, substitution, variability, extension, exception, assembly, and hidden-change pressures. | **Adapt as candidate prompts:** change the interface grammar, substitution policy, variation slot, evidence scope, exception boundary, or bearer only when the current architecture question needs it. | C.32 adds `interfaceGrammarChange`, `declaredScopeOrHolonLevelChange`, and `boundedException` as architecture-change kinds; the product-family worked case prepares interface-grammar change, evidence-scope split, and bounded exception as candidate alternatives. | Before a candidate is preferred, use `C.31.RSA` for reusable-structure accounting, `C.31.ASAP` for scale preference, `A.6.M` for interface grammar, `C.16` for measurement, `A.19.CPM` for comparison, `G.5` for selected-set result declaration, and `C.11` for local choice, as applicable to the current claim. |
| TRIZ ideality, Ideal Final Result, technical-system evolution regularities, and current FPF `C.19.1` BLP | **Historical heuristic lineage plus current FPF discipline:** older ideality language suggests useful candidate moves; BLP supplies the current scale-amenability rule. | **Use as lineage and adapt only as a candidate prompt:** transfer a function to an existing bearer, remove support bearers, use available resources, or try a more general bearer; judge the resulting candidate under current FPF rules. | C.32 adds `architectureIdealityPressureRef?`, `scaleAmenabilityPolicyRef?`, and `functionBearerConsolidation`; repair cues require function-bearing, affected architecture characteristics, losses, scale window, and BLP scale window or waiver when scale advantage is claimed. | An ideal-final-result slogan, fewer modules, or one universal module is not architecture adequacy, scale adequacy, or project architecture decision. |
| NAS survey line: Elsken, Metzen, and Hutter 2019 (`https://www.jmlr.org/papers/v20/18-598.html`); multi-objective differentiable NAS 2025 (`https://arxiv.org/abs/2402.18213`); hardware-aware NAS 2024 (`https://arxiv.org/abs/2404.12403`); Sutton's Bitter Lesson (`https://www.incompleteideas.net/IncIdeas/BitterLesson.html`) and scaling-law practice | **Current ML research and practice comparison:** functional graph search works under performance, resource, hardware, and transfer constraints. | **Adapt:** treat functional architecture as one selected structure and require bearer feasibility across module, deployment, resource, control, information, and evidence structures before comparison. | C.32 adds `functionBearerFeasibilityRef?`, `functionBearerFeasibilityRepair`, and didactic slices where a functional graph or method step fails because no bearer can carry it under current constraints. | A neural cell graph, function graph, benchmark winner, or scale curve is not holonic architecture adequacy unless selected structures and bearers are recovered. |
| Conway's law, mirroring, DORA loosely coupled teams (`https://dora.dev/capabilities/loosely-coupled-teams/`), and Team Topologies key concepts (`https://teamtopologies.com/key-concepts`) | **Current practitioner comparison with historical lineage:** these sources expose co-evolution and coordination pressure between organizational and technical structures without supplying a universal causal law. | **Adapt:** treat team, Work, responsibility, Method, toolchain, deployment, communication, evidence, and selected structures through their exact kinds; assert a direct influence relation only when its predicate is satisfied. Use inverse Conway only to generate a candidate change to selected influence-source structures. | C.32 adds `architectureInfluenceCorrespondenceRef?` and `architectureInfluenceCorrespondenceSynthesis`; use `C.32.CONWAY` for the synthesis-local frame or an exact pair row. Keep both architecture sides or modal claims, changed referent, any local system-role kind, classification or assignment, Work, module-interface, evidence, and mathematical-lens claims distinct. | Influence-source change, transformed-side change, joint change, and bounded mismatch remain candidate alternatives or comparison inputs. Architecture influence alone establishes no acting System, Work, or actual transformation. |
| MAAD 2025 (`https://arxiv.org/abs/2507.21382`) and LLM-assisted ADD 2025 (`https://arxiv.org/abs/2506.22688`) | **Current research comparison:** generated alternatives are practical, while the studies retain knowledge, trade-off, evaluation, and human-oversight limits. | **Adapt:** use AI outputs to widen candidate space, then recover source-side referent, selected structure, architecture-change kind, gain, loss, source-return condition, and pattern for the next question before palette admission. | C.32 Problem and Solution treat generated outputs as source cues; `sourceCueRefs?` and `sourceSideReferent?` prevent generated text from carrying an architecture-adequacy authority relation. | A generated blueprint, evaluation report, benchmark, or agent consensus is not an authority relation for architecture adequacy, evidence sufficiency, assurance, gate passage, or decision. |

**Source-currentness boundary.** Use each source row only for the C.32 candidate-generation move that the row transfers. If a named standard, guide, book edition, survey, or research line changes that move, recheck the row before using it again. If a receiving FPF pattern named in the row changes how it handles the source family, recheck the row before using it again. If the project needs comparison, selection, selected-set result declaration, actual publication, local choice, decision, evidence, or assurance, leave C.32 and open the pattern for the next question. Rows named as lineage, such as TRIZ ideality, information hiding, or mature DSM lineage, stay lineage until a current source relation is recovered.

### C.32:12 - Relations

- **Builds on:** `C.30` for the exact described holon, obtaining `ArchitectureRelation` occurrences, their selected `U.Structure` participants, and separately identified `ArchitectureClaim` content; `C.30.P`, `C.30.ASV`, `A.22`, `A.6.F`, `A.6.M`, `C.32.HCS`, `C.32.ACS`, `C.32.ACE`, `C.25`, `C.31`, `C.31.ASAP`, `C.16`, `C.16.P`, `E.22`, `E.23`, `C.19.1`, `C.30.LCA`, `C.30.TFS-REL`, `E.18`, `A.3.4`, `A.15`, and local patterns for recovering source-side architecture referents.
- **Uses:** `C.30.ILC` when a residual starts the candidate work; `C.32.MLAO` when residual-reducing multilevel framing is being used; `C.32.CONWAY` when exact influence-source and transformed-side architecture content must be co-synthesized without inferring acting, Work, or transformation facts; `C.32.FAIL` when a candidate needs repair before explicit comparison, selection, local choice, or decision; `C.32.ACE` when candidate eval results are needed before later comparison or selection; `C.33` when a source, description, view, decision record, eval report, handoff, or realized observation captures only part of selected structure; `C.34` when candidate or source structures need preservation adequacy or correspondence adequacy; `C.35` to recover the kind and assess the adequacy of a generated or discovered result before candidate palette use; `C.29` when mathematical-lens use is being claimed.
- **Patterns for the next questions:** `A.19.CPM` for explicit comparison claims, `A.19.SelectorMechanism` for set-returning selection claims, `G.5` for selected-set result declaration, `C.18` and `C.19` for archive, front, or pool-treatment policy, `C.11` for fixed local choice, `C.30.AD` for architecture-description work, `E.17` for a source-backed publication face and source return, `E.24.PUB` for the publication occurrence and audience availability, and `C.32.PAD` for project architecture decisions.
- **P2S docking:** `C.32.P2S` uses C.32 for the candidate-synthesis stages after problem pressure, selected structures, architecture characteristics, and structural uncertainty have been recovered; C.32 continues to define the candidate palette.
- **Routes to:** `C.32.MWA` when one usable practice-architecture answer must be synthesized from several structures that do not line up one-for-one; C.32 retains general candidate-palette construction.
- **Boundary:** Use C.32 to construct a candidate architecture palette for one grounded architecture question over selected structures of a described holon. C.35 may support C.32 by recovering a generated or discovered result's kind and assessing its adequacy for candidate-palette use, but C.35 does not select candidates, publish sets, or decide the project architecture. Evidence, assurance, gate, release, work authorization, Method rules, ethical mediation, and causal claims use their own patterns when those claims are being made.

### C.32:13 - Footer marker

Use `C.32` to construct a first useful palette of architecture candidate configurations for one grounded architecture question. Later front-policy, selected-set result declaration, actual publication, local choice, architecture-description, decision, gate, release, and authority-relation claims require their own definitions and tests.

### C.32:End

