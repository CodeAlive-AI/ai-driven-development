## C.32.HCS - Holon-Family Architecture Characteristic Starter Packs

> **Type:** Architectural characterization subpattern under C.32
> **Status:** Draft
> **Normativity:** Normative unless explicitly marked informative

### C.32.HCS:1 - Problem frame

Use this pattern when a practitioner must begin architecture-characteristic narrowing for a described holon and the available source catalogues are too broad to choose the first project criteria rows.

Primary working reader: an architect or architecture-responsible practitioner choosing a small first set of architecture-characteristic heads for the described holon family.

Typical entry phrases:

```text
"The source catalogue has hundreds of quality names; which few heads should we inspect first?"
"The described holon is a review method, not a software service; which characteristics transfer?"
"A role, organization, built asset, or evidence practice has reliability-like pressure, but the bearer and scale are unclear."
```

**First-minute use slice.** A method-family architect sees a long quality catalogue and a software-oriented checklist, but the described holon is a reusable review method. Using C.32.HCS, the practitioner chooses the method-family starter pack, inspects repeatability, transferability, evidence reuse, exception growth, and role substitutability, records teachability as a likely C.25 Q-Bundle, and carries only those starter heads and first project questions to `C.32.ACS`. The project starts from a small holon-family set instead of copying hundreds of names.

The primary `EntityOfConcern` is one holon-family starter pack for beginning to turn broad architecture-characteristic names into project criteria rows. A starter head is only a possible characteristic head before project bearer, scale, use class, proxy risk, and protected counter-characteristics are bound. HCS hands starter heads to ACS; Q-Bundles, measurements, eval programs, candidate palettes, comparison rules, G.5 publications, and architecture decisions stay with their receiving patterns.

Ordinary working move: choose the starter pack for the described holon family, keep only the heads that plausibly fit the project, ask the first project question for each head, then hand those heads to `C.32.ACS` for bearer, scale, and use-class binding.

The first useful output is a `HolonFamilyArchitectureCharacteristicStarterPack@FPF`. It is a working starter record under C.32.HCS: it suggests heads and first questions for one holon family. It does not introduce a new `U.*` kind and does not by itself create project criteria, scale rows, Q-Bundles, measurement methods, eval programs, or a universal holon ontology:

```text
HolonFamilyArchitectureCharacteristicStarterPack@FPF:
  holonFamilyRef:
  typicalSelectedStructureRefs:
  starterCharacteristicHeads:
    - architectureCharacteristicHead:
      usualBearerOrSelectedStructureRefs:
      likelyQBundleBoundary?:
      firstProjectQuestion:
      usualReceivingPatternRef:
  nonUniversalCaution:
  criteriaRowPatternRef: C.32.ACS
```

What goes wrong if C.32.HCS is missed: the team faces hundreds of `-ility` or quality names, copies a catalogue, or starts from a software-module list even when the described holon is a method, role, culture, built asset, or evidence-bearing practice.

What C.32.HCS buys in practice: the practitioner has a short holon-family starting point before `C.32.ACS` turns starter heads into project criteria rows, three to five optimization indicators, and monitored guardrails.

Adoption test: after using C.32.HCS, the project has a short starter set and first project questions; it has not copied a catalogue and has not yet claimed bearer, scale, use class, or optimization status.

Not this pattern when the project already has admitted architecture-characteristic rows with bearers, scales, and use classes. Also not this pattern when the current work is composite-quality modeling, measurement, eval design, candidate synthesis, comparison, publication of a selected set, local choice, or project architecture decision.

Common exits by claim kind:

- `C.32.ACS` for project criteria rows.
- `C.25` for Q-Bundles and composite quality families.
- `C.16` for measurement and `C.32.ACE` for eval programs or eval results.
- `E.13` when a source cue, score, benchmark, or dashboard starts replacing the architecture concern.
- `C.32` for candidate synthesis after project criteria rows exist.
- `A.19.CPM` for explicit comparison and `A.19.SelectorMechanism` for set-returning selection.
- `G.5` for publication of a selected set, `C.11` for local choice, and `C.32.PAD` for project decision.

### C.32.HCS:2 - Problem

Architecture characteristics recur more than functions do. Reliability, substitutability, change reach, evidence reuse, control separation, or coordination load can appear across systems, methods, roles, organizations, AI-agent setups, and cultures. The recurrence does not mean that the bearer, scale, or use is identical.

Functions and functional demands depend on the holon kind. A saw cuts, a method teaches or guides work, a role carries accountability, an organization coordinates, and a model-supported workflow classifies or acts. A project therefore needs starter packs that suggest common architecture-characteristic heads for a holon family while forcing project rebinding before optimization.

### C.32.HCS:3 - Forces

| Force | Tension |
|---|---|
| Broad catalogues | Standards, textbooks, and local sources offer many possible quality names. |
| Project attention | A project needs a small first set of draft criteria rows, not a catalogue. |
| Holon generality | The same head can recur across holon families, but the bearer and scale change. |
| Software-source overfit | Mature software sources are useful but overfit to code modules, services, and operations if copied. |
| Q-Bundle boundary | Many `-ility` heads are composite quality families, not one architecture characteristic. |

### C.32.HCS:4 - Solution

Choose a starter pack by the described holon's declared family. Use the pack only to start narrowing starter heads into project criteria rows; then hand the result to `C.32.ACS` for the project criteria set.

#### C.32.HCS:4.1 - Starter pack construction

Build or use a starter pack in this order:

1. Name the holon family and the selected structures usually involved in architecture synthesis for that family.
2. List a small set of starter characteristic heads that often matter for that family.
3. For each head, name likely bearers or selected structures, not only a quality word.
4. Record likely C.25 Q-Bundle boundaries when a head is usually composite.
5. State a first project question that helps the practitioner decide whether the head belongs as a draft row in the project criteria set.
6. Hand the resulting starter heads to `C.32.ACS`; do not optimize or measure inside HCS.

#### C.32.HCS:4.2 - Built-in starter packs

| Holon family | Typical selected structures | Starter heads to inspect first | Likely C.25 boundary |
|---|---|---|---|
| Engineered system, product family, or built asset | module, component, placement, deployment, maintenance access, control, information, evidence, manufacture, operation | reliability, availability, maintainability, safety, latency, locality, access, substitutability, evidence reuse, source-return cost, scale amenability | availability, safety, maintainability, resilience, security |
| Method family or practice | method steps, work products, roles, evidence records, teaching sequence, review structure, exception-handling structure | repeatability, teachability, transferability, reviewability, exception growth, evidence reuse, change reach, work burden, role substitutability | teachability, review quality, reliability of method enactment |
| Role, team, organization, or changing holon | role boundaries, communication relations, work responsibility, toolchain, deployment responsibility, evidence responsibility | coordination load, accountability clarity, independent change, testability, deployability, control separation, decision latency, evidence custody, substitutability | team performance, organizational effectiveness, reliability of service delivery |
| Culture, discipline, or episteme-bearing holon | norms, exemplars, teaching sequences, publication structures, review practices, evidence relations, role succession | norm transfer, correction latency, practice coherence, evidence reuse, learning reach, variant containment, source-return cost, role continuity | cultural quality, discipline health, trustworthiness |
| AI-agent setup, model-supported workflow, or information system | model boundary, tool boundary, retrieval service, supervisor relation, evidence refresh relation, deployment placement, action interface | function-bearer fit, observability, evidence refresh, policy controllability, latency, resource load, interface grammar burden, rollback, benchmark transfer risk | safety, trustworthiness, robustness, usefulness |
| Evidence-bearing assurance or certification practice | evidence packages, claim scopes, audit trails, inspection work, certification mechanisms, source records | evidence reuse, traceability, source-return cost, inspection latency, certification burden, scope stability, mechanism visibility, change reach | assurance-case quality, certification-practice quality, compliance-practice quality |

#### C.32.HCS:4.3 - Rebinding rule

When a starter head is reused at another declared holon level, rebind it. The reusable item is the head, not the row.

Example: `availability` for an engineered service may use time-window and service-scope measures. A method-family analogue may concern whether a method step and evidence relation are available to a role in the work situation. A role-family analogue may concern substitutable responsibility coverage. These are different bearers and scales.

Refresh the starter pack when its starting assumptions no longer hold: the described holon family changes, a B.2 whole reidentification changes the bearer or scale, a source catalogue changes the available vocabulary, repeated ACS project-row uses show that a head never survives project binding, or repeated ACS project-row uses reveal a missing head for that family. Refresh only starter-pack fields and blocked overreads. Existing project criteria rows remain with `C.32.ACS`; measurements remain with `C.16`; eval programs remain with `C.32.ACE`.

#### C.32.HCS:4.4 - ACS Criteria-Row Use

HCS stops with starter heads and first project questions. The next `C.32.ACS` use governs:

- whether C.32.ACS admits the head as a draft project criteria row;
- whether it is one characteristic or a C.25 Q-Bundle;
- whether the project uses it as an optimization indicator, monitored guardrail, or context-only row;
- which scale, reading, and receiving pattern apply.

Before ACS criteria-row use, ask one proxy-resistance question for each carried starter head: what architecture concern would worsen or disappear if the visible source cue looked better? A richer catalogue, familiar software term, higher benchmark, or cleaner dashboard is only a source signal. Carry it forward only when the holon family, likely bearer, likely scale, Q-Bundle boundary, and first project question are recoverable. If no worsening or lost concern can be named, keep the item as source vocabulary or remove it from the starter pack.

**Stop condition.** Stop C.32.HCS when the starter pack names the described holon family, starter heads, likely bearers or selected structures, likely composite-quality boundaries, first ACS questions, and any blocked overread. The next project criteria-row work belongs to `C.32.ACS`.

**Lowering condition.** Lower a starter head to source vocabulary or remove it from the starter pack when the holon family is not declared, the likely bearer or likely scale is missing, the composite-quality boundary is still unresolved, the first ACS question is absent, repeated ACS uses reject the head for that holon family, or the item is being used to smuggle measurement, eval, comparison, publication, local choice, or decision work into HCS. Use `C.25` when the head is composite, `C.32.ACS` when the project criteria-row question is ready, and the named receiving pattern when the stronger claim is current.

### C.32.HCS:5 - Worked slices

**Engineered-system family.** A field-device project starts from reliability, maintainability, substitutability, evidence reuse, locality, and source-return cost. `C.32.ACS` later marks only maintainability, substitutability, and evidence reuse as optimization indicators; safety and availability remain guardrails.

**Method family.** A reusable review method starts from repeatability, transferability, evidence reuse, exception growth, and role substitutability. Teachability belongs to C.25 because it combines learner scope, measures, mechanisms, and evidence.

**AI-agent workflow.** A retrieval-action setup starts from evidence refresh, policy controllability, latency, observability, and rollback. Benchmark performance stays a source signal or comparison input until an architecture bearer and scale row are named.

**Starter-pack proxy near-miss.** A review-method team copies availability, throughput, and testability from a software quality catalogue because the list looks mature. The copied heads make the starter pack look complete, but they hide exception growth, evidence reuse, and role substitutability, which are the architecture concerns that will later govern review work. C.32.HCS keeps the catalogue terms as source vocabulary, restores the method-family heads, and carries only rebound questions to `C.32.ACS`.

### C.32.HCS:6 - Receiving-Claim Boundary

C.32.HCS governs holon-family starter packs. It does not govern project scale rows, Q-Bundles, measurements, eval programs, candidate synthesis, comparison, selection, publication of a selected set, local choices, or project architecture decisions. Use `C.32.ACS`, `C.25`, `C.16`, `C.32.ACE`, `C.32`, `A.19.CPM`, `A.19.SelectorMechanism`, `G.5`, `C.11`, or `C.32.PAD` when those claims are being made.

### C.32.HCS:7 - Conformance checklist

| Check | Required result |
|---|---|
| `CC-HCS-1` | The described holon family is named. |
| `CC-HCS-2` | Starter heads are paired with likely bearers or selected structures. |
| `CC-HCS-3` | Q-Bundle boundaries are marked when the head is composite. |
| `CC-HCS-4` | Software-derived heads are generalized only after the holon bearer is recoverable. |
| `CC-HCS-5` | Before project optimization, measurement, comparison, or selection, starter heads are either handed to `C.32.ACS` for project-row admission or kept as source vocabulary. |
| `CC-HCS-6` | Source cues that look mature answer the proxy-resistance question or remain source vocabulary. |

### C.32.HCS:8 - Common failures and repairs

| Failure | Symptom | Repair |
|---|---|---|
| `CatalogueAsStarterPack` | Hundreds of terms are copied into the project. | Choose the holon family and keep only first heads that can change the next narrowing into project criteria rows. |
| `SoftwarePackOverfit` | Code-module terms are used for a method, role, or culture without rebinding. | Rebind the bearer and scale or demote the head to source vocabulary. |
| `FunctionalHeadAsArchitectureHead` | A domain function is used as the starter architecture characteristic. | Keep the function as functional demand; name the architecture characteristic that makes it sustainable. |
| `QBundleHeadAsScalar` | Maintainability, trustworthiness, or teachability is treated as one row. | Composite quality family work belongs to `C.25` before ACS chooses any slot. |
| `SourceSignalAsStarterHead` | Catalogue maturity, benchmark performance, or dashboard cleanliness is used to admit a starter head without a rebound bearer, likely scale, Q-Bundle boundary, or first ACS question. | Keep the signal as a source cue, ask what architecture concern worsened or disappeared, and carry the head forward only with a rebound bearer, likely scale, Q-Bundle boundary, and first ACS question. |

### C.32.HCS:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| Criteria-row narrowing starts from holon family. | The practitioner is not forced to read a giant catalogue first. | Starter packs must be maintained as FPF architecture practice grows. |
| Holonic generalization is disciplined. | Software sources can inform starter packs without importing software ontology. | Every reuse requires bearer and scale rebinding. |
| ACS remains project-specific. | HCS does not overload project criteria construction. | The project still must do ACS work before optimization. |

### C.32.HCS:10 - Rationale

The 300-to-3 problem needs a middle step. A project cannot optimize from a catalogue, but it also should not invent criteria from scratch. Holon-family starter packs give a small, recognizable entry while project criteria-row construction, measurement, eval, comparison, selection, publication of a selected set, local choice, and project architecture decision work stays with its receiving pattern.

### C.32.HCS:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.HCS. Keep a source name only when the draft uses it to set or revise a starter-pack field, an ACS criteria-use condition, or a blocked overread.

| Source to inspect | Why this source is load-bearing here | Transfer into HCS | Concrete HCS mutation | Blocked overread |
|---|---|---|---|---|
| ISO/IEC 25010:2023 (`https://www.iso.org/standard/78176.html`) and SQuaRE quality-model practice | Current standard source for ICT product quality vocabulary; useful as a stable catalogue source, not as FPF ontology. | Use quality-model terms as source vocabulary that must be rebound to the described holon family. | Starter-pack rows now separate starter heads, likely bearers or selected structures, and likely C.25 boundaries. | An ICT product quality-model characteristic is not automatically a project criterion, holon-family ontology, scale row, or eval program. |
| Richards and Ford, `Fundamentals of Software Architecture`, 2nd ed. (`https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/`) | Current practitioner source for architectural characteristics, trade-offs, scope, and limiting the working set before measurement or governance. | Keep the recurring-head idea, but generalize it only through bearer and scale rebinding. | HCS requires the holon family, likely bearers, likely selected structures, and first project questions before ACS criteria-row construction. | Software architecture characteristic groupings cannot be copied into methods, roles, cultures, built assets, or evidence practices without rebinding. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`) and `Software Architecture Metrics` (`https://www.oreilly.com/library/view/software-architecture-metrics/9781098112226/`) | Current practitioner line for guided change, architecture characteristics, and metric or eval work after quality goals are named. | Put HCS before metrics and eval programs: it supplies starter heads, then ACS chooses project rows and ACE defines eval programs when needed. | HCS stop condition explicitly ends at starter heads, likely bearers, likely Q-Bundle boundaries, and first project questions for ACS. | A metric, dashboard, or source-side fitness-function name is not a starter pack, project criterion, architecture-characteristic eval program, or architecture decision. |
| Current FPF `C.25`, `C.30`, `C.32.ACS`, `C.32.ACE`, and `C.16` | Local receiving-pattern law for Q-Bundles, grounded architecture, project criteria rows, eval programs, and measurement. | Keep HCS as the starter-pack governing pattern; stronger claims belong to their receiving patterns. | HCS relations and conformance rows name C.25 for composite quality families, C.30 for selected-structure recovery, ACS for criteria rows, ACE for eval programs, and C.16 for measurement. | A starter head is not a Q-Bundle, selected structure, measurement method, eval result, comparison rule, published selected set, local choice, or project architecture decision. |

**Source-currentness boundary.** Use ISO/IEC 25010:2023 as ICT product-quality vocabulary, not as holon-family ontology. Use the O'Reilly architecture-characteristic and evolutionary-architecture sources for recurring starter heads and for later metric or eval work after the heads are named. Use an FPF row only for the claim governed by the named receiving pattern. Reopen HCS when a named source edition changes starter-head guidance, when a receiving pattern changes how it handles that source family, when repeated `C.32.ACS` uses show that a starter head never survives project binding, or when repeated project uses reveal a missing head for the holon family.

### C.32.HCS:12 - Relations

- **Receiving use:** `C.32.ACS` project criteria-set construction, including scale rows and use classes when the project later needs them; `C.32.P2S` when starter heads are needed before the architecturing flow can bind project criteria, candidate synthesis, eval, and refresh.
- **Uses:** `C.25` when a starter head is composite; `C.30` and `C.30.ASV` when the selected structures are not yet recoverable.
- **Boundary:** HCS is not a catalogue, measurement pattern, Q-Bundle pattern, optimization method, or architecture decision pattern.

### C.32.HCS:13 - Footer marker

C.32.HCS closes when the practitioner can name a holon-family starter pack, starter architecture-characteristic heads, likely bearers, likely Q-Bundle boundaries, and first project questions for `C.32.ACS`.

### C.32.HCS:End

