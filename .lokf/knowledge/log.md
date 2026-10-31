# Change Log

## 2026-10-31

* **Prose**: reworded 8 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: the linkset and partition entries' descriptions follow their bodies, in the schema's own words rather than the Note's.
* **Changed**: the linkset and partition entries describe each term from the schema's own descriptions, which no longer follow the Note's wording.
* **Changed**: the security policy says the upstream watch's token can write issues, as `upstream-watch.yaml` grants and SECURITY.md now says, not that it is read-only.
* **Changed**: validating data says the Pydantic models now check the form of an identifier or a reference, which the schema holds to an IRI or a CURIE, and leave only an address's form unchecked.
* **Changed**: the schema concept says identifiers and references read as an IRI or a CURIE, and that each element cites its section of the Note, as `src/void/schema/void.yaml` now does.
* **Prose**: reworded 13 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Added**: void LinkML schema.
* **Added**: Generated artefacts.
* **Added**: The schema's OWL rendering.
* **Added**: Example data.
* **Added**: Upstream term lists.
* **Added**: Neighbours' adapt copies.
* **Added**: Describing Linked Datasets with the VoID Vocabulary.
* **Added**: VoID's vocabulary file.
* **Added**: VoID.
* **Added**: Linkset.
* **Added**: Partition.
* **Added**: Adapt copy.
* **Added**: Names and IRIs.
* **Added**: Scope, influences and mappings.
* **Added**: Regenerate and test after a schema change.
* **Added**: Validate data against the void schema.
* **Added**: Update the upstream pins.
* **Added**: Release a version.
* **Added**: Security policy.
* **Added**: Licence and attribution.
* **Added**: AI covenant.
* **Added**: Documentation site.
* **Added**: Build and test (main.yaml).
* **Added**: Lint & docs (lint-and-docs.yaml).
* **Added**: Upstream watch (upstream-watch.yaml).
* **Added**: Semantic release (semantic-release.yml).
* **Added**: Knowledge Registrar (knowledge-registrar.yaml).
* **Added**: Knowledge Librarian (knowledge-librarian.yaml).
* **Added**: Knowledge Release (knowledge-release.yaml).
* **Added**: Knowledge sync (knowledge-sync.yaml).
* **Added**: Knowledge website (knowledge-website.yaml).
* **Added**: Knowledge sources map.
* **Removal**: the sidecar's two placeholder services, which real concepts now replace.
* **Initialization**: Scaffolded the LOKF bundle for void with placeholder
  services. Real concepts to follow.
