# Chest Inventory Showcase (Python)

## Ziel

Das bestehende Inventarsystem zu einem testbaren Mid-Size-Projekt ausbauen, bei dem Geschaeftslogik sauber von CLI-Ein-/Ausgabe getrennt ist.

## Quelle im Learning Repository

- Hauptdatei: [python/projects/chest/chest.py](../../python/projects/chest/chest.py)

## Aktueller Stand

- Umfangreiche Inventarlogik mit Rucksack, Truhen, Gewichts- und Slot-Limits.
- Mehrere Kernfunktionen vorhanden (add_to_chest, quick_fill_chest, empty_chest_to_backpack).
- Hinweise auf bekannte Bugs und Feature-Ideen sind bereits direkt im Quelltext notiert.

## Showcase-Mehrwert

1. Core-Engine extrahieren: State und Regeln in testbare Module schneiden.
2. Fehlerrobustheit erhoehen: valide Grenzen fuer Gewicht, Stack und Slots.
3. Testabdeckung fuer komplexe Regeln sichtbar machen.

## Geplante Teststrategie

### Unit

- calculate_weight und count_item_types mit klaren Fixtures.
- Grenzfaelle fuer Slot-Limit und Gewichtslimit.
- Verhinderung ungueltiger Transfers.

### Integration

- Vollstaendiger Flow: Backpack fuellen -> in Truhe verschieben -> Truhe leeren.
- Reproduzierbarkeit ueber festen Zufalls-Seed oder deterministische Testdaten.

## Umsetzungsschritte

1. Quellstand in dieses Showcase uebernehmen.
2. Globale Variablen durch expliziten State ersetzen.
3. CLI-Funktionen von Core-Logik entkoppeln.
4. Test-Suite fuer Regeln und End-to-End-Flows aufbauen.

## Fertig, wenn

- Kernlogik ohne Benutzereingaben testbar ist.
- Die bekannten Regel-Bugs reproduzierbar getestet und behoben sind.
- Projekt als eigenstaendiges Repository laeuft.

## Platzhalter fuer spaeteren Repo-Link

- Externes Repository: TODO
