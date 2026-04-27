package REST;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class PersonHandlerTest {

    private static Connection connection;

    @BeforeAll
    static void setupDatabase() throws Exception {
        connection = DriverManager.getConnection("jdbc:derby:memory:rest_test_db;create=true");
        PersonHandler.setConnection(connection);
    }

    @BeforeEach
    void resetTable() throws Exception {
        Statement stmt = connection.createStatement();

        try {
            stmt.execute("DROP TABLE Personen");
        } catch (Exception ignored) {
            // First run has no table yet.
        }

        stmt.execute(
                "CREATE TABLE Personen (Id INT, Vorname VARCHAR(255), Nachname VARCHAR(255), Strasse VARCHAR(255), Hausnummer INT, PLZ VARCHAR(255), Ort VARCHAR(255))");
        stmt.execute(
                "INSERT INTO Personen (Id, Vorname, Nachname, Strasse, Hausnummer, PLZ, Ort) VALUES (1, 'Max', 'Mustermann', 'Hauptstrasse', 10, '12345', 'Berlin')");
        stmt.execute(
                "INSERT INTO Personen (Id, Vorname, Nachname, Strasse, Hausnummer, PLZ, Ort) VALUES (2, 'Erika', 'Musterfrau', 'Nebenweg', 7, '54321', 'Hamburg')");

        stmt.close();
    }

    @Test
    void handleGet_withoutId_returnsAllPersonsAsArray() {
        TestablePersonHandler handler = new TestablePersonHandler(null);

        String result = handler.handleGet();

        assertTrue(result.startsWith("["));
        assertTrue(result.endsWith("]"));
        assertTrue(result.contains("\"id\": 1"));
        assertTrue(result.contains("\"id\": 2"));
    }

    @Test
    void handleGet_withExistingId_returnsSinglePerson() {
        TestablePersonHandler handler = new TestablePersonHandler("1");

        String result = handler.handleGet();

        assertTrue(result.contains("\"id\": 1"));
        assertTrue(result.contains("\"vorname\": \"Max\""));
    }

    @Test
    void handleGet_withMissingId_returnsNotFoundError() {
        TestablePersonHandler handler = new TestablePersonHandler("999");

        String result = handler.handleGet();

        assertTrue(result.contains("Person nicht gefunden"));
    }

    @Test
    void handlePost_insertsPersonIntoDatabase() throws Exception {
        TestablePersonHandler handler = new TestablePersonHandler(null);

        String body = "{\"id\":3,\"vorname\":\"Mia\",\"nachname\":\"Muster\",\"strasse\":\"Marktplatz\",\"hausnummer\":12,\"plz\":\"10115\",\"ort\":\"Berlin\"}";
        String result = handler.handlePost(body);

        assertTrue(result.contains("gespeichert"));

        Statement stmt = connection.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT Vorname, Nachname FROM Personen WHERE Id = 3");

        assertTrue(rs.next());
        assertEquals("Mia", rs.getString("Vorname"));
        assertEquals("Muster", rs.getString("Nachname"));

        rs.close();
        stmt.close();
    }

    @Test
    void handlePut_partialUpdate_updatesOnlyProvidedFields() throws Exception {
        TestablePersonHandler handler = new TestablePersonHandler("1");

        String result = handler.handlePut("{\"vorname\":\"Moritz\"}");

        assertTrue(result.contains("teilweise aktualisiert"));

        Statement stmt = connection.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT * FROM Personen WHERE Id = 1");
        assertTrue(rs.next());
        assertEquals("Moritz", rs.getString("Vorname"));
        assertEquals("Mustermann", rs.getString("Nachname"));
        assertEquals("Hauptstrasse", rs.getString("Strasse"));

        rs.close();
        stmt.close();
    }

    @Test
    void handlePut_withoutAnyUpdatableField_returnsError() {
        TestablePersonHandler handler = new TestablePersonHandler("1");

        String result = handler.handlePut("{}");

        assertTrue(result.contains("Keine Felder zum Aktualisieren"));
    }

    @Test
    void handlePut_withInvalidId_returnsError() {
        TestablePersonHandler handler = new TestablePersonHandler("abc");

        String result = handler.handlePut("{\"vorname\":\"Moritz\"}");

        assertTrue(result.contains("ID muss numerisch sein"));
    }

    private static class TestablePersonHandler extends PersonHandler {
        private final String id;

        private TestablePersonHandler(String id) {
            this.id = id;
        }

        @Override
        public String getAttribute(String name) {
            if ("id".equals(name)) {
                return id;
            }
            return null;
        }
    }
}
