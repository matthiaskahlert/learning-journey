package REST;

import org.json.JSONObject;
import org.restlet.resource.Get;
import org.restlet.resource.Post;
import org.restlet.resource.Put;
import org.restlet.resource.ServerResource;

import java.sql.Connection;
import java.sql.PreparedStatement;
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
            if (id != null) {
                try (PreparedStatement stmt = datenbankVerbindung
                        .prepareStatement("SELECT * FROM Personen WHERE Id = ?")) {
                    stmt.setInt(1, Integer.parseInt(id));
                    ResultSet rs = stmt.executeQuery();
                    if (rs.next()) {
                        return "{ \"id\": " + rs.getInt("Id") +
                                ", \"vorname\": \"" + rs.getString("Vorname") +
                                "\", \"nachname\": \"" + rs.getString("Nachname") +
                                "\" }";
                    }
                    return "{ \"fehler\": \"Person nicht gefunden\" }";
                }
            }

            try (Statement stmt = datenbankVerbindung.createStatement()) {
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
            }
        } catch (Exception e) {
            return "{ \"fehler\": \"Serverfehler\" }";
        }
    }

    @Post
    public String handlePost(String body) {
        try {
            JSONObject person = new JSONObject(body);

            try (PreparedStatement stmt = datenbankVerbindung.prepareStatement(
                    "INSERT INTO Personen (Id, Vorname, Nachname, Strasse, Hausnummer, PLZ, Ort) VALUES (?, ?, ?, ?, ?, ?, ?)")) {
                stmt.setInt(1, person.getInt("id"));
                stmt.setString(2, person.getString("vorname"));
                stmt.setString(3, person.getString("nachname"));
                stmt.setString(4, person.getString("strasse"));
                stmt.setInt(5, person.getInt("hausnummer"));
                stmt.setString(6, person.getString("plz"));
                stmt.setString(7, person.getString("ort"));

                stmt.executeUpdate();
            }

            return "{ \"status\": \"Person mit Adresse gespeichert\" }";
        } catch (Exception e) {
            return "{ \"fehler\": \"Konnte Person nicht speichern\" }";
        }
    }

    @Put
    public String handlePut(String body) {
        String id = getAttribute("id");

        if (id == null) {
            return "{ \"fehler\": \"Keine ID angegeben\" }";
        }

        if (!id.matches("\\d+")) {
            return "{ \"fehler\": \"ID muss numerisch sein\" }";
        }

        try {
            JSONObject person = new JSONObject(body);
            Statement stmt = datenbankVerbindung.createStatement();

            StringBuilder sql = new StringBuilder("UPDATE Personen SET ");
            boolean first = true;

            if (person.has("vorname")) {
                if (!first) {
                    sql.append(", ");
                }
                sql.append("Vorname = '").append(escapeSql(person.getString("vorname"))).append("'");
                first = false;
            }

            if (person.has("nachname")) {
                if (!first) {
                    sql.append(", ");
                }
                sql.append("Nachname = '").append(escapeSql(person.getString("nachname"))).append("'");
                first = false;
            }

            if (person.has("adresse") && !person.isNull("adresse")) {
                JSONObject adresse = person.getJSONObject("adresse");

                if (adresse.has("strasse")) {
                    if (!first) {
                        sql.append(", ");
                    }
                    sql.append("Strasse = '").append(escapeSql(adresse.getString("strasse"))).append("'");
                    first = false;
                }

                if (adresse.has("hausnummer")) {
                    if (!first) {
                        sql.append(", ");
                    }
                    sql.append("Hausnummer = ").append(adresse.getInt("hausnummer"));
                    first = false;
                }

                if (adresse.has("plz")) {
                    if (!first) {
                        sql.append(", ");
                    }
                    sql.append("PLZ = '").append(escapeSql(adresse.getString("plz"))).append("'");
                    first = false;
                }

                if (adresse.has("ort")) {
                    if (!first) {
                        sql.append(", ");
                    }
                    sql.append("Ort = '").append(escapeSql(adresse.getString("ort"))).append("'");
                    first = false;
                }
            }

            if (first) {
                return "{ \"fehler\": \"Keine Felder zum Aktualisieren\" }";
            }

            sql.append(" WHERE Id = ").append(id);
            int aktualisierteZeilen = stmt.executeUpdate(sql.toString());

            if (aktualisierteZeilen == 0) {
                return "{ \"fehler\": \"Person nicht gefunden\" }";
            }

            return "{ \"status\": \"Person teilweise aktualisiert\" }";
        } catch (Exception e) {
            return "{ \"fehler\": \"Konnte Person nicht aktualisieren\" }";
        }
    }

    private static String escapeSql(String value) {
        return value.replace("'", "''");
    }
}
