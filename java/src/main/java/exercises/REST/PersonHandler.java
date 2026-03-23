package REST;

import org.restlet.resource.ServerResource;
import org.restlet.resource.Get;
import org.restlet.resource.Post;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

public class PersonHandler extends ServerResource {
    private static Connection datenbankVerbindung;

    public static void setConnection(Connection conn) {
        datenbankVerbindung = conn;
    }

    @Get
    public String handleGet() {
        String id = getAttribute("id");

        try {
            Statement stmt = datenbankVerbindung.createStatement();

            // 👉 FALL 1: Eine Person
            if (id != null) {
                ResultSet rs = stmt.executeQuery("SELECT * FROM Personen WHERE Id = " + id);

                if (rs.next()) {
                    return "{ \"id\": " + rs.getInt("Id") +
                            ", \"vorname\": \"" + rs.getString("Vorname") +
                            "\", \"nachname\": \"" + rs.getString("Nachname") +
                            "\" }";
                } else {
                    return "{ \"fehler\": \"Person nicht gefunden\" }";
                }
            }

            // 👉 FALL 2: Alle Personen
            ResultSet rs = stmt.executeQuery("SELECT * FROM Personen");

            StringBuilder json = new StringBuilder("[");
            boolean first = true;

            while (rs.next()) {
                if (!first) {
                    json.append(",");
                }

                json.append("{")
                        .append("\"id\": ").append(rs.getInt("Id")).append(",")
                        .append("\"vorname\": \"").append(rs.getString("Vorname")).append("\",")
                        .append("\"nachname\": \"").append(rs.getString("Nachname")).append("\"")
                        .append("}");

                first = false;
            }

            json.append("]");
            return json.toString();

        } catch (Exception e) {
            e.printStackTrace();
            return "{ \"fehler\": \"Serverfehler\" }";
        }
    }

    @Post
    public String handlePost(String body) {
        try {
            Statement stmt = datenbankVerbindung.createStatement();

            // Alle Felder parsen
            String id = body.split("\"id\":")[1].split(",")[0].trim();
            String vorname = body.split("\"vorname\":")[1].split("\"")[1];
            String nachname = body.split("\"nachname\":")[1].split("\"")[1];
            String strasse = body.split("\"strasse\":")[1].split("\"")[1];
            String hausnummer = body.split("\"hausnummer\":")[1].split(",")[0].trim();
            String plz = body.split("\"plz\":")[1].split("\"")[1];
            String ort = body.split("\"ort\":")[1].split("\"")[1];

            // Alle 7 Felder einfügen
            String sql = "INSERT INTO Personen (Id, Vorname, Nachname, Strasse, Hausnummer, PLZ, Ort) " +
                    "VALUES (" + id + ", '" + vorname + "', '" + nachname + "', '" +
                    strasse + "', " + hausnummer + ", '" + plz + "', '" + ort + "')";

            stmt.executeUpdate(sql);

            return "{ \"status\": \"Person mit Adresse gespeichert\" }";

        } catch (Exception e) {
            e.printStackTrace();
            return "{ \"fehler\": \"Konnte Person nicht speichern\" }";
        }
    }
}