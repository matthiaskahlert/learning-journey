
/* Entwickle eine Java-Klasse Fahrzeug, die als Basis für verschiedene Fahrzeugtypen dienen soll.
Die Klasse soll private Attribute für die Marke, das Modell und das Baujahr haben.

Erstelle einen Konstruktor, der diese drei Eigenschaften initialisiert.
Des Weiteren soll die Klasse eine Methode zeigeDetails() haben,
die Informationen über das Fahrzeug ausgibt.

Erweitere dann das Programm um eine Unterklasse Auto, die von Fahrzeug erbt
und zusätzliche Attribute wie Kraftstoffart und Anzahl der Türen enthält.
Implementiere in der Unterklasse einen eigenen Konstruktor,
der die Attribute der Basisklasse sowie die neuen Attribute initialisiert.
Die Methode zeigeDetails() soll überschrieben werden, um alle Informationen des Autos anzuzeigen.

a) Definiere die Klasse Fahrzeug mit den entsprechenden Attributen und Methoden.

b) Definiere die Klasse Auto als Unterklasse von Fahrzeug und erweitere sie
um die spezifischen Attribute und Methoden.

c) Erstelle in der main-Methode zwei Instanzen von Auto mit unterschiedlichen Eigenschaften
und rufe die Methode zeigeDetails() für beide Instanzen auf. */
package FahrzeugKlasse;

public class Main {
    public static void main(String[] args) {
        Auto auto1 = new Auto("Volkswagen", "Golf", 2020, "Benzin", 4);
        Auto auto2 = new Auto("Tesla", "Model 3", 2021, "Elektro", 4);

        System.out.println("Details von Auto 1:");
        auto1.zeigeDetails();
        System.out.println();
        System.out.println("Details von Auto 2:");
        auto2.zeigeDetails();
    }
}

class Fahrzeug {
    private String marke;
    private String modell;
    private int baujahr;

    // Konstruktor
    public Fahrzeug(String marke, String modell, int baujahr) {
        this.marke = marke;
        this.modell = modell;
        this.baujahr = baujahr;
    }

    public void zeigeDetails() {
        System.out.println("Marke: " + marke);
        System.out.println("Modell: " + modell);
        System.out.println("Baujahr: " + baujahr);
    }

}

class Auto extends Fahrzeug {
    private String kraftstoffart;
    private int tueranzahl;

    // Konstruktor
    public Auto(String marke, String modell, int baujahr, String kraftstoffart, int tueranzahl) {
        // super(...) weil die Attribute marke, modell und baujahr in der Basisklasse
        // Fahrzeug definiert sind.
        super(marke, modell, baujahr); // ← ruft Fahrzeug-Konstruktor auf
        this.kraftstoffart = kraftstoffart;
        this.tueranzahl = tueranzahl;
    }

    // Override weil die Methode zeigeDetails() in der Unterklasse Auto eine andere
    // Implementierung hat als in der Basisklasse Fahrzeug.
    @Override
    public void zeigeDetails() {
        super.zeigeDetails(); // ← ruft die Methode der Elternklasse auf. ohne super(...) würden Marke, Modell
                              // und Baujahr nicht angezeigt werden, da die Methode in Auto die Methode in
                              // Fahrzeug überschreibt.
        System.out.println("Kraftstoffart: " + kraftstoffart);
        System.out.println("Anzahl der Türen: " + tueranzahl);
    }
}

/*
 * Details von Auto 1:
 * Marke: Volkswagen
 * Modell: Golf
 * Baujahr: 2020
 * Kraftstoffart: Benzin
 * Anzahl der Türen: 4
 * 
 * Details von Auto 2:
 * Marke: Tesla
 * Modell: Model 3
 * Baujahr: 2021
 * Kraftstoffart: Elektro
 * Anzahl der Türen: 4
 */
