# Start Here: Claude Code in Cursor

This is the workshop path. It takes about ten minutes and keeps each decision visible.

## Before step 1

You need a current Cursor installation, Git or GitHub Desktop, and an eligible paid Claude Code
account. The standard free Claude.ai plan does not include Claude Code. On Windows, install Git
for Windows if you do not already have it.

## 1. Open and trust your own copy

1. Create a repository with [Use this template](https://github.com/floraldo/hive-workspace-starter/generate),
   or clone the public starter.
2. In Cursor, choose **File → Open Folder** and open that repository folder.
3. Trust the workspace only after confirming that it is the copy you created or cloned.

To clone directly instead of using the template:

```bash
git clone https://github.com/floraldo/hive-workspace-starter.git my-ai-workspace
cd my-ai-workspace
```

## 2. Install the Claude Code extension

Cursor should recommend **Claude Code** when this folder opens. Choose **Install**, then sign
in when Claude opens. If there is no recommendation prompt, open **Extensions** with
`Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS), search for **Claude Code**, and
install the extension published by Anthropic.

To open the extension after installation, click the Spark icon in the Activity Bar or status
bar, or open the Command Palette and choose **Claude Code: Open in New Tab**. Sign in in that
panel if you want the visual Cursor experience.

The extension is the easy visual way to talk to Claude in Cursor. The terminal agents in this
starter need the separate CLI installation in the next step.

## 3. Install the terminal CLI

Choose **Terminal → Run Task → 1. Install — Claude Code**. The bundled installer:

- shows the official Anthropic URL;
- downloads the installer to a temporary file;
- asks before it runs anything; and
- installs only for your user account, never into this repository.

When it finishes, close that terminal and open a new one. Run:

```text
claude --version
```

If the version check fails or something looks wrong, run `claude doctor` before troubleshooting.

Do not start a separate `claude` conversation here. The Flow task in the next step starts the
real workspace session and opens the normal browser sign-in when needed. Do not paste an API
key or password into this repository.

## 4. Start your first workspace agent

Choose **Terminal → Run Task → 2. Start 🌊 Flow (Claude)**. Flow opens in a dedicated Cursor
terminal, reads this workspace's instructions and status, and waits for a bounded request.

For a new copy, type this exact command in Flow:

```text
/setup-workspace
```

The default Flow task can accept file edits, but it starts by waiting for your task. Review its
proposals before approving anything.

## 5. Optional: run a small team

Only after Flow is working, choose **Terminal → Run Task → Optional — 🤖 Start 3-Agent Demo**.
This opens three conversations at once:

- 🌊 Flow is the only default writer.
- 🔭 Scout researches and orients.
- 🛠 Forge reviews and suggests refinements.

They share the same folder and Git state. Give each a separate, bounded responsibility. Use
separate Git worktrees if more than one agent needs to edit files.

## If something does not work

- If `claude` is not found after installation, open a new terminal first; then see the
  [official installation troubleshooting](https://code.claude.com/docs/en/troubleshoot-install).
  On Windows, fully restart Cursor first so its integrated terminal receives the updated PATH.
- If Cursor does not show Claude Code, run **Developer: Reload Window**, then check the
  Extensions view.
- If you prefer Codex, choose **Terminal → Run Task → Optional — Install Codex or Both** and
  then invoke `$setup-agent-team` to tailor the tasks.

For the full folder system and safety boundaries, return to [README.md](README.md).
