## SYSE.12 - Develop or Retain an Engineering Platform for Practitioner Work

> **Status:** Stable

### SYSE.12:0 - Use This When

Use this pattern when engineers cannot reliably model, compute, build, integrate, test, release, or observe an
engineered System because shared enablers—such as tools, data, models, automated or physical facilities, provider
Work, and support arrangements—are treated as incidental infrastructure or as a product with no named
practitioner Work.

Begin with one practitioner Work family and the engineering result it must produce. Identify the actual Systems
that enable or obstruct that Work, the capability practitioners need, the capability claimed for each platform
or provider System, the conditions under which those Systems participate or provide a result, and the burden or
failure that should change. Then choose whether to retain or change the enabling arrangement for that engineering result.

For a decision made before the relying Work, assess platform readiness and record a **platform readiness
assessment** based only on evidence already available. After practitioner Work, the responsible Agent reassesses
the platform and records a **platform-use assessment** based on observed participation, provision, burden, failure,
and engineering results.
Both assessments are epistemes. Each names the System, capability, Work, relation, result and evidence it is
about without replacing any of them, and retains its own evidence cutoff. Later observations can support a
subsequent assessment; they were not grounds used to make the earlier one.

Use `SYSE.25`–`SYSE.29` directly when the missing result is a task-grounded platform improvement, a supported
use path, an interface or contribution change, a qualified control placement, or a migration and retirement
result. The selected service-software Methods in `SYSE.30`–`SYSE.41` supply professional results for build,
feedback, artifacts, environments, data change, deployment, exposure, reliability, recovery, repetitive burden,
and capacity. Use those results to support the relevant platform claims, keeping evidence of pre-use
readiness separate from observations of later use.

Use Organization Change Engineering when positions, assignments, authority, or organization architecture are
the changed subject; Operations Management for continuing queues, support cases, capacity, and provider Work.
When the professional move is not supplied by the common language or the selected service-software Methods,
use a qualified application-profile Method—for example, for a laboratory, compiler, manufacturing cell,
clinical environment, electrical bench, or ship facility. The software selection is not complete software engineering.

#### SYSE.12:0.1 - Terms and Distinctions

| Name in this pattern | What it denotes |
| --- | --- |
| practitioner | An Agent performing the named engineering Work. Capability, assignment, authority, and actual Work remain separate claims. |
| engineering platform | A project-relative designation for an actual System selected to enable named engineering Work through direct relations such as capability, participation, provision, resource, interface, or condition relations. A future candidate remains a referent in a plan or description until an actual System satisfies its identity conditions. |
| provider arrangement | Plain wording for the provider Agents, other Systems, Work, Methods, interfaces, resources, conditions, and recovery relations on which platform use relies. Recover the actual participants and relations; they need not be parts of one platform System. |
| toolchain | Source-local wording that may denote an actual arrangement of tools or a description of that arrangement. Recover the actual Systems, configurations, interfaces, resource relations, participation in Work, and evidence before making a platform claim. |
| self-service | A source-local claim that a practitioner can obtain a stated result without case-specific provider Work at every step. Provider Work, platform participation, support, authority, conditions, and exceptions can still remain. |
| golden path | Source-local wording for either a recommended MethodDescription or a configured arrangement for a bounded case. Recover which one is meant; either remains separate from the world-side Method, its enactment, and evidence that it fits this Work. |
| practitioner-experience account | An episteme carrying evidence-backed claims about, for example, effort, delay, error, rework, recovery, autonomy, or result quality for named Work. A satisfaction result supports only the claim and population it measured. |
| platform readiness assessment and platform-use assessment | The readiness assessment uses evidence available before the relying Work. The use assessment uses later observations of that Work and the platform's actual participation or provision. They are different epistemes with different evidence windows. |

When a source says *service*, recover its claim—for example, a capability, promised result, performed
provision, or participation in Work. Name the holder or participants and supporting evidence. A promise alone
does not establish performed provision.

### SYSE.12:1 - Problem Frame

Engineering results depend on more than the architecture of the project system-of-interest. Systems such as
model repositories, simulation and calculation environments, manufacturing cells, test benches, configuration
and evidence stores, AI assistants, integration environments, and data spaces can change what engineers can
observe and do. Provider and support arrangements can do the same. One platform can help one Work family and
obstruct another.

Buying tools or forming a platform team does not establish that the resulting arrangement can support the named
practitioner Work. Platform engineering starts with that Work and consequences for the project system-of-interest
or its use, then develops the actual enabling arrangement. Platform Work and engineering Work on the project system-of-interest may occur
simultaneously; their dependency is not a lifecycle stage or evidence that one System is part of the other.

### SYSE.12:2 - Problem

A decision about an engineering platform requires answers to seven questions:

1. Which practitioner Agents, Work family, Method, result, configuration, and interval are being served?
2. Which actual Systems, provider Agents, interfaces, resources, and configurations form the current enabling
   arrangement, and which future candidates exist only in plans or descriptions?
3. What capability does the practitioner need, which System holds each claimed platform or provider capability,
   and under what envelope and currentness conditions?
4. Which conditions and direct relations actually matter—for example, access, participation, provision,
   availability, resource use, promise, support, exception, or fallback?
5. Which practitioner or System consequences should change—for example, effort, delay, error, rework, recovery,
   evidence continuity, or a result involving the project system-of-interest?
6. Which credible complete arrangements form the current decision alternatives—for example, retaining, changing,
   composing, obtaining, building, branching, bypassing, or retiring—and who has authority to choose among them?
7. What can be supported before practitioner Work, what is observed only later, and what change reopens each
   assessment?

Without these distinctions, platform teams can optimize adoption, ticket closure, or local automation while
moving integration burden to practitioners, concentrating failure, and degrading the engineering result.

### SYSE.12:3 - Forces

- Shared capabilities and provider Work can reduce duplication, while different engineering profiles need different
  interfaces, evidence, and physical means.
- Case-independent access can shorten feedback, while consequential changes still require separate permission
  and assurance.
- Recommended arrangements can reduce routine burden, while novel Work needs extension, bypass, and exception
  conditions.
- Automation can lower repeated effort, while hidden automation can erase provenance, uncertainty, or recovery.
- Practitioners need stable participation and provision, while Systems designated as project systems-of-interest, Methods,
  descriptions, and evidence demands keep changing.
- A maintained platform needs product care, but platform-local metrics cannot replace practitioner results or
  results involving the project system-of-interest.

### SYSE.12:4 - Solution

Choose an enabling arrangement for one named practitioner Work result, including retaining the current arrangement
when its use is supported. Develop only the selected changes. State the capability, conditions, participation or
provision relations, and evidence separately, then reassess the platform from observed use.

#### SYSE.12:4.1 - Perform the Move

1. **Name practitioner Work and result.** State the practitioner Agents or inclusion rule, Work family, Method,
   subject, expected result, current configuration, interval, and receiving decision.
2. **Recover the current enabling arrangement.** Identify actual Systems—such as tools, model or data stores,
   compute resources, AI assistants, laboratories, manufacturing cells, integration environments, evidence
   stores, or support Systems—only where their relations change the Work. Name provider Agents, interfaces,
   resources, conditions, and failures.
3. **Separate capability holders.** State the capability demanded of practitioners and the holder, Work family,
   envelope, measures, qualification window, currentness, and evidence for each platform or provider capability.
   Support each capability claim with evidence that bears on the named holder performing the Work family in
   that envelope. Administrative or descriptive records count only when their evidence relation supports that
   claim.
4. **State conditions and direct relations.** Name the conditions that bound the claim—for example, access,
   configuration, performance, evidence continuity, support, exception, fallback, cost, or resource conditions.
   Then state each direct relation used by the decision: platform participation in Work; production of a named result by a named Work occurrence; supply of the result or access to it from a named provider to a named receiver; receipt or use by that receiver; resource availability or use; applicable promise content; or another governed relation.
5. **Use Method repertoire and architecture when they change the choice.** A compatible `SYSE.15` result can
   supply available Methods and applicability limits; a compatible `SYSE.20` result can supply Method, Work,
   enablement, and conflict structures. Otherwise use a qualified source or name the missing result.
6. **Generate and choose among real alternatives.** Build a `C.11` option set from feasible complete
   arrangements. Candidates may retain the current arrangement, change a capability or relation, compose existing
   Systems, obtain or build a part, branch for a profile, preserve a bypass, or retire a harmful arrangement. Name
   the deciding Agent, authority, accepted losses, and questions outside that authority. Compare them for the
   same practitioner result and period of reliance, including continuing provider, maintenance, and recovery
   Work as well as practitioner effort. Use `SYSE.24` when the obtaining comparison is unresolved and `SYSE.25`
   when the improvement mechanism needs investigation.
7. **Perform selected platform-development Work.** When step 6 selects a change, record the performing Agents,
   assignments when relevant, Methods, temporal extents, results, actual transformations, resulting configuration,
   and evidence. A decision record does not change the platform. When the current arrangement is retained,
   continue to the readiness or use assessment that the receiving decision needs without creating development Work.
8. **Issue the pre-use readiness assessment.** State only capability and condition claims supported before the
   practitioner Work, with their evidence cutoff, currentness window, limits, fallback, and stop.
9. **Observe use and issue a later assessment.** Identify the practitioner Work occurrence and the actual
   platform participation, provision Work, or resource relation. Observe the consequences needed by the
   decision—for example, burden, delay, error, rework, recovery, evidence continuity, or results involving the
   project system-of-interest. Record the later assessment separately and use it only for later decisions.
10. **Return and reopen locally.** Supply only the supported claims needed by each receiving decision—for
    example, capability, condition, participation, provision, use, failure, or platform-change claims. Reconsider only
    the claims affected by a changed Work, Method, practitioner population, configuration, provider, condition,
    evidence basis, or consequence for the project system-of-interest.

Platform development, practitioner Work, support, change of the project system-of-interest, and evidence Work
can overlap. Every claimed use still needs an obtaining relation, and later evidence cannot justify earlier
reliance retroactively.

#### SYSE.12:4.2 - Record the Result

| Field | Required content |
| --- | --- |
| practitioner use | Agents or population, Work family, Method, subject, result, configuration, interval, and receiving decision. |
| platform and providers | Actual platform System and selected parts, provider Agents and Systems, interfaces, resources, configurations, and future candidates kept as plan or description content. |
| capabilities | Practitioner capability demands and each platform or provider capability holder, Work family, envelope, measures, qualification window, currentness, and evidence. |
| conditions and relations | Conditions used by the case, such as access, performance, evidence continuity, support, exception, fallback, cost, or resource conditions; each relied-on participation, provision, availability, resource-use, promise, or other governed relation. |
| alternatives and change | Current `C.11` OptionSet of complete arrangements; deciding Agent, authority, accepted losses, selected option; platform-development Work, transformation, and resulting configuration when a change is performed; and the evidence supporting the retained or changed arrangement. |
| pre-use readiness | Claims supported before practitioner Work, evidence cutoff, currentness window, limits, fallback, and stop. |
| observed use | Practitioner Work, actual participation or provision, burden and result observations, later assessment identity, and the decision it can change. |
| return and reopen | Claims supplied to each receiving decision, their limits, and the change that reopens each one. |

#### SYSE.12:4.3 - What Changes in Practice

Platform investment begins with an engineering result and observable practitioner Work. Engineers can improve a shared enabling System while keeping capability, Work, participation,
evidence, operations, organization change, administration, application-profile engineering, and decisions
about the project system-of-interest distinct.

### SYSE.12:5 - Worked Case: Platform Support for Flood-Pump Integration

Engineers integrating a flood-pump controller must reconcile identifiers among the model build,
hardware-in-the-loop bench, controller configuration, and evidence repository by hand. One missed link delays
the station integration result and makes recovery difficult.

The actual engineering platform includes the model-build System, bench, and evidence repository in configuration
C4. A support Agent provides recovery Work but is not made a part of the platform merely by supporting it. A
platform description records the structure; it is not the platform System.

For the next controller-integration campaign, each candidate must return evidence tied to the same model,
controller and bench configurations, preserve access to that evidence, and permit recovery after an interrupted
assembly. The competent incumbent records and checks the correspondence manually. It can still produce the
required result; the observed missed link and repeated copying across revisions are reasons to compare a repair.

The engineers compare retaining that arrangement, strengthening its manual correspondence check, adding
configuration-and-evidence links, replacing the bench, and obtaining bounded evidence-provision Work from
another provider. Strengthening the manual check avoids maintaining new bindings but leaves reconciliation in
each attempt. The linking option carries identifiers from their originating configurations into the assembled
evidence; it removes repeated copying but requires a provider to maintain the bindings when formats or
configurations change. Bench replacement would require requalification; no identified bench limitation makes
that work necessary for this repair.
Outside provision is competitive only if it returns the same configuration-linked evidence with the required
access and recovery; otherwise the engineers still perform the join. Manual fallback remains part of the
linking option.

The authorized Agent chooses the bounded linking change because revisions recur during this campaign and
preserving correspondence at evidence creation addresses the observed failure. The Agent accepts continuing
binding-maintenance and recovery Work. Retaining the manual arrangement could be preferable for an infrequent
job with adequate checks and support. This choice predicts a useful repair; its total burden advantage remains
to be assessed.

A platform-engineering team configures identifier bindings, repository links, and recovery hooks. This dated Work
is distinct from the actual transformation of the continuing platform from C4 to C5 and from the evidence that
describes the change. A support Agent then performs a recovery exercise.

The readiness assessment, issued after the exercise and before controller integration, states that:

- C5 is current;
- the bench and repository are available in their named configurations;
- the configuration-and-evidence links passed the checks already performed;
- the manual fallback remains executable; and
- automated repository export remains unsupported and blocks only Work that needs automated export recovery.

During later controller-integration and flood-discharge trial Work, engineer Agents use the C5 platform while
its model-build, bench, and evidence-store Systems provide their named functions. The observed relations support
platform participation in those Work occurrences; they do not assign the engineers' Work to the equipment. The
supplier's fixture-fabrication Work uses another arrangement, so the same participation claim does not apply
there.

The later use assessment records that the engineers' evidence-assembly effort for controller integration fell
from the stated local baseline of six person-hours to two and a half, while a repository outage took 45 minutes
to recover and the export gap remained. The provider's continuing binding-maintenance effort has not yet been
measured on the same basis. Thus the observations support the local assembly saving, not a claim that total
Work fell. Assess that claim using comparable provider and practitioner Work over the selected campaign; the
45-minute outage duration alone is not a measure of recovery effort.

If obtaining those observations is not worth its cost for the next decision, leave the total-burden claim open
and decide from the supported result and accepted maintenance obligation. A later finding that provider Work
outweighs the assembly saving reopens the improvement claim; it does not erase the verified links or completed
integration. These constructed observations support only this case and can change later platform decisions.
They cannot retroactively justify the earlier controller-integration reliance.

**Countercase.** A repository and continuous-integration server are installed, but no practitioner Work,
participation, provision, or engineering result is observed. Record the installed Systems and the proposed
enabling arrangement; do not infer platform capability or adoption from installation.

### SYSE.12:6 - Bias Annotation

Software platform practice supplies useful ideas about self-service, configured defaults, fast feedback, and
product care. Vendor catalogues and team-topology literature can also make a tool or team appear to be the whole
platform. Physical and cross-domain engineering adds other platform participants—for example, laboratories,
manufacturing cells, configuration and calibration Systems, evidence stores, provider Work, and recovery
arrangements.

Use publicity, university coverage, procurement, installation, usage counts, or satisfaction as evidence only for
the claims each can support. When broad prevalence or causal effect cannot be measured affordably, use
the best available case evidence and state its epistemic status.

### SYSE.12:7 - Conformance Checklist

- [ ] Practitioner Agents or population, Work, Method, result, configuration, interval, and receiving decision are
      named.
- [ ] Source-local *service* wording is interpreted for the claim being made, such as capability, provision,
      or participation.
- [ ] Capability holders and envelopes are supported, and each direct relation states its participants and
      conditions.
- [ ] Alternatives include retaining the current arrangement, a bounded change, a branch or bypass, and stopping
      or retiring where credible; authority and accepted losses are explicit.
- [ ] Platform-development Work, actual transformation, resulting configuration, and evidence remain distinct.
- [ ] A readiness assessment uses only evidence available before practitioner Work.
- [ ] A later use assessment identifies actual participation or provision and cannot justify the earlier reliance
      retroactively.
- [ ] Practitioner burden, recovery, evidence continuity, and results involving the project system-of-interest
      can reopen the affected platform claims.

### SYSE.12:8 - Common Failures and Repairs

| Failure | Repair |
| --- | --- |
| Treat a tool list as the platform | Identify actual Systems, selected structure, capability holders, interfaces, resources, configurations, and participation or provision relations. |
| Treat a platform team as the platform System | Identify the Agent performing platform Work and the changed enabling System separately. |
| Treat availability as use | Identify the practitioner Work occurrence and the obtaining platform-participation or provider-work relation with dated evidence. |
| Use later evidence to justify earlier reliance | Keep the pre-use readiness assessment and later use assessment separate, with their evidence windows and update relation. |
| Treat satisfaction or adoption as engineering value | Observe the practitioner and project-system consequences that matter to the decision, such as effort, delay, error, rework, recovery, evidence continuity, or an engineering result. |
| Treat a golden path as the Method | Separate MethodDescription, world-side Method, enactment, fit evidence, and bypass conditions. |
| Let the platform provider decide matters outside its authority | Return each decision—such as practitioner assignment, release of the project system-of-interest, assurance, organization, or operations—to the Agent authorized for it. |

### SYSE.12:9 - Consequences

This move exposes hidden enabling dependencies and practitioner burden and can reduce repeated integration and
evidence Work. It also adds continuing Work to maintain, support, configure, observe, and recover the platform.
Shared capabilities can also create coupling, provider monopoly, or failure concentration, so profile branches
and fallbacks preserve alternatives where those risks matter.

### SYSE.12:10 - Rationale

Engineering capability is a holder's ability to perform a named Work family or produce a result class within a
declared envelope, measure set, qualification window, and currentness condition. A chosen Method may constrain
that envelope or be tested for fit, but it is not the capability's target. A platform is useful only through
actual relations to practitioner Work. Engineers can make and assess claims about the platform's architecture,
configuration, evidence, use, and evolution for that Work.

### SYSE.12:11 - SoTA and Source Use

**Which enabling arrangement should support this engineering Work, and what justifies retaining or changing it?**
For ordinary internal software provision, the DORA/CNCF approach of developing a platform around users' tasks
is a sufficient starting answer when its provider capabilities and supported use already cover the Work.
It develops a small useful offering with users, composes existing provision, and learns from task outcomes.
Adopt that answer within its conditions.

For Work spanning software tools, physical facilities and separately performed provider Work, this pattern
selects an authored synthesis: carry that task-oriented development into the actual enabling arrangement,
qualify each relied-on capability and relation, and separate readiness before use from later observations.
Its gain is a supported decision about which Work the arrangement can enable: a bench, repository and support
provider can contribute different qualified results, and a missing export or changed maintenance burden
reopens only dependent claims.
The accepted cost is identifying those dependencies and maintaining their qualifications. This is a
constructive answer for mixed engineering Work, not evidence that it outperforms qualified direct provision.

The serious local alternative is to retain competent provision or repair its manual interaction without
developing a shared platform capability. It avoids new binding, interface and support obligations and can win
for infrequent or highly variable Work. The synthesis earns its added effort when repeated coordination or
cross-provider dependencies change the relying decision. If the direct source treatment or incumbent already
carries those distinctions adequately, reuse it.

| Source and comparison role | Disposition and practical consequence | Limit |
| --- | --- | --- |
| DORA, [Platform engineering capability guide](https://dora.dev/capabilities/platform-engineering/), updated 12 January 2026; “How to implement quality internal platforms,” especially “Design for extensibility.” A direct software-practice candidate. | **Adopt** task-oriented product development, a minimum useful offering, clear task feedback and extensibility. This selects the narrow improvement and supported interaction reached through `SYSE.25–SYSE.26`; extensibility returns to `SYSE.27`'s interface and contribution work. | Guidance for internal software platforms does not qualify a laboratory or manufacturing Method. |
| [CNCF Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/), “What is a platform,” “Attributes of platforms,” “Attributes of platform teams,” and “Enabling platform teams.” A provider-composition candidate. | **Adopt** a thin, composable offering over capable providers and supported user entry. **Adapt** the division of provision in :4.1 steps 2–4: the pump bench, repository and recovery Agent remain identifiable contributors. | The cloud-native arrangement is a supported alternative, not a required organization for every engineering profile. |
| DORA, [State of AI-assisted Software Development](https://dora.dev/research/2025/dora-report/), v2025.2, platform chapter pp. 66–72 and methodology pp. 113–131, with the [p. 70 correction](https://dora.dev/research/2025/errata/). Evidence limiting a one-sided benefit claim. | **Adopt** the need to examine task experience alongside delivery instability; **reject** an inference of universal causal benefit from the reported associations. This supports :4.1 step 9 and the separate burden/recovery observations in :5. | Survey and qualitative evidence does not compare all engineering arrangements or establish a cross-domain platform organization. |
| Tolio, Monostori, Váncza and Sauer, [Platform-based manufacturing](https://doi.org/10.1016/j.cirp.2023.04.091), CIRP Annals 72(2) (2023), 697–723; §§1–2.3, 6.1.1 and 6.3.1–6.3.3. A manufacturing alternative and transfer limit. | **Adapt** its different provider/participant arrangements, input-interpretation burden, traceability and data-use conditions into the alternatives in :4.1 step 6. In :5, outside provision must return usable, configuration-linked evidence; intermediation alone does not supply that result. | Standardized input can exclude needed variation. A manufacturing network does not supply the professional Method or qualification of each physical operation. |

In :4.1 step 6, this means comparing complete arrangements for the same result and period, including continuing
provider Work. The case in :5 selects identifier links while accepting their maintenance obligation and keeps
a measured practitioner saving separate from an unmeasured total-burden claim. `SYSE.24` supplies the
obtaining comparison; this pattern joins its result to capability, participation and evidence timing.

Reopen the affected choice when a changed input or provider breaks the relied-on correspondence or access,
when comparable continuing burden reverses the accepted trade-off, or when a supported alternative supplies
the same result with fewer obligations. Reopen the cross-profile synthesis only when a new use or comparative
source defeats the particular dependency or evidence distinction being carried across profiles.

### SYSE.12:12 - Relations

- `SYSE.25`–`SYSE.29` construct the bounded improvement, supported interaction, interface/contribution change,
  control placement, and migration results named above. Enter the Method for the missing result.
- `SYSE.30`–`SYSE.41` supply the selected service-software professional Methods. Apply each result to the
  platform capability and practitioner task for which its conditions and evidence hold.
- `SYSE.8` supplies a providing-System concept when missing; `SYSE.18` handles integration across independent
  decisions; `SYSE.24` compares whole obtaining arrangements.

- A compatible `SYSE.15` result supplies a bounded Method repertoire and applicability limits; it neither selects
  nor enacts the platform Method.
- A compatible `SYSE.20` result supplies Method, Work, enablement, and conflict structures; it neither turns an
  enabling dependency into a level nor selects the platform change.
- `A.2.2` governs holder-dependent capability. `A.6.P:4.11a` recovers *service* wording into promise, capability,
  bearer, dated Work, participation or provision relation, condition, and evidence claims without creating a
  generic service object.
- `A.15.1`, `A.2.1`, and `A.3.1` distinguish Work, assignment, and enacted Method. `A.3.4` distinguishes actual
  transformation, `A.15.PROD` claimed result production, and `A.22` descriptions of selected platform structure.
- `SYSE.11` may use a readiness assessment only for capability, conditions, and participation or provision
  claims supported before its Work. A later use assessment supplies grounds for subsequent decisions;
  judge the earlier reliance against the grounds available when it occurred.
- Neighboring DPFs retain their own Methods and decisions. These include Organization Change, Operations,
  Administration, application-profile engineering, security, safety, law, finance, procurement, and governance
  whenever the current question belongs there.

### SYSE.12:End
