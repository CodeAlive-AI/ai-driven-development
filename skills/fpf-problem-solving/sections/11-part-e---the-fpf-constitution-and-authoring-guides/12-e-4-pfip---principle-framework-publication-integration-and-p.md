## E.4.PFIP - Principle-Framework Publication Integration and Preservation

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### E.4.PFIP:1 - Problem frame

Use this pattern during assembly of accepted changes into a candidate FPF, DPF, or LPF publication when the maintainer must answer either of these questions:

1. Did the candidate incorporate every accepted source contribution with its intended meaning and use?
2. Did the candidate preserve the useful content and selected structure of the predecessor publication outside accepted changes?

Use it especially when a publication form is replaced, split, merged, added, retired, or assigned another bounded use. A clean build, matching source files, or a readable candidate cannot answer the second question.

The primary reader is a framework maintainer or integrator preparing one candidate publication. The primary `EntityOfConcern` is one candidate FPF, DPF, or LPF edition being assembled for one declared publication use. The method returns a preservation conclusion about that edition. Files and build results are construction means or evidence.

**Begin here.** Name the candidate framework edition and publication use, identify every accepted source contribution for this candidate, and list the predecessor and candidate publication-form expressions whose continuity or change is claimed. Then select the source-to-candidate comparison and the applicable predecessor-preservation branch.

The first result is a preservation conclusion for the declared use. It names losses, repairs, accepted content changes or retirements, unexpected additions, blockers, and unresolved correspondences or content decisions. Keep the complete comparison checkable. Ordinary retained content needs no positive prose row.

A maintainer can incorporate an accepted change while preserving unrelated predecessor content and assess a changed form while distinguishing the form, carrier, edition, and content.

**Related work.** Use `E.8` to author one pattern, `E.24.PUB` to identify publication, expression, and bearing relations, `E.17` to select reader-facing forms, `E.11` to design the public entry, `E.4.DPF.DA` to evaluate a DPF or LPF package, and `E.2.DA` to evaluate whole-FPF adequacy.

A responsible maintainer uses the local construction and release methods for repository operations and decisions to accept, admit, release, or land a publication.

A new publication with no predecessor needs the accepted-source comparison, the complete candidate inventory, checks of changed public entries and direct consumers, and the applicable package evaluation.

### E.4.PFIP:2 - Problem

Framework integration has two independent failure modes.

An accepted source contribution may never reach the candidate, or it may reach the wrong public entry or consumer. A candidate may also contain every accepted addition while losing useful predecessor content unnoticed, without any accepted decision to change it. The source-to-candidate comparison can detect the first failure and cannot answer the second.

Publication plurality makes the second failure harder to see:

- one framework edition can be exposed through a sequential monolith, extracted pattern texts, reader-entry and Architectural Reference forms, cards, diagrams, or retrieval forms;
- two forms can serve the same broad use without being versions of one another;
- a text diff can expose changed sentences but not a lost diagram relation, card field, retrieval cue, or admitted operation;
- splitting or merging forms can make a predecessor form disappear even though its content still needs a disposition; and
- a carrier can remain byte-identical while its selected edition, bounded use, or expression relation changes.

The recurring mistake is to use a proxy such as source parity, build success, carrier continuity, heading coverage, or textual similarity as proof that the complete predecessor publication survived.

### E.4.PFIP:3 - Forces

| Force | Tension |
| --- | --- |
| Accepted change vs predecessor continuity | Realize the new decisions in the candidate without treating all other predecessor content as disposable. |
| Complete traversal vs affordable use | Every item of predecessor content or selected structure required for the declared use needs an outcome, but ordinary retained content should not create a large positive ledger. |
| Several forms vs truthful comparison | The same edition may have several forms, yet shared use or shared carriers do not make those forms one eligible comparison pair. |
| Text convenience vs structural meaning | Line and span diffs are cheap for comparable text; diagrams, cards, and retrieval forms need their own content or selected-structure inventories. |
| Form evolution vs content disposition | A form can be retired, split, or merged without authorizing the retirement of what it expressed. |
| Reuse vs local specificity | FPF, DPF, and LPF publications share the integration problem, while an applicable FPF pattern still defines or constrains what matters for each form and use. |
| Strong assurance vs bounded result | The comparison can expose loss and support later reliance. Later admission, publication, release, or assurance decisions use their own methods. |

### E.4.PFIP:4 - Solution

For a candidate framework publication with a predecessor, run two independent comparisons:

- **accepted source to candidate:** whether each accepted source contribution was incorporated into the named part of a candidate publication-form expression without changing its accepted meaning or use; and
- **predecessor to candidate:** whether the candidate preserves the complete predecessor publication outside accepted content changes.

The predecessor-to-candidate question has two branches.

Use a one-to-one expression comparison for an eligible predecessor/candidate pair.

Use an allocation comparison for a non-one-to-one publication-form change, including every split or merge even when a narrower one-to-one pair also survives.

These comparisons and predecessor branches are operations of the method. They introduce no FPF kinds. When a later use needs the conclusion as a reusable episteme, identify it under `C.2.1` and state the later reliance separately.

A publication-form expression here is one independently identified expression under E.24.PUB that follows the selected reusable form. Fix its domain and equality rule before comparing it.

The form-mediated relation can remain true while its expression witness changes, so a preservation comparison identifies the predecessor and candidate expressions rather than relying on that relation alone.

#### E.4.PFIP:4.1 - Bound the candidate and accepted inputs

Identify:

- the candidate FPF, DPF, or LPF edition and declared publication use;
- every accepted source contribution included in this candidate edition;
- every candidate `PublicationExpressionRelation` occurrence, its selected edition, independently identified expression and bounded-use declaration, and any selected form and its `PublicationFormConformanceRelation`. Retain a current `PublicationFormExpressionRelation` claim with its expression witness;
- the corresponding carriers and publication occurrences only when their identities affect the comparison; and
- every predecessor expression whose continuity, replacement, retirement, split, merge, or use change is claimed.

Complete the accepted input set before assembly.

If one source contribution changes a public entry, required input, result, field meaning, action order, stop, return, or another consumed interface, either include the affected public entries and direct consumers in this candidate or leave that contribution out until they can be updated with it.

Before assigning a receiving passage, recover the content architecture that makes that receiver appropriate. Method placement and architectural-account placement answer different questions.

Place a Method by its subject, generality and required contributions under E.4 and E.4.PFAD. Place an architectural account by the named whole it explains under E.11.DSG:4.1. An account connecting Core and domain languages can belong to a Library account even when the general Method it explains belongs in Core.

Retiring a separate carrier supplies neither placement decision. If the receiver is not justified, return that architecture question before treating a content match as an accepted allocation.

For each accepted source contribution, record the candidate publication-form expression and the passage, field, relation, cue, or selected structure intended to incorporate it.

A source contribution with no corresponding predecessor content is an accepted addition. Changing or retiring predecessor content needs an accepted content decision; changing or retiring a publication form is not such a decision.

Use `E.24.PUB` to keep the framework edition, individually identified expression, reusable publication form, expression and conformance relations, carrier, bearing relation, audience, bounded use, and publication occurrence distinct. Use the smallest explicit statement that supports the comparison.

#### E.4.PFIP:4.2 - Compare accepted sources with candidate expressions

After assembly, inspect every accepted source contribution in the named part of its candidate publication-form expression.

For each contribution, ask whether the candidate preserves the selected claim, action, result, boundary, relation, structure, or other content that made the contribution acceptable. Classification by filename, heading, or copied wording is insufficient when the receiving use changed.

Classify each accepted source contribution with one of these outcomes:

- incorporated as accepted;
- incorporated with an accepted content change;
- missing or only partly incorporated;
- placed where the intended reader or consumer cannot use it; or
- blocked because the accepted source contribution or intended candidate expression part cannot be recovered.

You can retain an ordinary positive outcome in the checkable comparison without writing a prose row. This comparison establishes source carry-through only. Unrelated predecessor content needs its own comparison.

#### E.4.PFIP:4.3 - Compare one eligible expression pair

One preservation comparison follows one eligible pair: one predecessor `PublicationExpressionRelation` occurrence and one candidate occurrence, with both expression identities fixed.

Where form-mediated continuity is claimed, retain the corresponding `PublicationFormExpressionRelation` occurrences and identify the expression witnesses being compared.

A pair is eligible only when both expressions have the same declared bounded use and either:

- retain publication-form identity under the FPF pattern that defines or constrains that form; or
- are identified by an accepted one-to-one replacement or continuity decision.

The same broad use alone does not pair two forms when several forms serve that use.

Before concluding preservation, select one complete, form-appropriate comparison inventory. The inventory names every predecessor claim, instruction, boundary, field, relation, cue, or selected structure required for the declared use.

Beside each entry, record why it matters—the FPF pattern that defines or constrains the form, or another accepted comparison basis—and any candidate correspondence.

The inventory aids comparison. It does not make the named kinds members of one new kind.

For comparable text expressions, deletion and replacement spans expose independently actionable predecessor claims, instructions, and boundaries. These spans are one comparison technique. Completeness depends on coverage of what the declared use requires.

For a card, diagram, retrieval form, or another expression without shared span coordinates, inventory the claims or selected structures required for the declared use. Use the FPF pattern that defines or constrains that form and, when applicable, `C.33` to state captured and lost structure or `C.34` to state a bounded structural correspondence.

Traverse the entire predecessor inventory. For each named item of content or selected structure, record one outcome:

- matched by content or selected structure in one or more named candidate expression parts;
- intentionally changed or retired by an accepted content decision;
- accidentally lost; or
- blocked because the correspondence or decision cannot be established.

Classify candidate content or selected structure without a predecessor correspondence as an accepted or unexpected addition.

If no applicable FPF pattern or accepted comparison basis makes a complete inventory selectable for the declared use, stop at `missing form-comparison basis`. Carrier identity, visual similarity, or a successful build cannot complete the comparison.

#### E.4.PFIP:4.4 - Allocate a non-one-to-one form change

An accepted publication-form addition, retirement, split, merge, or use-change decision names the affected predecessor and candidate expression occurrences and any narrower one-to-one continuity that survives. It authorizes the form change. Predecessor content needs its own disposition.

Run a separate allocation comparison for every accepted form change that leaves an affected predecessor expression outside an eligible one-to-one pair, and for every split or merge even when narrower pairs survive.

1. Select a complete inventory for every predecessor expression named by the form-change decision.
2. For each named item of predecessor content or selected structure, use the receiving subject and publication function established in section 4.1, then record one or more corresponding candidate expression parts, an accepted content-change or content-retirement decision, an accidental-loss result, or a blocker. A complete textual match establishes correspondence. The receiver needs the architectural grounds from section 4.1.
3. Allow predecessor content to appear in several candidate expressions and several predecessor inventory entries to correspond to one candidate expression part.
4. Inspect the complete inventories of the named candidate expressions and classify candidate content or selected structure without a predecessor allocation as accepted or unexpected additions.
5. Reuse an eligible-pair result as correspondence evidence when applicable, but do not let it replace the allocation traversal.

Keep every named expression, carrier, edition, and publication occurrence separate throughout the allocation. Use the allocation comparison to reason across these objects. It requires no collective publication kind.

Without the form-change decision, stop at `missing publication-expression continuity decision`.

Without a complete selectable predecessor inventory, stop at `missing form-comparison basis`.

Without an outcome for any named item of predecessor content or selected structure, return accidental loss or a blocker. Retiring a form never retires its content by implication.

#### E.4.PFIP:4.5 - Complete the affected-publication comparison and return

Identify every affected occurrence of the exact expression relation and its selected reusable form where applicable. Include any form-mediated relation whose continuity is claimed. If carrier or publication identity affects the comparison, include its bearing and publication relations.

Run every applicable eligible-pair and allocation comparison. Check each shared public entry or direct consumer once across these comparisons and keep the separate expression results that depend on it.

Return a bounded preservation conclusion with:

- accidental losses and the expression parts that need repair;
- accepted content changes or retirements that account for a predecessor difference;
- unexpected additions;
- unresolved candidate correspondences or content-change questions;
- blockers and the comparisons they prevent; and
- the declared use for which the conclusion holds.

The complete traversal remains checkable. Unchanged predecessor content and selected structure receive no prose rows. A build result, successful accepted-source comparison, pattern-quality result, or package-adequacy result cannot substitute for that traversal.

When the framework publication has no predecessor, perform the accepted-source comparison, inspect the complete candidate inventory, check changed public entries and direct consumers, and use the applicable package evaluation.

When an unchanged edition is republished through a different form or carrier, use `E.24.PUB`, `E.17`, `C.33`, and `C.34` for the changed publication claims.

Use this pattern only when accepted-source integration or complete framework-publication continuity is the live problem.

### E.4.PFIP:5 - Archetypal Grounding

**One-to-one text revision.** A DPF maintainer adds an accepted pattern and updates one existing pattern. The source-to-candidate comparison confirms both changes. A text comparison with the predecessor monolith then finds an unrelated non-use boundary deleted during paragraph cleanup. That boundary has no accepted retirement decision, so the preservation conclusion reports accidental loss even though the build and accepted-source comparison are clean.

**One form split into two.** One predecessor pattern-text form is split into two candidate forms. The accepted split decision names all three expressions. The complete predecessor inventory allocates a shared working-situation claim to both candidates, three predecessor claims to one candidate pattern card, and one obsolete tool instruction to an accepted content-retirement decision.

A predecessor non-use warning appears in neither candidate. Retiring the old form does not retire the warning, so the missing line blocks preservation until the warning is restored or its content change or retirement is accepted.

**Architecture diagram.** One FPF architecture-diagram form is replaced one-to-one by a candidate diagram for the same orientation use. The diagrams have no useful line diff. The maintainer uses the FPF pattern that defines or constrains that diagram form to select named framework parts, dependency edges, and legend distinctions for the inventory. They use `C.33` to record captured and lost structure and `C.34` to record the declared correspondence.

One predecessor dependency edge has no candidate correspondent, so similar layout cannot support a positive conclusion.

**Local practice framework.** An LPF candidate replaces a repeated general explanation with a reference to a new FPF method. The accepted-source comparison passes. The predecessor comparison checks the LPF's local recovery cue, concrete work-size limit, and tool-specific stop because the general FPF method does not include those local actions. Replacing these local actions with the reference would lose them.

**A thematic account changes carrier.** A Library removes a separately published account that connects general development Methods, human learning and organizational change. The general development construction belongs in Core. The human and organizational mechanisms remain in their DPFs. The account explains their combined use, so its receiver is the Library Architectural Reference. Copying every paragraph into Core would preserve the words but change which whole Core claims to explain.

The allocation first establishes these receivers, then checks the complete transferred account, the retained domain Methods and the updated current returns. A different passage explaining only the connections among Core patterns can remain in the Core account.

### E.4.PFIP:6 - Bias-Annotation

**Scope:** Limited to accepted-source integration and predecessor continuity for FPF, DPF, and LPF publication expressions. The complete-traversal rule applies across text, diagrams, cards, retrieval forms, and split or merged publications only when a selectable inventory and feasible semantic inspection exist for the declared use.

This method is not a universal software-merge, data-migration, or digital-preservation method.

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Gov | Source parity, a successful build, or an accepted form change is read as permission to change or retire predecessor content. | Require an accepted content-change or content-retirement decision for that disposition. Use the preservation conclusion as comparison evidence. Acceptance, release, landing and assurance need their own authority. |
| Arch | An edition, an identified expression, a reusable form, an expression relation, a carrier, and a publication occurrence collapse into one file or bundle, so a surviving carrier is treated as surviving content. | Keep the objects distinct. Use eligible expression pairs for one-to-one continuity and allocation comparisons for every split or merge. |
| Epist (Epistemological and Ontological) | A selected inventory is treated as complete knowledge of the publication because filenames, headings, or visible text were covered. | Select the inventory through the applicable FPF pattern or another accepted basis for the declared use. Return `missing form-comparison basis` when no complete inventory can be selected. |
| Prag | Complete traversal grows into a written positive ledger, or cost pressure turns one proxy into preservation proof. | Traverse every inventory entry, reuse shared evidence, and report only losses, accepted changes or retirements that explain a difference, unexpected additions, blockers, and unresolved questions. |
| Did | Retained content without a prose row looks unchecked, so reviewers ask for duplicate status text instead of inspecting the traversal boundary. | State once that the complete inventory is checkable and ordinary retained entries need no prose rows. Use the contrasting worked cases to teach where a separate result is required. |

The sources below come mainly from software transformation, merge analysis, and digital preservation. They show how to compare meaning and how the comparison depends on the form. A principle framework remains a different subject from software or an archival object. The applicable FPF pattern defines or constrains what matters for each form, and the maintainer selects the inventory for the declared publication use.

### E.4.PFIP:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-PFIP-1` Bounded candidate | The candidate framework edition and declared publication use are named. |
| `CC-PFIP-2` Accepted inputs complete | Every accepted source contribution is included. When it changes a public entry or consumed interface, the affected public entries and direct consumers are included with it, or that source contribution is left out of this candidate. |
| `CC-PFIP-3` Two questions kept separate | When the publication has a predecessor, accepted-source incorporation and predecessor preservation receive independent conclusions. |
| `CC-PFIP-4` Publication relations distinguished | Edition, individually identified expression, reusable form, expression and conformance relations, carrier, bearing relation, audience, bounded use, and publication occurrence are identified separately when they affect the comparison. |
| `CC-PFIP-5` Pair eligibility established | Every one-to-one pair has the same declared use plus retained form identity or an accepted one-to-one continuity decision. |
| `CC-PFIP-6` Complete inventory selected | Each pair uses a complete inventory selected through the FPF pattern that defines or constrains the form, or through another accepted comparison basis. |
| `CC-PFIP-7` Non-text structure handled | A non-span form uses content or selected-structure correspondence chosen for the declared use. Visual or carrier similarity remains only supporting evidence. |
| `CC-PFIP-8` Predecessor inventory covered | Every named item of predecessor content or selected structure is matched, intentionally changed or retired by an accepted content decision, accidentally lost, or blocked. |
| `CC-PFIP-9` Candidate additions classified | Candidate content or selected structure without predecessor correspondence is classified as an accepted or unexpected addition. |
| `CC-PFIP-10` Split and merge allocation complete | Every split or merge traverses every named predecessor inventory across named candidate expression parts even when a narrower pair survives. |
| `CC-PFIP-11` Form and content decisions separate | Every form retirement, split, or merge has separate outcomes for the content expressed by the predecessor form. |
| `CC-PFIP-12` Shared consumers checked once | Shared public entries and direct consumers are checked once without merging the expression comparisons that depend on them. |
| `CC-PFIP-13` Affordable result | Unchanged predecessor content and selected structure remain in the checkable traversal and do not become a positive prose ledger. |
| `CC-PFIP-14` Authority boundary preserved | The conclusion is identified as comparison evidence. Any construction, acceptance, admission, release, landing, or assurance decision is obtained separately. |

### E.4.PFIP:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Source parity proves preservation | Accepted additions are present, but unrelated predecessor content may be gone. | Run the predecessor-to-candidate comparison independently. |
| Successful build proves preservation | Syntax and assembly succeed while meaning or selected structure disappears. | Select the form-appropriate inventory and inspect semantic outcomes. |
| Same use means same form | Two different forms serving orientation are paired as versions. | Require retained form identity or an accepted one-to-one continuity decision. |
| Text diff for every form | Diagram relations, card fields, or retrieval cues have no meaningful shared spans. | Use the FPF pattern that defines or constrains the form, `C.33`, or `C.34` to select content or structure. |
| Retired form, retired content | A split or merge decision is taken to authorize every omission from the old form without a content decision. | Run the allocation comparison over the complete predecessor inventory. |
| Collective-publication shortcut | Several forms or carriers are renamed as one bundle so one comparison seems sufficient. | Keep named expressions separate and use them as inputs to the allocation comparison. |
| Carrier continuity as content continuity | An unchanged file or address is treated as proof that the selected edition and expression still obtain. | Apply `E.24.PUB` and compare the selected expression. |
| Positive preservation ledger | Every unchanged sentence or field receives a report row. | Keep completeness checkable and report losses, accepted differences, unexpected additions, blockers, and unresolved correspondences or content-change questions. |
| Fabricated predecessor | A first publication is forced through a predecessor comparison. | Check accepted-source incorporation, the complete candidate inventory, and changed public entries and direct consumers. Use the applicable package evaluation. |

### E.4.PFIP:9 - Consequences

Framework integration becomes more reliable because a maintainer can distinguish a missing accepted change from an accidental loss of predecessor content and can compare text, diagrams, cards, and split forms using an inventory suited to each representation.

The cost is additional work whenever the claimed continuity affects use. Each eligible pair needs a complete form-appropriate inventory, and each split or merge needs a complete allocation traversal.

The cost stays bounded because retained content needs no positive prose rows and the method is used only for accepted-source integration or publication continuity.

A later claim may rely on the conclusion only as allowed by the FPF pattern that defines or constrains that claim. The conclusion carries no process authority.

### E.4.PFIP:10 - Rationale

FPF, DPF, and LPF publications share the same integration problem. Accepted source carry-through and predecessor preservation answer different questions. When both are claimed, neither implies the other.

`E.24.PUB` distinguishes edition, expression, form, carrier, audience, use, and publication occurrence. `E.17` explains how to provide several reader-facing forms. `C.33` and `C.34` define captured, lost, and corresponding selected structure. Redefining those distinctions here would create a second publication ontology. The integration method uses these existing distinctions together.

The one-to-one and allocation branches remain separate because they answer different correspondence questions. A pair compares two expressions. An allocation traverses several named expressions without inventing a collective expression or treating a form decision as a content decision.

### E.4.PFIP:11 - SoTA-Echoing

| Current source branch and reference | Working lesson | Adoption in this pattern | Boundary |
| --- | --- | --- | --- |
| Semantic merge: Da Silva, Borba, Maciel et al. (2024), [“Detecting semantic conflicts with unit tests”](https://doi.org/10.1016/j.jss.2024.112070) | Current empirical work on semantic merge shows that textual and structured merge can succeed while an unwanted semantic change remains. The method uses behavior-relevant tests as partial specifications. | **Adapt.** A successful build or text diff alone does not establish preservation. Use an inventory for the declared use and state loss outcomes. | Software tests are not imported as a universal framework-publication check; each publication form supplies its own comparison basis. |
| Transformation traceability and versioned co-evolution: Höppner and Tichy (2024), [“Traceability and reuse mechanisms, the most important properties of model transformation languages”](https://doi.org/10.1007/s10664-023-10428-2), and Homolka, Marchezan, Assunção et al. (2026), [“What really happened to my models?”](https://doi.org/10.1007/s10664-025-10773-4) | The empirical survey identifies traceability and reuse as leading transformation-language capabilities while showing that their effects vary with use and scale. The later evaluated approach retains complete model and metamodel histories, links model changes to the changes that caused them, and permits several versions to coexist. | **Adapt.** Source contributions, predecessor content, and selected structures keep explicit candidate correspondences. Source incorporation does not replace predecessor preservation. Pair results may be reused inside a larger allocation without replacing it. | The survey measures transformation-language practice, and the later approach evaluates model co-evolution. Neither establishes complete traceability for a framework publication. This pattern adds no transformation language, operation history, automatic correspondence claim, or generic traceability relation. |
| Reusable model migration: Bettini, Di Salle, Iovino, and Pierantonio (2024), [“Supporting reusable model migration with Edelta”](https://doi.org/10.1016/j.jss.2024.112012) | Changes to a metamodel can invalidate dependent artifacts. The evaluated approach reuses migration patterns across domains while retaining custom or interactive rules for changes that automatic migration cannot settle. | **Adapt.** One reusable comparison method covers FPF, DPF, and LPF. The pattern that defines or constrains a publication form supplies its form-specific inventory, and a changed public interface brings its direct consumers into the candidate. | The Edelta language, metamodel kinds, automatic copier, and model-migration operations are not imported into FPF publication ontology. |
| Digital-preservation planning: the current [NARA Digital Preservation Framework](https://www.archives.gov/preservation/digital-preservation/risk), its [structured-data preservation guidance](https://www.archives.gov/preservation/digital-preservation/linked-data/structureddata), and Becker (2018), [“Metaphors We Work By”](https://archivaria.ca/index.php/archivaria/article/view/13628) | NARA selects significant properties by record type and uses them as transformation-test criteria while stating that its plans are not exhaustive or universal. Becker shows why bits, records, computed performances, and preservation claims cannot be collapsed into one digital-object metaphor. | **Adapt.** The applicable FPF pattern defines or constrains the inventory basis, the maintainer selects the inventory for the declared use, and edition, content, form, carrier, and publication occurrence remain separate. | NARA record categories and archival authenticity terms are not imported as FPF kinds or as one universal significant-property list. |

Compare the properties and correspondences that matter for the declared use. The easiest visible proxy may omit them. The sources support this distinction in different cases. Semantic merge informs the one-to-one text case. Traceability and migration inform the split-form case and direct-consumer closure. Digital preservation informs the diagram case and the separation of edition, form, content, and carrier.

The method adapts that stance to principle-framework publications and keeps its scope narrower than general software merge, data migration, or digital preservation.

Reopen this source use when current publication-preservation or structured-transformation practice supplies a cheaper complete semantic comparison, shows that trace reuse can replace rather than only support allocation traversal, or demonstrates a non-framework use that warrants a broader pattern scope.

### E.4.PFIP:12 - Relations

- **Builds on:** `C.2.1` for framework-episteme identity and `EpistemeEditionRelation`, and `E.24.PUB` for `PublicationExpressionRelation`, `PublicationExpressionBearingRelation`, `PublicationFormConformanceRelation`, and `EpistemePublicationRelation`, together with the form-mediated `PublicationFormExpressionRelation` and `PublicationFormBearingRelation` when making that broader claim. Identify the expression witnesses so that a later reader can recover them. These relations keep the selected edition, expression, reusable form, carrier, audience, bounded use, and publication occurrence distinct.
- **Coordinates with:** `E.17` for several reader-facing forms and visible omissions, `E.11` for public entry and discovery, `C.33` for captured and lost selected structure, and `C.34` for declared structural correspondence.
- **Coordinates with:** `E.8` for material-revision authoring and direct-consumer repair. A maintainer uses `E.4.PFIP` to compare an assembled principle-framework publication, not to replace pattern authoring.
- **Entry from FPF and DPF authoring:** `E.4.FPF` refers maintainers here for integration or continuity of an FPF publication edition. `E.4.DPF` does the same for a DPF or LPF publication edition. Those two patterns continue to supply their respective authoring and publication-form guidance.
- **Evaluation use:** A bounded preservation conclusion may be used as evidence under `E.4.DPF.DA` only when package adequacy for the declared use depends on publication integration or continuity. Use `E.2.DA` to evaluate whole-FPF adequacy and `E.21` to evaluate individual pattern quality.
- **Later reliance:** Use `C.2.1` to identify the preservation conclusion as an episteme. Use `A.10` when the source-to-use account remains implicit or bounded reliance must remain replayable, and `G.11` when currentness needs qualification. Those later claims are not part of the comparison.

### E.4.PFIP:End
