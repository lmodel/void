---
type: Service
id: https://w3id.org/lmodel/void/knowledge/workflows/main
genre: reference
title: Build and test (main.yaml)
description: "The Build and test workflow, `.github/workflows/main.yaml`: on every pull request and push to `main`, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`, with `uv sync --locked`."
resource: .github/workflows/main.yaml
sources:
  - id: main.yaml
    resource: .github/workflows/main.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Build and test (main.yaml)

`.github/workflows/main.yaml` runs on every pull request and on a push to `main`. Its `test` job reads the checkout only and runs on Python 3.10, 3.11, 3.12, 3.13 and 3.14. It installs just 1.47.0 and the project with `uv sync --locked --group dev`, and runs `just test`. On Python 3.13 it also runs `just lint` and, after installing `.lokf/`'s toolkit, `just lokf-adapt-check`, which fails when `.lokf/void.yaml` is stale.[^main.yaml]

[^main.yaml]: .github/workflows/main.yaml, the header comment, the on key and the jobs
