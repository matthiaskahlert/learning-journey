1. Einordnen und Strukturieren (Theorie)

In dieser Phase meiner Weiterbildung liegt der Fokus auf dem Entwickeln und Testen von Benutzeroberflächen mit dem UI Framework Flutter. Anders als bei serverseitigem Code oder reiner Logik stellt UI-Testing besondere Anforderungen: Sichtbarkeit, Zustand und Nutzerinteraktion müssen gezielt simuliert werden. Aufbauend auf meinen bisherigen Erfahrungen mit testbarer Struktur habe ich mich hier besonders mit Widget-Tests und Integrationstests beschäftigt.

Bei Flutter unterscheidet man zwischen Unit-, Widget- und Integrationstests. Diese decken verschiedene Teile der App ab, von einzelnen Funktionen über UI-Komponenten bis hin zu kompletten Nutzerabläufen über mehrere Bildschirme. In dieser Phase lag der Fokus auf Widget- und Integrationstests.

Mit Widget-Tests kann man UI-Komponenten einzeln testen, ohne die ganze App zu starten. Man rendert ein Widget mit pumpWidget() und sucht dann gezielt mit sogenannten Findern nach Elementen. Wichtige Konzepte sind dabei find.text() oder find.byType() zum Auffinden von Elementen, tester.tap() für simulierte Interaktionen sowie tester.pump() oder pumpAndSettle(), um UI-Updates zu verarbeiten.

Nicht alle UI-Elemente sind sofort sichtbar, zum Beispiel bei Listen. Deshalb sind zusätzliche Interaktionen wie Scrollen (drag) notwendig. Bei komplexeren Widgets wie Listen, Dialogen oder responsiven Layouts entstehen weitere Anforderungen: Listen zeigen oft nur einen Teil der Inhalte, Dialoge müssen aktiv geöffnet und geschlossen werden und das Verhalten responsiver Layouts hängt von der Bildschirmgröße ab, die über MediaQuery gesteuert wird. Außerdem lassen sich in Widget-Tests externe Abhängigkeiten gezielt simulieren, beispielsweise indem man statt einer echten Datenquelle eine vorbereitete Testinstanz übergibt, die definierte Rückgabewerte liefert.

Integrationstests gehen einen Schritt weiter und prüfen komplette Abläufe, vom Start der App über Navigation und Nutzereingaben bis hin zur Validierung von Endzuständen. Sie laufen auf Emulatoren oder echten Geräten und bilden reale Nutzungsszenarien ab. Typischerweise startet man die App mit app.main(), simuliert UI-Interaktionen und überprüft die daraus entstehenden Zustandsänderungen. Darüber hinaus ermöglichen Integrationstests End-to-End-Validierung, Regressionstests und Performance-Messungen.

2. Verstehen und Verknüpfen (Praxisbeispiele)

Die beschriebenen Konzepte habe ich in meiner Abschlussaufgabe direkt angewendet: der Entwicklung einer Flutter-App für einen Lieferdienst. Da in einer echten Anwendung die Fahrzeugposition über ein Backend bereitgestellt wird, habe ich für diese Umsetzung eine Bewegungssimulation genutzt, um die Echtzeit-Aktualisierung darzustellen. Diese Simulation hat mir geholfen, realistische Testszenarien zu entwickeln, obwohl kein echtes Backend angebunden war.

Parallel dazu habe ich verschiedene Testarten kombiniert. Bei den Unit-Tests habe ich grundlegende Datenstrukturen wie Lieferoptionen überprüft, beispielsweise die Anzahl der Optionen, die korrekte Initialisierung von Werten, die Eindeutigkeit von IDs sowie die Gültigkeit von Preisen und Zeiten.

Der Schwerpunkt lag jedoch auf Widget-Tests. Hier habe ich zentrale UI-Komponenten überprüft, etwa ob alle Lieferoptionen korrekt angezeigt werden, ob die Navigation durch Tippen funktioniert, ob Inhalte kontextabhängig dargestellt werden und ob der „Jetzt bestellen“-Button das gewünschte Verhalten auslöst. Ein konkretes Beispiel war die Prüfung, ob beim Klick auf „Jetzt bestellen“ die korrekte Lieferoption übergeben wird. Dadurch konnte ich nicht nur die UI, sondern auch die zugrunde liegende Logik testen.

Auch verschiedene Zustände wie eine leere Bestellhistorie, korrekt formatierte Datumsanzeigen oder dynamisch geladene Listeninhalte konnte ich zuverlässig überprüfen. Dabei wurde mir deutlich, dass eine klare Struktur der Komponenten entscheidend für die Testbarkeit ist. Das Verhalten wird über Parameter und Callbacks gesteuert, während die Darstellung im Widget verbleibt. Dieses Prinzip knüpft direkt an meine bisherigen Erfahrungen an, bei denen ich begonnen habe, Logik von Ein- und Ausgabe zu trennen, um Tests zu erleichtern.

3. Anwenden und Bewerten (berufliche Relevanz)

Die in dieser Phase gelernten Konzepte sind sehr relevant für meine berufliche Entwicklung im Softwaretesting. Ich erkenne eine klare Verbindung zu klassischen Teststufen: Widget-Tests entsprechen funktionalen UI-Tests auf Komponentenebene, während Integrationstests End-to-End-Tests aus Nutzersicht abbilden.

Besonders wertvoll ist die Möglichkeit, reale Nutzerinteraktionen automatisiert zu testen. Dadurch lässt sich der Anteil manueller Tests reduzieren und gleichzeitig die Testabdeckung erhöhen. Ein zentraler Aspekt ist für mich die Erkenntnis, dass Testbarkeit stark vom Architektur- und UI-Design abhängt. Klare Zuständigkeiten, saubere Datenflüsse und gezielt eingesetzte Schlüssel (Key) sind entscheidend für eine effektive Testautomatisierung.

In der Praxis ergibt sich daraus eine wichtige Abwägung: Widget-Tests sind meist schneller, stabiler und einfacher zu pflegen, decken jedoch nur einzelne Komponenten ab. Integrationstests prüfen realistischere Abläufe, sind dafür aber deutlich aufwendiger und anfälliger. Tests müssen daher strategisch geplant und im Zusammenspiel betrachtet werden.

Auch Themen wie das Mocking von APIs in Widget-Tests, die Simulation von Gerätefunktionen oder Performance-Messungen in Integrationstests zeigen, wie nah diese Tests an realen Nutzungsszenarien sind. Für meine zukünftige Rolle im QA-Bereich bedeutet das ein vertieftes Verständnis für UI-Testautomatisierung, die Fähigkeit, Teststrategien über mehrere Ebenen hinweg zu entwickeln, sowie eine engere Zusammenarbeit zwischen Entwicklung und Testing.

4. Reflektieren und Hinterfragen (Weiterentwicklung)

Rückblickend sehe ich eine klare Entwicklung meines Lernprozesses: Anfangs ging es darum, dass Code überhaupt funktioniert, danach standen Stabilität und Fehlerbehandlung im Fokus, gefolgt von struktureller Testbarkeit. In dieser Phase liegt der Schwerpunkt nun auf dem Testen kompletter Nutzerinteraktionen.

Die Arbeit mit Flutter hat meine Sichtweise erweitert. Ich denke nicht mehr nur in Funktionen, sondern zunehmend in Nutzerabläufen. Ein wichtiger Aha-Moment war für mich die Kombination aus simulierten Daten und realistischen Testszenarien. Ich habe erkannt, dass sich auch ohne vollständige Systemlandschaft sinnvolle Tests entwickeln lassen.

Besonders interessant empfinde ich im Nachhinein die Veränderung meines Vorgehens: Während ich Testbarkeit früher oft erst nachträglich berücksichtigt habe, achte ich nun bereits während der Entwicklung darauf, wie sich Komponenten testen lassen. Konkret nutze ich bewusst Callbacks, um Verhalten gezielt überprüfen zu können.

Gleichzeitig habe ich festgestellt, dass UI-Tests komplexer und anfälliger sind als Unit-Tests, da bereits kleine Änderungen im Layout Auswirkungen auf Tests haben können. Daraus ergeben sich für mich mehrere weiterführende Fragen. In einem früheren Lernprotokoll habe ich die Testpyramide kennengelernt; nun frage ich mich, ob dieses Modell bei UI-lastigen Anwendungen wie Flutter weiterhin uneingeschränkt gilt oder ob Widget-Tests zumindest bei der Arbeit mit diesem UI Framework eine größere Rolle einnehmen. Außerdem interessiert mich, wie sich UI-Tests so gestalten lassen, dass sie langfristig stabil bleiben (z.B. durch Gruppierung der Tests in Klassen, so das man weniger Bereiche maintainen muss), und wie sich Teststrategien verändern, sobald ein echtes Backend integriert wird. Dabei stellt sich auch die Frage, wann Mock-Daten sinnvoll sind und wann Tests bewusst gegen reale Systeme laufen sollten.

Darüber hinaus beschäftigt mich, welche Tests automatisiert werden sollten und welche bewusst manuell bleiben, weil sie zu komplex oder wartungsintensiv sind. Derzeit schätze ich das so ein, das man oft laufende Regressionstests eher automatisieren möchte als Edgecases. Abschließend nehme ich mit, dass automatisiertes Testen für mich zunehmend ein integraler Bestandteil des Entwicklungsprozesses wird und nicht erst nachgelagert erfolgt.

