---
name: discovery-risk-tests
description: "Discovery, in parallel from step 03: run the risk tests from the product brief honestly. Pick the riskiest, write the hypothesis with the pass mark set in the brief, choose the cheapest test that answers it (signup page, fake door, spike on real data, waitlist, price page, cost check), run it, compare with the pass mark, decide, and update the brief. Use after the brief, alongside the PRD and the build, until every risk has a result. Also judges an existing test: /discovery-risk-tests validate <file>."
argument-hint: "[the risk to test] or validate <file>"
---

# Discovery · Risk tests (in parallel)

## When to use it
After the brief (03), for each risk in its table. Runs alongside the PRD and the build, until every risk has a result.

## The problem it solves
The brief writes the tests; this step runs them honestly and decides from them. Without it, the tests stay on paper and you build on assumptions.

## How to run it
- **The bar:** do what a senior engineer or the C-level who owns this area (CEO, CPO, CTO, CFO, CMO, COO) at a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it, so the user learns it. Senior also means knowing what to leave out: say what you skip and why.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Every `docs/…` path below means that folder.
- **Read first:** the risk table and the journal in `docs/01-discovery/03-product-brief.md`, and `docs/01-discovery/risk-tests.md` if it exists.
- **One test at a time.** The user runs it; you help design it and read the result.
- **The pass mark never moves after the result.** If it was wrong, say so in the journal and set a new one for the next test.
- **Nothing outside this machine without the user:** no page published, no email sent, no money taken.

## Steps

### 1. Pick the test
The riskiest open one: it would hurt most if wrong, and you are least sure about it. Usually value or viability before feasibility, because those are the ones developers avoid.

### 2. The hypothesis
> We believe [what]. We'll know it's true if [pass mark] by [date].

The pass mark is the one in the brief. Also write what would make the result unclear (too few people, a broken page).

### 3. The cheapest test that answers it

| Risk | Tests, cheapest first |
|---|---|
| **Value:** will they want it? | the interviews from 01; a signup page with the promise and a waitlist; a fake door (a button for a feature that doesn't exist yet, with an honest "coming soon"); a pre-order only with a clear refund |
| **Usability:** can they use it? | the prototype (`/discovery-prototype`) |
| **Feasibility:** can it be built? | a spike: a small throwaway test on real data, with a count (for example 30 known foods, compare the AI's estimates with the real values) |
| **Viability:** does it work as a business? | a waitlist from the channel you chose; a price page that counts clicks on each plan; the cost per user with the providers' real prices |

A product press release (from the brief's working-backwards step) makes a good signup page: the promise is already written.

### 4. Run it
Write down what you did, the raw data and the date. For a page: the visitors, the signups, where they came from. For a spike: every input and output, so someone else can check it.

### 5. Compare with the pass mark
**Pass**, **fail** or **unclear**. Unclear means more data, not a creative reading of the numbers.

### 6. Decide
Keep, change (the person, the feature, the price) or stop. Then:
- update the risk's status in the brief's table and add a journal line;
- if a big risk fails, go back to the brief and decide again;
- what changes in the product goes into the PRD, with a journal line.

### 7. The next test
Back to step 1 until every risk in the brief has a result.

Then add a section to `docs/01-discovery/risk-tests.md`:

```markdown
# Risk tests
## [Risk] – [type]
**Hypothesis:** We believe … We'll know it's true if … by …
**Test:** what, where, how many people or samples
**Ran:** [dates]
**Raw data:** [table or link]
**Result:** pass / fail / unclear, [the number] against [the pass mark]
**Decision:** keep / change / stop, because …; brief updated on [date]
```

## Validate mode
`/discovery-risk-tests validate <file>`: judge existing risk tests, change nothing.
1. Read the file and the brief's risk table and journal.
2. Check the template and "Done when" item by item, citing the lines.
3. Then ask: does every pass mark match the one in the brief, set before the test? Was the riskiest risk tested first, or the easiest? Is the raw data there, so someone else could check the result? Is any "unclear" read as a pass? Did the brief and the PRD change where a result says they should?
4. Report: findings by severity, each with the line, what's wrong and what to change; then what the tests do well; then what you couldn't evaluate. The user picks what to apply.

## The bad version and why not
- Moving the pass mark after seeing the result → every test "passes".
- Testing what's easy, not what's risky → you feel reassured and learn nothing.
- Building the whole product to test one risk → the most expensive test there is.
- A fake door without saying honestly that the feature is coming → you lose people's trust.
- Taking money for something that doesn't exist yet without saying so clearly → a legal and trust problem.

## What breaks if you skip it
The brief says "go with conditions", but nobody checks the conditions. You learn a risk was real after months of code.

## The principle behind it
Test the riskiest assumption with the cheapest test that answers it (Lean Startup's riskiest assumption test). The pass mark is set before the result.

## How to apply it at work
When a project rests on a big assumption ("customers will use this", "the API can take the load"), propose a small test with a pass mark before the build sprint.

## Done when
- [ ] every risk in the brief has a test section, riskiest first
- [ ] each one has the hypothesis, the pass mark from the brief, the raw data and the result
- [ ] each one has a decision, and the brief's table and journal are updated
- [ ] what changed in the product is in the PRD, with a journal line

## Next
Runs until every risk has a result. If a big one fails: back to Discovery · 03 Product brief.
