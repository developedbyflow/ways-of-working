# Comms

- **Use it when:** you write to people who need to know something or decide something. That covers a status update, a risk, a decision request and an incident update.
- **Not when:** you're writing the design itself → `/wow-design-doc`.
- **Reads:** the plan, `docs/risks.md`, the options for the decision, the incident notes, the experiment results in `docs/experiments/`.
- **Writes:** the message, and the decision recorded as an ADR once it's made.

## Rules
- **Bottom line first.** The first sentence says what they need to know or do.
- **Write for the reader.** No internal jargon for non-technical readers. Numbers come with their meaning: "checkout is 20% faster: 2.5 s → 2.0 s".
- **One ask:** explicit, with a date.

## Formats

**Status**, every week:
```markdown
Status: on track | at risk | off track
Done this week:
Next:
Risks: each one, with what we do about it
Ask: what I need, from whom, by when
```

**Risk:**
```markdown
Risk: what may happen, and when
Impact: on users, the date, the cost
Options: A (its cost), B (its cost)
Recommendation and ask
```

**Decision request:**
```markdown
Decision needed: <what>, by <date>
Criteria: what matters, in order
Options: 2–3, each with its cost and consequence
Recommendation: <option>, because <reason>
When the other option is right: <the objection you would accept>
```

**Incident update:**
```markdown
Impact: who is affected, since when
What we know, and what we're doing
Next update: <time>
```

## Steps
1. **Pick the format and fill it in.**
   - Skip it → a long message with the ask buried in paragraph four.
2. **For a decision, talk first:** see the key people one-to-one before the meeting or the message, so nobody is surprised.
3. **When people disagree:**
   - restate their point until they agree you got it right;
   - agree on the criteria first;
   - once it's decided, commit to it, even if you disagreed;
   - when text gets heated, move to a call.
4. **Send it.**
   - STOP: you send it. The skill never does.

## Done when
- [ ] the bottom line comes first
- [ ] there is one ask, with a date
- [ ] you sent it yourself

## Concepts if you get stuck
- Influence and communication as a lead
- Staff-level communication
- Working with product people

## Next level
- `staff` Proposals for executives: one page, with the business number first.

## Next
Back to the skill that called it.

## Changelog
- 2026-10-05: v1
