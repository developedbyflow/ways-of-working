# AI feature

- **Use it when:** a feature in your product calls an LLM: summaries, extracting data, chat, classifying, generating.
- **Not when:** you use AI to write code → `/wow-brief`.
- **Reads:** the problem, real example inputs, the provider's docs, pricing and data terms.
- **Writes:**
  - the prompt, versioned in the code;
  - the eval set: examples with their expected results;
  - the cost alerts;
  - the events, in `docs/tracking-plan.md`.

## Steps
1. **Is an LLM the right tool?** Could rules, search or a simple model do it? What does a wrong answer cost the user?
   - Skip it → you pay per request for what an `if` could do, or you ship confident wrong answers where they hurt.
2. **Examples first:** 20–50 real inputs with the expected output, including the hard ones and the bad ones. This is the eval set.
   - STOP: agree on what "good" means.
   - Skip it → you tune the prompt by feel.
3. **Context and prompt:**
   - send only the data the task needs;
   - ask for structured output (a JSON schema) and validate it in your code;
   - keep the prompt in the repo.
4. **Guardrails:**
   - treat the output as untrusted input: validate it, never run it, never render it as raw HTML;
   - users and documents can contain instructions aimed at the model, so never give the model a power it shouldn't use on its own;
   - never put a secret in its context.
5. **Privacy:** personal data only when the feature needs it. Check the provider's retention and training terms, and tell users.
6. **Cost and speed:**
   - monthly cost = tokens per request × requests per day × 30 × the price per token;
   - a limit per user and a total limit;
   - cache repeated answers, stream long ones, and set a timeout.
7. **When it fails:** what the user sees when the provider is down or slow, or when the output fails validation.
8. **Run the eval set on every prompt or model change**, and compare with the last run.
   - STOP: ship only if the results aren't worse.
   - Skip it → a "small" prompt change breaks one case in ten.
9. **Measure in production:** the outcome event or a thumbs up/down, the error rate, the cost per day.

## Done when
- [ ] the eval set runs with one command
- [ ] the output is validated
- [ ] the limits, alerts and fallback work
- [ ] privacy is checked

## Frontend · Backend · Fullstack
- **Frontend:** a streaming UI, loading and partial states, a label saying the content is AI-generated, a way to correct it.
- **Backend:** the provider call (→ `/wow-integration`), validation, limits.
- **Fullstack:** the server validates. Always.

## Concepts if you get stuck
- AI in the backend → [Backend 17 AI in the backend](https://claude.ai/artifact/VEv76dkdhgR6W2QAQspgUH)
- AI in the frontend → [F20 AI in the frontend](https://claude.ai/artifact/QcvMqVPoPV388owNPomyxC)
- AI systems at scale → [S16 AI Systems](https://claude.ai/artifact/P4zMfpCwLXkhJkQwZay5H9)

## Next level
- Eval results tracked over time.
- `staff` A cheaper model for the easy cases, the stronger one for the hard cases.

## Next
`/wow-integration`, `/wow-experiment`, `/wow-feature`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
