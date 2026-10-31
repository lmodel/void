# void

This project is a LinkML model of the Vocabulary of Interlinked Datasets
(VoID), the RDF vocabulary for describing datasets of linked data and the
links between them. It follows the W3C Interest Group Note of 3 March 2011,
and the vocabulary file its editors keep. Every VoID class and property keeps
its VoID name and IRI, and the Dublin Core, FOAF and RDF Schema terms a VoID
description uses keep theirs.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): what the classes are and what the model leaves out
- [`void.yaml`](schema/void.yaml): the schema

## Validating data

`linkml-validate -s src/void/schema/void.yaml -C Dataset dataset.yaml`
checks a file against the JSON Schema generated from the schema, and
`tests/test_data.py` holds every example to it. The validator checks:

- that each count, such as `triples` or `entities`, is a whole number of zero
  or more;
- that `uriSpace` reads as the start of an IRI, and that a `vocabulary` IRI
  has no final hash;
- that a linkset names two targets, or a subjects' and an objects' target,
  and at most one link predicate;
- that a class partition names one class and a property partition one
  property;
- that a dataset description names the dataset it is about, as its
  `primaryTopic` or among its `topic`s;
- that each identifier, each reference to another dataset or feature, and
  each `class`, `property` and `linkPredicate` reads as an IRI or a CURIE;
- that each address, such as a `dataDump`, is an IRI, that each date and
  count has its form, and that a record holds no key its class lacks.

Validate a file before loading it into either model in `src/void/datamodel/`.
LinkML 1.12.1 generates models that check less:

- The dataclasses check required fields and types, but no pattern, minimum
  or number of values, and they cannot load a class partition's `class` key,
  which is a Python keyword.
- The Pydantic models load that key and check the patterns, minimums and
  numbers of values, but not that an address is an IRI, and not the two
  rules that ask for one slot or another: a linkset's targets and a
  description's topic.

No validator checks these rules:

- that a linkset's targets, its subjects' target and its objects' target
  together name exactly two different datasets;
- that a `uriRegexPattern` is a regular expression;
- that each example and root resource of a dataset starts with its
  `uriSpace` and matches its `uriRegexPattern`, where it states them.

`tests/test_data.py` checks all three over every valid example.
