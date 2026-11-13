## D.3 - Describe an Ethical Conflict Across Levels or Scopes

> **Type:** D-family ethical conflict-description pattern
> **Status:** Stable


**Use this when.** Ethical claims at different declared levels or scopes raise an incompatibility, trade-off or unresolved value tension that needs explaining. State each ethical concern as a claim about the case.

**Not this pattern when.** If only the ethical value frame is missing, use `D.1`. If only entry recognition is needed, use `D.2`. If D.3 has already described the conflict and the question is mediation or decision use, use `D.4`. If the question is bias, fairness, impact audit, causal-fairness audit consumption, or ethical assurance, use `D.5`.

**What goes wrong if missed.** The team debates values or decisions before it can say who or what is affected, under which value frame and scope, over what horizon, and why the claims are in tension.

**What this buys.** A reader can see each side, what it affects, and how the sides are in tension before deciding what to do.

### D.3:1 - Problem Frame

Ethical conflicts can cross part–whole relations or overlapping scopes. A decision may improve an organization's performance while harming affected people; an episteme may shape decisions that benefit some users and disadvantage others. Declare the relations and scopes present in the case; structural levels do not establish a moral hierarchy.

The practical problem is connecting each claim to what it affects. An inventory of affected entities and values does not explain which claim concerns which entity or why those concerns are in tension for the present question. Describe each side as one connected statement and explain their tension.

The reusable result is a description episteme, not the conflict in the situation and not the form used to show it. The phrase *conflict structure* remains useful ordinary shorthand for the connected claim content inside that description.

### D.3:1.0 - Problem

An ethical conflict is often argued before it is described. The affected objects, scopes, value frames, claimed benefits and harms, evidence limits, and consequence horizons remain implicit, so mediation begins from slogans rather than from inspectable claims.

### D.3:1.1 - Forces

| Force | Tension |
| --- | --- |
| Conflict description vs. decision use | Make the sides and their tension inspectable for mediation or decision use under D.4. |
| Level and scope plurality vs. fixed ladder | Recover the relevant relations and scopes from the case; structural levels do not establish ethical priority. |
| Conflict vs. description | A narrative, table, graph, or formal expression can describe the conflict but is not the situation, claims, harms, or relations it describes. |
| First result vs. reusable precision | The first result needs connected sides and a tension statement; later reuse may need an identified episteme and typed supporting relations. |
| Agency evidence vs. responsibility | Evidence may support an agency characteristic or threshold. Responsibility needs its direct predicate and participants; no score, label, collection name, or assignment supplies it. |
| Architecture residual vs. ethical conflict | A cross-scope structure can be architectural, ethical, or both. `C.30.ILC` triages the architecture residual; D.3 describes the ethical conflict. |

### D.3:2 - Solution

#### D.3:2.1 - First result

Identify the sides needed to explain the conflict. At least two claims are involved; include more when the tension depends on their combination. For each side, write:

1. the ethical claim that states the concern in ordinary language;
2. the affected entity;
3. the declared level relation, claim scope, or Work extent that locates the concern;
4. the value premise under which the consequence matters, with a frame-edition reference when the reasoning uses one;
5. the expected benefit, harm, or constraint and its consequence horizon; and
6. the evidence use or uncertainty only when the side relies on it.

Then explain why the claims cannot all be met as stated, what would be traded, or why they remain in unresolved tension. Three or more claims may be jointly incompatible even when every pair is compatible. Name the intended use of this description and any question that remains to be settled. Stop when this makes the conflict inspectable for its intended use.

A short working note can be sufficient. Develop a more elaborate description only when its intended use requires the additional content.

#### D.3:2.2 - Reusable conflict description

When another reader or later use must cite, compare, revise, or publish the result, identify one `InterlevelEthicalConflictDescription`. This is an ordinary local name for one C.2.1 `U.Episteme`.

Apply the C.2.1 identity test:

- **EntityOfConcern:** one exact entity already recovered for the case, such as the plan, proposed system change, or decision situation whose ethical tension is being described. Do not use a loose bundle of several possible subjects.
- **ClaimGraph:** the exact claim content containing the conflict sides, their tension, and the next-use question. When those claims are explicitly restricted to part of the situation, it also identifies the description's ClaimScope.
- **effective ReferenceScheme:** the designation, interpretation, measurement, comparison, and evaluation rules needed to read those claims.

Changed claim content, EntityOfConcern, or effective ReferenceScheme identifies another episteme. Say that a later description revises or supersedes an earlier one only when a C.2.1 `EpistemeEditionRelation` is asserted. A changed narrative, table layout, publication form, carrier, or publication occurrence does not by itself change the episteme.

Use this content shape when a reusable record helps:

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
        valuePremise
        valueFrameEditionRef?
        expectedConsequence: what changes and why it counts, for example, as a benefit, harm, or constraint under that value premise
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

The `plainStatement` must name the incompatibility, trade-off, parity, or other tension claimed among the sides. In an ordinary case, it remains claim content in the description. If a receiving use relies on a separately obtaining direct relation, cite the relation definition and occurrence with its participants, applicability, and identity. If no adequate governor exists, record the `A.6.RCD` missing-governor result. Merely filling a reference field never makes a direct relation obtain.

#### D.3:2.3 - Add detail only when it changes the conflict or its next use

| Open this branch when... | Add... | Keep separate... |
| --- | --- | --- |
| A Method is part of a side's claim. | the exact `U.Method` under A.3.1 and, when cited, its MethodDescription under A.3.2 | Method identity from any dated performance |
| Performance occurred. | use A.13 to identify the performer System; use A.15.1 to admit the exact dated `U.Work` independently from its history, Method, extent, and containing System; if the conflict account must also identify the assignment under which the Work was performed, check that relation separately through F.6 | keep a plan, intention, assignment, capability, permission, authority, and responsibility separate from performed Work |
| Assignment matters. | the exact assignment species and the claim with its case basis under A.2.1; cite an obtaining occurrence when the account relies on one | assignment from performance, responsibility, permission, or authority |
| Role wording or classification needs clarification. | use E.10.ROLE to recover the meaning; when System classification is claimed, identify the local kind and the separate C.2.1 classification assertion under C.3.2 with its candidate-admissibility basis | ordinary wording, classification, assignment, and the acting System from one another |
| Evidence changes a side or its uncertainty. | identify the supporting content and the grounds for this use; apply A.10 when the source-to-use relation is implicit or must be replayable | available or stored evidence from what it warrants for this side |
| A change affects who may benefit or be harmed. | identify the proposed change and its supported possible consequences; when an actual transformation is claimed, identify its occurrence and affected participants under A.3.4 | a possible or described change from an obtaining transformation |
| Membership or part-whole structure matters. | the applicable collection-membership or part-whole predicate and its supported claim or unresolved condition; an affirmative occurrence claim needs its obtaining basis | a plural name from an acting or responsible System |
| Agency is disputed. | identify the agency claim and its supporting basis; use A.13 for an FPF agency claim, adding a Characteristic, Scale or threshold only when the claim or criterion requires it | an agency claim from responsibility |
| Responsibility, permission, authority, commitment, or participation is claimed. | the applicable direct predicate, participants and supported affirmative, negative or modal claim, or the unresolved condition; an affirmative occurrence claim needs its obtaining basis, and a separate occurrence reference is added when its identity is used | the relation family from an occurrence; the occurrence from evidence for it |
| A calculation or formal comparison changes the tension. | retain the calculation's subject correspondence, applicable assumptions and operation; use C.29 when the representation's choice, transfer or supported use remains unresolved | a formula or score from the ethical conflict or decision |
| Publication or audience use changes the ethical claim. | recover the claims made available, audience and bounded use under E.24.PUB, including the expression, carrier, form or occurrence identity that changes this judgement; use E.17 when a readable face of an accepted account must be produced | the published episteme from its expression, form, carrier, publishing Work, and availability relation |
| A harm or benefit depends on causality, assurance, or architecture. | only the affected C.28, B.3, D.5, or C.30.ILC return | the conflict description from causal proof, assurance, or architecture selection |

Open no branch merely because the field exists. The detail must change a side, the tension, or the next receiving use.

### D.3:3 - Collection and Episteme Cases

A collection is ethically current only when whole-level characteristics, membership relations, environment-mediated effects, or aggregate consequences matter. Use `A.14` for part-whole and membership relations and `C.13` for constructive grounding. A plural or institutional name does not make the collection an acting or responsible System.

An episteme is ethically current when its claim content, source use, publication, described EntityOfConcern, or model use changes the affected systems or decisions. Use C.2.1 for episteme identity and exact edition claims, and E.24.PUB for the publication relation; use E.17 when producing a readable face of an accepted account. The D.3 conflict description is a separate episteme about the selected case; it does not become identical to the policy, model, standard, or architecture description involved in one of its sides.

### D.3:4 - Boundaries

| Do this in D.3 | Do not do this in D.3 |
| --- | --- |
| Derive the declared levels and scopes from the case. | Impose a fixed moral ladder. |
| Connect every side's claim, affected entity, scope, value frame, consequence, and horizon. | Present flat bags of entities, values, evidence, and relations as if their connections were obvious. |
| Keep the conflict description, the situation it describes, and its narrative, table, graph, form, carrier, and publication separate. | Treat a file or diagram as the conflict, or treat description content as proof that a direct relation obtains. |
| Add Method, Work, assignment, classification, evidence use, agency, responsibility, publication, assurance, causal, or architecture detail only when current. | Require assurance-like apparatus before the first map exists. |
| Stop at an inspectable tension and next-use question. | Choose the compromise, refusal, override, or accepted residual; those are D.4 uses. |
| Use `C.30.ILC` when an architecture residual is also current. | Route every cross-scope architecture problem to ethics. |

### D.3:5 - Archetypal Grounding (Worked Slices)

**First engineering description.** A consultant is asked to improve a surveillance project's effectiveness.

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

This is enough to begin D.4 and does not decide who is responsible. If another reader must cite or revise the note, identify it as an `InterlevelEthicalConflictDescription` whose EntityOfConcern is the consulting-plan episteme.

If consulting Work later occurs, use A.13 to identify its performer and A.15.1 to admit the dated occurrence independently. Add F.6 only if the note must also identify the assignment under which that Work was performed. Add agency or relation detail only when that claim changes the account, using its pattern and preserving its affirmative, negative, conditional or unresolved result.

If the consulting agreement explicitly excludes deployment decisions, it grants no authority for those decisions. If the agreement's scope is unavailable, leave that authority claim unresolved and identify the missing agreement. D.4 can use either result: a justified denial concerns this agreement, while an unavailable premise leaves a question to settle.

**Joint incompatibility.** Three neighborhoods each claim at least one hour of a mobile clinic's service under a declared equal-access requirement. Only two service hours are available in the relevant window. Any pair of claims could be met; all three together cannot. Describe all three sides and the shared capacity condition before asking D.4 to examine continuations. No pairwise description captures this whole conflict.

**Conditional collection record.** A fleet-wide maintenance change lowers cost but may raise failure risk for a small subfleet operating in harsh conditions. The description has a fleet-cost side and a harsh-service safety side, each with its affected entity, scope, value premise and any frame edition used, consequence, and horizon. Add the exact fleet-membership relation because it locates the subfleet. Identify the reliability evidence and its grounds for this safety claim; use A.10 if the source-to-use relation is implicit or needs a replayable account. Return the causal question to C.28 if the risk claim depends on the proposed change.

None of those additions makes the fleet an acting or responsible whole; use A.1 for systemhood and the responsibility predicate for responsibility.

**Episteme record.** A published architecture description normalizes an interface assumption that excludes an alternative implementation. The EntityOfConcern of the D.3 description is the exact supplier-selection situation, not the architecture-description file. One side claims lower integration cost; the other claims unjust exclusion of affected suppliers under a named value-frame edition and horizon. Cite the architecture-description episteme and its publication or use only because that use carries the assumption into the decision. Use C.30.AD for description adequacy and E.24.PUB for the publication relation; D.3 records the ethical tension that remains.

### D.3:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Debate replaces a connected account | The team argues about values before connecting each claim to an affected entity, scope, frame, consequence, and horizon. | Write the side rows and tension statement before mediation. |
| Description becomes conflict | A diagram, matrix, or narrative is treated as the ethical conflict. | Identify the description as a C.2.1 episteme and keep its EntityOfConcern and presentation form separate. |
| Collection name becomes responsibility | Organization, society, public, market, or AI is treated as responsible by label. | Recover the subject and the responsibility predicate used, then establish its case basis or the unresolved question. Add membership, participation, assignment and agency claims only when that inference needs them. |
| Formal completeness displaces use | A large record is filled even though two sides and one tension already answer the question. | Stop at the first adequate description and add only detail consumed by the next use. |
| Architecture absorbs ethics | Cross-scope residual wording hides value, harm, responsibility, or admissible sacrifice. | Use the applicable architecture pattern for the residual and use D.3 with D.4 for the ethical conflict and its use. |

### D.3:6 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-D3-1 | A reusable result is one C.2.1 episteme with one exact EntityOfConcern, ClaimGraph, and effective ReferenceScheme. Edition, form, carrier, and publication remain separate. | Makes the reference used by D.4 reidentifiable. |
| CC-D3-2 | At least two sides each connect one ethical claim, affected entity, declared level relation or applicable scope, value premise, consequence, and horizon. Identify a value-frame edition when used; add evidence use and uncertainty when current. | Shows what each claim affects rather than presenting a flat inventory. |
| CC-D3-3 | Any ClaimScope on the whole description remains separate from side-specific ClaimScopes and Work extents. | Prevents the description's coverage from replacing the scope of a side. |
| CC-D3-4 | The tension names the sides and explains the incompatibility, trade-off, parity or unresolved tension relevant to the next use. A direct relation claim retains its predicate, participants, polarity or modality, and case basis or unresolved condition. An affirmative occurrence claim needs its obtaining basis; cite occurrence identity only when the receiving use needs it. | Prevents a reference field from manufacturing a fact in the situation. |
| CC-D3-5 | Classification assertion, Method, Work, relation definition, relation occurrence, evidence episteme, evidence use, publication, form, and carrier remain separately typed when used. | Prevents the conflict description from absorbing neighboring objects. |
| CC-D3-6 | The first result is readable without the optional enriched branches, and every added branch changes the conflict or its next use. | Keeps D.3 affordable in ordinary project work. |
| CC-D3-7 | The next-use statement names D.4, D.5, C.28, C.30.ILC, evidence, assurance, or another receiving pattern by value. | Keeps mapping separate from mediation, decision, proof, and assurance. |

### D.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Political label as structure | The conflict is named by a slogan such as society versus innovation. | Write the sides, affected entities, scopes, value frames, consequences, and horizon. |
| Flat inventory | The map lists values, entities, evidence, and relations without showing which belong together. | Use side rows and one tension statement. |
| Actor by plural noun | A collection is made responsible because its name is plural or institutional. | Recover the subject and the responsibility predicate with the basis for the claim; retain a negative result or unresolved condition when warranted. |
| Description-only conflict | The case becomes only a wording problem about a report, model, or standard. | Keep episteme identity and publication with their patterns while D.3 describes the affected systems, decisions, and ethical tension. |
| Mediation inside map | The description chooses the compromise. | Stop at the tension and next-use question; use D.4 for mediation or decision use. |
| Ontology as prose tax | Every simple concern is expanded into specialist relation language. | State the ordinary side first; add a formal identity only when another use relies on the distinction. |

### D.3:7 - Consequences

A connected conflict description lets mediation or decision work start from the claims and their tension. For later reliance, keep its subject, claims, interpretation and supporting relations identifiable.

### D.3:9 - Rationale

When a later judgement must cite or revise the description, C.2.1 identifies the claim-bearing episteme: the claims say what the sides are, its EntityOfConcern identifies the case, and its effective ReferenceScheme says how to read them.

Side rows make the conflict inspectable because they preserve which claim affects which entity and scope. Add supporting detail where it changes that account or its intended use.

### D.3:10 - SoTA-Echoing

The comparison below selects contributions from the named sources and editions for making value conflict inspectable before deciding it.

**How can design work expose affected parties, values, and long-horizon effects before choosing a solution?**

**Source and status.** Batya Friedman and David G. Hendry, *Value Sensitive Design: Shaping Technology with Moral Imagination* (MIT Press, 2019), established method account (`https://doi.org/10.7551/mitpress/7585.001.0001`).

**Selected contribution and limit.** Stakeholder analysis, value scenarios, and multilifespan timelines support explicit affected parties, values, and horizons. VSD does not supply FPF episteme identity, direct-relation identity, or a complete method for resolving value conflicts.

**Decision, receiving locus, and reopen.** **Adapt** affected-entity, value-frame, and horizon prompts into D.3:2 and the worked cases; **reject** VSD as a conflict ontology or decision authority. Reopen if a later method connects conflict sides to affected entities more clearly at comparable effort.

**How should ethical concerns remain traceable through system design?**

**Source and status.** ISO/IEC/IEEE 24748-7000:2022, Edition 1, published 2022-11, *Standard model process for addressing ethical concerns during system design* (`https://www.iso.org/standard/84893.html`; IEEE 7000-2021 remains the earlier lineage edition).

**Selected contribution and limit.** The standard traces elicited values through operational concepts, value propositions, requirements, and ethical risk-based design. Its full life-cycle process and organizational apparatus are much heavier than one D.3 map, and official status does not make it the default method.

**Decision, receiving locus, and reopen.** **Adapt** traceability from each value-frame claim to the affected design move and receiving decision in D.3:2.2-2.3; **reject** compulsory transfer of the full process. Reopen on a new edition or evidence that a lighter method gives better traceability.

**Must every value conflict become a single-scale trade-off or optimization?**

**Source and status.** Atay Kozlovski, “Parity and the Resolution of Value Conflicts in Design,” *Science and Engineering Ethics* 28, 22 (2022), DOI `10.1007/s11948-022-00375-4`.

**Selected contribution and limit.** The paper compares three VSD conflict approaches and argues that incommensurable values may stand in parity rather than in a better, worse, or equal ordering. It is a proposed repair, not a universal conflict-resolution procedure.

**Decision, receiving locus, and reopen.** **Adapt** the explicit tension branch and the rule against forcing one scale in D.3:2.1-2.2; send mediation to D.4. Reopen when stronger applied evidence changes how parity helps design decisions.

**How can cross-scope benefits, harms, and uncertainty be mapped in a living technical programme?**

**Source and status.** NIST, *Artificial Intelligence Risk Management Framework 1.0* (NIST AI 100-1, 2023-01-26) and its live Core, checked 2026-08-20 (`https://doi.org/10.6028/NIST.AI.100-1`; `https://airc.nist.gov/airmf-resources/airmf/5-sec-core/`). NIST states that a revised version is in progress.

**Selected contribution and limit.** MAP 1 and MAP 5 connect intended uses with positive and negative impacts across individuals, groups, communities, organizations, society, and the planet, while keeping uncertainty and changing conditions visible. The framework is AI-specific and its actor, governance, and responsibility language does not establish FPF systemhood or direct responsibility relations.

**Decision, receiving locus, and reopen.** **Adapt** the multi-scope affected-entity, consequence, uncertainty, and horizon prompts into D.3:2 and the collection case; **reject** the AI taxonomy, full governance apparatus, and any responsibility inference. Reopen when the announced revision is published or another domain method outperforms it for this use.

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
