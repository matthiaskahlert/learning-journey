// Entwickle eine einfache Flutter-App, die ein responsives Layout für eine Nachrichten-App simuliert. Die App soll zwei Hauptansichten haben: eine für Mobilgeräte und eine für Tablets. Für Mobilgeräte soll die App eine Liste von Nachrichtenüberschriften anzeigen, die beim Tippen eine Detailansicht der Nachricht in einem neuen Bildschirm öffnet. Für Tablets soll die App eine zweigeteilte Ansicht haben, bei der die linke Seite die Liste der Nachrichtenüberschriften und die rechte Seite die Detailansicht der ausgewählten Nachricht anzeigt.

// a) Definiere eine Klasse NewsItem, die Daten für eine einzelne Nachricht hält (z.B. Überschrift und Inhalt).

// b) Erstelle ein Widget NewsList, das eine Liste von NewsItem-Objekten annimmt und diese in einer für Mobilgeräte geeigneten Liste anzeigt.

// c) Entwickle ein Widget NewsDetail, das die Details eines NewsItem anzeigt.

// d) Berücksichtige bei der Implementierung, wie du mit den Constraints umgehst, um ein responsives Design zu erreichen.

import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class NewsItem {
  final String headline;
  final String content;

  NewsItem({required this.headline, required this.content});
}

class NewsList extends StatelessWidget {
  final List<NewsItem> newsItems;
  final ValueChanged<NewsItem> onItemTap;

  const NewsList({super.key, required this.newsItems, required this.onItemTap});

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: newsItems.length,
      itemBuilder: (context, index) {
        return ListTile(
          title: Text(newsItems[index].headline),
          onTap: () => onItemTap(newsItems[index]),
        );
      },
    );
  }
}

class NewsDetail extends StatelessWidget {
  final NewsItem newsItem;

  const NewsDetail({super.key, required this.newsItem});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(newsItem.headline)),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Text(newsItem.content),
      ),
    );
  }
}

class MyApp extends StatelessWidget {
  final List<NewsItem> newsItems = [
    NewsItem(
      headline: 'Nachricht 1',
      content: 'Dies ist der Inhalt der Nachricht Nr. 1',
    ),
    // Füge hier weitere NewsItems hinzu
  ];

  MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: LayoutBuilder(
          builder: (context, constraints) {
            if (constraints.maxWidth > 600) {
              // Tablet-Layout
              return Row(
                children: [
                  Expanded(
                    flex: 1,
                    child: NewsList(newsItems: newsItems, onItemTap: (item) {}),
                  ),
                  Expanded(
                    flex: 2,
                    child: NewsDetail(
                      newsItem: newsItems.first,
                    ), // Standardmäßig das erste Element anzeigen
                  ),
                ],
              );
            } else {
              // Mobilgerät-Layout
              return NewsList(
                newsItems: newsItems,
                onItemTap: (item) {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => NewsDetail(newsItem: item),
                    ),
                  );
                },
              );
            }
          },
        ),
      ),
    );
  }
}
