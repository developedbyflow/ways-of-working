---
name: risk-tests
description: "A tool for every phase: test a risky assumption before building on it. In Discovery, the risks from the product brief; in Delivery, a technical unknown (a spike, a load test); after launch, a channel or a price (an experiment). Pick the riskiest, write the hypothesis with the pass mark set in the brief, choose the cheapest test that answers it (signup page, fake door, spike on real data, waitlist, price page, cost check), run it, compare with the pass mark, decide, and update the brief. Use whenever the next step depends on an unchecked assumption. Also judges an existing test: /risk-tests validate <file>."
argument-hint: "[the risk to test] or validate <file>"
---

# Risk tests (any phase)

## When to use it
When you're about to build or decide something that rests on an assumption you haven't checked, and being wrong would cost a lot. You hear it as "I think people will…", "the AI can probably…", "it should work…". Ask: if it's false, how much do I lose, and how much does checking cost? Big loss, cheap check → test. Small loss (a two-way door) → just do it and watch. Big loss, expensive check → a smaller test, or cut the risk.

It happens in every phase:
- **Discovery:** the risks in the brief's table (value, usability, feasibility, viability), each when its "When" says;
- **Delivery:** a technical unknown before you commit to it ("can the database take 10,000 users?", "does this library do X?");
- **after launch:** a channel, a price, a change to a screen (an experiment).

## The problem it solves
The brief writes the tests; this step runs them honestly and decides from them. Without it, the tests stay on paper and you build on assumptions.

**What it is:** a small experiment that checks one risky assumption before you spend months building on it. The brief lists the risks, each with a test and a pass mark; this step runs them one by one.

**An example, the AI plate scan:**
- **The assumption:** "the AI recognizes what's on the plate and roughly how much". The scan feature rests on it.
- **The experiment, 1–2 days of work spread over a week:** before eating, weigh each food on the plate and take a photo, until you have 20 plates. Work out the real calories from the weights. Send the 20 photos to the AI provider you're considering and note its estimates.
- **The pass mark, fixed before you start:** 15 of 20 plates within ±20% of the real calories.
- **The decision:** pass → pick that provider and build the scan. Fail → try another provider, change the feature (the AI names the foods, you enter the grams), or postpone it.

**What it gives you:** you learn in days what you'd otherwise learn after months of code, and every decision rests on numbers, not hope.

## How to run it
- **The bar:** do what a senior engineer or the C-level who owns this area (CEO, CPO, CTO, CFO, CMO, COO) at a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it, so the user learns it. Senior also means knowing what to leave out: say what you skip and why.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Every `docs/…` path below means that folder.
- **Read first:** where the risk comes from (the brief's risk table and journal in Discovery, the architecture's open questions in Delivery) and `docs/01-discovery/risk-tests.md` if it exists. Product risks from the brief are recorded there; later phases record their tests in their own folder (`docs/02-delivery/risk-tests.md`…).
- **One test at a time.** The user runs it; you help design it and read the result.
- **The pass mark never moves after the result.** If it was wrong, say so in the journal and set a new one for the next test.
- **Nothing outside this machine without the user:** no page published, no email sent, no money taken.

## Steps

### 1. Pick the test
**Run a test when the next step depends on it.** The brief's risk table has a "When" column for each test; it says which tests are due now.

The riskiest open one: it would hurt most if wrong, and you are least sure about it. Usually value or viability before feasibility, because those are the ones developers avoid. But a test whose result blocks the architecture (for example which AI provider) runs before the architecture, whatever its type.

**When each test runs:**
- **before the architecture:** tests whose result picks a technology or a provider;
- **as early as possible, in parallel:** value tests (interviews), because a fail changes direction;
- **during the build:** tests that need part of the real app (testers on a slice);
- **before launch:** tests that need the whole app (a beta) or an audience (a waitlist).

### 2. The hypothesis
> We believe [what]. We'll know it's true if [pass mark] by [date].

The pass mark is the one in the brief. Also write what would make the result unclear (too few people, a broken page).

### 3. The cheapest test that answers it

| Risk | Tests, cheapest first |
|---|---|
| **Value:** will they want it? | the interviews from 01; a signup page with the promise and a waitlist; a fake door (a button for a feature that doesn't exist yet, with an honest "coming soon"); a pre-order only with a clear refund |
| **Usability:** can they use it? | the prototype (`/prototype`) |
| **Feasibility:** can it be built? | a spike: a small throwaway test on real data, with a count (for example 30 known foods, compare the AI's estimates with the real values) |
| **Viability:** does it work as a business? | a waitlist from the channel you chose; a price page that counts clicks on each plan; the cost per user with the providers' real prices |
| **Technical** (Delivery): will this technology hold? | a spike: the smallest throwaway code that answers the question; a load test with the expected numbers |
| **Growth** (after launch): does this change move a number? | an A/B test with a sample size worked out in advance; a channel test with a budget and a stop date |

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
`/risk-tests validate <file>`: judge existing risk tests, change nothing.
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
Back to the step that was waiting for the result. In Discovery, if a big risk fails: back to 03 Product brief.
