import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

/* 
Erstelle eine Java-Methode namens filterEvenNumbers, die eine Liste von Integer-Werten entgegennimmt 
und eine neue Liste zurückgibt, die nur die geraden Zahlen enthält. 
Verwende dabei Schleifen zur Iteration über die Liste und Verzweigungen zur Überprüfung, 
ob eine Zahl gerade ist. Stelle sicher, dass du die Methode in einer Klasse namens NumberUtils implementierst und teste deine Methode mit einer Liste von Zahlen, die du in der main-Methode definierst.

a) Implementiere die Methode filterEvenNumbers.

b) In der main-Methode, erstelle eine Liste von Integer-Werten und füge einige Zahlen hinzu.

c) Rufe die Methode filterEvenNumbers mit der erstellten Liste auf 
und speichere das Ergebnis in einer neuen Liste.

d) Gib die neue Liste mit den geraden Zahlen auf der Konsole aus.
*/
public class Uebung_7_2_Ue_01 {
    public static void main(String[] args) {
        // b) Erstellen einer Liste von Integer-Werten
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // c) Aufrufen der Methode filterEvenNumbers
        List<Integer> evenNumbers = filterEvenNumbers(numbers);

        // d) Ausgabe der geraden Zahlen auf der Konsole
        System.out.println("Gerade Zahlen: " + evenNumbers);
    }

    public static List<Integer> filterEvenNumbers(List<Integer> numbers) {
        List<Integer> evenNumbers = new ArrayList<>();
        for (Integer number : numbers) {
            if (number % 2 == 0) {
                evenNumbers.add(number);
            }
        }
        return evenNumbers;
    }
}
