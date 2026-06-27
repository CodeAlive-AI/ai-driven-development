## C.32.PAD - Project Architecture Decision After Candidate Synthesis

> **Type:** Architecture decision pattern under C.32
> **Status:** Draft
> **Normativity:** Normative unless explicitly marked informative

### C.32.PAD:1 - Problem frame

Use this pattern when a project has synthesized candidate architecture configurations and must make the project architecture decision that will guide later design, implementation, construction, operation, governance, or change work.

Primary working reader: an architect or architecture-responsible practitioner who has enough candidate synthesis, comparison input, and architecture-characteristic pressure to decide what architecture will be pursued now.

Typical entry phrases:

```text
"We have three candidate architecture configurations; which one becomes the project decision?"
"The candidate improves maintainability but worsens evidence reuse; what is the accepted trade-off?"
"Developers need to know which architectural style, method, or pattern use is now required."
"The architecture decision must say where architect-owned structure ends and developer-owned refinement starts."
"The ADR cannot be written yet because the decision relation is not clear."
```

**First-minute use slice.** A product-family architect has a C.32 candidate palette with three module, placement, and evidence-structure variants. C.32.ACS names maintainability, substitutability, and evidence reuse as optimization indicators, and C.32.ACE has evaluated the candidates under one parity frame. Using C.32.PAD, the architect records the selected configuration, the affected selected structures, the accepted loss in evidence reuse, the method-use instruction for product teams, the work split between architecture-owned structure and team-owned refinement, the source-return condition, and the reopen trigger. The result is not an ADR file yet; it is the project architecture decision relation that an ADR or another publication form can describe.

The primary `EntityOfConcern` is `ArchitectureDecisionRelation@Project`: a project-scoped decision relation over one bounded architecture question. It links the decision subject, candidate basis, selected architecture option, affected structures, architecture characteristics, rationale, accepted losses, consequences, method and work expectations, publication projection, evidence or eval exits, and reopen conditions.

`ArchitectureDecisionRelation@Project` is not a new `U.*` kind. It is a non-U project relation with filled slots. When a slot becomes load-bearing as an FPF object, recover the governing pattern for that object.

What goes wrong if C.32.PAD is missed: a team writes an architecture record, diagram, shortlist, ranking, or local choice without a recoverable project decision relation. Later workers cannot tell which architecture configuration is selected, which structures are affected, which method they must use, which losses were accepted, or when the decision must be reopened.

What C.32.PAD buys in practice: the project can turn a candidate palette into one governed decision relation that is strong enough to guide work, publish an ADR-like record, support review, and reopen under architecture evolution.

Ordinary working move: recover the live decision question, cite the candidate basis, select the architecture option or bounded exception, record the trade-off over declared architecture characteristics, then bind the decision to method-use expectations, work split, source-return, and reopen conditions.

Adoption test: after using C.32.PAD, another practitioner can answer: what architecture option was selected, from which candidate basis, for which affected structures, under which architecture-characteristic trade-off, with which method and work consequences, and under which reopen condition.

Not this pattern when the current work is candidate synthesis, architecture-description adequacy, ADR publication projection, adequacy evaluation, evidence, assurance, gate passage, local choice, or performed work. Use the receiving pattern named in `Relations` for those claims.

The first useful output is `ArchitectureDecisionRelation@Project`:

```text
ArchitectureDecisionRelation@Project:
  decisionId:
  decisionSubjectRef:
  describedHolonRef:
  boundedContextRef:
  decisionQuestion:
  candidateBasisRefs:
  comparisonOrSelectionRefs?
  structuralInformationLensUseRefs?
  holonTransitionOrBOSCTriggerRefs?
  transformerTransformedCorrespondenceRef?
  selectedArchitectureOptionRefs:
  selectedStructureEffects:
    - structureKindRef:
      selectedStructureRef:
      decisionEffect:
      governingPatternRef:
  architectureCharacteristicTradeoffs:
    - architectureCharacteristicRef:
      criteriaRowRef?
      expectedGain:
      acceptedLoss:
      evalResultRef?
      guardrailRef?
  rationaleRefs:
  rejectedOptionRefs:
  consequenceRows:
  architectureDescriptionRefs:
  methodUseInstructions:
    - methodDescriptionRefOrPatternRef:
      expectedStructureEffect:
      responsibleRoleRef:
      workBoundaryRef:
      readinessOrGateExitRef?
  architectDeveloperSplit:
    architectOwnedStructureRefs:
    developerOwnedRefinementRefs:
    sourceReturnCondition:
  publicationProjectionRef?
  evidenceOrAssuranceExitRefs?
  governanceExitRefs?
  reopenConditions:
  supersedesDecisionRefs?
  status:
```

The field names in this first-output form are publication-friendly filled-reference fields. Durable relation positions must be expressible through `A.6.5` SlotSpecs: each position has a local `SlotKind`, an admitted `ValueKind`, and a by-value or concrete `RefKind` filling mode. A field name such as `decisionSubjectRef` is not a SlotKind, not a U-kind, and not an ADR heading; it is the filled-reference field by which this project instance points to the value governed by the slot-bearing relation.

### C.32.PAD:2 - Problem


Architecture synthesis produces candidates; project work still needs a decision. The decision is not the candidate palette, not the selected set publication, not the architecture description, and not the ADR file. It is the project relation that says which architecture option is now pursued and what follows from that selection.

The problem is difficult because architecture decisions sit between structures and methods. Architecture descriptions describe selected structures of the target holon. A project architecture decision can also tell developer roles which method description, architectural style, pattern use, or work boundary they must follow so that later work produces or preserves the intended structures. For example, "use the client-server style here" is a method-use instruction whose intended result is a module and interaction structure of the target system. The decision relation must keep both sides visible: intended structure of the transformed holon and method expectations for the transformer holon.

The problem is also multilevel. The architect may decide selected structures at one holon level while developers later refine lower-level structures. A decision must therefore say where the architect-owned architecture claim stops, where developer-owned refinement starts, which source detail must remain recoverable, and which result can reopen the decision. If that boundary is missing, architecture governance becomes either empty advice or uncontrolled micro-management.

Finally, architecture decisions are evolutionary. They are made under current candidate knowledge, current characteristic criteria, current eval readings, and current organization or tool constraints. They should be explicit enough for present work and cheap enough to supersede when a better candidate, changed characteristic pressure, or transformer-transformed mismatch appears.

C.32.PAD solves the post-synthesis decision problem by making the decision relation explicit before any ADR-like publication projection is written.

### C.32.PAD:3 - Forces

| Force | Tension |
|---|---|
| Candidate plurality | Several candidate configurations can be valid under different trade-offs, while project work needs one current direction or a bounded exception. |
| Trade-off visibility | Architecture characteristics compete; a decision that hides accepted losses cannot be responsibly executed or reopened. |
| Structure and method coupling | The decision must govern intended structures of the target holon and may also prescribe developer methods that produce those structures. |
| Work split | Architect-owned structure and developer-owned refinement must be separated without severing source return. |
| Evolution | A decision must close enough work for now while staying reopenable when context, eval readings, or candidates change. |
| Publication pressure | Teams often want an ADR file before the decision relation is recoverable. |

### C.32.PAD:4 - Solution

Create `ArchitectureDecisionRelation@Project` before writing an ADR-like publication record. Treat it as the project decision relation that binds candidate basis, selected architecture option, affected structures, architecture-characteristic trade-offs, rationale, consequences, method expectations, work split, and reopen conditions.

Work in this order:

1. Name the decision subject: described holon, bounded context, decision question, and status.
2. Cite the candidate basis. Use `C.32` for the candidate palette, `C.32.MLAO` for residual-reducing multilevel candidate frames, `C.32.CONWAY` when transformer and transformed structures were synthesized together, and `C.32.FAIL` for repaired candidate errors.
3. Cite comparison or selection input only when it exists. Explicit comparison belongs to `A.19.CPM`; set-returning selection belongs to `A.19.SelectorMechanism`; selected-set publication belongs to `G.5`; local choice belongs to `C.11`.
4. State the selected architecture option or bounded exception. Name the affected selected structures and the governing pattern for each structure claim.
5. Record the architecture-characteristic trade-off. Use criteria rows from `C.32.ACS`, eval results from `C.32.ACE`, measurement support from `C.16`, Q-Bundles from `C.25`, modularity or scale support from `C.31`, and `C.29` structural-information lens uses for compressed recoverable structure, accepted description loss, hidden dependency, and source-return. None of those lenses, measures, or bundles decides the architecture by itself.
6. Record rationale, rejected options, accepted losses, and consequences. A rejected option can remain useful as a stepping stone or archive item; do not turn it into a failure unless the receiving failure pattern is triggered.
7. Bind the decision to architecture descriptions. Use `C.30.AD` for architecture-description adequacy and `C.30.ASV` for selected-structure view adequacy. A diagram, model, file, or view can describe the decision basis; it does not become the decision relation.
8. Bind the decision to method-use instructions when the architect needs developers to use a method, pattern, style, toolchain step, or work practice so the target holon gains the intended structure. Use `A.15`, `A.15.1`, `A.15.2`, `A.15.5`, `A.6.M`, `E.8`, `E.11.PUR`, and `C.24` according to the live claim.
9. State the architect-developer split. Name architect-owned selected structures, developer-owned refinement objects, source-return conditions, readiness exits, and governance exits. When the split depends on holon level, changed whole, or BOSC-triggered boundary pressure, fill `holonTransitionOrBOSCTriggerRefs?` through `B.2.P` claim-kind recovery or `B.2` whole reidentification instead of leaving a generic level note.
10. Choose a publication projection only after the decision relation is clear. Use `C.32.ADR` for ADR-like publication projection; use `E.17` and `E.24.PUB` for publication-face and publication-use claims.
11. Add evidence, assurance, gate, and governance exits only when those claims are being made. Use `A.10`, `B.3`, `A.21`, and the local governance pattern rather than adding those statuses to the decision relation by name.
12. Write reopen and supersession conditions. Reopen when the candidate basis changes, a protected architecture characteristic crosses its guardrail, the transformer structure can no longer produce the transformed structure, a stronger source changes the accepted loss, or the decision's method-use instruction proves unusable.

#### C.32.PAD:4.1 - Decision readiness

A C.32.PAD decision is ready to draft when the current decision relation can cite at least one candidate basis, one affected selected structure, one architecture-characteristic trade-off or declared reason for no live trade-off, one expected work consequence, one reopen condition, and any triggered `holonTransitionOrBOSCTriggerRefs?` or `structuralInformationLensUseRefs?` needed to preserve source return.

If the candidate basis is absent, return to `C.32`. If architecture-characteristic rows are absent, return to `C.32.ACS` or `C.25`. If the decision only says "the metric is best", return to `C.32.ACE`, `C.16`, or `A.19.CPM` before deciding. If the intended work method is not recoverable, return to `A.15`.

#### C.32.PAD:4.2 - Constructive architecture decision path

Some architecture decisions are constructive: they prescribe methods that, when used by developer roles, produce or preserve the intended structures. Admit that path only when the decision names:

- the architecture claim or selected structure to be produced or preserved;
- the method description, architectural style, pattern use, or work practice to be used;
- the developer role or transformer holon expected to use it;
- the expected structure effect on the transformed holon;
- the work-planning boundary and readiness or gate exit;
- the source-return condition and reopen trigger.

This keeps architecture decisions connected to work without treating the decision description, ADR file, method description, or performed work as the architecture itself.

#### C.32.PAD:4.3 - Minimum sufficient relation and slot-change impact

A small complete PAD instance can be this short:

```text
ArchitectureDecisionRelation@OrderFlow:
  decisionSubjectRef: order-integration architecture for product-family Q3
  describedHolonRef: product-family order-flow system
  candidateBasisRefs: [C32CandidatePalette:order-flow-2026-06]
  selectedArchitectureOptionRefs: [event-carried integration with payment exception]
  selectedStructureEffects:
    - structureKindRef: module structure
      selectedStructureRef: order events between service modules
      decisionEffect: preserve service substitutability, accept added event-schema governance
      governingPatternRef: C.30.ASV
  architectureCharacteristicTradeoffs:
    - architectureCharacteristicRef: substitutability
      expectedGain: service replacement without order-flow rewrite
      acceptedLoss: additional schema-version coordination
      guardrailRef: version-skew eval band
  methodUseInstructions:
    - methodDescriptionRefOrPatternRef: event-schema change method
      expectedStructureEffect: compatible event contracts across service modules
      responsibleRoleRef: service-team developer role
      workBoundaryRef: team-owned schema refinement after architect-owned event boundary
  architectDeveloperSplit:
    architectOwnedStructureRefs: [event boundary, payment exception]
    developerOwnedRefinementRefs: [schema fields inside approved event boundary]
    sourceReturnCondition: return to PAD when refinement changes event boundary or version-skew band
  holonTransitionOrBOSCTriggerRefs?: [B.2.P: no new operational whole claimed for team-local schema refinement]
  structuralInformationLensUseRefs?: [C.29: event-flow view compresses deployment and rollout structure; source-return keeps model refs recoverable]
  publicationProjectionRef?: C.32.ADR:order-flow-adr
  reopenConditions: [payment latency guardrail crossed, schema-version coordination cost guardrail crossed]
  status: acceptedForDeveloperWork
```

When a filled field changes, repair the smallest owner that governs the changed content:

| Changed filled field | Immediate repair locus |
|---|---|
| `candidateBasisRefs` or `selectedArchitectureOptionRefs` | Return to `C.32`, `C.32.MLAO`, comparison or selection inputs, then update PAD before ADR projection. |
| `selectedStructureEffects` | Repair the architecture claim or selected-structure view in `C.30`, `C.30.AD`, or `C.30.ASV`; then update PAD consequences. |
| `architectureCharacteristicTradeoffs` | Repair `C.32.ACS`, `C.32.ACE`, `C.25`, `C.16`, or comparison input before relying on the decision. |
| `methodUseInstructions` or `architectDeveloperSplit` | Repair method, work, role, readiness, and work-boundary claims through `A.15` family, `E.8`, `E.11.PUR`, or `C.24`. |
| `holonTransitionOrBOSCTriggerRefs?` | Use `B.2.P` for wording and claim-kind recovery; use `B.2` only when the decision depends on whole reidentification. |
| `structuralInformationLensUseRefs?` | Use `C.29` to state which structure is preserved, compressed, hidden, or recoverable; return to source when the accepted loss changes. |
| `publicationProjectionRef?` | Repair only the publication projection through `C.32.ADR`, `E.17`, or `E.24.PUB`; do not rewrite the decision by template pressure. |
| `reopenConditions` or `supersedesDecisionRefs?` | Update PAD and the active ADR-like projection; old decisions remain historical unless a governed archival policy says otherwise. |

### C.32.PAD:5 - Archetypal Grounding


**Software service architecture.** A platform team compares synchronous service calls, event-carried integration, and a bounded shared kernel. The selected option is event-carried integration for order events with a bounded exception for payment authorization. C.32.PAD records affected module and information structures, latency and substitutability trade-offs, the method-use instruction for service teams, the event-schema source-return condition, and the reopen trigger when payment volume crosses the declared eval band.

**Manufacturing fixture architecture.** A production architect compares a dedicated fixture per product, a universal fixture with adapters, and a mixed cell layout. The selected option uses a universal fixture only for products inside a scale window. C.32.PAD records module, placement, maintenance, and evidence-structure effects, the accepted setup-time loss, the method instruction for cell design, and the trigger for returning to candidate synthesis when adapter complexity exceeds the guardrail.

**Method-family architecture.** A review-method owner compares role-specialized review, peer rotation, and tool-supported triage. The selected option uses peer rotation plus a tool-supported evidence handoff. C.32.PAD records role, method, evidence, and information structures, the trade-off between teachability and evidence custody, and the developer-owned refinement boundary for local checklists.

**Transformer and transformed holons.** An automation program changes both the toolchain that transforms products and the product architecture being transformed. C.32.CONWAY supplies the correspondence frame. C.32.PAD records which toolchain structure is required to produce the target product structure and which mismatch will reopen the decision.

**Digital-twin structural information loss.** A built-asset team publishes a 6D-style digital-twin decision view for construction planning. The view intentionally hides supplier-contract and temporary-work structures. C.32.PAD records the selected building, placement, schedule, cost, operation, and evidence structures that the decision uses; `C.29` records which hidden structures remain recoverable and which accepted loss reopens the decision. The view count, file, and model do not become the decision authority.

### C.32.PAD:6 - Bias-Annotation

| Risk handled | How C.32.PAD handles it |
|---|---|
| Record-before-decision drift | The pattern requires `ArchitectureDecisionRelation@Project` before ADR-like publication projection. |
| Description-as-decision drift | Architecture descriptions remain `C.30.AD` objects; PAD records the decision relation that may cite them. |
| Metric-winner drift | Eval readings and metrics can inform trade-offs but do not select or decide by themselves. |
| Method-structure collapse | Method-use instructions and intended target structures are both recorded and kept distinct. |
| Work-split loss | Architect-owned structures, developer-owned refinement, and source-return conditions are explicit. |
| Evolution lock-in | Supersession and reopen conditions are part of the decision relation. |

### C.32.PAD:7 - Conformance Checklist

| Requirement | Required result |
|---|---|
| `CC-PAD-1` | The decision subject, described holon, bounded context, and decision question are explicit. |
| `CC-PAD-2` | The decision cites candidate basis from `C.32` or a named receiving candidate pattern, or states why no candidate-set question is live. |
| `CC-PAD-3` | The selected architecture option or bounded exception is named. |
| `CC-PAD-4` | Affected selected structures are named with governing pattern refs. |
| `CC-PAD-5` | Architecture-characteristic trade-offs, accepted losses, and guardrails are recorded. |
| `CC-PAD-6` | Architecture-description refs, method-use instructions, and performed-work boundaries remain distinct. |
| `CC-PAD-7` | The architect-developer split, source-return condition, and reopen conditions are recorded. |
| `CC-PAD-8` | Triggered holon-transition or BOSC boundary pressure cites `B.2.P` or `B.2`, and structural-information loss or compression cites `C.29`. |
| `CC-PAD-9` | ADR-like publication, evidence, assurance, gate, comparison, selection, selected-set publication, local choice, and work claims exit to their receiving patterns. |

### C.32.PAD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| `ADRBeforeDecisionRelation` | The team starts from an ADR template and fills prose before the selected option, trade-off, and work consequences are recoverable. | Draft `ArchitectureDecisionRelation@Project` first; then use `C.32.ADR` only as publication projection. |
| `CandidateWinnerByMetric` | One score, benchmark, or eval reading is treated as the architecture decision. | Return to `C.32.ACS`, `C.32.ACE`, `C.16`, and `A.19.CPM`; decide only after trade-offs and accepted losses are recorded. |
| `StructureOnlyDecision` | The decision names a target structure but gives no method-use or work-split instruction for those who must realize it. | Add method-description or pattern-use refs, responsible roles, work boundary, readiness exit, and expected structure effect; use `A.15` for work claims. |
| `MethodOnlyDecision` | The decision says which style, pattern, or tool to use but not which target structures it is expected to produce or preserve. | Name the intended selected structures and architecture-characteristic trade-offs; return to `C.30`, `C.30.ASV`, or `C.32` if the structure is not recoverable. |
| `FrozenArchitectureDecision` | The decision has no source-return or reopen condition. | Add eval guardrails, source-currentness return, transformer-transformed mismatch trigger, or supersession rule. |
| `LensOrQBundleAsDecisionAuthority` | A view, structural-information lens, measurement row, Q-Bundle, or eval reading is treated as if it selected the architecture. | Return the source to its owner: `C.29` for lens use, `C.25` for Q-Bundle, `C.16` for measurement, `C.32.ACE` for eval, and PAD for the actual decision relation. |
| `GovernanceByImplication` | Teams are expected to follow the decision, but no readiness, gate, evidence, assurance, or governance exit is named. | Add the exact receiving pattern refs; do not import those statuses into PAD. |

### C.32.PAD:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| The project decision relation is explicit before publication. | ADRs, design memos, and governance files can describe a recoverable decision rather than inventing one. | The architect must do decision work before documentation work. |
| Structure and method are coupled without collapsing. | Developers can see both intended architecture structures and required methods. | The decision record needs enough detail to avoid empty method instructions. |
| Trade-offs and accepted losses are recorded. | Later teams can reopen the decision under changed characteristics instead of guessing the original rationale. | Decisions may look less tidy because loss is visible. |
| Architect-developer split is stated. | Team refinement can proceed without losing source return. | Architecture governance must maintain split and reopen conditions. |

### C.32.PAD:10 - Rationale

C.32.PAD exists because candidate synthesis and architecture decision are different work moments. C.32 builds the option space; PAD commits the project to a current architecture option or bounded exception and records the method and work consequences of that commitment.

The pattern keeps three objects apart: `ArchitectureOf@Context` as the architecture claim over structures, `ArchitectureDecisionRelation@Project` as the project relation that selects and obligates, and `ArchitectureDecisionDescription@Project` as the description that can be published in ADR-like or other forms. This lets FPF reuse its existing description, method, work, evidence, assurance, measurement, and publication patterns instead of creating a separate architecture-only duplicate ontology.

The pattern is holonic because the same decision relation can apply to systems, organizations, methods, roles, built assets, AI-agent workflows, evidence practices, or other admitted holon kinds after affected structures, bearers, roles, and work boundaries are rebound.

### C.32.PAD:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.PAD. Keep a source citation only when it changes a decision-relation field, boundary, or reopen condition.

| Source to inspect | Why this source is load-bearing here | Transfer into PAD | Concrete PAD mutation | Blocked overread |
|---|---|---|---|---|
| ISO/IEC/IEEE 42010:2022 official standard (`https://www.iso.org/standard/74393.html`; IEEE page `https://standards.ieee.org/ieee/42010/6846/`) | Current official source for architecture-description requirements; it explicitly scopes itself to AD structure and expression, not architecting methods or the architecture itself. | Keep architecture descriptions as description objects and use PAD for the decision relation that may cite them. | PAD has `architectureDescriptionRefs`, selected-structure effects, and source-return conditions rather than treating a view, viewpoint, file, or model as the decision. | ISO 42010 architecture-description structure does not replace C.32 synthesis, A.15 method work, or PAD decision relation. |
| Michael Nygard, `Documenting Architecture Decisions` (`https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions`) | Practitioner source for small, statused records that preserve context, decision, and consequences across time. | Use context, decision, status, consequences, and supersession as publication-relevant decision-description fields. | PAD requires status, consequences, and supersession or reopen conditions before ADR projection. | ADR records are not the project decision relation and do not by themselves ground selected structures. |
| MADR 4.x (`https://adr.github.io/madr/`) | Current ADR practice with options, outcome, status, links, and confirmation pressure. | Require candidate basis, outcome, decision status, links to related decisions, and confirmation or eval exits. | PAD separates candidate basis, selected option, consequence rows, method-use instruction, and reopen conditions. | MADR's broad "any decision" use is not imported as FPF architecture-decision ontology. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`) | Current practitioner source for guided incremental architecture change and source-side fitness-function wording. | Treat eval support as `C.32.ACE` inputs and reopen conditions, not as the decision itself. | PAD requires eval refs, guardrails, and reopen conditions when evolutionary feedback guides the decision. | Fitness-function terminology is not imported as an FPF object name. |
| Ford, Richards, Sadalage, and Dehghani, `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Current practitioner source for trade-offs, least-worst choices, and architecture characteristics under uncertainty. | Make accepted losses and protected counter-characteristics mandatory decision content. | PAD records architecture-characteristic trade-offs, rejected options, accepted losses, and consequences. | A trade-off discussion does not replace candidate synthesis, comparison, evidence, or governance. |
| NASA Systems Engineering Handbook, decision analysis and trade-study practice (`https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf`) | Non-software engineering source for alternatives, selection criteria, assumptions, limitations, recommendation, impacts, and final decision documentation. | Generalize PAD beyond software ADR practice by requiring candidate basis, selection criteria or comparison refs, assumptions or accepted losses, impacts, and decision-maker commitment. | PAD carries `candidateBasisRefs`, `comparisonOrSelectionRefs?`, trade-offs, consequence rows, status, and reopen conditions for engineering decisions such as fixtures, vehicles, built assets, or methods. | NASA trade-study process is not imported as FPF architecture ontology and does not by itself decide the architecture. |
| Conway and Team Topologies source line, mediated through `C.32.CONWAY` | Architecture of the transformer holon and transformed holon can constrain each other. | Use correspondence as decision content when work organization, method, toolchain, or team structure must fit target architecture. | PAD may cite `transformerTransformedCorrespondenceRef` and reopen on mismatch. | Team structure is not automatically the target holon's architecture; correspondence must be recovered through C.32.CONWAY. |
| Current FPF `A.15`, `E.8`, `E.11.PUR`, `C.30.AD`, `C.32`, `C.32.ACS`, `C.32.ACE`, `C.32.ADR`, and `C.32.ADA` | Existing FPF ontology for method descriptions, pattern use, architecture descriptions, candidate synthesis, evals, publication projection, and adequacy evaluation. | Keep PAD narrow: decision relation after candidate synthesis. | Relation and conformance rows send neighboring claims to their governing patterns. | PAD does not duplicate FPF method, publication, evidence, assurance, or pattern-form doctrine. |

**Source-currentness boundary.** Recheck a source row when an ADR template, architecture-description standard, evolutionary-architecture practice, FPF pattern, or project governance practice changes the decision field, method-work boundary, or reopen condition that PAD uses.

### C.32.PAD:12 - Relations

- **Builds on:** `C.30`, `C.30.ASV`, `C.30.AD`, `C.32.P2S`, `C.32`, `C.32.MLAO`, `C.32.ACS`, `C.32.ACE`, `C.32.CONWAY`, `C.32.FAIL`, `C.25`, `C.16`, `C.29`, `C.31`, and `C.31.ASAP`.
- **Comparison and selection boundary:** `A.19.CPM` compares, `A.19.SelectorMechanism` returns a selected set, `G.5` publishes a selected set, and `C.11` governs local choice. PAD records the project architecture decision relation after those inputs are sufficient.
- **Description boundary:** `C.30.AD` and `C.30.ASV` govern architecture-description and selected-structure view adequacy. PAD may cite those descriptions but does not replace them.
- **Structural-information boundary:** `C.33`, `C.34`, and `C.35` may support PAD only for captured structure, lost structure, preservation adequacy, generated-carrier typing, or discovered-carrier typing used by the decision relation. PAD keeps decision relation, rationale, consequences, accepted losses, method consequences, work consequences, source-return, repair ownership, and supersession ownership.
- **Publication boundary:** `C.32.ADR` projects an `ArchitectureDecisionDescription@Project` into ADR-like form. `E.17` and `E.24.PUB` govern publication faces and publication-use claims.
- **Adequacy boundary:** `C.32.ADA` evaluates a PAD decision relation, method docking, and publication projection for a declared use.
- **P2S docking:** P2S reaches PAD only when implementation commitment is live; PAD records the decision relation and returns reopen conditions to P2S when actual structures, eval results, or source-return change the architecture question.
- **Method and work boundary:** `A.15`, `A.15.1`, `A.15.2`, `A.15.5`, `E.8`, `E.11.PUR`, and `C.24` govern method descriptions, work plans, readiness, pattern-use recommendations, and agentic tool-use work.
- **Evidence, assurance, and gate boundary:** `A.10`, `B.3`, and `A.21` govern evidence relations, assurance calculus, and gate profiles when those claims are current.

### C.32.PAD:13 - Footer marker

C.32.PAD closes when `ArchitectureDecisionRelation@Project` names the decision subject, candidate basis, selected architecture option or bounded exception, affected structures, architecture-characteristic trade-offs, accepted losses, rationale, consequences, architecture-description refs, method-use and work-split expectations, source-return condition, triggered holon-transition or BOSC refs, triggered structural-information lens uses, publication projection exit, and reopen or supersession conditions.

### C.32.PAD:End

