## A.6.RCD - Needed Relation Claim Derivation and Relation-Kind Admission

> **Type:** Kernel relation-foundation pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain name.** Derive the needed relation claim before admitting a relation kind.

### A.6.RCD:0 - Use This When

Use this pattern when an engineer can name the exact participant referents and the claim, check, decision, or continuation that is blocked, but no current direct relation states the needed relation-bearing claim.

Typical first-minute situations are:

- several governed relation facts seem to imply the needed claim, but `related to` or a convenient verb hides how;
- a formula, query path, graph edge, or rule appears to define the answer, and the team is about to treat it as a relation kind;
- the same compound claim recurs and the team needs to decide whether to keep deriving it locally, publish reusable predicate semantics, or admit a relation kind;
- a proposed primitive relation appears to be only a composition, projection, closure, aggregation, or cross-algebra juxtaposition of existing claims.

**Primary EntityOfConcern.** One exact needed relation-bearing claim for one named receiving use. The application also settles whether that claim remains local, receives a reusable predicate-definition episteme, or justifies a derived or primitive relation kind. This wording does not mint a `NeededRelationClaim` kind or an application-record kind.

**First useful move.** Write the blocked receiving use and the participant meanings in ordinary domain language. Then use `A.6.P` to verify that no current direct relation already closes the claim.

**What goes wrong if missed.** A team either leaves the claim as vague connective prose or promotes a formula, query, graph path, definition, or convenient name into ontology. The first loses replayable meaning. The second invents relation kinds without an obtaining law or occurrence identity.

**What this buys.** The engineer gets the lightest sufficient result: an existing direct relation, a local compound claim, reusable predicate-definition content with an optional separately admitted derived relation kind, or a genuinely irreducible primitive relation kind. The ontology grows only when the receiving use needs occurrence semantics that claim content alone cannot supply.

**Ordinary non-use boundary.** Do not use this pattern when a current direct relation already states the needed claim; use that direct pattern and stop. Do not use it for wording-only cleanup, mathematical-lens adequacy, naming, evidence, assurance, or publication questions. `E.10`, `C.29`, `F.18`, `A.10`, `B.3`, and `E.17` govern those questions respectively.

**Cheap stop.** If a readable current direct relation closes the receiving use, stop before constructing a compound claim. If a local compound claim closes it, stop before publishing a reusable definition. If a reusable definition closes it, stop before admitting a relation kind.

### A.6.RCD:1 - Problem Frame

FPF permits rich claims over already governed entities and relations without requiring one primitive relation kind for every useful sentence. The difficult case begins after relational precision restoration: the participants are recoverable, the receiving use is real, and simpler direct relations exist, but no one current direct relation carries the needed claim.

The ordinary result of this pattern is claim content in a `C.2.1` episteme. Deriving that content is not the constitution of an actual relation occurrence. Repeated use can justify reusable predicate-definition content. Only a further occurrence-semantics need can justify a derived relation kind, and only irreducible action-facing semantics can justify a primitive relation kind.

### A.6.RCD:2 - Problem

Two errors compete.

1. **Under-definition.** `Related to`, `fulfils`, `enacts`, `reachable`, `supports`, or another convenient phrase hides the base facts, participant meanings, polarity, intermediate participants, applicability, or rule by which the claim follows.
2. **Premature admission.** A repeated expression, formula, query, graph path, table row, definition, or name is treated as a relation kind or relation occurrence although no direct subject settlement states obtaining and occurrence identity.

Authors MUST preserve expressive claims while preventing representation-created ontology and primitive-kind inflation.

### A.6.RCD:3 - Forces

| Force | Tension to resolve |
| --- | --- |
| Exact semantics vs readable use | Authors MUST make each conforming derivation replayable without making every practitioner read formal notation. |
| Local affordability vs repeated reuse | One local claim should stay cheap; repeated semantics should not be copied inconsistently. |
| Expressive claims vs small ontology | FPF should permit compound truths without minting one kind per compound predicate. |
| Reuse vs hidden dependencies | Reusable definitions need visible base-relation and substrate editions. |
| Truth conditions vs occurrence semantics | A predicate can be satisfied without supplying a way to reidentify relation occurrences. |
| Formal power vs substrate authority | Constructor names are available only where the selected substrate gives them semantics. |
| Mathematical representation vs ontology | A formula, path, graph, or query can represent a rule without making that rule obtain in the world. |

### A.6.RCD:4 - Solution

Name the blocked receiving claim and participants. Reuse a current relation when it suffices. Derive only what the selected substrate warrants. Publish reusable predicate semantics only for repeated subject use. Admit a relation kind only with its direct obtaining and occurrence-identity laws. Stop when the receiving use works.

#### A.6.RCD:4.1 - Execute the demand-first method

1. **Name the receiver.** State the exact claim, check, decision, or continuation that cannot proceed, and what answer would close it.
2. **Recover participants and direct relations.** Use `A.6.P` to name the actual participant referents under their relation-participant meanings and retrieve the smallest plausible base from direct governing patterns and their obtaining laws. Similar tokens, shared field names, or adjacent graph edges are not a base.
3. **Choose the least constructor admitted by the current substrate.** State the constructor semantics and the base claim content it consumes. Do not infer an operator from punctuation or notation.
4. **Replay three things.** Test one positive case, one discriminating failure case, and the named receiving use. Keep hidden intermediates, polarity, scope, time, and base-definition editions visible when they change the result.
5. **Select the lightest disposition.** Choose exactly one of the four dispositions in section 4.3 and stop at its stopping rule.
6. **Open reusable semantics only when repeated subject use needs the same rule.** Identify one truthful `C.2.1` `EntityOfConcern`, state participant meanings, derivation, applicability, and dependencies, and keep the definition distinct from a `RelationSignature`.
7. **Open kind admission only when occurrence semantics are consumed.** A derived kind needs a direct subject settlement with obtaining, applicability, base dependencies, and a non-optional occurrence-identity rule. A primitive candidate additionally carries the failed derivation, the exact action-facing distinction lost, its own obtaining and recurrence laws, independent receiving uses, and a standalone governing-pattern obligation.

Use this compact working note only while the decision is live:

```text
A.6.RCD working note:
  blockedReceivingUse:
  participantMeanings:
  candidateBaseRelationClaims:
  selectedSubstrateAndEdition:
  constructorSemantics:
  positiveCase:
  discriminatingFailureCase:
  receivingUseReplay:
  disposition:
  predicateDefinitionEntityOfConcernIfCurrent:
  directSubjectSettlementIfKindCurrent:
  stopOrReturn:
```

The note is a pattern-local prompt. A filled, claim-bearing use is an episteme under `C.2.1`; the printed shape is not a new record kind, `RelationSignature`, relation kind, or relation occurrence.

#### A.6.RCD:4.2 - Respect substrate authority

A constructor probe is usable only when the selected substrate defines its inputs, output claim, applicability, and relevant laws. The following table is a non-exhaustive set of recurring single-substrate semantic probes. It is neither a universal operator registry nor a claim that any substrate supports the whole list.

| Recurring single-substrate semantic probe | Minimum semantics to recover | Boundary |
| --- | --- | --- |
| typed restriction | the base predicate, restricted participant kind or condition, and scope | a narrower claim is not automatically a new relation kind |
| participant permutation or converse | participant correspondence, polarity, and whether the direct subject ontology treats the inverse reading as the same occurrence | syntax does not decide occurrence identity |
| composition | the two or more base predicates, exact shared participant, order or direction, and intermediate witness policy | a hidden intermediate does not disappear from semantics because a query projects it away |
| projection | the source claim, retained participants, hidden participants, and existential or other projection law | projection can yield claim content without yielding an occurrence-identity rule |
| conjunction | all conjuncts, their common applicability, and one truth condition for the compound claim | co-truth does not create a cross-subject relation kind |
| negation or complement | the substrate's closed-world, open-world, constructive, probabilistic, or other negation law | absence of a base assertion is not automatically a negative relation fact |
| transitive or path closure | admitted edge relation, direction, path rule, zero-length policy, cycle policy, and subject structure | a graph path is a representation or witness; it is not the obtaining relation occurrence |
| aggregation | the population or collection, grouping rule, aggregated value, aggregation operator, empty or duplicate treatment, scope, and applicability | an aggregate or scalar summary does not silently become a relation predicate or occurrence |
| probabilistic operator | the event or sample space, random variables or events, probability operator or model, conditioning, threshold or decision rule, applicability, and uncertainty boundary | a probability, likelihood, or posterior does not silently become a relation predicate, and shared event labels do not bridge algebras |

**Cross-algebra claim-use boundary.** An explicit direct subject rule governs every joint receiving use of separately derived claims from different algebras, whether the use stays within one `U.BoundedContext` and one ReferencePlane or crosses contexts or planes. That rule states which claims are used and for what receiving use; it does not thereby define a cross-algebra constructor, a new predicate, or a relation occurrence. When the joint receiving use additionally depends on sense alignment across `U.BoundedContext`s or ReferencePlanes, authors MUST cite, in addition to that direct rule, the applicable `F.9` Bridge id, `CL`, Loss Notes, admitted-use statement, and the applicable ReferencePlane policy pin when planes differ. F.9 governs the declared alignment and its admitted cross-context use; it does not create the receiving-use relation, decision use, predicate, or relation occurrence. Any assurance penalty from that crossing reduces only `B.3` `R_eff`; it does not change `F` or `G`. One local same-context and same-plane joint use, one local single-substrate derivation, and bounded SoTA comparison require no fictitious Bridge.

A local compound claim needs recoverable constructor semantics, but it does not need a separately materialized substrate document. Authors MUST name and pin the substrate when the derivation is nontrivial, intended for interoperability, used as proof, or becomes a reusable predicate definition. If no current substrate supplies the proposed operator, return a missing-substrate blocker rather than improvising a universal constructor algebra.

#### A.6.RCD:4.3 - Select one of four dispositions

| Disposition | Test | Result | Stop |
| --- | --- | --- | --- |
| **1. Existing direct relation** | One current direct relation already has the needed participant meanings, obtaining condition, applicability, and receiving-use meaning. | State the readable direct claim under that pattern. | Stop. Do not derive a synonym predicate or duplicate relation kind. |
| **2. Local compound relation-bearing claim** | A substrate-admitted composition of governed base predicates closes this one receiving use, and no repeated definition or occurrence semantics is needed. | Put positive or negative compound claim content in one identified `C.2.1` episteme. An unresolved information-sufficiency or reliance assessment stays with the evaluation or evidence pattern; it is not a third predicate value. | Stop. Introduce no relation kind, `RelationSignature`, or `U.Relation` occurrence. |
| **3. Reusable predicate semantics, with derived-kind continuation only when needed** | Several uses in one direct subject practice need the same parameterized rule. | Publish one predicate-definition episteme. If those uses also need stable relation-occurrence semantics, return a derived-kind candidate plus its proposed direct subject settlement covering obtaining, applicability, base dependencies, and occurrence identity; route that candidate to `E.24` and `E.24.UK`, and to `A.11` when parsimony is current, for admission. | Stop at the definition unless occurrence semantics are named and the proposed settlement is supplied. A definition is not a kind; neither the proposal nor its direct subject pattern admits the kind. The route to `A.6.0` declaration opens only for an admitted result. |
| **4. Primitive relation kind** | Every accepted derivation loses one exact action-facing distinction, and the candidate has independent receiving uses plus its own obtaining, recurrence, applicability, and occurrence-identity laws. | Carry the candidate to `A.11`, `E.24`, and `E.24.UK`, and author a standalone direct subject pattern. | Stop or block if the failed derivation, lost distinction, independent use, direct pattern, or identity law is absent. A convenient name never passes this test. |

These are economy dispositions, not maturity stages. Later need can reopen a local claim or definition. The four dispositions do not impose a required maturity ladder on any application.

#### A.6.RCD:4.4 - Keep the governed objects distinct

| Object | What it is | What it is not |
| --- | --- | --- |
| existing direct relation occurrence | one obtaining `U.Relation` occurrence under its direct pattern | not its assertion, signature, identifier, or graph edge |
| local compound relation-bearing claim | claim content in one `C.2.1` episteme, asserting or denying satisfaction of a substrate-admitted compound predicate | not a relation kind and not a relation occurrence |
| reusable predicate-definition episteme | one `C.2.1` episteme in the direct subject pattern whose claims define parameterized predicate semantics | not a `RelationSignature` and not a classifier of relation occurrences |
| admitted derived relation kind | a classificatory distinction over relation occurrences, with obtaining defined through governed base relations | not the definition episteme; it needs its own direct subject settlement and identity rule |
| admitted primitive relation kind | a classificatory distinction whose needed action-facing semantics cannot be preserved by accepted derivation | not a reward for a familiar word or notation |
| claim or derivation representation | formula tokens, formula trees, query paths, graph elements, tables, diagrams, or other `C.29` representation elements | not satisfaction, obtaining, admission, or occurrence identity |
| designator or governed reference | a name or reference associated with an already settled definition episteme, relation kind, or individuated occurrence | not one token that silently creates or identifies all three |

#### A.6.RCD:4.5 - Settle a reusable predicate definition truthfully

A reusable predicate-definition episteme has one exact `C.2.1` `EntityOfConcern`. State what the definition claims about that value and why the repeated subject uses concern it. The `EntityOfConcern` can be a promise-content edition, a subject structure, a governed decision-work occurrence, or another exact subject value when that is truthful for the case. It is not a union of every participant, base assertion, formula, receiver, and publication that appears nearby.

Its content states:

- parameter and participant meanings;
- the exact base-relation claims and their direct governing patterns;
- the derivation rule under the selected substrate;
- polarity, scope, time, and applicability;
- base-definition and substrate dependencies plus their editions when current;
- positive and discriminating cases;
- the admissible claim use and the non-admissible occurrence or ontology overread.

If no single truthful `EntityOfConcern` can be selected, keep the needed results as local compound claims. Do not manufacture a union concern to make the definition publishable.

#### A.6.RCD:4.6 - Prepare derived or primitive relation-kind admission only with occurrence semantics

When a named receiver consumes occurrence semantics, A.6.RCD returns a relation-kind candidate and the settlement material needed for admission: a derived-kind candidate plus its proposed direct subject settlement, or a primitive-kind candidate plus its candidate standalone direct pattern. `E.24` and `E.24.UK` decide admission; `A.11` decides parsimony when that question is current. Neither a proposed settlement nor a candidate direct pattern admits the kind. For a candidate that is admitted, the resulting direct subject settlement states:

1. the classified relation occurrences and exact participant meanings;
2. the obtaining predicate and applicability;
3. for a derived kind, the exact derivation law and base-definition dependencies;
4. a direct occurrence-identity rule that distinguishes repetition;
5. recurrence, cessation, and continuation conditions when those distinctions matter;
6. at least one named receiving use that consumes occurrence semantics;
7. the standalone direct governing pattern.

An admitted relation kind never has `identity intentionally absent`. Ordinary use can omit explicit individuation, occurrence records, and designators because no receiver consumes them; the direct identity rule still exists.

A pure converse preserves one base occurrence only when the direct subject ontology explicitly says that inverse wording concerns the same occurrence. Restriction, projection, composition, closure, aggregation, and hidden intermediates require an explicit identity decision. Their syntax does not decide whether the derived occurrence inherits one base identity, is constituted as a composite occurrence, or has a new direct identity rule. If no truthful rule is available, remain at local-claim or predicate-definition level.

Authors MAY publish under `A.6.0` a `RelationSignature` whose `EntityOfConcern` is that exact kind only after the kind is admitted. The signature declares reusable SlotSpecs and restates the direct laws; it does not admit the kind or make an occurrence obtain.

#### A.6.RCD:4.7 - Separate recognition from assurance

**Recognition branch for ordinary receiving use.** Ask only:

1. What receiving claim or action is blocked?
2. Who or what are the exact participants, and under which meanings?
3. Does one current direct relation already answer it?
4. If not, what smallest substrate-admitted compound claim answers it?
5. Which of the four dispositions lets the receiver proceed now?

The ordinary branch can stop at a readable direct claim or one readable compound claim. It does not require a named substrate document, predicate-definition publication, relation kind, signature, explicit occurrence, or designator when the receiving use consumes none of them.

**Assurance branch for DPF and FPF authors.** DPF and FPF authors use this branch whenever they author a compound claim, reusable predicate definition, or relation-kind admission candidate, including a durable local compound claim that stops at disposition 2. In addition, verify:

- exact base patterns, definitions, editions, and applicability;
- selected substrate and constructor semantics;
- positive case, discriminating failure case, and receiving-use replay;
- one truthful definition `EntityOfConcern` when reusable semantics are published;
- dependency and currentness conditions;
- direct occurrence-identity and recurrence rules for every admitted relation kind;
- representation correspondence without representation-to-world collapse;
- naming only after the exact definition episteme, kind, or occurrence is settled;
- evidence, assurance, gate, and decision claims under their own governing patterns.

Passing the assurance branch does not make evidence constitutive of relation obtaining. It makes the derivation and admission decision replayable for the declared use.

#### A.6.RCD:4.8 - Stop and return deliberately

Stop at the first disposition that closes the named receiving use. Return to this pattern when:

- a relied-on base relation or predicate definition changes;
- the selected substrate edition or constructor semantics changes;
- applicability, polarity, participant meaning, scope, time, or hidden-intermediate policy changes;
- the derivation becomes unreadable, computationally unsuitable, or unable to interoperate for the declared use;
- repeated consumers begin to need one reusable definition or stable occurrence identity;
- a purported primitive gains an accepted lossless derivation, or a derived kind loses a truthful identity rule.

`G.11` governs currentness, dependency closure, and scoped refresh when a relied-on base definition, substrate edition, or applicability settlement changes. Re-evaluate only affected claims and dependent kinds; do not rebuild a global relation registry.

### A.6.RCD:5 - Archetypal Grounding — Worked Cases

#### A.6.RCD:5.1 - Promise-content fulfilment: reusable predicate semantics, not automatic kind admission

**Situation.** Several delivery and acceptance uses ask whether one exact `U.PromiseContent` edition is fulfilled. No one convenient word should hide the governed delivery-work facts, affected-referent post-state facts, and acceptance predicate.

**Base and derivation.** Use the direct A.2.3 relations governing that promise content, the exact delivery-work and post-state claims, and the acceptance predicate. Publish one predicate-definition episteme whose `EntityOfConcern` is the exact promise-content edition. Its claims state how those governed facts satisfy that content under the declared applicability.

**Positive case.** The named delivery work occurred, the affected referent has the required post-state, and every acceptance condition of the current promise-content edition is satisfied.

**Discriminating failure.** The same delivery work occurred, but one required post-state or acceptance condition is false. Work occurrence alone therefore does not satisfy the fulfilment predicate. Missing evidence produces an unresolved reliance assessment; it does not create a third predicate value.

**Disposition and stop.** Disposition 3 stops at the reusable predicate-definition episteme. If a later receiving use needs fulfilment occurrences, A.6.RCD returns a derived fulfilment-kind candidate plus a proposed direct A.2.3 subject settlement that supplies obtaining, applicability, dependencies, and a direct occurrence-identity rule. `E.24` and `E.24.UK` decide admission, with `A.11` applied when parsimony is current. The route to `A.6.0` declaration opens only for an admitted result. `Only truth is needed` means no explicit individuation is consumed; it never means identity is absent from an admitted kind.

#### A.6.RCD:5.2 - Role enactment: one local compound claim

**Situation.** A work record needs the readable claim that a holder enacted an assigned role in one exact work occurrence.

**Base and derivation.** Recover the obtaining `U.RoleAssignment`, the holder's exact participation in the work, the work occurrence, and the direct relation that makes that work relevant to the assigned role. State the local compound claim in one `C.2.1` episteme whose exact `EntityOfConcern` is the `U.RoleAssignment` occurrence under concern; neither the work-record wording, holder, work occurrence, nor a union of nearby objects substitutes for that concern.

**Positive case.** The same admitted `U.System` that holds the role assignment participates in the qualifying work while the assignment obtains and the work satisfies the direct role-relevance condition.

**Discriminating failure.** The assignment obtains, but another system performs the work, or the named holder performs work outside the assignment or outside the relevant work relation. Assignment plus nearby work is therefore insufficient.

**Disposition and stop.** Disposition 2. Keep the readable local enactment claim; admit no universal `RoleEnactment` kind, occurrence, or `RelationSignature`. If a later subject pattern demonstrates repeated occurrence-semantics need, reopen that exact subject case rather than generalizing from the verb.

#### A.6.RCD:5.3 - Supply-chain reachability: query, reusable definition, and conditional kind boundary

**Situation.** A supply-chain practice repeatedly asks whether one exact participant is reachable from another inside one identified subject structure.

**Base and derivation.** Name the direct edge-relation kinds, direction, structure, path or closure rule, zero-length and cycle policies, applicability, and edge-definition editions. A one-off answer is a local compound claim. Repeated query semantics can be published in a predicate-definition episteme whose `EntityOfConcern` is the exact subject structure within which the questions are asked.

**Positive case.** A path exists whose every edge is an obtaining occurrence of the admitted base relation under the current structure and closure rule.

**Discriminating failure.** A graph representation contains a visual or stored path, but one edge points in the wrong direction, denotes a different base relation, or belongs to a superseded structure edition. Representation connectivity therefore does not satisfy the reachability predicate.

**Disposition and stop.** A one-off query stops at disposition 2; repeated semantics stop at disposition 3's predicate definition. If the subject practice later needs reachability occurrences with action-facing identity, recurrence, continuation, or participation in another relation, A.6.RCD returns a derived reachability-kind candidate plus a proposed direct subject settlement that supplies the direct occurrence rule. `E.24` and `E.24.UK` decide admission, with `A.11` applied when parsimony is current. The route to `A.6.0` declaration opens only for an admitted result. Path identity, query-result-row identity, and relation-occurrence identity are not interchangeable.

#### A.6.RCD:5.4 - Formal and probabilistic result use: preserve separate algebras

**Situation.** One engineering decision-work occurrence consumes one formal result episteme and one probabilistic result episteme.

**Base and derivation.** Keep the formal result in its formal substrate and the probabilistic result in its probability substrate. State the two separately governed result-use assertions in one `C.2.1` episteme whose exact `EntityOfConcern` is the engineering decision-work occurrence. The formal and probabilistic result epistemes remain distinct used results; neither their pair nor a union of nearby objects replaces that concern.

No `F.9` Bridge is needed for this case as stated: the two result epistemes enter the decision through separately governed direct use relations, while neither claim content nor algebraic meaning is transported across a `U.BoundedContext` or ReferencePlane or combined into one predicate.

**Positive case.** Both direct use relations obtain for the decision-work occurrence under their own applicability, so the decision rationale can cite each result for its admitted use.

**Discriminating failure.** The two results are co-published or mention the same subject, but the decision work has no governed use relation to one of them. Shared carrier, topic, or notation does not establish decision use.

**Disposition and stop.** The apparent combined need decomposes into two independently governed receiving claims. Each closes under disposition 1 with its exact direct decision-use relation. Do not publish a cross-algebra conjunction predicate merely to join the sentences, and do not infer one composite relation occurrence from a decision record.

#### A.6.RCD:5.5 - Primitive-candidate stop test

A subject practice proposes a primitive relation because all accepted bases preserve co-occurrence and shared participants but lose one independently used subject distinction. The candidate advances only when the subject can name that lost distinction, show a positive and discriminating case, state its own obtaining and recurrence laws, distinguish repeated occurrences, and identify independent receiving uses. If any item is missing, the honest result is a local claim, reusable predicate definition, or exact blocker. This is disposition 4's positive test, not a license to mint a placeholder relation.

### A.6.RCD:6 - Bias-Annotation
Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for applications of this pattern across FPF subject practices.

This pattern corrects primitive-kind bias: a useful repeated phrase or representation can look ontologically important before its governed claim and occurrence semantics are recovered. It also corrects false-parsimony bias: if every accepted derivation loses a distinction that changes real work and the subject supplies its own obtaining and identity laws, refusing the primitive would hide needed ontology.

The formal examples can bias authors toward syntax-first reasoning. The method therefore begins from the blocked receiving use, direct participants, and direct relations. The ordinary branch stays readable; formal apparatus appears only when it changes replay, reuse, proof, interoperability, or admission.

### A.6.RCD:7 - Conformance Checklist

1. **Blocked receiver.** The exact claim, check, decision, or continuation under repair is named.
2. **Participants first.** Actual referents and relation-participant meanings are recovered before constructor or notation choice.
3. **Direct-relation stop.** `A.6.P` verifies that no current direct relation already closes the claim before compound derivation begins.
4. **Governed base.** Every base predicate names its direct governing pattern and obtaining law.
5. **Substrate authority.** Every used constructor has semantics in the selected substrate; nontrivial, interoperable, proof-bearing, or reusable derivation pins the substrate and edition.
6. **Replay.** One positive case, one discriminating failure case, and the receiving-use replay agree.
7. **Lightest disposition.** Exactly one of the four dispositions closes the current use; later branches are not opened by habit.
8. **Claim polarity.** Positive and negative compound assertions concern predicate satisfaction; information sufficiency, support, or reliance is evaluated separately.
9. **Definition identity.** A reusable predicate-definition episteme has one truthful `C.2.1` `EntityOfConcern`, exact applicability, and visible base dependencies.
10. **Definition/signature boundary.** A predicate-definition episteme is not a `RelationSignature` and does not classify relation occurrences.
11. **Derived-kind candidate and admission.** When a named receiver needs stable occurrence semantics, A.6.RCD returns a derived-kind candidate plus a proposed direct subject settlement covering derivation and dependencies, obtaining, applicability, recurrence where current, and a direct occurrence-identity rule. `E.24` and `E.24.UK` decide admission; `A.11` decides parsimony when current. Neither the proposal nor its direct subject pattern admits the kind, and only an admitted result proceeds to `A.6.0` declaration.
12. **Primitive-kind settlement.** A primitive candidate records the failed derivation, exact action-facing loss, independent uses, own obtaining and identity laws, and standalone direct pattern before A.11/E.24/E.24.UK admission can pass.
13. **Identity never absent.** Explicit individuation can be omitted from ordinary use; an admitted relation kind's identity rule cannot.
14. **Representation boundary.** Formula, query, graph, tree, path, diagram, row, and name remain representations or designators connected to independently recovered content.
15. **Neighboring claims.** Evidence, assurance, gate, work, decision, publication, naming, and currentness use their direct governing patterns.
16. **Stop or return.** The result states the current stop and the exact dependency or use change that would reopen it.

### A.6.RCD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| `RelatedTo` as a universal fallback | Vague wording substitutes for participants and predicate. | Name the blocked receiver and derive the smallest governed claim. |
| Formula-as-fact | A formula tree or theorem token is treated as predicate satisfaction. | Recover the claim and its applicability; keep the formula under `C.29`. |
| Query-path ontology | A path match is treated as an obtaining relation occurrence. | Separate base-edge obtaining, closure semantics, query result, and any later occurrence identity. |
| Definition-as-kind | A reusable episteme is treated as a classifier of occurrences. | Keep its one `EntityOfConcern` and claim content; run separate derived-kind admission only for an occurrence-semantics need. |
| Kind-by-name | A good relation name is treated as admission evidence. | Use `F.18` only after the exact definition episteme, kind, or occurrence is settled. |
| Identity intentionally absent | An admitted kind has truth conditions but no occurrence identity because current prose does not expose occurrences. | Supply the direct identity rule or remain at claim or definition level. |
| Universal constructor algebra | Restriction, negation, closure, probability, and cross-algebra conjunction are assumed to mean the same thing everywhere. | Use only operators supplied by the selected substrate; return a blocker otherwise. |
| Hidden intermediate erased | Projection removes an intermediate from notation and therefore from semantics. | State the shared participant and witness policy even when the receiving claim projects it away. |
| Cross-algebra conjunction | Formal and probabilistic results are merged because one decision uses both. | Keep each algebra and direct decision-use relation separate. |
| Primitive by exhaustion | Failure to find a derivation is treated as proof of irreducibility. | Record the searched governed base, exact lost distinction, positive and failure cases, and direct identity law; otherwise keep an exact blocker. |

### A.6.RCD:9 - Consequences

**Benefits.** FPF can state many exact compound claims without multiplying primitive relation kinds. Repeated subject semantics become reusable without confusing a definition with ontology. When occurrence semantics really matter, derived and primitive relation kinds enter with direct obtaining and identity laws rather than with syntax or names.

**Costs.** Authors MUST expose base dependencies and substrate semantics for nontrivial reuse. Authors of a direct subject pattern MUST supply the additional settlement content required by section 4.6 before a relation kind is admitted. Some familiar relation words remain local claims or exact blockers.

**Boundary.** This pattern reduces public primitive kinds and duplicate declarations; it does not reduce the number of true compound claims or obtaining base-relation facts.

### A.6.RCD:10 - Rationale

Claim composition and relation-kind admission answer different engineering questions. A claim asks whether an exact predicate, possibly built from governed base predicates, is satisfied for named referents. A relation kind classifies obtaining occurrences and therefore needs a rule for reidentifying those occurrences. Repetition of the first question can justify publication of the predicate rule; it does not answer the second.

The demand-first order is deliberately asymmetric. Existing direct relations are cheapest because their subject patterns already own obtaining and identity. Local compound claims preserve expressive reach without public ontology cost. Predicate-definition epistemes prevent repeated derivations from drifting. Derived relation kinds add occurrence semantics only where receivers consume them. Primitive relation kinds remain available for irreducible distinctions rather than being prohibited by abstract minimalism.

### A.6.RCD:11 - SoTA-Echoing

| Practice or source line | What this pattern uses | What it rejects or bounds |
| --- | --- | --- |
| W3C [OWL 2 Structural Specification](https://www.w3.org/TR/owl2-syntax/) inverse object properties and property-chain axioms | Typed inverse and composition examples constrain the substrate-authority test in 4.2 and the supply-chain reachability case in 5.3: direction, shared participants, and the selected chain law remain explicit. | An OWL axiom neither establishes FPF equivalence nor supplies world-side obtaining or occurrence identity; case 5.3 still stops at a local claim or predicate definition unless the subject practice separately supplies occurrence semantics. |
| [Alloy language reference](https://alloytools.org/spec.html) relational restriction, transpose, join, product, union, difference, and closure | This mature explicit-operator substrate constrains 4.2 and the supply-chain reachability replay in 5.3, including direction, closure, zero-length, and cycle policy. | Alloy syntax is not a universal FPF constructor algebra and does not admit relation kinds; case 5.3's kind branch remains stopped until a direct subject practice supplies action-facing occurrence semantics and identity. |
| W3C [SPARQL 1.1 Property Paths](https://www.w3.org/TR/sparql11-property-paths/) | Query-local path and closure semantics for the reachability worked case. | A successful path query is not an obtaining relation occurrence and its result-row identity is not occurrence identity. |
| Florio and Linnebo, [Introduction to Constructional Ontology](https://www.utwente.nl/en/eemcs/fois2024/resources/papers/florio-linnebo-introduction-to-constructional-ontology.pdf), 2024, and Borgo and Righetti, [Towards Applied Constructional Ontology](https://doi.org/10.3233/FAIA250480), 2025 | Their constructor, input, process, and output-identity distinctions are adapted as a discriminating probe for the occurrence-semantics gate in 4.6 and the primitive-candidate stop in 5.5: authors MUST state in the candidate's direct subject rule which construction is identity-bearing. | A construction description or inherited source category neither constitutes FPF work or a relation occurrence nor admits a relation kind; 5.5 remains stopped until the direct subject practice supplies its own obtaining and identity law. |
| Chris Partridge, [BORO Ontology](https://borosolutions.net/boro-ontology), C-FORS 2025 presentation; current bounded extensional comparator | Its temporal-extent, recurrence, and ontology-evolution pressure is adapted for the occurrence-identity requirements in 4.6 and the primitive-candidate stop in 5.5: a temporal gap distinguishes repeated occurrences only when the direct subject rule adopts that discriminator. | FPF rejects universal 4D identity, unrestricted composition, and BORO category architecture. Reopen this bounded comparison if a later BORO edition or a direct FPF identity rule changes whether temporal extent is action-relevant for the 4.6/5.5 stop. |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint relation-reification comparison | Its differentiated relational-aspect and reification patterns stress the object boundary in 4.4 and the occurrence-identity and primitive-candidate stops in 4.6 and 5.5. | FPF adapts those distinctions as a current comparison but rejects an OWL class, property, reifier, or imported category hierarchy as proof of obtaining or occurrence identity; the candidate remains stopped until its direct subject rule supplies both. |

Reopen these source-use decisions when a selected substrate changes its operator semantics, a newer practice invalidates one of the representation boundaries, or a direct FPF relation pattern supplies a more action-capable derivation or identity rule without worse ontology truth, reader use, or modeling cost.

### A.6.RCD:12 - Reopen Conditions

Reopen the exact affected disposition, not the whole relation foundation, when:

- a base relation definition, participant meaning, obtaining law, or applicability changes;
- a substrate edition changes a constructor used by the claim;
- a local claim recurs enough to need one stable definition;
- a reusable definition gains or loses a truthful single `EntityOfConcern`;
- a receiver begins or ceases to need stable occurrence identity;
- an admitted derived kind loses a base dependency or identity rule;
- an admitted primitive gains a lossless derivation or loses its independent action-facing use;
- repeated reader error shows that the definition, kind, occurrence, representation, or designator is being confused.

### A.6.RCD:13 - Relations

- **Entered from:** `A.6.P` only after exact participants are recovered and no current direct relation closes the named receiving claim.
- **Builds on:** `A.6.REL` for relation obtaining and occurrence identity; `A.6.5` for participant declaration discipline; `C.2.1` for local claims and predicate-definition epistemes; and the direct subject patterns supplying base relations.
- **Coordinates with:** `A.11`, `E.24`, and `E.24.UK` for parsimony, ontic settlement, and durable admission; `A.6.0` for `RelationSignature` only after relation-kind admission; `C.29` for derivation representations; `F.9` for Bridge id, `CL`, loss, admitted-use, and plane-policy discipline when claims cross contexts or ReferencePlanes; `B.3` for any resulting `R_eff`-only assurance penalty; `F.18` for names and designators after settlement; and `G.11` for dependency currentness and scoped refresh.
- **Does not replace:** direct subject relation patterns, `A.6.P`, `E.24.UK`, `C.29`, `F.18`, evidence or assurance patterns, or work and decision patterns.

### A.6.RCD:End

