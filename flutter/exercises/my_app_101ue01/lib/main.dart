/* 
Entwickle eine einfache Flutter-Anwendung, die aus drei Bildschirmen besteht: 
einem Startbildschirm, einem Detailbildschirm und einem Bestätigungsbildschirm. 
Der Startbildschirm soll ein Formular mit einem Eingabefeld für einen Namen 
und einem Button enthalten. 
Beim Klick auf den Button soll der eingegebene Name an den Detailbildschirm übergeben 
werden, der diesen Name anzeigt und einen Button enthält,
um zum Bestätigungsbildschirm zu navigieren.
Der Bestätigungsbildschirm soll eine Nachricht anzeigen,
dass der Prozess erfolgreich war, und einen Button, um zur Startseite zurückzukehren. 
Implementiere die Navigation zwischen diesen Bildschirmen 
unter Verwendung des Navigator-Stacks. 
Stelle sicher, dass das Formular im Startbildschirm vor der Navigation validiert wird, 
sodass der Name nicht leer ist.

 */

import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Navigator Uebung',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
      ),
      home: const StartScreen(),
    );
  }
}

class StartScreen extends StatefulWidget {
  const StartScreen({super.key});

  @override
  State<StartScreen> createState() => _StartScreenState();
}

class _StartScreenState extends State<StartScreen> {
  final _formKey = GlobalKey<FormState>();
  final TextEditingController _controller = TextEditingController();

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _goToDetailScreen() {
    if (_formKey.currentState!.validate()) {
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => DetailScreen(name: _controller.text.trim()),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Startbildschirm')),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Form(
            key: _formKey,
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: <Widget>[
                TextFormField(
                  controller: _controller,
                  decoration: const InputDecoration(
                    labelText: 'Name',
                    hintText: 'Gib deinen Namen ein',
                    border: OutlineInputBorder(),
                  ),
                  validator: (value) {
                    if (value == null || value.trim().isEmpty) {
                      return 'Bitte einen Namen eingeben';
                    }
                    return null;
                  },
                ),
                const SizedBox(height: 16),
                ElevatedButton(
                  onPressed: _goToDetailScreen,
                  child: const Text('Weiter zum Detailbildschirm'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class DetailScreen extends StatelessWidget {
  final String name;

  const DetailScreen({super.key, required this.name});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Detailbildschirm')),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: <Widget>[
            Text('Hallo, $name!'),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => const ConfirmationScreen(),
                  ),
                );
              },
              child: const Text('Zum Bestaetigungsbildschirm'),
            ),
          ],
        ),
      ),
    );
  }
}

class ConfirmationScreen extends StatelessWidget {
  const ConfirmationScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Bestaetigungsbildschirm')),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: <Widget>[
            const Text('Prozess erfolgreich!'),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: () {
                Navigator.pushAndRemoveUntil(
                  context,
                  MaterialPageRoute(builder: (context) => const StartScreen()),
                  (Route<dynamic> route) => false,
                );
              },
              child: const Text('Zurueck zum Startbildschirm'),
            ),
          ],
        ),
      ),
    );
  }
}
