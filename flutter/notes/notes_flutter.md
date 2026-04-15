📘 Meine Flutter Notes – Woche X

Um das Gelernte anzuwenden, notiere ich Lerninhalte, Beispiele und Reflektionen.


📅 Tagesnotizen
🗓️ Tag 1 – Thema / Schwerpunkt Environmentsetup

Kurze Zusammenfassung:

## Flutter CLI – Erste Schritte

Das Flutter CLI ist eine Sammlung von Kommandozeilenbefehlen, mit denen Flutter-Projekte erstellt, verwaltet, getestet, gebaut und deployt werden können – unabhängig von einer IDE.

**Grundsyntax:**
```
flutter [Befehl] [Unterbefehl] [Argumente] [Optionen]
```

---

### Hilfe

```bash
flutter help              # Liste aller Befehle
flutter help [Befehl]     # Hilfe zu einem bestimmten Befehl
```

---

### Projektmanagement

```bash
flutter create meine_app                                        # Neues Projekt erstellen
flutter create --org com.firma --template=app --platforms=android,ios --project-name=MeineApp mein_projekt
```

**Wichtige `create`-Optionen:**
| Option            | Bedeutung                                              |
|-------------------|--------------------------------------------------------|
| `--org`           | Organisations-ID (z. B. `com.meinefirma`)              |
| `--template`      | Projekttyp: `app`, `package`, `plugin`                 |
| `--platforms`     | Zielplattformen: `android`, `ios`, `web`, `windows` …  |
| `--project-name`  | Offizieller App-Name (darf Großbuchstaben enthalten)   |
| `--description`   | Projektbeschreibung                                    |

**Projektstruktur (Auszug):**
```
meine_app/
├── lib/
│   └── main.dart       # Einstiegspunkt der App
├── test/               # Testdateien
├── pubspec.yaml        # Metadaten & Abhängigkeiten
└── README.md
```

---

### Abhängigkeiten (pub)

```bash
flutter pub get                    # Abhängigkeiten herunterladen
flutter pub upgrade                # Abhängigkeiten aktualisieren
flutter pub outdated               # Veraltete Pakete anzeigen
flutter pub add package_name       # Paket hinzufügen
flutter pub remove package_name    # Paket entfernen
```

---

### App ausführen & debuggen

```bash
flutter devices                    # Verfügbare Geräte auflisten
flutter run                        # App im Debug-Modus starten
flutter run -d device_id           # App auf bestimmtem Gerät starten
flutter run -d chrome              # Web (Chrome)
flutter run -d windows             # Windows Desktop
```

**Laufzeit-Shortcuts:**
| Taste | Aktion                                          |
|-------|-------------------------------------------------|
| `r`   | Hot Reload (UI aktualisieren, ohne Neustart)    |
| `R`   | Hot Restart (App neu starten)                   |
| `h`   | Alle Befehle anzeigen                           |
| `d`   | DevTools im Browser öffnen                      |
| `q`   | App beenden                                     |

---

### Testing & Analyse

```bash
flutter test                         # Alle Tests ausführen
flutter test test/my_test.dart       # Einzelnen Test ausführen
flutter analyze                      # Statische Codeanalyse
flutter format lib                   # Code formatieren (Dart Style)
```

---

### Build & Deployment

```bash
# Android
flutter build apk           # APK erstellen
flutter build appbundle     # App Bundle für Play Store

# iOS (nur macOS)
flutter build ios           # iOS-Archiv → danach Xcode für Signierung

# Web
flutter build web           # Web-Version erstellen
```

Ausgabedateien: `build/app/outputs/`

---


### Variablendeklaration in Dart

In Dart gibt es drei Hauptarten, Variablen zu deklarieren: `var`, `final` und `const`. Der Unterschied zwischen ihnen ist subtil, aber wichtig:

- **`var`**: Deklariert eine Variable, deren Typ automatisch inferiert wird. Der Wert der Variable kann später geändert werden.
  ```dart
  var name = 'Alice';
  name = 'Bob'; // Gültig
  ```

- **`final`**: Deklariert eine Variable, die nach der Initialisierung nicht mehr geändert werden kann. Der Wert einer `final`-Variable kann jedoch zur Laufzeit berechnet werden.
  ```dart
  final currentTime = DateTime.now();
  // currentTime = DateTime.now(); // Fehler: Wert kann nicht geändert werden
  ```

- **`const`**: Deklariert eine Kompilierzeit-Konstante. Der Wert muss bereits zur Kompilierzeit vollständig bekannt sein.
  ```dart
  const pi = 3.14159;
  // const area = pi * radius; // Fehler, wenn radius nicht const ist
  ```

**Zusammenfassung:**
| Schlüsselwort | Änderbarkeit | Zeitpunkt der Wertzuweisung |
|---------------|--------------|-----------------------------|
| `var`         | Änderbar     | Zur Laufzeit                |
| `final`       | Nicht änderbar | Zur Laufzeit                |
| `const`       | Nicht änderbar | Zur Kompilierzeit           |

---

### Type System und Type Safety

Dart hat ein ausdrucksstarkes Typsystem, das sowohl statische Typsicherheit als auch Flexibilität bietet. Der Compiler prüft zur Kompilierzeit, ob Variablen und Ausdrücke den richtigen Typ haben, was viele Fehler frühzeitig erkennt.

#### Statische vs. Dynamische Typisierung

Obwohl Dart primär eine statisch typisierte Sprache ist, bietet es auch die Möglichkeit, mit dem `dynamic`-Typ dynamisch typisierte Variablen zu erstellen:

```dart
// Statisch typisierte Variable
String name = 'Anna';
int alter = 30;
// name = 42; // Fehler: Ein int kann nicht einem String zugewiesen werden

// Dynamisch typisierte Variable
dynamic dynamischeVariable = 'Ein String';
dynamischeVariable = 42;   // Kein Fehler: dynamic kann jeden Wert annehmen
dynamischeVariable = true; // Kein Fehler

// Vorsicht:
// int zahl = dynamischeVariable; // Kann zur Laufzeit fehlschlagen
```

Die Verwendung von `dynamic` kann in bestimmten Situationen nützlich sein, etwa beim Arbeiten mit JSON-Daten oder bei der Interaktion mit JavaScript in Flutter Web. Jedoch sollte sie sparsam eingesetzt werden, da sie die Vorteile der statischen Typsicherheit aufhebt.

#### Typinferenz

Dart bietet eine leistungsstarke Typinferenz, die es dem Compiler ermöglicht, den Typ einer Variable aus ihrem Initialwert abzuleiten:

```dart
// Explizite Typangabe
String expliziterName = 'Anna';

// Typinferenz mit var
var inferierterName = 'Ben'; // Dart leitet ab: String

print(expliziterName.runtimeType); // String
print(inferierterName.runtimeType); // String

// Nach der Initialisierung kann der Typ nicht mehr geändert werden
// inferierterName = 42; // Fehler: Ein int kann nicht einem String zugewiesen werden
```

Die Typinferenz macht den Code prägnanter, ohne die Typsicherheit zu beeinträchtigen. Sie wird häufig für lokale Variablen verwendet, während für öffentliche APIs und Klassenvariablen oft explizite Typangaben bevorzugt werden.

#### Type Promotion

Dart unterstützt Type Promotion: Wenn der Compiler durch eine `is`-Prüfung weiß, welcher konkrete Typ eine Variable hat, behandelt er die Variable in diesem Block automatisch als diesen Typ – ohne explizites Casting.

```dart
void verarbeiteWert(Object wert) {
  if (wert is String) {
    // 'wert' ist hier automatisch als String bekannt
    print('Länge: ${wert.length}'); // kein (wert as String) nötig
  } else if (wert is int) {
    // 'wert' ist hier automatisch als int bekannt
    print('Doppelter Wert: ${wert * 2}');
  } else {
    print('Unbekannter Typ: ${wert.runtimeType}');
  }
}

verarbeiteWert('Hallo'); // Länge: 5
verarbeiteWert(42);      // Doppelter Wert: 84
verarbeiteWert(true);    // Unbekannter Typ: bool
```

Type Promotion ist das Gegenstück zu `dynamic`: Statt Typsicherheit aufzugeben, prüft man den Typ explizit – und der Compiler weiß es danach auch. Besonders nützlich bei polymorphen Datenstrukturen.

---

## Grundlegende Datentypen in Dart

---

### Grundlegende Datentypen in Dart

Dart ist eine typisierte Sprache und bietet verschiedene eingebaute Datentypen. Hier sind die wichtigsten:

#### Numerische Typen
- **`int`**: Ganze Zahlen
  ```dart
  int ganzzahl = 42;
  ```
- **`double`**: Kommazahlen
  ```dart
  double kommazahl = 3.14;
  ```
- **`num`**: Kann sowohl `int` als auch `double` sein
  ```dart
  num beliebigZahl = 10;
  ```

#### Texttypen
- **`String`**: Zeichenketten
  ```dart
  String text = 'Hallo, Welt!';
  ```

#### Boolesche Werte
- **`bool`**: Wahrheitswerte
  ```dart
  bool wahr = true;
  bool falsch = false;
  ```

#### Listen (Arrays)
- **`List`**: Geordnete Sammlung von Elementen
  ```dart
  List<String> namen = ['Anna', 'Ben', 'Clara'];
  ```

#### Maps (Dictionaries/assoziative Arrays)
- **`Map`**: Schlüssel-Wert-Paare
  ```dart
  Map<String, int> alter = {
    'Anna': 30,
    'Ben': 25,
    'Clara': 35,
  };
  ```

#### Sets
- **`Set`**: Ungeordnete Sammlung eindeutiger Elemente
  ```dart
  Set<int> eindeutigeZahlen = {1, 2, 3, 4, 5};
  ```

#### Runes
- **`Runes`**: Für Unicode-Zeichen
  ```dart
  Runes herzEmoji = Runes('\u2665'); // ♥
  ```

#### Symbole
- **`Symbol`**: Für symbolische Namen
  ```dart
  Symbol symbolName = #someSymbol;
  ```

### Häufig verwendete Typen
In modernen Dart-Anwendungen, insbesondere mit Flutter, wirst du hauptsächlich mit den Typen `int`, `double`, `String`, `bool`, `List` und `Map` arbeiten. Die anderen Typen werden in spezielleren Situationen verwendet.

### Strings in Dart

Strings in Dart sind UTF-16-Zeichensequenzen. Sie können mit einfachen oder doppelten Anführungszeichen definiert werden:

- **Einfache und doppelte Anführungszeichen**
  ```dart
  String einfach = 'Das ist ein String mit einfachen Anführungszeichen.';
  String doppelt = "Das ist ein String mit doppelten Anführungszeichen.";
  ```

- **Multiline-Strings**: Strings, die sich über mehrere Zeilen erstrecken
  ```dart
  String mehrereZeilen = '''
  Dies ist ein String,
  der sich über mehrere
  Zeilen erstreckt.
  ''';
  ```

- **Raw-Strings**: Strings ohne Escape-Sequenzen
  ```dart
  String rohString = r'In diesem String werden \n und \t nicht als Escape-Sequenzen interpretiert.';
  ```

#### String-Interpolation
Ein besonders nützliches Feature von Dart ist die String-Interpolation, die es ermöglicht, Variablenwerte direkt in Strings einzubetten:

- **Einfache Interpolation**
  ```dart
  String name = 'Anna';
  int alter = 30;
  String vorstellung = 'Ich heiße $name und bin $alter Jahre alt.';
  ```

- **Komplexe Ausdrücke**: Verwende geschweifte Klammern für komplexere Ausdrücke
  ```dart
  String vorstellungKomplex = 'In 5 Jahren werde ich ${alter + 5} Jahre alt sein.';
  ```

Die String-Interpolation macht den Code lesbarer und vermeidet die umständliche Konkatenation, die in vielen anderen Sprachen notwendig ist.

### Operatoren in Dart

Dart bietet alle gängigen arithmetischen, Vergleichs-, logischen und Zuweisungsoperatoren. Zusätzlich gibt es einige Besonderheiten, die Dart von anderen Sprachen abheben:

#### Arithmetische Operatoren
- **Grundlegende Operationen**
  ```dart
  int a = 10;
  int b = 3;
  int summe = a + b; // 13
  int differenz = a - b; // 7
  int produkt = a * b; // 30
  double quotient = a / b; // 3.3333...
  int ganzzahlQuotient = a ~/ b; // 3 (ganzzahlige Division)
  int rest = a % b; // 1 (Modulo/Rest)
  ```
- **Increment und Decrement**
  ```dart
  a++; // a = a + 1
  b--; // b = b - 1
  ```

#### Vergleichsoperatoren
- **Vergleiche**
  ```dart
  bool istGleich = a == b; // false
  bool istNichtGleich = a != b; // true
  bool istGroesser = a > b; // true
  bool istKleiner = a < b; // false
  bool istGroesserGleich = a >= b; // true
  bool istKleinerGleich = a <= b; // false
  ```

#### Logische Operatoren
- **Logik**
  ```dart
  bool bedingung1 = true;
  bool bedingung2 = false;
  bool und = bedingung1 && bedingung2; // false (beide müssen wahr sein)
  bool oder = bedingung1 || bedingung2; // true (mindestens eine muss wahr sein)
  bool nicht = !bedingung1; // false (Negation)
  ```

#### Zuweisungsoperatoren
- **Kombinierte Zuweisungen**
  ```dart
  int c = 5;
  c += 2; // c = c + 2
  c -= 1; // c = c - 1
  c *= 3; // c = c * 3
  c ~/= 2; // c = c ~/ 2 (ganzzahlige Division)
  ```

#### Besondere Operatoren in Dart
- **Nullsicherheits-Operatoren** (wichtig für Null Safety)
  ```dart
  String? nullableString = null;
  String nichtNull = nullableString ?? 'Standardwert'; // ?? bietet einen Fallback, wenn der Wert null ist
  String? laenge = nullableString?.length.toString(); // Bedingter Zugriff
  ```

- **Typüberprüfung und Type-Cast**
  ```dart
  dynamic gemischt = 'Ein String';
  if (gemischt is String) {
    print('gemischt ist ein String');
  }
  if (gemischt is String) {
    String alsString = gemischt as String; // Explizites Casting
    print(alsString.toUpperCase());
  }
  ```

- **Kaskaden-Notation (..)**
  ```dart
  var liste = [1, 2, 3]
    ..add(4)
    ..add(5)
    ..remove(2); // Liste ist jetzt [1, 3, 4, 5]
  ```
  Die Kaskaden-Notation ist besonders in Flutter nützlich, wenn du mehrere Operationen auf demselben Objekt ausführen möchtest, ohne jedes Mal den Objektnamen wiederholen zu müssen.

### Kontrollstrukturen in Dart

Dart bietet alle üblichen Kontrollstrukturen wie `if-else`, Schleifen und `switch-case`. Zusätzlich gibt es moderne Erweiterungen wie Switch-Expressions in Dart 3.

#### If-Else
- **Bedingte Anweisungen**
  ```dart
  int alter = 18;
  if (alter >= 18) {
    print('Volljährig');
  } else if (alter >= 14) {
    print('Teenager');
  } else {
    print('Kind');
  }
  ```

#### Schleifen
- **For-Schleife**
  ```dart
  for (int i = 0; i < 5; i++) {
    print('Durchlauf $i');
  }
  ```

- **For-in-Schleife (für Collections)**
  ```dart
  List<String> früchte = ['Apfel', 'Banane', 'Kirsche'];
  for (var frucht in früchte) {
    print('Ich mag $frucht');
  }
  ```

- **While-Schleife**
  ```dart
  int counter = 0;
  while (counter < 5) {
    print('Counter: $counter');
    counter++;
  }
  ```

- **Do-While-Schleife** (wird mindestens einmal ausgeführt)
  ```dart
  int doCounter = 0;
  do {
    print('Do counter: $doCounter');
    doCounter++;
  } while (doCounter < 5);
  ```

#### Switch-Case
- **Klassische Switch-Case**
  ```dart
  String note = 'B';
  switch (note) {
    case 'A':
      print('Sehr gut');
      break;
    case 'B':
      print('Gut');
      break;
    case 'C':
      print('Befriedigend');
      break;
    default:
      print('Andere Note');
  }
  ```

- **Moderne Switch-Expression (Dart 3)**
  ```dart
  String note = 'B';
  String bewertung = switch (note) {
    'A' => 'Sehr gut',
    'B' => 'Gut',
    'C' => 'Befriedigend',
    _ => 'Andere Note' // _ ist der Default-Fall
  };
  ```

Die modernen Switch-Expressions bieten eine kompakte und ausdrucksstarke Möglichkeit, mehrere Fälle zu behandeln.

### Funktionen in Dart

Funktionen sind in Dart Objekte erster Klasse. Das bedeutet, sie können Variablen zugewiesen, als Argumente übergeben und von anderen Funktionen zurückgegeben werden.

#### Beispiele für Funktionen
- **Einfache Funktion**
  ```dart
  void grüßen() {
    print('Hallo!');
  }
  ```

- **Funktion mit Parametern und Rückgabewert**
  ```dart
  int addieren(int a, int b) {
    return a + b;
  }
  ```

- **Optionale und benannte Parameter**
  ```dart
  void grüßenOptional(String name, [String? titel]) {
    if (titel != null) {
      print('Hallo, $titel $name!');
    } else {
      print('Hallo, $name!');
    }
  }

  void personErstellen({
    required String name,
    required int alter,
    String? beruf,
  }) {
    print('Name: $name, Alter: $alter');
    if (beruf != null) {
      print('Beruf: $beruf');
    }
  }
  ```

- **Anonyme Funktionen und höhere Ordnung**
  ```dart
  var quadrieren = (int x) => x * x;
  print(quadrieren(4)); // 16

  void applyOperation(int a, int b, int Function(int, int) operation) {
    print('Ergebnis: ${operation(a, b)}');
  }
  applyOperation(4, 2, (a, b) => a + b); // Ergebnis: 6
  ```

In Flutter sind anonyme Funktionen besonders nützlich, z. B. für Callbacks und Event-Handler.

---

### Ausnahmebehandlung in Dart

Dart unterstützt strukturierte Ausnahmebehandlung mit `try-catch-finally`, um Fehler sicher zu handhaben.

#### Beispiele für Ausnahmebehandlung
- **Grundlegende Ausnahmebehandlung**
  ```dart
  try {
    int ergebnis = 10 ~/ 0; // Division durch Null
  } on IntegerDivisionByZeroException {
    print('Division durch Null ist nicht erlaubt');
  } catch (e) {
    print('Ein Fehler ist aufgetreten: $e');
  } finally {
    print('Aufräumarbeiten');
  }
  ```

- **Eigene Ausnahmen werfen**
  ```dart
  void prüfeAlter(int alter) {
    if (alter < 0) {
      throw ArgumentError('Alter kann nicht negativ sein');
    }
  }
  ```

In Flutter-Anwendungen ist eine gute Ausnahmebehandlung wichtig, um Abstürze zu vermeiden und sinnvolle Fehlermeldungen anzuzeigen.

---

### Dart-Libraries und Importe

In Dart werden Code-Module als Libraries organisiert. Du kannst Libraries importieren, um deren Funktionalität zu nutzen.

#### Beispiele für Importe
- **Standard-Libraries**
  ```dart
  import 'dart:math';
  ```

- **Mit Präfix zur Vermeidung von Namenskonflikten**
  ```dart
  import 'dart:math' as math;
  ```

- **Selektiver Import**
  ```dart
  import 'dart:math' show Random, min, max;
  import 'dart:math' hide Random;
  ```

- **Externe Pakete und lokale Dateien**
  ```dart
  import 'package:flutter/material.dart';
  import 'package:meine_app/models/user.dart';
  ```

In Flutter-Projekten sind Importe von Framework-Libraries und Paketen aus `pub.dev` essenziell.

---

## Zusammenfassung: Primitive Datentypen in Dart

Dart behandelt alle Werte als Objekte, auch die sogenannten primitiven Datentypen. Die wichtigsten sind:

- **int**: Ganze Zahlen (z. B. 42)
- **double**: Gleitkommazahlen (z. B. 3.14159)
- **num**: Oberklasse für int und double, kann beide aufnehmen

**Eigenschaften:**
- Die genaue Größe der Typen muss nicht beachtet werden, Dart verwaltet das automatisch.
- int: Wertebereich von -2^63 bis 2^63-1
- double: 64-Bit nach IEEE 754-Standard

**Beispiele:**
```dart
int meineGanzzahl = 42;
double meineGleitkommazahl = 3.14159;
num meineZahl = 10; // kann später int oder double sein

// Numerische Operationen
int summe = meineGanzzahl + 10; // 52
double produkt = meineGleitkommazahl * 2; // 6.28318

// Konvertierung zwischen Zahlentypen
double alsDouble = meineGanzzahl.toDouble(); // 42.0
int alsInt = meineGleitkommazahl.round(); // 3
```

---

## Zusammenfassung: Strings und Booleans in Dart

### Strings
Strings sind unveränderliche (immutable) Folgen von UTF-16-Codeeinheiten. Sie können mit einfachen oder doppelten Anführungszeichen, Escape-Sequenzen oder als Multiline-Strings definiert werden.

**Beispiele:**
```dart
String einfach = 'Ein einfacher String';
String doppelt = "Auch ein String";
String mitEscapeSequenzen = 'Tab: \t, Neue Zeile: \n';
String multiline = '''
Dies ist ein String
über mehrere Zeilen
hinweg.
''';

// String-Operationen
String zusammengesetzt = einfach + ' ' + doppelt; // Konkatenation
bool enthält = einfach.contains('einfach'); // true
String kleingeschrieben = einfach.toLowerCase();
String großgeschrieben = einfach.toUpperCase();
String teilstring = einfach.substring(4, 12); // 'einfache'
List<String> wörter = einfach.split(' '); // ['Ein', 'einfacher', 'String']

// String-Interpolation
String name = 'Anna';
int alter = 30;
String info = 'Name: $name, Alter: $alter'; // 'Name: Anna, Alter: 30'
String berechnung = 'Doppeltes Alter: ${alter * 2}'; // 'Doppeltes Alter: 60'
```

### Booleans
Der Typ `bool` kann nur die Werte `true` oder `false` annehmen. Andere Werte wie `null`, `0` oder leere Strings gelten NICHT als false.

**Beispiele:**
```dart
bool istWahr = true;
bool istFalsch = false;

// Logische Operationen
bool und = istWahr && istFalsch; // false
bool oder = istWahr || istFalsch; // true
bool negiert = !istWahr; // false

// Vergleichsoperationen
bool istGleich = 5 == 5; // true
bool istGroesser = 7 > 3; // true

// Bedingter Ausdruck
String status = istWahr ? 'Aktiviert' : 'Deaktiviert'; // 'Aktiviert'
```

Nur `true` und `false` sind gültige boolesche Werte in Dart. Das sorgt für expliziten und klaren Code.

---

## Zusammenfassung: Collections in Dart (List, Map, Set)

### Listen (List)
Geordnete Sammlungen von Elementen, vergleichbar mit Arrays. Listen können verändert oder unveränderlich sein.

**Beispiele:**
```dart
List<int> zahlen = [1, 2, 3, 4, 5];
List<String> namen = ['Anna', 'Ben', 'Clara'];
int erstesElement = zahlen[0]; // 1
String letzterName = namen[namen.length - 1]; // 'Clara'
zahlen.add(6); // [1, 2, 3, 4, 5, 6]
namen.remove('Ben'); // ['Anna', 'Clara']
zahlen.sort();
zahlen.forEach((zahl) => print(zahl));
List<int> mehrZahlen = [0, ...zahlen]; // Spread-Operator

// Collection-If und Collection-For
bool inkludiereSieben = true;
List<int> dynamischeZahlen = [1, 2, if (inkludiereSieben) 7];
List<String> früchte = ['Apfel', 'Banane', 'Kirsche'];
List<String> großeFrüchte = [for (var frucht in früchte) frucht.toUpperCase()];
```

### Maps
Sammlung von Schlüssel-Wert-Paaren, ähnlich wie Dictionaries.

**Beispiele:**
```dart
Map<String, int> alter = {'Anna': 30, 'Ben': 25, 'Clara': 35};
int annasAlter = alter['Anna'] ?? 0;
alter['David'] = 40;
alter.remove('Ben');
if (alter.containsKey('Clara')) {
  print('Clara ist ${alter['Clara']} Jahre alt.');
}
alter.forEach((name, jahre) {
  print('$name ist $jahre Jahre alt.');
});
Iterable<MapEntry<String, int>> eintraege = alter.entries;
Iterable<String> namen = alter.keys;
Iterable<int> alterswerte = alter.values;
```

### Sets
Ungeordnete Sammlung eindeutiger Elemente (keine Duplikate).

**Beispiele:**
```dart
Set<int> eindeutigeZahlen = {1, 2, 3, 4, 5};
Set<String> früchte = {'Apfel', 'Banane', 'Kirsche'};
eindeutigeZahlen.add(3); // Keine Änderung
eindeutigeZahlen.add(6); // {1, 2, 3, 4, 5, 6}
bool enthältBanane = früchte.contains('Banane'); // true
Set<int> andereZahlen = {4, 5, 6, 7, 8};
Set<int> vereinigung = eindeutigeZahlen.union(andereZahlen); // {1, 2, 3, 4, 5, 6, 7, 8}
Set<int> schnittmenge = eindeutigeZahlen.intersection(andereZahlen); // {4, 5, 6}
Set<int> differenz = eindeutigeZahlen.difference(andereZahlen); // {1, 2, 3}
```

**Hinweis:** Listen, Maps und Sets sind zentrale Werkzeuge für die Datenorganisation in Dart und Flutter.

---

## Zusammenfassung: Records und Enums in Dart

### Records (seit Dart 3.0)
Records sind zusammengesetzte Datentypen, mit denen mehrere Werte ohne eigene Klasse gruppiert werden können.

**Beispiele:**
```dart
// Ein Record mit zwei Werten
(String, int) person = ('Anna', 30);
String name = person.$1; // 'Anna'
int alter = person.$2; // 30

// Records mit benannten Feldern
({String name, int alter}) benannt = (name: 'Ben', alter: 25);
String benannterName = benannt.name; // 'Ben'
int benannterAlter = benannt.alter; // 25

// Records als Rückgabewerte von Funktionen
(String, int) getPersoneninfo() {
  return ('Clara', 35);
}
var (extrahierterName, extrahiertesAlter) = getPersoneninfo();
print('Name: $extrahierterName, Alter: $extrahiertesAlter');
```
Records sind praktisch, wenn Funktionen mehrere Werte zurückgeben oder Daten temporär gruppiert werden sollen.

### Enumerations (Enums)
Enums definieren einen Typ mit festen, benannten Werten.

**Beispiele:**
```dart
enum Wochentag { Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag }
Wochentag heute = Wochentag.Donnerstag;
String heuteAlsString = heute.toString(); // 'Wochentag.Donnerstag'
String nurName = heute.name; // 'Donnerstag'

// String zu Enum
Wochentag? vonString = Wochentag.values.firstWhere(
  (tag) => tag.name == 'Freitag',
  orElse: () => Wochentag.Montag,
);

// Iteration über alle Enum-Werte
for (var tag in Wochentag.values) {
  print('Wochentag: ${tag.name}');
}

// Switch mit Enums
switch (heute) {
  case Wochentag.Samstag:
  case Wochentag.Sonntag:
    print('Wochenende!');
    break;
  default:
    print('Arbeitstag');
}
```

**Erweiterte Enums (seit Dart 3.0):**
Enums können Felder, Methoden und Konstruktoren enthalten.
```dart
enum Farbe {
  rot(hex: 0xFF0000),
  grün(hex: 0x00FF00),
  blau(hex: 0x0000FF);

  const Farbe({required this.hex});
  final int hex;
  String get hexString => '#${hex.toRadixString(16).padLeft(6, '0')}';
}

Farbe meineFarbe = Farbe.blau;
print('Blau als Hex: ${meineFarbe.hexString}'); // '#0000ff'
```
Enums sind ideal für Status, Kategorien oder Optionen mit festem Wertebereich.
