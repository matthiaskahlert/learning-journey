/* 
Entwickle eine Java-Klasse Tier, die als Oberklasse für verschiedene Tierarten dienen soll. Die Klasse soll folgende Eigenschaften und Methoden haben:

a) Erstelle Attribute für den Namen des Tiers (name), sein Alter (alter) und eine statische Variable anzahlTiere, die die Anzahl der erstellten Tier-Instanzen zählt. Alle Attribute sollen private sein.

b) Implementiere einen Konstruktor, der den Namen und das Alter des Tiers setzt und die anzahlTiere um eins erhöht.

c) Erstelle eine nicht-statische Methode lautGeben(), die einen charakteristischen Laut des Tiers als String zurückgibt. Da diese Methode für die allgemeine Klasse Tier nicht spezifisch implementiert werden kann, soll sie abstrakt sein.

d) Füge eine statische Methode getAnzahlTiere() hinzu, die die Anzahl der erstellten Tier-Instanzen zurückgibt.

e) Schreibe eine Unterklasse Katze, die von Tier erbt und die Methode lautGeben() überschreibt, sodass sie den String "Miau" zurückgibt.

f) In der main-Methode deiner Klasse erstelle zwei Instanzen von Katze und rufe für beide die Methode lautGeben() auf. Gib dann die Gesamtanzahl der erstellten Tiere aus. 
*/

public class transfer_6_5_A_01 {
    public abstract class Tier {
        private String name;
        private int alter;
        private static int anzahlTiere = 0;

        public Tier(String name, int alter) {
            this.name = name;
            this.alter = alter;
            anzahlTiere++;
        }

        public abstract String lautGeben();

        public String getName() {
            return name;
        }

        public int getAlter() {
            return alter;
        }

        public static int getAnzahlTiere() {
            return anzahlTiere;
        }
    }

    public class Katze extends Tier {
        public Katze(String name, int alter) {
            super(name, alter);
        }

        @Override
        public String lautGeben() {
            return "Miau";
        }
    }

    public static class Main {
        public static void main(String[] args) {
            transfer_6_5_A_01 outer = new transfer_6_5_A_01();
            Katze katze1 = outer.new Katze("Whiskers", 3);
            Katze katze2 = outer.new Katze("Felix", 5);

            System.out.println(katze1.getName() + " (" + katze1.getAlter() + ") sagt: " + katze1.lautGeben());
            System.out.println(katze2.getName() + " (" + katze2.getAlter() + ") sagt: " + katze2.lautGeben());
            System.out.println("Anzahl der Tiere: " + Tier.getAnzahlTiere());
        }
    }
}
