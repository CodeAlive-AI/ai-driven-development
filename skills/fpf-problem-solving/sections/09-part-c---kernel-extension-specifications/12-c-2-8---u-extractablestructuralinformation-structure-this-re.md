## C.2.8 - `U.ExtractableStructuralInformation` — Structure This Reader Can Recover

> **Type:** Definitional (D)
> **Status:** Draft
> **Normativity:** Normative unless explicitly marked informative.

### C.2.8:1 - Problem frame

Use this pattern when an explanation, pattern text, architecture account or another expressed description must make selected structure recoverable by a particular reader or computational observer. You may be comparing two forms of the same account, deciding whether an added explanation exposes a missing dependency, or checking what an observer can extract with the available preparation and time.

**First useful move.** Name the relation or distinction the reader needs, identify the available account and its form, and state the preparation, source access and budget that can change recovery. Compare what the reader can correctly recover under those conditions. A useful result can be two sentences: “Both accounts expose the dependency on a durable write. Only the second account exposes why the reporting replica was chosen; this is an author estimate for readers familiar with replication, with the same source access and three-minute budget.”

The primary subject is **extractable structural information**: how much selected structure this reader or observer can correctly extract from this episteme through this form under the stated conditions. Here an *episteme* is the claim-bearing account; its *form* is how those claims are expressed. Prose, a diagram and a combined presentation may express the same claims differently.

**What goes wrong if missed.** Complete sentences or a shorter explanation can hide a needed condition. An expert may supply it from memory, so a correct answer can conceal what the account failed to explain. Comparing readers with different preparation or assistance can then make one text appear to expose more structure.

**What this buys.** One common structural question across forms and readers. The author can identify an additional recoverable dependency, preserve a sufficient explanation, or name the precise missing source or prerequisite.

Use an ordinary reading correction directly when the missing relation is already clear and no structural comparison is needed. Use the applicable task or learning evaluation when the live question is performance, burden, retention or transfer. This pattern supplies the structural-information characteristic those evaluations may consume; it does not select an explanation-design method or a universal quality score.

### C.2.8:2 - Problem

How can an author or evaluator compare structural recovery while distinguishing the account, its expression, the reader and the conditions of extraction?

A diagram may make dependencies visible without changing the described system. An added prerequisite explanation may change the claims as well as their expression. Two complete accounts may expose different structures within a short reading budget. A successful response can also depend on help that was unavailable for another response. The comparison needs to preserve these differences while retaining one meaning for structural amount.

### C.2.8:3 - Forces

| Force | Tension |
| --- | --- |
| Common aspect and diverse uses | The same structural question applies to a human reading a method and a program inspecting a graph, while their admissible operations and evidence differ. |
| Explicit articulation and bounded extraction | A complete semantic form can still demand more reconstruction than the reader's budget allows. |
| Preparation and attribution | Prior knowledge enables decoding and inference, but it can also repair a defective account independently. |
| Structural gain and practical choice | More selected structure is the positive direction of this characteristic; the extra recovery may still cost more than the task warrants. |
| Comparable values and honest limits | Numbers help a declared comparison, while a changed denominator, unvalidated estimator or absent observation can make them misleading. |

### C.2.8:4 - Solution

#### C.2.8:4.1 - Recover the structural question

Begin with the reader's needed understanding or action. Select the structure that matters to it: for example, a distinction between two alternatives, the dependency that orders two actions, or the reason a design choice changes under a new condition. A study of structural information may instead select a structure family for that research question. Selection need not assign task utility.

Identify the account and form being used. State only the conditions that could change the comparison: relevant concepts and notation the reader can use, available inference or inspection operations, accessible sources and help, and the effort or computation budget. A qualification or course title may locate evidence of preparation; it does not specify the usable knowledge by itself.

Then recover or estimate the selected structure and compare it with the relevant source or correctness criterion. Retain what each expression contributes, what remains missing and what a source return or prerequisite supplies. Reuse a sufficient current result. A new reading trial is useful when its possible outcomes could change the explanation or receiving decision.

Stop when that structural comparison answers the current question. If the selected structure or correctness basis is unresolved, return that gap before assigning an amount. If the practical question is whether a proposed change is worthwhile, use C.11.CRC and C.11 with extraction effort and task value stated separately.

#### C.2.8:4.2 - Characteristic and arity

**Tech name:** `U.ExtractableStructuralInformation`. **Plain name:** structure this reader or observer can extract. `ESI` is an abbreviation after the full name has been introduced.

This is an A.17 `U.RelationCharacteristic`, with arity three over the ordered tuple:

```text
(expressed episteme E, expressing publication form P, reader or observer O)
```

Its aspect is the amount of selected structure correctly extractable from E through P by O under stated comparison conditions. The characteristic is a dependent characteristic, not a root U-kind.

E retains its C.2.1 identity. P is the entity expressing that episteme in the applicable E.24.PUB publication-form relation and retains the more specific kind supplied by its form pattern. O is the specified human or computational observer. An estimate about a reader class states the relevant preparation and variation among its members; it does not treat the class as another individual reader.

Where exact notation helps, write `ESI_C(E, P, O)`. C fixes the selected structure, correctness criterion, relevant prior knowledge, usable operations, available assistance and tools, access conditions, budget and any other qualification that changes interpretation. These conditions qualify the characteristic of the tuple; they are not an additional bearer or a universal record kind.

Changing only expression can retain E. Adding, omitting or changing substantive claims can identify another episteme; use C.2.1 and the applicable source-to-target rule for that claim. In an explanation use, E.17.EFP's first screen distinguishes those branches when the difference matters. A comparison of forms alone holds the expressed claims constant.

The presentation carrier belongs in the access conditions when rendering, resolution, searchability or availability affects extraction. Changing access can change the qualified result while E and P remain the same. Attribute that difference to the changed access conditions. Ordinary references to a page, diagram or file are sufficient when they identify the required account and expression without ambiguity.

#### C.2.8:4.3 - Correct recovery and the expression's contribution

Correct recovery preserves the selected relation's participants, predicate, polarity, modality and action-changing conditions under the declared source or criterion. State the unit of structure only as precisely as the comparison needs. A qualitative result can name additional and missing dependencies directly; a count must also define its granularity.

Repeated expression of the same relation does not add structural amount merely by increasing words, boxes or arrows. A count of edges in a representation needs a correspondence to the selected semantic relations before it can count those relations.

Keep two questions distinct when the source contains a false or unsupported claim. A reader may correctly recover that the account asserts that claim. Establishing the claim about the described world requires its subject and evidence criteria. For recovery of warranted source structure, an unsupported relation does not count as a correct member. Recovering the assertion and endorsing its content are different results.

Prior knowledge may supply vocabulary, notation and inference used to decode the expression. A reader who independently corrects false text from memory has supplied a correction; the text does not receive credit for that corrected relation. When attribution matters, preserve the initial response and identify actual assistance and source returns before interpreting the observed difference. An explanation can expose already familiar structure: ESI is not restricted to newly learned information.

#### C.2.8:4.4 - Positive direction and scale choice

More selected structure correctly extractable under comparable conditions is the positive direction of ESI. If one result includes every correctly recoverable selected relation of another and adds selected relations, it has the positive structural direction. If each exposes something the other does not, retain that trade-off unless a justified scale resolves it.

A scale can be ordinal, a count, a fraction, a nonnegative structural weighting or a bit estimate. Its meaning and method must fit the declared use. A fraction has a fixed denominator; a weighted amount has an explicit structural interpretation. Changing the selected structure, granularity, denominator or weights changes the comparison basis. A task-utility weighting defines a separate score rather than silently becoming structural amount.

An ordered ESI scale declares the positive direction under A.17/A.18. A numeric comparison uses only operations legal for that scale. C.16 supplies the measurement chain when a measurement is claimed: the tuple and measurand, scale, method and model, obtained result and relevant uncertainty. Qualitative comparisons and conditional design estimates remain available without a validated human bit estimator.

A missing observation, unspecified denominator or unresolved criterion is missing basis for a value. It is not an observed zero. A zero has meaning only under a defined scale and a result that supports it.

#### C.2.8:4.5 - Reading results, estimates and robustness

A design walkthrough, an actual reading and a formal-model estimate can concern the same characteristic. State which grounds the assertion and the conditions at which it applies.

An observed response establishes the structure recovered in that trial and can ground an estimate of what is extractable. One success does not establish a maximum or reliability for a population; one failure does not establish impossibility. A computational procedure can support an exact bounded result when its operation and selected structure make that result derivable.

Repeat or perturb a reading when the receiving use needs a claim about robustness or transfer. Preserve the first response before giving a changed condition or further help. Success under the new condition strengthens the corresponding changed-condition claim; it does not add structure to the original result by itself.

For a cold-reader check, obtain the instruction from the publication, its declared prerequisites and the knowledge presupposed for the intended reader. The task may supply case facts. If it supplies the missing explanation of the instruction, the response shows use of that added explanation. Use F.19 to repair the publication before claiming that the publication itself supplied the action.

Absence of human validation restricts empirical claims about people. It does not restrict ESI to computational observers or prevent a conditional author estimate about a human reading situation.

#### C.2.8:4.6 - Relation to epiplexity and MDL

A formal structural-information estimate is useful when a mathematical model can represent the selected account, observer and extraction question. Use C.29 for that correspondence and its preserved and lost structure.

Finzi et al.'s computational epiplexity selects a time-bounded probabilistic program by a two-part coding criterion:

```text
P* = argmin over P in P_T of ( |P| + E[-log2 P(X)] )
S_T(X) = |P*|
H_T(X) = E[-log2 P*(X)]
```

Ties select the shorter program. The model term describes structural information; the residual is time-bounded entropy. Conditional versions allow side information, and practical estimators have their own assumptions. The execution bound and the effort of finding or estimating a model are distinct costs. [Finzi et al., v2, §3–4](https://arxiv.org/pdf/2601.03220v2)

For an ESI estimate, explain how the episteme and expression map to X, how the model class represents the observer's available operations, and which selected structure the model term estimates. State how prior knowledge is represented. Conditional model description given side information need not count all familiar structure a reader can recover.

Use epiplexity as a formal specialization where that correspondence holds. Otherwise it motivates the structural-information question without supplying its value. Total code length, text length and arbitrary model size are not interchangeable ESI measures. Ordinary description comparisons may use an adequate domain method without a coding model.

#### C.2.8:4.7 - Articulation, effort and useful change

C.2.4 `U.ArticulationExplicitness` orders progression from a cue to explicit branch-appropriate meaning and stable receiving use. ESI compares the selected structure extractable by an observer under a budget. Two complete descriptions at the same AE level can have different ESI; a reader's difficulty alone does not establish that the semantic branch was left unarticulated.

Measure or compare extraction effort separately. Two expressions may expose the same structure at different cost. Additional selected structure may also be irrelevant to the next task or displace more valuable work. C.11.CRC/C.11 make the marginal choice using the structural result, cost, protected results and receiving value. The chosen result may be the current sufficient explanation.

Use the method appropriate to the proposed change: C.37 for selecting representations, A.6.3.NAR for narrative ordering and source carry-through, or the applicable domain description or instructional method. ESI states the aspect being compared; it does not prescribe adding a diagram, example or lesson.

### C.2.8:5 - Archetypal Grounding

#### C.2.8:5.1 - Architecture account in prose and a diagram

A service account states:

> The API returns “stored” only after the Store confirms a durable write. Reports read a Replica updated from Store and may lag by five minutes. A synchronous report query to Store was rejected because report bursts must not delay request writes. If required report freshness becomes one second, reconsider the replica update design.

A second expression adds this diagram while retaining those four sentences:

```text
API --write--> Store --update--> Replica --read by--> Reports
API <--durable-write confirmation-- Store
```

The reader is an engineer familiar with durable writes and replicas. Select the acknowledgment dependency, report-source/lag relation, rejected alternative with its reason, and reconsideration condition. Both forms expose the same claims; the described architecture is unchanged. Compare recovery with the same three-minute budget and source access. The diagram's presence alone establishes no advantage.

Suppose a reading trial recovers three selected relations from the prose and all four from the combined expression. Report that bounded observed difference and identify the additional relation. If a source paragraph was supplied only before the second reading, the comparison also changed assistance. If the same reader encountered both forms, previous reading may contribute. These conditions prevent attributing the whole difference to form alone.

A reader unfamiliar with replication may need a prerequisite explanation. Adding its substantive claims changes the account as well as its expression. If the design requirement changes to one-second freshness, the account supplies reconsideration of the replica update design. It does not supply a replacement architecture. C.33 can record this captured structure and the source return needed for the next design question.

#### C.2.8:5.2 - A technical pattern's explicit plan

The plan in C.2.4:13.2 names Maintenance Team 2, Pump P-17, isolation, seal replacement and restoration only after LT-9 passes. For its planning use, the actor, action order and condition are explicit enough for AE4. A maintainer can recover the restore-after-pass dependency even when the note does not explain the LT-9 procedure.

If the selected use is carrying out that test, the applicable procedure must be available as a prerequisite or source return. The plan's articulation result does not teach the missing procedure. The useful ESI comparison names which required test relations the reader can recover with the available source access; it does not replace the planning judgment with a larger or smaller AE number.

#### C.2.8:5.3 - An observer with a two-statement budget

Let E describe edges A→B, B→C, A→D and D→C. Form P1 lists them in that order. Form P2 lists A→B, A→D, B→C, D→C. Observer O reads the first two edge statements and returns every two-edge path supported by those edges. Select the paths A→B→C and A→D→C as the structural denominator.

P1 gives O the edges needed for A→B→C; P2 gives two edges leaving A and no complete selected path. Under the declared count, the results are 1 and 0 out of two selected paths. With four statement reads, the same procedure recovers both paths from both forms.

This result follows from the stated algorithm and budget. It is neither a human-comprehension observation nor a Finzi estimate. It shows one characteristic applied to the same expressed claims under a precisely bounded computational observation.

#### C.2.8:5.4 - A whole-framework architectural rationale

A framework maintainer has several individual pattern-quality results and needs to decide what they establish about the framework as a whole. E.4.FPF:3–4 explains the different questions: E.21 evaluates a pattern; E.2.DA evaluates whole-FPF Pillar adequacy. The selected structure is this relation between the two scopes and the corresponding return.

For a reader who can already use those evaluation questions, the existing rationale and direct links may be sufficient. A less prepared reader may need the questions explained before the links are useful. An ESI comparison checks recovery of that scope distinction and next return under stated preparation and access. Counting the account's headings would not answer it.

### C.2.8:6 - Bias-Annotation

Selecting only easy or already familiar relations can make an account look strong while excluding what the receiving use needs. Derive the selection from that use or a declared research question before comparing expressions, and retain consequential losses.

Author familiarity can hide a prerequisite or make a correct expert response seem attributable to the text. Preserve actual help and source use when that distinction affects the conclusion. For a reader class, state relevant variation rather than treating one prepared reader as representative of everyone.

A coding model can privilege structure useful to its model class. Keep that selection and its correspondence visible when applying the estimate elsewhere.

### C.2.8:7 - Conformance Checklist

Use this checklist when a characteristic claim or comparison must be relied on or carried to another use. An ordinary local comparison may keep the same information in prose.

| Check | Required content |
| --- | --- |
| `CC-C.2.8-1` Aspect and arity | An ESI claim SHALL retain the episteme, expressing form and observer, with the selected structure and material comparison conditions recoverable. |
| `CC-C.2.8-2` Correctness | The claim SHALL state the relevant source or criterion and distinguish content recovery from a stronger warranted-world conclusion when that distinction matters. |
| `CC-C.2.8-3` Comparison | A claimed difference SHALL identify changed claims, form, preparation, access, help, operations or budget where they can explain the result. |
| `CC-C.2.8-4` Scale | A numerical value SHALL name its scale, structural unit or denominator and method. Ordered scales SHALL retain the positive structural direction; missing basis SHALL remain distinct from zero. |
| `CC-C.2.8-5` Grounds | An observation, design estimate or formal-model estimate SHALL retain its grounds and their actual scope. Prior-expertise correction and additional assistance SHALL be attributed separately where consequential. |
| `CC-C.2.8-6` Formal estimate | An epiplexity or other mathematical estimate used as ESI SHALL have the applicable C.29 correspondence; a claimed measurement SHALL satisfy C.16. |
| `CC-C.2.8-7` Distinct results | Amount SHALL remain distinguishable from articulation, extraction effort, task utility, evidence strength, learning and robustness. |
| `CC-C.2.8-8` Cold recovery | A publication-reading claim SHALL distinguish case facts from an explanation of the instruction supplied only by the test. |

### C.2.8:8 - Common Anti-Patterns and How to Avoid Them

| Observed or invited mistake | Repair |
| --- | --- |
| A fully articulated account is assumed equally recoverable by every reader | Retain its AE result and compare ESI for the selected reader preparation and budget. |
| The expert fixes false text, and the corrected relation is credited to that text | Preserve the initial answer and identify the correction supplied by expertise; repair the expression against its source. |
| Source-return links or a transfer test raise an amount score by their mere presence | Use source return as available support and transfer as its own tested result; compare the structure recovered under those conditions. |
| A missing denominator is scored as little structure | Return the missing comparison basis. Assign zero only when the declared scale and observation support it. |
| Fewer words, more boxes or a larger model are used as the structural measure | Identify the selected semantic structure and justify the representation or model correspondence. |
| A richer explanation is chosen despite a sufficient incumbent and no worthwhile gain | Compare the finite change's actual contribution and cost through C.11.CRC/C.11. |

### C.2.8:9 - Consequences

A shared characteristic lets an author compare forms without confusing them with the account's identity or the described architecture. It also lets a domain evaluation consume structural recovery while keeping its other results intact.

The practical cost is making material preparation, selection and access conditions explicit. That cost is small when the working situation already supplies them. Exact measurement or a causal claim about an explanation's effect requires more evidence because it answers a stronger question.

An additional example, prerequisite, diagram or changed order is useful when it exposes worthwhile structure under the actual conditions. Sometimes the current expression already supplies the needed structure. Both outcomes are compatible with this characteristic.

Reconsider the qualified result when the account, form, selected structure, observer preparation, available operations, help, carrier access, budget or correctness basis changes. Reuse an unchanged result for a matching use.

### C.2.8:10 - Architectural Rationale

The three-bearer definition explains why the same account can support different structural recoveries. The episteme distinguishes a content change, the form distinguishes expression, and the observer distinguishes who or what can extract the structure. Qualification conditions make comparison possible without inventing a new bearer for every resource limit.

Articulation explicitness, structural amount and task adequacy answer different questions. A plan can state its action condition completely while its reader lacks the prerequisite procedure. A diagram can expose additional relations while remaining insufficient for a design decision. Keeping these results separate preserves both the useful gain and the precise next question.

A common definition also allows unlike estimators without claiming universal commensurability. A path count and a justified coding estimate can address structural-information questions; their values are comparable only under an adequate scale and correspondence. The source studies therefore inform the aspect and its conditions while domain methods establish the particular result.

### C.2.8:11 - SoTA-Echoing

The computational line in Finzi et al. supplies a bounded-observer structural-information model. Adopt its observer dependence and separation of structural amount from downstream task relevance; adapt its formal use through the correspondence in :4.6. A computational estimate does not by itself establish human reading or learning effects. [Finzi et al., v2](https://arxiv.org/pdf/2601.03220v2)

MDL supplies the historical model-selection background: compare a model's description with the data description it permits. A small adequate model may explain rich structure, so minimizing total code length and comparing extractable structural amount must retain their different questions. [Grünwald's MDL account](https://homepages.cwi.nl/~pdg/book/book.html)

For human explanation, current preparation-sensitive research supplies a different constraint. The 2025 expertise-reversal meta-analysis supports treating assistance and prior knowledge jointly, with variation by population and domain. Adapt that result as a requirement to qualify a relevant reader comparison, not as an ESI scale. [Tetzlaff et al.](https://doi.org/10.1016/j.learninstruc.2025.102142)

The two 2025 biochemistry populations showed different near-transfer sequencing effects and no significant sequence effect on far transfer. The useful implication is to identify the knowledge and task conditions actually tested rather than infer a universal instructional sequence from a general expertise label. [He, Fiorella and Lemons](https://link.springer.com/article/10.1007/s10648-025-09993-3)

At comparable effort, ordinary source-based reconstruction often answers which needed relation became available. Use it for that question. Select a coding estimate, repeated reading or transfer observation only when its distinct possible results can change the claim or next action. Reopen a model correspondence or empirical generalization when new evidence contradicts the qualified use.

### C.2.8:12 - Relations

- **A.17/A.18 and C.16:** arity, characteristic/scale legality and the measurement chain for an actual measurement claim.
- **C.2.1 and E.24.PUB:** identity of the expressed episteme, publication form and presentation carrier.
- **C.2.4:** degree of explicit articulation and its receiving-use thresholds.
- **C.29:** mathematical-lens correspondence for a formal structural-information estimate.
- **C.33:** captured and missing structure, sufficiency and source return for an architecture use.
- **A.6.3.NAR and E.17.EFP:** narrative construction and explanation-faithfulness uses that consume structural recovery.
- **C.11.CRC/C.11 and C.37:** marginal comparison and choice, and selection of useful representations.
- **F.19 and A.19.ECS:** precise recoverable instruction, and construction of a domain evaluation that may use this characteristic.

### C.2.8:End
