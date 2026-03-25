import java.sql.*;

public class DerbyVerbindung {
    public static void main(String[] args) {
        Connection conn = null;

        try {
            // Stelle die Verbindung her
            String protocol = "jdbc:derby:";
            conn = DriverManager.getConnection(protocol + "Datenbanken/meineDatenbank2;create=true");

            // Tabelle erstellen
            Statement statement = conn.createStatement();
            String sql = "CREATE TABLE Personen (" +
                    "Vorname VARCHAR(255), " +
                    "Nachname VARCHAR(255), " +
                    "Strasse VARCHAR(255), " +
                    "Hausnummer INT, " +
                    "PLZ VARCHAR(255), " +
                    "Ort VARCHAR(255))";
            statement.execute(sql);

            System.out.println("Tabelle 'Personen' wurde erfolgreich erstellt.");
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // schließe die connection, falls sie geöffnet wurde
            if (conn != null) {
                try {
                    conn.close();
                    System.out.println("Datenbankverbindung geschlossen.");
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}