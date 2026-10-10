---
name: saas-brainstorm
description: "Discovery, step 00, the start of every new project: shape the raw ideas into docs/ideas.md, find the problems behind them and around them across many areas and lenses, score a shortlist on 6 criteria, check the top 3, pick one with two fallbacks. Use when the user starts a new product, with a raw list of ideas, a single idea, or nothing."
argument-hint: "[the idea, a field or a group of people, optional]"
---

# Discovery · 00 Brainstorm

## When to use it
The first step of every new project, after `/saas-setup`. Before it, write everything in your head into `docs/ideas.md`, in any form: features, names, "it would be cool if…". No idea yet? Start with an empty file.

## The problem it solves
Your raw ideas get a shape, and you pick a problem by comparing it with others, not the first one that comes to mind. Most ideas arrive as solutions; this step finds the problem behind each one.

## How to run it
- **The bar:** do what a senior engineer or the C-level who owns this area (CEO, CPO, CTO, CFO, CMO, COO) at a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it, so the user learns it. Senior also means knowing what to leave out: say what you skip and why.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Every `docs/…` path below means that folder.
- **Spot risky assumptions for the user:** when a decision here rests on something nobody has checked ("I think people will…", "the AI can probably…") and being wrong would cost a lot, stop and propose a risk test: what to check, how long it takes, the pass mark, and when it must be done. The user only says yes or no; run it with `/risk-tests`. Don't propose one for cheap, easy-to-undo choices.
- **Stay in exploring as long as possible.** Don't judge, group or score until step 4. When the flow slows, switch area or lens; don't conclude.
- **One prompt at a time,** then wait. Never dump a list of questions.
- **Switch area every ~8 problems.** Ideas drift toward the same theme; a new area forces new ones.
- **Problems count only when the user writes or accepts them.** You may offer a provocation ("people who move house lose a weekend to address changes — true for you?"); it goes in the list only if the user says yes.
- **Problems, not solutions.** When the user says "an app that…", park the solution in `docs/ideas.md` with the next ID, then ask "what hurts without it?" and write that problem. No idea is lost, and the list stays about problems.

## Steps

### 1. Shape the ideas
Read `docs/ideas.md`. If it's empty or missing, ask for a dump: "write everything in your head about what you'd like to build", then "anything else?". Nothing at all? Skip to step 3, the path without an idea.
- Give each idea the next free ID, a short name and one line on what it does for the user, with *From: brain dump*.
- Merge duplicates (the merged ID gets an arrow), keep the user's meaning, invent nothing.
- Rewrite the file in the format below, all under "New", and show it. The user confirms or corrects.

### 2. The problems behind the ideas
For each idea, or each group of similar ideas: "what hurts without it, and for whom?". Write the answer as a problem (who + what hurts) and fill the idea's *Solves* field. These are the first problems on the list.

### 3. Explore around them
- **With a clear idea:** at least 10 more problems around it: the same people's other problems, the step before and after, neighbouring areas. You check that your idea's problem is the strongest one there, not just the first.
- **Without one:** at least 30 problems, 30–45 minutes, across the areas.

Ask what the user knows well (job, hobbies, a group of people they belong to) and start with the area closest to that; the unfair advantage is a field you already understand. Use a lens when an area runs dry.

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

### 4. Group and cut to a shortlist
Merge duplicates, rewrite any solution as a problem, then the user picks the 8–12 they find most interesting.

### 5. Score the shortlist from 1 to 5
| Criterion | The question |
|---|---|
| **Pain** | how much does it hurt when it happens? |
| **Frequency** | daily, weekly, yearly? |
| **They pay already** | do people spend money or time on a workaround? |
| **Reach** | can you find and talk to these people? |
| **Buildable** | can you build a first version alone in a few weeks? |
| **You care** | would you still work on it in two years? |

The user gives the scores; you add them up.

### 6. Quick evidence on the top 3 (10 minutes each)
For each: search for complaints online and for products people pay for. Note one link for each. Paid competitors are good news: the problem is real and people pay.

### 7. Pick one, keep two
The user picks one, with the reason. On a tie, the one where people already pay or built a workaround wins. The other two are fallbacks if 01 drops the pick.

The format of `docs/ideas.md`:

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
Your ideas stay a pile of solutions with no problem behind them, and you pick the first one by enthusiasm, to find out at 01 that the problem is weak.

## The principle behind it
Many options first, then choose: diverge, then converge. Judging too early kills the ideas you need.

## How to apply it at work
When a team asks "what should we build next?", list the problems first (from support tickets, sales calls, user reviews), score them together, then pick.

## Done when
- [ ] `docs/ideas.md` in the format, every idea with an ID and, where known, the problem it solves
- [ ] the problems behind the ideas, plus at least 10 around a clear idea, or 30 from at least 5 areas without one, all written without solutions
- [ ] a shortlist of 8–12, scored on the 6 criteria
- [ ] evidence links for the top 3
- [ ] one picked with the reason, and two fallbacks
- [ ] every solution that came up is parked in `docs/ideas.md` with an ID

## Next
Discovery · 01 Problem (`/saas-problem`), with the picked problem.
