# Spike

- **Use it when:** only building something will answer the question. Does library X do Y? Which UI works? How fast is Z?
- **Not when:** the docs can answer it → `/wow-research`.
- **Reads:** the question.
- **Writes:** the answer, in `docs/research/` or in an ADR. The prototype code gets deleted.

## Steps
1. **The question and a time box:** hours, two days at most.
   - STOP: agree on the time box.
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
- Measuring the frontend → [F12 Web performance](https://claude.ai/artifact/HmfCtXjvx5CPXY2tPHt8Mc)
- Measuring the backend → [Backend 07 Performance](https://claude.ai/artifact/HDsFaNVTSoZC3EkyVTRngm)

## Next
`/wow-grill`, `/wow-feature` or `/wow-design-doc`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
