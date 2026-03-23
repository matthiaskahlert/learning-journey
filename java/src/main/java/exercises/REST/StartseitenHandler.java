package REST;

import org.restlet.resource.ServerResource;
import org.restlet.resource.Get;

public class StartseitenHandler extends ServerResource {

    @Get
    public String handleGet() {
        return "Server läuft!";
    }
}