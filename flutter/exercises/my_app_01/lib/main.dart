// Entwickle eine Flutter-Anwendung, die folgende Anforderungen erfüllt:

// a) Erstelle ein Stateful Widget namens FeedbackCounter, das einen Zähler für Benutzerfeedbacks anzeigt. Dieses Widget soll einen Button enthalten, der bei jedem Klick den Zähler um eins erhöht.

// b) Implementiere ein Stateless Widget namens WelcomeMessage, das eine Begrüßungsnachricht zusammen mit dem aktuellen Datum anzeigt. Verwende das DateFormat von intl Paket, um das Datum im Format "dd.MM.yyyy" darzustellen.

// c) Integriere beide Widgets in die Hauptansicht deiner Anwendung. Platziere das FeedbackCounter Widget oben und das WelcomeMessage Widget darunter.

// d) Stelle sicher, dass deine Anwendung das Material Design verwendet. Füge der App-Bar einen Titel hinzu, der "Feedback App" lautet, und verwende für den Button im FeedbackCounter Widget ein Icon anstelle von Text.

import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Feedback App',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: Scaffold(
        appBar: AppBar(title: Text('Feedback App')),
        body: Column(children: <Widget>[FeedbackCounter(), WelcomeMessage()]),
      ),
    );
  }
}

class FeedbackCounter extends StatefulWidget {
  const FeedbackCounter({super.key});

  @override
  FeedbackCounterState createState() => FeedbackCounterState();
}

class FeedbackCounterState extends State<FeedbackCounter> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.all(20),
      child: Column(
        children: <Widget>[
          Text('Feedback Count: $_counter', style: TextStyle(fontSize: 20)),
          IconButton(icon: Icon(Icons.add), onPressed: _incrementCounter),
        ],
      ),
    );
  }
}

class WelcomeMessage extends StatelessWidget {
  const WelcomeMessage({super.key});

  @override
  Widget build(BuildContext context) {
    final String date = DateFormat('dd.MM.yyyy').format(DateTime.now());
    return Container(
      margin: EdgeInsets.all(20),
      child: Text('Welcome! Today is $date', style: TextStyle(fontSize: 20)),
    );
  }
}
