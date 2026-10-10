# Market research

- **Use it when:** you know the problem and need to know whether the market is worth it: who else solves it, at what price, how many customers there are, and whether you can reach them.
- **What you get:** competitors, prices, what is a differentiator and what is only expected, a bottom-up size, and how many people you must reach for your goal, every number with its source.
- **Run it:** `/wow-market-research meal-planning apps in Europe`
- **Not when:** you're choosing a library or a vendor → `/wow-research`.
- **Reads:** `docs/product/problem.md`, the notes in `docs/interviews/`.
- **Writes:** `docs/research/YYYY-MM-market-<topic>.md`, with sources and dates.

## Steps
1. **The question:** which decision will this research support? Go or no-go, which group of customers, which price. Set a time box.
   - STOP: confirm the question.
2. **Competitors and alternatives:**
   - direct: the same kind of product;
   - indirect: a different product that does the same job;
   - doing nothing.

   For each one: who it's for, its price **per month and per year** (most people pay yearly, at a discount), its main promise, and what users praise and complain about.
   - Skip it → you discover them after launch.
3. **What customers say:** reviews in app stores, comparison sites, Reddit, forums. What they love, what they hate, what they wish for. Quote with links. A competitor's blog about its rivals is a lead, not evidence.
4. **Differentiator or expected?** Split your features in two: what at least one major competitor already does (expected, nobody switches for it) and what nobody does well (a reason to switch).
   - Skip it → "verified data" or "many languages" sold as unique when they are the minimum.
5. **Size, from the bottom up:** the number of customers you can reach × what they would pay per year. Top-down numbers from reports serve only as a sanity check, with their source.
   - Skip it → a "1% of a billion" slide nobody can act on.
6. **Work back from the goal:** the revenue goal ÷ the price = paying users; ÷ the conversion rate = sign-ups; ÷ the visit-to-sign-up rate = people who must see it. Usually the bottleneck is reach, not market size.
7. **The channel fits the user:** does the channel you plan (a YouTube channel, a community, ads) reach the people who have the problem, or only people like you?
   - Skip it → an audience that likes the content and never buys the product.
8. **Why now:** what changed (technology, rules, habits) that makes this possible or needed now.
9. **The answer:** a recommendation, the price hypothesis, plus what is still unknown.
   - STOP: decide.

Every number has a source and a date. Estimates are labelled as estimates.

## Done when
- [ ] the competitor table is filled in, with monthly and yearly prices
- [ ] customer quotes come with links
- [ ] features are split into differentiators and expected
- [ ] the size is estimated from the bottom up
- [ ] the funnel is worked back from the goal, and the channel is checked against the user
- [ ] the recommendation and the price hypothesis are written

## Concepts if you get stuck
- Competitive alternatives
- Table stakes vs differentiators
- Bottom-up market sizing
- Conversion funnel
- Why now

## Next level
- `staff` A competitor watch: update the table every quarter.

## Next
`/wow-product-brief`, `/wow-positioning`. End with `/wow-retro`.

## Changelog
- 2026-10-10: v2. Monthly and yearly prices; differentiators split from what is only expected; the funnel worked back from the goal; the channel checked against the user. From the MacroMate rebuild: $12/month looked high until yearly prices were compared, "verified food data" turned out to be expected, and a YouTube channel about building the app reaches developers who build apps, not people who want to lose weight.
- 2026-10-06: v1
