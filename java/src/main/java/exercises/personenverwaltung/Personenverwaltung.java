package personenverwaltung;

import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Personenverwaltung {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Person> personen = new LinkedList<>();
        boolean erfassen = true;

        while (erfassen) {
            System.out.println("Neue Person erfassen");
            System.out.println("Bitte geben Sie den Vornamen der Person ein:");
            String vorname = scanner.next();

            System.out.println("Bitte geben Sie den Nachnamen der Person ein:");
            String nachname = scanner.next();

            System.out.println("Bitte geben Sie die Straße an, in der die Person wohnt:");
            String strasse = scanner.next();

            int hausnummer;
            while (true) {
                System.out.println("Bitte geben Sie die Hausnummer an, in der die Person wohnt:");
                try {
                    hausnummer = Integer.valueOf(scanner.next());
                    break;
                } catch (NumberFormatException exception) {
                    System.out.println("Ungültige Eingabe.Bitte geben Sie eine gültige Zahl ein.");
                    System.out.println("Technischer Fehler: " + exception.getMessage());
                }
            }

            System.out.println("Bitte geben Sie die PLZ an, an der die Person wohnt:");
            String plz = scanner.next();

            System.out.println("Bitte geben Sie den Ort ein, an der die Person wohnt:");
            String ort = scanner.next();

            System.out.println("Ist die Person ein Mitarbeiter? ja / nein");
            String mitarbeiter = scanner.next();

            if (mitarbeiter.equalsIgnoreCase("ja")) {
                System.out.println("Bitte geben Sie das Gehalt der Person ein:");
                int gehalt = Integer.valueOf(scanner.next());

                Mitarbeiter m = new Mitarbeiter(vorname, nachname, strasse, hausnummer, plz, ort, gehalt);
                personen.add(m);
            } else {
                Kunde k = new Kunde(vorname, nachname, strasse, hausnummer, plz, ort);
                personen.add(k);
            }

            System.out.println("Datenerfassung abgeschlossen. Möchten Sie fortfahren?");
            String fortfahren = scanner.next();

            if (fortfahren.equalsIgnoreCase("nein")) {
                erfassen = false;
            }
        }

        scanner.close();
    }
}
