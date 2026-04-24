import 'package:flutter/material.dart';

class CounterOnePage extends StatefulWidget {
  final String titel;

  const CounterOnePage({Key? key, this.titel = 'Counter 1'}) : super(key: key);

  // Der veränderliche Teil ist im State-Objekt _CounterOnePageState.
  @override
  _CounterOnePageState createState() => _CounterOnePageState();
}

// Dieses State-Objekt enthält _daten, also den internen Zustand, der sich später ändern darf.
class _CounterOnePageState extends State<CounterOnePage> {
  late String _daten;

  // _log speichert alle Lifecycle-Einträge, damit sie in der App angezeigt werden können.
  final List<String> _log = [];

  // Hilfsmethode: Fügt einen Eintrag zur Log-Liste hinzu.
  // setState() innerhalb von _addLog sorgt dafür, dass die Anzeige sofort aktualisiert wird.
  void _addLog(String eintrag) {
    // dispose() läuft nach dem Unmount – mounted-Prüfung verhindert setState nach dispose.
    if (mounted) {
      setState(() {
        _log.add(eintrag);
      });
    }
  }

  @override
  void initState() {
    super.initState();
    print('initState aufgerufen'); // ignore: avoid_print

    // Initialisierung von Ressourcen
    _daten = 'Initialisierte Daten';

    // _addLog kann hier noch nicht setState aufrufen (Widget ist noch nicht eingehängt),
    // deshalb direkt zur Liste hinzufügen ohne setState.
    _log.add('initState aufgerufen');
  }

  // didChangeDependencies(): läuft nach initState() und später erneut, wenn sich geerbte Abhängigkeiten ändern
  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    print('didChangeDependencies aufgerufen'); // ignore: avoid_print

    // Zugriff auf Abhängigkeiten wie Theme oder Locale
    final helligkeit = Theme.of(context).brightness;
    print('Aktuelles Theme: $helligkeit'); // ignore: avoid_print
    _addLog('didChangeDependencies aufgerufen');
    _addLog('Aktuelles Theme: $helligkeit');
  }

  @override
  void didUpdateWidget(covariant CounterOnePage oldWidget) {
    super.didUpdateWidget(oldWidget);
    print('didUpdateWidget aufgerufen'); // ignore: avoid_print
    _addLog('didUpdateWidget aufgerufen');

    if (widget.titel != oldWidget.titel) {
      print('Titel hat sich geändert'); // ignore: avoid_print
      _addLog('Titel hat sich geändert');
    }
  }

  // build(): baut die sichtbare Oberfläche. Diese Methode darf oft laufen,
  // deshalb sollte sie keine aufwendige Initialisierung enthalten.
  @override
  Widget build(BuildContext context) {
    print('build aufgerufen'); // ignore: avoid_print

    // Bei Buttonclick wird setState aufgerufen und der interne Zustand aktualisiert.
    // setState markiert das Widget für einen Neuaufbau, wodurch build erneut ausgeführt wird, um die Oberfläche mit den neuen Daten zu aktualisieren.
    return Scaffold(
      appBar: AppBar(title: Text(widget.titel)),
      body: Column(
        children: [
          // Oberer Bereich: bisherige Widgets
          Center(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                const SizedBox(height: 16),
                Text(widget.titel),
                Text(_daten),
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      _daten = 'Aktualisierte Daten';
                      print('setState aufgerufen'); // ignore: avoid_print
                      _log.add('setState aufgerufen');
                    });
                  },
                  child: const Text('Daten aktualisieren'),
                ),
                const SizedBox(height: 16),
              ],
            ),
          ),
          const Divider(),
          // Log-Bereich: zeigt alle Lifecycle-Einträge als scrollbare Liste an.
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 12.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                const Text(
                  'Lifecycle-Log:',
                  style: TextStyle(fontWeight: FontWeight.bold),
                ),
                TextButton(
                  // Ermöglicht das Zurücksetzen des Logs zum Ausprobieren.
                  onPressed: () => setState(() => _log.clear()),
                  child: const Text('Leeren'),
                ),
              ],
            ),
          ),
          Expanded(
            // Expanded füllt den restlichen Platz und ermöglicht das Scrollen langer Logs.
            child: ListView.builder(
              padding: const EdgeInsets.symmetric(horizontal: 12.0),
              itemCount: _log.length,
              itemBuilder: (context, index) {
                return Text(
                  '${index + 1}. ${_log[index]}',
                  style: const TextStyle(fontFamily: 'monospace', fontSize: 13),
                );
              },
            ),
          ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    print('dispose aufgerufen'); // ignore: avoid_print
    // Hinweis: setState darf hier nicht mehr aufgerufen werden,
    // da das Widget bereits aus dem Baum entfernt wird.
    // Der Eintrag wird deshalb direkt zur Liste hinzugefügt (nur für Konsolen-Sichtbarkeit).

    // Freigabe von Ressourcen
    super.dispose();
  }
}
