# Kompetenzprotokoll 7 - Minitest in der Praxis: Teststruktur, Assertions und Testbarkeit durch Klassendesign

 

## 1. Einordnen und Strukturieren (Theorie)

 

In den letzten Kompetenzprotokollen habe ich mich viel mit automatisierten Tests in Python, Code-Modularisierung und der Testpyramide beschäftigt. Jetzt richte ich meinen Fokus darauf, wie man Unit-Tests in Ruby praktisch mit einem Test-Framework mit einem Testgetriebenen Entwicklungsansatz umsetzt. Dabei geht es nicht nur um das Framework selbst, sondern vor allem darum, wie Testbarkeit bereits beim Klassendesign entsteht und welche Strukturen dafür notwendig sind.
 
Minitest ist Rubys eingebautes Test-Framework (also eine Testsuite, die TDD and BDD approaches, mocking, und benchmarking ermöglicht) und seit der Ruby Version 1.9 Teil der Standardbibliothek (man muss es also nicht extra installieren). Die Idee dahinter ist einfach: Statt das Verhalten der Software nur manuell zu prüfen, schreibt man Tests, die das Verhalten automatisch überprüfen. Technisch legt man dafür eigene Testklassen an, die auf der Klasse Minitest::Test basieren. Durch diese Vererbung erkennt Ruby die Klasse als Test und stellt automatisch alle Funktionen bereit, die für das Ausführen und Auswerten der Tests notwendig sind. In diesen Klassen definiert man einzelne Testmethoden, die jeweils einen klaren Anwendungsfall prüfen.

Im Mittelpunkt stehen sogenannte Assertions. Diese geben eine klare Erwartung an den Code an, zum Beispiel, dass eine bestimmte Rückgabe entsteht oder eine Ausnahme ausgelöst wird. Eine typische Assertion ist assert_equal(expected, actual), bei der ein erwarteter Wert mit dem tatsächlichen Ergebnis verglichen wird. Wenn der Vergleich fehlschlägt, markiert der Test das automatisch als Fehler.

Ein weiterer wichtiger Punkt ist die Struktur eines Testlaufs. Vor jedem Test kann man einen Ausgangszustand herstellen (zum Beispiel mit der Methode setup), und nach dem Test wird dieser Zustand wieder bereinigt (teardown). So stellt man sicher, dass Tests unabhängig voneinander laufen und sich nicht gegenseitig beeinflussen.

Diese Unabhängigkeit ist ein Grundprinzip: Jeder Test muss für sich funktionieren und darf nicht davon abhängen, ob andere Tests vorher erfolgreich waren. Das führt zu einer klaren Denkweise: Statt Programme nur zum Laufen zu bringen, beschreibt man das Verhalten gezielt, prüft es und verbessert es Schritt für Schritt. Das ist der Kern von testgetriebener Entwicklung (TDD - Test Driven Developement): Erst den Test schreiben, dann die passende Umsetzung, und danach den Code verbessern, ohne das getestete Verhalten zu ändern.

 

## 2. Verstehen und Verknüpfen (Praxisbeispiel)

 

In meiner Ruby-Entwicklung sehe ich eine klare Entwicklung, die diese Theorie greifbar macht. In tdd_titleize_example.rb habe ich die String-Klasse um eine titleize-Methode erweitert und das Verhalten mit manuellen raise-Anweisungen geprüft, zum Beispiel raise 'Fail 1' unless 'this is a test'.titleize == 'This Is A Test'. Das funktioniert, ist aber kein echter automatisierter Test: Das Skript stoppt beim ersten Fehler und zeigt keine weiteren Ergebnisse.

In test_titleize.rb bin ich dann einen wichtigen Schritt weitergegangen. Ich habe eine Klasse TestTitleize erstellt, die von Minitest::Test erbt, und das Verhalten mit assert_equal beschrieben. Besonders interessant ist, dass ich absichtlich eine Assertion eingebaut habe, die fehlschlagen muss - assert_equal("Let's Make A Test Fail!", 'FooBar'.titleize). Das ist kein Fehler, sondern zeigt den roten Zustand im Red-Green-Zyklus: Wenn der Testrunner absichtlich scheitert, zeigt das, dass das Testsystem richtig funktioniert.

Ein weiteres Beispiel ist meine GeometricShape-Klasse aus Übung 6.C.01. Dort wirft die Basisklasse bei area einen NotImplementedError. Mit assert_raises(NotImplementedError) { GeometricShape.new(4).area } kann ich dieses Verhalten genau und reproduzierbar testen - eine Assertion, die ich früher nicht systematisch genutzt habe.

 

## 3. Anwenden und Bewerten (berufliche Relevanz)

 

Das Wissen über Minitest und strukturierte Unit-Tests hilft mir direkt in meinem Berufsziel im Softwaretesting und Testmanagement. Als angehende Fachkraft ist es wichtig zu wissen, wie Entwickler ihre Codeeinheiten testen. So kann ich bessere Anforderungen formulieren und Teststrategien mitgestalten.

Ein wichtiger Punkt ist, dass Testbarkeit nicht einfach später hinzugefügt wird, sondern schon durch das Klassendesign entsteht. Zum Beispiel ist das attr_reader :radius in meiner Circle-Klasse aus der Teilprüfung nicht nur praktisch, sondern nötig, damit ich eine Assertion wie assert_equal(3, circle.radius) schreiben kann. Andererseits zeigt die Klassenvariable @@count in derselben Klasse eine typische Testfalle: Sie sammelt Werte über alle Tests hinweg, wenn kein setup den Zustand zurücksetzt. Das kann zu falschen Ergebnissen führen - ein Problem, das ich schon aus Python kenne.

Das Verständnis vom Framework hilft mir auch, Rubys Minitest mit Pytest in Python und JUnit in Java zu vergleichen. Sie verfolgen alle die gleiche Grundidee, unterscheiden sich aber in Syntax und Umfang. Dieses Wissen ist im Testmanagement wertvoll, weil ich in Teams mit verschiedenen Technologien arbeiten und eine gemeinsame Sprache sprechen muss.

 

## 4. Reflektieren und Hinterfragen

 

Rückblickend sehe ich, dass der Wechsel von manuellen raise-Anweisungen zu Minitest mehr als ein technischer Schritt ist - es ist ein grundlegender Wandel in meiner Denkweise. Während ich in tdd_titleize_example.rb noch Schritt für Schritt gearbeitet habe („wenn etwas schiefgeht, stoppt das Programm“), denke ich mit Minitest mehr in klaren Szenarien. Ich formuliere Erwartungen bewusster und prüfe gezielt einzelne Verhaltensaspekte statt nur das Gesamtergebnis.

Ich habe aber auch gemerkt, dass mir dieser Perspektivwechsel nicht sofort leichtgefallen ist. Anfangs wollte ich vor allem, dass der Code funktioniert. Erst durch das bewusste Schreiben von Tests habe ich angefangen, mir vor der Umsetzung klarer zu überlegen, was genau passieren soll und wie ich das testen kann. Das fühlt sich aktuell noch ungewohnt an, zeigt mir aber deutlich, wie eng Testen und gutes Design miteinander verbunden sind.

Besonders deutlich wird das bei meinen bisherigen Ruby-Klassen. Die Circle-Klasse aus der Teilprüfung habe ich viel mit puts-Ausgaben überprüft. Erst später verstand ich, dass solche Ausgaben zwar beim Entwickeln helfen, aber keine echten Tests sind. Methoden wie attr_reader sind für mich jetzt nicht nur praktisch, sondern schaffen gezielt Zugriff, um Verhalten überhaupt testen zu können.

Gleichzeitig stoße ich noch an Grenzen meines Verständnisses. Ich kann einzelne Tests schreiben, bin aber unsicher, wie ich größere Teststrukturen sinnvoll aufbaue, wann ein Test ausreichend isoliert ist und ab wann er selbst zu komplex und schwer zu pflegen wird. Weiterführend frage ich mich, wie RSpec (RSpec ist ein Behavior-Driven Development (BDD) Framework für Ruby) sich im Alltag von Minitest unterscheidet und wann sich der Wechsel lohnt, wie man Testabdeckung mit Werkzeugen wie SimpleCov objektiv messen kann und wie externe Abhängigkeiten wie Datei-I/O durch Mocks ersetzt werden, um echte Testisolation zu erreichen. Diese Fragen zeigen mir, dass ich gerade an einem Übergang stehe: vom ersten Anwenden einzelner Tests zu einem tieferen Verständnis von Teststrategie und Testdesign. Diesen nächsten Schritt will ich in den kommenden Wochen bewusst weiterverfolgen.