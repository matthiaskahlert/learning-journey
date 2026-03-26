/* 
Du arbeitest für ein Unternehmen, das eine Software für die Verwaltung von Kontakten entwickelt. 
Die Anwendung soll Kontakte in einer CSV-Datei speichern und aus dieser lesen können. 
Jeder Kontakt besteht aus einem Vornamen, einem Nachnamen, einer E-Mail-Adresse und einer Telefonnummer. 
Die CSV-Datei soll folgende Struktur haben: Vorname,Nachname,Email,Telefonnummer. 
Führe folgende Schritte aus:

a) Erstelle eine Klasse Kontakt mit den Attributen vorname, nachname, email und telefonnummer. 
Implementiere einen Konstruktor, der alle Attribute als Parameter erhält, 
sowie Getter- und Setter-Methoden für jedes Attribut.

b) Erstelle eine Klasse KontaktVerwaltung, die eine Liste von Kontakt-Objekten verwaltet. 
Implementiere Methoden zum Hinzufügen eines neuen Kontakts, 
zum Löschen eines Kontakts anhand des Namens und zum Anzeigen aller Kontakte.

c) Implementiere eine Methode speichereKontakteInCSV, die die Liste der Kontakte in eine CSV-Datei schreibt. 
Verwende dabei FileWriter und BufferedWriter.

d) Implementiere eine Methode ladeKontakteAusCSV, die Kontakte aus einer CSV-Datei liest 
und in die Liste der Kontakte lädt. Verwende dabei FileReader und BufferedReader.

e) Erstelle eine Hauptklasse mit einer main-Methode, in der du die KontaktVerwaltung-Klasse instanziierst, 
einige Kontakte hinzufügst, die Kontakte in eine CSV-Datei speicherst, 
die Anwendung beendest, neu startest, und die Kontakte aus der CSV-Datei lädst und anzeigst.
*/

import java.io.*;
import java.util.*;

class Kontakt {
    private String vorname;
    private String nachname;
    private String email;
    private String telefonnummer;

    public Kontakt(String vorname, String nachname, String email, String telefonnummer) {
        this.vorname = vorname;
        this.nachname = nachname;
        this.email = email;
        this.telefonnummer = telefonnummer;
    }

    public String getVorname() {
        return vorname;
    }

    public void setVorname(String vorname) {
        this.vorname = vorname;
    }

    public String getNachname() {
        return nachname;
    }

    public void setNachname(String nachname) {
        this.nachname = nachname;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getTelefonnummer() {
        return telefonnummer;
    }

    public void setTelefonnummer(String telefonnummer) {
        this.telefonnummer = telefonnummer;
    }

    @Override
    public String toString() {
        return vorname + ", " + nachname + ", " + email + ", " + telefonnummer;
    }
}

class KontaktVerwaltung {
    private List<Kontakt> kontakte = new ArrayList<>();

    public void kontaktHinzufuegen(Kontakt kontakt) {
        kontakte.add(kontakt);
    }

    public boolean kontaktLoeschen(String vorname, String nachname) {
        return kontakte
                .removeIf(k -> k.getVorname().equalsIgnoreCase(vorname) && k.getNachname().equalsIgnoreCase(nachname));
    }

    public void kontakteAnzeigen() {
        if (kontakte.isEmpty()) {
            System.out.println("Keine Kontakte vorhanden.");
        } else {
            for (Kontakt k : kontakte) {
                System.out.println(k);
            }
        }
    }

    public void speichereKontakteInCSV(String dateiname) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(dateiname))) {
            for (Kontakt k : kontakte) {
                writer.write(k.getVorname() + "," + k.getNachname() + "," + k.getEmail() + "," + k.getTelefonnummer());
                writer.newLine();
            }
            System.out.println("Kontakte gespeichert in " + dateiname);
        } catch (IOException e) {
            System.out.println("Fehler beim Speichern: " + e.getMessage());
        }
    }

    public void ladeKontakteAusCSV(String dateiname) {
        kontakte.clear();
        try (BufferedReader reader = new BufferedReader(new FileReader(dateiname))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                if (parts.length == 4) {
                    kontaktHinzufuegen(new Kontakt(parts[0], parts[1], parts[2], parts[3]));
                }
            }
            System.out.println("Kontakte geladen aus " + dateiname);
        } catch (IOException e) {
            System.out.println("Fehler beim Laden: " + e.getMessage());
        }
    }
}

public class Uebung_9_5_C_01 {
    public static void main(String[] args) {
        String dateiname = "kontakte.csv";

        // 1. Kontakte anlegen und speichern
        KontaktVerwaltung verwaltung = new KontaktVerwaltung();
        verwaltung.kontaktHinzufuegen(new Kontakt("Anna", "Muster", "anna@example.com", "0123456789"));
        verwaltung.kontaktHinzufuegen(new Kontakt("Ben", "Beispiel", "ben@example.com", "0987654321"));
        verwaltung.kontaktHinzufuegen(new Kontakt("Clara", "Test", "clara@example.com", "01711223344"));

        System.out.println("Alle Kontakte:");
        verwaltung.kontakteAnzeigen();

        verwaltung.speichereKontakteInCSV(dateiname);

        // 2. Anwendung "beenden" und neu starten (simuliert durch neue Instanz)
        System.out.println("\n--- Anwendung neu gestartet ---\n");
        KontaktVerwaltung neueVerwaltung = new KontaktVerwaltung();
        neueVerwaltung.ladeKontakteAusCSV(dateiname);
        neueVerwaltung.kontakteAnzeigen();
    }
}
