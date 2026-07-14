---
name: setup-agent-team
description: Verify or install Claude Code and Codex with approval, choose a one-to-four-agent roster, and configure safe split-terminal Cursor tasks with names, emoji, roles, tools, and permission modes. Use when setting up or changing the workspace agent team.
---

# Setup Agent Team

Configure the existing bounded launcher; do not invent a new orchestration system.

1. Read `.claude/reference/agent-team.md` completely.
2. Inspect `.vscode/tasks.json` and `scripts/launch-agent.ps1|sh`. Check `claude --version`
   and `codex --version` read-only; a missing command is an expected setup state.
3. Ask the reference's five team questions in one compact round. Offer `🌊 Flow`,
   `🔭 Scout`, and `🛠 Forge` as defaults.
4. Show the roster and permission mapping before changing files.

For a missing CLI, show the official platform command and ask immediately before running
it. Install user-level, never in the repository. Keep authentication interactive and never
handle tokens.

Edit only the permitted fields in `.vscode/tasks.json`. Keep one to four agent tasks plus
the compound task; Unix and Windows arguments must match. Choose Claude auto only after
the user confirms support. Never add bypass, yolo, danger-full-access, or approval-never
flags.

Parse the JSON, resolve every compound dependency, check launcher syntax where available,
and reject forbidden flags. Offer one task as a smoke test; starting the full team requires
separate confirmation. Remind the user the panes share one working tree and default to one
writer unless separate Git worktrees exist.
