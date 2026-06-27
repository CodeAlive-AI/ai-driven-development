## A.16.2 - Reopen / SketchBackoff / Respecify

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Admissible reopen / backoff / respecification.

### A.16.2:1 - Problem frame
A governed history across the language-state chart must support admissible retreat as well as tightening. When a route, publication form, or framing scaffold over-commits, teams need a first-class way to reopen, back off, respecify, or retire a branch without pretending nothing changed.

### A.16.2:2 - Problem
Without an explicit retreat pattern, teams treat reopening as failure, hide regressions, silently mutate endpoint-bound or route-bearing forms back into exploratory cue-bearing publication forms with no audit trail, or let obsolete branches disappear without any visible withdrawal note.

### A.16.2:3 - Forces
| Force | Tension |
|---|---|
| **Reversibility vs trust** | Allow backoff without making the trajectory discipline look arbitrary. |
| **Explicit retreat vs clutter** | Name retreat and retirement without drowning the model in bookkeeping. |
| **Witness retention vs honest revision** | Keep what remains valid while explicitly discarding what no longer holds. |
| **Framing revision vs repair-pattern boundary** | Allow route-specification or framing-scaffold revision without letting `A.16.2` swallow slot-explicit epistemic precision repair from governing patterns. |

### A.16.2:4 - Solution
This pattern defines the retreat, reframing, and retirement side of the `A.16` move family.

#### A.16.2:4.1 - Move family
| Move | When to use it | What remains stable | What may change |
|---|---|---|---|
| `reopen` | the current family is still right, but closure was over-committed | family and major orientation | closure, rival set, guards |
| `sketchBackoff` | the current publication form overstates articulation or stability | witnesses, traces, some anchors | publication form, articulation-explicitness value, route certainty |
| `respecify` | the family remains plausible, but the framing scaffold, route specification, or facet-profile reading is wrong | broad domain, witness base, and major family commitments | framing scaffold, route specification, facet-profile reading |
| `retire` | a cue, route-bearing publication, or branch is no longer current or no longer worth preserving | historical continuity and any cited witnesses that still matter | currentness, authority, successor/no-successor status |

`respecify` is intentionally narrower than epistemic precision repair. Slot-explicit epistemic precision restoration, bearer repair, or endpoint-local lexical precision remains with governing patterns such as `A.6.P`, `C.16.Q`, and `A.6.A`.

#### A.16.2:4.2 - Required publication note
Every retreat or retirement move shall name:

- source publication form,
- source articulation / closure / route-authority state,
- trigger or counter-evidence,
- target family or target publication form,
- retained witnesses,
- withdrawn assumptions, route claims, or authority,
- and whether a successor now exists or the branch is retired without successor.

#### A.16.2:4.3 - Authority discipline
A retreat or retirement move shall not silently preserve operational, gate, commitment, or route authority if the retreat target form no longer supports that authority.

### A.16.2:5 - Archetypal Grounding
**Tell.** Backoff is not regression; it is an admissible language-state move when the current publication form over-commits. Retirement is not erasure; it is admissible withdrawal when continuation no longer deserves current authority.

**Show (System).** A rollback cue may reopen a prior decision path instead of pretending the original operationalization still holds, or retire one branch once a better-supported successor line has taken over.

**Show (Episteme).** A formalized hypothesis may sketch-backoff to a cue pack when its framing collapses under new exemplars, or it may respecify its route specification while leaving slot-explicit epistemic precision repair to governing patterns.

### A.16.2:6 - Bias-Annotation
The pattern pushes against false linear progress narratives. The cost is that teams must expose when closure or route authority is being relaxed, reframed, or retired.

### A.16.2:7 - Conformance Checklist
- `CC-A.16.2-1` Retreat or retirement moves **SHALL** cite the trigger or counter-evidence that justifies them.
- `CC-A.16.2-2` A retreat or retirement move **SHALL NOT** silently preserve endpoint authority if the target form no longer supports it.
- `CC-A.16.2-3` Reopen / backoff / respecify / retire moves **SHOULD** preserve witnesses and trace links whenever still valid.
- `CC-A.16.2-4` The target articulation, closure, and route-authority state **SHALL** be explicit when the move substantively changes any of them.
- `CC-A.16.2-5` `respecify` **SHALL NOT** be used to smuggle slot-explicit epistemic precision repair out of governing patterns.

### A.16.2:8 - Common Anti-Patterns and How to Avoid Them
- **Shame-driven concealment.** Teams hide the retreat. Publish the move.
- **Silent downgrade.** The publication loses closure state, route authority state, or endpoint authority claim but no one updates the route or authority state.
- **Retreat as erasure.** Earlier witnesses disappear even though they remain valid.
- **Respecify as silent repair.** `respecify` is used to hide a real epistemic precision restoration that belongs to later repair governing patterns.
- **Silent branch disappearance.** A branch stops mattering, but no retirement or supersession note is published.

### A.16.2:9 - Consequences
The benefit is explicit reversibility, reframing, and retirement handling. The trade-off is more explicit transition records and more explicit governance notes.

### A.16.2:10 - Rationale
Language-state history is not one-way tightening. Without retreat and retirement discipline, `A.6.P` and endpoint forms would encode only one-way progress and would hide the real cost of over-commitment.

### A.16.2:11 - SoTA-Echoing
This fits iterative design, incident response, scientific reframing, embodied inquiry, and exploratory model work where recovery from over-commitment and honest branch retirement are part of competent practice.

### A.16.2:12 - Relations
- Builds on: `A.16`, `C.2.5`.
- Coordinates with: `C.2.2a`, `A.16.0`, `A.16.1`, `B.4.1`, `B.5.2`, `A.6.P`, `A.6.A`, `C.16.Q`.
- Constrains: admissible retreat, respecification, and retirement paths.

### A.16.2:13 - Worked Retreat Trajectories

#### A.16.2:13.1 - Reopen within the same family
A routed evaluative note may remain within the same family but move from high closure to lower closure when a rival frame reopens. This is `reopen`, not `sketchBackoff`.

#### A.16.2:13.2 - Sketch-backoff to cue pack
An over-specified `A.6.A`-governed invitation may later prove premature. The admissible retreat is:

`actionInvitation -> sketchBackoff -> U.PreArticulationCuePack`

with explicit withdrawal of route authority that no longer holds.

#### A.16.2:13.3 - Respecify without repair-pattern drift
A route-bearing publication may keep the same broad family but replace one framing scaffold or route specification with another. That is `respecify`, not silent editing, and not slot-explicit epistemic precision repair.

#### A.16.2:13.4 - Retire an obsolete branch
A route-bearing branch may later become obsolete because another branch now carries the governing pattern and witness support for the current use. The admissible continuation is explicit `retire`, not silent disappearance.

### A.16.2:14 - Authoring and Review Guidance

#### A.16.2:14.1 - Author prompt
A retreat or retirement note should say:

- what proved over-committed or no longer current,
- what remains valid,
- what authority is withdrawn,
- what publication form now becomes appropriate,
- and whether any successor carries the continuity forward.

#### A.16.2:14.2 - Review prompt
A reviewer should ensure that retreat does not become silent erasure. Valid witnesses should survive unless explicitly discarded with reason, and retired branches should either name a successor or say clearly that none exists.

#### A.16.2:14.3 - Boundary reminder
Retreat is an admissible move, not a rhetorical excuse to avoid publishing mistakes. The value of the pattern depends on making the retreat or retirement visible.

### A.16.2:15 - Migration Notes

#### A.16.2:15.1 - Migration from regression language
Older language often talks about "going backwards" or "regressing". The preferred migration is to name whether the change is reopen, sketch-backoff, respecify, or retire, and what boundary or authority consequence follows.

#### A.16.2:15.2 - Integration reminder
When retreat affects governing patterns such as `A.6.P`, `A.6.A`, `C.16.Q`, or `A.15`, those governing patterns should be updated explicitly rather than left to drift on stale authority.

### A.16.2:16 - Retreat Package Discipline

A retreat is trustworthy only when it makes visible what changed, what survived, and what authority no longer holds.

#### A.16.2:16.1 - Minimal retreat note
A retreat note should make explicit:

- the **source form and authority-reference relation state**,
- the **triggering mismatch or counter-evidence**,
- the **move kind**,
- the **target form or target family**,
- the **retained witnesses**,
- the **withdrawn assumptions or route claims**,
- the **required downstream updates** for any affected governing pattern,
- and the **successor / no-successor status** if a branch is retired.

#### A.16.2:16.2 - Retreat is not erasure
Retreat preserves continuity: a high-closure formulation or formulation with endpoint authority claim was adopted, then shown to over-commit in stated respects, and therefore backed off or withdrawn admissibly.

#### A.16.2:16.3 - Partial retreat
Some retreats withdraw only one route claim, scope assumption, framing scaffold, or operational hook. In those cases name the surviving core rather than resetting everything.

### A.16.2:17 - Retained vs Withdrawn Authority

#### A.16.2:17.1 - Reopen
`reopen` usually preserves the family and much of the surrounding structure while withdrawing closure. It reintroduces rival possibilities without claiming that the entire earlier publication was inadmissible.

#### A.16.2:17.2 - Sketch-backoff
`sketchBackoff` withdraws closure state, route authority state, or endpoint authority claim more sharply. It typically preserves witnesses, exemplars, or cue anchors while withdrawing the over-committing publication form and any authority that depended on that form.

#### A.16.2:17.3 - Respecify
`respecify` keeps the broad family but changes framing scaffold, route specification, or facet-profile reading. It is neither pure retreat nor silent edit: it preserves enough of the prior publication to justify continuity, but it does not authorize semantic slot repair that belongs to governing patterns.

#### A.16.2:17.4 - Retire
`retire` ends current authority for a cue, route-bearing publication, or branch while preserving historical continuity. It may point to a better-supported successor or explicitly state that no successor currently exists.

### A.16.2:18 - Worked Recovery Cases

#### A.16.2:18.1 - Reopening a routed evaluative note
An evaluative note may have reached a high closure state under one route, but new contrasts reopen a serious rival. `reopen` is admissible when the bearer, family, and witness base remain largely intact but the closure claim must be relaxed.

#### A.16.2:18.2 - Sketch-backoff from prompt to cue pack
An abductive prompt may later prove over-committed because its open question was formulated before the cue anchors had stabilized. The admissible recovery is to sketch-backoff to `U.PreArticulationCuePack`, preserving the cue carriers while withdrawing prompt authority.

#### A.16.2:18.3 - Respecifying a route specification
A route-bearing publication may keep the same general direction but replace one route specification with another when later review shows that the original framing selected the wrong governing pattern family. The point of `respecify` is to make that replacement visible without pretending the earlier route specification never existed.

#### A.16.2:18.4 - Retiring a route branch
A route-bearing branch may later be withdrawn because better-supported grounds, clearer closure, or a more adequate successor publication now carry the work. `retire` keeps that withdrawal visible instead of letting the branch vanish into later prose.

### A.16.2:19 - Review Matrix for Retreat Integrity

A reviewer can test retreat integrity with five questions:

1. **Was the trigger explicit?** If not, the retreat risks becoming retrospective narrative repair.
2. **Was authority updated?** If the earlier publication with named authority-reference relation, evidence-support class, or gate/admission basis no longer applies, any dependent route-bearing publication, gate decision, or endpoint authority claim must have been revised.
3. **Did valid witnesses survive?** If all earlier grounding disappeared without reason, the retreat probably became erasure.
4. **Was the move kind correctly named?** Reopen, sketch-backoff, respecify, and retire solve different problems; confusing them obscures what actually changed.
5. **If a branch was retired, was successor / no-successor status explicit?** If not, retirement may be hiding silent laundering.

The matrix is intentionally small: `A.16.2` should keep retreat legible, not surround it with decorative procedure.

### A.16.2:20 - Required Downstream Repairs

#### A.16.2:20.1 - Stale downstream publication/work-target rule
A retreat or retirement often leaves stale downstream publications or work targets behind: prompts, `A.6.A`-governed invitations, evaluative notes, requirement candidates, or work hooks that were admissible only under the prior state with higher closure state, route authority state, or endpoint authority claim. A conforming retreat should therefore name which downstream publications or work targets remain valid, which must be revised, and which must be withdrawn.

#### A.16.2:20.2 - Narrow retreat propagation
Retreat propagation should be as narrow as truth permits. If only one framing scaffold failed, then only the downstream publications or work targets that depend on that scaffold need revision. Over-broad rollback is wasteful; under-broad rollback leaves false authority in circulation.

#### A.16.2:20.3 - Retreat timestamping and witness continuity
Where several revisions exist, the retreat note should make clear which earlier publication it revises and which witness set still carries continuity across the revision. Without that linkage, readers may not know whether two nearby texts are alternative drafts or a genuine retreat sequence.

### A.16.2:21 - Comparative Retreat Rule

#### A.16.2:21.1 - Retreat kinds are not interchangeable
`reopen`, `sketchBackoff`, `respecify`, and `retire` solve different problems. Comparing them as if they all meant "we stepped back" erases the specific authority change each one makes.

#### A.16.2:21.2 - Honest recovery over softening prose
A context may prefer softening language such as "refined further" or "adjusted slightly" even when a real retreat or retirement occurred. `A.16.2` rejects that habit. If authority fell, closure dropped, framing was withdrawn, or a branch was retired, the move should be named directly.

#### A.16.2:21.3 - Boundary to silent editing
If a publication is simply rewritten and no continuity or authority story is preserved, that is editing, not `A.16.2`. Retreat is a reviewable move only when the earlier high-closure form or form with endpoint authority claim remains part of the visible history.

### A.16.2:22 - Review Addendum for Retreat Integrity

Add three checks to the base retreat matrix:

- **Were downstream dependencies updated?**
- **Was the propagation scope truthful?**
- **Does the revised history remain legible?**

These checks keep `A.16.2` tied to explicit recovery and retirement rather than narrative smoothing.
### A.16.2:End

