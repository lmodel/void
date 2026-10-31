---
type: Reference
id: https://w3id.org/lmodel/void/knowledge/references/void-vocabulary-file
genre: reference
title: VoID's vocabulary file
description: The RDF Schema file that declares VoID's classes and properties, `rdfs/void.ttl` in the editors' repository cygri/void, pinned at commit `5b2ca68b7897` by its git object hash, since the namespace document at `http://rdfs.org/ns/void` redirects to a host that no longer answers. It states no licence.
resource: https://github.com/cygri/void/blob/5b2ca68b7897c2613d4269fd725f1812dce21267/rdfs/void.ttl
sources:
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the docstring and the vocabulary pins
  - id: terms
    resource: tests/upstream/void-terms.tsv
    title: the header lines
  - id: notice
    resource: NOTICE
    title: the VoID section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# VoID's vocabulary file

The editors' repository, cygri/void, keeps a copy of VoID's RDF Schema file as `rdfs/void.ttl`. The namespace document at `http://rdfs.org/ns/void` redirects to `http://vocab.deri.ie/void`, which no longer answers, so the schema reads the file from that repository.[^watch] `tests/upstream/void-terms.tsv` was read from it at commit `5b2ca68b7897`, git object `9a7ca133acf8`, whose `dcterms:modified` is 2011-03-06.[^terms]

The file and the repository state no licence, so this repository keeps a list of the file's terms and facts and none of its text.[^notice] The upstream watch reports when the file changes on the editors' default branch, a file is added beside it, or the repository states a licence.[^watch]

[^watch]: scripts/check_upstream_release.py, the docstring and the pins
[^terms]: tests/upstream/void-terms.tsv, the header lines
[^notice]: NOTICE, the VoID section
