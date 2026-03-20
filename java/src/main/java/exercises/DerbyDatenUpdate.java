import java.sql.*;

public class DerbyDatenUpdate {
    public static void main(String[] args) {
        Connection conn = null;
        String driver = "org.apache.derby.jdbc.EmbeddedDriver";

        try {
            Class.forName(driver);

            String protocol = "jdbc:derby:";
            conn = DriverManager.getConnection(protocol + "meineDatenbank;create=true");

            Statement statement = conn.createStatement();
            String sql = "UPDATE Personen SET Hausnummer = 666 " +
                    "WHERE Vorname = 'Max' " +
                    "AND Nachname = 'Mustermann'";
            statement.execute(sql);
        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
