---
name: saas-problem
description: "Discovery, step 01: who has the problem, what it is, how they solve it today and what it costs them, checked in 3–5 interviews about what people did, not about the idea. Use when the user starts a new app or product and has an idea, before market research and before any code. Also judges an existing problem page: /saas-problem validate <file>."
argument-hint: "[the idea, in a few words] or validate <file>"
---

# Discovery · 01 Problem

## When to use it
After `/saas-brainstorm`, with the problem picked there, before any code.

## The problem it solves
You know who you build for and what hurts them, so every later decision has a reason.

## How to run it
- **The bar:** do what a senior engineer or the C-level who owns this area (CEO, CPO, CTO, CFO, CMO, COO) at a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it, so the user learns it. Senior also means knowing what to leave out: say what you skip and why.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Every `docs/…` path below means that folder.
- **Spot risky assumptions for the user:** when a decision here rests on something nobody has checked ("I think people will…", "the AI can probably…") and being wrong would cost a lot, stop and propose a risk test: what to check, how long it takes, the pass mark, and when it must be done. The user only says yes or no; run it with `/risk-tests`. Don't propose one for cheap, easy-to-undo choices.
- **Read first:** `docs/01-discovery/00-brainstorm.md` (the picked problem and its fallbacks) and `docs/ideas.md`. Start from what is there; ask only what is missing.
- **One question at a time,** then wait. Write the file from the user's answers; never invent one.
- **If an answer is vague, push back** before moving on: "how often?", "how much, roughly?", "what did you do the last time?".
- **Mark every claim** as checked (someone told you, or you saw it) or as an assumption.
- **Feature ideas that come up** go to `docs/ideas.md`, under "New", with the next ID. Don't discuss them until the PRD. If the file doesn't exist (the brainstorm was skipped), create it in this format:

  ```markdown
  # Ideas
  Parking lot for feature ideas. Each idea has a stable ID (F-01, F-02…) that never changes, even when the order does. Unsorted until 04 PRD, which sorts them.

  ## New (not sorted yet)
  - **F-01 [Short name]:** what it does for the user, in one line. *From:* [step, date]. *Solves:* [the problem or complaint, if known]

  ## MVP (set in 04 PRD)
  ## After MVP
  ### High
  ### Medium
  ### Low
  ## Dropped
  - **F-07 [Name]:** why, so it isn't discussed again
  ## Merged
  - F-25 → F-11
  ```

  Rules: take the next free ID, never reuse one; a merged idea keeps its ID with an arrow; a dropped idea stays with its reason.

## Steps

### 1. Who?
One concrete person: age, situation, what they want. Starting with yourself is fine; say so.

### 2. What problem?
What they can't do today, without a solution in it. Then the same as a job story:
> When [situation], I want to [what they try to do], so I can [the outcome they want].

The job story keeps the focus on what they want to achieve, not on a feature.

### 3. How do they solve it today?
Each alternative (an app, a spreadsheet, a person, doing nothing), with what it does well and where it fails. A workaround they built themselves is the strongest sign the problem is real.

### 4. What does it cost them?
Time, money or results, in numbers. Approximate is fine, vague is not: "~30 minutes a day", not "a lot of time". These numbers become the success metrics in the PRD.

### 5. How strong is the problem?
Place it on the ladder; the higher, the better:
1. they are annoyed, but do nothing;
2. they tried something and gave up;
3. they built a workaround (a spreadsheet, a template, a routine);
4. they pay for something today;
5. they are looking for a better solution right now.

### 6. The segment
The wider group the person belongs to, one you can reach (for example "developers who want to lose weight"). Say where they gather: communities, forums, events, job titles.

### 7. Check it in 3–5 interviews
- **Who:** people from the segment who have the problem now. Strangers or acquaintances, not friends being nice. Find them in the communities from step 6, on LinkedIn, or among people you know.
- **The questions:** 5 questions about what they did, not about the idea. Start each with "Tell me about the last time you…". For example: what they tried, what they use now, why they stopped, how much time it takes, whether they ever paid.
- **Never ask:** "would you use…?", "would you pay…?", "do you think it's a good idea?". Hypotheticals and compliments predict nothing.
- **During the interview:** 20–30 minutes, and they talk most of the time. When they say "usually" or "always", ask for the last specific time. When they show emotion, ask "why?".
- **At the end:** tell them the idea, then ask for something real: an email for the beta, a pre-order, an intro to someone else with the problem.
- **After each one:** a short note with what they did (facts), their pains in their own words, what they pay for, and your interpretation kept separate.
- **Personal data:** ask before recording, keep notes private, no names in public repos.
- **The result:** 3 out of 5 describe the same problem → it's real. Fewer → change the who or the problem and check again, or drop it. Not done yet? Mark it "not yet verified"; it becomes a test in the product brief.

Then write `docs/01-discovery/01-problem.md`:

```markdown
# 01 – Problem
**Who:**
**Segment:** [the group], found in [where they gather]
**Problem:**
**Job story:** When …, I want to …, so I can …
**How they solve it today:**
- [alternative]: what it does well, where it fails
**What it costs them:**
**How strong:** [step on the ladder], because [evidence]
## Verify with others
[verified / not yet verified]
### Questions
### Results
| Person (no name) | What they did | What they use | Why they stopped | Time / cost | Paid? | Gave something real? |
**Pattern:** [x of 5 describe …]
**Decision:** keep / change / drop
```

## Validate mode
`/saas-problem validate <file>`: judge an existing problem page, change nothing.
1. Read the page, `docs/01-discovery/00-brainstorm.md` if it exists, `docs/ideas.md` and any interview notes.
2. Check the template and "Done when" item by item, citing the lines.
3. Then ask:
   - Is the person concrete enough to decide something, or is it "anyone who…"?
   - Does the problem hide a solution ("an app that…")?
   - Is every cost a number, and is each one checked or a guess?
   - Is the strength on the ladder backed by something someone did?
   - Were the interviews about the past, with people who aren't friends? Any "would you…?" question?
   - Is there a decision after the interviews, or are they still "not yet verified", and is that test in the brief?
4. Report: findings by severity, each with the line, what's wrong and what to change; then what the page does well; then what you couldn't evaluate. The user picks what to apply.

## The bad version and why not
- "For anyone who wants to eat healthy" → too vague to decide anything.
- Starting from the solution ("an app with AI") instead of the problem.
- Assuming everyone has your problem.
- Asking "would you use my app?" → almost everyone says yes to be nice. Only what they already did counts.
- Interviewing friends → they protect your feelings, not your product.

## What breaks if you skip it
You build features nobody uses.

## The principle behind it
Start from the problem, not the solution. You are not your user. Past behaviour predicts, opinions don't (The Mom Test).

## How to apply it at work
Before any feature or ticket, ask: what problem does this solve, for whom, and what does it cost them today? When a stakeholder asks for a feature, ask for the last time a user hit the problem.

## Done when
- [ ] one concrete person and a reachable segment, with where they gather
- [ ] the problem has no solution in it, plus a job story
- [ ] today's alternatives, each with where it fails
- [ ] the cost in numbers, and the strength on the ladder
- [ ] 3–5 interviews with a results table and a decision, or marked "not yet verified"
- [ ] feature ideas parked in `docs/ideas.md` with stable IDs

## Next
Discovery · 02 Market research (`/saas-market-research`).
