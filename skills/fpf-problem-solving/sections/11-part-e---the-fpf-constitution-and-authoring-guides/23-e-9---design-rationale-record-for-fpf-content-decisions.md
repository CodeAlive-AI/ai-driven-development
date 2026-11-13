## E.9 - Design-Rationale Record (DRR) for FPF Content Decisions

> **Type:** Governance and authoring pattern
> **Status:** Stable
> **Normativity:** Normative

### E.9:0 - Use this when

- A proposed normative change needs a statement of what FPF should say, why that answer is preferred, and which neighboring patterns or selected non-pattern FPF kind-reference pairs it affects.
- Several such loci must change together. An external record must keep the complete content decision available while authors distribute enduring text across Core.
- Authors would otherwise have to settle the same consequential question separately in several patterns or selected non-pattern FPF kind-reference pairs.
- Authors need to review a deprecation, narrowing, or cross-pattern amendment without reconstructing its rationale from patches, conversations, or scattered notes.

**Not this pattern when.** Normative Core rules belong in their selected loci. Keep campaign and process briefs outside the DRR. If a purely editorial `Delta-0` or `Delta-1` change needs a decision record, use the lightweight variant in `CC-DRR.5` when it fits. Use `E.9.DA` when a DRR already exists and you need to judge its answer, obligations at selected loci, source use, lexical closure, and drafting actionability for a declared downstream authoring use.

#### E.9:0.1 - What goes wrong if missed

- Later readers cannot recover why Core changed, which alternatives were rejected, or which exclusions were intentional.
- Coordinated amendments drift apart when the selected answer survives only in patches, handoffs, or a reviewer's memory.
- Later repairs can fit local wording while losing the constraints supplied by Pillars, taxonomy lenses, the impact graph, practical use, or pattern placement.

#### E.9:0.2 - What this buys

- An external record states the content of a bounded FPF change before authors rewrite Core.
- Four components keep the Problem frame, Decision, Rationale, and Consequences available for later review and replay.
- For a distributed change, the record holds the selected answer while authors draft the enduring Core text at the selected loci.

**First useful move.** State the working FPF problem, selected answer, practical change, selected loci, first substantive drafting action, and nearest boundary in plain, precise language before drafting or landing Core text.

**Cheap stop.** If local wording repair, application of an accepted pattern, or editorial cleanup preserves FPF semantics, obligations, boundaries, names, admissible uses, and normative force, it needs no full DRR.

Use `F.19` for kind-preserving plain rewriting and `E.10` for an unresolved FPF wording-use question. Use `E.17.AUD.LHR` for an overloaded local lexical head inside one publication unit and `C.2.P` for an episteme, publication, or source-use distinction still unresolved after `E.10`. Use `F.18` only for minting a durable reusable name and `E.8` for an authoring-form correction. Use `E.9` when a bounded content decision needs its rationale stated.

**Kind-or-boilerplate diagnostic.** Before proposing wording from a DRR as pattern prose, use `F.19` to separate boilerplate from substantive content. If the remaining wording still obscures its use, name, relation, claim, admissible use, selected locus, user action, or flow position, name the contribution applied: `E.10`, `E.10.ARCH`, `F.18`, or the pattern that defines the object or relation. Keep process, architecture, review, and reference boilerplate in the material it belongs to.

Before using proposed wording in a pattern, establish from the selected answer which object, relation, claim, slot, use, admissibility condition, or scope would change, or that none would change. Use `F.19` and the pattern that defines or constrains the distinction. Introduce Method, Work, application, or ClaimGraph details into ordinary wording only when that distinction changes the decision or a later reliance.

**Primary EntityOfConcern in plain terms.** The external decision-rationale record for one bounded FPF content decision or coordinated change set. The author must be able to recover the problem, selected answer, reasons, consequences, practical change, selected loci, and boundary without inventing them. Add exact C.2.1 identity only when the decision or a named later reliance needs it.

**Primary working reader.** An FPF author, reviewer, or steward uses the DRR to evaluate, challenge, or land a bounded content decision. Downstream pattern readers can use the guidance once it has been incorporated into Core.

### E.9:1 - Problem frame
Under Pillar **P‑10 Open‑Ended Evolution**, FPF's normative rules must adapt as new calculi and insights arrive. Changes whose answers and reasons cannot be recovered erode those rules. A formally detailed record can still defer the decision or distribute a harmful rule. A **Design‑Rationale Record (DRR)** preserves the selected answer and its reasons for one bounded change before authors distribute its normative content.

### E.9:2 - Problem
Either a direct edit to Core or a DRR that documents the apparatus but leaves the answer unusable can expose the following risks.

1. **Lost decision grounds** – future authors cannot recover why the answer
   was selected, which alternative or boundary mattered, or when to reopen it.
2. **Decision deferral** – a polished record leaves the answer, affected loci,
   or first drafting action for each later author to invent again.
3. **Proxy-led fanout** – an abstract rule passes a schema, checklist, or
   unrelated replay while making an actual predecessor/proposed host harder to
   understand or use.
4. **Conceptual and authority drift** – incremental edits blur the framework's
   foundations, or the temporary rationale record becomes a shadow Core law,
   process brief, or authorization source.

### E.9:3 - Forces

| Force | Tension |
|-------|---------|
| **Agility vs Rigour** | Evolve swiftly ↔ demonstrate deliberate, Pillar‑aligned decisions. |
| **Transparency vs Efficiency** | Provide a public argument trail ↔ avoid bureaucratic drag on minor edits. |
| **Clarity vs Conciseness** | Capture enough reasoning and coordinated implications ↔ prevent meta‑text from bloating the Core itself. |

### E.9:4 - Solution — state the decision before distributing it

Present the `Decision` account first in plain, precise language. Before a reader meets a DRR identity schema, a Method or Work account, or a catalogue of alternatives, they must be able to recover, in this order:

1. the working FPF problem and why it matters now;
2. the selected answer stated positively;
3. what changes in practitioner or authoring use;
4. the selected loci and the positive obligation each one carries;
5. the first substantive drafting action; and
6. the nearest boundary, blocker, or reopen condition.

If the answer is unsettled, develop it through a working expression under §4.2. The order above is for readers of the resulting decision; inquiry can start with an open question.

Once supported, the short decision account is the primary source for drafting. Add exact Method, Work, application, episteme identity, source use, assessment, or authority only when the decision or a named later reliance depends on that distinction.

A nontrivial DRR must make the four components below recoverable. They form the minimum decision kernel. `CC-DRR.5` gives the lightweight editorial variant.

| Minimum-kernel component | Guiding question | Typical content |
|-----------|------------------|-----------------|
| **Problem frame** | *Why are we talking about this?* | Working problem, trigger, intended FPF use-value, scenario, or external change. |
| **Decision** | *What will we do?* | Selected answer, positive content distribution, practical change, first drafting action, and nearest boundary. |
| **Rationale** | *Why this answer?* | The material comparison, load-bearing Pillar or taxonomy-lens effects, architecture/usability/SoTA grounds, and uncertainty that could change the answer. |
| **Consequences** | *What follows?* | Benefits, trade-offs, affected loci and direct consumers, practical gains/costs, validation obligation, and reopen condition. |

In this pattern, a **bounded coordinated change set** brings together mutually dependent content-decision questions within one decision boundary. Several patterns or selected non-pattern FPF kind-reference pairs carry the enduring FPF expression of that decision.

The **selected answer** is what FPF should say, which selected loci carry it, what practical action changes, what stays outside, and which source-use, evidence, validation, or loss/recoverability conditions remain live.

A **selected non-pattern FPF kind-reference pair** is a content-distribution instruction, not a new kind. It names an admitted FPF kind and one exact reference by value—for example a `U.View`, source map, source-use note, evidence-path record, review-finding record, or architecture-decision record. The selected patterns and such non-pattern items are the **selected loci** of the decision.

A **temporary convergence record** holds the selected answer while authors update several selected loci. Enduring normative rules belong in Core, and process state belongs outside the DRR.

Keep a rejected alternative only when it explains the selected answer, a live boundary, or a reopen condition. Pillars and taxonomy lenses may inform the decision, but the DRR records their load-bearing effects rather than rehearsing every lens or preserving the history of discussion.

Before adopting a language, ontology, or authoring rule for wider use, apply it to at least one real host and its proposed replacement, including their dependencies. At comparable effort, compare the recognizable entry, required inputs, first action, practitioner vocabulary, formality and assurance burden, first useful result, stop or return, preserved useful ideas, and direct consumers.

The proposed wording must pass the E.8 first screen and the `F.19` kind-preserving plain-rewrite test. A schema, invented fact pack, unrelated lane test, checklist, or promised review cannot replace this comparison. If the pilot makes the host harder to use without a compensating semantic gain, repair or reject the rule before applying it elsewhere.

A DRR records the selected answer. When exact identity or reliance makes the distinction material, separately identify the decision work and method, selected-answer result, C.2.1 DRR episteme, source-use relations, assessment and result, any acceptance or authority, and later realization work. An exact DRR episteme then follows C.2.1 identity by `<ClaimGraph, EntityOfConcern, effective ReferenceScheme>`; ordinary use does not require materializing that whole account.

#### E.9:4.1 - Minimum decision-inspection content blocks

A nontrivial DRR must also make the following parts of the decision available for inspection. Authors may present them within the four kernel components or in a dedicated `Decision grounds used` or decision-inspection block. They are part of an adequate decision before it reaches a later review.

| Decision-inspection content block | What must be recoverable by value | Usual location in the DRR |
|---|---|---|
| **Exact decision grounds and governing inheritance** | The exact source documents, accepted architecture and audit records, and inherited decisions that govern this choice, plus any uncertainty those grounds leave open. | Header or `Decision grounds used`, with the Problem frame or Rationale carrying the decision-relevant source use. |
| **Purpose, utility, and scenario grounding** | Intended FPF use-value, first-minute working situation, minimum scenario/anti-case grounding, and compact utility/fitness reading. | Problem frame. |
| **Decision-relevant alternatives and current disposition** | The alternatives needed to explain the selected answer, a live boundary, or a reopen condition, with their current disposition. Discussion history and harmless options stay outside the current DRR; retain them in a separate historical source only when a named later use needs that history. | Decision and Rationale. |
| **Content-distribution and outside-boundary map** | For each consequential part of the answer, state what each selected locus must say, which related loci stay unchanged and what must agree across them. For a selected pattern, name the first subject kind and the action to explain. Use a consistent, compact account of exclusions and non-obligations to guide distribution. Do not paste it into the pattern Solution as negative doctrine or leave its distinctions for a later wording repair. Ordinary `use/apply this pattern` remains valid shorthand. In the distribution map, state the concrete claim, relation, boundary, or practitioner action that would change. Repeated content-family and reference catalogues, README/ToC/E.11 navigation, current development's package-boundary, split/defer, and architecture-placement correspondence, and phrase-level boilerplate around simple claims stay in DRR, architecture documents, handoff, relation rows, README, ToC, `E.11`, or one compact local locus instead of the Solution. Publish use-changing architectural reasons under `E.8:4.2.3`. When proposed wording still needs precision restoration, name the pattern that supplies it: `E.10`, `E.10.ARCH`, `F.18`, `F.19`, or another governing pattern. Classify each named related locus now. Phrases such as `most likely` / `may need` / `if later touched` leave its disposition undecided. | Decision. |
| **Existing-pattern sufficiency and new-pattern necessity** | For each load-bearing selected answer, whether an existing pattern suffices, an existing non-pattern FPF kind-reference pair suffices, or a new locus is needed. Explain why the rejected options would put the content in the wrong place, overload its governing locus, or split it unnecessarily. | Decision and Rationale. |
| **Naming, ontology, and wrong-carrier-confusion account** | Head/branch/object/move/outside-work separation, tempting wrong-pattern assignment or wrong non-pattern FPF kind-reference assignment, and any load-bearing `F.18` naming obligation needed to keep the selected answer truthful by value. | Problem frame, Decision, and Rationale. |
| **Reusable content-disposition when triggered** | Whether a potentially reusable selected non-pattern FPF kind-reference pair remains local, is generalized now, is rejected, or is placed outside the current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record. | Decision and Rationale. |
| **Loss and recoverability template when source-loss or scope narrowing is declared** | Preserved distinctions, dropped distinctions, admissible use, non-admissible downstream use, recoverability class, and reopen/stop rule. | Decision and Consequences. |
| **Selected locus and related-pattern boundary account** | Why the selected loci carry the content, which tempting selected loci stay outside, and which patterns govern the claims, relations, or boundaries left outside. | Decision and Rationale. |
| **Convergence and overlap account when several content-decision branches touch the same carrier set** | Whether overlap is valid convergence or an architecture problem requiring reconsideration, what agreement across selected loci must hold, and whether the decision selects or refuses a new pattern or selected non-pattern FPF kind-reference pair. | Decision and Consequences. |
| **Selected-answer stability boundary** | Which elements of the selected answer are fixed now for later FPF drafting, and which later elaborations may strengthen wording, examples, source-use rows, or validation evidence without reopening the selected answer. | Decision and Consequences. |
| **Impact, practical gains, and remaining validation evidence obligation** | Affected patterns and selected non-pattern FPF kind-reference pairs, practical gains/costs, authority or release consequences when they follow from the content decision, and the remaining validation evidence obligation that constrains later authoring or landing. | Consequences. |
| **SoTA and competitive-positioning account when load-bearing** | Current best-known problem-solving source anchors and source-derived moves under E.8 that discipline the decision, what problem-owning domain or practice they answer to, which official, popular, or legacy alternatives they reject or bound when relevant, and what unresolved uncertainty would materially change the selected answer. | Problem frame, Rationale, and Consequences. |
| **Actual-host predecessor/proposed replay when a broad authoring rule is selected** | One dependency-aware real host comparison at comparable effort: recognizable entry, inputs, first action, vocabulary, formality and assurance burden, first useful result, stop or return, preserved useful ideas, and direct consumers. The proposed wording passes E.8 and F.19; a proxy or promised later review does not substitute. | Decision and Rationale, with the selected rule and pilot effect carried into the locus obligations. |
| **Campaign problem-solution unfolding carry-through when triggered** | For campaigns changing README entries, path-shaped patterns, pattern families, DPF entries, or first-practical routes: the map from admitted problem-side record refs or cues, accepted starting records, current starting structures, and entry cues to selected solution architecture, affected unfolding families, loci added or changed, governing-pattern map, content assigned from DRR or README into patterns or unfolding structures, and any independently grounded overread that a plausible intended reader could make. | Decision, selected-locus map, and Consequences. |

These blocks supply the content of the decision. Four headings cannot tell a later author the grounds, first-minute working situation, naming choice, distribution, sufficiency or necessity of a pattern or non-pattern FPF kind-reference pair, treatment of overlap, impact, or remaining uncertainty. Make those answers recoverable in the DRR without creating separate process paperwork.

For a coordinated change, settle the common answer in the DRR before drafting. Each author can then express that answer at the selected locus without having to decide it again.

When a decision connects several selected loci or mutually dependent edits to patterns and non-pattern FPF kind-reference pairs, its DRR **MAY** include more than the minimum kernel. It can state obligations at each locus, the choice between a new and an existing pattern, how impacts or non-goals map across the selected loci, coverage or agreement across them, and whether overlapping changes converge. A provisional account of the decision rule can hold the full bounded answer until its enduring content is distributed in Core.

These additions leave the DRR's kind unchanged. It conforms only while it records what FPF should say and why, what is excluded, how the selected loci are affected, and what improves in practice or authoring. A record with richer coordination content **MUST NOT** become a campaign plan, process script, baton carrier, packet checklist, staging log, or other development-process brief.

If an existing pattern or selected non-pattern kind-reference pair might suffice, or a new locus might be needed, the DRR must settle that choice. A tentative list leaves the choice to the next author.

Classify each pattern or non-pattern kind-reference pair that the accepted grounds or the DRR bring into the distribution question. State its obligation if selected. Otherwise identify it as an unchanged boundary neighbour, inherited unchanged, or outside the current decision with a named pattern, kind-reference pair, or decision record. Saying it `may need local hardening` leaves that choice open.

If the grounds reveal a potentially reusable non-pattern carrier or a related source-use, evidence, assurance, validation, or architecture-decision mechanism, the decision must classify it as generalized now, kept local with a reason, rejected, or outside with a named locus or decision record. The DRR records the choice; mentioning an artifact does not decide its use.

For source loss, simplification, redaction, summarization, or other declared loss, the DRR must state which distinctions survive and which are lost. Identify each admissible branch reading and its selected non-pattern FPF kind-reference pair, the uses without an admissible carrier or evidence path, the recoverability class, and the stop or reopen rule when the use exceeds the declared loss or narrower scope.

Before another author can use a nontrivial DRR to draft the selected changes, it must settle the material choices about its EntityOfConcern, selected loci, outside boundary, reusable content, and loss or recoverability regime. Each is selected, rejected, inherited unchanged, or placed outside with a named locus or decision record. While any of these choices is missing, the work is still establishing the decision grounds; it has not produced an accepted DRR.

The DRR episteme lives **outside** normative Core. A separately governed acceptance, authority, or realization decision may rely on it, but the word *accepted*, a record status, review mark, or publication does not make its claims true or authorize change.

Once realization is separately authorized, authors apply the selected answer to its loci in dated authoring work. The changed Core content, authoring work, result claims, checks, witnesses, publications, and any landing or release record remain distinct; apply the relevant pattern to each claim. The DRR remains external provenance and temporary convergence support; after realization, the enduring semantics must be available in Core.

Authors using a separately accepted selected answer may elaborate examples, SoTA-Echoing, recognition sections, local wording, and neighboring fit inside its declared stability boundary. A change to the selected answer, selected loci, outside boundary, reusable-content disposition, or loss/recoverability regime requires a successor decision result and DRR episteme rather than a silent edit to downstream prose.

Improvement work may apply E.23 to a DRR episteme. That work, its method applications, quality-result claims, and witnesses are separate from the DRR and do not turn the record into a pattern draft. When a successor decision relies on SoTA, its result must show what changed in the selected answer, locus obligation, boundary, example, validation obligation, or reopen condition; otherwise the source use remains rationale-only or lineage-only.

When a campaign changes route-shaped, unfolding-shaped, first-entry, DPF or multi-pattern path material, make the connection from its actual starting situation to the selected solution and next use recoverable. The following optional form can carry those contents; include only fields that describe the current decision:

```text
CampaignProblemSolutionUnfoldingCheck:
  campaignProblem:
  acceptedProblemSideRecordRefsOrCues:
  selectedSolutionArchitecture:
  affectedReadmeEntries:
  affectedUnfoldingFamilies:
  acceptedStartingRecordRefs[]:
  acceptedStartingStructureRefs[]:
  entryCueRefs[]:
  nextUseOrResultMap:
  unfoldingLociAddedOrChanged:
  governingPatternMapAddedOrChanged:
  patternPlacements:
  whatStayedOnlyInDRRAndMustMoveToPatternOrUnfoldingStructure:
  whatStayedOnlyInReadmeAndMustMoveToPatternOrUnfoldingStructure:
  blockedOverreads?: [only exact readings admitted by `F.19`'s grounded-contribution test]
  rejectedUnfoldingAlternatives?: <only those needed to explain the selected answer, boundary, or reopen condition>
  unfoldingCarryThroughResidueAfterContentUpdate:
  refreshOrReopenTrigger:
```

After host drafting, identify any enduring selected content that remains available only in the DRR. Move it into the selected pattern body, unfolding block, README seed, E.11 expansion or concrete relation locus so that the public reader can obtain and use the solution.

To preserve **P-2 Didactic Primacy** without duplicating meta-text, realization work using a separately accepted selected answer should distill stable Rationale, Consequences, SoTA-Echoing, Grounding, and other valid convergence content into the selected informative pattern loci under E.8. The DRR episteme remains external provenance; it is not itself landed or transformed into Core.

A substantive DRR is one claim-bearing episteme about one bounded current content-decision question/change set. It may carry selected obligations only in its Decision or Consequences, but no route, gate, handoff, packet, monolith, mutable status, or future-campaign state. Any undecided remainder is explicitly outside the decision with a named pattern, kind-reference pair, or successor decision record.

#### E.9:4.1a - Process-source method admission into FPF

When an author considers a stable method described in a process source, the author decides the FPF-admission disposition by value. The DRR records that decision and any source-use relation that matters; neither the source passage nor the record becomes a second canon.

Record the following when deciding whether to admit the method:

- the content of the passage or accepted decision ground being considered from the process source;
- the reusable FPF method recovered from that passage;
- the current FPF pattern, section, or accepted `DRR` that already carries the method, if any;
- the contribution still missing from FPF;
- the FPF pattern selected to carry that contribution;
- process-control material excluded from FPF pattern prose, such as task dispatch, seam state, helper behavior, Git recovery, packet transport, review transport, chat cadence, and mutable release state;
- how the passage or decision-ground item was used: quoted by value, narrowed in scope, instantiated as a case, used as decision grounds or drafting guidance, retained only as an example, or retired;
- any meaning loss or addition created by that source-use result: changed scope, relation, evidence path, admissible use, non-admissible use, reader use, or recoverability condition;
- the first improved FPF use that the admitted method gives to an author, reviewer, or downstream FPF user;
- the disposition: selected now, inherited and sufficient, rejected now, or outside this decision. For an outside item, name the evaluation pattern or accepted `DRR` that carries it, or state the content of the accepted decision ground that does so.

Reusable process-source methods may contribute beyond semio wording or pattern-authoring language. Admit the contribution when it is separable from local process mechanics, improves the selected FPF use, and has adequate grounds for the claims being made. Apply E.19 to pattern admission and E.21 when a pattern-quality conclusion is required. After the method lands in FPF, process documents should cite the selected FPF pattern instead of keeping a parallel long-form rule.

#### E.9:4.2 - Develop an unsettled decision through a working expression

If the answer is unknown, start with the difficulty and the material available. Use §4's order to present the answer once selected. Filling the Decision block in advance would require the author to guess what the inquiry is meant to establish.

Use a provisional expression to bring a consequential relation into view: juxtapose two cases, arrange competing explanations, trace a dependency, or compare an intended use with the result currently available. E.8:4.2.1.2 and A.6.3.RT.OE supply the expression construction. Identify what the arrangement lets you infer and what remains unsupported. A question mark can make an unresolved interpretation visible; it supplies no premise for choosing one answer.

Let the result change the decision question when it reveals that the original question conflated different work. Retain live alternatives only for the comparison they support. Replace a classification by format, tool or package name when the deciding difference concerns the operation or conditions of use. A working table can therefore be revised or discarded after it has produced the useful distinction.

Before another author relies on the selected answer, resolve each premise that can change its selected obligation, or bound the result so that the remaining uncertainty does not defeat that obligation. If neither is possible, state where the decision must stop. Use the four kernel components and the applicable inspection content in §4.1 to inspect that closure. Material already recoverable in the account need not be copied into another answer column. A source pointer without the needed substantive contribution is not recoverable decision content.

Keep this difference visible in the writing. “The source order for this row is unknown” can be a valid investigation result. “Convert this row using day/month/year” would require the missing premise. Conversely, a settled decision to stop such rows and request their interpretation can be supported even while their dates remain unknown. What remains open must be compared with the decision being made.

The record carries the resulting problem, selection, reasons and consequences, not every discarded worksheet or the chronology of deciding. Retain a working expression when a later use needs its reasoning or recoverability; otherwise carry its useful result and source return into the decision.

### E.9:5 - Archetypal Grounding (System / Episteme)

| Holon flavour | DRR analogue | Minimum kernel illustrated |
|---------------|--------------|-----------------------------|
| **`U.System`** (physical target) | The author compares options for a pump-motor change; the selected answer specifies brushless DC and exact control/maintenance loci. | The C.2.1 DRR episteme records inefficiency/plant-use problem, alternatives, energy-versus-cost/authority rationale, selected loci, control-schema and supplier consequences, and validation obligation. |
| **`U.Episteme`** (knowledge target) | The author compares options for a theory revision; the selected answer specifies a new axiom and exact theory/teaching loci. | The DRR episteme records conflicting data, alternatives, explanatory/Pillar rationale, selected distribution, predictions, curriculum consequences, and downstream validation obligation. |

#### E.9:5.1 - Decide what support a conversion pattern should carry

An author is revising the date-conversion explanation in E.8:4.2.1.1. The explanation already supplies the essential rule: use the applicable supplier guarantee to choose the date order before running the converter. North guarantees month/day/year, South day/month/year for the files at issue. The same text, `03/04/2026`, accordingly yields March 4 or April 3. The intended practitioner can run a converter with a supplied order. The author can follow that reasoning but has yet to decide whether the public method should prescribe a table, a per-row card or prose alone.

A first working note says: “Choose a standard date card; include source, raw value, order and converted value.” It proposes a form before establishing whether all four entries are independent user inputs or what their arrangement must let the reader do. Turning those words into a completed Decision would hide the open question.

The author constructs the raw/result expression and its unresolved cell shown in E.8:4.2.1.2. It keeps both possible results visible. Trying to select an output from the raw text alone fails. The supplier difference leads to the source-qualified comparison. This yields a more useful decision question: **which source-to-interpretation connection must the pattern explain, and which expression makes that connection usable without requiring unnecessary repeated entry?** The comparison shows which information must be available and which the user must enter. Removing repeated entry still requires access to the source information.

The author now compares three alternatives for practitioners with the same preparation:

| Alternative | What it supplies | What changes the decision |
| --- | --- | --- |
| Prose instruction and the current worked reasoning | The source-to-order selection and the mixed-order stop are already available. | It remains sufficient for a reader who can keep the small comparison in view; it does not prescribe a repeated record. |
| A four-field card manually completed for every row | An addressable per-row account can travel separately. | Within one qualified session, copying the fixed order and derived result adds work; separated use may instead need the source and guarantee return. |
| A source-qualified comparison in the explanation, with a use-relative working view | Both interpretations of the same raw text are inspectable together; the interpretation remains connected to its guarantee. | Its labels and context must remain recoverable if the table travels; a local single-source view may omit repeated displayed inputs only while the context supplies them. |

The comparison does not demonstrate that every reader is faster with a table. It establishes different supported operations and context dependencies. The author selects the third alternative for the explanatory example, retains the first as a sufficient compact use, and rejects the universal manual-card requirement. The selected pattern account has to teach the conditions of reducing the view and restoring the missing context.

A short decision account can now carry the useful result:

- **Problem frame:** the existing conversion method is available, but authors lack the worked choice between explanatory comparison and a mandatory record for each conversion.
- **Decision:** develop the expression-construction explanation in E.8:4.2.1.2, with the source-qualified comparison and a conditional reduced view. Preserve §4.2.1.1's source-to-order selection and stop when the date order is unknown. Do not prescribe a card for every row or change the converter's subject method.
- **Rationale:** the different outputs for identical raw text require an interpretation supplied by the applicable source. A juxtaposed comparison teaches this relation. Re-entering a value already supplied by the session is a separate burden with no additional contribution to that local operation. Detached reuse changes that judgement.
- **Consequences:** keep the guarantee's scope and source return beside the operation; restore row-level context for mixed or separated use. First draft the explanation and the expressions being compared at the named locus. Examine whether the intended reader can recover and apply the selection under the stated preparation. Do not claim observed learning, speed or universal usability from this construction.

These paragraphs supply the bounded content decision; they are not answers copied into every inspection row. Its exact grounds are the existing E.8 explanation, the stipulated supplier guarantees and the performed comparison. The related conversion operation remains unchanged. No new date kind, source-independent interpretation or general record schema is selected. A changed supplier guarantee reopens the affected interpretation; an actual reader failure would reopen the explanation or its support.

Now South changes to mixed orders without row-level information. The author can still settle the content decision to preserve the earlier results, represent the new unknown and stop that row's conversion pending a trustworthy interpretation. The missing date order does not prevent explaining that boundary. It does prevent selecting a particular converted date. If the proposed public method instead promised to convert every row without obtaining such information, the author would have to change that promise or stop the dependent decision.

E.9's four components and inspection content remain stable aids for making the final selection recoverable. The provisional card is not preserved merely because it was the first form used. Its useful source-to-interpretation distinction survives in the selected account, while unnecessary per-row manual entries are removed. Here E.9 applies to the choice of support for an author: the working expressions helped form the question and select an answer; the record preserves that supported answer for the next author.

### E.9:6 - Bias-Annotation

| Lens | Bias risk in DRR use | Mitigation in this pattern |
|---|---|---|
| **Gov** | The DRR can become a bureaucratic approval ritual rather than a decision-rationale record. | Keep `CC-DRR.5` for lightweight editorial changes and require richer DRRs only when the content decision is semantically load-bearing. |
| **Arch** | A rich DRR can become a shadow specification that competes with the selected Core loci. | Treat the DRR as a temporary convergence aid; enduring content is distributed into the selected Core loci. |
| **Onto/Epist** | Authors can mix content decisions, evidence paths, source-use grounds, process state, and provenance into one ambiguous object. | Require exact decision grounds and selected-answer boundaries while excluding process-order state, baton, packet, and mutable status state from the DRR. |
| **Prag** | The method adds work before editing Core text. | Allow pointer-based DRRs and require only the selected non-pattern FPF kind-reference pairs needed for the selected decision. |
| **Did** | Rationale can become too internal for later authors to use. | Distill stable rationale, consequences, anti-cases, and SoTA implications into informative pattern sections when the Core text is updated. |

This bias annotation applies to every FPF semantic change governed by `E.9`. It does not turn project-management state, helper state, or review logistics into DRR content.

### E.9:7 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC-DRR.0 (ordinary decision first, exact distinctions when material)** | The working problem, selected answer, practical change, loci, first drafting action, and nearest boundary are recoverable before optional method/work/application or episteme apparatus. If identity or named reliance changes the claim, the relevant method, work, result, record, source use, assessment, authority, and realization remain distinct. | Keeps the DRR usable without losing exact distinctions when they matter. |
| **CC-DRR.0a (optional exact DRR identity)** | When exact DRR identity is needed, its ClaimGraph, bounded decision-question/change-set EntityOfConcern, and effective ReferenceScheme are recoverable; carrier, rendering, route state, status, or later Core edit is not an identity constituent. | Preserves a recoverable claim episteme without making every ordinary DRR start from the schema. |
| **CC-DRR.0b (actual-host replay for broad rules)** | Before distributing a broad language, ontology, or authoring rule, replay it on at least one real host and its proposed replacement, accounting for their dependencies. The replay compares entry, inputs, action, vocabulary, formality and assurance burden, result, stop, useful predecessor ideas, and direct consumers at comparable effort; proxy evidence does not substitute. | Prevents a clean-looking abstract rule from degrading use of the affected patterns. |
| **CC-DRR.0c (positive decision and restrained alternatives)** | The current DRR carries the positive selected decision. A rejected alternative remains only when it explains the answer, a live boundary, or a reopen condition; Pillar and taxonomy-lens effects are recorded only where they changed the decision. | Prevents negative catalogues and ritual completeness from displacing the authoring source. |
| **CC‑DRR.1** | For a Delta-2 or Delta-3 semantic change, the DRR **SHALL** make Problem frame, Decision, Rationale, and Consequences recoverable before Core drafting. Any exact decision-work/application account or authority to realize the answer is added only when that identity or reliance is current and remains a separate governed claim. | Prevents undocumented semantic edits without imposing the high-reliance account on ordinary use. |
| **CC‑DRR.1a** | A DRR whose proposed change is expressed as a new or revised pattern written in the standard template (E.8) **MAY** satisfy that minimum kernel by **pointing to** the corresponding pattern sections rather than duplicating prose. | Avoids copying the argument a second time while keeping it recoverable. |
| **CC‑DRR.1b (rich convergence content is permitted)** | A DRR that coordinates several selected loci, or mutually dependent changes to patterns and selected non-pattern FPF kind-reference pairs, **MAY** include additional substantive sections beyond the minimum kernel—for example obligations on selected loci, explicit new-pattern vs existing-pattern decisions, boundary/non-goal maps, coverage or agreement maps across selected loci, convergence classification, or a provisional statement of the decision rule—provided that the DRR stays about the FPF content decision and **MUST NOT** become process management. | Lets a single record settle coordinated changes without leaving authors to invent decisions during distribution or create shadow documents. |
| **CC-DRR.1c (exact decision grounds are recoverable)** | A conforming DRR **MUST** make its exact decision grounds and governing inheritance recoverable by value, either in a dedicated `Decision grounds used` section or an equivalent header with exact source-use and rationale fields. Routing, status, and provenance records do not count unless their content governs the decision. | Lets authors verify the decision against the sources and inherited decisions that govern it, avoiding distortion through repeated retelling. |
| **CC-DRR.1d (problem-frame adequacy)** | The Problem frame **MUST** make the intended FPF use-value, first-minute working situation, minimum scenario/anti-case grounding, compact utility/fitness reading, and any load-bearing current SoTA, competitive-positioning, or inherited-decision justification recoverable by value. | Prevents a DRR from being formally labeled but pragmatically under-specified. |
| **CC-DRR.1e (current disposition map and content obligations)** | The Decision **MUST** name the selected loci and what each selected locus must say, including the first subject kind and action guidance expected in drafting when a pattern is selected. For every consequential part of the selected answer and every content question that the accepted grounds explicitly assign to this DRR, the Decision **MUST** record a current disposition: `selected now`, `rejected now`, `inherited unchanged`, or `outside current decision with named locus or decision record`. Boundary and non-obligation lists **MUST NOT** be handed to later drafting as copied negative doctrine. If an explicit strict-distinction claim, a pattern defining or constraining the claim, relation or boundary, or a ToC/navigation entry already carries the content, the Decision **MUST** classify it as a single pointer or leave it out of the distribution unless a documented local confusion requires a new, specific stop condition. The author **MUST** apply `F.19` before proposing wording for selected patterns; boilerplate stays outside pasteable pattern prose, and remaining content that still hides precision must name the applied `E.10`, `E.10.ARCH`, `F.18`, `F.19`, or governing pattern. Pattern application and selected-locus disposition **MUST** remain declarative content distribution, not architecture-placement memo. A named pattern is admissible only when its exact contribution to the distinction, claim boundary, relation, row shape, or naming decision is stated. For a named pattern or selected non-pattern FPF kind-reference pair in the distribution question, the Decision **MUST NOT** defer its disposition with wording such as `most likely`, `may need`, or `if later touched`. | Keeps tentative placement from passing for a content decision and keeps DRR boundary maps out of a pattern Solution. |
| **CC-DRR.1e2 (kind-restoration for proposed wording).** | When the DRR proposes changed wording for an FPF-qualified phrase, compare the pre-repair and post-repair object kind, relation or claim kind, live ontic slot or relation position, use, admissible scope, and practitioner action. If the wording changes kind, narrows or widens the object, collapses several kinds, treats a slot or use relation as a kind, or loses a live distinction, the DRR **MUST** record the accepted semantic decision by value or leave the wording as a blocking finding. When another pattern defines or constrains the live distinction, state its concrete contribution and cite it; require an exact claim-bearing episteme or `ClaimGraph` only when the receiving use depends on that identity. | Prevents DRR wording proposals from laundering ontology changes as editorial cleanup without imposing unused formal identity. |
| **CC-DRR.1f (reusable-content disposition when triggered)** | When accepted decision grounds expose a potentially reusable selected non-pattern FPF kind-reference pair or neighboring source-use, evidence, assurance, validation, or architecture-decision mechanism, the DRR **MUST** record whether it is generalized now, kept local with reason, rejected, or placed outside the current decision with named locus or decision record. | Prevents unexamined inheritance of local source-use publications, evidence records, assurance records, validation views, or architecture-decision relations. |
| **CC‑DRR.1g (source-loss and recoverability template when triggered)** | If the decision declares a source-loss mode, simplification, redaction, summarization, or other source-to-rendering loss, the DRR **MUST** make explicit the preserved distinctions, dropped distinctions, admissible uses, non-admissible downstream uses, recoverability class, and reopen or stop rule. | Prevents rhetorical smoothing from masquerading as stable content. |
| **CC‑DRR.1h (naming and ontology adequacy)** | A conforming DRR **MUST** make the selected head, branch, object, governed action, and outside-work separation recoverable by value and **MUST** expose any plausible assignment to the wrong pattern or non-pattern FPF kind-reference, or an `F.18` naming obligation, when it materially affects the decision. | Prevents semantically important naming and typing choices from being rediscovered later during pattern drafting. |
| **CC‑DRR.1i (existing-pattern sufficiency or new-pattern necessity is explicit)** | When a load-bearing selected answer could plausibly belong in an existing pattern, an existing selected non-pattern FPF kind-reference pair, or a proposed new locus, the DRR **MUST** make that sufficiency/necessity judgement by value and **MUST** explain why rejected options would misplace, overload, or falsely split the selected locus that governs the selected answer. | Prevents carrier selection from being rediscovered during downstream drafting. |
| **CC‑DRR.1j (selected-answer stability boundary is explicit)** | The Decision or Consequences **MUST** make clear which elements of the selected answer are fixed now for later FPF drafting and which later elaborations may strengthen wording, examples, source-use rows, or validation evidence without reopening the selected answer. | Prevents later drafting from silently widening or re-deciding the accepted answer. |
| **CC-DRR.1k (source-use result is explicit).** | When a source-borne method, architecture claim, accepted ground, or reusable passage shapes the decision, the DRR **MUST** state how it is used: quoted by value, narrowed, instantiated, decision-bearing, draft guidance, example-only, or retired. It also states any material meaning loss or addition in scope, relation, evidence path, admissible use, reader use, or recoverability. Name the exact source episteme, publication, and source-use relation when the decision or a named later reliance depends on those identities. | Blocks free paraphrase without making every source use start from a ClaimGraph or turning the source into a second canon. |
| **CC‑DRR.2** | The Rationale compares only material alternatives and records the load-bearing effects of the relevant Pillars and Principle-Taxonomy lenses. It **MUST NOT** preserve a ritual paragraph for every Pillar or lens when that item did not change the answer, boundary, or reopen condition. | Keeps cross-disciplinary alignment without turning completeness into a negative catalogue. |
| **CC‑DRR.3** | The DRR **SHALL** name the selected loci, the positive obligation each carries, and every direct consumer whose meaning must move in the same increment. It names a tempting outside locus only when that exclusion explains the answer, boundary, or reopen condition; it does not build an exhaustive impact catalogue. | Preserves dependency closure while keeping the positive decision readable. |
| **CC‑DRR.3a (practical and validation consequences are explicit)** | The Consequences account **MUST** expose the practical change in use, practical gains/costs, affected patterns and selected non-pattern FPF kind-reference pairs, and any outstanding obligation to validate the selected content, including the evidence it requires, or any authority or release consequence that constrains the decision. | Prevents consequences from collapsing into generic optimism or process-order prose. |
| **CC-DRR.3b (SoTA shapes the decision when load-bearing)** | When SoTA or competitive positioning is load-bearing, the DRR **MUST** make the current SoTA source-use line recoverable under E.8, state why it is current best-known problem-solving practice for the DRR decision question rather than merely official, recent, popular, or familiar, and state any uncertainty that would materially change the decision. A literature overview that does not shape the selected answer, boundary, or validation evidence obligation is non-conforming. | Keeps SoTA from becoming decorative appendix material or prestige-source substitution. |
| **CC‑DRR.4** | When a separately authorized selected answer is realized, dated authoring work **SHALL** incorporate its normative Decision content into the selected Core loci and **MAY** distill rationale/consequences/SoTA/grounding into informative loci. The DRR records the answer; it neither authorizes nor performs realization, and no new normative constraint may be invented outside the recorded answer. | Preserve Core authority and the record/work/result boundary. |
| **CC-DRR.4a (separate-law content proliferation is blocked)** | If the DRR needs compact law/check content, it **SHOULD** keep that content as a decision-law section or as obligations on selected existing amendment targets. It **MUST NOT** mint a separate `law sheet`, `profile`, selected non-pattern FPF kind-reference pair, or checklist unless the DRR selects and identifies that separate non-pattern FPF kind-reference pair and shows that it does not duplicate the DRR or selected amendment targets. | Prevents unnecessary separate source-use, validation, or shadow-law proliferation. |
| **CC‑DRR.4b (current decision object remains singular)** | A conforming DRR **MUST** remain one current content decision object. It **MUST NOT** carry process-order/gate/handoff/process state, mutable status, or hidden same-decision future-planning language; any undecided remainder **MUST** be marked outside the current decision with named locus or decision record. | Keeps the DRR ontologically about the FPF decision rather than about the development container. |
| **CC-DRR.4c (downstream authoring stays inside the separately accepted decision)** | Realization work **MAY** elaborate examples, SoTA-Echoing, recognition, wording, and neighboring fit inside the selected stability boundary, but **SHALL NOT** revise the selected answer, loci, outside boundary, reusable-content disposition, or loss/recoverability regime. Such a revision needs a successor decision result and DRR episteme. | Keep later drafting from re-deciding by drift. |
| **CC-DRR.4d (major decision gaps are not left to drafting-time invention)** | A conforming DRR **MUST NOT** leave material selected-answer branch choices about the EntityOfConcern, selected loci, outside-current-decision boundary, reusable-content disposition, or loss/recoverability regime for later authors to decide separately in a pattern or selected non-pattern FPF kind-reference pair. Those choices **MUST** already be selected, rejected, inherited unchanged, or placed outside the current decision with named locus or decision record. | Lets authors distribute one bounded answer without having to decide it again at each locus. |
| **CC‑DRR.5** | A DRR for minor, non‑substantive edits (Δ‑0/Δ‑1; e.g., typos, wording clarity, didactic rearrangements) **MAY** use a lightweight variant containing Problem‑frame (Context) + Decision only (“no semantic change”), provided it does not alter semantics. | Avoids bureaucratic drag on editorial work. |
| **CC‑DRR.6 (evidence boundary)** | For a material pattern change, the DRR **SHALL** state the content-scope or validation-evidence obligation that bears on the decision, and it **MAY** summarize already available decisive evidence by value when that evidence materially shapes the chosen content. The DRR **SHALL NOT** need a change-account id, run-manifest id, gate id, packet id, or authoring-evidence citation in order to count as complete; those remain in the relevant source, evaluation, authoring, review, or landing result. If later source, authoring, or refresh evidence motivates reopening or revising the decision, that evidence belongs in a successor DRR or other named successor decision record rather than being retrofitted into the accepted DRR. | Keeps the DRR a design-rationale record while preserving re-runnable evidence in the source or result responsible for it. |

### E.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | Why it fails | Repair |
|---|---|---|---|
| **Process brief disguised as DRR** | The record explains baton movement, packet state, review timing, or current campaign state. | It describes development process rather than the FPF content decision. | Remove mutable process state and keep only the decision grounds, selected answer, alternatives, and consequences. |
| **Shadow specification** | The DRR becomes the only place where stable semantics, examples, source-use rules, or validation rules remain after the Core has moved. | Later FPF readers cannot use the decision because it never became pattern content. | Distribute enduring content into the selected loci; leave the DRR as provenance. |
| **Four-label shell** | The record has Problem frame, Decision, Rationale, and Consequences headings, but no decision grounds, use-value, alternatives, content distribution, or impact account by value. | The minimum kernel is labeled but not substantively recoverable. | Fill the decision-inspection content blocks needed for the decision, or use the lightweight variant only for `Delta-0` / `Delta-1` edits that preserve semantics. |
| **Tentative carrier list** | The DRR says a pattern may need work later, is most likely affected, or should be watched if touched. | A named distribution question is postponed while pretending to be decided. | Classify each named pattern or selected non-pattern FPF kind-reference pair now: selected, rejected, inherited unchanged, or outside the current decision with a named record. |
| **Loss without use/reopen rule** | The decision summarizes, redacts, simplifies, or otherwise declares a source-loss mode but does not state admissible use, non-admissible downstream use, recoverability, and reopen conditions. | A representation with undeclared source loss can be used as if it were the full source. | Add the source-loss and recoverability template: preserved distinctions, dropped distinctions, admissible uses, non-admissible uses, recoverability class, and reopen or stop rule. |
| **Free paraphrase import** | The DRR restates a source-borne method, architecture claim, accepted decision-ground item, or reusable source passage in smoother prose but does not say whether it quoted, narrowed, instantiated, used as decision grounds, turned into draft guidance, kept example-only, or retired the source use. | The paraphrase can widen, weaken, or redirect the source while appearing to preserve it. | State the source-use result and loss and addition account, or keep the passage as a quotation or an example-only source named by value. |
| **Decorative SoTA appendix** | Sources are listed after the fact or treated as SoTA because they are official, recent, popular, or famous, but they do not change the selected answer, boundary, or validation obligation. | The record looks researched while the decision remains unchallenged by current best-known practice. | State what each load-bearing source makes the decision adopt, adapt, or reject, why it is current under E.8, and which uncertainty would materially change the answer. |
| **Negative catalogue as the decision** | Discussion history, every rejected option, every Pillar, and every taxonomy lens occupy more space than the positive answer and first drafting action. | Authors must reconstruct the selected move from exclusions and ritual coverage. | Keep only alternatives and lens effects that explain the selected answer, boundary, or reopen condition. Leave the rest outside the current DRR; retain it elsewhere only when a named later use needs that history. |
| **Proxy replay for a broad rule** | A schema, invented fact pack, lane comparison, or checklist is used to justify a rule that will rewrite practitioner-facing hosts. | The tested proxy can stay usable while the actual host entry, action, result, or burden degrades. | Replay the complete proposed rule on a real host, its proposed replacement and their direct consumers before fanout. |
| **Record as work or authority** | A filled, approved-looking, published, or adequate-looking DRR is said to have made the decision, passed review, authorized Core change, or performed realization. | Method, work, result, episteme, assessment, status/authority, and downstream change collapse. | Recover only the distinctions the current claim needs; let the DRR record rather than perform them. |

### E.9:9 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Recoverable decision grounds** – each semantic normative change carries its selected answer and reasons. | Adds deliberate friction; mitigated by CC‑DRR.5 (Δ‑0/Δ‑1 lightweight) and CC‑DRR.1a (pointer‑based DRRs). |
| **Inspectable decision** – comparing Pillar effects, alternatives, scenarios, and usefulness exposes the grounds and conflicts. | Authors must resolve the content decision before distribution so later drafting can use it. |
| **Institutional memory** – earlier reasons remain available when an alternative is reconsidered. | The growing DRR archive needs a usable index. |
| **Executable downstream authoring** - selected loci, outside-boundary, reusable-content decisions, selected-answer stability, and remaining validation evidence obligation are explicit enough for later drafting/landing without semantic invention. | Richer DRRs need discipline to avoid becoming shadow specs or process briefs; mitigated by CC-DRR.1b, CC-DRR.4a, CC-DRR.4b, CC-DRR.4c, and CC-DRR.4d. |

### E.9:10 - Rationale
FPF evolves through explicit, reviewable decisions rather than silent edits. The DRR is the minimum structured argument and, when several loci must move together, a temporary convergence record. This keeps P-10 Open-Ended Evolution compatible with P-1 Cognitive Elegance and P-2 Didactic Primacy. Exact method, work, result, episteme, assessment, and authority distinctions remain available when a current claim depends on them; they do not precede or replace the readable decision.

Every nontrivial conforming DRR must make Problem frame, Decision, Rationale, and Consequences recoverable. It may also carry the coordination content that prevents shadow documents or new decisions being invented during distribution to Core patterns and selected non-pattern FPF kind-reference pairs.

The minimum includes what authors and reviewers would otherwise have to reconstruct: exact grounds, use-value, the first-minute working situation, scenario, alternatives and current dispositions, naming or ontology obligations, content distribution, whether an existing pattern suffices or a new one is needed, overlap, stability of the answer, the graph of impacts and boundaries, practical payoff, and uncertainties that could change the decision.

Pointer-based DRRs (CC‑DRR.1a) prevent duplicated prose, and distribution
into Core patterns and selected non-pattern FPF kind-reference pairs (CC‑DRR.4) keeps the specification itself learnable
without turning the DRR into a permanent shadow canon. Process-law ordering,
gate, and handoff records stay outside because they are not part of the
content answer that FPF is selecting.

### E.9:11 - SoTA-Echoing

`E.9` draws on established decision-record and design-rationale practices. A cited standard or template does not establish current SoTA for every FPF decision. The DRR selects current problem-owning evidence under E.8 when that evidence is load-bearing. Its distinctive contribution is a decision-rationale record for one bounded FPF content decision, with enough by-value rationale to distribute durable content without making the record a shadow specification.

[MADR's template](https://adr.github.io/madr/decisions/adr-template.html) connects context, considered options, a justified decision and consequences; its confirmation section is optional. E.9 retains this concise rationale function. When one FPF decision changes several loci, it additionally assigns their content obligations and the conditions under which authors can use the selected answer. A longer record is useful only for those remaining dependencies.

[ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html) distinguishes an entity's architecture from its description and leaves architecting processes and recording media outside its scope. E.9 likewise keeps its decision record distinct from the selected architecture and the work that realizes it; the standard does not supply the FPF content decision or its admission result.

To improve the choice of content when a decision has substantial semantic consequences, the deciding work settles the answer, alternatives, losses, boundary, and loci. The DRR episteme lets another author replay that selection before drafting. Any durable rule, example, or obligation useful after realization belongs in the selected FPF pattern or non-pattern kind-reference pair, not in the DRR as permanent shadow canon.

When an identified source shapes the answer—for example a prior decision, standard, plan, or review packet—the DRR records how it is used and which payload is selected or left behind, including any material loss, destination locus, stop or return, reopen condition, and non-use boundary admitted by `F.19`'s grounded-contribution test. Name the exact source episteme, publication, and source-use relation when the decision or a named later reliance depends on those identities. A citation supplies traceability; every stronger receiving claim needs its direct result or relation.

### E.9:12 - Relations

* **Instantiates:** P‑10 Open‑Ended Evolution, P‑2 Didactic Primacy
* **Pattern publication form governed by:** E.8.
* **Interacts with:** E.5.4 for the lens check.
* **Complemented by:** `E.9.DA` when a particular DRR must be checked for a declared downstream authoring use. An ordinary bounded review judges the decision and returns precise findings or repaired text; a complete coordinate result and its exact assessment identities are added only when expressly requested or needed by a named later reliance. E.9.DA is not a second DRR form, review gate, acceptance status, or mandatory editorial step. E.12 separately governs didactic clarity, rationale and review of cognitive workload.

* **Coordinates with:** `E.23` for repeated improvement work on a DRR; C.2.1 for DRR and evaluation-result episteme identity; C.2.P/A.10/G.6 for exact source use and provenance; A.15.1 for performed decision, assessment, and realization Work; A.6.1 when a claim depends on an independently identified application of a declared mechanism operation; F.10/G.11 for status and currentness; E.24.PUB for publication; and C.29 for a mathematical-lens use when such a lens is used. None of these neighboring records or results changes the E.9 selected answer by implication.

### E.9:End
