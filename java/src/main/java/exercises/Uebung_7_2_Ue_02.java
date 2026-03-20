import java.util.ArrayList;
import java.util.List;

/* 

Aufgabe: Listen
Erstelle ein Java-Programm, das folgende Anforderungen erfüllt:

a) Definiere eine Methode filterEvenNumbers, die als Parameter eine Liste von Integer-Werten entgegennimmt 
und eine neue Liste zurückgibt, die nur die geraden Zahlen enthält.

b) In der main-Methode deklariere zwei Listen von Integer-Werten, 
wobei die erste Liste Werte von 1 bis 20 in aufsteigender Reihenfolge enthält u
nd die zweite Liste zunächst leer ist.

c) Verwende die Methode filterEvenNumbers, um die geraden Zahlen aus der ersten Liste zu filtern 
und das Ergebnis in der zweiten Liste zu speichern.

d) Gib die zweite Liste mit den gefilterten Werten auf der Konsole aus.

e) Implementiere eine Schleife, die die Werte der zweiten Liste durchläuft 
und für jeden Wert prüft, ob dieser größer als 10 ist. Falls ja, 
soll der Wert verdoppelt und das Ergebnis ausgegeben werden.*/

public class Uebung_7_2_Ue_02 {

    // a) Methode filterEvenNumbers
    public static List<Integer> filterEvenNumbers(List<Integer> numbers) {
        List<Integer> evenNumbers = new ArrayList<>();
        for (int number : numbers) {
            if (number % 2 == 0) {
                evenNumbers.add(number);
            }
        }
        return evenNumbers;
    }

    public static void main(String[] args) {
        // b) Erste Liste mit Werten von 1 bis 20
        List<Integer> firstList = new ArrayList<>();
        for (int i = 1; i <= 20; i++) {
            firstList.add(i);
        }

        // b) Zweite Liste, zunächst leer
        List<Integer> secondList = new ArrayList<>();

        // c) Filtere gerade Zahlen und speichere sie in der zweiten Liste
        secondList = filterEvenNumbers(firstList);

        // d) Gib die zweite Liste aus
        System.out.println("Gefilterte gerade Zahlen: " + secondList);

        // e) Schleife, die Werte prüft und verdoppelt, wenn größer als 10
        for (int number : secondList) {
            if (number > 10) {
                int doubled = number * 2;
                System.out.println("Verdoppelt: " + doubled);
            }
        }
    }
}
