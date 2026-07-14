#!/usr/bin/env python3
"""Validate the stable workspace contract using only the Python standard library."""

from __future__ import annotations

import json
import os
import re
import stat
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LIFECYCLE = ("00-context", "01-input", "02-output", "03-status", "04-knowledge")
SKILLS = (
    "capture",
    "new-project",
    "session-close",
    "session-open",
    "setup-agent-team",
    "setup-workspace",
)
FORBIDDEN_FLAGS = (
    "dangerously-skip-permissions",
    "--yolo",
    "danger-full-access",
    "--ask-for-approval never",
)
TEXT_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".toml"}


class Checks:
    def __init__(self) -> None:
        self.failures: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.failures.append(message)

    def require_path(self, relative: str) -> Path:
        path = ROOT / relative
        self.require(path.exists(), f"missing required path: {relative}")
        return path


def load_json(checks: Checks, relative: str) -> dict:
    path = checks.require_path(relative)
    if not path.is_file():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        checks.failures.append(f"invalid JSON in {relative}: {exc}")
        return {}
    checks.require(isinstance(value, dict), f"JSON root must be an object: {relative}")
    return value if isinstance(value, dict) else {}


def parse_frontmatter(checks: Checks, path: Path) -> dict[str, str]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        checks.failures.append(f"cannot read {path.relative_to(ROOT)}: {exc}")
        return {}
    checks.require(bool(lines) and lines[0].strip() == "---", f"missing frontmatter: {path.relative_to(ROOT)}")
    try:
        end = next(index for index, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        checks.failures.append(f"unclosed frontmatter: {path.relative_to(ROOT)}")
        return {}
    result: dict[str, str] = {}
    for line in lines[1:end]:
        if line and not line[0].isspace() and ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def validate_structure(checks: Checks) -> None:
    for folder in LIFECYCLE + ("projects", "apps", "packages", "scripts", "var"):
        checks.require_path(folder)

    projects = checks.require_path("projects")
    if projects.is_dir():
        for project in sorted(path for path in projects.iterdir() if path.is_dir() and not path.name.startswith(".")):
            for folder in LIFECYCLE:
                checks.require((project / folder).is_dir(), f"project {project.name} is missing {folder}/")

    for relative in (
        "00-context/workspace.md",
        "00-context/boundaries.md",
        "03-status/workspace-status.md",
        "03-status/tasks.md",
        "03-status/decisions.md",
        "04-knowledge/index.md",
        "projects/_template/00-context/brief.md",
        "projects/_template/03-status/status.md",
    ):
        checks.require_path(relative)


def validate_settings(checks: Checks) -> None:
    settings = load_json(checks, ".claude/settings.json")
    checks.require(settings.get("$schema") == "https://json.schemastore.org/claude-code-settings.json", "Claude settings schema is missing or unexpected")
    checks.require(settings.get("disableSkillShellExecution") is True, "dynamic shell execution in skills must remain disabled")
    denies = settings.get("permissions", {}).get("deny", [])
    for rule in ("Read(./.env)", "Read(./.env.*)", "Read(./secrets/**)", "Read(./credentials/**)"):
        checks.require(rule in denies, f"missing Claude deny rule: {rule}")


def validate_skills(checks: Checks) -> None:
    for name in SKILLS:
        claude_path = checks.require_path(f".claude/skills/{name}/SKILL.md")
        codex_path = checks.require_path(f".agents/skills/{name}/SKILL.md")
        checks.require_path(f".agents/skills/{name}/agents/openai.yaml")
        if not claude_path.is_file() or not codex_path.is_file():
            continue
        claude = parse_frontmatter(checks, claude_path)
        codex = parse_frontmatter(checks, codex_path)
        checks.require(claude.get("name") == name, f"Claude skill name mismatch: {name}")
        checks.require(codex.get("name") == name, f"Codex skill name mismatch: {name}")
        checks.require(bool(claude.get("description")), f"Claude skill description missing: {name}")
        checks.require(codex.get("description") == claude.get("description"), f"skill descriptions drifted: {name}")
        checks.require(claude.get("disable-model-invocation") == "true", f"Claude action skill must be user-invoked: {name}")
        wrapper = codex_path.read_text(encoding="utf-8")
        canonical = f".claude/skills/{name}/SKILL.md"
        checks.require(canonical in wrapper, f"Codex skill wrapper does not route to {canonical}")


def windows_task_values(args: list[str]) -> dict[str, str]:
    values: dict[str, str] = {}
    index = 0
    while index + 1 < len(args):
        if args[index] in {"-Tool", "-Name", "-Emoji", "-Role", "-Mode"}:
            values[args[index]] = args[index + 1]
            index += 2
        else:
            index += 1
    return values


def validate_tasks(checks: Checks) -> None:
    data = load_json(checks, ".vscode/tasks.json")
    tasks = data.get("tasks", [])
    checks.require(isinstance(tasks, list), "tasks.json tasks must be a list")
    if not isinstance(tasks, list):
        return
    labels = [task.get("label") for task in tasks if isinstance(task, dict)]
    checks.require(len(labels) == len(set(labels)), "task labels must be unique")
    label_set = set(labels)

    bootstrap_tasks = [
        task
        for task in tasks
        if isinstance(task, dict)
        and task.get("args") == ["${workspaceFolder}/scripts/bootstrap-agent.sh"]
    ]
    checks.require(len(bootstrap_tasks) == 1, "tasks.json must preserve one bootstrap task")
    if bootstrap_tasks:
        windows_args = bootstrap_tasks[0].get("windows", {}).get("args", [])
        checks.require(
            "${workspaceFolder}\\scripts\\bootstrap-agent.ps1" in windows_args,
            "bootstrap task is missing its Windows script",
        )

    compounds = [task for task in tasks if isinstance(task, dict) and "dependsOn" in task]
    checks.require(len(compounds) == 1, "tasks.json must contain exactly one compound agent-team task")
    if compounds:
        for dependency in compounds[0].get("dependsOn", []):
            checks.require(dependency in label_set, f"compound task references missing task: {dependency}")

    agent_tasks = []
    for task in tasks:
        if not isinstance(task, dict):
            continue
        args = task.get("args", [])
        if isinstance(args, list) and args and str(args[0]).endswith("scripts/launch-agent.sh"):
            agent_tasks.append(task)
    checks.require(1 <= len(agent_tasks) <= 4, "configure between one and four agent tasks")

    for task in agent_tasks:
        args = task["args"]
        checks.require(len(args) == 6, f"Unix launcher argument count is wrong: {task.get('label')}")
        if len(args) != 6:
            continue
        _, tool, name, emoji, role, mode = args
        checks.require(tool in {"claude", "codex"}, f"unsupported tool in task: {task.get('label')}")
        checks.require(mode in {"standard", "edit", "auto"}, f"unsupported mode in task: {task.get('label')}")
        presentation = task.get("presentation", {})
        checks.require(presentation.get("group") == "ai-agent-team", f"agent task is outside split-terminal group: {task.get('label')}")
        windows = task.get("windows", {})
        win_values = windows_task_values(windows.get("args", []))
        expected = {"-Tool": tool, "-Name": name, "-Emoji": emoji, "-Role": role, "-Mode": mode}
        checks.require(win_values == expected, f"Windows and Unix launcher values differ: {task.get('label')}")

    checked_text = (ROOT / ".vscode/tasks.json").read_text(encoding="utf-8")
    checked_text += (ROOT / "scripts/launch-agent.sh").read_text(encoding="utf-8")
    checked_text += (ROOT / "scripts/launch-agent.ps1").read_text(encoding="utf-8")
    lowered = checked_text.lower()
    for flag in FORBIDDEN_FLAGS:
        checks.require(flag not in lowered, f"forbidden launcher flag found: {flag}")


def validate_bootstrap(checks: Checks) -> None:
    ps = checks.require_path("scripts/bootstrap-agent.ps1")
    sh = checks.require_path("scripts/bootstrap-agent.sh")
    expected = {
        "https://claude.ai/install.ps1": ps,
        "https://chatgpt.com/codex/install.ps1": ps,
        "https://claude.ai/install.sh": sh,
        "https://chatgpt.com/codex/install.sh": sh,
    }
    for url, path in expected.items():
        if path.is_file():
            checks.require(url in path.read_text(encoding="utf-8"), f"official installer URL missing: {url}")
    if os.name != "nt" and sh.is_file():
        checks.require(bool(sh.stat().st_mode & stat.S_IXUSR), "bootstrap-agent.sh must be executable")


def validate_placeholders(checks: Checks) -> None:
    placeholder = re.compile(r"\{\{[A-Z_]+\}\}")
    roots = [ROOT / folder for folder in LIFECYCLE]
    projects = ROOT / "projects"
    if projects.is_dir():
        roots.extend(path for path in projects.iterdir() if path.is_dir() and path.name != "_template")
    for base in roots:
        if not base.exists():
            continue
        for path in base.rglob("*"):
            is_text = path.is_file() and path.suffix.lower() in TEXT_SUFFIXES
            has_placeholder = is_text and placeholder.search(
                path.read_text(encoding="utf-8", errors="ignore")
            )
            if has_placeholder:
                checks.failures.append(f"unresolved placeholder outside project template: {path.relative_to(ROOT)}")


def main() -> int:
    checks = Checks()
    validate_structure(checks)
    validate_settings(checks)
    validate_skills(checks)
    validate_tasks(checks)
    validate_bootstrap(checks)
    validate_placeholders(checks)

    if checks.failures:
        print("Starter validation failed:")
        for failure in checks.failures:
            print(f"- {failure}")
        return 1
    print("Starter validation passed: lifecycle, settings, skills, tasks, bootstrap, and placeholders are coherent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
