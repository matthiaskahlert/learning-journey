import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';

/* Entwickle eine Flutter-App, die ein Dashboard für eine fiktive Bibliothek darstellt. 
Das Dashboard soll folgende Elemente enthalten: eine Kopfzeile mit dem Namen der Bibliothek,
 eine horizontale Liste von Buchkategorien, 
 eine vertikale Liste von Büchern der ausgewählten Kategorie 
 und ein Fußbereich mit Kontaktdaten der Bibliothek. 
 Die App soll responsive sein, sodass sie sowohl auf einem Tablet 
 als auch auf einem Smartphone gut aussieht. 
 Berücksichtige dabei die Constraints und deren Auswirkungen auf die Widgets. 
 Verwende keine interaktiven Elemente wie Buttons.

a) Erstelle die Grundstruktur der App mit einem Scaffold, der eine AppBar 
und einen Body enthält.

b) Implementiere eine horizontale ListView für die Buchkategorien im oberen Teil des Body.
 Jedes Element der Liste soll ein Container sein, der den Namen der Kategorie enthält.

c) Implementiere unter der Liste der Kategorien eine vertikale ListView, 
die Bücher der ausgewählten Kategorie anzeigt. 
Jedes Buch soll in einem Container dargestellt werden, der den Buchtitel 
und den Autor anzeigt.

d) Stelle sicher, dass die App responsive ist, 
indem du MediaQuery und Flexible Widgets nutzt, 
um die Darstellung auf verschiedenen Bildschirmgrößen anzupassen.

 */
void main() {
  runApp(const BibliothekDashboardApp());
}

class BibliothekDashboardApp extends StatelessWidget {
  const BibliothekDashboardApp({super.key});

  static final ScrollBehavior _scrollVerhalten = const MaterialScrollBehavior()
      .copyWith(
        dragDevices: <PointerDeviceKind>{
          PointerDeviceKind.touch,
          PointerDeviceKind.mouse,
          PointerDeviceKind.stylus,
          PointerDeviceKind.invertedStylus,
          PointerDeviceKind.unknown,
        },
      );

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Bibliothek Dashboard',
      theme: ThemeData(colorSchemeSeed: Colors.teal, useMaterial3: true),
      scrollBehavior: _scrollVerhalten,
      home: const BibliothekDashboardPage(),
    );
  }
}

class BibliothekDashboardPage extends StatefulWidget {
  const BibliothekDashboardPage({super.key});

  @override
  State<BibliothekDashboardPage> createState() =>
      _BibliothekDashboardPageState();
}

class _BibliothekDashboardPageState extends State<BibliothekDashboardPage> {
  int _kategorieIndex = 0;

  static const List<String> kategorien = [
    'Science-Fiction',
    'Fantasy',
    'Dystopie',
    'Philosophie',
    'Python Grundlagen',
    'Python Vertiefung',
  ];

  static const Map<String, List<Buch>> buecherNachKategorie = {
    'Science-Fiction': [
      Buch(titel: 'Dune', autor: 'Frank Herbert'),
      Buch(titel: 'Dune Messiah', autor: 'Frank Herbert'),
      Buch(titel: 'Children of Dune', autor: 'Frank Herbert'),
      Buch(titel: 'God Emperor of Dune', autor: 'Frank Herbert'),
      Buch(titel: 'Heretics of Dune', autor: 'Frank Herbert'),
      Buch(titel: 'Chapterhouse: Dune', autor: 'Frank Herbert'),
    ],
    'Fantasy': [
      Buch(titel: 'Der Herr der Ringe', autor: 'JRR Tolkien'),
      Buch(titel: 'Harry Potter und der Stein der Weisen', autor: 'J.K. Rowling',),
    ],
    'Dystopie': [Buch(titel: '1984', autor: 'George Orwell')],
    'Philosophie': [Buch(titel: 'Der Alchimist', autor: 'Paulo Coelho')],
    'Python Grundlagen': [
      Buch(titel: 'Python lernen', autor: 'Max Mustermann'),
      Buch(titel: 'Python lernen', autor: 'John Doe'),
      Buch(titel: 'Python lernen', autor: 'Anna Schmidt'),
      Buch(titel: 'Einfuehrung in die Informatik', autor: 'Peter Mueller'),
      Buch(titel: 'Einfuehrung in die Informatik', autor: 'Laura Becker'),
      Buch(titel: 'Objektorientierte Programmierung', autor: 'Thomas Klein'),
      Buch(titel: 'Objektorientierte Programmierung', autor: 'Erika Musterfrau',),
    ],
    'Python Vertiefung': [
      Buch(titel: 'Fortgeschrittene Python-Programmierung', autor: 'Erika Musterfrau',),
      Buch(titel: 'Fortgeschrittene Python-Programmierung', autor: 'Max Mustermann',),
      Buch(titel: 'Datenstrukturen und Algorithmen', autor: 'Peter Mueller'),
      Buch(titel: 'Datenstrukturen und Algorithmen', autor: 'Julia Weber'),
      Buch(titel: 'Webentwicklung mit Python', autor: 'John Doe'),
      Buch(titel: 'Webentwicklung mit Python', autor: 'Anna Schmidt'),
      Buch(titel: 'Datenanalyse mit Python', autor: 'Max Mustermann'),
      Buch(titel: 'Datenanalyse mit Python', autor: 'Laura Becker'),
    ],
  };

  double _abstand(double klein, double gross, bool istTablet) {
    return istTablet ? gross : klein;
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final bool istTablet = MediaQuery.of(context).size.width >= 700;
    final String ausgewaehlteKategorie =
        kategorien[_kategorieIndex];
    final List<Buch> ausgewaehlteBuecher =
        buecherNachKategorie[ausgewaehlteKategorie] ?? const [];

    return Scaffold(
      appBar: AppBar(
        title: const Text('Bücherhallen Hamburg'),
        centerTitle: true,
      ),
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 1000),
            child: Padding(
              padding: EdgeInsets.symmetric(
                horizontal: istTablet ? 24 : 12,
                vertical: istTablet ? 16 : 10,
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Padding(
                    padding: const EdgeInsets.only(bottom: 8),
                    child: Text(
                      'Kategorien',
                      style: theme.textTheme.titleMedium,
                    ),
                  ),
                  SizedBox(
                    height: istTablet ? 90 : 72,
                    child: ListView.separated(
                      scrollDirection: Axis.horizontal,
                      itemCount: kategorien.length,
                      separatorBuilder: (_, separatorIndex) =>
                          const SizedBox(width: 10),
                      itemBuilder: (context, index) {
                        return KategorieElement(
                          name: kategorien[index],
                          istAusgewaehlt: index == _kategorieIndex,
                          istTablet: istTablet,
                          onTap: () {
                            setState(() {
                              _kategorieIndex = index;
                            });
                          },
                        );
                      },
                    ),
                  ),
                  SizedBox(height: _abstand(12, 18, istTablet)),
                  Text(
                    'Bücher in "$ausgewaehlteKategorie"',
                    style: theme.textTheme.titleMedium,
                  ),
                  const SizedBox(height: 8),
                  Expanded(
                    flex: istTablet ? 8 : 7,
                    child: ListView.separated(
                      itemCount: ausgewaehlteBuecher.length,
                      separatorBuilder: (_, separatorIndex) =>
                          SizedBox(height: istTablet ? 12 : 8),
                      itemBuilder: (context, index) {
                        return BuchElement(
                          buch: ausgewaehlteBuecher[index],
                          istTablet: istTablet,
                        );
                      },
                    ),
                  ),
                  SizedBox(height: _abstand(10, 12, istTablet)),
                  const KontaktFooter(),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}

class Buch {
  final String titel;
  final String autor;

  const Buch({required this.titel, required this.autor});
}

class KategorieElement extends StatelessWidget {
  final String name;
  final bool istAusgewaehlt;
  final VoidCallback onTap;
  final bool istTablet;

  const KategorieElement({
    super.key,
    required this.name,
    required this.istAusgewaehlt,
    required this.onTap,
    required this.istTablet,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return InkWell(
      borderRadius: BorderRadius.circular(14),
      onTap: onTap,
      child: Container(
        constraints: BoxConstraints(
          minWidth: istTablet ? 150 : 120,
          maxWidth: istTablet ? 220 : 170,
        ),
        alignment: Alignment.center,
        padding: const EdgeInsets.symmetric(horizontal: 14),
        decoration: BoxDecoration(
          color: istAusgewaehlt
              ? theme.colorScheme.primaryContainer
              : theme.colorScheme.surfaceContainerHighest,
          borderRadius: BorderRadius.circular(14),
        ),
        child: Text(
          name,
          textAlign: TextAlign.center,
          style: theme.textTheme.titleSmall,
        ),
      ),
    );
  }
}

class BuchElement extends StatelessWidget {
  final Buch buch;
  final bool istTablet;

  const BuchElement({super.key, required this.buch, required this.istTablet});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Container(
      padding: EdgeInsets.all(istTablet ? 16 : 12),
      decoration: BoxDecoration(
        color: theme.colorScheme.surfaceContainerLow,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: theme.colorScheme.outlineVariant),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(buch.titel, style: theme.textTheme.titleSmall),
          const SizedBox(height: 4),
          Text('Autor: ${buch.autor}', style: theme.textTheme.bodyMedium),
        ],
      ),
    );
  }
}

class KontaktFooter extends StatelessWidget {
  const KontaktFooter({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final bool istTablet = MediaQuery.of(context).size.width >= 700;

    return Container(
      width: double.infinity,
      padding: EdgeInsets.symmetric(
        horizontal: istTablet ? 24 : 16,
        vertical: istTablet ? 14 : 10,
      ),
      color: theme.colorScheme.secondaryContainer,
      child: Text(
        'Kontakt: Bücherhallen Hamburg | Tel: 040 123456789 | E-Mail: info@bib-hh.de',
        textAlign: TextAlign.center,
        style: theme.textTheme.bodySmall,
      ),
    );
  }
}
