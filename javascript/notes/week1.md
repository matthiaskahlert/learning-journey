# Meine Markdown notes Woche 1
## Tag 1
## Inhalt
JavaScript benötigt HTML und CSS kentnisse um den Einstieg zu erleichtern, denn es geht bei JavaScript hauptsächlich um das Eingreifen in die Darstellung von websites.
Daher sollte das HTML sicherheitshalber vom Validator geprüft werden.

## Todo Liste
    Todo:      
- [x] Wöchentliches Kompetenzprotokoll vorbereiten
    - [x] Protokoll - Themengebiete eingrenzen
    - [x] Protokoll - Vier Kategoriengebiete beschreiben und Kernfragen beantworten
    - [x] Protokoll abschicken zur Bewertung
- [x] Schlage Markup Validation Service nach - (Ausprobiert https://validator.w3.org/#validate_by_input)
- [x]  Frage beantworten, warum ich JavaScript nutzen will, zb Serverkommunikation für Testing, Design und Layout von Webseiten oder Animation und Effekte. (Serverkommunikation sollte für mich der Fokus sein)
- [x] nachschlagen was das defer-Attribut ist (habe auch async gelernt und defer angewendet beim einbinden einer separaten .js datei
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
    - [ ] 

## Learningfacts Kapitel 1 - HTML und CSS
- Cascading ist das Einfließen von Stilen aus vorangegangenen CSS Regeln.
- Bei der Kommunikation mit dem Server via JavaScript geht es um das Einlesen und Weiterreichen von Benutzereingaben, hier reichen solide Grundlagen für CSS.
- Man kann JavaScript Anweisungen direkt in die HTML Datei schreiben oder in eigene Dateien mit der Endung .js. Diese separaten .js Dateien kann man mit einem HTML script-Tag direkt in die HTML Datei einbinden. Beispiel: <script src="script.js" defer></script>
- Es gibt Module die man im und exportieren kann. Module organisieren Script Dateien, indem sie anwendungen in überschaubare Teile herunterbrechen und sie in separaten Dateien speichern. Diese Fragmente werden als Module importiert. Das type-Attribut des script Elements kennzeichnet JavaScript Dateien als Module.
- Da browser html Dateien Zeile für Zeile laden, aber bei externen css dateien den Inhalt komplett laden, kann es zu Latenzen kommen. Dies wird mit "just-in-time-loading" verhindert, dafür nutzt man die Attribute: defer und async. Mit defer lädt der Browser scripte erst vollständig (in derReihenfolge in der sie im code erscheinen), bevor er sie ausführt. Scripte mit async  werden ohne beachtung der Reihenfolge ausgeführt.
- Für JavaScript Entwicklung ist in den Browsern die Bworserkonsole der Dreh- und Angelpunkt, z.B. in Chrome via F12 -> console. Man kann über anweisungen im JavaScript code oder direkt in der Browserkonsole arbeiten um beispielsweise Variablen und Objekte zu testen und Ihre Struktur aufzuzeigen. Die Konsolenausgabe im Script erfolgt über console.log(var1, var2, vae3...); Beispielsweise braucht man nur den namen einer Variable um den Variablenwert zu sehen. Beispiel const mwst = x * mwstSatz / 119;
        console.log(mwst);
## Learningfacts Kapitel 2 - Variablen und Syntax
- JavaScript nutzt zur Deklaration (Bekanntmachung) von Variablen drei Schlüsselwörter: var, let und const.
- Variablennamen sollten mit einem Kleinbuchstaben, einem unterstrich oder einem Dollarzeichen beginnen. Sie sind Case-sensitive: X ist eine andere Variable als x. Viele nutzen sogenanntes camelCase, wobei die Variable klein beginnt, jedes neue Wort aber groß weitergeht. Beispiel: let alterVater, alterMutter, alterKind;
- Variablen haben gültigkeitsbereiche (scope) und gelten nur in dem Block, in dem sie deklariert wurden.
- Die Syntax ist die grammattik der Programmiersprache. Es gibt 
- Operatoren (zb boolsche, oder Mathematische wie AND, OR, NOT, +, - =)wobei das Gleichheitszeichen ein Zuweisungsoperator ist. Beispiel: 
        const breite = 200;
        const höhe = 125;
        let fläche = breite * höhe;
- Ausdruck (Expression), was eine Kombination aus Variablen, Oertatoren und Werten darstellt
        let fläche = breite * höhe;
- Semikolon - Regel, nicht hinter schließenden geschweiften Klammern, nur hinter Anweisungen.
- Schlüsselwörter (Keywords) beispielsweise let und const
- Kommentare (Comments) alles auf einer Zeile nach // sowie zwischen /* ... */ ist ein Kommentar und wird nicht ausgeführt bzw vom Browser ignoriert.
- Namen (Identifier) - ein Identifier ist ein Name den ich benutze um etwas zu benennen. Beeispiel: Variablen (let name = "Matze";) - hier ist Variablen der Identifier, name die Variable und Matze der Wert, der der Variablen zugeordnet ist. Die Variable kann über den identifier angesprochen werden. Identifier müssen mit Buchstaben einem Dollarzeichen uoder einem Unterstrich beginnen. das erste Zeichen darf keine Zoffer sein, bindestriche sind nicht erlaubt (wird als Minus interpretiert).
- Hochkommas - Sie sind für String genutzt, entweder soppeltes oder einfaches Hochkomma. 
## Übungsaufgabe 2.2.Ü.01
Die Aufgabe erschien mir einfach, aber durch das einbinden der separaten .js Datei kam es sozusagen zu einem Laufzeitfehler, welchen ich mit dem defer attribut beheben konnte. Anfangs hatte ich fehlerhafterweise auch noch den scr typ "module" zugewiesen, welcher den console output blockierte. das entfernen des modules führte zur lösung. ich habe mich für eine constante bei dem Namen entschieden, und für eine let variable beim alter.

## Kompetenzprotokoll
Um Schwerpunkte und einen Fokus bei meinem Lernfortschritt zu setzen, wende ich das Prizip des Kompetenzprotokolls an. Dies ist ein Teil der Prüfungsleistung in meiner Weiterbildung. Hierbei bearbeite ich das Gelernte wöchentlich in den vier Kategorien:
- Einordnen und Strukturieren: Theorie erklären
- Verstehen und Verknüpfen: Praxisbeispiel erklären
- Anwenden und Bewerten: Berufliche Relevanz erörtern
- Reflektieren und Hinterfragen: Lernprozess reflektieren oder offene
bzw. weiterführende Fragen formulieren

Zwei Themengebiete, welche mir derzeit als sehr relevant erscheinen ist die Browser-Konsole und die Liveserver extension bei Visual Studio Code.

Die Browser-Konsole ist Teil der Entwicklungswerkzeuge für die Webentwicklung und auf allen Haupt Browsern verfügbar. In Kombination mit dem Liveserver sehr hilfreich.
 ## Einordnen und strukturieren (Theorie erklären)
    Am ersten Kurstag habe ich besonders die Nutzung der Browser-Konsole und die Live-Server Extension in Visual Studio Code als interessant empfunden. 
    Die Browser-Konsole ist ein zentrales tool um die Änderungen meiner JavaScript-Dateien direkt im Browser auszuführen und Fehler zu identifizieren. 
    Man kann über Anweisungen im JavaScript codr oder direkt in der Konsole arbeiten um Variablen, funktioneen oder Brechnungen zu überprüfen. 
    Damit ist es mir möglich Änderungen "on the fly" zu testen und sofort die Auswirkungen von Änderungen zu bepbachten. 
    Die Live-Server-Extension von VSCode unterstützt dies, indem sie html Dateien automatisch neu lädt, sobald ich die Änderungen speichere. 
    So kann ich ohne refresh den direkten impact sehen. Das zentrale Prinzip hier sind schnelle feedback zyklen und direkte Sichtbarkeit von Änderungen.
## Verstehen und verknüpfen (Praxisbeispiel erklären)
    Ein konkretes Beispiel aus meiner bisherigen Erfahrung ist das testen kleiner JavaScript Funktionen direkt in der Browser Konsole. 
    Ich konnte einfache berechnungen direkt auf Korrektheit überprüfen, indem ich die Konsole nutzte. 
    Die Live-Server Extension hat durch die direkte automatische aktualisierung mein Verständnis vertieft, wie sich meine Änderungen auf meine Seite auswirkten. 
    Dies war bei der Fehlersuche der Übungsaufgabe sehr wertvoll, da es meine Lernkurve beschleunigt hat.
    So konnte ich die entsprechenden Fehlermeldungen wie die geworfenen Exceptiones direkt in der Browser-Konsole sehen was wiederum zu einem Umdenken und ausprobieren führte. 
    Schließlich führten meine Bemühungen dann auch zum Erfolg einer akzeptablen Umsetzung der Übungsaufgabe.
## Anwenden und bewerten (berufliche Relevanz erörtern)
    Für meine berufliche Praxis im Testmanagement und dem Softwaretesting sehe ich de Nutzen der Browser-Konsole und der Live-Server Extension direkt im schnellen Überprüfen von JavaScript Funktionen und HTML elementen.
    Dies ermöglicht eine frühe Fehlererkennung und spart Zeit und Aufwand im späteren Verlauf der Softwareentwicklung.Dies erleichtert die Qualitätssicherung, aber zeigt auch die relevanz für Softwareentwickler, um ein Verständnis der Funktionsweise von Code zu gewinnen. 
    Dies erleichtert auch die Kommunikation mit Entwicklern, wenn es um Fehlerbeschreibungen geht.
    Nicht zuletzt die Eingangs erwähnten kurzen feedback-Zyklen verkürzen die Entwicklungszeit und ermöglichen auch das schnelle validieren von Bugfixes.
## Reflektieren und Hinterfragen
     Rückblickend auf den ersten Kurstag habe ich erkannt, dass es mit der Browser-Konsole und der Live-Server Extension Wertvolle Hilfsmittel gibt, die den Lernprozess unterstützen und die Fehlersuche vereinfachen. 
    Folgefragen: 
     - Welche erweiterten Funktionen erleichtern komplexere debugging scenarien? 
     - Welche Konfigurationsmöglichkeiten habe icch beim Live-Server speziell bei größeren projekten? 
     - Mich interessiert auch, wie diese Tools in Testgetriebene Entwicklungsprozesse integriert werden können, um dies als bestPractise mitzunehmen. 
     Mir hat die Nutzung den direkten Zusammenhang zwischen der Theorie der der Code-Logik und der visuellen Umsetzung verständlicher gemacht. Weitere Vertiefung erkenne ich als notwendig an.

## Was ich morgen lernen will?
Mehr insights über Datentypen in JavaScript,also Typecasts / Datentyp-Konvertierungen sicher beherrschen.
## Learningfacts Kapitel 3 - Grundlegende Datentypen
    - 3.1 Es gibt folgende Datentypen:
        - Number (Integer oder Float)
        - Strings
        - Boolean
        - Null (leer, absichtliche abwesenheit eines Wertes)
        - Undefined (Variable der noch kein Wert zugewiesen wurde)
        - BigInt (Zshlrn zu groß für Number)
            Beispiel: Zum erzeugen ein n an die Integerzahl anhängen oder BigInt() aufrufen: let big = 123456789123n; 
        - Symbol (unveränderlicher Wert, z.B. um eindeutige Eigenschaften zu definieren)
    - 3.2 
        - Integer und Float
        In JavaScript sind Int und Float vom Typ Number.
        Zahlen werden im 64-bit Gleitkommaformat gespeichert.
        Wenn man ein int und ein float addiert, entstehen minimale fehler bei der Konvertierung der Zahlen. Dies führt zu ungenauigkeiten bei der darstellung von Brüchen. Es handelt sich also um Annäherungen an den nicht exakt zu treffenden Wert.
        - Nngative Zahlen, unendlich und NaN kennt JavaScript auch. unendlich wird mit dem Schlüsselwort Infinity definiert. NaN (Not a Number) entsteht wenn der code zu einer ungültigen Zahl führt, beispielsweise wenn man versucht, zwei Variablen mit dem Wert 0 durch null zu teilen, allerdings gilt es zu beachten, dass die Browserkonsole keinen Fehler ausgibt.
    - 3.3
        - Boolsche Werte
        true und false beziehungsweise 1 und 0 sind die unterste Ebene. Variablen vom Typ Boolean können nur einen Wert annehmen: true oder false, dies wird genutzt bei if/else Abfragen und Schleifen wie while oder "switch" anweisungen.
        Boole#sche Operatoren sind && (logisches AND), || (logisches OR), und ! (logisches NOT).
        - a&&b true wenn beide Operanden true sind
        - x||y true wenn mindestens einer der beiden Operanden true ist
        - !c gibt das Gegenteil des Wahrheitswertes von c zurück
    - 3.4 Strings - Zeichenketten
        - Alles in Hochkommas ist ein String!
        - Erlaubte Hochkommas sind 
            Backtick                ``
            einfaches Hochkomma     ''
            doppeltes Hochkomma     ""
            Anführungszeichen und apostrophe sind nicht erlaubt. Strings können zusammengeführt werden mit +, dies nennt man Konkatenation was in diesem Fall eine Verknüpfung der Stringss darstellt.
            const str1 = 'Schnee'
            const str2 = 'ball'
            let ergebnis = str1 + str2
            console.log("Ergebnis ist", ergebnis)
            Strings in Hochkomma dürfen keinen Zeilenumbruch haben, mit Backticks geht es allerdings. Innerhalb von Backticks dürfen auch variablen stehen!
                Variablen in Strings stehen in geschweiften Klammern {} und ihnen geht ein $ Zeichen voran:
                const q = 129
                const w = 23
                const mwst = `Im Betrag ${q + q * w / 100} € sind ${q*w /100} € MwSt. enthalten`;
                console.log(mwst);
        - typeof kann den Datentyp hinterfragen: console.log(mwst, typeof mwst); gibt den Wert von mwst und string als output in die Konsole.
        - Variablen, die ohne Wert mit let deklariert sind, wird der Wert undefined zugewiesen.
        - null wird zugewiesen, wenn man anzeigen möchte, dass kein Wert zugewiesen wurde. Es gibt einen Wert empty, den man herausfinden kann, indem man die Länge des Strings oder eines arrays prüft.
            const schrank = [];
            if (schrank.length >0) {
                ("Elemente Ausgeben");
            }   else {
                console.log("Nichts im Schrank!");
            } //Konsolen Log: Nichts im Schrank! die array.length Funktion prüft die länge des arrays
    3.6 Datentyp Konvertierungen
        JavaScript verzichtet auf einen expliziten Datentyp bei der deklaration von Variablen. vorteil ist: Geschwindigkeit, Nachteil: Bei Problemen ist die Fehlersuche schwierig.
        Die Konvertierung eines String in einen Number Datentyp ist notwendig bei der Erfassung von Usereingaben auf Webseiten in einem Formularfeld, da die Werte als Strings ankommen. 
        - Es gibt die funktion parseInt() um diese Datentypumwandlung vorzunehmen. Es wird alles bis zum ersten nicht numerischen zeichen geparst. 
        - mit parseFloat() wird der Dezimalpunkt berücksichtigt.
        - eine weitere Konvertierung ist Number(), diese Methode akzeptiert Ziffern, den Dezimalpunkt und auch vorzeichen wie - und + gibt allerdings NaN zurück, wenn ein anderes Zeichen im String ist.
        Unary Operator oder Plus-Operator ist auch eine option:
        let u = "24.56";
        let uni = +u;
        console.log("Unary", uni, typeof uni);
        NaN wird gebraucht wenn sichergestellt werden muss, das für Operationen ein zahlenwert vorliegt. 
        Mit der funktion isNAN() wird geprüft ob der Variable ein Zahlenwert zugrunde liegt.
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
        JavaScript wandelt automatisch Werte von einem Datentyp in einen anderen um, dies kann aber Fallstricke mit sich führen (Thema Konkatenation also Verknüpfung von Strings Beispiel:
            const result1 = "10"
            const result2 = 5
            result3 = result1 + result2
            console.log(result3); //log:"105"
        console.log(0 == "0"); log:true // hier wandelt JavaScript automatisch um
        console.log(0 === "0"); log: false //bei === keine umwandkung, typen sind verschieden (Zahl und String)

        