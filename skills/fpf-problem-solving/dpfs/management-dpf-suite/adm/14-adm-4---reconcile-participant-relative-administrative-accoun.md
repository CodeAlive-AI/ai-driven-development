## ADM.4 - Reconcile Participant-Relative Administrative Accounts

**Type:** Architectural\
**Status:** Stable

### ADM.4:0 - Use this when

Use this pattern when participants describe an administrative event or condition differently and that difference affects what someone should do. “We paid”, “we received”, “the account is active” and “the case is closed” can each be correct within one purpose while leaving another participant's question unanswered.

The subject is the administrative event or relation being described, together with the participant accounts needed for the receiving action. The first result is a usable correspondence that preserves each correct meaning, or a precise unresolved claim and its next resolver.

If the records already concern an unambiguous subject and supply adequate compatible facts for the action, use them directly. Reconciling accounts does not require a common database or a redesign of every source schema.

### ADM.4:1 - Problem frame

Several participants can be involved in one transfer, appointment or provision. Each keeps records for its own decisions. A payer records an outgoing payment; a recipient records an incoming receipt. An appointment owner records an effective assignment; a service provider records technical access. The first pair may describe one event differently, while the second pair may describe different related conditions.

A shared label, identifier or screen can conceal that distinction. A useful account identifies the subject, the claim made about it, the participant's position, the relevant time and the action for which the claim is used.

### ADM.4:2 - Problem

How can participants use their accounts together without erasing a correct difference or inventing agreement about an unresolved fact?

Forcing every record into one meaning can remove the creditor's claim or the specialist's qualification. Preserving every wording difference without examining its subject can leave an ordinary administrative action blocked. The practitioner needs a bounded correspondence, not either extreme.

### ADM.4:3 - Forces

A common event account helps coordination and reduces contradictory copying. Local accounts retain purposes, authority and distinctions that the shared representation may omit. The practitioner needs to proceed with an adequate subset of facts while preserving any uncertainty that can change the decision.

The comparison must also separate representation from effect. A consistent set of records does not itself transfer money, grant access or establish a relation. Conversely, different entry times need not mean that participants describe different events.

### ADM.4:4 - Solution

#### ADM.4:4.1 - Start from the receiving action

State what each relevant participant needs to decide or perform. A payer may need to establish whether an obligation is discharged; a recipient may need to allocate a receipt to an invoice. The administrative correspondence serves those actions.

Recover each source statement in its own terms. Ask what the participant means by “paid”: an instruction was issued, a transfer settled, or a particular obligation was discharged under an applicable rule. Retain the author, source, intended use and time when those facts affect interpretation. A source's authority matters to the claim for which it is used.

Do not demand a universal vocabulary before an ordinary action can proceed. If a supplied statement is already clear and adequate, use it.

#### ADM.4:4.2 - Identify the subjects before comparing the claims

Determine whether the statements concern one subject, different subjects, or subjects whose identity remains unresolved. Use the information appropriate to the actual event or relation: participant identities, the relevant action, source reference and its issuer, amount and currency where applicable, effective time and supporting evidence.

A matching local identifier is evidence to interpret within its source scheme. It does not alone prove event identity. Repeated participants can also take part in another event. Use SIE.5 when the cross-source identity question cannot be resolved from adequate supplied facts; SIE.4 and SIE.6 supply the needed alignment and claim-composition methods for a substantive meaning problem.

For a relation history, use ADM.3 and the direct A.6.REL identity rule only as far as the receiving use needs. A different edition of a claim can still describe the same relation.

#### ADM.4:4.3 - Choose the correct comparison result

Distinguish three situations:

| Situation | Result and next move |
| --- | --- |
| Correct participant-relative accounts of one subject | Preserve each account's meaning and state the correspondence needed for the participant actions. An outgoing payment and an incoming receipt can both describe the same transfer. |
| Different or related subjects | State the relation between them and use the appropriate facts for each question. A payment instruction, the resulting transfer and an obligation are different subjects; a label such as “payment” can refer to any of them. |
| Incompatible claims or an unresolved fact about the relevant subject | Preserve the exact claim and uncertainty. Obtain the evidence, qualified interpretation or authorized correction that can resolve it before relying on that disputed conclusion. |

These situations are distinguished by the case facts and meanings, not by a preference for agreement. Several can occur in one case: the parties can identify the same transfer and still disagree about the fee or its effect on an obligation.

#### ADM.4:4.4 - Retain only the correspondence needed for use

State the common subject and how each local account refers to it. Keep the local purpose, participant-relative meaning, effective time and authority or evidence qualification that changes the receiving action. A short joined explanation can be enough.

For the payer/recipient case, retain that A17 calls transfer T a disbursement by P and B82 calls T a receipt by Q. The shared event description can say that 300 moved from P to Q at the evidenced time. P and Q then apply their supplied conditions to their different administrative decisions.

Correct a source record only through the source's appropriate authority and procedure. A useful cross-source explanation does not authorize overwriting a participant's account or silently replacing its rule.

#### ADM.4:4.5 - Return the remaining question and stop

If the correspondence and supplied facts answer the receiving question, let the participant act under the applicable instruction. Record the useful correspondence where that action needs it.

If an amount, time or effect remains unknown, state the exact missing fact and request it from a source or checker able to establish it. If institutional applicability is disputed, return it to the competent decision maker. A technical retry is appropriate only after the state and applicable recovery rule are adequate; a missing settlement confirmation is not a reason to issue a potentially duplicate payment.

The reconciliation can finish with a correspondence plus one bounded unresolved claim. It need not make every source identical or settle questions outside the receiving use.

#### ADM.4:4.6 - What changes in practice

Participants can retain different correct descriptions and still coordinate. A handler can also distinguish a meaning problem from an unknown effect, a wrong identity or a rule question and request the right next result. Consistent wording becomes a means of understanding the event, rather than a substitute for establishing it.

### ADM.4:5 - Archetypal Grounding

#### ADM.4:5.1 - One transfer, two correct administrative accounts

In this constructed case, organization P makes one authorized transfer T of 300 currency units to hotel Q for invoice I. The case supplies bank evidence that the full amount was credited to Q at 13:00 on 10 September, with no fee deducted. The supplied invoice terms make the full 300 credit to this destination discharge P's 300 obligation. Q's supplied allocation rule applies a matching identified receipt to I. These conditions, including the authority for the payment and record actions, are inputs to the example.

P enters record A17 at 13:05 and calls T an outgoing payment or disbursement. Q enters B82 at 15:20 and calls T an incoming payment or receipt. The local record-entry events differ. Both records describe the same settled transfer at 13:00.

The handler establishes the correspondence using the bank reference with its issuer, the payer and recipient, destination, amount, currency, effective time and settlement evidence. The result is:

| Account retained | Correspondence | Action it supports |
| --- | --- | --- |
| P's A17: disbursement of 300 to Q for I | A17 describes transfer T from the payer's position. | P's responsible handler records the outgoing payment and, under the supplied invoice conditions, records the 300 obligation as discharged. |
| Q's B82: receipt of 300 from P for I | B82 describes T from the recipient's position. | Q's responsible handler allocates the receipt to I and updates the outstanding receivable under Q's supplied conditions. |

Both descriptions survive because their different directions are correct relative to different participants. The common event description supplies neither spending authority nor the rule for discharge or allocation; those are explicit inputs in this case. The participants can use this correspondence without replacing their ledgers or local record identifiers.

#### ADM.4:5.2 - The amount differs

Now suppose P's account concerns 300 and Q reports a credit of 290. The handler first asks what each amount measures. A fee, a gross-versus-net distinction, another transfer or a genuinely incorrect claim could change the answer.

If evidence establishes a 300 gross transfer and a 10 fee, those quantities can be compatible descriptions. Whether the payer's obligation is discharged still depends on the applicable payment conditions. If the evidence is unavailable, the handler preserves the unresolved credit or fee claim and obtains the needed source result. Neither a shared reference nor a familiar payment status settles it.

#### ADM.4:5.3 - The same label names different subjects

A traveller says “the trip was unsuccessful”; the travel desk says “the trip is complete”. The traveller means the negotiations produced no agreement. The desk means the travel conditions were supplied and the expense handling completed. ADM.1 separates those subjects and their connection. Treating them as two conflicting measurements of one result would send the next action to the wrong person.

In another case, two records both show “reference 17”, but the numbers belong to different issuing systems. The handler cannot combine them until identity is established. The shared numeral is insufficient correspondence.

### ADM.4:6 - Bias-Annotation

A common representation often adopts the vocabulary of the party that owns the tool. That party's purpose and authority can then appear universal. Ask whose decision each claim supports and which local qualification would be lost by the proposed common wording.

Access can also be asymmetric. One participant may have settlement evidence that another cannot inspect. Preserve the resulting reliance limit and request an adequate permitted source return; apparent silence or lack of access is not itself proof that the event failed.

### ADM.4:7 - Conformance Checklist

For the receiving administrative use, examine whether:

1. The participant actions and the subjects of the source statements are identifiable.
2. A claimed common identity is supported beyond an ambiguous shared label or reference.
3. The comparison distinguishes compatible participant-relative meanings, different subjects and incompatible or unresolved claims.
4. Relevant quantities, times, source meanings and institutional qualifications survive the correspondence.
5. Each participant can identify what the result supports and what it leaves unresolved.
6. A needed correction, evidence request or qualified decision reaches the appropriate source or responsible person.

These questions assess the usable correspondence. A separate claim that an obligation was discharged or an action was permitted still uses its governing conditions.

### ADM.4:8 - Common Anti-Patterns and How to Avoid Them

**Forcing correct directions to agree.** A common ledger replaces both “disbursement” and “receipt” with one participant's term. Preserve the common transfer and each participant's relation to it.

**Making the identifier do every job.** A matching reference is used as proof of identity, amount, settlement and authority. Establish the correspondence, then retain the separate facts each conclusion requires.

**Resolving missing effect by copying a status.** A payer's “sent” field is copied as “received” in another account. Obtain evidence of the relevant effect and preserve uncertainty until that evidence or the applicable recovery decision is adequate.

**Reconciling different subjects as contradictory views.** Negotiating work and travel administration are treated as one result. Identify their subjects and use the appropriate next action for each.

### ADM.4:9 - Consequences

A bounded correspondence can make participant accounts jointly usable while retaining their correct differences. It can reduce unnecessary schema redesign and make the unresolved question easier to route.

The result may remain partial because some meaning, evidence or institutional condition is unavailable. That limitation is useful when it isolates the exact conclusion that cannot yet be relied on. It does not require withholding every independently supported fact.

### ADM.4:10 - Architectural Rationale

The receiving action comes first because it determines which correspondence matters. Subject identity precedes comparison of participant meanings because a viewpoint label cannot establish that two statements concern the same thing. Institutional consequence follows separately because a common event description cannot determine a rule it does not contain.

Alternatives include full normalization into one account and leaving every source separate. Normalization can be economical when meanings and authority already match. It loses useful content when participant-relative meanings or decision conditions differ. Separate sources can remain adequate when one action needs only one account; a bounded correspondence is worthwhile when the participants must act together.

### ADM.4:11 - SoTA-Echoing

The practice question is how to preserve correct participant-relative accounts while producing an administrative result the parties can use. The selected line adopts SIE.4–SIE.6 for real alignment, identity and claim-composition work, and adapts the Partridge accounting and agentology comparison after the administrative subject is established.

One alternative is a single normalized representation whose terminology replaces all local accounts. The Partridge papers distinguish organizing an account around a participant from describing the common represented event, and separately examine how direction is represented. That contribution changes §§4.2–4.4 and the payer/recipient case: establish the common event, retain how each participant describes it, and keep the next institutional action under its supplied rule. The full BORO ontology and one-database infrastructure are not selected for this bounded result.

Thoroughly Modern Accounting, especially PDF pp. 9–10 and 13–14, and Ontology then Agentology, PDF pp. 5–8, supply conceptual arguments and worked representations. They do not establish the facts of a particular transfer or empirical superiority in every administrative setting. The July laboratory and later source pack supply the distinction between different subjects and different accounts of one subject. Both contributions are needed to avoid treating every disagreement as a viewpoint difference.

At comparable handling effort, a small explicit correspondence retains action-changing meaning without a full schema merger. Maintaining it has a cost when source meanings change. Reconsider the selected correspondence when a new participant, source scheme, quantity, effective-time rule or institutional decision makes the retained distinctions insufficient, or when an existing integrated account already supplies them adequately.

### ADM.4:12 - Relations

ADM.1 separates the enabled work and administrative result when a broad label hides different subjects. ADM.2 supplies participant standing and authority; ADM.3 supplies effective conditions and relation history. Use their results only when the receiving comparison needs them.

SIE.4–SIE.6 supply alignment, identity and claim composition for unresolved semantic integration. OPS.4 supplies usable current claims for ongoing handling. A.6.REL governs a relation occurrence and its distinction from revised descriptions when that history matters.

The responsible handler uses the correspondence with the applicable service or specialist instruction. In the transfer case, P's handler applies the supplied obligation-discharge condition and Q's handler applies the receipt-allocation rule. If a payment or other provision is still needed, the assigned and authorized provider follows the applicable instruction for that action. The provider performs it only when that instruction's prerequisites are met. The handler sends an unresolved substantive question to the specialist or decision maker competent to answer it.

### ADM.4:End
