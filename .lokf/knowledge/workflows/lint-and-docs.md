---
type: Service
id: https://w3id.org/lmodel/void/knowledge/workflows/lint-and-docs
genre: reference
title: Lint & docs (lint-and-docs.yaml)
description: "The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on pull requests, pushes to `main`, Mondays and by hand, it runs ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), markdownlint, lychee and codespell."
resource: .github/workflows/lint-and-docs.yaml
sources:
  - id: lint-and-docs.yaml
    resource: .github/workflows/lint-and-docs.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Lint & docs (lint-and-docs.yaml)

`.github/workflows/lint-and-docs.yaml` runs on every pull request, on a push to `main`, on Mondays at 06:00 UTC and by hand. Its four read-only jobs run:

- ShellCheck over the scripts;
- actionlint over the workflows;
- a word count that holds CONTRIBUTING.md to 1000 words and SECURITY.md to 900;
- markdownlint, lychee and codespell over the Markdown files.

The link check reads this repository's own links on `main` from the checkout.[^lint-and-docs.yaml]

[^lint-and-docs.yaml]: .github/workflows/lint-and-docs.yaml, the header comment, the on key and the jobs
