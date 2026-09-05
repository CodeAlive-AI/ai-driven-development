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

#### One connected reading and repair

1. **State the governing message.** Say what object, claim, action, event, or distinction the span needs to convey. Mark process traces, status language, reference boilerplate, quality proof, defensive caveats, ornamental detail, and other apparatus that may be displacing it. Apparatus receives no protection merely because it is true or polished.
2. **Recover the predicate and its participants.** Identify the operation and every participant that changes it. This may be an actor, object, source, target, result, or another required operand. Apply the same question to verbal and relational nouns: recover *of what*, *for what*, *between what*, or another required participant. Leave an argument implicit only when one intended value is cheaply and uniquely recoverable from the local span.
3. **Check predicate compatibility.** Recover what the complete claim asserts under its negation, modality, or conditions, and test the subject and participants under the intended literal or metonymic reading. A positive assertion must assign its predicate to a compatible kind. A denial may correct an evidenced type mistake under the plausible-reader test below; without that ground, “evidence does not notice the error” introduces an idle alternative. Keep ordinary metonymy when the relation is established and the capable participant or work remains recoverable: a diagram may show, a framework may help, a reminder may cue, and a constraint may limit.
4. **Resolve referents and kinds.** Pronouns, demonstratives, omitted heads, and repeated labels must select one locally appropriate referent. Preserve the object kind, claim or relation kind, slot or relation position, use and publication boundary, and flow distinction whenever one changes the claim. A shared grammatical position does not make different FPF kinds interchangeable.
5. **Test contribution.** Try deleting every optional contrast, guard, modifier, example, coordinated member, and extra proposition. Remove it when the plausible intended reader can still recognize, understand, decide, and act in the same way. Local truth and grammatical fit do not earn a phrase a place by themselves.
6. **Resolve coordination and lists on two axes.** First ask whether the receiving use needs a series at all. A list or parallel construction earns its form only when the reader must distinguish or retain its members together; otherwise select the governing claim, relation, or representative case. If a series is needed, determine its membership semantics. State the proposition or action it serves; use one kind or predicate only when it fits every member; distinguish a closed set, illustrative examples, alternatives, a sequence, several direct relations, and a failed ontology. A closed set needs its kind, membership rule, and closure. Illustrative examples need the proposition or kind first and a non-exhaustive cue when a plausible reader could mistake them for a classification. Then test discourse load: keep a member only when it adds a distinct consequence; reduce coordination repeated at several grammatical levels and modifier chains that make the reader retain needless branches or postpone the governing message. Length is evidence to inspect, not a verdict. If a list hides an FPF kind, relation, or structure that ordinary reading cannot recover, use the pattern that defines or tests it, or return the unresolved meaning as a blocker.
7. **Foreground, rewrite, and compare.** Put the governing event, claim, requested action, or decision before optional atmosphere, examples, caveats, and catalogues. A prerequisite may come first when it is needed for safe interpretation or action. Write the shortest ordinary technical sentence that preserves every live predicate and participant, established term, polarity, and action-changing detail. Such detail can include quantity or threshold, sequence or timing, criterion or tolerance, exception, and applicability. Compare before and after: any unsupported change of kind, relation, scope, use, currentness, or operational effect is a loss and blocks the rewrite unless another accepted decision authorizes it.

Keep ontology visible only where it carries the sentence. A term-source or type annotation is needed only when it changes how the reader identifies the object, kind, relation, slot, use, publication boundary, admissible use, or applicable rule. A record, card, table, schema, data structure, dashboard, or named form remains apparatus unless it carries one of those values. If ordinary domain wording already preserves them, keep the ordinary sentence. "The aircraft flies" is better than a typed expansion unless the flight function, system kind, or slot relation is under repair.

**Precision before a coarsened rendering.** When head kind, qualifier claim, or comparison basis remains unresolved in FPF-governed prose, use this working order:

Restore the head kind first; a narrowing qualifier such as `comparative`, `safe`, `interactive`, or `reliable` does **not** by itself restore that kind. Then unpack the qualifier claim, then check whether the comparison or escalation basis is homogeneous. Only after that may a later Plain, didactic, or coarsened rendering admissibly relax the sentence, while keeping the more precise upstream interpretation recoverable.

Judge homogeneity against the comparison or condition rule actually used; recover distinct relations separately when that rule combines them. The basis may be a homogeneous claim-kind criterion, threshold, or named defining, constraining, or source-relation condition.

Treat `exact`, `direct`, `current`, `governed`, `subject`, `owner`, `defining`, and similar qualifiers as content only when they distinguish live alternatives. Remove them when no such contrast changes the truth, action, stop, or reliance. A PatternID may remain an ordinary citation; expand it into a claim-bearing episteme, `ClaimGraph`, `U.MethodDescription`, `U.Method`, actor, assignment, `U.Work`, or another formal identity only when the current claim or a named later use depends on that distinction.

Keep ordinary practitioner action and instrumental pattern-use wording ordinary when it does not assert a particular dated Work occurrence. “Use `E.9` to record the decision” and “the framework maintainer compares the editions” need no invented Method, MethodDescription, performer, assignment, or Work identity.

Open the identity-bearing branch only when the sentence deliberately asserts a particular dated `U.Work` occurrence. Then point to its basis: A.13 first, independent A.15.1 Work admission second, and F.6 afterward only for precise assignment-bound attribution. Add a local system-role kind or a separate System-classification judgment only when that neighboring claim matters. Treat a pattern episteme as a `U.MethodDescription` only after `A.3.2` establishes that it has an already admitted Method as its `EntityOfConcern` and explains how that Method is performed. Otherwise cite the applicable pattern content as guidance and use `A.3.1` for the Method itself.

#### Plausible-reader guards and cold-reader recovery

Use two reader tests for different decisions.

- The **plausible intended reader** has the knowledge and task presupposed by the text. Use this reader to decide whether a foil, guard, warning, or contrast deserves mention. Do not substitute an adversarial reader who can imagine any false inference, or the author who already knows the answer.
- The **cold intended reader** lacks the author's private context and unpublished notes. Use this reader after the rewrite: they can recover the object, predicate, participants, relevant kind or ordinary status, relation, action-changing detail, and next useful action.

Retain a negative alternative, denied consequence, warning, or non-use statement only when the exact rejected reading has an independent local ground; a plausible intended reader could take that reading here, including an evidenced type mistake; and the distinction changes truth, understanding, selection, safety, stop, reliance, or action. An earlier or source claim, an observed recurring mistake, a serious competing position, a visible representation feature, or an applicable safety risk can supply the ground. The guard itself cannot.

Even a grounded guard should be the smallest clear correction. When actor allocation is the useful content, state it positively: “On receiving new evidence, the reader decides whether to reopen checking or revision.” When currentness is the useful content, state the direct use: “This guide conveys the seminar of 1 February 2026; check current rules against the current FPF edition.” Keep material negation, documented anti-patterns, fair disputes, and safety stops when their polarity or boundary is itself the claim.

#### Result and local revalidation

The ordinary result is the repaired text, or a blocker naming the unresolved meaning. Do not require a separate result form, card, table, progress row, or recorded answer for each facet of the reading.

After changing words or syntax, reread the changed sentence and only the nearby text needed to determine its referents, predicate, participants, contrast, modality, support, action, and result. The earlier semantic verdict does not transfer to new wording. Unchanged spans and conclusions remain reusable; a local edit does not trigger an automatic whole-document pass.

When a named high-risk or disputed decision needs inspectable evidence, show the before text, repaired text, live values that had to survive, and any unresolved blocker. Use the receiving decision's existing comparison or review result. The optional fields below can structure that result when its receiver needs them; ordinary corrections need no separate form.

If ordinary reading settles the issue, stop. Open `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, or an exact subject pattern only for a genuinely unresolved FPF word, kind, relation, role, function, name, source-use, or admissible-use question. A trigger helps find a candidate; it neither bans the wording nor closes the judgement.

#### F.19:4.1 - Result form

Use this optional form when the receiving decision needs the corresponding inspectable detail.

| Field | Meaning |
|---|---|
| `TextSpanRef` | Bounded span under repair. |
| `ApparatusCandidateSet` | Visible pattern-application, role, record, card, table, schema, data-structure wrapping, locus, flow, status, process, unsupported-negative-classification, reference, or quality-proof apparatus candidates. |
| `ContentCandidateSet` | Phrase parts that carry an object, claim, relation, value in `KindAndClaimMap`, action-guiding claim detail, flow position, evidence-use value, or user-facing action. |
| `ObjectOfConcern` | Object the span is about. |
| `KindAndClaimMap` | Head kind, claim kind, relation kind, current slot, relation position, use relation, publication relation when it changes admissible use, scope, and—when another pattern contributes—the pattern id plus what its content defines, constrains, or tests. |
| `ActionGuidingClaimDetails` | Only details consumed by the declared use: exact predicate and participants, polarity, quantity or threshold, temporal boundary and order, criterion, tolerance, exception, applicability condition, or another explicit operational distinction. Empty when none is current. |
| `FlowPosition` | Design, run, or coupled-flow position only when that position changes the claim or use. |
| `ApparatusDisposition` | Removed, moved, retained as content, or blocker when separation is not yet possible. |
| `RemainingContentPrecisionRestoration` | `not needed`, `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, a named pattern plus its concrete contribution, or blocker. |
| `PlainRewrite` | Short rewrite after apparatus removal and remaining-content precision restoration. |
| `KindPreservationCheck` | Pre-rewrite and post-rewrite object kind, relation or claim kind, current slot, relation position, use relation, admissible use, scope, and every `ActionGuidingClaimDetails` value; disposition is `preserved`, `split`, `intentionally changed by accepted decision`, or `blocker`. |
| `LossCheck` | What became false, less actionable, less local, less current, less recoverable, or less usable—including lost quantity, threshold, polarity, order, timing, criterion, tolerance, exception, or applicability condition—if the rewrite is accepted. |

#### F.19:4.2 - Pattern-prose specialization

When the repaired prose is an FPF pattern, apply the same method with one purpose test:

> Does this sentence help the pattern's intended user recognize and perform the pattern, or does it record development, review, projection, landing, quality, or source-management evidence about this version?

If it records evidence about the pattern version, keep that evidence outside the pattern unless the pattern's own primary `EntityOfConcern` is that evaluation or projection object. The evidence can cause edits to the pattern; it is not automatically pattern content.

Pattern prose keeps:

- the pattern's own primary `EntityOfConcern`;
- the first useful move;
- the practical delta and cost of missing it;
- a local boundary that passes F.19:4's full independent-ground, plausible-reader, contribution, and smallest-clear-correction test; and
- short references to related patterns after the pattern's own content is visible.

Public architectural reasons stay with the explanation when they help the intended user understand, select, combine, or adapt the Methods and profiles. Apply `E.8:4.2.3` to distinguish those reasons from the current version's development history.

Pattern prose moves out:


- rationale for the current draft's placement or promotion as a development decision;
- correspondence about producing or reviewing the draft rather than using the pattern;
- quality, projection, monolith-parity, landing, and source-management evidence; and
- repeated boundary doctrine already carried by another pattern.

### F.19:5 - Archetypal Grounding

These cases show repairs and situations in which ordinary wording should remain.

| Case | Before | Repair or disposition |
|---|---|---|
| Pattern use, ordinary | "`A.15` handles the work-planning claim." | "Use `A.15` to plan the work." |
| Pattern use, identity-bearing | "The pattern performed the planning." | "Engineer E performed planning Work W. Point to W's basis: A.13 first, independent A.15.1 Work admission second, and F.6 afterward only for precise assignment-bound attribution; use `A.3.2` only if a named episteme describes the enacted Method." |
| Pattern and relation, ordinary | "The governing relation is `C.29`." | "Use `C.29` to test whether the mathematical lens is admissible for this task." |
| Pattern and relation, identity-bearing | "`C.29` says so." | "If a comparison depends on the rule edition, cite the claim-bearing episteme and `ClaimGraph` that contain the admissibility rule." |
| Pattern-text purpose | "Pattern text must not contain corpus projection evidence." | "A pattern must not contain projection evidence about itself." |
| Evaluation scope | "The evaluation has pre-landing host-set use." | "This is a host-only evaluation; corpus-entry values need corpus-projection evidence." |
| Unsupported negative classification | "This Guide is not a seminar, not a transcript, but a learning route." No seminar-or-transcript confusion has been established. | "This Guide teaches the seminar's subject through explanations, examples, exercises, and checks." |
| Role-shaped label | "The platform owns scale." | "This scale compares platform and non-platform alternatives." |
| Publication and evidence mix | "The dashboard is the evidence gate." | "The dashboard presents evidence. Use `A.10` for the evidence claim and `A.21` for any gate decision." |
| Comparison, carrier, and publication mix | "E.4.PFIP preserves expression, carrier, and publication." | "The framework maintainer compares the predecessor and candidate publication expressions for the declared use. Use `E.10:0.2c.17` to separate the expression comparison from carrier-bearing and publication-occurrence claims." |
| Operational-detail loss | "Rewrite 'Boil for five minutes after simmer begins' as 'Cook until ready'." | "Reject the rewrite. It keeps a broad cooking action but loses the five-minute duration, start condition, and usable stop criterion." |
| Invented foil | “The concluding practical result is not a final scheme of the world, but the ability to problematize again.” | No live world-scheme reading is grounded. Write: “The concluding practical result is the ability to problematize again.” |
| Denied impossible agency | “The evidence does not notice the error and does not begin a new cycle.” | Evidence supplies grounds; a reader or system evaluates them. Write: “New evidence gives the reader grounds to check or revise the first distinction and decide whether to reopen the work.” |
| Unsupported currentness guard | “Historical modality does not turn the seminar claims into the current FPF norm.” | State the dated source and current-use action: “This guide conveys the seminar of 1 February 2026; check current rules against the current FPF edition.” |
| Missing operation operand | “Take the mixture and then pour.” | If the object or destination is not uniquely recoverable, restore it: “Pour the mixture into the flask.” |
| Incomplete relational noun | “Give the bearer to the next stage.” | Name what is borne and the transfer relation, or use the ordinary domain noun. |
| False common head | “The method selects, publishes, and evaluates the alternatives,” where the text combines unrelated activities and supplies no common Method or capable participant. | Recover the separate claims and participants. When the context instead supplies one Method and its capable executor, the same wording may be ordinary metonymy; the verb list alone is not a defect. |
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

These questions guide one connected reading; they do not require separate recorded answers. `KindPreservationCheck` names the comparison required of every rewrite. Its separate result form is optional under F.19:4.1.

| Check | Requirement |
|---|---|
| `CC-F19-1` | The repair names the text span and visible apparatus candidates before rewriting. |
| `CC-F19-2` | The repair separates apparatus from content by the values named in `KindAndClaimMap`, `ActionGuidingClaimDetails`, and `FlowPosition`; lexical dislike is not enough. Role- and function-shaped wording remains content until the connected reading or, for an unresolved claim, `E.10.ROLE` or `A.6.F` recovers it. |
| `CC-F19-3` | Apparatus is removed or moved before wording-use precision restoration is applied to the remaining content. |
| `CC-F19-4` | Content-bearing wording remains content; when ordinary reading leaves its meaning unresolved, it is repaired by `E.10`, `E.10.ARCH`, `F.18`, or the specific pattern that defines, constrains, or tests the remaining claim rather than deleted as style. |
| `CC-F19-5` | A removed apparatus word is not replaced by a synonym, metonymy, role label, container word, or status word that carries the same hidden apparatus. |
| `CC-F19-6` | Established FPF terms are preserved unless a named precision-restoration or naming pattern changes them. |
| `CC-F19-7` | Every accepted rewrite passes the `KindPreservationCheck` comparison; a change to object kind, relation or claim kind, current slot, relation position, use, scope, or a live action-guiding discriminant without an accepted decision remains a blocker. |
| `CC-F19-8` | Development, evaluation, projection, landing, use-found, repair, and source-management evidence stay in the evidence, projection, release, or publication loci that carry them unless the text is about that flow object. |
| `CC-F19-9` | The accepted rewrite is shorter or clearer without losing technical semantics or action-guiding detail. A longer rewrite is admissible only when it recovers a hidden kind, relation, role or assignment distinction, function claim, slot, claim boundary, quantity, threshold, polarity, order, timing, criterion, tolerance, exception, or applicability condition needed by the declared use. |
| `CC-F19-10` | The repair records any loss of truth, action, stop criterion, value, usability, locality, currentness, kind recoverability, or explicit operational detail used by the declared reader. |
| `CC-F19-11` | Term-source or type annotation is used only when it changes the object, kind, relation, slot, use, publication boundary, admissible use, or rule the reader must apply; stable ordinary prose is not expanded into type labels. |
| `CC-F19-12` | The accepted plain rewrite passes MG-DA cold-reader recovery: a reader without the `DRR`, campaign notes, or author memory can state the content-bearing object, kind or ordinary status, relation or claim position, admissible use, next practical action, and every quantity, threshold, ordering, timing, criterion, exception, or applicability condition that changes that action. When another pattern contributes, the reader can recover its id and contribution. Broad heads such as `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, and unqualified `specialization` are not plain enough when they hide what the practitioner must recognize. |
| `CC-F19-13` | Every added qualifier or formal identity has a named live contrast: it changes truth, action, stop, migration, publication, reuse, or reliance. An ordinary PatternID citation does not by itself require a `ClaimGraph`, `U.MethodDescription`, `U.Method`, actor, assignment, or `U.Work` expansion. |
| `CC-F19-14` | After apparatus removal, the sentence names every complement and live discriminant needed to determine what was selected, changed, compared, transformed, published, evaluated, relied on, started, stopped, ordered, limited, or excepted. |
| `CC-F19-15` | Ordinary practitioner action and instrumental “use pattern X” wording stays ordinary when it does not assert identity-bearing dated Work. When it does, point to the basis: A.13 first, independent A.15.1 Work admission second, and F.6 afterward only for precise assignment-bound attribution. Use one thin `E.10.ROLE` or `A.6.F` route for a role- or function-shaped trigger; do not copy either recovery taxonomy. `U.MethodDescription` appears only after the `A.3.2` test passes. |
| `CC-F19-16` | A heterogeneous list is split when its members need different heads or predicates; the rewrite uses the coordination-and-list move in F.19:4 instead of inventing one umbrella head, with `E.10:0.2c.17` only for an unresolved FPF kind or relation. |
| `CC-F19-17` | A negative alternative remains only when it passes F.19:4's full independent-ground, plausible-reader, contribution, and smallest-clear-correction test. Without that ground and contribution, the sentence states the positive object, relation, action, or result directly. Problem statements, disputes, material polarity, and documented anti-patterns remain content. |
| `CC-F19-18` Governing message | The intended reader and use are clear, and the governing object, claim, event, action, or distinction appears before optional apparatus. |
| `CC-F19-19` Semantic completeness | The predicate, required participants or operands, relational-noun complements, and local referents are recoverable without author memory or a reference puzzle. |
| `CC-F19-20` Predicate and kind fit | Interpret the complete predicate with its negation and modality. Positive assignments are kind-compatible under the intended literal or metonymic reading; a denial of a type mistake passes the grounded-contribution test. Preserve object kind, claim or relation kind, slot, relation position, use, and publication boundary where they change meaning. |
| `CC-F19-21` Meaning and loss preservation | The rewrite preserves every live term, polarity, quantity, threshold, temporal or ordering condition, criterion, tolerance, exception, applicability boundary, and other action-changing detail. Any accepted change of kind, relation, scope, currentness, or use has its own decision. |
| `CC-F19-22` Grounded contribution | Every optional guard, contrast, modifier, example, and coordinated member changes recognition, understanding, evidence, decision, safety, stop, reliance, or action for a plausible intended reader. A negative alternative has an independent local ground and is the smallest clear correction. |
| `CC-F19-23` Coordination and foregrounding | A list states the proposition or action it serves; its kind, predicate, membership semantics, and closure are not fabricated; illustrative status is clear when needed; and coordination or modifiers do not postpone the governing message. |
| `CC-F19-24` Plain result | A cold intended reader can recover the repaired claim and next useful action. The ordinary output is repaired text or a blocker, not a mandatory form or ledger. |
| `CC-F19-25` Local revalidation | Any changed wording or syntax has been reread with only its meaning-dependent neighbours. An older semantic verdict is reused only for unchanged text. |

### F.19:8 - Common anti-patterns and how to avoid them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Lexical paint | One umbrella word is replaced by another while the object kind stays hidden. | Recover the object kind and rewrite in the object's technical name. |
| Hypergeneric repair | The rewrite uses `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, or `specialization` to sound precise while hiding the actual object, relation, rule, or action. | Restore the practitioner-recognizable object and relation; for specialization, say what specializes what, by which specialization relation, and which inherited or changed slots or uses matter. |
| Plain-language drift | Smooth prose drops the kind named by value or admissible-use boundary. | Remove apparatus first, then restore remaining wording precision before shortening. |
| Flow smuggling | Development, projection, landing, or evaluation evidence is written as user-facing guidance. | Move the evidence to the review record, quality result, projection record, release document, or other appropriate evidence document and keep only the resulting user-facing action or boundary. |
| Role-shaped label as ontology | The word *role* is treated as one technical value or replaces the object kind. | Keep the phrase as content; use `E.10.ROLE` when ordinary reading leaves the actual claim unresolved; do not infer a branch from the word alone. |
| Function-shaped label as ontology | The word *function* is treated as one technical value or as proof of functioning, capability, assignment, or Work. | Keep the phrase as content; use `A.6.F` when ordinary reading leaves the claim unresolved; allow metonymy or several simultaneous readings without copying its dispatch here. |
| False common head | One grammatical subject is made to select, compare, carry, publish, and evaluate unlike things. | Split the claims using F.19:4's coordination-and-list move; use `E.10:0.2c.17` for unresolved FPF meaning and retain only heads that fit every listed member. |
| Slot label as ontology | A slot, field, relation-position, or use-relation label replaces the object kind, or the same object in several slots or relation positions is treated as several kinds. | Preserve object kind, slot, relation position, and use separately; cite the specific pattern only when its definition, constraint, or test is needed. |
| Apparatus-looking data structure | A record, card, table, schema, dashboard, or data-structure word is kept because it sounds precise, but it does not carry the EntityOfConcern, slot relation, publication boundary, admissible use, or next action. | Remove it, or use `E.24.CD`, `E.24.PUB`, or the specific content pattern when the structure really carries a candidate-ontic, publication, or domain relation. |
| Unsupported negative classification | The sentence introduces one or more alternative classes only to reject them, although the exact reading fails F.19:4's grounded-contribution test. | State the positive object and action. Retain a negative alternative only under the full independent-ground, plausible-reader, contribution, and smallest-clear-correction test. |
| Over-annotation as precision | The rewrite replaces a clear domain sentence with type labels, source-ontology tags, or slot names that do not change the claim. | Keep the domain sentence and annotate only the term or relation under repair. |
| Triggerless formal expansion | A PatternID citation becomes an “exact direct current subject owner”, `ClaimGraph`, Method, actor, assignment, or Work claim even though no alternative identity changes the result. | Keep the ordinary citation and action. Open the formal branch only after naming the contrast or later use that consumes it. |
| Overformalized precision | The rewrite preserves all terms but makes the sentence harder to think with or generalize from. | Keep the content-bearing kind and claim, drop apparatus that changes neither, and use a plain technical sentence plus a reference named by value where needed. |
| Apparatus-preserving paraphrase | A rewrite changes wording but keeps the same status, process, or quality-proof apparatus. | Return to the apparatus-and-content split and repair by value. |
| Truthful noise | A true denial or caveat answers an implausible question introduced by the sentence itself. | Remove the invented question and state the positive claim or action. |
| Impossible agency under denial | An incapable subject receives a predicate only so the prose can deny it. | Name the capable participant and allocate the action positively. |
| Missing operand as elegance | A verb or relational noun omits the value that determines the operation or relation. | Restore the participant unless one intended value is cheaply and uniquely local. |
| Enumeration as coverage | Examples, near-synonyms, abstract pairs, or several kinds simulate breadth but do not state a usable proposition. | Put the proposition first; mark examples; retain only independently consequential members. |
| Locally valid accumulation | Every pair or modifier passes alone, but nested coordination creates a catalogue and delays the message. | Summarize, subordinate, split, or delete by contribution and foreground the governing clause. |
| Trigger as verdict | A word list bans normal metonymy, negation, long sets, or expressive prose, or its silence is treated as clearance. | Use triggers only to locate candidates; decide from the whole span and declared use. |
| Checklist explosion | One semantic reading becomes separate forms or progress items for valency, agency, kind, referent, lists, and style. | Perform one connected repair and return the repaired text; use comparison evidence when the receiving decision needs it. |

### F.19:9 - Consequences

Technical prose becomes easier to trust and use because every asserted relation has supported participants, every retained guard answers a plausible question, and lists serve a visible proposition or action. The pattern also removes a source of stylistic copying: authors no longer see defensive truth, false symmetry, and exhaustive-looking catalogues presented as the normal shape of precision.

The cost is one semantic reread of the changed wording and its meaning-dependent neighbours. That cost stays local. Ordinary correction produces repaired text; only a named high-risk or disputed decision needs comparison evidence.

### F.19:10 - Rationale

Precise plain language has two obligations. The sentence must be semantically complete enough to recover its predicates, participants, referents, kinds, and operational detail. Every additional structure must also earn its place by changing understanding or use for the intended reader. Either obligation alone is insufficient: a fully typed sentence can still be noise, and a short sentence can still hide its object.

The order of repair therefore matters: recover the governing message and relations, remove unsupported structure and displaced apparatus, then write the shortest ordinary sentence that preserves the live meaning. `E.10` remains a cue and a route for unresolved FPF wording; it is not a rival normal-pass algorithm. Attention management remains outside the language pattern.

### F.19:11 - SoTA-Echoing

`SoTA` here means the best current contribution to the stated practice question, not the newest or most formal publication. The plain-language comparisons were qualified on 2026-08-19; the negative-parallelism row uses research published on 2026-08-20 and checked on 2026-09-01. A source's official status does not by itself make it SoTA.

**Bounded choice for ordinary technical prose.** Compare the audience-sensitive whole-span reading with cue-led sentence revision: find listed suspect expressions, improve their wording, and retain true ontological distinctions. The latter was the working default in the R11 case. It left “The evidence does not notice the error and does not begin a new cycle” after fluent rewriting because those verbs were outside the selector and the denial was true. With the same paragraph available, F.19's reading recovers the reader's already stated checking or revision, finds no independently grounded reader mistake that the denial prevents, and deletes the denial. The positive action stays; no new action is inferred from the deleted sentence.

Use one bounded reread of the same paragraph or short instruction as the comparison allowance. On the ordinary sentence “The diagram shows the dependency”, both approaches retain the wording; F.19 expressly preserves its recoverable metonymy. On the operational-detail case, applying either approach with meaning preservation rejects “Cook until ready”: it discards “five minutes after simmer begins”. The additional F.19 move is to examine the contribution and participants of an unflagged proposition, rather than taking a clear and locally true sentence as sufficient. **Adapt the audience-sensitive line** in F.19:4 steps 1–7 and `CC-F19-9`/`CC-F19-12`/`CC-F19-17`; keep lexical cues for recall. The accepted trade-off is a contextual judgement about each claim, including unflagged claims, instead of a fully mechanical vocabulary check. These are qualitative case comparisons, not measured timing or a controlled-language compliance test. Reopen the choice if that judgement repeatedly rejects useful prose or a lighter method catches the same defects while preserving the same uses.

| Practice question | Exact source and status | Selected payload and limit | Source-use decision, receiving locus, qualification, and reopen |
|---|---|---|---|
| How should ordinary technical prose help its intended reader act without being "dumbed down"? | ISO 24495-1:2023, *Plain language — Part 1: Governing principles and guidelines*, current published foundation (`https://www.iso.org/standard/78907.html`); Digital.gov, *Principles of plain language* and *Writing for understanding*, current living US-government practice guide (`https://digital.gov/guides/plain-language/principles`, `https://digital.gov/guides/plain-language/writing`), checked 2026-08-19. | Declare the reader and task; put the usable object and action first; organize for finding, understanding, and use; keep terms the intended reader needs. Neither source defines FPF ontology or requires expert prose to use general-public vocabulary. | **Adapt — reason:** these moves improve F.19's ordinary path without changing its semantic boundary. **Receiving loci:** F.19:0 first useful move; F.19:4 steps 1 and 7; `CC-F19-9` and `CC-F19-12`. **Qualification/currentness:** current standard and current practice guide, not FPF semantic authority. **Reopen:** a new edition changes a used principle, or cold-reader evidence shows that these moves no longer support the declared use. |
| How should plain prose address readers outside the author's specialty while retaining scientific content? | ISO 24495-3:2026, *Plain language — Part 3: Science writing*, Edition 1, current published standard (`https://www.iso.org/standard/86938.html`). | It extends the reader-sensitive principles of Part 1 to science writing for people with different backgrounds and interests. It expressly does not govern specialist scientific writing, and it supplies no test for FPF kinds or terms. | **Adapt — reason:** the cross-specialty reader boundary sharpens the cold-reader check without authorizing loss of technical content. **Receiving loci:** F.19:4 step 7 and `CC-F19-12`. **Qualification/currentness:** current for plain science communication, not proof that a specialist FPF distinction is dispensable. **Reopen:** the standard changes materially, or an F.19 case needs a different expert-to-expert boundary. |
| When is controlled technical language worth its added restriction and maintenance cost? | ASD-STE100, *Simplified Technical English: Standard for Technical Documentation*, Issue 9 (2025-01-15), current issue (`https://www.asd-ste100.org/`). | Its controlled vocabulary and writing rules reduce lexical and syntactic ambiguity in multilingual, safety-sensitive maintenance documentation. That setting does not show that a controlled dictionary, one-word/one-meaning rule, or compliance apparatus improves ordinary FPF prose. | **Reject as the default FPF language; retain as a conditional alternative — reason:** the ordinary cases above require recovering contribution and preserving meaning, with no demonstrated need for a maintained controlled lexicon. They do not establish how an STE-compliant treatment would perform. A multilingual maintenance use can justify that separate restriction and its maintenance cost. **Receiving loci:** F.19:4 step 7 and `CC-F19-9`/`CC-F19-12`; no controlled-language machinery is imported. **Qualification/currentness:** current controlled-language practice with an aerospace-maintenance origin. **Reopen:** an F.19 case demonstrates that bounded restrictions outperform the ordinary path for its declared reader and risk. |
| What action-guiding detail must survive when the prose tells someone what to do? | IEC/IEEE 82079-1:2019, *Preparation of information for use (instructions for use) of products — Part 1: Principles and general requirements*, Edition 2, published and marked for revision (`https://www.iso.org/standard/71620.html`). | It distinguishes step-by-step instructions within information for use and treats usable instructions as purpose- and user-sensitive. Its full information-management process, competency scheme, and evaluation apparatus are much broader than a bounded F.19 rewrite. | **Adapt the action-preservation branch; reject the surrounding documentation process — reason:** sequence, condition, quantity, warning, and stop detail improve the worked case and checks, while the larger apparatus does not improve them at comparable effort. **Receiving loci:** F.19:4 step 7, `ActionGuidingClaimDetails`, the operational-detail case, and `CC-F19-9`/`CC-F19-10`/`CC-F19-14`. **Qualification/currentness:** current published product-information reference, already marked for revision. **Reopen:** its successor changes a used principle, or an F.19 case requires a further action detail. |
| Can legally constrained prose become clearer without losing controlled terms or obligations? | ISO 24495-2:2025, *Plain language — Part 2: Legal communication*, current published standard (`https://www.iso.org/standard/85774.html`). | The current standard shows that reader access can coexist with nuanced concepts, required structures, rights, and obligations. It does not make legal drafting or disclosure compliance part of ordinary FPF authoring. | **Adapt the meaning-preservation lesson; reject legal-process transfer — reason:** the branch supports necessary terms without importing a legal-document method. **Receiving loci:** F.19:4 step 7 and the plain-language-drift and synonym-churn boundaries. **Qualification/currentness:** current legal-communication guidance. **Reopen:** F.19 acquires a legal-use case, or a later source changes the retained lesson. |
| Which recurring AI-writing form deserves a contextual reread? | Pew Research Center Data Labs, [How Much of the Internet Is Written With AI?](https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/), with [methodology](https://www.pewresearch.org/data-labs/2026/08/20/methodology-ai-content/), published 2026-08-20; checked 2026-09-01. | In dated English Common Crawl pages published after 2022-11-30, the six-month averages plotted at 2023-01 and 2026-01 show negative parallelism rising from 0.87 to 2.36 uses per 10,000 words, while remaining rare. The whole study sampled 490,000 pages; its dated subset is not a random sample of the whole web. | **Adapt as a recall cue:** inspect contrasts such as `not X, but Y` through F.19:4's contribution and plausible-reader tests and `CC-F19-17`/`CC-F19-22`. Frequency does not decide whether a particular contrast is useful or who wrote it. **Reopen:** changed measurement, or actual-use evidence that the cue misses defects or rejects useful contrasts. |
| What prevents a plain rewrite from changing an FPF claim while removing apparatus? | Current FPF patterns `E.8`, `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, `A.6.P`, and `E.21`, internal governing dependencies. | They recover the actual word, head, role- or function-shaped claim, relation, name, use, and quality loss before the sentence is shortened. They are not external evidence that F.19 is SoTA. | **Adopt as internal dependencies — reason:** they define, constrain, or test the meaning that F.19 must preserve. **Receiving loci:** F.19:4 steps 2–7, the result form, conformance checks, and Relations. **Qualification/currentness:** current FPF dependencies, kept thin rather than copied here. **Reopen:** a dependency changes a distinction or check used by F.19. |

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
| `E.21` | An `E.21` evaluation may use `F.19` findings through `PrecisionRestorationProfile` and lower affected quality coordinates without creating one coordinate per apparatus symptom. |
| `E.19`, `E.22`, `E.23` | During review, framing, or improvement-loop work, use `F.19` while keeping quality-loop records out of pattern prose. |
| `E.11` and `I.2` | First-entry and publication loci may use the same repair while returning semantic authority to the subject patterns. |

### F.19:End

