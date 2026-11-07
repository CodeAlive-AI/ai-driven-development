## CUST.3 - Develop a Repeatable Offering Family

> **Type:** Method pattern
> **Status:** Stable

### CUST.3:1 - Problem frame

Use this method when several local solutions suggest a common contribution, when a current family has accumulated exceptions, or when a new offering needs a deliberate range of variation. The input may be completed cases, qualified component results or explicit prospective cases; their evidence status must remain distinguishable.

The first move is to compare the result and the conditions that make it obtainable, then propose what must remain invariant and what may vary. A list of similar requests or a shared codebase does not construct that family.

Keep a one-off solution local when there is no useful, supported common contribution. A known adequate family can be used directly through CUST.4.

### CUST.3:2 - Problem

A local solution contains necessary constraints mixed with accidental arrangements. Copying it exports accidents; abstracting it too quickly removes conditions that made it work. A common technical part can coexist with different service obligations, while different technical implementations can provide one repeatable service. The family must explain these distinctions before its members are admitted.

### CUST.3:3 - Forces

| Tension | Construction choice |
| --- | --- |
| Common preparation and distinctive value | Which elements can be shared without losing the result customers need. |
| Broad applicability and supportable variation | Whether a parameter, branch, extension or separate family is justified. |
| Early investment and uncertain repetition | Whether to develop a platform now or consolidate sufficient local results later. |
| Technical transfer and permitted use | Which source materials and derived contributions may serve the next purpose. |
| Common release and installed obligations | Whether a proposed invariant can be introduced without abandoning existing members. |

### CUST.3:4 - Solution

#### CUST.3:4.1 - Establish the result the family is meant to serve

State the receiving result in terms that survive a change of implementation. For an analytical service, this might be a defensible eligibility decision from supplied records, not “the same dashboard everywhere.” State who uses it, the operating interval, required quality and the limits beyond which another offering is needed.

Choose cases that expose consequential variation: different inputs, operating environments, levels of recipient capability, support arrangements or acceptance conditions. Include a boundary case that might not belong. Similar sector or customer size can help locate candidates but does not prove commonality.

Do not require an arbitrary number of sales. A qualified design basis can support a prospective family; multiple unexamined deployments can fail to do so. Mark which claims rest on observation, analysis or an untested proposal.

#### CUST.3:4.2 - Recover the common causal and operating basis

Compare how each case obtains its result. Identify the common useful function, the work needed to perform it, and the information and capabilities that work requires. Then recover the conditions on which the function depends. Remove local names only after the meaningful role is clear.

For example, two deployments both “validate access,” but one checks a monthly file before analysis and another makes a live authorization decision. A shared phrase does not make their timing, failure handling or evidence interchangeable. They may share a narrower operation while needing different offerings.

Build an initial account of the invariants: what must remain true for all proposed members. Include meaningful input conditions, required operations, acceptance, support and continuing responsibilities where they determine the result. Explain why each invariant matters. “All members use component X” is weak if a replacement could preserve the function; “all accepted records have an interpretable eligibility status under the agreed policy” states the needed condition.

#### CUST.3:4.3 - Construct variations and choose their home

For each observed or proposed difference, ask whether it changes only a value, selects an already understood alternative, changes an interface, requires a different method or defeats the common result. Choose the smallest form that preserves the needed distinction.

| Proposed form | Construct it by | Return or rejection condition |
| --- | --- | --- |
| Parameter or configuration | Define allowable values, their meaning and effects on other choices. | A permitted value changes the obtaining method or invalidates another condition. |
| Adapter or extension | State the stable receiving interface, which inputs or outputs need conversion, what each conversion must preserve, and who maintains the adapter or extension. | The extension changes an assumed invariant or requires unsupported access. |
| Separate supported profile | Name the distinct combination of assumptions, execution and support. | Profiles share only a label and no useful common basis. |
| Common component | Extract a function with qualified interfaces and replaceable local inputs. | Useful operation depends on unrepresented local judgement. |
| Repeatable service method | Explain the work, preparation, choices, help and acceptance that transfer. | Repetition still requires hidden invention or unavailable specialist effort. |
| Local residue | Bound the case, obligation and reason for not generalizing it. | The residue repeatedly changes the shared basis and is no longer isolated. |

Compare both directions of development. A top-down family starts from a deliberate platform or common service design and derives permitted members. A bottom-up family extracts a useful common basis from differing local solutions. Neither direction is inherently superior. Use the first when the expected variation and shared investment are sufficiently understood; use the second when actual differences are still teaching you what is common. They can meet as a prospective design is corrected by deployment evidence.

When later engineering change, platform development or interface evolution is the live technical problem, obtain the complete result from [SYSE.23 — Choose What to Change So Later System Changes Become Easier](../../engineering-dpf-suite/syse/37-syse-23---choose-what-to-change-so-later-system-changes-beco.md), [SYSE.25 — Decide Whether and How to Improve a Platform from Practitioner-Task Evidence](../../engineering-dpf-suite/syse/45-syse-25---decide-whether-and-how-to-improve-a-platform-from.md), [SYSE.26 — Design a Supported Platform-Use Path](../../engineering-dpf-suite/syse/46-syse-26---design-a-supported-platform-use-path.md) or [SYSE.27 — Evolve Platform Interfaces and Contribution Paths](../../engineering-dpf-suite/syse/47-syse-27---evolve-platform-interfaces-and-contribution-paths.md). Bring back the actual supported function, interface, use path and change restrictions. CUST places those results within an offering family; it does not replace the engineering design.

#### CUST.3:4.4 - Build a member and a boundary, not only a schema

Take a proposed member and assemble it from the common basis plus the selected variations. Follow input preparation, operation, delivery, acceptance and support. Explain any conversion between supplier results and the receiving work. If “use the common module” leaves someone to invent a local procedure, either develop that procedure as a variation or retain the case outside the family.

Now change a consequential condition. Determine whether the member adapts by an allowed choice, needs requalification or leaves the family. This gives the variation rule operational meaning. A configuration table without this construction can admit combinations nobody can deliver.

Construct exclusions positively: explain what condition fails and what alternative remains. “Disconnected sites require a separately qualified synchronization and support method” is useful. “Unsupported configuration” alone is not an adequate return for the customer or field team.

#### CUST.3:4.5 - Separate what can transfer from what may transfer

Identify the materials and knowledge proposed for reuse, the next recipient and the purpose. Permission to perform local work, access information, learn from a case, disclose an example and redistribute an artifact can differ. Obtain the applicable result through [MKT.12 — Investigate a Customer or Market Question for a Decision](../mkt/27-mkt-12---investigate-a-customer-or-market-question-for-a-dec.md) and [MKT.14 — Develop and Change a Programme for Selected Customer Organisations](../mkt/29-mkt-14---develop-and-change-a-programme-for-selected-custome.md), including their permitted-use and local-material conditions. Obtain specialist advice where the right or obligation depends on it.

Construct the common contribution from permitted inputs. Options include a separately agreed use, a narrower explanation, independently obtained examples or another allowed component. Removing customer names or calling derived data synthetic does not alone establish that the receiving use is allowed.

If permission or an adequate replacement is absent, preserve the local result and stop that transfer. If a replacement changes the evidence basis, repeat the affected qualification.

#### CUST.3:4.6 - Make provision part of the family

For each member class, identify who can choose it, perform delivery, obtain help, accept the result and maintain the common and local parts. A technically reusable primitive can be one input; a supported offering also needs the work required to obtain its result.

Use CUST.6 to develop and transfer that work. Use CUST.7 to compare common preparation, local adaptation, variation qualification, support and changes over the relevant horizon. A broader family can save setup while increasing interaction testing and support. Include that possibility before admitting the breadth.

For a changed delivery or outcome model, receive the integrated concept from [SYSE.8 — Develop an Integrated Offering and Provider Concept for Using an Engineered Result](../../engineering-dpf-suite/syse/29-syse-8---develop-an-integrated-offering-and-provider-concept.md) where its engineered-result conditions fit. Carry responsibility, evidence and risk boundaries into the proposed members. A family of technical configurations does not automatically support a family of outcome guarantees.

#### CUST.3:4.7 - Decide what becomes supported and keep the reason revisable

Admit the common contribution only when its result, applicable members, variations, provision, permissions and ongoing responsibilities fit together. The decision can instead require a narrower family, a separately funded investigation, a local service or no change.

Identify the common owner and any local owner by their actual responsibility, not merely repository access. Give future users enough explanation to recognize membership and return an exception. CUST.4 provides the choice method and CUST.8 the change method.

When a case challenges the family, decide whether it exposes a local error, an omitted variation, a failed invariant or a mistaken general rule. Revise only the affected scope. Preserve existing supported members and their obligations while a broader claim is reconsidered.

### CUST.3:5 - Archetypal Grounding

The analytical provider compares three explicitly described uses. One customer supplies a monthly batch; a second has the same decision cycle but requires private hosting; a third needs an immediate decision while disconnected.

The common result is a defensible monthly eligibility answer from records interpreted under an agreed policy. The proposed invariants are an explicit status meaning, a qualified input mapping, evidence of the monthly computation and an obtainable correction route. Hosting is a variation only if monitoring, updates and support remain achievable. The report layout is local and does not change the common computation.

The provider constructs two members: hosted batch service and supported private batch service. Both use the same eligibility operation, but their deployment and support procedures differ. The private member includes scheduled access and a named escalation route. The disconnected immediate-decision case fails both the timing and obtaining assumptions. It is not admitted by adding a “disconnected=true” parameter.

A common primitive is extracted as the eligibility operation with explicit input meaning and output basis. A deployment method, not another primitive, carries preparation and private-site setup. A local report service remains separately funded. The offering family combines these different types of contribution.

Change the condition: customer samples used to establish the private profile cannot be distributed. The provider may use a qualified permitted explanation and independently obtained examples, then test the profile again. Without that basis the local deployment may remain valid while the proposed common package remains unavailable.

For a physical test-bench family, a common base and interchangeable measurement modules offer another construction. Connector fit does not prove measurement compatibility. A new module combination needs the corresponding calibration and technical qualification before it becomes an offering member.

### CUST.3:6 - Bias-Annotation

Family construction can favor the provider's convenience over meaningful customer differences. Test invariants against the intended result, not only common implementation. Conversely, customer-specific wording can conceal a useful common method.

### CUST.3:7 - Conformance Checklist

- Is the shared result defined independently of one convenient artifact?
- Are invariants justified by the useful results and the conditions for obtaining them?
- Are permitted variations and their interactions explained?
- Can a member be constructed and a nearby excluded case recognized?
- Are technical and permission conditions both satisfied for the proposed reuse?
- Are delivery, assistance, support and change responsibilities obtainable?
- Can a narrower family or local residue be selected without treating it as failed productization?

### CUST.3:8 - Common Anti-Patterns and How to Avoid Them

**Commonality by request count.** Compare the result and the conditions for obtaining it; repeated wording is not a family.

**Everything becomes a parameter.** Use a separate profile or method where the operation changes, and exclude combinations whose conditions do not fit.

**The primitive is the offering.** Add the delivery, acceptance and continuing responsibilities needed to provide it.

**Admission fields instead of construction.** Build a member, a changed-condition case and a support arrangement before judging admission.

### CUST.3:9 - Consequences

The method produces an offering family that can guide selection, delivery and change. It can reduce repeated invention while preserving meaningful differences.

It also creates a maintenance responsibility: invariants, variations and receiving methods must remain aligned. A narrower family may have greater practical value than a broad family with expensive qualification and uncertain support.

### CUST.3:10 - Architectural Rationale

The family is defined through common useful result and compatible provision, not one universal implementation layer. This allows technical components, service methods and local contributions to remain distinct while supporting the same customer use.

Constructing before qualifying makes the admission decision inspectable. Retaining local residue prevents the family from becoming a disguised catalogue of every historical customization.

### CUST.3:11 - SoTA-Echoing

Simpson, Siddique and Jiao's platform-development account supplies the useful top-down/bottom-up distinction and the commonality/differentiation trade-off. Salvador, de Holan and Piller supply solution-space development as a capability alongside process robustness and choice navigation. These are historical grounds for the construction.

The service-productization line adds that common provision can consist of a defined service and operating method rather than a manufactured component. CUST adopts that breadth and adds explicit permission, continuing obligation and local-residue decisions. The primary abstract of Bakås and colleagues' solution-space framework supports iterative frontend/backend learning.

Compared with a feature catalogue or a gate checklist, this combination changes the work: construct invariants, variations, a member and an exclusion before admission. Reopen the family method when its assumptions fail in an unlike service or when a qualified domain method supplies a better construction.

### CUST.3:12 - Relations

CUST.2 supplies explained differences, but CUST.3 can start from independently obtained cases. CUST.4 uses the admitted solution space; CUST.5 tests consequential unknowns; CUST.6 constructs repeatable provision; CUST.7 supplies the full resource comparison; CUST.8 governs changes affecting present members.

Use the results from the cited engineering and marketing Methods within their professional conditions when constructing the family.

### CUST.3:End
