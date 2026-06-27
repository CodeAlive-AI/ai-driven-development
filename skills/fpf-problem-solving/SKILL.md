---
name: fpf-problem-solving
description: "First Principles Framework (FPF) — thinking amplifier. Use when user wants to think through a complex problem, architect a system, evaluate alternatives, decompose complexity, classify problems, define quality attributes, plan rigorously, decide under uncertainty, establish causality, reason about time and trends, describe or synthesize architecture, check mathematical model fit, govern ontic/U-kind introduction, publish multi-view artifacts, refresh SoTA packs, trace provenance, or improve pattern quality. Also triggers on: FPF, bounded contexts, SoTA packs, assurance calculus, decision theory, causal reasoning, temporal reasoning, architecture description, modularity, structural adequacy, cultural evolution, quality gates, lexical discipline, FPF Parts A-G/I. Not for simple task planning, general philosophy, or Agile unrelated to FPF."
---

# First Principles Framework (FPF)

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
- Transfer an insight across domains without losing precision or introducing category errors
- Structure a proposal that must survive scrutiny from multiple expert perspectives
- Generate alternatives systematically instead of anchoring on the first idea
- Define what "better" means before comparing options
- Classify what kind of problem you're facing before searching for solutions
- Plan how an AI agent should select and sequence its tools under budget and trust constraints
- Make a decision under uncertainty — identify options, weigh evidence, and commit with an auditable rationale
- Establish whether X causes Y — or just correlates — and determine what intervention would work
- Publish a stable multi-view artifact without changing the source semantics
- Refresh a SoTA pack, benchmark, or evidence trail when evidence decays or telemetry changes
- Synthesize architecture candidates, compare structural options, or repair modularity/reuse claims
- Govern when a new ontic concept or U-kind should be introduced instead of just renamed

## How to navigate

The use cases above help decide WHETHER to invoke FPF. The router below decides WHERE to go once invoked.

### Step 1 — Match the thinking need to a starting point

| What you need to do | Start here |
|---|---|
| **Decompose** a complex whole into bounded parts | 05 Part A → A.1 Holons, A.1.1 Bounded Contexts, A.14 Mereology |
| **Assign** roles and responsibilities | 05 Part A → A.2 Roles, A.15 Role-Method-Work Alignment |
| **Set boundaries** on what statements mean | 06 Signature Stack → classify as definitions, gates, duties, or evidence |
| **Prevent category errors** (role vs. function, method vs. work) | 07 Constitutional Principles → A.7 Strict Distinction |
| **Evaluate confidence** in a claim or artifact — including formality, scope, and reliability of the underlying knowledge | 08 Part B → B.3 Trust & Assurance; 09 Part C → C.2 KD-CAL / F-G-R scoring, C.2.2 Reliability, C.2.3 Formality |
| **Compose** parts into wholes preserving properties | 08 Part B → B.1 Gamma algebra; 09 Part C → C.13 Compose-CAL, C.20 Discipline-CAL |
| **Reason through** a problem systematically | 08 Part B → B.5 Reasoning Cycle, B.5.2 Abductive Loop |
| **Generate alternatives** / explore solution space | 09 Part C → C.17 Creativity-CHR, C.18 Open-Ended Search, C.19 Explore-Exploit |
| **Measure and compare** options rigorously | 07 A.V → A.17-A.19 Characteristics, CSLC & SelectorMechanism; 09 Part C → C.16 MM-CHR; 13 Part G → G.9 Parity / Benchmark Harness |
| **Resolve conflicts** across stakeholders or values | 10 Part D → Ethics, bias audit, conflict optimization |
| **Unify vocabulary** across teams or domains | 12 Part F → concept sets, bridges, UTS, lexical continuity |
| **Document** for multiple audiences or stabilize a publication unit | 11 Part E → E.17 Multi-View Publication Kit, E.17.EFP Explanation Faithfulness, E.17.AUD PublicationUnit Stability |
| **Sharpen expression** — repair vague wording, surface ambiguity, restore precision of epistemic / measurement / architecture terms | 11 Part E → E.10.ARCH Wording-Use Ontological Precision Restoration, E.17.EFP Explanation Faithfulness; 09 Part C → C.2.P, C.16.P, C.30.P; 06 A.IV.A → A.6.H Wholeness Unpacking |
| **Decide** under uncertainty — structure options, weigh evidence, commit with auditable rationale | 09 Part C → C.11 Decsn-CAL |
| **Reason about time and change** — distinguish state readings, trends, currentness, and intervention-sensitive change | 09 Part C → C.27 Temporal Claim Adequacy, C.27.TA Temporal Aspect |
| **Establish causality** — climb the causality ladder, identify causal structure, check realizability | 09 Part C → C.28 CausalUse-CAL |
| **Check mathematical or modeling fit** — assess whether a formal lens / math model is adequate for the problem | 09 Part C → C.29 Mathematical Lens Use |
| **Describe architecture or structural views** — characterize structure, produce adequate architectural descriptions and view types, triage cross-scope architectural residuals | 09 Part C → C.30, C.30.AD, C.30.ASV, C.30.LCA, C.30.ILC, C.30.TFS-REL; 08 Part B → A.22 STRUCT-CAL |
| **Synthesize architecture** candidates or decisions — move from problem to structure, assess modularity/reuse, and publish ADR-style projections | 09 Part C → C.31 Modularity, C.32 Architecture Candidate Synthesis, C.32.P2S, C.32.PAD, C.32.ADR, C.32.ADA |
| **Assess structural information** — check architecture capture, source return, equivalence, morphisms, or discovery adequacy | 09 Part C → C.33, C.34, C.35 |
| **Model context-dependent or indeterminate states** — represent superposed, probe-coupled, or viability-bounded behaviour | 09 Part C → C.26 Quantum-Like Modeling Lens, C.26.1 Probe-Coupled Boundary, C.26.2 Enacted Distributed State, C.26.3 Viability-Envelope |
| **Survey a discipline** and build, ship, or refresh a reusable toolkit | 13 Part G → G.1-G.13 SoTA kit, CG-Frame, dispatcher, benchmarks, shipping, telemetry refresh, dashboards, external interop; 09 Part C → C.21 Discipline-CHR |
| **Classify** a problem type before solving | 09 Part C → C.22 Problem-CHR, C.3 Kind-CAL (typed reasoning) |
| **Define quality** attributes ("-ilities") as structured bundles | 09 Part C → C.25 Q-Bundle; 07 A.V → A.17-A.19 Characteristics |
| **Govern ontology** — decide whether a new ontic concept or U-kind is warranted | 11 Part E → E.24 Ontic Introduction Discipline, E.24.UK U-kind Governance |
| **Reason about cultural evolution** — describe cultural-evolution engineering or repair cultural-evolution wording | 09 Part C → C.36 Cultural Evolution, C.36.P Precision Restoration |
| **Orchestrate** agentic tool use under budgets and trust gates | 09 Part C → C.24 Agent-Tools-CAL |
| **Trace provenance** of a claim or detect refresh debt | 07 A.V → A.10 Evidence Graph; 13 Part G → G.6 Provenance Ledger, G.11 Telemetry-Driven Refresh & Decay |

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

| # | Section | Sub | When to use |
|---|---------|:---:|-------------|
| 01 | [Title page](sections/01-first-principles-framework---core-conceptual-specification/_index.md) | 0 | **Identify**: title, authorship, version date, top-level identity. |
| 02 | [Table of Content](sections/02-table-of-content/_index.md) | 0 | **Navigate**: locate a pattern, keyword, query cue, dependency, or neighboring section. |
| 03 | [FPF Readme](sections/03-first-principles-framework-readme/_index.md) | 7 | **Onboard**: understand what each part contributes before selecting a narrow pattern. |
| 04 | [Preface](sections/04-preface/_index.md) | 21 | **Orient**: read philosophy, adoption storylines, uncertainty posture, and purpose/non-goals. |
| 05 | [Part A — Kernel](sections/05-part-a---kernel-architecture-cluster/_index.md) | 21 | **Decompose and assign**: holons, bounded contexts, roles, transformers, method/work separation. |
| 06 | [A.IV.A — Signatures](sections/06-cluster-a-iv-a---signature-stack-boundary-discipline/_index.md) | 24 | **Set boundaries**: classify statements as definitions, gates, duties, evidence, signatures, or semantic repairs. |
| 07 | [A.V — Principles](sections/07-cluster-a-v---constitutional-principles-of-the-kernel/_index.md) | 36 | **Prevent confusion**: category errors, measuring, comparing, evidence graphs, mechanism suites, flow constraints, gate profiles. |
| 08 | [Part B — Reasoning](sections/08-part-b-trans-disciplinary-reasoning-cluster/_index.md) | 25 | **Compose and evaluate**: structural views (STRUCT-CAL), aggregation (Gamma), trust scores, emergence, reasoning cycles. |
| 09 | [Part C — Extensions](sections/09-part-c-kernel-extension-specifications/_index.md) | 73 | **Score, search, and architect**: epistemic quality, typed reasoning, measurement, decisions, search, agentic tool-use, quality bundles, temporal/causal/math lenses, architecture synthesis, structural adequacy, cultural evolution. |
| 10 | [Part D — Ethics](sections/10-part-d---multi-scale-ethics-and-conflict-optimization/_index.md) | 5 | **Resolve conflicts**: ethical trade-offs, bias auditing, safety overrides, conflict optimization. |
| 11 | [Part E — Constitution and Authoring](sections/11-part-e-the-fpf-constitution-and-authoring-guides/_index.md) | 53 | **Govern and publish**: pillars, guard-rails, lexical discipline, multi-view publication, publication-unit stability, transformation flows, pattern quality, ontic/U-kind governance. |
| 12 | [Part F — Unification](sections/12-part-f-the-unification-suite-concept-sets-sensecells-contextual-role-a/_index.md) | 21 | **Align vocabulary**: concept sets, sense cells, bridges, role descriptions, UTS, lexical continuity. |
| 13 | [Part G — SoTA Kit](sections/13-part-g-discipline-sota-patterns-kit/_index.md) | 15 | **Harvest and refresh disciplines**: SoTA Packs, CG-Frames, dispatchers, provenance ledgers, benchmark harnesses, shipping, telemetry refresh, dashboards, external interop. |
| 14 | [Part I — Annexes](sections/14-part-i-annexes-extended-tutorials/_index.md) | 1 | **Walk through**: expanded entry disambiguation cases for high-risk or repeatedly misclassified first-pattern choices. |
