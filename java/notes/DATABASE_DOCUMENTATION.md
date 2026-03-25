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
      <version>10.17.1.0</version>
    </dependency>
    <dependency>
        <groupId>org.apache.derby</groupId>
        <artifactId>derbytools</artifactId>
      <version>10.17.1.0</version>
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

### Wichtiger Hinweis zum Datenbank-Pfad
Neue Derby-Datenbanken sollen in diesem Projekt immer unter `java/Datenbanken` liegen.

Empfohlene JDBC-URL:

```text
jdbc:derby:Datenbanken/<DB_NAME>;create=true
```

Beispiel:

```text
jdbc:derby:Datenbanken/KundenDB;create=true
```

So landen alle Datenbanken in einem gemeinsamen Ordner und nicht mehr im Projekt-Root.

### Database Setup
1. Ensure the `Datenbanken` directory exists in `java`.
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

## SQL Grundlagen

### DELETE
Löscht Daten aus einer Tabelle basierend auf einer Bedingung.
```sql
DELETE FROM games
WHERE id = 1;
```

### UPDATE
Aktualisiert Daten in einer Tabelle basierend auf einer Bedingung.
```sql
UPDATE games
SET genre = 'Action RPG'
WHERE id = 1;
```

### SELECT
Wählt Daten aus einer Tabelle aus.
```sql
SELECT * FROM games;
```
Wählt nur bestimmte Spalten aus:
```sql
SELECT title, genre FROM games;
```

### NATURAL JOIN
Verbindet zwei Tabellen basierend auf gemeinsamen Spalten.
```sql
SELECT *
FROM games
NATURAL JOIN developers;
```

### Weitere Beispiele
- **WHERE**: Filtert Ergebnisse basierend auf einer Bedingung.
  ```sql
  SELECT * FROM games
  WHERE release_year > 2010;
  ```
- **ORDER BY**: Sortiert Ergebnisse.
  ```sql
  SELECT * FROM games
  ORDER BY release_year DESC;
  ```
- **LIMIT**: Begrenzung der Anzahl der Ergebnisse.
  ```sql
  SELECT * FROM games
  LIMIT 5;
  ```

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
- Ensure the database directory (`Datenbanken`) is not deleted between runs.
- Close all database connections after use to prevent resource leaks.

### ij Konsoile 
Da mich die Ansprache der Datenbank über Java ein bisschen genervt hat Wenn ich jetzt dazu übergegangen auch direkt in der Konsole natives SQL zu nutzen.

📘 Derby / ij – Spickzettel
# Derby / ij – Spickzettel

## 🚀 1. ij starten (Derby SQL-Konsole)

Voraussetzung: `derby.jar` und `derbytools.jar` liegen im `lib`-Ordner.

**Portable Beispiele für Windows:**

```powershell
java -cp "lib\\derbytools.jar;lib\\derby.jar" org.apache.derby.tools.ij

oder mit USERPROFILE (falls du nicht im `java`-Ordner stehst):
java -cp "$env:USERPROFILE\\repositories\\learning-journey\\java\\lib\\derbytools.jar;$env:USERPROFILE\\repositories\\learning-journey\\java\\lib\\derby.jar" org.apache.derby.tools.ij


Wenn alles klappt, erscheint:
ij>



2. Datenbank verbinden oder erstellen
CONNECT 'jdbc:derby:Datenbanken/meineDatenbank2;create=true';

oder mit einem absoluten Platzhalter-Pfad (ohne hardcodeten Benutzernamen):
CONNECT 'jdbc:derby:C:/<dein-pfad>/learning-journey/java/Datenbanken/meineDatenbank2;create=true';


- create=true erstellt die DB, falls sie nicht existiert
- Ohne Semikolon wird der Befehl nicht ausgeführt

3. Tabelle anlegen
CREATE TABLE games (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR(100),
    genre VARCHAR(50),
    release_year INT
);



4. Daten einfügen
INSERT INTO games (title, genre, release_year)
VALUES ('The Witcher 3', 'RPG', 2015);



5. Daten abfragen
SELECT * FROM games;



6. Daten aktualisieren
UPDATE games
SET genre = 'Action RPG'
WHERE id = 1;



7. Daten löschen
DELETE FROM games
WHERE id = 1;



8. Tabelle löschen
DROP TABLE games;



9. Verbindung schließen
DISCONNECT;



10. ij beenden
exit;



💡 Nützliche Hinweise
- Jeder SQL-Befehl muss mit einem Semikolon enden
- ij interpretiert Zeilen ohne Semikolon als „Befehl geht weiter“
- Datenbankordner wird automatisch erstellt, wenn create=true gesetzt ist
- In diesem Projekt sollen neue Datenbanken unter `java/Datenbanken` angelegt werden
- Derby speichert die DB als Ordnerstruktur, nicht als .db-Datei

---


