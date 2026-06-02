## E.9 - Design‑Rationale Record (DRR) Method

> **Type:** Governance and authoring pattern
> **Status:** Stable
> **Normativity:** Normative

### E.9:0 - Use this when

- one proposed normative change needs an explicit by-value account of what FPF should say, why this decision is preferred, and which neighboring patterns or selected non-pattern FPF kind-reference pairs it affects
- several patterns or selected non-pattern FPF kind-reference pairs must move together and one external decision record is needed to keep one bounded coordinated change set (one mutually dependent change set) semantically complete while enduring Core text is redistributed
- one bounded content decision question would otherwise force authors to decide the same load-bearing answer separately across several patterns or selected non-pattern FPF kind-reference pairs
- one deprecation, narrowing, or cross-pattern amendment must stay reviewable without reconstructing intent from patch history, chat memory, or scattered notes

**Not this pattern when.** Do not use `E.9` as the permanent location of normative Core law, as a campaign or process brief, or as the main vehicle for purely editorial `Delta-0` or `Delta-1` cleanup that fits the lightweight variant in `CC-DRR.5`. Use `E.9.DA` when one concrete `DRR` already exists and the live question is whether its selected answer, receiving-locus obligations, source use, lexical closure, and drafting actionability are adequate for a declared downstream authoring use.

### E.9:0.1 - What goes wrong if missed

- Core text changes without one explicit rationale account, so later readers cannot recover which alternatives were rejected or which exclusions were intentional
- coordinated multi-pattern amendments drift apart because the temporary selected-answer account survives only in patches, handoffs, or reviewer memory
- future repairs overfit to local wording and silently lose Pillar, taxonomy-lens, impact-graph, practical-use, or pattern-placement discipline

### E.9:0.2 - What this buys

- one external decision record that states the bounded FPF change by value before Core text is rewritten
- one minimum kernel that keeps Problem frame, Decision, Rationale, and Consequences recoverable for later review and replay
- one temporary convergence record for coordinated changes, while keeping enduring Core text in the selected patterns and selected non-pattern FPF kind-reference pairs rather than in the DRR
- one temporary convergence record that fixes the selected answer (the chosen content answer for the bounded content decision question) before later drafting fans out across several selected patterns or selected non-pattern FPF kind-reference pairs

**First useful move.** State the bounded FPF content decision question, the selected answer, the rationale for that answer, and the selected distribution across patterns or selected non-pattern FPF kind-reference pairs before drafting or landing the Core text.

**Cheap stop.** If the live change is ordinary local wording repair, application of an already accepted pattern, or editorial cleanup that does not change FPF semantics, obligations, boundaries, names, admissible uses, or normative force, do not open a full DRR. Use the lighter governing pattern for the local repair: `E.17.AUD.LHR` for one overloaded local lexical head inside one publication unit, `C.2.P` for one episteme, publication, or source-transfer phrase requiring local epistemic precision restoration, `E.10` for general lexical repair, `F.18` only when a durable reusable name is being minted, and `E.8` for authoring-form correction. Leave `E.9` for bounded content decisions that need rationale by value.

**Governed object in plain terms.** The governed object here is one external decision-rationale record for one bounded FPF content decision or one bounded coordinated change set. The minimal lens is simple: the record must keep the problem frame, decision, rationale, consequences, and impact and boundary account recoverable enough that accepted content can be distributed into the selected Core patterns and selected non-pattern FPF kind-reference pairs without semantic invention.

**Primary working reader.** The first working reader is an FPF author, reviewer, or steward who must evaluate, challenge, or land one bounded content decision. Downstream pattern readers benefit from the landed Core text; they are not the primary reader of the DRR itself.

### E.9:1 - Problem frame
FPF is engineered for Pillar **P‑10 Open‑Ended Evolution**: its normative
rules must adapt as new calculi and insights arrive. But change without a
record of *why* leads to conceptual erosion and undermines auditability.
Hence FPF requires an explicit **Design‑Rationale Record (DRR)**—a
durable *conceptual record* that precedes every normative change.

### E.9:2 - Problem
Direct edits to the Core, absent a structured rationale, trigger three
systemic hazards:

1. **Lost provenance** – future authors cannot infer the reasoning behind
   a rule; intent decays.
2. **Implicit assumptions** – discarded alternatives vanish from memory,
   so debates resurface and churn repeats.
3. **Conceptual drift** – incremental tweaks slip past the Eleven Pillars
   and Principle Taxonomy lenses, blurring the framework’s foundations.

### E.9:3 - Forces

| Force | Tension |
|-------|---------|
| **Agility vs Rigour** | Evolve swiftly ↔ demonstrate deliberate, Pillar‑aligned decisions. |
| **Transparency vs Efficiency** | Provide a public argument trail ↔ avoid bureaucratic drag on minor edits. |
| **Clarity vs Conciseness** | Capture enough reasoning and coordinated implications ↔ prevent meta‑text from bloating the Core itself. |

### E.9:4 - Solution — the DRR as a structured argument and temporary convergence record
Any proposal to add, modify or deprecate a `NORM`, `A`, `D`, or `GOV`
rule **MUST** be accompanied by a **Design‑Rationale Record**. By default,
a conforming DRR contains at least four conceptual components (below);
these form the minimum decision kernel recoverable by any conforming DRR.
A lightweight editorial variant is permitted by CC‑DRR.5.

In this pattern, a **bounded coordinated change set** means one bounded
group of mutually dependent content decisions whose enduring FPF
expression will be distributed across several patterns or selected non-pattern FPF kind-reference pairs.
In this pattern, the **selected answer** means the current set of chosen
content decisions for that bounded content decision question: what FPF should say, which
selected patterns or selected non-pattern FPF kind-reference pairs carry it, what stays outside, and what support or
loss/recoverability regime applies.
In this pattern, **selected non-pattern FPF kind-reference pair** is a tuple-like instruction, not one new kind: when a DRR selects a non-pattern publication, view, record, or relation to carry durable content, it must name the exact FPF kind and exact reference by value, for example pattern profile, `U.View`, source map, support note, authoritySourceRef target, evidence-basis record, review-basis record, or architecture-basis record.
In this pattern, a **temporary convergence record** means one external
decision record that temporarily holds the selected answer while
the selected Core patterns and selected non-pattern FPF kind-reference pairs are still being updated.

A nontrivial DRR may therefore govern one bounded coordinated change set.
In that case the DRR is the temporary convergence record for the selected
answer until selected Core patterns and selected non-pattern FPF kind-reference pairs are updated; it is not a second
permanent Core-law section.

| Minimum-kernel component | Guiding question | Typical content |
|-----------|------------------|-----------------|
| **Problem frame** | *Why are we talking about this?* | Problem statement, triggering insight, intended FPF use-value, scenario basis, or external change. |
| **Decision** | *What will we do?* | Precise normative text, selected content distribution, explicit outside-current-decision disposition, or other substantive change law to enter the specification. |
| **Rationale** | *Why is this the right thing?* | Comparison of alternatives, Pillar check, taxonomy-lens balance, architecture/usability/SoTA grounds. |
| **Consequences** | *What follows from this choice?* | Expected benefits, trade-offs, impacted patterns and selected non-pattern FPF kind-reference pairs, practical gains/costs, and remaining validation evidence obligation. |

#### E.9:4.1 - Minimum decision-support content blocks

A conforming DRR must also make the following decision-support content blocks
recoverable. They may live inside the four kernel components or inside one
dedicated `Basis used` / decision-support block, but they are part of
substantive DRR adequacy rather than later review-only hardening.

| Decision-support content block | What must be recoverable by value | Usual location in the DRR |
|---|---|---|
| **Exact substantive basis and governing inheritance** | Exact basis sources and inherited architecture/audit basis that materially govern the decision, plus any still-live uncertainty not already closed by that basis. | Header or `Basis used`, with Problem frame/Rationale support. |
| **Purpose, utility, and scenario basis** | Intended FPF use-value, first-minute working situation, minimum scenario/anti-case basis, and compact utility/fitness reading. | Problem frame. |
| **Alternatives and current disposition map** | Material alternatives plus one current disposition for each still-live content decision question this DRR must settle: `selected now`, `rejected now`, `inherited unchanged`, or `outside current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record`. When the accepted basis or the DRR itself already names one pattern or selected non-pattern FPF kind-reference pair as part of the live distribution question, that named pattern or selected non-pattern FPF kind-reference pair is already part of the current disposition map and must not remain one conditional watch item. | Decision and Rationale. |

| **Content-distribution and outside-boundary map** | For each load-bearing selected answer: selected patterns and selected non-pattern FPF kind-reference pairs, exact content obligations on each selected pattern or selected non-pattern FPF kind-reference pair, which nearby patterns or selected non-pattern FPF kind-reference pairs stay unamended under the current decision, and any agreement across selected patterns and selected non-pattern FPF kind-reference pairs that those selected patterns and selected non-pattern FPF kind-reference pairs must preserve. Named nearby patterns or selected non-pattern FPF kind-reference pairs must be classified now, not left as tentative `most likely` / `may need` / `if later touched` watch prose. | Decision. |

| **Existing-pattern sufficiency and new-pattern necessity** | For each load-bearing selected answer, whether one already-existing pattern is sufficient, one already-existing selected non-pattern FPF kind-reference pair is sufficient, or one newly selected pattern or selected non-pattern FPF kind-reference pair is necessary, and why rejected options would misplace, overload, or falsely split the pattern or selected non-pattern FPF kind-reference pair that governs the selected answer. | Decision and Rationale. |
| **Naming, ontology, and wrong-carrier-confusion account** | Head/branch/object/move/outside-work separation, tempting wrong-pattern assignment or wrong non-pattern FPF kind-reference assignment, and any load-bearing `F.18` naming obligation needed to keep the selected answer truthful by value. | Problem frame, Decision, and Rationale. |
| **Reusable-support disposition when triggered** | Whether a potentially reusable selected non-pattern FPF kind-reference pair remains local, is generalized now, is rejected, or is placed outside the current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record. | Decision and Rationale. |
| **Loss and recoverability template when source-loss or scope narrowing is declared** | Preserved distinctions, dropped distinctions, admissible use, non-admissible downstream use, recoverability class, and reopen/exit rule. | Decision and Consequences. |
| **Selected carrier and neighbor-boundary account** | Why the selected patterns and selected non-pattern FPF kind-reference pairs carry the content, which tempting patterns or selected non-pattern FPF kind-reference pairs stay outside, and which neighboring pattern assignments remain authoritative. | Decision and Rationale. |
| **Convergence and overlap account when several content-decision branches touch the same carrier set** | Whether overlap is valid convergence or one reopened architecture smell, what agreement across selected patterns and selected non-pattern FPF kind-reference pairs must hold, and whether a new pattern or selected non-pattern FPF kind-reference pair is actually selected or refused now. | Decision and Consequences. |
| **Selected-answer stability boundary** | Which elements of the selected answer are fixed now for later FPF drafting, and which later elaborations may strengthen wording, examples, or support without reopening the selected answer. | Decision and Consequences. |
| **Impact, practical gains, and remaining validation evidence obligation** | Affected patterns and selected non-pattern FPF kind-reference pairs, practical gains/costs, authority or release consequences when they follow from the content decision, and the remaining validation evidence obligation that still constrains later authoring or landing. | Consequences. |
| **SoTA and competitive-positioning account when load-bearing** | Current best-known problem-solving anchors under E.8 that discipline the decision, what problem-owning domain or practice they answer to, which official/popular/legacy alternatives they reject or bound when live, and what unresolved uncertainty would materially change the selected answer. | Problem frame, Rationale, and Consequences. |

These decision-support content blocks are not separate process paperwork. A DRR that keeps
only the four labels while leaving basis, first-minute use question, naming,
selected content distribution, pattern or selected non-pattern FPF kind-reference pair sufficiency or necessity, overlap handling, impact,
or live uncertainty implicit is structurally labeled but still
substantively immature.

Together these decision-support content blocks let the DRR act as one decision record
for one bounded coordinated change set: enough semantic closure that later
drafting distributes the selected answer into selected patterns and selected non-pattern FPF kind-reference pairs rather than
inventing it for the first time pattern by pattern.

When one bounded decision coordinates several patterns or selected non-pattern FPF kind-reference pairs, or one cluster of mutually dependent pattern edits and selected non-pattern FPF kind-reference pair edits, the DRR **MAY**
carry additional substantive sections beyond that minimum kernel. Typical substantive additions include obligations on selected patterns and selected non-pattern FPF kind-reference pairs, one explicit
new-pattern vs existing-pattern decision, one impact or non-goal map across selected patterns and selected non-pattern FPF kind-reference pairs, coverage or agreement maps across selected patterns and selected non-pattern FPF kind-reference pairs, convergence
classification, and one provisional decision-law account by value that
keeps the bounded change account semantically complete until enduring
Core text is distributed.

Such additions do not change the DRR’s kind. A DRR carrying them remains
conforming only when it stays about the FPF content decision: what FPF should
say, why, what is excluded, how selected patterns and selected non-pattern FPF kind-reference pairs are
affected, and what practical use or authoring action improves. A DRR carrying richer
convergence content **MUST NOT** become a campaign plan, process script,
baton carrier, packet checklist, staging log, or other development-process
brief.

When one selected answer could plausibly fit one already-existing pattern or selected non-pattern FPF kind-reference pair
or require one newly proposed pattern or selected non-pattern FPF kind-reference pair, the DRR must decide that
sufficiency/necessity question by value. It is not enough to list a
tentative carrier list or leave downstream drafting to discover the selected pattern or selected non-pattern FPF kind-reference pair later.

When the accepted basis or the DRR itself already names one pattern or
selected non-pattern FPF kind-reference pair as part of the live distribution question, that
pattern or selected non-pattern FPF kind-reference pair is not a neutral future watch item. The DRR
must classify it now either as one selected pattern or selected non-pattern FPF kind-reference pair
with explicit obligation, one explicit boundary neighbor kept unchanged,
one inherited-unchanged neighbor, or one outside-current-decision item
with named pattern, selected non-pattern FPF kind-reference pair, or decision record. Conditional or
time-relative pattern prose or prose for one selected non-pattern FPF kind-reference pair such as `most likely`, `may need local
hardening`, `if later touched`, `watch later`, or one equivalent
placeholder is non-conforming there because it marks one unmade current
decision rather than one explicit current disposition.


When one accepted basis exposes one potentially reusable selected non-pattern FPF kind-reference pair or neighboring support mechanism, the
DRR must not merely note that such support already exists. It must decide
whether that support is generalized now, kept local with a substantive
reason, rejected, or marked outside the current decision with a named pattern, selected non-pattern FPF kind-reference pair, or decision record.

When one selected answer involves source-loss mode, simplification, redaction,
summarization, or other declared loss, the DRR must make the admissible-use template explicit by value. Explanation alone is not enough; the decision
must say what remains preserved, what is dropped, which branch reading is admissible and which selected non-pattern FPF kind-reference pair carries it, which uses are unsupported, what recoverability class
applies, and what reopen or exit rule governs cases that exceed the
declared source-loss or scope-narrowing posture.

A nontrivial DRR is mature enough for downstream authoring only when
materially live selected-answer branch choices about the governed object, selected patterns and selected non-pattern FPF kind-reference pairs, outside-current-decision boundary, reusable-support disposition,
and loss/recoverability regime have already been selected, rejected,
inherited unchanged, or placed outside the current decision with a named pattern, selected non-pattern FPF kind-reference pair, or decision record. If those choices are still missing, the DRR is still basis work
rather than one accepted design-rationale record.

The DRR lives **outside** the normative Core. An accepted DRR **SHALL** be
landed by applying its Decision account and any stabilized enduring
content to the relevant pattern or selected non-pattern Core kind-reference pair as explicit
normative or informative text (the change is "in the Core"; the DRR is
not). A richer DRR **MAY** remain the temporary convergence record while
redistribution into selected Core patterns and selected non-pattern FPF kind-reference pairs is still incomplete, but it
**SHALL NOT** remain the permanent sole semantic carrier once landed Core text
exists.

Authors drafting from an accepted DRR **MAY** elaborate examples,
SoTA‑Echoing, recognition surfaces, local wording inside the selected patterns and selected non-pattern FPF kind-reference pairs, and neighboring fit. They **SHALL NOT** silently revise the selected answer, selected patterns and selected non-pattern FPF kind-reference pairs, outside-current-decision boundary, reusable-support disposition, or
declared loss/recoverability regime. Any such revision **SHALL** be handled
through one successor DRR or other named successor decision record.

A `DRR` may itself be improved through `E.23`, but the `DRR` remains the selected decision record, not a full pattern draft. When SoTA is load-bearing in that improvement, it must mutate the selected answer, receiving-locus obligation, boundary, example, validation obligation, or reopen condition; otherwise it is rationale-only or lineage-only for the DRR.


To preserve **P‑2 Didactic Primacy** without duplicating meta‑text,
authors landing an accepted DRR **SHOULD** distill stable and reusable
parts of its *Rationale*, *Consequences*, and other valid convergence
sections into the appropriate **informative** sections of the affected
pattern(s) (Rationale, Consequences, SoTA‑Echoing, Archetypal Grounding;
per the Pattern Template, E.8). The full DRR remains external as
provenance.

A substantive DRR is one current content decision object. It may carry
selected content obligations only when they are part of the
Decision or Consequences. It **MUST NOT** carry next-gate posture,
handoff/packet state, process-order state, monolith status, future campaign
planning, or one hidden promise that the same current content decision question will be
decided later inside the same decision object. Any undecided remainder must
be marked outside the current decision with a named pattern, selected non-pattern FPF kind-reference pair, or decision record.

#### E.9:4.1a - Process-source method admission into FPF

When a `DRR` imports stable method from process-source document-carried method description into `FPF`, it must decide the admission by value rather than treating process prose as a second canon.

The `DRR` names:

- the exact process-source passage or accepted process-source basis being considered;
- the reusable FPF method recovered from that passage;
- the current FPF pattern, section, or accepted `DRR` that already carries the method, if any;
- the remaining delta that current FPF does not yet carry;
- the receiving FPF pattern selected to carry that delta;
- process-control material excluded from FPF pattern prose, such as role dispatch, seam state, helper behavior, Git recovery, packet transport, review transport, chat cadence, and mutable release posture;
- the source-use result for that passage or basis: exact quote, narrowed scope, instantiated case, decision-bearing use, draft-guidance source, example-only use, or retired source use;
- any meaning loss or addition created by that source-use result: changed scope, relation, evidence basis, admissible use, non-admissible use, reader move, or recoverability condition;
- the first improved FPF use that the admitted method gives to an author, reviewer, or downstream FPF user;
- the current disposition: selected now, inherited sufficient, rejected now, or outside the current decision with the named evaluation pattern, accepted `DRR`, or accepted basis named by value.


Reusable process-source method is not limited to semio wording or pattern-authoring language. It may enter FPF only when it is separable from local process mechanics, improves FPF use, and has one exact evaluation pattern. After the method lands in FPF, process documents should cite the receiving FPF pattern instead of keeping a parallel long-form rule.
### E.9:5 - Archetypal Grounding (System / Episteme)

| Holon flavour | DRR analogue | Minimum kernel illustrated |
|---------------|--------------|-----------------------------|
| **`U.System`** (physical) | Engineering Change Order for pump motor upgrade. | Context: inefficiency and plant-use problem; Decision: switch to brushless DC and update the selected control/maintenance patterns or selected non-pattern FPF kind-reference pairs; Rationale: energy gain vs cost and authority fit; Consequences: new control schema, supplier change, validation evidence obligation. |
| **`U.Episteme`** (knowledge) | Foundational theory revision paper. | Context: conflicting data and explanatory problem; Decision: introduce new axiom and distribute its consequences into the selected theory/teaching patterns or selected non-pattern FPF kind-reference pairs; Rationale: explains legacy & new data, Pillar alignment, alternative rejection; Consequences: fresh predictions, update to curricula, downstream review obligation. |

### E.9:6 - Bias-Annotation

| Lens | Bias risk in DRR use | Mitigation in this pattern |
|---|---|---|
| **Gov** | The DRR can become a bureaucratic approval ritual rather than a decision-rationale record. | Keep `CC-DRR.5` for lightweight editorial changes and require richer DRRs only when the content decision is semantically load-bearing. |
| **Arch** | A rich DRR can become a shadow specification that competes with the selected Core patterns and selected non-pattern FPF kind-reference pairs. | Treat the DRR as temporary convergence support; enduring content is distributed into the selected Core patterns and selected non-pattern FPF kind-reference pairs. |
| **Onto/Epist** | Authors can mix content decisions, evidence basis, process state, and provenance into one ambiguous object. | Require exact substantive basis and selected-answer boundaries while excluding process-order state, baton, packet, and mutable status posture from the DRR. |
| **Prag** | The method adds work before editing Core text. | Allow pointer-based DRRs and require only the selected non-pattern FPF kind-reference pairs materially needed for the selected decision. |
| **Did** | Rationale can become too internal for later authors to use. | Distill stable rationale, consequences, anti-cases, and SoTA implications into informative pattern sections when the Core text is updated. |

Scope: this bias annotation is universal for FPF semantic changes governed by `E.9`. It does not turn project-management state, helper state, or review logistics into DRR content.
### E.9:7 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑DRR.1** | Any Δ‑2/Δ‑3 semantic change set against a `NORM`, `A`, `D`, or `GOV` pattern **SHALL** be backed by an accepted DRR containing at least Problem‑frame (Context), Decision, Rationale, and Consequences. | Prevents undocumented semantic edits while setting a minimum kernel rather than an artificial ceiling. |
| **CC‑DRR.1a** | A DRR whose proposed change is expressed as a new or revised pattern written in the standard template (E.8) **MAY** satisfy that minimum kernel by **pointing to** the corresponding pattern sections rather than duplicating prose. | Avoids “double writing” while keeping the argument recoverable. |
| **CC‑DRR.1b (rich convergence content is permitted)** | A DRR that coordinates several patterns or selected non-pattern FPF kind-reference pairs, or mutually dependent pattern and selected non-pattern FPF kind-reference pair changes, **MAY** include additional substantive sections beyond the minimum kernel—for example obligations on selected patterns or selected non-pattern FPF kind-reference pairs, explicit new-pattern vs existing-pattern decisions, boundary/non-goal maps, coverage or agreement maps across selected patterns and selected non-pattern FPF kind-reference pairs, convergence classification, or one provisional decision-law account by value—provided that the DRR stays about the FPF content decision and **MUST NOT** become process management. | Allows one semantically sufficient convergence record for coordinated changes without forcing mid-distribution invention or extra shadow documents. |
| **CC‑DRR.1c (exact basis is recoverable)** | A conforming DRR **MUST** make its exact substantive basis and governing inheritance recoverable by value, either in one dedicated `Basis used` section or one equivalent header/support block. Routing, status, and provenance records do not count unless their substantive content still governs the decision by value. | Prevents anti-telephone drift and keeps the decision inspectable against its real basis. |
| **CC‑DRR.1d (problem-frame adequacy)** | The Problem frame **MUST** make the intended FPF use-value, first-minute working situation, minimum scenario/anti-case basis, compact utility/fitness reading, and any load-bearing current SoTA / competitive-positioning basis or exact inherited-basis justification recoverable by value. | Prevents a DRR from being formally labeled but pragmatically under-specified. |
| **CC‑DRR.1e (current disposition map and content obligations)** | The Decision **MUST** name the selected patterns and selected non-pattern FPF kind-reference pairs and the content obligations each selected pattern or selected non-pattern FPF kind-reference pair must carry by value. For every load-bearing selected answer and for every still-live content decision question explicitly assigned to this DRR by accepted basis, the Decision **MUST** record one current disposition now: `selected now`, `rejected now`, `inherited unchanged`, or `outside current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record`. When one pattern or selected non-pattern FPF kind-reference pair is already named as part of that live distribution question, the Decision **MUST NOT** leave it in conditional or time-relative pattern prose or prose for one selected non-pattern FPF kind-reference pair such as `most likely`, `may need`, or `if later touched`. | Stops hidden deferral, including conditional/time-relative carrier-list wording, and prevents tentative carrier-list prose from replacing real content decisions. |

| **CC‑DRR.1f (reusable-support disposition when triggered)** | When accepted basis exposes a potentially reusable selected non-pattern FPF kind-reference pair or neighboring support mechanism, the DRR **MUST** decide whether it is generalized now, kept local with reason, rejected, or placed outside the current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record. | Prevents unexamined inheritance of local support publications, records, views, or relations. |
| **CC‑DRR.1g (source-loss and recoverability template when triggered)** | If the decision declares a source-loss mode, simplification, redaction, summarization, or other source-to-rendering loss, the DRR **MUST** make explicit the preserved distinctions, dropped distinctions, admissible uses, non-admissible downstream uses, recoverability class, and reopen or exit rule. | Prevents rhetorical smoothing from masquerading as stable content. |
| **CC‑DRR.1h (naming and ontology adequacy)** | A conforming DRR **MUST** make the selected head/branch/object/move/outside-work separation recoverable by value and **MUST** expose any tempting wrong-pattern assignment or wrong non-pattern FPF kind-reference assignment or load-bearing `F.18` naming obligation that materially affects the decision. | Prevents semantically important naming and typing choices from being rediscovered later during pattern drafting. |
| **CC‑DRR.1i (existing-pattern sufficiency or new-pattern necessity is explicit)** | When a load-bearing selected answer could plausibly live in one already-existing pattern, one already-existing selected non-pattern FPF kind-reference pair, or one newly proposed pattern or selected non-pattern FPF kind-reference pair, the DRR **MUST** make that sufficiency/necessity judgement by value and **MUST** explain why rejected options would misplace, overload, or falsely split the pattern or selected non-pattern FPF kind-reference pair that governs the selected answer. | Prevents carrier selection from being rediscovered during downstream drafting. |
| **CC‑DRR.1j (selected-answer stability boundary is explicit)** | The Decision or Consequences **MUST** make clear which elements of the selected answer are fixed now for later FPF drafting and which later elaborations may strengthen wording, examples, or support without reopening the selected answer. | Prevents later drafting from silently widening or re-deciding the accepted answer. |
| **CC‑DRR.1k (source-use result is explicit).** | When a DRR imports a source-borne method, architecture claim, accepted basis, or other reusable source passage, it **MUST** state how the source is used in the selected answer: exact quote, narrowed scope, instantiated case, decision-bearing use, draft-guidance source, example-only use, or retired source use. It **MUST** also state any meaning loss or addition in scope, relation, evidence basis, admissible use, non-admissible use, reader move, or recoverability condition. | Blocks free paraphrase and makes source movement reviewable without turning source documents into a second canon. |

| **CC‑DRR.2** | A conforming DRR **MUST** include a rationale account that compares the materially live alternatives and assesses the selected proposal against **all Eleven Pillars** and the five Principle‑Taxonomy lenses (`Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`). | Keeps evolution aligned, comparative, and cross‑disciplinary. |
| **CC‑DRR.3** | The DRR **SHALL** list every pattern, selected non-pattern FPF kind-reference pair, or neighboring pattern or selected non-pattern FPF kind-reference pair that it supersedes, amends, excludes from the current decision, assigns to a neighboring pattern or selected non-pattern FPF kind-reference pair, or risks impacting, together with any agreement across selected patterns and selected non-pattern FPF kind-reference pairs the selected patterns and selected non-pattern FPF kind-reference pairs must preserve. It **MUST** also make clear why the selected patterns and selected non-pattern FPF kind-reference pairs carry the content, which tempting patterns or selected non-pattern FPF kind-reference pairs stay outside, and, when several content-decision branches touch the same carrier set, whether that overlap is valid convergence or one reopened architecture smell. | Maintains an explicit impact/boundary graph for coordinated changes. |
| **CC‑DRR.3a (practical and validation consequences are explicit)** | The Consequences account **MUST** expose the practical change in use, practical gains/costs, affected patterns and selected non-pattern FPF kind-reference pairs, and any remaining content-scope validation evidence obligation or authority/release consequence that still constrains the selected decision by value. | Prevents consequences from collapsing into generic optimism or process-order prose. |
| **CC‑DRR.3b (SoTA shapes the decision when load-bearing)** | When SoTA or competitive positioning is load-bearing, the DRR **MUST** make the current SoTA basis recoverable under E.8, state why it is current best-known problem-solving practice for the governed problem rather than merely official, recent, popular, or familiar, and state any uncertainty that would materially change the decision. A literature overview that does not shape the selected answer, boundary, or validation evidence obligation is non-conforming. | Keeps SoTA from becoming decorative appendix material or prestige-source substitution. |
| **CC‑DRR.4** | An accepted DRR **SHALL** have its Decision account landed in the Core as the normative change. When that DRR temporarily carries richer convergence content, authors landing it **SHOULD** distribute any part that stabilizes into enduring FPF content into the relevant Core patterns and selected non-pattern FPF kind-reference pairs. Authors **MAY** distill other DRR sections into **informative** pattern sections (Rationale/Consequences/SoTA‑Echoing/Grounding), but they **SHALL NOT** introduce new normative constraints except via explicit `NORM`/`A`/`D`/`GOV` text. | Preserves Core authority while allowing a richer temporary convergence record. |
| **CC‑DRR.4a (separate-law content proliferation is blocked)** | If the DRR needs compact law/check content, it **SHOULD** keep that content as one decision-law section or as obligations on selected existing amendment targets. It **MUST NOT** mint a separate `law sheet`, `profile`, selected non-pattern FPF kind-reference pair, or checklist unless that separate selected non-pattern FPF kind-reference pair is selected by value and shown not to duplicate the DRR or the selected amendment targets. | Prevents unnecessary separate-support proliferation and shadow-law duplication. |
| **CC‑DRR.4b (current decision object remains singular)** | A conforming DRR **MUST** remain one current content decision object. It **MUST NOT** carry process-order/gate/handoff/process posture, mutable status, or hidden same-decision future-planning language; any undecided remainder **MUST** be marked outside the current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record. | Keeps the DRR ontologically about the FPF decision rather than about the development container. |
| **CC‑DRR.4c (downstream authoring stays inside the accepted decision)** | Authors drafting from an accepted DRR **MAY** elaborate examples, SoTA‑Echoing, recognition surfaces, local wording inside the selected patterns and selected non-pattern FPF kind-reference pairs, and neighboring fit, but they **SHALL NOT** silently revise the selected answer, selected patterns and selected non-pattern FPF kind-reference pairs, outside-current-decision boundary, reusable-support disposition, or declared loss/recoverability regime. Any such revision **SHALL** be handled through one successor DRR or other named successor decision record. | Keeps later pattern drafting from re-deciding bounded content by drift. |
| **CC‑DRR.4d (major decision gaps are not left to drafting-time invention)** | A conforming DRR **MUST NOT** leave materially live selected-answer branch choices about the governed object, selected patterns and selected non-pattern FPF kind-reference pairs, outside-current-decision boundary, reusable-support disposition, or loss/recoverability regime to be discovered case-by-case during later pattern drafting or drafting for one selected non-pattern FPF kind-reference pair. Those choices **MUST** already be selected, rejected, inherited unchanged, or placed outside the current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record. | Ensures the DRR actually coordinates one bounded change set rather than serving as a thin preface to later rediscovery. |
| **CC‑DRR.5** | A DRR for minor, non‑substantive edits (Δ‑0/Δ‑1; e.g., typos, wording clarity, didactic rearrangements) **MAY** use a lightweight variant containing Problem‑frame (Context) + Decision only (“no semantic change”), provided it does not alter semantics. | Avoids bureaucratic drag on editorial work. |
| **CC‑DRR.6 (evidence boundary)** | For Δ‑2/Δ‑3 lexical or authoring-sensitive changes, the DRR **SHALL** state the content-scope evidence or validation evidence obligation that bears on the decision, and it **MAY** summarize already-available decisive evidence by value when that evidence materially shapes the chosen content. The DRR **SHALL NOT** need a LAT id, run-manifest id, gate id, packet id, or other authoring-evidence citation in order to count as complete; those remain in the relevant evidence or authoring record. If later LAT or refresh evidence motivates reopening or revising the decision, that later evidence belongs in a successor DRR or other named successor decision record rather than being retrofitted into the accepted DRR. | Keeps the DRR a design-rationale record while preserving re-runnable evidence in the relevant evidence or authoring record. |

### E.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | Why it fails | Repair |
|---|---|---|---|
| **Process brief disguised as DRR** | The record explains baton movement, packet posture, review timing, or current campaign state. | It describes development process rather than the FPF content decision. | Remove mutable process state and keep only the substantive basis, selected answer, alternatives, and consequences. |
| **Shadow specification** | The DRR becomes the only place where stable semantics, examples, or support rules live after the Core has moved. | Later FPF readers cannot use the decision because it never became pattern content. | Distribute enduring content into the selected patterns and selected non-pattern FPF kind-reference pairs; leave the DRR as provenance. |
| **Four-label shell** | The record has Problem frame, Decision, Rationale, and Consequences headings, but no basis, use-value, alternatives, content distribution, or impact account by value. | The minimum kernel is labeled but not substantively recoverable. | Fill the decision-support content blocks that are live for the decision, or use the lightweight variant only for true `Delta-0` / `Delta-1` edits. |
| **Tentative carrier list** | The DRR says a pattern may need work later, is most likely affected, or should be watched if touched. | A named live distribution question is postponed while pretending to be decided. | Classify each named pattern or selected non-pattern FPF kind-reference pair now: selected, rejected, inherited unchanged, or outside the current decision with a named record. |
| **Loss without use/reopen rule** | The decision summarizes, redacts, simplifies, or otherwise declares a source-loss mode but does not state admissible use, non-admissible downstream use, recoverability, and reopen conditions. | A representation with undeclared source loss can be used as if it were the full source. | Add the source-loss and recoverability template: preserved distinctions, dropped distinctions, admissible uses, non-admissible uses, recoverability class, and reopen or exit rule. |
| **Free paraphrase import** | The DRR restates a source-borne method, architecture claim, accepted basis, or reusable source passage in smoother prose but does not say whether it quoted, narrowed, instantiated, used as a decision basis, turned into draft guidance, kept example-only, or retired the source use. | The paraphrase can widen, weaken, or redirect the source while appearing to preserve it. | State the source-use result and loss and addition account, or keep the passage as an exact quote or example-only support. |


| **Decorative SoTA appendix** | Sources are listed after the fact or treated as SoTA because they are official, recent, popular, or famous, but they do not change the selected answer, boundary, or validation evidence obligation. | The record looks researched while the decision remains unchallenged by current best-known practice. | State what each load-bearing source makes the DRR adopt, adapt, or reject, why that source family is current for the governed problem under E.8, and which uncertainty would materially change the answer. |
### E.9:9 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Complete audit trail** – every semantic normative change carries a structured “why”. | Adds deliberate friction; mitigated by CC‑DRR.5 (Δ‑0/Δ‑1 lightweight) and CC‑DRR.1a (pointer‑based DRRs). |
| **Higher decision quality** – Pillar, alternatives, scenario, and utility checks surface hidden conflicts early. | Authors must do more real content work up front; the gain is less downstream reinvention and less hidden deferral. |
| **Institutional memory** – prevents re‑litigation of rejected alternatives. | DRR archive grows; index stored in a non‑normative annex. |
| **Executable downstream authoring** – selected patterns and selected non-pattern FPF kind-reference pairs, outside-boundary, reusable-support decisions, selected-answer stability, and remaining validation evidence obligation are explicit enough for later drafting/landing without semantic invention. | Richer DRRs need discipline to avoid becoming shadow specs or process briefs; mitigated by CC‑DRR.1b, CC‑DRR.4a, CC‑DRR.4b, CC‑DRR.4c, and CC‑DRR.4d. |

### E.9:10 - Rationale
FPF evolves by **explicit, reviewable deltas** rather than silent edits.
The DRR is the *minimum structured argument*—and, when several patterns or selected non-pattern FPF kind-reference pairs must move together, an allowed temporary convergence record that keeps **P‑10 Open‑Ended Evolution** compatible with **P‑1
Cognitive Elegance** and **P‑2 Didactic Primacy**.

E.9 sets a **floor, not a ceiling**: every conforming DRR must make
Problem‑frame / Decision / Rationale / Consequences recoverable, but it
may carry richer substantive coordination content when that prevents
shadow documents or semantic invention during distribution into Core patterns and selected non-pattern FPF kind-reference pairs. The same floor also requires the decision-support content that
later authoring and review otherwise reconstruct manually: exact basis,
use-value, first-minute working situation, scenario basis, alternatives,
current disposition map, naming/ontology obligation, selected content distribution,
existing-pattern sufficiency/new-pattern necessity, overlap classification,
selected-answer stability, impact/boundary graph, practical payoff, and
any still-live uncertainty that materially shapes the decision.

Pointer-based DRRs (CC‑DRR.1a) prevent duplicated prose, and distribution
into Core patterns and selected non-pattern FPF kind-reference pairs (CC‑DRR.4) keeps the specification itself learnable
without turning the DRR into a permanent shadow canon. Process-law ordering,
gate, and handoff records stay outside because they are not part of the
content answer that FPF is selecting.

### E.9:11 - SoTA-Echoing

`E.9` aligns with contemporary architecture-decision and rationale-capture practice, but its contribution is not the existence of a decision record. ADR practice already carries compact context, decision, and consequence records. FPF uses the DRR as a decision-rationale record for one bounded FPF content decision, with enough by-value rationale to distribute durable content into selected patterns and selected non-pattern FPF kind-reference pairs.

| Practice source family | Local FPF invariant and practical implication | Popular shortcut rejected |
|---|---|---|
| **Architecture-description standards such as joint ISO, IEC, and IEEE 42010:2022** | Architecture work must make concerns, viewpoints, decisions, and rationale inspectable. A DRR adapts this to FPF content deltas by exposing the concerns and alternatives that shape the FPF change, not only the edited text. | Reject treating a patch or edited wording as self-explanatory architecture rationale. |
| **Markdown ADR practice, including post-2015 lightweight ADR and MADR-style templates** | Context, decision, and consequence records are useful when the live change is local. A semantic FPF amendment needs enough by-value support for later pattern drafting without reinvention. | Reject treating a generic ADR template as sufficient when a multi-pattern FPF change needs Pillar, lens, naming, SoTA, distribution, or loss and recoverability support. |
| **Continuous and evolutionary architecture decision-record practice** | Decision records are revisitable support for evolving systems. FPF keeps mutable process state out of the DRR and handles reopened content with a successor decision record. | Reject turning the DRR into a live status log, gate diary, or permanent shadow law. |
| **Research and design-rationale traditions around alternatives and trade-off capture** | Rejected alternatives and trade-offs must remain recoverable enough that future authors do not re-litigate or silently reverse the selected answer. FPF adapts this through the Eleven Pillars and Principle-Taxonomy lenses. | Reject recording only the selected answer while leaving why-this-not-that implicit. |

The practical gain is content-selection quality under semantic load: the DRR decides the selected answer, alternatives, losses, boundary, and receiving loci before pattern drafting begins. Any durable rule, example, or content obligation that remains useful after acceptance belongs in the selected FPF pattern or selected non-pattern FPF kind-reference pair, not in the DRR as a permanent shadow canon.

When a DRR relies on a source document, workstream plan, campaign queue, external review packet, standard, article, ADR-like note, or prior accepted decision, it states the source posture and carries the selected payload by value: adopt, adapt, reject, lineage-only, rationale-only, selected payload, rejected or non-carried payload, source loss, receiving locus, non-use boundary, and reopen condition. A cited source is not FPF doctrine, child DRR, review result, gate, evidence sufficiency, or monolith landing source by citation alone.

### E.9:12 - Relations

* **Instantiates:** P‑10 Open‑Ended Evolution, P‑2 Didactic Primacy
* **Template governed by:** `pat:authoring/pattern‑template` (E.8)
* **Interacts with:** `pat:guard/bias‑audit` (E.5.4) via lens check
* **Complemented by:** `E.9.DA` when one concrete `DRR` follows E.9 form but its adequacy for downstream drafting, host amendment, accepted-decision carry-through, source-use carry-through, or receiving-locus distribution is disputed or materially live. `E.9.DA` reads the `DRR` decision-adequacy claim; it is not a second DRR form, review gate, or mandatory ordinary editorial step. Also complemented by `pat:authoring/code-of-conduct` (E.12) for etiquette in DRR debate.

* **Coordinates with:** `E.23` when one `DRR` is being improved through repeated quality-improvement passes. `E.9` keeps the `DRR` kind and decision-record form; `E.9.DA` supplies the decision-adequacy object-under-improvement evaluation when adequacy is live; `E.23` governs the repeated method rather than turning the DRR into final pattern prose.


### E.9:End

