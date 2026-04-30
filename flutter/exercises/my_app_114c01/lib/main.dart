// Entwickle eine Flutter-App, die eine ToDo-Liste verwaltet. Die App soll folgende Funktionalitäten umfassen:

// a) Eine Startseite, die eine Liste von ToDo-Einträgen anzeigt. Jeder Eintrag soll aus einer Beschreibung und einem Status (erledigt/nicht erledigt) bestehen. Nutze eine Test-API wie https://reqres.in/ für das Abrufen der ToDo-Einträge.

// b) Die Möglichkeit, neue ToDo-Einträge über ein Formular hinzuzufügen. Die Daten sollen per POST-Request an die Test-API gesendet werden.

// c) Die Möglichkeit, den Status eines ToDo-Eintrags (erledigt/nicht erledigt) zu ändern. Dies soll durch einen PATCH-Request an die Test-API realisiert werden.

// d) Eine Detailansicht für jeden ToDo-Eintrag, die nach dem Tippen auf einen Eintrag in der Liste geöffnet wird. Diese Ansicht soll zusätzliche Informationen zum ToDo-Eintrag anzeigen und die Möglichkeit bieten, den Eintrag zu bearbeiten oder zu löschen.

// e) Eine Fehlerbehandlung, die dem Benutzer eine Nachricht anzeigt, falls die Kommunikation mit der API fehlschlägt
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:provider/provider.dart';

void main() {
  runApp(
    ChangeNotifierProvider(create: (_) => TodoProvider(), child: const MyApp()),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ToDo App mit API',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const HomePage(),
    );
  }
}

class TodoItem {
  final String id;
  final String description;
  final bool completed;

  const TodoItem({
    required this.id,
    required this.description,
    this.completed = false,
  });

  factory TodoItem.fromJson(Map<String, dynamic> json) {
    return TodoItem(
      id: json['id'].toString(),
      description: (json['description'] ?? json['name'] ?? '').toString(),
      completed: json['completed'] == true,
    );
  }

  Map<String, dynamic> toJson() {
    return {'id': id, 'description': description, 'completed': completed};
  }

  TodoItem copyWith({String? id, String? description, bool? completed}) {
    return TodoItem(
      id: id ?? this.id,
      description: description ?? this.description,
      completed: completed ?? this.completed,
    );
  }
}

class ApiService {
  static const String baseUrl = 'https://reqres.in/api';
  static const String fallbackBaseUrl = 'https://jsonplaceholder.typicode.com';
  static const String reqresApiKey = 'reqres-free-v1';

  static Map<String, String> get _headers => {'x-api-key': reqresApiKey};

  static Map<String, String> get _jsonHeaders => {
    'Content-Type': 'application/json',
    'x-api-key': reqresApiKey,
  };

  static Future<List<TodoItem>> getTodos() async {
    try {
      final response = await http.get(
        Uri.parse('$baseUrl/users?page=1'),
        headers: _headers,
      );

      if (response.statusCode == 200) {
        final Map<String, dynamic> data =
            json.decode(response.body) as Map<String, dynamic>;
        final List<dynamic> todosList = data['data'] as List<dynamic>? ?? [];
        return todosList
            .map(
              (todoJson) =>
                  TodoItem.fromJson(Map<String, dynamic>.from(todoJson as Map)),
            )
            .toList();
      }

      if (response.statusCode == 401 || response.statusCode == 403) {
        final fallbackResponse = await http.get(
          Uri.parse('$fallbackBaseUrl/posts?_limit=10'),
        );
        if (fallbackResponse.statusCode == 200) {
          final List<dynamic> fallbackList =
              json.decode(fallbackResponse.body) as List<dynamic>;
          return fallbackList
              .map(
                (item) => TodoItem(
                  id: item['id'].toString(),
                  description: (item['title'] ?? '').toString(),
                  completed: false,
                ),
              )
              .toList();
        }
      }

      throw Exception('Failed to load todos: ${response.statusCode}');
    } catch (e) {
      throw Exception('Error getting todos: $e');
    }
  }

  static Future<TodoItem> addTodo(TodoItem todo) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/users'),
        headers: _jsonHeaders,
        body: json.encode(todo.toJson()),
      );

      if (response.statusCode == 201 || response.statusCode == 200) {
        final Map<String, dynamic> data =
            json.decode(response.body) as Map<String, dynamic>;
        return TodoItem.fromJson(data).copyWith(
          id: data['id']?.toString() ?? todo.id,
          description: todo.description,
          completed: todo.completed,
        );
      }

      if (response.statusCode == 401 || response.statusCode == 403) {
        return todo;
      }

      throw Exception('Failed to add todo: ${response.statusCode}');
    } catch (e) {
      throw Exception('Error adding todo: $e');
    }
  }

  static Future<TodoItem> updateTodo(TodoItem todo) async {
    try {
      final response = await http.patch(
        Uri.parse('$baseUrl/users/${todo.id}'),
        headers: _jsonHeaders,
        body: json.encode(todo.toJson()),
      );

      if (response.statusCode == 200) {
        return todo;
      }

      if (response.statusCode == 401 || response.statusCode == 403) {
        return todo;
      }

      throw Exception('Failed to update todo: ${response.statusCode}');
    } catch (e) {
      throw Exception('Error updating todo: $e');
    }
  }

  static Future<void> deleteTodo(String id) async {
    try {
      final response = await http.delete(
        Uri.parse('$baseUrl/users/$id'),
        headers: _headers,
      );

      if (response.statusCode != 204 && response.statusCode != 200) {
        if (response.statusCode == 401 || response.statusCode == 403) {
          return;
        }
        throw Exception('Failed to delete todo: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Error deleting todo: $e');
    }
  }
}

class TodoProvider extends ChangeNotifier {
  List<TodoItem> _todos = [];
  bool _isLoading = false;
  String? _error;

  List<TodoItem> get todos => _todos;
  bool get isLoading => _isLoading;
  String? get error => _error;

  Future<void> fetchTodos() async {
    _setLoading(true);
    _clearError();
    try {
      final fetchedTodos = await ApiService.getTodos();
      _todos = fetchedTodos;
      notifyListeners();
    } catch (e) {
      _setError(e.toString());
    } finally {
      _setLoading(false);
    }
  }

  Future<void> addTodo(TodoItem todo) async {
    _setLoading(true);
    _clearError();
    try {
      final newTodo = await ApiService.addTodo(todo);
      _todos = [..._todos, newTodo];
      notifyListeners();
    } catch (e) {
      _setError(e.toString());
    } finally {
      _setLoading(false);
    }
  }

  Future<void> updateTodo(TodoItem todo) async {
    _setLoading(true);
    _clearError();
    try {
      final updatedTodo = await ApiService.updateTodo(todo);
      final index = _todos.indexWhere((t) => t.id == updatedTodo.id);
      if (index != -1) {
        _todos[index] = updatedTodo;
        notifyListeners();
      }
    } catch (e) {
      _setError(e.toString());
    } finally {
      _setLoading(false);
    }
  }

  Future<void> toggleTodoStatus(TodoItem todo) async {
    await updateTodo(todo.copyWith(completed: !todo.completed));
  }

  Future<void> deleteTodo(String id) async {
    _setLoading(true);
    _clearError();
    try {
      await ApiService.deleteTodo(id);
      _todos.removeWhere((todo) => todo.id == id);
      notifyListeners();
    } catch (e) {
      _setError(e.toString());
    } finally {
      _setLoading(false);
    }
  }

  void _setLoading(bool loading) {
    _isLoading = loading;
    notifyListeners();
  }

  void _setError(String errorMessage) {
    _error = errorMessage;
    notifyListeners();
  }

  void _clearError() {
    _error = null;
    notifyListeners();
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => HomePageState();
}

class HomePageState extends State<HomePage> {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      Provider.of<TodoProvider>(context, listen: false).fetchTodos();
    });
  }

  Future<void> _openAddTodoPage() async {
    await Navigator.push(
      context,
      MaterialPageRoute(builder: (_) => const AddTodoPage()),
    );
    if (!mounted) {
      return;
    }
    await Provider.of<TodoProvider>(context, listen: false).fetchTodos();
  }

  Future<void> _openTodoDetailPage(TodoItem todo) async {
    await Navigator.push(
      context,
      MaterialPageRoute(builder: (_) => TodoDetailPage(todo: todo)),
    );
    if (!mounted) {
      return;
    }
    await Provider.of<TodoProvider>(context, listen: false).fetchTodos();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('ToDo Liste')),
      body: Consumer<TodoProvider>(
        builder: (context, todoProvider, _) {
          if (todoProvider.error != null) {
            return Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Icon(Icons.error_outline, color: Colors.red, size: 48),
                  const SizedBox(height: 16),
                  const Text(
                    'Ein Fehler ist aufgetreten:',
                    style: TextStyle(fontSize: 16),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    todoProvider.error!,
                    textAlign: TextAlign.center,
                    style: const TextStyle(color: Colors.red),
                  ),
                  const SizedBox(height: 16),
                  ElevatedButton(
                    onPressed: todoProvider.fetchTodos,
                    child: const Text('Erneut versuchen'),
                  ),
                ],
              ),
            );
          }

          if (todoProvider.isLoading && todoProvider.todos.isEmpty) {
            return const Center(child: CircularProgressIndicator());
          }

          if (todoProvider.todos.isEmpty) {
            return const Center(child: Text('Keine Aufgaben vorhanden'));
          }

          return ListView.builder(
            itemCount: todoProvider.todos.length,
            itemBuilder: (context, index) {
              final todo = todoProvider.todos[index];
              return Card(
                margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                child: ListTile(
                  leading: Checkbox(
                    value: todo.completed,
                    onChanged: (_) => todoProvider.toggleTodoStatus(todo),
                  ),
                  title: Text(
                    todo.description,
                    style: TextStyle(
                      decoration: todo.completed
                          ? TextDecoration.lineThrough
                          : null,
                    ),
                  ),
                  onTap: () => _openTodoDetailPage(todo),
                ),
              );
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _openAddTodoPage,
        child: const Icon(Icons.add),
      ),
    );
  }
}

class AddTodoPage extends StatefulWidget {
  const AddTodoPage({super.key});

  @override
  State<AddTodoPage> createState() => AddTodoPageState();
}

class AddTodoPageState extends State<AddTodoPage> {
  final _formKey = GlobalKey<FormState>();
  final _descriptionController = TextEditingController();
  bool _isCompleted = false;

  @override
  void dispose() {
    _descriptionController.dispose();
    super.dispose();
  }

  Future<void> _submitForm() async {
    final formState = _formKey.currentState;
    if (formState == null || !formState.validate()) {
      return;
    }

    final newTodo = TodoItem(
      id: DateTime.now().millisecondsSinceEpoch.toString(),
      description: _descriptionController.text.trim(),
      completed: _isCompleted,
    );

    try {
      await Provider.of<TodoProvider>(context, listen: false).addTodo(newTodo);
      if (!mounted) {
        return;
      }
      Navigator.pop(context);
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Aufgabe erfolgreich hinzugefügt'),
          backgroundColor: Colors.green,
        ),
      );
    } catch (error) {
      if (!mounted) {
        return;
      }
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Fehler beim Hinzufügen: $error'),
          backgroundColor: Colors.red,
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Neue Aufgabe')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              TextFormField(
                controller: _descriptionController,
                decoration: const InputDecoration(
                  labelText: 'Beschreibung',
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null || value.trim().isEmpty) {
                    return 'Bitte geben Sie eine Beschreibung ein';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              Row(
                children: [
                  Checkbox(
                    value: _isCompleted,
                    onChanged: (value) {
                      setState(() {
                        _isCompleted = value ?? false;
                      });
                    },
                  ),
                  const Text('Bereits erledigt'),
                ],
              ),
              const SizedBox(height: 32),
              ElevatedButton(
                onPressed: _submitForm,
                child: const Text('Aufgabe hinzufügen'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class TodoDetailPage extends StatefulWidget {
  final TodoItem todo;

  const TodoDetailPage({super.key, required this.todo});

  @override
  State<TodoDetailPage> createState() => TodoDetailPageState();
}

class TodoDetailPageState extends State<TodoDetailPage> {
  late TextEditingController _descriptionController;
  late bool _isCompleted;

  @override
  void initState() {
    super.initState();
    _descriptionController = TextEditingController(
      text: widget.todo.description,
    );
    _isCompleted = widget.todo.completed;
  }

  @override
  void dispose() {
    _descriptionController.dispose();
    super.dispose();
  }

  Future<void> _updateTodo() async {
    final updatedTodo = widget.todo.copyWith(
      description: _descriptionController.text.trim(),
      completed: _isCompleted,
    );

    try {
      await Provider.of<TodoProvider>(
        context,
        listen: false,
      ).updateTodo(updatedTodo);
      if (!mounted) {
        return;
      }
      Navigator.pop(context);
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Aufgabe erfolgreich aktualisiert'),
          backgroundColor: Colors.green,
        ),
      );
    } catch (error) {
      if (!mounted) {
        return;
      }
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Fehler beim Aktualisieren: $error'),
          backgroundColor: Colors.red,
        ),
      );
    }
  }

  Future<void> _deleteTodo() async {
    final todoProvider = Provider.of<TodoProvider>(context, listen: false);
    final confirm = await showDialog<bool>(
      context: context,
      builder: (dialogContext) => AlertDialog(
        title: const Text('Aufgabe löschen'),
        content: const Text('Möchten Sie diese Aufgabe wirklich löschen?'),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(dialogContext, false),
            child: const Text('Abbrechen'),
          ),
          TextButton(
            onPressed: () => Navigator.pop(dialogContext, true),
            child: const Text('Löschen', style: TextStyle(color: Colors.red)),
          ),
        ],
      ),
    );

    if (confirm != true) {
      return;
    }

    try {
      await todoProvider.deleteTodo(widget.todo.id);
      if (!mounted) {
        return;
      }
      Navigator.pop(context);
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Aufgabe erfolgreich gelöscht'),
          backgroundColor: Colors.green,
        ),
      );
    } catch (error) {
      if (!mounted) {
        return;
      }
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Fehler beim Löschen: $error'),
          backgroundColor: Colors.red,
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Aufgabendetails'),
        actions: [
          IconButton(icon: const Icon(Icons.delete), onPressed: _deleteTodo),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Beschreibung:',
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            TextFormField(
              controller: _descriptionController,
              decoration: const InputDecoration(border: OutlineInputBorder()),
            ),
            const SizedBox(height: 16),
            Row(
              children: [
                Checkbox(
                  value: _isCompleted,
                  onChanged: (value) {
                    setState(() {
                      _isCompleted = value ?? false;
                    });
                  },
                ),
                const Text('Erledigt'),
              ],
            ),
            const SizedBox(height: 16),
            const Text(
              'ID:',
              style: TextStyle(fontSize: 14, fontWeight: FontWeight.bold),
            ),
            Text(widget.todo.id),
            const SizedBox(height: 32),
            ElevatedButton(
              onPressed: _updateTodo,
              style: ElevatedButton.styleFrom(
                minimumSize: const Size(double.infinity, 50),
              ),
              child: const Text('Änderungen speichern'),
            ),
          ],
        ),
      ),
    );
  }
}
