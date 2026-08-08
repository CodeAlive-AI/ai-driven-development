## A.16.0 - `U.LanguageStateMoveTrajectory` - Optional trajectory-account normal form over the language-state `U.CharacteristicSpace`

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state move trajectory.

**Builds on.**
`C.2.2a`, `A.16`, `A.19`, `E.17`, `E.18`, `E.10`, `F.18`.

**Used by.**
`A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`, `A.6.P`, `C.16.Q`, `A.6.A`, `F.9.1`, `E.17.1`.

**Use this when.** Use this pattern when one local language-state move is no longer enough because a reviewable history must keep episteme editions, publication forms, branches, retirements, or losses visible, or because an actual responsibility handoff depends on that history.

**What goes wrong if missed.** Readers treat cue packs, routed cue sets, endpoint-bound publications, and next-use dockings as one thing magically moving; forks, losses, authority changes, and work-requiring crossings become implicit, and an actual responsibility change may be mistaken for semantic docking.

**What this buys.** One optional trajectory account that records lineage, position claims, move kinds, publication forms, losses, and the next use and authority boundary without wrapping every local `A.16` move in heavy history machinery.

### A.16.0:1 - Problem frame
In engineering, inquiry, operator, and management practice, teams sometimes need more than a local move note. When branch structure, supersession, retirement, bridge-sensitive loss, a multi-step change in the applicable rule, or an actual responsibility handoff whose legitimacy depends on upstream history matters, readers need one place that identifies the episteme editions, publication forms, and links involved.

Cue packs, routed cue sets, abductive prompts, typed route-bounded projection forms, partial normal forms, and endpoint-bound records may appear in that history as publication forms or published records. They are not the disturbances, telemetry traces, model outputs, bodily tensions, or carrier documents that ground it.

The account must not pretend that one unchanged episteme or publication literally moves. It records the selected episteme edition at each load-bearing step, the form and publication occurrence when availability matters, and links to successor editions when claims change.

### A.16.0:2 - Problem
Without an explicit trajectory-account pattern for those heavier cases:

1. history is mistaken for a generic one-pass process story rather than read as typed language-state moves over a declared `U.CharacteristicSpace`;
2. an early seam form is confused with an endpoint-admitted episteme or with the publication occurrence that makes an episteme edition available;
3. forks, merges, route retirement, supersession, and route-sensitive loss become implicit and unverifiable;
4. every local move is either over-wrapped in ad hoc history prose or under-described in a way that hides a work boundary or a separately established responsibility or authority change;
5. bridge and viewpoint docking inherit under-described upstream history.

### A.16.0:3 - Forces
| Force | Tension |
| --- | --- |
| **History value vs wrapper inflation** | Publish lineage only when it matters, without making trajectory accounts mandatory around every admissible move. |
| **Lineage fidelity vs readable publication** | Trajectory history must stay branch-aware without becoming unreadable bookkeeping. |
| **Seam usefulness vs endpoint discipline** | Upstream publications must be useful while remaining visibly upstream of endpoint admission. |
| **Account clarity vs neighboring rules** | The trajectory account must explain heavy-history cases without taking over the position, move, publication, path, or endpoint rules. |
| **Local move lineage vs bridge entry** | A trajectory may later cross viewpoint or context boundaries, but that crossing does not redefine its move or lineage semantics. |

### A.16.0:4 - Solution
`U.LanguageStateMoveTrajectory` is the **optional** trajectory-account normal form for a load-bearing history across positions in the language-state `U.CharacteristicSpace` named in `C.2.2a`. It records selected episteme editions, links among changed editions, typed moves, publication forms, and any availability occurrence that matters.

It does **not** define position semantics, move admissibility, publication forms, or path-publication semantics. Use `C.2.2a` and `A.19` for positions, `A.16` for moves, `E.24.PUB` for publication availability, and `E.17` or `E.18` for face and path publication.

It answers the question: `when the history matters, which episteme edition is current, what precedes or branches from it, which moves and links connect the entries, how is each edition published when availability matters, what was lost, and which rule or use applies next?`

#### A.16.0:4.0a - E.24.UK settlement

`U.LanguageStateMoveTrajectory` is retained as a dependent durable trajectory-account U-kind under the language-state settlement, not as a root U-kind. Its identity depends on the selected episteme editions, the declared `U.CharacteristicSpace` from `C.2.2a`, the typed move and lineage links, and any publication occurrence that is load-bearing for the account. An ordinary local history, route note, or publication form does not become `U.LanguageStateMoveTrajectory` by resemblance.

#### A.16.0:4.1 - Keep the account positions distinct
Keep seven positions distinct:

- **selected episteme edition** - the current `U.Episteme` whose claims are being positioned or re-expressed;
- **lineage links** - explicit `derivedFrom`, `supersedes`, `forkedFrom`, `mergedFrom`, and retirement or no-successor links among episteme editions when the claims change;
- **grounds or witnesses** - disturbances, discrepancies, traces, model outputs, bodily tensions, contrasts, or exemplars that justify the history;
- **publication form** - a cue pack, routed cue set, prompt form, typed route-bounded projection form, partial normal form, or endpoint-bound record used to express an edition;
- **publication occurrence** - an `EpistemePublicationRelation` occurrence only when availability to an audience for a bounded use matters;
- **publication face** - the MVPK face on which a form is rendered when face typing matters;
- **carrier** - the document, console note, card, trace file, model output, or other entity that bears the form.

A form, face, carrier, or publication-occurrence change can leave the selected episteme edition unchanged. A changed claim discriminator identifies another episteme edition. Publication alone creates neither the edition nor a lineage link.

Several live routes for one selected edition are **not** yet a lineage fork. A fork requires separately identified successor editions with explicit links, authority, and losses; publishing the same edition through two forms is not enough.

A trajectory step may reuse one edition in another form, add a successor edition, or relate several editions through fork, merge, supersession, or retirement. It does **not** mean that the source phenomenon moved through the language-state chart.

Here `route` names an `A.16` move-family label or a typed upstream publication-form cue. It is not an action route, work sequence, workflow, or transformation-flow path.

#### A.16.0:4.2 - Position-account discipline
The position read by this pattern is the slot-explicit claim defined in `C.2.2a`: a partial coordinate publication in the declared language-state `U.CharacteristicSpace`, where each basis slot publishes a `ValueSet(slot)`, interval, or other admissible set-valued claim.

Early seam publications may leave some slots unknown or wide. That uncertainty is admissible only if it is explicit. A trajectory account therefore records the position claim for the current episteme edition and, when needed, for predecessor or sibling editions that justify the move reading.

#### A.16.0:4.3 - Use threshold and core trajectory record
A single local `A.16` move note is sufficient when no load-bearing branch, loss, or supersession structure needs publication and no actual responsibility handoff depends on upstream history.

Use `U.LanguageStateMoveTrajectory` when at least one of the following is load-bearing:

- derivation, supersession, fork, merge, or retirement structure;
- multi-step loss notes or reopen conditions that would be hidden by a compressed move note;
- an actual responsibility handoff whose legitimacy or interpretation depends on upstream history;
- bridge or viewpoint entry that depends on upstream route, loss, or lineage structure.

A conforming trajectory account then keeps at least the following explicit:

- the current selected episteme edition;
- predecessor, sibling, or ancestor editions when the current reading depends on lineage;
- the lineage link kind (`derivedFrom`, `supersedes`, `forkedFrom`, `mergedFrom`, `retiredWithSuccessor`, `retiredWithoutSuccessor`, or another explicitly typed link);
- the current position claim and any load-bearing predecessor position claims;
- the typed move or move sequence;
- the publication form and, when availability matters, the publication occurrence;
- the MVPK face only when rendering matters;
- the next question or use, the applicable pattern, and its concrete contribution;
- when an actual responsibility handoff is load-bearing, the separate participants, relation, object or action, scope, interval, and instituting-act references required by `A.16.0:4.6`;
- any loss note, reopen condition, branch-specific authority note, or bridge-sensitive note that matters.

#### A.16.0:4.4 - Recorded move-family discipline
`U.LanguageStateMoveTrajectory` records the `A.16` move family: `notice`, `stabilize`, `route`, `projection`, `formalize`, `operationalize`, `reopen`, `sketchBackoff`, `respecify`, and `retire`.

Not every account uses every move. Forward movement, retreat, reframing, and explicit retirement belong to one family defined in `A.16` when that history is worth publishing.

`A.16` defines the detailed move guards. `A.16.0` records the moves and their satisfied guards; it does not replace them.

#### A.16.0:4.5 - Seam publication and face discipline
A trajectory account may refer to seam publication forms that remain upstream of endpoint admission. In the current cluster these include:

- `U.PreArticulationCuePack`;
- `RoutedCueSet`;
- `U.AbductivePrompt`;
- partial normal forms already typed elsewhere;
- other explicitly typed upstream publications that preserve a non-endpoint position.

These are not a rival publication-face sequence. They are typed publication forms rendered, when necessary, on existing MVPK faces under `E.17`.

Untyped placeholders such as "route-bounded publication face" are non-conformant in a trajectory account unless the text also names the actual publication form and, separately, the MVPK face if face typing matters.

#### A.16.0:4.6 - Endpoint docking and next use
A trajectory does not need to terminate to be useful. What matters is a visible docking milestone to the next pattern-based question or later use.

Typical next-use patterns include:

- `A.6.P` for relation precision or repair;
- `A.6.A` for an action invitation;
- `C.16.Q` for evaluative precision or repair;
- `B.5.2` for abductive inquiry;
- `A.15` for method-facing or work-facing planning;
- `C.25` for endpoint bundle structure.

Name the next pattern and what its content defines, constrains, or tests. The account already identifies the selected episteme edition; add a project record, particular publication form, or publication occurrence only when that distinction changes the next use. This is next-use docking, not a transfer of responsibility, and a pattern reference alone does not prove endpoint admission.

**Separate responsibility-handoff branch.** Open this branch only when responsibility, commitment, permission, or authority actually changes. Name the giving and receiving admitted systems and, when roles are relevant, the exact role assignments through which they participate; the exact relation before and after the change under its applicable pattern; the governed object or action, scope, and effective interval; and any assigning, instituting, revoking, or superseding act that the relation requires. The trajectory account cites that relation and its history; episteme lineage, publication form, publication occurrence, endpoint admission, and next-use docking neither create nor prove it.

After docking to a next use, monitoring, maintenance, revisit, or later re-entry may continue through new lineage entries or later trajectories. Keep lineage continuity separate from the current endpoint use and from any separately established responsibility or authority relation.

#### A.16.0:4.7 - Effect-free moves versus work-requiring crossings
Some `formalize` and `operationalize` steps are effect-free epistemic changes: rewriting, slot-explicit articulation, route-bounded partialization, view retargeting, or normal-form repair over already available grounds.

Other steps require new measurements, experiments, instrumentation, execution, or other `U.Work`. When that happens, the trajectory account shall expose the work-boundary crossing instead of pretending that world-facing work occurred inside the language layer. The account records why the crossing was required; use the relevant work, gate, or endpoint pattern to describe or test the world step. Add a particular Work, assertion, or `ClaimGraph` identity only when the claim or later reliance depends on it.

A work-boundary crossing does not by itself transfer responsibility or authority. If a separate actual responsibility handoff occurs, use the triggered branch in `A.16.0:4.6` and keep its relation distinct from the Work, episteme lineage, publication, and endpoint use.

#### A.16.0:4.8 - Relation to `A.16` and `E.18`
`U.LanguageStateMoveTrajectory` is not an `E.18` path publication, and `A.16.0` does **not** define language-state move semantics.

- `A.19` and `C.2.2a` define the declared characteristic-space reading of positions;
- `A.16` defines move kinds and guards;
- `E.17` and `E.18` define publication-face discipline and graph publication of paths;
- endpoint patterns define, constrain, or test endpoint-local claims and uses;
- `E.24.PUB` distinguishes the selected episteme edition, publication form, carrier, bounded use, and any publication occurrence that matters.

`A.16.0` standardizes only the heavier history package for cases where that history is itself worth publication.

The word `move` remains inherited from `A.16` and means a typed language-state publication transition. `A.16.0` does not generalize it into project action, work-entry readiness, pattern-use recommendation, performed work, work plan, workflow, or transformation-flow path. If source wording uses move-like language outside this scope, restore the concern through `E.10.MOVE` before selecting `E.11.PUR`, `A.15.5`, the A.15 work family, or another applicable pattern.

#### A.16.0:4.9 - Bridge and viewpoint entry
A trajectory may later cross a viewpoint or context boundary. When that happens:

- bridge substitution licence remains with `F.9`;
- stance overlays remain with `F.9.1`;
- viewpoint reuse remains with `E.17.1`;
- endpoint-local semantics remain in the rules defined or tested by the named endpoint patterns; publication availability remains a separate `E.24.PUB` relation.

`A.16.0` only makes those entry points explicit so that later attachments do not float without an upstream history account.

### A.16.0:5 - Archetypal Grounding
**Tell.** A language-state trajectory account is not `we kept refining the note`. It is an optional, lineage-aware account of episteme editions and their publication history, with declared position claims, move kinds, losses, and the next applicable pattern or use.

**Show (System).** A service disturbance is a system-side phenomenon, not a trajectory lineage member. It grounds an alerting episteme lineage. One stabilized cue pack may first keep two routes live in one `RoutedCueSet`; only later, if distinct successor episteme editions are constituted and published, does the lineage fork.

**Show (Episteme).** A model-vs-observation discrepancy is a witness-lane tension, not the positioned episteme edition or its lineage. Once the discrepancy is preserved in a cue pack, one branch may express the selected edition in a typed prompt form and later formalize it; if the claims change, identify a successor edition. Another branch may reopen or retire if the provisional route proves unsupported.

### A.16.0:6 - Bias-Annotation
The pattern biases authors toward lineage-aware history accounts rather than stage stories about one magically maturing episteme or publication. That bias is intentional when branch, loss, next-use, actual responsibility, or authority semantics matter. The counter-bias is equally intentional: do **not** publish a trajectory account when a local move note already suffices.

### A.16.0:7 - Conformance Checklist
- `CC-A.16.0-1` `U.LanguageStateMoveTrajectory` **SHALL NOT** be treated as mandatory wrapper syntax around every `A.16` move.
- `CC-A.16.0-2` A language-state trajectory account **SHALL** identify the current selected episteme edition and **SHALL NOT** collapse it with grounds, publication form, publication occurrence, face, or carrier.
- `CC-A.16.0-3` Position claims used in the trajectory **SHALL** be published as slot-explicit claims in the declared language-state `U.CharacteristicSpace`, not as folk stage labels.
- `CC-A.16.0-4` Fork, merge, supersession, derivation, and retirement **SHALL** be made explicit whenever the account depends on them.
- `CC-A.16.0-5` Publication form and MVPK face **SHALL NOT** be collapsed, and untyped seam placeholders **SHALL NOT** substitute for typed publication forms.
- `CC-A.16.0-6` `projection` **SHALL** be read as route-bounded partialization with visible loss notes and an admissible reopen condition.
- `CC-A.16.0-7` Work-requiring `formalize` or `operationalize` steps **SHALL** expose the work-boundary crossing rather than pretending that `U.Work` occurred inside the language layer; they **SHALL NOT** call that crossing a responsibility handoff unless the separate `A.16.0:4.6` branch is satisfied.
- `CC-A.16.0-8` When graph publication of paths is needed, authors **SHOULD** reuse `E.18` rather than inventing a rival path calculus here.

### A.16.0:8 - Common Anti-Patterns and How to Avoid Them
- **Meta-wrapper inflation.** Treat `A.16.0` as obligatory around every move. Repair by publishing a local `A.16` move note unless a later use depends on the history.
- **One-publication myth.** Treat one frozen episteme as literally moving unchanged. Repair by publishing lineage members and their links.
- **Pattern and form collapse.** Treat a pattern reference as if it were a publication form. Repair by naming the form and the cited pattern's concrete definition, constraint, or test separately.
- **Form and face collapse.** Treat seam publications as if they minted a second MVPK face family. Repair by naming form and face separately.
- **Multi-route and fork collapse.** Treat several live routes for one selected episteme edition as if they were already several successor editions.
- **Hidden work crossing or invented responsibility handoff.** Do not describe operationalization as purely linguistic when it required new world-facing work, and do not treat that crossing or next-use docking as a responsibility transfer. Publish the work boundary; open the separate `A.16.0:4.6` branch only for an actual responsibility, commitment, permission, or authority change.

### A.16.0:9 - Consequences
The benefit is that heavy-history language-state movement becomes lineage-aware, reviewable, and dockable without premature endpoint capture or metonymic collapse. The trade-off is more explicit publication of position claims, lineage links, move kinds, loss notes, next-use docking, and any actual responsibility handoff when history is worth publishing.

### A.16.0:10 - Rationale
Language-state work needs one trajectory-account normal form for the subset of cases where history itself matters. Without it, readers have to reconstruct lineage, branch structure, retirement, next-use docking, and any actual responsibility handoff from fragments. With it overused, every local move becomes over-wrapped. The pattern exists to hold the middle line.

### A.16.0:11 - SoTA-Echoing
The pattern matches contemporary practice in exploratory inquiry, operator-centered incident work, model probing, and structured design iteration: admissible progress sometimes requires visible intermediate publications, branch-aware history, disciplined retreat, explicit next-use docking, and—where it actually occurs—a separately established responsibility handoff rather than a hidden jump from cue to endpoint.

### A.16.0:12 - Relations
- Builds on: `C.2.2a`, `A.16`, `A.19`, `E.17`, `E.18`.
- Coordinates with: `C.2.LS`, `A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`, `B.5.2`, `A.6.P`, `C.16.Q`, `A.6.A`, `F.9`, `F.9.1`, `E.17.1`, and `E.10.MOVE` when move-like wording is not a language-state trajectory-account claim.
- Constrains: trajectory-account publication, branch visibility, seam publication reading, docking visibility, and anti-pipeline language across the cluster.

### A.16.0:13 - Worked trajectories

#### A.16.0:13.1 - Multi-route state before fork
A routed operator cue may first keep intervention and inquiry routes live for one selected episteme edition in one `RoutedCueSet`. That is still a multi-route state. Only if distinct successor editions are later constituted, linked, and published does the lineage fork.

#### A.16.0:13.2 - Inquiry trajectory with fork
An inquiry cue pack centered on a felt or trace-anchored discrepancy cue may first identify one selected episteme edition, then fork into:

- `notice -> stabilize -> route -> projection -> formalize`, with a cue-derived prompt form expressing the explanatory branch, and
- `notice -> stabilize -> route -> projection -> operationalize`

if one branch supports explanatory work while another supports immediate probe or control work. The fork remains admissible only if the successor editions and links are visible and each branch keeps distinct loss notes and next-use conditions. If responsibility actually changes, keep the separately established responsibility-handoff conditions distinct as well.

#### A.16.0:13.3 - Operator trajectory with retirement
An operator alert note about a service disturbance may move:

`notice -> stabilize -> route -> projection -> operationalize`

If later evidence no longer supports one route, the admissible continuation may include explicit retirement of that branch rather than silent disappearance. The retirement does not erase the prior branch; it withdraws authority and preserves continuity explicitly.

#### A.16.0:13.4 - Bridge-sensitive trajectory
A route-bearing comparative note may move through a seam publication and only later dock to a bridge overlay or viewpoint bundle. The bridge or viewpoint attachment does not replace the trajectory account; it annotates or re-expresses a lineage that already exists.

### A.16.0:14 - Trajectory publication package discipline
A publishable trajectory account should normally identify:

- the current selected episteme edition;
- predecessor, sibling, or ancestor editions when they are load-bearing;
- the lineage link kind;
- the current position claim and any load-bearing predecessor position claims;
- the move or move sequence;
- the publication form and, when availability matters, the publication occurrence;
- the MVPK face only when rendering matters;
- the grounds or witnesses that make the history necessary;
- the next route, docking pattern and contribution, or retirement state;
- the losses, open rivals, or reopen conditions that matter for continuation.

If these are missing, the publication is usually only plain sequence prose, not a conforming trajectory account.

### A.16.0:15 - Practitioner check
A practitioner should ask:

1. Is the author describing history over the declared language-state `U.CharacteristicSpace`, or only narrating progress informally?
2. Is the selected episteme edition distinct from the grounds, publication form, occurrence, face, and carrier?
3. Is this history heavy enough to justify `A.16.0`, or would a local `A.16` move note have sufficed?
4. Are multi-route state and lineage fork being kept distinct?
5. Are derivation, supersession, fork, merge, or retirement links visible where the reading depends on them?
6. Does the current claim concern an episteme edition, a seam or endpoint publication form, or—when bounded availability matters—an `EpistemePublicationRelation` occurrence? Are those positions kept separate, and is the endpoint test named?
7. If `formalize` or `operationalize` required world-facing work, is the work-boundary crossing explicit? If responsibility, commitment, permission, or authority also changed, are its participants, exact relation, object or action, scope, interval, and required instituting act stated separately?

### A.16.0:16 - Boundary notes
`A.16.0` does not replace `C.2.2a` / `A.19` position semantics, `A.16` move guards, `A.16.1` cue-pack semantics, `A.16.2` retreat / retirement semantics, `B.4.1` seam entry routing, `B.5.2.0` abductive prompt species, `E.17` face typing, `E.18` path publication, or any endpoint-local repair logic.

Its job is narrower: publish one intelligible history package where lineage, branch, loss, retreat, retirement, next-use docking, or a separately established responsibility handoff is load-bearing. It does not turn those different relations into one handoff relation.
### A.16.0:End

