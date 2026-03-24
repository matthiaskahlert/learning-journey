package Caesar;

import java.util.Map;
import java.util.Scanner;

/**
 * Caesar-Chiffre Hauptanwendung mit CLI-Menü.
 * Benutzer kann zwischen Verschlüsseln, Entschlüsseln und Brute-Force wählen.
 */
public class CaesarApp {

    private static final Scanner scanner = new Scanner(System.in);
    private static boolean running = true;

    public static void main(String[] args) {
        System.out.println("\n");
        System.out.println("╔════════════════════════════════════════╗");
        System.out.println("║    CAESAR-CHIFFRE KRYPTOGRAPHIE       ║");
        System.out.println("║    Verschlüsseln. Entschlüsseln. Brute ║");
        System.out.println("╚════════════════════════════════════════╝\n");

        while (running) {
            showMenu();
            String choice = getUserInput("Wahl: ");

            switch (choice.trim()) {
                case "1" -> handleEncrypt();
                case "2" -> handleDecrypt();
                case "3" -> handleBruteForce();
                case "4" -> {
                    System.out.println("\n✅ Auf Wiedersehen!\n");
                    running = false;
                }
                default -> System.out.println("❌ Ungültige Eingabe. Bitte 1-4 wählen.\n");
            }
        }

        scanner.close();
    }

    /**
     * Zeigt das Hauptmenü an.
     */
    private static void showMenu() {
        System.out.println("═══ HAUPTMENÜ ═══");
        System.out.println("1. 🔐 Verschlüsseln");
        System.out.println("2. 🔓 Entschlüsseln");
        System.out.println("3. 🔑 Brute-Force (alle 25 Varianten)");
        System.out.println("4. 🚪 Beenden");
        System.out.println();
    }

    /**
     * Behandelt die Verschlüsselung.
     */
    private static void handleEncrypt() {
        System.out.println("\n--- VERSCHLÜSSELN ---");

        String text = getUserInput("Text eingeben: ");
        if (text.isEmpty()) {
            System.out.println("❌ Text darf nicht leer sein.\n");
            return;
        }

        int shift = getShiftInput();
        if (shift == -1)
            return;

        try {
            String encrypted = CaesarCipher.encrypt(text, shift);
            System.out.println("\n✅ Verschlüsselt:");
            System.out.println("   Eingabe:       " + text);
            System.out.println("   Verschiebung: " + shift);
            System.out.println("   Ergebnis:      " + encrypted + "\n");
        } catch (IllegalArgumentException e) {
            System.out.println("❌ Fehler: " + e.getMessage() + "\n");
        }
    }

    /**
     * Behandelt die Entschlüsselung.
     */
    private static void handleDecrypt() {
        System.out.println("\n--- ENTSCHLÜSSELN ---");

        String text = getUserInput("Text eingeben: ");
        if (text.isEmpty()) {
            System.out.println("❌ Text darf nicht leer sein.\n");
            return;
        }

        int shift = getShiftInput();
        if (shift == -1)
            return;

        try {
            String decrypted = CaesarCipher.decrypt(text, shift);
            System.out.println("\n✅ Entschlüsselt:");
            System.out.println("   Eingabe:       " + text);
            System.out.println("   Verschiebung: " + shift);
            System.out.println("   Ergebnis:      " + decrypted + "\n");
        } catch (IllegalArgumentException e) {
            System.out.println("❌ Fehler: " + e.getMessage() + "\n");
        }
    }

    /**
     * Behandelt die Brute-Force-Analyse.
     */
    private static void handleBruteForce() {
        System.out.println("\n--- BRUTE-FORCE ANALYSE ---");

        String text = getUserInput("Text eingeben: ");
        if (text.isEmpty()) {
            System.out.println("❌ Text darf nicht leer sein.\n");
            return;
        }

        System.out.println("\n🔄 Berechne alle 25 Varianten mit Multithreading...");

        // Performance messen
        long startTime = System.currentTimeMillis();
        Map<Integer, String> results = CaesarBruteForce.bruteForce(text);
        long endTime = System.currentTimeMillis();

        System.out.println(CaesarBruteForce.formatResults(results));
        System.out.println("⏱️  Berechnung dauerte: " + (endTime - startTime) + " ms\n");
    }

    /**
     * Fragt den Benutzer nach einer gültigen Verschiebung (1-25).
     * 
     * @return Die Verschiebung oder -1 bei Fehler
     */
    private static int getShiftInput() {
        try {
            String input = getUserInput("Verschiebung (1-25): ");
            int shift = Integer.parseInt(input.trim());

            if (!CaesarCipher.isValidShift(shift)) {
                System.out.println("❌ Verschiebung muss zwischen 1 und 25 liegen.\n");
                return -1;
            }

            return shift;
        } catch (NumberFormatException e) {
            System.out.println("❌ Bitte eine ganze Zahl eingeben.\n");
            return -1;
        }
    }

    /**
     * Hilfsmethode zum Einlesen von Benutzer-Input.
     * 
     * @param prompt Die Aufforderung
     * @return Die Benutzereingabe
     */
    private static String getUserInput(String prompt) {
        System.out.print(prompt);
        return scanner.nextLine();
    }
}
