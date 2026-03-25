import java.sql.*;

public class DerbyDatenUpdate {
    public static void main(String[] args) {
        Connection conn = null;

        try {
            String protocol = "jdbc:derby:";
            conn = DriverManager.getConnection(protocol + "Datenbanken/meineDatenbank2;create=true");

            Statement statement = conn.createStatement();
            String sql = "UPDATE Personen SET Hausnummer = 666 " +
                    "WHERE Vorname = 'Max' " +
                    "AND Nachname = 'Mustermann'";
            statement.execute(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
