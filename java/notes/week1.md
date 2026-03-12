# 📘 Meine Java Notes – Woche 1

Um das Gelernte anzuwenden, notiere ich Lerninhalte, Beispiele und Reflektionen.


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
In Java ist eine Variable ein benannter Speicherplatz, in dem ein Wert abgelegt wird. Jede Variable muss vor der Verwendung deklariert werden, wobei immer der Typ und der Name angegeben werden. Der Typ legt fest, welche Art von Werten gespeichert werden darf, zum Beispiel int für ganze Zahlen, double für Kommazahlen oder String für Texte. Java ist strikt typisiert, das bedeutet: Der Typ ist verpflichtend und kann nicht nachträglich automatisch geändert werden. Bemerkenswert ist, dass bei der Deklaration des Strings hier ein uppercase vonnöten ist. Dies liegt daran, dass String Methoden hat, weil es eine Klasse ist. Objekte und Klassen werden am Anfang Groß geschrieben.

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


### Vergleichsoperatoren

| Operator | Symbol | Beispiel | Ergebnis (Beispiel) |
|----------|--------|----------|-------------------|
| Kleiner-als | `<` | `5 < 10` | `true` |
| Größer-als | `>` | `5 > 10` | `false` |
| Gleich | `==` | `5 == 5` | `true` |
| Kleiner-gleich | `<=` | `5 <= 5` | `true` |
| Größer-gleich | `>=` | `10 >= 5` | `true` |
| Ungleich | `!=` | `5 != 10` | `true` |

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

Beispiel:
```java
// ich möchte den quotienten von zwei integer zahlen zahl_1 und zahl_2 ausrechnen
float quotient = zahl_1 / (float) zahl_2;
```
In Java wird automatisch eine sogenannte "Type Promotion" durchgeführt: Wenn einer der beiden Operanden float ist, wird der andere automatisch auch zu float konvertiert.

Deshalb reicht ein Cast aus:

zahl_1 / (float) zahl_2 → Java konvertiert zahl_1 automatisch zu float
Das Ergebnis ist float
Mit beiden Casts:

(float) zahl_1 / (float) zahl_2 → funktioniert auch, aber der zweite Cast ist redundant
Es ist also eine Frage der Code-Effizienz und Lesbarkeit: Man schreibt nur das Minimum, das nötig ist. Ein Cast reicht vollkommen aus, um das Ergebnis mit Dezimalstellen zu bekommen.

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
Erste Programme mit Java. 
VSCode stabil einrichten mit Java


Learningfacts:


String ist eine Klasse und wird bei Datentypangabe daher am Anfang groß geschrieben
Der Compiler ist eine Diva. Empfindlich und schnell eingeschnappt.

…

…
### If Verzweigung
```java
if(true){
 
}
// beispiel anweisung
        if (passwort.equals(geheimesPasswort)) {
            System.out.println("Passwort korrekt");
        } else {
            System.out.println("Passwort falsch");
        }

//dies kann aber auch mit else if gelöst werden:

        if(passwort.equals("passwort")){
            System.out.println("Passwort korrekt");
        } else if (passwort.equals(„admin“)){
            System.out.println("AdminPasswort korrekt");
        } else {
            System.out.println("Passwort falsch");
        }
```

### switch case verzweigung

Die `switch-case`-Verzweigung eignet sich besonders, wenn eine Variable auf **Gleichheit** mit mehreren festen Werten geprüft werden soll.

**Wichtige Merkmale:**
- Funktioniert nur mit: `byte`, `short`, `int`, `char` und `String`
- Jeder `case` endet mit `break;`, sonst wird der nächste `case` auch noch ausgeführt
- `default` ist wie `else` – wird ausgeführt, wenn kein `case` zutrifft
- Vergleicht nur auf Gleichheit (kein `<`, `>`, etc.)

**Beispiel: Monatsnamen zuordnen**

```java
int monat = 6;
String nameMonat;

switch(monat) {
    case 1: nameMonat = "Januar"; break;
    case 2: nameMonat = "Februar"; break;
    case 3: nameMonat = "März"; break;
    case 4: nameMonat = "April"; break;
    case 5: nameMonat = "Mai"; break;
    case 6: nameMonat = "Juni"; break;
    case 7: nameMonat = "Juli"; break;
    case 8: nameMonat = "August"; break;
    case 9: nameMonat = "September"; break;
    case 10: nameMonat = "Oktober"; break;
    case 11: nameMonat = "November"; break;
    case 12: nameMonat = "Dezember"; break;
    default: nameMonat = "Ungültiger Monat"; break;
}

System.out.println(nameMonat); // Output: Juni
```

**Merke:** `switch-case` ist kürzer und übersichtlicher als viele `if-else-if`-Blöcke!

### Schleifen

### while-Schleife

Die `while`-Schleife **wiederholt einen Code-Block, solange eine Bedingung erfüllt ist**.

**Syntax:**
```java
while(bedingung) {
    // Code wird wiederholt, solange bedingung = true
}
```

**Wichtig:**
- Nach dem Rumpf springt die Schleife zurück zur Bedingung (nicht wie `if`, das endet)
- **Laufvariable (Counter)** zum Zählen verwenden: `int i = 0;`
- **Immer hochzählen** (`i++` oder `i += 1;`), sonst: Endlosschleife!
- Programmierung beginnt bei 0: `while(i < 3)` = 3 Durchläufe (0, 1, 2)

**Beispiel: 3x "Durchlauf" ausgeben**
```java
int i = 0;
while(i < 3) {
    System.out.println("Durchlauf");
    i = i + 1;  // oder: i++
}
```

**Beispiel: Passwort mit Versuche-Limit**
```java
String passwort = "";
int versuche = 0;

while(!passwort.equals("geheim") && versuche < 3) {
    System.out.println("Passwort eingeben:");
    passwort = scanner.next();
    versuche++;
}

if(passwort.equals("geheim")) {
    System.out.println("Korrekt!");
} else {
    System.out.println("Zu viele Versuche!");
}
```

### do-while-Schleife

Die `do-while`-Schleife ist **fußgesteuert**: Sie führt den Code **mindestens einmal aus**, prüft die Bedingung erst danach.
- `while`: **kopfgesteuert** (prüft zuerst, führt dann aus)
- `do-while`: **fußgesteuert** (führt aus, prüft dann)

**Syntax:**
```java
do {
    // Code wird MINDESTENS einmal ausgeführt
} while(bedingung);  // Achtung: Semikolon!
```

**Beispiel: Einmal mindestens ausführen**
```java
int i = 100;
do {
    System.out.println("Durchlauf");
    i += 1;
} while(i < 5);  // i ist niemals < 5, aber Rumpf läuft einmal trotzdem!
// Output: Durchlauf (nur 1x!)
```

**Beispiel: Passwort-Eingabe (perfekt dafür!)**
```java
String passwort;
do {
    System.out.println("Passwort eingeben:");
    passwort = scanner.next();
} while(!passwort.equals("geheim"));
// Nutzer MUSS mindestens einmal eingeben!
```

### for-Schleife

Die `for`-Schleife ist **kopfgesteuert** und eine **Zählschleife**: Sie hat die Laufvariable direkt im Kopf eingebaut – übersichtlicher als `while`!

**Syntax:**
```java
for(initialisierung; bedingung; änderung) {
    // Code wird wiederholt
}
```

**Die 3 Teile (durch Semikolon getrennt):**
1. **Initialisierung**: `int i = 0` – Laufvariable deklarieren und starten
2. **Bedingung**: `i < 3` – Wann soll die Schleife laufen?
3. **Änderung**: `i++` – Wie ändert sich die Variable pro Durchlauf?

**Beispiel: 3x "Durchlauf" ausgeben**
```java
for(int i = 0; i < 3; i++) {
    System.out.println("Durchlauf");
}
// Output: Durchlauf (3x: bei i=0, 1, 2)
```

**Beispiel: Arrays durchlaufen**
```java
String[] farben = {"Rot", "Grün", "Blau"};
for(int i = 0; i < farben.length; i++) {
    System.out.println(farben[i]);
}
```

**Merke:** `i++` ist Kurzform für `i += 1` oder `i = i + 1`


### Funktionen

```Java
public static void funktion1(String s, int i){
    System.out.println(s);
    System.out.println(String.valueOf(i));
    }

```
Diese funktion hat Parameter. 
Der Wert der Parameter wird beim Aufruf der Funktion übergeben.

Die Funktion kann Informationen an die Aufrufende Stelle zurückgeben, den Rückgabewert.

im obigen beispiel ist der rückgabewert nicht angegeben, stattdessen void.

```java
//Funktionen mit Rückgabewert
public static String funktion1(){
    return "Test-String";
    }

public static int funktion2(int i){
    int j = 2+ i;
    return j;
    }
```
Der returnbefehl beendet die Funktionsausführung.
---

🗓️ Tag 5 – Thema OOP/ Klassen
In der objektorientierten Programmierung fasst man Dinge mit gleichen Eigenschaften und Verhalten in Klassen zusammen. Das reduziert Redundanz. Objekte sind Instanzen einer Klasse.

Klassen besitzen Attribute und Methoden.
Beispiel „Flasche“:
- Methoden: füllen, leeren
- Attribute: Größe, Farbe, geschlossen/offen

Wichtig ist, nur die Eigenschaften zu modellieren, die im Programm wirklich relevant sind.

```java
class Kunde {
    String vorname;
    String nachname;
    String strasse;
    int hausnummer;
    int plz;
    String ort;

    public Kunde(String vn, String nn, String str, int nummer, int p, String o) {
        vorname = vn;
        nachname = nn;
        strasse = str;
        hausnummer = nummer;
        plz = p;
        ort = o;
    }
}
```

Um eine Instanz einer Klasse zu erzeugen, benötigt man einen Konstruktor. Er wird beim Erstellen des Objekts aufgerufen und initialisiert dessen Zustand.

Ein Konstruktor hat keinen Rückgabewert (auch kein `void`). Das Objekt wird mit dem Schlüsselwort **new** erzeugt, die Werte in den Klammern sind die Argumente für den Konstruktor.

```java
// Wenn ein Kunde erstellt wird, dann speichere die übergebenen Werte in die passenden Felder.
Kunde kunde1 = new Kunde("Max", "Mustermann", "Musterstraße", 1, 12345, "Musterstadt");
```

möchte man die Objekterzeugung in der gleichen datei haben, muss die main methode innerhalb der Klassenklammern stehen und die Objekterzeugung dann innerhalb einer methode (z.B. in der main).
beispiel in: [Dieser Datei](java\src\main\java\exercises\Kunde.java).



Learningfacts:
Objektorientierung bedeutet:

Du erstellst Baupläne (Klassen),
baust daraus konkrete Dinge (Objekte),
diese Dinge haben eigene Daten (Attribute)
und können etwas tun (Methoden).

### 6.4 Zugriffsrechte (Zusammenfassung)
In Java unterscheiden sich public und private Methoden (Funktionen) durch ihre Sichtbarkeit:
public: Die Methode ist von überall aufrufbar, also auch aus anderen Klassen und Paketen.
private: Die Methode ist nur innerhalb derselben Klasse aufrufbar.

Damit Abstraktion in Klassen funktioniert, sollten Attribute nicht direkt von außen verwendet werden (z. B. `k1.strasse`). Wenn sich interne Felder ändern oder wegfallen, müsste sonst externer Code überall angepasst werden.

Mit dem Schlüsselwort `private` wird der direkte Zugriff von außerhalb der Klasse verhindert - sowohl bei Attributen als auch bei Methoden. `public` bedeutet dagegen: von außen erreichbar.

```java
class A {
    private int a;
    public int b;

    private void func() {
    }
}
```

Private Attribute sind wichtig für Datenqualität: Werte können über kontrollierte Methoden gelesen oder gesetzt werden. Dafür nutzt man Getter und Setter, z. B. `getHausnummer()`, `setHausnummer()`, `getPlz()` und `setPlz()`. So kann man beim Setzen prüfen, ob Werte gültig sind (z. B. Hausnummer nicht negativ).

```java
public class Konto {
    public void einzahlen(double betrag) {   // von außen nutzbar
        pruefeBetrag(betrag);
    }

    private void pruefeBetrag(double betrag) { // nur intern in Konto nutzbar
        if (betrag <= 0) {
            throw new IllegalArgumentException("Betrag muss > 0 sein");
        }
    }
}
// Hier kann man einzahlen(...) von außen aufrufen, pruefeBetrag(...) aber nicht.
```

Merksatz:
public = Teil der Außen-Schnittstelle,
private = interne Hilfslogik/Kapselung.


### Arrays in Java

Ein Array ist in Java wie ein Regal mit festen Fächern:

Es hat eine feste Größe (z. B. 5 Plätze).
Jeder Platz hat einen Index, startend bei 0.
Alle Plätze enthalten den gleichen Datentyp (nur int, nur String, usw.).

String <-> Array umwandeln
String.join(",", arr) macht aus einem String-Array einen Text.
"Max Moritz".split(" ") macht aus einem Text ein Array.
System.out.println(array) zeigt nicht die Inhalte schön an, sondern so etwas wie [Ljava.lang.String;@....
Für schöne Ausgabe: Schleife oder Arrays.toString(array).

Mehrdimensionale Arrays
String[][] raster ist ein Array aus Arrays (z. B. wie ein Raster/Bild).
Zugriff: raster[x][y].
In Java dürfen innere Arrays unterschiedlich lang sein (sog. „jagged array“).


Startparameter main(String[] args)
Beim Programmstart kannst du Werte übergeben.
Diese landen in args[0], args[1], ...
Gut für feste Start-Einstellungen (z. B. Port, Modus).

Syntax bei Arrayeigenschaften: array.length (kein ())

Automatische Standardwerte
int[] startet mit 0, boolean[] mit false, Objekt-Arrays mit null.
Bounds-Check zur Laufzeit
Ungültiger Index wirft sofort ArrayIndexOutOfBoundsException

Objekt-Arrays können null enthalten -> NullPointerException möglich.
array1 == array2 vergleicht Referenzen, nicht Inhalte.

For-each bei primitiven/Strings ändert oft nicht das Original, wenn du nur die Schleifenvariable neu setzt.

```java
for (String element : spalte) {
    element = "schwarz"; // aendert NICHT das Array selbst
}
```

Richtig wäre mit Index:
```java
for (int i = 0; i < spalte.length; i++) {
    spalte[i] = "schwarz";
}
```


### Listen in Java

Bei Arrays ist die Größe fest.
Bei Listen kann die Größe wachsen und schrumpfen.
Du kannst Elemente hinzufügen, ändern und wirklich löschen.

Elemente löschen
Nach Index: liste.remove(1) loescht das Element an Position 1.
Nach Wert: liste.remove("Wert2") loescht das erste passende Element.
Bei remove(Wert) bekommst du true/false zurueck: gefunden oder nicht.

Elemente aendern
Mit set(index, neuerWert), z. B. liste.set(0, "Neu").

Elemente tauschen
Manuell mit Zwischenspeicher (get + set).
Einfacher: Collections.swap(liste, 0, 1).

Listen durchlaufen
```java
// Mit Index-Schleife:
for (int i = 0; i < liste.size(); i++)

// Mit For-Each:
for (String s : liste)
```
Wichtig bei Aenderung waehrend Schleife
Wenn du waehrend des Durchlaufs loeschst/hinzufuegst, kann sich size() aendern.
Dann kann die Schleife frueher enden oder unerwartet laufen.


ArrayList vs LinkedList
ArrayList: besser bei haeufigem Lesen/Aendern per Index.
LinkedList: besser bei haeufigem Einfuegen/Loeschen.
In kleinen Programmen merkt man den Unterschied oft kaum.


Merksatz

Array = schnell und fest.
List = flexibel und alltagstauglich.
Meistens startet man in Java mit ArrayList, ausser es gibt einen klaren Grund fuer LinkedList

### public/private/static

In Java regeln diese Schlüsselwörter, **wer auf was zugreifen darf** und **ob etwas zur Klasse oder zum Objekt gehört**.

#### `public`

`public` bedeutet, dass auf eine Klasse, Methode oder Variable von außen zugegriffen werden darf.

- Eine `public`-Methode kann von anderen Klassen aufgerufen werden.
- Eine `public`-Klasse kann von anderen Klassen verwendet werden.

Beispiel:

```java
public void zeigeDetails() {
```

Diese Methode kann von außerhalb der Klasse aufgerufen werden.

#### `private`

`private` bedeutet, dass auf eine Variable oder Methode nur innerhalb derselben Klasse zugegriffen werden darf.

- Andere Klassen können nicht direkt auf `private` Attribute zugreifen.
- Das wird genutzt, um Daten zu schützen (Kapselung).

Beispiel:

```java
private String marke;
```

Die `marke` kann nur innerhalb der Klasse gelesen oder verändert werden.

#### `static`

`static` bedeutet, dass etwas zur **Klasse** gehört und nicht zu einem einzelnen Objekt.

- Normalerweise braucht man ein Objekt, um eine Methode aufzurufen.
- Bei `static` braucht man kein Objekt.

Beispiel:

```java
public static void main(String[] args)
```

Die `main`-Methode ist `static`, weil sie von Java aufgerufen wird, bevor ein Objekt existiert.

Man verwendet `static` z. B. für:

- die `main`-Methode
- Hilfsmethoden
- Konstanten
- Dinge, die für alle Objekte gleich sind

**Merksatz:**

- `public` = von überall erreichbar
- `private` = nur in dieser Klasse erreichbar
- `static` = gehört zur Klasse, nicht zum Objekt
…


### Java Exceptions

| Fehlerklasse | Bedeutung |
|---|---|
| `ArithmeticException` | Unzulässige arithmetische Operation, zum Beispiel Teilen durch `0` |
| `ArrayIndexOutOfBoundsException` | Zugriff auf einen nicht vorhandenen Index eines Arrays |
| `ClassCastException` | Versuch, ein Objekt zu einer Klasse umzuwandeln, zu der es nicht gehört |
| `Exception` | Oberklasse aller Fehler, die universell alle auftretenden Fehler auffängt |
| `FileNotFoundException` | Eine Datei, auf die zugegriffen werden soll, kann nicht gefunden werden |
| `IllegalArgumentException` | Übergabe eines unzulässigen Arguments an eine Funktion |
| `IndexOutOfBoundsException` | Zugriff auf einen nicht vorhandenen Index, zum Beispiel bei einer Liste |
| `IOException` | Fehler beim Lesen oder Schreiben von Dateien oder Ordnern |
| `NullPointerException` | Ein Objekt, auf das zugegriffen wird, hat unerwartet den Wert `null` |
| `NumberFormatException` | Versuch, einen String in eine Zahl umzuwandeln, der keine Zahl darstellt |


### try / catch / finally

Mit `try`, `catch` und `finally` kann man in Java auf Fehler kontrolliert reagieren.

Der `try`-Block enthält den Code, in dem ein Fehler auftreten kann.
Im `catch`-Block wird festgelegt, **welcher Fehler abgefangen werden soll** und was dann passieren soll.
Der `finally`-Block wird am Ende immer ausgeführt, egal ob ein Fehler aufgetreten ist oder nicht.

Kurz gesagt:

- `try` = hier könnte etwas schiefgehen
- `catch` = hier reagiere ich auf den Fehler
- `finally` = das wird zum Schluss auf jeden Fall noch ausgeführt

Beispiel:

```java
try {
    int ergebnis = 10 / 0;
    System.out.println(ergebnis);
} catch (ArithmeticException e) {
    System.out.println("Fehler: " + e.getMessage());
} finally {
    System.out.println("Dieser Block wird immer ausgeführt.");
}
```

Wichtig ist:

- Ohne Fehler läuft der Code im `try` ganz normal durch.
- Bei einem Fehler springt Java direkt in den passenden `catch`-Block.
- `finally` eignet sich z. B. für Aufräumarbeiten wie das Schließen von Dateien oder Scannern.

Merksatz:

Erst versuche ich etwas mit `try`, dann fange ich mögliche Fehler mit `catch` ab und am Ende räume ich mit `finally` auf.



### Abstrakte Klassen

In Java sind abstrakte Klassen eine Art Blaupause für andere Klassen. Sie können nicht direkt instanziiert werden, sondern dienen als Grundlage für Unterklassen, die von ihnen erben. Abstrakte Klassen werden mit dem Schlüsselwort `abstract` deklariert.

#### Eigenschaften einer abstrakten Klasse:
- **Abstrakte Methoden:**
  Abstrakte Klassen können Methoden enthalten, die keine Implementierung haben. Diese Methoden müssen von den Unterklassen überschrieben werden. Sie werden ebenfalls mit dem Schlüsselwort `abstract` deklariert.

- **Normale Methoden:**
  Neben abstrakten Methoden können abstrakte Klassen auch normale Methoden mit einer Implementierung enthalten.

- **Attribute:**
  Abstrakte Klassen können Attribute definieren, die von den Unterklassen geerbt werden.

- **Konstruktoren:**
  Abstrakte Klassen können Konstruktoren haben, die von den Unterklassen aufgerufen werden, um gemeinsame Attribute zu initialisieren.

- **Nicht instanziierbar:**
  Eine abstrakte Klasse kann nicht direkt instanziiert werden. Sie muss durch eine konkrete (nicht-abstrakte) Unterklasse erweitert werden.

#### Beispiel:
```java
// Abstrakte Klasse
abstract class Fahrzeug {
    String marke;
    String modell;

    public Fahrzeug(String marke, String modell) {
        this.marke = marke;
        this.modell = modell;
    }

    // Abstrakte Methode
    abstract double berechneReichweite();

    // Normale Methode
    public String anzeigenInformationen() {
        return "Marke: " + marke + ", Modell: " + modell;
    }
}

// Konkrete Unterklasse
class Elektroauto extends Fahrzeug {
    double batteriekapazitaet;

    public Elektroauto(String marke, String modell, double batteriekapazitaet) {
        super(marke, modell);
        this.batteriekapazitaet = batteriekapazitaet;
    }

    @Override
    double berechneReichweite() {
        return batteriekapazitaet * 6; // Beispiel: 6 km pro kWh
    }
}

public class Main {
    public static void main(String[] args) {
        Fahrzeug auto = new Elektroauto("Tesla", "Model 3", 75);
        System.out.println(auto.anzeigenInformationen());
        System.out.println("Reichweite: " + auto.berechneReichweite() + " km");
    }
}
```

#### Vorteile:
- **Wiederverwendbarkeit:** Gemeinsame Eigenschaften und Methoden können in der abstrakten Klasse definiert werden, um Redundanz zu vermeiden.
- **Flexibilität:** Unterklassen können die abstrakten Methoden auf ihre spezifischen Anforderungen anpassen.
- **Polymorphismus:** Abstrakte Klassen ermöglichen es, Objekte unterschiedlicher Unterklassen einheitlich zu behandeln.

#### Fazit:
Abstrakte Klassen sind eine wichtige Grundlage in der objektorientierten Programmierung, um gemeinsame Funktionalitäten bereitzustellen und gleichzeitig die Implementierung bestimmter Methoden den Unterklassen zu überlassen.

Eine abstrakte Klasse ist eine Klasse, die nur als Vorlage dient.
Man kann kein Objekt davon erstellen.
Sie kann gemeinsame Attribute und Methoden enthalten.
Sie kann abstrakte Methoden haben, die Unterklassen selbst implementieren müssen.
Unterklassen erben von der abstrakten Klasse und machen daraus echte Objekte.
