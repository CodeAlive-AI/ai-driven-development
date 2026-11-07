---
name: fpf-problem-solving
description: "Use the First Principles Framework (FPF) Library, Core plus 36 domain frameworks (DPFs) stored locally, to think more rigorously than the situation's default: decompose problems, architect systems, generate real alternatives, decide under uncertainty, reconsider decisions, establish causality, design control loops, recover and improve methods, steer, hand off or resume agent work, check sources and evidence, explain, rewrite text plainly, define quality, and apply field methods for strategy, goals/OKR, operations, management, research, decision design, systems engineering, knowledge access, mathematics, notation, narrative and human capability. Triggers: FPF, DPF, fpf.tools, Levenchuk, a pattern ID such as F.19, C.11.DUA, A.15.10, GOALS.7 or STR.18, bounded contexts, assurance, SoTA packs, operational parsimony, causal/temporal reasoning, modularity, lexical discipline. Not for simple task planning, general philosophy, or Agile unrelated to FPF."
---

# First Principles Framework (FPF) Library

## Attribution and license

This skill adapts the *FPF Library* by Anatoly Levenchuk — *First Principles Framework (FPF)*
Core, its domain frameworks (DPFs) and Library documents —
[ailev/FPF](https://github.com/ailev/FPF), upstream commit
`760424e38bff3b24c856ce798871402248ccb6bc`. The Library text in `sections/`, `dpfs/` and
`library/` is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Changes: the publications were split into section files with generated navigation indexes,
and their links were rewritten to point at the local files; this `SKILL.md` adds an
agent-oriented router and usage instructions. Map C paraphrases Anatoly Levenchuk's
cheatsheet of frequently used FPF patterns (November 2026).
See the [upstream licensing scope](https://github.com/ailev/FPF/blob/main/LICENSING.md).
Skill packaging and scripts are MIT licensed. This adaptation is not endorsed by
the FPF author.

An "Operating System for Thought" — a transdisciplinary architecture for reasoning,
written in human- and machine-readable pseudo-code. FPF turns raw intelligence (human or machine)
into organisationally usable reasoning: explicit bounded contexts, auditable artefacts, multi-view
descriptions, and disciplined hand-offs between specialised actors.

The Library has two layers, both stored locally:

- **FPF Core** (`sections/`) — transdisciplinary patterns with IDs such as `A.7`, `C.11.DUA`, `F.19`.
- **36 domain frameworks (DPFs)** (`dpfs/`) — methods of one field, with IDs such as `GOALS.7`,
  `STR.18`, `RMP.7`. Four Suites (Engineering, Management, Foundational Thinking, Human Capability
  Engineering) group related fields; the other frameworks stand alone. A DPF method builds on the
  Core patterns it names.

## Use cases

Use FPF whenever you need to think more rigorously than the situation's default.

- Apply a named FPF or DPF pattern (F.19, C.11.DUA, GOALS.7) to the current text, answer or task
- Repair a recurring trouble in work with an agent: hedging instead of judgment, a lost original question, restarting after a handoff, look-alike alternatives, a plan passed off as done work
- Answer a field question with that field's framework: strategy, goals and OKR, operations, marketing, finance, research, decisions, systems engineering, explanation, narrative, teaching people
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
- Reconsider a prior decision when new outcomes or changed conditions may invalidate its relied-on basis
- Establish whether X causes Y — or just correlates — and determine what intervention would work
- Connect observations, choices, and actions into a control loop with explicit feedback and decision points
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
- Qualify, trial, describe, transfer, compose, and introduce methods while checking their contribution and provision
- Develop opportunities, attainable problems, and support configurations from current results
- Fit checklist questions, criteria, and checking means to an occasion, then reconcile shared results
- Recover a reusable method cautiously from several performances, logs, or observations without treating the evidence as the method itself
- Make instructions usable after a change of speaker, recipient, location, time, or other reference condition
- Choose the next action during ongoing work, resume interrupted work, or make applicable methods visible when current facts, authority, and stop conditions matter
- Turn an ordinary handover, result demonstration, or successful workaround into a bounded question with a useful next move
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
- Compare continuation rules using bounded recorded histories without exposing future outcomes
- Test whether an evaluation can imitate improvement, rebuild affected evidence after evaluation changes, or improve the way further improvements are obtained
- Develop a line of thought from working notes, preserving its grounds and the relations that make a later continuation useful

## How to navigate

The use cases above help decide WHETHER to invoke FPF. The maps below decide WHERE to go once invoked.
All paths are relative to this skill's directory. Every ID resolves with one command:

```bash
python3 scripts/find_pattern.py C.11.DUA        # PatternID → file, section map, publication
python3 scripts/find_pattern.py HCD.12:4.1      # section reference → the line inside the file
python3 scripts/find_pattern.py GOALS           # DocID → the framework's entry file and practical entries
python3 scripts/find_pattern.py --search okr    # words → matching titles, keywords and queries
```

Without Python: `grep -F "| C.11.DUA |" PATTERN-INDEX.md` gives the file in the third column.

### Step 0 — Choose the map by how FPF came up

| What you have | Go to |
|---|---|
| A **pattern ID, section reference or DocID** — "apply F.19", "use C.11.DUA", "GOALS.7", "HCD.12:4.1", "EXD" | Resolve it with `find_pattern.py` and read that file (Step 2). Skip the maps. |
| A **familiar trouble** in work with an agent, a text, sources, an explanation, options or a plan | **Map C — Common troubles** |
| A **question inside a field** — strategy, goals/OKR, operations, marketing, finance, research, decisions, systems engineering, knowledge access, mathematics, explanation, teaching people | **Map B — Domain frameworks** |
| A **general thinking need** — decompose, identify, decide, compare, establish cause, architect, revise, publish | **Map A — Core router** |
| Nothing above fits, or you are unsure | `find_pattern.py --search <two or three words>`, then read the best hit's `_index.md` |

A field question often needs both layers: the DPF supplies the field's method and conditions, the Core
patterns it cites supply the general reasoning. Follow a Core ID from a DPF file the same way.

### Map A — Core router (thinking need → Core pattern)

Find the group first, then the row. Each row names the section folder and the patterns to start with.

#### A1. Model the subject — what it is, its parts, roles, and what words refer to

| What you need to do | Start here |
|---|---|
| **Decompose and model** a whole, track continuing objects, constrain configurations, or predict state changes | 05 Part A → A.1 Holons, A.1.1 Bounded Contexts, A.14 Mereology; A.1.RI object reidentification; A.3.3.CC constrained configurations, A.3.3.TR state change, A.3.3.PI prediction information |
| **Identify, trace, and discover** the acting or changed system, find omitted Systems that may bear consequences, then locate the first unsupported dependency from outside use through recursive builders | 05 Part A → A.1.SCR System Recognition, A.1.CSD Consequence-Bearer Discovery, A.1.STM System-Thinking Long Mantra; 03 FPF Readme → Recover a Lost Path |
| **Assign** system roles and responsibilities, **recover what “role” means**, **check permission**, or distinguish production work from the identity and completion of its product | 05 Part A → A.2 System Role Kinds and Assignments, A.2.8.PER Permission; 11 Part E → E.10.ROLE Role Meaning Recovery; 07 A.V → A.15 Role-Method-Work Alignment, A.15.PROD Production Work |
| **Recover** what project, process, or case language directly refers to before modeling it | 07 A.V → A.15.6 Project, Process, and Case Recovery |
| **Set boundaries** on what statements mean, **recover agent-relative references** after a transfer, **distinguish relations** from their individuated occurrences, or derive a missing relation claim | 06 Signature Stack → A.6.B boundary norms, A.6.P.RI agent-relative reference recovery, A.6.REL relation obtaining and occurrences, A.6.RCD relation-claim derivation, declarations, gates, duties, and evidence |
| **Prevent category errors** — a plan taken for done work, a description for a running system, a tool for a skill — or reconcile ontology premises before extending the framework | 07 Constitutional Principles → A.7 Strict Distinction, A.7.1 Consequence-Guided Ontological Problem Solving, A.7.2 Premise Reconciliation, A.7.CP Constructive Premise Compact |
| **Model context-dependent or indeterminate states** — represent superposed, probe-coupled, or viability-bounded behaviour | 09 Part C → C.26 Quantum-Like Modeling Lens, C.26.1 Probe-Coupled Boundary, C.26.2 Enacted Distributed State, C.26.3 Viability-Envelope |
| **Classify** a problem type, test whether a candidate is admissible for a kind judgment, or compare kind identity before claiming a cross-local correspondence | 09 Part C → C.22 Problem-CHR, C.22.PFR Problematic-For Relation, C.3 Kind-CAL, C.3.2 Kind Judgment, C.3.3 KindBridge |
| **Govern ontology** — detect an ontic candidate, decide its first-use disposition, and determine whether a new concept or U-kind is warranted | 11 Part E → E.24 Ontic Introduction Discipline, E.24.CD Ontic Candidate Detection and First-Use Disposition, E.24.UK U-kind Admission and Ontic Settlement |

#### A2. Reason, evaluate, and decide

| What you need to do | Start here |
|---|---|
| **Evaluate confidence** in a claim or artifact — including formality, scope, and reliability of the underlying knowledge | 08 Part B → B.3 Trust & Assurance; 09 Part C → C.2 KD-CAL / F-G-R scoring, C.2.2 Reliability, C.2.3 Formality |
| **Reason through or coordinate development** — initiate inquiry from ordinary work, develop a line of thought through working notes, construct a model, use or compare theories, recover arguments or constructions, revise premises, bridge domain vocabulary, name whether a subject is explored/shaped/evidenced/operated, or develop a new question | 08 Part B → B.5 Reasoning Cycle, B.5.PI inquiry from ongoing work, B.5.WN working notes, B.5.1 Explore → Shape → Evidence → Operate, B.5.2 Abductive Loop, B.5.3 Domain-Concept Bridge, B.5.4 concept recognition; B.5.FM first model, B.5.RA argument recovery, B.5.RC construction recovery, B.5.RR reasoning revision, B.5.TU theory use, B.5.TC theory comparison, B.5.QD new questions, B.5.SD substantive discussion |
| **Measure and compare** options, construct or repair measurement relations, and assess indication resolution | 07 A.V → A.17-A.19 Characteristics, CSLC & SelectorMechanism; 09 Part C → C.16 MM-CHR, C.16.MR measurement relation, C.16.IR indication resolution, C.16.RM measurement repair; 13 Part G → G.9 Parity / Benchmark Harness |
| **Decide, reconsider, appraise advice, or compare contributions** under uncertainty — compare a finite configuration change to the current configuration, determine whether changed conditions alter a prior decision’s basis, structure options, weigh evidence, and commit with auditable rationale | 09 Part C → C.11.CRC Configuration-Relative Contribution Comparison, C.11.MV method-option worth, C.11 Decsn-CAL, C.11.DBR Decision-Basis Reconsideration, C.11.DUA Decision-Useful Advice and Evidence Demands |
| **Reason about time and change** — distinguish state readings, trends, currentness, and intervention-sensitive change, or recover an actual temporal structure before testing coordination | 09 Part C → C.27 Temporal Claim Adequacy, C.27.TA Temporal Aspect; 03 FPF Readme → ACTUAL-TEMPORAL-STRUCTURE |
| **Establish causality** — climb the causality ladder, construct or challenge a causal model, identify causal structure, and check realizability | 09 Part C → C.28 CausalUse-CAL, C.28.CM causal-model construction/challenge, C.28.MR mechanism replacement |
| **Design a control loop** — connect observations, choices, and actions without losing their feedback or decision relations | 09 Part C → C.43 Connect Observation, Choice and Action in Control |
| **Connect mathematical and computational reasoning** — assess model fit, transfer results, realize computations, repair physical connections, compare symmetry transformations, or construct boundary balances | 09 Part C → C.29 Mathematical Lens Use, C.29.1 result transfer and symmetry, C.29.2 computational formulation, C.29.3 computational realization, C.29.BB boundary balance; 08 Part B → B.5.MPC physical/mathematical/computational connection, B.5.MPC.R repair |
| **Resolve conflicts** across stakeholders or values | 10 Part D → Ethics, bias audit, conflict optimization |
| **Define quality** attributes ("-ilities") as structured bundles | 09 Part C → C.25 Q-Bundle; 07 A.V → A.17-A.19 Characteristics |

#### A3. Find ways to obtain results and improve work

| What you need to do | Start here |
|---|---|
| **Recover, qualify, and develop methods** from performances or documentary sources, identify worthwhile improvements, return a partial result to its original question, develop a whole-subject account, trial intended contributions, check coherence and transfer, maintain variants, and introduce them into practice | 05 Part A → A.3.1.MR, A.3.1.DR, A.3.1.QM, A.3.1.WT, A.3.1.CC, A.3.1.FT, A.3.1.MV, A.3.1.MI; A.3.2.DE method descriptions; 09 Part C → C.39.QR original-question return, C.39.WA whole-subject account, C.39.MF development focus, C.39.WI worthwhile improvements, C.39.RQ situated requirements, C.39.RP repertoire, C.39.MC changed conditions |
| **Steer, resume, and recovery-test Work** by choosing the next action from current facts, resuming after interruption, making applicable methods noticeable, or recovering the actual performer/support configuration and probing interruption, handoff, delay, or reconfiguration | 07 A.V → A.15.7 Situation-Responsive Work Steering, A.15.8 Work-Performance Configuration and Recovery Testing, A.15.8.MS methodological support, A.15.10 Resume Interrupted Work, A.15.11 Make Applicable Methods Noticeable |
| **Screen mandatory work** for operational relevance before requiring a step, check, record, wait, cue, or tool use | 07 A.V → A.11.OP Decision-Relevant Least Action and Operational Parsimony; 09 Part C → C.42 Reduce Avoidable Work While Preserving the Needed Result |
| **Request or reuse specialist results** for one receiving decision while preserving the other practice’s authority | 07 A.V → A.15.9 Bounded Result from Another Practice |
| **Generate alternatives** / construct comparable ways to obtain one result, explore solution space, keep the original question and whole subject in view, and keep apparatus use bounded | 09 Part C → C.38 Comparable Ways to Obtain One Result, C.39 result construction, C.39.QR original-question return, C.39.WA whole-subject account, C.39.RO reusable operations, C.40 branching search and §4.8.1 recorded-history replay, C.40.CD co-development of problems and solutions; C.40.OD open-ended development, C.40.OC subject characterization, C.40.OI opportunity inquiry, C.40.OCN bounded opportunities, C.40.PC worthwhile problems/contributions, C.40.DC support configurations, C.40.JF joint reachability, C.40.JD joint development, C.40.NU neighboring uses/means, C.40.NP attainable problems, C.40.OP stepping stones, C.40.RQ requalification; C.17 Creativity-CHR, C.18 Open-Ended Search, C.19 Explore-Exploit, C.19.2 Use-Bounded Apparatus Application |
| **Compose** parts into wholes, recover how actions enact larger work, and check constituent-method replacements | 08 Part B → B.1 Gamma algebra, B.1.5.EW encompassing Work, B.1.5.RS constituent replacement, B.1.5.CM composite Method qualification; 09 Part C → C.13 Compose-CAL, C.20 Discipline-CAL |
| **Use checklists** to select questions for a result, fit the occasion, qualify criteria and checking means, preserve questions in templates, act on answers, and reconcile shared checks | 09 Part C → C.41, C.41.OF, C.41.QC, C.41.TF, C.41.UA, C.41.SR |
| **Probe or develop capability** — distinguish apparent capability loss from envelope, support, access, adaptation, or enactment failures; when development is separately selected, test whether improvement transfers beyond an exercise | 11 Part E → E.23 Quality Improvement Loop (no-change comparisons, changed-evaluation evidence, improving improvement methods), E.23.CAE Capability Access and Expression Differential Probe, E.23.CDI Developing Capability for a Named Work Family |
| **Orchestrate** agentic tool use under budgets and trust gates | 09 Part C → C.24 Agent-Tools-CAL |
| **Reason about cultural evolution** — describe cultural-evolution engineering or repair cultural-evolution wording | 09 Part C → C.36 Cultural Evolution, C.36.P Precision Restoration, C.36.RP sustaining and renewing shared work, C.36.MC method culture |
| **Survey a discipline** and build, ship, or refresh a reusable toolkit | 13 Part G → G.1-G.13 SoTA kit, CG-Frame, dispatcher, benchmarks, shipping, telemetry refresh, dashboards, external interop; 09 Part C → C.21 Discipline-CHR |

#### A4. Architecture and structure

| What you need to do | Start here |
|---|---|
| **Describe architecture or structural views** — characterize structure, unfold constraint-governed structure, produce adequate architectural descriptions and view types, triage cross-scope architectural residuals | 07 A.V → A.22 STRUCT-CAL, A.22.CGUS; 09 Part C → C.30, C.30.AD, C.30.ASV, C.30.LCA, C.30.ILC, C.30.TFS-REL |
| **Connect transformation flows** without collapsing independent structures into one flow or project | 11 Part E → E.18.NET Network of Transformation-Flow Structures |
| **Synthesize architecture** candidates or reconcile several non-isomorphic structures of one practice, then assess modularity/reuse or publish ADR-style projections | 09 Part C → C.31 Modularity, C.32 Architecture Candidate Synthesis, C.32.MWA Practice Architecture, C.32.MWA.PP performance/provision arrangements, C.32.PAD, C.32.ADR, C.32.ADA |
| **Assess structural information** — compare what a reader can recover from an explanation under stated conditions, or check architecture capture, source return, equivalence, morphisms, or discovery adequacy | 09 Part C → C.2.8 Extractable Structural Information, C.33, C.34, C.35 |

#### A5. Express, publish, and work with sources

| What you need to do | Start here |
|---|---|
| **Enter and apply** FPF: choose a starting point or practical entry, find results across a DPF suite, or apply one pattern to a first useful result | 03 FPF Readme → Start Here, Practical Entries; 11 Part E → E.11.DSG Architectural Reference, E.11.PUA Pattern Use |
| **Sharpen expression** — rewrite text plainly without bureaucratese or needless hedging, shorten an account without dropping what matters or strengthening its claims, repair vague wording, recover exact method/work relations and model/explanation uses, clarify what “learning,” “development,” “evolution,” “interest,” or “curiosity” means in the current claim, surface ambiguity, or restore precision of epistemic / measurement / architecture terms | 12 Part F → F.19 plain technical rewriting; 06 A.IV.A → A.6.3.CSC controlled semantic coarsening, A.6.P.WMR Exact Relation Recovery, A.6.H Wholeness Unpacking; 11 Part E → E.10 model/explanation use, E.10.LRN, E.10.DEV, E.10.INT interest/curiosity, E.10.ARCH, E.17.EFP; 09 Part C → C.2.P, C.16.P, C.30.P |
| **Select and combine representations** for one exact action or decision without treating them as interchangeable | 09 Part C → C.37 Use-Bounded Representation Selection and Co-Use, C.37.MP method representation profiles, C.37.CF content/form comparison |
| **Find, read, and check sources** — choose what is worth reading for the current question, recover what an author means by familiar words before reinterpreting them, and check that each cited source supports its claim | 12 Part F → F.1 source selection, F.0.1 source-local meaning recovery; 07 A.V → A.10 Evidence Graph; Map B → RMP research synthesis, KCAE corpus access |
| **Unify vocabulary or synthesize source ontologies** across teams or domains without flattening source-local claims | 12 Part F → F.0.2 Semantic Synthesis, F.0.2.MA method contribution allocation, F.0.2.RC constructive coverage, concept sets, bridges, UTS, lexical continuity |
| **Transform, document, publish, and reuse epistemes, views, or frameworks** while preserving subjects and product-specific bodies | 06 A.IV.A → A.6.2-A.6.4 episteme morphing/viewing/retargeting (separate exact arrow, bounded-use assertion, and current-case judgment), A.6.3.NAR narrative rendering, A.6.3.RT.OE operative expression; 11 Part E → E.4.CM Connected Methods, E.8.ML connected-method pattern languages, E.4.PFIP Publication Integration, E.11.PFP Publication Form Profile, E.17 Multi-View Publication Kit |
| **Trace provenance and revalidate affected uses** when a relied-on source changes, or detect refresh debt | 07 A.V → A.10 Evidence Graph, A.10.1 Revalidate Affected Uses; 13 Part G → G.6 Provenance Ledger, G.11 Telemetry-Driven Refresh & Decay |

For complex problems, follow paths across multiple rows and groups — the router shows where to start, not where to stop.

### Map B — Domain frameworks (field question → DPF)

Open the framework with `find_pattern.py <DocID>` or its `_index.md`. Each Suite's `_index.md` also has a
"Choose an entry" table that maps a field question to the exact framework or pattern.

| Field | Frameworks (DocID — what it works on) | Entry |
|---|---|---|
| **Management** | STR — direction, investment, business models, the strategizing mantra STR.18 · GOALS — goals, achievement evidence, OKR/CFR, assigning work to AI agents (GOALS.7) · OPS — operations, service delivery, queues, capacity · ADM — requests, permissions, obligations, records · CGOV — corporate governance · MA — management accounting, costs, forecasts · FIN — corporate finance · MKT — marketing, offers, acquisition, distribution · CUST — client variation and repeatable offerings · EAM — engineering asset renewal and replacement · LDR — leadership, joint direction · CB — communities and participation · OCE — organizational change: roles, authority, capabilities · HRM — workforce, selection, reward, voice | `dpfs/management-dpf-suite/_index.md` |
| **Engineering** | SYSE — systems engineering: system and use concepts, architecture, build/buy/reuse (SYSE.24), integration, AI-agent procedures · KCAE — finding, reading and using documentary knowledge, search that finds nothing · SIE — semantic integration across separately governed meanings · CAD — control architecture: observations, memory, planning and feedback · MNT — maintenance and restoration after failure | `dpfs/engineering-dpf-suite/_index.md` |
| **Foundational thinking** | MATH — mathematical objects, proofs · MMP — mathematical modeling of a subject question · PHY — physical accounts and idealizations · CMP — algorithms under correctness and resource conditions · NOT — notation: tables, diagrams, formulas people can read, trace and change | `dpfs/foundational-thinking-dpf-suite/_index.md` |
| **Human capability** | HCD — human capability development: what to teach for later work, programmes, feedback, assessment, transfer · SOM — somatic movement, effort and coordination | `dpfs/human-capability-engineering-dpf-suite/_index.md` |
| **Decisions and research** | PSDA — decision design: reformulate the problem, construct alternatives, compare consequences and uncertainty · RMP — research method: frame and design research, criticize evidence, synthesize studies (RMP.7) | `dpfs/psda/_index.md`, `dpfs/rmp/_index.md` |
| **Explanation and narrative** | EXD — explanation design: what the recipient needs explained, examples, repair in dialogue · NSTD — followable narratives and working accounts that keep relations, uncertainty and source returns | `dpfs/exd/_index.md`, `dpfs/nstd/_index.md` |
| **Economics and finance modeling** | ECO — exchange, commitments, incentives, shared resources, coordination · FDM — financial positions, rights, obligations, payment flows | `dpfs/eco/_index.md`, `dpfs/fdm/_index.md` |
| **Practice change and spread** | IS — implementation facilitation: put an evidence-informed practice to use locally · DTM — how practices persist and spread, and how protective action changes outcomes | `dpfs/is/_index.md`, `dpfs/dtm/_index.md` |
| **Rhythm, music and dance** | RHY — embodied rhythmics · MDPE — music and dance practice engineering | `dpfs/rhy/_index.md`, `dpfs/mdpe/_index.md` |

The Library's own map of how these fields connect: `dpfs/_index.md` (catalogue) and
`library/reference/_index.md` (Library Architectural Reference).

### Map C — Common troubles (what went wrong → pattern)

Frequent situations in work with an agent, phrased the way people notice them. A DocID without a number
(EXD, KCAE) means the framework: open its `_index.md` and take the practical entry that fits.

| What went wrong | Pattern |
|---|---|
| **The answer itself** | |
| Bureaucratic, mumbling text with needless caveats | F.19 |
| Asked for expertise, the agent repeats "not proven, not verified" instead of giving a judgment from the available evidence | C.11.DUA |
| After a long dig into details, the original question is still unanswered | C.39.QR |
| "Make it three times shorter" drops what matters or turns "sometimes helps" into "always works" | A.6.3.CSC |
| A written plan passed off as done work, a description as a running system, a tool as a skill | A.7 |
| **Working with an agent over time** | |
| Hand over a job without nudging after every step: the result, means, authority and a clear "done" | GOALS.7 |
| Continue after a break or a handoff from the right place, with what is done and what remains | A.15.10 |
| After "no, I meant something else", redo the reasoning and conclusions that depended on it | B.5.RR |
| A discussion that goes nowhere: work through objections, combine useful ideas, reach an answer | B.5.SD |
| **Explaining and writing** | |
| Explain exactly where the reader stopped understanding, with an example that shows how it works | EXD |
| Turn scattered thoughts into a text people can follow that still sounds like its author | NSTD |
| A twenty-section review that never shows how the whole subject fits together and why | C.39.WA |
| A table, diagram or formula nobody can search, trace or change | NOT |
| **Sources and evidence** | |
| Recover what an author means by familiar words before inventing a meaning | F.0.1 |
| "Author A thinks…, author B…" — compare their ideas and show what follows from them together | F.0.2 |
| Choose what is worth reading for the question instead of fifty random links | F.1 |
| "Nothing found" — reformulate queries, read the sources themselves, state what they give the answer | KCAE |
| Trace each important claim to a source that actually supports it | A.10 |
| A pile of studies: where they agree, why they differ, how many independent results versus retellings | RMP.7 |
| **Explanations and options** | |
| The agent falls for the first plausible explanation | B.5.2 |
| "It is all because of X" → how X produces the result, rival causes, observations that tell them apart | C.28.CM |
| Five "different" options that are one idea under five names | C.40 |
| "We have only two options and both are bad" — restate the problem, find other moves, compare consequences | PSDA |
| **Systems, strategy and ways of working** | |
| "Improve collaboration" or "adopt AI" without a way to get the result: who does what, with what, how actions connect | C.39 |
| A project whose answers to "for whom and why", "how it works", "what it is made of" and "who builds it" do not line up | A.1.STM |
| Only one system design on the table: alternative structures, what each part does, and what each sacrifices | C.32 |
| Buy, build or "give it to AI": the same result compared by implementation, upkeep and later exit | C.38 |
| A fashionable practice versus how you already work: the real gain, switching and running costs | C.11.CRC |
| "Collect metrics and make a plan" → who chooses which action from which observations, and when to change the decision | C.43 |
| Strategy versus reality: the wanted result, the way to it, and enough people and money for every promise | STR.18 |
| **Improving work** | |
| What to improve next: where effort is lost or a useful result is missed, and which change pays off | C.39.WI |
| Remove make-work while keeping the needed result — including "time saved" by an agent that costs an hour to fix | C.42 |
| Reviews that actually improve the result: check that edits help, keep what worked, stop endless polishing | E.23 |
| Training after which people can do the new work, checked in the work rather than in a retelling | HCD |

### Step 1 — Resolve the starting point

Resolve every ID from a map with `find_pattern.py`. For a section folder or a framework, open its
`_index.md` first: Core folders list their files with line counts and descriptions; a DPF `_index.md`
holds the framework's practical entries (Situation → Start with → Stop or return), its Table of Contents
with keywords and dependencies, and its file list.

### Step 2 — Read the narrowest part of the pattern

1. Read only the file you need. Do NOT load entire sections or whole frameworks.
2. Pattern files share one layout. Read `:1 Problem frame` (does it fit the case?) and `:4 Solution`
   first; some patterns open with `:0 Use this when`. Use `:7 Conformance Checklist` to check your own
   result and `:8 Anti-patterns` to spot a known failure. `:12 Relations` names neighbouring patterns.
   `find_pattern.py` prints the line of each part, so a long file can be read by line range.
3. Links inside the files point to local files. Follow one only when the current result needs what it
   supplies; a citation can be enough as it is. `library/USING-FPF.md` is the upstream rule set for
   resolving references, editions and citations.

### Step 3 — Apply in plain language

Use plain language for the user. Introduce FPF-internal names (U.Holon, Gamma, F-G-R)
only when they add precision the user needs. Stop at the first useful result — a practical entry's
"Stop or return" line says when (E.11.PUA). Cite the full ID (for example `GOALS.7:4`) when the user
may want to read the source. Your own answer is subject to the first group of Map C: say plainly what
you conclude (F.19, C.11.DUA) and bring it back to the original question (C.39.QR).

### Step 4 — Compose findings across sections and frameworks

When a problem draws from multiple sections:

1. State each pattern's contribution in one line (e.g., "Bounded Contexts gives us the parts; Trust Calculus scores our confidence in each").
2. If patterns from different sections appear to conflict, check for category errors via A.7 Strict Distinction — the conflict is usually a level confusion (role vs. function, method vs. work), not a real contradiction.
3. Synthesize in natural order: decomposition first (what are the parts?), then evaluation (how confident are we?), then resolution (what do we do about gaps?).
4. A DPF method and the Core patterns it cites are one line of reasoning: the DPF gives the field's conditions and cases, Core the general method. Do not restate the Core pattern when the DPF already applies it.
5. Do not just list FPF patterns — weave them into a coherent answer to the user's actual question.

## Starter prompt (example — adapt to the user's actual role and need)

> You have the FPF specification loaded.
> Help me structure my project / problem / programme.
> Use plain language for an engineer-manager.
> Propose: (1) bounded contexts / specialisations, (2) decision criteria, (3) key alternatives,
> (4) hand-offs, and (5) missing evidence or tests before commitment.
> Introduce internal FPF names only when they add precision.

## Library INDEX

Structural reference. Each entry is a folder — read its `_index.md` first, then pick the file.

### FPF Core (`sections/`)

Counts follow upstream H2 headings; the Architectural Reference includes its content-free `FPF.Reference:End` boundary marker.

| # | Section | Sub | When to use |
|---|---------|:---:|-------------|
| 01 | [Title page](sections/01-first-principles-framework---core-conceptual-specification/_index.md) | 0 | **Identify**: title, authorship, version date, top-level identity. |
| 02 | [Table of Contents](sections/02-table-of-contents/_index.md) | 0 | **Navigate**: locate a pattern, keyword, query cue, dependency, or neighboring section. |
| 03 | [FPF Readme](sections/03-first-principles-framework-readme/_index.md) | 12 | **Enter, onboard, and recover**: choose a starting point or practical entry, understand what each part contributes, connect actions to encompassing work, connect transformation flows, recover a lost path from outside use to recursive builders, or locate licensing and reuse terms. |
| 04 | [Architectural Reference](sections/04-first-principles-framework-architectural-reference/_index.md) | 22 | **Orient**: read philosophy, Architectural Rationale, shared source synthesis, profile choices, whole-combination conditions, uncertainty posture, and purpose/non-goals. |
| 05 | [Part A — Kernel](sections/05-part-a---kernel-architecture-cluster/_index.md) | 38 | **Decompose, identify, discover, trace, assign, recover, and authorize**: holons, bounded contexts, acting/changed-system recognition, consequence-bearing System discovery, outside-use dependency tracing, roles, permissions, candidate-Method recovery from Work evidence and documentary sources, qualification, trials, coherence, transfer, variants, introduction, method descriptions, transformers, method/work separation, object reidentification, constrained configurations, state-change rules, predictive information. |
| 06 | [A.IV.A — Signatures](sections/06-cluster-a-iv-a---signature-stack-boundary-discipline/_index.md) | 29 | **Set boundaries, recover references, derive relations, transform epistemes, and render**: recover agent-relative expressions after transfer; distinguish relations from occurrences; recover exact method/work and under-specified service/access relations; derive needed relation claims; keep source, receiving episteme, arrow, use claim, work, and publication distinct; shorten an account without losing what matters; classify statements, construct operative expressions, or render structure faithfully. |
| 07 | [A.V — Principles](sections/07-cluster-a-v---constitutional-principles-of-the-kernel/_index.md) | 50 | **Prevent confusion, remove ceremony, recover direct subjects, and steer, resume, or recovery-test Work**: category errors, ontology premises, decision-relevant operational parsimony, project/process/case language, situation-responsive next-action choice, interrupted-work resumption, making applicable methods noticeable, performer/support configuration and recovery probes, production-work identity, completion criteria and separate closure authority, measuring, comparing, evidence graphs and changed-source revalidation, methodological support, bounded specialist results, mechanism suites, transformation-step constraint validity, independent-check gate decisions, constraint-governed unfolding. |
| 08 | [Part B — Reasoning](sections/08-part-b---trans-disciplinary-reasoning-cluster/_index.md) | 43 | **Compose, evaluate, and coordinate development**: structural views (STRUCT-CAL), aggregation (Gamma), composite Method qualification, substantive discussion, constituent actions and encompassing Work, use-preserving Method replacement, trust scores, emergence, inquiry from ordinary work, working-note development, development states, domain-concept bridging, reasoning cycles, first models, concept recognition, theory use/comparison, argument and construction recovery, reasoning revision, new questions, physical/mathematical/computational connections. |
| 09 | [Part C — Extensions](sections/09-part-c---kernel-extension-specifications/_index.md) | 130 | **Score, compare, search, architect, and control**: epistemic quality, reader-extractable structural information, typed reasoning, measurement, configuration-relative contribution comparisons, reconsideration after a decision’s relied-on basis changes, comparable result routes, representation selection and co-use, decision-useful advice and evidence demands, decisions, bounded apparatus use, temporal/causal/math lenses, causal-model construction/challenge, observation-choice-action control loops, architecture synthesis across non-isomorphic practice structures, structural adequacy, cultural evolution, measurement construction/repair, result transfer, computational formulation/realization, symmetry comparison and boundary balances, reusable operations, branching search, recorded-history replay without future-outcome leakage, reproducible construct use, return to the original question, whole-subject accounts, and avoidable-work reduction that preserves the needed result; method worth, representation profiles, content/form changes, development focus, worthwhile method improvements, requirements, repertoire, opportunity inquiry and joint reachability, checklist construction and use. |
| 10 | [Part D — Ethics](sections/10-part-d---multi-scale-ethics-and-conflict-optimization/_index.md) | 5 | **Resolve conflicts**: ethical trade-offs, bias auditing, safety overrides, conflict optimization. |
| 11 | [Part E — Constitution and Authoring](sections/11-part-e---the-fpf-constitution-and-authoring-guides/_index.md) | 69 | **Enter, apply, clarify, probe, develop, govern, reuse, and publish**: practical entry and pattern use, DPF-suite navigation, learning/development/evolution and interest/curiosity claim recovery, connected methods, pattern languages and framework publication forms, quality-improvement loops with no-change comparisons and affected-evidence rebuilding, capability access/expression probing and development for named Work, edition continuity, multi-view publication, transformation-flow networks, pattern quality, ontic/U-kind governance. |
| 12 | [Part F — Unification](sections/12-part-f---the-unification-suite-concept-sets-sensecells-and-system-role/_index.md) | 24 | **Synthesize, align, and rewrite**: source-local meaning recovery, source selection for a current question, bounded semantic synthesis across source ontologies, method contribution allocation and constructive coverage, concept sets, sense cells, bridges with separate bounded-use claims and reliance basis, system-role descriptions, UTS, lexical continuity, plain technical rewriting. |
| 13 | [Part G — SoTA Kit](sections/13-part-g---discipline-sota-patterns-kit/_index.md) | 15 | **Harvest and refresh disciplines**: SoTA Packs, CG-Frames, dispatchers, provenance ledgers, benchmark harnesses, shipping, telemetry refresh, dashboards, external interop. |
| 14 | [Part H — Reserved](sections/14-part-h---reserved/_index.md) | 0 | **Reserve**: preserve the upstream Part H position for future specification content. |

### Domain frameworks and Library documents

| Path | When to use |
|---|---|
| [PATTERN-INDEX.md](PATTERN-INDEX.md) | **Resolve**: every DocID and PatternID of the Library with its local file (generated; read through `scripts/find_pattern.py`). |
| [dpfs/_index.md](dpfs/_index.md) | **Choose a field**: the DPF catalogue — Suites, standalone frameworks and what each works on. |
| `dpfs/<suite>/_index.md` | **Enter a Suite**: "Choose an entry" maps a field question to a framework or pattern; the Suite's Architectural Reference is in `suite-reference/`. |
| `dpfs/[<suite>/]<docid>/_index.md` | **Enter a framework**: practical entries, Table of Contents with keywords and dependencies, file list. |
| [library/USING-FPF.md](library/USING-FPF.md) | **Read and cite correctly**: how to resolve references, distinguish a source from material to apply, and name editions. |
| [library/reference/_index.md](library/reference/_index.md) | **Orient in the Library**: why Core, Suites and standalone DPFs are arranged this way; DocID catalogue (Library.Reference:11.1). |
| [library/_index.md](library/_index.md) | **Introduce**: the Library's own readme and first-use route. |
