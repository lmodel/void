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
  A technical property of how a dataset is served, such as an RDF syntax it can be read in or an HTTP feature its server supports.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TechnicalFeature  {

  private URI id;
  private String label;
  private String comment;
  private List<URI> seeAlso;


}