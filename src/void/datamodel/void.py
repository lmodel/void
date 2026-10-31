# Auto generated from void.yaml by pythongen.py version: 0.0.1
# Schema: void
#
# id: https://w3id.org/lmodel/void
# description: A LinkML rendering of the Vocabulary of Interlinked Datasets (VoID), the RDF vocabulary for describing datasets of linked data and the links between them, as the W3C Interest Group Note of 3 March 2011 explains it. Every VoID class and property keeps its VoID IRI, and the Dublin Core, FOAF and RDF Schema terms the Note uses in a description keep theirs.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDate

metamodel_version = "1.12.0"
version = "2011-03-03"

# Namespaces
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SD = CurieNamespace('sd', 'http://www.w3.org/ns/sparql-service-description#')
VOID = CurieNamespace('void', 'http://rdfs.org/ns/void#')
VOID_LINKML = CurieNamespace('void_linkml', 'https://w3id.org/lmodel/void/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = VOID_LINKML


# Types

# Class references
class DatasetId(URIorCURIE):
    pass


class LinksetId(DatasetId):
    pass


class DatasetDescriptionId(URIorCURIE):
    pass


class TechnicalFeatureId(URIorCURIE):
    pass


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    RDF triples from one provider, gathered under an IRI so that a description can speak of them as a whole.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOID["Dataset"]
    class_class_curie: ClassVar[str] = "void:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = VOID_LINKML.Dataset

    id: Union[str, DatasetId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    creator: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    contributor: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    publisher: Optional[Union[str, URI]] = None
    source: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    created: Optional[Union[str, XSDDate]] = None
    issued: Optional[Union[str, XSDDate]] = None
    modified: Optional[Union[str, XSDDate]] = None
    license: Optional[Union[str, URI]] = None
    subject: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    homepage: Optional[Union[str, URI]] = None
    page: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    feature: Optional[Union[Union[str, TechnicalFeatureId], list[Union[str, TechnicalFeatureId]]]] = empty_list()
    sparqlEndpoint: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    dataDump: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    uriLookupEndpoint: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    openSearchDescription: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    rootResource: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    exampleResource: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    uriSpace: Optional[str] = None
    uriRegexPattern: Optional[str] = None
    vocabulary: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    subset: Optional[Union[Union[str, DatasetId], list[Union[str, DatasetId]]]] = empty_list()
    classPartition: Optional[Union[Union[dict, "ClassBasedPartition"], list[Union[dict, "ClassBasedPartition"]]]] = empty_list()
    propertyPartition: Optional[Union[Union[dict, "PropertyBasedPartition"], list[Union[dict, "PropertyBasedPartition"]]]] = empty_list()
    triples: Optional[int] = None
    entities: Optional[int] = None
    classes: Optional[int] = None
    properties: Optional[int] = None
    distinctSubjects: Optional[int] = None
    distinctObjects: Optional[int] = None
    documents: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.creator, list):
            self.creator = [self.creator] if self.creator is not None else []
        self.creator = [v if isinstance(v, URI) else URI(v) for v in self.creator]

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, URI) else URI(v) for v in self.contributor]

        if self.publisher is not None and not isinstance(self.publisher, URI):
            self.publisher = URI(self.publisher)

        if not isinstance(self.source, list):
            self.source = [self.source] if self.source is not None else []
        self.source = [v if isinstance(v, URI) else URI(v) for v in self.source]

        if self.created is not None and not isinstance(self.created, XSDDate):
            self.created = XSDDate(self.created)

        if self.issued is not None and not isinstance(self.issued, XSDDate):
            self.issued = XSDDate(self.issued)

        if self.modified is not None and not isinstance(self.modified, XSDDate):
            self.modified = XSDDate(self.modified)

        if self.license is not None and not isinstance(self.license, URI):
            self.license = URI(self.license)

        if not isinstance(self.subject, list):
            self.subject = [self.subject] if self.subject is not None else []
        self.subject = [v if isinstance(v, URI) else URI(v) for v in self.subject]

        if self.homepage is not None and not isinstance(self.homepage, URI):
            self.homepage = URI(self.homepage)

        if not isinstance(self.page, list):
            self.page = [self.page] if self.page is not None else []
        self.page = [v if isinstance(v, URI) else URI(v) for v in self.page]

        if not isinstance(self.feature, list):
            self.feature = [self.feature] if self.feature is not None else []
        self.feature = [v if isinstance(v, TechnicalFeatureId) else TechnicalFeatureId(v) for v in self.feature]

        if not isinstance(self.sparqlEndpoint, list):
            self.sparqlEndpoint = [self.sparqlEndpoint] if self.sparqlEndpoint is not None else []
        self.sparqlEndpoint = [v if isinstance(v, URI) else URI(v) for v in self.sparqlEndpoint]

        if not isinstance(self.dataDump, list):
            self.dataDump = [self.dataDump] if self.dataDump is not None else []
        self.dataDump = [v if isinstance(v, URI) else URI(v) for v in self.dataDump]

        if not isinstance(self.uriLookupEndpoint, list):
            self.uriLookupEndpoint = [self.uriLookupEndpoint] if self.uriLookupEndpoint is not None else []
        self.uriLookupEndpoint = [v if isinstance(v, URI) else URI(v) for v in self.uriLookupEndpoint]

        if not isinstance(self.openSearchDescription, list):
            self.openSearchDescription = [self.openSearchDescription] if self.openSearchDescription is not None else []
        self.openSearchDescription = [v if isinstance(v, URI) else URI(v) for v in self.openSearchDescription]

        if not isinstance(self.rootResource, list):
            self.rootResource = [self.rootResource] if self.rootResource is not None else []
        self.rootResource = [v if isinstance(v, URI) else URI(v) for v in self.rootResource]

        if not isinstance(self.exampleResource, list):
            self.exampleResource = [self.exampleResource] if self.exampleResource is not None else []
        self.exampleResource = [v if isinstance(v, URI) else URI(v) for v in self.exampleResource]

        if self.uriSpace is not None and not isinstance(self.uriSpace, str):
            self.uriSpace = str(self.uriSpace)

        if self.uriRegexPattern is not None and not isinstance(self.uriRegexPattern, str):
            self.uriRegexPattern = str(self.uriRegexPattern)

        if not isinstance(self.vocabulary, list):
            self.vocabulary = [self.vocabulary] if self.vocabulary is not None else []
        self.vocabulary = [v if isinstance(v, URI) else URI(v) for v in self.vocabulary]

        if not isinstance(self.subset, list):
            self.subset = [self.subset] if self.subset is not None else []
        self.subset = [v if isinstance(v, DatasetId) else DatasetId(v) for v in self.subset]

        self._normalize_inlined_as_list(slot_name="classPartition", slot_type=ClassBasedPartition, key_name="class", keyed=False)

        self._normalize_inlined_as_list(slot_name="propertyPartition", slot_type=PropertyBasedPartition, key_name="property", keyed=False)

        if self.triples is not None and not isinstance(self.triples, int):
            self.triples = int(self.triples)

        if self.entities is not None and not isinstance(self.entities, int):
            self.entities = int(self.entities)

        if self.classes is not None and not isinstance(self.classes, int):
            self.classes = int(self.classes)

        if self.properties is not None and not isinstance(self.properties, int):
            self.properties = int(self.properties)

        if self.distinctSubjects is not None and not isinstance(self.distinctSubjects, int):
            self.distinctSubjects = int(self.distinctSubjects)

        if self.distinctObjects is not None and not isinstance(self.distinctObjects, int):
            self.distinctObjects = int(self.distinctObjects)

        if self.documents is not None and not isinstance(self.documents, int):
            self.documents = int(self.documents)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Linkset(Dataset):
    """
    A dataset of triples that join two datasets: each triple's subject belongs to one of them and its object to the
    other.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOID["Linkset"]
    class_class_curie: ClassVar[str] = "void:Linkset"
    class_name: ClassVar[str] = "Linkset"
    class_model_uri: ClassVar[URIRef] = VOID_LINKML.Linkset

    id: Union[str, LinksetId] = None
    target: Optional[Union[Union[str, DatasetId], list[Union[str, DatasetId]]]] = empty_list()
    subjectsTarget: Optional[Union[str, DatasetId]] = None
    objectsTarget: Optional[Union[str, DatasetId]] = None
    linkPredicate: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LinksetId):
            self.id = LinksetId(self.id)

        if not isinstance(self.target, list):
            self.target = [self.target] if self.target is not None else []
        self.target = [v if isinstance(v, DatasetId) else DatasetId(v) for v in self.target]

        if self.subjectsTarget is not None and not isinstance(self.subjectsTarget, DatasetId):
            self.subjectsTarget = DatasetId(self.subjectsTarget)

        if self.objectsTarget is not None and not isinstance(self.objectsTarget, DatasetId):
            self.objectsTarget = DatasetId(self.objectsTarget)

        if self.linkPredicate is not None and not isinstance(self.linkPredicate, URIorCURIE):
            self.linkPredicate = URIorCURIE(self.linkPredicate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DatasetDescription(YAMLRoot):
    """
    A web document, such as a void.ttl file published beside a dataset, that describes one or more datasets.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOID["DatasetDescription"]
    class_class_curie: ClassVar[str] = "void:DatasetDescription"
    class_name: ClassVar[str] = "DatasetDescription"
    class_model_uri: ClassVar[URIRef] = VOID_LINKML.DatasetDescription

    id: Union[str, DatasetDescriptionId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    creator: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    created: Optional[Union[str, XSDDate]] = None
    modified: Optional[Union[str, XSDDate]] = None
    primaryTopic: Optional[Union[str, DatasetId]] = None
    topic: Optional[Union[Union[str, DatasetId], list[Union[str, DatasetId]]]] = empty_list()
    inDataset: Optional[Union[str, DatasetId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetDescriptionId):
            self.id = DatasetDescriptionId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.creator, list):
            self.creator = [self.creator] if self.creator is not None else []
        self.creator = [v if isinstance(v, URI) else URI(v) for v in self.creator]

        if self.created is not None and not isinstance(self.created, XSDDate):
            self.created = XSDDate(self.created)

        if self.modified is not None and not isinstance(self.modified, XSDDate):
            self.modified = XSDDate(self.modified)

        if self.primaryTopic is not None and not isinstance(self.primaryTopic, DatasetId):
            self.primaryTopic = DatasetId(self.primaryTopic)

        if not isinstance(self.topic, list):
            self.topic = [self.topic] if self.topic is not None else []
        self.topic = [v if isinstance(v, DatasetId) else DatasetId(v) for v in self.topic]

        if self.inDataset is not None and not isinstance(self.inDataset, DatasetId):
            self.inDataset = DatasetId(self.inDataset)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TechnicalFeature(YAMLRoot):
    """
    A technical property of how a dataset is served, such as an RDF syntax it can be read in or an HTTP feature its
    server supports.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOID["TechnicalFeature"]
    class_class_curie: ClassVar[str] = "void:TechnicalFeature"
    class_name: ClassVar[str] = "TechnicalFeature"
    class_model_uri: ClassVar[URIRef] = VOID_LINKML.TechnicalFeature

    id: Union[str, TechnicalFeatureId] = None
    label: Optional[str] = None
    comment: Optional[str] = None
    seeAlso: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TechnicalFeatureId):
            self.id = TechnicalFeatureId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if not isinstance(self.seeAlso, list):
            self.seeAlso = [self.seeAlso] if self.seeAlso is not None else []
        self.seeAlso = [v if isinstance(v, URI) else URI(v) for v in self.seeAlso]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClassBasedPartition(YAMLRoot):
    """
    The slice of a dataset about the members of one class, written inside that dataset, most often to give counts for
    it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOID_LINKML["ClassBasedPartition"]
    class_class_curie: ClassVar[str] = "void_linkml:ClassBasedPartition"
    class_name: ClassVar[str] = "ClassBasedPartition"
    class_model_uri: ClassVar[URIRef] = VOID_LINKML.ClassBasedPartition

    class_: Union[str, URIorCURIE] = None
    triples: Optional[int] = None
    entities: Optional[int] = None
    classes: Optional[int] = None
    properties: Optional[int] = None
    distinctSubjects: Optional[int] = None
    distinctObjects: Optional[int] = None
    documents: Optional[int] = None
    propertyPartition: Optional[Union[Union[dict, "PropertyBasedPartition"], list[Union[dict, "PropertyBasedPartition"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.class_):
            self.MissingRequiredField("class_")
        if not isinstance(self.class_, URIorCURIE):
            self.class_ = URIorCURIE(self.class_)

        if self.triples is not None and not isinstance(self.triples, int):
            self.triples = int(self.triples)

        if self.entities is not None and not isinstance(self.entities, int):
            self.entities = int(self.entities)

        if self.classes is not None and not isinstance(self.classes, int):
            self.classes = int(self.classes)

        if self.properties is not None and not isinstance(self.properties, int):
            self.properties = int(self.properties)

        if self.distinctSubjects is not None and not isinstance(self.distinctSubjects, int):
            self.distinctSubjects = int(self.distinctSubjects)

        if self.distinctObjects is not None and not isinstance(self.distinctObjects, int):
            self.distinctObjects = int(self.distinctObjects)

        if self.documents is not None and not isinstance(self.documents, int):
            self.documents = int(self.documents)

        self._normalize_inlined_as_list(slot_name="propertyPartition", slot_type=PropertyBasedPartition, key_name="property", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PropertyBasedPartition(YAMLRoot):
    """
    The slice of a dataset made of the triples whose predicate is one property, written inside that dataset, most
    often to give counts for it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOID_LINKML["PropertyBasedPartition"]
    class_class_curie: ClassVar[str] = "void_linkml:PropertyBasedPartition"
    class_name: ClassVar[str] = "PropertyBasedPartition"
    class_model_uri: ClassVar[URIRef] = VOID_LINKML.PropertyBasedPartition

    property: Union[str, URIorCURIE] = None
    triples: Optional[int] = None
    entities: Optional[int] = None
    classes: Optional[int] = None
    properties: Optional[int] = None
    distinctSubjects: Optional[int] = None
    distinctObjects: Optional[int] = None
    documents: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.property):
            self.MissingRequiredField("property")
        if not isinstance(self.property, URIorCURIE):
            self.property = URIorCURIE(self.property)

        if self.triples is not None and not isinstance(self.triples, int):
            self.triples = int(self.triples)

        if self.entities is not None and not isinstance(self.entities, int):
            self.entities = int(self.entities)

        if self.classes is not None and not isinstance(self.classes, int):
            self.classes = int(self.classes)

        if self.properties is not None and not isinstance(self.properties, int):
            self.properties = int(self.properties)

        if self.distinctSubjects is not None and not isinstance(self.distinctSubjects, int):
            self.distinctSubjects = int(self.distinctSubjects)

        if self.distinctObjects is not None and not isinstance(self.distinctObjects, int):
            self.distinctObjects = int(self.distinctObjects)

        if self.documents is not None and not isinstance(self.documents, int):
            self.documents = int(self.documents)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=VOID_LINKML.id, name="id", curie=VOID_LINKML.curie('id'),
                   model_uri=VOID_LINKML.id, domain=None, range=URIRef)

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=VOID_LINKML.title, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=VOID_LINKML.description, domain=None, range=Optional[str])

slots.creator = Slot(uri=DCTERMS.creator, name="creator", curie=DCTERMS.curie('creator'),
                   model_uri=VOID_LINKML.creator, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.contributor = Slot(uri=DCTERMS.contributor, name="contributor", curie=DCTERMS.curie('contributor'),
                   model_uri=VOID_LINKML.contributor, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.publisher = Slot(uri=DCTERMS.publisher, name="publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=VOID_LINKML.publisher, domain=None, range=Optional[Union[str, URI]])

slots.source = Slot(uri=DCTERMS.source, name="source", curie=DCTERMS.curie('source'),
                   model_uri=VOID_LINKML.source, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.created = Slot(uri=DCTERMS.created, name="created", curie=DCTERMS.curie('created'),
                   model_uri=VOID_LINKML.created, domain=None, range=Optional[Union[str, XSDDate]])

slots.issued = Slot(uri=DCTERMS.issued, name="issued", curie=DCTERMS.curie('issued'),
                   model_uri=VOID_LINKML.issued, domain=None, range=Optional[Union[str, XSDDate]])

slots.modified = Slot(uri=DCTERMS.modified, name="modified", curie=DCTERMS.curie('modified'),
                   model_uri=VOID_LINKML.modified, domain=None, range=Optional[Union[str, XSDDate]])

slots.license = Slot(uri=DCTERMS.license, name="license", curie=DCTERMS.curie('license'),
                   model_uri=VOID_LINKML.license, domain=None, range=Optional[Union[str, URI]])

slots.subject = Slot(uri=DCTERMS.subject, name="subject", curie=DCTERMS.curie('subject'),
                   model_uri=VOID_LINKML.subject, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.homepage = Slot(uri=FOAF.homepage, name="homepage", curie=FOAF.curie('homepage'),
                   model_uri=VOID_LINKML.homepage, domain=None, range=Optional[Union[str, URI]])

slots.page = Slot(uri=FOAF.page, name="page", curie=FOAF.curie('page'),
                   model_uri=VOID_LINKML.page, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.primaryTopic = Slot(uri=FOAF.primaryTopic, name="primaryTopic", curie=FOAF.curie('primaryTopic'),
                   model_uri=VOID_LINKML.primaryTopic, domain=None, range=Optional[Union[str, DatasetId]])

slots.topic = Slot(uri=FOAF.topic, name="topic", curie=FOAF.curie('topic'),
                   model_uri=VOID_LINKML.topic, domain=None, range=Optional[Union[Union[str, DatasetId], list[Union[str, DatasetId]]]])

slots.label = Slot(uri=RDFS.label, name="label", curie=RDFS.curie('label'),
                   model_uri=VOID_LINKML.label, domain=None, range=Optional[str])

slots.comment = Slot(uri=RDFS.comment, name="comment", curie=RDFS.curie('comment'),
                   model_uri=VOID_LINKML.comment, domain=None, range=Optional[str])

slots.seeAlso = Slot(uri=RDFS.seeAlso, name="seeAlso", curie=RDFS.curie('seeAlso'),
                   model_uri=VOID_LINKML.seeAlso, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.feature = Slot(uri=VOID.feature, name="feature", curie=VOID.curie('feature'),
                   model_uri=VOID_LINKML.feature, domain=None, range=Optional[Union[Union[str, TechnicalFeatureId], list[Union[str, TechnicalFeatureId]]]])

slots.sparqlEndpoint = Slot(uri=VOID.sparqlEndpoint, name="sparqlEndpoint", curie=VOID.curie('sparqlEndpoint'),
                   model_uri=VOID_LINKML.sparqlEndpoint, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.dataDump = Slot(uri=VOID.dataDump, name="dataDump", curie=VOID.curie('dataDump'),
                   model_uri=VOID_LINKML.dataDump, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.uriLookupEndpoint = Slot(uri=VOID.uriLookupEndpoint, name="uriLookupEndpoint", curie=VOID.curie('uriLookupEndpoint'),
                   model_uri=VOID_LINKML.uriLookupEndpoint, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.openSearchDescription = Slot(uri=VOID.openSearchDescription, name="openSearchDescription", curie=VOID.curie('openSearchDescription'),
                   model_uri=VOID_LINKML.openSearchDescription, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.rootResource = Slot(uri=VOID.rootResource, name="rootResource", curie=VOID.curie('rootResource'),
                   model_uri=VOID_LINKML.rootResource, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.exampleResource = Slot(uri=VOID.exampleResource, name="exampleResource", curie=VOID.curie('exampleResource'),
                   model_uri=VOID_LINKML.exampleResource, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.uriSpace = Slot(uri=VOID.uriSpace, name="uriSpace", curie=VOID.curie('uriSpace'),
                   model_uri=VOID_LINKML.uriSpace, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z][A-Za-z0-9+.-]*:[^\s]*$'))

slots.uriRegexPattern = Slot(uri=VOID.uriRegexPattern, name="uriRegexPattern", curie=VOID.curie('uriRegexPattern'),
                   model_uri=VOID_LINKML.uriRegexPattern, domain=None, range=Optional[str])

slots.vocabulary = Slot(uri=VOID.vocabulary, name="vocabulary", curie=VOID.curie('vocabulary'),
                   model_uri=VOID_LINKML.vocabulary, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]],
                   pattern=re.compile(r'[^#]$'))

slots.subset = Slot(uri=VOID.subset, name="subset", curie=VOID.curie('subset'),
                   model_uri=VOID_LINKML.subset, domain=None, range=Optional[Union[Union[str, DatasetId], list[Union[str, DatasetId]]]])

slots.classPartition = Slot(uri=VOID.classPartition, name="classPartition", curie=VOID.curie('classPartition'),
                   model_uri=VOID_LINKML.classPartition, domain=None, range=Optional[Union[Union[dict, ClassBasedPartition], list[Union[dict, ClassBasedPartition]]]])

slots.propertyPartition = Slot(uri=VOID.propertyPartition, name="propertyPartition", curie=VOID.curie('propertyPartition'),
                   model_uri=VOID_LINKML.propertyPartition, domain=None, range=Optional[Union[Union[dict, PropertyBasedPartition], list[Union[dict, PropertyBasedPartition]]]])

slots.class_ = Slot(uri=VOID['class'], name="class", curie=VOID.curie('class'),
                   model_uri=VOID_LINKML.class_, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.property = Slot(uri=VOID.property, name="property", curie=VOID.curie('property'),
                   model_uri=VOID_LINKML.property, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.triples = Slot(uri=VOID.triples, name="triples", curie=VOID.curie('triples'),
                   model_uri=VOID_LINKML.triples, domain=None, range=Optional[int])

slots.entities = Slot(uri=VOID.entities, name="entities", curie=VOID.curie('entities'),
                   model_uri=VOID_LINKML.entities, domain=None, range=Optional[int])

slots.classes = Slot(uri=VOID.classes, name="classes", curie=VOID.curie('classes'),
                   model_uri=VOID_LINKML.classes, domain=None, range=Optional[int])

slots.properties = Slot(uri=VOID.properties, name="properties", curie=VOID.curie('properties'),
                   model_uri=VOID_LINKML.properties, domain=None, range=Optional[int])

slots.distinctSubjects = Slot(uri=VOID.distinctSubjects, name="distinctSubjects", curie=VOID.curie('distinctSubjects'),
                   model_uri=VOID_LINKML.distinctSubjects, domain=None, range=Optional[int])

slots.distinctObjects = Slot(uri=VOID.distinctObjects, name="distinctObjects", curie=VOID.curie('distinctObjects'),
                   model_uri=VOID_LINKML.distinctObjects, domain=None, range=Optional[int])

slots.documents = Slot(uri=VOID.documents, name="documents", curie=VOID.curie('documents'),
                   model_uri=VOID_LINKML.documents, domain=None, range=Optional[int])

slots.target = Slot(uri=VOID.target, name="target", curie=VOID.curie('target'),
                   model_uri=VOID_LINKML.target, domain=None, range=Optional[Union[str, DatasetId]])

slots.subjectsTarget = Slot(uri=VOID.subjectsTarget, name="subjectsTarget", curie=VOID.curie('subjectsTarget'),
                   model_uri=VOID_LINKML.subjectsTarget, domain=None, range=Optional[Union[str, DatasetId]])

slots.objectsTarget = Slot(uri=VOID.objectsTarget, name="objectsTarget", curie=VOID.curie('objectsTarget'),
                   model_uri=VOID_LINKML.objectsTarget, domain=None, range=Optional[Union[str, DatasetId]])

slots.linkPredicate = Slot(uri=VOID.linkPredicate, name="linkPredicate", curie=VOID.curie('linkPredicate'),
                   model_uri=VOID_LINKML.linkPredicate, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.inDataset = Slot(uri=VOID.inDataset, name="inDataset", curie=VOID.curie('inDataset'),
                   model_uri=VOID_LINKML.inDataset, domain=None, range=Optional[Union[str, DatasetId]])

slots.Linkset_target = Slot(uri=VOID.target, name="Linkset_target", curie=VOID.curie('target'),
                   model_uri=VOID_LINKML.Linkset_target, domain=Linkset, range=Optional[Union[Union[str, DatasetId], list[Union[str, DatasetId]]]])

slots.ClassBasedPartition_class = Slot(uri=VOID['class'], name="ClassBasedPartition_class", curie=VOID.curie('class'),
                   model_uri=VOID_LINKML.ClassBasedPartition_class, domain=ClassBasedPartition, range=Union[str, URIorCURIE])

slots.PropertyBasedPartition_property = Slot(uri=VOID.property, name="PropertyBasedPartition_property", curie=VOID.curie('property'),
                   model_uri=VOID_LINKML.PropertyBasedPartition_property, domain=PropertyBasedPartition, range=Union[str, URIorCURIE])
