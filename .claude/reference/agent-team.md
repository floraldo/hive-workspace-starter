# Agent Team Reference

Last checked against official documentation on 2026-07-14. Re-check the linked pages
before changing installers, CLI flags, or permission modes.

## Bootstrap boundary

The first agent CLI must be installed before an agent can run its setup skill. Prefer the
bundled bootstrap, which displays the official source, downloads the installer to a
temporary file, and asks before executing it:

- Windows: `powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\bootstrap-agent.ps1`
- macOS/Linux/WSL: `bash scripts/bootstrap-agent.sh`
- Cursor: **Terminal → Run Task → 1. Install — Claude Code**

Install CLIs at user level, never inside the repository. Authentication remains a separate
interactive provider flow; never request, copy, or store tokens.

## Cursor first-run path

The workspace includes a deliberately small amount of Cursor configuration:

- `.vscode/extensions.json` recommends `anthropic.claude-code`; Cursor may prompt the
  participant to install it, but the repository never silently installs an extension.
- `.vscode/settings.json` sets Claude Code's graphical panel to **plan** mode for its first
  conversation, keeps the bypass-permissions selector disabled, and turns off automatic tasks.
- `.vscode/tasks.json` provides the explicit terminal path below. It does not run installers or
  agents when a folder opens, because that could consume usage, prompt for sign-in, or execute
  in the wrong workspace.

For a Claude Code workshop, use these visible tasks in order:

1. **1. Install — Claude Code** — runs the bundled installer with Claude preselected.
2. Start a fresh terminal, run `claude --version`, and optionally `claude doctor`.
3. **2. Start 🌊 Flow (Claude)** — starts the first interactive terminal agent and opens the
   provider's normal sign-in when needed.
4. **Optional — 🤖 Start 3-Agent Demo** — starts Flow, Scout, and Forge only when the
   participant is ready for three concurrent conversations.

The Claude Code extension is the visual Cursor experience. Its bundled private CLI is not added
to the terminal `PATH`, so the terminal-agent tasks still require the standalone CLI in step 1.
If the extension is not visible after installation, reload the Cursor window and check the
Extensions view.

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
| `🛠 Forge` | review bounded work and suggest refinements | review |

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
- one Claude Code quick-start install task;
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
bootstrap tasks. Keep Unix and Windows agent values identical. Keep all tasks manual (never
`runOn: folderOpen`) and start them in `${workspaceFolder}`. In a shared working tree, configure
at most one `edit` or `auto` agent; make the others review agents. After edits, run
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
