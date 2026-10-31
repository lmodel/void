<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# void

Vocabulary of Interlinked Datasets (VoID), W3C Note of 2011 (LinkML)

> **Two ways in.** This README is one; the other is a docent, a museum's name
> for a guide. Install
> [`ktl-docent`](https://github.com/noelmcloughlin/knowledge-trust-ladder) into
> whatever agent you already use, by a route from
> [the install page](https://w3id.org/ktl/docs/install/), and ask it anything
> about this project. It answers from `.lokf/knowledge/`,
> the checked part of what the project knows, and says how far each answer has
> been trusted (still a draft, checked by automation only, or confirmed by a
> named person). It opens the source for exact values, and records what it
> could not answer so the gap gets filled. The same docent serves a person at a
> prompt, an agent reading this file, or a chatbot that can load a skill.
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt`
> says how to weigh it.

## Documentation Website

[https://lmodel.github.io/void](https://lmodel.github.io/void)

## What it models

The schema renders the Vocabulary of Interlinked Datasets (VoID), the RDF vocabulary for describing a dataset of linked data: what it is and who made it, how to reach it, what it holds, and the links between it and other datasets. It follows [Describing Linked Datasets with the VoID Vocabulary](https://www.w3.org/TR/2011/NOTE-void-20110303/), a W3C Interest Group Note of 3 March 2011, and the vocabulary file its editors keep at [cygri/void](https://github.com/cygri/void/blob/master/rdfs/void.ttl). The schema holds:

* **Datasets** (`Dataset`): a body of RDF data named by an IRI, with its general metadata, its access points (SPARQL endpoint, data dumps, URI lookup), its structure (URI space, vocabularies, subsets) and its statistics.
* **Linksets** (`Linkset`): a dataset of links between two datasets, with its two targets and its link predicate.
* **Descriptions** (`DatasetDescription`): the document, such as a `void.ttl` file, that describes datasets.
* **Technical features** (`TechnicalFeature`): something a dataset supports, such as an RDF syntax.
* **Partitions** (`ClassBasedPartition`, `PropertyBasedPartition`): the counts for one class or one property, given inside their dataset.

Every VoID class and property keeps its VoID name and Internationalized Resource Identifier (IRI), such as `void:distinctSubjects`, and the Dublin Core, FOAF and RDF Schema terms the Note uses keep theirs, such as `dcterms:title`. Only the identifier `id` and the two partition classes are the schema's own, under `void_linkml:`. A record refers to another dataset by its IRI.

The schema header's `version` is 2011-03-03, the Note's date, and its `source` is the Note's dated address. Release tags number the schema's versions. `tests/upstream/void-terms.tsv` lists the terms of the vocabulary file at the editors' pinned commit, and the tests hold the schema to it. A weekly workflow opens an issue when W3C publishes another edition of the Note, the editors change the vocabulary file, or a licence changes. [docs/index.md](docs/index.md) lists what the validator checks and the rules the tests check instead.

## Influences

None beyond VoID: the schema renders one vocabulary, and its release asset and governance files follow [lmodel/slsa](https://github.com/lmodel/slsa).

## Mappings

The schema borrows from no other vocabulary. Where VoID states how its classes relate to another vocabulary's, a class says so in a mapping:

* `Dataset` names the SPARQL 1.1 Service Description's `sd:Dataset` and `sd:Graph` in `narrow_mappings`, as the Note's section 6.5 says, and DCAT's `dcat:Dataset` in `broad_mappings`, since [DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) offers VoID's properties for a DCAT dataset whose data is RDF, and a DCAT dataset may hold data in any format.
* `DatasetDescription` names `foaf:Document` in `broad_mappings`, as the vocabulary file states.
* The two partition classes name `void:Dataset` in `broad_mappings`, since VoID makes a partition a dataset.

`tests/test_upstream.py` checks that each mapping names a term the pinned file of its vocabulary declares.

## Not modelled here

* The text of the Note and of the vocabulary file. Every description is this project's own.
* `dcterms:date`: a slot named `date` takes the name of LinkML's date type, and the generated Pydantic model then checks no date. `created`, `issued` and `modified` carry the dates the Note names.
* The people and organisations a description names, which FOAF describes: the schema takes their IRIs.
* The Waiver vocabulary's terms and the SPARQL Service Description's own terms.
* The rules no validator can check, which [docs/index.md](docs/index.md) lists.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch and the term list extractor
* [src/void/schema/](src/void/schema): the LinkML schema, `void.yaml` (edit this)
* [src/void/datamodel/](src/void/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data), the term lists in [upstream/](tests/upstream) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle, written in the Linked Open Knowledge Format (LOKF). Its domain schema is `.lokf/void.yaml`, which `lokf adapt` writes from `src/void/schema/void.yaml`. Edit the source, never the copy. A release carries the copy as `schema-<tag>-void.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

`just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. The copy roots the three classes whose instances VoID names by an IRI on `Concept`, so a concept may name any of these four as its `type`. In Obsidian, add them to the KTL Registrar and KTL Curator plugins' *Known LOKF types* setting:

```text
VoidDataset, Linkset, DatasetDescription, TechnicalFeature
```

The partitions stay values inside a dataset's concept. In the copy, LOKF's `id` replaces the schema's own.

A host imports the copy beside `lokf.yaml`, and LinkML merges the two into one namespace, where the last definition of a name wins silently. So the copy renames each name LOKF also defines and keeps its IRI: the class `Dataset` becomes `VoidDataset`, and the keys `title`, `description`, `publisher`, `source`, `created`, `license` and `target` take a `void_` prefix, such as `void_title`. A concept's own `title` and `description` are LOKF's.

Five keys are a neighbour copy's too, under another IRI there: `subject` is attack's, in-toto's, oscal's, slsa's, spdx's and stix's; `comment` attack's, spdx's and stix's; `modified` attack's and stix's; `label` oscal's; and `seeAlso` spdx's. In a host that imports both copies, one of them projects under the other's IRI. [lokf #169](https://github.com/nicholsn/lokf/issues/169) asks `adapt` for a `--beside` option to rename them. No class is shared. `tests/test_schema_rules.py` lists every shared name, checks the copy against LOKF and thirteen released neighbours, and fails on a new one.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)). The knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), as its `index.md` declares.

The Note is under the W3C Document License, and the vocabulary file states no licence, so this repository carries the text of neither: see [NOTICE](NOTICE). This is not a W3C project, and its use implies no endorsement by W3C or VoID's authors.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
