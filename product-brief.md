# Product brief

- **Use it when:** you picked an idea (a new product, or a big new area of one) and need one page everyone agrees on before writing requirements.
- **What you get:** one page everyone agrees on, with the buyer named, the boundary drawn, and the four risks and how to test each.
- **Run it:** `/wow-product-brief the meal planner`
- **Not when:** you're writing the requirements themselves → `/wow-prd`.
- **Reads:** `docs/product/ideas.md`, the notes in `docs/interviews/`, the market research in `docs/research/`, `docs/opportunities.md`.
- **Writes:** `docs/product/brief.md`.

```markdown
# <Product> brief
Summary: one paragraph that stands alone: what it is, for whom, why now
Problem: the job story, the evidence for it, and what the status quo costs them (hours, money, fines)
Who it's for first: the narrowest group that has the problem worst, and whether they must buy or want to
What they use today, and why it falls short
Our idea, in one paragraph; every number in it marked as evidence or guess
What makes it different, honestly: if the moat is "first in a small market", say so
Why now
Scope: in the first version, and explicitly out
How we'll know it works: the number, who pays it and at what price, and one leading indicator before the gate
Risks: value · usability · feasibility · viability, and how we test each, on the first version
Vision: where it goes in 2–3 years, with the ceiling
Decision: go, change, or drop, and why
```

## Steps
1. **Fill it from evidence.** Mark every guess as a guess, including the numbers inside the idea paragraph. A law or a trend is not the pain; the pain is what the status quo costs them: hours, money, fines. Write the cost.
   - Skip it → a confident page built on opinions.
2. **Check the buyer.** Who **must** buy (obliged by law, losing money, at risk) and who **wants** to (would like a tool)? Read the law or the contract yourself; a competitor's blog says what suits the competitor. Name the obliged party. If you pick the other one, write why.
   - Skip it → you sell a tool to the one who wants it, while the one who must pay buys a service from somebody else.
3. **The four risks:**
   - **value:** will they want it?
   - **usability:** can they use it?
   - **feasibility:** can we build it?
   - **viability:** does it work for the business (money, legal, reputation)?

   For each, write how you'll test it. Test the unknowns of the first version, not of the module that comes second.
   - Skip it → you test only feasibility, because that's what developers enjoy.
4. **Scope and sequence.** What the first version does, and what it explicitly doesn't. Nothing with a screen before the buyer is confirmed; until then build only what doesn't depend on the buyer, as tests.
   - Skip it → month one builds for the wrong buyer, and the PRD inherits a product with no edges.
5. **Optional: work backwards.** Write the launch announcement and its FAQ as if the product had already shipped. If the announcement is boring, the product is too.
6. **Optional: a lean canvas** (problem, customer groups, unique value, solution, channels, revenue, costs, key numbers, unfair advantage), when the business model is the open question and the brief doesn't already answer it. Don't repeat the brief in a table.
7. **Read by someone else.**
   - STOP: someone outside the idea reads it and tells you what they think it is. If they can't, rewrite it.
   - Nobody at hand? Run `/wow-product-brief validate <file>` (the Validate mode in `SKILLS.md`), then a critique against a different template (for example `/bmad-product-brief validate`). A second method finds the holes the first one hides: an inverted buyer, a test aimed at the wrong module, a missing boundary.
8. **Decide:** go, change, or drop.
   - STOP: you decide. When the honest answer is "I can't decide without talking to five people", write that as the decision, with the date you'll have talked to them.

## Done when
- [ ] one page, two at most
- [ ] every claim has evidence or is marked as a guess
- [ ] the buyer is the obliged party, or the brief says why not
- [ ] scope in and out is written
- [ ] the four risks each have a test, on the first version
- [ ] the number says who pays and at what price
- [ ] the decision is written

## Concepts if you get stuck
- The four product risks
- Must buy vs want to buy
- Working backwards: the press release and FAQ
- Lean canvas

## Next
`/wow-prd`, `/wow-experiment`, `/wow-interview` when the buyer is still open, `/wow-positioning`. End with `/wow-retro`.

## Changelog
- 2026-10-07: v2.1. Step 7 points to the Validate mode of `SKILLS.md`.
- 2026-10-07: v2. Added the summary, the buyer check (must vs want, read the law yourself), the cost of the status quo, scope and sequence, honest differentiation, the vision with its ceiling, "who pays and at what price" in the number, and the second-template critique as a stand-in outside reader. Source: the ProjectX dietitian-platform brief, validated against the BMad product-brief template. The v1 page produced an honest, testable brief that still inverted the buyer (the law obliges the unit; the brief picked the dietitian), aimed the spike at the second module, and had no boundary.
- 2026-10-06: v1
