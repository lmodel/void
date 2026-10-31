---
type: Service
id: https://w3id.org/lmodel/void/knowledge/workflows/semantic-release
genre: reference
title: Semantic release (semantic-release.yml)
description: "The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request to `main` its plan job says what the merge would release; on a push to `main` its release job, in the `release` Environment, runs semantic-release from `.github/release/package-lock.json` and dispatches the knowledge release."
resource: .github/workflows/semantic-release.yml
sources:
  - id: semantic-release.yml
    resource: .github/workflows/semantic-release.yml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Semantic release (semantic-release.yml)

`.github/workflows/semantic-release.yml` has two jobs. On a pull request to `main`, `plan` reads the checkout and says what the merge would release. On a push to `main`, `release` runs in the `release` Environment with `contents: write` and `actions: write`. It installs semantic-release and its plugins from `.github/release/package-lock.json` with `npm ci --ignore-scripts`. It then promotes the changelog, tags the release, publishes it, and dispatches the knowledge release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.[^semantic-release.yml]

[^semantic-release.yml]: .github/workflows/semantic-release.yml, the header comment, the on key and the jobs
