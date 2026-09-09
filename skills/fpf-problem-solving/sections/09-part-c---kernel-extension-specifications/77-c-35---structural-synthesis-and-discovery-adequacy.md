## C.35 - Structural Synthesis and Discovery Adequacy

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.35:1 - Problem frame

Use this pattern when a generated, searched, clustered, queried, learned, transformed, simulated, or discovered result may seed or inform architecturing, and the practitioner must decide what that exact result is and whether it can enter architecture work before or around `C.32` candidate admission.

Primary working reader: an architect, architecture researcher, AI-assisted architecture worker, model-based engineer, or reviewer receiving an exact result from DSM and MDM modularization, MBSE query and view generation, graph grammar, model transformation, NAS, DSE, QD, OEE, and NQD search, LLM-assisted architecture design, code-agent mapping, simulation, benchmark trace, or source discovery.

Typical entry phrases:

```text
"The LLM generated an architecture diagram; can it seed synthesis?"
"The DSM clustering suggests modules; is this a candidate architecture yet?"
"The MBSE query produced a view; does it describe an obtaining structure or only propose one?"
"NAS found a Pareto point; what architecture claim can use it?"
"A graph grammar transformed the model; what preservation and bearer boundary must be checked?"
```

**Primary working object.** The exact generated or discovered result on which the next architecture use would rely.

**First useful move.** Recover that result by its truthful kind, then say what organization it concerns, what the intended next use still requires, and what must not be inferred. If the organization is only proposed, keep it modal in an exact C.30 `ArchitectureClaim`. Treat a graph, diagram, matrix, encoding, or model as a separate C.29 representation when representation operations matter. Publication detail enters only when availability or form changes the use.

**Normal first result.** One sentence containing the same four facts is conforming. When a visible note is clearer, write only:

```text
Result: <exact result relied on>
Organization: <what already obtains or is only proposed>
Next-use condition: <one condition still required>
Limit and return: <forbidden overread and where to return>
```

Stop there when another practitioner can make the intended next move safely. Only when result identity, branch evidence, or a receiving claim must be reidentified independently, extend those four facts into the optional `StructuralSynthesisDiscoveryAdequacyNote@Project` C.2.1 episteme:
~~~text
StructuralSynthesisDiscoveryAdequacyNote@Project:
  resultRef:
  organizationConcern:
  nextArchitectureUseAndCondition:
  forbiddenOverreadOrReturn:
  resultKindAndIdentityRule?:
  admissibleUse?:
  unresolvedConditions?:
  representationRef?:
  representedObjectRef?:
  publicationFormRef?:
  publicationOccurrenceRef?:
  presentationCarrierRef?:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  structuralSynthesisAdequacyNoteProjectUseRelationRef?: U.RelationRef under a named architecture-use or work-use predicate when that relation identity is material
  groundedArchitectureQuestionRef?:
  resultBranch?: transformation | discovery | generative-proposal
  generationOrDiscoveryMethodRef?:
  generationOrDiscoveryWorkRef?: U.EntityRef constrained to U.Work
  generationOrDiscoveryWorkAttributionRefs?: refs to obtaining F.6 performedUnderAssignment relations only when the note or receiving use expressly represents attribution
  workToTransformationOrProductionClaimRefs?:
  transformationBranch?:
    exactSourceObjectRefs:
    exactResultObjectRefs:
    transformationTraceRef:
    preservedStructure:
    lostStructure:
    actualTransformationRefs?:
  discoveryBranch?:
    observationOrExtractionBasis:
    observedInferredUnknownStatus:
    coveredRegion:
    unexploredRegion:
    uncertainty:
    validation:
  generativeProposalBranch?:
    constraintRefs:
    proposedOrganizationContent:
    knownOmissions:
    validationNeeds:
    declaredBaselineComparison?:
      exactBaselineObjectRefs:
      preservedStructure:
      lostStructure:
  obtainingConstraintGovernedUnfoldingStructureRef?: exact A.22.CGUS reference only
  sourceLabelRecoveryRef?:
  obtainingStructureRefs?: exact A.22 U.Structure references only
  modalArchitectureClaimRef?: C.30 ArchitectureClaimRef or C.2.1 ClaimAddress to its exact claim
  candidateAdmissionCondition?:
  bearerOrRealizationBoundary?:
  obtainingRealizedHolonStructureRefs?: exact positive A.22 references only
  measurementOrEvalReturnRefs?:
  bearerFeasibilityQuestionRef?:
  nextClaimOrRuleRef?:
  receivingClaimKind?:
~~~
The note's first four fields reproduce the readable minimum; every later field is conditional on an actual dependency of the selected branch or receiving use. Its EntityOfConcern is the exact result designated by `resultRef`, not the reference value, representation, publication occurrence, form, or carrier used to reach it. When publication detail is relied on, `publicationFormRef`, `publicationOccurrenceRef`, and `presentationCarrierRef` each name their truthful object; omit every one that the receiving use does not need. Its ClaimGraph states the organization concerned, intended next use and condition, forbidden overread or return, and any additional admissible use or unresolved condition that the receiving use needs. Do not open or fill the dossier merely to prove completeness.

Here `@Project` is a compatibility and retrieval cue only. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. When the note is genuinely used in one actual project, `projectWorkOccurrenceRef` identifies the exact composite `U.Work` and `structuralSynthesisAdequacyNoteProjectUseRelationRef` identifies the direct relation by which that exact project Work uses the note. The suffix or either reference alone establishes no project locality. The admission-note episteme, its exact result, and the composite project Work remain distinct.

When the admission claim relies on performed generation or discovery, `generationOrDiscoveryWorkRef` is mandatory and names an independently admitted `U.Work` occurrence whose exact actual performers have A.13 cores and which A.15.1 admits independently; otherwise omit the Method and Work fields. `generationOrDiscoveryWorkAttributionRefs` are optional and appear only when the note or receiving use expressly represents precise assignment-bound attribution through the same obtaining A.13 assignment. Missing or failed F.6 leaves the Work ref intact. The Method, Work, attribution, admission-note episteme, generated result, representation, and any publication occurrence or carrier remain different objects.

`actualTransformationRefs` may cite only independently identified A.3.4 bounded changes; a Method label, transformation trace, graph edge, or before-and-after picture does not make a transformation actual. Any positive link from the Work to an actual transformation or produced entity must cite its declared predicate, an admitted A.6.RCD local claim, or the selected A.15.PROD branch in `workToTransformationOrProductionClaimRefs`; otherwise keep the objects separate and return `missing-governor`. An entry in `obtainingStructureRefs` resolves to an independently selected A.22 `U.Structure` with independently identified constituents, exact obtaining relation occurrences, applied constraints, and one named use frame. Whenever the result or a branch proposes an organization, `modalArchitectureClaimRef` is mandatory and identifies the exact C.30 `ArchitectureClaim` or ClaimAddress; its proposed constituents and relations stay modal until the A.22 basis actually exists. A result, representation, publication item, graph, cluster, description, or plausible modal wording supplies none of those four discriminators.

**Adoption test.** After using C.35, another practitioner can state the four-line minimum or an equivalent sentence: the exact result, the organization that already obtains or is only proposed, the one condition required for the next use, and the forbidden overread or return. That practitioner can also distinguish claim content, an obtaining A.22 structure, a C.29 representation, and a publication-side object. Additional identity, branch, Work, bearer, publication, evaluation, or next-claim detail appears only when the receiving use relies on it.

**What C.35 buys in practice.** The practitioner can keep a useful generated or discovered result without handing it architecture authority. Architecture use attaches to the exact result; changing a rendering or file does not silently change the admitted claim, and admitting a carrier does not silently admit claim content.

**Ordinary working move.** Write the one sentence or four lines first. Recover whether the organization already obtains or is only proposed, and stop if the next move and return are clear. Use A.22 only when its four identity discriminators resolve; otherwise keep the proposal modal in its exact architecture claim. Add a C.29 representation, branch basis, Method, Work, bearer, publication, evaluation, or exact next-claim reference only when the intended use depends on it.

**Not this pattern when.** If the current question is how to search, choose, measure, decide, authorize, publish, govern a reusable generator, govern a cultural-evolution case, or run the work itself, use the pattern that defines or decides that question first, including `C.36` for the cultural-evolution relation bundle. Use C.35 only when an exact generated or discovered result must be admitted or rejected before another architecture claim relies on it.

### C.35:2 - Problem

Modern architecture work receives claim-bearing outputs, representations, publication items, and other results from DSM clusters, MDM slices, MBSE queries, generated views, graph grammars, model transformations, LLM architecture proposals, AI-assisted ADD, code-agent relation graphs, NAS graphs, DSE traces, Pareto fronts, QD archives, benchmark traces, simulations, and source-corpus mining.

These results can expose candidate decompositions, relation gaps, hidden invariants, feasible search regions, trade-off points, source labels, or overlooked organization. They are not automatically obtaining A.22 structures, realized holon structures, eval results, evidence sufficiency, or decision authority.

C.35 handles the gap between exact result identity and architecture use. It first asks what the result is; which claim, represented object, or proposed organization it carries; whether representation or publication distinctions matter; and which architecture use is proposed. It then asks only the questions belonging to the actual branch. A transformation names its exact source and result objects, trace, preservation, and loss. A discovery names its observation or extraction basis, what is observed, inferred, or unknown, the covered and unexplored region, uncertainty, and validation. A generative proposal names its constraints, proposed organization or claim content, known omissions, and validation needs; source and preservation enter only when an actual baseline is declared. Method, performed Work, attribution, bearer feasibility, and publication detail enter only when the receiving use relies on them.

### C.35:3 - Forces

| Force | Tension |
| --- | --- |
| Discovery value vs authority overread | Generated and discovered outputs widen the candidate space; any selection, decision, proof, or realization claim still needs its own rule and support. |
| Result, proposal, obtaining structure, and representation | Claim-bearing result, modal architecture proposal, obtaining A.22 structure, represented object, representation, publication form or occurrence, and presentation carrier have different identities; include only the distinctions on which the architecture use relies. |
| Search quality vs architecture adequacy | A Pareto point, benchmark score, archive member, or cluster objective can guide synthesis only through the evidence required by its actual branch and the concrete rule for the next synthesis claim. |
| Model transformation vs preservation | Graph grammars and model transformations can return useful results, but transformation rules, exact source and result objects, trace, preserved structure, and lost structure matter only in the transformation branch. |
| Bearer feasibility | A function or relation found by search is architecturally feasible only when an admitted bearer can carry it under constraints. |
| Reusable generator boundary | One-case generated output stays with C.35 and its declared next use; reusable-generator or mechanism-suite claims require the patterns that define or constrain those claims. |

### C.35:4 - Solution

Start with the readable admission statement. Name the exact result, the organization it concerns, the one condition still required for the intended next use, and the forbidden overread or return. A sentence is enough; use the four-line form when separate lines make the boundary easier to see.

Use the smallest sufficient path:

1. Write the sentence or four lines. If they let the receiver act safely, stop.
2. When the obtaining-versus-proposed distinction affects use, identify the exact C.30 `ArchitectureClaim` or ClaimAddress for a proposal, or apply A.22's four discriminators for a positive structure. Add a C.29 representation only when correspondence or representation operations matter.
3. When the receiving use relies on how the result arose, add exactly one applicable branch. A transformation adds exact source and result objects, trace, preservation, and loss. A discovery adds observation or extraction basis, what is observed, what is inferred, what remains unknown, the covered and unexplored region, uncertainty, and validation. A generative proposal adds constraints, proposed organization content, known omissions, and validation needs; source and preservation enter only for an exact declared baseline.
4. When the admission claim relies on performed generation, discovery, production, or change, add the exact Method, dated `U.Work`, and the direct production, discovery-use, or Work-to-change claim. Otherwise omit them.
5. Add bearer feasibility, realized structure, publication, archive or front policy, evaluation, measurement, decision, reusable-generator, or exact next-claim references only when the intended use relies on that exact claim. Use its direct pattern rather than copying its dossier into C.35.
6. Stop when the receiver knows the admissible next move, the condition still open, and the limit or return. Materialize the optional full note only when those facts or their relied-on branch details need an independently reidentifiable result.

Conditional exits remain direct: `C.32` for candidate-palette use; `C.32.ACE` for eval programs and results; `C.16` for measurement; `C.29` for mathematical-lens use; `C.30.AD` or `C.30.ASV` for descriptions and views; `G.5`, `C.18`, and `C.19` for selected-set, archive, front, and pool claims; `E.24.PUB` for publication occurrence, form, and carrier; `E.17` for reader-facing publication of an accepted account; `C.32.PAD` for project architecture decisions and `C.32.ADR` for their ADR-like publication; and `E.20`, `G.1`, `G.10`, or `G.11` only when a reusable generator or mechanism suite is actually current.

CGUS-aware neighbor use: when a result is useful because it describes, compresses, or demonstrates a constraint-governed unfolding organization, C.35 admits only that exact result for the declared architecture use. Cite an A.22.CGUS structure only when its positive A.22 and A.22.CGUS basis already obtains; otherwise keep the organization as modal claim content. The structure itself, when it exists, remains with `A.22.CGUS`, `E.18.3`, `C.32.P2S`, `E.23`, or another direct structure pattern. If the encountered item is only a route card, narrative sequence, demonstrative slice, generated publication form, or presentation carrier, recover its claim-bearing result and represented object before making any positive structure claim. When it is a narrative sequence, `A.6.3.NAR` governs only the selected-source carry-through, ordering and connective account, loss, reader use, and return.


### C.35:5 - Archetypal Grounding

Tell: C.35 is the pattern for admitting or rejecting an exact generated or discovered result before another architecture claim relies on it. The result may come from search, clustering, query, learning, transformation, simulation, or discovery. C.35 does not search, select, decide, or realize architecture. It asks what the exact result is, whether the organization it concerns already obtains or is only proposed, what the intended use still requires, and what overread or return keeps it from acquiring false authority.

Show - generated claim and diagram not yet architecture. An LLM returns proposal claim `MedicalDeviceProposal-7` and diagram `MedicalDeviceDiagram-7`. The ordinary C.35 result is:

```text
Result: MedicalDeviceProposal-7.
Organization: a proposed device organization; its constituents and relations do not yet obtain.
Next-use condition: C.32 may use it after the missing safety constraint and bearer question are explicit.
Limit and return: do not read the proposal or diagram as A.22 structure or decision; return to the claim when either gap changes.
```

This is enough for the immediate candidate-use boundary. Add the generative-proposal branch only if the receiver relies on its constraints, omissions, or validation needs. Treat `MedicalDeviceDiagram-7` as a separate C.29 representation only when graphical correspondence matters; no source or preservation account is invented without a declared baseline.

Show - DSM and MDM clustering. A DSM modularization returns a clustering result based on co-change and interface hints. This is the discovery branch: C.35 identifies the exact claim-bearing cluster result and its extraction basis and records which dependencies are observed, which modular interpretation is inferred, what remains unknown, which matrix region was covered or unexplored, the uncertainty, and the validation needed before use. The inferred modular organization stays in its exact architecture claim; it is not an A.22 structure until the constituents, obtaining relations, applied constraints, and named use frame resolve. When matrix operations matter, C.29 separately identifies the representation and represented dependency object. A comparison with an earlier modularization may add an exact declared baseline and preservation account, but clustering alone does not require one.


Show - NAS result. A multi-objective NAS run returns a modal architecture claim about a proposed neural organization together with a graph representation and Pareto result. This is the generative-proposal branch: C.35 keeps those identities separate and records the search constraints, proposed organization content, known deployment and evidence omissions, bearer boundary, and validation and eval needs. The graph is a C.29 representation, not proof that the proposed relation occurrences obtain. C.35 does not invent a preserved-dataflow claim unless the run explicitly transforms or compares against a declared baseline. `C.32` may consume the proposal as candidate input; `C.32.ACE` handles evaluation results.

Show - graph grammar or model transformation. A graph-grammar Method is applied in dated generation Work and returns a claim-bearing result plus a graph representation for a product-line model. This is the transformation branch: C.35 names the Method, exact Work when performed-work reliance is current, exact source and result objects, rules, preserved interfaces, lost manufacturing constraints, and transformation trace. If the resulting organization is only proposed, it remains modal content in an exact architecture claim and the graph remains its C.29 representation. Source or result A.22 structures are cited only when their four discriminators independently resolve. If the use additionally asserts an actual formal or world-side change, it cites the exact A.3.4 occurrence and the separately governed Work-to-change or A.15.PROD claim; otherwise `model transformation` remains the Method or operation-family label and no `U.Transformation` is inferred. C.34 may check preservation; C.32 may admit the proposal without actualizing it.

### C.35:6 - Bias-Annotation

| Bias | How C.35 counters it |
| --- | --- |
| Output authority bias | Require only the readable minimum before another architecture claim relies on the result: exact result, actual or proposed organization, next-use condition, and forbidden overread or return. Add representation, publication, branch, or other detail only when the use depends on it. |
| Pareto-point admission bias | Treat a Pareto point, benchmark score, archive member, or search trace as a candidate input cue until its branch-specific basis and the concrete candidate-use rule are named. |
| Reusable-generator collapse | Keep one-case output admission in C.35; handle reusable-generator, mechanism-suite, model-family, or production-pipeline claims with `E.20`, `G.1`, `G.10`, `G.11`, or another pattern that defines or constrains those claims. |
| Bearer-free synthesis bias | Require bearer or realization boundary before treating a discovered function, relation, or candidate form as architecturally feasible. |
| Eval substitution bias | Handle eval programs and eval results under `C.32.ACE`; handle measurement under `C.16`; do not let good eval numbers act as candidate admission or decision authority. |
| Currentness freeze | Reopen when result identity or claim content, represented object or correspondence, source publication edition or source-use record, search space, query rule, validation trace, bearer constraints, realized structure, or eval return changes. A carrier-only change reopens C.35 only when availability or form changes the intended use. |

### C.35:7 - Conformance checklist

| Check | Pass condition |
| --- | --- |
| `CC-C35-1` | A sentence or four-line statement names the exact result, the organization that already obtains or is only proposed, the one condition required for the next use, and the forbidden overread or return. This is a conforming first result. |
| `CC-C35-2` | An optional materialized note has the exact result as its EntityOfConcern and repeats the readable minimum. It adds identity, representation, publication, project-use, branch, Method, Work, attribution, bearer, evaluation, or next-claim fields only when the receiving use relies on them. Any present publication-form, publication-occurrence, or presentation-carrier reference names its truthful object; absent publication apparatus creates no field-filling duty. |
| `CC-C35-3` | When branch evidence is relied on, exactly one branch is selected. Transformation supplies exact source and result objects, trace, preservation, and loss; discovery supplies observation or extraction basis, what is observed, what is inferred, what remains unknown, coverage, uncertainty, and validation; generative proposal supplies constraints, proposed organization content, omissions, and validation needs, with source and preservation only for an exact declared baseline. |
| `CC-C35-4` | A positive structure reference passes all four A.22 discriminators. Otherwise the organization remains modal architecture-claim content, which C.32 may receive as candidate input without treating it as obtaining architecture. |
| `CC-C35-5` | Bearer or realization detail appears only when the intended use relies on feasibility or realization; any such question uses the rule that defines or tests it. |
| `CC-C35-6` | Any current archive, front, pool, publication, eval, measurement, mathematical-lens, decision, evidence, assurance, gate, release, Method, or Work claim uses its direct pattern; an absent claim creates no C.35 field-filling duty. |
| `CC-C35-7` | The first result states the next-use condition and limit or return. An exact next-claim or rule reference is added only when the receiving action relies on reidentifying it independently. |

### C.35:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair move |
| --- | --- | --- |
| LLM output as architecture | Plausible prose and a diagram may denote a modal architecture claim and its representation; neither supplies obtaining relation occurrences, an A.22 structure, bearer feasibility, decision, or realization. | Recover the exact architecture claim or ClaimAddress, identify the diagram as a C.29 representation only when used, state the admission condition and return, and let C.32 consume the modal proposal without actualizing it. Use `C.32.PAD` and `C.32.ADR` for decision and ADR claims. |
| Pareto point as admission | A Pareto result records trade-off position under chosen criteria; its graph, table, or file is a neighboring representation or publication item, not architecture adequacy. | Name the exact result and the current next-use condition. Add search space, criteria, constraints, bearer boundary, and eval return only when the candidate use relies on them; then handle that use under `C.32`. |
| One output as reusable-generator governance | A single generated output does not by itself establish claims about the reusable generator's method, mechanism suite, dataset, prompt policy, or refresh process. | Keep the one-case output in C.35 and open `E.20`, `G.1`, `G.10`, `G.11`, or another pattern that defines or constrains the reusable-generator claim. |
| Cluster as module architecture | A cluster claim can expose co-change or dependency pressure while leaving functional-bearer semantics, interface substitutability, and obtaining relation occurrences unknown; its matrix or file does not settle that gap. | Recover the exact cluster result, extraction basis, observed and inferred content, unknowns, coverage, uncertainty, validation, and any C.29 representation. Keep the inferred organization modal unless A.22 passes; handle modularity and reuse under `C.31` and candidate use under `C.32`. |
| Transformation output as feasibility proof | A graph grammar or model-transformation Method can return a useful claim and representation while proving neither an actual `U.Transformation` nor an obtaining A.22 result structure. | Record the exact result, C.29 representation only when used, Method, Work and attribution when current, transformation trace, exact source and result objects, preservation, loss, and bearer boundary. Keep a proposed result organization in its architecture claim; cite A.22 only after its four discriminators resolve, and cite A.3.4 plus the Work-to-change or A.15.PROD claim for any actual change. |
| Bypassing eval and measurement governance | A search score, benchmark, ablation, or validation trace can look like proof of architecture quality. | Use `C.16` for measurement readings, `C.25` for Q-bundle use, `C.32.ACE` for eval programs and eval results, and `C.32.PAD` for project architecture decisions. |

### C.35:9 - Consequences

Positive consequences:

- Generated or discovered results can enter architecture work without becoming authority. Ordinary use stops after one sentence or four lines; the optional dossier appears only for a real downstream dependency.
- C.35 keeps the result-use return visible. If the exact result cannot support the next architecture claim, repair returns to that result, the obtaining structure or modal organization it concerns, the missing condition, and the required rule or test; the return never turns the proposal into an A.22 member.
- C.32 continues to define candidate-palette admission. C.35 supplies the result-use boundary that C.32 may need.
- Search, query, transformation, and AI-assisted results become auditable without conflating claim-bearing content, represented objects, representations, publication items, and carriers.
- Reusable generator governance stays outside C.35 until explicitly opened, which prevents one-case result review from becoming a hidden method or mechanism-suite pattern.
Costs and trade-offs:

- C.35 adds an admission step before fast use of generated outputs. That is a real cost when teams want quick candidate expansion.
- Some outputs will be useful but not yet admissible. The repair is not to discard them or fill irrelevant preservation rows; it is to supply the missing branch-specific basis, bearer boundary, validation, or next claim plus its required rule.
- The pattern is intentionally narrow. It does not choose among alternatives, manage archives, define eval programs, or authorize work.

### C.35:10 - Rationale

Architecture synthesis increasingly receives results from search, model transformation, LLM proposal, code-agent mapping, DSM modularization, NAS, simulation, benchmark, and source discovery. Refusing those results would waste useful structure. Accepting them as architecture would create false authority. Four readable facts are normally enough to hold the middle position: exact result, actual or proposed organization, next-use condition, and limit or return. The larger record is justified only by a receiving use that depends on its additional distinctions.

The separation among claim-bearing result, modal architecture claim, obtaining A.22 structure, represented object, C.29 representation, publication occurrence or form, presentation carrier, bearer boundary, eval result, and decision authority is the core ontology of the pattern. Without that separation, C.35 would duplicate C.29, C.32, PAD, ADR, ACE, C.16, C.18, C.19, G.5, E.24.PUB, and the patterns for evidence, assurance, gates, release, methods, and Work.
The source families explain why the branches differ. MBSE query practice, DSM and MDM work, and code-agent mapping expose discovery questions about extraction basis, observation, inference, unexplored regions, uncertainty, and validation. Graph grammars and model transformations expose the distinct need for exact source and result objects, trace, preservation, and loss. Multi-objective NAS and LLM-assisted design expose proposal questions about constraints, proposed organization, omissions, and validation without inventing a source structure. GonzoML shows why source labels still need recovery before any branch can support candidate admission.

### C.35:11 - SoTA-Echoing

| Source or practice line | Adopt, adapt, or reject | Concrete C.35 locus changed | Boundary and currentness |
| --- | --- | --- | --- |
| MBSE query and view generation | Adapt query results as discovery while separating the claim-bearing result, represented object, representation, and publication-side availability. | Adds query or extraction basis, separate observed, inferred, and unknown content, covered and unexplored model region, uncertainty, validation, and `C.30.AD` / `C.30.ASV` exits. | Query or view output is not architecture, realized structure, or proof. Reopen when result identity, model edition, query rule, viewpoint, represented object, coverage, or relied-on availability changes. |
| Graph grammars and model transformations | Adapt rule-governed transformation as the transformation branch. | Adds exact source and result objects, transformation trace, preserved structure, lost structure, and C.34 preservation exit. | Grammar or transformation output does not prove adequacy, feasibility, or realization. Reopen when transformation rules, source object, result object, trace, or constraints change. |
| DSM, MDM, and modularization practice including Jiang and Luo, arXiv:2604.28018 | Adapt modularization and LLM-assisted DSM work as discovery. | Adds extraction basis, observed dependencies, inferred clusters, unknown functional-bearer semantics, coverage, uncertainty, validation, and C.31 plus C.32 exits. | Cluster, partition, or MDM slice is not candidate architecture adequacy. Reopen when relation matrix, covered region, modularity objective, functional prior, validation, or solution pool changes. |
| Multi-objective NAS and Sukthanker et al., arXiv:2402.18213 | Adapt multi-objective search as a generative-proposal source. | Adds constraints, proposed neural organization, known omissions, validation needs, search criteria, bearer boundary, eval return, and C.32 admission condition. | A Pareto point or neural graph is not holonic architecture adequacy. Preservation is claimed only against an exact declared baseline. Reopen when search space, constraints, criteria, hardware target, proposal content, or eval trace changes. |
| DSE, QD, OEE, NQD, and evolutionary architecture practice inherited through C.32 | Adapt retained alternatives and stepping-stone pressure as candidate-input practice. | Strengthens candidate-generation input, result-use return, archive exit, front exit, pool-policy exit, and C.32 coordination. | These practices do not make C.35 a second candidate-set admission rule. `C.18`, `C.19`, and `G.5` define archive, front, and pool policy; `C.32` defines candidate-palette admission. |
| AI-assisted architecture design and AI-assisted ADD | Adapt generated decompositions, relation graphs, and decision proposals through the generative-proposal branch. | Adds constraints, proposed organization or claim content, known omissions, source-label recovery, validation needs, and candidate-admission boundary. | An LLM proposal, ADD suggestion, benchmark trace, or agent consensus is not decision authority, evidence sufficiency, realization, or architecture adequacy by itself. |
| Sapunov, `Theory of Code Space`, and code-agent architecture-map practice | Adapt partial-observability mapping through the discovery branch. | Adds observation or extraction basis, separate observed, inferred, and unknown content, confidence, covered and unexplored regions, active-passive comparison, and validation. | A code-agent map, JSON probe, benchmark score, dependency F1, invariant F1, or active-passive gap is not architecture adequacy, internal-state proof, safe-change authority, evidence sufficiency, gate passage, or release authority. |
| GonzoML neural-network architecture intake | Adapt neural architecture operation language as source-label recovery for discovery or generative proposals. | Adds recovery for dataflow change, routing, gating, memory placement, cache placement, block substitution, pruning, distillation, NAS, ablation, and compute, memory, and latency trade-offs without choosing a branch by label. | Neural-network labels, ablation gains, pruning masks, distillation success, and search outputs remain source cues until the branch-specific basis, bearer, affected characteristic, and next architecture claim plus its required rule are recovered. |

C.35 rejects the popular shortcut that a generated result, Pareto point, cluster, graph, or diagram is architecture because it looks useful. Recover the exact result first; add representation or publication details only when they matter; then state the intended use, missing condition, forbidden overread, and return.

### C.35:12 - Relations

- **Builds on:** `C.30`, `C.30.AD`, `C.30.ASV`, `A.22`, `C.32.P2S`, and `C.32`.
- **Uses:** `C.34` when the transformation branch or an explicit baseline comparison must preserve selected source structure; `C.33` when capture and loss in the output are the current issue; `C.29` when a formal search, graph, entropy, category, or learned representation is being used as a mathematical lens.
- **Coordinates with:** `A.3.4` for each actual bounded change; `A.15.1` for performed generation or discovery Work, `A.2.1` for the performers' obtaining assignments, and `F.6` only when precise assignment-bound attribution is current; `A.15.PROD` and `A.6.RCD` for exact production or Work-to-change claims; `C.36` when a cultural-evolution case supplies the generated or discovered result while retaining governance of that case; `C.30.STRAT`, `C.30.TFS-REL`, `A.6.M`, `C.31`, `C.31.ASAP`, `C.32.ACS`, `C.32.ACE`, `C.16`, `C.25`, `G.5`, `C.18`, `C.19`, `E.18`, `C.32.PAD`, and `C.32.ADR`.
- **Boundary:** C.35 governs exact-result use admission before or around C.32 candidate admission. It does not build the candidate palette, select from alternatives, govern reusable generators, define eval programs, measure values, decide projects, supply evidence or assurance, authorize work, publish the result, or prove realization.

### C.35:End

