# The path of change

"Make the change easy, then make the easy change" in practice: how to find the preparation, how
to order the steps, and how to move a live system from the old shape to the new one.

## Contents

- [Two kinds of change](#two-kinds-of-change)
- [Finding the preparation](#finding-the-preparation)
- [When to tidy](#when-to-tidy)
- [When the preparation is hard](#when-the-preparation-is-hard)
- [Code nobody understands](#code-nobody-understands)
- [Changing contracts and data](#changing-contracts-and-data)
- [Lifecycle changes](#lifecycle-changes)
- [Rollback and fix-forward](#rollback-and-fix-forward)
- [Rehearsing the next change](#rehearsing-the-next-change)
- [A design with a time limit](#a-design-with-a-time-limit)

## Two kinds of change

A **structure change** rearranges code and keeps behaviour. A **behaviour change** alters what
the system does. Keep them in separate steps, and where the project allows, in separate
commits:

- a structure change is checked by "nothing observable changed", so it is cheap to review and
  safe to revert;
- a behaviour change made on prepared structure is small, and its diff shows the intent.

Mixed together, neither can be reviewed, and a revert throws away both. The intention to keep
behaviour is not proof that it was kept: run the checks that exist, and add a characterization
check where there are none.

Each step leaves the system working and is safe to stop after. A plan whose middle steps leave
the system broken is one large step.

## Finding the preparation

Ask: *what would the code have to look like for this change to be one obvious edit?* The
difference between that and today's code is the preparation.

Aim it at the hard spot found by trying the direct change, not at general untidiness:

| The direct change is hard because | Preparation |
|---|---|
| The rule lives in several places | Bring it to one place first |
| The code that must vary is tangled with code that must not | Separate them; then vary one |
| The behaviour is scattered and cannot be followed | Gather it into one pile, understand it, then split along the real lines |
| Callers know the internals that must change | Put the new interface over the old implementation; move callers; then change the inside |
| The data shape does not fit | Change the shape first, with behaviour unchanged |
| A step has several effects that must now differ | Split deciding from doing |

Preparation may be nothing. If the direct change is easy and leaves the structure no worse,
make it.

## When to tidy

| When | If |
|---|---|
| **First** | It makes this change easier now, it is small, and it keeps behaviour |
| **After** | The right shape became clear only by making the change |
| **Later** | It is large, not blocking, and worth a step of its own. Record it where the project tracks such work |
| **Never** | The code will not be changed again, or the tidying would cost more than every change it helps |

Preparation serves a confirmed change or a justified risk. Restructuring for an imagined future
is speculation with a refactoring label.

## When the preparation is hard

Beck's warning is literal: the preparation can be most of the work. When it is:

**Try, note, revert, do the prerequisites.** Attempt the change naively. Note everything that
breaks or blocks it. Revert completely. Do one prerequisite that has no prerequisites of its
own, as a working step. Repeat until the original change goes through cleanly. The notes form a
graph of prerequisites; the tree is never left broken, and work can stop after any step. (The
Mikado method.)

**Keep the old interface while the inside moves.** Build the new structure beside the old one,
switch users one at a time, delete the old one last.

**Stop honestly.** If the preparation costs more than it returns over the horizon of the task,
make the direct change and say in the decision sentence what was left: "chose the direct change
over extracting X because the module is frozen after this release; accepting a third copy of
the rule".

## Code nobody understands

Before changing code without tests or a clear author:

- **Pin what it does.** Write characterization checks around the part to change. They record
  current behaviour, not required behaviour: label them so that nobody later reads a pinned bug
  as a requirement.
- **Find a seam.** A seam is a place where behaviour can be altered without editing in place: a
  parameter, an interface, a function passed in. Put the change at the seam and keep the edit
  inside the old code minimal.
- **Ask why the odd thing is there** before removing it. Look at history, the linked issue, the
  tests, the callers. Then decide with three things kept apart: what is required, what the code
  does, why it came to be. The reason may be a live constraint, a fix for a dead bug, or an
  accident that callers now depend on.
- **Do not widen the change.** Understanding code is not a mandate to rewrite it.

## Changing contracts and data

A contract or stored format with live clients or existing records cannot be changed in one
step. Use expand, migrate, contract:

1. **Expand.** Add the new form beside the old: a new field, endpoint, column or message
   version. Old clients and old code keep working.
2. **Migrate**, in an order that never leaves a consumer with something it cannot read:
   - first make every reader accept both forms, and deploy that everywhere;
   - only then let writers produce the new form;
   - backfill the old data: repeatable, resumable, in bounded batches, safe next to live
     writes;
   - switch a read that needs complete data after the backfill, or keep a working fallback to
     the old form until then.
3. **Contract.** Remove the old form after evidence that nothing uses it. The absence of
   complaints is not that evidence.

For each state on the way, write down what every running version writes and what every
consumer can read. A step is safe when those two lists match.

During the path, the intermediate states are part of the design. For each one, check:

- **Versions that coexist.** Old and new code run together during every deploy. Can old code
  read what new code writes, and the reverse?
- **Half-migrated data.** Some records are in the new shape, some in the old. Which code handles
  each, and what does a reader see?
- **Work in flight.** Jobs, sagas, queued messages and open sessions that started under the old
  rules: do they finish under the old rules, the new ones, or get converted?
- **Caches and derived copies.** They keep old shapes after the source has changed.
- **Order of deployment.** Which component must ship first, and is that enforced or only
  hoped for?

Temporary coexistence adds code and state. It is the price of compatibility, not a failure to
keep things DRY. A design with a correct end state and no executable path to it is not a design
yet.

## Lifecycle changes

Changes to how long things live break hidden assumptions:

- removing a periodic restart or re-creation removes the cleanup it performed in passing
  (leaked handles, stale caches, a stuck state that a restart used to clear);
- moving work into the background changes its ordering, how long locks are held, and who sees
  the error;
- merging pools or queues widens the reach of one bad tenant or job;
- splitting a component removes joint restarts that used to reset shared bad state;
- making a short-lived thing long-lived exposes growth nobody had to bound before.

When a change alters a lifetime, an owner or a restart pattern, look in the code and its
history for what depended on the old one. This is a targeted search, not a reason to read the
repository.

## Rollback and fix-forward

Decide for each step what "going back" means:

- a revert restores code. It does not restore data written in the new shape, messages already
  sent, or money already moved;
- a feature flag switches the code path. After the new path has written data or caused an
  outside effect, switching it off is a new state, not the old one;
- a restore from backup loses what was written after the backup, and is real only if the
  restore has been performed.

For every step name: what can be undone and how; the point of no return; and beyond it, how a
defect is fixed forward. Put the irreversible step as late as possible and make it as small as
possible. Before it, gather the evidence that would otherwise be wanted afterwards.

## Rehearsing the next change

After the design, take the next plausible change from the context and walk it through the new
structure. If it needs edits in many places or knowledge of internals, the structure hides the
wrong decision. This costs minutes and catches preparation aimed at the wrong axis.

Rehearse a confirmed or likely change. Rehearsing every imaginable one leads back to
speculative generality.

## A design with a time limit

Building for a limited horizon is legitimate: a prototype to learn the problem, a first version
for a scale that will be outgrown. It needs three things written down: the horizon, the signal
that it is time to replace it, and the way out (where the data goes, which contracts survive).
A time limit does not suspend the musts, and a rewrite and migration are never free.
