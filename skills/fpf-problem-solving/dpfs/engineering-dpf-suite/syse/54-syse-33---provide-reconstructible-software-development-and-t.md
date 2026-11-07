## SYSE.33 - Provide Reconstructible Software Development and Test Environments

> **Status:** Stable

> **Normativity:** Guidance within the stated software-engineering use; examples are illustrative.

### SYSE.33:1 - Problem frame

Use this pattern when development or a test works only on one prepared machine, fails because of shared mutable state, or cannot be repeated after an environment is lost. Start with the named task and the conditions it needs, including the resources, dependencies, data and access that must actually be available.

The first result is an environment that can be created and exercised for that task, with its applicable conditions and limits. If a required resource, permission or data source is unavailable, return the reconstructible description and the precise missing result; do not call that a usable environment.

Use an already adequate environment while it satisfies the task's conditions. Exact identity of every incidental machine property is unnecessary unless the task depends on it. This pattern concerns software development and test conditions, not the complete qualification of a physical laboratory or production process.

### SYSE.33:2 - Problem

A setup instruction can omit the package installed months ago, a manually altered service, a local credential or a shared fixture. Copying the machine then reproduces some of its history without explaining which conditions the task requires.

Infrastructure descriptions solve only part of the problem. A declared database is not its retained contents, a secret reference is not granted access, and a running machine is not evidence that the intended test can execute. Partial creation and configuration drift make these distinctions consequential.

### SYSE.33:3 - Forces

| Force | Practical tension |
| --- | --- |
| Fidelity and cost | A task needs representative conditions, not an unnecessarily expensive copy of every production component. |
| Isolation and cooperation | Independent attempts avoid interference while some integration questions require controlled shared dependencies. |
| Reconstruction and state | Replaceable infrastructure can be recreated; persistent information needs a separate retention and restoration basis. |
| Automation and authority | A mechanism may know the desired state without permission or capacity to produce it. |

### SYSE.33:4 - Solution

#### SYSE.33:4.1 - Define the environment for its task

Name the task, the software/configuration it exercises, its relevant dependencies, and the observations that will establish readiness for that use. Distinguish a local editing environment, a build worker, an integration test environment and a deployment target when their requirements differ.

Recover the current working conditions from a representative attempt. Identify the runtime and toolchain, resolved packages or images, network/service dependencies, resource needs, test data and access references. Separate relevant constraints from incidental machine history. Return unknown conditions that could change the test's meaning rather than assuming the current machine is authoritative.

Choose an equivalence criterion appropriate to the use. A behavior test may require the same database semantics and fixture content without requiring the same machine identifier. A timing claim may require additional resource and load conditions. An environment suitable for the first task is not automatically suitable for the second.

#### SYSE.33:4.2 - Separate description, provision and information

Keep the desired configuration under a retrievable versioned identity together with the supported creation or reconciliation procedure. Name actual resources independently so that their current state can be observed and their ownership established.

Distinguish replaceable resources, persistent state, disposable fixtures and credentials. Use synthetic data or data explicitly permitted for this task. Supply credentials through the authorized access mechanism; a reference can be retained without exposing the secret itself.

Decide which information may be discarded, which must be retained, and what a reconstruction is expected to restore. If continued use depends on preserved data, obtain the relevant recovery result through SYSE.34 or the qualified storage Method. Recreating an empty database does not satisfy a promise to restore its former contents.

#### SYSE.33:4.3 - Choose a creation and change mechanism

Compare a controlled push procedure with a pull-and-reconcile arrangement for the actual resources and operating conditions. A push procedure can be adequate for a bounded short-lived test environment. Continuous reconciliation may help where drift and continuing desired state are material. Neither choice removes the need to observe the resulting environment.

The [OpenGitOps v1.0.0 principles](https://opengitops.dev/) supply a specific line: versioned declarative desired state, automatic retrieval and continuing attempts to reconcile observed state. Use it where those conditions fit. Do not infer successful convergence from a committed declaration or an agent's presence.

For either mechanism, define the operation's bounded target, permitted changes and behavior after partial completion. Know how to identify resources already created by an attempt. Repeat a step only when its replay behavior is qualified; a repeated creation request must not silently create a second independently chargeable or stateful resource.

#### SYSE.33:4.4 - Provide isolation, lifetime and assistance

Give each independent attempt enough isolation to protect the meaning of its work. This may concern files, database rows, queues, network names or whole resources. Shared use is possible when the interference conditions are understood and controlled.

Set an appropriate lifetime and an actual holder for maintenance, assistance and disposition of retained information. A temporary environment must not disappear in the middle of promised work merely because a default expiry was reached. Conversely, indefinite retention of unused environments consumes resources and can preserve unnecessary access.

Limit cleanup to the resources and data actually owned by that environment and authorized for removal. If ownership or retained-data consequences are uncertain, return the uncertainty before deleting. A broad naming convention alone is not proof that every matching resource belongs to the current attempt.

#### SYSE.33:4.5 - Exercise clean creation, change and partial failure

Create an environment from the retained description without relying on the original machine's hidden setup. Observe the actual resources, effective configuration and dependency reachability, then run the representative task. A successful provisioning job without the task result establishes less.

When the arrangement promises configuration change, change one relevant configuration and verify both the intended new condition and the continuing task. If a manual intervention was needed, either make its necessary effect part of the supported procedure or identify the still-manual dependency. Do not let a reconciler and an unrecorded repair repeatedly undo each other.

Exercise a consequential partial-creation failure. Recover the actual effects before retrying, then reconcile, remove or retain them under the applicable permissions and data conditions. An unavailable observation leaves partial state unknown; it does not mean nothing was created.

Return the description/procedure, actual exercised environment, supported task and conditions, lifetime/support arrangement, and any remaining gap. Existing configuration and operating records can carry these facts.

#### SYSE.33:4.6 - Choose a fidelity boundary and make reconstruction converge

Construct the environment from the question the task must answer. For each interaction that could change that answer, choose whether the task needs the actual dependency, a controlled substitute or no dependency at all. A substitute is adequate only for the behavior it represents. An in-memory data store can make a transformation test fast while omitting collation, isolation or persistence behavior that a migration test needs. Identify those omitted questions and send them to the environment that can exercise them; do not require production duplication for a test whose answer does not depend on it.

Develop supported environment profiles when several tasks share the same consequential conditions. Each profile states what its users may infer: for example local functional feedback, real-database integration, or representative performance. Generate these profiles from shared configuration where feasible, but retain their intentional differences. A single universal environment can become slow and expensive; uncontrolled differences between ad hoc environments can invalidate comparisons. The deciding question is which differences affect the receiving claim.

Treat reconstruction as convergence from a known starting condition. Establish how the mechanism identifies an existing resource, inspects its actual state and chooses create, change, leave, or stop. Declarative desired state is useful only when those operations are supported for the relevant resource and state. A tool's state record can help associate resources with requests, but it is not the resource itself. If the record is lost while the resource survives, recover that association before creating another resource with the same business purpose.

Choose how to handle drift. Replacing a disposable worker is often simpler than understanding every manual change it accumulated. A shared stateful dependency may require an in-place repair that retains information and service continuity. Reconcile only what the mechanism actually owns. When emergency work deliberately changes a managed value, either adopt the new intended value through the supported change path or restore the former value after mitigation; two competing controllers must not keep undoing one another. Continuing reconciliation adds value when ongoing drift matters; an observed one-shot construction is sufficient for many short-lived tests.

Information and access make this more than infrastructure recreation. A usable retained-data environment needs a recoverable data source, a restore/import procedure, compatible schema and a way to verify the required state. Credentials need valid scope and availability at use time. Provisioned capacity needs to last through the promised task. A description that reconstructs machines but cannot obtain one of these prerequisites should still be retained, with the blocked task made explicit.

In a changed ParcelWorks use, a fast local substitute treats text comparison differently from the production database. Keep it for pure split/join feedback whose contract is unaffected. Move the persistence comparison to a profile using the relevant database semantics, and include the differing text case. If the new purpose is a latency guarantee, neither profile is sufficient merely because it uses the right database version: reproduce or justify the relevant load and resource envelope through SYSE.40. The action changes with the test question, while independently useful environments remain usable.

### SYSE.33:5 - Archetypal Grounding

In a constructed ParcelWorks example, address-service tests pass on a developer's machine but fail on a shared worker. Two causes are suspected: an unrecorded runtime version and tests that overwrite the same address row.

The team defines a bounded integration-test environment t7. Its description identifies the application artifact, runtime image, compatible database version, required text-handling settings, synthetic address fixtures and authorized test-service access reference. Each independent attempt gets its own fixture namespace. Production data and production credentials are outside this environment's permission.

For the normal construction, the provisioner creates the named resources and loads the synthetic fixtures. The test reads and changes an address containing a line separator, then checks the exact resulting display text. The team observes the effective runtime/database conditions rather than assuming that the description was applied. A fresh t8 can exercise the same task without copying the developer's home directory or t7's mutable fixture state.

The relevant equivalence is the qualified behavior and conditions, not equality of t7 and t8's resource identifiers. A later performance claim would need a new qualification of capacity and load; this successful functional test does not supply it.

The team next changes the configured test-service endpoint from one authorized sandbox to another. The environment's effective configuration and dependency test must reflect the new endpoint. If the desired file changes but the running process retains the old value, the change is not complete.

| Adverse observation | Correct interpretation | Bounded response |
| --- | --- | --- |
| Creation times out; lookup finds the worker but no database. | The attempt partially took effect. | Reuse the identified worker and create the missing database only under qualified replay conditions. |
| Lookup itself is unavailable. | Resource state is unknown. | Restore observation or obtain assistance before another potentially duplicating creation. |
| The database exists but the fixture-loading permission is absent. | Infrastructure exists; the test environment is not usable for its named task. | Return the permission gap. |
| A declaration requests the new endpoint, but the process uses the old one. | Desired and actual state differ. | Repair the application/reconciliation step and re-exercise the dependency. |
| An old test database contains retained results needed by a user. | “Temporary” does not establish permission to discard those results. | Resolve their disposition before cleanup. |

For this short-lived use, the team selects a controlled creation procedure with explicit observation rather than installing a permanent reconciliation service. Another environment with continuing drift could reasonably make the other choice. The test's result, failure recovery and data limits govern that decision.

What changes in practice is that the next person can construct and exercise the required conditions, or see the missing prerequisite, without inheriting an unexplained machine.

### SYSE.33:6 - Bias-Annotation

A familiar workstation can become an accidental standard, while a production-like environment can be assumed necessary for every task. Inspect which conditions actually affect the question. Automation can also make provision failures less visible by reporting success before access, fixture loading or a dependent service has been exercised.

### SYSE.33:7 - Conformance Checklist

- The environment is defined for a named task and an appropriate equivalence criterion.
- Desired configuration, actual resources, persistent information and access are distinguished.
- Hidden setup is removed from the supported creation path or exposed as a remaining dependency.
- Isolation and shared-state conditions preserve the meaning of independent attempts.
- Clean creation and consequential partial failure have usable responses; relevant configuration changes are qualified when that capability is promised.
- A real task result, not only provisioning completion, supports readiness for the stated use.
- Cleanup respects resource ownership, retained information and actual permission.

### SYSE.33:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| Clone the one working machine indefinitely. | Recover required conditions and exercise a clean construction. |
| Declare the environment in Git and report it ready. | Observe actual state and run the named task. |
| Treat infrastructure recreation as data restoration. | Obtain and exercise the separate information-recovery procedure. |
| Retry all creation after timeout. | Recover partial effects and repeat only qualified operations. |

### SYSE.33:9 - Consequences

Reconstructible environments can reduce hidden dependencies and make failures easier to compare. They require maintained descriptions, controlled fixture/access arrangements and attention to partial effects. Isolation can increase cost; excessive fidelity can slow feedback without improving the question being tested.

### SYSE.33:10 - Rationale

An environment serves a task through actual conditions, not through a description alone. Separating desired state, observed provision and information retention makes both successful reconstruction and a precise missing prerequisite possible. The same separation prevents automation from overstating recovery.

### SYSE.33:11 - SoTA-Echoing

For repeatable environment provision, **adapt** the shared-procedure and configuration practices in [DORA Deployment automation](https://dora.dev/capabilities/deployment-automation/) and the [Continuous Delivery pipeline](https://continuousdelivery.com/implementing/patterns/). Those approaches already treat environment variation as an engineering concern. Sections 4.5–4.6 derive the necessary fidelity from the task instead of requiring either a universal production clone or unrelated local setups.

**Adopt and adapt** [OpenGitOps v1.0.0](https://opengitops.dev/) when ongoing pull and reconciliation answer the drift problem. Compare it with a controlled one-shot or push procedure: continuing controllers can maintain desired state but add responsibility and need a clear ownership boundary. Both arrangements still need actual usable data, access and observed convergence for their promised task.

Reopen the profile or provision mechanism when provider behavior, dependency semantics, data permissions, expiry or the receiving task changes. Infrastructure reconstruction alone does not establish information restoration or performance under a new resource envelope.

### SYSE.33:12 - Relations

SYSE.26 supplies the supported practitioner path, SYSE.30 supplies recoverable builds, and SYSE.31 consumes credible test conditions. SYSE.13 identifies configuration; SYSE.34 supplies persistent-data compatibility and recovery. SYSE.41 performs the actual application deployment when that is the missing result. SYSE.29 governs migration or retirement of an environment path.

### SYSE.33:End
