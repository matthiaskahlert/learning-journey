/* Entwickle eine Funktion berechneFakultaet, die die Fakultät einer übergebenen ganzen Zahl berechnet und als Rückgabewert liefert. 
Die Fakultät einer Zahl n ist das Produkt aller ganzen Zahlen von 1 bis n und wird als n! dargestellt. 
Für die Berechnung soll eine rekursive Methode verwendet werden, d.h. die Funktion soll sich selbst aufrufen. 
Implementiere die Funktion in Java und teste sie mit verschiedenen Werten. 

a) Schreibe den Code für die Funktion berechneFakultaet.

b) Erstelle einen Testfall in der main-Methode, um die Funktion mit dem Wert 5 zu testen und das Ergebnis auf der Konsole auszugeben.  */

import java.math.BigInteger;
import java.util.Scanner;

public class Uebung_5_4_Ue_01 {

    public static BigInteger berechneFakultaet(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Die Zahl darf nicht negativ sein!");
        } else if (n == 0) {
            return BigInteger.ONE; // Fakultät von 0 ist 1
        } else {
            // BigInteger ist eine Klasse, die große Zahlen unterstützt, da die Fakultät
            // schnell sehr groß werden kann
            // Daher muss man int umwandeln, damit BigInteger damit arbeiten kann. dies gilt
            // auch für das * Ergebnis der Multiplikation
            // Hier nutzt man methoden wie multiply, da BigInteger nicht mit normalen
            // Operatoren wie * arbeiten kann
            return BigInteger.valueOf(n).multiply(berechneFakultaet(n - 1));
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Bitte geben Sie eine Zahl ein, um dessen Fakultät zu berechnen: ");
        int testZahl = scanner.nextInt();
        // int testZahl = 666;
        BigInteger ergebnis = berechneFakultaet(testZahl);
        System.out.println("Die Fakultät von " + testZahl + " ist: " + ergebnis);
    }
}