## B.2.5 - Supervisor-Subholon Feedback Relation

> **Type:** Part B holonic construction pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### B.2.5:0 - Use This When

Use this pattern when a holon is supervised, regulated, steered, corrected, constrained, or coordinated through a two-sided feedback relation between one supervising acting system and one or more supervised holons. If the supervision is conditioned by a local system-role kind or assignment, recover that classification and exact assignment separately.

The first useful move is to recover the facts supporting the feedback claim:

```text
Which holons are supervised?
Which admitted system supervises these holons for this feedback use, under which policy and during which time window, and which local supervisor system-role kind and exact assignment obtain when that classification matters?
What observation, report, signal, publication, or source relation carries state?
What influence, constraint, objective, mode, or work change returns?
Which rule and case facts couple that return to the observation for each supervised holon?
Which transformation, work, architecture, evidence, assurance, timing,
or causal claim is being made in addition to the relation?
```

**What goes wrong if missed.** A control diagram, policy note, dashboard, publication channel, or supervisor word starts carrying part-whole, agency, safety, assurance, timing, gate, or architecture claims that belong elsewhere.

**What this buys.** B.2.5 gives a readable compound claim: for each named holon, this system receives the stated observation and returns an influence coupled to it under the applicable rule. The observation, influence and coupling facts remain separately governed; the assertion can support a control description without introducing a fused feedback occurrence.

**Not this pattern when.**

- If the question is a control-structure view, use `C.30.LCA`.
- If the question is architecture or selected structure, use `C.30`, `A.22`, and `C.30.ASV`.
- If the question is reusable dynamics, timing, rate, or temporal validity, use `A.3.3` and `C.27`.
- If the question is causal use, use `C.28`.
- If the question is evidence, provenance, assurance, or a gate decision, use `A.10`, `G.6`, `B.3`, or `A.21` respectively. Use `A.20` for its internal-constraint test in a transformation-flow structure; other constraint claims need their direct pattern.
- If module or interface wording hides the exact claim, use `A.6.M` to recover it; use the direct pattern for an already precise allocation or commitment claim.
- If the question is whole reidentification, use `B.2`.

### B.2.5:1 - Problem Frame

A supervisor-subholon feedback claim states observation or reporting, returned influence and their coupling for named participants in one use. It is a conjunction under A.6.RCD, expressed in a C.2.1 assertion. Each base relation retains its own participants, applicability and identity rule. A system-role kind or assignment may qualify the acting system when independently established.

Use B.2.5 for this compound description. A broader architecture, MHT, Work or evidence account may use it while retaining the direct rules for those additional claims.

### B.2.5:2 - Problem

Without this pattern, three different structures collapse:

1. **Part-whole structure.** Which holons are parts of which wholes.
2. **Supervisor-subholon feedback relation.** Which admitted system supervises, what it observes, and what influence or constraint returns; add its system-role kind and assignment only when separately current.
3. **Description or representation structure.** Which diagram, dashboard, report, model, publication, or control-view description represents the relation.

When these are confused, a functional layer is treated as a physical part, a publication is treated as an acting system, a diagram is treated as evidence, or a supervisor label is treated as a gate or assurance result.

### B.2.5:3 - Forces

| Force | Tension |
| --- | --- |
| Recognizable feedback language vs kind precision | Engineers use feedback, control, supervision, and regulation language naturally; FPF needs the relation and neighboring claim kinds named. |
| Relation vs view | A supervisor-subholon relation may appear inside a control-structure view, but the view and relation are different objects. |
| Acting system vs episteme | A theory, model, standard, dashboard, or report used as a claim-bearing episteme remains distinct from the System that revises or uses it. |
| Closure vs stronger claims | A two-sided feedback relation can supply input to stability or assurance work, but does not certify those claims. |
| Medium visibility vs perfect communication | The relation needs observation or report and influence or constraint sides, including publication or medium limits when current. |

### B.2.5:4 - Solution

State the feedback claim in one C.2.1 episteme about the named controller and supervised holons. A sufficient ordinary reading is: “For every drone in this set during the stated interval, controller C receives the stated observations and returns commands coupled to those observations under rule R.” Use A.6.RCD's compound-claim branch; the description does not require a new relation kind or one independently reidentifiable feedback occurrence.

For a nonempty set H and each h in H, recover three propositions under their direct domain definitions:

1. **Observation:** which state of h is observed or reported to the controller, through which obtaining observation, report, publication or source relation.
2. **Return:** which influence from the controller reaches h, under the applicable command, constraint, objective, mode or Work predicate.
3. **Coupling:** which rule applies to this observation and return, and which facts establish that this return depends on that observation under the rule.

The compound claim is true exactly when all three propositions hold for every member of H under common applicability: the same named use, participants, scope and temporal qualification. This is ordinary logical conjunction of those propositions, not a combination of probability scores or assurance results. Recover each direct definition and its applicable edition when the claim relies on it. A local use needs no separately published conjunction rule.

An optional note can retain the needed details:

```text
SupervisorSubholonFeedbackClaim@Context:  // claim-bearing episteme, not U.Relation
  supervisingActingSystemRef: U.EntityRef resolving to one admitted U.System
  supervisedHolonRefs: FinSet(U.HolonRef)  // nonempty
  useAndTemporalQualification:
  pairClaims:  // one for every supervised holon
    supervisedHolonRef:
    observationClaimAndBaseRelationRefs:
    returnedInfluenceClaimAndBaseRelationRefs:
    applicableCouplingRuleAndEdition:
    couplingFacts:
  supervisorSystemRoleKindRef?:
  supervisorSystemRoleAssignmentRef?:
  evidenceRefs?:
  strongerClaimPatternRefs?:
```

Observation and influence references keep their own kinds; a report episteme, a signal occurrence and a source-use relation are not interchangeable occupants of one relation position. Evidence supports the assertion under A.10; its adequacy and the obtaining of the base facts remain separate questions. A local system-role kind and assignment are added only when they independently obtain and affect this use.

#### B.2.5:4.1 - Establish and qualify the conjunction

Co-present telemetry and commands are insufficient. For each pair, apply the coupling rule to the actual observation and return. An unrelated broadcast fails that condition; one-way reporting fails the two-sided predicate. If the rule is missing, return the missing governor. If the rule exists but a needed observation or dependency fact is unavailable, return missing information. Neither absence of proof alone nor an empty supervised set supports the affirmative assertion. A negative claim needs the rule's non-obtaining test and facts that satisfy it.

Keep the base occurrences and their own extent and continuity rules. A communication break can make an interval-qualified feedback assertion fail without ending a supervisor assignment. Reconnection requires current observation, return and coupling facts. Apply a changed policy to the affected interval; adding a holon extends the asserted set only after its own pair is supported.

Reopen the dedicated relation-kind alternative only when a receiving use needs to identify a feedback occurrence independently across changes. That alternative must supply its obtaining, extent and continuity rules, including interruptions, under A.6.RCD and A.6.REL. A useful compound description can stop here.

#### B.2.5:4.2 - Part-Whole Boundary

A supervised holon may be part of a larger holon, but supervision and parthood are different relations. A controller, committee, platform-governance group, review board, or tool-mediated group can supervise when the exact acting entity is independently admitted as `U.System`; it may do so under an exact system-role assignment without being a physical part of the supervised holon. A method, policy, or review practice can structure the supervision work; it does not supervise by itself.

Use `A.1` for holon recognition, `A.14` for the exact mereological claim, and `B.1` or `C.13` for the applicable construction account. Use B.2.5 for the compound supervisor-subholon feedback claim.

#### B.2.5:4.3 - Acting-System Boundary

The supervising participant is an admitted acting system. When local classification matters, A.2 supplies the exact supervisor system-role kind and A.2.1 supplies the obtaining assignment; neither label nor assignment acts. Do not create `U.TransformerRef` or treat a publication, theory, dashboard, model, method description, or report as the acting system.

For acting-side externalization, use `A.12`. For transformation, use `A.3.4`. For Work, use `A.15.1`. For system-role kind and assignment, use `A.2` and `A.2.1`.

#### B.2.5:4.4 - Control-Structure View Boundary

When feedback is drawn as planner, controller, observer, plant and supervisor structure, B.2.5 states the compound claim and `C.30.LCA` governs the control-structure view. The view can cite both the assertion and the independently obtaining base relations. Its arrows alone establish neither their obtaining nor the coupling.

#### B.2.5:4.5 - Neighboring Claim Boundary

B.2.5 does not certify stability, safety, assurance, evidence sufficiency, causal validity, gate passage, rate adequacy, or mathematical adequacy.

Use:

- `A.3.3` for reusable dynamics or state-evolution claims;
- `C.27` for temporal and rate adequacy;
- `C.28` for causal-use claims;
- `A.10` and `G.6` for evidence and provenance;
- `B.3` for assurance;
- `A.20` for its internal-constraint test in a transformation-flow structure and `A.21` for gate decisions;
- `C.29` for mathematical-lens use.

### B.2.5:5 - Archetypal Grounding (Worked Cases)

#### B.2.5:5.1 - Robotic Swarm

A fleet controller C supervises drone d1. In this illustrative protocol R1, each control tick requires a same-tick range report received by C and a returned command received by d1. The command is generated from that report: reduce speed when the reported obstacle distance is below 2 m; otherwise maintain speed. These protocol predicates govern reporting, command delivery and their coupling for this case; they do not establish sensor accuracy or safety.

| Case facts under R1 | Compound result |
| --- | --- |
| At tick 10, C receives d1's 1.2 m report, generates `reduce speed` from it under R1, and d1 receives that command. | All three conjuncts hold for {d1} at tick 10. |
| At tick 11, C receives telemetry, but the only delivered command is an unrelated scheduled broadcast. | The known command has no R1 coupling to that report; it does not satisfy this feedback predicate. |
| At tick 12, the report arrives but the complete tick trace shows no returned command. | The return conjunct fails. Reporting remains an independently supported fact. |
| At tick 13, the link breaks and the complete trace shows no same-tick report or return. | The claim covering every tick 10–13 fails under R1. A supervisor assignment may still continue under its own rule. |
| At tick 14, the link reconnects and a new report, R1-based command and delivery are established. | The tick-14 claim is supported from those new facts; the earlier interval does not become uninterrupted. |

If the tick-13 trace is unavailable, the corresponding conclusion is unresolved instead of negative. If R1 changes to R2, use R2's actual coupling test for the new interval. Adding d2 requires d2's own report, return and coupling facts before asserting feedback for {d1,d2}.

A C.30.LCA description consumes the report and command relation references plus the compound assertion. It need not invent a single feedback occurrence to draw the supported connection. Claims about convergence, delay tolerance, disturbance damping, evidence, assurance or safety use their subject patterns.

#### B.2.5:5.2 - Scientific Theory Revision

A theory is revised when labs publish findings and a research community reviews anomalies and accepted revisions.

B.2.5 can state feedback around review and revision when the reviewed object is independently admitted as a Holon and the report, returned revision influence and coupling rule are established. Otherwise retain the independently supported review or source-use claims. Recover the exact admitted System that performs the review or revision, whether it is a research community, standards body, lab, review board, or tool-mediated group; any local system-role kind and assignment are separate claims. The theory remains the reviewed or revised episteme.

For publication channels, journals, datasets, reports, and review records, keep each object's identity distinct from its current publication or source-use relation; recover content, form, representation, or carrier only when the case depends on that distinction.

#### B.2.5:5.3 - Product Platform Policy

A product platform constrains component teams through interface rules and release gates. B.2.5 states the component reports, returned constraints and rule coupling those constraints to the reports for the admitted platform or governance system; a system-role kind or assignment is added only when separately current.

Work alignment uses `A.15`; a separate work-authority claim needs its own direct pattern. Gate passage uses `A.21`; `A.6.M` restores interface wording before the exact commitment claim returns to its direct pattern; architecture view uses `C.30.LCA` when the control structure is described.

### B.2.5:5.4 - Bias-Annotation

| Bias | How B.2.5 prevents it |
| --- | --- |
| Supervisor relation mistaken for parthood or containing-whole identity | The supervisor relation is not a parthood claim; `A.1` governs holon recognition, `A.14` the exact mereological claim, and `B.1` or `C.13` the applicable construction account. |
| Feedback-as-proof bias | A closed feedback relation may supply input to separate stability, safety, assurance, or timing work, but does not certify those claims. |
| Description-as-relation bias | A diagram, dashboard, report, or control-view description does not establish the in-life feedback relation by itself. |
| Episteme-agency bias | Only an independently recognized Holon fills a supervised reference. A theory, standard, model, dashboard, or publication may instead be used on the source side under its own kind and relation; the supervising acting system must still be named, and any system-role assignment is separate. |

### B.2.5:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-B2.5-1` | A conforming use names supervised holons and the supervising acting system; it adds the local supervisor system-role kind and exact assignment only when each independently obtains. |
| `CC-B2.5-2` | A conforming use names the observation, report, or source side and the influence, constraint, or objective side. It also names the coupling rule, its case facts, common applicability, temporal qualification and evidence that changes the compound claim or its later use. |
| `CC-B2.5-3` | The assertion is the conjunction of observation, return and coupling for every member of a nonempty supervised set. It introduces no fused U.Relation occurrence; a mathematical loop needs its separate C.29 use. |
| `CC-B2.5-4` | No `U.TransformerRef` or `U.InteractionRef` is created. |
| `CC-B2.5-5` | Parthood, control-structure view, base publication and source-use relations, and the compound feedback assertion are kept separate. Each base occurrence keeps its own identity and extent rules. |
| `CC-B2.5-6` | Stability, safety, timing, causal, evidence, assurance, gate, and mathematical-lens claims use the patterns that define or test them. |
| `CC-B2.5-7` | Episteme examples name the acting systems that perform review, revision, publication, or use. |

### B.2.5:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Unspecified supervisor-subholon feedback | Subholons are said to be coordinated through supervisor-subholon feedback, but no supervising acting system, medium, or feedback relation is named. | Recover the supervised holons, actual supervising System, observation side and returned influence side. Record that claim only when the receiving use needs it; add a system-role kind or assignment only when independently current. |
| Functional layer as component | A planning or control layer is modeled as a physical part of the controlled holon. | Separate parthood from feedback relation; use `C.30.LCA` for the view. |
| Perfect communication | State access is assumed instant, complete, or lossless. | Name medium or publication limits; use `C.27`, `A.3.3`, or evidence-use patterns for timing and information claims. |
| Episteme acts | A theory, model, paper, dashboard, or standard senses, judges, plans, or adapts. | Recover each exact acting System through A.13 and let A.15.1 independently admit the dated revision Work. Add F.6 only when the account expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; F.6 identifies neither assignment nor performer, and missing or failed F.6 leaves the Work intact. A short sentence may omit an unused assignment identifier. Name the Method or review practice structuring the Work when current, and any publication or source-use relation. This Work rule does not make assignment or system-role classification a condition of the supervisor-subholon feedback relation itself. |
| Relation certifies safety | The feedback relation is treated as evidence, assurance, gate, or safety result. | Keep the relation and use the pattern for the stronger claim. |

### B.2.5:8 - Consequences

Positive consequences:

- Supervisor-subholon language stays useful without creating false acting objects or false part-whole claims.
- Control diagrams, publication channels, and feedback relations can be coordinated without being collapsed.
- Stability, safety, assurance, gate, timing, and evidence claims stay inspectable.

Costs:

- A compound feedback description is only the beginning of stronger analysis.
- Some control diagrams need qualification because their stronger claims remain unproven.
- Episteme examples require explicit acting systems for review and revision.

### B.2.5:9 - Rationale

Supervisor-subholon feedback is a recurring relation in control, organization, architecture, and epistemic revision. It becomes precise only when separated from part-whole composition, control-structure views, publication and source-use relations, and stronger assurance claims.

The compound assertion supplies the present description use. A reusable feedback predicate or a dedicated relation kind is a further choice under A.6.RCD when a receiver needs it and the additional semantics are available. A mathematical loop remains a separately selected lens or structure.

### B.2.5:10 - SoTA-Echoing — establish the feedback claimed for this interval

**Practice question.** What is enough to say that a named controller and holon participated in feedback during a specified interval? The selected line requires observation, returned influence and their rule-governed coupling. A serious cheaper alternative describes the intended controller, feedback channel and command channel in a functional control structure. That description can answer a design question before any operation occurs; it cannot alone settle an assertion about an actual interval.

[Åström and Murray's Feedback Systems, Chapter 1 summary](https://fbswiki.org/wiki/index.php/Introduction) supplies the selected control-theoretic line: feedback involves reciprocal influence, and sensing, computation and actuation form the basic control loop. The same source treats stability and useful closed-loop behavior as further design questions. **Adapt** reciprocal influence into the three propositions in §4, retaining each domain's actual coupling rule. This supports a minimal descriptive assertion, not an import of continuous-time dynamics into organizational or episteme examples.

The [STPA Handbook, MIT-STAMP-001, March 2018, Chapter 2, pp. 22–25 and 45–48](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf) supplies the substantive control-structure comparator and failure analysis. It distinguishes a functional structure of possible information flow from physical structure, and examines missing, delayed or incorrectly used feedback. **Adopt** those distinctions for the view boundary in §4.4 and the interruption cases in §5.1. **Reject** using the diagram alone as an actual-interval witness; that shortcut is not a claim of the handbook. The handbook remains a source for analysis of control and unsafe scenarios, not a certificate that B.2.5's assertion establishes safety.

The difference is visible at ticks 10–14 in §5.1. The intended diagram can stay unchanged while a delivered broadcast is unrelated to the observation, a command is absent, or the link is broken. Testing the three propositions distinguishes those cases and treats an unavailable trace as unresolved. The comparison therefore governs §4.1's coupling and absence tests and `CC-B2.5-2–3`, while leaving C.30.LCA to describe the structure.

For an operational claim, both approaches can reuse the same controller rule and available trace; checking the relevant observation/return pair adds local work but closes a question the diagram leaves open. For an intended design, retain the cheaper structural description. A full dynamics model or STPA analysis costs more and answers stronger questions; it is needed only when those questions are selected. Reopen when the coupling rule, interval or member set changes, or a receiving use needs to reidentify one feedback occurrence across interruptions. These sources do not supply that new occurrence's identity rule or establish the FPF Holon classification of an organizational example.

### B.2.5:11 - Relations

- **Builds on:** `A.6.RCD` for the compound claim and `C.2.1` for its assertion; `A.1`, `A.2.1`, `A.12`, `A.3.4`, `A.15.1`, `B.1`, `A.14`, and `C.13`.
- **Coordinates with:** `B.2` when exact feedback facts leave a whole-reidentification question; evidence separately supports or challenges the claims about those facts.
- **Coordinates with:** `C.30.LCA` for control-structure view, `A.3.3` for dynamics, `C.27` for temporal and rate adequacy, `C.28` for causal use, `A.10` and `G.6` for evidence, `B.3` for assurance, `A.20` for its internal-constraint test in a transformation-flow structure, `A.21` for gate decisions, `A.6.M` for module-interface wording, and `C.29` for mathematical-lens use.
- **Uses:** `B.2.P` when emergence or MHT wording hides the claim kind, including feedback or supervision invoked as an emergence claim. Ordinary feedback wording follows F.19/E.10 restoration and its direct subject pattern.

### B.2.5:End
