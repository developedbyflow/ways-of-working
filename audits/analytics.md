# Analytics audit

- **Bar:** every number you make decisions with comes from events you trust.
- **Tools:** the tracking plan, the analytics tool's live view or debugger, the Network tab.

## Checklist
- [ ] **A tracking plan exists** (`docs/tracking-plan.md`): for each event, its name (`object_action`), properties, owner, and the metric that uses it.
- [ ] **Events fire once**, with the right properties. Check it in staging.
- [ ] **Critical events** (order completed, sign-up) are sent from the server, not only from the browser. Ad blockers and closed tabs lose browser events.
- [ ] **Consent:** no tracking before consent where it's required, and no personal data in event properties.
- [ ] **Dashboards match the definitions,** for example what counts as an active user.
- [ ] **Events nobody uses** are removed.

## Concepts
- Tracking plans, server-side events, metrics → F23 The product-minded engineer
- The frontend in production → F16 The frontend in production

## Changelog
- 2026-10-05: v1
