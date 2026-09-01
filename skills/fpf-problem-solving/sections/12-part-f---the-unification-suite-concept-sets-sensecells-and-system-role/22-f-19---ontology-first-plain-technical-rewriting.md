## F.19 - Ontology-First Plain Technical Rewriting

> **Type:** Plain-technical precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative for FPF-governed technical prose unless explicitly marked informative; informative for external source prose until it is rewritten for FPF use

**Plain-name.** Ontology-first plain rewriting.

**Intent.**
Repair technical prose that is grammatically plausible or locally true yet makes the reader supply an unsupported relation, participant, alternative, list meaning, or rhetorical branch. First recover the governing object, claim, action, required operands, referents, and kinds; then remove apparatus and other structure that contributes nothing to the intended use. The normal result is repaired text, not an audit form. Preserve every technical distinction and operational detail that changes truth or action, and route only genuinely unresolved FPF wording to `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, or the subject pattern that defines it.

**Builds on.** `E.8`, `E.10`, `E.10.ARCH`, `F.18`, `A.6.P`, `A.7`, `E.18`, `E.21`, and source-use, evidence, assurance, gate, work, decision, publication, architecture, characteristic, state-family, and relation patterns when those objects carry the repaired span's claim.

**Coordinates with.** `E.19`, `E.22`, `E.23`, `A.19.SPR`, `C.2.P`, `C.16.P`, `C.30.P`, `E.11`, `I.2`, pattern-quality records, review records, `DRR`s, projection loci, and source-side notes.

### F.19:0 - Use this when

Use `F.19` when a bounded piece of technical prose is harder to understand or use than its intended claim requires. The sentence may be grammatical and every isolated statement may be true, yet the reader still has to invent a missing operand, accept an implausible relation, guess what a pronoun or relational noun refers to, interpret a list with no stated purpose, or wait through caveats and ornament before reaching the governing message.

Common signs are:

- a verb or relational noun whose needed participant is not cheaply recoverable;
- a grammatical subject that cannot bear the asserted predicate, even when that predicate appears inside a denial;
- a contrast, warning, or guard against a reading that no plausible intended reader has reason to make;
- one head or predicate imposed on unlike members;
- examples presented as a classification, or a catalogue presented instead of a proposition; and
- coordination repeated inside phrases and across clauses, or stacked modifiers, when one governing statement would do.

Item count is only a cue. Two coordinated members can already be needless, while a long inventory can be exact and useful when its kind, membership rule, and closure matter. Matching kinds and individually relevant members do not by themselves justify a series: the reader must need to distinguish or retain the members together for the intended use.

Apply the same method to FPF pattern prose and to other technical prose whose accepted domain terms, relations, claim boundaries, or use conditions must survive simplification.

**What goes wrong if missed.** The prose looks careful while introducing relations, alternatives, or branches that the work does not need. A later author or generator may then copy that shape as an acceptable technical style.

**What this buys.** The reader reaches the supported object, claim, and action sooner. Required technical distinctions remain; invented foils, false agency, reference puzzles, and catalogue rhetoric do not.

**First useful move.** State in one plain sentence what the intended reader must recognize, understand, decide, or do. Then read the whole natural span against that sentence before changing individual words.

**Not this pattern when.**

- If only one already-visible FPF word or head has an unresolved technical use, take the exact `E.10` route for it.
- If the question is a durable reusable name, use `F.18`.
- If source prose is only being observed and not admitted into governed technical prose, keep the observation source-side.
- If evocation, rhythm, ambiguity, or parallelism is the declared work of a poem, quotation, ceremonial passage, or other expressive genre, do not flatten it into technical instruction. Apply `F.19` only to the technical claim or action that must remain recoverable.
- If a language-specific grammar or idiom remains after the common semantic repair, use the applicable language profile.

**Primary EntityOfConcern in plain terms.** One sentence, row, paragraph, list, or small coherent section being repaired into precise plain technical prose.

### F.19:1 - Problem frame

Local truth is necessary but not sufficient for useful technical prose. “A mouse is not the Eiffel Tower” is true, but it introduces an Eiffel-Tower reading that the reader had no reason to construct. “The evidence does not notice the error” is also locally true, yet the denial makes *evidence* the subject of an impossible noticing relation. “The result is not a final scheme of the world” invents a grand alternative before the sentence reaches its actual result.

The same failure appears without negation. “Then pour” can omit the thing or destination that determines the operation. “Bearer” can leave the reader asking bearer of what. A grammatical series can give examples, methods, activities, and outcomes one false common head. Several individually valid pairs can create catalogue rhythm while never stating the proposition they are meant to support. Scenic or defensive detail can delay an urgent event or requested action.

One connected repair therefore answers two questions:

1. **Semantic completeness:** can the reader recover the predicate, its required participants or operands, local referents, member kinds, and the relation actually asserted?
2. **Pragmatic contribution:** does each explicit alternative, modifier, guard, list member, and extra proposition change what the plausible intended reader can recognize, understand, decide, or do?

The defect is not a word class or a forbidden syntax. Negative polarity can be the claim. A documented anti-pattern can quote the real error. A visible diagram feature can make one overreading plausible. Ordinary metonymy and ellipsis can be clearer than formal expansion. Judge the supported relation and the receiving use, not the presence of `not`, a comma, or a particular verb.

### F.19:2 - Problem

How can a practitioner repair technically plausible prose that asserts unsupported relations or makes the reader invent missing structure, while preserving the kinds, claim boundaries, operational detail, and established terms that the intended use actually needs—without building a controlled language, a universal ontology of speech, a prohibited-word list, or a form for every correction?

### F.19:3 - Forces

| Force | Tension |
|---|---|
| Plain wording vs technical meaning | Shorter prose helps only if object kinds, relations, uses, claim boundaries, and action-changing detail survive. |
| Local truth vs useful contribution | A clause can be true and type-compatible while answering no live question and displacing the positive path. |
| Explicitness vs ordinary recovery | Missing operands and referents can make a puzzle, but repeating every complement or formal identity makes ordinary prose harder to think with. |
| Guarding vs invented foils | A grounded warning or non-use boundary can prevent harm; an imaginable but unsupported mistake creates noise and teaches defensive style. |
| Enumeration vs governing message | Lists can encode required membership or alternatives; accumulation can also replace the proposition or postpone the action. |
| Portability vs local language needs | Predicate, participant, kind, referent, contribution, and list questions travel across languages; morphology and idiom remain local. |
| Reviewability vs bureaucracy | A disputed or high-risk rewrite may need comparison evidence; ordinary correction should produce repaired text, not a ledger. |

### F.19:4 - Solution

Use `OntologyFirstPlainRewrite` as one connected reading and repair over a natural sentence, row, paragraph, list, or small coherent section. Take the intended reader and use from the surrounding work; do not invent an adversarial reader or a persona form.

#### F.19:4.1 - One connected reading and repair

1. **State the governing message.** Say what object, claim, action, event, or distinction the span needs to convey. Mark process traces, status language, reference boilerplate, quality proof, defensive caveats, ornamental detail, and other apparatus that may be displacing it. Apparatus receives no protection merely because it is true or polished.
2. **Recover the predicate and its participants.** Identify the operation and every participant that changes it. This may be an actor, object, source, target, result, or another required operand. Apply the same question to verbal and relational nouns: recover *of what*, *for what*, *between what*, or another required participant. Leave an argument implicit only when one intended value is cheaply and uniquely recoverable from the local span.
3. **Check predicate compatibility.** The grammatical subject must be able to bear the asserted predicate under the intended literal or metonymic reading. Check inside negation, modality, conditions, examples, and the author's own quoted formulation: denying that evidence notices an error still introduces an evidence-noticing relation. Keep ordinary metonymy when the relation is established and the capable participant or work remains recoverable: a diagram may show, a framework may help, a reminder may cue, and a constraint may limit.
4. **Resolve referents and kinds.** Pronouns, demonstratives, omitted heads, and repeated labels must select one locally appropriate referent. Preserve the object kind, claim or relation kind, slot or relation position, use and publication boundary, and flow distinction whenever one changes the claim. A shared grammatical position does not make different FPF kinds interchangeable.
5. **Test contribution.** Try deleting every optional contrast, guard, modifier, example, coordinated member, and extra proposition. Remove it when the plausible intended reader can still recognize, understand, decide, and act in the same way. Local truth and grammatical fit do not earn a phrase a place by themselves.
6. **Resolve coordination and lists on two axes.** First ask whether the receiving use needs a series at all. A list or parallel construction earns its form only when the reader must distinguish or retain its members together; otherwise select the governing claim, relation, or representative case. If a series is needed, determine its membership semantics. State the proposition or action it serves; use one kind or predicate only when it fits every member; distinguish a closed set, illustrative examples, alternatives, a sequence, several direct relations, and a failed ontology. A closed set needs its kind, membership rule, and closure. Illustrative examples need the proposition or kind first and a non-exhaustive cue when a plausible reader could mistake them for a classification. Then test discourse load: keep a member only when it adds a distinct consequence; reduce coordination repeated at several grammatical levels and modifier chains that make the reader retain needless branches or postpone the governing message. Length is evidence to inspect, not a verdict.
7. **Foreground, rewrite, and compare.** Put the governing event, claim, requested action, or decision before optional atmosphere, examples, caveats, and catalogues. A prerequisite may come first when it is needed for safe interpretation or action. Write the shortest ordinary technical sentence that preserves every live predicate and participant, established term, polarity, and action-changing detail. Such detail can include quantity or threshold, sequence or timing, criterion or tolerance, exception, and applicability. Compare before and after: any unsupported change of kind, relation, scope, use, currentness, or operational effect is a loss and blocks the rewrite unless another accepted decision authorizes it.

Keep ordinary domain wording ordinary. A qualifier such as `exact`, `direct`, `current`, `governed`, or `defining` remains only when it distinguishes a live alternative. A PatternID may remain an ordinary citation; open a formal identity branch only when the current claim or a named later use consumes it. Treat a pattern episteme as a `U.MethodDescription` only after `A.3.2` establishes the described Method. For an actual dated Work claim, recover its basis through the applicable `A.13`, `A.15.1`, and `F.6` route. Use `E.10.ROLE` or `A.6.F` once when role- or function-shaped wording remains genuinely unresolved.

#### F.19:4.2 - Plausible-reader guards and cold-reader recovery

Use two reader tests for different decisions.

- The **plausible intended reader** has the knowledge and task presupposed by the text. Use this reader to decide whether a foil, guard, warning, or contrast deserves mention. Do not substitute an adversarial reader who can imagine any false inference, or the author who already knows the answer.
- The **cold intended reader** lacks the author's private context and unpublished notes. Use this reader after the rewrite: they can recover the object, predicate, participants, relevant kind or ordinary status, relation, action-changing detail, and next useful action.

Retain a negative alternative, denied consequence, warning, or non-use statement only when the exact rejected reading has an independent local ground; the reading is coherent and type-compatible; a plausible intended reader could take it here; and the distinction changes truth, understanding, selection, safety, stop, reliance, or action. An earlier or source claim, an observed recurring mistake, a serious competing position, a visible representation feature, or an applicable safety risk can supply the ground. The guard itself cannot.

Even a grounded guard should be the smallest clear correction. When actor allocation is the useful content, state it positively: “On receiving new evidence, the reader decides whether to reopen checking or revision.” When currentness is the useful content, state the direct use: “This guide conveys the seminar of 1 February 2026; check current rules against the current FPF edition.” Keep material negation, documented anti-patterns, fair disputes, and safety stops when their polarity or boundary is itself the claim.

#### F.19:4.3 - Result and local revalidation

The ordinary result is the repaired text, or a blocker naming the unresolved meaning. Do not require a separate result form, card, table, progress row, or recorded answer for each facet of the reading.

After changing words or syntax, reread the changed sentence and only the nearby text needed to determine its referents, predicate, participants, contrast, modality, support, action, and result. The earlier semantic verdict does not transfer to new wording. Unchanged spans and conclusions remain reusable; a local edit does not trigger an automatic whole-document pass.

When a named high-risk or disputed decision needs inspectable evidence, show only the before text, repaired text, live values that had to survive, and any unresolved blocker. Use the receiving decision's existing comparison or review result rather than inventing an `F.19` ledger.

If ordinary reading settles the issue, stop. Open `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, or an exact subject pattern only for a genuinely unresolved FPF word, kind, relation, role, function, name, source-use, or admissible-use question. A trigger helps find a candidate; it neither bans the wording nor closes the judgement.

#### F.19:4.4 - Pattern-prose specialization

When the repaired prose is an FPF pattern, apply the same method with one purpose test:

> Does this sentence help the pattern's intended user recognize and perform the pattern, or does it record development, review, projection, landing, quality, or source-management evidence about this version?

If it records evidence about the pattern version, keep that evidence outside the pattern unless the pattern's own primary `EntityOfConcern` is that evaluation or projection object. The evidence can cause edits to the pattern; it is not automatically pattern content.

Pattern prose keeps:

- the pattern's own primary `EntityOfConcern`;
- the first useful move;
- the practical delta and cost of missing it;
- a local boundary only for a documented confusion or action-changing stop; and
- short references to related patterns after the pattern's own content is visible.

Pattern prose moves out:

- package-placement rationale;
- correspondence about producing or reviewing the draft rather than using the pattern;
- quality, projection, monolith-parity, landing, and source-management evidence; and
- repeated boundary doctrine already carried by another pattern.

### F.19:5 - Archetypal Grounding

This bounded regression set keeps one distinct semantic or use boundary per row. It is not a vocabulary of prohibited forms.


| Case | Before | Repair or disposition |
|---|---|---|
| Ordinary versus identity-bearing pattern use | “`A.15` handles the work-planning claim” or “the pattern performed the planning.” | For ordinary guidance write “Use `A.15` to plan the work.” If the sentence deliberately asserts a dated Work occurrence, name its capable participant and recover the Work basis before attribution. |
| Publication and evidence kind | “The dashboard is the evidence gate.” | “The dashboard presents evidence. Use `A.10` for the evidence claim and `A.21` for any gate decision.” |
| Operational-detail loss | “Rewrite ‘Boil for five minutes after simmer begins’ as ‘Cook until ready’.” | Reject the rewrite. It loses the duration, start condition, and usable stop criterion. |
| Invented foil | “The concluding practical result is not a final scheme of the world, but the ability to problematize again.” | No live world-scheme reading is grounded. Write: “The concluding practical result is the ability to problematize again and choose the next move deliberately.” |
| Denied impossible agency | “The evidence does not notice the error and does not begin a new cycle.” | Evidence supplies grounds; a reader or system evaluates them. Write: “New evidence gives the reader grounds to check or revise the first distinction and decide whether to reopen the work.” |
| Unsupported currentness guard | “Historical modality does not turn the seminar claims into the current FPF norm.” | State the dated source and current-use action: “This guide conveys the seminar of 1 February 2026; check current rules against the current FPF edition.” |
| Missing operation operand | “Take the mixture and then pour.” | If the object or destination is not uniquely recoverable, restore it: “Pour the mixture into the flask.” |
| Incomplete relational noun | “Give the bearer to the next stage.” | Name what is borne and the transfer relation, or use the ordinary domain noun. |
| False common head | “The method selects, publishes, and evaluates the alternatives.” | Split the claims and name the capable actors or exact relations. Do not invent one subject merely to keep the sentence symmetrical. |
| Catalogue instead of proposition | “Goals and objectives, forms and methods, quality and efficiency are supported.” | State the actual capability or decision. Keep only members with distinct consequences. |
| Illustrative list read as classification | A bare plural head is followed by many instances with no signal that the list is partial. | Put the proposition or kind first, mark the cases as examples when completeness is plausibly ambiguous, and retain only representative cases. |
| Delayed governing event | An emergency report describes birds, wind, birches, heat, mist, and animals before saying that a house-museum is burning and a fire engine is no longer needed. | Put the event, location, safety consequence, and requested response first. Keep only detail that changes dispatch, safety, evidence, or identification. |
| Material negation | “Do not energize the unit while the cover is open.” | Retain when the open-cover state creates the named risk and the stop changes action. The polarity is the instruction. |
| Ordinary metonymy | “The diagram shows the dependency.” | Retain when the diagram depicts it and the reader can recover the represented relation; do not expand a clear sentence into a Method and Work trace. |
| Recoverable ellipsis | “Take the solution, mix, and pour it into the flask.” | Retain when `it` has one local antecedent and the destination is stated. The reader need not solve a reference puzzle. |
| Required long set | A legal set, interface signature, inventory, or safety checklist has many members. | Retain the full series when its kind, membership or governing rule, and closure are declared and each member changes use. |
| Expressive parallelism | “Расцветали яблони и груши...” in a song, quotation, or discussion of poetic form. | Retain only where evocation or rhythm is the declared work. In a technical message, rhythm does not earn repeated pairs or a delayed governing claim. |

### F.19:6 - Bias-Annotation

`F.19` deliberately biases toward direct, reader-usable technical prose. The protected value is kind-preserving clarity, not brevity by itself. A longer rewrite is better when it restores a participant, relation, boundary, or operational detail that the declared use needs.

| Likely bias | Failure | Countermove |
|---|---|---|
| Formal-completeness bias | Symmetrical contrasts, caveats, and lists look rigorous although they add no supported distinction. | Apply the contribution test and state the positive path first. |
| Adversarial-reader bias | Any imaginable mistake is treated as a reason for a guard. | Require an independent ground and a plausible intended reader. |
| Apparatus-preservation bias | A process, status, record, card, schema, or quality-proof phrase is replaced by another wrapper. | Recover the object and action, then remove or move the wrapper. |
| Overformalization bias | Clear metonymy, ellipsis, or a PatternID citation expands into type labels and Work machinery. | Formalize only a live distinction or unresolved relation. |
| Genre-flattening bias | Useful rhythm, evocation, or deliberate ambiguity is treated as defective technical accumulation. | Apply `F.19` only where precise technical recognition or action is the declared use. |

### F.19:7 - Conformance checklist

These are acceptance questions for one repaired span. They are not separate attention steps or separately recorded results.

| Check | Passing condition |
|---|---|
| `CC-F19-1` Governing message | The intended reader and use are clear, and the governing object, claim, event, action, or distinction appears before optional apparatus. |
| `CC-F19-2` Semantic completeness | The predicate, required participants or operands, relational-noun complements, and local referents are recoverable without author memory or a reference puzzle. |
| `CC-F19-3` Predicate and kind fit | Each subject can bear its predicate under the intended literal or metonymic reading; object kind, claim or relation kind, slot, relation position, use, and publication boundary remain distinct where they change meaning. The test includes negation and modality. |
| `CC-F19-4` Meaning and loss preservation | The rewrite preserves every live term, polarity, quantity, threshold, temporal or ordering condition, criterion, tolerance, exception, applicability boundary, and other action-changing detail. Any accepted change of kind, relation, scope, currentness, or use has its own decision. |
| `CC-F19-5` Grounded contribution | Every optional guard, contrast, modifier, example, and coordinated member changes recognition, understanding, evidence, decision, safety, stop, reliance, or action for a plausible intended reader. A negative alternative has an independent local ground and is the smallest clear correction. |
| `CC-F19-6` Coordination and foregrounding | A list states the proposition or action it serves; its kind, predicate, membership semantics, and closure are not fabricated; illustrative status is clear when needed; and coordination or modifiers do not postpone the governing message. |
| `CC-F19-7` Plain result | A cold intended reader can recover the repaired claim and next useful action. The ordinary output is repaired text or a blocker, not a mandatory form or ledger. |
| `CC-F19-8` Local revalidation | Any changed wording or syntax has been reread with only its meaning-dependent neighbours. An older semantic verdict is reused only for unchanged text. |

### F.19:8 - Common anti-patterns and how to avoid them

| Anti-pattern | What fails | Repair |
|---|---|---|
| Lexical paint | One official-sounding word replaces another while the object or relation remains hidden. | Recover the practitioner-recognizable object, predicate, and participants before choosing words. |
| Truthful noise | A true denial or caveat answers an implausible question introduced by the sentence itself. | Remove the invented question and state the positive claim or action. |
| Impossible agency under denial | An incapable subject receives a predicate only so the prose can deny it. | Name the capable participant and allocate the action positively. |
| Missing operand as elegance | A verb or relational noun omits the value that determines the operation or relation. | Restore the participant unless one intended value is cheaply and uniquely local. |
| False common head | One subject or umbrella kind is made to govern unlike predicates or members. | Split the claims or state their several direct relations. |
| Enumeration as coverage | Examples, near-synonyms, abstract pairs, or several kinds simulate breadth but do not state a usable proposition. | Put the proposition first; mark examples; retain only independently consequential members. |
| Locally valid accumulation | Every pair or modifier passes alone, but nested coordination creates a catalogue and delays the message. | Summarize, subordinate, split, or delete by contribution and foreground the governing clause. |
| Apparatus-preserving paraphrase | Process, status, quality proof, record, card, table, or schema survives under smoother wording. | Move evidence to its proper locus and keep only user-facing content. |
| Trigger as verdict | A word list bans normal metonymy, negation, long sets, or expressive prose, or its silence is treated as clearance. | Use triggers only to locate candidates; decide from the whole span and declared use. |
| Checklist explosion | One semantic reading becomes separate forms or progress items for valency, agency, kind, referent, lists, and style. | Perform one connected repair and return the repaired text; use external attention methods only when the surrounding work needs them. |

### F.19:9 - Consequences

Technical prose becomes easier to trust and use because every asserted relation has supported participants, every retained guard answers a plausible question, and lists serve a visible proposition or action. The pattern also removes a source of stylistic copying: authors no longer see defensive truth, false symmetry, and exhaustive-looking catalogues presented as the normal shape of precision.

The cost is one semantic reread of the changed wording and its meaning-dependent neighbours. That cost stays local. Ordinary correction produces repaired text; only a named high-risk or disputed decision needs comparison evidence.

### F.19:10 - Rationale

Precise plain language has two obligations. The sentence must be semantically complete enough to recover its predicates, participants, referents, kinds, and operational detail. Every additional structure must also earn its place by changing understanding or use for the intended reader. Either obligation alone is insufficient: a fully typed sentence can still be noise, and a short sentence can still hide its object.

The order of repair therefore matters: recover the governing message and relations, remove unsupported structure and displaced apparatus, then write the shortest ordinary sentence that preserves the live meaning. `E.10` remains a cue and a route for unresolved FPF wording; it is not a rival normal-pass algorithm. Attention management remains outside the language pattern.

### F.19:11 - SoTA-Echoing

`SoTA` here means the best current contribution to the stated practice question, not the newest or most formal publication. The comparison below is current to 2026-08-19; a source's official status does not by itself make it SoTA.

| Practice question | Exact source and status | Selected payload and limit | Source-use decision, receiving locus, qualification, and reopen |
|---|---|---|---|
| How should ordinary technical prose help its intended reader act without being "dumbed down"? | ISO 24495-1:2023, *Plain language — Part 1: Governing principles and guidelines*, current published foundation (`https://www.iso.org/standard/78907.html`); Digital.gov, *Principles of plain language* and *Writing for understanding*, current living US-government practice guide (`https://digital.gov/guides/plain-language/principles`, `https://digital.gov/guides/plain-language/writing`), checked 2026-08-19. | Declare the reader and task; put the usable object and action first; organize for finding, understanding, and use; keep terms the intended reader needs. Neither source defines FPF ontology or requires expert prose to use general-public vocabulary. | **Adapt — reason:** these moves improve F.19's ordinary path without changing its semantic boundary. **Receiving loci:** F.19:0 first useful move; F.19:4.1 steps 1 and 7; `CC-F19-1` and `CC-F19-7`. **Qualification/currentness:** current standard and current practice guide, not FPF semantic authority. **Reopen:** a new edition changes a used principle, or cold-reader evidence shows that these moves no longer support the declared use. |
| How should plain prose address readers outside the author's specialty while retaining scientific content? | ISO 24495-3:2026, *Plain language — Part 3: Science writing*, Edition 1, current published standard (`https://www.iso.org/standard/86938.html`). | It extends the reader-sensitive principles of Part 1 to science writing for people with different backgrounds and interests. It expressly does not govern specialist scientific writing, and it supplies no test for FPF kinds or terms. | **Adapt — reason:** the cross-specialty reader boundary sharpens the cold-reader check without authorizing loss of technical content. **Receiving loci:** F.19:4.1 step 7 and `CC-F19-7`. **Qualification/currentness:** current for plain science communication, not proof that a specialist FPF distinction is dispensable. **Reopen:** the standard changes materially, or an F.19 case needs a different expert-to-expert boundary. |
| When is controlled technical language worth its added restriction and maintenance cost? | ASD-STE100, *Simplified Technical English: Standard for Technical Documentation*, Issue 9 (2025-01-15), current issue (`https://www.asd-ste100.org/`). | Its controlled vocabulary and writing rules reduce lexical and syntactic ambiguity in multilingual, safety-sensitive maintenance documentation. That setting does not show that a controlled dictionary, one-word/one-meaning rule, or compliance apparatus improves ordinary FPF prose. | **Reject as the default FPF language; adapt only as a comparison probe — reason:** F.19's cheap ordinary path remains better unless a declared high-risk multilingual use shows otherwise at comparable effort. **Receiving loci:** F.19:4.1 step 7 and `CC-F19-7`; no controlled-language machinery is imported. **Qualification/currentness:** current controlled-language practice with an aerospace-maintenance origin. **Reopen:** an F.19 case demonstrates that bounded restrictions outperform the ordinary path for its declared reader and risk. |
| What action-guiding detail must survive when the prose tells someone what to do? | IEC/IEEE 82079-1:2019, *Preparation of information for use (instructions for use) of products — Part 1: Principles and general requirements*, Edition 2, published and marked for revision (`https://www.iso.org/standard/71620.html`). | It distinguishes step-by-step instructions within information for use and treats usable instructions as purpose- and user-sensitive. Its full information-management process, competency scheme, and evaluation apparatus are much broader than a bounded F.19 rewrite. | **Adapt the action-preservation branch; reject the surrounding documentation process — reason:** sequence, condition, quantity, warning, and stop detail improve the worked case and checks, while the larger apparatus does not improve them at comparable effort. **Receiving loci:** F.19:4.1 steps 2 and 7, the operational-detail grounding case, and `CC-F19-2`/`CC-F19-4`/`CC-F19-7`. **Qualification/currentness:** current published product-information reference, already marked for revision. **Reopen:** its successor changes a used principle, or an F.19 case requires a further action detail. |
| Can legally constrained prose become clearer without losing controlled terms or obligations? | ISO 24495-2:2025, *Plain language — Part 2: Legal communication*, current published standard (`https://www.iso.org/standard/85774.html`); US SEC, *A Plain English Handbook: How to Create Clear SEC Disclosure Documents* (1998; SEC page 1999), retained lineage (`https://www.sec.gov/about/reports-publications/newsextrahandbook`). | The current standard shows that reader access can coexist with nuanced concepts, required structures, rights, and obligations. The SEC handbook is lineage for concrete, direct presentation. Neither source makes legal drafting or disclosure compliance part of ordinary FPF authoring. | **Adapt the meaning-preservation lesson; reject legal-process transfer — reason:** the branch supports necessary terms without importing a legal-document method. **Receiving loci:** F.19:4.1 step 7 and the kind-and-loss-preservation boundary. **Qualification/currentness:** ISO 24495-2 is current legal-communication guidance; the SEC handbook is lineage only. **Reopen:** F.19 acquires a legal-use case, or a later source changes the retained lesson. |
| What prevents a plain rewrite from changing an FPF claim while removing apparatus? | Current FPF patterns `E.8`, `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, `A.6.P`, and `E.21`, internal governing dependencies. | They recover the actual word, head, role- or function-shaped claim, relation, name, use, and quality loss before the sentence is shortened. They are not external evidence that F.19 is SoTA. | **Adopt as internal dependencies — reason:** they define, constrain, or test the meaning that F.19 must preserve. **Receiving loci:** F.19:4.1 steps 2–7, the ordinary-result boundary in F.19:4.3, conformance checks, and Relations. **Qualification/currentness:** current FPF dependencies, kept thin rather than copied here. **Reopen:** a dependency changes a distinction or check used by F.19. |

### F.19:12 - Relations

| Related pattern | Relation |
|---|---|
| `E.8` | In FPF authoring, keep positive practitioner-facing content and pattern form there; use `F.19` for the shared sentence, coordination, list, and foregrounding repair rather than maintaining a second algorithm. |
| `E.10` | Use its compact cues to notice likely candidates and its exact rows only for unresolved FPF wording. The final ordinary semantic disposition belongs to `F.19` or the subject pattern. |
| `E.10.ARCH` | Use the shared wording-use architecture only when subject, predicate, relation, representation, or another ontological value remains unresolved after ordinary reading. |
| `E.10.ROLE` and `A.6.F` | Route a genuinely unresolved role- or function-shaped claim once; `F.19` keeps the capable-subject and metonymy boundary without copying either taxonomy. |
| `F.18` | Use it for durable reusable names after kind and use are known. |
| `A.6.P` | Use it when the remaining content hides relation kind, endpoint, basedness, anchoring, slot, relation position, or use relation. |
| `A.19.SPR`, `C.2.P`, `C.16.P`, `C.30.P` | Use the applicable pattern for unresolved state-family, source or publication, characteristic or scale, and architecture or structure claims. |
| `E.17.EFP` | Reuse its reader-fit boundary only when a reader distinction changes explanation use; `F.19` does not require a persona record. |
| `E.21`, `E.19`, `E.22`, and `E.23` | Reviews and improvement work may use `F.19` findings while keeping their records and attention state outside practitioner prose. |
| `E.11` and `I.2` | First-entry and publication loci may use the same repair while returning semantic authority to the subject patterns. |

### F.19:End

