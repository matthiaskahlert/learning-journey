// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter_test/flutter_test.dart';

import 'package:widget_lifecycle/main.dart';

void main() {
  testWidgets('zeigt Titel und aktualisiert Daten', (
    WidgetTester tester,
  ) async {
    await tester.pumpWidget(const LebenszyklusDemoApp());

    expect(find.text('Lebenszyklus Demo'), findsOneWidget);
    expect(find.text('Initialisierte Daten'), findsOneWidget);

    await tester.tap(find.text('Daten aktualisieren'));
    await tester.pump();

    expect(find.text('Aktualisierte Daten'), findsOneWidget);
  });
}
