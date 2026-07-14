---
paths:
  - "apps/**"
  - "packages/**"
  - "scripts/**"
---

# Work Promotion

- `scripts/` is for disposable experiments and one-off helpers. Document inputs, outputs,
  side effects, and safe use.
- Promote logic to `packages/` after reuse by at least two workflows or when it needs
  tests, a stable schema, versioning, or a public contract.
- Put stable human-facing entry points in `apps/`; apps may use packages, not the reverse.
- Do not create a package merely because a connector exists.
- Never place credentials or personal source data in code, fixtures, logs, or examples.
