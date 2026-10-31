---
type: Service
id: https://w3id.org/lmodel/void/knowledge/workflows/knowledge-registrar
genre: reference
title: Knowledge Registrar (knowledge-registrar.yaml)
description: "The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`, from the KTL sidecar: on a pull request that touches the bundle, on Mondays and by hand, it validates the bundle and runs the conventions script, and on a pull request it checks that each new human confirmation is backed by an approval or a signed commit."
resource: .github/workflows/knowledge-registrar.yaml
sources:
  - id: knowledge-registrar.yaml
    resource: .github/workflows/knowledge-registrar.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Knowledge Registrar (knowledge-registrar.yaml)

`.github/workflows/knowledge-registrar.yaml` is the gate of the Knowledge Trust Ladder (KTL) sidecar. It runs on a pull request that touches `.lokf/` or `knowledge_bundle`, on Mondays at 06:00 UTC and by hand. Its `validate` job runs `lokf validate --check-refs` and the conventions script. On a pull request, its `provenance` job checks that each new `human:` confirmation is backed by the pull request's approval or a signed commit, and its `attestation` job runs only for one that is not.[^knowledge-registrar.yaml]

[^knowledge-registrar.yaml]: .github/workflows/knowledge-registrar.yaml, the header comment, the on key and the jobs
