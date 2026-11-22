## SYSE.41 - Deploy a Verified Software Artifact with the Target Configuration and Handle Partial Failure

> **Status:** Stable

> **Normativity:** Guidance within the stated software-deployment use; examples are illustrative.

### SYSE.41:1 - Problem frame

Use this pattern to establish what artifact or configuration runs on a target or to deploy a required configuration. For a question about current state, identify the property and the target or population the answer must cover. For deployment, start with the artifact qualification from SYSE.32, the target and configuration from SYSE.13, the required resources and dependencies, any applicable data-change result from SYSE.34 and permission for the operation.

For a question about a running version or effective setting, a qualified readback on the relevant target can complete the answer. For a deployment, establish the intended runtime state, the applicable test result and any partial or uncertain effects. If several targets supply one service, the release decision may also depend on which versions operate together or where work is routed.

If the required current runtime already exists with applicable observation and test evidence, use the existing runtime and its evidence. If artifact qualification or data compatibility is missing, return that condition before the dependent operation. This pattern does not supply general application acceptance, wider exposure permission or the whole-System usability decision.

### SYSE.41:2 - Problem

Deployment changes several coupled things: installed software, effective configuration, dependencies and sometimes persistent state. Some changes can complete before a command times out. The controller can fail while one instance already runs the new binary with the old configuration.

Blindly repeating the whole job can duplicate resources or repeat a migration. Returning an old binary can also fail if the data or external contract has changed. The actual resulting runtime must therefore be recovered and tested independently of the controller's summary.

### SYSE.41:3 - Forces

| Force | Practical tension |
| --- | --- |
| Consistent procedure and different targets | Reuse reduces variation while environment-specific configuration and permissions remain real. |
| Bounded change and partial completion | A small deployment limits impact but can still leave mixed versions or states. |
| Fast return and compatibility | A previous runtime is useful only while it remains compatible with actual data and dependencies. |
| Technical success and reliance | Installation and a deployment test support a limited use, not every application behavior or release decision. |

### SYSE.41:4 - Solution

#### SYSE.41:4.1 - Recover the intended and actual configuration

Identify the target and the running property the decision needs. A qualified report of its effective setting may settle a question about that setting. For an installation, identify the verified artifact, establish that its bytes are obtainable, and recover the intended configuration and dependency conditions. Where configuration is supplied separately, carry the same tested package to the destination.

Inspect the actual target state before acting: what is running, what is installed, which configuration is effective, and whether an earlier attempt has already changed anything. A desired-state file or an old deployment record does not replace current observation when drift or partial effects are material.

Identify any last usable configuration and the conditions under which it can be restored. If there is no qualified fallback, state that limit. Before changing the target, establish permission for the intended operation and obtain any missing authority. Access to a deployment tool does not by itself authorize a different target, wider user exposure or an unqualified data change.

#### SYSE.41:4.2 - Construct a bounded deployment procedure

Choose the deployment unit and how existing useful service will be preserved where the architecture permits it. Define the order the dependencies require and the point at which a test or observation changes the next action.

Use [DORA Deployment automation](https://dora.dev/capabilities/deployment-automation/) to organize supplied packages, environment configuration and a deployment procedure. Its operations prepare the target, install the package, apply required configuration and dependency changes, and perform a deployment test. Bind these operations to the mechanisms and permissions available on the target.

Account for each step's partial and replay behavior. Preparation may create resources; installation may change only some targets; configuration may be written but not loaded. Include data operations only when SYSE.34 or an equivalent qualified result permits them. An outer deployment job is not authority to invent or repeat a migration.

#### SYSE.41:4.3 - Prepare, install and observe the actual runtime

Where the observed target still needs work, perform the required, authorised steps in order. These may include preparing resources and dependency access, installing or updating the selected artifact, and applying its matching configuration. Use the existing authorized secret mechanism and verify configuration without displaying the secret values.

Establish the running artifact and effective configuration on the targets the question covers. A service-wide attestation can answer for several targets if its coverage, meaning and currentness establish the required condition throughout. Preserve differences among instances when routing, coexistence or a partial change can alter the user’s result. Check the dependencies needed for that use.

For a reconciliation mechanism, observe convergence and the process result. A declaration accepted into version control or a desired replica count is not evidence that the intended artifact/configuration is serving the required use.

#### SYSE.41:4.4 - Perform the deployment test

Use a test result applicable to the required installation and connection. If the evidence is missing and a permitted test can supply it, exercise the bounded task. Establish the tested artifact and configuration, target, time and outcome, or state what remains unknown.

Distinguish missing observation from failure and failure from a successful but narrower test. A process health check can show liveness without demonstrating an application write/read or dependency interaction. Select the test from the intended next use.

Return a successful runtime result only for the targets and conditions for which the test and observations establish the required result. If a smaller qualified subset is useful, state its capacity and limits rather than silently presenting it as the complete requested deployment.

#### SYSE.41:4.5 - Choose a safe continuation after partial failure

After a timeout or interruption, use available observations to establish which states the deployment could have reached. Select a permitted continuation, removal or return that preserves the intended result in those states. If the same step is qualified for all of them, it may be repeated. If the choice depends on which effect occurred, inspect the target or original attempt, or hold the affected step. Verify the resulting runtime separately before relying on it.

Keep an unqualified candidate out of ordinary reliance where the architecture and authority permit that separation. Preserve the working prior service rather than damaging it during an uncertain repair. If the old service is no longer available, state that constraint instead of assuming a rollback path.

Use SYSE.34 before returning binaries across a changed data boundary. If effects or readback remain unknown, stop the operation that could create duplicate resources, repeat external effects or corrupt stored data, and request the missing observation or specialist result. A “failed deployment” label does not establish that no state changed.

#### SYSE.41:4.6 - Return the deployed result to its consumers

Return the runtime property, targets and time the observation covers. For deployment, include the dependency and test results required for reliance, any unresolved effects and the scope of the supported use. A procedure can be delivered for a future deployment. A claim of completed deployment needs grounds for the actual result.

SYSE.11 can use these integration observations to assess bounded usability of the resulting System. Use SYSE.35 when further exposure needs evaluation, and SYSE.14 when an authorized release decision is needed. A passed deployment test does not supply permission to widen use.

#### SYSE.41:4.7 - Choose the deployment arrangement and make interruption recoverable

Construct the procedure around the target's possible intermediate states. Separate preparation that can occur while the old service runs from operations that change a serving process or shared data. Place each compatibility prerequisite before its first consumer. Put an observation after the operation whose result determines the next choice. This creates a dependency structure that can permit parallel preparation while preserving necessary ordering.

Choose the replacement arrangement from coexistence and capacity. A rolling replacement can keep some old instances available while updating others, provided old and new versions can coexist and the remaining capacity is sufficient. A separately prepared candidate pool can be tested before routing changes, at the cost of extra resources and shared-state analysis. A stop-and-replace operation can be simpler for a service that permits the interruption and cannot coexist with its successor. Each needs a result test and a recovery boundary.

Identify the operation that starts the candidate’s effects on live work. Copying a file, restarting a process, reloading configuration, changing routing and enabling a feature can have different effects. The installed artifact may remain dormant; conversely, a scheduled worker can start processing shared work immediately when it starts. If runtime construction itself activates the candidate, obtain the corresponding exposure authority and protection before that action. Separation of deployment and wider exposure is a useful architecture where it exists, not a factual claim about every application.

Use stable resource or operation identities when the task asks what the interrupted request did or a safe continuation depends on its earlier effects. Advance a durable progress indication only when its corresponding effect is established under the failures the mechanism can undergo. After a lost acknowledgement, an authorized retry can complete the required operation if it is qualified for every state still possible, including partial execution and relevant intervening changes. When its safety depends on resolving an earlier effect, use reliable readback or another qualified reconciliation. If no permitted safe continuation is available, stop the affected step and identify the state or assistance still needed.

Keep the common procedure separate from legitimate target parameters. A test environment can supply a smaller pool and controlled data while retaining the same installation and configuration-loading mechanism. If production uses an additional proxy, identity provider or storage mode, exercise the relevant join before relying on lower-environment success. Keep target-specific exceptions visible and supported instead of growing unrelated scripts whose behavior can no longer be compared. Simplifying those exceptions can be a better investment than automating every historical variation.

Construct the deployment test to discriminate the next required claim. A process readback can establish the loaded artifact when it distinguishes the candidate builds, a connection exercise can establish access, and a bounded write/read can establish a selected application interaction. The collection must cover the promised installation result without becoming a substitute for every acceptance or reliability check. Use reserved test data or another qualified containment mechanism when test effects would otherwise reach ordinary users. A test that sends an actual customer notification needs the corresponding permission; tagging the request synthetic does not contain that effect.

For a scheduled importer, the apparent candidate pool may share the live work queue. Starting its workers already changes which version processes real jobs. The team can bind a candidate to a qualified test queue and limited credentials for isolated deployment testing, or treat startup as bounded live exposure with compatible jobs and a stop plan. If neither arrangement is available, a planned interruption may be the supported choice. The same artifact promotion and runtime readback remain useful. In each deployment architecture, identify the operation that first exposes live work to the candidate.

### SYSE.41:5 - Archetypal Grounding

In a constructed ParcelWorks deployment case, the platform already has a verified candidate artifact h2 and intended configuration c2. The old service has an observed serving pool at h1/c1. A separate two-instance candidate pool can be prepared, installed, configured, started and queried through an authorized operator interface.

The data state retains the old address contract under SYSE.34's single-authority correspondence. A release holder permits deployment and a synthetic address write/read test in the isolated candidate pool. This permission does not include routing general users to it.

The team constructs the following procedure from those available capabilities.

| Operation | Result to establish |
| --- | --- |
| Recover the old and candidate pools' current state. | h1/c1 remains usable for ordinary service; existing candidate effects, if any, are known. |
| Prepare candidate resources and dependency access. | The named candidate targets can reach the required database and artifact source under the permitted configuration. |
| Install retained h2 and apply c2. | Each candidate process is observed running h2 with effective c2. |
| Exercise the permitted address write/read. | The result preserves the selected D/L/T correspondence under the qualified data state. |
| Return the deployment result. | The observed targets, identity, test and limits are available to the next usability/exposure decision. |

In the normal constructed history, both instances run h2/c2, their required dependency is accessible and the bounded test succeeds. The old serving pool still receives ordinary traffic. The candidate is usable for the exercised test; further address-form acceptance and exposure remain separate.

Now consider a partial history. The first instance reports h2/c2. The second install request times out, but readback finds h2 running with c1 and a failing database connection test. The controller's failure did not mean that the second instance stayed unchanged.

The operator keeps ordinary routing on the old pool and excludes the unqualified candidate. With the partial state known, the operator applies the authorized c2 correction to the second instance, verifies that the running process loads c2, and repeats the bounded deployment test. If the correction fails, the operator can retain a clearly bounded qualified subset or remove/return the candidate only under the selected capacity and recovery conditions.

When direct readback is unavailable, determine whether an independent authenticated report covers the running configuration at the time required. A record of an earlier state needs grounds for continuity. Keep unresolved targets out of a deployment result requiring confirmed state. A separately commissioned readback or functional test remains due.

Returning candidate processes to h1/c1 is available in this example only because the old data contract remains valid and the runtime restoration test succeeds. A migration that loses information required by the old data contract or the agreed recovery result would remove that basis. A new data migration is never repeated merely because the outer deployment job did not report success.

Report the artifact and effective configuration established on each target, the available test result and any unresolved state. The recipient can then decide whether the available runtime supports its next use.

### SYSE.41:6 - Bias-Annotation

Deployment tools encourage attention to their own job state. That can hide mixed runtime configuration, unknown targets and a successful copy that was never loaded. Inspect the actual process and user-relevant test, including the continued validity of the fallback.

### SYSE.41:7 - Conformance Checklist

- Before changing a target, the applicable artifact qualification, target and configuration, dependencies, data conditions and permissions are established. A missing prerequisite is stated for the operation it prevents.
- For a deployment, establish the starting state or its uncertainty and identify any usable fallback and its conditions.
- A procedure for deployment identifies the ordering, partial effects and replay conditions that matter to that operation.
- For each target credited with successful deployment, observations establish the running artifact and effective configuration.
- For a claimed successful deployment, an applicable test covers the named use under permitted conditions. A missing test limits that claim.
- After partial failure, the selected continuation is authorized and qualified for the states still possible. A stateful return stays within its qualified boundary.
- The result states its interval, targets and limits without granting wider release authority.

### SYSE.41:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| Treat artifact promotion as deployment completion. | Establish which artifact and configuration are running and what the applicable deployment test shows. Recover missing evidence where possible. Deploy or correct the runtime when the required state is absent and the operation is authorised. |
| Report requested configuration as effective configuration. | Query what the running process uses. |
| Restart the whole deployment after a timeout. | Resolve effects that could make the next step unsafe. Repeat only steps qualified for the remaining states and permitted on the target. |
| Roll back binaries after incompatible data changes. | Establish the data recovery or forward repair available before relying on return. |

### SYSE.41:9 - Consequences

The pattern makes partial deployment visible and supports safer continuation or return. A successful deployment claim needs evidence of the commissioned runtime result and the tests the acceptance agreement requires. A return to prior service needs qualified fallback conditions; missing evidence limits the corresponding conclusion. Some deployment mechanisms need improvement before they can distinguish copied, loaded, failed and unknown states.

### SYSE.41:10 - Rationale

Deployment creates or changes the target runtime. Moving an artifact or declaring desired state supplies only part of that result. Observation and a bounded task test establish what the change produced. Separating that result from application acceptance and release preserves the reach of its evidence and authority.

### SYSE.41:11 - SoTA-Echoing

For making tested software usable in a runtime, **adopt and adapt** [DORA Deployment automation](https://dora.dev/capabilities/deployment-automation/) and the [Continuous Delivery pipeline](https://continuousdelivery.com/implementing/patterns/). Common procedures, same-artifact promotion, environment configuration and deployment tests come from these approaches. Sections 4.2–4.7 connect those operations to target-specific intermediate states and qualified recovery.

Compare rolling replacement, a separate candidate pool and planned interruption using coexistence, capacity, activation effects and recoverability. Repetition and order independence are capabilities to construct where needed, not properties granted by an automation tool. Actual readback and a retained operation/result relation cost engineering effort but permit a defensible continuation after lost acknowledgement.

Reopen the arrangement when configuration loading, target identity, provider behavior, data compatibility or exposure effects change. A scheduled worker can begin live work at startup; separation of deployment and exposure must be established for the architecture in use. A passed deployment test supplies its bounded runtime claim and no wider release authority.

### SYSE.41:12 - Relations

SYSE.32 supplies artifact-specific promotion evidence, SYSE.13 identifies target/configuration, SYSE.33 supplies reconstructible environment conditions and SYSE.34 supplies data compatibility/recovery. SYSE.11 uses actual integration observations for bounded usability; SYSE.35 governs exposure evaluation and SYSE.14 the release decision. SYSE.36 observes the deployment task, while SYSE.38 handles an active failure.

### SYSE.41:End
