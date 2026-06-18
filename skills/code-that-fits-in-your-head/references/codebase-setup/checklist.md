# Codebase Setup Checklist

Use when setting up a new code base, or auditing an existing one for baseline discipline. Designed as a read-do checklist: read an item, do it, move on. For an existing code base, switch to do-confirm and ideally run it with a second person.

## Before You Start

- [ ] You have a directory where the code base will live.
- [ ] You have (or can install) the language toolchain (compiler, package manager).
- [ ] You have (or can get) access to a CI service — self-hosted or cloud.
- [ ] You know the target deployment environment (or at least a pre-production stand-in).

## New Code Base — Top-Level Checklist

The canonical three-item list. Each item expands below.

- [ ] Use Git.
- [ ] Automate the build.
- [ ] Turn on all error messages.

## 1. Initialise Git

- [ ] Run `git init` in the project directory.
- [ ] (Optional) Add an empty initial commit: `git commit --allow-empty -m "Initial commit"`.
- [ ] Add a `.gitignore` appropriate to the language/toolchain.
- [ ] Confirm you can use Git from the command line (not just a GUI).
- [ ] (Later, not blocking) Connect to a remote host (GitHub, GitLab, etc.).

## 2. Scaffold the Minimum Application

- [ ] Use a wizard, scaffolding tool, or CLI (e.g. `dotnet new`, `npx create-*`) to generate a minimal runnable app (the "shell").
- [ ] Confirm the app runs locally and produces observable output (e.g. "Hello World").
- [ ] Commit the generated code to Git.

## 3. Automate the Build

- [ ] Create a build script at the repo root (e.g. `build.sh`, `build.ps1`).
- [ ] Script invokes the language's build tool (e.g. `dotnet build --configuration Release`).
- [ ] Script targets the **Release** configuration (matches production).
- [ ] Script is executable and runs cleanly on a fresh checkout.
- [ ] Commit the build script to Git.

## 4. Turn On All Error Messages

- [ ] Turn on **warnings as errors** in the build configuration.
- [ ] Apply the setting to **every build configuration** — Release AND Debug (or equivalent).
- [ ] Enable language-level static analyser / linter with the default or recommended rule set.
- [ ] Enable strict language features (e.g. C# nullable reference types, TypeScript `strict: true`).
- [ ] Run the build and confirm it still passes.
- [ ] If warnings appear: fix them immediately (there is almost no code yet).
- [ ] Commit the configuration change.

## 5. Wire Up a Deployment Pipeline

- [ ] Choose / provision a CI service.
- [ ] Configure the CI pipeline to run the build script on every push to mainline.
- [ ] Configure deployment to a pre-production environment on green builds.
- [ ] (If feasible) Configure deployment to production, gated on a manual sign-off.
- [ ] Confirm a full push → build → deploy cycle works end to end.

## Existing Code Base — Ratchet Checklist

Use when retrofitting checks onto a legacy project. Never flip everything at once.

### Survey

- [ ] List the libraries / packages / projects in the code base.
- [ ] Run the compiler; capture every warning.
- [ ] Run any available linter / analyser; capture every warning.
- [ ] Group warnings by type and by library.

### Pick a Slice

- [ ] Pick one library.
- [ ] Pick one warning type with a manageable count (around a dozen).
- [ ] Read the online documentation for that warning to understand the motivation.

### Fix and Flip

- [ ] Fix every instance of that warning in the chosen library.
- [ ] Commit incrementally as fixes are grouped logically.
- [ ] Merge into mainline.
- [ ] Flip that warning to **error** so it cannot regress.
- [ ] Commit the configuration change.

### Repeat

- [ ] Apply the same warning type to the next library, OR pick a new warning type in the same library.
- [ ] For opt-in strict features (e.g. nullable reference types), enable file-by-file or project-by-project.
- [ ] Apply the Boy Scout Rule on every unrelated change.

## Audit-Mode Quick Check

Use on an unknown repo to judge baseline discipline in under five minutes.

- [ ] Is there a `.git` directory at the root?
- [ ] Is there a build script committed at the root (or documented entry point)?
- [ ] Is the build script configured for Release?
- [ ] Is warnings-as-errors on in the build config?
- [ ] Is there a linter / analyser configuration committed?
- [ ] Does `git log` show an initial commit near the project's inception (not retroactive)?
- [ ] Does the CI config exist (`.github/workflows`, `.gitlab-ci.yml`, `azure-pipelines.yml`, etc.)?

## Red Flags

Stop and address if you find:

- No version control.
- Build only runs inside a specific IDE, with no script alternative.
- Hundreds of compiler warnings in the build log (checklist was skipped).
- Warnings-as-errors on in Release but off in Debug (or vice versa).
- No CI — every deployment is a human copying files.
- A project that started months or years ago with no history of incremental ratcheting.

## Quick Reference

| Aspect | Ideal | Acceptable | Red Flag |
|--------|-------|------------|----------|
| Version control | Git, initial commit on day 1 | Git added retroactively | No VCS |
| Build | Scripted, Release, runs locally and in CI | Scripted but only runs in CI | IDE-only build |
| Warnings | Zero, as errors in every config | Zero, as errors in Release only | Hundreds accumulated |
| Analyser/linter | Enabled with rule set committed | Available but not wired to build | Not installed |
| CI/CD | Push → build → deploy automated | Push → build only | No CI |
| Legacy migration | Ratchet in progress, visible in history | Not started but planned | "We'll get to it" |
