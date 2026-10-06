# Pricing

- **Use it when:** you set or change a price, or decide between free and paid.
- **What you get:** a price above your costs, checked against what people would pay, with VAT handled.
- **Run it:** `/wow-pricing the pro plan`
- **Not when:** you're checking what the app costs you to run → `/wow-audit cost`.
- **Reads:** `docs/gtm/positioning.md`, competitor prices from the market research in `docs/research/`, the cost audit, the notes in `docs/interviews/`.
- **Writes:** `docs/gtm/pricing.md`.

## Steps
1. **What they pay for:** per user, per use, per feature or per month. The price should grow with the value they get.
2. **Floor and ceiling:**
   - **floor:** what one customer costs you (hosting, AI tokens, payment fees, support);
   - **ceiling:** what it's worth to them, and what the alternatives cost.
   - Skip it → a price below cost. With AI features this happens often.
3. **The model:**
   - free trial, freemium or paid only;
   - monthly or yearly;
   - at most 2–3 plans at first.

   A free plan needs a reason: it must bring paying users.
4. **Test what they would pay:**
   - in interviews, four questions: at what price is it too cheap to trust, a bargain, getting expensive, too expensive;
   - then a real signal: a pre-order, or a pricing-page fake door (`/wow-experiment`).
5. **Taxes and payments:**
   - EU sales of digital services carry VAT;
   - a merchant of record (Paddle, Lemon Squeezy) handles VAT for you; with Stripe, you set the taxes up yourself (`/wow-integration`);
   - you need invoices and a refund policy.
   - Skip it → legal trouble at the first sale in another EU country.
6. **Decide and write it down:** the price, why, and what would make you change it.
   - STOP: you decide.
7. **Measure after launch:** conversion to paid, cancellations, refunds.

## Done when
- [ ] what they pay for is chosen
- [ ] the floor and ceiling have numbers
- [ ] the model is chosen
- [ ] there is a signal of what people would pay
- [ ] taxes are handled
- [ ] the decision is written

## Concepts if you get stuck
- Value-based pricing
- Van Westendorp price questions
- Merchant of record, EU VAT for digital services

## Next
`/wow-launch`, `/wow-experiment`. End with `/wow-retro`.

## Changelog
- 2026-10-06: v1
