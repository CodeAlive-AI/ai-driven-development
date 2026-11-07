# Corporate Governance Principles Framework

**DocID:** `CGOV` within **FPF Library**.

> A pattern language for making corporate decisions, arranging governing contributions, protecting rights and improving how this work is performed.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 21 September 2026
- **License:** © 2026 Anatoly Levenchuk. Original framework text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Third-party material retains its own terms.

Begin with the corporate matter and the result you need. A director, company secretary, shareholder, executive or adviser can use the methods to determine who may act, prepare a matter for decision, exercise a right, establish an arrangement or improve an existing practice.

Use the Table of Contents for a direct question. The Readme shows selected combinations of methods; the Architectural Reference explains their architecture, prerequisites and limits. **CGOV** is this framework's reference code. Its pattern numbers are stable addresses; the Parts group reading rather than prescribe an order of work.

The framework belongs to the [Management DPF Suite](../_index.md). To cite it, give the author, framework title, version shown here and, where relevant, the PatternID or Architectural Reference section.

# Table of Contents

## Public units

| Unit | Title | Use |
| --- | --- | --- |
| Readme | [Corporate Governance Principles Framework Readme](_index.md#corporate-governance-principles-framework-readme) | Use selected direct and connected examples to choose contributions and return when conditions change. |
| Architectural Reference | [Corporate Governance Principles Framework Architectural Reference](_index.md#corporate-governance-principles-framework-architectural-reference) | Understand the connected methods, their rationale, sources and limits. |
| CGOV.Reference:1 | [Problem frame - Governing a corporation through particular acts](01-cgov-reference-1---problem-frame---governing-a-corporation-t.md) |  |
| CGOV.Reference:2 | [Problem and forces - Joining competent contributions into an effective act](02-cgov-reference-2---problem-and-forces---joining-competent-co.md) |  |
| CGOV.Reference:3 | [Solution - Choose the receiving result and connect the necessary methods](03-cgov-reference-3---solution---choose-the-receiving-result-an.md) |  |
| CGOV.Reference:3.1 | [A vertical of work being performed](03-cgov-reference-3---solution---choose-the-receiving-result-an.md#cgovreference31---a-vertical-of-work-being-performed) |  |
| CGOV.Reference:4 | [Archetypal grounding - A bounded pilot commitment](04-cgov-reference-4---archetypal-grounding---a-bounded-pilot-co.md) |  |
| CGOV.Reference:5 | [Bias, limitations and consequences](05-cgov-reference-5---bias-limitations-and-consequences.md) |  |
| CGOV.Reference:6 | [Questions for use and recurrent failures](06-cgov-reference-6---questions-for-use-and-recurrent-failures.md) |  |
| CGOV.Reference:7 | [Architectural Rationale](07-cgov-reference-7---architectural-rationale.md) |  |
| CGOV.Reference:8 | [SoTA-Echoing - Source contributions and their limits](08-cgov-reference-8---sota-echoing---source-contributions-and-t.md) |  |
| CGOV.Reference:9 | [Relations, dependency and refresh](09-cgov-reference-9---relations-dependency-and-refresh.md) |  |

## Part I - Corporation, rights and powers

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [CGOV.1 - Frame the Corporate Matter and Its Governing Rules](11-cgov-1---frame-the-corporate-matter-and-its-governing-rules.md) | Stable | corporation; group; proposed act; governing rules. Which corporation must act, and which rules change the answer? | Applicable corporate rules; CGOV.2 and CGOV.3 when relevant rights or authority remain unresolved. |
| 2 | [CGOV.2 - Distinguish Shareholding, Voting Power, and Control](12-cgov-2---distinguish-shareholding-voting-power-and-control.md) | Stable | shareholding; votes; economic interest; control; denominator. Which rights do these holdings carry for this matter? | CGOV.1 for the matter; FPF A.6.REL for the distinct relations. |
| 3 | [CGOV.3 - Establish Authority for Corporate Appointments, Removals, and Decisions](13-cgov-3---establish-authority-for-corporate-appointments-remo.md) | Stable | appointment; removal; delegation; reserved matter; signing. Who may perform this act, and under which conditions? | CGOV.1 and CGOV.2 where the matter or rights are unresolved; applicable corporate powers. |

## Part II - Governing contributions and conflicts

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [CGOV.4 - Design Board and Executive Contributions](14-cgov-4---design-board-and-executive-contributions.md) | Stable | board; executive; contribution design; information; monitoring. Who should prepare, challenge, decide and follow the matter? | CGOV.3 for powers; OCE.4 for contribution design and OCE.5 where positions need design. |
| 2 | [CGOV.5 - Choose an Arrangement for Independent Corporate Oversight, with or without a Committee](15-cgov-5---choose-an-arrangement-for-independent-corporate-ove.md) | Stable | committee; remit; oversight; independence; resources. What arrangement can supply the required oversight contribution? | CGOV.3 and CGOV.4 for powers and contributions; OCE.4 for arrangement design. |
| 3 | [CGOV.6 - Expose Conflicts and Related-Party Interests](16-cgov-6---expose-conflicts-and-related-party-interests.md) | Stable | conflict of interest; related party; duty; participation. Which interest affects this matter and what changes in its handling? | CGOV.1 and CGOV.3 for the matter and duties; FPF A.6.REL for participants and conditions. |
| 4 | [CGOV.7 - Arrange Independent Review and a Disinterested Corporate Decision](17-cgov-7---arrange-independent-review-and-a-disinterested-corp.md) | Stable | independent review; valuation; eligibility; quorum. What review is needed, and who can make the decision? | CGOV.6 for the conflict; CGOV.8 for information; CGOV.11 for the subsequent corporate act. |

## Part III - Information, control, assurance and decision

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [CGOV.8 - Provide Corporate Information under Applicable Rights and Duties](18-cgov-8---provide-corporate-information-under-applicable-righ.md) | Stable | disclosure; information rights; confidentiality; timely access. What must this recipient receive, and has provision occurred? | CGOV.1 and CGOV.3 for the corporate basis; ADM.2 for permission questions where needed. |
| 2 | [CGOV.9 - Establish and Operate Internal Control](19-cgov-9---establish-and-operate-internal-control.md) | Stable | internal control; exposure; operation; response; effectiveness. How does this control change the exposure, and can it operate? | CGOV.3 for authority; OPS.18 where an operating-control contribution is needed. |
| 3 | [CGOV.10 - Obtain and Use a Scoped Audit or Assurance Conclusion for Corporate Governance](20-cgov-10---obtain-and-use-a-scoped-audit-or-assurance-conclus.md) | Stable | audit; assurance; professional conclusion; independence; scope. Does this report support the conclusion needed here? | CGOV.8 for provision; specialist engagement methods and applicable standards. |
| 4 | [CGOV.11 - Make and Record a Corporate Decision](21-cgov-11---make-and-record-a-corporate-decision.md) | Stable | corporate decision; deliberation; eligible participation; vote; resolution; record. How do authorized participants perform this decision? | CGOV.1 and CGOV.3 and any needed CGOV.6–CGOV.10 results; PSDA.14 may supply advice. |

## Part IV - Rights, consequences and renewal

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [CGOV.12 - Protect Corporate Minority Holders' Rights and Enable Contest or Exit](22-cgov-12---protect-corporate-minority-holders-rights-and-enab.md) | Stable | minority; protection; contest; exit; deadline. What right can the holder exercise, and what must be done before it expires? | CGOV.2, CGOV.3 and CGOV.8 for relevant rights, powers and information; the applicable remedy or transaction method. |
| 2 | [CGOV.13 - Monitor Corporate Performance and Require an Account](23-cgov-13---monitor-corporate-performance-and-require-an-accou.md) | Stable | performance; undertaking; accountability; denominator; response. What happened, who must account, and what response is permitted? | CGOV.3 and CGOV.11 for powers and undertakings; OCE.13 when organization-change comparison is needed. |
| 3 | [CGOV.14 - Decide Whether and How to Change Corporate Governing Instruments and Arrangements](24-cgov-14---decide-whether-and-how-to-change-corporate-governi.md) | Stable | constitution; amendment; adoption; registration; effectivity. Which acts make the proposed arrangement effective and usable? | CGOV.3 and CGOV.11 for powers and corporate acts; OCE.14 for a substantive arrangement revision. |
| 4 | [CGOV.15 - Decide Whether and How to Change Corporate-Governance Methods](25-cgov-15---decide-whether-and-how-to-change-corporate-governa.md) | Stable | method change; preparation; alternatives; variant; reuse. Which way of governing answers the recurring difficulty, and what should be retained or changed? | C.32.MWA.PP when architectural alternatives need comparison; A.3.1.MV for variants; FPF C.11.DUA for optional inquiry. |
| 5 | [CGOV.16 - Reconcile Constituent and Encompassing Corporate Governance Work](26-cgov-16---reconcile-constituent-and-encompassing-corporate-g.md) | Stable | constituent work; encompassing work; vertical; capability; simultaneous enactment. Why can a competent local action fail its contribution to the whole? | FPF B.1.5.EW for constituent/encompassing enactment; relevant corporate decision or operating method. |
| 6 | [CGOV.17 - Deliberately Continue and Change Corporate-Governance Culture](27-cgov-17---deliberately-continue-and-change-corporate-governa.md) | Stable | culture; succession; transmission; access; assistance; receiving work; retention. How can participants obtain and use the governing method? | FPF C.36 and C.36.RP for cultural relations and continuation; CGOV.16 for a missing constituent contribution. |

# Corporate Governance Principles Framework Readme

## Practical entries

These are selected examples of using the language. Bring the question from your work. If no example fits, search the Table of Contents by the difficulty, action or result and open the corresponding pattern.

You can ask an assisting agent: “Explain this and give me your comments in ordinary language, without framework jargon.” Supply the facts and applicable rules needed for your question; the agent must preserve uncertainty where those inputs do not settle the answer.

### CGOV-DELEGATION - Can this director sign the proposed commitment?

- **Situation:** A director is asked to sign a commitment, and an existing delegation may already be sufficient.
- **Question:** Who can authorize this act, and who can sign it?
- **First useful result or blocker:** The authority answer for the proposed act, including any distinct approval or signing condition.
- **Start with:** [CGOV.3](13-cgov-3---establish-authority-for-corporate-appointments-remo.md). Use the existing delegation and its conditions; [CGOV.1](11-cgov-1---frame-the-corporate-matter-and-its-governing-rules.md) helps if the corporation or proposed act remains unclear.
- **Stop or return:** Stop when the authority question is answered. If the assignment includes making the decision, continue through [CGOV.11](21-cgov-11---make-and-record-a-corporate-decision.md) or the established delegated procedure. An unmet condition limits that act; it does not automatically suspend unrelated preparation.

### CGOV-CONFLICTED-MATTER - Bring an interested-party transaction to a corporate decision

- **Situation:** A supplier transaction has favourable expert advice, but a director has an interest in the supplier and shareholders need information.
- **Question:** Which contributions must come together so that eligible participants can decide the actual proposal?
- **First useful result or blocker:** A usable answer to the unresolved authority, conflict or information question; an actual corporate decision when that is the assignment and its conditions can be met.
- **Start with:** [CGOV.1](11-cgov-1---frame-the-corporate-matter-and-its-governing-rules.md) to identify the act; use [CGOV.6](16-cgov-6---expose-conflicts-and-related-party-interests.md) for the interest and its consequences, [CGOV.7](17-cgov-7---arrange-independent-review-and-a-disinterested-corp.md) for warranted independent review and eligible participation, [CGOV.8](18-cgov-8---provide-corporate-information-under-applicable-righ.md) for information provision, and [CGOV.11](21-cgov-11---make-and-record-a-corporate-decision.md) for deliberation and decision. Existing sufficient contributions can be reused.
- **Stop or return:** Stop the affected decision when its participation or other required condition fails. Return only the missing contribution; preparation may remain possible. The connected example below explains the distinction.

Suppose the supplied rules reserve the transaction to the board, exclude the interested director from deliberation and voting, and require both remaining directors to approve. They also require a shareholder summary before the decision. Those are this case's inputs, not universal corporate rules.

The conflict account identifies the participation conditions. The information account specifies what the summary must convey and what confidential detail can be withheld. A specialist's valuation helps the directors judge terms under its assumptions. If another independent report would add no needed contribution and no rule requires it, [CGOV.7](17-cgov-7---arrange-independent-review-and-a-disinterested-corp.md) does not make commissioning one a prerequisite.

Now separate a preparatory commitment from a proposed live deployment. The case permits preparation but requires a technical release for deployment. The board may authorize preparation after the corporate conditions are met; the favourable valuation supplies neither the corporate act nor the technical release. If a director cannot participate, the existing advice remains usable while the decision awaits a permitted participation arrangement. If shareholder disclosure lacks a material assumption, repair that disclosure rather than commission a replacement valuation.

After a decision, use [CGOV.13](23-cgov-13---monitor-corporate-performance-and-require-an-accou.md) to follow the undertaking and any required conditions. [CGOV.14](24-cgov-14---decide-whether-and-how-to-change-corporate-governi.md) is useful when the governing arrangement itself needs amendment.

### CGOV-RECEIVING-WORK - Restore useful participation after a change of directors

- **Situation:** New directors have attended induction, but an important assumption still fails to enter the board's decision.
- **Question:** What prevents the contribution from being obtained and used in deliberation?
- **First useful result or blocker:** A correction directed at the missing contribution, carried into receiving work when implementation is the assignment.
- **Start with:** [CGOV.16](26-cgov-16---reconcile-constituent-and-encompassing-corporate-g.md) when the connection between the failed contribution and the larger work is unclear. Use [CGOV.17](27-cgov-17---deliberately-continue-and-change-corporate-governa.md) to establish how participants can obtain and use the contribution, distinguishing reasoning, access and transmission difficulties. [CGOV.8](18-cgov-8---provide-corporate-information-under-applicable-righ.md) supplies information provision; [CGOV.15](25-cgov-15---decide-whether-and-how-to-change-corporate-governa.md) helps when the way of preparing or discussing matters must change.
- **Stop or return:** Close a request for diagnosis with the supported diagnosis. For implementation, continue to the contribution's use under the applicable conditions. Return to the failed connection when timely access, assistance or changed preparation still leaves the work unusable.

A new director can interpret a forecast when given the papers, but a portal change delivers them after the vote. Restore timely access under the existing powers. More instruction does not repair that access failure.

Change the case: the papers now arrive on time, but the director treats income conditional on an unconfirmed customer renewal as secured. An explanation can be repeated, yet the relevant assumption is missed in a different proposal. The next move changes to targeted explanation and practice with varied proposals, using permitted specialist help. The receiving test is whether the director can use that dependency in the board's deliberation. Repeating the example establishes a narrower result.

This use has a vertical as well as a sequence. Identifying an assumption can be part of explaining a forecast while that explanation is part of deliberation on a corporate decision. The board's question determines which assumption matters; the director's ability to interpret it limits the contribution to the whole. Specialist analysis can help, while the director retains the participation and judgement required by the governing rules. [CGOV.16](26-cgov-16---reconcile-constituent-and-encompassing-corporate-g.md) explains how to recover this connection.

If the existing preparation method repeatedly hides assumptions until commitment, [CGOV.15](25-cgov-15---decide-whether-and-how-to-change-corporate-governa.md) helps change the operations within the available powers. [CGOV.14](24-cgov-14---decide-whether-and-how-to-change-corporate-governi.md) enters only when the change also requires an instrument or arrangement to be made effective. Use [CGOV.17](27-cgov-17---deliberately-continue-and-change-corporate-governa.md) to follow how participants obtain, use and retain the method across succession. A better description, a training event, performed participation and long-term retention are different possible results.

---

## Files of this publication

Generated by the skill's splitter: one file per section, in reading order.


### Corporate Governance Principles Framework Architectural Reference

- [CGOV.Reference:1 - Problem frame - Governing a corporation through particular acts](01-cgov-reference-1---problem-frame---governing-a-corporation-t.md) (10 lines)
- [CGOV.Reference:2 - Problem and forces - Joining competent contributions into an effective act](02-cgov-reference-2---problem-and-forces---joining-competent-co.md) (10 lines)
- [CGOV.Reference:3 - Solution - Choose the receiving result and connect the necessary methods](03-cgov-reference-3---solution---choose-the-receiving-result-an.md) (29 lines)
- [CGOV.Reference:4 - Archetypal grounding - A bounded pilot commitment](04-cgov-reference-4---archetypal-grounding---a-bounded-pilot-co.md) (18 lines)
- [CGOV.Reference:5 - Bias, limitations and consequences](05-cgov-reference-5---bias-limitations-and-consequences.md) (10 lines)
- [CGOV.Reference:6 - Questions for use and recurrent failures](06-cgov-reference-6---questions-for-use-and-recurrent-failures.md) (20 lines)
- [CGOV.Reference:7 - Architectural Rationale](07-cgov-reference-7---architectural-rationale.md) (12 lines)
- [CGOV.Reference:8 - SoTA-Echoing - Source contributions and their limits](08-cgov-reference-8---sota-echoing---source-contributions-and-t.md) (15 lines)
- [CGOV.Reference:9 - Relations, dependency and refresh](09-cgov-reference-9---relations-dependency-and-refresh.md) (22 lines)
- [CGOV.Reference:End](10-cgov-reference-end.md) (2 lines)

### Part I - Corporation, rights and powers

- [CGOV.1 - Frame the Corporate Matter and Its Governing Rules](11-cgov-1---frame-the-corporate-matter-and-its-governing-rules.md) (98 lines)
- [CGOV.2 - Distinguish Shareholding, Voting Power, and Control](12-cgov-2---distinguish-shareholding-voting-power-and-control.md) (112 lines)
- [CGOV.3 - Establish Authority for Corporate Appointments, Removals, and Decisions](13-cgov-3---establish-authority-for-corporate-appointments-remo.md) (105 lines)

### Part II - Governing contributions and conflicts

- [CGOV.4 - Design Board and Executive Contributions](14-cgov-4---design-board-and-executive-contributions.md) (108 lines)
- [CGOV.5 - Choose an Arrangement for Independent Corporate Oversight, with or without a Committee](15-cgov-5---choose-an-arrangement-for-independent-corporate-ove.md) (112 lines)
- [CGOV.6 - Expose Conflicts and Related-Party Interests](16-cgov-6---expose-conflicts-and-related-party-interests.md) (110 lines)
- [CGOV.7 - Arrange Independent Review and a Disinterested Corporate Decision](17-cgov-7---arrange-independent-review-and-a-disinterested-corp.md) (111 lines)

### Part III - Information, control, assurance and decision

- [CGOV.8 - Provide Corporate Information under Applicable Rights and Duties](18-cgov-8---provide-corporate-information-under-applicable-righ.md) (120 lines)
- [CGOV.9 - Establish and Operate Internal Control](19-cgov-9---establish-and-operate-internal-control.md) (124 lines)
- [CGOV.10 - Obtain and Use a Scoped Audit or Assurance Conclusion for Corporate Governance](20-cgov-10---obtain-and-use-a-scoped-audit-or-assurance-conclus.md) (128 lines)
- [CGOV.11 - Make and Record a Corporate Decision](21-cgov-11---make-and-record-a-corporate-decision.md) (145 lines)

### Part IV - Rights, consequences and renewal

- [CGOV.12 - Protect Corporate Minority Holders' Rights and Enable Contest or Exit](22-cgov-12---protect-corporate-minority-holders-rights-and-enab.md) (143 lines)
- [CGOV.13 - Monitor Corporate Performance and Require an Account](23-cgov-13---monitor-corporate-performance-and-require-an-accou.md) (152 lines)
- [CGOV.14 - Decide Whether and How to Change Corporate Governing Instruments and Arrangements](24-cgov-14---decide-whether-and-how-to-change-corporate-governi.md) (157 lines)
- [CGOV.15 - Decide Whether and How to Change Corporate-Governance Methods](25-cgov-15---decide-whether-and-how-to-change-corporate-governa.md) (177 lines)
- [CGOV.16 - Reconcile Constituent and Encompassing Corporate Governance Work](26-cgov-16---reconcile-constituent-and-encompassing-corporate-g.md) (160 lines)
- [CGOV.17 - Deliberately Continue and Change Corporate-Governance Culture](27-cgov-17---deliberately-continue-and-change-corporate-governa.md) (171 lines)
