// Entwickle eine Flutter-Anwendung, die eine einfache Buchhandlung repräsentiert. Die Anwendung soll die folgenden Funktionen beinhalten:

// a) Eine Startseite, die eine Liste von Büchern anzeigt. Jedes Buch soll durch ein ListTile-Widget dargestellt werden, das den Titel und den Autor des Buches anzeigt.

// b) Beim Tippen auf ein Buch soll eine Detailseite für das ausgewählte Buch geöffnet werden. Diese Seite soll den Titel, Autor, eine kurze Beschreibung und den Preis des Buches anzeigen. Implementiere die Navigation zwischen der Startseite und der Detailseite mit Named Routes.

// c) Auf der Detailseite soll ein Button "In den Warenkorb" vorhanden sein. Beim Klicken auf diesen Button soll ein Dialog erscheinen, der den Nutzer fragt, ob er das Buch zum Warenkorb hinzufügen möchte. Bei Bestätigung soll eine Snackbar mit der Nachricht "Buch zum Warenkorb hinzugefügt" erscheinen.

// d) Füge eine Navigationsleiste hinzu, die es ermöglicht, zwischen der Startseite und einer Warenkorbseite zu navigieren. Die Warenkorbseite soll eine Liste der hinzugefügten Bücher anzeigen.

import 'package:flutter/material.dart';

void main() {
  runApp(const BookstoreApp());
}

// Datenmodell für ein Buch
class Book {
  final String id;
  final String title;
  final String author;
  final String description;
  final double price;

  Book({
    required this.id,
    required this.title,
    required this.author,
    required this.description,
    required this.price,
  });
}

// Liste aller verfügbaren Bücher
final List<Book> bookList = [
  Book(
    id: '1',
    title: 'Der Alchimist',
    author: 'Paulo Coelho',
    description:
        'Ein Klassiker über einen andalusischen Hirten, der nach Ägypten reist, um einen Schatz zu finden.',
    price: 12.99,
  ),
  Book(
    id: '2',
    title: 'Harry Potter und der Stein der Weisen',
    author: 'J.K. Rowling',
    description:
        'Der erste Band der berühmten Fantasyreihe über den jungen Zauberer Harry Potter.',
    price: 15.99,
  ),
  Book(
    id: '3',
    title: 'Die Verwandlung',
    author: 'Franz Kafka',
    description:
        'Eine Geschichte über Gregor Samsa, der eines Morgens als Ungeziefer aufwacht.',
    price: 9.99,
  ),
  Book(
    id: '4',
    title: 'Der kleine Prinz',
    author: 'Antoine de Saint-Exupéry',
    description:
        'Eine poetische Erzählung über einen kleinen Prinzen, der verschiedene Planeten besucht.',
    price: 11.50,
  ),
  Book(
    id: '5',
    title: 'Stolz und Vorurteil',
    author: 'Jane Austen',
    description:
        'Ein Roman über die fünf Töchter der Familie Bennet und ihre Heiratsaussichten.',
    price: 10.75,
  ),
];

// Liste der Bücher im Warenkorb
List<Book> cartItems = [];

class BookstoreApp extends StatelessWidget {
  const BookstoreApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Buchhandlung',
      theme: ThemeData(
        primarySwatch: Colors.brown,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      // b) Named Routes definieren
      initialRoute: '/',
      routes: {
        '/': (context) => const HomePage(),
        '/detail': (context) => const BookDetailPage(),
        '/cart': (context) => const CartPage(),
        '/about': (context) => const AboutPage(),
      },
    );
  }
}

// a) Startseite mit Buchliste
class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _selectedIndex = 0;

  // Liste der Seiten für die Navigation
  final List<Widget> _pages = [
    const BookListPage(),
    const CartPage(),
    const AboutPage(),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Buchhandlung')),
      body: _pages[_selectedIndex],
      // d) Bottom Navigation Bar
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _selectedIndex,
        onTap: _onItemTapped,
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.book), label: 'Bücher'),
          BottomNavigationBarItem(
            icon: Icon(Icons.shopping_cart),
            label: 'Warenkorb',
          ),
          BottomNavigationBarItem(icon: Icon(Icons.info), label: 'Über uns'),
        ],
      ),
    );
  }
}

// Buchliste auf der Startseite
class BookListPage extends StatelessWidget {
  const BookListPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: bookList.length,
      itemBuilder: (context, index) {
        final book = bookList[index];
        // a) ListTile für jedes Buch
        return ListTile(
          title: Text(book.title),
          subtitle: Text(book.author),
          trailing: Text('${book.price.toStringAsFixed(2)} €'),
          // b) Navigation zur Detailseite
          onTap: () {
            Navigator.pushNamed(context, '/detail', arguments: book);
          },
        );
      },
    );
  }
}

// b) Detailseite für ein ausgewähltes Buch
class BookDetailPage extends StatelessWidget {
  const BookDetailPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Buchdaten aus den Route-Argumenten holen
    final book = ModalRoute.of(context)!.settings.arguments as Book;

    return Scaffold(
      appBar: AppBar(title: Text(book.title)),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              book.title,
              style: const TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            Text(
              'Autor: ${book.author}',
              style: const TextStyle(fontSize: 18, fontStyle: FontStyle.italic),
            ),
            const SizedBox(height: 16),
            const Text(
              'Beschreibung:',
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            Text(book.description, style: const TextStyle(fontSize: 16)),
            const SizedBox(height: 16),
            Text(
              'Preis: ${book.price.toStringAsFixed(2)} €',
              style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const Spacer(),
            // c) "In den Warenkorb" Button mit Dialog
            Center(
              child: ElevatedButton(
                onPressed: () {
                  // Dialog anzeigen
                  showDialog(
                    context: context,
                    builder: (BuildContext context) {
                      return AlertDialog(
                        title: const Text('Zum Warenkorb hinzufügen?'),
                        content: Text(
                          'Möchten Sie "${book.title}" zum Warenkorb hinzufügen?',
                        ),
                        actions: [
                          TextButton(
                            onPressed: () {
                              Navigator.of(context).pop();
                            },
                            child: const Text('Abbrechen'),
                          ),
                          TextButton(
                            onPressed: () {
                              // Buch zum Warenkorb hinzufügen
                              cartItems.add(book);
                              Navigator.of(context).pop();

                              // Snackbar anzeigen
                              ScaffoldMessenger.of(context).showSnackBar(
                                SnackBar(
                                  content: Text(
                                    '${book.title} wurde zum Warenkorb hinzugefügt',
                                  ),
                                  duration: const Duration(seconds: 2),
                                ),
                              );
                            },
                            child: const Text('Hinzufügen'),
                          ),
                        ],
                      );
                    },
                  );
                },
                child: const Padding(
                  padding: EdgeInsets.symmetric(horizontal: 32, vertical: 12),
                  child: Text('In den Warenkorb'),
                ),
              ),
            ),
            const SizedBox(height: 16),
          ],
        ),
      ),
    );
  }
}

// d) Warenkorbseite
class CartPage extends StatefulWidget {
  const CartPage({Key? key}) : super(key: key);

  @override
  State<CartPage> createState() => _CartPageState();
}

class _CartPageState extends State<CartPage> {
  @override
  Widget build(BuildContext context) {
    return cartItems.isEmpty
        ? const Center(
            child: Text(
              'Ihr Warenkorb ist leer',
              style: TextStyle(fontSize: 18),
            ),
          )
        : Column(
            children: [
              Expanded(
                child: ListView.builder(
                  itemCount: cartItems.length,
                  itemBuilder: (context, index) {
                    final book = cartItems[index];
                    return ListTile(
                      title: Text(book.title),
                      subtitle: Text(book.author),
                      trailing: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Text('${book.price.toStringAsFixed(2)} €'),
                          IconButton(
                            icon: const Icon(Icons.delete),
                            onPressed: () {
                              setState(() {
                                cartItems.removeAt(index);
                              });
                              ScaffoldMessenger.of(context).showSnackBar(
                                const SnackBar(
                                  content: Text('Buch entfernt'),
                                  duration: Duration(seconds: 1),
                                ),
                              );
                            },
                          ),
                        ],
                      ),
                    );
                  },
                ),
              ),
              // Gesamtsumme anzeigen
              Container(
                padding: const EdgeInsets.all(16),
                color: Colors.grey[200],
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const Text(
                      'Gesamtsumme:',
                      style: TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    Text(
                      '${cartItems.fold(0.0, (sum, book) => sum + book.price).toStringAsFixed(2)} €',
                      style: const TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          );
  }
}

// Über uns Seite
class AboutPage extends StatelessWidget {
  const AboutPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const Center(
      child: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.book, size: 80, color: Colors.brown),
            SizedBox(height: 20),
            Text(
              'Über unsere Buchhandlung',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 16),
            Text(
              'Willkommen in unserer virtuellen Buchhandlung! Wir bieten eine sorgfältig ausgewählte Sammlung von Klassikern und modernen Bestsellern.',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 16),
            ),
          ],
        ),
      ),
    );
  }
}
