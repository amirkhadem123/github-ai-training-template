# Exercise 4 — Respond to Review Feedback

## Scenario

Imagine that a reviewer has looked at your Risks change and left this comment:

> The Risks section is useful, but please group or order the risks by owner so the list is easier to scan. Keep the change limited to the Risks section.

## Your task

Do not immediately tell the AI to make the change.

First ask:

> Explain this review feedback in plain language. Propose the smallest update needed to address it. Tell me which files should change. Do not modify anything yet.

Then:

1. review the plan;
2. approve the change;
3. run the workflow again;
4. inspect the result;
5. inspect the diff;
6. create another meaningful commit;
7. push the branch.

If your pull request is still open, it will update automatically.

## Completion check

You should be able to explain why review feedback normally leads to another commit on the same working branch rather than a brand-new project.
