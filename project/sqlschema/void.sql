-- # Class: Dataset Description: A body of RDF data that one party publishes, maintains or gathers, treated as a single resource so that statements can be made about all of it.
--     * Slot: id Description: The IRI of the dataset, document or feature, written in full or as a CURIE.
--     * Slot: title Description: The name of the dataset or document.
--     * Slot: description Description: A short account, in prose, of what the dataset or document holds.
--     * Slot: publisher Description: The IRI of the person, organisation or service that makes the dataset available.
--     * Slot: created Description: The date the dataset or document was made.
--     * Slot: issued Description: The date the dataset was first published.
--     * Slot: modified Description: The date the dataset or document last changed.
--     * Slot: license Description: The IRI of the licence the dataset is published under.
--     * Slot: homepage Description: The web page about the dataset itself.
--     * Slot: uriSpace Description: The string every entity IRI in the dataset starts with, such as http://example.org/resource/.
--     * Slot: uriRegexPattern Description: A regular expression, in the syntax SPARQL uses, that matches the IRI of every entity in the dataset.
--     * Slot: triples Description: How many triples the dataset holds; for a linkset, how many links.
--     * Slot: entities Description: How many entities, resources with an IRI, the dataset describes.
--     * Slot: classes Description: How many distinct classes the dataset's rdf:type triples name.
--     * Slot: properties Description: How many distinct properties the dataset's triples use as predicates.
--     * Slot: distinctSubjects Description: How many distinct IRIs and blank nodes the dataset's triples have as subjects.
--     * Slot: distinctObjects Description: How many distinct IRIs, blank nodes and literals the dataset's triples have as objects.
--     * Slot: documents Description: How many RDF documents the dataset is published as, for a dataset spread over many documents whose triples are hard to count.
-- # Class: Linkset Description: A dataset of RDF links between two datasets: triples whose subjects are described in one of them and whose objects are described in the other.
--     * Slot: subjectsTarget Description: The dataset that describes the subjects of a linkset's links, named by its IRI.
--     * Slot: objectsTarget Description: The dataset that describes the objects of a linkset's links, named by its IRI.
--     * Slot: linkPredicate Description: The property every link of a linkset has as its predicate, such as owl:sameAs.
--     * Slot: id Description: The IRI of the dataset, document or feature, written in full or as a CURIE.
--     * Slot: title Description: The name of the dataset or document.
--     * Slot: description Description: A short account, in prose, of what the dataset or document holds.
--     * Slot: publisher Description: The IRI of the person, organisation or service that makes the dataset available.
--     * Slot: created Description: The date the dataset or document was made.
--     * Slot: issued Description: The date the dataset was first published.
--     * Slot: modified Description: The date the dataset or document last changed.
--     * Slot: license Description: The IRI of the licence the dataset is published under.
--     * Slot: homepage Description: The web page about the dataset itself.
--     * Slot: uriSpace Description: The string every entity IRI in the dataset starts with, such as http://example.org/resource/.
--     * Slot: uriRegexPattern Description: A regular expression, in the syntax SPARQL uses, that matches the IRI of every entity in the dataset.
--     * Slot: triples Description: How many triples the dataset holds; for a linkset, how many links.
--     * Slot: entities Description: How many entities, resources with an IRI, the dataset describes.
--     * Slot: classes Description: How many distinct classes the dataset's rdf:type triples name.
--     * Slot: properties Description: How many distinct properties the dataset's triples use as predicates.
--     * Slot: distinctSubjects Description: How many distinct IRIs and blank nodes the dataset's triples have as subjects.
--     * Slot: distinctObjects Description: How many distinct IRIs, blank nodes and literals the dataset's triples have as objects.
--     * Slot: documents Description: How many RDF documents the dataset is published as, for a dataset spread over many documents whose triples are hard to count.
-- # Class: DatasetDescription Description: A web document, such as a void.ttl file published beside a dataset, that describes one or more datasets.
--     * Slot: id Description: The IRI of the dataset, document or feature, written in full or as a CURIE.
--     * Slot: title Description: The name of the dataset or document.
--     * Slot: description Description: A short account, in prose, of what the dataset or document holds.
--     * Slot: created Description: The date the dataset or document was made.
--     * Slot: modified Description: The date the dataset or document last changed.
--     * Slot: primaryTopic Description: The dataset a description is about, when it describes one.
--     * Slot: inDataset Description: The dataset whose data this document is part of, named by its IRI.
-- # Class: TechnicalFeature Description: A technical property of how a dataset is served, such as an RDF syntax it can be read in or an HTTP feature its server supports.
--     * Slot: id Description: The IRI of the dataset, document or feature, written in full or as a CURIE.
--     * Slot: label Description: A short name for the feature.
--     * Slot: comment Description: A sentence or two about the feature.
-- # Class: ClassBasedPartition Description: The part of a dataset that describes the instances of one class, given within the dataset it is part of, usually to state counts.
--     * Slot: id
--     * Slot: class Description: The class whose instances a class partition describes, named by its IRI, such as foaf:Person.
--     * Slot: triples Description: How many triples the dataset holds; for a linkset, how many links.
--     * Slot: entities Description: How many entities, resources with an IRI, the dataset describes.
--     * Slot: classes Description: How many distinct classes the dataset's rdf:type triples name.
--     * Slot: properties Description: How many distinct properties the dataset's triples use as predicates.
--     * Slot: distinctSubjects Description: How many distinct IRIs and blank nodes the dataset's triples have as subjects.
--     * Slot: distinctObjects Description: How many distinct IRIs, blank nodes and literals the dataset's triples have as objects.
--     * Slot: documents Description: How many RDF documents the dataset is published as, for a dataset spread over many documents whose triples are hard to count.
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: Linkset_id Description: Autocreated FK slot
-- # Class: PropertyBasedPartition Description: The part of a dataset that holds the triples of one property, given within the dataset it is part of, usually to state counts.
--     * Slot: id
--     * Slot: property Description: The property whose triples a property partition holds, named by its IRI, such as foaf:name.
--     * Slot: triples Description: How many triples the dataset holds; for a linkset, how many links.
--     * Slot: entities Description: How many entities, resources with an IRI, the dataset describes.
--     * Slot: classes Description: How many distinct classes the dataset's rdf:type triples name.
--     * Slot: properties Description: How many distinct properties the dataset's triples use as predicates.
--     * Slot: distinctSubjects Description: How many distinct IRIs and blank nodes the dataset's triples have as subjects.
--     * Slot: distinctObjects Description: How many distinct IRIs, blank nodes and literals the dataset's triples have as objects.
--     * Slot: documents Description: How many RDF documents the dataset is published as, for a dataset spread over many documents whose triples are hard to count.
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: ClassBasedPartition_id Description: Autocreated FK slot
-- # Class: Dataset_creator
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: creator Description: The IRI of a person, organisation or service mainly responsible for making the dataset or document.
-- # Class: Dataset_contributor
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: contributor Description: The IRI of a person, organisation or service that contributed to the dataset.
-- # Class: Dataset_source
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: source Description: The IRI of a resource the dataset was derived from.
-- # Class: Dataset_subject
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: subject Description: The IRI of a topic the dataset is about, such as a DBpedia resource or a SKOS concept.
-- # Class: Dataset_page
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: page Description: Another web page about the dataset, such as a download page or a catalogue entry.
-- # Class: Dataset_feature
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: feature_id Description: A technical feature of the dataset, such as an RDF syntax it is served in, named by the feature's IRI.
-- # Class: Dataset_sparqlEndpoint
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: sparqlEndpoint Description: The address of a SPARQL endpoint whose default graph holds the dataset.
-- # Class: Dataset_dataDump
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: dataDump Description: The address of a file to download that holds the dataset, or a part of it, as RDF.
-- # Class: Dataset_uriLookupEndpoint
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: uriLookupEndpoint Description: An address to which the URL-encoded IRI of an entity is appended, so that a GET on the result returns an RDF description of the entity.
-- # Class: Dataset_openSearchDescription
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: openSearchDescription Description: The address of an OpenSearch description document for a text search over the dataset.
-- # Class: Dataset_rootResource
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: rootResource Description: The IRI of a central entity of the dataset, from which every other entity can be reached by following links in a few steps.
-- # Class: Dataset_exampleResource
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: exampleResource Description: The IRI of an entity typical of the dataset, for a reader to look up.
-- # Class: Dataset_vocabulary
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: vocabulary Description: The namespace IRI of a vocabulary the dataset uses, as a term's IRI reads without its local name and without a final hash, such as http://xmlns.com/foaf/0.1/.
-- # Class: Dataset_subset
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: subset_id Description: A dataset that is part of this one, named by its IRI.
-- # Class: Linkset_target
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: target_id Description: One of the two datasets a linkset links, named by its IRI.
-- # Class: Linkset_creator
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: creator Description: The IRI of a person, organisation or service mainly responsible for making the dataset or document.
-- # Class: Linkset_contributor
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: contributor Description: The IRI of a person, organisation or service that contributed to the dataset.
-- # Class: Linkset_source
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: source Description: The IRI of a resource the dataset was derived from.
-- # Class: Linkset_subject
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: subject Description: The IRI of a topic the dataset is about, such as a DBpedia resource or a SKOS concept.
-- # Class: Linkset_page
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: page Description: Another web page about the dataset, such as a download page or a catalogue entry.
-- # Class: Linkset_feature
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: feature_id Description: A technical feature of the dataset, such as an RDF syntax it is served in, named by the feature's IRI.
-- # Class: Linkset_sparqlEndpoint
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: sparqlEndpoint Description: The address of a SPARQL endpoint whose default graph holds the dataset.
-- # Class: Linkset_dataDump
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: dataDump Description: The address of a file to download that holds the dataset, or a part of it, as RDF.
-- # Class: Linkset_uriLookupEndpoint
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: uriLookupEndpoint Description: An address to which the URL-encoded IRI of an entity is appended, so that a GET on the result returns an RDF description of the entity.
-- # Class: Linkset_openSearchDescription
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: openSearchDescription Description: The address of an OpenSearch description document for a text search over the dataset.
-- # Class: Linkset_rootResource
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: rootResource Description: The IRI of a central entity of the dataset, from which every other entity can be reached by following links in a few steps.
-- # Class: Linkset_exampleResource
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: exampleResource Description: The IRI of an entity typical of the dataset, for a reader to look up.
-- # Class: Linkset_vocabulary
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: vocabulary Description: The namespace IRI of a vocabulary the dataset uses, as a term's IRI reads without its local name and without a final hash, such as http://xmlns.com/foaf/0.1/.
-- # Class: Linkset_subset
--     * Slot: Linkset_id Description: Autocreated FK slot
--     * Slot: subset_id Description: A dataset that is part of this one, named by its IRI.
-- # Class: DatasetDescription_creator
--     * Slot: DatasetDescription_id Description: Autocreated FK slot
--     * Slot: creator Description: The IRI of a person, organisation or service mainly responsible for making the dataset or document.
-- # Class: DatasetDescription_topic
--     * Slot: DatasetDescription_id Description: Autocreated FK slot
--     * Slot: topic_id Description: A dataset a description is about, when it describes several of equal weight.
-- # Class: TechnicalFeature_seeAlso
--     * Slot: TechnicalFeature_id Description: Autocreated FK slot
--     * Slot: seeAlso Description: The address of a page with more about the feature.

CREATE TABLE "Dataset" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	publisher TEXT,
	created DATE,
	issued DATE,
	modified DATE,
	license TEXT,
	homepage TEXT,
	"uriSpace" TEXT,
	"uriRegexPattern" TEXT,
	triples INTEGER,
	entities INTEGER,
	classes INTEGER,
	properties INTEGER,
	"distinctSubjects" INTEGER,
	"distinctObjects" INTEGER,
	documents INTEGER,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Dataset_id" ON "Dataset" (id);

CREATE TABLE "TechnicalFeature" (
	id TEXT NOT NULL,
	label TEXT,
	comment TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_TechnicalFeature_id" ON "TechnicalFeature" (id);

CREATE TABLE "Linkset" (
	"subjectsTarget" TEXT,
	"objectsTarget" TEXT,
	"linkPredicate" TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	publisher TEXT,
	created DATE,
	issued DATE,
	modified DATE,
	license TEXT,
	homepage TEXT,
	"uriSpace" TEXT,
	"uriRegexPattern" TEXT,
	triples INTEGER,
	entities INTEGER,
	classes INTEGER,
	properties INTEGER,
	"distinctSubjects" INTEGER,
	"distinctObjects" INTEGER,
	documents INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("subjectsTarget") REFERENCES "Dataset" (id),
	FOREIGN KEY("objectsTarget") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Linkset_id" ON "Linkset" (id);

CREATE TABLE "DatasetDescription" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	created DATE,
	modified DATE,
	"primaryTopic" TEXT,
	"inDataset" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("primaryTopic") REFERENCES "Dataset" (id),
	FOREIGN KEY("inDataset") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_DatasetDescription_id" ON "DatasetDescription" (id);

CREATE TABLE "Dataset_creator" (
	"Dataset_id" TEXT,
	creator TEXT,
	PRIMARY KEY ("Dataset_id", creator),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_creator_Dataset_id" ON "Dataset_creator" ("Dataset_id");
CREATE INDEX "ix_Dataset_creator_creator" ON "Dataset_creator" (creator);

CREATE TABLE "Dataset_contributor" (
	"Dataset_id" TEXT,
	contributor TEXT,
	PRIMARY KEY ("Dataset_id", contributor),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_contributor_Dataset_id" ON "Dataset_contributor" ("Dataset_id");
CREATE INDEX "ix_Dataset_contributor_contributor" ON "Dataset_contributor" (contributor);

CREATE TABLE "Dataset_source" (
	"Dataset_id" TEXT,
	source TEXT,
	PRIMARY KEY ("Dataset_id", source),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_source_source" ON "Dataset_source" (source);
CREATE INDEX "ix_Dataset_source_Dataset_id" ON "Dataset_source" ("Dataset_id");

CREATE TABLE "Dataset_subject" (
	"Dataset_id" TEXT,
	subject TEXT,
	PRIMARY KEY ("Dataset_id", subject),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_subject_subject" ON "Dataset_subject" (subject);
CREATE INDEX "ix_Dataset_subject_Dataset_id" ON "Dataset_subject" ("Dataset_id");

CREATE TABLE "Dataset_page" (
	"Dataset_id" TEXT,
	page TEXT,
	PRIMARY KEY ("Dataset_id", page),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_page_page" ON "Dataset_page" (page);
CREATE INDEX "ix_Dataset_page_Dataset_id" ON "Dataset_page" ("Dataset_id");

CREATE TABLE "Dataset_feature" (
	"Dataset_id" TEXT,
	feature_id TEXT,
	PRIMARY KEY ("Dataset_id", feature_id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(feature_id) REFERENCES "TechnicalFeature" (id)
);
CREATE INDEX "ix_Dataset_feature_Dataset_id" ON "Dataset_feature" ("Dataset_id");
CREATE INDEX "ix_Dataset_feature_feature_id" ON "Dataset_feature" (feature_id);

CREATE TABLE "Dataset_sparqlEndpoint" (
	"Dataset_id" TEXT,
	"sparqlEndpoint" TEXT,
	PRIMARY KEY ("Dataset_id", "sparqlEndpoint"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_sparqlEndpoint_sparqlEndpoint" ON "Dataset_sparqlEndpoint" ("sparqlEndpoint");
CREATE INDEX "ix_Dataset_sparqlEndpoint_Dataset_id" ON "Dataset_sparqlEndpoint" ("Dataset_id");

CREATE TABLE "Dataset_dataDump" (
	"Dataset_id" TEXT,
	"dataDump" TEXT,
	PRIMARY KEY ("Dataset_id", "dataDump"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_dataDump_dataDump" ON "Dataset_dataDump" ("dataDump");
CREATE INDEX "ix_Dataset_dataDump_Dataset_id" ON "Dataset_dataDump" ("Dataset_id");

CREATE TABLE "Dataset_uriLookupEndpoint" (
	"Dataset_id" TEXT,
	"uriLookupEndpoint" TEXT,
	PRIMARY KEY ("Dataset_id", "uriLookupEndpoint"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_uriLookupEndpoint_Dataset_id" ON "Dataset_uriLookupEndpoint" ("Dataset_id");
CREATE INDEX "ix_Dataset_uriLookupEndpoint_uriLookupEndpoint" ON "Dataset_uriLookupEndpoint" ("uriLookupEndpoint");

CREATE TABLE "Dataset_openSearchDescription" (
	"Dataset_id" TEXT,
	"openSearchDescription" TEXT,
	PRIMARY KEY ("Dataset_id", "openSearchDescription"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_openSearchDescription_openSearchDescription" ON "Dataset_openSearchDescription" ("openSearchDescription");
CREATE INDEX "ix_Dataset_openSearchDescription_Dataset_id" ON "Dataset_openSearchDescription" ("Dataset_id");

CREATE TABLE "Dataset_rootResource" (
	"Dataset_id" TEXT,
	"rootResource" TEXT,
	PRIMARY KEY ("Dataset_id", "rootResource"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_rootResource_Dataset_id" ON "Dataset_rootResource" ("Dataset_id");
CREATE INDEX "ix_Dataset_rootResource_rootResource" ON "Dataset_rootResource" ("rootResource");

CREATE TABLE "Dataset_exampleResource" (
	"Dataset_id" TEXT,
	"exampleResource" TEXT,
	PRIMARY KEY ("Dataset_id", "exampleResource"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_exampleResource_Dataset_id" ON "Dataset_exampleResource" ("Dataset_id");
CREATE INDEX "ix_Dataset_exampleResource_exampleResource" ON "Dataset_exampleResource" ("exampleResource");

CREATE TABLE "Dataset_vocabulary" (
	"Dataset_id" TEXT,
	vocabulary TEXT,
	PRIMARY KEY ("Dataset_id", vocabulary),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_vocabulary_Dataset_id" ON "Dataset_vocabulary" ("Dataset_id");
CREATE INDEX "ix_Dataset_vocabulary_vocabulary" ON "Dataset_vocabulary" (vocabulary);

CREATE TABLE "Dataset_subset" (
	"Dataset_id" TEXT,
	subset_id TEXT,
	PRIMARY KEY ("Dataset_id", subset_id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(subset_id) REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_subset_Dataset_id" ON "Dataset_subset" ("Dataset_id");
CREATE INDEX "ix_Dataset_subset_subset_id" ON "Dataset_subset" (subset_id);

CREATE TABLE "TechnicalFeature_seeAlso" (
	"TechnicalFeature_id" TEXT,
	"seeAlso" TEXT,
	PRIMARY KEY ("TechnicalFeature_id", "seeAlso"),
	FOREIGN KEY("TechnicalFeature_id") REFERENCES "TechnicalFeature" (id)
);
CREATE INDEX "ix_TechnicalFeature_seeAlso_seeAlso" ON "TechnicalFeature_seeAlso" ("seeAlso");
CREATE INDEX "ix_TechnicalFeature_seeAlso_TechnicalFeature_id" ON "TechnicalFeature_seeAlso" ("TechnicalFeature_id");

CREATE TABLE "ClassBasedPartition" (
	id INTEGER NOT NULL,
	class TEXT NOT NULL,
	triples INTEGER,
	entities INTEGER,
	classes INTEGER,
	properties INTEGER,
	"distinctSubjects" INTEGER,
	"distinctObjects" INTEGER,
	documents INTEGER,
	"Dataset_id" TEXT,
	"Linkset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id)
);
CREATE INDEX "ix_ClassBasedPartition_id" ON "ClassBasedPartition" (id);

CREATE TABLE "Linkset_target" (
	"Linkset_id" TEXT,
	target_id TEXT,
	PRIMARY KEY ("Linkset_id", target_id),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id),
	FOREIGN KEY(target_id) REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Linkset_target_target_id" ON "Linkset_target" (target_id);
CREATE INDEX "ix_Linkset_target_Linkset_id" ON "Linkset_target" ("Linkset_id");

CREATE TABLE "Linkset_creator" (
	"Linkset_id" TEXT,
	creator TEXT,
	PRIMARY KEY ("Linkset_id", creator),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id)
);
CREATE INDEX "ix_Linkset_creator_Linkset_id" ON "Linkset_creator" ("Linkset_id");
CREATE INDEX "ix_Linkset_creator_creator" ON "Linkset_creator" (creator);

CREATE TABLE "Linkset_contributor" (
	"Linkset_id" TEXT,
	contributor TEXT,
	PRIMARY KEY ("Linkset_id", contributor),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id)
);
CREATE INDEX "ix_Linkset_contributor_Linkset_id" ON "Linkset_contributor" ("Linkset_id");
CREATE INDEX "ix_Linkset_contributor_contributor" ON "Linkset_contributor" (contributor);

CREATE TABLE "Linkset_source" (
	"Linkset_id" TEXT,
	source TEXT,
	PRIMARY KEY ("Linkset_id", source),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id)
);
CREATE INDEX "ix_Linkset_source_source" ON "Linkset_source" (source);
CREATE INDEX "ix_Linkset_source_Linkset_id" ON "Linkset_source" ("Linkset_id");

CREATE TABLE "Linkset_subject" (
	"Linkset_id" TEXT,
	subject TEXT,
	PRIMARY KEY ("Linkset_id", subject),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id)
);
CREATE INDEX "ix_Linkset_subject_subject" ON "Linkset_subject" (subject);
CREATE INDEX "ix_Linkset_subject_Linkset_id" ON "Linkset_subject" ("Linkset_id");

CREATE TABLE "Linkset_page" (
	"Linkset_id" TEXT,
	page TEXT,
	PRIMARY KEY ("Linkset_id", page),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id)
);
CREATE INDEX "ix_Linkset_page_page" ON "Linkset_page" (page);
CREATE INDEX "ix_Linkset_page_Linkset_id" ON "Linkset_page" ("Linkset_id");

CREATE TABLE "Linkset_feature" (
	"Linkset_id" TEXT,
	feature_id TEXT,
	PRIMARY KEY ("Linkset_id", feature_id),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id),
	FOREIGN KEY(feature_id) REFERENCES "TechnicalFeature" (id)
);
CREATE INDEX "ix_Linkset_feature_Linkset_id" ON "Linkset_feature" ("Linkset_id");
CREATE INDEX "ix_Linkset_feature_feature_id" ON "Linkset_feature" (feature_id);

CREATE TABLE "Linkset_sparqlEndpoint" (
	"Linkset_id" TEXT,
	"sparqlEndpoint" TEXT,
	PRIMARY KEY ("Linkset_id", "sparqlEndpoint"),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id)
);
CREATE INDEX "ix_Linkset_sparqlEndpoint_sparqlEndpoint" ON "Linkset_sparqlEndpoint" ("sparqlEndpoint");
CREATE INDEX "ix_Linkset_sparqlEndpoint_Linkset_id" ON "Linkset_sparqlEndpoint" ("Linkset_id");

CREATE TABLE "Linkset_dataDump" (
	"Linkset_id" TEXT,
	"dataDump" TEXT,
	PRIMARY KEY ("Linkset_id", "dataDump"),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id)
);
CREATE INDEX "ix_Linkset_dataDump_Linkset_id" ON "Linkset_dataDump" ("Linkset_id");
CREATE INDEX "ix_Linkset_dataDump_dataDump" ON "Linkset_dataDump" ("dataDump");

CREATE TABLE "Linkset_uriLookupEndpoint" (
	"Linkset_id" TEXT,
	"uriLookupEndpoint" TEXT,
	PRIMARY KEY ("Linkset_id", "uriLookupEndpoint"),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id)
);
CREATE INDEX "ix_Linkset_uriLookupEndpoint_uriLookupEndpoint" ON "Linkset_uriLookupEndpoint" ("uriLookupEndpoint");
CREATE INDEX "ix_Linkset_uriLookupEndpoint_Linkset_id" ON "Linkset_uriLookupEndpoint" ("Linkset_id");

CREATE TABLE "Linkset_openSearchDescription" (
	"Linkset_id" TEXT,
	"openSearchDescription" TEXT,
	PRIMARY KEY ("Linkset_id", "openSearchDescription"),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id)
);
CREATE INDEX "ix_Linkset_openSearchDescription_openSearchDescription" ON "Linkset_openSearchDescription" ("openSearchDescription");
CREATE INDEX "ix_Linkset_openSearchDescription_Linkset_id" ON "Linkset_openSearchDescription" ("Linkset_id");

CREATE TABLE "Linkset_rootResource" (
	"Linkset_id" TEXT,
	"rootResource" TEXT,
	PRIMARY KEY ("Linkset_id", "rootResource"),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id)
);
CREATE INDEX "ix_Linkset_rootResource_rootResource" ON "Linkset_rootResource" ("rootResource");
CREATE INDEX "ix_Linkset_rootResource_Linkset_id" ON "Linkset_rootResource" ("Linkset_id");

CREATE TABLE "Linkset_exampleResource" (
	"Linkset_id" TEXT,
	"exampleResource" TEXT,
	PRIMARY KEY ("Linkset_id", "exampleResource"),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id)
);
CREATE INDEX "ix_Linkset_exampleResource_Linkset_id" ON "Linkset_exampleResource" ("Linkset_id");
CREATE INDEX "ix_Linkset_exampleResource_exampleResource" ON "Linkset_exampleResource" ("exampleResource");

CREATE TABLE "Linkset_vocabulary" (
	"Linkset_id" TEXT,
	vocabulary TEXT,
	PRIMARY KEY ("Linkset_id", vocabulary),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id)
);
CREATE INDEX "ix_Linkset_vocabulary_Linkset_id" ON "Linkset_vocabulary" ("Linkset_id");
CREATE INDEX "ix_Linkset_vocabulary_vocabulary" ON "Linkset_vocabulary" (vocabulary);

CREATE TABLE "Linkset_subset" (
	"Linkset_id" TEXT,
	subset_id TEXT,
	PRIMARY KEY ("Linkset_id", subset_id),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id),
	FOREIGN KEY(subset_id) REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Linkset_subset_subset_id" ON "Linkset_subset" (subset_id);
CREATE INDEX "ix_Linkset_subset_Linkset_id" ON "Linkset_subset" ("Linkset_id");

CREATE TABLE "DatasetDescription_creator" (
	"DatasetDescription_id" TEXT,
	creator TEXT,
	PRIMARY KEY ("DatasetDescription_id", creator),
	FOREIGN KEY("DatasetDescription_id") REFERENCES "DatasetDescription" (id)
);
CREATE INDEX "ix_DatasetDescription_creator_creator" ON "DatasetDescription_creator" (creator);
CREATE INDEX "ix_DatasetDescription_creator_DatasetDescription_id" ON "DatasetDescription_creator" ("DatasetDescription_id");

CREATE TABLE "DatasetDescription_topic" (
	"DatasetDescription_id" TEXT,
	topic_id TEXT,
	PRIMARY KEY ("DatasetDescription_id", topic_id),
	FOREIGN KEY("DatasetDescription_id") REFERENCES "DatasetDescription" (id),
	FOREIGN KEY(topic_id) REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_DatasetDescription_topic_topic_id" ON "DatasetDescription_topic" (topic_id);
CREATE INDEX "ix_DatasetDescription_topic_DatasetDescription_id" ON "DatasetDescription_topic" ("DatasetDescription_id");

CREATE TABLE "PropertyBasedPartition" (
	id INTEGER NOT NULL,
	property TEXT NOT NULL,
	triples INTEGER,
	entities INTEGER,
	classes INTEGER,
	properties INTEGER,
	"distinctSubjects" INTEGER,
	"distinctObjects" INTEGER,
	documents INTEGER,
	"Dataset_id" TEXT,
	"Linkset_id" TEXT,
	"ClassBasedPartition_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("Linkset_id") REFERENCES "Linkset" (id),
	FOREIGN KEY("ClassBasedPartition_id") REFERENCES "ClassBasedPartition" (id)
);
CREATE INDEX "ix_PropertyBasedPartition_id" ON "PropertyBasedPartition" (id);
