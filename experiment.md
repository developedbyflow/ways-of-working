# Experiment

- **Use it when:** you need proof that a change moved a number (conversion, retention, completion). That means an A/B test, or a fake door before you build.
- **Not when:** you just ship and watch for errors → step 7 of `/wow-feature`.
- **Reads:** the tracking plan, the current numbers, the traffic.
- **Writes:** `docs/experiments/YYYY-MM-name.md`, the events in `docs/tracking-plan.md`, the result.

## Steps
1. **Hypothesis:** "If we change X for users Y, metric Z goes up, because W." One primary metric.
   - Skip it → you'll find a metric that went up afterwards, and call it a win.
2. **Guardrails:** what must not get worse (errors, speed, refunds, unsubscribes).
3. **Sample size and duration:**
   - computed from the current rate, the smallest effect you care about, alpha 0.05 and power 0.8;
   - run it for at least one full week, so every weekday is included;
   - too little traffic → don't run an A/B test. Ship behind a flag and watch, or test with five users.
   - Skip it → noise gets declared a win.
4. **Set it up:**
   - each user always sees the same variant;
   - both variants send the same events;
   - check the events in staging first.
   - STOP: the events are verified before it starts.
5. **Don't peek:** decide only at the planned end. Checking every day and stopping at the first good result makes a false win far more likely.
6. **Decide by the rule from step 1:** ship, iterate or drop. Write the result even when it's "no difference".
   - STOP: you decide.
7. **Clean up:** remove the losing variant and the flag.

**Fake door:** a button for a feature that doesn't exist yet, where you count the clicks. Tell users honestly that it's coming, and use it rarely.

## Done when
- [ ] the experiment doc has the hypothesis, metrics, size, dates, result and decision
- [ ] the flag is removed

## Concepts if you get stuck
- A/B tests, sample size, peeking, fake doors → F23 The product-minded engineer
- Flags → F16 The frontend in production

## Next level
- `staff` One place where every experiment and its result lives.

## Next
`/wow-feature`, `/wow-comms` to share the result. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
