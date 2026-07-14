---
name: setup-agent-team
description: Verify or install Claude Code and Codex with approval, choose a one-to-four-agent roster, and configure safe split-terminal Cursor tasks with names, emoji, roles, tools, and permission modes. Use when setting up or changing the workspace agent team.
disable-model-invocation: true
---

# Setup Agent Team

Configure the existing bounded launcher; do not invent a new orchestration system.

1. Read `.claude/reference/agent-team.md` completely.
2. Inspect `.vscode/tasks.json`, `scripts/bootstrap-agent.ps1|sh`, and
   `scripts/launch-agent.ps1|sh`. Check `claude --version` and `codex --version` read-only;
   a missing command is an expected setup state.
3. Ask the reference's five team questions in one compact round. Offer `🌊 Flow`,
   `🔭 Scout`, and `🛠 Forge` as defaults.
4. Show the roster and permission mapping before changing files.

For a missing requested CLI, prefer the matching bundled bootstrap script. State which
official URL it downloads and ask before running it; the bootstrap asks again before the
installer executes. Install user-level, never inside the repository. Do not make
authentication non-interactive; ask the user to complete sign-in in the provider's own
flow. Never handle tokens.

Edit only the bounded fields permitted by the reference in `.vscode/tasks.json`. Keep one
to four agent tasks plus the compound task. A task's Unix and Windows arguments must match.
Use `standard`, `edit`, or `auto`; choose Claude `auto` only after the user confirms their
account/client supports it. Otherwise use `edit`. Never add bypass, yolo, danger-full-access,
or approval-never flags.

Run `python scripts/validate-starter.py` when Python is available; otherwise parse the JSON
and perform the reference's task checks directly. Then check launcher syntax where the
relevant shell is available. Offer to start one task as a smoke test; launching the whole
team is a separate confirmation because it starts multiple interactive processes.

Remind the user that the panes share one working tree. Default roles should leave one
writer and use other agents for research or review unless separate Git worktrees exist.
