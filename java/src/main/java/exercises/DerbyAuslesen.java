import java.sql.*;

public class DerbyAuslesen {
    public static void main(String[] args) {
        Connection conn = null;
        String driver = "org.apache.derby.jdbc.EmbeddedDriver";

        try {
            // Lade den Derby JDBC-Treiber
            Class.forName(driver);

            // Stelle die Verbindung zur Datenbank her
            String protocol = "jdbc:derby:";
            conn = DriverManager.getConnection(protocol + "meineDatenbank");

            // Erstelle ein Statement-Objekt
            Statement statement = conn.createStatement();

            // Füge Einträge in die Tabelle "Personen" ein
            String insertQuery = "INSERT INTO Personen (Vorname, Nachname, Strasse, Hausnummer, PLZ, Ort) VALUES " +
                    "('Max', 'Mustermann', 'Musterstrasse', 1, '12345', 'Musterstadt'), " +
                    "('Erika', 'Mustermann', 'Beispielweg', 2, '54321', 'Beispielstadt')";
            statement.executeUpdate(insertQuery);

            // Lese die Daten aus der Tabelle "Personen"
            String query = "SELECT * FROM Personen";
            ResultSet resultSet = statement.executeQuery(query);

            // Gib die Ergebnisse aus
            while (resultSet.next()) {
                System.out.println("Vorname: " + resultSet.getString("Vorname") + ", Nachname: "
                        + resultSet.getString("Nachname") + ", Strasse: " + resultSet.getString("Strasse")
                        + ", Hausnummer: "
                        + resultSet.getInt("Hausnummer") + ", Ort: " + resultSet.getString("Ort"));
            }

            resultSet.close();
            statement.close();
        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        } finally {
            // Schließe die Verbindung
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
