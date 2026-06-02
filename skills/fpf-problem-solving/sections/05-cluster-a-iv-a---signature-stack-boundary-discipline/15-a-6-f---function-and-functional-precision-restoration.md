## A.6.F - Function and Functional Precision Restoration (RPR-FUNCTION)

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### A.6.F:1 - Problem frame

Use this pattern when `function`, `functional`, `functionality`, `effect`, or a similar function-like phrase carries a live FPF claim beyond ordinary prose. The claim kind may be architecture, work, method, capability, role, quality, mathematical, module-allocation, interface, decision, evidence, or gate.

The first useful move is small:

```text
FunctionUseRepair:
phrase:
liveUse:
recoveredCarrierKind:
recoveredCarrierRef?:
falseCarrierKindRefs:
nextAdmissibleMove:
stopCondition:
```
Stop when the recovered carrier kind, any needed carrier ref, false carrier kinds, and the next admissible move are clear.

What goes wrong if A.6.F is missed: a function becomes a root kind; functional architecture becomes a peer ontology beside architecture; a capability becomes a function; a method or work occurrence becomes a function; a mathematical function becomes design ontology; a module allocation becomes functional truth; or a quality claim hides behind "functionality".

What A.6.F buys in practice: the practitioner can keep useful engineering language while recovering the exact carrier and the exact governing pattern that carries any remaining claim kind.

Not this pattern when the phrase is ordinary prose and carries no live FPF claim. If the live issue is a general relation word rather than function-like wording, use A.6.P. If the live issue is evaluative language, use C.16.Q. If the live issue is architecture-description adequacy, use C.30. If the live issue is an architecture structural view, use C.30.ASV.

### A.6.F:2 - Problem

FPF texts repeatedly use function-like wording for different carriers:

- required transformation or effect in an architecture view;
- capability of a holon;
- method wording;
- work occurrence or work result;
- role expectation or responsibility;
- mathematical function or relation;
- quality, fitness, or characteristic wording;
- module allocation or interface relation;
- functional architecture shorthand.

These uses are all legitimate in ordinary engineering speech. They are not the same FPF kind. If the text does not recover the carrier, subsequent reasoning cannot tell whether the sentence is about architecture, behavior, work, role, mathematics, module structure, quality, evidence, or decision claim.

### A.6.F:3 - Forces

| Force | Tension |
| --- | --- |
| Familiar engineering speech vs kind precision | Engineers naturally say "function", "functional", and "functionality"; FPF needs the carrier and non-function claim kind recoverable when the phrase carries a live FPF claim. |
| Functional architecture vs peer ontology | Functional architecture is useful, but it is the `FunctionalStructure` case of `ArchitectureOf@Context`, not a separate root architecture kind. |
| Capability/effect vs work/method | A function-like phrase may describe what a holon can do, what a method prescribes, or what work has done; those are different FPF carriers. |
| Mathematical function vs design relation | Mathematical functions and relations can be used for reasoning, but C.29 governs their lens use and stop condition. |
| Module allocation vs functional relation | Functional dependencies may be allocated to modules, but function and module/interface structure do not become one object. |
| Small repair vs unneeded evidence, quality, decision, or assurance apparatus | Most cases need carrier recovery and a stop condition, not a full architecture, evidence, quality, or decision claim apparatus. |

### A.6.F:4 - Solution

A.6.F is an A.6.P RPR specialization for function-like wording. It does not mint `U.Function`. It assigns the live use to an existing carrier and stops there unless another claim kind remains live.

#### A.6.F:4.1 - Trigger rule

A.6.F applies when a sentence uses function-like wording to carry one or more live FPF claim kinds:

- architecture or functional architecture;
- capability, effect, externally promised behavior, or user-visible functionality;
- method wording, work occurrence, or work result;
- role expectation or responsibility;
- mathematical function, mapping, relation, loss, objective, or value functional;
- quality, fitness, characteristic, score, or proxy wording;
- module allocation, interface, signature, port, API, protocol, flow, or mechanism relation;
- evidence, assurance, gate, decision, or release claim.

If none of those claim kinds is live, the wording may remain ordinary Plain prose.

#### A.6.F:4.2 - FunctionUseRepair

`FunctionUseRepair` is a pattern-local repair note, not a project publication, not evidence, not a decision, and not `U.Function`. `FunctionalStructure` is an `ArchitectureStructureKindRef` value under C.30.ASV, not a kernel Function kind.

```text
FunctionUseRepair ::= {
  phrase,
  liveUse:
    requiredTransformationOrEffect |
    holonCapability |
    methodOrProcedure |
    workOccurrenceOrResult |
    roleExpectation |
    mathematicalFunctionOrRelation |
    qualityOrCharacteristic |
    moduleAllocation |
    interfaceOrSignatureRelation |
    functionalArchitecture |
    evidenceAssuranceGateDecisionClaim |
    otherDeclared,
  recoveredCarrierKind:
    FunctionalStructure |
    U.Capability |
    U.Method |
    U.MethodDescription |
    U.Work |
    MathematicalFunctionUnderC29 |
    QBundleSlot |
    ModuleAllocationRelation |
    InterfaceSpecification |
    RoleExpectation |
    EvidenceOrGateCue |
    otherDeclared,
  recoveredCarrierRef?,
  falseCarrierKindRefs,
  recordGoverningPatternRef,
  governingPatternApplicationRefs?,
  admissibleUse,
  nonAdmissibleUse,
  nextAdmissibleMove,
  stopCondition
}
```

The repair is complete when a practitioner can say which carrier kind the function wording uses, which carrier kinds it does not use, and what the next admissible architecture or exact governing pattern application is. If the text still hides a function/capability/work/method/role/module/mathematical-function collapse, the repair is incomplete.
#### A.6.F:4.3 - Repair assignments

| Function wording use | First carrier | Boundary |
| --- | --- | --- |
| required transformation or effect | `VP.Functional`, `FunctionalStructureView@Context`, or locally declared capability/effect record | Does not imply physical module, work occurrence, or evidence. |
| capability of a holon | `U.Capability` or the exact capability-governing pattern or project record named by the live claim | Does not imply that a method, module, or work occurrence exists. |
| method wording | `U.Method`, `MethodDescription`, `VP.Procedural`, or A.15 design/run boundary as triggered | Does not imply execution. |
| work occurrence or work result | `U.Work`, Work record, or P2W relation under the governing TGA work-result pattern | Does not imply reusable function ontology. |
| responsibility or role expectation | `VP.RoleEnactor` and the relevant role/enactor relation | Does not imply the role-holder performed the work. |
| mathematical function or relation | C.29 mathematical-lens use with domain, codomain or relation domain, preserved/lost structure, lens-use posture, and stop condition | Does not become architecture, evidence, causal proof, assurance, or decision claim by itself. |
| quality or fitness expression | `C.25`, `C.16`, `C.16.Q`, `A.17`, `A.18`, or an admitted characteristic/measurement receiving pattern according to the live claim | Does not let "functionality" carry a quality claim without bearer and exact governing pattern. |
| module allocation | `FunctionalStructureView@Context` plus declared correspondence, allocation, retargeting, or module/interface repair as live | Does not make function and module one object. |
| interface or signature relation | `InterfaceSignatureBoundaryNote`, A.6.0, A.6.5, A.6.B, A.6.C, A.6.8, or the exact module/interface repair pattern when live | Does not turn a functional link, port label, API name, or signature into implemented compatibility. |
| functional architecture | `ArchitectureOf@Context` with `structureKindRef = FunctionalStructure` and `FunctionalStructureView@Context` under C.30.ASV | Not a peer architecture ontology and not a TGA graph by itself. |

#### A.6.F:4.4 - Functional architecture boundary

Functional architecture is the `FunctionalStructure` case of `ArchitectureOf@Context`: the intensional organization of required transformations, capabilities, effects, functional dependencies, and constraints that a holon is to realize, before or alongside allocation to modules, roles, work, evidence, control relations, or flow/transduction descriptions.

```text
FunctionalArchitecture@Context shorthand expands to:
  ArchitectureOf@Context(
    describedHolonRef,
    boundedContextRef,
    structureKindRefs includes FunctionalStructure,
    structureRefs includes candidate:U.Structure refs for required transformations,
      effects, capabilities, dependencies, and constraints,
    admissibleUse,
    nonAdmissibleUse
  )
```

This shorthand is admissible only when the expanded C.30/C.30.ASV reading is recoverable. A TGA graph, path slice, crossing, or flow valuation may be related to functional structure through `C.30.TGA-FLOW-REL`, but it is not the functional architecture itself.

#### A.6.F:4.5 - Function-flow-module alignment note

Use this note when functional wording touches flow or module allocation but does not yet require a full structural view or module/interface repair.

```text
FunctionFlowModuleAlignmentNote:
required function or effect:
flow path or dependency:
proposed module allocation:
role, work, or evidence consequence:
known mismatch:
governingPatternApplicationRefs:
admissible use:
non-admissible use:
```

The note is a boundary and source-finding aid. It is not the functional architecture, not a module relation, not an implemented interface, not evidence sufficiency, and not an architecture decision.

#### A.6.F:4.6 - Common carrier separations

| Confusion | Repair |
| --- | --- |
| function = module | Keep `VP.Functional` and `VP.ModuleInterface` distinct; connect them through declared correspondence, allocation, retargeting, or module/interface repair. |
| function = capability | Capability belongs to a holon; function-like wording describes required transformation/effect or architectural relation only when that carrier is declared. |
| function = work | Work is a dated occurrence or result; function is design-side or description-side content unless work evidence is explicitly live. |
| function = method | Method is a reusable way of doing; function-like wording names required transformation/effect only when method carrier is not live. |
| function = role | Role/enactor structure uses `VP.RoleEnactor` and role records; function-like responsibility wording needs role carrier recovery. |
| mathematical function = system purpose | Use C.29 for mathematical function or relation; recover domain/codomain, preserved/lost structure, lens-use posture, and stop condition. |
| functional diagram = evidence | Diagram is a view or publication; evidence claim uses `A.10` or `G.6`. |
| functionality = quality | Recover the quality bearer and exact governing pattern through `C.25`, `C.16`, or C.16.Q before using the wording as an adequacy claim. |

#### A.6.F:4.7 - Composability and compositionality

Composability and quality compositionality are separate claims. If the text says parts can be assembled, keep that as a structure/use claim. If it says a whole-system quality follows from parts, assign the quality-composition claim to `C.25` and C.16-backed measurement or quality claim:

```text
Composability:
  "A and B can be assembled under interface X."
  recoveredCarrierKind: ModuleAllocationRelation | InterfaceSpecification
Quality compositionality:
  "The assembled whole preserves safety, latency, or reliability."
  recoveredCarrierKind: QBundleSlot | structuralCharacteristicSupportsQBundleSlot | structuralCharacteristicCausalHypothesisForQBundleSlot | structuralCharacteristicEvidenceSupportForQBundleSlot
Non-admissible:
  successful assembly is not quality propagation
```

Compositional formalisms may express explicit composition structures and view/model relations. They do not make safety, latency, reliability, or another quality propagate automatically.

```text
CompositionalityClaim@Quality ::= {
  affectedQBundleRef,
  partStructureRefs,
  wholeStructureRef,
  compositionRelation,
  lensUsePosture,
  nonAdmissibleUse
}
```

#### A.6.F:4.8 - Worked slices

**Functional architecture phrase.** A team says, "the functional architecture is the user journey." A.6.F does not let the phrase create a separate architecture kind. The repair is:

```text
FunctionUseRepair:
phrase: "functional architecture"
liveUse: functionalArchitecture
recoveredCarrierKind: FunctionalStructure
recoveredCarrierRef: ArchitectureOf@Context with structureKindRef = FunctionalStructure
falseCarrierKindRefs: user journey publication, work log, TGA graph, module diagram
nextAdmissibleMove: open C.30.ASV only if the selected functional structure changes action
stopCondition: ordinary phrase remains Plain if no architecture claim is live
```
**Functionality as quality.** A product note says, "new functionality improves adequacy." The repair separates added capability or effect from quality claim. Capability/effect wording may stay as recognition, but adequacy claim goes to `C.25`, `C.16`, C.16.Q, or an admitted characteristic/measurement receiving pattern when the claim is live. A.6.F stops after carrier recovery when no quality claim remains.

**Mathematical function or loss.** A model note says, "the loss function explains the system purpose." The repair keeps the mathematical function under C.29 lens discipline: domain, codomain or relation domain, preserved/lost structure, lens-use posture, and stop condition. The loss may inform a reasoning move; it does not become system purpose, evidence sufficiency, causal proof, assurance, or project decision by itself.

### A.6.F:5 - Archetypal Grounding

| Tell-Show-Show row | Grounding |
| --- | --- |
| Tell | A practitioner reads "the function", "functional architecture", or "this functionality" and needs to know whether the sentence is about capability, effect, method, work, role, module allocation, mathematical relation, quality, or architecture. A.6.F asks for the carrier before the phrase carries a live FPF claim. |
| Show: `U.System` | A robot, software system, plant, product platform, or AI-agent system may have capabilities, required effects, control functions, module allocations, runtime flows, and user-visible functionality. Those are not one object; A.6.F assigns each live use to its carrier. |
| Show: `U.Episteme` | A functional diagram, SysML view, architecture note, generated code architecture note, benchmark report, or mathematical model may publish or substantiate a function-like claim. The episteme or publication does not become the function, capability, work, evidence, or architecture. |

### A.6.F:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto/Epist**, **Prag**, **Did**, **Gov**. Scope: function-like wording that carries a live FPF claim across FPF.

| Bias risk | Mitigation |
| --- | --- |
| Function-root bias | The pattern explicitly does not mint `U.Function`; it assigns wording to existing carriers. |
| Functional-architecture exception bias | Functional architecture is normalized as `FunctionalStructure`, not a peer ontology. |
| Module bias | Function/module allocation uses correspondence or module/interface repair; function and module remain distinct. |
| Mathematical bias | Mathematical function wording is assigned to C.29 when used as a lens. |
| Check-only bias | Every conformance item carries a repair move or exact governing pattern application. |

This checklist verifies the preceding guidance after the practitioner has chosen the live move; it is not a required project control form and not a substitute for the card, note, view, relation, or repair move above.

### A.6.F:7 - Conformance Checklist


| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-A6F-1 Carrier-kind recovery.** | Every function-like phrase that carries a live FPF claim names the recovered carrier kind and, when the claim points to a specific object, the recovered carrier ref. | Add `FunctionUseRepair` or demote the phrase to Plain prose. |
| **CC-A6F-2 No `U.Function`.** | The use does not mint or rely on `U.Function` as a new root kind. | Assign the use to functional view, capability, method, work, role, mathematical lens, quality/characteristic, module allocation, or exact governing pattern. |
| **CC-A6F-3 Functional architecture expansion.** | Functional architecture expands to `ArchitectureOf@Context` with `structureKindRef = FunctionalStructure` and C.30.ASV when it carries a live architecture claim. | Add the expansion or keep the phrase as ordinary recognition wording. |
| **CC-A6F-4 Function/capability split.** | Capability claims and function/effect claims remain distinct. | Assign capability claims to the exact capability-governing pattern or project record named by the live claim and keep function/effect wording in the functional view or effect record. |
| **CC-A6F-5 Function/work/method split.** | Method, work occurrence, and work result claims do not hide inside function wording. | Assign the claim to `U.Method`, `MethodDescription`, `U.Work`, Work record, or A.15/P2W as live. |
| **CC-A6F-6 Function/role split.** | Responsibility or role expectation wording uses `VP.RoleEnactor` and role/enactor relations when live. | Add the role carrier or remove the role claim from the function phrase. |
| **CC-A6F-7 Mathematical function boundary.** | Mathematical function or relation wording used to justify reasoning names C.29 lens fields and stop condition. | Add C.29 lens-use posture, preserved/lost structure, and stop condition, or mark mathematical use as ordinary. |
| **CC-A6F-8 Quality/functionality boundary.** | Quality, fitness, characteristic, score, or "functionality" wording recovers bearer and exact governing pattern. | Assign the claim to `C.25`, `C.16`, C.16.Q, `A.17`, `A.18`, or an admitted characteristic/measurement receiving pattern as live. |
| **CC-A6F-9 Module/interface boundary.** | Functional relation, module allocation, interface, signature, port, API, protocol, flow, and mechanism wording remain separated. | Add `FunctionFlowModuleAlignmentNote`, `InterfaceSignatureBoundaryNote`, declared correspondence/allocation, or exact module/interface repair. |
| **CC-A6F-10 Useful action.** | The repair leaves a surviving admissible move: assign carrier, open functional view, add alignment note, assign the live claim to C.29/C.30/C.30.ASV/A.15/C.25/C.16/A.10/B.3/A.20/A.21/C.11, or stop. | Restore that move, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

### A.6.F:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Root function kind** | The text treats function as a new universal object. | Use `FunctionUseRepair` and assign the use to an existing carrier. |
| **Functional architecture exception** | Functional architecture is treated as a peer architecture ontology. | Expand to `FunctionalStructure` under `ArchitectureOf@Context` and C.30.ASV. |
| **Capability collapse** | What the holon can do is treated as a functional dependency or vice versa. | Split capability carrier from functional relation/effect carrier. |
| **Work collapse** | Work occurrence or result is described as a function. | Assign occurrence/result claims to A.15/P2W and keep functional wording design-side unless work evidence is live. |
| **Mathematical-function import** | A mathematical function, loss, objective, or value functional becomes design ontology. | Use C.29 and state preserved/lost structure plus stop condition. |
| **Module allocation shortcut** | A function is considered implemented because a module is named. | Add correspondence, allocation, interface/signature boundary, or module/interface repair. |
| **Functionality as quality proxy** | "Functionality" carries adequacy or quality claim without bearer and exact governing pattern. | Recover bearer and exact governing pattern through `C.25`, `C.16`, C.16.Q, or an admitted characteristic/measurement receiving pattern. |
| **Sterile carrier repair** | The wording is typed but no useful move remains. | Restore the carrier assignment, functional view, alignment note, or exact governing pattern application. |

### A.6.F:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| Function-like prose remains usable without minting `U.Function`. | Uses that carry live FPF claims need carrier recovery. |
| Functional architecture becomes a normal architecture-by-structure-kind case. | C.30/C.30.ASV may be needed when the phrase carries an architecture claim. |
| Capability, method, work, role, mathematical, quality, module, and interface claims stay separable. | A single familiar word may split into several records when several claim kinds are live. |
| C.29, C.25, C.16, A.15, C.30, and module/interface patterns receive the claims they actually govern. | A conforming use stops after carrier recovery when no further claim kind is live, instead of opening all possible exact governing patterns. |

### A.6.F:10 - Rationale

Function-like wording is too useful to ban and too overloaded to leave ungoverned. The smallest useful repair is not a new ontology. It is carrier assignment: say what kind of thing the phrase is about, what it is not about, and what move remains admissible.

This design follows A.6.P: trigger phrase, carrier recovery, explicit relation fields and exact governing pattern fields, and lexical guardrails. It also follows C.30: functional architecture is selected structure for a described holon, not a peer of architecture and not a TGA graph by itself.

The pattern keeps ordinary language alive. A phrase can remain Plain when it carries no live FPF claim. When it carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim kind, the carrier and exact governing pattern application are recoverable.

### A.6.F:11 - SoTA-Echoing

| Practice or source line | A.6.F adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022 architecture-description discipline | Adapt view/concern discipline to functional architecture as a structure-kind view over an architecture claim. | Functional architecture expands through C.30 and C.30.ASV rather than becoming a separate ontology. | ISO terminology does not mint `U.Function` or turn diagrams into architecture. |
| OMG SysML v2 and KerML behavior/view practice | Adapt function/behavior/model-view separation as practice basis for functional-view recovery. | Functional views name selected functional structure and keep flow, module, and work relations separate. | SysML/KerML model elements do not override FPF carriers or import tool ontology. |
| INCOSE systems-engineering and MBSE functional-analysis practice | Adopt the practical need to separate function, requirement, behavior, physical allocation, and verification claim kinds. | A function-like phrase can guide architecture work only after capability/effect, allocation, evidence, and verification claim kinds are separated. | Functional analysis practice is not evidence sufficiency, assurance, gate passage, or project decision by itself. |
| ISO/IEC 25010 quality-model practice | Treat functionality/functional suitability as quality wording when it evaluates a product or service. | Assign quality-like uses to C.25/C.16/C.16.Q before they carry adequacy claims. | "Functionality" is not a free adequacy score and not a functional architecture record. |
| C.29 mathematical-lens discipline | Adopt domain/codomain or relation-domain, preserved/lost structure, lens-use posture, and stop condition for mathematical function use. | Mathematical function wording becomes lens-governed only when C.29 fields are recoverable. | Mathematical functions, objectives, and value functionals do not become system purpose, evidence, causal proof, assurance, or decision claim by themselves. |
| GonzoML neural-network architecture discussions | Adapt practitioner operation language involving blocks, activations, path-selection, memory/cache, loss functions, pruning, ablation, and architecture search as recognition material. | Function-like neural-network claims require carrier recovery: mathematical function, flow relation, module/interface claim kind, capability/effect, quality characteristic, or decision/evidence governing pattern. | Neural-network labels and benchmark results do not become FPF ontology, architecture decision, evidence sufficiency, gate passage, or assurance by themselves. |

### A.6.F:12 - Relations

Builds on: `A.6.P`, `A.6.0`, `A.6.5`, `A.6.B`, `A.6.C`, `A.6.8`, `A.6.9`, `A.7`, `E.10`, `C.2.P`, `F.18`, and `E.8`.

Coordinates with: `C.30`, `C.30.ASV`, `C.30.TGA-FLOW-REL`, `E.18`, `A.15`, `A.2`, `C.29`, `C.25`, `C.16`, `C.16.Q`, `A.17`, `A.18`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `C.11`, and the exact module/interface repair pattern when module or interface claim kind is live.

Does not replace: C.30 architecture-description adequacy, C.30.ASV architecture structural-view adequacy, E.TGA graph/path/crossing discipline, C.29 mathematical-lens adequacy, C.25 Q-Bundles, C.16 characterization, A.15 work/method discipline, A.10/G.6 evidence, B.3 assurance, A.20/A.21 gate/release records, or C.11 decisions.

### A.6.F:End

