# Buchladen OOP Showcase (Python)

## Ziel

Aus einem kompakten OOP-Lernbeispiel ein sauberes Portfolio-Quick-Win-Projekt mit klarer Unit- und Integrations-Testbasis erstellen.

## Quelle im Learning Repository

- Hauptdatei: [python/exercises/Teilpruefung 06/mkahlert_teilpruefung_06.py](../../python/exercises/Teilpr%C3%BCfung%2006/mkahlert_teilpruefung_06.py)

## Aktueller Stand

- Code uebernommen und in testbare Struktur geschnitten.
- Domain-Modul vorhanden: `bookstore.py`.
- Demo-Einstieg vorhanden: `demo.py`.
- Erste pytest-Suite vorhanden: `tests/test_bookstore.py`.

## Showcase-Mehrwert

1. Sehr gute Basis fuer schnelle, saubere Tests.
2. Gute Demonstration von OOP-Grundlagen plus testbarer Logik.
3. Ideal als erstes Portfolio-Projekt mit kurzer Umsetzungszeit.

## Geplante Teststrategie

### Unit

- Buch-Initialisierung und String-Repraesentation.
- Suche nach Kategorie (inkl. Case-Insensitive Verhalten).
- Gesamtpreis-Berechnung fuer verschiedene Listen.

### Integration

- Workflow-Test: Inventar aufbauen -> filtern -> Summen berechnen.
- Leere Ergebnisse und leeres Inventar als Randfaelle.

## Umsetzungsschritte

1. Quellstand in dieses Showcase uebernehmen. (erledigt)
2. Strukturverbesserung (Demo von Bibliothekslogik getrennt). (erledigt)
3. Unit- und Integrations-Tests implementieren. (erste Version erledigt)
4. README um Ausfuehrung, Tests und Learnings ergaenzen. (in Arbeit)

## Projektstruktur

- `bookstore.py`: Kernlogik mit `Buch`, `Buchladen` und `baue_demo_inventar`.
- `demo.py`: Konsolen-Demo fuer manuelle Ausfuehrung.
- `tests/test_bookstore.py`: Unit- und Workflow-nahe Tests.

## Lokale Ausfuehrung

1. Demo starten:

```bash
python demo.py
```

2. Tests ausfuehren:

```bash
pytest -q
```

## Testabdeckung aktuell

- String-Repraesentation eines Buchs.
- Kategorie-Suche (case-insensitive, trim).
- Gesamtpreis-Berechnung inklusive leerer Listen.
- Integrationsnaher Workflow ueber Demo-Inventar.

## Fertig, wenn

- Zentrale Methoden durch Tests abgesichert sind.
- Test-Command dokumentiert und reproduzierbar ist.
- Projekt in ein eigenes Repository ueberfuehrt und verlinkt ist.

## Platzhalter fuer spaeteren Repo-Link

- Externes Repository: TODO
