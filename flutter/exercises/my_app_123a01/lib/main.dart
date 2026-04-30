// Entwickle eine Flutter-Anwendung, die folgende Funktionalitäten umfasst:

// a) Erstelle eine Startseite mit einem Layout, das mindestens drei Buttons enthält: "Benutzereinstellungen", "Produktliste" und "Über uns". Nutze dafür passende Widgets und sorge für ein ansprechendes Design.

// b) Implementiere die Funktionalität für "Benutzereinstellungen", wo Nutzer ihre Präferenzen wie Theme (Dunkel/Hell), Sprache (Deutsch/Englisch) und Benachrichtigungseinstellungen (Ein/Aus) speichern können. Verwende Shared Preferences, um die Einstellungen lokal zu speichern.

// c) Für die "Produktliste" soll eine Navigation zu einer neuen Seite implementiert werden, auf der eine Liste von Produkten angezeigt wird. Jedes Produkt hat einen Namen, eine Beschreibung und einen Preis. Implementiere eine Möglichkeit, Produkte über eine HTTP-Anfrage von einem Mock-Server zu laden und sie in der App anzuzeigen.

// d) In der "Über uns"-Seite zeige Informationen über die App und den Entwickler an. Nutze hierfür ein einfaches Layout mit TextWidgets.

// e) Implementiere zusätzlich eine Funktion, mit der Nutzer ihre gesamten Daten (Einstellungen und Produktliste) in einer lokalen SQLite-Datenbank speichern können. Biete auch eine Möglichkeit, diese Daten wieder zu laden.

import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:path/path.dart' as p;
import 'package:shared_preferences/shared_preferences.dart';
import 'package:sqflite/sqflite.dart';

// Globaler Notifier für das Theme – kann von SettingsPage aus gesetzt werden
final ValueNotifier<bool> darkThemeNotifier = ValueNotifier<bool>(false);

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final prefs = await SharedPreferences.getInstance();
  darkThemeNotifier.value = prefs.getBool('darkTheme') ?? false;
  runApp(const MyApp());
}

// ─── Models ──────────────────────────────────────────────────────────────────

class Product {
  final int? id;
  final String name;
  final String description;
  final double price;

  const Product({
    this.id,
    required this.name,
    required this.description,
    required this.price,
  });

  factory Product.fromJson(Map<String, dynamic> json) => Product(
    id: json['id'] as int?,
    name: (json['title'] ?? json['name'] ?? '').toString(),
    description: (json['body'] ?? json['description'] ?? '').toString(),
    price: (json['price'] as num?)?.toDouble() ?? 0.0,
  );

  Map<String, dynamic> toMap() => {
    if (id != null) 'id': id,
    'name': name,
    'description': description,
    'price': price,
  };
}

// ─── Database Service ─────────────────────────────────────────────────────────

class DatabaseService {
  static Database? _db;

  static Future<Database> get database async {
    if (_db != null) return _db!;
    _db = await _initDb();
    return _db!;
  }

  static Future<Database> _initDb() async {
    final dbPath = await getDatabasesPath();
    final path = p.join(dbPath, 'app_data.db');
    return openDatabase(
      path,
      version: 1,
      onCreate: (db, version) async {
        await db.execute('''
          CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL
          )
        ''');
        await db.execute('''
          CREATE TABLE settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
          )
        ''');
      },
    );
  }

  static Future<void> saveProducts(List<Product> products) async {
    final db = await database;
    final batch = db.batch();
    batch.delete('products');
    for (final product in products) {
      batch.insert('products', product.toMap());
    }
    await batch.commit(noResult: true);
  }

  static Future<List<Product>> loadProducts() async {
    final db = await database;
    final rows = await db.query('products');
    return rows.map((r) => Product.fromJson(r)).toList();
  }

  static Future<void> saveSettings(Map<String, String> settings) async {
    final db = await database;
    final batch = db.batch();
    settings.forEach((key, value) {
      batch.insert('settings', {
        'key': key,
        'value': value,
      }, conflictAlgorithm: ConflictAlgorithm.replace);
    });
    await batch.commit(noResult: true);
  }

  static Future<Map<String, String>> loadSettings() async {
    final db = await database;
    final rows = await db.query('settings');
    return {for (final r in rows) r['key'] as String: r['value'] as String};
  }
}

// ─── App ─────────────────────────────────────────────────────────────────────

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  void initState() {
    super.initState();
    darkThemeNotifier.addListener(_onThemeChanged);
  }

  void _onThemeChanged() => setState(() {});

  @override
  void dispose() {
    darkThemeNotifier.removeListener(_onThemeChanged);
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'My App 123a01',
      theme: darkThemeNotifier.value
          ? ThemeData.dark()
          : ThemeData(primarySwatch: Colors.indigo),
      home: const HomePage(),
    );
  }
}

// ─── Home Page ────────────────────────────────────────────────────────────────

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Startseite')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            _NavButton(
              icon: Icons.settings,
              label: 'Benutzereinstellungen',
              onPressed: () => Navigator.push(
                context,
                MaterialPageRoute(builder: (_) => const SettingsPage()),
              ),
            ),
            const SizedBox(height: 16),
            _NavButton(
              icon: Icons.shopping_cart,
              label: 'Produktliste',
              onPressed: () => Navigator.push(
                context,
                MaterialPageRoute(builder: (_) => const ProductListPage()),
              ),
            ),
            const SizedBox(height: 16),
            _NavButton(
              icon: Icons.info_outline,
              label: 'Über uns',
              onPressed: () => Navigator.push(
                context,
                MaterialPageRoute(builder: (_) => const AboutPage()),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _NavButton extends StatelessWidget {
  final IconData icon;
  final String label;
  final VoidCallback onPressed;

  const _NavButton({
    required this.icon,
    required this.label,
    required this.onPressed,
  });

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 260,
      height: 56,
      child: ElevatedButton.icon(
        icon: Icon(icon),
        label: Text(label),
        onPressed: onPressed,
      ),
    );
  }
}

// ─── Settings Page ────────────────────────────────────────────────────────────

class SettingsPage extends StatefulWidget {
  const SettingsPage({super.key});

  @override
  State<SettingsPage> createState() => _SettingsPageState();
}

class _SettingsPageState extends State<SettingsPage> {
  bool _darkTheme = false;
  String _language = 'Deutsch';
  bool _notifications = true;

  @override
  void initState() {
    super.initState();
    _loadPrefs();
  }

  Future<void> _loadPrefs() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _darkTheme = prefs.getBool('darkTheme') ?? false;
      _language = prefs.getString('language') ?? 'Deutsch';
      _notifications = prefs.getBool('notifications') ?? true;
    });
  }

  Future<void> _savePrefs() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool('darkTheme', _darkTheme);
    await prefs.setString('language', _language);
    await prefs.setBool('notifications', _notifications);

    // Theme sofort auf die App anwenden
    darkThemeNotifier.value = _darkTheme;

    await DatabaseService.saveSettings({
      'darkTheme': _darkTheme.toString(),
      'language': _language,
      'notifications': _notifications.toString(),
    });

    if (!mounted) return;
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Einstellungen gespeichert'),
        backgroundColor: Colors.green,
      ),
    );
  }

  Future<void> _loadFromDb() async {
    final settings = await DatabaseService.loadSettings();
    if (settings.isEmpty) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Keine gespeicherten Daten gefunden')),
      );
      return;
    }
    setState(() {
      _darkTheme = settings['darkTheme'] == 'true';
      _language = settings['language'] ?? 'Deutsch';
      _notifications = settings['notifications'] != 'false';
    });
    darkThemeNotifier.value = _darkTheme;
    if (!mounted) return;
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Einstellungen aus Datenbank geladen'),
        backgroundColor: Colors.blue,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Benutzereinstellungen')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          SwitchListTile(
            title: const Text('Dunkles Theme'),
            value: _darkTheme,
            onChanged: (v) => setState(() => _darkTheme = v),
          ),
          ListTile(
            title: const Text('Sprache'),
            trailing: DropdownButton<String>(
              value: _language,
              items: const [
                DropdownMenuItem(value: 'Deutsch', child: Text('Deutsch')),
                DropdownMenuItem(value: 'Englisch', child: Text('Englisch')),
              ],
              onChanged: (v) => setState(() => _language = v ?? 'Deutsch'),
            ),
          ),
          SwitchListTile(
            title: const Text('Benachrichtigungen'),
            value: _notifications,
            onChanged: (v) => setState(() => _notifications = v),
          ),
          const SizedBox(height: 24),
          ElevatedButton(
            onPressed: _savePrefs,
            child: const Text('Einstellungen speichern (SharedPrefs + SQLite)'),
          ),
          const SizedBox(height: 12),
          OutlinedButton(
            onPressed: _loadFromDb,
            child: const Text('Einstellungen aus SQLite laden'),
          ),
        ],
      ),
    );
  }
}

// ─── Product List Page ────────────────────────────────────────────────────────

class ProductListPage extends StatefulWidget {
  const ProductListPage({super.key});

  @override
  State<ProductListPage> createState() => _ProductListPageState();
}

class _ProductListPageState extends State<ProductListPage> {
  List<Product> _products = [];
  bool _loading = false;
  String? _error;

  Future<void> _fetchProducts() async {
    setState(() {
      _loading = true;
      _error = null;
    });
    try {
      final response = await http.get(
        Uri.parse('https://jsonplaceholder.typicode.com/posts?_limit=15'),
      );
      if (response.statusCode == 200) {
        final List<dynamic> data = json.decode(response.body) as List<dynamic>;
        setState(() {
          _products = data.asMap().entries.map((e) {
            final item = Map<String, dynamic>.from(e.value as Map);
            item['price'] = (e.key + 1) * 4.99;
            return Product.fromJson(item);
          }).toList();
        });
      } else {
        setState(() => _error = 'HTTP-Fehler: ${response.statusCode}');
      }
    } catch (e) {
      setState(() => _error = 'Netzwerkfehler: $e');
    } finally {
      setState(() => _loading = false);
    }
  }

  Future<void> _saveToDb() async {
    if (_products.isEmpty) return;
    await DatabaseService.saveProducts(_products);
    if (!mounted) return;
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Produkte in SQLite gespeichert'),
        backgroundColor: Colors.green,
      ),
    );
  }

  Future<void> _loadFromDb() async {
    final products = await DatabaseService.loadProducts();
    if (products.isEmpty) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Keine Produkte in der Datenbank')),
      );
      return;
    }
    setState(() => _products = products);
    if (!mounted) return;
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Produkte aus SQLite geladen'),
        backgroundColor: Colors.blue,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Produktliste'),
        actions: [
          IconButton(
            icon: const Icon(Icons.save),
            tooltip: 'In SQLite speichern',
            onPressed: _saveToDb,
          ),
          IconButton(
            icon: const Icon(Icons.storage),
            tooltip: 'Aus SQLite laden',
            onPressed: _loadFromDb,
          ),
        ],
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(12),
            child: ElevatedButton.icon(
              icon: const Icon(Icons.cloud_download),
              label: const Text('Produkte laden'),
              onPressed: _fetchProducts,
            ),
          ),
          if (_loading) const LinearProgressIndicator(),
          if (_error != null)
            Padding(
              padding: const EdgeInsets.all(16),
              child: Text(_error!, style: const TextStyle(color: Colors.red)),
            ),
          Expanded(
            child: _products.isEmpty
                ? const Center(child: Text('Keine Produkte vorhanden'))
                : ListView.builder(
                    itemCount: _products.length,
                    itemBuilder: (context, index) {
                      final product = _products[index];
                      return Card(
                        margin: const EdgeInsets.symmetric(
                          horizontal: 12,
                          vertical: 6,
                        ),
                        child: ListTile(
                          title: Text(product.name),
                          subtitle: Text(
                            product.description,
                            maxLines: 2,
                            overflow: TextOverflow.ellipsis,
                          ),
                          trailing: Text(
                            '${product.price.toStringAsFixed(2)} €',
                            style: const TextStyle(fontWeight: FontWeight.bold),
                          ),
                        ),
                      );
                    },
                  ),
          ),
        ],
      ),
    );
  }
}

// ─── About Page ───────────────────────────────────────────────────────────────

class AboutPage extends StatelessWidget {
  const AboutPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Über uns')),
      body: const Padding(
        padding: EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'My App 123a01',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 16),
            Text('Version: 1.0.0', style: TextStyle(fontSize: 16)),
            SizedBox(height: 8),
            Text(
              'Diese App demonstriert Shared Preferences, HTTP-Anfragen '
              'und lokale SQLite-Datenspeicherung in Flutter.',
              style: TextStyle(fontSize: 15),
            ),
            SizedBox(height: 24),
            Text(
              'Entwickler',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 8),
            Text('Matthias Kahlert', style: TextStyle(fontSize: 15)),
            SizedBox(height: 4),
            Text(
              'Learning Journey – Flutter-Kurs',
              style: TextStyle(fontSize: 14, color: Colors.grey),
            ),
          ],
        ),
      ),
    );
  }
}
