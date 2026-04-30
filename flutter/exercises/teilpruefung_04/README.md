# teilpruefung_04 von Matthias Kahlert

Flutter-Prüfungsprojekt für einen lokalen Lieferdienst.

## Tracking-Ansatz

Die Kartenansicht nutzt bewusst eine Simulation statt echter GPS-Daten:

- Startpunkt ist der Rathausmarkt in Hamburg
- Der Marker bewegt sich periodisch in kleinen Schritten


Damit wird das geforderte Echtzeit-Tracking für die Pruefung demonstriert,
In einer echten App würde die Fahrzeugposition von einem Backend-Service bereitgestellt,
der die GPS-Daten des Fahrzeugs empfängt und an die App sendet.

## Device
Ich habe die app auf einem virtuellen Device über Android Studiu und zwar einem Pixel 10 mit API 37.0 "CinnamonBun" und Android 17.0 getestet. 

## Start

```bash
flutter pub get
flutter run
```

## Tests

```bash
flutter test
```
