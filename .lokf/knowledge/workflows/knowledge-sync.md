---
type: Service
id: https://w3id.org/lmodel/void/knowledge/workflows/knowledge-sync
genre: reference
title: Knowledge sync (knowledge-sync.yaml)
description: "The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`, from the KTL sidecar: every Monday at 04:10 UTC and by hand, it compares the skills pin with KTL's newest release and opens or refreshes one pull request that moves the pin and the sidecar's copies, holding workflow changes for a reviewer."
resource: .github/workflows/knowledge-sync.yaml
sources:
  - id: knowledge-sync.yaml
    resource: .github/workflows/knowledge-sync.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Knowledge sync (knowledge-sync.yaml)

`.github/workflows/knowledge-sync.yaml` runs every Monday at 04:10 UTC and by hand. It reads the skills pin and KTL's newest release, and when the pin is behind it copies the files `knowledge-sync.manifest` lists from that release. Its `publish` job, in the `knowledge-sync` Environment, opens or refreshes one pull request. A change to a workflow waits for the review Environment that `KNOWLEDGE_SYNC_REVIEW_ENVIRONMENT` names.[^knowledge-sync.yaml]

[^knowledge-sync.yaml]: .github/workflows/knowledge-sync.yaml, the header comment, the on key and the jobs
