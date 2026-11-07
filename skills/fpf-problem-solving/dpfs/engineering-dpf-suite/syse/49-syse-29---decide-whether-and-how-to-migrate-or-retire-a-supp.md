## SYSE.29 - Decide Whether and How to Migrate or Retire a Supported Platform Path

> **Status:** Stable

> **Normativity:** Guidance within the stated engineering use; examples are illustrative.

### SYSE.29:1 - Problem frame

Use this pattern when a supported provision is changing or disappearing and users, retained state, dependencies or support promises still rely on it. Start by finding the affected uses and what must remain obtainable or transferable. Compare them with the proposed receiving path before announcing that migration is complete.

The first result is a bounded migration or retirement decision, with an executable next increment when a change is selected, or an explanation of what prevents that change. Name any missing consumer information, permission, compatibility result or recovery result. The subject is the change of actual supported use, not merely a new version name or a removal date.

Use SYSE.27 when the old/new interface meaning is still undecided. A private unused prototype with no retained state or external obligation does not need this migration Method. A live provision cannot be treated as that prototype merely because recent traffic is zero.

### SYSE.29:2 - Problem

A new path can be technically available while existing users cannot perform their work through it. Old records may remain readable only through the retired service; infrequent recovery tasks may be absent from recent usage logs. A nominal rollback can restore an old executable while leaving incompatible data behind.

Keeping every old path indefinitely is not a solution either. Unsupported dependencies, security risks and maintenance burden can make continuation unacceptable. The decision must give remaining use and obligations a truthful disposition.

### SYSE.29:3 - Forces

| Force | Practical tension |
| --- | --- |
| Improvement and continuity | A better path may change the assumptions of users who cannot move immediately. |
| Retirement and retained state | Stopping new requests does not remove stored information, evidence or future recovery use. |
| Coexistence | Two paths can lower transition risk while increasing maintenance and compatibility burden. |
| Complete knowledge | Actual consumers may be hard to enumerate; uncertainty must be handled without inventing either zero risk or an endless support promise. |

### SYSE.29:4 - Solution

#### SYSE.29:4.1 - Recover the affected use and obligations

Combine use observations with actual dependency evidence: configured clients, templates, scheduled and recovery work, retained records and provider commitments. Name the population and interval the evidence covers. A quiet observation window does not establish absence of infrequent use.

For each materially different use, identify the required result, old configuration, retained state, relevant rights and support conditions. Distinguish a description that mentions the path from a live dependency on it.

Recover who can decide the change and who must provide the receiving result. If an independent provider controls availability, notice or withdrawal, use SYSE.18. Keep uncertainty explicit when the population cannot be completely enumerated; it informs the authorized decision rather than becoming a fictional empty inventory.

Find uses that must move together. Two apparently independent clients may share one writable data store, fixture, credential service or operating window. Group a next increment by those dependencies when separate movement would create an unsupported combination. Retain independent uses as separate options.

Ask users what they must still do after the last ordinary request. Recovery, interpretation of retained results and reproduction of an earlier configuration can create a future need even when no new production work is planned. When information about a consumer remains unavailable, state what observations were possible and which consequential reliance is still uncertain.

#### SYSE.29:4.2 - Compare the transition choices

Consider continued support, narrowed support, coexistence, adaptation, replacement and retirement against the actual user result and constraints. Include the burden and risks of keeping the old provision as well as those of moving.

Identify where old/new configurations can coexist and where they cannot. Recover state correspondence, supported interfaces and the effect of new-only features. Returning an executable, restoring data and repairing forward are different operations. Use SYSE.34 for software persistent-data compatibility and restoration, and the appropriate domain Method for physical recovery.

Keep complete obtaining alternatives with SYSE.24 when the receiving provision itself is still a choice. Migration planning does not prove that the proposed replacement is the better arrangement.

Construct the candidate transition forwards from the old state and backwards from the receiving use. Identify the first point at which the new path can supply the user's result, and which old dependencies remain necessary until then. Decide where old and new provision may both be available, which one accepts changes to shared state, and how effects made on one side become usable on the other. Use a qualified conversion or synchronization Method; a promise to “keep both in sync” is a missing operation.

Locate the point beyond which return no longer preserves the required result. New-only data, a removed decoder, a revoked permission or consumed material can cross that point. Before it, a tested return may restore the old use; after it, the feasible continuation may be forward repair, a separately qualified restoration with a stated loss, or an authorized interruption. Compare transition choices with that boundary visible.

Choose coexistence duration by the work it permits and the burden it creates. It should give real consumers time and means to establish their receiving uses while containing the risk of sustaining old provision. A provider withdrawal date is a constraint on available choices, not evidence that the migration fits. If migration capacity cannot meet it, compare narrower support, another receiving arrangement, an altered commitment and an explicit end of reliance with the holders who can decide them.

#### SYSE.29:4.3 - Construct one executable next increment

When a use is selected for migration, choose a representative affected use that can move under the actual permissions. Name its source configuration and state, receiving configuration, conversion or transfer operation, dependencies, assistance, acceptance question and recovery boundary.

Specify what will stop expansion: an unusable result, an unqualified variant, unknown partial effects, a lost support commitment or a violated constraint. Retain the previous path only where its continuing risk and obligations allow it. If no safe return exists, make the forward-repair or outage condition explicit before the change.

Explain the change at the user's point of use. Supply the replacement entry, relevant differences, needed action and support return. A notice is useful when a user can act on it; a calendar announcement alone does not provide a usable replacement or permission to migrate.

Supply the means of moving as part of the increment. A migration tool needs a qualified input class, an intelligible result, partial-effect recovery and an actual support provider just as the ordinary path does. Where a user must change how they work, demonstrate the new action and let them exercise it on representative material. A notice or training attendance is not evidence that the receiving task can be completed.

Arrange the increment with the users and providers who must perform it. Confirm the available window, preparation, access and resource demand together. If the same specialist must support ordinary use and the trial, reserve a feasible interval or change the increment. This is coordination of existing responsibilities; redesign assignments only when the existing ones cannot supply the work.

#### SYSE.29:4.4 - Exercise the receiving use and its failure branch

Establish qualified receiving use before widening reliance. Reuse a matching qualified result; perform a bounded trial or a clearly labelled rehearsal where its required basis is missing. Check the result through a representative consumer, including the old state, permissions, variants and partial-failure cases that can defeat this transition.

After an interrupted step, recover what actually changed before retrying. Test the claimed return or forward repair under the applicable state conditions. Keep a successful ordinary case from qualifying an unexercised recovery or infrequent-use branch.

Compare later use with the promised result and observe transferred user/provider burden. When a new condition changes compatibility or recovery, stop only the dependent move and repair or return that condition.

Use each trial result only for matching receiving conditions. A shared qualified conversion can cover several identical input classes, while an unexercised data format or different permission model remains separate. Expansion should either stay within the qualified class or obtain the missing evidence for the new class. Sampled success does not establish that every consumer moved; establish actual transition from the states and uses that changed.

After a move, observe the next consequential use, including delayed tasks where feasible. Retain only the former provision needed by the selected recovery or residual obligation. When a new defect appears, reopen the affected conversion, access or receiving operation rather than rerunning unrelated successful migrations.

#### SYSE.29:4.5 - Give retirement an explicit scope

Before ending the old provision, give each remaining supported use an actual disposition: qualified transfer, continued bounded support, an available outside result, or an authorized end of reliance with its consequences understood. State the consequences of that disposition for the affected users, retained state, rights and support obligations. Do not present an unresolved disposition as migration success.

Separate cessation of new requests, removal of a served interface, deletion of resources, retention of records and loss of the ability to interpret those records. They can require different actions and permissions. Retaining an export file is insufficient if the needed content, identity or receiving reader is lost.

Update the user-facing entry and support information when the actual availability changes. Remove obsolete access or resources only under the applicable authority and retention conditions. If retirement is justified despite residual uncertainty, state the accepted exposure and response; do not claim that zero users or zero obligations was proved.

Return the bounded decision, any completed increment, and any next work or premise still needed. Retirement is not implied by a date, a disabled button or a period of zero traffic.

### SYSE.29:5 - Archetypal Grounding

A separate constructed software example concerns three consumers of preview-environment recipe v1. Two use it daily; the third is a quarterly recovery exercise. Recipe v2 is available for the ordinary service class, and the provider wants to stop maintaining v1.

Thirty days of request logs show no use by the recovery consumer. Inspection of the actual recovery configuration nevertheless finds a pinned v1 dependency and retained environment metadata in v1's format. “No recent requests” therefore does not close that use.

The first increment moves one daily consumer. Its request identifies the same service artifact, synthetic data and acceptance question on v2. A constructed trial returns the expected configured environment and successful connection test. In the adverse trial, creation times out after allocating resources; the operator identifies the partial environment before repair. The next action reconciles its configuration or returns to the still-supported v1 route under the tested conditions. It does not create another environment blindly.

The other daily consumer then moves under the same qualified conditions. Retirement still stops at the recovery consumer: its restoration procedure has not been exercised on v2, and old metadata must remain interpretable. A working ordinary preview is not that missing recovery result.

Two continuations are possible. If a bounded recovery exercise and metadata-reading check establish the needed result on v2, the holder can decide the final move and end v1 under the actual support conditions. If they fail, the result is continued bounded v1 support, a different receiving arrangement or an explicitly authorized end of that recovery promise—not “all users migrated.” A retained decoder or qualified conversion may remain necessary after the old request endpoint stops serving.

Choose the first continuation for a complete illustrative outcome. The provider supplies a tested metadata decoder preserving artifact, recipe, synthetic-data identity and result references; the quarterly consumer performs its representative recovery exercise on v2 with the needed access. Both daily uses and that recovery use now have qualified receiving routes under the stipulated conditions. New requests to v1 can end, while the retained decoder and protected evidence remain available for the applicable retention period. The provider closes the served endpoint only; deletion of the old records remains a separate decision. These are constructed case results, not a report of an actual migration.

Change the condition: the external provider now withdraws the old endpoint before the quarterly exercise can be performed, and no qualified return remains after v2 starts writing its new-only state. Indefinite v1 support is no longer a feasible option. The holders compare a temporary outside recovery arrangement, postponing the state-changing move, or an authorized interruption of that recovery promise. If none is qualified or permitted, the affected migration remains unresolved. Ordinary v2 uses whose conditions are independent can continue.



For a physical inspection or machining path, exit also requires transferable tooling, programs, relevant rights and a provider capable of producing the required result. Sending a drawing does not qualify the receiving setup. Reverting the old program cannot restore material already removed from a component; recovery may require segregation, inspection, rework or replacement under the applicable engineering decision.

What changes in practice is the stopping condition: migration ends when the declared receiving uses and remaining obligations have actual dispositions, not when the new interface is announced.

### SYSE.29:6 - Bias-Annotation

Daily traffic makes ordinary users visible and hides infrequent recovery, archived-data and seasonal uses. The team funding the replacement may understate coexistence burden, while the team maintaining the old path may overstate the need to preserve it forever. Compare both risks at the actual reliance boundary.

### SYSE.29:7 - Conformance Checklist

- Affected users, dependencies, retained state and support conditions are recovered from more than recent traffic alone.
- The old/new result and compatibility conditions are concrete.
- When a change is selected, its next increment can be performed and checked under actual permission.
- Partial effects, return and forward-repair limits are explicit.
- Retirement distinguishes interface availability, resource removal and retained information use.
- Remaining obligations receive a truthful disposition, including any authorized residual exposure.

### SYSE.29:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| Zero traffic proves that a path is unused. | Inspect configured and infrequent uses and qualify the observation window. |
| The new endpoint exists, so migration is complete. | Exercise the receiving user's result with the relevant state and conditions. |
| Rollback means reinstalling the old binary. | Recover data and interface compatibility and the qualified recovery operation. |
| Keep the old path forever to avoid every risk. | Compare continued-support risks and select a bounded disposition with the actual holder. |
| A file export completes exit. | Check retained meaning, identity, rights and the receiving capability. |

### SYSE.29:9 - Consequences

Users can move through bounded qualified changes, and removal can proceed without silently abandoning state or support. Coexistence and interpretation of old records can remain costly. Explicit withdrawal may still be necessary; it is a decision about actual consequences.

### SYSE.29:10 - Rationale

A supported path connects users, results and continuing obligations. Changing its interface does not by itself change all those relations. Consumer-level trials and explicit residual dispositions let retirement be both bounded and truthful, while avoiding an automatic promise of indefinite support.

### SYSE.29:11 - SoTA-Echoing

**Adapt** the operations and feature-removal treatment in the [CNCF Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/). It already includes migration assistance, responsibility and ongoing operation. Its levels are contextual guidance, not a required target or a retirement timetable.

**Adopt the distinction**, from the [Kubernetes deprecation policy](https://kubernetes.io/docs/reference/deprecation-policy/), between ending a served version and retaining the ability to decode stored information. Its version-conversion and rollback conditions are useful comparators for coexistence. Kubernetes' own guarantees and notice periods remain local to Kubernetes.

Against that developed provider policy, this pattern adds the consumer-side construction: identify uses that must move together, obtain a receiving result with its old state, and derive the last feasible return and the remaining obligations. If an existing provider-managed transition already supplies these results and covers the actual consumer, use it; a second migration plan adds no value.

The practical alternatives are bounded continued support, coexistence with qualified conversion, replacement and an authorized end of reliance. Choose from their actual capability, support burden and consequences. Reopen on an overlooked consumer, changed state correspondence, failed receiving use or changed withdrawal terms. Physical transfer still needs its own tooling, rights, process qualification and recovery result.

### SYSE.29:12 - Relations

SYSE.27 supplies the old/new interface decision. SYSE.13 identifies configurations, SYSE.14 supplies release decisions and SYSE.18 handles independently governed providers. SYSE.24 compares whole obtaining arrangements. SYSE.34 supplies software/data recovery; SYSE.25 uses later task evidence to choose the next improvement.

### SYSE.29:End
