## E.17.ID.CR - Compare Sources Within a Shared Review Frame (ComparativeReviewUnit)

> **Status:** Stable

**Plain-name.** Bounded source comparison under a shared review frame.

**Use this when.** A team needs a small note, comparison sheet, or guided aid to compare available source epistemes or source publications. The unit should make one bounded contrast or a small set of contrast rows available for inspection, keep their shared review frame visible, and leave downstream claims and effects to the work that establishes them.

**First-minute working moment.** A team has two or more source-pinned notes, sheets, views, or review aids on the table. They need one comparison unit for their review: two design options for one release, two methods for one task family, two vendor bulletins for one control scope, two research syntheses for one uncertainty question, or two programme strategies for one initiative. The note compares the sources. Action selection, approval, ontology repair and wider control of the work remain separate. A comparison alone cannot decide among the options.

**First output.** One bounded comparison whose minimum content for ordinary use can be recovered in the unit or its immediate review context. A source-linked paragraph or small comparison table may suffice. The card below helps recover that content. The card can stay in the review context unless a receiving contract requires its separate publication. Include a blocked-use or boundary field only when it changes this comparison’s interpretation or use:

```text
ComparativeReviewUnit:
  ReviewedSources:
  SharedReviewFrame:
  ComparedAlternatives:
  ComparisonCriterionOrRows:
  BoundedLift:
  BlockedDownstreamClaimOrEffect:
  BoundaryTrigger:
```

**What goes wrong if missed.** A comparison unit is either dismissed as harmless prose or overread as equivalence, action selection, gate pressure, release approval, work or reliance guidance, or adjudication authority. The team then argues about hidden authority instead of inspecting the bounded contrast.

**What this buys in practice.** The team can compare the available sources, inspect one bounded contrast or a small comparison sheet, and identify a claim that goes beyond the comparison and the pattern that governs it when the boundary trigger fires.

**Not this pattern when.** If the primary question is no longer the bounded comparison unit or its shared review frame, name the crossed claim and apply the governing pattern for that claim: source transformation, bridge, explanation face, prompt or action selection, ontology or `EntityOfConcern` change, decision, work or reliance, gate, assurance, adjudication, or reduced-use source rendering.

**Quick working-fit check.**
1. Is the comparative review unit my work object?
2. Does the comparison preserve the shared review frame and keep distinct alternatives separate?
3. Is one bounded contrast or small row set being made visible?
4. Is the downstream claim or effect still outside?

If yes, stay here and keep the ordinary minimum recoverable. If no, use the neighboring-work boundary in `E.17.ID.CR:4.5`.

### E.17.ID.CR:1 - Problem frame
Engineer-managers, programme leads, and research or cultural reviewers often need to prepare or share a small unit that helps a team read two available source epistemes or source publications together. The aim is to compare them without overstating the downstream claim or effect the unit carries.
Typical moments include:
- a design-review note that says one already available option write-up foregrounds coupling risk more than another;
- a release or compliance comparison that says an internal control sheet and a vendor bulletin are not yet equivalent even though they speak to the same review task;
- an operations comparison that says a dashboard view and a maintenance note foreground different operational pressures in the same service episode;
- a research-review note that says one available synthesis foregrounds measurement uncertainty more than another without yet declaring a better method;
- a program or cultural review note that says one available brief foregrounds participation continuity more than another without yet deciding funding, curation, or program direction.

These comparison units make the next review discussion more precise.
Their risk is that a reader may treat a comparison as establishing equivalence, root cause, redesign priority, action selection, program choice, or approval.

### E.17.ID.CR:2 - Problem

Without a named comparative-review-unit discipline:
1. a useful comparative review unit is dismissed as harmless prose;
2. a cautious review aid is read as a licence for substitution, interoperability, or equivalence;
3. a calmly worded comparison can conceal pressure to select an action or conceal work on a hypothesis;
4. same-entity viewing, explanation rendering, and bounded comparison are treated as one kind of review;
5. ontology-facing target shift or changed EntityOfConcern hides inside comparative wording;
6. a review unit written to serve review is mistaken for work or reliance guidance, assurance shorthand, or release authority.

### E.17.ID.CR:3 - Forces

| Force | Tension |
| --- | --- |
| **Engineer-manager usability vs governance precision** | The pattern starts from a recognisable review situation without hiding its neighboring patterns. |
| **Middle-band reality** | Some bounded comparisons establish a contrast beyond a short F.9.1 stance note about an existing bounded-use claim without selecting an action. |
| **Source tether vs interpretive lift** | The comparison adds a bounded interpretation grounded in its sources. It cannot introduce a meaning independent of them. |
| **Comparison unit vs surrounding work** | The pattern keeps the comparative review unit, the bounded comparison, and the larger review process distinct even when the prose uses similar labels. |
| **Viewing restraint** | Interpretation does not absorb same-entity viewing, conservative rewriting, or representation-scheme transition whose main question is not bounded comparison. |
| **Bridge restraint** | Interpretation does not become a second bridge taxonomy. |
| **Explanation restraint** | The use of an existing explanation face remains governed by `E.17.EFP`. |
| **Abductive restraint** | Interpretation stops before an abductive-prompt or action-selection claim governs the next action. |
| **Ontology restraint** | Interpretation does not hide same-referent pressure, retargeted-EntityOfConcernRef pressure, or changed `EntityOfConcernRef`. |
| **Interpretant-side boundedness** | When reader fit affects the comparison, state the use it supports and its limits. Reader fit does not change the authority the comparison carries. |

### E.17.ID.CR:4 - Solution - comparative review units with bounded comparison, escalation, and boundary rules

#### E.17.ID.CR:4.1 - Ordinary comparative review-unit move

Make one bounded comparison from the claims the reviewed sources support. Start with the receiving review question, recover the relevant claims and conditions in each source, and derive the contrast on a common basis. A source-linked paragraph or small table can carry the result. Use the construction below when the comparison basis or contrast is not already established.

##### E.17.ID.CR:4.1.1 - Obtain the comparison from the available material

**Recover the question and its criterion.** Identify what the receiving review needs to distinguish and why: for example, the restoration time a release plan can guarantee, the populations covered by two studies, or the conditions under which two Methods can be used. Read the request, applicable requirement and surrounding review context for the object, situation and consequence that make a difference relevant.

Turn that difference into an answerable question about each source. If the purpose is only to compare the accounts, the criterion can concern their coverage or emphasis; state that subject. If a necessary priority or requirement is missing, ask the receiving reviewer which consequence or condition the comparison must resolve. Meanwhile retain any useful source contrast whose basis is already clear.

**Recover each source's answer.** Locate the passages bearing on that question, including definitions, qualifications and supporting results. For each alternative, recover what is asserted, about what, under which conditions and with what support. Keep the source return beside the extracted claim when it would otherwise be lost. Read enough surrounding argument to distinguish a stated result, an assumption, a proposed result and an unanswered question.

When a source is silent, report the missing coverage. Infer absence only when an explicit negative claim or a sufficiently complete account supports it.

**Establish the common basis.** Put the relevant claims together and ask whether the proposed predicate applies to both under compatible interpretations. A shorter reported time is comparable only after its event, unit, scope and status are understood: one observed duration, a mean and an upper bound answer different questions. A common topic does not make them interchangeable.

Recover a missing interpretation from the source's definitions or cited basis. Use the subject's comparison Method for the claim being compared: C.16 for measurement conditions, for example, or F.9 when a required semantic correspondence connects distinct local senses. If the correspondence or required fact remains unavailable, split the contrast into what each source establishes and state the exact missing basis for the stronger comparison. Different conditions can themselves be the useful contrast.

**Derive and bound the result.** State what follows from the aligned claims and show the reason that connects them. For textual emphasis, identify the content or allocation of discussion that warrants the contrast; this alone says nothing about the described alternatives' actual performance.

For a claim about the subject, preserve its applicable comparison rule and evidence. Distinguish a contrary result from insufficient support. Do not force a common ranking when the sources support different dimensions or incomparable conditions. A precise question such as “obtain B's restoration bound at production load L” is a usable return when that answer is necessary for the requested comparison.

**Publish for the receiving use.** Keep the sources, comparison basis, supported contrast and conditions needed to interpret it recoverable. Use an adjacent pair of passages, a paragraph or a table according to what the reader needs to inspect together. If the wording, arrangement or intended use could reasonably be taken as a stronger claim, state the limit on that stronger claim and the condition for reopening it. Apply the relevant neighboring Method when that stronger claim is requested.

**Worked construction.** A release brief asks whether a rollback plan can establish restoration within eight minutes at production load L. Note A states a ten-minute upper bound at L. Note B reports one six-minute rollback in staging at 0.2L. The reviewer first locates these passages and recovers the different status of the numbers: A gives a bound under the relevant load; B gives one observation under a smaller load. The shared question is the supported production restoration bound, not which displayed number is smaller.

The resulting note can say: “A establishes an upper bound of ten minutes at L; B reports six minutes once at 0.2L. Neither statement establishes the required eight-minute production bound. A may have a tighter supported bound; B needs support for a bound at L. These notes do not establish which rollback is faster in production.”

The comparison identifies the next inquiry: inspect A's bound derivation for an applicable tighter result, or obtain B's qualified bound at L from its validation or analysis. Select further testing only if the available support cannot answer the receiving question and that answer is still needed.

Now suppose B supplies a qualified seven-minute upper bound at L with the same restoration endpoint and applicable conditions. The comparison can establish that B supplies a bound meeting the eight-minute requirement while A's stated bound does not establish that fit. It still cannot infer that every B execution is faster than every A execution.

If B instead says nothing about restoration time, the result is a source-coverage gap. The same construction applies to non-numerical sources: align the claims and their conditions, then state only the contrast that those claims support.

In plain working terms, this pattern is for a review unit that says something like:
- `this option write-up foregrounds integration pressure more than that one`;
- `these two available source epistemes or source publications are useful together, but they are not yet equivalent`;
- `this dashboard view helps triage one contrastive question, but it is not yet a release decision or a root-cause claim`;
- `this research synthesis foregrounds uncertainty more than that one, but it is not yet a method choice`;
- `this program brief foregrounds continuity risk more than that one, but it is not yet a funding decision`.

If your review needs this kind of comparison, keep the ordinary minimum recoverable. If the first move is no longer bounded comparison over pinned sources, name the crossed claim and let its governing pattern carry that claim before this unit is used.

#### E.17.ID.CR:4.1.b - Compact placement

`ComparativeReviewUnit` governs this comparison within the wider `InterpretationDiscipline` naming family. The family name helps readers find the interpretation area; it does not govern the local claim. The local object is one comparative review unit carrying one bounded comparison, or a small set of bounded contrast rows, over already available source epistemes or source publications.

Use `E.17.ID.CR`, `ID.CR`, or `ComparativeReviewUnit` when this bounded comparison unit is the current object. Use the neighboring pattern when the crossed claim becomes primary.

#### E.17.ID.CR:4.1.c - Why the comparative-review-unit specialization needs its own discipline

Teams already produce small comparative review units, often as comparison notes, comparison sheets, or guided review aids, that add more interpretive lift than a short F.9.1 stance note about an existing bounded-use claim but still stop below action selection, ontology reframing, retargeting, or approval guidance.
Leaving that middle band unnamed creates two opposite failures: one reader dismisses the review unit as harmless prose, while another reads it as carrying substitution, action-selection pressure, or action authority.

This pattern gives teams a narrow way to prepare, share, and inspect that comparative review unit without implying a downstream claim or effect beyond what the source, bridge stance and bounded use support.

#### E.17.ID.CR:4.1.d - Local working vocabulary

This pattern uses a small local vocabulary for review.
- **Comparative review unit** = a lightweight review unit such as a short comparison note, small comparison sheet, guided review aid, or guided comparative UI whose stated purpose is one bounded comparison or a small set of bounded contrast rows under one shared review frame.
- **Base governing case** = the primary source relation, pattern-governing case, or project work question that already governs the review use before bounded comparison is added.
- **Reviewed source episteme or source publication** = an available source episteme or source publication under comparison, pinned or otherwise reviewable.
- **Source references** = `sourceAnchorSet` or `sourceRefs` that make the interpreted source episteme or source publication inspectable.
- **Shared review frame** = the review target, described situation, decision situation, release candidate, method family, control scope, problem frame, or source-set reference that remains preserved while the comparison is made.
- **Compared alternative** = one distinct option, method, bulletin, strategy, note, view, source episteme, source publication, or project-side FPF kind and reference named by value kept separate under the shared review frame.
- **Same `EntityOfConcernRef` case** = the special case where the compared sources describe the same entity. This is common, but it is not required when distinct alternatives remain under one shared review frame.
- **Interpretive lift** = the bounded contrast derived from available source claims; in a small comparison sheet, each row has its comparison criterion and material conditions under the shared review question.
- **Bridge references** = required `bridgeOccurrenceRef` and `boundedUseClaimRef` when the case depends on bridge-mediated correspondence rather than ordinary source interpretation alone. The use-claim reference resolves a claim whose `EntityOfConcern` is that Bridge occurrence and whose proposed use, direction, correspondence rule, tolerated loss, and polarity match this comparative unit. Optional `bridgeCardRef` cites reusable packaging, and optional `bridgeStanceRef` cites a separate F.9.1 episteme whose `EntityOfConcern` is the same bounded-use claim.
- **Bounded comparative use** = what this review unit can be used for while it remains only a bounded comparative review unit.
- **Overread risk** = how the review unit is most likely to be overread into a bridge, action-selection, ontology, or authority claim that it does not carry.
- **Prompt boundary** = the point at which an explanatory question with rival explanations still open becomes primary under `B.5.2.0` or `B.5.2`; `U.AbductivePrompt` classifies the published account of that initiating question under `B.5.2.0:4.2.1–4.2.2`.
- **Ordinary minimum block** = the smallest ordinary record that preserves what a reviewer needs to use the comparison within its bounds.
- **Load-bearing extension** = the fuller declaration record used when the case sits close to bridge, explanation, abductive, ontology, or authority boundaries.

These terms are local review fields for completing the comparative review unit. They keep source references, shared review frame, compared alternatives, bounded lift, blocked downstream claim or effect, and boundary trigger readable in the review unit.
When one of those fields starts carrying a bridge, evidence, gate, speech-act, commitment, work, authority, publication-face, or project-side FPF claim, name that crossed claim and use the governing pattern for it.

#### E.17.ID.CR:4.2 - Scope and exclusions

**In scope**
- bounded comparative asymmetry over already declared reviewed source epistemes or source publications;
- reader-facing interpretive caution that stays source-tethered and preserves the shared review frame;
- comparison of distinct alternatives under one shared review target, described situation, release candidate, method family, control scope, problem frame, or source-set reference;
- comparative review units that answer one explicit contrastive question without creating a rival action-selection search;
- bounded user-fit when that fit only limits use rather than widening authority.

**Out of scope**
- same-entity restatement, conservative rewrite, or representation shift whose main question stays with `A.6.3`, `A.6.3.CR`, or `A.6.3.RT`;
- a separate F.9.1 stance note that only clarifies an already constituted F.9 bounded-use claim;
- explanation-face use discipline, bounded-use boundary, or added-link review on existing faces (`E.17.EFP`);
- explanatory questions with rival explanations open (`B.5.2.0` or `B.5.2`), and choice among already available actions, probes, or method options (`C.11`);
- ontology-facing reframing or changed EntityOfConcern (`OntologicalReframing` or `A.6.4`);
- policy, gate, adjudication, assurance, or work-facing use (name the claim and use its governing pattern; see `E.17.ID.CR:4.5`).

#### E.17.ID.CR:4.2.a - Working-fit test

Use this discipline only when all of the following hold:
1. the reviewed source episteme or source publication is already pinned or otherwise reviewable;
2. the review unit adds one bounded comparative or interpretive lift, or a small set of bounded contrast rows with row-level comparison criteria;
3. the case is still answering a bounded contrastive question rather than selecting an action;
4. the shared review frame stays preserved, and compared alternatives remain distinct unless an explicit bridge or substitution source supplies equivalence, substitution, or another named relation between them;
5. the main question is not already better described as same-entity viewing, an F.9.1 stance note about an existing bounded-use claim, or explanation-face use discipline.

If any of those fail, handle the current work under the neighboring FPF pattern and project-side FPF kind and reference named by value that govern it.

#### E.17.ID.CR:4.2.b - Nearest neighboring work

Name the base source relation or work question before adding bounded comparison. If the current question is already source transformation, bridge, explanation-face use, prompt or action selection, ontology or changed `EntityOfConcern`, decision, work or reliance, gate, assurance, adjudication, or reduced-use source rendering, do not stretch `ComparativeReviewUnit` to carry it. Use the compact boundary map in `E.17.ID.CR:4.5` and the governing pattern for the crossed claim.

#### E.17.ID.CR:4.3 - Working-model first; plain questions first, ordinary minimum second, full declaration third

Most users can start with the questions below.
Following `E.14`'s working-model-first discipline, the questions help an engineer-manager keep the comparison within the work it supports.
The ordinary minimum block states the content needed for ordinary use; the card is one way to recover and arrange it.
The fuller declaration block remains available as a reviewable declaration extension that carries source, boundary, and downstream-claim fields by value. If an assurance or B.3 threshold applies, cite the separately constituted B.3 claim or record. The declaration extension cannot serve as that assurance record.

#### E.17.ID.CR:4.3.a - Five plain working questions

The near-top working-fit check selects the comparison task. Use these questions to recover its result:
1. Which available sources and alternatives answer the receiving review question?
2. Which claims, conditions and supporting passages in each source bear on it?
3. On what criterion can those claims be compared, and what does the comparison establish?
4. What necessary interpretation or fact remains unavailable, and where can it be obtained?
5. Does the present wording or receiving use imply a stronger claim whose grounds must be supplied?

Use :4.1.1 to obtain a missing comparison basis or contrast. Repair an ambiguous local expression under E.17.AUD.LHR when wording is the obstacle; use E.17.AUD.OOTD when the unit's primary subject or move remains unstable. Missing subject evidence remains a substantive gap.

#### E.17.ID.CR:4.3.b - Ordinary minimum block

For an ordinary bounded comparison, keep recoverable:
- the reviewed sources and passages carrying the relevant claims;
- the shared question, distinct alternatives and comparison criterion;
- the supported contrast and conditions needed to interpret it; and
- any unresolved basis that limits the requested result.

Add a downstream-use limit and its governing pattern when the wording, representation, receiving use or applicable authority rule gives rise to a stronger reading than the comparison supports. Preserve a required contractual form and the grounds of any actual equivalence, causal, choice, gate or authority claim.

Stop if the same note, sheet or review aid cannot keep those minimum answers stable because it confuses reviewed source episteme or source publication, bounded comparative review unit, bounded lift, and outside work. Repair local lexical-head kind pressure through `E.17.AUD.LHR` (`Local Head Restoration`). If the whole review unit still has unstable primary-subject identification (including the carried EntityOfConcern when applicable) or carried-move identification after that repair, apply `E.17.AUD.OOTD` (`PublicationUnit Primary-Subject Discipline`) before adding more declaration weight.

##### E.17.ID.CR:4.3.b.a - Ordinary working card

An ordinary comparative review unit keeps the applicable content below recoverable. Use these rows when their arrangement helps:

| Row | Plain question | Minimum answer |
| --- | --- | --- |
| **Reviewed source** | What already available source epistemes or source publications are being compared? | one pinned source slice, one explicit source pair, or one explicit source set |
| **Source references** | Where can a reviewer inspect that source episteme or source publication? | visible `sourceAnchorSet` or nearby `sourceRefs` |
| **Shared review frame and alternative identities** | What review target, described situation, or source-set reference is preserved, and what alternatives remain distinct under it? | preserved shared review frame; equivalence or substitution requires its applicable direct relation, with F.9 additionally governing any required cross-context semantic correspondence |
| **Bounded lift row(s)** | What contrast follows from the source claims? | the comparison basis, supported contrast and material conditions obtained through :4.1.1 |
| **Downstream-use limit, when needed** | What stronger reading is plausible here but unsupported? | the limit on that use, such as an unestablished equivalence or approval |
| **World-contact limit, when needed** | Does the receiving use require an explicit limit on action or reliance? | the applicable limit and its basis |
| **Boundary trigger, when needed** | What changed claim or condition requires further work? | the condition and the governing Method |

The working card may appear inline or in the immediate review context. Retain a card or table when its arrangement supports comparison or independent revision of contrast rows. Keep any form a receiving contract requires. When the unit travels separately, carry the interpretation and source return needed for that use.
Use these questions as the ordinary recovery reference for the near-top working-fit check:
- if rows 1-4 are still unstable because one local head word or qualifier has to carry too much of the meaning, stop and repair the wording through `E.17.AUD.LHR` (`Local Head Restoration`) before continuing to build the comparative review unit here;
- if the applicable content in rows 3-7 cannot stay stable because the same review unit still has unstable reviewed-source, comparative-move identification, or outside-work boundary after a local wording repair, apply `E.17.AUD.OOTD` (`PublicationUnit Primary-Subject Discipline`);
- if the applicable rows stay recoverable over one pinned source slice or source pair, one preserved shared review frame, distinct alternatives where present, and one bounded contrast or small row set, `ComparativeReviewUnit` remains the primary governing pattern.

The nearest stay-here worked slices for this pattern are `E.17.ID.CR:5.4.5` through `E.17.ID.CR:5.4.6.b`.
The nearest stop-and-reopen worked slice is `E.17.ID.CR:5.4.6.c`.

Use the fuller declaration extension only when one of the boundary, reader-fit, or misuse conditions in `E.17.ID.CR:4.3.c` becomes true.
`ComparativeReviewUnit` remains primary only while the ordinary minimum stays recoverable and the same review unit is still mainly about one bounded comparison, or a small set of bounded contrast rows, over already pinned source epistemes or source publications.

If the first question is what the review unit is about, what move it carries, and what wider work remains outside, use `E.17.AUD.OOTD` (`PublicationUnit Primary-Subject Discipline`) to stabilize that `PublicationUnit` question before extending the declaration.

#### E.17.ID.CR:4.3.c - Fuller Declaration Extension Guidance

A fuller declaration record becomes warranted only when a local condition changes the first action: reader fit changes how the comparison can be used, overread risk is high, a mixed case depends on `A.6.3.*` or `E.17.EFP`, or a bridge-mediated relation is live. Resolve remaining subject or move instability through `E.17.AUD.OOTD` before choosing the declaration weight, as below.

The fuller declaration extension can inherit already-declared case ids, source pins, and provenance references instead of restating them inline. When recorded as a claim-bearing review unit, that extension normally captures the ordinary minimum block plus only the neighboring-pattern fields that govern the mixed case.

Do not answer `PublicationUnit` instability by stacking more local fields onto the fuller declaration extension. If `E.17.AUD.LHR` (`Local Head Restoration`) has already repaired the local lexical-head pressure and the same review unit still has unstable reviewed-source, publication-unit, comparative-move identification, or outside-work boundary, stabilize that `PublicationUnit` question with `E.17.AUD.OOTD` (`PublicationUnit Primary-Subject Discipline`) before deciding how much declaration weight stays here.

#### E.17.ID.CR:4.3.d - Fuller Declaration Block
When the fuller declaration is warranted, make at least these fields recoverable:
- `sourceRelationClass` using the shared `E.17:5.1b` vocabulary when the comparison depends on source pointer, source availability or retrieval, source use, source faithfulness, claim recoverability, contradiction, omission, claim widening, added linkage, independent verification, bounded use, forbidden downstream use, or reopen trigger;
- `sourceAnchorSet` or `sourceRefs`;
- `comparativeRelationClass = sameEntityComparisonClass | sharedFrameDistinctAlternativeClass | readerFitComparativeClass`;
- `comparisonBasis`;
- `addedClaimPolicy`;
- required `bridgeOccurrenceRef` and `boundedUseClaimRef` when the case depends on bridge-mediated comparative relation; the use-claim reference resolves a claim whose `EntityOfConcern` is that Bridge occurrence and whose proposed use, direction, correspondence rule, tolerated loss, and polarity match the current comparative unit;
- optional `bridgeCardRef` when a reusable Card exists;
- optional `bridgeStanceRef` when it resolves the separate F.9.1 episteme whose `EntityOfConcern` is that use claim;
- `targetUserModel` when reader-fit is materially shaping the comparison unit;
- `interactionMode` when the review unit is not limited to a single static comparative sentence;
- `contrastiveQuestion` when the case answers a contrastive question;
- `boundedComparativeUse`;
- `overreadRisk`;
- `promptWorthinessThreshold`;
- `ontologyBoundaryTrigger`;
- `worldContactPolicy`;
- `downstreamAuthorityLimit`;
- `baseCasePattern` when the review unit is a mixed case layered over `A.6.3.*` or `E.17.EFP`.

`sourceRelationClass` classifies only the source relation or bounded claim for the local claim or use. `comparativeRelationClass` classifies only the comparative relation of this review unit. Neither field is a neighboring object or claim such as a relation kind, Bridge occurrence, bounded-use claim, Card, stance note, semantic identity, evidence relation, gate, assurance, work relation, speech act, commitment, authority reference, or decision record.

The `sameEntityComparisonClass` value is a special case for comparisons where the compared sources describe the same entity; it does not assert semantic identity. When the unit compares distinct alternatives, use `sharedFrameDistinctAlternativeClass` plus distinct alternative refs. Equivalence or substitution requires its applicable direct relation. When that use depends on correspondence between local senses from different semantic contexts, also establish the F.9 Bridge and its required bounded-use claim.
`readerFitComparativeClass` by itself does not create an interpretation claim. When bounded correspondence wording implies a cross-context Bridge, first apply F.9. The `boundedUseClaimRef` must resolve a claim whose `EntityOfConcern` is the `bridgeOccurrenceRef`, and its proposed use, direction, correspondence rule, tolerated loss, and polarity must match this comparative unit.

A positive proposed use requires affirmative polarity; when A.10 or B.3 is triggered, current reliance must support that use. A degraded reliance result narrows the use. Negative, abstaining, reopened, evidence-needed, blocked, or mismatched results stop this bridge-mediated use.

The pattern that directly constrains the proposed comparison decides authorization, and evidence of the comparative-review Work says whether it occurred.

A `bridgeCardRef` remains optional packaging. A `bridgeStanceRef` is also optional and is admissible only when it resolves a separate F.9.1 episteme whose `EntityOfConcern` is that same bounded-use claim. None of these references can substitute for another.
Use the main comparison question and the neighboring patterns’ boundaries to select the FPF pattern or project-side FPF kind and reference by value.

#### E.17.ID.CR:4.3.e - Interpretant-side block

The interpretant-side fields describe how reader fit affects this comparison. They do not specify a full interactive explanation or dialog-management system.
Use them to:
- identify how the comparison depends on its audience when it does;
- make the contrastive question, guided review mode, and bounded use visible;
- prevent comparison prose from implying prompt-bearing guidance, assurance or policy pressure.

#### E.17.ID.CR:4.3.f - Static note versus interactive aid

Use two comparison-relation forms.

1. **Static comparative review note.** A static note needs its sources, comparison criterion, supported contrast and material conditions. Use the `E.17:5.1b` source-relation class when that relation is disputed, and an explicit downstream-use limit or boundary trigger when the current use requires it.
2. **Interactive comparative aid.** Add `targetUserModel`, `interactionMode`, state or history needed for the comparison claim, `overreadRisk`, and bounded-use boundary only when the aid is interactive, stateful, adaptive, or user-model-bearing. These fields keep the interactive comparative aid from being mistaken for audience-neutral static prose; they do not carry a crossed claim.

A comparative review unit can expose or cite the source epistemes, source publications, or project-side FPF references being compared, but layout, fluent contrast, side-by-side placement, or guided-review reuse does not change the kind of the unit or create a stronger source relation.

If the required source relation is missing, the repair request or source-gap note is prospective only; it does not backdate a source relation into the earlier comparison.

**Comparative-review-unit identity over revision.** A revised comparison table, regenerated comparison note, or updated guided review aid is not the same bounded comparison merely because the layout, title, or compared-source family stayed familiar.

If new source input, revised source references, changed comparison criterion, changed shared review frame, or a change in the blocked downstream claim or effect changes the comparison identity or downstream use, publish the preserved comparative frame and the changed claims, or treat the result as a new comparative review unit before using it for a stronger crossed claim.

#### E.17.ID.CR:4.3.g - Representation ontology and modeling lens (informative)

This pattern does not model interpretation in general.
It models one comparative review unit governed by `ComparativeReviewUnit` within the broader `InterpretationDiscipline` family.
In each case, the object under review is the comparison unit.
That unit can appear as a comparison note, comparison sheet, or guided review aid, but it is not the whole review process or the source system.
The bounded comparison is the interpretive lift carried by that review unit.

The minimum typed lens is a compact record of:
- source references and source relation;
- one declared source-relation class;
- one declared comparison criterion and added-claim policy;
- one bounded-use boundary, one overread-risk line, and one `worldContactPolicy` that remains subordinate to the pattern governing a gate or adjudication claim; `A.21` governs a named gate decision under its applicable profile, while `A.20` applies only to a named internal-constraint check in a transformation-flow case;
- the relevant prompt, ontology, and authority boundary triggers;
- and which neighboring pattern still governs the base case when this remains a mixed overlay.

The lens keeps attention on the review unit and the problem-owning review domain, while the pattern governing the base case retains responsibility for source, continuity and boundary conditions.

#### E.17.ID.CR:4.3.h - Working read-out

A working reader can usually say, in one short paragraph:
- what reviewed source episteme or source publication is being comparatively read;
- what bounded interpretive lift is being added;
- what shared review frame remains preserved, and, in the special same-EntityOfConcern case, why the same `EntityOfConcernRef` remains preserved;
- which crossed claim is still outside this pattern and which neighboring pattern would govern that claim if it became primary;
- and which boundary condition shows that the primary claim is no longer a bounded `ComparativeReviewUnit` claim.

If the reader cannot give that account clearly, the review unit is no longer bounded enough to stay here; narrow it, clarify it, or make the governing neighboring pattern primary for the crossed claim.

#### E.17.ID.CR:4.4 - Branch-discipline summary

This section is the compact governing-rule summary for `ComparativeReviewUnit` inside the Core. Use the fuller solution, boundary table, worked slices, and relations section here only when you need the wording of a clause, the full field set, or the full reopen conditions.

1. **Preserve the shared review frame.**
   Keep the reviewed source episteme or source publication set, source references, declared comparison criterion, and distinct alternative identities visible. State `contrastiveQuestion` when the review depends on it.
2. **Keep the lift bounded and comparative.**
   The review unit can add one bounded comparative or asymmetry-bearing lift. It stops when that lift starts carrying a stronger crossed claim.
3. **Name the crossed claim instead of repeating exclusions.**
   When the case stops being bounded comparison, name the claim that crossed the boundary and apply the pattern that governs it; use `E.17.ID.CR:4.5` to identify the relevant boundary.
4. **Keep neighboring-pattern authority explicit.**
   Bridge-mediated comparison requires a `bridgeOccurrenceRef` and a tuple-matched `boundedUseClaimRef` whose `EntityOfConcern` is that Bridge.

   Positive use requires affirmative polarity and, when A.10 or B.3 is triggered, current reliance for that use. Degraded reliance narrows the use; a negative, abstaining, reopened, evidence-needed, blocked, or mismatched result stops it.

   A Card and F.9.1 stance note remain optional and separate. Authorization and evidence that comparative-review Work occurred remain with their own patterns and records.
5. **Keep reader-fit bounded.**
   `targetUserModel`, `interactionMode`, `contrastiveQuestion`, `boundedComparativeUse`, and `overreadRisk` can be stated when they change how the comparison is used, but these fields cannot confer authority.

#### E.17.ID.CR:4.5 - Neighboring-work boundary glance

Use this table to distinguish the comparison from neighboring project work and identify the source requirements for each claim.
For a fuller reading of a mixed case, read the applicable neighboring pattern with its row.

| When the case concerns… | Governing pattern or bounded disposition |
| --- | --- |
| one local lexical head or qualifier is still doing too much work, but a local wording repair would stabilize the same unit | `E.17.AUD.LHR` (`Local Head Restoration`) |
| the same note is mostly rewriting, reframing, or re-rendering the same EntityOfConcern with no bounded comparative lift | `A.6.3`, `A.6.3.CR`, or `A.6.3.RT` |
| the task is only to add a short reading note about an already constituted F.9 bounded-use claim | `F.9.1`; a Card is optional packaging |
| the comparison wording is now making a relation-precision claim between compared items | `A.6.P` |
| the comparison wording is now making sameness, equivalence, alignment, mapping, substitution, or a cross-context Bridge claim | `A.6.9` recovers the concrete predicate and its subject pattern. Use F.9 for an actual cross-context semantic correspondence and its bounded-use claim; F.9.1 supplies only an optional stance note about that claim. |
| the note is primarily a reduced-use source-pinned rendering with narrower-use, blocked downstream use, and source-bearing reopen discipline | `A.6.3.CSC Controlled Semantic Coarsening` |
| one review unit already keeps the same primary entity of concern, one bounded comparison, and one outside-work boundary stable | `ComparativeReviewUnit` within `InterpretationDiscipline` |
| the same unit still has unstable reviewed-source, comparative-move identification, or outside-work boundary after local repair | `E.17.AUD.OOTD` (`PublicationUnit Primary-Subject Discipline`) |
| the task is to govern explanation use on existing faces | `E.17.EFP` |
| the comparison raises an explanatory question with rival explanations still open | `B.5.2.0` or `B.5.2` |
| the target or ontology is changing and now needs continuity witnesses | `OntologicalReframing` or `A.6.4` |
| the unit is now used to choose among already available actions, probes, or method options, or to publish the resulting decision record | `C.11` |
| the unit is now being used for execution, gate, or adjudication consequence | `A.15` for System-Role–Method–Work alignment, `A.15.1` for dated `U.Work`, and `A.21` for a named gate decision under its applicable profile; `A.20` only for a named internal-constraint check in a transformation-flow case; adjudication stays with its defining policy or pattern |

For first-minute use, the following four boundaries summarize the rows around the comparison case. Use them with the near-top working-fit check and the ordinary working card:
- pressured local lexical head -> `E.17.AUD.LHR` (`Local Head Restoration`);
- stable same-object comparative review unit -> stay with `ComparativeReviewUnit`;
- same unit still unstable after local repair -> `E.17.AUD.OOTD` (`PublicationUnit Primary-Subject Discipline`);
- any stronger crossed claim already primary -> the governing pattern for that claim is primary.

If the comparison unit is already carrying neighboring work, use the boundary rows first and then read `E.17.ID.CR:5.4.7` through `E.17.ID.CR:5.4.10` as the nearest worked boundary examples.

#### E.17.ID.CR:4.5.a - Ordinary working order

The ordinary working order is to recover the receiving question, inspect the relevant source claims, establish their comparison basis and derive the bounded contrast as explained in :4.1.1. Publish that result with its source return and material conditions. Add a downstream limit or neighboring Method only when the current claim or receiving use requires it.

If the result cannot yet be obtained, return the missing source, interpretation, criterion or fact and the attainable inquiry that could settle it. Use E.17.AUD.LHR or E.17.AUD.OOTD when the obstacle is respectively local wording or unstable primary-subject or move identification; those repairs do not supply missing subject evidence.

### E.17.ID.CR:5 - Archetypal grounding

**Worked-slice note.** The system case, episteme case and worked boundary examples cover different situations. Choose the example that fits the case; their order does not prescribe a progression.
They show different bounded outcomes for the same governing pattern: some comparisons stay small and stop, some also need a neighboring pattern, and others reopen or need another governing pattern when new observations from outside the review, environmental changes or downstream constraints change what the comparison can support.

Make the ordinary minimum recoverable for the current comparison unit; if the boundary trigger fires, stop here or apply the governing pattern for the crossed claim.

#### E.17.ID.CR:5.1 - One comparison unit

`ComparativeReviewUnit` applies when a team prepares one stated, bounded comparison over source epistemes or source publications with already declared references, while any stronger crossed claim remains outside until the governing pattern for that claim is named.
Keep the unit small enough for a reviewer to recover the shared review frame, the same `EntityOfConcernRef` when the compared sources describe the same entity, the declared comparison criterion, the blocked downstream claim or effect, and the boundary trigger that would end interpretation.

#### E.17.ID.CR:5.2 - Same service episode

**Source slice.** Two pinned operating notes describe the same service episode from different operational responsibilities.
One note has its source reference in the maintenance log, the other in the continuity dashboard for the same declared episode and the same `EntityOfConcernRef`.

**Comparative review unit.** `Under the declared comparison criterion, the maintenance note foregrounds operator-induced variance, while the continuity note foregrounds buffer-sensitive drift; each view exposes a blind spot in the other without granting direct substitution.`

**Why this stays here.**
- source relation and source references are explicit;
- the same `EntityOfConcernRef` remains preserved;
- one bounded comparative lift is added;
- no substitution licence is added;
- no rival action-selection question is yet being asked.

#### E.17.ID.CR:5.3 - Two analytic renderings

**Source slice.** Two pinned analytic renderings over the same evidence set are already available for review.
One rendering is a `SourceLinkedExplanationReconstruction` on a `TechCard` face; the other is a compact comparison sheet that preserves the same evidence set and the same described operational episode.

**Comparative review unit.** `For maintenance reviewers, the reconstruction foregrounds operator load more than the comparison sheet, while the comparison sheet foregrounds recovery sequencing more than the reconstruction; this difference is useful for review, but it is not yet a design recommendation or an action-selection claim.`

**Why this stays here.**
- the base-case governing patterns remain identifiable;
- the comparative lift is explicit and bounded to one reviewer task;
- explanation-face governance and same-entity transform discipline remain with their neighboring patterns;
- explanatory questions, action selection, and authority-bearing use remain governed by their respective neighboring patterns.

#### E.17.ID.CR:5.4 - Worked boundary examples

##### E.17.ID.CR:5.4.1 - Lower-boundary stance-note case

**Stance-note unit.** `F.9 already records an obtaining Bridge and a bounded-use claim for reading the local maintenance-pressure term alongside the partner continuity term. This separate note says that, for that use, the relation is best read as asymmetry-explicating rather than substitution-friendly.`

Why it stays under `F.9.1`:

- the Bridge and bounded-use claim already exist;
- the note only makes the claim easier to read; and
- no bounded comparative lift beyond that stance note is added.

##### E.17.ID.CR:5.4.2 - Mixed primary-pattern composition with `A.6.3.RT`

**Base-case rendering.** A same-entity comparison sheet retabulates one pinned incident note into columns for trigger, pressure, and recovery.

**Comparative review unit.** `In the retabulated view, the recovery column makes the operator-induced asymmetry easier to inspect than the trigger column, but the table is not treated as establishing a new causal hierarchy.`

Why the case uses both patterns:
- `A.6.3.RT` still governs the base representation shift;
- bounded comparison is secondary and adds only the bounded contrast;
- most restrictive forbidden-use constraint wins, so no new ontology or gate claim is licensed.

##### E.17.ID.CR:5.4.3 - Mixed primary-pattern composition with `E.17.EFP`

**Base-case rendering.** A `TechCard`-face explanation rendering is already classified as `SourceLinkedExplanationReconstruction` and publishes a bounded connective policy.

**Comparative review unit.** `For maintenance reviewers, this rendering foregrounds the difference between operator load and throughput pressure more than the original prose, but it is not treated as a design-level recommendation.`

Why the case uses both patterns:
- `E.17.EFP` still governs explanation class and face bounded use;
- bounded comparison adds only bounded comparative use for one reviewer task;
- `E.17.EFP` still governs explanation-face use; any authority-bearing use must name its governing pattern.

##### E.17.ID.CR:5.4.4 - Guided review aid with bounded interaction mode

**Source slice.** A reviewer UI presents two pinned source notes side by side for the same described operational episode.

**Guided comparative review unit.** `Question: which note foregrounds variance introduced by operator timing rather than environmental drift? Bounded comparative use: bounded comparative triage only. Misuse risk: do not treat this aid as action selection or release guidance.`

Why it stays here:
- the interaction mode is explicit but still bounded;
- the review unit answers one contrastive question without initiating work on an explanatory prompt or action choice;
- bounded use and overread risk are stated in the aid instead of being implied by its tone.

##### E.17.ID.CR:5.4.5 - Product and design-review comparison case

**Source slice.** Two available design-review notes concern the same integration boundary and planned release. The release meeting needs to know what each note establishes about rollback and implementation effort.
Note A states: `Rollback uses the existing adapter, which must first be modified. No implementation-effort estimate is available.` Note B states: `Implementation uses one interface and is estimated at two engineer-days. Rollback has not been assessed.`

**Comparative review unit.** `For release review, A describes a rollback path conditional on modifying the adapter, while B leaves rollback unassessed. B supplies a two-engineer-day implementation estimate; A supplies no estimate. These source statements do not establish which option has lower total effort or risk. If the next decision needs that comparison, obtain the missing estimates and rollback assessment on a compatible basis.`

**Working-boundary use.** The shared review frame, bounded contrast and boundary with outside work are all explicit. The comparison therefore remains primary.

Why it stays here:
- the same planned release remains the `EntityOfConcernRef`;
- one bounded comparative lift is made explicit for a declared review task;
- the unit helps design discussion without selecting an action or granting approval.

##### E.17.ID.CR:5.4.6 - Compliance and release-review comparison case

**Source slice.** An internal control checklist and a vendor compliance bulletin are already available for the same release candidate and the same declared control scope.

**Comparative review unit.** `For release review, the vendor bulletin foregrounds protocol conformance more than rollback evidence, while the internal checklist foregrounds rollback evidence more than protocol conformance; this comparison helps frame the review, but it is not yet a release gate or equivalence claim.`

**Working-boundary use.** Under release or compliance pressure the comparison unit remains stable. The review concerns its bounded contrast, with no need for local wording repair or `PublicationUnit` stabilization.

Why it stays here:
- the comparison criterion is explicit and bounded to one review task;
- the source references remain visible and the same release candidate stays in view;
- the review unit helps an engineer-manager see the difference in emphasis without giving the comparison authority over the release gate.

##### E.17.ID.CR:5.4.6.a - Research-review comparison case

**Source slice.** Two already available research syntheses discuss the same measured phenomenon and the same declared evidence slice.
One synthesis foregrounds variance decomposition limits more; the other foregrounds protocol repeatability more.

**Comparative review unit.** `For method review, the first synthesis foregrounds variance decomposition limits more than the second, while the second foregrounds protocol repeatability more than the first; this asymmetry helps frame the discussion, but it is not yet a method choice or a claim that one synthesis is globally better.`

Why it stays here:
- the same measured phenomenon remains the `EntityOfConcernRef`;
- the comparative lift is bounded to one review task;
- the unit helps research discussion without selecting an action or reframing the ontology.

##### E.17.ID.CR:5.4.6.b - Program and cultural-review comparison case

**Source slice.** Two already available programme briefs discuss the same continuing initiative and the same declared participation scope.
One foregrounds continuity of community engagement more; the other foregrounds short-term event visibility more.

**Comparative review unit.** `For programme review, the first brief foregrounds participation continuity more than the second, while the second foregrounds short-term visibility more than the first; this comparison helps frame the discussion, but it is not yet a funding, curation, or programme-direction decision.`

Why it stays here:
- the same initiative remains the `EntityOfConcernRef`;
- the comparison criterion is explicit for one declared review task;
- the unit helps programme discussion without giving the comparison authority to decide.

##### E.17.ID.CR:5.4.6.c - Exogenous-change stop-and-reopen case

**Source slice.** An internal release-review comparison sheet already compares one control checklist and one vendor bulletin for the same declared release candidate and the same control scope.
Mid-review, an external incident bulletin arrives and changes the rollback assumptions governing use of that same candidate.

**Initial comparative review unit.** `Before the new bulletin, the vendor bulletin foregrounds protocol conformance more than rollback evidence, while the internal checklist foregrounds rollback evidence more than protocol conformance; this comparison frames the review, but it is not yet a release gate or equivalence claim.`

**Working-boundary follow-through.** The initial comparison fits `E.17.ID.CR:5.4.6`, but the new observation changes its declared criterion. Stop and reopen the unit.

**Why this stops and reopens.**
- the new outside observation changes the declared comparison criterion;
- the previous bounded comparison can remain traceable, but it cannot be used unchanged under the new review conditions;
- the bounded next use is either to restate a fresh comparative review unit over the new declared criterion or to apply a neighboring governing pattern if downstream gate or authority question has now become primary.

##### E.17.ID.CR:5.4.6.d - Lighter comparison note with source-return discipline

**Source episteme and source publication set.** A release team already has the full internal rollback worksheet, vendor bulletin, and incident-note bundle for one release candidate. A short comparison note is then prepared for the daily review stand-up.

**Comparative review unit.** `For today's review, the vendor bulletin foregrounds protocol conformance more than rollback evidence, while the internal rollback worksheet foregrounds rollback evidence more than protocol conformance; this short note is only a review aid over the same release candidate, and the full source episteme or source publication set remains primary for any bridge, release, coarsening, or work or reliance claim.`

Why it still stays here:
- the comparison unit is still one bounded comparative review unit, not a replacement for the source episteme or source publication set;
- the note remains source-pinned through the already available source episteme or source publication set, and bridge, gate, or work or reliance use remains with the governing pattern for that claim;
- any attempt to treat the short note as enough for equivalence, release approval, execution claim or effect, or a reduced-use source substitute requires source-bearing return, `A.6.3.CSC Controlled Semantic Coarsening`, or another neighboring pattern.

##### E.17.ID.CR:5.4.6.e - Functional versus constructive-description comparison

**Source slice.** A functional-description publication and a constructive publication or product-description publication describe the same pumping skid. The functional description foregrounds flow relation and method-selection relation; the constructive description foregrounds module composition and installed equipment.

**Comparative review unit.** `For design review, the functional description foregrounds what the skid is supposed to do in the declared flow relation, while the constructive description foregrounds what parts are present. This contrast helps the engineer keep function and construction separate, but it is not a module-equivalence claim, a performed-work record, or a gate decision.`

Why it stays here:
- both source publications keep source references and remain inspectable;
- the same pumping skid remains the `EntityOfConcernRef`;
- the bounded comparative lift is the function-versus-construction contrast for one review task;
- module equivalence, work occurrence, evidence, and gate claims remain blocked downstream uses.

##### E.17.ID.CR:5.4.6.f - Method-option comparison without method choice

**Source slice.** Two method descriptions are already pinned for the same fabrication task. One foregrounds lower setup cost; the other foregrounds tighter result-measurement discipline.

**Comparative review unit.** `For method review, the description of method M-1 foregrounds lower setup cost more, while the description of method M-2 foregrounds tighter result-measurement discipline more. This comparison helps prepare method discussion; method choice, a work plan, and evidence that either method has been performed remain outside it.`

Why it stays here:
- the reviewed source epistemes are pinned;
- the comparison criterion is explicit;
- no selected-method, work-plan, performed-work, evidence, or engineering-justification claim is added;
- if the team chooses a method or prepares a work plan, record the selected method as project `U.Method`, record the work plan as `U.WorkPlan` under `A.15.2`, and use `A.15.1` only when a dated `U.Work` occurrence is the governed occurrence claim.

**Nearest neighboring-work examples.** Use the next four cases to recognize prompt pressure, same-entity viewing, ontology shift, and gate or authority misuse when the boundary rows near the beginning point beyond the comparison.

##### E.17.ID.CR:5.4.7 - Upper-boundary prompt-bearing case

**Prompt-bearing review unit.** "This contrast raises the question whether both systems are being constrained by the same hidden gating variable, so we normally publish a U.AbductivePrompt around that shared control possibility."

Why `ComparativeReviewUnit` no longer governs:
- an explanatory question with rival explanations still open governs the next action;
- the review unit is now prompt-bearing rather than only interpretive;
- the selected governing pattern is `B.5.2.0` or `B.5.2` through explicit `U.AbductivePrompt` publication.

##### E.17.ID.CR:5.4.8 - Same-entity viewing boundary case

**Viewing rendering.** `The source note is retabulated into a compact comparison sheet that preserves the same claims and entity but makes pressure, trigger, and recovery fields easier to inspect.`

Why it does not enter interpretation:
- the main question is representational reshaping rather than bounded comparison;
- no bounded asymmetry or interpretive claim is added;
- the more precise governing pattern is `A.6.3.RT`.

##### E.17.ID.CR:5.4.9 - Ontology-boundary anti-case

**Ontology-pressuring review unit.** `The older maintenance note and the new field-observation note are best treated as two observational cuts over the same latent failure mode, so we normally recast both under a new operational kind and treat the source labels as legacy labels.`

Why `ComparativeReviewUnit` no longer governs:
- the case is now asking for a same-referent interpretation with continuity-witness demand or retargeted-EntityOfConcernRef interpretation;
- continuity witnesses would now be needed;
- bounded comparative interpretation is no longer enough, so the case applies `OntologicalReframing`.

##### E.17.ID.CR:5.4.10 - Authority and gate misuse anti-case

**Authority-pressuring review unit.** `Because this comparison consistently foregrounds the safer operating condition, reviewers can use the review unit as a release gate and do not need the underlying source episteme or source publication during triage.`

Why `ComparativeReviewUnit` no longer governs:
- the review unit is being overread as gate-facing authority;
- the bounded comparison has become a substitute for the source episteme or source publication;
- the release-gate claim is governed by `A.21` and the applicable release policy; use `A.20` only for an internal-constraint check that meets its transformation-flow conditions.

##### E.17.ID.CR:5.4.11 - Invalid publication and repair example

**Source slice.** Source note SN-12 and receiving note RN-12 use maintenance terms from different local semantic contexts.

**Invalid review unit.** `These two views describe the same entity for current operations, so the team can use whichever wording is easier.`

Why it is invalid here:
- no source references are visible;
- bridge-mediated comparison is being implied without identifying an obtaining Bridge and its bounded-use claim;
- the invitation to use either wording implies substitution and authority that the comparison does not establish.

**Minimal repair.** `Under Bridge B-12 between the local senses pinned by SN-12 and RN-12, bounded-use claim UC-12 has B-12 as its EntityOfConcern and says, with affirmative polarity, that the SN-12-to-RN-12 direction is suitable for comparing only the operator-timing concern in this review task; the remaining source distinctions are tolerated loss, not substitution. A current A.10 result supports relying on UC-12 for that use. Both notes foreground the concern, but they are not substitution-equivalent and the source episteme or source publication set remains primary. The pattern for the proposed review decides authorization, and evidence of the review Work says whether it occurred. Card BC-12 may be cited when that optional package is useful.`

What the repair does:
- restores the source references and verifies `bridgeOccurrenceRef`, the bounded-use claim's `EntityOfConcern`, its use/direction/rule/loss/polarity tuple, and current A.10 reliance for that positive use, while keeping any `bridgeCardRef` optional;
- narrows the claim back to bounded comparison and leaves authorization and the occurrence of comparative-review Work to their own patterns and evidence;
- reasserts the blocked downstream claim or effect.

### E.17.ID.CR:6 - Bias-Annotation

Scope: bounded comparative review units governed under `ComparativeReviewUnit` inside `InterpretationDiscipline`, not all review, all publication, or all decision work.

This pattern focuses on a bounded comparison over available sources. Recover the source claims, shared question, comparison basis and supported contrast. When the receiving work asks for a stronger claim, use its governing Method and retain the grounds already established by the comparison.

Fluent comparison can hide a stronger use. Make reader fit, interaction mode and source relation visible only when they change the unit’s use. Authority-bearing claims remain with their governing patterns and project-side FPF kinds and references named by value.

### E.17.ID.CR:7 - Conformance Checklist

A conformance check is retained only if it changes the next bounded use of the comparative review unit, blocks a concrete overclaim, or preserves a source reference or reopen condition needed for the declared bounded use.

Use ID.CR-Core for ordinary comparison notes. Conditional rows apply only when the note touches neighboring-pattern relation, bridge declaration, or reader-fit fields. For a fuller reading of a mixed case, use this checklist with the applicable neighboring pattern and the boundary conditions below.

#### E.17.ID.CR:7.1 - ID.CR-Core ordinary checks

1. **CC-ID-1 - Bounded comparative review unit is explicit.**
   The pattern distinguishes the bounded comparative review unit from the surrounding review or decision work.
2. **CC-ID-2 - Source references and comparison criterion are explicit.**
   A reviewer can see which fixed source episteme or source publication is being interpreted and which declared criterion or contrast supports the comparison.
3. **CC-ID-3 - The lift stays bounded.**
   The unit or its immediate review context keeps the supported contrast, comparison basis and material conditions recoverable. State a blocked use or reopen condition when it changes this comparison’s interpretation or receiving use.
4. **CC-ID-6 - Neighboring-pattern boundaries stay visible.**
   When the boundary trigger fires, the neighboring FPF pattern carries that prompt, ontology, action, gate, authority, or downstream claim instead of leaving it hidden inside comparative prose.
5. **CC-ID-8 - The review unit does not over-claim authority.**
   Any stronger authority claim requires its governing basis. Require an explicit review-only or non-executive limit when the unit’s wording, arrangement or receiving use could otherwise imply that authority.

#### E.17.ID.CR:7.2 - ID.CR-Conditional checks

1. **CC-ID-4 - Base-case governing-pattern relation is explicit.**
   A reviewer can tell why the case does not belong to `A.6.3.*`, an F.9 Bridge or bounded-use branch, an F.9.1 stance-note branch, `E.17.EFP`, `B.5.2(.0)`, `OntologicalReframing`, or `A.6.4`.
2. **CC-ID-5 - Bridge declaration does not hide.**
   If the case depends on bridge-mediated comparison, `bridgeOccurrenceRef` and `boundedUseClaimRef` are required. The latter resolves a claim whose `EntityOfConcern` is that Bridge and whose use/direction/rule/loss/polarity tuple matches the comparative unit.

   Positive use requires affirmative polarity and, when A.10 or B.3 is triggered, current reliance for that use; degraded reliance narrows it, while a negative, abstaining, reopened, evidence-needed, blocked, or mismatched result stops it.

   Authorization and the occurrence of comparative-review Work remain separate. Optional `bridgeCardRef` remains packaging; optional `bridgeStanceRef` resolves a separate F.9.1 episteme whose `EntityOfConcern` is that claim.
3. **CC-ID-7 - Reader-fit stays bounded.**
   `targetUserModel`, `interactionMode`, `contrastiveQuestion`, `boundedComparativeUse`, and `overreadRisk` are visible when needed, but they do not create an authority claim that the unit does not carry.

**Checklist recovery map.** To recover a checklist row by value for assurance, use its ordinary card row and worked example below. Consult these sources before relying on the checklist alone:

| Checklist row | Recover through first | Nearest worked or practical recovery |
| --- | --- | --- |
| `CC-ID-1` | `E.17.ID.CR:4.3.b.a` rows **Reviewed source** and **Shared review frame and alternative identities** | `E.17.ID.CR:5.4.5`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.a` |
| `CC-ID-2` | `E.17.ID.CR:4.3.b.a` rows **Reviewed source**, **Source references**, and **Bounded lift** | `E.17.ID.CR:5.4.5`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.a` |
| `CC-ID-3` | `E.17.ID.CR:4.3.b.a` rows **Bounded lift**, **Downstream-use limit, when needed**, and **World-contact limit, when needed** | `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.10`, `E.17.ID.CR:5.4.11` |
| `CC-ID-4` | near-top **Neighboring-work boundary**, **Quick working-fit check**, and `E.17.ID.CR:4.5 - Neighboring-work boundary glance` | `E.17.ID.CR:5.4.7` through `E.17.ID.CR:5.4.10` |
| `CC-ID-5` | `E.17.ID.CR:4.3.d` bridge-declaration fields plus `E.17.ID.CR:4.2` neighboring patterns | `E.17.ID.CR:5.4.1`, `E.17.ID.CR:5.4.2`, `E.17.ID.CR:5.4.3` |
| `CC-ID-6` | `E.17.ID.CR:4.3.b.a` row **Boundary trigger** plus the near-top boundary corridor | `E.17.ID.CR:5.4.7` through `E.17.ID.CR:5.4.10` |
| `CC-ID-7` | `E.17.ID.CR:4.3.d` interpretant-side fields, kept subordinate to the ordinary minimum and blocked downstream claim or effect | `E.17.ID.CR:5.4.4`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.b` |
| `CC-ID-8` | `E.17.ID.CR:4.3.b.a` rows **Downstream-use limit, when needed** and **World-contact limit, when needed** | `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.10`, `E.17.ID.CR:5.4.11` |

### E.17.ID.CR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it is wrong | How to avoid it |
| --- | --- | --- |
| **Comparison-unit instability** | The text sounds as if it governs a note in one section, a publication unit in another, a comparative move in a third, and a whole review process in a fourth. | Stabilise one bounded comparative review unit early and keep note, sheet, UI, and rendering labels explicit as ordinary forms of that object rather than stylistic substitutes. |
| **Bridge gloss inflation** | A helpful comparative sentence or stance word starts acting like a Bridge or use licence. | Require `bridgeOccurrenceRef` and `boundedUseClaimRef`; keep any Card optional, and use `bridgeStanceRef` only for a separate F.9.1 episteme about that claim. |
| **Soft prompt or choice smuggling** | The review unit has begun asking for an explanation or selecting an action but hides that change in comparative prose. | For an explanatory question with rival explanations still open, use `B.5.2.0` or `B.5.2` and publish the prompt's species, open question, scope, and motivating provenance. For a choice among already available actions, probes, or method options, use `C.11`; choice alone requires no `U.AbductivePrompt`. |
| **Viewing capture** | Same-entity restatement or representation-shift work is pulled into interpretation on the strength of improved readability alone. | Name the base source relation or representation work first and use bounded comparison only when bounded comparative lift is primary. |
| **Explanation-face laundering** | Interpretation language is used to avoid explicit `E.17.EFP` class and bounded-use review. | If face class or bounded connective prose is primary, stay with `E.17.EFP`. |
| **Gentle-tone advisory overread** | A calm explanatory tone can conceal an unsupported recommendation, assurance or gate claim. | State the applicable use limit and recover the grounds required by that stronger claim when it is requested. |
| **EntityOfConcern shift** | A changed target is mislabeled as interpretation because the prose still sounds comparative. | Apply `OntologicalReframing` or `A.6.4` once continuity witnesses or changed target govern the claim. |
| **Interface neutrality fiction** | A guided or contrastive aid pretends to be audience-neutral while steering blocked downstream use. | Make `targetUserModel`, `interactionMode`, and `contrastiveQuestion` explicit and keep the non-bounded use forbidden. |

### E.17.ID.CR:9 - Consequences

- The middle band between a short F.9.1 stance note about an existing bounded-use claim and prompt-bearing abduction becomes reviewable rather than rhetorical.
- Reviewers get a cleaner way to distinguish comparative interpretation from the first crossed claim that would make another governing pattern primary.
- Authors have a little more to declare. The comparison unit is more stable, and fewer mistakes at the boundaries with neighboring patterns go unnoticed.
- Guided comparative review units become easier to prepare: authors can state bounded use, overread risk and world-contact limits without implying a broader guidance claim.
- Users get a bounded way to keep comparative review units modest while the boundary trigger remains below the first crossed claim.

### E.17.ID.CR:10 - Rationale

Teams already write small comparative review units, often as comparison notes or sheets, to move a review forward.
What they usually lack is a disciplined way to keep that unit useful without letting it imply equivalence, an unstated hypothesis, pressure to redesign, or a release decision.

The pattern protects that everyday use of bounded comparisons.
It keeps a comparative review unit usable by making five entries visible enough to inspect: the bounded comparative review unit, the source references, the bounded comparative lift, the blocked downstream claim or effect, and the boundary trigger that would end interpretation.
A team can compare available source epistemes or source publications while keeping the authority of the comparison within its bounds.

### E.17.ID.CR:11 - SoTA-Echoing: Adopted and Adapted Invariants and Rejected Shortcuts


| Claim need | Source idea and named source | Source scope or reference | Local FPF invariant and practical local test | Nearest recovery reference | Adopted, adapted, or rejected shortcut |
| --- | --- | --- | --- | --- | --- |
| Comparative review units normally stay tied to explicit source, view, and review structure rather than shifting through helpful prose alone. | The official abstract identifies architecture-description concepts and practices; it supplies lineage for keeping the described subject and its views explicit. | Joint ISO, IEC, and IEEE 42010:2022; official abstract only, not a complete standard-conformance basis | This pattern uses that limited lineage. Its source references, comparison criterion and bounded-comparison rules are local FPF design, not requirements established by the inspected abstract. | `E.17.ID.CR:4.3.b.a` rows **Reviewed source**, **Source references**, and **Bounded lift**; `E.17.ID.CR:5.4.5`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.a` | **Use limited lineage.** |
| Interpretation and explanation use are use-sensitive and bounded by intended reader and knowledge limits rather than audience-neutral by default. | Explainable-AI guidance distinguishes explanation, meaningfulness for intended users, explanation accuracy, and knowledge limits instead of treating all helpful prose as equally safe. | Phillips et al. (2021), NIST IR 8312, *Four Principles of Explainable Artificial Intelligence*; source status = government guidance on AI explanations (2021) | This pattern adapts that stance into `targetUserModel`, `interactionMode`, `contrastiveQuestion`, `boundedComparativeUse`, and `overreadRisk`, while still keeping explanation-face use discipline with `E.17.EFP`. | `E.17.ID.CR:4.3.d` interpretant-side block, kept subordinate to the ordinary minimum; `E.17.ID.CR:5.4.4`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.b` | **Adopt and adapt.** |
| Static comparative notes and interactive comparative aids carry different relation loads. | Static review notes retain source references, a comparison criterion, a supported contrast and material conditions; explicit downstream limits are conditional. Interactive explanation-system practice becomes relevant only when the aid is interactive, stateful, adaptive, or user-model-bearing. | Labarta et al. (2026), *X-SYS: A Reference Architecture for Interactive Explanation Systems*, arXiv:2602.12748v3; source status = emerging preprint, not settled standard. | This pattern keeps the ordinary minimum sufficient for static notes and adds `targetUserModel`, `interactionMode`, state and history, `overreadRisk`, and bounded-use boundary only for interactive comparative aids. | `E.17.ID.CR:4.3.b.a` ordinary card; `E.17.ID.CR:4.3.f` static and interactive split; `E.17.ID.CR:5.4.4`, `E.17.ID.CR:5.4.7` | **Adapt conditionally.** Reject importing XAI architecture into ordinary static notes. |
| Reader plausibility, fidelity to a cited text, and faithfulness to a model decision process answer different questions. | NLP interpretation research distinguishes an explanation that convinces people from one that accurately reflects the model's prediction process; this does not establish fidelity to a cited engineering document. | Jacovi and Goldberg (2020), [*Towards Faithfully Interpretable NLP Systems*](https://aclanthology.org/2020.acl-main.386/), §§1–5; research source about NLP-model interpretation. | This pattern adapts the separation of evaluation questions by analogy. Its ordinary comparison of source claims uses its own explicit source references and comparison criterion, with the source-relation meanings in `E.17:5.1b`; it does not import a model-interpretation test. Further bridge, prompt or authority claims retain their own grounds. | `E.17.ID.CR:4.3.b.a` rows **Source references**, **Bounded lift row(s)**, **Blocked downstream claim or effect** and **World-contact limit**; `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.9`, `E.17.ID.CR:5.4.10`, `E.17.ID.CR:5.4.11` | **Adapt a limited analogy.** Keep the paper's model-process subject distinct from this pattern's source-text comparison. |
| Comparative review units do not become hidden ranking, aggregate recommendation, or false equivalence when a comparison sheet sorts or scores alternatives. | Quality-diversity practice and multi-objective optimization practice preserve diverse candidate sets and non-scalar trade-offs when one scalar score would hide relevant differences. | Mouret and Clune (2015), MAP-Elites; Deb et al. (2002), NSGA-II; source status = adapted design-space analogy, not naming or review standard | This pattern adapts only the anti-scalarization invariant: one comparison sheet can expose row-level comparison criteria, trade-offs, and visible ordering criteria, but it does not add equivalence, substitution, recommendation, method choice, gate passage, or decision authority unless `C.11`, `F.9`, `A.20`, `A.21`, another governing FPF pattern, or a project record named by value supplies that source relation or project record. | `E.17.ID.CR:4.3.b.a` rows **Bounded lift**, **Blocked downstream claim or effect**, and **Boundary trigger**; `E.17.ID.CR:5.4.5`, `E.17.ID.CR:5.4.6.e`, `E.17.ID.CR:5.4.6.f` | **Adapt conditionally.** Reject treating optimization vocabulary, Pareto wording, benchmark tables, or sorted display order as proof of a governing FPF relation. |

**Row 1.** The inspected ISO abstract supplies architecture-description lineage, not a rule for comparative review units. This pattern itself requires visible source references and comparison criteria so the reviewer can inspect the contrast. The **Reviewed source**, **Source references** and **Bounded lift** rows carry that local requirement; applying them makes no claim of conformity to the complete standard.

**Row 4.** Jacovi and Goldberg examine whether an interpretation reflects the reasoning behind an NLP model's prediction, separately from whether people find it convincing. A comparative review unit here instead compares claims in available sources under an explicit criterion. Its source-text fidelity follows from comparing what the note says with those sources, keeping their qualifiers, omissions and added contrasts visible under `E.17:5.1b` and this pattern's ordinary working card.

A note may reproduce a source accurately while the source's explanation misrepresents a model; a faithful model explanation may also be misquoted in a note. The evaluation question therefore selects what must be checked. Human review of source claims remains useful; this source analogy imposes no NLP-model intervention on an ordinary static comparison.

The **Blocked downstream claim or effect** and **World-contact limit** rows keep further bridge, prompt and authority claims subject to their own grounds. This lets an engineer-manager inspect what the comparison warrants without giving polished prose authority over the source episteme or publication set. Case linkage: see `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.9`, `E.17.ID.CR:5.4.10`, and `E.17.ID.CR:5.4.11`.

### E.17.ID.CR:12 - Relations
- **Citation.** Cite this pattern as `E.17.ID.CR`, `ID.CR`, or `ComparativeReviewUnit` when the current object is one bounded comparative review unit. Use `A.6.3.CR` when the intended pattern is `ConservativeRetextualization`.
- **Placement.** `ComparativeReviewUnit` sits inside the wider `InterpretationDiscipline` naming family, but the local governing object is the comparative review unit and its bounded comparison. The wider review or decision work remains outside until a crossed claim becomes primary.
- **Builds on:** `C.2.2a`, `A.16.0`, `F.9`, `F.9.1`, Part F, `A.6.9`, and `E.14`.
- **Coordinates with:** `A.6.P`, `A.6.3`, `A.6.3.CR`, `A.6.3.RT`, `A.6.3.CSC`, `F.9`, `F.9.1`, Part F, `A.6.9`, `E.17.EFP`, `B.5.2.0`, `B.5.2`, `OntologicalReframing`, `A.6.4`, `C.11`, `A.15`, `A.15.2`, `A.15.4`, `A.20`, `A.21`.
- **Boundary map.** Use `E.17.ID.CR:4.5` when the comparison starts carrying relation precision, bridge or sameness, prompt or action selection, ontology or changed target, decision, work or reliance, gate, assurance, adjudication, or reduced-source-use claims. The neighboring pattern governs only the crossed claim it names.
- **Local repair neighbors.** Use `E.17.AUD.LHR` only when a local lexical head or qualifier still destabilizes the same unit; use `E.17.AUD.OOTD` only when the reviewed-source, publication-unit, comparative-move, or outside-work boundary is still unstable after local repair.

### E.17.ID.CR:12a - C.29 mathematical-lens use relation

> When a bounded comparative review unit uses a mathematical comparison criterion, rival lens, invariant, obstruction, or structural similarity, `E.17.ID.CR` still works over comparison unit, viewpoint, comparison criterion, review-unit boundary, and bounded-use boundary.
>
> The applicable `C.29` output for the stated use can be cited only for the mathematical-lens use. If that output is `MathLensUse.LensCandidateNote`, retain its first-candidate recognition use and next lens-use action and output; `CandidateMathObject?` remains optional.
>
> When citing an output for a claim-bearing mathematical-lens use, use the exact `MathLensUse.OneLine`, `MathLensUse.MiniCard`, or `MathLensUse.FullCard` result required by C.29 and keep recoverable its candidate mathematical object, lens mapping mode, preserved and lost structure, and stop condition, plus `LensUseBoundaryValue` and `declaredLensUse` where C.29 requires them; include `blockedLensOverread?` only when it passes F.19's plausible-reader test.
>
> Keep the review unit's bounded use and blocked downstream claim or effect explicit. The C.29 output does not create the comparison record, adjudicate rival publications, or authorize bridge, evidence, selector, or benchmark claims outside the comparative-review-unit record.

### E.17.ID.CR:End
