export type DatasetId = string;
export type LinksetId = string;
export type DatasetDescriptionId = string;
export type TechnicalFeatureId = string;


/**
 * RDF triples from one provider, gathered under an IRI so that a description can speak of them as a whole.
 */
export interface Dataset {
    /** The IRI of the dataset, document or feature, written in full or as a CURIE. */
    id: string,
    /** A human-readable name for the dataset or document. */
    title?: string,
    /** A few sentences of prose saying what the dataset or document contains. */
    description?: string,
    /** The IRI of the agent, human or not, that chiefly made the dataset or document. */
    creator?: string[],
    /** The IRI of an agent that added to the dataset without being its main maker. */
    contributor?: string[],
    /** The IRI of the agent that releases the dataset for others to use. */
    publisher?: string,
    /** The IRI of an earlier resource whose content the dataset draws on. */
    source?: string[],
    /** The date the dataset or document was made. */
    created?: date,
    /** The date the dataset was first published. */
    issued?: date,
    /** The date the dataset or document last changed. */
    modified?: date,
    /** The IRI of the licence that sets the terms for using the dataset. */
    license?: string,
    /** The IRI of a topic the dataset covers, such as a DBpedia resource or a SKOS concept. */
    subject?: string[],
    /** The web page about the dataset itself. */
    homepage?: string,
    /** Any further web page with information on the dataset, for instance its download page or its catalogue entry. */
    page?: string[],
    /** Something the dataset's server or files support, for instance an RDF syntax, named by its IRI. */
    feature?: TechnicalFeatureId[],
    /** A SPARQL service whose default graph holds the dataset, for running queries on it. */
    sparqlEndpoint?: string[],
    /** A downloadable RDF file holding all of the dataset or a share of it. */
    dataDump?: string[],
    /** A web address that, with an entity's percent-encoded IRI added to its end, answers an HTTP GET with RDF about that entity. */
    uriLookupEndpoint?: string[],
    /** An OpenSearch file telling a client how to run keyword searches over the dataset. */
    openSearchDescription?: string[],
    /** The IRI of a starting point for crawling the dataset: a resource from which links lead, within a few hops, to all the others. */
    rootResource?: string[],
    /** The IRI of an entity typical of the dataset, for a reader to look up. */
    exampleResource?: string[],
    /** The string every entity IRI in the dataset starts with, such as http://example.org/resource/. */
    uriSpace?: string,
    /** A regular expression in SPARQL's syntax that each entity IRI of the dataset satisfies. */
    uriRegexPattern?: string,
    /** The namespace IRI of a vocabulary the dataset uses, as a term's IRI reads without its local name and without a final hash, such as http://xmlns.com/foaf/0.1/. */
    vocabulary?: string[],
    /** Another dataset contained in this one, named by its IRI. */
    subset?: DatasetId[],
    /** The dataset's slice for one class, given inside it. */
    classPartition?: ClassBasedPartition[],
    /** The dataset's slice for one property, given inside it. */
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
    /** How many RDF documents together carry the dataset, for example RDFa web pages. */
    documents?: number,
}


/**
 * A dataset of triples that join two datasets: each triple's subject belongs to one of them and its object to the other.
 */
export interface Linkset extends Dataset {
    /** Either dataset a linkset joins, named by its IRI. */
    target?: DatasetId[],
    /** The dataset at the subject end of every link in a linkset, named by its IRI. */
    subjectsTarget?: DatasetId,
    /** The dataset at the object end of every link in a linkset, named by its IRI. */
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
    /** A human-readable name for the dataset or document. */
    title?: string,
    /** A few sentences of prose saying what the dataset or document contains. */
    description?: string,
    /** The IRI of the agent, human or not, that chiefly made the dataset or document. */
    creator?: string[],
    /** The date the dataset or document was made. */
    created?: date,
    /** The date the dataset or document last changed. */
    modified?: date,
    /** The dataset a description is about, when it describes one. */
    primaryTopic?: DatasetId,
    /** A dataset a description is about, when it describes several of equal weight. */
    topic?: DatasetId[],
    /** The dataset that this document's triples belong to, named by its IRI. */
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
    /** A web page that tells more about the feature. */
    seeAlso?: string[],
}


/**
 * The slice of a dataset about the members of one class, written inside that dataset, most often to give counts for it.
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
    /** How many RDF documents together carry the dataset, for example RDFa web pages. */
    documents?: number,
    /** The dataset's slice for one property, given inside it. */
    propertyPartition?: PropertyBasedPartition[],
}


/**
 * The slice of a dataset made of the triples whose predicate is one property, written inside that dataset, most often to give counts for it.
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
    /** How many RDF documents together carry the dataset, for example RDFa web pages. */
    documents?: number,
}



