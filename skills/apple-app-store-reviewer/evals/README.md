# Skill evaluations

Run each case in a clean agent context twice: once with this skill and once without it (or against a frozen previous version). Save generated artifacts, timing, assertion grades, and human feedback in a separate workspace; do not write run outputs back into the skill directory.

The deterministic fixtures in `tests/` make mechanical assertions reproducible. Assertions involving judgment—such as whether a screenshot is misleading or an AI wrapper has meaningful native value—must cite concrete output evidence and receive human review.
