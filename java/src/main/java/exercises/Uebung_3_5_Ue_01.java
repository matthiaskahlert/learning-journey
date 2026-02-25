import java.util.Scanner;

public class Uebung_3_5_Ue_01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Bitte geben Sie eine Zahl ein: ");
        int zahl_1 = scanner.nextInt();
        System.out.print("Bitte geben Sie eine weitere Zahl ein: ");
        int zahl_2 = scanner.nextInt();
        int summe = zahl_1 + zahl_2;
        int differenz = zahl_1 - zahl_2;
        int produkt = zahl_1 * zahl_2;
        
        System.out.println("Sie haben die Zahl " + zahl_1 + " und die Zahl " + zahl_2 + " eingegeben.");
        System.out.println("Die Summe der beiden Zahlen ist: " + summe);
        System.out.println("Die Differenz der beiden Zahlen ist: " + differenz);
        System.out.println("Das Produkt der beiden Zahlen ist " + produkt);
        
        if (zahl_2 == 0) {
            System.out.println("Fehler: Division durch Null ist nicht erlaubt!");
        } else {
            float quotient = zahl_1 / (float) zahl_2;
            System.out.println("Der Quotient der beiden Zahlen ist " + quotient);
        }
        scanner.close();
    }

}
