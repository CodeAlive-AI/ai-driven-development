## SYSE.Application:5 - APP-SYSE-05 - Worked application: construct a supported software build-and-delivery path

This is a constructed desk example. Its numbers, trials and observations are stipulated to explain how the Methods compose. The result is a supported-path candidate with unresolved choices.


### SYSE.Application:5.1 - Initial situation and available means

ParcelWorks has six teams maintaining twelve internal service applications in Go and TypeScript, with PostgreSQL 18 data stores. Developers already use a managed CI service and an artifact registry. The provider offers version-addressable runner images and artifact storage by digest. Several teams frequently change a common staging environment.

Among twenty recent illustrative release attempts, six required repeated infrastructure contacts, four included failed tests that later passed on unchanged inputs, two used different staging/production bytes despite the same source revision, and one attempted application rollback failed after a database-column rename. These counts overlap; they do not describe thirteen distinct failed attempts. Burst submissions can wait without useful status.

The user need is to take a service change to bounded production use with meaningful feedback and a usable recovery option. Existing constraints prohibit production personal data in preview environments and release credentials in untrusted branch jobs. Product release holders authorize production changes; platform operators maintain provision but cannot waive those constraints.

The team will construct the delivery path, reliability objectives, exposure rules and data-change mechanism using the following source Methods: the DORA continuous-integration route under `SYSE.31`; configuration and release Methods in `SYSE.13` and `SYSE.14`; whole obtaining comparison in `SYSE.24`; independent-provider integration in `SYSE.18`; SLSA v1.2 artifact verification; and the PostgreSQL 18 engine primitives and recovery Method named in `SYSE.34`.


### SYSE.Application:5.2 - 1. Derive an improvement and compare repaired obtaining arrangements

Applying `SYSE.25`, the team groups the observations by the developer's failed undertaking. The first improvement hypothesis is a supported way to obtain trustworthy feedback and move the identified result into limited use. A new portal is one possible interface, not the user result.

The team uses `SYSE.24` to construct three whole arrangements. The comparison holds constant the service class, source change, provider capabilities, artifact identity, isolated test data/environment, permission, deployment-test question and observation horizon. All three must include support, recovery, variation, maintenance and exit.

| Arrangement | Constructed provision | Choice-changing burden still to observe |
| --- | --- | --- |
| A: repair and retain local pipelines | Each application repository owns its workflow and environment recipe, carries the verified artifact unchanged, creates an isolated test environment and provides its support/recovery procedure. The original identity and shared-staging faults are repaired here too. | Each consumer maintains and qualifies its implementation. Duplication and support difficulty are questions, not assumed defects. |
| B: thin shared provision over existing services | A versioned shared workflow/module supplies the same artifact/environment operations. Consumers pin their selected version and retain explicit service configuration. The provider supports the shared contribution and its compatibility path. | Shared-component maintenance, consumer qualification, coordinated support, migration and correlated failure remain real work. |
| C: portal plus its required backend | The interface exposes operations with the same artifact, environment, support and recovery obligations. | Its additional user gain must justify another interface's implementation and maintenance. That gain is not yet established for this CI-familiar cohort. |

A matched constructed happy-path trial gives the same limited result for A and B: each carries the intended artifact unchanged, provides an isolated environment and completes the same bounded deployment test for the same ordinary changes. Both improve on the faulty baseline.

The choice result is a retained A/B tie and one discriminating probe. Apply the same provider/toolchain update and a recoverable failure to both arrangements. Include all affected consumer qualification and observe developer effort, maintainer effort, support fulfillment and correlated impact over the same interval. Counting only the shared-module edit or only local consumer maintenance would break the comparison.

C remains deferred until its extra user-result hypothesis can be tested fairly. The rest of this application develops B for the probe. A requested language-specific variant outside the probe remains unqualified; its existing local path is retained with its known limits.


### SYSE.Application:5.3 - 2. Construct the supported interaction and provider relation

Using `SYSE.26`, the team constructs a request that identifies source/configuration, allowed service variant and requested environment. The path acknowledges one attempt, shows whether it is waiting, executing, failed or complete, and returns the identified result with usable assistance.

In a constructed interrupted attempt, the user loses the response after an environment is created. The path queries the original attempt and returns that environment instead of creating another one. If the actual effect cannot be recovered, it returns uncertainty and assistance. Cancellation stops only the effects its qualified procedure can stop.

An otherwise valid request for an unsupported variant receives an explanation of the support limit and the contribution needed to support it. `SYSE.27` gives the contributing team compatible interface examples, a bounded contribution path and the maintenance/support result needed for adoption. Use OCE.6 to obtain a missing assignment.

The managed CI provider controls some runner changes, while ParcelWorks controls the selected image and workflow. `SYSE.18` constructs the distributed-authority integration decision: use the available version-addressable images, identify the affected commitment and notice condition, exercise the provider interaction and retain an exit/provision alternative. The whole obtaining comparison remains with `SYSE.24`.


### SYSE.Application:5.4 - 3. Produce trustworthy integration, build and artifact results

The application team names its mainline, a small change, adequate build/tests and the permission to integrate. The direct DORA CI Method under `SYSE.31` supplies the missing shared-mainline result.

A small code counterexample makes that result visible. Mainline M0 allows parcel weights from 1 to 10, with the invariant minimum <= maximum. Source change A raises the minimum to 8; source change B, developed against M0, lowers the maximum to 5. These source-change labels are local to this example, not the obtaining arrangements above.

| Checked source state | Range | Result |
| --- | --- | --- |
| A on M0 | 8..10 | Branch check passes. |
| B on M0 | 1..5 | Branch check passes. |
| B combined with already integrated A | 8..5 | Combined invariant fails despite no textual merge conflict. |
| Withdraw B and retain A | 8..10 | Rebuild/retest can qualify the restored mainline. |

A current-base check would stop B before integration. In the adverse history where stale branch feedback was accepted, the post-integration check blocks qualification of that shared revision's artifacts. The authorized application team withdraws B, rebuilds/retests the restored result and returns the conflicting business intent before B is tried again.

`SYSE.30` recovers the chosen integrated revision's resolved dependencies, runner/toolchain and relevant generated inputs. A clean-build comparison exposes an embedded build timestamp. The team removes irrelevant variation from the specified artifact or explains the difference under a weaker comparison. In the latter case, only that weaker comparison is qualified.

`SYSE.31` also reproduces fixture interference: one test deletes a row still used by another. Attempt-specific fixtures remove that interference while a deliberately wrong transformation still fails. Slower integration and application acceptance remain required where their different questions matter.

Using `SYSE.32`, the consumer obtains the tested artifact by its qualified identity, checks applicable evidence and the expected builder/source/provenance correspondence, and retains the same bytes for the next use. A correctly signed but unexpected origin fails the configured trust condition. Obtain the required verifier result before relying on the artifact.

`SYSE.33` constructs an isolated test environment from the versioned configuration and synthetic data seed. A clean creation, a relevant configuration change and a partial-creation failure are exercised. Existing resources are recovered by attempt identity before retry; cleanup is bounded by ownership and retained-data permission. Check that the intended task can run before relying on the environment.

`SYSE.28` places two different controls from the supplied constraints. Untrusted branch execution must not obtain release credentials. Artifact verification must occur before the consumer relies on transferred bytes. The example uses no production personal data. Production changes require the product release holder's permission.


### SYSE.Application:5.5 - 4. Construct a compatible data change and its recovery boundary

Further ordinary case facts now matter. One non-partitioned PostgreSQL 18 table has an immutable row ID and non-null Unicode delivery_address D. Old applications read and replace D as a whole. The new form edits the first display line L and remaining display text T; it does not infer postal structure.

Other address-writing triggers, replicated writers that bypass local triggers and external side effects of these row updates are absent in this bounded construction. If inspection cannot establish those premises, the mechanism below is not qualified.

`SYSE.34` constructs the correspondence. Split D at its first line feed, LF. With no LF, L = D and T = null; otherwise T contains everything after the first LF. Preserve all characters, including further line feeds. An empty tail after a trailing LF is not null. The inverse is D = L when T is null, otherwise D = L + LF + T; L must contain no LF.

Thus “12 Oak St” has an absent tail, while the same text followed by LF has an empty tail. Both reconstruct exactly. Normalization, postal parsing or a new value that cannot pass this inverse crosses an explicit information-loss boundary.

During coexistence, D remains the single write authority. Old applications write D. The new adapter validates L/T, joins them and writes D, not independent derived columns. A row-level BEFORE INSERT OR UPDATE trigger derives L/T from NEW.delivery_address and returns the row. [PostgreSQL 18 trigger semantics](https://www.postgresql.org/docs/18/trigger-definition.html) supply synchronous same-row execution in the triggering transaction.

The authorized operator briefly fences new address writes and drains in-flight writers for schema/trigger installation. Before writers resume, actual roles must be unable to bypass the trigger or independently write derived columns. Inspect broad table grants, inherited rights, ownership and superuser access under [PostgreSQL 18 GRANT](https://www.postgresql.org/docs/18/sql-grant.html); a column revocation does not cancel a table grant.

Backfill uses bounded Read Committed transactions over stable ID ranges. For each named row it performs the equivalent of `UPDATE address SET delivery_address = delivery_address WHERE id = the_named_id`. The trigger derives from the current row being updated, never from an earlier cached D/L/T tuple. [PostgreSQL 18 Read Committed](https://www.postgresql.org/docs/18/transaction-iso.html#XACT-READ-COMMITTED) supplies the waiting-updater behavior for this stable-ID construction.

Advance the range position only after commit. An aborted transaction rolls back its changes and leaves the range unfinished. A lost acknowledgement permits replay from current values only because no other update side effect makes that repeat unsafe.

| Constructed history | Preserved result |
| --- | --- |
| Backfill derives A, then an old writer commits B. | The trigger derives B with the old write; neither reader prefers stale A. |
| An old writer holds the row, changes A to B and commits while backfill waits. | Backfill operates on current B rather than restoring an earlier observation. |
| Backfill commits A, acknowledgement is lost, an old writer commits B, then the range is replayed. | Replay derives B; a failed first transaction would retain neither its changes nor an advanced position. |
| The new form submits L = PO Box 7 and T = North Depot. | The adapter writes their exact joined D; the trigger reconstructs the same pair. |

Do not enable L/T-dependent readers before the scoped backfill and correspondence check establish their required population. Continuing writes retain the invariant. This release keeps D, the trigger and both reader contracts; an old executable can return without undoing legitimate new-form writes, subject to its other compatibility conditions.

Contraction is later work. Fence and drain all old writers and compatibility adapters, select the new write authority and validate its consumers before removing the old contract. If writes have lost data or compatibility required by the old contract, the old binary alone cannot restore that contract.

The separate [PostgreSQL 18 point-in-time recovery Method](https://www.postgresql.org/docs/18/continuous-archiving.html) requires an appropriate base backup and continuous required WAL archive, not a logical dump substituted into that mechanism. Restore the whole cluster into an appropriately isolated recovery arrangement, inspect the result and compare achieved loss/time with the authorized limits. Later business events require their own reconciliation. An archive gap blocks that fallback, not an independent non-data-changing artifact test.

Before using this data-change mechanism, exercise the schema, roles, concurrency, load and recovery arrangement in their deployed conditions.


### SYSE.Application:5.6 - 5. Produce and test an actual runtime

The service has an old serving pool, a separate two-instance candidate pool and an operator interface that can install an identified package, set configuration, start a process and read back actual runtime state. Its data use is the compatible state above. A release holder permits isolated deployment and a synthetic address write/read test, not general user exposure.

`SYSE.41` constructs the procedure: preserve ordinary routing on observed h1/c1; prepare the candidate resources and connections; install verified h2 with c2; query what actually runs on each target; and exercise the permitted write/read test under the data correspondence.

In the normal constructed history, both candidate instances run h2/c2, their dependency is accessible and the bounded test succeeds. `SYSE.11` can assess usability for that test use.

In the partial history, one instance reports h2/c2 while the second request times out. Readback finds h2 with c1 and a failing database connection. Keep ordinary service on the old pool, exclude the unqualified candidate, and reconcile the second instance to c2 or remove it from the candidate result. Unknown readback remains unknown, not “nothing changed.”

Repeat no data migration blindly. A return to h1/c1 is available only because the old data contract remains valid and the runtime restoration test succeeds. Wider release requires the release holder's decision.


### SYSE.Application:5.7 - 6. Measure the right tasks and evaluate exposure

`SYSE.36` is applied twice, to different software services. The application owner supplies the address-form acceptance meaning; the platform cannot substitute “deployment completed.”

| Subject and users | Eligible attempt and good result | Missing observation or decision |
| --- | --- | --- |
| Supported deployment path used by developers, with its path/configuration edition named | One authorized request for an already verified artifact/configuration in a supported class. Good means actual requested runtime identity and bounded deployment test returned within that class's agreed response limit. A pre-backend platform failure remains a failed eligible attempt. | Missing user-entry observation, unknown runtime or absent test prevents the good claim. Platform users/providers agree the objective and response policy. Without an agreed response bound, timeliness is not qualified. |
| Address application h2/c2, compared with the named h1/c1 control, used by parcel operators | One authorized view/edit/save of a supported address. The new form displays the correct components and preserves submitted text under the correspondence within the application's own agreed bound. A version/snapshot or controlled test separates later legitimate edits from corruption. | Missing form observation, value/identity correspondence or candidate/control attribution leaves application success unestablished. HTTP 200 is insufficient. The application owner supplies meaning and its release holder decides reliance. |

The common comparison concerns correct address use under each form's supported contract, not identical layout. The instrumentation must observe that meaning or expose the remaining gap. Each error budget and `SYSE.37` alert, if used, belongs to its own service and task population.

With permission for the bounded exposure and a qualified stopping action, `SYSE.35` evaluates application h2/c2, not the platform path edition. In one invented interval, nine general candidate requests occur but none uses the changed form. The relevant evidence is insufficient: the application-exposure result is inconclusive.

Meanwhile, all ten observed platform deployment attempts may have completed correctly within their own agreed and observed response bound. Those successes do not alter the application's inconclusive result.

In an adverse form observation, the new screen hides a non-empty tail although the backend preserves D/L/T and the platform deployed exactly h2/c2. Application acceptance fails, so exposure stops or returns within the qualified recovery boundary. This does not prove deployment-path failure. Conversely, failed CI workers can interrupt developer tasks while the old application continues serving parcel operators correctly.


### SYSE.Application:5.8 - 7. Recover, reduce burden and resolve migration

A different constructed burst fills shared execution capacity. Using `SYSE.40`, the team separates delivery-control work from heavy tests, bounds admission/waiting/retries and reports refused or late user attempts. The team uses `SYSE.38` to distinguish queue contention from a broken dependency using attempt-stage evidence and a permitted probe, then applies the qualified mitigation and verifies the user's result; uncertain data effects return to `SYSE.34`.

Later illustrative use of the explored B candidate shows fewer identity-reconciliation contacts but repeated requests for the unsupported build variant. `SYSE.39` compares an extension repair with automatic handling of those requests, including both developer and provider burden. `SYSE.25` uses that evidence to choose the next bounded improvement.

Using `SYSE.29`, the team migrates the affected users only after the new variant is usable and the old path's users, state, rights and support have a disposition. A quiet old endpoint does not establish that an infrequent recovery consumer is gone. `SYSE.21` becomes relevant when later practice supplies evidence for an engineering-culture change claim.


### SYSE.Application:5.9 - Result, stop and direct-entry variations

The example returns a constructed supported-path candidate for B, the retained A/B obtaining tie awaiting its matched maintenance/failure probe, an explicitly unqualified variant, an inconclusive application-exposure result and a concrete next improvement. `SYSE.14` keeps the actual release decision with its authorized holder.

A practitioner with an adequate SLO but no alert rule starts directly at `SYSE.37`; another with a failed job starts at `SYSE.38`. Neither must repeat the whole example.

For a separate high-volume service, the source-derived alert illustration with a thirty-day objective and 2% budget consumption in one hour yields 0.02 × 720 / 1 = 14.4, with a short companion window checking continuing consumption. It is neither ParcelWorks policy nor evidence for either ParcelWorks service. Ten eligible events per hour need their own interpretation; the high-volume threshold cannot simply be transplanted.

Ask the release holder for missing production permission. Revalidate the results that depend on a changed source, provider condition, representation, task meaning or observation gap.
