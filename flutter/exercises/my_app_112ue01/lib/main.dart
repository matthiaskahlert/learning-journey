// Entwickle eine einfache Flutter-Anwendung, die eine Liste von Beiträgen von einer externen API lädt und diese in einer ansprechenden Benutzeroberfläche anzeigt. Verwende dazu die Test-API "jsonplaceholder.typicode.com" für die Beiträge. Die Anwendung sollte folgende Funktionalitäten umfassen:

// a) Verwende das http-Paket, um eine GET-Anfrage an die API zu senden und die Daten zu erhalten. Die URL, die du verwenden sollst, ist https://jsonplaceholder.typicode.com/posts.

// b) Dekodiere die Antwort von der API, die im JSON-Format vorliegt, in eine Liste von Dart-Objekten.

// c) Erstelle ein Widget, das eine Liste dieser Beiträge anzeigt. Jeder Beitrag sollte mindestens den Titel und den Body des Beitrags zeigen.

// d) Implementiere eine einfache Navigation, die es ermöglicht, von der Hauptseite mit der Liste der Beiträge auf eine Detailseite zu navigieren, wenn ein Beitrag angeklickt wird. Auf der Detailseite sollen der Titel und der vollständige Body des Beitrags angezeigt werden.

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(title: 'Flutter Demo', home: PostsPage());
  }
}

class PostsPage extends StatefulWidget {
  const PostsPage({super.key});

  @override
  PostsPageState createState() => PostsPageState();
}

class PostsPageState extends State<PostsPage> {
  List posts = [];

  @override
  void initState() {
    super.initState();
    fetchPosts();
  }

  Future<void> fetchPosts() async {
    final response = await http.get(
      Uri.parse('https://jsonplaceholder.typicode.com/posts'),
    );
    if (response.statusCode == 200) {
      setState(() {
        posts = json.decode(response.body);
      });
    } else {
      throw Exception('Failed to load posts');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Posts')),
      body: ListView.builder(
        itemCount: posts.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(posts[index]['title']),
            subtitle: Text(posts[index]['body']),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => PostDetailPage(post: posts[index]),
                ),
              );
            },
          );
        },
      ),
    );
  }
}

class PostDetailPage extends StatelessWidget {
  final dynamic post;

  const PostDetailPage({super.key, this.post});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(post['title'])),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Text(post['body']),
      ),
    );
  }
}
