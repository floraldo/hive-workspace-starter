# Agent Team Reference

Last checked against official documentation on 2026-07-14. Re-check the linked pages
before changing installers, CLI flags, or permission modes.

## Bootstrap boundary

The first agent CLI must be installed before an agent can run its setup skill. Prefer the
bundled bootstrap, which displays the official source, downloads the installer to a
temporary file, and asks before executing it:

- Windows: `powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\bootstrap-agent.ps1`
- macOS/Linux/WSL: `bash scripts/bootstrap-agent.sh`
- Cursor: **Terminal → Run Task → 🧰 Setup — Install Agent CLI**

Install CLIs at user level, never inside the repository. Authentication remains a separate
interactive provider flow; never request, copy, or store tokens.

## Official sources and verification

| Tool | Windows installer | macOS/Linux/WSL installer | Verify |
|---|---|---|---|
| Claude Code | `https://claude.ai/install.ps1` | `https://claude.ai/install.sh` | `claude --version`; `claude doctor` |
| Codex | `https://chatgpt.com/codex/install.ps1` | `https://chatgpt.com/codex/install.sh` | `codex --version`; optionally `codex doctor` |

Sources:

- Claude Code installation: <https://code.claude.com/docs/en/installation>
- Codex CLI: <https://developers.openai.com/codex/cli>

Do not make a first install non-interactive. If the bootstrap is unavailable, show the
official platform command and obtain confirmation immediately before running it.

## Team questions

Ask in one compact round:

1. Use Claude Code, Codex, or a mixture?
2. How many terminals, from one to four? Three is the useful default.
3. For each: emoji, short name, role, and tool.
4. Permission posture: review, guided edit, or official auto where supported?
5. Should `.vscode/tasks.json` be changed now? Show the proposed roster first.

Suggested roster:

| Agent | Default role | Default posture |
|---|---|---|
| `🌊 Flow` | primary builder and coordinator | guided edit |
| `🔭 Scout` | research, sources, and orientation | review |
| `🛠 Forge` | implementation and refinement | guided edit |

Keep names to letters, numbers, spaces, `_`, or `-`; keep roles to one short sentence. Do
not embed shell commands, paths, secrets, or provider flags in names or roles.

## Permission mapping

| Requested posture | Claude Code | Codex |
|---|---|---|
| review | `--permission-mode default` | `--sandbox read-only --ask-for-approval on-request` |
| guided edit | `--permission-mode acceptEdits` | workspace-write/on-request Auto preset |
| auto | `--permission-mode auto` only when supported | `--sandbox workspace-write --ask-for-approval on-request` |

Claude Code auto mode is a research preview and is not available to every plan, model, or
provider. If eligibility is unknown, use guided edit. Never substitute
`--dangerously-skip-permissions`. Never use Codex `--yolo`, danger-full-access, or
approval-never for the workshop.

## Cursor task contract

`.vscode/tasks.json` contains:

- one interactive bootstrap task;
- one to four agent tasks;
- exactly one compound agent-team task.

Agent tasks share `presentation.group: "ai-agent-team"`, which creates split terminals in
VS Code-compatible task runners. The compound task starts dependencies in parallel.

Customization may change only:

- agent task label;
- `-Tool`/tool argument: `claude` or `codex`;
- name, emoji, role, and mode arguments;
- compound dependency labels.

Preserve shell commands, script paths, task type, presentation group, instance limit, and
bootstrap task. Keep Unix and Windows agent values identical. After edits, run
`python scripts/validate-starter.py` when Python is available (otherwise perform the same
checks directly), then smoke-test one agent before starting the team.

## Concurrency boundary

Split terminals share the repository and Git index. Default to one writer: Flow edits,
Scout researches, Forge reviews or waits. For simultaneous edits, create a separate Git
worktree and branch per agent.

Official references:

- Claude permission modes: <https://code.claude.com/docs/en/permission-modes>
- Codex sandbox and approvals: <https://developers.openai.com/codex/security>
- VS Code tasks and split terminal groups: <https://code.visualstudio.com/docs/debugtest/tasks>
