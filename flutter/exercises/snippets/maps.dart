void main() {
  Map<String, int> ages = {'Anna': 30, 'Ben': 25, 'Clara': 35};

  // Zugriff auf Werte
  int annasAge = ages['Anna'] ?? 0;
  print('Annas Alter: $annasAge');

  // Werte hinzufügen und entfernen
  ages['David'] = 40;
  print('Nach Hinzufügen von David: $ages');
  ages.remove('Ben');
  print('Nach Entfernen von Ben: $ages');

  // Überprüfung auf Schlüssel
  if (ages.containsKey('Clara')) {
    print('Clara ist ${ages['Clara']} Jahre alt.');
  }

  // Iteration über die Map
  ages.forEach((name, years) {
    print('$name ist $years Jahre alt.');
  });

  // Zugriff auf Einträge, Schlüssel und Werte
  Iterable<MapEntry<String, int>> entries = ages.entries;
  print('Einträge: $entries');
  Iterable<String> names = ages.keys;
  print('Namen: $names');
  Iterable<int> ageValues = ages.values;
  print('Alterswerte: $ageValues');
}
