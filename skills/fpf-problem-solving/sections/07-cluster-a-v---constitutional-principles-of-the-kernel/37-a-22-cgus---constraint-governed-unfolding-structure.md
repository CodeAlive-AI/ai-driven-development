## A.22.CGUS - Constraint-Governed Unfolding Structure

> **Type:** A.22 specialization of `U.Structure`
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### A.22.CGUS:0 - Use This When

Use this when a team has a P2S flow card, a P2W carry-through note, an abductive prompt path, an improvement cycle, a narrative ordering, a typing-grounding trace, or a README first-entry seed, and the visible form helps but also misleads. It looks like a route, loop, chain, table, graph, or story, while the useful engineering question is not "which sequence should everyone follow?" but "which admitted records, current structures, loci, constraints, and guards make some next uses admissible and block others?"

When that is the live question, name the object as `ConstraintGovernedUnfoldingStructure@Context`: an A.22-governed `U.Structure` whose named loci, relation signatures, constraints, invariants, guarded transitions, preserved and lost structure, direct governing-pattern exits, admissible next forms, and stop, return, split, or refresh conditions span more than one live locus.

Use CGUS only after the candidate structure has several governed loci and cross-locus constraints. A single recommendation, diagram, slogan, pattern list, or document section is not enough.

### A.22.CGUS:1 - Problem Frame

FPF often needs to explain how several admitted records, current structures, and governed loci jointly constrain several admissible next forms without turning that explanation into a workflow. A problem card, `G.2` source pack, architecture concern, candidate set, evaluation result, cue publication, and current `U.Structure` may together constrain pattern-use recommendations, candidate structures, rival hypotheses, evidence work, repair proposals, reader-facing narratives, or structure-use return conditions. The point is the constraint-governed relation among loci, relation signatures, guards, preserved and lost structure, and direct governing-pattern exits, not a one-input-one-output conversion.

These are not all transformation-flow structures. They may be architecture-facing, reasoning-facing, narrative-facing, improvement-facing, typing-grounding-facing, evidence-facing, refresh-facing, or first-entry-facing. Still, they share one structural need: the loci constrain each other, and the next admissible forms are recoverable only if the preserved structure, lost structure, guards, exits, and governing-pattern boundaries are visible.

### A.22.CGUS:2 - Problem

The problem is that a route-shaped or loop-shaped record or description can hide the structure it is trying to expose.

First, the record or description becomes decorative prose. The DRR or pattern uses words such as "flow", "move", "unfold", "loop", or "route", but no reader can recover the loci, constraints, preserved structure, lost structure, stop condition, or direct governing pattern for stronger claims.

Second, the record or description becomes a fake workflow. A teaching sequence, diagram, README entry, prompt example, or happy path is treated as the order in which real project work must happen. Method, work plan, performed work, evidence, gate, decision, publication, and architecture claims then silently move into the route-shaped record or description.

### A.22.CGUS:3 - Forces

| Force | Tension |
| --- | --- |
| Useful unfolding vs workflow overread | A structured unfolding helps a practitioner see what can come next, but the project sequence may be nonlinear, partial, interrupted, iterative, or delegated to different governing patterns. |
| Reusable `U.Structure` specialization vs root-kind inflation | FPF needs a reusable A.22 specialization of `U.Structure` for constraint-governed unfolding, but it must not mint `U.Route`, `U.Workflow`, `U.Process`, `U.Architecture`, or another root kind by appearance. |
| Description usefulness vs semio-bias | Route cards, graphs, tables, slides, narratives, and README lines can show the structure, but they are descriptions or demonstrative slices, not the structure itself. |
| Local claims vs universal calculus | P2W, P2S, abduction, narrative, improvement, grounding, refresh, and option selection need different direct governing patterns; CGUS only carries the shared constraint-governed unfolding structure. |
| Didactic entry vs shadow navigation | First-entry seed lines help new readers start, but they must not become a second specification or navigation authority beside the governing patterns. |

### A.22.CGUS:4 - Solution

Select `ConstraintGovernedUnfoldingStructure@Context <: U.Structure` as a thin A.22 specialization of `U.Structure` for constraint-governed unfolding across named loci.

A constraint-governed unfolding structure is a `U.Structure` whose relation signatures, constraints, invariants, guarded transitions, preserved and lost structure, and governing-pattern exits make several loci jointly constrain admissible next forms. It states how admitted starting records and already-current structures can participate in that structure. It does not state that real work must occur in the displayed order, and it does not require one starting record, one starting structure, or one resulting record.

Do not read "unfolding" as a chain by default. The unfolding structure may be branching, merging, cyclic, partially ordered, or graph-shaped, and it may leave several alternative next forms live at once. A linear chain, cycle drawn as "back to the start", seminar order, prompt path, or happy path is usually a `DemonstrativeUnfoldingSlice@Context`: one declared traversal or presentation of a wider structure.

#### A.22.CGUS:4.1 - Ontic Field Block

```text
ConstraintGovernedUnfoldingStructure@Context:
  kind: U.Structure
  unfoldingStructureId:
  boundedContextRef:
  declaredStructureSubstrateRef:
  entityOfConcernRef:
  acceptedStartingRecordRefs[]:
  acceptedStartingStructureRefs[]:
  promotedCoreFamilyCueRefs[]?:
    UF.P2W |
    UF.P2S |
    UF.ABD |
    UF.NAR |
    UF.IMP |
    UF.GND |
    UF.SEL |
    UF.REFRESH |
    UF.CALL |
    otherDeclared
  localFamilyCueRefs[]?:
  unfoldingFamilyClass?:
    transformationFlow |
    methodWork |
    reasoningSearch |
    narrativeOrdering |
    improvementLoop |
    typingGrounding |
    architectureSelection |
    selectionOrPortfolio |
    referenceCurrentness |
    toolUsePlanning |
    otherDeclared
  specializedStructureRef?:
  relationSignatureRefs[]:
  unfoldingLoci[]:
  constraintRefs[]:
  invariantRefs[]:
  guardedTransitionRefs[]:
  preservedStructure:
  lostOrHiddenStructure:
  admissibleNextFormKindRefs[]:
  defaultDemonstrativeSliceRecipeRefs[]:
  admissibleUse:
  nonAdmissibleUse:
  structureUseReturnCondition:
  stopCondition:
  reopenOrRefreshTriggers[]:
```

`acceptedStartingRecordRefs[]` names already admitted project records that the unfolding structure may use at the start of the current use: problem cards, `G.2` source packs, candidate-set records, evaluation results, cue publications, or other governed records. Each record must keep its own direct governing pattern and admitted use. The field does not make raw source prose, attractive distinctions, prompts, model output, or a visible route into an admitted starting record by itself.

`acceptedStartingStructureRefs[]` names already-current `U.Structure` refs that the unfolding structure may use at the start of the current use. This slot is intentionally separate from `acceptedStartingRecordRefs[]`: a record may describe, publish, or evaluate a structure, but it is not that structure.

`declaredStructureSubstrateRef` names the structure substrate whose loci and relations are being unfolded, such as transformation-flow structure, architecture-facing structure use, narrative ordering, abductive search, improvement loop, typing-grounding passage, refresh situation, or option-selection structure. `entityOfConcernRef` names the entity or concern whose unfolding is being organized. `unfoldingLoci[]` names the governed positions inside the structure. The accepted-starting slots are therefore not duplicates of substrate, EntityOfConcern, or loci: they record which admitted records and current structures are available at the start of the current unfolding use.

`promotedCoreFamilyCueRefs[]?` may name short FPF-core cues such as `UF.P2S` or `UF.REFRESH` when they help readers recognize a familiar core family. These cues are optional examples, not a maintained list, not a conformance vocabulary, and not a DPF index. A DPF or project-local package may use `localFamilyCueRefs[]?`, local cue examples, or no family cue at all; its authoritative route is the local governing-pattern map plus the relevant FPF and DPF pattern bodies. `unfoldingFamilyClass?` is optional broad retrieval and review shorthand; it is not the governing vocabulary.

`specializedStructureRef` is used only when a narrower `U.Structure` specialization is current, such as `E.18.3` for transformation-flow unfolding, `C.32.P2S` for architecture-facing P2S, `B.5.2` for abductive search, `A.6.3.NAR` for narrative ordering, `E.23` for improvement loops, or typing-grounding patterns for constructive-to-logical grounding.

#### A.22.CGUS:4.1a - Field Glosses

These fields are ordinary structure slots, not a second method, work, evidence, architecture, or publication record.

| Field | What this slot names | Not this | Direct exit when stronger claim is current |
| --- | --- | --- | --- |
| `relationSignatureRefs[]` | references to relation signatures that make the unfolding positions connectable | not proof that the relations hold in the world | `A.6.0`, `A.6.5`, or the pattern governing the relation |
| `constraintRefs[]` | constraints that restrict admissible continuations | not a gate result or work authorization | `A.20`, `A.21`, A.15 family, or the domain pattern |
| `invariantRefs[]` | structure that must survive admissible unfolding | not a measurement or evidence result | `C.16`, `C.25`, `A.10`, or `B.3` when those claims are current |
| `guardedTransitionRefs[]` | guarded changes between loci or admissible next positions | not a performed work occurrence | `A.3.4`, A.15 family, `A.20`, or `A.21` |
| `preservedStructure` | selected structure kept by this unfolding use | not a claim that every selected starting structure or source-described structure is preserved | `C.33`, `C.34`, or the direct governing pattern for the preservation claim |
| `lostOrHiddenStructure` | selected or expected structure not carried by the unfolding use | not a defect by itself | structure-use return condition, `C.33`, `C.34`, or the direct governing pattern named by the use |
| `admissibleNextFormKindRefs[]` | kinds of records or uses that may be written next | not a required sequence and not execution | receiving governing pattern for each next form |
| `defaultDemonstrativeSliceRecipeRefs[]` | teaching or planning slice recipes over the structure | not the structure and not work order | `DemonstrativeUnfoldingSlice@Context`, `E.17`, or A.15 family as current |
| `admissibleUse` | what this CGUS may safely support | not blanket permission for all uses | direct governing pattern for the supported claim |
| `nonAdmissibleUse` | blocked overread for this CGUS use | not a negative catalogue of every possible mistake | direct governing pattern that would be needed for the blocked claim |
| `structureUseReturnCondition` | condition that names the selected structure or expected structure at issue, the lost or hidden distinction, and the receiving governing pattern; when current it also names the exact source description, publication, source-use relation, lens result, extraction, or probe locus whose use must be repaired | not a `G.11` refresh unless currentness or decay is the claim | receiving governing pattern named by value |
| `stopCondition` | condition for keeping the current record, description, or demonstrative slice at reduced use | not failure of the admitted starting record, source pack, or description by itself | A.16, E.11, E.17, or the direct governing pattern as applicable |
| `reopenOrRefreshTriggers[]` | changed facts, currentness, or use conditions that reopen the smallest affected claim | not a new reopen and refresh ontology | `G.11` for currentness or decay; `E.18` for slice-local refresh; the direct governing pattern for repair |

#### A.22.CGUS:4.2 - Admission Test

Use CGUS only when all of these are recoverable enough for the next use:

| Coordinate | Required recovery | If missing |
| --- | --- | --- |
| Several logical loci | More than one governed position is live: problem-side record, current structure, candidate set, method relation, work-planning locus, evidence locus, reader route, evaluation row, refresh trigger, or another declared position. | Keep the candidate wording as a note, cue, recommendation, or description. |
| Cross-locus constraints | Loci constrain each other through relations, guards, boundaries, preserved or lost structure, stop rules, or return conditions. | Treat a list of steps or pattern IDs as an index until constraints are recoverable. |
| `U.Structure` specialization | The object is a `U.Structure` under A.22 or a narrower `U.Structure` specialization governed elsewhere. | Treat a card, graph, narrative, publication, README line, or method description as a description or seed. |
| Admissible next forms | One or more next forms are named: pattern-use recommendations, candidate sets, narrative orderings, work-plan seeds, method-selection frames, evaluation repair frames, architecture inputs, return requests, refresh actions, or demonstrative slices. | Do not sell the structure as user-facing solution structure. |
| Direct governing-pattern exits | Any locus that makes a stronger claim points to the pattern that governs that claim. | The unfolding structure is overreading itself as method, work, evidence, gate, decision, architecture, or publication authority. |
| Non-workflow boundary | The actual project sequence remains allowed to be nonlinear, iterative, partial, or interrupted. | Lower the artifact to a work plan or method description only if the direct pattern governs that claim. |
| Non-chain topology | Branches, joins, cycles, partial orders, many-to-many constraints, or alternative live next forms remain visible when they matter. | Treat a linear chain as a demonstrative slice until the wider structure is recoverable. |
| Stop, split, return, refresh | Conditions for stopping, splitting, returning to a governing pattern, or refreshing after changed evidence, currentness, or context are named. | The structure becomes a one-way story that cannot localize repair. |

#### A.22.CGUS:4.3 - Descriptions And Demonstrative Slices

Keep the structure separate from descriptions and teaching slices.

```text
ConstraintGovernedUnfoldingStructureDescription@Context:
  kind: U.Episteme
  entityOfConcernRef: ConstraintGovernedUnfoldingStructure@Context
  representationSchemeRef:
  viewpointRef?:
  preservedStructure:
  lostOrCoarsenedStructure:
  declaredUse:
  descriptionUseReturnCondition:
  publicationRefs[]?:
```

```text
DemonstrativeUnfoldingSlice@Context:
  kind: U.Episteme
  entityOfConcernRef: ConstraintGovernedUnfoldingStructure@Context
  demonstrationUseKind:
    happyPath |
    workedSlice |
    firstUseExample |
    promptExample |
    actualCaseReplay |
    variantComparison |
    otherDeclared
  traversalOrOrderingRuleRef:
  includedLocusRefs[]:
  omittedBranchRefs[]:
  loopCompressionPolicyRef?:
  alternativeSliceRefs[]?:
  presentationFormKind:
    orderedList |
    chainDiagram |
    flowCard |
    table |
    narrativePath |
    slideSequence |
    promptBlock |
    graphSlice |
    otherDeclared
  admissibleUse:
  nonAdmissibleUse:
  sliceUseReturnCondition:
```

`DemonstrativeUnfoldingSlice@Context` is the right place for a happy path, P2W chain, P2S chain, cycle steps, prompt example, case replay, or seminar sequence. The slice shows one admissible traversal of the unfolding structure for a declared use. It is not a chain in the world and not a performed-work order.

When a graph-shaped or workflow-shaped description is used for teaching, record which branches, joins, cycles, or alternatives are included, omitted, compressed, or represented by a "return to start" arrow. The slice may be a chain because the reader needs one path; the governed unfolding structure need not be a chain.

A demonstrative slice may also be used before execution as a slot-filling scaffold. The presentation chain holds attention on visible positions such as "first record", "candidate repair", "evaluation row", "gate condition", or "return". Each visible position asks which CGUS field or direct governing pattern must be filled: admitted starting record, starting structure, locus, constraint, invariant, guard, preserved structure, lost structure, admissible next form, stop condition, return condition, method or work link, evidence link, architecture use, or publication use. The chain helps the team plan the structure by filling or rejecting these slots; it does not make the slot filled and does not authorize the work.

Use the scaffold in small passes. First name the visible positions. Then attach each position to `unfoldingLoci[]` or to a direct governing pattern. Then fill constraints, invariants, guards, preserved and lost structure, admissible next forms, and stop or return conditions. If a position cannot be attached to a locus or governing pattern, keep the chain as a seed description or demonstrative slice and do not admit the full unfolding structure yet.

For example, "draft -> evaluate -> repair -> re-evaluate" is a useful presentation chain for an improvement cycle only after the object version, evaluation frame, candidate repair loci, expected evaluation movement, loop-decision locus, and stop or continue condition are recoverable. Before those slots are filled, the chain is a planning scaffold, not an improvement loop and not performed work.

#### A.22.CGUS:4.4 - Direct Governing Pattern Exits

CGUS carries the unfolding structure. It does not absorb stronger claims.

| Stronger claim being made | Direct governing pattern or family |
| --- | --- |
| Atomic bounded change | `A.3.4` |
| Method or method description | `A.3.1`, `A.3.2`, and method-composition patterns |
| Work plan, work entry, or performed work | `A.15.2`, `A.15.5`, `A.15.1`, and neighboring work patterns |
| Evidence, assurance, or gate | `A.10`, `B.3`, `A.20`, `A.21`, `G.6` as current |
| Architecture use, architecture decision, or architecture description | `C.30`, `C.30.ASV`, `C.32.P2S`, `C.32.PAD`, `C.32.ADR`, `C.30.AD` |
| Narrative rendering or publication use | `A.6.3.NAR`, `E.17`, `E.17.0` |
| Improvement of an object version | `E.23`, with evaluation patterns for the declared object |
| Source currentness, decay, edition shift, or refresh orchestration | `G.11` |
| Mathematical lens or formal modeling | `C.29`, `A.6.0`, `A.6.1` |

Use the word `refresh` only when a currentness, telemetry, edition, decay, or slice-local refresh claim is actually current. Otherwise use plain return, stop, split, or repair wording and name the direct governing pattern.

#### A.22.CGUS:4.4a - Direct Governing-Pattern Dependent Records

Some CGUS uses need dependent records that keep adjacent method, work, evidence, architecture, description, or publication claims inspectable. A.22.CGUS does not define those record schemas. It only requires that a CGUS field name the direct governing pattern before a stronger claim is relied on.

For method and work linkage, use the A.15-owned `MethodWorkUnfoldingLinkage@Context` only when the relation among method, method description, role assignment, capability-fit condition, work plan, readiness, performed work, evidence, assurance, or gate must stay inspectable as a relation. If only one method, work-plan, readiness, performed-work, evidence, assurance, or gate claim is current, use that direct governing record instead.

For architecture use, use the C.32.P2S-owned `ArchitectureUnfoldingStructureUse@Project` only when a named unfolding structure is being used as architecture-relevant structure in problem-to-structure architecturing. If the current claim is only grounded architecture, structural view, architecture description, decision, ADR-like projection, measurement, eval, or performed realization work, use the direct pattern for that claim.

This keeps A.22.CGUS thin: it governs the constraint-governed unfolding structure and its safe next-use boundary, while A.15, C.30, C.32, evidence, gate, publication, and domain patterns govern the adjacent records that carry stronger claims.

#### A.22.CGUS:4.5 - Promoted Core Family Cue Examples

The FPF core may promote a few short family cues when a cue helps readers recover a familiar governing pattern and a common blocked overread. This is an example device, not a maintained list of all CGUS families.

For example, `UF.P2S` can be useful when an architecture-facing question moves from problem pressure to candidate, selected, expected, or actual structures. The cue points the reader toward `C.32.P2S` and warns that a P2S card is not itself the architecture decision, architecture description, ADR, or realization work.

For example, `UF.IMP` can be useful when an object version, evaluation frame, candidate repairs, and re-evaluation are current. The cue points toward `E.23` and warns that a retry loop or prompt loop is not quality improvement by shape.

For example, `UF.REFRESH` can be useful when a `G.11` source-currentness relation, telemetry, evidence decay, or edition shift is current. The cue points toward `G.11` and warns that a stale reference set is not current authority.

If no promoted cue helps, omit the cue. Do not invent a core `UF.*` cue merely to make a CGUS use look governed. DPFs and project-local frameworks may carry their own local cue examples when useful, but the governing claim still comes from the local governing-pattern map and the relevant pattern bodies.

### A.22.CGUS:5 - Worked Slices

**Architecture P2S slice.** A team starts with architecture-relevant problem pressure. The unfolding structure may organize problem pressure, unknown structures, candidate structures, architecture characteristics, decision locus, realization work linkage, actual structure feedback, and return conditions. The P2S flow card can describe that organization, but the architecture decision remains governed by `C.32.PAD`, architecture descriptions by `C.30.AD`, and performed work by the A.15 family.

**Abductive search slice.** An inquiry starts from an abductive prompt and a cue set selected for the search. The unfolding structure may organize rival hypotheses, plausibility constraints, hypothesis-generation loci, evidence-return loci, and downstream tests. The structure is not evidence; evidence appears only when an evidence pattern governs the claim.

**Improvement-loop slice.** A pattern version has an evaluation frame and current evaluation result. The unfolding structure may organize candidate repairs, protected tradeoffs, expected evaluation movement, loop-decision locus, and re-evaluation. The loop is not improvement by shape; `E.23` governs improvement only after the object version and evaluation relation are recoverable.

**First-entry seed slice.** A README entry says "develop or review architecture." That line may seed an entry unfolding among problem-side records, candidate first governed records, likely governing-pattern returns, and next readable outputs. The README line is a seed description, not the project's unfolding structure and not a universal FPF route.

**Field-filled scaffold slice.** A team has a visible card sequence "problem pressure -> candidate options -> eval -> repair." At first this is only a demonstrative slice. It becomes a CGUS record only after fields are recoverable:

```text
acceptedStartingRecordRefs[]: ProblemCard@Cooling-v2; EvaluationResult@thermal-margin-v1
acceptedStartingStructureRefs[]: current module-placement structure
declaredStructureSubstrateRef: architecture-facing candidate synthesis and improvement-loop structure
unfoldingLoci[]: pressure locus; candidate-set locus; eval-result locus; repair-choice locus; return locus
constraintRefs[]: thermal margin threshold; service-access constraint; accepted-loss boundary
invariantRefs[]: cooling path must remain maintainable
guardedTransitionRefs[]: candidate enters repair only after eval-result relation is named
preservedStructure: candidate alternatives plus repair-locality relation
lostOrHiddenStructure: rejected-candidate details not shown in the teaching chain
admissibleNextFormKindRefs[]: C.32 candidate palette update; E.23 improvement input; C.32.PAD decision only later
structureUseReturnCondition: return to C.32 when a new candidate structure appears; return to E.23 when the changed object version is evaluated
stopCondition: keep as DemonstrativeUnfoldingSlice until candidate-set and eval relations are named
```

The same visible chain helps planning because each position asks for a slot. It does not make the project follow that order and does not authorize work.

**Reference-currentness slice.** A SoTA pack relies on telemetry and admitted reference-publication editions that may decay. CGUS may organize the current reference set, edition-shift loci, decay triggers, possible deprecation or reship, and return condition. The structure is not the currentness decision; `G.11` governs freshness, telemetry, decay, deprecation, reship, and no-change claims.

**Physical-modeling slice.** A team models a physical system or another governed EntityOfConcern whose behavior depends on component relations, conservation-like constraints, operating modes, calibration data, and analysis goals. CGUS may organize the model structure, admitted measured data, mode-change loci, compiler boundary, solver boundary, surrogate-substitution boundary, and return to calibration or model-discovery work. In a digital-twin case, the physical entity, digital model, measured-data history, simulation outputs, services, and bidirectional correspondence links remain different loci or records and relations governed by their direct patterns. The simulation run, generated code, exchange package, AI-assisted model edit, calibration result, and digital-twin publication are also separate produced carriers, work outputs, calibration records, or publications. Acausal modeling is useful here because it shows that relations and constraints can be stated before a calculation direction is chosen; `C.29`, `G.11`, `E.23`, evidence patterns, and domain DPF patterns govern stronger mathematical, currentness, evaluation, evidence, or domain-validity claims.

**Method/work linkage slice.** A method description is admitted because it may realize a governed structure change or change set. CGUS may organize the method relation, work-plan seed, readiness condition, expected structure effect, evidence or gate linkage, and stop condition. It does not authorize work. The method, plan, work-entry readiness, performed work, evidence, assurance, and gate claims remain with A.3, A.15, A.10, B.3, A.20, and A.21.

### A.22.CGUS:6 - Bias-Annotation

| Bias risk | Mitigation |
| --- | --- |
| Workflow bias | Name admissible next forms and actual non-workflow boundary. Use work and method patterns only when work or method claims are current. |
| Semio-bias | Treat cards, graphs, tables, route prose, slides, README entries, and narratives as descriptions or demonstrative slices unless the governed unfolding structure itself is named. |
| E.18 parent bias | Use `E.18.3` only for transformation-flow unfolding. Narrative, abduction, grounding, improvement, refresh, and first-entry seeds keep their direct governing patterns. |
| Shadow-spec bias | Promoted core family cues and README seeds are retrieval aids. They do not outrank pattern bodies, define a second navigation system, or stand in for DPF/local governing maps. |
| Lexical trigger bias | Words such as route, path, loop, process, workflow, diffusion, unfolding, graph, or sequence do not admit CGUS by themselves. Run the admission test. |

### A.22.CGUS:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-CGUS-1 Structure kind.** | The object is `ConstraintGovernedUnfoldingStructure@Context <: U.Structure` or a named narrower `U.Structure` specialization. | Lower to note, seed, description, route card, method description, or governing-pattern record. |
| **CC-CGUS-2 Loci and constraints.** | Several loci and cross-locus constraints are named. | Add loci and constraints or stop using CGUS. |
| **CC-CGUS-3 Description separation.** | Descriptions, views, diagrams, tables, graph expressions, narratives, slides, and README entries do not become the structure. | Recast them as `ConstraintGovernedUnfoldingStructureDescription` or `DemonstrativeUnfoldingSlice` with declared use. |
| **CC-CGUS-4 Direct governing patterns.** | Method, work, evidence, gate, decision, architecture, publication, refresh, and mathematical claims point to direct governing patterns. | Add governing-pattern exits or narrow the claim. |
| **CC-CGUS-5 Non-workflow boundary.** | The structure does not prescribe performed-work order by itself. | Move work-order claims to a work plan or method description if justified. |
| **CC-CGUS-6 Admissible next form.** | At least one admissible next form or demonstrative slice is named. | Keep the artifact internal until a next use is recoverable. |
| **CC-CGUS-7 Stop and return.** | Stop, split, return, and currentness-refresh conditions are recoverable where relevant. | Add the condition or lower the structure to a one-use explanation. |
| **CC-CGUS-8 Graph-shaped structure coverage.** | If the admitted starting record set, starting structure set, or visible expression is graph-shaped, case-like, or workflow-shaped, branching, joining, cyclic, partial-order, and alternative-live-next-form structure is preserved or explicitly lost. | Do not collapse the object to a chain. Make the chain a demonstrative slice and name the omitted graph structure. |

### A.22.CGUS:8 - Common Anti-Patterns And Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Pretty route as ontology** | A graph, table, route card, or slide deck is treated as the structure. | Name the structure separately and make the visible artifact a description or demonstrative slice. |
| **Universal P2W parent** | P2W is used as the parent for architecture, narrative, abduction, grounding, and refresh. | Use P2W as a rich transformation-flow family; use CGUS for the shared constraint-governed unfolding structure and direct governing patterns for each family. |
| **Loop word as improvement** | A retry loop or prompt loop is called improvement. | Open `E.23`; require object version, evaluation frame, candidate repair loci, and re-evaluation. |
| **README route authority** | A public entry line is treated as a mandatory FPF procedure. | Recast it as `EntryUnfoldingSeedDescription@Readme` and return to `E.11` plus direct governing patterns. |
| **Diffusion ontology import** | The diffusion analogy becomes mathematical diffusion, fixed point, CSP, sheaf, or category semantics. | Keep the analogy explanatory only; open `C.29` by a new decision if a mathematical lens is claimed. |
| **Solver or agent as ontology** | An execution artifact, such as a solver run, compiler output, or AI-assisted model edit, is treated as the governed unfolding structure. | Separate the reusable model structure from the execution or publication artifact. Use CGUS for the relation and constraint structure; use the direct mathematical, currentness, evaluation, evidence, publication, or domain pattern for the stronger claim. |

### A.22.CGUS:9 - Consequences

CGUS gives FPF a way to preserve route-shaped usefulness without turning route-shaped artifacts into workflows. A practitioner can see admitted starting records, current starting structures, constraints, possible next forms, alternatives, and return conditions while still knowing which direct pattern governs method, work, evidence, gate, decision, architecture, publication, refresh, or mathematical use.

The cost is extra kind discipline. A conforming use must name several loci, preserved and lost structure, non-admissible overreads, and direct pattern exits. If that is too heavy, the right result is usually a compact seed description or demonstrative slice, not a full CGUS record.

### A.22.CGUS:10 - Rationale

The selected design is a thin A.22 specialization of `U.Structure` because the recurring object is real but not a new root ontology. Constraint-based process modeling, case-management practice, artifact-centric modeling, acausal modeling, architecture-description practice, and FPF's own pattern use all separate a constraint-bearing structure from a performed trace, work order, view, publication, solver run, or example path. FPF adopts that separation as a constraint-governed unfolding structure and refuses to import one universal process calculus.

Physical modeling makes the same distinction concrete. In acausal modeling, component relations, quantities conserved across connections, and mode conditions can be declared before the model is compiled and solved in one chosen direction. The FPF import is only the general architecture of the move: structure and constraints first; derived calculation, demonstration, calibration, publication, or work use later under direct governing patterns.

CGUS is deliberately close to A.22. It is a `U.Structure` over a declared substrate in a bounded context. Descriptions, views, graph renderings, route cards, README entries, and examples help humans use it; they do not become it.

### A.22.CGUS:11 - SoTA-Echoing

| Exact source or practice anchor | FPF adoption | Boundary |
| --- | --- | --- |
| Object Management Group, *Case Management Model and Notation (CMMN) Version 1.1*, December 2016 | Adopt the weakly structured case-work pressure: possible work items and constraints may be visible without selecting one performed-work order. | Do not import CMMN notation or treat CGUS as a case-management method. |
| Chiariello, Fionda, Ielo, and Ricca, "Direct Encoding of Declare Constraints in ASP", arXiv:2412.10152, 2024; Burattin, Maggi, and Sperduti, "Conformance Checking Based on Multi-Perspective Declarative Process Models", arXiv:1503.04957, 2015 | Adopt declarative constraints and multi-perspective loci as pressure for admissible traces without first selecting one imperative sequence. | FPF does not import Declare, MP-Declare, ASP, or conformance-checking ontology. |
| Hildebrandt and Mukkamala, "Declarative Event-Based Workflow as Distributed Dynamic Condition Response Graphs", EPTCS 69, 2011 | Use DCR relation pressure for condition, response, include, exclude, role, and distribution-like loci. | Do not import DCR graph semantics as FPF workflow ontology. |
| Bagheri Hariri, Calvanese, Montali, Santoso, and Solomakhin, "Verification of Semantically-Enhanced Artifact Systems", arXiv:1308.6292, 2013, with artifact-centric and GSM lineage | Adapt attention to object/lifecycle state, stages, milestones, guards, and artifact state as pressure for named loci and guarded transitions. | CGUS does not become an artifact lifecycle method, database schema, or verification method. |
| ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise - Architecture description* | Use architecture-description separation as pressure to keep structure, description, viewpoint, view, correspondence, and publication apart. | Architecture-specific claims remain with `C.30` and `C.32`. |
| Modelica Association, *Modelica Language Specification* 3.6 (2023) and 3.7 (2026); JuliaHub, Dyad product page and Dyad documentation v3.0.0 | Adopt only the relation-first pattern: model components expose relations, connection constraints, units, conservation relations, and modes before one causal direction, calculation order, compiler output, solver run, or simulation trace is selected. | FPF does not import DAE, Modelica, Dyad, solver, compiler, or AI-agent ontology. A solver run, compiler output, or AI-assisted edit is a use over a model structure, not the CGUS itself. |
| Ma, Gowda, Anantharaman, Laughman, Shah, and Rackauckas, "ModelingToolkit: A Composable Graph Transformation System For Equation-Based Modeling", arXiv:2103.05244; Rackauckas et al., "Composing Modeling and Simulation with Machine Learning in Julia", arXiv:2105.05946; Functional Mock-up Interface standard | Use the model-toolchain separation to keep reusable symbolic model structure, structural transformations, analysis records, calibration records, model-discovery records, surrogate-substitution relations, model-exchange packages, and result publications as different loci or direct governing-pattern records. | FPF does not import FMI, digital-twin, ML-surrogate, calibration, or co-simulation ontology. Mathematical model claims use `C.29`; currentness, evaluation, evidence, publication, and domain-validity claims exit to their direct governing patterns. |
| FPF pattern-language practice | Use demonstrative slices and entry seeds for learnability while keeping pattern bodies as governing authority. | A first-entry route, example, or public card is not the specification. |

### A.22.CGUS:12 - Relations

Specializes: the `A.22` use of `U.Structure` when the selected structure is `ConstraintGovernedUnfoldingStructure@Context` and its loci, constraints, preserved or lost structure, admissible next forms, and direct governing-pattern exits are current.

Specialized by: `E.18.3` for transformation-flow unfolding structures, and by local blocks in `E.18.1`, `C.32.P2S`, `B.5.2`, `A.6.3.NAR`, `E.23`, `C.13`, `B.3.5`, and `C.3` when their admission tests pass.

Coordinates with: `E.11` for entry seeds and first-entry expansions, `E.9` and `E.9.DA` for campaign carry-through checks, `E.10.MOVE` and `C.2.P.DR` for lexical and declarative-representation repair, `G.11` for currentness and refresh claims, and `E.17` for publication of descriptions or demonstrative slices.

Does not replace: `A.3.1`, `A.3.2`, `A.15`, `A.10`, `B.3`, `A.20`, `A.21`, `C.30`, `C.32.PAD`, `C.32.ADR`, `C.29`, `G.11`, or any direct governing pattern for stronger claims.

### A.22.CGUS:End

