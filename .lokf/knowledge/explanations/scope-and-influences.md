---
type: Explanation
id: https://w3id.org/lmodel/void/knowledge/explanations/scope-and-influences
genre: explanation
title: Scope, influences and mappings
description: "What the void schema models and leaves out, the one influence beyond VoID (lmodel/slsa's release asset and governance files), and its mappings: `sd:Dataset` and `sd:Graph` as narrow and `dcat:Dataset` as broad for `Dataset`, `foaf:Document` for `DatasetDescription`, and `void:Dataset` for the partitions."
sources:
  - id: readme.md
    resource: README.md
    title: the What it models, Influences, Mappings and Not modelled here sections
  - id: void.yaml
    resource: src/void/schema/void.yaml
    title: the mappings and their notes
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Scope, influences and mappings

The schema models VoID's four classes and 27 properties, the Dublin Core and FOAF terms the Note uses in a description, and the label, comment and see-also of a technical feature. It leaves out the agents a description names, which FOAF describes, the Waiver vocabulary's terms, the SPARQL Service Description's own terms and `dcterms:date`.[^readme.md] Its one influence beyond VoID is lmodel/slsa, whose release asset and governance files it follows.

The schema borrows from no other vocabulary, and its mappings say only what VoID or the meaning of the terms states:[^void.yaml]

- `Dataset` names `sd:Dataset` and `sd:Graph` in `narrow_mappings`, as the Note's section 6.5 says, and `dcat:Dataset` in `broad_mappings`, since DCAT's dataset is any collection of data and VoID's holds RDF;
- `DatasetDescription` names `foaf:Document` in `broad_mappings`, as the vocabulary file states;
- the two partition classes name `void:Dataset` in `broad_mappings`.

[^readme.md]: README.md, the What it models, Influences and Not modelled here sections
[^void.yaml]: src/void/schema/void.yaml, the mappings and their notes
