# Database Integration Documentation

## Overview
This project demonstrates the integration of Apache Derby as an embedded database. It includes three main classes:

1. **DerbyTest**: Verifies that the Derby tools are correctly included.
2. **DerbyVerbindung**: Establishes a connection to the database and creates a table.
3. **DerbyAuslesen**: Inserts and retrieves data from the database.

## Setup Instructions

### Prerequisites
- Java Development Kit (JDK) installed.
- Maven installed (or use the Maven Wrapper).
- Apache Derby dependencies included in the `pom.xml` file.

### Maven Dependencies
Ensure the following dependencies are present in your `pom.xml` file:

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.derby</groupId>
        <artifactId>derby</artifactId>
        <version>10.15.2.0</version>
    </dependency>
    <dependency>
        <groupId>org.apache.derby</groupId>
        <artifactId>derbytools</artifactId>
        <version>10.15.2.0</version>
        <scope>system</scope>
        <systemPath>${project.basedir}/lib/derbytools.jar</systemPath>
    </dependency>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter</artifactId>
        <version>5.9.3</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```

### Database Setup
1. Ensure the `meineDatenbank` directory exists in the project root.
2. Run the `DerbyVerbindung` class to create the `Personen` table.
3. Run the `DerbyAuslesen` class to insert and retrieve data.

## Class Details

### DerbyTest
- **Purpose**: Confirms that the Derby tools are correctly included.
- **Usage**: Run the class to see a confirmation message.

### DerbyVerbindung
- **Purpose**: Establishes a connection to the database and creates a table named `Personen`.
- **Table Schema**:
  - `Vorname` (VARCHAR)
  - `Nachname` (VARCHAR)
  - `Strasse` (VARCHAR)
  - `Hausnummer` (INT)
  - `PLZ` (VARCHAR)
  - `Ort` (VARCHAR)
- **Usage**: Run the class to create the table.

### DerbyAuslesen
- **Purpose**: Inserts sample data into the `Personen` table and retrieves it.
- **Usage**: Run the class to insert and display data.

## Testing

### Unit Tests
- Use JUnit 5 to write tests for:
  - Database connection.
  - Table creation.
  - Data insertion and retrieval.

### Running Tests
- Use the following Maven command to run tests:
  ```bash
  mvn test
  ```

## Notes
- Ensure the database directory (`meineDatenbank`) is not deleted between runs.
- Close all database connections after use to prevent resource leaks.