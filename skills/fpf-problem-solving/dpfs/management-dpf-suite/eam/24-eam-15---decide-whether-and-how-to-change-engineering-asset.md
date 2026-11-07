## EAM.15 - Decide Whether and How to Change Engineering Asset-Management Methods

> **Type:** Method
> **Status:** Stable

### EAM.15:1 - Problem frame

Use this pattern when the reusable way of making asset decisions no longer answers current questions, or when a new technique could improve it. A condition ranking fails a coupled investment choice, a forecasting model no longer fits demand, or a new optimizer promises improvement without accounting for its data and interpretation burden.

Begin with the working question and the reusable operation that may need change. Return an adequate existing Method, a supported change or an explicitly qualified candidate. A new standard edition or tool release alone is not a reason to replace the repertoire.

### EAM.15:2 - Problem

Template, software and vocabulary changes can be mistaken for Method improvement. Conversely, a changed rule for eligibility, comparison or stopping can be hidden inside a spreadsheet update. Selecting techniques by fashion leaves their actual contribution and continuing burden unresolved.

### EAM.15:3 - Forces

Reusable Methods improve consistency while their assumptions can fail as assets and environments change. More sophisticated analysis can improve a consequential choice but demand unavailable evidence or displace useful work. General reuse needs enough explanation of applicability without freezing one context's inputs as universal rules.

### EAM.15:4 - Solution

Name the asset-management result and present difficulty. Recover the current way of obtaining it: operations, necessary inputs, comparison rules, applicability, useful result and stopping conditions. Distinguish a Method question from missing data, a tool failure or an organizational bottleneck.

Compare the existing way with materially different alternatives using the same question. Consult the relevant current technical sources, preserve their scope and identify what each alternative changes in practice. A different rate or asset price can be an input change; a different eligibility or selection rule can change the reusable way of doing.

Test the alternatives on the situations that expose the claimed difference. A desk calculation can establish a mathematical failure or improved answer for those inputs. A claim about real practitioner effort, decision quality or continuing effectiveness needs evidence of that actual use.

Compare the whole burden of obtaining, using and maintaining the proposed technique, including model fitting, data, interpretation, training and displaced decisions. Select further inquiry or a trial only when its attainable result can change the choice or warranted claim enough to justify that burden.

State the selected disposition. Retain a sufficient Method, adopt a supported change within actual authority, keep a candidate for a bounded trial or return the specific unresolved result. A current answer to one asset question need not wait for a general field-effectiveness study.

When later users need to distinguish a reusable variant, candidate lineage, changed description or tool, use [FPF A.3.1.MV](../../../sections/05-part-a---kernel-architecture-cluster/27-a-3-1-mv---construct-and-maintain-a-method-variant.md)'s provenance and reuse guidance. Preserve which operations are proposed, where they came from, the conditions and tests supporting them, and what remains untried. A desk calculation can establish how a proposed comparison works on supplied inputs. To report its actual application, identify the practitioners, the appraisal occasions, the operations they performed with the available information and support, and the results they returned. Neither a proposal nor its successful calculation establishes that later users have applied it.

Keep the applicable repertoire and its reconsideration conditions discoverable to users. Reopen it when a new problem, evidence or technical result changes its contribution; avoid mandatory refresh merely because a date or publication changed.

### EAM.15:5 - Archetypal Grounding

For CityWater, consider the candidate rule “fund the highest-condition-priority asset first, using its individually preferred option.” A priority order D, C, A, B would allocate 3 to D replacement, 3 to C modification and 2 to A refurbishment, exhausting the capital before B's required option. The rule fails to supply the needed four-station programme under the declared conditions.

Combination comparison instead finds FFMK within capital and service constraints. This desk case establishes the limitation of the priority rule for this problem and supplies a supported present answer.

For repeated use, practitioners can compare the techniques on representative cases with the same available inputs, recording unmet constraints, decision differences and total analysis effort. A bounded trial is useful when those real-use consequences can change adoption. Adding a more complex optimizer to a sixteen-combination problem needs a gain beyond producing the same answer.

### EAM.15:6 - Bias-Annotation

Successful demonstrations can overrepresent easy cases and expert users. Compare relevant failure cases, data availability and routine practitioner burden. A tool's technical benchmark can differ from the asset decision's useful result.

### EAM.15:7 - Conformance Checklist

Is the changed object a reusable operation, an input, a description or a tool? Does the comparison use the same practical question and preserve applicability? Is the gain supported at the scope claimed, with full burden and candidate status visible?

### EAM.15:8 - Common Anti-Patterns and How to Avoid Them

Equating newer software with a better Method bypasses the receiving decision. Compare its contribution using relevant cases.

Treating one successful calculation as field effectiveness overstates the evidence. Keep the mathematical result and observed practice claim separate.

### EAM.15:9 - Consequences

The repertoire can remain useful as asset questions and technical knowledge change. Some incumbent Methods are retained, some candidates need evidence and some techniques are unnecessary for the current task. Maintenance of reusable guidance has its own cost and responsibility.

### EAM.15:10 - Architectural Rationale

The pattern concerns reusable ways of obtaining asset-management results rather than the organization or one asset choice. It uses direct technical comparison and the existing Method Engineering contribution.

### EAM.15:11 - SoTA-Echoing

The common source account distinguishes professional concerns from technical Methods, including the limits of ratio ranking and whole-cost comparison. This pattern compares applicable contemporary techniques for the working question.

### EAM.15:12 - Relations

[EAM.1](10-eam-1---frame-the-engineered-assets-and-required-outcomes.md)–[EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) supply the working questions and outcomes that motivate Method change. [EAM.14](23-eam-14---decide-whether-and-how-to-change-the-asset-manageme.md) supplies an arrangement change where needed; [EAM.16](25-eam-16---deliberately-continue-and-change-engineering-asset.md) concerns cultural continuation. [FPF A.3.1.MV](../../../sections/05-part-a---kernel-architecture-cluster/27-a-3-1-mv---construct-and-maintain-a-method-variant.md) supplies variant, provenance and reuse guidance. [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) governs the worth of additional inquiry and trials.

### EAM.15:End
