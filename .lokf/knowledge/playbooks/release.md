---
type: Playbook
id: https://w3id.org/lmodel/void/knowledge/playbooks/release
genre: how-to
title: Release a version
description: "How a version of void is released: entries under `## [Unreleased]` in `CHANGELOG.md`, a releasing commit type (`feat:`, `fix:`, `security:`), semantic-release on a push to `main` from the `v0.0.0` baseline, and the knowledge release that attaches the schema copy, the bundle and the Copilot skill."
sources:
  - id: contributing
    resource: CONTRIBUTING.md
    title: the Releasing (maintainers) section
  - id: releaserc
    resource: .releaserc.json
    title: the release rules
  - id: changelog
    resource: CHANGELOG.md
    title: the baseline paragraph
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Release a version

1. Write each change under `## [Unreleased]` in `CHANGELOG.md`; the release job refuses an empty section.[^contributing]
2. Type the commit for what it is. Only `feat:`, `fix:`, `security:` and a breaking change start a release, and below 1.0.0 a breaking change bumps the minor version.[^releaserc]
3. Before the first releasing merge, push the signed `v0.0.0` baseline tag on `main`, so the first release is 0.1.0.[^changelog]
4. On the merge, `semantic-release.yml` retitles the section, commits `CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub release. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches the knowledge release, which attaches `schema-<tag>-void.yaml`, the bundle zip and the Copilot skill zip, each with its `.sha256` and attestation.

[^contributing]: CONTRIBUTING.md, the Releasing (maintainers) section
[^releaserc]: .releaserc.json, the release rules
[^changelog]: CHANGELOG.md, the baseline paragraph
