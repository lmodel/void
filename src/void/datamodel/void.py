# Auto generated from void.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-13T00:18:10
# Schema: void
#
# id: https://w3id.org/lmodel/void
# description: The Vocabulary of Interlinked Datasets (VoID) is an RDF Schema vocabulary for expressing metadata about RDF datasets. It is intended as a bridge between the publishers and users of RDF data, with applications ranging from data discovery to cataloging and archiving of datasets. This document provides a formal definition of the new RDF classes and properties introduced for VoID. It is a companion to the main specification document for VoID, Describing Linked Datasets with the VoID Vocabulary (http://www.w3.org/TR/void/).
# license: Apache Software License 2.0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EFO = CurieNamespace('EFO', 'http://identifiers.org/efo/')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
SIO = CurieNamespace('SIO', 'http://identifiers.org/sio/')
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/wiki/')
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms#')
DCTYPES = CurieNamespace('dctypes', 'http://purl.org/dc/dcmitype/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
VANN = CurieNamespace('vann', 'https://vocab.org/vann/')
VOID = CurieNamespace('void', 'https://w3id.org/lmodel/void/')
DEFAULT_ = VOID


# Types
class LiteralType(String):
    """ Literals are used for values such as strings, numbers, and dates """
    type_class_uri = RDF.literal
    type_class_curie = "rdf:literal"
    type_name = "literal type"
    type_model_uri = VOID.LiteralType


# Class references



class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Thing
    class_class_curie: ClassVar[str] = "owl:Thing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = VOID.NamedThing


class Resource(NamedThing):
    """
    source or supply from which benefit is produced
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS.Resource
    class_class_curie: ClassVar[str] = "rdfs:Resource"
    class_name: ClassVar[str] = "resource"
    class_model_uri: ClassVar[URIRef] = VOID.Resource


class Dataset(NamedThing):
    """
    A set of RDF triples that are published, maintained or aggregated by a single provider.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Dataset
    class_class_curie: ClassVar[str] = "schema:Dataset"
    class_name: ClassVar[str] = "dataset"
    class_model_uri: ClassVar[URIRef] = VOID.Dataset


class Document(NamedThing):
    """
    Form for preservation of structured and identified information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF.Document
    class_class_curie: ClassVar[str] = "foaf:Document"
    class_name: ClassVar[str] = "document"
    class_model_uri: ClassVar[URIRef] = VOID.Document


class DatasetDescription(Document):
    """
    A web resource whose foaf:primaryTopic or foaf:topics include void:Datasets.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VOID.DatasetDescription
    class_class_curie: ClassVar[str] = "void:DatasetDescription"
    class_name: ClassVar[str] = "dataset description"
    class_model_uri: ClassVar[URIRef] = VOID.DatasetDescription


class Linkset(Dataset):
    """
    A collection of RDF links between two void:Datasets.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VOID.Linkset
    class_class_curie: ClassVar[str] = "void:Linkset"
    class_name: ClassVar[str] = "linkset"
    class_model_uri: ClassVar[URIRef] = VOID.Linkset


class TechnicalFeature(NamedThing):
    """
    A technical feature of a void:Dataset, such as a supported RDF serialization format.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VOID.TechnicalFeature
    class_class_curie: ClassVar[str] = "void:TechnicalFeature"
    class_name: ClassVar[str] = "technical feature"
    class_model_uri: ClassVar[URIRef] = VOID.TechnicalFeature


# Enumerations


# Slots
class slots:
    pass

slots.class_partition = Slot(uri=VOID.class_partition, name="class partition", curie=VOID.curie('class_partition'),
                   model_uri=VOID.class_partition, domain=Dataset, range=Optional[Union[dict, "Dataset"]])

slots.data_dump = Slot(uri=VOID.data_dump, name="data dump", curie=VOID.curie('data_dump'),
                   model_uri=VOID.data_dump, domain=Dataset, range=Optional[Union[dict, Resource]])

slots.example_resource_of_dataset = Slot(uri=RDFS.resource, name="example resource of dataset", curie=RDFS.curie('resource'),
                   model_uri=VOID.example_resource_of_dataset, domain=Dataset, range=Optional[Union[dict, Resource]])

slots.feature = Slot(uri=VOID.feature, name="feature", curie=VOID.curie('feature'),
                   model_uri=VOID.feature, domain=Dataset, range=Optional[Union[dict, "TechnicalFeature"]])

slots.in_dataset = Slot(uri=VOID.in_dataset, name="in dataset", curie=VOID.curie('in_dataset'),
                   model_uri=VOID.in_dataset, domain=Document, range=Optional[Union[dict, Dataset]])

slots.a_link_predicate = Slot(uri=VOID.a_link_predicate, name="a link predicate", curie=VOID.curie('a_link_predicate'),
                   model_uri=VOID.a_link_predicate, domain=Linkset, range=Optional[Union[dict, NamedThing]])

slots.open_search_description = Slot(uri=VOID.open_search_description, name="open search description", curie=VOID.curie('open_search_description'),
                   model_uri=VOID.open_search_description, domain=Dataset, range=Optional[Union[dict, "Document"]])

slots.property_partition = Slot(uri=VOID.property_partition, name="property partition", curie=VOID.curie('property_partition'),
                   model_uri=VOID.property_partition, domain=Dataset, range=Optional[Union[dict, "Dataset"]])

slots.root_resource = Slot(uri=VOID.root_resource, name="root resource", curie=VOID.curie('root_resource'),
                   model_uri=VOID.root_resource, domain=Dataset, range=Optional[str])

slots.has_a_SPARQL_endpoint_at = Slot(uri=VOID.has_a_SPARQL_endpoint_at, name="has a SPARQL endpoint at", curie=VOID.curie('has_a_SPARQL_endpoint_at'),
                   model_uri=VOID.has_a_SPARQL_endpoint_at, domain=Dataset, range=Optional[str])

slots.has_subset = Slot(uri=VOID.has_subset, name="has subset", curie=VOID.curie('has_subset'),
                   model_uri=VOID.has_subset, domain=Dataset, range=Optional[Union[dict, "Dataset"]])

slots.target = Slot(uri=VOID.target, name="target", curie=VOID.curie('target'),
                   model_uri=VOID.target, domain=Linkset, range=Optional[Union[dict, Dataset]])

slots.has_an_URI_look_up_endpoint_at = Slot(uri=VOID.has_an_URI_look_up_endpoint_at, name="has an URI look-up endpoint at", curie=VOID.curie('has_an_URI_look_up_endpoint_at'),
                   model_uri=VOID.has_an_URI_look_up_endpoint_at, domain=Dataset, range=Optional[str])

slots.vocabulary = Slot(uri=VOID.vocabulary, name="vocabulary", curie=VOID.curie('vocabulary'),
                   model_uri=VOID.vocabulary, domain=Dataset, range=Optional[str])

slots.class = Slot(uri=RDFS.Class, name="class", curie=RDFS.curie('Class'),
                   model_uri=VOID.class, domain=Dataset, range=Optional[Union[dict, NamedThing]])

slots.objects_target = Slot(uri=VOID.objects_target, name="objects target", curie=VOID.curie('objects_target'),
                   model_uri=VOID.objects_target, domain=Linkset, range=Optional[Union[dict, Dataset]])

slots.property = Slot(uri=RDF.Property, name="property", curie=RDF.curie('Property'),
                   model_uri=VOID.property, domain=Dataset, range=Optional[Union[dict, NamedThing]])

slots.subjects_target = Slot(uri=VOID.subjects_target, name="subjects target", curie=VOID.curie('subjects_target'),
                   model_uri=VOID.subjects_target, domain=Linkset, range=Optional[Union[dict, Dataset]])

slots.classes = Slot(uri=VOID.classes, name="classes", curie=VOID.curie('classes'),
                   model_uri=VOID.classes, domain=Dataset, range=Optional[int])

slots.distinct_objects = Slot(uri=VOID.distinct_objects, name="distinct objects", curie=VOID.curie('distinct_objects'),
                   model_uri=VOID.distinct_objects, domain=Dataset, range=Optional[int])

slots.distinct_subjects = Slot(uri=VOID.distinct_subjects, name="distinct subjects", curie=VOID.curie('distinct_subjects'),
                   model_uri=VOID.distinct_subjects, domain=Dataset, range=Optional[int])

slots.number_of_documents = Slot(uri=VOID.number_of_documents, name="number of documents", curie=VOID.curie('number_of_documents'),
                   model_uri=VOID.number_of_documents, domain=Dataset, range=Optional[int])

slots.number_of_entities = Slot(uri=VOID.number_of_entities, name="number of entities", curie=VOID.curie('number_of_entities'),
                   model_uri=VOID.number_of_entities, domain=Dataset, range=Optional[int])

slots.number_of_properties = Slot(uri=VOID.number_of_properties, name="number of properties", curie=VOID.curie('number_of_properties'),
                   model_uri=VOID.number_of_properties, domain=Dataset, range=Optional[int])

slots.number_of_triples = Slot(uri=VOID.number_of_triples, name="number of triples", curie=VOID.curie('number_of_triples'),
                   model_uri=VOID.number_of_triples, domain=Dataset, range=Optional[int])

slots.URI_space = Slot(uri=VOID.URI_space, name="URI space", curie=VOID.curie('URI_space'),
                   model_uri=VOID.URI_space, domain=Dataset, range=Optional[Union[str, LiteralType]])