# Workspace Decisions

## 2026-07-14 — Use a fractal five-folder lifecycle

- **Decision:** The workspace root and each project use `00-context`, `01-input`,
  `02-output`, `03-status`, and `04-knowledge`. `projects/` stays unnumbered.
- **Why:** The same questions have the same homes at every scale.
- **Revisit when:** A repeated, concrete placement problem cannot be solved by the current
  meanings.

## 2026-07-14 — Earn automation through reuse

- **Decision:** Begin manually; use `scripts/` for experiments, `packages/` for tested
  reusable logic, and `apps/` for stable human-facing entry points.
- **Why:** Empty architecture is easier to understand than speculative modules.
