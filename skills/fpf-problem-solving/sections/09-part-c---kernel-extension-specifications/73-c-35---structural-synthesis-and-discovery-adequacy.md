## C.35 - Structural Synthesis and Discovery Adequacy

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.35:1 - Problem frame

Use this pattern when a generated, searched, clustered, queried, learned, transformed, simulated, or discovered output that carries or describes selected structure may seed or inform architecturing, and the practitioner must decide whether it can enter architecture work before or around `C.32` candidate admission.

Primary working reader: an architect, architecture researcher, AI-assisted architecture worker, model-based engineer, or reviewer receiving an output that carries or describes selected structure from DSM and MDM modularization, MBSE query and view generation, graph grammar, model transformation, NAS, DSE, QD, OEE, and NQD search, LLM-assisted architecture design, code-agent mapping, simulation, benchmark trace, or source discovery.

Typical entry phrases:

```text
"The LLM generated an architecture diagram; can it seed synthesis?"
"The DSM clustering suggests modules; is this a candidate architecture yet?"
"The MBSE query produced a view; what selected structure does it describe?"
"NAS found a Pareto point; what architecture claim can use it?"
"A graph grammar transformed the model; what preservation and bearer boundary must be checked?"
```

The first useful output is `StructuralSynthesisDiscoveryAdequacyNote@Project`:

```text
StructuralSynthesisDiscoveryAdequacyNote@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  structuralSynthesisAdequacyNoteProjectUseRelationRef?: U.RelationRef under a named architecture-use or work-use predicate when that relation identity is material
  groundedArchitectureQuestionRef:
  selectedSourceStructureRefs:
  generationOrDiscoveryMethodRef:
  generationOrDiscoveryWorkRef?: U.EntityRef constrained to U.Work
  searchOrQuerySpaceRef?:
  constraintRefs:
  producedCarrierOrDescriptionRefs:
  describedStructureRefs?:
  synthesisStructureMapOrTransformationTrace?:
  actualTransformationRefs?:
  workToTransformationOrProductionClaimRefs?:
  preservedStructure:
  lostStructure:
  constraintGovernedUnfoldingStructureRef?:
  sourceLabelRecoveryRef?:
  observationAndUncertaintyRefs?:
  validationOrComparisonRefs?:
  selectedCandidateStructureRefs?:
  candidateAdmissionCondition:
  bearerOrRealizationBoundary:
  realizedHolonStructureRefs?:
  measurementOrEvalReturnRefs?:
  bearerFeasibilityQuestionRef?:
  nextClaimOrRuleRef?:
  receivingClaimKind:
  admissibleUse:
  nonAdmissibleUse:
  carrierAdmissionReturnCondition:
```

Here `@Project` is a compatibility and retrieval cue only. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. When the note is genuinely used in one actual project, `projectWorkOccurrenceRef` identifies the exact composite `U.Work` and `structuralSynthesisAdequacyNoteProjectUseRelationRef` identifies the direct relation by which that exact project Work uses the note. The suffix or either reference alone establishes no project locality. The note and the composite project Work remain distinct.

When generation or discovery is claimed as performed Work, `generationOrDiscoveryWorkRef` is mandatory and names the independently identified `U.Work` occurrence. All facts required by A.15.1, A.2.1, and F.6 remain recoverable. A short projection may omit only an unused assignment identifier. The Method, Work, note, and produced carrier or description are different objects.

`actualTransformationRefs` may cite only independently identified A.3.4 bounded changes; a Method label, transformation trace, graph edge, or before-and-after picture does not make a transformation actual. Any positive link from the Work to an actual transformation or produced entity must cite its declared predicate, an admitted A.6.RCD local claim, or the selected A.15.PROD branch in `workToTransformationOrProductionClaimRefs`; otherwise keep the objects separate and return `missing-governor`. Every structure reference likewise resolves to an independently selected A.22 `U.Structure`; a carrier, graph, cluster, or description does not supply its four identity discriminators.

Adoption test: after using C.35, another practitioner can tell what was produced, which structure it describes, what it preserves and loses, what must happen before C.32 admission or realization claims, and which practical claim, question, rule, or test comes next. Record exact assertion identity only when that next use must travel independently.

What C.35 buys in practice: the practitioner can accept useful generated or discovered output without handing it authority. The pattern lets a search output, cluster, query result, model transformation, or LLM proposal become candidate input for architecturing only after carrier, described structure, admission condition, and the next claim or test are named.

Ordinary working move: name the produced carrier first, then the described structure, then the admission condition. If those three cannot be separated, do not let the output enter C.32 or a decision.

Not this pattern when the current question is how to search, choose, measure, decide, authorize, publish, govern a reusable generator, govern a cultural-evolution case, or run the work itself. Use the pattern that defines or decides that question first, including `C.36` for the cultural-evolution relation bundle. Use C.35 only when a produced carrier must be admitted or rejected before another architecture claim relies on it.

### C.35:2 - Problem

Modern architecture work receives outputs that carry or describe selected structure from many production and discovery practices: DSM clusters, MDM slices, MBSE queries, generated views, graph grammars, model transformations, LLM architecture proposals, AI-assisted ADD, code-agent relation graphs, NAS graphs, DSE traces, Pareto fronts, QD archives, benchmark traces, simulations, and source-corpus mining.

These outputs can be extremely useful. They can expose candidate decompositions, relation gaps, hidden invariants, feasible search regions, trade-off points, source labels, or overlooked structure. But they are not automatically architecture, selected candidate structures, realized holon structures, eval results, evidence sufficiency, or decision authority.

C.35 handles the gap between produced carrier and architecture use. It asks which exact generation or discovery Method was used; whether one independently admitted Work occurrence actually enacted it; which exact production, discovery-use, or work-to-change claim connects that Work to the carrier or change, if any; which independently selected source and described structures are recoverable; what is preserved and lost; what validation or comparison is available; what bearer or realization boundary is open; and what condition and rule must be met before the output can feed C.32 or another architecture claim.

### C.35:3 - Forces

| Force | Tension |
| --- | --- |
| Discovery value vs authority overread | Generated and discovered outputs widen the candidate space, but cannot select, decide, prove, or realize architecture by themselves. |
| Carrier vs described structure | A diagram, query result, graph, cluster, model, or proposal is a produced carrier or description; the selected structure it describes must be recovered. |
| Search quality vs architecture adequacy | A Pareto point, benchmark score, archive member, or cluster objective can guide synthesis only through declared structures, criteria, losses, and the concrete rule for the next synthesis claim. |
| Model transformation vs preservation | Graph grammars and model transformations can produce useful carriers only when transformation rules, preserved structure, and lost structure are recoverable. |
| Bearer feasibility | A function or relation found by search matters architecturally only when an admitted bearer can carry it under constraints. |
| Reusable generator boundary | One-case generated output stays with C.35 and its declared next use; reusable-generator or mechanism-suite claims require the patterns that define or constrain those claims. |

### C.35:4 - Solution

Create one `StructuralSynthesisDiscoveryAdequacyNote@Project` before admitting the output into candidate synthesis, evaluation, publication, decision, or realization claims.

Read the note as an admission check between generation and architecture work. The generated output can be useful only after the record says what it carries, what it drops, which next architecture use it may support, and under what rule.

`carrierAdmissionReturnCondition` names the produced carrier or description, the described selected structure, preserved structure, lost structure, missing structure, the candidate-admission condition, and the next claim or question plus its required rule or test that must be revisited before the carrier can support the next architecture use.

Work in this order:

1. Name the grounded architecture question and selected source structure refs. If no grounded architecture question exists, require `C.30`, `C.32.P2S`, or `C.32`.
2. Name the generation or discovery Method and search or query space—for example, a DSM, MDM, MBSE query, graph grammar, model transformation, LLM proposal, NAS, DSE, QD archive, code-agent probe, simulation, benchmark, or source-mining method. When actual performed generation or discovery is part of the claim, separately name the dated `U.Work`, keep all facts required by A.15.1, A.2.1, and F.6 recoverable, and name the production, discovery-use, or work-to-change claim on which this note relies.
3. Separate produced carrier or description from described structure. The carrier may be a diagram, table, graph, query result, cluster, model file, prompt output, or benchmark trace. Naming it as produced does not by itself establish which Work produced it, entity-identity inception, production completion, or a relation to an actual transformation; cite the predicate or local claim that establishes any such assertion.
4. State preserved structure, lost structure, constraints, source-label recovery, observation and uncertainty refs, validation or comparison refs, and transformation trace when present. If an actual change is claimed, also cite the independently identified A.3.4 `U.Transformation`; the trace and the selected A.22 structures remain separate from that occurrence.
5. State candidate-admission condition. Use `C.32` only when the described structure can be used as a candidate configuration or candidate-generation input under selected structures, architecture characteristics, constraints, gains, losses, and carrier-admission return.
6. State bearer or realization boundary. Use `bearerFeasibilityQuestionRef?` only when a concrete software, physical, organizational, Method, or epistemic bearer-feasibility rule has opened that separate question. If the source says `role`, recover its actual bearer or relation through `E.10.ROLE`; a local kind or assignment bears no function merely by form. Name the function or feasibility predicate, conditions, and subject pattern, or return `missing-governor`.
7. Use `G.5` for selected-set result declaration, `C.18` and `C.19` for archive, front, and pool policy, `E.17` for a source-backed publication face and source return, and `E.24.PUB` for the publication occurrence and audience availability.
8. Handle eval programs and eval results under `C.32.ACE`; handle measurement under `C.16`; handle mathematical-lens use under `C.29`; handle descriptions and views under `C.30.AD` or `C.30.ASV`; handle decisions and ADR projections under `C.32.PAD` or `C.32.ADR`.
9. Handle reusable-generator or mechanism-suite claims with `E.20`, `G.1`, `G.10`, `G.11`, or another pattern that defines or constrains the generator claim, only after that reusable-generator object is current.
10. Stop when admissible use, non-admissible use, carrier-admission return condition, the next claim or question, and its required rule or test are named.

CGUS-aware neighbor use: when the produced carrier is useful because it describes, compresses, or demonstrates a constraint-governed unfolding structure, C.35 admits only the produced carrier for the declared architecture use. The unfolding structure itself remains governed by `A.22.CGUS`, `E.18.3`, `C.32.P2S`, `E.23`, or another direct structure pattern. If the produced object is only a route card, narrative sequence, demonstrative slice, or generated framework carrier, name it as a carrier or `DemonstrativeUnfoldingSlice@Context` before making any selected-structure claim about the `U.Structure` it presents. When it is a narrative sequence, `A.6.3.NAR` governs only the selected-source carry-through, ordering and connective account, loss, reader use, and return.

### C.35:5 - Archetypal Grounding

Tell: C.35 is the pattern for admitting or rejecting a produced output or carrier before another architecture claim relies on the selected structure it describes. The output may be generated, searched, clustered, queried, learned, transformed, simulated, or discovered. C.35 does not search, select, decide, or realize architecture. It asks what was produced, what selected structure it describes, what is preserved and lost, what bearer boundary remains open, and what must be true before C.32 or another architecture use can rely on it.

Show - generated artifact not yet structure. An LLM produces a plausible architecture diagram for a medical device. C.35 records the prompt output as produced carrier, recovers described module, control, evidence, and placement structures where possible, records missing constraints and unknown bearers, and sets candidate admission condition "C.32 palette entry only after selected structures, characteristics, gains, losses, and carrier-admission return are named." The output is not a project decision or realized architecture.

Show - DSM and MDM clustering. A DSM modularization clusters components by co-change and interface hints. C.35 records the relation matrix, clustering method, preserved dependency structure, lost functional bearer semantics, semantic-alignment risk, and a carrier-admission condition that requires C.31 modularity and reuse checks plus C.32 candidate-synthesis checks before use. The cluster can seed candidate synthesis and modularity review, but it is not architecture adequacy by itself.

Show - NAS result. A multi-objective NAS run returns a neural architecture graph and Pareto point. C.35 records search space, constraints, performance and resource criteria refs, generated carrier, described functional architecture structure, preserved dataflow, lost deployment and evidence structure, bearer boundary, and eval return. Use `C.32` for candidate-palette admission and `C.32.ACE` for evaluation results.

Show - graph grammar or model transformation. A graph-grammar Method is applied in dated generation Work and returns a candidate-structure carrier for a product-line model. C.35 names the Method, exact Work when performed-work reliance is current, produced carrier, independently selected source and described structures, rules, preserved interfaces, lost manufacturing constraints, and transformation trace. If the use additionally asserts an actual formal or world-side change, it cites the exact A.3.4 occurrence and the separately governed Work-to-change or A.15.PROD claim; otherwise `model transformation` remains the Method or operation-family label and no `U.Transformation` is inferred. C.34 may check preservation; C.32 admits only after selected-structure and characteristic effects are recoverable.

### C.35:6 - Bias-Annotation

| Bias | How C.35 counters it |
| --- | --- |
| Output authority bias | Require produced carrier, described structure, admission condition, bearer boundary, the next claim plus its required rule, and non-admissible use before any architecture claim relies on the output. |
| Pareto-point admission bias | Treat a Pareto point, benchmark score, archive member, or search trace as a candidate input cue until selected structures, criteria, constraints, losses, and the concrete candidate-use rule are named. |
| Reusable-generator collapse | Keep one-case output admission in C.35; handle reusable-generator, mechanism-suite, model-family, or production-pipeline claims with `E.20`, `G.1`, `G.10`, `G.11`, or another pattern that defines or constrains those claims. |
| Bearer-free synthesis bias | Require bearer or realization boundary before treating a discovered function, relation, or candidate form as architecturally feasible. |
| Eval substitution bias | Handle eval programs and eval results under `C.32.ACE`; handle measurement under `C.16`; do not let good eval numbers act as candidate admission or decision authority. |
| Currentness freeze | Reopen the admission note when source publication edition, source-use record, search space, query rule, validation trace, bearer constraints, realized structure, or eval return changes. |

### C.35:7 - Conformance checklist

| Check | Pass condition |
| --- | --- |
| `CC-C35-1` | Grounded architecture question, independently selected source structures, generation or discovery Method, and produced carrier or description are named. When performed generation or discovery matters, name one dated Work occurrence and keep all facts required by A.15.1, A.2.1, and F.6 recoverable. |
| `CC-C35-2` | Note, Method, dated generation or discovery Work, any actual transformation, production or work-to-change claim, produced carrier or description, described structure, selected candidate structure, realized holon structure, measurement return, eval return, decision authority, and composite project Work remain distinct. |
| `CC-C35-3` | Preserved structure, lost structure, constraints, source-label recovery, observation refs, uncertainty refs, validation refs, comparison refs, and transformation trace are present when they affect use; none substitutes for the A.3.4 basis of an actual transformation or the four A.22 structure discriminators. |
| `CC-C35-4` | Candidate admission condition names what must be true before C.32 can use the result. |
| `CC-C35-5` | Bearer or realization boundary is stated, and any feasibility question uses the rule that defines or tests it. |
| `CC-C35-6` | Each current archive, front, pool, publication, eval, measurement, mathematical-lens, decision, evidence, assurance, gate, release, method, or work claim uses the pattern that defines or tests it. |
| `CC-C35-7` | Admissible use, non-admissible use, carrier-admission return condition, the next claim or question, and its required rule or test are named. |

### C.35:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair move |
| --- | --- | --- |
| LLM output as architecture | A plausible diagram or prose proposal may not carry selected structures, constraints, bearer feasibility, or carrier-admission return. | Record the output as produced carrier; recover described structure; set candidate-admission condition; use `C.32.PAD` and `C.32.ADR` for the decision and ADR claims. |
| Pareto point as admission | A Pareto point shows trade-off position under chosen criteria, not architecture adequacy across selected structures and bearers. | Name search space, criteria refs, constraints, preserved and lost structure, bearer boundary, and eval return; then handle candidate use under `C.32`. |
| One output as reusable-generator governance | A single generated artifact does not describe the method, mechanism suite, dataset, prompt policy, or refresh process that produced a reusable generator. | Keep the one-case output in C.35 and open `E.20`, `G.1`, `G.10`, `G.11`, or another pattern that defines or constrains the reusable-generator claim. |
| Cluster as module architecture | A DSM or MDM cluster can preserve co-change or dependency pressure while losing functional bearer semantics and interface substitutability. | Handle modularity and reuse claims under `C.31`; handle candidate palette use under `C.32`; keep C.35 for admission of the produced cluster carrier. |
| Transformation output as feasibility proof | A graph grammar or model-transformation Method can return a useful carrier while neither proving an actual `U.Transformation` nor connecting performed Work to the change, production, manufacturing, deployment, organizational, or method bearers. | Record the Method, Work and attribution when current, carrier, transformation trace, independently selected source and described structures, preserved structure, lost structure, and bearer boundary. Cite A.3.4 plus the Work-to-change or A.15.PROD claim that establishes any actual change; otherwise keep that branch absent. Use C.34 for preservation and the rule that defines or tests feasibility. |
| Bypassing eval and measurement governance | A search score, benchmark, ablation, or validation trace can look like proof of architecture quality. | Handle readings under `C.16`, Q-bundle use to `C.25`, eval programs and eval results to `C.32.ACE`, and decisions to `C.32.PAD`. |

### C.35:9 - Consequences

Positive consequences:

- Generated or discovered outputs, produced carriers, descriptions, clusters, graphs, traces, and query results can enter architecture work without becoming authority. The architect gets a useful admission note instead of rejecting useful outputs or accepting them too early.
- C.35 keeps the carrier-admission return visible for later use: if the produced carrier cannot support the next architecture claim, the repair returns to the named carrier, described structure, lost or missing structure, admission condition, and required rule or test.
- C.32 continues to define candidate-palette admission. C.35 supplies the carrier admission and carrier-admission return information that C.32 may need.
- Search, query, transformation, and AI-assisted outputs become auditable: selected source structures, search space, constraints, preserved structure, lost structure, validation refs, and bearer boundaries are visible.
- Reusable generator governance stays outside C.35 until explicitly opened, which prevents one-case output review from becoming a hidden method or mechanism-suite pattern.

Costs and trade-offs:

- C.35 adds an admission step before fast use of generated outputs. That is a real cost when teams want quick candidate expansion.
- Some outputs will be useful but not yet admissible. The repair is not to discard them; it is to name the missing selected structure, bearer boundary, validation trace, or next claim plus its required rule.
- The pattern is intentionally narrow. It does not choose among alternatives, manage archives, define eval programs, or authorize work.

### C.35:10 - Rationale

Architecture synthesis increasingly receives outputs from search, model transformation, LLM proposal, code-agent mapping, DSM modularization, NAS, simulation, benchmark, and source discovery. Refusing those outputs would waste useful structure. Accepting them as architecture would create false authority. C.35 occupies the middle position: admission of a produced carrier for a declared architecture use.

The separation of produced carrier, described structure, selected candidate structure, bearer boundary, eval return, and decision authority is the core ontology of the pattern. Without that separation, C.35 would duplicate C.32, PAD, ADR, ACE, C.16, C.18, C.19, G.5, and the patterns that define the neighboring evidence, assurance, gate, release, method, or work claims.

The source families explain the chain. MBSE query practice and generated views show why produced descriptions can reveal and omit structure. Graph grammars and model transformations show why transformation trace and preserved structure matter. DSM and MDM work shows semantic-alignment risk between structural optimization and functional priors. Multi-objective NAS shows why Pareto fronts and generated architecture graphs need search-space, criteria, and bearer recovery. Sapunov, ToCS, and GonzoML show why agent maps and neural architecture labels need observation, uncertainty, and source-label recovery before candidate admission.

### C.35:11 - SoTA-Echoing

| Source or practice line | Adopt, adapt, or reject | Concrete C.35 locus changed | Boundary and currentness |
| --- | --- | --- | --- |
| MBSE query and view generation | Adapt generated views and model queries as produced carriers. | Strengthens carrier-description separation, selected source structures, query rule, described structure, and requires `C.30.AD` and `C.30.ASV`. | Query output or view output is not architecture, realized structure, or proof. Reopen when model edition, query rule, viewpoint, or described structure changes. |
| Graph grammars and model transformations | Adapt rule-governed production and transformation trace. | Adds selected source structures, target structures, transformation trace, preserved structure, lost structure, and C.34 preservation exit. | Grammar or transformation output does not prove adequacy, feasibility, or realization. Reopen when transformation rules, source model, target model, or constraints change. |
| DSM, MDM, and modularization practice including Jiang and Luo, arXiv:2604.28018 | Adapt modularization and LLM-assisted DSM work as structure-discovery sources. | Adds semantic-alignment risk, relation matrix pressure, cluster admission boundary, and C.31 plus C.32 exits. | Cluster, partition, or MDM slice is not candidate architecture adequacy. Reopen when relation matrix, modularity objective, functional prior, or solution pool changes. |
| Multi-objective NAS and Sukthanker et al., arXiv:2402.18213 | Adapt multi-objective search and Pareto profiling. | Adds search space, objective criteria refs, generated neural architecture graph, Pareto point, bearer boundary, eval return, and C.32 admission condition. | A Pareto point or neural graph is not holonic architecture adequacy until selected structures, bearer boundary, and the next architecture claim plus its required rule are recovered. Reopen when search space, criteria, hardware target, or eval trace changes. |
| DSE, QD, OEE, NQD, and evolutionary architecture practice inherited through C.32 | Adapt retained alternatives and stepping-stone pressure as candidate-input practice. | Strengthens candidate-generation input, carrier-admission return, archive exit, front exit, pool-policy exit, and C.32 governance. | These practices do not make C.35 a second candidate-set admission rule. `C.18`, `C.19`, and `G.5` define archive, front, and pool policy; `C.32` defines candidate-palette admission. |
| AI-assisted architecture design and AI-assisted ADD | Adapt generated descriptions, decompositions, relation graphs, and decision proposals. | Adds source-label recovery, uncertainty refs, validation or comparison refs, and candidate-admission boundary. | LLM proposal, ADD suggestion, benchmark trace, or agent consensus is not decision authority, evidence sufficiency, realization, or architecture adequacy by itself. |
| Sapunov, `Theory of Code Space`, and code-agent architecture-map practice | Adapt partial-observability discovery into architecture admission. | Adds observed, inferred, and unknown distinctions, confidence, unexplored regions, invariant discovery, active-passive comparison, and validation refs. | A code-agent map, JSON probe, benchmark score, dependency F1, invariant F1, or active-passive gap is not architecture adequacy, internal-state proof, safe-change authority, evidence sufficiency, gate passage, or release authority. |
| GonzoML neural-network architecture intake | Adapt neural architecture operation language for generated or searched outputs. | Adds source-label recovery for dataflow change, routing, gating, memory placement, cache placement, block substitution, pruning, distillation, NAS, ablation, and compute, memory, and latency trade-offs. | Neural-network labels, ablation gains, pruning masks, distillation success, and search outputs remain source cues until selected structure, bearer, affected characteristic, loss, and the next architecture claim plus its required rule are recovered. |

C.35 rejects the popular shortcut that a generated output, Pareto point, or cluster is a candidate architecture because it looks useful. The better practice is to admit the carrier only after the described structure, losses, bearer boundary, validation trace, and the next architecture claim plus its required rule are clear.

### C.35:12 - Relations

- **Builds on:** `C.30`, `C.30.AD`, `C.30.ASV`, `A.22`, `C.32.P2S`, and `C.32`.
- **Uses:** `C.34` when generated or transformed output must preserve selected source structure; `C.33` when capture and loss in the output are the current issue; `C.29` when a formal search, graph, entropy, category, or learned representation is being used as a mathematical lens.
- **Coordinates with:** `A.3.4` for each actual bounded change; `A.15.1`, `A.2.1`, and `F.6` for performed generation or discovery Work; `A.15.PROD` and `A.6.RCD` for exact production or Work-to-change claims; `C.36` when a cultural-evolution case supplies the generated or discovered carrier while retaining governance of that case; `C.30.STRAT`, `C.30.TFS-REL`, `A.6.M`, `C.31`, `C.31.ASAP`, `C.32.ACS`, `C.32.ACE`, `C.16`, `C.25`, `G.5`, `C.18`, `C.19`, `E.18`, `C.32.PAD`, and `C.32.ADR`.
- **Boundary:** C.35 governs generated or discovered carrier adequacy before or around C.32 candidate admission. It does not build the candidate palette, select from alternatives, govern reusable generators, define eval programs, measure values, decide projects, supply evidence or assurance, authorize work, or prove realization.

### C.35:End

