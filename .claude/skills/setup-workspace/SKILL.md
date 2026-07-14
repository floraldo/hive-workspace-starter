---
name: setup-workspace
description: Personalize a fresh Hive Workspace Starter, interview the owner about work and boundaries, optionally inspect specifically approved personal documents, create a first project, and connect the copy to its own GitHub repository. Use for first-run setup or a deliberate reconfiguration of the starter.
disable-model-invocation: true
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

After confirmation, edit only the confirmed fields in:

- `00-context/*.md`;
- `03-status/workspace-status.md`, `tasks.md`, and `decisions.md`;
- a new `projects/<slug>/` copied from `projects/_template/`.

Preserve the five root folders, the five project folders, and unnumbered `projects/`.
Record unknowns as open questions. Record tool names and source-of-truth roles but never
credentials. Do not create an app or package unless observed reuse justifies it and the user
separately asks.

## GitHub connection

Treat GitHub as a separate external-write gate.

Read `.claude/reference/github-setup.md` completely only when the user asks to connect,
publish, or clarify a direct clone.

1. If the user created the repository with **Use this template**, preserve its origin and
   report that setup is complete.
2. If this is a direct clone of the starter, do not push to its origin. Offer local-only
   use or the reference's explicit `starter`-remote plus new-`origin` procedure.
3. For a new remote, support both the GitHub CLI and browser-created empty-repository paths.
   Ask for owner, name, and visibility; show the exact operation and get confirmation.
4. Never replace an origin, change visibility, publish content, or force-push silently.

## Validation

- Verify all root and project lifecycle folders exist.
- Parse `.claude/settings.json` and `.vscode/tasks.json` as JSON.
- Confirm placeholders remain only under `projects/_template/`.
- Confirm no secret-like values or copied personal documents were introduced.
- Confirm only approved files changed with `git status --short`.
- Run `python scripts/validate-starter.py` when Python is available; otherwise perform the
  same manifest checks directly and report that the deterministic script was unavailable.
- Report created, personalized, preserved, and deferred items separately.

Finish by suggesting `session-open`, `new-project`, and `setup-agent-team`.
