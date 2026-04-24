import 'package:flutter/material.dart';

class CounterThreePage extends StatelessWidget {
  const CounterThreePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Flutter Demo')),
      body: const Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            WillkommenWidget(),
            SizedBox(height: 20),
            ZaehlerWidget(),
          ],
        ),
      ),
    );
  }
}

class WillkommenWidget extends StatelessWidget {
  const WillkommenWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return const Text(
      'Willkommen in Flutter!',
      style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
    );
  }
}

class ZaehlerWidget extends StatefulWidget {
  const ZaehlerWidget({super.key});

  @override
  State<ZaehlerWidget> createState() => _ZaehlerWidgetState();
}

class _ZaehlerWidgetState extends State<ZaehlerWidget> {
  int _zaehler = 0;

  @override
  void initState() {
    super.initState();
    print('ZaehlerWidget wird initialisiert'); // ignore: avoid_print
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Text('Zaehler: $_zaehler', style: const TextStyle(fontSize: 22)),
        ElevatedButton(
          onPressed: () {
            setState(() {
              _zaehler++;
            });
          },
          child: const Text('Erhoehen'),
        ),
      ],
    );
  }

  @override
  void dispose() {
    print('ZaehlerWidget wird beseitigt'); // ignore: avoid_print
    super.dispose();
  }
}
