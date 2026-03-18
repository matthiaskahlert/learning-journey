package personenverwaltung;

import java.io.*;
import java.util.*;

public class CSVHandler {

    // Schreibt eine Liste von Personen in eine CSV-Datei
    public static void writeToCSV(List<Person> personen, String fileName) {
        try (FileWriter writer = new FileWriter(fileName)) {
            for (Person person : personen) {
                // Gemeinsame Felder: Vorname, Nachname, Adresse
                String zeile = person.vorname + ","
                        + person.nachname + ","
                        + person.adresse.strasse + ","
                        + person.adresse.getHausnummer() + ","
                        + person.adresse.plz + ","
                        + person.adresse.ort;

                // Typ-Identifikator + ggf. Gehalt
                if (person instanceof Mitarbeiter) {
                    Mitarbeiter m = (Mitarbeiter) person;
                    writer.write("Mitarbeiter," + zeile + "," + m.gehalt + "\n");
                } else {
                    writer.write("Kunde," + zeile + "\n");
                }
            }
            System.out.println("CSV-Datei wurde erfolgreich erstellt: " + fileName);
        } catch (IOException e) {
            System.out.println("Fehler beim Schreiben: " + e.getMessage());
        }
    }

    // Liest Personen aus einer CSV-Datei
    public static List<Person> readFromCSV(String fileName) {
        List<Person> personen = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] p = line.split(",");
                // p[0]=Typ, p[1]=Vorname, p[2]=Nachname, p[3]=Strasse, p[4]=Hausnr, p[5]=PLZ,
                // p[6]=Ort
                if (p[0].equals("Mitarbeiter")) {
                    // p[7]=Gehalt
                    personen.add(new Mitarbeiter(p[1], p[2], p[3], Integer.parseInt(p[4]), p[5], p[6],
                            Integer.parseInt(p[7])));
                } else if (p[0].equals("Kunde")) {
                    personen.add(new Kunde(p[1], p[2], p[3], Integer.parseInt(p[4]), p[5], p[6]));
                }
            }
            System.out.println("CSV-Datei wurde erfolgreich gelesen: " + fileName);
        } catch (IOException e) {
            System.out.println("Fehler beim Lesen: " + e.getMessage());
        }
        return personen;
    }

    public static void main(String[] args) {
        // Testdaten erstellen
        List<Person> personen = new ArrayList<>();
        personen.add(new Kunde("Max", "Mustermann", "Musterstrasse", 1, "12345", "Musterstadt"));
        personen.add(new Mitarbeiter("Anna", "Meier", "Arbeitsweg", 2, "54321", "Arbeitsstadt", 3000));

        // Define the file path to ensure the CSV is created in the personenverwaltung
        // folder
        String fileName = System.getProperty("user.dir")
                + "/java/src/main/java/exercises/personenverwaltung/personen.csv";

        // CSV schreiben
        writeToCSV(personen, fileName);

        // CSV lesen und ausgeben
        List<Person> gelesenePersonen = readFromCSV(fileName);
        for (Person person : gelesenePersonen) {
            if (person instanceof Mitarbeiter) {
                Mitarbeiter m = (Mitarbeiter) person;
                System.out.println("Mitarbeiter: " + m.ganzerName() + ", Gehalt: " + m.gehalt);
            } else {
                System.out.println("Kunde: " + person.ganzerName());
            }
        }
    }
}