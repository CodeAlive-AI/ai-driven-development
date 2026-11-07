---
name: fpf-problem-solving
description: "Use the First Principles Framework (FPF) Library, Core plus 36 domain frameworks (DPFs) stored locally, to think more rigorously than the situation's default: decompose problems, architect systems, generate real alternatives, decide under uncertainty, reconsider decisions, establish causality, design control loops, recover and improve methods, steer, hand off or resume agent work, check sources and evidence, explain, rewrite text plainly, define quality, and apply field methods for strategy, goals/OKR, operations, management, research, decision design, systems engineering, knowledge access, mathematics, notation, narrative and human capability. Triggers: FPF, DPF, fpf.tools, Levenchuk, a pattern ID such as F.19, C.11.DUA, A.15.10, GOALS.7 or STR.18, bounded contexts, assurance, SoTA packs, operational parsimony, causal/temporal reasoning, modularity, lexical discipline. Not for simple task planning, general philosophy, or Agile unrelated to FPF."
---

# First Principles Framework (FPF) Library

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

## When to use

Use FPF whenever you need to think more rigorously than the situation's default:

- Apply a named FPF or DPF pattern (F.19, C.11.DUA, GOALS.7) to the current text, answer or task
- Repair a recurring trouble in work with an agent: hedging instead of judgment, a lost original question, restarting after a handoff, look-alike alternatives, a plan passed off as done work
- Answer a field question with that field's framework: strategy, goals and OKR, operations, marketing, finance, research, decisions, systems engineering, explanation, narrative, teaching people
- Decompose a messy, cross-domain problem; identify the system that acts or changes; keep a plan, a description and a running system apart
- Decide under uncertainty: real alternatives, quality defined before comparing, causal claims checked, a decision reconsidered when its basis changes
- Find, qualify, steer or improve a way of working: methods, the next action, resuming work, removing ceremony, checklists, capability
- Architect systems and compare structures; rewrite, shorten, explain or publish an account without losing what matters
- Check sources and evidence: what to read, what an author means, whether a source supports the claim

Not for simple task planning, general philosophy, or Agile unrelated to FPF.

## How to navigate

All paths are relative to this skill's directory. One script resolves every reference and says where to start:

```bash
python3 scripts/find_pattern.py C.11.DUA            # a pattern: use when / not when, family, section map with lines
python3 scripts/find_pattern.py C.38 C.40 SYSE.24   # several: a short card each, to choose the one that fits
python3 scripts/find_pattern.py HCD.12:4.1          # a section reference: the line inside the file
python3 scripts/find_pattern.py GOALS               # a framework: its entries (situation → start with) and patterns
python3 scripts/find_pattern.py FPF                 # the Core: its practical entries and parts
python3 scripts/find_pattern.py --search okr        # English words: ranked entries, titles and keywords
```

Without Python: `grep -F "| C.11.DUA |" PATTERN-INDEX.md` gives the file in the third column.

### Step 0 — Choose the map by how FPF came up

| What you have | Go to |
|---|---|
| A **pattern ID, section reference or DocID** — "apply F.19", "use C.11.DUA", "GOALS.7", "HCD.12:4.1", "EXD" | Resolve it with `find_pattern.py` and read that file (Step 2) once the text, answer or task to apply it to is at hand. Skip the maps. |
| A **familiar trouble** in work with an agent, a text, sources, an explanation, options or a plan | **Map C — Common troubles** |
| A **question inside a field** — strategy, goals/OKR, operations, marketing, finance, research, decisions, systems engineering, knowledge access, mathematics, explanation, teaching people | **Map B — Domain frameworks** |
| A **general thinking need** — decompose, identify, decide, compare, establish cause, architect, revise, publish | **Map A — Core router** |
| Nothing above fits, or you are unsure | `find_pattern.py --search <one to three English words>` (translate a non-English request; partial matches are weak evidence), or `find_pattern.py FPF` for the Core's practical entries |

Before reading a pattern:

- **Have the object in hand.** If the request points at something you do not have ("the advice you just
  gave", "my report"), find it in the conversation or ask for it.
- **Choose by the cards.** When two rows or patterns could fit, pass them all to `find_pattern.py`: each
  card says when to use the pattern and when not to. If none fits, ask the user one clarifying question
  rather than forcing a pattern.
- **Use both layers for a field question.** The DPF supplies the field's method and conditions; the Core
  patterns it cites supply the general reasoning. Follow a Core ID from a DPF file the same way.

### Map A — Core router (thinking need → Core pattern)

Find the group first, then the row. Each row names the section folder and the patterns to start with; the
first pattern of a cell is the usual start. A pattern's card lists its family with titles
(`find_pattern.py C.40`), so a cell may name a family instead of every member.

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
| **Decide, reconsider, appraise advice, or compare contributions** under uncertainty — structure options, weigh evidence, commit with auditable rationale, compare a change with the current configuration, reconsider when a decision’s basis changes | 09 Part C → C.11.CRC Configuration-Relative Contribution Comparison, C.11.MV method-option worth, C.11 Decsn-CAL, C.11.DBR Decision-Basis Reconsideration, C.11.DUA Decision-Useful Advice and Evidence Demands |
| **Reason about time and change** — distinguish state readings, trends, currentness, and intervention-sensitive change, or recover an actual temporal structure before testing coordination | 09 Part C → C.27 Temporal Claim Adequacy, C.27.TA Temporal Aspect; 03 FPF Readme → ACTUAL-TEMPORAL-STRUCTURE |
| **Establish causality** — climb the causality ladder, construct or challenge a causal model, identify causal structure, and check realizability | 09 Part C → C.28 CausalUse-CAL, C.28.CM causal-model construction/challenge, C.28.MR mechanism replacement |
| **Design a control loop** — connect observations, choices, and actions without losing their feedback or decision relations | 09 Part C → C.43 Connect Observation, Choice and Action in Control |
| **Connect mathematical and computational reasoning** — assess model fit, transfer results, realize computations, repair physical connections, compare symmetry transformations, or construct boundary balances | 09 Part C → C.29 Mathematical Lens Use, C.29.1 result transfer and symmetry, C.29.2 computational formulation, C.29.3 computational realization, C.29.BB boundary balance; 08 Part B → B.5.MPC physical/mathematical/computational connection, B.5.MPC.R repair |
| **Resolve conflicts** across stakeholders or values | 10 Part D → Ethics, bias audit, conflict optimization |
| **Define quality** attributes ("-ilities") as structured bundles | 09 Part C → C.25 Q-Bundle; 07 A.V → A.17-A.19 Characteristics |

#### A3. Find ways to obtain results and improve work

| What you need to do | Start here |
|---|---|
| **Recover, qualify, and develop methods** — from performances or documents through trials, coherence and transfer to introduction into practice; find worthwhile improvements; return a partial result to its original question and the whole subject | 05 Part A → the A.3.1 family: A.3.1.MR recovery from Work evidence, A.3.1.DR from documentary sources, A.3.1.QM qualification, A.3.1.WT work trials, A.3.1.CC coherence, A.3.1.FT fit and transfer, A.3.1.MV variants, A.3.1.MI introduction into practice; A.3.2.DE method descriptions; 09 Part C → C.39.QR original-question return, C.39.WA whole-subject account, C.39.MF development focus, C.39.WI worthwhile improvements, C.39.RQ situated requirements, C.39.RP repertoire, C.39.MC changed conditions |
| **Steer, resume, and recovery-test Work** — choose the next action from current facts, resume after interruption, make applicable methods noticeable, recover the actual performer/support configuration and probe interruption, handoff, delay or reconfiguration | 07 A.V → A.15.7 Situation-Responsive Work Steering, A.15.8 Work-Performance Configuration and Recovery Testing, A.15.8.MS methodological support, A.15.10 Resume Interrupted Work, A.15.11 Make Applicable Methods Noticeable |
| **Screen mandatory work** for operational relevance before requiring a step, check, record, wait, cue, or tool use | 07 A.V → A.11.OP Decision-Relevant Least Action and Operational Parsimony; 09 Part C → C.42 Reduce Avoidable Work While Preserving the Needed Result |
| **Request or reuse specialist results** for one receiving decision while preserving the other practice’s authority | 07 A.V → A.15.9 Bounded Result from Another Practice |
| **Generate alternatives** / construct comparable ways to obtain one result, explore solution space, keep the original question and whole subject in view, and keep apparatus use bounded | 09 Part C → C.38 Comparable Ways to Obtain One Result, C.39 result construction, C.39.QR original-question return, C.39.WA whole-subject account, C.39.RO reusable operations, C.40 branching search and §4.8.1 recorded-history replay, with its family (opportunities, worthwhile problems, support configurations, joint development, stepping stones — `find_pattern.py C.40`); C.17 Creativity-CHR, C.18 Open-Ended Search, C.19 Explore-Exploit, C.19.2 Use-Bounded Apparatus Application |
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
| **Enter and apply** FPF: choose a starting point or practical entry, find results across a DPF suite, or apply one pattern to a first useful result | 03 FPF Readme → Start Here, Practical Entries (`find_pattern.py FPF` lists them); 11 Part E → E.11.DSG Architectural Reference, E.11.PUA Pattern Use |
| **Sharpen expression** — rewrite plainly without bureaucratese or needless hedging, shorten without dropping what matters or strengthening claims, repair vague wording, recover exact relations and model/explanation uses, clarify what “learning”, “development”, “evolution”, “interest” or “curiosity” claims, restore precision of epistemic, measurement or architecture terms | 12 Part F → F.19 plain technical rewriting; 06 A.IV.A → A.6.3.CSC controlled semantic coarsening, A.6.P.WMR Exact Relation Recovery, A.6.H Wholeness Unpacking; 11 Part E → E.10 model/explanation use, E.10.LRN, E.10.DEV, E.10.INT interest/curiosity, E.10.ARCH, E.17.EFP; 09 Part C → C.2.P, C.16.P, C.30.P |
| **Select and combine representations** for one exact action or decision without treating them as interchangeable | 09 Part C → C.37 Use-Bounded Representation Selection and Co-Use, C.37.MP method representation profiles, C.37.CF content/form comparison |
| **Find, read, and check sources** — choose what is worth reading for the current question, recover what an author means by familiar words before reinterpreting them, and check that each cited source supports its claim | 12 Part F → F.1 source selection, F.0.1 source-local meaning recovery; 07 A.V → A.10 Evidence Graph; Map B → RMP research synthesis, KCAE corpus access |
| **Unify vocabulary or synthesize source ontologies** across teams or domains without flattening source-local claims | 12 Part F → F.0.2 Semantic Synthesis, F.0.2.MA method contribution allocation, F.0.2.RC constructive coverage, concept sets, bridges, UTS, lexical continuity |
| **Transform, document, publish, and reuse epistemes, views, or frameworks** while preserving subjects and product-specific bodies | 06 A.IV.A → A.6.2-A.6.4 episteme morphing/viewing/retargeting, A.6.3.NAR narrative rendering, A.6.3.RT.OE operative expression; 11 Part E → E.4.CM Connected Methods, E.8.ML connected-method pattern languages, E.4.PFIP Publication Integration, E.11.PFP Publication Form Profile, E.17 Multi-View Publication Kit |
| **Trace provenance and revalidate affected uses** when a relied-on source changes, or detect refresh debt | 07 A.V → A.10 Evidence Graph, A.10.1 Revalidate Affected Uses; 13 Part G → G.6 Provenance Ledger, G.11 Telemetry-Driven Refresh & Decay |

For complex problems, follow paths across multiple rows and groups — the router shows where to start, not where to stop.

### Map B — Domain frameworks (field question → DPF)

`find_pattern.py <DocID>` prints the framework's entries (situation → start with) and all its patterns —
usually the fastest second step. A Suite's "Choose an entry" table maps a field question to the framework
or pattern (`find_pattern.py Management`, `Engineering`, `Foundational`, `HCE`).

| Field | Frameworks (DocID — what it works on) | Entry |
|---|---|---|
| **Management** | STR — direction, investment, business models, the strategizing mantra STR.18 · GOALS — goals and OKR/CFR: achievement evidence (GOALS.2), feasibility across shared people and capacity (GOALS.3), revising or ending a goal (GOALS.4), assigning work to AI agents (GOALS.7) · OPS — operations, service delivery, queues, capacity · ADM — requests, permissions, obligations, records · CGOV — corporate governance · MA — management accounting, costs, forecasts · FIN — corporate finance · MKT — markets and customers, offers, acquisition, distribution, market entry · CUST — client variation and repeatable offerings · EAM — engineering asset renewal and replacement · LDR — leadership, joint direction · CB — communities and participation · OCE — organizational change: roles, authority, capabilities · HRM — workforce, selection, reward, voice | `dpfs/management-dpf-suite/_index.md` |
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

Frequent situations in work with an agent, phrased the way people notice them. The first ID is where to
start; an ID after · covers the neighbouring case named before it. When a row is close but not exact,
compare the candidates' cards in one call: `find_pattern.py C.42 A.11.OP`.

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
| A discussion that goes nowhere: work through objections, combine useful ideas, reach an answer | B.5.SD when no shared answer has been built · CB.13 when no one has the mandate to decide (unsure which: ask) |
| **Explaining and writing** | |
| Explain exactly where the reader stopped understanding, with an example that shows how it works | EXD.4 repair in dialogue · EXD.2 the example · EXD.1 when it is unclear what needs explaining |
| Turn scattered thoughts into a text people can follow that still sounds like its author | NSTD.1 purpose and what must survive · NSTD.3 missing connections · B.5.WN while they are still working notes |
| A twenty-section review that never shows how the whole subject fits together and why | C.39.WA |
| A table, diagram or formula nobody can search, trace or change | NOT.7 · NOT.6 when a formula, table and diagram must change together |
| **Sources and evidence** | |
| Recover what an author means by familiar words before inventing a meaning | F.0.1 |
| "Author A thinks…, author B…" — compare their ideas and show what follows from them together | F.0.2 |
| Choose what is worth reading for the question instead of fifty random links | F.1 |
| "Nothing found" — reformulate queries, read the sources themselves, state what they give the answer | KCAE.SEARCH · KCAE.ASSESS for what a found source supports |
| Trace each important claim to a source that actually supports it | A.10 |
| A pile of studies: where they agree, why they differ, how many independent results versus retellings | RMP.7 |
| **Explanations and options** | |
| The agent falls for the first plausible explanation | B.5.2 |
| "It is all because of X" → how X produces the result, rival causes, observations that tell them apart | C.28.CM |
| Five "different" options that are one idea under five names | C.40 · ways to obtain one result → C.38 · structures of a system → C.32 |
| "We have only two options and both are bad" — restate the problem, find other moves, compare consequences | PSDA.1 → PSDA.5 → PSDA.8 |
| **Systems, strategy and ways of working** | |
| "Improve collaboration" or "adopt AI" without a way to get the result: who does what, with what, how actions connect | C.39 |
| A project whose answers to "for whom and why", "how it works", "what it is made of" and "who builds it" do not line up | A.1.STM |
| Only one system design on the table: alternative structures, what each part does, and what each sacrifices | C.32 (it starts from one described system, C.30) · from an outside need through structure to a decision → C.32.P2S |
| Buy, build or "give it to AI": the same result compared by implementation, upkeep and later exit | C.38 · inside an engineering project → SYSE.24 |
| A fashionable practice, a rewrite or a replacement versus how you already work: the real gain, switching and running costs | C.11.CRC |
| "Collect metrics and make a plan" → who chooses which action from which observations, and when to change the decision | C.43 |
| Strategy versus reality: the wanted result, the way to it, and enough people and money for every promise | STR.18 · field detail: MKT market, MA costs, FIN finance |
| **Improving work** | |
| What to improve next: where effort is lost or a useful result is missed, and which change pays off | C.39.WI |
| Remove make-work while keeping the needed result — including "time saved" by an agent that costs an hour to fix | C.42 · whether a mandatory step, check or record (proposed or already required) earns its place → A.11.OP |
| Reviews that actually improve the result: check that edits help, keep what worked, stop endless polishing | E.23 |
| Training after which people can do the new work, checked in the work rather than in a retelling | HCD.1 what later work needs · HCD.11 check in representative work · HCD.12 transfer |

### Step 1 — Resolve the starting point

Resolve every ID from a map with `find_pattern.py`. Its *use when* and *not when* lines tell you whether the
pattern fits before you open the file. For a framework, `find_pattern.py <DocID>` lists its entries
(Situation → Start with → Stop or return in its `_index.md`) and patterns; for a Core folder, its
`_index.md` lists the files with line counts and descriptions.

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

1. State each pattern's contribution in one line (e.g., "Bounded Contexts gives us the parts; Trust Calculus scores our confidence in each").
2. If patterns appear to conflict, check for category errors via A.7 Strict Distinction — the conflict is usually a level confusion (role vs. function, method vs. work), not a real contradiction.
3. Synthesize in natural order: decomposition first (what are the parts?), then evaluation (how confident are we?), then resolution (what do we do about gaps?).
4. A DPF method and the Core patterns it cites are one line of reasoning: the DPF gives the field's conditions and cases, Core the general method. Do not restate the Core pattern when the DPF already applies it.
5. Do not just list FPF patterns — weave them into a coherent answer to the user's actual question.

## Library layout

| Path | What it holds |
|---|---|
| [PATTERN-INDEX.md](PATTERN-INDEX.md) | Every DocID and PatternID with its local file (generated; read it through `scripts/find_pattern.py`) |
| `sections/<NN-part>/_index.md` | FPF Core: one folder per Part or cluster, one file per pattern; `_index.md` lists the files |
| [dpfs/_index.md](dpfs/_index.md) | The DPF catalogue: Suites, standalone frameworks and what each works on |
| `dpfs/<suite>/_index.md` | A Suite: its "Choose an entry" table; the Suite's Architectural Reference is in `suite-reference/` |
| `dpfs/[<suite>/]<docid>/_index.md` | A framework: practical entries, Table of Contents with keywords and dependencies, file list |
| [library/USING-FPF.md](library/USING-FPF.md) | How to resolve references, tell a source from material to apply, and name editions |
| [library/reference/_index.md](library/reference/_index.md) | Why Core, Suites and standalone DPFs are arranged this way; DocID catalogue (Library.Reference:11.1) |
| [library/_index.md](library/_index.md) | The Library's own readme and first-use route |

## Attribution and license

This skill adapts the *FPF Library* by Anatoly Levenchuk — *First Principles Framework (FPF)* Core, its
domain frameworks (DPFs) and Library documents — [ailev/FPF](https://github.com/ailev/FPF), upstream
commit `e317958532699b762dd9e7baf460f97bad7a4c9c`. The Library text in `sections/`, `dpfs/` and
`library/` is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Changes: the
publications were split into section files with generated navigation indexes, and their links were
rewritten to point at the local files; this `SKILL.md` adds an agent-oriented router and usage
instructions. Map C paraphrases Anatoly Levenchuk's cheatsheet of frequently used FPF patterns
(November 2026). See the [upstream licensing scope](https://github.com/ailev/FPF/blob/main/LICENSING.md).
Skill packaging and scripts are MIT licensed. This adaptation is not endorsed by the FPF author.
