// Einfache Klasse
class Person {
  // Felder (Instanzvariablen)
  String name;
  int alter;
  // Konstruktor
  Person(this.name, this.alter);
  // Methode
  void vorstellen() {
    print('Hallo, ich bin $name und $alter Jahre alt.');
  }
}

// Verwendung der Klasse
void main() {
  // Erstellung eines Objekts (Instanz)
  var person = Person('Anna', 30);
  // Zugriff auf Felder
  print(person.name); // 'Anna'
  print(person.alter); // 30
  // Aufruf einer Methode
  person.vorstellen(); // 'Hallo, ich bin Anna und 30 Jahre alt.'
  // Ändern von Feldern
  person.alter = 31;
  person.vorstellen(); // 'Hallo, ich bin Anna und 31 Jahre alt.'
}
