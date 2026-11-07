## ADM.2 - Establish the Relevant Participants and Relations for an Administrative Action

**Type:** Architectural\
**Status:** Stable

### ADM.2:0 - Use this when

Use this pattern when an administrative action depends on who the people or organizations are to one another: who may receive a service, who is responsible for it, who may decide, or who may perform the resulting action. Typical signals are “the employee is in the directory”, “management approved”, or “the administrator can do it” without the relation needed for this request.

The subject is the organizational relation that changes the administrative action. The first result names its participants, applicable conditions and grounds, or the exact missing relation that a competent person must resolve.

Reuse an adequate supplied assignment, entitlement or grant. If the only problem is a failed technical action under already established conditions, pass that problem to the provider using the existing instruction.

### ADM.2:1 - Problem frame

An administrator works with people in several capacities. The requester can act for a beneficiary. An organization's policy owner can define service conditions while another person decides an individual request. A technical operator can implement that decision. The relevant relations may connect people, organizations, resources and particular actions.

A role title is a useful clue to the source of those relations. It is insufficient when the intended action depends on a particular appointment, delegation, permission or obligation. A person can also fill several functions, each under its own conditions. The inquiry concerns the relation required for the action, rather than a count of departments or job titles.

### ADM.2:2 - Problem

How can a handler identify the participants and organizational standing that actually determine an administrative action?

If the handler substitutes an authenticated identity or a familiar role label for the relevant relation, the service may be provided to an ineligible recipient or refused to someone whose valid relation is missing from the convenient record. If decision authority and technical capability are conflated, an implementation action can silently replace a required decision.

### ADM.2:3 - Forces

Ordinary handling should reuse reliable facts and familiar responsibilities. A consequential action may nevertheless depend on a narrower grant or a different effective interval. An organizational chart makes people findable, but it may not show the counterparty, covered action or authority that this case needs.

The handler also needs a usable return when a relation cannot be established. Collecting more identity documents will not resolve every missing delegation or eligibility condition.

### ADM.2:4 - Solution

#### ADM.2:4.1 - Name the action and the participants it requires

Start with the proposed administrative action or needed condition. Identify the participant who would receive it and the person or organization expected to supply it. Distinguish the requester from the beneficiary when that difference affects the rule.

Then identify who may decide the unresolved question and who may perform the decided action. Keep only participants that change the result. A direct request with one authorized provider may require only a short sentence; a delegated payment may require the principal, delegate, payee and responsible treasury performer.

If a name, identifier or account may select the wrong person or organization, resolve that identity question before attaching organizational standing to it. SIE.5 supplies cross-source identity work when ordinary supplied evidence is inadequate.

#### ADM.2:4.2 - Recover the relation needed for this use

State the relation in ordinary language with its participants: “Mara holds the appointment covered by the archive eligibility rule”, “the archive custodian may grant read access to collection R”, or “Lee may configure the access that the custodian has granted”.

Recover the applicable source and conditions. Ask what establishes the relation, what action or resource it covers, when it applies, and what relevant restriction or ending condition can change the present use. A supplied current assignment can answer this inquiry directly. OCE.6 provides assignment results for an organizational-change question; reuse one only for the participants and responsibilities it actually establishes.

A.6.REL governs the underlying distinction between a relation obtaining and someone asserting or recording that it obtains. Its ordinary branch permits a readable relation statement. Add an occurrence identifier or a full relation model only when later work needs to distinguish another occurrence of that relation, including a later episode with the same participants.

#### ADM.2:4.3 - Keep eligibility, decision authority and performance distinct

For the intended action, ask which relation supplies each necessary condition. An effective appointment can make a person eligible to request access. A valid grant can permit a particular read action. A separate assignment and permission can allow a technical operator to configure the resource.

These facts can be supplied together in a well-designed service instruction. Keep them separately recoverable when a failure, restriction or later use depends on the difference. A.2.8.PER supplies the distinctions between granted permission, actual exercise and a finding of non-prohibition. A finding that no prohibition was located cannot fill a missing grant where the applicable rule requires one.

When a grant and another governing requirement imply incompatible conclusions for the same participant's action, identify the conflicting claims and their overlapping scope and time. First apply an existing precedence rule when its stated conditions select which claim governs that use. If the rule does not settle the conflict, reuse an adequate existing authorized decision or ask the person whose authority covers this conflict to decide which claim governs the specified action, scope and interval. Until a rule or such a decision settles it, return that question as unresolved. Do not infer precedence from record recency, seniority or technical capability alone.

#### ADM.2:4.4 - Return the usable participant account or the specific gap

The first result can be a short statement attached to the request. Name the relevant participants, the relation needed for each action, its effective conditions and the grounds that the receiving decision needs. Keep an unsupported relation claim explicit as a claim requiring resolution.

For example, “the supplied appointment establishes eligibility from 1 October; a read grant is still needed from the archive custodian” is actionable. “More approvals required” conceals the missing result and the person who can supply it.

A missing fact goes to a source or checker able to establish it. A missing grant or disputed rule application goes to the competent decision maker. If a valid condition is already met and provision failed, send the provider the authorized action and actual failure. Identification of a gap does not itself resolve it.

#### ADM.2:4.5 - What changes in practice

The handler asks the right person for the particular missing result and reuses adequate relations already supplied. Identity checking, eligibility, authority and technical performance no longer substitute for one another. The request can proceed as soon as its actual conditions are established.

### ADM.2:5 - Archetypal Grounding

#### ADM.2:5.1 - One access request, three different grounds

This constructed case concerns Mara reading collection R on 2 October for experiment E. The supplied archive rule makes an effective research appointment an eligibility condition. It authorizes the archive custodian to grant access and assigns technical configuration of an approved grant to Lee. The following case facts are supplied:

| Relevant relation | Supplied fact | Administrative consequence |
| --- | --- | --- |
| Research appointment | Mara's appointment is effective from 1 October and covers experiment E. | The appointment satisfies this case's stated appointment condition on 2 October. |
| Read grant | The custodian's valid grant permits Mara to read collection R during October. It excludes downloading. | The permitted action is reading within that scope and interval. |
| Configuration responsibility and permission | Lee is assigned and permitted to configure the granted access. | Lee can perform that configuration; a different access decision remains with the custodian. |

The handler can now ask Lee to repair Mara's failed login under the read grant. The result of this pattern is the participant and relation account that makes that request legitimate and precise. Whether Mara can actually read the collection still depends on successful provision.

A download request is a different action. The handler can state that it falls outside the supplied grant and return it through the archive's applicable decision route. The read grant is not widened by the technical availability of a download button.

#### ADM.2:5.2 - A familiar name identifies the wrong person

A directory contains two people named Mara. The appointment refers to one and the account request to the other. The handler first establishes the participant identity using the relevant sources. The appointment cannot be applied to the second person merely because the name matches.

If the identity and appointment were already unambiguous in an adequate request, the handler would reuse them. This pattern does not impose duplicate identity checking on every case.

#### ADM.2:5.3 - An applicable rule and an unresolved conflict

In both branches of this constructed case, Mara has the valid October read grant for collection R. A current security restriction prohibits reading that collection from 09:00 to 11:00 local time on 2 October. Her intended read is at 09:30. The grant and restriction therefore give incompatible conclusions about the same participant, action, collection and interval. The supplied authority account names the archive policy owner as the person authorized to resolve this kind of conflict.

In the first branch, an applicable policy explicitly gives that temporary security restriction precedence over read grants during the stated interval. The handler applies the rule and returns its result: the restriction governs Mara's 09:30 read, so that action cannot proceed under the grant. No further discretionary decision is needed to settle this inquiry. The result concerns the stated overlap; it does not rewrite the October grant.

In the second branch, the same grant, restriction, intended action and decision authority are supplied, but no applicable precedence rule or existing resolving decision is available. The handler returns the particular unresolved question to the archive policy owner: which claim governs Mara's read of R at 09:30 within the 09:00–11:00 restriction? Naming that person does not supply the answer. The handler does not authorize the disputed read from these inputs.

### ADM.2:6 - Bias-Annotation

Organizational charts and provider tools tend to foreground staff and ignore claimants, contractors, external counterparties or people represented by someone else. Include a participant when their relation changes the requested action, even if the convenient tool has no field for it.

Visible seniority can also bias a handler toward assuming authority. Recover the action-specific basis when it matters; expertise, employment, ownership and permission can have different implications under the supplied rule.

### ADM.2:7 - Conformance Checklist

For the named action, examine whether:

1. The requester, beneficiary, provider and decision maker are distinguished where their difference matters.
2. The needed relation is stated with its participants and applicable rule or adequate supplied result.
3. Its action, resource, interval and relevant restriction fit this use.
4. A role title, authenticated identity or technical capability has not replaced a missing institutional condition.
5. The result distinguishes an established relation, an unresolved claim and a missing decision.
6. The next request names both the missing result and someone competent to supply it.

The participant account supports the receiving action only within those conditions. It does not establish that the action was performed.

### ADM.2:8 - Common Anti-Patterns and How to Avoid Them

**Using the organizational chart as a universal permission table.** A person's department is known, but the requested expenditure exceeds the supplied delegation. Recover the delegation for that action and return the uncovered decision to its competent holder.

**Asking the technical operator to decide entitlement.** A provisioning team receives “please make it work” although eligibility is unresolved. Obtain that decision first, then give the operator the resulting action and scope.

**Repeating the wrong check.** Another identity check is requested when the actual missing fact is whether an appointment is effective. Reuse adequate identity evidence and resolve the relation or time question.

### ADM.2:9 - Consequences

A precise participant account can reduce misdirected questions and make delegated actions intelligible. It also exposes places where an organization has no clear deciding or provision responsibility.

The account may require qualified interpretation of a policy or relation. That can limit the dependent action. A supported eligibility result can remain useful while a distinct permission question is unresolved.

### ADM.2:10 - Architectural Rationale

The pattern begins with the action because that determines which relations matter. Starting from every relation a person has would make an ordinary service request unnecessarily large. Starting from a job title alone would lose the conditions that justify the action.

General relation and permission instructions remain with their FPF suppliers. The administrative contribution is the use-specific join: whose institutional standing supplies the requested condition, whose decision is needed, and which provider can act on it. That join can remain a readable sentence when the inputs are adequate.

### ADM.2:11 - SoTA-Echoing

The practice question is how to use organizational standing without confusing identity, eligibility, decision authority and provision. The selected line adopts A.6.REL's obtaining-versus-assertion distinction and A.2.8.PER's granted-permission distinctions, and adapts the laboratory's rule-owner, handler and provider separation to the administrative request.

One alternative is to infer entitlement from a directory identity, organizational title or technical account. NIST SP 800-63-4 is a bounded comparator: its identity-proofing, authentication and federation model helps identify what a digital-identity result actually establishes. It does not decide this archive's eligibility or read grant. That comparison changes §§4.1–4.3 and the access case: retain the supplied identity result and obtain only the different relation that remains missing. The extra explicitness is justified when that difference changes the action; adequate combined inputs can still be reused directly.

The May and June laboratory discussions provide failure examples and the specialist/handler distinction. OCE.6 supplies an actual assignment method for its own organizational-change question. Neither a reported incident nor an identity standard proves that a local authority relation obtains; the supplied rule and case facts do that work.

Reconsider how the handler establishes participant standing and authority for the intended action if a different institutional regime changes who can decide, if a grant's beneficiary or scope cannot be resolved by these instructions, or if a simpler available method preserves the same action-changing relations more reliably.

### ADM.2:12 - Relations

ADM.1 supplies the needed administrative condition when the action is unclear. ADM.3 determines the relevant effective time or relation change. ADM.4 handles incompatible or differently organized accounts of the participant or relation.

A.6.REL supplies relation obtaining and conditional occurrence identity. A.2.8.PER supplies the permission distinctions. OCE.6 can supply an adequate effective assignment; SIE.5 supplies identity resolution when sources do not select the participant reliably. The case's existing service instruction uses the resulting facts for its own decision and provision.

### ADM.2:End
