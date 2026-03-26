Kompetenzprotokoll 6 – Vom funktionierenden Code zur Teststrategie: Testpyramide, Testebenen und Architektur

    Einordnen und Strukturieren (Theorie)

In dieser Phase meiner Weiterbildung habe ich mich mehr darauf konzentriert, Softwaretests besser zu verstehen, statt nur Funktionen zu programmieren. Während ich mich in den vorherigen Protokollen mit Fehlerbehandlung, ersten automatisierten Tests und gut strukturiertem Code beschäftigt habe, geht es jetzt darum, wie man Tests systematisch plant und sinnvoll einsetzt.

In der professionellen Softwareentwicklung sieht man Testing nicht als einzelne Aufgabe, sondern als Teil der gesamten Entwicklungsstrategie. Ein wichtiges Konzept dabei ist die Testpyramide. Sie zeigt, wie verschiedene Testarten in welchem Verhältnis zueinander zusammenhängen und hilft, Tests ausgewogen zu gestalten.

Ganz unten in der Pyramide sind Unit-Tests. Die prüfen einzelne Funktionen oder Methoden für sich, ohne andere Teile. Sie laufen schnell, lassen sich leicht automatisieren und helfen, Fehlerzustände genau zu finden und einzugrenzen.

Darüber kommen Integrationstests. Die schauen, wie mehrere Komponenten zusammenarbeiten, zum Beispiel wie Daten zwischen Modulen fließen oder wie APIs funktionieren. Diese Tests sind aufwändiger als Unit-Tests, geben aber wichtige Infos über das Zusammenspiel der Teile.

Ganz oben sind End-to-End-Tests (E2E). Die simulieren, wie ein Nutzer das System wirklich benutzt und prüfen das ganze System. Dazu gehören API-Tests mit Tools wie Postman oder automatisierte Tests der Benutzeroberfläche. Diese Tests sind sehr aussagekräftig, aber auch komplexer in der Erstellung und Pflege.

Das Ziel der Testpyramide ist, dass die meisten Tests unten sind und nur wenige oben. So gibt es eine stabile Basis mit schnellen Rückmeldungen, auf der die anderen Tests sinnvoll aufbauen können. So können Risiken frühzeitig erkannt und reduziert werden.

Ein weiterer wichtiger Punkt ist, wie Testbarkeit und Softwarearchitektur zusammenhängen. Nur wenn Code modular ist und klare Aufgaben hat, lassen sich Teile gut einzeln testen. Wenn alles eng verbunden ist oder Logik direkt in der Benutzeroberfläche steckt, wird das viel schwieriger. Die objektorientierte Struktur in Java trägt dazu bei, dass Code häufig modular aufgebaut ist und sich dadurch besser testen lässt.

    Verstehen und Verknüpfen (Praxisbeispiele)

In meinen bisherigen Programmen habe ich verschiedene Testmethoden angewendet, ohne sie bewusst einer Struktur zuzuordnen. Rückblickend kann ich sie jetzt besser einordnen.

In meinem Kontaktverwaltungsprogramm und in der Prüfung zur Namensverwaltung habe ich Funktionen wie lade_daten() oder speichere_json() geschrieben, die unabhängig vom Menü arbeiten. Diese Trennung sorgt dafür, dass die Funktionen klare Eingaben und Ausgaben haben und sich gut einzeln testen lassen.

Meine bisherigen "Tests" waren oft manuelle Funktionsaufrufe im main-Block. Das half zwar, das Verhalten zu verstehen, ist aber eher exploratives Testen als eine reproduzierbare, automatisierte Lösung.

Mit Frameworks wie pytest für Python oder JUnit für Java habe ich angefangen, Tests besser zu strukturieren. Mit Assertions kann ich Erwartungen formulieren („Wenn Eingabe X, dann Ergebnis Y“) und automatisch prüfen lassen. So werden Tests zuverlässiger und nachvollziehbarer.

In meinem Java-Projekt mit REST-Schnittstellen bereite ich im Test eine In-Memory-Datenbank vor, setze Tabellen vor jedem Test zurück und prüfe dann das Verhalten der Endpunkte. Hier geht es nicht nur um einzelne Funktionen, sondern um das Zusammenspiel von Verarbeitung, Validierung und Datenhaltung.

Außerdem habe ich mit Postman erste Erfahrungen im API-Testing gesammelt. Diese Tests kommen der echten Nutzung schon sehr nahe, da sie echte HTTP-Anfragen simulieren. Gleichzeitig brauchen sie mehr Vorbereitung und Pflege als einfache Funktionstests.

Rückblickend sehe ich, dass meine Programme schon verschiedene Testebenen haben, die aber eher nebeneinander entstanden sind. Jetzt lerne ich, sie bewusst zu unterscheiden und gezielter einzusetzen.

    Anwenden und Bewerten (berufliche Relevanz)

Das Wissen über die verschiedenen Testebenen hilft mir, Tests bewusster zu planen und zu gewichten. Für meine Arbeit im Softwaretesting ist das ein wichtiger Schritt.

In der Praxis bedeutet das, dass ich darauf achten werde, Funktionen so zu gestalten, dass sie einzeln getestet werden können, Schnittstellen gezielt zu prüfen und nur wichtige Abläufe komplett durchzutesten. Dabei spielt auch das risikobasierte Testing eine Rolle: Wichtige Bereiche sollten gründlicher getestet werden als weniger kritische.

Eine wichtige Erkenntnis ist, dass nicht alles auf jeder Ebene getestet werden muss. Es geht darum, eine gute Balance zwischen Qualität und Aufwand zu finden.

Auch bei der Testautomatisierung wird das klarer. Schnell laufende Tests können regelmäßig oder bei jeder Änderung ausgeführt werden, während komplexere Tests gezielt eingesetzt werden. Mein aktueller Maven-Workflow im Java-Projekt zeigt mir, wie man Tests gut strukturiert und trennt.

Ich betrachte Code inzwischen nicht mehr nur danach, ob er funktioniert, sondern auch, wie gut er sich testen und erweitern lässt. Im Testmanagement wird klar, dass es nicht nur um einzelne Fehler geht, sondern um die ganze Qualitätssicherung.

    Reflektieren und Hinterfragen (Weiterentwicklung)

Rückblickend sehe ich, dass sich mein Lernen klar verändert hat. Am Anfang ging es mir nur darum, dass Programme funktionieren. Dann wurde Stabilität und Fehlerbehandlung wichtiger, danach Struktur und Wartbarkeit. Mit der Testpyramide und den Tools wie JUnit und Postman sehe ich Testing jetzt als ganzheitliches Konzept, das schon bei der Planung eine Rolle spielt.

Mir fällt auf, dass meine Tests meist einzelne Funktionen geprüft haben. Das Zusammenspiel von Komponenten habe ich oft nur indirekt getestet. Gerade bei Programmen mit Dateioperationen oder JSON-Speicherung sehe ich noch Chancen, bewusster zwischen isolierten und zusammengesetzten Tests zu unterscheiden.

Ich habe oft Tests erst nachträglich hinzugefügt. In Zukunft will ich ausprobieren, wie sich mein Vorgehen ändert, wenn ich Tests früher einbaue. Die Idee, Funktionen zuerst über ihr erwartetes Verhalten zu beschreiben und dann zu programmieren, finde ich besonders spannend.

Außerdem frage ich mich, wie tief Tests gehen sollten: Wann reicht ein Test, wann wird er zu kompliziert oder schwer zu pflegen? Bei größeren Szenarien überlege ich, wie man externe Abhängigkeiten sinnvoll einbeziehen oder ersetzen kann, ohne dass Tests instabil werden.

Ich frage mich auch, ob mein bisheriges Vorgehen eher technisch getrieben war, statt von einer klaren Struktur auszugehen. In künftigen Projekten will ich bewusster entscheiden, welche Tests ich einsetze, statt nur das zu machen, was gerade einfach ist.

Mich interessiert auch, wie sich meine Denkweise ändert, wenn ich Testing nicht als letzten Schritt sehe, sondern als festen Teil der Architektur. Langfristig will ich Code so schreiben, dass Testbarkeit von Anfang an mitgedacht wird.

Mein Ziel ist es, besser einzuschätzen, welche Tests wo den größten Nutzen bringen, und Programme so zu gestalten, dass sie nicht nur funktionieren, sondern auch langfristig verständlich und stabil bleiben.