# 📘 Meine Java Notes – Woche 1

Um das Gelernte anzuwenden, notiere ich Lerninhalte, Beispiele und Reflektionen.
[TOC]

Tagesnotizen
## 🗓️ Tag 1 – Start Java Kurs / 

### Schwerpunkt: Entwicklungsumgebung einrichten und ankommen.

Ich habe mich entschlossen anstatt auf Intellij IDEA oder Eclipse bei VS Code zu bleiben.
Hierfür habe ich das neuste JDK installiert, die Umgebungsvariable gesetzt und die entsprechende Extension in VS Code installiert (ich habe mich hier für das extension pack für Java von Microsoft entschieden, da es bereits Java IntelliSense, debugging, testing, Maven/Gradle support, project management und mehr beinhaltet).
Das Theorieskript besagt, dass eine Besonderheit von Java die strikte Typisierung und Objektorientierung sei.


Ich habe eine entsprechende Ordnerstruktur geschaffen:

java/
  src/
    main/
      java/
  bin/
Das erste Java File angelegt: [Hello World](java\src\main\java\exercises\Test.java). Das sieht zumindest schon vielversprechend aus.
Danach habe ich auch die .vscode JSON so angepasst, dass die Javasettings gelesen werden können:
```json

{
    "python.analysis.autoImportCompletions": true,
    "python.testing.pytestArgs": [
        "python"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "java.project.outputPath": "java/bin",
    "java.project.sourcePaths": [
        "java/src/main/java"
    ]
}

```

Danach musste ich den Java Language Server neu starten, denn wenn der Java‑Server den falschen Root nimmt, erwartet er java.src.main.java.exercises. Mit sourcePaths sagst du ihm, dass src/main/java der Root ist.

Danach kam eine Fehlermeldung:
```bash
...java\src\main\java\exercises\" && javac Test.java && java Test
Fehler: Hauptklasse Test konnte nicht gefunden oder geladen werden
Ursache: java.lang.NoClassDefFoundError: Test (wrong name: exercises/Test)
```


Daraufhin habe ich das Kommando hinter dem Run Button von VS Code neu konfiguriert durch eine tasks.json im .vscode-Ordner des Repos. 

Dies, so hoffte ich würde ändern, dass zum richtigen Startpunkt navigiert wird.

Beim Ausführen gab es aber wieder Fehlermeldungen, so dass ich die task.json verworfen habe. Durch Trial and Error kam ich dann darauf: Das Problem wurde dadurch verursacht, dass das Java-File im Exercises Ordner lag, so habe ich in der Settings den Path entsprechend zu "java/src/main/java/exercises" angepasst. Ich habe daraufhin den Package-Verweis gelöscht und die settings.json so belassen. Ich musste VS Code neustarten, damit die Änderungen auf dem Workspace wirksam waren. Nun kann ich Run Code und Run Java in VS Code nutzen ohne Fehlermeldung und mit der gewünschten Ordnerstruktur. Und ich kann den Rest des repositories in VSCode geöffnet lassen um ggfls querverweise zu haben oder zu vergleichen.
Ich muss halt schauen, wenn der exercise ordner nun source root ist, muss ich entweder später packages anlegen falls ich die source ändere, oder die unterschiedlichen aufgaben wie Prüfungen auch im exercises ordner ablegen.


### Das Erste Programm

Der erstellte src-Ordner dientnun als Speicherplatz für den Quelltext des Programms.
Es ist wichtig, dass der Klassenname dem Dateinamen entspricht, 
damit die Java-Compiler und -Laufzeitumgebung die Klasse korrekt erkennen und ausführen können. 

```java

public class Test {
    public static void main(String[] args) {
        System.out.println("Hello, World, I hope my Java Setup will work!");
    }
}

```
Die geschweiften Klammern ({,})markieren in Java sogenannte Anweisungblöcke, 
also Teile des Quelltexts, die zusammengehören.
In Java ist die main-Methode der Einstiegspunkt für die Ausführung eines Programms.
Sie muss immer die folgende Signatur haben: public static void main(String[] args)
Java-Quellcode wird vom Compiler zu Bytecode übersetzt. Je nach IDE läuft das unterschiedlich ab, aber am Ende kommt immer das Gleiche raus: eine .class-Datei mit dem Bytecode, den die Java Virtual Machine dann ausführt.


### Package, Klassenpfad und source root

**Package (Namespace)**
Ein Package ist der logische „Nachname“ einer Klasse. Es organisiert Klassen und verhindert Namenskonflikte.
Wenn oben steht package exercises;, dann heißt die Klasse technisch gesehen exercises.Test.
Wichtig: Der Package-Name muss exakt der Ordnerstruktur entsprechen.

**Source Root**
Der Source Root ist der Startpunkt der Paketstruktur. Alles unterhalb dieses Ordners wird als Package interpretiert.
Wenn src/main/java mein Source Root ist und darin ein Ordner exercises liegt, dann entspricht dieser Ordner dem Package exercises.
Der Source Root selbst gehört nicht zum Package-Namen.

**Classpath**
Der Classpath ist der Suchpfad der JVM beim Ausführen. Er sagt: „In diesen Ordnern oder JAR-Dateien darfst du nach kompilierten Klassen suchen.“
Wenn meine kompilierte Klasse als bin/exercises/Test.class liegt, muss bin im Classpath stehen. Dann kann Java exercises.Test finden und starten.

Kurz zusammengefasst:
Package = logischer Name
Source Root = Startpunkt der Paketstruktur
Classpath = Suchpfad beim Ausführen

### Variablen
In Java ist eine Variable ein benannter Speicherplatz, in dem ein Wert abgelegt wird. Jede Variable muss vor der Verwendung deklariert werden, wobei immer der Typ und der Name angegeben werden. Der Typ legt fest, welche Art von Werten gespeichert werden darf, zum Beispiel int für ganze Zahlen, double für Kommazahlen oder String für Texte. Java ist strikt typisiert, das bedeutet: Der Typ ist verpflichtend und kann nicht nachträglich automatisch geändert werden. Bemerkenswert ist, dass bei der Deklaration des Strings hier ein uppercase vonnöten ist. Dies lisgt daran,. das String Methoden hat, weil es eine Klasse ist. Objekte und Klassen werden am Anfang Grpß geschrieben.

```java
int alter = 30;
String name = "Matthias";
double kontostand = 105.75;
```
Der Variablenname darf aus Buchstaben, Zahlen und Unterstrichen bestehen, darf aber nicht mit einer Zahl beginnen. Üblicherweise werden Variablennamen kleingeschrieben und bei mehreren Wörtern im sogenannten CamelCase notiert, etwa kontoStand oder ausgabeText.

### Datentypen
Zahlen, Wahrheitswerte und Texte.
Zahlen:
| Datentyp | Zahlenart | Wertebereich |
|----------|-----------|--------------|
| `byte` | Ganzzahl | -128 bis 127 |
| `short` | Ganzzahl | -32.768 bis 32.767 |
| `int` | Ganzzahl | -2.147.483.648 bis 2.147.483.647 |
| `long` | Ganzzahl | -9.223.372.036.854.775.808 bis 9.223.372.036.854.775.807 |
| `float` | Kommazahl | -3,40282347 × 10³⁸ bis 3,40282347 × 10³⁸ |
| `double` | Kommazahl | -1,7976931348623157 × 10³⁰⁸ bis 1,7976931348623157 × 10³⁰⁸ |

Deklaration:
```java
byte a;
short b;
int c;
long d;

float e;
double f;
```
Texte
Sogenannte char-Variablen können genau ein Zeichen repräsentieren. Die kann man zur Speicherplatzreduktion nutzen. 
```java
char c;
c = 'x';
c = '7'; 
c = '!';
```
Sobald etwas in doppelten Anführungszeichen steht wird es als String interpretiert.

Wahrheitswerte

Wie gehabt true oder false.
Wertzuweisung für Bool'sche Variablen:
```java
boolean a;
a = true;
a = false;
```

### Operatoren
#### Arithmetische Operatoren
| Operator | Bedeutung | Beispiel | Ergebnis (Beispiel) |
|---|---|---|---|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraktion | `5 - 3` | `2` |
| `*` | Multiplikation | `5 * 3` | `15` |
| `/` | Division (Ganzzahldivision bei `int`) | `5 / 2` | `2` (bei `int`), `2.5` (bei `double`) |
| `%` | Modulo (Rest) | `5 % 2` | `1` |
| `++` | Inkrement (um 1 erhöhen) | `int x = 5; x++;` | `x` wird `6` |
| `--` | Dekrement (um 1 verringern) | `int x = 5; x--;` | `x` wird `4` |

#### String Konkatenation

Unter String-Konkatenation versteht man das Zusammenfügen mehrerer Zeichenketten zu einem neuen String. In Java geschieht dies mit dem `+`-Operator. Dabei können sowohl String-Variablen als auch String-Literale (Text in Anführungszeichen) miteinander verknüpft werden. Java wandelt dabei automatisch auch andere Datentypen wie Zahlen oder Wahrheitswerte in Strings um, wenn sie mit einem String verbunden werden. Dies macht die Konkatenation sehr flexibel für die Ausgabe und Formatierung von Texten.

```java
String a = "Hallo ";
String b = "Welt";
String c = a + b + "!";  // Ergebnis: "Hallo Welt!"

// Automatische Konvertierung anderer Typen:
String text = "Alter: " + 30;  // Ergebnis: "Alter: 30"
String ergebnis = "Summe: " + (5 + 3);  // Ergebnis: "Summe: 8"
```
#### Boolsche Operatoren

Boolesche Operatoren (auch logische Operatoren genannt) verknüpfen Wahrheitswerte miteinander und liefern als Ergebnis wieder einen boolean-Wert. Die wichtigsten Operatoren sind `&&` (logisches UND), `||` (logisches ODER) und `!` (logische Negation). Mit `&&` ist das Ergebnis nur dann `true`, wenn beide Operanden `true` sind. Bei `||` reicht es, wenn mindestens ein Operand `true` ist. Der `!`-Operator kehrt einen Wahrheitswert um. Diese Operatoren sind essentiell für Bedingungen und Kontrollstrukturen, um komplexe Entscheidungen im Programmablauf zu treffen.

```java
boolean a = true;
boolean b = false;

// UND-Verknüpfung (&&): beide müssen true sein
boolean c = a && b;  // Ergebnis: false
boolean d = true && true;  // Ergebnis: true

// ODER-Verknüpfung (||): mindestens einer muss true sein
boolean e = a || b;  // Ergebnis: true
boolean f = false || false;  // Ergebnis: false

// Negation (!): kehrt den Wert um
boolean g = !a;  // Ergebnis: false
boolean h = !b;  // Ergebnis: true
```


#### Wahrheitstafeln (mit 0 und 1)

AND (`&&`)
| A | B | A && B |
|---|---|--------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

OR (`||`)
| A | B | A \|\| B |
|---|---|----------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

XOR (`^`) (Entweder oder, nicht beides gleichzeitig)
| A | B | A ^ B |
|---|---|-------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

NOT (`!`)
| A | !A |
|---|----|
| 0 | 1 |
| 1 | 0 |

### Typumwandlung

Typumwandlung (Type Casting) bezeichnet die Konvertierung eines Wertes von einem Datentyp in einen anderen. In Java gibt es zwei Arten: 

**Implizite (automatische) Typumwandlung (Widening):** Diese erfolgt bei verlustfreien Konvertierungen, etwa von `int` nach `double` oder von `byte` nach `int`, da alle Werte des kleineren Typs problemlos im größeren Typ dargestellt werden können. Java führt diese Umwandlung automatisch durch, da keine Information verloren geht.

**Explizite Typumwandlung (Narrowing/Casting):** Wenn der Verlust von Genauigkeit und damit von Information droht, ist eine explizite Umwandlung nötig. Diese wird durch Voranstellen des Zieldatentyps in Klammern durchgeführt, z.B. `(int)`. Bei der Umwandlung von `double` zu `int` werden die Nachkommastellen einfach **abgeschnitten**, nicht gerundet. Aus `7.9` wird also `7`, nicht `8`!

Für die Umwandlung primitiver Typen in Strings verwendet man `String.valueOf()`, für die umgekehrte Richtung die entsprechenden Wrapper-Klassen wie `Integer.valueOf()` oder `Double.valueOf()`.

```java
// Implizite Typumwandlung (Widening) - automatisch
int i = 3;
double d = i;  // automatisch: int → double (Ergebnis: 3.0)

byte b = 100;
int j = b;  // automatisch: byte → int

// Explizite Typumwandlung (Narrowing) - manuell erforderlich
double x = 7.9;
int y = (int) x;  // manuell: double → int (Ergebnis: 7, NICHT 8!)

float f = 3.14f;
double dd = f;  // erlaubt: float → double
// float ff = dd;  // Fehler! Explizites Casting nötig:
float ff = (float) dd;  // OK

// Umwandlung zu/von String
int zahl = 7;
String s = String.valueOf(zahl);  // "7"

String text = "42";
int nummer = Integer.valueOf(text);  // 42
double komma = Double.valueOf("3.14");  // 3.14
```


### Nutzereingaben


    Ziel: Nutzereingaben in Java über die Konsole einlesen.
    Tool dafür: Scanner aus java.util.Scanner (muss importiert werden).
    Setup: Scanner scanner = new Scanner(System.in); → liest von der Konsole (System.in).
    Ablauf: Erst Nutzer per System.out.println(...) zur Eingabe auffordern, dann mit scanner.next() den nächsten eingegebenen Wert einlesen und z. B. in String name speichern.
    Wichtig: scanner.next() liefert grundsätzlich Text (String). Für Rechnen müssen Eingaben in Zahlen umgewandelt werden (z. B. zu int/Integer), sonst passiert bei "15" + "16" eine String-Verkettung ("1516") statt Addition (31).
    Ausgabe: Zahlen-Ergebnisse ggf. wieder zu String umwandeln, um sie sauber auszugeben.


---
Kurze Zusammenfassung

Was war heute Schwerpunkt? Kurzer Überblick über Thema, Übungen oder Theorie.

Learningfacts:

…

…

…

Beispiele / Code:

// Beispielcode oder Demo


Was ich morgen lernen will:

…

🗓️ Tag 2 – Thema / Schwerpunkt

Learningfacts:

…

…

Übungsaufgabe / Beispiel:

// Beispiel oder Übung


Reflexion:

…

Was ich morgen lernen will:

…

Tag 3 – Thema / Schwerpunkt

Learningfacts:

…

…

Codebeispiele:

// Beispielcode


Was ich morgen lernen will:

…

Kompetenzprotokoll Woche X

Ziel: Das Gelernte in vier Kategorien reflektieren, um Theorie, Praxis und Relevanz zu verknüpfen.

1️⃣ Einordnen & Strukturieren (Theorie erklären)

…

2️⃣ Verstehen & Verknüpfen (Praxisbeispiel erläutern)

…

3️⃣ Anwenden & Bewerten (Berufliche Relevanz erörtern)

…

4️⃣ Reflektieren & Hinterfragen (Lernprozess reflektieren / Fragen formulieren)

…

Offene Fragen:

…

…

🧩 Zusammenfassung der Woche

Wichtigste Erkenntnisse:

…

…

Tools / Konzepte, die ich neu verstanden habe:

…

…

Schwierigkeiten / To-do für nächste Woche:

…

…

💡 Nächste Woche – Fokus / Lernziele

…

…

…