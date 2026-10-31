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
  The slice of a dataset made of the triples whose predicate is one property, written inside that dataset, most often to give counts for it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PropertyBasedPartition  {

  private URI property;
  private Integer triples;
  private Integer entities;
  private Integer classes;
  private Integer properties;
  private Integer distinctSubjects;
  private Integer distinctObjects;
  private Integer documents;


}