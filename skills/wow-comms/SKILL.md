---
name: wow-comms
description: "Write a status, risk, decision or incident message: the bottom line first, one ask with a date. Never sends it. Use when the user runs /wow-comms, or agrees to a hand-off to it from another wow skill."
argument-hint: "[status | risk | decision | incident]"
---

# Comms

1. Read `${CLAUDE_SKILL_DIR}/../../SKILLS.md`. It says how every wow skill behaves; follow it for the whole run.
2. Read `${CLAUDE_SKILL_DIR}/../../comms.md`. It is the process: its steps, its STOPs, its "Done when" and its "Next".

The format is: $0

If it is empty, ask which format (STOP).

The user's input: $ARGUMENTS
