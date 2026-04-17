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

