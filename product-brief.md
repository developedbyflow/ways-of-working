# Product brief

- **Use it when:** you know the problem and the market, and need one page that decides whether to build it, before writing requirements.
- **What you get:** one page with what you learned, the four risks each with a test and a pass mark, and a decision.
- **Run it:** `/wow-product-brief the meal planner`
- **Not when:** you're writing the requirements themselves → `/wow-prd`.
- **Reads:** `docs/product/problem.md`, the market research in `docs/research/`, the notes in `docs/interviews/`.
- **Writes:** `docs/product/brief.md`.

```markdown
# <Product> brief
## Summary
- Problem · Users · Market · Why now · Differentiators
- Goal: the revenue or usage goal, translated into people (e.g. €2,000/month ≈ 190–300 paying users at $12)
## Biggest risks and how I test them
| Risk | Type (value · usability · feasibility · viability) | Test | Pass if |
## Scope: in the first version, and explicitly out
## Open decisions: what each blocks, who answers, by when
## Decision: go, go with conditions, change, or drop, and why
Fallback: what's left if it doesn't work (e.g. my own tool and a portfolio project)
```

## Steps
1. **Summarise from evidence.** Pull the problem, the users, the market and why now from `problem.md` and the market research. Mark every guess as a guess. Feature details belong in the PRD, not here.
   - Skip it → a confident page built on opinions.
2. **The goal in people.** A revenue goal decides nothing; the number of paying users it needs does: goal ÷ price.
3. **The four risks**, each with a test and a pass mark you can count:
   - **value:** will they want it? (the 3–5 people from `/wow-problem`: "3 out of 5")
   - **usability:** can they use it? (a few screens as a prototype, shown to 3 people before any code)
   - **feasibility:** can we build it? (do we have the data, does the AI do it well enough: "20 out of 30")
   - **viability:** does it work for the business: reach, money, legal? ("100 sign-ups before launch")

   Test the unknowns of the first version, not of what comes second.
   - Skip it → you test only feasibility, because that's what developers enjoy.
4. **Only for B2B, or when someone is obliged to buy:** who **must** buy (law, contract, losing money) and who only **wants** to? Read the law or the contract yourself and name the obliged party.
   - Skip it → you sell a tool to the one who wants it, while the one who must pay buys elsewhere.
5. **Scope:** what the first version does, and what it explicitly doesn't.
   - Skip it → the PRD inherits a product with no edges.
6. **Optional:** the launch announcement and its FAQ written as if it had shipped (if it's boring, the product is too); a lean canvas when the business model is the open question.
7. **Read by someone else.**
   - STOP: someone outside the idea reads it and tells you what they think it is. If they can't, rewrite it.
   - Nobody at hand? Run `/wow-product-brief validate <file>` (the Validate mode in `SKILLS.md`), then a critique against a different template (for example `/bmad-product-brief validate`).
8. **Decide:** go, go with conditions, change, or drop; write the fallback.
   - STOP: you decide. A test that fails later brings you back to this page to decide again.

## Done when
- [ ] one page, two at most
- [ ] every claim has evidence or is marked as a guess
- [ ] the goal is translated into paying users
- [ ] the four risks each have a test and a pass mark, on the first version
- [ ] scope in and out is written
- [ ] open decisions have an owner and a date
- [ ] the decision and the fallback are written

## Concepts if you get stuck
- The four product risks
- Must buy vs want to buy (B2B)
- Working backwards: the press release and FAQ
- Lean canvas

## Next
`/wow-prd`, `/wow-experiment` for the risk tests, `/wow-positioning`. End with `/wow-retro`.

## Changelog
- 2026-10-10: v3. Shorter: it summarises `problem.md` and the market research instead of repeating them; the goal is translated into paying users; every risk test has a pass mark, and usability is tested with a prototype; the buyer check applies to B2B; "go with conditions" and a fallback. From the MacroMate rebuild, where the separate users step was folded into the problem and the brief missed the usability risk.
- 2026-10-07: v2.1. Step 7 points to the Validate mode of `SKILLS.md`.
- 2026-10-07: v2. Added the summary, the buyer check (must vs want, read the law yourself), the cost of the status quo, scope and sequence, honest differentiation, the vision with its ceiling, "who pays and at what price" in the number, and the second-template critique as a stand-in outside reader. Source: the ProjectX dietitian-platform brief, validated against the BMad product-brief template. The v1 page produced an honest, testable brief that still inverted the buyer (the law obliges the unit; the brief picked the dietitian), aimed the spike at the second module, and had no boundary.
- 2026-10-06: v1
