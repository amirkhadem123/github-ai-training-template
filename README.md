# GitHub + AI Training Sandbox

This repository is the hands-on workspace for **GitHub + AI: Practical Workflows for Non-Technical Professionals**.

It is intentionally simple. You do not need to know Python, Git commands, or software development to use it.

## What you will practice

You will use this project to practice a standard AI-assisted workflow:

1. Understand the requirement.
2. Confirm which repository and branch you are working in.
3. Create a branch for the change.
4. Ask Codex or Claude Code to inspect the project.
5. Ask the AI to propose a plan before making changes.
6. Implement a small change.
7. Run and validate the workflow.
8. Review the changed files.
9. Commit and push your work.
10. Open a pull request.
11. Respond to review feedback.
12. Merge when the work is ready.

## Important: create your own copy

Do **not** use the training template itself as your working repository.

From the template repository, select **Use this template → Create a new repository**. Create your own training repository and complete all exercises there.

A suggested name is:

`github-ai-training-yourname`

Unless your instructor tells you otherwise, create only the default branch from the template.

## This is a disposable sandbox

Everything in this project uses fictional sample data and runs locally. It does not connect to production systems, customer data, or external services.

If you break your training copy, that is okay. The simplest reset is to create a fresh repository from the template.

## Project scenario

You manage a project team that produces a weekly status update from two inputs:

- `input/project-status.csv`
- `input/meeting-notes.md`

A small script produces:

- `output/weekly-update.md`

The starter workflow already creates a basic project summary. During the course, you will use an AI coding agent to improve it.

## Run the workflow

You do not need to memorize the command. Ask your AI assistant how to run the project.

If you want the direct command, from the repository root run:

```text
python scripts/generate-update.py
```

On some systems, the command may be `python3` instead of `python`.

## Start here

1. Read `COURSE-INSTRUCTIONS.md`.
2. Open `input/project-status.csv` and `input/meeting-notes.md`.
3. Open `output/weekly-update.md`.
4. Ask your AI assistant to explain the repository before changing anything.

## Safety

This project should never require real credentials. Do not add passwords, API keys, access tokens, customer data, or production configuration.

See `AGENTS.md` and `CLAUDE.md` for the instructions provided to AI coding agents.
