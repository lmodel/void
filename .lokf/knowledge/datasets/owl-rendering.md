---
type: VoidDataset
id: https://w3id.org/lmodel/void/knowledge/datasets/owl-rendering
genre: reference
title: The schema's OWL rendering
description: "`project/owl/void.owl.ttl`, the OWL ontology that gen-owl writes from the void schema, described as a VoID dataset: a Turtle file that w3id serves at `https://w3id.org/lmodel/void/void.owl.ttl`, using the OWL and RDF Schema vocabularies."
resource: project/owl/void.owl.ttl
license: Apache-2.0
derivedFrom:
  - https://w3id.org/lmodel/void/knowledge/datasets/void-linkml-schema
feature:
  - http://www.w3.org/ns/formats/Turtle
dataDump:
  - https://w3id.org/lmodel/void/void.owl.ttl
vocabulary:
  - http://www.w3.org/2002/07/owl
  - http://www.w3.org/2000/01/rdf-schema
sources:
  - id: void.owl.ttl
    resource: project/owl/void.owl.ttl
    title: the prefixes and the ontology header
  - id: justfile
    resource: justfile
    title: the gen-owl call in the gen-project recipe
  - id: w3id
    resource: https://github.com/perma-id/w3id.org/blob/master/ids/lmodel/.htaccess
    title: the rule for an .owl.ttl address
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# The schema's OWL rendering

`project/owl/void.owl.ttl` is the OWL ontology of the schema, in Turtle. The `gen-project` recipe writes it with a last call to gen-owl.[^justfile] It declares an OWL class for each class of the schema and a property for each slot, with the prefixes `owl:`, `rdfs:`, `void:` and `void_linkml:` among others.[^void.owl.ttl]

This concept is typed with the schema's own `VoidDataset`, so its frontmatter says in VoID's terms what the file is: Turtle (`feature`), the vocabularies it uses (`vocabulary`), and the address that serves it (`dataDump`). The w3id rules for lmodel send an address ending in `.owl.ttl` to the file of that name in `project/owl/` on the default branch.[^w3id] It is a check that the domain schema works: `lokf validate` holds this concept to `.lokf/void.yaml`.

[^justfile]: justfile, the gen-project recipe
[^void.owl.ttl]: project/owl/void.owl.ttl, the prefixes
[^w3id]: <https://github.com/perma-id/w3id.org/blob/master/ids/lmodel/.htaccess>, the OWL rule
