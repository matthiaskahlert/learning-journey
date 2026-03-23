package REST;

import org.restlet.resource.ServerResource;
import org.restlet.resource.Get;

public class PersonHandler extends ServerResource {

    @Get
    public String handleGet() {
        String id = getAttribute("id");

        if (id != null) {
            return "Person mit ID: " + id;
        } else {
            return "Alle Personen";
        }
    }
}