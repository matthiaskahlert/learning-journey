// a) Definiere Variablen für die Marke (String), das Modell (String),
//das Baujahr (int), ob das Auto neu oder gebraucht ist (bool)
//und den Kilometerstand (int?), wobei der Kilometerstand optional ist,
//da neue Autos keinen Kilometerstand haben.

// b) Implementiere einen Konstruktor, der alle Variablen außer dem Kilometerstand als Parameter erfordert.
//Der Kilometerstand soll über einen benannten Parameter gesetzt werden können,
//der standardmäßig null ist.

// c) Füge eine Methode zeigeDetails() hinzu, die die Details des Autos in der Konsole ausgibt.
//Wenn das Auto neu ist, soll "Neuwagen" statt des Kilometerstands ausgegeben werden.

// d) Erstelle eine Methode alterDesAutos(), die das Alter des Autos basierend auf dem aktuellen Jahr
//(angenommen 2023) berechnet und zurückgibt.
void main() {
  Auto auto1 = Auto('Volkswagen', 'Golf', 2020, false, kilometerstand: 15000);
  Auto auto2 = Auto('Tesla', 'Model 3', 2023, true);

  auto1.zeigeDetails();
  print('Alter des Autos: ${auto1.alterDesAutos()} Jahre\n');

  auto2.zeigeDetails();
  print('Alter des Autos: ${auto2.alterDesAutos()} Jahre');
}

class Auto {
  String marke;
  String modell;
  int baujahr;
  bool istNeu;
  int? kilometerstand; //Benannter Parameter, da er optional ist

  Auto(
    this.marke,
    this.modell,
    this.baujahr,
    this.istNeu, {
    this.kilometerstand, //Optionaler benannter Parameter mit Standardwert null
  });

  void zeigeDetails() {
    //Methode zum Ausgeben der Autodetails
    print('Marke: $marke');
    print('Modell: $modell');
    print('Baujahr: $baujahr');
    print('Zustand: ${istNeu ? 'Neuwagen' : 'Gebrauchtwagen'}');
    if (!istNeu) {
      print('Kilometerstand: ${kilometerstand ?? 'Nicht verfügbar'} km');
    }
  }

  int alterDesAutos() {
    return 2023 - baujahr;
  }
}
