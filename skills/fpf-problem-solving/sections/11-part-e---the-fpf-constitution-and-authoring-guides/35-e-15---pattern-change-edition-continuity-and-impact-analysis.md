## E.15 - Pattern Change, Edition Continuity, and Impact Analysis

**Pattern type.** Method pattern.

**Status.** Stable.

**Normativity.** Normative unless a passage is marked informative.

> **One-sentence summary.** Compare one exact predecessor pattern edition with its proposed successor, describe the actual change before naming its class, repair only the uses that depend on it, and use a wider search only when a real design choice remains.

### E.15:1 - Problem Frame

Use this pattern when an existing FPF pattern is being corrected, clarified, reorganized, refreshed from current sources, split, merged, renamed, or changed semantically, and someone needs to know what may continue and what must be reconsidered.

The primary `EntityOfConcern`—the thing being changed—is one exact existing FPF pattern edition. The candidate is its proposed successor. The useful result is that candidate plus a bounded account of what actually changed, which uses may be affected, which predecessor ideas remain, and which checks were rerun. Put that account in the decision, review, campaign, or landing result that needs it; this pattern does not require a separate trace object.

**First useful move.** Put the predecessor and candidate side by side and finish this sentence in ordinary language:

> A reader or user who relied on `<predecessor passage>` may now read, do, check, or conclude `<difference>`.

If the truthful answer is “nothing”, test that claim against the affected passages and stop after the smallest adequate repair and check. If the answer is uncertain because several materially different repairs remain plausible, open the alternative-comparison branch.

Not this pattern when authoring a first pattern seed with no predecessor; use E.8 and the subject-owning patterns. Do not use E.15 merely to run a wording check, make a design decision, perform a quality review, publish a pattern, or land a candidate: E.10, E.9, E.19 or E.21, E.24.PUB, and the landing process own those distinct questions. Return here when one of those activities changes an existing pattern edition and edition continuity or affected use is in question.

### E.15:2 - Problem

Two failure modes pull pattern change in opposite directions.

* A quick patch can preserve the visible sentence while losing a predecessor idea, changing a direct consumer, or leaving an old instruction elsewhere.
* A safety-minded author can turn a small repair into a full search, scoring, evidence, and publication programme whose records cost more than the decision and still do not prove that the chosen text is better.

Labels do not solve the problem. Calling an edit “lexical”, “minor”, “refresh”, or “refactor” does not say whether practitioner entry, inputs, action, conditions, result, ontology, or assurance changed. A version number communicates an already made compatibility judgment; it does not make that judgment true.

### E.15:3 - Forces

| Force | Tension |
| --- | --- |
| Fast repair vs continuity | A local correction should stay cheap, while material predecessor functions and dependent uses must not disappear. |
| Exact comparison vs semantic change | A textual diff locates changed words; it does not decide whether an idea, action, or result changed. |
| Reuse vs reverification | Unaffected results should be reused, but only after the dependency that made them unaffected is understood. |
| One good repair vs useful alternatives | Extra candidates help when a real choice remains; they are waste when one bounded non-dominated repair is already understood. |
| Precision vs working language | Ontological repair may need sharper distinctions, but the resulting whole pattern must remain readable and usable in a project. |
| Stable history vs current use | Old editions remain exact historical sources, while current reliance must name the edition it actually uses. |

### E.15:4 - Solution

#### E.15:4.1 - Recover the actual change

1. **Name the predecessor, candidate, question, and receiving use.** Use exact editions or recoverable source values. Add a ClaimScope, ReferenceScheme, model-use structure, or other qualifier only when the receiving use depends on it.
2. **Read the changed passage in both wholes.** Inspect enough of each pattern to recover the passage's function, not only its changed tokens.
3. **Describe the actual practitioner effect.** Ask separately whether the change alters recognition or entry, required inputs, the first or later action, applicability or stop conditions, returned result, normative claims, ontology, dependent uses, or assurance needed for reliance.
4. **Classify only after that comparison.** Use the smallest Delta-Class that matches the observed effect in §4.3. The planned label, commit subject, or amount of changed text is evidence to inspect, not the answer.

Keep wording, examples, informative rationale, normative conditions, and public naming distinct; changing one does not silently change the others. Keep `ClaimScope` and `WorkScope` distinct when both are current.

If an exact predecessor value needed for this comparison is unavailable, return that bounded continuity gap. Do not reconstruct it from a later edition, a title, or a remembered summary.

#### E.15:4.2 - Find the affected reach

Start with the changed claim or instruction and ask who uses it to read, act, check, decide, derive another statement, or preserve a public name. Search results and Relations entries help discover candidates, but neither proves dependence.

For every plausible consumer, decide one of three things:

* **depends:** its action, interpretation, condition, result, check, or public reference would change if the repaired claim changed;
* **mentions only:** it cites or describes the pattern but its current action remains valid;
* **unresolved:** the dependency cannot yet be decided from recoverable content.

Repair the exact dependent loci. Reuse an earlier result only when its conclusion and conditions remain unchanged and the changed premise lies outside its actual dependency. Reopen the smallest affected premise, consumer, example, check, or result; do not rerun an unrelated whole programme merely because an edition number changed.

An undeclared consumer can be real, and a declared dependency can be unused in the current question. Check actual and declared reach when the distinction matters.

#### E.15:4.3 - Classify the actual delta

| Class | Actual effect | Ordinary response |
| --- | --- | --- |
| **Δ-0 — editorial repair** | Spelling, punctuation, formatting, or wording changes while recognition, meaning, actions, conditions, results, checks, and dependent uses remain the same. | Make the direct repair; run the focused wording or structural check that could fail. |
| **Δ-1 — didactic re-expression** | Order, examples, or explanation changes while the same practitioner situation, action, normative conditions, result, and ontology remain recoverable. | Verify idea preservation and read the whole changed pattern for recognition, plain language, and action continuity. |
| **Δ-2 — normative clarification or refinement** | A previously intended rule becomes more explicit, bounded, or checkable, and semantic continuity is claimed, but affected instructions, checks, or consumers may need repair. | State the continuity claim, inspect the affected reach, and supply the equivalence or preservation evidence that the claim needs. Use a DRR when the refinement selects a material content decision. |
| **Δ-3 — semantic change** | Admissible inputs, actions, conditions, results, normative meaning, ontology, public identity, or dependency claims change. | Make the content decision explicit, repair the dependency-closed reach, and recheck every conclusion that relied on the changed premise. |

These are impact classes, not mandatory version-number syntax. If a publication uses SemVer or another version policy, map the already justified compatibility decision into that policy. Do not infer the class from `major`, `minor`, or `patch`.

Refine, rephrase, split, merge, generalize, constrain, rename, add, and retire remain useful edit descriptions. None has a fixed Delta-Class without its actual effect. A split that preserves every use may be Δ-1; a one-word change that reverses an obligation is Δ-3.

#### E.15:4.4 - Choose the least costly adequate route

**Direct bounded repair.** Use this ordinary route when the defect and one non-dominated repair are understood. Make the repair, inspect its actual consumers, perform the selected focused checks, and stop. Do not generate dummy alternatives or a search record.

**Alternative comparison.** Open this branch only when at least two materially plausible designs remain, a current SoTA choice can change the action, or a repeatable search is itself useful. State what the alternatives differ on and which intended use decides among non-dominated candidates. C.18 and C.19 may generate and retain alternatives when novelty or diversity is genuinely part of the question; E.22 and E.21 frame and evaluate pattern qualities.

Keep hard constraints separate from quality comparisons. A failed identity rule, broken reference, missing required result, or unreadable first action is a defect to repair, not a low score to trade away. Compare readability, precision, assurance cost, breadth, or other qualities on their applicable scales. Select by the stated intended use and protected trade-offs; do not add heterogeneous values into an undeclared winner score.

**Return a decision gap.** If the repair depends on an unresolved ontology, authority, source choice, or architecture decision, return that exact gap to its pattern or decision record. More variants do not compensate for a missing governing distinction.

#### E.15:4.5 - Preserve the predecessor by independent probes

For a material rewrite, derive a predecessor-use inventory from the predecessor itself before relying on the author's preservation map. Include each distinct working situation, first move, input, condition, result, prohibition, example function, consequence, source-derived contribution, and consumer-facing promise that the predecessor actually carried.

Then test each probe against the candidate:

* **preserved:** the same practical or semantic function remains;
* **changed intentionally:** the successor decision names the new function and why;
* **moved:** an exact current locus still supplies it without making discovery worse;
* **retired:** an explicit decision removes it and states the affected use;
* **lost or unresolved:** repair it or return it before claiming continuity.

Exact copied text may close by identity. A large deletion, compression, move, or rewrite does not close through line count, author intent, or a high-level summary. The independent inventory need not become a permanent row-by-row file when the receiving workflow needs only the verified candidate and aggregate result, but the inspection itself must be complete.

#### E.15:4.6 - Check the candidate proportionately

Select checks from the actual change and intended conclusion. A small Δ-0 repair may need one focused check. A Δ-2 or Δ-3 change may require semantic, ontological, consumer, source, preservation, or independent quality checks. Reuse a current check result when candidate, question, conclusion, and conditions are unchanged.

After a material ontological or formal repair, read the **whole changed pattern** as a cold practitioner. A local token scan cannot establish precise plain language. Check that the working situation, first action, examples, conditions, and result remain understandable without reconstructing the ontology from elsewhere. Simplify the expression, not the distinction. Keep a technical term when it names a real needed object or relation; remove stacked qualifiers and formal notation when they do no action-changing work.

Author-side use of E.10, E.19, or E.21 questions is development evidence. It does not become the independent review, complete quality result, admission, or landing conclusion that a later use may require.

#### E.15:4.7 - Keep one useful change account

Use the receiving workflow's existing record. A compact change account normally needs only:

| Question | Minimum useful answer |
| --- | --- |
| What changed? | Exact predecessor and candidate, changed loci, and ordinary-language actual effect. |
| How material is it? | Delta-Class with the reason from §4.3, not the desired label. |
| What may be affected? | Dependent loci and unresolved reach; mention-only citations need no repair recital. |
| What was preserved? | Material predecessor functions and any intentional change, move, or retirement. |
| Why this repair? | Direct repair reason, or alternatives and intended-use trade-off when a real choice existed. |
| What was checked? | The focused or whole-pattern results required for the claimed conclusion. |
| What reopens? | Only a source, premise, consumer, or condition whose change could invalidate the result. |

These answers may live in a DRR, review package, campaign result, source-use account, or landing preservation result as that workflow requires. Cite an existing E.21 or E.22 evaluation, F.15 result, source-use record, or decision instead of copying it. Do not mint a dedicated authoring trace, publish a work log with the pattern, or treat a file or publication occurrence as proof that the change was performed well.

#### E.15:4.8 - Edition continuity and stop rule

Keep accepted historical editions immutable and recoverable. A successor does not rewrite what an earlier edition meant. A source-edition change reopens only claims and actions that relied on the changed source value; unchanged exact inputs and unaffected premises remain reusable.

E.15 finishes when the candidate answers the change question, every actual dependent locus in scope is repaired or explicitly unresolved, material predecessor functions have dispositions, and the selected checks support the claimed Delta-Class and continuity. Publication, acceptance, registration, and landing remain separate later decisions.

Schedule a living refresh only for a high-value claim likely to change and only when someone will use the signal. Name the trigger and affected claim. Otherwise use ordinary periodic review; a generic “watch SoTA” obligation is not useful work.

### E.15:5 - Archetypal Grounding

**Tell.** Change the smallest semantic unit that solves the problem, but judge continuity at the scale where a reader or consumer could actually be harmed.

#### E.15:5.1 - Typo with no semantic reach

An identifier is spelled correctly everywhere except one explanatory sentence. The exact identifier, instruction, and checks remain unchanged. The author repairs the sentence, verifies the identifier and nearby reference, classifies the actual change as Δ-0, and stops. Three alternative phrasings and a DRR would add no value.

#### E.15:5.2 - Plain-language repair after an ontology correction

A relation passage is ontologically exact but has grown into two pages of qualifications that hide the first action. The candidate restores one readable explanation and keeps the exact relation test in the assurance section. Because a substantial rewrite can lose ideas, the author independently inventories the predecessor's entry, action, conditions, examples, and prohibitions, then reads the whole candidate as a cold user. If every semantic function remains, the result may be Δ-1 or Δ-2 depending on whether a normative clarification also occurred; the word count does not decide.

#### E.15:5.3 - One-word semantic change with dependent consumers

A conformance rule changes `may` to `must`. The diff is one word, but admissible use and failure conditions change. The actual class is Δ-3. The author repairs examples, checklist items, and direct consumers that relied on the optional branch and rechecks their conclusions. Unrelated source and publication checks are reused.

#### E.15:5.4 - A source edition changes one relied-on premise

A current research edition revises a limitation used by one SoTA decision. The pattern's other sources and practitioner steps do not depend on that premise. The author reopens that one source-use decision and its receiving passage, not every source row and not the whole corpus. If the selected action changes, the affected consumers follow; if it does not, the account states why the current result remains supported.

#### E.15:5.5 - A real architecture choice

A pattern could model a new distinction as a local value, a direct relation, or a selected structure, and each choice changes downstream use. No single repair is yet non-dominated. The author records the alternatives in the DRR, uses subject-specific criteria and E.21/E.22 qualities, and may use C.18/C.19 to broaden the candidate set. The comparison stops when the intended use supports one non-dominated architecture; search machinery is not retained as a universal authoring obligation.

### E.15:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal for changes to existing FPF pattern editions**.

The method biases toward continuity and inspectability (**Arch**, **Onto/Epist**). The direct-repair route, record-reuse rule, whole-pattern cold-reader check, and first-adequate-result stop protect practical speed and readability (**Prag**, **Did**). Decision and review authority remain with their own patterns (**Gov**).

### E.15:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-E15-1 (Exact change basis).** | A conforming use **MUST** identify the exact predecessor and candidate editions, the change question, and the receiving use. | Makes continuity replayable without a universal context record. |
| **CC-E15-2 (Actual delta first).** | Delta-Class **MUST** follow comparison of actual effects on recognition, inputs, actions, conditions, results, norms, ontology, consumers, and assurance; a label, version number, edit operator, or line count **MUST NOT** decide it. | Prevents small semantic changes and large harmless rewrites from being misclassified. |
| **CC-E15-3 (Proportional route).** | A direct understood repair **MUST NOT** be forced through multiple-candidate generation, aggregate scoring, a SoTA harvest, or a new trace record. Alternative comparison **MUST** be used only when materially plausible alternatives or a consequential current-source choice remain. | Keeps ordinary changes cheap without deleting the stronger branch. |
| **CC-E15-4 (Actual affected reach).** | Every in-scope locus whose action, interpretation, condition, result, check, or public reference depends on the changed premise **MUST** be repaired or explicitly unresolved. Mentions and declared links **MUST NOT** substitute for the actual dependency test. | Makes the repair dependency-closed. |
| **CC-E15-5 (Independent predecessor preservation).** | A material rewrite **MUST** be checked against an independently derived inventory of predecessor functions and uses. Every intentional change, move, or retirement **MUST** be named by its successor decision; an author-authored preservation map alone **MUST NOT** close completeness. | Prevents compression or restructuring from silently deleting ideas. |
| **CC-E15-6 (Valid selection).** | Hard constraints **MUST** remain separate from multi-scale qualities. When alternatives are compared, the selected candidate **MUST** be non-dominated for the stated intended use and protected trade-offs; an undeclared aggregate score **MUST NOT** choose it. | Makes “better” a replayable use-relative claim. |
| **CC-E15-7 (Record economy and object separation).** | The change account **MUST** reuse the receiving workflow's governed records by reference. A new episteme or publication **MUST NOT** be inferred from a form, file, self-log, or the fact that authoring occurred. | Avoids duplicate records and false work evidence. |
| **CC-E15-8 (Proportionate verification).** | Checks **MUST** be selected from the actual change and claimed conclusion. After material formal or ontological repair, the whole changed pattern **MUST** receive a precise-plain-language and practitioner-use read in addition to focused semantic checks. | Prevents locally exact repairs from making the pattern unusable. |
| **CC-E15-9 (Edition continuity).** | Historical editions **MUST** remain recoverable, and only affected premises or consumers **MUST** reopen. Publication, acceptance, registration, and landing **MUST NOT** be inferred from E.15 completion. | Separates semantic continuity from later lifecycle decisions. |
| **CC-E15-10 (Problem-specific SoTA).** | When external or internal SoTA changes the repair, the account **MUST** compare serious current alternatives at comparable application effort and state the adopted, adapted, or rejected contribution at the receiving locus. Source popularity, age, official status, or tool availability **MUST NOT** substitute for that decision. | Keeps research load-bearing and bounded. |

### E.15:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| **Every edit becomes a programme** | A typo triggers candidates, scoring, evidence packaging, and refresh work. | Use the direct bounded repair and stop after its focused check. |
| **Delta by label** | “Lexical” or “minor” hides an action-changing edit. | Describe the actual reader and consumer effect first. |
| **The author's map proves preservation** | A rewrite is checked only against what its author remembers preserving. | Derive predecessor-use probes independently and inspect every material function. |
| **Search output equals impact** | Every textual mention is edited, while an undeclared real consumer is missed. | Test whether each candidate locus actually depends on the changed premise. |
| **One score chooses the winner** | Readability, breadth, formal checks, and assurance are added without lawful scales or protected trade-offs. | Keep constraints separate and choose among non-dominated candidates for the intended use. |
| **Version number supplies semantics** | `major`, `minor`, or `patch` is treated as proof of compatibility. | Decide continuity first; use a version label only to communicate that decision. |
| **A new trace for every change** | DRR, review, source, check, and landing facts are copied into another authoring-trace record. | Keep the minimum change account in the receiving workflow and cite existing results. |
| **Precise fragment, unreadable pattern** | A formal repair passes a token check while the whole pattern loses recognition and practical entry. | Read the whole changed pattern as a cold practitioner and simplify non-load-bearing formal language. |
| **Self-log as practitioner guidance** | The pattern publishes its own authoring history and calls it Work or quality evidence. | Keep one worked practitioner case in the pattern; keep actual work and evaluation evidence in their direct records. |

### E.15:9 - Consequences

**Benefits.** Small repairs stay small. Material changes expose their real dependent reach. Historical editions remain usable. Independent predecessor probes make large rewrites safer. Alternative search remains available where it can improve a real decision, and whole-pattern plain-language checking keeps ontological precision usable.

**Costs and limits.** Actual dependency and predecessor-function inspection require semantic judgment; a repository search cannot automate them completely. A Δ-2 or Δ-3 repair can still be expensive when many consumers truly depend on the changed premise. This pattern reduces redundant checking but cannot make a broad semantic change local by declaration.

Reopen the method when the four Delta-Classes no longer distinguish action-relevant change, when dependency-focused verification demonstrably misses affected uses, or when a lower-effort method provides equal or better preservation and decision quality.

### E.15:10 - Rationale

The architecture is deliberately asymmetric. The common case receives a short path because extra alternatives and records cannot improve an already understood bounded repair. The strong branch remains because architecture, ontology, and current-source decisions sometimes have several non-dominated answers.

Exact predecessor comparison and affected-reach analysis work together. The predecessor prevents history from being rewritten; actual dependency prevents an edition label from reopening everything. Independent preservation probes answer a different question from an author's change explanation: they test what the explanation may have omitted.

Delta-Class stays useful as a compact impact signal, but only after the real change is known. E.21/E.22 own pattern quality, E.9 owns content decisions, E.19 owns review, and lifecycle patterns own publication and landing. E.15 connects these results without duplicating them.

### E.15:11 - SoTA-Echoing

The selected method combines exact edition comparison with dependency-aware incremental reverification and optional design-space search. No one source supplies the complete FPF procedure.

| Practice or research line | Status and contribution | Limit or rejected overread | Change to E.15 |
| --- | --- | --- | --- |
| [Git diff documentation](https://git-scm.com/docs/git-diff), current official documentation | **Adopt:** compare exact endpoints and keep historical values recoverable. | A textual or blob diff locates change but does not prove semantic preservation or actual consumer impact. | Exact predecessor/candidate recovery is mandatory; semantic probes remain separate. |
| [Semantic Versioning 2.0.0](https://semver.org/) | **Adapt as established release practice:** immutable released contents and explicit compatibility communication are useful. | SemVer depends on a declared public API and its labels do not decide FPF semantic continuity. It is not the current method for impact analysis. | Version syntax is optional and follows, rather than supplies, the Delta-Class decision. |
| [Current Bazel action-graph and incremental-build practice](https://bazel.build/about/intro) and its [actual-versus-declared dependency distinction](https://bazel.build/concepts/dependencies) | **Adapt:** trace changed inputs through actual dependencies and reuse unaffected work. This advances the effort-to-reliability frontier over full reruns when change is local. | A build graph is not an ontology of pattern meaning, and declared references can miss or overstate semantic dependence. | Inspect actual and declared consumers; reopen only affected conclusions. |
| Li, Chen, Huang, and Ding, [“Change-aware model checking for evolving concurrent programs based on Program Dependence Net”](https://doi.org/10.1002/smr.2626), 2024 | **Adopt the current research move by analogy:** use prior verified results and property-relevant dependency slices rather than rechecking an entire changed system. | Software paths and LTL properties do not transfer as FPF kinds or sufficient evidence for prose semantics. | Result reuse requires an unchanged conclusion and a justified outside-impact dependency. |
| MAP-Elites and quality-diversity search, with current FPF C.18/C.19 machinery | **Retain as optional lineage and method family:** useful when several materially different candidates and diversity itself matter. | Candidate multiplicity and archive coverage do not improve an understood local repair and do not select a winner across heterogeneous qualities. | Alternative generation is conditional; E.21/E.22 and intended use decide among non-dominated candidates. |
| Full rerun of every authoring, source, assurance, and review activity | **Reject as the default rival:** broad reruns can be appropriate after a genuinely broad Δ-3 change. | At comparable correctness, they spend more effort on unaffected premises and encourage ceremonial records. | Scope verification from actual change and dependencies, while preserving the explicit broad-change branch. |

The non-dominated contribution is therefore not a new authoring trace or scoring system. It is the combination of a cheap direct-repair path, actual-delta classification, independent predecessor preservation, actual-consumer reach, and whole-pattern practitioner-language verification, with stronger search and checking opened only by their real use.

### E.15:12 - Relations

**Builds on:**

* **E.8** for first-edition authoring shape and practitioner-facing pattern structure.
* **E.10**, **F.18**, and **F.19** for wording-use diagnosis, naming, and precise plain language.
* **E.9** for a material content decision and **E.9.DA** when that decision needs adequacy review.
* **F.0.1** and **F.1** for exact source-local meaning and question-relative source selection.
* **A.10** and **B.3** when a changed claim actually depends on evidence use or assurance.

**Coordinates with:**

* **E.19** for pattern review, **E.21/E.22** for quality evaluation, and **E.23** for repeated improvement.
* **C.18 and C.19** for optional candidate generation and explore/exploit control when a real alternative-search branch is open.
* **F.15** for applicable regression checks and **F.9** only when the changed use actually relates distinct local senses.
* **B.4** for later evolution-loop scheduling when a named refresh trigger is worth maintaining.
* **E.24.PUB** and the landing process for later publication and integration; neither follows from an E.15 result.

### E.15:End

