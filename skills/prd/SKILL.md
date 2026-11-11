---
name: prd
description: "What the first version does, exactly. Success metrics from the cost of the problem, user journeys, a glossary, ideas sorted into the MVP and after, checks for payment, both sides, AI cost and day one, a size check, yes/no acceptance criteria per feature, non-functional numbers that agree, and a ready-for-delivery check. Use after the brief decides go, before architecture and code. Also judges an existing PRD: /prd validate <file>."
argument-hint: "[the product or version] or validate <file>"
---

# PRD

## When to use it
After the brief decides "go" or "go with conditions" (03), before architecture and code.

## The problem it solves
You write down exactly what the app does (PRD = Product Requirements Document): what goes into the first version, and what "done" means for each feature. Design, architecture and code all start from it.

## How to run it
- **The bar:** do what a senior engineer or the C-level who owns this area (CEO, CPO, CTO, CFO, CMO, COO) at a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it, so the user learns it. Senior also means knowing what to leave out: say what you skip and why.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Every `docs/…` path below means that folder.
- **Spot risky assumptions for the user:** when a decision here rests on something nobody has checked ("I think people will…", "the AI can probably…") and being wrong would cost a lot, stop and propose a risk test: what to check, how long it takes, the pass mark, and when it must be done. The user only says yes or no; run it with `/risk-tests`. Don't propose one for cheap, easy-to-undo choices.
- **Read first:** everything in `docs/01-discovery/` and `docs/00-project/ideas.md`. Ask only what is missing.
- **The user decides** what goes in the MVP and what each criterion says. You propose, push back and check; you don't pick the cuts.
- **One feature at a time** for the criteria. Show each before the next.
- **Requirements, not implementation:** what the user can do and what must be true, never which library, database or vendor. Those are decided in the architecture.
- **Mark guesses** as `[ASSUMPTION]`; they are listed at the end.
- **IDs never change:** features keep their F-IDs from `ideas.md`; journeys are UJ-1, UJ-2…

## Steps

### 1. The goal
One line: the MVP solves the problem in 01, for the person in 01.

### 2. Success metrics
- **From the cost of the problem:** each cost in 01 becomes a target. "~30 minutes a day to log" → "a full day logged in under 5 minutes".
- **The user signal** from the brief (for example "logs food 5 days a week after the first month").
- **A counter-metric:** a number that must not get worse while you chase the others (for example "average calories logged don't drop because people stop logging snacks").
- For each: the target and how you measure it. Anything measured in the app becomes an **event** or a **daily counter** to track (for example `day_completed`, or `entries_added` per person per day when the team keeps daily counters instead of events, as MacroMate's ADR-0018 did), so you can see it from the first day.
- **Every target is a number, or `[ASSUMPTION]`** listed in Assumptions ("the share, set before the beta" is fine only there).
- **Who is counted:** only the people the metric is about (a weight-loss metric counts only people with the goal "lose", not everyone).
- **Small totals stay hidden:** a total behind fewer than ~5 people isn't published, because it points at one person.

### 3. User journeys
The 3–5 main flows, each as a short scene with a named person (from 01, not "the user"):
- **who and why:** one line of context;
- **where they start:** logged in or not, which screen, coming from where;
- **the path:** 3–5 concrete steps;
- **the moment value lands,** and how they know;
- **one edge case:** a real failure and what they do next.

Each journey later becomes screens and tests.

### 4. Glossary
Every domain word the PRD uses (for example *food, recipe, variant, meal, plan, log entry*), defined once, with how it relates to the others ("a recipe has many variants"). Use exactly these words everywhere after; no synonyms. Every domain word the criteria use gets an entry, not only the big nouns: a state (*read-only*), a place (*archive*), an action (*Complete day*); MacroMate's re-read found 6 missing on 2026-11-11. This becomes the data model and the names in the code (ubiquitous language, from Domain-Driven Design).

### 5. Sort the ideas
Take every idea from `docs/00-project/ideas.md` and sort it with the user:
- **MVP:** the smallest set that solves the problem in 01 end to end. It must have:
  - what the other features depend on (a weight chart needs a weight log; a scanner needs a data source);
  - what solves the problem;
  - the **expected** features from 02 that users won't live without;
  - **at least one differentiator** from 02, or nobody has a reason to switch.
- **After MVP:** High / Medium / Low, by value against effort. When the list is long, score with RICE (reach × impact × confidence ÷ effort).
- Order the MVP by dependencies first, then what solves the problem, then the rest. This dependency order isn't the build order: the build order is the slices of step 7, each usable before the next; `ideas.md` keeps the dependency order and says so.
- Rewrite `docs/00-project/ideas.md`: ideas move from "New" to their section; merged and moved ones go under "Merged or moved" with an arrow, dropped ones under "Dropped" with the date and why; set the header's Next free ID and Updated, and add a History line (the date, sorted in 04 PRD, what moved).

### 6. The checks a feature list misses
- **Payment:** if the goal is revenue, is there a feature through which people pay? Trial, plans, cancel.
- **Both sides:** every admin screen has the user action that fills it (admins see reported mistakes → users can report one), and the other way round.
- **AI cost:** for each AI feature, the cost per call, a monthly budget per user (around 10–20% of the price) and what happens when it runs out.
- **Day one:** does a new user get value in the first session, before they've entered any data? If not, add sample content, a template or an import.
- **Data in and out:** what users bring from their current tool (the switching cost in 02), and export of their own data.
- **Roles:** who can do what (user, admin, a member of a shared space), for each feature.

### 7. Size and time
Size each MVP feature: S (1–2 days), M (about a week), L (2+ weeks). Add them up and compare with the capacity until the launch date in the brief; if the brief has no date, until its checkpoint or the owner's date. Show the capacity as a sum, counted from the day you check (hours a week × weeks ÷ 8 h), and recount it on every re-check. Too long → cut features, cut parts of features, or ship in slices. A first version that takes a year is not a first version.

If the owner keeps a size that doesn't fit, write "fails on purpose, because …" with the decision. MacroMate: ~125 days at ~10 h a week ≈ 2 years against a June 2027 checkpoint; no feature cut, built in slices, and the checkpoint re-decides the date.

### 8. Functional requirements, per feature
The section is headed **"Functional requirements"**, next to "Non-functional requirements", so both kinds are found by name (at work and in interviews they're called that; "Done when" hid what they are). For each MVP feature, one at a time:
- **A short description:** what it does and which journeys it serves; one line is enough, and it tells a reader what the criteria are for.
- **Criteria you can tick yes or no:** "I can reset my password from the email", not "the account works well". The happy path and the main failures (wrong input, no connection, nothing found).
- **Given / when / then** only where the flow is complex.
- **Data rules** where they matter:
  - a missing value is not zero (an unknown nutrient, a day not logged);
  - store the raw data, calculate what derives from it (a grade, a total), so there is one source of truth;
  - when an item changes, past records keep their values (a snapshot).
- **Not in the MVP:** the parts of this feature left for later, on every feature where an idea waits in `ideas.md`, citing its F-ID ("Not in MVP: tolerating typos (F-24)"). MacroMate had it on only two features.

### 9. Non-functional requirements, with numbers
- **Speed:** 0.1 s feels instant, 1 s keeps the flow, 10 s is the limit. Set a number for the main actions.
- **Security:** who can see whose data, login rules, limits on requests (rate limiting), what happens to secrets.
- **Personal data:** consent, where it is hosted, export, deletion (including from backups), what is sent to third parties. Headed **Health data and GDPR** when health data is processed (explicit consent, minimum age, retention).
- **Offline**, if the app works without internet: what opens and what can be done, how long data waits on the device, what needs internet.
- **Devices** (with the browsers and the smallest screen), **Languages** (with number and date formats).
- **Availability and backups:** availability per month, RPO (how much data you can lose), RTO (how long to restore), and what each needs (alerts, a tested restore).
- **Accessibility:** WCAG level, contrast, tap targets, larger fonts.
- **Operations:** how users reach you and how fast you answer, terms and privacy pages, alerts when costs or errors spike.

Third-party providers appear as requirements (region, data processing agreement, no training on your data), never by name, in the criteria too ("the payment provider's page", "a phone call"); the name is chosen in the architecture. Names are fine where the name is the fact: data sources and their licences, a sign-in users see (Google), browsers, an Assumptions line quoting a calculation's figure, and an open decision about a provider already chosen. MacroMate's slip: a payment provider and an alerting vendor named in criteria, fixed 2026-11-11.

**Check that the numbers agree:** an RTO of 4 h doesn't fit in 99.5% availability (3.6 h down per month).

### 10. Non-goals and out of scope
- **Non-goals:** what the product is not and won't become in this version (for example "not a medical app", "no social feed").
- **Out of scope:** everything after the MVP, by reference to `docs/00-project/ideas.md`.

### 11. Assumptions and open decisions
- Every `[ASSUMPTION]` listed, to confirm or test.
- Every open decision: one-way or two-way door, what it blocks, who answers, by when. Those that block the architecture are asked now, with a recommended answer.

### 12. Review and ready for delivery
- Someone who will design or build it reads the PRD. Their questions are answered, or listed as open with an owner. Nobody at hand? Run `/prd validate <file>`.
- **Ready for delivery** when: every MVP feature has criteria, the numbers agree, the size fits the time (or fails on purpose, with the decision written), and no open decision blocks the architecture. The step that judges it writes the verdict in the file, with the date, not only in the chat.

Then write `docs/01-discovery/04-prd.md`:

```markdown
# 04 – PRD
## Goal
## Success metrics
| Problem today | Target | How I measure it | Event or daily counter |
Who is counted; totals behind fewer than ~5 people not published.
**Counter-metric:** …
## User journeys
### UJ-1 [Name] [does what]
## Glossary
- **Term:** definition, relation to other terms
## MVP scope
| ID | Feature | Why in the MVP (dependency / solves / expected / differentiator) | Size |
**Total size:** … against … until launch (capacity from [date]: … h a week × … weeks ÷ 8 h); fits / fails on purpose, because …
### Build order (slices)
1. **[Name]:** F-…, F-…. Before it, [the tests that must pass].
**Ready for delivery:** [date], yes / no, because …
## Functional requirements
### F-01 [Feature]
[What it does, which journeys: one line.]
- [ ] …
Not in MVP: … (F-…)
## Non-functional requirements
### Speed · Security · Personal data (or Health data and GDPR) · Offline · Devices · Languages · Availability and backups · Accessibility · Operations
## Non-goals
## Out of scope
Everything after the MVP in `docs/00-project/ideas.md`.
## Assumptions
## Open decisions
| Decision | One-way or two-way | Blocks | Who | By when |
## Journal
- [date]: [what was decided, by whom, what it changed]
```

## Validate mode
`/prd validate <file>`: judge an existing PRD, change nothing.
1. Read the PRD, its journal, everything in `docs/01-discovery/` and `docs/00-project/ideas.md`.
2. Check the template and "Done when" item by item, citing the lines.
3. Then ask: does every MVP feature trace back to the problem, a dependency, an expected feature or a differentiator? Can each criterion be ticked yes or no by someone else? Does the glossary match the words used? Do the non-functional numbers agree? Is any vendor named where a requirement belongs? Does the size fit the time?
4. Report: findings by severity, each with the line, what's wrong and what to change; then what the PRD does well; then what you couldn't evaluate. The user picks what to apply.

## After Design
Design makes the PRD precise; the PRD must say so, or the two drift. Once Design's steps are written, re-read the PRD against each step's files:
- **A criterion Design made precise** is written back with the number, marked "(added [date], [step])": session lengths, a reset link's life, speed measured as LCP and CLS on a slow 4G phone, a timeout.
- **An open decision Design raised** goes into Open decisions with its owner and date (the RTO against the database plan; a legal question before the first payment).
- **The risk tests' pass marks** go into Assumptions ("15 of 20 plates within ±20%"), until the test is run.
- **Each slice names the tests** that must pass before it starts.
- Recount the capacity, check the provider names, the glossary and the metrics again, and add a journal line.

## The bad version and why not
- Putting every idea in the first version.
- "The account works well" → nobody can say when it's done.
- Treating a missing value as zero (an unknown nutrient, a day not logged) → grades and averages come out wrong.
- Storing what can be calculated (for example a grade) → two sources of truth that end up disagreeing.
- Naming the database or the AI vendor in the PRD → the architecture decision is made without its trade-offs.
- An MVP with no way to pay, or an admin queue nothing fills.

## What breaks if you skip it
You never launch, because there's always something to add; or you launch something no one can say is finished.

## The principle behind it
The first version solves the problem, it doesn't tick every idea. Every requirement can be checked by someone other than its author.

## How to apply it at work
On any project, ask: what is the smallest thing we can ship that solves the problem, and how will we know it's done? In refinement, push every ticket to yes/no acceptance criteria.

## Done when
- [ ] success metrics from the cost of the problem, with the user signal, a counter-metric, events or daily counters, a number or `[ASSUMPTION]` for every target, who is counted, small totals hidden
- [ ] 3–5 journeys with a named person, the moment value lands and an edge case
- [ ] a glossary with every domain word the criteria use, used consistently
- [ ] ideas sorted, the MVP justified, dependencies checked, `docs/00-project/ideas.md` rewritten
- [ ] payment, both sides, AI cost, day one, data in and out, and roles checked
- [ ] the MVP size fits the time until launch, or fails on purpose with the decision, the capacity counted from the day it's checked
- [ ] every MVP feature has a one-line description and yes/no criteria, including the main failures, under "Functional requirements"; "Not in MVP" cites the waiting ideas' F-IDs
- [ ] non-functional numbers set, providers as requirements, numbers that agree
- [ ] non-goals and out of scope written
- [ ] assumptions and open decisions listed; the blocking ones answered
- [ ] reviewed or validated, and the ready-for-delivery verdict written in the file
- [ ] after Design: re-read against Design's files, precise criteria and new open decisions written back, risk tests' pass marks in Assumptions, tests named per slice

## Next
Prototype (`/prototype`), optional: when the main flow is new to people. Otherwise Design: the architecture.
