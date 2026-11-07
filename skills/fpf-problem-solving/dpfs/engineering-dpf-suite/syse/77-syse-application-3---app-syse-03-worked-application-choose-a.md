## SYSE.Application:3 - APP-SYSE-03 — Worked application: choose and bound an authentication-service migration

This constructed case tests whether the common Systems Engineering patterns still help when the System designated as project system-of-interest
is software-only rather than electromechanical. It assumes the named software-security result; it does not teach
cryptographic design or threat modeling, decide privacy or law, or grant release authority.


### SYSE.Application:3.1 - 1. Fix the System, use, and decision

`SYSE.1` identifies deployed software System `AccountAccessService`, current configuration `AS-7.4`, and the
bounded use: tenant login during a five-minute loss of communication between two regional session stores. The
next decision is whether to prepare one candidate architecture for a limited production canary. Account holders, tenant applications, the incident-response team, and the service operator are the affected
Systems relevant to this choice. The first result, `AccountAccessProjectFocus-R1`, excludes unrelated identity-
governance and user-interface changes.


### SYSE.Application:3.2 - 2. Compare architecture alternatives using displayed evidence

The project's software-security Agent performed `AuthenticationThreatModelingWork-TM4` by applying
`ProjectSoftwareSecurityThreatModelingMethod`. That Work produced `AuthenticationThreatModelResult-TM4`, which
supplies two constraints used here: regional cache replication must be mutually authenticated and encrypted,
and acceptance of a revoked credential must end within 120 seconds. The architecture Agent uses those constraints
to admit alternative `A` and exclude a ten-minute bearer token under the current threat model. The architecture
Agent remains responsible for the architecture choice, and the release Agent retains release authority.
Using `SYSE.5`, the architecture Agent develops three materially different bearer and interface alternatives.
Using `SYSE.6`, the same Agent compares them against four declared limits: failed logins below 1%, acceptance of a revoked credential for no more than 120 seconds,
95th-percentile login latency no greater than 3 seconds, and rollback within 30 minutes. A controlled partition
replay for configuration candidate `AS-7.5-rc2` returns these values:

| Alternative | Failed logins | Revoked-credential exposure | p95 login latency | Rollback | Result |
| --- | ---: | ---: | ---: | ---: | --- |
| `A` — replicated regional session cache | 0.6% | 80 s | 2.4 s | 18 min | Meets all four limits; adds replication and operating complexity. |
| `B` — signed ten-minute tokens with a revocation feed | 0.4% | 600 s | 1.8 s | 12 min | Rejected for this use because the 120-second security limit fails. |
| `C` — retain the single-region session store | 8.2% | 35 s | 2.1 s | 8 min | Rejected because the failed-login limit fails during the partition. |

`AuthenticationArchitectureDecision-AD7` therefore selects `A` for canary preparation. It records the added
replication burden as an accepted loss. The choice uses `AuthenticationThreatModelResult-TM4`; the table does not establish that specialist result or
transfer the specialist's authority.


### SYSE.Application:3.3 - 3. Bind the recommendation to configuration, effectivity, and evidence

Using `SYSE.13`, the configuration Agent identifies candidate configuration `AS-7.5-rc2` and its proposed
effectivity: tenant cohort `TenantCohort-Canary`, 5% of eligible traffic, regions `EU-West` and `EU-Central`, for
seven days. Using `SYSE.4`, the assurance Agent qualifies the partition replay only for the four claims and
conditions shown above. It does not support wide release, other regions, a different token lifetime, or a
different threat model.

The release-preparation Agent uses `SYSE.14` with the architecture decision, configuration account, replay
result, `AuthenticationThreatModelResult-TM4`, and rollback evidence. The Work returns this recommendation: prepare alternative `A` as `AS-7.5-rc2` for the stated 5%
canary; retain `AS-7.4` as the rollback configuration; do not widen effectivity until the release Agent receives
the canary observations and the required security permission. The recommendation is not the release occurrence
and grants no authority.


### SYSE.Application:3.4 - 4. What transfers and what remains specialist

The same Systems Engineering moves transfer unchanged: choose the project system-of-interest and use; expose affected
Systems; develop bearer and interface alternatives; bind claims to configuration and effectivity; qualify
evidence for a receiving decision; and keep the designated System distinct from the CI/CD and observability platform
used to change it. The software-security profile retains cryptographic construction, authentication threat modeling,
privacy and data-protection analysis, security-specific deployment conditions and security-incident response.
Their Methods and authorities remain external. Part VII supplies selected runtime, exposure and technical
recovery Methods only where their conditions fit; it does not supply those specialist security results or
change the evidence and permission limits of this case.


### SYSE.Application:3.5 - Result, stop, and reopen

Another practitioner can reproduce the recommendation by applying the four limits to the displayed values:
`A` is the only surviving architecture, and its evidence supports only the stated canary. Stop when the release
Agent can decide that canary with the named security permission and rollback available.

| Changed input | Reopen |
| --- | --- |
| project system-of-interest designation, partition use, affected Systems, or decision horizon | `SYSE.1` project-focus result |
| an architecture option, bearer/interface relation, or any of the four limits | `SYSE.6` architecture choice |
| candidate configuration, cohort, region, traffic share, or seven-day effectivity | `SYSE.13` configuration result |
| replay conditions, observation values, evidence window, or claim correspondence | `SYSE.4` evidence-use result |
| security permission, rollback availability, or canary observations | `SYSE.14` release recommendation |
| threat model, cryptographic construction, privacy constraint, or security authority | the owning software-security or legal Method and source |
