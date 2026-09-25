"""Generate a simple weekly project update from local sample data.

This starter script intentionally uses only Python's standard library.
Learners do not need to understand Python syntax to complete the course.
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATUS_FILE = ROOT / "input" / "project-status.csv"
NOTES_FILE = ROOT / "input" / "meeting-notes.md"
TEMPLATE_FILE = ROOT / "templates" / "weekly-update-template.md"
OUTPUT_FILE = ROOT / "output" / "weekly-update.md"


def load_projects() -> list[dict[str, str]]:
    with STATUS_FILE.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def load_notes() -> str:
    return NOTES_FILE.read_text(encoding="utf-8").strip()


def build_portfolio_summary(projects: list[dict[str, str]]) -> str:
    total = len(projects)
    on_track = sum(1 for project in projects if project["status"] == "On Track")
    at_risk = sum(1 for project in projects if project["status"] == "At Risk")
    blocked = sum(1 for project in projects if project["status"] == "Blocked")
    return (
        f"- Total projects: **{total}**\n"
        f"- On Track: **{on_track}**\n"
        f"- At Risk: **{at_risk}**\n"
        f"- Blocked: **{blocked}**"
    )


def build_project_status(projects: list[dict[str, str]]) -> str:
    lines = [
        "| Project | Owner | Status | Priority | Milestone | Due Date |",
        "|---|---|---|---|---|---|",
    ]
    for project in projects:
        lines.append(
            f"| {project['project']} | {project['owner']} | {project['status']} | "
            f"{project['priority']} | {project['milestone']} | {project['due_date']} |"
        )
    return "\n".join(lines)


def split_notes(notes: str) -> tuple[str, str]:
    highlights_marker = "## Highlights"
    decisions_marker = "## Decisions"
    followups_marker = "## Follow-ups"

    highlights = notes.split(highlights_marker, 1)[1].split(decisions_marker, 1)[0].strip()
    decisions = notes.split(decisions_marker, 1)[1].split(followups_marker, 1)[0].strip()
    followups = notes.split(followups_marker, 1)[1].strip()

    combined = f"### Decisions\n\n{decisions}\n\n### Follow-ups\n\n{followups}"
    return highlights, combined


def main() -> None:
    projects = load_projects()
    notes = load_notes()
    template = TEMPLATE_FILE.read_text(encoding="utf-8")

    highlights, decisions_followups = split_notes(notes)

    report = template.format(
        portfolio_summary=build_portfolio_summary(projects),
        project_status=build_project_status(projects),
        meeting_highlights=highlights,
        decisions_followups=decisions_followups,
    )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(report.strip() + "\n", encoding="utf-8")
    print(f"Created {OUTPUT_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
