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
  A dataset of triples that join two datasets: each triple's subject belongs to one of them and its object to the other.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Linkset extends Dataset {

  private List<Dataset> target;
  private Dataset subjectsTarget;
  private Dataset objectsTarget;
  private URI linkPredicate;


}