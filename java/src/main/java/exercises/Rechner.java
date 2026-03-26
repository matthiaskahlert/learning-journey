import java.util.Scanner;

public class Rechner {
    public static void main(String[] args) {
        System.out.println("Rechner startet...");
        // nun den scanner starten um tastatureingaben abzufangen
        Scanner scanner = new Scanner(System.in);
        // den user begrüßen und fragen welche rechenoperation er durchführen möchte
        System.out.println("Willkommen zum Java-Rechner!");

        while (true) {
            System.out.println("Welche mathematische Operation möchten Sie durchführen?\n" +
                    "Addition (A)\n" +
                    "Subtraktion (S)\n" +
                    "Multiplikation (M)\n" +
                    "Division (D)");
            System.out.print("Deine Antwort (A, S, M, D): ");
            String berechnung = scanner.nextLine().toUpperCase();

            switch (berechnung) {
                case "A":
                    System.out.println("Addition!");
                    // es wird eine variable namens addNumbers deklariert, als array von
                    // glitkommazahlen.
                    // dann wird die methode getTwoNumners aufgeruen und scanner wird als argument
                    // für die methoe übergeben, um nutzereingaben zu lesen.
                    double[] addNumbers = getTwoNumbers(scanner);
                    System.out.println("Ergebnis lautet: " + add(addNumbers[0], addNumbers[1]));
                    break;
                case "S":
                    System.out.println("Subtraktion!");
                    double[] subNumbers = getTwoNumbers(scanner);
                    System.out.println("Ergebnis lautet: " + subtract(subNumbers[0], subNumbers[1]));
                    break;
                case "M":
                    System.out.println("Multiplikation!");
                    double[] mulNumbers = getTwoNumbers(scanner);
                    System.out.println("Ergebnis lautet: " + multiply(mulNumbers[0], mulNumbers[1]));
                    break;
                case "D":
                    System.out.println("Division!");
                    double[] divNumbers = getTwoNumbers(scanner);
                    if (divNumbers[1] == 0) {
                        System.out.println("Teilen durch null ist nicht erlaubt.");
                    } else {
                        System.out.println("Ergebnis lautet: " + divide(divNumbers[0], divNumbers[1]));
                    }
                    break;
                default:
                    System.out.println(
                            "Ungültiger Operator. Bitte einen der folgenden Operatoren eingeben: (A, S, M, D)");
                    continue;
            }

            System.out.print("Möchten Sie das Programm beenden? (ja/nein): ");
            String beenden = scanner.nextLine().toLowerCase();
            if (beenden.equals("ja")) {
                System.out.println("Auf Wiedersehen!");
                break;
            } else if (!beenden.equals("nein")) {
                System.out.println("Ungültige Eingabe. Das Programm wird beendet.");
                break;
            }
        }

        scanner.close();
    }

    public static double[] getTwoNumbers(Scanner scanner) {
        System.out.print("Bitte die erste Zahl eingeben: ");
        double zahl1 = Double.parseDouble(scanner.nextLine());
        System.out.print("Bitte die zweite Zahl eingeben: ");
        double zahl2 = Double.parseDouble(scanner.nextLine());
        return new double[] { zahl1, zahl2 };
    }

    public static double add(double a, double b) {
        return a + b;
    }

    public static double subtract(double a, double b) {
        return a - b;
    }

    public static double multiply(double a, double b) {
        return a * b;
    }

    public static double divide(double a, double b) {
        return a / b;
    }
}
