## A.6.F - Function and Functional Precision Restoration (RPR-FUNCTION)

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### A.6.F:1 - Problem frame

Use this pattern when `function`, `functional`, `functionality`, `effect`, or a similar function-like phrase carries an FPF claim being made beyond ordinary prose. The claim kind may be architecture, work, method, capability, role, quality, mathematical, module-allocation, interface, or another FPF claim named by value.

The first useful move is small:

```text
FunctionUseRepair:
phrase:
sourceCueText?:
claimKindUnderRepair:
recoveredValueKindRefs?:
recoveredRelationRecordRefs?:
recoveredSlotRefs?:
recoveredViewRecordRefs?:
recoveredFpFReferenceRefs?:
directGoverningPatternApplicationRefs?:
blockedLocalOverreadRefs:
nextAdmissibleUse:
stopCondition:
```
Stop when the source cue, recovered value-kind refs, relation-record refs, slot refs, view-record refs, needed FPF reference refs, direct governing-pattern applications, the one local overread that would change this repair, and the next admissible use are clear.

What goes wrong if A.6.F is missed: a function becomes a root kind; functional architecture becomes a peer ontology beside architecture; a capability becomes a function; a method or work occurrence becomes a function; a mathematical function becomes design ontology; a module allocation becomes functional truth; or a quality claim hides behind "functionality".

What A.6.F buys in practice: the practitioner can keep useful engineering language while recovering the FPF value kind, relation record, slot reference, view record, or governing pattern named by value for any remaining claim kind.

Not this pattern when the phrase is ordinary prose and carries no FPF claim being made. If the issue under repair is a general relation word, evaluative language, grounded architecture adequacy, or an architecture structural view, use `A.6.P`, `C.16.Q`, `C.30`, or `C.30.ASV` respectively.

**E.10.ARCH governing-pattern relation.** When `E.10` encounters function-like wording whose required transformation, capability, method, work, role, mathematical-function use, quality use, module allocation, interface relation, architecture use, FPF kind named by value, relation, claim record, governing pattern, or stop condition is hidden, `E.10.ARCH` may apply `A.6.F` until those fields are recovered or the wording is lowered to ordinary prose, quote-only wording, reduced-use cue, blocked use, or incomplete rewrite. After recovery, the next application is the governing pattern named by the recovered relation; `A.6.F` does not own architecture, mathematics, quality, work, evidence, assurance, gate, decision, or release claims by function wording alone.

### A.6.F:2 - Problem

FPF texts repeatedly use function-like wording for different FPF kinds and relations:

- required transformation or effect in an architecture view;
- capability of a holon;
- method wording;
- work occurrence or work result;
- role expectation or responsibility;
- mathematical function or relation;
- quality, fitness, or characteristic wording;
- module allocation or interface relation;
- functional architecture shorthand.

These uses are all legitimate in ordinary engineering speech. They are not the same FPF kind. If the text does not recover the FPF value kind, relation record, slot reference, view record, or governing pattern named by value, subsequent reasoning cannot tell whether the sentence is about architecture, behavior, work, role, mathematics, module structure, quality, evidence, or decision claim.

### A.6.F:3 - Forces

| Force | Tension |
| --- | --- |
| Familiar engineering speech vs kind precision | Engineers naturally say "function", "functional", and "functionality"; FPF needs the FPF kind named by value, relation, claim record, view, or governing-pattern application recoverable when the phrase carries an FPF claim being made. |
| Functional architecture vs peer ontology | Functional architecture is useful, but it is the `FunctionalStructure` case of `ArchitectureOf@Context`, not a separate root architecture kind. |
| Capability or effect vs work or method | A function-like phrase may describe what a holon can do, what a method prescribes, or what work has done; those are different FPF kinds named by value, relations, and claim records. |
| Mathematical function vs design relation | Mathematical functions and relations can be used for reasoning, but C.29 governs their lens use and stop condition. |
| Module allocation vs functional relation | Functional dependencies may be allocated to modules, but function and module-interface structure do not become one FPF kind. |
| Small repair vs unneeded evidence, quality, decision, or assurance apparatus | Most cases need recovery of value kind, relation record, slot reference, view record, or governing pattern plus a stop condition, not a full architecture, evidence, quality, or decision claim apparatus. |

### A.6.F:4 - Solution

A.6.F is an A.6.P RPR specialization for function-like wording. It does not mint `U.Function`. It assigns the use under repair to an existing FPF kind, relation, claim record, view, or governing-pattern application and stops there unless another claim kind remains current.

#### A.6.F:4.1 - Trigger rule

A.6.F applies when a sentence uses function-like wording to carry one or more current FPF claim kinds:

- architecture or functional architecture;
- capability, effect, externally promised behavior, or user-visible functionality;
- method wording, work occurrence, or work result;
- role expectation or responsibility;
- mathematical function, mapping, relation, loss, objective, or value functional;
- quality, fitness, characteristic, score, or proxy wording;
- module allocation, interface, signature, port, API, protocol, flow, or mechanism relation;
- another FPF claim named by value, such as evidence, assurance, gate, decision, or release.

If none of those claim kinds is current, the wording may remain ordinary Plain prose.

#### A.6.F:4.2 - FunctionUseRepair

`FunctionUseRepair` is a pattern-local repair note. It carries no project-publication, evidence, decision, or `U.Function` authority. `FunctionalStructure` is an `ArchitectureStructureKindRef` value under C.30.ASV, not a kernel Function kind.

```text
FunctionUseRepair ::= {

  phrase,
  claimKindUnderRepair:
    requiredTransformation |
    requiredEffect |
    functionalElementLocus |
    transformerSideFiller |
    candidateBearer |
    inputCondition |
    outputCondition |
    functionalPort |
    holonCapability |
    methodPosition |
    methodDescription |
    mechanismRealization |
    workPlan |
    procedureWording |
    workOccurrence |
    workResult |
    roleExpectation |
    mathematicalFunction |
    mathematicalRelation |
    qualityExpression |
    characteristicExpression |
    moduleAllocation |
    interfaceRelation |
    signatureRelation |
    functionalArchitecture |
    evidenceClaim |
    assuranceClaim |
    gateClaim |
    decisionClaim |
    publicationClaim |
    otherDeclared,
  recoveredValueKindRefs?:
    U.Transformation |
    TransformationFlowStructure |
    U.Capability |
    U.Method |
    U.MethodDescription |
    U.Mechanism |
    U.WorkPlan |
    U.Work |
    MathematicalFunctionUnderC29 |
    otherDeclared,
  recoveredRelationRecordRefs?:
    FunctionalElement@Context |
    ModuleAllocationRelation |
    InterfaceSpecification |
    RoleExpectation |
    otherDeclared,
  recoveredSlotRefs?:
    TransformerRef? |
    CandidateBearerRef? |
    InputConditionRefs? |
    OutputConditionRefs? |
    FunctionalPortRefs? |
    FunctioningRef? |
    QBundleSlot |
    otherDeclared,
  recoveredViewRecordRefs?:
    FunctionalStructureView@Context |
    otherDeclared,
  recoveredFpFReferenceRefs?,

  sourceCueText?,
  directGoverningPatternApplicationRefs?,
  bearerRef?,
  candidateBearerRef?,
  functionalBehaviorRef?,
  blockedLocalOverreadRefs,
  admissibleUse,
  nonAdmissibleUse,
  nextAdmissibleUse,
  stopCondition
}
```
The repair is complete when a practitioner can say which FPF value kind named by value, relation record, slot reference, view record, or direct governing-pattern application the function-like wording uses. A source cue stays in `sourceCueText`; it is not a recovered value. If the text still hides a function, capability, work, method, role, module, evidence, gate, or mathematical-function collapse, the repair is incomplete.

#### A.6.F:4.3 - Repair assignments

When a function-like phrase is claim-bearing, recover the positive object under concern before lowering or rewriting the phrase. FPF treats `FunctionalElement@Context` as a view-local functional-structure record under C.30.ASV when stable identity, bearer, behavior, ports, capability, and allocation obligations are all current; otherwise A.6.F may stop at the smaller recovered value kind, relation record, slot reference, or source cue.

| Function wording use | Recovered FPF kind, relation, slot, or view | Boundary |
| --- | --- | --- |
| required functional behavior, transformation, or effect | `U.Transformation` for one bounded required change or required effect; `TransformationFlowStructure` for compound behavior; `FunctionalElement@Context.functionalBehaviorRef` when a functional element is current | Do not compare the element noun directly with `U.Transformation`. Compare the functional behavior or functioning with transformation, and keep the bearer or view-local locus separate. |
| functional element in a view | `FunctionalElement@Context` inside `FunctionalStructureView@Context` when selected view, bounded context, functional behavior, and bearer or candidate-bearer locus are current | Not `U.Function`, not a loose table row, and not the module by default. If no bearer or candidate allocation is current, keep a required transformation, effect, capability gap, or behavior slot rather than claiming a full functional element. |
| transformer-side filler and candidate bearer | `U.System` bearing `TransformerRole@Context` for a transformer-side filler; candidate system reference for an allocation candidate; coordinated with `A.3.4 TransformerRef?`, `A.7`, `A.15`, `A.15.1`, and `A.15.2` when role, work, responsibility, or enactment claims are current | A functional element may recover one of these loci, but it is not the whole transformer ontology. Device cues and transformer-bearer cues recover this locus when the claim is current; they do not mint a durable transformer kind. |
| input condition, output condition, and functional ports | `A.3.4 InputConditionRefs?`, `OutputConditionRefs?`, and `FunctionalPortRefs?`; `U.Signature` discipline through `A.6.0` and `A.6.5` when accepted or produced states, media, flows, signals, information, work products, formal objects, or functional port signatures matter | A functional port is not automatically a module interface. Use A.6.M only when module-interface or substitution compatibility is the claim. |
| capability of a holon | `U.Capability` or the capability-governing pattern or project record named by the claim being made | Does not imply that a method, module, work occurrence, or successful transformation exists. |
| method or algorithm wording | `U.Method` when the source says the semantic way of doing under conditions; `U.MethodDescription` when it is an authored procedure, code, solver, recipe, protocol, or algorithm text | Does not imply execution or evidence. Algorithm wording is a source cue; recover the current kind rather than treating it as software-only. |
| mechanism wording | `U.Mechanism` through `A.6.1` and `E.20` when a law-governed realization or operation structure is the claim | Does not become method, work, capability, or functional element by label. |
| work plan, work occurrence, or work result | `U.WorkPlan`, `U.Work`, Work record, or P2W carry-through relation under `A.15`, `A.15.2`, `A.15.1`, and `E.18.1` according to the asserted claim | Does not imply reusable function ontology or completed functioning. |
| responsibility or role expectation | `VP.AllocationResponsibility` and the relevant role-assignment or responsibility relation, with `U.RoleAssignment` when a role assignment claim is current | Does not imply the role-assigned system or acting holon performed the work or that the bearer has the capability. |
| mathematical function or relation | C.29 mathematical-lens use with domain, codomain or relation domain, preserved and lost structure, lens-use admissibility value, and stop condition | Does not become architecture, evidence, causal proof, assurance, or decision claim by itself. |
| quality or fitness expression | `C.25`, `C.16`, `C.16.Q`, `A.17`, `A.18`, or an admitted characteristic or measurement governing pattern according to the claim being made | Does not let "functionality" carry a quality claim without bearer and governing pattern. |
| module allocation | `FunctionalStructureView@Context` plus declared correspondence, allocation, retargeting, or `A.6.M` module-relation repair when a module-interface claim is being made | Does not make function and module one FPF kind; allow one module to realize many functional elements, many modules to realize one functional element, abstract functional elements before allocation, and modules with no current functional behavior in a view. |
| interface relation, module-interface relation, or signature relation | Use `A.6.RSIR` first when bare interface, API, port, protocol, or service-access wording could point to several direct EoCs; then use module-interface boundary note governed by `A.6.M` and signature discipline governed by `A.6.0` and `A.6.5`, with `A.6.B`, `A.6.C`, or `A.6.8` only when that boundary, contract, API, protocol, service, promise, or duty claim is being made | Does not turn a functional link, port label, API name, or signature into implemented compatibility. |
| evidence, result, assurance, gate, decision, or publication claim | the direct evidence, result, assurance, gate, decision, publication, or source pattern named by value | Function wording can point to these claims, but it does not authorize or prove them by itself. |
| functional architecture | `ArchitectureOf@Context` with `structureKindRef = FunctionalStructure` and `FunctionalStructureView@Context` under C.30.ASV | Not a peer architecture ontology, selected transformation-flow structure, or mathematical graph description by itself. |

#### A.6.F:4.4 - Functional architecture boundary

Functional architecture is the `FunctionalStructure` case of `ArchitectureOf@Context`: the declared organization of required transformations, capabilities, effects, functional dependencies, and constraints that a holon is to realize, before or alongside allocation to modules, roles, work, evidence, control relations, selected transformation-flow structures, or mathematical descriptions of those structures.

```text
FunctionalArchitecture@Context shorthand expands to:
  ArchitectureOf@Context(
    describedHolonRef,
    boundedContextRef,
    structureKindRefs includes FunctionalStructure,
    structureRefs includes `U.StructureRef` values for required transformations,
      effects, capabilities, dependencies, and constraints,
    admissibleUse,
    nonAdmissibleUse
  )
```

This shorthand is admissible only when the expanded C.30 or C.30.ASV interpretation is recoverable. A selected `TransformationFlowStructure`, path slice, crossing, flow valuation, or mathematical description may be related to functional structure through `C.30.TFS-REL`, `E.18`, or `E.18.2`, but it is not the functional architecture itself unless the positive selected-structure co-reference check succeeds.

#### A.6.F:4.5 - Function-flow-module alignment note

Use this note when functional wording touches flow or module allocation but does not yet require a full structural view or `A.6.M` module-relation repair.

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

The note records only the local function-flow-module alignment and boundary. Functional architecture, module relation, implemented-interface, evidence-sufficiency, and architecture-decision claims remain with their governing patterns.

#### A.6.F:4.6 - Common kind and relation separations

| Confusion | Repair |
| --- | --- |
| function = module | Keep `VP.Functional` and `VP.ModuleInterface` distinct; connect them through declared correspondence, allocation, retargeting, or `A.6.M` module-relation repair. |
| function = capability | Capability belongs to a holon; function-like wording describes required transformation, required effect, or architectural relation only when that FPF value kind, relation record, slot reference, view record, or governing pattern named by value is declared. |
| function = work | Work is a dated occurrence or result; function is design-side or description-side content unless a work-evidence claim is being made. |
| function = method | Method is a reusable way of doing; function-like wording names required transformation or effect only when a method or method-description claim is being made separately. |
| function = role | Role-assignment and responsibility structure uses `VP.AllocationResponsibility` and role records; function-like responsibility wording needs role-assignment or responsibility relation recovery. |
| mathematical function = holon purpose | Use C.29 for mathematical function or relation; recover domain, codomain or relation domain, preserved and lost structure, lens-use admissibility value, and stop condition. |
| functional diagram = evidence | Diagram is a view or publication; evidence claim uses `A.10` or `G.6`. |
| functionality = quality | Recover the quality bearer and governing pattern through `C.25`, `C.16`, or C.16.Q before using the wording as an adequacy claim. |

#### A.6.F:4.7 - Composability and compositionality

Composability and quality compositionality are separate claims. If the text says parts can be assembled, keep that as a structure or use claim. If it says a quality of the whole follows from parts, assign the quality-composition claim to `C.25` and C.16-backed measurement or quality claim:

```text
Composability:
  "A and B can be assembled under interface X."
  recoveredRelationRecordRefs: ModuleAllocationRelation; InterfaceSpecification
  directGoverningPatternApplicationRefs: A.6.M when a module-interface claim remains; A.6.5 when a signature claim remains
Quality compositionality:
  "The assembled whole preserves safety, latency, or reliability."
  recoveredSlotRefs: QBundleSlot; structuralCharacteristicQBundleInputSlot; structuralCharacteristicCausalHypothesisForQBundleSlot; structuralCharacteristicEvidenceRelationForQBundleSlot
  directGoverningPatternApplicationRefs: C.25; C.16 or C.16.Q; A.10 only when the evidence-provenance path is the claim being made
Non-admissible:
  successful assembly is not quality propagation
```
Compositional formalisms may express explicit composition structures and view or model relations. They do not make safety, latency, reliability, or another quality propagate automatically.

```text
CompositionalityClaim@Quality ::= {
  affectedQBundleRef,
  partStructureRefs,
  wholeStructureRef,
  compositionRelation,
  lensUseAdmissibilityValue,
  nonAdmissibleUse
}
```

#### A.6.F:4.8 - Worked slices

**Functional architecture phrase.** A team says, "the functional architecture is the user journey." A.6.F does not let the phrase create a separate architecture kind. The repair is:

```text
FunctionUseRepair:
phrase: "functional architecture"
claimKindUnderRepair: functionalArchitecture
recoveredSlotRefs: ArchitectureOf@Context.structureKindRef = FunctionalStructure
recoveredViewRecordRefs: FunctionalStructureView@Context when selected functional structure changes action
recoveredFpFReferenceRefs: ArchitectureOf@Context with structureKindRef = FunctionalStructure
directGoverningPatternApplicationRefs: C.30; C.30.ASV
blockedLocalOverreadRefs: user journey publication, work log, selected transformation-flow structure, mathematical graph description, module diagram
nextAdmissibleUse: open C.30.ASV only if the selected functional structure changes action
stopCondition: ordinary phrase remains Plain if no architecture claim is being made
```
**Functionality as quality.** A product note says, "new functionality improves adequacy." The repair separates added capability or effect from quality claim. Capability or effect wording may stay as recognition, but adequacy claim goes to `C.25`, `C.16`, C.16.Q, or an admitted characteristic or measurement governing pattern when the claim is being made. A.6.F stops after value-kind, relation-record, slot-reference, view-record, or governing-pattern recovery when no quality claim remains.

**Mathematical function or loss.** A model note says, "the loss function explains the holon purpose." The repair keeps the mathematical function under C.29 lens discipline: domain, codomain or relation domain, preserved and lost structure, lens-use admissibility value, and stop condition. The loss may inform a reasoning move; it does not become holon purpose, evidence sufficiency, causal proof, assurance, or project decision by itself.

**Pump-station functional dependency.** A maintenance note says, "the backup pump function is degraded." A.6.F first separates the required effect, the holon capability, the physical module allocation, the performed maintenance work, the evidence relation, and the quality claim. The functional wording may open a `FunctionalStructure` view under C.30.ASV or a capability record; it does not by itself prove the pump was tested, authorize operation, or make the backup module compatible with the main line.

**Product-platform allocation.** A hardware team says, "thermal management functionality moved to the chassis." The repair separates required heat-removal effect, module allocation, interface constraints, signature constraints, architecture structural view, and any evidence or gate claim. A.6.F keeps the function-like wording useful for architecture work while sending module-interface and evidence claims to their governing patterns.

### A.6.F:5 - Archetypal Grounding

| Tell-Show-Show row | Grounding |
| --- | --- |
| Tell | A practitioner reads "the function", "functional architecture", or "this functionality" and needs to know whether the sentence is about capability, effect, method, work, role, module allocation, mathematical relation, quality, or architecture. A.6.F asks for the FPF kind named by value, relation, claim record, view, or governing-pattern application before the phrase carries an FPF claim being made. |
| Show: `U.System` | A robot, software system, plant, product platform, or AI-agent system may have capabilities, required effects, control functions, module allocations, runtime flows, and user-visible functionality. Those are not one FPF kind; A.6.F assigns each use being made to its FPF kind named by value, relation, or governing pattern. |
| Show: `U.Episteme` | A functional diagram, SysML view, architecture note, generated code architecture note, benchmark report, or mathematical model may publish or substantiate a function-like claim. The episteme or publication does not become the function, capability, work, evidence, or architecture. |

### A.6.F:6 - Bias-Annotation

Lenses tested: **Arch**, **Ontology and episteme**, **Prag**, **Did**, **Gov**. Scope: function-like wording that carries an FPF claim being made across FPF.

| Bias risk | Mitigation |
| --- | --- |
| Function-root bias | The pattern explicitly does not mint `U.Function`; it assigns wording to existing FPF kinds, relations, or governing patterns. |
| Functional-architecture exception bias | Functional architecture is normalized as `FunctionalStructure`, not a peer ontology. |
| Module bias | Function-to-module allocation uses correspondence or `A.6.M` module-relation repair; function and module remain distinct. |
| Mathematical bias | Mathematical function wording is assigned to C.29 when used as a lens. |
| Check-only bias | Every conformance item carries a repair action or governing-pattern application. |

This checklist verifies the preceding guidance after the practitioner has chosen the selected repair action; it is not a required project control form and not a substitute for the card, note, view, relation, or repair guidance above.

### A.6.F:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-A6F-1 FPF recovery named by value.** | Every function-like phrase that carries an FPF claim being made names the recovered FPF value kind, relation record, slot reference, claim record, view record, or governing-pattern application and, when the claim points to a specific source, the recovered FPF reference. | Add `FunctionUseRepair` or demote the phrase to Plain prose. |
| **CC-A6F-2 No `U.Function`.** | The use does not mint or rely on `U.Function` as a new root kind. | Assign the use to functional view, capability, method, work, role, mathematical lens, quality or characteristic, module allocation, or governing pattern. |
| **CC-A6F-3 Functional architecture expansion.** | Functional architecture expands to `ArchitectureOf@Context` with `structureKindRef = FunctionalStructure` and C.30.ASV when it carries a architecture claim being made. | Add the expansion or keep the phrase as ordinary recognition wording. |
| **CC-A6F-4 Function and capability split.** | Capability claims and function or effect claims remain distinct. | Assign capability claims to the capability-governing pattern or project record named by the claim being made and keep function or effect wording in the functional view or effect record. |
| **CC-A6F-5 Function, work, and method split.** | Method, work occurrence, and work result claims do not hide inside function wording. | Assign the claim to `U.Method`, `MethodDescription`, `U.Work`, Work record, `A.15`, or `E.18.1` according to the asserted method, work, work-result, or P2W carry-through claim. |
| **CC-A6F-6 Function and role split.** | Responsibility or role expectation wording uses `VP.AllocationResponsibility` and role-assignment or responsibility relations when a role claim is being made. | Add the role-assignment or responsibility relation or remove the role claim from the function phrase. |
| **CC-A6F-7 Mathematical function boundary.** | Mathematical function or relation wording used to justify reasoning names C.29 lens fields and stop condition. | Add C.29 lens-use admissibility value, preserved and lost structure, and stop condition, or mark mathematical use as ordinary. |
| **CC-A6F-8 Quality and functionality boundary.** | Quality, fitness, characteristic, score, or "functionality" wording recovers bearer and governing pattern. | Assign the claim to `C.25`, `C.16`, `C.16.Q`, `A.17`, `A.18`, or the characteristic named by value or measurement governing pattern according to the asserted quality, characteristic, measurement, or comparison claim. |
| **CC-A6F-9 Module-interface boundary.** | Functional relation, module allocation, interface, signature, port, API, protocol, flow, and mechanism wording remain separated. | Add `A.6.RSIR` interface-cue recovery, `FunctionFlowModuleAlignmentNote`, a module-interface boundary note governed by `A.6.M`, signature-discipline note governed by `A.6.0` and `A.6.5`, declared correspondence, declared allocation, or `A.6.M` module-relation repair. |
| **CC-A6F-10 Useful action.** | The repair leaves a remaining admissible use: assign the FPF value kind, relation record, slot reference, view record, or governing pattern named by value; open functional view; add alignment note; assign the claim being made to C.29, C.30, C.30.ASV, A.15, C.25, C.16, A.10, B.3, A.20, A.21, or C.11; or stop. | Restore that use, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

### A.6.F:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Root function kind** | The text treats function as a new universal FPF kind. | Use `FunctionUseRepair` and assign the use to an existing FPF kind, relation, claim record, view, or governing-pattern application. |
| **Functional architecture exception** | Functional architecture is treated as a peer architecture ontology. | Expand to `FunctionalStructure` under `ArchitectureOf@Context` and C.30.ASV. |
| **Capability collapse** | What the holon can do is treated as a functional dependency or vice versa. | Split capability claim from functional relation or effect claim. |
| **Work collapse** | Work occurrence or result is described as a function. | Assign occurrence or result claims to A.15 and P2W and keep functional wording design-side unless a work-evidence claim is being made. |
| **Mathematical-function import** | A mathematical function, loss, objective, or value functional becomes design ontology. | Use C.29 and state preserved and lost structure plus stop condition. |
| **Module allocation shortcut** | A function is considered implemented because a module is named. | Add correspondence, allocation, module-interface boundary, signature-discipline boundary, or `A.6.M` module-relation repair. |
| **Functionality as quality proxy** | "Functionality" carries adequacy or quality claim without bearer and governing pattern. | Recover bearer and governing pattern through `C.25`, `C.16`, C.16.Q, or an admitted characteristic or measurement governing pattern. |
| **Sterile kind repair** | The wording is typed but no useful move remains. | Restore the value-kind assignment, relation-record assignment, slot-reference assignment, functional view, alignment note, or governing-pattern application. |

### A.6.F:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| Function-like prose remains usable without minting `U.Function`. | Uses that carry FPF claims being made need value-kind, relation-record, slot-reference, view-record, or governing-pattern recovery. |
| Functional architecture becomes a normal architecture-by-structure-kind case. | C.30 or C.30.ASV may be needed when the phrase carries an architecture claim. |
| Capability, method, work, role, mathematical, quality, module, and interface claims stay separable. | A single familiar word may split into several records when several claim kinds are being made. |
| C.29, C.25, C.16, A.15, C.30, and `A.6.M` govern only the claims that belong to them. | A conforming use stops after kind and relation recovery when no further claim kind is being made, instead of opening all possible governing patterns. |

### A.6.F:10 - Rationale

Function-like wording is too useful to ban and too overloaded to leave ungoverned. The smallest useful repair is not a new ontology. It is recovery of the value kind, relation record, slot reference, claim record, view record, or governing-pattern application: say what the phrase is about, what it is not about, and what use remains admissible.

This design follows A.6.P: trigger phrase, value-kind recovery, relation-record recovery, slot-reference recovery, explicit relation fields, governingPatternRef fields, and lexical guardrails. It also follows C.30: functional architecture is selected structure for a described holon, not a peer of architecture, not a selected transformation-flow structure by default, and not a mathematical graph description by itself.

The pattern keeps ordinary language usable. A phrase can remain Plain when it carries no FPF claim being made. When it carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim kind, the FPF kind named by value, relation, claim record, view, or governing-pattern application is recoverable.

### A.6.F:11 - SoTA-Echoing

| Practice or source line | A.6.F adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022 architecture-description discipline | Adapt view and concern discipline to functional architecture as a structure-kind view over an architecture claim. | Functional architecture expands through C.30 and C.30.ASV rather than becoming a separate ontology. | ISO terminology does not mint `U.Function` or turn diagrams into architecture. |
| OMG SysML v2 and KerML behavior and view practice | Adapt function, behavior, and model-view separation as practice source for functional-view recovery. | Functional views name selected functional structure and keep flow, module, and work relations separate. | SysML and KerML model elements do not override FPF kinds, relations, or governing patterns, and do not import tool ontology. |
| INCOSE systems-engineering and MBSE functional-analysis practice | Adopt the practical need to separate function, requirement, behavior, physical allocation, and verification claim kinds. | A function-like phrase can guide architecture work only after capability or effect, allocation, evidence, and verification claim kinds are separated. | Functional analysis practice is not evidence sufficiency, assurance, gate passage, or project decision by itself. |
| ISO/IEC 25010 quality-model practice | Treat functionality or functional suitability as quality wording when it evaluates a product or service. | Assign quality-like uses to C.25, C.16, or C.16.Q before they carry adequacy claims. | "Functionality" is not a free adequacy score and not a functional architecture record. |
| C.29 mathematical-lens discipline | Adopt domain, codomain or relation-domain, preserved and lost structure, lens-use admissibility value, and stop condition for mathematical function use. | Mathematical function wording becomes lens-governed only when C.29 fields are recoverable. | Mathematical functions, objectives, and value functionals do not become holon purpose, evidence, causal proof, assurance, or decision claim by themselves. |
| GonzoML neural-network architecture discussions | Adapt practitioner operation language involving blocks, activations, path-selection, memory, cache, loss functions, pruning, ablation, and architecture search as recognition material. | Function-like neural-network claims require kind and relation recovery: mathematical function, flow relation, module-interface claim kind, capability or effect, quality characteristic, or decision or evidence governing pattern. | Neural-network labels and benchmark results do not become FPF ontology, architecture decision, evidence sufficiency, gate passage, or assurance by themselves. |

### A.6.F:12 - Relations

Builds on: `A.6.P`, `A.6.RSIR`, `A.6.0`, `A.6.5`, `A.6.B`, `A.6.C`, `A.6.8`, `A.6.9`, `A.7`, `E.10`, `E.10.ARCH`, `C.2.P`, `F.18`, and `E.8`.

Coordinates with: `C.30`, `C.30.ASV`, `C.30.TFS-REL`, `E.18`, `A.15`, `A.2`, `C.29`, `C.25`, `C.16`, `C.16.Q`, `A.17`, `A.18`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `C.11`, `A.6.RSIR`, and `A.6.M` when a module or interface claim is being made.

Does not replace: C.30 grounded architecture and selected-structure adequacy, C.30.ASV architecture structural-view adequacy, E.18 selected transformation-flow structure, E.18.2 mathematical descriptions, C.29 mathematical-lens use, C.25 Q-Bundles, C.16 characterization, A.15 work and method discipline, A.10 or G.6 evidence, B.3 assurance, A.20 or A.21 gate or release records, or C.11 decisions.

### A.6.F:End

