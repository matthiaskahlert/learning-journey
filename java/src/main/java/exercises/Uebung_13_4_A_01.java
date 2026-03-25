/* 
Entwickle ein Java-Programm, das eine SQLite-Datenbank verwendet, um eine Tabelle namens Bestellungen zu erstellen und zu verwalten. Die Tabelle soll folgende Spalten enthalten: Bestellnummer (INTEGER), KundenID (INTEGER), Datum (DATE), Gesamtbetrag (FLOAT). Das Programm soll folgende Funktionalitäten haben:

a) Verbindung zur Datenbank herstellen und die Tabelle Bestellungen erstellen, falls sie noch nicht existiert.

b) Eine Methode, die es ermöglicht, neue Bestellungen hinzuzufügen. Die Methode soll die Bestellnummer automatisch als nächsthöhere Zahl generieren, indem sie die höchste vorhandene Bestellnummer in der Datenbank findet und diese um 1 erhöht.

c) Eine Methode, die es ermöglicht, alle Bestellungen eines bestimmten Kunden (durch KundenID) anzuzeigen. Verwende eine Schleife, um durch die Ergebnisse zu iterieren und gib sie in der Konsole aus.

d) Eine Methode, die den Gesamtbetrag aller Bestellungen berechnet und diesen ausgibt.

e) Eine Fehlerbehandlung, die SQL-Exceptions abfängt und dem Benutzer eine verständliche Nachricht ausgibt, sollte etwas schiefgehen
*/

import java.sql.*;

public class Uebung_13_4_A_01 {

    // a) Verbindung zur SQLite-Datenbank herstellen, erstellt die .db Datei
    // automatisch falls sie nicht existiert
    private static Connection verbindeZurDatenbank() {
        String url = "jdbc:sqlite:java\\src\\main\\java\\exercises\\bestellungen.db";
        Connection conn = null;
        try {
            conn = DriverManager.getConnection(url);
        } catch (SQLException e) {
            System.out.println("Verbindung zur Datenbank konnte nicht hergestellt werden: " + e.getMessage());
        }
        return conn;
    }

    // a) Tabelle erstellen, IF NOT EXISTS sorgt dafür, dass sie nicht doppelt
    // erstellt wird
    private static void erstelleTabelle() {
        String sql = "CREATE TABLE IF NOT EXISTS Bestellungen (" +
                "Bestellnummer INTEGER PRIMARY KEY AUTOINCREMENT," +
                "KundenID INTEGER NOT NULL," +
                "Datum DATE NOT NULL," +
                "Gesamtbetrag FLOAT NOT NULL)";
        try (Connection conn = verbindeZurDatenbank();
                Statement stmt = conn.createStatement()) {
            stmt.execute(sql);
        } catch (SQLException e) {
            System.out.println("Tabelle konnte nicht erstellt werden: " + e.getMessage());
        }
    }

    // b) Neue Bestellung hinzufügen, Bestellnummer wird durch AUTOINCREMENT
    // automatisch generiert
    private static void fuegeBestellungHinzu(int kundenID, Date datum, float gesamtbetrag) {
        String sql = "INSERT INTO Bestellungen (KundenID, Datum, Gesamtbetrag) VALUES (?, ?, ?)";
        try (Connection conn = verbindeZurDatenbank();
                PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, kundenID);
            pstmt.setDate(2, datum);
            pstmt.setFloat(3, gesamtbetrag);
            pstmt.executeUpdate();
            System.out.println("Bestellung hinzugefügt (Kunde: " + kundenID + ", Betrag: " + gesamtbetrag + ")");
        } catch (SQLException e) {
            System.out.println("Bestellung konnte nicht hinzugefügt werden: " + e.getMessage());
        }
    }

    // c) Alle Bestellungen eines bestimmten Kunden anzeigen
    private static void zeigeBestellungenVonKunde(int kundenID) {
        String sql = "SELECT * FROM Bestellungen WHERE KundenID = ?";
        try (Connection conn = verbindeZurDatenbank();
                PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, kundenID);
            ResultSet rs = pstmt.executeQuery();

            System.out.println("\n=== Bestellungen von Kunde " + kundenID + " ===");
            // Schleife über alle Ergebnisse
            while (rs.next()) {
                System.out.println("Bestellnummer: " + rs.getInt("Bestellnummer")
                        + ", Datum: " + rs.getDate("Datum")
                        + ", Gesamtbetrag: " + rs.getFloat("Gesamtbetrag"));
            }
        } catch (SQLException e) {
            System.out.println("Bestellungen konnten nicht abgerufen werden: " + e.getMessage());
        }
    }

    // d) Gesamtbetrag aller Bestellungen berechnen
    private static void berechneGesamtbetrag() {
        String sql = "SELECT SUM(Gesamtbetrag) AS Total FROM Bestellungen";
        try (Connection conn = verbindeZurDatenbank();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {
            if (rs.next()) {
                System.out.println("\nGesamtbetrag aller Bestellungen: " + rs.getFloat("Total"));
            }
        } catch (SQLException e) {
            System.out.println("Gesamtbetrag konnte nicht berechnet werden: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        // a) Tabelle erstellen
        erstelleTabelle();

        // b) Bestellungen hinzufügen
        fuegeBestellungHinzu(1, Date.valueOf("2025-03-20"), 99.99f);
        fuegeBestellungHinzu(2, Date.valueOf("2025-03-21"), 124.50f);
        fuegeBestellungHinzu(1, Date.valueOf("2025-03-22"), 49.99f);

        // c) Bestellungen von Kunde 1 anzeigen
        zeigeBestellungenVonKunde(1);

        // d) Gesamtbetrag ausgeben
        berechneGesamtbetrag();
    }
}
