package REST;

import org.json.JSONObject;
import org.restlet.resource.ServerResource;
import org.restlet.resource.Get;
import org.restlet.resource.Post;
import org.restlet.resource.Put;

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
            if (id != null) { // Wenn id != null, wird eine einzelne Person gesucht.
                ResultSet rs = stmt.executeQuery("SELECT * FROM Personen WHERE Id = " + id);

                if (rs.next()) { // Wenn dann rs.next() true ist, wird die Person zurückgegeben.
                    return "{ \"id\": " + rs.getInt("Id") +
                            ", \"vorname\": \"" + rs.getString("Vorname") +
                            "\", \"nachname\": \"" + rs.getString("Nachname") +
                            "\" }";
                } else { // Wenn rs.next() false ist, kommt "Person nicht gefunden".
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

    @Put
    public String handlePut(String body) {
        String id = getAttribute("id");

        if (id == null) {
            return "{ \"fehler\": \"Keine ID angegeben\" }";
        }

        try {
            JSONObject person = new JSONObject(body);
            JSONObject adresse = person.getJSONObject("adresse");

            Statement stmt = datenbankVerbindung.createStatement();

            String sql = "UPDATE Personen SET " +
                    "Vorname = '" + person.getString("vorname") + "', " +
                    "Nachname = '" + person.getString("nachname") + "', " +
                    "Strasse = '" + adresse.getString("strasse") + "', " +
                    "Hausnummer = " + adresse.getInt("hausnummer") + ", " +
                    "PLZ = '" + adresse.getString("plz") + "', " +
                    "Ort = '" + adresse.getString("ort") + "' " +
                    "WHERE Id = " + id;

            int aktualisierteZeilen = stmt.executeUpdate(sql);

            if (aktualisierteZeilen == 0) {
                return "{ \"fehler\": \"Person nicht gefunden\" }";
            }

            return "{ \"status\": \"Person aktualisiert\" }";

        } catch (Exception e) {
            e.printStackTrace();
            return "{ \"fehler\": \"Konnte Person nicht aktualisieren\" }";
        }
    }
}