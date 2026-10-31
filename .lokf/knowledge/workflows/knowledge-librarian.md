---
type: Service
id: https://w3id.org/lmodel/void/knowledge/workflows/knowledge-librarian
genre: reference
title: Knowledge Librarian (knowledge-librarian.yaml)
description: "The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`, from the KTL sidecar: every Monday at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`, it runs the ktl-librarian skill at the pinned KTL release in a read-only job and opens a review pull request from a job that runs no agent."
resource: .github/workflows/knowledge-librarian.yaml
sources:
  - id: knowledge-librarian.yaml
    resource: .github/workflows/knowledge-librarian.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Knowledge Librarian (knowledge-librarian.yaml)

`.github/workflows/knowledge-librarian.yaml` runs the ktl-librarian skill every Monday at 05:00 UTC and by hand. Its `earlier` job reads what became of the earlier pull requests. Its `refresh` job runs the agent in the `knowledge-librarian` Environment with no write token, from the skills pinned at `TRUST_LADDER_SKILLS_REF` v0.59.0. Its `publish` job runs no agent and opens the review pull request, refusing a change outside the bundle or to a person's record.[^knowledge-librarian.yaml]

[^knowledge-librarian.yaml]: .github/workflows/knowledge-librarian.yaml, the header comment, the on key and the jobs
