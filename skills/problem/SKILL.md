---
name: problem
description: "Who has the problem, what it is, how they solve it today and what it costs them, checked in at least 5 interviews (per sub-group, when the segment has two) about what people did, not about the idea, with the results kept private. Use when the user starts a new app or product and has an idea, before market research and before any code. Also judges an existing problem page: /problem validate <file>."
argument-hint: "[the idea, in a few words] or validate <file>"
---

# Problem

## When to use it
After `/brainstorm`, with the problem picked there, before any code.

## The problem it solves
You know who you build for and what hurts them, so every later decision has a reason.

## How to run it
- **The bar:** do what a senior engineer or the C-level who owns this area (CEO, CPO, CTO, CFO, CMO, COO) at a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it, so the user learns it. Senior also means knowing what to leave out: say what you skip and why.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Every `docs/…` path below means that folder.
- **Spot risky assumptions for the user:** when a decision here rests on something nobody has checked ("I think people will…", "the AI can probably…") and being wrong would cost a lot, stop and propose a risk test: what to check, how long it takes, the pass mark, and when it must be done. The user only says yes or no; run it with `/risk-tests`. Don't propose one for cheap, easy-to-undo choices.
- **Read first:** `docs/01-discovery/00-brainstorm.md` (the picked problem and its fallbacks) and `docs/00-project/ideas.md`. Start from what is there; ask only what is missing. **No brainstorm?** Then the problem comes from the user's own experience: say so on the page, and that there are no fallbacks, so a failed interview round means running `/brainstorm` before trying again.
- **One question at a time,** then wait. Write the file from the user's answers; never invent one.
- **If an answer is vague, push back** before moving on: "how often?", "how much, roughly?", "what did you do the last time?".
- **Mark every claim** as checked (someone told you, or you saw it) or as an assumption.
- **When the page changes later,** mark the change in place, "(added [date])" or "(corrected [date]: it said …)", and add a line to the journal: what changed, who decided, why. The old wording stays readable, so nobody repeats a mistake already fixed.
- **Feature ideas that come up** go to `docs/00-project/ideas.md`, under "New", with the next ID. Don't discuss them until the PRD. If the file doesn't exist (the brainstorm was skipped), create it in this format:

  ```markdown
  # Ideas

  | | |
  |---|---|
  | **What this is** | the parking lot for every feature idea, from the first brainstorm on: the MVP's features in the PRD's dependency order, everything after the MVP in priority buckets, and what was merged, moved or dropped, each with why |
  | **Updated** | [date] |
  | **README** | [00 Project](README.md), what this folder holds and the rules it shares with the ADRs |
  | **Next free ID** | F-[NN] |

  **The IDs:** each idea gets the next free number (F-01, F-02…) when it arrives and keeps it forever, even when its place, its priority or its phase changes. A number says nothing about priority or phase. Other documents cite ideas by their ID, never by a position or a range.

  **The order:** the MVP by dependency (what everything else needs first, then what solves the problem, then the rest), as the PRD's MVP table; that isn't the build order, which is the PRD's slices. After the MVP, three buckets, High, Medium and Low, each ordered from most to least wanted. A new idea waits in "New" until it's sorted.

  **What each idea says:** what it is, in one or two lines; where it came from and what it solves, when that isn't obvious; and any decision it would reopen (an ADR, the DPIA, a non-goal). The details of an MVP feature live in the PRD; this line is its summary.

  ## New (not sorted yet)
  - **F-01 [Short name]:** what it does for the user, in one line. *From:* [step, date]. *Solves:* [the problem or complaint, if known]

  ## MVP (set in 04 PRD)
  Order: what everything else depends on first, then what solves the problem, then the rest.

  ## After MVP
  Each bucket ordered from most to least wanted.

  ### High
  ### Medium
  ### Low

  ## Merged or moved
  Ideas that live on in another, their IDs kept.
  - **F-25** → merged into F-11 on [date]: [what it was]

  ## Dropped
  - **F-07 [Name]:** dropped [date]. [why, and the decision that forbids it], so it isn't discussed again

  ## History
  - [date]: written in [step].
  ```

  Rules: take the next free ID and move the header's Next free ID on; never reuse one. A merged or moved idea keeps its ID with an arrow; a dropped idea stays with its date and reason. Every change to the file sets Updated and adds a History line.

## Steps

### 1. Who?
One concrete person: age, situation, what they want. Starting with yourself is fine; say so.

### 2. What problem?
What they can't do today, without a solution in it. "Can't find an app that…" is a solution: it decides the answer is an app. Write what they can't tell, do or reach (for example "can't tell whether the numbers they log are right"). Then the same as a job story:
> When [situation], I want to [what they try to do], so I can [the outcome they want].

The job story keeps the focus on what they want to achieve, not on a feature.

### 3. How do they solve it today?
Each alternative (an app, a spreadsheet, a person, doing nothing), with what it does well and where it fails. A workaround they built themselves is the strongest sign the problem is real.

### 4. What does it cost them?
Time, money or results, in numbers. Approximate is fine, vague is not: "~30 minutes a day", not "a lot of time". These numbers become the success metrics in the PRD, so mark each one **measured** or **estimated** (and from how many people: your own guess is n = 1), and say how to measure it (for example "a week of logging with today's app, timed"). A metric built on a guess needs its baseline measured before launch.

### 5. How strong is the problem?
Place it on the ladder; the higher, the better:
1. they are annoyed, but do nothing;
2. they tried something and gave up;
3. they built a workaround (a spreadsheet, a template, a routine);
4. they pay for something today;
5. they are looking for a better solution right now.

### 6. The segment
The wider group the person belongs to, one you can reach (for example "developers who want to lose weight"). Say where they gather (communities, forums, events, job titles, colleagues): that's where you recruit the interviews. If the segment holds two groups whose problem may differ (losing weight and staying fit), name both; the interviews keep them apart. If others share the use without being users (the person they cook with, a manager who reads the report), name them too.

### 7. Check it in at least 5 interviews
- **Before the first one:** write down what "the same problem" means, which parts of step 2 must match (for example "at least two of its three parts, and logging that takes too long"), so the pass mark isn't bent after the answers. Set a dated **Status** (not started / running / done) and a **When**: the deadline, chosen on purpose (before Planning, before launch…), with the risk you accept if it's later.
- **Who:** at least 5 people from the segment who have the problem now, per sub-group when step 6 named two (or 5 from the main group and 2–3 from the other, kept apart, as a signal, not a verdict). Fewer than 5 can't reach the "3 of 5" pass. Not only friends: friends say what you want to hear. Find them where the segment gathers (step 6), on LinkedIn, or among people you know.
- **The questions:** about 5, about what they did, not about the idea. Start each with "Tell me about the last time you…", never about habits ("how much time per day?") and never yes or no. For example: what they tried, what they use now, why they stopped, how long it took the last day they did it, whether they ever paid. When others share the use (step 6), add one about them ("Do you cook or shop with someone? How did you plan it the last time?").
- **Never ask:** "would you use…?", "would you pay…?", "do you think it's a good idea?". Hypotheticals and compliments predict nothing.
- **During the interview:** 20–30 minutes, and they talk most of the time. When they say "usually" or "always", ask for the last specific time. When they show emotion, ask "why?".
- **At the end:** tell them the idea (not before), then ask for something real: an email for the beta, a pre-order, the name of someone else with the problem.
- **After each one:** a short note with what they did (facts), their pains in their own words, what they pay for, and your interpretation kept separate.
- **Personal data:** the notes go in a separate `docs/01-discovery/interviews.md`, created with the first interview: no names, consent before any recording, kept private (out of public repos), since the answers may be health or other personal details. The problem page holds only the summary and the status.
- **The result:** 3 out of 5 describe the same problem → it's real. Fewer → change who it's for or the problem and check again, or drop it, back to the brainstorm. Not done yet? The status says so; it becomes a test in the product brief.

Then write `docs/01-discovery/01-problem.md`:

```markdown
# 01 – Problem
**Who:**
**Segment:** [the group, and its sub-groups if two], found in [where they gather]; also using it: [who shares the use, if anyone]
**Problem:**
**Job story:** When …, I want to …, so I can …
**How they solve it today:**
- [alternative]: what it does well, where it fails
**What it costs them:** [number], measured / estimated (n = [people]); to measure: [how]
**How strong:** [step on the ladder], because [evidence]
## Verify with others
**Status ([date]):** not started / running / done. **When:** [deadline], because [why; the risk accepted if later]
**Who to ask:** at least 5 from [group], not only friends; [2–3 from the other group, kept apart]
**Questions:**
1. Tell me about the last time you…
**At the end:** [the real ask]
**Pass:** 3 of 5 describe the same problem, meaning [which parts must match]. **Fewer:** change who it's for or the problem, or drop it, back to the brainstorm.
**Results:** in `interviews.md` (private, no names). **Pattern:** [x of 5 describe …] **Decision:** keep / change / drop
## Journal
- [date]: [what was written or changed, by whom, why]
```

`docs/01-discovery/interviews.md`, private, one block per interview:

```markdown
# Interviews (private: no names, not in a public repo)
## P1, [date], [group], consent to record: yes / no
- **What they did:** … **What they use:** … **Why they stopped:** … **Time / cost:** … **Paid?** … **Gave something real?** …
- **In their words:** "…"
- **My reading:** … (kept apart from the facts)
```

## Validate mode
`/problem validate <file>`: judge an existing problem page, change nothing.
1. Read the page, `docs/01-discovery/00-brainstorm.md` if it exists, `docs/00-project/ideas.md` and any interview notes.
2. Check the template and "Done when" item by item, citing the lines.
3. Then ask:
   - Is the person concrete enough to decide something, or is it "anyone who…"?
   - Does the problem hide a solution ("an app that…")?
   - Is every cost a number, marked measured or estimated, with how to measure it?
   - Is the strength on the ladder backed by something someone did?
   - Were the interviews about the last time, with at least 5 people, not only friends? Any "would you…?", habit or yes/no question?
   - Was "the same problem" defined before the interviews, with a fail branch? Are the results in a private file, without names?
   - Is the status dated, with a deadline chosen on purpose? Is there a decision, or is the test in the brief?
   - Does each later change say what the page said before, with a journal line?
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
- [ ] the problem has no solution in it ("can't find an app that…" fails), plus a job story
- [ ] today's alternatives, each with where it fails
- [ ] the cost in numbers, each measured or estimated with how to measure it, and the strength on the ladder
- [ ] "the same problem" defined, at least 5 interviews per group about the last time, a real ask, a fail branch
- [ ] a dated status and a deadline; results in a private `interviews.md` and a decision, or the test in the brief
- [ ] a journal, with every later change marked "(added …)" or "(corrected …: it said …)"
- [ ] feature ideas parked in `docs/00-project/ideas.md` with stable IDs

## Next
Market research (`/market-research`).
