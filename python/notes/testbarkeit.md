Exkurs: Testbarkeit und persönliche Lernerfolge
Vertiefende Reflexion zu Kompetenzprotokoll 4

Dieses Dokument ist eine persönliche Vertiefung meiner Lernerfolge zum Thema automatisierte Tests und Testbarkeit. Es ergänzt mein viertes Kompetenzprotokoll und dient als Nachschlagewerk für meine weitere Entwicklung.
Zielsetzung dieses Exkurses

Während mein Kompetenzprotokoll 4 die formalen Anforderungen der Weiterbildung erfüllt, möchte ich in diesem Exkurs tiefer in meine praktischen Lernerfolge eintauchen. Dabei reflektiere ich:

    Welche konkreten Erkenntnisse ich beim Programmieren gewonnen habe
    Wo ich Verbindungen zu professionellem Testing erkenne
    Welche Best Practices ich bereits intuitiv angewendet habe
    Was ich noch vertiefen möchte

1. Meine praktischen Lernerfolge
Was ich konkret umgesetzt habe

Systematische Fehlerbehandlung in beiden Projekten:

In 8.7.C.01.py (Kontaktverwaltung) habe ich gelernt, dass Fehlerbehandlung nicht nur "try-except" schreiben bedeutet, sondern ein systematisches Konzept ist:
Python

# Mein Ansatz: Mehrschichtige Fehlerbehandlung
```py
try:
    with open(DATEINAME, 'r') as stream:
        kontakte = json.load(stream)
except (FileNotFoundError, json.JSONDecodeError):
    kontakte = []  # Fallback-Strategie
```
Was ich dabei gelernt habe:

    Verschiedene Exception-Typen können gleichzeitig abgefangen werden
    Ein sinnvoller Fallback (leere Liste) macht das Programm robuster
    Die Kombination von with und try-except ist Best Practice

Validierung vor dem Speichern:

Meine Duplikatprüfung war nicht Teil der Aufgabenstellung, aber ich habe sie hinzugefügt, weil ich an Datenintegrität gedacht habe:
Python

# Duplikatprüfung basierend auf E-Mail
```py
for kontakt in kontakte:
    if kontakt.get("E-Mail") == email:
        print(f"Kontakt mit der E-Mail {email} existiert bereits.")
        return  # Frühes Abbrechen verhindert inkonsistente Daten
```
Erkenntnis: Das frühe return verhindert, dass inkonsistente Daten gespeichert werden. Das ist ein Defensive Programming Ansatz, den ich bisher nur unbewusst genutzt habe.
Automatisierte Testläufe: Mein erster Kontakt mit Test Automation

In beiden Projekten habe ich einen if __name__ == "__main__"-Block genutzt, um Funktionen automatisch zu testen:

In 8.7.C.01.py:
Python
```py
if __name__ == "__main__":
    print("=== AUTOMATISCHE TESTS ===\n")
    
    # Test 1: Einzelne Kontakte speichern
    speichere_kontakt("Anna", "anna@mail.de", "+49151 12 34 567")
    speichere_kontakt("Bernd", "bernd@mail.de", "+49151 23 45 678")
    
    # Test 2: Mehrere Kontakte aus Liste
    daten = [
        ('Max', 'max@mail.de', '+49161 12 34 567'),
        ('Erika', 'erika@mail.de', '+49161 23 45 678'),
    ]
    for i in daten:
        speichere_kontakt(i[0], i[1], i[2])
    
    # Test 3: Anzeige validieren
    zeige_kontakte()
```
In mkahlert_teilpruefung_03.py:
Python
```py
TESTS_AKTIV = False  # Toggle für Testmodus

if TESTS_AKTIV:
    test_namen = lade_daten()
    zeige_namen(test_namen)
    speichere_json(test_namen)
```
Was ich dabei gelernt habe:

    Reproduzierbarkeit: Durch definierte Testdaten kann ich die Funktionen beliebig oft mit denselben Eingaben testen
    Automatisierung: Ich muss nicht mehr manuell Daten eingeben
    Regressionstests: Wenn ich Code ändere, kann ich schnell prüfen, ob alles noch funktioniert
    Dokumentation: Die Testdaten zeigen, wie die Funktionen benutzt werden sollen

Aha-Moment: Ich habe gemerkt, dass mein TESTS_AKTIV-Flag dem entspricht, was in CI/CD-Systemen über Umgebungsvariablen gesteuert wird. Professionell würde man schreiben:
Python
```py
import os
TESTS_AKTIV = os.getenv("RUN_TESTS", "false").lower() == "true"
```
2. Verbindungen zu professionellem Testing

Modularität als Grundlage für Testbarkeit:

Beide Programme haben kleine, fokussierte Funktionen:

    speichere_kontakt() macht nur das Speichern
    lade_kontakte() macht nur das Laden
    zeige_kontakte() macht nur die Anzeige

Warum das wichtig ist:
In der professionellen Softwareentwicklung nennt man das Single Responsibility Principle (SRP). Jede Funktion hat genau eine Aufgabe. Das macht sie:

    Leichter testbar (ich muss nur eine Sache prüfen)
    Leichter wartbar (Änderungen betreffen nur eine Stelle)
    Wiederverwendbar (ich kann die Funktion in anderen Kontexten nutzen)

Trennung von Logik und UI:

Meine Funktionen arbeiten unabhängig vom interaktiven Menü:
Python
```py
# Logik (testbar)
def lade_daten():
    # ... Daten laden
    return daten

# UI (nicht testbar, aber getrennt)
def hauptmenü():
    namen_liste = lade_daten()  # Nutzt die testbare Funktion
    # ... Menü-Logik
```
Erkenntnis: Diese Trennung ermöglicht es mir, die Logik zu testen, ohne das Menü zu starten. Das ist Dependency Inversion – ein wichtiges Prinzip für testbaren Code.
Was ich noch verbessern kann: Der Weg zu echten Unit-Tests

Aktueller Stand:
Python
```py
speichere_kontakt("Anna", "anna@mail.de", "+49151 12 34 567")
zeige_kontakte()  # Ausgabe: Anna wird angezeigt
```
Problem: Ich prüfe nur visuell, ob es funktioniert. Das ist kein automatischer Test.

Professioneller Ansatz mit Assertions:
Python
```py
def test_speichere_kontakt():
    # Arrange: Testdaten vorbereiten
    name = "Anna"
    email = "anna@mail.de"
    telefon = "+49151 12 34 567"
    
    # Act: Funktion ausführen
    speichere_kontakt(name, email, telefon)
    
    # Assert: Ergebnis prüfen
    kontakte = lade_kontakte()
    assert any(k['E-Mail'] == email for k in kontakte), "Kontakt wurde nicht gespeichert"
```
Was ich dabei lerne:

    assert macht den Test automatisch (kein manuelles Prüfen mehr)
    Das Arrange-Act-Assert-Pattern strukturiert Tests klar
    Tests können automatisch durchlaufen werden (z.B. in CI/CD)

3. Testbarkeit: Was ich jetzt verstehe
Das Problem mit echten Dateien

Meine aktuellen Tests:
Python
```py
TEXT_DATEI = 'python/exercises/Teilprüfung 03 lokal/namen.txt'
test_namen = lade_daten()  # Liest echte Datei
```
Probleme:

    Abhängigkeit vom Dateisystem: Test schlägt fehl, wenn Datei fehlt
    Seiteneffekte: Tests können sich gegenseitig beeinflussen
    Langsam: Disk-I/O ist langsamer als In-Memory-Tests
    Nicht isoliert: Test verändert echte Daten

Mocking: Die Lösung für testbare externe Abhängigkeiten

Was ich verstanden habe:
Mocking bedeutet, externe Abhängigkeiten durch kontrollierte Ersatzobjekte zu ersetzen. Statt einer echten Datei nutze ich ein Fake-Objekt, das das Verhalten simuliert.

Beispiel mit unittest.mock:
Python
```py
from unittest.mock import mock_open, patch

def test_lade_daten_mit_mock():
    # Fake-Dateiinhalt
    fake_inhalt = "Anna\nBernd\nCarla\n"
    
    # Mock erstellen
    with patch('builtins.open', mock_open(read_data=fake_inhalt)):
        daten = lade_daten()
    
    # Prüfen
    assert daten == ['Anna', 'Bernd', 'Carla']
```
Vorteile:

    Keine echte Datei nötig
    Schnell (alles im RAM)
    Isoliert (keine Seiteneffekte)
    Kontrollierbar (ich bestimme den Inhalt)

Fixtures: Reproduzierbare Testumgebungen

Was ich bisher gemacht habe:
Python
```py
daten = [
    ('Max', 'max@mail.de', '+49161 12 34 567'),
    ('Erika', 'erika@mail.de', '+49161 23 45 678'),
]
for i in daten:
    speichere_kontakt(i[0], i[1], i[2])
```
Das ist bereits ein Fixture: Ich erstelle einen definierten Startzustand für meine Tests.

Professionell mit PyTest:
Python
```py
import pytest

@pytest.fixture
def test_kontakte():
    """Fixture: Stellt Testdaten bereit"""
    return [
        ('Max', 'max@mail.de', '+49161 12 34 567'),
        ('Erika', 'erika@mail.de', '+49161 23 45 678'),
    ]

def test_speichern(test_kontakte):
    for name, email, tel in test_kontakte:
        speichere_kontakt(name, email, tel)
    
    kontakte = lade_kontakte()
    assert len(kontakte) == 2
```
Erkenntnis: Ich habe Fixtures bereits intuitiv genutzt, nur ohne Framework.
4. Test-Pyramide: Welche Tests wo?
Was ich jetzt verstehe

Es gibt verschiedene Test-Ebenen:
Code

        /\
       /  \      E2E Tests (wenige, langsam, komplett)
      /----\
     /      \    Integrationstests (einige, mittel, mehrere Module)
    /--------\
   /          \  Unit Tests (viele, schnell, einzelne Funktionen)
  /____________\

Meine aktuellen Tests sind eine Mischung:

Unit Test (testet eine Funktion):
Python
```py
test_namen = lade_daten()  # Testet nur lade_daten()
assert len(test_namen) > 0
```
Integrationstest (testet mehrere Funktionen zusammen):
Python
```py
speichere_kontakt("Anna", "anna@mail.de", "123")  # Funktion 1
kontakte = lade_kontakte()  # Funktion 2
zeige_kontakte()  # Funktion 3
```
Was ich lernen will:

    Unit Tests zuerst: Jede Funktion einzeln testen
    Integrationstests danach: Zusammenspiel testen
    E2E-Tests sparsam einsetzen: Nur für kritische User-Flows

5. Konkrete nächste Schritte
Was ich umsetzen will (priorisiert)

1. PyTest einrichten (Woche 9)
bash

pip install pytest
pytest test_kontakte.py

Ziel: Meine bestehenden Tests in PyTest-Format umschreiben.

2. Ersten echten Unit-Test schreiben
Python
```py
def test_lade_kontakte_mit_duplikat():
    # Test: Duplikat wird abgelehnt
    speichere_kontakt("Anna", "anna@mail.de", "123")
    speichere_kontakt("Anna", "anna@mail.de", "123")  # Duplikat
    
    kontakte = lade_kontakte()
    assert len(kontakte) == 1, "Duplikat wurde nicht verhindert"
```
3. Mocking ausprobieren (Woche 10)

    Tutorial durcharbeiten: unittest.mock oder pytest-mock
    Einen Test schreiben, der open() mockt

4. CI/CD Pipeline einrichten (Woche 11-12)

    GitHub Actions Workflow erstellen
    Tests automatisch bei jedem Push laufen lassen

6. Offene Fragen für Vertiefung
Fragen, die ich durch praktisches Ausprobieren klären will

    Wie organisiere ich Tests in größeren Projekten?
        Separate tests/-Ordner?
        Naming Conventions (test_*.py)?
        Wie vermeide ich Code-Duplikation in Tests?

    Wie teste ich Fehler-Szenarien systematisch?
    Python

    def test_lade_daten_datei_nicht_gefunden():
        # Wie teste ich, dass FileNotFoundError korrekt behandelt wird?
        pass

    Wie messe ich Test-Coverage?
        Tool: pytest-cov
        Ziel: Mind. 80% Abdeckung?

    Wie refaktoriere ich bestehenden Code, um ihn testbarer zu machen?
        Beispiel: Meine hauptmenü()-Funktion ist schwer testbar (wegen input())
        Lösung: Dependency Injection?

7. Persönliche Reflexion
Was mich motiviert

Aha-Momente während der Implementierung:

    Als ich gemerkt habe, dass mein TESTS_AKTIV-Flag professionellen CI/CD-Setups ähnelt
    Als ich verstanden habe, dass meine modularen Funktionen bereits "testbar by design" sind
    Als ich gemerkt habe, dass Fixtures etwas sind, was ich schon intuitiv genutzt habe

Was mir noch schwerfällt:

    Zwischen "Test" und "Test-Code" zu unterscheiden (meine print-Statements sind keine echten Tests)
    Edge Cases systematisch zu identifizieren (ich teste meist nur Happy Path)
    Tests zu schreiben, bevor ich die Funktion implementiere (TDD-Ansatz)

Was ich mitnehme:

    Automatisierte Tests sind weniger ein Tool, sondern eine Denkweise
    Testbarkeit beginnt beim Code-Design, nicht erst beim Testen
    Kleine, fokussierte Funktionen sind der Schlüssel zu gutem Testing

Ressourcen für meine weitere Lernreise

Mögliche Tutorials, die ich durcharbeiten könnte:

    Real Python: "Getting Started With Testing in Python" (pytest)
    PyTest Documentation: Official Tutorial
    Martin Fowler: "Mocks Aren't Stubs" (Konzepte verstehen)

Projekte zum Üben:

    Mein 8.7.C.01.py komplett mit PyTest umschreiben
    Einen Test mit Mocking implementieren
    GitHub Actions Workflow für automatische Tests

Community-Austausch:

    Fragen im Devdiscord stellen
    Code-Review von erfahrenen Entwicklern einholen

Zusammenfassung

Dieser Exkurs hat mir geholfen, meine Lernerfolge zu strukturieren und zu erkennen, dass ich bereits viele Konzepte intuitiv richtig angewendet habe. Gleichzeitig sehe ich klar, wo ich noch lernen muss:

Was ich kann:

    Fehlerbehandlung mit try-except
    Ressourcenverwaltung mit with
    Modulare, fokussierte Funktionen schreiben
    Einfache automatisierte Testläufe erstellen

Was ich als nächstes lerne:

    PyTest für echte Unit-Tests
    Mocking für isolierte Tests
    Assertions statt print-Statements
    CI/CD-Integration für automatische Tests

Mein Ziel:
Bis zur nächsten Teilprüfung ein Projekt mit vollständiger PyTest-Abdeckung und CI/CD-Pipeline erstellen.

Erstellt: 10.02.2026
Letztes Update: 10.02.2026
Status: Living Document