# Contributing

## Branching

- `main` — always working/demo-able. No direct pushes — everything goes through a PR
- Branch off `main` for any change:
  - `feature/short-description` — e.g. `feature/lobby-ui`
  - `fix/short-description` — e.g. `fix/reconnect-loop`
  - `docs/short-description` — e.g. `docs/add-setup-guide`

```bash
git checkout main
git pull
git checkout -b feature/short-description
```

## Commits

Keep messages short and with meaning:

```
feat: add lobby room creation
fix: handle client disconnect
docs: add ADR for websocket library choice
chore: update dependencies
```

## Opening a pull request

1. Push your branch and open a PR into `main`
2. Say **what changed** and if needed **how to test it** — don't leave it blank
3. Link the related issue if there is one (`Closes #12`)
4. Get at least one review/approval from a teammate before merging
5. Delete the branch after merging

## Opening an issue

Use template...

## Recording a decision

When the team settles something non-trivial (a library choice, a data model, a protocol design), add a short file to `docs/decisions/` using `0001-template.md` as a starting point. A few sentences on context, options considered, and the decision is enough.
