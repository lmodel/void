# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Added

- **A LinkML rendering of the Vocabulary of Interlinked Datasets (VoID), as the W3C Interest Group Note of 3 March 2011 explains it.** Its four classes and 27 properties keep VoID's names and IRIs, the Dublin Core, FOAF and RDF Schema terms the Note uses keep theirs, and every description is this project's own.
- **The rules of the Note that LinkML can state**: counts of zero or more, identifiers and references that read as an IRI or a CURIE, a URI space that reads as the start of an IRI, a vocabulary IRI with no final hash, a linkset with two targets or a subjects' and an objects' target and one link predicate, a partition with one class or property, and a description about at least one dataset. Tests check the rest over the examples.
- **Term lists read from the pinned vocabulary files**, which the tests hold the schema and its mappings to, and a weekly upstream watch that reports a new edition of the Note, a change to the vocabulary file, a changed licence or a check that could not finish.
- **`.lokf/void.yaml`, the schema's `lokf adapt` copy, rooted on `Dataset`, `DatasetDescription` and `TechnicalFeature`.** The knowledge release attaches it as `schema-<tag>-void.yaml`, and tests hold its names apart from those of the Linked Open Knowledge Format (LOKF) and of thirteen released lmodel copies.
- **An example of each class and a counter-example for each constraint**, held to the validator by `just test`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.59.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **`.github/release/package-lock.json`, which pins semantic-release and every package it pulls in.** The release job installs from it with `npm ci`, and Dependabot keeps it current.

### Changed

- **The project moves from the 2023 linkml-project-cookiecutter to linkml-project-copier v0.5.0**, with uv in place of Poetry, and its Python project is named `void-linkml`. PyPI publishing stays off.
- **VoID's terms have VoID's IRIs.** The old schema bound `void:` to `https://w3id.org/lmodel/void/`; that namespace now holds only what the schema adds, under `void_linkml:`.
- **Classes and slots take VoID's own names**, such as `DatasetDescription` and `distinctSubjects`, in place of the old space-separated ones, such as `dataset description` and `distinct subjects`.

### Removed

- **The old schema's classes and slots that are not VoID's**: `named thing`, `resource`, `document`, `literal type` and the three subsets.
- **The guessed mappings**, such as the Wikidata, EFO, IAO and SIO ones.
- **The PyPI publishing workflow and the mkdocs site.** The knowledge website replaces the site.
