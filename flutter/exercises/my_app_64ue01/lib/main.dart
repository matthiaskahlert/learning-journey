// Entwickle eine einfache Flutter-App, die eine Liste von Einträgen anzeigt. Jeder Eintrag soll aus einem Titel und einer kurzen Beschreibung bestehen. Die App soll folgende Anforderungen erfüllen:

// a) Erstelle ein neues Flutter-Projekt in deiner Entwicklungsumgebung.

// b) Definiere ein Haupt-Widget, das ein Scaffold-Widget verwendet. Das Scaffold-Widget soll eine AppBar enthalten mit dem Titel "Meine Einträge".

// c) Im Body des Scaffold-Widgets, verwende ein ListView-Widget, um eine Liste von Einträgen anzuzeigen. Jeder Eintrag soll durch ein ListTile-Widget repräsentiert werden, das einen Titel und eine Untertitel enthält. Die Titel sollen "Eintrag 1", "Eintrag 2", "Eintrag 3" usw. lauten, und die Untertitel sollen eine kurze Beschreibung des jeweiligen Eintrags sein.

// d) Stelle sicher, dass deine App responsive Layouts unterstützt. Verwende MediaQuery, um die Größe des Bildschirms abzufragen und die Darstellung der Liste entsprechend anzupassen. Wenn der Bildschirm breit genug ist, soll die Liste in zwei Spalten angezeigt werden, ansonsten in einer Spalte.

// e) Dokumentiere den Code angemessen, um die Funktionen und die Struktur deiner App zu erklären.

import 'package:flutter/material.dart';

void main() {
  runApp(MeineApp());
}

class MeineApp extends StatelessWidget {
  const MeineApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('Meine Einträge')),
        body: ResponsiveListView(),
      ),
    );
  }
}

class ResponsiveListView extends StatelessWidget {
  const ResponsiveListView({super.key});

  @override
  Widget build(BuildContext context) {
    // Überprüfe die Größe des Bildschirms
    bool isWideScreen = MediaQuery.of(context).size.width > 600;

    // Erstelle eine Liste von Einträgen
    List<Widget> eintraege = List.generate(10, (index) {
      return ListTile(
        title: Text('Eintrag ${index + 1}'),
        subtitle: Text('Eine kurze Beschreibung des Eintrags ${index + 1}.'),
      );
    });

    // Entscheide, wie die Liste angezeigt werden soll, basierend auf der Bildschirmgröße
    if (isWideScreen) {
      // Anzeige in zwei Spalten, wenn der Bildschirm breit genug ist
      return GridView.count(crossAxisCount: 2, children: eintraege);
    } else {
      // Standardmäßige Anzeige in einer Spalte
      return ListView(children: eintraege);
    }
  }
}
