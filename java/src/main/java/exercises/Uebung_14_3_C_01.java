/* 
Du arbeitest für ein Unternehmen, das eine interne Anwendung zur Verwaltung von Mitarbeiterdaten entwickelt. 
Deine Aufgabe ist es, eine Java-Anwendung zu erstellen, die eine Verbindung zu einer Datenbank herstellt, eine Tabelle für Mitarbeiterdaten erstellt, Daten hinzufügt und eine REST-Schnittstelle bereitstellt, um Mitarbeiterdaten abzufragen.

a) Stelle zunächst eine Verbindung zu einer Apache Derby-Datenbank her. Verwende dazu die JDBC-Schnittstelle und den Treiber org.apache.derby.jdbc.EmbeddedDriver. Die Datenbank soll den Namen MitarbeiterDB tragen. Sollte die Datenbank noch nicht existieren, soll sie automatisch erstellt werden.

b) Erstelle eine Tabelle Mitarbeiter mit den Spalten ID (INT, Primärschlüssel), Vorname (VARCHAR(255)), Nachname (VARCHAR(255)), Abteilung (VARCHAR(255)) und Einstellungsdatum (DATE).

c) Füge der Tabelle Mitarbeiter mindestens drei Datensätze hinzu. Verwende dafür den SQL-Befehl INSERT INTO.

d) Entwickle eine einfache REST-Schnittstelle mit einem GET-Endpoint /mitarbeiter, der alle Mitarbeiterdaten als JSON zurückgibt. Implementiere die Abfrage der Daten aus der Datenbank und die Umwandlung in das JSON-Format.
*/

import java.sql.*;
import java.io.IOException;
import java.net.InetSocketAddress;
import org.json.JSONArray;
import org.json.JSONObject;
import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

public class Uebung_14_3_C_01 {
    private static final String DB_URL = "jdbc:derby:Datenbanken/MitarbeiterDB;create=true";

    public static void main(String[] args) throws Exception {
        // a) Verbindung zur Datenbank herstellen
        Connection conn = DriverManager.getConnection(DB_URL);
        Statement stmt = conn.createStatement();

        // b) Tabelle erstellen (nur wenn sie nicht existiert)
        try {
            stmt.executeUpdate("CREATE TABLE Mitarbeiter (" +
                    "ID INT PRIMARY KEY, " +
                    "Vorname VARCHAR(255), " +
                    "Nachname VARCHAR(255), " +
                    "Abteilung VARCHAR(255), " +
                    "Einstellungsdatum DATE)");
        } catch (SQLException e) {
            // Tabelle existiert evtl. schon
        }

        // c) Datensätze hinzufügen (nur wenn leer)
        ResultSet rs = stmt.executeQuery("SELECT COUNT(*) FROM Mitarbeiter");
        rs.next();
        if (rs.getInt(1) == 0) {
            stmt.executeUpdate(
                    "INSERT INTO Mitarbeiter (ID, Vorname, Nachname, Abteilung, Einstellungsdatum) VALUES (1, 'Max', 'Mustermann', 'IT', '2020-01-15')");
            stmt.executeUpdate(
                    "INSERT INTO Mitarbeiter (ID, Vorname, Nachname, Abteilung, Einstellungsdatum) VALUES (2, 'Erika', 'Musterfrau', 'HR', '2019-03-22')");
            stmt.executeUpdate(
                    "INSERT INTO Mitarbeiter (ID, Vorname, Nachname, Abteilung, Einstellungsdatum) VALUES (3, 'John', 'Doe', 'Finance', '2021-07-01')");
        }
        rs.close();
        stmt.close();
        conn.close();

        System.out.println("Datenbank bereit. Starte REST-Server auf Port 8080...");

        // d) REST-Server starten
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
        server.createContext("/mitarbeiter", new MitarbeiterHandler());
        server.setExecutor(null);
        server.start();
    }

    // Handler für /mitarbeiter
    static class MitarbeiterHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (!"GET".equals(exchange.getRequestMethod())) {
                exchange.sendResponseHeaders(405, -1); // Method Not Allowed
                return;
            }
            try (Connection conn = DriverManager.getConnection(DB_URL);
                    Statement stmt = conn.createStatement();
                    ResultSet rs = stmt.executeQuery("SELECT * FROM Mitarbeiter")) {
                JSONArray mitarbeiterArray = new JSONArray();
                while (rs.next()) {
                    JSONObject obj = new JSONObject();
                    obj.put("ID", rs.getInt("ID"));
                    obj.put("Vorname", rs.getString("Vorname"));
                    obj.put("Nachname", rs.getString("Nachname"));
                    obj.put("Abteilung", rs.getString("Abteilung"));
                    obj.put("Einstellungsdatum", rs.getDate("Einstellungsdatum").toString());
                    mitarbeiterArray.put(obj);
                }
                String response = mitarbeiterArray.toString();
                exchange.getResponseHeaders().add("Content-Type", "application/json; charset=UTF-8");
                exchange.sendResponseHeaders(200, response.getBytes().length);
                exchange.getResponseBody().write(response.getBytes());
                exchange.getResponseBody().close();
            } catch (SQLException e) {
                String msg = "Fehler beim Datenbankzugriff: " + e.getMessage();
                exchange.sendResponseHeaders(500, msg.getBytes().length);
                exchange.getResponseBody().write(msg.getBytes());
                exchange.getResponseBody().close();
            }
        }
    }
}
// Die Datei erstellt die Derby-Datenbank,
// fügt Datensätze ein und stellt einen REST-Endpoint /mitarbeiter bereit,
// der alle Mitarbeiterdaten als JSON zurückgibt.
// Starte das Programm und rufe im Browser oder mit curl
// http://localhost:8080/mitarbeiter auf,
// um die Daten zu sehen.