## E.5.1 - DevOps Lexical Firewall

### E.5.1:1 - Problem frame
The FPF Core is meant to remain valid across decades and technology
generations.  Implementation details—file formats, build pipelines,
runtime flags—evolve rapidly and differ between domains.  When such
terms invade normative prose, the Core ages as quickly as the tools it
mentions.

### E.5.1:2 - Problem
*Conceptual erosion*: a rule that cites a transient technology becomes
obsolete when that technology fades, forcing unnecessary Core revisions
and fragmenting historical audits.

### E.5.1:3 - Forces

| Force | Tension |
|-------|---------|
| **Timelessness** | Concepts must survive tool turnover. |
| **Pedagogic clarity** | Examples need concreteness ↔ too much concreteness hard‑codes technology. |
| **Cross‑domain reach** | Physical‑system engineers and knowledge‑theorists use different stacks. |

### E.5.1:4 - Solution
Establish a **Lexical Firewall** around the **Conceptual Core** *(conceptual constraint; not a build‑time linter)*:

1. **Keep abstract definitions independent of incidental machinery.**
   A Core definition **SHALL NOT** make an unrelated tool, file format, command or deployment arrangement necessary to identify or use its conceptual subject. Describe that subject directly; place the implementation in Tooling.

2. **Retain necessary syntax for a governed concrete subject.**
   When a rule governs a particular publication form, protocol or grammar, it **MAY** state the exact syntax needed to apply that subject's conformance condition. Name the governed subject and edition or use boundary. The exception applies only where replacing the syntax with a conceptual alias would remove an operative condition. A heading marker in a heading grammar qualifies; an unrelated build command does not. Calling executable code a grammar example supplies no exception.

3. **Keep executable teaching in its own source.**
   A Core concept needing a runnable illustration cites the teaching or Tooling artifact by conceptual name. Runnable teaching programs, concrete execution paths and commands remain there. A subject-defining syntax fragment under item 2 is not a runnable illustration merely because it appears in a code span or block. Mathematical expressions follow E.5.2: explain their interpretation, operation and prerequisites, with semantic mapping when compared or translated.

4. **Use aliases where they preserve the rule.**
   An incidental technical term can be defined in a Tooling Glossary and cited by conceptual alias. Preserve necessary spelling under item 2 when the concrete subject's condition would otherwise become untestable.

*Non‑normative automation.* Machine checks **MAY** exist in Tooling; they are advisory and **MUST NOT** be imported into the Core.

### E.5.1:5 - Archetypal Grounding (System / Episteme)

| Scenario | `U.System` example | `U.Episteme` example |
|----------|-------------------|----------------------|
| **Normative text** | “Identify the system's actual constituents and the relations by which they form the whole.” (No modelling-language syntax.) | “Identify the claim content, the entity it concerns, and the effective reference scheme.” (No proof-engine syntax.) |
| **Illustrative link** | A modelling profile resides in the Tooling family; Core cites it as “the reference system‑profile”. | A linting routine lives in Tooling; Core cites it as “the reference episteme‑checker”. |

#### E.5.1:5.1 - Four placement decisions

| Actual governed use | Placement and first action |
| --- | --- |
| E.8 H-1/H-6/H-9 govern this edition's Markdown pattern headings: level-2 `##`, the identifier/title separator ` - `, and `### <PatternId>:End`. | Keep those necessary syntax fragments in E.8. The author can write/check the heading and sentinel; “the reference heading mark” would lose the condition. The rule is about this publication form, not the ontology of the described System. |
| An unrelated abstract System definition requires a container-build command. | Move the command and its operational prerequisites to Tooling. Recover the System definition independently of that implementation. |
| A runnable program demonstrates a conceptual method. | Keep the program in its teaching/Tooling source and cite its conceptual role from Core. Calling it a grammar example does not change its role. |
| A Euclidean construction expression supplies a reasoning step under the subject Method. | Keep the expression where its meaning, construction operation and prerequisites are supplied under E.5.2. Its operative role is not reduced to illustration; compared expressions retain their mapping duty. |

### E.5.1:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑LFW.1** | A Core pattern excludes incidental implementation dependence. Exact syntax is allowed only when necessary for the conformance condition of its named publication form, protocol or grammar, under a stated edition/use boundary. |
| **CC‑LFW.2** | Executable illustrations are cited by conceptual name and kept in their teaching/Tooling source. A necessary subject-defining syntax fragment follows §4 item 2; it is not replaced by an alias that loses the condition. |
| **CC‑LFW.3** | Core pedagogical examples may describe behavior; runnable teaching code remains outside Core. Mathematical expressions retain E.5.2 interpretation/operation duties. A label such as “example” alone grants no syntax exception. |

### E.5.1:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Core stays evergreen and cross‑domain. | Move incidental implementation details and runnable teaching code to Tooling or Pedagogy. Retain necessary governed-subject syntax under §4 item 2 and operative mathematics under E.5.2. |
| A token scan can locate places to inspect. | The subject and operative condition decide conformance; an allow-list alone cannot decide incidental dependence. |

### E.5.1:8 - Rationale
Language shapes thought.  By firewalling transient jargon, we uphold
**P‑1 Cognitive Elegance** (clarity), **P‑2 Didactic Primacy** (domain‑neutral
exposition) and **P‑5 FPF Layering** (clean separation between Core
and Tooling). The subject-sensitive boundary keeps abstract concepts portable while allowing a form-specific rule to state the syntax that its reader must use.

### E.5.1:9 - Relations
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)
* **Constrains:** every pattern in Conceptual Core
* **Instantiates pillars:** P‑1, P‑2, P‑5

### E.5.1:End
