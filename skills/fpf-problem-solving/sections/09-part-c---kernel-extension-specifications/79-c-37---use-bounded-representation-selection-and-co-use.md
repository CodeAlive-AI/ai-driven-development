## C.37 - Use-Bounded Representation Selection and Co-Use

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.37:1 - Problem frame

**Plain name.** Selecting and using representations for one action.

**Use this when.** One person, team, organization, or other consuming System must take one exact action or make one exact decision, and several diagrams, tables, models, records, plans, descriptions, views, notations, or other results may each support only part of that use.

This is the one-use selection branch of representation work. The governed move is to decide how the receiver may use independently governed candidate results for that exact action. C.37 does not decide what those results are, whether their subject-side claims obtain, whether an episteme is a view, whether a graph is mathematically admitted, whether evidence may be relied on, or whether the receiving action is authorized. Those answers remain with their direct patterns.

**Primary working reader.** A practitioner who has more than one plausible way of seeing or carrying information into an action and needs a defensible selection without building a universal representation taxonomy.

**First useful move.** Name the receiving System and exact action or decision in one sentence. For each candidate, name the direct result it already has, the exact claim this use would rely on, what the candidate exposes and withholds, and the direct result that permits, declines, or leaves that use unresolved. Stop after one row if one row is enough.

**First useful result.** One logically complete use-bounded representation-selection account: one or more candidate claims with their material loss, direct basis and exact receiving action supported, declined or unresolved. It can be the immediate working answer; the row form and persistent record are not required when no later use needs them. Its use boundary is `<receiving System, exact action or decision>`. If retained as a standalone claim-bearing object, it has ordinary C.2.1 identity, an exact EntityOfConcern and effective reference scheme; the use boundary does not replace episteme identity.

**What goes wrong if missed.** A readable diagram is treated as a conforming view; provenance is treated as approval; an evidence classification is treated as permission; several adjacent results are treated as one coherent structure; or a choice made for one action silently travels into another action with different loss, evidence, and decision conditions.

**What this buys.** The practitioner can say which candidate is selected, declined, or unresolved for one use; which exact claim is being carried; what remains hidden or transformed; what direct result supports the use; and what change requires return or reconsideration.

**Not this pattern when.** Use the direct pattern and stop when it already returns the complete one-result/one-use selection and limits. Use `E.17.0` for view conformance, `C.29` for a mathematical-lens use, `A.6.3.RT` for changing representation while preserving content, `A.22` for selected structure, `C.13` for a construction or collection question, `E.24.PUB` for publication, and `C.2.P.DR` for declarative-representation overread. Use C.37 only when the receiving action still needs the cross-kind selection account after those direct results are available.

### C.37:2 - Problem

Representations are useful because they foreground different things. A workflow diagram may expose order while hiding effort. A work plan may expose intended timing while saying nothing about actual performance. A work record may expose an observed breakdown while saying nothing about whether a proposed change will repair it. A graph may support traversal or calculation while omitting distinctions needed by a receiving decision.

The practical question is therefore not “which representation is best?” It is “which exact candidate result may this receiver use for this action, for which claim, under which limits, and what direct result makes that use available?”

Five recurrent shortcuts make the answer unsafe:

1. **Object shortcut.** A label such as *diagram*, *view*, *model*, *graph*, or *record* substitutes for the direct result that identifies the candidate and its subject-side claim.
2. **Classification shortcut.** An A.2.4 intended first evidence-use classification is treated as evidence sufficiency or permission.
3. **Provenance shortcut.** A source path, current carrier, or authentic publication is treated as a positive `RelianceDisposition` or receiving result.
4. **Decision shortcut.** A selected row is treated as the choice, authorization, permission, or gate result without the direct receiving pattern.
5. **Composition shortcut.** Several rows are treated as a collection, structure, integrated view, world model, or graph merely because one receiver reads them together.

### C.37:3 - Forces

| Force | Tension |
| --- | --- |
| Useful foregrounding vs visible loss | A representation helps by emphasizing some distinctions, but the same emphasis can hide uncertainty, conditions, or alternative readings. |
| Cross-kind comparison vs direct authority | Candidate results may be diagrams, plans, records, views, or mathematical objects, while each keeps a different identity and obtaining rule. |
| Cheap orientation vs bounded reliance | Reversible inspection may need only a direct result and limit; consequential use may require an exact A.10 path and disposition. |
| Co-use vs invented whole | Several candidates may be needed for one action without forming a collection, structure, composite view, or unified world account. |
| Stable source vs changing action | The same candidate can be selected for one action and declined for another because the relied-on claim and tolerated loss differ. |
| Clear decision support vs borrowed authority | The account must help a decision without becoming the choice, gate, permission, authorization, assurance, or domain result. |

### C.37:4 - Solution

Use one action spine:

1. name the receiving System and exact action or decision;
2. recover each candidate and its direct subject result;
3. separate the direct subject result, optional first-use classification, bounded reliance, receiving result, and auxiliary facts;
4. state what the candidate exposes or preserves and what it withholds, loses, transforms, or leaves uncertain;
5. mark the row `select`, `decline`, or `unresolved` for the named use and give its return trigger;
6. co-record only rows that support the same receiver and exact action or decision.

**Local mantra.** *One receiver, one action. Recover each candidate under its direct pattern. Name the claim, reliance, loss, receiving result, disposition, and return. Put rows together only for that action.*

The mantra is a recall aid, not a decision rule. The receiving pattern still emits the choice, gate, permission, authorization, or domain result.

#### C.37:4.1 - Fix the receiving use before inspecting candidates

Write one sentence:

```text
<receiving System> must <take this exact action or make this exact decision>.
```

Every row in the account uses that same receiver and action. A diagram used to select a proposed Method edition and the same diagram used later to tailor that Method belong to different accounts. Adjacent actions, one project, one carrier, or one meeting do not merge their use boundaries.

If one direct pattern already returns the complete representation–operation choice and limits for this use, take that direct exit. Do not add C.37 merely to rename its result.

#### C.37:4.2 - Recover each row through five separate layers

Open only the layers required by the attempted use.

| Layer | What must be recoverable | What it does not establish |
| --- | --- | --- |
| Direct subject result | The candidate's independently governed kind or result, its subject, and any exact representation, conformance, correspondence, transition, structure, collection, mathematical, plan, Work, or domain relation on which the selected claim depends. | Intended evidence use, reliance, receiving decision, permission, gate passage, or authorization. |
| Optional A.2.4 first-use classification | When the candidate episteme is being used as evidence or as a status carrier, the exact episteme, target claim or status, scope, polarity or value, window, and intended use. | Provenance, sufficiency, `RelianceDisposition`, assurance, permission, or receiving action. |
| A.10 bounded reliance, when material | The exact relied-on claim, source and provenance path, premise, reference, decision-use, operation-argument, or other direct use relation, time/currentness boundary, bounded evidence use, unsupported attempted use, challenge when current, one current `RelianceDisposition`, and its reopen or stop condition. | Claim truth, selector outcome, gate result, approval, permission, assurance, or Work authorization. |
| Receiving result | The exact `ChoiceResult`, gate result, permission, authorization, acceptance, or domain result supplied by the pattern that defines or tests the receiving action. | Candidate identity or evidence merely by mentioning the row. |
| Auxiliary facts | Lens, publication, form, carrier, repair, provenance, source, or rendering facts needed to interpret or recover the row. | Any missing positive subject result, reliance, or receiving result. |

If a layer required by the attempted use is negative, missing, or unresolved, do not borrow support from another layer. Decline the row or mark it unresolved and name the missing fact or direct result.

#### C.37:4.3 - State exposure, loss, and the row disposition

For each candidate, state only distinctions that change the receiving action:

- what it exposes, foregrounds, or preserves;
- what it withholds, omits, loses, transforms, or leaves uncertain;
- the exact claim for which it is selected or declined;
- the direct result and, when material, A.10 disposition that bounds that claim;
- the condition that sends the reader back to the source or reopens selection.

Use exactly these ordinary row dispositions:

| Disposition | Use |
| --- | --- |
| `select` | The required direct subject result is positive, every required reliance condition supports the exact bounded use, and the receiving result permits this candidate's stated contribution. Narrow the selected claim when A.10 says `degrade`; do not invent a second disposition vocabulary. |
| `decline` | A required direct result is negative, the receiving result excludes the candidate, or the candidate's loss makes the attempted use inadmissible. State the retained weaker use, if any. |
| `unresolved` | A required identity, relation, currentness fact, reliance path, disposition, or receiving result is missing or ambiguous. Name what would reopen the row. |

Selection is use-bounded. It does not make the candidate true, complete, current, published, conforming, relied on, assured, or authorized outside the exact claim and action stated in the row.

#### C.37:4.4 - Use the smallest complete account

Use this readable shape when the result must be retained:

```text
Use-bounded representation-selection account:
  Receiving System and exact action or decision:
  Receiving-result governor and result:
  Candidate rows:
    - Candidate and direct subject result:
      Exact claim used:
      Intended first evidence use, if current:
      A.10 path, direct use relation, and RelianceDisposition, if current:
      Exposed or preserved:
      Withheld, lost, transformed, or uncertain:
      Disposition: select | decline | unresolved
      Return or reconsideration trigger:
  Action supported, declined, or blocked under the combined limits:
```

One row is a valid minimum when C.37 still adds a needed layer separation. If the direct pattern already supplies the same complete one-result/one-use answer, use the direct exit instead.

This is a logical claim group, not a universal record kind, `U.Representation`, `RepresentationOf` relation, taxonomy, manifest, view family, collection, or structure. Do not give it another schema merely because several domains use the same questions.

#### C.37:4.5 - Realize the result once

First determine whether a later receiving use needs the selection basis retained. An immediate sufficient selection can finish with its material loss and direct receiving result, without a new record or a certificate explaining non-retention.

When retention is needed:

1. If an owning domain result already carries the same receiving use, embed the complete needed claim group and action boundary there.
2. Otherwise retain that basis as one ordinary C.2.1 episteme.
3. Create no embedded and standalone duplicate for the same use.

A later reader who must reconstruct the selection receives its logically complete basis; a bare verdict or locator is insufficient for that use.

Retention does not weaken the required separation: direct subject result, optional A.2.4 classification, A.10 reliance when material, receiving result, exposure and loss, disposition and return remain recoverable as needed by that use. An immediate answer preserves the same substantive limits without instantiating every form field. A cross-use ensemble may later relate accounts under its own direct pattern; C.37 does not perform that organization.

#### C.37:4.6 - Keep co-use local to one action

`Co-use` means only that the same receiver relies on two or more completed rows for one exact action or decision. Each row keeps its own direct result, premise, reliance boundary, loss, and return trigger. One positive row cannot repair another row's missing subject result or reliance path.

Co-use does not establish:

- one collection or selected structure;
- one multi-view family or mutual conformance;
- one integrated model or coherent world account;
- one constructional whole or composition relation;
- one shared representation scheme, graph, or correspondence;
- one assurance result or authorization.

Open `C.13`, `A.22`, `E.17.0`, `C.29`, a domain integration pattern, or another direct governor only when the receiving action depends on that additional claim.

#### C.37:4.7 - Recognition, reliance, assurance, and action remain separate

Recognition asks what the candidate is and which direct result or relation obtains. A.2.4 may add only its first evidence-use or status-use classification. A.10 adds one bounded evidence-provenance and reliance result only when the exact use relies on evidence. `B.3` enters only when an actual named assurance claim is current; consequence or reuse alone does not require an assurance package. The receiving pattern then owns the action result.

This split lets ordinary reversible work stop cheaply. A practitioner may inspect or compare a candidate under its direct result and visible limit without opening A.10 or B.3 when no evidence reliance or assurance claim is being made. When reliance is material, the exact path and disposition become mandatory for that use.

#### C.37:4.8 - Direct exits and boundary cases

| Case | C.37 disposition |
| --- | --- |
| One direct domain Method already selects one representation–operation configuration for the same one use and returns its limits, as RHY.5 does for rhythmic-representation choice. | Use that Method and result; do not invoke C.37 for a duplicate account. |
| A candidate is called a view but `EpistemeViewpointConformanceRelation(E,P)` fails or cannot be evaluated. | Decline it for the view-dependent use or mark that row unresolved. C.37 cannot grant `U.View` membership. Another independently positive direct basis may support a different row and claim. |
| A candidate is a mathematical graph or other mathematical object. | First identify the object and obtaining subject relations under their direct patterns; then use `C.29` for the explicit lens, mapping, preserved and lost structure, admitted use, and stop. C.37 neither admits the object nor makes the mapping obtain. |
| A candidate is an ordinary non-graph diagram. | Identify its episteme and subject. Require an exact positive conformance, representation, correspondence, or domain result for the selected claim. Add A.10 when evidence is relied on. Publication, carrier, provenance, or C.2.P.DR repair cannot supply the missing basis or receiving result. |
| Several project, process, or case viewpoints concern one Work. | Co-record them only when each can change the same exact action about that independently identified Work. A viewpoint for another action starts another account. |

### C.37:5 - Archetypal Grounding

#### C.37:5.1 - Method change selected for one bounded trial

`MethodEngineer-ME1` must select or decline `MethodChange-MC7` as the proposed Method edition for one bounded trial in planned Work item `WP4`. This one decision is the join key for all three rows. A C.11 `ChoiceResult`, or the corresponding direct Method Engineering decision result, owns the selection.

| Candidate | Direct result, reliance, and receiving result | Exposed and withheld | Disposition and return |
| --- | --- | --- | --- |
| Workflow diagram in `MethodDescription-MD5`, edition 5 | A.3.2 identifies the episteme as a MethodDescription about `Method-M2`. A.2.4 may classify its intended evidence use. A.10 path `P-MD5` carries the premise “edition 5 states the proposed MC7 action order,” its source/currentness window, direct decision-use relation, and `RelianceDisposition=pass`. The C.11 result alone selects or declines MC7. | Exposes proposed sequence and handoff; withholds actual effort, achieved result, and future performer availability. | `select` for proposed-way claims only; return if the edition, intended Method, path, or reliance window changes. |
| `WorkPlan-WP4` trial item | A.15.2 identifies the schedule-of-intent episteme and its planned performer, interval, and capability conditions. A.2.4 may classify the intended use. A.10 path `P-WP4` carries the premise “WP4 currently provides the named trial slot and conditions,” source/currentness, direct decision-use relation, and `RelianceDisposition=pass`. The C.11 result alone selects or declines MC7. | Exposes a bounded trial slot and intended conditions; withholds actual occurrence, performance, and result. | `select` for planned-trial feasibility only; return if the plan, performer, interval, capability condition, path, or disposition changes. |
| `WorkRecord-W19` about actual `Work-W19` | A.15.1 admits the dated Work independently; C.2.1 identifies the record episteme. A.2.4 may classify its intended use. A.10 path `P-W19` carries the premise “WorkRecord-W19 reports the stated rework and effort under the named earlier conditions,” its provenance and decision-use relation, and `RelianceDisposition=degrade` to that comparability-limited premise. The C.11 result alone selects or declines MC7. | Exposes observed breakdown and effort under the earlier edition and conditions; withholds proof that MC7 fixes the breakdown or that the trial planned in WP4 will reproduce those observations. | `select` only for the narrowed comparability-qualified premise; return if the observed conditions, path, currentness, disposition, or relevance to MC7 changes. |

The resulting account does not say that three rows jointly prove MC7. It says which bounded premises the receiver may use, what each leaves out, and which C.11 result follows under those limits. If the same diagram is later used for a tailoring choice or WorkRecord-W19 for a learning decision, start another account.

#### C.37:5.2 - Failed diagram use

A release team receives a polished architecture diagram and wants to authorize deployment. E.24.PUB establishes that the diagram edition is available through a current carrier. C.2.P.DR repairs one route-shaped arrow that had been read as operational authority. Neither result establishes view conformance, a representation correspondence, runtime structure, evidence reliance, or deployment permission. Until the needed direct subject result, A.10 path and disposition, and permission or gate result are available, the row is `unresolved`; visual polish and provenance cannot upgrade it. If the direct release gate or permission pattern instead returns a negative result because its required basis is absent, the row is `decline`; classification, publication, provenance, and repair facts cannot override that direct result.

#### C.37:5.3 - One decision now and a later reader's need

In a constructed retention variant of section 5.1, the engineer completes the current comparison using the three independently qualified inputs. The direct receiving result and material limits are already clear: the description supplies proposed order, the plan supplies intent rather than performed Work, and the earlier record supplies only its comparability-limited observation. If no later use needs another account of this comparison, the answer is complete without a standalone C.37 record. Required source and receiving-result evidence remain under their own governors.

Now suppose a later trial reviewer must reconstruct why those particular inputs were usable for WP4. That use needs the exact claims, source and reliance boundaries, losses, dispositions and receiving result—not merely “MC7 selected.” Retain the complete basis in the existing same-use decision account if it can carry it, otherwise in one identifiable account. A new receiving decision still requires its own use-bounded selection; the retained earlier basis is not authority for the new action.

### C.37:6 - Bias-Annotation  *(informative)*

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Ontological | Repeated use of diagrams, tables, and records motivates a universal representation kind or relation. | Keep each candidate under its direct kind and relation; C.37 governs only the one-use selection move. |
| Epistemic | Selected means true, sufficient, or assured. | State the exact claim, A.10 disposition when material, unsupported use, and any separately current B.3 assurance claim. |
| Decision | The account is mistaken for the receiving choice, permission, authorization, or gate result. | Name the direct receiving-result governor and its actual result. |
| Structural | Co-used rows appear to form one integrated whole. | Treat co-use as a shared action key only; open collection, structure, construction, or coherence claims separately. |
| Didactic | A large form replaces the recognizable action. | Start with one receiver, one action, and one row; add a field only when it changes selection or return. |

### C.37:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-C37.1` One receiving use | Every row names the same receiving System and exact action or decision. Another action starts another account. |
| `CC-C37.2` Direct exit tested | The account is absent when one direct pattern already supplies the complete one-result/one-use selection and limits. |
| `CC-C37.3` Direct subject result | Each row identifies the candidate, subject, direct governor, and every positive relation required by the selected claim. |
| `CC-C37.4` A.2.4 bounded | First evidence-use or status-use classification is optional and never substitutes for provenance, reliance, or action authority. |
| `CC-C37.5` A.10 bounded | When evidence reliance is material, the exact claim, path, direct use relation, time/currentness boundary, bounded evidence use, unsupported attempted use, challenge when current, current `RelianceDisposition`, and reopen or stop condition are recoverable. |
| `CC-C37.6` Receiving result separate | The direct choice, gate, permission, authorization, acceptance, or domain pattern supplies the action result. |
| `CC-C37.7` Exposure and loss | Each selected or declined claim states what is exposed or preserved and what is withheld, lost, transformed, or uncertain. |
| `CC-C37.8` Honest disposition | Each row is `select`, `decline`, or `unresolved`; `degrade` narrows the selected claim rather than creating another row vocabulary. |
| `CC-C37.9` Return visible | Every row names the source or direct pattern and the condition that reopens selection. |
| `CC-C37.10` Co-use bounded | Joint use means only reliance by the same receiver for the same action; no collection, structure, view family, graph, or integrated world account is inferred. |
| `CC-C37.11` Use-needed retention | An immediate sufficient selection can finish without another record. When a later use needs the complete basis, it is recoverable once in an owning same-use result or one ordinary C.2.1 episteme, never both. |
| `CC-C37.12` Assurance progressive | B.3 is opened only for an actual named assurance claim; reversible inspection carries no mandatory assurance burden. |
| `CC-C37.13` No universal ontology | No `U.Representation`, universal `RepresentationOf`, fixed representation taxonomy, master mediation route, or public account kind is introduced. |

### C.37:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Best representation overall | A candidate is ranked without a receiver, action, exact claim, or tolerated loss. | Start a one-use account and compare only claims that can change that action. |
| Evidence-use classification as warrant | A.2.4 is treated as a positive reliance or authorization result. | Add A.10 only when reliance is material and keep the direct receiving result separate. |
| Provenance as decision | A current source or authentic carrier is treated as a positive choice or permission result. | Use provenance only inside the exact bounded path; require the direct choice, gate, permission, or domain result. |
| Publication as representation authority | A published diagram is accepted because it is available and readable. | Recover the direct subject result, any exact conformance or correspondence, and the relied-on claim; E.24.PUB supplies availability only. |
| Co-use as composition | Several rows become a collection, structure, integrated view, or graph by adjacency. | Keep independent rows; open C.13, A.22, E.17.0, C.29, or a domain integration pattern only for an additional named claim. |
| Duplicate account | A completed immediate choice is made to create an unused record, or an owning result and standalone episteme repeat the same claims. | Retain the complete basis only for a use that needs it; embed once in the same-use owner when available, otherwise use one identifiable account. |
| Cross-use carryover | A row selected for one decision is silently reused for tailoring, learning, maintenance, or another action. | Start another account and re-evaluate direct result, loss, path, disposition, and receiving result. |
| Diagram-first ontology | What exists or what happened is inferred from a graph, table, card, or route shape without the direct subject result. | Recover the direct object and relation first; then state the exact representation use or `none`. |

### C.37:9 - Consequences

The gain is a small, repeatable bridge from heterogeneous results to one practical action. A practitioner sees exactly why each candidate may be used, what it cannot support, and where the decision must return when sources, conditions, or reliance change. Domain results remain authoritative and can embed the claim group without duplicating it.

The cost is disciplined incompleteness: some attractive candidates remain declined or unresolved because publication, provenance, classification, or visual form cannot supply a missing direct result. That cost is preferable to an account that looks integrated while borrowing warrant across incompatible layers.

### C.37:10 - Rationale

The receiving use is the smallest stable boundary shared across domains. Representation kinds, correspondence relations, view predicates, plan claims, Work records, mathematical objects, and decision results do not converge on one ontology, but practitioners repeatedly need the same action sequence over them: recover the direct result, state the relied-on claim and loss, test bounded reliance when material, obtain the receiving result, and select, decline, or stop.

`Co-use` is chosen instead of *composition* because the rows need not form a new whole. The same receiver may use them together while every candidate and relation retains its own identity, predicate, and return condition.

### C.37:11 - SoTA-Echoing  *(informative)*

| Source line and status | Adopted move | Rejected overread |
| --- | --- | --- |
| Dutilh Novaes, *Formal Languages in Logic* (2012), and Krämer, “Why notational iconicity is a form of operational iconicity” (2017), conceptual and diagrammatic-reasoning lineage already used by C.2.1 | Representation and notation can change what users can inspect, compare, calculate, or infer; each row therefore states exposure, loss, and bounded use. | Reasoning affordance does not identify the represented subject, make a direct relation obtain, or authorize the receiving action. |
| [W3C PROV-O Recommendation](https://www.w3.org/TR/prov-o/), 2013, stable provenance lineage used by A.10 and C.2.1 | Preserve exact source, entity, activity, and derivation distinctions when they are material to bounded reliance. | Provenance alone is not truth, currentness, permission, assurance, decision, or evidence of actual use. |
| [Decision Theory, Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/archives/fall2023/entries/decision-theory/), stable baseline used by C.11 | Fix the chooser, option or action question, comparison basis, and explicit receiving result rather than ending with an informed-looking inventory. | C.37 does not replace C.11 or turn every representation-selection question into one universal decision calculus. |

Reopen this source use when newer representation, provenance, view, or decision practice supplies a lower-effort way to keep the same direct-result and receiving-action boundaries, or when real interoperability requires a common standalone account kind that cannot preserve them through ordinary C.2.1 identity and direct references.

### C.37:12 - Relations

- **Builds on:** `C.2.1` for any standalone account episteme and for the identity of claim-bearing candidate results.
- **Coordinates with:** the direct pattern governing each candidate's subject result; `A.2.4` for optional first evidence-use or status-use classification; `A.10` for evidence-provenance and bounded reliance; and the direct choice, gate, permission, authorization, acceptance, or domain pattern for the receiving result.
- **Coordinates with:** `E.17.0` for view conformance, `C.29` for mathematical-lens use, `E.24.PUB` for publication, `A.6.3.RT` for representation transitions, `A.22` for selected structure, `C.13` for construction and collection boundaries, and `C.2.P.DR` for declarative-representation overread repair.
- **Used by:** domain patterns only when differently governed candidate results must support one exact receiving action and the direct one-result/one-use path is not already complete.

### C.37:End

