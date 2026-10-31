from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "2011-03-03"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'upstream_license': {'tag': 'upstream_license',
                                          'value': 'The Note is under the W3C '
                                                   'Document License '
                                                   '(https://www.w3.org/Consortium/Legal/copyright-documents); '
                                                   'the vocabulary file states no '
                                                   'licence.'},
                     'vocabulary_file': {'tag': 'vocabulary_file',
                                         'value': 'https://github.com/cygri/void/blob/5b2ca68b7897c2613d4269fd725f1812dce21267/rdfs/void.ttl'},
                     'vocabulary_modified': {'tag': 'vocabulary_modified',
                                             'value': '2011-03-06'}},
     'comments': ["The version is the date of the Note's edition, and the source "
                  'its dated address. The schema renders every class and property '
                  'that the vocabulary file declares, as its editors keep it at '
                  'the commit the vocabulary_file annotation names; '
                  'tests/upstream/void-terms.tsv lists them, and the tests hold '
                  'this schema to that list.',
                  'Neither the Note nor the vocabulary file is copied: every '
                  "description here is this project's own, and NOTICE says why.",
                  "Kept from the Note's account of a description: the Dublin Core "
                  "terms of its sections 2.2, 2.4 and 2.5, FOAF's homepage and "
                  'page (2.1) and topic and primaryTopic (6.2), and the RDF Schema '
                  'label, comment and seeAlso of a technical feature (2.6). Left '
                  'out: dcterms:date, since a slot named date takes the name of '
                  "LinkML's date type, and the generated Pydantic model then "
                  'checks none of the dates, while created, issued and modified '
                  'carry the dates the Note names; the agents a description names, '
                  "which FOAF describes; the Waiver vocabulary's norms and waiver "
                  '(2.4); and the SPARQL Service Description terms (6.5), which '
                  'describe a service rather than a dataset.'],
     'default_prefix': 'void_linkml',
     'default_range': 'string',
     'description': 'A LinkML rendering of the Vocabulary of Interlinked Datasets '
                    '(VoID), the RDF vocabulary for describing datasets of linked '
                    'data and the links between them, as the W3C Interest Group '
                    'Note of 3 March 2011 explains it. Every VoID class and '
                    'property keeps its VoID IRI, and the Dublin Core, FOAF and '
                    'RDF Schema terms the Note uses in a description keep theirs.',
     'id': 'https://w3id.org/lmodel/void',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'void',
     'prefixes': {'dcat': {'prefix_prefix': 'dcat',
                           'prefix_reference': 'http://www.w3.org/ns/dcat#'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'foaf': {'prefix_prefix': 'foaf',
                           'prefix_reference': 'http://xmlns.com/foaf/0.1/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'sd': {'prefix_prefix': 'sd',
                         'prefix_reference': 'http://www.w3.org/ns/sparql-service-description#'},
                  'void': {'prefix_prefix': 'void',
                           'prefix_reference': 'http://rdfs.org/ns/void#'},
                  'void_linkml': {'prefix_prefix': 'void_linkml',
                                  'prefix_reference': 'https://w3id.org/lmodel/void/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/void', 'https://www.w3.org/TR/void/'],
     'source': 'https://www.w3.org/TR/2011/NOTE-void-20110303/',
     'source_file': 'src/void/schema/void.yaml',
     'title': 'Vocabulary of Interlinked Datasets (VoID)'} )


class Dataset(ConfiguredBaseModel):
    """
    RDF triples from one provider, gathered under an IRI so that a description can speak of them as a whole.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['dcat:Dataset'],
         'class_uri': 'void:Dataset',
         'comments': ['A dataset is named by an IRI, and the IRI of another dataset is '
                      "how a subset, a linkset's target or a description refers to "
                      'it.'],
         'from_schema': 'https://w3id.org/lmodel/void',
         'narrow_mappings': ['sd:Dataset', 'sd:Graph'],
         'notes': ["The narrow mappings are the Note's own statement (section 6.5) "
                   "that a SPARQL service description's datasets and graphs are VoID "
                   "datasets. The broad mapping reads DCAT's dataset, any collection "
                   "of data that one agent publishes, as wider than VoID's, which "
                   'holds RDF alone.'],
         'tree_root': True})

    id: str = Field(default=..., description="""The IRI of the dataset, document or feature, written in full or as a CURIE.""", json_schema_extra = { "linkml_meta": {'comments': ['VoID has no property for the IRI, which RDF writes as the '
                      "subject, so the key lives in this schema's own namespace."],
         'domain_of': ['Dataset', 'DatasetDescription', 'TechnicalFeature']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name for the dataset or document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A few sentences of prose saying what the dataset or document contains.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'],
         'slot_uri': 'dcterms:description'} })
    creator: Optional[list[str]] = Field(default=None, description="""The IRI of the agent, human or not, that chiefly made the dataset or document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'], 'slot_uri': 'dcterms:creator'} })
    contributor: Optional[list[str]] = Field(default=None, description="""The IRI of an agent that added to the dataset without being its main maker.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcterms:contributor'} })
    publisher: Optional[str] = Field(default=None, description="""The IRI of the agent that releases the dataset for others to use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcterms:publisher'} })
    source: Optional[list[str]] = Field(default=None, description="""The IRI of an earlier resource whose content the dataset draws on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcterms:source'} })
    created: Optional[date] = Field(default=None, description="""The date the dataset or document was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'], 'slot_uri': 'dcterms:created'} })
    issued: Optional[date] = Field(default=None, description="""The date the dataset was first published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcterms:issued'} })
    modified: Optional[date] = Field(default=None, description="""The date the dataset or document last changed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'], 'slot_uri': 'dcterms:modified'} })
    license: Optional[str] = Field(default=None, description="""The IRI of the licence that sets the terms for using the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcterms:license'} })
    subject: Optional[list[str]] = Field(default=None, description="""The IRI of a topic the dataset covers, such as a DBpedia resource or a SKOS concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcterms:subject'} })
    homepage: Optional[str] = Field(default=None, description="""The web page about the dataset itself.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'foaf:homepage'} })
    page: Optional[list[str]] = Field(default=None, description="""Any further web page with information on the dataset, for instance its download page or its catalogue entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'foaf:page'} })
    feature: Optional[list[str]] = Field(default=None, description="""Something the dataset's server or files support, for instance an RDF syntax, named by its IRI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:feature'} })
    sparqlEndpoint: Optional[list[str]] = Field(default=None, description="""A SPARQL service whose default graph holds the dataset, for running queries on it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:sparqlEndpoint'} })
    dataDump: Optional[list[str]] = Field(default=None, description="""A downloadable RDF file holding all of the dataset or a share of it.""", json_schema_extra = { "linkml_meta": {'comments': ['A page that links to downloads is not a dump; give it as a page '
                      'instead.'],
         'domain_of': ['Dataset'],
         'slot_uri': 'void:dataDump'} })
    uriLookupEndpoint: Optional[list[str]] = Field(default=None, description="""A web address that, with an entity's percent-encoded IRI added to its end, answers an HTTP GET with RDF about that entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:uriLookupEndpoint'} })
    openSearchDescription: Optional[list[str]] = Field(default=None, description="""An OpenSearch file telling a client how to run keyword searches over the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:openSearchDescription'} })
    rootResource: Optional[list[str]] = Field(default=None, description="""The IRI of a starting point for crawling the dataset: a resource from which links lead, within a few hops, to all the others.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:rootResource'} })
    exampleResource: Optional[list[str]] = Field(default=None, description="""The IRI of an entity typical of the dataset, for a reader to look up.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:exampleResource'} })
    uriSpace: Optional[str] = Field(default=None, description="""The string every entity IRI in the dataset starts with, such as http://example.org/resource/.""", json_schema_extra = { "linkml_meta": {'comments': ['VoID writes it as a literal, not as an IRI, so the range is a '
                      "string, held to the form of an IRI's start."],
         'domain_of': ['Dataset'],
         'slot_uri': 'void:uriSpace'} })
    uriRegexPattern: Optional[str] = Field(default=None, description="""A regular expression in SPARQL's syntax that each entity IRI of the dataset satisfies.""", json_schema_extra = { "linkml_meta": {'comments': ["The validator checks no regular expression's syntax; "
                      'tests/test_data.py compiles each one in the examples.'],
         'domain_of': ['Dataset'],
         'slot_uri': 'void:uriRegexPattern'} })
    vocabulary: Optional[list[str]] = Field(default=None, description="""The namespace IRI of a vocabulary the dataset uses, as a term's IRI reads without its local name and without a final hash, such as http://xmlns.com/foaf/0.1/.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:vocabulary'} })
    subset: Optional[list[str]] = Field(default=None, description="""Another dataset contained in this one, named by its IRI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:subset'} })
    classPartition: Optional[list[ClassBasedPartition]] = Field(default=None, description="""The dataset's slice for one class, given inside it.""", json_schema_extra = { "linkml_meta": {'comments': ['VoID makes it a narrower subset; here it is a value, so it does '
                      "not inherit subset's range."],
         'domain_of': ['Dataset'],
         'slot_uri': 'void:classPartition'} })
    propertyPartition: Optional[list[PropertyBasedPartition]] = Field(default=None, description="""The dataset's slice for one property, given inside it.""", json_schema_extra = { "linkml_meta": {'comments': ['VoID makes it a narrower subset; here it is a value, so it does '
                      "not inherit subset's range."],
         'domain_of': ['Dataset', 'ClassBasedPartition'],
         'slot_uri': 'void:propertyPartition'} })
    triples: Optional[int] = Field(default=None, description="""How many triples the dataset holds; for a linkset, how many links.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:triples'} })
    entities: Optional[int] = Field(default=None, description="""How many entities, resources with an IRI, the dataset describes.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:entities'} })
    classes: Optional[int] = Field(default=None, description="""How many distinct classes the dataset's rdf:type triples name.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:classes'} })
    properties: Optional[int] = Field(default=None, description="""How many distinct properties the dataset's triples use as predicates.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:properties'} })
    distinctSubjects: Optional[int] = Field(default=None, description="""How many distinct IRIs and blank nodes the dataset's triples have as subjects.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:distinctSubjects'} })
    distinctObjects: Optional[int] = Field(default=None, description="""How many distinct IRIs, blank nodes and literals the dataset's triples have as objects.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:distinctObjects'} })
    documents: Optional[int] = Field(default=None, description="""How many RDF documents together carry the dataset, for example RDFa web pages.""", ge=0, json_schema_extra = { "linkml_meta": {'comments': ['Use it where the triples are hard to count; triples and '
                      'entities say more where they can be given.'],
         'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:documents'} })

    @field_validator('uriSpace')
    def pattern_uriSpace(cls, v):
        pattern=re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:[^\s]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid uriSpace format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid uriSpace format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('vocabulary')
    def pattern_vocabulary(cls, v):
        pattern=re.compile(r"[^#]$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid vocabulary format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid vocabulary format: {v}"
            raise ValueError(err_msg)
        return v


class Linkset(Dataset):
    """
    A dataset of triples that join two datasets: each triple's subject belongs to one of them and its object to the other.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'description': 'Two targets, named with target.',
                     'slot_conditions': {'target': {'name': 'target',
                                                    'required': True}}},
                    {'description': "The subjects' target and the objects' target.",
                     'slot_conditions': {'objectsTarget': {'name': 'objectsTarget',
                                                           'required': True},
                                         'subjectsTarget': {'name': 'subjectsTarget',
                                                            'required': True}}}],
         'class_uri': 'void:Linkset',
         'comments': ['A linkset links exactly two distinct datasets: the targets, the '
                      "subjects' target and the objects' target together name two. The "
                      'validator checks that two are named; tests/test_data.py checks '
                      'that they differ.'],
         'from_schema': 'https://w3id.org/lmodel/void',
         'slot_usage': {'target': {'maximum_cardinality': 2,
                                   'minimum_cardinality': 2,
                                   'multivalued': True,
                                   'name': 'target'}}})

    target: Optional[list[str]] = Field(default=None, description="""Either dataset a linkset joins, named by its IRI.""", min_length=2, max_length=2, json_schema_extra = { "linkml_meta": {'comments': ['Linkset makes it a list of two. The slot itself stays '
                      'single-valued, so that subjectsTarget and objectsTarget, its '
                      'narrower slots, inherit one value each.'],
         'domain_of': ['Linkset'],
         'slot_uri': 'void:target'} })
    subjectsTarget: Optional[str] = Field(default=None, description="""The dataset at the subject end of every link in a linkset, named by its IRI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkset'], 'is_a': 'target', 'slot_uri': 'void:subjectsTarget'} })
    objectsTarget: Optional[str] = Field(default=None, description="""The dataset at the object end of every link in a linkset, named by its IRI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkset'], 'is_a': 'target', 'slot_uri': 'void:objectsTarget'} })
    linkPredicate: Optional[str] = Field(default=None, description="""The property every link of a linkset has as its predicate, such as owl:sameAs.""", json_schema_extra = { "linkml_meta": {'comments': ['A linkset has one; links with two predicates make two '
                      'linksets.'],
         'domain_of': ['Linkset'],
         'slot_uri': 'void:linkPredicate'} })
    id: str = Field(default=..., description="""The IRI of the dataset, document or feature, written in full or as a CURIE.""", json_schema_extra = { "linkml_meta": {'comments': ['VoID has no property for the IRI, which RDF writes as the '
                      "subject, so the key lives in this schema's own namespace."],
         'domain_of': ['Dataset', 'DatasetDescription', 'TechnicalFeature']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name for the dataset or document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A few sentences of prose saying what the dataset or document contains.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'],
         'slot_uri': 'dcterms:description'} })
    creator: Optional[list[str]] = Field(default=None, description="""The IRI of the agent, human or not, that chiefly made the dataset or document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'], 'slot_uri': 'dcterms:creator'} })
    contributor: Optional[list[str]] = Field(default=None, description="""The IRI of an agent that added to the dataset without being its main maker.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcterms:contributor'} })
    publisher: Optional[str] = Field(default=None, description="""The IRI of the agent that releases the dataset for others to use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcterms:publisher'} })
    source: Optional[list[str]] = Field(default=None, description="""The IRI of an earlier resource whose content the dataset draws on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcterms:source'} })
    created: Optional[date] = Field(default=None, description="""The date the dataset or document was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'], 'slot_uri': 'dcterms:created'} })
    issued: Optional[date] = Field(default=None, description="""The date the dataset was first published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcterms:issued'} })
    modified: Optional[date] = Field(default=None, description="""The date the dataset or document last changed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'], 'slot_uri': 'dcterms:modified'} })
    license: Optional[str] = Field(default=None, description="""The IRI of the licence that sets the terms for using the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcterms:license'} })
    subject: Optional[list[str]] = Field(default=None, description="""The IRI of a topic the dataset covers, such as a DBpedia resource or a SKOS concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcterms:subject'} })
    homepage: Optional[str] = Field(default=None, description="""The web page about the dataset itself.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'foaf:homepage'} })
    page: Optional[list[str]] = Field(default=None, description="""Any further web page with information on the dataset, for instance its download page or its catalogue entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'foaf:page'} })
    feature: Optional[list[str]] = Field(default=None, description="""Something the dataset's server or files support, for instance an RDF syntax, named by its IRI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:feature'} })
    sparqlEndpoint: Optional[list[str]] = Field(default=None, description="""A SPARQL service whose default graph holds the dataset, for running queries on it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:sparqlEndpoint'} })
    dataDump: Optional[list[str]] = Field(default=None, description="""A downloadable RDF file holding all of the dataset or a share of it.""", json_schema_extra = { "linkml_meta": {'comments': ['A page that links to downloads is not a dump; give it as a page '
                      'instead.'],
         'domain_of': ['Dataset'],
         'slot_uri': 'void:dataDump'} })
    uriLookupEndpoint: Optional[list[str]] = Field(default=None, description="""A web address that, with an entity's percent-encoded IRI added to its end, answers an HTTP GET with RDF about that entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:uriLookupEndpoint'} })
    openSearchDescription: Optional[list[str]] = Field(default=None, description="""An OpenSearch file telling a client how to run keyword searches over the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:openSearchDescription'} })
    rootResource: Optional[list[str]] = Field(default=None, description="""The IRI of a starting point for crawling the dataset: a resource from which links lead, within a few hops, to all the others.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:rootResource'} })
    exampleResource: Optional[list[str]] = Field(default=None, description="""The IRI of an entity typical of the dataset, for a reader to look up.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:exampleResource'} })
    uriSpace: Optional[str] = Field(default=None, description="""The string every entity IRI in the dataset starts with, such as http://example.org/resource/.""", json_schema_extra = { "linkml_meta": {'comments': ['VoID writes it as a literal, not as an IRI, so the range is a '
                      "string, held to the form of an IRI's start."],
         'domain_of': ['Dataset'],
         'slot_uri': 'void:uriSpace'} })
    uriRegexPattern: Optional[str] = Field(default=None, description="""A regular expression in SPARQL's syntax that each entity IRI of the dataset satisfies.""", json_schema_extra = { "linkml_meta": {'comments': ["The validator checks no regular expression's syntax; "
                      'tests/test_data.py compiles each one in the examples.'],
         'domain_of': ['Dataset'],
         'slot_uri': 'void:uriRegexPattern'} })
    vocabulary: Optional[list[str]] = Field(default=None, description="""The namespace IRI of a vocabulary the dataset uses, as a term's IRI reads without its local name and without a final hash, such as http://xmlns.com/foaf/0.1/.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:vocabulary'} })
    subset: Optional[list[str]] = Field(default=None, description="""Another dataset contained in this one, named by its IRI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'void:subset'} })
    classPartition: Optional[list[ClassBasedPartition]] = Field(default=None, description="""The dataset's slice for one class, given inside it.""", json_schema_extra = { "linkml_meta": {'comments': ['VoID makes it a narrower subset; here it is a value, so it does '
                      "not inherit subset's range."],
         'domain_of': ['Dataset'],
         'slot_uri': 'void:classPartition'} })
    propertyPartition: Optional[list[PropertyBasedPartition]] = Field(default=None, description="""The dataset's slice for one property, given inside it.""", json_schema_extra = { "linkml_meta": {'comments': ['VoID makes it a narrower subset; here it is a value, so it does '
                      "not inherit subset's range."],
         'domain_of': ['Dataset', 'ClassBasedPartition'],
         'slot_uri': 'void:propertyPartition'} })
    triples: Optional[int] = Field(default=None, description="""How many triples the dataset holds; for a linkset, how many links.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:triples'} })
    entities: Optional[int] = Field(default=None, description="""How many entities, resources with an IRI, the dataset describes.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:entities'} })
    classes: Optional[int] = Field(default=None, description="""How many distinct classes the dataset's rdf:type triples name.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:classes'} })
    properties: Optional[int] = Field(default=None, description="""How many distinct properties the dataset's triples use as predicates.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:properties'} })
    distinctSubjects: Optional[int] = Field(default=None, description="""How many distinct IRIs and blank nodes the dataset's triples have as subjects.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:distinctSubjects'} })
    distinctObjects: Optional[int] = Field(default=None, description="""How many distinct IRIs, blank nodes and literals the dataset's triples have as objects.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:distinctObjects'} })
    documents: Optional[int] = Field(default=None, description="""How many RDF documents together carry the dataset, for example RDFa web pages.""", ge=0, json_schema_extra = { "linkml_meta": {'comments': ['Use it where the triples are hard to count; triples and '
                      'entities say more where they can be given.'],
         'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:documents'} })

    @field_validator('uriSpace')
    def pattern_uriSpace(cls, v):
        pattern=re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:[^\s]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid uriSpace format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid uriSpace format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('vocabulary')
    def pattern_vocabulary(cls, v):
        pattern=re.compile(r"[^#]$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid vocabulary format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid vocabulary format: {v}"
            raise ValueError(err_msg)
        return v


class DatasetDescription(ConfiguredBaseModel):
    """
    A web document, such as a void.ttl file published beside a dataset, that describes one or more datasets.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'description': 'The one dataset the description is about.',
                     'slot_conditions': {'primaryTopic': {'name': 'primaryTopic',
                                                          'required': True}}},
                    {'description': 'The datasets the description is about.',
                     'slot_conditions': {'topic': {'name': 'topic',
                                                   'required': True}}}],
         'broad_mappings': ['foaf:Document'],
         'class_uri': 'void:DatasetDescription',
         'from_schema': 'https://w3id.org/lmodel/void',
         'notes': ["The broad mapping is the vocabulary file's own statement that a "
                   'dataset description is a FOAF document.']})

    id: str = Field(default=..., description="""The IRI of the dataset, document or feature, written in full or as a CURIE.""", json_schema_extra = { "linkml_meta": {'comments': ['VoID has no property for the IRI, which RDF writes as the '
                      "subject, so the key lives in this schema's own namespace."],
         'domain_of': ['Dataset', 'DatasetDescription', 'TechnicalFeature']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name for the dataset or document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A few sentences of prose saying what the dataset or document contains.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'],
         'slot_uri': 'dcterms:description'} })
    creator: Optional[list[str]] = Field(default=None, description="""The IRI of the agent, human or not, that chiefly made the dataset or document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'], 'slot_uri': 'dcterms:creator'} })
    created: Optional[date] = Field(default=None, description="""The date the dataset or document was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'], 'slot_uri': 'dcterms:created'} })
    modified: Optional[date] = Field(default=None, description="""The date the dataset or document last changed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetDescription'], 'slot_uri': 'dcterms:modified'} })
    primaryTopic: Optional[str] = Field(default=None, description="""The dataset a description is about, when it describes one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetDescription'], 'slot_uri': 'foaf:primaryTopic'} })
    topic: Optional[list[str]] = Field(default=None, description="""A dataset a description is about, when it describes several of equal weight.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetDescription'], 'slot_uri': 'foaf:topic'} })
    inDataset: Optional[str] = Field(default=None, description="""The dataset that this document's triples belong to, named by its IRI.""", json_schema_extra = { "linkml_meta": {'comments': ['A document names one; a document in two datasets points at a '
                      'dataset that holds both as subsets.'],
         'domain_of': ['DatasetDescription'],
         'slot_uri': 'void:inDataset'} })


class TechnicalFeature(ConfiguredBaseModel):
    """
    A technical property of how a dataset is served, such as an RDF syntax it can be read in or an HTTP feature its server supports.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'void:TechnicalFeature',
         'comments': ['W3C names the RDF syntaxes under http://www.w3.org/ns/formats/, '
                      'such as http://www.w3.org/ns/formats/Turtle; a feature of '
                      "another kind takes an IRI of its publisher's own."],
         'from_schema': 'https://w3id.org/lmodel/void'})

    id: str = Field(default=..., description="""The IRI of the dataset, document or feature, written in full or as a CURIE.""", json_schema_extra = { "linkml_meta": {'comments': ['VoID has no property for the IRI, which RDF writes as the '
                      "subject, so the key lives in this schema's own namespace."],
         'domain_of': ['Dataset', 'DatasetDescription', 'TechnicalFeature']} })
    label: Optional[str] = Field(default=None, description="""A short name for the feature.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TechnicalFeature'], 'slot_uri': 'rdfs:label'} })
    comment: Optional[str] = Field(default=None, description="""A sentence or two about the feature.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TechnicalFeature'], 'slot_uri': 'rdfs:comment'} })
    seeAlso: Optional[list[str]] = Field(default=None, description="""A web page that tells more about the feature.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TechnicalFeature'], 'slot_uri': 'rdfs:seeAlso'} })


class ClassBasedPartition(ConfiguredBaseModel):
    """
    The slice of a dataset about the members of one class, written inside that dataset, most often to give counts for it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['void:Dataset'],
         'class_uri': 'void_linkml:ClassBasedPartition',
         'comments': ['VoID gives a partition no class of its own: it is a dataset, '
                      'usually a blank node. This schema writes it as a value inside '
                      'its dataset, so it has no IRI, and its class lives in this '
                      "schema's own namespace. The name follows VoID's phrase for it "
                      "and differs from the classPartition slot's by more than case, "
                      'so that their pages are two files on a filesystem that ignores '
                      'case.'],
         'from_schema': 'https://w3id.org/lmodel/void',
         'slot_usage': {'class': {'name': 'class', 'required': True}}})

    class_: str = Field(default=..., alias="class", description="""The class whose instances a class partition describes, named by its IRI, such as foaf:Person.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClassBasedPartition'], 'slot_uri': 'void:class'} })
    triples: Optional[int] = Field(default=None, description="""How many triples the dataset holds; for a linkset, how many links.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:triples'} })
    entities: Optional[int] = Field(default=None, description="""How many entities, resources with an IRI, the dataset describes.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:entities'} })
    classes: Optional[int] = Field(default=None, description="""How many distinct classes the dataset's rdf:type triples name.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:classes'} })
    properties: Optional[int] = Field(default=None, description="""How many distinct properties the dataset's triples use as predicates.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:properties'} })
    distinctSubjects: Optional[int] = Field(default=None, description="""How many distinct IRIs and blank nodes the dataset's triples have as subjects.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:distinctSubjects'} })
    distinctObjects: Optional[int] = Field(default=None, description="""How many distinct IRIs, blank nodes and literals the dataset's triples have as objects.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:distinctObjects'} })
    documents: Optional[int] = Field(default=None, description="""How many RDF documents together carry the dataset, for example RDFa web pages.""", ge=0, json_schema_extra = { "linkml_meta": {'comments': ['Use it where the triples are hard to count; triples and '
                      'entities say more where they can be given.'],
         'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:documents'} })
    propertyPartition: Optional[list[PropertyBasedPartition]] = Field(default=None, description="""The dataset's slice for one property, given inside it.""", json_schema_extra = { "linkml_meta": {'comments': ['VoID makes it a narrower subset; here it is a value, so it does '
                      "not inherit subset's range."],
         'domain_of': ['Dataset', 'ClassBasedPartition'],
         'slot_uri': 'void:propertyPartition'} })


class PropertyBasedPartition(ConfiguredBaseModel):
    """
    The slice of a dataset made of the triples whose predicate is one property, written inside that dataset, most often to give counts for it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['void:Dataset'],
         'class_uri': 'void_linkml:PropertyBasedPartition',
         'comments': ['As for a class partition, VoID gives it no class of its own, '
                      'and this schema writes it as a value inside its dataset.'],
         'from_schema': 'https://w3id.org/lmodel/void',
         'slot_usage': {'property': {'name': 'property', 'required': True}}})

    property: str = Field(default=..., description="""The property whose triples a property partition holds, named by its IRI, such as foaf:name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertyBasedPartition'], 'slot_uri': 'void:property'} })
    triples: Optional[int] = Field(default=None, description="""How many triples the dataset holds; for a linkset, how many links.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:triples'} })
    entities: Optional[int] = Field(default=None, description="""How many entities, resources with an IRI, the dataset describes.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:entities'} })
    classes: Optional[int] = Field(default=None, description="""How many distinct classes the dataset's rdf:type triples name.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:classes'} })
    properties: Optional[int] = Field(default=None, description="""How many distinct properties the dataset's triples use as predicates.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:properties'} })
    distinctSubjects: Optional[int] = Field(default=None, description="""How many distinct IRIs and blank nodes the dataset's triples have as subjects.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:distinctSubjects'} })
    distinctObjects: Optional[int] = Field(default=None, description="""How many distinct IRIs, blank nodes and literals the dataset's triples have as objects.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:distinctObjects'} })
    documents: Optional[int] = Field(default=None, description="""How many RDF documents together carry the dataset, for example RDFa web pages.""", ge=0, json_schema_extra = { "linkml_meta": {'comments': ['Use it where the triples are hard to count; triples and '
                      'entities say more where they can be given.'],
         'domain_of': ['Dataset', 'ClassBasedPartition', 'PropertyBasedPartition'],
         'slot_uri': 'void:documents'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Dataset.model_rebuild()
Linkset.model_rebuild()
DatasetDescription.model_rebuild()
TechnicalFeature.model_rebuild()
ClassBasedPartition.model_rebuild()
PropertyBasedPartition.model_rebuild()
