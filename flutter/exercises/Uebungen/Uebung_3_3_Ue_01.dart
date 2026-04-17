// Entwickle eine Dart-Funktion, die eine Liste von Zahlen entgegennimmt
//und zwei Operationen ausführt:
//Erstens soll sie die Summe aller Zahlen berechnen
//und zweitens soll sie eine neue Liste zurückgeben,
//in der jede Zahl mit 2 multipliziert wurde.
//Verwende für diese Übung die Dart-Syntax und Grundkonzepte,
//die du gelernt hast, einschließlich Variablen, Datentypen,
//Null Safety und Funktionen. Achte darauf, dass deine Funktion gut strukturiert ist
//und effizient arbeitet.
void main() {
  List<int> zahlen = [1, 2, 3, 4, 5];
  var ergebnis = berechneSummeUndMultipliziere(zahlen);
  print('Die Summe der Zahlen ist: ${ergebnis['summe']}');
  print(
    'Die neue Liste mit multiplizierten Zahlen ist: ${ergebnis['multiplizierteZahlen']}',
  );
}

Map<String, dynamic> berechneSummeUndMultipliziere(List<int> zahlen) {
  int summe = 0;
  List<int> multiplizierteZahlen = [];

  for (int zahl in zahlen) {
    summe += zahl;
    multiplizierteZahlen.add(zahl * 2);
  }

  return {'summe': summe, 'multiplizierteZahlen': multiplizierteZahlen};
}


