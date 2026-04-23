// a) Definiere eine Klasse Task mit den Eigenschaften name (String), deadline (DateTime), und completed (bool).
//Implementiere einen Konstruktor, der alle Eigenschaften initialisiert,
//und eine Methode markAsCompleted(), die completed auf true setzt.

// b) Verwende Generics, um eine Liste von Task-Objekten zu erstellen.

// c) Implementiere eine Funktion addTask, die eine neue Task zur Liste hinzufügt.
//Die Funktion soll name und deadline als Parameter haben
//und die completed-Eigenschaft standardmäßig auf false setzen.

// d) Erstelle eine asynchrone Funktion fetchTasks, die simuliert,
//dass sie die Aufgabenliste aus einer externen Quelle lädt.
//Verwende Future.delayed mit einer Verzögerung von 2 Sekunden,
//um eine vordefinierte Liste von Task-Objekten zurückzugeben.

// e) Benutze async und await, um fetchTasks aufzurufen,
//und drucke anschließend alle Aufgaben und deren Status in der Konsole aus.

// f) Implementiere eine Funktion completeTask,
//die den Namen einer Aufgabe als Parameter nimmt
//und diese Aufgabe in der Liste als abgeschlossen markiert.
//Verwende eine Lambda-Funktion, um die entsprechende Aufgabe in der Liste zu finden und zu aktualisieren.

// a) Klasse Task
class Task {
  String name;
  DateTime deadline;
  bool completed;

  Task({required this.name, required this.deadline, this.completed = false});

  void markAsCompleted() {
    completed = true;
  }
}

// b) Generische Liste für die Aufgaben
List<Task> taskList = [];

// c) Fügt eine neue Aufgabe mit completed = false hinzu.
void addTask(String name, DateTime deadline) {
  taskList.add(Task(name: name, deadline: deadline));
}

// d) Simuliert das Laden von Aufgaben aus einer externen Quelle.
Future<List<Task>> fetchTasks() async {
  await Future.delayed(Duration(seconds: 2));
  return [
    Task(
      name: 'Projektportfolio fertigstellen',
      deadline: DateTime.now().add(Duration(days: 1)),
    ),
    Task(
      name: 'Weitere Bewerbungen schreiben',
      deadline: DateTime.now().add(Duration(days: 2)),
    ),
  ];
}

// e) Lädt Aufgaben asynchron und gibt sie in der Konsole aus.
Future<void> printTasks() async {
  List<Task> tasks = await fetchTasks();
  for (var task in tasks) {
    print(
      'Name: ${task.name}, Fällig bis: ${task.deadline.toString().split('.').first} Uhr, Erledigt: ${task.completed}',
    );
  }
}

// f) Markiert eine Aufgabe pro Name als erledigt (Lambda in firstWhere).
void completeTask(String name) {
  taskList.firstWhere((task) => task.name == name).markAsCompleted();
}

void main() async {
  addTask('Dart lernen', DateTime.now().add(Duration(days: 3)));
  addTask('Flutter-Projekt abschließen', DateTime.now().add(Duration(days: 7)));

  print('Aufgaben werden geladen...');
  await printTasks();

  completeTask('Dart lernen');
  print('\nAktualisierte Aufgabenliste:');
  for (var task in taskList) {
    print(
      'Name: ${task.name}, Fällig bis: ${task.deadline.toString().split('.').first} Uhr, Erledigt: ${task.completed}',
    );
  }
}
