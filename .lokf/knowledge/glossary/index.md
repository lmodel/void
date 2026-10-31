# Glossary

* [VoID](void.md) - VoID, the Vocabulary of Interlinked Datasets: an RDF vocabulary, under the namespace `http://rdfs.org/ns/void#`, for describing datasets of linked data and the links between them. This repository renders it as a LinkML schema.
* [Linkset](linkset.md) - A linkset (`void:Linkset`): a dataset of triples joining exactly two datasets, each triple's subject in one and its object in the other, named with two targets or with a subjects' and an objects' target, and with at most one link predicate.
* [Partition](partition.md) - A class-based or property-based partition: the slice of a dataset about one class's members or made of one property's triples, given in this schema as a `ClassBasedPartition` or `PropertyBasedPartition` value inside its dataset, usually to state counts.
* [Adapt copy](adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its top classes re-rooted on `Concept` and every name LOKF also defines renamed with its IRI kept. Here it is `.lokf/void.yaml`.
