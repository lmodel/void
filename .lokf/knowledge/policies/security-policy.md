---
type: Policy
id: https://w3id.org/lmodel/void/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the three assets a release carries, the ruleset on `main`, and the two repository settings not yet in force.
resource: SECURITY.md
sources:
  - id: security.md
    resource: SECURITY.md
    title: every section
  - id: dependabot.yml
    resource: .github/dependabot.yml
    title: the five update entries
generated:
  by: process:ktl-librarian
  at: "2026-10-31T18:07:34Z"
status: draft
---

# Security policy

`SECURITY.md` asks for a vulnerability to be reported through GitHub's private vulnerability reporting, not in a public issue. One person maintains the repository, so a first reply takes days, and there is no bounty. Only the latest release receives fixes.[^security.md]

A release carries the schema and the Python models generated from it. Nothing goes to PyPI. When the bundle or the schema changed, the knowledge release attaches three assets, each with its `.sha256` and a build-provenance attestation: the schema's adapt copy, the bundle as a zip and a Microsoft 365 Copilot skill zip. The upstream watch reads W3C's page of the Note and asks the GitHub API about the editors' repository, sending the workflow's token, which can write issues, to `api.github.com` alone.

The policy's table names each workflow and what holds it:

- read-only pull request checks;
- a release job only on a push to `main`, in the `release` Environment;
- the Pages scopes on the website's deploy job alone;
- an upstream watch that writes only issues;
- a librarian whose agent holds no write token.

Every workflow declares `permissions: {}` at the top and pins its actions to commit hashes, which Dependabot keeps current with the locks, monthly.[^dependabot.yml]

A ruleset on `main` blocks deletion and force-pushes and keeps the history linear. Two settings are not yet in force: required reviewers on the `release` Environment, and secret scanning with push protection.[^security.md]

[^security.md]: SECURITY.md, every section
[^dependabot.yml]: .github/dependabot.yml, the five entries
