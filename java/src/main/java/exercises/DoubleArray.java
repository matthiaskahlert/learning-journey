import java.util.ArrayList;

public class DoubleArray {

    /*
     * a) Deklariere ein Array von double-Werten mit mindestens 5 verschiedenen
     * Dezimalzahlen.
     * b) Konvertiere dieses Array in eine ArrayList<Double>.
     * c) Verwende eine Schleife, um die ArrayList<Double> zu durchlaufen
     * und alle Werte zu verdoppeln.
     * d) Gib die ArrayList<Double> sowohl vor als auch nach der Verarbeitung auf
     * der Konsole aus.
     */
    public static void main(String[] args) {
        // a)
        double[] array = { 1.1, 2.2, 3.3, 4.4, 5.5 };

        // b)
        ArrayList<Double> arrayList = new ArrayList<>();
        ArrayList<Double> verdoppelteWerte = new ArrayList<>();

        for (double wert : array) {
            arrayList.add(wert);
        }

        // c)
        for (int i = 0; i < arrayList.size(); i++) {
            verdoppelteWerte.add(arrayList.get(i) * 2);
        }

        // d)
        System.out.println("ArrayList vor der Verarbeitung:");
        System.out.println(arrayList);
        System.out.println("ArrayList nach der Verarbeitung:");
        System.out.println(verdoppelteWerte);
    }
}
