import 'package:flutter/material.dart';

class CounterTwoTitle extends StatelessWidget {
  const CounterTwoTitle({super.key});

  @override
  Widget build(BuildContext context) {
    // Dieses StatelessWidget zeigt nur einen festen Titel an.
    return const Text('Meine Zähler-App');
  }
}

class CounterTwoPage extends StatefulWidget {
  const CounterTwoPage({super.key});

  @override
  State<CounterTwoPage> createState() => _CounterTwoPageState();
}

class _CounterTwoPageState extends State<CounterTwoPage> {
  // Interner Zustand: startet bei 0 und wird per setState aktualisiert.
  int _counter = 0;

  void _incrementCounter() {
    // setState markiert das Widget für den Neuaufbau, damit der neue Wert sichtbar wird.
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const CounterTwoTitle()),
      body: Center(
        child: Column(
          // mainAxisSize.min: die Column nimmt nur so viel Platz ein wie nötig,
          // die Kinder werden dann vertikal zentriert – genau wie in Counter 1.
          mainAxisSize: MainAxisSize.min,
          children: [
            // Erklärender Absatz: zeigt dem Nutzer, was diese Seite demonstriert.
            const Padding(
              padding: EdgeInsets.symmetric(horizontal: 24.0),
              child: Text(
                'Dieses Beispiel zeigt ein StatefulWidget mit Zustandsverwaltung.\n'
                'Jeder Klick auf den Button erhöht den Zähler um 1.\n'
                'setState() sorgt dafür, dass Flutter das Widget neu zeichnet '
                'und der aktuelle Wert sofort sichtbar wird.',
                textAlign: TextAlign.center,
              ),
            ),
            const SizedBox(height: 24),
            // Anzeige des aktuellen Zählerstands.
            Text(
              'Zählerstand: $_counter',
              style: Theme.of(context).textTheme.headlineSmall,
            ),
            const SizedBox(height: 24),
            // FloatingActionButton im Body platziert, damit die Position
            // mit Counter 1 übereinstimmt (Button mittig, nicht unten rechts).
            FloatingActionButton(
              onPressed: _incrementCounter,
              // Bei jedem Klick wird _incrementCounter aufgerufen.
              child: const Icon(Icons.add),
            ),
          ],
        ),
      ),
    );
  }
}
