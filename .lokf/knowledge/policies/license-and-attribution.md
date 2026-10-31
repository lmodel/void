---
type: Policy
id: https://w3id.org/lmodel/void/knowledge/policies/license-and-attribution
genre: reference
title: Licence and attribution
description: "The repository's licences and what it may take from elsewhere: Apache-2.0 for the schema and code, CC BY 4.0 for the knowledge bundle, no text of the VoID Note (W3C Document License) or of the vocabulary file (no licence stated), the term lists' IRIs and facts, and the template's and KTL's notices."
resource: NOTICE
sources:
  - id: notice
    resource: NOTICE
    title: every section
  - resource: LICENSE
    title: the Apache License 2.0
  - id: readme.md
    resource: README.md
    title: the License section
  - resource: website/NOTICE
    title: the adapted graph explorer
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Licence and attribution

The schema and the code are under the Apache License 2.0, and the knowledge bundle in `.lokf/knowledge/` is under CC BY 4.0, as its `index.md` declares.[^readme.md]

NOTICE says what the repository takes from VoID. The Note is under the W3C Document License, which allows a changed version only in software and its documentation. The vocabulary file and the editors' repository state no licence. So the repository copies no definition, comment, label or example from either. The schema names each term by its IRI and describes it in this project's own words. The term lists hold IRIs and the facts the file states about them.[^notice] The schema names the other vocabularies (the DCMI Metadata Terms, FOAF, RDF Schema, the SPARQL Service Description and DCAT) by IRI only.

NOTICE also carries the MIT licence of linkml-project-copier and the Apache-2.0 notice of the Knowledge Trust Ladder's sidecar and website templates.[^notice]

[^readme.md]: README.md, the License section
[^notice]: NOTICE, every section
