/* 
Erstelle ein Java-Programm, das eine einfache Simulation eines Warenlagers durchführt. 
In diesem Lager sollen verschiedene Produkte mit ihrer jeweiligen Menge aufbewahrt werden. 
Das Programm soll folgende Funktionalitäten bieten:

a) Definiere eine Methode produktHinzufuegen, die ein Produkt und dessen Menge zu einem Array von Produkten hinzufügt. 
Falls das Produkt bereits existiert, soll die Menge aktualisiert werden.

b) Definiere eine Methode produktEntfernen, die ein Produkt aus dem Array entfernt. 
Falls das Produkt nicht gefunden wird, soll eine entsprechende Nachricht ausgegeben werden.

c) Definiere eine Methode lagerBestandAnzeigen, die den aktuellen Lagerbestand aller Produkte anzeigt.

d) Verwende Verzweigungen und Schleifen, um die Logik in den Methoden zu implementieren.

e) Das Array soll als ein Array von Objekten einer Klasse Produkt definiert werden, 
die zwei Attribute hat: name (String) und menge (int).

f) Das Hauptprogramm (main-Methode) soll das Array initialisieren und eine Benutzerschnittstelle in der Konsole bieten, 
in der Produkte hinzugefügt, entfernt und der Lagerbestand angezeigt werden kann. 
*/

public class Uebung_7_1_Ue_02 {
    class Produkt {
        String name;
        int menge;

        public Produkt(String name, int menge) {
            this.name = name;
            this.menge = menge;
        }
    }

    // Weitere Methoden wie produktHinzufuegen, produktEntfernen und lagerBestandAnzeigen
    // würden hier implementiert werden
    // a) Logik zum Hinzufügen eines Produkts zum Lager
    public void produktHinzufuegen(Produkt[] lager, String name, int menge) {
        for (int i = 0; i < lager.length; i++) {
            if (lager[i] != null && lager[i].name.equals(name)) {
                lager[i].menge += menge;
                System.out.println("Produktmenge aktualisiert: " + name);
                return;
            }
        }
        for (int i = 0; i < lager.length; i++) {
            if (lager[i] == null) {
                lager[i] = new Produkt(name, menge);
                System.out.println("Produkt hinzugefügt: " + name);
                return;
            }
        }
        System.out.println("Lager ist voll, Produkt konnte nicht hinzugefügt werden.");
    }
    // b) Logik zum Entfernen eines Produkts aus dem Lager
    public void produktEntfernen(Produkt[] lager, String name) {
        for (int i = 0; i < lager.length; i++) {
            if (lager[i] != null && lager[i].name.equals(name)) {
                lager[i] = null;
                System.out.println("Produkt entfernt: " + name);
                return;
            }
        }
        System.out.println("Produkt nicht gefunden: " + name);
    }
    // c) Logik zum Anzeigen des aktuellen Lagerbestands
    public void lagerBestandAnzeigen(Produkt[] lager) {
        System.out.println("Aktueller Lagerbestand:");
        for (Produkt produkt : lager) {
            if (produkt != null) {
                System.out.println("- " + produkt.name + ": " + produkt.menge);
            }
        }
    }

    public static void main(String[] args) {
        Uebung_7_1_Ue_02 uebung = new Uebung_7_1_Ue_02();
        Produkt[] lager = new Produkt[10]; // Lager mit Platz für 10 Produkte

        java.util.Scanner scanner = new java.util.Scanner(System.in);
        while (true) {
            System.out.println("\nWählen Sie eine Aktion:");
            System.out.println("1: Produkt hinzufügen");
            System.out.println("2: Produkt entfernen");
            System.out.println("3: Lagerbestand anzeigen");
            System.out.println("4: Beenden");
            int auswahl = scanner.nextInt();
            scanner.nextLine(); // Zeilenumbruch einlesen

            switch (auswahl) {
                case 1:
                    System.out.print("Produktname: ");
                    String name = scanner.nextLine();
                    System.out.print("Menge: ");
                    int menge = scanner.nextInt();
                    scanner.nextLine(); // Zeilenumbruch einlesen
                    uebung.produktHinzufuegen(lager, name, menge);
                    break;
                case 2:
                    System.out.print("Produktname: ");
                    name = scanner.nextLine();
                    uebung.produktEntfernen(lager, name);
                    break;
                case 3:
                    uebung.lagerBestandAnzeigen(lager);
                    break;
                case 4:
                    System.out.println("Programm beendet.");
                    scanner.close();
                    return;
                default:
                    System.out.println("Ungültige Auswahl, bitte erneut versuchen.");
            }
        }
    }
}
