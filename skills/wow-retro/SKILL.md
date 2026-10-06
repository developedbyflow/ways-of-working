---
name: wow-retro
description: "Close the loop after a task, a week or a quarter: improve the page and CLAUDE.md, compare estimate and actual, write the impact log; each quarter, CV bullets, STAR stories and career tracker evidence. Use when the user runs /wow-retro, or at the end of another wow skill."
argument-hint: "[task | week | quarter]"
---

# Retro

1. Read `${CLAUDE_SKILL_DIR}/../../SKILLS.md`. It says how every wow skill behaves; follow it for the whole run.
2. Read `${CLAUDE_SKILL_DIR}/../../retro.md`. It is the process: its steps, its STOPs, its "Done when" and its "Next".

The mode is the first word of the input when it is `task`, `week` or `quarter`. Otherwise the mode is task, and the whole input says what to look at or change.

The impact log path is in the personal settings (see `SKILLS.md`). If the file doesn't exist yet, create it with the title `# Impact log`.

The user's input: $ARGUMENTS
