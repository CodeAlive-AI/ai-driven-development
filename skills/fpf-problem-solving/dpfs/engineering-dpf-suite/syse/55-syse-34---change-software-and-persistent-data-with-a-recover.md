## SYSE.34 - Change Software and Persistent Data with a Recovery Boundary

> **Status:** Stable

> **Normativity:** Guidance within the stated software-and-data change use; examples are illustrative.

### SYSE.34:1 - Problem frame

Use this pattern when a software change can alter stored information, its interpretation, or which old and new consumers can use it. Start with the values that must survive, the permitted writers and readers, and the point at which a previous executable would cease to understand the resulting state.

The first result is a bounded change-and-recovery procedure: compatible states, the selected write/synchronization mechanism, validation, the irreversible boundary, operating limits and the actual decision holder. If a required data fact, database-specific Method or permission is missing, return that precise gap.

Do not undertake a migration merely because an executable changes. An unchanged data contract may need only a compatibility check. Conversely, a schema that looks unchanged can conceal a changed meaning. This pattern does not provide a universal database algorithm or promise zero downtime.

### SYSE.34:2 - Problem

“Add fields, copy data, switch readers” leaves important work unspecified. Old writers may continue changing the original representation after a copy. Two new authorities can disagree. A retried backfill may overwrite a legitimate later write with a cached earlier value.

Returning the old executable is not enough when the new software has removed information or written values the old software cannot interpret. Even a successful database restore can omit later business events or repeat external effects. Recovery needs a real state boundary, not only a rollback button.

### SYSE.34:3 - Forces

| Force | Practical tension |
| --- | --- |
| Continuing service and simple change | Coexistence reduces coordinated interruption but adds compatibility and synchronization work. |
| New meaning and reversibility | A richer representation can improve use while making an exact return impossible. |
| Bounded migration and concurrency | Small batches control load; concurrent writes still need an explicit ordering rule. |
| Technical recovery and acceptable loss | A restore mechanism can work while its time or information loss remains unacceptable to the people relying on the service. |

### SYSE.34:4 - Solution

#### SYSE.34:4.1 - Recover meaning, consumers and authority

Describe the old and proposed values using the application's meaning, including null, empty, ordering, precision and identity distinctions that matter. Define a correspondence and any inverse. Identify inputs that cannot be represented or carried back without loss; do not hide them behind a convenient conversion.

Find every relevant writer and reader, including jobs, imports, replicas, recovery tools and infrequent clients. Recover the actual database/storage edition, constraints, triggers, isolation and permission conditions that the procedure will use.

Obtain the required meaning and acceptance limits from their holders. The platform can support the mechanism without deciding which information may be lost or how long the business can operate without the service.

#### SYSE.34:4.2 - Choose a change strategy and its states

Compare a bounded coordinated interruption with compatible coexistence. A short interruption can be simpler and safer for a small service; coexistence is useful only when its compatibility can actually be maintained. For either strategy, qualify the recovery actions available from its intermediate states, including forward repair where it is needed.

For parallel change, add the needed representation without prematurely removing the old contract, qualify coexistence, migrate consumers, and contract only after the old use has been resolved. The historical [Parallel Change Method](https://martinfowler.com/bliki/ParallelChange.html) supplies that strategy, not an engine-specific synchronization mechanism.

Identify what is valid at each intermediate state: which executable can read or write, what data transformation has occurred, and what return remains possible. A failed step must have a known stop or recovery action from its actual partial state.

#### SYSE.34:4.3 - Construct the write and backfill mechanism

Choose one authoritative representation during coexistence when that can satisfy the use, and derive the other views through a specified transactional or otherwise qualified mechanism. If independent writers are required, obtain an explicit conflict/order resolution Method; the instruction “write both” does not supply one.

Select a backfill rule that accounts for concurrent updates. Use the database's qualified locking, current-row or version-check behavior so that an old observation cannot silently replace a later legitimate write. Bound work and resource effects, including locks, storage growth and effects on serving traffic.

Make retry behavior explicit. Determine which transaction effects and progress observations are committed together, which may be replayed, and which external effects cannot be repeated. After a lost acknowledgement, first recover the actual state; a migration log entry alone is not proof that every dependent effect occurred.

#### SYSE.34:4.4 - Validate coexistence and the actual recovery claim

Derive the required histories from the selected transition and its supported uses. Exercise ordinary and boundary values, the writers/readers and concurrency that occur in that strategy, and consequential partial-failure or replay cases. Verify information correspondence as well as successful execution.

Do not activate a consumer that relies on a new representation before its required population and continuing-write invariant are established. If some data is intentionally outside the scope, ensure that the consumer can identify and handle that boundary.

Test the proposed return under the state it will actually encounter. Returning an executable, restoring information and reconciling later external events are different operations. Obtain a database-specific restore Method and suitable backup/archive material where restoration is part of the promise; measure its achieved loss and time against the authorized limits.

#### SYSE.34:4.5 - Execute within the boundary and separate contraction

Carry out the qualified bounded increment with the actual permission and observation needed to stop. A timeout or inconsistent state suspends dependent reliance; it does not justify blindly restarting the whole procedure.

Retain the old contract while the selected return depends on it. Removing old fields, accepting non-invertible new values or changing the write authority is a later state change with its own consumer and recovery question. Use SYSE.29 to arrange migration or continued support for remaining users, decide what must happen to retained state, and fulfil or obtain permission to end support commitments that outlive the technical transition.

Return the achieved compatible state, applicable evidence and remaining limits to deployment and release work. An engineered procedure is not evidence that it has already run, and a successful migration is not general release permission.

#### SYSE.34:4.6 - Derive the transition from compatibility in both time directions

Treat each intermediate state as a combination of running readers and writers, stored representations and in-flight work. Ask two different questions: can the next version use the state it will receive, and can the intended recovery version use the state the next version may create? Successful upgrade alone does not answer return. Include asynchronous messages and queued jobs: they can carry an older contract after its producer has stopped running.

Construct the transition backward from the desired new use. Identify the first action that requires new information, a new representation or a new interpretation. Before that action, establish every consumer capability needed for coexistence. One useful arrangement is to deploy readers that understand both forms while writers still emit the old form, then change writers after the dual-reading capability is present where needed. Another retains one old representation as authoritative and adapts new use to it, as in section 5. Both have costs: dual readers must remain correct for both meanings, while an adapter can limit which new values are expressible.

Compare those arrangements with a coordinated interruption. If all consumers can be stopped within an acceptable interval, a verified backup and a bounded offline transformation may need less mechanism than online coexistence. The interruption still needs prevention of late writes, a defined transformed population and a recovery decision after partially completed work. A large table, strict availability need or independently upgraded clients can make that arrangement infeasible. Choose from those conditions rather than treating online migration as automatically superior.

Common mechanisms for a continuously updated dataset include transactional projection, change-stream replication and a bounded write fence. A transaction can update the authoritative value and its derived representation together. A qualified change stream can carry updates after a known snapshot position, with ordering, replay and gap detection that the consumer understands. A bounded write fence can create a stable interval for transformation and switch. Merely running a bulk copy while writers remain active supplies none of these guarantees. A change-stream design additionally needs a rule for duplicates, reordering, deletion and catching up before the new reader depends on it. Obtain the storage-specific implementation for the chosen mechanism.

Do not treat coexistence completion as permission to remove old support. Find what can still return old data: a scheduled job, retained message, offline client, dormant disaster-recovery image or a restore from an earlier backup. A contraction may require keeping a conversion on the restore path even after no live client uses it. Select a compatibility horizon from those supported uses and retention commitments. This horizon can differ from the time needed to observe a canary or to finish the ordinary application rollout.

For a claimed return, test the state of greatest relevant exposure. In a coexistence strategy, include old and new writes; include partial migration and lost acknowledgement where they can affect the return. Follow which representation each reader sees and which effect a repeated operation could duplicate. If return would discard legitimate later events, decide whether those events can be replayed or reconciled and who may accept the remaining loss. A backup can supply older data without supplying this reconciliation. Keep a useful forward-repair option when exact reversal is unavailable.

For an unlike case, a job-message format gains a new optional field. First release workers able to read both formats while producers continue sending the old one. Then change a bounded producer population and observe completion of whole jobs. Retiring old workers is insufficient evidence to remove old-format reading: queued or archived jobs may still contain it. Conversely, rolling producers back does not remove already emitted new-format messages. If old workers cannot read those messages, recovery must retain compatible workers, translate messages with qualified meaning, or drain the queue under an agreed restriction. This is the same compatibility reasoning with a different persistence mechanism; the PostgreSQL trigger in section 5 is not its implementation.

### SYSE.34:5 - Archetypal Grounding

#### SYSE.34:5.1 - Define a reversible address correspondence

In a constructed ParcelWorks example, one non-partitioned PostgreSQL 18 table has an immutable row ID and a non-null Unicode text value D, stored as delivery_address. Old applications read and replace that whole value. The new form edits the first display line L separately from the remaining display text T. It does not infer postal structure.

Split D at its first line-feed character, LF. If no LF exists, set L = D and T = null. Otherwise L is the text before that LF and T is all text after it, including any further line feeds. Reconstruct D as L when T is null, or L + LF + T otherwise. L must contain no LF. Preserve every character; do not normalize whitespace.

| Old D | New L | New T | Reconstructed meaning |
| --- | --- | --- | --- |
| 12 Oak St | 12 Oak St | null | No line separator was present. |
| 12 Oak St followed by LF | 12 Oak St | empty text | The trailing separator is preserved. |
| 12 Oak St, LF, North, LF, Depot | 12 Oak St | North, LF, Depot | Remaining lines stay in the tail. |
| Empty text | empty text | null | Empty but non-null old text remains representable. |

This correspondence makes old and new text mutually recoverable within the stated domain. Postal parsing, normalization or an additional field that cannot be joined back is outside it and reopens the recovery decision.

#### SYSE.34:5.2 - Keep one write authority during coexistence

The selected authority remains D. Old applications write D directly. The new application's adapter validates L/T, joins them into D and writes D; it does not independently write derived columns.

A row-level BEFORE INSERT OR UPDATE trigger computes L/T from NEW.delivery_address and returns the modified row. The exact [PostgreSQL 18 trigger behavior](https://www.postgresql.org/docs/18/trigger-definition.html) supplies same-transaction execution and returned-row semantics. This construction excludes other address-writing triggers, replicated writers that bypass this trigger and external side effects of these row updates. If those premises are not established, this mechanism is not yet qualified.

The authorized operator briefly fences new address writes and drains in-flight writers while installing the schema and trigger. Ordinary application roles must not bypass the mechanism or independently write the derived columns. The [PostgreSQL 18 privilege rules](https://www.postgresql.org/docs/18/sql-grant.html) require inspection of table grants, inherited rights, ownership and superuser access; revoking a column privilege does not cancel a broad table grant. Resume old writers only after the actual configuration satisfies those conditions.

#### SYSE.34:5.3 - Backfill current rows rather than cached values

Backfill operates in bounded Read Committed transactions over stable ID ranges. For each named ID, it performs the equivalent of:

```sql
UPDATE address
SET delivery_address = delivery_address
WHERE id = the_named_id;
```

Here the_named_id is a bound value for the immutable row identity, not literal executable SQL. The trigger derives from the row being updated. The procedure never writes a D/L/T tuple cached by an earlier SELECT.

Under [PostgreSQL 18 Read Committed](https://www.postgresql.org/docs/18/transaction-iso.html#XACT-READ-COMMITTED), an updater waiting on another updater proceeds against the qualifying updated row after that transaction commits. The immutable ID keeps this case's selection stable. This is not a general guarantee for arbitrary multi-row predicates.

Advance the batch position only after commit. An aborted transaction retains neither its row changes nor an advanced position. If commit succeeded but its acknowledgement was lost, replay the range using current values. The case's exclusion of other update side effects is necessary for that replay to remain safe.

| Constructed history | Result |
| --- | --- |
| Backfill derives A, then an old writer commits B. | The trigger derives B with that write; both representations describe B. |
| Old writer B holds the row while backfill waits. | Backfill acts on the committed current B and does not restore A. |
| Backfill commits A, acknowledgement is lost, old writer commits B, then the range is replayed. | Replay derives B from current D. |
| New writer submits L = PO Box 7 and T = North Depot. | The adapter writes their exact joined D; the trigger reconstructs the same pair. |
| A backfill transaction fails before commit. | Its derived-field changes are rolled back and the range remains unfinished. |

Enable L/T-dependent readers only after the scoped backfill and a correspondence check establish their required population. Continuing writes must preserve the same invariant. The table contains constructed histories, not a report of executed PostgreSQL qualification; deployment use requires exercising the actual schema, roles, concurrency and recovery arrangement.

#### SYSE.34:5.4 - State the return and its end

This release retains D, the trigger and both reader contracts. Subject to the application's other compatibility conditions, the old executable can return while preserving legitimate address writes made through the new form. It is not necessary to undo those writes.

Contraction is separate. Before removing the old contract, fence and drain all old writers and compatibility adapters, select the new write authority and validate its consumers. Once a lossy transformation or incompatible new write has occurred, an old binary alone cannot restore the prior usable state.

Suppose a later contraction removes a trailing LF and retains neither the original D nor another copy of the absent-versus-empty tail distinction. Both `12 Oak St` (T = null) and `12 Oak St` followed by LF (T = empty text) then become `12 Oak St`: whether a separator existed is lost, and returning the old executable cannot reconstruct it. An exact-return promise therefore requires retaining D or that lossless distinction before this change; accepting its removal requires the actual decision holder to authorize a narrower promise. After the information is gone, exact restoration needs an independently retained, qualified recovery source and is unavailable without one. A qualified forward repair must meet the actually accepted result; it is not an inverse obtainable from the transformed value alone.

A distinct fallback uses [PostgreSQL 18 point-in-time recovery](https://www.postgresql.org/docs/18/continuous-archiving.html). It needs a suitable base backup and continuous required WAL archive; a logical dump is not a substitute for that mechanism. Restore the whole cluster into an appropriately isolated recovery arrangement, inspect its state and evaluate achieved loss/time. Choosing an earlier recovery point does not reconcile all later business events.

If an archive gap prevents that fallback, its recovery claim stops. A qualified forward repair may still be possible, and an independent non-data-changing artifact test can continue.

What changes in practice is that the team can explain which state remains usable after each change, why concurrent writes are preserved, and where “return to the old version” ceases to mean recovery.

### SYSE.34:6 - Bias-Annotation

Success on a static sample can hide concurrency, inherited privileges and rare representations. Teams can also prefer zero downtime without pricing the complexity of coexistence. Inspect real writers and adverse histories, and compare a bounded interruption with a more elaborate online construction.

### SYSE.34:7 - Conformance Checklist

- Old/new meaning and information-loss boundaries are explicit.
- All relevant writers/readers and engine-specific conditions are accounted for.
- Where old and new representations coexist, their authority and synchronization mechanism is concrete.
- Backfill cannot overwrite a later legitimate write with a stale observation.
- Consequential partial failure, lost acknowledgement and any allowed replay have qualified behavior.
- A new reader starts only with the population and continuing invariant it needs.
- Each promised executable return, data restore or later-event reconciliation is qualified for its own result.
- Contraction and permission to accept loss are not inferred from successful deployment.

### SYSE.34:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| Read old values, copy them later, then prefer any non-null new field. | Account for intervening writes and establish a maintained correspondence before new-reader reliance. |
| Make both old and new fields authoritative. | Choose one authority or supply a real conflict-resolution Method. |
| Repeat the entire migration after a timeout. | Recover committed and partial effects, then apply the qualified replay rule. |
| Reinstall an old binary after irreversible data loss. | Use a qualified forward repair or information recovery with accepted limits. |

### SYSE.34:9 - Consequences

The pattern makes the conditions and limits of migration and recovery claims explicit. Compatible coexistence can reduce interruption while adding temporary schema, adapter and maintenance cost. Some changes remain irreversible or require a planned outage; exposing that fact is more useful than promising a rollback that cannot preserve the information.

### SYSE.34:10 - Rationale

Compatibility is a relation between actual representations and consumers over time. A transition must maintain that relation under the writers that remain active. Whether recovery is possible therefore depends on the resulting state and available permitted operations, not merely on the availability of an earlier executable.

### SYSE.34:11 - SoTA-Echoing

For application/data transitions, **adopt and adapt** [DORA Database change management](https://dora.dev/capabilities/database-change-management/) and the foundational 2014 [Parallel Change](https://martinfowler.com/bliki/ParallelChange.html) treatment. Compatible intermediate states and versioned migration are established professional Methods. A coordinated interruption remains a serious alternative when its cost is acceptable and online coexistence is harder to support.

The DORA address example is insufficient as a concurrency implementation when old writers remain active: generic dual writing and null fallback do not determine authority, atomicity or exact text correspondence. Sections 5.2–5.3 construct one bounded alternative from PostgreSQL 18's trigger, privilege and isolation contracts. Section 4.6 derives other arrangements from actual readers, writers, in-flight work and recovery horizons. A change stream or write fence needs its own implementation qualification; the trigger does not generalize to every store.

Reopen the transition when representation meaning, writer population, engine behavior, side effects or supported return/restore paths change. Keeping old binaries or possessing a backup does not alone establish a usable recovery.

### SYSE.34:12 - Relations

SYSE.13 identifies software and data configurations. SYSE.27 and SYSE.29 address consumer compatibility and migration; SYSE.33 supplies controlled test conditions. SYSE.41 consumes the data-change result during deployment, SYSE.35 respects it during exposure recovery, and SYSE.38 uses it when an incident has partial data effects. Use SYSE.14 when a separately authorized release decision is needed.

### SYSE.34:End
