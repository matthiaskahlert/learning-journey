/* 
Aufgabe: OOP

Entwickle eine Java-Anwendung, die ein einfaches System zur Verwaltung von Bibliotheksbenutzern und deren Ausleihvorgängen darstellt. Folge diesen Schritten:

a) Definiere eine Klasse Buch, die die Eigenschaften titel, autor und isbn besitzt. 
Implementiere einen Konstruktor, der alle drei Eigenschaften initialisiert, 
sowie entsprechende Getter-Methoden für jede Eigenschaft.

b) Definiere eine Klasse Benutzer, die die Eigenschaften benutzerID, name 
und eine Liste von ausgeliehenen Büchern (List<Buch> ausgelieheneBuecher) besitzt. 
Der Konstruktor soll benutzerID und name initialisieren und die Liste leer initialisieren. 
Implementiere eine Methode bucheAusleihen(Buch buch), die ein Buch zur Liste der ausgeliehenen Bücher hinzufügt.

c) Erstelle eine statische Klasse Bibliotheksverwaltung mit einer 
statischen Methode bucheZurueckgeben(Benutzer benutzer, Buch buch), 
die ein Buch aus der Liste der ausgeliehenen Bücher eines Benutzers entfernt, wenn es vorhanden ist.

d) In der main-Methode deines Programms, erstelle mehrere Instanzen von Buch und Benutzer. 
Führe Ausleih- und Rückgabevorgänge durch, indem du die entsprechenden Methoden der Klassen verwendest.

e) Stelle sicher, dass deine Klassen und Methoden angemessene Zugriffsrechte haben, 
um die Prinzipien des Kapselns in der objektorientierten Programmierung zu demonstrieren.
*/

import java.util.*;

class BibliotheksBuch {
    private String titel;
    private String autor;
    private String isbn;

    public BibliotheksBuch(String titel, String autor, String isbn) {
        this.titel = titel;
        this.autor = autor;
        this.isbn = isbn;
    }

    public String getTitel() {
        return titel;
    }

    public String getAutor() {
        return autor;
    }

    public String getIsbn() {
        return isbn;
    }

    public String beschreibungAnzeigen() {
        return "'" + titel + "' von " + autor + " (ISBN: " + isbn + ")";
    }
}

class Benutzer {
    private int benutzerID;
    private String name;
    private List<BibliotheksBuch> ausgelieheneBuecher;

    public Benutzer(int benutzerID, String name) {
        this.benutzerID = benutzerID;
        this.name = name;
        this.ausgelieheneBuecher = new ArrayList<>();
    }

    public int getBenutzerID() {
        return benutzerID;
    }

    public String getName() {
        return name;
    }

    public List<BibliotheksBuch> getAusgelieheneBuecher() {
        return ausgelieheneBuecher;
    }

    public void bucheAusleihen(BibliotheksBuch buch) {
        ausgelieheneBuecher.add(buch);
        System.out.println(name + " hat das Buch " + buch.getTitel() + " ausgeliehen.");
    }
}

class Bibliotheksverwaltung {
    public static void bucheZurueckgeben(Benutzer benutzer, BibliotheksBuch buch) {
        if (benutzer.getAusgelieheneBuecher().remove(buch)) {
            System.out.println(benutzer.getName() + " hat das Buch " + buch.getTitel() + " zurückgegeben.");
        } else {
            System.out.println(benutzer.getName() + " hat das Buch " + buch.getTitel() + " nicht ausgeliehen.");
        }
    }
}

public class Uebung_6_7_A_01 {
    public static void main(String[] args) {
        // Bücher anlegen
        BibliotheksBuch buch1 = new BibliotheksBuch("Der Herr der Ringe", "J.R.R. Tolkien", "978-0261102385");
        BibliotheksBuch buch2 = new BibliotheksBuch("Harry Potter und der Stein der Weisen", "J.K. Rowling",
                "978-0747532699");
        BibliotheksBuch buch3 = new BibliotheksBuch("Dune", "Frank Herbert", "978-0441013593");

        // Benutzer anlegen
        Benutzer benutzer1 = new Benutzer(1, "Anna");
        Benutzer benutzer2 = new Benutzer(2, "Ben");

        // Ausleihen
        benutzer1.bucheAusleihen(buch1);
        benutzer1.bucheAusleihen(buch2);
        benutzer2.bucheAusleihen(buch3);

        // Rückgabe
        Bibliotheksverwaltung.bucheZurueckgeben(benutzer1, buch1);
        Bibliotheksverwaltung.bucheZurueckgeben(benutzer2, buch2); // nicht ausgeliehen

        // Übersicht
        System.out.println("\nAusgeliehene Bücher von " + benutzer1.getName() + ":");
        for (BibliotheksBuch b : benutzer1.getAusgelieheneBuecher()) {
            System.out.println(b.beschreibungAnzeigen());
        }
        System.out.println("\nAusgeliehene Bücher von " + benutzer2.getName() + ":");
        for (BibliotheksBuch b : benutzer2.getAusgelieheneBuecher()) {
            System.out.println(b.beschreibungAnzeigen());
        }
    }
}
