# Research

- **Use it when:**
  - official docs or other primary sources can answer the question;
  - you're choosing a library or a vendor;
  - you're deciding whether to build or buy.
- **What you get:** an answer from official sources, with versions and dates, instead of a blog post from three versions ago.
- **Run it:** `/wow-research which date library for React Native?`
- **Not when:** only building something will answer it → `/wow-spike`.
- **Reads:** official docs, specs, release notes, source code, issue trackers. Blog posts come last.
- **Writes:** `docs/research/YYYY-MM-topic.md` (question, answer, sources, date), or the ADR directly.

## Steps
1. **The question in one sentence**, what you'll decide with the answer, and a time limit.
   - STOP: confirm.
2. **Sources, best first:**
   1. docs and specs;
   2. source code and release notes;
   3. issue tracker;
   4. posts by the people who build the tool.

   Every claim gets its link and the version it applies to.
   - Skip it → you build on a blog post written three versions ago.
3. **Choosing a library or vendor:** score each candidate on the same criteria.
   - **Fit:** does it do the job without hacks?
   - **Performance:** bundle size on the frontend; latency and memory on the backend.
   - **Developer experience:** types, docs, error messages.
   - **Health:** last release, open issues, number of maintainers.
   - **Risk:** security history, license, lock-in, the cost of moving away.
   - **Cost:** price, time, learning.
   - Skip it → you pick by hype or habit.
4. **Build or buy:**
   - Build only when it's what makes your product different, or when nothing fits.
   - Count the cost of running it for two years, not just the cost of building it.
5. **The answer:** one paragraph, the recommendation, and what is still unknown.
   - STOP: you decide. A decision becomes an ADR.

## Done when
- [ ] every claim has a source with a version, and the note has a date
- [ ] the decision is in an ADR

## Concepts if you get stuck
- Trade-offs
- Evaluating technology as a lead
- Packages, versions, the supply chain

## Next level
- `staff` A one-page evaluation template the whole team reuses.

## Next
`/wow-grill`, `/wow-spike`, `/wow-design-doc` or `/wow-upgrade`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
