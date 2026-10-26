## C.31 - Modularity and Reusable Structure Characteristics

> **Type:** Characterization pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.31:1 - Problem frame

Use this pattern when modularity or reusable-structure language is doing work in an architecture discussion and the practitioner needs to know which few characteristics matter, what repair follows, and whether any measurement or comparison is admissible.

First identify the few characteristics that matter to the architecture question, the observed difficulty and any needed repair. An adequate ordinary account can finish; `ModularityVectorLite` offers a compact way to retain it:

```text
ModularityVectorLite:
  describedHolonRef:
  architectureQuestion:
  intendedArchitectureUse:
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?:
  architectureClaimRef?:
  selectedStructureRefs:
  structureKindRefs:
  threeLiveCharacteristicsAtMost:
  observedProblem:
  repairDirection:
  relatedClaimPatternLocatorsIfClaimed:
  nonAdmissibleOverread?:
  stopCondition:
```

For the first diagnostic move, select at most three characteristics and connect them to the observed problem and any warranted repair. This limits the first inquiry, not the eventual analysis. A clearly bounded report-only proxy can be a sufficient result.

Claim-use boundary: before relying on a characteristic for comparison, causal explanation, assurance, selection or another further use, establish the grounds required by that claim. Making a qualified local account available to an audience preserves its limits; publication alone does not turn it into a measurement or a selection result. Add only the information on which the receiving use depends.

What goes wrong if C.31 is missed: "modular" becomes a binary label; a single modularity score hides incompatible characteristics; interface publication is confused with substitutability; internal cohesion is improved while evidence reuse gets worse; bespoke residue moves from templates into work or assurance; and complexity language becomes a commensurable score without a declared characteristic, scale, measurement basis, comparison basis, or admissible-use boundary.

What C.31 buys in practice: the practitioner can choose the modularity characteristic that matters, identify a warranted repair, and determine what further measurement, evidence, causal, scale, selection or accounting grounds the intended use requires.

Not this pattern when the question under repair is only source-label recovery, module-interface relation repair, reusable-structure accounting, general measurement admissibility, quality-family claim, architecture scale-preference claim, mathematical-lens use, candidate architecture synthesis, or selection. Use `C.30.STRAT`, `A.6.M`, `C.31.RSA`, `C.16`, `C.25`, `C.31.ASAP`, `C.29`, `C.32`, `G.5`, or `C.11` as appropriate: `C.32` governs candidate architecture synthesis, `G.5` selected-set result declaration, and `C.11` local choice.

### C.31:2 - Problem

Architecture work often asks for more modularity, better reuse, lower coupling, more explicit interfaces, cleaner allocation, or less bespoke residue. These phrases point to real engineering work, but they do not name one scalar property.

Modularity can improve along one characteristic while worsening another. A design can reduce external coupling and increase interface alphabet size. A platform can standardize interfaces and create unhelpful rigidity. Evidence reuse can improve while functional-to-module allocation remains tangled. A report can show a high reuse share while hiding source-return work or residual uncertainty.

C.31 turns modularity talk into a small characteristic vector plus repair direction. It does not promise that every characteristic is measurable now, comparable across cases, causal, admissible for decision use, or evidence-backed.

### C.31:3 - Forces

| Force | Tension |
| --- | --- |
| Fast architecture repair vs measurement admissibility | Practitioners often need the next modularity move before a full measurement template exists. |
| Characteristic plurality vs scalar pressure | Different modularity interpretations have different subjects, scales, evidence, declared measurement or comparison basis, subject-pattern needs, and risks; one score hides that plurality. |
| Useful proxy vs proxy substitution | A cheap share, count, or graph interpretation can guide local repair, but it may become a false quality, evidence, or decision claim. |
| Module-interface view vs broader structure | Modularity can involve functions, flows, control, work, evidence, data, placement, or scale, not only modules. |
| Local repair vs cross-case use | A local diagnosis can stop at report-only use. Cross-case comparison needs the actual bearers, characteristic and comparison rule under C.16, with C.25 when a broader quality claim is made. G.5 governs a selected-set declaration and C.11 a local choice. E.24.PUB governs publication and audience availability; E.17 applies when a source-backed face and return are needed. |
| Complexity pressure vs complexity ontology | Residual pressure and growth signals are useful, but complexity is not one commensurable architecture characteristic. |

### C.31:4 - Solution

C.31 defines and constrains modularity and reusable-structure characteristic assertions as C.16-compatible characteristic heads, composite descriptions, lens-backed characteristic interpretations, temporal or scale-sensitive characteristic interpretations, causal-use-sensitive characteristic interpretations, or report-only proxies. It starts from action guidance and adds fields for beyond-local-repair use only when a use being made requires them.

#### C.31:4.1 - Ordinary output: `ModularityVectorLite`

The ordinary output is a small account of the characteristics that explain the difficulty and what follows from them. `ModularityVectorLite` can retain it. Its first diagnostic pass names at most three characteristics; later work can extend the account when the question requires it.

```text
ModularityVectorLite:
  describedHolonRef:
  architectureQuestion:
  intendedArchitectureUse:
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?:
  architectureClaimRef?:
  selectedStructureRefs:
  structureKindRefs:
  threeLiveCharacteristicsAtMost:
    - characteristicRef:
      characteristicScaleRef?:
      evidenceRefs?:
      comparisonBasisRef?:
      currentCue:
      repairDirection:
      claimUseClass:
      forbiddenOverread?:
  observedProblem:
  relatedClaimPatternLocatorsIfClaimed:
  stopCondition:
```

The account is complete enough when it answers the architecture question or identifies the next warranted repair. State a blocked inference when a plausible intended reader could make it here and the distinction matters. `relatedClaimPatternLocatorsIfClaimed` locates a governing pattern; it supplies neither the claim nor its grounds. Further use needs the actual subject, assertion and applicable rule. Exact rule identity is required only under section 4.3. Architecture scale-preference claims use `C.31.ASAP`.

#### C.31:4.1a - Filled `ModularityVectorLite`

```text
ModularityVectorLite:
  describedHolonRef: ProductPlatform@FieldPumpFamily
  architectureQuestion: which structural repair would reduce field-replacement and certification burden?
  intendedArchitectureUse: choose the next modularity repair for field service and procurement
  claimScopeRef?: field-service and procurement architecture claims
  qualificationWindowRef?: 2026Q2
  architectureClaimRef?: ArchitectureClaim@PumpControllerPlatform
  selectedStructureRefs: PumpControllerModuleInterfaceStructure, PumpControllerEvidencePackageStructure
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
  relatedClaimPatternLocatorsIfClaimed: A.6.M for the module-interface relation; C.31.RSA if report-only share becomes reusable-structure accounting; A.10 or B.3 only if an exact evidence-use or assurance-use assertion is being made.
  stopCondition: stop at local repair until measurement basis, comparability basis, and any selection or assurance use are declared under their subject patterns.
```

Near miss: a high interface-standardization count alone is not a C.31 improvement. If field-service work, source-return events, or variant-specific evidence increase, the vector records that proxy divergence and returns to repair rather than treating the count as architecture quality.

#### C.31:4.2 - Characteristic classes

Identify the classes that apply to the characteristic use. They distinguish requirements and can overlap: a measured temporal relationship used causally needs its measurement, time-window and causal grounds.

| Class | Use | Boundary |
| --- | --- | --- |
| `DirectCharacteristic` | A C.16-governed characteristic can be named with subject, scale, unit or unitless interpretation, declared measurement basis, comparability basis, and repair action. | It is not automatically a score or decision selector. |
| `CompositeCharacteristicDescription` | The head is a bundle or description with sub-slots, such as function-module alignment or flow-boundary alignment. | Do not pretend the bundle is one raw measure. |
| `LensBackedCharacteristic` | The head depends on a model description or mathematical lens, such as compression or RG or coarsening lens. | Apply C.29 for lens use that changes action. |
| `TemporalOrScaleCharacteristic` | The head depends on time window, repeated instance, scale variable, aggregation scope, or source-return condition. | Apply `C.31.ASAP` for architecture scale preference, `C.27` for temporal adequacy, and `C.18.1` or `C.19.1` when scale-law or general BLP preference claims are being made. |
| `CausalUseSensitiveCharacteristic` | The interpretation is used to claim effect or intervention success. | Apply C.28 before relying on the claim causally. |
| `ReportOnlyProxy` | The interpretation is only a local diagnostic or communication aid. | Preserve its stated scope and relevant limits; use the applicable subject rule before stronger reliance. |

In C.31, `declared basis` and `comparability basis` name C.16-compatible measurement or comparison fields. They are not generic reason words and are not substitutes for evidence, assurance, cause, source, decision, or architecture-description relations.

#### C.31:4.3 - Measurement-head mapping

When a proposed comparison or decision relies on a measurement head whose meaning or admissible operations remain unresolved, recover the following mapping. Reuse an adequate existing account; the form is optional.

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
  commonFalseUse?:
  nonAdmissibleUse?:
  repairAction:
  relationFunctionClaimRef?:     # only when this use depends on exact rule identity
  authoritySourceRef?:           # only when a non-pattern source carries relevant authority
```

Use an ordinary PatternID to locate the rule. Under E.10 L-EPI-PUB, relationFunctionClaimRef identifies the defining or constraining ClaimGraph only when interpretation, comparison, migration, publication or reuse depends on that exact rule identity. It is not a demand to establish a separate relation-function individual. When an external standard, policy or other non-pattern source carries the relevant authority, use authoritySourceRef for that source instead.

For example, an ordinary InterfaceStandardizationShare account states its subject, the counted interface population, conformance specification, ratio Scale, source/test basis and limitations. It needs no extra rule-identity claim merely to describe that share. If a comparison combines two editions that count partial conformance differently, cite the exact defining predicates through relationFunctionClaimRef before treating their shares as comparable. The comparison still needs its actual measurement and evidence basis; citing the predicate supplies neither test results nor assurance.

This mapping prepares a C.16-compatible measurement or a report-only interpretation; it does not supply observations or a measurement procedure. Recover the evidence or source relations that the actual claim relies on. Use `evidenceClaimAbsentBecause` only when the receiving use needs an explanation of that absence; a local cue needs no invented evidence claim. Sharing a bounded account preserves its existing qualification.

#### C.31:4.4 - C.31 characteristic card

Use the full card when retaining or comparing the characteristic requires these distinctions. An existing adequate account can carry them:

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
  nonAdmissibleUse?:
  repairAction:
  relatedClaimPatternLocators:
  relationFunctionClaimRef?:     # same rule-identity condition as MeasurementHeadMapping
  authoritySourceRef?:           # relevant non-pattern authority, when used
```

A measurement or comparison states the characteristic, bearer, scale, unit interpretation, measurement or comparison basis, and evidence on which it relies under C.16. Retain relevant limits and any warranted repair. When source material is used as evidence, identify that source relation. A checklist, dashboard label or inherited score supplies no missing basis. The optional card organizes this content; it does not make a qualitative diagnostic cue a measurement.

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
| `FlowModuleBoundaryAlignmentCharacteristic` | Flow topology crosses declared interfaces rather than hidden channels. | vector, ordinal, or bundle description | transformation-flow structure refs and interface refs | flows bypass declared module boundaries | expose crossing, revise interface, or apply C.30.TFS-REL for the bounded architecture use of the selected transformation-flow structure | publication or assurance claim about that architecture use |
| `ControlStructureSeparationCharacteristic` | Control responsibilities, rates, and boundaries are explicit enough for the architecture move. | ordinal or vector | LCA or control description and temporal adequacy basis | control relation is hidden inside module label | apply C.30.LCA, C.27, A.3.3, or B.3 when a control, temporal, dynamics, or assurance claim kind is being made | stability, assurance, or gate use |
| `HiddenCouplingDiscoveryRate` | Hidden dependencies discovered after integration or change. | rate | defect and change records | dependencies appear late | expose side channel, revise interface spec, add sentinel, or reopen boundary | integration risk, repeated release, or assurance claim |
| `CrossBoundaryChangeReach` | How many modules, views, or work items a local change touches. | distribution | change-impact records | local change travels farther than claimed | split relation, add interface grammar, revise allocation, or source return | release, decision, or comparison claim |
| `WorkRepeatabilityShare` | Delivery, operation, or test work under repeatable method descriptions. | ratio | work records and method descriptions | work repeats as bespoke effort | describe the repeatable Method in a `MethodDescription` under A.3.2 or accept exception | work planning, evidence reuse, or scale use |
| `EvidenceReuseShare` | Evidence package items reused across instances or contexts. | ratio | evidence graph and validity context | evidence is recreated or mis-scoped | move repeated evidence into reusable evidence or assurance package | certification, safety-case, or assurance claim |
| `RegulatoryBespokeResidue` | One-off regulatory or acceptance content not covered by reusable structures. | ratio or ordinal | safety, approval, or regulatory records | each instance needs new regulatory argument | isolate residue, add reusable evidence package, or keep bounded exception | safety case, approval, or publication claim |
| `LearningTransferCoefficient` | Improvement transfer from one instance or run to subsequent instances. | slope or elasticity | repeated work data and learning curve records | improvement claim hides time or causal assumptions | apply C.27 for temporal adequacy and C.28 for causal use | causal, benchmark, or scale-preference use |
| `BespokeResidueShare` | Share of structure not covered by reusable templates or rules. | report-only share unless C.16 measurement basis is declared | RSA description and exception register | residue is hidden under reuse score | use C.31.RSA and source-return condition | accounting, comparison, or decision claim |
| `RGFlowStability` | Stability of characteristic vector across declared coarse-graining scopes. | vector or ordinal | declared multi-scope architecture graphs | coarse-graining hides lower-scope hazards | apply C.29 for lens use and C.31.ASAP when an architecture scale-preference claim is being made | RG, scale, or lens transfer use |
| `ExceptionCurveSlope` | Change in one-off exceptions over a scale variable. | slope | exception records against scale variable | exceptions grow with scale | apply C.31.ASAP or accept bounded exception | scale preference, publication, or decision claim |

#### C.31:4.6 - Claim-scoped residual heads

C.31 uses residual heads only as qualitative repair cues. These heads do not create one complexity characteristic.

| Head | Meaning | Related claim pattern locator and assertion requirement | Risk | Repair direction |
| --- | --- | --- | --- | --- |
| ComplexityGrowthPressure | Pressure to add, split, mediate, or stabilize a declared aggregation scope, interface grammar, control relation, evidence scope, work-method scope, abstraction scope, or source-return condition. | C.30.ILC, C.31.ASAP when an architecture scale-preference claim is being made, G.5, C.11 | treating more apparatus as progress | name the pressure and the repair direction; use set-return or decision patterns when the corresponding claim is being made |
| `FrustrationResidual` | Persistent cross-scope residual after attempted local repair or a stated reason for its insufficiency. | `C.30.ILC`, C.29-local cross-scope lens claim | turning a lens-backed interpretation into proof | keep as residual cue or apply C.29 or C.30.ILC |
| `ConflictResidualSlope` | Residual grows or shrinks over declared scale variable, scale window, or coarse-graining scale. | `C.31.ASAP`, `C.29`, `C.27`, `C.18.1`, `C.19.1` | treating two points as universal law | declare window, lens-use boundary, and measurement basis or stop at report-only |
| `DeclaredScopeAdditionCost` | Added work, evidence, change-policy, latency, observability, accountability, or interface cost from a new declared aggregation or control scope. | `C.16`, `C.31`, `C.30.LCA` | ignoring the cost of added structure | identify cost bearer and apply the measurement pattern if used for comparison |
| `BespokeResidueGrowth` | One-off exceptions grow with deployment spread, regulation, or project repetition. | `C.31.RSA`, `C.31.ASAP` when an architecture scale-preference claim is being made | assuming all bespoke work is bad | split useful exception from repairable residue |
| `InterfaceAlphabetGrowth` | Interface variants grow faster than reuse, substitutability, or integration payoff. | `A.6.M`, `C.31` | premature standardization | add platform grammar, split context, or accept bounded variation |
| `SourceReturnCost` | Frequency or cost of returning from a compressed, indexed, coarse, extracted, or accounting view to source-side structure records. | `C.29`, source-return discipline, `A.10` | over-compression | add source-return condition or reduce compression |
| `ControlNestingDepthRisk` | Nested control relations create latency, accountability, observability, stability, or assurance cost. | `C.30.LCA`, `C.27`, `B.3`, `A.3.3` | LCA-as-proof | apply control, temporal, assurance, or dynamics subject patterns when the corresponding claim is being made |

#### C.31:4.7 - Proxy-risk discipline

When a decision relies on a proxy, identify how it could diverge from the intended value and how that divergence would be detected. The card can retain these as `proxyRisk` and `auditQuestion`. An observed divergence blocks the unsupported value inference; the measured proxy can remain a valid report within its scope.

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
- described holon, architecture question or intended use, ClaimScope or qualification window, architecture claim, structure kind, characteristic head, or repair direction changes;
- a report-only proxy is used to support a stronger comparison, assurance, causal, selection or scale-preference claim; simply publishing its qualified local meaning does not create that stronger use;
- `C.31.RSA`, `C.31.ASAP`, `C.16`, `C.25`, `C.29`, `C.30.STRAT`, `A.6.M`, `C.30`, `C.30.ASV`, `A.10`, `B.3`, `A.20`, `A.21`, `G.5`, or `C.11` changes the boundary for the neighboring claim being made.

Admissible repair results are: keep the result report-only, split or rename the characteristic head, update basis or evidence fields, revise the repair direction, change `relatedClaimPatternLocatorsIfClaimed`, lower a score to a local proxy, or stop the unsupported use and establish the required subject claim under its applicable rule.

### C.31:5 - Archetypal Grounding

**Tell.** Modularity is a vector of action-guiding characteristics, not a magic scalar. A good C.31 interpretation says what to repair next.

**Show.** A product architecture can have high interface standardization and still poor substitutability. A software-system architecture can reduce external coupling while increasing hidden data custody. A safety-case architecture can reuse evidence while increasing regulatory bespoke residue. Each case needs a different characteristic and a different repair.

**Show.** A DSM or dependency graph can substantiate a modularity interpretation, but the graph does not by itself say which dependency kind matters, what scale applies, whether the interpretation is comparable, or what action follows.

Holon and episteme: C.31 characterizes selected module-interface and other architecture-relevant structures of described holons for named architecture questions and uses; the described holon may be an admitted system, organization-as-system, episteme, work occurrence, discipline, or another admitted holon kind. Publication-family material uses the episteme and publication patterns. A MethodDescription is an episteme; a Method uses A.3.1, and any relation asserted for it uses the pattern that defines that relation. C.31 heads, cards, vectors, and report-only proxies are characteristic records, declared-measurement-basis records, comparability-basis records, or report-only records about those structures.

### C.31:6 - Bias-Annotation

| Bias risk | C.31 repair |
| --- | --- |
| Scalar bias | Refuse one modularity score unless scoring method and comparability basis are declared. |
| Measure-first bias | Identify the useful characteristic question and warranted repair; use measurement when its result can answer that question. |
| Interface-publication bias | Treat public interfaces as only one possible basis for substantiating substitutability. |
| Proxy bias | Identify and check the divergence that matters when a decision relies on a proxy. |
| Complexity umbrella bias | Keep residual heads claim-scoped and apply scale, RG, or lens subject patterns when those uses are being made. |
| Source-label bias | Preserve an already clear source meaning. Use `C.30.STRAT` when a label still hides the characteristic subject, structure, scale or admissible use. |

### C.31:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| `CC-C31-1` | The first diagnostic pass identifies at most three relevant characteristics, the observed problem and any warranted repair. An adequate ordinary account can finish; later analysis may extend it. |
| `CC-C31-2` | Each characteristic head under evaluation is classified as `DirectCharacteristic`, `CompositeCharacteristicDescription`, `LensBackedCharacteristic`, `TemporalOrScaleCharacteristic`, `CausalUseSensitiveCharacteristic`, or `ReportOnlyProxy`. |
| `CC-C31-3` | A measurement or comparison has the C.16 meaning, operations and supporting basis required by its actual use. Recover an unresolved measurement head through section 4.3; an adequate existing account needs no new form. Exact rule-identity dependence requires relationFunctionClaimRef; an ordinary locator does not. Non-pattern authority uses authoritySourceRef under E.10. |
| `CC-C31-4` | Each selected characteristic contributes to the architecture answer or a warranted repair. Any further claim retains its subject and governing rule. |
| `CC-C31-5` | Report-only proxies retain their scope and action-changing limits. Stronger reliance requires its own grounds; publishing the bounded report does not enlarge them. |
| `CC-C31-6` | A decision that relies on a proxy addresses the relevant divergence risk and how it is checked. |
| `CC-C31-7` | Complexity, residual, and growth heads remain claim-scoped cues; apply C.29, C.31.ASAP when an architecture scale-preference claim is being made, C.27, C.28, C.16, C.25, C.30.ILC, C.31.RSA, G.5, or C.11 when the corresponding claim kind is being made. |
| `CC-C31-8` | No C.31 text treats modularity as a single quality proof, assurance proof, gate result, causal proof, or architecture decision. |
| `CC-C31-9` | Any score discloses scoring method, codomain, polarity, characteristic basis, comparability basis, and use boundary through the subject pattern. |
| `CC-C31-10` | A source-dependent use retains the source contribution, assumptions and limits needed by its claim. Use G.2 when a current comparative SoTA basis is needed; a familiar method or bounded historical result does not require a new source row merely to be used. |
| `CC-C31-11` | Source labels retain their clear local meaning. Use C.30.STRAT only for unresolved stratification or structure meaning that changes the characteristic use. |
| `CC-C31-12` | A vector, card, or report-only proxy states a lowering or reopen condition when proxy audit worsens, measurement or comparability basis changes, evidence relation, evidence-provenance relation, or source relation becomes stale, characteristic head changes, or a related subject pattern changes. |

### C.31:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| `ScalarModularityScore` | A single score claims architecture quality. | Replace with `ModularityVectorLite`, disclosed scoring basis and subject pattern, or report-only boundary. |
| `UntypedMeasureList` | A table of heads appears without characteristic, scale, declared measurement basis, or repair action. | Classify heads and create C.16-compatible cards only where the recovered claim needs them. |
| `MeasurementBeforeRepair` | The practitioner is asked for full measurement before one useful move exists. | Start with at most three characteristics under evaluation and repair direction. |
| `OpenInterfaceEqualsModular` | Interface publication is treated as modularity. | Apply relation repair through A.6.M and characterize only the interface or substitutability head under evaluation. |
| `ComplexityAsOneCharacteristic` | Algorithmic cost, graph-connectivity cost, policy and approval cost, evidence-maintenance cost, and cognitive cost are averaged. | Keep residual heads claim-scoped and apply lens or measurement patterns when those uses are being made. |
| `ProxyBecomesValue` | A report-only proxy becomes a beyond-local-repair claim. | State forbidden use and use the subject pattern before relying on that claim. |

### C.31:9 - Consequences

Benefits:

- Modularity becomes action-guiding without becoming one fake score.
- Cheap repair remains possible before measurement.
- Characteristic, declared-measurement-basis, comparability-basis, proxy-risk, and subject-pattern boundaries are visible.
- DSM, MOSA, platform, product-line, and architecture-operation sources can inform practice without importing their ontology wholesale.

Costs:

- Familiar score language often has to be downgraded to report-only use.
- Cross-case comparison needs the applicable measurement and comparison grounds, with quality, source, evidence or decision work when that particular claim requires it.
- Some attractive "complexity" statements need an exact characteristic, a lens-backed interpretation, or a residual cue.

### C.31:10 - Rationale

C.31 is a characterization pattern because modularity and reusable-structure talk changes engineering action through characteristics: coupling, cohesion, interface variation, substitutability, reuse, evidence reuse, hidden coupling, source-return cost, and residual growth. Their use depends on recovering the subject and relevant structural relation, then adding scale, measurement or comparison grounds only for the claims that need them. The account should explain the answer or warranted repair and any action-changing limit.

The small first inquiry preserves affordability. A practitioner may need one relation to repair, one interface grammar to tighten or one residue to account for. These distinctions determine whether measurement could improve the next move; a complete diagnostic answer can stop without a full card.

The pattern rejects a single complexity or modularity score because selected heads are not automatically commensurable. When a local score is genuinely useful, it belongs under disclosed scoring, comparator, characteristic, declared-measurement-basis, and subject-pattern discipline.

### C.31:11 - SoTA-Echoing

| Source or practice | Currentness or lineage use | Adopt and adapt for C.31 | Rejected overread | Practitioner implication |
| --- | --- | --- | --- | --- |
| DSM and dependency-structure practice (`https://dsmweb.org/design-structure-matrix-dsm/`; `https://dsmweb.org/introduction-to-dsm/`) | Architecture-analysis practice for dependency representation, clustering, and compact dependency communication. | Adopt typed dependency analysis as a possible declared measurement or comparison basis for specific C.31 heads such as `InternalCohesionDensity`, `ExternalCouplingDensity`, `InterfaceAlphabetSize`, and `HiddenCouplingDiscoveryRate`. | A dependency matrix is not architecture, proof, complete modularity, assurance, or decision by itself. | Use the dependency kind and subject to select the architecture question; add a scale or comparison basis when making that measurement or comparison. |
| Cabigiosu and Camuffo, "Measuring Modularity" (`https://doi.org/10.1109/TEM.2016.2614881`) | Published modularity-measurement source used as measure-plurality lineage, not as a universal current scoring rule. | Adopt the result that modularity measures answer different engineering or management questions; adapt it into `Characteristic plurality vs scalar pressure`, `MeasurementHeadMapping`, and proxy-risk fields. | One measure family is not universal modularity adequacy and does not settle architecture quality. | The practitioner asks which characteristic changes action before choosing any measure family. |
| Jung and Simpson modularity indices for DSM-based assessment (`https://pure.psu.edu/en/publications/new-modularity-indices-for-modularity-assessment-and-clustering-o/`) | Product-architecture and DSM-index lineage for index choice, clustering, and assessment variation. | Use as evidence that index choice depends on architecture type, dependency kind, and measure purpose; adapt by requiring the characteristic, scale, measurement and comparability basis, with relevant limits. | One modularity index is not FPF architecture quality, architecture adequacy, or decision authority. | An index used for comparison or decision needs its declared structure, dependency type, scale and relevant limits. A published account preserves that qualification. |
| MOSA and open systems practice (`https://www.cto.mil/sea/mosa/`; `https://www.cto.mil/wp-content/uploads/2025/03/MOSA-Implementation-Guidebook-27Feb2025-Cleared.pdf`) | Engineering and acquisition practice family for modular interfaces, conformance, severable components, replacement, and supplier diversity. | Adopt the pressure to make interface standards, conformance, substitutability, and supplier-diversity relations explicit; adapt by applying A.6.M when the module or interface claim needed by `InterfacePublicness`, `SubstitutabilityWidth`, or another head remains unresolved, and by applying `G.5` or `C.11` to supplier-set selection or procurement decision use when that use is being made. | `Open`, public, platform, API, conformance, or supplier-diversity label is not modularity, procurement suitability, or a beyond-local-repair claim by itself. | Open-system conformance and substitution claims inform C.31 once their relevant module-interface meaning and basis are recoverable; procurement and other beyond-local-repair uses require their subject pattern. |
| Platform and product-line engineering practice (`https://tag-app-delivery.cncf.io/fr/whitepapers/platform-eng-maturity-model/`; `https://www.sei.cmu.edu/library/variability-in-software-product-lines/`; `https://arxiv.org/abs/2605.21353`) | Product-line variability lineage, platform-engineering maturity-model and SPLE-review cues; used for variability-slot, extension-rule, reuse, and exception-residue characteristic discipline. | Adopt variability slots, extension rules, template records, product-line records, allowed variation, and exception-residue tracking as possible C.31 characteristic subjects or declared measurement bases. | A platform or product-line label is not modularity value, reusable-structure proof, architecture scale-preference evidence, procurement suitability, or decision authority. | The practitioner names which characteristic changes action: interface standardization, module-type reuse, template compression, bespoke residue, exception curve, or the subject pattern for a beyond-local-repair claim being made. |
| Conway and mirroring, information-hiding, effective-interface, and abstraction-leakage lineage | Socio-technical and interface-boundary sources used as holon-architecture lineage, not as software-only ontology. | Keep the source meaning in ordinary language. State only the correspondence claims that obtain: organization Systems and relations; system-role classifications and assignments; enactor relations; division of work; and dated Work whose exact actual performers are recovered through A.13 and which A.15.1 independently admits. Add assignment and F.6 refs to a reusable record only when it or the receiving use expressly represents precise assignment-bound attribution; keep module-interface structures separate. Infer none from the lineage phrase. | Team boundary, delivery unit, documented interface, assignment, or abstraction label is not module boundary, Work occurrence, substitutability, modularity quality, or decision by itself. | The practitioner separates organization relations, work or procedure organization, any Work chain, explicit interface, implicit dependency, and modularity characteristic before claiming improvement. |
| Amdahl, queueing, and coordination-overhead laws (`https://www.cs.cmu.edu/~18742/papers/Amdahl1967.pdf`; `https://arxiv.org/abs/1306.3302`; `https://arxiv.org/abs/2603.20654`) | Mathematical law and queueing lineage plus extension sources for communication, synchronization, and scalable-workload-fraction limits. | Adopt serial fraction, synchronization, communication overhead, WIP, waiting, bottleneck, and partitionability as possible C.31 defect signals; apply `C.29`, `E.18`, or `C.30.TFS-REL` when mathematical speedup or flow claims are being made. | More modules, teams, services, flow branches, processors, accelerators, or work partitions are not improvement by count. | A module split is evaluated by changed characteristics and bottlenecks, not by decomposition count. |
| Goodhart and Campbell proxy-pressure laws and holon-architecture trade-off discipline | General proxy-risk and trade-off lineage for architecture characteristic use. | Adopt vector and trade-off discipline plus proxy-risk discipline: no single modularity score, reusable share, benchmark, or index establishes value or beyond-local-repair use without the subject pattern for that use. | One declared measure value, benchmark, reusable-share number, or modularity index is not architecture value or decision authority. | The practitioner identifies the characteristic and checks the proxy-to-value inference on which a comparison or decision relies. |
| Architecture-operation language, with neural-network and software-system discussions as source examples, including the GonzoML architecture-operation intake | Practitioner-language source for replacement, selection, pruning, distillation, ablation, block substitution, memory or cache placement, gating, routing, and architecture search; not used as a standard. | Adopt operations as recognition cues for structure, relation, flow, scale, or candidate-set repair under consideration; keep the local meaning of block, layer, expert, cache, router or gate and use `C.30.STRAT` when that meaning still obscures the characteristic use. | Block, layer, expert, cache, router, gate, benchmark, ablation, pruning, or distillation label is not an FPF characteristic by default. | The operation points to a possible characteristic. Recover its subject, interpretation and admissible use; establish a scale when measurement requires one. |

**Source-use and refresh.** A source row identifies a contribution and its limits. A historical method or result can support a use within its established premises; it does not establish the current comparative standing of an approach. When the question depends on present acquisition rules, a changed interface standard or newer comparative evidence, recover that basis through G.2 or the applicable source rule before relying on it. A source citation supplies no missing measurement, conformance test or decision premise.

Reopen only the dependent characteristic, comparison or repair when its source meaning, assumptions or applicable rule changes. For example, a changed substitution specification can alter InterfaceStandardizationShare and SubstitutabilityWidth while leaving an earlier counted population intact. A queueing-model change reopens the dependent bottleneck inference; it does not erase an independently observed dependency. Preserve unchanged source uses and bounded historical results.

### C.31:12 - Relations

| Pattern | Relation |
| --- | --- |
| `C.30.STRAT` | Recovers unresolved stratification or structure meanings in source labels when those distinctions change the C.31 use. |
| `A.6.M` | Repairs a module-interface claim when its meaning or required substitution conditions remain unresolved. |
| `C.31.RSA` | Governs reusable-structure accounting, bespoke residue, and report-only shares. |
| `C.31.ASAP` | Governs architecture scale-preference claims after C.31 names the scale-sensitive characteristic, scale variable or window, and repair direction. |
| `C.16`, `A.17`, `A.18`, `A.19` | Govern characteristic, scale, coordinate, score, unit, comparability, and measurement admissibility. |
| `C.25` | Governs broader quality-family Q-Bundles when modularity is used in a quality claim. |
| `C.30` and `C.30.ASV` | Govern architecture claims and structural views that supply C.31 subjects. |
| `C.33`, `C.34`, and `C.35` | Use C.33 and C.34 for captured-structure, lost-structure, preservation, and correspondence adequacy around modularity and reusable-structure material. Use C.35 to recover the kind of a generated or discovered result and assess its adequacy for the next architecture use. C.31 remains the pattern for modularity, reuse, proxy-risk, report-only, and characteristic use. |
| `C.30.ILC` | Governs cross-scope residual and frustration recognition when architecture move triage is being made. |
| `C.29` | Governs mathematical-lens use such as compression, RG, epiplexity, or graph-lens transfer. |
| `C.27`, `C.18.1`, `C.19.1` | C.27 governs temporal-claim adequacy, C.18.1 scale-law lens binding, and C.19.1 scale-based comparison, preference, or waiver. For temporal or set-dynamic claims involving learning transfer, exception slope, or scale-window movement, use the applicable branch. |
| `C.28` | Governs causal-use claims. |
| `A.10`, `B.3`, `A.20`, `A.21` | Govern evidence provenance and reliance, named assurance claims, internal-constraint results, and named gate decisions, respectively. Safety and release claims use their direct domain patterns. |
| `C.32.P2S` | Uses C.31 modularity and reusable-structure characteristics when problem pressure must continue into candidate synthesis, decision, realization, and actual-structure feedback; C.31 still governs only characteristic and report-only modularity use. |
| `G.2`, `C.32`, `G.5`, `C.11` | Define SoTA-basis, candidate architecture synthesis, selected-set declaration, and local-decision predicates, respectively. Candidate-generation or architecture-synthesis claims use the Method and conditions in C.32 or another applicable synthesis pattern. C.31 records only modularity or reusable-structure characteristic use and report-only boundaries. |

### C.31:End
