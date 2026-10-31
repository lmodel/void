---
type: Service
id: https://w3id.org/lmodel/void/knowledge/workflows/knowledge-release
genre: reference
title: Knowledge Release (knowledge-release.yaml)
description: "The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`, from the KTL sidecar: on a published release once `KNOWLEDGE_RELEASE_ENABLED` is `true`, or by hand, it validates and packs the bundle and attaches the bundle zip, the Copilot skill zip and the schema copy `schema-<tag>-void.yaml`, each with its `.sha256` and attestation."
resource: .github/workflows/knowledge-release.yaml
sources:
  - id: knowledge-release.yaml
    resource: .github/workflows/knowledge-release.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Knowledge Release (knowledge-release.yaml)

`.github/workflows/knowledge-release.yaml` runs on a published release once `KNOWLEDGE_RELEASE_ENABLED` is `true`, and when dispatched. Its `pack` job reads the checkout, validates the bundle and packs it, and says whether the bundle or the schema changed since the last release. Its `attach` job then attaches the assets, each with its `.sha256` and a build-provenance attestation, and runs no third-party package.[^knowledge-release.yaml]

[^knowledge-release.yaml]: .github/workflows/knowledge-release.yaml, the header comment, the on key and the jobs
