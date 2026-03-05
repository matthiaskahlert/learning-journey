/* Erstelle eine Java-Funktion berechneKreisflaeche, die den Flächeninhalt eines Kreises berechnet. 
Die Funktion soll den Radius als Parameter erhalten und den berechneten Flächeninhalt als Rückgabewert vom Typ double liefern. 
Verwende dafür die Konstante Math.PI für die Zahl Pi. Implementiere anschließend ein Hauptprogramm, 
in dem die Funktion berechneKreisflaeche zweimal aufgerufen wird: einmal mit dem Radius 5 und einmal mit dem Radius 7.5. 
Speichere die Ergebnisse in zwei verschiedenen Variablen und gib diese anschließend auf der Konsole aus. 
Kommentiere deinen Code, um die Funktionsweise zu erklären. 
 */
public class Uebung_5_3_Ue_01 {

    // Funktion zur Berechnung der Kreisfläche
    public static double berechneKreisflaeche(double radius) {
        return Math.PI * radius * radius;
    }

    public static void main(String[] args) {
        // Aufruf der Funktion mit Radius 5
        double flaeche1 = berechneKreisflaeche(5);
        System.out.println("Fläche des Kreises mit Radius 5: " + flaeche1);

        // Aufruf der Funktion mit Radius 7.5
        double flaeche2 = berechneKreisflaeche(7.5);
        System.out.println("Fläche des Kreises mit Radius 7.5: " + flaeche2);
    }
}
