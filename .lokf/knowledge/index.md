---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/void/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: void Knowledge Bundle
description: Vocabulary of Interlinked Datasets (VoID), W3C Note of 2011 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/void/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# void Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for void. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/void/`: the README as its home page, `docs/`, the schema's pages, a page per concept and the four `lokf export` files, with redirects from the retired mkdocs site's addresses.

# Datasets

* [void LinkML schema](datasets/void-linkml-schema.md) - The LinkML schema of the Vocabulary of Interlinked Datasets (VoID), `src/void/schema/void.yaml` (schema id `https://w3id.org/lmodel/void`, version 2011-03-03): VoID's four classes and 27 properties under VoID's own names and IRIs, two partition classes of its own, and the Dublin Core, FOAF and RDF Schema terms a VoID description uses. Its `lokf adapt` copy `.lokf/void.yaml` is the bundle's domain schema.
* [Generated artefacts](datasets/generated-artefacts.md) - What `just gen-project` and `just gen-doc` generate from the void schema: the projections in `project/` (JSON Schema, JSON-LD, OWL, SHACL, ShEx, SQL, GraphQL, Protobuf, Excel, Java, TypeScript), the Python dataclasses and Pydantic models in `src/void/datamodel/`, the merged schema in `docs/schema/` and the schema pages in `docs/elements/`.
* [The schema's OWL rendering](datasets/owl-rendering.md) - `project/owl/void.owl.ttl`, the OWL ontology that gen-owl writes from the void schema, described as a VoID dataset: a Turtle file that w3id serves at `https://w3id.org/lmodel/void/void.owl.ttl`, using the OWL and RDF Schema vocabularies.
* [Example data](datasets/example-data.md) - The examples `tests/test_data.py` checks: valid records of every class in `tests/data/valid/` and `tests/data/problem/valid/`, and counter-examples in `tests/data/invalid/`, each naming in its first line, `# Fails at:`, where the validator must report it.
* [Upstream term lists](datasets/upstream-term-lists.md) - The two term lists in `tests/upstream/`, which `scripts/extract_void_terms.py` writes from pinned files: VoID's 31 terms with the domain, range, parent and functional facts of each, and the classes and properties of the five other vocabularies the schema names. `tests/test_upstream.py` holds the schema and its mappings to them.
* [Neighbours' adapt copies](datasets/neighbour-copies.md) - The thirteen released lmodel adapt copies in `tests/neighbours/`, each pinned by its SHA-256, against which `tests/test_schema_rules.py` holds this schema's copy: no shared class, and only the listed shared keys (`subject`, `comment`, `modified`, `label`, `seeAlso`).

# References

* [Describing Linked Datasets with the VoID Vocabulary](references/void-note.md) - The W3C Interest Group Note of 3 March 2011 that explains the Vocabulary of Interlinked Datasets (VoID), by Keith Alexander, Richard Cyganiak, Michael Hausenblas and Jun Zhao, at `https://www.w3.org/TR/2011/NOTE-void-20110303/`, under the W3C Document License. The schema header pins it as its source.
* [VoID's vocabulary file](references/void-vocabulary-file.md) - The RDF Schema file that declares VoID's classes and properties, `rdfs/void.ttl` in the editors' repository cygri/void, pinned at commit `5b2ca68b7897` by its git object hash, since the namespace document at `http://rdfs.org/ns/void` redirects to a host that no longer answers. It states no licence.

# Glossary

* [VoID](glossary/void.md) - VoID, the Vocabulary of Interlinked Datasets: an RDF vocabulary, under the namespace `http://rdfs.org/ns/void#`, for describing datasets of linked data and the links between them. This repository renders it as a LinkML schema.
* [Linkset](glossary/linkset.md) - A linkset (`void:Linkset`): a dataset of triples joining exactly two datasets, each triple's subject in one and its object in the other, named with two targets or with a subjects' and an objects' target, and with at most one link predicate.
* [Partition](glossary/partition.md) - A class-based or property-based partition: the slice of a dataset about one class's members or made of one property's triples, given in this schema as a `ClassBasedPartition` or `PropertyBasedPartition` value inside its dataset, usually to state counts.
* [Adapt copy](glossary/adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its top classes re-rooted on `Concept` and every name LOKF also defines renamed with its IRI kept. Here it is `.lokf/void.yaml`.

# Explanations

* [Names and IRIs](explanations/names-and-iris.md) - Why the schema keeps VoID's names and IRIs (`void:Dataset`, `void:distinctSubjects`) and the Dublin Core, FOAF and RDF Schema ones, puts only what it adds under `void_linkml:`, names the partition classes as it does, relaxes the slot naming rule, and leaves `dcterms:date` out.
* [Scope, influences and mappings](explanations/scope-and-influences.md) - What the void schema models and leaves out, the one influence beyond VoID (lmodel/slsa's release asset and governance files), and its mappings: `sd:Dataset` and `sd:Graph` as narrow and `dcat:Dataset` as broad for `Dataset`, `foaf:Document` for `DatasetDescription`, and `void:Dataset` for the partitions.

# Playbooks

* [Regenerate and test after a schema change](playbooks/regenerate-and-test.md) - How to change the void schema: edit `src/void/schema/void.yaml`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit the regenerated files with the change.
* [Validate data against the void schema](playbooks/validate-data.md) - How to check a VoID description written as YAML or JSON with `linkml-validate -s src/void/schema/void.yaml -C <Class>`, what the validator checks, what the generated dataclasses and Pydantic models leave out, and the three rules no validator states.
* [Update the upstream pins](playbooks/update-upstream-pins.md) - What to do when the upstream watch opens an issue: a new edition of the VoID Note, a changed or dropped vocabulary file, a changed licence, or a check that could not finish; which pins move together (the watch, `scripts/extract_void_terms.py`, the schema header and the term lists' checksums).
* [Release a version](playbooks/release.md) - How a version of void is released: entries under `## [Unreleased]` in `CHANGELOG.md`, a releasing commit type (`feat:`, `fix:`, `security:`), semantic-release on a push to `main` from the `v0.0.0` baseline, and the knowledge release that attaches the schema copy, the bundle and the Copilot skill.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose.

# Policies

* [Security policy](policies/security-policy.md) - How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the three assets a release carries, the ruleset on `main`, and the two repository settings not yet in force.
* [Licence and attribution](policies/license-and-attribution.md) - The repository's licences and what it may take from elsewhere: Apache-2.0 for the schema and code, CC BY 4.0 for the knowledge bundle, no text of the VoID Note (W3C Document License) or of the vocabulary file (no licence stated), the term lists' IRIs and facts, and the template's and KTL's notices.
* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work on void: a contributor owns what they submit, an element must say what VoID says, no text of the Note or the vocabulary file, VoID's terms keep VoID's IRIs, and the scheduled librarian commits as a bot, through pull requests a person approves.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow, `.github/workflows/main.yaml`: on every pull request and push to `main`, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`, with `uv sync --locked`.
* [Lint & docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on pull requests, pushes to `main`, Mondays and by hand, it runs ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), markdownlint, lychee and codespell.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its void-sources job runs `scripts/check_upstream_release.py` against the VoID Note's page and the editors' repository, and on a finding opens or updates the issue titled Upstream watch: the VoID Note or vocabulary file has changed.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request to `main` its plan job says what the merge would release; on a push to `main` its release job, in the `release` Environment, runs semantic-release from `.github/release/package-lock.json` and dispatches the knowledge release.
* [Knowledge Registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`, from the KTL sidecar: on a pull request that touches the bundle, on Mondays and by hand, it validates the bundle and runs the conventions script, and on a pull request it checks that each new human confirmation is backed by an approval or a signed commit.
* [Knowledge Librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`, from the KTL sidecar: every Monday at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`, it runs the ktl-librarian skill at the pinned KTL release in a read-only job and opens a review pull request from a job that runs no agent.
* [Knowledge Release (knowledge-release.yaml)](workflows/knowledge-release.md) - The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`, from the KTL sidecar: on a published release once `KNOWLEDGE_RELEASE_ENABLED` is `true`, or by hand, it validates and packs the bundle and attaches the bundle zip, the Copilot skill zip and the schema copy `schema-<tag>-void.yaml`, each with its `.sha256` and attestation.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`, from the KTL sidecar: every Monday at 04:10 UTC and by hand, it compares the skills pin with KTL's newest release and opens or refreshes one pull request that moves the pin and the sidecar's copies, holding workflow changes for a reviewer.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`, from the KTL website templates: it builds the site on a pull request or push that touches its inputs, on Mondays and by hand, and deploys it to GitHub Pages from `main` once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
