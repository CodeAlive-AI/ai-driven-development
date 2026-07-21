## C.31 - Modularity and Reusable Structure Characteristics

> **Type:** Characterization pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.31:1 - Problem frame

Use this pattern when modularity or reusable-structure language is doing work in an architecture discussion and the practitioner needs to know which few characteristics matter, what repair follows, and whether any measurement or comparison is admissible.

The first useful move is deliberately small:

```text
ModularityVectorLite:
  describedHolonRef:
  boundedContextRef:
  architectureClaimRef?:
  structureKindRefs:
  threeLiveCharacteristicsAtMost:
  observedProblem:
  repairDirection:
  relatedClaimGovernanceIfClaimed:
  nonAdmissibleOverread:
  stopCondition:
```

Start with recognition, at most three characteristics under evaluation, the observed problem, and a repair direction. A report-only proxy is an admissible stop when no beyond-local-repair use is being made.

Claim-use boundary: comparison, publication, evidence, assurance, gate, decision, benchmark, causal-use, cross-case reuse, selection, procurement, and architecture scale-preference are beyond-local-repair uses in C.31. Add their fields only when that use is being made and recoverable by value and the governing pattern can be named.

What goes wrong if C.31 is missed: "modular" becomes a binary label; a single modularity score hides incompatible characteristics; interface publication is confused with substitutability; internal cohesion is improved while evidence reuse gets worse; bespoke residue moves from templates into work or assurance; and complexity language becomes a commensurable score without a declared characteristic, scale, measurement basis, comparison basis, or admissible-use boundary.

What C.31 buys in practice: the practitioner can see which modularity characteristic changes the next architecture use, which false use is blocked, which repair is plausible, and which governing pattern governs measurement, evidence, causal, scale, selection, or accounting claims.

Not this pattern when the question under repair is only source-label recovery, module-interface relation repair, reusable-structure accounting, general measurement admissibility, quality-family claim, architecture scale-preference claim, mathematical-lens use, candidate architecture synthesis, or selection. Use `C.30.STRAT`, `A.6.M`, `C.31.RSA`, `C.16`, `C.25`, `C.31.ASAP`, `C.29`, `G.5`, or `C.11` as appropriate; do not treat C.31 as the synthesis or selector pattern.

### C.31:2 - Problem

Architecture work often asks for more modularity, better reuse, lower coupling, more explicit interfaces, cleaner allocation, or less bespoke residue. These phrases point to real engineering work, but they do not name one scalar property.

Modularity can improve along one characteristic while worsening another. A design can reduce external coupling and increase interface alphabet size. A platform can standardize interfaces and create unhelpful rigidity. Evidence reuse can improve while functional-to-module allocation remains tangled. A report can show a high reuse share while hiding source-return work or residual uncertainty.

C.31 turns modularity talk into a small characteristic vector plus repair direction. It does not promise that every characteristic is measurable now, comparable across cases, causal, admissible for decision use, or evidence-backed.

### C.31:3 - Forces

| Force | Tension |
| --- | --- |
| Fast architecture repair vs measurement admissibility | Practitioners often need the next modularity move before a full measurement template exists. |
| Characteristic plurality vs scalar pressure | Different modularity interpretations have different subjects, scales, evidence, declared measurement or comparison basis, governing-pattern needs, and risks; one score hides that plurality. |
| Useful proxy vs proxy substitution | A cheap share, count, or graph interpretation can guide local repair, but it may become a false quality, evidence, or decision claim. |
| Module-interface view vs broader structure | Modularity can involve functions, flows, control, work, evidence, data, placement, or scale, not only modules. |
| Local repair vs cross-case publication | A local diagnosis can stop at report-only use; cross-case comparison needs C.16, C.25, G.2, and possibly G.5 or C.11 claim-governance assignment. |
| Complexity pressure vs complexity ontology | Residual pressure and growth signals are useful, but complexity is not one commensurable architecture characteristic. |

### C.31:4 - Solution

C.31 governs modularity and reusable-structure characteristics as C.16-compatible characteristic heads, composite descriptions, lens-backed characteristic interpretations, temporal or scale-sensitive characteristic interpretations, causal-use-sensitive characteristic interpretations, or report-only proxies. It starts from action guidance and adds fields for beyond-local-repair use only when a use being made requires them.

#### C.31:4.1 - Ordinary output: `ModularityVectorLite`

`ModularityVectorLite` is the ordinary output. It names at most three characteristics under evaluation because the first task is to find the next repair, not to audit all possible modularity interpretations.

```text
ModularityVectorLite:
  describedHolonRef:
  boundedContextRef:
  architectureClaimRef?:
  structureKindRefs:
  threeLiveCharacteristicsAtMost:
    - characteristicRef:
      currentCue:
      repairDirection:
      claimUseClass:
      forbiddenOverread:
  observedProblem:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

The vector is complete enough when it states what can be done next and what cannot be inferred. If a characteristic is used beyond local repair, use the appropriate card and governing pattern; architecture scale-preference claims are governed by `C.31.ASAP`.

#### C.31:4.1a - Filled `ModularityVectorLite`

```text
ModularityVectorLite:
  describedHolonRef: ProductPlatform@FieldPumpFamily
  boundedContextRef: FieldServiceAndProcurement@2026Q2
  architectureClaimRef?: ArchitectureOf@PumpControllerPlatform
  structureKindRefs: ModuleInterfaceStructure, EvidencePackageStructure
  threeLiveCharacteristicsAtMost:
    - characteristicRef: InterfaceStandardizationShare
      currentCue: controller ports are named by the same API family, but three field variants still require adapter-specific wiring.
      repairDirection: narrow the interface grammar and name the allowed variation before counting the interface as standardized.
      claimUseClass: local repair cue
      forbiddenOverread: the public API label is not substitutability or procurement suitability.
    - characteristicRef: SubstitutabilityWidth
      currentCue: two alternate controller boards pass the bench test, but only one has the required thermal envelope and connector constraints.
      repairDirection: state the substitution conditions and the exception before using the alternative count.
      claimUseClass: report-only proxy until C.16 or selection use is being made
      forbiddenOverread: the alternate-board count is not a selection result.
    - characteristicRef: EvidenceReuseShare
      currentCue: electrical-safety evidence is reused, while environmental evidence is recreated per enclosure variant.
      repairDirection: split reusable evidence package from variant-specific evidence and add source-return condition.
      claimUseClass: local repair cue with possible evidence-package use
      forbiddenOverread: reused evidence is not assurance sufficiency.
  observedProblem: the team says the platform is modular because interfaces are public and evidence is reusable, but field replacement and certification still create variant-specific work.
  relatedClaimGovernanceIfClaimed: A.6.M for the module-interface relation; C.31.RSA if report-only share becomes reusable-structure accounting; A.10 or B.3 only if evidence or assurance use is being made.
  stopCondition: stop at local repair until measurement basis, comparability basis, and any selection or assurance use are declared by their governing patterns.
```

Near miss: a high interface-standardization count alone is not a C.31 improvement. If field-service work, source-return events, or variant-specific evidence increase, the vector records that proxy divergence and returns to repair rather than treating the count as architecture quality.

#### C.31:4.2 - Characteristic classes

Every C.31 head is classified before use:

| Class | Use | Boundary |
| --- | --- | --- |
| `DirectCharacteristic` | A C.16-governed characteristic can be named with subject, scale, unit or unitless interpretation, declared measurement basis, comparability basis, and repair action. | It is not automatically a score or decision selector. |
| `CompositeCharacteristicDescription` | The head is a bundle or description with sub-slots, such as function-module alignment or flow-boundary alignment. | Do not pretend the bundle is one raw measure. |
| `LensBackedCharacteristic` | The head depends on a model description or mathematical lens, such as compression or RG or coarsening lens. | Apply C.29 for lens use that changes action. |
| `TemporalOrScaleCharacteristic` | The head depends on time window, repeated instance, scale variable, aggregation scope, or source-return condition. | Apply `C.31.ASAP` for architecture scale preference, `C.27` for temporal adequacy, and `C.18.1` or `C.19.1` when scale-law or general BLP preference claims are being made. |
| `CausalUseSensitiveCharacteristic` | The interpretation is used to claim effect or intervention success. | Apply C.28 before relying on the claim causally. |
| `ReportOnlyProxy` | The interpretation is only a local diagnostic or communication aid. | State forbidden overread and the governing pattern needed for any beyond-local-repair use. |

In C.31, `declared basis` and `comparability basis` name C.16-compatible measurement or comparison fields. They are not generic reason words and are not substitutes for evidence, assurance, cause, source, decision, or architecture-description relations.

#### C.31:4.3 - Measurement-head mapping

When a head becomes decision-facing or publication-facing, create `MeasurementHeadMapping` before relying on it:

```text
MeasurementHeadMapping:
  sourceHead:
  knownMeasureFamilyOrPractice:
  fpfCharacteristicKind:
  scaleType:
  unitPolicy:
  declaredBasisNeeded:
  requiredEvidence:
  evidenceRelationRefs?:
  evidenceProvenanceRelationRefs?:
  sourceRelationRefs?:
  evidenceClaimAbsentBecause?:
  commonFalseUse:
  nonAdmissibleUse:
  repairAction:
  governingPatternRef:
```

This mapping is not a measurement template by itself. It prepares a C.16-compatible characteristic card or a report-only boundary. When the head is decision-facing or publication-facing, the mapping names required evidence plus at least one evidence relation, evidence-provenance relation, or source relation. If no evidence claim is being made, `evidenceClaimAbsentBecause` states why the head remains local, report-only, or repair-only.

#### C.31:4.4 - C.31 characteristic card

Use the full card only when the use goes beyond local repair:

```text
ModularityCharacteristicCard:
  characteristicRef:
  subjectRef or relationSubjectTuple:
  characteristicClass:
  scaleRef:
  unitInterpretation:
  declaredBasisRef:
  comparabilityBasisRef:
  requiredEvidence:
  evidenceRelationRefs?:
  evidenceProvenanceRelationRefs?:
  sourceRelationRefs?:
  evidenceClaimAbsentBecause?:
  proxyRisk:
  auditQuestion:
  nonAdmissibleUse:
  repairAction:
  relatedClaimGovernanceRefs:
```

Each card states its own C.16 well-formedness fields: characteristic, scale, unit or unitless interpretation, declared measurement basis, comparability basis, evidence relation, evidence-provenance relation, source relation, or evidence-claim-absent reason, non-admissible use, and repair action. When source material is used as evidence, the source relation is named. A source checklist, source-discharge slice, dashboard label, or inherited score is not enough.

#### C.31:4.5 - Seed characteristic heads and repair actions

These heads are seeds, not an exhaustive taxonomy. Use only the heads that change the next action.

| Characteristic head | Intended characteristic interpretation | Typical scale or value form | Declared measurement or comparison basis | Defect signal | Repair direction | Escalation trigger |
| --- | --- | --- | --- | --- | --- | --- |
| `InternalCohesionDensity` | Density of typed relations inside a proposed module. | ratio or graph-derived value | typed dependency graph or DSM | proposed module has insufficient typed internal dependency basis | split the proposed module, move relations, or reclassify as component relation | comparison, clustering, or publication use |
| `ExternalCouplingDensity` | Cross-boundary dependencies per module or interface. | ratio or distribution | typed dependency graph, interface graph, integration defects | hidden external dependencies dominate module boundary | expose dependency, revise interface spec, split context, or accept bounded exception | integration risk, assurance, or release claim |
| `InterfaceAlphabetSize` | Count or entropy-like variety of interface types. | count or entropy-like value | interface registry | too many interface variants erase modular benefit | reduce variants, introduce interface grammar, split context, or document exception | platform grammar, candidate selection, or publication use |
| `InterfaceStandardizationShare` | Share of interfaces conforming to declared specifications. | ratio or percentage | conformance tests and specifications | standardization is low where reuse needs it | define or narrow standards, add conformance tests, or stop at local exception | cross-case comparison, certification, or procurement decision claim |
| `InterfacePublicness` | Openness, publication, and vendor-neutrality value. | ordinal or category | standards, API specs, licensing, access terms | open label lacks substitutability relation, substitution policy, conformance expectation, or interface specification | recover interface spec, substitution policy, and conformance expectation | open-architecture claim, procurement decision claim, or publication claim |
| `SubstitutabilityWidth` | Number or diversity of compatible alternatives for a slot or interface. | count or diversity value | approved implementations, vendors, tests | only one viable implementation exists | repair interface spec, loosen unnecessary coupling, or mark single-source exception | competition, platform, or decision claim |
| `ModuleTypeReuseRate` | Instances per module type or template. | ratio or count | product-line records, bills of material, template records | reuse is claimed only by repeated naming | define module type, allowed variation, and measurement basis | cross-case reuse or product-line publication |
| `TemplateCompressionGain` | Description saving from template plus parameters compared with instance-by-instance descriptions. | ratio or bits under declared method | corpus or model-description method | compression erases safety, law-domain, or source distinctions | add source-return condition, split template, or apply C.29 | lens-characteristic or effect claim, publication, or decision use |
| `FunctionModuleAlignmentCharacteristic` | Functional elements and module relations align without unmanaged many-to-many exceptions. | vector, ordinal, or bundle description | functional view and module relation records | allocation hides many-to-many exceptions | split function from module claim, revise allocation, or add correspondence | candidate decomposition or quality-composition claim |
| `FlowModuleBoundaryAlignmentCharacteristic` | Flow topology crosses declared interfaces rather than hidden channels. | vector, ordinal, or bundle description | transformation-flow structure refs and interface refs | flows bypass declared module boundaries | expose crossing, revise interface, or apply C.30.TFS-REL for the architecture-to-transformation-flow relation claim | publication or assurance claim about the architecture-to-transformation-flow relation |
| `ControlStructureSeparationCharacteristic` | Control responsibilities, rates, and boundaries are explicit enough for the architecture move. | ordinal or vector | LCA or control description and temporal adequacy basis | control relation is hidden inside module label | apply C.30.LCA, C.27, A.3.3, or B.3 when a control, temporal, dynamics, or assurance claim kind is being made | stability, assurance, or gate use |
| `HiddenCouplingDiscoveryRate` | Hidden dependencies discovered after integration or change. | rate | defect and change records | dependencies appear late | expose side channel, revise interface spec, add sentinel, or reopen boundary | integration risk, repeated release, or assurance claim |
| `CrossBoundaryChangeReach` | How many modules, views, or work items a local change touches. | distribution | change-impact records | local change travels farther than claimed | split relation, add interface grammar, revise allocation, or source return | release, decision, or comparison claim |
| `WorkRepeatabilityShare` | Delivery, operation, or test work under repeatable method descriptions. | ratio | work records and method descriptions | work repeats as bespoke effort | move repeated work into `MethodDescription` or accept exception | work planning, evidence reuse, or scale use |
| `EvidenceReuseShare` | Evidence package items reused across instances or contexts. | ratio | evidence graph and validity context | evidence is recreated or mis-scoped | move repeated evidence into reusable evidence or assurance package | certification, safety-case, or assurance claim |
| `RegulatoryBespokeResidue` | One-off regulatory or acceptance content not covered by reusable structures. | ratio or ordinal | safety, approval, or regulatory records | each instance needs new regulatory argument | isolate residue, add reusable evidence package, or keep bounded exception | safety case, approval, or publication claim |
| `LearningTransferCoefficient` | Improvement transfer from one instance or run to subsequent instances. | slope or elasticity | repeated work data and learning curve records | improvement claim hides time or causal assumptions | apply C.27 for temporal adequacy and C.28 for causal use | causal, benchmark, or scale-preference use |
| `BespokeResidueShare` | Share of structure not covered by reusable templates or rules. | report-only share unless C.16 measurement basis is declared | RSA description and exception register | residue is hidden under reuse score | use C.31.RSA and source-return condition | accounting, comparison, or decision claim |
| `RGFlowStability` | Stability of characteristic vector across declared coarse-graining scopes. | vector or ordinal | declared multi-scope architecture graphs | coarse-graining hides lower-scope hazards | apply C.29 for lens use and C.31.ASAP when an architecture scale-preference claim is being made | RG, scale, or lens transfer use |
| `ExceptionCurveSlope` | Change in one-off exceptions over a scale variable. | slope | exception records against scale variable | exceptions grow with scale | apply C.31.ASAP or accept bounded exception | scale preference, publication, or decision claim |

#### C.31:4.6 - Claim-scoped residual heads

C.31 uses residual heads only as qualitative repair cues. These heads do not create one complexity characteristic.

| Head | Meaning | Related claim governance | Risk | Repair direction |
| --- | --- | --- | --- | --- |
| ComplexityGrowthPressure | Pressure to add, split, mediate, or stabilize a declared aggregation scope, interface grammar, control relation, evidence scope, work-method scope, abstraction scope, or source-return condition. | C.30.ILC, C.31.ASAP when an architecture scale-preference claim is being made, G.5, C.11 | treating more apparatus as progress | name the pressure and the repair direction; use set-return or decision patterns when the corresponding claim is being made |
| `FrustrationResidual` | Persistent cross-scope residual after local repair. | `C.30.ILC`, C.29-local cross-scope lens claim | turning a lens-backed interpretation into proof | keep as residual cue or apply C.29 or C.30.ILC |
| `ConflictResidualSlope` | Residual grows or shrinks over declared scale variable, scale window, or coarse-graining scale. | `C.31.ASAP`, `C.29`, `C.27`, `C.18.1`, `C.19.1` | treating two points as universal law | declare window, lens-use boundary, and measurement basis or stop at report-only |
| `DeclaredScopeAdditionCost` | Added work, evidence, change-policy, latency, observability, accountability, or interface cost from a new declared aggregation or control scope. | `C.16`, `C.31`, `C.30.LCA` | ignoring the cost of added structure | identify cost bearer and apply the measurement pattern if used for comparison |
| `BespokeResidueGrowth` | One-off exceptions grow with deployment spread, regulation, or project repetition. | `C.31.RSA`, `C.31.ASAP` when an architecture scale-preference claim is being made | assuming all bespoke work is bad | split useful exception from repairable residue |
| `InterfaceAlphabetGrowth` | Interface variants grow faster than reuse, substitutability, or integration payoff. | `A.6.M`, `C.31` | premature standardization | add platform grammar, split context, or accept bounded variation |
| `SourceReturnCost` | Frequency or cost of returning from a compressed, indexed, coarse, extracted, or accounting view to source-side structure records. | `C.29`, source-return discipline, `A.10` | over-compression | add source-return condition or reduce compression |
| `ControlNestingDepthRisk` | Nested control relations create latency, accountability, observability, stability, or assurance cost. | `C.30.LCA`, `C.27`, `B.3`, `A.3.3` | LCA-as-proof | apply control, temporal, assurance, or dynamics governing patterns when the corresponding claim is being made |

#### C.31:4.7 - Proxy-risk discipline

Every decision-facing C.31 card includes `ProxyRisk` and `AuditQuestion`. If the proxy diverges from the value it was meant to represent, the card stops at report-only use or returns to repair.

| Head | Proxy risk | Audit question |
| --- | --- | --- |
| `ExternalCouplingDensity` | Teams hide dependencies instead of reducing them. | Did integration failures or source-return events fall? |
| `InterfaceStandardizationShare` | Premature standardization blocks useful variation. | Did exception slope or workarounds rise? |
| `InterfacePublicness` | Open label without substitutability. | Are alternative implementations actually viable under declared conditions? |
| `TemplateCompressionGain` | Compression erases safety, law-domain, or source distinctions. | Did source-return events or bounded exceptions rise? |
| `EvidenceReuseShare` | Reused evidence becomes stale or mis-scoped. | Does evidence remain valid in the new context? |
| `RGFlowStability` | Coarse-graining hides lower-scope hazards. | Are source-return conditions triggered? |

#### C.31:4.8 - Rejected shortcut

The expression `ModularityScore = average(all measures)` is not admissible as a C.31 result. A local score is admissible only when the scoring method, codomain, polarity, characteristic basis, comparability basis, and use boundary are disclosed through the governing scoring or comparator pattern. Without that, keep the result as report-only or return to `ModularityVectorLite`.

#### C.31:4.9 - Lowering and currentness conditions

Lower or reopen a `ModularityVectorLite`, `ModularityCharacteristicCard`, or report-only proxy when any of these conditions changes the characteristic use:

- proxy audit worsens, such as more integration failures, workarounds, source-return events, stale evidence reuse, or bounded exceptions;
- measurement basis, comparability basis, scoring method, codomain, polarity, unit policy, or declared characteristic basis changes;
- evidence relation, evidence-provenance relation, source relation, evidence-claim-absent reason, or source-return condition changes;
- described holon, bounded context, architecture claim, structure kind, characteristic head, or repair direction changes;
- a report-only proxy is used for comparison, selection, publication, assurance, benchmark, causal-use, cross-case reuse, decision, procurement, or architecture scale-preference;
- `C.31.RSA`, `C.31.ASAP`, `C.16`, `C.25`, `C.29`, `C.30.STRAT`, `A.6.M`, `C.30`, `C.30.ASV`, `A.10`, `B.3`, `A.20`, `A.21`, `G.5`, or `C.11` changes the boundary for the neighboring claim being made.

Admissible repair results are: keep the result report-only, split or rename the characteristic head, update basis or evidence fields, revise the repair direction, change `relatedClaimGovernanceIfClaimed`, lower a score to a local proxy, or stop C.31 use for the beyond-local-repair claim and use the governing pattern.

### C.31:5 - Archetypal Grounding

**Tell.** Modularity is a vector of action-guiding characteristics, not a magic scalar. A good C.31 interpretation says what to repair next.

**Show.** A product architecture can have high interface standardization and still poor substitutability. A software-system architecture can reduce external coupling while increasing hidden data custody. A safety-case architecture can reuse evidence while increasing regulatory bespoke residue. Each case needs a different characteristic and a different repair.

**Show.** A DSM or dependency graph can substantiate a modularity interpretation, but the graph does not by itself say which dependency kind matters, what scale applies, whether the interpretation is comparable, or what action follows.

Holon and episteme: architecture and modules are selected structures of described holons; the described holon may be an admitted system, organization-as-system, episteme, work occurrence, bounded context, discipline, or another admitted holon kind. Publication-family material enters through episteme and publication owners; method descriptions enter as epistemes; method values enter through their method owner and relation slots. C.31 heads, cards, vectors, and report-only proxies are characteristic records, declared-measurement-basis records, comparability-basis records, or report-only records about those structures.

### C.31:6 - Bias-Annotation

| Bias risk | C.31 repair |
| --- | --- |
| Scalar bias | Refuse one modularity score unless scoring method and comparability basis are declared. |
| Measure-first bias | Start with `ModularityVectorLite` and repair direction before C.16-heavy fields. |
| Interface-publication bias | Treat public interfaces as only one possible basis for substantiating substitutability. |
| Proxy bias | Add `ProxyRisk` and `AuditQuestion` to every decision-facing card. |
| Complexity umbrella bias | Keep residual heads claim-scoped and apply scale, RG, or lens governing patterns when those uses are being made. |
| Source-label bias | Treat software, neural-network, chiplet, safety-case, product-line, block, layer, expert, cache, router, and gate labels as source examples until `C.30.STRAT` and the governing pattern recover the FPF characteristic subject, structure, scale, and admissible use. |

### C.31:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| `CC-C31-1` | Ordinary use starts with `ModularityVectorLite`, three characteristics under evaluation at most, observed problem, repair direction, and stop condition. |
| `CC-C31-2` | Each characteristic head under evaluation is classified as `DirectCharacteristic`, `CompositeCharacteristicDescription`, `LensBackedCharacteristic`, `TemporalOrScaleCharacteristic`, `CausalUseSensitiveCharacteristic`, or `ReportOnlyProxy`. |
| `CC-C31-3` | A decision-facing or publication-facing head has `MeasurementHeadMapping`, C.16-compatible fields, and a required evidence relation, evidence-provenance relation, source relation, or explicit evidence-claim-absent reason before it is relied on. |
| `CC-C31-4` | Each characteristic row states at least one repair action or claim named by value-governance assignment. |
| `CC-C31-5` | Report-only proxies state forbidden overread and do not establish beyond-local-repair use. |
| `CC-C31-6` | Proxy-risk and audit-question fields are present for decision-facing cards. |
| `CC-C31-7` | Complexity, residual, and growth heads remain claim-scoped cues; apply C.29, C.31.ASAP when an architecture scale-preference claim is being made, C.27, C.28, C.16, C.25, C.30.ILC, C.31.RSA, G.5, or C.11 when the corresponding claim kind is being made. |
| `CC-C31-8` | No C.31 text treats modularity as a single quality proof, assurance proof, gate result, causal proof, or architecture decision. |
| `CC-C31-9` | Any score discloses scoring method, codomain, polarity, characteristic basis, comparability basis, and use boundary through the governing pattern. |
| `CC-C31-10` | SoTA seeds for DSM, modularity-index, empirical modularity, platform, evidence-reuse, Conway and mirroring, Amdahl, queueing, coordination-overhead, information-hiding, abstraction-leakage, or Goodhart and Campbell proxy-risk sources are converted into pattern-local `G.2` rows before C.31 uses them for practitioner guidance being relied on. |
| `CC-C31-11` | Source labels such as block, layer, expert, cache, router, or gate use `C.30.STRAT` before they become C.31 characteristic subjects, scale cues, repair actions, or proxy-risk rows. |
| `CC-C31-12` | A vector, card, or report-only proxy states a lowering or reopen condition when proxy audit worsens, measurement or comparability basis changes, evidence relation, evidence-provenance relation, or source relation becomes stale, characteristic head changes, or a related governing pattern changes. |

### C.31:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| `ScalarModularityScore` | A single score claims architecture quality. | Replace with `ModularityVectorLite`, disclosed scoring basis and governing pattern, or report-only boundary. |
| `UntypedMeasureList` | A table of heads appears without characteristic, scale, declared measurement basis, or repair action. | Classify heads and create C.16-compatible cards only where the recovered claim needs them. |
| `MeasurementBeforeRepair` | The practitioner is asked for full measurement before one useful move exists. | Start with three characteristics under evaluation and repair direction. |
| `OpenInterfaceEqualsModular` | Interface publication is treated as modularity. | Apply relation repair through A.6.M and characterize only the interface or substitutability head under evaluation. |
| `ComplexityAsOneCharacteristic` | Algorithmic cost, graph-connectivity cost, policy and approval cost, evidence-maintenance cost, and cognitive cost are averaged. | Keep residual heads claim-scoped and apply lens or measurement patterns when those uses are being made. |
| `ProxyBecomesValue` | A report-only proxy becomes a beyond-local-repair claim. | State forbidden use and use the governing pattern before relying on that claim. |

### C.31:9 - Consequences

Benefits:

- Modularity becomes action-guiding without becoming one fake score.
- Cheap repair remains possible before measurement.
- Characteristic, declared-measurement-basis, comparability-basis, proxy-risk, and governing-pattern boundaries are visible.
- DSM, MOSA, platform, product-line, and architecture-operation sources can inform practice without importing their ontology wholesale.

Costs:

- Familiar score language often has to be downgraded to report-only use.
- Cross-case comparison requires additional C.16, C.25, G.2, comparator, evidence, or decision claim.
- Some attractive "complexity" statements are assigned to characteristic named by value, lens, or residual cue rather than becoming a general complexity pattern here.

### C.31:10 - Rationale

C.31 is a characterization pattern because modularity and reusable-structure talk changes engineering action through characteristics: coupling, cohesion, interface variation, substitutability, reuse, evidence reuse, hidden coupling, source-return cost, and residual growth. Those heads are useful only when their subject, scale, declared measurement or comparison basis, false use, and repair action is visible.

The pattern puts `ModularityVectorLite` first to preserve affordability. Many practitioners need to see one relation to repair, one interface grammar to tighten, or one residue to account for. Requiring the full measurement apparatus too early would turn C.31 into a control form and would violate the architecture source invariant: repair succeeds only when one useful admissible action remains.

The pattern rejects a single complexity or modularity score because selected heads are not automatically commensurable. When a local score is genuinely useful, it belongs under disclosed scoring, comparator, characteristic, declared-measurement-basis, and governing-pattern discipline.

### C.31:11 - SoTA-Echoing

| Source or practice | Currentness or lineage use | Adopt and adapt for C.31 | Rejected overread | Practitioner implication |
| --- | --- | --- | --- | --- |
| DSM and dependency-structure practice (`https://dsmweb.org/design-structure-matrix-dsm/`; `https://dsmweb.org/introduction-to-dsm/`) | Mature and still-used architecture-analysis practice for dependency representation, clustering, and compact dependency communication. | Adopt typed dependency analysis as a possible declared measurement or comparison basis for specific C.31 heads such as `InternalCohesionDensity`, `ExternalCouplingDensity`, `InterfaceAlphabetSize`, and `HiddenCouplingDiscoveryRate`. | A dependency matrix is not architecture, proof, complete modularity, assurance, or decision by itself. | A dependency graph helps only after dependency kind, subject, scale, repair direction, and non-admissible use are declared. |
| Cabigiosu and Camuffo, "Measuring Modularity" (`https://doi.org/10.1109/TEM.2016.2614881`) | Published modularity-measurement source used as measure-plurality lineage, not as a universal current scoring rule. | Adopt the result that modularity measures answer different engineering or management questions; adapt it into `Characteristic plurality vs scalar pressure`, `MeasurementHeadMapping`, and proxy-risk fields. | One measure family is not universal modularity adequacy and does not settle architecture quality. | The practitioner asks which characteristic changes action before choosing any measure family. |
| Jung and Simpson modularity indices for DSM-based assessment (`https://pure.psu.edu/en/publications/new-modularity-indices-for-modularity-assessment-and-clustering-o/`) | Product-architecture and DSM-index lineage for index choice, clustering, and assessment variation. | Use as evidence that index choice depends on architecture type, dependency kind, and measure purpose; adapt by requiring characteristic, scale, measurement basis, comparability basis, and forbidden overread. | One modularity index is not FPF architecture quality, architecture adequacy, or decision authority. | Index use requires declared structure, dependency type, scale, and non-admissible overread before publication, comparison, or decision use. |
| MOSA and open systems practice (`https://www.cto.mil/sea/mosa/`; `https://www.cto.mil/wp-content/uploads/2025/03/MOSA-Implementation-Guidebook-27Feb2025-Cleared.pdf`) | Current engineering and acquisition practice family for modular interfaces, conformance, severable components, replacement, and supplier diversity. | Adopt the pressure to make interface standards, conformance, substitutability, and supplier-diversity relations explicit; adapt by applying A.6.M before C.31 characterizes `InterfacePublicness`, `SubstitutabilityWidth`, or related heads, and by applying `G.5` or `C.11` to supplier-set selection or procurement decision use when that use is being made. | `Open`, public, platform, API, conformance, or supplier-diversity label is not modularity, procurement suitability, or a beyond-local-repair claim by itself. | Open-system conformance and substitution claims may change C.31 repair only after the module-interface relation is repaired; procurement and other beyond-local-repair uses require their governing pattern. |
| Platform and product-line engineering practice (`https://tag-app-delivery.cncf.io/fr/whitepapers/platform-eng-maturity-model/`; `https://www.sei.cmu.edu/library/variability-in-software-product-lines/`; `https://arxiv.org/abs/2605.21353`) | Mature product-line variability lineage plus current platform-engineering maturity-model and current SPLE-review cues; used for variability-slot, extension-rule, reuse, and exception-residue characteristic discipline. | Adopt variability slots, extension rules, template records, product-line records, allowed variation, and exception-residue tracking as possible C.31 characteristic subjects or declared measurement bases. | A platform or product-line label is not modularity value, reusable-structure proof, architecture scale-preference evidence, procurement suitability, or decision authority. | The practitioner names which characteristic changes action: interface standardization, module-type reuse, template compression, bespoke residue, exception curve, or the governing pattern for a beyond-local-repair claim being made. |
| Conway and mirroring, information-hiding, effective-interface, and abstraction-leakage lineage | Socio-technical and interface-boundary sources used as holon-architecture lineage, not as software-only ontology. | Adopt declared correspondence across role and enactor structures, work and procedural structures, and module-interface structures; separate explicit interface specification from observed or implicit interface; recover hidden coupling and source-return conditions. | Team boundary, delivery unit, documented interface, or abstraction label is not module boundary, substitutability, modularity quality, or decision by itself. | The practitioner separates team and work structure, explicit interface, implicit dependency, and modularity characteristic before claiming improvement. |
| Amdahl, queueing, and coordination-overhead laws (`https://www.cs.cmu.edu/~18742/papers/Amdahl1967.pdf`; `https://arxiv.org/abs/1306.3302`; `https://arxiv.org/abs/2603.20654`) | Mature mathematical law and queueing lineage plus current extension sources for communication, synchronization, and scalable-workload-fraction limits. | Adopt serial fraction, synchronization, communication overhead, WIP, waiting, bottleneck, and partitionability as possible C.31 defect signals; apply `C.29`, `E.18`, or `C.30.TFS-REL` when mathematical speedup or flow claims are being made. | More modules, teams, services, flow branches, processors, accelerators, or work partitions are not improvement by count. | A module split is evaluated by changed characteristics and bottlenecks, not by decomposition count. |
| Goodhart and Campbell proxy-pressure laws and holon-architecture trade-off discipline | General proxy-risk and trade-off lineage for architecture characteristic use. | Adopt vector and trade-off discipline plus proxy-risk discipline: no single modularity score, reusable share, benchmark, or index establishes value or beyond-local-repair use without the governing pattern for that use. | One declared measure value, benchmark, reusable-share number, or modularity index is not architecture value or decision authority. | The practitioner states which characteristic changes action and which proxy overread is blocked before comparison or decision. |
| Architecture-operation language, with neural-network and software-system discussions as source examples, including the GonzoML architecture-operation intake | Current practitioner-language source for replacement, selection, pruning, distillation, ablation, block substitution, memory or cache placement, gating, routing, and architecture search; not used as a standard. | Adopt operations as recognition cues for structure, relation, flow, scale, or candidate-set repair under consideration; keep block, layer, expert, cache, router, and gate as `C.30.STRAT` source labels until the FPF characteristic subject, relation kind, scale, and admissible use are recovered. | Block, layer, expert, cache, router, gate, benchmark, ablation, pruning, or distillation label is not an FPF characteristic by default. | The operation points to a possible characteristic; it does not name the characteristic until the FPF kind, subject, scale, and admissible use are recovered. |

**Source-currentness front.** Use the table's `Currentness or lineage use` cell as the source-use boundary. A lineage row can explain why a characteristic family matters, but it cannot establish current comparison, procurement, assurance, benchmark, decision, publication, or other beyond-local-repair use without a current source relation under `G.2` or the governing pattern for that use. Refresh the source use when MOSA or acquisition guidance changes, platform or product-line practice changes, DSM or modularity-index practice changes, queueing or coordination-overhead assumptions change, proxy-pressure law is used for a new claimed value relation, or architecture-operation language is used as current practice rather than as source-side recognition language. When refresh changes the source-use relation, update the affected characteristic head, proxy-risk field, audit question, related claim governance, or report-only boundary rather than treating the older source as current by default.

Rows named current, such as MOSA guidance, current platform practice, current scalable-workload extensions, or current architecture-operation corpus material, require source refresh before beyond-local-repair use when the named practice changes. Rows named lineage stay lineage unless a current source relation is explicitly recovered.

Older or local sources may serve as lineage or worked examples only when the row says so. They do not stand in for current competitive source, and they do not make a modularity value admissible for beyond-local-repair use without the governing pattern for that use.


### C.31:12 - Relations

| Pattern | Relation |
| --- | --- |
| `C.30.STRAT` | Recovers source labels such as layer, level, tier, stack, block, expert, cache, router, and gate before C.31 uses any recovered characteristic subject, scale cue, repair action, or proxy-risk row. |
| `A.6.M` | Repairs module-interface relations before C.31 characterizes modularity. |
| `C.31.RSA` | Governs reusable-structure accounting, bespoke residue, and report-only shares. |
| `C.31.ASAP` | Governs architecture scale-preference claims after C.31 names the scale-sensitive characteristic, scale variable or window, and repair direction. |
| `C.16`, `A.17`, `A.18`, `A.19` | Govern characteristic, scale, coordinate, score, unit, comparability, and measurement admissibility. |
| `C.25` | Governs broader quality-family Q-Bundles when modularity is used in a quality claim. |
| `C.30` and `C.30.ASV` | Govern architecture claims and structural views that supply C.31 subjects. |
| `C.33`, `C.34`, and `C.35` | Govern captured-structure adequacy, lost-structure adequacy, preservation adequacy, correspondence adequacy, generated-carrier adequacy, or discovered-carrier adequacy around modularity and reusable-structure material. C.31 still owns modularity, reuse, proxy-risk, report-only, and characteristic use. |
| `C.30.ILC` | Governs cross-scope residual and frustration recognition when architecture move triage is being made. |
| `C.29` | Governs mathematical-lens use such as compression, RG, epiplexity, or graph-lens transfer. |
| `C.27`, `C.18.1`, `C.19.1` | Govern temporal and set-dynamic claims such as learning transfer, exception slope, and scale-window movement. |
| `C.28` | Governs causal-use claims. |
| `A.10`, `B.3`, `A.20`, `A.21` | Govern evidence, assurance, gate, safety, and release claims. |
| `C.32.P2S` | Uses C.31 modularity and reusable-structure characteristics when problem pressure must continue into candidate synthesis, decision, realization, and actual-structure feedback; C.31 still governs only characteristic and report-only modularity use. |
| `G.2`, `G.5`, `C.11` | Govern SoTA basis, set-return selection, and local decision claims. Candidate-generation or architecture-synthesis claims stay outside C.31 unless `G.5`, `C.11`, or a named architecture-synthesis governing pattern governs that claim; C.31 records only modularity or reusable-structure characteristic use and report-only boundaries. |

### C.31:End

