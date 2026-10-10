---
name: discovery-brainstorm
description: "Discovery, optional step before 01: find a problem worth building for when you have no idea yet. 30+ problems across many areas and lenses, a shortlist scored on 6 criteria, a quick evidence check on the top 3, one picked with two fallbacks. Use when the user wants to build something but doesn't know what; skip it when they already have an idea."
argument-hint: "[a field or a group of people, optional]"
---

# Discovery · Brainstorm (optional)

## When to use it
Only when you want to build something and have no idea what. With an idea, go straight to `/discovery-problem`.

## The problem it solves
You pick a problem by comparing it with many others, from areas you wouldn't have thought of alone, not the first one that comes to mind.

## How to run it
- **Stay in exploring as long as possible.** Don't judge, group or score until step 3. When the flow slows, switch area or lens; don't conclude.
- **One prompt at a time,** then wait. Never dump a list of questions.
- **Switch area every ~8 problems.** Ideas drift toward the same theme; a new area forces new ones.
- **Problems count only when the user writes or accepts them.** You may offer a provocation ("people who move house lose a weekend to address changes — true for you?"); it goes in the list only if the user says yes.
- **Problems, not solutions.** When the user says "an app that…", park the solution in `docs/ideas.md` with the next ID, then ask "what hurts without it?" and write that problem. No idea is lost, and the list stays about problems.

## Steps

### 1. Pick where to start
If `docs/ideas.md` exists, read it first: every idea there hides a problem someone has. Then ask what they know well (job, hobbies, a group of people they belong to). Start with the area closest to that; the unfair advantage is a field you already understand.

### 2. Explore: at least 30 problems, 30–45 minutes
Go through the areas, and use a lens on each when the area runs dry.

**Areas:**
- **Your day:** walk through yesterday hour by hour; then a typical week, then a month (bills, admin, chores).
- **Your work:** repeated tasks, copy-paste between tools, spreadsheets, waiting for approvals, handoffs that lose information.
- **People around you:** partner, family, friends, colleagues. What do they complain about? What do they ask you to help with?
- **Money:** what you pay for and dislike, subscriptions you cancelled and why, what you'd pay to never do again.
- **Health and body:** food, sleep, training, doctors, medication.
- **Home:** cooking, cleaning, repairs, moving, renting, neighbours.
- **Life events:** a new job, a baby, a move, a wedding, a diagnosis, retirement. Each one creates a burst of new problems.
- **Communities:** 1–2 star reviews of popular apps, Reddit or forum posts that start with "is there an app that…" or "how do you deal with…".
- **Hobbies:** what slows you down or costs too much in something you do for fun.
- **What changed recently:** a new law, a new technology (AI, a new sensor, a new API), a price rise, a product shutting down.

**Lenses** (one at a time, on the current area):
- **Workaround hunt:** where do people use a spreadsheet, paper, notes or a WhatsApp group for something? Each one is a problem.
- **Complaint mining:** what do people complain about every week, in their own words?
- **Five whys:** take a small annoyance and ask "why?" until you reach the real problem behind it.
- **Make it worse:** "how could this be even more annoying?" The answers show what people already suffer.
- **Outsider eyes:** describe how people do it today as if you saw it for the first time. What looks strange or slow?
- **Cross-pollination:** what works well in one field but is missing in another (for example tracking a parcel vs tracking a repair)?
- **Question storming:** only questions, no answers, for five minutes ("why does it take three emails to book a…?").

Write each problem in one line: who + what hurts. "Freelancers chase late invoices every month", not "invoicing app".

### 3. Group and cut to a shortlist
Merge duplicates, rewrite any solution as a problem, then the user picks the 8–12 they find most interesting.

### 4. Score the shortlist from 1 to 5
| Criterion | The question |
|---|---|
| **Pain** | how much does it hurt when it happens? |
| **Frequency** | daily, weekly, yearly? |
| **They pay already** | do people spend money or time on a workaround? |
| **Reach** | can you find and talk to these people? |
| **Buildable** | can you build a first version alone in a few weeks? |
| **You care** | would you still work on it in two years? |

The user gives the scores; you add them up.

### 5. Quick evidence on the top 3 (10 minutes each)
For each: search for complaints online and for products people pay for. Note one link for each. Paid competitors are good news: the problem is real and people pay.

### 6. Pick one, keep two
The user picks one, with the reason. On a tie, the one where people already pay or built a workaround wins. The other two are fallbacks if 01 drops the pick.

Create `docs/ideas.md` if it doesn't exist, in this format:

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

Then write `docs/01-discovery/00-brainstorm.md`:

```markdown
# 00 – Brainstorm
## All problems
### [area]
- [who + what hurts]
## Shortlist
| Problem | Pain | Frequency | They pay | Reach | Buildable | You care | Total |
## Evidence on the top 3
- [problem]: [complaint link], [paid product link]
## Pick
**Picked:** [problem], because [reason]
**Fallbacks if it fails in 01:** [2nd], [3rd]
```

## The bad version and why not
- Writing solutions instead of problems ("an app that…") → you compare ideas, not needs.
- Stopping at the first good idea → nothing to compare it with.
- Staying in one area → 30 versions of the same problem.
- Scoring while still exploring → the list stops growing.
- Picking a problem you can't reach the people for → you can't check it in 01 or sell it later.
- Picking a problem you don't care about → you quit after three months.

## What breaks if you skip it
Nothing, if you already have an idea. Without one, you pick by enthusiasm and find out at 01 that the problem is weak.

## The principle behind it
Many options first, then choose: diverge, then converge. Judging too early kills the ideas you need.

## How to apply it at work
When a team asks "what should we build next?", list the problems first (from support tickets, sales calls, user reviews), score them together, then pick.

## Done when
- [ ] at least 30 problems from at least 5 areas, written without solutions
- [ ] a shortlist of 8–12, scored on the 6 criteria
- [ ] evidence links for the top 3
- [ ] one picked with the reason, and two fallbacks
- [ ] every solution that came up is parked in `docs/ideas.md` with an ID

## Next
Discovery · 01 Problem (`/discovery-problem`), with the picked problem.
