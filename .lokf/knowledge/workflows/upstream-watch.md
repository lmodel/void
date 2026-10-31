---
type: Service
id: https://w3id.org/lmodel/void/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its void-sources job runs `scripts/check_upstream_release.py` against the VoID Note's page and the editors' repository, and on a finding opens or updates the issue titled Upstream watch: the VoID Note or vocabulary file has changed."
resource: .github/workflows/upstream-watch.yaml
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

`.github/workflows/upstream-watch.yaml` runs every Monday at 07:00 UTC and by hand. Its one job, `void-sources`, reads the checkout and holds `issues: write`. It runs `scripts/check_upstream_release.py` on the runner's Python, with the workflow's token, which the script sends to `api.github.com` alone. On a finding, `.github/scripts/report-issue.sh` opens the issue titled "Upstream watch: the VoID Note or vocabulary file has changed", or comments on the open one.[^upstream-watch.yaml] [Update the upstream pins](../playbooks/update-upstream-pins.md) says what each finding asks for.

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml, the header comment, the on key and the jobs
