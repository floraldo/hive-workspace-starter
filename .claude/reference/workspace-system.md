# Workspace System

This is the normative folder contract used by setup and session skills.

## Fractal lifecycle

The same five questions exist at two scales:

| Folder | Root meaning | Project meaning |
|---|---|---|
| `00-context/` | workspace purpose, people, voice, tools, boundaries | brief, scope, audience, constraints, done criteria |
| `01-input/` | cross-project sources and inbox | sources selected for this project |
| `02-output/` | cross-project deliverables and exports | drafts and approved project deliverables |
| `03-status/` | workspace state, tasks, decisions | current state, next action, blockers, activity |
| `04-knowledge/` | reviewed learning useful broadly | durable project decisions and learning |

`projects/` is never numbered. It is a container whose children repeat the lifecycle.

## Placement test

Ask in order:

1. Does this concern one bounded project? Use that project's matching folder.
2. Does it apply across projects? Use the matching root folder.
3. Is its destination unknown? Put it temporarily in `01-input/inbox/` with provenance.
4. Is it generated runtime material? Put it under `var/`, not in the lifecycle.

## Promotion ladder

```text
manual conversation or checklist
            ↓ repeats
throwaway script in scripts/
            ↓ reused by 2+ workflows or needs tests/contracts
reusable package in packages/
            ↓ needs a stable human-facing entry point
app in apps/
```

Connectors are access paths to systems. Packages are implementation logic. Google Drive,
Gmail, Calendar, Notion, Slack, and CRMs begin as scoped connectors; they become packages
only when deterministic shared behavior is actually required.

## Required invariants

- Root and every real project have all five lifecycle directories.
- `_template/` retains only `{{PROJECT_NAME}}`, `{{PROJECT_SLUG}}`, and
  `{{PROJECT_DATE}}` placeholders.
- No existing file is silently overwritten during setup.
- Status files have one clear next action.
- Knowledge states provenance and confidence.
- Credentials and sensitive raw documents never enter the scaffold.
