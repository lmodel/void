---
type: GlossaryTerm
id: https://w3id.org/lmodel/void/knowledge/glossary/linkset
title: Linkset
description: "A linkset (`void:Linkset`): a dataset of RDF links between exactly two datasets, whose subjects lie in one and whose objects lie in the other, named with two targets or with a subjects' and an objects' target, and with at most one link predicate."
definedBy:
  - https://w3id.org/lmodel/void/knowledge/references/void-note
sources:
  - id: void.yaml
    resource: src/void/schema/void.yaml
    title: the Linkset class and its comments
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Linkset

A linkset is a `Dataset` of links between two datasets: each link's subject is described in one dataset and its object in the other. It names the two with `target`, or with `subjectsTarget` and `objectsTarget`, and it has at most one `linkPredicate`, such as `owl:sameAs`. The validator checks that two are named; `tests/test_data.py` checks that they differ.[^void.yaml]

[^void.yaml]: src/void/schema/void.yaml, the Linkset class
