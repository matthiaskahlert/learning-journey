// Entwickle eine einfache Flutter-App, die eine Benutzeroberfläche mit verschiedenen Buttons und einem Eingabefeld bietet. Die App soll folgende Funktionalitäten haben:

// a) Erstelle ein Layout mit einem Column-Widget, das ein TextField und vier Buttons enthält: einen TextButton, einen ElevatedButton, einen OutlinedButton und einen FloatingActionButton. Jeder Button soll eine eindeutige Aktion durchführen, wenn er gedrückt wird (z.B. das Anzeigen einer Snackbar mit einer Nachricht, die den Typ des gedrückten Buttons angibt).

// b) Das TextField soll für die Eingabe eines Namens verwendet werden. Sobald der Name eingegeben und ein spezieller Button (wähle einen der vier Buttons aus) gedrückt wird, soll eine Begrüßungsnachricht mit dem eingegebenen Namen in einer Snackbar angezeigt werden.

// c) Passe das Aussehen des ElevatedButton an, indem du die Hintergrundfarbe, die Textfarbe und den Innenabstand (Padding) änderst. Für den OutlinedButton definiere einen Rand mit einer spezifischen Farbe und Breite.

import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('Übungs-App')),
        body: MyCustomForm(),
        floatingActionButton: FloatingActionButton(
          onPressed: () {
            // Aktion für FloatingActionButton
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('FloatingActionButton wurde gedrückt')),
            );
          },
          child: Icon(Icons.add),
        ),
      ),
    );
  }
}

class MyCustomForm extends StatefulWidget {
  const MyCustomForm({Key? key}) : super(key: key);

  @override
  _MyCustomFormState createState() => _MyCustomFormState();
}

class _MyCustomFormState extends State<MyCustomForm> {
  final _controller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        TextField(
          controller: _controller,
          decoration: InputDecoration(
            labelText: 'Name',
            hintText: 'Gib deinen Namen ein',
          ),
        ),
        TextButton(
          onPressed: () {
            // Aktion für TextButton
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('TextButton wurde gedrückt')),
            );
          },
          child: Text('Text Button'),
        ),
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.blue, // Hintergrundfarbe
            foregroundColor: Colors.white, // Textfarbe
            padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
          ),
          onPressed: () {
            // Aktion für ElevatedButton
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('ElevatedButton wurde gedrückt')),
            );
          },
          child: Text('Elevated Button'),
        ),
        OutlinedButton(
          style: OutlinedButton.styleFrom(
            side: BorderSide(color: Colors.green, width: 2),
          ),
          onPressed: () {
            // Aktion für OutlinedButton
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('OutlinedButton wurde gedrückt')),
            );
          },
          child: Text('Outlined Button'),
        ),
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: const Color.fromARGB(
              255,
              77,
              255,
              1,
            ), // Hintergrundfarbe
            foregroundColor: const Color.fromARGB(
              255,
              255,
              255,
              255,
            ), // Textfarbe
            padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
          ),
          onPressed: () {
            // Aktion für speziellen Button zur Begrüßung
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('Hallo, ${_controller.text}!')),
            );
          },
          child: Text('Sag Hallo'),
        ),
      ],
    );
  }
}
