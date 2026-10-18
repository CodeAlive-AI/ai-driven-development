## E.11.DSG - Architectural Reference

> **Type:** Specialization of E.11 (E)
> **Status:** Stable
> **Normativity:** Normative for an architectural reference and its public entries.

### E.11.DSG:1 - Problem frame

#### E.11.DSG:1.1 - Use this when

Use this pattern when writing an architectural account for the users of a named method language: how it is assembled, why its parts and connections are selected, what they make possible and how to use them. The account can explain one framework, a DPF Suite or FPF Library. Understanding its choices also lets a user question a premise or propose an improvement. Call it `<name of the explained whole> Architectural Reference`. It carries the public architecture, shared explanation and useful question-led entries, with returns to the full Methods and evidence. It is a support unit of the explained language unless independent use or change justifies a separate product boundary; this function does not by itself make the account another framework or the discipline being described.

**First useful result.** Give the reader a usable account of the whole's purpose, constituents, connections and limits, then a direct way into the needed explanation or Method. For a working question, give an answer or honest blocker. Distinguish an available result, a MethodDescription to use, direct-source evidence and a result still missing. Explain each necessary contribution and end that entry with an ordinary stop or return. Do not fill a missing result with another title.

**Primary EntityOfConcern.** One architectural-reference episteme: the public account of one named language assembly under C.2.1. Its content belongs to the explained whole and can be embedded in that whole's publication or separately carried. It can share the whole's publication and change boundary or have an independently useful product boundary under E.4:4.1. Separate files alone settle neither choice.

**What this buys.** The reader can understand the whole without its internal development records, select a useful route, recognize constituent and external contributions, and reach the full Methods, cases, limits and evidence needed to act or adapt the language.

**Not this pattern when.** Use E.4:4.2 and E.4.PFAD to decide which discipline a Suite describes and how its subdisciplines compose it. Use E.8 and the applicable Core or DPF authoring pattern to develop an unwritten Method, including a composite Method. Use a known pattern directly when its contribution is already clear; the architectural reference is not a prerequisite for that use. A separate curriculum or instructional Guide is a pedagogical companion. E.11.PFP governs framework publication form; it does not turn a supporting architectural reference into another framework. Describing FPF Library's connections does not claim a discipline above all its DPFs.

### E.11.DSG:2 - Problem

A list of titles does not explain the language's architecture or tell a practitioner which contributions answer a working question. A collection of short answers can omit the shared rationale, source synthesis and whole conditions needed for adaptation. Conversely, a long tutorial or metadata catalogue can hide the useful first answer, and an attractive summary can conceal a Method that has never been developed enough to reproduce.

These failures confuse different structures. A reader may treat all cited disciplines as constituents of the Suite, treat a MethodDescription as an already obtained result, or treat a cross-reference as proof of compatibility. A changed supplying Method can then leave the advice misleading even though every link still opens.

### E.11.DSG:3 - Forces

| Force | Pressure on the solution |
| --- | --- |
| Fast first use | A reader needs an answer before a catalogue of internal distinctions. |
| Exact return | A short entry must lead to the full contribution, its actual supplying framework and the conditions needed for use. |
| Public architectural account | Shared rationale, alternatives, sources and whole conditions must remain available without making the reader traverse them before every known pattern. |
| Different subjects | The composite discipline, its Suite description, constituent frameworks, external suppliers, Reference and publication or access arrangement are not interchangeable. |
| Honest combination | Several resources may be necessary, alternatives, or merely plausible; the Reference must state the actual relation or uncertainty. |
| Current action | Date, status, warning, availability, and source return matter only when they change what the reader should do. |
| Low record burden | Ordinary lookup may remain conversation; addressable answers are justified only by later review, reuse, publication, or reliance. |
| Language reach | Translation and language-specific maintenance may change the episteme or the product boundary. |

### E.11.DSG:4 - Solution

Develop the account of the named whole under section 4.1, preserving the explanations needed to understand and adapt it. For a problem-led entry, write the practical answer first. State the recognizable situation and question, then say what each returned item actually is and what it contributes: an available result of its own kind and supplying product, a MethodDescription used to select or perform its Method, direct-source evidence for a named claim or decision, or a named unavailable result with its blocker and retry. State maintenance only when it changes the answer. End the entry with the ordinary stop or return. Add identity, relation, evidence, warning, or reliance detail only when it changes the answer's truth, the reader's choice, or a named later use.

When an account cites a basis or directs readers to another contribution, use E.8:4.2.2.2 to make the purpose clear in ordinary prose. Preserve the difference among an explanation already given, an available result, material to apply, and a contribution still unavailable. This distinction does not make every relation between frameworks an application instruction or require a label beside every address.

#### E.11.DSG:4.1 - Identify the explained whole and the account's boundary

Start from the language assembly selected under E.4 and E.4.PFAD. Identify what the whole enables and which constituents and connections it contains. For a Suite, recover its composite discipline under C.20, constituent DPFs, whole-forming connections and outside suppliers. For FPF Library, recover the relations among Core, Suites and standalone frameworks without inferring disciplinary parthood from their use or co-publication. A useful outside contribution remains outside unless its separate part relation is established.

Identify the architectural-reference episteme under C.2.1 by its claims, subject and effective ReferenceScheme. Its claims include the whole's purpose and architecture, intended readers and questions, answers and gaps, and sources and conditions needed to use them. Its scheme resolves the named whole, constituent and external frameworks, Methods, results and relation words. A title or a folder supplies a locator, not those distinctions.

Keep the architectural reference as a support unit of the explained whole when their readers, content change and publication boundary agree. Give it a separate product boundary only when readers need to use, cite or revise the account independently. If continuity across independently managed editions matters, E.4:4.2.5 supplies the product-series distinction. This publishing choice does not make the account a subdiscipline or a constituent DPF.

Establish publication, availability, currentness and maintenance only to the extent claimed. An author, locator or recent date does not establish a maintaining System or a commitment to future updates. A stale Reference can cease to supply a reliable route while the Suite and its constituent Methods remain directly usable.

##### E.11.DSG:4.1.1 - Explain the architecture and its reasons at this level

Explain the working problems served by the whole, the contributions of its constituents and the connections that make their use coherent. State the shared assumptions, combination conditions and limitations that are not recoverable from one constituent alone. Include the alternatives and tradeoffs that help a reader choose or adapt the arrangement, the source synthesis and SoTA grounds behind it, and representative cases in which a whole condition changes the next action. Use the substantive questions in E.11.PFP:4.7 for a framework account; at another assembly level retain the questions that its promised use actually needs. A short entry and exact constituent returns can spare a familiar reader repetition, but a locator does not supply an unwritten shared explanation.

Choose the receiver from the named whole the account explains, then choose its carrier. In a one-file framework, embed that framework's architectural reference as a named unit. In a multi-file language, provide the account at that language's assembly level and make the constituent accounts reachable. For example, an Engineering Suite Architectural Reference explains the Suite's composition; the FPF Library Architectural Reference explains its relations to other Suites and standalone DPFs. Neither source-file boundaries nor generated website pages create additional explained wholes. Use the full qualified title at the unit's entrance and an unambiguous shorter mention within it; a generic heading `Reference` alone does not identify the subject.

Keep the account's **referential index** recoverable: who speaks, to whom, about which language, and for which reader action. In an Architectural Reference, its author explains the named language to its users. They need to understand how the arrangement works, what it enables, how to use its contributions and why it was chosen. Resolve wording such as 'we', 'you', 'here' and 'this framework' from that position. Identify the reading purpose, not a person's profession: a framework developer selecting a Method is a user in that passage; when the explained framework itself teaches framework development, its developers are its practitioner users.

Distinguish that explanation from instructions for constructing or revising a pattern language. This pattern and the applicable E.9, architecture and authoring patterns address that development work. A Reference can explain a constraint on valid use of its language; state whom it constrains, under which conditions and from which governing pattern it follows. A sentence about what the authors selected does not by itself impose an obligation on users or future authors.

Publish the architectural decisions realized by this language and the reasons needed to understand and use them. The architectural reference can be their public statement, not merely a summary of a private record. Keep chronology, superseded decisions, review correspondence and release logs in the corresponding project's documentation. E.9 develops and records a substantive decision; a decision record is not historical by its kind. The public account retains the operative choice and its useful grounds. An explanation of an already described Method can remain in its pattern or the architectural reference of the whole it explains. A separate course or Guide serves a learning purpose; it is not a substitute for the language's own explanation.

##### E.11.DSG:4.1.2 - Make current decisions understandable and revisable

Organize the account around the architectural questions that matter to users of this language. A reader may need to understand a boundary before choosing a Method. The same explanation can let that reader challenge the boundary and propose a change; it need not teach the work of developing the next framework edition. Give such a decision a recognizable title and section address. Connect related decisions: a choice of field boundary can determine which Methods are constituents, which are suppliers and what a whole-level Method still has to obtain. A list of isolated decisions cannot replace the account of that whole.

For a decision needed to understand, combine or revise the language, make these answers recoverable:

1. **Question and conditions.** What difficulty or requirement does the choice address, and which competing forces shape it?
2. **Selected arrangement.** What is constituted or separated, which relations hold, and where are they realized in the language? Distinguish the selected architecture from a proposed alternative or an illustrative case.
3. **Grounds and alternatives.** Why is this arrangement useful under those conditions? Compare the serious alternatives that could change the choice, with their sources and limits. An unexplained preference or reference to an inaccessible DRR supplies no rationale.
4. **Consequences and revision.** What can readers obtain with this arrangement, what does it cost or leave unresolved, and which Methods or connections depend on it? Explain what changed condition would justify reconsideration and what related claims would then need examination.

These are substantive questions, not four mandatory subheadings or a demand for one ADR file per decision. Use connected prose, a comparison table, a diagram or a developed case as the question requires. Section titles should name the architectural issue or choice; E.11.PFP:4.7 supplies the framework-wide content functions, and section 4.2.1 supplies the addresses. Keep a shared premise once and return to it from the decisions that use it. The reader should not have to assemble the whole from repeated miniature forms.

A decision can define the architecture of this published language without imposing a universal rule on all disciplines or frameworks. State any normative requirement with its actual scope and return to its governing pattern. Conversely, an explanatory form does not make the language's declared composition an optional opinion. Claims about the discipline still need their C.20 grounds; publishing a decision does not create those subject-side relations.

Architectural patterns can contribute to this account or organize its explanation when they belong to the explained language and supply a result its users need. Develop a missing reusable construction as a complete E.8 pattern in Core, the relevant DPF or the Suite according to its subject. An architectural-reference publication may carry that pattern if its full body, identity, reader use, entry and authoritative source remain explicit under E.11.PFP. Otherwise return to its existing full body. Distinguish a domain architectural Method used by the language's practitioners from a Method for developing the language itself. Reusability alone does not place the latter in a user-facing account. Sharing a carrier does not turn ordinary explanatory sections into normative authoring Methods. A record explaining why this language selects one architecture is not automatically a new pattern; E.9 and the applicable architecture and authoring patterns supply the development Methods.

First test the account for its user's work. From the account and its reachable suppliers, can the reader recognize when the language is useful, select and connect its contributions, and explain why a relevant architectural condition changes that use? If the reader can only repeat the arrangement or guess why it was chosen, develop the missing explanation.

An informed change proposal supplies an additional test of that understanding. A user who questions the arrangement should be able to identify the decision, the challenged premise, a meaningful alternative, its expected gain and the connections it could affect. This requires neither private authoring history nor a mandatory issue form. It does not replace the account's user-facing purpose with a Method for changing the framework.

#### E.11.DSG:4.2 - Make the public minimum immediately useful

Make the account noticeable from the ordinary entrance to the explained language. A reader who does not know that an architectural explanation exists must be able to recognize its purpose before searching for its title. In a README or equivalent entrance, offer a prominent, ordinary-language question such as “How is this language organized and why?”, link directly to the account, and state what it explains. Place that choice where readers first choose how to enter, alongside the route to a known Method. A link buried among filenames or offered only as an extra worked example does not communicate that purpose.

Test this entrance from the reader's starting situation, without supplying the Reference's name or destination as the answer. Can the reader notice that the explanation exists, tell what question it answers, and choose it when the arrangement is unclear? Can someone with a familiar sufficient Method still proceed directly? Successful filename search or link resolution answers a different question.


Make these facts recoverable before the reader chooses an entry. An embedded architectural reference can use the containing publication's edition, date, status and ToC wherever they already identify this unit and its content; do not repeat that front matter or constitute a separate edition solely for the account. A separately carried unit exposes the necessary facts at its own entrance:

- the qualified architectural-reference title and exact edition locator;
- fixed edition date, intended readers, and practical use;
- actionable status or an honest non-current, superseded, or retired warning, together with its as-of basis;
- a direct entry to the account of the explained whole, with constituent and external contributions distinguished; and
- a table of contents that locates the architectural account, useful question-led entries and their supplying explanations without implying a mandatory order.

The edition date says when this edition was constituted. It is not a changing currentness claim or the date of every publication occurrence. Show the author when attribution, trust, contact, reliance, or source return changes what the reader should do. A byline does not identify the Reference maintainer, suite maintainer, publisher, or authority.

Every problem-led entry keeps this small visible core:

```text
recognizable situation and practical question
first useful answer or honest blocker
available result, MethodDescription, direct-source evidence, or named unavailable result needed now, and what each contributes
ordinary stop or return
```

Add a DPF product series' or edition's state, field promise, detailed locator, applicability, evidence, availability, dependency, compatibility, warning, author, or claim-local reopen condition only when it changes the choice, truth, stop, return, or named reliance. Put a genuinely shared boundary once at Reference or section level. Do not repeat empty fields or turn ordinary architectural decisions into pattern-index entries. Use section addresses for the account. If the publication also carries declared E.8 patterns, retain their distinct entries and full bodies under E.11.PFP.

Frame each entry around a real working question and the decision or action the reader needs next. Let the answer branch, overlap, or offer several honest stops when the situation does; do not force a false linear procedure. Keep the action-changing answer in the entry and return to detailed sources and explanations already provided in the account or its constituents instead of repeating them. At Reference level, state whose information need is served, how the publication is presented and made available, how readers return to its sources, and where later review or retirement is decided. Future revision or continued availability requires a separate commitment.

##### E.11.DSG:4.2.1 - Give each answer a stable address and a recoverable extent

Use the architectural-reference unit's declared key and give each substantive heading a stable section address, for example `Engineering.Reference:2` and `Engineering.Reference:2.1`. These are `SectionRef` values for the unit, not PatternIDs or a framework identity. Keep one qualified unit title, a contents entry for every substantive heading, and a final `<ReferenceKey>:End` boundary. In an embedded account, use the containing publication's ToC rather than add another one. A structural Contents heading needs no section address. Use nested contents entries to make the answer hierarchy visible and every substantive heading reachable.

Make the heading levels express the actual containment of the answers. In a Markdown carrier, a complete addressed section includes its own text and child sections up to the next heading of the same or a higher level, or the document's end boundary. The numbers and heading hierarchy must agree; a number alone does not change the returned extent. Place examples and variations under the explanation whose answer they develop. An independently retrieved example returns to any parent or related explanation needed to interpret it.

Keep an established SectionRef when only the heading title changes. When moving a section beneath another parent requires a different hierarchical path, assign its current SectionRef and record the correspondence in the publication or access maintenance material. Update maintained links to the current section. Preserve former returns in each access route that claims that continuity; do not reuse a former address for another answer or place a migration history in practitioner prose. A new answer receives an unused address. Preserve returns to saved heading fragments using facilities permitted by the selected publication form. For Markdown, follow E.8:4.1.1 and update maintained links to the corresponding native heading. Resolution of a carrier fragment does not establish that another access route can resolve the former SectionRef. If a route cannot preserve a return, identify the replacement and the affected reliance before claiming continuity. Check the full contents and complete returned sections, including their children, in each selected presentation or access route. Successful title search establishes findability for that query; stable identity and complete extraction need their own evidence.

#### E.11.DSG:4.3 - Keep lookup Work and the answer separate

A person, team, or assisting System may use one Reference edition while doing lookup Work. Ordinary use alone does not establish a Method, assignment, operation application, evidence, or authority. Identify those objects only when the current claim actually needs their direct rules.

An ordinary answer may remain readable conversation. Persist one only when review, reuse, publication, or later reliance needs an addressable result. First identify the exact practical-question episteme `Q`. Then identify the answer episteme `A` under `C.2.1` as `<claim content = J_a, EntityOfConcern = Q, effective ReferenceScheme = R_a>`. `J_a` states the answer, exact Reference edition used, every returned resource or blocker, and what each does in this answer. `R_a` resolves those values and the use-specific relation words. This is an ordinary episteme, not a new lookup-result kind.

Say directly what each returned item does. For an available result, name the result's actual kind, supplying product and edition or current state, receiving use, and any currentness or availability condition that can change that use. State maintenance only when it changes the answer. For a MethodDescription, name the described Method and how the reader uses the description; do not present its expected result as already obtained. For direct-source evidence, name the supported claim or decision and the source limits. For an unavailable result, name the blocker and retry condition. Recommendation, alternative, dependency, compatibility, and co-listing remain separate claims and create none of these stronger relations.

#### E.11.DSG:4.4 - Test sufficiency and each item's necessity

Call an answer a **sufficient combination with every returned item necessary** only when the Reference entry gives a recoverable candidate boundary, required result, and sufficiency rule, the combination satisfies that rule, and removing any returned item makes the result insufficient. The boundary is the resources actually inspected through the entry and its direct source returns, not every publication that might exist. This item-necessity test does not establish the smallest combination. A “smallest” claim also needs a declared size criterion and a comparison or argument showing that no smaller in-scope combination is sufficient.

When that test cannot be completed, return a bounded plausible combination and name the uncertainty or missing item. Do not disguise a convenient shortlist as a `JointUseSet`. Use `G.5` only when every named returned resource is required for one named use and the current inclusion basis supports that all-items-needed claim.

#### E.11.DSG:4.5 - Return to the full Methods and refresh the affected answers

The architectural reference supplies the current account of the explained whole, with exact returns to inherited explanations. For a Suite it distinguishes constituent DPFs from the external frameworks that a question happens to use. It also identifies the supplying edition, Method or result whenever that difference can change the answer. A reproducible comparison may pin an assembly and constituent-edition selection; ordinary current use needs a reliable current return, not a history of editorial decisions.

When a supplying DPF changes, compare the contribution consumed by the answer. Refresh the answer if the Method, conditions, result, evidence, applicability or availability changed materially. A new layout need not change the answer; a stable URL does not prove stable content. Use E.4.PFIP for preservation across reconstructed publications and E.4.PFR for a genuine edition dependency or compatibility claim.

When a DPF moves or a former pattern is divided, return to the full current Methods that supply the required results. Preserve a distinct result only where its explanation still exists. A list of successor titles, an empty redirect pattern or an old locator cannot stand in for lost content. Update maintained links and test their destinations and complete returned sections in the selected publication form.

If the field boundary or constituent relation changes, return that architecture question to E.4:4.2 and E.4.PFAD. Do not keep a false membership statement because an older Reference printed it. A Reference can show the newly supported arrangement without claiming that a publication edit itself transformed the discipline.

When an answer loses a required contribution, name the missing result and its consequence. Offer a direct known DPF route when sufficient, a bounded qualified alternative when supported, or an honest stop. An unavailable Reference does not prohibit direct DPF use. An unavailable constituent publication does limit the Suite's claimed usable coverage; neither fact erases the discipline.

#### E.11.DSG:4.6 - Distinguish expression, derivative, edition, and product

Another layout, carrier, rendering, or faithful expression of the same exact claims under the same scheme presents the same Reference episteme. A translation or other derivative that changes claims or effective scheme is a distinct episteme with an exact source-to-use path under `C.2.P`; when meanings cross schemes, test the `F.9` Bridge and bounded use separately. Title or provenance alone establishes no `EpistemeEditionRelation`.

A language-specific derivative stays within the same Reference product only while it uses the same intended readers and use, access rule, warning rule, later-review rule, and retirement rule. A separately established maintenance relation changes product identity only when the identity rule says so. If a language community needs a different current state or any of those rules, select another Reference product. A comparison across Suites can belong to the FPF Library Architectural Reference. Give it an independent product identity only when its use and change boundary justify that choice under E.4:4.1.

### E.11.DSG:5 - Archetypal Grounding

#### E.11.DSG:5.1 - Organization change and continuing operation

A manager asks how to reorganize a service without losing control of daily operation. A useful Reference answer can be three sentences: name the organization-change result for the organizational change; name the operations result for continuing operation; stop when those two contributions answer the question, or return the missing result. Co-use establishes no dependency between the DPFs.

If the decision is safety-critical or legally constrained, add the exact source date, jurisdiction or applicability, authority boundary, warning, and reopen condition because those values change the answer and action. The simple and expanded answers use the same distinctions; they carry different justified detail.

#### E.11.DSG:5.2 - External suppliers and a translated Reference

A Reference may combine results from narrative, language-practice and pedagogical DPFs for one lesson-planning question. It labels each as a constituent or an external supplier according to the actual field architecture; their co-use alone creates no Suite. Include all three only if removing any one makes that result insufficient under the stated rule. Otherwise present alternatives or a bounded plausible combination.

A Spanish translation of an English Reference is a derivative episteme when its effective scheme changes. It remains in the same Reference product only while it uses the same reader and use, access rule, warning rule, later-review rule, and retirement rule. A separately established maintenance relation changes product identity only when the identity rule says so. A different Spanish use or current state may select another Reference product even when its title and cited DPFs remain recognizable.

#### E.11.DSG:5.3 - Returns after content or publication changes

| Situation | Reader-facing result |
| --- | --- |
| One DPF contribution is known and sufficient. | Use that DPF directly; no Reference detour is required. |
| A question needs both a constituent engineering Method and external financial analysis. | Explain the two contributions and their connection without including Finance in Engineering. |
| A known constituent Method is usable before the Suite's architectural reference is available. | Use the Suite's framework entrance or that constituent directly when sufficient. A missing shared account limits combined or adaptive uses that depend on its explanation; do not claim that account is available. |
| A supplying Method changes its applicability condition. | Reconsider and repair the affected answer even when the file and title are unchanged. |
| A Method moves into Core or is divided between DPFs. | Return to the current full explanations and verify that each needed contribution survived. Remove obsolete maintained links. |
| A publication is unavailable. | State the resulting use limit; do not infer that the discipline or Method ceased to exist. |
| A former constituent relation proves unsupported. | Correct the field description and Reference; retain a justified external use if one remains. |
| A Reference cannot return to the full explanation or evidence. | Treat its advice as unqualified for that reliance, repair the return or name the missing result. |
| One presentation exposes several framework and support publications. | Keep their identities and contributions distinct; the common presentation does not merge their fields. |
| The Library does not supply a necessary Method. | Name the missing construction and return to a Core or DPF development question, or to a direct source with explicit limits. |

#### E.11.DSG:5.4 - Understanding an arrangement before questioning it

A Library user needs to work without a network and considers proposing that each DPF include its own editable copy of all general Methods. The Library Architectural Reference explains two relevant decisions: general constructions have one full Core source because their conditions apply across subjects; a usable publication must also make its required texts obtainable. Their consequence is not a requirement for network access. A self-contained distribution of identified editions can answer the access problem without creating separately maintained versions of the same Method. A change to the general Method is a different proposal and must consider its other users. The account lets the user choose a sufficient offline arrangement and distinguish it from a proposal to change a general Method. It does not teach how to maintain the Library.

A user of a single-file semantic-integration framework wants repeatable queries and considers proposing a materialized graph for every integration. Its architectural reference explains the selected freedom of realization: a live provider can forbid copying, while another use may require repeatable local queries. SIE.8 carries the full Method for selecting a realization under those conditions. The Reference explains why the language retains that choice and how it relates to identity, interfaces and validation. An issue claiming that every integration must copy the sources can therefore be tested against a stated condition; an issue showing a new arrangement that meets both access and repeatability requirements can improve the Method. Reprinting SIE.8 in the Reference would add no missing architectural explanation.

In both cases the author first explains an arrangement that the user needs to apply. Understanding its reasons also makes a meaningful challenge possible. That additional result does not change the account into instructions to future framework developers. A project log or a table of current filenames supplies neither the practical explanation nor its reasons.

### E.11.DSG:6 - Bias-Annotation

- **Catalogue bias.** A longer list of included DPF product series looks more complete. Judge the entry by whether it returns the right contributions or blocker for the current question.
- **Combination bias.** Co-use looks like dependency or compatibility. State those relations only after their exact edition-level predicates pass.
- **Freshness-display bias.** A current-looking page or recent date looks maintained. Require the direct maintenance, source-return, status, and currentness facts.
- **Precision-display bias.** Repeated fields and formal identities look safer. Keep the ordinary answer first and add only detail that changes truth or action.

### E.11.DSG:7 - Conformance Checklist

| ID | Passing condition |
| --- | --- |
| `CC-DSG.1` Useful entrance | From the ordinary entrance, a cold reader who was not given the Reference title can notice that an architectural explanation exists, identify the explained whole and its purpose, and choose that route. A familiar sufficient Method remains directly usable. Each problem-led entry exposes the working situation, practical question, useful answer or blocker, exact contributions, and stop or return before internal apparatus. |
| `CC-DSG.2` Whole and source return | The architectural reference identifies its subject and edition, supplies the whole's architecture and returns to the full supplying Methods or evidence. For a Suite, constituent frameworks and external suppliers remain distinct. Edition detail appears when the receiving use needs it. |
| `CC-DSG.3` Different subjects and boundaries | Discipline, Suite edition, constituent DPFs, external frameworks, supporting Reference, available results, MethodDescriptions, lookup Work, answer, publication and access remain distinct. The Reference's product boundary follows its actual use and change needs. |
| `CC-DSG.4` Progressive detail | Date and actionable status are visible; author, evidence, relation, product-series state, warning, and reopen detail appears only when it changes reader action, truth, or named reliance. |
| `CC-DSG.5` Answer discipline | Each returned item is classified and stated separately as an available result of its actual kind and supplying product, a `MethodDescription` reference, direct-source evidence, or a named unavailable result. Its readable contribution or blocker is explicit; maintenance appears only when it changes use, and recommendation, alternative, dependency, compatibility, and co-listing create none of those relations. |
| `CC-DSG.6` Sufficiency and necessity tested | The combination satisfies the declared sufficiency rule and removing any returned item makes the required result insufficient within the stated candidate boundary. A “smallest” claim additionally states a size criterion and establishes that no smaller in-scope combination is sufficient; otherwise retain the narrower necessity claim or call the answer bounded and plausible. |
| `CC-DSG.7` Change and return honesty | A changed supplying contribution reopens the affected answer. Moves and splits return to complete current explanations without losing required Methods or importing public migration history. Unsupported composition claims are corrected. Unavailability limits the claimed route or coverage without erasing the discipline or forbidding a sufficient direct DPF use. |
| `CC-DSG.8` Derivative boundary | Expression, translation or other derivative, an established edition-continuity relation, language-specific product, and carrier are distinguished by their actual identity, source, scheme, reader-use, and maintenance facts. |
| `CC-DSG.9` Plain-language whole passage | The complete changed passage can be read by an engineer or manager without reconstructing ontology notation; exact triples and relation terms appear only where they change identification or a stronger claim. |
| `CC-DSG.10` Current problem-led entry fit | Each problem-led entry starts from a real working question, supports necessary branches or honest stops, links out distracting detail, and reflects the intended readers' information need, presentation, availability, and any separately established maintenance fact that changes use. The entry form records what was adopted, adapted, and rejected from current task-guide practice and when to recheck it. |
| `CC-DSG.11` Addressable complete answers | Every substantive heading has a unit-local stable section address and is reachable through the contents. Heading levels and addresses agree with the actual answer containment. Complete returns include the selected section and its children; necessary surrounding explanation remains reachable. Earlier saved returns still resolve or have a declared replacement. |
| `CC-DSG.12` Public architecture retained | The account's author, intended user, explained language and reader action are recoverable. The account explains operative decisions, connections, shared conditions, alternatives and source grounds so that users can understand its usefulness and apply its contributions without internal development records. An informed challenge is an additional use of that understanding, not a shift to normative framework-development instructions. Required content does not impose one section template. An included or returned architectural pattern serves the language's users and retains its full E.8 body and explicit owner. The account belongs to a real language-assembly level and preserves direct pattern entry. Embedded or separate carriage does not by itself create a product series or disciplinary membership. |

### E.11.DSG:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Why it fails | Repair |
| --- | --- | --- |
| Unnoticed architectural account | The file and its links work, but the entrance never tells readers that the language’s arrangement is explained or why that explanation matters. | Offer the architectural question and its direct answer at the point of choosing a reading route; test recognition from that entrance, not only retrieval by a supplied title. |
| DPF list as Reference answer | Titles do not say whether an entry returns an available result, a MethodDescription, source evidence, or a missing result, nor what it contributes. | State the question, classify each return, name its direct contribution or blocker, and stop or return. |
| Reference hides an unwritten Method | A short answer or application supplies a Solution without a recognizable problem, construction, conditions and cases. | Develop the Method under E.8 in its proper Core, DPF or Suite-level pattern; retain the architectural explanation and a direct return to that Method in the architectural reference. |
| Reference performs lookup | Publication content is mistaken for dated Work or an operation application. | When a direct claim needs lookup Work, use A.13 to identify its actual performer and A.15.1 to admit the dated occurrence independently. If the claim must also identify the assignment under which the lookup was performed, check that relation separately through F.6. Keep the Method and any A.6.1 application bindings separate. |
| Disciplinary composition from navigation | Co-listing makes outside suppliers appear to be subdisciplines, or an open link is treated as proof that its answer remains usable. | Return to the C.20-grounded Suite architecture for composition and to the supplying contribution for applicability and currentness. |
| Mandatory answer record | Every conversation produces a lookup-result object. | Keep ordinary answers in prose; persist only for named review, reuse, publication, or reliance. |
| “Smallest” from item necessity | Removing any one item can defeat this combination while another, smaller combination still works. | State the supported sufficiency and item-necessity claim. Claim “smallest” only with a size criterion and a comparison or argument excluding smaller sufficient combinations; otherwise say “bounded plausible combination.” |
| Translation as edition | Shared title or provenance hides changed claims or scheme. | Identify the derivative episteme and source-to-use path; test edition continuity independently. |
| Byline as maintenance or authority | Author attribution is made to carry responsibility, currentness, or authority. | Show attribution when useful and establish maintenance, publication, authority, and currentness separately. |

### E.11.DSG:9 - Consequences

**Benefits.** Readers can understand and adapt the language from its public architectural account or start with a short answer and reach the complete Methods and evidence. They can distinguish a Suite constituent from an outside supplier, a description from an available result, and a useful combination from a gap. A changed field architecture need not destroy valid cross-framework uses.

**Costs.** Someone must keep the answers connected to the contributions on which they rely whenever continued maintenance is promised. Consequential answers may need more source or applicability detail. Developing an unwritten Method costs more than adding a link, but the link alone would leave the practitioner to invent that Method.

### E.11.DSG:10 - Rationale

An architectural reference explains the structure and reasons of a method language. For a Suite, the discipline described and the account of its framework remain different subjects; for FPF Library, connections among languages need not be disciplinary part relations. This is why the account can explain outside contributions without absorbing their fields and why repairing or retiring the account does not reidentify a discipline.

Progressive detail keeps ordinary use short without shortening the full explanation needed for adaptation. A trustworthy entry exposes its useful contribution and returns to the developed Method rather than making navigation compensate for missing content.

### E.11.DSG:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and E.11.DSG mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should a reader with one cross-DPF question receive a truthful first answer without being forced through instruction or lookup machinery? | The best-known line currently available for this bounded FPF question combines `E.11`/`E.11.PUA` situation-first entry with the four independently governed returns from `E.8:4.1.3`, `A.3.2`, `A.10`, `A.15.1`, `A.15.PROD`, and `C.2.1`: an available result, a MethodDescription, direct-source evidence, or a named unavailable result. | Instructional how-to guidance is the serious popular default. Diátaxis [*How-to guides*](https://diataxis.fr/how-to-guides/) is retained only as that comparator: it begins from a real-world goal, permits forks, and keeps action central, but its instructional form assumes a task and procedure rather than a cross-product answer publication. | The default can turn the Reference into a tutorial, a forced sequence, or the reader's Work and can hide honest gaps. **Adapt:** the opening, `E.11.DSG:4.2–4.5`, cases, `CC-DSG.5`, and anti-patterns make the first answer short, progressive, source-returning, and explicit about gaps; **reject** a universal documentation taxonomy, mandatory detour, and co-listing as Suite or dependency evidence. | The FPF patterns supply the selected internal best-known line for this product boundary; the linked Diátaxis page is a popular-practice comparator, not SoTA-bearing evidence; cross-domain cases are transfer and counterexample evidence, not authority. No external source validates the architectural-reference form as a whole. | Reopen if a serious current alternative gives a more truthful or lower-effort cross-product answer, if cold-reader evidence still classifies the Reference as instruction or lookup Work, or if the direct FPF return kinds and source/currentness boundaries change. |
| How much common explanation belongs to the public language rather than only to its development records? | E.11.PFP:4.7 already requires the substantive E.8 functions, shared rationale, source synthesis, alternatives and cases needed to understand and adapt a framework. E.4 applies the account at each actual language-assembly level. | A title index plus short question-led answers gives direct entry but can leave the architecture and shared use conditions outside the publication. | Preserve the complete public account in section 4.1.1 and use short entries as entrances into it; return full constituent explanations without requiring every reader to traverse the whole. | These FPF rules supply the internal content and architecture basis for this publication form. The decision does not claim an empirical advantage or a general taxonomy of all documentation. | Reopen when readers still need private development records to recover the architecture, when the account hides a missing Method, or when a different public arrangement preserves the same explanations with less unnecessary reading. |
| How can users understand an operative architectural decision well enough to apply or question it? | E.9's decision kernel and E.11.PFP's whole account supply the substantive construction; current [arc42 guidance on architecture decisions](https://docs.arc42.org/section-9/) supports stating choices, criteria and rationale in a form fitted to their use. | A mandatory ADR per decision supplies a repeatable form; unconstrained prose avoids repetitive fields but can hide the choice and its consequences. [Nygard's 2011 account](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) is the historical source for a compact decision record with pattern-like balancing of forces. | Sections 4.1.1–4.1.2 preserve the author-to-user explanation, require recoverable questions, selected arrangement, grounds and consequences, and allow connected prose. Section 5.4 first tests practical understanding, then an informed challenge. A needed reusable architectural Method retains its complete pattern. | These are design and practice grounds, not evidence that one template is empirically best for FPF. Nygard addresses a future developer; that addressee is not transferred unchanged to the user-facing account. Arc42 permits several forms and discourages duplicated rationale; it does not settle the Reference's reader or subject. | Reopen when users cannot recover an arrangement's practical consequence or reasons, when a challenge requires private authoring knowledge, or when a different form preserves the same explanation at lower total effort. |

The composite discipline, Suite edition, constituent DPFs, external suppliers, Reference, answer, lookup Work, publication and availability remain governed by their direct FPF patterns. Compare their contributions to the actual reader question; identity evidence, source evidence and use evidence support different claims.

### E.11.DSG:12 - Relations

- **Specializes:** `E.11` for the architectural reference of a named language assembly and its useful question-led entries; it does not specialize `E.11.PFP`.
- **Uses:** `E.4:4.1` for the architectural-reference function and product boundary; `E.11.PFP:4.7` for a framework account; `E.4:4.2` and `E.4.PFAD` for the Suite's composite-discipline and framework architecture; `C.20` for disciplinary composition; `E.9` for developing and recording the explained decisions; `C.2.1` for Reference and DPF editions; and `G.5` only for an actual `JointUseSet`.
- **Coordinates with:** `E.4.PFR` for exact edition dependency and compatibility; `C.2.P` and `F.9` for derivatives and cross-scheme use; `E.17`, `E.24.PUB`, and `G.11` for source return, publication, availability, and currentness; `E.11.PUA` and `E.11.PUR` for actual selected-pattern use and pattern-use coordination.
- **Constrains:** public architectural accounts of frameworks, Suites and FPF Library, their question-led entries and source returns, truthful treatment of external suppliers and gaps, and repairs after changes to Methods, language or field architecture, or publication.

### E.11.DSG:End
