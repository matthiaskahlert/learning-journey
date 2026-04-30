# teilpruefung_04 von Matthias Kahlert

Flutter-Prüfungsprojekt für einen Liefer / Kurierdienst:

- Startseite mit Lieferoptionen
- Detailseite mit Lieferzeit und Kosten
- Kartenansicht mit Geolokalisierung
- Profilbereich mit Bestellhistorie

## Hinweis zur Aufgabenstellung (Karte)

In der Aufgabenstellung wird für die Kartenansicht die Fahrzeugposition in Echtzeit gefordert und die Nutzung von `google_maps_flutter` (mit OpenStreetMap-Bezug) sowie optional `geolocator` erwähnt. Ich hab nun aber keine Fahrzeugposition simuliert, sondern mich bewusst stattdessen direkt für die **Geolocation des aktuellen Devices** als Kartenposition entschieden.

## Tests

Die Datei `test/widget_test.dart` enthält zusätzlich noch 21 Tests

Tests starten mit:

```bash
flutter test
```

## Voraussetzungen

- Flutter SDK ist installiert
- Abhängigkeiten mit `flutter pub get` installieren
- Für Android-Emulator-Tests muss eine gültige Mock-Location gesetzt sein, oder man landet bei der default location des meulators, bei mir war das mountain view von google...
