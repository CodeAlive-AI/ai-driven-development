## E.19 - Pattern Quality Gates: Review and Refresh Profiles

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative

### E.19:0 - Use this when

Use `E.19` when one exact new, substantially revised, or aging FPF pattern edition or bounded subset needs a repeatable admission, refresh, or return-for-repair review. `E.19` supplies profile-based questions and conclusion semantics. A reviewer applies the selected questions and returns either repaired text with focused verification or actionable findings.

Use it especially when a draft looks structurally compliant but may still fail on first-minute usability, primary `EntityOfConcern` stability, terminology, SoTA grounding, related-pattern boundaries, examples, anti-patterns, or shipping-facing authority claims.

**Not this pattern when.** Use `E.8` to write the pattern body. Use `E.9` to record the content decision that explains why FPF should change. Use `E.9.DA` when the question is whether one exact DRR is adequate for a declared downstream authoring use before drafting or host amendment; its ordinary result may be precise findings or repaired text, while exact C.2.1 and coordinate-result apparatus is conditional on a requested reusable result or named reliance. Use `E.21` for ordinal pattern-quality evaluation of one exact pattern version. Use `E.23` when the aim is repeated quality improvement against an object-under-improvement evaluation rather than one admission or refresh review profile. Use local patterns for the domain rule or constraint being reviewed. Use project gate or release patterns when the question is whether a project publication, work-result record, or release candidate passes a delivery gate. E.19 governs review of FPF pattern admission/refresh only; its profiles and results do not certify the world, project, publication, or release.

### E.19:0.1 - What goes wrong if missed

Review collapses into heading compliance or personal taste. A draft can pass because it has the right headings while still being hard for a practitioner to recognise, too thin against current practice, unclear about its primary `EntityOfConcern`, relation record, or claim record, or misleading about related patterns and the authority each pattern's content actually carries.

### E.19:0.2 - What this buys

`E.19` gives authors, reviewers, and stewards a shared review profile: what must be checked, how deep the check should go, which defects block admission or refresh, and what evidence is needed before a pattern-quality claim is made. It also makes the recognition text visible before the heavier assurance machinery begins.

**First useful move.** Name the reviewed pattern edition or subset and the admission or refresh question. Select `PCP-BASE` plus only the risk profiles the question needs. Inspect the affected loci, then repair and verify each defect or return the actionable findings.

**Local-repair boundary.** If baseline triage shows that the current review question has no present ontology, usability, SoTA, boundary, naming, or authority risk beyond a small mechanical repair, close with that repair direction. Do not run every profile just because `E.19` exists, and do not claim an `E.21` quality value unless `E.21` has evaluated the pattern version over its required coordinate set.

**Three quick recognition situations.** The same review move should be visible before the profile details:

| What the reviewer sees | Risk-selected move | First useful result |
| --- | --- | --- |
| A safety-critical subsystem-deployment pattern adds a condition in prose but not in its Solution or Conformance Checklist, introduces scope-hiding terms, and treats matching cross-team labels as identity. | Apply `PCP-BASE`, `PCP-NORM`, and `PCP-TERM`; add `PCP-BRIDGE` only if the text actually claims a relation across contexts. | Repair and recheck the requirement, terms, and identity claim, or return one actionable findings set. Solution and checklist constrain the same system claim; project deployment permission remains under its own governing rule. |
| An episteme or publication pattern still reads smoothly, but its sources are stale, its Relations use superseded names, or a carrier is treated as the claim it carries. | Apply `PCP-BASE` and `PCP-REFRESH`; add `PCP-TERM` for the claim, publication, or carrier confusion. | Update and verify the affected Solution, source use/currentness, publication/carrier distinctions, and Relations, or return complete findings. Handle historical-only evidence as lineage under E.8. |
| A Method pattern says that the Method or checklist performed dated work, leaving the acting system, Work, and result hidden. | Apply `PCP-BASE` and `PCP-TERM`; add `PCP-MOD` only if the text mixes guidance with an actual occurrence. | Restore plain Method guidance and state the acting system, Work, and result separately only when an actual occurrence is claimed. |

**Primary EntityOfConcern in plain terms.** One FPF pattern edition or bounded subset under an admission or refresh review question. The selected checks, reviewer, any repair, findings, optional aggregate result and evidence use, and any authority-bearing decision remain distinct when those objects are current.

**Primary working reader.** The first reader is an FPF reviewer, with the pattern author close behind. The review must still be answerable to the eventual practitioner or manager who will rely on the admitted pattern.

### E.19:1 - Problem frame

FPF evolves by adding and revising patterns. Over time, the framework accumulates two kinds of risk:

1. **Admission risk** — a newly authored pattern can be structurally compliant yet still fail on ontology, semantics, terminology conflicts and vagueness, scope, SoTA in related disciplines, or cross-context hygiene.

2. **Staleness risk** — older patterns can remain internally consistent while drifting away from contemporary practice and newer parts of FPF, current internal vocabulary, or updated related patterns and their defining or constraining content. The result is “quiet decay”: the pattern still appears clear, but becomes misleading, incomplete, or incompatible.

FPF already contains many checklists and constraints, but they are distributed across patterns and suites. Authors and reviewers therefore lack a single, repeatable way to answer: *What should be checked, and how deep, before a pattern is admitted or kept?*

### E.19:2 - Problem

Without a unified, explicit review pattern:

* Different reviewers optimize for formal or template compliance and miss deeper ontological, semantic, and naming issues, producing bureaucratic output that does not improve the enforceable Conformance Checklist.
* Authors “optimize for the visible checklist” and miss hidden requirements (lexical discipline, Bridge hygiene, SoTA‑Echoing quality, scope claims, delta‑class impact).
* Older patterns accumulate conceptual staleness and diverge from current practice, current terminology, or current internal invariants.
* The specification's normative content becomes harder to trust: compliance becomes a matter of reviewer taste rather than a repeatable gate.

### E.19:3 - Forces

| Force                                   | Tension                                                                             |
| --------------------------------------- | ----------------------------------------------------------------------------------- |
| **Uniformity vs Fit**                   | One universal checklist is simple ↔ different pattern kinds carry different risks.  |
| **Rigor vs Editorial cost**             | Deep audits increase quality ↔ they must remain feasible for routine updates.       |
| **Stability vs Evolution**              | Canon should stay stable ↔ it must absorb new SoTA and correct mistakes.            |
| **Conceptual purity vs Enforceability** | Core must stay implementation-agnostic ↔ gates must still be actionable and auditable.     |
| **Local meaning vs Reuse**              | Patterns must remain context-bound ↔ authors want to reuse ideas across domains. |
| **Freshness vs timelessness**           | Some claims should be evergreen ↔ others decay and must be refreshed on cadence.    |

### E.19:4 - Solution — Profile-based gates for admission and refresh

Establish **Pattern Quality Gates (PQG)**: a conceptual family of profile-based declarations for admission and refresh checks rather than a single monolithic checklist.

A **Pattern Check Profile (PCP)** is a named bundle of check families. Profiles are **additive**: every review configuration includes the baseline profile and only the risk-driven profiles needed by the declared question. A PCP specifies questions and closure conditions; the reviewer applies them and returns findings or repaired text. An unselected profile requires no result row or durable disposition.

Choose review depth from the harm if a defect survives, the novelty and complexity of the claim, how widely the pattern will be reused, and how likely its sources or neighbors are to change. Pattern length, official status, and the number of available checks do not justify deeper review by themselves. Use cheap automated or template checks for properties they can actually test, then spend reviewer attention on semantic, ontological, practitioner-use, and current-source questions they cannot close.

**Terminology note (disambiguation).** PQG and PCP are editorial review constructs in the authoring plane (Part E). They are distinct from enactment and runtime gating constructs such as `OperationalGate(profile)`, `GateProfile`, and `GateDecision` (A.21), which govern Work transitions and gate decision policies elsewhere in FPF.

**Mint vs reuse.** This pattern mints **PQG**, **PCP**, and the profile IDs `PCP-BASE`, `PCP-MOD`, `PCP-PRAG`, `PCP-NORM`, `PCP-SOTA`, `PCP-BRIDGE`, `PCP-SUITE`, `PCP-P2W`, `PCP-TERM`, `PCP-DEONT`, `PCP-REFRESH`, and `PCP-ENTRY`. It reuses existing FPF terms (e.g., **Delta-Class**, **DRR**, **Bridge**, **CL**, **SoTA Synthesis Pack**) without changing their meanings.

For an ordinary bounded review, keep the reviewed edition or subset, question, selected profiles, checked loci, defects or repairs, and conclusion. When exact replay or a named later use needs a stronger account, also keep independently recoverable:

1. the exact reviewed FPF pattern edition or bounded subset and the declared admission/refresh question;
2. the review configuration: baseline and risk-selected PCP declarations, exact question scope, use, qualification window, and stop boundary;
3. the semantic review `U.Method`, when that identity matters; call an episteme its `U.MethodDescription` only after it passes A.3.2;
4. for each actual review, repair, or verification occurrence asserted as dated `U.Work`, recover every exact actual performer through A.13 and use A.15.1 to identify its time, Method, containing System, and Work independently. Add F.6 only when the review account expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment. That attribution must be independently grounded rather than inferred from holder identity or timing, and a missing or failed F.6 link leaves the Work intact;
5. each exact PCP check application and A.6.1 binding only when the receiving use must replay those bindings;
6. any distinct authoring/repair work, changed pattern edition, and focused verification work/application in inspect-repair-verify form;
7. actionable finding or blocker claims, focused-verification claims, and one C.2.1 aggregate E.19 review-result episteme when a durable conclusion is required;
8. any separate authority-bearing admission, refresh, return-for-repair, or waiver decision and its decision work;
9. witnesses, A.10 evidence-use or provenance relations, and any B.3 assurance or reliance result when those claims are made; and
10. any F.10 status use, publication occurrence or form, carrier, and currentness relation used by the receiving claim.

Any local system-role kind and its independently evaluated classification are optional separate claims; neither supplies assignment or performance. Route unresolved source *role* through `E.10.ROLE`, and name intended-reader or representation positions directly. When a later claim relies on a dated occurrence, apply item 4 and `CC-E19-0`.

The phrase **review run** is Plain shorthand for that configuration, the reviewer's actions, and their results. The §4 account keeps the declarations, applied Method, actual review work, findings, result, and any authority-bearing decision distinct when those identities are needed.

#### E.19:4.1 - Define the reviewed pattern or subset

Name the reviewed pattern or bounded subset, its edition or other stable version basis, the admission or refresh question, the selected profile questions, and the review boundary. That is enough for an ordinary bounded review. Add exact scope, window, and review-configuration identities only when a receiving result or named reliance needs them. Profile choice selects the questions and review depth; an ordinary bounded review requires no progress record.

When a reusable result or named reliance depends on how the review was enacted, apply the item 4 actual-Work account and `CC-E19-0` to each asserted review, repair, or verification occurrence. If a durable aggregate result is needed, constitute a C.2.1 result episteme whose EntityOfConcern is the reviewed pattern edition or subset and whose ClaimGraph states the review scope, applicable profile questions, actionable findings or aggregate cleared boundary, conclusion, and reopen condition. Add a non-use boundary only when it changes a named receiving use under the `F.19` plausible-intended-reader test. Witnesses, evidence use, the optional result publication, and any authority-bearing admission or refresh decision remain separate.

Choose inspect-repair-verify when the reviewer may edit and same-turn repair fits the declared use. Choose independent findings when the review needs separation from the author or an unchanged candidate. Independence changes who edits; it does not add a dossier or expand the selected questions.

**Choose one review form.** An `E.19` review has two forms:

1. **Inspect, repair, and verify.** One bounded review may include inspection, repair, and focused verification. A reviewer performs those actions; distinguish their performer, Method, affected object, or occurrence only when the positions differ or a named later use needs them. Apply item 4 and `CC-E19-0` if the account asserts dated Work. Apply every selected question, repair every in-scope defect, and reapply the affected checks. The changed edition and focused verification carry the substantive evidence; constitute an aggregate E.19 result episteme only when a receiving admission or refresh decision requires it. Make a separate findings record only for an unresolved blocker, a decision outside current authority, or transfer to another author.
2. **Independent findings.** A reviewer applies the selected questions without changing the reviewed pattern or subset. One C.2.1 findings-result episteme or semantic handoff records every actionable defect and blocker, with repair direction precise enough for the author to act without repeating the diagnosis. It is neither the reviewing action nor an admission decision.

A selected question that reveals no defect requires no durable pass entry. Independent review does not accumulate positive recitals, and inspect-repair-verify does not duplicate completed repairs in a parallel findings record. If another pattern defines a reusable value or decision required by the declared use—such as an `E.21` coordinate, a `DRR` decision, or a landing result—that value belongs to the result required by that pattern rather than to an `E.19` progress account. `E.19` specifies the substantive questions and outcomes independently of how a working environment keeps place during the review.

**Complete the selected scope.** Inspect every independently answerable question in the declared baseline and risk-selected scope. The first defect, blocker, or already-negative admission conclusion may prevent a positive verdict, but it does not complete the review and does not suppress findings that remain independently obtainable. Stop before the selected scope is complete only when a missing source, missing authority, unsafe boundary, or equivalent condition makes the remaining questions impossible to judge truthfully or safely. In that case, record the unexamined scope and why it cannot be judged; do not present the partial findings set as complete.

A nontrivial pattern-quality review SHOULD state its quality-evaluation purpose before depth is selected. Use `E.22` or an equivalent compact question frame to say whether this review is a `floorEvaluation`, `exceptionalImprovementEvaluation`, `paretoTradeoffEvaluation`, `openQuestionDiscoveryEvaluation`, `absorptionEvaluation`, or a declared combination. If the purpose is absent, `E.19` treats the review as an admission-refresh blocker read, not as a request to raise every evaluated coordinate toward exceptional expression. When coordinate values, `PatternQualityStatus`, or all-`4`/all-`5` claims are needed for one pattern version, the review opens or consumes an `E.21` result instead of assigning those values inside `E.19`.

When the review opens or consumes `E.21`, `E.19` treats `E.21` as a hard pattern-quality evaluation, not as a selectable profile. The review must not accept an `E.21` claim that omits required coordinates, omits `ShortRationale`, omits `PrecisionRestorationProfile`, uses inactive/triggered-coordinate language, narrows the requested use to make the result pass, or replaces coordinate values with blocker triage. In inspect-repair-verify, repair or re-evaluate the affected result where that work is in scope; in independent findings, record the exact defect. Baseline triage can answer only the `E.19` review boundary when no `E.21` quality value, all-`4`/all-`5` claim, landing-quality claim, or pattern-improvement movement claim is being made.

If the aim is repeated improvement against an object-under-improvement evaluation, use `E.23` for the repeated method. An E.19 review configuration may supply PCP questions and its result episteme may supply findings inside that loop, but a profile is not the loop method and an E.19 result is not an ordinal quality value. Only a separate E.21 assessment application and result episteme can state the E.21 coordinate values for the changed pattern version.

`E.19` reviewer and reviewed-pattern wording is FPF pattern-quality gate wording. It governs FPF admission, refresh, return-for-repair, blocker, and review-profile claims, not `E.21` coordinate assignment and not project-side publication interpretation, explanation interpretation, comparative review-unit use, or participation in a named project-side review relation. When those project-side relations are used, use the publication or project-side pattern that names the object being interpreted or reviewed.

**Project-side reuse boundary.** Use this boundary when an E.19 review-result episteme is cited as project certification, project evidence, safety-assurance material, gate input, release justification, compliance-assurance material, assurance material, work authority, or publication truth. First identify the exact FPF pattern-quality claim it states: admission, refresh, repair return, or selected pattern-quality boundary. Any project-side reuse then opens the concrete relation that governs that use: `A.10` for evidence/currentness, `B.3` for assurance, `F.10` for status use/interpretation, `A.20` for a current local CV status when applicable, `A.21` for gate decision, `A.15` for work, or the relevant project-side pattern. The E.19 result may be evidence about FPF pattern quality; it is not certification of the project world. Plain wording in the reviewed text remains ordinary unless it changes admissible use, evidence, gate, assurance, work, decision, status use, or FPF pattern application. A project refusal or approval requires a project-side governing relation that states the project claim and its admissible use.



Formal or template defects (e.g. non-compliance with E.8 structure or not conforming to RFC deontic terminology) have lower review priority than semantic or ontological defects or non-SoTA Solutions. In inspect-repair-verify, repair them within the declared boundary; in independent findings, record them with concrete repair direction.

E.g. if the header block is missing or incomplete, **continue with ontology and semantic review first**. Treat missing header fields as one mechanical defect, not as a reason to stop (PCP-BASE #7).

When a proposed or accepted pattern change needs a best-known **Delta-Class (Δ-0…Δ-3)** and initial **impact radius**, place them in the governing change, decision, or landing result using E.15's actual-effect and actual-dependency tests. `E.19` repairs or reports an omission that matters to the selected review; it does not copy a successful change account into a second review record.

#### E.19:4.2 - Apply the baseline profile to every run

Every run MUST include **PCP‑BASE** as a triage baseline. Full-depth checking
is selected only where the relevant risk is present; reviewer depth SHOULD
prioritize the FPF-governed sections and enforceable requirements in E.19:4.2.1.

1. **Internal coherence (problem <-> conformance claim <-> solution)**
   The Conformance Checklist matches Problem statement and the Solution (no "orphan requirements" and no "unclaimed requirements").
2. **Lexical discipline & reserved vocabulary**
   Terms and registers follow lexical rules; ambiguous "everyday" synonyms do not silently replace kernel vocabulary.
3. **SoTA-Echoing minimum compliance (E.8)**
   SoTA-Echoing satisfies the E.8 authoring requirements applicable to the pattern kind (Architectural vs Definitional), including explicit adopt/adapt/reject stances and the E.8 two-part SoTA test: current best-known problem-solving practice for the named practice question, and by-value incorporation into FPF-governed pattern loci. If a SoTA Synthesis Pack exists for the topic, SoTA-Echoing binds to it rather than forking an untracked narrative; any divergence of pattern norms from contemporary practice is explicitly stated as such. SoTA-Echoing **MUST** be non-decorative, **MUST** reflect best-known current practice rather than official status, source recency, institutional adoption, or merely popular defaults for the declared problem, and **MUST** govern the Solution and other FPF-governed sections, or those sections **MUST** justify divergence explicitly.
4. **Cross-pattern compatibility & impact radius**
   Relations are consistent with declared dependencies and dependents; declared scope/impact is compatible or explicitly limited.
5. **Didactic grounding**
   Archetypal Grounding is present and teaches the concept with concrete cases or references, not only abstractions.
6. **Reader-fit**
   The pattern body addresses the intended FPF user in the working role governed by that pattern. FPF developers, package architects, reviewers, and evaluators are appropriate readers when they occupy that role. FPF-governed sections explain admissible use, costs, boundaries, the concrete definitions, constraints, tests, or other contributions used from FPF patterns named by value, project-side FPF kinds and references named by value, and related relations named by value in user terms. Architecture placement, freeze or merge state, package-boundary rationale, reference boilerplate, quality or projection evidence, corpus-entry evidence, `PatternQualityStatus`, monolith-parity evidence, landing evidence, and broader package-development rationale stay in `DRR`, architecture documents, review handoff, `E.21` result, `E.19` findings, README, ToC, `E.11`, `I.2`, cards, retrieval or projection carriers, release or landing evidence carriers, companions, or ordinary references unless they change the working reader's first admissible move.
7. **Template & section integrity**
   This is lowest priority for review depth and **SHOULD NOT** consume effort that would displace ontology, semantics, modularity, slot discipline, or SoTA checks.
8. **Modularity & contradiction hygiene**
   The pattern **SHOULD NOT** be overloaded or significantly expand requirements or dependencies without an explicit reason and impact record.
   Checks include: scope containment, split/refactor recommendations when warranted, and contradiction scans against neighbor patterns in Relations.
   The pattern SHOULD balance cohesion and coupling across FPF.
   If the pattern defines specialization or an abstraction stack, it SHOULD NOT mix slot interfaces or parameters from different abstraction positions; use explicit `⊑/⊑⁺` or `Uses` cuts instead.
9. **Substantive solution and locus adequacy**
   Baseline triage includes a small reviewed-pattern-specific question set about the actual problem and current change: does the pattern still solve the stated problem, are decision loci and applications of the relevant patterns correct, are kind boundaries and selected companion or projection functions preserved, did anything get worse, are SoTA rows current enough for the claim they discipline, and is the support material required by that claim neither too thin nor too heavy?
10. **Triggered method, performer, work, and result separation**
   When a Solution says how work should be done, first distinguish content that defines, constrains, tests, or guides a Method from an assertion that one dated Work occurrence or world-side change actually obtains. Method guidance alone does not trigger a fictive performer or Work. If an account asserts dated `U.Work`, verify the §4 actual-Work account; if it asserts a world-side change, identify the change relation, the pattern that defines it, and the things it relates. Keep the intended-reader position, any qualifying A.3.2 method-description episteme, actual performer, Work, and problem-facing result separate. For a literal dated `U.Work` claim, return a finding when an episteme, checklist, plan, prose, or intended-reader or representation position is made to perform Work, or when Work and result are collapsed. Judge ordinary or metonymic wording through the complete-claim test in `F.19`; a familiar instrumental expression alone does not require a formal Work account.

##### E.19:4.2.1 - Triage: spend depth on FPF-governed sections without making reviews heavier

PQG is meant to increase *semantic and ontological trust*, not to turn every review into an exhaustive editorial audit on form. To keep reviews feasible while improving the important parts:

* Treat **FPF-governed sections and deontic requirements** as the primary depth loci:
  * the pattern’s **Problem frame**, **Rationale**, and **worked slices** when a new family, profile, or specialization would otherwise be intelligible only from project context,
  * reader fit in **Problem**, **Solution**, **Consequences**, **Rationale**, and worked slices whenever the draft risks mixing user guidance with package-development rationale,
  * the pattern’s **Conformance Checklist** (the enforceable conformance check set): keep items universal, cognitively ergonomic, not overly prohibitive, and avoid duplicating checks that belong to other patterns (modularity),
  * **deontic clauses** (`MUST/SHALL/SHOULD/MAY`) that define requirements on the authoring/validation plane (not laws of nature or mathematical facts; ensure an explicit conformance subject),
  * **admissibility constraints** (`Invariant:` / `Well-formedness constraint:`) that define valid models (cardinality, typing/kinds, totality) and are written as non-deontic predicates (no RFC keywords inside the predicate),
  * **definitions and mint/reuse decisions** (new terms, renamed terms, scope claims baked into names, names that are not overloaded and are properly chosen),
  * **cross-context and cross-plane claims** (Bridge hygiene and “sameness” assertions),
  * **SoTA** (when the pattern claims state-of-the-art rather than a popular-but-outdated solution or vocabulary),
  * **substantive solution and locus adequacy**: one reviewed-pattern-specific content pass checks whether the repaired text still solves the stated problem, assigns claim-bearing material to the correct governing loci named by value, preserves kind boundaries and selected companion or projection functions, keeps quality/projection evidence and executor/reviewer correspondence out of the pattern unless the pattern's own `EntityOfConcern` and user-facing action are that evaluation/projection work, and has not become either under-grounded or over-bureaucratic,
  * **modularity and Slot discipline of A.6.5** that provide evolvability of FPF,
  * **absence of contradictions in a pattern**,
  * **Relations** that define compatibility and impact radius.
* Treat **low-signal text** as “quick-pass” unless it changes meaning: headings, micro-typos, stylistic polish, and non-FPF-governed narrative refactors, including RFC-form deontic cleanup. Automate a check only when the tool tests one clearly named property. A clean result closes only that property; it cannot establish semantics, ontology, practical usefulness, or source currentness.
* **Do not block semantic review on template and RFC compliance defects.** Missing header block fields (E.8 H-5), missing canonical sections, or a missing footer marker are fixable integrity defects. Record them as repair items and continue with the FPF-governed section checks in the same run.
* **Whole-span precise language.** Reviewers SHOULD apply `F.19` to the selected FPF-governed span. Its semantic reading, precision-before-coarsening order, MG-DA cold-reader recovery, and hypergeneric/specialization test supply the common language check.
* **Precision-restoration distribution must be preserved.** Apply `CC-E19-21`; keep only review-specific questions here and use the declared language or subject owner for the repair.
* **Review-specific continuity questions.** Apply these to the changed claim and affected uses:
  1. Is the pattern's own `EntityOfConcern`, first useful move, practical delta, and any action-changing applicability boundary recoverable, with its action guidance before auxiliary wording, publication, architecture-placement, package, or quality apparatus?
  2. After wording or reference migration, does the claim still reach the same referent through the intended slot or reference position and alignment path? Record any deliberate retargeting in the governing change decision.
  3. When phrase apparatus, semio bias, architecture placement, package rationale, or quality apparatus changed, did the repair preserve the function that was actually needed and remove only the displaced apparatus? Name each outside definition, constraint, or test by its supplying pattern and use a formal identity only for a live distinction or named reliance.
  4. Do the affected current consumers still receive the intended meaning and use? Resolve semantic, mechanical, or compatibility changes in the affected sources; report unresolved conflicts rather than creating a disposition for every unaffected consumer.
* **Use preservation and guard selection are different decisions.** Always compare the admissible uses of the old and repaired claims under their governing rules, including any expansion or narrowing. The `F.19` plausible-reader test decides whether an explicit description, publication-use, or non-use guard deserves mention. A justified guard still undergoes the same before/after use comparison. Use `F.19` and the direct owners for Method, Work, evidence, assurance, gate, status, decision, and unresolved *role* claims; dated Work uses `CC-E19-0`.

When E.21 is active, its `PrecisionRestorationProfile` carries the quality result; E.19 does not duplicate it.
* **Design-time and run-time both count.** The same precision discipline applies to FPF pattern prose and to any reviewed publication text, worked slice, or performed-work exemplar when that text is being assessed for admissibility, guidance, reuse, gating, release, policy, assurance, or action-selection use.
* **Report ordering (impact-first).** In run outputs and remediation direction, prioritize findings on ontology, semantic, modularity and SoTA-related FPF-governed sections first; group low-signal formatting/typos into one compact tail finding unless they change meaning.

#### E.19:4.3 - Add risk-driven profiles

**PCP‑PRAG (Pragmatic utility & adoption)** — Trigger: the pattern is Normative and claims practice guidance.
Checks include: a visible first-reading recognition text early enough for a cold working reader; a recognisable first-minute working situation; one short `Use this when` or equivalent entry; a plain statement of what goes wrong if the pattern is missed; a plain statement of what the pattern buys in practice; the first admissible action-guiding move the user should take; a visible ordinary `not this pattern when` boundary; a minimally viable example; non-decorative Consequences/Anti-Patterns; at least one worked slice when the pattern is easy to misuse; a visible assurance text carrying declaration, guidance/check, modeling, and review/check scope; reader-fit consistency so that the assurance text does not silently widen or universalize the recognition-text claim; explicit practical payoff in user-facing prose; a short user-facing statement of the primary `EntityOfConcern`, relation record, or claim record and any minimal modeling lens when typed declaration material has FPF-governed use; nearby pairwise plain glosses for FPF-governed technical terms that appear before the heavier harness; a short working-reader implication for any `SoTA-Echoing` rows that carry explanatory work plus visible linkage to the worked cases or boundary slices they discipline; explicit primary working reader, concern, and viewpoint when several working-reader situations are being served; an explicit `So what?` adoption test; and, when the pattern claims universal or transdisciplinary reach, heterogeneous recognition-text situations adequate to the claimed breadth with `F.16` preferred as the compact example-matrix template.
When admission or refresh includes precise-language repair, apply `CC-E19-7a`. It preserves practical guidance and the Plain/Tech relation under `E.2` `P-2` and `E.12`, with formal identity and dated-Work checks only under the conditions stated there. `F.19` governs the whole-span repair; `E.10` supplies compact cues and FPF routing.

For a broad cleanup across several patterns, or any cleanup that touches FPF-governed Problem frames, Problem sections, first-use recognition text, archetypal grounding, examples, or worked slices, check whether the didactic function was harmed. In inspect-repair-verify, restore the working situation, first useful move, and the definition, constraint, test, or other pattern contribution needed by the claim; in independent findings, record the exact harm and repair direction. A positive `improved` or `preserved` account is required only when another evaluation makes that value one of its substantive results, and it belongs in that evaluation.

**PCP‑MOD (Modularity and abstraction-boundary discipline)** — Trigger: the reviewed pattern or subset shows scope creep or abstraction-boundary mixing (e.g., one pattern bundles universal core rules with frame-specific content and discipline-specific method semantics; or it mixes EntityOfConcern, Description, and Specification positions in one object).

Checks include:

* an explicit **core vs extensions** cut (universal invariants are factored into one stable “core”, and extensions reference it rather than re-stating or mutating it),
* no conflation of **specialization vs dependency**: use `⊑/⊑⁺` for refinement/extension and `Uses` for pipelines; do not mix their semantics,
* no conflation of package-form, concrete pattern-to-claim contribution, and package-relation functions: **Pack vs Kit vs Suite vs Family vs Bundle vs Cluster vs Profile vs Overlay vs Record vs Umbrella** are not interchanged, and the review states carrier status, the definition, constraint, test, or other pattern contribution actually used, and the package relation explicitly instead of leaving them implicit or varying them for style,
* description-lane descriptions and their publications do not grow mechanism semantics; for an MVPK face or projected publication form, no-new-claim checks that it introduces no claim beyond the selected episteme and no-shadow-default checks that it introduces no undeclared default. Keep the selected episteme, optional projection/construction, face, publication form, publication occurrence, rendering, and carrier distinct. The selected episteme has `U.View` membership only when exact E.17.0 conformance independently obtains; face status, projection, profile selection, and compliance with these two checks establish no membership or truth,
* slot-discipline hygiene for any ordered specialization set: SlotKind invariance is preserved and inherited operations do not gain new mandatory inputs (A.6.5 / A.6.1 specialization discipline).

**PCP‑REFRESH (Staleness & compatibility refresh)** — Trigger: staleness signals are present, for example an outdated SoTA claim, a renamed or superseded relation, terminology drift, or an explicit refresh window in a current source-use, change, or decision record.
Checks include:

* refresh-sensitive claims are identified and either (a) updated from the best current problem-relevant source line with matching Solution changes, or (b) explicitly scope-limited and labeled as historical lineage; source date, count, official status, or novelty alone does not establish current-best use,
* select living refresh only for a high-priority claim or pattern subset likely to change when new evidence or a changed neighbor appears. Monitor and reopen the smallest affected unit at a named trigger; return it to ordinary periodic review when continued surveillance no longer buys enough currentness for its cost,
* Relations are updated to current pattern IDs; deprecations/renames are handled via explicit continuity notes (no silent relabeling),
* when one new or substantially revised pattern subset is being prepared for send or landing, inspect the related patterns, the concrete constraints or tests they supply, companion patterns, Relations entries, and monolith-backed pattern sections that may require aligned edits. Repair an in-scope mismatch or return it as a finding. Successful alignment remains visible in the changed sources and the governing landing or release result, not in an E.19 pass recital,
* any long-lived companion, profile, check sheet, pattern-local companion row, review harness, or analogous selected non-pattern FPF kind-reference pair kept with the reviewed pattern or subset states its use question, the concrete pattern contribution or selected non-pattern FPF kind-reference pair it serves, admissible companion-only use, one real breakage if absent, and demotion or deletion condition when no such breakage exists.
* when the refresh causes Δ‑2/Δ‑3, verify that the governing change or decision result carries its actual-effect Delta-Class, actual dependent reach, and any DRR, focused verification, source-refresh, or F.9 consequence that the changed use really requires under E.15, F.15, and F.9; repair or report an omission rather than copying a successful account into E.19,

Trigger overrides are permitted but intentionally rare. Override a triggered profile only when its risk is genuinely absent in this case and a compensating check covers the live concern. When the override changes an admission, refresh, or other governing decision, place its reason in that decision basis; otherwise E.19 requires no separate positive override account.

**PCP‑NORM (Normative guidance integrity)** — Trigger: the pattern introduces or changes normative requirements, introduces new conformance items, or shifts downstream requirements.
Checks include:

* **Delta‑Class (Δ‑0…Δ‑3)** and **impact radius** are explicit (what breaks, who depends on this),
* requirements are testable in principle (conceptually), scoped, and non-contradictory,
* downstream patterns cited in Relations are compatible with the new guidance.
* where the change is Δ‑2/Δ‑3 or a new normative pattern is being admitted: a DRR exists and references the PQG findings (pointer is sufficient; no duplicated prose).

**PCP‑SOTA (Evidence and SoTA alignment)** — Trigger: the pattern’s Solution asserts “best practice”, “state-of-the-art”, or introduces new synthesis claims.
Checks include:

* each “best practice” claim or SoTA claim in the Solution is explicitly **bound** to SoTA‑Echoing rows (or to SoTA Synthesis Pack identifiers when used), rather than floating as ungrounded prescription, and those rows identify best-known current practice rather than popularity alone,
* the selected SoTA practice or source set answers the declared working problem and the relevant domain or practice tradition rather than merely justifying package placement, naming neatness, or pattern clustering,
* each SoTA row changes at least one FPF-governed outcome for the pattern: what the user may do, a source-supported applicability or reliance limit, which FPF pattern application must be named, or a claim's eligibility for a named release, policy, assurance, gate, action-selection, or adjudication use. An explicit rejected reading follows F.19's grounded-guard test,
* novel synthesis is not presented as established SoTA: it is either (a) framed as a scoped hypothesis with explicit limits, or (b) promoted into or registered as a SoTA Synthesis Pack entry before the pattern is admitted as normative guidance; a merely explanatory SoTA note that leaves the FPF-governed sections untouched is non-conforming,
* where traditions disagree substantively, the pattern makes the disagreement visible and states whether it adopts, adapts, or rejects each relevant source idea instead of silently selecting one tradition,
* retrieval or benchmark methods are used only when the relevant evidence relation is present; their dimensions do not become universal pattern-quality benchmarks,
* refresh‑sensitive claims (those likely to decay) are explicitly marked with scope limits, timespan notes, or lineage labeling when appropriate.

**PCP‑BRIDGE (Cross-context or cross-plane reuse integrity)** — Trigger: the pattern imports claims, terms, or norms across contexts, disciplines, or reference planes.
Checks include:

* explicit Bridge usage where required (no silent identity by spelling),
* Congruence and loss are made explicit where applicable,
* any cross-plane reuse is explicitly acknowledged and its penalties do not leak into unrelated assurances.

**PCP‑SUITE (Mechanism-suite integrity)** — Trigger: the reviewed pattern or subset introduces or revises a suite-level Description that enumerates multiple distinct mechanisms (e.g., `MechSuiteDescription` or a suite specialization) and/or changes suite requirements, conformance pins, or suite protocols.
Checks include:

* the suite remains a **Description-level** object: it enumerates member `U.Mechanism.EntityOfConcern` refs and declares shared requirements/pins, but does **not** define mechanism blocks (`OperationAlgebra`, `Transport`, `Audit`, …) and is not used as a mechanism node,
* membership has **set semantics**: `mechanisms` is duplicates-free and order carries no semantics; any intended ordering is expressed only in `suite_protocols`,
* suite protocols are **closed over membership**: if `suite_protocols` is present, each protocol step references a member mechanism (no “step points outside the suite”),
* the suite is not a family of implementations: it MUST NOT be encoded as a `MechFamilyDescription` (families remain “many realizations of one mechanism”, not “many mechanisms”),
* the suite does **not** mint transport exceptions: any cross-context, cross-plane, or cross-kind requirement remains Bridge-only; loss or penalty handling stays with `R/R_eff` only; the suite does not embed CL/Φ/Ψ/Φ_plane tables (references/pins only),
* CG/CN authority pins remain explicit references to the single governance card and legality gate: if suite protocols include numeric comparison/aggregation/scoring, they cite `CG‑Spec` (SCP + Γ-fold + MinimalEvidence) and (where applicable) `CN‑Spec`, rather than duplicating “local CG‑Spec-like” content,
* suite protocols contain **no hidden tails**: if UNM/UINDM/ULSAM are required, the protocol expresses them as explicit `Uses` steps and suite audit requirements cite the chosen mechanism ids/refs (no “implicit normalization/aggregation inside score/compare/select”),
* gate separation is preserved: mechanisms and guards use tri-state `GuardDecision := {pass|degrade|abstain}` and MUST NOT publish `GateDecision` or `DecisionLog`; `block` remains gate-level only (`OperationalGate(profile)`),
* defaults remain single-sourced: portfolio mode, dominance regime, and unknown/failure behavior are either pinned in `TaskSignature` or one policy-assignment record, or not claimed; the suite does not define competing defaults,
* when the suite claims reusable outputs, publish/telemetry is explicit and terminates via existing publication forms/faces (e.g., G.10 and/or PTM), not as a hidden tail inside a selection step.

**PCP‑P2W (Planned baseline & slot-fillings seam integrity)** — Trigger: the reviewed pattern or subset introduces or revises planned-filling content in one exact `U.WorkPlan` against an exact governed declaration member, including a publication or view of that content.

Apply the planned-filling rules in `A.15.3` to the changed plan content and its affected consumers:

* `A.15.3:4.0–4.4` govern declaration-local PlanItem content, declaration and member recovery, intended-performance and planned-value designation, target-declared cardinality, and positive intended-use meaning. Use the corresponding `CC-A15.3-01` and `CC-A15.3-03…09` questions.
* `A.15.3:4.2`, `4.5`, and `4.6` govern conditional reference/policy pins, independently established actual use, baseline-preserving comparison, and read-only publication. Use `CC-A15.3-11…14` for these uses.
* `A.15.3:12a–12b` supply the ordinary A.15.2 plan-content exit and the exact missing-source blocker when reusable typed use is needed but cannot be supported.

The declaration's own pattern defines member meaning and actual-use predicates; A.15.2/A.15.3 define the planned intention. Review the use actually changed under those rules, retaining the exact declaration and WorkPlan editions on which that use relies.
**PCP-TERM (Terminology & naming protocol)** — Trigger: the pattern introduces new terms, new U-kind pressure, new governed value names, new “unified names”, redefines existing labels, leans on FPF-governed phrases whose head kind or qualifier claim kind or admissible-use boundary is not yet restored, or uses FPF-governed trigger wording as if the word itself carried the needed kind.
Checks include:

* the “mint vs reuse” decision is explicit when a term is introduced or changed,
* naming follows the local-first naming protocol and avoids scope smuggling (role-word meanings, metrics, or stages baked into labels; overloaded words used as terms with a local sense). Remediation **SHOULD** use F.18 when its durable-name use condition applies,
* when `F.18` winner selection and `A.6.P` follow-through are both needed under their respective use conditions, treat them as one chain: inspect the candidate heads or phrases, kind conflicts, lexical conflicts, selected wording, and survival of the repaired phrase; repair a broken chain or return its exact defect rather than recording the successful chain as a pass account,
* use the semantic-area cues in `E.10:0.2` with F.19's whole-span reading. The accepted sentence itself or its governing declaration must make the relevant object, value frame, relation, work, authority reference, pattern application, publication kind, companion function, or conformance claim recoverable; repair or report any case where it does not,
* for unresolved generic heads or claim-bearing qualifiers, and for a subsequent comparison, escalation, downgrade, or other use that puts pressure on that interpretation, apply `F.19:4`'s precision-before-coarsening rule,
* when repaired wording still carries an architectural claim kind or admissible-use boundary, verify that the resulting primary `EntityOfConcern`, first useful move, outside work, and any `E.10.ROLE` disposition or package-form decision remain recoverable in the repaired text or the decision that set the boundary; repair or report a mismatch, and
* source-side old wording and continuity rules are respected.
**PCP‑DEONT (Deontic clause hygiene: RFC keywords)** — Trigger: the pattern conflates admissibility/validity constraints with deontic obligations (e.g., uses RFC keywords where a non-deontic Invariant: predicate is required).
Checks include:
* Deontic requirements are expressed with RFC-style keywords (see H-8);
* obligations are not smuggled into prose as informal imperatives. Admissibility/validity constraints are stated non‑deontically as `Invariant:` / `Well‑formedness constraint:` predicates and referenced from the Conformance Checklist when enforceable.
* **Subject discipline for RFC keywords.** If a sentence uses RFC keywords, its grammatical subject **MUST** be an agent or a published record or model whose required content is being constrained. State modeled-world admissibility or validity requirements as `Invariant:` or `Well-formedness constraint:` predicates and reference them from CC items when needed, under E.8 H-8 and `CC-SG.4`.

**PCP-ENTRY (Pattern-entry discoverability and entry-orientation changes)** —
Trigger: one change substantively affects how one reader recognizes, selects,
rejects, or reclassifies one applicable direct pattern body, applicable projection function,
first-entry pattern-comparison set, Problem-frame recognition signature,
expanded entry-disambiguation case, or entry lexical-query cue.

Trigger classification:

`PCP-ENTRY` is an editorial review profile under the existing `PCP` family.
PCP-ENTRY is risk-triggered rather than universal.
Use one lead review profile for the change, and import other profiles only for
their specific failure mode.

Use this risk-trigger model:

* **Trigger class 0 — micro-edit**
  punctuation, formatting, typo repair, grammar, or meaning-preserving
  compression with unchanged pattern-selection effect.
  No `PCP-ENTRY`, no compact pattern-local note, no evidence mode, and no parity scan
  are required.

* **Trigger class 1 — local recognition wording repair**
  one improved `Use this when`, `Not this pattern when`, or one removed
  sequence-implying phrase with unchanged candidate-pattern set and unchanged
  governing-entry or applicable-projection-function boundary.
  Only the four-question core check is required.

* **Trigger class 2 — substantive entry, companion, or projection change**
  one new or changed README scenario, ToC query cue, `E.11` entry-distribution locus, `I.2` expanded entry-disambiguation case, pattern, or applicable projection function
  newly treated as entry-bearing, one changed wrong-pattern or
  governing-entry or applicable-projection-function boundary, one changed local
  first-entry selection effect, or one substantive lexical-query cue change.
  The author runs the core check and adds at most one selected risk check if
  needed. A compact pattern-local note is conditional on the rationale need
  stated below.

* **Trigger class 3 — multi-companion-function or high-risk public entry change**
  one change affecting several selected projection or companion functions together, one
  public-entry rewrite, one often-misclassified entry-recognition function, or one newly
  introduced first-entry pattern-comparison set.
  The author runs the core check and adds only the relevant selected risk
  check, usually parity, wrong-pattern, public-entry, or expanded-entry-disambiguation-case
  adequacy.

* **Trigger class 4 — retrieval-facing, observed-failure, or measured-improvement change**
  one retrieval-facing companion or projection function changes, one observed misretrieval or repeated
  search failure is being repaired, or the patch itself claims measured
  discoverability improvement.
  One selected evidence mode may be required, but benchmark-style reporting is
  not the default.

* **Trigger class 5 — normative authority, kind, or durable-name change**
  one entry-selection split, stable-name settlement, label-family change, or other
  normative architectural rewrite is in scope.
  `DRR`, `PCP-TERM`, and `PCP-MOD` are the lead decision or review profiles as applicable;
  `PCP-ENTRY` reviews only the entry-facing effects.

Ordinary non-triggers include:

* punctuation, formatting, and typo fixes;
* meaning-preserving prose tightening;
* one bare mention of a pattern without changed entry-selection effect;

* local wording repair that preserves the current first honest entry-recognition function,
  candidate-pattern set, governing-entry or applicable-projection-function boundary,
  and first-entry pattern-comparison-set membership.

`PCP-ENTRY` reviews entry-facing effects alongside the independently applicable
`PCP-PRAG`, `PCP-MOD`, `PCP-TERM`, `PCP-NORM`, or other profile.
Its distinctive object is changed pattern-selection effect, changed first-use
entry-recognition function, changed first-entry pattern-comparison-set membership, changed tempting-wrong-pattern
boundary, changed Problem-frame recognition function, changed expanded entry-disambiguation case
effect, changed entry lexical-query cue, and changed semantic companion-or-projection function parity.

Its default review scope is one small core triggered check:

1. **No workflow implication**
   Entry text does not imply mandatory sequence, control transfer, handoff, or
   publication, carrier, or record sequence unless another governing entry or applicable projection function
   explicitly governs that semantics.

2. **Governing-entry boundary preserved**
   Entry, index, and lexical-query companion functions do not redefine the direct pattern body's `Problem`
   or `Solution`.

3. **First honest entry-recognition function preserved**
   The change does not make the first entry-recognition function or case signal misleading.

4. **No duplicate high-detail companion or projection function**
   The change does not create one new stale echo or one second high-detail
   companion or projection function outside the one applicable direct pattern body or applicable projection function already
   named for the claim.

A change pays only the review cost of the concern it actually changes.
Learning-order edits do not trigger `PCP-ENTRY` unless they also change
candidate-pattern set, governing-entry or applicable-projection-function boundary,
first honest entry-recognition function, or first-entry pattern-comparison-set membership.
Lexical-only edits do not trigger extra entry-review scope unless they change
pattern-selection effect or entry recognition.
Retrieval fixtures are not required unless retrieval-facing behavior is
explicitly claimed, one machine-consumed projection is in scope, or one
observed misretrieval is being repaired.

When the risk warrants more than that core check, the run may add only the
relevant selected risk checks:

* one parity check when more than one pattern-entry
  discoverability-bearing projection changes;
* one wrong-pattern check when misclassification is observed or independently
  plausible for the intended reader under F.19's grounded-guard test;
* one lexical check when subject-language divergence is substantive;
* one expanded-entry-disambiguation-case check when `I.2` changes or one high-risk
  first-entry pattern-comparison set still lacks depth;
* one public-entry check when coarse public entry wording substantively changes
  entry-selection effect or carries high public-entry risk;
* one retrieval check when the change is retrieval-facing or repairs one
  observed retrieval failure.

Substantial discoverability changes leave one compact pattern-local note only when the governing discoverability decision needs that rationale; use the current `DRR`, `PCP` result, patch note, or other governing decision result rather than an E.19 progress record.
That pattern-local note may stop at one explicit rationale when the risk is already
controlled by governing-entry or applicable-projection-function inspection, companion-or-projection function
partition, or one local wording repair.
It is not a separate review record unless the change is high-risk, disputed,
public-facing with substantive entry risk, or retrieval-facing.

When one compact pattern-local note is needed, it names only the changed companion or projection function, the
affected first-entry pattern-comparison set or pattern, the changed first-use entry-recognition function or
recognition signature, the governing entry or applicable projection function for the
claim or projection function, and the selected check if any.

Empirical evidence is required only when the change is:

* high-risk;
* disputed;
* retrieval-facing;
* repeatedly misclassified;
* public-facing with substantive entry-selection change, repeated failure, or one
  measured-improvement claim;
* or itself claims measured discoverability improvement.

`PCP-ENTRY-E4` is selected only when retrieval-facing behavior is explicitly
claimed, one machine-consumed projection is in scope, or one observed
misretrieval is being repaired.
Public-facing changes with substantive entry-selection risk usually select `PCP-ENTRY-E1`.
Lexical-hook changes usually select `PCP-ENTRY-E3`.
Changes across multiple projections or companion functions usually select `PCP-ENTRY-E5`.
Observed search or query failures usually select `PCP-ENTRY-E6`, optionally
together with `PCP-ENTRY-E3` or `PCP-ENTRY-E4` when the failure is lexical or
retrieval-facing.

Select only evidence modes needed for the changed entry risk. An unselected
mode requires no result row or durable disposition.
Selected evidence modes may include:

1. **PCP-ENTRY-E1 — cold-reader recognition or pattern-selection task**
   Given one real case signal, can one reader recover the intended applicable
   direct pattern body or one admissible candidate-pattern set?
   One tiny micro-task is enough. Ask for the alternative in item 2 only when
   an observed choice or independent local cues make it plausible for the
   intended reader and the distinction changes selection or use; otherwise
   omit that item.

   ```text
   Given this entry-recognition phrase, name:
   1. the first candidate pattern,
   2. when grounded, one tempting wrong pattern,
   3. the admissible entry stop,
   4. the governing entry or applicable projection function.
   ```

2. **PCP-ENTRY-E2 — wrong-pattern and wrong-entry trap**
   For an observed or independently plausible misclassification, can the reader
   distinguish the intended pattern, entry, or family from that alternative?
   Use direct problem and subject cues; add an explicit rejected alternative
   only when F.19's grounded-guard test warrants it.

3. **PCP-ENTRY-E3 — lexical query check**
   Does subject-domain phrasing retrieve the governing entry or applicable
   projection function without uncontrolled aliases?

4. **PCP-ENTRY-E4 — retrieval or `RAG` fixture**
   Does retrieval recover the governing entry or applicable projection function under
   exact-ID or keyword phrasing, under semantic paraphrase phrasing, and under
   projection-vs-governing-entry ambiguity, while keeping retrieved companion material,
   source faithfulness, stale echoes, and post-rationalized citation-like material distinct
   from the applicable direct pattern body?
   Retrieval returns the governing entry or intended projection cue before one
   stale echo, and answer-to-governing-entry faithfulness remains intact.
   When thin echoes are used, check that they carry a governing-entry reference.

5. **PCP-ENTRY-E5 — companion-or-projection function parity check**
   Check that one governing entry or applicable projection function stays unique
   and the changed companion or projection functions agree on first-use
   entry-recognition function, wrong-pattern boundary, projection-only status,
   and no claim beyond the Core pattern body's admitted use; they need not share
   identical wording or examples. Include any explicit absence note in that
   comparison; identical rows are not required either.

6. **PCP-ENTRY-E6 — observed failure or query-log capture**
   Does one observed misretrieval, wrong-pattern loop, or repeated query miss
   still survive after the repair, or has the failure actually been
   removed?

#### E.19:4.3.1 - Tiny golden case bank for regression and worked examples

Select a case that exercises the changed entry risk. Cases 1–4 specialize `I.2.4`, `I.2.2`, `I.2.6`, and `I.2.3` respectively; `E.11` governs the entry-distribution use, and the direct subject patterns govern the recovered claims. Cases 5–6 add search and retrieval stress under `PCP-ENTRY-E1` and `PCP-ENTRY-E4`. Another relevant E.11/I.2 case may be used. Select empirical evidence under `PCP-ENTRY`; unselected cases need no run or absence note.

The `tempting_wrong_pattern_or_wrong_relation` column is conditional on an observed or independently plausible reader mistake that changes selection or use. Leave it unused when that condition is absent; keep the case's positive recognition and admissible stop.

| Case | case_signal | expected_first_entry_pattern_comparison_set | candidate_patterns | tempting_wrong_pattern_or_wrong_relation | admissible_entry_stop | companion_or_projection_functions_that_help | projections_that_do_not_define_semantics |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | “we need a shortlist, not one winner” | pattern-comparison set for comparison, pool treatment, and selected-set result declaration | `A.19.CN`, `A.17-A.19`, `C.18`, `C.19`, `G.0`, and `G.5` when selected-set result declaration is claimed | treating `C.11` as one one-off choice when the real entry-recognition function is selected-set result declaration or candidate-set stabilization | admissible candidate-pattern set stabilised or selected-set result declaration opened | README scenario or `E.11` entry-distribution cue, one pattern `Problem frame`, one expanded entry-disambiguation case if compact cues still fail | one README blurb, one thin echo, one lexical-query row alone |
| 2 | “we have a vague cue, not yet a claim” | pre-articulation cue pattern-comparison set | `C.2.LS`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0` | forcing the cue into one endpoint-claim, quality, or assurance pattern too early | `entry-recognition-reclassified` or cue preserved for the admissible next entry-recognition function | README scenario or `E.11` entry-distribution cue, one pattern `Problem frame`, one case-linked `I.2` expanded entry-disambiguation case when needed | one coarse public entry projection alone |
| 3 | “this is the same EntityOfConcern re-expressed for another audience” | same-EntityOfConcern rewrite pattern-comparison set | `A.6.3.CR`, `A.6.3.RT`, `E.17.EFP`, `E.17.ID.CR` | changing the EntityOfConcern or creating a competing semantic rule track merely to serve another audience | `wrong-pattern-rejected` or same-EntityOfConcern rewrite opened | one expanded entry-disambiguation case, one pattern `Problem frame`, governing-entry pointer | one parallel explanatory blurb treated as one second pattern body |
| 4 | “the API says X” | boundary-claim unpacking pattern-comparison set | `A.6`, `A.6.B`, `A.6.C`, `A.6.P`, `C.16.Q`, `A.6.A`, `E.17` | treating one boundary phrase as one agent duty, promise, quality verdict, or generic agreement paragraph without atomic claim assignment or quality-term repair with recovered characteristic and scale | `boundary-claim-pattern-opened`, `quality-term-repair-exited`, or atomic claim set opened | one boundary-focused `E.11` entry-distribution cue, one pattern `Problem frame`, one expanded entry-disambiguation case where interface/access/confused-quality wording is common | one query cue or public entry projection treated as the governing entry |
| 5 | “I found a pattern by search, but I am not sure it is the right one” | one pattern-local recognition-signature case under the selected pattern-comparison set | one candidate applicable direct pattern body plus one case-near related pattern when needed | one lexical near-match or same-family pattern without governing-entry fit | `non-use-confirmed` or `pattern-selected` | one pattern `Problem frame`, one `E.11` entry-distribution cue, one lexical-query hook | one search-query row alone |
| 6 | “the LLM retrieved a helpful-looking paragraph but not the pattern” | one retrieval-facing first-entry pattern-comparison case | one applicable direct pattern body plus one applicable projection function | one stale thin echo or one projection-only companion function answered as if it were the governing entry | `governing-entry-opened` or `expanded-entry-disambiguation-case-needed` | one governing-entry reference, one projection-only status marker, one retrieval-facing pointer to the applicable direct pattern body | one thin echo chunk without governing-entry reference or projection-only cue |

In case 3, evaluate episteme identity separately under `C.2.1`: its discriminators are claim content, EntityOfConcern, and effective reference scheme. Changed wording or audience alone leaves that identity unchanged; a changed discriminator identifies another episteme. `A.6.3.CR` permits claim-preserving or explicitly loss-declared same-EntityOfConcern re-expression under its own use conditions.

Selected cases test:

* entry-recognition consistency;
* wrong-pattern or wrong-entry rejection;
* admissible entry-stop honesty;
* lexical-query discipline;
* thin-echo retrieval hygiene;
* and governing-entry and projection separation in the changed entry text.

When one empirical or retrieval evidence run is selected, keep recoverable the
facts needed to understand its question and result. A structured result may use
the following field names, including only those needed by that run:

```text
viewpoint_class
task_prompt_or_query
expected_governing_entry_or_admissible_candidate_set
near_miss_patterns_or_projection_functions_if_any
time_budget_if_relevant
success_criterion_if_relevant
success_or_failure_note
observed_failure_mode_if_any
rationale_or_repair_action
```

When retrieval evidence is selected, keep retrieval result, answer
faithfulness, and stale-echo result distinct without forcing benchmark-style
reporting on ordinary edits.
Use the retrieval questions in `PCP-ENTRY-E4`, including its conditional
thin-echo reference check.
Ordinary local guidance stays prose-only rather than minting one stable
governing-entry reference by default.

#### E.19:4.3.2 - Common hardening questions are triggered by review need

Open a common hardening question when the concern has FPF-governed use, is disputed, or is explicitly invoked by the reviewed pattern or subset. Inspect the relevant source and the reviewed loci. In inspect-repair-verify, repair any defect and verify the affected use; in independent findings, record the defect and repair direction. When the question reveals no defect, make no durable absence or pass recital.

Use these questions only for the selected review concern:

1. **Usability and working-reader fit.** Open this when first-reading recognition text, assurance text, first-minute working-reader usability, practical payoff, worked slices, primary-reader fit, or `E.8` / `E.12` / `E.13` / `E.14` / `E.17.*` / `F.16` checks can change the admission or refresh result. If a separate evaluation assigns a value, use that evaluation's result rather than copying it into E.19 findings.
2. **Scenario, anti-case, and utility-fit source set.** Open this when a scenario pack, anti-case corpus, pilot bank, utility tree, fitness catalog, or analogous source is actually relevant or substantively disputed. Record only a missing, misused, or failing source/case as an E.19 finding.
3. **Packaging, concrete pattern contribution, package relation, and shipping fit.** Open this for a publication, pattern-contribution, or package-relation claim. The changed sources and governing publication or release result carry successful alignment; E.19 repairs or reports a mismatch.
4. **Domain-tightened profile depth.** Open this when a domain-specific note actually tightens a selected profile. Apply its questions; do not add a second account of positive results.
5. **Accepted-decision or accepted-source-material carry-through.** Open this when the reviewed pattern, subset, or current change is claimed to implement an accepted `DRR`, repair findings, intake material, architecture source material, or other accepted source material named by value. Inspect each independently applicable decision against the reviewed loci and the concrete pattern, claim, companion, result, or accepted source that carries it; require exact predicate or defining `ClaimGraph` identity only when that decision or the named reliance needs it. Repair or report partial, missing, wrongly rejected, wrongly routed, or wrongly classified carry-through. The accepted source remains the decision source; E.19 does not duplicate decisions that are expressed sufficiently, inherited unchanged, correctly absent, or outside the reviewed subset. An `E.17.ID.CR` comparative review unit, `PublicationUnit`, publication form or face, source-pinned interpretation case, source material, or project-side review relation retains its own kind in that comparison.

For `PCP-ENTRY`, the ordinary compact pattern-local change note remains enough when the governed discoverability decision requires one; no separate E.19 account is created merely because the profile was checked.

#### E.19:4.3.3 - Pattern-Edition Use-Value Replay

Use this replay when an exact candidate pattern edition changes materially under `E.8:4.1.2`. Run it once on the stable candidate before acceptance or landing, not after each edit. Start with the bounded E.8 loop over the actual predecessor and proposed prose, then open only each affected prior-edition or candidate-only use whose result can differ, pinned to its exact basis and changed locus. Treat a change as mechanical only when the smallest relevant comparison shows that every materiality value named in `E.8:4.1.2` is preserved. A genuinely bounded local semantic edit opens only its affected use probe and changed wording group; physical rewrite size is not evidence.

When the candidate keeps, merges, removes, profiles, reuses, externally supplies, or omits a narrower contribution, apply the same-situation decision in `E.8:4.1.3`. If reuse or a gap answers the working question, verify which return is actually present: an available result of its own kind and supplying product, a MethodDescription reference, direct-source evidence, or a named unavailable result. For an external result, verify the exact result and supplying product, receiving use, practical discovery route, material currentness or availability, and the statement that it remains outside the receiving framework; state maintenance only when it changes that use. Otherwise the package still has a gap or omission. When the resulting stable set materially changes a promised problem family, verify the current `E.4.DPF.DA` D12 judgement for the resulting exact edition required by `E.8:4.1.3`. Reuse a matching current result when the exact edition, promised families, declared use, relied-on results, and relevant conditions did not change; E.19 asks for neither a duplicate package evaluation nor evidence that a revisit occurred.


Judge each affected use probe separately when its result can differ by exact predecessor or candidate-only basis, working use or relying work, expected first useful result, boundary, necessity, or evidence mode. One review may contain probes from both bases. A grouped verdict such as `uses preserved or added` or `usability preserved` cannot substitute for those judgements. E.19 does not prescribe a per-probe progress store: inspect-repair-verify repairs and verifies failed probes, while independent findings records only regressions, insufficiencies, invalid transfers, unsupported decisions, and blockers. When `E.8`, `E.21`, or another governing evaluation requires reusable dispositions or values, keep them in that evaluation's result rather than copying them into E.19 findings.

**Changed-wording check inside each affected prior-edition probe.** Keep the selected use probe as the outer unit. When a predecessor-bearing candidate materially rewrites a normative sentence or inseparable sentence group that carries the governed extension, action discriminator, first useful result, stop, or neighboring-pattern exit, give that wording group its applicable differential disposition below before closing the outer probe. Keep sentences together only when they serve one reader task and must receive one disposition; split them when their extension, action, result, or route can differ.

For each changed wording group:

1. pin the old and candidate wording and the exact use it serves;
2. state in plain language the subject, concrete action or choice, visible result, and any actual stop or exit needed by that use;
3. compare the old and candidate head and modifiers, modal force, admitted referents or actions, applicability boundary under its governing rule, and local interpretation burden. Check every widening or narrowing against that rule and the accepted change decision, independently of the reader-plausibility question in the next step;
4. if independent local evidence makes one rival reading plausible to the intended reader and its treatment can differ, test that exact case. Use the plausible-reader test to decide whether an explicit guard contributes to the final wording; the extension comparison remains required. Do not invent a nearest alien or excluded case merely to complete the review form; and
5. apply the differential disposition. `preserved` requires no unauthorized widening or narrowing and no greater decoding burden: a reader must not need campaign memory or an ontology-development memorandum to recover the action.

For a new action-guiding paragraph with no predecessor, do not invent history or a foil. Verify that the local wording exposes a recognizable situation, concrete action or choice, visible first result, and any independently grounded applicability or neighboring-pattern boundary needed for use.

Keep the cheap path cheap. Formatting, typo, link, citation, or exact-reference corrections remain mechanical when the smallest comparison proves that no `E.8:4.1.2` materiality value changed. A bounded semantic edit checks only its affected wording group and use probe. Reuse an earlier hunk or language result only when the object and compared editions, changed scope, and assurance question match this extension, modal-force, applicability, and interpretation-burden test; idea presence or broad-use preservation is not enough. This is one same-increment stable-candidate pass before acceptance or landing, not per-keystroke review, a new ledger, or a one-finding handoff.

**Prior-edition differential.** For one candidate pattern edition × one prior-edition use probe, distinguish the applicable disposition when the governing decision needs it:

| Disposition | Semantic test and recoverability |
| --- | --- |
| `preserved` | The situation, action, result, and any action-changing boundary carried by the prior use remain semantically available; every material changed wording group retains its head-and-modifier extension, modal force, admitted valid cases, valid rule-defined exclusions, and no-greater-decoding-burden condition. The declared use remains admissible and replayable from the pinned editions. |
| `improved` | The required old use and every required changed-wording boundary remain preserved, and the same bounded comparison also demonstrates an action, result, boundary, affordability, or interpretation-burden gain. |
| `transferred` | A discoverable handoff reaches one named neighboring pattern whose Solution carries the needed action guidance and exposes its result. A bare pattern ID or unreachable action is `regressed`. |
| `intentionally retired` | An accepted decision drops a harmful or false old action and supplies the corrected positive action or boundary as the recoverability endpoint. |
| `regressed` | A required action, result, risk disclosure, cheap exit, or usable handoff is absent; or changed wording changes modal force, widens or narrows admitted referents or actions without an accepted basis, alters a rule-defined applicability boundary, or makes the reader decode more unstated ontology. Repair or an explicit retirement decision is required. |

A use classified as unsupported historical residue before replay receives no differential disposition and supports no compatibility claim. New evidence of a valid old use reopens that classification instead of restoring wording silently. A required `regressed` probe prevents a positive conclusion, but it does not stop inspection of the remaining independent probes.

**Candidate-only adequacy.** Review one candidate pattern edition × one new intended-use probe against its exact candidate-only basis, never against invented history. Distinguish these outcomes when the governing decision needs them:

| Outcome | Semantic test |
| --- | --- |
| **adequate for the candidate-only use** | The selected basis, recognizable situation, concrete action or choice, first useful result, intended reader, and any independently grounded action-changing boundary are recoverable from the local candidate wording and executable enough for the declared use. |
| **absent or insufficient for the candidate-only use** | The use is only promised, named, over-broad, ambiguous, or unsupported; the intended reader cannot perform the action, distinguish the first result, or recover an applicability or neighboring-pattern boundary that the declared use actually needs. |

A missing candidate-only decision or basis is `absent or insufficient`; it never licenses a fabricated prior edition. Absence for a required new use prevents a positive conclusion but does not stop the other independent probes. Absence for optional breadth is non-blocking by itself but cannot support breadth, transfer, or exceptional-expression claims. If no exact new intended use is selected, no candidate-only check opens.

**Replay the positive Solution separately.** Judge the following over the candidate edition when their answers can differ:

1. the governed subject;
2. the recurring problem and ordinary failure;
3. an executable proposed move;
4. a first useful result rather than completed review apparatus.

**When the Solution uses a boundary or guard.** Judge each guard for which independent local evidence makes the exact rival reading plausible to the intended reader and whose presence changes action. Check whether any remaining guard merely supplies the outline that the positive Solution should state directly. Refine this question by boundary whenever boundaries can pass, fail, or route independently. This guard check leaves the rule-defined extension comparison above intact.

**When the Solution concerns a Method, work, or world-side change.** First distinguish content that defines, constrains, tests, or guides from an assertion of one actual occurrence. Method guidance alone triggers no fictive performer or Work. When an account asserts dated `U.Work`, verify the §4 actual-Work account; when it asserts a world-side change, identify the change relation, the pattern that defines it, and the things it relates. Keep the intended-reader position, any qualifying A.3.2 method-description episteme, actual performer, Work, and problem-facing result separate. A literal dated-Work claim is defective if an episteme, checklist, plan, prose, or intended-reader or representation position performs Work. Judge ordinary metonymy through `F.19`.

Follow the short first-use rendering's action and result logic against a concrete situation. Merely finding words such as `situation`, `move`, `result`, or `stop` is not evidence. Repair each failed item or record it as an exact finding with remediation direction; do not replace the replay with one prose-quality impression.

**Replay each triggered enumeration or coordination under `F.19`.** Apply its contribution, coordination/list, and foregrounding rules in `F.19:4`, including the return to a defining or testing pattern when an FPF kind, relation, or structure remains hidden. Review a member separately only when its membership or contribution can fail independently or require a different repair. An unchanged series still covered by its exact rule needs no positive recital, and a blanket `all lists are coherent` conclusion cannot replace this reading.

Desk replay is the ordinary evidence mode for affected uses, changed wording groups, new action-guiding paragraphs, the positive Solution, and enumerations. Escalate to a cold reader, AI agent, or observed-work exercise when competing actions remain plausible, a near-miss boundary or result distinction is not recoverable by inspection, a transfer is uncertain, or a missed failure has high consequence. When a claim extends recurring applicability beyond the exact cases, do not treat three examples alone—the traditional rule of three—as validation. When the claim's value or consequence warrants it, select a proportionate qualitative practitioner survey, action-research cycle, or case study. Evidence escalation is risk-selected; it is not a universal benchmark or an ordinary-rewrite requirement. E.19 defines repair or finding outputs while leaving ordinal coordinate values and `PatternQualityStatus` to the full E.21 evaluation.

#### E.19:4.4 - Decision outcomes

Complete the selected review scope before making an admission, refresh, or return-for-repair conclusion. A first defect or already-negative conclusion does not end the search for other independently obtainable findings. If a condition makes the remaining questions impossible to judge truthfully or safely, name the unexamined scope and the condition instead of presenting a partial result as complete.

**Inspect, repair, and verify.** Complete every in-scope review application, repair every defect through the relevant authoring work, and perform focused verification over the affected questions. The changed pattern edition and focused-verification claims are the substantive evidence and remain distinct from work; constitute one aggregate E.19 result episteme only when a receiving admission/refresh decision needs it. Record only an unresolved blocker, a decision outside current authority, or work that must transfer; do not create a parallel list retelling completed repairs.

**Independent findings.** Leave one compact C.2.1 findings-result episteme or semantic handoff containing all actionable in-scope defects and blockers, ordered by semantic impact, with repair direction precise enough that the author need not rediscover the diagnosis. If the selected questions reveal no defect, create neither an empty pass report nor positive checklist recital. The findings result is not the dated review work or an authority-bearing admission decision.

If a governing admission, refresh, `E.21`, `DRR`, publication, or release decision requires a durable conclusion or value, use its existing result. That result may cite E.19 findings or the repaired candidate; it does not turn per-question positive outcomes into a second review record.

**Precision-remediation order.** When a defect sentence combines a generic head, a claim-bearing qualifier, and mixed comparison-criterion pressure, remediation SHOULD follow the precision-before-coarsening rule in `F.19:4`. That rule supplies the head/qualifier/comparison order and the recoverable precise interpretation required for a later Plain, didactic, or coarsened restatement.

**Kind-restoration verification.** A wording, naming, or F.19 phrase-level repair does not succeed merely because the old trigger word disappeared. Recheck the pre-repair and post-repair kind, relation or claim kind, admissible use, and scope. If the repair narrows, widens, splits, or changes them without an accepted decision, repair it or keep the defect unresolved. The repaired object, focused verification, or governing decision carries this evidence; E.19 does not require a per-repair pass account.

**Ordering and effort.** Put ontology, semantics, modularity, and SoTA defects in FPF-governed sections before compact low-signal formatting findings. If semantic defects are present, address them before mechanical edits; formatting and micro-typos must not dominate the work by volume.

### E.19:5 - Archetypal Grounding — transfer across three pattern subjects

The three worked situations in §0.2 use the same review move: name the exact pattern edition and review question, apply `PCP-BASE` plus only the live risk profiles, inspect the complete selected scope, and either repair and recheck the defects or return one complete actionable findings set.

**Transfer result.** Profile selection and the two review forms transfer unchanged. Each subject keeps its own correctness question: system requirements agree with their conformance claims; episteme and publication uses keep claims, source use/currentness, publication occurrences, and carriers distinct; and Method guidance is distinguished from performed Work. A successful example from one case cannot stand in for either of the others.

### E.19:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** (applies to all patterns and all clusters).

Bias risks and mitigations:

* **Governance bias (Gov):** reviewers may over-prioritize compliance signals and under-prioritize teaching value.
  *Mitigation:* PCP‑BASE checks didactic grounding and internal coherence and prioritizes ontology and semantics.
* **Architecture bias (Arch):** internal package architecture can displace the problem-owning domain or practice.
  *Mitigation:* test EntityOfConcern, narrowed branch, and practical payoff against the domain/practice question and relevant SoTA under `CC-E19-7`.
* **Epistemic monoculture (Onto/Epist):** SoTA‑Echoing can become single-tradition name-dropping.
  *Mitigation:* use multiple traditions when the question or claimed breadth requires them; make substantive disagreement visible. Use F.18 for neutral durable naming when its use condition applies.
* **Pragmatic bias (Prag):** a pattern can be “correct” yet unusable.
  *Mitigation:* consequences and anti-patterns remain mandatory sections, surfacing material costs or limitations and grounded misuse or application boundaries under `E.8`; an already established boundary may be referenced.
* **Didactic bias (Did):** narrative quality can be mistaken for truth.
  *Mitigation:* conformance and SoTA‑Echoing sections bind claims to explicit requirements and lineage.

### E.19:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-E19-0 (Review, result, and decision remain distinct).** | The reviewer performs the review; the profile or checklist declares questions; the findings, review record, or optional aggregate result state review claims; intended-reader and representation positions specify audience or form; and an authority-bearing decision uses those claims under its own rule. If an account asserts actual review, repair, or verification `U.Work`, the §4 actual-Work account **MUST** hold; a compact result may omit only an assignment identifier unused by the receiving claim. Keep any local system-role kind and separate System-classification judgment distinct, and route unresolved source *role* through `E.10.ROLE`. | Prevents editorial declarations and records from acting as reviewers or authority without burdening an ordinary review with unused identities. |
| **CC-E19-0a (MVPK face and View boundary).** | When a PCP inspects an MVPK face or projected publication form, apply no-new-claim and no-shadow-default to the claims and defaults actually carried by that face/form. Keep selected episteme, optional projection/construction, face, publication form, publication occurrence, rendering, and carrier distinct. Assert `U.View` membership only for the selected episteme when exact E.17.0 conformance independently obtains; profile selection, projection, or compliance with these two checks supplies no membership. | Preserves publication/face discipline without turning E.19 into a View classifier. |
| **CC-E19-1 (Baseline triage is mandatory).** | Every configured PQG review **MUST** include **PCP-BASE** for the reviewed pattern or subset. When the baseline review is complete and finds no risk requiring another profile, the review may finish after any small mechanical defect is either repaired and checked or returned as an independent finding. This is only an `E.19` review boundary; it cannot support an `E.21` coordinate value, `PatternQualityStatus`, a claim that every coordinate is `4` or every coordinate is `5`, landing-quality claim, or improvement-movement claim without the complete `E.21` result required for that claim. | Ensures one shared triage floor without turning every review into a full audit or substitute quality measurement. |
| **CC-E19-2 (Profile selection covers the live risks).** | The review scope **MUST** name PCP-BASE, every risk-selected PCP, the risk selecting each additional profile, and any override. It **MUST** consider the whole current profile set rather than only the easiest visible family. When an override affects a later admission, refresh, or other governing decision, its false-positive reason and compensating check belong in that decision basis; successful profile choices need no per-profile pass entries. An unselected profile requires no result row or durable disposition. | Makes review depth repeatable without a separate record of successful checks. |
| **CC-E19-3 (Delta-Class and actual impact for material changes).** | If the reviewed pattern change is **Δ-2/Δ-3** under E.15's actual-effect test, the governing change or decision result **MUST** carry its Delta-Class, actual dependent reach, a DRR pointer when a material content decision was selected, and the focused refresh, verification, or F.9 consequences that the changed use requires. E.19 repairs or reports a missing or false account; it does not duplicate a successful one. | Keeps evolution controlled while leaving change evidence with the change decision. |
| **CC-E19-4 (Conformance-claim coherence is enforced).** | Inspect-repair-verify **MUST** eliminate orphan and unclaimed requirements by aligning the reviewed pattern's Conformance Checklist, deontic clauses, admissibility constraints, and Solution. Independent findings **MUST** identify each surviving incoherence and give concrete repair direction. | Preserves the CC as the enforceable conformance check set in both review forms. |
| **CC-E19-5 (Triage & noise discipline).** | The run **SHOULD** prioritize FPF-governed sections and deontic requirements (e.g. CC, content of deontic clauses and content of admissibility constraints, definitions, Relations, SoTA, modularity) and keep purely mechanical edits (e.g. RFC-form deontic cleanup) minimal. Template defects **MUST** be fixed before admission (or before closing a refresh run) but **MUST NOT** be used to skip semantic review. | Improves semantic trust without turning review into form-only compliance. |
| **CC-E19-6 (Review form and findings completeness).** | The review **MUST** choose one form from E.19:4.1 and inspect every independently answerable in-scope question even after the first defect, blocker, or negative conclusion. Inspect-repair-verify ends with every in-scope defect repaired and focused verification performed; independent review ends with one complete set of actionable defects and blockers plus concrete repair direction. A question that reveals no defect gets no durable pass entry. Early stop is allowed only when the remaining questions cannot be judged truthfully or safely, and then the unexamined scope and cause **MUST** be named. | Prevents both first-defect stopping and a third, report-producing review form. |
| **CC-E19-7 (Recognition text, assurance text, and self-containment).** | Admission or refresh runs for new and substantially revised patterns **MUST** check that a first-reading recognition text appears early enough for the intended reader, that the heavier assurance text remains visibly second rather than becoming the first real point of entry, and that the assurance text does not silently shift the recognition-text claim. The run **MUST** check for a recognisable working situation, what goes wrong if the pattern is missed, what the pattern buys, the first admissible action-guiding move the user should take, and an ordinary `not this pattern when` boundary; for any FPF-governed typed declaration or modeling lens, the run **MUST** confirm that a short user-facing statement exposes the primary `EntityOfConcern`, relation record, or claim record and the minimal lens that keeps it reviewable; the run **MUST** also check that the primary `EntityOfConcern`, relation record, or claim record keeps one stable kind across title, opening function, declaration function, worked slices, and related-pattern or companion guidance named by value rather than drifting between the named primary `EntityOfConcern`, an act, a work-result record, and carrier-placement labels. When a broader umbrella name and a narrower operative branch are both used, the run **MUST** check that the recognition text makes that stack explicit enough to identify the umbrella, the active branch, the primary `EntityOfConcern`, the move, and the wider work or process that still remains outside. The recognition text **MUST** start from a recognisable problem-owning domain or practice moment whenever that can be done without loss of precision, rather than opening first with internal package architecture or taxonomy language. Early FPF-governed technical terms **MUST** receive nearby pairwise plain glosses; transform-like families **MUST** carry concrete worked slices plus ordinary-vs-FPF-governed wording guidance where needed; and any `SoTA-Echoing` used as explanatory grounding **MUST** state a short practitioner or manager implication plus visible linkage to the worked cases or boundary slices it disciplines. If SoTA or practice tradition has FPF-governed use, the run **MUST** check that primary-EntityOfConcern choice, narrowed-branch choice, and practical payoff remain answerable to the relevant domain or practice rather than only to internal package architecture. If a pattern claims universal or transdisciplinary usefulness, the run **MUST** check that this breadth is already demonstrated in the recognition text through heterogeneous situations adequate to the claimed breadth, with `F.16` preferred as the example-matrix template. | Prevents architecturally correct but reader-opaque patterns and keeps broad claims from appearing only late in the assurance text. |
| **CC-E19-7a (Precise-language repair cannot leave inert recognition).** | If admission or refresh includes a precise-language repair, apply `F.19` to the changed span and use `E.10` only for compact FPF routing. Check that the intended reader can recover why the distinction matters, the reader use, and the pattern or rule contribution that carries any formal claim. Keep Plain or didactic wording ordinary when it adds no such claim; otherwise map it back to the repaired Tech reading. Add an exact assertion, predicate, `ClaimGraph`, or displayed identity only when it distinguishes truth, action, stop, or named reliance. If the Tech reading asserts dated Work, apply `CC-E19-0`. In inspect-repair-verify, restore any harmed working situation or first useful move; in independent review, record the exact harm. | Prevents type-correct cleanup from destroying practical guidance or forcing unused formal apparatus. |
| **CC-E19-8 (Whole-span precise-language repair).** | Apply `F.19` to the complete natural span, including predicates inside negation or modality, required operands and relational complements, referents, subject-predicate compatibility, coordination, lists, modifiers, guards, and governing-claim order. Use compact `E.10` cues to locate candidates and open `E.10.ARCH` or an exact subject pattern only while an FPF kind or relation remains unresolved. After a wording or syntax change, reread the changed sentence and only its meaning-dependent neighbors. Inspect-repair-verify leaves repaired wording and focused verification; independent review records only a failed repair or blocker. | Keeps precise language semantic and usable without duplicating `F.19` as a phrase-by-phrase account. |
| **CC-E19-9 (Package-form, concrete pattern contribution, and package-relation function-word discipline).** | Use the package-form and relation cues in `E.10:0.2` to check whether the text preserves the actual package form, concrete pattern contribution, and package relation. If a repair introduces or retains a head already occupied elsewhere in FPF, verify intentional reuse or repair/report the collision. | Keeps concrete pattern contributions, package relations, review functions, and package forms legible without recording successful collision checks. |
| **CC-E19-10 (Reader-fit discipline).** | Check the reviewed pattern or subset for the intended FPF user, an explicit primary reader/concern/viewpoint when several readers are served, and separation of user guidance from package-development, review, evaluation, projection, integration, or release reasoning about the same pattern version. Part E patterns may govern authoring or review as their declared subject matter, but that does not admit development correspondence about the current version. Repair each leak or return its exact locus as a finding; sections with no leak need no scan recital. | Keeps reviews from accepting conceptually correct but reader-confused patterns. |
| **CC-E19-10a (Quality/projection carrier leakage).** | Check whether pattern prose, including Relations, Rationale, SoTA-Echoing, worked slices, examples, tables, and the Conformance Checklist, contains corpus projection, retrieval/cold-reader evidence, publication parity, integration evidence, `PatternQualityStatus`, all-`4`/all-`5` posture, or development correspondence about that pattern version. This is a sentence-function check, not a lexical search. Move such material to the applicable `E.21` result, E.19 findings, README/ToC/E.11/I.2, projection, publication, integration, or release result and retain only the pattern's admissible user-facing move or boundary. | Prevents quality and projection proof from becoming pattern prose. |
| **CC-E19-11 (Precision before relaxation).** | If remediation preserves or introduces a Plain, didactic, or coarsened restatement of a repaired FPF-governed sentence, the run **MUST** keep a more precise upstream interpretation recoverable and must not let the softened form become the only wording with authority-reference claim kind or admissible-use boundary. | Keeps later readability aids subordinate to an explicit more precise interpretation. |
| **CC-E19-12 (Integration impact is checked).** | Before publication or integration of a new or substantially revised subset, inspect related patterns and the concrete constraints or tests they supply, companion notes, Relations entries, and affected published sections. Repair each in-scope mismatch or return it as a finding and name any genuinely outside boundary. Successful synchronization remains in the changed sources and governing publication, integration, or release result. | Prevents an isolated local improvement without duplicating synchronization evidence. |
| **CC-E19-13 (Usability and proxy-to-value are checked).** | For a new or substantially revised subset, check recognition versus assurance text, first-minute situation, practical payoff, ordinary boundary, worked slices, primary reader/viewpoint, and the applicable `E.8`, `E.12`, `E.13`, `E.14`, `E.17.*`, `F.16`, or local-equivalent questions. Repair or report a usability defect. If a score, coordinate, benchmark, projection signal, or all-`5` posture is used as value evidence, the governing `E.13` result—not an E.19 pass account—must carry intended value, proxy use, gains, losses, minimally viable value slice, and reopen condition. | Prevents visible review success from replacing practical value. |
| **CC-E19-14 (Scenario, anti-case, and utility fit are checked when applicable).** | When the domain has a relevant scenario pack, anti-case corpus, pilot bank, utility tree, fitness catalog, or analogous common source, use its applicable cases and qualities. Repair a failing case or return the exact failure, missing source, or out-of-scope boundary as a finding; do not record cases that revealed no defect merely to prove consultation. | Keeps common validation sources active without a separate consultation record. |
| **CC-E19-15 (Packaging, concrete pattern contribution, package relation, and shipping fit are checked).** | Before a publication or integration claim, inspect the relevant package form, the definition, constraint, test, or other pattern contribution actually used, package relation, publication function and authority reference, and the actual publication and integration facts. Repair or report any mismatch. The governing publication, integration, or release result carries the successful state claim; E.19 does not repeat it. | Keeps shipping claims truthful without a second state account. |
| **CC-E19-16 (Domain-tightened profile depth is applied).** | When a domain-specific depth note such as semio `FIT-*` applies, use it to tighten the selected PCP questions. Repair or report any defect it reveals; do not add positive or not-found recitals to an E.19 result. | Keeps domain-specific depth operative rather than optional folklore or extra reporting. |
| **CC-E19-17 (Companion-material retention is justified).** | When a new or refreshed pattern subset keeps a long-lived companion, profile, check sheet, pattern-local companion row, review harness, or analogous selected non-pattern FPF kind-reference pair, the retention basis **MUST** make its companion function explicit: companion use question, concrete pattern contribution or selected non-pattern FPF kind-reference pair served, admissible companion-only use, one real breakage if absent, and retention, accepted-source-material-only, or removal condition when no such breakage exists. Use the governing retention or design decision; no separate E.19 pass account is required. | Prevents companion material from remaining by inertia or becoming hidden authority after the pattern body already carries the usable guidance. |
| **CC-E19-18 (Substantive solution and locus adequacy is checked).** | A new, refreshed, or materially repaired subset **MUST** receive a pattern-specific substantive adequacy check unless the change is purely mechanical. Check whether it still solves the stated problem, assigns claims to the correct governing loci, preserves kind boundaries and selected companion/projection functions, keeps SoTA grounding current enough, remains usable without excess apparatus, and worsens no content relation. Repair each in-scope failure or return it as a finding and name any needed wider boundary. Questions that reveal no defect need no separate account. | Prevents clean checklists and terminology from hiding wrong content. |
| **CC-E19-19 (Accepted-decision carry-through is checked).** | When the reviewed pattern, subset, or current change is claimed to implement an accepted `DRR`, repair findings, intake material, architecture source material, or other accepted source named by value, inspect each applicable decision against the reviewed loci or the named concrete pattern contribution, claim, companion, result, or source that carries it. Require exact predicate or defining `ClaimGraph` identity only when the decision or named reliance needs it. Repair or report partial, missing, wrongly rejected, wrongly routed, or wrongly classified carry-through. The accepted source remains the decision source; do not duplicate decisions expressed sufficiently, inherited unchanged, correctly absent, or outside the subset. Keep `E.17.ID.CR` units, `PublicationUnit`, publication forms/faces, source materials, and project-side review relations in their governing kinds. | Prevents accepted decisions from disappearing without making E.19 their second authority. |
| **CC-E19-20 (Project-side reuse has its own governing result).** | Reuse outside FPF pattern-quality review requires a project-side governing result that names the project claim, relation, required evidence or assurance, and the exact contribution taken from E.19. The E.19 result remains scoped to the reviewed FPF pattern edition or subset. | Keeps pattern review and project-side decisions under their respective rules. |
| **CC-E19-21 (Precise-language distribution is preserved).** | When the reviewed change repairs language or edits its rules, check the selected distribution: `F.19` owns the common whole-span semantic and pragmatic repair; `E.10` supplies compact cues and exact routing; `E.10.ARCH` opens only for unresolved ontological recovery; exact subject patterns define or test the recovered object or relation; affected patterns keep only thin cues unless the recovered subject is their own EntityOfConcern. A review fails this row when an affected pattern grows a rival normal-pass algorithm, mandatory counterreading field, duplicate trigger registry, or check-internal attention mechanics. | Prevents pattern admission or refresh from duplicating the language method or reintroducing ungrounded guards. |
| **CC-E19-22 (EntityOfConcern and precise-language triage is applied).** | For the changed span and affected pattern texts, apply the review-specific continuity questions in §4.2.1 and the common `F.19` reading. Compare admissible use before and after independently of whether an explicit guard is warranted. Add formal identities only when truth, a live distinction, or named reliance needs them; apply A.3.1 and A.3.2 before claiming Method or MethodDescription, and `CC-E19-0` to dated Work. Use E.21 `PrecisionRestorationProfile` when that evaluation is active. | Prevents a type-correct rewrite from changing referent, path, use, or consumer behavior while keeping deep restoration auxiliary to the pattern claim. |
| **CC-E19-23 (Pattern-edition use-value replay preserves distinct outcomes).** | When `E.8:4.1.2` selects a material edition change, judge separately only the affected use probes and changed wording groups whose result can differ. Apply `F.19` to each group: compare its subject, predicate, participants, modal force, referents, operands, contribution, information order, and applicability boundary under its governing rule. Check widening and narrowing against that rule and the accepted change decision independently of reader-plausibility; use the plausible-reader test for explicit-guard contribution. Do not invent an alien case or guard. Replay the positive Solution and each coordination or enumeration member whose membership or contribution can differ. Reuse prior results only when object, editions, scope, and assurance question match. Run this once on the stable candidate before acceptance or landing; do not create per-keystroke review, a second ledger, or positive recitals. | Prevents broad-use preservation from hiding semantic drift while keeping bounded edits cheap. |

### E.19:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | How to avoid / repair |
| ---------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------- |
| **Primary-EntityOfConcern drift** | The draft appears to govern one thing in the opening, another in the declaration block, and a third in the examples or related-pattern or companion guidance named by value. | Review cannot tell whether the pattern defines or constrains a `PublicationUnit`, an interpretive move, a work-result record, or a whole process, so later naming and boundary decisions become unstable. | Stabilise one primary `EntityOfConcern` early, keep its head kind explicit, and mark note, sheet, UI, rendering, or process labels as either examples of that object or separate related entities rather than stylistic substitutes. |
| **Reader-fit clean but pragmatically foggy** | The draft is addressed to the right reader in principle, but cold working readers still cannot recognise the situation, practical payoff, primary `EntityOfConcern`, relation named by value, claim record, or first useful move early enough. | The run passes reader-fit hygiene while still failing pragmatic fit and first-minute usability. | Pull a recognisable working situation upward, add one minimally viable worked case, make the practical payoff explicit in nearby user-facing prose, expose the primary `EntityOfConcern` and any minimal modeling lens in plain terms, add plain glosses for early claim-bearing terms, and require `SoTA-Echoing` rows that carry claim kind, admissible-use boundary, or explanatory work to name the practitioner or manager implication plus the case they discipline. |
| **Architecture-clean but domain-thin** | The text is internally well placed in the package, but the primary `EntityOfConcern`, narrowed branch, or practical payoff are justified mainly through package architecture while the problem-owning domain, practice, or SoTA appears late or decoratively. | The pattern passes internal architecture checks while drifting away from the domain whose work it claims to improve. | Pull the problem-owning domain moment into the recognition text, make the narrowed branch and primary `EntityOfConcern` answerable to the relevant domain or practice, and require FPF-governed `SoTA-Echoing` to discipline the practical cases rather than merely bless them after the fact. |
| **Type-correct but inert precise-language repair** | A `F.19` repair, located or routed with `E.10` when needed, restores kind language but leaves the reader unable to say why the distinction matters, what use remains, which definition, constraint, or test carries a formal claim, or how Plain wording maps back to the Tech reading when both registers are used. | The review accepts typed wording while losing action guidance. | Restore the working situation, reader use, and the contributing pattern or rule; map Plain wording back to the Tech reading when both are used. Keep the explanation ordinary unless a live contrast or named reliance needs an exact assertion, predicate, `ClaimGraph`, or displayed identity. Apply `CC-E19-0` only if the repaired claim asserts dated Work. |
| **Expressive overread rebound after precise-language repair** | The pass makes the text more engaging, but the added Plain or didactic wording carries an ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim not recoverable from the Tech reading or cited rule. | The review mistakes readability for recovered semantic work. | Keep the line ordinary when it only helps recognition. Otherwise recover the claim kind or admissible-use boundary through the Tech reading and cite the pattern or rule that defines or tests it; use a grounded non-use disposition only when the receiving use needs it, or return an incomplete rewrite. |
| **Profile or record as reviewer.** | A selected PCP, checklist, findings form, result episteme, or review record is said to have performed the review, repaired the pattern, admitted it, supplied assurance, or authorized downstream use. | Reviewer action, repair, result, evidence, and decision authority collapse. | Say ordinarily that a reviewer applies the questions and name the action actually performed. Profiles and checklists declare questions; findings and records state review claims. Apply `CC-E19-0` only when the claim deliberately asserts dated Work; add evidence, assurance, or decision relations only when they independently obtain. |
| **Verdict-only review** | Independent review ends with pass/fail or prose complaints but no complete actionable finding set, or repair-mode review reports defects without repairing and rechecking them. | Leaves later work to rediscover diagnosis or mistakes an intention to repair for a completed repair. | In independent review, record every actionable in-scope defect and blocker with precise direction; in inspect-repair-verify, repair and verify them. Questions with no defect get no durable pass recital. |
| **Single giant checklist** | Review becomes a long, unfocused ritual that few complete. | Increases cost; reduces fit and rigor in practice. | Use a minimal baseline plus risk-selected profiles; use `E.21` only when a pattern-version quality value is being evaluated. |
| **Template-only compliance** | All headings exist, but requirements are vague and untestable. | Looks uniform; fails enforceability and auditability. | Enforce normative clause hygiene and CC/Solution coherence. |
| **SoTA name-dropping** | SoTA-Echoing is a list of buzzwords with no stance. | Breaks evidence lineage; invites monoculture. | Require adopt/adapt/reject with reasons per item. |
| **Terminology drift by “synonym”** | Authors swap kernel terms for nicer-sounding words. | Increases ambiguity; harms cross-pattern composability. | Apply PCP-TERM and preserve established kernel terms. For a genuinely introduced term, use E.8 S-3's first-appearance gloss; use F.18 when a durable reusable name is needed. |
| **Lexical substitution accepted as repair** | The reviewed text no longer contains the trigger word, but the replacement changes the FPF kind, relation, current ontic slot, relation position, use relation, or claim kind, admissible use, or scope. | The review rewards surface cleanup while ontology drift remains or gets worse. | Apply F.19's `KindPreservationCheck` comparison; its separate result form is optional. If pre/post kinds or slots, relation positions, use relations, or claim kinds do not match and no accepted split/change decision supplies the change, keep the finding blocking. |
| **Form-only review** | Review time goes to formatting and micro-edits while the normative content, terms, Bridges, modularity, slot discipline and SoTA stance are barely checked. | Raises editorial cost without raising semantic trust. | Use the triage rule: treat FPF-governed sections as depth loci and keep mechanical cleanup subordinate to semantic correction. |
| **Checklist-clean but content-wrong** | The named profiles, lexical checks, and conformance rows are marked complete, but the repaired text no longer solves the stated problem, assigns a claim to the wrong locus, creates shadow authority, loses a selected companion or projection function, or adds needless boilerplate or support material. | Review accepts a locally tidy pattern while weakening the actual `FPF` guidance. | Apply substantive solution and locus adequacy: name local content questions, check the actual problem and governing loci named by value, ask what became worse, and widen the declared boundary by value when the fix belongs outside the initial reviewed pattern or subset. |
| **Architecturally right, didactically thin** | The family is admissible, but readers still need project notes to understand what the pattern really governs. | Trust in the pattern depends on external context rather than the pattern text. | Add the missing problem frame, worked slices, local definitions, and guidance naming the concrete contribution of a relevant pattern or the project-side FPF kind and reference before admission. |
| **Scenario-name grounding** | Grounding names a situation but does not show what the source and resulting publication actually look like. | Readers cannot tell why the case stays in the family or where it leaves the family. | Add concrete source and resulting-publication slices, especially for transform families and easy boundary confusions. |
| **Generic-head underspecification** | An FPF-governed phrase uses a generic head such as `note`, `view`, `guidance`, `output`, or `artifact`, but the run leaves that head uninterpreted. | Review discusses the sentence before the object kind is even stable. | Use the F.19:4 head-kind and precision-before-coarsening rules, with the object's defining pattern where its kind remains unresolved. |
| **Qualifier-smuggled claim kind or admissible-use boundary** | A modifier such as `comparative`, `safe`, `interactive`, `reliable`, or `faithful` is doing the semantic work while the run treats the phrase as already precise. | The review blesses apparent precision without recovering the actual claim kind or admissible-use boundary. | Use F.19:4 to unpack the qualifier's claim kind, comparison criterion, and admissible or downstream-use boundary before accepting the phrase. |
| **Mixed comparison criterion** | One sentence compares or ranks publication-form, carrier, process, authority-reference, or project-record values without a shared governed comparison basis. | The ranking's criterion or condition remains unjustified; different object kinds alone do not invalidate a shared criterion. | Use F.19:4's precision-before-coarsening rule and its comparison/condition-basis test. |
| **Sentence-level shorthand drift** | A few innocent-looking words (“species”, “branch”, “flow”, “input/output”) quietly carry the claim kind or admissible-use boundary. | Review passes while key relations remain implicit or wrong. | Read the complete affected span through F.19. Recover any missing claim, relation, definition, constraint, test, package relation, or publication meaning only where it changes the current use. |
| **Package-form, pattern-contribution, and package-relation drift** | The text slides between `family`, `bundle`, `cluster`, `profile`, `overlay`, `suite`, `kit`, or `record` without showing that the ontology changed. | Reviews miss the difference between a concrete pattern-to-claim contribution, an authority reference, and a package relation because each local sentence still sounds plausible. | Require one intended package-function word, name the definition, constraint, test, or other pattern contribution actually used, check the package relation explicitly, and treat stylistic noun-swapping as a semantic defect. |
| **Reader-fit leakage** | Pattern sections explain why the pattern was isolated, what landing form is safest, or why merge or freeze is premature. | Review accepts a package memo disguised as a user pattern. | Move current-version package-development reasoning to its companion or governing publication, integration, or release result. Keep the user's action and any warranted applicability boundary; cite the subject pattern only for an actual separate release, policy, assurance, gate, action-selection, or adjudication claim. |
| **Quality-carrier leakage** | Pattern prose explains corpus projection, retrieval evidence, publication parity, integration evidence, `PatternQualityStatus`, all-`4`/all-`5` posture, or development correspondence about its own current version as if it were user guidance. | Review accepts quality proof or package evidence disguised as pattern content. | Move it to the governing E.21 result, E.19 findings, README/ToC/E.11/I.2, or projection, publication, integration, or release result; keep only the user-facing move or boundary justified by that evidence. |
| **Apparatus overwrap** | A simple claim, relation, object, action, or placement is wrapped in role-word, carrier, locus, flow, state, status, text, package, or process language that adds no new kind or user-facing action. | Review accepts bureaucratic prose as precision, or replaces it with prettier prose that loses the FPF kind. | Use F.19's apparatus/content distinction, contribution test, and `KindPreservationCheck` comparison. Retain content-bearing apparatus under its defining pattern; otherwise remove the wrapper and preserve the same EntityOfConcern, head kind, relation or claim kind, admissible use, and established FPF term. |
| **Companion material retained by inertia** | A companion note, profile, check sheet, companion row, or review harness remains attached to a pattern family after the pattern body already carries the usable guidance, but the text does not say what real breakage returns if that companion material is absent. | Companion material becomes permanent local folklore, hidden authority, or reader cost without a corresponding use gain. | State the companion-use question, governing source, companion-only use, real breakage if absent, and retention, accepted-source-material-only, or removal condition; otherwise fold the useful example into the pattern or keep it only in the accepted source material. |
| **Pattern-quality result as project certificate** | An `E.19` pass is cited as proof that a project release, safety claim, compliance state, work result, publication, or gate has passed. | Collapses FPF pattern-quality review into project-world evidence or gate authority. | Keep `E.19` as pattern-quality review; open `A.10`, `B.3`, `A.20`, `A.21`, `A.15`, or the pattern that defines or constrains the project-side claim being made. |

### E.19:9 - Consequences

| Benefits                                                                         | Trade-offs and mitigations                                                                   |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Repeatable admission decisions** — reviewers share a common review language.     | More explicit editorial work; mitigated by a small baseline and risk-selected profiles.        |
| **Higher trust in normative content** — CC becomes the enforceable conformance check set. | Authors must align prose and CC carefully; mitigated by coherence checks.                  |
| **Controlled evolution** — reviewers detect and repair conceptual drift.              | Periodic workload; mitigated by prioritizing high-dependency and high-risk patterns first. |
| **Less hidden drift** — terminology and cross-context reuse become explicit.     | Some drafts will be delayed; mitigated by early profile selection when the relevant risk is already visible.        |

### E.19:10 - Rationale

Patterns are both **teaching publications** and **normative guidance publications**. A specification that grows without explicit quality gates can become a patchwork: locally good, globally inconsistent. A profile-based gate combines a short common baseline with depth selected for the live risk and pattern kind.

The baseline profile protects cross-pattern comparability and editorial sanity. Risk-selected profiles keep depth where it matters: norms, SoTA claims, cross-context reuse, terminology changes, staleness refresh, and reader fit. A pattern that is admissible in package terms but speaks to the wrong reader is still a review defect.

### E.19:11 - SoTA-Echoing — problem-first comparison of review approaches

**Working trade-off.** For one exact FPF pattern edition, detect semantic, ontological, practitioner-use, and source-currentness defects without making an ordinary review cost more than its likely harm warrants. **Design inference from the compared scopes:** combine narrowly targeted tools, human review of contextual defects, practitioner evidence for claimed transfer, and living-guidance methods for volatile claims. The source contributions and their limits are stated separately below.

**Evidence binding.** If a current SoTA Synthesis Pack answers this exact review or refresh trade-off, cite it and keep this section consistent with it. Otherwise, use the source contributions below for the named review question and decision; source identity alone does not establish the quality of that decision.

| Current approach and source | Coverage and effort | E.19 decision | Where this changes E.19 |
| --- | --- | --- | --- |
| **Proportionate independent assurance.** UK Government Analysis Function, [*The AQuA Book*](https://www.gov.uk/guidance/the-aqua-book) (2025). | Scales assurance by consequence, complexity, novelty, reuse, longevity, and uncertainty; separates the analyst, independent assurer, and approver. Its validation questions address fitness for use as well as specification compliance; the required effort varies with the selected assurance depth. | **Adopt and adapt.** Use those factors to select depth and retain an independent-findings form. Do not import government roles, approval stages, or mandatory assurance records into an ordinary FPF review. | The depth rule in §4; the two-form choice in §4.1; risk-selected profiles in §4.3; result and decision separation in §4.4. |
| **Lightweight change review with bounded automation.** Google's Engineering Practices, [Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html) and [Speed of Code Reviews](https://google.github.io/eng-practices/review/reviewer/speed.html); Sadowski et al. (2018), [Modern Code Review: A Case Study at Google](https://research.google/pubs/modern-code-review-a-case-study-at-google/), supplies bounded empirical evidence. | Current practitioner guidance favors self-contained reviewable changes and prompt feedback while preserving review quality. The study examines nine million reviewed code changes plus interviews and a survey. The evidence is code-specific; FPF's semantic replay remains a domain adaptation. | **Adapt, domain-bounded.** Keep one stable candidate, cheap mechanical checks, focused recheck, and a local-repair stop. Reject the code-review workflow and approval convention as FPF review semantics. | The local stop in §0.2; quick-pass automation in §4.2.1; stable-candidate and focused-recheck rules in §4.3.3. |
| **Practitioner-facing pattern validation.** Riehle, Harutyunyan, and Barcomb (2025), [Pattern Discovery and Validation Using Scientific Research Methods](https://doi.org/10.1007/978-3-662-70810-1_6), with the [authors' 2021 preprint](https://arxiv.org/abs/2107.06065) for the method; Iba (2021), [How to Write Patterns](https://hillside.net/plop/2021/plopourri/PLoP21_PLOPOURRI_Iba_Methodology4.pdf), supplies bounded writing and critique guidance. | Qualitative surveys, action research, and case studies provide methods for testing recurring applicability and transfer beyond the rule-of-three heuristic. Practitioner participation and observation add work beyond desk replay. | **Adopt selectively.** Escalate when universal or transfer claims remain uncertain or a missed failure has high consequence. Keep Iba for recognition, examples, consequences, and critique; do not treat critique culture alone as validation proof. | The recognition cases in §0.2 and their subject-specific transfer in §5; evidence escalation in §4.3.3; the breadth test in `CC-E19-7`. |
| **Living-guidance refresh.** Cheyne et al. (2023), [Methods for living guidelines: early guidance based on practical experience. Paper 1: Introduction](https://research-management.mq.edu.au/ws/portalfiles/portal/256300896/Publisher_version_open_access_.pdf). | Prioritises questions for living mode, varies surveillance frequency, updates the smallest recommendation affected by new evidence, and permits transition out of living mode. The approach improves currency but carries sustained cost and comes from clinical guidance. | **Adapt, domain-bounded.** Reopen the smallest affected FPF pattern or subset on a material trigger and stop continuous surveillance when its expected gain no longer justifies the effort. Keep the clinical governance and GRADE procedures outside the portable FPF method. | `PCP-REFRESH`; the bounded review object in §4.1; the reopen and stop rules. |
| **Narrow structural, ontology-tool, and retrieval checks.** [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html); Garijo, Corcho, and Poveda-Villalón (2021), [FOOPS!](https://ceur-ws.org/Vol-2980/paper321.pdf), with its [test catalogue](https://oeg-upm.github.io/fair_ontologies/doc/catalog.html); [RAGAS](https://aclweb.org/anthology/2024.eacl-demo.16.pdf) and [ARES](https://arxiv.org/abs/2311.09476) (2023–2024). | ISO 42010 supplies requirements for architecture-description structure and expression. FOOPS! tests selected FAIR-ontology properties. The retrieval evaluators distinguish context and answer relevance, faithfulness, and context adequacy. These are different properties and evidence relations; their outputs are not interchangeable pattern-quality scores. | **Retain only for the named property.** Use ISO 42010 as an architecture-description reference and FOOPS! only for an applicable machine-readable ontology. Select a retrieval evaluator against the required fixture properties; RAGAS/ARES illustrate that property split. A clean narrow check does not settle the remaining admission, usability, ontology, or source-currentness questions. | `PCP-BASE` structure checks; quick-pass automation in §4.2.1; `PCP-ENTRY-E4`; the no-project-certificate boundary. |

**Selected current front.** Ordinary E.19 use combines a lightweight stable-candidate review with cheap bounded automation, then scales review depth by likely harm, novelty, reuse breadth, and source volatility. It preserves independent findings as a real review form, tests breadth with practitioner evidence only when the claim warrants it, and refreshes the smallest triggered unit. The selected trade-off avoids running questions for absent risks while retaining human judgement of semantics, practical use, and current-source decisions. Practitioner studies and continued surveillance add effort only when the claimed breadth or currentness warrants it. Reopen this choice when another approach demonstrates equal or better detection of those four defect families at lower comparable effort.

When a receiving use requires a reusable E.19 result, it states the review claim for one exact FPF pattern edition or subset. Its EntityOfConcern, ClaimGraph, scope, applicable profiles, findings or aggregate cleared boundary, conclusion, and reopen condition state that pattern-quality claim. Any project-side reuse supplies its own governing relation, evidence or assurance, and decision under the relevant project rule. Review, repair, verification, result publication, admission or refresh decision, and project-side reuse remain separately recoverable. Reopen the affected result claim when a change to the reviewed text, accepted source, SoTA grounding, related pattern contribution, selected companion or projection function, profile trigger, review boundary, or claimed downstream use can change its conclusion or applicability.

### E.19:12 - Relations

* **Builds on:**

  * `E.8` (authoring conventions; canonical section order; SoTA-Echoing authoring requirements)
  * `F.19` (common whole-span precise-language repair, plausible-intended-reader guard test, coordination and list contribution, and local semantic reread after wording change)
  * `E.10` (compact lexical cues and exact FPF routing)
  * `E.10.ARCH` (deep-only ontological recovery architecture after `F.19` and `E.10` leave an unresolved FPF object or relation)
  * `E.9` (design rationale records for changes that affect semantics)
  * `E.9.DA` (content-first adequacy check for one exact DRR before pattern drafting or host amendment. An ordinary bounded check returns precise findings or repaired text; a full coordinate result and exact assessment identities are added only when explicitly requested or used by a named later reliance. An E.19 finding may expose an upstream DRR defect, but an E.19 pass, return, or absence is not E.9.DA evidence.)
  * `E.22` (improvement-oriented quality-evaluation question framing; distinguishes floor blocker review, exceptional-improvement review, Pareto trade-off inspection, open-question discovery, and absorption impact before an E.19 review result is formed.)
  * `E.23` (repeated quality-improvement method; an E.19 profile can supply questions and findings inside such a loop, but E.23 governs repeated absorption, object-under-improvement re-evaluation, method-family selection, and stop, continue, switch-method, open-new-frame, or hold decisions.)
  * `E.15` (change between exact pattern editions; actual-delta classification, affected-reach repair, predecessor preservation, and proportionate verification)
  * `A.6.5` (slot discipline; SlotKind/ValueKind/refMode invariants)
  * `A.6.P` (direct relation and participant recovery when the claim remains unresolved)

* **Coordinates with:**

  * `A.13` and `A.15.1` (exact actual-performer recovery and independent review, repair, or verification Work); `A.2`, `A.2.1`, and `F.6` only when local classification or precise assignment-bound attribution is expressly consumed; `A.6.1` separately defines check applications and bindings
  * `A.3.2` and `E.10.ROLE` (the full `U.MethodDescription` membership test and recovery of an ambiguous source *role* without forcing a system-role kind, assignment, participant, or representation position)
  * `C.2.1` (finding, focused-verification, aggregate review-result, and optional record epistemes)
  * `A.10` and `B.3` (evidence use/provenance and any assurance or reliance on an E.19 result)
  * `F.10` and `E.24.PUB` (status use/interpretation and publication occurrence/form/carrier; neither is review work or admission authority)
  * `F.8` (mint vs reuse decisions)
  * `F.18` (local-first naming when one durable reusable name is needed)
  * `F.9` (cross-context alignment discipline)
  * `F.15` (conceptual harness and regression framing)
  * `E.17` (MVPK publication and face discipline; an MVPK face, projected publication form, projection/construction, publication occurrence, rendering, and carrier remain distinct)
  * `E.17.0` (independent conformance required before the selected episteme has `U.View` membership; E.19 profile checks and no-new-claim/no-shadow-default compliance create no membership)
  * `E.11` (pattern-entry discoverability discipline, for `PCP-ENTRY` only as a review hook, not as a semantic prerequisite)
  * `E.13` (pragmatic utility and proxy-to-value alignment when a pattern-quality pass, score, coordinate value, checklist result, benchmark, projection signal, or release posture is being used as value evidence)
  * `E.21` (scoped pattern-quality characteristic space, coordinate evidence discipline, `PatternQualityStatus`, and stop condition; E.19 findings may become evidence only through the exact E.21 assessment application. Final coordinate values and `PatternQualityStatus` belong to a separate E.21 result episteme, not the E.19 profile or result.)
  * `A.6.7` (`MechSuiteDescription` suite-level semantics)
  * `E.20` (mechanism-introduction and governing-definition changes when its trigger applies)
  * `A.15.3` (`SlotFillingsPlanItem` P2W planned-baseline seam)
  * `G.11` (refresh/decay orchestration principles, where applicable)

### E.19:End

