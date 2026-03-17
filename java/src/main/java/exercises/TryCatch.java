import java.util.ArrayList;

public class TryCatch {
    // Methode zur Division zweier Zahlen
    public static int division(int zaehler, int nenner) {
        // Überprüfung, ob der Nenner 0 ist, da Division durch 0 nicht erlaubt ist
        if (nenner == 0) {
            throw new ArithmeticException("Division durch 0 ist nicht erlaubt.");
        }

        // Rückgabe des Ergebnisses der Division
        return zaehler / nenner;
    }

    public static void main(String[] args) {
        try {
            // Versuch, eine Division durchzuführen, die eine Ausnahme auslösen könnte
            int ergebnis = division(10, 0);
            System.out.println("Ergebnis: " + ergebnis);
        } catch (ArithmeticException e) {
            // Abfangen der Ausnahme und Ausgabe einer Fehlermeldung
            System.out.println("Fehler: " + e.getMessage());
        }

        // Erstellung einer leeren Liste
        ArrayList<Integer> liste = new ArrayList<>();
        try {
            // Versuch, auf das erste Element der Liste zuzugreifen
            liste.get(0);
        } catch (IndexOutOfBoundsException e) {
            // Abfangen der Ausnahme, wenn die Liste leer ist, und Ausgabe einer
            // Fehlermeldung
            System.out.println("Fehler: " + e.getMessage());
        }
    }
}
