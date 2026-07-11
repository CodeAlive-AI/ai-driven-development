## E.4.DPF.DA - Domain Principle Framework Package-Adequacy Evaluation CharacteristicSpace

> **Type:** Evaluation (E)
> **Status:** Stable
> **Normativity:** Normative unless marked informative.

### E.4.DPF.DA:1 - Problem frame

Use this pattern when a framework author, reviewer, steward, or AI agent must decide whether one Domain Principle Framework or Local Practice Framework package is good enough for one declared domain or local use.

Primary `EntityOfConcern`: `DPFPackageAdequacyEvaluation@Context`, an authored evaluation over one bounded framework package edition. The package may be a DPF seed, selected pattern host set, all-in-one publication carrier, card set, skill pack, MCP-backed access service, source-pack-backed pattern family, or enterprise local practice framework edition. The first useful output is a coordinate table with values, short rationales, evidence loci, and repair proposals.

Do not use `E.2.DA` directly as the ordinary DPF package evaluation. `E.2.DA` asks whether FPF-level objects realize the FPF Pillars for broad FPF use. A DPF package has a narrower burden: it must serve one declared domain or local context while depending on FPF Core without redefining it. Use `E.2.DA` only when the DPF package changes or claims FPF-level Pillar adequacy.

Use `E.21` for the quality of individual DPF pattern bodies. Use this pattern for the package as a whole: domain scope, source basis, Core dependency, DPF-wide publication-carrier form, pattern-set coverage, relation and edition records, local publication, evaluation route, refresh route, and adoption utility.

### E.4.DPF.DA:2 - Problem

DPF packages will often be produced quickly from source material, prompts, external literature, local practice, or generated candidates. Some are good enough as seeds; some can answer a domain question for an AI agent; some are public-ready publication carriers; some are only source summaries wearing pattern headings.

Without a DPF-specific adequacy evaluation, teams tend to use one of three wrong substitutes:

- they apply `E.2.DA` and ask whether the package is "FPF-like in general", even though the package is meant for one domain;
- they average `E.21` scores of individual patterns and miss package-level failures such as missing source packs, broken dependency direction, poor first entry, or stale edition records;
- they inspect section presence and conclude that an all-in-one carrier, map, or seed package is adequate because it has patterns, a table of contents, a readme, a preface, maps, and sources.

The result is adoption risk. A reader may get a fluent local framework that does not know its domain boundary, does not preserve rival source traditions, duplicates FPF Core ontology, hides relation functions, has no refresh route, or cannot tell a practitioner what typical problem is live, which known failure mode to avoid, and which SoTA solution move to try first.

### E.4.DPF.DA:3 - Forces

| Force | Tension |
| --- | --- |
| Domain boundedness vs FPF generality | The DPF must be strong for one domain or local context, not a second FPF Core. |
| Pattern quality vs package quality | Strong individual patterns can still form a weak package if source, relation, publication, or refresh structures are missing. |
| Fast seeds vs reliance-bearing packages | A seed may be useful for exploration, but public or operational use needs higher evidence and repair routes. |
| Source richness vs source theatre | A long bibliography can decorate the package while missing adopted payload, rejected alternatives, currentness, and pattern consequences. |
| Local usability vs formal assurance | Readers need first moves and worked cases, while maintainers need edition, dependency, relation, quality, and refresh records. |
| Improvement vs proxy optimization | Adding maps, source rows, all-`5` claims, or review proof can make the package less usable. |

### E.4.DPF.DA:4 - Solution

Evaluate one DPF package edition for one declared use through a DPF-specific adequacy characteristic space. The evaluation is derived from the shape of `E.2.DA`, but it is not the FPF Pillar evaluation. It asks whether the package realizes FPF-grounded domain value for a declared domain or local context.

```text
DPFPackageAdequacyEvaluation@Context:
  evaluatedPackageRef:
  packageKind: domain-principle-framework | local-practice-framework | seed | selected-host-set | all-in-one-publication-carrier | skill-pack | mcp-backed-access-service | mixed
  declaredDomainOrLocalContext:
  intendedReaderOrOperator:
  declaredUse:
  nonUseBoundary:
  fpfCoreEditionRef:
  dependencyAndEditionRefs:
  sourceBasisRefs:
  pfadDecisionRefs:
  patternSetRefs:
  relationRecordRefs:
  publicationCarrierRefs:
  accessCarrierRefs:
  qualityEvidenceRefs:
  refreshRefs:
  evaluationEvidenceBasis:
  coordinateTable:
  protectedTradeoffSet:
  status:
  firstRepairOrNoProposalDisposition:
  reopenCondition:
```

#### E.4.DPF.DA:4.1 - Ordinal scale

| Value | Label | Meaning |
| --- | --- | --- |
| `0` | `wrongKindOrNoBasis` | The object is not an evaluable DPF package for the declared use, or required basis is absent. |
| `1` | `namedOnly` | The package name or topic exists, but the package cannot guide domain or local work. |
| `2` | `partialSeed` | Useful source, prompt, or pattern-seed material exists, but package obligations are incomplete or fragile. |
| `3` | `locallyUsableWithVisibleLimits` | The package can support bounded exploration or local use with explicit limits and repairs. |
| `4` | `wellGroundedForDeclaredDPFUse` | The package is coherent, source-grounded, FPF-dependent, navigable, and refreshable for the declared use. |
| `5` | `exceptionallyGroundedForDeclaredDPFUse` | The package is replayable across source basis, pattern set, relation records, heterogeneous cases, publication carriers, improvement route, refresh route, and blocked overreads. |

Default floor is `4` for public, teaching, enterprise, operational, or reliance-bearing DPF use. A fast seed or exploratory prompt output may use floor `3` only when non-use, missing evidence, and next repair are explicit.

#### E.4.DPF.DA:4.2 - Required coordinates

Every `E.4.DPF.DA` run evaluates every coordinate below. Do not drop a coordinate because the package is "only a seed"; assign the value that the seed earns.

In this pattern, `known failure modes` means beginner mistakes and experienced-practitioner failures caused by stale, local-only, or non-SoTA practice. Do not narrow the check to novice errors only.

| Coordinate | Evaluation question | Good state |
| --- | --- | --- |
| `D1DomainScopeAndUseAdequacy` | Is the domain or local context, reader, declared use, and non-use boundary recoverable? | The package tells whom it is for, what domain situation it covers, what it does first, and what it must not be used for. |
| `D2DidacticEntryAndAdoptionAdequacy` | Can the intended reader or assisting agent find the first useful entry and get a first working result without FPF developer knowledge? | ToC, readme, preface, pattern-use routes, skill entries, MCP access cues, and examples make adoption cheap and non-magical, while support maps are reached from work triggers rather than front-loaded as required reading. |
| `D3ScalableFormalityAndAssurancePathAdequacy` | Can the package move from plain local use toward stronger records, evaluation, evidence, or assurance without rewriting the package? | Plain guidance, typed records, source pins, evaluation rows, and stronger owners are staged. |
| `D4CoreDependencyAndDomainBoundaryAdequacy` | Does the package depend on FPF Core while keeping domain knowledge inside the DPF? | Core owners are reused; local terms do not redefine Core; possible Core amendment candidates are explicit; FPF Core and the main monolith do not depend on this DPF except through a deliberate Core amendment. |
| `D5PackageFormLayeringAndRelationAdequacy` | Are pattern set, support maps or appendices, relation records, edition dependencies, publication carriers, access carriers, source packs, and quality records separated? | `E.4.PFR`, `E.4.PFAD`, source, publication, access, quality, support-map, appendix, and refresh loci remain distinct, findable, and reached from the right work triggers. |
| `D6DomainLexiconAndKindSettlementAdequacy` | Are domain terms, local vocabulary, candidate ontics, and FPF owners settled well enough for use? | Local terms have kind, owner, admissible use, blocked overread, and naming route when needed. |
| `D7PracticeUtilityAndProblemResolutionAdequacy` | Does the package change real domain or local action, diagnosis, design, explanation, teaching, or repair? | Patterns solve recognizable domain problems with positive SoTA-informed moves, known failure modes or anti-patterns, and worked cases, not only taxonomy, ontology, commentary, or talk guidance. |
| `D8HeterogeneousCaseAndTransferAdequacy` | Has the package been tested against diverse enough domain cases, reader roles, or local situations? | Heterogeneous probes show where the same pattern set works, fails, or needs a neighbouring owner. |
| `D9EditionStateAndCurrentnessAdequacy` | Are package edition, source currentness, dependency pins, qualification window, and status of carriers explicit? | Readers can tell what version they use, what source state supports it, and what changes it. |
| `D10ImprovementAndRefreshAdequacy` | Can the package improve through `E.22`/`E.23` and refresh through `G.11` without giant reopen or process theatre? | Low values produce repair rows; source, edition, telemetry, and use failures have smallest reopen routes. |
| `D11DomainSoTAAlignmentAdequacy` | Does current domain or local SoTA discipline pattern selection, solution, examples, boundaries, and reopen triggers? | Sources change the package content; they are not bibliography, claim theatre, or authority by citation. |

#### E.4.DPF.DA:4.3 - Result row shape

An `E.4.DPF.DA` result uses this table shape:

| Coordinate | Value | ShortRationale | EvidenceLocus | RepairOrNoProposal |
| --- | --- | --- | --- | --- |
| `<D1..D11>` | `<0..5>` | `<why this value, why lower would understate evidence, why higher would overstate it or what would lower or reopen a 5>` | `<package section, source row, relation record, pattern body, readme, ToC, skill entry, MCP route, worked case, quality result, refresh route, missing locus>` | `<repair, no-proposal with checked loci, or owning neighbour>` |

A prose verdict, a checklist-count result, a table without evidence loci, or an average of `E.21` pattern values is not an `E.4.DPF.DA` result.

#### E.4.DPF.DA:4.3a - DPF-wide package-form checks

Run this subpass for any all-in-one DPF publication carrier, selected-host-set, card set, skill pack, MCP-backed access service, or package publication or access carrier. These checks do not replace the eleven coordinates; they supply package-level evidence mainly for `D1`, `D2`, `D4`, `D5`, `D7`, `D8`, `D9`, `D10`, and `D11`.

| Package-form check | Passing condition | Primary affected coordinates |
| --- | --- | --- |
| `PFM1 Front-door order` | The package front door has a usable ToC, readme, and preface or equivalent first-entry carrier before pattern bodies; the reader can choose a first pattern without reading support apparatus first. | `D2`, `D5` |
| `PFM2 Pattern-language primacy` | Pattern bodies remain the main language of use. Large maps, source-use tables, relation records, edition notes, and package architecture material appear after pattern bodies or in appendices or support sections unless they are a short first-entry aid. | `D2`, `D5`, `D7` |
| `PFM3 Map discoverability` | Every support map or appendix has at least one live entry route from ToC or readme, a pattern `Relations` section, low-value repair action, source-return condition, or package-refresh condition. A map that cannot be reached from work lowers package adequacy even if the map is correct. | `D2`, `D5`, `D10` |
| `PFM4 Dependency direction` | The DPF may cite FPF Core and explicitly depended-on upstream DPFs or local frameworks; FPF Core and the main monolith do not cite this DPF as required authority. If a DPF discovery belongs in Core, it returns through a Core amendment decision rather than a reverse dependency. | `D4`, `D5`, `D9` |
| `PFM5 Publication-and-access-carrier boundary` | The all-in-one carrier, readme, preface, ToC, card set, maps, skill pack, MCP-backed access route, retrieval route, and assistant integration are publication or access carriers. They do not become the framework architecture, source pack, quality result, admission status, process state, runtime dependency, work authority, evidence source, or currentness proof by being visible or callable. | `D5`, `D9` |
| `PFM6 Public package naming` | The public title and primary file or package name use a domain- or practice-specific framework name such as `<DomainOrPractice> Principles Framework`, with the domain or practice head visible. `Principles Framework` alone is only a kind or head phrase, not an individual framework name. Format slang such as `local monolith`, process state such as `draft`, and file-layout labels stay out of public package identity unless the carrier is explicitly a workspace-only artifact. | `D1`, `D2`, `D5`, `D6`, `D9` |
| `PFM7 Development-state absence` | Package carriers contain user-facing package content and durable package relations, not scattered `draft`, `DRR`, handoff, ledger, review-status, admission-blocker, helper-state, or process-run residue. | `D5`, `D9`, `D10` |
| `PFM8 Cross-DPF relation discipline` | References to another DPF or local framework are recorded as dependency, specialization, source reuse, publication, selected-set, or other `E.4.PFR` relation with blocked stronger reading and refresh condition. | `D4`, `D5`, `D9` |
| `PFM9 Normal-pattern maturity` | Every pattern body claimed as part of a public, teaching, enterprise, or reliance-bearing DPF is a normal action-guiding FPF-style pattern for its declared use: it is drafted through `E.8`, evaluated through `E.21`, and not merely a heading skeleton, seed note, prompt output, compressed DRR recap, term sheet, ontology catalog, or commentary about the domain. The pattern should show the typical problem, known failure mode or anti-pattern, SoTA-informed solution move, worked case, and boundary. Seeds are allowed only when the package status says `seedOnly` or the affected pattern is explicitly non-reliance-bearing. | `D2`, `D7`, `D8`, `D11` |
| `PFM10 Access-currentness and callable-use boundary` | Skill packs and MCP-backed access services expose framework edition, dependency, source and currentness, bounded use, and refresh route. Generated outputs route to `C.35`; tool and work actions route to `A.15` or the local work owner; evidence, assurance, decision, and currentness claims route to their direct owners. | `D2`, `D5`, `D9`, `D10` |
| `PFM11 Carrier structure-account and controlled structural coarsening` | Readme, Preface, or equivalent first-entry carrier provides a structure-account: what the package exposes for whom, which domain or local structures and source denominator it foregrounds, what it deliberately coarsens, abstracts, omits, loses, or sends to appendices and sources, and how a reader returns to pattern bodies, source packs, evidence owners, or relation records. This is source-structure-to-publication/access accounting, not only text summarization. The carrier is not itself the framework edition, the domain, or a narrative by type. In architecture-mediated narrative-rendering cases, the return chain is `narrative rendering carried by a publication or access carrier -> architecture description or view -> architecture as selected structures in context -> wider source structures`; when no narrative rendering is present, the first step is `framework publication or access carrier -> selected source structures`. Every arrow has its own selection, coarsening, abstraction, omission, preservation, and loss account. If package-level structure-capture or epiplexity is claimed, its declared use and lowering reason are explicit. | `D1`, `D2`, `D5`, `D7`, `D8`, `D10`, `D11` |

A failure in this subpass lowers the affected coordinate even when individual pattern bodies pass `E.21`. Repair the package carrier, relation record, first-entry route, dependency record, or support-map placement; do not copy the package-form proof into pattern bodies.

#### E.4.DPF.DA:4.4 - Evidence basis and neighbouring owners

Use these owners instead of expanding this pattern into a package bureaucracy:

| Evidence or defect | Owner |
| --- | --- |
| Source payload, rejected alternatives, source currentness, and source-use boundary | `G.2`, `G.11` |
| Framework architecture decision, selected pattern set, publication carrier, dependency boundary | `E.4.PFAD`, `E.4`, `E.4.PFR` |
| Individual pattern quality | `E.21` |
| Pattern admission or profile gating | `E.19` |
| First-entry and publication carrier | `E.11`, `E.17` |
| Carrier structure-account, captured/coarsened/lost structure, package-level source return, and structure-capture or epiplexity account | `E.4.DPF`, `E.11`, `E.17`, `A.6.3.CSC`, `C.33`, `C.34`, and `A.6.3.NAR` when sequential narrative rendering is load-bearing |
| Naming and local vocabulary | `E.10`, `F.18`, direct governing pattern |
| Generated or searched package candidate | `C.35`, then `E.4.PFAD` or direct owner |
| Carrier capture, loss, and preservation | `C.33`, `C.34` |
| Improvement framing and repeated improvement | `E.22`, `E.23` |
| FPF-level Pillar effect | `E.2.DA`, only when the package changes FPF-level adequacy |

When a coordinate is below floor, return a finding or repair proposal. When a coordinate is at `4` and improvement is requested, search for a substantive non-dominated improvement. Do not raise a value by adding proof apparatus, more maps, more citations, or quality-status prose unless the package becomes easier to use, more source-grounded, more accurately bounded, or more refreshable.

#### E.4.DPF.DA:4.5 - Status

| Status | Meaning |
| --- | --- |
| `admissibleForDeclaredDPFUse` | All coordinates meet the declared floor for the stated DPF use, with non-use and reopen conditions named. |
| `repairBeforeDPFUse` | One or more coordinates are below floor for the stated use. |
| `seedOnly` | The package is useful as a seed or prompt output but not for reliance-bearing use. |
| `holdForPFADDecision` | The package architecture, pattern set, dependency, or publication unit needs a framework architecture decision. |
| `holdForCoreAmendmentDecision` | A package claim may belong in FPF Core and must not be hidden inside a DPF. |
| `refreshNeeded` | The package was adequate before, but source, Core edition, local use, telemetry, or dependency state has changed. |

### E.4.DPF.DA:5 - Archetypal Grounding

Tell: A personal-development DPF is generated in one short run. It may have useful principles and pattern seeds. `E.4.DPF.DA` can mark it `seedOnly` with high values for first-entry utility and low values for source-currentness, heterogeneous probes, relation records, or refresh. That is not failure; it is an honest package status and a next repair route.

Show: A domain DPF all-in-one publication carrier contains domain patterns, a source-use map, a Core-bridge map, relation records, and heterogeneous acceptance cases for several user situations. `E.4.DPF.DA` asks whether those cases actually force the pattern set to solve different domain problems, whether source rows changed pattern obligations, whether maps are reachable during work, and whether the package's local evaluation pattern can feed `E.22`/`E.23` without becoming a hidden Core dependency.

Show: A hydroponic-cucumber DPF has excellent crop-control sources but no relation records and no first-entry carrier. `E.21` may find that individual crop patterns are good, but `D5PackageFormLayeringAndRelationAdequacy` and `D2DidacticEntryAndAdoptionAdequacy` stay below floor until relation records and first-use routes exist.

Near miss: A DPF all-in-one publication carrier has a huge map before the pattern bodies. The map is correct but cold readers do not know when to open it. `D2` and `D5` fall unless pattern relations, low-value repair actions, or first-entry text route readers into the map from a real work trigger.

Near miss: A DPF has polished readme and Preface prose, but neither says what selected domain structure the publication/access expression exposes, what it deliberately coarsens or abstracts, or where a reader returns for fuller source and pattern detail. If the carrier is based on an architecture description, view, model, or graph, it also hides the fact that the intermediate source already selected and coarsened structure on the route `source structures -> architecture -> architecture description or view -> publication/access expression`. `D1`, `D2`, `D5`, `D7`, `D8`, and `D11` fall because the carrier may be pleasant but its structure-capture claim is not inspectable.

### E.4.DPF.DA:6 - Bias-Annotation

The first drift is whole-FPF overreach: a DPF package is judged as if it had to cover every domain. Repair by declaring one domain or local context and evaluating adequacy for that context.

The second drift is local excellence laundering: good-looking patterns, a polished monolith, or generated fluency hides missing source, relation, edition, and refresh structures. Repair by evaluating the package coordinates, not only pattern bodies.

The third drift is quality proof leakage: evaluation results, review status, or package architecture evidence are copied into user-facing pattern prose. Repair by moving quality evidence to this evaluation, `E.21`, `E.19`, `E.11`, `I.2`, or publication evidence loci, and keep only the user-facing move or boundary in pattern bodies.

The fourth drift is invisible carrier narration: the package is presented as a transparent list of principles, so nobody asks which domain structures were selected, coarsened, abstracted, omitted, or already transformed through `source structures -> architecture -> architecture description or view -> publication/access expression` before the publication carrier was written. Repair by making the readme, Preface, or access front door provide a short carrier structure-account and checking it through `PFM11`.

### E.4.DPF.DA:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-DPFDA.1 Object and use declared | Evaluated package edition, package kind, domain or local context, intended reader, declared use, and non-use boundary are named. |
| CC-DPFDA.2 All coordinates evaluated | All eleven coordinates receive value, short rationale, evidence locus, and repair or no-proposal disposition. |
| CC-DPFDA.3 E.2.DA boundary respected | The result does not claim FPF-level Pillar adequacy unless `E.2.DA` is separately invoked. |
| CC-DPFDA.4 E.21 not averaged | Individual pattern-quality results are evidence only where they change package adequacy. |
| CC-DPFDA.5 Source and SoTA payload checked | Source rows change pattern selection, solution, examples, boundaries, or refresh; decorative citation lowers `D11`. |
| CC-DPFDA.6 Relation and publication separated | Maps, manifests, readmes, prefaces, ToCs, all-in-one carriers, source packs, relation records, quality records, and pattern bodies keep their owners. |
| CC-DPFDA.6a Package-form subpass complete | `PFM1` through `PFM11` have explicit pass, fail, or not-applicable-with-reason dispositions before D1, D2, D4, D5, D7, D8, D9, D10, and D11 values are assigned. |
| CC-DPFDA.6b Reverse dependency blocked | The result checks that FPF Core and the main monolith do not depend on this DPF; any needed Core-level content returns through a Core amendment decision. |
| CC-DPFDA.6c Structure-account checked | The result checks whether readme, Preface, ToC, all-in-one carrier, skill entry, or MCP front door states reader, selected or exposed structure, controlled coarsening, abstraction, omission, loss, source return, and any structure-capture or epiplexity claim before adoption or package adequacy values are raised. |
| CC-DPFDA.7 Improvement route concrete | Below-floor coordinates return smallest useful repair slices; above-floor improvement proposals are substantive or explicitly dominated. |
| CC-DPFDA.8 Seed status honest | Seed, prompt-output, and generated candidates are not promoted to reliance-bearing package status without evidence, admission, quality, and refresh routes. |

### E.4.DPF.DA:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| `E.2.DA` as DPF review | The package is judged against whole-FPF Pillars and domain adequacy is blurred. | Use `E.4.DPF.DA`; invoke `E.2.DA` only for FPF-level effects. |
| `E.21` averaging | Strong individual pattern scores hide weak package architecture. | Evaluate package coordinates directly; use `E.21` only as evidence. |
| Source bibliography as adequacy | Sources are listed but do not change the package. | Return to `G.2`; carry adopted and rejected payload into pattern moves and boundaries. |
| Publication carrier as package proof | The carrier is readable but relation, edition, source, and refresh structures are unrecoverable. | Add `E.4.PFAD`, `E.4.PFR`, source-use, quality, and refresh loci; keep publication as carrier. |
| Invisible carrier structure-account | The carrier never tells what domain or local structure it selected, coarsened, abstracted, or omitted for the intended reader, so readers mistake the package for the domain itself or cannot judge coverage. | Add readme, Preface, ToC, skill-entry, or access-front-door carrier structure-account text, including source-return and structure-capture boundary, then rerun `PFM11`. |
| Skill or MCP access as package proof | The package is callable through a skill or endpoint, so the access carrier is treated as if it proved the framework edition, source, quality, or currentness. | Record the skill or endpoint as an access carrier, expose edition and relation refs, and evaluate the underlying package and patterns through `E.4.DPF.DA` and `E.21`. |
| Skeleton patterns as package proof | The package has pattern headings and canonical sections, but the bodies do not teach a working reader what to do, how to judge boundaries, or how source payload changes action. | Treat the package as `seedOnly`, then harden each body through `E.8` and `E.21` before public or reliance-bearing use. |
| Ontology or conversation package as DPF | The package explains terms, roles, or ways to talk about the domain, but it does not help the intended practitioner resolve typical domain problems with SoTA moves. | Lower `D7` and usually `D11`; keep the ontology or conversation guide as support material and add problem frames, solution moves, worked cases, and anti-pattern repairs. |
| Map hoarding | Huge maps appear before patterns and no work trigger leads to them. | Move maps after pattern bodies or make pattern relations and low-value repairs route to them. |
| Reverse dependency leak | FPF Core or the main monolith starts citing a DPF as required authority. | Move the claim into a Core amendment if it belongs in Core; otherwise keep the dependency one-directional from DPF to Core. |
| Process-state leakage | The package carrier includes `draft`, `DRR`, handoff, ledger, review, admission, or helper-state residue as package content. | Remove process state from package carriers and keep only durable user-facing package content, relation records, source-use boundaries, and refresh routes. |
| Seed promotion | A fast prompt result is treated as public DPF. | Mark `seedOnly`, name missing coordinates, and run `E.23` hardening. |
| Citation-driven `5` | Values rise because more sources, review proof, or maps were added. | Raise values only when action, source grounding, owner routing, adoption, or refresh improves. |

### E.4.DPF.DA:9 - Consequences

The pattern adds one package-level evaluation on top of individual pattern checks. The cost is worthwhile when DPF packages become reusable across domains, enterprises, AI-agent prompt packs, teaching materials, or local practice frameworks.

It also prevents a common false choice. A DPF seed can be useful without pretending to be public-ready, and a public-ready package can remain domain-bounded without pretending to be FPF Core.

### E.4.DPF.DA:10 - Rationale

FPF needed `E.2.DA` because a local edit can improve one pattern while harming the whole language. DPF packages need the analogous but narrower instrument: a package can have good patterns while failing as a domain framework. Domain source grounding, relation architecture, first-entry adoption, package publication, and refresh are package-level effects.

The coordinate set mirrors the spirit of the FPF Pillars but changes the adequacy question. FPF asks whether the whole framework remains broadly first-principle and cross-domain. A DPF asks whether one bounded domain or local framework is strong enough for its declared use while preserving dependency on FPF Core and source-return to its domain traditions.

### E.4.DPF.DA:11 - SoTA-Echoing

| Claim | Exact source ref and status | Pattern locus changed | Adoption status |
| --- | --- | --- | --- |
| Domain frameworks need co-evolving terminology, examples, usability, and evaluation rather than a static term list. | Zhang, Struber, Hebig, `Development and Evolution of Xtext-based DSLs on GitHub: An Empirical Investigation`, arXiv:2501.19222, 2025 current empirical DSL-evolution source. | Coordinates `D1`, `D2`, `D6`, `D9`, and `D10` require bounded context, adoption route, vocabulary settlement, edition state, and refresh. | Adapt co-evolution discipline to FPF-grounded frameworks; reject grammar or metamodel ontology unless a specific DPF owns it. |
| Reusable-core and domain-variation work needs explicit dependency, adoption, tooling, and evolution discipline. | Nazar, `Software Product Line Engineering: Adoption, Tooling and AI Era Challenges`, arXiv:2605.21353, 2026 current survey and reopen trigger for stronger future SPLE synthesis. | Coordinates `D4`, `D5`, `D9`, and `D10`, plus `PFM4` and `PFM7`, require Core dependency, relation records, edition pins, blocked reverse dependency, and refresh. | Adapt reusable-core discipline; reject software feature-model semantics as the default DPF ontology. |
| Pattern-language validation needs worked cases and near misses, not only section presence. | Riehle, Harutyunyan, Barcomb, `Pattern Discovery and Validation Using Scientific Research Methods`, arXiv:2107.06065, 2021 current validation-practice source; Iba, `Pattern Languages as Media for the Creative Society`, arXiv:1308.1178, lineage for pattern-language use. | Coordinate `D8`, `Archetypal Grounding`, and anti-patterns require heterogeneous probes and transfer checks. | Adopt validation pressure; route detailed pattern-body quality to `E.21`. |
| Architecture descriptions and publication carriers do not equal the architecture or package adequacy. | `ISO/IEC/IEEE 42010:2022`, current architecture-description standard ref. | Coordinates `D5` and `D9`, publication-carrier anti-pattern, and map-hoarding near miss separate publication carriers from package structures. | Adopt description-boundary discipline; adapt through `C.33`, `C.34`, `E.11`, and `E.17`. |
| Quality measures can become targets and make the object worse. | Goodhart, Campbell, management-accounting surrogation, specification-gaming, and reward-hacking lines already carried through `E.2.DA`, `E.13`, `E.21`, `E.22`, and `E.23`. | `Solution`, `Conformance Checklist`, and anti-patterns forbid all-`5`, source-count, map-count, or review-proof targeting. | Adopt proxy-risk discipline; values rise only through package-use improvement. |

### E.4.DPF.DA:12 - Relations

- **Builds on:** `A.19.ECS` for evaluation characteristic-space construction.
- **Specializes by object:** `E.2.DA` supplies the adjacent form for complete multi-coordinate adequacy evaluation, but this pattern changes the evaluated object from FPF-level object to DPF package edition.
- **Coordinates with:** `E.4`, `E.4.DPF`, `E.4.PFAD`, and `E.4.PFR` for framework family, authoring spine, architecture decisions, relation records, edition dependencies, and package architecture.
- **Coordinates with:** `G.2` and `G.11` for source packs, source currentness, and refresh.
- **Coordinates with:** `E.21`, `E.19`, `E.22`, and `E.23` for individual pattern quality, admission review, evaluation framing, and repeated improvement.
- **Coordinates with:** `E.11`, `E.17`, `F.18`, `C.33`, `C.34`, and `C.35` for first entry, publication, naming, preservation, correspondence, and produced-carrier admission.
- **Exits to:** `E.2.DA` when a DPF package change claims FPF-level Pillar adequacy or proposes Core amendment effects.

### E.4.DPF.DA:End

