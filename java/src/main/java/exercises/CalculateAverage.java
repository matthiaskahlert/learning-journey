/* 
Entwickle eine Java-Methode calculateAverage, die als Parameter ein Array von Ganzzahlen entgegennimmt 
und das arithmetische Mittel dieser Zahlen berechnet und zurückgibt. 
Berücksichtige dabei, dass das Array auch leer sein könnte. 
Verwende eine Schleife, um die Summe der Zahlen im Array zu berechnen. 
Implementiere zusätzlich eine Verzweigung, die überprüft, ob das Array leer ist, 
und in diesem Fall eine entsprechende Meldung ausgibt und -1 zurückgibt, um anzuzeigen, 
dass kein Durchschnitt berechnet werden konnte. Teste deine Methode mit einem Array, 
das die Ganzzahlen von 1 bis 10 enthält, und gib das Ergebnis auf der Konsole aus. 
*/

public class CalculateAverage {
    public static float calculateAverage(int[] zahlen) {
        System.out.println("Berechnung des Durchschnitts...");
        if (zahlen.length == 0) {
            System.out.println(" Das Array ist leer. Kann keinen Durchschnitt berechnen.");
            return -1;
        } else {
            float summe = 0;
            int anzahl = zahlen.length;
            for (int i = 0; i < anzahl; i++) {
                summe += zahlen[i];
            }
            float durchschnitt = summe / anzahl;

            System.out.println("Der Durchschnitt beträgt: " + durchschnitt);
            return durchschnitt;
        }

    }

    public static void main(String[] args) {
        // Test-Array mit den Zahlen 1 bis 10
        int[] zahlen = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        // Berechnung des Durchschnitts
        float ergebnis = calculateAverage(zahlen);

        // Ausgabe des Ergebnisses
        System.out.println("Das berechnete arithmetische Mittel ist: " + ergebnis);
    }
}