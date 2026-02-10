Kompetenzprotokoll 4 – Automatisierte Tests und Fehlerbehandlung in Python

Dieses Kompetenzprotokoll dokumentiert meine Lernfortschritte der achten Weiterbildungswoche. Der inhaltliche Schwerpunkt liegt auf automatisierten Tests sowie auf robuster Fehlerbehandlung in Python. Dabei habe ich mich insbesondere mit try-except-Blöcken, der with-Anweisung zur sicheren Ressourcenverwaltung und der testbaren Strukturierung von Funktionen beschäftigt.

Ein Teil der in diesem Protokoll beschriebenen Erkenntnisse ist durch eigenständige Vertiefung entstanden. Da das Thema automatisierte Tests im bisherigen Weiterbildungsverlauf nur kurz angerissen wurde, war es für mich wichtig, mich darüber hinaus intensiver mit diesem Bereich zu befassen, um meinen fachlichen Fokus im Softwaretesting weiterzuentwickeln.

1. Einordnen und Strukturieren (Theorie)
Fehlerbehandlung mit try-except

In Python werden Fehler nicht ignoriert, sondern über sogenannte Exceptions behandelt. Mithilfe von try-except-Blöcken können kritische Codeabschnitte abgesichert werden, sodass ein Programm auch bei unerwarteten Situationen nicht abstürzt. Besonders relevant ist dies beim Zugriff auf externe Ressourcen wie Dateien.

Python ermöglicht eine gezielte Fehlerbehandlung durch spezifische Exception-Typen wie FileNotFoundError, json.JSONDecodeError oder IOError. Dadurch lassen sich unterschiedliche Fehlerszenarien differenziert behandeln und verständliche Rückmeldungen erzeugen. Diese Art der Fehlerbehandlung trägt wesentlich zur Stabilität und Wartbarkeit von Software bei.

Ressourcenverwaltung mit der with-Anweisung

Die with-Anweisung stellt sicher, dass Ressourcen wie Dateien korrekt geschlossen werden, selbst wenn während der Verarbeitung ein Fehler auftritt. Der sogenannte Kontextmanager übernimmt dabei automatisch das Öffnen und Schließen der Ressource.

Gerade im Zusammenspiel mit Fehlerbehandlung verhindert dieses Konzept typische Probleme wie noch geöffnete Dateien oder gesperrte Ressourcen. Für produktionsnahe Anwendungen ist dies vermutlich ein weiterer Baustein für robustere Softwareentwicklung.

Testbarer Code mit if __name__ == "__main__"

Der if __name__ == "__main__"-Block sorgt dafür, dass bestimmter Code (und zwar der in der folgenden if-Bedingung) nur beim direkten Ausführen eines Skripts ausgeführt wird, nicht jedoch beim Import als Modul. Diese Struktur eignet sich besonders gut, um einfache automatisierte Testläufe von der eigentlichen Programmlogik zu trennen.

Aus meiner aktuellen Perspektive zeigt mir dieser Ansatz, wie sich Test-Code und Produktiv-Code klar voneinander abgrenzen lassen. Er bildet - so verstehe und vermute ich es derzeit - eine konzeptionelle Grundlage für testgetriebene Entwicklung und den späteren Einsatz professioneller Testframeworks.

2. Verstehen und Verknüpfen (Praxisbeispiele)
Praxisbeispiel: Kontaktverwaltung mit Duplikatprüfung

Im Programm zur Kontaktverwaltung (8.7.C.01.py) habe ich eine Funktion implementiert, die Kontakte in einer JSON-Datei speichert und dabei auf Duplikate prüft. Beim Laden der bestehenden Daten werden mögliche Fehler wie eine fehlende oder beschädigte Datei abgefangen. Ist dies der Fall, wird mit einer leeren Datenstruktur weitergearbeitet.

Vor dem Speichern neuer Kontakte erfolgt eine Validierung auf Basis der E-Mail-Adresse, um doppelte Einträge zu vermeiden. Zusätzlich wird auch der Schreibvorgang selbst abgesichert, sodass das Programm selbst bei Fehlern stabil weiterläuft.

Dieses Beispiel verdeutlicht für mich das Zusammenspiel von Fehlerbehandlung, Validierung der Daten und Test der Funktionsstruktur. Durch definierte Testdaten im __main__ Block konnte ich die Funktionalität reproduzierbar überprüfen, ohne manuelle Eingaben vornehmen zu müssen.

Praxisbeispiel: Namensverwaltung mit optionalem Testmodus

In der Teilprüfung 03 (mkahlert_teilpruefung_03.py) habe ich ein Programm entwickelt, das Namen aus einer Textdatei einliest, diese verarbeitet und optional als JSON speichert. Zusätzlich zur geforderten Aufgabe habe ich einen konfigurierbaren Testmodus eingebunden. Dieser ermöglicht es, die Kernfunktionen sequenziell auszuführen, ohne das interaktive Menü zu starten.

Dabei habe ich unter anderem auf korrekte Zeichenkodierung (utf-8) geachtet, um auch Umlaute zuverlässig zu verarbeiten. Die Trennung von Programmlogik und Benutzerinteraktion hat mir deutlich gemacht, wie wichtig diese modulare Struktur für automatisierte Tests ist. Die Funktionen lassen sich dadurch unabhängig vom Nutzungskontext prüfen und die Testabdeckung lässt sich bis auf den gewünschten Grad erweitern. 

3. Anwenden und Bewerten (berufliche Relevanz)

Die behandelten Konzepte sind für meine zukünftige Tätigkeit im Softwaretesting und Testmanagement von zentraler Bedeutung. Fehlerbehandlung ist ein wesentliches Qualitätsmerkmal von Software und beeinflusst sowohl Stabilität als auch Benutzerfreundlichkeit.

Durch meine eigenen Implementierungen habe ich ein besseres Verständnis dafür entwickelt,
an welchen Stellen Fehlerbehandlung notwendig ist (z. B. Datei-I/O, Nutzereingaben),
welche Fehlertypen sinnvoll abgefangen werden sollten,
und wie verständliche Fehlermeldungen zur Qualitätssicherung beitragen.

Auch einfache automatisierte Testruns steigern die Effizienz erheblich. Bei der Erstellung von Testszenarien musste ich mich bewusst mit den gewünschten Anforderungen auseinandersetzen um auch die semantische Funktionsweise prüfen zu können. Sie ermöglichen reproduzierbare Testszenarien, erleichtern (und verringern manuelle) Regressionstests und dokumentieren das erwartete Verhalten einer Anwendung direkt im Code.

Die von mir verwendete Struktur lässt sich perspektivisch auf CI/CD-Umgebungen übertragen. Tests könnten dort automatisiert bei jedem Commit ausgeführt werden, um fehlerhafte Änderungen frühzeitig zu erkennen. Darüber hinaus habe ich durch die Arbeit mit JSON ein Datenformat genutzt, das in der Testautomatisierung weit verbreitet ist, etwa im API-Testing oder beim Umgang mit Konfigurations- und Testdaten.

4. Reflektieren und Hinterfragen (Weiterentwicklung)

Die achte Weiterbildungswoche hat mir deutlich gemacht, dass automatisierte Tests weniger ein einzelnes Werkzeug als vielmehr eine grundlegende Denkweise sind. Beim Schreiben meiner Programme habe ich begonnen, Code bewusster zu strukturieren und bereits während der Implementierung über Testbarkeit nachzudenken.

Gleichzeitig ist mir bewusst geworden, dass meine bisherigen Tests noch einfach gehalten sind und vor allem auf Konsolenausgaben basieren und mit echten Dateien arbeiten. 
Es wird klar, dass in professionellen Testumgebungen häufig sogenanntes Mocking eingesetzt wird, um externe Abhängigkeiten zu simulieren und Tests unabhängig vom Dateisystem zu machen. Mocking bedeutet, reale Systembestandteile (z. B. Datenbanken oder APIs) durch kontrollierte Ersatzobjekte (Testdatenbanken, Test-APIs, fake-Antworten...) zu ersetzen, die das Verhalten des Produktivsystems nachahmen.

Diese Tests brauchen auch sogenannte Assertions („Wenn Eingabe X erfolgt, erwarte ich Ergebnis Y.“), also Annahmen, die automatisch und eindeutig zwischen Erfolg und Fehler unterscheiden. Eine Assertion ist also eine Anweisung, mit der ein erwartetes Ergebnis automatisch überprüft wird. Mir ist aufgefallen, dass Entwicklungsumgebungen zahlreiche weiterführende Assertion-Varianten anbieten. Aktuell möchte ich mich in Zukunft erst einmal bewusst auf einfache Assertions konzentrieren, um das Grundprinzip sicher zu verstehen. 

Auch ohne explizite Nutzung von Testframeworks habe ich begonnen, Tests mit definierten Ausgangszuständen durchzuführen. Rückblickend entspricht dieses Vorgehen dem Konzept von Fixtures, die einen reproduzierbaren Startzustand für Tests sicherstellen.

Daraus ergeben sich für mich mehrere weiterführende Fragen:

- Wie unterscheiden sich Unit-, Integrations-Tests und End-to-End-Tests in Projekten meiner aktuellen Größenordnung, und wann ist welche Testebene sinnvoll?
- Wie lassen sich externe Abhängigkeiten wie Dateien oder APIs mithilfe von Mocking und Fixtures testen, ohne reale Ressourcen zu verwenden?
- Wie integriere ich automatisierte Tests mit Frameworks wie PyTest in eine CI/CD-Pipeline?
- Welche Prinzipien helfen dabei, Code von vornherein testbarer zu gestalten?

Rückblickend fand ich die Implementierung von Fehlerbehandlung und Ressourcenmanagement herausfordernd aber wichtig. Gleichzeitig sehe ich Entwicklungsbedarf bei Testabdeckung, Testorganisation und dem Einsatz von Assertions. In den kommenden Wochen würde ich gerne einmal neben den geplanten Weiterbildungsinhalten gezielt PyTest ausprobieren und mich mit der strukturierten Organisation von Tests beschäftigen.

Ziel ist es, meine bisherigen Ansätze weiter zu professionalisieren und vielleicht sogar fundiertes Feedback zu erhalten, ob meine Herangehensweise im Bereich automatisierter Tests fachlich in die richtige Richtung geht. Motivierend dabei ist es, die gelernten Begriffe mit meiner eigenen beruflichen Erfahrung abzugleichen und Konzepte zu erkennen, die ich bereits intuitiv genutzt habe.