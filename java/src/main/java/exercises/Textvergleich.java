import java.util.Scanner;

public class Textvergleich {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String geheimesPasswort = "ultrageheimesPasswort";
        System.out.print("Bitte Passwort eingeben: ");
        String passwort = scanner.next();
        // equals() Methode vergleicht den Inhalt von Strings, während == den Speicherort vergleicht
        if (passwort.equals(geheimesPasswort)) {
            System.out.println("Passwort korrekt");
        } else {
            System.out.println("Passwort falsch");
        }
        scanner.close();
    }
}
