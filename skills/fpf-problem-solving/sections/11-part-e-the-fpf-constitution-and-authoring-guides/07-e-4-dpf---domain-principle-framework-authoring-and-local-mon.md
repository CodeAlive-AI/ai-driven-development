## E.4.DPF - Domain Principle Framework Authoring and Local-Monolith Landing

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative.

### E.4.DPF:1 - Problem frame

Use this pattern when a group needs to create a domain principle framework or local practice framework grounded in FPF: for example a hydroponic-cucumber framework, a neural-network architecture framework, or a Codex-process framework.

Primary `EntityOfConcern`: the authoring method for a bounded FPF-grounded framework edition. The first useful output is not a list of candidate pattern names. It is an authoring spine with context, SoTA source pack, architecture decision, name-card route, pattern drafts, relation and edition records, publication unit, quality loop, and currentness route.

Use this pattern when the work creates a framework. Use `E.11` or `E.17` when the work only changes how existing material is exposed to readers.

Plain vocabulary for adoption:

| Public phrase | Use it for |
| --- | --- |
| `principle framework` | The general public phrase for an FPF-grounded framework of patterns, decisions, relation records, source basis, publication, quality, and refresh. |
| `Domain Principle Framework` | A principle framework for a domain such as greenhouse cucumbers, neural-network architecture, or safety certification practice. |
| `Local Practice Framework` | A principle framework for one organization, project, team, role context, or local operating practice. |
| `bounded context` | The domain or local situation where this framework's meanings hold. |
| `framework edition` | One versioned state of the framework with dependency, compatibility, publication, quality, and refresh records. |
| `local monolith` | A publication carrier for local readers, not the framework architecture itself. |

Old intake labels such as `SPF`, `TPF`, or broad `xPF` remain source aliases until `F.18` settles a durable public name and any admissible short form. `ZPF` has a campaign-local `F.18` name card that selects `FoundationalPrinciplePatternSet` / "foundational principle pattern set" as the primary name and keeps `ZPF` only as a mnemonic alias, not as a public "zero principles" framework name.

### E.4.DPF:2 - Problem

Domain and local framework authors often have strong source material and urgent local needs, but they can lose FPF discipline in three ways. They copy FPF terms without settling the domain ontology. They publish a local monolith before deciding the framework architecture. Or they produce a useful checklist that is local process guidance but not yet an FPF-grounded pattern framework.

A working framework needs more than a good table of contents. It needs source-grounded pattern selection, architecture decisions, relation records, edition dependencies, names, worked cases, quality evaluation, and refresh conditions.

### E.4.DPF:3 - Forces

| Force | Tension |
| --- | --- |
| Domain urgency | The local team needs usable guidance soon, but premature durable names and pattern heads freeze poor ontology. |
| Source richness | Domain traditions provide valuable methods and examples, but source summaries can hide rival traditions and lost evidence. |
| FPF reuse | FPF Core gives strong authoring, relation, and quality patterns, but direct copying can mask domain-specific concerns. |
| Publication need | A local monolith helps readers, but it can hide relation, dependency, and currentness records. |
| Evolution | Domain and local frameworks must improve as sources, uses, and Core editions change. |

### E.4.DPF:4 - Solution

Author the framework through a spine whose outputs are inspectable at each step:

First-hour route for a first framework:

1. Write a one-paragraph context note: domain or local context, intended reader, first use, and non-use boundary.
2. Create a source-pack stub: source traditions to inspect, rival traditions to avoid losing, first examples, and claim status.
3. Draft one PFAD question: what framework family is being created, what first pattern set is in scope, what depends on FPF Core, and what must not land in Core.
4. Mark public names provisional: use `Domain Principle Framework` or `Local Practice Framework` in prose, and send durable names or abbreviations to `F.18`.
5. Draft one to three first pattern candidates through `E.8`, each with a recognizable problem frame, positive solution, worked slice, and local anti-pattern.
6. Add relation and edition rows for those candidates: source reuse, specialization, publication, dependency, compatibility, or refresh as needed.
7. Pick the first-entry carrier: local readme, preface, table of contents, card set, or local monolith.
8. Name the first quality and refresh route: what will be evaluated, what can improve next, and what source, Core edition, or local-use change reopens the framework.

Stop the first hour when those outputs exist, even if every pattern body is still rough. A rough framework with context, source basis, decision question, provisional names, first pattern candidates, relation rows, publication carrier, quality route, and refresh trigger is inspectable. A long monolith without those outputs is not yet an FPF-grounded framework.

Prompt-shaped starter for SoTA harvesting and first candidate generation:

```text
Help draft a first FPF-grounded principle-framework candidate.

Bounded context:
Intended reader and first use:
Non-use boundary:
Source traditions to inspect:
Rival traditions or schools not to lose:
Local examples or internal sources:
Adopted source payload to carry into pattern solutions:
Rejected source payload and why rejected:
Candidate first patterns, each with problem frame, positive solution, worked slice, and local anti-pattern:
Candidate relation functions among the patterns:
Dependency on FPF Core or a domain framework edition:
Publication carrier for first entry:
Quality route: which first drafts should be evaluated and improved:
Refresh triggers: source change, Core edition change, local-use telemetry, or policy change:

Return the result as a draft source-pack summary, PFAD question, candidate pattern list, relation-record candidates, publication carrier note, quality-route note, and refresh-trigger note.
Do not present generated text as authoritative. State what must return to `G.2`, `C.35`, `E.4.PFAD`, `E.4.PFR`, `F.18`, `E.21`, and `G.11` before the framework can be relied on.
```

1. **Context declaration.** State the domain or local bounded context, intended reader, first use, and non-use boundary.
2. **Source pack.** Use `G.2` to gather SoTA traditions, claim sheets, examples, source-use decisions, rejected alternatives, and source-currentness notes.
3. **Architecture decision.** Use `E.9` and `E.4.PFAD` to decide purpose, framework family, pattern split, relation structure, publication unit, dependency boundary, and source-return obligations.
4. **Name preparation.** Use `E.10` for kind discipline and `F.18` for durable names before public pattern heads or abbreviations are stabilized.
5. **Carrier admission.** Use `C.33`, `C.34`, or `C.35` before relying on local monoliths, tables of contents, relation graphs, source summaries, search outputs, transformed views, or generated candidates as architecture evidence.
6. **Pattern drafting.** Draft patterns with `E.8`: recognition text, positive solution, worked cases, boundary, local anti-patterns, SoTA-Echoing, conformance checks, and relations.
7. **Relation and edition discipline.** Use `E.4.PFR` for relation functions, dependency direction, compatibility boundary, deprecation, supersession, and edition effects.
8. **Quality cycle.** Use `E.22` to frame the evaluation purpose, quality floor, trade-off question, and expected improvement proposal when that frame is not already scoped. Use `E.21` to evaluate pattern quality, `E.23` for repeated improvement, and `E.19` only when admission or profile gating is actually being claimed. If an evaluation result needs a carrier, publish or refresh that carrier through the direct publication or currentness owner rather than through `E.22`.
9. **Admission review.** Use `E.19` when the local process asks whether a pattern or framework slice is ready for admission.
10. **Local monolith landing.** Publish the framework in its own local monolith, readme, preface, table of contents, or equivalent first-entry carrier. Do not land domain or local frameworks into `FPF-Spec.md` by default.
11. **Currentness route.** Use `G.11` for refresh plans, edition pins, source decay, deprecation, and supersession conditions.

Starter evaluation characteristics for a principle-framework improvement loop:

| Characteristic question | Direct owner to use |
| --- | --- |
| Discoverability | Can the intended reader find the first useful entry and governing pattern? Use `E.11`, then evaluate the pattern or projection through the applicable quality owner. |
| Source fidelity | Are adopted and rejected source payloads recoverable in source packs, solutions, boundaries, and examples? Use `G.2`, `C.33`, `C.34`, and pattern-quality evaluation. |
| Ontology clarity | Are Core, domain, local, publication, source, decision, relation, quality, and refresh claims kept as different kinds? Use `E.10`, `F.18`, `F.19`, and the direct owner. |
| Relation typedness | Are pattern-use, specialization, dependency, publication, preservation, quality, and source-use relations separated? Use `E.4.PFR`. |
| Compatibility impact | Can maintainers see what breaks or must migrate when Core, domain, or local editions change? Use `E.4.PFR`, `E.5.3`, and `G.11`. |
| Refreshability | Are source decay, edition pins, local-use telemetry, and supersession conditions actionable? Use `G.11`. |
| Package navigability | Can the selected pattern set, relation records, source packs, decision records, quality evidence, and first-entry carrier be found without treating the package as runtime machinery? Use `G.5`, `E.4.PFR`, and `E.11`. |
| Adoption telemetry | Are repeated reader errors, skipped records, stale sources, and local-use failures routed to refresh or improvement? Use `G.11` and `E.23`. |
| Didactic first use | Can a first-time domain or local author write the first useful output without prior FPF developer knowledge? Use `E.11`, `E.12`, `E.21`, and `E.23`. |

These are evaluation characteristics for selecting and framing improvement work. They are not measurement programs by themselves. If the pass needs a measurement, eval, evidence, or adequacy record, create it through the pattern that owns that object, such as `E.21`, `E.9.DA`, `E.2.DA`, `C.16`, `A.10`, or the relevant architecture-characteristic pattern.

The spine is complete only when a reader can answer: what framework edition is being authored, which sources and decisions shaped it, which patterns and relations were selected, where it is published, how quality improves, and when it returns for refresh or repair.

### E.4.DPF:5 - Archetypal Grounding

Tell: A hydroponic-cucumber framework begins with crop-production concerns, horticulture and greenhouse-control sources, local examples, and FPF Core dependency. Its first local monolith is a publication unit for domain users, while relation records, source packs, and quality evaluations remain separately recoverable.

Show: A neural-network architecture framework may draw on dataflow architecture, model components, training and inference concerns, evaluation practice, and recent architecture-analysis work. The framework can describe layers, blocks, flows, optimization constraints, and interpretability concerns, but each pattern must still be grounded through `G.2`, drafted through `E.8`, and related through `E.4.PFR`.

Show: A workspace-specific Codex process framework can contain prelanding and baton-handoff patterns. It should state its local context, dependency on FPF Core, process sources, local carriers, and refresh route. A useful local checklist stays a local checklist until it has source grounding, pattern bodies, relation records, and quality evaluation.

Show: An enterprise local practice framework for architecture review starts from the organization's review context, internal policies, proprietary examples, and approval path. It can depend on FPF Core and on a domain principle framework, but its confidential evidence, role assignments, training plan, and rollout telemetry stay local.

Enterprise local-practice slice:

| Output | Enterprise question |
| --- | --- |
| Local context | Which organization, product line, team, role context, and decision class is governed? |
| Internal sources | Which policies, standards, review records, incidents, templates, and examples are adopted or rejected? |
| Constraints | Which regulatory, confidentiality, intellectual-property, tool-access, and security boundaries constrain publication? |
| Owners | Which steward owns the framework edition, source pack, relation records, local monolith, and refresh plan? |
| Approval route | Which management, engineering, safety, legal, or assurance reviews are needed before local use? |
| Rollout and training | Which roles need first-use examples, training material, and migration support? |
| Dependency | Which FPF Core edition and domain framework edition are depended on, and which reverse dependency is blocked? |
| Migration | What changes after FPF Core edition change, domain-framework edition change, policy change, or repeated local misuse? |
| Adoption telemetry | Which reader errors, skipped relation records, stale source packs, or quality regressions trigger `G.11` refresh? |

Replayable authoring slice:

| Authoring output | Filled slice |
| --- | --- |
| Context declaration | `GreenhouseCropDomain`, intended reader: crop-system architect and senior grower; first use: decide first pattern set for cucumber production guidance |
| `G.2` source pack | greenhouse climate-control sources, crop nutrition sources, local production logs; rejected source: generic gardening advice without controlled-environment evidence |
| Architecture decision | `PFAD-HC-001` selects four first patterns, local monolith carrier, FPF Core dependency, and no Core landing |
| Naming route | provisional `HydroponicCucumberPrincipleFramework`; `F.18` name card required before public abbreviation |
| First pattern draft | `HC.NutrientMonitoring` drafted with `E.8`: problem frame, solution, worked greenhouse slice, SoTA row, conformance checks |
| Relation and edition record | `PFR-HC-source-reuse` links nutrient pattern to source pack; dependency record points to `FPFCorePatternSet@current` |
| Quality cycle | `E.22` frames evaluation purpose; `E.21` scores first draft; `E.23` records the next improvement loop |
| Local publication | local monolith readme and table of contents expose the framework after source-return notes are present |
| Refresh route | `G.11` refresh when source pack, Core edition, or greenhouse-control practice changes |

### E.4.DPF:6 - Bias-Annotation

The first drift is source-summary confidence: a summary feels sufficient because it names the right domain terms. The repair is to turn sources into a `G.2` source pack with adopted and rejected payload, then carry that payload into pattern solutions and examples.

The second drift is monolith-first authoring. The repair is not to delay publication forever; it is to publish after the architecture decision, relation records, and source-return notes are recoverable.

### E.4.DPF:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-DPF.1 Context declared | Domain or local bounded context, intended reader, first use, and non-use boundary are named. |
| CC-DPF.2 Source pack present | `G.2` source basis includes adopted payload, rejected alternatives, examples, claim status, and currentness notes. |
| CC-DPF.3 Architecture decision present | `E.4.PFAD` or direct `E.9` plus `C.32.PAD` records purpose, pattern split, relation structure, publication unit, dependency boundary, and consequences. |
| CC-DPF.4 Names prepared | Durable public names and abbreviations have `F.18` name-card work or are explicitly provisional source aliases. |
| CC-DPF.5 Carriers admitted | Any monolith, graph, generated set, source summary, or transformed view used as evidence has `C.33`, `C.34`, or `C.35` treatment. |
| CC-DPF.6 Patterns drafted through E.8 | Pattern bodies carry recognition text, positive solution, worked cases, local anti-patterns, checklist, SoTA-Echoing, and relations. |
| CC-DPF.7 Quality and refresh routes present | `E.22` frames evaluation purpose when needed; `E.21`, `E.23`, and `G.11` routes are named with edition or refresh conditions. |

### E.4.DPF:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Checklist promoted to framework | Local tips are published as a principle framework without source, relation, or quality work. | Treat the checklist as local process text until `G.2`, `E.8`, `E.4.PFR`, and `E.21` are satisfied. |
| Source summary as SoTA | A literature summary replaces adopted and rejected source payload. | Build a `G.2` source pack and carry each load-bearing source into solution, boundary, or example text. |
| Local monolith as architecture | The publication unit hides relation and dependency records. | Add `E.4.PFAD`, `E.4.PFR`, and source-return records before relying on the monolith as architecture evidence. |
| Generated candidate authority | Search or LLM output becomes the framework because it is fluent. | Use `C.35` for admission, then decide candidate selection through `E.4.PFAD` or `C.32`. |

Adoption risk tripwires:

| Risk | Early repair |
| --- | --- |
| Public name settles before the kind is settled. | Keep the intake name as a source alias and route durable naming through `F.18`. |
| Generated or searched material is trusted because it uses familiar FPF words. | Admit the carrier through `C.35`, then decide selected use through `E.4.PFAD`, `E.4.PFR`, or the direct pattern owner. |
| Core, domain, or local edition changes but old users keep following stale guidance. | Add dependency, compatibility, migration, deprecation, supersession, and refresh records through `E.4.PFR` and `G.11`. |
| Enterprise evidence is confidential or proprietary. | Publish a safe local carrier while keeping internal source packs, examples, role assignments, and approval evidence under the local owner. |
| No owner can answer whether the framework is current, adopted, or broken in use. | Name owners for framework edition, source pack, relation records, local publication, quality evidence, and refresh plan. |
| Reader errors and skipped records are treated as training noise. | Treat repeated misuse as adoption telemetry and route it to `E.23` improvement or `G.11` refresh. |
| Compatibility debt hides behind a version label or package manifest. | Record the impacted relations, compatibility boundary, migration work, and blocked runtime or build reading in `E.4.PFR`. |

### E.4.DPF:9 - Consequences

The authoring spine adds overhead before a local framework becomes durable. That overhead prevents hidden source loss, hidden Core change, hidden relation semantics, and hidden currentness debt.

The pattern also makes local publication more useful. Readers get a coherent local monolith or first-entry carrier, while maintainers can still inspect the framework edition, source pack, relation records, decision records, and quality route.

### E.4.DPF:10 - Rationale

Domain and local frameworks are not mere subsets of FPF. They are FPF-grounded framework editions in bounded contexts. They need domain source work, FPF authoring discipline, architecture decisions, relation records, quality loops, and refresh routes.

The pattern keeps the work practical by using existing FPF owners instead of inventing a second framework-development ontology. Its contribution is the ordered spine and the requirement that each produced artifact has a receiving owner.

### E.4.DPF:11 - SoTA-Echoing

| Claim | Exact source ref and status | Pattern locus changed | Adoption status |
| --- | --- | --- | --- |
| Domain-tailored frameworks need co-evolving ontology, examples, usability, and evaluation rather than only a term list. | Zhang, Struber, Hebig, `Development and Evolution of Xtext-based DSLs on GitHub: An Empirical Investigation`, arXiv:2501.19222, 2025 current empirical DSL-evolution source, `https://arxiv.org/abs/2501.19222`. | `Solution` requires context declaration, source pack, name preparation, carrier admission, and pattern drafting; `Common Anti-Patterns` blocks checklist promotion and source-summary substitution. | Adapt co-evolution discipline to FPF framework authoring; reject grammar, parser, metamodel, or code-generator ontology unless a framework deliberately specifies a language. |
| Reusable core and domain variation require explicit family and dependency work. | Nazar, `Software Product Line Engineering: Adoption, Tooling and AI Era Challenges`, arXiv:2605.21353, 2026 current survey and reopen trigger for stronger future SPLE synthesis, `https://arxiv.org/abs/2605.21353`. | `Solution` steps for architecture decision, relation and edition discipline, and local monolith landing keep Core, domain framework, and local framework separate. | Adapt domain-engineering and reusable-core discipline; reject software-product feature-model ontology as FPF default. |
| Pattern bodies need condition-based use, examples, validation, and improvement loops. | Riehle, Harutyunyan, Barcomb, `Pattern Discovery and Validation Using Scientific Research Methods`, arXiv:2107.06065, 2021 current validation-practice source; Iba, `Pattern Languages as Media for the Creative Society`, arXiv:1308.1178, lineage for pattern languages as practice media. | `Solution` step 6 requires `E.8` pattern drafting; replayable authoring slice shows source pack to pattern draft to quality cycle; `Checklist` requires `E.22`, `E.21`, `E.23`, and `G.11` routes. | Adopt validation and worked-example pressure; adapt through FPF quality and improvement owners. |
| Architecture-description carriers help authoring only when their captured and lost structure is explicit. | `ISO/IEC/IEEE 42010:2022`, current official architecture-description standard ref, `https://www.iso.org/standard/74393.html`. | `Carrier admission` step and `Local monolith as architecture` anti-pattern require `C.33`, `C.34`, or `C.35` treatment before carriers seed architecture decisions. | Adopt architecture-description boundary discipline; adapt source-return and admission to FPF carriers. |

### E.4.DPF:12 - Relations

- **Uses:** `G.2` for source pack and SoTA synthesis.
- **Uses:** `E.8`, `E.10`, and `F.18` for pattern drafting, kind discipline, and names.
- **Coordinates with:** `E.4` for family membership and `E.4.PFAD` for architecture decisions.
- **Coordinates with:** `E.4.PFR` for relation, dependency, edition, compatibility, deprecation, and supersession records.
- **Coordinates with:** `C.33`, `C.34`, and `C.35` for carrier preservation and admission.
- **Coordinates with:** `E.22` for quality-evaluation framing when needed, `E.21` for pattern-quality evaluation, `E.23` for repeated improvement, `E.19` for admission or profile gating when claimed, and `G.11` for currentness.
- **Exits to:** `E.11` and `E.17` when the live problem is publication or first-entry discoverability rather than framework authoring.

### E.4.DPF:End

