// Entwickle eine Flutter-Anwendung für eine fiktive Bibliothek, die es Benutzern ermöglicht,
// Bücher zu durchsuchen, auszuleihen und Bewertungen abzugeben.
// Die Anwendung soll folgende Funktionalitäten umfassen:

// a) Erstelle eine Startseite (HomePage) mit einem AppBar, der den Titel "Bibliotheks-App" trägt,
// und einem Body, der zwei Buttons enthält: "Bücher durchsuchen" und "Meine Ausleihen".
// Verwende für die Buttons ElevatedButton.

// b) Implementiere eine Seite BrowseBooksPage, auf der Benutzer eine Liste von Büchern sehen können.
// Jedes Buch soll als Karte (Card) dargestellt werden, die den Titel des Buches,
// den Autor und einen Button "Ausleihen" enthält.
// Beim Klicken auf "Ausleihen" soll ein Dialog erscheinen, der den Benutzer fragt,
// ob er das Buch ausleihen möchte. Bei Bestätigung soll eine Snackbar
// mit der Nachricht "Buch ausgeliehen" erscheinen.

// c) Erstelle eine Seite MyLoansPage, die alle vom Benutzer ausgeliehenen Bücher anzeigt.
// Ähnlich wie auf der BrowseBooksPage sollen die Bücher als Karten dargestellt werden,
// jedoch mit einem zusätzlichen Button "Zurückgeben".
// Beim Klicken auf "Zurückgeben" soll eine Snackbar mit der Nachricht "Buch zurückgegeben" erscheinen.

// d) Füge eine Funktionalität hinzu, um Bewertungen zu Büchern abzugeben.
// Nach dem Ausleihen eines Buches soll ein Dialog erscheinen, der den Benutzer auffordert,
// das Buch zu bewerten (1 bis 5 Sterne).
// Speichere die Bewertung und zeige sie auf der BrowseBooksPage unter dem entsprechenden Buch an.

// e) Implementiere Navigation und Routing zwischen den Seiten.
// Verwende Named Routes für die Navigation. Stelle sicher, dass Parameter
// (wie z.B. das ausgeliehene Buch) zwischen den Routen übergeben werden können.

import 'package:flutter/material.dart';

void main() {
  runApp(const BibliothekApp());
}

class Buch {
  final String id;
  final String titel;
  final String autor;
  final String kategorie;

  const Buch({
    required this.id,
    required this.titel,
    required this.autor,
    required this.kategorie,
  });
}

// State wird sauber gekapselt um daten und UI zu trennen, damit die Seiten nicht direkt miteinander kommunizieren müssen
class BibliothekState {
  final List<Buch> ausgelieheneBuecher;
  final Map<String, int> bewertungen;

  BibliothekState({
    required List<Buch> ausgelieheneBuecher,
    required Map<String, int> bewertungen,
  }) : ausgelieheneBuecher = List<Buch>.unmodifiable(ausgelieheneBuecher),
       bewertungen = Map<String, int>.unmodifiable(bewertungen);

  factory BibliothekState.empty() {
    return BibliothekState(
      ausgelieheneBuecher: const [],
      bewertungen: const {},
    );
  }

  BibliothekState copy() {
    return BibliothekState(
      ausgelieheneBuecher: List<Buch>.from(ausgelieheneBuecher),
      bewertungen: Map<String, int>.from(bewertungen),
    );
  }

  BibliothekState copyWith({
    List<Buch>? ausgelieheneBuecher,
    Map<String, int>? bewertungen,
  }) {
    return BibliothekState(
      ausgelieheneBuecher:
          ausgelieheneBuecher ?? List<Buch>.from(this.ausgelieheneBuecher),
      bewertungen: bewertungen ?? Map<String, int>.from(this.bewertungen),
    );
  }
}

// Bücherliste aus bibliothek_dashboard
final List<Buch> buecherListe = [
  Buch(
    id: '1',
    titel: 'Dune',
    autor: 'Frank Herbert',
    kategorie: 'Science-Fiction',
  ),
  Buch(
    id: '2',
    titel: 'Dune Messiah',
    autor: 'Frank Herbert',
    kategorie: 'Science-Fiction',
  ),
  Buch(
    id: '3',
    titel: 'Der Herr der Ringe',
    autor: 'J.R.R. Tolkien',
    kategorie: 'Fantasy',
  ),
  Buch(
    id: '4',
    titel: 'Harry Potter und der Stein der Weisen',
    autor: 'J.K. Rowling',
    kategorie: 'Fantasy',
  ),
  Buch(id: '5', titel: '1984', autor: 'George Orwell', kategorie: 'Dystopie'),
  Buch(
    id: '6',
    titel: 'Der Alchimist',
    autor: 'Paulo Coelho',
    kategorie: 'Philosophie',
  ),
  Buch(
    id: '7',
    titel: 'Die Verwandlung',
    autor: 'Franz Kafka',
    kategorie: 'Klassiker',
  ),
  Buch(
    id: '8',
    titel: 'Der kleine Prinz',
    autor: 'Antoine de Saint-Exupéry',
    kategorie: 'Klassiker',
  ),
];

// gemeinsamer card-builder für beide seiten
Widget buildBuchCard(
  Buch buch,
  int? bewertung,
  VoidCallback actionButton,
  String actionButtonLabel,
  bool actionDisabled,
  ThemeData theme,
) {
  return Card(
    margin: const EdgeInsets.only(bottom: 12),
    child: Padding(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            buch.titel,
            style: theme.textTheme.titleMedium?.copyWith(
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 4),
          Text('Autor: ${buch.autor}', style: theme.textTheme.bodyMedium),
          Text(
            'Kategorie: ${buch.kategorie}',
            style: theme.textTheme.bodySmall,
          ),
          if (bewertung != null) ...[
            const SizedBox(height: 8),
            Row(
              children: [
                ...List.generate(
                  5,
                  (i) => Icon(
                    i < bewertung ? Icons.star : Icons.star_border,
                    color: Colors.amber,
                    size: 18,
                  ),
                ),
                const SizedBox(width: 6),
                Text('$bewertung/5 Sternen', style: theme.textTheme.bodySmall),
              ],
            ),
          ],
          const SizedBox(height: 12),
          ElevatedButton(
            onPressed: actionDisabled ? null : actionButton,
            child: Text(actionButtonLabel),
          ),
        ],
      ),
    ),
  );
}

class BibliothekApp extends StatelessWidget {
  const BibliothekApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Bibliotheks-App',
      theme: ThemeData(
        colorSchemeSeed: const Color.fromARGB(255, 43, 0, 255),
        useMaterial3: true,
      ),
      initialRoute: '/',
      routes: {
        // kleine route-map: name -> page
        '/': (context) => const HomePageHost(),
        '/browse': (context) => const BrowseBooksPage(),
        '/loans': (context) => const MyLoansPage(),
      },
    );
  }
}

class HomePageHost extends StatefulWidget {
  const HomePageHost({super.key});

  @override
  State<HomePageHost> createState() => _HomePageHostState();
}

class _HomePageHostState extends State<HomePageHost> {
  BibliothekState _state = BibliothekState.empty();

  void _updateState(BibliothekState nextState) {
    setState(() {
      _state = nextState.copy();
    });
  }

  @override
  Widget build(BuildContext context) {
    return HomePage(state: _state, onStateChanged: _updateState);
  }
}

// a) Startseite
class HomePage extends StatelessWidget {
  final BibliothekState state;
  final ValueChanged<BibliothekState> onStateChanged;

  const HomePage({
    super.key,
    required this.state,
    required this.onStateChanged,
  });

  Future<void> _oeffneBrowse(BuildContext context) async {
    final result = await Navigator.pushNamed(
      context,
      '/browse',
      arguments: state.copy(),
    );

    // daten rüberschicken und geänderte daten wieder zurückholen
    if (context.mounted && result is BibliothekState) {
      onStateChanged(result);
    }
  }

  Future<void> _oeffneLoans(BuildContext context) async {
    final result = await Navigator.pushNamed(
      context,
      '/loans',
      arguments: state.copy(),
    );

    if (context.mounted && result is BibliothekState) {
      onStateChanged(result);
    }
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Scaffold(
      appBar: AppBar(title: const Text('Bibliotheks-App'), centerTitle: true),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              'Willkommen in den\nBücherhallen Hamburg',
              textAlign: TextAlign.center,
              style: theme.textTheme.headlineSmall?.copyWith(
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 48),
            ElevatedButton(
              // route + argumente (state) als paket
              onPressed: () => _oeffneBrowse(context),
              child: const Padding(
                padding: EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                child: Text('Bücher durchsuchen'),
              ),
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              // gleiches prinzip fuer meine ausleihen
              onPressed: () => _oeffneLoans(context),
              child: const Padding(
                padding: EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                child: Text('Meine Ausleihen'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

// b) BrowseBooksPage
class BrowseBooksPage extends StatefulWidget {
  const BrowseBooksPage({super.key});

  @override
  State<BrowseBooksPage> createState() => _BrowseBooksPageState();
}

class _BrowseBooksPageState extends State<BrowseBooksPage> {
  late BibliothekState _state;
  bool _initialisiert = false;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (_initialisiert) {
      return;
    }

    _state = (ModalRoute.of(context)!.settings.arguments as BibliothekState)
        .copy();
    _initialisiert = true;
  }

  void _zurueckMitState() {
    // aktualisierten daten werden zurückgegeben
    Navigator.pop(context, _state.copy());
  }

  void _zeigeBewertungsDialog(Buch buch) {
    int ausgewaehlterStern = 0;

    showDialog(
      context: context,
      builder: (BuildContext dialogContext) {
        return StatefulBuilder(
          builder: (context, setDialogState) {
            return AlertDialog(
              title: const Text('Buch bewerten'),
              content: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text('"${buch.titel}" bewerten:'),
                  const SizedBox(height: 16),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: List.generate(5, (index) {
                      return IconButton(
                        icon: Icon(
                          index < ausgewaehlterStern
                              ? Icons.star
                              : Icons.star_border,
                          color: Colors.amber,
                        ),
                        onPressed: () {
                          setDialogState(() => ausgewaehlterStern = index + 1);
                        },
                      );
                    }),
                  ),
                  if (ausgewaehlterStern > 0)
                    Text('$ausgewaehlterStern von 5 Sternen'),
                ],
              ),
              actions: [
                TextButton(
                  onPressed: () => Navigator.of(dialogContext).pop(),
                  child: const Text('Überspringen'),
                ),
                TextButton(
                  onPressed: ausgewaehlterStern == 0
                      ? null
                      : () {
                          setState(() {
                            final neueBewertungen = Map<String, int>.from(
                              _state.bewertungen,
                            );
                            neueBewertungen[buch.id] = ausgewaehlterStern;
                            _state = _state.copyWith(
                              bewertungen: neueBewertungen,
                            );
                          });
                          Navigator.of(dialogContext).pop();
                        },
                  child: const Text('Bewertung speichern'),
                ),
              ],
            );
          },
        );
      },
    );
  }

  void _zeigeAusleihDialog(Buch buch) {
    showDialog(
      context: context,
      builder: (BuildContext dialogContext) {
        return AlertDialog(
          title: const Text('Buch ausleihen?'),
          content: Text('Möchten Sie "${buch.titel}" ausleihen?'),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(dialogContext).pop(),
              child: const Text('Abbrechen'),
            ),
            TextButton(
              onPressed: () {
                setState(() {
                  _state = _state.copyWith(
                    ausgelieheneBuecher: [..._state.ausgelieheneBuecher, buch],
                  );
                });
                Navigator.of(dialogContext).pop();
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text('Buch ausgeliehen'),
                    duration: Duration(seconds: 2),
                  ),
                );
                _zeigeBewertungsDialog(buch);
              },
              child: const Text('Ausleihen'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, result) {
        if (!didPop) {
          _zurueckMitState();
        }
      },
      child: Scaffold(
        appBar: AppBar(
          leading: IconButton(
            icon: const Icon(Icons.arrow_back),
            onPressed: _zurueckMitState,
          ),
          title: const Text('Bücher durchsuchen'),
          actions: [
            IconButton(
              onPressed: () async {
                final result = await Navigator.pushNamed(
                  context,
                  '/loans',
                  arguments: _state.copy(),
                );

                if (!mounted) {
                  return;
                }
                if (result is BibliothekState) {
                  setState(() {
                    _state = result.copy();
                  });
                }
              },
              icon: const Icon(Icons.library_books),
              tooltip: 'Meine Ausleihen',
            ),
          ],
        ),
        body: ListView.builder(
          padding: const EdgeInsets.all(12),
          itemCount: buecherListe.length,
          itemBuilder: (context, index) {
            final buch = buecherListe[index];
            final bewertung = _state.bewertungen[buch.id];
            final istAusgeliehen = _state.ausgelieheneBuecher.contains(buch);
            return buildBuchCard(
              buch,
              bewertung,
              () => _zeigeAusleihDialog(buch),
              istAusgeliehen ? 'Bereits ausgeliehen' : 'Ausleihen',
              istAusgeliehen,
              theme,
            );
          },
        ),
      ),
    );
  }
}

// c) MyLoansPage
class MyLoansPage extends StatefulWidget {
  const MyLoansPage({super.key});

  @override
  State<MyLoansPage> createState() => _MyLoansPageState();
}

class _MyLoansPageState extends State<MyLoansPage> {
  late BibliothekState _state;
  bool _initialisiert = false;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (_initialisiert) {
      return;
    }

    _state = (ModalRoute.of(context)!.settings.arguments as BibliothekState)
        .copy();
    _initialisiert = true;
  }

  void _zurueckMitState() {
    Navigator.pop(context, _state.copy());
  }

  void _zurueckgeben(Buch buch) {
    setState(() {
      final neueAusleihen = List<Buch>.from(_state.ausgelieheneBuecher)
        ..remove(buch);
      _state = _state.copyWith(ausgelieheneBuecher: neueAusleihen);
    });
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Buch zurückgegeben'),
        duration: Duration(seconds: 2),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final aktuelleAusleihen = _state.ausgelieheneBuecher;

    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, result) {
        if (!didPop) {
          _zurueckMitState();
        }
      },
      child: Scaffold(
        appBar: AppBar(
          leading: IconButton(
            icon: const Icon(Icons.arrow_back),
            onPressed: _zurueckMitState,
          ),
          title: const Text('Meine Ausleihen'),
        ),
        body: aktuelleAusleihen.isEmpty
            ? const Center(
                child: Text(
                  'Keine Bücher ausgeliehen.',
                  style: TextStyle(fontSize: 16),
                ),
              )
            : ListView.builder(
                padding: const EdgeInsets.all(12),
                itemCount: aktuelleAusleihen.length,
                itemBuilder: (context, index) {
                  final buch = aktuelleAusleihen[index];
                  final bewertung = _state.bewertungen[buch.id];
                  return buildBuchCard(
                    buch,
                    bewertung,
                    () => _zurueckgeben(buch),
                    'Zurückgeben',
                    false,
                    theme,
                  );
                },
              ),
      ),
    );
  }
}
