---
name: discovery-brainstorm
description: "Discovery, optional step before 01: find a problem worth building for when you have no idea yet. 10 problems scored 1–5, one picked. Use when the user wants to build something but doesn't know what; skip it when they already have an idea."
argument-hint: "[a field or a group of people, optional]"
---

# Discovery · Brainstorm (optional)

## When to use it
Only when you want to build something and have no idea what. With an idea, go straight to `/discovery-problem`.

## The problem it solves
You pick a problem by comparing it with others, not the first one that comes to mind.

## Steps
Ask one question at a time and wait for the answer. The problems and the scores come from the user; you may suggest where to look, never fill the list yourself.

1. **Where to look:** problems you have yourself, problems of people around you, complaints in the reviews of existing apps, work people still do in spreadsheets or on paper.
2. **At least 10 problems, no judging.** Problems, not solutions: "planning meals for the week takes an hour", not "a meal-planning app". 20–30 minutes.
3. **Score each from 1 to 5** on:
   - how painful it is;
   - how often it happens;
   - whether you can reach those people;
   - whether you can build a first version alone in a few weeks.
4. **Pick one**, with the reason. The user decides; you only add up the scores.

Then write `docs/00-brainstorm.md`:

```markdown
# 00 – Brainstorm
| Problem | Pain | Frequency | Reach | Buildable | Total |
**Picked:** [problem], because [reason]
```

## The bad version and why not
- Writing solutions instead of problems ("an app that…") → you compare ideas, not needs.
- Stopping at the first idea → nothing to compare it with.
- Picking a problem you can't reach the people for → you can't check it in 01 or sell it later.

## What breaks if you skip it
Nothing, if you already have an idea. Without one, you pick by enthusiasm and find out at 01 that the problem is weak.

## The principle behind it
Many options first, then choose. Diverge, then converge.

## How to apply it at work
When a team asks "what should we build next?", list the problems first, score them together, then pick.

## Done when
- [ ] at least 10 problems, written without solutions
- [ ] each one scored on the 4 criteria
- [ ] one picked, with the reason

## Next
Discovery · 01 Problem (`/discovery-problem`), with the picked problem.
