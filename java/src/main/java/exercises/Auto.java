// Klassendefinition für ein Auto
public class Auto {
    String marke;
    String modell;
    int baujahr;
    int kilometerstand;

    // Konstruktor
    public Auto(String marke, String modell, int baujahr, int kilometerstand) {
        this.marke = marke;
        this.modell = modell;
        this.baujahr = baujahr;
        this.kilometerstand = kilometerstand;
    }

    // Methode zur Altersberechnung des Autos
    public int alterInJahren(int aktuellesJahr) {
        return aktuellesJahr - baujahr;
    }

    // Main Methode zum Testen der Auto-Klasse
    public static void main(String[] args) {
        Auto auto1 = new Auto("Volkswagen", "Golf", 2010, 150000);
        Auto auto2 = new Auto("BMW", "3er", 2015, 80000);

        System.out.println(
                "Das Auto " + auto1.marke + " " + auto1.modell + " ist " + auto1.alterInJahren(2024) + " Jahre alt.");
        System.out.println(
                "Das Auto " + auto2.marke + " " + auto2.modell + " ist " + auto2.alterInJahren(2024) + " Jahre alt.");
    }

}
