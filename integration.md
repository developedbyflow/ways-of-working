# Integration with an external service

- **Use it when:** your app calls a service you don't own (payments, sign-in provider, email, maps, another team's API), or receives its webhooks.
- **Not when:**
  - you design the API others call → `/wow-api-design`;
  - the service is an LLM → `/wow-ai-feature`, which runs this inside.
- **Reads:** the provider's docs, limits, pricing, status page and SDK.
- **Writes:**
  - the client code;
  - the secrets, in the secret store;
  - a runbook entry, "what to do when X is down";
  - `docs/risks.md`.

## Steps
1. **The contract:** the exact calls, errors, rate limits and payload limits. Pin the API version.
   - Skip it → it breaks the day they change a default.
2. **Secrets:**
   - keys in the secret store, never in the code or the frontend bundle;
   - restricted keys with the least access that works;
   - a plan for rotating them.
3. **Call from the server.** A key that must stay secret never goes to the browser.
4. **Timeouts and retries:**
   - a timeout on every call;
   - retries only for network errors, 429 and 503, and only for operations that are safe to repeat;
   - backoff with jitter, and a cap on the total time.
   - Skip it → one slow provider freezes your app.
5. **Idempotency:** a key on every operation that creates something, like a payment, so a retry doesn't create it twice.
6. **Webhooks:**
   - verify the signature;
   - answer 200 fast, then do the work in the background;
   - expect duplicates and events in the wrong order, and store the event id.
7. **When it's down:** what the user sees. Queue it and retry later, offer less, or show a clear message. Stop calling for a while when every call fails (a circuit breaker).
8. **Test mode:** sandbox keys and the provider's test data. Recorded responses or contract tests in CI. Never real money in a test.
9. **Watch it:**
   - log each call (duration, status, no personal data);
   - an alert on the error rate;
   - an alert on usage and billing.
   - STOP: before going live, check the limits, the price, and what happens when it's down.

## Done when
- [ ] timeouts, retries and idempotency are in place
- [ ] webhook signatures are checked
- [ ] the fallback works, the alerts are set, and test mode is used in CI
- [ ] the runbook entry exists

## Concepts if you get stuck
- Calls between systems, retries, webhooks
- Idempotency and correctness across services
- Payments
- Secrets
- Running it in production

## Next level
- Vendor review: what data they receive and where they store it. Under GDPR, the vendor is a processor.
- `staff` A thin wrapper inside your code, so the rest of the app doesn't depend on the vendor.

## Next
`/wow-feature`; `/wow-audit privacy` for the data you share with the vendor. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
