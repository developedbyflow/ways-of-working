# The problem

- **Use it when:** you have an idea for a product, and you need to know who has the problem, what they do today and what it costs them, before anything else.
- **What you get:** one page with the problem, the person, the segment and the cost, checked on 3–5 people; a parking lot for the feature ideas that show up on the way.
- **Run it:** `/wow-problem a calorie tracker I can trust`
- **Not when:**
  - you have no idea yet → `/wow-brainstorm` first;
  - the product is live and you look for what to improve → `/wow-product-review`.
- **Reads:** your notes; the problem picked in `/wow-brainstorm`, if you ran it.
- **Writes:** `docs/product/problem.md`, `docs/product/ideas.md`.

```markdown
# Problem
**Who:** one concrete person: age, situation, what they want
**Segment:** the wider group that person belongs to
**Problem:** what they can't do today, in one or two sentences
**How they solve it today:** each alternative, with what it does well and where it fails
**What it costs them:** time, money or results, in numbers (estimates are fine)
## Verify with others
The questions, then the results: who, what they did, what they use, why they stopped, time per day, what they paid
```

## Steps
1. **One concrete person,** not "anyone who wants to eat healthy". Starting with yourself is fine; say so.
   - Skip it → a problem so vague it decides nothing.
2. **The problem, without the solution.** What they can't do today. Feature ideas that come up go straight to `docs/product/ideas.md`, unsorted.
   - Skip it → a list of features before anyone knows what they solve.
3. **How they solve it today:** other apps, spreadsheets, paper, a person, or nothing. For each: what it does well and where it fails. A workaround they built themselves (templates, a spreadsheet) is the strongest sign the problem is real.
4. **What it costs them, in numbers:** minutes a day, money, months without results. Approximate is fine; vague is not ("~30 minutes a day", not "a lot of time"). These numbers become the success metrics in the PRD.
   - Skip it → no way to tell later whether the product solved anything.
5. **The segment:** the wider group the person belongs to, the one you can reach (for example "developers who want to lose weight").
6. **Verify on 3–5 people from the segment,** with `/wow-interview`: questions about what they did, not about your idea; strangers or acquaintances, not friends being nice; ask for something real at the end (an email for the beta).
   - STOP: do 3 out of 5 describe the same problem? Keep it, change it, or drop it. Not done yet? Write it down as "not yet verified"; it becomes the value test in the brief.
7. **The idea parking lot:** every idea in `docs/product/ideas.md` gets a stable ID (F-01, F-02…) that never changes, even when the order does. Nothing is sorted or discussed until the PRD.

## Done when
- [ ] one concrete person and a reachable segment
- [ ] the problem is written without a solution in it
- [ ] today's alternatives, each with where it fails
- [ ] the cost in numbers
- [ ] verified on 3–5 people, or marked "not yet verified"
- [ ] feature ideas are parked with stable IDs, not discussed

## Concepts if you get stuck
- Jobs to be done
- The Mom Test: questions about their past, not your idea
- Workarounds as evidence

## Next
`/wow-market-research`. End with `/wow-retro`.

## Changelog
- 2026-10-10: v1. Replaces the problem half of `brainstorm.md` and makes interviews the check of this step. From the MacroMate rebuild: a separate "users" step stayed empty until interviews were done, and a 13-feature list arrived before the problem was written.
