## D.2 - Recognize Ethical Concerns Across Levels and Scopes (Multilevel Ethics)

> **Type:** D-family ethical entry pattern
> **Status:** Stable


**Use this when.** A proposed action may benefit one party and impose a cost or risk on another, or it may change who is responsible for the consequences. The parties can be parts of one system, members of overlapping groups or users affected through a shared service.

**Not this pattern when.** If only the value frame is missing, use `D.1`. If `D.3` has already described the conflict, use that result. If the conflict has to be mediated or used in a decision, use `D.4`. If the concern is bias, fairness, impact audit, causal-fairness audit consumption, or ethical assurance, use `D.5`.

**What goes wrong if missed.** A team sees the improvement it sought and recommends the change while somebody else loses access, takes on work or bears a new risk.

**What this buys.** Identify who or what may bear a consequence, explain how the action could reach them, and choose the ethical question that needs an answer.

### D.2:1 - Problem Frame

An organization can save work by moving it to its members. A project can meet its target while people outside the project lose access to a service. A standard can improve coordination for some users while excluding a device on which others rely. In each case, follow the change from the decision to those who may gain or lose.

Use a level of composition when the concern depends on what a constituent does within an identified whole. Two groups can share members, or rely on the same service, without either group being a constituent of the other. Identify the relation that carries the effect. Someone can bear a consequence without taking part in the decision.

### D.2:1.0 - Problem

A change can benefit one affected entity while imposing harm, exclusion or risk elsewhere, or change who is responsible for its consequences. The failure is to infer ethical sufficiency from the local gain without examining consequences for others. When responsibility matters, state its basis; a kind or assignment does not by itself establish that responsibility. Use `E.10.ROLE` when role wording leaves the relevant object or relation unclear.

### D.2:1.1 - Forces

| Force | Tension |
| --- | --- |
| Local benefit vs. cross-level harm | A change can improve one declared scope while imposing cost, risk, or exclusion elsewhere. |
| Situation-defined levels vs. fixed ladders | Identify the relevant composition, membership or exposure in the situation and the conditions assumed in the claim. |
| Affected entities and their descriptions | Identify the affected entity, whether a system or an episteme such as a standard, and explain whose use or interests make the change an ethical concern. |
| Early recognition vs. premature mediation | Use D.2 to make the conflict visible, D.3 to describe its sides and tension, and D.4 for mediation. |
| Ethical concern vs. architecture residual | Cross-scope residuals can be architectural, ethical, or both; choose the method for the question that needs answering. |

### D.2:2 - Solution

Start with the proposed action or arrangement and the gain it promises. Use an existing account if it identifies the affected parties and explains the consequences that matter here. Otherwise trace the changes in work, use or dependency to the entities that may experience their effects. Say which connections already exist, which the proposal would create, and which effects are observed or predicted. If you cannot tell who might experience an effect or how it would reach them, use `A.1.CSD` to investigate and state what remains unknown.

Connect each material consequence to the party or entity affected, the value premise that makes it matter and the conditions under which the change could produce it. If the claim concerns a whole, establish how the effects on its constituents bear on the property in question. A saving for one office may be extra work for another. If the claim concerns other settings, establish which conditions of that explanation hold there. State the next question. Use D.3 when the sides and their tension need describing. When an adequate account of the conflict already exists, it can go directly into the D.4 comparison.

Use `MultilevelEthicsEntry@Context` when the practitioner or a recipient needs to recover these connections for comparison or revision. Keep its content in the existing answer or working note when that suffices. If an existing note says only “level or scope”, recover which relation, affected population or applicability condition the note identified. Retain a reference to a `U.WorkScope` with the capability it qualifies, or to a `U.PublicationScope` with the publication view or form it qualifies. If the meaning of the old label is still unclear, keep the original wording and identify that uncertainty. Add the evidence, value-frame editions and supporting relations on which the stated concern relies.

```text
MultilevelEthicsEntry@Context:
  ethicalConcernRef
  affectedEntityOfConcernRef
  valueFrameEditionRefs?
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  compositionRelationRefs?  // identified whole and constituent, when their relation matters
  affectedPopulationOrAreaRefs?  // who is included or where exposure occurs
  affectedHolonRefs?
  affectedEpistemeRefs?
  roleWordRecoveryRefs?: E.10.ROLE results when the relevant role meaning needed clarification
  localSystemRoleKindRefs?: FinSet(U.KindRef)
  systemRoleClassificationAssertionRefs?: FinSet(U.EpistemeRef)
  systemRoleAssignmentRows?: FinSet({
    assignmentSpeciesRef: U.RelationKindRef constrained under U.SystemRoleAssignment
    assignmentOccurrenceRef: U.RelationRef constrained to an obtaining occurrence of assignmentSpeciesRef, with participants, holder, applicability, and extent recoverable
  })
  participationOrAffectedPartyRelationRefs?: direct relation refs
  participationOrAffectedPartyMissingGovernorRefs?: A.6.RCD results
  responsibilityRelationRefs?: direct relation refs
  responsibilityMissingGovernorRefs?: A.6.RCD results
  commitmentRelationRefs?: direct relation refs
  commitmentMissingGovernorRefs?: A.6.RCD results
  permissionRelationRefs?: direct relation refs
  permissionMissingGovernorRefs?: A.6.RCD results
  authorityRelationRefs?: direct relation refs
  authorityMissingGovernorRefs?: A.6.RCD results
  interestOrConcernRefs
  capabilityOrFunctioningConcernRefs?
  methodRefs?
  workRefs?
  transformationRefs?
  expectedConsequenceRefs
  evidenceRefs?
  uncertaintyOrCurrentnessCondition?
  nextSubjectPatternLocator
```

The entry has one job: make the multilevel concern recognizable and choose its next use. It does not require a separate dossier or new inquiry before the concern can be discussed. A proposed inquiry goes through `C.11.DUA` when its receiving contribution or feasibility is unresolved; conflict description and decision use remain with `D.3` and `D.4`.

Material systems and epistemes can be affected EntitiesOfConcern. For an episteme such as a standard, state which uses and interests make its change ethically relevant.

### D.2:3 - Recognition Matrix

| Working situation | What to recover | Next pattern to apply |
| --- | --- | --- |
| A Method helps one team meet its target while increasing risk for another team or for users. | Affected holons, any independently current assignment, Method, actual Work when present, expected consequences, evidence, and each responsibility, commitment, permission, authority, or participation relation that the concern relies on. | `D.3` conflict description |
| A city service gains capacity while access for night-shift workers in one district may worsen. | Identify the service, who can use it at the relevant hours, how the proposed change affects access, and whose responsibilities or value claims it engages. | `D.3` conflict description |
| A technical standard improves interoperability but excludes a minority device, language, publication form, or data source. | Standard or episteme whole, affected systems, publication and use relations, consequence horizon. | `D.3`, with `C.2.1` and `E.17` as needed |
| An overall result meets its target while the outcome for a particular group is unknown. | Recover who entered the count, which outcome was measured, and whether the result supports the claim about that group. | `D.5`, with `C.28` when a causal claim matters |
| An architecture move reduces residual at one holon level while creating cross-scope residual elsewhere. | Architecture structure, selected scopes, residual, affected value concerns. | `C.30.ILC`; use `D.3` if ethical conflict is live |

### D.2:4 - Boundaries

D.2 recognizes ethical concerns across levels and scopes. Use the corresponding subject method to judge a conflict, mediate it or conduct an audit.

An affected population identifies who may experience a change. A composition relation identifies a whole and its constituent. A claim’s scope identifies the conditions under which the assertion applies (`A.2.6`). A proposed use can fall within the stated scope while evidence for its predicted effect is still missing. The same fact can matter to more than one of these questions. A change to a service can affect an entire organization on one occasion. To use that explanation for future decisions, identify what would carry the effect again. `B.5.MR` compares what models fix or leave open. Use `C.29` when a mathematical representation is needed to examine scale, a trade-off or an allocation.

### D.2:5 - Archetypal Grounding (Worked Slice)

A product team wants to reduce service cost by making a medical device harder to service outside authorized centers. The team expects better manufacturer quality control and lower liability risk. To find who may bear the cost, follow the proposed restriction through the service arrangement: some regions have local repair services but no authorized center; losing the local route may prolong device downtime and reduce patients' timely access.

This is a possible consequence of the restriction, with its likelihood and extent still to be established. The next question is which service restriction, if any, addresses the hazard without imposing avoidable access harm. That question and the connected sides complete the present `D.2` recognition; `D.3` can describe their tension from this account.

Now suppose a release decision depends on whether a proposed servicing method can leave calibration outside the declared tolerance. A qualified test team can perform the discriminating check before the release window closes, and the release authority needs its result under the applicable rule. Preserve that investigation and the rule's force.

Use `C.11.DUA` to compare the restriction's protective contribution with access harm, feasible alternatives, delay, and displaced work. `D.4` carries the resulting decision, including the authority needed to change a requirement or accept a residual. If the required basis cannot be obtained, the proposed release remains unsupported; a narrower continuation must meet its conditions.

### D.2:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Local improvement treated as sufficient | A proposal benefits one party while imposing costs elsewhere. | Trace where the work, risk or loss goes and why it matters to those affected. |
| Fixed ladder bias | A hierarchy such as individual, team and society is imposed on an affected population. | Identify actual composition, membership, use or exposure. Establish responsibility where the judgement relies on it. |
| System-only bias | Multilevel ethics is limited to material systems and misses epistemes, standards, publications, or descriptions. | Treat affected systems and epistemes as admitted holons when the case makes them current. |
| Architecture absorbs ethics | A cross-scope residual is treated only as architecture because it has a structural shape. | Use `C.30.ILC` for architecture residual and `D.3` and `D.4` when value, harm, responsibility, or admissible sacrifice is live. |

### D.2:6 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-D2-1 | Identify the whole and constituent when composition matters, the membership or exposure that locates the affected parties, and the conditions on which the consequence claim depends. Use the distinctions needed for the next decision. | Makes clear whose gain or loss is at issue and where the explanation applies. |
| CC-D2-2 | Name the affected entities, Methods, actual Work and consequences needed for the concern. Clarify unclear role wording with `E.10.ROLE`; keep any local kind and C.2.1 classification assertion distinct. For an assignment, use its declared species and support the claim; an asserted occurrence needs its participants and applicability. Establish participation, responsibility, commitment, permission and authority separately when relied on, retaining a supported negative or conditional result, or the missing fact or rule. | Keeps the entry usable without making assignment imply participation or responsibility. |
| CC-D2-3 | The result identifies the next live question and `D.3`, `D.4`, `D.5`, `C.30.ILC`, or another subject pattern that answers it. The entry record is used only when its recoverable content contributes to that use. | Keeps D.2 as entry recognition, not conflict solver. |
| CC-D2-4 | Mathematical reasoning retains its subject, interpretation and applicable conditions. Use `C.29` when representation choice, transfer or supported use remains unresolved, and the measurement pattern when a measurement claim is current. | Keeps mathematical support distinct from ethical priority. |

### D.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| One-level ethics | The case is treated as good because one declared level improves. | Name every affected level or scope that changes the ethical claim. |
| Ladder import | A fixed level list is imported before the case is understood. | Recover the situation-defined scopes first. |
| Entry as solution | D.2 is used to decide the conflict. | Name the concern and select D.3, D.4, D.5, C.30.ILC, or another subject pattern for its next use. |
| Hidden episteme harm | A standard, model, policy, or architecture description is treated only as a document, not as an affected episteme with use consequences. | Separate the episteme, its publication relation, use relation, and affected systems or people. |

### D.2:7 - Consequences

Making cross-scope concerns explicit lets the practitioner choose the next question, such as an ethical conflict, an architectural consequence or a need for audit.

### D.2:9 - Rationale

A change can look technically local while shifting costs, risks or responsibilities across affected entities. Recovering those relations lets the practitioner formulate the ethical question before choosing mediation, an audit or an architectural response.

### D.2:10 - SoTA-Echoing

For recognizing a transferred consequence, **adopt** A.1.CSD's tracing of a proposed change through actual relations and supported possible effects, when the affected account is incomplete. Compared with judging only the proposal's local target or assigning priority by level, :2 and the service-restriction case retain the access loss alongside the claimed quality benefit. D.1 supplies the value premise; D.3 and D.4 describe and decide the resulting conflict.

This construction makes the traced concern available for the next question without a fixed level catalogue or a full impact study. Its conclusion covers the bearers and effect paths recovered. Reuse an adequate existing account; reconsider it when a new relation, consequence or value premise changes the affected concern.

### D.2:11 - Relations

- Builds on `D.1` for ethical value frame boundary.
- Use `A.1`, `B.1` and `C.13` to recover holons and composition, and `A.2.6` to establish where a claim applies.
- Coordinates with `D.3` for the interlevel ethical conflict description and with `D.4` for mediation or decision use.
- Coordinates with `D.5` for bias, fairness, impact audit, causal-fairness audit consumption, and ethical assurance.
- Coordinates with `C.11.DUA` when a proposed inquiry or disputed protective requirement needs contribution, feasibility, and burden appraisal.
- Coordinates with `A.15`, `A.3.4`, `C.16`, `C.29`, and `C.30.ILC` when method, work, transformation, measurement, mathematical lens, or architecture residual claims are current.

### D.2:End
