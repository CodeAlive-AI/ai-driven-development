## SYSE.8 - Develop an Integrated Offering and Provider Concept for Using an Engineered Result

> **Status:** Stable

### SYSE.8:0 - Use This When

Use this pattern when a project is defining what a provider will make available and under what promise. The
proposal may, for example, transfer a product, grant access to a shared enabling System, maintain an agreed
condition, or accept responsibility for an agreed result, but the project has not yet connected that promise to
the provider arrangement needed for the receiving use.

The result is an **account that connects a bounded offering to the provider arrangement, responsibility claims,
and evidence needed for it**. It becomes an input to engineering and neighboring decisions. The account
describes an engineering proposal; commercial viability, actual provider Systems, performed Work, duties, and
authority claims require their own support.

Apply the pattern when a choice among forms of provision—for example, transfer, access, continuing provision,
or responsibility for a result—changes the engineered System, interfaces, provider Systems, capabilities,
risks, or realization network. A mere change from *product* to *service* wording is outside its boundary. Use `A.2.3` for promise content alone; use `SYSE.1`,
`SYSE.16`, and `SYSE.2` when the engineering subject, its use or its relation to the product SoI is unclear. Neighboring specialist practices retain
their own Methods, results, and authority—for example, practices governing demand, positioning, price, finance,
legal duty, organization change, continuing operations, or shared enabling Systems.

#### SYSE.8:0.1 - Terms and Distinctions

The everyday words in this field are overloaded. Recover the object or relation before relying on them:

| Name in this pattern | What it denotes |
| --- | --- |
| client-side use | A bounded actual or possible-future situation in which a receiving System obtains or attempts to obtain a result. A scenario or journey is a description of that use. |
| promise content | A consumer-facing `U.PromiseContent` episteme stating the promised outcome, applicability, access terms when access is promised, and acceptance claims. Ground the provider, Method, Work occurrence, and any commitment through their own relations. |
| supplied or accessed subject | The product, asset, material portion, data, episteme, capability access, or other subject transferred, changed, accessed, or made available. It need not be a System. |
| provider System | An actual System that participates in a named provider relation, is classified under a local provider SystemRole kind, or holds an assignment under that kind. A department or company name is only a clue until the underlying System and relation are identified. |
| provider arrangement | The Systems and relations through which provision is expected to happen. Its account distinguishes actual providers and partners from possible-future provider referents. |
| integrated offering concept | The engineering proposal connecting a bounded offering to the provider arrangement needed for the receiving use. This local collective name preserves the kinds of its participants. |
| fulfilment or acceptance claim | An assertion of whether specified promise content was fulfilled or a named acceptance occurred, under stated conditions and within a declared window. An evaluator assesses evidence and reaches the judgement. The assertion and the underlying fulfilment or acceptance remain distinct. |

Bare *service* is a recognition cue. At a consequential use, apply the FPF service-word recovery in
`A.6.P:4.11a` and name the recovered referent or relation. A local `ProviderSystemRole` kind, an assignment
occurrence, an actual provider System, its capability, its Method, and its dated Work remain different objects.

### SYSE.8:1 - Problem Frame

Many engineered results are usable only through an arrangement that continues beyond transfer of a product.
For example, software needs operating infrastructure and change capability; a machine may need consumables,
calibration, maintenance, logistics, data, trained operators, or financing; and a promised condition such as
temperature, availability, or stock level needs Systems that can observe and restore it. Changing the commercial
or access relation can also change the technical architecture and the allocation of risks—for example,
variability, failure, asset, or update risk.

Product-only engineering leaves those changes to later improvisation. Service-first rhetoric creates the
opposite failure: every object and Work occurrence is bundled under one broad word, and the project assumes that
renaming the offer creates a desired effect—for example, demand, recurring revenue, sustainability, or
provider capability.

### SYSE.8:2 - Problem

A plausible technical product concept can coexist with an impossible provider concept. Recurring mismatches
include promising availability without observing the relevant state, retaining ownership without financing or
maintenance capability, automating access while transferring exception Work to users, and depending on partner
Systems whose responsibilities and interfaces are not engineered.

Four failures recur in engineering descriptions: a business model omits bearer and interface constraints; a
technical architecture description omits obligations and continuing Work; an SLA omits the actual provider
arrangement; and a service blueprint is treated as evidence that provision will work. Use the descriptions needed
for the bounded decision, with their claims and omissions explicit.

### SYSE.8:3 - Forces

The engineering decision must manage these recurring tensions:

- A first concept must support its receiving decision with proportionate effort, while the provider arrangement crosses several kinds of boundary—for
  example, technical, operational, organizational, financial, legal, or commercial.
- Arrangements such as product transfer, access provision, continuing activity, availability responsibility,
  or result responsibility allocate assets, variability, evidence, and risk differently.
- Provider Agents need freedom to choose Methods, yet promise content and acceptance claims must be explicit.
- A technically feasible arrangement can be commercially unattractive; a commercially attractive promise can
  be physically unrealizable.
- Partner Systems and internal shared enabling Systems can supply capability through relations that make them
  neither parts of the provider System nor subjects of the same project.
- Continuing provision needs a dependable arrangement, while changed conditions or evidence can require
  reconsideration of both the offering and provider choices.
- Current PSS and servitization literature supplies many representations and Methods. Selecting one for the
  current use and claiming a performance gain still require project evidence.

### SYSE.8:4 - Solution

Develop client-use and provider-arrangement candidates together. Name the engineering decision that consumes
each choice and obtain needed specialist results from the responsible practice.

First inspect available accounts of this use. Reuse one that already connects plausible alternatives, the
provider's and client's decision-relevant Work, and applicable grounds to the receiving decision. If a missing
connection can change the choice, develop that connection through :4.1 and preserve unaffected grounds. When
the receiving use or the range of possible arrangements is itself unsettled, use the relevant PSS design work
in :11 to generate candidates before qualifying them for the engineering decision.


#### SYSE.8:4.1 - Perform the Move

1. **Bound the use and decision.** Name the client-side use, intended change, receiving Systems, the actual System or intended System referent selected for engineering, configuration, horizon and decision. When engineering a provider, retain the product uses and obligations that ground its capability and distinguish them from the provider's local acceptance. Use `SYSE.1`, `SYSE.16`, or `SYSE.17` results only
   when they fit that subject, configuration, use, horizon, decision, and evidence window. Otherwise use a
   qualified direct source or record the missing result, then pause only the decision that needs it. These result
   dependencies do not prescribe the order of Work.
2. **Recover the promise.** State the consumer-facing promise content and its edition, eligibility or
   applicability, access terms when access is promised, acceptance conditions, and the evaluation Method and
   evidence needed to evaluate fulfilment. Keep each actual commitment, permission, delivery relation,
   acceptance relation, payment, and Work occurrence separate.
3. **Name the subject.** Identify what is transferred, accessed, changed, used, restored, or kept within a
   stated range or condition: for example, a machine, material lot, software edition, data, access point, temperature range,
   stock state, or performed Work. Keep non-System subjects in their recovered kinds.
4. **Compare materially different candidates.** Reuse applicable alternatives and generate further ones when
   an unresolved decision needs them. Plausible arrangements include product transfer with support, access or
   use provision, continuing availability responsibility, result-oriented provision, and mixed forms. Retain
   variety when evidence can still change the choice.
5. **Develop the provider structure.** For each candidate, identify the actual provider and partner Systems.
   Represent a provider that does not yet exist only as an intended referent in a possible-future claim. Record the
   relations and assignments that obtain. Then name the capabilities, Methods, recurring and exceptional Work,
   interfaces, resources, data, tools, shared enabling Systems, supply relations, and recovery arrangements that
   can change the decision. State the kind of each relation—for example, parthood, interaction, transfer, access,
   obligation, or contribution—and ground it independently of any intended referent.
6. **Separate expected Work from responsibility and authority.** For planned Work, name the intended performer
   Agent or the conditions for selecting one, together with the sought result. For Work that has occurred, identify the actual performer Agent and the Work
   independently; add assignment-bound attribution only when the receiving use needs it. Separately identify the
   System that holds or owns each asset; the Agent expected to bear or manage variability and failure exposure,
   observe or restore a condition, and receive each decision or evidence result; and any current responsibility,
   commitment, permission, legal duty, or authority relation.
7. **Connect realization and continuing change.** Identify the realization and change Work, its intended or
   actual performer Agents as applicable, and the Systems it uses or changes. Name the subjects changed—for
   example, the product, provider capability, interfaces, data, operating arrangement, or shared enabling
   Systems. State what later evidence or change will reopen the concept—for example, evidence from a new
   configuration, update, migration, maintenance event, partner change, or recovery attempt.
8. **Obtain specialist results.** Request a specialist result only when it can change the candidate—for example,
   a result from strategy, marketing, commercial analysis, finance, law, organization change, operations,
   supporting-System engineering, safety, security, or environmental engineering. Preserve its source and
   authority boundary. When finance depends on the engineering result or its acceptance, use :4.4 to develop the connected alternative.
9. **Compare the candidates.** Compare decision-relevant consequences—for example, client-side use, technical
   feasibility, architecture, capability, value, cost, financing, risk allocation, operational burden,
   changeability, evidence, or affected-System consequences. Keep non-equivalent measures separate unless an
   explicit aggregation Method preserves the distinctions used by the decision.
10. **Record the bounded concept.** Give each candidate one current disposition: select it, retain it for later
    comparison, branch it by a stated condition, or reject it. Record unsupported claims, needed specialist and
    realization results, responsibilities, evidence needs, and conditions for reconsideration. A conditional
    candidate is useful when it makes the next decision visible.

Analysis of use, concept development, architecture, organization change, operations, commercial analysis, trials,
and realization Work can overlap and reopen earlier decisions. Each receiving decision needs the particular
inputs on which it relies; the numbered explanation does not determine when every activity must occur.

#### SYSE.8:4.2 - Record the Result

For a new account, begin with the client-side use and decision, one promise claim, the supplied or accessed
subject, one actual provider System or named possible-future provider referent, one critical Work or direct
relation, and one evidence gap or receiving decision. An adequate existing result can be referenced and used
directly; adopting this Method does not require recopying it.

Expand this account through the moves in :4.1 only where another fact can change the current candidate.
Details that cannot yet change it may remain *not yet needed*. Mark a needed but unavailable answer as
*unknown* and name the claim or decision it blocks. The account can use several representations; use those
descriptions as sources and ground the provider arrangement in its actual Systems and relations.


#### SYSE.8:4.3 - What Changes in Practice

The practitioner follows the receiving use beyond product transfer, exposes the provider's continuing Work and
the burden passed to the client, and returns their consequences to the engineering decision.


#### SYSE.8:4.4 - Connect the offering to conditional finance

Use this continuation when obtaining money depends on a technical result or its acceptance, or when financing terms change the result the provider can supply. An adequate funded arrangement can be used directly. The question here is how to develop a coherent offering when the engineering and financial conditions still change one another.

**Connect the promised result to the event that permits payment.** For each live candidate, recover the required functioning and operating conditions, the configuration to which the evidence applies, and what must be observed or demonstrated. Identify who judges that result and what the proposed terms make payable after that judgement. Obtain the applicable terms and event interpretation through [FDM.1](../../fdm/09-fdm-1---recover-the-financial-position-behind-a-record.md) and [FDM.3](../../fdm/11-fdm-3---derive-events-and-conditional-flows-from-financial-c.md) when those relations are unresolved. Keep the technical result, its acceptance, the payment obligation and the money's usable date distinguishable. A satisfactory trial can support the technical claim while the agreed payment still arrives too late for the next construction action.

**Ask finance for the condition that the engineering proposal must resolve.** Supply the relevant realization and operating account, including the work and means needed to obtain the acceptance evidence. [FIN.2](../../management-dpf-suite/fin/15-fin-2---assess-liquidity-and-funding-needs-by-date.md) returns the payer, amount, usable date and remaining exposure; [FIN.10](../../management-dpf-suite/fin/23-fin-10---design-financing-instruments-and-terms.md) constructs or compares terms with prospective participants. Recover which technical or acceptance premise those results consume. If funds are released after commissioning but commissioning needs those funds, the current proposal has no funded start. ECO.4 supplies the general construction of attainable complementary commitments; the engineer must still identify a realizable first result and what its evidence establishes.

**Develop the changed offering with the affected specialists.** Work back from that failed condition. A smaller independently useful result may be obtainable with available means. A different bearer, temporary qualified operating method, supplied component or division of responsibility may change the first payment, preparation cost or continuing work. Compare these with retaining the technical arrangement and changing only financing. Preserve the receiving use's necessary performance and protection; a proposed reduction in the promise needs the affected recipient's decision.

For every serious variation, explain what changes in functioning, realization, observation, recovery and provider capability. Obtain the corresponding operating and financial consequences. For example, replacing an automatic observation with a manual one requires an adequate observation method, capable available performers and an interval that fits the required response. Its recurring labour and exception work belong in the new account. A temporary method also needs a supported end or transition; calling it temporary supplies neither the replacement nor the work of switching.

An earlier milestone can become a financing condition if a participant accepts the result it actually establishes and the exposure that remains. A readiness test might justify an advance while leaving performance in use to later acceptance. State that allocation in the proposal. Changing a payment milestone does not make the earlier evidence establish the later performance claim. Conversely, a qualified earlier test can be useful even when it does not establish the entire service: use its result for the bounded decision it supports.

**Return one compatible alternative to both decisions.** Send the changed configuration, evidence requirement, preparation and operating work to the financial contributor. Return the resulting cash dates, conditions and restrictions to the engineering and provider decisions. Replace the affected premises together: a new advance changes the later amount due, while a new operating method can change the cost and meaning of acceptance. Use FIN.10 for participation, financing claims and closing, and ECO.3–ECO.4 when the missing contribution is a different exchange or combination of commitments. The participating decision-makers retain their respective authority.

Follow an ordinary completion and a consequential interruption through the proposed arrangement. If evidence arrives late, fails, or applies to another configuration, determine which payment, draw or next action is still supported and what remains due. Reconsider the dependent construction or service commitment while it can still be changed. A contractual remedy for failure can allocate loss without providing the means to maintain the promised functioning; obtain the engineering recovery separately.

Return the supported concept, a conditional proposal for the participants, a justified wait for a specified result, or rejection of an unsupported arrangement. A wait is useful only while it can still meet the receiving need or leads to an agreed changed need. Technical approval, acceptance of commercial terms and provision of money remain decisions or events of their respective participants. This engineering account supplies their connection and the design consequences; it does not itself perform those acts.


### SYSE.8:5 - Worked Case: Cast-Iron Transfer, Delivery, or Replenishment

A foundry organization and a machining company must decide how an accepted grey-cast-iron lot will reach the
machining plant. The lot is a material portion, not a System. They compare three arrangements for the same
machining use, material specification, unloading point, and planning horizon.

A commercial lead may decide price and credit and select an arrangement only after an operations coordinator
accepts its schedule. Each person has a current assignment and a separate authority relation. The assignments
identify their project participation; they do not create authority.

#### SYSE.8:5.1 - The Three Alternatives

| Candidate | Offered result | Allocation proposed |
| --- | --- | --- |
| **Gate transfer** | The accepted lot is available at the foundry gate. | The foundry performs production Work; the machining company arranges transport from the gate. |
| **Scheduled delivery** | The accepted lot reaches the plant's unloading point between 08:00 and 12:00 on the agreed day. | `ForgeHaul-A` is the proposed logistics-provider System, with transport and exception recovery described below. |
| **Stock replenishment** | Accepted stock at the plant stays above a stated minimum during operating windows. | A stock sensor exists; the replenishment controller is only an intended System referent. |

Current lot and gate records support gate availability, and the operations coordinator accepts the handover
window. Gate transfer places little provider burden on the foundry while passing transport coordination to the
machining company.

For replenishment, sensor history does not yet establish observation reliability; no finance result supports
retained inventory, and no authorized commitment supplies restoration responsibility. Observation Work,
replenishment Work, access permission, custody, ownership, and restoration commitment remain separate claims.
The candidate remains open for a named observation test and finance decision.

#### SYSE.8:5.2 - Scheduled Delivery and Its Grounds

`Truck-12` is the intended transport bearer. A driver selected under the qualified-driver condition is the
intended Agent for the planned transport Work. The proposed `PlantHandover-and-Acceptance-Lot-27` relation keeps
custody with the foundry until handover at the unloading point. It lets the machining receiver accept only the
identified lot, seal, mass, and visible condition against `LotAcceptanceRule-7`. Under proposed
`DeliveryExceptionRecovery-Lot-27`, the provider dispatcher must arrange a replacement truck within four hours
after a truck failure before handover.

Operations coordinator `OC-4` has performed delivery-assessment Work using the plant's delivery-planning Method.
The resulting `DeliveryScheduleAssessment-Lot-27` uses the current carrier roster, unloading calendar, and ten
recent runs on the same route: nine arrived inside a four-hour window; one truck failure was recovered with a
replacement in three hours. This supports planning for the 08:00–12:00 window and four-hour recovery only for
this route, lot class, season, and current provider roster. It establishes neither future performance nor legal
responsibility. The authorized operations coordinator accepts that schedule.

#### SYSE.8:5.3 - Commercial Comparison and Engineering Return

For schedule-accepted candidates, `CommercialComparisonRule-2` compares quoted buyer payments plus receiving
transport-coordination Work valued at EUR 50 per staff-hour. It selects a candidate only when its advantage
exceeds EUR 100 and records any earlier payment obligation.

| Candidate | Lot quote and payment | Other buyer payment | Receiving Work | Compared total |
| --- | --- | --- | --- | --- |
| Gate transfer | EUR 40,000, due in 30 days | EUR 1,800 haulage, due within 7 days | Eight staff-hours of pickup and exception coordination: EUR 400 | EUR 42,200 |
| Scheduled delivery | EUR 42,000, due in 30 days | None in the stated comparison | One staff-hour of arrival confirmation and handover: EUR 50 | EUR 42,050 |

The EUR 150 advantage exceeds the EUR 100 threshold. Using the schedule assessment, the operations
coordinator's acceptance and the comparison rule, the authorized commercial lead selects scheduled delivery
for this lot and retains gate transfer as fallback. The earlier haulage payment remains visible rather than
being silently treated as equivalent credit. Replenishment remains a possible-future candidate pending its
named observation test and finance decision.

The selection does not assert that transport, handover, acceptance, or recovery Work has occurred. The intended
driver becomes an actual performer only through separately identified Work. Engineers carry the resulting
product, interface, custody, Work, provider, evidence and recovery constraints into use, architecture and
realization decisions. Commercial and operations decisions retain their own authority and evidence. Replacing
these relations with *cast iron as a service* would lose the decision.

For this lot, the alternatives and receiving use are already known. Comparing lot quotations alone would
prefer gate transfer; joining the receiving Work and accepted schedule grounds changes that choice. An existing
procurement and operations account containing these connections would already suffice. A PSS comparison with
the same connections and supplied facts reaches the same result; building another case repository or business
model would need a further decision to justify it.

If the question changes to keeping stock available throughout a season, explore the plant's consumption and
replenishment activities, possible provider partners and the inventory business arrangement. That broader
design work can generate alternatives to the present replenishment proposal. It still leaves the named
observation test, financing and restoration commitment to their responsible practices; a promising blueprint
does not supply those results.


#### SYSE.8:5.4 - A replenishment promise needs money before service acceptance

Now change the foundry case from one delivered lot to keeping the machining plant's accepted stock above an agreed minimum during days 10–60. This is a new receiving use, so the single-lot selection in :5.3 remains valid for its original question. The new proposal needs observation, replenishment and exception response under stated limits on consumption and delivery delay.

The following constructed inputs are supplied for comparing two provider arrangements. They are stipulated engineering, operating and negotiating grounds, not observations of a real provider. Amounts are thousands of euros. The provider has 5 of usable cash after other commitments and must retain 1. The compatible operating account covers routine purchases and replacements; the table shows the additional preparation, opening inventory and observation work that distinguish these proposals. At day 60 the plant resumes its established stock arrangement; the supplied account includes the needed handover and support. The initial schedule assumes timely successful performance and payment, with no other incremental cash flows, taxes or financing charges.

The automatic candidate costs 4 on day 0 to prepare the observation and control system, 6 for inventory on day 10, and 2 for operation on day 45. Its stipulated commissioning method requires the installed stock and plant configuration. The customer offers total payment 12 on day 30, after acceptance of the initial service period. No presently offered finance is drawable before that acceptance. A successful component test would not satisfy either this installed commissioning requirement or the customer's service-acceptance condition.

A qualified operating comparison also supplies a manual candidate for the same bounded stock promise. Preparation and a readiness demonstration cost 3 on day 0, inventory still costs 6 on day 10, and manual observation and response cost 5 on day 45. The specified consumption and delivery limits permit this method; the needed people, observation interval and exception response are included in that account. Its readiness can be demonstrated with existing means before buying the opening inventory. A satisfactory demonstration would support readiness for the bounded manual operation under those conditions; acceptance of the actual service period remains later.

The customer is willing to consider paying 6 on day 7 after that readiness judgement and the remaining 6 on day 30 after service acceptance. This advance transfers exposure to the customer. Its stated negotiating position accepts that exposure only for the demonstrated manual arrangement and the proposed correction or refund terms. The parties must still agree those terms and make the payments. Before commitment, FIN.10 must also establish the cash consequences of the agreed correction or refund obligations in the states where they apply. The successful-performance schedule below leaves that exposure unresolved. There is no corresponding early-payment offer for the automatic candidate.

| Event | Automatic candidate: projected cash | Manual candidate with the proposed advance: projected cash |
| --- | ---: | ---: |
| Opening usable cash | 5 | 5 |
| Day 0: preparation | 5 − 4 = 1 | 5 − 3 = 2 |
| Day 7: conditional advance | 1 | 2 + 6 = 8 |
| Day 10: opening inventory | 1 − 6 = −5 | 8 − 6 = 2 |
| Day 30: remaining customer payment | Not a feasible continuation from the unfunded day-10 action | 2 + 6 = 8 |
| Day 45: operation | Not reached on the supplied funding grounds | 8 − 5 = 3 |

FIN.2 exposes a day-10 need for 6 of additional usable money in the automatic candidate: paying 6 from cash 1 while retaining reserve 1 requires that amount. The later payment of 12 cannot cover that date. For the manual candidate, the forecast retains the reserve at every displayed event, provided readiness, terms and settlement occur as proposed. Its 6 advance is part of the total 12, so the day-30 receipt is only 6.

The engineering return is a conditional manual offering with its observation method, staffing, supported operating limits, early readiness question and later service acceptance. The financial return is its dated conditional coverage. Neither return establishes the other's premises: the cash account does not qualify manual replenishment, and the operating comparison does not create the customer's advance. The useful next work is to obtain the stated readiness judgement and participant agreements, or change the proposal if their conditions cannot be met. The customer can also retain ordinary lot purchasing if it prefers arranging its own stock protection to accepting the new exposure.

This is not a choice of the cheapest isolated component. The manual method has higher continuing work cost, while its different readiness conditions make an earlier payment proposal possible. The parties compare that complete arrangement with obtainable finance for automation, another complete provider offer, a changed service start or refusal. A financial value comparison uses FIN.6 or FIN.9 if the decision needs it; the displayed balances establish only dated payment capacity under the supplied terms.

**Change the readiness date.** Suppose the manual readiness result cannot be obtained until day 14, so the proposed advance cannot settle before then. On day 10, cash would be 2 − 6 = −4. Maintaining the reserve now requires 5 of earlier net funding. Waiting for the unchanged day-14 advance leaves the promised day-10 start unsupported. Obtain a finance arrangement covering that interval, agree a later start with its operating consequences, select another provider arrangement, or decline the start. Preserve the manual method's otherwise adequate technical result; the changed evidence date has invalidated the funding and start conditions.

**Change financing while retaining the automatic design.** Instead, suppose a lender actually offers 6 net before the day-10 inventory payment, independently of service acceptance, for repayment of 7 on day 30. With all other supplied conditions retained, automatic-candidate cash is 1 after preparation, 1 after funding and inventory purchase, 6 after receiving 12 and repaying 7, and 4 after operation. It now meets the reserve without changing the technical concept. FIN.10 compares that financing proposal and its conditions; the engineering decision can retain the automatic arrangement if the whole comparison supports it. The earlier funding failure no longer supplies a reason to prefer manual provision.

If consumption or the permitted response interval changes, obtain the affected operating qualification and return its cost, capability and evidence consequences to the same comparison. A cash forecast for the earlier manual arrangement remains evidence about that earlier arrangement. The decision needs the version that can fulfil the changed stock promise.


### SYSE.8:6 - Bias Annotation

Select candidate distinctions and Methods for the named engineering decision rather than importing a branded
framework as a whole. Sources such as PSS, servitization, service design, SaaS, outcome contracting, or
engineering of shared enabling Systems can contribute bounded alternatives. Reported economic and
environmental gains are configuration-dependent. Academic popularity or official adoption is evidence of
visibility or declared use, not of enacted prevalence or success.

Identify each provider or receiving System from its own basis and name the actual Agent performing each Work
occurrence. Keep neighboring claims separate—for example, claims about ownership, legal duty, capability,
authority, assignment, or a later provider-development decision—even when one System participates in several of
them.

### SYSE.8:7 - Conformance Checklist

| ID | A conforming use... |
| --- | --- |
| `CC-SYSE8-1` | names the client-side use, intended change, receiving Systems, actual System or intended System referent selected for engineering, configuration, horizon and decision; provider engineering retains product-use grounds and its own bounded acceptance. |
| `CC-SYSE8-2` | separates promise content, commitments, permissions, supplied or accessed subjects, Systems, Methods, Work, fulfilment, acceptance, payment, and evidence. |
| `CC-SYSE8-3` | compares materially different offering and provider arrangements, reuses adequate existing results, and develops further candidates or connections only where the decision needs them. |
| `CC-SYSE8-4` | identifies provider and partner Systems, relations, assignments when current, capabilities, interfaces, Work, resources, shared enabling Systems, and recovery. |
| `CC-SYSE8-5` | separates expected Work, result restoration, custody or ownership, and risk exposure from any independently supported responsibility, duty, permission, or authority claim. |
| `CC-SYSE8-6` | connects the selected concept to realization, provider-capability change, configuration, continuing operation, and reopen evidence. |
| `CC-SYSE8-7` | preserves specialist decisions and authority rather than absorbing, for example, strategy, finance, law, organization change, operations, or Platform Engineering. |
| `CC-SYSE8-8` | returns a bounded conditional or selected concept with unsupported claims, evidence needs, receiving decisions, and reopen conditions. |
| `CC-SYSE8-9` | when finance depends on technical acceptance, connects the same configuration, evidence, payment conditions and usable dates; returns changed work and exposure to both the engineering and financial comparisons. |

### SYSE.8:8 - Common Failures and Repairs


| Failure | Symptom | Repair |
| --- | --- | --- |
| Rename and declare victory | A product is called a service or solution with no changed engineering claim. | Recover the promise, subjects, provider arrangement, and decision; stop if none changes. |
| Service-object collapse | Provider, API, promise, Method, Work, ticket, access, product, and result share one referent. | Apply `A.6.P:4.11a`; name each referent and direct relation. |
| Product-only architecture | Technical transfer is designed while continuing provision and recovery are assumed. | Develop provider Systems, capability, Work, interfaces, resources, evidence, and change with the product concept. |
| Provider as organization label | A company or department label is used as if it had identified the actual Agent for every provider Work occurrence. | Recognize the actual Systems and Agents; separate local SystemRole kinds, assignments, capabilities, and Work attribution. |
| Universal PSS recipe | One canvas, maturity ladder, or servitization sequence is made mandatory. | Generate context-relevant alternatives and compare them under the named use and evidence. |
| Guaranteed gain | Recurring revenue, sustainability, loyalty, or market growth is inferred from the arrangement form. | Return the commercial, financial, environmental, and use claims to evidence and specialist decisions. |
| Hidden burden transfer | Automation or self-service reduces provider effort while increasing user Work or excluding cases. | Trace Work, exception handling, affected Systems, and burden under each candidate. |
| Specialist absorption | Systems Engineering invents a neighboring result—for example, a price, legal duty, organization design, operating policy, or Platform Engineering result. | Obtain the specialist result and use it as an input with its authority boundary. |
| Frozen provider | Launch architecture is treated as sufficient for continuing provision. | Record configuration, update, maintenance, partner, migration, recovery, and reopen evidence. |
| Unfunded acceptance | The plan needs money before the technical or acceptance event that permits its release. | Use :4.4 to compare a realizable earlier result, changed terms or another provider arrangement, and retain the exposure of each party. |

### SYSE.8:9 - Consequences

The project can compare arrangements that change the engineered System and provider capability. Promises are
matched to feasible provider arrangements and evidence plans. Technical architecture exposes operational and
organizational dependencies, and specialist results reach the decisions that need them.

The cost is coordination across several practices and maintenance of corresponding descriptions. Viability and
success retain their own evidence and decisions. Record unsupported promise, capability, responsibility, and
evidence claims in the offering-and-provider account so that concept comparison and realization decisions can
branch or stop the candidate before commitment.

### SYSE.8:10 - Rationale

A choice among transfer, access, continuing provision, or responsibility for a result can change both the
engineered subject and the provider arrangement that sustains its use. This pattern connects those design
decisions, using the FPF distinctions at their points of application.



### SYSE.8:11 - SoTA-Echoing

**How much offering and provider design is needed before choosing an arrangement for a bounded use?** The
selected answer is to reuse a sufficient account, repair a consequential missing connection, or expand the
design inquiry when the use or candidate range is unsettled. The :4 entry rule, :4.1 move 4 and :4.2 make that
choice part of the Method.

A serious alternative is richer PSS comparison and design. **Adopt** [Kim (2020), §§2.5.2 and 6.1–6.3](https://www.cambridge.org/core/journals/design-science/article/representation-framework-of-productservice-systems/1DFF0672BB42549F65F07B9247985787)'s
connection between customer activities, actors, value, business models and detailed provision activities.
**Adapt** its selective, iterative use of representation spaces and case analogies: use the parts that can
expose an overlooked arrangement or develop an unfamiliar one. Its comparison of cases helps generate design
choices but does not qualify this project's provider capability or future performance.

**Adopt** [Brambila-Macias, Sakao and Kowalkowski (2018), §4.3](https://doi.org/10.1017/dsj.2018.3)'s attention to
customer networks, hidden coordination costs and organizational flexibility. Moves 5, 6 and 9 apply that
contribution by recovering the work and constraints behind a price or promise. **Reject** quote-only selection
when those consequences can change the receiving decision.

The local synthesis connects these design contributions to scoped evidence, separate specialist authority and
the next engineering decision. In :5, both this account and a PSS comparison containing the same client Work
and schedule grounds select delivery: EUR 42,050 against EUR 42,200. An already adequate account has no missing
connection for this Method to repair. For the fixed lot and known options, further analogy or business-model
development has no demonstrated decision benefit. For the changed question of continuing stock availability,
that exploration can reveal different allocations and provider arrangements.

The trade-off is to maintain the grounds and allocations needed for the bounded choice while
deferring broader opportunity search. Each claim used in the decision still needs applicable support.
Bounding the use too narrowly can hide an alternative; use the richer PSS treatment to reconsider the range
of arrangements. No comparative time saving or industrial performance advantage is established by the worked
arithmetic. Reopen the depth choice when a changed use, overlooked actor or continuing task, or evidence of a
better feasible arrangement defeats the existing account. Reconsider only the affected provider or engineering
claims when a local capability, allocation or evidence condition changes.

The [PPP Reference Guide 3.0, Performance Requirements](https://ppp.worldbank.org/performance-requirements) connects the required service with observation and consequences of failure. Its [Payment Mechanism](https://ppp.worldbank.org/payment-mechanism) treatment connects payment conditions, timing and risk allocation, including financial consequences of underperformance. **Adapt** that connection in :4.4: an engineering result and its evidence can determine which financial event is supportable, while financing can require a changed provider arrangement. The guide's public-project setting supplies neither this private customer's willingness to advance money nor a general preference for outcome payment. The stock case supplies its own constructed terms. Use current applicable professional and institutional grounds for the actual arrangement.


### SYSE.8:12 - Relations

- `A.15.6` supplies the general project-focus and system-of-interest distinctions. `SYSE.1` specializes that
  result for an engineering project; `SYSE.16` supplies the operational use-context account; and `SYSE.17`
  supplies consequence-bearing Systems and unresolved consequences. Compatible current results can be supplied
  directly; the relations do not impose a lifecycle order.
- A `SYSE.8` account supplies only its supported provider-arrangement claims and design constraints to the
  Agents performing linked-concept, realization, or architecture-decision Work. Those Agents apply `SYSE.2` to
  compare linked use and System concepts, `SYSE.3` to develop the recursive realization network, or `SYSE.6` to
  decide the engineered architecture.
- `A.2.3` defines promise content and its acceptance-facing structure. `A.6.P:4.11a` recovers the actual referent
  or relation hidden by *service* or *access* wording. Neither pattern selects a provider arrangement.
- Organization Change Engineering changes provider organization and capability; Operations Management
  coordinates continuing provision; and Platform Engineering changes shared enabling Systems and the Methods
  used to provide or evolve them. Neighboring practices—for example, strategy, commercial analysis, finance,
  law, safety, security, environmental engineering, or governance—retain their own decisions and authority.
- Application profiles retain specialized offering and provider Methods—for example, software, electrical,
  mechanical, building, ship, transport, medical, industrial, or public-sector Methods—when their subjects,
  risks, evidence, or working moves differ.

For conditional finance, FIN.2 supplies dated funding needs and FIN.10 constructs financing terms; FDM.1 and FDM.3 supply unresolved positions and contractual events. ECO.3 and ECO.4 supply exchange construction and complementary commitments. SYSE.8:4.4 returns those results to the offering, technical evidence and provider arrangement; the financial and economic Methods remain external suppliers.

### SYSE.8:End
