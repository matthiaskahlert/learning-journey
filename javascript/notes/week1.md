# Meine Markdown notes Woche 1
## Tag 1
## Inhalt
JavaScript benötigt HTML und CSS kentnisse um den Einstieg zu erleichtern, denn es geht bei JavaScript hauptsächlich um das Eingreifen in die Darstellung von websites.
Daher sollte das HTML sicherheitshalber vom Validator geprüft werden.

## Todo Liste
    Todo:      
                - [ ] Wöchentliches Kompetenzprotokoll vorbereiten
                    - [x]   Themengebiete eingrenzen
                    - [ ]   Vier Kategoriengebiete beschreiben und Kernfragen beantworten    -                  [ ] schlage MArkup Validation Service nach.
               - [ ]  Frage beantworten, warum ich JavaScript nutzen will, zb Serverkommunikation für Testing, Design und Layout von Webseiten oder Animation und Effekte.
               - [x] nachschlagen was das defer-Attribut ist. 
               - [ ] VS code erweiterungen installieren https://lms.velptec.de/mod/velptecpdfinstruct/view.php?id=93727
                    - [x]   live server
                    - [ ]   Material Icon Theme
                    - [ ]    TODO highlight
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
Die aufgabe erschien einfach, aber durch das einbinden der separaten .js Datei kam es sozusagen zu einem Laufzeitfehler, welchen ich mit dem defer attribut beheben konnte. Anfangs hatte ich fehlerhafterweise auch noch den scr typ "module" zugewiesen, welcher den console output blockierte. das entfernen des modules führte zur lösung. ich habe mich für eine constante bei dem Namen entschieden, und für eine let variable beim alter.

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
    Am ersten Kurstag habe ich besonders die Nutzung der Browser-Konsole und die Live-Server Extension in Visual Studio Code als interessant empfunden. Die Browser-Konsole ist ein zentrales tool um die Änderungen meiner JavaScript-Dateien direkt im Browser auszuführen und Fehler zu identifizieren. Man kann über Anweisungen im JavaScript codr oder direkt in der Konsole arbeiten um Variablen, funktioneen oder Brechnungen zu überprüfen. Damit ist es mir möglich Änderungen "on the fly" zu testen und sofort die Auswirkungen von Änderungen zu bepbachten. Die Live-Server-Extension von VSCode unterstützt dies, indem sie html Dateien automatisch neu lädt, sobald ich die Änderungen speichere. So kann ich ohne refresh den direkten impact sehen. Das zentrale Prinzip hier sind schnelle feedback zyklen und direkte Sichtbarkeit von Änderungen.
## Verstehen und verknüpfen (Praxisbeispiel erklären)
    Ein konkretes Beispiel aus meiner bisherigen Erfahrung ist das testen kleiner JavaScript Funktionen direkt in der Browser Konsole. Ich konnte einfache berechnungen direkt auf Korrektheit überprüfen, indem ich die Konsole nutzte. Die Live-Server Extension hat durch die direkte automatische aktualisierung mein Verständnis vertieft, wie sich meine Änderungen auf meine Seite auswirkten. Dies war bei der Fehlersuche der Übungsaufgabe sehr wertvoll, da es meine Lernkurve beschleunigt hat.
## Anwenden und bewerten (berufliche Relevanz erörtern)
    Für meine berufliche Praxis im Testmanagement und dem Softwaretesting sehe ich de Nutzen der Browser-Konsole und der Live-Server Extension direkt im schnellen Überprüfen von JavaScript Funktionen und HTML elementen. Dies ermöglicht eine frühe Fehlererkennung und spart Zeit und Aufwand im späteren Verlauf der Softwareentwicklung.Dies erleichtert die Qualitätssicherung, aber zeigt auch die relevanz für Softwareentwickler, um ein Verständnis der Funktionsweise von Code zu gewinnen. Dies erleichtert auch die Kommunikation mit Entwicklern, wenn es um Fehlerbeschreibungen geht.
## Reflektieren und Hinterfragen
     Rückblickend auf den ersten Kurstag habe ich erkannt, dass es mit der Browser-Konsole und der Live-Server Extension Wertvolle Hilfsmittel gibt, die den Lernprozess unterstützen und die Fehlersuche vereinfachen. Folgefragen: welche erweiterten Funktionen erleichtern komplexere debugging scenarien? Welche Konfigurationsmöglichkeiten habe icch beim Live-Server speziell bei größeren projekten? Mich interessiert auch, wie diese Tools in Testgetriebene Entwicklungsprozesse integriert werden können, um dies als bestPractise mitzunehmen. Mir hat die Nutzung den direkten Zusammenhang zwischen der Theorie der der Code-Logik und der visuellen Umsetzung verständlicher gemacht. Weitere Vertiefung erkenne ich als notwendig an.
