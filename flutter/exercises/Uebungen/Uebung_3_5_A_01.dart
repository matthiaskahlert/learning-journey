// Entwickle eine Dart-Anwendung, die ein einfaches Adressbuch verwaltet.
//Dein Adressbuch soll die Möglichkeit bieten, neue Kontakte hinzuzufügen,
//bestehende Kontakte zu suchen und die Details eines Kontakts zu aktualisieren.
//Nutze dabei die Konzepte der objektorientierten Programmierung,
//Collections und Generics. Folge diesen Schritten:

// a) Definiere eine Klasse Kontakt, die mindestens die Eigenschaften name (String) und telefonnummer (String) hat. Stelle sicher, dass die Klasse einen Konstruktor besitzt, der beide Eigenschaften als Parameter akzeptiert.

class Kontakt {
  String name;
  String telefonnummer;

  Kontakt(this.name, this.telefonnummer);

  @override
  String toString() => 'Name: $name, Telefonnummer: $telefonnummer';
}

// b) Erstelle eine Klasse Adressbuch, die eine Liste von Kontakt-Objekten verwaltet.
class Adressbuch {
  final List<Kontakt> _kontakte = [];

  void neuerKontakt(Kontakt kontakt) {
    _kontakte.add(kontakt);
  }

  Kontakt? sucheKontakt(String name) {
    for (var kontakt in _kontakte) {
      if (kontakt.name == name) {
        return kontakt;
      }
    }
    return null;
  }

  bool aktualisiereKontakt(String name, String neueTelefonnummer) {
    var kontakt = sucheKontakt(name);
    if (kontakt != null) {
      kontakt.telefonnummer = neueTelefonnummer;
      return true;
    }
    return false;
  }
}

void main() {
  var adressbuch = Adressbuch();

  // Kontakte hinzufügen
  adressbuch.neuerKontakt(Kontakt('Anna', '123456'));
  adressbuch.neuerKontakt(Kontakt('Bernd', '654321'));
  adressbuch.neuerKontakt(Kontakt('Clara', '111222'));

  // Suche nach Kontakt
  var kontakt = adressbuch.sucheKontakt('Bernd');
  if (kontakt != null) {
    print('Gefundener Kontakt: $kontakt');
  } else {
    print('Kontakt nicht gefunden.');
  }

  // Aktualisiere Kontakt
  bool aktualisiert = adressbuch.aktualisiereKontakt('Bernd', '999888');
  if (aktualisiert) {
    print('Telefonnummer aktualisiert.');
    print('Neuer Kontakt: ${adressbuch.sucheKontakt('Bernd')}');
  } else {
    print('Kontakt zum Aktualisieren nicht gefunden.');
  }

  // Suche nach nicht vorhandenem Kontakt
  var nichtGefunden = adressbuch.sucheKontakt('Dieter');
  print(nichtGefunden == null ? 'Dieter nicht gefunden.' : nichtGefunden);
}
