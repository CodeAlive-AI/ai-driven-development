# Codebase Setup Rules

Concrete rules for initialising a new code base or tightening an existing one. These are hard rules: apply them unless you have a specific reason not to.

## Core Rules

### 1. Use Git From Line 1

Initialise a Git repository *before* writing any code.

- Run `git init` in the directory where the code will live.
- Do *not* wait to connect to a remote (GitHub, GitLab, etc.) — that can always come later.
- Apply this rule to any code base expected to live more than a week. The threshold for creating a repo should be low; you can always delete `.git` to undo.
- Optional: create an empty initial commit (`git commit --allow-empty -m "Initial commit"`). This makes rewriting history easier before publishing.
- Learn Git at the command-line level, not just through a GUI. Invest one or two days in the basics — it is trivial compared to learning a programming language.

### 2. Automate the Build From Line 1

Commit a build script that compiles (and later tests and deploys) the code, runnable by any developer on their machine.

- Create the minimal deployable application first (a "shell" from a wizard/scaffolding tool). Commit and deploy it *before* writing real functionality.
- Add a build script file (e.g. `build.sh`, `build.ps1`, `build.bat`) at the repo root and commit it.
- Configure the build script to produce a **Release** build — the automated build must reflect what goes to production.
- As build steps are added (tests, packaging, analyzers), add them to the script as well.
- The script is a low-friction tool: if it passes locally, it is OK to push.
- Start simple. Don't reach for a full-blown build tool (Cake, Nuke, FAKE, Gradle) unless the simple script demonstrably does not fit.

**Example — minimal `build.sh`**:
```bash
#!/usr/bin/env bash
dotnet build --configuration Release
```

### 3. Turn On All Error Messages (Warnings as Errors)

Treat every compiler warning, linter warning, and static-analysis warning as a build-breaking error.

- Turn on **warnings as errors** as one of the first things you do. On a new code base there is nothing to break.
- Apply the setting to **every build configuration** — Release *and* Debug. If your toolchain stores these per-config (e.g. Visual Studio), set both. Put "set both" on your checklist.
- Enable the language's static analysers / linters (in .NET: Roslyn analysers / FxCop successors).
- Turn on language features that improve static checking (e.g. C# 8 **Nullable reference types**) immediately, while there is no code to break.
- Treat the cost of addressing seven warnings today as far lower than hundreds later.
- False positives exist in linters; suppress them narrowly via the tool's options rather than disabling the rule.

### 4. Build the Deployment Pipeline Early

Once the build script works locally, wire it to a CI service and a deployment pipeline.

- Pushing to `master` (or the mainline) should trigger an automated pipeline that either deploys to production or leaves it one manual sign-off away.
- If you don't have a CI server, get one. Cloud-based services exist; the dollar cost is a small fraction of a programmer's salary.
- If you don't have a production environment yet, target a pre-production environment — preferably one that mirrors production's network topology. Use VMs or containers if hardware parity is not possible.

### 5. Apply the Gradual Ratchet to Legacy Code Bases

When retrofitting checks onto existing code, turn guards on one slice at a time — never all at once.

- Work library-by-library (package-by-package, project-by-project).
- Work **one warning type at a time**. Extract the existing warning list, group by type, pick a type with a manageable count (say a dozen), fix them all.
- Keep the warnings as *warnings* while fixing so the code continues to build. Commit incrementally.
- Once that type is at zero in that library, **flip it to an error** so it cannot regress.
- Repeat: pick another warning type, or apply the same type to another library.
- For nullable reference types (or equivalent opt-in features): enable file-by-file or project-by-project.
- Rule of thumb: Boy Scout Rule — leave each touched area cleaner than you found it.

### 6. Use Automated Gates as Cultural Armour

A machine-enforced rule is harder to override under delivery pressure than a human-held convention.

- When stakeholders push to "just ship it," a build that fails on warnings is a stronger answer than an opinion.
- Turn former human decisions into machine-enforced rules wherever possible.
- Use your judgment: in a healthy organisation, be open about the gates; in an unhealthy one, the gates can quietly protect engineering discipline. Do this for the good of the organisation, not personal agenda.

## Guidelines

Less strict recommendations:

- Prefer command-line interfaces for frequent operations (like Git day-to-day); prefer IDE wizards for rare operations (like creating a new project).
- Build scripts are more portable as POSIX shell (`build.sh`) but any script format is fine as long as it is committed and runnable.
- Read the online documentation for each analyser rule before suppressing it — most rules encode decades of accumulated knowledge.
- Don't show screenshots or step-by-step GUI instructions in documentation; they go stale fast.

## Exceptions

When these rules may be relaxed:

- **Truly ephemeral code**: A throwaway script you will delete within a week can skip `git init`. The threshold should still be low.
- **Large legacy migrations**: Don't block all work to reach zero warnings — follow the gradual ratchet instead.
- **Known-bad false positive in analyser**: Suppress the specific rule at the specific site, with a comment explaining why. Do not disable the analyser globally.

## Quick Reference

| Rule | Summary |
|------|---------|
| Use Git | `git init` before first line of code. |
| Automate build | Commit a build script; Release config; runnable locally. |
| Warnings as errors | Turn on, in every build config, on day 1. |
| Enable analysers/linters | Ship a baseline rule set; suppress false positives narrowly. |
| Enable strict language features | E.g. C# nullable reference types — turn on while code is empty. |
| Deployment pipeline early | CI wired to mainline; release or near-release on green. |
| Ratchet for legacy | One library, one warning type at a time; flip to error at zero. |
| Machine-enforced gates | Convert human conventions to build-breaking rules. |
