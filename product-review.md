# Product review (an existing product)

- **Use it when:** you have a live product and need to decide what to improve next.
- **What you get:** the 1–3 improvements most likely to move your main number, with the evidence.
- **Run it:** `/wow-product-review the meal planner`
- **Not when:** you're checking one quality area (accessibility, performance and so on) → `/wow-audit`.
- **Reads:** analytics (funnel, retention), support tickets, app reviews, the notes in `docs/interviews/`, `docs/tracking-plan.md`, `docs/experiments/`.
- **Writes:** `docs/product/review-YYYY-MM.md`, `docs/opportunities.md`.

## Steps
1. **The outcome:** the one number you want to move this quarter: activation, retention or revenue.
   - STOP: agree on it.
   - Skip it → you improve things that don't matter.
2. **The numbers:**
   - the funnel, step by step: visit → sign-up → first value → habit → paid;
   - where the biggest drop is;
   - retention by sign-up week: do people come back after one week, and after four?
   - Skip it → you guess where it hurts.
3. **What users say:** support tickets, reviews, interview notes, reasons for cancelling. Group them, and count each group.
4. **Opportunities:** the needs and pains that would move the outcome if you solved them. Draw them as a tree: outcome → opportunities → solution ideas.
   - Skip it → a feature list with no link to the number.
5. **Pick:** compare the opportunities by impact, confidence (how much evidence) and effort, with RICE.
   - STOP: you pick 1–3.
6. **Test before building:** each picked solution gets its riskiest assumption tested small first (`/wow-experiment`), then built (`/wow-feature`).

## Done when
- [ ] the outcome is chosen
- [ ] the funnel has its numbers
- [ ] user feedback is grouped and counted
- [ ] the opportunity tree exists, and 1–3 picks have evidence

## Concepts if you get stuck
- Funnel and retention by cohort
- Opportunity solution tree
- RICE

## Next level
- A product review every month.
- `staff` Team goals tied to outcomes, not to features.

## Next
`/wow-experiment`, `/wow-prd`, `/wow-roadmap`, `/wow-feature`. End with `/wow-retro`.

## Changelog
- 2026-10-06: v1
