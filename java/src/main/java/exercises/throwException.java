import java.util.Scanner;

public class throwException {
    public static float nettoBerechnen(float bruttopreis, int mwStSatz) throws Exception {
        if (mwStSatz != 19 && mwStSatz != 7) {
            throw new Exception("Ungültiger Mehrwertsteuersatz: " + mwStSatz + ". Nur 7 oder 19 zulässig.");
        }
        return bruttopreis - (bruttopreis * mwStSatz / 100.0f);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean erneuteEingabe = true;

        System.out.println("Bitte geben Sie den Bruttopreis ein:");
        float brutto = Float.valueOf(scanner.next());

        while (erneuteEingabe) {
            System.out.println("Bitte geben Sie den Mehrwertsteuersatz ein (7 oder 19):");
            int mwStSatz = Integer.valueOf(scanner.next());

            try {
                System.out.println("Der Nettopreis beträgt: " + nettoBerechnen(brutto, mwStSatz));
                erneuteEingabe = false; // Eingabe war erfolgreich, Schleife verlassen
            } catch (Exception e) {
                System.out.println(e.getMessage());
                System.out.println("Bitte versuchen Sie es erneut.");
            }
        }

        scanner.close();
    }
    /*
     * Ein wichtiges Detail, das nicht übersehen werden darf:
     * Damit ein so geworfener Fehler innerhalb der Funktion unbehandelt bleiben
     * kann,
     * also nicht direkt mit einem try-catch-Block umgeben werden muss,
     * muss dem Kopf der Funktion explizit die Information hinzugefügt werden,
     * dass diese Funktion einen Fehler werfen kann.
     * 
     * Dies geschieht mit dem Zusatz throws Exception.
     * Fehlt dieser Zusatz, so lässt sich das Programm nicht kompilieren.
     * 
     */
}
