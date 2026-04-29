// Entwickle eine Flutter-Anwendung für ein kleines Umfrage-Tool, das folgende Anforderungen erfüllt:

// a) Erstelle eine Startseite, die einen Begrüßungstext und einen Button enthält. Der Button soll "Zur Umfrage" lauten und den Nutzer zu einer neuen Seite mit der Umfrage navigieren, ohne die Verwendung von Navigation und Routing. Nutze stattdessen einen Zustandsmanagement-Ansatz, um zwischen den Ansichten zu wechseln.

// b) Auf der Umfrageseite, implementiere ein Formular mit mindestens drei verschiedenen Arten von Eingabefeldern (z.B. Textfeld für den Namen, Dropdown für das Alter und Radio Buttons oder Checkboxen für Geschlecht). Jedes Eingabefeld soll mit entsprechenden Labels und Hinweistexten versehen sein.

// c) Füge Validierungen für jedes Eingabefeld hinzu. Beispielsweise soll das Textfeld für den Namen nicht leer sein, das Alter soll aus der Dropdown-Liste ausgewählt werden, und mindestens eine Option bei den Geschlechtsauswahlen soll ausgewählt sein.

// d) Implementiere einen "Absenden"-Button am Ende des Formulars. Beim Klicken soll geprüft werden, ob alle Eingaben valide sind. Falls ja, zeige eine Bestätigungsnachricht in einem Dialogfenster an, das die eingegebenen Daten zusammenfasst. Falls nicht, zeige Fehlermeldungen an den entsprechenden Stellen im Formular an.

// e) Integriere Gestensteuerung, indem du ein "Doppeltippen" auf den Hintergrund der Umfrageseite implementierst, welches den Nutzer zurück zur Startseite bringt.

import 'package:flutter/material.dart';

void main() {
  runApp(const SurveyApp());
}

class SurveyApp extends StatelessWidget {
  const SurveyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Umfrage-Tool',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const MainScreen(),
    );
  }
}

// Modell für die Umfragedaten
class SurveyData {
  String? name;
  int? age;
  String? gender;

  SurveyData({this.name, this.age, this.gender});
}

// Haupt-Widget für die App, verwaltet den Zustand

class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  // a) Zustandsmanagement für Wechsel zwischen Start- und Umfrageseite
  bool _showSurvey = false;
  final SurveyData _surveyData = SurveyData();

  void _toggleView() {
    setState(() {
      _showSurvey = !_showSurvey;
    });
  }

  @override
  Widget build(BuildContext context) {
    // Je nach Zustand entweder Startseite oder Umfrageseite anzeigen
    return _showSurvey
        ? SurveyPage(onBack: _toggleView, surveyData: _surveyData)
        : HomePage(onSurveyStart: _toggleView);
  }
}

// a) Startseite mit Begrüßungstext und Button
class HomePage extends StatelessWidget {
  final VoidCallback onSurveyStart;

  const HomePage({super.key, required this.onSurveyStart});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Umfrage-Tool')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Willkommen zur Umfrage in der SurveyApp!',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 30),
            ElevatedButton(
              onPressed: onSurveyStart,
              child: const Text('Zur Umfrage'),
            ),
          ],
        ),
      ),
    );
  }
}

// b, c, d, e) Umfrageseite mit Formular, Validierung, Button und Gestensteuerung
class SurveyPage extends StatefulWidget {
  final VoidCallback onBack;
  final SurveyData surveyData;

  const SurveyPage({
    super.key,
    required this.onBack,
    required this.surveyData,
  });

  @override
  State<SurveyPage> createState() => _SurveyPageState();
}

class _SurveyPageState extends State<SurveyPage> {
  final _formKey = GlobalKey<FormState>();
  final TextEditingController _nameController = TextEditingController();
  String? _selectedGender;
  int? _selectedAge;
  bool _showGenderError = false;

  // Liste für Altersoptionen generieren
  List<DropdownMenuItem<int>> _getAgeItems() {
    List<DropdownMenuItem<int>> items = [];
    for (int i = 18; i <= 100; i++) {
      items.add(DropdownMenuItem<int>(value: i, child: Text(i.toString())));
    }
    return items;
  }

  // Dialog mit Zusammenfassung anzeigen
  void _showSummaryDialog() {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text('Umfrage abgeschlossen'),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text('Name: ${_nameController.text}'),
              Text('Alter: $_selectedAge'),
              Text('Geschlecht: $_selectedGender'),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
                widget.onBack(); // Zurück zur Startseite
              },
              child: const Text('OK'),
            ),
          ],
        );
      },
    );
  }

  @override
  void dispose() {
    _nameController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Umfrage ausfüllen')),
      // e) GestureDetector für Doppeltippen
      body: GestureDetector(
        onDoubleTap: widget.onBack, // Doppeltippen führt zurück zur Startseite
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Form(
            key: _formKey,
            child: ListView(
              children: [
                // b) TextField für den Namen
                TextFormField(
                  controller: _nameController,
                  decoration: const InputDecoration(
                    labelText: 'Name',
                    hintText: 'Gib deinen Namen ein',
                    border: OutlineInputBorder(),
                  ),
                  // c) Validierung für Name
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Bitte gib deinen Namen ein';
                    }
                    return null;
                  },
                  onSaved: (value) {
                    widget.surveyData.name = value;
                  },
                ),
                const SizedBox(height: 20),

                // b) Dropdown für das Alter
                DropdownButtonFormField<int>(
                  initialValue: _selectedAge,
                  decoration: const InputDecoration(
                    labelText: 'Alter',
                    hintText: 'Wähle dein Alter',
                    border: OutlineInputBorder(),
                  ),
                  items: _getAgeItems(),
                  onChanged: (value) {
                    setState(() {
                      _selectedAge = value;
                    });
                  },
                  // c) Validierung für Alter
                  validator: (value) {
                    if (value == null) {
                      return 'Bitte wähle dein Alter';
                    }
                    return null;
                  },
                  onSaved: (value) {
                    widget.surveyData.age = value;
                  },
                ),
                const SizedBox(height: 20),

                // b) Checkboxen für Geschlecht (genau eine Auswahl)
                const Text('Geschlecht:', style: TextStyle(fontSize: 16)),
                CheckboxListTile(
                  title: const Text('Männlich'),
                  value: _selectedGender == 'Männlich',
                  onChanged: (value) {
                    if (value == true) {
                      setState(() {
                        _selectedGender = 'Männlich';
                        _showGenderError = false;
                      });
                    }
                  },
                ),
                CheckboxListTile(
                  title: const Text('Weiblich'),
                  value: _selectedGender == 'Weiblich',
                  onChanged: (value) {
                    if (value == true) {
                      setState(() {
                        _selectedGender = 'Weiblich';
                        _showGenderError = false;
                      });
                    }
                  },
                ),
                CheckboxListTile(
                  title: const Text('Divers'),
                  value: _selectedGender == 'Divers',
                  onChanged: (value) {
                    if (value == true) {
                      setState(() {
                        _selectedGender = 'Divers';
                        _showGenderError = false;
                      });
                    }
                  },
                ),
                // c) Fehlermeldung für Geschlecht
                if (_showGenderError)
                  const Padding(
                    padding: EdgeInsets.only(left: 16.0),
                    child: Text(
                      'Bitte wähle ein Geschlecht',
                      style: TextStyle(color: Colors.red, fontSize: 12),
                    ),
                  ),
                const SizedBox(height: 30),

                // d) Absenden-Button
                ElevatedButton(
                  onPressed: () {
                    // Überprüfen ob Geschlecht ausgewählt wurde (manuell, da nicht Teil von FormField)
                    final bool hasGender = _selectedGender != null;
                    setState(() {
                      _showGenderError = !hasGender;
                    });

                    // Alle Validierungen prüfen
                    if (_formKey.currentState!.validate() && hasGender) {
                      _formKey.currentState!.save();
                      widget.surveyData.gender = _selectedGender;

                      // Dialog mit Zusammenfassung anzeigen
                      _showSummaryDialog();
                    }
                  },
                  child: const Text('Umfrage absenden'),
                ),
                const SizedBox(height: 20),

                // Hinweis für Gestensteuerung
                const Text(
                  'Hinweis: Doppeltippe auf den Hintergrund, um zur Startseite zurückzukehren.',
                  style: TextStyle(fontSize: 12, fontStyle: FontStyle.italic),
                  textAlign: TextAlign.center,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
