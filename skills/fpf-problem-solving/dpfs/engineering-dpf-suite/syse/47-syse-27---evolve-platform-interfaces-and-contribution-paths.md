## SYSE.27 - Evolve Platform Interfaces and Contribution Paths

> **Status:** Stable

> **Normativity:** Guidance within the stated engineering use; examples are illustrative.

### SYSE.27:1 - Problem frame

Use this pattern when independent changes by platform users, contributors or providers can break a supported interaction, or when every useful variation waits for one central team to implement it. Start with one proposed change and the actual consumers whose result it can alter. Recover the interface they use, the behavior they rely on and the contribution they need to make.

The first result is a bounded interface/contribution evolution decision, including consumer effects and a usable way to test a contribution. An interface may be an API, configuration format, template, physical connection or agreed operational exchange.

Do not create an extension mechanism for one private implementation with no independent consumer. Use SYSE.29 when an already selected change requires migration, and SYSE.18 when another governing Agent's decision is indispensable. This pattern changes the supported technical interaction; organizational contribution design and actual assignments remain separate questions.

### SYSE.27:2 - Problem

An interface can keep the same spelling while its units, defaults or failure behavior change. A new template can work for its author and break a consumer's unexercised variant. Conversely, requiring the central provider to implement every variation can suppress useful specialist contributions and encourage unmanaged forks.

The recurring task is to choose how the proposed contribution can enter the provision while preserving or deliberately changing the promises on which other users rely.

### SYSE.27:3 - Forces

| Force | Practical tension |
| --- | --- |
| Independent change | Contributors need room to improve their work; consumers need stable enough behavior to rely on. |
| Compatibility | Retaining every old behavior can become costly; silent breakage transfers that cost without agreement. |
| Shared extension | A reusable contribution can reduce duplication while creating new maintenance and support work. |
| Technical acceptance | Tests can establish a bounded behavior; they cannot grant permission to change another party's provision. |

### SYSE.27:4 - Solution

#### SYSE.27:4.1 - Recover the consumed behavior

Identify the actual users and versions in use, including infrequent consumers and retained templates that may run later. Read the requests and results they rely on: meaning, units, defaults, supported limits, error behavior, configuration and relevant timing conditions. Names and type signatures alone may hide the consequential contract.

Separate internal implementation choices from observable behavior. Identify which observations would distinguish a compatible implementation change from a changed promise. When use evidence is incomplete, retain that uncertainty rather than declare that no consumer exists.

Clarify who owns the interface, who may contribute, who can accept the technical change and who can authorize its actual use. Use existing assignments when they suffice. If the contribution relation or assignment is missing, use the applicable OCE.4 or OCE.6 result; do not appoint an owner by adding a name to a template.

Recover the direction of reliance. An old consumer using a new provider is a different case from a new consumer falling back to an old provider. A template copied into a repository can outlive its published replacement; identify which parts remain maintained centrally and which now belong to that consumer. Tests based only on the newest template miss that live dependency.

When a supported promise is incomplete, inspect reasonable existing use before classifying a behavior as internal. An undocumented unit conversion, timing assumption or returned-value format may have become a real dependency. Decide whether to preserve it, narrow the promise through an authorized transition, or return the unresolved consequence. The absence of documentation does not itself settle the user's loss.

#### SYSE.27:4.2 - Compare the change forms

| Possible form | When it can supply the needed result | Burden or limit to examine |
| --- | --- | --- |
| Internal implementation change | The consumed behavior remains within its existing promise. | Show that the relevant effects are preserved, not merely that requests still parse. |
| Compatible extension | New use can be added without changing supported old use. | Check old defaults, limits, failure behavior and the cost of the extension. |
| Adapter | A bounded translation can preserve the old use while a different interface operates behind it. | State losses, unsupported values, extra failure points and maintenance. |
| Explicit versioned break | The new result cannot honestly preserve the old promise. | Name affected consumers, coexistence and the migration/recovery question. |
| Refusal or outside route | The contribution is not justified or cannot be supported under the current conditions. | Give an actionable reason and a legitimate alternative or missing-premise return. |

A version label communicates a choice; it does not establish compatibility. Compare the actual cases and consequences before selecting the label or mechanism. Do not promise an adapter if lost information or changed physical effects would prevent the existing consumer from obtaining the promised result.

Derive an extension boundary from the variation that must be independent. Preserve the facts that the whole path relies on, then ask what can vary without changing them. A duration parameter may be enough for different test lengths. A separate provider implementation can be appropriate when languages need different qualified builds but return the same artifact identity and failure meaning. A change in the returned result's meaning needs a changed contract, not merely a larger plugin interface.

Compare the shared core with a maintained adapter, a separate supported profile and a private outside route. Frequent variation with stable common behavior can justify a shared extension; a rare specialist use may cost less to support separately. Include who will understand, test, repair and retire the extension. Reuse of code is not enough if every use still requires a central expert to establish its applicability.

#### SYSE.27:4.3 - Make contribution possible at the supported boundary

State what a contributor may change and what remains controlled by the provider. Supply a reproducible way to exercise the interaction, examples of supported old and new use, relevant acceptance checks, and enough failure information for a contributor to repair a rejected proposal.

Make dependencies explicit: a contribution may require a toolchain, resource, permission or domain Method not yet supplied. Preserve the distinction between a technically valid proposal, an accepted contribution and a deployed provision. A contribution test should not expose release credentials or unrestricted provider access.

Choose a maintained extension point only where independently changing use justifies it. A small parameter or documented composition may be enough; an open-ended plugin system can cost more to secure, qualify and support than the variants it enables.

Give contributors the decision basis, not only submission mechanics. Explain which user result the boundary protects, why the fixed conditions matter and which alternatives remain acceptable. Provide a small example they can adapt and a way to see whether their proposed result can be consumed. When a proposal fails, return the failed condition and the observed case so that the contributor can revise the technical idea.

Agree the continuing work before offering a new supported extension. The contributor may supply domain implementation and examples while the platform provider supplies integration, distribution and first-line diagnosis. Establish who handles an incompatible update, an absent maintainer or an urgent failure. An experimental contribution can remain available under an explicit experimental scope until those conditions are supplied. Acceptance into a repository and a promise of continued support are different decisions.

For copied templates, explain how future change reaches existing instances: a maintained dependency, an update tool with preserved local edits, a consumer-maintained copy, or an explicit migration. A generator only controls what it creates. Do not promise continued updating merely because newly generated instances contain the repair.

#### SYSE.27:4.4 - Exercise effects on consumers

Run or construct the selected compatibility cases against the old and proposed behavior. Include normal use and the defaults, limits, failures or unsupported requests that can change acceptance under the actual contract.

Use the intended result consumer to interpret the outputs. A request that is syntactically accepted but receives a different unit, deadline or configuration is not compatible merely because the interface returns success.

For a physical connection, a fit test may establish only fit. Load, alignment, measurement and safe-operation claims retain their own qualification. For software, a contract test supports its exercised conditions, not all interoperability or application correctness.

Exercise the version combinations that the proposed transition will actually allow. During coexistence this can include old consumer/new provider and new consumer/old provider, in addition to each matched pair. Compare both input interpretation and the receiving user's result. A new consumer that emits a value the old provider cannot represent cannot safely use that fallback.

Choose an order that preserves the supported combinations. For example, make receivers understand an added representation before producers begin emitting it. Keep emission restricted where the old receiver remains supported. If compatibility depends on persistent state or an irreversible effect, obtain that domain result before claiming a return path. SYSE.34 supplies the software data question; SYSE.29 organizes the affected users' transition.

Interpret a successful test at its actual reach. A contract test can expose the changed timeout unit. It cannot establish that a build algorithm is qualified for a new language or that an unknown consumer has no reliance. Resolve such gaps by obtaining the missing result, limiting the supported claim, or changing the selected form.

#### SYSE.27:4.5 - Decide support and the next change increment

Return the selected form, affected use, relevant test result or gap, and the actual maintenance/support arrangement. Make rejection useful: distinguish an implementation defect from an unsupported requirement or missing authority.

When users must move, carry the defined old/new behavior and affected consumers to SYSE.29. When an independent provider controls a needed change or commitment, use SYSE.18; a common schema cannot substitute for that decision. Revisit the interface from actual failures and contribution burden rather than from the number of extensions accepted.

Revisit the boundary when the next change no longer fits its reasons. A succession of adapters can indicate that the common result has split into materially different profiles. Conversely, repeated compatible contributions may justify moving a stable operation into shared provision. Compare those choices through the supported user result and continuing burden, retaining existing useful contributions whose conditions still hold.

### SYSE.27:5 - Archetypal Grounding

In an invented software-platform example, a workflow interface accepts `timeout: 5`. In version v1 the optional integer is an elapsed-time limit in minutes, measured from acceptance to completion; supported values are 1–30 and omission means 5. Several repositories pin v1, and one rarely used recovery workflow still carries the old template.

A contributor changes the implementation to interpret the same value as seconds. The request still parses and the contribution's example passes because its job completes in three seconds. Existing users can now time out after five seconds instead of three hundred. The proposed change is a breaking change, not an internal optimization.

The provider and contributor compare three repairs. Retaining only v1's external integer-minute input avoids the break but cannot express the new seconds-level use. An explicitly named seconds parameter can add that use while preserving v1's meaning; the internal duration unit can remain minutes if conversion preserves the requested limit. A new incompatible interface can also work, but it requires consumer migration.

The selected constructed design preserves v1's external `timeout` contract and gives the new interface a separate `timeout_seconds` input. The new input accepts 60–1800 seconds, including a new 90-second use. The adapter translates an accepted v1 request into a request that expresses duration only through `timeout_seconds`. It maps v1's 1, 5 and 30 minutes to 60, 300 and 1800 seconds; an omitted value also becomes 300. Values 0 and 31 remain invalid v1 requests. In an adverse attempt, the new interface receives a request containing both `timeout: 5` and `timeout_seconds: 90`. Because the old field specifies 300 seconds and the new one 90, the interface rejects the request as ambiguous rather than choosing either value. A constructed attempt that completes after 240 seconds meets the old five-minute limit and the adapter's 300-second limit, but not the silently changed five-second limit. Consumer examples include the infrequent recovery workflow, not only the contributor's fast demonstration.

The result is a bounded change with an exercised compatibility account. An actual maintainer still has to accept and support it, and the version reaching a consumer remains a configuration question. A passing example does not authorize the contributor to update every repository.

The construction also checks a hidden implementation condition. The ninety-second request requires a backend that can represent and enforce ninety seconds. If the backend stores only integer minutes and rounds upward, the request would run for up to two minutes. Renaming the input or adding an adapter does not repair that loss. The provider must implement adequate duration handling, restrict the supported values, or return this variant as unsupported. In this constructed case, it implements whole-second handling and exercises the boundary and omitted-input cases before offering the extension.

Change the condition again: a proposed extension for a new recovery client requires thirty seconds, while an outage fallback still calls a v1 provider whose supported minimum is one minute. Ordinary v1 clients remain unaffected, but this new consumer cannot use that fallback. Keeping v1 as a route for that client would change the promised limit. The selected response is to retain v1 for its valid consumers and withhold the thirty-second use until its provider and recovery arrangement are supplied. A single “backward compatible” label would conceal this directional difference.

Another team proposes a new language-specific build extension. The contribution entry can state its expected inputs, output and maintenance need, but without a qualified build Method and supported recovery it remains an unqualified proposal. The interface mechanism does not supply that missing professional result.

For a physical bench, a replacement fixture may match the mounting holes while changing the locating datum. A component can fit yet be measured relative to the wrong reference. The consumed behavior therefore includes the datum and measurement relation, not just bolt compatibility. A qualified fixture/measurement result is needed before the replacement is represented as compatible.

What changes in practice is the acceptance question: “Does it parse or fit?” becomes “Does this consumer obtain the promised result under the supported conditions, and who will sustain that result?”

### SYSE.27:6 - Bias-Annotation

Active consumers and easy demonstrations are easier to see than dormant recovery use or difficult variants. Contributor enthusiasm can also hide ongoing support cost. Seek evidence from the users whose work would fail under the proposed change, including the provider who must maintain it.

### SYSE.27:7 - Conformance Checklist

- Actual consumers and their relied-on behavior are identified at the grain that can change the decision.
- Internal change, extension, adapter, break and refusal are compared by effects rather than labels.
- Contributors can exercise the supported interaction and understand a rejection.
- Compatibility examples include meaningful old use and relevant adverse conditions.
- Technical acceptance, actual assignment, permission and deployed configuration remain distinct.
- Each migration need, outside-provider decision or missing specialist Method is returned to the practice or holder that can address it.

### SYSE.27:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| A matching signature is called compatible. | Compare units, defaults, failure behavior and the user's returned result. |
| Every variation becomes a central-team ticket. | Select a bounded maintained contribution point where independent contributions justify it. |
| Every variation becomes a plugin. | Compare a small parameter, composition or outside route before adding an open-ended mechanism. |
| A passing contribution test licenses rollout. | Recover the actual accepting authority, support conditions and configuration change. |

### SYSE.27:9 - Consequences

Contributors gain a usable route for change and consumers can distinguish preserved behavior from a deliberate break. Adapters and coexistence cost maintenance and can prolong obsolete interfaces. Refusal can be the correct bounded result when support, qualification or a justified use is absent.

### SYSE.27:10 - Rationale

An interface connects independently changing work through expectations. Making those expectations executable or otherwise inspectable reduces accidental coupling, while explicit change forms prevent a version name from hiding losses. The same reasoning preserves the difference between technical interoperability and another party's decision to participate.

### SYSE.27:11 - SoTA-Echoing

**Adopt and adapt** [Google AIP-180, Backwards compatibility](https://google.aip.dev/180), especially its separation of source, wire and semantic compatibility, unchanged defaults and judgement about consumer scope. It already treats a parsing success as insufficient. Sections 4.1 and 4.4 carry that developed reasoning into the supported platform task and its allowed version combinations. Its protobuf/JSON rules are not a mechanical-connection standard.

**Adapt** the contribution and evolving-operation treatment in the [CNCF Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/). It supplies a serious participatory alternative to central implementation, with operational support as part of the offering.

Compared with direct use of an API compatibility guide, this pattern also constructs the boundary at which a contributor can supply a qualified domain result and explains how maintenance reaches existing users. Where an existing framework already supplies that boundary and support, reuse it. A private fork can be adequate for a bounded private use; shared consumers make its future-change burden consequential.

The accepted trade-off is additional contract and support work for independent change. Reopen when a new consumer changes the supported combinations, an adapter cannot preserve meaning, a copied template misses required evolution, or support costs outweigh the useful variation.

### SYSE.27:12 - Relations

SYSE.26 supplies the supported user interaction and SYSE.13 identifies versions and configurations. SYSE.29 handles migration or retirement. SYSE.18 supplies integration decisions across independent authority; SYSE.24 compares complete obtaining arrangements. OCE.4 supplies contribution-architecture design and OCE.6 supplies actual holder assignments when those organizational results are missing.

### SYSE.27:End
