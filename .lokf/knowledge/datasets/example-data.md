---
type: Dataset
id: https://w3id.org/lmodel/void/knowledge/datasets/example-data
genre: reference
title: Example data
description: "The examples `tests/test_data.py` checks: valid records of every class in `tests/data/valid/` and `tests/data/problem/valid/`, and counter-examples in `tests/data/invalid/`, each naming in its first line, `# Fails at:`, where the validator must report it."
resource: tests/data
derivedFrom:
  - https://w3id.org/lmodel/void/knowledge/datasets/void-linkml-schema
sources:
  - id: tests-data
    resource: tests/data
    title: the three folders and their README
  - id: test_data.py
    resource: tests/test_data.py
    title: the tests and the rules no validator states
  - id: index.md
    resource: docs/index.md
    title: the Validating data section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Example data

`tests/data/` holds the examples, each named after the class it is checked against, as `ClassName-anything.yaml`:[^tests-data]

- `valid/` holds records that conform to the schema;
- `problem/valid/` holds valid records with a class partition's `class` key, which the generated dataclasses cannot load under LinkML 1.12.1, since `class` is a Python keyword;
- `invalid/` holds counter-examples, each opening with `# Fails at: <pointer>`.

`tests/test_data.py` holds every valid example to the validator, the committed JSON Schema and the Pydantic model, and loads the ones in `valid/` into the dataclasses. Each counter-example must fail the validator at the place it names and nowhere else. The test also checks two rules no validator states over every valid example: a linkset's targets name two different datasets, and a dataset's example and root resources start with its `uriSpace` and match its `uriRegexPattern`.[^test_data.py] `docs/index.md` lists what the validator checks and what each generated model leaves out.[^index.md]

The records describe fictional datasets on `example.org` addresses, in the shapes of the Note's examples, and copy none of the Note's text.

[^tests-data]: tests/data/README.md
[^test_data.py]: tests/test_data.py, the docstrings
[^index.md]: docs/index.md, the Validating data section
