
/* 
Entwickle ein Java-Programm, das folgende Funktionalitäten implementiert:

a) Definiere eine Klasse Person mit den Attributen name und alter. 
Implementiere einen Konstruktor, der diese Werte initialisiert, sowie eine Methode toString(), 
die die Personendaten als String zurückgibt.

b) Erstelle eine Klasse PersonenVerwaltung, die ein Array von Person-Objekten verwaltet. 
Implementiere Methoden zum Hinzufügen, Löschen und Anzeigen von Personen. Beachte dabei, 
dass das Array dynamisch sein soll und sich vergrößern oder verkleinern kann.

c) In der Klasse PersonenVerwaltung, implementiere eine Methode speicherePersonen(), 
die alle Personen aus dem Array in einer Textdatei personen.txt speichert. 
Verwende dazu einen BufferedWriter. Implementiere zusätzlich eine Methode ladePersonen(), 
die die Personen aus der Datei personen.txt liest und sie in das Array lädt. 
Verwende dazu einen Scanner.

d) Füge eine Fehlerbehandlung hinzu, die IOExceptions abfängt und eine aussagekräftige Fehlermeldung ausgibt. 
Verwende try-catch-Blöcke und wirf mit throw new Error("Fehlermeldung") einen Fehler, 
wenn beim Laden der Datei etwas schiefgeht. Stelle sicher, 
dass in jedem Fall die verwendeten Ressourcen im finally-Block geschlossen werden.

e) Implementiere eine einfache Benutzeroberfläche in der main-Methode, die es ermöglicht, 
Personen hinzuzufügen, zu löschen, anzuzeigen und die Speicher- und Ladeoperationen auszuführen. 
Verwende Verzweigungen, um auf Benutzereingaben zu reagieren, und Schleifen, um das Menü wiederholt anzuzeigen.
*/
import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

// a) Klasse Person
class Person {
    private final String name;
    private final int alter;

    public Person(String name, int alter) {
        this.name = name;
        this.alter = alter;
    }

    public String getName() {
        return name;
    }

    public int getAlter() {
        return alter;
    }

    @Override
    public String toString() {
        return name + " (" + alter + " Jahre)";
    }
}

// b) Klasse PersonenVerwaltung
class PersonenVerwaltung {
    private static final int START_KAPAZITAET = 10;
    private static final String DATEINAME = "personen.txt";

    private Person[] personen;
    private int anzahl;

    public PersonenVerwaltung() {
        this.personen = new Person[START_KAPAZITAET];
        this.anzahl = 0;
    }

    public void addPerson(String name, int alter) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Name darf nicht leer sein.");
        }
        if (alter < 0) {
            throw new IllegalArgumentException("Alter darf nicht negativ sein.");
        }

        ensureCapacityForAdd();
        personen[anzahl] = new Person(name, alter);
        anzahl++;
    }

    public boolean deletePerson(int index) {
        if (index < 0 || index >= anzahl) {
            return false;
        }

        for (int i = index; i < anzahl - 1; i++) {
            personen[i] = personen[i + 1];
        }
        personen[anzahl - 1] = null;
        anzahl--;
        shrinkIfNeeded();
        return true;
    }

    public Person[] getAllePersonen() {
        return Arrays.copyOf(personen, anzahl);
    }

    public void speicherePersonen() throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(DATEINAME))) {
            for (Person person : getAllePersonen()) {
                writer.write(person.getName() + ";" + person.getAlter());
                writer.newLine();
            }
        }
    }

    public void ladePersonen() {
        try (Scanner scanner = new Scanner(new File(DATEINAME))) {
            clear();
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                if (line.trim().isEmpty()) {
                    continue;
                }
                String[] parts = line.split(";", 2);
                if (parts.length != 2) {
                    throw new IllegalStateException("Ungültiges Dateiformat in " + DATEINAME + ": " + line);
                }

                String name = parts[0].trim();
                int alter = Integer.parseInt(parts[1].trim());
                addPerson(name, alter);
            }
        } catch (IOException e) {
            throw new IllegalStateException("Fehler beim Laden der Personen: " + e.getMessage(), e);
        } catch (NumberFormatException e) {
            throw new IllegalStateException("Ungültiges Alter in Datei: " + e.getMessage(), e);
        }
    }

    public int getAnzahl() {
        return anzahl;
    }

    private void clear() {
        personen = new Person[START_KAPAZITAET];
        anzahl = 0;
    }

    private void ensureCapacityForAdd() {
        if (anzahl >= personen.length) {
            personen = Arrays.copyOf(personen, personen.length * 2);
        }
    }

    private void shrinkIfNeeded() {
        int minKapazitaet = START_KAPAZITAET;
        if (personen.length > minKapazitaet && anzahl <= personen.length / 4) {
            int neueKapazitaet = Math.max(minKapazitaet, personen.length / 2);
            personen = Arrays.copyOf(personen, neueKapazitaet);
        }
    }
}

// e) Benutzeroberfläche
public class Uebung_9_2_A_01 {
    public static void main(String[] args) {
        PersonenVerwaltung verwaltung = new PersonenVerwaltung();

        try (Scanner input = new Scanner(System.in)) {
            boolean laufen = true;

            while (laufen) {
                printMenue();
                String wahl = input.nextLine().trim();

                switch (wahl) {
                    case "1":
                        System.out.print("Name: ");
                        String name = input.nextLine();
                        Integer alter = readInt(input, "Alter: ");
                        if (alter != null) {
                            try {
                                verwaltung.addPerson(name, alter);
                                System.out.println("Person hinzugefügt.");
                            } catch (IllegalArgumentException e) {
                                System.out.println("Fehler: " + e.getMessage());
                            }
                        }
                        break;

                    case "2":
                        printAllePersonen(verwaltung);
                        if (verwaltung.getAnzahl() > 0) {
                            Integer index = readInt(input, "Index der Person zum Löschen: ");
                            if (index != null) {
                                boolean geloescht = verwaltung.deletePerson(index - 1);
                                System.out.println(geloescht ? "Person gelöscht." : "Ungültiger Index.");
                            }
                        }
                        break;

                    case "3":
                        printAllePersonen(verwaltung);
                        break;

                    case "4":
                        try {
                            verwaltung.speicherePersonen();
                            System.out.println("Personen wurden gespeichert.");
                        } catch (IOException e) {
                            System.out.println("Fehler beim Speichern: " + e.getMessage());
                        }
                        break;

                    case "5":
                        try {
                            verwaltung.ladePersonen();
                            System.out.println("Personen wurden geladen.");
                        } catch (IllegalStateException e) {
                            System.out.println("Fehler beim Laden: " + e.getMessage());
                        }
                        break;

                    case "6":
                        System.out.println("Auf Wiedersehen!");
                        laufen = false;
                        break;

                    default:
                        System.out.println("Ungültige Option.");
                }
            }
        }
    }

    private static void printMenue() {
        System.out.println("\n=== Personenverwaltung ===");
        System.out.println("1. Person hinzufügen");
        System.out.println("2. Person löschen");
        System.out.println("3. Alle Personen anzeigen");
        System.out.println("4. Personen speichern");
        System.out.println("5. Personen laden");
        System.out.println("6. Beenden");
        System.out.print("Wählen Sie eine Option: ");
    }

    private static void printAllePersonen(PersonenVerwaltung verwaltung) {
        Person[] personen = verwaltung.getAllePersonen();
        if (personen.length == 0) {
            System.out.println("Keine Personen gespeichert.");
            return;
        }

        System.out.println("\n--- Personen ---");
        for (int i = 0; i < personen.length; i++) {
            System.out.println((i + 1) + ". " + personen[i]);
        }
    }

    private static Integer readInt(Scanner scanner, String prompt) {
        System.out.print(prompt);
        String line = scanner.nextLine().trim();
        try {
            return Integer.parseInt(line);
        } catch (NumberFormatException e) {
            System.out.println("Bitte eine gültige Ganzzahl eingeben.");
            return null;
        }
    }
}
