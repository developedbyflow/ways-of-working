---
name: discovery-market-research
description: "Discovery, step 02: what already exists, how big the market is, why now, and how many people you must reach to hit the goal. Use after the problem is written (docs/01-problem.md), before choosing features."
argument-hint: "[the product or the problem]"
---

# Discovery · 02 Market research

## When to use it
After you know the problem and who it's for (01), before choosing features.

## The problem it solves
Three answers: what already exists, how big the market is, why now.

## Steps
Read `docs/01-problem.md` first. Do the research yourself, one step at a time, and show each result before the next. Every number gets its source, or is marked "guess". Prices come from the vendor's own price page, read directly.

1. **The list:** the apps and tools people use today for this problem. Start from "How they solve it today" in 01.
2. **For each one:** what it does well, what it does badly (from user reviews), what it costs. Quote 1–2 real complaints with links. A competitor's blog about its rivals is a lead, not evidence.
3. **Split the features in two:**
   - **expected:** at least one competitor has it. You need it, but it doesn't set you apart;
   - **differentiators:** no major competitor does it.
4. **Prices per month and per year.** Most people pay yearly, at a discount.
5. **Market size, bottom-up:** people you can reach × what they'd pay a year. Industry report figures only as a sanity check, with their source.
6. **Why now:** is the market growing or shrinking, what changed (a technology, a law, a habit, a competitor getting worse). Note any rule that limits what you can build or claim (health data, medical claims, payments).
7. **Work back from the goal.** Ask the user for the goal (for example 250 paying users). Then: how many sign-ups that needs, and how many people must see the product. Use a table, one assumption per row. This, not market size, is usually the bottleneck.
8. **The channel:** where those people are. Check that the channel's audience is the user from 01, not someone else.
9. **The answer:** go, change or stop; the price you'll test; what is still unknown. The user decides.

Then write `docs/02-market-research.md`:

```markdown
# 02 – Market research
Researched [month year]. Prices and estimates are approximate.
## 1. Competitors
| App | Price / month | Price / year | Good at | Main complaint |
### Expected (not a differentiator)
### Differentiators (no major app does these)
## 2. Market size
## 3. Funnel from the goal
| Step | Assumption | Source or "guess" | Result |
## 4. Why now
## 5. Channel
## 6. Answer
Go / change / stop, the price to test, what is still unknown.
## Sources
```

## The bad version and why not
- "There's nothing like it" → there almost always is.
- Listing as differentiators things others already have (for example a verified database, many languages). That's only the minimum people expect.
- Picking a channel whose audience isn't your user (for example programming videos for a nutrition app).

## What breaks if you skip it
You build something that already exists, better and cheaper.

## The principle behind it
You are only better compared to something specific.

## How to apply it at work
Before a new feature or tool, check: does something already do this?

## Done when
- [ ] every alternative from 01 is in the table, with monthly and yearly prices
- [ ] features split into expected and differentiators
- [ ] market size, with sources
- [ ] why now, with at least one concrete change
- [ ] the funnel from the goal, every assumption marked as a source or a guess
- [ ] the channel checked against the user from 01
- [ ] an answer: go, change or stop, decided by the user

## Next
Discovery · 03 Product brief (`/discovery-product-brief`).
