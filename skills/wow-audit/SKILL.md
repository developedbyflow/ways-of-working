---
name: wow-audit
description: "Audit one area of an existing app (security, privacy, performance, accessibility, seo, ux, analytics, testing, dx, production-readiness, cost, architecture): tools, manual checks, findings with what breaks, the user's decisions, numbers before and after. Use when the user runs /wow-audit, or agrees to a hand-off to it from another wow skill."
argument-hint: "[area]"
---

# Audit

1. Read `${CLAUDE_SKILL_DIR}/../../SKILLS.md`. It says how every wow skill behaves; follow it for the whole run.
2. Read `${CLAUDE_SKILL_DIR}/../../audit.md`. It is the process: its steps, its STOPs, its "Done when" and its "Next".

The area is: $0

Also read `${CLAUDE_SKILL_DIR}/../../audits/$0.md`. If the area is empty or has no file, list the areas from `audit.md` and ask which one (STOP).

The user's input: $ARGUMENTS
