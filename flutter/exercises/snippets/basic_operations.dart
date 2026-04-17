void main() {
  int a = 10;
  int b = 3;
  int summe = a + b; // 13
  int differenz = a - b; // 7
  int produkt = a * b; // 30
  double quotient = a / b; // 3.3333...
  int ganzzahlQuotient = a ~/ b; // 3 (ganzzahlige Division)
  int rest = a % b; // 1 (Modulo/Rest)
  print('Summe: $summe');
  print('Differenz: $differenz');
  print('Produkt: $produkt');
  print('Quotient: $quotient');
  print('Ganzzahliger Quotient: $ganzzahlQuotient');
  print('Rest: $rest');

  // inkrement und dekrement
  a++; // a = a + 1
  b--; // b = b - 1
  print('Inkrementiertes a: $a'); // 11
  print('Dekrementiertes b: $b'); // 2

  // Boolsche Operatoren
  bool istGleich = a == b; // false
  bool istNichtGleich = a != b; // true
  bool istGroesser = a > b; // true
  bool istKleiner = a < b; // false
  bool istGroesserGleich = a >= b; // true
  bool istKleinerGleich = a <= b; // false
  print('"a == b" Ist gleich: $istGleich');
  print('"a != b" Ist nicht gleich: $istNichtGleich');
  print('"a > b" Ist größer: $istGroesser');
  print('"a < b" Ist kleiner: $istKleiner');
  print('"a >= b" Ist größer oder gleich: $istGroesserGleich');
  print('"a <= b" Ist kleiner oder gleich: $istKleinerGleich');
  // kombinierte zuweisungsoperatoren

  int c = 5;
  c += 2; // c = c + 2 = 7
  print(c);
  c -= 1; // c = c - 1 = 6
  print(c);
  c *= 3; // c = c * 3 = 18
  print(c);
  c ~/= 2; // c = c ~/ 2 = 9 (ganzzahlige Division)
  print(c);
  c %= 4; // c = c % 4 = 1 (Modulo)
  print(c);
}
