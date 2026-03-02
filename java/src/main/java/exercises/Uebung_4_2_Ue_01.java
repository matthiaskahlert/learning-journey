/*
 * Aufgabe: Schleifentypen demonstrieren
 * 
 * Entwickle ein Java-Programm, das die Funktionsweise verschiedener Schleifentypen demonstriert.
 * Erstelle dazu eine Klasse SchleifenDemo mit einer main-Methode, in der du folgende Aufgaben bearbeitest:
 * 
 * a) Verwende eine while-Schleife, um die Zahlen von 1 bis 10 auf der Konsole auszugeben. 
 *    Achte darauf, dass du eine Zählvariable korrekt initialisierst und in jedem Durchlauf inkrementierst.
 * 
 * b) Implementiere eine do-while-Schleife, die mindestens einmal ausgeführt wird und eine Benutzereingabe
 *    über die Konsole erwartet. Die Schleife soll solange wiederholt werden, bis der Benutzer das Wort 
 *    "exit" eingibt. Verwende dafür ein Scanner-Objekt.
 * 
 * c) Erstelle eine for-Schleife, die rückwärts von 10 bis 1 zählt und dabei jede Zahl auf der Konsole 
 *    ausgibt. Verwende dabei die korrekte Syntax für die Initialisierung, Bedingung und das Update der 
 *    Zählvariable.
 */

import java.util.Scanner;

public class Uebung_4_2_Ue_01 {
    public static void main(String[] args) {
        // a) while-Schleife: Zahlen von 1 bis 10
        System.out.println("a) while-Schleife:");
        int i = 1;
        while (i < 11) {
            System.out.println(i);
            i += 1;
        }

        // b) do-while-Schleife: Benutzereingabe bis "exit"
        System.out.println("\nb) do-while-Schleife:");
        Scanner scanner = new Scanner(System.in);
        String eingabe;
        do {
            System.out.println("Geben Sie 'exit' ein!");
            eingabe = scanner.nextLine();

            if (!eingabe.equals("exit")) {
                System.out.println("Falsche Eingabe! Versuchen Sie es erneut.");
            }
        } while (!eingabe.equals("exit"));

        System.out.println("Eingabe korrekt!");

        // c) for-Schleife: Rückwärts von 10 bis 1
        System.out.println("\nc) for-Schleife:");
        for (int j = 10; j >= 1; j--) {
            System.out.println(j);
        }

        scanner.close();
    }
}