/* Erstelle eine Java-Klasse namens Buch, die als Attribute den Titel, den Autor, das Erscheinungsjahr und die ISBN-Nummer hat. 
Implementiere einen Konstruktor, der alle diese Attribute als Parameter erhält und sie entsprechend setzt. 
Zusätzlich soll die Klasse eine nicht-statische Methode beschreibungAnzeigen haben, die eine Zeichenkette zurückgibt, 
welche alle Attribute des Buches in einem sinnvollen Satz zusammenfasst. 
Erstelle dann in der main-Methode zwei verschiedene Buch-Objekte mit unterschiedlichen Attributen 
und rufe für jedes Objekt die Methode beschreibungAnzeigen auf, um die Informationen auf der Konsole auszugeben. */

public class Buch {
    String titel;
    String autor;
    int jahr;
    String isbn;

    // Konstruktor
    public Buch(String titel, String autor, int jahr, String isbn) {
        this.titel = titel;
        this.autor = autor;
        this.jahr = jahr;
        this.isbn = isbn;
    }

    // Methode zur Anzeige der buchbeschreibung
    public String beschreibungAnzeigen() {
        String beschreibung;
        beschreibung = "Das Buch '" + titel + "' wurde von " + autor + " im Jahr " + jahr + " veröffentlicht. ISBN: "
                + isbn;
        return beschreibung;
    }

    public static void main(String[] args) {
        Buch buch1 = new Buch("Der Herr der Ringe", "J.R.R. Tolkien", 1954, "978-0261102385");
        Buch buch2 = new Buch("Harry Potter und der Stein der Weisen", "J.K. Rowling", 1997, "978-0747532699");
        Buch buch3 = new Buch("Dune", "Frank Herbert", 1965, "978-0441013593");
        Buch buch4 = new Buch("Dune Messiah", "Frank Herbert", 1969, "978-0441172696");
        Buch buch5 = new Buch("Children of Dune", "Frank Herbert", 1976, "978-0441104024");
        Buch buch6 = new Buch("God Emperor of Dune", "Frank Herbert", 1981, "978-0441172696");
        Buch buch7 = new Buch("Heretics of Dune", "Frank Herbert", 1984, "978-0441104031");
        Buch buch8 = new Buch("Chapterhouse: Dune", "Frank Herbert", 1985, "978-0441104055");

        System.out.println(buch1.beschreibungAnzeigen());
        System.out.println(buch2.beschreibungAnzeigen());
        System.out.println(buch3.beschreibungAnzeigen());
        System.out.println(buch4.beschreibungAnzeigen());
        System.out.println(buch5.beschreibungAnzeigen());
        System.out.println(buch6.beschreibungAnzeigen());
        System.out.println(buch7.beschreibungAnzeigen());
        System.out.println(buch8.beschreibungAnzeigen());
    }
}
