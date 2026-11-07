## SYSE.30 - Make Software Builds Repeatable and Traceable

> **Status:** Stable

> **Normativity:** Guidance within the stated software-engineering use; examples are illustrative.

### SYSE.30:1 - Problem frame

Use this pattern when two builds of “the same source” produce unexplained differences, a package cannot be rebuilt after a worker disappears, or nobody can recover which inputs produced a tested artifact. Start with one required output and one actual build attempt. Recover its source, resolved dependencies, instructions, toolchain and environment before interpreting a source label as a complete build identity.

The result is a repeatable build procedure and an input/output account, or a precise uncontrolled input that prevents that result. In Software Platform Engineering this makes later test and artifact claims refer to recoverable bytes. It does not prove that those bytes behave correctly or came from a trustworthy builder.

If the needed artifact already exists and the task is to transfer that exact artifact, use SYSE.32. If separately developed changes still need integration into a checked mainline, use the direct CI source route in SYSE.31; reproducible isolated branches are not an integrated application.

### SYSE.30:2 - Problem

A source revision omits many influences on a build: dependency resolution, generated inputs, tool versions, platform defaults and ambient state. “Run the same command again” can reuse yesterday's output or resolve a different dependency today. The command may succeed in both cases without reproducing the claimed artifact.

Without an explicit output and comparison criterion, a team can also confuse repeatable execution, equivalent behavior and byte identity. Each supports a different later use.

### SYSE.30:3 - Forces

| Force | Practical tension |
| --- | --- |
| Reconstruction | Recording more inputs helps recovery; irrelevant detail increases maintenance and hides the inputs that actually change output. |
| Fast builds | Caches reduce delay but can hide an undeclared dependency or a build that never ran. |
| Byte identity | Strict comparison detects unexplained variation; some outputs deliberately contain separately varying operational information. |
| Availability | Pinned inputs stabilize meaning, but a version name is not enough when its bytes later disappear. |

### SYSE.30:4 - Solution

#### SYSE.30:4.1 - Fix the output and the claim

Name the artifacts needed by the next consumer: for example an executable package and its dependency bundle. Distinguish them from build logs and other ancillary results. State whether the current need is to repeat the procedure, explain provenance, compare functional behavior, or reproduce the specified artifacts byte for byte.

Use the Reproducible Builds meaning of a reproducible build only for the byte-identical specified artifacts under the declared source, environment and instructions. If a comparison deliberately ignores selected metadata, state that narrower equivalence and why it is enough for the receiving use; do not report the same result as byte reproducibility. Do not exclude a differing file merely to make the result pass.

#### SYSE.30:4.2 - Recover what the build actually consumed

Begin with the source revision and any uncommitted or generated input included in the attempt. Recover the exact build instructions, resolved dependency versions and content identities, toolchain, build configuration and relevant environment conditions. A dependency declaration and the dependencies actually resolved are separate evidence.

Inspect influences that can change the selected output: local files, network downloads, compiler flags, environment variables, locale, paths, timestamps, random values and ordering. Remove an irrelevant influence when the operation permits it; otherwise control or record it. A container image can help identify a toolchain without describing every relevant host or external-service condition.

Retain the inputs or a usable authorized acquisition route for the intended reconstruction interval. A recorded URL that no longer supplies the identified bytes is a recovery gap. Reuse existing build metadata and configuration records when they answer these questions; no particular manifest format is required.

#### SYSE.30:4.3 - Construct one controlled execution

Turn the recovered instructions into an executable procedure with explicit inputs and outputs. Start in a clean workspace and obtain the named inputs. Prevent an undeclared local file or an unbounded “latest” dependency from silently changing the result. Keep secrets outside public logs and use the authorized access mechanism.

Treat caches according to their role. An identified dependency cache can supply a known input; an old final package cannot demonstrate that the present build procedure works. For the reconstruction check, execute the relevant build work rather than copy a previously produced output. If complete isolation is expensive, state which remaining influences are controlled, observed or unresolved.

Bind the resulting artifact identities to the actual input set and execution. SYSE.13 supplies configuration identity. A successful exit without the promised output is not successful construction.

#### SYSE.30:4.4 - Compare independent repetitions and explain differences

When the receiving use needs reproducibility, repeat from the identified inputs in a fresh execution. Where the claim includes transfer between builders, use the relevant independent builder or environment, not just a second invocation on the same dirty worker.

Compare the specified output bytes, commonly through a suitable cryptographic digest followed by a useful difference inspection when they differ. Change one suspected influence at a time when that can discriminate the cause. Explain the variation before accepting an equivalence claim.

For incidental build timestamps, prefer removing them from the specified artifact or deriving a needed date from the named source. Retain actual execution time in separate build evidence when it is needed. A tool-specific fixed-date mechanism works only where the selected tool supports it; changing a clock globally can affect behavior that depends on elapsed time. Rebuild and compare after the repair.

A matching pair is bounded evidence, not proof against every future environment. If a dependency, toolchain or output requirement changes, qualify the affected build again. Preserve a useful partial result: “the build runs from these inputs, but archive order remains uncontrolled” is more informative than “reproducible” with an unexplained exception.

#### SYSE.30:4.5 - Return the right result to the next use

Return the procedure, recoverable input identities, specified artifacts and the comparison result with its conditions. Return an explicit missing input or unexplained difference when that is the honest result.

Behavioral tests consume this artifact through SYSE.31. Artifact authenticity, trust expectations and promotion use SYSE.32. Actual runtime installation uses SYSE.41. None of those results is established by a build digest. Identify a package rebuilt for another environment and compare its bytes with those of the previously tested artifact before deciding which earlier evidence remains applicable.

#### SYSE.30:4.6 - Turn an inherited build into a maintainable construction

The practical starting point is often one working developer command, not an empty build system. Follow that command backward from the promised package. For each generated file, determine whether it is deliberately supplied as an identified input or produced by this build. Recover the producing actions for the latter; for each action, identify the files, tools and parameters that can affect its result. Continue until the remaining inputs are deliberately supplied source, acquired dependencies or declared environment conditions. This forms a build dependency graph: an edge says that one action needs another's output, not merely that it happened later in a log. A generated header copied from a colleague's machine must be accounted for through its producing action or as an identified supplied input obtainable for reconstruction; compilation success alone does not settle this.

Use the graph to decide what to control. A font compiler that downloads an unspecified font while building has an acquisition dependency. Obtain an identified permitted font first and provide it as an input, or retain the network dependency and its reconstruction limitation. A generator that reads the operator's home directory has an ambient dependency: either make the required setting explicit or remove that read. Do not place credentials in the dependency archive; retain the authorized way to obtain the identified private input and the fact that future access is a reconstruction condition.

Separate input acquisition from transformation where that makes the construction more inspectable. Run the transformation with only the chosen input set and necessary services available, then inspect a failure for a genuinely missing prerequisite. A strict sandbox is useful for exposing hidden reads, but a successful sandboxed invocation is not a proof of deterministic output. A container can fix a user-space toolchain while still sharing a kernel or depending on a remote generator. Choose these controls for the actual claim instead of treating one packaging technology as a guarantee.

The same account governs caching and parallelism. A reused intermediate result must correspond to the relevant action, input contents, toolchain and effective parameters. If its lookup key ignores a compiler option that changes output, the cache can return a package that no action in this attempt produced. Independent actions may run together when their inputs are ready and they do not communicate through an unmodelled scratch file or mutable service. A build system can schedule a graph efficiently only to the extent that its declarations represent the actual dependencies.

When two clean builds disagree, locate the first differing intermediate result rather than rewriting all controls. Compare its inputs and execution influences, repair the contributing action, then rerun the affected downstream construction. When intermediates match but the final archive differs, examine the packaging action, including member ordering, file attributes and embedded signatures. If signing intentionally introduces fresh values, define a separately reproducible payload and a separately verified signed envelope before using that distinction; it does not make the entire signed file byte-identical.

A practical qualification uses the variations the promise covers: a fresh workspace without final-output cache, another supported worker, and relevant differences such as path, locale or time. Deliberately change a real input as well: the new build must consume it rather than return a stale cached result. Keep a periodic reconstruction or an input-retention check only when it protects a real future use. The ordinary delivery path can reuse an already qualified artifact; reconstruction capability and artifact promotion solve different problems.

For example, a reporting tool generates a parser from a grammar, compiles it with a library, and packages the executable with templates. An inherited build tracks only the source files. The recovered construction adds the grammar generator, grammar, library bytes and template contents to their actual consuming actions. A template-only change need not regenerate the parser, but it must change or revalidate the packaged result. If an upgrade changes the generator's output, earlier parser tests cannot be inherited solely because the hand-written source stayed unchanged. This reasoning applies to another language or build tool without assuming that its cache or dependency scanner is already correct.

### SYSE.30:5 - Archetypal Grounding

In a constructed ParcelWorks case, the developer supplies service revision r17 and asks for the package that will be tested. Two workers report successful builds with different package digests. Both claim r17. The team first names the service package as the reproducible artifact; the execution log is separate evidence.

Inspection recovers build recipe b3, dependency set d9 and runner image i7 from both attempts. The package contains the same service files but also a generated line, “built at 10:02” in the first attempt and “built at 10:07” in the second. The source label was correct but incomplete: wall-clock time changed a specified output.

The application does not use that line for business behavior, and exact execution time is needed only for diagnosis. The team removes the line from the package and retains it in the separate build evidence. A required source-version label remains r17. Two fresh executions of the repaired recipe, with the same d9 and i7, produce identical specified package bytes. The result names that tested input set and comparison.

Now change the case: a dependency named “stable” resolves to different bytes on the second worker. Removing the timestamp cannot repair this difference. The next result is the exact unresolved dependency identity and a bounded acquisition/pinning repair. If the original bytes cannot lawfully be obtained, exact reconstruction remains unavailable even though a newer package could be built and tested as a different candidate.

A third case reuses the first worker's final package from cache. Matching digests prove that the same cached bytes were returned, not that the procedure reconstructed them. A fresh execution is still needed for the reconstruction claim.

What changes in practice is the next debugging question. Instead of debating whether r17 is “the same version,” the team can identify which input changed, which artifact was tested and which claim the comparison actually supports. A later test failure still requires behavioral investigation.

### SYSE.30:6 - Bias-Annotation

Successful builds on a familiar worker can hide dependence on its local state. A focus on byte equality can also distract from malicious or incorrect but deterministic output. Include the environment transfer relevant to the real use, and keep correctness and builder trust as separate questions.

### SYSE.30:7 - Conformance Checklist

- The specified output and comparison criterion are explicit before differences are judged.
- Actual source, resolved inputs and relevant environment are recoverable, not merely declared.
- The procedure produces the named output from a clean execution under stated conditions.
- A reconstruction check does not substitute a cached final artifact for execution.
- Differences are explained or returned as a bounded gap; ignored metadata is not silently removed from the claim.
- Correctness, authenticity, mainline integration and deployment remain separate results.

### SYSE.30:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| A source commit is treated as the complete build input. | Recover resolved dependencies, generated inputs and relevant environment conditions. |
| Two successful exits are called reproducibility. | Compare the specified outputs under an explicit criterion. |
| A build report names an available version but its bytes cannot be recovered. | Preserve the identified input or state the unavailable reconstruction dependency. |
| Equal digests are accepted as proof of safe software. | Use the separate behavior and trust questions for the actual artifact. |

### SYSE.30:9 - Consequences

Differences become diagnosable and tested bytes remain identifiable. Controlled inputs and retention cost storage, maintenance and sometimes build speed. Apply stronger reconstruction controls when the receiving claim needs them; transferring an already verified artifact should not force a needless rebuild.

### SYSE.30:10 - Rationale

A build is an operation over more than a source-tree name. Recovering its actual inputs closes a practical explanation gap, while an explicit output criterion prevents a weaker comparison from being reused as a stronger result. Independent reconstruction and artifact trust then contribute different evidence.

### SYSE.30:11 - SoTA-Echoing

For constructing recoverable builds, **adopt** the specified-input and byte-comparison criterion in the [Reproducible Builds definition](https://reproducible-builds.org/docs/definition/), with its [environment recording](https://reproducible-builds.org/docs/recording/) and [timestamp](https://reproducible-builds.org/docs/timestamps/) treatments. **Adapt** the isolation reasoning in [Bazel Hermeticity](https://bazel.build/basics/hermeticity/) without requiring Bazel. These professional approaches already address hidden dependencies and nondeterminism.

The construction here connects the chosen build claim to an inherited dependency graph, cache reuse, diagnosis of differing intermediates and the downstream tested artifact. A hermetic execution and a byte-reproducible result answer different questions. A retained artifact is often the economical delivery input; independent reconstruction costs additional execution and input retention and is selected for the claim that needs it.

Reopen the affected construction when a required input disappears, a toolchain or generator changes, an independent builder disagrees, or the receiving use needs another output/equivalence claim.

### SYSE.30:12 - Relations

SYSE.13 supplies configuration identity. SYSE.31 constructs meaningful feedback and exposes the exact continuous-integration Method when a shared-mainline result is missing. SYSE.32 verifies artifact-specific trust and promotion; SYSE.33 supplies reconstructible development/test conditions; SYSE.41 performs actual deployment. SYSE.4 governs reliance on the resulting evidence for a named engineering claim.

### SYSE.30:End
