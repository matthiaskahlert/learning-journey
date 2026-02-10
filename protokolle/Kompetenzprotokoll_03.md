## Kompetenzprotokoll 3 – Einstieg in Python

Dieses Kompetenzprotokoll dokumentiert meine Lernfortschritte der siebten Woche, in der ich erstmals intensiv mit Python gearbeitet habe. Im Fokus standen grundlegende Pythonkonzepte wie Variablen, Datentypen, Operatoren sowie der Unterschied zwischen veränderbaren und unveränderbaren Objekten.

### 1. Einordnen und Strukturieren (Theorie)

#### Variablen und Zuweisungen
In Python erfolgt eine Zuweisung über den Ausdruck: name = wert.

Eine Variable ist dabei kein Container, sondern ein Verweis (Reference) auf ein Objekt im Speicher. Wird ein neuer Wert zugewiesen, verweist der Variablenname auf ein neues Objekt.

Beispiel:
```py
x = 1
x = 5   # x verweist nun auf ein neues Objekt
```

Im Gegensatz zu JavaScript, wo Zuweisungen mit destructure eher als Zusatzfeature existieren, bietet Python native und besonders einfache Mehrfach- und Parallelzuweisungen:
```py
a = b = 10
x, y = 1, 2
```

#### Datentypen und Typ-Hierarchie
Python stellt verschiedene grundlegende Datentypen bereit: Zahlen ( int, float, complex), Wahrheitswerte (bool), Leerer Wert (NoneType ), Sequenzen (str, tuple, list), Mengen (set) und Abbildungen (dict). Diese Datentypen unterscheiden sich insbesondere darin, ob sie veränderbar (mutable) oder unveränderbar (immutable) sind.

Bei Mutable Datentypen (list, dict, set) finden die Änderungen direkt am Objekt statt, während bei  Immutable Datentypen (int, float, strings, Tupel) Änderungen immer ein neues Objekt erzeugen. 
Warum ist das wichtig? weil dieses Konzept entscheidend sein kann für ein korrektes Verständnis von Python, insbesondere im Umgang mit Speicherverwaltung, Referenzen und Funktionen. Es erklärt z.B., warum Listen in funktionen "verändert zurückkommen" können, Zahlen oder Strings jedoch nicht.

### 2. Verstehen und Verknüpfen (Praxisbeispiele)

Es folgen einige Praxisbeispiele über Unveränderbarkeit von Strings, welche ich in diesem Kompetenzprotokoll reflektieren möchte. Es zeigt: Strings sind unveränderbar. Der Versuch, ein einzelnes Zeichen zu verändern, führt zu einem "TypeError" Fehler.
```py
s = "Hallo"
s[0] = "X"   # TypeError: 'str' object does not support item assignment
```

Um einen geänderten String zu erzeugen, muss ein neues Objekt gebaut werden:
```py
s = "Hallo"
s = "X" + s[1:]
```

Betrachtet man den Unterschied zwischen list und set, erkennt man: Listen erlauben Duplikate, wohingegen Sets doppelte Werte automatisch entfernen.
```py
l = [1, 2, 2, 3]
s = {1, 2, 2, 3}   # doppelte Elemente werden entfernt - > {1, 2, 3}
```

Die Unveränderbarkeit kann man super mit einer Funktion für Speicheradressen und Objektidentität ("id()") untersuchen. Die Funktion id() zeigt die Identität eines Objekts (intern oft dessen Speicheradresse). dafür schauen wir auf ein Beispiel mit immutable - Bei einer Typkonvertierung entsteht hier also ein neues Objekt und  - wie sich herausstellt - daher eine neue ID:
```py
c = 42
print("Wert:", c, "Typ:", type(c), "ID:", id(c)) 
# print ausgabe ist Wert: 42 Typ: <class 'int'> ID: 140709883144264

c = str(c)   # Typecast: int → str
print("Wert:", c, "Typ:", type(c), "ID:", id(c)) 
# print ausgabe ist Wert: 42 Typ: <class 'str'> ID: 21627135164644
```

Obiges Praxisbeispiel zeigt, dass bei Änderungen von immutable objects oder Typecasts bzw Typenkonvertierungen neue Objekte entstehen! Es ändert sich die ID und damit die interne Speicheradresse. Diese Adressen unterscheiden sich auf jedem System, aber es zeigt, dass es ein neues Objekt ist, das auf einen anderen Bereich im Speicher verweist. Gleiches Vorgehen untersuchen wir nun anhand eines mutable Datentyps. Es stellt sich heraus, die Änderungen erfolgen am selben Objekt: 
```py
l = [1, 2, 3]
print("Wert:", l, "Typ:", type(l), "ID:", id(l)) #Wert: [1, 2, 3] Typ: <class 'list'> ID: 2047573815232

l.append(4)
print("Wert:", l, "Typ:", type(l), "ID:", id(l)) #Wert: [1, 2, 3, 4] Typ: <class 'list'> ID: 2047573815232
```

Man erkennt: Listen werden "in-place" verändert, weshalb die Identität und der Speicherwert unverändert bleiben.
Diese Beobachtungen verdeutlichen den grundlegenden Unterschied zwischen veränderbaren und unveränderbaren Datentypen und zeigen wie Python mit Objekten und Referenzen arbeitet

### 3. Anwenden und Bewerten (berufliche Relevanz)

Die behandelten Grundlagen sind für meine zukünftige Arbeit im Softwaretesting und in der testgetriebenen Entwicklung besonders relevant. Das gewonnene Verständnis von Datentypen und deren veränderbarkeit kann sich zukünftig auf die Qualität und Zuverlässigkeit meiner Tests auswirken.
Zu wissen, wann eine Variable auf ein neues Objekt zeigt und wann ein bestehendes Objekt verändert wird kann entscheidens sein für Fehlersuche und Debugging, Reproduzierbarkeit und Rückverfolgbarkeit von Testergebnissen, das Verstehen von Funktionsparametern und auch für das Vermeiden von Seiteneffekten in Testfällen.

Die Praxisbeispiele von Mutable/Immutable im Testkontext / Softwaretesting und beim Arbeiten mit Testdaten zeigen: Es ist wichtig einschätzen zu können, wann meine Testdaten (z.B. input daten bei Unit-Tests) unverändert bleiben, wann möglicherweise Seiteneffekte auftreten, z.B. wenn ich eine Liste an eine Funktion übergeben muss, wie Datenstrukturen eventuell ungewollt verändert werden und wie man eine sichere Testdatenbasis schafft
Datenaustausch findet ja häufig in Form von JSON-Strukturen oder XML-Modelle statt. Das Konzept hilft mir am Ende des Tages, damit sauberer umzugehen um damit fehlerhafte Testergebnisse zu vermeiden.
Die Grundlagen können mir in Bezug auf Automatisierung auch den Einstieg in Frameworks wie PyTest oder Robot Framework erleichtern z.B. bei der validierung von API-Daten.

### 4. Reflektieren und Hinterfragen (Weiterentwicklung)

Die erste Python-Woche hat mir einige Bausteine für ein stabiles Fundament vermittelt. Mein bisheriger Kurs und der PYthon kurs sind auch didaktisch unterschiedlich aufgebaut, ich habe den Eindruck dass der Selbststudium anteil in Python höher ist, komme aber aufgrund der Vorkenntnisse aus dem JavaScript kurs ganz okay zurecht damit. Gleichzeitig sind dabei neue Fragen entstanden, die ich versuchen werde, in den kommenden Wochen zu vertiefen:

- Worin unterscheiden sich Shallow Copy und Deep Copy?
- Welche Datenstrukturen eignen sich besonders für umfangreiche Testdaten?
- Wie lassen sich moderne Testing-Konzepte wie Test Driven Develeopment mit Python umsetzen?
- Wie schreibe ich gute Unit-Tests mit Python?

In der nächsten Woche möchte ich bewusst kleine Programme schreiben, um ein besseres Gefühl für Unis-Tests in Python zu bekommen.