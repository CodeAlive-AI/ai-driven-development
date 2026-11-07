## EAM.3 - Establish the Asset Information and Configuration Basis

> **Type:** Method
> **Status:** Stable

### EAM.3:1 - Problem frame

Use this pattern when a choice depends on matching asset, condition, cost and intervention records. Two records have the same station label but concern different installed units, or a proposal uses a description that no longer applies.

Start with the decision and identify which differences would change its answer. Return a usable information basis for those assets, with unresolved matches and their consequences. An adequate current basis can be reused.

For practice with record dates, installed state and quotation validity, use [the first-use task](12-eam-3---establish-the-asset-information-and-configuration-ba.md#eam341---first-use-with-two-quotations).

### EAM.3:2 - Problem

A station code, serial unit, design variant and configuration description can share a convenient name while denoting different things. Combining them can attach an old condition account to new equipment or price a modification of a configuration that is not installed. Requiring a complete database before any choice creates the opposite problem: useful work waits for irrelevant information.

### EAM.3:3 - Forces

Stable identifiers support continuity while changing configuration changes applicability. More data can improve the answer but adds collection, reconciliation and maintenance work. A missing match can block one option without blocking the whole asset question.

### EAM.3:4 - Solution

Name the receiving decision and select the information it requires. Identify the actual assets or intended asset referents, their locations and the configuration boundaries whose differences matter. Use [SYSE.13](../../engineering-dpf-suite/syse/38-syse-13---establish-configuration-identity-variants-and-effe.md) when identity, description edition or effectivity needs a fuller account.

For each relied-on record, recover its subject, source and applicable interval. Distinguish what was designed, observed, installed or proposed. A current database entry is evidence only to the extent that its source and maintenance support the claim being used.

Match the condition and performance observations to the actual unit, duty and measurement basis. Match the intervention proposal to the installed constituents and interfaces. Match costs to that same scope and horizon. State any correspondence used to join records with different identifiers.

Resolve conflicting records at their sources. A later timestamp alone does not make a record more applicable. An inspection, installation record or responsible specialist's reconciliation may settle the particular conflict. Preserve a known mismatch rather than averaging incompatible values.

Consider the consequence of each gap. If every plausible value leaves the requested answer unchanged, qualify the answer and continue. If the value changes technical eligibility, cost or service, obtain the smallest worthwhile applicable result or keep the affected option conditional.

Return the information needed for the choice in a form its recipient can inspect. A small table can suffice. Identify the configuration, duty or source change that would reopen it. An enterprise data-model redesign belongs in [EAM.14](23-eam-14---decide-whether-and-how-to-change-the-asset-manageme.md) only when that arrangement is the recurring problem being addressed.

#### EAM.3:4.1 - First use with two quotations

Use this practice when you can read asset and supplier records but still need to distinguish a record's date, the installed state and the time for which a price applies. Keep your first answer before reading the explanation and discussion. The figures and dates below are constructed teaching inputs.

**Make a first attempt.** C-07 has had drive configuration V2 since time 8; its installed state is confirmed for the required decision time 15. Quotation Q1 was issued at 12 and covers V1. A separate, unwithdrawn Q2 was issued at 6 and expressly covers the required V2 modification, service and appraisal horizon; its commercial terms remain valid until 20. Neither quotation is treated as a successive edition of the other. Which quotation can support the modification-cost claim at 15, and why? Record any correspondence or fact you cannot yet establish.

Choose an available edition containing [Use a record for one configuration-dependent claim (SYSE.13:4.4)](../../engineering-dpf-suite/syse/38-syse-13---establish-configuration-identity-variants-and-effe.md#syse1344---use-a-record-for-one-configuration-dependent-claim), including its uncertain-time explanation, and keep that copy available for the exercise. Read that bounded fragment with your attempted answer in view. Return here with the supported installed state, the quotation's subject and conditions, and the period needed by the decision. The rest of [SYSE.13](../../engineering-dpf-suite/syse/38-syse-13---establish-configuration-identity-variants-and-effe.md) is needed only if another configuration question requires it.

**Compare your reasoning.** Q2 supports the specified cost claim at 15: it covers the actual V2 modification, the needed scope and the applicable commercial period. Q1 remains a quotation for V1 despite its later issue date. Q2's issue before installation does not prevent it from describing the later installed configuration. If your actual records leave V2 or interface coverage unsettled, ask the supplier that specific question or retain a conditional cost. A quotation alone does not establish future service performance; independently applicable water-demand information remains usable.

Revise your answer where its grounds differ from this account. Then try the following changes before reading their discussions.

**Changed time.** The decision is now required at 21. Configuration and work scope are unchanged, and no renewed Q2 terms have been supplied. What remains supported?

**Discussion.** Q2 no longer supplies a valid price for the required time. Obtain applicable terms or leave the cost conditional. The installed-state account and independently usable demand information remain valid.

**Uncertain installation time.** For this separate variation, return to the decision at 15. Replace both the original installation-time premise and the confirmation of V2 at 15 with evidence of exactly one transition from V1 to V2 at a time τ in [14,16]. No independent evidence establishes the configuration at 15. Q2 covers only V2 and remains valid until 20. Can it now supply an unconditional cost?

**Discussion.** Its commercial period fits, but V2 at 15 is not established. Keep Q2's cost conditional until evidence establishes the relevant state or another applicable cost result covers the remaining possibilities. Q1's existence alone does not supply such a result. Where a requested conclusion is supported for every admissible state, retain that conclusion with its information limit; these inputs do not establish that condition for the Q2 price.

Use the same reasoning on one of your own records, stating what the available source supports and what would reopen the match. Comparing an answer with this discussion can guide correction; it does not establish independent ability on new material. If the remaining distinction is unclear, obtain competent feedback on that step before relying on an unsupported match.

### EAM.3:5 - Archetypal Grounding

In a constructed C modification case, the station register names C, the installation record identifies serial unit C-07 with drive configuration V2, and a vendor estimate prices modification of V1. The estimate cannot yet supply C-07's modification cost or feasibility.

The practitioner asks the supplier whether the proposed modification and price cover C-07/V2, giving the installed configuration and required service. A returned applicable estimate closes that gap; a statement that V2 needs another interface changes the option's cost or timing. The water-demand account can remain usable throughout this repair.

If the discrepancy concerns only an old descriptive label and the source records establish that both labels denote the same installed state, record that correspondence and reuse the estimate. No new asset or design variant is created by the label difference.

### EAM.3:6 - Bias-Annotation

Well-maintained records tend to make their assets easier to compare, which can disadvantage poorly documented sites. Treat missing evidence as an information limit rather than automatically poor condition. A vendor or asset owner may also describe scope in the way most favorable to its proposal.

### EAM.3:7 - Conformance Checklist

Can each material observation, price and intervention be matched to the right asset, configuration and use? Are actual and proposed states distinct? Does every unresolved match have a stated consequence for the receiving decision?

### EAM.3:8 - Common Anti-Patterns and How to Avoid Them

Using the latest record without checking its subject can replace applicable evidence with an unrelated revision. Match identity and effectivity first.

Completing every register field before giving advice burdens a decision that may need only one configuration fact. Select information by its use.

### EAM.3:9 - Consequences

The practitioner can combine records without silently changing their subjects. Some options remain conditional while others can be compared. Keeping the basis current costs work, so its detail and refresh conditions follow the decisions that depend on it.

### EAM.3:10 - Architectural Rationale

The information basis is organized around the receiving decision. It relies on configuration guidance already available in Systems Engineering and supplies the asset-specific joins needed for condition, cost and intervention comparison.

### EAM.3:11 - SoTA-Echoing

For deciding whether a condition observation and intervention estimate apply to the same installed asset, adopt the decision-specific configuration basis in [SYSE.13](../../engineering-dpf-suite/syse/38-syse-13---establish-configuration-identity-variants-and-effe.md): identify the unit, distinguish it from its descriptions, and establish their applicability under the relevant conditions. Adapt that result in the Solution by joining condition, proposal and cost only where the asset choice needs the correspondence. In the C-07/V2 case, asking whether the V1 estimate covers the actual configuration can resolve or expose the consequential mismatch without recollecting the usable demand information.

The serious broader alternative is a maintained configuration baseline within an integrated asset-information arrangement. GFMAM's *Asset Management Landscape*, third edition, June 2024, sections 5.4–5.5 ([pp. 66–69](https://gfmam.org/sites/default/files/2024-06/GFMAM_AM_Landscape_v3.0_English_2024.pdf#page=66)), supplies that organization-wide information/configuration comparator. Reuse such an arrangement when it already supports the needed match. Establishing or repairing the whole arrangement first can be worthwhile for repeated decisions, but its existence or a current-status label cannot settle this particular unit/estimate correspondence. The selected local reconciliation puts effort into the answer-changing gap and preserves its evidence for reuse; it accepts less coverage of unrelated assets. It does not relax applicable configuration-control requirements. [SYSE.13](../../engineering-dpf-suite/syse/38-syse-13---establish-configuration-identity-variants-and-effe.md) supplies the identity and effectivity distinctions, while the professional source describes the wider maintained capability; neither establishes C-07's installed state. Reopen the comparison if an installation or source revision invalidates a match, an unresolved difference can change the option, or repeated reconciliation costs make a shared information repair the better answer under EAM.14.

### EAM.3:12 - Relations

[EAM.1](10-eam-1---frame-the-engineered-assets-and-required-outcomes.md) selects the concern. [EAM.5](14-eam-5---assess-asset-condition-and-performance.md) uses matched observations; [EAM.7](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md) and [EAM.8](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md) use applicable proposals; [EAM.12](21-eam-12---integrate-specialist-results-for-an-asset-recommend.md) checks the results before decision. [SYSE.13](../../engineering-dpf-suite/syse/38-syse-13---establish-configuration-identity-variants-and-effe.md) governs the needed configuration basis, and [MNT.4](../../engineering-dpf-suite/mnt/15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) supplies condition content with its measurement and duty conditions.

### EAM.3:End
