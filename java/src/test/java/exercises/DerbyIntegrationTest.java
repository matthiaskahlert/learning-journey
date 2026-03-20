/*
 * package exercises;
 * 
 * import org.junit.jupiter.api.*;
 * import java.sql.*;
 * 
 * import static org.junit.jupiter.api.Assertions.*;
 * 
 * @TestMethodOrder(MethodOrderer.OrderAnnotation.class)
 * public class DerbyIntegrationTest {
 * 
 * private static final String DB_URL = "jdbc:derby:meineDatenbank;create=true";
 * private static Connection connection;
 * 
 * @BeforeAll
 * public static void setupDatabase() throws SQLException,
 * ClassNotFoundException {
 * Class.forName("org.apache.derby.jdbc.EmbeddedDriver");
 * connection = DriverManager.getConnection(DB_URL);
 * }
 * 
 * @AfterAll
 * public static void tearDownDatabase() throws SQLException {
 * if (connection != null) {
 * connection.close();
 * }
 * }
 * 
 * @BeforeEach
 * public void resetDatabase() throws SQLException {
 * Statement statement = connection.createStatement();
 * 
 * // Drop the table if it exists
 * try {
 * statement.execute("DROP TABLE TestTable");
 * } catch (SQLException e) {
 * // Ignore error if the table does not exist
 * }
 * 
 * // Recreate the table with the correct schema
 * String createTableSQL = "CREATE TABLE TestTable (" +
 * "ID INT PRIMARY KEY, " +
 * "Name VARCHAR(255), " +
 * "Strasse VARCHAR(255), " +
 * "Hausnummer INT)";
 * statement.execute(createTableSQL);
 * statement.close();
 * }
 * 
 * @AfterEach
 * public void truncateTable() throws SQLException {
 * Statement statement = connection.createStatement();
 * // Truncate the table to ensure a clean state for subsequent tests
 * statement.execute("DELETE FROM TestTable");
 * statement.close();
 * }
 * 
 * @Test
 * 
 * @Order(1)
 * public void testTableCreation() throws SQLException {
 * Statement statement = connection.createStatement();
 * 
 * // Drop the table if it exists
 * try {
 * statement.execute("DROP TABLE TestTable");
 * } catch (SQLException e) {
 * // Ignore error if the table does not exist
 * }
 * 
 * // Create the table
 * String createTableSQL = "CREATE TABLE TestTable (" +
 * "ID INT PRIMARY KEY, " +
 * "Name VARCHAR(255), " +
 * "Strasse VARCHAR(255), " +
 * "Hausnummer INT)";
 * statement.execute(createTableSQL);
 * 
 * // Verify table creation
 * DatabaseMetaData metaData = connection.getMetaData();
 * ResultSet tables = metaData.getTables(null, null, "TESTTABLE", null);
 * assertTrue(tables.next(), "Table 'TestTable' should exist.");
 * 
 * tables.close();
 * statement.close();
 * }
 * 
 * @Test
 * 
 * @Order(2)
 * public void testInsertData() throws SQLException {
 * Statement statement = connection.createStatement();
 * 
 * // Insert data into the table
 * String insertSQL =
 * "INSERT INTO TestTable (ID, Name, Strasse, Hausnummer) VALUES (1, 'TestName', 'TestStreet', 123)"
 * ;
 * int rowsInserted = statement.executeUpdate(insertSQL);
 * 
 * assertEquals(1, rowsInserted, "One row should be inserted.");
 * statement.close();
 * }
 * 
 * @Test
 * 
 * @Order(3)
 * public void testRetrieveData() throws SQLException {
 * Statement statement = connection.createStatement();
 * String querySQL = "SELECT * FROM TestTable WHERE ID = 1";
 * ResultSet resultSet = statement.executeQuery(querySQL);
 * 
 * assertTrue(resultSet.next(), "Data should be retrieved.");
 * assertEquals("TestName", resultSet.getString("Name"),
 * "Name should match the inserted value.");
 * 
 * resultSet.close();
 * statement.close();
 * }
 * 
 * @Test
 * 
 * @Order(4)
 * public void testRetrieveDataWithAddress() throws SQLException {
 * Statement statement = connection.createStatement();
 * String querySQL = "SELECT * FROM TestTable WHERE ID = 1";
 * ResultSet resultSet = statement.executeQuery(querySQL);
 * 
 * assertTrue(resultSet.next(), "Data should be retrieved.");
 * assertEquals("TestName", resultSet.getString("Name"),
 * "Name should match the inserted value.");
 * assertEquals("TestStreet", resultSet.getString("Strasse"),
 * "Strasse should match the inserted value.");
 * assertEquals(123, resultSet.getInt("Hausnummer"),
 * "Hausnummer should match the inserted value.");
 * 
 * resultSet.close();
 * statement.close();
 * }
 * }
 */