## C.35 - Assess Generated or Discovered Results for Architecture Use

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
"The MBSE query produced a view; which organization is observed, proposed, or still unestablished?"
"NAS found a Pareto point; what architecture claim can use it?"
"A graph grammar transformed the model; what preservation and bearer boundary must be checked?"
```

**Primary working object.** The exact generated or discovered result on which the next architecture use would rely.

**First useful move.** Identify the result and the organization it concerns, then state its supported next use and any condition or limitation that affects reliance. Distinguish supported, refuted and unestablished claims about existing organization from proposals for a possible organization. Keep a proposal modal; add exact C.30 claim identity when the receiving use needs independent reidentification. Keep a representation distinct from its represented object when correspondence or representation operations matter. Use `C.30.AD` or `C.30.ASV` for architecture descriptions or views, and `C.29` for a remaining mathematical-representation choice, transfer, or reliance question. Publication detail enters only when availability or form changes the use.

**Normal first result.** A short sentence can suffice; reuse an adequate existing account. When separate lines help, use:

```text
Result: <exact result relied on>
Organization: <organization concerned; whether the claim about it is established, refuted or unestablished, or presents a proposal>
Next use: <supported use and any unresolved condition>
Limit and return, if needed: <material limitation and how to resolve it>
```

Stop there when another practitioner can make the intended next move safely. Only when result identity, branch evidence, or a receiving claim must be reidentified independently, extend those four facts into the optional `StructuralSynthesisDiscoveryAdequacyNote@Project` C.2.1 episteme:
~~~text
StructuralSynthesisDiscoveryAdequacyNote@Project:
  resultRef:
  organizationConcern:
  nextArchitectureUseAndCondition:
  forbiddenOverreadOrReturn?:
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
The note retains the result, organization, next use and any material limit or return; its fields are included when the selected branch or receiving use needs them. Its EntityOfConcern is the exact result designated by `resultRef`, not the reference value, representation, publication occurrence, form, or carrier used to reach it. When publication detail is relied on, `publicationFormRef`, `publicationOccurrenceRef`, and `presentationCarrierRef` each name their truthful object; omit every one that the receiving use does not need. Its ClaimGraph states the organization concerned, supported next use, and any material limitation or unresolved condition. A plausible mistaken inference is corrected when that changes reliance. Do not open or fill the dossier merely to prove completeness.

Here `@Project` is a compatibility and retrieval cue only. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. When the note is genuinely used in one actual project, `projectWorkOccurrenceRef` identifies the exact composite `U.Work` and `structuralSynthesisAdequacyNoteProjectUseRelationRef` identifies the direct relation by which that exact project Work uses the note. The suffix or either reference alone establishes no project locality. The admission-note episteme, its exact result, and the composite project Work remain distinct.

When reliance depends on how the result was actually generated or discovered, retain the actual operation and the material source, input, performer and condition facts needed to establish that history and its bearing on the result. For an express claim about a particular `U.Work`, `generationOrDiscoveryWorkRef` names that independently admitted occurrence: its actual performers have A.13 cores and A.15.1 supplies Work admission. Include the Method reference when the receiving claim depends on that Method. `generationOrDiscoveryWorkAttributionRefs` appear only for precise assignment-bound F.6 attribution. Missing or failed F.6 attribution alone leaves independently admitted Work intact; recheck an admission premise questioned by the same finding and any conclusion depending on it. The operation, Work, attribution, admission-note episteme, result, representation and publication objects retain their distinct identities.

`actualTransformationRefs` cite independently identified A.3.4 bounded changes. A positive link from Work to an actual transformation or produced entity uses the applicable declared predicate and its supporting facts, including A.15.PROD when its branch is selected. Return `missing-governor` under A.6.RCD when no applicable predicate governs the link; leave missing case facts unresolved and reject a link contradicted by them. An entry in `obtainingStructureRefs` resolves to an A.22 `U.Structure` with independently identified constituents, obtaining relation occurrences, applied constraints and a named use frame. An incomplete basis for a claim about existing organization leaves that claim unestablished. A proposal remains modal until its proposed organization obtains; supply `modalArchitectureClaimRef` when that claim must be independently reidentified. A result, representation, publication item, graph, cluster or description supplies only the structural facts it actually establishes.

**Adoption test.** After using C.35, another practitioner can state the four-line minimum or an equivalent sentence: the exact result, the organization concerned and whether the claim about it is established, refuted or unestablished, or presents a proposal, the supported next use and any unresolved condition, material limitation or required return. That practitioner can also distinguish claim content, an obtaining A.22 structure, its representation, and a publication-side object when those distinctions affect use. Additional identity, branch, Work, bearer, publication, evaluation, or next-claim detail appears only when the receiving use relies on it.

**What C.35 buys in practice.** The practitioner can keep a useful generated or discovered result without handing it architecture authority. Architecture use attaches to the exact result; changing a rendering or file does not silently change the admitted claim, and admitting a carrier does not silently admit claim content.

**Ordinary working move.** Explain the organization concerned, its actual or proposed status, what remains unestablished, and the use the result supports. Stop when the next move and any material limit or return are clear. Claim an obtaining A.22 structure only when its four identity discriminators resolve. Preserve an unestablished claim about existing organization as unresolved and a proposal as modal. Add exact claim identity, representation, branch, Method, Work, bearer, publication or evaluation detail when the intended use depends on it; use C.29 for an unresolved mathematical-representation choice, transfer, or reliance question.

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
| Model transformation vs preservation | Graph grammars and model transformations can return useful results, but the transformation claim needs its rules, source and result objects, trace and preservation/loss account. An express baseline comparison also needs the preservation relation it claims. |
| Bearer feasibility | A feasibility claim needs a viable bearer and applicable constraints. The bearer may be proposed; a claim that it actually exists requires its independent admission. |
| Reusable generator boundary | One-case generated output stays with C.35 and its declared next use; reusable-generator or mechanism-suite claims require the patterns that define or constrain those claims. |

### C.35:4 - Solution

Start with the result, the organization it concerns and its supported next use. State any unresolved condition or material limitation and how it can be resolved. A sentence or an adequate existing account can suffice.

Use the smallest sufficient path:

1. Give or reuse the sufficient account. If it lets the receiver make the intended next move, stop.
2. When organization status affects use, distinguish an obtaining structure, a refuted or unestablished claim about existing organization, and a proposal. Apply A.22's four discriminators to a positive structure claim. Add exact C.30 claim identity when the receiving use needs independent reidentification. Distinguish the representation when correspondence or representation operations matter; use C.29 for a remaining mathematical-representation choice, transfer, or reliance question.
3. When the receiving use relies on how the result arose, select the applicable branch for that claim. A complex result may need separate accounts for claims arising through different operations; do not infer one branch's basis from another. A transformation adds exact source and result objects, trace, preservation, and loss. A discovery adds observation or extraction basis, what is observed, what is inferred, what remains unknown, the covered and unexplored region, uncertainty, and validation. A generative proposal adds constraints, proposed organization content, known omissions, and validation needs; source and preservation enter only for an exact declared baseline.
4. When reliance depends on how the result arose, establish the actual operation and the history facts material to that use. Add the exact Method, independently admitted dated `U.Work`, and direct production, discovery-use or Work-to-change relation only when those particular claims are being made; retain the premises and evidence each requires.
5. Add bearer feasibility, realized structure, publication, archive or front policy, evaluation, measurement, decision, reusable-generator, or exact next-claim references only when the intended use relies on that exact claim. Use its direct pattern rather than copying its dossier into C.35.
6. Stop when the receiver knows the supported next move and any unresolved condition, material limit or return. Materialize the optional full note only when those facts or their relied-on branch details need an independently reidentifiable result.

Conditional exits remain direct: `C.32` for candidate-palette use; `C.32.ACE` for eval programs and results; `C.16` for measurement; `C.29` for an unresolved mathematical-representation choice, transfer, or reliance question; `C.30.AD` or `C.30.ASV` for descriptions and views; `G.5`, `C.18`, and `C.19` for selected-set, archive, front, and pool claims; `E.24.PUB` for publication occurrence, form, and carrier; `E.17` when a publication is an episteme projection; `C.32.PAD` for project architecture decisions and `C.32.ADR` for their ADR-like publication; and `E.20`, `G.1`, `G.10`, or `G.11` only when a reusable generator or mechanism suite is actually current.

CGUS-aware neighbor use: when a result is useful because it describes, compresses, or demonstrates a constraint-governed unfolding organization, C.35 admits only that exact result for the declared architecture use. Cite an A.22.CGUS structure only when its positive A.22 and A.22.CGUS basis already obtains; retain an unestablished claim about an existing organization as unresolved, and a proposal as modal claim content. The structure itself, when it exists, remains with `A.22.CGUS`, `E.18.3`, `C.32.P2S`, `E.23`, or another direct structure pattern. If the encountered item is only a route card, narrative sequence, demonstrative slice, generated publication form, or presentation carrier, recover its claim-bearing result and represented object before making any positive structure claim. When it is a narrative sequence, `A.6.3.NAR` governs only the selected-source carry-through, ordering and connective account, loss, reader use, and return.


### C.35:5 - Archetypal Grounding

C.35 is the pattern for admitting or rejecting an exact generated or discovered result before another architecture claim relies on it. The result may come from search, clustering, query, learning, transformation, simulation, or discovery. C.35 does not search, select, decide, or realize architecture. It asks what the exact result is, which organization it concerns, whether the claim about that organization is established, refuted or unestablished, or instead presents a proposal, what use it supports, and which conditions or limitations affect further reliance.

Generated claim and diagram not yet architecture. An LLM returns proposal claim `MedicalDeviceProposal-7` and diagram `MedicalDeviceDiagram-7`. The ordinary C.35 result is:

```text
Result: MedicalDeviceProposal-7.
Organization: a proposed device organization; its constituents and relations do not yet obtain.
Next-use condition: C.32 may use it after the missing safety constraint and bearer question are explicit.
Limit and return: do not read the proposal or diagram as A.22 structure or decision; return to the claim when either gap changes.
```

This is enough for the immediate candidate-use boundary. Add the generative-proposal branch only if the receiver relies on its constraints, omissions, or validation needs. Treat `MedicalDeviceDiagram-7` as a separate representation when graphical correspondence matters, using C.30.AD or C.30.ASV for its architecture description or view and C.29 when a mathematical-representation choice, transfer, or reliance question remains; no source or preservation account is invented without a declared baseline.

DSM and MDM clustering. A DSM modularization returns a clustering result based on co-change and interface hints. This is the discovery branch: C.35 identifies the exact claim-bearing cluster result and its extraction basis and records which dependencies are observed, which modular interpretation is inferred, what remains unknown, which matrix region was covered or unexplored, the uncertainty, and the validation needed before use. The inferred modular organization remains an unestablished claim about the existing organization until the needed constituents, obtaining relations, applied constraints and use frame are supported. A proposed reorganization remains a distinct modal claim. Retain the matrix's mapping to the represented dependencies and the validity conditions of its operations; use C.29 when choosing, transferring, or relying on that representation remains unresolved. A comparison with an earlier modularization may add an exact declared baseline and preservation account, but clustering alone does not require one.


NAS result. A multi-objective NAS run returns a modal architecture claim about a proposed neural organization together with a graph representation and Pareto result. This is the generative-proposal branch: C.35 keeps those identities separate and records the search constraints, proposed organization content, known deployment and evidence omissions, bearer boundary, and validation and eval needs. The graph represents the proposal; C.29 applies when a separate mathematical-representation choice, transfer, or reliance question remains. It does not prove that the proposed relation occurrences obtain. C.35 does not invent a preserved-dataflow claim unless the run explicitly transforms or compares against a declared baseline. `C.32` may consume the proposal as candidate input; `C.32.ACE` handles evaluation results.

Graph grammar or model transformation. A graph-grammar Method is applied in dated generation Work and returns a claim-bearing result plus a graph representation for a product-line model. This is the transformation branch: C.35 names the Method, exact Work when performed-work reliance is current, exact source and result objects, rules, preserved interfaces, lost manufacturing constraints, and transformation trace. If the resulting organization is only proposed, it remains modal content in an exact architecture claim and the graph remains a representation of that proposal, with C.29 used for an unresolved mathematical-representation choice, transfer, or reliance question. Source or result A.22 structures are cited only when their four discriminators independently resolve. If the use additionally asserts an actual formal or world-side change, it cites the exact A.3.4 occurrence and the separately governed Work-to-change or A.15.PROD claim; otherwise `model transformation` remains the Method or operation-family label and no `U.Transformation` is inferred. C.34 may check preservation; C.32 may admit the proposal without actualizing it.

### C.35:6 - Bias-Annotation

| Bias | How C.35 counters it |
| --- | --- |
| Output authority bias | Identify the result, organization, the status of the actual or proposed claim, and supported next use, with any material condition, limitation or return. Add representation, publication, branch, or other detail only when the use depends on it. |
| Pareto-point admission bias | Treat a Pareto point, benchmark score, archive member, or search trace as a candidate input cue until its branch-specific basis and the concrete candidate-use rule are named. |
| Reusable-generator collapse | Keep one-case output admission in C.35; handle reusable-generator, mechanism-suite, model-family, or production-pipeline claims with `E.20`, `G.1`, `G.10`, `G.11`, or another pattern that defines or constrains those claims. |
| Bearer-free synthesis bias | Require bearer or realization boundary before treating a discovered function, relation, or candidate form as architecturally feasible. |
| Eval substitution bias | Handle eval programs and eval results under `C.32.ACE`; handle measurement under `C.16`; do not let good eval numbers act as candidate admission or decision authority. |
| Currentness freeze | Reopen when result identity or claim content, represented object or correspondence, source publication edition or source-use record, search space, query rule, validation trace, bearer constraints, realized structure, or eval return changes. A carrier-only change reopens C.35 only when availability or form changes the intended use. |

### C.35:7 - Conformance checklist

| Check | Pass condition |
| --- | --- |
| `CC-C35-1` | A sentence or four-line statement names the exact result, the organization concerned and whether the claim about it is established, refuted or unestablished, or presents a proposal, the supported next use and any unresolved condition, material limitation or required return. This is a conforming first result. |
| `CC-C35-2` | An optional materialized note has the exact result as its EntityOfConcern and repeats the readable minimum. It adds identity, representation, publication, project-use, branch, Method, Work, attribution, bearer, evaluation, or next-claim fields only when the receiving use relies on them. Any present publication-form, publication-occurrence, or presentation-carrier reference names its truthful object; absent publication apparatus creates no field-filling duty. |
| `CC-C35-3` | When branch evidence is relied on, the applicable branch is selected for each claim; distinct operations in a complex result retain their separate bases. Transformation supplies exact source and result objects, trace, preservation, and loss; discovery supplies observation or extraction basis, what is observed, what is inferred, what remains unknown, coverage, uncertainty, and validation; generative proposal supplies constraints, proposed organization content, omissions, and validation needs, with source and preservation only for an exact declared baseline. |
| `CC-C35-4` | A positive structure reference passes all four A.22 discriminators. An unestablished claim about existing organization remains unresolved; a refuted claim stays refuted; a proposal stays modal. C.32 may use a qualified provisional result without treating an unestablished or proposed organization as obtaining architecture. |
| `CC-C35-5` | Bearer or realization detail appears only when the intended use relies on feasibility or realization; any such question uses the rule that defines or tests it. |
| `CC-C35-6` | Any current archive, front, pool, publication, eval, measurement, mathematical-lens, decision, evidence, assurance, gate, release, Method, or Work claim uses its direct pattern; an absent claim creates no C.35 field-filling duty. |
| `CC-C35-7` | The first result states the supported next use and any condition, limit or return that changes reliance. An exact next-claim or rule reference is added only when the receiving action relies on reidentifying it independently. |

### C.35:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair move |
| --- | --- | --- |
| LLM output as architecture | Plausible prose and a diagram may denote a modal architecture claim and its representation; neither supplies obtaining relation occurrences, an A.22 structure, bearer feasibility, decision, or realization. | Recover the proposal, adding exact claim identity when its use needs independent reidentification; distinguish the diagram and its correspondence when used. Use C.29 for an unresolved mathematical-representation choice, transfer, or reliance question. State the admission condition and return; C.32 can consume the modal proposal without actualizing it. Use `C.32.PAD` and `C.32.ADR` for decision and ADR claims. |
| Pareto point as admission | A Pareto result records trade-off position under chosen criteria; its graph, table, or file is a neighboring representation or publication item, not architecture adequacy. | Name the exact result and the current next-use condition. Add search space, criteria, constraints, bearer boundary, and eval return only when the candidate use relies on them; then handle that use under `C.32`. |
| One output as reusable-generator governance | A single generated output does not by itself establish claims about the reusable generator's method, mechanism suite, dataset, prompt policy, or refresh process. | Keep the one-case output in C.35 and open `E.20`, `G.1`, `G.10`, `G.11`, or another pattern that defines or constrains the reusable-generator claim. |
| Cluster as module architecture | A cluster claim can expose co-change or dependency pressure while leaving functional-bearer semantics, interface substitutability, and obtaining relation occurrences unknown; its matrix or file does not settle that gap. | Recover the exact cluster result, extraction basis, observed and inferred content, unknowns, coverage, uncertainty, validation, and the representation correspondence required by its use. Keep unestablished claims about the existing organization unresolved and any proposed reorganization modal; handle modularity and reuse under `C.31` and candidate use under `C.32`. |
| Transformation output as feasibility proof | A graph grammar or model-transformation Method can return a useful claim and representation while proving neither an actual `U.Transformation` nor an obtaining A.22 result structure. | Recover the exact result, source and result objects, transformation trace, preservation and loss, and the bearer boundary needed by the use. Include the Method, Work and attribution when those claims are current. Retain a relied-on representation correspondence and use C.29 for a remaining choice, transfer, or reliance question. Keep a proposed result organization in its architecture claim; cite A.22 only after its four discriminators resolve, and cite A.3.4 plus the Work-to-change or A.15.PROD claim for any actual change. |
| Bypassing eval and measurement governance | A search score, benchmark, ablation, or validation trace can look like proof of architecture quality. | Use `C.16` for measurement readings, `C.25` for Q-bundle use, `C.32.ACE` for eval programs and eval results, and `C.32.PAD` for project architecture decisions. |

### C.35:9 - Consequences

Positive consequences:

- Generated or discovered results can enter architecture work without becoming authority. Ordinary use can stop with a sufficient account; additional detail appears only for a receiving dependency.
- C.35 keeps the result-use return visible. If the exact result cannot support the next architecture claim, repair returns to that result, the organization it concerns and any unresolved or refuted claim about it, the missing condition, and the required rule or test; the return never turns the proposal into an A.22 member.
- C.32 continues to define candidate-palette admission. C.35 supplies the result-use boundary that C.32 may need.
- Search, query, transformation, and AI-assisted results become auditable without conflating claim-bearing content, represented objects, representations, publication items, and carriers.
- Reusable generator governance stays outside C.35 until explicitly opened, which prevents one-case result review from becoming a hidden method or mechanism-suite pattern.
Costs and trade-offs:

- Assessing a result takes attention. Reuse a sufficient account; obtain further detail when it can change the warranted next use.
- Some outputs will be useful but not yet admissible. The repair is not to discard them or fill irrelevant preservation rows; it is to supply the missing branch-specific basis, bearer boundary, validation, or next claim plus its required rule.
- The pattern is intentionally narrow. It does not choose among alternatives, manage archives, define eval programs, or authorize work.

### C.35:10 - Rationale

Architecture synthesis receives results from search, model transformation, LLM proposal, code-agent mapping, DSM modularization, NAS, simulation, benchmark and source discovery. A short account can identify the result, the organization it concerns and the supported next use, with any condition or limitation that affects reliance. The larger record is justified by a receiving use that depends on its additional distinctions.

The result can carry a proposal, describe an obtaining structure or serve as a representation. Its selected use determines which distinctions and supporting results matter: representation correspondence, feasibility, evaluation, publication or decision authority, for example. Obtain each required result under its own subject rule; retain a mathematical representation's mapping and validity conditions, using C.29 when a separate choice, transfer, or reliance question remains.
The source families explain why the branches differ. MBSE query practice, DSM and MDM work, and code-agent mapping expose discovery questions about extraction basis, observation, inference, unexplored regions, uncertainty, and validation. Graph grammars and model transformations expose the distinct need for exact source and result objects, trace, preservation, and loss. Multi-objective NAS and LLM-assisted design expose proposal questions about constraints, proposed organization, omissions, and validation without inventing a source structure. The GonzoML intake supplies neural operation vocabulary; resolve a source label when its meaning is unclear and changes the branch-specific claim or use.

### C.35:11 - SoTA-Echoing

| Source or practice line | Use of the contribution | Contribution to the assessment | Boundary of use |
| --- | --- | --- | --- |
| MBSE query and view generation | Adapt query results as discovery while separating the claim-bearing result, represented object, representation, and publication-side availability. | Identifies query or extraction basis, separate observed, inferred, and unknown content, covered and unexplored model region, uncertainty, validation, and `C.30.AD` / `C.30.ASV` exits. | Query or view output is not architecture, realized structure, or proof. Reopen when result identity, model edition, query rule, viewpoint, represented object, coverage, or relied-on availability changes. |
| Graph grammars and model transformations | Adapt rule-governed transformation as the transformation branch. | Identifies exact source and result objects, transformation trace, preserved structure, lost structure, and C.34 preservation exit. | Grammar or transformation output does not prove adequacy, feasibility, or realization. Reopen when transformation rules, source object, result object, trace, or constraints change. |
| DSM, MDM, and modularization practice including Jiang and Luo, arXiv:2604.28018 | Adapt modularization and LLM-assisted DSM work as discovery. | Identifies extraction basis, observed dependencies, inferred clusters, unknown functional-bearer semantics, coverage, uncertainty, validation, and C.31 plus C.32 exits. | Cluster, partition, or MDM slice is not candidate architecture adequacy. Reopen when relation matrix, covered region, modularity objective, functional prior, validation, or solution pool changes. |
| Multi-objective NAS and Sukthanker et al., arXiv:2402.18213 | Adapt multi-objective search as a generative-proposal source. | Identifies constraints, proposed neural organization, known omissions, validation needs, search criteria, bearer boundary, eval return, and C.32 admission condition. | A Pareto point or neural graph is not holonic architecture adequacy. Preservation is claimed only against an exact declared baseline. Reopen when search space, constraints, criteria, hardware target, proposal content, or eval trace changes. |
| DSE, QD, OEE, NQD, and evolutionary architecture practice inherited through C.32 | Adapt retained alternatives and stepping-stone pressure as candidate-input practice. | Connects candidate input and its use conditions to the applicable archive, front, pool policy and C.32 candidate-palette rules. | These practices do not make C.35 a second candidate-set admission rule. `C.18`, `C.19`, and `G.5` define archive, front, and pool policy; `C.32` defines candidate-palette admission. |
| AI-assisted architecture design and AI-assisted ADD | Adapt generated decompositions, relation graphs, and decision proposals through the generative-proposal branch. | Identifies constraints, proposed organization or claim content, known omissions, source-label recovery, validation needs, and candidate-admission boundary. | An LLM proposal, ADD suggestion, benchmark trace, or agent consensus is not decision authority, evidence sufficiency, realization, or architecture adequacy by itself. |
| Sapunov, `Theory of Code Space`, and code-agent architecture-map practice | Adapt partial-observability mapping through the discovery branch. | Identifies observation or extraction basis, separate observed, inferred, and unknown content, confidence, covered and unexplored regions, active-passive comparison, and validation. | A code-agent map, JSON probe, benchmark score, dependency F1, invariant F1, or active-passive gap is not architecture adequacy, internal-state proof, safe-change authority, evidence sufficiency, gate passage, or release authority. |
| GonzoML neural-network architecture intake | Adapt neural architecture operation language as source-label recovery for discovery or generative proposals. | Identifies recovery for dataflow change, routing, gating, memory placement, cache placement, block substitution, pruning, distillation, NAS, ablation, and compute, memory, and latency trade-offs without choosing a branch by label. | Use clear source-local meanings directly. Obtain the branch-specific basis, bearer or characteristic needed by the architecture claim; ablation or benchmark gains alone do not establish it. |

### C.35:12 - Relations

- **Builds on:** `C.30`, `C.30.AD`, `C.30.ASV`, `A.22`, `C.32.P2S`, and `C.32`.
- **Uses:** `C.34` when the transformation branch or an explicit baseline comparison must preserve selected source structure; `C.33` when capture and loss in the output are the current issue; `C.29` when choosing, transferring, or relying on a mathematical representation remains unresolved.
- **Coordinates with:** `A.3.4` for each actual bounded change; `A.13` for actual performer assignment bases, then independent `A.15.1` for performed generation or discovery Work, `A.2.1` for the assignments, and `F.6` only when precise assignment-bound attribution is current; `A.15.PROD` and `A.6.RCD` for exact production or Work-to-change claims; `C.36` when a cultural-evolution case supplies the generated or discovered result while retaining governance of that case; `C.30.STRAT`, `C.30.TFS-REL`, `A.6.M`, `C.31`, `C.31.ASAP`, `C.32.ACS`, `C.32.ACE`, `C.16`, `C.25`, `G.5`, `C.18`, `C.19`, `E.18`, `C.32.PAD`, and `C.32.ADR`.
- **Boundary:** C.35 governs exact-result use admission before or around C.32 candidate admission. It does not build the candidate palette, select from alternatives, govern reusable generators, define eval programs, measure values, decide projects, supply evidence or assurance, authorize work, publish the result, or prove realization.

### C.35:End
