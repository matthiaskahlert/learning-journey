package Caesar;

/**
 * Unit-Tests für Caesar-Chiffre
 */
public class CaesarTest {

    public static void main(String[] args) {
        System.out.println("\n╔════════════════════════════════════════╗");
        System.out.println("║  CAESAR-CHIFFRE TEST-SUITE             ║");
        System.out.println("╚════════════════════════════════════════╝\n");

        int passed = 0;
        int failed = 0;

        // Test 1: Einfache Verschlüsselung
        if (testEncrypt("hello", 5, "mjqqt")) {
            System.out.println("✅ Test 1: Einfache Verschlüsselung");
            passed++;
        } else {
            System.out.println("❌ Test 1 FEHLER");
            failed++;
        }

        // Test 2: Großbuchstaben
        if (testEncrypt("HELLO", 5, "MJQQT")) {
            System.out.println("✅ Test 2: Großbuchstaben");
            passed++;
        } else {
            System.out.println("❌ Test 2 FEHLER");
            failed++;
        }

        // Test 3: Gemischte Fall
        if (testEncrypt("Hello World", 3, "Khoor Zruog")) {
            System.out.println("✅ Test 3: Gemischte Groß-/Kleinschreibung");
            passed++;
        } else {
            System.out.println("❌ Test 3 FEHLER");
            failed++;
        }

        // Test 4: Wrap-around (xyz + 3 = abc)
        if (testEncrypt("xyz", 3, "abc")) {
            System.out.println("✅ Test 4: Wrap-around am Alphabetende");
            passed++;
        } else {
            System.out.println("❌ Test 4 FEHLER");
            failed++;
        }

        // Test 5: Nicht-Buchstaben bleiben unverändert
        if (testEncrypt("abc123!@", 1, "bcd123!@")) {
            System.out.println("✅ Test 5: Nicht-Buchstaben bleiben unverändert");
            passed++;
        } else {
            System.out.println("❌ Test 5 FEHLER");
            failed++;
        }

        // Test 6: Entschlüsselung (mjqqt mit shift 5 wurde mit hello verschlüsselt)
        if (testDecrypt("mjqqt", 5, "hello")) {
            System.out.println("✅ Test 6: Entschlüsselung");
            passed++;
        } else {
            System.out.println("❌ Test 6 FEHLER");
            failed++;
        }

        // Test 7: Ungültige Verschiebung
        if (testInvalidShift()) {
            System.out.println("✅ Test 7: Ungültige Verschiebung (0)");
            passed++;
        } else {
            System.out.println("❌ Test 7 FEHLER");
            failed++;
        }

        // Test 8: Ungültige Verschiebung (zu groß)
        if (testInvalidShift26()) {
            System.out.println("✅ Test 8: Ungültige Verschiebung (26)");
            passed++;
        } else {
            System.out.println("❌ Test 8 FEHLER");
            failed++;
        }

        // Test 9: Brute-Force gibt 25 Ergebnisse
        if (testBruteForce("test")) {
            System.out.println("✅ Test 9: Brute-Force liefert 25 Varianten");
            passed++;
        } else {
            System.out.println("❌ Test 9 FEHLER");
            failed++;
        }

        // Test 10: Round-Trip (Verschlüsseln + Entschlüsseln = Original)
        if (testRoundTrip("test", 7)) {
            System.out.println("✅ Test 10: Round-Trip Verschlüsseln-Entschlüsseln");
            passed++;
        } else {
            System.out.println("❌ Test 10 FEHLER");
            failed++;
        }

        System.out.println("\n" + "=".repeat(50));
        System.out.println("ERGEBNIS: " + passed + " bestanden, " + failed + " fehlgeschlagen");
        System.out.println("=".repeat(50) + "\n");
    }

    private static boolean testEncrypt(String text, int shift, String expected) {
        try {
            String result = CaesarCipher.encrypt(text, shift);
            return result.equals(expected);
        } catch (Exception e) {
            return false;
        }
    }

    private static boolean testDecrypt(String text, int shift, String expected) {
        try {
            String result = CaesarCipher.decrypt(text, shift);
            return result.equals(expected);
        } catch (Exception e) {
            return false;
        }
    }

    private static boolean testInvalidShift() {
        try {
            CaesarCipher.encrypt("test", 0);
            return false; // Sollte Exception werfen
        } catch (IllegalArgumentException e) {
            return true;
        }
    }

    private static boolean testInvalidShift26() {
        try {
            CaesarCipher.encrypt("test", 26);
            return false; // Sollte Exception werfen
        } catch (IllegalArgumentException e) {
            return true;
        }
    }

    private static boolean testBruteForce(String text) {
        try {
            java.util.Map<Integer, String> results = CaesarBruteForce.bruteForce(text);
            return results.size() == 25;
        } catch (Exception e) {
            return false;
        }
    }

    private static boolean testRoundTrip(String text, int shift) {
        try {
            String encrypted = CaesarCipher.encrypt(text, shift);
            String decrypted = CaesarCipher.decrypt(encrypted, shift);
            return decrypted.equals(text);
        } catch (Exception e) {
            return false;
        }
    }
}
