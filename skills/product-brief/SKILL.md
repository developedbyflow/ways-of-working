---
name: product-brief
description: "One page that decides whether to build. A summary from 01–02, the goal in paying users, the four risks each with a test and a pass mark set in advance, scope in and out, and a decision: go, go with conditions, change or stop. Use after the problem and the market research, before writing requirements. Also judges an existing brief: /product-brief validate <file>."
argument-hint: "[the product] or validate <file>"
---

# Product brief

## When to use it
After the problem (01) and the market research (02), before describing features in the PRD.

## The problem it solves
Everything you know about the product on one page, and a conscious decision to go on, change something or stop. The decision is the end of the brief.

## How to run it
- **The bar:** do what a senior engineer or the C-level who owns this area (CEO, CPO, CTO, CFO, CMO, COO) at a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it, so the user learns it. Senior also means knowing what to leave out: say what you skip and why.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Every `docs/…` path below means that folder.
- **Spot risky assumptions for the user:** when a decision here rests on something nobody has checked ("I think people will…", "the AI can probably…") and being wrong would cost a lot, stop and propose a risk test: what to check, how long it takes, the pass mark, and when it must be done. The user only says yes or no; run it with `/risk-tests`. Don't propose one for cheap, easy-to-undo choices.
- **Read first:** `docs/01-discovery/01-problem.md`, `docs/01-discovery/02-market-research.md`, `docs/00-project/ideas.md`. Ask only what is missing.
- **Summarise, don't repeat.** Link to 01 and 02 for the detail. One page, two at most.
- **Mark every claim** as evidence (with where it comes from) or as a guess.
- **Push back when an answer is thin,** especially on the goal, the risks and the pass marks. The user decides; the brief must feel like theirs.
- **Feature details belong in the PRD,** not here. New feature ideas go to `docs/00-project/ideas.md`, under "New", with the next ID.

## Steps

### 1. The summary
From 01 and 02, one or two lines each:
- **Problem**, **users**, **market**, **why now**;
- **the solution:** what the product does for the user, as an experience and an outcome, not a feature list;
- **differentiators:** only the ones from 02 that answer a real complaint. Be honest: if the edge is focus or speed, say so; don't invent a moat.

### 2. The goal in people
A revenue goal decides nothing; the number of paying users it needs does.
- goal ÷ what's left per paying user (step 4) = paying users, not goal ÷ price. Do it once for the monthly and once for the yearly price, in one currency, with the conversion written: the real number sits between, by the mix (for example €2,000/month ≈ ~226–425 paying users at \$12/month or \$80/year, at \$1 ≈ €0.90).
- By when.
- **One user signal** that shows the product works for them (for example "logs food 5 days a week after the first month"). Revenue tells you late; this tells you early.

### 3. Who pays
- **For consumers:** the user pays. Check the price against 02.
- **For businesses, or when someone is obliged to buy:** who **must** buy (a law, a contract, losing money) and who only **wants** to? Read the law or the contract yourself and name the obliged party. Selling to the one who wants it while the one who must pay buys elsewhere is the classic mistake.

### 4. Rough money check
Price minus what each paying user costs you per month: payment fees, hosting, AI calls, email, support time. One column per way of paying (monthly, yearly, through a store), and two rows of "left":
- **the typical user**, and **the heavy user**: the one who uses every paid call they're allowed. Bound them by a monthly AI budget per person, not only a daily cap: a daily cap alone lets one user cost more than they pay. Count the users who don't pay (a trial) too.
- **Fees, with their source and date.** A subscription without a merchant of record, for example Stripe in the EEA: 1.5% + €0.25 a card payment, plus 0.7% for Billing and 0.5% for Tax (stripe.com/ie/pricing, read 2026-11-11), and you handle VAT yourself. A merchant of record, which handles VAT for you: ~5% + \$0.50 (Paddle). App stores: 15% for a small seller (Apple's Small Business Program; Google Play's EEA subscriptions 10% + a 5% billing fee, read 2026-11-11). **Say whether VAT is inside the base** of every fee: a 5% taken on a price with 21% VAT costs more than on the price before it.
- **Guesses first, real costs later.** Before Design it's guesses, marked as such. Once the system design's monthly cost exists, redo the table from it, in the same commit as the cost. The journal never says "replaced" while the table isn't (MacroMate's journal said so twice while the table kept October's guesses for a month).

If the margin is thin or negative at your price, it's a viability risk for step 5.

### 5. The four risks
Marty Cagan's four product risks (*Inspired*). First find them with a **pre-mortem:** "It's a year later and the product failed. Why?" Write every reason, then sort them into the four types:
- **value:** will people want it? (usually the interviews from 01, at least 5 people from the segment, not only friends: "3 out of 5")
- **usability:** can they use it? (a few screens as a clickable prototype, shown to 5 people before any code: Nielsen's 5 users find most problems)
- **feasibility:** can it be built? (do you have the data, does the AI do it well enough: "20 out of 30 correct")
- **viability:** does it work as a business? (reach, money from step 4, legal: "100 sign-ups before launch"); some teams call it **business** risk.

Each pre-mortem reason gets a **Covered by:** the risk test, the money check, a rule, or "not tested" with why. A reason with nothing in that column is a risk nobody is watching.

For each risk: a test, a **pass mark set now, before the test**, **what a fail sends back** (which decision is redone, what is dropped or switched off), how long the test takes, **when it runs** (the gate that depends on it: "before the architecture", "before slice 1", "before launch"), and a status with its date. Put the riskiest first: the one that would hurt most if wrong and that you are least sure about. If the rows are sorted some other way, say the order they must pass in, by gate, in one line above the table. Test what the first version needs, not what comes second.

### 6. Scope
What the first version does, as a few capabilities, and what it explicitly doesn't. The boundary, not a feature list; the PRD turns it into features.

### 7. Vision
Where it goes in 2–3 years if it works, in two or three lines, and its ceiling: what would stop it from growing further.

### 8. Open decisions
Every decision still open, what it blocks, who answers, by when, and what kind of door it is:
- **one-way door:** hard to undo (a price promised to early users, a data model, a legal entity). Take the time, write the reasoning.
- **two-way door:** easy to undo (a name, a screen, a free tier). Decide fast and move on.

Those that block the PRD are asked now, as questions with a recommended answer.

### 9. Optional: working backwards (PRFAQ)
When the summary feels flat or the user isn't sure what the product is, use Amazon's Working Backwards: write the launch as if it had shipped, before building.
- **The press release,** under a page: a headline, who it's for, the problem, how it solves it, a quote from a user, how to start, the price.
- **The customer FAQ:** what a buyer would ask ("how much?", "why not [competitor]?", "what happens to my data?", "what if I stop paying?").
- **The internal FAQ:** what the team would ask ("what's hardest to build?", "what does a user cost us?", "what did we leave out?", "what kills this?").
- **Hard mode:** challenge every vague answer and every claim without evidence. If the press release is boring, the product is too.

The press release makes a good signup page for the value test (`/risk-tests`): the promise is already written. Shown to people from the segment, it turns from a thinking tool into evidence.

When the business model itself is the open question, add a lean canvas instead.

### 10. An outside reader
Someone outside the idea reads the page and says back what the product is and for whom. If they can't, rewrite. Nobody at hand? Run `/product-brief validate <file>`.

### 11. The decision
- **Go**, **go with conditions** (start the PRD while the tests run), **change** or **stop**, and why.
- **The fallback:** what's left if it doesn't work (for example "my own tool and a portfolio project").
- **Where it stands ([date]):** one line under the decision, kept current as the project moves: which steps are done, each test's status and gate, and why the decision still holds.
- When a test fails later, come back to this page, decide again, and add a line to the journal.
- **Later changes are marked** in place, "(added [date])" or "(corrected [date]: it said …)", and each gets a journal line: what changed, who decided, why. The page stays readable and its history stays checkable.

Then write `docs/01-discovery/03-product-brief.md`:

```markdown
# 03 – Product brief
## Summary
- **Problem:** … **Users:** … **Market:** … **Why now:** …
- **Solution:** …
- **Differentiators:** …
## Goal
- [goal] ≈ [N–M] paying users at [price/month or price/year], from what's left per user, at [conversion], by [date]
- **User signal:** …
## Who pays
## Money check
Per paying user per month, [before / with] VAT; source: [guesses / the system design's cost].
| | Monthly | Yearly | Through a store |
|---|---|---|---|
| Price | | | |
| Fees (VAT in the base or not) | | | |
| AI, a typical user | | | |
| AI of the users who don't pay | | | |
| Hosting and the rest | | | |
| **Left, typical user** | | | |
| AI, a heavy user: the monthly budget used up | | | |
| **Left, heavy user** | | | |
## Pre-mortem
| Reason | Type | Covered by |
## Risks and how I test them
Order they must pass in: …
| Risk | Type | Test | Pass if | If it fails | Takes | When | Status |
## Scope
**In the first version:** … **Out:** …
## Vision
## Open decisions
| Decision | One-way or two-way | Blocks | Who | By when |
## Decision
**[Go / go with conditions / change / stop]**, because …
**Where it stands ([date]):** …
**Fallback:** …
## Journal
- [date]: [what was decided, by whom, what it changed]
```

## Validate mode
`/product-brief validate <file>`: judge an existing brief, change nothing.
1. Read the brief, its journal, 01 and 02. A critique that ignores what was already decided is shallow.
2. Check the template and "Done when" item by item, citing the lines.
3. Then ask what no template asks: who must act or pay, and is that who the brief names? Is every number marked as evidence or guess, including inside the prose? Does the money check match the system design's cost, and does the journal claim a change the table doesn't show? Does each test aim at the first version, and say what a fail sends back? Was each pass mark set before the test? What is explicitly out? What does doing nothing cost?
4. Go to the primary source for any claim that rests on a law, a contract or a price.
5. Report: findings by severity, each with the line, what's wrong and what to change; then what the brief does well; then what you couldn't evaluate. The user picks what to apply.

## The bad version and why not
- Going straight to code because "the idea is good".
- Testing only feasibility, because that's what developers enjoy.
- Setting the pass mark after the test → every result looks like a pass.
- A test with no failure path: when it fails, nobody knows what to undo, so it gets explained away.
- A money check left at its first guesses after the real costs exist, with a journal line saying it was updated.
- A moat that isn't there ("our AI is better").
- Five pages: nobody reads it, so nobody challenges it.

## What breaks if you skip it
You spend months on an idea you never weighed, and you have no line to tell you when to stop.

## The principle behind it
A written decision can be checked later. Decide what counts as success before you see the result.

## How to apply it at work
Before a big project, ask for a one-page brief: the problem, the market, the four risks with tests, and the decision. In a kickoff, run the pre-mortem.

## Done when
- [ ] one page, two at most (the journal and the dated marks of later changes not counted), linking to 01 and 02 instead of repeating them
- [ ] every claim marked as evidence or guess
- [ ] the goal in paying users, with a date and a user signal
- [ ] who pays is named; for B2B, who must buy
- [ ] the money check per user, typical and heavy (bounded by a monthly AI budget), every fee sourced and dated, VAT in or out of its base; redone from the system design's cost once it exists
- [ ] the goal's paying users from what's left per user, in one currency, the conversion written
- [ ] a pre-mortem whose every reason has a "Covered by"
- [ ] the four risks, each with a test, a pass mark set in advance, what a fail sends back, a gate and a dated status; riskiest first, or the order by gate said
- [ ] scope in and out
- [ ] open decisions with what they block, who and by when
- [ ] read by someone outside the idea, or validated
- [ ] the decision, where it stands (dated), the fallback and the first journal line; later changes marked "(added/corrected [date])" with a journal line each

## Next
PRD (`/prd`). The risk tests run in parallel with it (`/risk-tests`).
