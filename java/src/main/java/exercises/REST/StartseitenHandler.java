package REST;

import org.restlet.resource.Get;
import org.restlet.resource.Post;
import org.restlet.resource.ServerResource;

public class StartseitenHandler extends ServerResource {

    @Get("txt")
    public String handleGet() {
        return "Vielen Dank fuer Ihre GET Anfrage";
    }

    @Post("txt")
    public String handlePost() {
        return "Vielen Dank fuer Ihre POST Anfrage";
    }
}