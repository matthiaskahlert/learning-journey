import java.util.Scanner;

public class ifVerzweigung {
    public static void main(String[] args) {
        // Zahleneingabe durch den Benutzer
        Scanner scanner = new Scanner(System.in);
        System.out.print("Bitte geben Sie eine Zahl ein: ");
        int zahl = scanner.nextInt();
        // Überprüfung, ob die Zahl positiv, negativ oder null ist
        if (zahl > 0) {
            System.out.println("Die Zahl ist positiv.");
        } else if (zahl < 0) {
            System.out.println("Die Zahl ist negativ.");
        } else {
            System.out.println("Die Zahl ist null.");
        }
        scanner.close();
    }
}
