## E.10.ROLE - Recovering What “Role” Means in the Current Claim

> **Type:** Lexical and ontological precision restoration (E)
>
> **Status:** Stable
>
> **Plain name:** Recover what “role” means here

### E.10.ROLE:0 - Use This When

Use this pattern when claim-bearing wording uses *role* and the current sentence does not yet reveal which object or relation it means.

> A **system role** is a context-local kind for an entity already admitted under A.1 as a `U.System`, which may be a person, team, organization, or non-human technical object. The name creates no admission, assignment, agency, capability, or Work.

A **system-role assignment** is one exact occurrence under `U.SystemRoleAssignment`. The bare word *role* identifies neither object.

**First useful result.** Rewrite the ordinary domain sentence so that its recognizable object and action or relation are explicit. Select the pattern for that object or relation. Stop there unless the receiving claim needs a technical designation, exact occurrence, predicate, assertion, or reference.

For example:

- “Alice is reviewer” may remain ordinary recognition prose;
- “Alice holds the review assignment for this manuscript” makes an assignment claim current;
- “the report plays a role in approval” normally needs an evidence-use, source-use, reliance, or other direct relation, not a system-role assignment;
- “the first role in this tuple” normally points to a representation position, not a system-role kind.

**Not this pattern when.** Keep ordinary or quoted wording unchanged when no FPF claim relies on the word. When the object and its direct pattern are already clear, use that pattern directly. Use `A.6.RSIR` when the unresolved question is specifically about participation in a direct relation, a relation declaration, an interface, or a representation position.

`ROLE` remains in this PatternID because it is the ambiguous source word that opens this recovery. It is not a Tech designation for one governed object and is not a naming precedent.

### E.10.ROLE:1 - Problem Frame

Readers meet *role* in organizational, engineering, mathematical, software, documentary, and ordinary language. The same spelling may point to a local classification of systems, one assignment occurrence, participation in a relation, a declaration slot, a position in a representation or organization, functioning, capability, Work, authority, responsibility, use of an episteme, or no technical claim at all.

One remote definition cannot make the word safe in every sentence. Replacing every occurrence with `SystemRole` is also wrong: it would turn unrelated participation, slot, representation, evidence, and ordinary-language claims into a new ontology.

### E.10.ROLE:2 - Problem

A cold reader needs to answer two questions at the point of use:

1. What exact object or relation does this sentence claim?
2. What useful action or conclusion depends on making that distinction?

If the text answers neither question, a fluent rewrite can preserve the word while changing the claim. A mechanical replacement can be even worse: it can assign a report, schema field, relation participant, or diagram position to a system-role kind that was never intended.

### E.10.ROLE:3 - Forces

| Force | Tension |
|---|---|
| Natural wording vs technical identity | Practitioners need short sentences, while a later claim may need one exact kind, assignment, relation, or declaration. |
| Familiar word vs many neighboring objects | The word aids recognition but cannot select one ontology by itself. |
| Direct routing vs duplicate ontology | The entry must find the right pattern without copying that pattern's rules. |
| Precise distinction vs modifier stacking | Add `system`, `kind`, `assignment`, or another qualifier only when it distinguishes a live alternative. |
| One check vs procedural burden | Recover the claim once; do not create a form or ledger for a clean local repair. |

### E.10.ROLE:4 - Solution

Use the sentence's intended claim, not the trigger word, to select the result.

1. Quote or locate the bounded phrase only when its source identity matters.
2. Write the ordinary sentence the reader should understand, naming the recognizable object and action or relation.
3. Select one branch below from that recovered claim. The examples are non-exhaustive; they illustrate result families and do not define a new role taxonomy.
4. Apply the selected pattern only as far as the receiving claim needs. Add a Tech designation, occurrence identity, predicate, assertion, reference, evidence, or assurance only when omitting it would change truth, action, reuse, or reliance.
5. For one recovered claim, stop when one exact object or relation and its pattern are selected, or return the exact `missing-governor`, missing-information, quote-only, or ordinary-non-use result.

If recovery shows that the same bounded phrase carries several distinct claims at once, rewrite them as separate ordinary sentences and apply steps 3–5 to each sentence. Ambiguity by itself is not evidence of several claims. Use A.6.C **Contract Unpacking for Boundaries** only when its contract-like boundary-language trigger holds; otherwise apply the direct rule for each recovered claim. Do not create a multi-claim record or an umbrella role object.

| Current claim recovered from the wording | Required result and next action |
|---|---|
| One exact local work-facing system-role kind, or a technical claim that one admitted system counts under it | For kind recovery, use C.3 and A.2 to identify one exact context-local system-role kind; a durable local designation normally ends in `...SystemRole`, for example `ReviewerSystemRole`. For a current classification judgment, use A.2 and C.3.2 and keep the admitted candidate system, exact kind, current `KindSignature` edition, context slice, and `true | false | unknown` result recoverable. Kind admission is not the classification judgment. |
| One obtaining assignment of an admitted system to that kind | Recover one occurrence of an exact direct species under `U.SystemRoleAssignment` through A.2.1. Assignment creates neither system admission, another classification, capability, participation, responsibility, nor Work. |
| “The system as reviewer” or similar readable designation | Keep the readable actor designation when it carries the needed ordinary claim. Recover exact system identity, a separately obtaining classification, or an assignment only when the receiving claim uses that distinction. Create no `SystemInRole` individual. |
| Participant meaning or actual participant of a direct relation | Use `A.6.RSIR` and the pattern for that direct relation. State the participant meaning and actual participant without calling either a system role. |
| One place in a declaration, for example a source-named field, argument, result, endpoint, slot, or port | Use `A.6.RSIR`, followed by A.6.5, A.6.1, or the exact interface pattern. Recover `SlotKind`, `SlotSpec`, an argument or result declaration, or the interface term rather than `SystemRole`. |
| One position in a representation, for example a tuple component, formula argument, graph endpoint, diagram place, schema field, or call position | Use the pattern for the selected representation and C.29 correspondence. The position is neither participant meaning nor system-role kind. |
| Another object or relation, for example participation, functioning, capability, Method, Work, obligation, permission, access, authority, responsibility, position, result, or status | Use the direct pattern and relation for that claim. If exact participants are known but no current direct relation closes the use, return the exact `missing-governor` result through A.6.RCD. |
| A use of an episteme, for example when a report, standard, dataset, description, model, or publication “plays a role” | Recover the exact evidence-use, source-use, description-use, publication-use, reliance, status-use, or other direct relation. The episteme does not become a system-role holder. |
| Ordinary or quoted wording carrying no FPF claim | Retain it as ordinary or source wording. Create no Tech token, kind, assignment, or repair record. |

#### E.10.ROLE:4.1 - Boundary with A.6.RSIR

`E.10.ROLE` starts from the ambiguous word and recovers the sentence's work-facing or use-facing object. Use `A.6.RSIR` for the narrower question of direct-relation participation, reusable declaration, interface, operation declaration or binding, and representation position.

If the recovered claim leaves a direct-participation, reusable-declaration, interface, operation-declaration-or-binding, or representation-position question unanswered, apply `A.6.RSIR` to that question. If it recovers a system-role kind, assignment, capability, Work, deontic relation, evidence use, another direct object, or ordinary non-use, apply that object's direct rule and do not apply RSIR. Neither pattern duplicates the other's subject rules.

#### E.10.ROLE:4.2 - Lightweight Result

For a local repair, the result is normally only:

```text
source sentence: the report played a role in approval
recovered sentence: reviewers used Report-R as evidence for ApprovalClaim-C
applicable rule: A.10 evidence-use relation
blocked overread: Report-R has no system-role assignment by this claim
stop: ApprovalClaim-C remains the current question
```

No separate repair record is required unless another named use must inspect or reuse the decision.

### E.10.ROLE:5 - Archetypal Grounding — Worked Slices

#### E.10.ROLE:5.1 - Alice Is Reviewer

“Alice is reviewer” may stay as readable recognition prose when no technical classification claim is consumed. If only the local kind matters, identify `ReviewerSystemRole` through C.3 and A.2. If a technical classification judgment matters, use A.2 and C.3.2 and keep Alice, `ReviewerSystemRole`, the current `KindSignature` edition, the context slice, and the `true | false | unknown` result recoverable. If assignment identity matters, first name the declared assignment species `JournalReviewAssignmentRelation` and establish that its direct predicate obtains for the actual participants, including Alice as holder, under the stated applicability. Only then identify `ReviewAssignment-82` as the occurrence and state its extent. A roster, appointment label, description, or evidence item may support the assignment claim but does not make the assignment obtain. If performed Work matters, first recover Alice's A.13 core for this action and independently admit `ReviewWork-82` under A.15.1. Because this branch also says that Alice performed the Work under `ReviewAssignment-82`, F.6 afterward relates the already admitted Work to that same assignment. Classification, assignment, Work, and attribution remain separate. None follows merely from the ordinary sentence. A short projection may omit an assignment identifier unused by its receiving claim only when every relation the claim consumes remains recoverable.

#### E.10.ROLE:5.2 - A Report Plays a Role in Approval

The report is an episteme. Rewrite the claim as “reviewers used Report-R as evidence for ApprovalClaim-C”, then use A.10 for the evidence-use relation and B.3 only when an assurance claim or material-reliance threshold is current. The report becomes neither a system nor a holder of a system-role assignment.

#### E.10.ROLE:5.3 - API Provider Role

“The API role is provider” does not yet reveal which claim is meant. It may hide several claims, but the wording alone does not establish that; recover the intended claim before selecting and applying a rule. First ask whether a provider System is current and whether its classification under a local provider system-role kind matters. If the assignment itself matters, name its declared assignment species and the obtaining occurrence separately; do not infer either from root-family typing or the word *role*. Provision, service, declaration, interface, schema position, publication, promise, and access claims each use their own pattern. Only when provider Work is current, recover every precise performer's A.13 core and independently admit the dated Work under A.15.1. Add F.6 afterward only if this provider account also needs precise assignment-bound attribution through the same obtaining assignment. The API description is neither assigned nor a performer.

#### E.10.ROLE:5.4 - Passive Test Article

A passive test article may independently pass A.1 and be classified under `TestArticleSystemRole`. If an assignment claim matters, name its declared assignment species before identifying an occurrence. Neither classification nor assignment makes the article an agent or performer. The role-bearing source claim to recover is: `TestArticle-7 participates passively in TestWork-9 during TestInterval-9`; its intended participant order is article, Work, then applicability interval. No current pattern supplies a direct passive-participation predicate with those participants, applicability, and occurrence identity, so the current result is the A.6.RCD `missing-governor` for that exact attempted claim. Any tester or test-rig Work first reuses every precise performer's A.13 core and is independently admitted under A.15.1; add F.6 only when the tester account also needs precise assignment-bound attribution. A short projection may omit an unused assignment identifier, but it keeps the article, Work, interval, and missing relation recoverable.

### E.10.ROLE:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for claim-bearing uses of *role* that enter this pattern; ordinary and quoted non-uses remain outside it. The pattern deliberately favors Onto/Epist precision, which can tempt an author to expand every sentence into technical apparatus. Writing the ordinary sentence first, adding only distinctions used by the receiving claim, and stopping when the applicable direct rule is clear preserve Prag and Did usefulness, while the separate branches preserve Gov and Arch boundaries.

### E.10.ROLE:7 - Conformance Checklist

1. Is *role* being used in a claim, rather than only in ordinary or quoted wording?
2. Does the repaired ordinary sentence name the recognizable object and action or relation?
3. Was the result selected from the recovered claim rather than from the word alone?
4. If a system-role kind is current, are its local boundary and stable contribution distinction recoverable through C.3 and A.2? If a technical classification claim is current, are the candidate’s independent A.1 system admission, exact kind, current `KindSignature` edition, context slice, and `true | false | unknown` C.3.2 judgment separately recoverable?
5. If an assignment is current, can you identify both the assignment occurrence and its declared species? Does that species' direct predicate obtain for the actual participants, including the holder, under the stated applicability, and is the occurrence's extent recoverable? Is supporting evidence kept separate from whether the assignment obtains?
6. Are participation, declaration slot, operation binding, interface place, and representation position kept distinct?
7. Are functioning, capability, Work, deontics, access, authority, responsibility, evidence use, and results kept under their direct relations?
8. Does ordinary prose stay ordinary when no technical distinction changes the receiving claim?
9. Does the repair add a qualifier only for a live alternative and avoid a fixed formal expansion?
10. For each recovered claim, does the repair stop after one exact object or relation and its applicable rule are selected?

### E.10.ROLE:8 - Common Anti-Patterns and How to Avoid Them — Role-Word Repairs

| Anti-pattern | Repair |
|---|---|
| Replace every *role* with `SystemRole` | Recover the current claim first; use `SystemRole` morphology only for an exact local system-role kind. |
| Replace every *role* with *position* | Distinguish system classification, assignment, relation participation, declaration place, representation position, and ordinary wording. |
| Send every case through A.6.RSIR | Use RSIR only for direct-relation, declaration, interface, operation, or representation recovery. |
| Treat an episteme's use as a work assignment | Recover its evidence-use, source-use, publication-use, reliance, status-use, or other direct relation. |
| Expand a short sentence into a full ontology bundle | Add only the distinction consumed by the receiving claim, then stop. |
| Create a durable list of all possible senses | Keep the branch table as recovery examples; admit objects and relations only through their direct patterns. |

### E.10.ROLE:9 - Consequences — Reopen Condition

**Benefits.** Cold readers can recover the intended object at the point of use. Natural practitioner language survives. Technical names become more precise without turning relation slots, evidence uses, or representation positions into system-role kinds.

**Costs.** A claim-bearing ambiguous sentence needs one bounded interpretation before it can be reused. Some old compact Tech names must be retired or made explicitly historical.

Reopen this pattern only when an actual bare-*role* use cannot reach one exact object, relation, ordinary non-use, or missing governor without duplicating `A.6.RSIR`, or when repeated cold readers still infer system admission, assignment, agency, capability, participation, or Work from `SystemRole` morphology.

### E.10.ROLE:10 - Rationale

The recurring problem is word-sense recovery, not a missing universal role category. FPF therefore makes an internal architectural choice: recover the claim expressed in this use, then use the direct pattern for the recovered kind, assignment, participant, declaration place, representation position, or relation. The trigger word neither supplies that ontology nor makes the recovered claim obtain.

The pattern therefore stays thin. It supplies an entry and a stop rule, while C.3, A.2, A.2.1, A.6.RSIR, A.6.5, C.29, A.10, A.15, and other direct patterns retain their own predicates and identity laws.

### E.10.ROLE:11 - SoTA-Echoing

No external source governs this design, and FPF imports neither an external upper ontology nor its terminology. Two current lines provide the main SoTA comparison. The [gUFO account](https://arxiv.org/abs/2603.20948) and [OntoUML role documentation](https://ontouml.readthedocs.io/en/latest/classes/sortals/role/index.html) and [specification](https://ontology.com.br/ontouml/spec/) test anti-rigidity, external dependence, and the connection to a base kind. [Engineering-function work](https://doi.org/10.3233/SW-223188) tests the separation among function, behavior, and capability. FPF uses both lines as bounded comparators and adapts their tests to keep holder identity, changing classification, assignment, capability, functioning, and Work distinct.

Other comparisons have narrower uses. FPF adapts [Toyoshima's role facets](https://doi.org/10.3233/AO-210244) as diagnostic questions about position, specification, and potential. It uses [DOLCE](https://doi.org/10.3233/AO-210259), [BFO](https://www.iso.org/standard/74572.html), and [CCO](https://arxiv.org/abs/2404.17758) as bounded comparators for dependence and the distinctions among persistent entities, processes, roles, dispositions, capabilities, and functions. It keeps [DnS](https://doi.org/10.1007/978-3-540-39964-3_44) as lineage for separating descriptions from entities participating in described settings. These comparisons supply distinctions and counterexamples, not FPF kinds or assignment identity.

Within FPF, E.10 and E.10.ARCH define trigger recognition and recovery distribution. A.2, C.3, and C.3.2 define system-role kinds and classification judgments; A.2.1 defines assignment occurrences; A.6.RSIR defines direct-relation, declaration, interface, and representation recovery; and F.19 constrains the final plain wording. Together they define the ordinary-sentence-first, thin entry, but cannot supply a missing direct relation or establish that the recovered claim is true. Reopen this choice if one of those patterns changes that boundary, or if a stronger current comparison exposes a case in which the thin entry cannot preserve both plain language and whether the recovered relation obtains.

### E.10.ROLE:12 - Relations

| Pattern | Use |
|---|---|
| `E.10` | Detect bare *role* as a trigger with no default Tech reading. |
| `E.10.ARCH` | Place this bounded entry in the wording-use restoration architecture. |
| `A.2`, `C.3`, `C.3.1`, and `C.3.2` | Recover exact local system-role kinds; judge candidate membership through C.3.2 under an exact signature edition and slice; recover subkind order and continuity. |
| `A.2.1`, `A.2.5`, `A.2.7`, and `F.6` | Recover assignments, assignment state, relations among system-role kinds, and performed-Work attribution. |
| `A.6.RSIR`, `A.6.5`, `A.6.1`, and `C.29` | Recover direct-relation participation, declaration places, operation declarations and bindings, interfaces, and representation positions. |
| `A.10`, `B.3`, `F.10`, and `E.17` | Recover evidence, assurance, status, source, and publication uses of epistemes. |
| `F.18` and `F.19` | Check durable names and the final plain precise sentence after the object is recovered. |

### E.10.ROLE:End

