# 📘 Meine Java Notes – Woche 1

Um das Gelernte anzuwenden, notiere ich Lerninhalte, Beispiele und Reflektionen.


Tagesnotizen
## 🗓️ Tag 22 Java  Kurs

### Dateisystem

Der heutige Focus iegt auf der kurzen zusammenfassung von Kapitel neun, welcher im Stundenplan nicht vorgesehen war, ich werd den stoff trotzdem bruchen.

Kapitel 9 befasst sich mit dem Dateisystem, also 
- (Text)Dateien schreiben mit FileWriter
- (Text)Dateien lesen mit Scanner
- Dateien löschen und umbenennen mit delete und renameTo
- Ordner erstellenb, mit mkdirs
- Ordner löschen mit delete
- Ordner umbenennen mit renameTo
- Inhalt anzeigen mit listFiles, isFile und isDirectory
- Objekte speichern mit write
- csv dateien einlesen ()
- binärdateien speichern mit write und Serializable
- binärdateien lesen über readObject und EOFException

#### Textdateien schreiben
```java
import java.io.FileWriter;
import java.io.IOException;

public class WriteTextFile {
    public static void main(String[] args) {
        try (FileWriter writer = new FileWriter("example.txt")) {
            writer.write("Hallo, Welt!\nDas ist ein Beispiel.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

#### Textdateien lesen
```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadTextFile {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(new File("example.txt"))) {
            while (scanner.hasNextLine()) {
                System.out.println(scanner.nextLine());
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```

#### Dateien löschen und umbenennen
```java
import java.io.File;

public class FileOperations {
    public static void main(String[] args) {
        File file = new File("example.txt");
        if (file.renameTo(new File("renamed_example.txt"))) {
            System.out.println("Datei umbenannt.");
        } else {
            System.out.println("Umbenennen fehlgeschlagen.");
        }

        if (file.delete()) {
            System.out.println("Datei gelöscht.");
        } else {
            System.out.println("Löschen fehlgeschlagen.");
        }
    }
}
```

#### Ordner erstellen
```java
import java.io.File;

public class CreateDirectory {
    public static void main(String[] args) {
        File directory = new File("newFolder");
        if (directory.mkdirs()) {
            System.out.println("Ordner erstellt.");
        } else {
            System.out.println("Ordnererstellung fehlgeschlagen.");
        }
    }
}
```

#### Ordner löschen
```java
import java.io.File;

public class DeleteDirectory {
    public static void main(String[] args) {
        File directory = new File("newFolder");
        if (directory.delete()) {
            System.out.println("Ordner gelöscht.");
        } else {
            System.out.println("Löschen fehlgeschlagen.");
        }
    }
}
```

#### Inhalt anzeigen
```java
import java.io.File;

public class ListFiles {
    public static void main(String[] args) {
        File directory = new File(".");
        File[] files = directory.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isFile()) {
                    System.out.println("Datei: " + file.getName());
                } else if (file.isDirectory()) {
                    System.out.println("Ordner: " + file.getName());
                }
            }
        }
    }
}
```

#### Objekte speichern
```java
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.Serializable;

public class SaveObject {
    public static void main(String[] args) {
        Person person = new Person("Max", 25);
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("person.dat"))) {
            oos.writeObject(person);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class Person implements Serializable {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

#### Binärdateien lesen
```java
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class ReadObject {
    public static void main(String[] args) {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("person.dat"))) {
            while (true) {
                try {
                    Person person = (Person) ois.readObject();
                    System.out.println("Name: " + person.name + ", Alter: " + person.age);
                } catch (EOFException e) {
                    break;
                }
            }
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}

class Person implements Serializable {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

### Dynamische Ermittlung des Arbeitsverzeichnisses in Java

In Java kann das aktuelle Arbeitsverzeichnis (Working Directory) mit der Methode `System.getProperty("user.dir")` dynamisch ermittelt werden. Dies ist besonders nützlich, um plattformunabhängige Pfade zu erstellen oder Dateien relativ zum Arbeitsverzeichnis zu finden.

Beispiel:
```java
public class Main {
    public static void main(String[] args) {
        String currentDir = System.getProperty("user.dir");
        System.out.println("Aktuelles Arbeitsverzeichnis: " + currentDir);
    }
}
```

- `System.getProperty("user.dir")` gibt den absoluten Pfad des aktuellen Arbeitsverzeichnisses zurück.
- Dies ist hilfreich, um hartcodierte Pfade zu vermeiden und Programme flexibler zu gestalten.


### Externe Bibliotheken

- JSON Bibliothek wird genutzt um JSON zu lesen und zu schreiben von .jar dateien
- bibliothek einbinden
- zum einlesen und unwandeln braucht man einen parser.

### JSON-Dateien lesen und schreiben in Java

JSON (JavaScript Object Notation) ist ein Format, um strukturierte Daten zu speichern und auszutauschen. In Java kann man JSON-Dateien mit Bibliotheken wie `Jackson` oder `Gson` einfach lesen und schreiben. Hier ist ein einfaches Beispiel mit der `Jackson`-Bibliothek:

#### JSON schreiben
```java
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;

public class WriteJson {
    public static void main(String[] args) {
        ObjectMapper objectMapper = new ObjectMapper();

        Person person = new Person("Max", 25);
        try {
            objectMapper.writeValue(new File("person.json"), person);
            System.out.println("JSON-Datei wurde erstellt.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class Person {
    public String name;
    public int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

#### JSON lesen
```java
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;

public class ReadJson {
    public static void main(String[] args) {
        ObjectMapper objectMapper = new ObjectMapper();

        try {
            Person person = objectMapper.readValue(new File("person.json"), Person.class);
            System.out.println("Name: " + person.name + ", Alter: " + person.age);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class Person {
    public String name;
    public int age;

    public Person() {
        // Standardkonstruktor für Jackson
    }
}
```

#### Erklärung
- **`ObjectMapper`**: Ein zentraler Bestandteil der Jackson-Bibliothek, um JSON-Daten zu lesen und zu schreiben.
- **JSON schreiben**: Mit `writeValue()` wird ein Java-Objekt in eine JSON-Datei umgewandelt.
- **JSON lesen**: Mit `readValue()` wird eine JSON-Datei in ein Java-Objekt umgewandelt.

#### Abhängigkeit hinzufügen
Um Jackson zu verwenden, füge die folgende Abhängigkeit zu deiner `pom.xml` hinzu (falls Maven genutzt wird):
```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.15.0</version>
</dependency>
```
Ich habe mich nun entschieden die org.json bibliothek zu nutzen, dafür musste ich maven installieren.

## Spickzettel: JSON in Java in 60 Sekunden (org.json + Maven)

### Was brauche ich?
- Eine `pom.xml` mit `org.json`-Dependency.
- Eine JSON-Datei, z. B. `src/main/java/exercises/data.json`.
- Eine Java-Klasse mit `main`, z. B. `JsonReader`.

### Die 5 wichtigsten Schritte
1. JSON-Datei als String lesen (`Files.readString(...)`).
2. String in `JSONObject` umwandeln (`new JSONObject(text)`).
3. Werte lesen:
   - Text: `getString("name")`
   - Zahl: `getInt("age")`
   - Array: `getJSONArray("skills")`
4. Optional über Arrays iterieren (`for`, `length()`).
5. Ergebnis ausgeben oder in Java-Objekte übertragen.

### Mini-Beispiel (Lesen)
```java
import org.json.JSONArray;
import org.json.JSONObject;

import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

public class JsonReader {
    public static void main(String[] args) throws Exception {
        String text = Files.readString(
            Path.of("src", "main", "java", "exercises", "data.json"),
            StandardCharsets.UTF_8
        );

        JSONObject json = new JSONObject(text);
        String name = json.getString("name");
        int age = json.getInt("age");
        JSONArray skills = json.getJSONArray("skills");

        System.out.println(name + " - " + age + " - " + skills.toList());
    }
}
```

### Befehle, die ich wirklich nutze
Im Ordner `java`:
```powershell
mvn compile
mvn --% -q exec:java -Dexec.mainClass=JsonReader
```

### Warum `--%` in PowerShell?
- Sonst kann PowerShell `-D...` falsch parsen.
- Mit `--%` geht der Parameter korrekt an Maven durch.

### Wenn etwas rot ist oder nicht läuft
1. Prüfen, ob `pom.xml` im `java`-Ordner liegt.
2. `mvn compile` ausführen.
3. In VS Code: `Java: Clean Java Language Server Workspace`.
4. VS Code neu laden.