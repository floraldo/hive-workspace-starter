---
name: new-project
description: Create one bounded project beneath projects by copying the canonical 00-context through 04-knowledge template and filling a short brief and status. Use when starting a new campaign, client-safe initiative, deliverable, or other outcome.
argument-hint: "<project name>"
disable-model-invocation: true
---

# New Project

1. Use `$ARGUMENTS` as the proposed name or ask for it when empty.
2. Ask for outcome, definition of done, owner, and any deadline or approval boundary.
3. Create a lowercase hyphenated slug from letters, numbers, and hyphens. Reject path
   separators, `.` and `..`.
4. If `projects/<slug>/` exists, stop and offer to open it; never merge silently.
5. Copy `projects/_template/` exactly, then replace `{{PROJECT_NAME}}`,
   `{{PROJECT_SLUG}}`, and `{{PROJECT_DATE}}` only in the new copy.
6. Fill confirmed brief and status fields; leave unknowns explicit.
7. Verify all five lifecycle folders exist and report the path and first next action.

Do not create apps, packages, connectors, or automation merely because a project exists.
