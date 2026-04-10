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


## Termary operator
Der ternary operator bietet eine kompakte Möglichkeit, einfache Entscheidungen im Code zu treffen.

```ruby
age = 10
type = age < 18 ? "child" : "adult"
puts "You are a " + type
```

Erklärung:
Die zweite Zeile verwendet den sogenannten ternären Operator. Damit kannst du eine Kurzform von if-else schreiben:

Aufbau:
<Bedingung> ? <Wert wenn wahr> : <Wert wenn falsch>

In diesem Beispiel prüft age < 18, ob das Alter kleiner als 18 ist.

Ist das wahr, wird "child" zugewiesen, sonst "adult".

Bei age = 10 ist die Bedingung wahr, also steht am Ende:
You are a child

## pattern matching case/in

Beispiel für Pattern Matching in Ruby:

```ruby
person = {name: "Anna", age: 17}

case person
in name:, age: 18..
  puts "#{name} ist volljährig."
in name:, age:
  puts "#{name} ist noch nicht volljährig."
end
# Ausgabe: "Anna ist noch nicht volljährig."
```


Erklärung:

Das case/in prüft, ob das Alter im Bereich 18 oder älter liegt (age: 18..).
Wenn nicht, wird der zweite Zweig genommen und der Name sowie das Alter ausgegeben.
Die Schreibweise name: bindet den Wert direkt an die Variable name.
So kannst du mit Pattern Matching einfach und übersichtlich strukturierte Daten prüfen und Variablen daraus extrahieren!
## while until

Mit while und until kannst du in Ruby Schleifen schreiben: while wiederholt den Block, solange die Bedingung wahr ist, until solange sie falsch ist.  Beide Varianten eignen sich für wiederholte Abläufe mit unterschiedlichen Abbruchbedingungen.

```ruby

x = 1
while x < 100
puts x
x = x * 2
end
```

```ruby

x = 1
until x > 99
puts x
x = x * 2
end
```

## CodeBlöcke
Code Blocks in Ruby sind anonyme, wiederverwendbare Codeabschnitte, die an Methoden übergeben werden können. Sie werden mit { ... } oder do ... end geschrieben. Methoden wie each führen den Codeblock für jedes Element aus.
Man kann benannte Parameter (|x|) oder nummerierte Parameter (_1) verwenden.
Eigene Methoden können Codeblöcke mit &block oder yield akzeptieren. Mit yield wird der Block aufgerufen, ohne ihn explizit als Parameter zu deklarieren.
Codeblöcke können auch als Proc-Objekte gespeichert und mit call ausgeführt werden.
Wichtig: Pro Methode kann nur ein Codeblock übergeben werden.
Lambda ist eine spezielle Form von Proc mit strengerer Parameterprüfung.


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

## Time Class in Ruby
In Ruby kann man mit der Time-Klasse Datum und Uhrzeit einfach verarbeiten: Time.now liefert dir den aktuellen Zeitpunkt, den Ruby beim Ausgeben als gut lesbaren Text zeigt. Intern speichert Ruby Zeit als Mikrosekunden seit de UNIX Zeit also dem 1. Januar 1970 (UTC/GMT), dadurch lassen sich Zeitpunkte leicht vergleichen, zum Beispiel mit kleiner oder größer. Praktisch ist auch, dass man mit Sekunden rechnen kann: Zieht man 10 ab, bekommt man die Uhrzeit 10 Sekunden früher, und addiert man 86.400, springst du genau einen Tag nach vorne. So kannt man Zeiten in Programmen relativ einfach prüfen, vergleichen und verschieben.

```ruby
puts Time.now
puts Time.now - 10
puts Time.now + 86400
2026-04-01 12:44:19 +0200
2026-04-01 12:44:09 +0200
2026-04-02 12:44:20 +0200
```

| Methode | Was die Methode zurückgibt |
|---|---|
| `hour` | Eine Zahl für die Stunde im 24-Stunden-Format (z. B. 21 für 21:00 Uhr). |
| `min` | Die Anzahl der Minuten nach der vollen Stunde. |
| `sec` | Die Anzahl der Sekunden nach der vollen Minute. |
| `usec` | Die Anzahl der Mikrosekunden nach der vollen Sekunde (1.000.000 Mikrosekunden = 1 Sekunde). |
| `day` | Die Tagesnummer im Monat. |
| `mday` | Synonym für `day`, also der Tag des Monats. |
| `wday` | Die Tagesnummer in der Woche (Sonntag = 0, Samstag = 6). |
| `yday` | Die Tagesnummer im Jahr. |
| `month` | Die Monatsnummer des Datums (z. B. 11 für November). |
| `year` | Das Jahr des Datums. |
| `zone` | Den Namen der Zeitzone, die zur Uhrzeit gehört. |
| `utc?` | `true` oder `false`, je nachdem, ob Zeit/Datum in der UTC/GMT-Zeitzone ist oder nicht. |
| `gmt?` | Synonym für `utc?` für alle, die den Begriff GMT bevorzugen. |

## Ranges in Ruby

Ranges in Ruby sind super praktisch, wenn du nicht alle Werte einzeln speichern willst, sondern nur den Bereich selbst, also zum Beispiel “alles von A bis Z” als ('A'..'Z'). Statt ein großes Array von Hand zu schreiben, kannst du diesen Bereich direkt nutzen, mit to_a bei Bedarf in ein Array umwandeln oder mit each darüber laufen. Mit include? prüfst du schnell, ob ein Wert im Bereich liegt, etwa ob "R" enthalten ist (ja) oder "r" (nein, wegen Groß-/Kleinschreibung). Außerdem kannst du Ranges bei Arrays als Indexbereich verwenden, um mehrere Elemente auf einmal zu lesen oder zu ersetzen, z. B. a[1..3]. Kurz gesagt: Ranges machen Code kürzer, klarer und helfen dir, mit zusammenhängenden Werten elegant zu arbeiten.

```ruby
# Beispiel 2: Range als Array-Index verwenden
zahlen = [10, 20, 30, 40, 50]
p zahlen[1..3]
# Ausgabe: [20, 30, 40]
```

## Symbole in Ruby
Ein Symbol wird durch ein vorangestelltes Doppelpunktzeichen (:) dargestellt, gefolgt von einer Zeichenkette
Symbole in Ruby sind feste Namen mit Doppelpunkt, zum Beispiel :good, :name oder :male.
 Symbole in Ruby (z. B. :name) sind unveränderliche (immutable) Zeichenketten, die als spg. Bezeichner fungieren. Ihr "Wert" ist im Grunde ihr Name selbst. Sie sind sehr effizient, da für ein Symbol mit demselben Namen im gesamten Programm nur ein einziges Objekt im Speicher existiert. 

Einfach gesagt:

Ein String ist Text-Inhalt, z. B. "good".
Ein Symbol ist eher ein Label/Bezeichner, z. B. :good
Warum nutzt man Symbole?

Sie sind für feste Werte gedacht (Optionen, Zustände, Schlüssel).
Sie sind effizienter als Strings, weil Ruby dasselbe Symbol wiederverwendet.
Code wird oft klarer, weil man sofort sieht: Das ist ein fester Bezeichner, kein normaler Text.
Typische Nutzung:

Zustände/Optionen
Hash-Keys
```ruby
person = { name: "Fred", age: 20, gender: :male }
```
Hier sind name, age, gender und :male Symbole.



```ruby
current_situation = :good
puts "Everything is fine" if current_situation == :good
puts "PANIC!" if current_situation == :bad
```

Symbole sind wie Namensschilder für feste Konzepte im Code, Strings sind normaler Text.

## Objektklassen und Typumwandlung in Ruby

In Ruby ist jeder Wert ein Objekt mit einer bestimmten Klasse, zum Beispiel String, Integer, Float oder Symbol. Deshalb ist es wichtig zu wissen: Gleich aussehende Werte verhalten sich unterschiedlich, je nachdem zu welcher Klasse sie gehören. "12" ist Text, 12 ist eine Zahl. Darum ergibt "12" + "10" den Text 1210 (zusammenfügen), aber 12 + 10 ergibt 22 (rechnen). Mit sogenannten to_-Methoden kannst du Werte umwandeln: to_i macht aus Text eine Ganzzahl, to_f eine Kommazahl, to_s macht aus Zahlen oder Symbolen wieder Text, und to_sym macht aus Text ein Symbol. Kurz gesagt: Wenn etwas „falsch rechnet“ oder „komisch zusammengefügt“ wird, liegt es oft daran, dass der Wert in der falschen Klasse ist und zuerst umgewandelt werden muss.
…
## Ruby on Rails

Ruby on Rails

Definition:
Ruby on Rails (Rails) ist ein Web-Application-Framework, das die Entwicklung von Webanwendungen erleichtert. Es bietet Konventionen, Strukturen und Systeme als Grundlage für die Entwicklung.

Bedeutung:

Rails hat die Popularität von Ruby außerhalb Japans stark gesteigert.
Es hat Ruby von einer kleinen Entwickler-Community zu Hunderttausenden von Entwicklern weltweit gebracht.
Einfluss:

Rails hat die Dynamik des gesamten Ruby-Ökosystems verändert.
Es ist ein zentraler Grund für das Interesse an Ruby geworden.
Hinweis:

Ein vollständiges Rails-Tutorial ist schwierig, da sich das Framework schnell weiterentwickelt.
Kapitel 13 behandelt Rails-Entwicklung kurz.
Rails ist ein entscheidender Faktor für die Verbreitung und Bedeutung von Ruby in der Softwareentwicklung.

## Open source

Definition:

Open Source bedeutet, dass der Quellcode einer Software öffentlich zugänglich ist.
Es gibt oft Lizenzbeschränkungen, die festlegen, was mit dem Code gemacht werden darf.
Ruby und Open Source:

Ruby und fast alle Bibliotheken sind Open Source.
Entwickler können mit Ruby geschlossene, proprietäre Anwendungen erstellen, ohne den Quellcode offenzulegen.
Beispiel: 37signals und Ruby on Rails:

37signals veröffentlichte den Quellcode von Basecamp nicht, stellte aber das Ruby on Rails Framework als Open Source bereit.
Vorteile: Publicity für das Unternehmen und Beiträge von talentierten, unbezahlten Entwicklern.
Vorteile von Open Source:

Projekte wie Apache, nginx und PostgreSQL profitieren von der Zusammenarbeit unbezahlter Entwickler.
Open Source fördert kontinuierliche Verbesserungen und Innovationen.
Entscheidung:

Die Wahl zwischen Open Source und geschlossener Entwicklung ist oft schwierig und hängt von den Zielen des Projekts ab.
Kultur:

Die Open-Source-Community basiert auf dem freien Teilen von Wissen und Zusammenarbeit zur Verbesserung von Systemen und Diensten.
Open Source wird zunehmend zum Standard für die Entwicklung von Programmiersprachen, Bibliotheken und ähnlicher Software.
Bedeutung für Ruby:

Die Ruby-Community ist stark von der Open-Source-Kultur geprägt.
Entwickler veröffentlichen oft Tools und Code-Tricks, um von Peer-Reviews und der daraus resultierenden Popularität zu profitieren.
Vorteile:

Open Source kann die Qualität von Code und Tools verbessern.
Es kann die Bekanntheit in der Branche steigern und ist oft keine schlechte Geschäftsentscheidung.

## OOP

Objektorientierte Programmierung (OOP) ist ein Ansatz, bei dem Code in Klassen und Objekte aufgeteilt wird.

- Eine Klasse ist die Vorlage (z. B. `Car`).
- Ein Objekt ist eine konkrete Instanz dieser Vorlage (z. B. mein rotes Auto).

Warum ist das hilfreich?

- Struktur: Große Programme werden übersichtlicher, weil Daten und Verhalten zusammengehoeren.
- Wiederverwendbarkeit: Klassen koennen mehrfach genutzt werden, statt Logik staendig neu zu schreiben.
- Wartbarkeit: Aenderungen sind einfacher, weil man gezielt an einer Klasse arbeitet.
- Erweiterbarkeit: Neue Funktionen lassen sich ueber Vererbung/Komposition sauber ergaenzen.
- Teamarbeit: Einheitliche Struktur macht Code fuer andere schneller verstaendlich.

Wichtige OOP-Konzepte:

- Kapselung: Interne Details werden geschuetzt, nach außen gibt es klare Schnittstellen.
- Vererbung: Eine Klasse kann Eigenschaften/Methoden einer anderen uebernehmen.
- Polymorphismus: Unterschiedliche Objekte koennen gleich angesprochen werden (z. B. alle haben `area`).
- Abstraktion: Nur das Wesentliche wird sichtbar, Komplexitaet bleibt intern.

Kurzfazit: OOP braucht anfangs etwas mehr Struktur, spart aber bei groesseren Projekten viel Zeit und Fehler.

## Local, Global, Object und Class Variables

### Lokale Variablen
Beispiel: x = 10  
Nur dort gültig, wo sie definiert wurden (z.B. in einer Methode oder einem Block).  
Außerhalb dieses Bereichs nicht sichtbar.  
Zwei Methoden können beide eine eigene Variable x haben, ohne sich zu stören.  

### Globale Variablen
Beispiel: $x = 10  
Überall im Programm sichtbar, auch in Klassen und Methoden.  
Beginnen mit $.  
Werden in Ruby selten genutzt, da sie Code unübersichtlich machen können.  

### Objekt-/Instanzvariablen
Beispiel: @seite = 5  
Gehören zu einem bestimmten Objekt.  
Beginnen mit @.  
Jede Instanz hat ihren eigenen Wert.  
Können von allen Methoden des Objekts verwendet werden.  

### Klassenvariablen
Beispiel: @@anzahl = 0  
Gelten für alle Objekte einer Klasse gemeinsam.  
Beginnen mit @@.  
Beispiel: Zählt, wie viele Objekte insgesamt erzeugt wurden.  
Werden oft durch Klasseninstanzvariablen ersetzt, da @@ in Vererbungen problematisch sein kann.  

### Merke:
Lokal = nur im aktuellen Bereich  
Global = überall  
Objekt = pro Objekt  
Klasse = für alle Objekte der Klasse gemeinsam  

## Instanzmethoden vs Klassenmethoden

```ruby
# Beispiel: Square mit Instanz- und Klassenmethoden

class Square
  @@count = 0  # Klassenvariable: zählt alle erstellten Objekte

  def initialize(side_length)
    @side = side_length  # Instanzvariable: gehört zu diesem Objekt
    @@count += 1
  end

  # Instanzmethode: arbeitet mit einem einzelnen Objekt
  def area
    @side * @side
  end

  # Klassenmethode: arbeitet auf Klassenebene
  def self.count
    @@count
  end
end

# Nutzung:

s1 = Square.new(4)
s2 = Square.new(5)

puts s1.area   # => 16
puts s2.area   # => 25

puts Square.count  # => 2
```


Instanzmethoden arbeiten mit einem Objekt und können nur über eine Instanz aufgerufen werden (z.B. s1.area)
Klassenmethoden (z. B. self.count) werden mit self.definiert und  arbeiten mit der Klasse selbst (Square.count). Sie eignen sich für Aufgaben, die die Klasse als Ganzes betreffen, wie z. B. das Zählen aller erzeugten Objekte.
@ → gehört zum Objekt
@@ → gehört zur Klasse

## Klassen- override

In Ruby kann man bestehende Methoden von Klassen einfach überschreiben (overriden). Das gilt sogar für eingebaute Klassen wie String.

Beispiel:
```ruby
class String
  def length
    20
  end
end

puts "Hallo".length   # Gibt immer 20 aus!
puts "abc".length     # Gibt auch 20 aus!
```

Das bedeutet: Egal wie lang der Text wirklich ist, length gibt jetzt immer 20 zurück.

Auch eigene Methoden kannst du so überschreiben:
```ruby
class Dog
  def talk
    puts "Wuff!"
  end
end

my_dog = Dog.new
my_dog.talk   # Wuff!

class Dog
  def talk
    puts "Heul!"
  end
end

my_dog.talk   # Heul!

```

Achtung: Das ist mächtig, kann aber zu Problemen führen, wenn man selbst (oder durch Bibliotheken) wichtige Methoden überschreibt, auf die andere Teile des Programms angewiesen sind.

## Reflection
Reflection bedeutet, dass ein Programm sich selbst „anschauen“ und Informationen über sich herausfinden kann – zum Beispiel, welche Methoden ein Objekt hat.

In Ruby kannst du z. B. mit methods herausfinden, was ein Objekt alles kann:
```ruby
a = "Hallo"
puts a.methods
```

Das gibt dir eine lange Liste von Methoden, die du auf Strings anwenden kannst, z. B. upcase, length, reverse usw.

Du kannst auch sehen, welche Variablen ein Objekt hat:
```ruby
class Person
  attr_accessor :name, :age
end

p = Person.new
p.name = "Fred"
p.age = 20
puts p.instance_variables  # => [:@name, :@age]
```
Wozu ist das gut?
Mit Reflection kannst du z. B. herausfinden, was ein Objekt kann, ohne den Code zu kennen. Das ist praktisch für Werkzeuge, Debugging oder wenn du flexibel programmieren willst.

Merke:

obj.methods zeigt alle Methoden eines Objekts.
obj.instance_variables zeigt alle Variablen eines Objekts.
Du musst das am Anfang nicht oft nutzen, aber später kann es sehr hilfreich sein!



## Kapselung (Encapsulation)
Hier ist eine leicht verständliche Zusammenfassung mit Beispiel:

Encapsulation (Kapselung) bedeutet, dass Daten und Methoden in einer Klasse „versteckt“ werden können, sodass nicht alles von außen zugreifbar ist. So schützt du wichtige Teile deines Codes und kannst steuern, wie auf Daten zugegriffen wird.

```ruby
class Person
  def initialize(name)
    set_name(name)
  end

  def name
    @first_name + ' ' + @last_name
  end

  private

  def set_name(name)
    first, last = name.split(' ')
    @first_name = first
    @last_name = last
  end
end

p = Person.new("Fred Bloggs")
puts p.name           # => "Fred Bloggs"
p.set_name("Max Mustermann") # Fehler! set_name ist privat
```
- public: Methoden sind von überall aufrufbar (Standard).
- private: Methoden sind nur innerhalb der Klasse aufrufbar, nicht von außen.
- protected: Methoden sind für alle Objekte der gleichen Klasse zugänglich, aber nicht von außen.

Du kannst z. B. sicherstellen, dass Namen immer korrekt gesetzt werden und niemand versehentlich interne Variablen verändert.
So bleibt dein Code stabil und leicht wartbar.

## Verschachtelte Klassen - Nested Classes

In Ruby kann man eine Klasse in eine andere Klasse hineinlegen. Das nennt man verschachtelte Klassen (nested classes). Das macht man, wenn eine Klasse nur für eine andere Klasse gebraucht wird und nicht überall im Programm.

```ruby
class Zeichnung
  class Linie
  end
  class Kreis
  end
end
```
Hier gibt es die Klasse Zeichnung und darin die Klassen Linie und Kreis.
Innerhalb von Zeichnung kann man einfach Linie oder Kreis benutzen.
Außerhalb muss man Zeichnung::Linie oder Zeichnung::Kreis schreiben.

```ruby
a = Zeichnung::Kreis.new
```


## Scope von Konstanten
Konstanten arbeiten nicht wie globale Variablen.
Sie sind im Scope der jeweiligen Klasse definiert und stehen auch Unterklassen zur Verfügung, sofern sie dort nicht neu definiert werden.

## Module als Namespaces
Ein  Problem mit Namenskonflikten in Ruby entsteht, wenn du mehrere Dateien einbindest (z. B. mit require), die Methoden oder Klassen mit denselben Namen definieren. Ruby kennt keine echten „private“ Methoden auf Dateiebene - alles landet im selben globalen Namensraum, wenn du es lädst.

Beispiel:

Du hast in Datei A eine Methode random, die eine Zahl liefert.
In Datei B gibt es auch eine Methode random, die einen Buchstaben liefert.
Wenn du beide Dateien einbindest, überschreibt die zuletzt geladene Version die vorherige. Es gibt dann nur noch eine Methode random - die andere ist „verloren“.
Das gilt auch für Klassen: Wenn du zweimal eine Klasse Song definierst (in verschiedenen Dateien), werden die Definitionen zusammengeworfen - Methoden aus beiden Dateien landen in einer Klasse. Das kann zu unerwartetem Verhalten führen.

Lösung:
Um solche Konflikte zu vermeiden, nutzt man in Ruby ***Module als Namespaces***. Damit kannst du Methoden und Klassen „einsperren“, sodass sie nicht mit gleichnamigen Methoden/Klassen aus anderen Dateien kollidieren.

Beispiel mit Namespace:
```ruby
module NumberStuff
  def self.random
    rand(1000000)
  end
end

module LetterStuff
  def self.random
    (rand(26) + 65).chr
  end
end

puts NumberStuff.random  # Zahl
puts LetterStuff.random  # Buchstabe
```

So gibt es keinen Konflikt, weil die Methoden eindeutig über ihren Modulnamen angesprochen werden.

Fazit:
Ohne Namespaces überschreibt die letzte geladene Definition die vorherige. Mit Namespaces (Modulen) kannst du Namenskonflikte vermeiden.

## Mix-ins

Das „Mix-in“-Konzept in Ruby bedeutet, dass du Funktionalität aus Modulen in beliebige Klassen „hineinmischen“ kannst – ähnlich wie Bausteine, die du flexibel verwendest.

Warum gibt es Mix-ins?
Ruby unterstützt keine Mehrfachvererbung (eine Klasse kann nur von einer anderen Klasse erben). Aber manchmal willst du Methoden mehreren, völlig unterschiedlichen Klassen zur Verfügung stellen – ohne alles doppelt zu schreiben.

Wie funktioniert das?
Du schreibst Methoden in ein Modul. Mit include (für Instanzmethoden) oder extend (für Klassenmethoden) kannst du dieses Modul in eine Klasse „mischen“. Die Klasse bekommt dann alle Methoden des Moduls, als hätte sie sie selbst definiert.

Beispiel:
```ruby
module UsefulFeatures
  def class_name
    self.class.to_s
  end
end

class Person
  include UsefulFeatures
end

x = Person.new
puts x.class_name  # Ausgabe: Person
```


Hier bekommt Person die Methode class_name aus dem Modul. Das geht auch mit anderen Klassen – du kannst UsefulFeatures in beliebig viele Klassen einbinden.

Fazit:
Mix-ins sind Rubys Weg, um Code wiederzuverwenden und Funktionalität flexibel zu teilen – ohne die Probleme von Mehrfachvererbung. Sie machen deinen Code modularer und übersichtlicher.

## Enumerable
Das Modul Enumerable in Ruby ist eine Sammlung von Methoden, die dir viele praktische Funktionen für das Durchlaufen und Auswerten von Listen (wie Arrays oder Hashes) geben – z. B. sort, max, min, select, collect, find usw.

Wie funktioniert das?

Enumerable ist ein Modul, das Methoden wie sort, max, min, select usw. bereitstellt.
Damit du diese Methoden nutzen kannst, muss deine Klasse eine each-Methode haben, die alle Elemente „durchgeht“ (iteriert).
Wenn du include Enumerable in deine Klasse schreibst, bekommst du alle diese Methoden „geschenkt“ – sie funktionieren dann automatisch mit deiner each-Methode.
```ruby
class AlleVokale
  include Enumerable
  VOKALE = %w{a e i o u}
  def each
    VOKALE.each { |v| yield v }
  end
end

x = AlleVokale.new
x.max      # => "u"
x.sort     # => ["a", "e", "i", "o", "u"]
x.select { |v| v > "j" } # => ["o", "u"]
```
Wichtig:

Array und Hash haben Enumerable schon eingebunden, deshalb kannst du dort immer z. B. .max, .sort, .select usw. nutzen.
Wenn du eine eigene Klasse baust, musst du nur each definieren und Enumerable einbinden – dann hast du sofort viele mächtige Methoden.
Fazit:
Enumerable macht Iteration und Auswertung von Listen in Ruby sehr einfach und spart dir viel Code. Alles, was du brauchst, ist eine each-Methode und include Enumerable.

## Comparable
Das Modul Comparable in Ruby ermöglicht es, eigene Klassen mit Vergleichsoperatoren wie <, <=, ==, >=, > und between? auszustatten. Damit kannst du Objekte deiner Klasse direkt vergleichen, z. B. sortieren oder prüfen, ob ein Wert zwischen zwei anderen liegt.

Wie funktioniert das?

Du schreibst include Comparable in deine Klasse.
Du musst die Methode <=> (Spaceship-Operator) definieren. Diese Methode vergleicht das aktuelle Objekt mit einem anderen:
Gibt -1 zurück, wenn das eigene Objekt „kleiner“ ist,
0, wenn beide gleich sind,
1, wenn das eigene Objekt „größer“ ist.
Beispiel:

```ruby
class Song
  include Comparable # modul wird eingebunden
  attr_accessor :length
  def <=>(other) # spaceship operator definiert die methode
    @length <=> other.length # vergleicht die Länge (@length) des aktuellen Song-Objekts mit der Länge eines anderen Song-Objekts:
  end

  def initialize(song_name, length)
    @song_name = song_name
    @length = length
  end
end

a = Song.new('Better Days', 201)
b = Song.new('Glücklich', 200)
c = Song.new('Superpapa', 194)

a < b # false       
b >= c # true
a.between?(c, b) # false
```
Wichtig:
Du kannst selbst bestimmen, nach welchem Kriterium verglichen wird (hier: Länge des Songs). Sobald <=> definiert ist, bekommst du alle Vergleichsoperatoren von Comparable „geschenkt“.

Fazit:
Mit Comparable kannst du eigene Objekte wie Zahlen vergleichen und sortieren, indem du nur eine Methode (<=>) implementierst. Das macht deinen Code flexibler und mächtiger.

## Mix-Ins mit Namespaces und Klassen in Ruby

In Ruby kann man Module als Namespaces nutzen, um gleichnamige Klassen zu trennen:
```ruby
module ToolBox
  class Ruler
    attr_accessor :length
  end
end

module Country
  class Ruler
    attr_accessor :name
  end
end
```

ToolBox::Ruler und Country::Ruler sind zwei verschiedene Klassen.
Mit include Country kann man die Inhalte des Moduls (hier die Klasse Ruler) in den aktuellen Gültigkeitsbereich holen:

```ruby
include Country
c = Ruler.new
c.name = "King Henry VIII"
```

Jetzt kann man Ruler direkt verwenden, ohne Country:: davor zu schreiben.
Möchte man weiterhin auf die andere Klasse zugreifen, nutzt man weiterhin ToolBox::Ruler.
Fazit:
Mit include kann man Klassen und Methoden aus Modulen in den aktuellen Scope holen, sodass sie wie lokale Klassen/Methoden wirken. Das ist praktisch, wenn man temporär einen bestimmten Namespace bevorzugen möchte.

2. Statische Typisierung in Ruby mit RBS

Ruby ist dynamisch typisiert: Der Typ einer Variable wird erst zur Laufzeit bestimmt.

Beispiel:
```ruby
count = 3
puts count.class  # => Integer
```

Seit Ruby 3 gibt es optional RBS (Ruby Signature), um statische Typisierung zu ermöglichen:

```ruby
# sig/employee.rbs
class Employee
  attr_reader name: String
  attr_reader security_level: Integer
  attr_reader email_addresses: Array[String]
  def initialize: (name: String, security_level: Integer) -> void
  def access_granted?: (level: Integer) -> bool
end
```


Man legt eine .rbs-Datei an, die die Typen für Klassen, Methoden und Eigenschaften beschreibt.
Beispiel:
Vorteile:
Findet Fehler (z. B. falsche Typen, fehlende Methoden) schon vor der Ausführung.
Bessere IDE-Unterstützung und Autovervollständigung.
Optional: Man kann RBS schrittweise einführen, nicht für das ganze Projekt auf einmal.
Fazit:
RBS bringt statische Typisierung nach Ruby, was hilft, Fehler frühzeitig zu erkennen und die Wartbarkeit großer Projekte zu verbessern. Es ist aber optional und kann nach Bedarf eingesetzt werden.

Kurz gesagt:

Mit Modulen und include kann man Namespaces flexibel nutzen und Klassen/Mixins in den aktuellen Scope holen.
RBS ermöglicht statische Typisierung in Ruby, um Fehler früh zu erkennen und die Codequalität zu steigern.


## Nutzung von externen Dateien

In Ruby gibt es zwei unterschiedliche Wege, um Code aus anderen Dateien zu laden:

### 1. `require_relative` – Für Module und Klassen

**Wofür?** Um Dateien zu laden, die im gleichen Verzeichnis oder in Unterverzeichnissen liegen.

**Wie funktioniert es?**
- Sucht relativ zur aktuellen Datei (nicht vom Working Directory)
- Cacht die Datei – wird nur einmal geladen
- Ideal für Module, Classes und Mixins

**Beispiel aus vowel_test.rb:**
```ruby
require_relative 'string_extensions'
# Sucht string_extensions.rb im gleichen Verzeichnis wie vowel_test.rb
puts 'This is a test'.vowels.join('-')
# Ausgabe: i-i-a-e
```

**Warum nicht `require './string_extensions'`?**
- `require './...'` sucht vom Working Directory, nicht von der aktuellen Datei
- Funktioniert nicht zuverlässig mit Code Runner
- `require_relative` ist der Standard-Weg in Ruby

---

### 2. `load` mit `File.join(__dir__, '...')` – Für externe Skripte

**Wofür?** Um externe Skripte zu laden, die mehrfach ausgeführt werden sollen.

**Wie funktioniert es?**
- `__dir__` gibt das Verzeichnis der aktuellen Datei zurück (Magic-Konstante)
- `File.join()` verbindet Pfade sicher (funktioniert auf Windows, Mac, Linux)
- Lädt die Datei JEDES MAL neu aus (nicht gecacht!)

**Beispiel aus b_load.rb:**
```ruby
# __dir__        = Das Verzeichnis, in dem DIESE DATEI (b_load.rb) liegt
# File.join()    = Verbindet Pfade sicher (funktioniert auf Windows, Mac, Linux)
# Zusammen: Lade die Datei 'a.rb' aus dem gleichen Verzeichnis wie b_load.rb

load File.join(__dir__, 'a.rb')
puts 'Hello from b.rb'

# Lädt a.rb nochmal - load führt den Code jedes Mal erneut aus (nicht gecacht)
load File.join(__dir__, 'a.rb')
puts 'Hello again from b.rb'
```

**Ausgabe:**
```
Hello from a.rb
Hello from b.rb
Hello from a.rb
Hello again from b.rb
```
(a.rb wird zweimal loaded und ausgeführt!)

---

### Unterschied: `require_relative` vs. `load`

| Aspekt | `require_relative` | `load` |
|--------|---|---|
| **Nutzung** | Module, Classes, Mixins | Externe Skripte |
| **Caching** | Ja (wird nur einmal geladen) | Nein (wird jedes Mal neu ausgeführt) |
| **Syntax** | `require_relative 'dateiname'` | `load File.join(__dir__, 'dateiname.rb')` |
| **Pfad-Typ** | Relativ zur aktuellen Datei | Muss explizit mit `__dir__` und `File.join` gebaut werden |
| **Use-Case** | Wenn du Code einmal brauchst und dann weiterarbeitest | Wenn du Code mehrfach/dynamisch ausführen musst |

---

### Warum funktioniert `require './datei.rb'` oft nicht?

Der Play-Button (Code Runner) startet Dateien oft nicht aus dem Verzeichnis der Ruby-Datei, sondern vom Project-Root. Deshalb schlägt `require './datei.rb'` fehl.

**Lösung:** Immer `require_relative` verwenden!

---

Codebeispiele:

**vowel_test.rb** – `require_relative`
```ruby
require_relative 'string_extensions'
puts 'This is a test'.vowels.join('-')
```

**b_load.rb** – `load` mit `File.join(__dir__, '...')`
```ruby
load File.join(__dir__, 'a.rb')
puts 'Hello from b.rb'
```

### Nested Inclusions

erschachteltes Einbinden (Nested Inclusions) in Ruby

Wenn du mit require, require_relative oder load Dateien einbindest, wird deren Code so behandelt, als wäre er direkt in die Ursprungsdatei eingefügt.
Eingebundene Dateien können selbst wieder andere Dateien einbinden – beliebig tief verschachtelt.
Beispiel:
d.rb → require_relative 'a'
a.rb → require_relative 'b'
b.rb → require_relative 'c'
c.rb definiert eine Methode example
In d.rb kannst du dann direkt example aufrufen, weil alle Einbindungen „durchgereicht“ werden.
Vorteil: Große Projekte lassen sich so modular und übersichtlich strukturieren, auch mit vielen Abhängigkeiten.

##  Bibliotheken und Gems in Ruby



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

## Ruby Gems – Was ist das und wie nutzt man sie?

**Was ist ein Gem?**
- Ein Gem ist ein Paket aus Ruby-Code, das von anderen entwickelt und veröffentlicht wurde.
- Gems enthalten oft Bibliotheken, Tools oder Erweiterungen, die du in deinen eigenen Programmen nutzen kannst.
- Beispiele: `rails` (Webentwicklung), `nokogiri` (XML/HTML-Parsing), `colorize` (bunte Terminalausgabe).

**Warum sind Gems wichtig?**
- Du musst das Rad nicht neu erfinden – viele Probleme sind schon gelöst!
- Du sparst Zeit und bekommst geprüften, oft gut dokumentierten Code.
- Große Projekte werden übersichtlicher, weil du auf viele kleine Bausteine zurückgreifen kannst.

**Wie installiere ich ein Gem?**
- Im Terminal: `gem install <gemname>`
- Beispiel: `gem install colorize`

**Wie nutze ich ein Gem im Code?**
- Mit `require '<gemname>'` bindest du das Gem in dein Ruby-Programm ein.
- Beispiel:
  ```ruby
  require 'colorize'
  puts "Hallo".colorize(:red)
  ```

**Wo finde ich Gems?**
- Die zentrale Anlaufstelle ist [https://rubygems.org](https://rubygems.org)
- Dort kannst du nach Gems suchen, Doku lesen und sehen, wie du sie installierst.

**Standardbibliotheken vs. Gems:**
- Standardbibliotheken sind schon bei Ruby dabei (z.B. `net/http`, `json`).
- Gems musst du meist extra installieren.

**Tipp:**
- Mit `gem list` siehst du alle installierten Gems auf deinem System.
- Mit `gem update` kannst du alle Gems aktualisieren.

**Fazit:**
Gems sind das Herzstück der Ruby-Community. Sie machen Ruby so vielseitig und mächtig, weil du auf die Arbeit von tausenden Entwicklern zurückgreifen kannst. Nutze sie, um schneller und besser zu programmieren!

## Einstieg: Documentation, Error Handling, Debugging & Testing in Ruby
Softwarequalität ist kein Zufall - sie entsteht durch systematisches Arbeiten, gute Dokumentation, sauberes Fehler-Handling, gezieltes Debugging und vor allem durch Tests. Gerade im beruflichen Umfeld sind diese Themen entscheidend, um robuste, wartbare und nachvollziehbare Software zu entwickeln.

1. Dokumentation
Dokumentation ist mehr als Kommentare: Sie hilft dir und anderen, Code zu verstehen, zu warten und weiterzuentwickeln.
In Ruby nutzt man oft RDoc oder YARD für strukturierte Dokumentation.
Gute Dokumentation beschreibt nicht nur das "Wie", sondern auch das "Warum" hinter dem Code.
2. Fehlerbehandlung (Error Handling)
Fehler passieren - entscheidend ist, wie du damit umgehst.
Ruby nutzt begin ... rescue ... end-Blöcke, um Fehler abzufangen und kontrolliert zu reagieren.
Ziel: Programme sollen nicht abstürzen, sondern verständliche Fehlermeldungen liefern oder sich sinnvoll verhalten.
3. Debugging
Debugging ist das gezielte Suchen und Beheben von Fehlern.
Ruby bietet Tools wie puts/p für einfache Ausgaben, aber auch den Debugger (byebug, debug-Gem).
Systematisches Debugging spart Zeit und Nerven – und hilft, die eigenen Denkfehler zu erkennen.
4. Testing
Tests sind das Rückgrat der Softwarequalität.
In Ruby gibt es verschiedene Test-Frameworks: minitest (Standard), RSpec (beliebt für BDD).
Mit Tests prüfst du, ob dein Code das tut, was er soll – und schützt dich vor ungewollten Fehlern bei Änderungen.
Warum ist das wichtig?
Dokumentation, Fehlerbehandlung, Debugging und Tests machen den Unterschied zwischen "funktionierendem" und "professionellem" Code.
Sie sind die Basis für Teamarbeit, Wartbarkeit und Weiterentwicklung.
Wer diese Themen beherrscht, wird zum gefragten Entwickler – gerade im Bereich Softwarequalität.


