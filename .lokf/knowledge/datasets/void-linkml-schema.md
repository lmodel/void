---
type: Dataset
id: https://w3id.org/lmodel/void/knowledge/datasets/void-linkml-schema
genre: reference
title: void LinkML schema
description: "The LinkML schema of the Vocabulary of Interlinked Datasets (VoID), `src/void/schema/void.yaml` (schema id `https://w3id.org/lmodel/void`, version 2011-03-03): VoID's four classes and 27 properties under VoID's own names and IRIs, two partition classes of its own, and the Dublin Core, FOAF and RDF Schema terms a VoID description uses. Its `lokf adapt` copy `.lokf/void.yaml` is the bundle's domain schema."
resource: src/void/schema/void.yaml
version: "2011-03-03"
license: Apache-2.0
derivedFrom:
  - https://w3id.org/lmodel/void/knowledge/references/void-note
  - https://w3id.org/lmodel/void/knowledge/references/void-vocabulary-file
sources:
  - id: void.yaml
    resource: src/void/schema/void.yaml
    title: the header, the classes, the slots and their comments
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes and their roots
  - id: void-copy
    resource: .lokf/void.yaml
    title: the copy lokf adapt wrote
  - id: readme.md
    resource: README.md
    title: the What it models and Knowledge Trust Ladder (KTL) sections
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the tool.lokf table
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# void LinkML schema

`src/void/schema/void.yaml` is the schema, titled "Vocabulary of Interlinked Datasets (VoID)". Its header gives `version: "2011-03-03"`, the date of the W3C Interest Group Note, and `source: https://www.w3.org/TR/2011/NOTE-void-20110303/`, the Note's dated address. Its `vocabulary_file` annotation names the vocabulary file at the editors' commit `5b2ca68b7897`, and its licence is Apache-2.0.[^void.yaml]

## Classes

- **`Dataset`** (`void:Dataset`) is a body of RDF data named by an IRI. It holds the general metadata, the access points, the structure and the statistics, and it is the tree root.
- **`Linkset`** (`void:Linkset`) is a `Dataset` of links between two datasets. It names two `target`s, or a `subjectsTarget` and an `objectsTarget`, and at most one `linkPredicate`.
- **`DatasetDescription`** (`void:DatasetDescription`) is the document that describes datasets. It names a `primaryTopic` or one or more `topic`s.
- **`TechnicalFeature`** (`void:TechnicalFeature`) is something a dataset supports, such as an RDF syntax.
- **`ClassBasedPartition`** and **`PropertyBasedPartition`** are the schema's own value classes, under `void_linkml:`. Each holds the counts for one class or one property inside its dataset, and names that class or property.

Every VoID property keeps its VoID local name and IRI, such as `distinctSubjects` (`void:distinctSubjects`). The Dublin Core, FOAF and RDF Schema slots keep theirs, such as `title` (`dcterms:title`) and `homepage` (`foaf:homepage`). The identifier `id` is the schema's own. Every count is an integer of zero or more.[^void.yaml]

## As the bundle's domain schema

A domain schema of the Linked Open Knowledge Format (LOKF) is a LinkML schema that adds a host's classes beside LOKF's `lokf.yaml`, so that `lokf validate` checks the concepts typed with them. This bundle's domain schema is `.lokf/void.yaml`, which `lokf adapt` writes from the schema. The `schema :=` line of `.lokf/justfile` and the `[tool.lokf]` table of `.lokf/pyproject.toml` both name it.[^readme.md]

`project.justfile` roots the copy on `Dataset`, `DatasetDescription` and `TechnicalFeature`, passes `--prefix void`, and passes `--keep source` to keep `dcterms:source` apart from LOKF's slot of the same IRI.[^project.justfile] In the copy, `Dataset` is `VoidDataset`, and `title`, `description`, `publisher`, `source`, `created`, `license` and `target` carry a `void_` prefix, each with its IRI.[^void-copy] A concept may name `VoidDataset`, `Linkset`, `DatasetDescription` or `TechnicalFeature` as its `type`.

[Generated artefacts](generated-artefacts.md) lists what is generated from this file, and [Names and IRIs](../explanations/names-and-iris.md) says why the names are VoID's.

[^void.yaml]: src/void/schema/void.yaml, the header, the classes and the slots
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^project.justfile]: project.justfile, the knowledge bundle recipes
[^void-copy]: .lokf/void.yaml, the classes and slots it renames
