---
type: Dataset
id: https://w3id.org/lmodel/void/knowledge/datasets/upstream-term-lists
genre: reference
title: Upstream term lists
description: "The two term lists in `tests/upstream/`, which `scripts/extract_void_terms.py` writes from pinned files: VoID's 31 terms with the domain, range, parent and functional facts of each, and the classes and properties of the five other vocabularies the schema names. `tests/test_upstream.py` holds the schema and its mappings to them."
resource: tests/upstream
derivedFrom:
  - https://w3id.org/lmodel/void/knowledge/references/void-vocabulary-file
sources:
  - id: upstream
    resource: tests/upstream
    title: the two lists and their header lines
  - id: extract
    resource: scripts/extract_void_terms.py
    title: the docstring and the pins
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the tests
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Upstream term lists

`tests/upstream/` holds two lists, each with header lines that name the files it was read from:[^upstream]

- `void-terms.tsv` lists the 31 terms VoID's vocabulary file declares, 4 classes and 27 properties, read at the editors' commit `5b2ca68b7897`. For each it gives the kind, whether VoID calls it functional, and its domain, range and parent. It holds no label or comment, which are the file's text.
- `vocabulary-terms.txt` lists the classes and properties that the published files of the DCMI Metadata Terms, FOAF, RDF Schema, the SPARQL 1.1 Service Description and DCAT declare.

`scripts/extract_void_terms.py` downloads each file into memory, refuses it unless its git object hash or SHA-256 is the pinned one, and writes the lists.[^extract] `tests/test_upstream.py` pins each list by its SHA-256 and checks that the schema renders every VoID term and no other. It also checks that each slot keeps its term's domain, range and cardinality, and that each mapping names a class its vocabulary declares.[^test_upstream.py]

[^upstream]: tests/upstream/, the header lines
[^extract]: scripts/extract_void_terms.py, the docstring
[^test_upstream.py]: tests/test_upstream.py, the tests
