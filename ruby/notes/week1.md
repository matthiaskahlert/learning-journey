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

## Symbols in Ruby
Symbole in Ruby sind feste Namen mit Doppelpunkt, zum Beispiel :good, :name oder :male.

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
