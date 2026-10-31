---
type: GlossaryTerm
id: https://w3id.org/lmodel/void/knowledge/glossary/linkset
title: Linkset
description: "A linkset (`void:Linkset`): a dataset of triples joining exactly two datasets, each triple's subject in one and its object in the other, named with two targets or with a subjects' and an objects' target, and with at most one link predicate."
definedBy:
  - https://w3id.org/lmodel/void/knowledge/references/void-note
sources:
  - id: void.yaml
    resource: src/void/schema/void.yaml
    title: the Linkset class and its comments
generated:
  by: process:ktl-librarian
  at: "2026-10-31T18:09:37Z"
status: draft
---

# Linkset

A linkset is a `Dataset` of triples that join two datasets: each triple's subject belongs to one of them and its object to the other. It names the two with `target`, or with `subjectsTarget` and `objectsTarget`, and it has at most one `linkPredicate`, such as `owl:sameAs`. The validator checks that two are named, and `tests/test_data.py` checks that they differ.[^void.yaml]

[^void.yaml]: src/void/schema/void.yaml, the Linkset class
