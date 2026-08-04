## E.17.1 - `U.ViewpointBundleLibrary` - Reusable Viewpoint Bundles

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Viewpoint bundle library.

**Use this when.** The same coherent family of already admitted viewpoint editions recurs across projects, schools, or publication uses, and users need one editioned catalogue from which exact viewpoint references can be imported without restating or reidentifying the viewpoints.

**First useful result.** One exact library edition, one `ViewFamilyId`, and one finite non-empty set of `U.ViewpointRef` values that each resolve to an exact E.17.0 viewpoint episteme edition.

**Do not use this when.** One describing use merely selects one viewpoint or a small one-off set that has no recurring family-level purpose. Keep the exact references local; a bundle adds no conformance, membership, structure, publication, or correspondence merely by collecting them.

**What changes in practice.** Authors reuse governed references and preserve their bundle provenance; reviewers can detect silent member substitution, alias collision, and package-driven membership claims.



**Builds on.**
`A.6.2-A.6.4` (episteme morphism classes), `A.6.5 U.RelationSlotDiscipline`, `A.7`, `E.7`, `E.10`, `E.10.D1`, `E.10.D2`, and `E.17.0 MultiViewDescribing`.

**Used by.**
`E.17.2` (TEVB engineering viewpoint bundles), `E.18:5.12`, and domain-specific viewpoint families for architecture, governance, safety, research, or assurance.

### E.17.1:1 - Problem frame

**Selected-family discipline.** Viewpoint bundles declare `EntityOfConcernClassSpec` constraints for the selected entities their viewpoints can describe. Bundle labels, aliases, annexes, files, and publication faces never select the entity by themselves.

`MultiViewDescribing` lets engineers recognize several epistemes about one exact entity as views under exact viewpoint editions and recover cross-view relations only when those relations actually obtain. In practice many such viewpoint families recur across projects and schools: engineering teams reuse functional / procedural / structural / interface viewpoints; governance teams reuse risk / control / compliance / operations viewpoints; research teams reuse theory / experiment / inference / limitation viewpoints.

FPF therefore needs one explicit governing pattern for reusable viewpoint families so that authors can import them, name them stably, review them once, and keep viewpoint-family identity separate from document labels, publication faces, and publication forms.

### E.17.1:2 - Problem

Without a viewpoint-bundle library pattern:

1. **Each domain invents local viewpoint families.**
   Similar families reappear under slightly different labels, but no stable catalogue `U.Episteme` records whether the underlying viewpoints are actually the same.
2. **Viewpoint identity drifts.**
   A family called `functional`, `capability`, or `operational` may differ only lexically, or may differ semantically, but there is no disciplined place to tell which is which.
3. **`MultiViewDescribing` cannot reuse a family cleanly.**
   Every instance must restate its finite viewpoint family locally instead of importing an existing bundle.
4. **ISO 42010-style viewpoint libraries remain external.**
   FPF lacks a native place where reusable viewpoint libraries can be expressed as first-class, reviewable objects.
5. **Reader-facing labels leak into semantics.**
   Authors reuse the same name for viewpoints, views, publication faces, or folders, and the boundary between EntityOfConcern and Description episteme becomes unclear.

### E.17.1:3 - Forces

| Force | Tension |
|---|---|
| **Reuse vs local fit** | Authors want reusable viewpoint families, but a local project may still need a subset or a context-specific extension. |
| **Stable identity vs evolution** | Bundles must stay stable enough for long-term reuse while still admitting editioned change. |
| **EntityOfConcern clarity vs label convenience** | A bundle library is a catalogue episteme whose members reference exact viewpoint epistemes, yet teams often prefer one reader-facing label across viewpoint, view, publication form, and carrier. |
| **Engineering vs publication discipline** | Engineering viewpoints and publication viewpoints both matter, but they must not collapse into one id namespace. |
| **Rich libraries vs cognitive economy** | A library should be rich enough for real reuse without becoming so large that authors cannot choose from it coherently. |

### E.17.1:4 - Solution - `U.ViewpointBundleLibrary`

`E.17.1` governs `U.ViewpointBundleLibrary` as one reusable C.2.1 catalogue episteme whose named bundles package exact `U.ViewpointRef` values resolving to exact E.17.0 viewpoint episteme editions. Library, bundle, family id, reference, designator, and P remain distinct. Neither a library nor bundle redefines viewpoint identity or membership, grants `U.View` membership, or creates publication forms and carriers.

#### E.17.1:4.1 - Core role

A conforming viewpoint-bundle library makes three things explicit:

- **which family is being named,** via `ViewFamilyId`;
- **which `U.ViewpointRef` members resolve to the exact viewpoint episteme editions packaged by that family;**
- **under what entity of concern class and edition discipline** the family is valid.

This lets `MultiViewDescribing` import a finite viewpoint family from a stable catalogue `U.Episteme` instead of restating it ad hoc in every local description family.

#### E.17.1:4.2 - `U.ViewpointBundleLibrary` (catalogue episteme)

A `U.ViewpointBundleLibrary` is a catalogue `U.Episteme` of viewpoint bundles with at least:

- `libraryId : LibraryId`
- `editionId : EditionId`
- `bundles : FinSet(U.ViewpointBundle)`
- optional governance metadata such as responsibility role assignment, change-control note, or scope tags

Normative constraints:

1. Within one library edition, each `ViewFamilyId` **SHALL** be unique.
2. Libraries **SHALL NOT** define new kernel episteme kinds or publication-face/form kinds.
3. Libraries **MAY** be specialized as core FPF libraries or organization-local extensions that preserve the same bundle discipline.

#### E.17.1:4.3 - `U.ViewpointBundle` and `ViewFamilyId`

A `U.ViewpointBundle` is a finite, non-empty family of governed `U.ViewpointRef` values packaged for reuse. Every reference resolves to one exact viewpoint episteme edition that has already gained `U.Viewpoint` membership under E.17.0. The bundle neither admits P nor changes P's C.2.1 identity.

Minimal structure:

- `viewFamilyId : ViewFamilyId`;
- `EntityOfConcernClassSpec <: U.Entity`, used only as the compatibility constraint for the targets admitted by the member viewpoints;
- `viewpointRefs : FinSet(U.ViewpointRef)`;
- optional `ArchetypalCards : FinSet(U.ArchetypalGroundingRef)`;
- optional `AlignmentNotes` for exact ISO 42010 or domain-standard correspondence claims; and
- optional typed annex references for lexical, bridge, A.16 move-publication, example, or SoTA companion material.

`ViewFamilyId` designates the bundle. A member `U.ViewpointRef` resolves an exact P, and any `ViewpointId` exposed for readers is only P's designator. The family id, reference, designator, and episteme are distinct; no token, list position, prefix, alias, or member spelling substitutes for P.

The bundle constraint does not select an actual EntityOfConcern, supply P's fixed target-kind criterion, or judge a candidate episteme. Those claims remain in exact P and E.17.0 conformance. A bundle is not a bundle of views, files, forms, carriers, or publication occurrences. If a receiving use needs an A.22 structure among the member viewpoints, it separately recovers exact obtaining relations and selects that structure; bundle adjacency or order is not structure.

Changing the member-reference set, family meaning, or compatibility constraint requires another bundle edition. Repackaging, annex layout, publication form, carrier, or audience does not reidentify any unchanged member viewpoint episteme.

#### E.17.1:4.4 - Import discipline into `MultiViewDescribing`

When a describing use declares a `ViewFamilyId`, it identifies the exact library and bundle edition and then names the exact imported reference subset `Sigma`:

- `Sigma` is a subset of that exact bundle edition's `viewpointRefs`;
- every member is an exact `U.ViewpointRef` resolving to one admitted viewpoint episteme edition P;
- every candidate episteme E used under a member is independently identified under C.2.1 and is a `U.View` only when `EpistemeViewpointConformanceRelation(E,P)` obtains; and
- every actual one-viewpoint selection for one describing use carries one singular `viewpointRef`; importing the family neither selects P for that use nor establishes conformance.

A local subset names both the source `ViewFamilyId` and the member references actually used, while keeping omitted members visible as unused or intentionally excluded. A multi-bundle use preserves each exact source bundle edition and member provenance rather than flattening everything into one unnamed family. If one use selects several viewpoints, it constructs their exact governed C.13 collection; it does not overload one reference or infer a new family from adjacency.

Construction, identity viewing, transformation, bundle membership, selection, naming, rendering, or publication grants neither `U.Viewpoint` nor `U.View` membership. A local overlay may add didactic or publication material without changing the imported bundle. Changing a member viewpoint's meaning, the reference target, membership set, or family meaning requires a new local bundle or edition rather than silent mutation under the inherited id.

#### E.17.1:4.5 - Guard and naming discipline

- A viewpoint bundle is a family of **viewpoints**, not a bundle of views or documents.
- `ViewFamilyId` is a lexical family id, not a publication-face/form kind.
- Engineering viewpoint ids and publication viewpoint ids may coexist, but they **SHALL** remain disambiguated.
- Bundle semantics come from the exact viewpoint episteme editions resolved by its member references, not from the spelling pattern of the family id.

#### E.17.1:4.6 - Publication and representation stay outside the bundle

A published library is the same selected C.2.1 episteme edition participating in exact E.24.PUB relations:

- `PublicationFormExpressionRelation` relates that selected edition, one exact publication form, and one exact bounded-use declaration;
- `PublicationFormBearingRelation` relates one exact `U.PresentationCarrier` and that form; and
- `EpistemePublicationRelation` relates the selected edition, audience declaration, bounded-use declaration, form, and carrier for one maximal continuous availability interval.

Changing a participant or restoring availability after a gap yields another publication occurrence under E.24.PUB; it does not reidentify an unchanged library, bundle, or member viewpoint. Rendering, printing, or uploading is separate system-performed `U.Work`. C.29 representation is separately governed when a diagram or catalogue rendering corresponds to independently recovered bundle objects. Publication, representation, form, carrier, or rendering grants no viewpoint or View membership and makes no world-side subject relation obtain.

### E.17.1:5 - Archetypal Grounding


**Tell.** A viewpoint bundle library lets FPF say "use this already-defined viewpoint family" without confusing that family with the concrete views or publication faces that later realize it.

**Show (System).** A TEVB engineering bundle can package exact `U.ViewpointRef` members `ref(VP.Functional)`, `ref(VP.Procedural)`, `ref(VP.AllocationResponsibility)`, and `ref(VP.ModuleInterface)` for holon descriptions. Each reference resolves the exact viewpoint episteme P designated by its corresponding `VP.*` token. Later `MultiViewDescribing` uses import that exact bundle edition and the needed reference subset rather than redefining the same engineering viewpoints each time.

**Show (Episteme).** A governance-oriented bundle can package exact `U.ViewpointRef` members `ref(VP.Risk)`, `ref(VP.Control)`, `ref(VP.Compliance)`, and `ref(VP.Operations)` as one reusable family for service or program descriptions. Each reference resolves the exact viewpoint episteme P designated by its corresponding `VP.*` token. Publication faces/forms may later expose that family, but the bundle itself remains a value inside a viewpoint-family catalogue `U.Episteme`, not the report publication face.

### E.17.1:6 - Bias-Annotation

The pattern biases FPF toward bundle-first reuse and against ad hoc local re-invention of recurring viewpoint families. That bias is intentional. The small cost of maintaining libraries and editions is lower than the long-term cost of unstable viewpoint identity.

### E.17.1:7 - Conformance Checklist

- `CC-VBL-0` Within one exact library edition, each `ViewFamilyId` identifies exactly one bundle and remains distinct from member references, P designators, views, forms, and carriers.
- `CC-VBL-1` Every member is an exact `U.ViewpointRef` resolving to one independently admitted viewpoint episteme edition whose fixed target-kind criterion is compatible with the bundle constraint.
- `CC-VBL-2` Bundle membership, position, spelling, alias, packaging, or publication admits no P as `U.Viewpoint`; E.17.0 remains the sole membership owner.
- `CC-VBL-3` A describing use imports an exact subset from an exact bundle edition, preserves omissions and provenance, and selects any one actual P through one singular reference.
- `CC-VBL-4` Every candidate E is independently identified and gains `U.View` membership only through obtaining E/P conformance—not through construction, selection, bundling, naming, form, carrier, rendering, or publication.
- `CC-VBL-5` `ViewFamilyId` is not used as a publication-face/form kind, carrier kind, viewpoint reference, or substitute for an exact member.
- `CC-VBL-6` Changes to member references, targets, family meaning, or compatibility constraints create another bundle edition; publication or annex-only change does not reidentify unchanged P.
- `CC-VBL-7` Multi-bundle imports preserve source editions and collisions; any separately needed organization or correspondence has its own A.22 or direct-relation governor.
- `CC-VBL-8` E.24.PUB expression, bearing, publication, recurrence, rendering work, and C.29 representation remain distinct and establish neither membership nor a world-side subject relation.
- `CC-VBL-9` A bundle intended for non-expert reuse should provide exact archetypal-grounding references for its member viewpoints; grounding aids recognition but grants no membership.

### E.17.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | How FPF prevents it |
|---|---|---|
| **Publication-face hijack** | A `ViewFamilyId` is reused as a publication-face name or document type. | `CC-VBL-5` keeps the family designator distinct from a publication face, form, carrier, viewpoint reference, or exact member. |
| **Bundle equals view collection** | A folder or report pack is called a viewpoint bundle even though no governed references resolve to admitted `U.Viewpoint` epistemes. | `E.17.1` defines the bundle as a declared family of exact viewpoint references, not a file grouping. |
| **Silent local drift** | A local project keeps the old family id but swaps in different viewpoints. | `CC-VBL-6` requires another bundle edition when member references, targets, family meaning, or compatibility constraints change. |
| **Namespace collapse** | Engineering viewpoint ids and publication viewpoint ids are mixed as if they were one namespace. | The solution keeps id spaces distinct and requires explicit attribution. |

### E.17.1:9 - Consequences

| Benefit | Trade-off / Mitigation |
|---|---|
| **Reusable viewpoint families.** Stable bundle ids let many projects reuse the same family without restating it. | Libraries need governance and edition discipline. |
| **Cleaner `MultiViewDescribing`.** A use can import a reviewed bundle instead of spelling out every viewpoint locally. | Local exceptions must be made explicit rather than hidden in prose. |
| **Better architectural alignment.** ISO 42010-style viewpoint-library practice gains a native FPF catalogue episteme. | Initial bundle authoring requires care in naming and grounding. |
| **Lexical hygiene.** Bundle ids, viewpoint ids, views, publication faces, and publication forms stop collapsing into one label. | Authors must learn the separation once and then keep it. |

### E.17.1:10 - Rationale

`MultiViewDescribing` already assumes that viewpoint plurality exists. `E.17.1` supplies the packaging discipline for that plurality, including cases where viewpoints are used to re-express positions in `U.LanguageStateSpace` or trajectories in `U.LanguageStateMoveTrajectory`. Without it, every domain can only improvise locally, and long-term correspondence between viewpoint families remains fragile.

### E.17.1:11 - SoTA-Echoing

The pattern aligns with post-2015 multi-view practice: ISO 42010 viewpoint libraries, model-based systems engineering viewpoint catalogues, assurance-oriented viewpoint families, and reusable concern bundles in architecture and governance work. FPF adopts the reusable-library idea, but keeps the ontology stricter by separating bundle ids, viewpoint ids, views, publication faces, and publication forms.

### E.17.1:12 - Relations

- **Builds on:** `C.2.1` for library and member-episteme identity; `E.17.0` for exact P membership, reference resolution, singular use selection, and sole E/P view-membership rule; `C.13` for explicit imported collections; `A.22` for any separately selected organization; `A.6.2-A.6.4` for optional episteme-construction histories; `A.7`, `E.7`, and `E.10` for carrier, authoring, and naming discipline; `E.24.PUB` for publication; and `C.29` for representation.
- **Constrains:** E.17.0 consumers whenever they import a reusable family; an import narrows eligible references but neither selects one P for a use nor proves conformance.
- **Coordinates with:** `C.2.2a`, `A.16.0`, `E.17`, `E.17.2`, `E.18:5.12`, `F.9`, `F.9.1`, and domain-specific families requiring stable reuse.
- **Protects:** exact separation among library edition, bundle edition, `ViewFamilyId`, `U.ViewpointRef`, P designator, P, candidate/View E, any A.22 structure, form, carrier, publication occurrence, and C.29 representation.

#### E.17.1:12.1 - Typed annex manifests for thin bundles

`VF.*` and other reusable viewpoint bundles may reference typed `AnnexManifestRef` assets with roles such as `lexical`, `bridge`, `movePublication`, `examples`, optional `sota`, and optional `pilotTrace`. This keeps the bundle itself thin while allowing A.16 move-publication notes, lexical baggage, and bridge annexes to remain explicit and typed rather than folded into the bundle core.

### E.17.1:13 - Bundle Anatomy and Member Discipline

A viewpoint-bundle library becomes thin and reusable only when the bundle itself stays stable while the member viewpoints remain explicit enough to review independently. The bundle therefore has two simultaneous obligations: coherence at the family level and clarity at the member level.

#### E.17.1:13.1 - What a viewpoint member should make explicit

Each `U.ViewpointRef` member inside a reusable bundle resolves to one exact viewpoint episteme edition whose claim content makes explicit at least:

- the **concern family** it brings into focus,
- the **stakeholder families** for whom that concern matters,
- the **entity of concern class** for which it is admissible,
- the **independently admitted episteme kinds** whose exact membership rules allow candidates under that viewpoint,
- and any **bundle-specific conformance or correspondence notes** that later view families should preserve.

`E.17.1` does not redefine the internals of `U.Viewpoint`. It states what must remain visible if a viewpoint is to be reused as part of a bundle rather than as an undocumented local label.

#### E.17.1:13.2 - Bundle-level coherence

A bundle is not just a bag of viewpoints with one shared prefix. A coherent bundle should answer a recognizable family-level question, such as:

- *which engineering concerns are standard for holon description?*
- *which governance perspectives are required for a service review?*
- *which research-method viewpoints recur across inquiry reports?*

If the member viewpoints do not share that family-level purpose, the result is not one bundle but an uncurated catalogue fragment.

#### E.17.1:13.3 - Thin bundles, rich annexes

`E.17.1` intentionally allows bundles to stay thin. Rich companion material such as:

- lexical discipline notes,
- bridge overlays,
- A.16 move-publication notes,
- worked examples,
- or SoTA references

may live in typed annex manifests. This preserves a stable bundle core while still letting reuse packages carry enough didactic material and review help.

### E.17.1:14 - Import, Subset, and Multi-Bundle Coordination

The value of viewpoint bundles appears most clearly when they are imported, subsetted, and coordinated across several reused families. Those cases need explicit discipline so that a local project does not quietly mutate what it claims to be reusing.

#### E.17.1:14.1 - Subset selection

A `MultiViewDescribing` use may legitimately import only a subset of a bundle's viewpoint references. When it does so, it should declare:

- which `ViewFamilyId` is the source,
- which viewpoint members are actually in local use,
- and whether the omitted members are simply unused or are intentionally excluded because the local scope does not require them.

The local family must not speak as if it had imported the whole bundle while silently dropping inconvenient viewpoints.

#### E.17.1:14.2 - Local overlays vs new bundles

A local project often wants a small adaptation: one extra concern note, one narrower stakeholder emphasis, one local naming convention. `E.17.1` prefers explicit overlays or new editions over silent mutation.

A practical rule is:

- if the local project selects a subset or adds only didactic/publication material, keep the exact imported bundle edition unchanged and declare the local subset or annex; do not treat the overlay as bundle content;
- if the local project changes viewpoint membership or meaning, publish a new local bundle or a new edition.

This is how bundle reuse remains trustworthy across organizations.

#### E.17.1:14.3 - Multi-bundle coordination

Many real description families need more than one bundle, for example:

- one engineering viewpoint family,
- one safety or assurance family,
- and one governance or publication-oriented family.

In such cases, `E.17.1` expects the family to preserve the provenance of each exact member reference and resolved viewpoint episteme P rather than flattening everything into one unnamed `Sigma`. Cross-family correspondence names each participating exact `U.ViewpointRef` or resolved P together with its exact source bundle edition and `ViewFamilyId` provenance; the corresponding `VP.*` token may remain only as a readable designator.

#### E.17.1:14.4 - Engineering vs publication families

Some contexts need both engineering viewpoints and publication viewpoints. `E.17.1` permits both, but it does not allow one family id to erase the distinction. A family that imports both kinds must keep the namespaces and bundle origins explicit so that authors do not confuse *how the holon is being understood* with *how a publication face/form chooses to expose that understanding*.

### E.17.1:15 - Worked Bundle Families

#### E.17.1:15.1 - TEVB engineering family

A TEVB engineering bundle for holons may include exact `U.ViewpointRef` members such as:

- `ref(VP.Functional)`,
- `ref(VP.Procedural)`,
- `ref(VP.AllocationResponsibility)`,
- `ref(VP.ModuleInterface)`.

Each listed reference resolves the exact viewpoint episteme P designated by the `VP.*` token inside `ref(...)`. The important point is not the vocabulary alone. The bundle states that these viewpoints are intended to recur together for one engineering family of concerns. A later description family then imports that exact engineering bundle edition and its needed references rather than re-inventing a local list of "roughly similar" viewpoints.

#### E.17.1:15.2 - Governance and risk family

A governance bundle may group exact `U.ViewpointRef` members such as:

- `ref(VP.Risk)`,
- `ref(VP.Control)`,
- `ref(VP.Compliance)`,
- `ref(VP.Operations)`.

Each listed reference resolves the exact viewpoint episteme P designated by the `VP.*` token inside `ref(...)`. This bundle is valuable precisely because the four viewpoints recur together but are not interchangeable. Keeping their exact references in one family edition makes the reuse visible while preserving each member's distinct meaning.

#### E.17.1:15.3 - Research-method family

A research-method bundle may include exact `U.ViewpointRef` members such as:

- `ref(VP.Theory)`,
- `ref(VP.Experiment)`,
- `ref(VP.Inference)`,
- `ref(VP.Limitations)`,
- and, where appropriate, `ref(VP.Reproducibility)`.

Each listed reference resolves the exact viewpoint episteme P designated by the `VP.*` token inside `ref(...)`. A local inquiry note might import only three exact references, but the import remains legible because the omitted members still belong to one reviewed source bundle edition rather than disappearing into ad hoc prose.

#### E.17.1:15.4 - Cross-family description relation positions

A serious project may use TEVB engineering viewpoints for the design family, a governance bundle for program oversight, and a publication-oriented family for public publication faces and publication forms. `E.17.1` keeps these relation positions reviewable by preserving which bundle each viewpoint came from and by preventing the final publication face or publication form from masquerading as the viewpoint library itself.

### E.17.1:16 - Authoring and Review Guidance

#### E.17.1:16.1 - For bundle authors

Bundle authors should ask:

- what recurring family is being named,
- which viewpoints truly belong together in that family,
- what local didactic publications or examples belong in annexes instead of the bundle core,
- and whether the bundle is stable enough to deserve a reusable `ViewFamilyId`.

A good bundle is not maximal. It is coherent, reviewable, and reusable.

#### E.17.1:16.2 - For reviewers

Reviewers should inspect both levels:

- **member level** - are the included viewpoints individually explicit enough to be reused?
- **bundle level** - do they actually form one coherent family rather than one convenient list?

They should also check whether a local project has silently forked the bundle while still using the inherited family id.

#### E.17.1:16.3 - For integrators and librarians

Integrators should keep libraries small, curated, and editioned. It is usually better to publish:

- one stable core bundle,
- one explicit local extension,
- and one clear subset declaration

than to let one giant family absorb every recurring viewpoint a domain has ever used. Library sprawl destroys the cognitive advantage that reusable bundles are supposed to provide.

### E.17.1:17 - Edition and Migration Notes

#### E.17.1:17.1 - Rename vs semantic change

A lexical rename that leaves viewpoint meaning and membership unchanged may be treated as a naming-layer migration. A change in membership, concern, admissibility, or member semantics is not just a rename; it requires a new edition or a new local bundle.

#### E.17.1:17.2 - Migration from local `Sigma` lists

Legacy `MultiViewDescribing` uses often publish only one local list of viewpoints. Migration should proceed by:

1. identifying recurring families across several such local lists,
2. publishing those families as explicit bundles,
3. then rewriting the local families to import the new `ViewFamilyId` and declare any subset selection explicitly.

This sequence preserves provenance and avoids pretending that the reusable family had always existed.

#### E.17.1:17.3 - Migration from publication-face/form-bound naming

If a legacy practice uses one label interchangeably for a viewpoint family, a viewpoint, a report section, and a publication face, migration separates those positions explicitly. `ViewFamilyId` remains at the bundle layer; exact `U.ViewpointRef` values resolve P while any `ViewpointId` is only P's designator; publication-face names remain publication-layer vocabulary.

#### E.17.1:17.4 - Boundary to annex growth

Annex manifests are useful, but a bundle should not become a thin shell hiding all of its meaning elsewhere. The core bundle still needs enough explicit member and family structure to stand on its own. Annexes deepen reuse; they do not replace the bundle's primary declaration.
### E.17.1:18 - Import Collision and Alias Discipline

#### E.17.1:18.1 - Family id is not a synonym bag
A `ViewFamilyId` does not mean that all member viewpoints are interchangeable labels for one concern. It means that a reviewed family of viewpoints is intended to recur together. Authors should therefore resist the common drift where one convenient bundle name begins to substitute for all of its members.

#### E.17.1:18.2 - Import collision rule
When two imported bundles contribute viewpoints with overlapping lexical names, the publication should preserve the originating viewpoint ids and bundle provenance rather than silently merging the members. Bundle reuse is admissible only if collisions remain inspectable.

#### E.17.1:18.3 - Alias boundary
Local teaching aliases may be added for readability, but the alias must dock to explicit member viewpoints and must not erase bundle provenance. If the alias starts doing bundle-selection work by itself, it is making an unsupported bundle-selection claim and should be replaced by explicit member references.

### E.17.1:19 - Bundle Projection and Comparative Use

#### E.17.1:19.1 - Projection to local subsets
A description family may project only a subset of a reusable bundle. This is admissible if the omitted members remain visible as omitted rather than disappearing into an ad hoc local list. Projection keeps bundle provenance intact while acknowledging that local publication rarely uses every member.

#### E.17.1:19.2 - Comparative bundle use
Bundles may be compared across contexts only if the comparison preserves member ids, member meanings, and subset/projection decisions. Comparing two bundle labels alone is not enough, because similarly named families may contain materially different viewpoint sets.

#### E.17.1:19.3 - Boundary to publication-face design
A publication face may render one composite presentation of several viewpoints, but the face is not the bundle. `E.17.1` therefore requires the underlying member structure to remain recoverable even when a public-facing document flattens it for readability.

### E.17.1:20 - Review Matrix and Library Governance

A reviewer can test a viewpoint bundle library with five questions:

1. **Do the member viewpoints still have explicit standalone meaning?**
2. **Does the bundle name describe one coherent recurring family rather than one convenience list?**
3. **If a subset is imported, is the omitted remainder still visible as omission rather than silent deletion?**
4. **If several bundles interact, is provenance preserved across collisions and local aliases?**
5. **Has a publication face started impersonating the library itself?**

Library governance should therefore prefer small, editioned, provenance-preserving bundles over lexical mega-families that are easy to name but hard to reuse truthfully.
### E.17.1:End

