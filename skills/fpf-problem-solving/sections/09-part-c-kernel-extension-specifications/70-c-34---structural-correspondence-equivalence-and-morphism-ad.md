## C.34 - Structural Correspondence, Equivalence, and Morphism Adequacy

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.34:1 - Problem frame

Use this pattern when two structure-bearing objects are being treated as the same enough for architecture work and the practitioner must say what selected structure is preserved, what is lost, and which use the correspondence licenses.

Primary working reader: an architect, reviewer, or model-assisted practitioner comparing views, descriptions, source models, generated graphs, candidate architectures, realized structures, abstraction levels, coarsened models, or transformed models.

Typical entry phrases:

```text
"These two diagrams look equivalent; what relation is actually preserved?"
"The model query and the architecture view should correspond; what was lost in projection?"
"The generated graph matches the module graph; is the semantic relation the same?"
"This candidate preserves dataflow but changes control authority."
"The neural architecture replacement keeps shape but changes routing and memory placement."
```

The first useful output is `StructuralPreservationAdequacyNote@Context`:

```text
StructuralPreservationAdequacyNote@Context:
  sourceStructureRefs:
  targetStructureRefs:
  architectureClaimRef?:
  mappingMode:
    exactEquivalence | isomorphism | homomorphism | correspondence |
    projection | abstraction | coarsening | simulationRelation |
    nearSameness | declaredOther
  preservedRelationsOrConstraints:
  preservedInvariantsOrCompositions?:
  lostStructure:
  relationTypeSemantics?:
  sourceObservationClass?:
  directionality:
  scopeOrScaleWindow?:
  lensUseOutputRef?:
  correspondenceRecordRef?:
  admissibleUse:
  nonAdmissibleUse:
  sourceReturnCondition:
  receivingOwnerOrPatternRef:
  receivingClaimKind:
```

Adoption test: after using C.34, another practitioner can tell which mapping mode is being claimed, which structure is preserved, which structure is lost, whether the relation is directional or scoped, and which downstream claim is licensed.

What C.34 buys in practice: the practitioner can say "same enough for this use" without smuggling in stronger equivalence. The pattern makes sameness conditional on preserved relation, declared loss, and receiving use.

Ordinary working move: put the source and target structures side by side, circle the relation or constraint that must survive, name the relation that does not survive, and choose the weakest mapping word that still supports the next use.

Not this pattern when the current claim is only mathematical-lens use, generic bridge translation, measurement, structural view adequacy, architecture-description correspondence, candidate synthesis, decision, evidence, assurance, gate, release, or work authorization. Use the direct owner and keep C.34 only for the architecture-specific preservation claim.

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
| Compression vs loss | Projection, abstraction, coarsening, and simulation relations make work possible by dropping structure. |
| Cross-context reach | A mapping across teams, source traditions, tool models, or holon levels needs bridge and conformance owners when substitution or transfer is claimed. |

### C.34:4 - Solution

Create one `StructuralPreservationAdequacyNote@Context` before relying on the same-enough claim.

Read the note as a disciplined "same enough" card. It does not ask for perfect identity unless the use requires it; it asks what must survive for the next architecture action and what loss remains visible.

Work in this order:

1. Name source and target structures. Do not start from labels, diagrams, or tool objects alone.
2. Name the intended architecture use: view correspondence, candidate comparison, source recovery, generated-output admission, realization check, eval support, decision repair, or another receiving claim.
3. Choose the weakest mapping mode that is adequate for the use. Use `exactEquivalence` only when empty loss is justified.
4. State preserved relations or constraints in domain and FPF terms. Include relation-type semantics when edge or link meaning changes the use.
5. State lost structure, hidden structure, directionality, and scope or scale window.
6. Cite `C.29` only when a mathematical object, graph match, functor, invariant, entropy, or formal mapping is being used as a lens.
7. Cite `C.30.ASV`, `C.30.AD`, or their correspondence records when the relation is view or architecture-description correspondence.
8. Cite `F.9` or `F.15` when the claim crosses bounded contexts, source traditions, or later conformance strengthening.
9. Stop when admissible use, non-admissible use, source-return condition, receiving owner, and receiving claim kind are named.

### C.34:5 - Archetypal Grounding

Tell: C.34 is the pattern for a declared architecture preservation claim. It is used when a practitioner says that one structure-bearing object is the same enough as another for a specific architecture use. The pattern does not ask for the strongest possible proof. It asks for the weakest adequate mapping mode, preserved structure, lost structure, directionality, scope, admissible use, and receiving owner.

Show - view and description case. Two architecture diagrams are edge-isomorphic. In one diagram an edge means data dependency; in the other it means control authority. C.34 records mapping mode `nearSameness`, preserved node partition, lost relation-type semantics, and non-admissible use "control separation decision." The repair is to recover relation semantics through `C.30.ASV`, `C.30.TFS-REL`, or `C.30.LCA` before using the mapping for architecture work.

Show - source model and generated graph case. A code-agent dependency graph matches module names in a source model but marks several edges inferred and several regions unexplored. C.34 records source observation class, directionality, preserved dependency hints, lost dynamic wiring, and non-admissible use "safe-change authority." The graph may help inspect candidate dependencies, but it cannot prove release readiness.

Show - candidate and realized structure case. A candidate architecture promises that a service split preserves interface substitutability, but the realized structure adds shared storage and a hidden orchestration dependency. C.34 records preserved interface signatures, lost runtime independence, changed coupling, and source return to `A.6.M`, `C.31`, `C.30`, and `C.32.PAD` before the decision is reused.

Show - neural substitution case. A candidate replaces an attention block with an SSM block. C.34 asks which selected structures are preserved: sequence dataflow, routing interface, memory access, latency envelope, training resource boundary, or inference resource boundary. Shape sameness or benchmark improvement does not by itself preserve the architecture relation needed by the next claim.

### C.34:6 - Bias-Annotation

| Bias | How C.34 counters it |
| --- | --- |
| Shape-equivalence bias | Require relation-type semantics, preserved structure, and lost structure. Same nodes or edges are not enough. |
| Formalism-laundering bias | Keep graph isomorphism, morphism, functor, entropy, or simulation wording as lens or mapping support until the architecture use, preserved structure, and loss are declared. |
| Symmetric-equivalence overclaim | Require directionality and scope. A projection, abstraction, simulation relation, or coarsening often licenses one direction only. |
| Semantic-loss hiding | Make lost control authority, allocation, bearer semantics, placement, timing, confidence, or source-tradition meaning explicit before the mapping is reused. |
| Bridge-bypass bias | Route cross-context substitution, source-tradition transfer, and later conformance strengthening to `F.9` or `F.15` instead of letting C.34 authorize the transfer alone. |

### C.34:7 - Conformance checklist

| Check | Pass condition |
| --- | --- |
| `CC-C34-1` | Source and target structures are named before the mapping claim. |
| `CC-C34-2` | Mapping mode is selected and is not stronger than the declared use needs. |
| `CC-C34-3` | Preserved relations or constraints and lost structure are both stated. |
| `CC-C34-4` | Relation-type semantics, observation class, directionality, and scope are present when they affect use. |
| `CC-C34-5` | Mathematical-lens, view, description, bridge, conformance, candidate-synthesis, measurement, eval, decision, evidence, assurance, gate, release, and work-authorization claims route to their owners. |
| `CC-C34-6` | Admissible use, non-admissible use, source-return condition, receiving owner, and receiving claim kind are named. |

### C.34:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair move |
| --- | --- | --- |
| Edge-isomorphism overread | Isomorphic graphs can preserve shape while changing edge meaning, source observation class, or use. | Record relation-type semantics, preserved relation, lost relation, and non-admissible use. |
| Semantic-loss hiding | A projection or coarsening can look clean because it drops exactly the structure that the next decision needs. | Name lost structure and source-return condition before comparison, decision repair, or candidate admission. |
| Exact-equivalence overclaim | Exact equivalence is stronger than most architecture uses need and is often false. | Choose the weakest adequate mapping mode: correspondence, projection, abstraction, coarsening, simulation relation, or near-sameness when that is enough. |
| Generated graph proof overclaim | A generated graph can match labels or topology while hiding dynamic wiring, confidence, or unexplored regions. | Use C.34 only for the preservation claim; route generated-carrier admission to `C.35` and evidence, assurance, gate, or release claims to their owners. |
| Formal lens laundering | A morphism, functor, entropy value, or graph match sounds rigorous but may be local to a mathematical object. | Route lens use to `C.29`; return to C.34 only after preserved structure, lost structure, mapping mode, and architecture use are stated. |
| Bridge owner bypass | A cross-context or cross-tradition mapping can preserve local structure while losing local sense. | Use `F.9` for the bridge and `F.15` for later regression or conformance strengthening before substitution is relied on. |

### C.34:9 - Consequences

Positive consequences:

- Architects can use partial sameness without pretending to have identity. This keeps comparison, projection, generated-output admission, realization checks, and decision repair usable.
- Formal methods become useful at the right locus: graph matching, category-theoretic morphisms, entropy, and simulation relations can support the mapping without becoming architecture ontology.
- Cross-context and source-tradition risks are visible early because directionality, scope, bridge loss, and conformance owners are named.
- Later decisions can be repaired locally: the preservation note says which relation failed, which structure was lost, and which owner must receive the return.

Costs and trade-offs:

- C.34 adds friction before easy claims such as "same diagram," "same graph," or "same module." That cost prevents stronger authority from entering through weak similarity.
- The pattern does not prove formal equivalence by itself. When proof, measurement, evidence, assurance, gate, release, or work authorization is current, the corresponding owner must still act.
- Some comparisons will lower from equivalence to correspondence or near-sameness. That lowering is a success when it prevents a false downstream claim.

### C.34:10 - Rationale

Architecture preservation is use-relative. The same two structures can be equivalent for one use, merely corresponding for another, and unusable for a third. A mature C.34 therefore cannot be a generic formalism pattern. It must start from source and target selected structures, then choose the weakest mapping mode that licenses the next architecture use.

This keeps C.34 separate from its neighbors. `C.29` owns mathematical-lens use. `C.30.AD` and `C.30.ASV` own description and view records. `F.9` owns cross-context bridges. `F.15` owns regression and conformance harnesses. `C.32` owns candidate synthesis. C.34 contributes the preservation claim that those owners may need, but it does not replace them.

The source families explain the safeguards. Structural-equivalence research shows that symmetry can compact search only under explicit conditions. Applied category theory shows why preservation maps are powerful but still formal lenses until tied to the architecture use. MBSE view practice makes projection and omitted structure ordinary. Sapunov and ToCS, plus GonzoML, show why observed relation maps and neural substitution labels need typed relation, confidence, and source-label recovery before architecture use.

### C.34:11 - SoTA-Echoing

| Source or practice line | Adopt, adapt, or reject | Concrete C.34 locus changed | Boundary and currentness |
| --- | --- | --- | --- |
| Yang et al., `Structural Equivalence in Subgraph Matching`, arXiv:2301.03161 | Adapt structural-equivalence and symmetry discipline. | Strengthens `mappingMode`, the weakest adequate mapping rule, and the warning against label or shape overread. | Subgraph structural equivalence does not define holon architecture equivalence outside declared structures and use. Reopen when the source graph, target graph, or use changes. |
| Fong and Spivak, `Seven Sketches in Compositionality`, arXiv:1803.05316 | Adapt applied category-theory preservation language through `C.29`. | Keeps morphism, functor, sketch, and composition vocabulary tied to preserved structure, lost structure, mapping mode, and architecture use. | Older source is lineage and still useful as applied compositional practice, but it does not become the default FPF architecture ontology. |
| Multi-view architecture and MBSE query and view practice | Adopt the ordinary need for view correspondence, projection, query, and coarsening. | Adds view and description cases plus owner exits to `C.30.AD` and `C.30.ASV`. | View output or query output is not architecture and not realized structure. Reopen when viewpoint, query rule, model edition, or described structure changes. |
| Sapunov, ToCS, and code-agent architecture-map practice | Adapt partial-observation preservation discipline. | Adds source observation class, inferred edges, unexplored regions, confidence, and active-passive gap as preservation-lowering conditions. | A code-agent map, JSON probe, dependency F1, invariant F1, or active-passive gap does not prove architecture equivalence, safe change, assurance, gate passage, or release readiness. |
| GonzoML neural-network architecture intake | Adapt neural architecture operation language. | Adds dataflow, routing, memory placement, cache placement, resource boundary, block substitution, and affected-characteristic checks for neural structure substitution. | Neural labels, ablations, pruning masks, distillation success, or benchmark gains remain source material until selected structures, preserved relations, lost relations, and receiving owners are recovered. |

C.34 rejects one common but weak practice: treating any formal-looking mapping as architecture equivalence. The stronger practice is to say exactly what survives, what is lost, and what downstream use is licensed.

### C.34:12 - Relations

- **Builds on:** `A.22`, `C.30`, `C.30.ASV`, `C.30.AD`, `C.29`, and `F.9`.
- **Uses:** `C.16`, `C.25`, and `C.32.ACE` when a preservation, similarity, distance, entropy, loss, or compression claim is recorded as a reading or eval result.
- **Coordinates with:** `C.32`, `C.32.PAD`, `C.32.ADR`, `C.30.TFS-REL`, `C.30.STRAT`, `A.6.M`, `C.31`, `C.31.ASAP`, `E.18`, and `F.15`.
- **Boundary:** C.34 governs declared preservation adequacy for an architecture use. It does not make a formalism ontology, select a candidate, decide a project, establish evidence or assurance, or authorize substitution across contexts without bridge and conformance owners.

### C.34:End

