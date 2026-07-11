## E.4.PFAD - Principle-Framework Architecture Decision

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative.

### E.4.PFAD:1 - Problem frame

Use this pattern when a framework author or steward must decide the architecture of one FPF-grounded domain principle framework or local practice framework: its purpose, selected pattern set, relation structure, publication or access carrier, dependency boundary, names, source basis, quality route, and currentness route.

Primary `EntityOfConcern`: `PrincipleFrameworkArchitectureDecision@Context`, a framework-local architecture decision relation with explicit slots. The first useful output is a filled decision relation, not an ADR document and not the realized framework itself.

Use this pattern only when the decision has framework-specific obligations beyond generic architecture-decision practice. If the decision only needs ordinary decision rationale or ordinary project architecture decision slots, use `E.9`, `C.32.PAD`, and `C.32.ADR` directly.

### E.4.PFAD:2 - Problem

Framework architecture decisions recur in FPF-grounded work. A steward must decide whether a set of patterns belongs in Core, in a domain framework, in a local framework, or in publication and pedagogy. They must also decide how the framework depends on FPF Core, what edition boundary it has, what sources ground it, what names are admissible, and which carriers publish or expose the framework.

If those decisions are hidden in prose, table shape, or an ADR-like file, later maintainers cannot tell which structure was selected, which alternative was rejected, what consequences were accepted, or when the decision should be repaired or superseded.

### E.4.PFAD:3 - Forces

| Force | Tension |
| --- | --- |
| Decision memory | The framework needs durable rationale, but decision memory must not be confused with the framework structure itself. |
| Framework-specific slots | Generic decision patterns carry much of the method, but framework editions add dependency, naming, source-return, publication, and currentness obligations. |
| Lightweight publication | ADR-like records are useful, but their headings do not create the decision relation. |
| Evolution | Framework decisions may become obsolete when sources, Core editions, domain scope, or local use changes. |
| Non-duplication | A child pattern must not repeat `E.9`, `C.32.PAD`, or `C.32.ADR` without adding framework-specific value. |

### E.4.PFAD:4 - Solution

Create one `PrincipleFrameworkArchitectureDecision@Context` relation before publishing the decision through any ADR-like carrier.

```text
PrincipleFrameworkArchitectureDecision@Context:
  frameworkDecisionId
  governedFrameworkRef
  boundedContextRef
  frameworkEditionRef
  fpfCoreEditionRef
  decisionQuestion
  sourceBasisRefs
  sotaSynthesisPackRefs?
  namingDecisionRefs
  selectedPatternSetRefs
  selectedPatternRelationRefs
  publicationUnitRefs
  accessCarrierRefs?
  dependencyAndEditionRefs
  qualityEvaluationRefs
  admissionReviewRefs
  rejectedAlternatives
  rationaleRefs
  consequences
  publicationCarrierRefs?
  sourceReturnConditions
  refreshOrSupersessionConditions
```

Fill the relation in this order:

1. State the decision question as an architecture question about the framework edition.
2. Name the bounded context, governed framework, and FPF Core edition dependency.
3. List the source basis and SoTA synthesis packs that make the decision admissible.
4. Select the pattern set and relation records, or state why the decision is not yet ready.
5. Select the publication or access carrier only after the structure being exposed is clear.
6. Record dependency and edition effects under `E.5.3` and `E.4.PFR`.
7. Record naming decisions or required `F.18` name-card work.
8. Record rejected alternatives, rationale, consequences, quality route, source-return route, and refresh or supersession conditions.
9. Publish the decision projection through `C.32.ADR` or `E.17` only after the decision relation exists.

`qualityEvaluationRefs` and `admissionReviewRefs` are distinct reference families. `qualityEvaluationRefs` point to `E.4.DPF.DA` package adequacy, `E.21` pattern-quality evaluation, or `E.23` improvement evidence. `admissionReviewRefs` point to `E.19` only when the decision is being used to claim admission, profile gating, external-review readiness, or landing readiness.

Demotion condition: if no framework-specific slots are live, do not keep this pattern in play. Use `E.9` for rationale, `C.32.PAD` for project architecture decision structure, and `C.32.ADR` for the publication projection.

### E.4.PFAD:5 - Archetypal Grounding

Tell: A team wants a hydroponic-cucumber domain principle framework. The PFAD decision asks whether the framework depends directly on FPF Core only, or also on an agriculture-domain framework edition; which crop-growth concerns become first patterns; which source packs are strong enough; and which publication or access carrier will expose the framework.

Show: A Codex local practice framework has process patterns for baton handoff and prelanding checks. The decision records that these are local practice framework patterns, not FPF Core patterns. It names the FPF Core edition, selected local process patterns, local publication unit, source-return owners, and refresh conditions.

Show: An ADR-like file saying "accepted: create domain framework" is insufficient. The decision relation must name selected pattern set, dependencies, source basis, rejected alternatives, consequences, and repair conditions before the ADR-like carrier can be trusted as a projection.

Filled decision slice:

```text
PrincipleFrameworkArchitectureDecision@HydroponicCucumberDomain:
  frameworkDecisionId: PFAD-HC-001
  governedFrameworkRef: HydroponicCucumberPrincipleFramework@GreenhouseCropDomain
  boundedContextRef: commercial greenhouse cucumber production
  frameworkEditionRef: HC-DPF-0.1-draft
  fpfCoreEditionRef: FPFCorePatternSet@current
  decisionQuestion: Which first pattern set and relation structure should carry crop-growth architecturing guidance?
  sourceBasisRefs: G2-HC-source-pack, greenhouse-control source notes, accepted FPF ecosystem DRR
  namingDecisionRefs: F18-HC-framework-name-card-required
  selectedPatternSetRefs: problem-framing, nutrient-monitoring, climate-control interpretation, harvest-feedback patterns
  selectedPatternRelationRefs: PFR-HC-source-reuse, PFR-HC-specialization, PFR-HC-publication
  publicationUnitRefs: HC-all-in-one-carrier-readme-and-toc
  accessCarrierRefs: HC-grower-skill-pack-or-MCP-route-if-built
  dependencyAndEditionRefs: depends on FPFCorePatternSet@current; no Core reverse dependency
  qualityEvaluationRefs: E21-HC-first-pattern-evaluation
  admissionReviewRefs: none until admission is claimed
  rejectedAlternatives: land into FPF-Spec.md; publish only a crop checklist
  rationaleRefs: source-pack claim sheet and E.4 family map
  consequences: faster domain guidance; explicit refresh debt when sources or Core edition change
  publicationCarrierRefs: HC-all-in-one-carrier
  accessCarrierRefs: HC-grower-skill-pack-or-MCP-route-if-built
  sourceReturnConditions: return to G.2 when source pack loses a rival horticulture tradition
  refreshOrSupersessionConditions: G.11 refresh when Core edition or greenhouse practice changes
```

### E.4.PFAD:6 - Bias-Annotation

The main drift is carrier-first decision making: a team starts from ADR headings, a status field, or a template and assumes that filling the file has made the decision. The repair is to fill the decision relation first and publish a projection second.

The second drift is child-pattern duplication: PFAD can become a local restatement of generic decision practice. The repair is to keep only the framework-specific slots live and return generic decision work to `E.9`, `C.32.PAD`, and `C.32.ADR`.

### E.4.PFAD:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-PFAD.1 Decision relation exists | A filled `PrincipleFrameworkArchitectureDecision@Context` relation exists before any ADR-like publication is treated as the decision. |
| CC-PFAD.2 Framework-specific slots live | The decision uses at least one framework-specific slot: edition dependency, selected pattern set, relation graph, publication carrier, access carrier, name cards, source-return, quality route, or currentness route. |
| CC-PFAD.3 Generic owners reused | Rationale uses `E.9`; project architecture decision shape uses `C.32.PAD`; publication projection uses `C.32.ADR` or `E.17`. |
| CC-PFAD.4 Alternatives and consequences present | Rejected alternatives, rationale, consequences, and repair or supersession conditions are recoverable. |
| CC-PFAD.5 Source and name routes present | Source packs, source-return conditions, and required name-card work are named. |
| CC-PFAD.6 Quality and admission separated | `E.21` quality evaluation refs and `E.19` admission review refs are separate or explicitly absent. |
| CC-PFAD.7 Demotion checked | If framework-specific obligations are absent, the decision is handled directly by neighboring patterns. |

### E.4.PFAD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| ADR as decision | A publication projection is treated as the decision relation. | Fill `PrincipleFrameworkArchitectureDecision@Context`, then project it through `C.32.ADR` if useful. |
| Template-led selection | Headings decide what evidence is gathered. | Start from the architecture question, source basis, alternatives, selected structures, and consequences. |
| PFAD overgrowth | The pattern repeats generic decision practice. | Demote to `E.9` plus `C.32.PAD` and keep only a relation row if no framework-specific slot is active. |
| Hidden Core change | A domain or local decision silently changes FPF Core meaning. | Record framework family and dependency direction under `E.4` and `E.5.3`. |

### E.4.PFAD:9 - Consequences

PFAD makes framework decisions more inspectable, because a later maintainer can recover the decision question, source basis, selected structures, rejected alternatives, and repair conditions. The cost is an extra decision relation before publication.

The pattern also constrains ADR use. ADR-like records remain useful, but they become projections of a decision relation rather than the place where the ontology is invented.

### E.4.PFAD:10 - Rationale

FPF already has decision, architecture decision, and ADR-projection patterns. The reason PFAD exists is narrower: framework authors repeatedly need the same framework-specific slots that generic decision patterns do not keep visible by default. Those slots are edition dependency, selected pattern set, relation structure, publication carrier, access carrier, source-return, naming, quality route, and currentness route.

PFAD is therefore a specialization by obligation, not by vocabulary. If those obligations are not live, the specialization has no value.

### E.4.PFAD:11 - SoTA-Echoing

| Claim | Exact source ref and status | Pattern locus changed | Adoption status |
| --- | --- | --- | --- |
| Architecture decisions need context, decision, status, consequences, and supersession memory, but the record must not replace the decision relation. | Nygard, `Documenting Architecture Decisions`, 2011 lineage source still current for compact ADR section functions, `https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions`; MADR, maintained template practice, current projection-format source, `https://adr.github.io/madr/`. | `Solution` requires `PrincipleFrameworkArchitectureDecision@Context` before `C.32.ADR` projection; filled decision slice includes rejected alternatives, consequences, and supersession condition. | Adopt section-function memory; adapt by making ADR-like text a projection of a prior FPF relation. |
| Architecture decision records need concern, rationale, and description-boundary discipline. | `ISO/IEC/IEEE 42010:2022`, official current standard ref for architecture-description concepts and architecture-versus-description boundary, `https://www.iso.org/standard/74393.html`. | `Problem frame` says first output is relation, not ADR or realized framework; `Relations` keeps `C.32.PAD` and `C.32.ADR` as owners. | Adopt rationale recovery; adapt to framework selected structures, source-return, and receiving owners. |
| A framework-decision specialization must remain justified by recurring local obligations and near misses. | Riehle, Harutyunyan, Barcomb, `Pattern Discovery and Validation Using Scientific Research Methods`, arXiv:2107.06065, 2021 current validation-practice source. | `Demotion condition`, `Conformance Checklist`, and `Common Anti-Patterns` require PFAD to collapse when framework-specific slots are absent. | Adopt validation pressure; reject a child pattern that only repeats generic decision slots. |
| Compatibility, deprecation, and supersession need impact thinking beyond a label or status field. | `Semantic Versioning 2.0.0`, current-standard compatibility-boundary practice, `https://semver.org/spec/v2.0.0.html`; Chen et al., `Breaking Changes in Software Ecosystems: A Systematic Literature Review`, arXiv:2605.24397, 2026 current SLR, `https://arxiv.org/abs/2605.24397`. | `refreshOrSupersessionConditions`, `dependencyAndEditionRefs`, and `E.4.PFR` relation exits become required PFAD slots. | Adapt compatibility-impact discipline to framework editions; reject software package, build, and binary semantics. |

### E.4.PFAD:12 - Relations

- **Uses:** `E.9` as the rationale kernel for framework-local architecture decisions; it specializes only the recurring framework-specific obligations and does not create a second generic decision ontology.
- **Coordinates with:** `C.32.PAD` for architecture-decision slot discipline.
- **Coordinates with:** `C.32.ADR` and `E.17` for decision publication projections.
- **Coordinates with:** `E.4` for family membership and selected structures.
- **Coordinates with:** `E.4.PFR` for dependency, edition, compatibility, relation, and supersession effects.
- **Coordinates with:** `F.18`, `G.2`, `G.11`, `E.4.DPF.DA`, `E.21`, `E.23`, `C.33`, `C.34`, and `C.35` for name, source, currentness, package adequacy, pattern quality, preservation, and produced-carrier claims.

### E.4.PFAD:End

