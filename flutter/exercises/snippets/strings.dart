void main() {
  // In Dart können Strings mit einfachen oder doppelten Anführungszeichen definiert werden. Beide Möglichkeiten sind gleichwertig, und die Wahl zwischen ihnen hängt oft von der Lesbarkeit ab. Wenn ein String beispielsweise ein einfaches Anführungszeichen enthält, ist es einfacher, den String mit doppelten Anführungszeichen zu definieren, um Escape-Sequenzen zu vermeiden.
  String einfach = 'Das ist ein String mit einfachen Anführungszeichen.';
  String doppelt = "Das ist ein String mit doppelten Anführungszeichen.";
  print(einfach);
  print(doppelt);
  //multilinestrings können mit drei einfachen oder drei doppelten Anführungszeichen erstellt werden. Sie ermöglichen es, Strings über mehrere Zeilen zu erstrecken, ohne dass Escape-Sequenzen für Zeilenumbrüche erforderlich sind.
  String mehrereZeilen = '''
Dies ist ein String,
der sich über mehrere
Zeilen erstreckt.
''';
  print(mehrereZeilen);

  //rohstrings interpretieren keine Escape-Sequenzen, d.h. \n und \t werden nicht als Zeilenumbruch bzw. Tabulator interpretiert, sondern als normale Zeichen behandelt.
  String rohString =
      r'In diesem String werden \n und \t nicht als Escape-Sequenzen interpretiert.';
  print(rohString);

  //string-interpolation ermöglicht es, Variablen und Ausdrücke direkt in einen String einzufügen. Dazu wird das Dollarzeichen ($) verwendet, gefolgt von der Variablen oder einem Ausdruck in geschweiften Klammern ({}).
  String name = 'Matze';
  int alter = 45;
  String ort = 'Hamburg';
  String vorstellung =
      'Ich heiße $name, bin $alter Jahre alt und komme aus $ort.';
  print(vorstellung);
  String vorstellungKomplex =
      'In 5 Jahren werde ich ${alter + 5} Jahre alt sein und mich aber immer noch wie 25 fühlen!';
  print(vorstellungKomplex);
}
