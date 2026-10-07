# Spike

- **Use it when:** only building something will answer the question. Does library X do Y? Which UI works? How fast is Z?
- **What you get:** a measured answer in hours, and no prototype code left in production.
- **Run it:** `/wow-spike can IndexedDB hold 10,000 meals offline fast enough?`
- **Not when:** the docs can answer it → `/wow-research`.
- **Reads:** the question, or the document it comes from: a brief's feasibility test, a PRD's open question. Extract the questions from the document; the user doesn't restate them.
- **Writes:** the answer, in `docs/research/` or in an ADR. The prototype code gets deleted.

## Steps
1. **The question and a time box:** hours, two days at most. Several questions from one document → one table: question, expected answer, time box.
   - STOP: agree on the time box. When the questions come from a brief or a PRD, fold this into the page confirmation: one line, one answer.
   - Skip it → the spike quietly becomes the feature.
2. **Build the smallest thing that answers it**, on a throwaway branch. No tests, no polish.
   - **UI questions:** 2–3 variants you can switch between on one page.
   - **Logic or speed questions:** one script with a measurement.
3. **Show it:** the number, a screenshot or a recording.
4. **Write the answer:** what you learned, the number, your recommendation, and what is still unknown.
   - STOP: decide.
5. **Throw the code away**, then build it properly with `/wow-feature`.
   - Skip it → prototype code without tests reaches production.

## Done when
- [ ] the question is answered in writing
- [ ] the branch is deleted

## Concepts if you get stuck
- Measuring the frontend
- Measuring the backend

## Next
`/wow-grill`, `/wow-feature` or `/wow-design-doc`. End with `/wow-retro`.

## Changelog
- 2026-10-07: reads the brief or PRD the questions come from; several questions as one table; one STOP, not two.
- 2026-10-05: v1
