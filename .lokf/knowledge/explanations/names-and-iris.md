---
type: Explanation
id: https://w3id.org/lmodel/void/knowledge/explanations/names-and-iris
genre: explanation
title: Names and IRIs
description: Why the schema keeps VoID's names and IRIs (`void:Dataset`, `void:distinctSubjects`) and the Dublin Core, FOAF and RDF Schema ones, puts only what it adds under `void_linkml:`, names the partition classes as it does, relaxes the slot naming rule, and leaves `dcterms:date` out.
sources:
  - id: about.md
    resource: docs/about.md
    title: the names paragraph and What is left out
  - id: linkmllint
    resource: .linkmllint.yaml
    title: the comment
  - id: void.yaml
    resource: src/void/schema/void.yaml
    title: the header comments and the partition comments
  - id: changelog
    resource: CHANGELOG.md
    title: the Changed section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Names and IRIs

The schema renders VoID, so a record's keys are the terms a VoID description in RDF uses, and each element's IRI is VoID's own: `void:Dataset` is `http://rdfs.org/ns/void#Dataset`. The Dublin Core, FOAF and RDF Schema slots keep their names and IRIs, such as `title` for `dcterms:title`. Only the identifier `id` and the two partition classes are the schema's own, under `void_linkml:` (`https://w3id.org/lmodel/void/`).[^about.md] The old schema had bound `void:` to that w3id namespace; VoID's terms now have VoID's IRIs.[^changelog]

VoID's properties are lowerCamelCase, so `.linkmllint.yaml` lets slot names take that form.[^linkmllint] The partition classes are `ClassBasedPartition` and `PropertyBasedPartition`, after VoID's phrase for them, because `ClassPartition` would differ from the `classPartition` slot only by case, and their schema pages would be one file on a filesystem that ignores case.[^void.yaml]

`dcterms:date` is left out. A slot named `date` takes the name of LinkML's date type, and the generated Pydantic model then checks none of the dates. `created`, `issued` and `modified` carry the dates the Note names.[^about.md]

[^about.md]: docs/about.md, the names paragraph and What is left out
[^changelog]: CHANGELOG.md, the Changed section
[^linkmllint]: .linkmllint.yaml, the comment
[^void.yaml]: src/void/schema/void.yaml, the partition classes
