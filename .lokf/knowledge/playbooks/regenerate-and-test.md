---
type: Playbook
id: https://w3id.org/lmodel/void/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test after a schema change
description: "How to change the void schema: edit `src/void/schema/void.yaml`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit the regenerated files with the change."
sources:
  - id: contributing
    resource: CONTRIBUTING.md
    title: Development setup and Before opening a pull request
  - id: justfile
    resource: justfile
    title: the lint, gen-project, gen-doc and test recipes
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Regenerate and test after a schema change

1. Install the tools once: `uv sync --group dev`, with [just](https://github.com/casey/just) on the path.[^contributing]
2. Edit `src/void/schema/void.yaml`. Keep VoID's names and IRIs, and describe each element in your own words.
3. Run `just lint`, which runs linkml-lint under `.linkmllint.yaml` and reports errors only.[^justfile]
4. Run `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit `project/`, `src/void/datamodel/`, `docs/schema/` and `.lokf/void.yaml` with the change.
5. Run `just test`: schema generation into `tmp/`, pytest and the example runner.
6. Add an example under `tests/data/valid/` for a new class, and a counter-example under `tests/data/invalid/` for a new constraint.

[^contributing]: CONTRIBUTING.md, Development setup and Before opening a pull request
[^justfile]: justfile, the lint recipe
