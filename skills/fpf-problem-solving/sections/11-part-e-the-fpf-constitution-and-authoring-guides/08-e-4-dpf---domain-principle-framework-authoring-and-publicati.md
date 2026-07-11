## E.4.DPF - Domain Principle Framework Authoring and Publication-or-Access Carrier Assembly

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative.

### E.4.DPF:1 - Problem frame

Use this pattern when a group needs to create a domain principle framework or local practice framework grounded in FPF: for example a hydroponic-cucumber framework, a neural-network architecture framework, or a Codex-process framework.

Primary `EntityOfConcern`: the authoring method for a bounded FPF-grounded framework edition. The first useful output is not a list of candidate pattern names. It is an authoring spine with context, SoTA source pack, architecture decision, name-card route, pattern drafts, relation and edition records, publication carrier, access carrier, quality loop, and currentness route.

Default artifact contract for a request such as "make a DPF about this topic" separates developer and user carriers. In a campaign or repository setting, create a developer decision carrier such as `SUBSTANTIVE-DRR.md` or `DPF-DRR.md` governed by `E.9` and checked by `E.9.DA`; it carries the source basis, selected architecture, PFAD decision, candidate pattern split, relation plan, quality plan, and rejected alternatives. Create a user-facing framework publication or access carrier named by the individual framework, such as `<DomainOrPractice>-PRINCIPLES-FRAMEWORK.md`, `<PublicFrameworkName>.md`, a split readme, pattern, and appendix set, a skill pack, or an MCP-backed access service; it is the access route through which readers or agents use the DPF edition. Optional source-pack, PFR, quality-run, package-evaluation, skill-manifest, or access-service files may be separate when they need independent maintenance, but they must not be copied into the user carrier as process state.

Use this pattern when the work creates a framework. Use `E.11` or `E.17` when the work only changes how existing material is exposed to readers.

Plain vocabulary for adoption:

| Public phrase | Use it for |
| --- | --- |
| `principle framework` | The general public phrase for an FPF-grounded framework of patterns, decisions, relation records, source basis, publication, quality, and refresh. |
| `Domain Principle Framework` | A principle framework for a domain such as greenhouse cucumbers, neural-network architecture, or safety certification practice. |
| `Local Practice Framework` | A principle framework for one organization, project, team, role context, or local operating practice. |
| `bounded context` | The domain or local situation where this framework's meanings hold. |
| `framework edition` | One versioned state of the framework with dependency, compatibility, publication, quality, and refresh records. |
| `framework publication carrier` | A reader-facing carrier for a framework edition: readme, preface, table of contents, pattern bodies, support maps, relation records, and refresh route as needed. |
| `framework access carrier` | A user-facing or agent-facing access carrier for a framework edition: all-in-one publication carrier, split document set, card set, skill pack, MCP-backed access service, retrieval route, or assistant integration. It exposes the selected framework edition; it does not define the framework architecture, source pack, quality result, runtime dependency, or work authority by itself. |
| `local monolith` | Workspace and editorial shorthand for one all-in-one framework publication carrier. Do not use it as the public framework name, and do not treat it as the framework architecture itself. |

Old intake labels such as `SPF`, `TPF`, or broad `xPF` remain source aliases until `F.18` settles a durable public name and any admissible short form. `ZPF` has a campaign-local `F.18` name card that selects `FoundationalPrinciplePatternSet` / "foundational principle pattern set" as the primary name and keeps `ZPF` only as a mnemonic alias, not as a public "zero principles" framework name.

### E.4.DPF:2 - Problem

Domain and local framework authors often have strong source material and urgent local needs, but they can lose FPF discipline in three ways. They copy FPF terms without settling the domain ontology. They publish a framework carrier before deciding the framework architecture. Or they produce a useful checklist that is local process guidance but not yet an FPF-grounded pattern framework.

A working framework needs more than a good table of contents. It needs source-grounded pattern selection, architecture decisions, relation records, edition dependencies, names, worked cases, quality evaluation, and refresh conditions.

A DPF is not a domain ontology, glossary, literature survey, or guide to talking about a topic. It exists so an intended practitioner or assisting agent can enter typical problem situations in the domain, avoid known failure modes, and apply source-grounded SoTA solution moves with visible boundaries and refresh conditions. Those failure modes include beginner mistakes and experienced-practitioner failures caused by stale, local-only, or non-SoTA practice. Ontology and vocabulary matter only insofar as they make those problem-solving moves safer and more reusable.

### E.4.DPF:3 - Forces

| Force | Tension |
| --- | --- |
| Domain urgency | The local team needs usable guidance soon, but premature durable names and pattern heads freeze poor ontology. |
| Source richness | Domain traditions provide valuable methods and examples, but source summaries can hide rival traditions and lost evidence. |
| Problem-solving primacy | A DPF may need terms and ontology, but those are supports for recognizing recurring domain problems and choosing SoTA solution moves, not the framework's payoff by themselves. |
| FPF reuse | FPF Core gives strong authoring, relation, and quality patterns, but direct copying can mask domain-specific concerns. |
| Publication need | A framework publication carrier helps readers, but it can hide relation, dependency, and currentness records. |
| Evolution | Domain and local frameworks must improve as sources, uses, and Core editions change. |

### E.4.DPF:4 - Solution

Author the framework through a spine whose outputs are inspectable at each step:

First-hour route for a first framework:

1. Write a one-paragraph context note: domain or local context, intended reader, first use, and non-use boundary.
2. Create a source-pack stub: source traditions to inspect, rival traditions to avoid losing, first examples, and claim status.
3. Draft one PFAD question: what framework family is being created, which domain or local problem-situation architecture and solution-move architecture the first pattern set will render, what depends on FPF Core, and what must not land in Core.
4. Mark public names provisional: use `Domain Principle Framework` or `Local Practice Framework` in prose, and send durable names or abbreviations to `F.18`.
5. Draft one to three first pattern candidates through `E.8`, each with a recognizable problem frame, known failure mode or local anti-pattern, positive SoTA-informed solution move, worked slice, and boundary. In the first hour these are pattern seeds unless they already pass the declared `E.21` pattern-quality use.
6. Add relation and edition rows for those candidates: source reuse, specialization, publication, dependency, compatibility, or refresh as needed.
7. Pick the first-entry and publication or access carrier: readme, preface, table of contents, card set, all-in-one local carrier, split document set, skill pack, MCP-backed access service, or another access face.
8. Name the first quality and refresh route: what will be evaluated, what can improve next, and what source, Core edition, or local-use change reopens the framework.

Stop the first hour when those outputs exist, even if every pattern body is still rough. A rough framework with context, source basis, decision question, provisional names, first pattern candidates, relation rows, publication carrier, quality route, and refresh trigger is inspectable. A long all-in-one carrier without those outputs is not yet an FPF-grounded framework. Do not promote this rough output to a reliance-bearing DPF publication carrier until the DRR or decision carrier is checked for the intended authoring use, the pattern bodies are hardened as normal FPF patterns, and the package is evaluated through `E.4.DPF.DA`.

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
Recurring domain or local problem situations and forces:
Reusable solution moves and consequences:
Candidate first patterns, each with problem frame, positive solution, worked slice, and local anti-pattern:
Candidate relation functions among the patterns:
Dependency on FPF Core or a domain framework edition:
Publication or access carrier for first entry:
Quality route: which first drafts should be evaluated and improved:
Refresh triggers: source change, Core edition change, local-use telemetry, or policy change:

Return the result as a draft source-pack summary, PFAD question, candidate pattern list, relation-record candidates, publication or access carrier note, quality-route note, and refresh-trigger note. If the requester wants a ready DPF rather than a seed, return the developer DRR or decision carrier and the user DPF publication or access carrier as separate artifacts or clearly separated sections, then name which `E.21`, `E.4.DPF.DA`, and refresh checks remain before reliance.
Do not present generated text as authoritative. State what must return to `G.2`, `C.35`, `E.4.PFAD`, `E.4.PFR`, `F.18`, `E.21`, and `G.11` before the framework can be relied on.
```

1. **Context declaration.** State the domain or local bounded context, intended reader, first use, and non-use boundary.
2. **Source pack.** Use `G.2` to gather SoTA traditions, claim sheets, examples, source-use decisions, rejected alternatives, and source-currentness notes.
3. **Architecture decision.** Use `E.9` and `E.4.PFAD` to decide purpose, framework family, domain or local problem-and-solution architecture, pattern split, relation structure, publication carrier, access carrier, dependency boundary, and source-return obligations.
4. **Name preparation.** Use `E.10` for kind discipline and `F.18` for durable names before public pattern heads or abbreviations are stabilized.
5. **Carrier admission.** Use `C.33`, `C.34`, or `C.35` before relying on all-in-one carriers, tables of contents, relation graphs, source summaries, search outputs, transformed views, or generated candidates as architecture evidence.
6. **Pattern drafting.** Draft patterns with `E.8`: recognition text, positive solution, worked cases, boundary, local anti-patterns, SoTA-Echoing, conformance checks, and relations. In a DPF, those pattern bodies are the pattern-language rendering of selected domain or local problem-situation architecture and solution-move architecture. `E.8` means a normal action-guiding pattern body, not only a section skeleton. A thin skeleton, prompt seed, or compressed design note remains a pattern seed until `E.21` says it is adequate for the declared DPF use.
7. **Relation and edition discipline.** Use `E.4.PFR` for relation functions, dependency direction, compatibility boundary, deprecation, supersession, and edition effects.
8. **Quality cycle.** Use `E.22` to frame the evaluation purpose, quality floor, trade-off question, and expected improvement proposal when that frame is not already scoped. Use `E.4.DPF.DA` to evaluate the package as a DPF or local-framework package, `E.21` to evaluate individual pattern quality, `E.23` for repeated improvement, and `E.19` only when admission or profile gating is actually being claimed. If an evaluation result needs a carrier, publish or refresh that carrier through the direct publication or currentness owner rather than through `E.22`.
9. **Admission review.** Use `E.19` when the local process asks whether a pattern or framework slice is ready for admission.
10. **Framework publication-or-access carrier assembly.** Publish or expose the framework in its own DPF or local-framework carrier: all-in-one local carrier, split readme, preface, and pattern files, table of contents, cards, skill pack, MCP-backed access service, retrieval route, or another first-entry form. Do not land domain or local frameworks into `FPF-Spec.md` by default.
11. **Currentness route.** Use `G.11` for refresh plans, edition pins, source decay, deprecation, and supersession conditions.

For an all-in-one DPF publication carrier, assemble the content in a reproducible order. This order is a publication shape, not a new framework kind:

1. Public framework title and package edition ref: use a domain- or practice-specific framework name such as `<DomainOrPractice> Principles Framework`; `Principles Framework` alone is only the head or kind phrase, not an individual framework name. Do not put `local monolith`, `draft`, process status, or file-layout slang in the public title.
2. Dependency declaration: FPF Core edition, depended-on DPF or local-framework editions, and blocked reverse dependency.
3. Table of contents: pattern bodies first as the main language of use; support maps and relation records reachable but not front-loaded as required reading.
4. Readme or first practical entries: intended reader, first use, non-use boundary, first outputs, and a short statement of which selected domain or local structures this carrier exposes for that reader.
5. Preface or framework context: cross-cutting ideas that make the pattern set cohere, plus the selected structure families the carrier foregrounds, deliberately coarsens, defers, or sends back to sources and pattern bodies.
6. Package carrier structure-account: intended reader and use, selected source-structure denominator, recurring problem-situation structures, reusable solution-move structures, captured structure, deliberately coarsened, abstracted, omitted, or lost structure, source-return condition, and quality or epiplexity route. This may be a short subsection in the readme or preface when the carrier is compact.
7. Package boundary and owner routing: Core owners reused, local terms bounded, and source, evidence, assurance, publication, and refresh exits named.
8. Pattern index: pattern ids, titles, first use, and any local prefix discipline.
9. Pattern bodies: each drafted through `E.8`, with recognition text, positive solution, worked cases, local anti-patterns, SoTA-Echoing, conformance checks, and relations, and each evaluated or explicitly marked as a seed under `E.21` before the package is claimed for public, teaching, enterprise, or reliance-bearing use.
10. Heterogeneous acceptance cases or transfer probes: examples that force the pattern set to work across unlike uses rather than only repeating the motivating case.
11. Support maps or appendices: architecture bridge, source-use map, precision map, package-name route, or other reference material placed after pattern bodies unless a short front-door trigger table is needed.
12. Source use and refresh map: source rows with adopted payload, rejected or bounded readings, currentness triggers, and `G.2`/`G.11` return conditions.
13. Pattern-framework relation and edition records: `E.4.PFR` rows for dependency, specialization, publication, source reuse, evaluation, generated-carrier, teaching publication-carrier, ethics, deprecation, or supersession relations.
14. Refresh route: what returns to source, pattern quality, package adequacy, edition dependency, or publication carrier when source, Core edition, local use, telemetry, or evaluation changes.
Every DPF publication or access carrier bears or serves a publication/access expression that makes selected domain or local structures available for a declared reader and use; the carrier is not itself the framework edition, the domain, or a narrative by type. In an all-in-one publication carrier, the readme and preface usually carry the first explanatory route, and sometimes a narrative rendering, through the domain. They must therefore say what they are telling, for whom, which structures they foreground, which structures are deliberately coarsened, abstracted, omitted, or left to source return, and where a reader returns for fuller pattern, source, evidence, or relation detail. This is not only text-to-text summarization: the source-bearing side may be actual or possible holon structure, an architecture description, a view, a source pack, a model, a graph, or a pattern set. In architecture-mediated narrative-rendering use, read the return chain as `narrative rendering carried by a publication or access carrier -> architecture description or view -> architecture as selected structures in context -> wider source structures`. When no narrative rendering is present, read the first step as `framework publication or access carrier -> selected source structures`. Each step has selected structure, captured structure, coarsening, abstraction, omission, loss, and return conditions. An architecture description is often already a coarsened representation of selected real, expected, candidate, or actual structures, so the DPF carrier must not hide that second-step loss. This does not make every DPF a literary narrative or make every carrier a narrative; it makes the publication/access representation relation inspectable. When a sequential narrative rendering is load-bearing, use `A.6.3.NAR`; when the publication expression deliberately keeps only a narrower-use coarsened rendering, use `A.6.3.CSC`; for structure capture and loss, use `C.33`; for same-enough or preservation claims, use `C.34`; for first-entry publication, use `E.11` and `E.17`; for package adequacy, use `E.4.DPF.DA`.

Keep process state out of the carrier. DRR text, handoff notes, ledger rows, review status, helper state, admission blockers, and landing evidence may shape the package, but the publication carrier should contain only durable user-facing package content, source-use boundaries, relation records, quality routes, and refresh conditions. A short source-use or relation record may appear in the user carrier when it helps readers and maintainers use the DPF; a DRR argument, review transcript, or quality proof does not.

For skill packs and MCP-backed access, keep the same framework edition identity and relation records visible. A skill or endpoint may help a user find, select, retrieve, render, or apply DPF patterns, but it is an access carrier until another governing pattern makes a stronger claim. If the carrier generates candidate text, use `C.35`; if it performs work or triggers tools, use `A.15` and the local tool or work owner; if it claims currentness, evidence, assurance, or decision authority, use `G.11`, `A.10`, `B.3`, `E.9`, or the direct owner. Do not read a skill manifest, MCP tool name, endpoint schema, or protocol route as the DPF architecture.

Starter evaluation characteristics for a principle-framework improvement loop:

| Characteristic question | Direct owner to use |
| --- | --- |
| Discoverability | Can the intended reader find the first useful entry and governing pattern? Use `E.11`, then evaluate the pattern or projection through the applicable quality owner. |
| Source fidelity | Are adopted and rejected source payloads recoverable in source packs, solutions, boundaries, and examples? Use `G.2`, `C.33`, `C.34`, and pattern-quality evaluation. |
| Ontology clarity | Are Core, domain, local, publication, source, decision, relation, quality, and refresh claims kept as different kinds? Use `E.10`, `F.18`, `F.19`, and the direct owner. |
| Relation typedness | Are pattern-use, specialization, dependency, publication, preservation, quality, and source-use relations separated? Use `E.4.PFR`. |
| Compatibility impact | Can maintainers see what breaks or must migrate when Core, domain, or local editions change? Use `E.4.PFR`, `E.5.3`, and `G.11`. |
| Refreshability | Are source decay, edition pins, local-use telemetry, and supersession conditions actionable? Use `G.11`. |
| Package navigability | Can the selected pattern set, relation records, source packs, decision records, quality evidence, and first-entry or access carrier be found without treating the package as runtime machinery? Use `G.5`, `E.4.PFR`, and `E.11`. |
| Adoption telemetry | Are repeated reader errors, skipped records, stale sources, and local-use failures routed to refresh or improvement? Use `G.11` and `E.23`. |
| Didactic first use | Can a first-time domain or local author write the first useful output without prior FPF developer knowledge? Use `E.11`, `E.12`, `E.21`, and `E.23`. |

These are evaluation characteristics for selecting and framing improvement work. They are not measurement programs by themselves. If the pass needs a DPF package adequacy result, use `E.4.DPF.DA`; if it needs individual pattern quality, use `E.21`; if it needs DRR adequacy, FPF-level Pillar adequacy, measurement, evidence, or architecture-characteristic evaluation, use the pattern that owns that object, such as `E.9.DA`, `E.2.DA`, `C.16`, `A.10`, or the relevant architecture-characteristic pattern.

The spine is complete only when a reader can answer: what framework edition is being authored, what problem-and-solution architecture it renders, which sources and decisions shaped it, which patterns and relations were selected, where it is published, how quality improves, and when it returns for refresh or repair.

### E.4.DPF:5 - Archetypal Grounding

Tell: A hydroponic-cucumber framework begins with crop-production concerns, horticulture and greenhouse-control sources, local examples, and FPF Core dependency. Its first all-in-one publication carrier is for domain users, while relation records, source packs, and quality evaluations remain separately recoverable.

Show: A neural-network architecture framework may draw on dataflow architecture, model components, training and inference concerns, evaluation practice, and recent architecture-analysis work. The framework can describe layers, blocks, flows, optimization constraints, and interpretability concerns, but each pattern must still be grounded through `G.2`, drafted through `E.8`, and related through `E.4.PFR`.

Show: A workspace-specific Codex process framework can contain prelanding and baton-handoff patterns. It should state its local context, dependency on FPF Core, process sources, local carriers, and refresh route. A useful local checklist stays a local checklist until it has source grounding, pattern bodies, relation records, and quality evaluation.

Show: An enterprise local practice framework for architecture review starts from the organization's review context, internal policies, proprietary examples, and approval path. It can depend on FPF Core and on a domain principle framework, but its confidential evidence, role assignments, training plan, and rollout telemetry stay local.

Enterprise local-practice slice:

| Output | Enterprise question |
| --- | --- |
| Local context | Which organization, product line, team, role context, and decision class is governed? |
| Internal sources | Which policies, standards, review records, incidents, templates, and examples are adopted or rejected? |
| Constraints | Which regulatory, confidentiality, intellectual-property, tool-access, and security boundaries constrain publication? |
| Owners | Which steward owns the framework edition, source pack, relation records, publication or access carrier, and refresh plan? |
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
| Architecture decision | `PFAD-HC-001` selects four first patterns, publication or access carrier, FPF Core dependency, and no Core landing |
| Naming route | provisional `HydroponicCucumberPrincipleFramework`; `F.18` name card required before public abbreviation |
| First pattern draft | `HC.NutrientMonitoring` drafted with `E.8`: problem frame, solution, worked greenhouse slice, SoTA row, conformance checks |
| Relation and edition record | `PFR-HC-source-reuse` links nutrient pattern to source pack; dependency record points to `FPFCorePatternSet@current` |
| Quality cycle | `E.22` frames evaluation purpose; `E.21` scores first draft; `E.23` records the next improvement loop |
| Local publication or access | framework readme, table of contents, skill pack, or MCP-backed access route exposes the framework after source-return notes are present |
| Refresh route | `G.11` refresh when source pack, Core edition, or greenhouse-control practice changes |

### E.4.DPF:6 - Bias-Annotation

The first drift is source-summary confidence: a summary feels sufficient because it names the right domain terms. The repair is to turn sources into a `G.2` source pack with adopted and rejected payload, then carry that payload into pattern solutions and examples.

The second drift is publication-carrier-first authoring. The repair is not to delay publication forever; it is to publish after the architecture decision, relation records, and source-return notes are recoverable.

### E.4.DPF:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-DPF.1 Context declared | Domain or local bounded context, intended reader, first use, and non-use boundary are named. |
| CC-DPF.2 Source pack present | `G.2` source basis includes adopted payload, rejected alternatives, examples, claim status, and currentness notes. |
| CC-DPF.3 Architecture decision present | `E.4.PFAD` or direct `E.9` plus `C.32.PAD` records purpose, domain or local problem-and-solution architecture, pattern split, relation structure, publication or access unit, dependency boundary, and consequences. |
| CC-DPF.4 Names prepared | Durable public names and abbreviations have `F.18` name-card work or are explicitly provisional source aliases. |
| CC-DPF.5 Carriers admitted | Any all-in-one carrier, skill pack, MCP-backed access route, graph, generated set, source summary, or transformed view used as evidence has `C.33`, `C.34`, or `C.35` treatment. |
| CC-DPF.6 Patterns drafted through E.8 | Pattern bodies carry recognition text for recurring domain or local problem situations, positive SoTA-informed solution moves, worked cases, known failure modes or local anti-patterns, checklist, SoTA-Echoing, and relations. Skeletons, prompt seeds, and compressed design notes are named as seeds rather than treated as normal DPF patterns. |
| CC-DPF.7 Quality and refresh routes present | `E.22` frames evaluation purpose when needed; `E.4.DPF.DA` package adequacy, `E.21` pattern quality, `E.23` improvement, and `G.11` refresh routes are named with edition or refresh conditions. Public, teaching, enterprise, or reliance-bearing DPF publication names the checked pattern-quality basis or remains `seedOnly`. |
| CC-DPF.8 Carrier structure-account visible | Readme, Preface, or equivalent first-entry carrier says which domain or local problem-and-solution structures the framework exposes, for whom, what is foregrounded, deliberately coarsened, abstracted, omitted, deferred, or lost, and where source, pattern, evidence, or relation return happens. |
| CC-DPF.9 Problem-solving primacy | The DPF tells which typical domain or local problems it helps solve, which known failure modes it blocks, and which source-grounded SoTA solution moves it offers. If it mainly provides vocabulary, ontology, commentary, or conversation guidance, it is not yet a reliance-bearing DPF. |

### E.4.DPF:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Checklist promoted to framework | Local tips are published as a principle framework without source, relation, or quality work. | Treat the checklist as local process text until `G.2`, `E.8`, `E.4.PFR`, and `E.21` are satisfied. |
| Source summary as SoTA | A literature summary replaces adopted and rejected source payload. | Build a `G.2` source pack and carry each load-bearing source into solution, boundary, or example text. |
| Ontology catalog as framework | The package classifies the domain or defines terms, but it does not tell a practitioner what typical problem is live or what SoTA solution move avoids a known failure. | Keep ontology as support material; draft or repair DPF patterns around problem frames, positive solution moves, worked cases, anti-patterns, and refresh. |
| Publication carrier as architecture | The publication or access carrier hides relation and dependency records. | Add `E.4.PFAD`, `E.4.PFR`, and source-return records before relying on the carrier as architecture evidence. |
| Invisible framework story | A DPF carrier reads as a neutral list of principles, but the reader cannot tell what source or domain structures were selected, why this route is for them, what was deliberately coarsened, abstracted, omitted, or left to source return, or whether the carrier is a second-step coarsening after an architecture description or view. | Add a short carrier structure-account in the readme, Preface, or equivalent carrier, then evaluate it through `E.4.DPF.DA` rather than scattering explanation into every pattern body. |
| Generated candidate authority | Search or LLM output becomes the framework because it is fluent. | Use `C.35` for admission, then decide candidate selection through `E.4.PFAD` or `C.32`. |
| Skeleton carrier as DPF | A file has a ToC, headings, and very short pattern-shaped sections, but readers still cannot apply the patterns without reconstructing the missing guidance from the DRR or source notes. | Keep it as `seedOnly`; harden each DPF pattern through `E.8`, evaluate through `E.21`, and only then assemble the user publication carrier. |
| Access carrier as framework | A skill pack, MCP endpoint, retrieval route, or assistant integration is treated as the framework itself because it is what agents call. | Record it as an access carrier through `E.4.PFR`, expose framework edition and refresh refs, and route generated, tool, evidence, currentness, or work claims to their direct owners. |

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

The pattern also makes local publication more useful. Readers get a coherent publication carrier or first-entry carrier, while maintainers can still inspect the framework edition, source pack, relation records, decision records, and quality route.

### E.4.DPF:10 - Rationale

Domain and local frameworks are not mere subsets of FPF. They are FPF-grounded framework editions in bounded contexts. They need domain source work, FPF authoring discipline, architecture decisions, relation records, quality loops, and refresh routes.

The pattern keeps the work practical by using existing FPF owners instead of inventing a second framework-development ontology. Its contribution is the ordered spine and the requirement that each produced artifact has a receiving owner.

### E.4.DPF:11 - SoTA-Echoing

| Claim | Exact source ref and status | Pattern locus changed | Adoption status |
| --- | --- | --- | --- |
| Domain-tailored frameworks need co-evolving ontology, examples, usability, and evaluation rather than only a term list. | Zhang, Struber, Hebig, `Development and Evolution of Xtext-based DSLs on GitHub: An Empirical Investigation`, arXiv:2501.19222, 2025 current empirical DSL-evolution source, `https://arxiv.org/abs/2501.19222`. | `Solution` requires context declaration, source pack, name preparation, carrier admission, and pattern drafting; `Common Anti-Patterns` blocks checklist promotion and source-summary substitution. | Adapt co-evolution discipline to FPF framework authoring; reject grammar, parser, metamodel, or code-generator ontology unless a framework deliberately specifies a language. |
| Reusable core and domain variation require explicit family and dependency work. | Nazar, `Software Product Line Engineering: Adoption, Tooling and AI Era Challenges`, arXiv:2605.21353, 2026 current survey and reopen trigger for stronger future SPLE synthesis, `https://arxiv.org/abs/2605.21353`. | `Solution` steps for architecture decision, relation and edition discipline, and publication-carrier assembly keep Core, domain framework, and local framework separate. | Adapt domain-engineering and reusable-core discipline; reject software-product feature-model ontology as FPF default. |
| Pattern bodies need condition-based use, examples, validation, and improvement loops. | Riehle, Harutyunyan, Barcomb, `Pattern Discovery and Validation Using Scientific Research Methods`, arXiv:2107.06065, 2021 current validation-practice source; Iba, `Pattern Languages as Media for the Creative Society`, arXiv:1308.1178, lineage for pattern languages as practice media. | `Solution` step 6 requires `E.8` pattern drafting; replayable authoring slice shows source pack to pattern draft to quality cycle; `Checklist` requires `E.22`, `E.21`, `E.23`, and `G.11` routes. | Adopt validation and worked-example pressure; adapt through FPF quality and improvement owners. |
| Architecture-description carriers help authoring only when their captured and lost structure is explicit. | `ISO/IEC/IEEE 42010:2022`, current official architecture-description standard ref, `https://www.iso.org/standard/74393.html`. | `Carrier admission` step and `Publication carrier as architecture` anti-pattern require `C.33`, `C.34`, or `C.35` treatment before carriers seed architecture decisions. | Adopt architecture-description boundary discipline; adapt source-return and admission to FPF carriers. |

### E.4.DPF:12 - Relations

- **Uses:** `G.2` for source pack and SoTA synthesis.
- **Uses:** `E.8`, `E.10`, and `F.18` for pattern drafting, kind discipline, and names.
- **Coordinates with:** `E.4` for family membership and `E.4.PFAD` for architecture decisions.
- **Coordinates with:** `E.4.PFR` for relation, dependency, edition, compatibility, deprecation, and supersession records.
- **Coordinates with:** `C.33`, `C.34`, and `C.35` for carrier preservation and admission.
- **Coordinates with:** `E.22` for quality-evaluation framing when needed, `E.4.DPF.DA` for DPF package adequacy, `E.21` for pattern-quality evaluation, `E.23` for repeated improvement, `E.19` for admission or profile gating when claimed, and `G.11` for currentness.
- **Exits to:** `E.11` and `E.17` when the live problem is publication or first-entry discoverability rather than framework authoring.

### E.4.DPF:End

