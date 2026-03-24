# TestSetup

## Ziel
Diese Datei dokumentiert den aktuellen Stand der Tests im Java-Teil des Repositories.
Sie beschreibt:
- welche Testverfahren verwendet werden,
- wie die Tests arbeiten,
- was aktuell abgedeckt ist,
- was noch nicht abgedeckt ist.

Die Dokumentation ist als Lern- und Referenzbasis gedacht (u. a. fuer den Weg Richtung SDIT).

## Aktuelles Test-Stack
- Testframework: JUnit 5 (Jupiter)
- Build/Test Runner: Maven Surefire
- Datenbank in REST-Tests: Apache Derby In-Memory
- Testquellen: `java/src/test/java`

## Testausfuehrung
Alle Tests:
```powershell
Set-Location java
mvn test
```

Nur REST-Handler-Tests:
```powershell
Set-Location java
mvn "-Dtest=PersonHandlerTest" test
```

## Uebersicht der vorhandenen Testklassen

### 1) REST.PersonHandlerTest
Datei: `java/src/test/java/REST/PersonHandlerTest.java`

Art:
- Komponentennahe Unit/Component-Tests fuer den REST-Handler
- Kein echter HTTP-Server-Start
- Handler wird direkt aufgerufen

Technik:
- In `@BeforeAll` wird Derby In-Memory verbunden: `jdbc:derby:memory:rest_test_db;create=true`
- In `@BeforeEach` wird Tabelle `Personen` neu erstellt und mit 2 Datensaetzen befuellt
- Eine Test-Subclass (`TestablePersonHandler`) ueberschreibt `getAttribute("id")`, um URL-Parameter zu simulieren

Abdeckung:
- GET ohne ID liefert JSON-Array mit allen Personen
- GET mit ID liefert eine Person
- PUT als Partial Update aktualisiert nur uebergebene Felder
- PUT mit leerem Update-Body liefert Fehler
- PUT mit ungueltiger ID liefert Fehler

Nicht direkt abgedeckt:
- HTTP Routing ueber `RESTSchnittstelle`/Router
- POST-Endpunkt
- Verhalten bei konkurrierenden Zugriffen

### 2) personenverwaltung.PersonenverwaltungTest
Datei: `java/src/test/java/personenverwaltung/PersonenverwaltungTest.java`

Art:
- Konsolenfluss-Test (Blackbox auf `main`)

Technik:
- Simulierte Benutzereingabe ueber `System.setIn`
- Ausgabepruefung ueber `System.setOut`

Abdeckung:
- Kunde-Flow laeuft ohne Exception
- Mitarbeiter-Flow laeuft ohne Exception
- Basis-Ausgaben werden geprueft

Nicht direkt abgedeckt:
- Detaillierte Fachlogik einzelner Methoden
- Fehlerfaelle bei invaliden Eingaben

### 3) CalculateAverageTest
Datei: `java/src/test/java/CalculateAverageTest.java`

Art:
- Klassischer Unit-Test einer Rechenfunktion

Abdeckung:
- Durchschnitt fuer normales Array
- Sonderfall leeres Array

### 4) Uebung_7_1_Ue_02_Test
Datei: `java/src/test/java/Uebung_7_1_Ue_02_Test.java`

Art:
- Unit-Tests fuer Lager-Logik

Abdeckung:
- Produkt hinzufuegen
- Produktmenge erhoehen bei bestehendem Produkt
- Produkt entfernen
- Anzeige des Lagerbestands ohne Fehler

### 5) Uebung_7_2_Ue_01Test und Uebung_7_2_Ue_02Test
Dateien:
- `java/src/test/java/Uebung_7_2_Ue_01Test.java`
- `java/src/test/java/Uebung_7_2_Ue_02Test.java`

Art:
- Unit-Tests fuer Filterlogik gerader Zahlen

Abdeckung je Klasse:
- gemischte Zahlen
- leere Eingabeliste
- nur ungerade Zahlen
- nur gerade Zahlen

### 6) exercises.DerbyIntegrationTest
Datei: `java/src/test/java/exercises/DerbyIntegrationTest.java`

Status:
- Aktuell vollständig auskommentiert (nicht aktiv im Testlauf)

Bedeutung:
- Historischer Entwurf fuer Datenbank-Integrationschecks
- Wird derzeit nicht ausgefuehrt

## Bewertung des aktuellen Settings
Staerken:
- Solider Mix aus Unit-Tests und komponentennahen Tests
- REST-Kernlogik (GET/PUT) ist automatisiert pruefbar
- Testdaten werden in REST-Tests reproduzierbar pro Test neu aufgebaut

Grenzen:
- Kein echter End-to-End HTTP-Test der REST-Schnittstelle
- POST ist derzeit nicht durch Tests abgesichert
- Keine automatisierte Coverage-Messung im Buildprozess

## Nächste Schritte
1. HTTP-Integrationstest fuer `/person` und `/person/{id}` ergaenzen (Server starten, echte Requests senden).
2. POST-Tests aufnehmen (Happy Path und Fehlerfaelle).
3. Negativtests fuer JSON-Fehlformat und fehlende Felder erweitern.
4. JaCoCo fuer Coverage-Reporting integrieren.
5. Testfaelle in Given/When/Then-Struktur vereinheitlichen.


