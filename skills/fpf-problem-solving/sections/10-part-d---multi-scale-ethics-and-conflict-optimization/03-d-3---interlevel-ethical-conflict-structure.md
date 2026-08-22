## D.3 - Interlevel Ethical Conflict Structure

> **Type:** D-family ethical conflict-description pattern
> **Status:** Stable
> **Pattern role:** This compact pattern helps a practitioner make an interlevel ethical conflict inspectable and identify the result as an `InterlevelEthicalConflictDescription` episteme. Use D.4 for mediation and decision use, D.5 for bias, fairness, impact, and ethical assurance, C.28 for causal claims, and C.30.ILC for architecture residuals.

**Use this when.** Use this pattern when ethical claims at different declared levels or scopes cannot all be met as stated, and their tension must be clear before mediation, decision, assurance, or architecture work. State an ethical concern as the claim that makes it current in this case.

**Not this pattern when.** If only the ethical value frame is missing, use `D.1`. If only entry recognition is needed, use `D.2`. If D.3 has already described the conflict and the current question is mediation or decision use, use `D.4`. If the question is bias, fairness, impact audit, causal-fairness audit consumption, or ethical assurance, use `D.5`.

**What goes wrong if missed.** The team debates values or decisions before it can say who or what is affected, under which value frame and scope, over what horizon, and why the live claims are in tension.

**What this buys.** A reader can see each side, what it affects, and how the sides are in tension before deciding what to do. The same description can later support work under `D.4`, `D.5`, evidence, causal, assurance, or architecture patterns without turning its table or file into the conflict itself.

### D.3:1 - Problem Frame

Interlevel ethical conflict is not just disagreement between people. It may involve a system part and a whole, a person and an organization, one organization and a community, a project and a society, a collection and its members, an episteme family and the decisions it shapes, or an architecture move and the holon levels it affects. The case supplies its levels and scopes; D.3 does not impose a universal moral ladder.

The practical problem is connecting each claim to what it affects. A list of affected entities, values, Methods, Work, evidence, and horizons does not show which claim concerns which entity or why two sides cannot both be satisfied. D.3 therefore records each side as one connected statement and then records the tension among the sides.

The reusable result is a description episteme, not the conflict in the situation and not the form used to show it. The phrase *conflict structure* remains useful ordinary shorthand for the connected claim content inside that description. It does not name a new public `U.*` kind or a generic direct relation.

### D.3:1.0 - Problem

An ethical conflict is often argued before it is described. The affected objects, scopes, value frames, claimed benefits and harms, evidence limits, and consequence horizons remain implicit, so mediation begins from slogans rather than from inspectable claims.

### D.3:1.1 - Forces

| Force | Tension |
| --- | --- |
| Conflict description vs. decision use | The sides and their tension must be inspectable before D.4 can mediate, refuse, or support a bounded decision. |
| Level and scope plurality vs. fixed ladder | A case may involve persons, teams, organizations, communities, systems, epistemes, or environments without one universal hierarchy. |
| Conflict vs. description | A narrative, table, graph, or formal expression can describe the conflict but is not the situation, claims, harms, or relations it describes. |
| Cheap first result vs. reusable precision | Most cases first need two clear sides and one tension statement; later reuse may need an identified episteme and typed supporting relations. |
| Agency evidence vs. responsibility | Evidence may support an agency characteristic or threshold. Responsibility still needs its own direct predicate and actual participants; no score, label, collection name, or assignment supplies it. |
| Architecture residual vs. ethical conflict | A cross-scope structure can be architectural, ethical, or both. `C.30.ILC` triages the architecture residual; D.3 describes the ethical conflict. |

### D.3:2 - Solution

#### D.3:2.1 - First useful result

Start with two sides and one tension statement. For each side, write:

1. the ethical claim that states the concern in ordinary language;
2. the exact affected entity;
3. the declared level relation, claim scope, or Work extent that locates the concern;
4. the value-frame edition under which the consequence matters;
5. the expected benefit, harm, or constraint and its consequence horizon; and
6. the evidence use or uncertainty only when the side currently relies on it.

Then say why the sides cannot both be met as stated, what would be traded, or why they remain in unresolved tension. Name the next live use: mediation, refusal, a decision, an evidence or causal question, assurance, or architecture return. Stop there when this makes the conflict inspectable for that use.

This first result can remain a short working note. It does not need a schema, publication, assurance package, responsibility model, or complete account of every participant.

#### D.3:2.2 - Reusable conflict description

When another reader or later use must cite, compare, revise, or publish the result, identify one `InterlevelEthicalConflictDescription`. This is an ordinary local name for one C.2.1 `U.Episteme`, not a newly admitted `U.*` kind.

Apply the C.2.1 identity test:

- **EntityOfConcern:** one exact entity already recovered for the case, such as the plan, proposed system change, or decision situation whose ethical tension is being described. Do not use a loose bundle of several possible subjects.
- **ClaimGraph:** the exact claim content containing the conflict sides, their tension, and the next-use question. When those claims are explicitly restricted to part of the situation, it also identifies the description's ClaimScope.
- **effective ReferenceScheme:** the designation, interpretation, measurement, comparison, and evaluation rules needed to read those claims.

Changed claim content, EntityOfConcern, or effective ReferenceScheme identifies another episteme. Say that a later description revises or supersedes an earlier one only when an exact C.2.1 `EpistemeEditionRelation` is asserted. A changed narrative, table layout, publication form, carrier, or publication occurrence does not by itself change the episteme.

Use this compact content shape when a reusable record helps:

```text
InterlevelEthicalConflictDescription — C.2.1 identity:
  entityOfConcernRef
  claimGraph:
    descriptionClaimScopeRef?
    conflictSides: at least two rows
      - sideId
        ethicalClaim: plain statement that identifies the claim; add a ClaimAddress only when reusing an existing claim
        affectedEntityRef
        declaredLevelRelationRef?
        sideClaimScopeRef?
        affectedWorkExtentRef?
        valueFrameEditionRef
        expectedConsequence: what changes and why it counts, for example, as a benefit, harm, or constraint under that value frame
        consequenceHorizon
        evidenceUseRef?
        uncertaintyStatement?
    tension:
      sideIds
      plainStatement
      directRelationDefinitionRef?
      obtainingRelationOccurrenceRef?
      missingGovernorRef?
    nextUse: plain statement; cite a question episteme only when another use needs that identity
  effectiveReferenceSchemeRef
```

When present, `descriptionClaimScopeRef` identifies the declared part of the situation covered by the whole description. Do not add it merely to complete the shape. A side's ClaimScope or Work extent says where that side applies; it never substitutes for the whole-description scope.

The `plainStatement` must name the exact incompatibility, trade-off, parity, or other tension claimed among the sides. In an ordinary case, it remains claim content in the description. If a receiving use relies on a separately obtaining direct relation, cite the exact relation definition and occurrence with its participants, applicability, and identity. If no adequate governor exists, record the exact `A.6.RCD` missing-governor result. Merely filling a reference field never makes a direct relation obtain.

#### D.3:2.3 - Add detail only when it changes the conflict or its next use

| Open this branch when... | Add... | Keep separate... |
| --- | --- | --- |
| A Method is part of a side's claim. | the exact `U.Method` under A.3.1 and, when cited, its MethodDescription under A.3.2 | Method identity from any dated performance |
| Performance actually occurred. | the exact dated `U.Work`, performer System, Method, Work extent, and containing System under A.15.1 | a plan, intention, assignment, or capability from performed Work |
| Assignment matters. | the exact assignment species and its obtaining occurrence under A.2.1, with actual participants and applicability | assignment from performance, responsibility, permission, or authority |
| Role-shaped wording or classification matters. | one E.10.ROLE recovery, then the local kind and a separate C.2.1 classification assertion episteme under C.3.2 after the candidate passes its admissibility test | the word *role*, kind, assertion, assignment, and acting System from one another |
| Evidence changes a side or its uncertainty. | the evidence episteme and the exact A.10 evidence-use or reliance result | stored evidence from reliance on it |
| A transformation changes who benefits or is harmed. | the exact transformation occurrence under A.3.4 and its affected participants | a transformation description from the occurrence |
| Membership or part-whole structure matters. | the exact collection-membership or part-whole predicate and obtaining occurrence | a plural name from an acting or responsible System |
| Agency is disputed. | the exact Characteristic, Scale, threshold, and supporting evidence use | an agency reading from responsibility |
| Responsibility, permission, authority, commitment, or participation is claimed. | the exact relation definition and obtaining occurrence, or the exact A.6.RCD missing-governor result | the relation family from an occurrence; the occurrence from evidence for it |
| A calculation or formal comparison changes the tension. | the exact C.29 representation, its correspondence to the independently recovered objects, and the operation used | a formula or score from the ethical conflict or decision |
| Publication or audience use changes the ethical claim. | the selected episteme edition, publication occurrence, form, carrier, audience, and bounded use under E.17 and E.24.PUB | the published episteme from its form, carrier, publishing Work, and availability relation |
| A harm or benefit depends on causality, assurance, or architecture. | only the affected C.28, B.3, D.5, or C.30.ILC return | the conflict description from causal proof, assurance, or architecture selection |

Open no branch merely because the field exists. The detail must change a side, the tension, or the next receiving use.

### D.3:3 - Collection and Episteme Cases

A collection is ethically current only when whole-level characteristics, membership relations, environment-mediated effects, or aggregate consequences matter. Use `A.14` for part-whole and membership relations and `C.13` for constructive grounding. A plural or institutional name does not make the collection an acting or responsible System.

An episteme is ethically current when its claim content, source use, publication, described EntityOfConcern, or model use changes the affected systems or decisions. Use C.2.1 for episteme identity and exact edition claims, and E.17 with E.24.PUB for publication. The D.3 conflict description is a separate episteme about the selected case; it does not become identical to the policy, model, standard, or architecture description involved in one of its sides.

### D.3:4 - Boundaries

| Do this in D.3 | Do not do this in D.3 |
| --- | --- |
| Derive the declared levels and scopes from the case. | Invent `U.Level`, `U.Frustration`, `U.Emergence`, or a fixed moral ladder. |
| Connect every side's claim, affected entity, scope, value frame, consequence, and horizon. | Present flat bags of entities, values, evidence, and relations as if their connections were obvious. |
| Keep the conflict description, the situation it describes, and its narrative, table, graph, form, carrier, and publication separate. | Treat a file or diagram as the conflict, or treat description content as proof that a direct relation obtains. |
| Add Method, Work, assignment, classification, evidence use, agency, responsibility, publication, assurance, causal, or architecture detail only when current. | Require assurance-like apparatus before the first useful map exists. |
| Stop at an inspectable tension and next-use question. | Choose the compromise, refusal, override, or accepted residual; those are D.4 uses. |
| Use `C.30.ILC` when an architecture residual is also current. | Route every cross-scope architecture problem to ethics. |

### D.3:5 - Archetypal Grounding (Worked Slices)

**Minimal engineering record.** A consultant is asked to improve a surveillance project's effectiveness.

```text
Case: whether to accept the named consulting plan
Scope: the proposed consulting work and the intended deployment it would enable
Side A: the client receives more effective engineering advice; affected entity: client project;
        value frame: client delivery edition 3;
        consequence and horizon: near-term performance benefit during design.
Side B: the proposed capability increases foreseeable harm to monitored people;
        affected entity: the named affected population; value frame: project ethics edition 2;
        consequence and horizon: rights and safety harm over service life.
Tension: performing the plan would advance Side A by enabling the harm named in Side B.
Next use: D.4 refusal or conditions; C.28 first if the harm claim needs causal support.
```

This is enough to begin D.4 and does not decide who is responsible. If another reader must cite or revise the note, identify it as an `InterlevelEthicalConflictDescription` whose EntityOfConcern is the consulting-plan episteme. If consulting Work later occurs, add its A.15.1 basis. Add assignment, agency, responsibility, permission, or authority only through their independently obtaining relations or exact missing governors.

**Conditional collection record.** A fleet-wide maintenance change lowers cost but may raise failure risk for a small subfleet operating in harsh conditions. The description has a fleet-cost side and a harsh-service safety side, each with its affected entity, scope, value-frame edition, consequence, and horizon. Add the exact fleet-membership relation because it locates the subfleet. Add the reliability evidence episteme and A.10 evidence use because the safety side relies on them. Return the causal question to C.28 if the risk claim depends on the proposed change. None of those additions makes the fleet an acting or responsible whole; use A.1 for systemhood and the exact responsibility predicate for responsibility.

**Episteme record.** A published architecture description normalizes an interface assumption that excludes an alternative implementation. The EntityOfConcern of the D.3 description is the exact supplier-selection situation, not the architecture-description file. One side claims lower integration cost; the other claims unjust exclusion of affected suppliers under a named value-frame edition and horizon. Cite the architecture-description episteme and its publication or use only because that use carries the assumption into the decision. Use C.30.AD for description adequacy and use E.17 with E.24.PUB for publication; D.3 records the ethical tension that remains.

### D.3:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Debate replaces a connected account | The team argues about values before connecting each claim to an affected entity, scope, frame, consequence, and horizon. | Write the side rows and tension statement before mediation. |
| Description becomes conflict | A diagram, matrix, or narrative is treated as the ethical conflict itself. | Identify the description as a C.2.1 episteme and keep its EntityOfConcern and presentation form separate. |
| Collection name becomes responsibility | Organization, society, public, market, or AI is treated as responsible by label. | Recover systemhood, membership, participation, assignment, and agency evidence separately; cite the exact responsibility relation or missing governor. |
| Formal completeness displaces use | A large record is filled even though two sides and one tension already answer the current question. | Stop at the first adequate description and add only detail consumed by the next use. |
| Architecture absorbs ethics | Cross-scope residual wording hides value, harm, responsibility, or admissible sacrifice. | Use the applicable architecture pattern for the residual and use D.3 with D.4 for the ethical conflict and its use. |

### D.3:6 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-D3-1 | A reusable result is one C.2.1 episteme with one exact EntityOfConcern, ClaimGraph, and effective ReferenceScheme. Edition, form, carrier, and publication remain separate. | Makes the reference used by D.4 reidentifiable. |
| CC-D3-2 | At least two sides each connect one ethical claim, affected entity, declared level relation or applicable scope, value-frame edition, consequence, and horizon. Evidence use and uncertainty are added when current. | Shows what each claim affects rather than presenting a flat inventory. |
| CC-D3-3 | Any ClaimScope on the whole description remains separate from side-specific ClaimScopes and Work extents. | Prevents the description's coverage from replacing the scope of a side. |
| CC-D3-4 | The tension names the sides and states why they cannot all be met as stated. Any direct relation claim cites its definition and obtaining occurrence, or the exact A.6.RCD missing-governor result. | Prevents a reference field from manufacturing a fact in the situation. |
| CC-D3-5 | Classification assertion, Method, Work, relation definition, relation occurrence, evidence episteme, evidence use, publication, form, and carrier remain separately typed when used. | Prevents the conflict description from absorbing neighboring objects. |
| CC-D3-6 | The first useful result is readable without the optional enriched branches, and every added branch changes the conflict or its next use. | Keeps D.3 affordable in ordinary project work. |
| CC-D3-7 | The next-use statement names D.4, D.5, C.28, C.30.ILC, evidence, assurance, or another receiving pattern by value. | Keeps mapping separate from mediation, decision, proof, and assurance. |

### D.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Political label as structure | The conflict is named by a slogan such as society versus innovation. | Write the concrete sides, affected entities, scopes, value frames, consequences, and horizon. |
| Flat inventory | The map lists values, entities, evidence, and relations without showing which belong together. | Use side rows and one tension statement. |
| Actor by plural noun | A collection is made responsible because its name is plural or institutional. | Recover systemhood and each relation separately; cite an exact responsibility occurrence or missing governor. |
| Description-only conflict | The case becomes only a wording problem about a report, model, or standard. | Keep episteme identity and publication with their patterns while D.3 describes the affected systems, decisions, and ethical tension. |
| Mediation inside map | The description chooses the compromise. | Stop at the tension and next-use question; use D.4 for mediation or decision use. |
| Ontology as prose tax | Every simple concern is expanded into specialist relation language. | State the ordinary side first; add a formal identity only when another use relies on the distinction. |

### D.3:7 - Consequences

Work under `D.4`, `D.5`, `B.3`, `C.28`, `A.10`, `C.11`, and `C.30.ILC` can cite one conflict description without mistaking that description for the ethical object. The cost is that a reusable description must keep its claims, subject, interpretation, and neighboring relations distinct. The gain is that ordinary mediation and decision work can start from a short, connected account rather than a slogan or a large assurance form.

### D.3:9 - Rationale

The description episteme resolves the pattern's main ambiguity. The ethical situation is not a file or table, while D.4 still needs a stable object it can cite. C.2.1 supplies that object without inventing a universal conflict kind: the claims say what the sides are, one exact EntityOfConcern says what case they concern, and the effective ReferenceScheme says how to read them.

Side rows make the conflict inspectable because they preserve which claim affects which entity and scope. Conditional branches then recover Method, Work, transformations, evidence use, collection structure, agency, responsibility, publication, assurance, causality, and architecture only where the case actually depends on them. This keeps exact ontology available without making specialist prose the entrance price for ethical work.

### D.3:10 - SoTA-Echoing

`SoTA` here means the best current contribution to the practical question of making value conflict inspectable before deciding it. The comparison is current to 2026-08-20; publication date, popularity, and official status are not sufficient by themselves.

| Practice question | Exact source and status | Selected contribution and limit | Decision, receiving locus, and reopen |
| --- | --- | --- | --- |
| How can design work expose affected parties, values, and long-horizon effects before choosing a solution? | Batya Friedman and David G. Hendry, *Value Sensitive Design: Shaping Technology with Moral Imagination* (MIT Press, 2019), established method account (`https://doi.org/10.7551/mitpress/7585.001.0001`). | Stakeholder analysis, value scenarios, and multilifespan timelines support explicit affected parties, values, and horizons. VSD does not supply FPF episteme identity, direct-relation identity, or a complete method for resolving value conflicts. | **Adapt** affected-entity, value-frame, and horizon prompts into D.3:2 and the worked cases; **reject** VSD as a conflict ontology or decision authority. Reopen if a later method connects conflict sides to affected entities more clearly at comparable effort. |
| How should ethical concerns remain traceable through system design? | ISO/IEC/IEEE 24748-7000:2022, Edition 1, published 2022-11, *Standard model process for addressing ethical concerns during system design* (`https://www.iso.org/standard/84893.html`; IEEE 7000-2021 remains the earlier lineage edition). | The standard traces elicited values through operational concepts, value propositions, requirements, and ethical risk-based design. Its full life-cycle process and organizational apparatus are much heavier than one D.3 map, and official status does not make it the default method. | **Adapt** traceability from each value-frame claim to the affected design move and receiving decision in D.3:2.2-2.3; **reject** compulsory transfer of the full process. Reopen on a new edition or evidence that a lighter method gives better traceability. |
| Must every value conflict become a single-scale trade-off or optimization? | Atay Kozlovski, “Parity and the Resolution of Value Conflicts in Design,” *Science and Engineering Ethics* 28, 22 (2022), DOI `10.1007/s11948-022-00375-4`. | The paper compares three VSD conflict approaches and argues that incommensurable values may stand in parity rather than in a better, worse, or equal ordering. It is a proposed repair, not a universal conflict-resolution procedure. | **Adapt** the explicit tension branch and the rule against forcing one scale in D.3:2.1-2.2; send actual mediation to D.4. Reopen when stronger applied evidence changes how parity helps design decisions. |
| How can cross-scope benefits, harms, and uncertainty be mapped in a living technical programme? | NIST, *Artificial Intelligence Risk Management Framework 1.0* (NIST AI 100-1, 2023-01-26) and its live Core, checked 2026-08-20 (`https://doi.org/10.6028/NIST.AI.100-1`; `https://airc.nist.gov/airmf-resources/airmf/5-sec-core/`). NIST states that a revised version is in progress. | MAP 1 and MAP 5 connect intended uses with positive and negative impacts across individuals, groups, communities, organizations, society, and the planet, while keeping uncertainty and changing conditions visible. The framework is AI-specific and its actor, governance, and responsibility language does not establish FPF systemhood or direct responsibility relations. | **Adapt** the multi-scope affected-entity, consequence, uncertainty, and horizon prompts into D.3:2 and the collection case; **reject** the AI taxonomy, full governance apparatus, and any responsibility inference. Reopen when the announced revision is published or another domain method outperforms it for this use. |

### D.3:11 - Relations

- Builds on `D.1` and `D.2` for value-frame boundary and multilevel entry.
- Uses `C.2.1` to identify the reusable conflict-description episteme and any classification assertion episteme.
- Uses `E.10.ROLE` once when role-shaped wording must be recovered before kind, assertion, assignment, agency, or responsibility claims are made.
- Uses `A.6.RCD` when a needed direct relation has no adequate governor.
- Builds on `A.1`, `A.14`, `B.1`, and `C.13` when systemhood, part-whole, membership, collections, or constructive grounding are current.
- Coordinates with `D.4` for mediation and decision use and with `D.5` for bias, fairness, impact audit, causal-fairness audit consumption, and ethical assurance.
- Coordinates with `E.17` and `E.24.PUB` for publication, form, carrier, audience, and availability claims.
- Coordinates with `C.30.ILC`, `A.10`, `B.3`, `C.28`, and `C.29` when architecture residual, evidence, assurance, causal, or mathematical-lens claims are current.

### D.3:End

