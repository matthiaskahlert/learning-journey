## Kompetenzprotokoll 2

Um Schwerpunkte und einen Fokus bei meinem Lernfortschritt zu setzen, wende ich das Prinzip des Kompetenzprotokolls an. Dies ist ein Teil der Prüfungsleistung in meiner Weiterbildung. Hierbei bearbeite ich das Gelernte wöchentlich in den vier Kategorien:
- Einordnen und Strukturieren: Theorie erklären
- Verstehen und Verknüpfen: Praxisbeispiel erklären
- Anwenden und Bewerten: Berufliche Relevanz erörtern
- Reflektieren und Hinterfragen: Lernprozess reflektieren oder offene
bzw. weiterführende Fragen formulieren

Zwei Themengebiete, welche mir derzeit als sehr relevant erscheinen sind Funktionen und Objekte.


### Einordnen und strukturieren (Theorie erklären)
 
    In der zweiten Weiterbildungswoche habe ich die Themengebiete Funktionen und Objekte als besonders interessant aber auch als herausfordernd empfunden. 
    Funktionen sind zentrale Bausteine jeder Programmiersprache und Objekte gehören zu den wichtigsten Konzepten in JavaScript, weil sie Daten und Verhalten gemeinsam abbilden können. 
    In JavaScript dienen sie dazu, Codeblöcke wiederverwendbar zu machen. Sie können Parameter entgegennehmen, Berechnungen durchführen und Ergebnisse zurückgeben. 
    Im Gegensatz zu einmalig geschriebenen Skripten ermöglichen Funktionen es, logische Abläufe gezielt einzusetzen. 
    Die erlernten Konzepte zu Parameterübergabe, Rückgabewerten und Scope (Gültigkeitsbereich) haben mir geholfen, besser zu verstehen, wie Daten zwischen verschiedenen Funktionsblöcken fließen. 
    Damit habe ich die Grundlagen verstanden, um Code systematisch zu strukturieren. Dieses Prinzip, ist sowohl in der Spieleentwicklung als auch im Testmanagement unverzichtbar.

#### Theorie von Objekten
    Sie bestehen aus sogenannten Schlüssel-Wert-Paaren, bei denen jeder Schlüssel (Property / Eigenschaft) einen bestimmten Wert (Value) enthält.  Mit Objekten lassen sich komplexe Zusammenhänge strukturiert darstellen: Objekte können auch Funktionen enthalten, man spricht dann von Methoden.
    Im Kontext der Spieleentwicklung können Objekte jegliche Entitäten repräsentieren, also Spielfiguren, Items, Buffs…, inklusive ihrer Eigenschaften wie Namen, Lebenspunkte oder Position und ihrer Methoden wie bewegen(), angreifen() oder Effekte über eine gewisse Zeit. 
    So lassen sich komplexe Zusammenhänge strukturiert darstellen. 
    Im Kontext der Spieleentwicklung können Objekte sogenannte Entitäten repräsentieren, also Spielfiguren, Items oder Buffs, inklusive ihrer Eigenschaften wie Name, Lebenspunkte oder Position und ihrer Methoden wie bewegen(), angreifen() oder Effekte über eine gewisse Zeit. 
    Im Testmanagement lassen sich Objekte hervorragend einsetzen, um Testfälle strukturiert zu modellieren, etwa mit Feldern wie summary, description, expectedResult, stepsToReproduce oder storyReference. 
    So kann man auch im Code Testdaten abbilden, anstatt sie in unübersichtlichen Tabellen zu pflegen. 
    Ich habe verstanden, dass Objekte eine Brücke zwischen Daten und logischer Verarbeitung bilden. 
    Sie machen den Code nicht nur übersichtlicher, sondern auch leichter zu erweitern, da neue Eigenschaften einfach hinzugefügt werden können, ohne die gesamte Struktur zu verändern. 
    Dies spart  Zeit und ermöglicht eine effektive Objekterstellung, was im beruflichen Kontext oft entscheidend ist.
    
### Verstehen und verknüpfen (Praxisbeispiel erklären)

    Man kann sich in der Praxis zum Beispiel ein Objekt für eine Spielfigur vorstellen:

    let player = {
      name: "Phoenix",
      health: 100,
      buff: {isActive : true, expirationDate: 2025.12.24 23:59:00, effect: DMG+=5}
      position: { x: 10, y: 20 },
      move: function(dx, dy) {
        this.position.x += dx;
        this.position.y += dy;
      }
    };
    
    Dieses Beispiel verdeutlicht, wie man in einem Objekt sowohl Daten (z. B. health, position) als auch Verhalten (z. B. move()) kombiniert. Über Methoden kann das Objekt eigenständig Zustände verändern. Das ist beispielsweise besonders in der Softwareentwicklung für Games wichtig-
    Ähnlich lässt sich dieses Konzept auf das Testmanagement übertragen:
    
    let testCase = {
      summary: "Login mit gültigen Daten",
      description: "Prüft den erfolgreichen Login",
      expectedResult: "Benutzer wird weitergeleitet",
      stepsToReproduce: ["Seite öffnen", "Daten eingeben", "Absenden"],
      storyRef: "JIRA-123"
    };
    
    Solche Strukturen helfen dabei, Testdaten programmatisch zu verarbeiten oder automatisch auszuwerten. 
    Durch den Einsatz von Objekten kann man Testfälle dynamisch erstellen, speichern oder analysieren, etwa im Rahmen von Testautomatisierungen. 
     Das verdeutlicht, dass sich das theoretische Konzept von Objekten direkt auf reale Arbeitsprozesse übertragen lässt.
    Wenn Testabläufe oder Auswertungen modular aufgebaut sind, kann man sie leichter pflegen, erweitern oder automatisieren. 
    Das ist ganz ähnlich wie in einem Spiel, in dem jedes Feature, Mechanik oder Entität in einem eigenen Container oder Funktion organisiert ist und somit leichter getestet oder verändert werden kann.

    
    
### Anwenden und bewerten (berufliche Relevanz erörtern)

    Das Wissen über Funktionen und Modularisierung ist für meine berufliche Zukunft sehr relevant. 
    Im Testmanagement kann ich Funktionen nutzen, um wiederkehrende Testschritte oder Prüfroutinen zu automatisieren. 
    So lassen sich zum Beispiel Validierungen für verschiedene Eingabetypen in einer zentralen Funktion abbilden und in mehreren Testfällen wiederverwenden. 
    Besonders wichtig finde ich, dass Funktionen auch eine Grundlage für testgetriebene Entwicklung (TDD) bilden.
    Jede Funktion kann isoliert getestet und verifiziert werden, bevor sie in den Gesamtkontext eingebunden wird. 
    Dieses Prinzip lässt sich direkt auf automatisierte Tests übertragen. Für meine zukünftige Arbeit bedeutet das, dass ich durch das Verständnis von Funktionslogik präzisere Testfälle formulieren und besser nachvollziehen kann, wie Code funktioniert. 
    Funktionen sind damit nicht nur ein technisches  Werkzeug, sondern ein methodischer Ansatz zur Qualitätssicherung und Fehlerprävention.
    Auch das Konzept der Objekte ist in meiner beruflichen Praxis von großer Bedeutung, da es hilft, sowohl Spielinhalte als auch Testdaten strukturiert abzubilden. 
    In der Spieleentwicklung kann ich über Objekte Spielfiguren, Inventare oder Gegner dynamisch steuern. Das ermöglicht mir, komplexe Zusammenhänge realitätsnah zu modellieren. 
    Im Testmanagement ist der Nutzen ähnlich groß. Testobjekte können alle relevanten Informationen eines Testfalls enthalten und automatisiert verarbeitet werden. 
    Diese könnten theoretisch an APIs übergeben oder über ein Testmanagementtool wie Testrail verwaltet werden und sind auch beim Erstellen von Reports nützlich. 
    Objektstrukturen lassen sich meines wissens direkt mit gängigen Testframeworks verknüpfen, zum Beispiel mit JSON-Strukturen in Postman oder Cypress. 
    Da ich solche Tools zukünftig sicher beherrschen möchte, bietet mir das Wissen über Objekte und Funktionen eine ideale Grundlage, um in die testgetriebene Entwicklung einzusteigen und meine Automatisierungsfähigkeiten auszubauen.

### Reflektieren und Hinterfragen

    Teilweise fällt es mir noch schwer, komplexe Abhängigkeiten zwischen Funktionen zu überblicken, insbesondere wenn Funktionen innerhalb anderer Funktionen aufgerufen werden oder verschiedene Datentypen gleichzeitig verwendet werden. 
    Hier möchte ich tiefer einsteigen, um zu verstehen, wie man solche Strukturen testbar und nachvollziehbar hält. 
    Ich möchte lernen, gezielt Funktionen zu schreiben, die ich anschließend selbst mit Testdaten prüfe.
    So kann ich in kleinen Schritten in Richtung testgetriebene Entwicklung vorankommen. 
     Außerdem interessiert mich perspektivisch, wie man Objekte in professionellen Testframeworks einsetzt werden können, beispielsweise wie ich sie in einer CI/CD Umgebung einbinden kann um nicht nur Lokal zu testen, sondern die Regressionstests zu automatisieren.. 
    Ein weiteres Lernziel ist, die Verbindung zwischen Objekten und JSON-Datenformaten zu vertiefen, da diese in der Testautomatisierung eine wichtige Rolle spielen. 
    Das DOM wurde bisher nur kurz angerissen, aber es war scxhon zu erkennen, dass das Zusammenspiel von JavaScript-Logik und DOM-Manipulation der Schlüssel ist, um Frontend-Tests gut strukturiert umzusetzen.
    Für die kommenden Tage nehme ich mir vor, regelmäßig kleine Codebeispiele zu entwickeln, um Funktionen und Objekte gezielt zu kombinieren. 
    Ich möchte meinen Lernprozess bewusst fortführen, um langfristig ein tieferes technisches Verständnis für automatisierte Tests, Spielelogik und testgetriebene Entwicklung zu erlangen.