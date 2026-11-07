# Map A — Core router (thinking need → Core pattern)

Part of the `fpf-problem-solving` skill: `SKILL.md` Step 0 sends a general thinking need here. Paths and
commands are relative to the skill directory. After choosing a pattern, continue with `SKILL.md`
Steps 1–4 (resolve, read the narrowest part, apply in plain language, compose).

Find the group first, then the row. Each row names the Core section folder and the patterns to start
with; the first pattern of a cell is the usual start. Resolve them with `python3 scripts/find_pattern.py
<ID> [<ID> …]` (one card per ID: when to use it and when not to). A card lists the pattern's family with
titles (`find_pattern.py C.40`), so a cell may name a family instead of every member.

## A1. Model the subject — what it is, its parts, roles, and what words refer to

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

## A2. Reason, evaluate, and decide

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

## A3. Find ways to obtain results and improve work

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

## A4. Architecture and structure

| What you need to do | Start here |
|---|---|
| **Describe architecture or structural views** — characterize structure, unfold constraint-governed structure, produce adequate architectural descriptions and view types, triage cross-scope architectural residuals | 07 A.V → A.22 STRUCT-CAL, A.22.CGUS; 09 Part C → C.30, C.30.AD, C.30.ASV, C.30.LCA, C.30.ILC, C.30.TFS-REL |
| **Connect transformation flows** without collapsing independent structures into one flow or project | 11 Part E → E.18.NET Network of Transformation-Flow Structures |
| **Synthesize architecture** candidates or reconcile several non-isomorphic structures of one practice, then assess modularity/reuse or publish ADR-style projections | 09 Part C → C.31 Modularity, C.32 Architecture Candidate Synthesis, C.32.MWA Practice Architecture, C.32.MWA.PP performance/provision arrangements, C.32.PAD, C.32.ADR, C.32.ADA |
| **Assess structural information** — compare what a reader can recover from an explanation under stated conditions, or check architecture capture, source return, equivalence, morphisms, or discovery adequacy | 09 Part C → C.2.8 Extractable Structural Information, C.33, C.34, C.35 |

## A5. Express, publish, and work with sources

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
