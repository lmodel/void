---
type: GlossaryTerm
id: https://w3id.org/lmodel/void/knowledge/glossary/partition
title: Partition
description: "A class-based or property-based partition: the part of a dataset that describes one class's instances or holds one property's triples, given in this schema as a `ClassBasedPartition` or `PropertyBasedPartition` value inside its dataset, usually to state counts."
definedBy:
  - https://w3id.org/lmodel/void/knowledge/references/void-note
sources:
  - id: void.yaml
    resource: src/void/schema/void.yaml
    title: the two partition classes and their comments
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Partition

VoID calls the part of a dataset that describes one class's instances a class-based partition, and the part that holds one property's triples a property-based partition. Each is itself a dataset, usually a blank node. VoID gives them no class of their own, so the schema writes each as a value inside its dataset, in `classPartition` or `propertyPartition`. Its classes `ClassBasedPartition` and `PropertyBasedPartition` sit under `void_linkml:`. Each names one `class` or one `property` and may carry the counts.[^void.yaml]

[^void.yaml]: src/void/schema/void.yaml, the partition classes
