package Caesar;

public class DebugDecrypt {
    public static void main(String[] args) {
        System.out.println("\n=== DECRYPT DEBUG ===\n");

        // Test 1: hello mit 5 verschlüsselt
        String encrypted = CaesarCipher.encrypt("hello", 5);
        System.out.println("Encrypted 'hello' mit shift 5: " + encrypted);

        String decrypted = CaesarCipher.decrypt(encrypted, 5);
        System.out.println("Decrypted mit shift 5: " + decrypted);
        System.out.println("Erwartet: hello");
        System.out.println("Match: " + decrypted.equals("hello") + "\n");

        // Test 2: khoor manuell mit 5 entschlüsseln
        String manual = "khoor";
        System.out.println("Manual decrypt 'khoor' mit shift 5:");
        String result = CaesarCipher.decrypt(manual, 5);
        System.out.println("Ergebnis: " + result);
        System.out.println("Match with 'hello': " + result.equals("hello") + "\n");

        // Test 3: Original-Beispiel
        System.out.println("Original-Beispiel 'uhlDAReHHw' mit shift 5:");
        String orig = "uhlDAReHHw";
        String origDecrypt = CaesarCipher.decrypt(orig, 5);
        System.out.println("Decrypted: " + origDecrypt);

        // Auch encrypt testen
        String origEncrypt = CaesarCipher.encrypt(orig, 5);
        System.out.println("Encrypted: " + origEncrypt + "\n");
    }
}
