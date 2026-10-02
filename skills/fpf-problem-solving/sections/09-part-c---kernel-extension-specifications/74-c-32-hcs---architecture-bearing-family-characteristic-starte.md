## C.32.HCS - Architecture-Bearing Family Characteristic Starter Packs

> **Type:** Architectural characterization subpattern under C.32
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.32.HCS:1 - Problem frame

Use this pattern when a practitioner must choose a few architecture-characteristic starter heads for a described holon or for method, system-role-assignment, work, evidence, or cultural-evolution structures recovered from a source label, and the available catalogues are too broad to choose the first project criteria rows.

Primary working reader: an architect or architecture-responsible practitioner choosing a small first set of architecture-characteristic heads for an admitted holon family or another recovered architecture-bearing family, after naming the described holon or source-bearing episteme or publication context and any recovery patterns actually used.

Typical entry phrases:

```text
"The source catalogue has hundreds of quality names; which few heads should we inspect first?"
"The source calls this a review practice or method; what described holon, method-side structure, work family, and system-role side are actually under pressure?"
"A system-role assignment, organization, built asset, or evidence workflow has reliability-like pressure, but the bearer and scale are unclear."
```

**First-minute use slice.** A review lead must choose qualities for a reusable review method. Recovering the source word "practice" through A.3.1 identifies the Method itself as the described non-agentive holon. The lead inspects how its parts connect evidence, judgement and repair, then asks which of repeatability, transferability, evidence reuse and exception growth matters for the receiving work. A particular completed review is a separate A.15.1 Work occurrence; its actual coverage, elapsed time and rework require their own observations. The organization that performs reviews is another possible System, with different coordination and staffing questions. Teachability is a likely C.25 Q-Bundle. HCS returns these distinct starter questions to `C.32.ACS`; it does not replace the Method with the performing organization.

The primary `EntityOfConcern` is one architecture-bearing family starter pack for beginning to turn broad architecture-characteristic names into project criteria rows. A starter head is only a possible characteristic head before project bearer, scale, use class, proxy risk, and protected counter-characteristics are bound. Carry admitted starter heads to ACS. Keep Q-Bundles, measurements, eval programs, candidate palettes, comparison rules, G.5 result declarations, actual publications, and architecture decisions as separate objects handled by their applicable patterns.

Ordinary working move: choose the starter pack for the admitted holon family or recovered architecture-bearing family, keep only the heads that plausibly fit the project, ask the first project question for each head, then hand those heads to `C.32.ACS` for bearer, scale, and use-class binding.

The first useful output is an `ArchitectureBearingFamilyCharacteristicStarterPack@FPF`. It is a working starter record under C.32.HCS: it suggests heads and first questions for one admitted holon family or one recovered architecture-bearing family. It does not introduce a new `U.*` kind and does not by itself create project criteria, scale rows, Q-Bundles, measurement methods, eval programs, or a universal holon ontology:

```text
ArchitectureBearingFamilyCharacteristicStarterPack@FPF:
  architectureBearingFamilyRef:
  describedHolonRef?:
  presentationCarrierRef?:
  starterPackUse:
  recoveryPatternRefs?:
  typicalSelectedStructureRefs:
  starterCharacteristicHeads:
    - architectureCharacteristicHead:
      usualBearerOrSelectedStructureRefs:
      likelyQBundleBoundary?:
      firstProjectQuestion:
      usualNextQuestionPatternRef:
  nonUniversalCaution:
  criteriaRowPatternRef: C.32.ACS
```

Use `describedHolonRef` when the starter heads concern an exact holon. Use `presentationCarrierRef` only when the carrier itself changes how the starter pack is presented or used; do not fill it as a substitute for the described holon.

What goes wrong if C.32.HCS is missed: the team faces hundreds of `-ility` or quality names, copies a catalogue, or starts from a software-module list even when a source label such as method, role, culture, practice, built asset, or evidence workflow still hides what actually bears the characteristic.

What C.32.HCS buys in practice: the practitioner has a short architecture-bearing starting point before `C.32.ACS` turns starter heads into project criteria rows, normally three to five optimization indicators, and monitored guardrails.

Adoption test: after using C.32.HCS, the project has a short starter set and first project questions; it has not copied a catalogue and has not yet claimed bearer, scale, use class, or optimization status.

Not this pattern when the project already has admitted architecture-characteristic rows with bearers, scales, and use classes. Also not this pattern when the current work is composite-quality modeling, measurement, eval design, candidate synthesis, comparison, selected-set result declaration, actual publication, local choice, or project architecture decision.

Common exits by claim kind:

- `C.32.ACS` for project criteria rows.
- `C.25` for Q-Bundles and composite quality families.
- `C.16` for measurement and `C.32.ACE` for eval programs or eval results.
- `E.13` when a source-looking cue, score, benchmark, or dashboard starts replacing the architecture concern.
- `C.32` for candidate synthesis after project criteria rows exist.
- `A.19.CPM` for explicit comparison and `A.19.SelectorMechanism` for set-returning selection.
- `G.5` for selected-set result declaration, `C.11` for local choice, and `C.32.PAD` for a project decision. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability.

### C.32.HCS:2 - Problem

Architecture characteristics recur more than functions do. Reliability, substitutability, change reach, evidence reuse, control separation, or coordination load can appear across admitted holons and across method, system-role-assignment, work, evidence, or cultural-evolution structures. The same head may require a different bearer, scale, use, or pattern definition or test. Recurrence alone neither establishes that a source-labelled method-like object satisfies `U.Method`, nor turns a local system-role kind into a holon, nor admits practice or culture as holon kinds.

A function depends on what performs it, while a functional demand may also depend on the holon that needs that performance. A saw-as-system can cut; a system may satisfy a local system-role-kind criterion; an obtaining system-role assignment may place that system in work-facing use; and a direct responsibility relation may hold independently. A method description can guide work, an enacted work family can be repeatable, and an organization-as-system can coordinate. A culture or practice label must first be resolved into systems, disciplines, method and work families, local system-role kinds and assignments, canon or memory epistemes, recognition and selection regimes, or mediation systems. A project therefore needs starter packs that suggest common heads while requiring the practitioner to re-identify the bearer, any separate demand holder, and the scale before optimization.

### C.32.HCS:3 - Forces

| Force | Tension |
|---|---|
| Broad catalogues | Standards, textbooks, and local sources offer many possible quality names. |
| Project attention | A project needs a small first set of draft criteria rows, not a catalogue. |
| Bearer recovery | The same head can recur across admitted holon families and adjacent structures, but the family, bearer, scale, and any needed source-label recovery can change. |
| Software-source overfit | Mature software sources are useful but overfit to code modules, services, and operations if copied. |
| Q-Bundle boundary | Many `-ility` heads are composite quality families, not one architecture characteristic. |

### C.32.HCS:4 - Solution

Choose a starter pack by the admitted holon family or recovered architecture-bearing family. Use the pack only to start narrowing starter heads into project criteria rows; then hand the result to `C.32.ACS` for the project criteria set.

#### C.32.HCS:4.1 - Starter pack construction

Build or use a starter pack in this order:

1. Name the admitted holon family or recovered architecture-bearing family. If the source label is method, role, practice, culture, tradition, style, or evidence practice, recover the bearer before choosing heads. A Method admitted by A.3.1 is itself a non-agentive holon; its description, a Work occurrence under A.15.1, and the performing System remain separate. When the label is only a description-side family, name the source-bearing episteme or publication context. Record only the recovery patterns actually used.
2. List a small set of starter characteristic heads that often matter for that family.
3. For each head, name likely bearers or selected structures, not only a quality word.
4. Record likely C.25 Q-Bundle boundaries when a head is usually composite.
5. State a first project question that helps the practitioner decide whether the head belongs as a draft row in the project criteria set.
6. Hand the resulting starter heads to `C.32.ACS`; do not optimize or measure inside HCS.

Choose with four distinct considerations: the common characterization method, the bearer kind, the domain or practice, and the concrete use and interests. These considerations intersect. A software-development Method and an instructional Method share a bearer kind but serve different work; a biological system and Work performed in the same project share a domain but have different bearers. Neither domain membership nor a shared quality name supplies the missing structure, value meaning or observation.

#### C.32.HCS:4.2 - Built-in starter packs

| Architecture-bearing family or recovered source label | Structures and related values to inspect | Starter heads to inspect first | Likely C.25 boundary |
|---|---|---|---|
| Engineered system, product family, or built asset | module, component, placement, deployment, maintenance access, control, information, evidence, manufacture, operation | reliability, availability, maintainability, safety, latency, locality, access, substitutability, evidence reuse, source-return cost, scale amenability | availability, safety, maintainability, resilience, security |
| Method admitted by A.3.1, including a source "practice" when recovery establishes that bearer | Method parts and their input/result, ordering, guard, feedback, refinement and substitution relations; C.30.ASV:4.5a distinguishes these from description, performer and Work structures | repeatability under stated conditions, transferability, exception growth, evidence reuse, change reach and enactment burden; first ask which relation changes the attainable work result | teachability, review quality, reliability of enactment |
| Work occurrence admitted by A.15.1, or a family of such occurrences | actual constituent performances, their obtaining connections, time and resource conditions, required contributions and observed results; keep a WorkPlan and the reusable Method separate | completion of needed contributions, coordination delay, recovery or rework, resource burden and result adequacy; first ask what happened in the occurrence and which structural difference could matter for a later one | delivery reliability, cost of useful completion, robustness of coordinated performance |
| Role-word, team, organization, or changing-holon case after the applicable recovery | Use `E.10.ROLE` only for unresolved claim-bearing *role* wording; A.2/C.3 and A.2.7 only for a local system-role kind, a separate System-classification judgment, or a relation among kinds; A.2.1 only for an assignment species or occurrence; A.14 only when a changing-holon question is current. Otherwise use the direct relation, architecture, organization, representation, function, responsibility, availability, staffing, Work-coverage, or ordinary non-use route actually recovered. | Carry only the exact or explicitly provisional head into ACS: for example coordination load, independent change, testability, deployability, control separation, decision latency, evidence custody, kind substitutability, assignment continuity, holder replacement, staffing, Work coverage, availability, or responsibility. Infer no branch from another. | team performance, organizational effectiveness, reliability of service delivery |
| Discipline or cultural-evolution case after C.20/C.36 recovery | discipline holon, collective systems, method and work families, local system-role kinds and assignments, canon or memory epistemes, publication structures, review records, evidence relations, succession of systems in assignments, recognition and selection regimes | norm transfer, correction latency, coherence of enacted methods and work, evidence reuse, learning reach, variant containment, source-return cost, continuity of needed contributions | cultural quality, discipline health, trustworthiness |
| AI-agent setup, model-supported workflow, or information system | model boundary, tool boundary, retrieval service, supervisor relation, evidence refresh relation, deployment placement, action interface | function-bearer fit, observability, evidence refresh, policy controllability, latency, resource load, interface grammar burden, rollback, benchmark transfer risk | safety, trustworthiness, robustness, usefulness |
| Evidence-bearing assurance or certification work arrangement after A.10/A.15 recovery | evidence packages, claim scopes, audit trails, inspection work, certification mechanisms, evidence-provenance entries, source-currentness relation records, method descriptions, system-role assignments, direct responsibility relations | evidence reuse, traceability, source-return cost, inspection latency, certification burden, scope stability, mechanism visibility, change reach | assurance-case quality, certification-work quality, compliance-work quality |

In HCS, `source-return cost` is a starter head for a holon family only when repeated source return incurs effort, latency, or risk. The return is from a derivative, coarsened, extracted, rendered, or reused publication or evidence carrier back to the named source expression, selected source `U.Episteme`, `EpistemePublicationRelation` occurrence when availability matters, source-bearing relation, evidence-provenance entry, evidence relation, transform record, or defining ClaimGraph needed for stronger reliance. It is not a generic source-quality name. If the project is only asking whether a catalogue term is useful, keep the wording as source catalogue wording; if recoverability itself is the concern, carry `source-return cost` to `C.32.ACS` and bind its bearer, scale, and use.

#### C.32.HCS:4.3 - Rebinding rule

When a starter head is reused at another bearer kind, holon level, domain, or concrete use, rebind it. Name the target bearer, relevant relations, receiving result, conditions, quality meaning and attainable observation. State which part of the source construction survives and which part needs replacement. The reusable item is a candidate head, not an already valid project row.

Example: `availability` for an engineered service may use time-window and service-scope measures. A method-side case may ask whether an exact System can access a Method description and evidence relation in the working situation. A kind case may ask whether A.2.7 admits substitution; an assignment case may ask whether holder replacement or assignment continuity obtains; a responsibility case needs its own direct relation. These are different bearers, predicates, and scales.

Refresh the starter pack when its starting assumptions no longer hold: the admitted holon family changes, source-label recovery changes the recovered family or bearer, a B.2 whole reidentification changes the bearer or scale, a source catalogue changes the available vocabulary, repeated ACS project-row uses show that a head never survives project binding, or repeated ACS project-row uses reveal a missing head for that family. Refresh only starter-pack fields and blocked overreads. Existing project criteria rows remain with `C.32.ACS`; measurements remain with `C.16`; eval programs remain with `C.32.ACE`.

#### C.32.HCS:4.4 - ACS Criteria-Row Use

HCS stops with starter heads and first project questions. The next `C.32.ACS` use governs:

- whether C.32.ACS admits the head as a draft project criteria row;
- whether it is one characteristic or a C.25 Q-Bundle;
- whether the project uses it as an optimization indicator, monitored guardrail, or context-only row;
- which scale, reading, and pattern for the next question apply.

Before ACS criteria-row use, ask one proxy-resistance question for each carried starter head: what architecture concern would worsen or disappear if the visible catalogue entry, domain term, benchmark row, or dashboard value looked better? Such visible material is not yet an architecture-characteristic starter head. Carry it forward only when the architecture-bearing family, likely bearer, likely scale, Q-Bundle boundary, first project question, source catalogue entry, benchmark row, dashboard row, or publication row, source-to-use path, and reopen condition remain recoverable. Also name the selected source `U.Episteme` and an `EpistemePublicationRelation` occurrence when availability matters. If the architecture concern cannot be recovered, keep the wording as source catalogue wording or remove it from the starter pack. When the concern and the required starter-head bindings are recoverable but no plausible worsening or loss is found, carry the head forward, name the concerns inspected, and leave any unresolved proxy risk explicit.

**Stop condition.** Stop C.32.HCS when the starter pack names the admitted holon family or recovered architecture-bearing family, starter heads, likely bearers or selected structures, likely composite-quality boundaries, first ACS questions, and any blocked overread. The next project criteria-row work belongs to `C.32.ACS`.

**Lowering condition.** Lower a starter head to source catalogue wording or remove it from the starter pack when the architecture-bearing family is not declared, the likely bearer or likely scale is missing, the composite-quality boundary is still unresolved, the first ACS question is absent, repeated ACS uses reject the head for that family, or the item is being used to smuggle measurement, eval, comparison, publication, local choice, or decision work into HCS. Use `C.25` when the head is composite, `C.32.ACS` when the project criteria-row question is ready, and the named pattern for the next question when the stronger claim is current.

### C.32.HCS:5 - Worked slices

**Engineered-system family.** A field-device project starts from reliability, maintainability, substitutability, evidence reuse, locality, and source-return cost. `C.32.ACS` later marks only maintainability, substitutability, and evidence reuse as optimization indicators; safety and availability remain guardrails.

**Method and Work.** A reusable review Method connects source recovery, comparison, judgement and correction. Evidence reuse and change reach are plausible starter heads because changing how a dependent claim is found can alter both missed defects and repeated reading. A completed review has a separate Work question: were the required comparisons performed, and what delay or rework actually occurred? Improving the next Method version cannot retroactively change that Work. If the issue is reviewer staffing, select the performing organization and its contributions instead. Local system-role-kind substitution uses A.2.7; assignment continuity and Work coverage retain their own bearers.

**Same bearer, different domain.** An instructional Method also has parts, order and feedback, but its receiving result concerns what a learner can do under specified support. Removing corrective feedback may simplify the description while weakening the Method. Carry the learner result and help conditions into ACS; do not reuse software throughput or readability as if either measured learning. Teachability is composite and uses C.25.

**AI-agent workflow.** A retrieval-action setup starts from evidence refresh, policy controllability, latency, observability, and rollback. Benchmark performance stays a benchmark signal or comparison input until an architecture bearer and scale row are named.

**Starter-pack proxy near-miss.** A review team copies availability, throughput, and testability from a software quality catalogue because the list looks mature. The copied heads make the starter pack look complete, but they hide exception growth, evidence reuse, kind substitution, assignment continuity, and Work coverage, which have different bearers and predicates. C.32.HCS keeps the catalogue terms as source wording; A.3.1 and A.15 separate the Method, descriptions, assignments, and Work, while A.2.7 supplies kind-relation structure and substitution only for kinds. HCS carries only the recovered questions to `C.32.ACS`.

### C.32.HCS:6 - Receiving-Claim Boundary

Use C.32.HCS only to build architecture-bearing family starter packs. For work beyond starter-pack construction, use the exits in §1. C.32.HCS neither establishes a source-labelled object as `U.Method`, nor turns a local system-role kind into a holon, nor admits practice, culture, tradition, or style as holon kinds.

### C.32.HCS:7 - Conformance checklist

| Check | Required result |
|---|---|
| `CC-HCS-1` | The architecture-bearing family is named; when it is not itself an admitted holon family, the described holon or the source-bearing episteme or publication context for a description-side family is named, together with any recovery-pattern refs actually used. |
| `CC-HCS-2` | Starter heads are paired with likely bearers or selected structures. |
| `CC-HCS-3` | Q-Bundle boundaries are marked when the head is composite. |
| `CC-HCS-4` | Software-derived heads are generalized only after the source label is resolved to an architecture-bearing family and the bearer and scale are recoverable. |
| `CC-HCS-5` | Before project optimization, measurement, comparison, or selection, starter heads are either handed to `C.32.ACS` for project-row admission or kept as source catalogue wording. |
| `CC-HCS-6` | Catalogue, benchmark, or dashboard cues that look mature answer the proxy-resistance question or remain source catalogue wording. |

### C.32.HCS:8 - Common failures and repairs

| Failure | Symptom | Repair |
|---|---|---|
| `CatalogueAsStarterPack` | Hundreds of terms are copied into the project. | Choose the architecture-bearing family and keep only first heads that can change the next narrowing into project criteria rows. |
| `SoftwarePackOverfit` | Code-module terms are used for a method, role, practice, culture, or tradition without resolving the source label and rebinding bearer and scale. | Recover the described holon or the source-bearing episteme or publication context for a description-side family; name any recovery pattern actually used, then rebind bearer and scale or demote the head to source catalogue wording. |
| `FunctionalHeadAsArchitectureHead` | A domain function is used as the starter architecture characteristic. | Keep the function as functional demand; name the architecture characteristic that makes it sustainable. |
| `QBundleHeadAsScalar` | Maintainability, trustworthiness, or teachability is treated as one row. | Composite quality family work belongs to `C.25` before ACS chooses any slot. |
| `CatalogueCueAsStarterHead` | Catalogue maturity, benchmark performance, or dashboard cleanliness is used to admit a starter head without a rebound bearer, likely scale, Q-Bundle boundary, or first ACS question. | Keep the signal as source-looking catalogue, benchmark, or dashboard cue, ask what architecture concern worsened or disappeared, and carry the head forward only with a rebound bearer, likely scale, Q-Bundle boundary, and first ACS question. |

### C.32.HCS:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| Criteria-row narrowing starts from architecture-bearing family. | The practitioner is not forced to read a giant catalogue first. | Starter packs must be maintained as FPF architecture practice grows. |
| Cross-family generalization is disciplined. | Software sources can inform starter packs without importing software ontology or admitting source labels as holon kinds. | Every reuse must re-identify the family, bearer, and scale; record a recovery pattern only when a source label needed recovery. |
| ACS remains project-specific. | HCS does not overload project criteria construction. | The project still must do ACS work before optimization. |

### C.32.HCS:10 - Rationale

The 300-to-3 problem needs a middle step. A project cannot optimize from a catalogue, but it also should not invent criteria from scratch. Architecture-bearing starter packs give a small, recognizable entry.

### C.32.HCS:11 - SoTA-Echoing

These sources inform the starter-pack fields, ACS criteria-use conditions, and blocked overreads described below.

| Source to inspect | Why this source is load-bearing here | Transfer into HCS | Effect on HCS use | Blocked overread |
|---|---|---|---|---|
| ISO/IEC 25010:2023 (`https://www.iso.org/standard/78176.html`) and SQuaRE quality-model practice | Current standard source for ICT product quality vocabulary; useful as a stable catalogue reference, not as FPF ontology. | Use quality-model terms as source catalogue wording that must be rebound to the admitted holon family or recovered architecture-bearing family. | Starter-pack rows separate starter heads, likely bearers or selected structures, any source-label recovery actually needed, and likely C.25 boundaries. | An ICT product quality-model characteristic is not automatically a project criterion, holon ontology, scale row, eval program, or admission of a source label as a holon kind. |
| Richards and Ford, `Fundamentals of Software Architecture`, 2nd ed. (`https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/`) | Current practitioner source for architectural characteristics, trade-offs, scope, and limiting the working set before measurement or governance. | Keep the recurring-head idea, but generalize it only by rebinding family, bearer, and scale. | HCS requires the architecture-bearing family, likely bearers, likely selected structures, a recovery-pattern ref only when needed, and first project questions before ACS criteria-row construction. | Software architecture characteristic groupings cannot be copied into methods, roles, cultures, practices, built assets, or evidence workflows named by source wording without recovery and rebinding. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`); Ciceri et al., `Software Architecture Metrics` (`https://www.oreilly.com/library/view/software-architecture-metrics/9781098112226/`) | Current practitioner line for guided change, architecture characteristics, and metric or eval work after quality goals are named. | Put HCS before metrics and eval programs: it supplies starter heads, then ACS chooses project rows and ACE defines eval programs when needed. | HCS stop condition explicitly ends at starter heads, likely bearers, likely Q-Bundle boundaries, and first project questions for ACS. | A metric, dashboard, imported fitness-function name, or imported eval-program name is not a starter pack, project criterion, architecture-characteristic eval program, or architecture decision. |
| Current FPF `C.25`, `C.30`, `C.32.ACS`, `C.32.ACE`, and `C.16` | Local rules for Q-Bundles, grounded architecture, project criteria rows, eval programs, and measurement. | Use HCS only for starter packs; use the named pattern for each stronger claim. | HCS relations and conformance rows name C.25 for composite quality families, C.30 for selected-structure recovery, ACS for criteria rows, ACE for eval programs, and C.16 for measurement. | A starter head is not a Q-Bundle, selected structure, measurement method, eval result, comparison rule, declared selected-set result, published selected set, local choice, or project architecture decision. |

The bearer/domain distinction in §4.1 also uses C.30.ASV:4.5a and the developed instructional-design example in van Merriënboer, [*4C/ID: An Overview of Main Design Principles*](https://www.4cid.org/wp-content/uploads/2021/04/vanmerrienboer-4cid-overview-of-main-design-principles-2021.pdf) (2019; author-hosted copy uploaded in 2021), its explanation of whole tasks, support and feedback. This is retained design lineage: it shows why a Method’s parts and their relations can matter to a learner result. HCS adopts that question, not a claim of instructional effectiveness for an untested population. Reopen the transfer when the target Method needs a relation or outcome the recovered structure does not represent.

**Source-currentness boundary.** Use ISO/IEC 25010:2023 as ICT product-quality vocabulary, not as holon-family ontology. Use the O'Reilly architecture-characteristic and evolutionary-architecture sources for recurring starter heads and for later metric or eval work after the heads are named. Use an FPF row only for the claim it defines, constrains, or tests. Reopen HCS when a named source edition changes starter-head guidance, when the pattern for a next question changes how it handles that source family, when repeated `C.32.ACS` uses show that a starter head never survives project binding, when repeated project uses reveal a missing head for the admitted holon family or recovered architecture-bearing family, or when source-label recovery changes the recovered family or bearer.

### C.32.HCS:12 - Relations

- **Receiving use:** `C.32.ACS` project criteria-set construction, including scale rows and use classes when the project later needs them; `C.32.P2S` when starter heads are needed before the architecturing flow can bind project criteria, candidate synthesis, eval, and refresh.
- **Uses:** `C.25` when a starter head is composite; `C.30` and `C.30.ASV` when the selected structures are not yet recoverable.
- **Boundary:** HCS is not a catalogue, measurement pattern, Q-Bundle pattern, optimization method, or architecture decision pattern.

### C.32.HCS:13 - Footer marker

C.32.HCS closes when the practitioner can name an architecture-bearing starter pack, any needed described holon, source-bearing episteme or publication context, any recovery-pattern refs actually used, starter architecture-characteristic heads, likely bearers, likely Q-Bundle boundaries, and first project questions for `C.32.ACS`.

### C.32.HCS:End
