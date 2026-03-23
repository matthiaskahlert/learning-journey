package REST;

import org.restlet.Component;
import org.restlet.data.Protocol;
import org.restlet.resource.ServerResource;
import org.restlet.routing.Router;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import org.restlet.resource.Post;


public class RESTSchnittstelle {
    private static Connection datenbankVerbindung = null;

    public static void dbInitialisieren() {
        try {
            Statement statement = datenbankVerbindung.createStatement();
            String sql = "SELECT * FROM Personen";
            statement.execute(sql);
        } catch (java.sql.SQLSyntaxErrorException e) {
            try {
                Statement statement = datenbankVerbindung.createStatement();
                String sql = "CREATE TABLE Personen (Id INT, Vorname VARCHAR(255), Nachname VARCHAR(255), Strasse VARCHAR(255), Hausnummer INT, PLZ VARCHAR(255), Ort VARCHAR(255))";
                statement.execute(sql);
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        final Component component = new Component();

        int port = 8080;
        if (args.length > 0) {
            try {
                port = Integer.parseInt(args[0]);
            } catch (NumberFormatException ignored) {
            }
        }

        component.getServers().add(Protocol.HTTP, port);
        try {
            String driver = "org.apache.derby.jdbc.EmbeddedDriver";
            Class.forName(driver);

            String protocol = "jdbc:derby:";
            datenbankVerbindung = DriverManager.getConnection(protocol + "personenDatenbank;create=true");

            dbInitialisieren();
            PersonHandler.setConnection(datenbankVerbindung);

        } catch (Exception e) {
            e.printStackTrace();
        }

        // 👉 HIER KOMMT DER ROUTER
        Router router = new Router(component.getContext().createChildContext());

        router.attach("/", StartseitenHandler.class);
        router.attach("/person", PersonHandler.class);
        router.attach("/person/{id}", PersonHandler.class);

        component.getDefaultHost().attach(router);

        try {
            component.start();
            System.out.println("Server läuft auf Port " + port);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}