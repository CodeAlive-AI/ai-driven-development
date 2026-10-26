## C.34 - Assess Structural Correspondence for Architecture Use (Equivalence and Morphisms)

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.34:1 - Problem frame

Use this pattern when two descriptions, views, models, generated outputs, or realized observations that carry or describe selected structure are being treated as the same enough for architecture work and the practitioner must say what selected structure is preserved, what is lost, and which use the correspondence licenses.

Primary working reader: an architect, reviewer, or model-assisted practitioner comparing views, descriptions, source models, generated graphs, candidate architectures, realized structures, abstraction levels, coarsened models, or transformed models.

Typical entry phrases:

```text
"These two diagrams look equivalent; what relation is actually preserved?"
"The model query and the architecture view should correspond; what was lost in projection?"
"The generated graph matches the module graph; is the semantic relation the same?"
"This candidate preserves dataflow but changes control authority."
"The neural architecture replacement keeps shape but changes routing and memory placement."
"The narrative order preserves the architecture trade-off; what selected source structure is still same enough for this use?"
```

The first useful result explains which correspondence supports the intended architecture use. An ordinary account can suffice; reuse an adequate existing account. `StructuralPreservationAdequacyNote@Context` is an optional working form:

```text
StructuralPreservationAdequacyNote@Context:
  selectedSourceStructureRefs:
  selectedTargetStructureRefs:
  architectureClaimRef?:
  mappingMode:
    exactEquivalence | isomorphism | homomorphism | correspondence |
    projection | abstraction | coarsening | simulationRelation |
    nearSameness | declaredOther
  preservedRelationsOrConstraints:
  preservedInvariantsOrCompositions?:
  lostStructure?:
  relationTypeSemantics?:
  relationObservationClass?:
  directionality:
  scopeOrScaleWindow?:
  lensUseOutputRef?:
  correspondenceRecordRef?:
  constraintGovernedUnfoldingStructureRefs?:
  admissibleUse:
  nonAdmissibleUse?:
  preservationLossReturnCondition?:
  nextClaimOrRuleRef?:
  receivingClaimKind?:
```

After using C.34, another practitioner can recover the claimed correspondence, preserved structure, direction and scope, any loss or uncertainty that limits reliance, and the use it supports.

What C.34 buys in practice: the practitioner can say "same enough for this use" without smuggling in stronger equivalence. The pattern makes sameness conditional on preserved relation, declared loss, and receiving use.

Ordinary working move: put the source and target structures side by side, circle the relation or constraint that must survive, name any relation that does not survive, and choose a warranted mapping that supports the next use without seeking a stronger result unless needed.

Not this pattern when the current claim is only mathematical-lens use, generic bridge translation, measurement, structural view adequacy, architecture-description correspondence, candidate synthesis, decision, evidence, assurance, gate, release, or work authorization. Use the pattern that defines or tests that current claim and keep C.34 only for the architecture-specific preservation claim.

### C.34:2 - Problem

Architecture work often needs "same enough" claims. A view should correspond to a description. A generated graph should preserve selected dependencies. A candidate should preserve required interfaces while changing placement. A realized structure should match an expected selected structure enough for an evaluation or decision repair. A neural-network substitution should preserve dataflow or routing while changing memory and compute trade-offs.

The dangerous shortcut is to accept visual similarity, label sameness, graph isomorphism, or formal vocabulary as adequacy. An edge-isomorphic graph can lose relation semantics. A projection can preserve module names while dropping control authority. A category-theoretic morphism can be useful as a C.29 lens without proving architecture equivalence. A DSM cluster can preserve co-change pressure while losing functional bearer semantics.

C.34 makes the preservation claim explicit before the result is used.

### C.34:3 - Forces

| Force | Tension |
| --- | --- |
| Equivalence vs use | Exact equivalence is rare and often unnecessary; the declared use decides how much preservation is enough. |
| Formal rigor vs practitioner action | Formal mapping modes help only when preserved and lost structure are named in architecture terms. |
| Shape vs semantics | Two graphs, views, or diagrams can have the same shape while their relation types differ. |
| Compression vs loss | Projection, abstraction, coarsening, and simulation relations make work possible by dropping structure. In a chain from selected source structures to architecture, architecture description or view, and narrative or framework carrier, preservation must be checked relation by relation rather than claimed as one global sameness. |
| Cross-context reach | A mapping across teams, source traditions, tool models, or holon levels needs the applicable Bridge predicate and conformance test when substitution or transfer is claimed. |

### C.34:4 - Solution

Establish what must survive for the next architecture action and what the correspondence preserves. State any material loss or uncertainty. Use the optional note when it helps retain or share that account.

Work in this order:

1. Name the selected source structures and selected target structures. Do not start from labels, diagrams, or tool objects alone.
2. Name the intended architecture use: view correspondence, candidate comparison, structure recovery, generated-output admission, realization check, eval support, decision repair, or another receiving claim.
3. Select a warranted mapping mode sufficient for the use. A weaker sufficient correspondence can finish the work; an already established stronger result can be reused within its scope. Use `exactEquivalence` only when preservation of the entire selected structure is established within the declared scope.
4. State preserved relations or constraints in clear domain terms. Use FPF distinctions where the claim depends on them. Include relation-type semantics when edge or link meaning changes the use.
5. State directionality and scope or scale window, with any material lost or hidden structure. Distinguish an observed loss from preservation left unestablished by incomplete observation. Neither supports a claim requiring the missing preservation, but each selects a different next inquiry or repair.
6. Cite `C.29` only when a mathematical object, graph match, functor, invariant, entropy, or formal mapping is being used as a lens.
7. Cite `C.30.ASV`, `C.30.AD`, or their correspondence records when the relation is view or architecture-description correspondence.
8. Cite `A.6.3.NAR` when the target episteme or representation is a narrative rendering whose ordering rationale, preserved selected source structure, source-return condition, and any unresolved stronger assertion with the pattern that defines it must stay inspectable.
9. Use `F.9` for cross-context or cross-tradition substitution or claim transport that requires a Bridge. Use `F.15` when the receiving use needs its static or regression conformance tests.
10. Stop when the supported use and its grounds are clear, with any material limitation and the condition for resolving it. Apply an additional mapping, Bridge or conformance rule when that use requires it.

CGUS-aware neighbor use: when a route-shaped publication card, narrative sequence, generated route card, framework publication, or demonstrative slice is claimed to preserve a constraint-governed unfolding structure, use C.34 only to check the sameness relation. The result names selected source and target structures, mapping mode, preserved constraints, preserved ordering or branching relations, lost alternatives, directionality, and admissible use. `A.22.CGUS`, `E.18.3`, `C.32.P2S`, or another direct structure pattern continues to define or constrain the selected unfolding `U.Structure`; cite an exact `ClaimGraph` only if that structure claim must travel independently. A demonstrative slice is a `U.Episteme` that presents one traversal of a qualified CGUS. Its correspondence to that structure may be checked here; `DemonstrativeUnfoldingSlice@Context` is a readable lineage cue, not an exact slice identity. When that presentation is a narrative, `A.6.3.NAR` defines its source selection, ordering and connective account, preservation/loss, use, and return, not the selected structure. The C.34 result says only whether the target is same enough for the declared architecture use.

### C.34:5 - Archetypal Grounding

Tell: C.34 is the pattern for a declared architecture preservation claim. It is used when a practitioner says that one description, view, model, generated output, or realized observation is same enough as another for a specific architecture use. The account identifies a sufficient warranted mapping, preserved structure, direction, scope and supported use, together with any material loss or uncertainty and the concrete rule needed by further reliance.

Show - view and description case. Two architecture diagrams are edge-isomorphic. In one diagram an edge means data dependency; in the other it means control authority. C.34 records mapping mode `nearSameness`, preserved node partition, lost relation-type semantics, and non-admissible use "control separation decision." Recover the relation semantics through `C.30.ASV`, `C.30.TFS-REL` or `C.30.LCA` before relying on the mapping for control separation. Its supported node-partition use remains available.

Show - source model and generated graph case. A code-agent dependency graph matches module names in the model used as the source, but marks several edges inferred and several regions unexplored. C.34 records relation observation class, directionality, preserved dependency hints, lost dynamic wiring, and non-admissible use "safe-change authority." The graph may help inspect candidate dependencies, but it cannot prove release readiness.

Show - candidate and realized structure case. A candidate architecture promises that a service split preserves interface substitutability, but the realized structure adds shared storage and a hidden orchestration dependency. C.34 records preserved interface signatures, lost runtime independence, changed coupling, and a preservation-loss condition that reopens the dependent decision premise before its reuse. Use `A.6.M` for substitutability, `C.31` for the function-bearer relation, `C.30` for the changed structure and `C.32.PAD` for the affected decision as each question requires.

Show - neural substitution case. A candidate replaces an attention block with an SSM block. C.34 asks which selected structures are preserved: sequence dataflow, routing interface, memory access, latency envelope, training resource boundary, or inference resource boundary. Shape sameness or benchmark improvement does not by itself preserve the architecture relation needed by the next claim.

Show - selected source structure and narrative structure case. An architecture narrative orders a candidate set as "pressure, alternative, trade-off, decision, residual." C.34 records mapping mode `correspondence`, preserved structure `candidate alternative and selected trade-off relation`, lost structure `full Pareto-front detail and rejected-candidate evals`, directionality `selected source structure to narrative only`, and admissible use `team orientation and decision memory`. The narrative order is not exact equivalence and does not license implementation, evidence, or assurance use without the rule that defines or tests that downstream claim.

### C.34:6 - Bias-Annotation

| Bias | How C.34 counters it |
| --- | --- |
| Shape-equivalence bias | Require relation-type semantics, preserved structure, and lost structure. Same nodes or edges are not enough. |
| Formalism-laundering bias | Keep graph isomorphism, morphism, functor, entropy, or simulation wording as lens or mapping support until the architecture use, preserved structure, and loss are declared. |
| Symmetric-equivalence overclaim | Require directionality and scope. A projection, abstraction, simulation relation, or coarsening often licenses one direction only. |
| Semantic-loss hiding | Make lost control authority, allocation, bearer semantics, placement, timing, confidence, or source-tradition meaning explicit before the mapping is reused. |
| Bridge-bypass bias | Handle cross-context substitution, source-tradition transfer, and later conformance strengthening under `F.9` or `F.15` instead of letting C.34 authorize the transfer alone. |

### C.34:7 - Conformance checklist

| Check | Pass condition |
| --- | --- |
| `CC-C34-1` | Source and target structures are named before the mapping claim. |
| `CC-C34-2` | The selected mapping is warranted and sufficient for the declared use; no stronger result is required merely to complete the assessment. |
| `CC-C34-3` | Preserved relations or constraints and any material loss or uncertainty are stated; absence of a preservation result is distinguished from an observed loss. |
| `CC-C34-4` | Relation-type semantics, observation class, directionality, and scope are present when they affect use. |
| `CC-C34-5` | Each current mathematical-lens, view, description, Bridge, conformance, candidate-synthesis, measurement, eval, decision, evidence, assurance, gate, release, or work-authorization claim uses the pattern that defines or tests it. |
| `CC-C34-6` | The supported use and its grounds are clear, with any material limitation, recovery condition and rule required by the next reliance. |

### C.34:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair move |
| --- | --- | --- |
| Edge-isomorphism overread | Isomorphic graphs can preserve shape while changing edge meaning, relation observation class, or use. | Record relation-type semantics, preserved relation, lost relation, and non-admissible use. |
| Semantic-loss hiding | A projection or coarsening can look clean because it drops exactly the structure that the next decision needs. | Name lost structure and preservation-loss return condition before comparison, decision repair, or candidate admission. |
| Exact-equivalence overclaim | Exact equivalence is stronger than most architecture uses need and is often false. | Use a warranted correspondence, projection, abstraction, coarsening, simulation relation or near-sameness when sufficient. Exact equivalence may be retained when independently justified. |
| Generated graph proof overclaim | A generated graph can match labels or topology while hiding dynamic wiring, confidence, or unexplored regions. | Use C.34 only for the preservation claim; handle generated-carrier admission under `C.35`, and apply the rules that define evidence, assurance, gate, or release claims when those claims are current. |
| Narrative-order equivalence overclaim | A narrative can preserve a useful path through selected source structure while dropping alternatives, relation semantics, measurements, or directionality. | Record the weakest adequate correspondence, preserved structure, lost structure, directionality, and non-admissible use; use `A.6.3.NAR` for the narrative rendering relation. |
| Formal lens laundering | A morphism, functor, entropy value, or graph match sounds rigorous but may be local to a mathematical object. | Handle lens use under `C.29`; use C.34 only after preserved structure, lost structure, mapping mode, and architecture use are stated. |
| Bridge-governance bypass | A cross-context or cross-tradition mapping can preserve local structure while losing local sense. | Use `F.9` for the Bridge. Apply `F.15` when the current or changed use needs its conformance tests; reuse an adequate existing result. |

### C.34:9 - Consequences

Positive consequences:

- Architects can use partial sameness without pretending to have identity. This keeps comparison, projection, generated-output admission, realization checks, and decision repair usable.
- Formal methods become useful at the right locus: graph matching, category-theoretic morphisms, entropy, and simulation relations can support the mapping without becoming architecture ontology.
- Cross-context and source-tradition risks are visible early because directionality, scope, bridge loss, and the applicable conformance rules are named.
- Later decisions can be repaired locally: the preservation note says which relation failed, which structure was lost, and which claim or check must be reopened.

Costs and trade-offs:

- Assessing correspondence takes attention. Reuse an adequate account; investigate further when a plausible preservation difference could change the intended use.
- The pattern does not prove formal equivalence by itself. When proof, measurement, evidence, assurance, gate, release, or work authorization is current, apply the corresponding rule or test.
- Some comparisons will lower from equivalence to correspondence or near-sameness. That lowering is a success when it prevents a false downstream claim.

### C.34:10 - Rationale

Architecture preservation is use-relative. The same two structures can be equivalent for one use, merely corresponding for another, and unusable for a third. For this architecture-specific claim, start from source and target selected structures, then establish a warranted correspondence sufficient for the next architecture use.

This keeps C.34 separate from its neighbors. `C.29` defines mathematical-lens-use accounts. `C.30.AD` and `C.30.ASV` govern architecture-description and structural-view adequacy, with records for uses that need them. `F.9` defines cross-context Bridges. `F.15` supplies static and regression conformance tests over a finite slice of exact governed objects and versions for one receiving use. `C.32` describes candidate synthesis. C.34 contributes the preservation claim those uses may need, but it does not replace them.

The source families explain the safeguards. Structural-equivalence research shows that symmetry can compact search only under explicit conditions. Applied category theory shows why preservation maps are powerful but still formal lenses until tied to the architecture use. MBSE view practice makes projection and omitted structure ordinary. Sapunov and ToCS, plus GonzoML, show why observed relation maps and neural substitution labels need typed relation, confidence, and source-label recovery before architecture use.

### C.34:11 - SoTA-Echoing

| Source or practice line | Use of the contribution | Contribution to the assessment | Boundary of use |
| --- | --- | --- | --- |
| Yang et al., `Structural Equivalence in Subgraph Matching`, arXiv:2301.03161 | Adapt structural-equivalence and symmetry discipline. | Supports a warranted mapping mode and the distinction between shape and the relations needed for use. | Subgraph structural equivalence does not define holon architecture equivalence outside declared structures and use. Reopen when the source graph, target graph, or use changes. |
| Fong and Spivak, `Seven Sketches in Compositionality`, arXiv:1803.05316 | Adapt applied category-theory preservation language through `C.29`. | Keeps morphism, functor, sketch, and composition vocabulary tied to preserved structure, lost structure, mapping mode, and architecture use. | Older source is lineage and still useful as applied compositional practice, but it does not become the default FPF architecture ontology. |
| Multi-view architecture and MBSE query and view practice | Adopt the ordinary need for view correspondence, projection, query, and coarsening. | Supports view and description correspondence under `C.30.AD` and `C.30.ASV`. | View output or query output is not architecture and not realized structure. Reopen when viewpoint, query rule, model edition, or described structure changes. |
| Sapunov, ToCS, and code-agent architecture-map practice | Adapt partial-observation preservation discipline. | Makes relation observation class, inferred edges, unexplored regions, confidence and active-passive gap conditions on the warranted preservation claim. Incomplete observation can leave preservation unknown without demonstrating structural loss. | A code-agent map, JSON probe, dependency F1, invariant F1, or active-passive gap does not prove architecture equivalence, safe change, assurance, gate passage, or release readiness. |
| GonzoML neural-network architecture intake | Adapt neural architecture operation language. | Distinguishes dataflow, routing, memory and cache placement, resource boundaries, block substitution and affected characteristics in neural structure substitution. | Use clear source-local meanings directly. Recover an unresolved selected structure or preservation relation when it changes the architecture claim; benchmark gains alone do not establish that preservation. |

### C.34:12 - Relations

- **Builds on:** `A.22`, `C.30`, `C.30.ASV`, `C.30.AD`, `C.29`, and `F.9`.
- **Uses:** `C.16`, `C.25`, and `C.32.ACE` when a preservation, similarity, distance, entropy, loss, or compression claim is recorded as a reading or eval result.
- **Coordinates with:** `C.32`, `C.32.PAD`, `C.32.ADR`, `C.30.TFS-REL`, `C.30.STRAT`, `A.6.M`, `A.6.3.NAR`, `C.31`, `C.31.ASAP`, `E.18`, and `F.15`.
- **Boundary:** C.34 tests declared preservation adequacy for an architecture use. It does not make a formalism ontology, select a candidate, decide a project, establish evidence or assurance, or authorize substitution across contexts; that substitution still requires the applicable Bridge predicate and conformance rule.

### C.34:End
