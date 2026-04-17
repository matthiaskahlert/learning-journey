void main() {
  // basis ausnahmebehandlung
  try {
    int ergebnis = 10 ~/ 0; // Division durch Null
  } on UnsupportedError {
    print('Division durch Null ist nicht erlaubt');
  } catch (e) {
    print('Ein Fehler ist aufgetreten: $e');
  } finally {
    print('Aufräumarbeiten');
  }

  // allgemeiner fehler mit ausgeführtem catch block
  try {
    throw FormatException('Ungültiges Format'); // Wirft einen anderen Fehler
  } on UnsupportedError {
    print('Division durch Null ist nicht erlaubt');
  } catch (e) {
    print(
      'Ein Fehler ist aufgetreten: $e',
    ); // Dieser Block wird jetzt ausgeführt
  } finally {
    print('Aufräumarbeiten');
  }

  // eigene Exception werfen
  List<int> alterswerte = [-3, 22]; // Liste mit Alterswerten
  void pruefeAlter(int alter) {
    if (alter < 0) {
      throw ArgumentError('Alter kann nicht negativ sein');
    }
    print('Das Alter ist gültig: $alter');
  }

  for (int alter in alterswerte) {
    try {
      pruefeAlter(alter);
    } catch (e) {
      print('Fehler: $e');
    } finally {
      print('Prüfung abgeschlossen.');
    }
  }
}
