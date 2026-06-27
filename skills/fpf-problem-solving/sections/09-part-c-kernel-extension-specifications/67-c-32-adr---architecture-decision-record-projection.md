## C.32.ADR - Architecture Decision Record Projection

> **Type:** Architecture publication pattern under C.32
> **Status:** Draft
> **Normativity:** Normative unless explicitly marked informative

### C.32.ADR:1 - Problem frame

Use this pattern when an `ArchitectureDecisionRelation@Project` or equivalent project architecture decision must be published as an ADR-like record, decision memo, trade-study record, certification rationale, or similar decision-description record.

Primary working reader: an architect or architecture-responsible practitioner preparing a decision record for developers, reviewers, maintainers, operators, certifiers, or future architects.

Typical entry phrases:

```text
"The project decision is made; now we need an ADR that future developers can use."
"The record must show options, decision, rationale, consequences, and confirmation without becoming the decision itself."
"This is not a software project; can a trade-study memo play the ADR role?"
"The ADR package must link to architecture views without duplicating the whole architecture description."
"A future team must know when this decision is superseded or violated."
```

**First-minute use slice.** A platform architect has a C.32.PAD decision relation selecting event-carried integration with a bounded exception. Using C.32.ADR, the architect creates an ADR projection with section functions for problem frame, candidate options, decision outcome, rationale, consequences, method-use instruction, work split, confirmation eval, source-return links, and supersession. The file is short enough for developers to read, but it remains a publication projection of the decision description, not the decision relation and not the architecture itself.

The primary `EntityOfConcern` is `ArchitectureDecisionRecordProjection@Project`: a publication projection of `ArchitectureDecisionDescription@Project` into an ADR-like record or package. Select this pattern only when the work is to publish or package that decision description for a declared reader use; generic ADR advice that cannot be mapped to decision-section functions stays outside C.32.ADR.

`ArchitectureDecisionRecordProjection@Project` is not a new `U.*` kind and not a new root publication ontology. It is a project publication projection with filled section-function rows. Use `E.17` and `E.24.PUB` for publication-face and publication-use claims; use `C.32.PAD` for the decision relation.

What goes wrong if C.32.ADR is missed: the project either publishes a record-shaped text that hides the actual architecture decision, or it copies architecture descriptions, diagrams, and method material into a record without telling the reader what decision was made and what work must change.

What C.32.ADR buys in practice: a decision record can be small, readable, updateable, and still tied to candidate synthesis, selected structures, architecture characteristics, method-use instructions, work split, confirmation evals, and source-return.

Ordinary working move: start from a PAD decision relation, select the record's publication scope, map each necessary section to the decision content it carries, then publish only what the reader needs to use, check, or reopen the decision.

Adoption test: after using C.32.ADR, a future reader can recover the decision question, considered options, outcome, rationale, consequences, required method or work change, confirmation or eval path, source links, and supersession condition without mistaking the record for the architecture or the decision relation.

Not this pattern when the decision relation is not yet recoverable, the current work is architecture-description adequacy, the record is a general MVPK publication face, or the claim is evidence, assurance, gate passage, local choice, performed work, or pattern authoring. Use the receiving pattern named in `Relations`.

The first useful output is `ArchitectureDecisionRecordProjection@Project`:

```text
ArchitectureDecisionRecordProjection@Project:
  projectionId:
  architectureDecisionRelationRef:
  architectureDecisionDescriptionRef:
  publicationCarrierRef:
  publicationScopeRef:
  intendedReaderRefs:
  status:
  sectionFunctionRows:
    - sectionFunction:
      sectionHeadingOrCarrierSlot:
      sourceDecisionSlotRefs:
      requiredReaderUse:
      omittedByDesign?
      sourceReturnCondition?
  architectureDescriptionRefs:
  methodAndWorkRefs:
  confirmationOrEvalRefs:
  supersedesRecordRefs?
  supersededByRecordRef?
  updateOrReopenCondition:
  publicationUseRefs?
```

### C.32.ADR:2 - Problem

ADR practice is useful because it makes architectural decisions small enough to read and update. It is also easy to misuse. A record can become a substitute for the decision relation, a loose essay about architecture, a copied architecture description, or a method prescription with no recoverable target structure.

C.32.ADR treats ADR as a publication projection. The project decision relation belongs to `C.32.PAD`. The architecture description belongs to `C.30.AD` and related view patterns. The method description or pattern-use recommendation belongs to `A.15`, `E.8`, and `E.11.PUR` when those claims are live. The ADR-like record publishes a decision description for a declared reader and use.

The section question is therefore not "which headings are allowed?" The section question is "which decision functions must a reader recover?" A heading can vary by organization or industry, but the record must carry the decision question, candidate options or reason no candidate set is live, outcome, rationale, consequences, method-use instruction when the decision guides work, work split, confirmation or eval path, source-return, status, and supersession or reopen condition.

ADR-like projection is not software-only. Engineering trade-study records, safety-certification rationale, design review memos, BIM decision logs, method-governance records, and organization-design records can play the same publication role after the project decision relation and record use are typed. The source form may differ; the FPF section functions stay recoverable.

### C.32.ADR:3 - Forces

| Force | Tension |
|---|---|
| Reader economy | The record should be short enough to use, but not so short that decision content disappears. |
| Section variation | ADR templates and engineering memos differ, while the decision functions must remain recoverable. |
| Publication and decision separation | The record publishes a description of the decision; it does not become the decision relation. |
| Architecture and method coupling | A record often needs to cite both target structures and required developer methods. |
| Evolution | Supersession, violation detection, and update conditions must be visible without making the record a governance system. |
| Cross-domain use | Software ADR practice must generalize to other holon kinds without importing software-only assumptions. |

### C.32.ADR:4 - Solution

Create `ArchitectureDecisionRecordProjection@Project` from an existing `ArchitectureDecisionRelation@Project` and `ArchitectureDecisionDescription@Project`. If the decision relation is missing, return to `C.32.PAD` before writing the record.

Work in this order:

1. Name the publication carrier and intended readers. The carrier can be a Markdown ADR file, decision memo, trade-study record, engineering change note, certification rationale, design-review record, or another typed file or record.
2. Cite the decision relation and decision description. If the record cannot cite them, draft them first.
3. Choose the smallest record scope that lets intended readers use the decision. Avoid copying architecture descriptions or full method descriptions; cite them by value where possible.
4. Map section functions to headings or carrier slots. Use local headings if needed, but keep the function rows recoverable.
5. Carry the candidate basis. Record candidate options from `C.32` or the reason no candidate-set question is live. Do not invent options in the ADR after the decision.
6. Carry the decision outcome. State the selected architecture option, bounded exception, or supersession relation from PAD.
7. Carry rationale, accepted losses, and consequences. Include architecture-characteristic trade-offs and guardrails, not only benefits.
8. Carry method-use instruction and work split when the decision guides developer work. Cite `A.15`, method descriptions, pattern-use refs, readiness exits, and expected structure effects rather than burying them in prose.
9. Carry confirmation, eval, or violation-detection exits. Use `C.32.ACE`, `C.16`, `A.10`, `B.3`, `A.21`, or governance patterns when those claims are live.
10. Carry publication and source-return boundaries. Use `E.17`, `E.24.PUB`, and `C.30.AD` for publication-face and architecture-description claims.
11. Carry status, supersession, and update conditions. Old records remain useful as history when superseded; the active decision relation tells which one governs current work.

#### C.32.ADR:4.1 - Required section functions

The following section functions are required unless the decision relation states why the function is not live for this record use.

| Section function | What the record must let the reader recover |
|---|---|
| Identity and status | Record id, title, status, date or version, relation to superseded or superseding records. |
| Problem frame and decision question | The bounded architecture question, described holon, context, and current reader use. |
| Forces and architecture characteristics | The architecture characteristics, constraints, concerns, and trade-offs that made the decision nontrivial. |
| Candidate options | Candidate options, rejected options, bounded exception, or stated reason no candidate-set question is live. |
| Decision outcome | The selected architecture option and affected selected structures. |
| Rationale | Why this outcome is acceptable now, including accepted losses and protected guardrails. |
| Consequences | Expected effects on structures, methods, teams, costs, risks, evidence, operation, and later change. |
| Method-use instruction | Required style, pattern use, method description, or work practice, when the decision changes developer work. |
| Work split | Architect-owned selected structures, developer-owned refinement, readiness or gate exits, and source-return condition. |
| Confirmation or eval exit | How the decision can be checked, evaluated, monitored, or found violated. |
| Publication boundary | Links to architecture descriptions, views, evidence, assurance, and source material without making the ADR the source object. |

#### C.32.ADR:4.2 - ADR package use

When several records form a package, create a package map that names active, proposed, superseded, and related records. A package map is a publication navigation aid. It does not merge decisions, replace PAD relations, or decide record priority by file order alone.

When one decision changes another, use explicit supersession or amendment links. Do not rewrite history by deleting the old record unless the project has a governed archival policy.

### C.32.ADR:5 - Archetypal Grounding

**Software ADR.** A team publishes an ADR for event-carried integration. The record uses local headings, but the function rows recover context, options, selected outcome, rationale, consequences, method-use instruction for event schema work, confirmation eval, and supersession. Developers can see what to implement and when the decision reopens.

**Manufacturing trade-study record.** A fixture decision is published as an engineering trade-study memo rather than a Markdown ADR. The memo carries candidate fixture variants, selected universal-fixture scope, accepted setup-time loss, cell-design method instruction, evidence links, and reopen threshold. C.32.ADR admits the memo because it projects the decision description for the intended reader.

**Certification rationale.** A regulated product records a safety-architecture decision in a certification rationale. The record carries the decision outcome, rationale, evidence refs, architecture-description refs, and confirmation path, while evidence and assurance claims stay in `A.10` and `B.3`.

**Method-governance record.** A method family decides that reviewers must use an evidence handoff pattern before final review. The ADR-like record cites the method description and expected evidence-structure effect; it does not become the method itself or the performed review work.

### C.32.ADR:6 - Bias-Annotation

| Risk handled | How C.32.ADR handles it |
|---|---|
| Template-first writing | The record starts from a PAD decision relation and section functions, not from a blank template. |
| Publication-as-decision drift | The ADR projection cites the decision relation and remains a publication object. |
| Architecture-copy drift | Architecture descriptions are cited through `C.30.AD`; the record carries only decision-relevant references. |
| Method prose drift | Method-use instruction is typed through `A.15`, `E.8`, or `E.11.PUR` when live. |
| History loss | Status and supersession are record functions; old records stay recoverable unless governed archival policy says otherwise. |
| Software-only overread | ADR-like projection is generalized by section function and reader use, not by software tool convention. |

### C.32.ADR:7 - Conformance Checklist

| Requirement | Required result |
|---|---|
| `CC-ADR-1` | The record cites an `ArchitectureDecisionRelation@Project` or states the equivalent accepted decision relation by value. |
| `CC-ADR-2` | The record's publication carrier, intended readers, scope, and status are explicit. |
| `CC-ADR-3` | Section functions are mapped to headings or carrier slots. |
| `CC-ADR-4` | Problem frame, forces, candidate options, outcome, rationale, consequences, confirmation or eval exit, and supersession or update condition are recoverable. |
| `CC-ADR-5` | Method-use instruction and work split are included when the decision guides developer work. |
| `CC-ADR-6` | Architecture descriptions, views, evidence, assurance, gate, method, work, and publication claims exit to their governing patterns. |
| `CC-ADR-7` | The record does not create new candidate options, new architecture-description adequacy, or new evidence authority by prose. |

### C.32.ADR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| `BlankTemplateADR` | A template is filled with plausible prose but no PAD relation can be cited. | Draft or recover `ArchitectureDecisionRelation@Project` with `C.32.PAD`; then project it into the record. |
| `ArchitectureDescriptionDump` | The ADR copies diagrams, views, or model text and the decision outcome is hard to find. | Keep the record small; cite architecture-description refs and restore decision outcome, rationale, consequences, and work effects. |
| `OptionsInventedInRecord` | The ADR lists options that were not part of candidate synthesis or accepted decision basis. | Return to `C.32`, `A.19.CPM`, or PAD; update the decision relation before updating the record. |
| `MethodInstructionHiddenInRationale` | Developers are expected to change work, but the instruction is buried in rationale prose. | Add a method-use section function with method refs, responsible roles, expected structure effect, and readiness or gate exit. |
| `NoConfirmationPath` | Future teams cannot tell whether the decision still holds or has been violated. | Add confirmation, eval, guardrail, source-return, or supersession condition; use the receiving evaluation or governance pattern. |
| `PackageOrderAsGovernance` | The latest file by number is treated as active without explicit status or supersession. | Add package map or status fields; make active, proposed, superseded, and related relations explicit. |

### C.32.ADR:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| ADR is a publication projection. | Records stay readable while decision authority remains in PAD. | Authors must maintain the relation between record and decision. |
| Section functions are stable even when headings vary. | Software ADR, engineering memo, and certification rationale can be compared by function. | Local templates must be mapped rather than copied blindly. |
| Method and work effects are visible. | Developers can act on the decision instead of only reading rationale. | Records may need exact method refs and work-split refs. |
| Supersession is explicit. | Future readers can distinguish history from current decision. | Record packages need simple upkeep. |

### C.32.ADR:10 - Rationale

ADR practice is valuable when it makes architectural decisions communicable and revisitable. It becomes weak when a record is treated as the decision itself or when a template substitutes for decision work.

C.32.ADR therefore uses the record as a projection. The decision relation is made in `C.32.PAD`; the record publishes a decision description for a declared reader. This preserves the strongest ADR practice, small and updateable records, while adding FPF kind control for architecture descriptions, method descriptions, evidence, assurance, gate, publication, and performed work.

The pattern also generalizes ADR practice beyond software by using section functions rather than software-specific carrier assumptions. A record can be a Markdown file, engineering memo, or certification rationale if it projects the decision description and keeps receiving claims with their governing patterns.

### C.32.ADR:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.ADR. Keep a source citation only when it changes section function, projection boundary, or update condition.

| Source to inspect | Why this source is load-bearing here | Transfer into ADR projection | Concrete ADR mutation | Blocked overread |
|---|---|---|---|---|
| Michael Nygard, `Documenting Architecture Decisions` (`https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions`) | Foundational practitioner source for small decision records with context, decision, status, and consequences. | Preserve the small-record and future-reader practice. | C.32.ADR requires status, context, decision outcome, consequences, and supersession or reopen condition. | The ADR record is not the decision relation or the architecture description. |
| MADR 4.x (`https://adr.github.io/madr/`) | Current Markdown ADR practice with options, outcome, status, links, and confirmation. | Use options, outcome, links, and confirmation as section functions rather than fixed FPF ontology. | Required section functions include candidate options, decision outcome, confirmation or eval exit, and package links. | "Any decision" scope is not imported as architecture-decision kind expansion. |
| ISO/IEC/IEEE 42010:2022 official standard (`https://www.iso.org/standard/74393.html`; IEEE page `https://standards.ieee.org/ieee/42010/6846/`) with the 42010 companion site as secondary reading (`https://iso-architecture.org/42010/`) | Current official source for architecture descriptions, viewpoints, views, correspondence, and rationale. | Keep architecture views as cited description refs inside the ADR projection. | ADR rows carry `architectureDescriptionRefs` and publication boundary instead of copying view content wholesale. | A 42010 architecture description is not an ADR projection and not a PAD relation. |
| 2026 ADR violation-detection research (`https://arxiv.org/abs/2602.07609`) | Recent research shows explicit decisions are easier to check, while implicit deployment or organization knowledge remains weak. | Make confirmation, violation-detection scope, and non-code source refs explicit. | ADR section functions require confirmation or eval exit, source-return condition, and method or deployment refs when live. | LLM-detectability is not evidence, assurance, or gate passage. |
| Current FPF `E.8`, `E.17`, `E.24.PUB`, `A.15`, `A.10`, `B.3`, `C.30.AD`, and `C.32.PAD` | Existing FPF patterns govern pattern form, publication, method work, evidence, assurance, architecture description, and decision relation. | Keep ADR projection thin and typed. | The record maps section functions and exits neighboring claims to their governing patterns. | ADR projection does not duplicate pattern language, MVPK, method, evidence, assurance, gate, or description doctrine. |
| NASA Systems Engineering Handbook, decision analysis and trade-study practice (`https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf`) plus domain certification-rationale practice where governed locally | Non-software engineering decisions are commonly recorded through trade studies, engineering memos, review records, safety cases, or certification rationale. NASA supplies a concrete source for alternatives, criteria, assumptions, recommendation, impacts, and decision documentation. | Generalize by record function and reader use rather than by Markdown file convention. | `publicationCarrierRef` can be a memo, trade-study record, certification rationale, or design-review record, while section functions still recover problem frame, options, outcome, rationale, consequences, confirmation, source return, status, and supersession. | Non-software carrier form does not change the PAD decision relation or section functions. |

**Source-currentness boundary.** Recheck a source row when ADR template practice, decision-record tooling, violation-detection practice, architecture-description practice, FPF publication patterns, or project governance changes the section function or update rule used by C.32.ADR.

### C.32.ADR:12 - Relations

- **Builds on:** `C.32.PAD`, `C.32.P2S`, `C.30.AD`, `C.30.ASV`, `E.17`, `E.24.PUB`, `A.15`, `E.8`, `E.11.PUR`, and `C.32.ADA`.
- **Decision boundary:** Use `C.32.PAD` for the project architecture decision relation. C.32.ADR publishes an `ArchitectureDecisionDescription@Project`; it is not generic ADR guidance and not a second decision authority.
- **Structural-information boundary:** ADR-like projections may cite `C.33`, `C.34`, or `C.35` only to show captured structure, lost structure, preservation adequacy, generated-carrier typing, or discovered-carrier typing behind the projected decision. The ADR projection remains a publication projection of a decision description; it is not the architecture, the decision relation, or generated-carrier authority.
- **P2S docking:** P2S may cite an ADR projection as one stage where decision, rationale, method expectation, and source-return are published for readers; ADR does not carry the whole architecturing flow.
- **Architecture-description boundary:** Use `C.30.AD` and `C.30.ASV` for architecture-description and view adequacy. ADR carries refs and reader-use slices, not full description authority.
- **Pattern and method boundary:** Use `E.8` when the published object is an FPF pattern, `E.11.PUR` for pattern-use recommendation, and `A.15` for method and work claims.
- **Publication boundary:** Use `E.17` and `E.24.PUB` for MVPK face, publication carrier, and publication-use claims not specific to architecture decisions.
- **Evaluation boundary:** Use `C.32.ADA` for decision adequacy; use `C.32.ACE`, `C.16`, `A.10`, `B.3`, or `A.21` for eval, measurement, evidence, assurance, or gate claims.
- **Package boundary:** A record package map aids navigation among records. It does not decide active architecture by file order; PAD relations and status refs remain governing.

### C.32.ADR:13 - Footer marker

C.32.ADR closes when `ArchitectureDecisionRecordProjection@Project` cites the decision relation and decision description, names carrier, readers, scope, status, section-function mapping, decision outcome, rationale, consequences, method and work refs when live, confirmation or eval exit, publication boundaries, and update or supersession condition.

### C.32.ADR:End

