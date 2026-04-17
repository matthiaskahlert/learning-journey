void main() {
  void gruessen(name) {
    print('Hallo $name!');
  }

  gruessen('Matthias'); // Aufruf der Funktion
  // funktion mit rückgabewert
  int addieren(int a, int b) {
    return a + b;
  }

  int ergebnis = addieren(5, 3); // Aufruf der Funktion
  print('Das Ergebnis der Addition ist: $ergebnis');
  // funktion mit optionalen parameter
  void gruessenOptional(String name, [String? titel]) {
    if (titel != null) {
      print('Hallo, $titel $name!');
    } else {
      print('Hallo, $name!');
    }
  }

  // Aufruf der Funktion mit und ohne optionalem Parameter
  gruessenOptional('Matthias');
  gruessenOptional('Matthias', 'Dr.');
  // funktion mit benannten parameter
  void personErstellen({
    required String name,
    required int alter,
    String? beruf,
  }) {
    print('Name: $name, Alter: $alter');
    if (beruf != null) {
      print('Beruf: $beruf');
    }
  }

  personErstellen(name: 'Matthias', alter: 45, beruf: 'Softwareentwickler');
  //anonyme funktionen
  var quadrieren = (int x) => x * x;
  print(quadrieren(4)); // 16

  void applyOperation(int a, int b, int Function(int, int) operation) {
    print('Ergebnis: ${operation(a, b)}');
  }

  applyOperation(4, 2, (a, b) => a + b); // Ergebnis: 6
}
