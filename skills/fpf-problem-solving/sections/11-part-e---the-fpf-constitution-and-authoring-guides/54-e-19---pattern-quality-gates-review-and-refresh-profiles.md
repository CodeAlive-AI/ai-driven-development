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
| A system-pattern draft adds a deployment condition in prose but not in its Solution or Conformance Checklist, and treats matching cross-team labels as identity. | Apply `PCP-BASE` and `PCP-NORM`; add `PCP-BRIDGE` only if the text actually claims a relation across contexts. | Repair and recheck the requirement and identity claim, or return one actionable findings set that says exactly what must change. |
| An episteme or publication pattern still reads smoothly, but its sources are stale, its Relations use superseded names, or a carrier is treated as the claim it carries. | Apply `PCP-BASE` and `PCP-REFRESH`; add `PCP-TERM` for the claim, publication, or carrier confusion. | Update the affected Solution, source decision, and Relations, or return complete findings for the affected passages. |
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

A **Pattern Check Profile (PCP)** is a named bundle of check families. Profiles are **additive**: every review configuration includes the baseline profile and only the risk-driven profiles needed by the declared question. A PCP specifies questions and closure conditions; it is not a reviewer, `U.Method`, work occurrence, finding, result, or gate decision.

Choose review depth from the harm if a defect survives, the novelty and complexity of the claim, how widely the pattern will be reused, and how likely its sources or neighbors are to change. Pattern length, official status, and the number of available checks do not justify deeper review by themselves. Use cheap automated or template checks for properties they can actually test, then spend reviewer attention on semantic, ontological, practitioner-use, and current-source questions they cannot close.

**Terminology note (disambiguation).** PQG and PCP are editorial review constructs in the authoring plane (Part E). They are distinct from enactment and runtime gating constructs such as `OperationalGate(profile)`, `GateProfile`, and `GateDecision` (A.21), which govern Work transitions and gate decision policies elsewhere in FPF.

**Mint vs reuse.** This pattern mints **PQG**, **PCP**, and the profile IDs `PCP-BASE`, `PCP-MOD`, `PCP-PRAG`, `PCP-NORM`, `PCP-SOTA`, `PCP-BRIDGE`, `PCP-SUITE`, `PCP-P2W`, `PCP-TERM`, `PCP-DEONT`, `PCP-REFRESH`, and `PCP-ENTRY`. It reuses existing FPF terms (e.g., **Delta-Class**, **DRR**, **Bridge**, **CL**, **SoTA Synthesis Pack**) without changing their meanings.

For an ordinary bounded review, keep the reviewed edition or subset, question, selected profiles, checked loci, defects or repairs, and conclusion. When exact replay or a named later use needs a stronger account, also keep independently recoverable:

1. the exact reviewed FPF pattern edition or bounded subset and the declared admission/refresh question;
2. the review configuration: baseline and risk-selected PCP declarations, exact question scope, use, qualification window, and stop boundary;
3. the semantic review `U.Method`, when that identity matters; call an episteme its `U.MethodDescription` only after it passes A.3.2;
4. for each actual review, repair, or verification occurrence asserted as dated `U.Work`, use A.15.1 to identify its time, Method, containing System, and every performer; use F.6 to identify the exact assignment under which each performer acted. The attribution must be independently grounded rather than inferred from holder identity or timing. A compact account may omit only an assignment identifier unused by the receiving claim; all world-side facts remain recoverable;
5. each exact PCP check application and A.6.1 binding only when the receiving use must replay those bindings;
6. any distinct authoring/repair work, changed pattern edition, and focused verification work/application in inspect-repair-verify form;
7. actionable finding or blocker claims, focused-verification claims, and one C.2.1 aggregate E.19 review-result episteme when a durable conclusion is required;
8. any separate authority-bearing admission, refresh, return-for-repair, or waiver decision and its decision work;
9. witnesses, A.10 evidence-use or provenance relations, and any B.3 assurance or reliance result when those claims are made; and
10. any F.10 status use, publication occurrence or form, carrier, and currentness relation used by the receiving claim.

Any local system-role kind and its independently evaluated classification are optional separate claims; neither supplies assignment or performance. Route unresolved source *role* through `E.10.ROLE`, and name intended-reader or representation positions directly. When a later claim relies on a dated occurrence, apply item 4 and `CC-E19-0`.

The phrase **review run** is Plain shorthand for that configured set of objects and relations, not a new kind or actor. A profile, checklist, filled findings form, result episteme, or published record performs no review and grants no admission, assurance, authority, status use, or `U.View` membership.

#### E.19:4.1 - Define the reviewed pattern or subset

Name the reviewed pattern or landing subset, its edition or other stable version basis, the admission or refresh question, the selected profile questions, and the review boundary. That is enough for an ordinary bounded review. Add exact scope, window, and review-configuration identities only when a receiving result or named reliance needs them. Profile choice narrows review depth; it does not turn the selected questions into a progress record or perform the review.

When a reusable result or named reliance depends on how the review was enacted, apply the item 4 actual-Work account and `CC-E19-0` to each asserted review, repair, or verification occurrence. If a durable aggregate result is needed, constitute a C.2.1 result episteme whose EntityOfConcern is the reviewed pattern edition or subset and whose ClaimGraph states the review scope, applicable profile questions, actionable findings or aggregate cleared boundary, conclusion, non-use, and reopen condition. Witnesses, evidence use, the optional result publication, and any authority-bearing admission or refresh decision remain separate.

Choose inspect-repair-verify when the reviewer may edit and same-turn repair fits the declared use. Choose independent findings when the review needs separation from the author or an unchanged candidate. Independence changes who edits; it does not add a dossier or expand the selected questions.

**Choose one review form.** An `E.19` review has two forms:

1. **Inspect, repair, and verify.** One bounded review may include inspection, repair, and focused verification. A reviewer performs those actions; distinguish their performer, Method, affected object, or occurrence only when the positions differ or a named later use needs them. Apply item 4 and `CC-E19-0` if the account asserts dated Work. Apply every selected question, repair every in-scope defect, and reapply the affected checks. The changed edition and focused verification carry the substantive evidence; constitute an aggregate E.19 result episteme only when a receiving admission or refresh decision requires it. Make a separate findings record only for an unresolved blocker, a decision outside current authority, or transfer to another author.
2. **Independent findings.** A reviewer applies the selected questions without changing the reviewed pattern or subset. One C.2.1 findings-result episteme or semantic handoff records every actionable defect and blocker, with repair direction precise enough for the author to act without repeating the diagnosis. It is neither the reviewing action nor an admission decision.

A selected question that reveals no defect requires no durable pass entry. Independent review does not accumulate positive recitals, and inspect-repair-verify does not duplicate completed repairs in a parallel findings record. If another pattern defines a reusable value or decision required by the declared use—such as an `E.21` coordinate, a `DRR` decision, or a landing result—that value belongs to the result required by that pattern rather than to an `E.19` progress account. The local work method may provide transient attention markers; `E.19` governs the substantive questions and outcomes, not how those markers survive an agent's working context.

**Complete the selected scope.** Inspect every independently answerable question in the declared baseline and risk-selected scope. The first defect, blocker, or already-negative admission conclusion may prevent a positive verdict, but it does not complete the review and does not suppress findings that remain independently obtainable. Stop before the selected scope is complete only when a missing source, missing authority, unsafe boundary, or equivalent condition makes the remaining questions impossible to judge truthfully or safely. In that case, record the unexamined scope and why it cannot be judged; do not present the partial findings set as complete.

A nontrivial pattern-quality review SHOULD state its quality-evaluation purpose before depth is selected. Use `E.22` or an equivalent compact question frame to say whether this review is a `floorEvaluation`, `exceptionalImprovementEvaluation`, `paretoTradeoffEvaluation`, `openQuestionDiscoveryEvaluation`, `absorptionEvaluation`, or a declared combination. If the purpose is absent, `E.19` treats the review as an admission-refresh blocker read, not as a request to raise every evaluated coordinate toward exceptional expression. When coordinate values, `PatternQualityStatus`, or all-`4`/all-`5` claims are needed for one pattern version, the review opens or consumes an `E.21` result instead of assigning those values inside `E.19`.

When the review opens or consumes `E.21`, `E.19` treats `E.21` as a hard pattern-quality evaluation, not as a selectable profile. The review must not accept an `E.21` claim that omits required coordinates, omits `ShortRationale`, omits `PrecisionRestorationProfile`, uses inactive/triggered-coordinate language, narrows the requested use to make the result pass, or replaces coordinate values with blocker triage. In inspect-repair-verify, repair or re-evaluate the affected result where that work is in scope; in independent findings, record the exact defect. Baseline triage can answer only the `E.19` review boundary when no `E.21` quality value, all-`4`/all-`5` claim, landing-quality claim, or pattern-improvement movement claim is being made.

If the aim is repeated improvement against an object-under-improvement evaluation, use `E.23` for the repeated method. An E.19 review configuration may supply PCP questions and its result episteme may supply findings inside that loop, but a profile is not the loop method and an E.19 result is not an ordinal quality value. Only a separate E.21 assessment application and result episteme can state the E.21 coordinate values for the changed pattern version.

`E.19` reviewer and reviewed-pattern wording is FPF pattern-quality gate wording. It governs FPF admission, refresh, return-for-repair, blocker, and review-profile claims, not `E.21` coordinate assignment and not project-side publication interpretation, explanation interpretation, comparative review-unit use, or participation in a named project-side review relation. When those project-side relations are used, use the publication or project-side pattern that names the object being interpreted or reviewed.

**Project-side reuse boundary.** Use this boundary when an E.19 review-result episteme is cited as project certification, project evidence, safety-assurance material, gate input, release justification, compliance-assurance material, assurance material, work authority, or publication truth. First identify the exact FPF pattern-quality claim it states: admission, refresh, repair return, or selected pattern-quality boundary. Any project-side reuse then opens the concrete relation that governs that use: `A.10` for evidence/currentness, `B.3` for assurance, `F.10` for status use/interpretation, `A.20` for a current local CV status when applicable, `A.21` for gate decision, `A.15` for work, or the relevant project-side pattern. The E.19 result may be evidence about FPF pattern quality; it is not certification of the project world. Plain wording in the reviewed text remains ordinary unless it changes admissible use, evidence, gate, assurance, work, decision, status use, or FPF pattern application.

**Common wrong first interpretation.** A favorable E.19 review-result claim means the project, release, publication, safety claim, or compliance claim is certified. First honest entry: that result concerns only the exact FPF pattern edition and review scope; project-side reuse names its own governing relation, evidence/assurance source, and decision authority.

**Misuse guard.** A pattern-quality caution, return-for-repair result, or selected pattern-quality boundary result cannot be reused as project refusal or project approval unless a project-side governing relation states admissible and non-admissible use for that relation.

Formal or template defects (e.g. non-compliance with E.8 structure or not conforming to RFC deontic terminology) have lower review priority than semantic or ontological defects or non-SoTA Solutions. In inspect-repair-verify, repair them within the declared boundary; in independent findings, record them with concrete repair direction.

E.g. if the header block is missing or incomplete, **continue with ontology and semantic review first**. Treat missing header fields as one mechanical defect, not as a reason to stop (PCP-BASE #7).

When a proposed or accepted change needs a best-known **Delta-Class (Δ-0…Δ-3)** and initial **impact radius**, place them in the governing change, decision, or landing result using existing definitions where available (e.g., the LEX-AUTH protocol). `E.19` repairs or reports an omission that matters to the selected gate; it does not copy a successful change account into a second review record.

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
   The pattern body stays addressed to the intended FPF user rather than to FPF developers, package architects, reviewers, evaluators, or release/projection carriers. FPF-governed sections explain admissible use, costs, boundaries, the concrete definitions, constraints, tests, or other contributions used from FPF patterns named by value, project-side FPF kinds and references named by value, and related relations named by value in user terms. Architecture placement, freeze or merge state, package-boundary rationale, reference boilerplate, quality or projection evidence, corpus-entry evidence, `PatternQualityStatus`, monolith-parity evidence, landing evidence, and broader package-development rationale stay in `DRR`, architecture documents, review handoff, `E.21` result, `E.19` findings, README, ToC, `E.11`, `I.2`, cards, retrieval or projection carriers, release or landing evidence carriers, companions, or ordinary references unless they change the working reader's first admissible move.
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
   When a Solution says how work should be done, first distinguish content that defines, constrains, tests, or guides a Method from an assertion that one dated Work occurrence or world-side change actually obtains. Method guidance alone does not trigger a fictive performer or Work. If an account asserts dated `U.Work`, verify the §4 actual-Work account; if it asserts a world-side change, identify the change relation, the pattern that defines it, and the things it relates. Keep the intended-reader position, any qualifying A.3.2 method-description episteme, actual performer, Work, and problem-facing result separate. Return a finding when an episteme, checklist, plan, prose, or intended-reader or representation position is made to perform Work, or when Work and result are collapsed.

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
* **Sentence-level precision matters on FPF-governed prose.** Reviewers SHOULD inspect FPF-governed sentences for generic heads, claim-bearing qualifiers, overloaded trigger words, bare relation shorthand, and hidden process/API metaphors. The default repair order is: restore head kind, then qualifier claim kind or admissible-use boundary, then comparison criterion or escalation condition homogeneity, and only then judge whether a later Plain or coarsened rendering is admissible. This is an MG-DA cold-reader check: after repair, a reader without the `DRR`, campaign notes, or reviewer memory must be able to state the object, kind, relation or claim kind, admissible use, and next applicable pattern or rule. Broad replacements such as `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, or unqualified `specialization` remain defects unless the specific object, relation position, and applicable defining, constraining, or checking content are named; specialization wording must say what specializes what, by which specialization relation, and which inherited or changed slots or uses matter.
* **Precision-restoration distribution must be preserved.** `E.10` recognizes the wording problem, `E.10.ARCH` supplies the shared recovery architecture, and the selected realization pattern supplies the concrete rule or guidance for its subject. Affected patterns keep only thin pointers instead of copying trigger lists or recovery algorithms. Treat pattern content as defining, constraining, testing, or guiding by default. Claim a Method or MethodDescription only after A.3.1 and A.3.2 admit it; a pattern identifier or body establishes no performer, assignment, Work, result, responsibility, or authority.
* **EntityOfConcern and precision-restoration questions travel with the same triage.** Before acceptance ask:
  1. What is this pattern's own `EntityOfConcern`, first useful move, practical delta, and bounded non-use?
  2. Does its own action guidance come before auxiliary wording, publication, architecture-placement, package, or quality apparatus?
  3. After wording or reference migration, does the claim still reach the same referent through the intended slot or reference position and alignment path? Record any deliberate retargeting instead of hiding it in a renamed head.
  4. Do description and publication-use guards still admit only the intended uses, rather than widening use because the wording is now type-correct?
  5. When phrase apparatus, semio bias, architecture placement, package rationale, or quality apparatus changed, did the repair preserve the function that was actually needed and remove only the displaced apparatus?
  6. Which pattern supplies each outside definition, constraint, or test, and is formal identity actually needed for truth, a live distinction, or named reliance? Apply F.19 to phrase-level trouble before word, head, or use restoration.
  7. Has every claim-bearing *role* use passed E.10.ROLE, and have Method, Work, evidence, assurance, gate, status, and decision claims remained under their own predicates?
  8. Has every affected current consumer received a semantic, mechanical, compatibility, or not-triggered disposition?

When E.21 is active, its `PrecisionRestorationProfile` carries the quality result; E.19 does not duplicate it.
* **Design-time and run-time both count.** The same precision discipline applies to FPF pattern prose and to any reviewed publication text, worked slice, or performed-work exemplar when that text is being assessed for admissibility, guidance, reuse, gating, release, policy, assurance, or action-selection use.
* **Report ordering (impact-first).** In run outputs and remediation direction, prioritize findings on ontology, semantic, modularity and SoTA-related FPF-governed sections first; group low-signal formatting/typos into one compact tail finding unless they change meaning.

#### E.19:4.3 - Add risk-driven profiles

**PCP‑PRAG (Pragmatic utility & adoption)** — Trigger: the pattern is Normative and claims practice guidance.
Checks include: a visible first-reading recognition text early enough for a cold working reader; a recognisable first-minute working situation; one short `Use this when` or equivalent entry; a plain statement of what goes wrong if the pattern is missed; a plain statement of what the pattern buys in practice; the first admissible action-guiding move the user should take; a visible ordinary `not this pattern when` boundary; a minimally viable example; non-decorative Consequences/Anti-Patterns; at least one worked slice when the pattern is easy to misuse; a visible assurance text carrying declaration, guidance/check, modeling, and review/check scope; reader-fit consistency so that the assurance text does not silently widen or universalize the recognition-text claim; explicit practical payoff in user-facing prose; a short user-facing statement of the primary `EntityOfConcern`, relation record, or claim record and any minimal modeling lens when typed declaration material has FPF-governed use; nearby pairwise plain glosses for FPF-governed technical terms that appear before the heavier harness; a short working-reader implication for any `SoTA-Echoing` rows that carry explanatory work plus visible linkage to the worked cases or boundary slices they discipline; explicit primary working reader, concern, and viewpoint fields when several working-reader situations are being served; an explicit `So what?` adoption test; and, when the pattern claims universal or transdisciplinary reach, at least three heterogeneous recognition-text situations with `F.16` preferred as the compact example-matrix template.
If an `E.10` trigger scan selects epistemic precision restoration during admission or refresh, `PCP-PRAG` treats type-correct-but-inert wording as a usability defect under `E.2` `P-2` and `E.12`: the reader must still recover why the distinction matters, what use remains, and which pattern or rule supplies the needed definition, constraint, or test. Any Plain recognition line maps back to the recovered Tech reading when both registers are used. Keep ordinary wording ordinary when it asserts none of those technical objects. Add an exact assertion, predicate, `ClaimGraph`, or displayed identity only when it changes truth, action, stop, or named reliance. If that assertion is dated Work, apply `CC-E19-0`.

For a broad cleanup across several patterns, or any cleanup that touches FPF-governed Problem frames, Problem sections, first-use recognition text, archetypal grounding, examples, or worked slices, check whether the didactic function was harmed. In inspect-repair-verify, restore the working situation, first useful move, and the definition, constraint, test, or other pattern contribution needed by the claim; in independent findings, record the exact harm and repair direction. A positive `improved` or `preserved` account is required only when another evaluation makes that value one of its substantive results, and it belongs in that evaluation.

**PCP‑MOD (Modularity and abstraction-boundary discipline)** — Trigger: the reviewed pattern or subset shows scope creep or abstraction-boundary mixing (e.g., one pattern bundles universal core rules with frame-specific content and discipline-specific method semantics; or it mixes EntityOfConcern, Description, and Specification positions in one object).

Checks include:

* an explicit **core vs extensions** cut (universal invariants are factored into one stable “core”, and extensions reference it rather than re-stating or mutating it),
* no conflation of **specialization vs dependency**: use `⊑/⊑⁺` for refinement/extension and `Uses` for pipelines; do not mix their semantics,
* no conflation of package-form, concrete pattern-to-claim contribution, and package-relation functions: **Pack vs Kit vs Suite vs Family vs Bundle vs Cluster vs Profile vs Overlay vs Record vs Umbrella** are not interchanged, and the review states carrier status, the definition, constraint, test, or other pattern contribution actually used, and the package relation explicitly instead of leaving them implicit or varying them for style,
* description-lane descriptions and their publications do not grow mechanism semantics; for an MVPK face or projected publication form, no-new-claim checks that it introduces no claim beyond the selected episteme and no-shadow-default checks that it introduces no undeclared default. Keep the selected episteme, optional projection/construction, face, publication form, publication occurrence, rendering, and carrier distinct. The selected episteme has `U.View` membership only when exact E.17.0 conformance independently obtains; face status, projection, profile selection, and compliance with these two checks establish no membership or truth,
* slot-discipline hygiene for any ordered specialization set: SlotKind invariance is preserved and inherited operations do not gain new mandatory inputs (A.6.5 / A.6.1 specialization discipline).

**PCP‑REFRESH (Staleness & compatibility refresh)** — Trigger: staleness signals are present (e.g., outdated SoTA rows, renamed/superseded Relations entries, terminology drift, or an explicit refresh window in LAT/DRR).
Checks include:

* refresh‑sensitive claims are identified (time‑bounded or ecosystem‑bounded) and either (a) updated with post‑2015 evidence **and** matching Solution changes, or (b) explicitly scope‑limited and labeled as historical lineage,
* select living refresh only for a high-priority claim or pattern subset likely to change when new evidence or a changed neighbor appears. Monitor and reopen the smallest affected unit at a named trigger; return it to ordinary periodic review when continued surveillance no longer buys enough currentness for its cost,
* Relations are updated to current pattern IDs; deprecations/renames are handled via explicit continuity notes (no silent relabeling),
* when one new or substantially revised pattern subset is being prepared for send or landing, inspect the related patterns, the concrete constraints or tests they supply, companion patterns, Relations entries, and monolith-backed pattern sections that may require aligned edits. Repair an in-scope mismatch or return it as a finding. Successful alignment remains visible in the changed sources and the governing landing or release result, not in an E.19 pass recital,
* any long-lived companion, profile, check sheet, pattern-local companion row, review harness, or analogous selected non-pattern FPF kind-reference pair kept with the reviewed pattern or subset states its use question, the concrete pattern contribution or selected non-pattern FPF kind-reference pair it serves, admissible companion-only use, one real breakage if absent, and demotion or deletion condition when no such breakage exists.
* when the refresh causes Δ‑2/Δ‑3, verify that the governing change or decision result carries its Delta‑Class, impact radius, `DRR` pointer, and any refresh and Bridge obligations required by E.15/F.15/F.9; repair or report an omission rather than copying a successful account into E.19,

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
* each SoTA row changes at least one FPF-governed outcome for the pattern: what the user may do, what the user must not over-read, which FPF pattern application must be named, or which claim cannot be raised to release, policy, assurance, gate, action-selection, or adjudication use,
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
Checks include:

* `SlotFillingsPlanItem` remains declaration-local `PlanItem` content inside one exact `U.WorkPlan` ClaimGraph; it is not a U-kind, execution log, mechanism, independent record, relation occurrence, or second slot ontology,
* every relied-on row names the intended-performance designator, exact declaration edition, declaration-local member designator and family, the exact ClaimGraph defining the member's reusable meaning and corresponding later actual-use predicate, the pattern locus that supplies that definition, the positive planned value or designation, the target declaration's effective designation rule and semantic cardinality, and the exact planning conditions; A.15.2/A.15.3 define the intended-use claim independently of the target declaration,
* declaration families remain distinct: relation-participant rows target only `SlotSpec`s in exact `RelationSignature` editions, operation rows target exact A.6.1 `ArgumentDeclaration`s or `ResultDeclaration`s, and any other row targets an explicitly governed declaration member with a corresponding actual-use predicate; a method description, kit or suite description, schema field, card, checklist, interface form, database field, or generic slot-bearing description is not a target merely because it displays a field,
* target-declared cardinality remains operative: for a single-valued target, exact conditions and an exact resolution rule make at most one planned value effective for any one intended use; multivalued set, order, repetition, or multiplicity semantics are never inferred from row count or layout,
* a row is positive intended-use content; omission is open-world, while prohibition, exclusion, required absence, and completeness remain separately governed plan claims rather than empty fillers or negated references,
* planned filling stays plan content: a planned value, compatible ValueKind, matching token, WorkPlan, or PlanItem establishes no dated work, obtaining relation participant, operation application, argument or result binding, returned value, change, production, delivery, acceptance, or outcome,
* when later actual use is compared with the plan, the direct relation predicate or exact A.6.1 application-binding predicate must obtain independently; a missing-filler or negative comparison requires an applicable closure or negative criterion and exact case facts; the comparison preserves the cited WorkPlan edition and expresses substitution or variance as a neighboring governed claim rather than backfilling the plan,
* declaration-edition pins, planned-value-edition pins, concrete reference kinds, time, location, capability, readiness, gate, evidence, source-currentness, bridge, publication, baseline, or comparison conditions appear only when the named receiving use relies on them; every policy or reference used by that claim keeps its concrete kind, edition, applicability, and effective reference scheme, plus its issuing authority, source, or defining rule when that distinction matters, and the profile introduces no unconditional crossing, time-selector, scope, audit-pin, or context bundle,
* a card, table, view, index, or generated summary is read-only publication of selected WorkPlan claim content: it does not add planned fillings, defaults, declaration meanings, cardinality, conditions, baseline semantics, or a second row authority, and
* when no reusable declaration member is needed, lower to ordinary A.15.2 plan content; when the declaration member, reusable meaning, corresponding later actual-use predicate, or defining or constraining pattern content cannot be recovered, return the exact missing-source blocker rather than manufacturing a SlotSpec, description wrapper, generic field declaration, or actual-use relation.
**PCP-TERM (Terminology & naming protocol)** — Trigger: the pattern introduces new terms, new U-kind pressure, new governed value names, new “unified names”, redefines existing labels, leans on FPF-governed phrases whose head kind or qualifier claim kind or admissible-use boundary is not yet restored, or uses FPF-governed trigger wording as if the word itself carried the needed kind.
Checks include:

* the “mint vs reuse” decision is explicit when a term is introduced or changed,
* naming follows the local-first naming protocol and avoids scope smuggling (role-word meanings, metrics, or stages baked into labels; overloaded words used as terms with a local sense). Remediation **SHOULD** use F.18,
* when PCP-TERM is selected, `F.18` winner selection and `A.6.P` follow-through form one chain: inspect the candidate heads or phrases, kind conflicts, lexical conflicts, selected wording, and survival of the repaired phrase; repair a broken chain or return its exact defect rather than recording the successful chain as a pass account,
* classify FPF-governed trigger wording before acceptance by semantic area, not by a local forbidden-word list. Typical classes include admissibility/deontic terms, evidence and review-check terms, action-invitation terms, characteristic/scale and stratification source labels, state-family terms, lifecycle/process terms, pattern-application wording, publication-form terms, and local equivalents. The accepted sentence itself or its governing declaration must make the relevant object, value frame, relation, work, authority reference, pattern application, publication kind, companion function, or conformance claim recoverable; repair or report any case where it does not,
* generic heads and claim-bearing qualifiers are not accepted at face value in FPF-governed prose: restore the head kind first, and do not count a narrowing qualifier as that restoration; only then restore the qualifier claim kind or admissible-use boundary,
* if a sentence compares, escalates, downgrades, or otherwise puts pressure on a phrase after that restoration, check that the comparison criterion is ontologically homogeneous,
* when repaired wording still carries an architectural claim kind or admissible-use boundary, verify that the resulting primary `EntityOfConcern`, first useful move, outside work, and any `E.10.ROLE` disposition or package-form decision remain recoverable in the repaired text or the decision that set the boundary; repair or report a mismatch, and
* source-side old wording and continuity rules are respected.
**PCP‑DEONT (Deontic clause hygiene: RFC keywords)** — Trigger: the pattern conflates admissibility/validity constraints with deontic obligations (e.g., uses RFC keywords where a non-deontic Invariant: predicate is required).
Checks include:
* Deontic requirements are expressed with RFC-style keywords (see H-8);
* obligations are not smuggled into prose as informal imperatives. Admissibility/validity constraints are stated non‑deontically as `Invariant:` / `Well‑formedness constraint:` predicates and referenced from the Conformance Checklist when enforceable.
* **Subject discipline for RFC keywords.** If a sentence uses RFC keywords, its grammatical subject **MUST** be an agent or a published record or model whose required content is being constrained. RFC keywords **MUST NOT** modify modeled-world entities such as Earth, an assignment, a system-role kind, or a holon; express those requirements as `Invariant:` or `Well-formedness constraint:` predicates and reference them from CC items when needed.

**PCP-ENTRY (Pattern-entry discoverability and entry-orientation changes)** —
Trigger: one change substantively affects how one reader recognizes, selects,
rejects, or reclassifies one applicable direct pattern body, applicable projection function,
first-entry pattern-comparison set, Problem-frame recognition signature,
expanded entry-disambiguation case, or entry lexical-query cue.

Trigger classification:

`PCP-ENTRY` is an explicit profile identifier under the existing Pattern Check Profile family. It reuses the `PCP` profile kind; it is an editorial review profile, not a runtime gate, not `GateProfile`, not a workflow state, and not a new route registry.
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
  The author leaves one compact pattern-local note, runs the core check, and adds at
  most one selected risk check if needed.

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

`PCP-ENTRY` stays one narrow additive review profile, not one super-profile
that absorbs `PCP-PRAG`, `PCP-MOD`, `PCP-TERM`, `PCP-NORM`, and every other
review/check scope.
It composes with `PCP-PRAG`, `PCP-TERM`, and `PCP-MOD`; it does not replace
them.
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
* one wrong-pattern check when known misclassification is present;
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

One compact risk-triggered gate is enough here:

| Change shape | Default check | Acceptance signal |
| --- | --- | --- |
| typo, grammar, formatting, meaning-preserving compression | no evidence run beyond ordinary review | current entry-recognition function, governing-entry or applicable-projection-function boundary, and companion or projection function remains unchanged |
| one Problem-frame recognition-signature wording change or one wrong-pattern clarification | reviewer-only entry check | no workflow implication and no governing-entry or applicable-projection-function drift |
| one README scenario, ToC query cue, `E.11` entry-distribution locus, `I.2` expanded entry-disambiguation case, or changed candidate-pattern set | pattern-selection or wrong-pattern check | intended applicable direct pattern body or one admissible candidate-pattern set is recoverable without one false mandatory sequence |
| one lexical-hook change | lexical query check | subject-domain phrasing recovers the governing entry or applicable projection function without uncontrolled alias drift |
| two or more projection or companion functions change together | companion-or-projection function parity check | one governing entry or applicable projection function stays unique and the changed companion or projection functions agree on first-use entry-recognition function, wrong-pattern boundary, projection-only status, and no claim beyond the Core pattern body's admitted use; they need not share identical wording or examples |
| one high-risk public-facing or substantively changed first-entry companion or projection function changes | cold-reader recognition task | one reader can recover the intended applicable direct pattern body or admissible candidate-pattern set under the named first honest entry-recognition function |
| one retrieval-facing companion or projection function changes or one observed misretrieval is repaired | retrieval or `RAG` fixture | retrieval returns the governing entry or intended projection cue before one stale echo, and answer-to-governing-entry faithfulness remains intact |

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

The following evidence modes are selected high-risk tools, not one suite to
exhaust on ordinary authoring passes.
Selected evidence modes may include:

1. **PCP-ENTRY-E1 — cold-reader recognition or pattern-selection task**
   Given one real case signal, can one reader recover the intended applicable
   direct pattern body or one admissible candidate-pattern set?
   One tiny micro-task is enough:

   ```text
   Given this entry-recognition phrase, name:
   1. the first candidate pattern,
   2. one tempting wrong pattern,
   3. the admissible entry stop,
   4. the governing entry or applicable projection function.
   ```

2. **PCP-ENTRY-E2 — wrong-pattern and wrong-entry trap**
   Does the companion or projection function actively prevent the most tempting wrong pattern or wrong
   family?

3. **PCP-ENTRY-E3 — lexical query check**
   Does subject-domain phrasing retrieve the governing entry or applicable
   projection function without uncontrolled aliases?

4. **PCP-ENTRY-E4 — retrieval or `RAG` fixture**
   Does retrieval recover the governing entry or applicable projection function under
   exact-ID or keyword phrasing, under semantic paraphrase phrasing, and under
   projection-vs-governing-entry ambiguity, while keeping retrieved companion material,
   source faithfulness, stale echoes, and post-rationalized citation-like material distinct
   from the applicable direct pattern body?

5. **PCP-ENTRY-E5 — companion-or-projection function parity check**
   Do the companion or projection functions, plus any explicit absence note, preserve
   the same first-use entry-recognition function, governing entry or applicable projection function,
   wrong-pattern boundary, projection-only status, and no-claim-beyond-Core
   claim without requiring identical wording, rows, or examples?

6. **PCP-ENTRY-E6 — observed failure or query-log capture**
   Does one observed misretrieval, wrong-pattern loop, or repeated query miss
   still survive after the repair, or has the failure actually been
   removed?

#### E.19:4.3.1 - Tiny golden case bank for regression and worked examples

One tiny golden case bank is enough here. It is a review-regression echo, not the canonical entry inventory: rows 1-4 mirror README scenarios, `E.11` entry-distribution loci, and `I.2` expanded entry-disambiguation cases that already carry entry companion or projection functions, while rows 5-6 add review-specific search and retrieval stress cases. `E.11` and `I.2` remain the governing entry companions; this bank only tests whether a change preserved them.
It is not one benchmark suite and does not require universal empirical review for ordinary wording or companion-or-projection function edits.
A run may cite one relevant golden case or state that none is relevant. It does
not need to execute the whole bank.
It keeps a stable set of recurring entry-recognition functions recoverable across hardening
passes:

| Case | case_signal | expected_first_entry_pattern_comparison_set | candidate_patterns | tempting_wrong_pattern_or_wrong_relation | admissible_entry_stop | companion_or_projection_functions_that_help | projections_that_do_not_define_semantics |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | “we need a shortlist, not one winner” | pattern-comparison set for comparison, pool treatment, and selected-set result declaration | `A.19.CN`, `A.17-A.19`, `C.18`, `C.19`, `G.0`, and `G.5` when selected-set result declaration is claimed | treating `C.11` as one one-off choice when the real entry-recognition function is selected-set result declaration or candidate-set stabilization | admissible candidate-pattern set stabilised or selected-set result declaration opened | README scenario or `E.11` entry-distribution cue, one pattern `Problem frame`, one expanded entry-disambiguation case if compact cues still fail | one README blurb, one thin echo, one lexical-query row alone |
| 2 | “we have a vague cue, not yet a claim” | pre-articulation cue pattern-comparison set | `C.2.LS`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0` | forcing the cue into one endpoint-claim, quality, or assurance pattern too early | `entry-recognition-reclassified` or cue preserved for the admissible next entry-recognition function | README scenario or `E.11` entry-distribution cue, one pattern `Problem frame`, one case-linked `I.2` expanded entry-disambiguation case when needed | one coarse public entry projection alone |
| 3 | “this is the same EntityOfConcern re-expressed for another audience” | same-EntityOfConcern rewrite pattern-comparison set | `A.6.3.CR`, `A.6.3.RT`, `E.17.EFP`, `E.17.ID.CR` | minting one second `U.Episteme` for the same claim or one second competing explanatory lane instead of one same-EntityOfConcern rewrite | `wrong-pattern-rejected` or same-EntityOfConcern rewrite opened | one expanded entry-disambiguation case, one pattern `Problem frame`, governing-entry pointer | one parallel explanatory blurb treated as one second pattern body |
| 4 | “the API says X” | boundary-claim unpacking pattern-comparison set | `A.6`, `A.6.B`, `A.6.C`, `A.6.P`, `C.16.Q`, `A.6.A`, `E.17` | treating one boundary phrase as one agent duty, promise, quality verdict, or generic agreement paragraph without atomic claim assignment or quality-term repair with recovered characteristic and scale | `boundary-claim-pattern-opened`, `quality-term-repair-exited`, or atomic claim set opened | one boundary-focused `E.11` entry-distribution cue, one pattern `Problem frame`, one expanded entry-disambiguation case where interface/access/confused-quality wording is common | one query cue or public entry projection treated as the governing entry |
| 5 | “I found a pattern by search, but I am not sure it is the right one” | one pattern-local recognition-signature case under the selected pattern-comparison set | one candidate applicable direct pattern body plus one case-near related pattern when needed | one lexical near-match or same-family pattern without governing-entry fit | `non-use-confirmed` or `pattern-selected` | one pattern `Problem frame`, one `E.11` entry-distribution cue, one lexical-query hook | one search-query row alone |
| 6 | “the LLM retrieved a helpful-looking paragraph but not the pattern” | one retrieval-facing first-entry pattern-comparison case | one applicable direct pattern body plus one applicable projection function | one stale thin echo or one projection-only companion function answered as if it were the governing entry | `governing-entry-opened` or `expanded-entry-disambiguation-case-needed` | one governing-entry reference, one projection-only status marker, one retrieval-facing pointer to the applicable direct pattern body | one thin echo chunk without governing-entry reference or projection-only cue |

These six cases are enough to keep:

* entry-recognition consistency;
* wrong-pattern or wrong-entry rejection;
* admissible entry-stop honesty;
* lexical-query discipline;
* thin-echo retrieval hygiene;
* and governing-entry and projection separation recoverable as the amendment
  lands.

When one empirical or retrieval evidence run is actually selected, the run
makes recoverable only the fields needed by that run, such as:

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
One minimal retrieval fixture checks exact ID or keyword retrieval, semantic
paraphrase retrieval, projection-vs-governing-entry disambiguation,
and, when thin echoes are used, thin-echo governing-entry reference presence.
Ordinary local guidance stays prose-only rather than minting one stable
governing-entry reference by default.

#### E.19:4.3.2 - Common hardening questions are triggered by review need

Open a common hardening question when the concern has FPF-governed use, is disputed, or is explicitly invoked by the reviewed pattern or subset. Inspect the relevant source and the reviewed loci. In inspect-repair-verify, repair any defect and verify the affected use; in independent findings, record the defect and repair direction. When the question reveals no defect, make no durable absence or pass recital.

Use these questions only for the selected entry-recognition function:

1. **Usability and working-reader fit.** Open this when first-reading recognition text, assurance text, first-minute working-reader usability, practical payoff, worked slices, primary-reader fit, or `E.8` / `E.12` / `E.13` / `E.14` / `E.17.*` / `F.16` checks can change the admission or refresh result. If a separate evaluation assigns a value, use that evaluation's result rather than copying it into E.19 findings.
2. **Scenario, anti-case, and utility-fit source set.** Open this when a scenario pack, anti-case corpus, pilot bank, utility tree, fitness catalog, or analogous source is actually relevant or substantively disputed. Record only a missing, misused, or failing source/case as an E.19 finding.
3. **Packaging, concrete pattern contribution, package relation, and shipping fit.** Open this before a send-facing, landing-facing, monolith-facing, pattern-contribution, or package-relation claim. The changed sources and governing landing or release result carry successful alignment; E.19 repairs or reports a mismatch.
4. **Domain-tightened profile depth.** Open this when a domain-specific note actually tightens a selected profile. Apply its questions; do not add a second account of positive results.
5. **Accepted-decision or accepted-source-material carry-through.** Open this when the reviewed pattern, subset, or current change is claimed to implement an accepted `DRR`, returned-finding set, intake, architecture source material, or other accepted source material named by value. Inspect each independently applicable decision against the reviewed loci and the concrete pattern, claim, companion, result, or accepted source that carries it; require exact predicate or defining `ClaimGraph` identity only when that decision or the named reliance needs it. Repair or report partial, missing, wrongly rejected, wrongly routed, or wrongly classified carry-through. The accepted source remains the decision source; E.19 does not duplicate decisions that are expressed sufficiently, inherited unchanged, correctly absent, or outside the reviewed subset. Do not rename an `E.17.ID.CR` comparative review unit, `PublicationUnit`, publication form or face, source-pinned interpretation case, source material, or project-side review relation as an `E.19` reviewed pattern or subset.

For `PCP-ENTRY`, the ordinary compact pattern-local change note remains enough when the governed discoverability decision requires one; no separate E.19 account is created merely because the profile was checked.

#### E.19:4.3.3 - Pattern-Edition Use-Value Replay

Use this replay when an exact candidate pattern edition changes materially under `E.8:4.1.2`. Run it once on the stable candidate before acceptance or landing, not after each edit. Start with the bounded E.8 loop over the earlier edition and proposed prose, then open only each affected earlier-edition or candidate-only use whose result can differ, pinned to its exact basis and changed locus. Treat a change as mechanical only when the smallest relevant comparison shows that every materiality value named in `E.8:4.1.2` is preserved. A genuinely bounded local semantic edit opens only its affected use probe and changed wording group; physical rewrite size is not evidence.

When the candidate keeps, merges, removes, profiles, reuses, externally supplies, or omits a narrower contribution, apply the same-situation decision in `E.8:4.1.3`. If reuse or a gap answers the working question, verify which return is actually present: an available maintained result of its own kind and supplying product, a maintained MethodDescription reference, direct-source evidence, or a named unavailable result. For an external result, verify the receiving use, discovery route, material currentness or availability, and the statement that it remains outside the receiving framework; otherwise the package still has a gap or omission. When the resulting stable set materially changes a promised problem family, require a current `E.4.DPF.DA` `D12DomainProblemFamilyCoverageAdequacy` result for the resulting exact DPF or LPF edition. Reuse a matching current package result when its exact basis is unchanged; E.19 asks for neither a duplicate package evaluation nor evidence that a revisit occurred.

Judge each affected use probe separately when its result can differ by exact earlier-edition or candidate-only basis, working use or relying work, expected first useful result, boundary, necessity, or evidence mode. One review may contain probes from both bases. A grouped verdict such as `uses preserved or added` or `usability preserved` cannot substitute for those judgements. E.19 does not prescribe a per-probe progress store: inspect-repair-verify repairs and verifies failed probes, while independent findings records only regressions, insufficiencies, invalid transfers, unsupported decisions, and blockers. When `E.8`, `E.21`, or another governing evaluation requires reusable dispositions or values, keep them in that evaluation's result rather than copying them into E.19 findings.

**Changed-wording check inside each affected earlier-edition probe.** Keep the selected use probe as the outer unit. When a candidate materially rewrites earlier-edition wording in a normative sentence or inseparable sentence group that carries the governed extension, action discriminator, first useful result, stop, or neighboring-pattern exit, give that wording group its applicable differential disposition below before closing the outer probe. Keep sentences together only when they serve one reader task and must receive one disposition; split them when their extension, action, result, or route can differ.

For each changed wording group:

1. pin the earlier-edition and candidate wording and the exact use it serves;
2. state in plain language the subject, concrete action or choice, visible result, and stop or exit;
3. compare the earlier-edition head and modifiers, modal force, admitted referents/actions, excluded near-misses, and local interpretation burden;
4. probe the nearest alien case the candidate might newly admit and the nearest valid case it might newly exclude, naming any case that crosses the boundary; and
5. apply the differential disposition. `preserved` requires no unauthorized widening or narrowing and no greater decoding burden: a reader must not need campaign memory or an ontology-development memorandum to recover the action.

For a new action-guiding paragraph with no earlier edition, do not invent history. Test one nearby alien case that must remain outside and verify that the local wording itself exposes a recognizable situation, concrete action or choice, visible first result, and non-use or neighboring-pattern exit.

Keep the cheap path cheap. Formatting, typo, link, citation, or exact-reference corrections remain mechanical when the smallest comparison proves that no `E.8:4.1.2` materiality value changed. A bounded semantic edit checks only its affected wording group and use probe. Reuse an earlier hunk or lexical result only when the object and compared editions, changed scope, and assurance question match this extension, modal-force, near-miss, and interpretation-burden test; idea presence or broad-use preservation is not enough. This is one same-increment stable-candidate pass before acceptance or landing, not per-keystroke review, a new ledger, or a one-finding handoff.

**Earlier-edition differential.** For one candidate pattern edition × one earlier-edition use probe, distinguish the applicable disposition when the governing decision needs it:

| Disposition | Semantic test and recoverability |
| --- | --- |
| `preserved` | The situation, action, result, and required boundary remain semantically available; every material changed wording group retains its head-and-modifier extension, modal force, admitted valid cases, excluded near-misses, and no-greater-decoding-burden condition. The declared use remains admissible and replayable from the pinned editions. |
| `improved` | The required earlier-edition use and every required changed-wording boundary remain preserved, and a separate replay demonstrates an action, result, boundary, affordability, or interpretation-burden gain. |
| `transferred` | A discoverable handoff reaches one named neighboring pattern whose Solution carries the needed action guidance and exposes its result. A bare pattern ID or unreachable action is `regressed`. |
| `intentionally retired` | An accepted decision drops a harmful or false earlier-edition action and supplies the corrected positive action or boundary as the recoverability endpoint. |
| `regressed` | A required action, result, risk disclosure, cheap exit, or usable handoff is absent; or changed wording admits an unauthorized alien case, excludes a valid case, changes modal force, or makes the reader decode more unstated ontology. Repair or an explicit retirement decision is required. |

A use classified as unsupported historical residue before replay receives no differential disposition and supports no compatibility claim. New evidence of a valid earlier-edition use reopens that classification instead of restoring wording silently. A required `regressed` probe prevents a positive conclusion, but it does not stop inspection of the remaining independent probes.

**Candidate-only adequacy.** Review one candidate pattern edition × one new intended-use probe against its exact candidate-only basis, never against invented history. Distinguish these outcomes when the governing decision needs them:

| Outcome | Semantic test |
| --- | --- |
| **adequate for the candidate-only use** | The selected basis, recognizable situation, concrete action or choice, first useful result, action-changing boundary, intended reader, and one nearby alien case that stays outside are recoverable from the local candidate wording and executable enough for the declared use. |
| **absent or insufficient for the candidate-only use** | The use is only promised, named, over-broad, ambiguous, or unsupported; the intended reader cannot perform the action, distinguish the first result, reject the nearby alien case, or recognize the non-use/neighbor exit from the local wording. |

A missing candidate-only decision or basis is `absent or insufficient`; it never licenses a fabricated earlier edition. Absence for a required new use prevents a positive conclusion but does not stop the other independent probes. Absence for optional breadth is non-blocking by itself but cannot support breadth, transfer, or exceptional-expression claims. If no exact new intended use is selected, no candidate-only check opens.

**Replay the positive Solution separately.** Judge the following over the candidate edition when their answers can differ:

1. the governed subject;
2. the recurring problem and ordinary failure;
3. an executable proposed move;
4. a first useful result rather than completed review apparatus;
5. each prominent boundary or guard and the credible neighboring case whose action it changes;
6. guards that inspect an already present positive Solution instead of supplying its outline; and
7. for a Solution whose content concerns a Method, work, or world-side change, first distinguish content that defines, constrains, tests, or guides from an assertion of one actual occurrence. Method guidance alone triggers no fictive performer or Work. When an account asserts dated `U.Work`, verify the §4 actual-Work account; when it asserts a world-side change, identify the change relation, the pattern that defines it, and the things it relates. Keep the intended-reader position, any qualifying A.3.2 method-description episteme, actual performer, Work, and problem-facing result separate. Treat the item as defective if an episteme, checklist, plan, prose, or intended-reader or representation position performs Work.

Refine item 5 by boundary whenever boundaries can pass, fail, or route independently. Follow the short first-use rendering's action and result logic against a concrete situation. Merely finding words such as `situation`, `move`, `result`, or `stop` is not evidence. Repair each failed item or record it as an exact finding with remediation direction; do not replace the replay with one prose-quality impression.

**Replay each triggered enumeration.** Verify the semantic resolution selected under `E.8:4.1.2`: a declared closed set has one explicit membership rule covering every member; named-kind or proposition examples remain subordinate and explicitly non-exhaustive; heterogeneous neighbors do not assert a false common kind; an implicit kind, relation, or structure reaches an existing pattern or rule that defines or tests it, or remains blocked; and a hidden action or claim is stated before its examples. Review a member separately when its membership can fail independently or require a different repair. A genuinely small closed set may be judged together only when one rule yields one truthful conclusion for every member and no member can differ. Nearby nouns that assert no common membership, and an unchanged declared set or example list still covered by its exact rule, need no durable positive recital. A blanket `all lists are coherent` conclusion cannot replace review of a triggered enumeration.

Desk replay is the ordinary evidence mode for affected uses, changed wording groups, new action-guiding paragraphs, the positive Solution, and enumerations. Escalate to a cold reader, AI agent, or observed-work exercise when competing actions remain plausible, a near-miss boundary or result distinction is not recoverable by inspection, a transfer is uncertain, or a missed failure has high consequence. When a claim extends recurring applicability beyond the exact cases, do not treat three examples alone—the traditional rule of three—as validation. When the claim's value or consequence warrants it, select a proportionate qualitative practitioner survey, action-research cycle, or case study. Evidence escalation is risk-selected; it is not a universal benchmark or an ordinary-rewrite requirement. E.19 defines repair or finding outputs while leaving ordinal coordinate values and `PatternQualityStatus` to the full E.21 evaluation.

#### E.19:4.4 - Decision outcomes

Complete the selected review scope before making an admission, refresh, or return-for-repair conclusion. A first defect or already-negative conclusion does not end the search for other independently obtainable findings. If a condition makes the remaining questions impossible to judge truthfully or safely, name the unexamined scope and the condition instead of presenting a partial result as complete.

**Inspect, repair, and verify.** Complete every in-scope review application, repair every defect through the relevant authoring work, and perform focused verification over the affected questions. The changed pattern edition and focused-verification claims are the substantive evidence and remain distinct from work; constitute one aggregate E.19 result episteme only when a receiving admission/refresh decision needs it. Record only an unresolved blocker, a decision outside current authority, or work that must transfer; do not create a parallel list retelling completed repairs.

**Independent findings.** Leave one compact C.2.1 findings-result episteme or semantic handoff containing all actionable in-scope defects and blockers, ordered by semantic impact, with repair direction precise enough that the author need not rediscover the diagnosis. If the selected questions reveal no defect, create neither an empty pass report nor positive checklist recital. The findings result is not the dated review work or an authority-bearing admission decision.

If a governing admission, refresh, `E.21`, `DRR`, landing, or release decision requires a durable conclusion or value, use its existing result. That result may cite E.19 findings or the repaired candidate; it does not turn per-question positive outcomes into a second review record.

**Precision-remediation order.** When a defect sentence combines a generic head, a claim-bearing qualifier, and mixed comparison-criterion pressure, remediation SHOULD repair them in that order: restore head kind, then qualifier claim kind or admissible-use boundary, then comparison-criterion homogeneity. A narrowing qualifier does **not** by itself repair the head-kind defect. Only after those repairs may the review keep or reintroduce a Plain, didactic, or coarsened restatement, and only if the more precise upstream interpretation remains recoverable.

**Kind-restoration verification.** A wording, naming, or F.19 phrase-level repair does not succeed merely because the old trigger word disappeared. Recheck the pre-repair and post-repair kind, relation or claim kind, admissible use, and scope. If the repair narrows, widens, splits, or changes them without an accepted decision, repair it or keep the defect unresolved. The repaired object, focused verification, or governing decision carries this evidence; E.19 does not require a per-repair pass account.

**Ordering and effort.** Put ontology, semantics, modularity, and SoTA defects in FPF-governed sections before compact low-signal formatting findings. If semantic defects are present, address them before mechanical edits; formatting and micro-typos must not dominate the work by volume.

### E.19:5 - Archetypal Grounding — transfer across three pattern subjects

The common move is the same in all three situations: name the exact pattern edition and review question, apply `PCP-BASE` plus only the live risk profiles, inspect the complete selected scope, and either repair and recheck the defects or return one complete actionable findings set. What differs is the claim that must remain true for that pattern kind.

| Pattern subject and recognizable defect | Kind-specific question | First useful result |
| --- | --- | --- |
| **System pattern.** A safety-critical team proposes a subsystem-deployment pattern. Requirements appear in prose but not in the Conformance Checklist, new terms hide scope, and cross-team labels are treated as equivalent. | Do Solution and checklist constrain the same system claim? Does any claimed cross-context identity satisfy the applicable Bridge rule? | `PCP-NORM`, `PCP-TERM`, and, only when triggered, `PCP-BRIDGE` produce a repaired and rechecked requirement set or complete findings. The checklist becomes the stated conformance body, so later users do not read prose and checklist as different requirements. The result says nothing about whether the subsystem may deploy. |
| **Episteme or publication pattern.** An older evidence-sufficiency pattern still reads clearly, but its source basis, terminology, and Relations are stale, and its publication carrier is confused with the claim it carries. | Are the claim, its source use, currentness, publication occurrence, and carrier still distinct and supported by current sources? | `PCP-REFRESH` and the relevant terminology check produce updated Solution, source decisions, and Relations or complete findings for the author, followed by focused verification. Historical evidence remains labeled as lineage, so a clear-looking old pattern is not mistaken for current guidance. |
| **Method and Work pattern.** A review-method pattern says that a Method, checklist, or result performed the review. | Does the text merely guide a Method, or does it assert dated Work? If Work is asserted, who acted and what result followed? | The repair keeps ordinary Method guidance plain. It adds the acting system, Work occurrence, and result only for an actual occurrence, or returns that conflation as a finding. |

**Transfer result.** Profile selection and the two review forms transfer unchanged. What counts as correct does not: system requirements must agree with their conformance claims, episteme and publication uses must keep claims and carriers distinct, and Method guidance must not be mistaken for performed Work. A successful example from one row cannot stand in for either of the others.

### E.19:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** (applies to all patterns and all clusters).

Bias risks and mitigations:

* **Governance bias (Gov):** reviewers may over-prioritize compliance signals and under-prioritize teaching value.
  *Mitigation:* PCP‑BASE includes didactic grounding and internal coherence checks and priority for ontology and semantics, not to form.
* **Epistemic monoculture (Onto/Epist):** SoTA‑Echoing can become single-tradition name-dropping.
  *Mitigation:* require explicit multi-tradition coverage and usage of F.18 for neutral naming.
* **Pragmatic bias (Prag):** a pattern can be “correct” yet unusable.
  *Mitigation:* consequences and anti-patterns remain mandatory sections, surfacing trade-offs and misuse paths.
* **Didactic bias (Did):** narrative quality can be mistaken for truth.
  *Mitigation:* conformance and SoTA‑Echoing sections bind claims to explicit requirements and lineage.

### E.19:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-E19-0 (Review, result, and decision remain distinct).** | Keep the reviewed edition or subset, selected questions, ordinary reviewer action, repairs or findings, optional aggregate result, and authority-bearing decision distinct. If an account asserts actual review, repair, or verification `U.Work`, the §4 actual-Work account **MUST** hold; a compact result may omit only an assignment identifier unused by the receiving claim. Keep any local system-role kind and separate System-classification judgment distinct, and route unresolved source *role* through `E.10.ROLE`. A profile, checklist, record, result, or intended-reader or representation position performs no Work and grants no decision. | Prevents editorial declarations and records from acting as reviewers or authority without burdening an ordinary review with unused identities. |
| **CC-E19-0a (MVPK face and View boundary).** | When a PCP inspects an MVPK face or projected publication form, apply no-new-claim and no-shadow-default to the claims and defaults actually carried by that face/form. Keep selected episteme, optional projection/construction, face, publication form, publication occurrence, rendering, and carrier distinct. Assert `U.View` membership only for the selected episteme when exact E.17.0 conformance independently obtains; profile selection, projection, or compliance with these two checks supplies no membership. | Preserves publication/face discipline without turning E.19 into a View classifier. |
| **CC-E19-1 (Baseline triage is mandatory).** | Every configured PQG review **MUST** include **PCP-BASE** for the reviewed pattern or subset. When the baseline review is complete and finds no risk requiring another profile, the review may finish after any small mechanical defect is either repaired and checked or returned as an independent finding. This is only an `E.19` review boundary; it cannot support an `E.21` coordinate value, `PatternQualityStatus`, a claim that every coordinate is `4` or every coordinate is `5`, landing-quality claim, or improvement-movement claim without the complete `E.21` result required for that claim. | Ensures one shared triage floor without turning every review into a full audit or substitute quality measurement. |
| **CC-E19-2 (Profile selection covers the live risks).** | The review scope **MUST** name PCP-BASE, every risk-selected PCP, the risk selecting each additional profile, and any override. It **MUST** consider the whole current profile set rather than only the easiest visible family. When an override affects a later admission, refresh, or other governing decision, its false-positive reason and compensating check belong in that decision basis; successful profile choices need no per-profile pass entries. | Makes review depth repeatable without a separate record of successful checks. |
| **CC-E19-3 (Delta-Class & impact for breaking change levels).** | If the reviewed change is **Δ-2/Δ-3** per E.15, the governing change or decision result **MUST** carry Delta-Class, impact radius, a DRR pointer, and the required refresh and Bridge consequences. E.19 repairs or reports a missing or false account; it does not duplicate a successful one. | Keeps evolution controlled while leaving change evidence with the change decision. |
| **CC-E19-4 (Conformance-claim coherence is enforced).** | Inspect-repair-verify **MUST** eliminate orphan and unclaimed requirements by aligning the reviewed pattern's Conformance Checklist, deontic clauses, admissibility constraints, and Solution. Independent findings **MUST** identify each surviving incoherence and give concrete repair direction. | Preserves the CC as the enforceable conformance check set in both review forms. |
| **CC-E19-5 (Triage & noise discipline).** | The run **SHOULD** prioritize FPF-governed sections and deontic requirements (e.g. CC, content of deontic clauses and content of admissibility constraints, definitions, Relations, SoTA, modularity) and keep purely mechanical edits (e.g. RFC-form deontic cleanup) minimal. Template defects **MUST** be fixed before admission (or before closing a refresh run) but **MUST NOT** be used to skip semantic review. | Improves semantic trust without turning review into form-only compliance. |
| **CC-E19-6 (Review form and findings completeness).** | The review **MUST** choose one form from E.19:4.1 and inspect every independently answerable in-scope question even after the first defect, blocker, or negative conclusion. Inspect-repair-verify ends with every in-scope defect repaired and focused verification performed; independent review ends with one complete set of actionable defects and blockers plus concrete repair direction. A question that reveals no defect gets no durable pass entry. Early stop is allowed only when the remaining questions cannot be judged truthfully or safely, and then the unexamined scope and cause **MUST** be named. | Prevents both first-defect stopping and a third, report-producing review form. |
| **CC-E19-7 (Recognition text, assurance text, and self-containment).** | Admission or refresh runs for new and substantially revised patterns **MUST** check that a first-reading recognition text appears early enough for the intended reader, that the heavier assurance text remains visibly second rather than becoming the first real point of entry, and that the assurance text does not silently shift the recognition-text claim. The run **MUST** check for a recognisable working situation, what goes wrong if the pattern is missed, what the pattern buys, the first admissible action-guiding move the user should take, and an ordinary `not this pattern when` boundary; for any FPF-governed typed declaration or modeling lens, the run **MUST** confirm that a short user-facing statement exposes the primary `EntityOfConcern`, relation record, or claim record and the minimal lens that keeps it reviewable; the run **MUST** also check that the primary `EntityOfConcern`, relation record, or claim record keeps one stable kind across title, opening function, declaration function, worked slices, and related-pattern or companion guidance named by value rather than drifting between the named primary `EntityOfConcern`, an act, a work-result record, and carrier-placement labels. When a broader umbrella name and a narrower operative branch are both used, the run **MUST** check that the recognition text makes that stack explicit enough to identify the umbrella, the active branch, the primary `EntityOfConcern`, the move, and the wider work or process that still remains outside. The recognition text **MUST** start from a recognisable problem-owning domain or practice moment whenever that can be done without loss of precision, rather than opening first with internal package architecture or taxonomy language. Early FPF-governed technical terms **MUST** receive nearby pairwise plain glosses; transform-like families **MUST** carry concrete worked slices plus ordinary-vs-FPF-governed wording guidance where needed; and any `SoTA-Echoing` used as explanatory grounding **MUST** state a short practitioner or manager implication plus visible linkage to the worked cases or boundary slices it disciplines. If SoTA or practice tradition has FPF-governed use, the run **MUST** check that primary-EntityOfConcern choice, narrowed-branch choice, and practical payoff remain answerable to the relevant domain or practice rather than only to internal package architecture. If a pattern claims universal or transdisciplinary usefulness, the run **MUST** check that this breadth is already demonstrated in the recognition text through at least three heterogeneous situations, with `F.16` preferred as the example-matrix template. | Prevents architecturally correct but reader-opaque patterns and keeps broad claims from appearing only late in the assurance text. |
| **CC-E19-7a (Epistemic precision cleanup cannot leave inert recognition).** | If admission or refresh includes `E.10`-triggered epistemic precision restoration, check that the intended reader can still recover why the distinction matters, the remaining admissible use, and the pattern or rule contribution that carries any formal claim. Keep Plain or didactic wording ordinary when it adds no such claim; otherwise map it back to the repaired Tech reading under `E.10:6.2`. Add an exact assertion, predicate, `ClaimGraph`, or displayed identity only when it distinguishes truth, action, stop, or named reliance. If the Tech reading asserts dated Work, apply `CC-E19-0`. In inspect-repair-verify, restore any harmed working situation or first useful move; in independent review, record the exact harm. | Prevents type-correct cleanup from destroying practical guidance or forcing unused formal apparatus. |
| **CC-E19-8 (Sentence-level precision restoration).** | Review FPF-governed sentences for generic heads, claim-bearing qualifiers, overloaded trigger words, bare relation shorthand, hidden slots or relation positions, use-relation or claim-kind shorthand, and hidden process or API metaphors. An `E.10` scan closes only not-triggered and local lexical cases; episteme, publication, or source-use cases open `C.2.P`, and state-family cases open `A.19.SPR` or the pattern that defines or tests them. Restore head kind before qualifier claim kind or admissible-use boundary, then any live slot, relation position, use relation, claim kind, and comparison-criterion homogeneity. Verify the kind, relation, admissible use, and scope before and after the repair; broad umbrella wording exposes the umbrella, active branch, primary `EntityOfConcern`, first useful move, and outside work only when those distinctions carry the claim. Naming repair follows the `F.18 -> A.6.P` chain. Inspect-repair-verify leaves the repaired wording and focused check; independent review records only a broken chain, failed restoration, or blocker. | Keeps controlled technical writing from collapsing into free shorthand without demanding a positive phrase-by-phrase account. |
| **CC-E19-9 (Package-form, concrete pattern contribution, and package-relation function-word discipline).** | Check that `primary carrier`, `specialization`, `profile`, `overlay`, `family`, `bundle`, `cluster`, `suite`, `pack`, `kit`, `record`, `umbrella`, and local equivalents match the actual ontology rather than drifting by style. If a repair introduces or retains a head already occupied elsewhere in FPF, verify intentional reuse or repair/report the collision. | Keeps concrete pattern contributions, package relations, review functions, and package forms legible without recording successful collision checks. |
| **CC-E19-10 (Reader-fit discipline).** | Check every pattern host or monolith section for the intended FPF user, an explicit primary reader/concern/viewpoint when several readers are served, and separation of user guidance from package-development, review, evaluation, projection, landing, or release reasoning about the same pattern version. Part E patterns may govern authoring or review as their declared subject matter, but that does not admit development correspondence about the current version. Repair each leak or return its exact locus as a finding; sections with no leak need no scan recital. | Keeps reviews from accepting conceptually correct but reader-confused patterns. |
| **CC-E19-10a (Quality/projection carrier leakage).** | Check whether pattern prose, including Relations, Rationale, SoTA-Echoing, worked slices, examples, tables, and the Conformance Checklist, contains corpus projection, retrieval/cold-reader evidence, monolith parity, landing evidence, `PatternQualityStatus`, all-`4`/all-`5` posture, or development correspondence about that pattern version. This is a sentence-function check, not a lexical search. Move such material to the applicable `E.21` result, E.19 findings, README/ToC/E.11/I.2, projection, release, or landing result and retain only the pattern's admissible user-facing move or boundary. | Prevents quality and projection proof from becoming pattern prose. |
| **CC-E19-11 (Precision before relaxation).** | If remediation preserves or introduces a Plain, didactic, or coarsened restatement of a repaired FPF-governed sentence, the run **MUST** keep a more precise upstream interpretation recoverable and must not let the softened form become the only wording with authority-reference claim kind or admissible-use boundary. | Keeps later readability aids subordinate to an explicit more precise interpretation. |
| **CC-E19-12 (Integration impact is checked).** | Before send or monolith-facing motion for a new or substantially revised subset, inspect related patterns and the concrete constraints or tests they supply, companion notes, Relations entries, and monolith sections. Repair each in-scope mismatch or return it as a finding and name any genuinely outside boundary. Successful synchronization remains in the changed sources and governing landing or release result. | Prevents an isolated local improvement without duplicating synchronization evidence. |
| **CC-E19-13 (Usability and proxy-to-value are checked).** | For a new or substantially revised subset, check recognition versus assurance text, first-minute situation, practical payoff, ordinary boundary, worked slices, primary reader/viewpoint, and the applicable `E.8`, `E.12`, `E.13`, `E.14`, `E.17.*`, `F.16`, or local-equivalent questions. Repair or report a usability defect. If a score, coordinate, benchmark, projection signal, or all-`5` posture is used as value evidence, the governing `E.13` result—not an E.19 pass account—must carry intended value, proxy use, gains, losses, minimally viable value slice, and reopen condition. | Prevents visible review success from replacing practical value. |
| **CC-E19-14 (Scenario, anti-case, and utility fit are checked when applicable).** | When the domain has a relevant scenario pack, anti-case corpus, pilot bank, utility tree, fitness catalog, or analogous common source, use its applicable cases and qualities. Repair a failing case or return the exact failure, missing source, or out-of-scope boundary as a finding; do not record cases that revealed no defect merely to prove consultation. | Keeps common validation sources active without a separate consultation record. |
| **CC-E19-15 (Packaging, concrete pattern contribution, package relation, and shipping fit are checked).** | Before a send-, landing-, or monolith-facing claim, inspect the relevant package form, the definition, constraint, test, or other pattern contribution actually used, package relation, publication function and authority reference, and the actual send, landing, and monolith facts. Repair or report any mismatch. The governing release or landing result carries the successful state claim; E.19 does not repeat it. | Keeps shipping claims truthful without a second state account. |
| **CC-E19-16 (Domain-tightened profile depth is applied).** | When a domain-specific depth note such as semio `FIT-*` applies, use it to tighten the selected PCP questions. Repair or report any defect it reveals; do not add positive or not-found recitals to an E.19 result. | Keeps domain-specific depth operative rather than optional folklore or extra reporting. |
| **CC-E19-17 (Companion-material retention is justified).** | When a new or refreshed pattern subset keeps a long-lived companion, profile, check sheet, pattern-local companion row, review harness, or analogous selected non-pattern FPF kind-reference pair, the result **MUST** make its companion function explicit: companion use question, concrete pattern contribution or selected non-pattern FPF kind-reference pair served, admissible companion-only use, one real breakage if absent, and retention, accepted-source-material-only, or removal condition when no such breakage exists. | Prevents companion material from remaining by inertia or becoming hidden authority after the pattern body already carries the usable guidance. |
| **CC-E19-18 (Substantive solution and locus adequacy is checked).** | A new, refreshed, or materially repaired subset **MUST** receive a pattern-specific substantive adequacy check unless the change is purely mechanical. Check whether it still solves the stated problem, assigns claims to the correct governing loci, preserves kind boundaries and selected companion/projection functions, keeps SoTA grounding current enough, remains usable without excess apparatus, and worsens no content relation. Repair each in-scope failure or return it as a finding and name any needed wider boundary. Questions that reveal no defect need no separate account. | Prevents clean checklists and terminology from hiding wrong content. |
| **CC-E19-19 (Accepted-decision carry-through is checked).** | When the reviewed pattern, subset, or current change is claimed to implement an accepted `DRR`, returned findings, intake, architecture source material, or other accepted source named by value, inspect each applicable decision against the reviewed loci or the named concrete pattern contribution, claim, companion, result, or source that carries it. Require exact predicate or defining `ClaimGraph` identity only when the decision or named reliance needs it. Repair or report partial, missing, wrongly rejected, wrongly routed, or wrongly classified carry-through. The accepted source remains the decision source; do not duplicate decisions expressed sufficiently, inherited unchanged, correctly absent, or outside the subset. Keep `E.17.ID.CR` units, `PublicationUnit`, publication forms/faces, source materials, and project-side review relations in their governing kinds. | Prevents accepted decisions from disappearing without making E.19 their second authority. |
| **CC-E19-20 (Pattern-quality review is not project certification).** | If an `E.19` result is reused outside FPF pattern-quality review, the project-side governing result **MUST** name the project-side claim, relation, and required evidence or assurance. `E.19` alone **MUST NOT** be treated as project evidence, gate input, release justification, compliance or safety assurance, work authority, or publication truth. E.19 repairs or reports misuse; it does not create a duplicate project-side account. | Prevents pattern review from supplying false project-world certification. |
| **CC-E19-21 (Precision-restoration distribution is preserved).** | When the reviewed change applies or edits `E.10`-triggered precision restoration, the run **MUST** check that the selected precision-restoration architecture remains distributed: `E.10` states trigger and applicability, `E.10.ARCH` states shared recovery architecture, realization patterns perform ontological unpacking for the EntityOfConcern, relation, claim, characteristic-space item, state-family field, or other selected ontological neighborhood named by value, and affected patterns carry only thin pointers named by value unless they themselves work over the recovered primary entity, relation, claim, characteristic-space item, state-like field, or phrase or record named by value. A review fails this row when an affected pattern silently grows a second trigger registry, a duplicate recovery algorithm, or a local architecture that contradicts the selected restoration pattern. | Prevents pattern admission or refresh from re-centralizing wording-use restoration or duplicating `E.10.ARCH` inside affected patterns. |
| **CC-E19-22 (EntityOfConcern and precision-restoration triage is applied).** | For the changed span and every affected current host, check: the pattern's own object, action guidance, practical delta and non-use; same-referent preservation; slot or reference migration; any retargeting result; the intended alignment path; description and publication-use guards; phrase and semio-bias repair; architecture, package and quality apparatus whose function changed; and one disposition for every affected consumer. Route claim-bearing *role* through `E.10.ROLE`; apply A.3.1 and A.3.2 before claiming Method or MethodDescription; add formal identities only when truth or named reliance needs them. Use E.21 `PrecisionRestorationProfile` when that evaluation is active, and apply `CC-E19-0` to dated Work. | Prevents a type-correct rewrite from changing referent, path, use, or consumer behavior while keeping precision restoration auxiliary to the pattern claim. |
| **CC-E19-23 (Pattern-edition use-value replay preserves distinct outcomes).** | When `E.8:4.1.2` selects a material edition change, judge separately only the materially affected use probes whose exact earlier-edition or candidate-only basis, working use, expected result, boundary, necessity, evidence, or repair can differ. Inside each affected earlier-edition probe, give every materially changed normative sentence or inseparable reader-task group its applicable differential disposition after comparing head/modifiers, modal force, admitted and excluded cases, nearest alien/valid boundary cases, and interpretation burden. A new action-guiding paragraph supplies a local situation, action, result, non-use/neighbor exit, and nearby alien case without invented history. When a narrower contribution is kept, merged, removed, profiled, reused, externally supplied, or omitted, apply `E.8:4.1.3`; distinguish the available maintained result and supplying product, maintained `MethodDescription`, direct-source evidence, and named unavailable result; test the external-result use and availability boundary; and, after a material promised-family change, require the current `E.4.DPF.DA` `D12DomainProblemFamilyCoverageAdequacy` result for the resulting exact DPF or LPF edition. Reuse that package result only while its exact basis remains unchanged, without demanding proof that a revisit occurred. Replay the positive Solution and independently contestable enumeration members, continue after failures, and reuse other prior results only when object/versions, scope, and assurance question match this exact test. Run this once on the stable candidate before acceptance or landing; do not create per-keystroke review, a second ledger, or positive recitals. | Prevents broad-use preservation from hiding sentence-level extension drift, false external coverage, family-level loss, or ontology-bureaucratese while keeping bounded edits cheap. |

### E.19:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | How to avoid / repair |
| ---------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------- |
| **Primary-EntityOfConcern drift** | The draft appears to govern one thing in the opening, another in the declaration block, and a third in the examples or related-pattern or companion guidance named by value. | Review cannot tell whether the pattern defines or constrains a `PublicationUnit`, an interpretive move, a work-result record, or a whole process, so later naming and boundary decisions become unstable. | Stabilise one primary `EntityOfConcern` early, keep its head kind explicit, and mark note, sheet, UI, rendering, or process labels as either examples of that object or separate related entities rather than stylistic substitutes. |
| **Reader-fit clean but pragmatically foggy** | The draft is addressed to the right reader in principle, but cold working readers still cannot recognise the situation, practical payoff, primary `EntityOfConcern`, relation named by value, claim record, or first useful move early enough. | The run passes reader-fit hygiene while still failing pragmatic fit and first-minute usability. | Pull a recognisable working situation upward, add one minimally viable worked case, make the practical payoff explicit in nearby user-facing prose, expose the primary `EntityOfConcern` and any minimal modeling lens in plain terms, add plain glosses for early claim-bearing terms, and require `SoTA-Echoing` rows that carry claim kind, admissible-use boundary, or explanatory work to name the practitioner or manager implication plus the case they discipline. |
| **Architecture-clean but domain-thin** | The text is internally well placed in the package, but the primary `EntityOfConcern`, narrowed branch, or practical payoff are justified mainly through package architecture while the problem-owning domain, practice, or SoTA appears late or decoratively. | The pattern passes internal architecture checks while drifting away from the domain whose work it claims to improve. | Pull the problem-owning domain moment into the recognition text, make the narrowed branch and primary `EntityOfConcern` answerable to the relevant domain or practice, and require FPF-governed `SoTA-Echoing` to discipline the practical cases rather than merely bless them after the fact. |
| **Type-correct but inert epistemic precision cleanup** | An `E.10`-triggered repair restores kind language but leaves the reader unable to say why the distinction matters, what use remains, which definition, constraint, or test carries a formal claim, or how Plain wording maps back to the Tech reading when both registers are used. | The review accepts typed wording while losing action guidance. | Restore the working situation, remaining admissible use, and the contributing pattern or rule; map Plain wording back to the Tech reading when both are used. Keep the explanation ordinary unless a live contrast or named reliance needs an exact assertion, predicate, `ClaimGraph`, or displayed identity. Apply `CC-E19-0` only if the repaired claim asserts dated Work. |
| **Expressive overread rebound after epistemic precision cleanup** | The pass makes the text more engaging, but the added Plain or didactic wording carries an ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim not recoverable from the Tech reading or cited rule. | The review mistakes readability for recovered semantic work. | Keep the line ordinary when it only helps recognition. Otherwise recover the claim kind or admissible-use boundary through the Tech reading and cite the pattern or rule that defines or tests it, or demote the phrase to reduced-use cue, quote-only wording, blocked transfer, or rewrite incomplete. |
| **Profile or record as reviewer.** | A selected PCP, checklist, findings form, result episteme, or review record is said to have performed the review, repaired the pattern, admitted it, supplied assurance, or authorized downstream use. | Reviewer action, repair, result, evidence, and decision authority collapse. | Say ordinarily that a reviewer applies the questions and name the action actually performed. Profiles declare checks and records package references only. Apply `CC-E19-0` only when the claim deliberately asserts dated Work; add evidence, assurance, or decision relations only when they independently obtain. |
| **Verdict-only review** | Independent review ends with pass/fail or prose complaints but no complete actionable finding set, or repair-mode review reports defects without repairing and rechecking them. | Leaves later work to rediscover diagnosis or mistakes an intention to repair for a completed repair. | In independent review, record every actionable in-scope defect and blocker with precise direction; in inspect-repair-verify, repair and verify them. Questions with no defect get no durable pass recital. |
| **Single giant checklist** | Review becomes a long, unfocused ritual that few complete. | Increases cost; reduces fit and rigor in practice. | Use a minimal baseline plus risk-selected profiles; use `E.21` only when a pattern-version quality value is being evaluated. |
| **Template-only compliance** | All headings exist, but requirements are vague and untestable. | Looks uniform; fails enforceability and auditability. | Enforce normative clause hygiene and CC/Solution coherence. |
| **SoTA name-dropping** | SoTA-Echoing is a list of buzzwords with no stance. | Breaks evidence lineage; invites monoculture. | Require adopt/adapt/reject with reasons per item. |
| **Terminology drift by “synonym”** | Authors swap kernel terms for nicer-sounding words. | Increases ambiguity; harms cross-pattern composability. | Apply PCP-TERM and require explicit mini-definitions on first use. |
| **Lexical substitution accepted as repair** | The reviewed text no longer contains the trigger word, but the replacement changes the FPF kind, relation, current ontic slot, relation position, use relation, or claim kind, admissible use, or scope. | The review rewards surface cleanup while ontology drift remains or gets worse. | Require a `KindRestorationCheck`; if pre/post kinds or slots, relation positions, use relations, or claim kinds do not match or an accepted split/change decision is absent, keep the finding blocking. |
| **Form-only review** | Review time goes to formatting and micro-edits while the normative content, terms, Bridges, modularity, slot discipline and SoTA stance are barely checked. | Raises editorial cost without raising semantic trust. | Use the triage rule: treat FPF-governed sections as depth loci and keep mechanical cleanup subordinate to semantic correction. |
| **Checklist-clean but content-wrong** | The named profiles, lexical checks, and conformance rows are marked complete, but the repaired text no longer solves the stated problem, assigns a claim to the wrong locus, creates shadow authority, loses a selected companion or projection function, or adds needless boilerplate or support material. | Review accepts a locally tidy pattern while weakening the actual `FPF` guidance. | Apply substantive solution and locus adequacy: name local content questions, check the actual problem and governing loci named by value, ask what became worse, and widen the declared boundary by value when the fix belongs outside the initial reviewed pattern or subset. |
| **Architecturally right, didactically thin** | The family is admissible, but readers still need project notes to understand what the pattern really governs. | Trust in the monolith depends on external context rather than the pattern text. | Add the missing problem frame, worked slices, local definitions, and guidance naming the concrete contribution of a relevant pattern or the project-side FPF kind and reference before admission. |
| **Scenario-name grounding** | Grounding names a situation but does not show what the source and resulting publication actually look like. | Readers cannot tell why the case stays in the family or where it leaves the family. | Add concrete source and resulting-publication slices, especially for transform families and easy boundary confusions. |
| **Generic-head underspecification** | An FPF-governed phrase uses a generic head such as `note`, `view`, `guidance`, `output`, or `artifact`, but the run leaves that head uninterpreted. | Review discusses the sentence before the object kind is even stable. | Restore the head kind first in pattern-local terms before accepting or comparing the sentence. |
| **Qualifier-smuggled claim kind or admissible-use boundary** | A modifier such as `comparative`, `safe`, `interactive`, `reliable`, or `faithful` is doing the semantic work while the run treats the phrase as already precise. | The review blesses apparent precision without recovering the actual claim kind or admissible-use boundary. | Unpack the qualifier into explicit claim kind or admissible-use boundary, comparison criterion, or downstream-use boundary before acceptance. |
| **Mixed comparison criterion** | One sentence compares or ranks publication-form, carrier, process, authority-reference, or project-record values on one comparison criterion. | The sentence remains ontologically incoherent even after local wording is polished. | Restore head kind, then qualifier claim kind or admissible-use boundary, then rewrite the comparison through a homogeneous claim-kind criterion, threshold, or named defining, constraining, or source-relation condition. |
| **Sentence-level shorthand drift** | A few innocent-looking words (“species”, “branch”, “flow”, “input/output”) quietly carry the claim kind or admissible-use boundary. | Review passes while key relations remain implicit or wrong. | Inspect FPF-governed sentences one by one and replace shorthand with explicit claim or relation definitions, constraints, tests, package relations, or publication language. |
| **Package-form, pattern-contribution, and package-relation drift** | The text slides between `family`, `bundle`, `cluster`, `profile`, `overlay`, `suite`, `kit`, or `record` without showing that the ontology changed. | Reviews miss the difference between a concrete pattern-to-claim contribution, an authority reference, and a package relation because each local sentence still sounds plausible. | Require one intended package-function word, name the definition, constraint, test, or other pattern contribution actually used, check the package relation explicitly, and treat stylistic noun-swapping as a semantic defect. |
| **Reader-fit leakage** | Pattern sections explain why the pattern was isolated, what landing form is safest, or why merge or freeze is premature. | Review accepts a package memo disguised as a user pattern. | Move package-development reasoning to its companion or release result; keep the pattern in terms of what the user may do, must avoid, and which pattern defines or tests any separate release, policy, assurance, gate, action-selection, or adjudication claim. |
| **Quality-carrier leakage** | Pattern prose explains corpus projection, retrieval evidence, monolith parity, landing evidence, `PatternQualityStatus`, all-`4`/all-`5` posture, or development correspondence as if it were user guidance. | Review accepts quality proof or package evidence disguised as pattern content. | Move it to the governing `E.21`, E.19 findings, README/ToC/E.11/I.2, projection, release, or landing result; keep only the user-facing move or boundary justified by that evidence. |
| **Apparatus overwrap** | A simple claim, relation, object, action, or placement is wrapped in role-word, carrier, locus, flow, state, status, text, package, or process language that adds no new kind or user-facing action. | Review accepts bureaucratic prose as precision, or replaces it with prettier prose that loses the FPF kind. | First ask whether the extra word changes a recoverable kind, relation, claim kind, admissible use, evidence value, or user-facing action. If yes, use precision restoration. If no, rewrite in plain FPF terms and verify kind preservation: same `EntityOfConcern`, head kind, relation or claim kind, and established FPF term. |
| **Companion material retained by inertia** | A companion note, profile, check sheet, companion row, or review harness remains attached to a pattern family after the pattern body already carries the usable guidance, but the text does not say what real breakage returns if that companion material is absent. | Companion material becomes permanent local folklore, hidden authority, or reader cost without a corresponding use gain. | State the companion-use question, governing source, companion-only use, real breakage if absent, and retention, accepted-source-material-only, or removal condition; otherwise fold the useful example into the pattern or keep it only in the accepted source material. |
| **Pattern-quality result as project certificate** | An `E.19` pass is cited as proof that a project release, safety claim, compliance state, work result, publication, or gate has passed. | Collapses FPF pattern-quality review into project-world evidence or gate authority. | Keep `E.19` as pattern-quality review; open `A.10`, `B.3`, `A.20`, `A.21`, `A.15`, or the pattern that defines or constrains the project-side claim being made. |

### E.19:9 - Consequences

| Benefits                                                                         | Trade-offs and mitigations                                                                   |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Repeatable admission decisions** — reviewers share a common review language.     | More explicit editorial work; mitigated by a small baseline and risk-selected profiles.        |
| **Higher trust in normative content** — CC becomes the enforceable conformance check set. | Authors must align prose and CC carefully; mitigated by coherence checks.                  |
| **Controlled evolution** — runs prevent conceptual bit-rot.              | Periodic workload; mitigated by prioritizing high-dependency and high-risk patterns first. |
| **Less hidden drift** — terminology and cross-context reuse become explicit.     | Some drafts will be delayed; mitigated by early profile selection during authoring.        |

### E.19:10 - Rationale

Patterns are both **teaching publications** and **normative guidance publications**. A specification that grows without explicit quality gates becomes a patchwork: locally good, globally inconsistent. A profile-based gate is the smallest structure that keeps reviews repeatable while remaining sensitive to risk and pattern kind.

The baseline profile protects cross-pattern comparability and editorial sanity. Risk-selected profiles keep depth where it matters: norms, SoTA claims, cross-context reuse, terminology changes, staleness refresh, and reader fit. A pattern that is admissible in package terms but speaks to the wrong reader is still a review defect.

### E.19:11 - SoTA-Echoing — problem-first comparison of review approaches

**Working trade-off.** For one exact FPF pattern edition, detect semantic, ontological, practitioner-use, and source-currentness defects without making an ordinary review cost more than its likely harm warrants. No single current practice dominates that trade-off. Cheap tools and fixed checklists cover narrow repeatable properties; independent human review exposes contextual defects; practitioner studies test claimed transfer; living-guidance practice keeps volatile claims current. `E.19` therefore combines the non-dominated moves below—those for which no compared alternative improves one side without worsening the other—instead of importing one external workflow.

**Evidence binding.** If a current SoTA Synthesis Pack answers this exact review or refresh trade-off, cite it and keep this section consistent with it. Otherwise, the table below is the current source-use basis for this revision. Do not copy it into another seed list or treat a reference-only source as SoTA.

| Current approach and source | Coverage and effort | E.19 decision | Where this changes E.19 |
| --- | --- | --- | --- |
| **Proportionate independent assurance.** UK Government Analysis Function, *The AQuA Book* (2025). | Scales assurance by consequence, complexity, novelty, reuse, longevity, and uncertainty; separates the analyst, independent assurer, and approver. It catches fit-for-use and reasoning defects that template checks miss, but deeper independence costs more. | **Adopt and adapt.** Use those factors to select depth and retain an independent-findings form. Do not import government roles, approval stages, or mandatory assurance records into an ordinary FPF review. | The depth rule in §4; the two-form choice in §4.1; risk-selected profiles in §4.3; result and decision separation in §4.4. |
| **Lightweight change review with bounded automation.** Sadowski, Söderberg, Church, Sipko, and Bacchelli (2018), “Modern Code Review: A Case Study at Google”. | Empirical study of nine million code reviews supports small changes, quick iterations, human review, and tool assistance as an affordable engineering line. Its evidence is code-specific and does not establish pattern semantics or transdisciplinary transfer. | **Adapt, domain-bounded.** Keep one stable candidate, cheap mechanical checks, focused recheck, and a local-repair stop. Reject the code-review workflow and approval convention as FPF review semantics. | The local stop in §0.2; quick-pass automation in §4.2.1; stable-candidate and focused-recheck rules in §4.3.3. |
| **Practitioner-facing pattern validation.** Riehle, Harutyunyan, and Barcomb (2025), “Pattern Discovery and Validation Using Scientific Research Methods”; Iba (2021) remains bounded writing and critique guidance. | Qualitative surveys, action research, and case studies test recurring applicability and transfer more directly than template conformance or three examples alone, but they cost more than desk replay. | **Adopt selectively.** Escalate when universal or transfer claims remain uncertain or a missed failure has high consequence. Keep Iba for recognition, examples, consequences, and critique; do not treat critique culture alone as validation proof. | The three-situation recognition strip; §5 transfer slice; evidence escalation in §4.3.3; the breadth test in `CC-E19-7`. |
| **Narrower-contribution and family-coverage review.** Riehle, Harutyunyan, and Barcomb (2025); Chuprina et al. (2024), *Towards an Approach to Pattern-based Domain-Specific Requirements Engineering*; Marchezan de Paula et al. (2022), *Software product line scoping: A systematic literature review*. | Pattern validation supports cases and actual-use evidence; the domain-specific requirements case shows domain content changing parameters, defects, checks, and verification but remains an early proof of concept; product-line scoping separates reusable-contribution and family-boundary decisions but uses software-specific machinery. None supplies an FPF specificity threshold or package-adequacy result. | **Adapt and bound.** Check the action-changing contribution, four truthful return forms, honest external-result boundary, material family-change trigger, and exact-basis result reuse. Reject feature models, software-product ontology, component-count adequacy, and proof of a revisit as universal review rules. | `E.19:4.3.3` and `CC-E19-23`, using `E.8:4.1.3` for the contribution decision and `E.4.DPF.DA` for package coverage. Reopen when current practice changes the actual-use test, external-result boundary, family-scope decision, or safe reuse basis. |
| **Living-guidance refresh.** Cheyne et al. (2023), “Methods for living guidelines: early guidance based on practical experience. Paper 1: Introduction”; PRISMA 2020 remains reporting lineage. | Prioritises questions for living mode, varies surveillance frequency, updates the smallest recommendation affected by new evidence, and permits transition out of living mode. PRISMA adds transparent reporting of what changed, but not a living-review architecture. The approach improves currency but carries sustained cost and comes from clinical guidance. | **Adapt, domain-bounded.** Reopen the smallest affected FPF pattern or subset on a material trigger and stop continuous surveillance when its expected gain no longer justifies the effort. Reject clinical governance, GRADE machinery, and PRISMA forms as universal FPF process. | `PCP-REFRESH`; the bounded review object in §4.1; the reopen and stop rules. |
| **Narrow structural, ontology-tool, and retrieval checks.** ISO/IEC/IEEE 42010:2022; Garijo, Corcho, and Poveda-Villalón (2021), “FOOPS!: An Ontology Pitfall Scanner for the FAIR Principles”; RAGAS and ARES (2023–2024). | Each supplies a repeatable check for a different narrow property: structured-description consistency, selected FAIR-ontology pitfalls, or retrieval context relevance, answer relevance, faithfulness, and context adequacy. None tests the whole E.19 problem, and their outputs are not comparable pattern-quality scores. | **Retain only for the named property.** Use ISO 42010 as a structure reference, FOOPS! only when a machine-readable ontology is actually under review, and RAGAS or ARES only for a selected retrieval fixture. Reject a clean tool result as admission, usability, ontology, or source-currentness proof. | `PCP-BASE` structure checks; quick-pass automation in §4.2.1; `PCP-ENTRY-E4`; the no-project-certificate boundary. |

**Selected current front.** Ordinary E.19 use combines a lightweight stable-candidate review with cheap bounded automation, then scales review depth by likely harm, novelty, reuse breadth, and source volatility. It preserves independent findings as a real review form, tests breadth with practitioner evidence only when the claim warrants it, and refreshes the smallest triggered unit. A universal exhaustive checklist costs more without reliably finding contextual defects; tool-only review costs less but misses semantics, practical use, and current-source decisions. Reopen this choice when another approach demonstrates equal or better detection of those four defect families at lower comparable effort.

Action result from the pattern-review and validation practice grounding: a favorable, cautionary, or return-for-repair E.19 result episteme, clean checklist, or clean retrieval-entry check does not become project certification, project evidence, safety/compliance assurance, gate input, release justification, work authority, publication truth, or project refusal/approval. Its EntityOfConcern is the exact reviewed FPF pattern edition or subset; its ClaimGraph states the review scope, applicable profiles, findings or aggregate cleared boundary, conclusion, non-use, and reopen condition. Review/repair/verification work, witnesses and evidence use, F.10 status use, B.3 assurance, publication/currentness, and any authority-bearing admission or refresh decision remain separate. Reopen the result when the reviewed text, accepted-source-material decision, SoTA grounding, a related pattern or concrete constraint it supplies, selected companion/projection function, profile trigger, review boundary, or attempted project-side reuse changes.

### E.19:12 - Relations

* **Builds on:**

  * `E.8` (authoring conventions; canonical section order; SoTA-Echoing authoring requirements)
  * `E.10` (lexical discipline, trigger detection, and applicability)
  * `E.10.ARCH` (distributed precision-restoration architecture and realization-pattern split)
  * `E.9` (design rationale records for changes that affect semantics)
  * `E.9.DA` (content-first adequacy check for one exact DRR before pattern drafting or host amendment. An ordinary bounded check returns precise findings or repaired text; a full coordinate result and exact assessment identities are added only when explicitly requested or used by a named later reliance. An E.19 finding may expose an upstream DRR defect, but an E.19 pass, return, or absence is not E.9.DA evidence.)
  * `E.22` (improvement-oriented quality-evaluation question framing; distinguishes floor blocker review, exceptional-improvement review, Pareto trade-off inspection, open-question discovery, and absorption impact before an E.19 review result is formed.)
  * `E.23` (repeated quality-improvement method; an E.19 profile can supply questions and findings inside such a loop, but E.23 governs repeated absorption, object-under-improvement re-evaluation, method-family selection, and stop, continue, switch-method, open-new-frame, or hold decisions.)
  * `E.15` (authoring/evolution protocol; harness mindset; refresh planning)
  * `A.6.5` (slot discipline; SlotKind/ValueKind/refMode invariants)

* **Coordinates with:**

  * `A.15.1`, `F.6`, `A.2`, and `A.2.1` (actual review, repair, or verification Work and the assignment under which each performer acted); `A.6.1` separately defines check applications and bindings
  * `A.3.2` and `E.10.ROLE` (the full `U.MethodDescription` membership test and recovery of an ambiguous source *role* without forcing a system-role kind, assignment, participant, or representation position)
  * `C.2.1` (finding, focused-verification, aggregate review-result, and optional record epistemes)
  * `A.10` and `B.3` (evidence use/provenance and any assurance or reliance on an E.19 result)
  * `F.10` and `E.24.PUB` (status use/interpretation and publication occurrence/form/carrier; neither is review work or admission authority)
  * `F.8` (mint vs reuse decisions)
  * `F.18` (local-first naming protocol)
  * `F.9` (cross-context alignment discipline)
  * `F.15` (conceptual harness and regression framing)
  * `E.17` (MVPK publication and face discipline; an MVPK face, projected publication form, projection/construction, publication occurrence, rendering, and carrier remain distinct)
  * `E.17.0` (independent conformance required before the selected episteme has `U.View` membership; E.19 profile checks and no-new-claim/no-shadow-default compliance create no membership)
  * `E.11` (pattern-entry discoverability discipline, for `PCP-ENTRY` only as a review hook, not as a semantic prerequisite)
  * `E.13` (pragmatic utility and proxy-to-value alignment when a pattern-quality pass, score, coordinate value, checklist result, benchmark, projection signal, or release posture is being used as value evidence)
  * `E.21` (scoped pattern-quality characteristic space, coordinate evidence discipline, `PatternQualityStatus`, and stop condition; E.19 findings may become evidence only through the exact E.21 assessment application. Final coordinate values and `PatternQualityStatus` belong to a separate E.21 result episteme, not the E.19 profile or result.)
  * `A.6.7` (`MechSuiteDescription` suite-level semantics)
  * `A.15.3` (`SlotFillingsPlanItem` P2W planned-baseline seam)
  * `G.11` (refresh/decay orchestration principles, where applicable)

### E.19:End

