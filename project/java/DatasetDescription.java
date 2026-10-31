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
  A web document, such as a void.ttl file published beside a dataset, that describes one or more datasets.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DatasetDescription  {

  private URI id;
  private String title;
  private String description;
  private List<URI> creator;
  private LocalDate created;
  private LocalDate modified;
  private Dataset primaryTopic;
  private List<Dataset> topic;
  private Dataset inDataset;


}