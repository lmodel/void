---
type: GlossaryTerm
id: https://w3id.org/lmodel/void/knowledge/glossary/adapt-copy
title: Adapt copy
description: "An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its top classes re-rooted on `Concept` and every name LOKF also defines renamed with its IRI kept. Here it is `.lokf/void.yaml`."
sources:
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: project.justfile
    resource: project.justfile
    title: the comment above the recipes
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Adapt copy

An adapt copy is what `lokf adapt` writes from a published LinkML schema, so that a knowledge bundle can use the schema's classes beside LOKF's own. It roots the classes it is given on `Concept`, drops the schema's identifier for LOKF's `id`, and renames each name LOKF also defines, keeping the IRI.[^readme.md] This repository's copy is `.lokf/void.yaml`. `just lokf-adapt` rewrites it and `just lokf-adapt-check` says when it is stale.[^project.justfile] A release attaches it as `schema-<tag>-void.yaml`.

[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^project.justfile]: project.justfile, the knowledge bundle recipes
