## E.18.2 - Transformation Flow Mathematical Description

> **Tech-name:** `TransformationFlowMathematicalDescription`
> **Plain-name:** mathematical description of a transformation-flow structure
> **Type:** Architectural pattern (E)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part E -> E.18 child pattern
> **Builds on:** `E.18` Transformation Flow Structure, `E.18.NET` Network of Transformation-Flow Structures, `C.29` Mathematical Lens Use, `C.2.1` `U.Episteme`, `E.17` publication machinery, `A.3.4` `U.Transformation`, `A.6.0` `U.Signature`, `A.6.5` slot discipline, `A.15` work family, `A.20`, `A.21`, and `C.30` architecture family.
> **Purpose:** record how a graph, algebraic, categorical, tuple, path, slice, morphism, quotient, fold, refinement, factorization, wiring, or related mathematical expression describes exactly one selected `TransformationFlowStructure` or `TransformationFlowStructureNetwork@Context`: what it represents, what it preserves, what it loses, which declared use it serves, and which exact relation and test carry any stronger project claim.

### E.18.2:1 - Problem frame

Use this pattern when the current EntityOfConcern is a mathematical description of exactly one selected transformation-flow structure, one selected network of such structures, or one independently identified part of that subject. The description may be a graph, hypergraph, category-theory object, algebra, tuple, matrix, network expression, wiring diagram, morphism family, quotient, fold, refinement, factorization, path relation, slice relation, or another formal expression.

The primary EntityOfConcern is `TransformationFlowMathematicalDescription@Context`: a `C.2.1 U.Episteme` specialization whose described ontic subject is exactly one selected `TransformationFlowStructure` under E.18 or one selected `TransformationFlowStructureNetwork@Context` under E.18.NET. E.18.2 does not invent a second local description format. The one-TFS and network reference branches are mutually exclusive; `CandidateMathObject`, `ExpressionKind`, `MappingMode`, `PreservedStructure`, `LostStructure`, and `DeclaredUse` fill claim or description-content slots, while `PublicationFaceRef?` remains a separate publication relation through E.17. E.18.2 keeps five values distinct:

| Value under concern | Pattern contribution used | Boundary |
|---|---|---|
| one selected compound structure of transformations and adjacent loci | E.18 defines one-TFS identity, allowed loci and relations, selection constraints, and local-value rules; apply those rules to select the exact structure | not a mathematical expression merely because a graph or algebra describes it |
| one selected network of independently identified TFS or nested-network members and exact cross-member relations | E.18.NET defines membership, boundary, and cross-member relation requirements; apply those rules to select the exact network and identify its obtaining cross-member relation occurrences | not a graph, record, view, or publication, and not several valuations or one internal subflow |
| mathematical description of exactly one selected TFS or network | `E.18.2` | records represented subject, expression kind, mapping mode, preserved/lost structure, declared use, and the boundary to stronger project claims |
| declared mathematical-lens use and its adequacy | C.29 defines the bounded adequacy test and returned lens-use result; apply it when adequacy, payoff, preserved/lost structure, or a stop condition is claim-bearing | not a local E.18.2 invention |
| rendered graph, table, equation, diagram, or other publication face | `E.17` publishes the face; the applicable view or architecture-description pattern supplies its membership or adequacy result when that claim is current | may publish the mathematical description but neither becomes it nor reidentifies the selected TFS or network |

When the described selected structure is one A.22-selected CGUS qualified under `E.18.3` through an independently identified E.18 substrate, E.18.2 still defines only the mathematical description. A graph, path expression, category object, algebra, tuple, or matrix may describe substrate positions, crossings, and condition labels, but the expression does not decide whether a condition is an applied claim, an E.18 `GuardFail` event, or an independently defined relation occurrence. It may also describe preserved or lost structure, exact supporting relations to independently identified neighboring values, and stop or reconsideration questions, but it remains `TransformationFlowMathematicalDescription@Context` or a C.29 lens-use claim. It does not become the selected CGUS or its substrate and does not carry method, work, evidence, architecture, publication, or refresh authority.

#### E.18.2:1.1 - Use this when

- one selected `TransformationFlowStructure`, one selected `TransformationFlowStructureNetwork@Context`, or an independently identified part of that subject needs a graph, algebra, category, tuple, morphism, quotient, fold, refinement, factorization, wiring, matrix, or network expression;
- a diagram or equation set helps compare composition, decomposition, coarser/finer partitioning, internal transfer, crossing, or refresh inside one TFS, or exact cross-member relations in one selected network, but the mathematical expression itself must not authorize work;
- a source says "graph", "network", "path", "morphism", "algebra", "category", "workflow", "pipeline", "dataflow", or "functional diagram" and the claim being made is the mathematical description of one already selected TFS or TFS network;
- a reader needs to decide whether the visible object is one E.18 TFS, one E.18.NET network, an E.18.2 mathematical description, a C.29 lens-use claim, or only an E.17 publication face.

#### E.18.2:1.2 - What goes wrong if missed

A project source expression, source publication, or diagram can make a graph-shaped expression look like the flow structure itself. Then mathematical neatness silently becomes evidence, work completion, gate readiness, architecture adequacy, or permission to act. The opposite error is also common: every graph-shaped structure is demoted to "just a diagram", so the selected structure, its slices, and its refresh boundaries disappear.

#### E.18.2:1.3 - What this buys

The practitioner can use mathematical structure without overclaiming it. The record names exactly one represented E.18 TFS or E.18.NET network, the expression used, what the expression preserves, what it loses, the declared use, and the result returned after applying the pattern whose Solution answers any stronger claim.

#### E.18.2:1.4 - Not this pattern when

- one selected transformation-flow structure itself is the EntityOfConcern; use `E.18`;
- one selected network of independently identified TFS or nested-network members is the EntityOfConcern; use `E.18.NET`;
- one A.22-selected CGUS whose E.18.3 qualification uses an independently identified E.18 substrate is the EntityOfConcern; use `E.18.3`;
- one bounded transformation is the EntityOfConcern; use `A.3.4`;
- the claim is general mathematical-lens adequacy outside transformation-flow structures; use `C.29`;
- the claim is a publication face or view publication; use `E.17` and the relevant view or architecture-description pattern;
- the claim is work planning, performed work, evidence, assurance, gate fit, gate decision, release, decision, or architecture adequacy; use the applicable row in §4.4 and keep the exact plan, Work, evidence relation, assurance result, gate result, release claim, choice, or architecture result returned there.

### E.18.2:2 - Problem

Transformation-flow structures are often easiest to inspect through mathematics. A graph can expose dependency and reachability, a category can expose composition, a quotient can expose coarser structure, a fold can expose aggregation, a refinement can expose lost detail, a wiring expression can expose interface placement, and a tuple can make slot positions explicit.

Those expressions are useful because they preserve selected structure while ignoring other structure. That same usefulness creates risk. If the expression is treated as the structure itself, the project may believe that a path in a graph proves a possible performed-work order, that a commutative square proves a real bridge, that a fold proves safe aggregation, or that a wiring diagram proves integration readiness.

E.18.2 solves the description problem: it records a mathematical expression over one already selected E.18 TFS or E.18.NET network and says what that expression may be used for. It does not select or reidentify that world-side subject, decide an atomic transformation, establish a work occurrence, pass a gate, settle an evidence case, or establish an architecture claim.

### E.18.2:3 - Forces

| Force | What must be preserved | Pressure to manage |
|---|---|---|
| Mathematical usefulness | Graphs, categories, tuples, algebra, morphisms, paths, slices, quotients, folds, refinements, factorizations, and wiring can expose structure that prose misses. | Mathematical form can look stronger than the claim it can carry. |
| EoC separation | The selected E.18 TFS or E.18.NET network, its E.18.2 mathematical description, its E.17 publication, and its C.29 lens-use adequacy are different values. | One visible source or publication face may present all of them at once. |
| Composition and decomposition | One TFS and recursive TFS networks need reviewable composition, factorization, slice, fold, and refinement claims. | The expression can hide which exact E.18 TFS, E.18.NET network, or independently identified part is being described. |
| Publication usability | Readers need diagrams, tables, equations, and views. | A publication face can be mistaken for evidence, gate passage, or performed work. |
| Related-claim economy | Apply E.18 to select one exact flow structure, A.3.4 to identify one actual bounded change, E.17 to publish a face, A.20 or A.21 to obtain validity or gate results, A.15 to identify plans or Work, and C.30 to state an architecture claim. | Repeating those patterns' boundary doctrine inside E.18.2 creates fanout. |

### E.18.2:4 - Solution

Write a `TransformationFlowMathematicalDescription@Context` only when the mathematical expression changes the current transformation-flow description move. Name exactly one described ontic subject: one E.18 TFS or one E.18.NET network. Keep that subject reference, the mathematical description, any C.29 lens-use judgment, and any E.17 publication face separate. Then decide whether the C.29 lens-use card is needed for adequacy, payoff, preserved/lost structure, or boundary.

#### E.18.2:4.1 - First-use record

Use this compact record for ordinary cases:

```text
TransformationFlowMathematicalDescription@Context:
  # exactly one described ontic subject branch is present:
  DescribedTransformationFlowStructureRef?:
  DescribedTransformationFlowStructureNetworkRef?:
  DescribedSliceOrLocusRef?:
  CandidateMathObject:
  ExpressionKind:
  MappingMode:
  PreservedStructure:
  LostStructure:
  DeclaredUse:
  BoundaryStop:
  C29LensUseRef?:
  PublicationFaceRef?:
```

Exactly one of `DescribedTransformationFlowStructureRef?` and `DescribedTransformationFlowStructureNetworkRef?` is present. The first points to one E.18 TFS; the second points to one already selected E.18.NET network. `DescribedSliceOrLocusRef?` may cite an existing path, slice, `FlowPositionRef`, `ExposedFlowPositionRef`, member path, E.18.NET `NetworkCrossFlowRelationRowRef`, or other independently identified part without copying the fields that define that object. `CandidateMathObject` and `ExpressionKind` name the graph, algebra, category, tuple, morphism, quotient, fold, refinement, factorization, wiring, matrix, network expression, or related mathematical object. `PreservedStructure`, `LostStructure`, `DeclaredUse`, and `BoundaryStop` follow the C.29 discipline when the expression is claim-bearing. `PublicationFaceRef?` points to a separate E.17 publication. The compact record has no generic neighboring-object reference. When a neighboring claim is materially needed, cite its exact C.2.1 claim-bearing episteme in the subject-specific account; identify an ontic subject or relation occurrence only through a separately named, correctly typed reference supplied by the pattern for that claim.

#### E.18.2:4.2 - Expression families

| Expression family | Use when it describes | Required boundary |
|---|---|---|
| graph, hypergraph, network expression, DSM, DMM, MDM, or matrix | dependency, internal transfer, exact cross-member relation, adjacency, interface placement, clustering, or change propagation inside one selected TFS or across one selected TFS network | not the selected TFS or network: apply E.18's one-TFS identity and selection constraints or E.18.NET's membership, boundary, and cross-member relation rules to select that ontic subject; E.18.2 defines only this description; not work occurrence, gate passage, or evidence |
| mathematical path or path slice | reachability, carried relation, currentness slice, refresh locality, or crossing-local replay | not a project procedure or performed sequence |
| tuple, record, slot relation, or typed relation expression | slot positions, relation arity, locus typing, and value placement | not a new U-kind and not a replacement for A.6.5 slot discipline |
| morphism, composition, category, operad, optic, or wiring expression | composition, interface, substitution, transfer law, or decomposition of selected transformations | not proof that the represented work can be performed or that interfaces are semantically compatible |
| quotient, fold, coarsening, refinement, or factorization | coarser/finer partitioning, aggregation, retained/lost structure, and alternative decomposition | not an identity claim without preserved/lost structure and return condition |
| algebra, semiring, equation system, or constraint system | operation law, conservation, admissible composition, or constraint propagation over the selected structure | not a mechanism, formal substrate, or empirical law unless the formal substrate satisfies the A.6.0 declaration test, the postulate or principle frame satisfies the A.6.1 definition and application test, and the relevant evidence test is current |
| learned representation, embedding, simulation object, or differentiable surrogate | approximate structure, optimization, similarity, or predictive proxy over transformation-flow structure | not architecture adequacy, OOD guarantee, causal proof, or release readiness by itself |

These families are prompts for recovery, not a taxonomy of new FPF kinds. A local expression may combine several families; the record still names exactly one selected TFS or network subject, one current described part when relevant, and the declared use.

#### E.18.2:4.3 - Five-way subject, description, lens, and publication discriminator

Use this discriminator before writing or accepting a mathematical description:

```text
If the claim selects one TFS or its internal flow structure, use E.18.
If the claim selects independently identified TFS or nested-network members plus exact cross-member relations, use E.18.NET.
If the claim describes exactly one selected TFS or network with mathematics, use E.18.2.
If the claim evaluates that mathematical lens use, use C.29 with the E.18.2 description reference.
If the claim publishes a graph, table, equation, diagram, card, or other face, use E.17 and the relevant view or architecture-description pattern.
```

The same visible source may require several records, but each E.18.2 description chooses one described ontic subject branch. A refrigerator principle scheme may include an E.17 publication face, a functional-architecture view, one selected E.18 TFS, a thermodynamic mechanism claim, and an E.18.2 graph or equation description. A network diagram may similarly publish an E.18.2 description of one already selected E.18.NET network. If the expression is evaluated as a lens, apply the C.29 adequacy test; if it is rendered or published, identify the E.17 publication face and any current view or architecture-description membership. Neither record reidentifies the TFS or network.


#### E.18.2:4.4 - Related claims

E.18.2 defines only the mathematical-description relation. For any neighboring claim, use the row below that names the exact contribution needed now:

| Current claim | Use |
|---|---|
| one bounded change under conditions | Apply A.3.4's occurrence test and identity rule to identify the changed referent, boundary, actual change facts, and continuity or reidentification basis. |
| one selected transformation-flow structure, flow valuation, path, slice, crossing, or refresh locus | Apply E.18's identity, selection-constraint, and local-value rules to select that exact one-TFS structure and identify the local values used by the claim. |
| one selected network of independently identified TFS or nested-network members and exact cross-member relations | Apply E.18.NET's membership, boundary, and cross-member relation requirements to select the exact members and identify the obtaining cross-member relation occurrences. |
| one A.22-selected CGUS qualified through an independently identified E.18 substrate, with constraints and guarded alternatives whose applied-claim, E.18-event, or independently defined relation basis remains separate, plus preserved/lost structure, neighboring values connected by exact supporting relations, and stop or reconsideration questions | `E.18.3` qualifies that selected CGUS for this substrate use without identifying the substrate or neighboring values |
| mathematical-lens adequacy, preserved/lost structure, payoff, or stop condition | `C.29` returns the bounded lens-use result |
| method | Apply A.3.1's method criteria to identify the exact `U.Method`. |
| method-description membership | `A.3.2` tests one C.2.1 episteme against one admitted `U.Method` |
| mechanism or mechanism application | `A.6.1` supplies the mechanism declaration and exact application binding |
| formal-substrate signature | `A.6.0` supplies the profile-specific signature declaration |
| work plan | Apply A.15.2's plan-identity and intended-work rules to identify the plan and intended-work relations. |
| performed work | Apply A.15.1's occurrence and identity rules to identify the dated `U.Work` occurrence. |
| evidence use | `A.10` supplies the evidence relation for the named reliance |
| assurance use | `B.3` returns the bounded assurance result for that reliance |
| internal step validity | `A.20` returns the constraint-validity result |
| gate profile or decision | `A.21` supplies the gate profile, aggregation, decision, and publication minima |
| release | Apply A.15.1 to test and identify an actual release action as Work; test a separate subject-release claim with its named predicate or return the exact A.6.RCD result. |
| local choice | `C.11` returns the `ChoiceResult` |
| architecture | `C.30` carries the architecture claim |
| architecture structural view | `C.30.ASV` returns the structural-view adequacy result |
| functional structure | `A.6.F` supplies the exact function/bearer claim |
| module interface | `A.6.M` supplies the module-interface relation |
| reusable-structure characteristics | `C.31` carries the reusable-structure claim |
| publication face or explanation-faithfulness use | `E.17` supplies the publication face; `E.17.EFP` returns the explanation-faithfulness result |

### E.18.2:4.5 - Archetypal Grounding (Worked Slices)

**Refrigerator principle scheme.** A vapor-compression diagram can be a publication face. The cooling cycle can be a selected `TransformationFlowStructure`. The thermodynamic laws are mechanism or formal-substrate claims. The graph or equation set that describes the cycle is an E.18.2 mathematical description. It may preserve transformation order, heat-transfer constraints, and cycle closure while losing maintenance work, sensor uncertainty, and installation context. It does not prove the refrigerator works or authorize a repair.

**Two descriptions of one build-the-builder network.** A nested wiring description can preserve finite member paths and exposed positions while hiding an n-ary relation's qualification. A hypergraph description of the same exact E.18.NET value can preserve relation arity and endpoints while flattening recursive member boundaries. Both E.18.2 records cite the same network ref and state different preserved and lost structure; neither graph creates or reidentifies the network. A rendered diagram is a further E.17 publication value.

**P2W carry-through.** A P2W source expression or publication may draw a graph-shaped path from formal substrate to principle frame, mechanism position, method selection, work planning, work, and evaluation. The graph-shaped expression can be an E.18.2 description of the selected carry-through structure. The P2W move itself remains `E.18.1`; work planning remains A.15; dated work remains `U.Work`.

**Neural-network dataflow.** A transformer architecture diagram may describe layers, attention blocks, residual connections, and graph-like connection structure. If the current claim selects one TFS, use E.18; if it selects independently identified TFS or nested-network members plus exact cross-member relation occurrences, use E.18.NET; if it is an architecture claim, use C.30. If the current claim is the mathematical graph, tensor-shape relation, or wiring expression that describes one such already selected subject, use E.18.2. For benchmark superiority, apply the relevant comparison test. For training Work, apply A.15.1's occurrence and identity rules; for an evidence claim, state the A.10 evidence-use relation; for release, test the release action as Work and any separate subject-release predicate; for causality, apply the exact causal predicate and test. The diagram supplies none of those project results.

**Circuit and algorithm.** A logic-circuit schematic can describe a transformation-flow structure realizing a Boolean relation. The netlist, wiring graph, algebraic normal form, and truth table are different mathematical or formal descriptions. They do not by themselves decide whether the selected method exists, whether the CMOS mechanism is valid under voltage and timing conditions, or whether a dated powered run occurred.

### E.18.2:4.6 - Bias-Annotation

| Bias | How E.18.2 prevents it |
| --- | --- |
| Graph-as-world bias | One selected TFS stays with `E.18`, one selected network stays with `E.18.NET`, and a graph or algebraic object remains the E.18.2 mathematical description unless applying the pattern whose Solution answers a stronger question returns a different current result. |
| Path-as-procedure bias | A mathematical path or path slice can express reachability or locality; method and work-plan claims stay with method and work-plan patterns. |
| Diagram-as-architecture bias | Architecture adequacy stays with `C.30`, `C.30.ASV`, and related architecture patterns; E.18.2 records only the mathematical-description relation. |
| Math-as-authority bias | No mathematical expression authorizes work, passes a gate, settles evidence, grants release, or proves assurance by itself. |
| Publication-as-description bias | Publication faces and rendered diagrams stay with `E.17` unless the current EntityOfConcern is the mathematical description itself. |

### E.18.2:5 - Conformance checklist

- `CC-E18.2-1` The current EntityOfConcern is `TransformationFlowMathematicalDescription@Context`, not the selected E.18 TFS or E.18.NET network itself.
- `CC-E18.2-2` Exactly one described ontic subject branch is present: `DescribedTransformationFlowStructureRef?` or `DescribedTransformationFlowStructureNetworkRef?`. The optional `DescribedSliceOrLocusRef?` resolves through the selected E.18 or E.18.NET subject and does not duplicate its fields.
- `CC-E18.2-3` The mathematical expression family is named without minting a new U-kind.
- `CC-E18.2-4` Preserved structure, lost structure, declared use, and boundary stop are named when the expression is claim-bearing.
- `CC-E18.2-5` C.29 is used when mathematical-lens adequacy, payoff, obstruction, preserved/lost structure, or stop condition is being evaluated beyond the local description relation.
- `CC-E18.2-6` Graph, path, slice, morphism, algebra, category, tuple, quotient, fold, refinement, factorization, wiring, and network-expression language stays mathematical-description language unless the practitioner has independently selected the ontic subject by applying E.18 or E.18.NET.
- `CC-E18.2-7` No mathematical expression proves work occurrence, authorizes action, passes a gate, settles evidence, or establishes architecture adequacy by itself.
- `CC-E18.2-8` A rendered graph, table, equation, diagram, or other publication face remains separate from the mathematical description and is handled through `E.17`; changing it alone reidentifies neither the description nor its selected TFS or network subject.
- `CC-E18.2-9` When selected TFS, selected network, work, method, mechanism, signature, evidence, gate, decision, architecture, function, module-interface, or reusable-structure claims are current, apply the exact contribution named for that claim in §4.4 and keep the result it returns. E.18.2 records only the mathematical-description relation for one already selected ontic subject.
- `CC-E18.2-10` A source expression or publication face that carries several claims is split into records by current EntityOfConcern and relation position, not by the expression's or publication's name.

### E.18.2:6 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| **Graph-as-world.** A graph-shaped expression is treated as the project-world structure because it is visually convincing. | Name whether the current EoC is one E.18 TFS, one E.18.NET network, an E.18.2 mathematical description, a C.29 lens-use judgment, or an E.17 publication face. |
| **Path-as-procedure.** A mathematical path or path slice is read as a required project procedure. | Keep it as a mathematical relation over a selected structure; use method or work-plan patterns for procedures. |
| **Algebra-as-mechanism.** An operation law or equation system is treated as a realized mechanism. | Use A.6.0 for formal substrate and A.6.1 for mechanism claims; keep E.18.2 to the expression relation. |
| **Fold-as-identity.** A quotient, fold, or coarsening erases detail and is then used as if nothing was lost. | State preserved structure, lost structure, and lost-structure return condition; use C.29 when the adequacy of the fold matters. |
| **Diagram-as-architecture adequacy.** A clean diagram is treated as proof that the architecture is good. | Use `C.30` for the architecture claim, `C.30.ASV` for architecture structural-view adequacy, and `C.31` for reusable-structure characteristics; `E.18.2` only describes one already selected TFS or network mathematically. |

### E.18.2:7 - Consequences

| Consequence | Benefit | Cost or mitigation |
|---|---|---|
| Mathematical descriptions get their own local record. | Graphs, paths, slices, quotients, and wiring can be used without becoming hidden ontology. | One source expression or publication face may need several records. |
| E.18 and E.18.NET stay about selected ontic structures. | One TFS and one network of independently identified TFS members remain inspectable without becoming their mathematical descriptions. | Readers must choose E.18, E.18.NET, or E.18.2 by the current EntityOfConcern. |
| C.29 remains general. | E.18.2 does not duplicate the whole mathematical-lens pattern. | Claim-bearing adequacy needs a C.29 reference. |
| Boundary to work, gates, evidence, and architecture is explicit. | Mathematical prestige does not replace project checks. | Stronger claims require the exact contribution and returned result named for that claim in §4.4. |

### E.18.2:8 - Rationale

Graph-shaped or morphism-shaped source labels do not carry current ontology by themselves here. They remain useful only when the current EntityOfConcern is named: E.18 keeps one selected TFS, E.18.NET keeps one selected network, A.3.4 keeps bounded transformation, E.18.1 keeps P2W carry-through, and E.18.2 keeps one mathematical description of exactly one selected TFS or network.

The pattern is intentionally narrower than C.29. C.29 answers the general question "is this mathematical lens use adequate for this declared purpose?" E.18.2 answers the local question "what mathematical expression describes this one selected TFS or network, and which declared use does that expression serve here?" This prevents shadow math-lens doctrine while preserving the practical value of graph, path, category, tuple, and algebraic expression in transformation-flow work.

### E.18.2:9 - SoTA-Echoing

| Practice tradition | Distinction kept for E.18.2 | E.18.2 invariant | Practitioner implication | Return if |
|---|---|---|---|---|
| FPF strict-distinction, selected-structure, architecture-description, and view apparatus (`A.7`, `A.22`, `C.30.AD`, `E.17`) | A description or view can expose one selected TFS or network without becoming that structure or evidence. | The mathematical description names exactly one subject branch, expression, preserved/lost structure, declared use, and boundary stop. | A readable model can guide inspection without authorizing action. | The selected E.18 TFS or E.18.NET network, publication face, evidence relation, or architecture claim changes. |
| SysML v2 — deliberately excluded | No move or lineage is adopted for E.18.2: this campaign does not treat SysML v2's long-promoted model-and-diagram program as current working SoTA for the problem. | Search prominence, diagram familiarity, and the word *system* do not establish a useful structure/description boundary. | Use practices that solve the current modeling problem in operating tools and projects; do not import a SysML v2 basis by default. | Reconsider only on concrete project evidence that changes the current problem and outperforms the adopted working line. |
| Applied category theory, wiring diagrams, and graph rewriting (Fong & Spivak, arXiv [`1803.05316`](https://arxiv.org/abs/1803.05316); Spivak, arXiv [`1305.0297`](https://arxiv.org/abs/1305.0297); Baez & Fong, arXiv [`1504.05625`](https://arxiv.org/abs/1504.05625); Bonchi et al., arXiv [`1602.06771`](https://arxiv.org/abs/1602.06771); Patterson/Spivak/Vagner, arXiv [`2101.12046`](https://arxiv.org/abs/2101.12046)). | Formal expression is useful because it preserves some structure and drops other structure. | Quotient, fold, refinement, factorization, and wiring claims name what survives and what is lost. | Coarser and finer descriptions can be compared without pretending they are identical. | The preserved/lost structure, mapping mode, or C.29 lens-use adequacy changes. |
| Digital-thread, research-object, and source-reference practice (RO-Crate paper, arXiv [`2108.06503`](https://arxiv.org/abs/2108.06503); Di Cosmo/Gruenpeter/Zacchiroli, arXiv [`2001.08647`](https://arxiv.org/abs/2001.08647); ISO 23247 digital-twin lineage). | Replay works only when record kinds remain distinct. | E.18.2 descriptions cite one E.18 TFS or E.18.NET network and exact related records rather than absorbing work, evidence, gate, and publication claims. | A trace graph can remain useful without becoming proof, plan, or performed work. | Source-currentness relation, work-family law, evidence, gate, or publication-use relation changes. |
| Engineering architecture practice uses functional, dataflow, and interface diagrams under explicit view, viewpoint, and correspondence discipline. | A diagram may describe architecture, transformation-flow structure, method, mechanism, or publication face according to the current EoC. | E.18.2 keeps only the mathematical-description relation; architecture adequacy remains under `C.30`, architecture structural-view adequacy remains under `C.30.ASV`, and reusable-structure characteristics remain under `C.31`. | Functional and dataflow diagrams can be used without semio-bias or architecture overclaim. | The architecture selected structure, viewpoint, or correspondence relation changes. |

### E.18.2:10 - Relations

- Apply E.18's one-TFS identity, allowed-locus, selection-constraint, and local-value rules to select one `TransformationFlowStructure` and identify the flow valuation, path, slice, crossing, transfer annotations, and refresh locality used by the claim.
- Apply E.18.NET's membership, boundary, and cross-member relation requirements to select one network of independently identified TFS or nested-network members and identify its obtaining cross-member relation occurrences.
- Apply A.3.4 to identify an actual bounded `U.Transformation`, its changed referent, boundary, facts, and continuity or reidentification rule.
- Apply C.29 to evaluate mathematical-lens use and retain its returned adequacy, preserved/lost structure, payoff, obstruction, or stop result when that claim is current.
- Use C.2.1 for description-episteme identity and E.17 for publication faces and their publication boundary.
- Use A.6.0 for formal-substrate signatures, A.6.1 for mechanisms and applications, A.6.5 for slot discipline, and E.20 for mechanism-method placement.
- Apply A.15.1 to identify performed Work, A.15.2 to identify work plans, A.20 to obtain internal-step validity, A.21 to obtain gate results, A.10 to state evidence relations, B.3 to obtain assurance, and C.11 to obtain local choices.
- Apply C.30 to state architecture claims, C.30.AD to identify architecture descriptions, C.30.ASV to evaluate structural views, A.6.F to state function/bearer claims, A.6.M to state module-interface relations, and C.31 to state reusable-structure characteristics.

### E.18.2:End

