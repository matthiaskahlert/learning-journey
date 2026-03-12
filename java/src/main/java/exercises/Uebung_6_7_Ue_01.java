/* 
Entwickle eine abstrakte Klasse Fahrzeug mit den Attributen marke, modell und farbe. 
Implementiere in dieser Klasse einen Konstruktor, der alle drei Attribute initialisiert. 
Zusätzlich soll die Klasse zwei abstrakte Methoden anzeigenInformationen() und berechneReichweite() beinhalten. 
Die Methode anzeigenInformationen() gibt die Attribute des Fahrzeugs in einem formatierten String zurück, 
während berechneReichweite() die Reichweite des Fahrzeugs basierend auf dem aktuellen Kraftstoffvorrat und dem Verbrauch berechnet.

a) Erstelle eine konkrete Klasse Elektroauto, die von Fahrzeug erbt und die abstrakten Methoden implementiert. 
Die Klasse Elektroauto soll zusätzlich das Attribut batteriekapazität (in kWh) beinhalten. 
Die Reichweite soll als das Produkt aus Batteriekapazität und einer Effizienzkonstante berechnet werden, 
die angibt, wie viele Kilometer das Auto pro kWh zurücklegen kann.

b) Schreibe eine Testklasse mit einer main-Methode, in der du ein Objekt der Klasse Elektroauto erstellst 
und die Methoden anzeigenInformationen() und berechneReichweite() aufrufst. 
Verwende für die Effizienzkonstante den Wert 6 km/kWh. 
*/

public class Uebung_6_7_Ue_01 {
    abstract class Fahrzeug {
        String marke;
        String modell;
        String farbe;

        public Fahrzeug(String marke, String modell, String farbe) {
            this.marke = marke;
            this.modell = modell;
            this.farbe = farbe;
        }

        // Abstrakte Methode zur Anzeige der Fahrzeuginformationen
        public abstract String anzeigenInformationen();

        // Abstrakte Methode zur Berechnung der Reichweite
        public abstract double berechneReichweite();
    }

    class Elektroauto extends Fahrzeug {
        double batteriekapazitaet; // in kWh
        static final double EFFIZIENZ = 6.0; // km pro kWh

        public Elektroauto(String marke, String modell, String farbe, double batteriekapazitaet) {
            super(marke, modell, farbe);
            this.batteriekapazitaet = batteriekapazitaet;
        }

        @Override
        public String anzeigenInformationen() {
            return "Marke: " + marke + ", Modell: " + modell + ", Farbe: " + farbe + ", Batteriekapazität: "
                    + batteriekapazitaet + " kWh";
        }

        @Override
        public double berechneReichweite() {
            return batteriekapazitaet * EFFIZIENZ;
        }
    }

    public static void main(String[] args) {
        Uebung_6_7_Ue_01 uebung = new Uebung_6_7_Ue_01();
        Elektroauto elektroauto = uebung.new Elektroauto("Tesla", "Model 3", "Rot", 75);

        // Fahrzeuginformationen anzeigen
        System.out.println(elektroauto.anzeigenInformationen());

        // Reichweite berechnen und anzeigen
        System.out.println("Reichweite: " + elektroauto.berechneReichweite() + " km");
    }
}
