## What this specification is (and how to use it)

This document is the **Core Conceptual Specification** of the **First Principles Framework (FPF)**. It defines a small, domain-agnostic kernel and a set of extension patterns for **publishing, checking, and evolving conceptual work** about *systems* and *epistemes* (knowledge claims) — and about the organisations and communities that build them. In FPF terms these are all **holons**: things that can be treated as wholes and as parts.

FPF is written as a **pattern language**. A pattern is not a tutorial and not a “best practice” blog post; it is a reusable **action-guidance form**: *Problem frame → Problem → Forces → Solution*, ending with a **Conformance Checklist**. The canonical template, terminology registers, and the interpretation of RFC-2119/8174 keywords live in **E.8**.

One important cluster of the Core deals with a recurrent real-world problem: teams often have to work with language that is **not yet stable enough** to count as a finished claim, endpoint judgement, or action record, but is already too important to leave as private intuition or carrier noise. In engineering, inquiry, and operator work this shows up as under-articulated cues, partial formulations, candidate route cues, abductive prompts, and endpoint-governed publications.

FPF therefore treats this not as one vague maturity sequence but as a governed region of a declared **language-state chart** over `U.CharacteristicSpace`, with explicit facet sources, admissible transduction moves, receiving-pattern seam publications, and explicit handoff to receiving endpoint governing patterns. That cluster is what lets an engineer-manager say, in a disciplined way, not only *what is already known*, but also *what is emerging, how far it is articulated, how closed it is, how it is anchored, which receiving governing patterns or publication forms remain live, and which receiving governing pattern or publication form should receive it next*.

The current operational subset of that cluster is already present inside the Core. It includes corridor-reading notes in `C.2.2a`, `C.2.LS`, and `A.16`; the checked language-state support patterns `A.16.0`, `A.16.1`, and `A.16.2`; naming and lexical governing-pattern discipline in `F.18`, `E.10`, and `A.6.P`; the checked downstream load-family specializations `C.16.Q` and `A.6.A`; same-described-entity textual re-expression in `A.6.3.CR`; the **non-latent case family** of same-described-entity representation-scheme transition in `A.6.3.RT`; explanation classification over existing MVPK faces in `E.17.EFP`; publication-unit problem-kind classification in `E.17.AUD`; local lexical-head repair in `E.17.AUD.LHR`; `PublicationUnit` stability over one primary described entity and carried move in `E.17.AUD.OOTD`; and bounded comparative reading over comparative review units in `E.17.ID.CR`. In other words, the monolith now carries not only the early language-state corridor itself, but also the checked language-governance and support-pattern families that keep that corridor admissible, plus the first downstream families for same-entity rewrites, representation changes, explanation-facing renderings, publication-unit problem-kind classification, local head restoration, `PublicationUnit` stabilization, and bounded comparative review units. This material is integrated as Core baseline for this corridor, its checked language-governance and support branches, and its first downstream families, but it does not license latent/decode-mediated `A.6.3.RT` cases as part of that settled non-latent case family. Those latent or decode-mediated `A.6.3.RT` cases remain outside the current non-latent case family.

**What is in this document (map)**
- **Part A - Kernel Architecture Cluster:** holons, bounded contexts, role and scope discipline, transformers, time/evolution, work-planning and plan-to-work seams, measurement/comparability foundations, and the signature-stack and boundary-discipline family.
- **Part B - Trans-disciplinary Reasoning Cluster:** aggregation, emergence, trust and assurance, canonical evolution and reasoning cycles, pre-abductive routing, abductive prompting, creative search entry, and bridge-use families.
- **Part C - Kernel Extension Specifications:** the extension calculi and characterization families - Sys/KD/Kind/Method/LOG/CHR, measurement, creativity, NQD, explore/exploit policy, discipline health, problem typing, method-maturity, agentic tool-use, and quality-bundle patterns.
- **Part D - Multi-scale Ethics & Conflict-Optimisation:** axiological neutrality, multi-scale ethics, conflict topology, trust-aware mediation, and bias and ethical-assurance overlays.
- **Part E - The FPF Constitution and Authoring Guides:** vision, pillars, guard-rails, didactic architecture, authoring protocol, lexical law, human-facing working-model discipline, multi-view describing/publication governance, transduction-graph architecture, review gates, and DRR-based evolution governance.
- **Part F - The Unification Suite (U-Suite):** concept-set building, local naming, role descriptions, mint/reuse discipline, bridges, status mappings, method-quartet harmonisation, harnesses, and human-facing publication surfaces such as UTS.
- **Part G - Discipline SoTA Patterns Kit:** CG-Spec, CG-Frame kit authoring, SoTA harvesting and synthesis, admissible characteristics/calculi authoring, selector/dispatcher patterns, shipping surfaces, and telemetry and refresh discipline for repeatable domain packs.
- **Parts H-K:** glossary, annexes and extended tutorials, indexes and navigation aids, and tracked lexical or migration debt.

The navigation clusters below are **reading clusters**. They are not new governing-pattern families and do not relocate semantics out of the patterns they reference.

- **Language-state navigation cluster (C.2.2a-C.2.7, A.16-A.16.2, B.4.1, B.5.2.0, A.6.3.CR, A.6.3.RT, E.17.EFP, E.17.ID.CR, E.17.AUD.LHR, E.17.AUD.OOTD, C.16.Q, A.6.A):** how FPF models positions in a language-state chart, admissible transduction trajectories between those positions, early seam publications, route publication, local head restoration, `PublicationUnit` stabilization, abductive handoff, and the first same-entity textual, representational, explanation-facing, local-head-restoration, publication-unit-stability, and bounded comparative-reading families without flattening them into one vague maturity story.
- **Project-alignment navigation cluster (A.1.1, A.15, A.15.2, A.15.3, B.5.1, F.9, F.11, F.17):** how FPF establishes local semantic framing, role-method-work alignment, plan/run separation, a simple project/process reading, bridge-aware alignment, and a first human-facing work sheet.
- **Boundary-discipline navigation cluster (A.6, A.6.B, A.6.C, A.6.P, C.16.Q, A.6.A):** how FPF unpacks contract-language and interface boundaries into L/A/D/E-classified atomic claims, claim registers, precision-restoration branches, and auditable publication faces without mixed-boundary drift.
- **Comparability & selection navigation cluster (A.17-A.19, A.19.CN, A.19.CPM, A.19.SelectorMechanism, G.0, G.5):** how FPF declares characteristics, governs comparability, keeps comparison distinct from selection, and produces admissible selected-set or set-result outcomes without hidden scalarization or hidden thresholds.
- **Generator, SoTA, and set-result navigation cluster (A.0, G.0, G.1, G.2, G.5, G.11, C.17-C.19):** how FPF authors a reusable generation, harvest, selector, or set-result scaffold with explicit comparability governance, set-return selection, and open-ended search discipline.
- **Same-entity rewrite, explanation, and comparative-reading navigation cluster (A.6.3.CR, A.6.3.RT, E.17.EFP, E.17.ID.CR, E.17.AUD.LHR, E.17.AUD.OOTD):** how FPF restates, re-renders, explains, repairs, stabilizes, and compares already-authored epistemes and publications without silently changing the described entity or minting a second semantic track.

**Where to start**

The order of Parts in this document follows the didactic architecture of the
Core. A first practical entry does not have to follow that macro-order.

This guidance is coarse entry orientation only. It introduces no new norms and
does not change authoritative pattern meaning.

> **Preface is high-recall, low-detail.**
> `J.4` is the compact canonical entry index.
> `I.2` is the worked-reading depth role.
> The pattern's own `Problem frame` is the local high-precision first-reading
> role.

Choose the first entry by what you are really trying to decide, publish, or
stabilize, not by chapter order.

Consider a human-facing stabilizing result early when vocabulary, decision
criteria, or publication need to stay shareable. A typical admissible stabilizing
result is `F.17 (UTS)` when vocabulary alignment is live; other live questions have
their own publication or review forms.

Use `B.3` when assurance, trust calibration, or evidence transport is already part of the
present question. Use `E.9 (DRR)` when a change to normative content,
authoritative pattern meaning, or durable canon rationale must actually be
published; do not treat it as a universal day-one gate.

- For the **why**: inspect `E.1-E.2`.
- For **writing or reviewing patterns**: inspect `E.8` and `E.19`.
- For **project alignment** - contexts, roles, method, plan, run, and a first
  shared work or vocabulary stabilizer: inspect `A.1.1`, `A.15`,
  `A.15.2`, `A.15.3`, and `B.5.1`. Consider `F.11` when method vocabulary and work vocabulary
  must be aligned across contexts, `F.9` when bridge discipline matters, and
  `F.17` when term stabilization is the live question.
- When the real situation is **partly-said cue and language-state discovery**:
  inspect `C.2.2a`, `C.2.LS`, and `C.2.4-C.2.7`,
  `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, and `B.5.2.0`. Consider endpoint patterns
  such as `C.16.Q`, `A.6.A`, or `C.25` only when the live question is actually
  endpoint-owned.
- For **boundary unpacking** - API, contract, protocol, `SLO/SLA`, acceptance
  clause, compliance text, or interface language: inspect `A.6`, `A.6.B`, and
  `A.6.C`. If the first question is only "what description is this?", inspect
  `A.6.RSIG` before L/A/D/E-classified claim structure. Add `A.6.P`, `C.16.Q`, or `A.6.A`
  only when relation, quality, or action wording is the live question.
- For **admissible comparison, pool, selection, or selected-set publication**:
  inspect `A.19:0`, `A.17-A.19`, `A.19.CN`, `G.0`, `C.18`, `C.19`, and `G.5`.
  Consider `C.11` only when the live question has narrowed to one local decision
  doctrine, and `C.24` only when the next live object is a `CallPlan` or
  `CheckpointReturn`.
- When the work is to publish a **reusable generator, SoTA, or portfolio kit**:
  inspect `A.0`, `G.0`, `G.1`, `G.2`, and `G.5`. Consider `B.5.2.1` and
  `C.17-C.19` when creative search, novelty, or explore/exploit policy is
  already central. Consider `G.10` or `G.11` when shipping or refresh is live.
- For **same-entity rewrite, explanation, representation change, repair, or
  bounded comparative reading** without minting a new described entity: inspect
  `A.6.3.CR`, `A.6.3.RT`, `E.17.EFP`, and `E.17.ID.CR`. Consider
  `E.17.AUD.LHR` for pressured-head local repair and `E.17.AUD.OOTD` for
  `PublicationUnit` stability.

`Preface` helps the reader begin entry; it does not become one second `J.4`.
Update `Preface` when the global entry map changes or the center of gravity of
`FPF` shifts materially. If only one local nearby-pattern cue or one
worked-reading branch changes, that is not automatically one reason to rewrite
`Preface`.

Everything in the Core is intentionally tool-agnostic. Implementation details
belong to Tooling and worked examples belong to the Pedagogical Companion. The
rest of this `Preface` provides non-normative motivation and reading heuristics
for the patterns that follow.

