# Git and GitHub Setup

Use the smallest path that matches the participant's goal.

## Path 1: GitHub template (recommended)

Choose **Use this template** on `floraldo/hive-workspace-starter`, create a repository,
then clone that new repository. Its `origin` already belongs to the participant. Preserve
it; do not add the starter as a submodule.

## Path 2: Direct clone for local work

```bash
git clone https://github.com/floraldo/hive-workspace-starter.git my-ai-workspace
cd my-ai-workspace
```

The files are fully editable locally. `origin` still names the public starter, so a normal
participant should not try to push there. Local-only use requires no further GitHub setup.

## Claim a direct clone as a new repository

Do this only when the user explicitly asks to publish their copy.

1. Confirm `git status` and the current origin.
2. Ask for GitHub owner, repository name, and public/private visibility.
3. Preserve provenance by renaming the starter remote:

   ```bash
   git remote rename origin starter
   ```

4. If GitHub CLI is installed and authenticated, show and confirm this operation:

   ```bash
   gh repo create OWNER/NAME --private --source . --remote origin --push
   ```

   Replace `--private` with `--public` only when the user chooses public.

5. Without GitHub CLI, ask the user to create an empty repository in the browser. Then
   show and confirm:

   ```bash
   git remote add origin NEW_REPOSITORY_URL
   git push -u origin main
   ```

Never delete or replace a remote silently, force-push, change repository visibility, or
publish personal content as part of workspace personalization. GitHub authentication is a
separate user-controlled step.
