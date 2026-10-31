---
type: Dataset
id: https://w3id.org/lmodel/void/knowledge/datasets/neighbour-copies
genre: reference
title: Neighbours' adapt copies
description: "The thirteen released lmodel adapt copies in `tests/neighbours/`, each pinned by its SHA-256, against which `tests/test_schema_rules.py` holds this schema's copy: no shared class, and only the listed shared keys (`subject`, `comment`, `modified`, `label`, `seeAlso`)."
resource: tests/neighbours
sources:
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the pins, the shared keys and the tests
  - resource: tests/neighbours
    title: the copies
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Neighbours' adapt copies

`tests/neighbours/` holds the schema assets of thirteen lmodel releases: slsa v0.8.0, github-actions v0.3.0, oscal v0.1.2, spdx v0.1.0, nist-sp-800-218 v0.1.1, nist-sp-800-53 v0.1.0, nist-sp-800-171 v0.1.0, nist-csf-v2 v0.1.0, in-toto v0.1.1, cis-controls v0.2.0, iso27001 v0.1.0, stix v0.1.0 and attack v0.1.0. Each was checked against its release's `.sha256` and attestation, and `tests/test_schema_rules.py` pins it by its SHA-256.[^test_schema_rules.py]

The test holds `.lokf/void.yaml` apart from LOKF and from each neighbour. No class, enum or type is shared. Five keys are shared, each under another IRI in the neighbour, and the test lists them so that a new one fails:

- `subject`, with six neighbours;
- `comment`, with attack, spdx and stix;
- `modified`, with attack and stix;
- `label`, with oscal;
- `seeAlso`, with spdx.

They are the local names of the Dublin Core and RDF Schema terms the schema keeps.[^test_schema_rules.py] The README points at lokf issue #169, which asks `lokf adapt` for a `--beside` option to rename them.[^readme.md]

[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and SHARED_WITH_NEIGHBOURS
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
