# Pull request

- **Use it when:** you open your own PR.
- **Not when:** you're reviewing someone else's → `/wow-review`.
- **Reads:** the ticket, your diff, `docs/definition-of-done.md`.
- **Writes:** the PR description, plus a line for the release notes when users will notice the change.

## Steps
1. **Review your own diff first** → `/wow-review`. Fix what it finds before anyone else sees it.
   - Skip it → reviewers spend their time on what you would have caught.
2. **Size:** one purpose per PR, with refactoring separate from behavior changes. Keep it small enough to review in one sitting.
   - Skip it → slow, shallow reviews.
3. **The description:**
   ```markdown
   ## What and why
   One paragraph, plus the ticket link.
   ## What it looks like
   A screenshot or GIF (UI) · a request and its response (API) · a diagram (flow)
   ## Proof it works
   The tests added · numbers before and after · how I tested it
   ## Risk
   Can it be undone? (flag off, revert) Or not? (data migration, emails sent)
   Who is affected if it breaks?
   ## How to test it
   Steps for the reviewer
   ```
   - Skip the risk section → a change that can't be undone merges like a typo fix.
4. **Commits:** `type(scope): summary`, in English.
5. **Before opening:** checks green, definition of done ticked.
   - STOP: you open it and you merge it. The skill never pushes.

## Done when
- [ ] the description has the picture, the proof and the risk
- [ ] CI is green
- [ ] the definition of done is ticked

## Concepts if you get stuck
- CI and the pipeline
- Good PRs as a lead

## Next level
- Stacked PRs for a long feature: small PRs that build on each other.
- `staff` A PR template for the team, with the risk section.

## Next
After the merge → `/wow-deploy`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
