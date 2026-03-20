import java.sql.*;

public class DerbyVerbindung {
    public static void main(String[] args) {
        Connection conn = null;
        String driver = "org.apache.derby.jdbc.EmbeddedDriver";

        try {
            // lade den e Derby JDBC driver
            Class.forName(driver);

            // Stelle die Verbindung her
            String protocol = "jdbc:derby:";
            conn = DriverManager.getConnection(protocol + "meineDatenbank;create=true");

            // Create a table
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
        } catch (SQLException | ClassNotFoundException e) {
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