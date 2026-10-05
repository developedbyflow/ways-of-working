# API design

- **Use it when:** you add or change an API that a client calls: your frontend, a mobile app, another team.
- **Not when:** you call someone else's API → `/wow-integration`.
- **Reads:** what the client needs (the screens from `/wow-ui-design`), `GLOSSARY.md`, the API's existing conventions.
- **Writes:** the OpenAPI document, the requests in the `.http` file, the generated TypeScript types.

## Steps
1. **What the client needs:** for each screen or action, the data that goes in and comes out.
   - Skip it → endpoints shaped like tables, and the client makes five calls for one screen.
2. **Resources and operations:**
   - nouns in the URL, plus the HTTP methods: `GET` is safe, `PUT` and `DELETE` are idempotent, `POST` is neither;
   - the status codes: 201 with `Location`, 204, 400, 404, 409, 422.
3. **The contract first:**
   - request and response bodies as DTOs, not entities, with the required fields marked;
   - dates in ISO 8601 UTC; money in minor units or as a decimal string;
   - errors as Problem Details.
   - STOP: the client side reads the contract before anyone writes code.
4. **Lists:** pagination (a cursor for big or changing lists, an offset for small ones), filters, sorting, and a maximum page size.
5. **Who is allowed:** authentication, plus an authorization check on every operation and on every object. A user reads only their own orders.
   - Skip it → anyone can read anyone's data by changing an id in the URL.
6. **Safety:**
   - an idempotency key on any `POST` that creates an order or a payment, so a retry doesn't do it twice;
   - rate limits and request size limits.
7. **Change without breaking:**
   - adding a field is fine;
   - removing or renaming one needs a new version;
   - deprecate with a date (the `Deprecation` and `Sunset` headers).
   - Skip it → a deploy breaks a client you didn't know about.
8. **Generate the types, and write the `.http` requests**, with what you should see written above each one.

## Done when
- [ ] OpenAPI lists every status code each endpoint returns
- [ ] the `.http` requests exist
- [ ] the types are generated
- [ ] every operation has its authorization rule

## Frontend · Backend · Fullstack
- **Frontend:** you read and agree to the contract, then mock it (MSW) while the backend is being built.
- **Backend:** you write it and you own it.
- **Fullstack:** the contract comes before either side.

## Concepts if you get stuck
- Methods, status codes, DTOs, validation, pagination, versioning, OpenAPI
- Authorization
- How the client consumes it

## Next level
- Contract tests that fail when a breaking change ships.
- `staff` API guidelines for the team.

## Next
`/wow-data-model`; `/wow-feature` (tests from the contract); `/wow-migration` for a breaking change. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
