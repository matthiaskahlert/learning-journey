# REST Person Handler Showcase (Java)

## Ziel

Aus einem bestehenden REST-Lernprojekt ein portfoliofaehiges Backend-Showcase machen, mit Fokus auf Testbarkeit, Integrationstests und robuster Datenbanklogik.

## Quelle im Learning Repository

- Handler: [java/src/main/java/exercises/REST/PersonHandler.java](../../java/src/main/java/exercises/REST/PersonHandler.java)
- Bestehende Tests: [java/src/test/java/REST/PersonHandlerTest.java](../../java/src/test/java/REST/PersonHandlerTest.java)

## Aktueller Stand

- Eigenstaendiges Maven-Projekt ist angelegt (`pom.xml`).
- Handler und Tests sind in diese Showcase-Struktur uebernommen.
- GET/POST/PUT sind testbar gegen In-Memory-Derby.
- Fuer lokale Testbarkeit ohne externes Restlet-JAR sind minimale Restlet-Stand-ins enthalten.

## Showcase-Mehrwert

1. Security-Hardening: SQL-Concatenation in sichere Prepared Statements ueberfuehren.
2. API-Verhalten absichern: klare Fehlerantworten und konsistente Status-Messages.
3. Stabiler Testaufbau: Unit-nahe Tests plus DB-Integrationstests.

## Geplante Teststrategie

### Unit-orientiert

- Validierung von Eingaben (id fehlt, id nicht numerisch, leere Payload).
- JSON-Parsing Fehlerfaelle.

### Integration

- GET ohne id liefert Liste.
- GET mit gueltiger id liefert genau eine Person.
- PUT mit Teilpayload aktualisiert nur erlaubte Felder.
- POST persistiert Person inklusive Adressfeldern.
- Nicht gefundene IDs liefern reproduzierbare Fehlerantwort.

## Umsetzungsschritte

1. Code aus dem Learning-Pfad in dieses Showcase uebernehmen. (erledigt)
2. SQL-Zugriffe auf Prepared Statements umstellen. (teilweise erledigt)
3. Testfaelle ausbauen und Regressionstest-Suite erstellen. (erste Version erledigt)
4. README um Test-Commands, Architektur und Learnings erweitern. (in Arbeit)

## Projektstruktur

- `src/main/java/REST/PersonHandler.java`: Kernlogik fuer GET/POST/PUT.
- `src/test/java/REST/PersonHandlerTest.java`: Integrationstests gegen In-Memory-Derby.
- `src/main/java/org/restlet/resource/*`: kleine Stand-ins fuer testbaren Handler ohne externes Restlet-JAR.

## Lokale Ausfuehrung

1. Tests starten:

```bash
mvn test
```

## Testabdeckung aktuell

- GET ohne ID und mit ID.
- GET fuer nicht vorhandene ID.
- POST-Persistierung in Derby.
- PUT Teilupdate und Validierungsfehler.

## Fertig, wenn

- Alle vorhandenen plus neue Tests stabil lokal laufen.
- Kritische SQL-Risiken beseitigt sind.
- Projekt in ein eigenes Repository verschoben und verlinkt ist.

## Platzhalter fuer spaeteren Repo-Link

- Externes Repository: TODO
