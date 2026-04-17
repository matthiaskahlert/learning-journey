void main() {
  List<int> zahlen = [1, 2, 3, 4, 5];
  List<String> namen = ['Anna', 'Ben', 'Clara'];

  // Zugriff auf Elemente
  int erstesElement = zahlen[0]; // 1
  print('Erstes Element der Liste: $erstesElement');
  String letzterName = namen[namen.length - 1]; // 'Clara'
  print('Letzter Name in der Liste: $letzterName');

  // Elemente hinzufügen und entfernen
  zahlen.add(6); // [1, 2, 3, 4, 5, 6]
  print('Liste nach Hinzufügen von 6: $zahlen');
  namen.remove('Ben'); // ['Anna', 'Clara']
  print('Liste nach Entfernen von Ben: $namen');

  // Sortieren und Iteration
  zahlen.sort();
  print('Sortierte Liste: $zahlen');
  zahlen.forEach((zahl) => print('Zahl: $zahl'));

  // Spread-Operator
  List<int> mehrZahlen = [0, ...zahlen]; // Spread-Operator
  print('Liste mit Spread-Operator: $mehrZahlen');

  // Collection-If und Collection-For
  bool includeSeven = true;
  List<int> dynamicNumbers = [1, 2, if (includeSeven) 7];
  print('Dynamische Liste: $dynamicNumbers');

  List<String> fruits = ['Apfel', 'Banane', 'Kirsche'];
  List<String> upperCaseFruits = [
    for (var fruit in fruits) fruit.toUpperCase(),
  ];
  print('Großgeschriebene Früchte: $upperCaseFruits');
}
