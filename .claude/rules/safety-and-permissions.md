# Safety and Permissions

- Ask before deleting, overwriting, moving many files, publishing, sending, purchasing,
  authenticating, or changing an external system.
- Outside-repository discovery requires current consent naming exact paths and whether
  metadata or content may be read. Default to repository-only access.
- Never seek or store passwords, tokens, private keys, browser sessions, or credential
  files. Stop if they appear unexpectedly.
- Read permission does not authorize copying or editing.
- Do not weaken `.claude/settings.json` safety denies without an explicit request.
- Never launch Claude with `--dangerously-skip-permissions` or Codex with `--yolo` from
  workspace tasks.
