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

### Befehle, die ich derzeit nutze
Im Ordner `java`:
```powershell
mvn clean
mvn compile
mvn --% -q exec:java -Dexec.mainClass=JsonReader
mvn test
```

### Warum `--%` in PowerShell?
- Sonst kann PowerShell `-D...` falsch parsen.
- Mit `--%` geht der Parameter korrekt an Maven durch.

### Wenn etwas rot ist oder nicht läuft
1. Prüfen, ob `pom.xml` im `java`-Ordner liegt.
2. `mvn compile` ausführen.
3. In VS Code: `Java: Clean Java Language Server Workspace`.
4. VS Code neu laden.
### GUI
Java nutzt Standardbibliotheken für GUI Elenmente wie Buttons etc.
Drei bekannte Bibliotheken für grafische Benutzerpberflächen sind Swing, JavaFX und SWT.
- Ich nutze die Swing
- Fenster werden mit JFrame erzeugt.
- 
```java
import javax.swing.JFrame;

public class Fensterprogramm {
    public static void main (String[] args) {
        JFrame f=new JFrame();
        f.setSize(400,500);
        f.setVisible(true);
    }
}
```
Damit sich das Programm auch nach schließen des Fensters beendet braucht man 
```java
setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
```
- Textfelder mit JTextArea
```java
JTextArea textArea = new JTextArea();
f.add(textArea);

f.setVisible(true);
```
- textfelder erscheinung a anpassen mit setBackground, setForeground, setFont
  

```java
// um Color und Font zu nutzen muss man das noch importieren:
import java.awt.Color;
import java.awt.Font;
// ...%
textArea.setBackground(Color.BLUE);
textArea.setForeground(Color.WHITE);
textArea.setFont(new Font("Serif", Font.ITALIC, 16));


```

- Buttons mit einem Objekt vom Typ JButton erstellen
- Der Button braucht einen ActionListener der die Funktion actionPerformed beides wird importiert
- import java.awt.event.ActionEvent;
- import java.awt.event.ActionListener;
- Layout kann man mit BorderLayout setzen, dies teilt den Bereich auf in:
 


#### Layout Positionen und Labels

| Name         | Position |
|--------------|----------|
| PAGE_START   | B1    Header   |
| LINE_START   | B2       |
| CENTER       | B3       |
| LINE_END     | B4       |
| PAGE_END     | B5     Footer  |

folgender code zeigt die bereiche

```java

```

#### BorderLayout Beispiel

```java
import javax.swing.*;
import java.awt.*;

public class BorderLayoutExample {
    public static void main(String[] args) {
        JFrame f = new JFrame();
        f.setSize(300, 200);
        f.setLayout(new BorderLayout());

        JButton button1 = new JButton("B1");
        f.add(button1, BorderLayout.PAGE_START);

        JButton button2 = new JButton("B2");
        f.add(button2, BorderLayout.LINE_START);

        JButton button3 = new JButton("B3");
        f.add(button3, BorderLayout.CENTER);

        JButton button4 = new JButton("B4");
        f.add(button4, BorderLayout.LINE_END);

        JButton button5 = new JButton("B5");
        f.add(button5, BorderLayout.PAGE_END);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
```
#### FlowLayout Beispiel
- im FlowLayout werden die Elemente in einer Reihe positioniert, falls das Fenster zu klein ist, geht es eine Reihe weiter unten weiter.
beispiel
```java
import javax.swing.*;
import java.awt.*;

public class FlowLayoutExample {
    public static void main(String[] args) {
        JFrame f = new JFrame();
        f.setSize(300, 200);
        f.setLayout(new FlowLayout());

        JButton button1 = new JButton("B1");
        f.add(button1);

        JButton button2 = new JButton("B2");
        f.add(button2);

        JButton button3 = new JButton("B3");
        f.add(button3);

        JButton button4 = new JButton("B4");
        f.add(button4);

        JButton button5 = new JButton("B5");
        f.add(button5);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
```
#### GridLayout Beispiel 
Beim GridLayout sind die Elemente im wesentlichen wie in einer Tabelle angeordnet. Beim Erstellen gibt man an wieviele Reihen und Spalten man braucht.
Das `GridLayout` ist ein Layout-Manager in Java, der Komponenten in einem rechteckigen Raster anordnet. Jede Zelle des Rasters hat die gleiche Größe, und die Komponenten werden zeilenweise von links nach rechts hinzugefügt.

```java
f.setLayout(new GridLayout(3, 2));
```

### Daten einlesen und speichern
- in der GUI nutzen wir einen Swing Standard Dialog zur Dateiauswahl mit JFileChooser und showOpenDialog.
über getSelectedFile kann dann direkt drauf zugegriffen werden.

Zum anzeigen der - eingelesenen daten

### Zusammenfassung GUI

## GUI Grundlagen

### 1. Fenster
Der erste Schritt zur grafischen Benutzerschnittstelle ist ein Fenster, in dem dann später alle Elemente des Programms angezeigt werden. Hierzu wird ein JFrame-Objekt erzeugt und dann dessen Größe festgelegt. Zwar existiert das Fenster-Objekt nun, wird aber noch nicht auf dem Bildschirm angezeigt. Erst durch den Befehl `setVisible` wird es schließlich auch sichtbar.

### 2. Textfelder
Um der Benutzerschnittstelle ein erstes Element hinzuzufügen, erstellt man ein Objekt vom Typ `JTextArea` und fügt es dem Fenster über den Befehl `add` hinzu. Das Ergebnis ist ein Textfeld, das das gesamte Fenster ausfüllt und in das man nun etwas eingeben kann.

### 3. Buttons
Einen Button zu erstellen und dem Fenster hinzuzufügen, ist so einfach wie bei allen anderen Elementen. Es wird lediglich ein Objekt vom Typ `JButton` erstellt, dem Konstruktor wird als Parameter die Beschriftung übergeben und der Button wird zum Fenster hinzugefügt. So richtig sinnvoll wird ein Button aber natürlich erst, wenn auch etwas passiert, sobald man auf ihn klickt. Dafür muss dem Button ein sogenannter `ActionListener` hinzugefügt werden. Dieser enthält eine Funktion `actionPerformed`, die aufgerufen wird, sobald der Button angeklickt wird. Hier kann man beliebigen Programmcode ausführen.

### 4. Layout
Ein einzelnes Element zum Fenster hinzuzufügen, ist zwar die Grundlage für eine grafische Benutzerschnittstelle, aber natürlich nicht ausreichend. In der Regel besteht eine Oberfläche aus vielen verschiedenen Elementen. Diese korrekt anzuordnen – auch dann, wenn sich die Größe des Fensters verändert, weil der Benutzer es größer oder kleiner zieht –, ist gar nicht so einfach. Standardmäßig verwenden Swing-Programme das sogenannte `BorderLayout`, das den Bildschirm in fünf Bereiche teilt. Deutlich weniger strukturiert geht es im Vergleich dazu beim `FlowLayout` zu. Hier werden die Elemente einfach so lange in einer Reihe nebeneinander platziert, bis die Reihe voll ist. Dann geht es in der nächsten Reihe weiter. Das kann besonders dann praktisch sein, wenn sich die Größe eines Fensters verändert. Eine dritte Art des Layouts in Swing ist das sogenannte `GridLayout`, das im Wesentlichen wie eine Tabelle funktioniert. Beim Erstellen des `GridLayout` wird festgelegt, wie viele Reihen und Spalten das Layout haben soll, und jedes neu hinzugefügte Element wird dann in der nächsten leeren Zelle platziert.

## Multitasking

Für parallele Programmierung nutzt man Threads. Ein Thread ist ein Ausführungsstrang, der unabhängig von anderen Threads laufen kann. Dies ermöglicht es, mehrere Aufgaben gleichzeitig auszuführen.

### Threads in Java

#### Thread mit der `Runnable`-Schnittstelle
Die `Runnable`-Schnittstelle wird verwendet, um die Logik eines Threads zu definieren. Ein Thread wird dann mit einem `Thread`-Objekt gestartet.

```java
public class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Thread läuft: " + Thread.currentThread().getName());
    }

    public static void main(String[] args) {
        Thread thread = new Thread(new MyRunnable());
        thread.start();
    }
}
```

#### Thread mit der `Thread`-Klasse
Alternativ kann die `Thread`-Klasse erweitert werden, um einen eigenen Thread zu erstellen.

```java
public class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread läuft: " + getName());
    }

    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start();
    }
}
```

#### Wichtige Methoden der `Thread`-Klasse
- `start()`: Startet den Thread.
- `run()`: Enthält den Code, der im Thread ausgeführt wird.
- `sleep(milliseconds)`: Pausiert den Thread für die angegebene Zeit.
- `join()`: Wartet, bis ein anderer Thread beendet ist.
- `isAlive()`: Prüft, ob ein Thread noch läuft.

#### Beispiel: Mehrere Threads
```java
public class MultiThreadExample {
    public static void main(String[] args) {
        Runnable task = () -> {
            for (int i = 0; i < 5; i++) {
                System.out.println(Thread.currentThread().getName() + " - " + i);
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        };

        Thread thread1 = new Thread(task, "Thread 1");
        Thread thread2 = new Thread(task, "Thread 2");

        thread1.start();
        thread2.start();
    }
}
```

#### Synchronisation von Threads
Wenn mehrere Threads auf dieselbe Ressource zugreifen, kann es zu Problemen kommen. Die Synchronisation stellt sicher, dass nur ein Thread gleichzeitig auf eine kritische Sektion zugreifen kann.

```java
public class SynchronizedExample {
    private int counter = 0;

    public synchronized void increment() {
        counter++;
    }

    public static void main(String[] args) {
        SynchronizedExample example = new SynchronizedExample();

        Runnable task = () -> {
            for (int i = 0; i < 1000; i++) {
                example.increment();
            }
        };

        Thread thread1 = new Thread(task);
        Thread thread2 = new Thread(task);

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Endergebnis: " + example.counter);
    }
}
```
#### Locks und Deadlocks im Threading
Lock
Ein Lock ist ein Mechanismus um den zugriff auf eine resource zu synchronisieren - durch das lock kann nur ein thread darauf zugreifen.
In Java bietet die Klasse ReentrantLock eine erweiterte Kontrolle über den Zugriff auf kritische Abschnitte im Vergleich zu synchronized. ReentrantLock: Ein ReentrantLock erlaubt es einem Thread, denselben Lock mehrmals zu erwerben, ohne in einen Deadlock zu geraten. Der Lock muss jedoch genauso oft freigegeben (unlock()) werden, wie er erworben wurde (lock()).
```java
lock.lock();
lock.lock();
lock.unlock();
lock.unlock();
```

Deadlocks 
Gerade wenn mehrere Locks im Einsatz sind, besteht die Gefahr, dass ein sogenannter Deadlock entsteht. 
Ein Deadlock tritt auf, wenn zwei oder mehr Threads aufeinander warten, um Ressourcen freizugeben, und dadurch in einer Endlosschleife blockiert sind. 
Thread 1 hat etwas, das Thread 2 braucht
Thread 2 hat etwas, das Thread 1 braucht
beide warten aufeinander

Warum ist das schlimm?

Weil das Programm nicht abstürzt.
Es läuft weiter…
aber hängt.
CPU läuft
Programm reagiert nicht
Thread wartet für immer

#### Conditions
Conditions (Bedingungen) helfen, wenn Threads nicht nur geschützt, sondern auch in einer bestimmten Reihenfolge laufen sollen.
Condition gehört immer zu einem lock, weil man nur sicher warten kann, wenn man einen lock hat!
```java
Lock lock = new ReentrantLock();
Condition bedingung1 = lock.newCondition();
Condition bedingung2 = lock.newCondition();
```

await condition
```java
// TZhread bleibt stehen und wartet, bis die bedingung erfüllt ist
lock.lock();
try {
    bedingung1.await();
} finally {
    lock.unlock();
}
```
Wann immer die await condition ausgeführt wird, wartet das Programm  beim Ausführen an dieser Stelle so lange, bis es ein Signal erhält.

signal condition
weckt einen anderen thread auf

```java
bedingung1.signal();
```
signalAll()
Der signalAll-Befehl gehört zur Klasse Condition, die in Kombination mit einem Lock verwendet wird. Er wird verwendet, um alle wartenden Threads aufzuwecken, die auf eine bestimmte Bedingung warten.


```java
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class SignalAllExample {
    private final Lock lock = new ReentrantLock();
    private final Condition condition = lock.newCondition();
    private boolean ready = false;

    public void waitForSignal() {
        lock.lock();
        try {
            while (!ready) {
                System.out.println(Thread.currentThread().getName() + " wartet...");
                condition.await(); // Thread wartet auf die Bedingung
            }
            System.out.println(Thread.currentThread().getName() + " wurde aufgeweckt!");
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            lock.unlock();
        }
    }

    public void signalAllThreads() {
        lock.lock();
        try {
            ready = true; // Zustand ändern
            System.out.println("Alle Threads werden aufgeweckt...");
            condition.signalAll(); // Alle wartenden Threads aufwecken
        } finally {
            lock.unlock();
        }
    }

    public static void main(String[] args) {
        SignalAllExample example = new SignalAllExample();

        // Threads, die auf das Signal warten
        Runnable waitingTask = example::waitForSignal;

        Thread t1 = new Thread(waitingTask, "Thread 1");
        Thread t2 = new Thread(waitingTask, "Thread 2");
        Thread t3 = new Thread(waitingTask, "Thread 3");

        t1.start();
        t2.start();
        t3.start();

        // Signal senden, nachdem die Threads gestartet wurden
        try {
            Thread.sleep(1000); // Kurze Verzögerung, um sicherzustellen, dass alle Threads warten
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        example.signalAllThreads();
    }
}
```

#### Threads stoppen

Da threads oft in endlosschleife laufen, braucht man eine stop funktion
```java
public class StopbarerThread implements Runnable {
    private boolean stop = false;

    public void stop() {
        this.stop=true;
    }

    public void run() {
        while(!stop){}
    }
}
```
Die stop-Methode beendet einen Thread auf strukturierte Weise, indem sie ihm Zeit gibt, seine Ausführung zu beenden, während die interrupt-Methode eine schnelle, aber potenziell riskante Beendigung erzwingt, die zu Datenverlust führen kann.


### Beispiel: Thread mit interrupt beenden
```java
public class InterruptExample implements Runnable {
    @Override
    public void run() {
        try {
            while (!Thread.currentThread().isInterrupted()) {
                System.out.println("Thread läuft...");
                Thread.sleep(1000); // Simuliert Arbeit
            }
        } catch (InterruptedException e) {
            System.out.println("Thread wurde unterbrochen!");
        }
        System.out.println("Thread beendet.");
    }

    public static void main(String[] args) {
        Thread thread = new Thread(new InterruptExample());
        thread.start();

        try {
            Thread.sleep(3000); // Hauptthread wartet 3 Sekunden
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        thread.interrupt(); // Thread unterbrechen
    }
}
```




### Datenbankanbindung in java
ich nutze die derby tools von java

https://db.apache.org/derby/releases/release-10_17_1_0.cgi



### REST Schnittstellen

### REST-Schnittstellen und HTTP-Methoden

Während in Java Funktionsnamen verwendet werden, um auf verschiedene Funktionalitäten zuzugreifen, verwendet man bei REST-Schnittstellen hierfür verschiedene URLs, also Webadressen, und HTTP-Methoden. Die vier wichtigsten dieser Methoden sind:

| Methode | Auswirkung |
|---------|------------|
| GET     | Lädt eine Ressource vom Server, es werden keine Daten verändert. |
| POST    | Legt eine neue Ressource an. |
| PUT     | Ändert eine vorhandene Ressource. |
| DELETE  | Löscht eine Ressource auf dem Server. |

#### Entsprechung zu SQL

Jede der HTTP-Methoden hat eine mehr oder weniger genaue Entsprechung in SQL:

- **GET** entspricht etwa **SELECT**
- **POST** entspricht **INSERT**
- **PUT** entspricht **UPDATE**
- **DELETE** trägt sogar in beiden Fällen den gleichen Namen
