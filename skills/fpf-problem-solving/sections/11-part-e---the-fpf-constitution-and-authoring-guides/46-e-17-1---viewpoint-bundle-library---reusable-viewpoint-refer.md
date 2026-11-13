## E.17.1 - Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Tech-name.** `ViewpointBundleLibrary` (pattern and catalogue form, not a U-kind).

**Plain-name.** Viewpoint bundle library.

**Use this when.** The same coherent family of already admitted viewpoint editions recurs across projects, schools, or publication uses, and users need one editioned catalogue from which they can import viewpoint references without restating or reidentifying the viewpoints.

**First action.** Resolve one already admitted catalogue edition L and its family designator, retrieve the local declaration, and resolve only the `U.ViewpointRef` members needed now. If L or the declaration is new, missing, or disputed, use §4.2 to recover `<G_L, K_L, R_L>` and verify L's C.2.1 constitution for that edition. Reuse that result while the edition, effective scheme, and relied-on premises stay unchanged.

**First useful result.** One catalogue edition L, one ordinary family designator retrieving a local declaration claim block, and one finite non-empty member set of `U.ViewpointRef` values that each resolve to an E.17.0 viewpoint episteme edition. L retains its C.2.1 identity. The compact locator `<editionDesignator(L), familyDesignator>` aids retrieval under `R_L` but is neither L's identity nor a separate bundle kind or entity.

**Ordinary stop.** Stop when L, the declaration, and the needed reference subset are recoverable. Do not reconstruct L's constitution, instantiate every member, select an A.22 structure, prove conformance, or publish the catalogue merely to import an admitted family.

**Admission boundary.** E.24.UK admits `U.Viewpoint` and `U.View`; it does not admit `U.ViewpointBundleLibrary` or `U.ViewpointBundle`. E.17.1 therefore defines an ordinary catalogue-episteme form and local bundle declarations in its claim content.

**Do not use this when.** A describing use needs only to select one viewpoint or a small one-off set that has no recurring family-level purpose. Keep the references local; collecting them in a bundle adds no conformance, `U.Viewpoint` or `U.View` membership, structure, publication, or correspondence.

**What changes in practice.** Authors reuse references and preserve their bundle provenance. Reviewers can detect silent member substitution, alias collision, and package-driven membership claims.



**Builds on.**
`A.6.2-A.6.4` (episteme morphism classes), A.6.5 relation-declaration slot discipline, `A.7`, `E.7`, `E.10`, `E.10.D1`, `E.10.D2`, and `E.17.0 MultiViewDescribing`.

**Used by.**
`E.17.2` (TEVB engineering viewpoint bundles), `E.18:5.12`, and domain-specific viewpoint families for architecture, governance, safety, research, or assurance.

### E.17.1:1 - Problem frame

**Selected-family discipline.** A local declaration states its target-kind compatibility condition as either a by-value criterion or a reference that resolves to the ClaimGraph defining or constraining the admitted target kind. Bundle labels, aliases, annexes, files, and publication faces never supply that criterion or select an actual entity by themselves.

`MultiViewDescribing` lets engineers recognize several epistemes about one entity as views under viewpoint editions and recover cross-view relations only when those relations obtain. Many viewpoint families recur across projects and schools. Engineering teams reuse functional, procedural, structural and interface viewpoints. Governance teams reuse risk, control, compliance and operations viewpoints. Research teams reuse theory, experiment, inference and limitation viewpoints.

E.17.1 provides a pattern for packaging reusable viewpoint families. With it, authors can import them, name them stably, review them once, and keep viewpoint-family identity separate from document labels, publication faces, and publication forms.

### E.17.1:2 - Problem

When recurring viewpoint families lack a stable catalogue:

1. **Each domain invents local viewpoint families.**
   Similar families reappear under slightly different labels, but no stable catalogue `U.Episteme` records whether the underlying viewpoints are the same.
2. **Viewpoint identity drifts.**
   A family called `functional`, `capability`, or `operational` may differ only in name or may differ in meaning. Without a stable catalogue, users have no systematic way to tell.
3. **No catalogue entry to import.**
   Each describing use that needs the family must restate it locally instead of importing an existing bundle.
4. **No reusable local declaration.**
   Available viewpoints are known through external terminology or project lists, but no catalogue supplies the local references needed for repeated import.
5. **Reader-facing labels leak into semantics.**
   Authors reuse the same name for viewpoints, views, publication faces, or folders, and the boundary between EntityOfConcern and Description episteme becomes unclear.

### E.17.1:3 - Forces

| Force | Tension |
|---|---|
| **Reuse vs local fit** | Authors want reusable viewpoint families, but a local project may need a subset or a context-specific extension. |
| **Stable identity vs evolution** | Bundles must stay stable enough for long-term reuse while admitting editioned change. |
| **EntityOfConcern clarity vs label convenience** | A bundle library is a catalogue episteme whose members reference viewpoint epistemes, yet teams often prefer one reader-facing label across viewpoint, view, publication form, and carrier. |
| **Engineering vs publication discipline** | Engineering viewpoints and publication viewpoints both matter, but their reader-facing designators must not collapse into one lexical namespace. |
| **Rich libraries vs cognitive economy** | A library should be rich enough for reuse without becoming so large that authors cannot choose from it coherently. |

### E.17.1:4 - Solution - one catalogue episteme with local bundle declarations

`E.17.1` defines a reusable form for one ordinary C.2.1 catalogue episteme L whose local bundle declarations package `U.ViewpointRef` values resolving to E.17.0 viewpoint episteme editions. L, a declaration claim block within L, its ordinary family designator, each reference, each viewpoint designator, and P remain distinct. Neither the catalogue nor a declaration redefines viewpoint identity or membership, grants `U.View` membership, or creates publication forms and carriers.

#### E.17.1:4.1 - Core role

A conforming viewpoint-bundle library makes three things explicit:

- **which family is being named,** by an ordinary family designator interpreted under `R_L`;
- **which `U.ViewpointRef` members resolve to the viewpoint episteme editions packaged by that family;**
- **which target-kind compatibility condition and catalogue-edition discipline constrain the family.**

This lets `MultiViewDescribing` import a finite viewpoint family from a stable catalogue `U.Episteme` instead of restating it ad hoc in every local description family.

#### E.17.1:4.2 - Reuse an admitted catalogue; open full constitution only when needed

**Existing-catalogue route.** Resolve the already admitted catalogue edition L, retrieve the local declaration by its family designator under L's effective `R_L`, and resolve only the member references needed now. Do not reconstruct L's complete C.2.1 constitution merely to import an admitted edition.

Open the complete constitution below for the affected catalogue edition when authoring or admitting a new L, when the identity of L or its edition, or the resolution of a reference, is disputed, or when a named later use needs the catalogue's ClaimGraph, subject, or scheme as inspectable premises. Reuse an existing check while that edition, its effective scheme, and the relied-on premises stay unchanged. The complete constitution has three participants:

- `G_L : NonemptyClaimContent` is the catalogue's complete interpreted claim content (`ClaimGraph`), stating its scope, local family declarations, referenced viewpoint editions, target-kind compatibility conditions, and edition-change rule.
- `K_L` is the catalogue subject: the independently identified finite C.13 collection of already admitted viewpoint episteme editions whose recurring reuse groupings L describes. Its collection identity, members, obtaining membership relations, and identity rule are established before L. Neither the catalogue nor a declaration creates them.
- `R_L : EpistemeInterpretationScheme` is the effective rule collection under which the catalogue's ordinary library, edition, and family designators resolve; each `U.ViewpointRef` resolves to P; target-kind criteria and compatibility claims are interpreted; and reference, omission, provenance, and edition-change rules are read. C.2.1:4.1.2 supplies both ranges; the catalogue requires the full content and rule coverage stated here.

An eligible replacement for `R_L` must also resolve the catalogue’s designators and interpret its criteria. Range membership alone supplies neither result. A missing rule leaves the affected retrieval or compatibility judgement unresolved. Each referenced P retains its own effective scheme and E.17.0 membership. Resolving its reference under `R_L` does not transfer the catalogue's scheme to P.

`EpistemeConstitutionRelation(G_L, K_L, R_L)` must obtain. The participant-determined triple `<G_L, K_L, R_L>` identifies catalogue episteme L. If a proposed catalogue has only a file, label, list, or card but lacks an identifiable `K_L` or an effective `R_L`, stop. L has not yet been constituted.

`G_L` makes at least these claims recoverable:

- one ordinary library designator and one ordinary edition designator interpreted under `R_L`;
- a finite set of local family-declaration claim blocks, each retrievable inside `G_L` by one ordinary family designator interpreted under `R_L`;
- the `U.ViewpointRef` members and target-kind compatibility claim for each declaration; and
- only maintenance claims currently needed, using the branch that matches the present claim:
  - for a current maintenance-System claim, cite the admitted maintenance `U.System`; cite a local system-role kind and its independently evaluated classification only when that classification is current;
  - for actual maintenance Work, recover the actual performer through A.13 and let A.15.1 independently admit the dated `U.Work`. Add F.6 only when the catalogue claim or receiving use expressly relies on precise assignment-bound attribution through the same obtaining A.13 assignment. F.6 identifies neither assignment nor performer. Missing or failed F.6 alone leaves independently admitted Work intact. A short catalogue claim may omit identifiers its bounded use does not need;
  - for current maintenance responsibility, cite its direct admitted predicate and actual participants or return the missing governor; assignment establishes no responsibility; and
  - for prospective maintenance guidance, retain only the change-control note, intended maintenance condition or `U.WorkPlan`, and scope tag; this content asserts no performed Work, current assignment, or responsibility.

The catalogue entry cites these values. Their definitions or constraints come from elsewhere, and the entry creates none of them.

Library, edition, and family designators are lexical values under `R_L`, not local ValueKinds, public U-kinds, episteme identity discriminators, or entities by spelling. A local family declaration is claim content in `G_L`, not by itself a separate entity or episteme. Its compact locator `<editionDesignator(L), familyDesignator>` is a retrieval aid under `R_L`; it does not replace L's C.2.1 identity.

If a receiving use needs one declaration as a separately identified episteme, constitute that new episteme independently under C.2.1 rather than inferring it from a row.

Normative constraints:

1. Within one `G_L`, every family designator **SHALL** retrieve exactly one local declaration claim block under `R_L`.
2. A catalogue **SHALL NOT** define new kernel episteme kinds, id kinds, reference kinds, or publication-face/form kinds merely to type its fields.
3. A catalogue **MAY** be a core FPF catalogue or an organization-local extension when the same constitution, resolution, and family-declaration discipline remains recoverable.

#### E.17.1:4.3 - Local bundle declaration and its ordinary family designator

A bundle declaration is a bounded claim block inside `G_L`. It states one finite, non-empty recurring family of `U.ViewpointRef` values resolving to members of catalogue subject `K_L`. Under `R_L`, each reference resolves to one viewpoint episteme edition P already admitted to `U.Viewpoint` membership under E.17.0. The declaration neither admits P nor changes P's C.2.1 identity.

Its minimum claim content is:

- one ordinary `familyDesignator`, unique within `G_L` under `R_L`;
- one target-kind compatibility condition: either the by-value criterion used for this family or a reference that resolves to the ClaimGraph defining or constraining the admitted target kind. If member viewpoints use different fixed target-kind criteria, the declaration states the compatibility rule rather than inventing a common superclass token;
- `viewpointRefs`, one finite non-empty set of `U.ViewpointRef` values;
- optional references that resolve under their applicable schemes to archetypal-grounding examples or sections, with their intended recognition use stated;
- optional alignment claims naming the source and relation when a correspondence is asserted; and
- optional references that resolve under their applicable schemes to annex assets, each with its local role such as lexical note, Bridge material, A.16 move-publication note, example, or SoTA companion.

The family designator retrieves the declaration claim block inside L. A member `U.ViewpointRef` resolves to its P edition, and any reader-facing viewpoint token is only P's designator. The family designator, declaration claim block, reference, viewpoint designator, P, and L are distinct. No token, list position, prefix, alias, or member spelling substitutes for an episteme or reference.

The compatibility condition neither selects an actual EntityOfConcern for a describing use nor supplies or changes any member P's fixed target-kind criterion. Those claims remain in P and E.17.0 conformance.

A bundle is not a bundle of views, files, forms, carriers, or publication occurrences. If a receiving use needs an A.22 structure among the member viewpoints, it separately recovers obtaining relations and selects that structure. Declaration adjacency or order is not structure.

Changing the member-reference set, family meaning, compatibility condition, or the interpretation supplied by `R_L` changes `G_L` or the effective scheme and therefore identifies another catalogue episteme. Repackaging, annex layout, publication form, carrier, or audience does not reidentify unchanged L or any unchanged member viewpoint episteme.

#### E.17.1:4.4 - Import discipline into `MultiViewDescribing`

When you name a family designator for a describing use, resolve catalogue edition L and its effective `R_L`, retrieve the designated declaration inside `G_L`, then name the imported reference subset `Sigma`. If L or the declaration is not already recoverable, use §4.2 to establish `<G_L, K_L, R_L>` before import:

- `Sigma` is a subset of that declaration's `viewpointRefs` in L;
- every member is a `U.ViewpointRef` resolving to one admitted viewpoint episteme edition P;
- every candidate episteme E used under a member is independently identified under C.2.1 and is a `U.View` only when `EpistemeViewpointConformanceRelation(E,P)` obtains; and
- every one-viewpoint selection for one describing use carries a single `viewpointRef`; importing the family neither selects P for that use nor establishes conformance.

A local subset names catalogue edition L, the source family designator, and the member references actually used, and identifies omitted members as unused or intentionally excluded.

A multi-library use preserves each `<editionDesignator(L), familyDesignator>` source and member provenance rather than flattening everything into one unnamed family. If one use selects several viewpoints, it constructs their C.13 collection with membership. It does not overload one reference or infer a new family from adjacency.

Construction, identity viewing, transformation, declaration membership, selection, naming, rendering, or publication grants neither `U.Viewpoint` nor `U.View` membership.

A local overlay may add didactic or publication material without changing L. Changing a member viewpoint's meaning, the reference target, membership set, or family meaning requires a new local catalogue edition carrying the revised or new family declaration rather than silent mutation under the inherited family designator.

#### E.17.1:4.5 - Guard and naming discipline

- A viewpoint bundle is a family of **viewpoints**, not a bundle of views or documents.
- The family designator is an ordinary lexical value under `R_L`, not a local id kind, publication-face/form kind, reference, or entity.
- Engineering viewpoint designators and publication viewpoint designators may coexist, but their namespaces **SHALL** remain disambiguated.
- Bundle semantics come from the viewpoint episteme editions resolved by its member references, not from the spelling pattern of the family designator.

#### E.17.1:4.6 - Publication and representation stay outside the bundle

A published library is the same selected C.2.1 episteme edition participating in E.24.PUB relations:

- `PublicationExpressionRelation` relates that selected edition, one independently identified expression, and one bounded-use declaration;
- `PublicationExpressionBearingRelation` relates one independently identified physical or digital carrier to that expression;
- `PublicationFormConformanceRelation` relates the expression to any selected reusable publication form whose rules it satisfies; and
- `EpistemePublicationRelation` relates the selected edition, audience declaration, bounded-use declaration, expression, and carrier for one maximal continuous availability interval.

When form-mediated expression and bearing are claimed, retain E.24.PUB's corresponding relations with the same expression as witness. A change of exact publication need not interrupt broader availability of the library through its permitted expressions and carriers.

Changing a participant or restoring availability after a gap yields another publication occurrence under E.24.PUB; it does not reidentify unchanged L or any member viewpoint.

Rendering, printing, or uploading is separate system-performed `U.Work`. For a diagram or catalogue rendering, recover the correspondence between its elements and independently identified declarations or viewpoint epistemes. Use A.6.3.RT/A.6.3.RT.OE when constructing an expression or changing its representation scheme. Add C.29 when choosing or using a mathematical representation raises an inference or transfer question. Publication, representation, form, carrier, or rendering grants no viewpoint or view membership and makes no represented world-side relation obtain.

### E.17.1:5 - Archetypal Grounding


In FPF, an author can instruct a project to use an already defined viewpoint family without confusing that family with the views or publication faces the project uses later.

**System description: hypothetical template instance.** E.17.2 can guide one project to bind local references `r_functional`, `r_procedural`, `r_allocation`, and `r_module` to project P editions inside one constituted catalogue L. Until those bindings and their resolution under `R_L` exist, these names are variables and no reusable TEVB family value is present.

**Governance account: hypothetical family shape.** A project could bind local references for risk, control, compliance, and operations viewpoints in one catalogue declaration. The labels alone are not references or P editions. This example becomes reusable only after that project supplies complete `<G_L, K_L, R_L>`, bindings, and one ordinary family designator.

### E.17.1:6 - Bias-Annotation

After a recurring family-level use is established, the pattern favours reusing the catalogue and discourages teams from silently recreating the same family under local labels. For a one-off selection, keep the references local. The catalogue cost is justified only when reuse, comparison, or maintenance changes a named practitioner action.

### E.17.1:7 - Conformance Checklist

- `CC-VBL-0` The triple `<G_L, K_L, R_L>` constitutes L; ordinary import resolves an admitted L and its declaration without reconstructing that triple, while authoring, admission, or disputed identity opens the complete §4.2 check. Within `G_L`, each ordinary family designator retrieves exactly one local declaration claim block and remains distinct from L, member references, P designators, views, forms, and carriers.
- `CC-VBL-1` Every member is a `U.ViewpointRef` resolving to one independently admitted viewpoint episteme edition whose fixed target-kind criterion is compatible with the bundle constraint.
- `CC-VBL-2` Bundle membership, position, spelling, alias, packaging, or publication admits no P as `U.Viewpoint`; E.17.0 alone defines the membership test.
- `CC-VBL-3` A describing use imports a subset from `<editionDesignator(L), familyDesignator>`, preserves omissions and provenance, and selects any one P through a single reference.
- `CC-VBL-4` Every candidate E is independently identified and gains `U.View` membership only through obtaining E/P conformance—not through construction, selection, bundling, naming, form, carrier, rendering, or publication.
- `CC-VBL-5` A family designator is not used as an id kind, publication-face/form kind, carrier kind, viewpoint reference, or substitute for a member.
- `CC-VBL-6` Changes to member references, targets, family meaning, or compatibility constraints create another catalogue edition carrying the revised or new family declaration; publication or annex-only change does not reidentify unchanged P.
- `CC-VBL-7` Multi-bundle imports preserve catalogue provenance. A comparison identifies its predicate, participants, scope and operative interpretation and applies the subject method. A cross-local-sense use additionally retains the F.17 endpoints, obtaining F.9 Bridge and separate `<u,d,r,t>` claim; affirmative reliance needs the same-use A.10 provenance and the applicable ordinary-reliance or named-assurance result under F.9:4.2. Keep only the conclusion supported by these grounds.
- `CC-VBL-8` E.24.PUB expression, bearing, publication, recurrence, rendering work, and mathematical representation under C.29 remain distinct, grant no viewpoint or view membership, and make no represented world-side relation obtain.
- `CC-VBL-9` A bundle intended for non-expert reuse should provide references that resolve under their applicable schemes to archetypal-grounding examples or sections for its member viewpoints. Grounding aids recognition but grants no membership.

### E.17.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | How FPF prevents it |
|---|---|---|
| **Publication-face hijack** | A family designator is reused as a publication-face name or document type. | `CC-VBL-5` keeps the ordinary designator distinct from a publication face, form, carrier, viewpoint reference, or member. |
| **Bundle equals view collection** | A folder or report pack is called a viewpoint bundle even though no `U.ViewpointRef` values resolve to admitted `U.Viewpoint` epistemes. | `E.17.1` defines the bundle as a declared family of viewpoint references, not a file grouping. |
| **Silent local drift** | A local project keeps the old family designator but swaps in different viewpoints. | `CC-VBL-6` requires another catalogue edition carrying the revised or new family declaration when member references, targets, family meaning, or compatibility constraints change. |
| **Namespace collapse** | Engineering and publication viewpoint designators are mixed as if they were one lexical namespace. | The solution keeps the designator namespaces distinct and requires explicit attribution. |

### E.17.1:9 - Consequences

| Benefit | Trade-off / Mitigation |
|---|---|
| **Reusable viewpoint families.** Stable family designators within catalogue editions let many projects reuse the same declaration without restating it. | Catalogues need maintenance and edition discipline. |
| **Cleaner `MultiViewDescribing`.** A use can import a reviewed bundle instead of spelling out every viewpoint locally. | Authors must state local exceptions. |
| **Reusable catalogue without imported ontology.** A repeated-reference problem in FPF can be addressed with one local catalogue episteme. ISO 42010 supplies historical vocabulary. It supplies neither evidentiary authority nor an imported ontology. | Initial catalogue authoring requires care in C.2.1 constitution, reference resolution, and grounding. |
| **Lexical hygiene.** Family designators, viewpoint designators, views, publication faces, and publication forms stop collapsing into one label. | Authors must learn these distinctions and keep them in use. |

### E.17.1:10 - Rationale

`MultiViewDescribing` supports viewpoint plurality. `E.17.1` supplies packaging and provenance discipline for that plurality, including cases where viewpoints are used to re-express positions in a language-state chart declared under C.2.2a or language-state history accounts through the `LanguageStateMoveTrajectory` form under `A.16.0`. It makes member provenance explicit across repeated uses.

Semantic correspondence is a separate result: same-scheme comparison states its predicate and participants, while cross-context comparison uses F.9 and a bounded-use reliance path.

### E.17.1:11 - Source status, local rationale, and reopen condition

ISO 42010 is retained only as historical vocabulary lineage for the words *view* and *viewpoint*. It is not current architecting SoTA, does not supply FPF identity or conformance laws, and does not justify this catalogue architecture. No current external problem-solving source or reusable source comparison is claimed by this E.17.1 edition.

This design has a local FPF rationale. The problem is repeated use of the same E.17.0 viewpoint episteme editions. Users need to resolve references, preserve source catalogue and omission provenance, and avoid reidentifying P or turning a family label into membership.

One C.2.1 catalogue ClaimGraph with local declaration claim blocks is the least additional object that answers those actions while reusing C.2.1 identity, E.17.0 membership, C.13 collection, F.9 comparison, and E.24.PUB publication boundaries.

Reopen the local architecture if a current source or exercised project catalogue demonstrates a simpler way to preserve reference resolution, P identity, subsets, omissions, provenance, and cross-context comparison without losing any of those practitioner actions, or if project replay shows that one catalogue ClaimGraph with local declarations adds apparatus without changing a practitioner action. Until then, describe this as provisional local design, not source-established SoTA.

### E.17.1:12 - Relations

- **Builds on:** `C.2.1` for library and member-episteme identity; `E.17.0` for P membership, reference resolution, singular use selection, and sole E/P view-membership rule; `C.13` for explicit imported collections; `A.22` for any separately selected organization; `A.6.2-A.6.4` for optional episteme-construction histories; `A.7`, `E.7`, and `E.10` for carrier, authoring, and naming discipline; `E.24.PUB` for publication; `A.6.3.RT`/`A.6.3.RT.OE` for expression construction and representation-scheme transition; and `C.29` for mathematical-lens use.
- **Constrains:** E.17.0 consumers whenever they import a reusable family; an import narrows eligible references but neither selects one P for a use nor proves conformance.
- **Coordinates with:** `C.2.2a`, `A.16.0`, `E.17`, `E.17.2`, `E.18:5.12`, `F.9`, `F.9.1`, and domain-specific families requiring stable reuse.
- **Protects:** separation among catalogue triple `<G_L, K_L, R_L>`, catalogue episteme L, local declaration claim block, ordinary family designator, `U.ViewpointRef`, P designator, P, candidate/View E, any A.22 structure, form, carrier, publication occurrence, and their representations.

#### E.17.1:12.1 - Resolvable annex references for thin bundles

An ordinary project family designator may be accompanied by references that resolve under the applicable source or reference scheme to annex assets. Each reference states its local role, such as `lexical`, `bridge`, `movePublication`, `examples`, optional `sota`, or optional `pilotTrace`. Neither the field spelling nor the role value creates a new reference kind, manifest entity, or typed annex asset.

This keeps the declaration claim block thin while allowing A.16 move-publication notes, lexical material, Bridge material, and examples to remain explicit rather than folded into the core family claim.

### E.17.1:13 - Bundle Anatomy and Member Discipline

A viewpoint-bundle library becomes thin and reusable only when the bundle stays stable while the member viewpoints remain explicit enough to review independently. The bundle must be coherent as a family and clear about each member.

#### E.17.1:13.1 - What a viewpoint member should make explicit

Each `U.ViewpointRef` member inside a reusable bundle resolves to one viewpoint episteme edition whose claim content makes explicit at least:

- the **concern family** it brings into focus,
- **stakeholder or audience referents** only when they change the concerns,
- the **target-kind criterion** it carries and the compatibility condition under which this family can reuse it,
- the **independently admitted episteme kinds** whose membership rules allow candidates under that viewpoint,
- any **bundle-specific conformance notes** later users must retain, plus a reference that resolves to the comparison claim or F.9 Bridge when either has independently been established; a note or reference creates no correspondence.

`E.17.1` does not redefine the internals of `U.Viewpoint`. It states what must remain visible if a viewpoint is to be reused as part of a bundle rather than as an undocumented local label.

#### E.17.1:13.2 - Bundle-level coherence

A shared prefix does not make a coherent bundle. A coherent bundle should answer a recognizable family-level question, such as:

- *which engineering concerns are standard for holon description?*
- *which governance perspectives are required for a service review?*
- *which research-method viewpoints recur across inquiry reports?*

If the member viewpoints do not share that family-level purpose, the result is not one bundle but an uncurated catalogue fragment.

#### E.17.1:13.3 - Thin bundles, rich annexes

`E.17.1` allows bundles to stay thin. Projects may link to companion material by references that resolve to the annex assets under their applicable schemes. State the local role of each reference. Examples include:

- lexical discipline notes,
- bridge overlays,
- A.16 move-publication notes,
- worked examples,
- or SoTA references

This preserves a stable declaration claim block while letting the reuse package carry enough teaching material and review guidance.

### E.17.1:14 - Import, Subset, and Multi-Bundle Coordination

Importing a family, selecting a subset and coordinating several families show why viewpoint bundles are useful. Make each choice explicit so that other users can tell what the project has reused and what it has changed.

#### E.17.1:14.1 - Subset selection

A `MultiViewDescribing` use may import only a subset of a bundle's viewpoint references. When it does so, it should declare:

- which ordinary family designator is the source,
- which viewpoint members are in local use,
- and whether the omitted members are unused or are intentionally excluded because the local scope does not require them.

The local family must not speak as if it had imported the whole bundle while silently dropping inconvenient viewpoints.

#### E.17.1:14.2 - Local overlays vs new bundles

A local project often wants a small adaptation: one extra concern note, one narrower stakeholder emphasis, one local naming convention. `E.17.1` prefers explicit overlays or new editions over silent mutation.

A practical rule is:

- if the local project selects a subset or adds only didactic/publication material, keep catalogue edition L and its declaration unchanged and declare the local subset or annex; do not treat the overlay as declaration content;
- if the local project changes viewpoint membership or meaning, publish a new local catalogue edition carrying the revised or new family declaration.

#### E.17.1:14.3 - Multi-bundle coordination: provenance first, comparison separately

Many description families need more than one bundle, for example:

- one engineering viewpoint family,
- one safety or assurance family,
- and one governance or publication-oriented family.

Preserve the provenance of every imported `U.ViewpointRef` and resolved P as `<editionDesignator(L), familyDesignator, member reference>`. That tuple identifies where each member came from. It establishes no semantic sameness, difference, correspondence, translation, substitution, or admissible comparison by itself.

Identify the P editions or claim subgraphs being compared, the comparison predicate, polarity, scope and participants. Recover how each source interprets the values used by that predicate, then apply its subject method. Different schemes may require a representation or quantity conversion without requiring a semantic Bridge. If the material supports only a lexical or structural contrast (such as members, omissions, order, target criteria or claim-shape differences), state that limited result.

When the comparison or proposed reuse depends on a semantic relation between distinct local senses, resolve their F.17 `SchemeSenseCell` endpoints and establish the F.9 Bridge. State the proposed use separately as one bounded C.2.1 claim about that Bridge with `<u,d,r,t>` and polarity.

For reliance on an affirmative claim, retain the same-use A.10 provenance. Ordinary reliance requires `RelianceDisposition=pass`; when a named assurance claim is current, require its B.3 result with `disposition=supported-for-use` for that bounded use.

If a required meaning, correspondence or reliance ground is missing, withhold the dependent conclusion and retain the supported contrast or exact inquiry. Catalogue provenance identifies the sources in every branch.

#### E.17.1:14.4 - Engineering vs publication families

Some contexts need both engineering viewpoints and publication viewpoints. A shared family designator must preserve the distinction between engineering and publication viewpoints. A family that imports both kinds must keep the namespaces and catalogue origins explicit so that authors can distinguish *how the holon is being understood* from *how a publication face/form chooses to expose that understanding*.

### E.17.1:15 - Worked family shapes, not shipped catalogue values

#### E.17.1:15.1 - Hypothetical TEVB project binding

E.17.2 supplies an authoring template, not a repository-shipped family. One project may constitute catalogue L and bind four local variables:

- `r_functional -> P_functional`,
- `r_procedural -> P_procedural`,
- `r_allocation -> P_allocation`,
- `r_module -> P_module`.

Only after those are `U.ViewpointRef` values resolving to admitted P editions under L's effective scheme can the project's ordinary family designator retrieve a reusable local declaration. Another project with similarly spelled variables or labels has not imported this family unless it resolves the same L and references.

#### E.17.1:15.2 - Hypothetical governance and risk shape

A project may author a governance-oriented declaration with local reference variables such as:

- `r_risk -> P_risk`,
- `r_control -> P_control`,
- `r_compliance -> P_compliance`,
- `r_operations -> P_operations`.

This is an example of a possible declaration shape, not a current family. Each left-hand variable must be bound to a local `U.ViewpointRef`; each right-hand variable must be bound to one P independently admitted under E.17.0. L, `R_L`, and the family designator must exist before reusable import is claimed. The four positions recur together but remain non-interchangeable.

#### E.17.1:15.3 - Hypothetical research-method shape

A project may likewise consider local variables `r_theory`, `r_experiment`, `r_inference`, `r_limitations`, and, where appropriate, `r_reproducibility`. This list teaches a candidate family shape only. A local inquiry note can import a subset only after the project has constituted L, bound each retained variable to a reference and P, and made omitted members visible in one declaration claim block.

#### E.17.1:15.4 - Cross-family description relation positions

A project may use one materialized local TEVB instance for its design family, another local governance family for program oversight, and another local publication-oriented family for publication faces and forms. `E.17.1` keeps these relation positions reviewable by preserving which catalogue and declaration each viewpoint came from and by preventing a final publication face or form from masquerading as the catalogue itself.

### E.17.1:16 - Authoring and Review Guidance

#### E.17.1:16.1 - For bundle authors

Bundle authors should ask:

- what recurring family is being named,
- which viewpoints belong together in that family,
- what local didactic publications or examples belong in annexes instead of the bundle core,
- and whether the bundle is stable enough to deserve a reusable family designator.



#### E.17.1:16.2 - For reviewers

Reviewers should inspect both levels:

- **member level** - are the included viewpoints individually explicit enough to be reused?
- **bundle level** - do they form one coherent family rather than one convenient list?

They should also check whether a local project has silently forked the bundle while still using the inherited family designator.

#### E.17.1:16.3 - For integrators and librarians

Integrators should keep libraries small, curated, and editioned. Publish only the smallest declaration set the current reuse needs:

- one stable core declaration when a recurring family is established,
- one explicit local extension only when local membership or meaning changes,
- and one clear subset declaration only when the current use imports a subset.

Do not create all three by default.

### E.17.1:17 - Edition and Migration Notes

#### E.17.1:17.1 - Rename vs semantic change

A lexical rename that leaves viewpoint meaning and membership unchanged may be treated as a naming-layer migration. A change in membership, concern, admissibility, or member semantics requires another catalogue edition carrying the revised or new family declaration.

#### E.17.1:17.2 - Migration from local `Sigma` lists

Legacy `MultiViewDescribing` uses often publish only one local list of viewpoints. Migration should proceed by:

1. identifying recurring families across several such local lists,
2. publishing those families as explicit bundles,
3. then rewriting the local families to import the new ordinary family designator and declare any subset selection.

This sequence preserves provenance and avoids pretending that the reusable family had always existed.

#### E.17.1:17.3 - Migration from publication-face/form-bound naming

If a legacy practice uses one label interchangeably for a viewpoint family, a viewpoint, a report section, and a publication face, distinguish those uses of the label during migration. The ordinary family designator remains at the declaration layer. `U.ViewpointRef` values resolve P while any reader-facing viewpoint token is only P's designator. Publication-face names remain publication-layer vocabulary.

#### E.17.1:17.4 - Boundary to annex growth

Annex references are useful, but a declaration should not become a thin shell hiding all of its meaning elsewhere. The core declaration must state enough about its members and their organization as a family to stand on its own. Annexes deepen reuse, but they do not replace the declaration's primary claims.
### E.17.1:18 - Import Collision and Alias Discipline

#### E.17.1:18.1 - A family designator is not a synonym bag
An ordinary family designator does not mean that all member viewpoints are interchangeable labels for one concern. One declaration states that this reviewed family of viewpoints is intended to recur together. Authors should keep the family designator distinct from each member.

#### E.17.1:18.2 - Import collision rule
When two imported bundles contribute viewpoints with overlapping lexical names, preserve the originating viewpoint designators and catalogue provenance rather than silently merging the members. Inspectable collisions make provenance adequate; they do not show that the local senses correspond or that either member may substitute for the other.

#### E.17.1:18.3 - Alias boundary
Local teaching aliases may be added for readability, but the alias must identify the member viewpoints it denotes and must not erase bundle provenance. If the alias alone is used to select the bundle, the selection is unsupported. The project should replace the alias in that use with explicit member references.

### E.17.1:19 - Bundle Projection and Comparative Use

#### E.17.1:19.1 - Projection to local subsets
A description family may project only a subset of a reusable bundle. This is admissible if the description of the local subset identifies the omitted members. Projection keeps bundle provenance intact while acknowledging that local publication rarely uses every member.

#### E.17.1:19.2 - Comparative bundle use

Name the members or claim subgraphs, comparison predicate, polarity, scope and participants; recover their operative interpretation and apply the subject method as in :14.3. If only names, member sets, omissions or structures can be compared, state that bounded contrast and stop.

When the comparison needs a semantic relation between distinct local senses, use their F.17 cells and the obtaining F.9 Bridge. A proposed comparison, translation or reuse needs its separate bounded-use claim with direction, correspondence rule, tolerated loss and polarity. For reliance on an affirmative claim, retain the same-use A.10 provenance and the applicable ordinary-reliance or named-assurance result under F.9:4.2. Use F.9.1 only when a separate stance episteme about that bounded-use claim is needed. The note explains this use and leaves the Bridge and its bounded-use claim unchanged. Assess a different correspondence or a wider use under F.9. Retain an unresolved required basis as the limit on the dependent use.

#### E.17.1:19.3 - Boundary to publication-face design
A publication face may render one composite presentation of several viewpoints, but the face is not the bundle. `E.17.1` therefore requires the underlying member structure to remain recoverable even when a public-facing document flattens it for readability.

### E.17.1:20 - Review Matrix and Catalogue Maintenance

A reviewer can test a viewpoint bundle library with five questions:

1. **Do the member viewpoints still have explicit standalone meaning?**
2. **Does the declaration retrieved by the family designator describe one coherent recurring family rather than one convenience list?**
3. **If a subset is imported, can the reviewer see which members were omitted?**
4. **If several bundles interact, is provenance preserved, and does each comparison use its subject method with F.9 added only for a semantic relation between distinct local senses?**
5. **Has a publication face started impersonating the library?**

Prefer small, provenance-preserving declarations inside editioned catalogues over lexical mega-families that are easy to name but hard to reuse truthfully.
### E.17.1:End
