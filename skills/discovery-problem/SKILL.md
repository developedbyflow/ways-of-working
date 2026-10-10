---
name: discovery-problem
description: "Discovery, step 01: who has the problem, what it is, how they solve it today and what it costs them, checked on 3–5 people. Use when the user starts a new app or product and has an idea, before market research and before any code."
argument-hint: "[the idea, in a few words]"
---

# Discovery · 01 Problem

## When to use it
The first step of any new product, before any code.

## The problem it solves
You know who you build for and what hurts them, so every later decision has a reason.

## Steps
Ask one question at a time and wait for the answer. Write the file from the user's answers; never invent one. If an answer is vague, push back once before moving on.

1. **Who?** One concrete person: age, situation, what they want. Starting with yourself is fine; say so.
2. **What problem?** What they can't do today, without a solution in it. Feature ideas that come up go to `docs/ideas.md`, each with a stable ID (F-01, F-02…), not discussed.
3. **How do they solve it today?** Each alternative (an app, a spreadsheet, a person, nothing), with what it does well and where it fails. A workaround they built themselves is the strongest sign the problem is real.
4. **What does it cost them?** Time, money or results, in numbers. Approximate is fine, vague is not: "~30 minutes a day", not "a lot of time".
5. **The segment:** the wider group the person belongs to, one you can reach (for example "developers who want to lose weight").
6. **Check it on 3–5 people from the segment:** strangers or acquaintances, not friends being nice.
   - Write 5 questions about what they did, not about the idea: what they tried, what they use, why they stopped, how much time it takes, whether they ever paid. Start each with "Tell me about the last time you…" and note their pains in their own words.
   - Don't mention the idea until the end. Then ask for something real: an email for the beta.
   - 3 out of 5 describe the same problem → it's real. Fewer → change the who or the problem and check again, or drop it.
   - Not done yet? Mark it "not yet verified"; it becomes a test in the product brief.

Then write `docs/01-problem.md`:

```markdown
# 01 – Problem
**Who:**
**Segment:**
**Problem:**
**How they solve it today:**
- [alternative]: what it does well, where it fails
**What it costs them:**
## Verify with others
[verified / not yet verified], the 5 questions, the results
```

## The bad version and why not
- "For anyone who wants to eat healthy" → too vague to decide anything.
- Starting from the solution ("an app with AI") instead of the problem.
- Assuming everyone has your problem.
- Asking "would you use my app?" → almost everyone says yes to be nice. Only what they already did counts.

## What breaks if you skip it
You build features nobody uses.

## The principle behind it
Start from the problem, not the solution. You are not your user.

## How to apply it at work
Before any feature or ticket, ask: what problem does this solve, and for whom?

## Done when
- [ ] one concrete person and a reachable segment
- [ ] the problem has no solution in it
- [ ] today's alternatives, each with where it fails
- [ ] the cost in numbers
- [ ] checked on 3–5 people, or marked "not yet verified"
- [ ] feature ideas parked in `docs/ideas.md` with stable IDs

## Next
Discovery · 02 Market research (`/discovery-market-research`).
