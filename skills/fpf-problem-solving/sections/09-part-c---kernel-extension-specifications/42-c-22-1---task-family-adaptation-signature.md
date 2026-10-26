## C.22.1 - Task-family adaptation signature

> **Status:** Stable

**Purpose.**
Compare how a holder, dyad or bounded specialist portfolio acquires usable specialization on a declared task family. An adaptation signature connects the threshold, acquisition time and cost, and prior exposure with any claimed transfer, retention, downside or entry into a new solution corridor. An explicit account in ordinary prose is sufficient when these distinctions and their grounds are recoverable; a shared record can support later selector or parity use.

**Keywords.** adaptation signature; task-family specialization; time-to-threshold; budget-to-threshold; prior exposure; corridor entry; stepping stone; transfer; retention; downside field.

### C.22.1:1 - Problem frame

Final task score alone does not tell whether a holder, dyad, or bounded specialist portfolio acquired usable specialization quickly, under what budget, with what prior exposure, whether the resulting competence transferred, or whether it entered a genuinely new solution corridor. If those elements are not published together, the adaptation claim splinters across task typing, probe notes, selector prose, and parity notes, and later readers can no longer tell what exactly was being compared.

### C.22.1:2 - Problem

A comparison of specialization acquisition needs a common task family and work target, with enough acquisition history to distinguish equal final scores reached under different conditions.

### C.22.1:3 - Use this when

- the live task-family adaptation claim is not only that a holder or dyad solved a task, but how fast it acquired usable specialization on a declared task family
- comparison must stay honest about the work-measure threshold target, prior exposure, adaptation budget, transfer field, and reuse window
- movement into a new solution corridor or stepping-stone family is part of the real novelty claim

### C.22.1:4 - What goes wrong if missed

- adaptation claims collapse into vague `got better` language with no declared work-measure threshold target or budget-to-threshold account
- parity later compares outcomes that were reached under different prior exposure, different work-measure threshold targets, or different reuse windows
- nonhuman or unfamiliar solution corridors are either romanticized as novelty or dismissed as noise because the corridor entry was never typed

### C.22.1:5 - What this buys

- adaptation speed becomes reviewable by value on the same declared `TaskFamily` and work target
- later `G.5 / G.9` portfolio and parity work can compare specialization claims on the same declared basis
- stepping-stone or solution-corridor movement becomes visible as one typed part of the adaptation claim rather than one afterthought

### C.22.1:6 - Forces

| Force | Tension |
| :--- | :--- |
| Threshold crossing vs final score | A static outcome can look similar even when one system specialized much faster or more cheaply than another. |
| Local novelty vs reproducible evidence | Corridor-entry claims matter, but they are easy to over-romanticize when no baseline or entry evidence is published. |
| Task anchor vs adaptation-signature question | Task typing fixes what is being acquired; selector and parity rules govern subsequent comparisons. |
| Reuse upside vs specialization cost | Transfer, retention, and downside matter to the same claim even when the first threshold crossing looks impressive. |

### C.22.1:7 - Solution — one adaptation signature over the `C.22` anchor

- Use one shared adaptation-signature field set for this question. `G.5`, `G.9`, and later notes may cite or consume it, but they should not silently rename threshold, prior-exposure, transfer, downside, or corridor-entry terms.
- Bind the adaptation signature to the declared `TaskFamilyRef` or `TaskSignature` and work target. Reuse an existing account when it supplies the needed fields and grounds.
- The signature should expose at least:
  - `thresholdTarget`
  - `timeToThreshold`
  - `budgetToThreshold`
  - `postThresholdEfficiency?`
  - `priorExposureDeclaration`
  - `transferTarget?`
  - `transferGain?`
  - `retentionWindow?`
  - `downsideEffect?`
  - `corridorEntryBaseline?`
  - `corridorEntryEvidence?`
  - `steppingStoneEvidence?`
- Anchor these fields to the same work target and work-measure threshold semantics declared by `C.22`. State the time origin, budget boundary and threshold-observation rule. If the threshold was not reached or the available history cannot establish its first crossing, say so and retain the observed limit; do not invent a crossing time or cost.
- `C.22` continues to carry the declared task-family anchor, task typing, and baseline `TaskSignature`. `C.22.1` narrows the adaptation-signature question to threshold timing, reuse, downside, and corridor-entry disclosure over that existing anchor.

### C.22.1:8 - Corridor, transfer, and durability discipline

- If the adaptation claim depends on entering a new solution corridor, publish the `corridorEntryBaseline` first: the prior repertoire, baseline set, or comparison family relative to which corridor entry is being claimed.
- State `corridorEntryEvidence` that supports the claimed difference from that baseline, such as a reproducible solution class, a stable descriptor shift or a supported stepping-stone sequence. Name what distinguishes the corridor; an unfamiliar sample alone does not establish entry.
- If a stepping stone mattered, publish the stepping-stone evidence as part of the adaptation signature rather than treating it as retrospective color.
- Corridor or stepping-stone notes do not replace the work-measure threshold account; they explain why the adaptation path matters, not whether the threshold was actually reached.
- A fast threshold result is not yet enough to claim durable specialization.
- If transfer to a neighboring task family is claimed, name the transfer target and the observed gain explicitly.
- If retention is claimed, name the reuse or retention window rather than letting durability hide inside one isolated run.
- If specialization harms neighboring task families, narrows reusable competence, or creates de-specialization cost, publish that in `downsideEffect?` rather than telling only the upside story.
- If post-threshold performance matters to later exploitation, publish `postThresholdEfficiency?` so the claim is not trapped at the threshold-crossing moment only.

### C.22.1:9 - Worked moment

Consider two research setups, A and B, adapting to the same catalyst-search family. This is an illustrative comparison. The declared threshold is at least 80 accepted predictions out of the same 100 held-out cases under a fixed validation rule. Both start with the same training corpus and no prior exposure to those held-out cases. Time starts when adaptation begins; the budget counts all adaptation and evaluation calls. The rule checks threshold attainment at the end of each round.

A first meets the rule after 2 hours and 120 calls; B after 6 hours and 480 calls. Both finish at 85/100. The signatures therefore distinguish acquisition time and cost despite equal final scores. They report first observed attainment at the declared checkpoints, without claiming an unobserved earlier crossing.

On a named adjacent family, the same before/after test gives A 60/100 then 70/100 and B 60/100 then 60/100. That supports A's observed 10-percentage-point transfer gain on this test and no observed gain for B on it; it does not settle all neighboring families. Retention beyond the measured run is untested, and no durable-specialization claim is made. If A also claims corridor entry, it names the prior repertoire and the repeatable solution class absent from that baseline; the faster threshold alone does not supply this evidence.

The comparison can finish with these bounded claims. If A's prior exposure later proves different, reopen the equal-exposure comparison while retaining the observed histories. A later retention claim needs its own window and observations. A selector may use the signature under its applicable rule; the signature alone chooses neither setup.

### C.22.1:10 - Consequences

- Acquisition time and cost can be compared with prior exposure and any claimed post-threshold efficiency on one recoverable basis.
- Selector and parity pattern applications can consume a stable upstream specialization object without minting shadow vocabularies.
- Claimed corridor entry and known downside remain visible alongside the specialization gain.

### C.22.1:11 - Rationale

The reader needs one place where the adaptation claim stays whole. `C.22` keeps the task family and work target explicit. `A.15` distinguishes probe plans from performed Work. A claim about a particular dated Work occurrence needs A.13 and independent A.15.1 admission; precise assignment-bound attribution additionally uses F.6. `C.24` defines call-planning `CheckpointReturn` records after an action or option is fixed; `E.16` governs budget, guard, and ledger enforcement for autonomy claims. Probe results, checkpoint records, and budget records may supply evidence for the adaptation claim. `G.5` and `G.9` later compare several candidates or parity runs. `C.22.1` keeps the specialization story readable across those neighbouring pattern applications by connecting threshold timing to the claimed reuse, downside and corridor-entry evidence.

### C.22.1:12 - SoTA-Echoing

**Claim 1.** A comparison of specialization acquisition keeps the declared work-measure threshold and prior exposure explicit. It reports time and budget to threshold or states that the threshold was not reached.

**Practice source, local alignment, and adoption decision.** [FactorMiner v1 (2026-02-16)](https://arxiv.org/html/2602.14670v1), §§4.1–4.4, separates factor quality and redundancy, the effect of experience memory on screening yield, and factor-evaluation computation time. [SkillOpt v2 (2026-05-25)](https://arxiv.org/html/2605.23904v2), §§3.1, 3.4–3.5 and 4.3–4.4, changes an external skill text while holding the task-execution model fixed, selects text revisions through held-out validation, and evaluates transfer and training tokens per test-score gain. This pattern **adopts** these distinctions among the changed object, attained result, evaluation or training cost, and tested reuse.

**The shared field set is an original FPF construction.** For the question in §§1–6, §7 **adapts** those narrower comparisons by connecting the acquisition history to one `TaskFamilyRef` or `TaskSignature` and work-measure threshold. A terminal score and total cost per score gain can describe the attained result and average improvement cost, yet leave the resources needed to reach a particular threshold unresolved. Recording threshold timing and prior exposure adds observation effort but makes histories with the same final score distinguishable; §8 then separates claimed transfer, retention, and downside. The pattern **rejects** substituting either paper's reported metrics for this shared acquisition account. Reopen the comparison if a rival protocol supports the same specialization judgement with less observation, or exposes a consequential difference that these fields cannot express.

**Claim 2.** A corridor-entry claim needs a baseline and evidence for the claimed difference.

C.17 separates novelty and diversity relative to a declared comparison basis; C.18 distinguishes generated candidates, retained archives and fronts. Here that distinction supplies a conditional question: when acquisition includes a claimed new corridor, which prior repertoire and observations establish it? The fields in §8 make that evidence recoverable without treating one unfamiliar sample as reproducible entry.

**Claim 3.** Selector and parity comparisons depend on compatible interpretations of the fields they consume.

G.5 and G.9 consume this shared field set. Their users must retain its threshold, prior-exposure and conditional reuse meanings when comparing candidates; a silent downstream redefinition would change the comparison basis.

**Evidence-source note.** Use each source result with its measured object and evaluation conditions. Factor admission and skill-edition selection concern different objects from a holder's acquisition of usable specialization. For `timeToThreshold` and `budgetToThreshold`, relate the acquisition evidence named in §11 to the declared threshold and prior exposure; faster evaluation or tokens per score-point gain alone cannot supply that history. Transfer, retention, and corridor-entry claims keep their separately stated evidence requirements.

| Source-bound anchor family | Source-use relation/currentness | What it disciplines in this pattern |
| --- | --- | --- |
| Novelty and search accounts | C.17 and C.18 provide the internal distinctions used above. | Corridor baseline, descriptor shift, stepping-stone evidence, and whether novelty is reproducible rather than one unfamiliar sample. |
| Agentic adaptation studies | FactorMiner v1 and SkillOpt v2: versioned preprints, used for the bounded comparisons above. | FactorMiner distinguishes factor quality, memory-guided yield, and evaluation cost; SkillOpt distinguishes text revision, validation, transfer, and training cost. The common acquisition field set is constructed in §§7–11. |
| Transfer / retention evaluation | The applying comparison must name its observations, task family and evaluation conditions. | Transfer target, retention window, downside and reuse evidence remain separate from first threshold attainment. |
### C.22.1:13 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: a claim that a holder, dyad, team, explicitly scoped specialist portfolio, or agent acquires usable specialization faster on one declared `TaskFamilyRef` or `TaskSignature`. A method may be selected, refined, or retired as part of that story.
- This pattern keeps: threshold target, time-to-threshold, budget-to-threshold, prior exposure, transfer, retention, downside, corridor-entry evidence, and adaptation-signature fields.
- Generic "learns faster" wording without a task-family anchor leaves the adaptation claim incomplete. Faster threshold crossing alone does not establish durable specialization; retention needs its own window and evidence, and any additional transfer, downside or corridor-entry claim needs its stated grounds.

- Next-question boundary: classify the claim as Dyn1 when only a trend is live; use C.24 for call planning after the action or option is fixed; use the C.22.1 adaptation signature when specialization is the live adaptation question.

**Builds on:** `C.22` TaskSignature anchoring, `C.19.1` `BLP` compatibility, `A.15` system-role-kind and assignment, Method, WorkPlan, and Work-occurrence separation, `C.24` call planning and `CheckpointReturn` semantics after the action or option is fixed, `E.16` budget enforcement.
**Coordinates with:** `G.5` selector specialization profiles, `G.9` adaptation parity, `G.11` later telemetry/refresh reuse.

**Coordinates with:** `E.23` when repeated object improvement includes a claim of durable task-family specialization. C.22.1 supplies the adaptation account for that claim; E.23 governs the improvement loop.

**Constrained by:** `E.10` lexical discipline.

### C.22.1:14 - Not this pattern when

- the claim only needs to name the task family and work-measure threshold target, with no adaptation-speed or transfer claim at all; ordinary `C.22` anchoring is enough
- the question under repair is already selector or parity law across candidate selected sets; that belongs to `G.5 / G.9`
- the threshold or prior-exposure basis cannot yet be established: retain a narrower observation or an unresolved adaptation claim. Missing corridor evidence leaves that corridor claim unresolved; it need not prevent a separately supported threshold account

### C.22.1:15 - Conformance checklist

- `CC-C22.1-1` An adaptation signature **SHALL** bind to one declared `TaskFamily` or `TaskSignature`, one work target, and one work-measure threshold target rather than one generic improvement story.
- `CC-C22.1-2` An adaptation signature **SHALL** publish `timeToThreshold`, `budgetToThreshold`, and `priorExposureDeclaration`; if threshold was not reached, the signature **SHALL** say so explicitly instead of implying success.
- `CC-C22.1-3` Any declared transfer, retention, post-threshold-efficiency, downside, corridor-entry, or stepping-stone claim **SHALL** be explicit by value with the target, baseline, evidence source, or evidence locus named, not left as narrative garnish.
- `CC-C22.1-4` This pattern may refine specialization timing and reuse claims over the declared `C.22` anchor, but it **SHALL NOT** redefine acceptance-gate thresholds, task-family attachment, or selector/parity law governed by another FPF pattern.
- `CC-C22.1-5` Downstream selector/parity pattern applications **SHALL** cite or consume the same published adaptation-signature field set rather than silently redefining threshold, prior-exposure, transfer, retention, downside, or corridor-entry terms.

### C.22.1:End
