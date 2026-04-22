// a) Definiere eine Klasse Person
class Person {
  String name;
  int alter;
  String? email;

  Person({required this.name, required this.alter, this.email});
}

// b) Erstelle eine Funktion holePersonenDaten
Future<List<Person>> holePersonenDaten() async {
  try {
    return await Future.delayed(
      Duration(seconds: 2),
      () => [
        Person(name: 'Alice', alter: 25, email: 'alice@example.com'),
        Person(name: 'Bob', alter: 30, email: null),
        Person(name: 'Charlie', alter: 35, email: 'charlie@example.com'),
      ],
    );
  } catch (e) {
    throw Exception('Fehler beim Abrufen der Daten: $e');
  }
}

// c) Verwende die map-Methode
List<String> verarbeitePersonenDaten(List<Person> personen) {
  return personen
      .where((person) => person.email != null)
      .map((person) => 'Name: ${person.name}, Alter: ${person.alter}')
      .toList();
}

// d) Demonstriere die Verwendung von async und await in der main-Funktion
void main() async {
  try {
    List<Person> personen = await holePersonenDaten();
    List<String> ergebnisse = verarbeitePersonenDaten(personen);
    print('Verarbeitete Daten:');
    ergebnisse.forEach(print);
  } catch (e) {
    print('Fehler: $e');
  }
}
