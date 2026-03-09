/* 
Du sollst ein kleines Java-Programm schreiben, das eine Klasse Buch und eine Klasse Bibliothek beinhaltet. 
Die Klasse Buch soll Attribute für den Titel, den Autor und das Erscheinungsjahr haben. 
Alle Attribute sollen private sein, und es soll öffentliche Getter- und Setter-Methoden geben, 
um auf diese Attribute zuzugreifen. Zusätzlich soll es einen Konstruktor geben, 
der alle drei Attribute als Parameter erhält.
Die Klasse Bibliothek soll eine Methode hinzufuegen haben, die ein Buch-Objekt als Parameter erhält 
und dieses in einer internen Liste speichert. 
Da wir keine Listen verwenden dürfen, sollst du ein Array verwenden, 
um die Bücher zu speichern. 
Es soll auch eine Methode zeigeBuecher geben, die alle Bücher in der Bibliothek auf der Konsole ausgibt. 
Beachte, dass du für das Array eine feste Größe vorgeben musst und keine dynamische Liste verwenden darfst. 
Implementiere auch eine Fehlerbehandlung für den Fall, dass mehr Bücher hinzugefügt werden sollen, 
als das Array fassen kann.
a) Definiere die Klasse Buch mit den entsprechenden Attributen, Konstruktor, Getter- und Setter-Methoden.

b) Definiere die Klasse Bibliothek mit einem Array für Buch-Objekte, der Methode hinzufuegen und der Methode zeigeBuecher.

c) Schreibe eine main-Methode, in der du einige Buch-Objekte erstellst und sie der Bibliothek hinzufügst. Gib anschließend alle Bücher der Bibliothek aus. 
*/

public class transfer_6_4_A_01 {
    // Klasse Buch mit privaten Attributen
    class Buch {
        private String titel;
        private String autor;
        private int erscheinungsjahr;
        
        //Konstruktor
        public Buch(String titel, String autor, int erscheinungsjahr) {
            this.titel = titel;
            this.autor = autor;
            this.erscheinungsjahr = erscheinungsjahr;
        }
        // Getter- und Setter-Methoden
        public String getTitel() {
            return titel;
        }

        public void setTitel(String titel) {
            this.titel = titel;
        }

        public String getAutor() {
            return autor;
        }

        public void setAutor(String autor) {
            this.autor = autor;
        }

        public int getErscheinungsjahr() {
            return erscheinungsjahr;
        }

        public void setErscheinungsjahr(int erscheinungsjahr) {
            this.erscheinungsjahr = erscheinungsjahr;
        }
    }

    class Bibliothek {
        private Buch[] buecher;
        private int anzahlBuecher;

        // Konstruktor
        public Bibliothek(int kapazitaet) {
            buecher = new Buch[kapazitaet];
            anzahlBuecher = 0;
        }

        // Methode zum Hinzufügen eines Buches
        public void hinzufuegen(Buch buch) {
            if (anzahlBuecher < buecher.length) {
                buecher[anzahlBuecher] = buch;
                anzahlBuecher++;
            } else {
                System.out.println("Fehler: Die Bibliothek ist voll. Kein weiteres Buch kann hinzugefügt werden.");
            }
        }

        // Methode zum Anzeigen aller Bücher in der Bibliothek
        public void zeigeBuecher() {
            System.out.println("Bücher in der Bibliothek:");
            for (int i = 0; i < anzahlBuecher; i++) {
                System.out.println((i + 1) + ". " + buecher[i].getTitel() + " von " + buecher[i].getAutor() + " (" + buecher[i].getErscheinungsjahr() + ")");
            }
        }
    }

    public static void main(String[] args) {
        // Buch und Bibliothek gehören logisch zur äußeren Klasse, daher müssen wir eine Instanz der äußeren Klasse erstellen, um auf sie zuzugreifen
        transfer_6_4_A_01 programm = new transfer_6_4_A_01();
        Bibliothek bibliothek = programm.new Bibliothek(3); // Bibliothek mit Kapazität für 3 Bücher

        // Erstellen von Buch-Objekten
        Buch buch1 = programm.new Buch("Der Alchimist", "Paulo Coelho", 1988);
        Buch buch2 = programm.new Buch("Die Verwandlung", "Franz Kafka", 1915);
        Buch buch3 = programm.new Buch("Der Herr der Ringe", "J.R.R. Tolkien", 1954);
        Buch buch4 = programm.new Buch("Harry Potter und der Stein der Weisen", "J.K. Rowling", 1997);

        // Hinzufügen der Bücher zur Bibliothek
        bibliothek.hinzufuegen(buch1);
        bibliothek.hinzufuegen(buch2);
        bibliothek.hinzufuegen(buch3);
        bibliothek.hinzufuegen(buch4); // Dieser Versuch sollte eine Fehlermeldung ausgeben

        // Anzeigen aller Bücher in der Bibliothek
        bibliothek.zeigeBuecher();
    }
}
