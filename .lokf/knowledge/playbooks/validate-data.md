---
type: Playbook
id: https://w3id.org/lmodel/void/knowledge/playbooks/validate-data
genre: how-to
title: Validate data against the void schema
description: How to check a VoID description written as YAML or JSON with `linkml-validate -s src/void/schema/void.yaml -C <Class>`, what the validator checks, what the generated dataclasses and Pydantic models leave out, and the three rules no validator states.
sources:
  - id: index.md
    resource: docs/index.md
    title: the Validating data section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T18:07:34Z"
status: draft
---

# Validate data against the void schema

1. Name the class the file holds, such as `Dataset` or `Linkset`, and run `linkml-validate -s src/void/schema/void.yaml -C Dataset dataset.yaml`.[^index.md]
2. Validate before loading a file into either model in `src/void/datamodel/`. The dataclasses check no pattern, minimum or number of values, and cannot load a class partition's `class` key. The Pydantic models check those, but they check neither that an address is an IRI nor the two rules that ask for one slot or another.
3. Check by hand, or as `tests/test_data.py` does, what no validator states:
   - a linkset's targets name two different datasets;
   - a `uriRegexPattern` is a regular expression;
   - each example and root resource starts with the `uriSpace` and matches the `uriRegexPattern`.

[^index.md]: docs/index.md, the Validating data section
