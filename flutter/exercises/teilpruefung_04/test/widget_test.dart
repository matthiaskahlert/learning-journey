import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:teilpruefung_04/main.dart';

void main() {
  // Unit-Tests

  group('Lieferoption', () {
    test('kLieferoptionen enthält genau 3 Einträge', () {
      expect(kLieferoptionen.length, 3);
    });

    test('Erste Option ist "Essen" mit korrekten Werten', () {
      final essen = kLieferoptionen.first;
      expect(essen.id, 'food');
      expect(essen.bezeichnung, 'Essen');
      expect(essen.geschaetzteZeit, 30);
      expect(essen.preisEur, 6.90);
    });

    test('Alle Optionen haben eindeutige IDs', () {
      final ids = kLieferoptionen.map((o) => o.id).toList();
      expect(ids.toSet().length, ids.length);
    });

    test('Alle Optionen haben positive Preise und Zeiten', () {
      for (final option in kLieferoptionen) {
        expect(option.preisEur, greaterThan(0));
        expect(option.geschaetzteZeit, greaterThan(0));
      }
    });
  });

  group('BestellverlaufEintrag', () {
    test('Speichert alle Felder korrekt', () {
      final datum = DateTime(2024, 1, 15);
      final eintrag = BestellverlaufEintrag(
        titel: 'Pakete',
        erstelltAm: datum,
        status: 'Unterwegs',
      );
      expect(eintrag.titel, 'Pakete');
      expect(eintrag.erstelltAm, datum);
      expect(eintrag.status, 'Unterwegs');
    });
  });

  // Widget-Tests
  group('Startseite', () {
    testWidgets('Zeigt alle 3 Lieferoptionen an', (tester) async {
      await tester.pumpWidget(
        MaterialApp(home: Startseite(beiBestellung: (_) {})),
      );
      for (final option in kLieferoptionen) {
        expect(find.text(option.bezeichnung), findsOneWidget);
      }
    });

    testWidgets('Zeigt den App-Titel "SchnellBote"', (tester) async {
      await tester.pumpWidget(
        MaterialApp(home: Startseite(beiBestellung: (_) {})),
      );
      expect(find.text('SchnellBote'), findsOneWidget);
    });

    testWidgets('Tippen auf eine Karte öffnet die Detailseite', (tester) async {
      await tester.pumpWidget(
        MaterialApp(home: Startseite(beiBestellung: (_) {})),
      );
      await tester.tap(find.text(kLieferoptionen.first.bezeichnung));
      await tester.pumpAndSettle();
      expect(find.text('Jetzt bestellen'), findsOneWidget);
    });
  });

  group('Detailseite', () {
    Widget buildDetailseite(
      Lieferoption option, {
      ValueChanged<Lieferoption>? onBestellen,
    }) {
      return MaterialApp(
        home: Detailseite(
          lieferoption: option,
          beiBestellung: onBestellen ?? (_) {},
        ),
      );
    }

    testWidgets('Zeigt die geschätzte Lieferzeit an', (tester) async {
      final essen = kLieferoptionen.first;
      await tester.pumpWidget(buildDetailseite(essen));
      expect(find.text('ca. ${essen.geschaetzteZeit} Minuten'), findsOneWidget);
    });

    testWidgets('Essen-Option zeigt Label "Liefergebühr ab"', (tester) async {
      final essen = kLieferoptionen.firstWhere((o) => o.id == 'food');
      await tester.pumpWidget(buildDetailseite(essen));
      expect(find.text('Liefergebühr ab'), findsOneWidget);
    });

    testWidgets('Dokumente-Option zeigt Label "Lieferkosten"', (tester) async {
      final dokumente = kLieferoptionen.firstWhere((o) => o.id == 'documents');
      await tester.pumpWidget(buildDetailseite(dokumente));
      expect(find.text('Lieferkosten'), findsOneWidget);
    });

    testWidgets('Essen-Option zeigt Hinweis zur Preisvariation', (
      tester,
    ) async {
      final essen = kLieferoptionen.firstWhere((o) => o.id == 'food');
      await tester.pumpWidget(buildDetailseite(essen));
      expect(
        find.textContaining('Mindestbestellwert'),
        findsAtLeastNWidgets(1),
      );
    });

    testWidgets('"Jetzt bestellen"-Button ruft den Callback auf', (
      tester,
    ) async {
      bool aufgerufen = false;
      final essen = kLieferoptionen.first;
      await tester.pumpWidget(
        MaterialApp(
          home: Detailseite(
            lieferoption: essen,
            beiBestellung: (_) => aufgerufen = true,
          ),
        ),
      );
      await tester.ensureVisible(find.text('Jetzt bestellen'));
      await tester.tap(find.text('Jetzt bestellen'));
      await tester.pump();
      expect(aufgerufen, isTrue);
    });

    testWidgets('"Jetzt bestellen" übergibt die korrekte Lieferoption', (
      tester,
    ) async {
      Lieferoption? uebergeben;
      final pakete = kLieferoptionen.firstWhere((o) => o.id == 'packages');
      await tester.pumpWidget(
        MaterialApp(
          home: Detailseite(
            lieferoption: pakete,
            beiBestellung: (o) => uebergeben = o,
          ),
        ),
      );
      await tester.ensureVisible(find.text('Jetzt bestellen'));
      await tester.tap(find.text('Jetzt bestellen'));
      await tester.pump();
      expect(uebergeben?.id, 'packages');
    });
  });

  group('Profilseite', () {
    testWidgets('Zeigt Leertext wenn keine Bestellungen vorhanden', (
      tester,
    ) async {
      await tester.pumpWidget(
        const MaterialApp(home: Profilseite(bestellverlauf: [])),
      );
      expect(find.text('Noch keine Bestellungen vorhanden.'), findsOneWidget);
    });

    testWidgets('Zeigt Bestellverlauf-Einträge mit Titel und Status', (
      tester,
    ) async {
      final eintraege = [
        BestellverlaufEintrag(
          titel: 'Pakete',
          erstelltAm: DateTime(2024, 3, 10),
          status: 'Unterwegs',
        ),
      ];
      await tester.pumpWidget(
        MaterialApp(home: Profilseite(bestellverlauf: eintraege)),
      );
      expect(find.text('Pakete'), findsOneWidget);
      expect(find.text('Unterwegs'), findsOneWidget);
    });

    testWidgets('Formatiert das Datum korrekt als TT.MM.JJJJ', (tester) async {
      final eintraege = [
        BestellverlaufEintrag(
          titel: 'Essen',
          erstelltAm: DateTime(2024, 3, 5),
          status: 'Zugestellt',
        ),
      ];
      await tester.pumpWidget(
        MaterialApp(home: Profilseite(bestellverlauf: eintraege)),
      );
      expect(find.text('05.03.2024'), findsOneWidget);
    });

    testWidgets('Zeigt Nutzernamen "Max Mustermann"', (tester) async {
      await tester.pumpWidget(
        const MaterialApp(home: Profilseite(bestellverlauf: [])),
      );
      expect(find.text('Max Mustermann'), findsOneWidget);
    });
  });

  group('Hauptbildschirm', () {
    testWidgets('Zeigt BottomNavigationBar mit 3 Tabs', (tester) async {
      await tester.pumpWidget(const MaterialApp(home: Hauptbildschirm()));
      expect(find.text('Startseite'), findsOneWidget);
      expect(find.text('Karte'), findsOneWidget);
      expect(find.text('Profil'), findsOneWidget);
    });

    testWidgets('Startet standardmäßig auf der Startseite', (tester) async {
      await tester.pumpWidget(const MaterialApp(home: Hauptbildschirm()));
      expect(find.text('SchnellBote'), findsOneWidget);
    });

    testWidgets('Navigation zum Profil-Tab zeigt leere Bestellhistorie', (
      tester,
    ) async {
      await tester.pumpWidget(const MaterialApp(home: Hauptbildschirm()));
      await tester.tap(find.text('Profil'));
      await tester.pump();
      expect(find.text('Noch keine Bestellungen vorhanden.'), findsOneWidget);
    });
  });
}
