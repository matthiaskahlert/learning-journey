// Entwickle ein einfaches Dart-Programm, das folgende Anforderungen erfüllt:

// a) Definiere eine Variable alter vom Typ int und weise ihr dein Alter zu.

// b) Definiere eine Variable name vom Typ String und weise ihr deinen Namen zu.

// c) Definiere eine Variable istStudent vom Typ bool und weise ihr den Wert true zu, wenn du ein Student bist, andernfalls false.

// d) Erstelle eine Liste lieblingsfächer vom Typ String, die mindestens drei deiner Lieblingsfächer enthält.

// e) Verwende die Variablen alter, name, und istStudent sowie die Liste lieblingsfächer,
//um eine Ausgabe in der Konsole zu erzeugen, die folgendes Format hat:
//"Hallo, mein Name ist [name], ich bin [alter] Jahre alt und es ist [istStudent], dass ich ein Student bin. Meine Lieblingsfächer sind: [lieblingsfächer]."

// f) Füge eine Null-Safety-Überprüfung für die Variable name hinzu, um sicherzustellen, dass sie nicht null ist, bevor du sie verwendest. Falls name null ist, soll stattdessen "Anonym" ausgegeben werden.

void main() {
  int alter = 45;
  // String? name = "Max"; // nullable: kann null sein oder einen Wert haben
  String? name = null; // Testfall: gibt "Anonym" aus
  bool istStudent = false;
  List<String> Lieblingsfaecher = ["Physik", "Sport", "Geschichte"];
  print(
    "Hallo, mein Name ist ${name ?? "Anonym"}, ich bin $alter Jahre alt und es ist $istStudent, dass ich ein Student bin. Meine Lieblingsfächer sind: ${Lieblingsfaecher.join(", ")}.",
  );
}
