# About void

This page is for anyone reading the [LinkML](https://linkml.io) schema's
elements: it says what the classes are and what the model leaves out.

VoID describes a dataset of RDF data as a whole: what it is and who made it,
how to reach it, what it holds, and which links join it to other datasets.
The schema has a class for each of VoID's four classes. A `Dataset` is
the data itself, named by an IRI. A `Linkset` is a dataset of links between
two datasets. A `DatasetDescription` is the document, such as a `void.ttl`
file, that describes them. A `TechnicalFeature` is something a dataset
supports, such as an RDF syntax. Two classes of the schema's own,
`ClassBasedPartition` and `PropertyBasedPartition`, hold the counts for one
class or one property inside the dataset they belong to.

The names are VoID's own, and so are the IRIs: `void:Dataset` is
`http://rdfs.org/ns/void#Dataset`, and the slot `distinctSubjects` is
`void:distinctSubjects`. The general metadata keeps the Dublin Core and FOAF
names and IRIs the Note uses, such as `title` (`dcterms:title`) and
`homepage` (`foaf:homepage`). Only what the schema adds (the identifier `id`
and the two partition classes) is in its own namespace, `void_linkml:`
(`https://w3id.org/lmodel/void/`). A record refers to another dataset by its
IRI; a partition sits inside its dataset.

The descriptions are this project's own words. The Note is under the W3C
Document License and the vocabulary file states no licence, so the schema,
its examples and these pages carry no text of either. NOTICE states the
position.

## What is left out

- `dcterms:date`: a slot named `date` would take the name of LinkML's date
  type, and the generated Pydantic model would then check none of the dates.
  `created`, `issued` and `modified` carry the dates the Note names.
- The people and organisations a description names as creator, contributor
  or publisher: the schema takes their IRIs, and FOAF describes them.
- The Waiver vocabulary's norms and waiver statements, and the SPARQL
  Service Description terms, which describe a service rather than a dataset.
- The deprecated parts of earlier VoID versions, such as statistics through
  the Statistical Core Vocabulary.

## Reference

- [Describing Linked Datasets with the VoID Vocabulary](https://www.w3.org/TR/2011/NOTE-void-20110303/), W3C Interest Group Note, 3 March 2011
- [The vocabulary file](https://github.com/cygri/void/blob/master/rdfs/void.ttl), as its editors keep it
