
/* 
Erstelle ein Java-Programm, das ein Array von Ganzzahlen (int-Werten) einliest und diese sortiert. 
Dabei soll das Programm robust gegenüber Fehleingaben sein und dem Benutzer die Möglichkeit geben, 
Eingabefehler zu korrigieren. Verwende dabei Verzweigungen, Schleifen und try-catch-Blöcke. Gehe wie folgt vor:

a) Deklariere ein Array, das bis zu 10 Ganzzahlen aufnehmen kann.

b) Implementiere eine Schleife, die die Zahlen vom Benutzer einliest. Verwende einen try-catch-Block, um sicherzustellen, dass nur Ganzzahlen akzeptiert werden. Bei einer Fehleingabe soll der Benutzer aufgefordert werden, die Eingabe zu wiederholen.

c) Nachdem alle Zahlen eingegeben wurden, sortiere das Array.

d) Gib das sortierte Array aus.
*/
import java.util.Scanner;
import java.util.Arrays;

public class Uebung_8_2_Ue_01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numbers = new int[10];
        int count = 0;

        while (count < 10) {
            System.out.print("Geben Sie eine Ganzzahl ein (" + (count + 1) + "/10): ");
            try {
                numbers[count] = Integer.parseInt(scanner.nextLine());
                count++;
            } catch (NumberFormatException e) {
                System.out.println("Ungültige Eingabe. Bitte geben Sie eine Ganzzahl ein.");
            }
        }

        Arrays.sort(numbers);
        System.out.println("Sortiertes Array: " + Arrays.toString(numbers));
        scanner.close();
    }
}
