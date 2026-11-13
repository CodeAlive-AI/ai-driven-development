---
name: fpf-problem-solving
description: "Use the First Principles Framework (FPF) Library, Core plus 36 domain frameworks (DPFs) stored locally, to think more rigorously than the situation's default: decompose problems, architect systems, generate real alternatives, decide under uncertainty, reconsider decisions, establish causality, design control loops, recover and improve methods, steer, hand off or resume agent work, check sources and evidence, explain, rewrite text plainly, define quality, and apply field methods for strategy, goals/OKR, operations, management, research, decision design, systems engineering, knowledge access, mathematics, notation, narrative and human capability. Triggers: FPF, DPF, fpf.tools, Levenchuk, a pattern ID such as F.19, C.11.DUA, A.15.10, GOALS.7 or STR.18, bounded contexts, assurance, SoTA packs, operational parsimony, causal/temporal reasoning, modularity, lexical discipline. Not for simple task planning, general philosophy, or Agile unrelated to FPF."
---

# First Principles Framework (FPF) Library

A transdisciplinary architecture for reasoning — an "Operating System for Thought" that turns raw
intelligence, human or machine, into organisationally usable reasoning: bounded contexts, auditable
artefacts, multi-view descriptions and disciplined hand-offs.

The Library has two layers, both stored locally:

- **FPF Core** (`sections/`) — transdisciplinary patterns with IDs such as `A.7`, `C.11.DUA`, `F.19`.
- **36 domain frameworks (DPFs)** (`dpfs/`) — methods of one field, with IDs such as `GOALS.7`,
  `STR.18`, `RMP.7`, most of them grouped into four Suites (Management, Engineering, Foundational
  Thinking, Human Capability Engineering). A DPF method builds on the Core patterns it names.

## When to use

Use FPF whenever you need to think more rigorously than the situation's default:

- Apply a named FPF or DPF pattern (F.19, C.11.DUA, GOALS.7) to the current text, answer or task
- Repair a recurring trouble in work with an agent: hedging instead of judgment, a lost original question, restarting after a handoff, look-alike alternatives, a plan passed off as done work
- Answer a field question — strategy, OKR, operations, research, engineering, teaching — with that field's framework
- Decompose a messy, cross-domain problem; identify the system that acts or changes; keep a plan, a description and a running system apart
- Decide under uncertainty: real alternatives, quality defined before comparing, causal claims checked, a decision reconsidered when its basis changes
- Find, qualify, steer or improve a way of working: methods, the next action, resuming work, removing ceremony, checklists, capability
- Architect systems and compare structures; rewrite, shorten, explain or publish an account without losing what matters
- Check sources and evidence: what to read, what an author means, whether a source supports the claim

## How to navigate

Paths are relative to this skill's directory. One script resolves every reference and says where to start:

```bash
python3 scripts/find_pattern.py C.11.DUA           # card: use when / not when, family, section lines
python3 scripts/find_pattern.py C.38 C.40 SYSE.24  # one card each, to choose
python3 scripts/find_pattern.py HCD.12:4.1         # the line of a section
python3 scripts/find_pattern.py GOALS              # a framework: entries (situation → start with), patterns
python3 scripts/find_pattern.py FPF                # the Core's practical entries and parts
python3 scripts/find_pattern.py --search okr       # ranked English-word search
```

Without Python: `grep -F "| C.11.DUA |" PATTERN-INDEX.md` (file in the third column).

### Step 0 — Choose the map by how FPF came up

| What you have | Go to |
|---|---|
| A **pattern ID, section reference or DocID** — "apply F.19", "use C.11.DUA", "GOALS.7", "HCD.12:4.1", "EXD" | Resolve it with `find_pattern.py` and read that file (Step 2) once the text, answer or task to apply it to is at hand. Skip the maps. |
| A **familiar trouble** in work with an agent, a text, sources, an explanation, options or a plan | **Map C — Common troubles** |
| A **question inside a field** — strategy, goals/OKR, operations, marketing, finance, research, decisions, systems engineering, knowledge access, mathematics, explanation, teaching people | **Map B — Domain frameworks** |
| A **general thinking need** — decompose, identify, decide, compare, establish cause, architect, revise, publish | **Map A — Core router** |
| Nothing above fits, or you are unsure | `find_pattern.py --search <one to three English words>` (translate a non-English request; partial matches are weak evidence), or `find_pattern.py FPF` for the Core's practical entries |

Before reading a pattern:

- **Have the object in hand.** If the request points at something you lack ("the advice you just gave",
  "my report"), find it in the conversation or ask for it.
- **Choose by the cards.** When several rows or patterns could fit, pass them all to `find_pattern.py`. If
  none fits, ask the user one clarifying question rather than forcing a pattern.
- **Use both layers for a field question.** The DPF gives the field's method and conditions, the Core
  patterns it cites the general reasoning.

### Map A — Core router (thinking need → Core pattern)

For a general thinking need, read [references/core-router.md](references/core-router.md): one row per need,
with the Core section and the patterns to start with. Its groups and needs:

- **A1. Model the subject** — decompose and model; identify, trace, and discover; assign roles and permissions; recover what project or case language refers to; set boundaries on what statements mean; prevent category errors; model context-dependent or indeterminate states; classify; govern ontology
- **A2. Reason, evaluate, and decide** — evaluate confidence; reason through or coordinate development; measure and compare; decide, reconsider, appraise advice, or compare contributions; reason about time and change; establish causality; design a control loop; connect mathematical and computational reasoning; resolve conflicts; define quality
- **A3. Find ways to obtain results and improve work** — recover, qualify, and develop methods; steer, resume, and recovery-test Work; screen mandatory work; request or reuse specialist results; generate alternatives; compose; use checklists; probe or develop capability; orchestrate agentic tool use; reason about cultural evolution; survey a discipline
- **A4. Architecture and structure** — describe architecture or structural views; connect transformation flows; synthesize architecture; assess structural information
- **A5. Express, publish, and work with sources** — enter and apply; sharpen expression; select and combine representations; find, read, and check sources; unify vocabulary or synthesize source ontologies; transform, document, publish, and reuse epistemes, views, or frameworks; trace provenance and revalidate affected uses

### Map B — Domain frameworks (field question → DPF)

`find_pattern.py <DocID>` prints a framework's entries and patterns — usually the fastest second step;
a Suite name (`Management`, `Engineering`, `Foundational`, `HCE`) prints its "Choose an entry" table.

| Field | Frameworks (DocID — what it works on) |
|---|---|
| **Management** | STR — direction, investment, business models, the strategizing mantra STR.18 · GOALS — goals and OKR/CFR: achievement evidence (GOALS.2), feasibility across shared people and capacity (GOALS.3), revising or ending a goal (GOALS.4), assigning work to AI agents (GOALS.7) · OPS — operations, service delivery, queues, capacity · ADM — requests, permissions, obligations, records · CGOV — corporate governance · MA — management accounting, costs, forecasts · FIN — corporate finance · MKT — markets and customers, offers, acquisition, distribution, market entry · CUST — client variation and repeatable offerings · EAM — engineering asset renewal and replacement · LDR — leadership, joint direction · CB — communities and participation · OCE — organizational change: roles, authority, capabilities · HRM — workforce, selection, reward, voice |
| **Engineering** | SYSE — systems engineering: system and use concepts, architecture, build/buy/reuse (SYSE.24), integration, AI-agent procedures · KCAE — finding, reading and using documentary knowledge, search that finds nothing · SIE — semantic integration across separately governed meanings · CAD — control architecture: observations, memory, planning and feedback · MNT — maintenance and restoration after failure |
| **Foundational thinking** | MATH — mathematical objects, proofs · MMP — mathematical modeling of a subject question · PHY — physical accounts and idealizations · CMP — algorithms under correctness and resource conditions · NOT — notation: tables, diagrams, formulas people can read, trace and change |
| **Human capability** | HCD — human capability development: what to teach for later work, programmes, feedback, assessment, transfer · SOM — somatic movement, effort and coordination |
| **Decisions and research** | PSDA — decision design: reformulate the problem, construct alternatives, compare consequences and uncertainty · RMP — research method: frame and design research, criticize evidence, synthesize studies (RMP.7) |
| **Explanation and narrative** | EXD — explanation design: what the recipient needs explained, examples, repair in dialogue · NSTD — followable narratives and working accounts that keep relations, uncertainty and source returns |
| **Economics and finance modeling** | ECO — exchange, commitments, incentives, shared resources, coordination · FDM — financial positions, rights, obligations, payment flows |
| **Practice change and spread** | IS — implementation facilitation: put an evidence-informed practice to use locally · DTM — how practices persist and spread, and how protective action changes outcomes |
| **Rhythm, music and dance** | RHY — embodied rhythmics · MDPE — music and dance practice engineering |

The Library's own map of how these fields connect: `dpfs/_index.md` (catalogue) and
`library/reference/_index.md` (Library Architectural Reference).

### Map C — Common troubles (what went wrong → pattern)

Frequent situations in work with an agent, as people notice them. The first ID is where to start; an ID
after · covers the neighbouring case named before it. For a near miss, compare cards: `find_pattern.py C.42 A.11.OP`.

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

Resolve every ID from a map with `find_pattern.py`: its *use when* and *not when* lines say whether the
pattern fits before you open the file. A framework's entries run Situation → Start with → Stop or return.

### Step 2 — Read the narrowest part of the pattern

1. Read only the file you need. Do NOT load entire sections or whole frameworks.
2. Pattern files share one layout. Read `:1 Problem frame` (does it fit the case?) and `:4 Solution`
   first; some patterns open with `:0 Use this when`. Use `:7 Conformance Checklist` to check your own
   result and `:8 Anti-patterns` to spot a known failure. `:12 Relations` names neighbouring patterns.
   `find_pattern.py` prints the line of each part, so a long file can be read by line range.
3. Links point to local files. Follow one only when the current result needs what it supplies; a
   citation can be enough as it is.

### Step 3 — Apply in plain language

Use plain language for the user. Introduce FPF-internal names (U.Holon, Gamma, F-G-R)
only when they add precision the user needs. Stop at the first useful result — a practical entry's
"Stop or return" line says when (E.11.PUA). Cite the full ID (for example `GOALS.7:4`) when the user
may want to read the source. Your own answer is subject to the first group of Map C: say plainly what
you conclude (F.19, C.11.DUA) and bring it back to the original question (C.39.QR).

### Step 4 — Compose findings across sections and frameworks

1. State each pattern's contribution in one line ("Bounded Contexts gives the parts; Trust Calculus scores our confidence in each").
2. An apparent conflict between patterns is usually a level confusion (role vs. function, method vs. work): check it with A.7 Strict Distinction.
3. Order the synthesis: the parts first, then confidence, then what to do about the gaps.
4. A DPF method and the Core patterns it cites are one line of reasoning; do not restate a Core pattern the DPF already applies.
5. Weave the patterns into an answer to the user's actual question; do not just list them.

## Library layout

`PATTERN-INDEX.md` maps every ID to its file (generated). `sections/` is the Core, one folder per Part with
an `_index.md`; `dpfs/` the frameworks (`dpfs/_index.md` catalogue, Suite and framework `_index.md`
entries); `library/USING-FPF.md` the upstream rules for references, editions and citations.

## Attribution and license

Adapted from the *FPF Library* by Anatoly Levenchuk ([ailev/FPF](https://github.com/ailev/FPF), upstream
commit `1e57ccda08ebbb9d49b7b2190bc2740b72075a13`), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/):
split into section files with generated indexes and local links; routing and Map C (a paraphrase of
Anatoly Levenchuk's cheatsheet of frequently used patterns) added. Not endorsed by the FPF author. Full
notice and the list of changes: [README.md](README.md#license). Skill packaging and scripts: MIT.
