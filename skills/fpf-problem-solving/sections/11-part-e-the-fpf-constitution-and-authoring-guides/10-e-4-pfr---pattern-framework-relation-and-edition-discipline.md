## E.4.PFR - Pattern-Framework Relation and Edition Discipline

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative.

### E.4.PFR:1 - Problem frame

Use this pattern when an FPF framework needs to record how patterns, framework editions, publication carriers, access carriers, source packs, decisions, generated carriers, and quality records relate without collapsing every relation into dependency, method order, inheritance, runtime/API relation, or cross-reference.

Primary `EntityOfConcern`: relation and edition records for an FPF-grounded pattern framework. The first useful output is one or more relation records with a relation function, direct governing pattern, dependency or edition effect when present, blocked stronger reading, and return condition.

Use this pattern for relation, dependency, compatibility, deprecation, supersession, and edition discipline. Use `E.11.PUR` for pattern-use recommendations and `E.17` for publication structures.

### E.4.PFR:2 - Problem

Pattern frameworks need many relation functions. One pattern may specialize another. A local framework may depend on a domain framework edition. An all-in-one publication carrier may publish a selected pattern set. A skill pack or MCP-backed service may expose access to that set. A generated graph may suggest relation candidates. A quality result may evaluate a pattern version. These relations have different meanings and different owners.

If they are all recorded as "related patterns" or "dependencies", maintainers cannot tell which relation can be used for what purpose, which stronger reading is blocked, what breaks when an edition changes, or which owner receives repair.

### E.4.PFR:3 - Forces

| Force | Tension |
| --- | --- |
| Relation economy | Frameworks need compact relation records, but compact rows can hide relation function. |
| Dependency pressure | Edition dependencies are useful, but they are not specialization, pattern-use order, or publication grouping. |
| Compatibility pressure | Framework editions need compatibility boundaries, deprecation, and supersession, but FPF frameworks are not software packages. |
| Generated structure pressure | Graphs and search outputs can suggest relations, but relation meaning must be decided by FPF owners. |
| Evolution | A relation that was valid for one edition may require repair after Core, source, or local use changes. |

### E.4.PFR:4 - Solution

Record relation claims through explicit relation records before using them for architecture, publication, dependency, or quality work.

```text
PatternFrameworkRelationRecord@Context:
  relationId
  sourceRef
  targetRef
  relationFunction
  governedUse
  directGoverningPatternRef
  dependencyOrEditionEffect?
  preservationOrAdmissionRef?
  blockedStrongerReading
  sourceReturnCondition?
  refreshOrSupersessionCondition?

FrameworkEditionDependencyRecord@Context:
  frameworkEditionRef
  dependsOnEditionRefs
  dependencyReason
  compatibilityBoundary
  deprecationOrSupersessionRefs?
  refreshConditionRefs?
  e53ConformanceNote

FrameworkPackageManifest@Context:
  frameworkEditionRef
  selectedPatternSetPublicationRef
  relationRecordRefs
  dependencyAndEditionRecordRefs
  editionStatus
  deprecationOrSupersessionRefs?
  sourcePackRefs
  qualityEvidenceRefs
  refreshPlanOrCurrentnessRefs
  firstEntryCarrierRefs
  blockedRuntimeOrBuildReading
```

Use relation functions by what they do:

| Relation function | Admissible use | Owner |
| --- | --- | --- |
| Pattern-use recommendation | Selects or sequences a pattern use for a concern. | `E.11.PUR` |
| Governing-pattern relation | Says which pattern owns a claim, relation, value, boundary, or publication form. | Direct governing pattern |
| Specialization | Narrows a parent pattern's EntityOfConcern, use, or publication form with inherited and changed obligations. | Parent pattern and `E.8` |
| Architecture decision link | Connects a decision relation to selected framework structures and consequences. | `E.4.PFAD`, `C.32.PAD` |
| Publication relation | Exposes selected content through all-in-one carrier, readme, preface, card, view, or table of contents. | `E.11`, `E.17` |
| Access relation | Exposes selected framework content or pattern-use routes through a skill pack, MCP-backed access service, retrieval route, or assistant integration with edition, bounded use, and blocked runtime/build overread. | `E.11`, `E.17`, with `C.35`, `A.15`, `A.10`, `B.3`, `E.9`, or `G.11` when generated output, work/tool action, evidence, assurance, decision, or currentness claims are live. |
| Framework edition dependency | Declares reliance on a more stable framework edition with compatibility and refresh conditions. | `E.5.3`, `G.11` |
| Preservation relation | Claims that one carrier, edition, profile, or projection preserves selected structure for a licensed use. | `C.34`, with `C.33` when loss is local to one carrier |
| Produced-carrier admission | Allows generated, searched, mined, or transformed carriers to seed framework work under declared conditions. | `C.35` |
| Quality framing, evaluation, or improvement | Frames the evaluation question, evaluates FPF-level adequacy, one DPF package, or one pattern, or records repeated improvement. | `E.22` for framing, `E.2.DA` for whole-FPF adequacy, `E.4.DPF.DA` for DPF package adequacy, `E.21` for individual pattern quality, `E.23` for improvement |
| Selected-set publication | Publishes a selected set with scope and selection conditions. | `G.5` |
| Source or decision reuse | Uses a source line, SoTA pack, `DRR`, accepted decision, or evidence/source claim by value for a bounded relation use. | `G.2` for source packs and SoTA, `E.9` for accepted DRR or decision rationale, `A.10` when an evidence or currentness claim is made |

Apply the edition rule: domain and local frameworks depend toward more stable editions. A local practice framework may depend on a domain principle framework and FPF Core. A domain principle framework may depend on FPF Core. FPF itself as a First Principles Framework edition is handled through `E.4.FPF`; FPF Core does not depend on domain or local frameworks except through a deliberate Core amendment.

Use compatibility practice narrowly: state compatibility boundary, dependency impact, deprecation, supersession, and refresh conditions. Do not import software build or performed-work semantics into pattern relations.

Use `FrameworkPackageManifest@Context` only when authors need one package-like index for a domain principle framework or local practice framework. For the form of FPF itself, use `E.4.FPF` and its `FPFFormMap`; do not force FPF into the DPF/local manifest shape. The manifest lists the selected pattern set publication, access carriers, relation records, dependency pins, edition status, deprecation or supersession refs, source-pack pins, quality evidence, refresh plan, and first-entry carrier. Listing a skill package, MCP endpoint, API route, or assistant integration records a framework access route only; it does not create imports, APIs, runtime dependencies, build semantics, module calls, tool permission, or authority over pattern-use relations. If the selected pattern set itself is being published, use `G.5`; if currentness is being planned, use `G.11`; if the manifest is used as architecture evidence, use `C.33` or `C.34` for captured and lost structure.

### E.4.PFR:5 - Archetypal Grounding

Tell: A hydroponic-cucumber framework edition depends on an FPF Core edition. It has a publication relation to its all-in-one publication carrier, an access relation to a grower-assistant skill pack or MCP-backed advisory route when those are built, a source relation to greenhouse-control source packs, a specialization relation where one pattern narrows an FPF authoring pattern for crop-domain use, and quality relations for evaluated pattern drafts.

Show: A local Codex process framework depends on FPF Core and on selected architecture patterns. Its baton-handoff pattern may coordinate with `E.11.PUR`, but that relation is not an instruction to perform that method. The relation record states the governed use and the direct pattern owner.

Show: A generated relation graph says pattern A "depends on" pattern B. PFR does not accept the word at face value. It asks whether the relation is recommendation, specialization, publication, edition dependency, preservation, admission, quality, or source use, then records the decided function.

Dependency and specialization example:

```text
PatternFrameworkRelationRecord@CodexProcessFramework:
  relationId: PFR-CODEX-DEP-001
  sourceRef: CodexPrelandingAttentionPattern@LocalPracticeFramework
  targetRef: FPFCorePatternSet@current
  relationFunction: Framework edition dependency
  governedUse: local process pattern uses FPF Core authoring and quality rules
  directGoverningPatternRef: E.5.3
  dependencyOrEditionEffect: local framework depends on Core; no Core reverse dependency
  blockedStrongerReading: not specialization and not instruction to perform Core patterns
  refreshOrSupersessionCondition: refresh when Core edition changes relevant authoring rules
```

Source and decision reuse example:

```text
PatternFrameworkRelationRecord@HydroponicCucumberDomain:
  relationId: PFR-HC-SRC-001
  sourceRef: G2-HC-nutrient-source-pack
  targetRef: HC.NutrientMonitoringPattern@draft
  relationFunction: Source or decision reuse
  governedUse: pattern solution uses source-pack claim sheet by value for nutrient-monitoring guidance
  directGoverningPatternRef: G.2
  preservationOrAdmissionRef: C.33-source-pack-summary-loss-note
  blockedStrongerReading: not framework edition dependency, not specialization, not publication relation
  sourceReturnCondition: return to G.2 when the source pack drops a rival horticulture tradition
```

### E.4.PFR:6 - Bias-Annotation

The main drift is relation-word overread: a useful word such as "depends", "uses", or "profiles" is treated as if its ordinary meaning settled the relation function. The repair is to write the relation function, governed use, owner, and blocked stronger reading in the record.

The second drift is software-package analogy overreach. Compatibility and deprecation practices are useful, but pattern frameworks are not software packages. The repair is to keep edition dependency and compatibility as FPF records, not as build or performed-work semantics.

### E.4.PFR:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-PFR.1 Relation record exists | Each load-bearing relation has a record naming source, target, relation function, governed use, owner, and return condition. |
| CC-PFR.2 Function before label | The relation function is selected by what the relation does, not by word similarity. |
| CC-PFR.3 Dependency separated | Framework edition dependency is separated from specialization, publication, pattern-use recommendation, and preservation. |
| CC-PFR.4 E.5.3 respected | Dependency direction points toward stable framework editions and Core does not depend on domain or local frameworks. |
| CC-PFR.5 Compatibility boundary present | Edition dependencies that carry compatibility claims name boundary, deprecation, supersession, and refresh conditions. |
| CC-PFR.6 Carrier relation routed | Publication, access, preservation, and produced-carrier claims use `E.11`, `E.17`, `C.33`, `C.34`, `C.35`, `A.15`, or `G.11` as appropriate. |
| CC-PFR.7 Source and decision reuse routed | Source-line, SoTA-pack, DRR, accepted-decision, evidence, and currentness reuse claims route to `G.2`, `E.9`, or `A.10` instead of relation-label prose. |

### E.4.PFR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Related-pattern flattening | A relation list hides relation function and owner. | Convert load-bearing rows into `PatternFrameworkRelationRecord@Context`. |
| Dependency as specialization | A framework edition dependency is read as child-pattern inheritance. | Use `FrameworkEditionDependencyRecord@Context` and state any specialization separately. |
| Compatibility by version label | A new edition number is assumed to settle impact. | Add compatibility boundary, deprecation, supersession, and refresh conditions. |
| Generated graph as relation authority | A produced graph decides relation meaning. | Use `C.35` for admission, then record relation functions through PFR. |
| Callable route as dependency | A skill, MCP endpoint, API route, or assistant integration is read as framework edition dependency, runtime import, or method order. | Record an `Access relation` with bounded use and blocked stronger reading; route tool/work behavior, generated outputs, and currentness claims to their owners. |
| Source prose as relation authority | A paragraph says a source or DRR "supports" a pattern but does not state bounded use, owner, or return condition. | Record `Source or decision reuse` with `G.2`, `E.9`, or `A.10` as owner and a source-return condition. |

### E.4.PFR:9 - Consequences

PFR makes relation work more explicit and less terse. The gain is that dependency impact, publication use, preservation, specialization, quality, and source-return claims no longer compete under one ambiguous relation label.

The pattern also makes edition changes more inspectable. When a framework edition changes, maintainers can inspect dependency records, compatibility boundaries, deprecation, supersession, and refresh conditions instead of searching prose.

### E.4.PFR:10 - Rationale

FPF pattern ecosystems are declarative relation systems. Relations constrain admissible use, publication, dependency, preservation, evaluation, and source return. They are not one general edge kind and not a performed-work order.

The pattern adopts the useful part of package and versioning practice, but only at the level of public compatibility, dependency impact, deprecation, supersession, and refresh. This keeps FPF relation ontology intact while still learning from mature ecosystem practice.

### E.4.PFR:11 - SoTA-Echoing

| Claim | Exact source ref and status | Pattern locus changed | Adoption status |
| --- | --- | --- | --- |
| Ecosystem dependencies need compatibility boundaries and impact inspection, not only version labels. | `Semantic Versioning 2.0.0`, current-standard versioning and compatibility-boundary practice, `https://semver.org/spec/v2.0.0.html`; Chen et al., `Breaking Changes in Software Ecosystems: A Systematic Literature Review`, arXiv:2605.24397, 2026 current SLR, `https://arxiv.org/abs/2605.24397`. | `FrameworkEditionDependencyRecord@Context`, `CC-PFR.5`, and compatibility anti-pattern require boundary, deprecation, supersession, refresh, and impact inspection. | Adapt compatibility and dependency-impact discipline to framework editions; reject software build and binary dependency ontology. |
| Reuse across related frameworks needs core assets, variation, and evolution discipline. | Nazar, `Software Product Line Engineering: Adoption, Tooling and AI Era Challenges`, arXiv:2605.21353, 2026 current survey, `https://arxiv.org/abs/2605.21353`. | Relation-function table separates framework edition dependency from specialization and publication; `E.5.3` direction is repeated as an edition rule. | Adapt reusable-core and variation thinking to FPF Core, domain frameworks, and local frameworks. |
| Relation-rich systems need declarative relation meaning rather than performed-work order. | `Modelica Language Specification 3.6`, Modelica Association, current maintained language-spec analogy, `https://specification.modelica.org/maint/3.6/MLS.pdf`. | `PatternFrameworkRelationRecord@Context`, `Bias-Annotation`, and examples require relation function, governed use, owner, and blocked stronger reading. | Use as analogy only; reject equations, solvers, simulation, class-model semantics, and acausal-language ontology for FPF. |
| Source and produced-carrier relation claims need validation, evidence, and loss accounting before reuse. | Riehle, Harutyunyan, Barcomb, `Pattern Discovery and Validation Using Scientific Research Methods`, arXiv:2107.06065, 2021 current validation-practice source; `ISO/IEC/IEEE 42010:2022` as current description-boundary standard ref. | Added `Source or decision reuse` relation row, source-reuse examples, `CC-PFR.7`, and source-prose anti-pattern. | Adopt validation and description-boundary pressure; route source reuse to `G.2`, decision reuse to `E.9`, evidence/currentness claims to `A.10`, and produced carriers to `C.35`. |

### E.4.PFR:12 - Relations

- **Builds on:** `E.5.3` for directed dependency and family-order discipline.
- **Coordinates with:** `E.4` for family membership and selected structure architecture.
- **Coordinates with:** `E.4.FPF` when relation and edition records concern FPF itself as a first-principles framework edition or one of its publication/access carriers.
- **Coordinates with:** `E.4.PFAD` when a relation or dependency is selected by an architecture decision.
- **Coordinates with:** `E.11.PUR` for pattern-use recommendation and sequencing.
- **Coordinates with:** `E.11`, `E.17`, and `G.5` for publication and selected-set exposure.
- **Coordinates with:** `F.18` for relation and framework names.
- **Coordinates with:** `G.11` for refresh, `E.22` for quality-evaluation framing, `E.2.DA` for whole-FPF adequacy evaluation, `E.4.DPF.DA` for DPF package adequacy evaluation, `E.21` for individual pattern-quality evaluation, and `E.23` for repeated improvement.
- **Coordinates with:** `C.33`, `C.34`, and `C.35` for carrier loss, preservation, and produced-carrier admission.

### E.4.PFR:End

