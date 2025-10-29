# Meine Markdown notes Woche 1
## Tag 1
## Inhalt
JavaScript benötigt HTML und CSS Kenntnisse um den Einstieg zu erleichtern, denn es geht bei JavaScript hauptsächlich um das Eingreifen in die Darstellung von Websites.
Daher sollte das HTML sicherheitshalber vom Validator geprüft werden.

## Todo Liste
    Todo:      
- [x] Wöchentliches Kompetenzprotokoll vorbereiten
    - [x] Protokoll - Themengebiete eingrenzen
    - [x] Protokoll - Vier Kategoriengebiete beschreiben und Kernfragen beantworten
    - [x] Protokoll abschicken zur Bewertung
- [x] Schlage Markup Validation Service nach - (Ausprobiert https://validator.w3.org/#validate_by_input)
- [x]  Frage beantworten, warum ich JavaScript nutzen will, zb Serverkommunikation für Testing, Design und Layout von Webseiten oder Animation und Effekte. Serverkommunikation sollte für mich der Fokus sein.
- [x] nachschlagen was das defer-Attribut ist (habe auch async gelernt und defer angewendet beim einbinden einer separaten .js datei)
- [ ] VS code erweiterungen installieren https://lms.velptec.de/mod/velptecpdfinstruct/view.php?id=93727
    - [x]   live server
    - [ ]   Material Icon Theme
    - [ ]  TODO highlight
    - [ ]    Auto rename Tag
    - [ ]    Für Kotlin: Kotlin IDE for Visual Studio Code
    - [ ]    Für Python3: Python extension for Visual Studio Code
    - [ ]    Für Java: Extension Pack for Java
    - [ ]    Erweiterungen für Webentwicklung
    - [ ]    Babel JavaScript
    - [ ]    Dependency Analytics
    - [ ]    ES7+ React/Redux/React-Native snip
    - [ ]    ESLint
    - [ ]    Jest
    - [ ]    JSON
    - [ ]    Node Essentials
    - [ ]    Path Intellisense
    - [ ] Switch Anweisung lernen
    - [ ] Verstehen wie der querySelector funktioniert

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
        let fläche = breite * höhe;
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
 ## Einordnen und strukturieren (Theorie erklären)
    Am ersten Kurstag habe ich besonders die Nutzung der Browser-Konsole und die Live-Server Extension in Visual Studio Code als interessant empfunden. 
    Die Browser-Konsole ist ein zentrales Tool um die Änderungen meiner JavaScript-Dateien direkt im Browser auszuführen und Fehler zu identifizieren. 
    Man kann über Anweisungen im JavaScript Code oder direkt in der Konsole arbeiten um Variablen, Funktionen oder Berechnungen zu überprüfen. 
    Damit ist es mir möglich Änderungen "on the fly" zu testen und sofort die Auswirkungen von Änderungen zu beobachten. 
    Die Live-Server-Extension von VSCode unterstützt dies, indem sie HTML Dateien automatisch neu lädt, sobald ich die Änderungen speichere. 
    So kann ich ohne refresh den direkten impact sehen. Das zentrale Prinzip hier sind schnelle Feedback-Zyklen und direkte Sichtbarkeit von Änderungen.
## Verstehen und verknüpfen (Praxisbeispiel erklären)
    Ein konkretes Beispiel aus meiner bisherigen Erfahrung ist das testen kleiner JavaScript Funktionen direkt in der Browser Konsole. 
    Ich konnte einfache Berechnungen direkt auf Korrektheit überprüfen, indem ich die Konsole nutzte. 
    Die Live-Server Extension hat durch die direkte automatische Aktualisierung mein Verständnis vertieft, wie sich meine Änderungen auf meine Seite auswirkten. 
    Dies war bei der Fehlersuche der Übungsaufgabe sehr wertvoll, da es meine Lernkurve beschleunigt hat.
    So konnte ich die entsprechenden Fehlermeldungen wie die geworfenen Exceptions direkt in der Browser-Konsole sehen was wiederum zu einem Umdenken und ausprobieren führte. 
    Schließlich führten meine Bemühungen dann auch zum Erfolg einer akzeptablen Umsetzung der Übungsaufgabe.
## Anwenden und bewerten (berufliche Relevanz erörtern)
    Für meine berufliche Praxis im Testmanagement und dem Softwaretesting sehe ich den Nutzen der Browser-Konsole und der Live-Server Extension direkt im schnellen Überprüfen von JavaScript Funktionen und HTML Elementen.
    Dies ermöglicht eine frühe Fehlererkennung und spart Zeit und Aufwand im späteren Verlauf der Softwareentwicklung.Dies erleichtert die Qualitätssicherung, aber zeigt auch die Relevanz für Softwareentwickler, um ein Verständnis der Funktionsweise von Code zu gewinnen. 
    Dies erleichtert auch die Kommunikation mit Entwicklern, wenn es um Fehlerbeschreibungen geht.
    Nicht zuletzt die Eingangs erwähnten kurzen Feedback-Zyklen verkürzen die Entwicklungszeit und ermöglichen auch das schnelle validieren von Bugfixes.
## Reflektieren und Hinterfragen
     Rückblickend auf den ersten Kurstag habe ich erkannt, dass es mit der Browser-Konsole und der Live-Server Extension Wertvolle Hilfsmittel gibt, die den Lernprozess unterstützen und die Fehlersuche zu vereinfachen. 
    Folgefragen: 
     - Welche erweiterten Funktionen erleichtern komplexere Debugging-Szenarien? 
     - Welche Konfigurationsmöglichkeiten habe icch beim Live-Server speziell bei größeren Projekten? 
     - Mich interessiert auch, wie diese Tools in Testgetriebene Entwicklungsprozesse integriert werden können, um dies als Best-Practice mitzunehmen. 
     Mir hat die Nutzung den direkten Zusammenhang zwischen der Theorie der Code-Logik und der visuellen Umsetzung verständlicher gemacht. Weitere Vertiefung erkenne ich als notwendig an.

## Was ich morgen lernen will?
Mehr insights über Datentypen in JavaScript, also Typecasts / Datentyp-Konvertierungen sicher beherrschen.

## Tag2

## Learningfacts Kapitel 3 - Grundlegende Datentypen
    - 3.1 Es gibt folgende Datentypen:
        - Number (Integer oder Float)
        - Strings
        - Boolean
        - Null (leer, absichtliche Abwesenheit eines Wertes)
        - Undefined (Variable der noch kein Wert zugewiesen wurde)
        - BigInt (Zahlen zu groß für Number)
            Beispiel: Zum erzeugen ein n an die Integerzahl anhängen oder BigInt() aufrufen: let big = 123456789123n; 
        - Symbol (unveränderlicher Wert, z.B. um eindeutige Eigenschaften zu definieren)
    - 3.2 
        - Integer und Float
        In JavaScript sind Int und Float vom Typ Number.
        Zahlen werden im 64-bit Gleitkommaformat gespeichert.
        Wenn man ein int und ein float addiert, entstehen minimale Fehler bei der Konvertierung der Zahlen. Dies führt zu Ungenauigkeiten bei der Darstellung von Brüchen. Es handelt sich also um Annäherungen an den nicht exakt zu treffenden Wert.
        - Negative Zahlen, unendlich und NaN kennt JavaScript auch. Unendlich wird mit dem Schlüsselwort Infinity definiert. NaN (Not a Number) entsteht wenn der Code zu einer ungültigen Zahl führt, beispielsweise wenn man versucht, zwei Variablen mit dem Wert 0 durch null zu teilen, allerdings gilt es zu beachten, dass die Browserkonsole keinen Fehler ausgibt.
    - 3.3
        - Boolsche Werte
        true und false beziehungsweise 1 und 0 sind die unterste Ebene. Variablen vom Typ Boolean können nur einen Wert annehmen: true oder false, dies wird genutzt bei if/else Abfragen und Schleifen wie while oder "switch" Anweisungen.
        Boolesche Operatoren sind && (logisches AND), || (logisches OR), und ! (logisches NOT).
        - a&&b true wenn beide Operanden true sind
        - x||y true wenn mindestens einer der beiden Operanden true ist
        - !c gibt das Gegenteil des Wahrheitswertes von c zurück
    - 3.4 Strings - Zeichenketten
        - Alles in Hochkommas ist ein String!
        - Erlaubte Hochkommas sind 
            Backtick                ``
            einfaches Hochkomma     ''
            doppeltes Hochkomma     ""
            Anführungszeichen und Apostrophe sind nicht erlaubt. Strings können zusammengeführt werden mit +, dies nennt man Konkatenation was in diesem Fall eine Verknüpfung der Strings darstellt.
            const str1 = 'Schnee'
            const str2 = 'ball'
            let ergebnis = str1 + str2
            console.log("Ergebnis ist", ergebnis)
            Strings in Hochkomma dürfen keinen Zeilenumbruch haben, mit Backticks geht es allerdings. Innerhalb von Backticks dürfen auch Variablen stehen!
                Variablen in Strings stehen in geschweiften Klammern {} und ihnen geht ein $ Zeichen voran:
                const q = 129
                const w = 23
                const mwst = `Im Betrag ${q + q * w / 100} € sind ${q*w /100} € MwSt. enthalten`;
                console.log(mwst);
        - typeof kann den Datentyp hinterfragen: console.log(mwst, typeof mwst); gibt den Wert von mwst und string als output in die Konsole.
        - Variablen, die ohne Wert mit let deklariert sind, wird der Wert undefined zugewiesen.
        - null wird zugewiesen, wenn man anzeigen möchte, dass kein Wert zugewiesen wurde. Es gibt einen Wert empty, den man herausfinden kann, indem man die Länge des Strings oder eines Arrays prüft.
            const schrank = [];
            if (schrank.length >0) {
                ("Elemente Ausgeben");
            }   else {
                console.log("Nichts im Schrank!");
            } //Konsolen Log: Nichts im Schrank! die array.length Funktion prüft die Länge des Arrays
    3.6 Datentyp Konvertierungen
        JavaScript verzichtet auf einen expliziten Datentyp bei der Deklaration von Variablen. Vorteil ist: Geschwindigkeit, Nachteil: Bei Problemen ist die Fehlersuche schwierig.
        Die Konvertierung eines String in einen Number Datentyp ist notwendig bei der Erfassung von Usereingaben auf Webseiten in einem Formularfeld, da die Werte als Strings ankommen. 
        - Es gibt die Funktion parseInt() um diese Datentypumwandlung vorzunehmen. Es wird alles bis zum ersten nicht numerischen Zeichen geparst. 
        - mit parseFloat() wird der Dezimalpunkt berücksichtigt.
        - eine weitere Konvertierung ist Number(), diese Methode akzeptiert Ziffern, den Dezimalpunkt und auch Vorzeichen wie - und + gibt allerdings NaN zurück, wenn ein anderes Zeichen im String ist.
        Unary Operator oder Plus-Operator ist auch eine Option:
        let u = "24.56";
        let uni = +u;
        console.log("Unary", uni, typeof uni);
        NaN wird gebraucht wenn sichergestellt werden muss, das für Operationen ein Zahlenwert vorliegt. 
        Mit der Funktion isNaN() wird geprüft ob der Variable ein Zahlenwert zugrunde liegt.
        - Number zu String
        Die Funktion .toString() wandelt einen Variablenwert in einen String um.
        let h = 12345;
            result = h.toString();
            console.log("h wurde umgewandelt", result, typeof result ); //log: h wurde umgewandelt 12345 string
        In der Klammer kann auch ein Parameter stehen, wenn es sich vorher um eine Number gehandelt hat, man kann dann die Zahlenbasis angeben.
        - Number zu Boolean
        Nur 0 liefert false, alles andere liefert den Wert true nach Datentypkonvertierung. Beispiel:
            const bnum = 256;
            const bumw = Boolean(bnum);
            console.log("Boolean´sche Umwandlung bumw ist gleich:", bumw, typeof bumw);
        - String zu Boolean
        nur ein leerer String führt zu false
        - implizite Datentypumwandlung
        JavaScript wandelt automatisch Werte von einem Datentyp in einen anderen um, dies kann aber Fallstricke mit sich führen (Thema Konkatenation) also Verknüpfung von Strings Beispiel:
            const result1 = "10"
            const result2 = 5
            result3 = result1 + result2
            console.log(result3); //log:"105"
        console.log(0 == "0"); log:true // hier wandelt JavaScript automatisch um
        console.log(0 === "0"); log: false //bei === keine umwandkung, typen sind verschieden (Zahl und String)

## Was ich morgen lernen will?
Mehr insights über zusammengesetzte Datentypen in JavaScript, also Objekte wie das DOM.

## Tag 3
## Learningfacts Kapitel 4 - zusammengesetzte Datentypen
Komplexe Datentypen nennt man Objekte, sie können mehr als eine Komponente speichern. So kann ein Objekt beispielsweise einen String, Number und einen Booleanwert enthalten. Objekte erkennt man an den geschweiften Klammern:
const kurs = { 
    title:      "Stricken für Anfänger",
    coach:      "Julia",
    places:     12,
    started:    true,
    location:   "Hamburg",
}
Das Objekt kurs hat auch Informationen wie title und places, welche man als Eigenschaften bezeichnet, englisch properties. Von außen spricht man das Objekt folgendermaßen an:
kurs.places ist eine Eigenschaft des Objekts und stellt einen besonderen Typ einer Variablen dar. So kann man sie auch ändern:
kurs.places = 14;
kurs.title = "Stricken für Anfänger - Teil II";
...
- Das wichtigste Objekt ist das DOM (Document Object Model), es ist die Schnittstelle zum HTML-Dokument. Objekte haben Eigenschaften, und Methoden für die einfachen Datentypen Strings, Number, Boolean.

-Math Object
Es gibt globale Objekte, die man nicht erzeugen muss, um sie zu nutzen, man kann sie direkt einsetzen, wie das Objekt Math.
Gibt man in der Browserkonsole "Math." ein, werden einem die verschiedenen Komponenten von Math angezeigt.
Die mathematischen Konstanten werden mit dem Math Objekt entsprechend genutzt wie: 
Math.PI, 
Math.SQRT1_2 (Quadratwurzel von 1/2),
Math.LN10 (Logarithmus Naturalis zur Basis 10)
Die Konstanten werden in Großbuchstaben geschrieben.
Andere Methoden nicht:
Math.cos()
Math.trunc() (gibt den Wert vor dem Komma zurück, entfernt Nachkommastellen)
Math.floor() rundet ab, bei negativen Zahlen also Math.floor(-2.7) -> ergibt -3
Math.random() (erzeugt einen Random-Wert zwischen 0 und 1)
Math.max() (gibt die größte von null oder mehr Zahlen wieder)
Math.min() (gibt die kleinste von null oder mehr Zahlen wieder)

- Operanden und Operatoren
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

const num = 23
if (num % 2 === 0) {
    console.log(`${num} ist eine gerade Zahl`)
} else {
    console.log(`${num} ist eine ungerade Zahl`)
} //23 ist eine ungerade Zahl


- Zuweisungen
Das Gleichheitszeichen ist auch ein Operator, es weist der Variablen auf der linken Seite einen Wert zu.

Zuweisen                    =
Addieren und zuweisen       +=
Subtrahieren und zuweisen   -=
Dividieren und zuweisen     /=
Multiplizieren und zuweisen *=
Exponent und zuweisen       **=
Modulo und zuweisen         %=

- Vergleichsoperatoren
hat denselben Wert      ==
strenges gleich         ===
ungleich                !=
strenges ungleich       !==
größer als              >
kleiner als             <
größer oder gleich      >=
kleiner oder gleich     <=

- String Länge - string length
Ein String hat eine Länge, dies ist eine Eigenschaft.
Eigenschaften werden (wie bei Objekten) mit einem Punkt vor dem Variablennamen geschrieben.
const str1 = "Matthias Kahlert"
const stringLänge = str1.length;
console.log(` Der String ${str1} hat die Stringlänge von ${stringLänge}.`);

const a1 = str1[0]; //JavaScript erreicht jedes Zeichen im String mit einem index aus eckigen Klammern. es Beginnt bei 0 zu zählen. 
console.log(`Das 1. Zeichen des Strings ist ${a1}.`);

Ein String hat Eigenschaften wie: Unterteilen, Suchen und Ersetzen.
In der Browserkonsole kann man mit console.log("String", str1.__proto__); alle Möglichkeiten der String Eigenschaften sehen.
Die wichtigsten für uns sind 
- replace()
- indexOf() - gibt den ersten gefundenen index des Zeichens des strings zurück. es hilft, sich den string als Array vorzustellen. Jedes Zeichen des Strings hat eine Indexnummer, beginnend mit der 0.
- search()
- split()
- includes() - gibt true zurück, wenn die gesuchte Zeichenfolge im String enthalten ist.
    beispiel:
    const randomQuote = "Aller Anfang ist schwer!";
    console.log(randomQuote.includes("Anfang"));
- string.substring(start,end) - start für das erste Zeichen end für das letzte. mit nur einem argument gibt substring() den Teilstring von start bis ende zurück.
- string.replace()
- string.replaceAll()
- string.toLowerCase()
- string.toUpperCase()
Die Methode string.charAt() gibt das Zeichen des Strings an einem Index zurück. 
 der string.charCodeAt() gibt den Unicode Wert zurück (In UTF-16)
 string.match durchducht einen string nach einer zeichenkette und gibt den ersten treffer zurück
 - string.slice() extrahiert einen Teil aus dem String mit start (inklusive) und end (exklusive)Argumenten. string.slice kann auch vom ende her zählen also mit negativen Werten als string.slice(-5) gibt es die letzten fünf Zeichen des Strings aus.
 string.localeCompare() vergleicht zwei Strings unter Einbeziehung der Sprache miteinander und gibt einen numerischen Wert zurück. Es gibt drei Argumente:

1. Zeichenkette die verglichen wird
2. Länderkürzel (Weglassen, denn Browser default genutzt werden soll)
3. sensitivity, optional, default ist nicht case sensitiv. es geht u-kf-upper und u-kf-lower, sowie u-kn-true (für die sortierung von zahlen)
- string.split() teilt einen string bei jedem vorkommen eines Zeichens oder Teilstrings und speichert die Teile in einem Array. Dies kann nützlich sein beim trennen einer CSV.
- string.trim() entfernt "Weißraum" also Leerzeichen, Tabstops, Zeilenumbrüche am Anfang und am Ende eines Strings. Dies kann wichtig sein, wenn man daten aus Eingabefeldern von Formularen übernimmt!
- es gibt auch string.trimLeft() und string.trimRight() wenn man nur an einer Seite die Leerzeichen entfernen möchte.

- 4.10 Reguläre Ausdrücke
Reguläre Ausdrücke werden z.B. genutzt um Benutzereingaben zu prüfen, sie können verhindern, dass z.B. HTML Tags in Eingabefelder geschrieben werden, bzw. diese ignoriert werden. Man spricht von Regex (Regular Expressions)
    - Metazeichen und Suchmuster
    Reguläre Ausdrücke enthalten ein Suchmuster aus Metazeichen für irreguläre Zeichenfolgen. Das Metazeichen für Zahlen ist Beispielsweise \d oder [0-9]. Ein Suchmuster für fünf Zahlen wäre dem zur Folge \d5 oder [0-9]{5}
    es gibt weitere Platzhalter:
        - \w Buchstabe, Ziffer oder Unterstrich
        - \W ein Sonderzeichen
        - \d eine Ziffer zwischen 0-9
        - \D ein Zeichen, dass keine Ziffer ist
        - \s ein Weißraum
        - \S Jedes Zeichen ausser Weißraum
        - \b Wortgrenze
        - \B keine Wortgrenze
    Metazeichen wie ^und $ suchen am anfang bzw am Ende eines Strings
        - . findet alle Zeichen außer Zeilenende
        - ^ Anfang eines Strings
        - $ Ende eines Strings
        - | Alternativen
        - () Teile des Suchmusters abgrenzen
        - [] Zeichenklassen
        - {} Replikatoren
    Zeichenklassen
        - [xyz] beliebiger Buchstabe x, y oder z
        - [^xyz] jeder buchstabe außer xyz
        - [0-9] Ziffern 0-9
        - [a-z] jeder Kleinbuchstabe von a-z
        - [A-Za-z0-9] alle Buchstaben und Ziffern
        - [a-zß-ü] alle Kleinbuchstaben und Umlaute
    Replikatoren
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

