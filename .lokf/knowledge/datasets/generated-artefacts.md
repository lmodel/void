---
type: Dataset
id: https://w3id.org/lmodel/void/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What `just gen-project` and `just gen-doc` generate from the void schema: the projections in `project/` (JSON Schema, JSON-LD, OWL, SHACL, ShEx, SQL, GraphQL, Protobuf, Excel, Java, TypeScript), the Python dataclasses and Pydantic models in `src/void/datamodel/`, the merged schema in `docs/schema/` and the schema pages in `docs/elements/`."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/void/knowledge/datasets/void-linkml-schema
sources:
  - id: justfile
    resource: justfile
    title: the gen-project, gen-doc and test recipes
  - id: generators.yaml
    resource: .linkml/generators.yaml
    title: the generators' settings
  - resource: project
    title: the generated folders
  - resource: src/void/datamodel
    title: the generated Python models
  - resource: docs/schema
    title: the merged schema
  - resource: docs/elements
    title: the schema pages gen-doc writes
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Generated artefacts

`just gen-project` runs gen-project with the settings in `.linkml/generators.yaml`, then gen-pydantic, gen-java, gen-typescript and gen-owl.[^justfile] It writes:

- `project/`, with a folder per projection: `excel/`, `graphql/`, `java/`, `jsonld/`, `jsonschema/`, `owl/`, `prefixmap/`, `protobuf/`, `shacl/`, `shex/`, `sqlschema/` and `typescript/`;
- `src/void/datamodel/void.py`, the dataclasses, and `void_pydantic.py`, the Pydantic models.

`just gen-doc` writes the merged schema to `docs/schema/void.yaml` and a page per element to `docs/elements/`, which git ignores and the website shows under `schema/`. The generators' settings skip the Markdown generator in gen-project.[^generators.yaml]

All of these are generated, so a change goes into the schema and the recipes run again. The OWL rendering in `project/owl/void.owl.ttl` is described on its own in [The schema's OWL rendering](owl-rendering.md).

[^justfile]: justfile, the gen-project and gen-doc recipes
[^generators.yaml]: .linkml/generators.yaml, the excludes and the generator arguments
