export type DatasetId = string;
export type LinksetId = string;
export type DatasetDescriptionId = string;
export type TechnicalFeatureId = string;


/**
 * A body of RDF data that one party publishes, maintains or gathers, treated as a single resource so that statements can be made about all of it.
 */
export interface Dataset {
    /** The IRI of the dataset, document or feature, written in full or as a CURIE. */
    id: string,
    /** The name of the dataset or document. */
    title?: string,
    /** A short account, in prose, of what the dataset or document holds. */
    description?: string,
    /** The IRI of a person, organisation or service mainly responsible for making the dataset or document. */
    creator?: string[],
    /** The IRI of a person, organisation or service that contributed to the dataset. */
    contributor?: string[],
    /** The IRI of the person, organisation or service that makes the dataset available. */
    publisher?: string,
    /** The IRI of a resource the dataset was derived from. */
    source?: string[],
    /** The date the dataset or document was made. */
    created?: date,
    /** The date the dataset was first published. */
    issued?: date,
    /** The date the dataset or document last changed. */
    modified?: date,
    /** The IRI of the licence the dataset is published under. */
    license?: string,
    /** The IRI of a topic the dataset is about, such as a DBpedia resource or a SKOS concept. */
    subject?: string[],
    /** The web page about the dataset itself. */
    homepage?: string,
    /** Another web page about the dataset, such as a download page or a catalogue entry. */
    page?: string[],
    /** A technical feature of the dataset, such as an RDF syntax it is served in, named by the feature's IRI. */
    feature?: TechnicalFeatureId[],
    /** The address of a SPARQL endpoint whose default graph holds the dataset. */
    sparqlEndpoint?: string[],
    /** The address of a file to download that holds the dataset, or a part of it, as RDF. */
    dataDump?: string[],
    /** An address to which the URL-encoded IRI of an entity is appended, so that a GET on the result returns an RDF description of the entity. */
    uriLookupEndpoint?: string[],
    /** The address of an OpenSearch description document for a text search over the dataset. */
    openSearchDescription?: string[],
    /** The IRI of a central entity of the dataset, from which every other entity can be reached by following links in a few steps. */
    rootResource?: string[],
    /** The IRI of an entity typical of the dataset, for a reader to look up. */
    exampleResource?: string[],
    /** The string every entity IRI in the dataset starts with, such as http://example.org/resource/. */
    uriSpace?: string,
    /** A regular expression, in the syntax SPARQL uses, that matches the IRI of every entity in the dataset. */
    uriRegexPattern?: string,
    /** The namespace IRI of a vocabulary the dataset uses, as a term's IRI reads without its local name and without a final hash, such as http://xmlns.com/foaf/0.1/. */
    vocabulary?: string[],
    /** A dataset that is part of this one, named by its IRI. */
    subset?: DatasetId[],
    /** A part of the dataset that describes the instances of one class. */
    classPartition?: ClassBasedPartition[],
    /** A part of the dataset that holds the triples of one property. */
    propertyPartition?: PropertyBasedPartition[],
    /** How many triples the dataset holds; for a linkset, how many links. */
    triples?: number,
    /** How many entities, resources with an IRI, the dataset describes. */
    entities?: number,
    /** How many distinct classes the dataset's rdf:type triples name. */
    classes?: number,
    /** How many distinct properties the dataset's triples use as predicates. */
    properties?: number,
    /** How many distinct IRIs and blank nodes the dataset's triples have as subjects. */
    distinctSubjects?: number,
    /** How many distinct IRIs, blank nodes and literals the dataset's triples have as objects. */
    distinctObjects?: number,
    /** How many RDF documents the dataset is published as, for a dataset spread over many documents whose triples are hard to count. */
    documents?: number,
}


/**
 * A dataset of RDF links between two datasets: triples whose subjects are described in one of them and whose objects are described in the other.
 */
export interface Linkset extends Dataset {
    /** One of the two datasets a linkset links, named by its IRI. */
    target?: DatasetId[],
    /** The dataset that describes the subjects of a linkset's links, named by its IRI. */
    subjectsTarget?: DatasetId,
    /** The dataset that describes the objects of a linkset's links, named by its IRI. */
    objectsTarget?: DatasetId,
    /** The property every link of a linkset has as its predicate, such as owl:sameAs. */
    linkPredicate?: string,
}


/**
 * A web document, such as a void.ttl file published beside a dataset, that describes one or more datasets.
 */
export interface DatasetDescription {
    /** The IRI of the dataset, document or feature, written in full or as a CURIE. */
    id: string,
    /** The name of the dataset or document. */
    title?: string,
    /** A short account, in prose, of what the dataset or document holds. */
    description?: string,
    /** The IRI of a person, organisation or service mainly responsible for making the dataset or document. */
    creator?: string[],
    /** The date the dataset or document was made. */
    created?: date,
    /** The date the dataset or document last changed. */
    modified?: date,
    /** The dataset a description is about, when it describes one. */
    primaryTopic?: DatasetId,
    /** A dataset a description is about, when it describes several of equal weight. */
    topic?: DatasetId[],
    /** The dataset whose data this document is part of, named by its IRI. */
    inDataset?: DatasetId,
}


/**
 * A technical property of how a dataset is served, such as an RDF syntax it can be read in or an HTTP feature its server supports.
 */
export interface TechnicalFeature {
    /** The IRI of the dataset, document or feature, written in full or as a CURIE. */
    id: string,
    /** A short name for the feature. */
    label?: string,
    /** A sentence or two about the feature. */
    comment?: string,
    /** The address of a page with more about the feature. */
    seeAlso?: string[],
}


/**
 * The part of a dataset that describes the instances of one class, given within the dataset it is part of, usually to state counts.
 */
export interface ClassBasedPartition {
    /** The class whose instances a class partition describes, named by its IRI, such as foaf:Person. */
    class: string,
    /** How many triples the dataset holds; for a linkset, how many links. */
    triples?: number,
    /** How many entities, resources with an IRI, the dataset describes. */
    entities?: number,
    /** How many distinct classes the dataset's rdf:type triples name. */
    classes?: number,
    /** How many distinct properties the dataset's triples use as predicates. */
    properties?: number,
    /** How many distinct IRIs and blank nodes the dataset's triples have as subjects. */
    distinctSubjects?: number,
    /** How many distinct IRIs, blank nodes and literals the dataset's triples have as objects. */
    distinctObjects?: number,
    /** How many RDF documents the dataset is published as, for a dataset spread over many documents whose triples are hard to count. */
    documents?: number,
    /** A part of the dataset that holds the triples of one property. */
    propertyPartition?: PropertyBasedPartition[],
}


/**
 * The part of a dataset that holds the triples of one property, given within the dataset it is part of, usually to state counts.
 */
export interface PropertyBasedPartition {
    /** The property whose triples a property partition holds, named by its IRI, such as foaf:name. */
    property: string,
    /** How many triples the dataset holds; for a linkset, how many links. */
    triples?: number,
    /** How many entities, resources with an IRI, the dataset describes. */
    entities?: number,
    /** How many distinct classes the dataset's rdf:type triples name. */
    classes?: number,
    /** How many distinct properties the dataset's triples use as predicates. */
    properties?: number,
    /** How many distinct IRIs and blank nodes the dataset's triples have as subjects. */
    distinctSubjects?: number,
    /** How many distinct IRIs, blank nodes and literals the dataset's triples have as objects. */
    distinctObjects?: number,
    /** How many RDF documents the dataset is published as, for a dataset spread over many documents whose triples are hard to count. */
    documents?: number,
}



