import java.util.Scanner;

public class Passwortschutz {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String passwort = "";
        int i = 0;

        while (!passwort.equals("passwort") && i < 3) {
            System.out.println("Bitte Passwort eingeben:");
            passwort = scanner.next();
            i += 1;
        }

        if (passwort.equals("passwort")) {
            System.out.println("Passwort korrekt");
        } else {
            System.out.println("Zu viele Fehlversuche");
        }
        scanner.close();
    }
}
