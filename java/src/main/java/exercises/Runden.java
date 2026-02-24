import java.lang.Math;

public class Runden {
    public static void main(String[] args) {
        double zahl = 3.14159;
        double gerundet = Math.round(zahl * 100.0) / 100.0; // Runden auf 2 Dezimalstellen
        System.out.println("Die gerundete Zahl ist: " + gerundet);
    }
}
