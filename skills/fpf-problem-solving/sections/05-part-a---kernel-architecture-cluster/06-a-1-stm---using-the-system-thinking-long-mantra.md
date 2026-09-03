## A.1.STM - Using the System-Thinking Long Mantra

> **Type:** Part A practitioner application pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain name.** Use the system-thinking long mantra.

**Mint or reuse.** This pattern introduces no U-kind, relation kind, project kind, case kind, map kind, or record kind. `A.1.STM` is a PatternID. *Long mantra* and *attention map* are Plain names for a repeatable reminder and its readable dependency display.

### A.1.STM:0 - Practitioner entry

**Use this when.** Use this pattern when a project team has, or is choosing, one common project system-of-interest but cannot tell which answer is missing on the map from the change expected outside that system to the work and systems that make or change it, and onward to the work and systems that make or change those builders. Use it also when a local result has no supported next fact connecting it to production or change, release, runtime use, or that outside change.

**First useful move.** Name the final result that matters now: a release, runtime use, or specific change expected outside the project system-of-interest. If a local result is current, say exactly what it is about and name the next supported fact needed to connect it to production or change, release, runtime use, or that outside change. Read backward only far enough to name the first answer that is absent, stale, disputed, or unsupported. Then state that exact question and use the one subject pattern whose `Use this when` accepts it as a locator for the required definition or constraint.

**Memorable reminder.**

> Start with the change needed outside the system the project is about. Choose that system and its boundary by that use; only then choose its inside. Ask how it will be made or changed, who or what can do that work, and what must make or change those builders. Read backward to the first unsupported answer. Follow real work and changes forward; for each local result, name the supported next fact that connects it to production or change, release, runtime use, or the outside change—or stop where that fact is missing.

This reminder is the Plain long mantra. Section 4 gives the working steps for using it.

**Not this pattern when.** If the current question is already one system-recognition, project designation, service/access, architecture, Method, Work, transformation, TFS/network, causal-use, evidence, or assurance question, use that direct pattern and stop there. Do not traverse the long map merely because a project mentions a project system-of-interest.

**What this buys.** The practitioner returns one located gap, one subject pattern, and one next question or action—or a truthful stop.

### A.1.STM:1 - Problem

A project can get every nearby statement locally right and still lose the long dependency. One team improves a component, another produces a builder, and another measures operation, yet nobody can show which supported relation carries those results toward use of the project system-of-interest. The gap is often hidden by a diagram arrow, the word *creates*, or a calendar sequence.

The opposite failure is to turn the reminder into a universal route. Then project Work becomes a network, a case becomes a slice type, a planned system is treated as already existing, and every arrow appears to be the same relation. A.1.STM keeps the long question visible while every local truth stays with its subject pattern.

### A.1.STM:2 - Forces

| Force | Tension |
| --- | --- |
| Whole-project coherence | A distant use must stay visible without making one pattern id or ClaimGraph stand for all intermediate subject assertions. |
| Outside before inside | Architecture is justified by a revisable external-use hypothesis, yet discovery and feedback may reopen that hypothesis. |
| Backward justification | Reading from value toward missing support is useful, but it is not temporal order or transformation direction. |
| Forward actuality | Work and changes must be traced through facts that obtain, not through planned arrows or shared names. |
| Local contribution | A team needs to know how its result matters without inventing a universal contribution relation. |
| Recursive builders | Build-the-builder reasoning must recur without a creator kind, fixed levels, or a generic `creates` edge. |
| Evidence and return | A supported answer may later become stale or fail; reopening should be local rather than restarting the whole map. |

### A.1.STM:3 - The attention map

Keep these regions visible. They are questions and result locations, not stages or fields of a record.

| Region | Plain question | Subject pattern or honest stop |
| --- | --- | --- |
| Outside change and use | What should become different for a beneficiary or relying use? | Use the relevant problem, plan, decision, promise, or description pattern. Return a missing or contested rationale when the expected use is not supported. |
| Project system-of-interest | Which system and boundary can support that use? | Use A.1/A.1.SCR for an existing system and A.15.6 for project designation. Keep an intended future system in plan or description content until identity inception. Test any local system-role kind and system-role assignment separately under A.2/A.2.1. |
| Runtime transformation and system participation | Which exact environment or input referent actually changes in use, and how does an already existing project system-of-interest participate? | Use A.3.4 for an actual bounded change of one continuing referent and the exact dynamics, interaction, causality, participation, or Work pattern for the system-side claim. Required behaviour, a use scenario, or an observed output proves no transformation. Causal or interaction participation supplies no work-facing assignment, Method, or Work. |
| Inside and architecture | Which internal organization could support the outside use? | Use C.32.P2S and the C.30 family. Keep architecture choice, selected structures, actual structures, descriptions, and views distinct. |
| Making or changing systems | Which Method, Work, existing materials or parts, production facts, and builder systems are needed? | Use A.3.1, A.3.4, the A.15 family, A.15.PROD, and A.12. Do not transform a system before it exists or infer change from Method or Work alone. |
| Joint network and builders | Which independently identified transformation-flow structures must be considered together for operation, production, identity inception, later change, verification, feedback, and recursive builders? | Use E.18 for each TFS and E.18.NET only when exact cross-member relation occurrences and endpoint bindings obtain. Otherwise keep a Plain provisional map and name the missing member, governor, predicate result, occurrence, or binding. |
| Local contribution | What is the team's exact subject and which supported relations connect its result to release or use? | Use the subject and relation patterns; use C.28 only for an actual causal-use claim. No generic `contributesTo` edge is implied. |
| Evidence, assurance, and return | What supports each load-bearing answer, what reliance is claimed, and what changed fact reopens it? | Use A.10 for claim-bound evidence and B.3 only for a named assurance use. Reopen the smallest answer whose basis changed. |

Read **backward** across these regions to justify a needed result and locate the first unsupported answer. This is logical attention, not didactic order, a WorkPlan, dated Work order, `U.Transfer`, or transformation direction.

Trace **forward** through independently grounded facts: performer systems and assignments, dated Work, changes of continuing referents, production participation, identity inception, completion, later use, and environment-side change. In the runtime region, identify the exact environment or input referent and its A.3.4 change separately from the direct causal, interaction, functioning, participation, or Work claim for the already existing project system-of-interest; add work-facing assignment, Method, or Work only when those claims separately obtain. These facts may occupy several TFS or network members. Shared identity or temporal adjacency connects none of them without a directly governed relation occurrence and its endpoint bindings.

### A.1.STM:4 - Solution

1. **Choose by the final result.** Name the release, runtime use, or specific change expected outside the project system-of-interest. If a local result is current, say exactly what it is about and ask which supported fact connects it next to production or change, release, runtime use, or that outside change. If another long mantra better matches the final result, leave A.1.STM.
2. **Place supported answers and the current scope.** Put only answers supported by named facts, observations, decisions, or results in the matching regions. At project level, name the admitted E.18.NET selection and its exact use question; before admission, keep a Plain provisional map and name the missing member, relation occurrence, or endpoint binding. In neither case call the network project Work. For one current case, state only four things in ordinary language: the exact subject or claim; the bounded references and direct claims needed to answer this closure question; the separately governed closure basis; and one named downstream receiving use that remains outside the closed case. Use A.15.6 to choose any technical reference form the case actually needs; do not copy those forms here. Keep plans, descriptions, Methods, Work, systems, changes, relations, evidence, and assurance distinct; do not turn this placement into a dossier or record schema.
3. **Find the first unsupported dependency.** Read backward from the final result and choose the earliest missing, stale, disputed, or unsupported answer that blocks the next dependency. *First* means logical firstness, not calendar firstness.
4. **Use one subject pattern.** Perform the working move described by the pattern whose `Use this when` accepts the missing question, and retain the resulting assertion or named stop. Do not copy its `Solution` into this pattern.
5. **Return only what the next use needs.** Put the answer back in the map. Select an E.18.NET network only when its members, relations, constraints, use frame, and endpoint bindings are grounded. Usually return the individual answers. Select another A.22 structure only when one named later task must reuse their organization as one thing and all four identity discriminators pass. Otherwise keep the direct plurality or Plain provisional map.
6. **Trace forward and test.** Follow actual Work, production and identity facts, later changes, participation in use, and environment-side changes through their subject patterns. Repeat for each relevant builder branch. Bind evidence to the claim it supports; stop at the first unsupported direct link and reopen only the smallest affected earlier answer.

Four orders remain separate throughout: the order used to teach the map; the logical dependency read backward; planned or actual Work order; and the subject relations that obtain. One ordering establishes none of the others.

### A.1.STM:5 - Minimal worked use

A pump-modernization project needs `PumpUnit-3` to restore reliable water delivery in its operating environment. The plan designates the already existing pump as the **project system-of-interest**. A.1 recognition, that designation, any `SystemOfInterestSystemRole`, and any system-role assignment remain four separate questions.

The team already supports the outside-use hypothesis and a controller-architecture choice. Reading backward exposes the first unsupported answer: can the planned controller result become an actual system ready for installation? The team leaves A.1.STM for the subject patterns. It identifies `ControllerSubassembly-7` and other pre-existing materials as the continuing subjects of any A.3.4 changes; recovers each actual fabricator's A.13 core; independently admits fabrication Work under A.15.1; and uses A.15.PROD separately for production participation, controller identity inception, and production completion. This minimal case consumes no exact assignment-bound attribution, so it does not open F.6. It does not describe transformation of the controller before the controller exists.

For the controller-production case, the subject and closure basis are explicit. The case closes only when the independently governed identity-inception, completion or readiness, evidence, and decision claims needed here pass. The named downstream receiving use—installation and later operation in `PumpUnit-3`—is visible but remains outside the closed case.

At project level, the team may select TFS members concerning controller production, pump modification, qualification, and pump operation together under E.18.NET only after each member is independently identified and the required production, installation, participation, use, or feedback occurrences and endpoint bindings obtain. Until then the network remains a Plain provisional explanation with the missing link named. Actual facts are then traced forward from fabrication Work and changes, through controller inception and pump modification, to later pump operation. When runtime use is claimed, the already existing `PumpUnit-3` and its direct participation claim remain separate. If dated runtime Work is claimed, recover every performer's A.13 core and independently admit the occurrence under A.15.1; add F.6 only when precise assignment-bound attribution is also current. Keep either actor-side claim separate from any A.3.4 change of one exact continuing delivery-side environment or input referent; the expected reliable-delivery hypothesis alone establishes neither actuality. A failed relation or missing binding stops that claim without erasing the valid local results.

If later operation shows that reliable water delivery depends on an upstream reservoir-control assembly outside the proposed `PumpUnit-3` boundary, the team reopens the outside-use, project designation, and boundary hypotheses before revising the architecture and network selection. It does not preserve the old inside merely because Work has already begun.

### A.1.STM:6 - Direct exits and near misses

| Current question | Leave through | Near miss blocked here |
| --- | --- | --- |
| Is this exact existing entity a system? | A.1 and A.1.SCR | A noun, diagram box, plan, system-role label or assignment, or capability does not establish systemhood. |
| Which omitted Systems may undergo relevant changes that alter the current decision or investigation? | A.1.CSD | Use the current frame as a starting point for A.1.CSD's bounded search; keep possible paths modal until their direct predicates are supported. |
| Which system is this project about? | A.15.6 | Keep system identity, project designation, system-role-kind interpretation, and any system-role assignment distinct. |
| What is promised, provided, connected, permitted, or stopped? | A.6.P §4.11a, then its subject pattern | *Service* or *access* does not select a system or one service bundle. |
| Which inside could support the outside use? | C.32.P2S and C.30 family | Architecture chosen before a stated outside-use hypothesis must return to that missing basis. |
| What actual runtime change and system participation obtain? | A.3.4 and the exact dynamics, interaction, causality, participation, assignment, Method, or Work pattern needed by the claim | An expected effect, required behaviour, observed output, or project designation proves neither an actual change nor an actor-side or Work claim. |
| What reusable way, performed occurrence, or actual change is current? | A.3.1, A.15.1, or A.3.4 | Method, Work, and Transformation are different objects and none proves the others. |
| Did production, identity inception, completion, or readiness occur? | A.15.PROD, A.15.5, and A.21 as applicable | A final visible step, result label, or `DesignRunTag` proves none of these claims. |
| Is this one TFS, an internal subflow, or a network? | E.18 and E.18.NET | A graph shape, shared entity, or `creates` label does not identify a network or relation. |
| Does evidence support this claim, and may a receiver rely on it? | A.10 and B.3 | Evidence availability and assurance are not truth, actuality, or map completion. |

### A.1.STM:7 - Recognition stress boundary

Before a map relies on an acting system or changed-system boundary, use the one A.1 recognition architecture through A.1.SCR. Its heterogeneous stress cases cover an engineered pump, an animal, a human, a software-realized AI agent, a robotic AI agent, a coordinated collective and roster near miss, the Moon and a tide bearer, plus the exact proposed-system readings `SutureControl-M17`, `GameSessionWhole-GS204`, and `InternetAccessArrangement-CA17` beside their ordinary subject-pattern readings.

A.1.STM consumes only the returned recognition result. It does not repeat the six-component test, replace the exact entity with a convenient neighboring bearer, infer a system-role assignment from causal participation, or infer Method, Work, transformation, promise, permission, project designation, or a system-role kind from systemhood.

### A.1.STM:8 - Conformance checklist

| ID | Check |
| --- | --- |
| `CC-A1-STM-1` | The intended final result and the first unsupported logical dependency are readable without decoding a technical record. |
| `CC-A1-STM-2` | Expected outside use and the project-system boundary are stated before internal architecture is justified; the actual runtime transformation of an exact environment or input referent and any system participation remain separately governed, and feedback may reopen the earlier hypotheses. |
| `CC-A1-STM-3` | Project system-of-interest identity, project designation, system-role-kind interpretation, and system-role assignment remain separate. |
| `CC-A1-STM-4` | Project Work, an admitted project-level network selection or Plain provisional map, and one minimal case placement retain their own identities; the case states an exact subject or claim, only the bounded references and direct claims needed now, its closure basis, and a named downstream use that remains outside. |
| `CC-A1-STM-5` | Backward attention, forward actuality, didactic order, Work order, and direct subject relations are not substituted for one another. |
| `CC-A1-STM-6` | Every local answer is one exact assertion under its subject predicate, with the pattern retained only as a locator, or a truthful stop. |
| `CC-A1-STM-7` | A case names one subject or claim, its closure basis, and a downstream receiving use that is explicitly outside the closed case. |
| `CC-A1-STM-8` | An admitted network has independently identified members, exact obtaining cross-member relations, applied constraints, a use frame, and complete endpoint bindings; otherwise the map stays provisional. |
| `CC-A1-STM-9` | Expected environmental effect, actual runtime transformation and system participation, production, identity inception, completion, later change, and use are separately grounded; required behaviour is not actuality, and no not-yet-existing system is transformed. |
| `CC-A1-STM-10` | Evidence is bound to its claim, assurance is limited to a named reliance use, and changed grounds reopen only the smallest affected answer. |

### A.1.STM:9 - Common anti-patterns

| Anti-pattern | Repair |
| --- | --- |
| Mantra as algorithm | Restore the map as an attention aid; use direct patterns for every result and WorkPlan for planned order. |
| Project equals network | Keep actual project as composite `U.Work` and E.18.NET as a selected non-agentive `U.Structure`. |
| Case equals subnetwork | Name the case subject, closure basis, bounded references, and excluded downstream use; select a structure only when one receiving use needs the whole organization. |
| Creator graph import | Identify TFS or nested-network members and exact cross-member occurrences; add no creator kind or generic `creates` edge. |
| Shared entity as edge | Name the directly governed production, inception, participation, use, feedback, or other occurrence and bind its participants. |
| Architecture first | Return to the outside-use and boundary hypothesis before justifying internal structure. |
| Intended system acts | Keep it in plan or description content until identity inception; only an existing admitted system can perform Work. |
| Systemhood proves Work | Test causal participation, system-role assignment, Method, Work, and transformation separately. |

### A.1.STM:10 - Consequences

**Benefits.** Teams can locate a missing long-range dependency. Local results remain usable, builder recursion remains visible, and a missing relation stays an explicit stop rather than becoming a convenient arrow.

**Costs.** Practitioners must name the final result, keep several kinds of order apart, and return to subject patterns for local truth. A provisional map may remain incomplete for a long time.

**Limits.** This pattern does not identify a system, designate a project system-of-interest, select architecture, admit Work or transformation, close a case, identify a TFS network, or establish evidence or assurance. It only governs how a practitioner uses the long attention map to find and return the next result.

### A.1.STM:11 - SoTA-Echoing

> **Informative.** These sources provide bounded pressure on use of the long attention map. The named subject patterns remain authoritative for kinds, relations, participants, and pass conditions.

| Source | Useful pressure for this pattern | Disposition | A.1.STM action, stop, or limit affected |
| --- | --- | --- | --- |
| R5 *Systems Thinking* and R6–R8 systems guides, across their current and historical forms | Systems practice starts with the use or change sought outside the project system-of-interest, then justifies its boundary and internal organization, while allowing evidence and iteration to reopen those hypotheses. | **Adopt outside-before-inside; adapt system-of-interest to a separate project designation; reject function, role, or name as identity.** | A.1.STM:3 places outside use and project-system boundary before architecture, and :5 reopens both when operation contradicts them. The designation supplies neither A.1 systemhood nor a system-role assignment, and *project system-of-interest* carries no target- or goal-derived semantics. |
| Rival R5–R9 mantra formulations and the seminar long/local-mantra account | The useful constant is sustained attention from a final use to distant support, entry at the first unsupported answer, backward justification, forward actuality, and return—not one canonical sentence or step sequence. | **Adopt the attention and training function; synthesize the variants; reject algorithm, fixed sequence, and default CGUS readings.** | A.1.STM:0 chooses the map by the final result; :3 separates backward reasoning from forward facts; :4 opens one subject pattern and returns its result. The reminder is neither the `Solution`, a Method, WorkPlan, calendar order, nor an admitted demonstrative structure. |
| R5/R6 recursive-builder practice and their `CreatorGraph` renderings, read with current E.18 and E.18.NET | Build-the-builder reasoning must consider operation, production, identity inception, later change, feedback, and builder branches together, but the picture alone supplies no members or relations. | **Adapt recursion to independently identified TFS or nested-network members; reject creator-graph ontology and universal edges.** | The `Joint network and builders` region, Solution steps 2, 5, and 6, and the pump worked use require exact cross-member occurrences and endpoint bindings. Shared identity, a `creates` label, or temporal adjacency does not admit a network or connect two members. |
| Guide whole-project and local-focus contrasts, read with current A.15.6, E.18, and E.18.NET | A project team needs both the longer project dependency and a bounded local concern, but the guide picture does not by itself distinguish project Work, network selection, case subject, closure, and later use. | **Adapt to a minimal subject- or claim-centred case result; reject project=network, case=slice, and dossier readings.** | Solution step 2 and the pump worked use name the exact subject or claim, only the references and direct claims needed now, a separately governed closure basis, and one downstream receiving use that remains outside the closed case. Project-level reasoning may continue into that later member without reopening the closed case as a record. |
| Deutsch, [*Constructor Theory*](https://arxiv.org/abs/1210.7439), 2012, read with current A.3.4, A.15.PROD, and E.18 | Required behavior and possible production or change depend on exact substrates, conditions, and constructor-side facts; a task or description is not an actual occurrence. | **Adopt the possibility/actuality pressure; adapt it to FPF subject patterns; reject actuality from requirement, Method, or Work alone.** | The runtime and making/changing regions, forward trace, and worked use distinguish one continuing changed referent, production participation, identity inception, later use, and system-side participation. A not-yet-existing system is not transformed, and required behavior proves no actual change. |
| R5/R6 function, role, service, access, and “our system” variants | Familiar words can point to a system, capability, role, Work, Method, promise, state, bearer, arrangement, or another directly governed object; they do not agree on one default referent or universal contribution relation. | **Adopt the need to keep the long dependency visible; adapt every local claim to its exact subject predicate and retain the pattern only as a locator; reject lexical defaults and generic contribution.** | The `Local contribution` region and neighboring subject results require the exact subject and supported production, installation, participation, release, use, causal, evidence, or other relation. Service/access wording first undergoes A.6.P recovery; a missing direct link stops the long-map claim. |

The reconciliation of long-mantra attention, subject-qualified results or blockers, minimal case closure, and E.18.NET recursion is a scoped FPF synthesis of these pressures, not an external consensus claim. Reopen the smallest affected clause if practitioner testing cannot distinguish the map from the `Solution`, a WorkPlan, or CGUS; if outside-before-inside or system-of-interest practice changes; if E.18.NET cannot express recursive builders without false membership; if a case exposes a missing runtime, closure, relation predicate, or link; or if *creator graph*, *function/role*, *service*, target-like system wording, fixed sequence, or a universal contribution edge again becomes load-bearing.

### A.1.STM:12 - Rationale

The useful inheritance from systems-thinking mantras is the connected attention span: expected outside change and project-system boundary, separately grounded runtime transformation and participation, internal organization, making or changing the system, and recursive builders. FPF preserves that span while rejecting a single algorithm, a creator graph ontology, word-induced systemhood, and a universal route. Project-level network placement and a minimal subject- or claim-centred case placement keep the span usable without identifying project, network, case, or record. The smallest reusable account is therefore a thin use pattern beside A.1, not an expansion of system recognition or architecture.

### A.1.STM:13 - Relations

- **Builds on:** the Plain long/local boundary in Preface; `A.1` and `A.1.SCR` for exact system recognition; and `A.15.6` for project system-of-interest designation, actual project Work, and subject- or claim-centred case recovery.
- **Coordinates with:** `C.32.P2S` and the C.30 family for outside-use-to-architecture reasoning; `A.3.4` and the patterns for exact dynamics, interaction, causality, participation, assignment, Method, and Work claims in runtime change and system participation; `A.2` and `A.2.1` for system-role-kind interpretation and assignment; `A.3.1`, `A.12`, the A.15 family, `A.15.PROD`, `A.15.5`, and `A.21` for Method, Work, production, identity, readiness, and gates; `E.18` and `E.18.NET` for TFS and project-level network selection; `A.15.6` for the minimal case recovery and closure boundary; `A.10` and `B.3` for evidence and assurance; `A.1.CSD` when the missing answer is which other Systems may undergo relevant changes; and `C.28` only for actual causal-use claims.
- **Optional demonstration:** `A.22.CGUS` may govern a separately admitted demonstrative unfolding slice. Ordinary use of this long mantra requires no CGUS, F.17 row, durable card, or registration.
- **Does not replace:** any direct pattern named above. A.1.STM returns that pattern's result or stop to the attention map and defines no world-side predicate.

### A.1.STM:End

