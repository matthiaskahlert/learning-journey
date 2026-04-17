void main() {
  String? nullableString = null;
  print('nullableString: $nullableString'); // nullableString ist null.

  // ?? ersetzt null durch einen Standardwert.
  String nichtNull = nullableString ?? 'Standardwert';
  print('nichtNull: $nichtNull'); // nichtNull ist 'Standardwert'.

  // ?. verhindert einen Fehler und gibt null zurück, wenn der linke Wert null ist.
  String? laenge = nullableString?.length.toString();
  print('laenge: $laenge'); // laenge ist null, da nullableString null ist.
}
