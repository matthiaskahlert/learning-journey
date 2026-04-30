// Erstelle eine einfache Flutter-Anwendung, die Daten von einer RESTful API abruft. Die Anwendung soll eine Liste von Posts anzeigen, die von der JSONPlaceholder API (https://jsonplaceholder.typicode.com/posts) abgerufen werden. Verwende das http-Paket für die Netzwerkanfrage. Die Anwendung soll folgende Schritte beinhalten:

// a) Füge das http-Paket zu deinen Abhängigkeiten in der pubspec.yaml-Datei hinzu und führe flutter pub get aus.

// b) Importiere das http-Paket in deiner Dart-Datei.

// c) Erstelle eine Funktion, die asynchron die Posts von der JSONPlaceholder API abruft. Verwende die http.get()-Methode, um eine GET-Anfrage an die URL https://jsonplaceholder.typicode.com/posts zu stellen.

// d) Überprüfe den Statuscode der Antwort. Wenn der Statuscode 200 ist, wandle die Antwort (response.body) mit jsonDecode in ein Dart-Objekt um und gib dieses zurück.

// e) Zeige die abgerufenen Posts in einem ListView-Widget an. Jeder Post soll in einem ListTile-Widget dargestellt werden, wobei der Titel des Posts als Titel und der Body als Untertitel angezeigt wird.

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(title: 'Flutter Demo', home: const PostsPage());
  }
}

class PostsPage extends StatefulWidget {
  const PostsPage({super.key});

  @override
  PostsPageState createState() => PostsPageState();
}

class PostsPageState extends State<PostsPage> {
  late Future<List<Post>> posts;

  @override
  void initState() {
    super.initState();
    posts = fetchPosts();
  }

  Future<List<Post>> fetchPosts() async {
    final response = await http.get(
      Uri.parse('https://jsonplaceholder.typicode.com/posts'),
    );

    if (response.statusCode == 200) {
      List jsonResponse = json.decode(response.body);
      return jsonResponse.map((post) => Post.fromJson(post)).toList();
    } else {
      throw Exception('Failed to load posts');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Posts')),
      body: FutureBuilder<List<Post>>(
        future: posts,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return ListView.builder(
              itemCount: snapshot.data!.length,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text(snapshot.data![index].title),
                  subtitle: Text(snapshot.data![index].body),
                );
              },
            );
          } else if (snapshot.hasError) {
            return Text("${snapshot.error}");
          }
          return CircularProgressIndicator();
        },
      ),
    );
  }
}

class Post {
  final int id;
  final String title;
  final String body;

  Post({required this.id, required this.title, required this.body});

  factory Post.fromJson(Map<String, dynamic> json) {
    return Post(id: json['id'], title: json['title'], body: json['body']);
  }
}
