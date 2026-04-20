import 'dart:collection';

void main() {
  // Erstellen einer Queue
  Queue<String> warteschlange = Queue<String>();

  // Elemente hinzufügen
  warteschlange.add('Erster'); // Fügt am Ende hinzu
  warteschlange.add('Zweiter');
  warteschlange.addFirst('Neuer Erster'); // Fügt am Anfang hinzu
  warteschlange.addLast('Letzter'); // Fügt am Ende hinzu
  print(warteschlange); // (Neuer Erster, Erster, Zweiter, Letzter)

  // Elemente entfernen
  String erster = warteschlange.removeFirst(); // 'Neuer Erster'
  String letzter = warteschlange.removeLast(); // 'Letzter'
  print(warteschlange); // (Erster, Zweiter)

  // Queue durchlaufen
  for (var element in warteschlange) {
    print(element);
  }
}
