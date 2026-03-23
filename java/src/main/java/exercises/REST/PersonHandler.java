package REST;

import org.restlet.resource.ServerResource;
import org.restlet.resource.Get;
import java.sql.Connection;

public class PersonHandler extends ServerResource {
    private static Connection datenbankVerbindung;

    public static void setConnection(Connection conn) {
        datenbankVerbindung = conn;
    }

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