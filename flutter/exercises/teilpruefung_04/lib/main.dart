// Aufgabe

// Entwickle eine Flutter-App für ein lokales Lieferdienst-Unternehmen, das seinen Kunden ermöglicht,
// die Lieferung ihrer Bestellungen in Echtzeit zu verfolgen. Die App sollte folgende Funktionen beinhalten:

// a) Eine Startseite, die eine Übersicht über die verschiedenen Lieferoptionen bietet
// (z.B. Essen, Dokumente, Pakete). Nutze für jede Option ein Card-Widget mit einer kurzen Beschreibung.

// b) Eine Detailseite für jede Lieferoption, die nach dem Tippen auf eine der Optionen auf der Startseite erscheint.
// Diese Seite sollte Informationen wie geschätzte Lieferzeit und Kosten anzeigen. Verwende hierfür geeignete Layout-Widgets.

// c) Eine Kartenansicht, die die aktuelle Position des Lieferfahrzeugs in Echtzeit anzeigt,
// sobald der Nutzer seine Bestellung aufgibt.
// Integriere das google_maps_flutter-Plugin (basierend auf OpenStreetMap)und optional das geolocator-Plugin,
// um die aktuelle Position des Fahrzeugs zu ermitteln und auf der Karte anzuzeigen.
// OpenStreetMap ist eine Open-Source-Alternative, die keine API-Schlüssel oder Zahlungsinformationen erfordert.

// d) Eine Navigationsleiste am unteren Bildschirmrand, die es dem Nutzer ermöglicht,
// zwischen der Startseite, der Kartenansicht und einem Profilbereich zu wechseln.
// Der Profilbereich soll einfache Nutzerinformationen anzeigen.

// Hinweise:
//     Das flutter_map-Plugin nutzt OpenStreetMap-Daten und ist vollständig kostenlos
//     Es werden keine API-Schlüssel oder Kreditkarteninformationen benötigt
//     Die Lernziele (Kartenintegration, Live-Positionsanzeige, Navigation, State Management) bleiben identisch

import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong2/latlong.dart';

void main() => runApp(const LieferApp());

class Lieferoption {
  final String id;
  final String bezeichnung;
  final IconData icon;
  final String beschreibung;
  final int geschaetzteZeit;
  final double preisEur;

  const Lieferoption({
    required this.id,
    required this.bezeichnung,
    required this.icon,
    required this.beschreibung,
    required this.geschaetzteZeit,
    required this.preisEur,
  });
}

const List<Lieferoption> kLieferoptionen = [
  Lieferoption(
    id: 'food',
    bezeichnung: 'Essen',
    icon: Icons.restaurant,
    beschreibung:
        'Frische Gerichte aus lokalen Restaurants. Der Endpreis variiert je nach Restaurant, Warenkorb und Liefergebühr.',
    geschaetzteZeit: 30,
    preisEur: 6.90,
  ),
  Lieferoption(
    id: 'documents',
    bezeichnung: 'Dokumente',
    icon: Icons.description,
    beschreibung:
        'Sichere und schnelle Kurier-Zustellung wichtiger Unterlagen.',
    geschaetzteZeit: 45,
    preisEur: 19.90,
  ),
  Lieferoption(
    id: 'packages',
    bezeichnung: 'Pakete',
    icon: Icons.inventory_2,
    beschreibung: 'Zuverlässiger Transport von Paketen jeder Größe.',
    geschaetzteZeit: 60,
    preisEur: 24.90,
  ),
];

class BestellverlaufEintrag {
  final String titel;
  final DateTime erstelltAm;
  final String status;

  const BestellverlaufEintrag({
    required this.titel,
    required this.erstelltAm,
    required this.status,
  });
}

class LieferApp extends StatelessWidget {
  const LieferApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Fixkurier - Ihr Schneller Bote',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        scaffoldBackgroundColor: const Color(0xFFF4F6F8),
        colorScheme: const ColorScheme.light(
          primary: Color(0xFF5C8DC5),
          onPrimary: Colors.white,
          primaryContainer: Color(0xFFD9E6F4),
          onPrimaryContainer: Color(0xFF1F3E62),
          secondary: Color(0xFF909EAE),
          onSecondary: Colors.white,
          secondaryContainer: Color(0xFFE0E6ED),
          onSecondaryContainer: Color(0xFF323B46),
          tertiary: Color(0xFFAD9E90),
          onTertiary: Colors.white,
          tertiaryContainer: Color(0xFFECE5DE),
          onTertiaryContainer: Color(0xFF4E453A),
          surface: Colors.white,
          onSurface: Color(0xFF1D1F23),
          error: Color(0xFFB3261E),
          onError: Colors.white,
        ),
      ),
      home: const Hauptbildschirm(),
    );
  }
}

// Footer Navigation

class Hauptbildschirm extends StatefulWidget {
  const Hauptbildschirm({super.key});

  @override
  State<Hauptbildschirm> createState() => _HauptbildschirmState();
}

class _HauptbildschirmState extends State<Hauptbildschirm> {
  int _ausgewaehlterIndex = 0;
  Lieferoption? _aktiveBestellung;
  final List<BestellverlaufEintrag> _bestellverlauf = [];

  void _bestellungAufgeben(Lieferoption lieferoption) {
    setState(() {
      _aktiveBestellung = lieferoption;
      _bestellverlauf.insert(
        0,
        BestellverlaufEintrag(
          titel: lieferoption.bezeichnung,
          erstelltAm: DateTime.now(),
          status: 'Unterwegs',
        ),
      );
      _ausgewaehlterIndex = 1;
    });
  }

  @override
  Widget build(BuildContext context) {
    final seiten = <Widget>[
      Startseite(beiBestellung: _bestellungAufgeben),
      Kartenansicht(aktiveBestellung: _aktiveBestellung),
      Profilseite(bestellverlauf: _bestellverlauf),
    ];

    return Scaffold(
      body: seiten[_ausgewaehlterIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _ausgewaehlterIndex,
        onTap: (index) => setState(() => _ausgewaehlterIndex = index),
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Startseite'),
          BottomNavigationBarItem(icon: Icon(Icons.map), label: 'Karte'),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: 'Profil'),
        ],
      ),
    );
  }
}

// Startseite mit Übersicht der Lieferoptionen

class Startseite extends StatelessWidget {
  final ValueChanged<Lieferoption> beiBestellung;

  const Startseite({super.key, required this.beiBestellung});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Fixkurier - Ihr Schneller Bote'),
        centerTitle: true,
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(12),
        itemCount: kLieferoptionen.length,
        itemBuilder: (context, index) {
          final lieferoption = kLieferoptionen[index];
          return _LieferoptionKarte(
            lieferoption: lieferoption,
            beiBestellung: beiBestellung,
          );
        },
      ),
    );
  }
}

class _LieferoptionKarte extends StatelessWidget {
  final Lieferoption lieferoption;
  final ValueChanged<Lieferoption> beiBestellung;

  const _LieferoptionKarte({
    required this.lieferoption,
    required this.beiBestellung,
  });

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 8),
      child: InkWell(
        borderRadius: BorderRadius.circular(12),
        onTap: () => Navigator.push(
          context,
          MaterialPageRoute(
            builder: (_) => Detailseite(
              lieferoption: lieferoption,
              beiBestellung: beiBestellung,
            ),
          ),
        ),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Row(
            children: [
              CircleAvatar(
                radius: 28,
                backgroundColor: colorScheme.primaryContainer,
                child: Icon(
                  lieferoption.icon,
                  size: 28,
                  color: colorScheme.onPrimaryContainer,
                ),
              ),
              const SizedBox(width: 16),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      lieferoption.bezeichnung,
                      style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      lieferoption.beschreibung,
                      style: Theme.of(context).textTheme.bodySmall,
                    ),
                    const SizedBox(height: 6),
                    Row(
                      children: [
                        Icon(
                          Icons.schedule,
                          size: 14,
                          color: colorScheme.primary,
                        ),
                        const SizedBox(width: 4),
                        Text(
                          'ca. ${lieferoption.geschaetzteZeit} Min.',
                          style: Theme.of(context).textTheme.labelSmall
                              ?.copyWith(color: colorScheme.primary),
                        ),
                        const SizedBox(width: 12),
                        Icon(Icons.euro, size: 14, color: colorScheme.primary),
                        const SizedBox(width: 4),
                        Text(
                          '${lieferoption.preisEur.toStringAsFixed(2)} €',
                          style: Theme.of(context).textTheme.labelSmall
                              ?.copyWith(color: colorScheme.primary),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
              Icon(Icons.chevron_right, color: colorScheme.outline),
            ],
          ),
        ),
      ),
    );
  }
}

// Detailseite

class Detailseite extends StatelessWidget {
  final Lieferoption lieferoption;
  final ValueChanged<Lieferoption> beiBestellung;

  const Detailseite({
    super.key,
    required this.lieferoption,
    required this.beiBestellung,
  });

  bool get _istEssenslieferung => lieferoption.id == 'food';

  String get _kostenLabel =>
      _istEssenslieferung ? 'Liefergebühr ab' : 'Lieferkosten';

  String get _kostenWert => _istEssenslieferung
      ? 'ab ${lieferoption.preisEur.toStringAsFixed(2)} € zzgl. Warenkorbwert'
      : '${lieferoption.preisEur.toStringAsFixed(2)} €';

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;
    final textTheme = Theme.of(context).textTheme;

    return Scaffold(
      appBar: AppBar(title: Text(lieferoption.bezeichnung)),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Card(
              child: Padding(
                padding: const EdgeInsets.all(24),
                child: Column(
                  children: [
                    Icon(
                      lieferoption.icon,
                      size: 72,
                      color: colorScheme.primary,
                    ),
                    const SizedBox(height: 16),
                    Text(
                      lieferoption.bezeichnung,
                      style: textTheme.headlineSmall?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 12),
                    Text(
                      lieferoption.beschreibung,
                      style: textTheme.bodyLarge,
                      textAlign: TextAlign.center,
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 16),
            Card(
              child: Padding(
                padding: const EdgeInsets.symmetric(
                  vertical: 16,
                  horizontal: 24,
                ),
                child: Column(
                  children: [
                    _InfoZeile(
                      icon: Icons.schedule,
                      label: 'Geschätzte Lieferzeit',
                      value: 'ca. ${lieferoption.geschaetzteZeit} Minuten',
                    ),
                    const Divider(height: 24),
                    _InfoZeile(
                      icon: Icons.euro,
                      label: _kostenLabel,
                      value: _kostenWert,
                    ),
                  ],
                ),
              ),
            ),
            if (_istEssenslieferung) ...[
              const SizedBox(height: 12),
              Card(
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Text(
                    'Die Gesamtkosten setzen sich aus Warenkorbwert und Liefergebühr zusammen. Je nach Restaurant können Mindestbestellwert und Lieferkosten variieren.',
                    style: textTheme.bodyMedium,
                  ),
                ),
              ),
            ],
            const SizedBox(height: 24),
            FilledButton.icon(
              onPressed: () {
                Navigator.pop(context);
                beiBestellung(lieferoption);
              },
              icon: const Icon(Icons.shopping_cart_checkout),
              label: const Text('Jetzt bestellen'),
              style: FilledButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 16),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _InfoZeile extends StatelessWidget {
  final IconData icon;
  final String label;
  final String value;

  const _InfoZeile({
    required this.icon,
    required this.label,
    required this.value,
  });

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;
    return Row(
      children: [
        Icon(icon, color: colorScheme.primary),
        const SizedBox(width: 12),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                label,
                style: Theme.of(context).textTheme.labelMedium?.copyWith(
                  color: colorScheme.onSurfaceVariant,
                ),
              ),
              const SizedBox(height: 2),
              Text(
                value,
                style: Theme.of(
                  context,
                ).textTheme.titleMedium?.copyWith(fontWeight: FontWeight.w600),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

// Kartenansicht

class Kartenansicht extends StatefulWidget {
  final Lieferoption? aktiveBestellung;

  const Kartenansicht({super.key, required this.aktiveBestellung});

  @override
  State<Kartenansicht> createState() => _KartenansichtState();
}
// Hinweis: In einer echten App würde die Fahrzeugposition von einem Backend-Service bereitgestellt,
// der die GPS-Daten des Fahrzeugs empfängt und an die App sendet. Ich arbeite mit einer Simulation.

class _KartenansichtState extends State<Kartenansicht> {
  // Startpunkt: Rathausmarkt, Hamburg
  LatLng _aktuellePosition = const LatLng(53.5509, 9.9937);
  final MapController _kartenController = MapController();
  Timer? _simulationsTimer;
  String _standortQuelle = 'Simulation';

  @override
  void didUpdateWidget(covariant Kartenansicht oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (widget.aktiveBestellung != null &&
        oldWidget.aktiveBestellung != widget.aktiveBestellung) {
      _starteSimulation();
    }
  }

  @override
  void initState() {
    super.initState();
    _starteSimulation();
  }

  void _starteSimulation() {
    _simulationsTimer?.cancel();

    _simulationsTimer = Timer.periodic(const Duration(seconds: 2), (_) {
      if (!mounted) return;

      setState(() {
        _aktuellePosition = LatLng(
          _aktuellePosition.latitude + 0.0002,
          _aktuellePosition.longitude + 0.0003,
        );
        _standortQuelle = 'Simulation';
      });
      _kartenController.move(_aktuellePosition, 15);
    });
  }

  void _aufStandortZentrieren() {
    _kartenController.move(_aktuellePosition, 15);
  }

  @override
  void dispose() {
    _simulationsTimer?.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;
    return Scaffold(
      appBar: AppBar(
        title: const Text('Lieferung verfolgen'),
        centerTitle: true,
      ),
      body: Stack(
        children: [
          FlutterMap(
            mapController: _kartenController,
            options: MapOptions(
              initialCenter: _aktuellePosition,
              initialZoom: 15,
            ),
            children: [
              TileLayer(
                urlTemplate: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
                userAgentPackageName: 'com.example.teilpruefung_04',
              ),
              MarkerLayer(
                markers: [
                  Marker(
                    point: _aktuellePosition,
                    width: 52,
                    height: 52,
                    child: Container(
                      decoration: BoxDecoration(
                        color: colorScheme.primaryContainer,
                        shape: BoxShape.circle,
                        boxShadow: [
                          BoxShadow(
                            color: Colors.black26,
                            blurRadius: 6,
                            offset: const Offset(0, 2),
                          ),
                        ],
                      ),
                      child: Icon(
                        Icons.my_location,
                        color: colorScheme.onPrimaryContainer,
                        size: 30,
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
          Positioned(
            top: 12,
            left: 12,
            right: 12,
            child: Card(
              color: colorScheme.surface,
              child: Padding(
                padding: const EdgeInsets.all(10),
                child: Text(
                  'Aktuelle Position: ${_aktuellePosition.latitude.toStringAsFixed(5)}, ${_aktuellePosition.longitude.toStringAsFixed(5)}\nQuelle: $_standortQuelle',
                  style: Theme.of(context).textTheme.bodySmall,
                ),
              ),
            ),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton.small(
        tooltip: 'Position zentrieren',
        onPressed: _aufStandortZentrieren,
        child: const Icon(Icons.my_location),
      ),
    );
  }
}

// Profilseite

class Profilseite extends StatelessWidget {
  final List<BestellverlaufEintrag> bestellverlauf;

  const Profilseite({super.key, required this.bestellverlauf});

  String _datumFormatieren(DateTime datum) {
    final tag = datum.day.toString().padLeft(2, '0');
    final monat = datum.month.toString().padLeft(2, '0');
    return '$tag.$monat.${datum.year}';
  }

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;
    final textTheme = Theme.of(context).textTheme;

    return Scaffold(
      appBar: AppBar(title: const Text('Profil'), centerTitle: true),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          // Nutzerinformationen
          Card(
            child: Padding(
              padding: const EdgeInsets.all(24),
              child: Column(
                children: [
                  // hier ist ein mockup - man kann es erweitern, so das der nutzer hier sein profilbild einfügen kann
                  CircleAvatar(
                    radius: 40,
                    backgroundColor: colorScheme.primaryContainer,
                    child: Icon(
                      Icons.person,
                      size: 40,
                      color: colorScheme.onPrimaryContainer,
                    ),
                  ),
                  const SizedBox(height: 12),
                  Text(
                    'Max Mustermann',
                    style: textTheme.titleLarge?.copyWith(
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    'max.mustermann@musteremail.de',
                    style: textTheme.bodyMedium?.copyWith(
                      color: colorScheme.onSurfaceVariant,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    '+49 170 1234567',
                    style: textTheme.bodyMedium?.copyWith(
                      color: colorScheme.onSurfaceVariant,
                    ),
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(height: 16),
          Text(
            'Bestellhistorie',
            style: textTheme.titleMedium?.copyWith(fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          if (bestellverlauf.isEmpty)
            Card(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Text(
                  'Noch keine Bestellungen vorhanden.',
                  style: textTheme.bodyMedium,
                ),
              ),
            )
          else
            ...bestellverlauf.map(
              (eintrag) => Card(
                margin: const EdgeInsets.only(bottom: 8),
                child: ListTile(
                  leading: Icon(Icons.receipt_long, color: colorScheme.primary),
                  title: Text(eintrag.titel),
                  subtitle: Text(_datumFormatieren(eintrag.erstelltAm)),
                  trailing: Chip(
                    label: Text(eintrag.status, style: textTheme.labelSmall),
                    backgroundColor: colorScheme.secondaryContainer,
                  ),
                ),
              ),
            ),
        ],
      ),
    );
  }
}
