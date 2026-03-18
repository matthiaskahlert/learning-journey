package personenverwaltung;

import java.util.Scanner;

public class MitarbeiterverwaltungKonsole {

    private static Mitarbeiter[] mitarbeiterArray = new Mitarbeiter[50];
    private static int count = 0;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean beenden = false;

        while (!beenden) {
            System.out.println("\nMitarbeiterverwaltung");
            System.out.println("1 - Mitarbeiter hinzufügen");
            System.out.println("2 - Alle Mitarbeiter anzeigen");
            System.out.println("3 - Mitarbeiter suchen");
            System.out.println("4 - Programm beenden");
            System.out.print("Auswahl: ");

            int auswahl;
            try {
                auswahl = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Ungültige Eingabe. Bitte eine Zahl eingeben.");
                continue;
            }

            switch (auswahl) {
                case 1 -> hinzufuegen(scanner);
                case 2 -> alleAnzeigen();
                case 3 -> suchen(scanner);
                case 4 -> {
                    System.out.println("Programm beendet.");
                    beenden = true;
                }
                default -> System.out.println("Ungültige Auswahl. Bitte erneut versuchen.");
            }
        }

        scanner.close();
    }

    private static void hinzufuegen(Scanner scanner) {
        if (count >= mitarbeiterArray.length) {
            System.out.println("Das Array ist voll. Kein weiterer Mitarbeiter kann hinzugefügt werden.");
            return;
        }

        System.out.print("Vorname: ");
        String vorname = scanner.nextLine();

        System.out.print("Nachname: ");
        String nachname = scanner.nextLine();

        System.out.print("Adresse: ");
        String adresse = scanner.nextLine();

        System.out.print("Gehalt: ");
        double gehalt;
        try {
            gehalt = Double.parseDouble(scanner.nextLine());
        } catch (NumberFormatException e) {
            System.out.println("Ungültige Eingabe für Gehalt. Abbruch.");
            return;
        }

        System.out.print("Abteilung: ");
        String abteilung = scanner.nextLine();

        mitarbeiterArray[count++] = new Mitarbeiter(vorname, nachname, adresse, gehalt, abteilung);
        System.out.println("Mitarbeiter erfolgreich hinzugefügt.");
    }

    private static void alleAnzeigen() {
        if (count == 0) {
            System.out.println("Keine Mitarbeiter vorhanden.");
            return;
        }

        System.out.println("\nListe aller Mitarbeiter:");
        for (int i = 0; i < count; i++) {
            System.out.println((i + 1) + ". " + mitarbeiterArray[i]);
        }
    }

    private static void suchen(Scanner scanner) {
        System.out.print("Vorname: ");
        String vorname = scanner.nextLine();

        System.out.print("Nachname: ");
        String nachname = scanner.nextLine();

        for (int i = 0; i < count; i++) {
            Mitarbeiter m = mitarbeiterArray[i];
            if (m.getVorname().equalsIgnoreCase(vorname) && m.getNachname().equalsIgnoreCase(nachname)) {
                System.out.println("Mitarbeiter gefunden: " + m);
                return;
            }
        }

        System.out.println("Mitarbeiter nicht gefunden.");
    }

    // ---------------- Klassen ----------------

    static class Person {
        private String vorname;
        private String nachname;
        private String adresse;

        public Person(String vorname, String nachname, String adresse) {
            this.vorname = vorname;
            this.nachname = nachname;
            this.adresse = adresse;
        }

        public String getVorname() { return vorname; }
        public String getNachname() { return nachname; }
        public String getAdresse() { return adresse; }

        @Override
        public String toString() {
            return vorname + " " + nachname + ", Adresse: " + adresse;
        }
    }

    static class Mitarbeiter extends Person {
        private double gehalt;
        private String abteilung;

        public Mitarbeiter(String vorname, String nachname, String adresse, double gehalt, String abteilung) {
            super(vorname, nachname, adresse);
            this.gehalt = gehalt;
            this.abteilung = abteilung;
        }

        public double getGehalt() { return gehalt; }
        public String getAbteilung() { return abteilung; }

        @Override
        public String toString() {
            return super.toString() + ", Gehalt: " + gehalt + ", Abteilung: " + abteilung;
        }
    }
}