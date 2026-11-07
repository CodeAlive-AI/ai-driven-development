## KCAE.CHANGE - Keep Source Reading and Derived Views Coherent through Change

> **Type:** Method pattern
> **Status:** Stable

### KCAE.CHANGE:1 - Problem frame

**Use this when** sources, extraction, permissions, representations or cached judgements change while access continues or resumes after an interruption. A search hit and its opened passage can each be valid in isolation and form an invalid pair.

The gain is a truthful choice among coherent current access, identified historical access and a bounded degraded route. A frozen one-use dossier needs only a fixed source basis, not an elaborate generation service. More machinery becomes justified when concurrent readers, several stores or repeated refresh make that basis hard to preserve.

### KCAE.CHANGE:2 - Problem

Updating one index does not atomically update sources, vectors, summaries, permissions and stored recommendations. A content hash catches a changed block but can miss a changed parent heading or governing exception. A completed update job does not by itself prove that the searchable collection matches a fresh construction or that the result is still applicable now.

### KCAE.CHANGE:3 - Forces

Availability competes with coherent switching. Rebuilding everything can be wasteful; selective reuse can retain hidden stale dependencies. Immutable generations simplify reading but consume storage. Source currency, model compatibility and permission currency can change at different rates.

### KCAE.CHANGE:4 - Solution

#### KCAE.CHANGE:4.1 - Detect changes at the relevant dependency boundaries

Maintain a source inventory that can distinguish addition, deletion, content change, relocation, replacement and a change in role or authority. Identify editions and membership from the source system or a captured snapshot. A directory scan of a changing tree is not automatically a snapshot: obtain source locking, immutable revisions, a stable export, or detect concurrent mutation and retry the affected acquisition.

Establish how a change becomes observable: an authorized event feed, revision query, periodic polling, supplied export or explicit owner notification. Record the last successful observation and the coverage or freshness interval it supports. Detect a broken subscription, failed fetch or missed sequence where the source permits it. “No change event received” supports currency only under a functioning channel with the required coverage; after an unexplained gap, recover the current inventory or mark currentness unknown. A periodic full reconciliation can find missed additions and deletions that an event-only path would retain indefinitely.

Track the dependencies actually used to derive a result. A retrieval unit can depend on its bytes, enclosing heading, table structure, contextual prefix, linked definition, extraction version and model configuration. An assessment additionally depends on the case facts, criterion and source-role basis. A recommendation additionally depends on burden and the receiving opportunity. These are different invalidation sets.

For example, moving an unchanged clause from “general availability” to “obsolete compatibility” leaves its block hash unchanged and changes its practical interpretation. Recompute the context-sensitive representation and reopen dependent assessments. An unchanged embedding can sometimes be reused technically while the source address or applicability is updated; do not infer semantic validity from that reuse.

#### KCAE.CHANGE:4.2 - Construct a candidate generation without disturbing readers

For a repeated service, assign a generation identifier to a coherent source snapshot and the derived views prepared against it. A manifest identifies source membership, editions, extraction and representation configurations, and each view's ready, unavailable or limited status. It need not duplicate the complete data, but it must resolve exact reads and state what a route can search.

Build new or changed units, remove deleted membership, update structural links and recompute context-dependent units. Reuse an embedding only when the required source/context and embedding-space conditions still hold. A change of model, preprocessing, vector dimension or comparison convention can require a new compatible index. Mixed spaces do not become comparable because their numeric dimensions happen to match.

Persist the candidate and test a newly loaded instance, not only the in-memory builder. Exercise build, save, close, load, query and source read. This catches missing files, omitted metadata and incompatible serialization. Validate required view membership, exact return addresses and representative changed cases before making the generation selectable. A failed optional view can leave a useful generation with fewer routes; a failed necessary source reader prevents that use.

#### KCAE.CHANGE:4.3 - Publish and read one coherent generation

In a single store with a transaction that covers all relevant data, use that store's actual transaction and isolation semantics. In a composition of object storage, a lexical database and a vector service, a metadata manifest is not a transaction over those stores. Obtain a different publication construction.

One workable construction uses immutable generation-specific objects and namespaces. Build and durably store all objects needed for a declared route; validate their resolvability; then atomically change a small catalogue pointer to the new manifest using a store that actually supports that operation. Readers acquire the pointer once and pass its generation through search, open and pagination. They can see the complete old generation or the complete new one; they must not independently fetch “latest” at every step. This claim depends on immutable names, durable objects, an atomic pointer operation and preserved objects during a read. Test these assumptions in the chosen stores.

Use an expected previous pointer or equivalent compare-and-swap when concurrent publishers are possible. A publisher that loses the race must reconcile its source basis; blindly installing its older candidate can regress currency. Preserve old objects while readers still hold them, through bounded read leases, reference tracking or a declared retention interval with an explicit expiry response. Garbage collection must not silently break an in-flight read.

If those facilities are unavailable, a maintenance interval with unavailable service during installation is a legitimate simpler construction. State that availability tradeoff. Do not claim atomic continuous service merely because the individual store updates usually finish quickly.

#### KCAE.CHANGE:4.4 - Separate historical coherence from current authority

A pinned historical generation can be perfectly coherent and no longer govern today's action. Mark the requested use: historical explanation, current recommendation or comparison across editions. Before a consequential current recommendation is used, check the authority/currentness condition required by the use. If it changed, reopen the affected judgement against the new source. A user-visible old answer needs a stale or superseded disposition where continued reliance matters.

A failed vector update need not force stale advice. Use the new generation's exact or lexical route, a direct source scan, or a qualified unchanged subset whose dependency boundary is known. Advertise that route's scope. If no adequate current route remains, return an availability limitation. Keeping an old generation online is a service rollback; it does not make an old rule current again.

If users edit sources while the prepared view lags, either construct a new snapshot before serving those edits or expose a delta layer: exact current additions and changes plus tombstones for removed old material, with an explicit combined membership and conflict rule. The merge must remove obsolete hits and open the selected current edition. A silent mixture of edited files and an old index is not an incremental profile.

#### KCAE.CHANGE:4.5 - Handle deletion and permission change explicitly

Source deletion can mean removal from current membership, withdrawal of a claim, retention expiry or access revocation. Obtain that meaning from the source policy. Keep authorized historical material only when retention permits it. Purge or quarantine prohibited copies in indexes, caches, summaries, logs and memory according to that policy; removing one search row is not a complete deletion procedure.

Where a provider removes index entries eventually, enforce current membership and permission at result release and source opening as well as at query filtering. A stale candidate identifier must not expose withdrawn content. Overfetching and post-filtering can change recall and latency; measure that cost. Rechecking permission still leaves a time-of-check/time-of-use question. Use the source service's enforcement at the actual read or action when immediate revocation matters, and state any remaining race rather than claiming universal instantaneous revocation.

A permission cache has its own allowed age. Source-generation pinning must not freeze permission to an obsolete grant. If source content may be retained historically but a particular reader loses access, the generation remains a historical object while that reader's operation is denied.

#### KCAE.CHANGE:4.6 - Test update, recovery and dependent use

Construct changes that exercise the intended guarantees: add a decisive passage; alter a condition; move an unchanged block under a different heading; split a section; delete a source; change a permission; fail a vector build; interrupt before and after pointer publication; reopen from persisted state; and read across the switch. Select cases from the actual architecture rather than treating this list as exhaustive.

Compare incremental and fresh construction on a stable input. For deterministic representations, compare exact membership and expected values. For stochastic extraction or approximate retrieval, compare the intended semantic and retrieval properties with recorded variation; byte inequality is not automatically a defect, and job completion is not equivalence. Repeat questions whose answers depend on the change and unchanged controls that should retain their result.

Follow dependencies into cached assessments, composed relations, deliveries and episode memory. Invalidate, recompute or retain each at its actual basis. A failed source update and a changed model have different consequences. Preserve sound unaffected results, but do not let a valid low-level hash become an all-purpose reuse certificate.

### KCAE.CHANGE:5 - Archetypal Grounding

CedarBench revision 8 adds a destination-certification condition to automatic resend, relocates the procedure and removes an old workaround. The new source and lexical reader pass their checks; vector construction fails. Publish a generation whose current routes are exact and lexical, with vector search unavailable for the changed material. A revision-7 vector hit cannot authorize revision-8 operation. Pending resend advice is reopened because its condition dependency changed.

A historical analyst can still request revision 7 if retention and permission allow it. Its exact reader remains valid for that named inquiry. This is not a claim that the older procedure is approved today. If the source store forbids retained copies after withdrawal, even the historical request must return that access limit.

### KCAE.CHANGE:6 - Bias-Annotation

Successful happy-path refreshes can hide cross-store races. Test interruption and denied access as ordinary states. Desire to avoid rebuilding can make dependencies artificially narrow; inspect contextual changes outside the unchanged block. Conversely, invalidating everything can make maintenance unaffordable; retain results on a sufficiently specific surviving basis.

### KCAE.CHANGE:7 - Conformance Checklist

Is the source snapshot actually stable? Are contextual and configuration dependencies included? Can a freshly loaded instance read the prepared generation? What operation makes it selectable, and which store guarantees it? Does one reader remain on one generation? Can historical coherence be distinguished from current authority? Are deletion and permission enforced at the relevant operations? Have dependent judgements received dispositions?

### KCAE.CHANGE:8 - Common Anti-Patterns and How to Avoid Them

A manifest is not a distributed transaction. A hash of one block is not a hash of its meaning. A successful refresh is not proof of fresh-build equivalence. Rollback does not reinstate superseded authority. Deleting an index entry does not necessarily delete provider-held content or prevent eventual stale hits; enforce the actual data lifecycle.

### KCAE.CHANGE:9 - Consequences

The service can remain useful during partial refresh without hiding its limits. Generations and retained dependencies cost storage and engineering effort. Small installations can choose a frozen snapshot or a maintenance interval instead. Coherence and currency remain separate properties across every profile.

### KCAE.CHANGE:10 - Architectural Rationale

Immutable content plus a controlled selection operation reduces a many-store consistency problem to a smaller publication boundary, under explicit assumptions. Dependency-specific invalidation preserves affordable reuse. Separate permission enforcement prevents an otherwise useful historical snapshot from extending a revoked grant.

### KCAE.CHANGE:11 - SoTA-Echoing

CodeNib's versioned code-corpus construction and update experiments motivate separate checks for source/view identity, persistence and fresh-build comparison; its code results do not establish correctness for another corpus. SQLite documents guarantees within its own database. OpenAI's retrieval documentation distinguishes asynchronous ingestion and eventually consistent removal. KCAE.Profiles:3 uses those bounded capabilities without extending one store's guarantee across a composition. Reopen this construction when the source or provider changes its durability, deletion, namespace or transaction semantics.

### KCAE.CHANGE:12 - Relations

KCAE.SOURCE supplies source identity and context dependencies; KCAE.INDEX supplies view configurations; KCAE.DELIVER consumes pinned reading; KCAE.MEMORY consumes invalidation; KCAE.EVAL compares changed behavior. The receiving domain's authority policy determines what governs current action; this engineering method does not create it.

### KCAE.CHANGE:End
