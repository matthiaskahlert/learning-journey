Ruby Markdown Notes – Woche 1




Um das Gelernte anzuwenden, notiere ich Lerninhalte, Beispiele und Reflektionen.
[TOC]


📅 Tagesnotizen
# Tag 1 – Ruby / Entwicklungsumgebung aufsetzen

## Kurze Zusammenfassung:

Was war heute Schwerpunkt? Kurzer Überblick über Thema, Übungen oder Theorie.

## Vorgehensweise:

- ruby installieren auch mit empfohlener MSYS2 development toolchain. Ich entscheide mich für die neuste Ruby version 4.0.2.-1 inklusive Devkit. die MSYS2 toolchain ist umfangreich vom Datenvolumen her, aber wird empfohlen für
- nach der Ruby installation kümmere ich mich um die VSCode Extensions: 
  Extension "Ruby LSP" von Shopify installieren (shopify.ruby-lsp) — offizieller Language Server, ersetzt die alte ruby Extension
  
  als optional angegeben wurde der "Ruby Debugger" für Debugging-Support, die extension lass ich mal vorerst weg.

  damit die extension die ruby installation findet, musste ich die settings.json anpassen bzgl:
```json
  "rubyLsp.rubyVersionManager": {
    "identifier": "none"
  }
```

## MSYS2 toolchain

MSYS2 ist eine Unix-ähnliche Entwicklungsumgebung (GCC, Make, etc.) für Windows. Ruby selbst braucht sie nicht — aber viele Gems (Ruby-Pakete) enthalten native Erweiterungen, die in C geschrieben sind und zur Installationszeit kompiliert werden müssen.


Konkrete Beispiele:

nokogiri (XML/HTML-Parsing) — sehr häufig genutzt
bcrypt (Passwort-Hashing)
mysql2 / pg (Datenbank-Treiber)
ffi (Foreign Function Interface)
Ohne MSYS2 bekommst du bei solchen Gems einen Fehler.

## irb

IRB (Interactive Ruby) ist eine REPL-Umgebung, die Ruby-Code Zeile für Zeile ausführt und das Ergebnis sofort anzeigt — ideal zum schnellen Ausprobieren von Ausdrücken und Methoden, ohne eine Datei anlegen zu müssen. Im Gegensatz zum Run-Button bleibt der Zustand (Variablen, Objekte) zwischen den Eingaben erhalten.


## Ruby Hilfsmethoden accessor, reader, writer

Ruby kann automatisch Getter- und Setter-Methoden für Instanzvariablen einer Klasse generieren — statt sie manuell zu schreiben.

| Methode | Lesen | Schreiben | Wann nutzen? |
|---|---|---|---|
| `attr_reader` | ✅ | ❌ | Wert soll nur gelesen werden (z.B. ID, Erstelldatum) |
| `attr_writer` | ❌ | ✅ | Wert soll nur gesetzt werden (selten genutzt) |
| `attr_accessor` | ✅ | ✅ | Wert soll gelesen und geändert werden |

Beispiele / Code:

```ruby
class Person
  attr_accessor :name   # getter + setter
  attr_reader   :id     # nur getter
  attr_writer   :email  # nur setter
end

p = Person.new
p.name = "Matthias"   # setter
puts p.name           # getter → "Matthias"
```

## puts

`puts` ist die wichtigste Ausgabefunktion in Ruby. Sie gibt den Wert eines Ausdrucks im Terminal aus und fügt automatisch einen Zeilenumbruch an. Ohne `puts` sieht man beim Ausführen von Ruby-Dateien keine Ausgabe, selbst wenn Variablen gesetzt oder berechnet werden.

Beispiel:

```ruby
name = "Matthias"
puts name           # gibt "Matthias" aus
```

Im Unterschied zu IRB, wo das Ergebnis jeder Zeile angezeigt wird, muss man beim Ausführen von Dateien immer explizit `puts` verwenden, um Werte sichtbar zu machen.
nel ethode



## <=> (Raumschiff-Operator)

Der sogenannte Raumschiff-Operator `<=>` vergleicht zwei Werte miteinander. Er gibt immer nur -1, 0 oder 1 zurück:
- `-1`, wenn der linke Wert kleiner ist
- `0`, wenn beide gleich sind
- `1`, wenn der linke Wert größer ist

Beispiel:
```ruby
5 <=> 7   # => -1
5 <=> 5   # => 0
7 <=> 5   # => 1
```
Er wird oft beim Sortieren verwendet.

## Kernel

Das Ruby-Modul `Kernel` stellt grundlegende Methoden wie `puts`, `print`, `gets` oder `exit` bereit, die in jedem Ruby-Programm überall verfügbar sind. Diese Methoden werden automatisch in alle Klassen eingebunden. Der Begriff `Kernel` in Ruby hat nichts mit dem Betriebssystem-Kernel (Hardware) zu tun, sondern bezeichnet einfach das „Herzstück“ der Ruby-Basisfunktionen.


## Schlefen mit Zahlenbereichen
```ruby
1.upto(5) { ... }
```
Führt den Block für alle Zahlen von 1 bis 5 aus (aufsteigend).
Beispiel:
```ruby
10.downto(5) { ... }
```
Führt den Block für alle Zahlen von 10 bis 5 aus (absteigend).
Beispiel:
```ruby
0.step(50, 5) { ... }
```
Führt den Block von 0 bis 50 in 5er-Schritten aus.
Beispiel:

Alle drei Methoden sind elegante Ruby-Wege, um Schleifen mit Zahlenbereichen zu schreiben.


## Typkonvertierung in Ruby

In Ruby kannst du Werte mit Methoden wie `to_i`, `to_f`, `to_s` usw. in andere Typen umwandeln. Das ist oft nötig, um z.B. Ganzzahlen in Fließkommazahlen zu verwandeln, damit Divisionen korrekt funktionieren.

| Methode      | Zweck                        | Beispiel                | Ergebnis         |
|--------------|------------------------------|-------------------------|------------------|
| `to_i`       | In Integer (Ganzzahl)        | `'42.7'.to_i`           | `42`             |
| `to_f`       | In Float (Kommazahl)         | `'3'.to_f`              | `3.0`            |
| `to_s`       | In String                    | `10.to_s`               | `'10'`           |
| `to_sym`     | In Symbol                    | `'name'.to_sym`         | `:name`          |
| `to_a`       | In Array (bei manchen Objekten) | `(1..3).to_a`        | `[1, 2, 3]`      |

**Beispiel für Division mit Typkonvertierung:**
```ruby
x = 10
y = 3
puts x.to_f / y.to_f   # ergibt 3.3333333333333335
```


## Delimiter / Begrenzungszeichen in Ruby

Ruby erlaubt verschiedene Schreibweisen für Strings, sogenannte Delimiter (Begrenzungszeichen). Das ist praktisch für mehrzeilige Strings oder wenn der Text Anführungszeichen enthält. Mit `%q` und `%Q` kannst du beliebige Zeichen als Begrenzung wählen.

| Schreibweise    | Bedeutung                           |
| --------------- | ----------------------------------- |
| `'text'`        | normaler String                     |
| `%q!text!`      | gleicher String, anderer Begrenzer  |
| `"text \\#{x}"`   | String mit Variablen                |
| `%Q!text \\#{x}!` | gleiche Sache mit anderem Begrenzer |

**Hinweis:**
- `%q` entspricht einfachen Anführungszeichen (keine Interpolation)
- `%Q` entspricht doppelten Anführungszeichen unterstützt Interpolation, also hier kann ich Variablen im String angeben.
- Als Begrenzungszeichen kannst du fast jedes Zeichen nehmen: `!`, `/`, `{}`, `[]`, `()` usw.


## Heredoc in Ruby

Mit Heredoc kannst du in Ruby bequem mehrzeilige Strings schreiben, ohne Escape-Zeichen oder spezielle Delimiter. Die Syntax ist:

```ruby
x = <<END_MY_STRING_PLEASE
This is the string
And a second line
END_MY_STRING_PLEASE
```

Der Text zwischen den beiden `END_MY_STRING_PLEASE`-Markern wird als String gespeichert. Der Marker kann beliebig gewählt werden (z.B. `TEXT`, `DOC`, etc.), muss aber am Anfang der Zeile stehen. Heredoc unterstützt auch String-Interpolation wie bei doppelten Anführungszeichen.

## String-Methoden: Beispiele und Ausgabe

| Ausdruck                  | Ausgabe    |
|---------------------------|------------|
| "Test" + "Test"            | TestTest   |
| "test".capitalize         | Test       |
| "Test".downcase           | test       |
| "Test".chop               | Tes        |
| "Test".next               | Tesu       |
| "Test".reverse            | tseT       |
| "Test".sum                | 416        |
| "Test".swapcase           | tEST       |
| "Test".upcase             | TEST       |
| "Test".upcase.reverse     | TSET       |
| "Test".upcase.reverse.next| TSEU       |

Diese Methoden zeigen, wie flexibel und mächtig Strings in Ruby bearbeitet werden können.


## RegEx und Stringmodifizierung

Reguläre Ausdrücke (RegEx) in Ruby sind Suchmuster, mit denen du gezielt Text in Strings finden, prüfen oder verändern kannst. Sie werden in Schrägstrichen geschrieben, zum Beispiel /abc/. Mit den Methoden sub und gsub kannst du Text ersetzen: sub ersetzt nur das erste Vorkommen, während gsub alle Vorkommen austauscht. Die Methode scan erlaubt es, alle passenden Stellen im String zu finden und weiterzuverarbeiten, etwa "abc".scan(/./) { |c| puts c }, was jeden Buchstaben einzeln ausgibt.

Die wichtigsten RegEx-Zeichen und ihre Bedeutung findest du in dieser Tabelle:

| Zeichen   | Bedeutung                          |
|:----------|:-----------------------------------|
| `^`       | Anfang des Strings oder der Zeile   |
| `$`       | Ende des Strings oder der Zeile     |
| `.`       | Beliebiges Zeichen                 |
| `\d`      | Ziffer (0–9)                       |
| `\w`      | Buchstabe, Zahl oder Unterstrich   |
| `\s`      | Leerzeichen                        |
| `[aeiou]` | Einer der Buchstaben a, e, i, o, u |
| `[a-z]`   | Ein Buchstabe von a bis z          |
Mit dem Operator =~ kannst du prüfen, ob ein String ein Muster enthält, zum Beispiel "Hallo" =~ /a/, was die Position des ersten Treffers oder nil zurückgibt. Klammern () in einem RegEx speichern Teilstücke separat, sodass du mit match gezielt auf diese zugreifen kannst, etwa "abc def".match(/(\\w+) (\\w+)/)[1] für das erste Wort.

RegEx werden häufig verwendet, um Text zu durchsuchen, Daten wie Zahlen zu extrahieren, Strings zu ersetzen oder Eingaben zu validieren. Auch wenn sie anfangs ungewohnt wirken, reichen die Grundfunktionen für die meisten Aufgaben im Alltag völlig aus.



Was ich morgen lernen will:

…

🗓️ Tag 2 – Thema / Array und List



Learningfacts:
## Arraymethoden
| Methode/Beispiel                | Erklärung |
|---------------------------------|-----------|
| x[2]                            | Gibt das Element an Index 2 zurück |
| x[2] += 1                       | Erhöht das Element an Index 2 um 1 |
| x[2] = "Foobar" * 3             | Setzt das Element an Index 2 auf den String "FoobarFoobarFoobar" |
| x << "Rocket"                   | Fügt "Rocket" am Ende des Arrays hinzu (shovel operator) |
| x.push("Launcher")              | Fügt "Launcher" am Ende des Arrays hinzu |
| x.pop                           | Entfernt und gibt das letzte Element zurück |
| x.length                        | Gibt die Anzahl der Elemente im Array zurück |
| x.join(',')                     | Verbindet alle Elemente zu einem String, getrennt durch Kommas |
| x.include?(3)                   | Prüft, ob das Array die Zahl 3 enthält |
| x.empty?                        | Prüft, ob das Array leer ist |
| x.first / x.last                | Gibt das erste/letzte Element zurück |
| x.first(2)                      | Gibt die ersten 2 Elemente als Array zurück |
| x.reverse                       | Gibt ein neues Array mit umgekehrter Reihenfolge zurück |
| x.each { |e| ... }              | Iteriert über alle Elemente |
| x.collect { |e| e * 2 }         | Gibt ein neues Array mit dem Ergebnis des Blocks zurück (map) |
| x + y                           | Verbindet zwei Arrays zu einem neuen Array |
| x - y                           | Gibt ein Array mit den Elementen aus x, die nicht in y sind |

## Hashes
Ein Hash in Ruby ist eine Sammlung von Schlüssel-Wert-Paaren, ähnlich wie ein Wörterbuch oder Map in anderen Programmiersprachen. Jeder Schlüssel (key) ist eindeutig und verweist auf einen Wert (value). Hashes werden mit geschweiften Klammern geschrieben.

```ruby
person = {
  name: "Anna",
  age: 28,
  city: "Berlin"
}

puts person[:name]   # gibt "Anna" aus
puts person[:age]    # gibt 28 aus
puts person[:city]   # gibt "Berlin" aus
```

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