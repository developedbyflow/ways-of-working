# Launch

- **Use it when:** you put a product, or a big feature, in front of the public.
- **What you get:** a launch where the product can take money, and you know which channel worked.
- **Run it:** `/wow-launch version 1`
- **Not when:** you're shipping code → `/wow-deploy`.
- **Reads:** `docs/gtm/positioning.md`, `docs/gtm/pricing.md`, the first version in `docs/product/prd.md`, the production-readiness audit.
- **Writes:** `docs/gtm/launch-plan.md`, the landing page text, the launch checklist.

## Steps
1. **Goal and number:** sign-ups, paying users or waitlist size, within a time window.
2. **Ready to sell:**
   - `/wow-audit production-readiness` and `/wow-audit privacy` are done;
   - payments are tested in live mode;
   - terms of service and a privacy policy are published;
   - a support email works;
   - the launch events are in the tracking plan.
   - STOP: every item is green.
   - Skip it → the launch brings users to something that breaks or can't take money.
3. **The landing page:**
   - the message from the positioning, with one call to action;
   - proof: screenshots, a demo video, quotes;
   - fast and accessible (`audits/performance.md`, `audits/accessibility.md`, `audits/seo.md`).
4. **An audience before launch:** a waitlist, the people you interviewed, the places where your best-fit customers gather.
   - Skip it → you launch to nobody.
5. **Channels:** pick 2–3 (Product Hunt, communities, your YouTube or X, newsletters, partners). For each: the post and the date.
6. **The demo:** a 1–2 minute video that shows the job done from start to finish.
7. **Launch day and the week after:** watch the numbers and the errors, answer every comment, fix what blocks people (`/wow-incident` if needed).
8. **Results by channel:** what brought users and how many converted. They feed `/wow-growth`.

## Done when
- [ ] the ready-to-sell checklist is green
- [ ] the landing page is live
- [ ] the channels are scheduled
- [ ] the results by channel are written

## Concepts if you get stuck
- SEO for developers
- UX for developers
- The product-minded engineer

## Next
`/wow-growth`. End with `/wow-retro`.

## Changelog
- 2026-10-06: v1
