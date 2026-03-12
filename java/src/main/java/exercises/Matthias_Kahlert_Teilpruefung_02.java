/* 
Entwickle ein Java-Programm, das ein einfaches Modell einer Unternehmenshierarchie repräsentiert. 
Das Programm soll folgende Anforderungen erfüllen:

a) Erstelle eine abstrakte Klasse Mitarbeiter, die als Oberklasse für verschiedene Arten von Mitarbeitern dient. 
Diese Klasse soll die Attribute vorname, nachname und abteilung (als String) sowie jahresgehalt (als double) enthalten. 
Implementiere einen Konstruktor, der alle diese Attribute initialisiert. 
Zusätzlich soll die Klasse eine abstrakte Methode arbeitsBeschreibung() enthalten, 
die in den Unterklassen implementiert werden muss und eine Beschreibung der Arbeit des Mitarbeiters zurückgibt.

b) Erstelle eine konkrete Klasse Manager, die von Mitarbeiter erbt und das zusätzliche Attribut bonus (als double) hat. 
Der Konstruktor von Manager soll alle Attribute inklusive bonus initialisieren. 
Überschreibe die Methode arbeitsBeschreibung(), sodass sie eine passende Beschreibung für einen Manager zurückgibt.

c) Erstelle eine konkrete Klasse Entwickler, die von Mitarbeiter erbt.
Die Klasse Entwickler soll keine zusätzlichen Attribute haben. 
Implementiere den Konstruktor und die Methode arbeitsBeschreibung(), 
die eine Beschreibung der Tätigkeiten eines Entwicklers zurückgibt.

d) Implementiere in der Klasse Manager eine nicht-statische Methode erhöheBonus(double betrag), 
die den Bonus des Managers um den übergebenen Betrag erhöht.

e) Erstelle in einer main-Methode zwei Instanzen von Manager und zwei Instanzen von Entwickler. 
Verwende Schleifen und Verzweigungen, um eine Liste aller Mitarbeiter auszugeben, wobei für Manager der Bonus separat aufgeführt werden soll.

f) Implementiere eine statische Methode gesamtKosten, die eine Liste von Mitarbeiter-Objekten entgegennimmt und die gesamten Kosten für das Unternehmen berechnet (Summe der Jahresgehälter aller Mitarbeiter plus die Boni der Manager). 
*/

import java.util.ArrayList;
import java.util.List;

public class Matthias_Kahlert_Teilpruefung_02 {
    // a) Abstrakte Klasse für alle Mitarbeiter. Muss von den Unterklassen
    // überschrieben werden.
    static abstract class Mitarbeiter {
        String vorname;
        String nachname;
        String abteilung;
        double jahresgehalt;

        public Mitarbeiter(String vorname, String nachname, String abteilung, double jahresgehalt) {
            this.vorname = vorname;
            this.nachname = nachname;
            this.abteilung = abteilung;
            this.jahresgehalt = jahresgehalt;
        }

        public String ganzerName() {
            return vorname + " " + nachname;
        }

        public abstract String arbeitsBeschreibung();
    }

    // b) Manager erbt von Mitarbeiter und hat zusätzlich einen Bonus
    static class Manager extends Mitarbeiter {
        double bonus;

        public Manager(String vorname, String nachname, String abteilung, double jahresgehalt, double bonus) {
            super(vorname, nachname, abteilung, jahresgehalt);
            this.bonus = bonus;
        }

        @Override
        public String arbeitsBeschreibung() {
            return "Koordiniert die Entwicklung, plant Releases, stimmt sich mit Design, Art und Programming ab und trägt Verantwortung für den Projekterfolg.";
        }

        // d) Bonus wird um den übergebenen Betrag erhöht
        public void erhoeheBonus(double betrag) {
            bonus += betrag;
        }

        // Gleiche Methode mit Umlaut passend zur Aufgabenstellung
        public void erhöheBonus(double betrag) {
            erhoeheBonus(betrag);
        }
    }

    // c) Entwickler erbt von Mitarbeiter und hat keine zusätzlichen Attribute
    static class Entwickler extends Mitarbeiter {
        public Entwickler(String vorname, String nachname, String abteilung, double jahresgehalt) {
            super(vorname, nachname, abteilung, jahresgehalt);
        }

        @Override
        public String arbeitsBeschreibung() {
            return "Entwickelt Gameplay- und Engine-Code, analysiert Fehler, optimiert Systeme und arbeitet eng mit Design und Art zusammen.";
        }
    }

    // f) Berechnet die Lohnkosten des Unternehmens
    public static double gesamtKosten(List<Mitarbeiter> mitarbeiterListe) { // static, damit ich sie in main aufrufen
                                                                            // kann, ohne eine Instanz der Klasse zu
                                                                            // erstellen
        double gesamtKosten = 0;

        for (Mitarbeiter mitarbeiter : mitarbeiterListe) {
            gesamtKosten += mitarbeiter.jahresgehalt;

            if (mitarbeiter instanceof Manager) { // mit instanceof kann ich sicherstellen, dass ich auf bonus zugreifen
                                                  // kann, da nur Manager diesen haben
                Manager manager = (Manager) mitarbeiter;
                gesamtKosten += manager.bonus;
            }
        }
        return gesamtKosten;
    }

    public static void main(String[] args) {
        List<Mitarbeiter> mitarbeiterListe = new ArrayList<>(); // die Liste speichert Manager und Mitarbeiter, da beide
                                                                // von Mitarbeiter erben

        // e) Zwei Manager und zwei Devs erstellen
        Manager manager1 = new Manager("Anna", "Schmidt", "Game Production", 92000, 12000);
        Manager manager2 = new Manager("Thomas", "Becker", "Technical Direction", 105000, 15000);
        Entwickler entwickler1 = new Entwickler("Alena", "Meyer", "Gameplay Programming", 72000);
        Entwickler entwickler2 = new Entwickler("David", "Fischer", "Engine Development", 78000);

        // Managerbonus erhöhen
        manager1.erhoeheBonus(1500);

        mitarbeiterListe.add(manager1);
        mitarbeiterListe.add(manager2);
        mitarbeiterListe.add(entwickler1);
        mitarbeiterListe.add(entwickler2);

        System.out.println("=== Mitarbeiterliste ===");

        for (Mitarbeiter mitarbeiter : mitarbeiterListe) {
            System.out.println("Name: " + mitarbeiter.ganzerName());
            System.out.println("Abteilung: " + mitarbeiter.abteilung);
            System.out.println("Jahresgehalt: " + mitarbeiter.jahresgehalt + " Euro");
            System.out.println("Tätigkeit: " + mitarbeiter.arbeitsBeschreibung());

            if (mitarbeiter instanceof Manager) {
                Manager manager = (Manager) mitarbeiter;
                System.out.println("Bonus: " + manager.bonus + " Euro");
            }

            System.out.println("------------------------------");
        }

        System.out.println("Gesamtkosten des Unternehmens: " + gesamtKosten(mitarbeiterListe) + " Euro");
    }
}
