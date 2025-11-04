# Meine Markdown notes Woche 1

Um das gelernte Wissen anwenden zu können ntiere ich mir die Lerninhalte und Beispiele.
 [TOC] 





## Tag 1

JavaScript benötigt HTML und CSS Kenntnisse um den Einstieg zu erleichtern, denn es geht bei JavaScript hauptsächlich um das Eingreifen in die Darstellung von Websites.
Daher sollte das HTML sicherheitshalber vom Validator geprüft werden.


## Learningfacts Kapitel 1 - HTML und CSS

- Cascading ist das Einfließen von Stilen aus vorangegangenen CSS Regeln.
- Bei der Kommunikation mit dem Server via JavaScript geht es um das Einlesen und Weiterreichen von Benutzereingaben, hier reichen solide Grundlagen für CSS.
- Man kann JavaScript Anweisungen direkt in die HTML Datei schreiben oder in eigene Dateien mit der Endung .js. Diese separaten .js Dateien kann man mit einem HTML script-Tag direkt in die HTML Datei einbinden. Beispiel: <script src="script.js" defer></script>
- Es gibt Module die man im und exportieren kann. Module organisieren Script Dateien, indem sie anwendungen in überschaubare Teile herunterbrechen und sie in separaten Dateien speichern. Diese Fragmente werden als Module importiert. Das type-Attribut des script Elements kennzeichnet JavaScript Dateien als Module.
- Da Browser HTML Dateien Zeile für Zeile laden, aber bei externen CSS Dateien den Inhalt komplett laden, kann es zu Latenzen kommen. Dies wird mit "just-in-time-loading" verhindert, dafür nutzt man die Attribute: defer und async. Mit defer lädt der Browser scripte erst vollständig (in derReihenfolge in der sie im code erscheinen), bevor er sie ausführt. Scripte mit async  werden ohne beachtung der Reihenfolge ausgeführt.
- Für JavaScript Entwicklung ist in den Browsern die Browserkonsole der Dreh- und Angelpunkt, z.B. in Chrome via F12 -> console. Man kann über Anweisungen im JavaScript Code oder direkt in der Browserkonsole arbeiten um beispielsweise Variablen und Objekte zu testen und Ihre Struktur aufzuzeigen. Die Konsolenausgabe im Script erfolgt über console.log(var1, var2, vae3...); Beispielsweise braucht man nur den namen einer Variable um den Variablenwert zu sehen. Beispiel const mwst = x * mwstSatz / 119;
        console.log(mwst);
  
## Learningfacts Kapitel 2 - Variablen und Syntax

- JavaScript nutzt zur Deklaration (Bekanntmachung) von Variablen drei Schlüsselwörter: var, let und const.
- Variablennamen sollten mit einem Kleinbuchstaben, einem Unterstrich oder einem Dollarzeichen beginnen. Sie sind Case-sensitive: X ist eine andere Variable als x. Viele nutzen sogenanntes CamelCase, wobei die Variable klein beginnt, jedes neue Wort aber groß weitergeht. Beispiel: let alterVater, alterMutter, alterKind;
- Variablen haben Gültigkeitsbereiche (Scope) und gelten nur in dem Block, in dem sie deklariert wurden.
- Die Syntax ist die Grammatik der Programmiersprache. Es gibt 
- Operatoren (zb boolsche, oder Mathematische wie AND, OR, NOT, +, - =) wobei das Gleichheitszeichen ein Zuweisungsoperator ist. Beispiel: 


        
        const breite = 200;
        const höhe = 125;
        let fläche = breite * höhe;


        
- Ausdruck (Expression), was eine Kombination aus Variablen, Operatoren und Werten darstellt
- Semikolon - Regel, nicht hinter schließenden geschweiften Klammern, nur hinter Anweisungen.
- Schlüsselwörter (Keywords) beispielsweise let und const
- Kommentare (Comments) alles auf einer Zeile nach // sowie zwischen /* ... */ ist ein Kommentar und wird nicht ausgeführt bzw vom Browser ignoriert.
- Namen (Identifier) - ein Identifier ist ein Name den ich benutze um etwas zu benennen. Beispiel: Variablen (let name = "Matze";) - hier ist Variablen der Identifier, name die Variable und Matze der Wert, welcher der Variablen zugeordnet ist. Die Variable kann über den identifier angesprochen werden. Identifier müssen mit Buchstaben einem Dollarzeichen uoder einem Unterstrich beginnen. das erste Zeichen darf keine Ziffer sein, Bindestriche sind nicht erlaubt (wird als Minus interpretiert).
- Hochkommas - Sie sind für String genutzt, entweder doppeltes oder einfaches Hochkomma, Backticks sind empfehlenswert, wenn der String Zeilenumbrüche oder Variablen enthalten soll.
## Übungsaufgabe 2.2.Ü.01
Die Aufgabe erschien mir einfach, aber durch das einbinden der separaten .js Datei kam es sozusagen zu einem Laufzeitfehler, welchen ich mit dem defer attribut beheben konnte. Anfangs hatte ich fehlerhafterweise auch noch den scr typ "module" zugewiesen, welcher den console output blockierte. Das entfernen des modules führte zur Lösung. ich habe mich für eine Konstante bei dem Namen entschieden, und für eine let variable beim alter.


## Kompetenzprotokoll 1

Um Schwerpunkte und einen Fokus bei meinem Lernfortschritt zu setzen, wende ich das Prinzip des Kompetenzprotokolls an. Dies ist ein Teil der Prüfungsleistung in meiner Weiterbildung. Hierbei bearbeite ich das Gelernte wöchentlich in den vier Kategorien:
- Einordnen und Strukturieren: Theorie erklären
- Verstehen und Verknüpfen: Praxisbeispiel erklären
- Anwenden und Bewerten: Berufliche Relevanz erörtern
- Reflektieren und Hinterfragen: Lernprozess reflektieren oder offene
bzw. weiterführende Fragen formulieren

Zwei Themengebiete, welche mir derzeit als sehr relevant erscheinen ist die Browser-Konsole und die Live-Server Extension bei Visual Studio Code.

Die Browser-Konsole ist Teil der Entwicklungswerkzeuge für die Webentwicklung und auf allen Haupt Browsern verfügbar. In Kombination mit dem Liveserver sehr hilfreich.

 ### Einordnen und strukturieren (Theorie erklären)
 
    Am ersten Kurstag habe ich besonders die Nutzung der Browser-Konsole und die Live-Server Extension in Visual Studio Code als interessant empfunden. 
    Die Browser-Konsole ist ein zentrales Tool um die Änderungen meiner JavaScript-Dateien direkt im Browser auszuführen und Fehler zu identifizieren. 
    Man kann über Anweisungen im JavaScript Code oder direkt in der Konsole arbeiten um Variablen, Funktionen oder Berechnungen zu überprüfen. 
    Damit ist es mir möglich Änderungen "on the fly" zu testen und sofort die Auswirkungen von Änderungen zu beobachten. 
    Die Live-Server-Extension von VSCode unterstützt dies, indem sie HTML Dateien automatisch neu lädt, sobald ich die Änderungen speichere. 
    So kann ich ohne refresh den direkten impact sehen. Das zentrale Prinzip hier sind schnelle Feedback-Zyklen und direkte Sichtbarkeit von Änderungen.
    
### Verstehen und verknüpfen (Praxisbeispiel erklären)

    Ein konkretes Beispiel aus meiner bisherigen Erfahrung ist das testen kleiner JavaScript Funktionen direkt in der Browser Konsole. 
    Ich konnte einfache Berechnungen direkt auf Korrektheit überprüfen, indem ich die Konsole nutzte. 
    Die Live-Server Extension hat durch die direkte automatische Aktualisierung mein Verständnis vertieft, wie sich meine Änderungen auf meine Seite auswirkten. 
    Dies war bei der Fehlersuche der Übungsaufgabe sehr wertvoll, da es meine Lernkurve beschleunigt hat.
    So konnte ich die entsprechenden Fehlermeldungen wie die geworfenen Exceptions direkt in der Browser-Konsole sehen was wiederum zu einem Umdenken und ausprobieren führte. 
    Schließlich führten meine Bemühungen dann auch zum Erfolg einer akzeptablen Umsetzung der Übungsaufgabe.
    
### Anwenden und bewerten (berufliche Relevanz erörtern)

    Für meine berufliche Praxis im Testmanagement und dem Softwaretesting sehe ich den Nutzen der Browser-Konsole und der Live-Server Extension direkt im schnellen Überprüfen von JavaScript Funktionen und HTML Elementen.
    Dies ermöglicht eine frühe Fehlererkennung und spart Zeit und Aufwand im späteren Verlauf der Softwareentwicklung.Dies erleichtert die Qualitätssicherung, aber zeigt auch die Relevanz für Softwareentwickler, um ein Verständnis der Funktionsweise von Code zu gewinnen. 
    Dies erleichtert auch die Kommunikation mit Entwicklern, wenn es um Fehlerbeschreibungen geht.
    Nicht zuletzt die Eingangs erwähnten kurzen Feedback-Zyklen verkürzen die Entwicklungszeit und ermöglichen auch das schnelle validieren von Bugfixes.
    
### Reflektieren und Hinterfragen

     Rückblickend auf den ersten Kurstag habe ich erkannt, dass es mit der Browser-Konsole und der Live-Server Extension Wertvolle Hilfsmittel gibt, die den Lernprozess unterstützen und die Fehlersuche zu vereinfachen. 
    Folgefragen: 
     - Welche erweiterten Funktionen erleichtern komplexere Debugging-Szenarien? 
     - Welche Konfigurationsmöglichkeiten habe icch beim Live-Server speziell bei größeren Projekten? 
     - Mich interessiert auch, wie diese Tools in Testgetriebene Entwicklungsprozesse integriert werden können, um dies als Best-Practice mitzunehmen. 
     Mir hat die Nutzung den direkten Zusammenhang zwischen der Theorie der Code-Logik und der visuellen Umsetzung verständlicher gemacht. Weitere Vertiefung erkenne ich als notwendig an.

## Was ich morgen lernen will - Tag 1?

Mehr insights über Datentypen in JavaScript, also Typecasts / Datentyp-Konvertierungen sicher beherrschen.

## Tag2

## Learningfacts Kapitel 3 - Grundlegende Datentypen

### 3.1  Datentypen

Es gibt folgende Datentypen:
        - Number (Integer oder Float)
        - Strings
        - Boolean
        - Null (leer, absichtliche Abwesenheit eines Wertes)
        - Undefined (Variable der noch kein Wert zugewiesen wurde)
        - BigInt (Zahlen zu groß für Number)
            Beispiel: Zum erzeugen ein n an die Integerzahl anhängen oder BigInt() aufrufen: let big = 123456789123n; 
        - Symbol (unveränderlicher Wert, z.B. um eindeutige Eigenschaften zu definieren)
        
### 3.2 Int und Float

- Integer und Float
  In JavaScript sind Int und Float vom Typ Number.
  Zahlen werden im 64-bit Gleitkommaformat gespeichert.
  Wenn man ein int und ein float addiert, entstehen minimale Fehler bei der Konvertierung der Zahlen. Dies führt zu Ungenauigkeiten bei der Darstellung von Brüchen. Es handelt sich also um Annäherungen an den nicht exakt zu treffenden Wert.
  - Negative Zahlen, unendlich und NaN kennt JavaScript auch. Unendlich wird mit dem Schlüsselwort Infinity definiert. NaN (Not a Number) entsteht wenn der Code zu einer ungültigen Zahl führt, beispielsweise wenn man versucht, zwei Variablen mit dem Wert 0 durch null zu teilen, allerdings gilt es zu beachten, dass die Browserkonsole keinen Fehler ausgibt.
### 3.3 Boolean
- Boolsche Werte
true und false beziehungsweise 1 und 0 sind die unterste Ebene. Variablen vom Typ Boolean können nur einen Wert annehmen: true oder false, dies wird genutzt bei if/else Abfragen und Schleifen wie while oder "switch" Anweisungen.
Boolesche Operatoren sind && (logisches AND), || (logisches OR), und ! (logisches NOT).
- a&&b true wenn beide Operanden true sind
- x||y true wenn mindestens einer der beiden Operanden true ist
- !c gibt das Gegenteil des Wahrheitswertes von c zurück
- 
### 3.4 Strings - Zeichenketten

- Alles in Hochkommas ist ein String!
- Erlaubte Hochkommas sind 
  Backtick                ``
  einfaches Hochkomma     ''
  doppeltes Hochkomma     ""
  Anführungszeichen und Apostrophe sind nicht erlaubt. Strings können zusammengeführt werden mit +, dies nennt man Konkatenation was in diesem Fall eine Verknüpfung der Strings darstellt.
  
```js
const str1 = 'Schnee'
const str2 = 'ball'
let ergebnis = str1 + str2
console.log("Ergebnis ist", ergebnis)
```

Strings in Hochkomma dürfen keinen Zeilenumbruch haben, mit Backticks geht es allerdings. Innerhalb von Backticks dürfen auch Variablen stehen!
Variablen in Strings stehen in geschweiften Klammern {} und ihnen geht ein $ Zeichen voran:
```js
const q = 129
const w = 23
const mwst = `Im Betrag ${q + q * w / 100} € sind ${q*w /100} € MwSt. enthalten`;
console.log(mwst);
```
- typeof kann den Datentyp hinterfragen: console.log(mwst, typeof mwst); gibt den Wert von mwst und string als output in die Konsole.
- Variablen, die ohne Wert mit let deklariert sind, wird der Wert undefined zugewiesen.
- null wird zugewiesen, wenn man anzeigen möchte, dass kein Wert zugewiesen wurde. Es gibt einen Wert empty, den man herausfinden kann, indem man die Länge des Strings oder eines Arrays prüft.
 ```js       
            const schrank = [];
            if (schrank.length >0) {
                ("Elemente Ausgeben");
            }   else {
                console.log("Nichts im Schrank!");
            } //Konsolen Log: Nichts im Schrank! die array.length Funktion prüft die Länge des Arrays
```
            
### 3.6 Datentyp Konvertierungen

JavaScript verzichtet auf einen expliziten Datentyp bei der Deklaration von Variablen. Vorteil ist: Geschwindigkeit, Nachteil: Bei Problemen ist die Fehlersuche schwierig.
Die Konvertierung eines String in einen Number Datentyp ist notwendig bei der Erfassung von Usereingaben auf Webseiten in einem Formularfeld, da die Werte als Strings ankommen. 
- Es gibt die Funktion parseInt() um diese Datentypumwandlung vorzunehmen. Es wird alles bis zum ersten nicht numerischen Zeichen geparst. 
- mit parseFloat() wird der Dezimalpunkt berücksichtigt.
- eine weitere Konvertierung ist Number(), diese Methode akzeptiert Ziffern, den Dezimalpunkt und auch Vorzeichen wie - und + gibt allerdings NaN zurück, wenn ein anderes Zeichen im String ist.
Unary Operator oder Plus-Operator ist auch eine Option:
 ```js  
        
        let u = "24.56";
        let uni = +u;
        console.log("Unary", uni, typeof uni);
```
        
NaN wird gebraucht wenn sichergestellt werden muss, das für Operationen ein Zahlenwert vorliegt. 
Mit der Funktion isNaN() wird geprüft ob der Variable ein Zahlenwert zugrunde liegt.
- Number zu String
Die Funktion .toString() wandelt einen Variablenwert in einen String um.

 ```js        
let h = 12345;
result = h.toString();
console.log("h wurde umgewandelt", result, typeof result ); //log: h wurde umgewandelt 12345 string
```
        
In der Klammer kann auch ein Parameter stehen, wenn es sich vorher um eine Number gehandelt hat, man kann dann die Zahlenbasis angeben.
- Number zu Boolean
Nur 0 liefert false, alles andere liefert den Wert true nach Datentypkonvertierung. Beispiel:
 ```js         
 const bnum = 256;
 const bumw = Boolean(bnum);
 console.log("Boolean´sche Umwandlung bumw ist gleich:", bumw, typeof bumw);
```
            
- String zu Boolean
  nur ein leerer String führt zu false
- implizite Datentypumwandlung
JavaScript wandelt automatisch Werte von einem Datentyp in einen anderen um, dies kann aber Fallstricke mit sich führen (Thema Konkatenation) also Verknüpfung von Strings Beispiel:

```js      
  const result1 = "10"
  const result2 = 5
  result3 = result1 + result2
  console.log(result3); //log:"105"
  console.log(0 == "0"); log:true // hier wandelt JavaScript automatisch um
  console.log(0 === "0"); log: false //bei === keine umwandkung, typen sind verschieden (Zahl und String)
```

## Was ich morgen lernen will - Tag 2?

Mehr insights über zusammengesetzte Datentypen in JavaScript, also Objekte wie das DOM.


## Tag 3
## Learningfacts Kapitel 4 - zusammengesetzte Datentypen

Komplexe Datentypen nennt man Objekte, sie können mehr als eine Komponente speichern. So kann ein Objekt beispielsweise einen String, Number und einen Booleanwert enthalten. Objekte erkennt man an den geschweiften Klammern:
```js 
const kurs = { 
    title:      "Stricken für Anfänger",
    coach:      "Julia",
    places:     12,
    started:    true,
    location:   "Hamburg",
}
```
Das Objekt kurs hat auch Informationen wie title und places, welche man als Eigenschaften bezeichnet, englisch properties. Von außen spricht man das Objekt folgendermaßen an:
kurs.places ist eine Eigenschaft des Objekts und stellt einen besonderen Typ einer Variablen dar. So kann man sie auch ändern:
kurs.places = 14;
kurs.title = "Stricken für Anfänger - Teil II";

- Das wichtigste Objekt ist das DOM (Document Object Model), es ist die Schnittstelle zum HTML-Dokument. Objekte haben Eigenschaften, und Methoden für die einfachen Datentypen Strings, Number, Boolean.


### Math Object

Es gibt globale Objekte, die man nicht erzeugen muss, um sie zu nutzen, man kann sie direkt einsetzen, wie das Objekt Math.
Gibt man in der Browserkonsole "Math." ein, werden einem die verschiedenen Komponenten von Math angezeigt.
Die mathematischen Konstanten werden mit dem Math Objekt entsprechend genutzt wie: 
* Math.PI, 
* Math.SQRT1_2 (Quadratwurzel von 1/2),
* Math.LN10 (Logarithmus Naturalis zur Basis 10)
Die Konstanten werden in Großbuchstaben geschrieben.


Andere Methoden nicht:
* Math.cos()
* Math.trunc() (gibt den Wert vor dem Komma zurück, entfernt Nachkommastellen)
* Math.floor() rundet ab, bei negativen Zahlen also Math.floor(-2.7) -> ergibt -3
* Math.random() (erzeugt einen Random-Wert zwischen 0 und 1)
* Math.max() (gibt die größte von null oder mehr Zahlen wieder)
* Math.min() (gibt die kleinste von null oder mehr Zahlen wieder)


### Operanden und Operatoren

Die üblichen mathematischen Operatoren bei JavaScript sind:
    - Addition          +
    - Division          /
    - Multiplikation    *
    - Subtraktion       -
    - Inkrement         ++ (Kurzform für +1)
    - Dekrement         -- (Kurzform für -1)
    - Exponent          **
    - Modulo            %  (Reminder: gibt nur den Rest zurück. 7 % 3 = 1, also 7 geteilt durch drei sind 2, mit dem Rest 1)
    - Negation          -
Man kann die Modulo Berechnung auch nutzen um zu prüfen ob ein Wert gerade oder ungerade ist, bei einer division durch zwei haben gerade Zahlen keinen Rest.
```js 
const num = 23
if (num % 2 === 0) {
    console.log(`${num} ist eine gerade Zahl`)
} else {
    console.log(`${num} ist eine ungerade Zahl`)
} //23 ist eine ungerade Zahl
```

### Zuweisungen

Das Gleichheitszeichen ist auch ein Operator, es weist der Variablen auf der linken Seite einen Wert zu.

Zuweisen                    =
Addieren und zuweisen       +=
Subtrahieren und zuweisen   -=
Dividieren und zuweisen     /=
Multiplizieren und zuweisen *=
Exponent und zuweisen       **=
Modulo und zuweisen         %=

### Vergleichsoperatoren

hat denselben Wert      ==
strenges gleich         ===
ungleich                !=
strenges ungleich       !==
größer als              >
kleiner als             <
größer oder gleich      >=
kleiner oder gleich     <=


### String Eigenschaften

Stringlänge - string length
Ein String hat eine Länge, dies ist eine Eigenschaft.
Eigenschaften werden (wie bei Objekten) mit einem Punkt vor dem Variablennamen geschrieben.

```js
const str1 = "Matthias Kahlert"
const stringLänge = str1.length;
console.log(` Der String ${str1} hat die Stringlänge von ${stringLänge}.`);

const a1 = str1[0]; //JavaScript erreicht jedes Zeichen im String mit einem index aus eckigen Klammern. es Beginnt bei 0 zu zählen. 
console.log(`Das 1. Zeichen des Strings ist ${a1}.`);
```

Ein String hat Eigenschaften wie: Unterteilen, Suchen und Ersetzen.
In der Browserkonsole kann man mit console.log("String", str1.__proto__); alle Möglichkeiten der String Eigenschaften sehen.

Wichtige Methoden: 
- replace(searchValue, replaceValue)
 Ersetzt das erste Vorkommen von SearchValue durch replaceValue
- replaceAll(searchValue, replaceValue)
Ersetzt alle Vorkommen von searchValue.
- indexOf(substring)
Gibt den ersten gefundenen index des Zeichens des strings zurück. Es hilft, sich den string als Array vorzustellen. Jedes Zeichen des Strings hat eine Indexnummer, beginnend mit der 0.
- search()
Mit einem RegEx sucht search() auch nach Variationen des Suchmusters.
- split()
- includes()
Gibt true zurück, wenn die gesuchte Zeichenfolge im String enthalten ist.

           const randomQuote = "Aller Anfang ist schwer!";
           console.log(randomQuote.includes("Anfang"));
  
- string.substring(start,end)
  start für das erste Zeichen end für das letzte. mit nur einem argument gibt substring() den Teilstring von start bis ende zurück.
- string.replace()
- string.replaceAll()
- string.toLowerCase()
- string.toUpperCase()
- string.charAt()
  gibt das Zeichen des Strings an einem Index zurück. 
- string.charCodeAt()
  gibt den Unicode Wert zurück (In UTF-16)
- string.match
  durchsucht einen String nach einer Zeichenkette und gibt den ersten Treffer zurück. Mit Nutzung von regulären ausdrücken gibt es alle Treffer zurück. Wenn Match mit regEx genutzt wird (regEx sitzen in Schrägstrichen anstatt in hochkommas), wird es um zwei Parameter erweitert. i ( case insensitiv) und g (global) durchsucht den ganzen String.
- string.slice()
  extrahiert einen Teil aus dem String mit start (inklusive) und end (exklusive)Argumenten.
- string.slice
  kann auch vom ende her zählen also mit negativen Werten als string.slice(-5) gibt es die letzten fünf Zeichen des Strings aus.
- string.sort()
Sortierreihenfolge basiert auf UTF-16 codewerten. Problematisch bei Zahlen: [1, 100000, 21, 30, 4]
- string.localeCompare()
  vergleicht zwei Strings unter Einbeziehung der Sprache miteinander und gibt einen numerischen Wert zurück. Es gibt drei Argumente:

              1. Zeichenkette die verglichen wird
              2. Länderkürzel (Weglassen, denn Browser default genutzt werden soll)
              3. sensitivity, optional, default ist nicht case sensitiv. es geht u-kf-upper und u-kf-lower, sowie u-kn-true (für die sortierung von zahlen)
              
- string.split() teilt einen string bei jedem vorkommen eines Zeichens oder Teilstrings und speichert die Teile in einem Array. Dies kann nützlich sein beim trennen einer CSV.
- string.trim() entfernt "Weißraum" also Leerzeichen, Tabstops, Zeilenumbrüche am Anfang und am Ende eines Strings. Dies kann wichtig sein, wenn man daten aus Eingabefeldern von Formularen übernimmt!
- es gibt auch string.trimLeft() und string.trimRight() wenn man nur an einer Seite die Leerzeichen entfernen möchte.
- array.join()
Methode um array elemente in einen string zu übergeben. in der Klammer kann ein separator stehen, default (also wenn keiner gegeben ist) wird ein Komma gesetzt.

´´´js
const stadtnamenString = gefundeneStaedte.join();
console.log(stadtnamenString); //log: Berlin,Köln,München,Hamburg,Leipzig,Dortmund
´´´


### 4.10 Reguläre Ausdrücke

Reguläre Ausdrücke werden z.B. genutzt um Benutzereingaben zu prüfen, sie können verhindern, dass z.B. HTML Tags in Eingabefelder geschrieben werden, bzw. diese ignoriert werden. Man spricht von Regex (Regular Expressions)


#### Metazeichen und Suchmuster

Reguläre Ausdrücke enthalten ein Suchmuster aus Metazeichen für irreguläre Zeichenfolgen. Das Metazeichen für Zahlen ist Beispielsweise \d oder [0-9]. Ein Suchmuster für fünf Zahlen wäre dem zur Folge \d5 oder [0-9]{5}
    es gibt weitere Platzhalter:
    
        - \w Buchstabe, Ziffer oder Unterstrich
        - \W ein Sonderzeichen
        - \d eine Ziffer zwischen 0-9
        - \D ein Zeichen, dass keine Ziffer ist
        - \s ein Weißraum
        - \S Jedes Zeichen ausser Weißraum
        - \b Wortgrenze (Ein Wort beginnt und endet an Wortgrenzen.)
        - \B keine Wortgrenze
        
Metazeichen wie ^und $ suchen am anfang bzw am Ende eines Strings

        - . findet alle Zeichen außer Zeilenende
        - ^ Anfang eines Strings
        - $ Ende eines Strings
        - | Alternativen
        - () Teile des Suchmusters abgrenzen
        - [] Zeichenklassen
        - {} Replikatoren

        
#### Zeichenklassen

    - [xyz] beliebiger Buchstabe x, y oder z
    - [^xyz] jeder buchstabe außer xyz
    - [0-9] Ziffern 0-9
    - [a-z] jeder Kleinbuchstabe von a-z
    - [A-Za-z0-9] alle Buchstaben und Ziffern
    - [a-zß-ü] alle Kleinbuchstaben und Umlaute

        
#### Replikatoren
    - {n,m} mindestens n mal höchstens m mal
    - {n,} mindestens n mal
    - {n} genau n mal
    - * 0 mal oder öfter, äquivalent zu {0,}
    - + 1 mal oder öfter, äquivalent zu {1,}
    - ? 0 oder 1 mal, äquivalent zu {0,1}
        
Methoden regulärer Objekte: exec() und test()
    analog zu suchmethoden search() bei Strings bieten diese beiden suchmethoden für Regex.Die Methoden werden auf dem Regex ausgeführt, ihr Argument ist der String: regex.exec(string)
    exec() findet die erste Position eines Suchmusters oder null
    test() prüft ob ein String dem Muster entspricht.
    Man kann also Strings auf reguläre Ausdrücke prüfen.

## Was ich morgen lernen will - Tag3?
Mehr insights über Schleifen, Abfragen, Ablaufkontrollen!


## Tag 4
## Learningfacts Kapitel 5.1-5.4 Abfragen und Schleifen
### 5.1 Abfragen und Schleifen
If/else Abfragen sind nötig f++ür die Logik von komplexen Abläufen.
Die beiden Grundlegenden Methoden sind 
* Verzweigungen: if/else, switch
* Schleifen und Iterationen (while,for)

*Verzweigungen*
```js
if (Bedingung){
    Anweisungen;
} else {
    Anweisungen;
}


switch (Ausdruck) {
    case label1:
        Anweisungen;
        break;
    case label2:
        Anweisungen;
        break;
    ...
}
``` 

*Schleifen*
```js
while (Bedingung) {
    Anweisungen;
} 

do {
    Anweisungen;
} while (Bedingung);
```

*Iteration*
```js
for (Anweisung; Bedingung; Anweisung) {
    Anweisungen;
}
```
### 5.2 if.then-else
die if-Abfrage führt Anweisungen nur aus, wenn die Vedingun erfüllt ist.
Bedingung kann alles sein, was true oder false zurückgibt. Zur Formulierung nutzt man logische- und Vergleichsoperatoren.
Anweisungen können auch weitere if/else Bedingungen darstellen, und somit tiefer verschachtelte Anweisungen, dies braucht man z.B. wenn mehr als nur "endweder oder" vorliegt, also mehrere optionen.
Die geschweiften Klammern in der if-Abfrage erzeugen den Gültigkeitsbereich der Variablen den sog. Block-scope.
Wichtig: Variablen die im Block scope deklariert werden, sind ausserhalb der geschweiftenklammern dem zur folge nicht Gültig, bzw gelten als undefiniert / nicht bekannt.

Es gibt eine Kurzform der if-/else, wenn nur eine Anweisung vorliegt:

```js
if (x>=y) console.log(`${x}>=${y}`);
else console.log(`${x} ist nicht >= ${y}`)
```
Bei mehreren Optionen beginnt das verschachteln der Abfragen:

### 5.3 switch

JavaScripts switch case führt die Anweisungen in einer Liste auf. Insbesondere bei komplexeren if/else Abfragen bietet switch eine bessere Übersicht über die Alternativen.

```js
const country = "Frankreich";
switch (country) {
    case "Deutschland":
        console.log("Deutschland");
        break;

    case "Frankreich":
        console.log("Frankreich");
        break;

    case "Irland":
        console.log("Irland");
        break;

    default:
        console.log(`Weder Deutschland, Frankreich oder Irland`);
}
```
break sorgt dafür, dass der case verlassen wird, default ist für Fälle, in denen keine der Bedingungen zutrifft.
fehlt das break, werden die anweisungen des folgenden switch cases auch durchgeführt.

Wenn man die gleiche Variable in verschiedenen switch cases benötigt, kann man sich den block scope zur nutze machen:

```js
const auswahl = "Äpfel";
switch(auswahl) {
    case "Birnen":
        const wahl = "Birnen";
        console.log(`${wahl}`);
        break;

    case "Äpfel":
        const wahl = "Äpfel";
        console.log(`${wahl}`);
        break;

    default:
        console.log(`${auswahl} nicht im Angebot`); // log: Uncaught SyntaxError: Identifier 'wahl' has already been declared
    }

```
daher kann man geschweifte Klammern setzen im case und den Gültigkeitsbereich der Variablen auf den case beschränken:
```js
    case "Birnen":
        {
        const wahl = "Birnen";
        console.log(`${wahl}`);
        }
```


### Regex: Wörter mit Großbuchstaben finden
Es gibt die Aufgabe eine Variable mit Stadtnamen zu erstellen und mithilfe von Regex alle Wörter, die mit einem Großbuchstaben beginnen (also Stadtnamen) zu finden. Der einfachheit halber habe ich auf andere Wörter mit Großbuchstaben verzichtet.
#### Beispieltext:
```js
const text = `Berlin ist schön groß.
Köln ist bekannt.
München begeistert viele.
Hamburg ist toll!
Leipzig wächst schnell.
Dortmund ist auch halbwegs bekannt.`;
```
#### Lösung mit Regex
```js
const gefundeneStaedte = text.match(/\b[A-Z][a-zß-ü]{1,}/g);
console.log(gefundeneStaedte); 
// Ausgabe: ['Berlin', 'Köln', 'München', 'Hamburg', 'Leipzig', 'Dortmund']

```
#### Erklärung des Regex
| Teil           | Bedeutung                                                                            |
| -------------- | ------------------------------------------------------------------------------------ |
| `/…/`          | Trennt das **Regex-Muster** vom restlichen Code                                      |
| `\b`           | **Wortgrenze** → stellt sicher, dass das Muster am Anfang eines Wortes beginnt       |
| `[A-Z]`        | Das erste Zeichen muss **ein Großbuchstabe** sein                                    |
| `[a-zß-ü]{1,}` | Danach kommen **ein oder mehrere Kleinbuchstaben** (inklusive `ß` und Umlaute `äöü`) |
| `g`            | **global flag** → durchsucht den gesamten String, nicht nur den ersten Treffer       |

Finde alle Wörter, die mit einem Großbuchstaben beginnen (also Stadtnamen).

#### Funktionsweise
1. match() sucht im Text nach allen Stellen, die auf das Regex passen.

2. Jedes Wort, das mit einem Großbuchstaben beginnt und danach nur Kleinbuchstaben hat, wird zurückgegeben.

3. Ergebnis ist ein Array aller gefundenen Stadtnamen.



## Tag 5

## Learningfacts Kapitel 5.5-5.11 Abfragen und Schleifen

### 5.5 for-Schleifen
#### Funktionsweise von Schleifen
Durch wiederholungen greifen Schleifen wiederholt auf Daten zu. die for-Schcleife baut sich wie folgt auf:
```js
for ([Anfangsausdruck]; [Bedingung]; [Inkrement])
Anweisung;

for (let i = 0; i<= 9; i++) {
    console.log(i) // Anweisung: mach was mit i
}
```

| Teil                       | Bedeutung                                                        |Beispiel               |
| -------------------------- | ---------------------------------------------------------------- | --------------------- |
| Startwert/Anfangsausdruck  | Wird einmal an Anfang ausgeführt                                 | let i = 0             |
| Bedingung                  | Wird vor jedem Durchlauf ausgeführt Wenn false Schleife endet    | i<5                   |
| Inkrement / Schritt        | Wird nach jedem Durchlauf ausgeführt                             | i++ (erhöht i um 1)   |



Da die Schleife die Variable mit jedem Durchlauf verändert, sind Konstanten hier ungeeignet für i.
Auch hier: Geschweifte Klammern bilden einen Block-Scope.

```js

const step = 5
for (i = 1; i<=20; i+=step) {
    const result = i * 17;
    console.log("result", `${i} * 17 = ${result}`);
}

```

#### Verschachtelte for-Schleifen
```js
const hue = [14, 28, 95]
const sat = [50, 100]

for (let i =0; i<hue.length; i++) {
    console.log(`${i}. Farbe: ${hue[i]}`)
    for (let j=0; j<sat.length; j++) {
        console.log(`Farbe hsl(${hue[i]}, ${sat[j]}%, 100%)`)
    }
}
```

Die innere Schleife läuft bis zur letzten Bedingung und geht dann wieder in die äußere.

#### Break und continue
break beendet eine Schleife vorzeitig und kann nur innerhalb von switch-,while- und for-Schleifen verwendet werden.

```js
for (let i = 0; i<12; i++){
    console.log(i);
    if (i===8) {
        console.log("Schleife abbrechen");
        break;
    }
}
```
In dem Beispiel zählt die Schleife nur bis 8, dann wird die break bedingung ausgeführt.

continue überspringt index Werte und führt die Schleife an einer anderen stelle wieder aus.
```js
for (let i = 0; i<12; i++){
    if (i===5 || i === 10){
        console.log(`${i} überspringen`);
        continue; // hier sagt continue:"ich bin fertig mit dem durchlauf", also bei index 5 und 10 wird die else Anweisung übersprungen.
    } else{
        console.log(`${i}`);
    }
}
```
### 5.6 while-Schleifen
Die while-Schleife braucht nur eine Bedingung:

```js
while (Bedingung) {
    Anweisungen;
}

let i = 0;
while (i<10){
    console.log(`${i} ist i.`);
    i++
}
```
Ohne die Schritte zählt die Schleife unendlich weiter und muss abgebrochen werden. Bei while-schleifen muss man *immer* sicherstellen, dass die Bedingung false wird.


Wenn die Anzahl der Durchläufe bekannt ist, wählt man for-Schleifen, wenn nicht, ist while besser geeignet.

#### while-Schleifen verschachtelt

let i = 0
while (i<=4){
    console.log(`i ist ${i}`);
    let j = 10;
    while (j>5){
        const result = i * j;
        console.log(`${i} * ${j} = ${result}`);
        j--;
    }
}

mit labels kann man aus Schleifen ausbrechen.
```js
labelName:
for (...) {
  ...
  break labelName;
}


```


####  Schleifen und logische Operatoren

In logischen Operatoren hat jeder Wert einen inhärenten Booleschen Wert, truthy oder falsy. es gibt auch nullish

```js
    if (i % fizzbuzz===0 && i !=0){
        console.log(`FizzBuzz! ${i} ist ein ganzzahliges Vielfaches von ${fizz} und ${buzz}`);


```
der ??-Operator ist der nullish Operator, er definiert null oder undefined.
```js
let n;
let foo;
n = foo ?? "default";
console.log("nullish", n); //log:nullish default
```
foo ist initialisiert aber undefined, daher falsy. ?? prüft ob eine Variable einen Wert hat, falls nicht, wird ein Standardwert eingesetzt.

### 5.9 Ternary Operator

unary, binary und ternary Operator
Unary (Einfache) Operatoren sind eine einstellige Verknüfung, also zb ! (Negation/not), -x (Vorzeichenänderung) xx++ (Inkrement)
Binary (zweifache) Operatoren: einer vor und einer nach dem operator: Addition a+b
Ternary (dreifache) Operatoren: Kurzform einer if / else abfrage. Beispiel:
t = alter < 16 ? "10 €":"50€"
der ternary operator kann als kurzform genutzt werden, wenn if/else zu komplex wird.
ternary operatoren weisen Variablen einen Wert abhängig von Bedingungen zu, hingegen if/else Abfragen ermöglichen die Entscheidung, welcher Code ausgeführt wird.
```js
const foo = (Bedingung) ? wenn true : wenn false;
```
Bedingung = 1. Operand
wenn true = 2. Operand
wenn false = 3. Operand
= Operator
? Operator
: Operator

Beispiel:
const begleitung = alter <=16 ? "begleitet" : "unbegleitet";

##### Ternary mit Mehreren Anweisungen

Ternary erlaubt mehrere anweisungen, diese werden in Runde Klammern geschrieben-

Kurzform: bedingung ? (a, b, c) : (d, e, f);

oder:

bedingung
  ? (anweisung1, anweisung2, anweisung3)
  : (alternative1, alternative2, alternative3);


const = radtour = {gefahren = 15; steigung = 3}
let anleitung;
radtour.gefahren > 10 ?(console.log("reicht")), (anleitung = "reicht"):(console.log("weiter")), (anleitung = "weiter, fahrt");

### 5.10 Übung


```js
const foo = (Bedingung) ? wenn true : wenn false;
```
const farbe = "grün";
let = style;
style = farbe === "grün" ? "color:green" : "color:red";


### 5.11 Implizite Typ-Konvertierungen in Abfragen

in if-abfragen setzen wir runde Klammern(), alles in diesen Klammern wird zu einem Boole#schen Wert umgewandelt, jeder string der nicht leer ist und jede zahl die nicht 0 ist wird zu true.
nur wenige werte werden zu false:

const x = false;
const val = 0;
const empty = ""; //oder const empty = ''
const nichts = null;
const unknown = undefined;
const notNum = NaN;

Einen leeren String nutzen wir um in einem Eingabeformular zu prüfen, ob etwas im eingabefeld vorhanden ist, oder obdas Feld leer ist.

Mit null prüfen wir, ob es ein angesprochenes HTML Element wirklich gibt, mit NaN ob eine Zahl eingegeben wurde.
