---
name: new-project
description: Create one bounded project beneath projects by copying the canonical 00-context through 04-knowledge template and filling a short brief and status. Use when starting a new campaign, client-safe initiative, deliverable, or other outcome.
---

# New Project

1. Use the supplied name or ask for it.
2. Ask for outcome, definition of done, owner, deadline, and approval boundary.
3. Create a lowercase hyphenated slug from letters, numbers, and hyphens. Reject path
   separators, `.` and `..`.
4. If `projects/<slug>/` exists, stop; never merge silently.
5. Copy `projects/_template/`, then replace its three project placeholders only in the copy.
6. Fill confirmed brief and status fields; leave unknowns explicit.
7. Verify all five lifecycle folders and report the first next action.

Do not create apps, packages, connectors, or automation merely because a project exists.
