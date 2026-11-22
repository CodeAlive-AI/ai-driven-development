## SYSE.12 - Develop or Retain an Engineering Platform for Practitioner Work

> **Status:** Stable

### SYSE.12:0 - Use This When

Use this pattern when a decision about an engineering result depends on the shared Systems and support that practitioners need to model, compute,
build, integrate, test, release or observe the engineered System. Common problems include treating tools, data, models, automated or physical
facilities, provider Work and support arrangements as incidental infrastructure, or developing them as a product with no named
practitioner Work.

Begin with the receiving decision and the practitioner work it must support. For one job, establish the result, available help and relevant conditions for that job. For a shared platform, identify which work can occur together, which tasks may compete, and which services or results are reusable. Choose the systems, provider work and distinctions in the demand model that can alter what practitioners can do by the required time. A readiness or actual-use question can finish without a redesign.

For a decision before the relying Work, use or prepare a **platform readiness assessment**
based on the evidence available at that time. For a later decision about use, the responsible
Agent uses or prepares a **platform-use assessment** from observations of participation,
provision, burden,
engineering results and any failures. These assessments are epistemes about the
System, capability, Work, relation, result and evidence. Each keeps its own evidence cutoff.
Later observations can inform a subsequent decision.

Use `SYSE.25`–`SYSE.29` directly when the missing result is a task-grounded platform improvement, a supported
use path, an interface or contribution change, a qualified control placement, or a migration and retirement
result. The selected service-software Methods in `SYSE.30`–`SYSE.41` supply professional results for build,
feedback, artifacts, environments, data change, deployment, exposure, reliability, recovery, repetitive burden,
and capacity. Use those results to support the relevant platform claims, keeping evidence of pre-use
readiness separate from observations of later use.

Use Organization Change Engineering when positions, assignments, authority or organization architecture are the
changed subject, and Operations Management for continuing queues, support cases, capacity and provider Work. Where
the common language and selected service-software Methods leave a professional task uncovered, use a qualified
application-profile Method, for example for a laboratory, compiler, manufacturing cell, clinical environment,
electrical bench or ship facility. For other software engineering tasks, obtain the professional contribution the project needs.

#### SYSE.12:0.1 - Terms and Distinctions

| Name in this pattern | What it denotes |
| --- | --- |
| practitioner | An Agent performing the named engineering Work. Capability, assignment, authority, and actual Work remain separate claims. |
| engineering platform | A project-relative designation for an actual System selected to enable named engineering Work through direct relations such as capability, participation, provision, resource, interface, or condition relations. A future candidate remains a referent in a plan or description until an actual System satisfies its identity conditions. |
| provider arrangement | Plain wording for the provider Agents, other Systems, Work, Methods, interfaces, resources, conditions, and recovery relations on which platform use relies. Recover the actual participants and relations; they need not be parts of one platform System. |
| toolchain | Source-local wording that may denote an actual arrangement of tools or a description of that arrangement. Recover the actual Systems, configurations, interfaces, resource relations, participation in Work, and evidence before making a platform claim. |
| self-service | A source-local claim that a practitioner can obtain a stated result without case-specific provider Work at every step. Provider Work, platform participation, support, authority, conditions, and exceptions can remain. |
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

Buying tools or forming a platform team does not establish that the arrangement can support the named practitioner
Work. Start from that Work and its consequences for the project system-of-interest or its use. Retain a sufficient
enabling arrangement or develop the change the decision calls for. Platform Work and engineering Work on the project system-of-interest
may overlap. Their dependency alone establishes neither a lifecycle stage nor a part–whole relation.

### SYSE.12:2 - Problem

Use the following questions to establish what the platform must support and what the commissioning practitioner needs to decide.

1. Which practitioner Agents, Work family, Method, result, configuration, and interval are being served?
2. Which actual Systems, provider Agents, interfaces, resources, and configurations form the current enabling
   arrangement, and which future candidates exist only in plans or descriptions?
3. What capability does the practitioner need, which System holds each claimed platform or provider capability,
   and under what envelope and currentness conditions?
4. Which conditions and direct relations matter—for example, access, participation, provision,
   availability, resource use, promise, support, exception, or fallback?
5. Which consequences for practitioners or the System matter to the choice, and which should be preserved or changed? Consider effort, delay, error,
   rework, recovery, evidence continuity or a result involving the project system-of-interest.
6. When a choice of platform arrangement is due, which credible alternatives serve the required work and who may choose among them? Consider retaining, changing, composing, obtaining, building, branching, bypassing or retiring an arrangement as appropriate.
7. What can be supported before practitioner Work, what is observed only later, and what change reopens each
   assessment?

Without these distinctions, platform teams can optimize adoption, ticket closure, or local automation while
moving integration burden to practitioners, concentrating failure, and degrading the engineering result.

### SYSE.12:3 - Forces

- Shared capabilities and provider Work can reduce duplication, while different engineering profiles need different
  interfaces, evidence, and physical means.
- Case-independent access can shorten feedback, while consequential changes require separate permission
  and assurance.
- Recommended arrangements can reduce routine burden, while novel Work needs extension, bypass, and exception
  conditions.
- Automation can lower repeated effort, while hidden automation can erase provenance, uncertainty, or recovery.
- Practitioners need stable participation and provision, while Systems designated as project systems-of-interest, Methods,
  descriptions, and evidence demands keep changing.
- A maintained platform needs product care, but platform-local metrics cannot replace practitioner results or
  results involving the project system-of-interest.

### SYSE.12:4 - Solution

Start from the practitioner result or combination of results the platform must support. An assessment of the current arrangement establishes whether it provides the required capability under the stated conditions. A design or recommendation establishes which arrangement could do so and why. When the commission includes changing the platform, carry the decision through to the resulting configuration and the evidence its recipient needs.

#### SYSE.12:4.1 - Perform the Move

1. **Name the practitioner work, result and required coverage.** Identify the practitioners or inclusion rule, Methods, configurations, interval and receiving decision. If the question covers several work families, establish whether each needs its own result or whether they must be supported together. Retain demands and distinctions that could defeat that support even when each task fits separately. Use the known scope directly for a single task.
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
6. **Compare enabling arrangements when a platform choice is due.** A supported readiness or use assessment can settle a question about the present arrangement at steps 8–9. For a live choice, use `C.11` and develop the alternatives still missing. Options can include retaining the current arrangement, changing a capability
   or relation, composing existing Systems, obtaining or building a part, branching for a profile, preserving a bypass,
   or retiring a harmful arrangement. Name the deciding Agent, authority, accepted losses and questions outside that authority. Compare
   the alternatives for the same practitioner result and period of reliance, including continuing provider, maintenance
   and recovery Work alongside practitioner effort. Use `SYSE.24` when the obtaining comparison is unresolved and `SYSE.25`
   when the improvement mechanism needs investigation.
7. **Perform the platform change when commissioned and authorized.** If the work includes implementing the selected change, record the performing Agents,
   assignments when relevant, Methods, temporal extents, results, actual transformations, resulting configuration,
   and evidence. A decision record does not change the platform. When the current arrangement is retained,
   continue to the readiness or use assessment that the receiving decision needs without creating development Work.
8. **Assess readiness for a pre-use decision.** Use a sufficient existing assessment or state the capability and condition claims that the evidence
   available before practitioner Work supports. Keep the evidence cutoff, currentness window, limits, fallback and stop.
9. **Assess observed use for a later decision.** Use an adequate existing use assessment when it covers the question. Otherwise
   identify the practitioner Work occurrence and how the platform participated, the provider supplied a result or a resource
   was used. Use existing observations and obtain any further observations needed about burden, delay, error, rework, recovery, evidence
   continuity or the engineering result. Record the assessment separately from readiness. It can support later decisions.
10. **Return and reopen locally.** Supply only the supported claims needed by each receiving decision—for
    example, capability, condition, participation, provision, use, failure, or platform-change claims. Reconsider only
    the claims affected by a changed Work, Method, practitioner population, configuration, provider, condition,
    evidence basis, or consequence for the project system-of-interest.

Platform development, practitioner Work, support, change of the project system-of-interest and evidence Work can overlap. A claim that the platform
was used requires evidence of a relation that held in that Work, such as its participation, provision to the practitioner or use of a resource. Later observations can
support subsequent reliance.

#### SYSE.12:4.2 - Record the Result

| Field | Required content |
| --- | --- |
| practitioner use | Agents or population, Work family, Method, subject, result, configuration, interval, and receiving decision. |
| platform and providers | Actual platform System and selected parts, provider Agents and Systems, interfaces, resources, configurations, and future candidates kept as plan or description content. |
| capabilities | Practitioner capability demands and each platform or provider capability holder, Work family, envelope, measures, qualification window, currentness, and evidence. |
| conditions and relations | Conditions used by the case, such as access, performance, evidence continuity, support, exception, fallback, cost, or resource conditions; each relied-on participation, provision, availability, resource-use, promise, or other governed relation. |
| alternatives and change | For a choice of arrangement, the complete available options, deciding Agent, authority, accepted losses, disposition and grounds. For an actual change, the work and transformation that produced the resulting configuration. |
| pre-use readiness | For a pre-use decision, the assessment of capability and conditions supported before practitioner Work, with evidence cutoff, currentness window, limits, fallback and stop. |
| observed use | For a decision about actual use, the practitioner Work, participation or provision, observations about burden and results, the use assessment and the decision it can inform. |
| return and reopen | Claims supplied to each receiving decision, their limits, and the change that reopens each one. |

#### SYSE.12:4.3 - What Changes in Practice

Before investing in a platform, identify the result practitioners need, the Work they would perform to produce it and what you could observe about that Work. Engineers can improve a shared enabling System while distinguishing practitioner, platform and provider capabilities from the Work performed, the platform’s participation and
evidence of its contribution. Operations, organization change, administration, application-profile engineering and decisions about the project system-of-interest
retain their own scope.

### SYSE.12:5 - Worked Case: Platform Support for Flood-Pump Integration

Engineers integrating a flood-pump controller must reconcile identifiers among the model build,
hardware-in-the-loop bench, controller configuration, and evidence repository by hand. One missed link delays
the station integration result and makes recovery difficult.

The actual engineering platform includes the model-build System, bench, and evidence repository in configuration
C4. A support Agent provides recovery Work but is not made a part of the platform merely by supporting it. A
platform description records the structure; it is not the platform System.

For the next controller-integration campaign, each candidate must return evidence tied to the same model,
controller and bench configurations, preserve access to that evidence, and permit recovery after an interrupted
assembly. The competent incumbent records and checks the correspondence manually. It can produce the
required result; the observed missed link and repeated copying across revisions are reasons to compare a repair.

The engineers compare retaining that arrangement, strengthening its manual correspondence check, adding
configuration-and-evidence links, replacing the bench, and obtaining bounded evidence-provision Work from
another provider. Strengthening the manual check avoids maintaining new bindings but leaves reconciliation in
each attempt. The linking option carries identifiers from their originating configurations into the assembled
evidence; it removes repeated copying but requires a provider to maintain the bindings when formats or
configurations change. Bench replacement would require requalification; no identified bench limitation makes
that work necessary for this repair.
Outside provision is competitive only if it returns the same configuration-linked evidence with the required
access and recovery; otherwise the engineers must match the evidence to the configurations. Manual fallback remains part of the
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

The later use assessment records that the engineers’ evidence-assembly effort for controller integration fell
from the local baseline of six person-hours to two and a half. Recovery from a repository outage took 45 minutes,
and the export gap remained. The provider’s continuing binding-maintenance effort has not been measured
on the same basis. The observations establish the local assembly saving. To assess total Work, compare
the arrangements over the same campaign, counting provider and practitioner effort on a comparable
basis. The outage duration alone does not measure recovery effort.

If obtaining those observations is not worth its cost for the next decision, leave total burden open and
decide from the supported result and accepted maintenance obligation. If additional provider effort
outweighs the assembly saving, reconsider the claimed improvement. The verified links and completed integration
remain established. These constructed observations support this case and can inform later decisions.
Earlier reliance must be judged on the evidence then available.

**Countercase.** A repository and continuous-integration server are installed, but no practitioner Work,
participation, provision, or engineering result is observed. Record the installed Systems and the proposed
enabling arrangement; do not infer platform capability or adoption from installation.

### SYSE.12:6 - Bias Annotation

Software platform practice contributes self-service, configured defaults, fast feedback and product care.
Vendor catalogues and team-topology literature can make a tool or team appear to be the whole platform. Physical
and cross-domain engineering also relies on Systems such as laboratories, manufacturing cells, configuration
and calibration Systems and evidence stores, as well as on provider Work and recovery
arrangements.

Use publicity, university coverage, procurement, installation, usage counts or satisfaction only for the claims
each can support. When measuring broad prevalence or causal effect is too costly, explain what the
best available cases establish, what kind of evidence they provide and where its limits lie.

### SYSE.12:7 - Conformance Checklist

- [ ] Practitioner Agents or population, Work, Method, result, configuration, interval, and receiving decision are
      named.
- [ ] Source-local *service* wording is interpreted for the claim being made, such as capability, provision,
      or participation.
- [ ] Capability holders and envelopes are supported, and each direct relation states its participants and
      conditions.
- [ ] For a design or retention decision, the comparison includes the credible alternatives that could change it and records authority and accepted losses. For an assessment of one or several work families, the evidence covers the separate or combined practitioner results requested.
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
| Treat availability as use | Identify the practitioner Work occurrence and dated evidence that the platform participated in it or that a provider supplied the result relied on. |
| Use later evidence to justify earlier reliance | Keep the pre-use readiness assessment and later use assessment separate, with their evidence windows and update relation. |
| Treat satisfaction or adoption as engineering value | Observe the practitioner and project-system consequences that matter to the decision, such as effort, delay, error, rework, recovery, evidence continuity, or an engineering result. |
| Treat a golden path as the Method | Separate MethodDescription, world-side Method, enactment, fit evidence, and bypass conditions. |
| Let the platform provider decide matters outside its authority | Return each decision—such as practitioner assignment, release of the project system-of-interest, assurance, organization, or operations—to the Agent authorized for it. |

### SYSE.12:9 - Consequences

This move exposes hidden dependencies and practitioner burden and can reduce repeated integration and evidence Work. Account
for any continuing maintenance, support, configuration, observation or recovery required by each arrangement, including any
extra Work introduced by the change. Shared capabilities can create coupling, provider monopoly or concentrated failure,
so preserve profile branches and fallbacks where those risks matter.

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

For Work spanning software tools, physical facilities and separately performed provider Work,
apply task-oriented development to the enabling arrangement. Qualify each capability and relation
on which practitioners rely. Separate readiness before use from later observations. A
bench, repository and support provider can contribute different results. A missing export or
a changed maintenance burden reopens only the dependent claims. Identifying these dependencies
and maintaining their
qualifications takes work. The pump case illustrates this approach to mixed engineering
Work. A claim that it outperforms qualified direct provision requires comparative evidence.

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
comparison of obtaining alternatives. Use its result with the evidence for capability and participation, distinguishing what was known before use from what was observed later.

Reopen the affected choice when a changed input or provider breaks the relied-on correspondence or access,
when comparable continuing burden reverses the accepted trade-off, or when a supported alternative supplies
the same result with fewer obligations. Reopen the cross-profile synthesis only when a new use or comparative
source defeats the particular dependency or evidence distinction being carried across profiles.

### SYSE.12:12 - Relations

- `SYSE.25`–`SYSE.29` construct the bounded improvement, supported interaction, interface/contribution change,
  control placement, and migration results named above. Use the relevant Method when its result is missing.
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
