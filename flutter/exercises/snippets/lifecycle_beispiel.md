import 'package:flutter/material.dart';
// hier passieren eigentlich drei Dinge nacheinander: Die App startet, Flutter baut die Oberfläche auf,
// und ein StatefulWidget verwaltet dabei seinen eigenen Zustand.

void main() {
  // LebenszyklusDemoApp ist der Einstiegspunkt des sichtbaren UI-Baums
  runApp(const LebenszyklusDemoApp());
}

class LebenszyklusDemoApp extends StatelessWidget {
  const LebenszyklusDemoApp({super.key});

  // In LebenszyklusDemoApp wird in build() ein MaterialApp zurückgegeben.
  // Das liefert Material-Design-Grundfunktionen wie Theme, Scaffold und Buttons.
  // Das home ist ein Scaffold, also die Grundseite,
  // und darin liegt das Widget LebenszyklusBeispiel.
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Scaffold(
        body: Center(child: LebenszyklusBeispiel(titel: 'Lebenszyklus Demo')),
      ),
    );
  }
}

class LebenszyklusBeispiel extends StatefulWidget {
  final String titel;

  const LebenszyklusBeispiel({Key? key, required this.titel}) : super(key: key);

  // Der veränderliche Teil ist im State-Objekt _LebenszyklusBeispielState.
  @override
  _LebenszyklusBeispielState createState() => _LebenszyklusBeispielState();
}

// Dieses State-Objekt enthält _daten, also den internen Zustand, der sich später ändern darf.
class _LebenszyklusBeispielState extends State<LebenszyklusBeispiel> {
  late String _daten;

  @override
  void initState() {
    super.initState();
    print('initState aufgerufen');

    // Initialisierung von Ressourcen
    _daten = 'Initialisierte Daten';
  }

  // didChangeDependencies(): läuft nach initState() und später erneut, wenn sich geerbte Abhängigkeiten ändern
  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    print('didChangeDependencies aufgerufen');

    // Zugriff auf Abhängigkeiten wie Theme oder Locale
    print('Aktuelles Theme: ${Theme.of(context).brightness}');
  }

  @override
  void didUpdateWidget(covariant LebenszyklusBeispiel oldWidget) {
    super.didUpdateWidget(oldWidget);
    print('didUpdateWidget aufgerufen');

    if (widget.titel != oldWidget.titel) {
      print('Titel hat sich geändert');
    }
  }

  // build(): baut die sichtbare Oberfläche. Diese Methode darf oft laufen,
  // deshalb sollte sie keine aufwendige Initialisierung enthalten.
  @override
  Widget build(BuildContext context) {
    print('build aufgerufen');

    // Bei Buttonclick wird setState aufgerufen und der interne Zustand aktualisiert.
    // setState markiert das Widget für einen Neuaufbau, wodurch build erneut ausgeführt wird, um die Oberfläche mit den neuen Daten zu aktualisieren.
    return Column(
      children: [
        Text(widget.titel),
        Text(_daten),
        ElevatedButton(
          onPressed: () {
            setState(() {
              _daten = 'Aktualisierte Daten';
              print('setState aufgerufen');
            });
          },
          child: Text('Daten aktualisieren'),
        ),
      ],
    );
  }

  @override
  void dispose() {
    print('dispose aufgerufen');

    // Freigabe von Ressourcen
    super.dispose();
  }
}
