---
name: setup-workspace
description: Personalize a fresh Hive Workspace Starter, interview the owner about work and boundaries, optionally inspect specifically approved personal documents, create a first project, and connect the copy to its own GitHub repository. Use for first-run setup or a deliberate reconfiguration of the starter.
---

# Setup Workspace

Personalize the supplied system without redesigning it.

1. Read `.claude/reference/workspace-system.md` and
   `.claude/reference/setup-interview.md` completely.
2. Confirm the repository root. Inspect only the top-level tree, required lifecycle
   folders, current instruction files, `git status`, and `git remote -v`.
3. Report missing required paths or collisions. Do not silently create a hybrid structure,
   overwrite user content, or rename an existing lifecycle.
4. Ask the six setup questions from the interview reference together. Include the explicit
   outside-repository document question; default to repository-only access.
5. If outside access is requested, run the consent protocol exactly. A general "yes" is
   not enough. Discovery remains read-only and does not authorize copying.
6. Summarize the proposed personalization and ask for confirmation before writing.

After confirmation, edit only the confirmed fields in `README.md`, `00-context/*.md`, root
`03-status/*.md`, and a new `projects/<slug>/` copied from `projects/_template/`. Preserve
the five root folders, five project folders, and unnumbered `projects/`. Record unknowns as
questions and never store credentials. Do not create speculative apps or packages.

## GitHub connection

Treat GitHub as a separate external-write gate. Preserve an origin created with **Use this
template**. Never push a direct clone back to the starter origin. With no origin, verify
`gh auth status`, ask for owner/name/visibility, show the exact operation, and get
confirmation before `gh repo create --source . --push`. Never replace an origin, change
visibility, publish content, or force-push silently.

## Validation

- Verify root and project lifecycle folders.
- Parse `.claude/settings.json` and `.vscode/tasks.json`.
- Keep placeholders only under `projects/_template/`.
- Confirm no secrets or personal-document copies were introduced.
- Confirm only approved files changed with `git status --short`.
- Report created, personalized, preserved, and deferred items separately.

Finish by suggesting `session-open`, `new-project`, and `setup-agent-team`.
