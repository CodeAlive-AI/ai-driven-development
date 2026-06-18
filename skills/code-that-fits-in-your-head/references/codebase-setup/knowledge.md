# Codebase Setup Knowledge

Core concepts for setting up a new code base (or retrofitting one) with discipline from the first line of code.

## Overview

Setting up a code base correctly means establishing version control, an automated build, and strict error checking *before* any meaningful code is written. Checklists make these steps reliable. A checklist is an aid to memory, not a bureaucratic control — it lets skilled practitioners focus on hard problems by offloading the trivial-but-important steps.

## Key Concepts

### The Checklist Principle

**Definition**: A checklist is a simple list of items covered in a few minutes at pause points in a task.

It is *not* a complex flowchart with detailed instructions. Its purpose is to prevent skipped steps, not to audit or restrict the practitioner.

**Key points**:
- Checklists originated in 1935 with the B-17 bomber, after an experienced test pilot crashed it because the plane was "too much airplane for one man to fly."
- The goal: *improve outcomes with no increase in skill*.
- Checklists empower experts; they don't constrain them.
- The most powerful checklists are those that leave *no* audit trail — they exist to be used in the moment, not to document compliance.

### Cognitive Offloading

**Definition**: Freeing working memory by externalising trivial-but-important steps to a written list.

When a task is complex, it is almost inevitable that you forget to consider one thing or two. A checklist lets you stop trying to remember the trivial and focus on the hard parts.

**Key points**:
- You don't have to make an effort to remember — you just have to remember to *refer to the checklist* at pause points.
- The problem is rarely that you don't know how to do something; it is that you *forget* to do it, even knowing you should.

### Read-Do vs Do-Confirm

**Definition**: Two formats for running a checklist.

- **Read-do**: Read each item, then immediately perform the action before moving to the next.
- **Do-confirm**: Do all the things from memory, then run through the list to confirm you did them.

**Key points**:
- Imperative-worded lists ("Use Git", "Automate the build") naturally suggest read-do.
- Do-confirm should be run with at least one other person. Pilots do this: one reads, the other confirms. Alone, it is too easy to skip a step — a copilot keeps you honest.

### Automated Checks as Automated Checklists

**Definition**: Compilers, linters, analysers, and warnings-as-errors are machine-enforced checklists that run every build.

Every time these tools run, they control for thousands of potential issues — work no human would do line by line.

**Key points**:
- Most languages ship with these tools; they are rarely wrong.
- Suppressing false positives is cheap; walking away from the tools is expensive.
- "The future is unevenly distributed" — many of these tools have existed for decades but are underused.

## Why Do It On Day 1

Retrofitting discipline onto a large code base is a formidable task. Setting it up when the code base is *empty* costs almost nothing:

- Zero code means zero existing warnings to triage.
- Zero code means no deployment pipeline to untangle.
- Each new warning can be dealt with the moment it appears — one at a time, while the context is fresh.

The moment you postpone, the cost rises non-linearly.

## Terminology

| Term | Definition |
|------|------------|
| Checklist | A short list of trivial-but-important items, covered in minutes at pause points. |
| Read-do | Read item, do item, move on. |
| Do-confirm | Do everything, then verify against the list (ideally with a partner). |
| Walking Skeleton | The thinnest possible slice of real functionality that can be built, deployed, and tested end-to-end. |
| Shell | An even thinner step: a wizard- or scaffolding-generated app, committed and deployed before the Walking Skeleton. |
| Warnings-as-errors | Compiler option that fails the build on any warning — prevents warning accumulation. |
| Analyser / Linter | Automated tool that flags code smells, naming issues, security and performance problems. |
| Boy Scout Rule | Leave the code in a better state than you found it. |

## Common Misconceptions

- **Myth**: Checklists are for unskilled workers; experts don't need them.
  **Reality**: Surgeons and airline pilots use checklists specifically *because* they are experts. Skill and memory are different things.

- **Myth**: A checklist is a bureaucratic compliance document.
  **Reality**: The most effective checklists leave no paper trail. They exist to be used, not audited.

- **Myth**: Turning on all warnings will just slow the team down.
  **Reality**: Seven warnings today are easier to fix than hundreds of warnings in six months. The illusion that code is maintainable without discipline is what gets upset, not real productivity.

- **Myth**: You can't add strict checks to a legacy code base.
  **Reality**: You can. Turn checks on one library, one rule, and one warning category at a time (the ratchet).

## Quick Reference

| Concept | One-Line Summary |
|---------|-----------------|
| Checklist | Aid to memory for trivial-but-important steps. |
| Read-do | Do each item as you read it. |
| Do-confirm | Do, then verify — preferably with a partner. |
| Improve outcomes, no extra skill | The entire point of a checklist. |
| Day 1 setup | Cheapest possible moment to enforce discipline. |
| Gradual ratchet | Only viable path for legacy code bases. |
