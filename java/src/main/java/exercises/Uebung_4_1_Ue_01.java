import java.util.Scanner;

/**
 * Übung 4.1 - Ue.01: Tierkategorisierung
 * 
 * Programm zur Klassifizierung von Tieren basierend auf:
 * - Tiertyp (Säugetier, Vogel, Reptil, Fisch, Amphibie, Insekt)
 * - Durchschnittliche Lebensdauer in Jahren
 * - Flugfähigkeit (ja/nein)
 * 
 * Ausgabe:
 * - Lebensklasse: kurzlebig (≤2 Jahre), mittellebig (>2, ≤10 Jahre), langlebig (>10 Jahre)
 * - Flugfähigkeit: flugfähig oder nicht flugfähig
 */
public class Uebung_4_1_Ue_01 {
    
    public static void main(String[] args) {
        // a) BENUTZEREINGABE - Scanner initialisieren
        Scanner scanner = new Scanner(System.in);
        
        // Eingaben speichern in Variablen
        System.out.println("=== Tierkategorisierung ===\n");
        
        // Tiertyp eingeben
        System.out.print("Tiertyp eingeben (Säugetier/Vogel/Reptil/Fisch/Amphibie/Insekt): ");
        String tiertyp = scanner.nextLine();
        
        // Lebensdauer eingeben
        System.out.print("Durchschnittliche Lebensdauer in Jahren eingeben: ");
        double lebensdauer = scanner.nextDouble();
        
        // Flugfähigkeit eingeben
        System.out.print("Kann das Tier fliegen? (ja/nein): ");
        String flugfaehigkeit = scanner.next();
        
        // Scanner schließen
        scanner.close();
        
        System.out.println("\n=== Klassifizierungsergebnis ===\n");
        
        // b) KLASSIFIZIERUNG DER LEBENSDAUER
        String lebensklasse;
        
        if (lebensdauer <= 2) {
            lebensklasse = "kurzlebig";
        } else if (lebensdauer > 2 && lebensdauer <= 10) {
            lebensklasse = "mittellebig";
        } else {
            lebensklasse = "langlebig";
        }
        
        System.out.println("Tiertyp: " + tiertyp);
        System.out.println("Lebensdauer: " + lebensdauer + " Jahre");
        System.out.println("Lebensklasse: " + lebensklasse);
        
        // c) ÜBERPRÜFUNG DER FLUGFÄHIGKEIT
        String flugstatus;
        
        if (flugfaehigkeit.equalsIgnoreCase("ja")) {
            flugstatus = "flugfähig";
        } else if (flugfaehigkeit.equalsIgnoreCase("nein")) {
            flugstatus = "nicht flugfähig";
        } else {
            flugstatus = "ungültige Eingabe";
        }
        
        System.out.println("Flugfähigkeit: " + flugstatus);
        
        // Zusammenfassung
        System.out.println("\n=== Zusammenfassung ===");
        System.out.println("Das Tier ist ein " + tiertyp + ", das " + lebensklasse + 
                          " ist und " + flugstatus + ".");
    }
}