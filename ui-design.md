# UI design

- **Use it when:** a new screen or flow, or a big change to one.
- **What you get:** every state of every screen designed before users find the missing ones.
- **Run it:** `/wow-ui-design the checkout flow`
- **Not when:** a component or tokens that many screens reuse → `/wow-design-system`.
- **Reads:** the problem and the acceptance criteria, the design system, the analytics funnel (where users drop off).
- **Writes:** the flow diagram, the states of each screen, the list of components (in the ticket or the design doc), and a prototype only when the flow is unclear.

## Steps
1. **The user's steps:** the main path from entry to done; where users come from; what they need at each step. Draw it as a flow diagram.
   - Skip it → screens that make sense one at a time but not in order.
2. **States per screen:** empty, loading, error, partial, success. Add slow network and offline when they matter.
   - Skip it → users discover the missing states.
3. **Real content:** real text and real data lengths (a long name, zero items, 1,000 items), not lorem ipsum.
4. **Components:** take them from the design system. A new one only when nothing fits → `/wow-design-system`.
5. **Forms:**
   - only the fields you need, with the right input types;
   - validate when the user leaves the field;
   - show the error next to the field, saying how to fix it;
   - keep what the user typed.
6. **Accessible from the start:** a keyboard path, the focus order, labels, contrast, target size, headings, and announcements when content changes.
   - Skip it → retrofitting costs more than building it in.
7. **Small screens:** what's in thumb reach, tap target size, what hides or moves.
8. **Feedback and speed:**
   - under 0.1 s feels instant; over 1 s, show progress;
   - skeletons for content;
   - an optimistic update when the action can be undone.
9. **Unclear?** Build 2–3 variants as a `/wow-spike`, or test the flow with five users.
   - STOP: agree on the flow and the states before building.

## Done when
- [ ] the flow diagram exists
- [ ] every screen has its states, and the component list is written
- [ ] the keyboard path works

## Frontend · Backend · Fullstack
- **Frontend:** you own it.
- **Backend:** you read it to know what data each screen needs, and which error means which state.
- **Fullstack:** each error state on the screen maps to an API error.

## Concepts if you get stuck
- UX for developers, states, forms, speed
- Accessibility
- HTML and CSS
- Loading and error states for server data
- Design system

## Next level
- Test big flows with five users before building them.
- `staff` One kit of UX states for the whole product.

## Next
`/wow-api-design`, `/wow-design-system`, `/wow-feature`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
