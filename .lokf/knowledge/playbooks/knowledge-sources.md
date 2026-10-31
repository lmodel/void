---
type: Playbook
id: https://w3id.org/lmodel/void/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location and external source this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose."
resource: .
sources:
  - resource: README.md
  - resource: docs/about.md
  - resource: docs/index.md
  - resource: src/void/schema
  - resource: src/void/datamodel
  - resource: project.justfile
  - resource: .lokf/void.yaml
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
  - resource: NOTICE
  - resource: LICENSE
  - resource: scripts
  - resource: .github/scripts
  - resource: .github/workflows
  - resource: .github/dependabot.yml
  - resource: .github/release
  - resource: justfile
  - resource: .linkml/generators.yaml
  - resource: .linkmllint.yaml
  - resource: project
  - resource: docs/schema
  - resource: docs/elements
  - resource: tests
  - resource: CONTRIBUTING.md
  - resource: .releaserc.json
  - resource: CHANGELOG.md
  - resource: website
  - resource: SECURITY.md
  - resource: AI_COVENANT.md
exclusions:
  - resource: .github/ISSUE_TEMPLATE
    reason: Issue forms, which are governance text and state nothing about the schema.
  - resource: .github/pull_request_template.md
    reason: The pull request checklist, which repeats CONTRIBUTING.md.
  - resource: CODE_OF_CONDUCT.md
    reason: The Contributor Covenant, governance text with nothing about the schema.
  - resource: uv.lock
    reason: The package's lock file, tooling that pins versions.
  - resource: pyproject.toml
    reason: Package metadata and spell checkers' settings; the changelog states the Python project's name.
  - resource: .gitignore
    reason: "Tooling: the files git ignores."
  - resource: .editorconfig
    reason: "Tooling: editor settings."
  - resource: .yamllint.yaml
    reason: "Tooling: the YAML linter's settings."
  - resource: .pre-commit-config.yaml
    reason: "Tooling: the hooks and the files they leave alone."
  - resource: .markdownlint-cli2.jsonc
    reason: "Tooling: the Markdown linter's settings."
  - resource: lychee.toml
    reason: "Tooling: the link checker's settings."
  - resource: config.public.mk
    reason: "Tooling: the variables the justfile loads."
  - resource: .copier-answers.yml
    reason: The copier template's answers, which `just update` reads.
  - resource: src/README.md
    reason: Text from the project template.
  - resource: docs/templates-linkml
    reason: The template's placeholders for gen-doc, not pages.
  - resource: examples/README.md
    reason: Text from the project template about generated example output.
  - resource: src/void/__init__.py
    reason: Package plumbing.
  - resource: src/void/_version.py
    reason: Package plumbing.
  - resource: src/void/schema/README.md
    reason: Text from the project template.
  - resource: llms.txt
    reason: The pointer that sends agents to this bundle.
  - resource: knowledge_bundle
    reason: The sidecar's link to the bundle.
  - resource: .github/PULL_REQUEST_TEMPLATE
    reason: The sidecar sync's pull request template.
  - resource: .lokf/lokf.yaml
    reason: LOKF's schema, pinned by the sidecar.
  - resource: .lokf/scripts
    reason: The sidecar's scripts, which the weekly sync replaces.
  - resource: .lokf/m365
    reason: The sidecar's Copilot skill builder and its instructions.
  - resource: .lokf/README.md
    reason: The sidecar's own README.
  - resource: .lokf/queries.http
    reason: The sidecar's sample queries.
  - resource: .lokf/ingest.yaml.sample
    reason: The sidecar's example ingest manifest, which this host does not use.
  - resource: .lokf/uv.lock
    reason: The sidecar's lock file.
  - resource: .lokf/.gitignore
    reason: The sidecar's git settings.
  - resource: .lokf/.gitattributes
    reason: The sidecar's git settings.
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Knowledge sources

A refresh run checks these sources again instead of finding them anew. Update this table whenever a source of the repository's knowledge moves, appears or goes.

Each concept derived from a file or folder of this repository names it by its path from the repository root, in `resource` and in `sources`. `knowledge-report.sh worklist` lists the concepts whose source moved since their stamp. It never fetches a page, so re-read the external sources this table names when the upstream watch reports a change.

| Source | Yields | Re-check by |
| --- | --- | --- |
| `src/void/schema/void.yaml` | `datasets/void-linkml-schema`, the `glossary/` terms, `explanations/names-and-iris` | re-read the header, the classes, the slots, the mappings and the comments |
| `project.justfile`, `.lokf/void.yaml`, `.lokf/justfile`, `.lokf/pyproject.toml`, the README's Knowledge Trust Ladder (KTL) section | the domain-schema section of `datasets/void-linkml-schema`, `glossary/adapt-copy` | re-read the `--root`, `--prefix` and `--keep` arguments, the copy's renames, the `schema :=` line and the `[tool.lokf]` table |
| `scripts/`, `.github/scripts/`, `tests/upstream/` | `playbooks/update-upstream-pins`, `datasets/upstream-term-lists`, `workflows/upstream-watch` | re-read the pins, the docstrings and the lists' header lines |
| `README.md` (What it models, Influences, Mappings, Not modelled here), `docs/about.md`, `.linkmllint.yaml`, `CHANGELOG.md` | `explanations/scope-and-influences`, `explanations/names-and-iris` | re-read each section and the lint comment |
| `justfile`, `.linkml/generators.yaml`, `project/`, `src/void/datamodel/`, `docs/schema/`, `docs/elements/` | `datasets/generated-artefacts`, `datasets/owl-rendering` | re-read the `gen-project`, `gen-doc` and `test` recipes and the `excludes`; re-list `project/*/` |
| `tests/` | `datasets/example-data`, `datasets/neighbour-copies` | re-count `valid/`, `problem/valid/` and `invalid/`; re-read the tests and the neighbours' checksums |
| the Validating data section of `docs/index.md` | `playbooks/validate-data` | re-read the section |
| `CONTRIBUTING.md`, the `lint`, `gen-project`, `gen-doc` and `test` recipes | `playbooks/regenerate-and-test` | confirm the setup, the checklist and the recipes |
| `.releaserc.json`, `.github/release/`, `CHANGELOG.md`, the Releasing section of `CONTRIBUTING.md` | `playbooks/release`, `workflows/semantic-release` | re-read the release rules, the commands and the baseline paragraph |
| the nine files in `.github/workflows/` | the nine `workflows/` concepts | re-read each file's `on` keys, its jobs' permissions and environments, and the variables it reads |
| `website/` | `services/documentation-site` | re-read `site.config.mjs` and `website/README.md` |
| `NOTICE`, `LICENSE`, `website/NOTICE`, the License section of `README.md` | `policies/license-and-attribution` | re-read each third-party entry |
| `SECURITY.md`, `.github/dependabot.yml` | `policies/security-policy` | re-read the table of surfaces and the settings not yet in force |
| `AI_COVENANT.md` | `policies/ai-covenant` | re-read the project note and the section on agent automation |
| <https://www.w3.org/TR/2011/NOTE-void-20110303/> | `references/void-note`, `glossary/void` | re-read it when the upstream watch reports a new edition |
| `rdfs/void.ttl` in <https://github.com/cygri/void> | `references/void-vocabulary-file` | re-read it when the upstream watch reports a changed file |
| the w3id.org rules for lmodel | the dump address in `datasets/owl-rendering` | re-read the OWL rule when the routes change |

The paths under `exclusions` are left out, each for the reason it gives: governance text, tooling settings, template text, package plumbing, the pointer for agents, and the sidecar's files. Some of the sidecar's files are sources even so: the domain schema, the justfile's `schema :=` line and the `[tool.lokf]` table.

No concept here quotes the VoID Note or the vocabulary file, whose text the repository does not copy.
