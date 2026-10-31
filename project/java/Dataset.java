package example;

/* metamodel_version: 1.12.0 */
/* version: 2011-03-03 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  RDF triples from one provider, gathered under an IRI so that a description can speak of them as a whole.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Dataset  {

  private URI id;
  private String title;
  private String description;
  private List<URI> creator;
  private List<URI> contributor;
  private URI publisher;
  private List<URI> source;
  private LocalDate created;
  private LocalDate issued;
  private LocalDate modified;
  private URI license;
  private List<URI> subject;
  private URI homepage;
  private List<URI> page;
  private List<TechnicalFeature> feature;
  private List<URI> sparqlEndpoint;
  private List<URI> dataDump;
  private List<URI> uriLookupEndpoint;
  private List<URI> openSearchDescription;
  private List<URI> rootResource;
  private List<URI> exampleResource;
  private String uriSpace;
  private String uriRegexPattern;
  private List<URI> vocabulary;
  private List<Dataset> subset;
  private List<ClassBasedPartition> classPartition;
  private List<PropertyBasedPartition> propertyPartition;
  private Integer triples;
  private Integer entities;
  private Integer classes;
  private Integer properties;
  private Integer distinctSubjects;
  private Integer distinctObjects;
  private Integer documents;


}