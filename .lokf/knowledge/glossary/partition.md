---
type: GlossaryTerm
id: https://w3id.org/lmodel/void/knowledge/glossary/partition
title: Partition
description: "A class-based or property-based partition: the slice of a dataset about one class's members or made of one property's triples, given in this schema as a `ClassBasedPartition` or `PropertyBasedPartition` value inside its dataset, usually to state counts."
definedBy:
  - https://w3id.org/lmodel/void/knowledge/references/void-note
sources:
  - id: void.yaml
    resource: src/void/schema/void.yaml
    title: the two partition classes and their comments
generated:
  by: process:ktl-librarian
  at: "2026-10-31T18:09:37Z"
status: draft
---

# Partition

A class-based partition is the slice of a dataset about the members of one class, and a property-based partition is the slice made of the triples whose predicate is one property. VoID counts each as a dataset in its own right, usually a blank node. VoID gives them no class of their own, so the schema writes each as a value inside its dataset, in `classPartition` or `propertyPartition`. Its classes `ClassBasedPartition` and `PropertyBasedPartition` sit under `void_linkml:`. Each names one `class` or one `property` and may carry the counts.[^void.yaml]

[^void.yaml]: src/void/schema/void.yaml, the partition classes
