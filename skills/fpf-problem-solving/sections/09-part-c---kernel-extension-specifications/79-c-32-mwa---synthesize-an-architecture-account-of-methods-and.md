## C.32.MWA - Synthesize an Architecture Account of Methods and Their Use

> **Tech-name:** `MethodArchitectureSynthesisFromSeveralStructures`
> **Plain-name:** connect methods with their performance, support and development in one usable architecture account
> **Type:** Method-description pattern under `C.32`
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### C.32.MWA:1 - Problem frame

Use this pattern when a decision about related methods and their use depends on several structures that do not line up one-for-one: how methods are composed, how work is performed, what supports it, and how methods are developed or retained. The question may involve different wholes and relations even when one source shows them in aligned rows.

The subject is one or several related Methods considered together with their performance, support and development. Identify the relevant Methods, performed or planned Work, participating or supporting Systems, descriptions and models, capabilities and providers, and cultural relations separately. Select only what can change the decision. The account can include relations beyond a Method's constituents: using a platform to perform a Method does not make that platform part of the Method. Each precise C.30 architecture claim still names its own holon and selected structure.

Here **method** is the main name for a reusable way of doing. **Practice** can name the same way, often emphasizing its established use, as E.10:0.2c.21a explains. A claim about performed Work, a community or a description requires those separately identified objects; the wording itself introduces no broader Practice whole.

The primary working reader is an architect, methodologist, practice designer, or domain-framework author who has already found useful source material but cannot safely copy its table, stack, lifecycle, or diagram as the architecture account.

**First useful move.** State whether the architecture question concerns arrangements already used in representative Work or a proposed organization of Method use. These are the obtaining and possible-future entries. Keep that status for each relied-on claim: an existing provider or development activity does not make the proposed use actual. Then write the architecture question in one sentence and select only the structures that can change its answer.

**What goes wrong if missed.** A source layout is mistaken for the arrangement it describes. A list becomes levels, a procedure becomes a hierarchy, overlapping activities become a sequence, a model becomes the thing modeled, or a future design acquires fictitious performed Work. A local repair may also look successful only because its unresolved burden moved to another structure or scope.

**What this buys in practice.** The reader gets a short, usable account of the selected Methods and their use, structures and relations, their correspondences, the main conflict or moved burden, and the alternative that changes the current decision. The account can remain ordinary prose; a table or symbolic form is optional assurance.

**Not this pattern when.**

- Use the direct Method, Work, subject, description, capability, provider, or cultural-change pattern when only one such claim is unclear.
- Use base `C.32` when the need is a palette of architecture candidates for one already grounded architecture question, rather than one coherent answer about Methods and their use from several non-isomorphic structures.
- Use `C.30.ILC` and `C.32.MLAO` when an already recovered cross-scope conflict or residual is the main subject.
- Do not use this pattern for one clear Method decomposition, one procedure order, a carrier index, a universal level stack, a mandatory record schema, domain filling, product-roster generation, or lifecycle design.
- A practitioner can use this Method to prepare evidence for a framework or project decision. Making that decision, establishing a product, publishing a description, or putting a proposed organization of Method use into effect remains separate work.

For the smaller question of what encompassing work is being done through one current action, start with **B.1.5.EW**. It can expose a missing constituent or a changed condition without requiring this full synthesis. Use **B.1.5.RS** when the difficulty is preserving encompassing uses while replacing one constituent. Return here when the answer depends on several structures that do not correspond one-for-one.

The result is an **architecture synthesis for Methods and their use**: a readable account connecting the selected Methods, Work and other identified objects through the relations relevant to one architecture question, with their consequences for the decision. The account describes how these objects fit together; whether any Methods form a composite Method remains a separate claim under B.1.5.

### C.32.MWA:2 - Problem

Professional-practice sources commonly mix several useful accounts. One may show Method order, another Work participation, another organizational or technical subjects, another capabilities and providers, another descriptions or models, and another cultural generation or retention. Their rows can look aligned while referring to different wholes and relations.

Three failures follow.

1. **Layout substitution.** The source's visible order or nesting is copied before the practitioner knows whether it means Method composition, Work order or overlap, subject composition, model grouping, provider dependency, cultural scale, or only chapter order.
2. **Present/future substitution.** A proposed organization of Method use is described as though a representative Work occurrence had already happened, so the architecture gains evidence it does not have.
3. **Local-success substitution.** A candidate resolves one visible conflict but hides the residual or burden it moves elsewhere. The account reports the gain and loses the trade-off.

A fourth failure appears only in some uses: a live product-boundary question is reduced to one favored publication arrangement, or a product comparison is forced into an architecture question that does not concern product identity. Both errors confuse a conditional comparison with a universal step.

### C.32.MWA:3 - Forces

| Force | Tension to hold |
| --- | --- |
| **One answer vs several structures** | The decision needs a coherent account, while the useful structures may remain non-isomorphic. |
| **Actual use vs prospective design** | Obtaining Work offers dated evidence; proposed Method use needs a truthful realization and later-test account instead. |
| **Precision vs readable entry** | Exact kinds and relations prevent false claims; notation-first prose can make the Method unusable to the practitioner who needs it. |
| **Candidate breadth vs proportional effort** | The first source layout is rarely enough; an unlimited candidate search can delay the decision without changing it. |
| **Local gain vs moved burden** | One structure can improve while another inherits cost, delay, evidence burden, loss of control, or unresolved residual. |
| **Project choice vs cultural change** | A project can deliberately choose or change an arrangement; distributed generation, transmission, selection, retention, and loss are different claims. |
| **Reusable Method vs domain filling** | The action sequence transfers across domains; actual domain Methods, institutions, evidence, constraints, and cases remain with the receiving domain. |

### C.32.MWA:4 - Solution

Build one readable synthesis from the relations supported by the current case. Keep the following eight actions in order as an attention aid, not as a claim that the activity being studied is one eight-stage process.

#### C.32.MWA:4.1 - Eight actions

1. **Choose a truthful entry.** For an obtaining organization of Method use, anchor one independently admitted representative performed Work occurrence and the useful result at stake; establish the other relied-on relations separately. For a possible-future organization, anchor an intended-use case, `WorkPlan`, or another correctly typed prospective account; state what would put that proposal into use and how later representative Work would test it. Keep actual development or support Work separate from the proposed use. Actual and prospective claims can coexist in the same account.
2. **Name the subject and participants.** State the subject under discussion (`EntityOfConcern`) and the actual kinds of the participants before classifying rows or positions. A source word such as *practice*, *layer*, *role*, *model*, or *provider* does not settle those kinds.
3. **Build alternatives for the question.** State whether the alternatives are competing architecture accounts of the same arrangement, proposed changes to that arrangement, or both. Competing accounts can reveal a relation that a sequence-only description misses; proposed changes alter how the Methods would be used or supported. Keep those comparisons distinct. Prepare alternatives that can change the decision or fail on different cases. When NQD is the current generation test, retain NQD-distinct candidates: their novelty is not a relabeling, their use-value preserves the declared constraints, and their diversity exposes different failure modes. Do not accept the source's first layout as the option set, and do not turn NQD into one scalar score.
4. **Recover each relation actually used.** In ordinary words first, state whether the source claim concerns Method composition or order, Work parthood or overlap, a subject relation, description or model use, a capability or provider dependency, cultural dynamics, or another admitted relation. Use the pattern that defines or constrains that relation when the claim matters to the answer. For structures of a Method and its uses, C.30.ASV:4.5a helps select the question before drawing its representation.
5. **Separate the described objects from their descriptions.** Keep identified Methods, Work, Systems and their relations distinct from the descriptions, models, views and coarse-grained accounts about them. A description can itself be used in Work; name that use separately from what it describes. State the correspondence and the distinctions each description preserves or loses.
6. **Reidentify a whole when needed.** Use `B.2` when the previously identified Method, Work, System, or Discipline whole cannot carry the current claim. Reidentify a selected structure under `A.22`'s four identity discriminators when the current claim requires a different selected structure. Do not keep the old identity merely to preserve a neat stack.
7. **Compare conflict and moved burden.** Expose conflicts between candidate structures. For every apparent local repair, ask what residual, constraint, cost, evidence burden, delay, or loss moved to another structure or scope. Compare the alternatives against the named architecture question, not against visual tidiness.
8. **Keep deliberate and distributed change distinct.** Separate a project's architecture choice or intervention from cultural generation, transmission, recognition, selection, rejection, retention, and loss. A project can influence those processes without controlling or proving them.

#### C.32.MWA:4.2 - Short working result

Write the first result as a short account that another practitioner can use without decoding a private ontology. This outline is a writing aid, not a mandatory schema:

```text
Current architecture question:
Entry: obtaining / possible-future organization of Method use; status of each relied-on claim
Representative occurrence or prospective anchor:
Useful result at stake:
Selected structures and the relations used:
Correspondences between described objects and descriptions, with losses:
Alternatives: competing accounts / proposed arrangements / both
Main conflict and any moved residual or burden:
Alternative that changes the current decision:
Source-return or later-test condition:
```

A compact table can support this account. Symbolic predicates are optional assurance and belong after the readable explanation. The result stops at architecture evidence; comparison, selection, decision, publication, evidence, assurance, or gate claims use their own patterns when those claims become current.

#### C.32.MWA:4.3 - Conditional product-boundary comparison

Only when product identity is the current architecture question, compare these four genuinely different arrangements:

1. one domain DPF;
2. independently maintained sibling DPFs;
3. direct use of FPF plus exact domain sources; and
4. a proposed common applied DPF.

For each arrangement, state the recurring practitioner problem, first useful result, independently useful boundary, sources and maintenance burden, and what another arrangement would leave hidden or duplicate. These four are comparison forms, not a selected product roster. When product identity is not the question, do not force this comparison into the Method.

#### C.32.MWA:4.4 - Stop, lower, and reopen

Stop when the short synthesis identifies the truthful entry, selected structures and relations, important correspondences and losses, at least one genuinely different alternative, the main conflict or moved burden, and the next use. Do not keep adding views that cannot change the decision.

Lower the claim when the subject, representative occurrence or prospective anchor, relation, evidence boundary, or alternative is not recoverable. Preserve the useful source cue and return to the direct pattern or source instead of completing the architecture by guesswork.

Reopen when representative Work contradicts the synthesis, a proposed organization of Method use is put into practice, a new structure changes the decision, a moved burden becomes material, a direct source changes, or the product-boundary question enters or leaves scope.

### C.32.MWA:5 - Archetypal Grounding

**Tell — methods and their social-dance use.** A five-minute social-dance occurrence sits inside a longer party. The architecture question connects dance methods, their performance, participant capabilities and the transmission of the style. Preparation has a real first-then order, while movement regulation, figure performance, partner coordination, style-specific performance and event participation can overlap in time. A teaching diagram is a description; bodily and pair capabilities concern participating Systems; scene transmission and later style selection are cultural relations. The synthesis keeps these structures linked but not identical. A sequence-only stack loses simultaneity, while one culture-level stack loses the actual Work and subject relations.

**Show — engineering Methods in performed Work.** In a 90-minute power-converter integration run, model correction overlaps simulation, rig reconfiguration precedes closed-loop test, assurance overlaps later testing, and restoration of a simulation service overlaps the run without becoming part of the converter-integration Work. Plant and controller models are descriptions used in the Work, not the converter or the Work. The team compares a sequence-only account with a linked account of Method, Work, subjects, models, platform service, capability, and evidence. The linked account wins for this question because it preserves both the rig-change–then–test unfolding and the overlapping activities. If evidence assembly is moved to the platform, the synthesis records platform availability and traceability as a moved burden rather than declaring an unqualified gain.

**Show again — possible-future use of a Method.** A five-day Method-adaptation sprint is obtaining Work. The candidate Method is described, but the proposed organization of its use has not yet been performed. The team anchors the architecture in the intended project use, the incumbent Method used during the sprint, the candidate MethodDescription, and a planned representative trial. It compares candidate organizations of Method parts, tool and description support, provider capability, trial Work, and later repertoire maintenance. It states which support and representative Work would put the proposed organization into use and what the trial must observe. It does not invent past Work enacting the candidate Method. If the question is only how the project will use the candidate, the four product arrangements are omitted; if the question becomes where an independently maintained Method family belongs, that conditional comparison is opened explicitly.

Across the three cases, the same Method preserves a truthful entry, several non-isomorphic structures, exact relation claims, separation of described objects from descriptions, whole reidentification, genuinely different alternatives, moved burdens, and the boundary between deliberate project change and distributed cultural change. The domain details remain different.

### C.32.MWA:6 - Bias-Annotation

**Scope:** Limited to synthesizing one usable architecture account of Methods and their use when several selected structures do not line up one-for-one. This is not a universal ontology, a required view set, a product-selection Method, or a complete architecting lifecycle.

| Lens | Likely drift | Repair |
| --- | --- | --- |
| **Gov** | The synthesis is treated as a decision, authorization, accepted product boundary, published result, or current practice. | State the next use and apply the separate decision, publication, acceptance, or currentness pattern only when that claim is current. |
| **Arch** | One source stack, lifecycle, matrix, or preferred view becomes the architecture. | Select only structures that change the question; recover their relations and correspondences; retain non-isomorphism. |
| **Onto-Epist** | A model, description, row, level label, or future design is treated as the described object or an obtaining relation. | Name the subject and participant kinds, distinguish obtaining from prospective, and state what each description preserves and loses. |
| **Prag** | The synthesis becomes a large mandatory dossier or a relation inventory no decision uses. | Start with the short result; add a view or formal check only when it changes the current decision or prevents a demonstrated overread. |
| **Did** | Formal notation and specialist ontology appear before the working situation and first useful result. | Use ordinary case language first, give nearby plain glosses for necessary FPF terms, and keep symbolic assurance optional. |

### C.32.MWA:7 - Conformance Checklist

| Check | Passing observation |
| --- | --- |
| **CC-MWA-1 — Recognizable use** | The opening names a current decision that needs one answer across several structures, plus an ordinary non-use boundary. |
| **CC-MWA-2 — Truthful entry** | The synthesis states whether it concerns an obtaining or possible-future organization of Method use. An obtaining claim has representative performed Work and the basis for each relied-on relation; a prospective claim has an intended-use or plan anchor, realization condition and later-test condition. Actual and proposed claims retain separate status in one account. |
| **CC-MWA-3 — Subject before layout** | The Methods under consideration and the Work, Systems or other objects needed to explain their performance, support and development are identified before source rows are interpreted. Practice may name the same reusable way as Method; neither that synonym nor the connected account introduces an encompassing Practice object. |
| **CC-MWA-4 — Candidate difference** | The synthesis distinguishes competing accounts of an arrangement from proposed changes to it. Alternatives differ by decision use or unlike-case failure, not merely labels or picture layout; a better account alone establishes no world-side change. When NQD is current, novelty, use-value and diversity remain distinct. |
| **CC-MWA-5 — Relation recovery** | Every relation used in the answer is stated by value and supported through its defining or constraining pattern when material. Order is not overlap; overlap is not parthood; co-use is not Method composition. |
| **CC-MWA-6 — Subject-description separation** | The identified Methods, Work, Systems and relations remain distinct from descriptions, models, views and coarse-graining. A description’s use in Work is separate from the objects it describes; important correspondences and losses are stated. |
| **CC-MWA-7 — Whole reidentification** | A Method, Work, System, or Discipline whole is reidentified when the old whole cannot carry the claim; a selected structure is reidentified under A.22 when the claim requires a different selected structure. |
| **CC-MWA-8 — Conflict and moved burden** | The main conflict is named and every claimed local improvement states any material residual or burden moved elsewhere. |
| **CC-MWA-9 — Conditional product branch** | The four product arrangements are compared when product identity is current and omitted when it is not; the comparison itself selects no product. |
| **CC-MWA-10 — Deliberate/distributed distinction** | Project choice and intervention remain distinct from cultural generation, transmission, recognition, selection, retention, and loss. |
| **CC-MWA-11 — Usable result** | A cold reader can recover the short synthesis, the decision-changing alternative, the next use, and the stop or reopen condition without reading symbolic assurance first. |
| **CC-MWA-12 — Unlike grounding** | At least two unlike cases test the Method, and a prospective case is used whenever the candidate claims it can synthesize an architecture account for proposed Method use. |

### C.32.MWA:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| **Copy the source stack** | Printed order can be chapter order, explanation order, Method order, Work order, subject grouping, or nothing architectural. | Name the subject and recover each relation before retaining a structure. |
| **Fictitious representative Work** | Proposed Method use acquires false evidence and false actuality. | Use an intended-use case, `WorkPlan`, or other prospective account; state realization and later-test conditions. |
| **One view set for every practice** | A convenient template becomes a universal ontology and imports irrelevant work. | Always keep the identity-and-relation check; add other structures only when they change the decision. |
| **Synonyms as alternatives** | Several names hide one unchanged organization and create false diversity. | State what decision, relation, or unlike-case result differs; merge candidates that differ only by labels. |
| **Local win, invisible burden** | The apparent improvement exports cost, delay, evidence, control, or residual to another structure. | Name the receiving scope and compare the moved burden with the claimed gain. |
| **Product comparison everywhere** | The Method becomes framework-product design even when the architecture of Methods and their use is the only question. | Open the four-option branch only when product identity is current. |
| **Product comparison nowhere** | A live field or maintenance boundary is hidden inside a favored architecture. | Compare the four arrangements and pass the result to the applicable product decision. |
| **Model equals its subject** | A view or matrix is treated as a world-side whole or relation. | State the described subject, model use, correspondence, and preserved and lost distinctions. |
| **Project choice equals cultural success** | A deliberate intervention is taken as proof of later recognition, spread, selection, or retention. | Keep the project claim and each cultural-change claim separate; use `C.36` for the latter. |
| **Notation as the first result** | The account becomes precise but unusable to the practitioner who must act on it. | Lead with the short prose synthesis; retain notation only where it catches a real ambiguity or supports a later check. |

### C.32.MWA:9 - Consequences

The Method preserves useful differences among Method, Work, subject, description, capability/provider, and cultural structures while producing one decision-ready account. It prevents source tables, lifecycle diagrams, and models from silently defining the objects and relations under discussion. It also makes prospective claims and moved burdens inspectable.

The cost is a small amount of relation recovery and alternative construction before a clean diagram can be accepted. Some attractive source organizations will remain unresolved or will be retained only as descriptions. That cost is proportional: the first result is short, structures that cannot change the decision are omitted, and formal assurance is optional.

Receiving domains still supply their own Methods, institutions, evidence, constraints, providers, cases, and maintenance conditions. Reuse of this Method does not move those fillings into FPF.

### C.32.MWA:10 - Rationale

The eight actions follow the dependencies of a truthful synthesis. The entry must distinguish obtaining from prospective before evidence is interpreted. Subjects and participant kinds must be known before a source layout is classified. Alternatives must exist before the first layout can be challenged. Relations and description correspondences then make the alternatives comparable. Whole reidentification prevents a neat name from carrying the wrong claim. Conflict and moved-burden comparison expose the real trade-off, and the final deliberate/distributed distinction prevents one project from being mistaken for cultural evolution.

The Method does not require all structures to fit one master diagram. Its common result is coherence through stated relations and correspondences, not visual isomorphism. This is why a short prose account can be the first useful result and why a matrix, graph, or formal model remains optional.

### C.32.MWA:11 - SoTA-Echoing

The sources below make complementary contributions; none is used as authority for the whole Method. The pattern composes only the bounded moves stated in the table, and the final row keeps current FPF distinctions authoritative.

| Source line | Contribution and limit | Decision and transfer into this pattern |
| --- | --- | --- |
| [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html), current architecture-description standard | Distinguishes the architecture of an entity from an architecture description and supports concerns, viewpoints, model kinds, and correspondences. It explicitly does not specify an architecting Method and is not a system or practice ontology. | **Adopt narrowly:** keep subject, architecture, description, view, and correspondence distinct. **Reject:** treating standard conformance or a view set as the practice architecture. Carried into actions 2, 4, and 5 and CC-MWA-3/5/6. |
| Grootenboer and Edwards-Groves, [*The Theory of Practice Architectures* (2024)](https://link.springer.com/book/10.1007/978-981-99-7350-7), and Olney and Wood, [learning-design practice study (2023)](https://doi.org/10.3389/feduc.2023.1291032) | Current practice-research line showing that professional practice is shaped across multiple sites and material-economic, cultural-discursive, and social-political arrangements. It gives a strong empirical antidote to procedure-only accounts, but its three media are one theory's selected structures rather than universal FPF kinds. | **Adopt:** multi-site, enabling/constraining, and empirical-practice attention. **Adapt:** recover the actual Method, Work, subject, description, capability/provider, and cultural relations needed by the case. **Reject:** importing the three media as a mandatory universal view set. Carried into Forces, Grounding, action 4, and the limited-scope bias. |
| Alter, [*Work System Theory* (2013)](https://aisel.aisnet.org/jais/vol14/iss2/1/), established work-system line | Provides a practitioner-readable way to examine participants, activities, information, technologies, products/services, customers, environment, infrastructure, and strategy together rather than reducing work to IT or a process chart. Its fixed framework is valuable for recognition but does not distinguish every FPF Method, Work, description, capability, and cultural relation. | **Adapt as recognition lineage:** start from useful Work and its result and look beyond one technical structure. **Reject:** treating the nine elements as a complete or mandatory practice ontology. Carried into Problem frame, actions 1–2, and obtaining cases. |
| Bartolomei et al., [Engineering Systems Multiple-Domain Matrix (2012)](https://doi.org/10.1002/sys.20193), with DSM/DMM lineage | Organizes source-side node classes in diagonal blocks and relation types within and between those classes in off-diagonal blocks; it supports tagging, storing, retrieving, and analyzing engineering-system information. It is engineering-modeling lineage, not current authority for practice ontology, and its source categories are not universal FPF kinds. | **Adopt as lineage:** make the source-side class and relation type visible when several structures are compared. **Adapt:** recover each exact receiving relation or correspondence, state what it preserves and loses, use ordinary prose first, and add a matrix only when it helps the decision. **Reject:** row alignment, matrix membership, or visual clustering as a world-side relation. Carried into actions 3–7 and the layout/model anti-patterns. |
| Current FPF `A.3.1`, `B.1.5`, `A.15.1`, `A.22`, `B.2`, `C.30`, `C.30.AD`, `C.30.ILC`, `C.32`, `C.32.MLAO`, and `C.36` | Supplies the maintained distinctions among Method, performed Work, selected-structure identity, whole reidentification, architecture, description, conflict, candidate synthesis, moved residual, and cultural change. | **Adopt and compose:** these patterns provide the exact tests used by the eight actions. C.32.MWA adds the obtaining/prospective discriminator, several-structure synthesis, conditional product comparison, and one readable result; it does not redefine the neighboring kinds or relations. |

Recheck these source uses when a newer applicable architecture-description standard, practice-architecture synthesis, work-system method, or multi-domain technique changes the practical move, or when unlike cases show that the eight actions no longer preserve a decision-relevant structure at proportional effort.

### C.32.MWA:12 - Relations

- **Builds on:** `A.3.1` for Method identity, `B.1.5` for Method order/composition and Work enactment distinctions, `A.15.1` and `F.6` for actual performed Work and attribution when claimed, `A.22` for selected-structure identity, `B.2` for whole reidentification, `C.30` and `C.30.AD` for architecture and architecture-description distinctions, and `C.36` for cultural-change relations.
- **Coordinates with:** base `C.32` for general architecture candidate synthesis; `C.17` and `C.18` only when NQD generation, novelty/diversity, archive, or front claims are current; `C.30.STRAT` before accepting level, layer, tier, stack, or similar source wording; and `C.30.ILC` plus `C.32.MLAO` when a conflict, residual, or moved burden needs its own treatment.
- **Provides a result to:** `E.4.PFAD` when several practice structures change a framework-architecture answer; `E.4.DPF` when those structures change DPF identity, scope, pattern organization, first use, or use of named results; `E.4.DPF.DA` when package adequacy needs the resulting two-way sequence-versus-simultaneity evidence; and `E.23.CDI` only when target-practice architecture must be recovered or compared before capability development.
- **Does not replace:** the direct domain sources and Methods, `E.4` product-family decisions, explicit comparison or selection, project architecture decision, `E.24.PUB` publication occurrence and availability, evidence or assurance, or the currentness and refresh patterns.

### C.32.MWA:13 - Footer marker

Use `C.32.MWA` to build one readable architecture synthesis for Methods and their use across several structures without turning a source layout, description, future design, local repair, or project choice into more than the current case supports.

### C.32.MWA:End
