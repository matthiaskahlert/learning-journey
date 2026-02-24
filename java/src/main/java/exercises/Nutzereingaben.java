import java.util.Scanner;

public class Nutzereingaben {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Bitte geben Sie eine Zahl ein: ");
        int zahl = scanner.nextInt();
        System.out.println("Sie haben die Zahl " + zahl + " eingegeben.");
        scanner.close();
    }
}
