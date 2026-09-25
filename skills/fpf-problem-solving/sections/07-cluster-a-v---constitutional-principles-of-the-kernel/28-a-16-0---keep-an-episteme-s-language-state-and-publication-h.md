## A.16.0 - Keep an Episteme's Language-State and Publication History Recoverable

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Technical alias.** `LanguageStateMoveTrajectory` names the optional history-account form described here. It is not an additional U-kind or an identity rule for the filled account.

**Builds on.**
`C.2.1`, `C.2.2a`, `A.16`, `A.19`, `E.24.PUB`, `E.17`, `E.10`, `F.18`.

**Used by.**
`A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`, `A.6.P`, `C.16.Q`, `A.6.A`, `F.9.1`, `E.17.1`.

**Use this when.** Use this pattern when one local language-state move is no longer enough because a reviewable history must keep episteme editions, publication forms, branches, retirements, or losses visible, or because an actual responsibility handoff depends on that history.

**What goes wrong if missed.** Readers treat cue packs, routed cue sets, endpoint-bound publications, and next-use dockings as successive states of one unchanged episteme; forks, losses, authority changes, and work-requiring crossings become implicit, and an actual responsibility change may be mistaken for semantic docking.

**What this buys.** One optional trajectory account that records lineage, position claims, move kinds, publication forms, losses, and the next use and authority boundary without wrapping every local `A.16` move in heavy history machinery.

### A.16.0:1 - Problem frame
In engineering, inquiry, operator, and management practice, teams sometimes need more than a local move note. When branch structure, supersession, retirement, bridge-sensitive loss, a multi-step change in the applicable rule, or an actual responsibility handoff whose legitimacy depends on upstream history matters, readers need one place that identifies the episteme editions, publication forms, and links involved.

Cue packs, routed cue sets, abductive prompts, typed route-bounded projection forms, partial normal forms, and endpoint-bound records may appear in that history as publication forms or published records. They are not the disturbances, telemetry traces, model outputs, bodily tensions, or carrier documents that ground it.

The trajectory account records the selected episteme edition at each load-bearing step, the form and publication occurrence when availability matters, and independently established lineage links among distinct epistemes when claims change.

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
`LanguageStateMoveTrajectory` is an **optional account form** for history across positions in the language-state `U.CharacteristicSpace` named in `C.2.2a`. A filled history account is an ordinary C.2.1 episteme when its claim content, EntityOfConcern and effective ReferenceScheme are identified. Its content can state selected source editions, independently obtaining lineage, typed moves, publication forms and any availability occurrence that matters.

It does not define position semantics, move admissibility, publication forms, or transformation-flow structure. Use `C.2.2a` and `A.19` for positions, `A.16` for moves, `E.24.PUB` for publication availability, and `E.17` for publication faces. `E.18` applies only when the current subject is an independently selected TransformationFlowStructure; `E.18.2` describes that structure mathematically.

It answers the question: `when the history matters, which episteme edition is current, what precedes or branches from it, which moves and links connect the entries, how is each edition published when availability matters, what was lost, and which rule or use applies next?`

#### A.16.0:4.0a - Identify the account and its expression

1. **Apply the history threshold.** Keep a local A.16 move note when it answers the receiving question. Use the fuller account only when branch, loss, lineage or an actual responsibility history changes a later use.
2. **Identify the account's subject.** For a source-centred history, name the exact source episteme as EntityOfConcern and state the relevant edition and relation claims in the account's ClaimGraph. For a relation-centred account, identify the independently obtaining relation it concerns. A negative or unresolved lineage claim remains about an independently identified source or other subject; it creates no relation occurrence.
3. **Recover the relevant history claims.** Distinguish the source editions, position claims, actual lineage, moves, losses and next use needed here. Use their direct rules below. State an unknown link or a supported no-successor result explicitly rather than inventing continuity.
4. **Choose an adequate expression.** The `LanguageStateMoveTrajectory` form can express that account. Under E.24.PUB, publication form is a relation-defined participant meaning over an independently identified entity; using the form admits no subtype or second account individual. Recover its expression relation, carrier and any availability occurrence only when the receiving claim needs those distinctions.
5. **Return the history needed by the next use.** Make the relevant branch, loss, limit or responsibility fact recoverable. Stop when that use is supported; a further account of the account's own history is needed only if another receiving question requires it.

The filled account has its own C.2.1 identity. Described source editions, position claims, loss notes and relation facts contribute to its content; they are not additional identity fields. A source-history event and the account acquiring knowledge of that event are different changes. Changed account content identifies another episteme, with edition continuity asserted only when its own relation obtains.

Several unrelated sources displayed in one table do not become one history individual. A common carrier or form can support separately grounded accounts and expression claims. Each claimed E.24.PUB publication occurrence still concerns one exact selected episteme edition and one bounded use. Publishing a history account is also distinct from publishing each source edition that it describes.

#### A.16.0:4.1 - Keep the account positions distinct
Keep the account's own identity and publication distinct from these seven values described in its history:

- **selected episteme edition** - the current `U.Episteme` whose claims are being positioned or re-expressed;
- **lineage links** - independently established derivation, supersession, fork, merge or retirement relations among the selected epistemes, each under its defining predicate; state a no-successor result when that is the supported account;
- **grounds or witnesses** - disturbances, discrepancies, traces, model outputs, bodily tensions, contrasts, or exemplars that justify the history;
- **publication form** - a cue pack, routed cue set, prompt form, typed route-bounded projection form, partial normal form, or endpoint-bound record used to express an edition;
- **publication occurrence** - an `EpistemePublicationRelation` occurrence only when availability to an audience for a bounded use matters;
- **publication face** - the MVPK face on which a form is rendered when face typing matters;
- **carrier** - the document, console note, card, trace file, model output, or other entity that bears the form.

A form, face, carrier, or publication-occurrence change can leave the selected episteme unchanged. A changed C.2.1 discriminator identifies another episteme. Call it a continuing edition only when the exact C.2.1 EpistemeEditionRelation obtains; any other lineage claim requires its own defining predicate and obtaining facts. Publication alone creates neither the episteme nor a lineage link.

Several live routes for one selected edition are **not** yet a lineage fork. A fork claim requires independently identified successor epistemes and the obtaining lineage predicate under its direct rule. Disclose losses and any authority facts that the selected account or that rule actually needs; authority is not a universal extra fork participant. Publication of the successors is not a universal prerequisite, and two publications of the same edition create no fork.

A trajectory step may reuse one edition in another form, add a successor episteme, or relate several epistemes through fork, merge, supersession, or retirement. It does **not** describe a trajectory of the source phenomenon.

Here `route` names an `A.16` move-family label or a typed upstream publication-form cue. It is not an action route, work sequence, workflow, or transformation-flow path.

#### A.16.0:4.2 - Position-account discipline
The position read by this pattern is the slot-explicit claim defined in `C.2.2a`: a partial coordinate publication in the declared language-state `U.CharacteristicSpace`, where each basis-slot reading is published as a `ValueSet(slot)`, interval, or other admissible set-valued claim.

Early seam publications may leave some slots unknown or wide. That uncertainty is admissible only if it is explicit. A trajectory account therefore records the position claim for the current episteme edition and, when needed, for predecessor or sibling editions that justify the move reading.

#### A.16.0:4.3 - Use threshold and core trajectory record
A single local `A.16` move note is sufficient when no load-bearing branch, loss, or supersession structure needs publication and no actual responsibility handoff depends on upstream history. An existing version history can also supply the answer when the needed source-use, continuity and loss facts are already recoverable there; the form does not require copying them into another document.

Use the `LanguageStateMoveTrajectory` account form when at least one of the following changes the receiving use:

- derivation, supersession, fork, merge, or retirement structure;
- multi-step loss notes or reopen conditions that would be hidden by a compressed move note;
- an actual responsibility handoff whose legitimacy or interpretation depends on upstream history;
- bridge or viewpoint entry that depends on upstream route, loss, or lineage structure.

An account using this form identifies its own subject, claim content and effective ReferenceScheme. It makes the following history content explicit to the extent needed by the selected use:

- the current selected episteme edition;
- predecessor, sibling, or ancestor editions when the current reading depends on lineage;
- the lineage link kind (`derivedFrom`, `supersedes`, `forkedFrom`, `mergedFrom`, `retiredWithSuccessor`, `retiredWithoutSuccessor`, or another explicitly typed link);
- the current position claim and any load-bearing predecessor position claims;
- the typed move or move sequence;
- the publication form and, when availability matters, the publication occurrence;
- the MVPK face only when rendering matters;
- the next question or use, the applicable pattern, and its concrete contribution;
- when an actual responsibility handoff is load-bearing, the separate participants, relation, object or action, scope, interval, and instituting-act references required by `A.16.0:4.6`;
- the grounds or witnesses and still-live rivals needed to justify the entries, with any loss note, reopen condition, branch-specific authority note or bridge-sensitive note that matters.

#### A.16.0:4.4 - Recorded move-family discipline
The `LanguageStateMoveTrajectory` account form records the `A.16` move family: `notice`, `stabilize`, `route`, `projection`, `formalize`, `operationalize`, `reopen`, `sketchBackoff`, `respecify`, and `retire`.

Not every account uses every move. Forward movement, retreat, reframing, and explicit retirement belong to one family defined in `A.16` when that history is worth publishing.

`A.16` defines the detailed move guards. `A.16.0` records the moves and their satisfied guards; it does not replace them.

#### A.16.0:4.5 - Seam publication and face discipline
A trajectory account may refer to seam publication forms that remain upstream of endpoint admission. In the current cluster these include:

- `PreArticulationCuePack`;
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
- `C.16.Q` for quality or evaluative-characterization wording repair;
- `B.5.2` for abductive inquiry;
- `A.15.2` for planning future Work, including its target Method;
- `C.25` for quality-family decomposition and Q-Bundle structure.

Name the next pattern and what its content defines, constrains, or tests. The account already identifies the selected episteme edition; add a project record, particular publication form, or publication occurrence only when that distinction changes the next use. This is next-use docking, not a transfer of responsibility, and a pattern reference alone does not prove endpoint admission.

**Separate responsibility-handoff branch.** Open this branch only when responsibility, commitment, permission, or authority actually changes. Name the exact relation before and after the change under its applicable pattern, then the participants in that relation's own roles. Include giving and receiving admitted systems when its predicate requires them and, when their system-role classification matters, the exact system-role kinds and assignments through which they participate. State its governed object or action, scope, effective interval, and any assigning, instituting, revoking, or superseding act that the relation requires. The trajectory account cites that relation and its history; episteme lineage, publication form, publication occurrence, endpoint admission, and next-use docking neither create nor prove it.

After docking to a next use, monitoring, maintenance, revisit, or later re-entry may continue through new lineage entries or later trajectories. Keep lineage continuity separate from the current endpoint use and from any separately established responsibility or authority relation.

#### A.16.0:4.7 - Re-expression and additional world-facing Work
Some `formalize` and `operationalize` steps re-express already available grounds through rewriting, slot-explicit articulation, route-bounded partialization, view retargeting, or normal-form repair. Performing those activities can itself be dated Work under A.15.1; the distinction here is whether new world-side measurements or interventions are needed.

Some steps additionally require new measurements, experiments, installation or use of instrumentation, execution, or other `U.Work`. When that happens, the trajectory account shall expose the work-boundary crossing. The account records why the crossing was required; use the relevant work, gate, or endpoint pattern to describe or test the world step. Add a particular Work, assertion, or `ClaimGraph` identity only when the claim or later reliance depends on it.

A work-boundary crossing does not by itself transfer responsibility or authority. If a separate actual responsibility handoff occurs, use the triggered branch in `A.16.0:4.6` and keep its relation distinct from the Work, episteme lineage, publication, and endpoint use.

#### A.16.0:4.8 - Relation to `A.16` and `E.18`
A language-state trajectory account does not by itself establish an E.18 TransformationFlowStructure, and A.16.0 does not define language-state move semantics.

- `A.19` and `C.2.2a` define the declared characteristic-space reading of positions;
- `A.16` defines move kinds and guards;
- `E.17` defines publication-face discipline; `E.18` governs an independently selected TransformationFlowStructure and `E.18.2` its mathematical description;
- endpoint patterns define, constrain, or test endpoint-local claims and uses;
- `E.24.PUB` distinguishes the selected episteme edition, publication form, carrier, bounded use, and any publication occurrence that matters.

`A.16.0` standardizes only the heavier history package for cases where that history is itself worth publication.

The word `move` remains inherited from `A.16` and means a typed language-state publication transition. `A.16.0` does not generalize it into project action, work-entry readiness, pattern-use recommendation, performed work, work plan, workflow, or transformation-flow path. If source wording uses move-like language outside this scope, restore the concern through `E.10.MOVE` before selecting `E.11.PUR`, `A.15.5`, the A.15 work family, or another applicable pattern.

#### A.16.0:4.9 - Bridge and viewpoint entry
A trajectory may later cross a viewpoint or context boundary. When that happens:

- the trajectory establishes neither an F.9 Bridge nor the suitability of any bounded cross-context use; exact relation and use claims remain with `F.9`;
- stance notes remain with `F.9.1`;
- viewpoint reuse remains with `E.17.1`;
- endpoint-local semantics remain in the rules defined or tested by the named endpoint patterns; publication availability remains a separate `E.24.PUB` relation.

`A.16.0` only makes those entry points explicit. It establishes no current reliance, authorization, or receiving use. When those questions are live, apply triggered `A.10` or `B.3` for reliance, the pattern that directly constrains the receiving action for authorization, and evidence of the receiving Work or publication for occurrence. No bundled record is required when those questions are not live.

### A.16.0:5 - Archetypal Grounding
**Tell.** A language-state trajectory account is not `we kept refining the note`. It is an optional, lineage-aware account of episteme editions and their publication history, with declared position claims, move kinds, losses, and the next applicable pattern or use.

**Show (System).** A service disturbance is a system-side phenomenon, not a trajectory lineage member. It grounds an alerting episteme lineage. One stabilized cue pack may first keep two routes live in one `RoutedCueSet`; record a fork only after distinct successor epistemes and their independently established fork links are identified.

**Show (Episteme).** A model-vs-observation discrepancy is a witness-lane tension, not the positioned episteme edition or its lineage. Once the discrepancy is preserved in a cue pack, one branch may express the selected edition in a typed prompt form and later formalize it; if the claims change, identify another episteme and assert continuation only when its exact relation obtains. Another branch may reopen or retire if the provisional route proves unsupported.

#### A.16.0:5.1 - Five identity and use cases

These are constructed distinctions. History account H1 has source episteme S0 as its exact EntityOfConcern, claims about S0's language-state history and an effective ReferenceScheme.

| Change or receiving question | Result |
|---|---|
| H1's unchanged claims are displayed in another arrangement or on another carrier. | H1 remains the same episteme. Recover the changed form, bearing or availability relation only when needed. |
| The author learns a new supported fact about S0's history and changes the account's claim content. | The resulting account H2 is another episteme. It is a continuing edition of H1 only if the C.2.1 edition relation obtains. Learning this fact did not itself change S0's history. |
| Independently identified S1 and S2 are successors of S0, and the actual historical facts satisfy the selected lineage rule's fork predicate; neither successor has been published. | The fork already obtains and can be described. Two different publications of S0 alone would not satisfy this case. |
| A route projection retains a conclusion but omits an assumption needed to reconstruct its applicability. | The loss note identifies that assumption and which receiving use can no longer recover it, retaining the supported content and stating the needed reopen condition. |
| Under an already defined review-responsibility rule, Ana is responsible for review case K until time t; an authorized instituting act G assigns that responsibility to Boris from t. | Cite the rule, both actual relations, their participants, review scope, time and instituting act. The history account reports this change. Language-state movement, a new form or next-use docking supplies none of those responsibility facts. |

For a question about whether S0 has a successor when the evidence is incomplete, keep S0 as the account's subject and state that unresolved claim. For a question about an actual independently identified lineage relation R, an account may instead have R as its subject. A table showing unrelated S0 and T0 does not supply a common history-object identity.

### A.16.0:6 - Bias-Annotation
The pattern biases authors toward lineage-aware history accounts rather than stage stories that conflate re-expression with changed claims. That bias is intentional when branch, loss, next-use, actual responsibility, or authority semantics matter. The counter-bias is equally intentional: do **not** publish a trajectory account when a local move note already suffices.

### A.16.0:7 - Conformance Checklist
- `CC-A.16.0-1` The `LanguageStateMoveTrajectory` account form **SHALL NOT** be treated as mandatory wrapper syntax around every `A.16` move or as an additional U-kind.
- `CC-A.16.0-2` Identify the account episteme through its own C.2.1 content, subject and scheme. Distinguish it from the source editions and relations it describes, and distinguish each selected publication edition from grounds, form, availability occurrence, face and carrier.
- `CC-A.16.0-3` Position claims used in the trajectory **SHALL** be published as slot-explicit claims in the declared language-state `U.CharacteristicSpace`, not as folk stage labels.
- `CC-A.16.0-4` State the independently obtaining fork, merge, supersession, derivation or retirement facts whenever the account depends on them. Preserve negative or unresolved claims without inventing a relation. Successor publication and generic authority are not universal fork requirements.
- `CC-A.16.0-5` Publication form and MVPK face **SHALL NOT** be collapsed, and untyped seam placeholders **SHALL NOT** substitute for typed publication forms.
- `CC-A.16.0-6` `projection` **SHALL** be read as route-bounded partialization with visible loss notes and an admissible reopen condition.
- `CC-A.16.0-7` Work-requiring `formalize` or `operationalize` steps **SHALL** expose the work-boundary crossing; they **SHALL NOT** call that crossing a responsibility handoff unless the separate `A.16.0:4.6` branch is satisfied.
- `CC-A.16.0-8` When the history is represented by an independently selected TransformationFlowStructure, authors **SHALL** apply E.18 to that structure and use E.18.2 when a mathematical description is needed. A graph rendering alone establishes neither subject.

### A.16.0:8 - Common Anti-Patterns and How to Avoid Them
- **Meta-wrapper inflation.** Treat `A.16.0` as obligatory around every move. Repair by publishing a local `A.16` move note unless a later use depends on the history.
- **One-publication myth.** Record a changed claim discriminator under the same episteme edition. Repair by identifying the different epistemes and only the lineage links whose predicates obtain.
- **Pattern and form collapse.** Treat a pattern reference as if it were a publication form. Repair by naming the form and the cited pattern's concrete definition, constraint, or test separately.
- **Form and face collapse.** Treat seam publications as if they minted a second MVPK face family. Repair by naming form and face separately.
- **Multi-route and fork collapse.** Treat several live routes for one selected episteme edition as if they were already several successor epistemes.
- **Hidden work crossing or invented responsibility handoff.** Do not describe operationalization as purely linguistic when it required new world-facing work, and do not treat that crossing or next-use docking as a responsibility transfer. Publish the work boundary; open the separate `A.16.0:4.6` branch only for an actual responsibility, commitment, permission, or authority change.

### A.16.0:9 - Consequences
The benefit is that heavy-history language-state movement becomes lineage-aware, reviewable, and dockable without premature endpoint capture or metonymic collapse. The trade-off is more explicit publication of position claims, lineage links, move kinds, loss notes, next-use docking, and any actual responsibility handoff when history is worth publishing.

### A.16.0:10 - Rationale
Language-state work needs one trajectory-account normal form for the subset of cases where history itself matters. Without it, readers have to reconstruct lineage, branch structure, retirement, next-use docking, and any actual responsibility handoff from fragments. With it overused, every local move becomes over-wrapped. The pattern exists to hold the middle line.

### A.16.0:11 - SoTA-Echoing

**Practice question.** What is the lightest history that lets a later reader recover which note supplied a claim, what changed or was lost, and how that affects the next use?

The selected line retains only the source and loss relations needed by that question. [W3C PROV-DM, Recommendation of 30 April 2013, §§2.2.1.2 and 5.2.1–5.2.2](https://www.w3.org/TR/2013/REC-prov-dm-20130430/), supplies the substantive provenance distinction: derivation connects an output to what it used, can be expanded when activity details matter, and is broader than revision. **Adapt** that selective detail in §§4.0a and 4.3. A PROV derivation or revision assertion supplies no automatic C.2.1 edition relation, truth warrant or language-state position; those claims still need their own facts and rules.

The serious alternative is ordinary version history with relevant diffs and change notes. *Pro Git*, second edition, [§2.3, Viewing the Commit History](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History), supplies a concrete implementation: patches expose textual changes and a graph exposes repository branches and merges. This is often sufficient and should be reused. Its limit for the present question is that a file parent or deletion does not by itself say which source claim was used, whether episteme continuity holds, or which omitted condition changes reliance.

For the same three notes in §14, both approaches can expose the missing restart window. The targeted history also makes two needed judgments explicit: S1 used S0 but failed the stated continuation rule; S2 returns directly to S0 and restores the observations and rivals needed by the diagnostic question. This requires no new incident observations. Its cost is a short semantic annotation after the same content comparison; its gain is that the next reader need not reconstruct why the capacity conclusion was withdrawn. **Reject** deriving those judgments solely from chronological adjacency or repository ancestry. When the existing change note already supplies them, §4.3 stops without another account.

The loss annotation has a separate practice basis. The *Site Reliability Workbook* (2018), [chapter 10, “Missing context” and “Key details omitted”](https://sre.google/workbook/postmortem-culture/), contrasts an inadequate incident account with one that retains the context and facts needed for learning and action. **Adopt** that action-changing-detail criterion in §4.3 and §14's restart-window loss. This is failure evidence for an unqualified summary, not a requirement to write a full postmortem or a source for FPF lineage identity. The selected history preserves an unresolved diagnostic question; it need not manufacture a settled cause or corrective action.

Reopen the choice of account when the receiving question needs an unrecorded branch, source use, lost condition or authority fact. If an existing note or diff annotation now makes all those facts recoverable, reuse it. If automated interchange becomes the actual need, compare an adequate structured provenance representation with this small human-readable account; prose alone may then cease to suffice.

### A.16.0:12 - Relations
- Builds on: `C.2.2a`, `A.16`, `A.19`, `E.17`.
- Coordinates with: `C.2.LS`, `A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`, `B.5.2`, `A.6.P`, `C.16.Q`, `A.6.A`, `F.9`, `F.9.1`, `E.17.1`, and `E.10.MOVE` when move-like wording is not a language-state trajectory-account claim.
- Constrains: trajectory-account publication, branch visibility, seam publication reading, docking visibility, and anti-pipeline language across the cluster.

### A.16.0:13 - Worked trajectories

#### A.16.0:13.1 - Multi-route state before fork
A routed operator cue may first keep intervention and inquiry routes live for one selected episteme edition in one `RoutedCueSet`. That is still a multi-route state. A lineage fork exists when independently identified distinct successor epistemes and the actual historical facts satisfy the selected fork predicate. Both successors may still be unpublished. Conversely, publishing the same edition twice creates two publication claims, not a fork.

#### A.16.0:13.2 - Inquiry trajectory with fork
An inquiry cue pack centered on a felt or trace-anchored discrepancy cue may first identify one selected episteme edition, then fork into:

- `notice -> stabilize -> route -> projection -> formalize`, with a cue-derived prompt form expressing the explanatory branch, and
- `notice -> stabilize -> route -> projection -> operationalize`

if one branch supports explanatory work while another supports immediate probe or control work. The account of that fork identifies the successor epistemes and obtaining lineage links, and discloses each branch's relevant losses and next-use conditions. These disclosures describe the fork; their publication does not create it. If responsibility actually changes, keep the separately established responsibility-handoff conditions distinct as well.

#### A.16.0:13.3 - Operator trajectory with retirement
An operator alert note about a service disturbance may move:

`notice -> stabilize -> route -> projection -> operationalize`

If later evidence no longer supports one route, the admissible continuation may include explicit retirement of that branch rather than silent disappearance. The retirement does not erase the prior branch; it ends the retired branch's current use and preserves continuity explicitly. Any authority change still requires the separate relation in §4.6.

#### A.16.0:13.4 - Bridge-sensitive trajectory
A route-bearing comparative note may move through a seam publication and only later dock to a bridge overlay or viewpoint bundle. The bridge or viewpoint attachment does not replace the trajectory account; it annotates or re-expresses a lineage that already exists.

### A.16.0:14 - Filled history: a restart incident loses its scope

This constructed incident concerns `CheckoutSystem-17`. All three notes below use `Incident17Scheme`, which fixes the System name, trace identifiers and time interpretation. History account H17 has source episteme S0 as its EntityOfConcern; the notes it describes have the checkout System as theirs.

The local incident-edition rule permits a note to continue S0 only if it actually uses S0, retains that System and scheme, preserves the reported observation window and observations, and explicitly marks any changed diagnosis or next question. It allows a diagnosis to be withdrawn or a question added; a scope-dropping summary fails the continuation condition. This is the applicable C.2.1 rule for this example, not a rule inferred from the filenames.

| Entry and source use | Content and position needed here | History result and receiving action |
|---|---|---|
| S0, the initial incident note, grounded in trace T17 | Three timeouts occurred during 09:00–09:02 after restart; the 09:04 request succeeded. Cold-cache startup and database-pool startup remain rival explanations. The named observations and rivals support `ValueSet(AE)={AE2}` and `ValueSet(CD)={CD2}` using the C.2.4/.5 starter anchors. | Preserve the time window, later success and both rivals for the diagnostic question. The note establishes no permanent capacity shortage. |
| S1, a briefing composed from S0 | “Checkout is permanently undersized; add replicas.” The explicit claim/action supports AE3; the selected capacity route is CD3. It omits both the restart window and the later success, and drops the rival explanations. | S1 has changed claim content and fails the stated edition-continuity rule. Record that failed continuation claim rather than silently linking it as the next valid edition. Its polish and closure establish no stronger warrant. |
| S2, a corrected note composed directly from S0 after S1's loss is found | Retains both observations and rivals; adds “Which explanation accounts for the restart-only timeouts, and what observation would distinguish them?” It withdraws the permanent-shortage conclusion. Its explicit diagnostic structure gives `ValueSet(AE)={AE3}`; restored rivals give `ValueSet(CD)={CD2}`. | C.2.1 continuation from S0 to S2 obtains: distinct content, actual source use, same System/scheme, retained observations and an explicitly changed question satisfy the stated rule. Do not infer continuation from S1. |

The A.16 `reopen` guard is met for the earlier capacity-route commitment: recovering S0 reveals the lost scope and unsupported elimination of rivals. The local next-use rule requires at least AE2, both named rivals and the observation window to be recoverable; it permits a return to B.5.2.0's diagnostic-question entry, not authorization to add replicas. S2 meets that guard. The receiving practitioner can now frame the discriminating inquiry while withholding the permanent-capacity conclusion. Any additional measurement is prospective Work under its own rule.

This short history is needed because the loss occurred between notes and changes how the later action proposal may be used. If the same facts and return were already recoverable in one adequate local move note, §4.3 would stop there. No successor publication, fork, responsibility transfer or history-of-H17 is required for this result.

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
`A.16.0` does not replace `C.2.2a` / `A.19` position semantics, `A.16` move guards, `A.16.1` cue-pack semantics, `A.16.2` retreat / retirement semantics, `B.4.1` seam entry routing, `B.5.2.0` abductive prompt species, `E.17` face typing, `E.18` selected transformation-flow structure, or any endpoint-local repair logic.

Its job is narrower: publish one intelligible history package where lineage, branch, loss, retreat, retirement, next-use docking, or a separately established responsibility handoff is load-bearing. It does not turn those different relations into one handoff relation.
### A.16.0:End
