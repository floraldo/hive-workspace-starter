# Scripts

Use this folder for throwaway experiments, one-off migrations, and small helpers while a
workflow is still being learned.

At the top of a script, state its purpose, inputs, outputs, side effects, safe run command,
and likely deletion date. If the same logic serves multiple workflows or needs tests and a
stable contract, promote it to `packages/`.

The `bootstrap-agent`, `launch-agent`, and `validate-starter` scripts are deliberate
workspace infrastructure used by setup, Cursor tasks, and CI; they are not business logic.

- `bootstrap-agent.*` downloads an official Claude Code or Codex installer to a temporary
  file and runs it only after confirmation.
- `launch-agent.*` starts one bounded interactive terminal agent.
- `validate-starter.py` checks the lifecycle, settings, skills, and task contract without
  third-party Python packages.

For the workshop's simplest path, use **Terminal → Run Task → 1. Install — Claude Code**.
The optional installer task retains the Claude/Codex/Both choice for people who need it.
