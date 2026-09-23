---
name: fpf-problem-solving
description: "Use First Principles Framework (FPF) to decompose problems, architect systems, evaluate alternatives, define quality, recover and replace methods, disambiguate agent-relative instructions, steer or resume work, surface applicable methods, coordinate development states, bridge domain terms, screen mandatory steps, compare configurations, probe capability, decide under uncertainty, establish causality, reason about time, synthesize ontologies, govern ontic admission, publish views, revalidate sources, select representations, and appraise advice. Triggers: FPF, bounded contexts, SoTA packs, assurance calculus, decision theory, operational parsimony, causal/temporal reasoning, architecture, modularity, transformation flows, structural adequacy, cultural evolution, lexical discipline, Parts A-I. Not for simple task planning, general philosophy, or Agile unrelated to FPF."
---

# First Principles Framework (FPF)

## Attribution and license

This skill adapts *First Principles Framework (FPF)* by Anatoly Levenchuk,
[ailev/FPF](https://github.com/ailev/FPF), upstream commit
`4ddaf71557d4159e988cc61d2bd3088bfc1d2803`. The FPF specification text in
`sections/` is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Changes: the specification was split into section files and given generated navigation
indexes; this `SKILL.md` adds an agent-oriented router and usage instructions.
See the [upstream licensing scope](https://github.com/ailev/FPF/blob/main/LICENSING.md).
Skill packaging and the splitter are MIT licensed. This adaptation is not endorsed by
the FPF author.

An "Operating System for Thought" — a transdisciplinary architecture for reasoning,
written in human- and machine-readable pseudo-code. FPF turns raw intelligence (human or machine)
into organisationally usable reasoning: explicit bounded contexts, auditable artefacts, multi-view
descriptions, and disciplined hand-offs between specialised actors.

## Use cases

Use FPF whenever you need to think more rigorously than the situation's default.

- Decompose a messy, cross-domain problem into parts that can be reasoned about independently
- Make a high-stakes decision with incomplete evidence — and know what evidence is still missing
- Get a mixed team to reason together without vocabulary collisions or hidden assumptions
- Audit whether a conclusion is well-founded or just plausible
- Transform or transfer an insight without losing its subject, precision, or stated limitations
- Structure a proposal that must survive scrutiny from multiple expert perspectives
- Generate alternatives systematically instead of anchoring on the first idea
- Define what "better" means before comparing options
- Classify what kind of problem you're facing before searching for solutions
- Plan how an AI agent should select and sequence its tools under budget and trust constraints
- Make a decision under uncertainty — identify options, weigh evidence, and commit with an auditable rationale
- Establish whether X causes Y — or just correlates — and determine what intervention would work
- Publish a stable multi-view artifact without changing the source semantics
- Assemble or check a public framework publication form while preserving product-specific bodies and references
- Develop a holder system's capability for a named Work family and verify transfer in representative Work
- Synthesize source ontologies for one bounded authoring decision without flattening their local meanings
- Refresh a SoTA pack, benchmark, or evidence trail when evidence decays or telemetry changes
- Synthesize architecture candidates, compare structural options, or repair modularity/reuse claims
- Detect an ontic candidate, decide its first-use disposition, and govern whether a new concept or U-kind should be introduced instead of just renamed
- Identify the exact system that acts or is intended to change, then trace a lost path from outside use to architecture, production, and recursive builders
- Discover other systems that may bear relevant consequences before a decision closes
- Explain how constituent actions perform larger work and whether a replacement preserves each receiving use
- Recover a reusable method cautiously from several performances, logs, or observations without treating the evidence as the method itself
- Make instructions usable after a change of speaker, recipient, location, time, or other reference condition
- Choose the next action during ongoing work, resume interrupted work, or make applicable methods visible when current facts, authority, and stop conditions matter
- Coordinate whether a system or episteme is being explored, shaped, evaluated, or operated without confusing that state with claim assurance
- Preserve domain vocabulary while recovering which exact FPF value or relation a local term currently claims
- Recover the actual performer/support configuration for Work and test what survives interruption, handoff, delay, or reconfiguration
- Decide whether a proposed mandatory step, check, record, wait, or tool use changes a substantive result or only adds ceremony
- Compare what a finite addition, replacement, or intervention contributes relative to the current configuration
- Clarify what a claim about human, machine, organizational, or cultural “learning” actually says changed
- Clarify what “development” or “evolution” means by naming the changed subject, continuity rule, posture, and value basis
- Probe whether apparent capability loss is really an envelope, support, access, adaptation, enactment, or capability-change issue before choosing redevelopment
- Revalidate affected decisions when a relied-on source changes and the full set of receivers is unknown
- Request or reuse a bounded specialist result while preserving supplier authority and the receiving decision
- Select and combine diagrams, models, records, or other representations for one exact use
- Compare what structure a reader can correctly recover from an explanation under stated preparation, access, and time constraints
- Turn build, buy, reuse, outsource, or AI labels into comparable complete ways to obtain one result
- Check whether advice or an evidence demand helps the recipient’s decision and leads to a feasible next step
- Apply one selected FPF pattern to a current question and stop at the first useful result
- Construct a first model, apply an unfamiliar theory, recover an argument, or revise reasoning after a premise changes
- Connect physical, mathematical, and computational contributions into an interpretable answer
- Design a measurement relation and determine what its indications can actually resolve
- Track object identity across observations, describe constrained configurations, and retain information needed to predict change
- Develop new questions, reusable operations, and branching search from available results

## How to navigate

The use cases above help decide WHETHER to invoke FPF. The router below decides WHERE to go once invoked.

### Step 1 — Match the thinking need to a starting point

| What you need to do | Start here |
|---|---|
| **Decompose and model** a whole, track continuing objects, constrain configurations, or predict state changes | 05 Part A → A.1 Holons, A.1.1 Bounded Contexts, A.14 Mereology; A.1.RI object reidentification; A.3.3.CC constrained configurations, A.3.3.TR state change, A.3.3.PI prediction information |
| **Identify, trace, and discover** the acting or changed system, find omitted Systems that may bear consequences, then locate the first unsupported dependency from outside use through recursive builders | 05 Part A → A.1.SCR System Recognition, A.1.CSD Consequence-Bearer Discovery, A.1.STM System-Thinking Long Mantra; 03 FPF Readme → Recover a Lost Path |
| **Assign** system roles and responsibilities, **recover what “role” means**, **check permission**, or distinguish production work from the identity and completion of its product | 05 Part A → A.2 System Role Kinds and Assignments, A.2.8.PER Permission; 11 Part E → E.10.ROLE Role Meaning Recovery; 07 A.V → A.15 Role-Method-Work Alignment, A.15.PROD Production Work |
| **Recover a reusable method** from several performances or direct evidence without overclaiming Method identity | 05 Part A → A.3.1.MR Candidate-Method Recovery from Work Evidence |
| **Recover** what project, process, or case language directly refers to before modeling it | 07 A.V → A.15.6 Project, Process, and Case Recovery |
| **Steer, resume, and recovery-test Work** by choosing the next action from current facts, resuming after interruption, making applicable methods noticeable, or recovering the actual performer/support configuration and probing interruption, handoff, delay, or reconfiguration | 07 A.V → A.15.7 Situation-Responsive Work Steering, A.15.8 Work-Performance Configuration and Recovery Testing, A.15.10 Resume Interrupted Work, A.15.11 Make Applicable Methods Noticeable |
| **Screen mandatory work** for operational relevance before requiring a step, check, record, wait, cue, or tool use | 07 A.V → A.11.OP Decision-Relevant Least Action and Operational Parsimony |
| **Request or reuse specialist results** for one receiving decision while preserving the other practice’s authority | 07 A.V → A.15.9 Bounded Result from Another Practice |
| **Select and combine representations** for one exact action or decision without treating them as interchangeable | 09 Part C → C.37 Use-Bounded Representation Selection and Co-Use |
| **Set boundaries** on what statements mean, **recover agent-relative references** after a transfer, **distinguish relations** from their individuated occurrences, or derive a missing relation claim | 06 Signature Stack → A.6.B boundary norms, A.6.P.RI agent-relative reference recovery, A.6.REL relation obtaining and occurrences, A.6.RCD relation-claim derivation, declarations, gates, duties, and evidence |
| **Prevent category errors** or reconcile ontology premises before extending the framework | 07 Constitutional Principles → A.7 Strict Distinction, A.7.1 Consequence-Guided Ontological Problem Solving, A.7.2 Premise Reconciliation, A.7.CP Constructive Premise Compact |
| **Evaluate confidence** in a claim or artifact — including formality, scope, and reliability of the underlying knowledge | 08 Part B → B.3 Trust & Assurance; 09 Part C → C.2 KD-CAL / F-G-R scoring, C.2.2 Reliability, C.2.3 Formality |
| **Compose** parts into wholes, recover how actions enact larger work, and check constituent-method replacements | 08 Part B → B.1 Gamma algebra, B.1.5.EW encompassing Work, B.1.5.RS constituent replacement; 09 Part C → C.13 Compose-CAL, C.20 Discipline-CAL |
| **Reason through or coordinate development** — construct a model, use or compare theories, recover arguments or constructions, revise premises, bridge domain vocabulary, name whether a subject is explored/shaped/evidenced/operated, or develop a new question | 08 Part B → B.5 Reasoning Cycle, B.5.1 Explore → Shape → Evidence → Operate, B.5.2 Abductive Loop, B.5.3 Domain-Concept Bridge, B.5.4 concept recognition; B.5.FM first model, B.5.RA argument recovery, B.5.RC construction recovery, B.5.RR reasoning revision, B.5.TU theory use, B.5.TC theory comparison, B.5.QD new questions |
| **Enter and apply** FPF: choose a practical entry, find results across a DPF suite, or apply one pattern to a first useful result | 03 FPF Readme → Practical Entries; 11 Part E → E.11.DSG DPF Suite Reference, E.11.PUA Pattern Use |
| **Generate alternatives** / construct comparable ways to obtain one result, explore solution space, and keep apparatus use bounded | 09 Part C → C.38 Comparable Ways to Obtain One Result, C.39 result construction, C.39.RO reusable operations, C.40 branching search, C.40.CD co-development of problems and solutions; C.17 Creativity-CHR, C.18 Open-Ended Search, C.19 Explore-Exploit, C.19.2 Use-Bounded Apparatus Application |
| **Measure and compare** options, construct or repair measurement relations, and assess indication resolution | 07 A.V → A.17-A.19 Characteristics, CSLC & SelectorMechanism; 09 Part C → C.16 MM-CHR, C.16.MR measurement relation, C.16.IR indication resolution, C.16.RM measurement repair; 13 Part G → G.9 Parity / Benchmark Harness |
| **Resolve conflicts** across stakeholders or values | 10 Part D → Ethics, bias audit, conflict optimization |
| **Unify vocabulary or synthesize source ontologies** across teams or domains without flattening source-local claims | 12 Part F → F.0.2 Conceptual Synthesis, concept sets, bridges, UTS, lexical continuity |
| **Transform, document, publish, and reuse epistemes, views, or frameworks** while preserving subjects and product-specific bodies | 06 A.IV.A → A.6.2-A.6.4 episteme morphing/viewing/retargeting (separate exact arrow, bounded-use assertion, and current-case judgment), A.6.3.NAR narrative rendering, A.6.3.RT.OE operative expression; 11 Part E → E.4.PFIP Publication Integration, E.11.PFP Publication Form Profile, E.17 Multi-View Publication Kit |
| **Sharpen expression** — repair vague wording, recover exact method/work relations and model/explanation uses, clarify what “learning,” “development,” “evolution,” “interest,” or “curiosity” means in the current claim, surface ambiguity, or restore precision of epistemic / measurement / architecture terms | 06 A.IV.A → A.6.P.WMR Exact Relation Recovery, A.6.H Wholeness Unpacking; 11 Part E → E.10 model/explanation use, E.10.LRN, E.10.DEV, E.10.INT interest/curiosity, E.10.ARCH, E.17.EFP; 09 Part C → C.2.P, C.16.P, C.30.P |
| **Decide, appraise advice, or compare contributions** under uncertainty — compare a finite configuration change to the current configuration, structure options, weigh evidence, and commit with auditable rationale | 09 Part C → C.11.CRC Configuration-Relative Contribution Comparison, C.11 Decsn-CAL, C.11.DUA Decision-Useful Advice and Evidence Demands |
| **Reason about time and change** — distinguish state readings, trends, currentness, and intervention-sensitive change, or recover an actual temporal structure before testing coordination | 09 Part C → C.27 Temporal Claim Adequacy, C.27.TA Temporal Aspect; 03 FPF Readme → ACTUAL-TEMPORAL-STRUCTURE |
| **Establish causality** — climb the causality ladder, identify causal structure, check realizability | 09 Part C → C.28 CausalUse-CAL, C.28.MR mechanism replacement |
| **Connect mathematical and computational reasoning** — assess model fit, transfer results, realize computations, repair physical connections, compare symmetry transformations, or construct boundary balances | 09 Part C → C.29 Mathematical Lens Use, C.29.1 result transfer and symmetry, C.29.2 computational formulation, C.29.3 computational realization, C.29.BB boundary balance; 08 Part B → B.5.MPC physical/mathematical/computational connection, B.5.MPC.R repair |
| **Describe architecture or structural views** — characterize structure, unfold constraint-governed structure, produce adequate architectural descriptions and view types, triage cross-scope architectural residuals | 07 A.V → A.22 STRUCT-CAL, A.22.CGUS; 09 Part C → C.30, C.30.AD, C.30.ASV, C.30.LCA, C.30.ILC, C.30.TFS-REL |
| **Connect transformation flows** without collapsing independent structures into one flow or project | 11 Part E → E.18.NET Network of Transformation-Flow Structures |
| **Synthesize architecture** candidates or reconcile several non-isomorphic structures of one practice, then assess modularity/reuse or publish ADR-style projections | 09 Part C → C.31 Modularity, C.32 Architecture Candidate Synthesis, C.32.MWA Practice Architecture, C.32.PAD, C.32.ADR, C.32.ADA |
| **Assess structural information** — compare what a reader can recover from an explanation under stated conditions, or check architecture capture, source return, equivalence, morphisms, or discovery adequacy | 09 Part C → C.2.8 Extractable Structural Information, C.33, C.34, C.35 |
| **Model context-dependent or indeterminate states** — represent superposed, probe-coupled, or viability-bounded behaviour | 09 Part C → C.26 Quantum-Like Modeling Lens, C.26.1 Probe-Coupled Boundary, C.26.2 Enacted Distributed State, C.26.3 Viability-Envelope |
| **Survey a discipline** and build, ship, or refresh a reusable toolkit | 13 Part G → G.1-G.13 SoTA kit, CG-Frame, dispatcher, benchmarks, shipping, telemetry refresh, dashboards, external interop; 09 Part C → C.21 Discipline-CHR |
| **Classify** a problem type, test whether a candidate is admissible for a kind judgment, or compare kind identity before claiming a cross-local correspondence | 09 Part C → C.22 Problem-CHR, C.22.PFR Problematic-For Relation, C.3 Kind-CAL, C.3.2 Kind Judgment, C.3.3 KindBridge |
| **Define quality** attributes ("-ilities") as structured bundles | 09 Part C → C.25 Q-Bundle; 07 A.V → A.17-A.19 Characteristics |
| **Govern ontology** — detect an ontic candidate, decide its first-use disposition, and determine whether a new concept or U-kind is warranted | 11 Part E → E.24 Ontic Introduction Discipline, E.24.CD Ontic Candidate Detection and First-Use Disposition, E.24.UK U-kind Admission and Ontic Settlement |
| **Probe or develop capability** — distinguish apparent capability loss from envelope, support, access, adaptation, or enactment failures; when development is separately selected, test whether improvement transfers beyond an exercise | 11 Part E → E.23.CAE Capability Access and Expression Differential Probe, E.23.CDI Developing Capability for a Named Work Family |
| **Reason about cultural evolution** — describe cultural-evolution engineering or repair cultural-evolution wording | 09 Part C → C.36 Cultural Evolution, C.36.P Precision Restoration, C.36.RP sustaining and renewing shared work |
| **Orchestrate** agentic tool use under budgets and trust gates | 09 Part C → C.24 Agent-Tools-CAL |
| **Trace provenance and revalidate affected uses** when a relied-on source changes, or detect refresh debt | 07 A.V → A.10 Evidence Graph, A.10.1 Revalidate Affected Uses; 13 Part G → G.6 Provenance Ledger, G.11 Telemetry-Driven Refresh & Decay |

For complex problems, follow paths across multiple sections — the router shows where to start, not where to stop.

### Step 2 — Read the _index.md, then the sub-section

1. Open the `_index.md` of the target section folder — it lists all sub-sections with line counts and descriptions.
2. Read only the specific sub-section file you need.
3. Do NOT load entire sections. Pick the narrowest file that serves the user's question.

### Step 3 — Apply in plain language

Use plain language for the user. Introduce FPF-internal names (U.Holon, Gamma, F-G-R)
only when they add precision the user needs.

### Step 4 — Compose findings across sections

When a problem draws from multiple sections:

1. State each pattern's contribution in one line (e.g., "Bounded Contexts gives us the parts; Trust Calculus scores our confidence in each").
2. If patterns from different sections appear to conflict, check for category errors via A.7 Strict Distinction — the conflict is usually a level confusion (role vs. function, method vs. work), not a real contradiction.
3. Synthesize in natural order: decomposition first (what are the parts?), then evaluation (how confident are we?), then resolution (what do we do about gaps?).
4. Do not just list FPF patterns — weave them into a coherent answer to the user's actual question.

## Starter prompt (example — adapt to the user's actual role and need)

> You have the FPF specification loaded.
> Help me structure my project / problem / programme.
> Use plain language for an engineer-manager.
> Propose: (1) bounded contexts / specialisations, (2) decision criteria, (3) key alternatives,
> (4) hand-offs, and (5) missing evidence or tests before commitment.
> Introduce internal FPF names only when they add precision.

## Section INDEX

Structural reference. Each entry is a folder — read its `_index.md` first, then pick the sub-section.
Counts follow upstream H2 headings; the Preface includes its content-free `FPF.Preface:End` boundary marker.

| # | Section | Sub | When to use |
|---|---------|:---:|-------------|
| 01 | [Title page](sections/01-first-principles-framework---core-conceptual-specification/_index.md) | 0 | **Identify**: title, authorship, version date, top-level identity. |
| 02 | [Table of Contents](sections/02-table-of-contents/_index.md) | 0 | **Navigate**: locate a pattern, keyword, query cue, dependency, or neighboring section. |
| 03 | [FPF Readme](sections/03-first-principles-framework-readme/_index.md) | 11 | **Enter, onboard, and recover**: choose a practical entry, understand what each part contributes, connect actions to encompassing work, connect transformation flows, recover a lost path from outside use to recursive builders, or locate licensing and reuse terms. |
| 04 | [Preface](sections/04-preface/_index.md) | 22 | **Orient**: read philosophy, Architectural Rationale, shared source synthesis, profile choices, whole-combination conditions, uncertainty posture, and purpose/non-goals. |
| 05 | [Part A — Kernel](sections/05-part-a---kernel-architecture-cluster/_index.md) | 30 | **Decompose, identify, discover, trace, assign, recover, and authorize**: holons, bounded contexts, acting/changed-system recognition, consequence-bearing System discovery, outside-use dependency tracing, roles, permissions, candidate-Method recovery from Work evidence, transformers, method/work separation, object reidentification, constrained configurations, state-change rules, predictive information. |
| 06 | [A.IV.A — Signatures](sections/06-cluster-a-iv-a---signature-stack-boundary-discipline/_index.md) | 29 | **Set boundaries, recover references, derive relations, transform epistemes, and render**: recover agent-relative expressions after transfer; distinguish relations from occurrences; recover exact method/work and under-specified service/access relations; derive needed relation claims; keep source, receiving episteme, arrow, use claim, work, and publication distinct; classify statements, construct operative expressions, or render structure faithfully. |
| 07 | [A.V — Principles](sections/07-cluster-a-v---constitutional-principles-of-the-kernel/_index.md) | 49 | **Prevent confusion, remove ceremony, recover direct subjects, and steer, resume, or recovery-test Work**: category errors, ontology premises, decision-relevant operational parsimony, project/process/case language, situation-responsive next-action choice, interrupted-work resumption, making applicable methods noticeable, performer/support configuration and recovery probes, production-work identity, completion criteria and separate closure authority, measuring, comparing, evidence graphs and changed-source revalidation, bounded specialist results, mechanism suites, transformation-step constraint validity, independent-check gate decisions, constraint-governed unfolding. |
| 08 | [Part B — Reasoning](sections/08-part-b---trans-disciplinary-reasoning-cluster/_index.md) | 39 | **Compose, evaluate, and coordinate development**: structural views (STRUCT-CAL), aggregation (Gamma), constituent actions and encompassing Work, use-preserving Method replacement, trust scores, emergence, development states, domain-concept bridging, reasoning cycles, first models, concept recognition, theory use/comparison, argument and construction recovery, reasoning revision, new questions, physical/mathematical/computational connections. |
| 09 | [Part C — Extensions](sections/09-part-c---kernel-extension-specifications/_index.md) | 94 | **Score, compare, search, and architect**: epistemic quality, reader-extractable structural information, typed reasoning, measurement, configuration-relative contribution comparisons, comparable result routes, representation selection and co-use, decision-useful advice and evidence demands, decisions, bounded apparatus use, temporal/causal/math lenses, architecture synthesis across non-isomorphic practice structures, structural adequacy, cultural evolution, measurement construction/repair, result transfer, computational formulation/realization, symmetry comparison and boundary balances, reusable operations and branching search. |
| 10 | [Part D — Ethics](sections/10-part-d---multi-scale-ethics-and-conflict-optimization/_index.md) | 5 | **Resolve conflicts**: ethical trade-offs, bias auditing, safety overrides, conflict optimization. |
| 11 | [Part E — Constitution and Authoring](sections/11-part-e---the-fpf-constitution-and-authoring-guides/_index.md) | 68 | **Enter, apply, clarify, probe, develop, govern, reuse, and publish**: practical entry and pattern use, DPF-suite navigation, learning/development/evolution and interest/curiosity claim recovery, framework publication forms and preservation, capability access/expression probing and development for named Work, edition continuity, multi-view publication, transformation-flow networks, pattern quality, ontic/U-kind governance. |
| 12 | [Part F — Unification](sections/12-part-f---the-unification-suite-concept-sets-sensecells-and-system-role/_index.md) | 22 | **Synthesize and align**: bounded conceptual synthesis across source ontologies, concept sets, sense cells, bridges with separate bounded-use claims and reliance basis, system-role descriptions, UTS, lexical continuity. |
| 13 | [Part G — SoTA Kit](sections/13-part-g---discipline-sota-patterns-kit/_index.md) | 15 | **Harvest and refresh disciplines**: SoTA Packs, CG-Frames, dispatchers, provenance ledgers, benchmark harnesses, shipping, telemetry refresh, dashboards, external interop. |
| 14 | [Part H — Reserved](sections/14-part-h---reserved/_index.md) | 0 | **Reserve**: preserve the upstream Part H position for future specification content. |
| 15 | [Part I — Annexes](sections/15-part-i---annexes-extended-tutorials/_index.md) | 1 | **Walk through**: expanded entry disambiguation cases for high-risk or repeatedly misclassified first-pattern choices. |
