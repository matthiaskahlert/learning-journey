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
    print('Laenge: ${wert.length}'); // kein (wert as String) noetig
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
  String vorstellung = 'Ich heisse $name und bin $alter Jahre alt.';
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
  List<String> fruechte = ['Apfel', 'Banane', 'Kirsche'];
  for (var frucht in fruechte) {
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
  void gruessen() {
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
  void gruessenOptional(String name, [String? titel]) {
    if (titel != null) {
      print('Hallo, $titel $name!');
    } else {
      print('Hallo, $name!');
    }
  }
// mit required werden benannte Parameter als erforderlich markiert 
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
bool enthaelt = einfach.contains('einfach'); // true
String kleingeschrieben = einfach.toLowerCase();
String grossgeschrieben = einfach.toUpperCase();
String teilstring = einfach.substring(4, 12); // 'einfache'
List<String> woerter = einfach.split(' '); // ['Ein', 'einfacher', 'String']

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
List<String> fruechte = ['Apfel', 'Banane', 'Kirsche'];
List<String> grosseFruechte = [for (var frucht in fruechte) frucht.toUpperCase()];
```

### Maps
Sammlung von Schlüssel-Wert-Paare, ähnlich wie Dictionaries.

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
Set<String> fruechte = {'Apfel', 'Banane', 'Kirsche'};
eindeutigeZahlen.add(3); // Keine Änderung
eindeutigeZahlen.add(6); // {1, 2, 3, 4, 5, 6}
bool enthaeltBanane = fruechte.contains('Banane'); // true
Set<int> andereZahlen = {4, 5, 6, 7, 8};
Set<int> vereinigung = eindeutigeZahlen.union(andereZahlen); // {1, 2, 3, 4, 5, 6, 7, 8}
Set<int> schnittmenge = eindeutigeZahlen.intersection(andereZahlen); // {4, 5, 6}
Set<int> differenz = eindeutigeZahlen.difference(andereZahlen); // {1, 2, 3}
```
Unterschiede
| Eigenschaft        | Liste       | Map                          | Set                                 |
|--------------------|-------------|------------------------------|-------------------------------------|
| Geordnet           | Ja          | Nein (Schlüssel-Wert-Paare)  | Nein                                |
| Duplikate erlaubt  | Ja          | Schlüssel: Nein, Werte: Ja   | Nein                                |
| Zugriff            | Über Index  | Über Schlüssel               | Direkter Zugriff (ungeordnet)        |
| Einsatzbereich     | Reihenfolge wichtig | Schlüssel-Wert-Zuordnung | Einzigartige Werte                  |
Wann benutzt man was?
Liste: Wenn die Reihenfolge wichtig ist oder du Duplikate speichern möchtest.
Map: Wenn du Daten mit einem Schlüssel verknüpfen möchtest (z. B. Name → Alter).
Set: Wenn du sicherstellen möchtest, dass alle Elemente einzigartig sind.
**Hinweis:** Listen, Maps und Sets sind zentrale Werkzeuge für die Datenorganisation in Dart und Flutter.

---

## Records und Enums in Dart

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
  gruen(hex: 0x00FF00),
  blau(hex: 0x0000FF);

  const Farbe({required this.hex});
  final int hex;
  String get hexString => '#${hex.toRadixString(16).padLeft(6, '0')}';
}

Farbe meineFarbe = Farbe.blau;
print('Blau als Hex: ${meineFarbe.hexString}'); // '#0000ff'
```
Enums sind ideal für Status, Kategorien oder Optionen mit festem Wertebereich.

---

## Null Safety, Nullable und `late` leicht erklaert

Seit Dart 2.12 gibt es **Null Safety**. Die Idee ist einfach: Viele Bugs entstehen, wenn man aus Versehen mit `null` arbeitet. Dart unterscheidet deshalb klar zwischen Typen, die `null` sein duerfen, und Typen, die es nicht sein duerfen.

- **Non-nullable**: `String`, `int`, `bool` (duerfen nicht `null` sein)
- **Nullable**: `String?`, `int?`, `bool?` (duerfen `null` sein)

```dart
String text = 'Hallo';   // nie null
String? name = null;     // darf null sein
```

### 1) `??` ist nur eine Kurzform fuer eine if-else-Pruefung

```dart
String result = name ?? 'Gast';
```

Das bedeutet genau:

```dart
String result;
if (name != null) {
  result = name;
} else {
  result = 'Gast';
}
```

Merksatz: **`??` nimmt den linken Wert, wenn er nicht null ist, sonst den rechten Fallback-Wert.**

### 2) Wichtige Null-Aware-Operatoren

- `?.` Zugriff nur, wenn nicht `null`
- `??` Fallback bei `null`
- `??=` Zuweisung nur dann, wenn aktuell `null`
- `!` Ich bin sicher, dass es nicht `null` ist (vorsichtig einsetzen)

```dart
String? name = null;
  int? laenge = name?.length;          // null statt Fehler

String? text = null;
text ??= 'Standard';                 // setzt nur, weil text null ist
text ??= 'Ignoriert';                // bleibt 'Standard'

String? wert = 'Hallo';
String sicher = wert!;               // ok
```

Hinweis zu `!`: Wenn der Wert doch `null` ist, gibt es zur Laufzeit einen Fehler.

### 3) Flow Analysis: Dart denkt mit

Wenn du vorher auf `null` pruefst, weiss Dart danach, dass der Wert nicht mehr `null` ist:

```dart
void printLaenge(String? input) {
  if (input == null) {
    print('Kein Text');
    return;
  }
  // Hier ist input sicher nicht null
  print(input.length);
}
```

### 4) Nullable Parameter und Rueckgabewerte

```dart
String verarbeite(String? input) {
  return input ?? 'Standardwert';
}

int? findeIndex(List<String> liste, String element) {
  final index = liste.indexOf(element);
  return index >= 0 ? index : null;
}
```

### 5) Was macht `late`?

`late` bedeutet: **Die Variable ist non-nullable, wird aber spaeter initialisiert.**

Das ist hilfreich, wenn der Wert nicht sofort beim Erstellen bekannt ist, aber vor der ersten Nutzung sicher gesetzt wird.

```dart
class Person {
  final String name;
  late String adresse;

  Person(this.name);

  void setzeAdresse(String neueAdresse) {
    adresse = neueAdresse;
  }
}
```

Wenn du auf ein `late`-Feld zugreifst, bevor es gesetzt wurde, gibt es einen Laufzeitfehler.

#### `late` mit Lazy-Initialisierung

Der Wert kann auch erst bei der **ersten Verwendung** berechnet werden:

```dart
class User {
  final String vorname;
  User(this.vorname);

  late String vollerName = '$vorname Mustermann';
}
```

### Kurz zusammengefasst

- Nutze `?`, wenn `null` erlaubt sein soll.
- Nutze `??`, um einen klaren Standardwert zu setzen.
- Nutze `!` nur, wenn du wirklich sicher bist.
- Nutze `late`, wenn ein non-nullable Wert spaeter gesetzt wird.

## Lambda Funktionen

### Lambda-Ausdruecke (anonyme Funktionen) kurz erklaert

Lambda-Ausdruecke sind **Funktionen ohne Namen**, die direkt an der Stelle geschrieben werden, wo man sie braucht.
Sie sind ideal fuer kurze Logik, zum Beispiel bei Callbacks oder als Funktionsargument.

#### 1) Zwei Schreibweisen

```dart
// Lange Form
var quadrieren = (int x) {
  return x * x;
};

// Kurzform mit Arrow-Syntax (gleiches Verhalten)
var quadrierenKurz = (int x) => x * x;

// Zusaetzliches Beispiel: kubieren
var kubieren = (int x) => x * x * x;

print(quadrieren(3)); // 9
print(quadrierenKurz(3)); // 9
print(kubieren(3));   // 27
```

Merksatz: Wenn der Funktionskoerper nur aus **einem Ausdruck** besteht, ist `=>` oft die kuerzeste und lesbarste Form.

#### 2) Haeufiger Einsatz: Callbacks

```dart
List<int> zahlen = [1, 2, 3, 4, 5];
var quadratzahlen = zahlen.map((zahl) => zahl * zahl).toList();
// [1, 4, 9, 16, 25]
```

Hier bekommt `map(...)` eine anonyme Funktion, die fuer jedes Element ausgefuehrt wird.

#### 3) Auch mit benannten Parametern moeglich

```dart
var gruessen = ({required String name}) => 'Hallo, $name!';
print(gruessen(name: 'Anna')); // Hallo, Anna!
```

#### 4) Closure: Funktion merkt sich ihren Kontext

Eine Lambda-Funktion kann auf Variablen aus der umgebenden Funktion zugreifen.
Das nennt man **Closure**.

```dart
Function multipliziere(int faktor) {
  return (int zahl) => zahl * faktor;
}

var verdoppeln = multipliziere(2);
var verdreifachen = multipliziere(3);

print(verdoppeln(5));    // 10
print(verdreifachen(5)); // 15
```

Warum das nuetzlich ist:
- Du kannst schnell kleine, spezialisierte Funktionen bauen.
- Dein Code bleibt kuerzer und oft besser lesbar.
- Besonders in Flutter ist das praktisch fuer UI-Callbacks (`onPressed`, `onTap`, `map`, `where` usw.).

## Rekursive Funktionen, Kaskaden, Generatoren und Komposition

### Rekursive Funktionen

Eine rekursive Funktion ruft sich selbst auf, bis eine Abbruchbedingung erreicht ist.

```dart
int fakultaet(int n) {
  if (n <= 1) {
    return 1; // Abbruchbedingung
  }
  return n * fakultaet(n - 1);
}

print(fakultaet(5)); // 120
```

Merke:
- Ohne Abbruchbedingung laeuft Rekursion endlos weiter.
- Rekursion ist gut fuer baumartige oder geschachtelte Strukturen.

### Kaskadierte Funktionsaufrufe (`..`)

Mit der Kaskaden-Notation fuehrst du mehrere Operationen auf demselben Objekt aus, ohne den Objektnamen zu wiederholen.

```dart
// Ohne Kaskade
var liste = <int>[];
liste.add(1);
liste.add(2);
liste.add(3);
liste.remove(2);

// Mit Kaskade
var liste2 = <int>[]
  ..add(1)
  ..add(2)
  ..add(3)
  ..remove(2);

print(liste);  // [1, 3]
print(liste2); // [1, 3]
```

Einfach gesagt:
- Ohne `..`: Liste, mach das. Liste, mach das.
- Mit `..`: Liste, mach alles nacheinander bis zum Semikolon.

### Generatorfunktionen

Generatoren erzeugen Werte Schritt fuer Schritt statt alle auf einmal.

```dart
// Synchroner Generator
Iterable<int> zaehlenBis(int n) sync* {
  for (int i = 1; i <= n; i++) {
    yield i;
  }
}

for (var zahl in zaehlenBis(5)) {
  print(zahl); // 1, 2, 3, 4, 5
}
```

```dart
// Asynchroner Generator
Stream<int> periodicGenerator(int n, Duration abstand) async* {
  for (int i = 1; i <= n; i++) {
    await Future.delayed(abstand);
    yield i;
  }
}

periodicGenerator(3, const Duration(seconds: 1)).listen((zahl) {
  print('Tick: $zahl');
});
```

Wann nuetzlich:
- Bei grossen Datenmengen
- Bei Datenstroemen ueber Zeit (Events, Timer, Animationen)

### Funktionskompositionen

Bei der Funktionskomposition wird das Ergebnis einer Funktion direkt an die naechste weitergegeben.

```dart
int verdoppeln(int x) => x * 2;
int plusEins(int x) => x + 1;

int verdoppelnUndPlusEins(int x) => plusEins(verdoppeln(x));

print(verdoppelnUndPlusEins(3)); // 7
```

```dart
Function komposition(Function f, Function g) {
  return (x) => g(f(x));
}

var verdoppelnDannPlusEins = komposition(verdoppeln, plusEins);
print(verdoppelnDannPlusEins(3)); // 7
```

Vorteil:
- Du baust komplexe Logik aus kleinen, gut testbaren Bausteinen auf.

## Praktische Anwendungen von Funktionen in Flutter

### Event-Handler und Callbacks

```dart
ElevatedButton(
  onPressed: () {
    print('Button wurde gedrueckt');
    // Fuehre weitere Aktionen aus...
  },
  child: const Text('Druecken'),
)
```

Leicht erklaert:
- `onPressed` bekommt eine Funktion.
- Diese Funktion wird erst ausgefuehrt, wenn der Button gedrueckt wird.

### Widget-Fabriken

```dart
Widget personenKarte(Person person) {
  return Card(
    child: ListTile(
      title: Text(person.name),
      subtitle: Text('Alter: ${person.alter}'),
    ),
  );
}

ListView(
  children: personen.map(personenKarte).toList(),
)
```

Leicht erklaert:
- Eine Funktion baut fuer jedes Datenobjekt ein passendes Widget.
- So bleibt dein UI-Code kuerzer und wiederverwendbar.

### Zustandsmanagement-Callbacks

```dart
void _toggleFavorit() {
  setState(() {
    _istFavorit = !_istFavorit;
  });
}

IconButton(
  icon: Icon(_istFavorit ? Icons.favorite : Icons.favorite_border),
  onPressed: _toggleFavorit,
)
```

Leicht erklaert:
- Der Callback aendert den Zustand.
- `setState` sagt Flutter: Bitte neu zeichnen.

### BuildContext-Erweiterungen
BuildContext ist in Flutter so etwas wie der aktuelle Ort eines Widgets im Widget-Baum.
Der Widget-Baum ist die verschachtelte Struktur aller Widgets deiner App.

MaterialApp
└── Scaffold
    ├── AppBar
    │   └── Text
    └── Center
        └── ElevatedButton
            └── Text

Eine BuildContext-Erweiterung bedeutet:
Du fügst diesem Ort eigene Hilfsfunktionen hinzu, damit du später kürzer und bequemer darauf zugreifen kannst.

Beispiel ohne Erweiterung:
```dart
extension BuildContextExtensions on BuildContext {
  ThemeData get theme => Theme.of(this);
  TextTheme get textTheme => theme.textTheme;
  ColorScheme get colorScheme => theme.colorScheme;

  void showSnackBar(String message) {
    ScaffoldMessenger.of(this).showSnackBar(
      SnackBar(content: Text(message)),
    );
  }
}

ElevatedButton(
  onPressed: () => context.showSnackBar('Aktion ausgefuehrt'),
  child: const Text('Aktion'),
)
```

Leicht erklaert:
- Du erweiterst `BuildContext` um eigene Helferfunktionen.
- Dadurch wird der Widget-Code klarer und lesbarer.

## Kurzes Recaap zu Objektorientierter Programmierung in Dart

Durch Mixins und Extensions wird in Dart die Klassesche OOP erweitert.
Eine einfache Klasse wird wie folgt erstellt:
```dart
// Einfache Klasse
class Person {
  // Felder (Instanzvariablen)
  String name;
  int alter;
  // Konstruktor
  Person(this.name, this.alter);
  // Methode
  void vorstellen() {
    print('Hallo, ich bin $name und $alter Jahre alt.');
  }
}

// Verwendung der Klasse
void main() {
  // Erstellung eines Objekts (Instanz)
  var person = Person('Anna', 30);
  // Zugriff auf Felder
  print(person.name); // 'Anna'
  print(person.alter); // 30
  // Aufruf einer Methode
  person.vorstellen(); // 'Hallo, ich bin Anna und 30 Jahre alt.'
  // Ändern von Feldern
  person.alter = 31;
  person.vorstellen(); // 'Hallo, ich bin Anna und 31 Jahre alt.'
}


```

Die Konstruktorfunktion ist in Dart mit verschiedenen Fuktionen ausgestattet.

Es gibt die klassische weise (Standardkonstruktor):
```dart
class Person {
  String name;
  int alter;
  // Standardkonstruktor
  Person(this.name, this.alter);
}
```

Die bereits bekannte schreibweise this.name ist eine einfache Art und Weise, Konstruktorpaarameter direkt den Instanzvariablen zuzuweisen.

Eine Alternative bildet die explizite form, Welche sich sehr an die Syntax aus anderen Programmiersprachen anlehnt:

```dart
class Person {
  String name;
  int alter;
  // Standardkonstruktor (explizite Form)
  Person(String name, int alter) {
    this.name = name;
    this.alter = alter;
  }
}
```

Darüber hinaus gibt es auch benannte Konstruktorfunktionen.
Sie werden verwendet um mehrere Konstroktoren in einer Klasse zu definieren.
Sie haben spezifische Namen der nach einem Punkt folgt.
Beispiel:
```dart
class Person {
  String name;
  int age;

  // Standardkonstruktor
  Person(this.name, this.age);

  // Benannter Konstruktor
  Person.fromName(this.name) : age = 0;

  Person.fromAge(this.age) : name = 'Unknown';
}

void main() {
  var person1 = Person('Alice', 25);
  var person2 = Person.fromName('Bob');
  var person3 = Person.fromAge(30);

  print('${person1.name}, ${person1.age}'); // Ausgabe: Alice, 25
  print('${person2.name}, ${person2.age}'); // Ausgabe: Bob, 0
  print('${person3.name}, ${person3.age}'); // Ausgabe: Unknown, 30
}
```
| **Eigenschaft** | **Standardkonstruktor** | **Benannter Konstruktor** |
|------------------|-------------------------|----------------------------|
| **Name**        | Hat keinen Namen        | Hat einen spezifischen Namen |
| **Anzahl**      | Es kann nur einen Standardkonstruktor geben | Es können mehrere benannte Konstruktoren geben |
| **Verwendung**   | Wird für allgemeine Initialisierungen verwendet | Wird für spezifische Initialisierungen verwendet |
| **Syntax**       | ClassName(...)         | ClassName.constructorName(...) |


Ein Singleton-Fabrikkonstruktor ermöglicht es, eine globale Instanz einer Klasse zu erstellen, auf die alle Teile des Programms zugreifen können. Änderungen an dieser Instanz wirken sich global aus, da keine Kopien erstellt werden."

Zusammenfassung der Vorteile
Ein Singleton-Fabrikkonstruktor bietet:

Globale Verfügbarkeit: Eine Instanz, die überall zugänglich ist.
Zentrale Kontrolle: Du bestimmst, wie und wann die Instanz erstellt wird.
Effizienz: Spart Speicher und Ressourcen durch Wiederverwendung.
Konsistenz: Alle Teile des Programms verwenden dieselbe Instanz.
Sicherheit: Verhindert unerwartete Instanzen durch Kapselung.
Wann ist ein Singleton sinnvoll?
Ein Singleton ist besonders nützlich, wenn:

Du eine globale Ressource verwalten möchtest (z. B. Logger, Konfiguration, Datenbankverbindung).
Du sicherstellen möchtest, dass es nur eine Instanz einer Klasse gibt.
Du Speicher und Ressourcen sparen möchtest, indem du Instanzen wiederverwendest.
Du eine Single Source of Truth benötigst, die überall im Programm konsistent ist.

Beispiel: Logger-Klasse mit Singleton
Ein Logger ist ein klassisches Beispiel für einen Singleton, da du sicherstellen möchtest, dass alle Teile des Programms dieselbe Instanz verwenden, um Log-Nachrichten zu schreiben.


```dart
class Logger {
  static final Logger _instance = Logger._internal();

  // Privater Konstruktor
  Logger._internal();

  // Fabrikkonstruktor gibt immer die gleiche Instanz zurück
  factory Logger() {
    return _instance;
  }

  void log(String message) {
    print('[LOG]: $message');
  }
}

void main() {
  var logger1 = Logger();
  var logger2 = Logger();

  logger1.log('Dies ist eine Nachricht.');
  logger2.log('Dies ist eine weitere Nachricht.');

  print(identical(logger1, logger2)); // true
}
```

Zusammenfassend lässt sich sagen, dass; Ein Singleton bietet eine globale Instanz, die sicherstellt, dass alle Teile des Programms dieselbe Klasse verwenden.
Es gibt dir die absolute Sicherheit, dass keine unerwarteten Instanzen erstellt werden.
Gleichzeitig birgt es die Gefahr von engen Kopplungen und unerwarteten Nebenwirkungen, wenn die Instanz unkontrolliert geändert wird.

### Zusammenfassung: Initialisierungsliste und Singleton-Fabrik-Konstruktoren

1. **Initialisierungsliste**:
   - Wird verwendet, um Instanzvariablen vor der Ausführung des Konstruktorkörpers zu initialisieren.
   - Besonders nützlich für `final`- und `const`-Variablen sowie für die Übergabe von Werten an Superklassen-Konstruktoren.
   - Sorgt für eine effiziente und klare Initialisierung.

2. **Singleton-Fabrik-Konstruktoren**:
   - Stellen sicher, dass nur eine einzige Instanz einer Klasse existiert.
   - Verhindern die wiederholte Erstellung von Objekten und sparen Ressourcen.
   - Kombinieren sich gut mit Initialisierungslisten, um die Instanz direkt bei der Erstellung korrekt zu initialisieren.

3. **Gemeinsamkeiten**:
   - Beide Mechanismen bieten Kontrolle und Effizienz bei der Objektinitialisierung.
   - Sie machen den Code klarer und strukturierter.

4. **Unterschiede**:
   - Initialisierungslisten sind für die Initialisierung von Variablen gedacht, während Singleton-Fabrik-Konstruktoren die Wiederverwendbarkeit einer Instanz sicherstellen.

5. **Kombination**:
   - Initialisierungslisten können verwendet werden, um die Variablen eines Singleton-Objekts effizient zu setzen.
   - Dies ermöglicht eine klare Trennung zwischen der Initialisierung und der Singleton-Logik.

### Zusammenfassung: Getter und Setter

1. **Definition**:
   - Getter und Setter sind spezielle Methoden, die den Zugriff auf Eigenschaften einer Klasse kontrollieren.
   - Sie sehen aus wie normale Eigenschaften, verhalten sich aber wie Methoden.

2. **Vorteile**:
   - **Kapselung**: Verbergen die Implementierungsdetails einer Klasse und bieten eine saubere API.
   - **Validierung**: Ermöglichen die Überprüfung von Werten, bevor sie gesetzt werden (z. B. Temperatur nicht unter -273,15 °C).
   - **Berechnete Eigenschaften**: Getter können Werte dynamisch berechnen (z. B. Umrechnung von Celsius in Fahrenheit).

3. **Beispiel**:
   - Getter und Setter für eine Temperaturklasse:
     - Getter: Berechnung von `fahrenheit` basierend auf `celsius`.
     - Setter: Validierung von `celsius` und Umrechnung von `fahrenheit` in `celsius`.

4. **Verwendung**:
   - Getter und Setter bieten eine flexible Möglichkeit, Eigenschaften zu lesen und zu schreiben, ohne die interne Logik der Klasse offenzulegen.
   - Sie sind nützlich für Validierung, berechnete Eigenschaften und das Observer-Pattern.



### Klassenvererbung

Vererbung bedeutet, dass eine Klasse (die Subklasse) von einer anderen Klasse (der Superklasse) erbt.
Die Subklasse übernimmt Eigenschaften und Methoden der Superklasse und kann sie erweitern oder anpassen.

Super bzw Elternklasse:
```dart
class Fahrzeug {
  String typ;

  // Konstruktor der Superklasse
  Fahrzeug(this.typ);

  void fahren() {
    print('$typ fährt.');
  }
}

```

und hier ein beispiel für die sub bzw kindklasse:

```dart
class Auto extends Fahrzeug {
  int ps;

  // Konstruktor der Subklasse
  Auto(this.ps) : super('Auto'); // Ruft den Konstruktor der Superklasse auf

  @override
  void fahren() {
    super.fahren(); // Ruft die Methode der Superklasse auf
    print('Das Auto hat $ps PS.');
  }
}
```

### Mixins

Mixins sind ein mächtiges Werkzeug in Dart, um **Codewiederverwendung** und **Modularität** zu fördern. Sie ermöglichen es, Funktionalität **horizontal** (über verschiedene Klassenhierarchien hinweg) zu teilen, anstatt nur **vertikal** durch Vererbung. 

Ein Mixin ist wie eine Art "Baukasten", mit dem du Methoden und Eigenschaften in mehrere Klassen einfügen kannst, ohne dass diese Klassen direkt miteinander verwandt sein müssen. 

#### **Syntax-Beispiel für Mixins:**
```dart
mixin Fliegen {
  void fliegen() {
    print('Ich kann fliegen!');
  }
}

class Vogel with Fliegen {}
class Flugzeug with Fliegen {}

void main() {
  var vogel = Vogel();
  vogel.fliegen(); // Ausgabe: Ich kann fliegen!

  var flugzeug = Flugzeug();
  flugzeug.fliegen(); // Ausgabe: Ich kann fliegen!
}
```

#### **Warum Mixins verwenden?**
- **Code teilen**: Mixins erlauben es, wiederverwendbare Funktionalität in verschiedene Klassen einzufügen.
- **Flexibilität**: Sie sind nicht an eine bestimmte Klassenhierarchie gebunden.
- **Häufige Verwendung in Flutter**: Mixins werden oft genutzt, um gemeinsame Funktionalitäten zu implementieren.

**Fazit**: Mixins sind ein mächtiges Werkzeug für Codewiederverwendung und Modularität in Dart. Sie ermöglichen es, Funktionalität horizontal (über verschiedene Klassenhierarchien hinweg) statt vertikal (durch Vererbung) zu teilen. In Flutter werden Mixins häufig verwendet, um gemeinsame Funktionalitäten zu implementieren.

### Extensions / Erweiterungsmethoden (Extension Methods)

**Was sind Erweiterungsmethoden?**
- Erweiterungsmethoden wurden in Dart 2.7 eingeführt.
- Sie ermöglichen es, bestehenden Klassen neue Funktionalitäten hinzuzufügen, ohne die Klassen selbst zu verändern oder von ihnen zu erben.
- Besonders nützlich, wenn du den Quellcode einer Klasse nicht ändern kannst (z. B. bei Standardbibliotheksklassen).

#### **Einfaches Beispiel:**
```dart
// Erweiterung für den String-Typ
extension StringErweiterungen on String {
  bool istEmail() {
    return contains('@') && contains('.');
  }

  String kapitalisieren() {
    if (isEmpty) return this;
    return '${this[0].toUpperCase()}${substring(1)}';
  }
}

void main() {
  var email = 'beispiel@example.com';
  print(email.istEmail()); // true
  print('dart'.kapitalisieren()); // Dart
}
```

#### **Warum Erweiterungsmethoden verwenden?**
- **Codewiederverwendung**: Du kannst häufig benötigte Funktionen für bestehende Klassen definieren.
- **Keine Vererbung nötig**: Funktionalität wird hinzugefügt, ohne die Klassenhierarchie zu beeinflussen.
- **Lesbarkeit**: Erweiterungsmethoden fördern eine flüssige und ausdrucksstarke Programmierung.

#### **Erweiterte Beispiele:**
- Erweiterungen können auch für primitive Typen wie `int` oder komplexere Datenstrukturen wie `List` verwendet werden.
- Sie sind besonders nützlich in Flutter, um Funktionalität zu Widgets oder dem `BuildContext` hinzuzufügen.
Beispiel zur Syntax bei vererbung einer superklasse aus einer API bibliothek:

```dart

// Superklasse (z. B. aus einer API-Bibliothek)
class HttpResponse {
  final int statusCode;
  final List<int> bodyBytes;

  HttpResponse(this.statusCode, {required this.bodyBytes});

  String get body => String.fromCharCodes(bodyBytes);
}

// Subklasse, die von HttpResponse erbt
class CustomHttpResponse extends HttpResponse {
  CustomHttpResponse(int statusCode, {required List<int> bodyBytes})
      : super(statusCode, bodyBytes: bodyBytes);

  // Neue Methode hinzufügen
  bool isSuccess() {
    return statusCode >= 200 && statusCode < 300;
  }

  // Bestehende Methode erweitern oder anpassen
  @override
  String get body => super.body.toUpperCase(); // Beispiel: Body in Großbuchstaben
}

void main() {
  var response = CustomHttpResponse(200, bodyBytes: [104, 101, 108, 108, 111]); // "hello"
  print(response.isSuccess()); // true
  print(response.body); // HELLO
}

```


#### **Fazit:**
Erweiterungsmethoden sind ein leistungsstarkes Werkzeug, um bestehenden Klassen neue Funktionen hinzuzufügen, ohne deren Quellcode zu ändern. Sie fördern eine saubere, modulare und wiederverwendbare Codebasis und sind besonders hilfreich in Flutter, um gemeinsame Funktionalitäten zu implementieren.


### Operatorüberladung in Dart

Die Operatorüberladung in Dart ermöglicht es, das Verhalten von Operatoren wie `+`, `-`, `*`, `==` und anderen für benutzerdefinierte Klassen anzupassen. Dadurch können Klassen so gestaltet werden, dass sie sich natürlicher und intuitiver verwenden lassen. Ein Beispiel ist die Klasse `Vektor`, die mathematische Vektoren repräsentiert:

```dart
class Vektor {
  final double x;
  final double y;

  const Vektor(this.x, this.y);

  // Überladung des + Operators
  Vektor operator +(Vektor other) {
    return Vektor(x + other.x, y + other.y);
  }

  // Überladung des - Operators
  Vektor operator -(Vektor other) {
    return Vektor(x - other.x, y - other.y);
  }

  // Überladung des * Operators (Skalarprodukt)
  double operator *(Vektor other) {
    return x * other.x + y * other.y;
  }

  // Überladung des negate Operators
  Vektor operator -() {
    return Vektor(-x, -y);
  }

  // Überladung des == Operators
  @override
  bool operator ==(Object other) {
    if (identical(this, other)) return true;
    return other is Vektor && other.x == x && other.y == y;
  }

  @override
  int get hashCode => x.hashCode ^ y.hashCode;

  @override
  String toString() => 'Vektor($x, $y)';
}
```

### Vorteile der Operatorüberladung
- **Lesbarkeit**: Der Code wird lesbarer, da domänenspezifische Operationen wie Vektoraddition oder Skalarprodukte direkt mit Operatoren ausgedrückt werden können.
- **Intuitivität**: Benutzerdefinierte Klassen können sich wie eingebaute Datentypen verhalten.

### Wichtige Hinweise
- **Konsistenz**: Überladene Operatoren sollten sich so verhalten, wie man es von ihnen erwartet. Zum Beispiel sollte der `+` Operator immer eine Addition repräsentieren.
- **Ergänzungen**: Wenn der `==` Operator überladen wird, sollte auch die `hashCode`-Methode überschrieben werden, um Konsistenz zu gewährleisten.

### Beispielanwendung
```dart
void main() {
  var v1 = Vektor(3, 4);
  var v2 = Vektor(1, 2);

  print(v1 + v2); // Vektor(4, 6)
  print(v1 - v2); // Vektor(2, 2)
  print(v1 * v2); // 11.0
  print(-v1);     // Vektor(-3, -4)
  print(v1 == Vektor(3, 4)); // true
}
```

Die Operatorüberladung ist ein mächtiges Werkzeug, sollte jedoch mit Bedacht eingesetzt werden, um Missverständnisse zu vermeiden.



## Collections und Generics in Dart
### Queues / Warteschlangen in Dart

Dart bietet mit der `dart:collection`-Bibliothek die Möglichkeit, Queues (Warteschlangen) zu verwenden, die sich besonders für FIFO (First-In-First-Out) oder LIFO (Last-In-First-Out) Operationen eignen. Queues bieten effizientere Einfüge- und Entfernungsoperationen am Anfang der Collection im Vergleich zu Listen.

#### Beispiel:
```dart
import 'dart:collection';

void main() {
  // Erstellen einer Queue
  Queue<String> warteschlange = Queue<String>();

  // Elemente hinzufügen
  warteschlange.add('Erster'); // Fügt am Ende hinzu
  warteschlange.add('Zweiter');
  warteschlange.addFirst('Neuer Erster'); // Fügt am Anfang hinzu
  warteschlange.addLast('Letzter'); // Fügt am Ende hinzu
  print(warteschlange); // (Neuer Erster, Erster, Zweiter, Letzter)

  // Elemente entfernen
  String erster = warteschlange.removeFirst(); // 'Neuer Erster'
  String letzter = warteschlange.removeLast(); // 'Letzter'
  print(warteschlange); // (Erster, Zweiter)

  // Queue durchlaufen
  for (var element in warteschlange) {
    print(element);
  }
}
```

#### Vorteile von Queues:
- **FIFO und LIFO:** Unterstützt sowohl First-In-First-Out als auch Last-In-First-Out Operationen.
- **Effizienz:** Bietet effizientere Einfüge- und Entfernungsoperationen am Anfang der Collection im Vergleich zu Listen.

### Unveränderliche Collections

Dart bietet auch unveränderliche (immutable) Versionen der Collection-Typen an, die nach ihrer Erstellung nicht mehr geändert werden können.

#### Beispiele:
```dart
// Unveränderliche Listen
List<int> veränderlicheZahlen = [1, 2, 3];
List<int> unveränderlicheZahlen = List.unmodifiable(veränderlicheZahlen);
// unveränderlicheZahlen.add(4); // Fehler: Kann nicht modifiziert werden

// Unveränderliche Sets
Set<String> veränderlicheFrüchte = {'Apfel', 'Banane'};
Set<String> unveränderlicheFrüchte = Set.unmodifiable(veränderlicheFrüchte);

// Unveränderliche Maps
Map<String, int> veränderlicheAlter = {'Anna': 30, 'Ben': 25};
Map<String, int> unveränderlicheAlter = Map.unmodifiable(veränderlicheAlter);
```

#### Vorteile von unveränderlichen Collections:
- **Datenintegrität:** Garantiert, dass Daten nicht versehentlich geändert werden.
- **Nebenläufigkeit:** Besonders hilfreich in nebenläufigen Kontexten.
- **Sicherheit:** Ideal bei der Übergabe von Daten an andere Funktionen.

### Generics
Generics einfach wie Platzhalter für Typen. 

Normalerweise sagst du in Dart:

int zahl = 5;
String text = "Hallo";

Mit Generics sagst du:
👉 „Ich weiß noch nicht, welcher Typ hier reinkommt — das entscheide ich später.“

Dafür nutzt man sowas wie <T>
(T steht einfach für „Type“, könnte auch <X> heißen)


Generics sind also Platzhalter für Typen. Sie ermöglichen es dir, Klassen, Funktionen oder Collections so zu schreiben, dass sie mit verschiedenen Typen arbeiten können, ohne die Typsicherheit zu verlieren.

### Generische Collections
Generische Collections wie `List<T>`, `Set<T>` (T für Type als Typparameter) und `Map<K, V>` (K und V für Key und Value) erlauben es, den Typ der enthaltenen Elemente zu spezifizieren. Dies verbessert die Typprüfung und die IDE-Unterstützung. Beispiele:
- `List<String> namen = ['Anna', 'Ben', 'Clara'];`
- `Set<int> zahlenSet = {1, 2, 3};`
- `Map<String, double> gewichte = {'Apfel': 0.2, 'Banane': 0.15};`

### Generische Klassen
Eigene generische Klassen können erstellt werden, um wiederverwendbare und typsichere Komponenten zu entwickeln. 

📦 **Beispiel: Eine Box**

Ohne Generics:
```dart
class Box {
  final dynamic wert;
  Box(this.wert);
}
```
Problem:
👉 dynamic ist unsicher (kann alles sein → Fehler erst zur Laufzeit)

Mit Generics:
```dart
class Box<T> {
  final T wert;
  Box(this.wert);
  T öffnen() => wert;
}
```
Verwendung:
- `var stringBox = Box<String>('Hallo');`
- `var intBox = Box<int>(42);`

### Mehrere Typparameter
Generische Typen können mehrere Typparameter haben, wie in der Klasse `Paar<K, V>`:
```dart
class Paar<K, V> {
  final K erster;
  final V zweiter;
  Paar(this.erster, this.zweiter);
}
```

### Generische Methoden
Auch Methoden können generisch sein, unabhängig von der Klasse:
```dart
T ersteElement<T>(List<T> liste) {
  if (liste.isEmpty) {
    throw ArgumentError('Liste darf nicht leer sein');
  }
  return liste.first;
}
```

### Einschränkung von Typparametern
Mit `extends` können Typparameter eingeschränkt werden, um nur bestimmte Typen zuzulassen. Beispiel:
```dart
class NummerBox<T extends num> {
  final T wert;
  NummerBox(this.wert);
  double quadrat() => wert * wert;
}
```

### Generische Mixins
Mixins können ebenfalls generisch sein, um die Wiederverwendbarkeit zu erhöhen:
```dart
mixin Loggable<T> {
  void log(T wert) {
    print('Log: $wert');
  }
}
```

Generics bieten in Dart eine leistungsstarke Möglichkeit, flexiblen und dennoch typsicheren Code zu schreiben.


### Collection-Operationen

## Zusammenfassung: Funktionale Methoden für Collections

Funktionale Methoden in Dart ermöglichen es, Operationen auf Collections einfach und deklarativ auszudrücken. Hier ist eine vereinfachte Übersicht der wichtigsten Methoden und ihrer Bedeutungen:

| Methode      | Bedeutung                     | Beschreibung |
|--------------|-------------------------------|--------------|
| **map**      | verändern                     |Transformiert jedes Element der Collection und gibt eine neue Collection zurück|
| **where**    | filtern                       | Filtert die Collection und gibt eine neue Collection mit Elementen zurück, die eine Bedingung erfüllen|
| **firstWhere** | erstes passendes            | Findet das erste Element, das eine Bedingung erfüllt|
| **reduce**   | zusammenrechnen               |Reduziert die Collection auf einen einzelnen Wert durch Anwendung einer Funktion auf aufeinanderfolgende Elemente|
| **fold**     | zusammenrechnen mit Startwert | Ähnlich wie reduce, aber mit einem expliziten Anfangswert|
| **any**      | gibt es eins?                 | Prüft, ob mindestens ein Element eine Bedingung erfüllt|
| **every**    | sind alle so?                 |  Prüft, ob alle Elemente eine Bedingung erfüllen|
| **expand**   | flach machen                  |Erzeugt eine flache Liste aus einer Collection von Collections|
| **forEach**  | für jedes Element etwas tun   |Führt eine Funktion für jedes Element aus|

### Beispiele für die Methoden

- **map**: Verändert jedes Element und gibt eine neue Collection zurück.
  ```dart
  var zahlen = [1, 2, 3];
  var quadriert = zahlen.map((zahl) => zahl * zahl).toList(); // [1, 4, 9]
  ```

- **where**: Filtert Elemente basierend auf einer Bedingung.
  ```dart
  var zahlen = [1, 2, 3, 4];
  var gerade = zahlen.where((zahl) => zahl % 2 == 0).toList(); // [2, 4]
  ```

- **reduce**: Reduziert die Collection auf einen Wert.
  ```dart
  var zahlen = [1, 2, 3];
  var summe = zahlen.reduce((a, b) => a + b); // 6
  ```

- **fold**: Wie reduce, aber mit Startwert.
  ```dart
  var zahlen = [1, 2, 3];
  var summe = zahlen.fold(10, (a, b) => a + b); // 16
  ```

- **any**: Prüft, ob mindestens ein Element eine Bedingung erfüllt.
  ```dart
  var zahlen = [1, 2, 3];
  var hatGerade = zahlen.any((zahl) => zahl % 2 == 0); // true
  ```

- **every**: Prüft, ob alle Elemente eine Bedingung erfüllen.
  ```dart
  var zahlen = [2, 4, 6];
  var alleGerade = zahlen.every((zahl) => zahl % 2 == 0); // true
  ```

- **firstWhere**: Findet das erste Element, das eine Bedingung erfüllt.
  ```dart
  var zahlen = [1, 2, 3];
  var ersteGerade = zahlen.firstWhere((zahl) => zahl % 2 == 0); // 2
  ```

- **expand**: Macht eine Liste von Listen flach.
  ```dart
  var listen = [[1, 2], [3, 4]];
  var flach = listen.expand((liste) => liste).toList(); // [1, 2, 3, 4]
  ```

- **forEach**: Führt eine Aktion für jedes Element aus.
  ```dart
  var früchte = ['Apfel', 'Banane'];
  früchte.forEach((frucht) => print('Ich mag $frucht'));
  ```

Diese Methoden machen den Code kürzer, lesbarer und ausdrucksstärker. Sie sind besonders nützlich, wenn du mit Collections arbeitest und komplexe Operationen deklarativ ausdrücken möchtest.

## Verketten von Collection-Operationen

Ein großer Vorteil der funktionalen Methoden ist, dass sie verkettet werden können, um komplexe Transformationen als eine Folge einfacherer Operationen auszudrücken:

```dart
var personen = [
  {'name': 'Anna', 'alter': 30, 'stadt': 'Berlin'},
  {'name': 'Ben', 'alter': 25, 'stadt': 'München'},
  {'name': 'Clara', 'alter': 35, 'stadt': 'Berlin'},
  {'name': 'David', 'alter': 28, 'stadt': 'Hamburg'},
  {'name': 'Eva', 'alter': 32, 'stadt': 'Berlin'},
];

// Finde das durchschnittliche Alter von Personen aus Berlin
double durchschnittsalterBerlin = personen
  .where((person) => person['stadt'] == 'Berlin')
  .map((person) => person['alter'] as int)
  .reduce((summe, alter) => summe + alter) /
  personen.where((person) => person['stadt'] == 'Berlin').length;
print(durchschnittsalterBerlin); // (30 + 35 + 32) / 3 = 32.33...

// Namen aller Personen über 30, alphabetisch sortiert
List<String> namenÜber30 = personen
  .where((person) => (person['alter'] as int) > 30)
  .map((person) => person['name'] as String)
  .toList()
  ..sort();
print(namenÜber30); // [Clara, Eva]
```

## Collection Controls in Dart

Collection Controls ermöglichen es, Listen und Maps dynamisch beim Erstellen zu bauen. Hier sind die wichtigsten Konzepte einfach erklärt:

### 1. Collection if
Mit `if` kannst du Elemente nur dann hinzufügen, wenn eine Bedingung erfüllt ist.

```dart
var liste = [
  "Apfel",
  if (true) "Banane",
  "Kirsche"
];
// Ergebnis: ["Apfel", "Banane", "Kirsche"]

var map = {
  "Apfel": 1,
  if (true) "Banane": 2,
};
// Ergebnis: {"Apfel": 1, "Banane": 2}
```

### 2. Collection for
Mit `for` kannst du eine Liste direkt beim Erstellen transformieren.

```dart
var zahlen = [1, 2, 3];
var quadriert = [
  for (var z in zahlen) z * z
];
// Ergebnis: [1, 4, 9]

var gerade = [
  for (var z in zahlen)
    if (z % 2 == 0) z * z
];
// Ergebnis: [4]

var fruits = ["Apfel", "Banane"];
var map = {
  for (var f in fruits)
    f: f.length
};
// Ergebnis: {"Apfel": 5, "Banane": 6}
```

### 3. Spread Operator `...`
Der Spread-Operator fügt Elemente einer Liste in eine andere Liste ein.

```dart
var a = [1, 2];
var b = [3, 4];
var neu = [...a, ...b];
// Ergebnis: [1, 2, 3, 4]

var extra = true ? [5, 6] : [];
var liste = [...a, ...extra];

List<int>? maybe = null;
var liste = [...a, ...?maybe];
// Null-sicher: kein Crash!
```

### 4. Pattern Matching (Dart 3)
Pattern Matching hilft, Listen und Maps zu "zerlegen" und Variablen direkt zuzuweisen.

```dart
// Listen auspacken
var liste = [1, 2, 3];
var [a, b, c] = liste;
// a = 1, b = 2, c = 3

// Rest nehmen
var [first, second, ...rest] = [1, 2, 3, 4];
// first = 1, second = 2, rest = [3, 4]

// Map auspacken
var person = {"name": "Anna", "alter": 30};
var {"name": name, "alter": alter} = person;
// name = "Anna", alter = 30

// Pattern Matching in switch
var wert = [1, 2];
switch (wert) {
  case [var x, var y]:
    print(x + y);
}
// Erkennt automatisch: "Liste mit 2 Elementen"
```

### Mini-Zusammenfassung
- **Collection if**: Element nur hinzufügen, wenn Bedingung true.
- **Collection for**: Liste direkt transformieren.
- **Spread (`...`)**: Liste in Liste einfügen.
- **Spread null-safe (`...?`)**: Nur wenn nicht null.
- **Pattern Matching**: Collections "auseinandernehmen" und Variablen erstellen.


## Asynchrone Programmierung in Dart

In Dart wird asynchrone Programmierung hauptsächlich durch zwei Konzepte unterstützt:
- Futures: Repräsentieren einen einzelnen asynchronen Wert, der in der Zukunft verfügbar sein wird
- Streams: Repräsentieren eine Sequenz asynchroner Ereignisse über Zeit

### Futures

Ein **Future** ist wie ein promise in JavaScript.

- Das Ergebnis ist **jetzt noch nicht da**.
- Es kommt **später** (oder es gibt einen Fehler).

### Denkmodell in 1 Minute

Wenn du eine Future-Funktion aufrufst, passiert Folgendes:

1. Die Funktion startet eine asynchrone Arbeit.
2. Dein Programm läuft **sofort weiter** (blockiert nicht).
3. Später endet die Arbeit mit:
   - einem Wert (Erfolg) oder
   - einem Fehler.

Das ist wichtig für Flutter, damit die UI flüssig bleibt.

---

### Einfaches Beispiel mit then, catchError, whenComplete

```dart
Future<String> fetchUserData() {
  return Future.delayed(const Duration(seconds: 2), () {
    return 'User data loaded';
  });
}

void main() {
  print('Fetching user data...');

  fetchUserData()
      .then((data) {
        print('Data received: $data');
      })
      .catchError((error) {
        print('Error: $error');
      })
      .whenComplete(() {
        print('Operation completed');
      });

  print('Main function continues executing');
}
```

Merke:
- `then(...)`: läuft bei Erfolg.
- `catchError(...)`: läuft bei Fehler.
- `whenComplete(...)`: läuft immer (ähnlich wie `finally`).

---

### Wichtige Future-Konstruktoren

```dart
Future<int> sofortiger = Future.value(42);
Future<int> fehlerhafter = Future.error(Exception('Something went wrong'));

Future<String> verzoegerter = Future.delayed(
  const Duration(seconds: 1),
  () => 'Delayed result',
);

Future<int> zukunft = Future(() {
  return 123;
});
```

Wann welcher?
- `Future.value(...)`: Ergebnis ist direkt bekannt.
- `Future.error(...)`: gezielt einen Fehler-Future erzeugen.
- `Future.delayed(...)`: Verzögerung simulieren (z. B. Netzwerk).
- `Future(() { ... })`: asynchrone Berechnung starten.

---

### Futures verketten (Schritt für Schritt)

```dart
Future<String> getUserName() {
  return Future.delayed(const Duration(seconds: 1), () => 'Anna');
}

Future<int> getUserAge(String name) {
  return Future.delayed(const Duration(seconds: 1), () {
    if (name == 'Anna') return 30;
    throw Exception('User not found');
  });
}

Future<String> createGreeting(String name, int age) {
  return Future.value('Hallo, $name! Du bist $age Jahre alt.');
}

void main() {
  getUserName()
      .then((name) => getUserAge(name))
      .then((age) => createGreeting('Anna', age))
      .then((greeting) => print(greeting))
      .catchError((e) => print('Error: $e'));
}
```

Jeder `then` wartet auf den vorherigen Schritt.

---

### Fehlerbehandlung mit Fallback

```dart
Future<double> divideNumbers(int a, int b) {
  return Future(() {
    if (b == 0) {
      throw Exception('Division by zero');
    }
    return a / b;
  });
}

void main() {
  divideNumbers(10, 0)
      .then((result) => print('Result: $result'))
      .catchError((error) {
        print('Caught error: $error');
        return 0.0; // Fallback-Wert
      })
      .then((value) => print('Final value: $value'));
}
```

Didaktischer Punkt:
- `catchError` kann nicht nur loggen, sondern auch einen Ersatzwert liefern.

---

### Selektiv Fehler abfangen

```dart
import 'dart:async';
import 'dart:math';

Future<Object> riskyOperation() {
  return Future(() {
    final random = Random().nextInt(3);
    switch (random) {
      case 0:
        return 'Success';
      case 1:
        throw FormatException('Invalid format');
      default:
        throw TimeoutException('Operation timed out');
    }
  });
}

void main() {
  riskyOperation()
      .then((result) => print('Success: $result'))
      .catchError(
        (error) => print('Format error: $error'),
        test: (error) => error is FormatException,
      )
      .catchError(
        (error) => print('Timeout error: $error'),
        test: (error) => error is TimeoutException,
      )
      .catchError((error) => print('Unknown error: $error'));
}
```

Mit `test:` filterst du gezielt Fehlertypen.

---

### Mehrere Futures gleichzeitig

```dart
Future<String> fetchData1() =>
    Future.delayed(const Duration(seconds: 1), () => 'Data 1');
Future<String> fetchData2() =>
    Future.delayed(const Duration(seconds: 2), () => 'Data 2');
Future<String> fetchData3() =>
    Future.delayed(const Duration(seconds: 3), () => 'Data 3');

void main() {
  Future.wait([fetchData1(), fetchData2(), fetchData3()]).then((results) {
    print('All results: $results');
  });

  Future.any([fetchData1(), fetchData2(), fetchData3()]).then((result) {
    print('First result: $result');
  });
}
```

Unterschied:
- `Future.wait(...)`: wartet auf **alle**.
- `Future.any(...)`: nimmt das **erste** fertige Ergebnis.

Wichtig bei `wait`: Die Ergebnisliste ist in der **Eingabe-Reihenfolge**, nicht in der Reihenfolge der Fertigstellung.

---

### Häufige Stolperfallen

- Fehler in Futures ohne `catchError` gehen leicht verloren.
- Zu lange Ketten werden schnell unübersichtlich.
- Nicht vergessen: Asynchron heißt, dass Code-Reihenfolge im Quelltext nicht automatisch Ausführungsreihenfolge bedeutet.

---

### Mini-Merkliste

- Future = ein späterer Einzelwert oder Fehler.
- `then` = Erfolg, `catchError` = Fehler, `whenComplete` = immer.
- `Future.wait` für "alles parallel und dann weiter".
- `Future.any` für "das schnellste Ergebnis reicht".


## Async und Await in Dart

Mit `async` und `await` kannst du asynchronen Code so schreiben, dass er fast wie synchroner Code aussieht.
Das macht Abläufe meist leichter lesbar als lange `then(...)`-Ketten.

### Grundidee

- `async` markiert eine Funktion als asynchron.
- Eine `async`-Funktion liefert immer einen `Future` zurück.
- `await` wartet auf das Ergebnis eines `Future`.

Wichtig:
- `await` pausiert nur die aktuelle Funktion.
- Der Rest der App (z. B. UI) läuft weiter.

---

### Einfaches Beispiel mit async/await

```dart
Future<String> getUserName() async {
  return Future.delayed(const Duration(seconds: 1), () => 'Anna');
}

Future<int> getUserAge(String username) async {
  return Future.delayed(const Duration(seconds: 1), () => 30);
}

Future<String> fetchUserData() async {
  try {
    final username = await getUserName();
    final age = await getUserAge(username);
    return 'User: $username, Age: $age';
  } catch (e) {
    return 'Error fetching user data: $e';
  }
}

Future<void> main() async {
  print('Fetching user data...');
  final userData = await fetchUserData();
  print(userData);
  print('Operation completed');
}
```

Didaktisch wichtig:
- Die Schritte stehen von oben nach unten in natürlicher Reihenfolge.
- Das ist meist einfacher zu lesen und zu debuggen.

---

### Gleiches Verhalten mit then-Kette (zum Vergleich)

```dart
Future<String> fetchUserData() {
  return getUserName().then((username) {
    return getUserAge(username).then((age) {
      return 'User: $username, Age: $age';
    });
  }).catchError((e) {
    return 'Error fetching user data: $e';
  });
}
```

Beide Varianten funktionieren.
`async/await` ist aber bei mehreren Schritten oft klarer.

---

### Fehlerbehandlung mit try/catch/finally

```dart
Future<double> divideNumbers(int a, int b) async {
  if (b == 0) {
    throw Exception('Division by zero');
  }
  return a / b;
}

Future<void> main() async {
  try {
    final result = await divideNumbers(10, 0);
    print('Result: $result');
  } catch (e) {
    print('Caught error: $e');
  } finally {
    print('Operation completed');
  }
}
```

Vorteil:
- Fehlerbehandlung fühlt sich an wie bei synchronem Code.

---

### Parallel arbeiten mit async/await

```dart
Future<String> fetchData1() =>
    Future.delayed(const Duration(seconds: 1), () => 'Data 1');
Future<String> fetchData2() =>
    Future.delayed(const Duration(seconds: 2), () => 'Data 2');
Future<String> fetchData3() =>
    Future.delayed(const Duration(seconds: 3), () => 'Data 3');

Future<void> performParallelTasks() async {
  print('Starting parallel tasks...');

  // 1) Alle drei Futures gleichzeitig starten
  final future1 = fetchData1();
  final future2 = fetchData2();
  final future3 = fetchData3();

  // 2) Danach auf Ergebnisse warten
  final result1 = await future1;
  final result2 = await future2;
  final result3 = await future3;

  print('Results: $result1, $result2, $result3');

  // Alternative: kompakt mit Future.wait
  final allResults = await Future.wait([
    fetchData1(),
    fetchData2(),
    fetchData3(),
  ]);
  print('All results: $allResults');
}
```

Merke:
- Wenn du sofort hintereinander `await` auf neue Aufrufe machst, laufen sie nacheinander.
- Wenn du zuerst Futures startest und dann awaitest, laufen sie parallel.

---

### Typischer Anfängerfehler

Nicht parallel (langsamer):

```dart
final a = await fetchData1();
final b = await fetchData2();
final c = await fetchData3();
```

Parallel (oft schneller):

```dart
final f1 = fetchData1();
final f2 = fetchData2();
final f3 = fetchData3();

final a = await f1;
final b = await f2;
final c = await f3;
```

---

### Isolate leicht erklärt

Ein **Isolate** ist in Dart eine eigene Ausführungseinheit mit:

- eigenem Speicher
- eigenem Event-Loop

Wichtig für dein Verständnis:

- Standardmäßig läuft deine App im **Main-Isolate**.
- `async/await` arbeitet innerhalb dieses Isolates.
- `await` pausiert nur die aktuelle Funktion, nicht das ganze Isolate.
- Deshalb können andere Aufgaben (z. B. UI-Events) weiterlaufen.

Unterschied zu Threads in anderen Sprachen:

- Isolates teilen **keinen** Speicher.
- Kommunikation läuft über Nachrichten.
- Das reduziert typische Race-Condition-Probleme.

Praxis-Merke:

- Für I/O-Wartezeiten (Netzwerk, Datei, Datenbank): `async/await` reicht meist.
- Für lange, rechenintensive Arbeit: eigenes Isolate starten, damit die UI flüssig bleibt.

---

### Mini-Zusammenfassung

- `async/await` macht Future-Code meist lesbarer.
- `await` pausiert nur die aktuelle Funktion, nicht das gesamte Main-Isolate.
- `try/catch/finally` ist der natürliche Weg für Fehlerbehandlung.
- Für parallele Tasks: erst starten, dann awaiten, oder direkt `Future.wait` nutzen.


## Streams in Dart

Ein **Stream** ist wie ein Future – aber statt eines einzelnen Wertes liefert er **eine Folge von Werten über die Zeit**.

- Ein Future: „Ich gebe dir irgendwann **einen** Wert."
- Ein Stream: „Ich sende dir **mehrere** Werte, einen nach dem anderen."

### Denkmodell in 1 Minute

Stell dir vor, du horchst auf ein Radio:
- Nicht du fragst, wann etwas kommt.
- Das Radio **sendet** – und du hörst zu.

Das ist ein Stream. Er sendet Ereignisse, und du reagierst darauf.

---

### Einfaches Beispiel mit `listen`

```dart
Stream<int> countStream(int max) async* {
  for (int i = 1; i <= max; i++) {
    await Future.delayed(const Duration(seconds: 1));
    yield i;
  }
}

void main() {
  final subscription = countStream(5).listen(
    (data) => print('Data: $data'),
    onError: (error) => print('Error: $error'),
    onDone: () => print('Stream completed'),
    cancelOnError: false,
  );

  // Subscription nach 3 Sekunden abbrechen
  Future.delayed(const Duration(seconds: 3), () {
    subscription.cancel();
    print('Subscription cancelled');
  });
}
// Ausgabe:
// Data: 1
// Data: 2
// Subscription cancelled
```

Merke:
- `listen(...)`: horcht auf eingehende Werte.
- `onError`: reagiert auf Fehler.
- `onDone`: läuft, wenn der Stream beendet ist.
- `cancelOnError: false`: Stream läuft trotz Fehler weiter.
- `subscription.cancel()`: Abonnement jederzeit beendbar.

---

### Wichtige Stream-Konstruktoren

```dart
// async*-Generator: klassisch, schrittweise
Stream<int> mitGenerator(int max) async* {
  for (int i = 1; i <= max; i++) {
    await Future.delayed(const Duration(seconds: 1));
    yield i;
  }
}

// StreamController: manuell steuern
import 'dart:async';
StreamController<String> mitController() {
  final controller = StreamController<String>();
  controller.add('Erstes Ereignis');
  controller.add('Zweites Ereignis');
  controller.addError('Etwas lief schief');
  controller.close();
  return controller;
}

// Aus Futures zusammensetzen
Stream<int> ausFutures() {
  return Stream.fromFutures([
    Future.delayed(const Duration(seconds: 1), () => 1),
    Future.delayed(const Duration(seconds: 2), () => 2),
    Future.delayed(const Duration(seconds: 3), () => 3),
  ]);
}

// Periodisch in festem Takt
Stream<int> periodisch() {
  return Stream.periodic(const Duration(seconds: 1), (count) => count + 1).take(5);
}
```

Wann welcher?
- `async*` mit `yield`: am häufigsten, gut lesbar.
- `StreamController`: wenn Ereignisse von außen kommen (z. B. Nutzereingaben).
- `Stream.fromFutures`: wenn Futures zu einem Stream gebündelt werden sollen.
- `Stream.periodic`: für regelmäßige Ereignisse (z. B. Timer, Animationsframes).

---

### Stream-Transformationen

Streams unterstützen dieselben Operationen wie Listen – aber asynchron, Wert für Wert:

```dart
Stream<int> numberStream() async* {
  for (int i = 1; i <= 5; i++) {
    await Future.delayed(const Duration(milliseconds: 500));
    yield i;
  }
}

void main() async {
  // map – jeden Wert transformieren
  numberStream()
      .map((n) => n * 2)
      .listen((data) => print('Doubled: $data'));

  // where – nur passende Werte durchlassen
  numberStream()
      .where((n) => n % 2 == 0)
      .listen((data) => print('Even: $data'));

  // take – nur die ersten N Werte
  numberStream()
      .take(3)
      .listen((data) => print('Taken: $data'));

  // skip – die ersten N Werte überspringen
  numberStream()
      .skip(2)
      .listen((data) => print('Skipped first 2: $data'));

  // distinct – aufeinanderfolgende Duplikate entfernen
  Stream.fromIterable([1, 1, 2, 2, 3, 3, 4])
      .distinct()
      .listen((data) => print('Distinct: $data'));

  // Transformationen verketten
  numberStream()
      .where((n) => n % 2 == 1)
      .map((n) => n * n)
      .listen((data) => print('Odd squares: $data'));
}
```

Merke:
- Transformationen laufen asynchron – Schritt für Schritt mit jedem neuen Wert.
- Sie können beliebig verkettet werden, ähnlich wie bei Collections.

---

### Fehlerbehandlung in Streams

```dart
Stream<int> errorStream() async* {
  for (int i = 1; i <= 5; i++) {
    await Future.delayed(const Duration(milliseconds: 500));
    if (i == 3) throw Exception('Fehler bei Element 3');
    yield i;
  }
}

void main() {
  // Variante 1: onError im listen-Aufruf
  errorStream().listen(
    (data) => print('Data: $data'),
    onError: (error) => print('Fehler abgefangen: $error'),
    onDone: () => print('Stream abgeschlossen'),
    cancelOnError: false,
  );

  // Variante 2: handleError als Transformation
  errorStream()
      .handleError((error) => print('Behandelter Fehler: $error'))
      .listen(
        (data) => print('Daten nach Fehlerbehandlung: $data'),
        onDone: () => print('Stream abgeschlossen'),
      );
}
```

Didaktischer Punkt:
- `cancelOnError: false` lässt den Stream nach einem Fehler weiterlaufen.
- `handleError(...)` kann wie `catchError` bei Futures einen `test:`-Parameter erhalten, um nur bestimmte Fehlertypen zu behandeln.

---

### Single-Subscription vs. Broadcast Stream

Standardmäßig kann ein Stream **nur einen Listener** haben.
Wenn mehrere Teile der App auf dieselben Ereignisse hören sollen, braucht man einen **Broadcast Stream**:

```dart
import 'dart:async';

void main() {
  // Single-Subscription: nur ein Listener erlaubt
  final singleController = StreamController<int>();
  singleController.stream.listen((data) => print('Listener 1: $data'));
  // singleController.stream.listen(...); // würde Fehler werfen!

  // Broadcast: mehrere Listener erlaubt
  final broadcastController = StreamController<int>.broadcast();
  broadcastController.stream.listen((data) => print('Broadcast 1: $data'));
  broadcastController.stream.listen((data) => print('Broadcast 2: $data'));

  broadcastController.add(1);
  broadcastController.add(2);

  Future.delayed(const Duration(seconds: 1), () {
    singleController.close();
    broadcastController.close();
  });
}
```

Unterschied:
| | Single-Subscription | Broadcast |
|---|---|---|
| Listener | genau einer | beliebig viele |
| Typischer Einsatz | einmalige Datenströme | UI-Events, State-Updates |

---

### `async*` und `yield` im Detail

```dart
// Einzelwerte ausgeben
Stream<int> countStream(int max) async* {
  for (int i = 1; i <= max; i++) {
    await Future.delayed(const Duration(seconds: 1));
    yield i;
  }
}

// Bedingt yielden
Stream<int> nurGerade(int max) async* {
  for (int i = 1; i <= max; i++) {
    await Future.delayed(const Duration(milliseconds: 500));
    if (i % 2 == 0) yield i;
  }
}

// Anderen Stream einbetten mit yield*
Stream<int> verschachtelt(int outer, int inner) async* {
  for (int i = 1; i <= outer; i++) {
    yield i;
    yield* innerStream(i, inner); // delegiert an anderen Stream
  }
}

Stream<int> innerStream(int faktor, int count) async* {
  for (int i = 1; i <= count; i++) {
    yield faktor * 10 + i;
  }
}
```

Merke:
- `yield`: fügt **einen** Wert zum Stream hinzu.
- `yield*`: delegiert an einen **anderen Stream** und fügt alle seine Werte ein.

---

### `await for` – Über Streams iterieren

Mit `await for` kannst du über einen Stream iterieren wie über eine normale Liste – aber asynchron:

```dart
Future<void> processStream() async {
  print('Verarbeitung startet...');
  await for (final data in countStream(5)) {
    print('Verarbeitet: $data');
  }
  print('Verarbeitung abgeschlossen');
}

Future<void> main() async {
  await processStream();
}
// Ausgabe:
// Verarbeitung startet...
// Verarbeitet: 1
// Verarbeitet: 2
// Verarbeitet: 3
// Verarbeitet: 4
// Verarbeitet: 5
// Verarbeitung abgeschlossen
```

Didaktisch wichtig:
- `await for` wartet auf jeden Wert, bevor der Schleifenkörper weiterläuft.
- Die Schleife endet automatisch, wenn der Stream geschlossen wird.
- Gut lesbar, wenn du alle Werte der Reihe nach verarbeiten willst.

---

### Häufige Stolperfallen

- Single-Subscription-Stream mehrfach abonnieren → Fehler zur Laufzeit.
- Subscription vergessen zu `cancel()` → Speicherlecks, besonders in Widgets.
- Transformationen auf einem bereits abonnierten Stream anwenden → neuer Stream nötig.

---

### Mini-Merkliste

- Stream = eine Folge asynchroner Werte über die Zeit.
- `listen(...)` abonniert, `cancel()` beendet das Abonnement.
- `async*` mit `yield` ist der einfachste Weg, Streams zu erstellen.
- `map`, `where`, `take`, `skip`, `distinct` funktionieren wie bei Collections – aber asynchron.
- `onError` / `handleError` für Fehlerbehandlung.
- Broadcast Stream für mehrere Listener.
- `await for` macht Stream-Iteration so lesbar wie eine normale Schleife.


### Dependency Management mit pub.dev

In der modernen Softwareentwicklung ist die Nutzung vorgefertigter Pakete entscheidend für Effizienz. Das zentrale Repository für Flutter- und Dart-Pakete, pub.dev, bietet eine Vielzahl von Tools, um deine Anwendungen zu verbessern. Hier sind die wichtigsten Punkte:

Arten von Paketen:

Dart-Pakete: Reiner Dart-Code, der in jeder Dart-Anwendung verwendet werden kann.
Flutter-Pakete: Enthalten Dart- und plattformspezifischen Code für Flutter-Apps.
Plugin-Pakete: Bieten native Implementierungen für plattformspezifische Funktionen wie Kamera oder GPS.
Effektive Strategien zur Paketsuche:

Verwende präzise Suchbegriffe (z. B. „image picker“).
Filtere nach Flutter-kompatiblen Paketen.
Erkunde beliebte und offizielle Pakete (z. B. „Flutter Favorite“).
Bleibe über Flutter-Communities und Blogs auf dem Laufenden.
Pakete zu deinem Projekt hinzufügen:

Füge das Paket manuell zur pubspec.yaml hinzu oder nutze flutter pub add.
Führe flutter pub get aus, um die Abhängigkeiten herunterzuladen.
Importiere das Paket in deinem Code (z. B. import 'package:http/http.dart';).
Versionsverwaltung:

Nutze semantische Versionierung (MAJOR.MINOR.PATCH), um Updates zu verwalten.
Die Datei pubspec.lock stellt sicher, dass die Abhängigkeitsversionen konsistent bleiben.
Erweiterte Abhängigkeitsquellen:

Gehostet (pub.dev), Git-Repositories, lokale Pfade oder SDK-Abhängigkeiten.
Eigene Pakete erstellen:

Nutze flutter create --template=package, um ein neues Paket zu erstellen.
Dokumentiere und teste dein Paket, bevor du es auf pub.dev veröffentlichst.
Durch die effektive Nutzung von pub.dev kannst du Zeit sparen, Redundanz reduzieren und dich auf die Entwicklung einzigartiger Funktionen für deine Anwendungen konzentrieren.


## Widgets

Widgets Repräsentieren Und verwalten den Zustand meiner Anwendung.
Die app besteht aus Widgets, die miteinander verschachtelt sind. Durch die Verschachtelung von Widgets entsteht ein Widgetbaum. Die Wurzel des Baums ist ein App Widget Und von dort aus verzweigt sich die Hierarchie in immer spezifischere UI Elemente.
Flutter ist ein UI Framework in dem alles in Dart geschrieben ist und dadurch kann Logik Und UI Eng miteinander verwoben werden.
Ein einfaches Beispiel für ein Widget ist ein Text-Widget:
```dart
Text('Hallo, Flutter!', style: TextStyle(fontSize: 24))

```
Virgins können auch Eigenschaften haben zum Beispiel Farbe Position und Verhalten. Diese Eigenschaften kann man verschachteln.

```dart
Container(
  padding: EdgeInsets.all(16.0),
  decoration: BoxDecoration(
    color: Colors.blue,
    borderRadius: BorderRadius.circular(8.0),
  ),
   child: Text(
    'Hallo, Flutter!',
    style: TextStyle(
      color: Colors.white,
      fontSize: 24.0,
    ),
  ),
)
```


In Flutter beschreibt man wie die UI zu einer bestimmten Zeitpunkt aussehen soll, basierend auf dem aktuellen Zustand der Anwendung. Ändert sich der Zustand, wird die Widget Beschreibung neu erstellt. Kann man beschreibt also Einfac, wie die UI für jeden möglichen Zustand aussehen soll.

Um eine Änderung in der UI zu bewirken, erstellt man ein neues Widget das die neue Konfiguration widerspiegelt. Flutter ist so optimiert dass es nur die tatsächlichen Unterschiede zwischen dem alten und dem neuen Widgetbaum aktualisiert.

Widgets and flatter haben mehrere Hauptkategorien und deren Verständnis Ist Wichtig, da sie unterschiedliche Rollen haben:

| Kategorie | Beschreibung | Beispiele |
|-----------|--------------|-----------|
| **Strukturelle und Layout-Widgets** | Definieren, wie UI-Elemente angeordnet und positioniert werden. Sie dienen als "Behälter" für andere Widgets und bestimmen deren räumliche Beziehungen. | Container, Row, Column, Stack |
| **Styling- und Anzeigewidgets** | Verantwortlich für die visuelle Darstellung von Inhalten. Konzentrieren sich auf das Aussehen und die Präsentation, nicht auf das Layout. | Text, Image, Icon |
| **Interaktive Widgets** | Akzeptieren Benutzereingaben und reagieren auf Benutzerinteraktionen. Bilden die Brücke zwischen der Benutzeroberfläche und der Anwendungslogik. | Button, TextField, Slider |
| **Containerwidgets für Zustandsverwaltung** | Helfen bei der Verwaltung und Weitergabe des Anwendungszustands durch den Widget-Baum. Entscheidend für die Entwicklung interaktiver Anwendungen. | StatefulWidget, InheritedWidget, Provider-Widgets |

### Stateless und Stateful widgets
In Flutter gibt es zwei Haupttypen von Widgets:

Stateless Widgets:

Sind unveränderlich und haben keinen inneren Zustand.
Ihre Darstellung wird ausschließlich durch die Eingabeparameter bestimmt.
Geeignet für statische UI-Elemente, wie Texte, Icons oder Container mit festen Eigenschaften.
Einfach zu implementieren: Du erstellst eine Klasse, die von StatelessWidget erbt, und überschreibst die build-Methode um die Darstellung zu definieren.

Stateful Widgets:

Können sich dynamisch ändern, da sie einen inneren Zustand besitzen.
Reagieren auf Benutzerinteraktionen und Datenänderungen.
Sie bestehen aus zwei Klassen: der Widgetklasse, die von StatefulWidget erbt und einer zweiten Klasse(dem State-Objekt), dass von State erbt, und das die Darstellungslogik und den Zustand verwaltet.


```dart
// Dieses stateless Widget nimmt einen Namen als Parameter entgegen und zeigt einen Gruß an. 
class GrussWidget extends StatelessWidget {
  final String name;

  // Konstruktor zum Übergeben des Namens
  const GrussWidget({Key? key, required this.name}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Rückgabe des Widgets, das angezeigt werden soll
    return Container(
      padding: EdgeInsets.all(16.0),
      color: Colors.blue,
      child: Text(
        'Hallo, $name!',
        style: TextStyle(color: Colors.white),
      ),
    );
  }
}
```

```dart
// Dieses Beispiel zeigt ein Stateful widget und zwar ein ZählerWidget, das einen Zähler anzeigt und einen Button bereitstellt, um den Zähler zu erhöhen.

// Das StatefulWidget selbst
class ZaehlerWidget extends StatefulWidget {
  const ZaehlerWidget({Key? key}) : super(key: key);

  @override
  _ZaehlerWidgetState createState() => _ZaehlerWidgetState();
}

// Der Zustand des StatefulWidget
class _ZaehlerWidgetState extends State<ZaehlerWidget> {
  int _zaehler = 0; // Eine Zustandsvariable

  void _erhoeheZaehler() {
    // setState informiert Flutter, dass sich der Zustand geändert hat
    setState(() {
      _zaehler++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // Die Darstellung basierend auf dem aktuellen Zustand
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text('Zähler: $_zaehler'),
        ElevatedButton(
          onPressed: _erhoeheZaehler,
          child: Text('Erhöhen'),
        ),
      ],
    );
  }
}
```
Die setState-Methode ist essenziell für die Zustandsverwaltung in StatefulWidgets. Sie informiert Flutter, dass sich der Zustand geändert hat, wodurch die build-Methode erneut aufgerufen wird, um die UI zu aktualisieren.


setState baut das Widget nicht sofort neu auf, sondern markiert es als "schmutzig" (dirty).
Der Neuaufbau erfolgt in der nächsten Frame-Rendering-Phase, um Effizienz zu gewährleisten und unnötige Updates zu vermeiden.

### Widget-Lebenszyklus

Ein gutes Verständnis des Lebenszyklus von Widgets ermöglicht es mir, Ressourcen effizienter zu verwalten sowie auf Veränderungen und Fehler zu reagieren.
